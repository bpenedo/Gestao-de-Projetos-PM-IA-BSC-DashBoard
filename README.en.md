# 🧭 Gestão de Projetos PM IA BSC DashBoard (Build and Analyze Your Own AI Portfolio Projects)

<p align="center">
  <img src="docs/hero.jpg" alt="AI Project Management PM BSC DashBoard" width="820">
</p>

🌐 [Português](README.md) · **English** · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [中文](README.zh.md) · [한국어](README.ko.md) · [हिन्दी](README.hi.md) · [עברית](README.he.md) · [Svenska](README.sv.md) · [Русский](README.ru.md) · [Suomi](README.fi.md)

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

### 💸 You pay for AI every month. But is AI paying **you** back?

Every time the card is charged by **ChatGPT, Claude, Copilot, Gemini, Perplexity, DeepSeek, Kimi, Qwen…**, a
**million-dollar** question goes unanswered: **where is the return?** How many person-hours were actually saved?
How much of your money **evaporated** into hallucination, rework and waiting? Which AI project **deserves to
scale today** — and which one is **bleeding cash** while you applaud the "innovation"?

You don't have an AI cost. You have a **silent leak** — and you're blindfolded. Because *"what is not measured
cannot be managed or improved"* — and the market measures it for you, and bills you.

**This framework turns the lights on.** It converts the **invisible spend** of your AI subscriptions into
**measurable, comparable and auditable return** — with the rigor of the **Balanced Scorecard** (Kaplan &
Norton), **Wall-Street-grade investment analysis** and **multi-criteria decision**. It's the difference between
*hoping* and *knowing*. Between paying for AI and **profiting** from it.

> *"What is not measured cannot be managed or improved."* — Kaplan & Norton

> *"Those who measure with precision, build with excellence."* — Pierre Vernier

> *When you pray and study, do not let [my words] leave you. With every word and expression that leaves your lips, keep in mind to bring about a Unification.* — Aryeh Kaplan

> *Pure metaphysics, situating itself by essence above and beyond all forms and all contingencies, is neither Eastern nor Western: it is universal.* — René Guénon

> *To know yourself is to know your own lineage and your own power.* — Harvey Spencer Lewis

> *Scientia es Lux Lucis* ∞ Sapere Aude S∴A∴☬ ☿

> 🐺 **Stop PAYING for AI in the dark.** While the market subscribes to AI on faith — and becomes the **Gartner**
> statistic (≥30% of GenAI projects abandoned after the pilot) —, **you** will measure every token, elect the
> winning project and convert invisible spend into **auditable return**: NPV · IRR · MIRR · EAA · 70+ KPIs ·
> multi-criteria decision · C-Level dashboard in **12 languages**. **The AI is already yours. Now make it
> PROFITABLE** — for free, on your machine, in **5 minutes**: `./run_all.sh --mock && npm run dev` 🔥

> 📖 **Main documentation:** **[`foundations/README.md`](foundations/README.md)** ·
> ⚙️ **Setup (bring your own keys):** [`foundations/pipeline/SETUP.md`](foundations/pipeline/SETUP.md) ·
> 📊 **KPIs:** [`foundations/KPIs.md`](foundations/KPIs.md) / [`foundations/KPIs_README.md`](foundations/KPIs_README.md)

---

## 📑 Table of contents

