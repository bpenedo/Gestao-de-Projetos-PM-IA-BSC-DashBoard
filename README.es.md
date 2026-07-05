# 🧭 Framework VPL — Gestión de Proyectos (PM) de IA con Panel BSC y Dashboard

🌐 [Português](README.md) · [English](README.en.md) · **Español** · [Français](README.fr.md) · [Deutsch](README.de.md) · [中文](README.zh.md) · [한국어](README.ko.md) · [हिन्दी](README.hi.md) · [עברית](README.he.md) · [Svenska](README.sv.md) · [Русский](README.ru.md) · [Suomi](README.fi.md)

![Method](https://img.shields.io/badge/method-Balanced%20Scorecard-1F3A5F)
![AI](https://img.shields.io/badge/AI-LLM%20observability-45a1bf)
![Finance](https://img.shields.io/badge/finance-VAN%20·%20TIR%20·%20IR-46a485)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-PyO3-orange?logo=rust&logoColor=white)
![Dashboard](https://img.shields.io/badge/dashboard-Evidence-236aa4)
![PDF](https://img.shields.io/badge/pitch%20deck-LaTeX-008080)
![status](https://img.shields.io/badge/status-v1-success)

> Un framework para **medir cualquier proyecto de IA de principio a fin** — del consumo de tokens al
> retorno financiero — bajo las 4 perspectivas del **Balanced Scorecard** (Kaplan & Norton).
>
> *"Lo que no se mide no se puede gestionar ni mejorar."*

> *Cuando ores y estudies, no dejes que [mis palabras] te abandonen. Con cada palabra y expresión que sale de tus labios, ten presente traer una Unificación.* — Aryeh Kaplan

> *La metafísica pura, situándose por esencia por encima y más allá de todas las formas y contingencias, no es ni oriental ni occidental: es universal.* — René Guénon

> *Conocerse a sí mismo es conocer el propio linaje y el propio poder.* — Harvey Spencer Lewis

> *Scientia es Lux Lucis* ∞ Sapere Aude S∴A∴☬ ☿

> 📖 **Documentación principal:** **[`foundations/README.md`](foundations/README.md)** ·
> ⚙️ **Configuración (usa tus propias claves):** [`foundations/pipeline/SETUP.md`](foundations/pipeline/SETUP.md) ·
> 📊 **KPIs:** [`foundations/KPIs.md`](foundations/KPIs.md) / [`foundations/KPIs_README.md`](foundations/KPIs_README.md)

---

## ✨ Qué entrega el framework

- **KPIs (4 perspectivas BSC):** madurez, capital humano, financiero + economía de APIs
  (`IEET`, `IOLI`, `ITR`, `IITA`, `PEUC`, `ICCA`, `IDLS`, `IBMT`) y **EVM** (CPI/SPI/EAC).
- **Conceptos de frontera:** **VRT/kTR** (unidad de recuperación de costos tokenizable — "el m² de Gitman")
  y **PSR** (Project Score 0–5 ⭐).
- **Diagnóstico operativo:** **VRT en 5 bloques**, **HCI** (hora crítica de interrupción),
  **desperdicios Lean Six Sigma** y **RCA de alucinación por taxonomía de prompt** (cuello de botella por proyecto + intersección).
- **Financiero:** **VAN, TIR, IR (índice de rentabilidad), Payback** simple/descontado, **dolarización** y comparación con **SELIC** y la **tasa de interés de EE. UU.**
- **Visual:** **mapa 5D** del portafolio, **dashboard Evidence** (BI as Code) y **pitch decks** en LaTeX de los proyectos elegibles.
- **Pipeline:** **Langfuse → SQLite → Evidence**, con sincronización **asíncrona concurrente** y clasificación acelerada en **Rust (PyO3)**.

## 🚀 Inicio rápido (demo, sin Langfuse)
```bash
cd foundations/pipeline
pip install -r requirements.txt
cd ../evidence && npm install && cd ../pipeline
./run_all.sh --mock          # datos anónimos (Project A..J) -> KPIs -> VAN -> 5D -> pitch decks -> dashboard
cd ../evidence && npm run dev # http://localhost:3000
```
Para datos reales: completa `foundations/pipeline/.env` con **tus propias** claves de Langfuse
(ver [`SETUP.md`](foundations/pipeline/SETUP.md)) y ejecuta `./run_all.sh`.

## 🗂️ Estructura
```
foundations/
├── README.md            ← documentación principal
├── KPIs.md · KPIs_README.md · BSC_Dashboard.md · solucoes_relatorios.md
├── pipeline/            ← ETL, consultas, seeds, Rust, generadores (5D, pitch deck), SETUP.md
├── evidence/            ← dashboard Evidence (BI as Code)
└── pitchdeck/           ← plantilla estándar + pitch decks generados
```

## 🏷️ Topics
`project-management` · `kanban` · `task-management` · `dashboard` · `executive-dashboard` ·
`business-intelligence` · `analytics` · `data-visualization` · `kpi` · `metrics` ·
`balanced-scorecard` · `llm` · `ai` · `llm-observability` · `llmops` · `langfuse` · `roi` ·
`agile` · `scrum` · `python`

---

**Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard** · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
