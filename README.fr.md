# 🧭 Framework VPL — Gestion de Projets (PM) IA avec Panneau BSC et Dashboard

🌐 [Português](README.md) · [English](README.en.md) · [Español](README.es.md) · **Français** · [Deutsch](README.de.md) · [中文](README.zh.md) · [한국어](README.ko.md) · [हिन्दी](README.hi.md) · [עברית](README.he.md) · [Svenska](README.sv.md) · [Русский](README.ru.md) · [Suomi](README.fi.md)

![Method](https://img.shields.io/badge/method-Balanced%20Scorecard-1F3A5F)
![AI](https://img.shields.io/badge/AI-LLM%20observability-45a1bf)
![Finance](https://img.shields.io/badge/finance-VAN%20·%20TRI%20·%20IP-46a485)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-PyO3-orange?logo=rust&logoColor=white)
![Dashboard](https://img.shields.io/badge/dashboard-Evidence-236aa4)
![PDF](https://img.shields.io/badge/pitch%20deck-LaTeX-008080)
![status](https://img.shields.io/badge/status-v1-success)

> Un framework pour **mesurer tout projet d'IA de bout en bout** — de la consommation de tokens au
> retour financier — selon les 4 perspectives du **Balanced Scorecard** (Kaplan & Norton).
>
> *« Ce qui n'est pas mesuré ne peut être ni géré ni amélioré. »*

> *Lorsque tu pries et étudies, ne laisse pas [mes paroles] te quitter. À chaque mot et expression qui sort de tes lèvres, aie à l'esprit d'opérer une Unification.* — Aryeh Kaplan

> *La métaphysique pure, se situant par essence au-dessus et au-delà de toutes les formes et de toutes les contingences, n'est ni orientale ni occidentale : elle est universelle.* — René Guénon

> *Se connaître soi-même, c'est connaître sa propre lignée et son propre pouvoir.* — Harvey Spencer Lewis

> *Scientia es Lux Lucis* ∞ Sapere Aude S∴A∴☬ ☿

> 📖 **Documentation principale :** **[`foundations/README.md`](foundations/README.md)** ·
> ⚙️ **Configuration (apportez vos clés) :** [`foundations/pipeline/SETUP.md`](foundations/pipeline/SETUP.md) ·
> 📊 **KPI :** [`foundations/KPIs.md`](foundations/KPIs.md) / [`foundations/KPIs_README.md`](foundations/KPIs_README.md)

---

## ✨ Ce que le framework fournit

- **KPI (4 perspectives BSC) :** maturité, capital humain, financier + économie d'API
  (`IEET`, `IOLI`, `ITR`, `IITA`, `PEUC`, `ICCA`, `IDLS`, `IBMT`) et **EVM** (CPI/SPI/EAC).
- **Concepts de pointe :** **VRT/kTR** (unité de récupération de coût tokenisable — « le m² de Gitman »)
  et **PSR** (Project Score 0–5 ⭐).
- **Diagnostic opérationnel :** **VRT en 5 blocs**, **HCI** (heure critique d'interruption),
  **gaspillages Lean Six Sigma** et **RCA d'hallucination par taxonomie de prompt** (goulot par projet + intersection).
- **Financier :** **VAN, TRI, IP (indice de profitabilité), Payback** simple/actualisé, **dollarisation** et comparaison avec le **SELIC** et le **taux d'intérêt américain**.
- **Visuel :** **carte 5D** du portefeuille, **dashboard Evidence** (BI as Code) et **pitch decks** en LaTeX des projets éligibles.
- **Pipeline :** **Langfuse → SQLite → Evidence**, avec synchronisation **asynchrone concurrente** et classification accélérée en **Rust (PyO3)**.

## 🚀 Démarrage rapide (démo, sans Langfuse)
```bash
cd foundations/pipeline
pip install -r requirements.txt
cd ../evidence && npm install && cd ../pipeline
./run_all.sh --mock          # données anonymes (Project A..J) -> KPI -> VAN -> 5D -> pitch decks -> dashboard
cd ../evidence && npm run dev # http://localhost:3000
```
Pour des données réelles : renseignez `foundations/pipeline/.env` avec **vos propres** clés Langfuse
(voir [`SETUP.md`](foundations/pipeline/SETUP.md)) et lancez `./run_all.sh`.

## 🗂️ Structure
```
foundations/
├── README.md            ← documentation principale
├── KPIs.md · KPIs_README.md · BSC_Dashboard.md · solucoes_relatorios.md
├── pipeline/            ← ETL, requêtes, seeds, Rust, générateurs (5D, pitch deck), SETUP.md
├── evidence/            ← dashboard Evidence (BI as Code)
└── pitchdeck/           ← modèle standard + pitch decks générés
```

## 🏷️ Topics
`project-management` · `kanban` · `task-management` · `dashboard` · `executive-dashboard` ·
`business-intelligence` · `analytics` · `data-visualization` · `kpi` · `metrics` ·
`balanced-scorecard` · `llm` · `ai` · `llm-observability` · `llmops` · `langfuse` · `roi` ·
`agile` · `scrum` · `python`

---

**Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard** · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
