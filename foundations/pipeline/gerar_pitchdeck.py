"""
Gera o PITCH DECK (1 página, estilo do exemplo pitchdeck/pitch sample.jpg) para CADA projeto
que tenha VPL > 0 e ILL > 1 em BRL **e** em USD (ILL é adimensional → igual nas duas moedas;
exige-se também vpl > 0 e vpl_usd > 0).

Saída na pasta foundations/pitchdeck/:
  - pitchdeck_<projeto>_DDMMAAAA.md   (markdown)
  - pitchdeck_<projeto>_DDMMAAAA.pdf  (LaTeX compilado com tectonic)

Uso:  python3 gerar_pitchdeck.py ["Nome do Projeto"]   (sem arg = todos os elegíveis)
Autor: Bruno Teixeira Penedo.
"""
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

from db import get_conn
from config import QUERIES_DIR, FOUNDATIONS_DIR

PITCH_DIR = FOUNDATIONS_DIR / "pitchdeck"
HOJE = datetime.now().strftime("%d%m%Y")


def _tex_escape(s):
    s = str(s)
    # normaliza unicode sem glifo no Latin Modern
    for a, b in [("—", "--"), ("–", "-"), ("·", "-"), ("“", '"'), ("”", '"'),
                 ("’", "'"), ("‘", "'"), ("→", "->")]:
        s = s.replace(a, b)
    for a, b in [("\\", r"\textbackslash{}"), ("&", r"\&"), ("%", r"\%"), ("$", r"\$"),
                 ("#", r"\#"), ("_", r"\_"), ("{", r"\{"), ("}", r"\}"), ("~", r"\textasciitilde{}"),
                 ("^", r"\textasciicircum{}")]:
        s = s.replace(a, b)
    return s


def _dados():
    conn = get_conn()
    kpis = {r["project_name"]: r for r in conn.execute(
        (QUERIES_DIR / "kpis_bsc_ia.sql").read_text()).fetchall()}
    vpl = {r["project_name"]: r for r in conn.execute("SELECT * FROM vpl_resultado").fetchall()}
    fluxo = {}
    for r in conn.execute("SELECT * FROM vpl_fluxo ORDER BY project_name, periodo").fetchall():
        fluxo.setdefault(r["project_name"], []).append(r)
    conn.close()
    return kpis, vpl, fluxo


def _conteudo(proj, k, v, fl):
    """Monta os campos do pitch (financeiros reais + texto-template editável)."""
    money = lambda x: f"R$ {x:,.0f}".replace(",", ".")
    usd = lambda x: f"US$ {x:,.0f}".replace(",", ".")
    return {
        "nome": proj,
        "vpl": money(v["vpl"]), "vpl_usd": usd(v["vpl_usd"]),
        "tir": f"{v['tir']*100:.1f}%" if v["tir"] is not None else "n/d",
        "ill": f"{v['ill']:.2f}" if v["ill"] is not None else "n/d",
        "pb": f"{v['payback_descontado']:.1f}" if v["payback_descontado"] is not None else "n/d",
        "pb_usd": f"{v['payback_desc_usd']:.1f}" if v["payback_desc_usd"] is not None else "n/d",
        "psr": f"{k['kpi_psr']:.2f}", "cpp": money(k["kpi_cpp"]),
        "burn": money(k["burn_rate_ia"]), "peuc": f"{k['kpi_peuc']:.0f}%",
        "icca": f"{k['kpi_icca']:.2f}x",
        "selic": f"{v['selic']*100:.1f}%", "us_rate": f"{v['us_rate']*100:.1f}%",
        "fluxo": fl,
        # Campos qualitativos (template editável):
        "pitch": "Iniciativa de IA medida ponta a ponta pelo Framework BSC PM IA: entrega valor "
                 "mensurável com eficiência de tokens, qualidade de entrega e retorno financeiro positivo.",
        "problema": "Projetos de IA escalam custo de tokens e alucinação sem visibilidade de retorno, "
                    "corroendo margem antes de provar valor.",
        "solucao": "Painel BSC que mede custo (VRT/CPP), qualidade (PEUC), desperdício (Lean) e retorno "
                   "(VPL/TIR/ILL), com RCA de alucinação e plano de melhoria contínua (PDCA).",
        "modelo": "Receita recorrente (assinatura/uso) com margem protegida pelo controle de Burn Rate "
                  "e cobertura de custo (ICCA).",
        "mercado": "Empresas e produtos que constroem soluções com LLMs e precisam provar ROI por projeto.",
        "concorrentes": "Observabilidade de LLM genérica (sem BSC/finanças) e planilhas manuais sem RCA.",
        "vantagem": "Unidade de recuperação tokenizável (kTR), Score PSR 0-5 e RCA por taxonomia de prompt "
                    "— diagnóstico financeiro + operacional num só painel.",
        "gtm": "Onboard por projeto (tag no Langfuse) -> dashboard automático -> checkpoint semanal -> "
               "decisões de escala guiadas por VPL/TIR vs. SELIC e juros dos EUA.",
        "tracao": f"PSR {k['kpi_psr']:.2f}/5 | PEUC {k['kpi_peuc']:.0f}% | ICCA {k['kpi_icca']:.2f}x | "
                  f"VPL {money(v['vpl'])} | TIR {v['tir']*100:.1f}%.",
    }


