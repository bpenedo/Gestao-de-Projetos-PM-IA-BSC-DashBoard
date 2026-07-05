# 🧭 Framework VPL — ניהול פרויקטים (PM) של AI עם לוח BSC ודשבורד

🌐 [Português](README.md) · [English](README.en.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [中文](README.zh.md) · [한국어](README.ko.md) · [हिन्दी](README.hi.md) · **עברית** · [Svenska](README.sv.md) · [Русский](README.ru.md) · [Suomi](README.fi.md)

![Method](https://img.shields.io/badge/method-Balanced%20Scorecard-1F3A5F)
![AI](https://img.shields.io/badge/AI-LLM%20observability-45a1bf)
![Finance](https://img.shields.io/badge/finance-NPV%20·%20IRR%20·%20PI-46a485)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-PyO3-orange?logo=rust&logoColor=white)
![Dashboard](https://img.shields.io/badge/dashboard-Evidence-236aa4)
![PDF](https://img.shields.io/badge/pitch%20deck-LaTeX-008080)
![status](https://img.shields.io/badge/status-v1-success)

> מסגרת **למדידת כל פרויקט AI מקצה לקצה** — מצריכת הטוקנים ועד לתשואה הפיננסית —
> תחת 4 הפרספקטיבות של **Balanced Scorecard** (Kaplan & Norton).
>
> *"מה שלא נמדד לא ניתן לניהול ולא ניתן לשיפור."*

> *כאשר אתה מתפלל ולומד, אל תיתן [לדבריי] לעזוב אותך. עם כל מילה וביטוי היוצאים משפתיך, שים אל לבך להביא ייחוד.* — Aryeh Kaplan

> *המטאפיזיקה הטהורה, השוכנת מעצם מהותה מעל ומעבר לכל הצורות וכל המקרים, אינה מזרחית ואינה מערבית: היא אוניברסלית.* — René Guénon

> *להכיר את עצמך פירושו להכיר את שושלתך ואת כוחך.* — Harvey Spencer Lewis

> *Scientia es Lux Lucis* ∞ Sapere Aude S∴A∴☬ ☿

> 📖 **תיעוד ראשי:** **[`foundations/README.md`](foundations/README.md)** ·
> ⚙️ **התקנה (עם המפתחות שלכם):** [`foundations/pipeline/SETUP.md`](foundations/pipeline/SETUP.md) ·
> 📊 **KPI:** [`foundations/KPIs.md`](foundations/KPIs.md) / [`foundations/KPIs_README.md`](foundations/KPIs_README.md)

---

## ✨ מה המסגרת מספקת

- **KPI (4 פרספקטיבות BSC):** בשלות, הון אנושי, פיננסי + כלכלת API
  (`IEET`, `IOLI`, `ITR`, `IITA`, `PEUC`, `ICCA`, `IDLS`, `IBMT`) ו-**EVM** (CPI/SPI/EAC).
- **מושגי חזית:** **VRT/kTR** (יחידת השבת עלות ניתנת-לטוקניזציה — "המ״ר של Gitman")
  ו-**PSR** (ציון פרויקט 0–5 ⭐).
- **אבחון תפעולי:** **VRT ב-5 בלוקים**, **HCI** (שעת ההפרעה הקריטית),
  **בזבוזי Lean Six Sigma** ו-**RCA של הזיות לפי טקסונומיית פרומפט** (צוואר בקבוק לכל פרויקט + חיתוך).
- **פיננסי:** **NPV, IRR, PI, החזר השקעה** (פשוט/מהוון), **דולריזציה** והשוואה ל-**SELIC** ולריבית של **ארה״ב**.
- **חזותי:** **מפת 5D** של התיק, **דשבורד Evidence** (BI as Code) ו-**pitch decks** ב-LaTeX לפרויקטים כשירים.
- **צינור (pipeline):** **Langfuse → SQLite → Evidence**, עם סנכרון **אסינכרוני מקבילי** וסיווג מואץ ב-**Rust (PyO3)**.

## 🚀 התחלה מהירה (הדגמה, ללא Langfuse)
```bash
cd foundations/pipeline
pip install -r requirements.txt
cd ../evidence && npm install && cd ../pipeline
./run_all.sh --mock          # נתונים אנונימיים (Project A..J) -> KPI -> NPV -> 5D -> pitch decks -> דשבורד
cd ../evidence && npm run dev # http://localhost:3000
```
לנתונים אמיתיים: מלאו את `foundations/pipeline/.env` עם מפתחות **Langfuse שלכם**
(ראו [`SETUP.md`](foundations/pipeline/SETUP.md)) והריצו `./run_all.sh`.

## 🗂️ מבנה
```
foundations/
├── README.md            ← תיעוד ראשי
├── KPIs.md · KPIs_README.md · BSC_Dashboard.md · solucoes_relatorios.md
├── pipeline/            ← ETL, שאילתות, seeds, Rust, מחוללים (5D, pitch deck), SETUP.md
├── evidence/            ← דשבורד Evidence (BI as Code)
└── pitchdeck/           ← תבנית סטנדרטית + pitch decks שנוצרו
```

## 🏷️ Topics
`project-management` · `kanban` · `task-management` · `dashboard` · `executive-dashboard` ·
`business-intelligence` · `analytics` · `data-visualization` · `kpi` · `metrics` ·
`balanced-scorecard` · `llm` · `ai` · `llm-observability` · `llmops` · `langfuse` · `roi` ·
`agile` · `scrum` · `python`

---

**Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard** · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
