"""
gerar_admtools.py — PIPELINE ADMINISTRATIVA CONCORRENTE + i18n (Passo 2).

Gera, DO ZERO, o DOSSIÊ do PROJETO ELEITO (SWOT · PESTELC · 5W4H · Pareto · GUT · Radar)
em PARALELO (ProcessPoolExecutor) e AGORA por IDIOMA: as 6 imagens são renderizadas com o
texto interno traduzido, saindo em ../evidence/static/admtools/<lang>/*.png.

Strings: catálogo PT embutido (fallback) + traduções em _private/image_i18n.json (git-ignored).
Fontes por idioma (mpl fallback é instável): DejaVu (latino/cirílico) · WenQuanYi (中/한) ·
Noto Devanagari (हिन्दी) · Noto Hebrew (עברית).

Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
"""
import json
import os
import sqlite3
from concurrent.futures import ProcessPoolExecutor, as_completed

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["text.parse_math"] = False
import numpy as np
import matplotlib.patheffects as pe
from matplotlib.patches import FancyBboxPatch, RegularPolygon, Circle, Wedge

GLOW = [pe.withStroke(linewidth=2.4, foreground="#12202f")]
BASE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(BASE, "bsc_ia.db")
STATIC = os.path.join(BASE, "..", "evidence", "static", "admtools")
STAMP = ("Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard  ·  "
         "©️ Bruno Penedo — 2026 · linkedin.com/in/bpenedo · bpenedo@gmail.com")
AZUL, VERM, AMAR, VERD = "#2E75B6", "#C00000", "#FFC000", "#548235"
NAVY = "#1F3A5F"
LANGS = ["pt", "en", "es", "fr", "de", "zh", "ko", "hi", "he", "sv", "ru", "fi"]
FONT = {"zh": "WenQuanYi Zen Hei", "ko": "WenQuanYi Zen Hei",
        "hi": "Noto Sans Devanagari", "he": "Noto Sans Hebrew"}

