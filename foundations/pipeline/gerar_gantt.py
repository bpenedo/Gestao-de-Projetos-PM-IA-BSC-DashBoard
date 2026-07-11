"""
Gráficos de cronograma: Gantt (com caminho crítico) + risco de prazo (histograma da
data de término e curva S), no mesmo estilo visual dos gráficos de Monte Carlo.

Por projeto, gera:
  • <projeto>_gantt.png       — barras por tarefa (posições p50 PERT); tarefas críticas
    em vermelho, não-críticas em azul com a folga em cinza-claro; linhas verticais para
    a deadline baseline e para o P80 (compromisso recomendável).
  • <projeto>_prazo_risco.png — histograma da data de término + curva S acumulada, com
    marcadores de P50, P80 e da deadline baseline.

Saída: ../evidence/static/mc/<projeto>_<tipo>.png  (dados anônimos, git-ignored).

Uso:  python3 gerar_gantt.py            # todos os projetos
      python3 gerar_gantt.py --projeto "Project C"
Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026.
"""
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

from db import get_conn
from config import FOUNDATIONS_DIR

STATIC = FOUNDATIONS_DIR / "evidence" / "static" / "mc"
STATIC.mkdir(parents=True, exist_ok=True)

VERMELHO = "#FF0000"
BORDA_BARRA = "#800000"
AZUL = "#1F77B4"
FOLGA = "#C9D6E5"
FUNDO_PLOT = "#D9D9D9"


def _slug(nome):
    return nome.replace(" ", "_")


def gantt(conn, projeto):
    rows = conn.execute(
        "SELECT tarefa_id, nome, inicio, fim, duracao, folga, indice_criticidade, eh_critico "
        "FROM cronograma_critico WHERE project_name=? ORDER BY tarefa_id", (projeto,)
    ).fetchall()
    if not rows:
        return None
    meta = conn.execute(
        "SELECT prazo_alvo, p50, p80 FROM mc_cronograma WHERE project_name=?", (projeto,)
    ).fetchone()
    prazo, p50, p80 = meta

    fig, ax = plt.subplots(figsize=(10, 0.55 * len(rows) + 1.6))
    ax.set_facecolor(FUNDO_PLOT)
    y = list(range(len(rows)))[::-1]           # tarefa 1 no topo
    for yi, (tid, nome, ini, fim, dur, folga, crit, ehc) in zip(y, rows):
        cor = VERMELHO if ehc else AZUL
        ax.barh(yi, dur, left=ini, height=0.55, color=cor, edgecolor=BORDA_BARRA, zorder=3)
        if folga > 0.05:                        # folga como extensão cinza (não-crítica)
            ax.barh(yi, folga, left=fim, height=0.28, color=FOLGA, edgecolor="none", zorder=2)
        ax.text(ini + dur / 2, yi, f"{nome}  ({crit:.0f}%)", va="center", ha="center",
                fontsize=7.5, color="white" if ehc else "white", zorder=4)

    ax.axvline(prazo, color="#333", ls="--", lw=1.4, zorder=5)
    ax.axvline(p80, color="#0A7", ls="-", lw=1.6, zorder=5)
    ax.set_yticks(y)
    ax.set_yticklabels([f"T{r[0]}" for r in rows], fontsize=8)
    ax.set_xlabel("dias desde o início do projeto", fontstyle="italic", fontsize=9)
    ax.set_title(f"Cronograma — {projeto}   (barras vermelhas = caminho crítico; "
                 f"% = índice de criticidade)", fontweight="bold", fontsize=10)
    ax.set_axisbelow(True)
    ax.grid(axis="x", color="white", lw=0.8)
    leg = [Line2D([0], [0], color=VERMELHO, lw=8, label="tarefa crítica"),
           Line2D([0], [0], color=AZUL, lw=8, label="tarefa com folga"),
           Line2D([0], [0], color="#333", ls="--", lw=1.4, label=f"deadline baseline ({prazo:.0f}d)"),
           Line2D([0], [0], color="#0A7", lw=1.6, label=f"P80 — commit ({p80:.0f}d)")]
    ax.legend(handles=leg, fontsize=7.5, loc="lower right", framealpha=0.9)
    fig.tight_layout()
    out = STATIC / f"{_slug(projeto)}_gantt.png"
    fig.savefig(out, dpi=110); plt.close(fig)
    return out


def risco_prazo(conn, projeto):
    hrows = conn.execute(
        "SELECT classe_inf, frequencia, cumulativo FROM mc_cronograma_hist "
        "WHERE project_name=? ORDER BY classe_inf", (projeto,)
    ).fetchall()
    if not hrows:
        return None
    meta = conn.execute(
        "SELECT prazo_alvo, p50, p80, prob_no_prazo FROM mc_cronograma WHERE project_name=?",
        (projeto,)
    ).fetchone()
    prazo, p50, p80, prob = meta
    xs = [r[0] for r in hrows]
    freq = [r[1] for r in hrows]
    cum = [r[2] for r in hrows]
    largura = (xs[1] - xs[0]) if len(xs) > 1 else 1.0

    fig, ax = plt.subplots(figsize=(9.5, 4.2))
    ax.set_facecolor(FUNDO_PLOT)
    ax.bar(xs, freq, width=largura, color=VERMELHO, edgecolor=BORDA_BARRA, align="edge", zorder=3)
    ax.set_ylabel("Frequency", fontstyle="italic")
    ax.set_xlabel("data de término (dias)", fontstyle="italic")
    ax.set_title(f"Risco de prazo — {projeto}   P(no prazo) = {prob:.1f}%",
                 fontweight="bold")
    ax.grid(axis="y", color="white", lw=0.8); ax.set_axisbelow(True)

    ax2 = ax.twinx()
    ax2.plot([x + largura for x in xs], cum, color="#003", lw=1.6, zorder=4)
    ax2.set_ylabel("Cumulative %", fontstyle="italic"); ax2.set_ylim(0, 100)
    for v, cor, lab in [(prazo, "#333", "deadline"), (p50, "#0A7", "P50"), (p80, "#06C", "P80")]:
        ax.axvline(v, color=cor, ls="--", lw=1.3, zorder=5)
        ax.text(v, ax.get_ylim()[1] * 0.96, f" {lab}", color=cor, fontsize=8, rotation=90, va="top")
    fig.tight_layout()
    out = STATIC / f"{_slug(projeto)}_prazo_risco.png"
    fig.savefig(out, dpi=110); plt.close(fig)
    return out


def main():
    conn = get_conn()
    alvo = None
    if "--projeto" in sys.argv:
        alvo = sys.argv[sys.argv.index("--projeto") + 1]
    projetos = [alvo] if alvo else [
        r[0] for r in conn.execute(
            "SELECT project_name FROM mc_cronograma ORDER BY project_name")]
    n = 0
    for p in projetos:
        if gantt(conn, p) and risco_prazo(conn, p):
            n += 1
    conn.close()
    print(f"✅ Gantt + risco de prazo gerados para {n} projeto(s) em {STATIC}")


if __name__ == "__main__":
    main()
