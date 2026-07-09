# 🧭 Gestão de Projetos PM IA BSC DashBoard (Build and Analyze Your Own AI Portfolio Projects)

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

Vi är **pionjärer** i ett nytt territorium — **gränsen mellan artificiell intelligens och värderedovisning**. Som
upptäcktsresande som kartlägger okartlagd mark är detta ramverk **kompassen** (🧭) som förvandlar prenumerationernas
dimma till **tydliga avkastningsrutter**: varje token en mil; varje projekt en expedition mot vinst. Där det fanns
blind kostnad föds **mätbar möjlighet**; där det fanns ett dött kalkylark blomstrar en **levande investeringstes**.

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