# --------------------------------------------------------------------------- #
#  Catálogo de strings (PT = fallback). Traduções carregadas de _private/image_i18n.json.
# --------------------------------------------------------------------------- #
PT = {
 "crown": "Jóia da Coroa",
 "swot_sub": "Análise estratégica orientada a dados", "swot_t": "SWOT — {win}  ({crown})",
 "n_s": "Forças", "n_w": "Fraquezas", "n_o": "Oportunidades", "n_t": "Ameaças",
 "s1": "Menor alucinação do portfólio (IITA {iita}% vs média {a_iita}%)",
 "s2": "Menor desperdício Lean (IDLS {idls}% vs {a_idls}%)",
 "s3": "Entrega útil elevada (PEUC {peuc}%, ~{ratio}× média)",
 "s4": "PSR {psr} acima da média ({a_psr})",
 "w1": "PSR {psr} ainda abaixo da meta 4,0", "w2": "Fila/cota presente (IOLI {ioli}%)",
 "w3": "Fluxo de caixa REAL ainda não medido",
 "o1": "VPL R$ {vpl} · TIR {tir}% > SELIC", "o2": "Escalar piloto com eficiência já comprovada",
 "o3": "Reusar padrões de prompt de baixa alucinação",
 "t1": "Placeholder financeiro pode reordenar ranking", "t2": "Corrida de inovação tecnológica concorrente",
 "t3": "Dependência de cota de API (rate limit 429)",
 "pestel_sub": "Fatores macroambientais (7 dimensões)", "pestel_t": "PESTELC — {win}",
 "f_p": "Político", "f_e": "Econômico", "f_s": "Social", "f_t": "Tecnológico",
 "f_ec": "Ecológico", "f_l": "Legal", "f_c": "Cultural",
 "d_p": "Sem entraves políticos ao uso de IA hoje; monitorar marcos regulatórios de IA.",
 "d_e": "Custo por token em queda; retorno (TIR>SELIC) favorece a escala do eleito.",
 "d_s": "Gerações Y/Z demandam automação inteligente e resposta em tempo real.",
 "d_t": "Modelos evoluem rápido; eficiência (baixo IITA/IDLS) é vantagem sustentável.",
 "d_ec": "Menor desperdício de tokens reduz consumo computacional e energético.",
 "d_l": "LGPD e governança de dados; rastreabilidade via Langfuse mitiga risco.",
 "d_c": "Cultura data-driven (Kaplan): 'o que não é medido não é gerenciado'.",
 "w4h_t": "5W4H — Plano de Ação · {win}", "w4h_center": "Plano de Ação",
 "q_what": "O quê?", "q_why": "Por quê?", "q_where": "Onde?", "q_when": "Quando?",
 "q_who": "Quem?", "q_how": "Como?", "q_howmuch": "Quanto custa?", "q_howmany": "Quantos?", "q_howlong": "Quanto tempo?",
 "a_what": "Escalar {win} como piloto oficial de IA",
 "a_why": "Menor alucinação (IITA) e menor muda (IDLS) do portfólio",
 "a_where": "Pipeline BSC · Langfuse→SQLite→Evidence",
 "a_when": "Próximo sprint (weekly de sexta)", "a_who": "PM + Dev + revisor LLM-as-judge",
 "a_how": "Inserir fluxos de caixa reais + re-rodar AHP-TOPSIS",
 "a_howmuch": "Invest. ~R$ {inv} · VPL R$ {vpl}", "a_howmany": "Meta: TIR {tir}% · PSR 4,0",
 "a_howlong": "1 sprint p/ fluxos · payback ~{pb} períodos",
 "pareto_t": "Pareto de Falhas por Categoria de Prompt · {win}",
 "pareto_sub": "Priorize a cauda que concentra 80% das falhas (dados reais)",
 "pareto_y1": "Falhas (contagem)", "pareto_y2": "Acumulado %",
 "gut_t": "Matriz GUT — Priorização de Ações · {win}",
 "gut_sub": "Gravidade × Urgência × Tendência (1–5) · maior GUT = agir primeiro",
 "gut_c1": "Gravidade", "gut_c2": "Urgência", "gut_c3": "Tendência", "gut_c4": "GUT (G×U×T)",
 "gut_cbar": "Criticidade",
 "g1": "Inserir fluxos de caixa reais (fechar MCDA)", "g2": "Elevar PSR de {psr} → 4,0",
 "g3": "Reduzir IOLI (fila + backoff exponencial)", "g4": "Grounding RAG / citar fontes (↓ alucinação)",
 "g5": "Padronizar prompts de baixa alucinação",
 "radar_t": "Radar Competitivo — {win} vs Portfólio",
 "rad_psr": "PSR\n(qualidade)", "rad_peuc": "PEUC\n(entrega útil)", "rad_anti": "Anti-alucinação\n(100-IITA)",
 "rad_lean": "Lean\n(100-IDLS)", "rad_stab": "Estabilidade\n(100-IOLI)", "rad_cost": "Custo-efic.\n(CPP inv.)",
 "rad_avg": "Média do portfólio", "rad_win": "{win} (eleito)",
 # categorias de prompt (dados) — traduzíveis
 "cat_Conversa/Aberto": "Conversa/Aberto", "cat_RAG/Busca": "RAG/Busca",
 "cat_Transformacao/Formato": "Transformação/Formato", "cat_Raciocinio/Analise": "Raciocínio/Análise",
 "cat_Sumarizacao": "Sumarização", "cat_Geracao de Codigo": "Geração de Código",
 "cat_Extracao de Dados": "Extração de Dados",
}
_extra = os.path.join(BASE, "..", "_private", "image_i18n.json")
TXT = {"pt": PT}
if os.path.exists(_extra):
    try:
        for lang, d in json.load(open(_extra, encoding="utf-8")).items():
            TXT[lang] = d
    except Exception:
        pass


def S(key, D):
    tpl = TXT.get(D["lang"], {}).get(key) or PT.get(key, key)
    try:
        return tpl.format(**D["fmt"])
    except Exception:
        return tpl


