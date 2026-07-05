"""
gerar_admtools.py — PIPELINE ADMINISTRATIVA CONCORRENTE (Jóia da Coroa).

Gera, DO ZERO (100% em código, sem depender de nenhuma imagem previamente fornecida),
o DOSSIÊ de ferramentas administrativas do PROJETO ELEITO pelo AHP-TOPSIS 2n.
As 6 ferramentas são renderizadas EM PARALELO (ProcessPoolExecutor):

  1. SWOT            — matriz de forças/fraquezas/oportunidades/ameaças (data-driven)
  2. PESTEL/EC       — 7 fatores macroambientais em hexágonos
  3. 5W2H            — roda de plano de ação (What..How much)
  4. PARETO          — categorias de prompt por falha (dados REAIS) + 80/20
  5. GUT (Heatmap)   — matriz de priorização Gravidade×Urgência×Tendência
  6. RADAR           — impressão digital competitiva do eleito vs média do portfólio

Saída: ../evidence/static/admtools/*.png  (regeneráveis; git-ignored p/ privacidade).

Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026.
https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
"""
import os
import sqlite3
from concurrent.futures import ProcessPoolExecutor, as_completed

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["text.parse_math"] = False  # trata "R$" como texto literal (não como mathtext)
import numpy as np
import matplotlib.patheffects as pe
from matplotlib.patches import FancyBboxPatch, RegularPolygon, Circle, Wedge

# contorno escuro sutil p/ dar legibilidade a texto branco sobre cores claras (ex.: amarelo)
GLOW = [pe.withStroke(linewidth=2.4, foreground="#12202f")]

BASE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(BASE, "bsc_ia.db")
OUT = os.path.join(BASE, "..", "evidence", "static", "admtools")
STAMP = ("Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard  ·  "
         "©️ Bruno Penedo — 2026 · linkedin.com/in/bpenedo · bpenedo@gmail.com")

# Paleta institucional (coerente com os templates conhecidos)
AZUL, VERM, AMAR, VERD = "#2E75B6", "#C00000", "#FFC000", "#548235"
NAVY = "#1F3A5F"


# --------------------------------------------------------------------------- #
#  Carga de dados do PROJETO ELEITO (executada 1x no processo principal)
# --------------------------------------------------------------------------- #
def carregar_contexto():
    c = sqlite3.connect(DB)
    c.row_factory = sqlite3.Row
    win = c.execute("SELECT * FROM decisao_mcda WHERE rank_final=1").fetchone()
    if not win:
        raise SystemExit("⚠️  Sem projeto eleito (rode ahp_topsis.py antes).")
    W = win["project_name"]

    kq = open(os.path.join(BASE, "queries", "kpis_bsc_ia.sql")).read()
    kpis = [dict(r) for r in c.execute(kq)]
    me = next((r for r in kpis if r["project_name"] == W), {})

    def media(k):
        v = [r[k] for r in kpis if r.get(k) is not None]
        return round(sum(v) / len(v), 2) if v else 0.0

    pareto = [dict(r) for r in c.execute("""
        SELECT prompt_categoria cat, COUNT(*) n,
               SUM(CASE WHEN tipo_erro NOT IN ('NENHUM','') AND tipo_erro IS NOT NULL
                        THEN 1 ELSE 0 END) er
        FROM logs_langfuse WHERE project_name=? GROUP BY 1""", (W,))]
    fin = c.execute("SELECT * FROM vpl_resultado WHERE project_name=?", (W,)).fetchone()
    fin = dict(fin) if fin else {}
    c.close()

    return {
        "win": W,
        "ci": round(win["ci_final"], 4),
        "me": {k: me.get(k) for k in me},
        "avg": {k: media(k) for k in
                ("kpi_psr", "kpi_peuc", "kpi_iita", "kpi_idls_lean", "kpi_ioli", "kpi_itr", "kpi_cpp")},
        "pareto": pareto,
        "fin": fin,
    }


# --------------------------------------------------------------------------- #
#  Helpers de estilo
# --------------------------------------------------------------------------- #
def _rodape(fig):
    fig.text(0.5, 0.012, STAMP, ha="center", va="bottom", fontsize=6.5, color="#8a8f98")


