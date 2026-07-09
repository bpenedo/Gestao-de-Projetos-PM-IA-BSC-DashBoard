"""
Gráficos da decisão multicritério integrada (DEMATEL → ELECTRE · PROMETHEE · MAUT · MCDA-C).

  1. Diagrama causa–efeito do DEMATEL: proeminência (R+C) no eixo X e relação (R-C)
     no eixo Y. Acima da linha y=0 estão as CAUSAS (alavancas); abaixo, os EFEITOS.
     O tamanho do ponto é proporcional ao peso derivado do critério.
  2. Mapa de posições por método: matriz projetos × métodos com a posição de cada
     projeto, evidenciando concordâncias e divergências entre as escolas de decisão.

Saída: ../evidence/static/mc/  (dados anônimos: Project A..J)
Uso:  python3 gerar_mcdm_graficos.py
Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from db import get_conn
from config import FOUNDATIONS_DIR

STATIC = FOUNDATIONS_DIR / "evidence" / "static" / "mc"
CAUSA, EFEITO = "#c0392b", "#1f77b4"


def diagrama_causa_efeito(conn):
    linhas = conn.execute("""SELECT rotulo, prominencia, relacao, papel, peso
                             FROM dematel_criterio ORDER BY prominencia DESC""").fetchall()
    if not linhas:
        return None
    x = np.array([r["prominencia"] for r in linhas])
    y = np.array([r["relacao"] for r in linhas])
    pesos = np.array([r["peso"] for r in linhas])
    cores = [CAUSA if r["papel"] == "causa" else EFEITO for r in linhas]

    fig, ax = plt.subplots(figsize=(8.8, 5.6))
    ax.axhline(0, color="black", lw=1.1)
    ax.scatter(x, y, s=pesos * 3200, c=cores, alpha=0.85, edgecolors="white", linewidths=1.3, zorder=3)

    # Rótulos SEMPRE fora do círculo, com linha de chamada. Para cada ponto testamos
    # offsets candidatos e ficamos com o primeiro que não colide com um rótulo já posto
    # (distância medida em pontos de tela) — critérios próximos continuam legíveis.
    candidatos = [(0, 26), (0, -30), (34, 12), (-34, 12), (34, -18), (-34, -18), (46, 30), (-46, 30)]
    postos = []
    trans = ax.transData
    for i, (r, xi, yi) in enumerate(zip(linhas, x, y)):
        px, py = trans.transform((xi, yi))
        for dx, dy in candidatos:
            alvo = (px + dx, py + dy)
            if all((alvo[0] - a) ** 2 + (alvo[1] - b) ** 2 > 62 ** 2 for a, b in postos):
                break
        postos.append(alvo)
        ax.annotate(f"{r['rotulo']}  {r['peso']*100:.1f}%", (xi, yi),
                    xytext=(dx, dy), textcoords="offset points",
                    fontsize=9, fontweight="bold", ha="center", va="center", color=cores[i], zorder=5,
                    bbox=dict(boxstyle="round,pad=0.28", fc="white", ec=cores[i], lw=0.9, alpha=0.95),
                    arrowprops=dict(arrowstyle="-", color=cores[i], lw=1.0, shrinkA=0, shrinkB=4))

    faixa = max(abs(y).max(), 0.1) * 1.35
    ax.set_ylim(-faixa, faixa)
    ax.fill_between(ax.get_xlim(), 0, faixa, color=CAUSA, alpha=0.05, zorder=0)
    ax.fill_between(ax.get_xlim(), -faixa, 0, color=EFEITO, alpha=0.05, zorder=0)
    ax.text(0.985, 0.965, "CAUSAS — alavancas: aja aqui", transform=ax.transAxes, ha="right",
            fontsize=9.5, fontweight="bold", color=CAUSA)
    ax.text(0.985, 0.03, "EFEITOS — termômetros: resultado do que já foi feito", transform=ax.transAxes,
            ha="right", fontsize=9.5, fontweight="bold", color=EFEITO)

    ax.set_xlabel("Proeminência  R + C  (importância no sistema)", fontsize=10.5)
    ax.set_ylabel("Relação  R − C  (causa ↑ / efeito ↓)", fontsize=10.5)
    ax.set_title("DEMATEL — estrutura causal dos critérios de decisão\n"
                 "(o tamanho do círculo é o peso derivado por influência)",
                 fontsize=12, fontweight="bold")
    ax.grid(alpha=0.25, linestyle=":")
    ax.set_axisbelow(True)

    caminho = STATIC / "dematel_causa_efeito.png"
    fig.savefig(caminho, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return caminho


def mapa_metodos(conn):
    linhas = conn.execute("SELECT project_name, metodo, rank_ FROM decisao_mcdm").fetchall()
    if not linhas:
        return None
    consenso = {r["project_name"]: r["rank_final"] for r in
                conn.execute("SELECT project_name, rank_final FROM decisao_consenso")}

    metodos = sorted({r["metodo"] for r in linhas})
    projetos = sorted(consenso, key=lambda p: consenso[p])
    M = np.full((len(projetos), len(metodos) + 1), np.nan)
    for r in linhas:
        M[projetos.index(r["project_name"]), metodos.index(r["metodo"])] = r["rank_"]
    for p, pos in consenso.items():
        M[projetos.index(p), -1] = pos

    rotulos = metodos + ["CONSENSO\n(Borda)"]
    fig, ax = plt.subplots(figsize=(1.55 * len(rotulos) + 2.4, 0.52 * len(projetos) + 2.3))
    im = ax.imshow(M, cmap="RdYlGn_r", aspect="auto", vmin=1, vmax=len(projetos))

    for i in range(len(projetos)):
        for j in range(len(rotulos)):
            ax.text(j, i, f"{int(M[i, j])}º", ha="center", va="center",
                    fontsize=9.5, fontweight="bold" if j == len(rotulos) - 1 else "normal",
                    color="black")
    ax.axvline(len(metodos) - 0.5, color="black", lw=2.2)

    ax.set_xticks(range(len(rotulos)))
    ax.set_xticklabels(rotulos, fontsize=9)
    ax.set_yticks(range(len(projetos)))
    ax.set_yticklabels(projetos, fontsize=9.5)
    ax.set_title("Posição de cada projeto por escola de decisão\n"
                 "(verde = melhor · divergência entre métodos é informação, não ruído)",
                 fontsize=12, fontweight="bold")
    fig.colorbar(im, ax=ax, shrink=0.85, label="Posição (1º = melhor)")

    caminho = STATIC / "mcdm_metodos.png"
    fig.savefig(caminho, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return caminho


def main():
    STATIC.mkdir(parents=True, exist_ok=True)
    conn = get_conn()
    gerados = [c for c in (diagrama_causa_efeito(conn), mapa_metodos(conn)) if c]
    conn.close()
    for c in gerados:
        print(f"  🖼️  {c.relative_to(FOUNDATIONS_DIR)}")
    print(f"\n✅ {len(gerados)} gráficos de decisão multicritério.")


if __name__ == "__main__":
    main()
