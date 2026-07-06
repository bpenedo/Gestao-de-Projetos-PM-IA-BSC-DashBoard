"""
Gera o MAPA 5D do portfólio de projetos de IA (estilo 5dchart.com — esferas 3D
glossy) usando a lib render_5d vendorizada localmente (pipeline/fivedchart_lib.py).

i18n (Passo 2): gera uma versão POR IDIOMA com os rótulos internos traduzidos.
  pt  -> 5d_projetos.png   (referenciada pela página PT)
  <l> -> 5d_<l>.png        (en/es/fr/de/zh/ko/hi/he/sv/ru/fi)
Fontes com fallback por glifo (mpl 3.11): DejaVu (latino/cirílico) + WenQuanYi (CJK/한글)
+ Noto Devanagari (हिन्दी) + Noto Hebrew (עברית).

5 dimensões: X=Volume(tokens) · Y=PEUC% · Z=PSR(0-5) · tamanho=Burn Rate · cor=ICCA.
Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
"""
import sys

import matplotlib
matplotlib.rcParams["font.family"] = "sans-serif"
matplotlib.rcParams["font.sans-serif"] = [
    "DejaVu Sans", "WenQuanYi Zen Hei", "Noto Sans Devanagari", "Noto Sans Hebrew"]
matplotlib.rcParams["axes.unicode_minus"] = False

from db import get_conn
from config import QUERIES_DIR, FOUNDATIONS_DIR
from fivedchart_lib import render_5d

STATIC = FOUNDATIONS_DIR / "evidence" / "static"

# Catálogo de rótulos por idioma (KPIs/siglas e R$ preservados).
STR = {
 "pt": ("Mapa 5D do Portfólio de Projetos de IA — visão C-Level",
        ["Volume (tokens) — escala", "PEUC % — qualidade", "PSR (0-5) — saúde"],
        "Dim.5 — ICCA (sustentabilidade: verde > 3x)", "Dim.4 — Burn Rate de IA (R$)",
        "X=escala(tokens)  Y=qualidade(PEUC)  Z=saúde(PSR)  |  tamanho=burn rate  cor=ICCA"),
 "en": ("5D Map of the AI Project Portfolio — C-Level view",
        ["Volume (tokens) — scale", "PEUC % — quality", "PSR (0-5) — health"],
        "Dim.5 — ICCA (sustainability: green > 3x)", "Dim.4 — AI Burn Rate (R$)",
        "X=scale(tokens)  Y=quality(PEUC)  Z=health(PSR)  |  size=burn rate  color=ICCA"),
 "es": ("Mapa 5D del portafolio de proyectos de IA — visión C-Level",
        ["Volumen (tokens) — escala", "PEUC % — calidad", "PSR (0-5) — salud"],
        "Dim.5 — ICCA (sostenibilidad: verde > 3x)", "Dim.4 — Burn Rate de IA (R$)",
        "X=escala(tokens)  Y=calidad(PEUC)  Z=salud(PSR)  |  tamaño=burn rate  color=ICCA"),
 "fr": ("Carte 5D du portefeuille de projets IA — vue C-Level",
        ["Volume (tokens) — échelle", "PEUC % — qualité", "PSR (0-5) — santé"],
        "Dim.5 — ICCA (durabilité : vert > 3x)", "Dim.4 — Burn Rate IA (R$)",
        "X=échelle(tokens)  Y=qualité(PEUC)  Z=santé(PSR)  |  taille=burn rate  couleur=ICCA"),
 "de": ("5D-Karte des KI-Projektportfolios — C-Level-Sicht",
        ["Volumen (Tokens) — Skala", "PEUC % — Qualität", "PSR (0-5) — Gesundheit"],
        "Dim.5 — ICCA (Nachhaltigkeit: grün > 3x)", "Dim.4 — KI-Burn-Rate (R$)",
        "X=Skala(Tokens)  Y=Qualität(PEUC)  Z=Gesundheit(PSR)  |  Größe=Burn Rate  Farbe=ICCA"),
 "zh": ("AI 项目组合 5D 地图 — C 级视图",
        ["体量（Token）— 规模", "PEUC % — 质量", "PSR (0-5) — 健康"],
        "维度5 — ICCA（可持续性：绿 > 3x）", "维度4 — AI 消耗率 (R$)",
        "X=规模(Token)  Y=质量(PEUC)  Z=健康(PSR)  |  大小=消耗率  颜色=ICCA"),
 "ko": ("AI 프로젝트 포트폴리오 5D 지도 — C-레벨 관점",
        ["규모(토큰) — 스케일", "PEUC % — 품질", "PSR (0-5) — 건전성"],
        "차원5 — ICCA (지속가능성: 초록 > 3x)", "차원4 — AI 소진율 (R$)",
        "X=규모(토큰)  Y=품질(PEUC)  Z=건전성(PSR)  |  크기=소진율  색=ICCA"),
 "hi": ("AI परियोजना पोर्टफोलियो का 5D मानचित्र — C-लेवल दृश्य",
        ["आयतन (टोकन) — पैमाना", "PEUC % — गुणवत्ता", "PSR (0-5) — स्वास्थ्य"],
        "आयाम5 — ICCA (संधारणीयता: हरा > 3x)", "आयाम4 — AI बर्न रेट (R$)",
        "X=पैमाना(टोकन)  Y=गुणवत्ता(PEUC)  Z=स्वास्थ्य(PSR)  |  आकार=बर्न रेट  रंग=ICCA"),
 "he": ("מפת 5D של תיק פרויקטי ה-AI — מבט דרג בכיר",
        ["נפח (טוקנים) — היקף", "PEUC % — איכות", "PSR (0-5) — בריאות"],
        "ממד5 — ICCA (קיימות: ירוק > 3x)", "ממד4 — Burn Rate של AI (R$)",
        "X=היקף(טוקנים)  Y=איכות(PEUC)  Z=בריאות(PSR)  |  גודל=burn rate  צבע=ICCA"),
 "sv": ("5D-karta över AI-projektportföljen — C-nivåvy",
        ["Volym (tokens) — skala", "PEUC % — kvalitet", "PSR (0-5) — hälsa"],
        "Dim.5 — ICCA (hållbarhet: grön > 3x)", "Dim.4 — AI Burn Rate (R$)",
        "X=skala(tokens)  Y=kvalitet(PEUC)  Z=hälsa(PSR)  |  storlek=burn rate  färg=ICCA"),
 "ru": ("5D-карта портфеля ИИ-проектов — взгляд C-уровня",
        ["Объём (токены) — масштаб", "PEUC % — качество", "PSR (0-5) — здоровье"],
        "Изм.5 — ICCA (устойчивость: зелёный > 3x)", "Изм.4 — Burn Rate ИИ (R$)",
        "X=масштаб(токены)  Y=качество(PEUC)  Z=здоровье(PSR)  |  размер=burn rate  цвет=ICCA"),
 "fi": ("Tekoälyprojektisalkun 5D-kartta — johtotason näkymä",
        ["Volyymi (tokenit) — mittakaava", "PEUC % — laatu", "PSR (0-5) — terveys"],
        "Ulottuvuus 5 — ICCA (kestävyys: vihreä > 3x)", "Ulottuvuus 4 — Tekoälyn Burn Rate (R$)",
        "X=mittakaava(tokenit)  Y=laatu(PEUC)  Z=terveys(PSR)  |  koko=burn rate  väri=ICCA"),
}


