# 🧭 Framework VPL — BSC पैनल और डैशबोर्ड के साथ AI परियोजना प्रबंधन (PM)

🌐 [Português](README.md) · [English](README.en.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [中文](README.zh.md) · [한국어](README.ko.md) · **हिन्दी** · [עברית](README.he.md) · [Svenska](README.sv.md) · [Русский](README.ru.md) · [Suomi](README.fi.md)

![Method](https://img.shields.io/badge/method-Balanced%20Scorecard-1F3A5F)
![AI](https://img.shields.io/badge/AI-LLM%20observability-45a1bf)
![Finance](https://img.shields.io/badge/finance-NPV%20·%20IRR%20·%20PI-46a485)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-PyO3-orange?logo=rust&logoColor=white)
![Dashboard](https://img.shields.io/badge/dashboard-Evidence-236aa4)
![PDF](https://img.shields.io/badge/pitch%20deck-LaTeX-008080)
![status](https://img.shields.io/badge/status-v1-success)

> **किसी भी AI परियोजना को आद्योपांत मापने** के लिए एक फ्रेमवर्क — टोकन खपत से लेकर
> वित्तीय प्रतिफल तक — **बैलेंस्ड स्कोरकार्ड** (Kaplan & Norton) के 4 दृष्टिकोणों के अंतर्गत।
>
> *"जो मापा नहीं जाता, उसे न तो प्रबंधित किया जा सकता है और न ही सुधारा जा सकता है।"*

> *जब तुम प्रार्थना और अध्ययन करो, तो [मेरे वचनों] को अपने से न जाने दो। तुम्हारे होंठों से निकलने वाले हर शब्द और अभिव्यक्ति के साथ, एक एकत्व लाने का ध्यान रखो।* — Aryeh Kaplan

> *शुद्ध तत्त्वमीमांसा, अपने सार में सभी रूपों और सभी आकस्मिकताओं से ऊपर और परे स्थित होकर, न तो प्राच्य है न पाश्चात्य: वह सार्वभौमिक है।* — René Guénon

> *स्वयं को जानना अपनी वंश-परंपरा और अपनी शक्ति को जानना है।* — Harvey Spencer Lewis

> *Scientia es Lux Lucis* ∞ Sapere Aude S∴A∴☬ ☿

> 📖 **मुख्य दस्तावेज़ीकरण:** **[`foundations/README.md`](foundations/README.md)** ·
> ⚙️ **सेटअप (अपनी चाबियाँ लाएँ):** [`foundations/pipeline/SETUP.md`](foundations/pipeline/SETUP.md) ·
> 📊 **KPI:** [`foundations/KPIs.md`](foundations/KPIs.md) / [`foundations/KPIs_README.md`](foundations/KPIs_README.md)

---

## ✨ फ्रेमवर्क क्या प्रदान करता है

- **KPI (4 BSC दृष्टिकोण):** परिपक्वता, मानव पूंजी, वित्तीय + API अर्थव्यवस्था
  (`IEET`, `IOLI`, `ITR`, `IITA`, `PEUC`, `ICCA`, `IDLS`, `IBMT`) और **EVM** (CPI/SPI/EAC)।
- **अग्रणी अवधारणाएँ:** **VRT/kTR** (टोकनयोग्य लागत-वसूली इकाई — "Gitman का m²")
  और **PSR** (परियोजना स्कोर 0–5 ⭐)।
- **परिचालन निदान:** **5 ब्लॉकों में VRT**, **HCI** (महत्वपूर्ण व्यवधान समय),
  **लीन सिक्स सिग्मा अपव्यय** और **प्रॉम्प्ट वर्गीकरण द्वारा मतिभ्रम RCA** (प्रति परियोजना अड़चन + प्रतिच्छेदन)।
- **वित्तीय:** **NPV, IRR, PI, पेबैक** (सरल/छूटयुक्त), **डॉलरीकरण** और **SELIC** एवं **अमेरिकी ब्याज दर** से तुलना।
- **दृश्य:** पोर्टफोलियो का **5D मानचित्र**, **Evidence डैशबोर्ड** (BI as Code) और पात्र परियोजनाओं के LaTeX **पिच डेक**।
- **पाइपलाइन:** **Langfuse → SQLite → Evidence**, **अतुल्यकालिक समवर्ती** सिंक और **Rust (PyO3)** में त्वरित वर्गीकरण के साथ।

## 🚀 त्वरित प्रारंभ (डेमो, Langfuse के बिना)
```bash
cd foundations/pipeline
pip install -r requirements.txt
cd ../evidence && npm install && cd ../pipeline
./run_all.sh --mock          # अनाम डेटा (Project A..J) -> KPI -> NPV -> 5D -> pitch decks -> डैशबोर्ड
cd ../evidence && npm run dev # http://localhost:3000
```
वास्तविक डेटा के लिए: `foundations/pipeline/.env` में **अपनी** Langfuse चाबियाँ भरें
([`SETUP.md`](foundations/pipeline/SETUP.md) देखें) और `./run_all.sh` चलाएँ।

## 🗂️ संरचना
```
foundations/
├── README.md            ← मुख्य दस्तावेज़ीकरण
├── KPIs.md · KPIs_README.md · BSC_Dashboard.md · solucoes_relatorios.md
├── pipeline/            ← ETL, क्वेरी, seeds, Rust, जनरेटर (5D, pitch deck), SETUP.md
├── evidence/            ← Evidence डैशबोर्ड (BI as Code)
└── pitchdeck/           ← मानक टेम्पलेट + जनरेट किए गए pitch decks
```

## 🏷️ Topics
`project-management` · `kanban` · `task-management` · `dashboard` · `executive-dashboard` ·
`business-intelligence` · `analytics` · `data-visualization` · `kpi` · `metrics` ·
`balanced-scorecard` · `llm` · `ai` · `llm-observability` · `llmops` · `langfuse` · `roi` ·
`agile` · `scrum` · `python`

---

**Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard** · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