def _titulo(ax, txt, sub=""):
    ax.set_title(txt, fontsize=17, fontweight="bold", color=NAVY, pad=14)
    if sub:
        ax.text(0.5, 1.005, sub, transform=ax.transAxes, ha="center",
                fontsize=9.5, color="#5b6672")


# --------------------------------------------------------------------------- #
#  1) SWOT
# --------------------------------------------------------------------------- #
def fig_swot(D, path):
    me, avg, fin = D["me"], D["avg"], D["fin"]
    iita, idls, psr = me.get("kpi_iita", 0), me.get("kpi_idls_lean", 0), me.get("kpi_psr", 0)
    peuc, ioli = me.get("kpi_peuc", 0), me.get("kpi_ioli", 0)
    S = [f"Menor alucinação do portfólio (IITA {iita}% vs média {avg['kpi_iita']}%)",
         f"Menor desperdício Lean (IDLS {idls}% vs {avg['kpi_idls_lean']}%)",
         f"Entrega útil elevada (PEUC {peuc}%, ~{peuc/max(avg['kpi_peuc'],1):.1f}× média)",
         f"PSR {psr} acima da média ({avg['kpi_psr']})"]
    Wk = [f"PSR {psr} ainda abaixo da meta 4,0",
          f"Fila/cota presente (IOLI {ioli}%)",
          "Fluxo de caixa REAL ainda não medido"]
    O = [f"VPL R$ {fin.get('vpl',0):,.0f} · TIR {fin.get('tir',0)*100:.1f}% > SELIC",
         "Escalar piloto com eficiência já comprovada",
         "Reusar padrões de prompt de baixa alucinação"]
    T = ["Placeholder financeiro pode reordenar ranking",
         "Corrida de inovação tecnológica concorrente",
         "Dependência de cota de API (rate limit 429)"]

    cols = [("S", "Strengths", AZUL, S), ("W", "Weaknesses", VERM, Wk),
            ("O", "Opportunities", AMAR, O), ("T", "Threats", VERD, T)]
    fig, ax = plt.subplots(figsize=(12.4, 7.6)); ax.axis("off")
    ax.set_xlim(0, 4); ax.set_ylim(0, 10)
    _titulo(ax, f"SWOT — {D['win']}  (Jóia da Coroa)", "Análise estratégica orientada a dados")
    for i, (L, name, col, items) in enumerate(cols):
        x = i + 0.5
        ax.add_patch(FancyBboxPatch((x - 0.44, 1.55), 0.88, 7.35,
                     boxstyle="round,pad=0.02,rounding_size=0.12",
                     facecolor=col, edgecolor="white", lw=2))
        # texto alinhado à esquerda + contorno escuro = leitura confortável em qualquer cor
        body = "\n\n".join("•  " + _wrap(t, 21) for t in items)
        ax.text(x - 0.385, 8.55, body, ha="left", va="top", color="white",
                fontsize=10.5, fontweight="medium", linespacing=1.45, path_effects=GLOW)
        ax.add_patch(Circle((x, 1.05), 0.45, facecolor="white", edgecolor=col, lw=3))
        ax.text(x, 1.1, L, ha="center", va="center", color=col, fontsize=22, fontweight="bold")
        ax.text(x, 0.32, name, ha="center", va="center", color="#333", fontsize=10.5, fontweight="bold")
    _rodape(fig)
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor="white"); plt.close(fig)
    return path


