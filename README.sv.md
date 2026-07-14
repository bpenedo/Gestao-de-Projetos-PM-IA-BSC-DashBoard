# 🧭 Gestão de Projetos PM IA BSC DashBoard (Build and Analyze Your Own AI Portfolio Projects)

<p align="center">
  <img src="docs/hero.jpg" alt="AI-projektledning PM BSC DashBoard" width="820">
</p>

🌐 [Português](README.md) · [English](README.en.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [中文](README.zh.md) · [한국어](README.ko.md) · [हिन्दी](README.hi.md) · [עברית](README.he.md) · **Svenska** · [Русский](README.ru.md) · [Suomi](README.fi.md)

![Method](https://img.shields.io/badge/method-Balanced%20Scorecard-1F3A5F)
![AI](https://img.shields.io/badge/AI-LLM%20observability-45a1bf)
![Finance](https://img.shields.io/badge/finance-NPV%20·%20IRR%20·%20MIRR%20·%20PI-46a485)
![Decision](https://img.shields.io/badge/MCDM-DEMATEL%20·%20ELECTRE%20·%20PROMETHEE%20·%20MAUT%20·%20MCDA--C-8E44AD)
![Risk](https://img.shields.io/badge/risk-Monte%20Carlo%2010k%20·%20VaR%20·%20CVaR-DC143C)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-PyO3-orange?logo=rust&logoColor=white)
![Dashboard](https://img.shields.io/badge/dashboard-Evidence-236aa4)
![PDF](https://img.shields.io/badge/pitch%20deck-LaTeX-008080)
![i18n](https://img.shields.io/badge/i18n-12%20languages-0E7C86)
![status](https://img.shields.io/badge/status-v1-success)

### 💸 Du betalar för AI varje månad. Men betalar AI **dig** tillbaka?

Varje gång kortet dras av **ChatGPT, Claude, Copilot, Gemini, Perplexity, DeepSeek, Kimi, Qwen…** förblir en
**miljonfråga** obesvarad: **var är avkastningen?** Hur många persontimmar sparades egentligen? Hur mycket av dina
pengar **förångades** i hallucination, omarbete och väntan? Vilket AI-projekt **förtjänar att skalas idag** — och
vilket **blöder kassa** medan du applåderar "innovationen"?

Du har ingen AI-kostnad. Du har ett **tyst läckage** — med ögonbindel på. För *"det som inte mäts kan varken
styras eller förbättras"* — och marknaden mäter det åt dig och skickar räkningen.

**Det här ramverket tänder ljuset.** Det förvandlar de **osynliga utgifterna** för dina AI-prenumerationer till
**mätbar, jämförbar och granskningsbar avkastning** — med stringensen hos **Balanced Scorecard** (Kaplan &
Norton), **investeringsanalys på Wall Street-nivå** och **flerkriteriebeslut**. Det är skillnaden mellan att
*hoppas* och att *veta*. Mellan att betala för AI och att **tjäna** på den.

> *"Det som inte mäts kan varken styras eller förbättras."* — Kaplan & Norton

> *"Den som mäter med precision bygger med excellens."* — Pierre Vernier

> *När du ber och studerar, låt inte [mina ord] lämna dig. Med varje ord och uttryck som lämnar dina läppar, håll i minnet att åstadkomma en Förening.* — Aryeh Kaplan

> *Den rena metafysiken, som till sitt väsen befinner sig ovanför och bortom alla former och alla tillfälligheter, är varken östlig eller västlig: den är universell.* — René Guénon

> *Att känna sig själv är att känna sin egen härkomst och sin egen kraft.* — Harvey Spencer Lewis

> *Scientia es Lux Lucis* ∞ Sapere Aude S∴A∴☬ ☿

> 🐺 **Sluta BETALA för AI i mörkret.** Medan marknaden prenumererar på AI av tro — och blir **Gartner**-statistik
> (≥30 % av GenAI-projekten överges efter piloten) — kommer **du** att mäta varje token, utse det vinnande
> projektet och omvandla osynliga utgifter till **granskningsbar avkastning**: NPV · IRR · MIRR · EAA · 70+ KPI:er
> · flerkriteriebeslut · C-nivå-dashboard på **12 språk**. **AI:n är redan din. Gör den nu LÖNSAM** — gratis, på
> din maskin, på **5 minuter**: `./run_all.sh --mock && npm run dev` 🔥

> 📖 **Huvuddokumentation:** **[`foundations/README.md`](foundations/README.md)** ·
> ⚙️ **Setup (ta med dina egna nycklar):** [`foundations/pipeline/SETUP.md`](foundations/pipeline/SETUP.md) ·
> 📊 **KPI:er:** [`foundations/KPIs.md`](foundations/KPIs.md) / [`foundations/KPIs_README.md`](foundations/KPIs_README.md)

---

## 📑 Innehåll

- [🌅 Varför detta ändrar spelet](#-varför-detta-ändrar-spelet)
- [📈 Bevisen (Gartner · IDC · PwC · McKinsey · MIT)](#-bevisen-gartner--idc--pwc--mckinsey--mit)
- [💥 Kostnaden för passivitet](#-kostnaden-för-passivitet-gör-räknestycket-som-ingen-gör)
- [✨ Funktioner](#-funktioner)
- [📸 Skärmbilder (anonym dashboard)](#-skärmbilder-anonym-dashboard)
- [🚀 Snabbstart](#-snabbstart-demo-utan-langfuse)
- [🏗️ Arkitektur](#️-arkitektur)
- [📊 KPI-katalog](#-kpi-katalog-70)
- [💰 Finansiell investeringsanalys](#-finansiell-investeringsanalys)
- [🏆 Flerkriteriebeslut + Dossier](#-flerkriteriebeslut-ahp-topsis-2n--kronjuvelsdossier)
- [🎲 Monte Carlo — risken som medelvärdet döljer](#-monte-carlo--risken-som-medelvärdet-döljer)
- [🧮 Fem beslutsskolor. En dom.](#-fem-beslutsskolor-en-dom)
- [🔬 Signalen ligger uppströms — och där bor hävstången](#-signalen-ligger-uppströms--och-där-bor-hävstången)
- [🎓 Grunder: vad Monte Carlo är, och vad flerkriteriebeslut är](#-grunder-vad-monte-carlo-är-och-vad-flerkriteriebeslut-är)
- [🌐 12 språk](#-12-språk)
- [🙋 Invändningar (frågorna du ställer dig just nu)](#-invändningar-frågorna-du-ställer-dig-just-nu)
- [🧩 Medföljande Skills](#-medföljande-skills-build--analyze-your-own)
- [📚 Resurser & referenser](#-resurser--referenser-awesome)
- [🗺️ Färdplan](#️-färdplan)
- [🧰 Steg-för-steg-installation (lokalt, från noll)](#-steg-för-steg-installation-lokalt-från-noll)
- [🤝 Bidra](#-bidra)
- [📄 Licens & upphovsrätt](#-licens--upphovsrätt)

---

## 🌅 Varför detta ändrar spelet

**Det finns två sorters människor i AI-eran.** De första prenumererar på allt, spenderar stort och **ber** att det
ska gå bra — och göder den grymma statistiken över projekt som dör i piloten. De andra gör vad Wall Street gör med
varje seriös tillgång: de **mäter, jämför, prioriterar och omfördelar** — och förvandlar varje prenumerationsdollar
till **ränta-på-ränta-avkastning**. Den enda skillnaden mellan dem **är varken talang eller budget. Det är
instrumentering.**

Generativ AI skapade en ny klass av återkommande utgifter — **prenumerationer och tokens** — och med den decenniets
dyraste slöseri: **det osynliga.** Det du inte ser rättar du inte. Det du inte mäter skalar du inte. Och det du inte
bevisar godkänner inte styrelsen.

**Det här projektet flyttar dig från den första stammen till den andra.** Det instrumenterar varje AI-projekt som en
**finansiell tillgång** och mäter det under **Balanced Scorecard**, **investeringsanalys (NPV, IRR, MIRR, EAA, PI,
återbetalningstid)** och **Lean Six Sigma** — och **utser till och med det bästa projektet i din portfölj** via en
flerkriteriemodell (**AHP-TOPSIS 2n**). Den ogenomskinliga månadsräkningen blir en **granskningsbar
investeringstes**: du får veta, med siffror, var du ska skala, var du ska skära, var prenumerationen betalar sig
själv på **veckor** — och var den blöder utan täckning.

Vi är **pionjärer** i ett nytt territorium — **gränsen mellan artificiell intelligens och högvärdig finansiell intelligens**. Som
upptäcktsresande som kartlägger okartlagd mark är detta ramverk **kompassen** (🧭) som förvandlar prenumerationernas
dimma till **tydliga avkastningsrutter**: varje token en mil; varje projekt en expedition mot vinst. Där det fanns
blind kostnad föds **mätbar möjlighet**; där det fanns ett dött kalkylark blomstrar en **levande investeringstes**.

### 🚀 För Micro-SaaS, SaaS, startups och solopreneurer

Här är vad ingen berättade när du byggde in AI i din produkt: **du flyttade just AI från marknadsföringsbudgeten
till din COGS.** Och COGS som växer med användningen är ingen kostnad — det är en **inteckning i din
bruttomarginal**. Varje ny användare kostar nu tokens. Varje omkörning orsakad av hallucination bränner
marginalen två gånger. Och räkningen dyker upp först vid månadsskiftet, när det är för sent att ångra.

| Du är… | Smärtan ingen mäter | Vad ramverket ger tillbaka |
|---|---|---|
| **Solopreneur** | du *är* teamet; din timme är den dyraste tillgång som finns | **tornadon** pekar ut variabeln som rör resultatet — alltså **var du ska investera din nästa timme** |
| **Micro-SaaS** | tokenkostnaden växer med användningen och äter marginalen i tysthet | en fördelning **anpassad till dina verkliga tokens** + **CVaR**: den dåliga månaden har ett pris *innan* den kommer |
| **SaaS i skala** | varje AI-funktion är ett projekt som slåss om samma färdplan | **fem metoder** väljer vilken som går live — och **robustheten** säger om förstaplatsen överlever ett fel på 2 punkter i en vikt |
| **Startup som reser kapital** | investeraren köper inte *"vi använder AI"* | de köper **NPV, IRR, återbetalningstid och `P(NPV<0)`** — och **pitch-decket kommer färdigt**, i LaTeX |

**Vad som faktiskt ändras.** Din bruttomarginal slutar vara en uppskattning och blir en **fördelning med
prissatt svans**. Din runway slutar vara enkel division och får en **VaR**: *"i 19 av 20 scenarier räcker min
kassa minst N månader."* Och när board-decket eller due diligencen kommer öppnar du inte ett kalkylark ingen kan
reproducera — du öppnar en siffra med **fast frö**, som vilken medgrundare, investerare eller revisor som helst
kör om och får **exakt densamma**.

> **En brutal ompositionering:** solopreneuren börjar besluta som en CFO. Och CFO:n börjar besluta i en
> solopreneurs tempo.

> **Löftet:** att förvandla den som *betalar för AI* till den som *tjänar på AI* — och den som *använder AI* till
> den som **pionjärt behärskar, mäter och mångfaldigar den**. Med siffror, inte med tro.

---

## 📈 Bevisen (Gartner · IDC · PwC · McKinsey · MIT)

Tro inte på mig. **Tro på instituten som studerat detta i decennier** — vars dom är enhällig: **AI skapar enormt
värde, men levererar det bara till dem som mäter och styr.** De som "använder AI utan att behärska den" blir en
avhoppsstatistik; de som instrumenterar avkastningen **behåller priset**.

- 🧭 **Gartner** — förutspådde att **≥ 30 % av de generativa AI-projekten skulle överges efter proof of concept
  före slutet av 2025**, med **oklart affärsvärde** som central orsak (utöver dålig data, stigande kostnader och
  svaga kontroller). *→ utan mätning dör projektet i piloten.*
- 🔬 **MIT** (rapporten *"The GenAI Divide / State of AI in Business 2025"*, NANDA-initiativet) — allmänt rapporterat
  att den **stora majoriteten av företags GenAI-piloter inte ger någon mätbar P&L-effekt**; minoriteten som levererar
  värde kombinerar AI med **process och mätning**. *→ skillnaden är att mäta, inte att införa.*
- 💵 **IDC** (studien *"The Business Opportunity of AI"*, sponsrad av Microsoft) — organisationer som **mäter och
  optimerar** rapporterade en avkastning i storleksordningen **flera dollar per 1 US$** investerad i AI, med stor
  spridning mellan ledare och eftersläntrare. *→ ROI finns — och gynnar dem som instrumenterar.*
- 🌍 **PwC** (*"Sizing the Prize"*) — uppskattar att AI kan tillföra upp till **~15,7 biljoner US$** till den globala
  ekonomin till 2030; men priset går till dem som **fångar** värdet, inte till dem som bara konsumerar det. *→ kakan
  är gigantisk; biten tillhör dem som mäter.*
- 🏆 **McKinsey** (*"The State of AI"*) och **BCG × MIT Sloan** — en minoritetsgrupp av **"AI high performers"**
  fångar oproportionerlig avkastning; vändpunkten kommer när AI kopplas till **mätvärden, styrning och återinvestering**
  där avkastningen är bevisad. *→ vinnarna mäter, prioriterar och omfördelar.*

> **Det är precis den klyftan detta ramverk korsar:** det tar dig från sidan som *ger upp i piloten* till sidan med
> **faktiska, bevisade resultat** — med BSC, investeringsanalys och flerkriteriebeslut.

> ⚠️ **Ärlighetsnotis (läs):** siffrorna ovan speglar verkliga rubriker från dessa institut, men **rapporter och
> procentsatser uppdateras** — verifiera exakta värden och år i **primärkällorna** (Gartner Newsroom; IDC/Microsoft
> *Business Opportunity of AI*; PwC *Sizing the Prize*; McKinsey *State of AI*; MIT *State of AI in Business*) innan
> du citerar dem i officiellt material. Här tjänar de som **riktningsgivande grund**, inte som numerisk garanti.

---

## 💥 Kostnaden för passivitet (gör räknestycket som ingen gör)

En **PRO-AI**-prenumeration kostar mellan **20 och 200 US$ per månad och plats**. Multiplicera med antalet personer
i ditt team. Multiplicera med 12 månader. Tillämpa nu det som instituten redan **bevisat**: **Gartner** projicerar
**≥ 30 % avhopp** och **MIT** visar att **majoriteten av piloterna inte ger avkastning**. En enorm del av den summan
är ingen investering — det är **ren blödning**.

> **Konkret exempel (byt ut mot dina siffror):** 10 platser × 30 US$/mån × 12 = **3 600 US$/år**. Om ~30 % blir
> osynligt slöseri är det **~1 080 US$/år som förångas** — från ETT litet team, på ETT år. Med din verkliga siffra
> är chocken större.

Och här är det som gör ont: **den här kostnaden ackumuleras och väntar inte.** Varje månad utan mätning är en månad
av läckage som **inte kommer tillbaka** — medan konkurrenten som instrumenterat redan **omfördelar kapital till det
som lönar sig**. Pionjärfördelen byggs tidigt: **den som mäter först skalar först.**

Det billigaste ögonblicket att börja var igår. Det näst bästa är **nu** — och det kostar **0 US$** och **5 minuter**.
Frågan är inte *"har jag råd att mäta?"*. Den är ***"hur länge till har jag råd att INTE mäta?"***

---

## ✨ Funktioner

- **📊 KPI:er (4 BSC-perspektiv) + API-ekonomi:** mognad, humankapital, finansiellt och token-effektivitet — `IEET`,
  `IOLI`, `ITR`, `IITA`, `PEUC`, `ICCA`, `IDLS`, `IBMT` — plus **EVM** (CPI/SPI/EAC).
- **🪙 Frontkoncept:** **VRT/kTR** (tokeniserbar kostnadsåtervinningsenhet — *"Gitmans m²"*) och **PSR** (Project
  Score 0–5 ⭐) för att rangordna varje projekts hälsa.
- **🔬 Driftdiagnostik:** **VRT i 5 block**, **HCI** (kritisk avbrottstimme), **Lean Six Sigma-slöserier** (viktade
  tokens) och **hallucinations-RCA per prompttaxonomi** (flaskhals per projekt + snitt).
- **💰 Fullständig finanssvit:** **NPV, IRR, MIRR, EAA (ekvivalent annuitet), PI, återbetalningstid** (enkel &
  diskonterad), **dollarisering** och jämförelse med **SELIC** och den **amerikanska räntan**.
- **🏆 Flerkriteriebeslut:** **AHP-TOPSIS 2n** (dubbel normalisering) utser det **bästa projektet** i portföljen med
  **robusthetstest** — och genererar ett **administrativt dossier** (SWOT, PESTELC, 5W4H, Pareto, GUT, Radar).
- **🗺️ C-nivå-visualisering:** **interaktiv 5D-karta**, djup-donutar, hållbarhetskvadrant, trender och LaTeX-**pitch
  decks** för behöriga projekt.
- **⚙️ Verklig pipeline:** **Langfuse → SQLite → Evidence**, med **asynkron samtidig** synk och klassificering
  accelererad i **Rust (PyO3)**.
- **💳 AI-FinOps:** katalog över **prenumerationsplaner** (OpenAI, Anthropic, Google, Perplexity, xAI, Mistral,
  DeepSeek, Kimi, Qwen…) med **växelkurs + IOF** och fördelningsbas (burn rate).
- **🌐 12 språk** i dashboarden **och i texten inuti diagrambilderna** (inkl. Devanagari, Hebreiska och CJK).
<!-- eixo-execucao -->
- **📅 Monte Carlo-tidplan (PERT) + Gantt:** samma Monte Carlo-motor riktad mot **aktivitetslängder** — fördelning av slutdatum, **P80** (åtagandet PMI rekommenderar), `P(i tid)` och **kritisk linje** med **kritikalitetsindex** (i hur många % av de 10 000 simuleringarna varje aktivitet är kritisk — det som deterministisk CPM döljer).
- **📐 Earned Value Management + Earned Schedule:** **SPI · CPI · EAC · ETC · VAC · TCPI** och **S-kurvan** (PV/EV/AC). Förenar **kostnad + tid + omfattning** i en bild. **SPI(t)** rättar SPI:s kända brist: att konvergera mot 1 i slutet även när projektet är försenat.
- **⚙️ AI:ns exekveringshälsa över tid:** latens **p50/p95/p99** mot ett **SLO**, **token budget burndown**, **kvalitetsregression** (SPC-liknande regel) och **modelldrift** via **Kolmogorov-Smirnov** — allt från **verkliga** Langfuse-loggar.
- **🚨 Riskregister + Sannolikhets-×-Konsekvens-matris:** den *kvalitativa* risk varje PMO kräver, med ägare, trigger och åtgärd. Sannolikheterna är **förankrade i verkliga signaler** (SLO-brott, CPI, drift), inte gissningar.
- **🌊 Flödesmått (Kanban):** **CFD**, **cykeltid P50/P85** (prognos per percentil, inte gissning), **throughput** och **WIP**.

---

## 📸 Skärmbilder (anonym dashboard)

> 100 % anonym demo (projekt visas som *Project A…J*). Verklig data/verkliga namn följer aldrig med paketet.

**🌐 Portföljens 5D-karta** — 5 dimensioner per projekt: **X**=tokens · **Y**=PEUC (kvalitet) · **Z**=PSR (hälsa) ·
**storlek**=Burn Rate · **färg**=ICCA (hållbarhet). *Var ska man skala? Höger/bak, högt och grönt. Var ska man skära?
Stort och rött.*

![5D-karta över AI-projektportföljen](docs/screenshots/5d-portfolio-map.png)

**🏆 "Kronjuvels"-dossier** (projekt utsett av AHP-TOPSIS) — genererat av en samtidig Python-pipeline:

| SWOT | Konkurrensradar |
|---|---|
| ![SWOT](docs/screenshots/swot.png) | ![Konkurrensradar](docs/screenshots/radar.png) |

| PESTELC (makromiljö) | GUT-matris (prioritering) |
|---|---|
| ![PESTELC](docs/screenshots/pestel.png) | ![GUT](docs/screenshots/gut.png) |

| 5W4H (handlingsplan) | Fel-Pareto (80/20) |
|---|---|
| ![5W4H](docs/screenshots/5w4h.png) | ![Pareto](docs/screenshots/pareto.png) |

### 📅 Exekveringsaxeln — tidplan, earned value, AI-hälsa, risk och flöde

**Gantt med kritisk linje** — röda staplar är den kritiska linjen; **%** på varje aktivitet är *kritikalitetsindex*: i hur många procent av de 10 000 simuleringarna aktiviteten styrde slutdatumet.

![Gantt med kritisk linje — röda staplar är den kritiska linjen; % på va](docs/screenshots/cronograma-gantt.png)

**Tidsrisk** — fördelningen av slutdatum, med deadline, **P50** och **P80** utmarkerade. Åta dig P80, inte den deterministiska skattningen (optimistisk pga merge bias).

![Tidsrisk — fördelningen av slutdatum, med deadline, P50 och P80 utmark](docs/screenshots/cronograma-risco-prazo.png)

**EVM:s S-kurva** — PV (planerat) · EV (intjänat) · AC (verklig kostnad). EV under PV = försening; AC över EV = budgetöverskridande.

![EVM:s S-kurva — PV (planerat) · EV (intjänat) · AC (verklig kostnad). ](docs/screenshots/evm-curva-s.png)

**Latens under SLO** — p50/p95/p99 per dag, från verkliga loggar. Korsad linje = tjänsten försämrades.

![Latens under SLO — p50/p95/p99 per dag, från verkliga loggar. Korsad l](docs/screenshots/exec-latencia-slo.png)

**Riskmatris S × K** — bubbla = exponering (S×K). Sannolikheten förankrad i projektets verkliga signaler.

![Riskmatris S × K — bubbla = exponering (S×K). Sannolikheten förankrad ](docs/screenshots/risco-matriz-pi.png)

**Cumulative Flow Diagram** — parallella band = friskt flöde; ett band som sväller = flaskhals / fastnat WIP.

![Cumulative Flow Diagram — parallella band = friskt flöde; ett band som](docs/screenshots/fluxo-cfd.png)

---

## 🚀 Snabbstart (demo, utan Langfuse)

**Noll risk. Noll kostnad. 5 minuter.** Kör den på din maskin och se hela dashboarden med anonym data:

```bash
cd foundations/pipeline
pip install -r requirements.txt
cd ../evidence && npm install && cd ../pipeline
./run_all.sh --mock          # anonym data (Project A..J) -> KPI -> NPV/MIRR/EAA -> 5D -> pitch decks -> dashboard
cd ../evidence && npm run dev # http://localhost:3000
```

För **verklig data**, fyll i `foundations/pipeline/.env` med **dina egna** Langfuse-nycklar (se
[`SETUP.md`](foundations/pipeline/SETUP.md)) och kör `./run_all.sh`. Varje användare använder sitt **eget konto** —
inga författarnycklar följer med paketet.

---

## 🏗️ Arkitektur

```
   Dina AI-appar               Observerbarhet         Analytics-as-Code           Du
 (ChatGPT, Claude, API…)   ┌──────────────┐   ┌──────────────────┐   ┌──────────────────────┐
        │ traces           │   Langfuse   │   │  SQLite (schema  │   │  Evidence (BI as     │
        └─────────────────▶│  (SDK v4)    │──▶│  + KPI-frågor)   │──▶│  Code) · 12 språk    │
                           └──────────────┘   └──────────────────┘   └──────────┬───────────┘
   asynkron samtidig synk               klassificering i Rust (PyO3)            │
                                                                    ┌───────────┴───────────┐
                                                                    │ AHP-TOPSIS · Dossier  │
                                                                    │ 5D · Pitch decks (TeX)│
                                                                    └───────────────────────┘
```

**Stack:** Python 3.13 · SQLite/DuckDB · Evidence.dev (SvelteKit) · Rust + PyO3 + maturin · matplotlib ·
tectonic (LaTeX) · Noto/WenQuanYi-typsnitt för bild-i18n.

---

## 📊 KPI-katalog (70+)

Urval (fullständig katalog i [`foundations/KPIs_Lean6s_BSC.md`](foundations/KPIs_Lean6s_BSC.md)):

| Förkortning | Namn | Vad den besvarar |
|---|---|---|
| **PSR** | Project Score Rating (0–5) | AI-projektets övergripande hälsa |
| **PEUC** | % nyttig leverans per förbrukning | Hur mycket av utgiften som blev nyttig leverans |
| **IITA** | Index för hallucinerade tokens | % hallucination/omarbete |
| **IDLS** | Lean-slöseriindex | Muda (tokens viktade efter allvar) |
| **VRT/kTR** | Tokeniserbart återvinningsvärde | "Gitmans m²" — kostnad per 1k tokens |
| **ICCA** | Kostnadstäckningsindex per prenumeration | Täcker den kostnaden? (>3× friskt) |
| **CPP** | Kostnad per framstegspoäng | Huvudindikator (lägre är bättre) |

---

## 💰 Finansiell investeringsanalys

Varje projekt blir en **investeringstes**: från ditt kassaflöde (CSV) beräknar ramverket **NPV**, **IRR**, **MIRR
(återinvesterar till projektkostnaden)**, **EAA (ekvivalent annuitet av NPV)**, **PI (lönsamhetsindex)** och
**återbetalningstid** (enkel/diskonterad) — det **dollariserar** flödet och jämför med **SELIC** och den
**amerikanska räntan**. Det genererar en LaTeX-**pitch deck** för varje projekt med **NPV > 0 och PI > 1** i både BRL
**och** USD. Målet är brutalt praktiskt: **att ta reda på om din AI-prenumeration betalar sig — och hur snabbt.**

---

## 🏆 Flerkriteriebeslut (AHP-TOPSIS 2n) + Kronjuvelsdossier

Med flera projekt, vilket ska skalas först? **AHP-TOPSIS 2n**-modellen viktar indikatorerna som kriterier (vikter via
**AHP** med konsistenskvot **CR ≤ 0,10**) och rangordnar med **TOPSIS** över **två normaliseringar** (vektor +
min-max), och rapporterar **robusthet** (överensstämmelse mellan normaliseringarna). Vinnaren — **"Kronjuvelen"** —
får ett fullständigt **administrativt dossier** (SWOT · PESTELC · 5W4H · Pareto · GUT · Radar) genererat från grunden
av kod, med en verkställande **Bottom-Line** och ärliga **C-nivå-insikter**. **Du presenterar inte ett kalkylark. Du
presenterar en dom.**

---

## 🎲 Monte Carlo — risken som medelvärdet döljer

Ett **i genomsnitt** positivt NPV skyddar ingen. Medelvärdet är finansvärldens bekvämaste lögn: det beskriver ett
scenario som kanske aldrig inträffar. Det som avgör ditt öde är **svansen** — den dåliga dagen.

Detta ramverk simulerar **10 000 framtider** för varje projekt: varje kassaflöde blir en **slumpvariabel** och hela portföljen räknas om iteration för
iteration. Till slut har du inte ett tal — du har **hela fördelningen av dina pengar**:

- **`P(NPV < 0)`** — den verkliga sannolikheten för förlust. Talet ingen visar dig.
- **VaR 5 %** — det värsta rimliga scenariot: *"i 19 av 20 framtider tjänar jag minst detta."*
- **CVaR 5 %** — när katastrofen väl inträffar, vad den kostar i genomsnitt.
- **Känslighetstornado** — multipel regression och Pearsonkorrelation: vilken variabel som verkligen rör ditt NPV.
- **20 indatafördelningar**, en validerad **korrelationsmatris** (Iman-Conover, som bevarar marginalfördelningarna
  exakt) och **percentiler från 1 % till 99 %**, med ett histogram på 100 klasser.

Fast frö: kör igen och du får **exakt** samma resultat. Granskningsbart — inte "magi".

> **Vändningen:** du slutar välja projektet med högst NPV och börjar välja **det som överlever det dåliga scenariot**.
> Det är riskhantering — det som skiljer investeraren från spelaren.

![Histograma de Monte Carlo do VPL — 10.000 iterações, 100 classes](docs/screenshots/mc-histograma.png)

| Kumulativ fördelning av NPV | Känslighetstornado |
|---|---|
| ![Kumulativ fördelning av NPV](docs/screenshots/mc-acumulado.png) | ![Känslighetstornado](docs/screenshots/mc-tornado.png) |

---

## 🧮 Fem beslutsskolor. En dom.

En metod kan ha fel. Fem metoder som är eniga kan det inte.

Enligt arkitekturen hos **John (2025)** — *Integration of DEMATEL with Other MCDM Methods* — kartlägger **DEMATEL** den
kausala strukturen mellan kriterierna och skiljer **orsaker** (spakar att agera på) från **verkningar** (termometrar för
det som redan gjorts). Ur dessa inflytandeslingor föds **vikterna**: inte godtyckliga, utan **härledda ur problemets
struktur**. De matar fyra rivaliserande skolor:

| Metod | Skola | Vad den frågar |
|---|---|---|
| **ELECTRE I** | Överklassning | "Vem överklassar vem — och vem överlever odominerad?" |
| **PROMETHEE II** | Överklassning | "Vad är varje projekts nettopreferensflöde?" |
| **MAUT** | Nytta | "Vilket maximerar nyttan för en riskavert beslutsfattare?" |
| **MCDA-C** | Konstruktivistisk | "Vem ligger över nivån *Bra* — och vem under *Neutral*?" |
| **AHP-TOPSIS 2n** | Avstånd till idealet | "Vem är närmast ideallösningen i båda normaliseringarna?" |

Vinnaren kommer ur **Borda-konsensus** mellan de fem, redan **riskjusterad** av Monte Carlo. Och när metoderna är
**oense** visar dashboarden oenigheten — för det är information: valet är känsligt för beslutsskolan och förtjänar
beslutsfattarens öga.

| DEMATEL — orsaker × verkningar | Placering per metod |
|---|---|
| ![DEMATEL — orsaker × verkningar](docs/screenshots/dematel.png) | ![Placering per metod](docs/screenshots/mcdm-metodos.png) |

### 💼 Vad som ändras i din vardag — från frilansare till koncern

Det spelar ingen roll om du betalar **20 US$ på ett PRO-abonnemang** eller **200 000 US$ i företagsavtal**: matematiken
för slöseri är densamma — bara antalet nollor ändras.

| | **SMB / frilansare** | **Storföretag** |
|---|---|---|
| **Den verkliga smärtan** | 3 abonnemang, noll överblick, tight kassa | 40 AI-piloter, ingen med tillskrivet resultat |
| **Monte Carlo levererar** | *"detta projekt har 12 % risk att gå med förlust, och den dåliga månaden kostar 3 400 US$"* | VaR/CVaR per affärsenhet: aggregerad, granskningsbar risk — inte anekdot |
| **MCDM levererar** | vilket av de 3 projekten som ska skalas **först**, med pengarna som finns | vilken av de 40 piloterna som blir produkt — försvarbart i kommittén, metoden explicit |
| **Vinsten redan imorgon** | säg upp abonnemanget som inte betalar sig, redan denna vecka | omfördela budget på **evidens**, inte på internpolitik |

**I praktiken:** **tornadon** pekar ut variabeln som rör resultatet — alltså **var du ska investera din nästa
arbetstimme**. **DEMATEL** avslöjar att minska hallucination (IITA) är en **orsak**, inte ett symptom: agera där, så
förbättras NPV, IRR och risk *tillsammans*. Det är AI-styrning som slutar vara åsikt och blir **ingenjörskonst**.


---

## 🔬 Signalen ligger uppströms — och där bor hävstången

Jag upptäckte det genom att mäta ramverket självt: NPV:s känslighetstornado returnerade **exakt**
`1,0 · 0,9091 · 0,8264 · 0,7513…` — diskonteringsfaktorerna `1/(1+i)ᵗ`. Eftersom NPV är **linjärt** i kassaflödena
säger en simulering av enbart flödena ingenting utöver räntan. **Den verkliga stokastiska signalen ligger uppströms:
i tokens.**

### 1️⃣ Sluta godtyckligt välja fördelning. Anpassa den till dina data.

Elva kandidatfördelningar anpassas med **maximum likelihood** till din verkliga tokenförbrukningsserie
(`logs_langfuse`). Den med **lägst AIC** vinner — AIC bestraffar varje extra parameter och förhindrar överanpassning —
och **Kolmogorov-Smirnov**-testet mäter anpassningsgraden. Detta är den klassiska *fördelningsanpassningen till data*, och det är
vad som avslöjar förbrukningens **tunga svans**: vissa prompter kostar 10× det typiska, och det är den svansen som
spränger budgeten — osynlig för den som använder medelvärden.

**Och när anpassningen är dålig skriker ramverket.** Om KS p-värdet faller under 0,05 varnar skärmen `SVAG ANPASSNING`
i rött, i stället för att låtsas precision. En ärlig siffra slår en vacker.

![Fördelningsanpassning till verkliga tokens — 11 kandidater, AIC-urval, Kolmogorov-Smirnov-anpassning](docs/screenshots/ajuste-distribuicoes.png)

### 2️⃣ Överlever din rangordning ett fel på 2 punkter i en vikt?

Varje flerkriteriemetod returnerar en vinnare med **implicit 100 % säkerhet**. Men kriterievikter är skattningar, inte
uppenbarade sanningar. Om två procentenheter på IITA-vikten byter plats på 1:a och 2:a, är "vinnaren" en artefakt av
kalibreringen.

Så vi stör DEMATEL-vikterna med en **Dirichlet** — `w' ~ Dir(κ·w)`, som lever exakt på simplexet och bevarar
`E[w'] = w`, alltså stör **utan att snedvrida** — och rangordnar om **2 000 gånger**. Domen byter natur:

> *"Project C är bäst"* ⟶ **"Project C vinner i 99,9 % av de rimliga preferensuniversumen"**

Det är ett **konfidensintervall för själva beslutet**. Och det avslöjar vad konsensus dolde: i skärmen nedan
**väljer PROMETHEE II ledaren i endast 25,4 % av universumen**. Fyra skolor är eniga; en avviker rakt av. Det är inte
brus — det är varningen att valet beror på om du föredrar *överklassning* framför *nytta*. Ingen enskild rangordning
skulle någonsin berätta det.

![Rangordningens robusthet via Dirichlet-störning — vinstsannolikhet och oenighet mellan skolor](docs/screenshots/robustez-dirichlet.png)

### ⚡ Den konkreta hävstången

| Resurs | Före | Efter |
|---|---|---|
| **Tid** | veckor av debatt om vilket projekt som ska skalas | domen kommer med en sannolikhet — debatten avslutas på ett möte |
| **Beräkning** | 10 000 iterationer × 10 projekt, vektoriserat i NumPy | sekunder, på din maskin, utan moln och utan kostnad |
| **Kapital** | budget fördelad efter övertygelse | fördelad efter `P(vinst)` och `VaR` — värsta fallet redan prissatt |
| **Anseende** | *"jag tror att den här är bäst"* | *"den vinner i 99,9 % av scenarierna; och här är metoden som avviker, och varför"* |
| **Granskningsbarhet** | ett kalkylark ingen kan reproducera | fast frö: vem som helst kör om och får **exakt** samma siffra |

### 💼 Från 20-dollarsabonnemanget till 200 000-dollarskontraktet

**Är du frilansare eller SMB:** den anpassade fördelningen säger vad **den dåliga tokenmånaden kommer att kosta**
innan den kommer — och robustheten säger om det verkligen lönar sig att flytta insatsen till det andra projektet,
eller om båda är jämna inom felmarginalen. Du slutar optimera i mörker med tight kassa.

**Är du ett storföretag:** `P(vinst)` är den saknade pusselbiten i investeringskommittén. Den förvandlar *"team A
förespråkar projekt X"* till **"projekt X vinner under 99,9 % av försvarbara viktkalibreringar, och den enda
avvikande skolan är överklassning, på kriterium Y"**. Politisk debatt blir **teknisk debatt** — och CFO får en siffra
som överlever revision.

> **Den sista vändningen:** ramverket slutar mäta risken i **pengarna** och börjar mäta risken i **själva beslutet**.
> Väldigt få platser i världen gör detta.

---

## 🎓 Grunder: vad Monte Carlo är, och vad flerkriteriebeslut är

### 🎲 Matematisk Monte Carlo-simulering

#### 📖 Begreppet

Monte Carlo är en numerisk metod som besvarar frågor om osäkra system **genom slumpmässig sampling**. Idén vänder
matematikerns instinkt upp och ned: i stället för att härleda svaret på **sluten form** — lösa integralen, kombinatoriken,
differentialekvationen — bygger man en **modell**, drar tusentals realiseringar av de osäkra variablerna och **räknar helt
enkelt vad som hände**. Det man får till slut är inte ett tal: det är **resultatets sannolikhetsfördelning**.

Två lagar bär upp den. **Stora talens lag** garanterar att medelvärdet av simuleringarna konvergerar mot det sanna värdet.
**Centrala gränsvärdessatsen** säger hur snabbt: standardfelet avtar som `1/√N`. Följden är ärlig och något grym — **för
att fördubbla precisionen måste man fyrdubbla iterationerna**. Monte Carlo är inte snabbt. Dess dygd ligger på annat håll:
felet **beror inte på problemets dimension**. Deterministiska kvadraturmetoder lider av *dimensionalitetens förbannelse*
och kollapsar vid dussintals variabler; Monte Carlo gör det inte. Den vinner precis där den analytiska matematiken dör.

#### 📖 Var och när den uppstod

**Los Alamos, New Mexico, 1946.** Den polske matematikern **Stanisław Ulam** konvalescerade efter en hjärninflammation och
lade patiens dagarna i ända. Han undrade vad sannolikheten att vinna ett parti var. Han försökte med kombinatoriken och gav
upp: ohanterlig. Då slog honom något så enkelt att det såg ut som fusk — **spela hundra partier, räkna hur många du vinner
och dividera**. Han insåg omedelbart att detta inte var ett korttrick: det var en **allmän integrationsmetod** för problem
som ingen visste hur man löste.

Han tog idén till **John von Neumann**, som genast såg tillämpningen på problemet som upptog dem i Manhattanprojektet:
**neutrondiffusion** i klyvbart material. Att **simulera** slumpvandringen hos tusentals neutroner — spridning, absorption,
klyvning — var genomförbart; att lösa transportekvationen var det inte. **Nicholas Metropolis** föreslog namnet **"Monte
Carlo"**, efter kasinot i Monaco där en morbror till Ulam brukade låna pengar för att spela. **ENIAC** gjorde de första
beräkningarna möjliga, och **1949** publicerade Metropolis och Ulam *"The Monte Carlo Method"* i *Journal of the American
Statistical Association*.

Metoden föddes, bokstavligen, ur mötet mellan ett **kortspel** och **atombomben**. Få vetenskapliga idéer har ett så
förbryllande födelsebevis.

#### 📖 Metodiken, i fem steg

1. **Modellera.** Skriv utfallet som en funktion av indata: `y = f(x₁, …, xₙ)`.
2. **Tilldela fördelningar.** Varje osäkert indata får en fördelning. Finns **historiska data** *anpassas* den till dem; om
   inte, postuleras den — och det måste **deklareras**.
3. **Sampla.** Dra `N` scenarier. Är variablerna **korrelerade** måste samplingen respektera den strukturen: att dra
   oberoende där verkligt beroende finns är metodens vanligaste fel.
4. **Propagera.** Beräkna `f` i varje scenario. Här **förvandlas** indatas osäkerhet till utfallets osäkerhet, utan någon
   linjär approximation.
5. **Analysera.** Studera fördelningen: medelvärde och spridning, **percentiler**, händelsesannolikheter (`P(y < 0)`),
   **svansen** (VaR, CVaR) och **känsligheten** (vilket `xᵢ` rör `y`).

#### 📖 Användning och tillämpningar i världen

- **Finans:** prissättning av exotiska optioner (utan sluten form), **VaR** och **CVaR** för portföljer, regulatoriska
  stresstester (Basel), kreditrisk.
- **Teknik:** strukturell tillförlitlighet, tillverkningstoleranser, felanalys i komplexa system.
- **Projektledning:** tids- och kostnadsrisk (PERT:s probabilistiska utveckling), S-kurvor för färdigställande.
- **Fysik och kemi:** partikeltransport, strålskärmning, statistisk mekanik.
- **Operations och försörjningskedjor:** köer, lager, kapacitet under osäker efterfrågan.
- **Epidemiologi:** sjukdomsspridning och policyutvärdering under osäkerhet.
- **Inom AI självt:** **MCMC** (bayesiansk inferens), **MCTS** — trädsökningen som förde AlphaGo förbi Lee Sedol — och
  *Monte Carlo dropout* för att skatta osäkerhet i neurala nät.

#### 🔒 Metodik, användning och tillämpning EXKLUSIVA för detta projekt

Här är Monte Carlo ingen akademisk utsmyckning: den är portföljens **riskmotor**.

- **Indata.** Varje periodiskt kassaflöde blir en **triangulär** variabel (`min`, `typvärde`, `max`), med typvärde vid det
  deterministiska värdet och svansar vid ±30 %. **Tokenförbrukningen** — den enda verkligt tungsvansade variabeln —
  **postuleras inte**: elva kandidatfördelningar **anpassas med maximum likelihood** till din verkliga `logs_langfuse`-serie,
  den med **lägst AIC** vinner, och anpassningen mäts med **Kolmogorov-Smirnov**. Faller p-värdet under 0,05 skriver skärmen
  `SVAG ANPASSNING` i rött i stället för att låtsas precision.
- **Korrelationen.** När flödena är beroende använder samplingen **Iman-Conover**, som påtvingar rangkorrelation samtidigt
  som den **bevarar marginalfördelningarna exakt**. Matrisen valideras först: symmetrisk, enhetsdiagonal, positivt definit.
- **Propageringen.** **10 000 iterationer** per projekt, med **fast frö (42)**: kör igen och du får exakt samma tal. Det är
  ingen detalj — det är vad som gör resultatet **granskningsbart** av en delägare, en investerare eller en revisor.
- **Utfallen.** Inte bara NPV: vi simulerar **NPV, IRR, MIRR, EAA, PI** och **tokenkostnaden**, var och en med de tio
  klassiska deskriptiva måtten (skevhet och kurtosis enligt Excels definitioner), **percentiler från 1 % till 99 %** och ett
  **histogram med 100 klasser**.
- **Risken som betyder något.** `P(NPV < 0)` är den verkliga sannolikheten för förlust. **VaR 5 %** är det värsta rimliga
  scenariot — *"i 19 av 20 framtider tjänar jag minst detta"*. **CVaR 5 %** besvarar det ingen frågar: när katastrofen väl
  inträffar, **vad kostar den i genomsnitt**.
- **Känsligheten.** **Tornadon** beräknas i båda klassiska formerna: **betana från en multipel regression** (effekten av +1 i
  ett indata på NPV) och **Pearsonkorrelationen** (hur mycket det indatats osäkerhet styr NPV:s osäkerhet). Komplementära
  läsningar; dashboarden visar båda.
- **En upptäckt ramverket gjorde om sig självt.** När det mätte sig självt gav tornadon betan **exakt lika med
  diskonteringsfaktorerna** `1/(1+i)ᵗ` — eftersom NPV är *linjärt* i flödena. Att bara simulera flödena säger alltså inget
  utöver räntan. **Den verkliga stokastiska signalen ligger uppströms, i tokens.** Den insikten motiverade
  fördelningsanpassningen till verkliga data.
- **Risken göder beslutet.** Två Monte Carlo-utfall går in som **kriterier** i flerkriteriemodellen: `P(NPV<0)` som ett
  **kostnads**kriterium och **VaR 5 %** som ett **nytto**kriterium. Det slutliga valet föds därför redan **riskjusterat**, inte
  bara justerat för väntevärdet.


**Vad det är.** En metod som besvarar svåra frågor **genom lottning**. I stället för att lösa matematiken i ett
osäkert system på sluten form — ofta omöjligt — tilldelar man **sannolikhetsfördelningar** till indatavariablerna,
drar tusentals scenarier, beräknar utfallet i vart och ett och betraktar **hela fördelningen** av utfall. Stora
talens lag garanterar konvergens; felet avtar som `1/√N`, det vill säga **att fyrdubbla iterationerna halverar
felet**.

**Hur den föddes.** Los Alamos, 1946. **Stanisław Ulam**, konvalescent efter en sjukdom, lade patiens och undrade
vad sannolikheten att vinna var. Han insåg att lösa kombinatoriken var brutalt — men att **simulera** hundratals
partier och helt enkelt räkna var trivialt. Han tog idén till **John von Neumann**, och de båda tillämpade den på
problemet som upptog dem i Manhattanprojektet: **neutrondiffusion** i klyvbart material. **Nicholas Metropolis**
döpte metoden till "Monte Carlo", efter kasinot i Monaco där en morbror till Ulam brukade spela. **ENIAC** gjorde de
första beräkningarna möjliga. Metoden föddes, bokstavligen, ur mötet mellan ett kortspel och atombomben.

**Var den används idag.** Optionsprissättning och **VaR** inom finans; strukturell tillförlitlighet inom teknik;
tids- och kostnadsrisk i projektledning; partikelfysik; försörjningskedjor; epidemiologi. Och inom AI självt:
**MCMC** (bayesiansk inferens) och **MCTS** — trädsökningen som förde AlphaGo förbi Lee Sedol.

**Hur den tjänar oss här.** Varje kassaflöde i ditt projekt blir en slumpvariabel, och tokenförbrukningen får den
fördelning som är **anpassad till dina verkliga data**. Vi kör 10 000 scenarier och till slut har du inget NPV — du
har **fördelningen av dina pengar**: `P(NPV < 0)` (den verkliga sannolikheten för förlust), **VaR 5 %** (det värsta
rimliga scenariot), **CVaR 5 %** (vad det kostar när katastrofen inträffar) och **tornadon** (vilken variabel som
faktiskt rör resultatet). Medelvärdet ljuger; svansen avgör.

### 🧮 Flerkriterieanalys för beslut (MCDA)

#### 📖 Begreppet och vad det är till för

Att välja mellan projekt är svårt av två skäl som inget kalkylark löser. För det första **står kriterierna i konflikt**:
projektet med högst NPV är oftast det mest riskfyllda. För det andra är de **inkommensurabla**: det finns ingen ärlig
aritmetik som adderar kronor, hallucinationsprocent och omarbetningstimmar.

MCDA (*Multi-Criteria Decision Analysis*) är fältet — fött på 1960-70-talen, i gränslandet mellan operationsanalys och
beslutsteori — som möter precis detta. Det **lovar inte rätt svar.** Det lovar något nyttigare: att göra valet
**explicit, granskningsbart och försvarbart**.

Dess grundtes är obekväm och befriande på samma gång: **det finns inget "bäst" i ett vakuum.** Det finns ett bäst *givet ett
preferenssystem som någon gjort explicit*. Varje beslutsfattare arbetar redan med ett preferenssystem — skillnaden är att det
utan MCDA är **implicit, inkonsekvent och ogranskningsbart**. Att byta den tysta åsikten mot en explicit modell: där ligger
hela vinsten.

#### 📖 Användning och tillämpningar i världen

Leverantörsval och portföljprioritering; val av energiteknik (sol × vind × biomassa); lokalisering av fabriker, sjukhus och
deponier; miljökonsekvensbedömning; offentlig politik och budgetallokering; personalurval; underhållsprioritering; och —
alltmer — **teknoekonomisk bedömning** av framväxande teknik, vilket är precis fallet med en AI-projektportfölj.

#### 📖 De tre beslutsskolorna

- **Amerikanska skolan (värde och nytta).** Aggregerar allt till **ett enda tal**. Antar att ett dåligt betyg på ett kriterium
  kan **kompenseras** av toppbetyg på andra. Enkel, kraftfull — och ibland farlig. `AHP`, `MAUT`.
- **Europeiska skolan (överklassning).** Grundad av **Bernard Roy**. Accepterar att två alternativ kan vara **ojämförbara**
  och tillåter **veto**: en katastrofal prestation på ett kriterium **köps inte loss** av excellens på andra. Den modellerar
  beslutsfattarens verkliga tvekan genom **trösklar**. `ELECTRE`, `PROMETHEE`.
- **Konstruktivistiska skolan.** Modellen *upptäcks* inte, den **byggs tillsammans med beslutsfattaren**, genom
  problemstrukturering och skalor förankrade i referensnivåer. `MCDA-C`.

#### 📖 1. DEMATEL — *Decision-Making Trial and Evaluation Laboratory*

**Vad det är.** Skapad av **Gabus & Fontela** vid **Battelle Memorial Institute** (Genève, 1972-73) för att studera komplexa,
sammanflätade världsproblem. Den **rangordnar inte alternativ**: den kartlägger den **kausala strukturen mellan kriterierna**.

**Hur den fungerar.** Experter fyller i en **direktrelationsmatris** `Z` (hur mycket kriterium *i* påverkar *j*, från 0 till 4).
Man normaliserar med `s = max(största radsumma, största kolumnsumma)` och får **totalrelationsmatrisen** `T = X(I − X)⁻¹`, som
summerar direkt påverkan **och all indirekt**, längs vilken väg som helst. Därur kommer `R` (radsummor) och `C` (kolumnsummor):
**`R+C` är prominensen** (betydelse i systemet) och **`R−C` är relationen** (positiv = **orsak**; negativ = **verkan**).

**Allmän användning.** Hållbara försörjningskedjor, hinder för teknikadoption, systemisk riskanalys.

**🔒 I detta projekt.** DEMATEL besvarar frågan som **föregår** rangordningen: *"var ska jag agera?"*. Den avslöjar att
**IITA (hallucination), PSR (hälsa) och IDLS (Lean-slöseri) är ORSAKER**, medan **NPV, IRR, PI och riskmåtten är VERKNINGAR**.
Det är kontraintuitivt och befriande: att jaga NPV är meningslöst — det är en **termometer**. Agera på hallucinationen, så
förbättras NPV, IRR och risk *tillsammans*. Dessutom postuleras inte kriteriernas **vikter**: de **härleds ur
inflytandestrukturen**, via `wᵢ ∝ √((R+C)ᵢ² + (R−C)ᵢ²)`. Dessa vikter matar de **övriga fem metoderna** — integrationsmönstret
som John (2025) beskriver.

#### 📖 2. AHP-TOPSIS 2n — *Analytic Hierarchy Process* + *Technique for Order Preference by Similarity to Ideal Solution*

**Vad det är.** **Saaty (1977)** föreslog AHP: härleda vikter ur **parvisa jämförelser** mellan kriterier, med ett
**konsistenstest** som avslöjar motsägelsefulla omdömen (`CR ≤ 0,10`). **Hwang & Yoon (1981)** föreslog TOPSIS: det bästa
alternativet är det som ligger **närmast ideallösningen** och **längst från anti-ideallösningen**.

**Hur den fungerar.** Beslutsmatrisen normaliseras, kolumnerna multipliceras med vikterna, euklidiska avstånd till ideal- och
anti-ideallösningarna beräknas, och **närhetskoefficienten** `Ci = d⁻/(d⁺+d⁻)` ordnar allt.

**Allmän användning.** Världens mest använda par inom MCDM — från leverantörsval till prestationsutvärdering.

**🔒 I detta projekt.** Vi kör TOPSIS under **två normaliseringar** — vektor (euklidisk) och min-max (linjär) — därav **"2n"**.
Varje projekt får två koefficienter och slutrankningen är medelvärdet. Vad vi vinner är ett mått som nästan ingen rapporterar:
**samstämmigheten mellan normaliseringarna**. När de två är oense om ett projekts placering är dess resultat **skört inför ett
godtyckligt tekniskt val** — och dashboarden visar det. Detta projekts Saaty-matris har `CR = 0,0119`, långt under gränsen 0,10.

#### 📖 3. ELECTRE I — *ÉLimination Et Choix Traduisant la REalité*

**Vad det är.** **Bernard Roy (1968)**, på konsultfirman SEMA i Paris. Det är nollpunkten för den europeiska
överklassningsskolan. Frågan är inte *"vilket betyg har var och en?"* utan *"är **a** minst lika bra som **b**?"*.

**Hur den fungerar.** För varje par `(a, b)` beräknas två index. **Konkordansen** `C(a,b)` summerar vikterna för de kriterier
där `a` är minst lika bra som `b`. **Diskordansen** `D(a,b)` mäter `a`:s **största nackdel** mot `b`. Man säger att `a`
**överklassar** `b` om konkordansen är hög **och** diskordansen låg. Mängden alternativ som **ingen överklassar** är **kärnan**
(*kernel*) — menyn av försvarbara val.

**Allmän användning.** Offentliga och miljömässiga beslut, där att kompensera ett katastrofalt kriterium vore oacceptabelt.

**🔒 I detta projekt.** ELECTRE är metoden som **vägrar ljuga av bekvämlighet**. Ett projekt med stratosfäriskt NPV och
skandalös hallucination **köper inte** sin plats: **diskordansen** stoppar det. Ramverket rapporterar **kärnan** — projekten
som inget annat dominerar — och använder som poäng den **netto överklassningsgraden** (hur många det dominerar, minus hur många
som dominerar det). Den är också den enda av de sex som får säga: *"dessa två projekt är helt enkelt **ojämförbara**"*.

#### 📖 4. PROMETHEE II — *Preference Ranking Organization METHod for Enrichment Evaluation*

**Vad det är.** **Jean-Pierre Brans (1982)**, förfinad med **Bernard Mareschal och Philippe Vincke (1985)**. Också
överklassning, men med en elegant vändning: i stället för en binär tröskel mäts **hur mycket** `a` föredras framför `b`.

**Hur den fungerar.** För varje kriterium passerar skillnaden `d = g(a) − g(b)` genom en **preferensfunktion** som omvandlar den
till en grad mellan 0 och 1. Brans föreslog **sex generaliserade funktioner** (vanlig, kvasikriterium, preferenströskel, nivå,
linjär med indifferens, gaussisk), parametriserade av en **indifferenströskel `q`** (under vilken skillnaden är oväsentlig) och
en **preferenströskel `p`** (över vilken preferensen är total). De viktade graderna summeras: `φ⁺` är hur mycket `a` dominerar
de andra, `φ⁻` hur mycket det domineras, och **nettoflödet** `φ = φ⁺ − φ⁻` ger en **fullständig förordning** (PROMETHEE II).

**Allmän användning.** Energi, logistik, hälsa — närhelst det är viktigt att gradera preferensens **intensitet**.

**🔒 I detta projekt.** Vi använder funktionen **linjär med indifferens**, med `q` och `p` skattade från 10 %- och 90 %-kvantilerna
av de observerade avvikelserna för varje kriterium. PROMETHEE besvarar *"hur mycket bättre är vinnaren?"*, inte bara *"är den
bättre?"*. Och det var just den som gav portföljens intressantaste fynd: i robusthetsanalysen **väljer PROMETHEE II
konsensusledaren i endast 25,4 % av preferensuniversumen** — medan de andra fyra skolorna är eniga. Konsensus **dolde en oenighet
mellan skolor**.

#### 📖 5. MAUT — *Multi-Attribute Utility Theory*

**Vad det är.** **Ralph Keeney & Howard Raiffa (1976)**, direkta arvtagare till von Neumann och Morgenstern. Det är den amerikanska
skolan i axiomatisk form: om dina preferenser lyder vissa rationalitetsaxiom, då finns en **nyttofunktion** som representerar dem,
och att besluta är att **maximera den förväntade nyttan**.

**Hur den fungerar.** Varje kriterium får en **nyttofunktion** `uⱼ` som avbildar prestation på tillfredsställelse. Den globala
nyttan är additiv: `U(a) = Σ wⱼ · uⱼ(a)` — giltig under **additivt oberoende** i preferens. Det avgörande är funktionens **form**:
ett **konkavt** `u` representerar **riskaversion** (den andra miljonen är värd mindre än den första); linjärt är neutralitet;
konvext är risksökande.

**Allmän användning.** Medicinska beslut, energipolitik, förhandling — varje sammanhang där hållningen till risk måste **göras
explicit och försvaras**.

**🔒 I detta projekt.** Vi använder **exponentiell** nytta `u(z) = (1 − e^(−r·z)) / (1 − e^(−r))` med aversionskoefficient `r = 2`.
Det är ett **deklarerat etiskt val**: ramverket är **konservativt**. En osäker vinst är värd mindre än en säker vinst med samma
väntevärde — precis som en försiktig CFO skulle bedöma den. Där TOPSIS behandlar alla vinster som utbytbara **bestraffar MAUT det
höga, osäkra löftet**.

#### 📖 6. MCDA-C — *Flerkriteriellt beslutsstöd — konstruktivistiskt*

**Vad det är.** Formaliserat av **Leonardo Ensslin, Gilberto Montibeller och Sandra Noronha (2001)**, med rötter hos Roy och Bana e
Costa. Premissen är filosofisk: modellen **föregår inte** beslutsfattaren. Den **byggs med honom**, i tre faser —
**strukturering** (kognitiva kartor, deskriptorer), **utvärdering** (värdefunktioner, substitutionstakter) och **rekommendationer**.

**Hur den fungerar.** Varje kriterium får en **deskriptor** med nivåer, varav två är ankare: nivån **Neutral** (under vilken
prestationen äventyrar) och nivån **Bra** (över vilken det råder excellens). Värdefunktionen är förankrad: `V = 0` vid Neutral,
`V = 100` vid Bra, och den **extrapolerar** fritt utanför intervallet.

**Allmän användning.** Utvärdering av organisatorisk prestation, offentlig förvaltning, sammanhang där beslutsfattaren måste
**lära sig** om sitt eget problem.

**🔒 I detta projekt.** I avsaknad av en struktureringssession med beslutsfattaren förankrar vi nivåerna i portföljens
**observerade kvartiler**: `Neutral = Q1`, `Bra = Q3`. Detta bevarar det unika med MCDA-C — den **ordnar** inte bara, den
**klassificerar**: `V < 0` är **äventyrande**, `0 ≤ V ≤ 100` är **konkurrenskraftig**, `V > 100` är **excellens**. Ett projekt kan
toppa rankningen och ändå ligga i det äventyrande bandet. Ingen annan metod i denna uppsättning skulle berätta det för dig.

#### 📖 Varför fem metoder, och inte en

Därför att **varje skola misslyckas på sitt eget sätt**, och en ensam metod returnerar en vinnare med **implicit 100 % säkerhet** —
vilket alltid är en lögn. AHP-TOPSIS överkompenserar; ELECTRE vägrar ibland avgöra; MAUT beror på nyttans form; MCDA-C på ankarna.

Vi kör alla fem med **samma vikter** (DEMATEL:s) och avslutar med **Borda-konsensus**. Då upphör oenigheten mellan dem att vara en
olägenhet och blir **information**: när fyra är eniga och en avviker rakt av är det inte brus — det är varningen att ditt val
**beror på den beslutsskola** du implicit antagit.

#### 📖 Den sista frågan: överlever domen?

Hela byggnaden ovan vilar på **vikter**, och vikter är **skattningar**. Om två procentenheter på IITA-vikten byter plats på 1:a och
2:a, är "vinnaren" en **artefakt av kalibreringen**, inte ett faktum om portföljen.

Därför stör vi DEMATEL-vikterna med en **Dirichlet** — `w' ~ Dir(κ·w)`, som lever exakt på simplexet och bevarar `E[w'] = w`,
alltså stör **utan att snedvrida** — och rangordnar om **2 000 gånger**. Domen byter natur:

> *"Project C är bäst"* ⟶ **"Project C vinner i 99,9 % av de rimliga preferensuniversumen"**

Det är ett **konfidensintervall för själva beslutet**. Med det slutar ramverket mäta enbart risken i **pengarna** och börjar mäta
risken i **beslutet**.


**Vad det är och vad det är till för.** När du väljer mellan projekt **står kriterierna i konflikt** (högt NPV kommer
oftast med hög risk) och är **inkommensurabla** (hur adderar man kronor med hallucinationsprocent?). MCDA är fältet
som gör det valet explicit, granskningsbart och försvarbart. Dess grundtes är obekväm och befriande: **det finns inget
"bäst" i ett vakuum.** Det finns ett bäst *givet ett preferenssystem som du gjort explicit*. Att byta implicit åsikt
mot en explicit modell — där ligger hela vinsten.

**De tre skolorna.** Den **amerikanska**, om värde och nytta (AHP, MAUT): aggregerar allt till ett enda tal. Den
**europeiska**, om överklassning (ELECTRE, PROMETHEE), från Bernard Roy: accepterar att två alternativ kan vara
**ojämförbara** och tillåter **veto** — ett uselt betyg på ett kriterium köps inte loss av toppbetyg på andra. Den
**konstruktivistiska** (MCDA-C): modellen upptäcks inte, den **byggs tillsammans med beslutsfattaren**.

| Metod | Ursprung | Central fråga | Vad bara den ger | I AI-portföljen |
|---|---|---|---|---|
| **DEMATEL** | Gabus & Fontela, Battelle (1972-73) | *"Vem påverkar vem?"* | skiljer **orsak** från **verkan** och härleder **vikterna** ur själva inflytandestrukturen | visar att minska hallucination (IITA) är en **orsak** — agera där, så förbättras NPV, IRR och risk tillsammans |
| **AHP-TOPSIS 2n** | Saaty (1977) · Hwang & Yoon (1981) | *"Vem är närmast ideallösningen?"* | vikter via parvisa jämförelser med **konsistenstest** (CR ≤ 0,10) | rangordnar under **två normaliseringar** och rapporterar samstämmigheten |
| **ELECTRE I** | Bernard Roy (1968) | *"Vem överklassar vem — och vem överlever odominerad?"* | **ojämförbarhet** och **veto**: ett uselt kriterium köps inte loss | isolerar **kärnan** av projekt som inget annat dominerar |
| **PROMETHEE II** | Brans & Vincke (1985) | *"Vad är nettopreferensflödet?"* | **sex preferensfunktioner** med indifferens- och preferenströsklar | graderar *hur mycket* bättre ett projekt är, inte bara *om* det är det |
| **MAUT** | Keeney & Raiffa (1976) | *"Vad maximerar beslutsfattarens nytta?"* | modellerar **riskaversion** genom konkav nytta | bestraffar osäkra vinster — en försiktig beslutsfattare betalar inte lika mycket för dem |
| **MCDA-C** | Ensslin, Montibeller & Noronha (2001) | *"Var ligger nivån Bra, och var Neutral?"* | **förankrad värdefunktion**: `V=0` vid Neutral, `V=100` vid Bra, med extrapolering | klassificerar i **äventyrande / konkurrenskraftig / excellens** i stället för att bara ordna |

**Varför fem, och inte en.** Varje skola misslyckas på sitt eget sätt. En ensam metod returnerar en vinnare med
**implicit 100 % säkerhet** — alltid en lögn. Kör man alla fem och avslutar med **Borda-konsensus** blir oenigheten
mellan dem **information**: när fyra är eniga och en avviker rakt av är det inte brus — det är varningen att ditt val
beror på om du föredrar *överklassning* framför *nytta*. Och **Dirichlet-störningen** av vikterna besvarar den sista
frågan: *"överlever förstaplatsen ett fel på två procentenheter i kalibreringen?"*


### 🧪 De fyra kugghjulen: Iman-Conover, Kolmogorov-Smirnov, Dirichlet och tornadon

De två stora metoderna ovan vilar på fyra mindre delar — och det är i dem skillnaden bor mellan en ärlig simulering och en
vacker siffra. De är värda att känna till.

#### 🔗 Iman-Conover — att påtvinga korrelation **utan att förstöra fördelningarna**

**Vad det är.** Föreslogs av **Ronald Iman och William Conover (1982)**. Det löser ett problem som ser trivialt ut och inte är
det: *hur drar man korrelerade variabler när marginalfördelningarna inte är normala?* Den naiva vägen — generera korrelerade
normalfördelningar via Cholesky och transformera dem — **deformerar marginalerna**. Och har du just anpassat en LogNormal till
dina data kastar deformationen bort precis det arbete du gjort.

**Hur det fungerar.** Det är en **omordning efter rang**, inte en värdetransformation. En referens byggs av **van der
Waerden-poängen** `Φ⁻¹(i/(n+1))`, blandade kolumnvis; man beräknar `P = chol(R)` (målet) och `Q = chol(corr(M))` (referensens
oavsiktliga korrelation); man bildar `S = M·(Q⁻¹P)ᵀ`. Sedan **omordnas varje kolumn i det ursprungliga stickprovet efter rangen
i `S`**. Eftersom endast *ordningen* på redan dragna värden ändras förblir **marginalfördelningarna exakta** — bit för bit.

**En fin och ärlig detalj.** `R` är korrelationen hos den *normala referensen*, inte resultatets Pearsonkorrelation. Den
inducerade rangkorrelationen följer normalkopulan: `ρ_S = (6/π)·arcsin(R/2)`. För `R = 0,80` ger det **0,7859** — exakt vad vi
mätte vid test (0,786). Det är inget fel i metoden; det är dess matematik.

**Allmän användning.** Finansiell risk (korrelerade tillgångar), strukturell tillförlitlighet, latinsk hyperkubsampling.

**🔒 I detta projekt.** Det är detta som låter oss korrelera kassaflödena **utan att offra** den fördelning som anpassats till
dina tokens. Före användning valideras matrisen: symmetrisk, enhetsdiagonal och **positivt definit** (via Cholesky). En
inkonsekvent korrelationsmatris avvisas med det minsta egenvärdet rapporterat — i stället för att tyst producera meningslösa tal.

#### 📏 Kolmogorov-Smirnov — avståndet mellan vad du **antar** och vad data **säger**

**Vad det är.** Ett **icke-parametriskt** anpassningstest. Statistikan är enkel och vacker: `D = sup |Fₙ(x) − F(x)|`, det största
vertikala avståndet mellan dina datas **empiriska fördelningsfunktion** och den **teoretiska** du föreslog. Under nollhypotesen
**beror `D`:s fördelning inte på vilket `F` det är** — därav *distribution-free*.

**En metodologisk ärlighetsreservation.** Det klassiska KS p-värdet förutsätter att parametrarna i `F` fixerades **innan** man såg
data. När de **skattas ur samma data** (som här, med maximum likelihood) blir testet **optimistiskt**: det accepterar för lätt.
Stringens skulle kräva **Lilliefors**-korrektionen eller en **parametrisk bootstrap**. Därför behandlar vi KS som en **diagnos**,
inte ett bevis — och använder det bara för att **förkasta** dåliga anpassningar, aldrig för att förklara en anpassning "riktig".

**Allmän användning.** Anpassningsgrad; jämförelse av två stickprov (två-stickprovs-KS); upptäckt av data-*drift* i
maskininlärningssystem i produktion.

**🔒 I detta projekt.** Det mäter hur väl den AIC-vinnande fördelningen faktiskt beskriver din tokenserie. När p-värdet faller
under 0,05 skriver skärmen **`SVAG ANPASSNING` i rött** — i demoportföljen inträffar det för ett av projekten, och ramverket
**visar** det i stället för att dölja. En ärlig siffra slår en vacker.

#### 🎲 Dirichlet-störning — beslutets **konfidensintervall**

**Vad det är.** **Dirichlet**-fördelningen är den naturliga fördelningen på **simplexet**: vektorer av positiva tal som summerar
till 1 — precis vad en viktvektor är. Den är multinomialfördelningens konjugat och Betafördelningens generalisering.

**Varför den, och inte gaussiskt brus.** Att addera normalbrus till vikter ger negativa värden och bryter enhetssumman.
Dirichlet lever *inuti* det giltiga rummet. Och parametriserad som `w' ~ Dir(κ·w)` har den två egenskaper som gör den perfekt:
`E[w'] = w` (den stör **utan att snedvrida**) och `Var(w'ᵢ) = wᵢ(1−wᵢ)/(κ+1)` (spridningen styrs med ett enda vred). När
`κ → ∞` kollapsar den på de ursprungliga vikterna.

**Allmän användning.** Bayesiansk *prior* för proportioner; Latent Dirichlet Allocation (**LDA**) i ämnesmodellering; Rubins
**bayesianska bootstrap** (1981); och viktkänslighetsanalys i flerkriteriebeslut.

**🔒 I detta projekt.** Med `κ = 200` svänger en vikt på 13 % med ungefär **±2,37 procentenheter** — den rimliga felmarginalen i
ett expertomdöme. Vi rangordnar om **2 000 gånger** och får `P(vinst)` för varje projekt. Det var detta kugghjul som avslöjade
portföljens obekvämaste fynd: konsensus är robust (99,9 %), men **PROMETHEE II väljer ledaren i endast 25,4 % av universumen**.
Utan Dirichlet skulle den oenigheten förbli osynlig.

#### 🌪️ Känslighetstornado — vilken variabel som **verkligen** rör resultatet

**Vad det är.** Ett liggande stapeldiagram, sorterat efter absolut effekt, som besvarar: *bland alla osäkra indata, vilka rör
utfallet?* Namnet kommer av formen — breda staplar överst, smala nederst.

**Två mått som ser lika ut och inte är det.**
- **Betat** i en multipel regression svarar: *"om detta indata ökar med 1 enhet, hur mycket ökar utfallet?"* Det är en
  **enhets**effekt, likgiltig för hur mycket det indatat faktiskt varierar.
- **Pearsonkorrelationen** svarar: *"hur mycket av utfallets osäkerhet styrs av detta indata?"* Den bär redan med sig
  **osäkerhetens skala** (ungefär `β·σᵢ/σ_y`).

En variabel kan ha ett enormt beta och noll korrelation: den *skulle* röra resultatet mycket, men i praktiken **varierar den
knappt**. Att rapportera bara ett av de två är en halv sanning.

**Allmän användning.** Projektrisk, finansiella modeller, tillförlitlighetsteknik, simulatorkalibrering.

**🔒 I detta projekt.** Här gjorde tornadon något ovanligt: den **avslöjade en begränsning i modellen själv**. Körd mot NPV kom
betana ut **exakt lika med `1/(1+i)ᵗ`** — diskonteringsfaktorerna — eftersom NPV är *linjärt* i flödena. Regressionstornadon är i
det fallet **degenererad**: den säger inget utöver räntan. Det är **korrelationen** som bär signalen. Och när tokenkostnaden kom in
som variabel blev dess beta `−1/(1+i)ᵗ` (kostnaden går in med minustecken) och dess korrelation nära noll. Lästa tillsammans är
utsagan precis och ärlig: *"varje extra enhet i tokens tar 0,91 från NPV — men i detta projekt kommer NPV:s osäkerhet inte från
tokens."* Inget av måtten ensamt skulle säga det.

---

<!-- budget-global-section -->

## 💰 Global tokenbudget — varje projekt är ett KOSTNADSSTÄLLE

**Det finns EN budget: den för planen du abonnerar på.** Allt annat **rinner ur den**. Varje projekt är ett **kostnadsställe** — det har **ingen egen budget**. Dess tilldelning är en **skiva av den globala budgeten**, och den skivan **räknas om automatiskt** varje gång ett projekt tillkommer eller lämnar portföljen. **Inget skapas; allt fördelas.**

> **Den strukturella buggen detta rättade.** Varje projekts tokenbudget var `förbrukning × 1,10` — exakt 1,100 för **alla tio**. Cirkulär. Självrättfärdigande. **Inget projekt kunde spränga sin budget, per konstruktion.** *En budget som härleds ur den egna utgiften är ingen budget: det är ett kvitto.* Idag, med kvoten från den verkliga poolen, **spränger 6 av 10 projekt den**.

```text
   ASSINATURA DO PLANO / PLAN SUBSCRIPTION
              │
              ▼
   💰 BUDGET GLOBAL  ─────────  a quota mensal contratada. É FINITA.
              │
              ├── piso igualitário (50%)
              └── por VALOR entregue (50%)
              │
              ▼
   🏷️ CENTRO DE CUSTO 1 … N  ──  a cota de CADA projeto
```

### 🍩 Koncept — poolen är DELAD och ÄNDLIG

**Koncept.** Langfuse, CloudZero, Vantage och de andra ger **kostnad per projekt**, som om vart och ett hade sin egen kran. **Det har det inte.** Det finns **en tecknad plan** med ändlig månadskvot, och **varje token ett projekt bränner är en token ett annat inte får**. Det är **allmänningens tragedi** tillämpad på AI-budgeten.

**Metodik.** Den globala budgeten kommer från avtalet: `platser × US$ × växelkurs × (1+IOF)` plus fast infra, vilket ger **månatlig TCO** och **kostnad per miljon tokens**. Verklig förbrukning kommer från loggarna, projicerad till en **månatlig run-rate**. Därur faller **kvotutnyttjande**, **marginal** och **poolens uttömningsdatum**.

**Tillämpning — och siffran som gör ont.** **31 % av förbrukningen är SLÖSERI**: 29 miljoner tokens/månad brända på anrop som **misslyckades och gav ingenting tillbaka** (hallucination, rate-limit). Det är **4,7× hela din avtalsmarginal**. Rakt ut: **du skulle knuffas till en större plan på grund av anrop som aldrig levererade ett svar.** Att skära bort hälften av slöseriet frigör mer kapacitet än hela marginalen — **utan att spendera en krona till**.

![Global budget per projekt (Burn Token Rate) — varje skiva är inte 'dess kostnad': det är kapaciteten den tar från de andra](docs/screenshots/budget-donut-burn-token.png)

### ⚖️ Adaptiv fördelning och KORSSUBVENTION — vem betalar för vem

**Koncept.** Att fördela **efter förbrukning** är marknadsstandard, och det är **självrättfärdigande**: den som bränner mest får störst kvot, vilket **legitimerar slöseriet**. Den ärliga fördelningen sker efter **levererat värde (EV)**.

**Metodik.** Varje kostnadsställes kvot är `lika golv (50 %) + levererat värde (50 %)`, **omdimensionerad så fort N ändras** — ett nytt projekt har EV = 0 och skulle utan golvet få **noll tokens** och aldrig kunna producera värde. **Korssubventionen** är skillnaden mellan kvoten det skulle få för vad det **förbrukar** och den för vad det **levererar**. Summan av subventionerna är **exakt noll**: det är en överföring, inte värdeskapande.

**Tillämpning.** Effektivitetsspannet är **68×**: Project F levererar **642** i värde per miljon tokens; Project J, **10**. Och fördelningen avslöjar notan: **R$ 3 431/månad — 40 % av TCO — överförs från de effektiva till de ineffektiva, varje månad, i mörkret.** Project F, portföljens billigaste, **betalar Project J:s nota**.

![Korssubvention — den som förbrukar mer än den levererar subventioneras; den som levererar mer än den förbrukar betalar de andras nota](docs/screenshots/budget-subsidio-cruzado.png)

### 🔒 PRISSATT resurskonkurrens — kausalkedjan tillämpad på PORTFÖLJEN

**Koncept.** Kausalkedjan binder, **inuti** ett projekt: `token som driftat → risk → tid (P80) → pengar`. Detta binder **MELLAN** projekt: `ett projekts överuttag → poolen töms → de ANDRA stryps → DERAS P80 glider → DERAS Cost of Delay skickar notan`.

**Metodik.** Det kräver **samtidigt** FinOps (kvoten), EVM (levererat värde), risk (exponering) och ett simulerat schema (P80). Det är därför **inget verktyg på marknaden gör det** — inget har de fyra motorerna tillsammans. Langfuse ser token. Jira ser uppgiften. CloudZero ser fakturan. **Inget av dem kan säga att projekt J kostar projekt F R$ X i försening.**

**Tillämpning — och ärligheten som bär siffran.** I strypningsscenariot **orsakar Project J R$ 3 730 i skada på de andra och lider bara R$ 853** — saldo +2 877: det är **FÖRÖVAREN**. **Project C, 30× effektivare, lider R$ 867 och orsakar inget** — det är ett **OFFER**. Saldona summerar till **noll**: varje förövare har ett offer.

> ⚠️ **Men idag RYMS poolen** (94 % av kvoten). **Det finns ingen fysisk strypning** — ingen stannar, ingen glider. Skadan är **allokativ**, inte **operativ**. Att säga *"J försenar C"* medan poolen har marginal vore **en lögn klädd i stringens**. Därför är modulen **scenariobaserad** och **märkt som prognos**: den visar *från vilken punkt* poolen vänder (+10 % förbrukning → hela portföljen stannar 0,9 dagar, R$ 1 497) och *vad det kostar när den vänder*.

![Prissatt resurskonkurrens — vem orsakar skadan och vem betalar den; när poolen sinar stannar ALLA, även de effektiva som inte orsakade något](docs/screenshots/budget-contencao.png)

### 🪓 Skärpolitik — om portföljen behöver plats, VEM lämnar?

**Koncept.** Detta är frågan portföljkommittén **aldrig kan besvara**. I en ändlig pool tar det att släppa in projekt N+1 **tokens från alla N som redan var där** — att släppa in ett projekt **späder ut alla med 9,1 %**.

**Metodik.** Det ärliga svaret är **inte "den som spenderar mest"** — att skära efter rå förbrukning skulle straffa ett **stort och produktivt** projekt. Svaret är **"den som levererar minst PER TOKEN"**: sortering efter **effektivitet** (EV ÷ miljon tokens) frigör mest pool till **lägsta värdekostnad**. Diagonalen `y = x` skiljer skäret som **lönar sig** från det som **förstör mer än det frigör**.

**Tillämpning.** Att skära **Project J** frigör **20,5 % av poolen** och offrar **1,9 % av värdet** — det öppnar nästan 2 nya platser utan att späda ut någon. Att skära **Project F** skulle frigöra 3,4 % och offra **21,2 % av värdet**: det skulle **förstöra mer värde än det frigör kapacitet**. **Detta är inte "skär kostnader" — det är en explicit avvägning, med siffror.**

![Skärpolitik — % av poolen som frigörs mot % av värdet som offras; diagonalen skiljer det lönsamma skäret från det förstörande](docs/screenshots/budget-politica-corte.png)

---
<!-- pm-agent-section -->

## 🤖 Project Manager Agent — läser 10 dimensioner, lär sig och **vet när den ska tiga**

Dashboarden **diagnostiserar**. Kausalkedjan **kvantifierar**. Agenten **beslutar vad som ska göras nu** — och lär sig, cykel efter cykel, vilken spak som faktiskt rör nålen *i just det projektet*. Den sveper över **10 dimensioner** (tid, ROI, risk, tokens, kostnad, modelldrift, tillförlitlighet, kvalitet, flöde och slöseri), omvandlar var och en till **ekvivalenta projektdagar × just det projektets fördröjningskostnad**, och svarar på den enda fråga som betyder något: **vad ska göras nu, och vad är det värt.**

> **Svagheten vi måste rätta till.** Agenten rekommenderade **alltid** något: varje cykel tog den den största skadan och skrek. **En agent som skriker varje vecka blir brus, och brus ignoreras** — den ändrar alltså ingenting, hur rätt den än har. **Den saknade rätten att tiga.** Det är precis vad de tre metoderna nedan levererar.

### 🚦 PRINCE2 — *management by exception*: rätten att tiga

**Koncept.** PRINCE2:s *management by exception* säger att chefen **inte ska störas** så länge projektet håller sig inom överenskomna toleranser. När **prognosen** spräcker toleransen — inte utfallet, **prognosen** — utlöses en **Exception Report**.

**Metodik.** En tolerans per dimension (tid, kostnad, risk, kvalitet, nytta). Eskalering drivs av **prognosen**: Monte Carlos P80 och EVM:s EAC. Exception Report har fyra obligatoriska delar — **orsak, påverkan, ALTERNATIV och rekommendation**. Det är raden med *alternativ* som skiljer en avvikelserapport från ett larm: att eskalera utan att erbjuda alternativ är att skjuta problemet uppåt, inte att leda.

**Tillämpning här.** Toleranserna är **inga siffror vi hittat på** — de kommer från vad projektet **redan deklarerat**: det utlovade datumet (`prazo_alvo`), den godkända budgeten (`BAC`), det **egna riskregistrets** klassificering (`nivel='critico'`) och **projektets egen kvalitetsbaslinje** (regression mot sig själv, i DORA-anda). Endast ROI-gränsen är uttalad policy — och den ligger synlig, så att styrelsen kan invända. Alternativen agenten erbjuder är **absorbera** (bränna ledningsreserven), **återhämta** (komprimera kritiska linjen) eller **omförhandla** (flytta datumet eller skära i omfattning).

![PRINCE2-toleranser — varje dimensions marginal till avvikelse; endast Kvalitet spräckte, och endast den eskaleras](docs/screenshots/prince2-tolerancias.png)

### 🌡️ CCPM (Goldratt) — *buffer management* och feberdiagrammet

**Koncept.** I Goldratts *Critical Chain* är bufferten inte fett gömt i varje uppgift: den är en **explicit kudde i projektets slut**. **Feberdiagrammet** korsar *hur mycket av kedjan som är klar* med *hur mycket buffert som förbrukats*, och säger i vilken av tre zoner du befinner dig.

**Metodik.** Gränserna är **diagonala**, och det är metodens kärna: att bränna buffert **i slutet** är normalt — att bränna den **i början** är allvarligt, eftersom ett helt projekt återstår. **GRÖN = gör ingenting. GUL = planera återhämtningen. RÖD = agera nu.**

```
verde/amarelo:    y = 1/3 + (1/3)·x
amarelo/vermelho: y = 2/3 + (1/3)·x
```

**Tillämpning här.** Bufferten är `P80 − P50` från **Monte Carlo-schemat** vi redan körde. Förbrukningen är **Earned Schedule-förseningen** omräknad till dagar. Och det är feberdiagrammet som ger agenten en objektiv trigger för tystnad: **grön zon plus inom tolerans = inget att eskalera.** Idag får **3 av 10 projekt** exakt det — och det är genom att tiga när det inte finns något att säga som agenten förtjänar rätten att bli hörd när det finns.

![CCPM-feberdiagram — de 10 projekten i de tre zonerna; de diagonala gränserna gör samma bufferförbrukning ofarlig i slutet och allvarlig i början](docs/screenshots/ccpm-fever-chart.png)

### 🏦 PMI — *reserve analysis*: kontingens × ledningsreserv

**Koncept.** PMI skiljer två reserver som nästan alla blandar ihop: **kontingensen** täcker *kända okända* (variabiliteten du **mätt**), och **ledningsreserven** täcker *okända okända* (chocken).

**Metodik.** `kontingens = P80 − P50` och `ledningsreserv = P95 − P80`. Plus jämförelsen nästan ingen gör: kontingensen du **har** mot den ditt **riskregister rättfärdigar** (EMV — *Integrated Cost-Schedule Risk Analysis*, Hulett). En varaktighetsbuffert är **blind för riskhändelser**; det är där nästan varje schema upptäcker att det var optimistiskt.

**Tillämpning här — och en läxa i ärlighet.** Att omvandla ”påverkan 4” (skala 1–5) till dagar kräver en mappning som är **vår, inte din**. Så vi **stresstestade vårt eget antagande**: halvera den antagna påverkan och slutsatsen ”underreserverad” vänder från **10/10 till 1/10 projekt**. Det är en **knivsegg**, och därför **säljs den inte som ett fynd** — varje projekt bär fältet `robusto`, och agenten **varnar när dess egen tolkning inte överlever stresstestet**. Det som **återstår helt utan antaganden** är ren aritmetik, och det är det verkliga fyndet: **bufferten är ~9 % av kedjan, mot de 25–50 % som CCPM arbetar med.**

### 🏃 Sprintar och fredagens weekly-debatt

**Koncept.** Fredagens *weekly*-debatt om framsteg behöver **siffror**, inte åsikter. Åsikter flyttar inga projekt.

**Metodik.** Tre mått öppnar diskussionen. **(1) Say-do-kvot** (`ΔEV ÷ ΔPV`): ett team på 0,7 är **inte långsamt** — det *lovar 30 % mer än det kan leverera*. Kapacitet lagas inte med press; åtaganden lagas med förutsägbarhet. Och say-do **långt över 1** är inte heller hjältemod: det är en **trasig baslinje**. **(2) Sprintens lokala CPI**, avskild från den kumulativa **med avsikt** — den kumulativa är ett medelvärde, och medelvärden **döljer** den senaste dåliga sprinten: ett kumulativt CPI på 1,05 kan hysa en sista sprint på 0,60. **Den lokala anklagar; den kumulativa tröstar.** **(3) Velocity-baserad prognos**: om teamet behöver 6 sprintar och bara 4 återstår är **datumet redan dött** — och ingen märkte det, eftersom det kumulativa burndownet fortfarande *ser ut* att ligga nära plan.

**Tillämpning här.** Sprinten är **inte påhittad**: den är **EVM-perioden**, kadensen projektet redan har, med verkliga PV/EV/AC. Att bygga en sprintkalender parallellt med schemat vore att skapa en **andra sanning** om samma projekt — och två sanningar är detsamma som ingen.

> **⚠️ Efterlevnad, sagt rakt ut.** Detta är en **kadensbaserad framstegsrapport byggd på EVM (ANSI/EIA-748) med agilt inspirerade mått** — **det är inte Scrum**. *Scrum Guide 2020* innehåller **varken** ”velocity” **eller** ”burndown chart” (de är marknadspraxis, inte officiella artefakter), och den ersatte Sprint Backlogens *commitment* med **Sprint Goal**, och behandlar backloggen som en **prognos**. Alltså är ”say-do-kvot (levererat ÷ åtagit)” **industrins** vokabulär, inte kanonisk Scrum. **Måttet är ärligt; det är etiketten som skulle ljuga.**

![Sprintar — say-do-kvot per sprint och det verkliga burndownet mot plan; kadensen är EVM-perioden](docs/screenshots/sprints-weekly.png)

### 🎯 Radarn och omlärningsmotorn — varför denna dimension och inte en annan

Agenten **tittar inte bara på vinnaren** — den visar hela bänken. Varje dimension blir **ekvivalenta dagar**, dagarna blir **pengar** via *det* projektets fördröjningskostnad, och vikten är vad agenten **lärt sig där**. Prioritet är `skada × vikt`.

**Omlärningsmotorn** är en *kontextuell bandit* — enkel och granskbar, och vi säger det rakt ut: **detta är inte deep learning**. Varje cykel rekommenderar agenten en spak och **sparar dess målmått**; nästa cykel **håller den sig själv ansvarig**. Förbättrades → vikten **stiger**. Försämrades → den **faller**. Rörelse under 2 % är brus, och **agenten lär sig inte av brus**. Endast spaken den **rekommenderade** bedöms: den svarar för vad den bad om och **tar inte åt sig äran för vad slumpen förbättrade**. Resultatet är en profil som **inte passar grannprojektet** — och det är precis poängen.

![Radar över de 10 dimensionerna — varje dimensions skada på samma linjal (R$), och den agenten valde att angripa](docs/screenshots/pm-agent-radar.png)

---
## 🌐 12 språk

Dashboarden, projektsidorna **och texten inuti diagrambilderna** är lokaliserade på **12 språk**:
Português · English · Español · Français · Deutsch · 中文 · 한국어 · हिन्दी · עברית · Svenska · Русский · Suomi.
Översättningen drivs av ett **Translation Memory** (SDL Trados-stil) som standardiserar och snabbar upp nya språk.

---

## 🙋 Invändningar (frågorna du ställer dig just nu)

- **"Jag har inte tid."** → Fem minuter med `./run_all.sh --mock` och dashboarden körs på din skärm. Att mäta **ger
  tillbaka** de timmar du redan förlorar på omarbete och hallucination.
- **"Det är för komplext."** → En rad. Ramverket gör ETL, beräkningar, rangordning och bilder; **du läser bara domen.**
- **"Min AI-verksamhet är liten."** → Just därför väger varje dollar mer. Litet idag, portfölj imorgon — **mät innan
  du skalar slöseriet.**
- **"Jag använder inte Langfuse."** → Demon körs **100 % utan Langfuse**. När du vill ha verklig data kopplar du in
  **ditt** konto (aldrig mitt).
- **"Det är bara ännu en snygg dashboard."** → Nej. Det är **Balanced Scorecard + investeringsanalys
  (NPV/IRR/MIRR/EAA) + flerkriteriebeslut (AHP-TOPSIS)** — styrelseinstrument, inte dekoration.
- **"Vad händer med min datasekretess?"** → Demon är **100 % anonym** (Project A…J); verklig data/verkliga namn och
  nycklar stannar **utanför paketet**. Du kör **lokalt**, med **ditt** konto.
- **"Vad kostar det?"** → **Ingenting.** Öppen källkod, på din maskin. Det enda priset är att fortsätta att **inte
  mäta** — och det priset betalar du redan.

---

## 🧩 Medföljande Skills (*build & analyze your own*)

Detta repo levererar återanvändbara **Skills** (Claude Code):

- **`measuring-ai-projects`** — definiera/mäta/rapportera KPI:er för AI-projekt (kärnan i detta ramverk).
- **`github-benchmark-analyzer`** — analysera och benchmarka **vilket som helst** GitHub-repo/-profil (stjärnor,
  forkar, följare, hashtaggar, README-stil, nyckelord, språk) och extrahera vad ledarna har gemensamt. **Bygg och
  analysera din egen portfölj** — även mot marknaden.

---

## 📚 Resurser & referenser (Awesome)

Jättarnas axlar detta ramverk står på:

- **Strategi & mätning:** Kaplan & Norton — *The Balanced Scorecard* · Peter Drucker (målstyrning).
- **Lean Six Sigma:** taxonomin över de 8 slöserierna (Muda), PDCA/Kaizen, Ishikawa/RCA.
- **Företagsfinans:** Lawrence Gitman — *Principles of Managerial Finance* (NPV, IRR, MIRR, PI).
- **Flerkriteriebeslut:** Thomas Saaty (**AHP**) · Hwang & Yoon (**TOPSIS**).
- **Teknisk stack:** [Langfuse](https://langfuse.com) (LLM observability) · [Evidence](https://evidence.dev)
  (BI as Code) · [Rust/PyO3](https://pyo3.rs) · [Tectonic](https://tectonic-typesetting.github.io) (LaTeX).

---

## 🗺️ Färdplan

- [x] Pipeline Langfuse → SQLite → Evidence + Rust
- [x] 70+ KPI:er (BSC + API-ekonomi + Lean) · EVM
- [x] Finansiellt (NPV, IRR, MIRR, EAA, PI, återbetalningstid, dollarisering)
- [x] AHP-TOPSIS 2n + administrativt dossier (6 verktyg)
- [x] Dashboard och bilder på **12 språk**
- [ ] Fler observerbarhetskopplingar (OpenTelemetry, Helicone)
- [ ] Fleranvändar-SaaS-läge + inbyggd schemaläggning
- [ ] Publicering av statisk dashboard (GitHub Pages)

---

## 🧰 Steg-för-steg-installation (lokalt, från noll)

> Allt körs **på din maskin**. Inga författarnycklar följer med paketet och ingen data lämnar din dator.

### Steg 0 — Förutsättningar

| Krav | Version | Obligatoriskt? | Till vad |
|---|---|---|---|
| **Python** | 3.10+ | ✅ | pipeline, KPI:er, Monte Carlo, MCDM |
| **Node.js + npm** | 18+ | ✅ | dashboard (Evidence) |
| **git** | valfri | ✅ | klona repot |
| **Rust + maturin** | stabil | ⬜ valfritt | snabbar upp loggklassificering |
| **tectonic** | valfri | ⬜ valfritt | bygger PDF-pitch-decks |

*På Windows, använd **WSL** eller **Git Bash** — pipelinen är ett `bash`-skript.*

### Steg 1 — Klona repot
```bash
git clone https://github.com/bpenedo/Gestao-de-Projetos-PM-IA-BSC-DashBoard.git
cd Gestao-de-Projetos-PM-IA-BSC-DashBoard
```

### Steg 2 — Isolerad Python-miljö
```bash
cd foundations/pipeline
python3 -m venv .venv
source .venv/bin/activate        # Windows (PowerShell): .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Steg 3 — Dashboardens beroenden
```bash
cd ../evidence
npm install
```

### Steg 4 — Kör demon (anonym, utan uppgifter)
```bash
cd ../pipeline
./run_all.sh --mock
```

I tur och ordning: anonym demodata → KPI:er → NPV/IRR/MIRR/EAA/PI → **fördelningsanpassning till tokens** →
**Monte Carlo (10 000 iterationer)** → AHP-TOPSIS 2n → **DEMATEL · ELECTRE · PROMETHEE · MAUT · MCDA-C** →
**rangordningens robusthet (Dirichlet)** → grafer → administrativt dossier → 5D-karta → pitch decks → dashboardbygge.

### Steg 5 — Öppna dashboarden
```bash
cd ../evidence
npm run dev          # http://localhost:3000
npm run preview      # (alternativa) serve o estático já compilado em build/
```

### Steg 6 — Byt till DINA data

**6.1 — Uppgifter och parametrar** (alla valfria; utan `.env` används standardvärdena):
```bash
cd ../pipeline
cp .env.example .env      # edite: LANGFUSE_PUBLIC_KEY, LANGFUSE_SECRET_KEY, SELIC_ANUAL, USD_BRL...
```

**6.2 — Ditt kassaflöde** (det matar NPV, IRR och Monte Carlo):
```bash
cp fluxo_caixa_template.csv fluxo_caixa.csv
```
Format: `periodo 0` är investeringen (negativt flöde) och `taxa` är diskonteringsräntan per period (`0.10` = 10 %).
```csv
project_name,periodo,fluxo,taxa
Project A,0,-12000,0.10
Project A,1,3000,0.10
Project A,2,4000,0.10
```

**6.3 — Kör med verklig data:**
```bash
./run_all.sh          # sem --mock: sincroniza do Langfuse e usa fluxo_caixa.csv
```

### Steg 7 (valfritt) — Acceleration och PDF
```bash
cd analise_rs && maturin develop --release && cd ..   # Rust (PyO3): classificação mais rápida
```
För pitch-decks, installera **tectonic** (t.ex. `cargo install tectonic` eller din distros pakethanterare).

### Steg 8 (valfritt) — Schemalägg uppdateringen
```bash
crontab -e
*/15 * * * * /CAMINHO/ABSOLUTO/foundations/pipeline/run_all.sh >> /tmp/bsc.log 2>&1
```

### 🩺 Vanliga problem

| Symptom | Trolig orsak | Lösning |
|---|---|---|
| `no such table: ...` | databasen inte initierad | `python3 db.py` |
| Dashboardbygget misslyckas | gamla artefakter | `rm -rf ../evidence/build && npm run build` |
| `findfont: Failed to find font weight` | matplotlib-varning | ofarlig, ignorera |
| `Precisa de ≥2 projetos` | portfölj med bara ett projekt | MCDM jämför alternativ; lägg till ett till |
| `KS p-värde < 0,05` på skärmen | fördelningen beskriver inte dina data väl | samla fler observationer; ramverket varnar i stället för att dölja |
| Siffrorna ändras mellan körningar | fröet ändrades | håll `MC_SEED` fast för reproducerbarhet |

---

## 🤝 Bidra

Bidrag är **mycket välkomna**! Öppna en *issue* som beskriver ditt förslag (ny KPI, koppling, språk, rättelse) och
skicka en *pull request*. Standarder: läsbar kod i linje med omgivningen, ingen personlig data i paketet (demon är
anonym). Nya språk: lägg till målen i Translation Memory och kör generatorn.

## 📄 Licens & upphovsrätt

© **Bruno Penedo** — 2026. Användning, studier och bidrag uppmuntras; för kommersiell användning/vidaredistribution,
kontakta författaren. *(En formell OSS-licens kan läggas till — öppna en issue med din preferens.)*

## 🏷️ Topics
`awesome-list` · `education` · `resources` · `computer-science` · `python` · `business-intelligence` ·
`llmops` · `finops` · `aiops` · `programming` · `development` · `lists` · `free` · `unicorns` · `dashboard` ·
`balanced-scorecard` · `langfuse` · `llm-observability` · `kpi` · `project-management`

---

⭐ **Om detta ramverk kastar ljus över dina AI-utgifter, lämna en stjärna — och börja tjäna på det du redan betalar för.**

---

**Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard** · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
