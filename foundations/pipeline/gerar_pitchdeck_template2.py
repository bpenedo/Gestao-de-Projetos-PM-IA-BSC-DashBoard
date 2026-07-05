"""
gerar_pitchdeck_template2.py — SEGUNDO template de Pitch Deck (layout alternativo ao template 1).

Layout: banner superior full-width (teal) + faixa de 4 KPI-cards + corpo em 2 colunas
+ rodapé de FINANCIALS (fluxo de caixa descontado). Distinto do template 1 (sidebar navy).

Gera um PDF GENÉRICO e ANÔNIMO (placeholders entre colchetes) para uso como BASE reutilizável:
    foundations/pitchdeck/Pitch Deck Template.pdf

Uso:
    python3 gerar_pitchdeck_template2.py            # gera o template genérico (placeholders)
Requer tectonic (compilador LaTeX). Edite os campos [ENTRE COLCHETES] por projeto antes de apresentar.

Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
"""
import os
import subprocess
import tempfile
from pathlib import Path

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = Path(BASE).parent / "pitchdeck" / "Pitch Deck Template.pdf"
STAMP = ("Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard "
         "\\textcopyright~Bruno Penedo -- 2026. linkedin.com/in/bpenedo -- bpenedo@gmail.com")


def _sec(titulo, itens):
    linhas = r" \\ ".join(rf"\small $\bullet$ {t}" for t in itens)
    return (rf"\textbf{{\textcolor{{teal}}{{{titulo}}}}}\\[1pt] {linhas}\\[9pt]")


def _tex():
    esq = "".join([
        _sec("PITCH", ["[Visão e missão da iniciativa de IA em uma frase]"]),
        _sec("PROBLEMA / OPORTUNIDADE", ["[Dor do mercado-alvo]", "[Tamanho da oportunidade]"]),
        _sec("SOLUCAO / PRODUTO", ["[Como o projeto resolve, medido pelos KPIs do framework]"]),
        _sec("MODELO DE NEGOCIO", ["[Como gera receita/margem]", "[Precificacao]"]),
        _sec("MERCADO", ["[TAM/SAM/SOM]", "[Perfil do cliente]"]),
    ])
    dir_ = "".join([
        _sec("CONCORRENTES", ["[Principais players e riscos externos]"]),
        _sec("VANTAGEM COMPETITIVA", ["[Diferenciais: kTR, PSR, baixa alucinacao (IITA), Lean (IDLS)]"]),
        _sec("EXECUCAO / GO-TO-MARKET", ["[Milestones e plano de execucao]"]),
        _sec("TRACAO", ["[KPIs alcancados: PSR, PEUC, CPP, Burn Rate]"]),
        _sec("USE OF FUNDS", ["40\\% Produto/IA $\\cdot$ 25\\% GTM $\\cdot$ 20\\% Operacao $\\cdot$ 15\\% Reserva"]),
    ])
    kpi = (r"\newcommand{\kpi}[2]{\colorbox{soft}{\parbox[t][1.35cm][c]"
           r"{\dimexpr0.235\textwidth-2\fboxsep}{\centering\color{ink}"
           r"{\footnotesize #1}\\[3pt]{\Large\bfseries #2}}}}")
    fin_rows = r"""
0 & [invest.] & [invest.] & [acum.]\\
1 & [fluxo 1] & [desc. 1] & [acum. 1]\\
2 & [fluxo 2] & [desc. 2] & [acum. 2]\\
3 & [fluxo 3] & [desc. 3] & [acum. 3]\\
4 & [fluxo 4] & [desc. 4] & [acum. 4]\\
5 & [fluxo 5] & [desc. 5] & [acum. 5]\\
"""
    return rf"""\documentclass[10pt]{{extarticle}}
\usepackage[a4paper,margin=1cm]{{geometry}}
\usepackage[T1]{{fontenc}}
\usepackage[utf8]{{inputenc}}
\usepackage{{xcolor}}
\usepackage{{array}}
\usepackage{{helvet}}
\renewcommand{{\familydefault}}{{\sfdefault}}
\definecolor{{teal}}{{HTML}}{{0E7C86}}
\definecolor{{ink}}{{HTML}}{{16303B}}
\definecolor{{soft}}{{HTML}}{{EAF2F3}}
\pagestyle{{empty}}
\setlength{{\parindent}}{{0pt}}
\setlength{{\fboxsep}}{{6pt}}
{kpi}
\begin{{document}}

\colorbox{{teal}}{{\parbox[t]{{\dimexpr\textwidth-2\fboxsep}}{{\color{{white}}
{{\LARGE\bfseries [NOME DO PROJETO]}}\\[2pt]
{{\large EXECUTIVE PITCH DECK \textbullet{{}} TEMPLATE 2}}\\[1pt]}}}}

\vspace{{7pt}}
\kpi{{VPL (R\$)}}{{[VPL]}}\hfill\kpi{{TIR}}{{[TIR]}}\hfill\kpi{{ILL (PI)}}{{[ILL]}}\hfill\kpi{{PSR (0-5)}}{{[PSR]}}

\vspace{{10pt}}
\begin{{minipage}}[t]{{0.485\textwidth}}
{esq}
\end{{minipage}}\hfill
\begin{{minipage}}[t]{{0.485\textwidth}}
{dir_}
\end{{minipage}}

\vfill
\colorbox{{ink}}{{\parbox{{\dimexpr\textwidth-2\fboxsep}}{{\color{{white}}\centering\bfseries
FINANCIALS \textbullet{{}} Fluxo de Caixa Descontado}}}}
\vspace{{4pt}}
{{\centering\small
\begin{{tabular}}{{>{{\centering\arraybackslash}}p{{0.14\textwidth}}|>{{\centering\arraybackslash}}p{{0.24\textwidth}}|>{{\centering\arraybackslash}}p{{0.24\textwidth}}|>{{\centering\arraybackslash}}p{{0.24\textwidth}}}}
\textbf{{Periodo}} & \textbf{{Fluxo}} & \textbf{{Fluxo desc.}} & \textbf{{Acum. desc.}}\\ \hline
{fin_rows}
\end{{tabular}}\par}}

\vspace{{6pt}}
{{\centering\footnotesize {STAMP}\par}}
\end{{document}}
"""


def main():
    tex = _tex()
    with tempfile.TemporaryDirectory() as tmp:
        tf = Path(tmp) / "template2.tex"
        tf.write_text(tex, encoding="utf-8")
        try:
            r = subprocess.run(["tectonic", "-o", tmp, str(tf)],
                               capture_output=True, text=True)
        except FileNotFoundError:
            print("⚠️  tectonic não instalado — não foi possível gerar o PDF.")
            return
        pdf = Path(tmp) / "template2.pdf"
        if r.returncode != 0 or not pdf.exists():
            print("⚠️  Falha ao compilar:\n", r.stderr[-1500:])
            return
        OUT.parent.mkdir(exist_ok=True)
        OUT.write_bytes(pdf.read_bytes())
    print(f"✅ Template 2 gerado (genérico/anônimo): {OUT}")


if __name__ == "__main__":
    main()
