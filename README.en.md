# 🧭 Gestão de Projetos PM IA BSC DashBoard (Build and Analyze Your Own AI Portfolio Projects)

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

We are **pioneers** of a new territory — the **frontier between artificial intelligence and the accounting of
value**. Like explorers charting unmapped lands, this framework is the **compass** (🧭) that turns the fog of
subscriptions into **clear routes of return**: each token a mile; each project an expedition toward profit.
Where there was blind cost, **measurable opportunity** is born; where there was a dead spreadsheet, a **living
investment thesis** blossoms.

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
