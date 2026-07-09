# 🧭 Gestão de Projetos PM IA BSC DashBoard (Build and Analyze Your Own AI Portfolio Projects)

🌐 [Português](README.md) · [English](README.en.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [中文](README.zh.md) · [한국어](README.ko.md) · [हिन्दी](README.hi.md) · [עברית](README.he.md) · [Svenska](README.sv.md) · [Русский](README.ru.md) · **Suomi**

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

### 💸 Maksat tekoälystä joka kuukausi. Mutta maksaako tekoäly **sinulle** takaisin?

Joka kerta kun **ChatGPT, Claude, Copilot, Gemini, Perplexity, DeepSeek, Kimi, Qwen…** veloittaa korttia, jää
**miljoonien** kysymys vastaamatta: **missä on tuotto?** Kuinka monta henkilötyötuntia todella säästyi? Kuinka
paljon rahastasi **haihtui** hallusinaatioon, uudelleentekemiseen ja odottamiseen? Mikä tekoälyprojekti **ansaitsee
skaalata tänään** — ja mikä **vuotaa kassaa**, kun taputat "innovaatiolle"?

Sinulla ei ole tekoälykustannusta. Sinulla on **hiljainen vuoto** — silmät sidottuina. Sillä *"mitä ei mitata, sitä
ei voi johtaa eikä parantaa"* — ja markkina mittaa sen puolestasi ja lähettää laskun.

**Tämä kehys sytyttää valon.** Se muuttaa tekoälytilaustesi **näkymättömät menot** **mitattavaksi, vertailukelpoiseksi
ja auditoitavaksi tuotoksi** — **Balanced Scorecardin** (Kaplan & Norton), **Wall Streetin tason
investointianalyysin** ja **monikriteeripäätöksen** tarkkuudella. Se on ero *toivomisen* ja *tietämisen* välillä.
Tekoälystä maksamisen ja sillä **ansaitsemisen** välillä.

> *"Mitä ei mitata, sitä ei voi johtaa eikä parantaa."* — Kaplan & Norton

> *"Joka mittaa tarkkuudella, rakentaa erinomaisuudella."* — Pierre Vernier

> *Kun rukoilet ja opiskelet, älä anna [sanojeni] jättää sinua. Jokaisen huuliltasi lähtevän sanan ja ilmauksen kanssa pidä mielessä Ykseyden toteuttaminen.* — Aryeh Kaplan

> *Puhdas metafysiikka, joka olemukseltaan sijaitsee kaikkien muotojen ja kaikkien satunnaisuuksien yläpuolella ja tuolla puolen, ei ole itäinen eikä läntinen: se on universaali.* — René Guénon

> *Itsensä tunteminen on oman sukujuurensa ja oman voimansa tuntemista.* — Harvey Spencer Lewis

> *Scientia es Lux Lucis* ∞ Sapere Aude S∴A∴☬ ☿

> 🐺 **Lopeta tekoälystä MAKSAMINEN pimeässä.** Kun markkina tilaa tekoälyä uskolla — ja muuttuu **Gartnerin**
> tilastoksi (≥30 % GenAI-projekteista hylätään pilotin jälkeen) — **sinä** mittaat jokaisen tokenin, valitset
> voittajaprojektin ja muutat näkymättömät menot **auditoitavaksi tuotoksi**: NPV · IRR · MIRR · EAA · 70+ KPI ·
> monikriteeripäätös · johtotason dashboard **12 kielellä**. **Tekoäly on jo sinun. Tee siitä nyt KANNATTAVA** —
> ilmaiseksi, omalla koneellasi, **5 minuutissa**: `./run_all.sh --mock && npm run dev` 🔥

> 📖 **Päädokumentaatio:** **[`foundations/README.md`](foundations/README.md)** ·
> ⚙️ **Asennus (tuo omat avaimesi):** [`foundations/pipeline/SETUP.md`](foundations/pipeline/SETUP.md) ·
> 📊 **KPI:t:** [`foundations/KPIs.md`](foundations/KPIs.md) / [`foundations/KPIs_README.md`](foundations/KPIs_README.md)

---

## 📑 Sisällys

- [🌅 Miksi tämä muuttaa pelin](#-miksi-tämä-muuttaa-pelin)
- [📈 Todisteet (Gartner · IDC · PwC · McKinsey · MIT)](#-todisteet-gartner--idc--pwc--mckinsey--mit)
- [💥 Toimimattomuuden hinta](#-toimimattomuuden-hinta-tee-laskelma-jota-kukaan-ei-tee)
- [✨ Ominaisuudet](#-ominaisuudet)
- [📸 Kuvakaappaukset (anonyymi dashboard)](#-kuvakaappaukset-anonyymi-dashboard)
- [🚀 Pikaopas](#-pikaopas-demo-ilman-langfusea)
- [🏗️ Arkkitehtuuri](#️-arkkitehtuuri)
- [📊 KPI-luettelo](#-kpi-luettelo-70)
- [💰 Investointitason talousanalyysi](#-investointitason-talousanalyysi)
- [🏆 Monikriteeripäätös + Dossier](#-monikriteeripäätös-ahp-topsis-2n--kruununjalokivi-dossier)
- [🎲 Monte Carlo — riski, jonka keskiarvo kätkee](#-monte-carlo--riski-jonka-keskiarvo-kätkee)
- [🧮 Viisi päätöksenteon koulukuntaa. Yksi tuomio.](#-viisi-päätöksenteon-koulukuntaa-yksi-tuomio)
- [🌐 12 kieltä](#-12-kieltä)
- [🙋 Vastaväitteet (kysymykset, joita kysyt itseltäsi juuri nyt)](#-vastaväitteet-kysymykset-joita-kysyt-itseltäsi-juuri-nyt)
- [🧩 Mukana tulevat Skillit](#-mukana-tulevat-skillit-build--analyze-your-own)
- [📚 Resurssit & viitteet](#-resurssit--viitteet-awesome)
- [🗺️ Tiekartta](#️-tiekartta)
- [🤝 Osallistuminen](#-osallistuminen)
- [📄 Lisenssi & tekijyys](#-lisenssi--tekijyys)

---

## 🌅 Miksi tämä muuttaa pelin

**Tekoälyaikakaudella on kahdenlaisia ihmisiä.** Ensimmäiset tilaavat kaiken, kuluttavat isosti ja **rukoilevat**,
että se toimii — ja paisuttavat julmaa tilastoa projekteista, jotka kuolevat pilottiin. Toiset tekevät sen, mitä
Wall Street tekee jokaiselle vakavalle omaisuuserälle: he **mittaavat, vertailevat, priorisoivat ja kohdentavat
uudelleen** — ja muuttavat jokaisen tilausdollarin **korkoa korolle -tuotoksi**. Ainoa ero heidän välillään **ei ole
lahjakkuus eikä budjetti. Se on instrumentointi.**

Generatiivinen tekoäly loi uuden toistuvien menojen luokan — **tilaukset ja tokenit** — ja sen mukana vuosikymmenen
kalleimman tuhlauksen: **näkymättömän.** Mitä et näe, sitä et korjaa. Mitä et mittaa, sitä et skaalaa. Ja mitä et
todista, sitä hallitus ei hyväksy.

**Tämä projekti siirtää sinut ensimmäisestä heimosta toiseen.** Se instrumentoi jokaisen tekoälyprojektin
**rahoitusomaisuutena** ja mittaa sitä **Balanced Scorecardin**, **investointianalyysin (NPV, IRR, MIRR, EAA, PI,
takaisinmaksuaika)** ja **Lean Six Sigman** alla — ja jopa **valitsee salkkusi parhaan projektin**
monikriteerimallilla (**AHP-TOPSIS 2n**). Läpinäkymätön kuukausilasku muuttuu **auditoitavaksi investointiteesiksi**:
saat numeroin selville, missä skaalata, missä leikata, missä tilaus maksaa itsensä takaisin **viikoissa** — ja missä
se vuotaa ilman katetta.

Olemme uuden alueen **edelläkävijöitä** — **tekoälyn ja arvon kirjanpidon välisen rajan**. Kuten tutkimusmatkailijat,
jotka kartoittavat vielä kartoittamatonta maata, tämä kehys on **kompassi** (🧭), joka muuttaa tilausten sumun
**selkeiksi tuottoreiteiksi**: jokainen token maili; jokainen projekti retkikunta kohti voittoa. Missä oli sokea
kustannus, syntyy **mitattava mahdollisuus**; missä oli kuollut taulukko, kukkii **elävä investointiteesi**.

> **Lupaus:** muuttaa se, joka *maksaa tekoälystä*, siksi, joka *ansaitsee tekoälyllä* — ja se, joka *käyttää
> tekoälyä*, siksi, joka **edelläkävijänä hallitsee, mittaa ja moninkertaistaa sitä**. Numeroin, ei uskolla.

---

## 📈 Todisteet (Gartner · IDC · PwC · McKinsey · MIT)

Älä usko minua. **Usko instituutteja, jotka ovat tutkineet tätä vuosikymmeniä** — joiden tuomio on yksimielinen:
**tekoäly luo valtavaa arvoa, mutta antaa sen vain niille, jotka mittaavat ja hallitsevat.** Ne, jotka "käyttävät
tekoälyä hallitsematta sitä", muuttuvat hylkäystilastoksi; ne, jotka instrumentoivat tuoton, **pitävät palkinnon**.

- 🧭 **Gartner** — ennusti, että **≥ 30 % generatiivisen tekoälyn projekteista hylätään konseptitodistuksen jälkeen
  vuoden 2025 loppuun mennessä**, keskeisenä syynä **epäselvä liiketoiminta-arvo** (lisäksi huono data, nousevat
  kustannukset ja heikot kontrollit). *→ ilman mittausta projekti kuolee pilottiin.*
- 🔬 **MIT** (raportti *"The GenAI Divide / State of AI in Business 2025"*, NANDA-aloite) — laajasti raportoitu, että
  **valtaosa yritysten GenAI-piloteista ei tuota mitattavaa vaikutusta tulokseen**; vähemmistö, joka tuottaa arvoa,
  yhdistää tekoälyn **prosessiin ja mittaukseen**. *→ ero on mittaamisessa, ei käyttöönotossa.*
- 💵 **IDC** (tutkimus *"The Business Opportunity of AI"*, Microsoftin tukema) — organisaatiot, jotka **mittaavat ja
  optimoivat**, raportoivat tuoton suuruusluokkaa **useita dollareita jokaista sijoitettua 1 US$** kohti, suurella
  hajonnalla johtajien ja jälkeenjääneiden välillä. *→ ROI on olemassa — ja suosii instrumentoijia.*
- 🌍 **PwC** (*"Sizing the Prize"*) — arvioi, että tekoäly voi lisätä jopa **~15,7 biljoonaa US$** maailmantalouteen
  vuoteen 2030 mennessä; mutta palkinto menee niille, jotka **kaappaavat** arvon, ei vain kuluttaville. *→ kakku on
  jättimäinen; siivu kuuluu mittaaville.*
- 🏆 **McKinsey** (*"The State of AI"*) ja **BCG × MIT Sloan** — vähemmistöryhmä **"AI high performers"** kaappaa
  suhteettoman tuoton; käännekohta tulee, kun tekoäly kytketään **mittareihin, hallintoon ja uudelleensijoittamiseen**
  siellä, missä tuotto on todistettu. *→ voittajat mittaavat, priorisoivat ja kohdentavat uudelleen.*

> **Juuri tämän kuilun tämä kehys ylittää:** se siirtää sinut puolelta, joka *luovuttaa pilotissa*, puolelle, jolla
> on **todellisia, todistettuja tuloksia** — BSC:llä, investointianalyysillä ja monikriteeripäätöksellä.

> ⚠️ **Rehellisyyshuomautus (lue):** yllä olevat luvut heijastavat näiden instituuttien todellisia otsikoita, mutta
> **raportit ja prosentit päivittyvät** — varmista tarkat arvot ja vuosi **alkulähteistä** (Gartner Newsroom;
> IDC/Microsoft *Business Opportunity of AI*; PwC *Sizing the Prize*; McKinsey *State of AI*; MIT *State of AI in
> Business*) ennen kuin siteeraat niitä virallisessa materiaalissa. Tässä ne toimivat **suuntaa antavana perustana**,
> eivät numeraalisena takuuna.

---

## 💥 Toimimattomuuden hinta (tee laskelma, jota kukaan ei tee)

**PRO-tekoälytilaus** maksaa **20–200 US$ kuukaudessa per paikka**. Kerro tiimisi henkilömäärällä. Kerro 12
kuukaudella. Sovella nyt sitä, minkä instituutit ovat jo **todistaneet**: **Gartner** ennustaa **≥ 30 % hylkäystä**
ja **MIT** osoittaa, että **valtaosa piloteista ei tuota**. Valtava osa tuosta summasta ei ole investointi — se on
**puhdasta verenvuotoa**.

> **Suora esimerkki (vaihda omat lukusi):** 10 paikkaa × 30 US$/kk × 12 = **3 600 US$/vuosi**. Jos ~30 % muuttuu
> näkymättömäksi tuhlaukseksi, se on **~1 080 US$/vuosi haihtumassa** — YHDESTÄ pienestä tiimistä, YHDESSÄ vuodessa.
> Omalla oikealla luvullasi järkytys on suurempi.

Ja tässä se osa, joka sattuu: **tämä kustannus kertyy korkoa korolle eikä odota.** Jokainen mittaamaton kuukausi on
kuukausi vuotoa, joka **ei palaa** — kun taas kilpailija, joka instrumentoi, jo **kohdentaa pääomaa siihen, mikä
tuottaa**. Edelläkävijän etu rakennetaan varhain: **se, joka mittaa ensin, skaalaa ensin.**

Halvin hetki aloittaa oli eilen. Toiseksi paras on **nyt** — ja se maksaa **0 US$** ja **5 minuuttia**. Kysymys ei
ole *"onko minulla varaa mitata?"*. Se on ***"kuinka kauan minulla vielä on varaa OLLA mittaamatta?"***

---

## ✨ Ominaisuudet

- **📊 KPI:t (4 BSC-näkökulmaa) + API-talous:** kypsyys, inhimillinen pääoma, taloudellinen ja token-tehokkuus —
  `IEET`, `IOLI`, `ITR`, `IITA`, `PEUC`, `ICCA`, `IDLS`, `IBMT` — sekä **EVM** (CPI/SPI/EAC).
- **🪙 Rajakäsitteet:** **VRT/kTR** (tokenisoitava kustannustenpalautusyksikkö — *"Gitmanin m²"*) ja **PSR** (Project
  Score 0–5 ⭐) kunkin projektin terveyden luokitteluun.
- **🔬 Operatiivinen diagnostiikka:** **VRT 5 lohkossa**, **HCI** (kriittinen keskeytystunti), **Lean Six Sigma
  -hukat** (painotetut tokenit) ja **hallusinaatio-RCA promptitaksonomian mukaan** (pullonkaula per projekti +
  leikkaus).
- **💰 Täysi talouspaketti:** **NPV, IRR, MIRR, EAA (ekvivalentti annuiteetti), PI, takaisinmaksuaika** (yksinkertainen
  & diskontattu), **dollarisointi** ja vertailu **SELIC**-korkoon ja **USA:n korkoon**.
- **🏆 Monikriteeripäätös:** **AHP-TOPSIS 2n** (kaksoisnormalisointi) valitsee salkun **parhaan projektin**
  **robustisuustestillä** — ja luo **hallinnollisen dossierin** (SWOT, PESTELC, 5W4H, Pareto, GUT, Radar).
- **🗺️ Johtotason visuaalit:** **interaktiivinen 5D-kartta**, syvyysdonitsit, kestävyyskvadrantti, trendit ja
  LaTeX-**pitch deckit** kelpoisille projekteille.
- **⚙️ Todellinen putki:** **Langfuse → SQLite → Evidence**, **asynkronisella samanaikaisella** synkronoinnilla ja
  **Rustissa (PyO3)** kiihdytetyllä luokittelulla.
- **💳 Tekoäly-FinOps:** **tilaussuunnitelmien** luettelo (OpenAI, Anthropic, Google, Perplexity, xAI, Mistral,
  DeepSeek, Kimi, Qwen…) **valuuttakurssilla + IOF** ja jakoperusteella (burn rate).
- **🌐 12 kieltä** dashboardissa **ja kaavioiden kuvien sisäisessä tekstissä** (ml. devanagari, heprea ja CJK).

---

## 📸 Kuvakaappaukset (anonyymi dashboard)

> 100 % anonyymi demo (projektit näytetään muodossa *Project A…J*). Todellinen data/nimet eivät koskaan tule paketin mukana.

**🌐 Salkun 5D-kartta** — 5 ulottuvuutta per projekti: **X**=tokenit · **Y**=PEUC (laatu) · **Z**=PSR (terveys) ·
**koko**=Burn Rate · **väri**=ICCA (kestävyys). *Missä skaalata? Oikealla/takana, korkealla ja vihreänä. Missä
leikata? Suuri ja punainen.*

![Tekoälyprojektisalkun 5D-kartta](docs/screenshots/5d-portfolio-map.png)

**🏆 "Kruununjalokivi"-dossier** (AHP-TOPSISin valitsema projekti) — luotu samanaikaisella Python-putkella:

| SWOT | Kilpailututka |
|---|---|
| ![SWOT](docs/screenshots/swot.png) | ![Kilpailututka](docs/screenshots/radar.png) |

| PESTELC (makroympäristö) | GUT-matriisi (priorisointi) |
|---|---|
| ![PESTELC](docs/screenshots/pestel.png) | ![GUT](docs/screenshots/gut.png) |

| 5W4H (toimintasuunnitelma) | Vika-Pareto (80/20) |
|---|---|
| ![5W4H](docs/screenshots/5w4h.png) | ![Pareto](docs/screenshots/pareto.png) |

---

## 🚀 Pikaopas (demo, ilman Langfusea)

**Nolla riskiä. Nolla kustannusta. 5 minuuttia.** Aja se omalla koneellasi ja näe koko dashboard anonyymillä datalla:

```bash
cd foundations/pipeline
pip install -r requirements.txt
cd ../evidence && npm install && cd ../pipeline
./run_all.sh --mock          # anonyymi data (Project A..J) -> KPI -> NPV/MIRR/EAA -> 5D -> pitch deckit -> dashboard
cd ../evidence && npm run dev # http://localhost:3000
```

**Todellista dataa** varten täytä `foundations/pipeline/.env` **omilla** Langfuse-avaimillasi (ks.
[`SETUP.md`](foundations/pipeline/SETUP.md)) ja aja `./run_all.sh`. Jokainen käyttäjä käyttää **omaa tiliään** —
tekijän avaimet eivät tule paketin mukana.

---

## 🏗️ Arkkitehtuuri

```
   Sinun tekoälysovelluksesi   Havainnoitavuus         Analytics-as-Code           Sinä
 (ChatGPT, Claude, API…)   ┌──────────────┐   ┌──────────────────┐   ┌──────────────────────┐
        │ traces           │   Langfuse   │   │  SQLite (schema  │   │  Evidence (BI as     │
        └─────────────────▶│  (SDK v4)    │──▶│  + KPI-kyselyt)  │──▶│  Code) · 12 kieltä   │
                           └──────────────┘   └──────────────────┘   └──────────┬───────────┘
   asynkroninen samanaikainen synk.     luokittelu Rustissa (PyO3)              │
                                                                    ┌───────────┴───────────┐
                                                                    │ AHP-TOPSIS · Dossier  │
                                                                    │ 5D · Pitch deckit(TeX)│
                                                                    └───────────────────────┘
```

**Pino:** Python 3.13 · SQLite/DuckDB · Evidence.dev (SvelteKit) · Rust + PyO3 + maturin · matplotlib ·
tectonic (LaTeX) · Noto/WenQuanYi-fontit kuvien i18n:ää varten.

---

## 📊 KPI-luettelo (70+)

Otos (koko luettelo tiedostossa [`foundations/KPIs_Lean6s_BSC.md`](foundations/KPIs_Lean6s_BSC.md)):

| Lyhenne | Nimi | Mihin vastaa |
|---|---|---|
| **PSR** | Project Score Rating (0–5) | Tekoälyprojektin yleisterveys |
| **PEUC** | Hyödyllinen tuotos per kulutus % | Kuinka paljon menoista muuttui hyödylliseksi tuotokseksi |
| **IITA** | Hallusinoitujen tokenien esiintyvyysindeksi | Hallusinaation/uudelleentekemisen % |
| **IDLS** | Lean-hukkaindeksi | Muda (vakavuudella painotetut tokenit) |
| **VRT/kTR** | Tokenisoitava palautusarvo | "Gitmanin m²" — kustannus per 1k tokenia |
| **ICCA** | Tilauskustannusten kattavuusindeksi | Kattaako kustannuksen? (>3× terve) |
| **CPP** | Kustannus per edistymispiste | Pääindikaattori (mitä pienempi, sitä parempi) |

---

## 💰 Investointitason talousanalyysi

Jokaisesta projektista tulee **investointiteesi**: kassavirrastasi (CSV) kehys laskee **NPV**:n, **IRR**:n, **MIRR**:n
**(uudelleensijoittaa projektin kustannuksella)**, **EAA**:n **(NPV:n ekvivalentti annuiteetti)**, **PI**:n
**(kannattavuusindeksi)** ja **takaisinmaksuajan** (yksinkertainen/diskontattu) — **dollarisoiden** virran ja
vertaillen **SELIC**-korkoon ja **USA:n korkoon**. Se luo LaTeX-**pitch deckin** jokaiselle projektille, jonka **NPV
> 0 ja PI > 1** sekä BRL:ssä **että** USD:ssä. Tavoite on raa'an käytännöllinen: **selvittää, maksaako tekoälytilauksesi
itsensä takaisin — ja kuinka nopeasti.**

---

## 🏆 Monikriteeripäätös (AHP-TOPSIS 2n) + Kruununjalokivi-dossier

Kun projekteja on useita, minkä skaalata ensin? **AHP-TOPSIS 2n** -malli painottaa indikaattorit kriteereinä (painot
**AHP**:lla johdonmukaisuussuhteella **CR ≤ 0,10**) ja järjestää **TOPSIS**illä **kahdella normalisoinnilla** (vektori
+ min-max), raportoiden **robustisuuden** (normalisointien välinen yhtäpitävyys). Voittaja — **"Kruununjalokivi"** —
saa täyden **hallinnollisen dossierin** (SWOT · PESTELC · 5W4H · Pareto · GUT · Radar), joka luodaan tyhjästä koodilla,
johtotason **Bottom-Linen** ja rehellisten **johtotason oivallusten** kera. **Et esitä taulukkoa. Esität tuomion.**

---

## 🎲 Monte Carlo — riski, jonka keskiarvo kätkee

**Keskimäärin** positiivinen NPV ei suojaa ketään. Keskiarvo on rahoituksen mukavin valhe: se kuvaa skenaariota, jota
ei ehkä koskaan tule. Kohtalosi ratkaisee **häntä** — se huono päivä.

Tämä kehys simuloi **10 000 tulevaisuutta** jokaiselle projektille (moottori yhteensopiva **SimulAr v2.5**:n kanssa,
Luciano Machain, UNR/Argentiina): jokainen kassavirta muuttuu **satunnaismuuttujaksi** ja koko salkku lasketaan uudelleen
iteraatio kerrallaan. Lopussa sinulla ei ole lukua — sinulla on **rahojesi koko jakauma**:

- **`P(NPV < 0)`** — todellinen tappion todennäköisyys. Se luku, jota kukaan ei näytä sinulle.
- **VaR 5 %** — pahin uskottava skenaario: *"19:ssä tulevaisuudessa 20:stä ansaitsen vähintään tämän."*
- **CVaR 5 %** — kun katastrofi todella iskee, paljonko se keskimäärin maksaa.
- **Herkkyystornado** — monimuuttujaregressio ja Pearsonin korrelaatio: mikä muuttuja todella liikuttaa NPV:täsi.
- **20 syötejakaumaa**, validoitu **korrelaatiomatriisi** (Iman-Conover, joka säilyttää reunajakaumat täsmälleen) ja
  **prosenttipisteet 1 %:sta 99 %:iin**, sekä 100 luokan histogrammi, identtinen SimulArin käsikirjan kanssa.

Kiinteä siemen: aja uudelleen ja saat **täsmälleen** saman tuloksen. Auditoitavaa — ei "taikuutta".

> **Käännekohta:** lakkaat valitsemasta korkeimman NPV:n projektia ja alat valita **sitä, joka selviää huonosta
> skenaariosta**. Se on riskienhallintaa — se erottaa sijoittajan pelurista.

![Histograma de Monte Carlo do VPL — 10.000 iterações, 100 classes](docs/screenshots/mc-histograma.png)

| NPV:n kertymäjakauma | Herkkyystornado |
|---|---|
| ![NPV:n kertymäjakauma](docs/screenshots/mc-acumulado.png) | ![Herkkyystornado](docs/screenshots/mc-tornado.png) |

---

## 🧮 Viisi päätöksenteon koulukuntaa. Yksi tuomio.

Yksi menetelmä voi erehtyä. Viisi samaa mieltä olevaa menetelmää ei.

Seuraten **Johnin (2025)** arkkitehtuuria — *Integration of DEMATEL with Other MCDM Methods* — **DEMATEL** kartoittaa
kriteerien välisen syy-rakenteen ja erottaa **syyt** (vivut, joihin tarttua) **seurauksista** (jo tehdyn lämpömittarit).
Näistä vaikutussilmukoista syntyvät **painot**: ei mielivaltaisesti asetettuja, vaan **ongelman rakenteesta johdettuja**.
Ne ruokkivat neljää kilpailevaa koulukuntaa:

| Menetelmä | Koulukunta | Mitä se kysyy |
|---|---|---|
| **ELECTRE I** | Ylivertaisuus | "Kuka ylittää kenet — ja kuka selviää hallitsemattomana?" |
| **PROMETHEE II** | Ylivertaisuus | "Mikä on kunkin projektin nettopreferenssivirta?" |
| **MAUT** | Hyöty | "Mikä maksimoi riskiä karttavan päättäjän hyödyn?" |
| **MCDA-C** | Konstruktivistinen | "Kuka on *Hyvä*-tason yläpuolella — ja kuka *Neutraalin* alapuolella?" |
| **AHP-TOPSIS 2n** | Etäisyys ideaaliin | "Kuka on lähinnä ideaaliratkaisua molemmissa normalisoinneissa?" |

Voittaja nousee viiden **Borda-konsensuksesta**, jo Monte Carlolla **riskikorjattuna**. Ja kun menetelmät ovat **eri
mieltä**, dashboard näyttää erimielisyyden — sillä sekin on informaatiota: valinta on herkkä päätöskoulukunnalle ja
ansaitsee päättäjän silmän.

| DEMATEL — syyt × seuraukset | Sijoitus menetelmittäin |
|---|---|
| ![DEMATEL — syyt × seuraukset](docs/screenshots/dematel.png) | ![Sijoitus menetelmittäin](docs/screenshots/mcdm-metodos.png) |

### 💼 Mikä muuttuu arjessasi — freelancerista konserniin

Sillä ei ole väliä, maksatko **20 US$ PRO-tilauksesta** vai **200 000 US$ yrityssopimuksista**: hukan matematiikka on
sama — vain nollien määrä muuttuu.

| | **Pk-yritys / freelancer** | **Suuryritys** |
|---|---|---|
| **Todellinen kipu** | 3 tilausta, nolla näkyvyyttä, tiukka kassa | 40 tekoälypilottia, yhtäkään ei ole kohdennettu tulokseen |
| **Monte Carlo antaa** | *"tällä projektilla on 12 % todennäköisyys tappiolle, ja huono kuukausi maksaa 3 400 US$"* | VaR/CVaR liiketoimintayksiköittäin: koottu, auditoitava riski — ei anekdootti |
| **MCDM antaa** | minkä kolmesta projektista skaalaat **ensin** olemassa olevalla rahalla | mikä 40 pilotista muuttuu tuotteeksi — puolustettavissa komiteassa, menetelmä näkyvissä |
| **Hyöty jo huomenna** | irtisano tilaus, joka ei maksa itseään takaisin — jo tällä viikolla | kohdenna budjetti **näytön** perusteella, ei sisäpolitiikan |

**Käytännössä:** **tornado** osoittaa muuttujan, joka liikuttaa tulosta — eli **mihin sijoitat seuraavan työtuntisi**.
**DEMATEL** paljastaa, että hallusinaation vähentäminen (IITA) on **syy**, ei oire: toimi siellä, niin NPV, IRR ja riski
paranevat *yhdessä*. Näin tekoälyn hallinnasta lakkaa olemasta mielipide ja tulee **insinööritaitoa**.


---

## 🌐 12 kieltä

Dashboard, projektikohtaiset sivut **ja kaavioiden kuvien sisäinen teksti** on lokalisoitu **12 kielelle**:
Português · English · Español · Français · Deutsch · 中文 · 한국어 · हिन्दी · עברית · Svenska · Русский · Suomi.
Kääntämistä ohjaa **Translation Memory** (SDL Trados -tyyliin), joka standardoi ja nopeuttaa uusia kieliä.

---

## 🙋 Vastaväitteet (kysymykset, joita kysyt itseltäsi juuri nyt)

- **"Minulla ei ole aikaa."** → Viisi minuuttia komennolla `./run_all.sh --mock`, ja dashboard pyörii näytölläsi.
  Mittaaminen **palauttaa** ne tunnit, jotka jo menetät uudelleentekemiseen ja hallusinaatioon.
- **"Se on liian monimutkaista."** → Yksi rivi. Kehys hoitaa ETL:n, laskennat, järjestyksen ja kuvat; **sinä vain
  luet tuomion.**
- **"Tekoälytoimintani on pieni."** → Juuri siksi jokainen dollari painaa enemmän. Pieni tänään, salkku huomenna —
  **mittaa ennen kuin skaalaat tuhlauksen.**
- **"En käytä Langfusea."** → Demo pyörii **100 % ilman Langfusea**. Kun haluat todellista dataa, kytket **oman**
  tilisi (et koskaan minun).
- **"Se on vain yksi kaunis dashboard lisää."** → Ei. Se on **Balanced Scorecard + investointianalyysi
  (NPV/IRR/MIRR/EAA) + monikriteeripäätös (AHP-TOPSIS)** — johtotason työkaluja, ei koristetta.
- **"Entä datani yksityisyys?"** → Demo on **100 % anonyymi** (Project A…J); todellinen data/nimet ja avaimet pysyvät
  **paketin ulkopuolella**. Ajat **paikallisesti**, **omalla** tililläsi.
- **"Paljonko se maksaa?"** → **Ei mitään.** Avoin lähdekoodi, omalla koneellasi. Ainoa hinta on jatkaa **mittaamatta
  jättämistä** — ja sitä maksat jo.

---

## 🧩 Mukana tulevat Skillit (*build & analyze your own*)

Tämä repositorio toimittaa uudelleenkäytettäviä **Skillejä** (Claude Code):

- **`measuring-ai-projects`** — määrittele/mittaa/raportoi tekoälyprojektien KPI:t (tämän kehyksen ydin).
- **`github-benchmark-analyzer`** — analysoi ja benchmarkkaa **mikä tahansa** GitHub-repositorio/-profiili (tähdet,
  forkit, seuraajat, hashtagit, README-tyyli, avainsanat, kielet) ja poimi, mikä johtajilla on yhteistä. **Rakenna ja
  analysoi oma salkkusi** — jopa markkinaa vastaan.

---

## 📚 Resurssit & viitteet (Awesome)

Jättiläisten hartiat, joilla tämä kehys seisoo:

- **Strategia & mittaus:** Kaplan & Norton — *The Balanced Scorecard* · Peter Drucker (tavoitejohtaminen).
- **Lean Six Sigma:** 8 hukan (Muda) taksonomia, PDCA/Kaizen, Ishikawa/RCA.
- **Yritysrahoitus:** Lawrence Gitman — *Principles of Managerial Finance* (NPV, IRR, MIRR, PI).
- **Monikriteeripäätös:** Thomas Saaty (**AHP**) · Hwang & Yoon (**TOPSIS**).
- **Tekninen pino:** [Langfuse](https://langfuse.com) (LLM observability) · [Evidence](https://evidence.dev)
  (BI as Code) · [Rust/PyO3](https://pyo3.rs) · [Tectonic](https://tectonic-typesetting.github.io) (LaTeX).

---

## 🗺️ Tiekartta

- [x] Putki Langfuse → SQLite → Evidence + Rust
- [x] 70+ KPI (BSC + API-talous + Lean) · EVM
- [x] Talous (NPV, IRR, MIRR, EAA, PI, takaisinmaksuaika, dollarisointi)
- [x] AHP-TOPSIS 2n + hallinnollinen dossier (6 työkalua)
- [x] Dashboard ja kuvat **12 kielellä**
- [ ] Lisää havainnoitavuuskonnektoreita (OpenTelemetry, Helicone)
- [ ] Monivuokralainen SaaS-tila + natiivi ajastus
- [ ] Staattisen dashboardin julkaisu (GitHub Pages)

---

## 🤝 Osallistuminen

Kontribuutiot ovat **erittäin tervetulleita**! Avaa *issue*, joka kuvaa ehdotuksesi (uusi KPI, konnektori, kieli,
korjaus), ja lähetä *pull request*. Standardit: luettava, ympäristöönsä sopiva koodi, ei henkilötietoja paketissa
(demo on anonyymi). Uudet kielet: lisää kohteet Translation Memoryyn ja aja generaattori.

## 📄 Lisenssi & tekijyys

© **Bruno Penedo** — 2026. Käyttöä, opiskelua ja kontribuutioita kannustetaan; kaupallista käyttöä/uudelleenjakelua
varten ota yhteyttä tekijään. *(Muodollinen OSS-lisenssi voidaan lisätä — avaa issue mieltymyksesi kera.)*

## 🏷️ Topics
`awesome-list` · `education` · `resources` · `computer-science` · `python` · `business-intelligence` ·
`llmops` · `finops` · `aiops` · `programming` · `development` · `lists` · `free` · `unicorns` · `dashboard` ·
`balanced-scorecard` · `langfuse` · `llm-observability` · `kpi` · `project-management`

---

⭐ **Jos tämä kehys valaisee tekoälymenojasi, jätä tähti — ja ala ansaita sillä, mistä jo maksat.**

---

**Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard** · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