def _md(c):
    fin = "\n".join(f"| {r['periodo']} | {r['fluxo']:,.0f} | {r['fluxo_desc']:,.0f} | {r['cum_desc']:,.0f} |"
                    for r in c["fluxo"])
    return f"""# 📈 Pitch Deck — {c['nome']}
*Gerado em {datetime.now():%d/%m/%Y} · Framework BSC PM IA (Bruno Teixeira Penedo)*

## Executive Summary
- **PITCH:** {c['pitch']}
- **PROBLEMA/OPORTUNIDADE:** {c['problema']}
- **SOLUÇÃO/PRODUTO:** {c['solucao']}
- **MODELO DE NEGÓCIO:** {c['modelo']}
- **MERCADO:** {c['mercado']}
- **CONCORRENTES:** {c['concorrentes']}
- **VANTAGEM COMPETITIVA:** {c['vantagem']}
- **GO-TO-MARKET:** {c['gtm']}
- **TRAÇÃO:** {c['tracao']}

## Financial Information
| Métrica | BRL | USD |
|---|---|---|
| VPL | {c['vpl']} | {c['vpl_usd']} |
| TIR | {c['tir']} | — |
| ILL (PI) | {c['ill']} | {c['ill']} |
| Payback descontado | {c['pb']} per. | {c['pb_usd']} per. |
| Benchmarks | SELIC {c['selic']} | EUA {c['us_rate']} |

**KPIs:** PSR {c['psr']}/5 · CPP {c['cpp']}/% · Burn {c['burn']} · PEUC {c['peuc']} · ICCA {c['icca']}

## Fluxo de Caixa (descontado)
| Período | Fluxo | Fluxo desc. | Acum. desc. |
|---|---|---|---|
{fin}
"""


