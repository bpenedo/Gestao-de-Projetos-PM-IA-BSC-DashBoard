"""
Gráficos das duas simulações a montante:

  1. AJUSTE DE DISTRIBUIÇÕES aos tokens reais ("Fit distributions to data", SimulAr p.67):
     histograma dos tokens observados com a densidade da distribuição vencedora
     sobreposta, mais o ranking das candidatas por AIC.

  2. ROBUSTEZ DO RANKING (perturbação de Dirichlet nos pesos do DEMATEL):
     probabilidade de cada projeto vencer o consenso, e a divergência entre as
     escolas de decisão sobre o líder.

Saída: ../evidence/static/mc/  (dados anônimos: Project A..J)
Uso:  python3 gerar_robustez_graficos.py
Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
"""
import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

from db import get_conn
from config import FOUNDATIONS_DIR

STATIC = FOUNDATIONS_DIR / "evidence" / "static" / "mc"
ROXO, VERMELHO, VERDE = "#8E44AD", "#c0392b", "#1f9d55"


def ajuste_tokens(conn, projeto):
    linhas = conn.execute("""SELECT distribuicao, parametros, aic, ks_stat, ks_pvalue, escolhida
                             FROM mc_ajuste_distribuicao
                             WHERE project_name=? AND variavel='TOKENS' ORDER BY rank_""",
                          (projeto,)).fetchall()
    if not linhas:
        return None
    tokens = np.array([r[0] for r in conn.execute(
        "SELECT prompt_tokens + completion_tokens FROM logs_langfuse WHERE project_name=?",
        (projeto,))], float)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.4, 4.9), gridspec_kw={"width_ratios": [1.35, 1]})

    # --- Esquerda: dados observados + densidade ajustada
    vencedora = linhas[0]
    d = json.loads(vencedora["parametros"])
    ax1.hist(tokens, bins=32, density=True, color="#b8c4d0", edgecolor="#5a6b7d",
             linewidth=0.5, label=f"tokens observados (n={tokens.size})")
    xs = np.linspace(tokens.min(), tokens.max(), 400)
    pdf = getattr(stats, d["scipy"]).pdf(xs, *d["params"])
    ax1.plot(xs, pdf, color=VERMELHO, lw=2.6,
             label=f"{vencedora['distribuicao']} ajustada (MLE)")
    aderiu = vencedora["ks_pvalue"] >= 0.05
    ax1.set_title(f"Distribuição ajustada aos tokens reais — {projeto}\n"
                  f"vencedora por AIC: {vencedora['distribuicao']}  ·  "
                  f"KS p={vencedora['ks_pvalue']:.3f} "
                  f"({'aderência plausível' if aderiu else 'ADERÊNCIA FRACA'})",
                  fontsize=11.5, fontweight="bold",
                  color="black" if aderiu else VERMELHO)
    ax1.set_xlabel("Tokens por geração (prompt + completion)", fontsize=10)
    ax1.set_ylabel("Densidade", fontsize=10)
    ax1.legend(fontsize=9)
    ax1.grid(alpha=0.25, linestyle=":")
    ax1.set_axisbelow(True)

    # --- Direita: ranking das candidatas por AIC
    nomes = [r["distribuicao"] for r in linhas][::-1]
    aics = [r["aic"] for r in linhas][::-1]
    cores = [VERDE if r["escolhida"] else "#9aa7b4" for r in linhas][::-1]
    ax2.barh(range(len(nomes)), aics, color=cores, edgecolor="white", height=0.7)
    ax2.set_yticks(range(len(nomes)))
    ax2.set_yticklabels(nomes, fontsize=9)
    ax2.set_xlim(min(aics) * 0.985, max(aics) * 1.004)
    ax2.set_xlabel("AIC = 2k − 2·log L   (menor é melhor)", fontsize=10)
    ax2.set_title(f"{len(nomes)} candidatas ajustadas por máxima verossimilhança\n"
                  "(verde = escolhida; a penalização por parâmetro evita sobreajuste)",
                  fontsize=11, fontweight="bold")
    ax2.grid(axis="x", alpha=0.25, linestyle=":")
    ax2.set_axisbelow(True)

    fig.tight_layout()
    caminho = STATIC / "ajuste_distribuicoes.png"
    fig.savefig(caminho, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return caminho


def robustez(conn):
    cons = conn.execute("""SELECT project_name, prob_vitoria, rank_medio, rank_p05, rank_p95
                           FROM mcdm_robustez WHERE metodo='CONSENSO (Borda)'
                           ORDER BY prob_vitoria DESC""").fetchall()
    if not cons:
        return None
    lider = cons[0]["project_name"]
    metodos = conn.execute("""SELECT metodo, prob_vitoria FROM mcdm_robustez
                              WHERE project_name=? AND metodo<>'CONSENSO (Borda)'
                              ORDER BY prob_vitoria DESC""", (lider,)).fetchall()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.4, 5.0), gridspec_kw={"width_ratios": [1.25, 1]})

    # --- Esquerda: probabilidade de vencer o consenso
    nomes = [r["project_name"] for r in cons][::-1]
    probs = [r["prob_vitoria"] for r in cons][::-1]
    cores = [ROXO if p > 0.05 else "#d5d9de" for p in probs]
    ax1.barh(range(len(nomes)), probs, color=cores, edgecolor="white", height=0.72)
    for i, p in enumerate(probs):
        if p > 0.05:
            ax1.text(p + 1.2, i, f"{p:.1f}%", va="center", fontsize=9.5, fontweight="bold", color=ROXO)
    ax1.set_yticks(range(len(nomes)))
    ax1.set_yticklabels(nomes, fontsize=9.5)
    ax1.set_xlim(0, 108)
    ax1.set_xlabel("% dos universos de preferência em que o projeto vence", fontsize=10)
    ax1.set_title("Robustez da decisão — perturbação de Dirichlet nos pesos\n"
                  "w′ ~ Dir(κ·w),  κ=200,  2.000 universos  ·  E[w′] = w (não enviesa)",
                  fontsize=11.5, fontweight="bold")
    ax1.grid(axis="x", alpha=0.25, linestyle=":")
    ax1.set_axisbelow(True)

    # --- Direita: concordância entre escolas sobre o líder
    m_nomes = [r["metodo"] for r in metodos][::-1]
    m_probs = [r["prob_vitoria"] for r in metodos][::-1]
    m_cores = [VERDE if p >= 60 else (VERMELHO if p < 40 else "#e0a52b") for p in m_probs]
    ax2.barh(range(len(m_nomes)), m_probs, color=m_cores, edgecolor="white", height=0.68)
    for i, p in enumerate(m_probs):
        ax2.text(p + 1.5, i, f"{p:.1f}%", va="center", fontsize=9.5, fontweight="bold")
    ax2.set_yticks(range(len(m_nomes)))
    ax2.set_yticklabels(m_nomes, fontsize=9.5)
    ax2.set_xlim(0, 118)
    ax2.axvline(50, color="black", lw=0.9, linestyle="--", alpha=0.6)
    ax2.set_xlabel("% dos universos em que o método elege o líder", fontsize=10)
    ax2.set_title(f"Concordância entre escolas sobre o líder ({lider})\n"
                  "vermelho = a escola discorda; o consenso estava mascarando a divergência",
                  fontsize=11, fontweight="bold")
    ax2.grid(axis="x", alpha=0.25, linestyle=":")
    ax2.set_axisbelow(True)

    fig.tight_layout()
    caminho = STATIC / "robustez_dirichlet.png"
    fig.savefig(caminho, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return caminho


def main():
    STATIC.mkdir(parents=True, exist_ok=True)
    conn = get_conn()
    linha = conn.execute("SELECT project_name FROM decisao_consenso ORDER BY rank_final LIMIT 1").fetchone()
    projeto = linha[0] if linha else "Project A"
    gerados = [c for c in (ajuste_tokens(conn, projeto), robustez(conn)) if c]
    conn.close()
    for c in gerados:
        print(f"  🖼️  {c.relative_to(FOUNDATIONS_DIR)}")
    print(f"\n✅ {len(gerados)} gráficos (ajuste de distribuições + robustez do ranking).")


if __name__ == "__main__":
    main()