def catn(cat, D):  # nome de categoria traduzido (fallback = valor de dados)
    return TXT.get(D["lang"], {}).get("cat_" + cat) or PT.get("cat_" + cat, cat)


# --------------------------------------------------------------------------- #
def carregar_contexto():
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
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
    avg = {k: media(k) for k in ("kpi_psr", "kpi_peuc", "kpi_iita", "kpi_idls_lean", "kpi_ioli", "kpi_itr", "kpi_cpp")}
    pareto = [dict(r) for r in c.execute("""
        SELECT prompt_categoria cat, COUNT(*) n,
               SUM(CASE WHEN tipo_erro NOT IN ('NENHUM','') AND tipo_erro IS NOT NULL THEN 1 ELSE 0 END) er
        FROM logs_langfuse WHERE project_name=? GROUP BY 1""", (W,))]
    fin = c.execute("SELECT * FROM vpl_resultado WHERE project_name=?", (W,)).fetchone()
    fin = dict(fin) if fin else {}
    c.close()
    me = {k: me.get(k) for k in me}
    fmt = {
        "win": W, "crown": "",
        "iita": me.get("kpi_iita", 0), "idls": me.get("kpi_idls_lean", 0), "psr": me.get("kpi_psr", 0),
        "peuc": me.get("kpi_peuc", 0), "ioli": me.get("kpi_ioli", 0),
        "a_iita": avg["kpi_iita"], "a_idls": avg["kpi_idls_lean"], "a_psr": avg["kpi_psr"],
        "ratio": round(me.get("kpi_peuc", 0) / max(avg["kpi_peuc"], 1), 1),
        "vpl": f"{fin.get('vpl', 0):,.0f}", "tir": f"{fin.get('tir', 0) * 100:.1f}",
        "inv": f"{abs(fin.get('vpl', 0)) * 0.5:,.0f}", "pb": f"{fin.get('payback_descontado', 0):.1f}",
    }
    return {"win": W, "ci": round(win["ci_final"], 4), "me": me, "avg": avg,
            "pareto": pareto, "fin": fin, "fmt": fmt}


def _rodape(fig):
    fig.text(0.5, 0.012, STAMP, ha="center", va="bottom", fontsize=6.5, color="#8a8f98")


def _titulo(ax, txt, sub=""):
    ax.set_title(txt, fontsize=17, fontweight="bold", color=NAVY, pad=14)
    if sub:
        ax.text(0.5, 1.005, sub, transform=ax.transAxes, ha="center", fontsize=9.5, color="#5b6672")


def _wrap(txt, width):
    import textwrap
    return "\n".join(textwrap.wrap(txt, width)) or txt


# --------------------------------------------------------------------------- #  1) SWOT
def fig_swot(D, path):
    S_ = [S(k, D) for k in ("s1", "s2", "s3", "s4")]
    Wk = [S(k, D) for k in ("w1", "w2", "w3")]
    O = [S(k, D) for k in ("o1", "o2", "o3")]
    T = [S(k, D) for k in ("t1", "t2", "t3")]
    cols = [("S", S("n_s", D), AZUL, S_), ("W", S("n_w", D), VERM, Wk),
            ("O", S("n_o", D), AMAR, O), ("T", S("n_t", D), VERD, T)]
    fig, ax = plt.subplots(figsize=(12.4, 7.6)); ax.axis("off")
    ax.set_xlim(0, 4); ax.set_ylim(0, 10)
    crown = TXT.get(D["lang"], {}).get("crown") or PT["crown"]
    _titulo(ax, PT["swot_t"].format(win=D["win"], crown=crown) if D["lang"] == "pt"
            else (TXT.get(D["lang"], {}).get("swot_t") or PT["swot_t"]).format(win=D["win"], crown=crown),
            S("swot_sub", D))
    for i, (L, name, col, items) in enumerate(cols):
        x = i + 0.5
        ax.add_patch(FancyBboxPatch((x - 0.44, 1.55), 0.88, 7.35,
                     boxstyle="round,pad=0.02,rounding_size=0.12", facecolor=col, edgecolor="white", lw=2))
        body = "\n\n".join("•  " + _wrap(t, 21) for t in items)
        ax.text(x - 0.385, 8.55, body, ha="left", va="top", color="white",
                fontsize=10.5, fontweight="medium", linespacing=1.45, path_effects=GLOW)
        ax.add_patch(Circle((x, 1.05), 0.45, facecolor="white", edgecolor=col, lw=3))
        ax.text(x, 1.1, L, ha="center", va="center", color=col, fontsize=22, fontweight="bold")
        ax.text(x, 0.32, name, ha="center", va="center", color="#333", fontsize=10.5, fontweight="bold")
    _rodape(fig)
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor="white"); plt.close(fig)
    return path


