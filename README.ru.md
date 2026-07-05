# 🧭 Framework VPL — управление ИИ-проектами (PM) с панелью BSC и дашбордом

🌐 [Português](README.md) · [English](README.en.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [中文](README.zh.md) · [한국어](README.ko.md) · [हिन्दी](README.hi.md) · [עברית](README.he.md) · [Svenska](README.sv.md) · **Русский** · [Suomi](README.fi.md)

![Method](https://img.shields.io/badge/method-Balanced%20Scorecard-1F3A5F)
![AI](https://img.shields.io/badge/AI-LLM%20observability-45a1bf)
![Finance](https://img.shields.io/badge/finance-NPV%20·%20IRR%20·%20PI-46a485)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Dashboard](https://img.shields.io/badge/dashboard-Evidence-236aa4)

> Фреймворк для **сквозного измерения любого ИИ-проекта** — от расхода токенов до
> финансовой отдачи — по 4 перспективам **Balanced Scorecard** (Kaplan & Norton).
>
> *«Что не измеряется, тем нельзя управлять и то нельзя улучшить.»*

> *Когда ты молишься и учишься, не позволяй [моим словам] покинуть тебя. С каждым словом и выражением, исходящим из твоих уст, держи в уме совершить Единение.* — Aryeh Kaplan

> *Чистая метафизика, по своей сущности пребывающая над и за пределами всех форм и всех случайностей, не является ни восточной, ни западной: она универсальна.* — René Guénon

> *Познать себя — значит познать свой род и свою силу.* — Harvey Spencer Lewis

> *Scientia es Lux Lucis* ∞ Sapere Aude S∴A∴☬ ☿

> 📖 **Основная документация:** **[`foundations/README.md`](foundations/README.md)** ·
> ⚙️ **Настройка (свои ключи):** [`foundations/pipeline/SETUP.md`](foundations/pipeline/SETUP.md)

## ✨ Что даёт фреймворк
- **KPI (4 перспективы BSC):** зрелость, человеческий капитал, финансы + экономика API (`IEET`, `IOLI`, `ITR`, `IITA`, `PEUC`, `ICCA`, `IDLS`, `IBMT`) и **EVM**.
- **Передовые концепции:** **VRT/kTR** и **PSR** (оценка проекта 0–5 ⭐).
- **Финансы:** **NPV, IRR, TIRM, VUL, PI, окупаемость**, долларизация и сравнение с **SELIC** и ставкой США.
- **Визуализация:** **5D-карта** портфеля, **дашборд Evidence** (BI as Code) и LaTeX-**питч-деки**.
- **Конвейер:** **Langfuse → SQLite → Evidence**, асинхронная параллельная синхронизация и классификация, ускоренная в **Rust (PyO3)**.

## 🚀 Быстрый старт (демо, без Langfuse)
```bash
cd foundations/pipeline
pip install -r requirements.txt
cd ../evidence && npm install && cd ../pipeline
./run_all.sh --mock          # анонимные данные (Project A..J) -> KPI -> NPV -> 5D -> pitch decks -> дашборд
cd ../evidence && npm run dev # http://localhost:3000
```

## 🏷️ Topics
`project-management` · `dashboard` · `business-intelligence` · `kpi` · `balanced-scorecard` · `llm` · `ai` · `llm-observability` · `langfuse` · `roi` · `python`

---

**Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard** · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