def _tex(c):
    e = _tex_escape
    fin_rows = " \\\\\n".join(
        f"{r['periodo']} & {r['fluxo']:,.0f} & {r['fluxo_desc']:,.0f} & {r['cum_desc']:,.0f}".replace(",", ".")
        for r in c["fluxo"])

    def sec(icon, titulo, txt):
        return rf"\textbf{{\textcolor{{navy}}{{{e(icon)}~{e(titulo)}}}}}\\ \small {e(txt)}\\[12pt]"

    main = "\n".join([
        sec(">", "PITCH", c["pitch"]),
        sec("?", "PROBLEMA / OPORTUNIDADE", c["problema"]),
        sec("*", "SOLUCAO / PRODUTO", c["solucao"]),
        sec("$", "MODELO DE NEGOCIO", c["modelo"]),
        sec("#", "MERCADO", c["mercado"]),
        sec("=", "CONCORRENTES", c["concorrentes"]),
        sec("+", "VANTAGEM COMPETITIVA", c["vantagem"]),
        sec(">", "EXECUCAO / GO-TO-MARKET", c["gtm"]),
        sec("@", "TRACAO", c["tracao"]),
    ])
    side = rf"""
\textbf{{FINANCIAL INFORMATION}}\\[2pt]
\small Stage: Demo / pronto\\
VPL (BRL): {e(c['vpl'])}\\
VPL (USD): {e(c['vpl_usd'])}\\
TIR: {e(c['tir'])} \quad ILL: {e(c['ill'])}\\
Payback desc.: {e(c['pb'])} per. (BRL) / {e(c['pb_usd'])} (USD)\\
SELIC: {e(c['selic'])} \quad EUA: {e(c['us_rate'])}\\[6pt]
\textbf{{KPIs (BSC)}}\\[2pt]
\small PSR: {e(c['psr'])}/5\\
CPP: {e(c['cpp'])}/\%\\
Burn Rate: {e(c['burn'])}\\
PEUC: {e(c['peuc'])} \quad ICCA: {e(c['icca'])}\\[6pt]
\textbf{{USE OF FUNDS}}\\[2pt]
\small 40\% Produto/IA\\ 25\% Go-to-Market\\ 20\% Operacao\\ 15\% Reserva\\[6pt]
\textbf{{TEAM}}\\[2pt]
\small Founder \& PM -- Framework BSC PM IA\\
"""
    return rf"""\documentclass[10pt]{{extarticle}}
\usepackage[a4paper,margin=1cm]{{geometry}}
\usepackage{{xcolor}}
\usepackage[T1]{{fontenc}}
\usepackage[utf8]{{inputenc}}
\usepackage{{array}}
\definecolor{{navy}}{{HTML}}{{1F3A5F}}
\pagestyle{{empty}}
\setlength{{\parindent}}{{0pt}}
\begin{{document}}
\colorbox{{navy}}{{\parbox{{\dimexpr\textwidth-2\fboxsep}}{{\color{{white}}\centering
\LARGE\textbf{{{e(c['nome'])}}} \\ \normalsize EXECUTIVE SUMMARY -- PITCH DECK }}}}
\\[8pt]
\begin{{minipage}}[t]{{0.33\textwidth}}
\colorbox{{navy}}{{\parbox[t][0.62\textheight][t]{{\dimexpr\linewidth-2\fboxsep}}{{\color{{white}}
{side}
}}}}
\end{{minipage}}\hfill
\begin{{minipage}}[t]{{0.63\textwidth}}
{main}
\end{{minipage}}
\\[8pt]
\colorbox{{navy}}{{\parbox{{\dimexpr\textwidth-2\fboxsep}}{{\color{{white}}\centering\textbf{{FINANCIALS -- Fluxo de Caixa Descontado}}}}}}
\\[2pt]
\begin{{center}}
\begin{{tabular}}{{>{{\bfseries}}c c c c}}
Periodo & Fluxo & Fluxo desc. & Acum. desc.\\ \hline
{fin_rows}\\
\end{{tabular}}
\end{{center}}

\vspace{{8pt}}
{{\centering\footnotesize Framework BSC PM IA \textcopyright Bruno Teixeira Penedo -- 2026.\par}}
\end{{document}}
"""


def gerar(proj, c):
    PITCH_DIR.mkdir(exist_ok=True)
    slug = proj.lower().replace(" ", "_")
    base = PITCH_DIR / f"pitchdeck_{slug}_{HOJE}"
    base.with_suffix(".md").write_text(_md(c), encoding="utf-8")
    tex = _tex(c)
    with tempfile.TemporaryDirectory() as tmp:
        tf = Path(tmp) / "pitch.tex"
        tf.write_text(tex, encoding="utf-8")
        try:
            r = subprocess.run(["tectonic", "-o", tmp, str(tf)], capture_output=True, text=True)
        except FileNotFoundError:
            return False, "tectonic não instalado (só o .md foi gerado)"
        pdf = Path(tmp) / "pitch.pdf"
        if pdf.exists():
            base.with_suffix(".pdf").write_bytes(pdf.read_bytes())
            return True, base.with_suffix(".pdf")
        return False, r.stderr[-400:]


def main():
    kpis, vpl, fluxo = _dados()
    alvo = sys.argv[1] if len(sys.argv) > 1 else None
    elegiveis = [p for p, v in vpl.items()
                 if v["vpl"] and v["vpl"] > 0 and v["vpl_usd"] and v["vpl_usd"] > 0
                 and v["ill"] and v["ill"] > 1.0 and (alvo is None or p == alvo)]
    if not elegiveis:
        print("⚠️  Nenhum projeto elegível (precisa VPL>0 e ILL>1 em BRL e USD).")
        return
    print(f"Elegíveis (VPL+ILL positivos em BRL e USD): {', '.join(sorted(elegiveis))}")
    for proj in sorted(elegiveis):
        c = _conteudo(proj, kpis[proj], vpl[proj], fluxo.get(proj, []))
        ok, info = gerar(proj, c)
        print(f"  {'✅' if ok else '❌'} {proj} -> {info}")


if __name__ == "__main__":
    main()
