# 🧭 Framework VPL — KI-Projektmanagement (PM) mit BSC-Panel & Dashboard

🌐 [Português](README.md) · [English](README.en.md) · [Español](README.es.md) · [Français](README.fr.md) · **Deutsch** · [中文](README.zh.md) · [한국어](README.ko.md) · [हिन्दी](README.hi.md) · [עברית](README.he.md) · [Svenska](README.sv.md) · [Русский](README.ru.md) · [Suomi](README.fi.md)

![Method](https://img.shields.io/badge/method-Balanced%20Scorecard-1F3A5F)
![AI](https://img.shields.io/badge/AI-LLM%20observability-45a1bf)
![Finance](https://img.shields.io/badge/finance-Kapitalwert%20·%20IRR%20·%20PI-46a485)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-PyO3-orange?logo=rust&logoColor=white)
![Dashboard](https://img.shields.io/badge/dashboard-Evidence-236aa4)
![PDF](https://img.shields.io/badge/pitch%20deck-LaTeX-008080)
![status](https://img.shields.io/badge/status-v1-success)

> Ein Framework, um **jedes KI-Projekt durchgängig zu messen** — vom Token-Verbrauch bis zur
> finanziellen Rendite — unter den 4 Perspektiven der **Balanced Scorecard** (Kaplan & Norton).
>
> *„Was nicht gemessen wird, kann weder gesteuert noch verbessert werden."*

> *Wenn du betest und lernst, lass [meine Worte] dich nicht verlassen. Mit jedem Wort und Ausdruck, der deine Lippen verlässt, halte im Sinn, eine Vereinigung zu bewirken.* — Aryeh Kaplan

> *Die reine Metaphysik, die sich ihrem Wesen nach über und jenseits aller Formen und aller Kontingenzen befindet, ist weder östlich noch westlich: sie ist universal.* — René Guénon

> *Sich selbst zu kennen bedeutet, die eigene Abstammung und die eigene Kraft zu kennen.* — Harvey Spencer Lewis

> *Scientia es Lux Lucis* ∞ Sapere Aude S∴A∴☬ ☿

> 📖 **Hauptdokumentation:** **[`foundations/README.md`](foundations/README.md)** ·
> ⚙️ **Einrichtung (eigene Schlüssel mitbringen):** [`foundations/pipeline/SETUP.md`](foundations/pipeline/SETUP.md) ·
> 📊 **KPIs:** [`foundations/KPIs.md`](foundations/KPIs.md) / [`foundations/KPIs_README.md`](foundations/KPIs_README.md)

---

## ✨ Was das Framework liefert

- **KPIs (4 BSC-Perspektiven):** Reife, Humankapital, Finanzen + API-Ökonomie
  (`IEET`, `IOLI`, `ITR`, `IITA`, `PEUC`, `ICCA`, `IDLS`, `IBMT`) und **EVM** (CPI/SPI/EAC).
- **Grenzkonzepte:** **VRT/kTR** (tokenisierbare Kostendeckungseinheit — „Gitmans m²")
  und **PSR** (Project Score 0–5 ⭐).
- **Betriebliche Diagnose:** **VRT in 5 Blöcken**, **HCI** (kritische Unterbrechungsstunde),
  **Lean-Six-Sigma-Verschwendungen** und **Halluzinations-RCA nach Prompt-Taxonomie** (Engpass pro Projekt + Schnittmenge).
- **Finanziell:** **Kapitalwert (NPV), IRR, PI, Amortisation** (einfach/diskontiert), **Dollarisierung** und Vergleich mit dem **SELIC** und dem **US-Zinssatz**.
- **Visuell:** **5D-Karte** des Portfolios, **Evidence-Dashboard** (BI as Code) und LaTeX-**Pitch-Decks** für förderfähige Projekte.
- **Pipeline:** **Langfuse → SQLite → Evidence**, mit **asynchroner nebenläufiger** Synchronisierung und in **Rust (PyO3)** beschleunigter Klassifizierung.

## 🚀 Schnellstart (Demo, ohne Langfuse)
```bash
cd foundations/pipeline
pip install -r requirements.txt
cd ../evidence && npm install && cd ../pipeline
./run_all.sh --mock          # anonyme Daten (Project A..J) -> KPIs -> NPV -> 5D -> Pitch-Decks -> Dashboard
cd ../evidence && npm run dev # http://localhost:3000
```
Für echte Daten: `foundations/pipeline/.env` mit **Ihren eigenen** Langfuse-Schlüsseln ausfüllen
(siehe [`SETUP.md`](foundations/pipeline/SETUP.md)) und `./run_all.sh` ausführen.

## 🗂️ Struktur
```
foundations/
├── README.md            ← Hauptdokumentation
├── KPIs.md · KPIs_README.md · BSC_Dashboard.md · solucoes_relatorios.md
├── pipeline/            ← ETL, Queries, Seeds, Rust, Generatoren (5D, Pitch-Deck), SETUP.md
├── evidence/            ← Evidence-Dashboard (BI as Code)
└── pitchdeck/           ← Standardvorlage + generierte Pitch-Decks
```

## 🏷️ Topics
`project-management` · `kanban` · `task-management` · `dashboard` · `executive-dashboard` ·
`business-intelligence` · `analytics` · `data-visualization` · `kpi` · `metrics` ·
`balanced-scorecard` · `llm` · `ai` · `llm-observability` · `llmops` · `langfuse` · `roi` ·
`agile` · `scrum` · `python`

---

**Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard** · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
