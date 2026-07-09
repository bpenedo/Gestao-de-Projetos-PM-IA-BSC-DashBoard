"""
Gráficos de Monte Carlo replicando o SimulAr v2.5 (janela "Simulation Results").

Reproduz, com os mesmos elementos visuais do manual (foundations/mc/simularusermanual.pdf):

  • Histograma de frequência (p.60): 100 classes do mínimo ao máximo, barras
    vermelhas com borda escura, área de plotagem cinza com grades horizontais,
    título sublinhado em negrito, eixo Y "Frequency" em itálico, rótulos do eixo X
    com as bordas inferiores das classes girados a 90°, e o rodapé
    "Probability less than => v  Equals to => p %".
  • Histograma acumulado (p.62): a opção "Cumulative %" da mesma janela.
  • Tornado de sensibilidade (p.63-64): barras horizontais vermelhas a partir do
    zero, ordenadas pelo |beta| decrescente (maior no topo), rótulo de cada barra
    com "variável, valor", e eixo X em itálico ("Regression" ou "Correlation").

Saída: ../evidence/static/mc/<projeto>_<variavel>_<tipo>.png  (dados anônimos).

Uso:  python3 gerar_mc_graficos.py            # só o vencedor do consenso
      python3 gerar_mc_graficos.py --todos    # todos os projetos
Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
"""
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

from db import get_conn
from config import FOUNDATIONS_DIR

STATIC = FOUNDATIONS_DIR / "evidence" / "static" / "mc"

# Paleta do SimulAr (janela "Simulation Results").
VERMELHO = "#FF0000"
BORDA_BARRA = "#800000"
FUNDO_PLOT = "#D9D9D9"
ROTULO = {"VPL": "NPV", "TIR": "IRR", "TIRM": "MIRR", "VUL": "EAA", "ILL": "PI"}


def _titulo_sublinhado(fig, ax, texto):
    """Título em negrito com sublinhado, como no SimulAr."""
    t = ax.set_title(texto, fontsize=13, fontweight="bold", color="black", pad=12)
    fig.canvas.draw()
    bb = t.get_window_extent(renderer=fig.canvas.get_renderer())
    (x0, y0), (x1, _) = ax.transAxes.inverted().transform(bb.get_points())
    ax.add_artist(Line2D([x0, x1], [y0 - 0.012, y0 - 0.012], transform=ax.transAxes,
                         color="black", lw=1.1, clip_on=False))


def _moldura(ax):
    """Área de plotagem cinza com grades horizontais — o visual da janela do SimulAr."""
    ax.set_facecolor(FUNDO_PLOT)
    ax.grid(axis="y", color="black", lw=0.4, alpha=0.55)
    ax.set_axisbelow(True)
    for lado in ax.spines.values():
        lado.set_color("black")
        lado.set_linewidth(0.8)


def _eixo_x_classes(ax, inferiores, passo=4):
    ax.set_xticks(range(0, len(inferiores), passo))
    ax.set_xticklabels([f"{inferiores[i]:.4f}" for i in range(0, len(inferiores), passo)],
                       rotation=90, fontsize=5.5, family="monospace")