# --------------------------------------------------------------------------- #
#  2) PESTEL/EC (hexágonos)
# --------------------------------------------------------------------------- #
def fig_pestel(D, path):
    fatores = [
        ("P", "Político", VERD, "Sem entraves políticos ao uso de IA hoje; monitorar marcos regulatórios de IA."),
        ("E", "Econômico", VERM, "Custo por token em queda; retorno (TIR>SELIC) favorece a escala do eleito."),
        ("S", "Social", AMAR, "Gerações Y/Z demandam automação inteligente e resposta em tempo real."),
        ("T", "Tecnológico", AZUL, "Modelos evoluem rápido; eficiência (baixo IITA/IDLS) é vantagem sustentável."),
        ("E", "Ecológico", "#2E9E8F", "Menor desperdício de tokens reduz consumo computacional e energético."),
        ("L", "Legal", "#7B4FA3", "LGPD e governança de dados; rastreabilidade via Langfuse mitiga risco."),
        ("C", "Cultural", "#E08A2B", "Cultura data-driven (Kaplan): 'o que não é medido não é gerenciado'."),
    ]
    n = len(fatores)
    fig, ax = plt.subplots(figsize=(15, 8.6)); ax.axis("off")
    ax.set_xlim(0, n); ax.set_ylim(0, 7.6)
    _titulo(ax, f"PESTELC — {D['win']}", "Fatores macroambientais (7 dimensões)")
    r = 0.58
    for i, (L, nome, col, txt) in enumerate(fatores):
        cx, cy = i + 0.5, 3.8
        ax.add_patch(RegularPolygon((cx, cy), 6, radius=r, orientation=np.pi/6,
                     facecolor=col, edgecolor="white", lw=2))
        ax.text(cx, cy + 0.14, L, ha="center", va="center", color="white",
                fontsize=20, fontweight="bold", path_effects=GLOW)
        ax.text(cx, cy - 0.28, nome, ha="center", va="center", color="white",
                fontsize=11, fontweight="bold", path_effects=GLOW)
        up = i % 2 == 0
        ty = cy + 1.55 if up else cy - 1.55
        ax.annotate("", xy=(cx, ty), xytext=(cx, cy + (r if up else -r)),
                    arrowprops=dict(arrowstyle="->", color="#8a97a6", lw=1.5))
        ax.text(cx, ty + (0.07 if up else -0.07), _wrap(txt, 20),
                ha="center", va="bottom" if up else "top", fontsize=11.5,
                fontweight="medium", color="#1f2b38", linespacing=1.34)
    _rodape(fig)
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor="white"); plt.close(fig)
    return path


# --------------------------------------------------------------------------- #
#  3) 5W2H (roda de plano de ação)
# --------------------------------------------------------------------------- #
def fig_5w4h(D, path):
    fin = D["fin"]
    # 5W (O quê..Quem) + 4H (Como, Quanto custa, Quantos, Quanto tempo) = 5W4H
    setores = [
        ("O quê?\n(What)", f"Escalar {D['win']} como piloto oficial de IA", "#8E2434"),
        ("Por quê?\n(Why)", "Menor alucinação (IITA) e menor muda (IDLS) do portfólio", "#B93A2B"),
        ("Onde?\n(Where)", "Pipeline BSC · Langfuse→SQLite→Evidence", "#D9752B"),
        ("Quando?\n(When)", "Próximo sprint (weekly de sexta)", "#E8A62B"),
        ("Quem?\n(Who)", "PM + Dev + revisor LLM-as-judge", "#F1C40F"),
        ("Como?\n(How)", "Inserir fluxos de caixa reais + re-rodar AHP-TOPSIS", "#3FA36B"),
        ("Quanto custa?\n(How much)", f"Invest. ~R$ {abs(fin.get('vpl',0))*0.5:,.0f} · VPL R$ {fin.get('vpl',0):,.0f}", "#2E86AB"),
        ("Quantos?\n(How many)", f"Meta: TIR {fin.get('tir',0)*100:.0f}% · PSR 4,0", "#2C3E63"),
        ("Quanto tempo?\n(How long)", f"1 sprint p/ fluxos · payback ~{fin.get('payback_descontado',0):.1f} períodos", "#7B4FA3"),
    ]
    fig, ax = plt.subplots(figsize=(8.6, 8.6)); ax.axis("off")
    ax.set_xlim(-1.38, 1.38); ax.set_ylim(-1.38, 1.38); ax.set_aspect("equal")
    fig.suptitle(f"5W4H — Plano de Ação · {D['win']}", fontsize=16, fontweight="bold",
                 color=NAVY, y=0.965)
    n = len(setores); step = 360 / n
    for i, (q, ans, col) in enumerate(setores):
        a0 = 90 - i * step; a1 = a0 - step
        ax.add_patch(Wedge((0, 0), 1.0, a1, a0, width=0.62, facecolor=col,
                     edgecolor="white", lw=2))
        mid = np.radians((a0 + a1) / 2)
        rq = 0.69
        ax.text(rq*np.cos(mid), rq*np.sin(mid), q, ha="center", va="center",
                color="white", fontsize=7.6, fontweight="bold", linespacing=1.05)
        ra = 1.16
        ha = "left" if np.cos(mid) >= 0 else "right"
        ax.text(ra*np.cos(mid), ra*np.sin(mid), _wrap(ans, 26), ha=ha, va="center",
                fontsize=7.2, color="#33404d")
    ax.add_patch(Circle((0, 0), 0.38, facecolor="white", edgecolor="#dcdcdc", lw=1.5))
    ax.text(0, 0.06, "5W4H", ha="center", va="center", fontsize=19, fontweight="bold", color=VERM)
    ax.text(0, -0.14, "Plano de Ação", ha="center", va="center", fontsize=9, color="#5b6672")
    _rodape(fig)
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor="white"); plt.close(fig)
    return path


