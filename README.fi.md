# 🧭 Framework VPL — tekoälyprojektien hallinta (PM) BSC-paneelilla ja dashboardilla

🌐 [Português](README.md) · [English](README.en.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [中文](README.zh.md) · [한국어](README.ko.md) · [हिन्दी](README.hi.md) · [עברית](README.he.md) · [Svenska](README.sv.md) · [Русский](README.ru.md) · **Suomi**

![Method](https://img.shields.io/badge/method-Balanced%20Scorecard-1F3A5F)
![AI](https://img.shields.io/badge/AI-LLM%20observability-45a1bf)
![Finance](https://img.shields.io/badge/finance-NPV%20·%20IRR%20·%20PI-46a485)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Dashboard](https://img.shields.io/badge/dashboard-Evidence-236aa4)

> Kehys **minkä tahansa tekoälyprojektin mittaamiseen päästä päähän** — token-kulutuksesta
> taloudelliseen tuottoon — **Balanced Scorecardin** (Kaplan & Norton) 4 näkökulman mukaan.
>
> *"Mitä ei mitata, sitä ei voi hallita eikä parantaa."*

> *Kun rukoilet ja opiskelet, älä anna [sanojeni] jättää sinua. Jokaisen huuliltasi lähtevän sanan ja ilmauksen kohdalla pidä mielessä Yhdistymisen aikaansaaminen.* — Aryeh Kaplan

> *Puhdas metafysiikka, sijaiten olemukseltaan kaikkien muotojen ja kaikkien satunnaisuuksien yläpuolella ja tuolla puolen, ei ole itämainen eikä länsimainen: se on universaali.* — René Guénon

> *Itsensä tunteminen on oman sukulinjansa ja oman voimansa tunteminen.* — Harvey Spencer Lewis

> *Scientia es Lux Lucis* ∞ Sapere Aude S∴A∴☬ ☿

> 📖 **Pääkirjaus:** **[`foundations/README.md`](foundations/README.md)** ·
> ⚙️ **Asennus (omat avaimet):** [`foundations/pipeline/SETUP.md`](foundations/pipeline/SETUP.md)

## ✨ Mitä kehys tarjoaa
- **KPI:t (4 BSC-näkökulmaa):** kypsyys, henkinen pääoma, talous + API-talous (`IEET`, `IOLI`, `ITR`, `IITA`, `PEUC`, `ICCA`, `IDLS`, `IBMT`) ja **EVM**.
- **Eturintaman käsitteet:** **VRT/kTR** ja **PSR** (projektipisteet 0–5 ⭐).
- **Talous:** **NPV, IRR, TIRM, VUL, PI, takaisinmaksu**, dollarisointi ja vertailu **SELIC**- ja USA:n korkoon.
- **Visuaalinen:** salkun **5D-kartta**, **Evidence-dashboard** (BI as Code) ja LaTeX-**pitch deckit**.
- **Putki:** **Langfuse → SQLite → Evidence**, asynkroninen rinnakkainen synkronointi ja **Rust (PyO3)**-kiihdytetty luokittelu.

## 🚀 Pika-aloitus (demo, ilman Langfusea)
```bash
cd foundations/pipeline
pip install -r requirements.txt
cd ../evidence && npm install && cd ../pipeline
./run_all.sh --mock          # anonyymit tiedot (Project A..J) -> KPI -> NPV -> 5D -> pitch deckit -> dashboard
cd ../evidence && npm run dev # http://localhost:3000
```

## 🏷️ Topics
`project-management` · `dashboard` · `business-intelligence` · `kpi` · `balanced-scorecard` · `llm` · `ai` · `llm-observability` · `langfuse` · `roi` · `python`

---

**Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard** · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