def histograma(conn, projeto, variavel="VPL", cumulativo=False):
    linhas = conn.execute("""SELECT bin_inferior, frequencia, cumul_pct FROM mc_histograma
                             WHERE project_name=? AND variavel=? ORDER BY bin_idx""",
                          (projeto, variavel)).fetchall()
    if not linhas:
        return None
    est = conn.execute("""SELECT prob_menor_zero, iteracoes FROM mc_estatisticas
                          WHERE project_name=? AND variavel=?""", (projeto, variavel)).fetchone()

    inferiores = [r["bin_inferior"] for r in linhas]
    altura = [r["cumul_pct"] for r in linhas] if cumulativo else [r["frequencia"] for r in linhas]

    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    _moldura(ax)
    ax.bar(range(len(altura)), altura, width=1.0, color=VERMELHO,
           edgecolor=BORDA_BARRA, linewidth=0.35)
    _titulo_sublinhado(fig, ax, f"{ROTULO.get(variavel, variavel)} — {projeto}")
    ax.set_ylabel("Cumulative %" if cumulativo else "Frequency", fontsize=9, style="italic")
    ax.set_xlim(-0.5, len(altura) - 0.5)
    if cumulativo:
        ax.set_ylim(0, 100)
    _eixo_x_classes(ax, inferiores)

    if not cumulativo and est:
        fig.text(0.5, -0.10,
                 f"Probability less than =>  0    Equals to =>  {est['prob_menor_zero']:.2f} %"
                 f"      ({est['iteracoes']:,} iterations · {len(altura)} bins)",
                 ha="center", fontsize=8.5, family="monospace")

    sufixo = "cumulativo" if cumulativo else "frequencia"
    caminho = STATIC / f"{projeto.replace(' ', '_')}_{variavel}_{sufixo}.png"
    fig.savefig(caminho, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return caminho


def tornado(conn, projeto, variavel="VPL", modo="regressao"):
    coluna = "beta_regressao" if modo == "regressao" else "coef_correlacao"
    linhas = conn.execute(f"""SELECT variavel_entrada, {coluna} AS v FROM mc_tornado
                              WHERE project_name=? AND variavel_saida=?
                              ORDER BY ABS({coluna}) ASC""", (projeto, variavel)).fetchall()
    if not linhas:
        return None
    nomes = [r["variavel_entrada"] for r in linhas]   # menor -> maior (topo do gráfico = maior)
    valores = [r["v"] for r in linhas]

    fig, ax = plt.subplots(figsize=(8.2, 0.52 * len(nomes) + 1.9))
    _moldura(ax)
    ax.grid(axis="y", visible=False)
    ax.grid(axis="x", color="black", lw=0.4, alpha=0.55)
    ax.barh(range(len(valores)), valores, height=0.62, color=VERMELHO,
            edgecolor=BORDA_BARRA, linewidth=0.6)
    ax.axvline(0, color="black", lw=0.9)

    for i, (nome, v) in enumerate(zip(nomes, valores)):
        ha = "left" if v >= 0 else "right"
        deslocamento = (max(map(abs, valores)) or 1) * 0.02
        ax.text(v + (deslocamento if v >= 0 else -deslocamento), i, f"  {nome}, {v:.4f}  ",
                va="center", ha=ha, fontsize=7.5, color="black")

    _titulo_sublinhado(fig, ax, f"{ROTULO.get(variavel, variavel)} — {projeto}")
    ax.set_yticks(range(len(nomes)))
    ax.set_yticklabels(nomes, fontsize=8)
    ax.set_xlabel("Regression" if modo == "regressao" else "Correlation", fontsize=9, style="italic")
    limite = max(map(abs, valores)) * 1.45 or 1
    ax.set_xlim(-limite * 0.35, limite)

    caminho = STATIC / f"{projeto.replace(' ', '_')}_{variavel}_tornado_{modo}.png"
    fig.savefig(caminho, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return caminho


def main():
    STATIC.mkdir(parents=True, exist_ok=True)
    conn = get_conn()

    if "--todos" in sys.argv:
        projetos = [r[0] for r in conn.execute(
            "SELECT DISTINCT project_name FROM mc_estatisticas ORDER BY project_name")]
    else:
        linha = conn.execute(
            "SELECT project_name FROM decisao_consenso ORDER BY rank_final LIMIT 1").fetchone()
        if not linha:
            print("⚠️  Rode mcdm.py antes (ou use --todos).")
            return
        projetos = [linha[0]]

    gerados = 0
    for proj in projetos:
        for caminho in (histograma(conn, proj, "VPL"),
                        histograma(conn, proj, "VPL", cumulativo=True),
                        tornado(conn, proj, "VPL", "regressao"),
                        tornado(conn, proj, "VPL", "correlacao")):
            if caminho:
                gerados += 1
                print(f"  🖼️  {caminho.relative_to(FOUNDATIONS_DIR)}")
    conn.close()
    print(f"\n✅ {gerados} gráficos de Monte Carlo (estilo SimulAr) em {STATIC.relative_to(FOUNDATIONS_DIR)}/")


if __name__ == "__main__":
    main()