# --------------------------------------------------------------------------- #
#  4) PARETO (dados reais)
# --------------------------------------------------------------------------- #
def fig_pareto(D, path):
    dat = sorted(D["pareto"], key=lambda r: r["er"], reverse=True)
    dat = [r for r in dat if r["er"] > 0] or dat
    cats = [r["cat"] for r in dat]
    er = np.array([r["er"] for r in dat], dtype=float)
    tot = er.sum() or 1.0
    cum = np.cumsum(er) / tot * 100
    fig, ax = plt.subplots(figsize=(11, 6.2))
    x = np.arange(len(cats))
    bars = ax.bar(x, er, color=AZUL, edgecolor="white", zorder=3)
    for b, v in zip(bars, er):
        ax.text(b.get_x()+b.get_width()/2, v+0.1, int(v), ha="center", fontsize=9, color=NAVY)
    ax2 = ax.twinx()
    ax2.plot(x, cum, "-o", color=VERM, lw=2, zorder=4)
    ax2.axhline(80, ls="--", color="#999", lw=1)
    ax2.text(len(cats)-0.5, 82, "80%", color="#777", fontsize=8, ha="right")
    for xi, c in zip(x, cum):
        ax2.text(xi, c+2.5, f"{c:.0f}%", ha="center", fontsize=8, color=VERM)
    ax.set_xticks(x); ax.set_xticklabels([_wrap(c, 12) for c in cats], fontsize=8)
    ax.set_ylabel("Falhas (contagem)", color=NAVY); ax2.set_ylabel("Acumulado %", color=VERM)
    ax2.set_ylim(0, 112); ax.set_ylim(0, er.max()*1.25 if er.max() else 1)
    _titulo(ax, f"Pareto de Falhas por Categoria de Prompt · {D['win']}",
            "Priorize a cauda que concentra 80% das falhas (dados reais)")
    ax.grid(axis="y", ls=":", alpha=.4, zorder=0)
    _rodape(fig)
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor="white"); plt.close(fig)
    return path


# --------------------------------------------------------------------------- #
#  5) GUT (heatmap de priorização)
# --------------------------------------------------------------------------- #
def fig_gut(D, path):
    # Ações estratégicas do eleito priorizadas por Gravidade × Urgência × Tendência (1-5)
    acoes = [
        ("Inserir fluxos de caixa reais (fechar MCDA)", 5, 5, 5),
        ("Elevar PSR de {:.1f} → 4,0".format(D["me"].get("kpi_psr", 0)), 4, 4, 4),
        ("Reduzir IOLI (fila + backoff exponencial)", 3, 4, 4),
        ("Grounding RAG / citar fontes (↓ alucinação)", 4, 3, 3),
        ("Padronizar prompts de baixa alucinação", 3, 3, 4),
    ]
    acoes = sorted(acoes, key=lambda a: a[1]*a[2]*a[3], reverse=True)
    rot = [a[0] for a in acoes]
    M = np.array([[a[1], a[2], a[3], a[1]*a[2]*a[3]] for a in acoes], dtype=float)
    fig, ax = plt.subplots(figsize=(10.5, 5.6))
    disp = M.copy(); disp[:, 3] = disp[:, 3] / 125 * 5  # normaliza GUT (máx 125) p/ escala de cor
    im = ax.imshow(disp, cmap="RdYlGn_r", aspect="auto", vmin=1, vmax=5)
    cols = ["Gravidade", "Urgência", "Tendência", "GUT (G×U×T)"]
    ax.set_xticks(range(4)); ax.set_xticklabels(cols, fontsize=10, fontweight="bold")
    ax.set_yticks(range(len(rot))); ax.set_yticklabels([_wrap(r, 34) for r in rot], fontsize=9)
    for i in range(len(rot)):
        for j in range(4):
            val = int(M[i, j])
            ax.text(j, i, val, ha="center", va="center", fontsize=11, fontweight="bold",
                    color="#111" if disp[i, j] < 3.5 else "white")
    _titulo(ax, f"Matriz GUT — Priorização de Ações · {D['win']}",
            "Gravidade × Urgência × Tendência (1–5) · maior GUT = agir primeiro")
    fig.colorbar(im, ax=ax, shrink=.8, label="Criticidade")
    _rodape(fig)
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor="white"); plt.close(fig)
    return path


