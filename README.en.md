# 🧭 Framework VPL — AI Project Management (PM) with a BSC Panel & Dashboard

🌐 [Português](README.md) · **English** · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [中文](README.zh.md) · [한국어](README.ko.md) · [हिन्दी](README.hi.md) · [עברית](README.he.md)

![Method](https://img.shields.io/badge/method-Balanced%20Scorecard-1F3A5F)
![AI](https://img.shields.io/badge/AI-LLM%20observability-45a1bf)
![Finance](https://img.shields.io/badge/finance-NPV%20·%20IRR%20·%20PI-46a485)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-PyO3-orange?logo=rust&logoColor=white)
![Dashboard](https://img.shields.io/badge/dashboard-Evidence-236aa4)
![PDF](https://img.shields.io/badge/pitch%20deck-LaTeX-008080)
![status](https://img.shields.io/badge/status-v1-success)

> A framework to **measure any AI project end to end** — from token consumption to
> financial return — under the 4 perspectives of the **Balanced Scorecard** (Kaplan & Norton).
>
> *"What is not measured cannot be managed or improved."*

> 📖 **Main documentation:** **[`foundations/README.md`](foundations/README.md)** ·
> ⚙️ **Setup (bring your own keys):** [`foundations/pipeline/SETUP.md`](foundations/pipeline/SETUP.md) ·
> 📊 **KPIs:** [`foundations/KPIs.md`](foundations/KPIs.md) / [`foundations/KPIs_README.md`](foundations/KPIs_README.md)

---

## ✨ What the framework delivers

- **KPIs (4 BSC perspectives):** maturity, human capital, financial + API economy
  (`IEET`, `IOLI`, `ITR`, `IITA`, `PEUC`, `ICCA`, `IDLS`, `IBMT`) and **EVM** (CPI/SPI/EAC).
- **Frontier concepts:** **VRT/kTR** (tokenizable cost-recovery unit — "Gitman's m²")
  and **PSR** (Project Score 0–5 ⭐).
- **Operational diagnostics:** **VRT in 5 blocks**, **HCI** (critical interruption hour),
  **Lean Six Sigma wastes** and **hallucination RCA by prompt taxonomy** (bottleneck per project + intersection).
- **Financial:** **NPV, IRR, PI, Payback** (simple/discounted), **dollarization** and comparison with **SELIC** and the **US interest rate**.
- **Visual:** portfolio **5D map**, **Evidence dashboard** (BI as Code) and LaTeX **pitch decks** for eligible projects.
- **Pipeline:** **Langfuse → SQLite → Evidence**, with **asynchronous concurrent** sync and classification accelerated in **Rust (PyO3)**.

## 🚀 Quick start (demo, no Langfuse)
```bash
cd foundations/pipeline
pip install -r requirements.txt
cd ../evidence && npm install && cd ../pipeline
./run_all.sh --mock          # anonymous data (Project A..J) -> KPIs -> NPV -> 5D -> pitch decks -> dashboard
cd ../evidence && npm run dev # http://localhost:3000
```
For real data: fill `foundations/pipeline/.env` with **your own** Langfuse keys
(see [`SETUP.md`](foundations/pipeline/SETUP.md)) and run `./run_all.sh`.

## 🗂️ Structure
```
foundations/
├── README.md            ← main documentation
├── KPIs.md · KPIs_README.md · BSC_Dashboard.md · solucoes_relatorios.md
├── pipeline/            ← ETL, queries, seeds, Rust, generators (5D, pitch deck), SETUP.md
├── evidence/            ← Evidence dashboard (BI as Code)
└── pitchdeck/           ← standard template + generated pitch decks
```

## 🏷️ Topics
`project-management` · `kanban` · `task-management` · `dashboard` · `executive-dashboard` ·
`business-intelligence` · `analytics` · `data-visualization` · `kpi` · `metrics` ·
`balanced-scorecard` · `llm` · `ai` · `llm-observability` · `llmops` · `langfuse` · `roi` ·
`agile` · `scrum` · `python`

## 🔒 Privacy
The demo is **100% anonymous** (Project A…J). Personal data, conversations and real databases stay **out of the
package** (`foundations/_private/`, git-ignored). Before publishing, run the sanitization in
[`github_load.md`](foundations/github_load.md).

---

**Framework "Gestão de Projetos (PM) IA com Painel BSC e DashBoard"** · ©️ Bruno Teixeira Penedo — 2026. All rights reserved. E-mail: bpenedo@gmail.com
