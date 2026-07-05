# 🧭 Framework VPL — AI-projektledning (PM) med BSC-panel & dashboard

🌐 [Português](README.md) · [English](README.en.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [中文](README.zh.md) · [한국어](README.ko.md) · [हिन्दी](README.hi.md) · [עברית](README.he.md) · **Svenska** · [Русский](README.ru.md) · [Suomi](README.fi.md)

![Method](https://img.shields.io/badge/method-Balanced%20Scorecard-1F3A5F)
![AI](https://img.shields.io/badge/AI-LLM%20observability-45a1bf)
![Finance](https://img.shields.io/badge/finance-NPV%20·%20IRR%20·%20PI-46a485)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Dashboard](https://img.shields.io/badge/dashboard-Evidence-236aa4)

> Ett ramverk för att **mäta vilket AI-projekt som helst från början till slut** — från token-förbrukning till
> finansiell avkastning — under de 4 perspektiven i **Balanced Scorecard** (Kaplan & Norton).
>
> *"Det som inte mäts kan varken styras eller förbättras."*

> *När du ber och studerar, låt inte [mina ord] lämna dig. Med varje ord och uttryck som lämnar dina läppar, ha i åtanke att åstadkomma en Förening.* — Aryeh Kaplan

> *Den rena metafysiken, som till sitt väsen befinner sig över och bortom alla former och alla tillfälligheter, är varken östlig eller västlig: den är universell.* — René Guénon

> *Att känna sig själv är att känna sin egen härstamning och sin egen kraft.* — Harvey Spencer Lewis

> *Scientia es Lux Lucis* ∞ Sapere Aude S∴A∴☬ ☿

> 📖 **Huvuddokumentation:** **[`foundations/README.md`](foundations/README.md)** ·
> ⚙️ **Installation (ta med egna nycklar):** [`foundations/pipeline/SETUP.md`](foundations/pipeline/SETUP.md)

## ✨ Vad ramverket levererar
- **KPI:er (4 BSC-perspektiv):** mognad, humankapital, finansiellt + API-ekonomi (`IEET`, `IOLI`, `ITR`, `IITA`, `PEUC`, `ICCA`, `IDLS`, `IBMT`) och **EVM**.
- **Frontlinjekoncept:** **VRT/kTR** och **PSR** (projektpoäng 0–5 ⭐).
- **Finansiellt:** **NPV, IRR, TIRM, VUL, PI, Payback**, dollarisering och jämförelse med **SELIC** och USA:s ränta.
- **Visuellt:** portföljens **5D-karta**, **Evidence-dashboard** (BI as Code) och LaTeX-**pitch decks**.
- **Pipeline:** **Langfuse → SQLite → Evidence**, asynkron samtidig synk och klassificering accelererad i **Rust (PyO3)**.

## 🚀 Snabbstart (demo, utan Langfuse)
```bash
cd foundations/pipeline
pip install -r requirements.txt
cd ../evidence && npm install && cd ../pipeline
./run_all.sh --mock          # anonyma data (Project A..J) -> KPI -> NPV -> 5D -> pitch decks -> dashboard
cd ../evidence && npm run dev # http://localhost:3000
```

## 🏷️ Topics
`project-management` · `dashboard` · `business-intelligence` · `kpi` · `balanced-scorecard` · `llm` · `ai` · `llm-observability` · `langfuse` · `roi` · `python`

---

**Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard** · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
