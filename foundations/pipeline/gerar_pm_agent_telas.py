"""
Telas do Project Manager Agent para os READMEs (12 idiomas):

  1. fever chart (CCPM/Goldratt)      — as zonas VERDE/AMARELO/VERMELHO com as diagonais
  2. radar de dimensões (PM Agent)    — dano em R$ por dimensão, na mesma régua
  3. tolerâncias (PRINCE2)            — folga de cada dimensão até a exceção
  4. sprints (say-do + burndown)      — o material do debate da weekly

Decisões de visualização (e por que):
  · o fever chart usa a paleta de STATUS (verde/amarelo/vermelho), que é reservada a estado —
    e NUNCA só a cor: cada projeto leva rótulo, e as fronteiras levam texto.
  · radar e tolerâncias são UMA série -> sem legenda; o título nomeia a série.
  · burndown tem DUAS séries -> legenda presente, e os dois rótulos diretos.
  · eixo único em todos. Nenhum gráfico de eixo duplo.

Saída: ../../docs/screenshots/*.png  (dados anônimos Project A..J, versionados)

Uso:  python3 gerar_pm_agent_telas.py
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

FUNDO_PLOT = "#D9D9D9"
AZUL, VERDE, AMARELO, VERMELHO = "#1F77B4", "#2CA02C", "#E8A33D", "#D62728"
TINTA, TINTA2 = "#1A1A1A", "#5A5A5A"
COR_ZONA = {"VERDE": VERDE, "AMARELO": AMARELO, "VERMELHO": VERMELHO}


def _base(ax):
    ax.set_facecolor(FUNDO_PLOT)
    ax.grid(alpha=0.25, color="white", linewidth=0.8)
    ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(TINTA2)


def fever_chart(conn):
    rows = conn.execute(
        "SELECT project_name, pct_cadeia, pct_buffer, zona FROM buffer_fever "
        "ORDER BY project_name").fetchall()
    fig, ax = plt.subplots(figsize=(11, 6.5))
    _base(ax)
    x = np.linspace(0, 1, 100)
    lv, lr = 1/3 + x/3, 2/3 + x/3
    # As zonas. Fronteiras DIAGONAIS: queimar buffer no fim é normal; no começo é grave.
    ax.fill_between(x, 0, lv, color=VERDE, alpha=0.16)
    ax.fill_between(x, lv, lr, color=AMARELO, alpha=0.18)
    ax.fill_between(x, lr, 1.6, color=VERMELHO, alpha=0.15)
    ax.plot(x, lv, color=VERDE, lw=2)
    ax.plot(x, lr, color=VERMELHO, lw=2)

    # Descolisão: dois projetos no mesmo x sumiam um atrás do outro (A e G, ambos em 62%).
    # Um gráfico que esconde um ponto está mentindo por omissão.
    usados = []
    n_est = 0
    for p, cad, buf, z in sorted(rows, key=lambda r: r[1]):
        cx = cad
        while any(abs(cx - u) < 0.035 for u in usados):
            cx += 0.038
        usados.append(cx)

        estourou = buf > 1.55
        yy = 1.52 if estourou else buf
        ax.scatter(cx, yy, s=150, color=COR_ZONA[z], edgecolor="white",
                   linewidth=2, zorder=5, marker="^" if estourou else "o")
        # Quem estourou a escala leva o VALOR REAL no rótulo — cravar em 155% e calar
        # o número seria esconder que o buffer foi estourado 4 vezes.
        # Os rótulos com valor são LARGOS: alternar a altura evita que se atropelem.
        if estourou:
            dy = -20 if n_est % 2 == 0 else -36
            n_est += 1
            txt = f"{p.split()[-1]} ({buf:.0%})"
        else:
            dy, txt = 12, p.split()[-1]
        ax.annotate(txt, (cx, yy), xytext=(0, dy), textcoords="offset points",
                    ha="center", fontsize=9, color=TINTA, fontweight="bold")
    ax.text(0.99, 1.575, "▲ = fora da escala (buffer estourado)", ha="right",
            fontsize=8.5, color="#8B1A1A", style="italic")

    ax.text(0.03, 0.13, "VERDE — não faça nada\n(e o agente CALA)", fontsize=10,
            color="#1B5E20", fontweight="bold")
    ax.text(0.03, 0.52, "AMARELO — planeje a recuperação", fontsize=10,
            color="#8A5A00", fontweight="bold")
    ax.text(0.03, 1.30, "VERMELHO — aja agora", fontsize=10,
            color="#8B1A1A", fontweight="bold")
    ax.set_xlim(-0.02, 1.02); ax.set_ylim(0, 1.68)
    ax.set_xlabel("% da cadeia concluída", color=TINTA)
    ax.set_ylabel("% do buffer consumido (P80 − P50)", color=TINTA)
    ax.set_title("Fever chart do buffer (CCPM / Goldratt) — 10 projetos\n"
                 "as fronteiras são DIAGONAIS: 60% de buffer é VERDE no fim e VERMELHO no começo",
                 fontsize=12, fontweight="bold", color=TINTA)
    ax.xaxis.set_major_formatter(lambda v, _: f"{v:.0%}")
    ax.yaxis.set_major_formatter(lambda v, _: f"{v:.0%}")
    fig.tight_layout()
    fig.savefig(SHOTS / "ccpm-fever-chart.png", dpi=130, facecolor="white")
    plt.close(fig)
    return "ccpm-fever-chart.png"


def radar_dimensoes(conn, projeto="Project H"):
    rows = conn.execute(
        "SELECT dimensao, dano_rs, escolhida FROM pm_agent_radar WHERE project_name=? "
        "AND ciclo=(SELECT MAX(ciclo) FROM pm_agent_radar WHERE project_name=?) "
        "ORDER BY dano_rs", (projeto, projeto)).fetchall()
    dims = [r[0] for r in rows]
    dano = [r[1] for r in rows]
    esc = [r[2] for r in rows]
    # Magnitude -> sequencial de UMA cor (claro->escuro). A escolhida ganha destaque
    # por cor E por rótulo — nunca só por cor.
    mx = max(dano) or 1
    cores = [plt.cm.Blues(0.30 + 0.60 * (d / mx)) for d in dano]
    for i, e in enumerate(esc):
        if e:
            cores[i] = VERMELHO

    fig, ax = plt.subplots(figsize=(11, 6))
    _base(ax)
    b = ax.barh(dims, dano, color=cores, edgecolor="white", linewidth=1.5, height=0.72)
    for i, (d, e) in enumerate(zip(dano, esc)):
        rot = f"R$ {d:,.0f}" + ("   ◀ ESCOLHIDA pelo agente" if e else "")
        ax.text(d + mx * 0.015, i, rot, va="center", fontsize=9.5,
                color=TINTA, fontweight="bold" if e else "normal")
    ax.set_xlim(0, mx * 1.42)
    ax.set_xlabel("dano estimado (R$) — dias-equivalentes × custo do atraso deste projeto",
                  color=TINTA)
    ax.set_title(f"Radar das 10 dimensões — {projeto}\n"
                 "o agente não olha só a vencedora: ele mostra a bancada inteira, na mesma régua",
                 fontsize=12, fontweight="bold", color=TINTA)
    fig.tight_layout()
    fig.savefig(SHOTS / "pm-agent-radar.png", dpi=130, facecolor="white")
    plt.close(fig)
    return "pm-agent-radar.png"


def tolerancias(conn, projeto="Project A"):
    rows = conn.execute(
        "SELECT dimensao, folga_pct, estourou FROM pm_agent_tolerancia WHERE project_name=? "
        "AND ciclo=(SELECT MAX(ciclo) FROM pm_agent_tolerancia WHERE project_name=?) "
        "ORDER BY folga_pct", (projeto, projeto)).fetchall()
    dims = [r[0] for r in rows]
    folga = [r[1] * 100 for r in rows]
    est = [r[2] for r in rows]
    cores = [VERMELHO if e else VERDE for e in est]

    fig, ax = plt.subplots(figsize=(11, 5.4))
    _base(ax)
    ax.barh(dims, folga, color=cores, edgecolor="white", linewidth=1.5, height=0.66)
    ax.axvline(0, color=TINTA, lw=2)
    for i, (f, e) in enumerate(zip(folga, est)):
        lbl = ("EXCEÇÃO — escala" if e else "dentro da tolerância")
        ax.text(f + (2.5 if f >= 0 else -2.5), i, f"{f:+.0f}%  {lbl}",
                va="center", ha="left" if f >= 0 else "right",
                fontsize=9.5, color=TINTA, fontweight="bold" if e else "normal")
    lo, hi = min(folga + [0]), max(folga + [0])
    ax.set_xlim(lo - 42, hi + 42)
    ax.set_xlabel("folga até a tolerância acordada (negativo = estourou)", color=TINTA)
    ax.set_title(f"Tolerâncias — PRINCE2 management by exception ({projeto})\n"
                 "a tolerância sai do que o PROJETO já declarou: a data prometida, o orçamento "
                 "aprovado,\no próprio registro de risco, a baseline de qualidade do próprio projeto",
                 fontsize=12, fontweight="bold", color=TINTA)
    fig.tight_layout()
    fig.savefig(SHOTS / "prince2-tolerancias.png", dpi=130, facecolor="white")
    plt.close(fig)
    return "prince2-tolerancias.png"


def sprints_weekly(conn, projeto="Project A"):
    rows = conn.execute(
        "SELECT sprint, say_do, restante, restante_ideal FROM sprints "
        "WHERE project_name=? ORDER BY sprint", (projeto,)).fetchall()
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13.5, 5.4))

    # ── say-do ratio: UMA série -> sem legenda; o título nomeia. Linha de referência em 1.
    _base(a1)
    sp = [r[0] for r in rows if r[1] is not None]
    sd = [r[1] for r in rows if r[1] is not None]
    cor = [VERDE if 0.85 <= v <= 1.15 else (AMARELO if v > 1.15 else VERMELHO) for v in sd]
    a1.bar(sp, sd, color=cor, edgecolor="white", linewidth=1.5, width=0.66)
    a1.axhline(1.0, color=TINTA, lw=2, ls="--")
    a1.text(sp[0] - 0.4, 1.03, "prometido = entregue", fontsize=9, color=TINTA)
    for x, v in zip(sp, sd):
        a1.text(x, v + 0.03, f"{v:.0%}", ha="center", fontsize=9, color=TINTA)
    a1.set_xlabel("sprint (= período do EVM)", color=TINTA)
    a1.set_ylabel("entregue / comprometido", color=TINTA)
    a1.yaxis.set_major_formatter(lambda v, _: f"{v:.0%}")
    a1.set_title("Say-do ratio — a métrica que muda o tom da reunião\n"
                 "0,7 não é lentidão: é prometer 30% a mais do que se entrega",
                 fontsize=11, fontweight="bold", color=TINTA)

    # ── burndown: DUAS séries -> legenda presente + rótulo direto nas duas.
    _base(a2)
    sp2 = [r[0] for r in rows]
    real = [r[2] for r in rows]
    ideal = [r[3] for r in rows]
    spr = [s for s, v in zip(sp2, real) if v is not None]
    rr = [v for v in real if v is not None]
    a2.plot(sp2, ideal, color=AZUL, lw=2, ls="--", marker="o", ms=5, label="planejado (BAC − PV)")
    a2.plot(spr, rr, color=VERMELHO, lw=2.5, marker="o", ms=8, label="real (BAC − EV)")
    if rr:
        a2.annotate("real", (spr[-1], rr[-1]), xytext=(6, 4), textcoords="offset points",
                    color=VERMELHO, fontweight="bold", fontsize=10)
    a2.annotate("planejado", (sp2[-1], ideal[-1]), xytext=(-64, 22),
                textcoords="offset points", color=AZUL, fontweight="bold", fontsize=10)
    a2.legend(frameon=False, loc="upper right")
    a2.set_xlabel("sprint (= período do EVM)", color=TINTA)
    a2.set_ylabel("trabalho restante", color=TINTA)
    a2.set_title("Burndown do projeto — real contra o planejado\n"
                 "a sprint não é inventada: é o período do EVM, com PV/EV/AC reais",
                 fontsize=11, fontweight="bold", color=TINTA)

    fig.tight_layout()
    fig.savefig(SHOTS / "sprints-weekly.png", dpi=130, facecolor="white")
    plt.close(fig)
    return "sprints-weekly.png"


def main():
    conn = get_conn()
    print("🖼️  Telas do Project Manager Agent para os 12 READMEs")
    for f in (fever_chart(conn), radar_dimensoes(conn), tolerancias(conn),
              sprints_weekly(conn)):
        print(f"   ✅ docs/screenshots/{f}")
    conn.close()


if __name__ == "__main__":
    main()
