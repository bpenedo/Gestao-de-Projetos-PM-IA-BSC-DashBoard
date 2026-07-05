# 🧭 Framework VPL — 基于 BSC 面板与仪表盘的 AI 项目管理（PM）

🌐 [Português](README.md) · [English](README.en.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · **中文** · [한국어](README.ko.md) · [हिन्दी](README.hi.md) · [עברית](README.he.md) · [Svenska](README.sv.md) · [Русский](README.ru.md) · [Suomi](README.fi.md)

![Method](https://img.shields.io/badge/method-Balanced%20Scorecard-1F3A5F)
![AI](https://img.shields.io/badge/AI-LLM%20observability-45a1bf)
![Finance](https://img.shields.io/badge/finance-NPV%20·%20IRR%20·%20PI-46a485)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-PyO3-orange?logo=rust&logoColor=white)
![Dashboard](https://img.shields.io/badge/dashboard-Evidence-236aa4)
![PDF](https://img.shields.io/badge/pitch%20deck-LaTeX-008080)
![status](https://img.shields.io/badge/status-v1-success)

> 一个**端到端衡量任何 AI 项目**的框架——从 token 消耗到财务回报——
> 依据**平衡计分卡**（Balanced Scorecard，Kaplan & Norton）的 4 个维度。
>
> *"无法衡量的东西就无法管理，也无法改进。"*

> *当你祈祷与研习时，勿让[我的话语]离你而去。你唇间吐出的每一个词与语，都当心怀成就一种合一。* — Aryeh Kaplan

> *纯粹的形而上学，就其本质而言超越并凌驾于一切形式与一切偶然之上，既非东方亦非西方：它是普世的。* — René Guénon

> *认识你自己，就是认识自己的血脉与自己的力量。* — Harvey Spencer Lewis

> *Scientia es Lux Lucis* ∞ Sapere Aude S∴A∴☬ ☿

> 📖 **主文档：** **[`foundations/README.md`](foundations/README.md)** ·
> ⚙️ **配置（使用你自己的密钥）：** [`foundations/pipeline/SETUP.md`](foundations/pipeline/SETUP.md) ·
> 📊 **KPI：** [`foundations/KPIs.md`](foundations/KPIs.md) / [`foundations/KPIs_README.md`](foundations/KPIs_README.md)

---

## ✨ 框架提供什么

- **KPI（BSC 的 4 个维度）：** 成熟度、人力资本、财务 + API 经济性
  （`IEET`、`IOLI`、`ITR`、`IITA`、`PEUC`、`ICCA`、`IDLS`、`IBMT`）以及 **EVM**（CPI/SPI/EAC）。
- **前沿概念：** **VRT/kTR**（可代币化的成本回收单位——"Gitman 的每平方米"）
  和 **PSR**（项目评分 0–5 ⭐）。
- **运营诊断：** **VRT 五分块**、**HCI**（关键中断时段）、
  **精益六西格玛浪费**，以及**按提示词分类的幻觉根因分析（RCA）**（各项目瓶颈 + 交集）。
- **财务：** **NPV、IRR、PI、回收期**（简单/贴现）、**美元化**，并与 **SELIC** 和**美国利率**对比。
- **可视化：** 组合的 **5D 地图**、**Evidence 仪表盘**（BI as Code），以及合格项目的 LaTeX **路演材料（pitch deck）**。
- **流水线：** **Langfuse → SQLite → Evidence**，采用**异步并发**同步，并以 **Rust（PyO3）**加速分类。

## 🚀 快速开始（演示，无需 Langfuse）
```bash
cd foundations/pipeline
pip install -r requirements.txt
cd ../evidence && npm install && cd ../pipeline
./run_all.sh --mock          # 匿名数据 (Project A..J) -> KPI -> NPV -> 5D -> pitch decks -> 仪表盘
cd ../evidence && npm run dev # http://localhost:3000
```
若使用真实数据：在 `foundations/pipeline/.env` 中填入**你自己的** Langfuse 密钥
（见 [`SETUP.md`](foundations/pipeline/SETUP.md)），然后运行 `./run_all.sh`。

## 🗂️ 结构
```
foundations/
├── README.md            ← 主文档
├── KPIs.md · KPIs_README.md · BSC_Dashboard.md · solucoes_relatorios.md
├── pipeline/            ← ETL、查询、seed、Rust、生成器（5D、pitch deck）、SETUP.md
├── evidence/            ← Evidence 仪表盘（BI as Code）
└── pitchdeck/           ← 标准模板 + 生成的 pitch deck
```

## 🏷️ Topics
`project-management` · `kanban` · `task-management` · `dashboard` · `executive-dashboard` ·
`business-intelligence` · `analytics` · `data-visualization` · `kpi` · `metrics` ·
`balanced-scorecard` · `llm` · `ai` · `llm-observability` · `llmops` · `langfuse` · `roi` ·
`agile` · `scrum` · `python`

---

**Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard** · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