# --------------------------------------------------------------------------- #  2) PESTELC
def fig_pestel(D, path):
    fatores = [("P", S("f_p", D), VERD, S("d_p", D)), ("E", S("f_e", D), VERM, S("d_e", D)),
               ("S", S("f_s", D), AMAR, S("d_s", D)), ("T", S("f_t", D), AZUL, S("d_t", D)),
               ("E", S("f_ec", D), "#2E9E8F", S("d_ec", D)), ("L", S("f_l", D), "#7B4FA3", S("d_l", D)),
               ("C", S("f_c", D), "#E08A2B", S("d_c", D))]
    n = len(fatores)
    fig, ax = plt.subplots(figsize=(15, 8.6)); ax.axis("off")
    ax.set_xlim(0, n); ax.set_ylim(0, 7.6)
    _titulo(ax, (TXT.get(D["lang"], {}).get("pestel_t") or PT["pestel_t"]).format(win=D["win"]), S("pestel_sub", D))
    r = 0.58
    for i, (L, nome, col, txt) in enumerate(fatores):
        cx, cy = i + 0.5, 3.8
        ax.add_patch(RegularPolygon((cx, cy), 6, radius=r, orientation=np.pi/6, facecolor=col, edgecolor="white", lw=2))
        ax.text(cx, cy + 0.14, L, ha="center", va="center", color="white", fontsize=20, fontweight="bold", path_effects=GLOW)
        ax.text(cx, cy - 0.28, nome, ha="center", va="center", color="white", fontsize=11, fontweight="bold", path_effects=GLOW)
        up = i % 2 == 0
        ty = cy + 1.55 if up else cy - 1.55
        ax.annotate("", xy=(cx, ty), xytext=(cx, cy + (r if up else -r)), arrowprops=dict(arrowstyle="->", color="#8a97a6", lw=1.5))
        ax.text(cx, ty + (0.07 if up else -0.07), _wrap(txt, 20), ha="center", va="bottom" if up else "top",
                fontsize=11.5, fontweight="medium", color="#1f2b38", linespacing=1.34)
    _rodape(fig)
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor="white"); plt.close(fig)
    return path