- [🌅 Why this changes the game](#-why-this-changes-the-game)
- [📈 The evidence (Gartner · IDC · PwC · McKinsey · MIT)](#-the-evidence-gartner--idc--pwc--mckinsey--mit)
- [💥 The cost of inaction](#-the-cost-of-inaction-do-the-math-nobody-does)
- [✨ Features](#-features)
- [📸 Screenshots (anonymous dashboard)](#-screenshots-anonymous-dashboard)
- [🚀 Quick start](#-quick-start-demo-no-langfuse)
- [🏗️ Architecture](#️-architecture)
- [📊 KPI catalog](#-kpi-catalog-70)
- [💰 Investment-grade financial analysis](#-investment-grade-financial-analysis)
- [🏆 Multi-criteria decision + Dossier](#-multi-criteria-decision-ahp-topsis-2n--crown-jewel-dossier)
- [🎲 Monte Carlo — the risk the average hides](#-monte-carlo--the-risk-the-average-hides)
- [🧮 Five schools of decision. One verdict.](#-five-schools-of-decision-one-verdict)
- [🔬 The signal is upstream — and that is where the leverage lives](#-the-signal-is-upstream--and-that-is-where-the-leverage-lives)
- [🎓 Foundations: what Monte Carlo is, and what Multi-Criteria Decision is](#-foundations-what-monte-carlo-is-and-what-multi-criteria-decision-is)
- [🌐 12 languages](#-12-languages)
- [🙋 Objections (the questions you're asking right now)](#-objections-the-questions-youre-asking-right-now)
- [🧩 Bundled skills](#-bundled-skills-build--analyze-your-own)
- [📚 Resources & references](#-resources--references-awesome)
- [🗺️ Roadmap](#️-roadmap)
- [🧰 Step-by-step setup (local, from scratch)](#-step-by-step-setup-local-from-scratch)
- [🤝 Contributing](#-contributing)
- [📄 License & authorship](#-license--authorship)

---

## 🌅 Why this changes the game

**There are two kinds of people in the AI era.** The first subscribe to everything, spend big and **pray** it
works out — and swell the cruel statistic of projects that die in the pilot. The second do what Wall Street does
with any serious asset: they **measure, compare, prioritize and reallocate** — and turn every subscription
dollar into **compounding return**. The only difference between them **isn't talent or budget. It's
instrumentation.**

Generative AI created a new class of recurring expense — **subscriptions and tokens** — and, with it, the most
expensive waste of the decade: **the invisible kind.** What you don't see, you don't fix. What you don't
measure, you don't scale. And what you don't prove, the board doesn't approve.

**This project moves you from the first tribe to the second.** It instruments every AI project as a **financial
asset** and measures it under the **Balanced Scorecard**, **investment analysis (NPV, IRR, MIRR, EAA, PI,
Payback)** and **Lean Six Sigma** — and it even **elects the best project in your portfolio** through a
multi-criteria model (**AHP-TOPSIS 2n**). The opaque monthly bill becomes an **auditable investment thesis**:
you find out, with numbers, where to scale, where to cut, where the subscription pays for itself in **weeks** —
and where it is bleeding without coverage.

We are **pioneers** of a new territory — the **frontier between artificial intelligence and high-value financial intelligence**. Like explorers charting unmapped lands, this framework is the **compass** (🧭) that turns the fog of
subscriptions into **clear routes of return**: each token a mile; each project an expedition toward profit.
Where there was blind cost, **measurable opportunity** is born; where there was a dead spreadsheet, a **living
investment thesis** blossoms.

### 🚀 For Micro-SaaS, SaaS, Startups and Solopreneurs

Here's what nobody told you when you embedded AI into your product: **you just moved AI from your marketing
budget into your COGS.** And COGS that grows with usage isn't an expense — it's a **mortgage on your gross
margin**. Every new user now costs tokens. Every retry caused by hallucination burns margin twice. And the bill
only shows up at month's end, when it's too late to undo.

| You are… | The pain nobody measures | What this framework hands back |
|---|---|---|
| **Solopreneur** | you *are* the team; your hour is the most expensive asset there is | the **tornado** points to the variable that moves the result — hence **where to invest your next hour** |
| **Micro-SaaS** | token cost grows with usage and eats the margin in silence | a distribution **fitted to your real tokens** + **CVaR**: the bad month has a price *before* it arrives |
| **SaaS at scale** | every AI feature is a project fighting for the same roadmap | **five methods** elect which one ships — and **robustness** says whether 1st place survives a 2-point error in a weight |
| **Startup raising** | the investor doesn't buy *"we use AI"* | they buy **NPV, IRR, payback and `P(NPV<0)`** — and the **pitch deck comes out ready**, in LaTeX |

**What actually changes.** Your gross margin stops being an estimate and becomes a **distribution with a priced
tail**. Your runway stops being simple division and gains a **VaR**: *"in 19 out of 20 scenarios, my cash lasts
at least N months."* And when the board deck or the due diligence comes, you don't open a spreadsheet nobody can
reproduce — you open a number with a **fixed seed**, that any co-founder, investor or auditor reruns and gets
**exactly the same**.

> **A brutal repositioning:** the solopreneur starts deciding like a CFO. And the CFO starts deciding at the
> speed of a solopreneur.

> **The promise:** turn whoever *pays for AI* into whoever *profits from AI* — and whoever *uses AI* into whoever
> **pioneeringly masters, measures and multiplies it**. With numbers, not with faith.

---

## 📈 The evidence (Gartner · IDC · PwC · McKinsey · MIT)

Don't take my word for it. **Take the word of the institutes that have studied this for decades** — and whose
verdict is unanimous: **AI creates immense value, but only delivers for those who measure and govern.** Those
who "use AI without mastering it" become an abandonment statistic; those who instrument the return **keep the
prize**.

- 🧭 **Gartner** — predicted that **≥ 30% of generative-AI projects would be abandoned after proof of concept by
  the end of 2025**, with **unclear business value** as the central cause (plus poor data, escalating costs and
  weak controls). *→ without measurement, the project dies in the pilot.*
- 🔬 **MIT** (report *"The GenAI Divide / State of AI in Business 2025"*, NANDA initiative) — widely reported that
  the **vast majority of enterprise GenAI pilots deliver no measurable P&L impact**; the minority that delivers
  value combines AI with **process and measurement**. *→ the difference is measuring, not adopting.*
- 💵 **IDC** (study *"The Business Opportunity of AI"*, sponsored by Microsoft) — organizations that **measure and
  optimize** reported a return on the order of **several dollars for each US$ 1** invested in AI, with wide
  dispersion between leaders and laggards. *→ ROI exists — and favors those who instrument.*
- 🌍 **PwC** (*"Sizing the Prize"*) — estimates AI could add up to **~US$ 15.7 trillion** to the global economy by
  2030; but the prize goes to those who **capture** the value, not merely consume it. *→ the pie is huge; the
  slice belongs to those who measure.*
- 🏆 **McKinsey** (*"The State of AI"*) and **BCG × MIT Sloan** — a minority group of **"AI high performers"**
  captures disproportionate return; the turning point is when AI is coupled to **metrics, governance and
  reinvestment** where the return is proven. *→ winners measure, prioritize and reallocate.*

> **This is exactly the divide this framework crosses:** it moves you off the side that *abandons at the pilot*
> and onto the side with **actual, proven results** — with BSC, investment analysis and multi-criteria decision.

> ⚠️ **Honesty note (read this):** the figures above reflect real headlines from these institutes, but **reports
> and percentages are updated** — confirm the exact values and year in the **primary sources** (Gartner Newsroom;
> IDC/Microsoft *Business Opportunity of AI*; PwC *Sizing the Prize*; McKinsey *State of AI*; MIT *State of AI in
> Business*) before citing them in official material. Here they serve as **directional grounding**, not a
> numerical guarantee.

---

## 💥 The cost of inaction (do the math nobody does)

A **PRO AI** subscription costs between **US$ 20 and US$ 200 per month, per seat**. Multiply by the number of
people on your team. Multiply by 12 months. Now apply what the institutes have **already proven**: **Gartner**
projects **≥ 30% abandonment** and **MIT** shows the **majority of pilots don't return**. A huge slice of that
total isn't investment — it's **pure bleeding**.

> **Straight example (swap in your own numbers):** 10 seats × US$ 30/month × 12 = **US$ 3,600/year**. If ~30%
> becomes invisible waste, that's **~US$ 1,080/year evaporating** — from ONE small team, in ONE year. With your
> real number, the shock is bigger.

And here's the part that hurts: **this cost compounds and doesn't wait.** Every month without measuring is a
month of leakage that **won't come back** — while the competitor who instrumented is already **reallocating
capital to what pays off**. First-mover advantage is built early: **whoever measures first, scales first.**

The lowest-cost moment to start was yesterday. The second best is **now** — and it costs **US$ 0** and **5
minutes**. The question isn't *"can I afford to measure?"*. It's ***"how much longer can I afford NOT to?"***

---

## ✨ Features

- **📊 KPIs (4 BSC perspectives) + API economy:** maturity, human capital, financial and token efficiency —
  `IEET`, `IOLI`, `ITR`, `IITA`, `PEUC`, `ICCA`, `IDLS`, `IBMT` — plus **EVM** (CPI/SPI/EAC).
- **🪙 Frontier concepts:** **VRT/kTR** (tokenizable cost-recovery unit — *"Gitman's m²"*) and **PSR** (Project
  Score 0–5 ⭐) to rank the health of each project.
- **🔬 Operational diagnostics:** **VRT in 5 blocks**, **HCI** (critical interruption hour), **Lean Six Sigma
  wastes** (weighted tokens) and **hallucination RCA by prompt taxonomy** (bottleneck per project + intersection).
- **💰 Full financial suite:** **NPV, IRR, MIRR, EAA (Net Uniform Value), PI, Payback** (simple & discounted),
  **dollarization** and comparison with **SELIC** and the **US interest rate**.
- **🏆 Multi-criteria decision (5 methods):** **DEMATEL** (causal structure + influence-derived weights) feeding
  **ELECTRE I · PROMETHEE II · MAUT · MCDA-C · AHP-TOPSIS 2n**, with **Borda consensus** and an **administrative
  dossier** (SWOT, PESTELC, 5W4H, Pareto, GUT, Radar).
- **🎲 Risk (Monte Carlo):** **10,000 iterations** per project, **20 distributions**, correlation
  matrix (Iman-Conover), **P(NPV<0)**, **VaR/CVaR 5%**, percentiles 1–99% and a **tornado** (regression + correlation).
- **🗺️ C-Level visuals:** **interactive 5D map**, depth donuts, sustainability quadrant, trends and LaTeX **pitch decks** for eligible projects.
- **⚙️ Real pipeline:** **Langfuse → SQLite → Evidence**, with **asynchronous concurrent** sync and classification accelerated in **Rust (PyO3)**.
- **💳 AI FinOps:** **subscription plan** catalog (OpenAI, Anthropic, Google, Perplexity, xAI, Mistral, DeepSeek,
  Kimi, Qwen…) with **FX + IOF** and an allocation base (burn rate).
- **🌐 12 languages** in the dashboard **and inside the chart images** (incl. Devanagari, Hebrew and CJK).
<!-- eixo-execucao -->
- **📅 Monte Carlo schedule (PERT) + Gantt:** the same Monte Carlo engine aimed at **task durations** — distribution of the finish date, **P80** (the commitment the PMI recommends), `P(on time)` and the **critical path** with a **criticality index** (in what % of the 10,000 simulations each task is critical — what deterministic CPM hides).
- **📐 Earned Value Management + Earned Schedule:** **SPI · CPI · EAC · ETC · VAC · TCPI** and the **S-curve** (PV/EV/AC). Unites **cost + schedule + scope** in one frame. **SPI(t)** fixes the known flaw of SPI, which converges to 1 at the end even when the project is late.
- **⚙️ AI execution health over time:** latency **p50/p95/p99** against an **SLO**, **token budget burndown**, **quality regression** (SPC-style rule) and **model drift** via **Kolmogorov-Smirnov** — all from **real** Langfuse logs.
- **🚨 Risk register + Probability × Impact matrix:** the *qualitative* risk every PMO asks for, with owner, trigger and mitigation. Probabilities are **anchored in real signals** (SLO breaches, CPI, drift), not guesswork.
- **🌊 Flow metrics (Kanban):** **CFD**, **cycle time P50/P85** (percentile forecasting, not guessing), **throughput** and **WIP**.

---

## 📸 Screenshots (anonymous dashboard)

> 100% anonymous demo (projects shown as *Project A…J*). Real data/names never ship with the package.

**🌐 Portfolio 5D map** — 5 dimensions per project: **X**=tokens · **Y**=PEUC (quality) · **Z**=PSR (health) ·
**size**=Burn Rate · **color**=ICCA (sustainability). *Where to scale? Right/back, high and green. Where to cut?
Large and red.*

![AI project portfolio 5D map](docs/screenshots/5d-portfolio-map.png)

**🏆 "Crown Jewel" dossier** (project elected by AHP-TOPSIS) — generated by a concurrent Python pipeline:

| SWOT | Competitive radar |
|---|---|
| ![SWOT](docs/screenshots/swot.png) | ![Competitive radar](docs/screenshots/radar.png) |

| PESTELC (macro-environment) | GUT matrix (prioritization) |
|---|---|
| ![PESTELC](docs/screenshots/pestel.png) | ![GUT](docs/screenshots/gut.png) |

| 5W4H (action plan) | Failure Pareto (80/20) |
|---|---|
| ![5W4H](docs/screenshots/5w4h.png) | ![Pareto](docs/screenshots/pareto.png) |

### 📅 Execution axis — schedule, earned value, AI health, risk and flow

**Gantt with critical path** — red bars are the critical path; the **%** on each task is the *criticality index*: in what percent of the 10,000 simulations that task drove the deadline.

![Gantt with critical path — red bars are the critical path; the % on ea](docs/screenshots/cronograma-gantt.png)

**Schedule risk** — the distribution of the finish date, with the deadline, **P50** and **P80** marked. Commit to P80, not to the deterministic estimate (optimistic because of merge bias).

![Schedule risk — the distribution of the finish date, with the deadline](docs/screenshots/cronograma-risco-prazo.png)

**EVM S-curve** — PV (planned) · EV (earned) · AC (actual cost). EV below PV means late; AC above EV means over budget.

![EVM S-curve — PV (planned) · EV (earned) · AC (actual cost). EV below ](docs/screenshots/evm-curva-s.png)

**Latency under SLO** — p50/p95/p99 per day, from real logs. Cross the line and the service degraded.

![Latency under SLO — p50/p95/p99 per day, from real logs. Cross the lin](docs/screenshots/exec-latencia-slo.png)

**Risk matrix P × I** — bubble = exposure (P×I). Probability anchored in the project's real signals.

![Risk matrix P × I — bubble = exposure (P×I). Probability anchored in t](docs/screenshots/risco-matriz-pi.png)

**Cumulative Flow Diagram** — parallel bands = healthy flow; a fattening band = bottleneck / stuck WIP.

![Cumulative Flow Diagram — parallel bands = healthy flow; a fattening b](docs/screenshots/fluxo-cfd.png)

---

## 🚀 Quick start (demo, no Langfuse)

**Zero risk. Zero cost. 5 minutes.** Run it on your machine and see the full dashboard with anonymous data:

```bash
cd foundations/pipeline
pip install -r requirements.txt
cd ../evidence && npm install && cd ../pipeline
./run_all.sh --mock          # anonymous data (Project A..J) -> KPIs -> NPV/MIRR/EAA -> 5D -> pitch decks -> dashboard
cd ../evidence && npm run dev # http://localhost:3000
```

For **real data**, fill `foundations/pipeline/.env` with **your own** Langfuse keys (see
[`SETUP.md`](foundations/pipeline/SETUP.md)) and run `./run_all.sh`. Each user uses their **own account** — no
author keys ship with the package.

---

## 🏗️ Architecture

```
     Your AI apps                Observability          Analytics-as-Code            You
 (ChatGPT, Claude, API…)   ┌──────────────┐   ┌──────────────────┐   ┌──────────────────────┐
        │ traces           │   Langfuse   │   │  SQLite (schema  │   │  Evidence (BI as     │
        └─────────────────▶│  (SDK v4)    │──▶│  + KPI queries)  │──▶│  Code) · 12 languages│
                           └──────────────┘   └──────────────────┘   └──────────┬───────────┘
   async concurrent sync            classification in Rust (PyO3)              │
                                                                    ┌───────────┴───────────┐
                                                                    │ AHP-TOPSIS · Dossier  │
                                                                    │ 5D · Pitch decks (TeX)│
                                                                    └───────────────────────┘
```

**Stack:** Python 3.13 · SQLite/DuckDB · Evidence.dev (SvelteKit) · Rust + PyO3 + maturin · matplotlib ·
tectonic (LaTeX) · Noto/WenQuanYi fonts for image i18n.

---

## 📊 KPI catalog (70+)

Sample (full catalog in [`foundations/KPIs_Lean6s_BSC.md`](foundations/KPIs_Lean6s_BSC.md)):

| Acronym | Name | What it answers |
|---|---|---|
| **PSR** | Project Score Rating (0–5) | Overall AI-project health |
| **PEUC** | % of Useful Delivery per Consumption | How much of the spend became useful delivery |
| **IITA** | Hallucinated-Token Incidence Index | % of hallucination/rework |
| **IDLS** | Lean Waste Index | Muda (tokens weighted by severity) |
| **VRT/kTR** | Tokenizable Recovery Value | "Gitman's m²" — cost per 1k tokens |
| **ICCA** | Subscription Cost Coverage Index | Does it cover the cost? (>3× healthy) |
| **CPP** | Cost per Progress Point | Master indicator (lower is better) |

---

## 💰 Investment-grade financial analysis

Each project becomes an **investment thesis**: from your cash flow (CSV), the framework computes **NPV**, **IRR**,
**MIRR (reinvests at the project rate)**, **EAA (equivalent annual annuity of NPV)**, **PI (profitability index)**
and **Payback** (simple/discounted) — **dollarizing** the flow and comparing with **SELIC** and the **US interest
rate**. It generates a LaTeX **pitch deck** for every project with **NPV > 0 and PI > 1** in both BRL **and** USD.
The goal is brutally practical: **find out whether your AI subscription pays for itself — and how fast.**

---

## 🏆 Multi-criteria decision (AHP-TOPSIS 2n) + Crown Jewel dossier

With several projects, which to scale first? The **AHP-TOPSIS 2n** model weights the indicators as criteria
(weights via **AHP** with consistency ratio **CR ≤ 0.10**) and ranks by **TOPSIS** across **two normalizations**
(vector + min-max), reporting **robustness** (agreement between normalizations). The winner — the **"Crown
Jewel"** — receives a full **administrative dossier** (SWOT · PESTELC · 5W4H · Pareto · GUT · Radar) generated
from scratch by code, with an executive **Bottom-Line** and honest **C-Level insights**. **You don't present a
spreadsheet. You present a verdict.**

---

## 🎲 Monte Carlo — the risk the average hides

A positive NPV **on average** protects no one. The average is the most comfortable lie in finance: it describes a
scenario that may never happen. What decides your fate is the **tail** — the bad day.

This framework simulates **10,000 futures** for each project: every cash flow becomes a **random variable** and the whole portfolio is recomputed iteration
by iteration. In the end you don't have a number — you have **the entire distribution of your money**:

- **`P(NPV < 0)`** — the real probability of loss. The number nobody shows you.
- **VaR 5%** — the worst plausible scenario: *"in 19 out of 20 futures, I make at least this much."*
- **CVaR 5%** — when disaster strikes, how much it costs on average.
- **Sensitivity tornado** — multiple regression and Pearson correlation: which variable actually moves your NPV.
- **20 input distributions**, a validated **correlation matrix** (Iman-Conover, which preserves the exact marginals)
  and **percentiles from 1% to 99%**, with a 100-bin histogram.

Fixed seed: run it again and you get **exactly** the same result. Auditable — not "magic".

> **The turn:** you stop picking the project with the highest NPV and start picking **the one that survives the bad
> scenario**. That is risk management — what separates the investor from the gambler.

![Histograma de Monte Carlo do VPL — 10.000 iterações, 100 classes](docs/screenshots/mc-histograma.png)

| Cumulative distribution of NPV | Sensitivity tornado |
|---|---|
| ![Cumulative distribution of NPV](docs/screenshots/mc-acumulado.png) | ![Sensitivity tornado](docs/screenshots/mc-tornado.png) |

---

## 🧮 Five schools of decision. One verdict.

One method can be wrong. Five methods agreeing cannot.

Following the architecture of **John (2025)** — *Integration of DEMATEL with Other MCDM Methods* — **DEMATEL** maps the
causal structure among criteria and separates **causes** (levers to act on) from **effects** (thermometers of what was
already done). From those influence loops the **weights** are born: not arbitrated, but **derived from the structure of
the problem**. They feed four rival schools:

| Method | School | What it asks |
|---|---|---|
| **ELECTRE I** | Outranking | "Who outranks whom — and who survives undominated?" |
| **PROMETHEE II** | Outranking | "What is each project's net preference flow?" |
| **MAUT** | Utility | "Which maximizes the utility of a risk-averse decision-maker?" |
| **MCDA-C** | Constructivist | "Who is above the *Good* level — and who is below *Neutral*?" |
| **AHP-TOPSIS 2n** | Distance to ideal | "Who is closest to the ideal solution under both normalizations?" |

The winner comes from the **Borda consensus** of the five, already **risk-adjusted** by Monte Carlo. And when the
methods **disagree**, the dashboard shows the disagreement — because that is information: the choice is sensitive to the
decision school and deserves the decision-maker's eye.

| DEMATEL — causes × effects | Rank by method |
|---|---|
| ![DEMATEL — causes × effects](docs/screenshots/dematel.png) | ![Rank by method](docs/screenshots/mcdm-metodos.png) |

### 💼 What changes in your day — from freelancer to corporation

It doesn't matter whether you pay **US$ 20 on a PRO plan** or **US$ 200k in enterprise contracts**: the math of waste
is the same — only the number of zeros changes.

| | **SMB / freelancer** | **Large enterprise** |
|---|---|---|
| **The real pain** | 3 subscriptions, zero visibility, tight cash | 40 AI pilots, none with attributed P&L |
| **Monte Carlo delivers** | *"this project has a 12% chance of losing money, and the bad month costs US$ 3.4k"* | VaR/CVaR per business unit: aggregate, auditable risk — not anecdote |
| **MCDM delivers** | which of the 3 projects to scale **first**, with the money you actually have | which of the 40 pilots becomes a product — defensible in committee, method explicit |
| **The next-day gain** | cancel the subscription that doesn't pay for itself, this week | reallocate budget on **evidence**, not on internal politics |

**In practice:** the **tornado** points to the variable that moves the result — that is, **where to invest your next
hour of work**. **DEMATEL** reveals that cutting hallucination (IITA) is a **cause**, not a symptom: act there and NPV,
IRR and risk improve *together*. This is AI management ceasing to be opinion and becoming **engineering**.


---

## 🔬 The signal is upstream — and that is where the leverage lives

I found this by measuring the framework itself: the NPV sensitivity tornado returned **exactly**
`1.0 · 0.9091 · 0.8264 · 0.7513…` — the discount factors `1/(1+i)ᵗ`. Because NPV is **linear** in the cash flows,
simulating only the flows tells you nothing beyond the rate. **The real stochastic signal is upstream: in the tokens.**

### 1️⃣ Stop arbitrating the distribution. Fit it to your data.

Eleven candidate distributions are fitted by **maximum likelihood** to your real token-consumption series
(`logs_langfuse`). The one with the **lowest AIC** wins — AIC penalizes each extra parameter and prevents
overfitting — and the **Kolmogorov-Smirnov** test measures goodness of fit. This is the classic *fit-distributions-to-data* step, and it is what reveals the **heavy tail** of consumption: some prompts cost 10× the typical one, and that
tail is what blows up the budget — invisible to anyone using the mean.

**And when the fit is bad, the framework shouts.** If the KS p-value drops below 0.05, the screen warns
`WEAK FIT` in red instead of faking precision. An honest number beats a pretty one.

![Fitting distributions to real tokens — 11 candidates, AIC selection, Kolmogorov-Smirnov goodness of fit](docs/screenshots/ajuste-distribuicoes.png)

### 2️⃣ Does your ranking survive a 2-point error in a weight?

Every multi-criteria method returns a winner with an **implicit 100% confidence**. But criteria weights are
estimates, not revealed truths. If two percentage points on the IITA weight swap 1st and 2nd place, the "winner" is
an artifact of the calibration.

So we perturb the DEMATEL weights with a **Dirichlet** — `w' ~ Dir(κ·w)`, which lives exactly on the simplex and
preserves `E[w'] = w`, perturbing **without bias** — and re-rank **2,000 times**. The verdict changes nature:

> *"Project C is the best"* ⟶ **"Project C wins in 99.9% of plausible preference universes"**

That is a **confidence interval on the decision itself**. And it exposes what the consensus was hiding: in the
screen below, **PROMETHEE II elects the leader in only 25.4% of universes**. Four schools agree; one flatly
dissents. That is not noise — it is the warning that the choice depends on whether you prefer *outranking* over
*utility*. No single ranking would ever tell you that.

![Ranking robustness via Dirichlet perturbation — win probability and disagreement between schools](docs/screenshots/robustez-dirichlet.png)

### ⚡ The concrete leverage

| Resource | Before | After |
|---|---|---|
| **Time** | weeks arguing about which project to scale | the verdict arrives with a probability — the argument ends in one meeting |
| **Processing** | 10,000 iterations × 10 projects, vectorized in NumPy | seconds, on your machine, no cloud and no cost |
| **Capital** | budget allocated by conviction | allocated by `P(win)` and `VaR` — with the worst case already priced |
| **Reputation** | *"I think this one is best"* | *"it wins in 99.9% of scenarios; and here is the method that dissents, and why"* |
| **Auditability** | a spreadsheet nobody can reproduce | fixed seed: anyone reruns it and gets **exactly** the same number |

### 💼 From the US$ 20 plan to the US$ 200k contract

**If you are a freelancer or SMB:** the fitted distribution tells you **what the bad token month will cost** before
it arrives — and the robustness tells you whether it's really worth moving effort to the other project, or whether
both are tied inside the margin of error. You stop optimizing in the dark with tight cash.

**If you are a large enterprise:** `P(win)` is the missing piece in the investment committee. It turns *"team A
champions project X"* into **"project X wins under 99.9% of defensible weight calibrations, and the only dissenting
school is outranking, on criterion Y"**. Political debate becomes **technical debate** — and the CFO gets a number
that survives audit.

> **The final turn:** the framework stops measuring the risk of the **money** and starts measuring the risk of the
> **decision itself**. Very few places in the world do this.

---

## 🎓 Foundations: what Monte Carlo is, and what Multi-Criteria Decision is

### 🎲 Monte Carlo mathematical simulation

#### 📖 The concept

Monte Carlo is a numerical method that answers questions about uncertain systems **through random sampling**. The idea
inverts the mathematician's instinct: instead of deducing the answer in **closed form** — solving the integral, the
combinatorics, the differential equation — you build a **model**, draw thousands of realizations of the uncertain
variables and simply **count what happened**. What you get in the end is not a number: it is the **probability
distribution of the outcome**.

Two laws hold it up. The **Law of Large Numbers** guarantees that the average of the simulations converges to the true
value. The **Central Limit Theorem** tells you how fast: the standard error falls as `1/√N`. The consequence is honest
and slightly cruel — **to double the precision you must quadruple the iterations**. Monte Carlo is not fast. Its virtue
is elsewhere: the error **does not depend on the dimension of the problem**. Deterministic quadrature methods suffer
the *curse of dimensionality* and collapse with dozens of variables; Monte Carlo does not. It wins exactly where
analytical mathematics dies.

#### 📖 Where and when it arose

**Los Alamos, New Mexico, 1946.** The Polish mathematician **Stanisław Ulam** was convalescing from encephalitis and
spent his days playing solitaire. He wondered what the probability of winning a game was. He tried the combinatorics
and gave up: intractable. Then something occurred to him so simple it looked like cheating — **play a hundred games,
count how many you win, and divide**. He realized at once that this was no card-table trick: it was a **general method
of integration** for problems nobody knew how to solve.

He took the idea to **John von Neumann**, who immediately saw its application to the problem consuming them in the
Manhattan Project: **neutron diffusion** in fissile material. Simulating the random walk of thousands of neutrons —
scattering, absorption, fission — was feasible; solving the transport equation was not. **Nicholas Metropolis**
proposed the name **"Monte Carlo"**, after the Monaco casino where an uncle of Ulam's used to borrow money to gamble.
The **ENIAC** made the first computations possible, and in **1949** Metropolis and Ulam published *"The Monte Carlo
Method"* in the *Journal of the American Statistical Association*.

The method was born, literally, of the meeting between a **card game** and the **atomic bomb**. Few scientific ideas
have such a disconcerting birth certificate.

#### 📖 The methodology, in five steps

1. **Model.** Write the output as a function of the inputs: `y = f(x₁, …, xₙ)`.
2. **Assign distributions.** Every uncertain input gets a distribution. If **historical data** exists, it is *fitted*
   to them; if not, it is asserted — and that must be **declared**.
3. **Sample.** Draw `N` scenarios. If the variables are **correlated**, the sampling must respect that structure:
   drawing independently where real dependence exists is the method's most common error.
4. **Propagate.** Compute `f` in each scenario. This is where the uncertainty of the inputs **becomes** the uncertainty
   of the output, with no linear approximation.
5. **Analyze.** Study the resulting distribution: mean and deviation, **percentiles**, probability of events
   (`P(y < 0)`), the **tail** (VaR, CVaR) and the **sensitivity** (which `xᵢ` moves `y`).

#### 📖 Uses and applications in the world

- **Finance:** pricing exotic options (where no closed form exists), portfolio **VaR** and **CVaR**, regulatory stress
  tests (Basel), credit risk.
- **Engineering:** structural reliability, manufacturing tolerances, failure analysis in complex systems.
- **Project management:** schedule and cost risk (the probabilistic evolution of PERT), completion S-curves.
- **Physics and chemistry:** particle transport, radiation shielding, statistical mechanics.
- **Operations and supply chains:** queues, inventories, capacity under uncertain demand.
- **Epidemiology:** disease spread and policy evaluation under uncertainty.
- **Inside AI itself:** **MCMC** (Bayesian inference), **MCTS** — the tree search that took AlphaGo past Lee Sedol —
  and *Monte Carlo dropout* for estimating uncertainty in neural networks.

#### 🔒 Methodology, use and application EXCLUSIVE to this project

Here Monte Carlo is no academic ornament: it is the **risk engine** of the portfolio.

- **The inputs.** Each periodic cash flow becomes a **Triangular** variable (`min`, `mode`, `max`), with mode at the
  deterministic value and tails at ±30%. Token consumption — the one genuinely heavy-tailed variable — is **not
  asserted**: eleven candidate distributions are **fitted by maximum likelihood** to your real `logs_langfuse` series,
  the one with the **lowest AIC** wins, and goodness of fit is measured by **Kolmogorov-Smirnov**. If the p-value drops
  below 0.05, the screen prints `WEAK FIT` in red instead of faking precision.
- **The correlation.** When flows are dependent, sampling uses **Iman-Conover**, which imposes rank correlation while
  **preserving the marginal distributions exactly**. The matrix is validated first: symmetric, unit diagonal, positive
  definite.
- **The propagation.** **10,000 iterations** per project, with a **fixed seed (42)**: run it again and you get exactly
  the same number. That is not a detail — it is what makes the result **auditable** by a partner, an investor or an
  auditor.
- **The outputs.** Not only NPV: we simulate **NPV, IRR, MIRR, EAA, PI** and the **token cost**, each with the ten
  classic descriptive statistics (skewness and kurtosis under Excel's definitions), **percentiles from 1% to 99%** and
  a **100-bin histogram**.
- **The risk that matters.** `P(NPV < 0)` is the real probability of loss. **VaR 5%** is the worst plausible scenario —
  *"in 19 out of 20 futures I make at least this much"*. **CVaR 5%** answers what nobody asks: when disaster strikes,
  **what does it cost on average**.
- **The sensitivity.** The **tornado** is computed in both classic forms: the **betas of a multiple regression** (the
  effect of +$1 on an input over NPV) and the **Pearson correlation** (how much that input's uncertainty dictates NPV's
  uncertainty). They are complementary readings; the dashboard shows both.
- **A discovery by the framework about itself.** Measuring itself, the tornado returned betas **exactly equal to the
  discount factors** `1/(1+i)ᵗ` — because NPV is *linear* in the flows. Simulating only the flows therefore tells you
  nothing beyond the rate. **The real stochastic signal is upstream, in the tokens.** That finding is what motivated
  fitting distributions to real data.
- **Risk feeds the decision.** Two Monte Carlo outputs enter as **criteria** in the multi-criteria model: `P(NPV<0)` as
  a **cost** criterion and **VaR 5%** as a **benefit** criterion. The final choice is therefore born **risk-adjusted**,
  not merely expectation-adjusted.


**What it is.** A method that answers hard questions **by drawing lots**. Instead of solving the mathematics of an
uncertain system in closed form — often impossible — you assign **probability distributions** to the input
variables, draw thousands of scenarios, compute the outcome in each one and observe the **entire distribution** of
outputs. The Law of Large Numbers guarantees convergence; the error falls as `1/√N`, meaning **quadrupling the
iterations halves the error**.

**How it was born.** Los Alamos, 1946. **Stanisław Ulam**, convalescing from an illness, was playing solitaire and
wondered what the probability of winning was. He realized that solving the combinatorics was brutal — but
**simulating** hundreds of games and simply counting was trivial. He took the idea to **John von Neumann**, and the
two applied it to the problem occupying them in the Manhattan Project: **neutron diffusion** in fissile material.
**Nicholas Metropolis** named the method "Monte Carlo", after the Monaco casino where an uncle of Ulam's used to
gamble. The **ENIAC** made the first computations feasible. The method was born, literally, from the meeting of a
card game and the atomic bomb.

**Where it is used today.** Option pricing and **VaR** in finance; structural reliability in engineering; schedule
and cost risk in project management; particle physics; supply chains; epidemiology. And inside AI itself: **MCMC**
(Bayesian inference) and **MCTS** — the tree search that took AlphaGo past Lee Sedol.

**How it serves us here.** Every cash flow of your project becomes a random variable, and token consumption gets the
distribution **fitted to your real data**. We run 10,000 scenarios and, in the end, you don't have an NPV — you have
**the distribution of your money**: `P(NPV < 0)` (the real chance of loss), **VaR 5%** (the worst plausible
scenario), **CVaR 5%** (what it costs when disaster strikes) and the **tornado** (which variable actually moves the
result). The mean lies; the tail decides.

### 🧮 Multi-Criteria Decision Analysis (MCDA)

#### 📖 The concept and what it is for

Choosing between projects is hard for two reasons no spreadsheet solves. First, criteria **conflict**: the
highest-NPV project is usually the riskiest. Second, they are **incommensurable**: there is no honest arithmetic that
adds dollars to a hallucination percentage and hours of rework.

MCDA (*Multi-Criteria Decision Analysis*) is the field — born in the 1960s-70s at the frontier of operations research
and decision theory — that confronts exactly this. It **does not promise the right answer**. It promises something more
useful: to make the choice **explicit, auditable and defensible**.

Its founding thesis is uncomfortable and liberating at once: **there is no "best" in a vacuum.** There is a best *given
a preference system someone made explicit*. Every decision-maker already operates with a preference system — the
difference is that, without MCDA, it is **implicit, inconsistent and unauditable**. Trading tacit opinion for an
explicit model: that is the entire gain.

#### 📖 Uses and applications in the world

Supplier selection and portfolio prioritization; choice of energy technologies (solar × wind × biomass); siting of
plants, hospitals and landfills; environmental impact assessment; public policy and budget allocation; personnel
selection; maintenance prioritization; and — increasingly — **techno-economic assessment** of emerging technologies,
which is exactly the case of an AI project portfolio.

#### 📖 The three schools of decision

- **American school (value and utility).** Aggregates everything into a **single number**. Assumes a bad score on one
  criterion can be **compensated** by great scores on others. Simple, powerful — and sometimes dangerous. `AHP`, `MAUT`.
- **European school (outranking).** Founded by **Bernard Roy**. Accepts that two alternatives may be **incomparable**
  and admits the **veto**: catastrophic performance on one criterion **is not bought off** by excellence elsewhere. It
  models the decision-maker's real hesitation through **thresholds**. `ELECTRE`, `PROMETHEE`.
- **Constructivist school.** The model is not *discovered*, it is **built together with the decision-maker**, through
  problem structuring and scales anchored on reference levels. `MCDA-C`.

#### 📖 1. DEMATEL — *Decision-Making Trial and Evaluation Laboratory*

**What it is.** Created by **Gabus & Fontela** at the **Battelle Memorial Institute** (Geneva, 1972-73) to study complex,
entangled world problems. It **does not rank alternatives**: it maps the **causal structure among criteria**.

**How it works.** Experts fill a **direct-relation matrix** `Z` (how much criterion *i* influences *j*, from 0 to 4). It
is normalized by `s = max(largest row sum, largest column sum)`, giving the **total-relation matrix** `T = X(I − X)⁻¹`,
which sums direct influence **and all indirect influence**, along any path. From it come `R` (row sums) and `C` (column
sums): **`R+C` is prominence** (importance in the system) and **`R−C` is relation** (positive = **cause**; negative =
**effect**).

**General use.** Sustainable supply chains, barriers to technology adoption, systemic risk analysis.

**🔒 In this project.** DEMATEL answers the question that **precedes** the ranking: *"where should I act?"*. It reveals
that **IITA (hallucination), PSR (health) and IDLS (Lean waste) are CAUSES**, while **NPV, IRR, PI and the risk metrics
are EFFECTS**. It is counterintuitive and liberating: chasing NPV is pointless — NPV is a **thermometer**. Act on
hallucination and NPV, IRR and risk improve *together*. Moreover, the criteria **weights** are not asserted: they are
**derived from the influence structure**, via `wᵢ ∝ √((R+C)ᵢ² + (R−C)ᵢ²)`. Those weights feed the **other five methods**
— the integration pattern described by John (2025).

#### 📖 2. AHP-TOPSIS 2n — *Analytic Hierarchy Process* + *Technique for Order Preference by Similarity to Ideal Solution*

**What it is.** **Saaty (1977)** proposed AHP: derive weights from **pairwise comparisons** between criteria, with a
**consistency test** that exposes contradictory judgments (`CR ≤ 0.10`). **Hwang & Yoon (1981)** proposed TOPSIS: the
best alternative is the one **closest to the ideal solution** and **farthest from the anti-ideal**.

**How it works.** Normalize the decision matrix, multiply the columns by the weights, compute Euclidean distances to the
ideal and anti-ideal solutions, and the **closeness coefficient** `Ci = d⁻/(d⁺+d⁻)` orders everything.

**General use.** The most widely used pair in MCDM worldwide — from supplier selection to performance evaluation.

**🔒 In this project.** We run TOPSIS under **two normalizations** — vector (Euclidean) and min-max (linear) — hence the
**"2n"**. Each project gets two coefficients and the final ranking is the average. What we gain is a measure almost
nobody reports: the **agreement between the normalizations**. When the two disagree about a project's position, that
project's result is **fragile to an arbitrary technical choice** — and the dashboard shows it. This project's Saaty
matrix has `CR = 0.0119`, well below the 0.10 limit.

#### 📖 3. ELECTRE I — *ÉLimination Et Choix Traduisant la REalité*

**What it is.** **Bernard Roy (1968)**, at the SEMA consultancy in Paris. It is ground zero of the European outranking
school. The question is not *"what is each one's score?"* but *"is **a** at least as good as **b**?"*.

**How it works.** For each pair `(a, b)` two indices are computed. **Concordance** `C(a,b)` sums the weights of the
criteria on which `a` is at least as good as `b`. **Discordance** `D(a,b)` measures `a`'s **greatest disadvantage**
against `b`. We say `a` **outranks** `b` if concordance is high **and** discordance is low. The set of alternatives
**nobody outranks** is the **kernel** — the menu of defensible choices.

**General use.** Public and environmental decisions, where compensating a catastrophic criterion would be unacceptable.

**🔒 In this project.** ELECTRE is the method that **refuses to lie for convenience**. A project with a stratospheric NPV
and scandalous hallucination **does not buy** its place: **discordance** bars it. The framework reports the **kernel** —
the projects no other dominates — and uses as score the **net outranking degree** (how many it dominates, minus how many
dominate it). It is also the only one of the six that is allowed to say: *"these two projects are simply
**incomparable**"*.

#### 📖 4. PROMETHEE II — *Preference Ranking Organization METHod for Enrichment Evaluation*

**What it is.** **Jean-Pierre Brans (1982)**, refined with **Bernard Mareschal and Philippe Vincke (1985)**. Also
outranking, but with an elegant turn: instead of a binary threshold, it measures **how much** `a` is preferred to `b`.

**How it works.** For each criterion, the difference `d = g(a) − g(b)` passes through a **preference function** that maps
it to a degree between 0 and 1. Brans proposed **six generalized functions** (usual, quasi-criterion, preference
threshold, level, linear with indifference, Gaussian), parameterized by an **indifference threshold `q`** (below which
the difference is irrelevant) and a **preference threshold `p`** (above which preference is total). The weighted degrees
are summed: `φ⁺` is how much `a` dominates the others, `φ⁻` how much it is dominated, and the **net flow**
`φ = φ⁺ − φ⁻` yields a **complete preorder** (PROMETHEE II).

**General use.** Energy, logistics, health — whenever grading the **intensity** of preference matters.

**🔒 In this project.** We use the **linear with indifference** function, with `q` and `p` estimated from the 10% and 90%
quantiles of the observed deviations on each criterion. PROMETHEE answers *"by how much is the winner better?"*, not
merely *"is it better?"*. And it produced the portfolio's most interesting finding: in the robustness analysis,
**PROMETHEE II elects the consensus leader in only 25.4% of the preference universes** — while the other four schools
agree. The consensus was **masking a disagreement between schools**.

#### 📖 5. MAUT — *Multi-Attribute Utility Theory*

**What it is.** **Ralph Keeney & Howard Raiffa (1976)**, direct heirs of von Neumann and Morgenstern. It is the American
school in axiomatic form: if your preferences obey certain rationality axioms, then a **utility function** representing
them exists, and deciding means **maximizing expected utility**.

**How it works.** Each criterion gets a **utility function** `uⱼ` mapping performance into satisfaction. Global utility
is additive: `U(a) = Σ wⱼ · uⱼ(a)` — valid under **additive independence** in preference. The crucial point is the
function's **shape**: a **concave** `u` represents **risk aversion** (the second million is worth less than the first);
linear is neutrality; convex is risk-seeking.

**General use.** Medical decisions, energy policy, negotiation — any context where the attitude toward risk must be
**made explicit and defended**.

**🔒 In this project.** We use **exponential** utility `u(z) = (1 − e^(−r·z)) / (1 − e^(−r))` with aversion coefficient
`r = 2`. That is a **declared ethical choice**: the framework is **conservative**. An uncertain gain is worth less than a
certain gain of the same mean — exactly as a prudent CFO would assess it. Where TOPSIS treats all gains as fungible,
MAUT **penalizes the high, uncertain promise**.

#### 📖 6. MCDA-C — *Multicriteria Decision Aid — Constructivist*

**What it is.** Formalized by **Leonardo Ensslin, Gilberto Montibeller and Sandra Noronha (2001)**, with roots in Roy and
Bana e Costa. The premise is philosophical: the model **does not preexist** the decision-maker. It is **built with him**,
in three phases — **structuring** (cognitive maps, descriptors), **evaluation** (value functions, substitution rates) and
**recommendations**.

**How it works.** Each criterion gets a **descriptor** with levels, two of which are anchors: the **Neutral** level (below
which performance compromises) and the **Good** level (above which there is excellence). The value function is anchored:
`V = 0` at Neutral, `V = 100` at Good, and it **extrapolates** freely outside the interval.

**General use.** Organizational performance evaluation, public management, contexts where the decision-maker must **learn**
about his own problem.

**🔒 In this project.** Absent a structuring session with the decision-maker, we anchor the levels on the portfolio's
**observed quartiles**: `Neutral = Q1`, `Good = Q3`. This preserves what is unique to MCDA-C — it does not merely
**order**, it **classifies**: `V < 0` is **compromising**, `0 ≤ V ≤ 100` is **competitive**, `V > 100` is **excellence**.
A project can top the ranking and still sit in the compromising band. No other method in this set would tell you that.

#### 📖 Why five methods, and not one

Because **each school fails differently**, and a lone method returns a winner with an **implicit 100% confidence** — which
is always a lie. AHP-TOPSIS over-compensates; ELECTRE sometimes refuses to decide; MAUT depends on the shape of the
utility; MCDA-C depends on the anchors.

We run all five with the **same weights** (DEMATEL's) and close with a **Borda consensus**. Then the disagreement between
them stops being a nuisance and becomes **information**: when four agree and one flatly dissents, that is not noise — it
is the warning that your choice **depends on the decision school** you implicitly adopted.

#### 📖 The final question: does the verdict survive?

The whole edifice above rests on **weights**, and weights are **estimates**. If two percentage points on the IITA weight
swap 1st and 2nd place, the "winner" is an **artifact of the calibration**, not a fact of the portfolio.

That is why we perturb the DEMATEL weights with a **Dirichlet** — `w' ~ Dir(κ·w)`, which lives exactly on the simplex and
preserves `E[w'] = w`, perturbing **without bias** — and re-rank **2,000 times**. The verdict changes nature:

> *"Project C is the best"* ⟶ **"Project C wins in 99.9% of plausible preference universes"**

It is a **confidence interval on the decision itself**. With it, the framework stops measuring only the risk of the
**money** and starts measuring the risk of the **decision**.


**What it is and what it's for.** When you choose between projects, the criteria **conflict** (high NPV usually
comes with high risk) and are **incommensurable** (how do you add dollars to a hallucination percentage?). MCDA is
the field that makes that choice explicit, auditable and defensible. Its founding thesis is uncomfortable and
liberating: **there is no "best" in a vacuum.** There is a best *given a preference system you made explicit*.
Trading implicit opinion for an explicit model is the whole gain.

**The three schools.** The **American** one, of value and utility (AHP, MAUT): aggregates everything into a single
number. The **European** one, of outranking (ELECTRE, PROMETHEE), from Bernard Roy: accepts that two alternatives
may be **incomparable** and allows a **veto** — a terrible score on one criterion is not bought off by great scores
elsewhere. The **constructivist** one (MCDA-C): the model is not discovered, it is **built together with the
decision-maker**.

| Method | Origin | Central question | What only it brings | In the AI portfolio |
|---|---|---|---|---|
| **DEMATEL** | Gabus & Fontela, Battelle (1972-73) | *"Who influences whom?"* | separates **cause** from **effect** and derives the **weights** from the influence structure itself | shows that cutting hallucination (IITA) is a **cause** — act there and NPV, IRR and risk improve together |
| **AHP-TOPSIS 2n** | Saaty (1977) · Hwang & Yoon (1981) | *"Who is closest to the ideal solution?"* | pairwise-comparison weights with a **consistency test** (CR ≤ 0.10) | ranks under **two normalizations** and reports the agreement between them |
| **ELECTRE I** | Bernard Roy (1968) | *"Who outranks whom — and who survives undominated?"* | **incomparability** and **veto**: one terrible criterion is not bought off by great ones | isolates the **kernel** of projects no other project dominates |
| **PROMETHEE II** | Brans & Vincke (1985) | *"What is the net preference flow?"* | **six preference functions** with indifference and preference thresholds | grades *how much* better a project is, not merely *whether* it is |
| **MAUT** | Keeney & Raiffa (1976) | *"What maximizes the decision-maker's utility?"* | models **risk aversion** through concave utility | penalizes uncertain gains — a prudent decider does not pay the same for them |
| **MCDA-C** | Ensslin, Montibeller & Noronha (2001) | *"Where is the Good level, and where is Neutral?"* | **anchored value function**: `V=0` at Neutral, `V=100` at Good, with extrapolation | classifies into **compromising / competitive / excellence** rather than merely ordering |

**Why five, and not one.** Each school fails in a different way. A single method returns a winner with an **implicit
100% confidence** — always a lie. Running all five and closing with a **Borda consensus** turns the disagreement
between them into **information**: when four agree and one flatly dissents, that is not noise — it is the warning
that your choice depends on whether you prefer *outranking* over *utility*. And the **Dirichlet perturbation** of
the weights answers the final question: *"does 1st place survive a two-percentage-point error in the calibration?"*


### 🧪 The four gears: Iman-Conover, Kolmogorov-Smirnov, Dirichlet and the tornado

The two great methods above rest on four smaller parts — and it is in them that the difference lies between an honest
simulation and a pretty number. They are worth knowing.

#### 🔗 Iman-Conover — imposing correlation **without destroying the distributions**

**What it is.** Proposed by **Ronald Iman and William Conover (1982)**. It solves a problem that looks trivial and is
not: *how do you draw correlated variables when the marginals are not normal?* The naive route — generate correlated
normals via Cholesky and transform them — **deforms the marginals**. And if you have just fitted a LogNormal to your
data, deforming it throws away exactly the work you did.

**How it works.** It is a **rank reordering**, not a value transformation. A reference is built from the **van der
Waerden scores** `Φ⁻¹(i/(n+1))`, shuffled per column; one computes `P = chol(R)` (the target) and `Q = chol(corr(M))`
(the reference's accidental correlation); then `S = M·(Q⁻¹P)ᵀ`. Each column of the original sample is then
**reordered according to the ranks of `S`**. Because only the *order* of already-drawn values changes, the **marginal
distributions remain exact** — bit for bit.

**A fine, honest detail.** `R` is the correlation of the *normal reference*, not the Pearson correlation of the result.
The induced rank correlation follows the normal copula: `ρ_S = (6/π)·arcsin(R/2)`. For `R = 0.80` that gives **0.7859**
— exactly what we measured when testing (0.786). It is not an error of the method; it is its mathematics.

**General uses.** Financial risk (correlated assets), structural reliability, Latin hypercube sampling.

**🔒 In this project.** It is what lets us correlate the cash flows **without sacrificing** the distribution fitted to
your tokens. Before use, the matrix is validated: symmetric, unit diagonal and **positive definite** (via Cholesky). An
inconsistent correlation matrix is rejected with the smallest eigenvalue reported — instead of silently producing
meaningless numbers.

#### 📏 Kolmogorov-Smirnov — the distance between what you **assume** and what the data **say**

**What it is.** A **non-parametric** goodness-of-fit test. The statistic is simple and beautiful:
`D = sup |Fₙ(x) − F(x)|`, the largest vertical gap between the **empirical distribution function** of your data and the
**theoretical** one you proposed. Under the null hypothesis, the distribution of `D` **does not depend on which `F` it
is** — hence *distribution-free*.

**A methodological honesty caveat.** The classic KS p-value assumes the parameters of `F` were fixed **before** seeing
the data. When they are **estimated from the same data** (as here, by maximum likelihood), the test becomes
**optimistic**: it accepts too readily. Rigor would call for the **Lilliefors** correction or a **parametric
bootstrap**. We therefore treat KS as a **diagnostic**, not a proof — and use it only to **reject** bad fits, never to
declare a fit "correct".

**General uses.** Goodness of fit; comparing two samples (two-sample KS); detecting data *drift* in production machine
learning systems.

**🔒 In this project.** It measures how well the AIC-winning distribution really describes your token series. When the
p-value drops below 0.05, the screen prints **`WEAK FIT` in red** — in the demo portfolio this happens for one of the
projects, and the framework **shows it** rather than hiding it. An honest number beats a pretty one.

#### 🎲 Dirichlet perturbation — the **confidence interval of the decision**

**What it is.** The **Dirichlet** distribution is the natural distribution over the **simplex**: vectors of positive
numbers summing to 1 — exactly what a weight vector is. It is the conjugate of the multinomial and the generalization
of the Beta.

**Why it, and not Gaussian noise.** Adding normal noise to weights produces negative values and breaks the unit sum.
The Dirichlet lives *inside* the valid space. And, parameterized as `w' ~ Dir(κ·w)`, it has two properties that make it
perfect for the job: `E[w'] = w` (it perturbs **without bias**) and `Var(w'ᵢ) = wᵢ(1−wᵢ)/(κ+1)` (dispersion is
controlled by a single knob). As `κ → ∞`, it collapses onto the original weights.

**General uses.** Bayesian *prior* for proportions; Latent Dirichlet Allocation (**LDA**) in topic modeling; Rubin's
**Bayesian bootstrap** (1981); and weight-sensitivity analysis in multi-criteria decision.

**🔒 In this project.** With `κ = 200`, a 13% weight wobbles by about **±2.37 percentage points** — the plausible margin
of error of an expert judgment. We re-rank **2,000 times** and obtain `P(win)` for each project. It was this gear that
revealed the portfolio's most uncomfortable finding: the consensus is robust (99.9%), but **PROMETHEE II elects the
leader in only 25.4% of the universes**. Without the Dirichlet, that disagreement would stay invisible.

#### 🌪️ Sensitivity tornado — which variable **really** moves the result

**What it is.** A horizontal bar chart, sorted by absolute effect, answering: *among all the uncertain inputs, which
ones move the output?* The name comes from the shape — wide bars on top, narrow at the bottom.

**Two measures that look alike and are not.**
- The **beta** of a multiple regression answers: *"if this input rises by 1 unit, how much does the output rise?"* It is
  a **unit** effect, indifferent to how much that input actually varies.
- The **Pearson correlation** answers: *"how much of the output's uncertainty is dictated by this input?"* It already
  embeds the **scale of the uncertainty** (roughly `β·σᵢ/σ_y`).

A variable can have a huge beta and zero correlation: it *would* move the result a lot, but in practice it **barely
varies**. Reporting only one of the two is half the truth.

**General uses.** Project risk, financial models, reliability engineering, simulator calibration.

**🔒 In this project.** Here the tornado did something rare: it **exposed a limitation of the model itself**. Run against
NPV, the betas came out **exactly equal to `1/(1+i)ᵗ`** — the discount factors — because NPV is *linear* in the flows.
The regression tornado is, in this case, **degenerate**: it says nothing beyond the rate. It is the **correlation** that
carries the signal. And when token cost entered as a variable, its beta was `−1/(1+i)ᵗ` (cost enters with a minus sign)
and its correlation was near zero. Read together, the statement is precise and honest: *"each extra $1 in tokens takes
$0.91 off NPV — but in this project, NPV's uncertainty does not come from tokens."* Neither measure alone would say that.

---

<!-- budget-global-section -->

<!-- budget-blueprint -->

> ## 🌿 Your AI portfolio is a **biosphere** — treat it like one
>
> Stop thinking of each project as an isolated spreadsheet. **They live in the same ecosystem, and that
> ecosystem has one finite resource flowing through it: your plan's token pool.** Each project is a
> species competing for it. And like every biosphere, it obeys two laws no one can repeal:
>
> - **Carrying capacity is finite.** What one species consumes extra, another goes without. There is no
>   infinite growth in a closed pool — there is only *who is eating whose lunch*.
> - **With no brakes, the ecosystem collapses into monoculture.** The species that gains unchecked positive
>   feedback smothers all the others — and dies with them, having destroyed the diversity that fed it.
>
> **That is why this module exists.** No tool on the market — Langfuse, CloudZero, Vantage — sees the
> portfolio as a living organism: they give you *cost per project*, as if each breathed its own air. It
> doesn't. **Here you see the whole biosphere** — who thrives, who parasitises, who pays for whom, and what
> it costs to admit one more species into the ecosystem. In money, not opinion.


## 💰 Global Token Budget — every project is a COST CENTRE

**There is ONE budget: the plan you pay for.** Everything else **flows down from it**. Each project is a **cost centre** — it has **no budget of its own**. Its allowance is a **slice of the Global Budget**, and that slice is **recomputed automatically** every time a project joins or leaves the portfolio. **Nothing is created; everything is divided.**

> **The structural bug this fixed.** Each project's token budget was `consumption × 1.10` — exactly 1.100 across **all ten** projects. Circular. Self-justifying. **No project could ever go over budget, by construction.** *A budget derived from your own spend is not a budget: it's a receipt.* Today, with the quota coming from the real pool, **6 of 10 projects blow through it**.

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

### 🍩 Concept — the pool is SHARED and FINITE

**Concept.** Langfuse, CloudZero, Vantage and the rest give you **cost per project**, as if each had its own tap. **It doesn't.** There is **one contracted plan** with a finite monthly quota, and **every token one project burns is a token another will not have**. It is the **tragedy of the commons** applied to an AI budget.

**Methodology.** The Global Budget comes from the contract: `seats × US$ × FX × (1+IOF)` plus fixed infra, yielding the **monthly TCO** and the **cost per million tokens**. Real consumption comes from the logs, projected into a **monthly run-rate**. From that fall out the **quota utilisation**, the **headroom** and the **pool exhaustion date**.

**How we apply it — and the number that hurts.** **31% of consumption is WASTE**: 29 million tokens/month burned on calls that **failed and returned nothing** (hallucination, rate-limit). That is **4.7× your entire contractual headroom**. In plain words: **you would be pushed into a bigger plan because of calls that never delivered an answer.** Cutting half the waste frees more capacity than the whole headroom — **without spending a cent more**.

![Global Budget used per project (Burn Token Rate) — each slice is not 'its cost': it is the capacity it takes from the others](docs/screenshots/budget-donut-burn-token.png)

### ⚖️ Adaptive allocation and CROSS-SUBSIDY — who is paying for whom

**Concept.** Allocating **by consumption** is the market standard, and it is **self-justifying**: whoever burns most gets the biggest quota, which **legitimises the waste**. The honest allocation is by **value delivered (EV)**.

**Methodology.** Each cost centre's quota is `equal floor (50%) + value delivered (50%)`, **resized whenever N changes** — a new project has EV = 0 and, without the floor, would get **zero tokens** and could never produce value. The **cross-subsidy** is the gap between the quota it would get for what it **consumes** and the one for what it **delivers**. The subsidies sum to **exactly zero**: it is a transfer, not value creation.

**How we apply it.** The efficiency spread is **68×**: Project F delivers **642** of value per million tokens; Project J, **10**. And the allocation reveals the bill: **R$ 3,431/month — 40% of TCO — is transferred from the efficient to the inefficient, every month, in the dark.** Project F, the cheapest in the portfolio, **is paying Project J's bill**.

![Cross-subsidy — whoever consumes more than they deliver is subsidised; whoever delivers more than they consume pays the others' bill](docs/screenshots/budget-subsidio-cruzado.png)

### 🔒 PRICED contention — the causal chain applied to the PORTFOLIO

**Concept.** The causal chain links, **inside** one project: `token that drifted → risk → schedule (P80) → money`. This links **BETWEEN** projects: `one project's overrun → pool exhaustion → the OTHERS are throttled → THEIR P80 slips → THEIR Cost of Delay sends the bill`.

**Methodology.** It requires, **simultaneously**, FinOps (the quota), EVM (value delivered), risk (exposure) and a simulated schedule (the P80). That is why **no tool on the market does it** — none has the four engines together. Langfuse sees the token. Jira sees the task. CloudZero sees the invoice. **None of them can say that Project J is costing Project F R$ X in delay.**

**How we apply it — and the honesty that holds the number up.** In the throttling scenario, **Project J causes R$ 3,730 of damage to the others and only suffers R$ 853** — balance +2,877: it is the **AGGRESSOR**. **Project C, 30× more efficient, suffers R$ 867 and causes nothing** — it is a **VICTIM**. The balances sum to **zero**: every aggressor has a victim.

> ⚠️ **But today the pool FITS** (94% of quota). **There is no physical throttling** — nobody stops, nobody slips. The damage is **allocative**, not **operational**. Saying *"J is delaying C"* while the pool still has headroom would be **a lie dressed as rigour**. That is why the module is **scenario-based** and **labelled as a forecast**: it shows *at what point* the pool turns (+10% consumption → the whole portfolio stops for 0.9 days, R$ 1,497) and *what it costs when it does*.

![Priced contention — who causes the damage and who pays for it; when the pool dries up EVERYONE stops, including the efficient who caused nothing](docs/screenshots/budget-contencao.png)

### 🪓 Cut policy — if the portfolio needs room, WHO leaves?

**Concept.** This is the question the portfolio committee **can never answer**. In a finite pool, admitting project N+1 **takes tokens from all N already there** — admitting one project **dilutes everyone by 9.1%**.

**Methodology.** The honest answer is **not "the one that spends most"** — cutting by raw consumption would punish a **large, productive** project. The answer is **"the one that delivers least PER TOKEN"**: ranking by **efficiency** (EV ÷ million tokens) frees the most pool at the **least cost in value**. The `y = x` diagonal separates the cut that **pays off** from the one that **destroys more than it frees**.

**How we apply it.** Cutting **Project J** frees **20.5% of the pool** while sacrificing **1.9% of the value** — it opens nearly 2 new slots without diluting anyone. Cutting **Project F** would free 3.4% and sacrifice **21.2% of the value**: it would **destroy more value than it frees capacity**. **This is not "cut costs" — it is an explicit trade-off, with numbers.**

![Cut policy — % of pool freed against % of value sacrificed; the diagonal separates the cut that pays off from the one that destroys](docs/screenshots/budget-politica-corte.png)

---
<!-- budget-loop-section -->

## 🔁 Budget re-learning loop — the agent that **evolves with the ecosystem**

**A healthy ecosystem has memory.** The predator learns which prey is worth the chase; the plant learns which way to grow. Without that learning there is no adaptation — only blind trial and error, forever. That was exactly what the agent lacked: it recommended *cutting waste*, but **never checked, the following week, whether the cut it ordered actually freed pool.** Recommending without verifying is not management — it is recycled guesswork.

**Concept.** The PM Agent closes the loop: it **stores the number** the week it recommends the cut and, the following weekly, **holds itself to account**. Did waste drop? The recommendation worked. It didn't? It failed. It is the same **contextual bandit** as the re-learning engine — now applied to the **token** dimension, the scarcest resource in the biosphere.

**Methodology.** Only the action **it recommended** is judged — it answers for what it ordered and **takes no credit for what luck freed**. The cut worked → its confidence in that recommendation **rises**. It didn't → it **falls**. Movement below 2% is noise, and **it does not learn from noise**. Confidence is **per project**: the agent discovers which cuts actually free pool in *that* ecosystem.

**Direct benefit.** Every Friday the agent arrives at the weekly with an accounting of its own advice: *"last week I ordered cutting HALLUCINATION_CODE; it freed R$ X of pool — I raise my confidence"* or *"it didn't take — I lower my confidence and reconsider"*. Over time it stops repeating the cut that doesn't work in your context and doubles down on the one that does. **Your budget stops being run by a fixed rule and starts being run by an agent that learned to play on your board.**

![Budget re-learning loop — waste rises and falls, and the agent's confidence responds: up when the cut works, down when it fails, ignoring the noise](docs/screenshots/budget-loop-reaprendizagem.png)

---
<!-- pm-agent-section -->

## 🤖 Project Manager Agent — reads 10 dimensions, learns, and **knows when to stay quiet**

The dashboard **diagnoses**. The causal chain **quantifies**. The agent **decides what to do now** — and, cycle after cycle, learns which lever actually moves the needle *on that specific project*. It sweeps **10 dimensions** (schedule, ROI, risk, tokens, cost, model drift, reliability, quality, flow and waste), converts each into **equivalent project-days × that project's own cost of delay**, and answers the only question that matters: **what to do now, and what it's worth.**

> **The weakness we had to fix.** The agent **always** recommended something: every cycle it grabbed the biggest damage and shouted. **An agent that shouts every week becomes noise, and noise gets ignored** — so it changes nothing, however right it is. **It lacked the right to stay quiet.** That is what the three methodologies below deliver.

### 🚦 PRINCE2 — *management by exception*: the right to stay quiet

**Concept.** PRINCE2's *management by exception* says the manager **must not be disturbed** while the project stays within agreed tolerances. When the **forecast** breaches tolerance — not the actuals, the **forecast** — an **Exception Report** fires.

**Methodology.** A tolerance per dimension (time, cost, risk, quality, benefit). Escalation is driven by the **forecast**: the Monte Carlo P80 and the EVM EAC. The Exception Report has four mandatory parts — **cause, impact, OPTIONS and recommendation**. It is the *options* line that separates an exception report from an alarm: escalating without offering alternatives is pushing the problem upward, not managing it.

**How we apply it.** The tolerances are **not numbers we invented** — they come from what the project **already declared**: the promised date (`prazo_alvo`), the approved budget (`BAC`), the **risk register's own classification** (`nivel='critico'`), and the **project's own quality baseline** (regression against itself, DORA-style). Only the ROI limit is explicit policy — and it is in plain sight, for the board to disagree with. The options the agent offers are **absorb** (burn management reserve), **recover** (compress the critical path) or **renegotiate** (move the date or cut scope).

![PRINCE2 tolerances — each dimension's headroom before exception; only Quality breached, and only Quality is escalated](docs/screenshots/prince2-tolerancias.png)

### 🌡️ CCPM (Goldratt) — *buffer management* and the fever chart

**Concept.** In Goldratt's *Critical Chain*, the buffer is not padding hidden inside every task: it is an **explicit cushion at the end of the project**. The **fever chart** crosses *how much of the chain is complete* with *how much of the buffer is consumed*, and tells you which of three zones you are in.

**Methodology.** The boundaries are **diagonal**, and that is the essence of the method: burning buffer **late** is normal — burning it **early** is serious, because a whole project still lies ahead. **GREEN = do nothing. YELLOW = plan the recovery. RED = act now.**

```
verde/amarelo:    y = 1/3 + (1/3)·x
amarelo/vermelho: y = 2/3 + (1/3)·x
```

**How we apply it.** The buffer is `P80 − P50` from the **Monte Carlo schedule** we already ran. Consumption is the **Earned Schedule slip** converted into days. And it is the fever chart that gives the agent an objective trigger for silence: **green zone plus within tolerance = nothing to escalate.** Today **3 of the 10 projects** get exactly that — and it is by staying quiet when there is nothing to say that the agent earns the right to be heard when there is.

![CCPM fever chart — the 10 projects across the three zones; the diagonal boundaries make the same buffer burn benign late and serious early](docs/screenshots/ccpm-fever-chart.png)

### 🏦 PMI — *reserve analysis*: contingency vs management reserve

**Concept.** PMI separates two reserves that almost everyone conflates: **contingency** covers the *known-unknowns* (the variability you **measured**), and **management reserve** covers the *unknown-unknowns* (the shock).

**Methodology.** `contingency = P80 − P50` and `management reserve = P95 − P80`. Plus the comparison almost nobody makes: the contingency you **have** against the one your **risk register justifies** (EMV — *Integrated Cost-Schedule Risk Analysis*, Hulett). A duration buffer is **blind to risk events**; that is where most schedules discover they were optimistic.

**How we apply it — and a lesson in honesty.** Converting “impact 4” (a 1–5 scale) into days requires a mapping that is **ours, not yours**. So we **stress-tested our own assumption**: halve the assumed impact and the “under-reserved” conclusion flips from **10/10 to 1/10 projects**. It is a **knife-edge**, and therefore it is **not sold as a finding** — every project carries a `robusto` flag, and the agent **warns you when its own reading does not survive the stress test**. What is left **with no assumption at all** is pure arithmetic, and it is the real finding: **the buffer is ~9% of the chain, against the 25–50% CCPM works with.**

### 🏃 Sprints and the Friday weekly debate

**Concept.** The Friday *weekly* progress debate needs **numbers**, not opinions. Opinions do not move projects.

**Methodology.** Three metrics open the discussion. **(1) Say-do ratio** (`ΔEV ÷ ΔPV`): a team at 0.7 is **not slow** — it is *promising 30% more than it can deliver*. You do not fix capacity by pushing harder; you fix commitment with predictability. And say-do **well above 1** is not heroism either: it is a **broken baseline**. **(2) The sprint's local CPI**, kept apart from the cumulative **on purpose** — the cumulative is an average, and averages **hide** the recent bad sprint: a cumulative CPI of 1.05 can shelter a last sprint at 0.60. **The local one accuses; the cumulative one consoles.** **(3) Velocity-based forecast**: if the team needs 6 sprints and only 4 remain, **the date is already dead** and nobody noticed, because the cumulative burndown still *looks* close to plan.

**How we apply it.** The sprint is **not invented**: it is the **EVM period**, the cadence the project already has, with real PV/EV/AC. Building a sprint calendar parallel to the schedule would create a **second truth** about the same project — and two truths is the same as none.

> **⚠️ Conformance, said plainly.** This is a **cadence-based progress report built on EVM (ANSI/EIA-748) with agile-inspired metrics** — **it is not Scrum**. The *2020 Scrum Guide* contains **neither** “velocity” **nor** “burndown chart” (they are industry practice, not official artefacts), and it replaced the Sprint Backlog *commitment* with the **Sprint Goal**, treating the backlog as a **forecast**. So “say-do ratio (delivered ÷ committed)” is **industry** vocabulary, not canonical Scrum. **The metric is honest; it is the label that would lie.**

![Sprints — say-do ratio per sprint and the real burndown against plan; the cadence is the EVM period](docs/screenshots/sprints-weekly.png)

### 🎯 The radar and the re-learning engine — why this dimension and not another

The agent **does not look only at the winner** — it shows the whole bench. Each dimension becomes **equivalent days**, days become **money** at *that* project's cost of delay, and the weight is what the agent **learned there**. Priority is `damage × weight`.

The **re-learning engine** is a *contextual bandit* — simple and auditable, and we say it plainly: **this is not deep learning**. Each cycle the agent recommends a lever and **stores its target metric**; the next cycle it **holds itself to account**. Improved → the weight **rises**. Worsened → it **falls**. Movement below 2% is noise, and **the agent does not learn from noise**. Only the lever it **recommended** is judged: it answers for what it told you to do and **takes no credit for what luck improved**. The result is a profile that **does not fit the project next door** — and that is exactly the point.

![Radar of the 10 dimensions — each one's damage on the same ruler (R$), and the one the agent chose to attack](docs/screenshots/pm-agent-radar.png)

---
## 🌐 12 languages

The dashboard, per-project pages **and the text inside the chart images** are localized in **12 languages**:
Português · English · Español · Français · Deutsch · 中文 · 한국어 · हिन्दी · עברית · Svenska · Русский · Suomi.
Translation is driven by a **Translation Memory** (SDL Trados style) that standardizes and speeds up new languages.

---

## 🙋 Objections (the questions you're asking right now)

- **"I don't have time."** → Five minutes with `./run_all.sh --mock` and the dashboard is running on your screen.
  Measuring **gives back** the hours you already lose to rework and hallucination.
- **"It's too complex."** → One line. The framework does the ETL, the math, the ranking and the images; **you
  just read the verdict.**
- **"My AI operation is small."** → That's exactly why each dollar weighs more. Small today, portfolio tomorrow —
  **measure before you scale the waste.**
- **"I don't use Langfuse."** → The demo runs **100% without Langfuse**. When you want real data, you plug in
  **your** account (never mine).
- **"It's just another pretty dashboard."** → No. It's **Balanced Scorecard + investment analysis (NPV/IRR/MIRR/EAA)
  + multi-criteria decision (AHP-TOPSIS)** — board instruments, not decoration.
- **"What about my data privacy?"** → The demo is **100% anonymous** (Project A…J); real data/names and keys stay
  **out of the package**. You run **locally**, with **your** account.
- **"How much does it cost?"** → **Nothing.** Open source, on your machine. The only price is to keep **not
  measuring** — and that one, you're already paying.

---

## 🧩 Bundled skills (*build & analyze your own*)

This repository ships reusable **Skills** (Claude Code):

- **`measuring-ai-projects`** — define/measure/report KPIs for AI projects (the core of this framework).
- **`github-benchmark-analyzer`** — analyze and benchmark **any** GitHub repository/profile (stars, forks,
  followers, hashtags, README style, keywords, languages) and extract what the leaders have in common. **Build
  and analyze your own portfolio** — even against the market.

---

## 📚 Resources & references (Awesome)

Shoulders of giants this framework stands on:

- **Strategy & measurement:** Kaplan & Norton — *The Balanced Scorecard* · Peter Drucker (management by objectives).
- **Lean Six Sigma:** the 8-wastes (Muda) taxonomy, PDCA/Kaizen, Ishikawa/RCA.
- **Corporate finance:** Lawrence Gitman — *Principles of Managerial Finance* (NPV, IRR, MIRR, PI).
- **Multi-criteria decision:** Thomas Saaty (**AHP**) · Hwang & Yoon (**TOPSIS**).
- **Tech stack:** [Langfuse](https://langfuse.com) (LLM observability) · [Evidence](https://evidence.dev)
  (BI as Code) · [Rust/PyO3](https://pyo3.rs) · [Tectonic](https://tectonic-typesetting.github.io) (LaTeX).

---

## 🗺️ Roadmap

- [x] Langfuse → SQLite → Evidence pipeline + Rust
- [x] 70+ KPIs (BSC + API economy + Lean) · EVM
- [x] Financial suite (NPV, IRR, MIRR, EAA, PI, Payback, dollarization)
- [x] AHP-TOPSIS 2n + administrative dossier (6 tools)
- [x] Dashboard and images in **12 languages**
- [ ] Extra observability connectors (OpenTelemetry, Helicone)
- [ ] Multi-tenant SaaS mode + native scheduling
- [ ] Static dashboard publishing (GitHub Pages)

---

## 🧰 Step-by-step setup (local, from scratch)

> Everything runs **on your machine**. No author keys ship with the package and no data leaves your computer.

### Step 0 — Prerequisites

| Requirement | Version | Required? | What for |
|---|---|---|---|
| **Python** | 3.10+ | ✅ | pipeline, KPIs, Monte Carlo, MCDM |
| **Node.js + npm** | 18+ | ✅ | dashboard (Evidence) |
| **git** | any | ✅ | cloning the repository |
| **Rust + maturin** | stable | ⬜ optional | speeds up log classification |
| **tectonic** | any | ⬜ optional | builds the PDF pitch decks |

*On Windows, use **WSL** or **Git Bash** — the pipeline is a `bash` script.*

### Step 1 — Clone the repository
```bash
git clone https://github.com/bpenedo/Gestao-de-Projetos-PM-IA-BSC-DashBoard.git
cd Gestao-de-Projetos-PM-IA-BSC-DashBoard
```

### Step 2 — Isolated Python environment
```bash
cd foundations/pipeline
python3 -m venv .venv
source .venv/bin/activate        # Windows (PowerShell): .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Step 3 — Dashboard dependencies
```bash
cd ../evidence
npm install
```

### Step 4 — Run the demo (anonymous, no credentials)
```bash
cd ../pipeline
./run_all.sh --mock
```

In order, the pipeline runs: anonymous demo data → KPIs → NPV/IRR/MIRR/EAA/PI → **fitting distributions to tokens** →
**Monte Carlo (10,000 iterations)** → AHP-TOPSIS 2n → **DEMATEL · ELECTRE · PROMETHEE · MAUT · MCDA-C** →
**ranking robustness (Dirichlet)** → charts → administrative dossier → 5D map → pitch decks → dashboard build.

### Step 5 — Open the dashboard
```bash
cd ../evidence
npm run dev          # http://localhost:3000
npm run preview      # (alternativa) serve o estático já compilado em build/
```

### Step 6 — Switch to YOUR data

**6.1 — Credentials and parameters** (all optional; without `.env` the pipeline uses the defaults):
```bash
cd ../pipeline
cp .env.example .env      # edite: LANGFUSE_PUBLIC_KEY, LANGFUSE_SECRET_KEY, SELIC_ANUAL, USD_BRL...
```

**6.2 — Your cash flow** (this is what feeds NPV, IRR and the Monte Carlo):
```bash
cp fluxo_caixa_template.csv fluxo_caixa.csv
```
Format: `periodo 0` is the investment (negative flow) and `taxa` is the per-period discount rate (`0.10` = 10%).
```csv
project_name,periodo,fluxo,taxa
Project A,0,-12000,0.10
Project A,1,3000,0.10
Project A,2,4000,0.10
```

**6.3 — Run with real data:**
```bash
./run_all.sh          # sem --mock: sincroniza do Langfuse e usa fluxo_caixa.csv
```

### Step 7 (optional) — Acceleration and PDFs
```bash
cd analise_rs && maturin develop --release && cd ..   # Rust (PyO3): classificação mais rápida
```
For the pitch decks, install **tectonic** (e.g. `cargo install tectonic` or your distro's package manager).

### Step 8 (optional) — Schedule the refresh
```bash
crontab -e
*/15 * * * * /CAMINHO/ABSOLUTO/foundations/pipeline/run_all.sh >> /tmp/bsc.log 2>&1
```

### 🩺 Common problems

| Symptom | Likely cause | Fix |
|---|---|---|
| `no such table: ...` | database not initialized | `python3 db.py` |
| Dashboard build fails | stale artifacts | `rm -rf ../evidence/build && npm run build` |
| `findfont: Failed to find font weight` | matplotlib warning | harmless, ignore it |
| `Precisa de ≥2 projetos` | portfolio with a single project | MCDM compares alternatives; add another |
| `KS p-value < 0.05` on screen | the distribution doesn't describe your data well | collect more samples; the framework warns instead of hiding |
| Numbers change between runs | seed was changed | keep `MC_SEED` fixed for reproducibility |

---

## 🤝 Contributing

Contributions are **very welcome**! Open an *issue* describing your proposal (new KPI, connector, language, fix)
and send a *pull request*. Standards: readable code consistent with its surroundings, no personal data in the
package (the demo is anonymous). New languages: add the targets to the Translation Memory and run the generator.

## 📄 License & authorship

© **Bruno Penedo** — 2026. Use, study and contribution encouraged; for commercial use/redistribution, consult the
author. *(A formal OSS license can be added — open an issue with your preference.)*

## 🏷️ Topics
`awesome-list` · `education` · `resources` · `computer-science` · `python` · `business-intelligence` ·
`llmops` · `finops` · `aiops` · `programming` · `development` · `lists` · `free` · `unicorns` · `dashboard` ·
`balanced-scorecard` · `langfuse` · `llm-observability` · `kpi` · `project-management`

---

⭐ **If this framework sheds light on your AI spend, leave a star — and start profiting from what you already pay for.**

---

**Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard** · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
