# 🧭 Framework VPL — Gestão de Projetos (PM) IA com Painel BSC e DashBoard

🌐 **Português** · [English](README.en.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [中文](README.zh.md) · [한국어](README.ko.md) · [हिन्दी](README.hi.md) · [עברית](README.he.md) · [Svenska](README.sv.md) · [Русский](README.ru.md) · [Suomi](README.fi.md)

![Method](https://img.shields.io/badge/method-Balanced%20Scorecard-1F3A5F)
![AI](https://img.shields.io/badge/AI-LLM%20observability-45a1bf)
![Finance](https://img.shields.io/badge/finance-VPL%20·%20TIR%20·%20ILL-46a485)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-PyO3-orange?logo=rust&logoColor=white)
![Dashboard](https://img.shields.io/badge/dashboard-Evidence-236aa4)
![PDF](https://img.shields.io/badge/pitch%20deck-LaTeX-008080)
![status](https://img.shields.io/badge/status-v1-success)

> Framework para **mensurar qualquer projeto de IA ponta a ponta** — do consumo de tokens ao
> retorno financeiro — sob as 4 perspectivas do **Balanced Scorecard** (Kaplan & Norton).
>
> *"O que não é medido não pode ser gerenciado nem melhorado."*

> *Quando você ora e estuda, não deixe [minhas palavras] te abandonarem. Com cada palavra e expressão que sai de seus lábios, tenha em mente trazer uma Unificação.* — Aryeh Kaplan

> *A metafísica pura, situando-se, por essência, acima e além de todas as formas e de todas as contingências, não é nem oriental nem ocidental: é universal.* — René Guénon

> *Conhecer a si mesmo é conhecer a própria linhagem e o próprio poder.* — Harvey Spencer Lewis

> *Scientia es Lux Lucis* ∞ Sapere Aude S∴A∴☬ ☿

> 📖 **Documentação principal:** **[`foundations/README.md`](foundations/README.md)** ·
> ⚙️ **Setup (traga suas chaves):** [`foundations/pipeline/SETUP.md`](foundations/pipeline/SETUP.md) ·
> 📊 **KPIs:** [`foundations/KPIs.md`](foundations/KPIs.md) / [`foundations/KPIs_README.md`](foundations/KPIs_README.md)

---

## ✨ O que o framework entrega

- **KPIs (4 perspectivas BSC):** maturidade, capital humano, financeiro + economia de APIs
  (`IEET`, `IOLI`, `ITR`, `IITA`, `PEUC`, `ICCA`, `IDLS`, `IBMT`) e **EVM** (CPI/SPI/EAC).
- **Conceitos de fronteira:** **VRT/kTR** (unidade de recuperação tokenizável — "o m² de Gitman")
  e **PSR** (Project Score 0–5 ⭐).
- **Diagnóstico operacional:** **VRT em 5 blocos**, **HCI** (horário crítico de interrupção),
  **Wastes Lean Six Sigma** e **RCA de alucinação por taxonomia de prompt** (gargalo por projeto + interseção).
- **Financeiro:** **VPL, TIR, ILL, Payback** simples/descontado, **dolarização** e comparação com **SELIC** e **juros dos EUA**.
- **Visual:** **mapa 5D** do portfólio, **dashboard Evidence** (BI as Code) e **pitch decks** em LaTeX dos projetos elegíveis.
- **Pipeline:** **Langfuse → SQLite → Evidence**, com sync **assíncrono concorrente** e classificação acelerada em **Rust (PyO3)**.

## 🚀 Início rápido (demo, sem Langfuse)
```bash
cd foundations/pipeline
pip install -r requirements.txt
cd ../evidence && npm install && cd ../pipeline
./run_all.sh --mock          # dados anônimos (Project A..J) -> KPIs -> VPL -> 5D -> pitch decks -> dashboard
cd ../evidence && npm run dev # http://localhost:3000
```
Para dados reais: preencha `foundations/pipeline/.env` com **as suas chaves** do Langfuse
(ver [`SETUP.md`](foundations/pipeline/SETUP.md)) e rode `./run_all.sh`.

## 🗂️ Estrutura
```
foundations/
├── README.md            ← documentação principal
├── KPIs.md · KPIs_README.md · BSC_Dashboard.md · solucoes_relatorios.md
├── pipeline/            ← ETL, queries, seeds, Rust, geradores (5D, pitch deck), SETUP.md
├── evidence/            ← dashboard Evidence (BI as Code)
└── pitchdeck/           ← template padrão + pitch decks gerados
```

## 🏷️ Topics
`project-management` · `kanban` · `task-management` · `dashboard` · `executive-dashboard` ·
`business-intelligence` · `analytics` · `data-visualization` · `kpi` · `metrics` ·
`balanced-scorecard` · `llm` · `ai` · `llm-observability` · `llmops` · `langfuse` · `roi` ·
`agile` · `scrum` · `python`

---

**Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard** · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