# --------------------------------------------------------------------------- #  3) 5W4H
def fig_5w4h(D, path):
    QT = [("q_what", "What", "a_what", "#8E2434"), ("q_why", "Why", "a_why", "#B93A2B"),
          ("q_where", "Where", "a_where", "#D9752B"), ("q_when", "When", "a_when", "#E8A62B"),
          ("q_who", "Who", "a_who", "#F1C40F"), ("q_how", "How", "a_how", "#3FA36B"),
          ("q_howmuch", "How much", "a_howmuch", "#2E86AB"), ("q_howmany", "How many", "a_howmany", "#2C3E63"),
          ("q_howlong", "How long", "a_howlong", "#7B4FA3")]
    setores = [(f"{S(qk, D)}\n({en})", S(ak, D), col) for qk, en, ak, col in QT]
    fig, ax = plt.subplots(figsize=(8.6, 8.6)); ax.axis("off")
    ax.set_xlim(-1.38, 1.38); ax.set_ylim(-1.38, 1.38); ax.set_aspect("equal")
    fig.suptitle((TXT.get(D["lang"], {}).get("w4h_t") or PT["w4h_t"]).format(win=D["win"]),
                 fontsize=16, fontweight="bold", color=NAVY, y=0.965)
    n = len(setores); step = 360 / n
    for i, (q, ans, col) in enumerate(setores):
        a0 = 90 - i * step; a1 = a0 - step
        ax.add_patch(Wedge((0, 0), 1.0, a1, a0, width=0.62, facecolor=col, edgecolor="white", lw=2))
        mid = np.radians((a0 + a1) / 2)
        ax.text(0.69*np.cos(mid), 0.69*np.sin(mid), q, ha="center", va="center",
                color="white", fontsize=7.6, fontweight="bold", linespacing=1.05)
        ha = "left" if np.cos(mid) >= 0 else "right"
        ax.text(1.16*np.cos(mid), 1.16*np.sin(mid), _wrap(ans, 26), ha=ha, va="center", fontsize=7.2, color="#33404d")
    ax.add_patch(Circle((0, 0), 0.38, facecolor="white", edgecolor="#dcdcdc", lw=1.5))
    ax.text(0, 0.06, "5W4H", ha="center", va="center", fontsize=19, fontweight="bold", color=VERM)
    ax.text(0, -0.14, S("w4h_center", D), ha="center", va="center", fontsize=9, color="#5b6672")
    _rodape(fig)
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor="white"); plt.close(fig)
    return path


# --------------------------------------------------------------------------- #  4) PARETO
def fig_pareto(D, path):
    dat = sorted(D["pareto"], key=lambda r: r["er"], reverse=True)
    dat = [r for r in dat if r["er"] > 0] or dat
    cats = [catn(r["cat"], D) for r in dat]
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
    for xi, cc in zip(x, cum):
        ax2.text(xi, cc+2.5, f"{cc:.0f}%", ha="center", fontsize=8, color=VERM)
    ax.set_xticks(x); ax.set_xticklabels([_wrap(cc, 12) for cc in cats], fontsize=8)
    ax.set_ylabel(S("pareto_y1", D), color=NAVY); ax2.set_ylabel(S("pareto_y2", D), color=VERM)
    ax2.set_ylim(0, 112); ax.set_ylim(0, er.max()*1.25 if er.max() else 1)
    _titulo(ax, (TXT.get(D["lang"], {}).get("pareto_t") or PT["pareto_t"]).format(win=D["win"]), S("pareto_sub", D))
    ax.grid(axis="y", ls=":", alpha=.4, zorder=0)
    _rodape(fig)
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor="white"); plt.close(fig)
    return path


# --------------------------------------------------------------------------- #  5) GUT
def fig_gut(D, path):
    acoes = [(S("g1", D), 5, 5, 5), (S("g2", D), 4, 4, 4), (S("g3", D), 3, 4, 4),
             (S("g4", D), 4, 3, 3), (S("g5", D), 3, 3, 4)]
    acoes = sorted(acoes, key=lambda a: a[1]*a[2]*a[3], reverse=True)
    rot = [a[0] for a in acoes]
    M = np.array([[a[1], a[2], a[3], a[1]*a[2]*a[3]] for a in acoes], dtype=float)
    fig, ax = plt.subplots(figsize=(10.5, 5.6))
    disp = M.copy(); disp[:, 3] = disp[:, 3] / 125 * 5
    im = ax.imshow(disp, cmap="RdYlGn_r", aspect="auto", vmin=1, vmax=5)
    cols = [S("gut_c1", D), S("gut_c2", D), S("gut_c3", D), S("gut_c4", D)]
    ax.set_xticks(range(4)); ax.set_xticklabels(cols, fontsize=10, fontweight="bold")
    ax.set_yticks(range(len(rot))); ax.set_yticklabels([_wrap(r, 34) for r in rot], fontsize=9)
    for i in range(len(rot)):
        for j in range(4):
            ax.text(j, i, int(M[i, j]), ha="center", va="center", fontsize=11, fontweight="bold",
                    color="#111" if disp[i, j] < 3.5 else "white")
    _titulo(ax, (TXT.get(D["lang"], {}).get("gut_t") or PT["gut_t"]).format(win=D["win"]), S("gut_sub", D))
    fig.colorbar(im, ax=ax, shrink=.8, label=S("gut_cbar", D))
    _rodape(fig)
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor="white"); plt.close(fig)
    return path