def _items():
    sql = (QUERIES_DIR / "kpis_bsc_ia.sql").read_text(encoding="utf-8")
    conn = get_conn()
    rows = conn.execute(sql).fetchall()
    conn.close()
    return [dict(x=float(r["total_tokens"] or 0), y=float(r["kpi_peuc"] or 0),
                 z=float(r["kpi_psr"] or 0), s=max(float(r["burn_rate_ia"] or 0), 1.0),
                 c=float(r["kpi_icca"] or 0), lbl=r["project_name"]) for r in rows]


# Fonte por idioma (cobre o script + latino/dígitos; fallback automático é instável no mpl).
FONT = {"zh": "WenQuanYi Zen Hei", "ko": "WenQuanYi Zen Hei",
        "hi": "Noto Sans Devanagari", "he": "Noto Sans Hebrew"}


def gerar(lang, items):
    fnt = FONT.get(lang, "DejaVu Sans")
    # font.family como LISTA (após o import da lib, que fixa 'DejaVu Sans') → fallback por glifo:
    # fonte do idioma primeiro (script + latino), DejaVu para pontuação/latino residual.
    matplotlib.rcParams["font.family"] = [fnt, "DejaVu Sans"]
    title, axes, color_label, size_title, note = STR[lang]
    out = STATIC / ("5d_projetos.png" if lang == "pt" else f"5d_{lang}.png")
    render_5d(items, axes, title, str(out), color_mode="value", cmap="RdYlGn",
              color_label=color_label, size_legend_title=size_title,
              size_fmt=lambda v: f"R$ {v:,.0f}", note=note)
    return out


def main():
    items = _items()
    if not items:
        print("⚠️  Sem dados — rode ./run_all.sh primeiro.")
        return
    langs = sys.argv[1:] or list(STR)
    for l in langs:
        out = gerar(l, items)
        print(f"  ✓ {out.name}")
    print(f"✅ 5D gerado ({len(items)} projetos) para: {', '.join(langs)}")


if __name__ == "__main__":
    main()
