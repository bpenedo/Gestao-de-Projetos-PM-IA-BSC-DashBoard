"""
Telas do Budget Global de tokens para os READMEs (12 idiomas):

  1. donut do burn de tokens  — Budget Global utilizado por projeto
  2. subsídio cruzado         — quem banca quem, em R$/mês
  3. contenção precificada    — algozes × vítimas (a cadeia causal do PORTFÓLIO)
  4. política de corte        — % do pool liberado × % do valor sacrificado

Decisões de visualização:
  · o donut é a ÚNICA fatia legítima de um todo (o pool é 100% e finito).
  · subsídio e saldo são DIVERGENTES (positivo/negativo com zero significativo) → dois polos
    + zero neutro. Nunca arco-íris, nunca hue no meio.
  · a política de corte é um scatter (dois eixos comparáveis), com a diagonal y=x separando
    "corte que compensa" de "corte que destrói mais do que libera".
  · nenhuma cor sozinha carrega identidade: tudo leva rótulo.

Saída: ../../docs/screenshots/*.png

Uso:  python3 gerar_orcamento_telas.py
Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from db import get_conn
from config import FOUNDATIONS_DIR

SHOTS = FOUNDATIONS_DIR.parent / "docs" / "screenshots"
SHOTS.mkdir(parents=True, exist_ok=True)

FUNDO = "#D9D9D9"
AZUL, VERDE, VERMELHO, LARANJA = "#1F77B4", "#2CA02C", "#D62728", "#E8A33D"
TINTA, TINTA2 = "#1A1A1A", "#5A5A5A"


def _base(ax):
    ax.set_facecolor(FUNDO)
    ax.grid(alpha=0.25, color="white", linewidth=0.8)
    ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(TINTA2)


def donut(conn):
    rows = conn.execute(
        "SELECT project_name, tokens_mes, eficiencia FROM orcamento_rateio "
        "ORDER BY tokens_mes DESC").fetchall()
    g = conn.execute("SELECT tokens_contratados, consumo_run_rate, desperdicio_rr "
                     "FROM orcamento_global").fetchone()
    quota, cons, desp = g
    nomes = [r[0].split()[-1] for r in rows]
    val = [r[1] for r in rows]
    efic = [r[2] for r in rows]

    # Magnitude sequencial: quem tem PIOR eficiência fica mais escuro (chama atenção).
    mx = max(efic) or 1
    cores = [plt.cm.Blues(0.85 - 0.55 * (e / mx)) for e in efic]

    fig, ax = plt.subplots(figsize=(11, 7.2))
    w, t, a = ax.pie(
        val, labels=nomes, colors=cores, startangle=90, counterclock=False,
        autopct=lambda p: f"{p:.1f}%", pctdistance=0.80,
        wedgeprops=dict(width=0.42, edgecolor="white", linewidth=2),
        textprops=dict(fontsize=10, color=TINTA))
    for x in a:
        x.set_fontsize(9)
        x.set_fontweight("bold")

    ax.text(0, 0.12, f"{cons/1e6:,.0f}M", ha="center", fontsize=26,
            fontweight="bold", color=TINTA)
    ax.text(0, -0.06, "tokens/mês", ha="center", fontsize=11, color=TINTA2)
    ax.text(0, -0.24, f"{cons/quota:.0%} da quota\ncontratada", ha="center",
            fontsize=10, color=TINTA2)
    ax.set_title("Budget Global utilizado por projeto — ótica do Burn Token Rate\n"
                 "cada fatia NÃO é 'o custo dele': é a capacidade que ele retira dos OUTROS\n"
                 f"(tom mais escuro = pior eficiência · {desp/1e6:.0f}M/mês do total é "
                 f"DESPERDÍCIO em chamadas que falharam)",
                 fontsize=12, fontweight="bold", color=TINTA, pad=18)
    fig.tight_layout()
    fig.savefig(SHOTS / "budget-donut-burn-token.png", dpi=130, facecolor="white")
    plt.close(fig)
    return "budget-donut-burn-token.png"


def subsidio(conn):
    rows = conn.execute(
        "SELECT project_name, subsidio_brl, eficiencia, papel FROM orcamento_rateio "
        "ORDER BY subsidio_brl").fetchall()
    nomes = [r[0].split()[-1] for r in rows]
    sub = [r[1] for r in rows]
    efic = [r[2] for r in rows]
    # DIVERGENTE: dois polos + zero neutro. Vermelho = é subsidiado; verde = paga a conta.
    cores = [VERMELHO if s > 0 else VERDE for s in sub]

    fig, ax = plt.subplots(figsize=(11, 6))
    _base(ax)
    ax.barh(nomes, sub, color=cores, edgecolor="white", linewidth=1.5, height=0.7)
    ax.axvline(0, color=TINTA, lw=2)
    lim = max(abs(min(sub)), abs(max(sub)))
    for i, (s, e) in enumerate(zip(sub, efic)):
        lbl = f"R$ {s:+,.0f}  ({e:.0f} EV/Mtok)"
        ax.text(s + (lim * 0.03 if s >= 0 else -lim * 0.03), i, lbl, va="center",
                ha="left" if s >= 0 else "right", fontsize=9, color=TINTA)
    ax.set_xlim(-lim * 1.75, lim * 1.75)
    ax.text(lim * 0.9, len(nomes) - 0.4, "◀ É SUBSIDIADO\n(consome mais do que entrega)",
            fontsize=10, color="#8B1A1A", fontweight="bold", ha="center")
    ax.text(-lim * 0.9, 0.4, "PAGA A CONTA DOS OUTROS ▶\n(entrega mais do que consome)",
            fontsize=10, color="#1B5E20", fontweight="bold", ha="center")
    ax.set_xlabel("subsídio cruzado (R$/mês) — cota por CONSUMO menos cota por VALOR entregue",
                  color=TINTA)
    ax.set_title("Quem banca quem — o subsídio cruzado do pool de tokens\n"
                 "ratear por CONSUMO é auto-justificante: premia quem queima. "
                 "O rateio honesto é por VALOR ENTREGUE.",
                 fontsize=12, fontweight="bold", color=TINTA)
    fig.tight_layout()
    fig.savefig(SHOTS / "budget-subsidio-cruzado.png", dpi=130, facecolor="white")
    plt.close(fig)
    return "budget-subsidio-cruzado.png"


def contencao(conn):
    rows = conn.execute(
        "SELECT project_name, custo_sofrido, culpa_rs, saldo, papel, eficiencia "
        "FROM contencao_projeto ORDER BY saldo").fetchall()
    nomes = [r[0].split()[-1] for r in rows]
    sofre = [-r[1] for r in rows]          # negativo: é o que ele PERDE
    causa = [r[2] for r in rows]           # positivo: o dano que ele CAUSA aos outros
    saldo = [r[3] for r in rows]
    # O papel vem do BANCO, não é recalculado aqui. Recalcular abriria divergência entre o
    # gráfico e o dashboard — e um gráfico que discorda da tabela é um gráfico que mente.
    papel = [r[4] for r in rows]
    efic = [r[5] for r in rows]

    fig, ax = plt.subplots(figsize=(11.5, 6.2))
    _base(ax)
    y = np.arange(len(nomes))
    ax.barh(y, causa, color=VERMELHO, edgecolor="white", linewidth=1.5, height=0.62,
            label="dano que ELE CAUSA aos outros")
    ax.barh(y, sofre, color=AZUL, edgecolor="white", linewidth=1.5, height=0.62,
            label="dano que ELE SOFRE")
    ax.set_yticks(y)
    ax.set_yticklabels(nomes)
    ax.axvline(0, color=TINTA, lw=2)
    lim = max(max(causa), abs(min(sofre)))
    for i, (s, e, pa) in enumerate(zip(saldo, efic, papel)):
        ax.text(lim * 1.10, i, f"saldo R$ {s:+,.0f}  ·  {e:.0f} EV/Mtok  ·  {pa}",
                va="center", fontsize=9, color=TINTA,
                fontweight="bold" if pa == "ALGOZ" else "normal")
    ax.set_xlim(-lim * 1.25, lim * 2.55)
    ax.set_ylim(-0.8, len(nomes) - 0.2)
    ax.legend(frameon=False, loc="upper right", bbox_to_anchor=(1.0, 1.02))
    ax.set_xlabel("R$ no cenário de estrangulamento do pool (+25% de consumo)", color=TINTA)
    ax.set_title("Contenção de recurso PRECIFICADA — a cadeia causal do PORTFÓLIO\n"
                 "o excedente de um esgota o pool → estrangula os OUTROS → o P80 DELES escorrega "
                 "→ o Cost of Delay DELES cobra a conta\n"
                 "⚠️ CENÁRIO, não estado atual: hoje o pool ainda cabe, e nada disso está acontecendo",
                 fontsize=11.5, fontweight="bold", color=TINTA)
    fig.tight_layout()
    fig.savefig(SHOTS / "budget-contencao.png", dpi=130, facecolor="white")
    plt.close(fig)
    return "budget-contencao.png"


def corte(conn):
    rows = conn.execute(
        "SELECT project_name, pct_pool_liberado, pct_valor_perdido, eficiencia, ordem_corte "
        "FROM admissao_politica ORDER BY ordem_corte").fetchall()
    fig, ax = plt.subplots(figsize=(10.5, 7))
    _base(ax)
    lim = max(max(r[1] for r in rows), max(r[2] for r in rows)) * 1.25

    # A diagonal y = x separa o corte que COMPENSA do que DESTRÓI.
    ax.plot([0, lim], [0, lim], color=TINTA2, ls="--", lw=2)
    ax.fill_between([0, lim], [0, lim], 0, color=VERDE, alpha=0.12)
    ax.fill_between([0, lim], [0, lim], lim, color=VERMELHO, alpha=0.12)
    ax.text(lim * 0.72, lim * 0.14, "CORTAR COMPENSA\nlibera mais pool\ndo que sacrifica valor",
            fontsize=10, color="#1B5E20", fontweight="bold", ha="center")
    ax.text(lim * 0.24, lim * 0.80, "NÃO CORTE\ndestrói mais valor\ndo que libera capacidade",
            fontsize=10, color="#8B1A1A", fontweight="bold", ha="center")

    for p, pool, val, ef, o in rows:
        c = VERDE if pool > val else VERMELHO
        ax.scatter(pool, val, s=170, color=c, edgecolor="white", linewidth=2, zorder=5)
        ax.annotate(f"{p.split()[-1]} ({ef:.0f})", (pool, val), xytext=(0, 13),
                    textcoords="offset points", ha="center", fontsize=9,
                    color=TINTA, fontweight="bold")
    ax.set_xlim(0, lim); ax.set_ylim(0, lim)
    ax.xaxis.set_major_formatter(lambda v, _: f"{v:.0%}")
    ax.yaxis.set_major_formatter(lambda v, _: f"{v:.0%}")
    ax.set_xlabel("% do POOL que se LIBERA ao cortar o projeto", color=TINTA)
    ax.set_ylabel("% do VALOR que se SACRIFICA ao cortar o projeto", color=TINTA)
    ax.set_title("Política de corte — quem sai, se o portfólio precisa de espaço?\n"
                 "a resposta NÃO é 'o que gasta mais' — é 'o que entrega menos POR TOKEN'\n"
                 "(entre parênteses: EV por milhão de tokens)",
                 fontsize=12, fontweight="bold", color=TINTA)
    fig.tight_layout()
    fig.savefig(SHOTS / "budget-politica-corte.png", dpi=130, facecolor="white")
    plt.close(fig)
    return "budget-politica-corte.png"


def main():
    conn = get_conn()
    print("🖼️  Telas do Budget Global para os 12 READMEs")
    for f in (donut(conn), subsidio(conn), contencao(conn), corte(conn)):
        print(f"   ✅ docs/screenshots/{f}")
    conn.close()


if __name__ == "__main__":
    main()