# --------------------------------------------------------------------------- #  6) RADAR
def fig_radar(D, path):
    me, avg = D["me"], D["avg"]
    eixos = [S(k, D) for k in ("rad_psr", "rad_peuc", "rad_anti", "rad_lean", "rad_stab", "rad_cost")]

    def vetor(src):
        cpp = src.get("kpi_cpp", 1) or 1; cpp_avg = avg["kpi_cpp"] or 1
        return [(src.get("kpi_psr", 0)/5)*100, src.get("kpi_peuc", 0), max(0, 100-src.get("kpi_iita", 0)),
                max(0, 100-src.get("kpi_idls_lean", 0)), max(0, 100-src.get("kpi_ioli", 0)),
                min(100, cpp_avg/cpp*60)]
    v_me, v_avg = vetor(me), vetor(avg)
    N = len(eixos)
    ang = np.linspace(0, 2*np.pi, N, endpoint=False).tolist(); ang += ang[:1]
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    for vals, col, lab, fill in [(v_avg, "#9aa4af", S("rad_avg", D), 0.10), (v_me, AZUL, S("rad_win", D), 0.28)]:
        vv = vals + vals[:1]
        ax.plot(ang, vv, "-o", color=col, lw=2, label=lab); ax.fill(ang, vv, color=col, alpha=fill)
    ax.set_xticks(ang[:-1]); ax.set_xticklabels(eixos, fontsize=9)
    ax.set_ylim(0, 100); ax.set_yticks([20, 40, 60, 80, 100])
    ax.set_yticklabels(["20", "40", "60", "80", "100"], fontsize=7, color="#888")
    ax.set_title((TXT.get(D["lang"], {}).get("radar_t") or PT["radar_t"]).format(win=D["win"]),
                 fontsize=15, fontweight="bold", color=NAVY, pad=26)
    ax.legend(loc="upper right", bbox_to_anchor=(1.16, 1.12), fontsize=9)
    _rodape(fig)
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor="white"); plt.close(fig)
    return path


def _worker(args):
    nome, path, D = args
    fnt = FONT.get(D["lang"], "DejaVu Sans")
    matplotlib.rcParams["font.family"] = [fnt, "DejaVu Sans"]
    return {"swot": fig_swot, "pestel": fig_pestel, "5w4h": fig_5w4h,
            "pareto": fig_pareto, "gut": fig_gut, "radar": fig_radar}[nome](D, path)


def main():
    import sys
    base = carregar_contexto()
    langs = sys.argv[1:] or LANGS
    print(f"🏆 Projeto eleito: {base['win']} (Ci={base['ci']}) · idiomas: {', '.join(langs)}")
    tarefas = []
    for lang in langs:
        D = dict(base, lang=lang)
        outdir = os.path.join(STATIC, lang)
        os.makedirs(outdir, exist_ok=True)
        for n in ("swot", "pestel", "5w4h", "pareto", "gut", "radar"):
            tarefas.append((n, os.path.join(outdir, f"{n}.png"), D))
    ok = 0
    with ProcessPoolExecutor(max_workers=min(8, os.cpu_count() or 4)) as ex:
        futs = {ex.submit(_worker, t): (t[0], t[2]["lang"]) for t in tarefas}
        for f in as_completed(futs):
            n, lg = futs[f]
            try:
                f.result(); ok += 1
            except Exception as e:
                print(f"   ✗ {lg}/{n}: {e}")
    print(f"✅ Dossiê i18n: {ok}/{len(tarefas)} imagens em admtools/<lang>/ ({len(langs)} idiomas)")


if __name__ == "__main__":
    main()