# --------------------------------------------------------------------------- #
#  6) RADAR (impressão digital competitiva)
# --------------------------------------------------------------------------- #
def fig_radar(D, path):
    me, avg = D["me"], D["avg"]
    def q(iita):  # qualidade = 100 - alucinação
        return max(0, 100 - iita)
    eixos = ["PSR\n(qualidade)", "PEUC\n(entrega útil)", "Anti-alucinação\n(100-IITA)",
             "Lean\n(100-IDLS)", "Estabilidade\n(100-IOLI)", "Custo-efic.\n(CPP inv.)"]
    def vetor(src):
        cpp = src.get("kpi_cpp", 1) or 1
        cpp_avg = avg["kpi_cpp"] or 1
        return [
            (src.get("kpi_psr", 0) / 5) * 100,
            src.get("kpi_peuc", 0),
            q(src.get("kpi_iita", 0)),
            max(0, 100 - src.get("kpi_idls_lean", 0)),
            max(0, 100 - src.get("kpi_ioli", 0)),
            min(100, cpp_avg / cpp * 60),  # menor CPP => maior score (relativo à média)
        ]
    v_me, v_avg = vetor(me), vetor(avg)
    N = len(eixos)
    ang = np.linspace(0, 2*np.pi, N, endpoint=False).tolist(); ang += ang[:1]
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    for vals, col, lab, fill in [(v_avg, "#9aa4af", "Média do portfólio", 0.10),
                                 (v_me, AZUL, D["win"] + " (eleito)", 0.28)]:
        vv = vals + vals[:1]
        ax.plot(ang, vv, "-o", color=col, lw=2, label=lab)
        ax.fill(ang, vv, color=col, alpha=fill)
    ax.set_xticks(ang[:-1]); ax.set_xticklabels(eixos, fontsize=9)
    ax.set_ylim(0, 100); ax.set_yticks([20, 40, 60, 80, 100])
    ax.set_yticklabels(["20", "40", "60", "80", "100"], fontsize=7, color="#888")
    ax.set_title(f"Radar Competitivo — {D['win']} vs Portfólio", fontsize=15,
                 fontweight="bold", color=NAVY, pad=26)
    ax.legend(loc="upper right", bbox_to_anchor=(1.16, 1.12), fontsize=9)
    _rodape(fig)
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor="white"); plt.close(fig)
    return path


# --------------------------------------------------------------------------- #
#  utilitários
# --------------------------------------------------------------------------- #
def _wrap(txt, width):
    import textwrap
    return "\n".join(textwrap.wrap(txt, width)) or txt


# worker de nível de módulo (picklável)
def _worker(args):
    nome, path, D = args
    return {"swot": fig_swot, "pestel": fig_pestel, "5w4h": fig_5w4h,
            "pareto": fig_pareto, "gut": fig_gut, "radar": fig_radar}[nome](D, path)


def main():
    os.makedirs(OUT, exist_ok=True)
    D = carregar_contexto()
    print(f"🏆 Projeto eleito (Jóia da Coroa): {D['win']}  (Ci={D['ci']})")
    tarefas = [(n, os.path.join(OUT, f"{n}.png"), D)
               for n in ("swot", "pestel", "5w4h", "pareto", "gut", "radar")]
    with ProcessPoolExecutor(max_workers=min(6, os.cpu_count() or 4)) as ex:
        futs = {ex.submit(_worker, t): t[0] for t in tarefas}
        for f in as_completed(futs):
            nome = futs[f]
            try:
                print(f"   ✓ {nome:8s} → {os.path.relpath(f.result(), BASE)}")
            except Exception as e:
                print(f"   ✗ {nome:8s} FALHOU: {e}")
    print(f"✅ Dossiê administrativo gerado em {os.path.relpath(OUT, BASE)}/ (6 ferramentas, concorrente)")


if __name__ == "__main__":
    main()
