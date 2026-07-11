"""
Telas do eixo de EXECUÇÃO para o README: saúde da IA no tempo, matriz de risco P×I
e Cumulative Flow Diagram. Mesmo estilo visual dos demais gráficos do pacote.

Saída: ../evidence/static/mc/tela_<nome>.png  (dados anônimos Project A..J).

Uso:  python3 gerar_telas_execucao.py [--projeto "Project C"]
Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026.
"""
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from db import get_conn
from config import FOUNDATIONS_DIR

STATIC = FOUNDATIONS_DIR / "evidence" / "static" / "mc"
STATIC.mkdir(parents=True, exist_ok=True)
FUNDO = "#D9D9D9"
NIVEL_COR = {"baixo": "#2CA02C", "medio": "#FFC000", "alto": "#FF7F0E", "critico": "#D62728"}


def tela_latencia(conn, projeto):
    rows = conn.execute(
        "SELECT dia, p50, p95, p99 FROM exec_latencia_tempo WHERE project_name=? ORDER BY dia",
        (projeto,)).fetchall()
    if not rows:
        return None
    dias = [r[0][-5:] for r in rows]
    fig, ax = plt.subplots(figsize=(9.5, 4.2))
    ax.set_facecolor(FUNDO)
    for i, (lab, cor) in enumerate([("p50", "#1F77B4"), ("p95", "#FF7F0E"), ("p99", "#D62728")], 1):
        ax.plot(dias, [r[i] for r in rows], marker="o", lw=2, color=cor, label=lab)
    ax.axhline(5.0, color="#B00", ls="--", lw=1.6)
    ax.text(0, 5.05, " SLO p95 = 5 s", color="#B00", fontsize=8, va="bottom")
    ax.set_title(f"Saúde de execução da IA — latência por dia ({projeto})", fontweight="bold")
    ax.set_ylabel("segundos", fontstyle="italic")
    ax.set_xlabel("dia", fontstyle="italic")
    ax.grid(color="white", lw=0.8); ax.set_axisbelow(True)
    ax.legend(fontsize=8, framealpha=0.9)
    fig.tight_layout()
    out = STATIC / "tela_exec_latencia.png"
    fig.savefig(out, dpi=110); plt.close(fig)
    return out


def tela_risco(conn, projeto):
    rows = conn.execute(
        "SELECT categoria, probabilidade, impacto, exposicao, nivel FROM risco_registro "
        "WHERE project_name=? ORDER BY exposicao DESC", (projeto,)).fetchall()
    if not rows:
        return None
    fig, ax = plt.subplots(figsize=(8.2, 5.4))
    ax.set_facecolor(FUNDO)
    # zonas de risco ao fundo (verde -> vermelho)
    for xi in range(1, 6):
        for yi in range(1, 6):
            exp = xi * yi
            cor = "#2CA02C" if exp < 4 else "#FFF2CC" if exp < 9 else "#FCE4D6" if exp < 15 else "#F8CBAD"
            ax.add_patch(plt.Rectangle((xi - 0.5, yi - 0.5), 1, 1, color=cor, alpha=0.45, zorder=1))
    # Riscos distintos caem com frequência na MESMA célula (P,I) e as bolhas se
    # sobrepõem, escondendo dados. Desempilha em leque dentro da célula e põe o
    # rótulo FORA da bolha (dentro ficava ilegível).
    ocupadas = {}
    for cat, p, i, exp, niv in rows:
        k = (p, i)
        n = ocupadas.get(k, 0)
        ocupadas[k] = n + 1
        dx, dy = (0.0, 0.0) if n == 0 else (0.16 * (1 if n % 2 else -1), 0.16 * ((n + 1) // 2))
        x, y = p + dx, i + dy
        ax.scatter(x, y, s=exp * 55, color=NIVEL_COR.get(niv, "#555"),
                   edgecolor="#333", lw=1.2, zorder=3, alpha=0.92)
        ax.annotate(f"{cat} ({exp})", (x, y), xytext=(0, -16), textcoords="offset points",
                    fontsize=7.5, ha="center", color="#222", zorder=5,
                    bbox=dict(boxstyle="round,pad=0.18", fc="white", ec="none", alpha=0.75))
    ax.set_xlim(0.5, 5.5); ax.set_ylim(0.5, 5.5)
    ax.set_xticks(range(1, 6)); ax.set_yticks(range(1, 6))
    ax.set_xlabel("Probabilidade (1–5)", fontstyle="italic")
    ax.set_ylabel("Impacto (1–5)", fontstyle="italic")
    ax.set_title(f"Matriz de risco Probabilidade × Impacto ({projeto})\n"
                 "bolha = exposição (P×I); probabilidade ancorada nos sinais reais",
                 fontweight="bold", fontsize=10)
    ax.grid(color="white", lw=0.8); ax.set_axisbelow(True)
    fig.tight_layout()
    out = STATIC / "tela_risco_matriz.png"
    fig.savefig(out, dpi=110); plt.close(fig)
    return out


def tela_cfd(conn, projeto):
    rows = conn.execute(
        "SELECT dia, backlog, doing, review, done FROM fluxo_cfd WHERE project_name=? ORDER BY dia",
        (projeto,)).fetchall()
    if not rows:
        return None
    dias = [r[0][-5:] for r in rows]
    series = np.array([[r[1] for r in rows], [r[2] for r in rows],
                       [r[3] for r in rows], [r[4] for r in rows]], float)
    fig, ax = plt.subplots(figsize=(9.5, 4.4))
    ax.set_facecolor(FUNDO)
    ax.stackplot(dias, series, labels=["backlog", "doing", "review", "done"],
                 colors=["#B0BEC5", "#FFC000", "#4FA3E3", "#2CA02C"], alpha=0.95)
    ax.set_title(f"Cumulative Flow Diagram — fluxo de trabalho ({projeto})", fontweight="bold")
    ax.set_ylabel("itens", fontstyle="italic")
    ax.set_xlabel("dia", fontstyle="italic")
    ax.legend(loc="upper left", fontsize=8, framealpha=0.9)
    ax.grid(color="white", lw=0.8); ax.set_axisbelow(True)
    fig.tight_layout()
    out = STATIC / "tela_fluxo_cfd.png"
    fig.savefig(out, dpi=110); plt.close(fig)
    return out


def main():
    conn = get_conn()
    proj = sys.argv[sys.argv.index("--projeto") + 1] if "--projeto" in sys.argv else None
    if not proj:
        row = conn.execute("SELECT project_name FROM decisao_consenso "
                           "ORDER BY rank_final ASC LIMIT 1").fetchone()
        proj = row[0] if row else "Project C"
    feitos = [f for f in (tela_latencia(conn, proj), tela_risco(conn, proj),
                          tela_cfd(conn, proj)) if f]
    conn.close()
    print(f"✅ {len(feitos)} telas de execução geradas ({proj}) em {STATIC}")


if __name__ == "__main__":
    main()
