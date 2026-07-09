# 🧭 Gestão de Projetos PM IA BSC DashBoard (Build and Analyze Your Own AI Portfolio Projects)

🌐 [Português](README.md) · [English](README.en.md) · [Español](README.es.md) · **Français** · [Deutsch](README.de.md) · [中文](README.zh.md) · [한국어](README.ko.md) · [हिन्दी](README.hi.md) · [עברית](README.he.md) · [Svenska](README.sv.md) · [Русский](README.ru.md) · [Suomi](README.fi.md)

![Method](https://img.shields.io/badge/method-Balanced%20Scorecard-1F3A5F)
![AI](https://img.shields.io/badge/AI-LLM%20observability-45a1bf)
![Finance](https://img.shields.io/badge/finance-VAN%20·%20TRI%20·%20TRIM%20·%20IP-46a485)
![Decision](https://img.shields.io/badge/MCDM-DEMATEL%20·%20ELECTRE%20·%20PROMETHEE%20·%20MAUT%20·%20MCDA--C-8E44AD)
![Risk](https://img.shields.io/badge/risk-Monte%20Carlo%2010k%20·%20VaR%20·%20CVaR-DC143C)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-PyO3-orange?logo=rust&logoColor=white)
![Dashboard](https://img.shields.io/badge/dashboard-Evidence-236aa4)
![PDF](https://img.shields.io/badge/pitch%20deck-LaTeX-008080)
![i18n](https://img.shields.io/badge/i18n-12%20langues-0E7C86)
![status](https://img.shields.io/badge/status-v1-success)

### 💸 Vous payez pour l'IA chaque mois. Mais l'IA vous paie-t-elle **en retour** ?

Chaque fois que la carte est débitée par **ChatGPT, Claude, Copilot, Gemini, Perplexity, DeepSeek, Kimi, Qwen…**,
une question à **des millions** reste sans réponse : **où est le retour ?** Combien d'heures-homme ont réellement
été économisées ? Combien de votre argent s'est **évaporé** en hallucination, reprise et attente ? Quel projet
d'IA **mérite d'être déployé aujourd'hui** — et lequel **saigne la trésorerie** pendant que vous applaudissez
l'« innovation » ?

Vous n'avez pas un coût d'IA. Vous avez une **fuite silencieuse** — et vous avez les yeux bandés. Car *« ce qui
n'est pas mesuré ne peut être ni géré ni amélioré »* — et le marché le mesure pour vous, et vous en présente la
facture.

**Ce framework allume la lumière.** Il transforme la **dépense invisible** de vos abonnements d'IA en **retour
mesurable, comparable et auditable** — avec la rigueur du **Balanced Scorecard** (Kaplan & Norton), de l'**analyse
d'investissement de niveau Wall Street** et de la **décision multicritère**. C'est la différence entre *espérer* et
*savoir*. Entre payer pour l'IA et en **tirer profit**.

> *« Ce qui n'est pas mesuré ne peut être ni géré ni amélioré. »* — Kaplan & Norton

> *« Qui mesure avec précision, bâtit avec excellence. »* — Pierre Vernier

> *Lorsque tu pries et étudies, ne laisse pas [mes paroles] te quitter. Avec chaque mot et chaque expression qui sort de tes lèvres, garde à l'esprit d'accomplir une Unification.* — Aryeh Kaplan

> *La métaphysique pure, se situant par essence au-dessus et au-delà de toutes les formes et de toutes les contingences, n'est ni orientale ni occidentale : elle est universelle.* — René Guénon

> *Se connaître soi-même, c'est connaître sa propre lignée et sa propre puissance.* — Harvey Spencer Lewis

> *Scientia es Lux Lucis* ∞ Sapere Aude S∴A∴☬ ☿

> 🐺 **Arrêtez de PAYER pour l'IA à l'aveugle.** Pendant que le marché s'abonne à l'IA par foi — et devient la
> statistique de **Gartner** (≥30 % des projets de GenAI abandonnés après le pilote) —, **vous** allez mesurer
> chaque token, élire le projet gagnant et convertir la dépense invisible en **retour auditable** : VAN · TRI ·
> TRIM · AÉ · 70+ KPI · décision multicritère · tableau de bord C-Level en **12 langues**. **L'IA est déjà à
> vous. Rendez-la maintenant RENTABLE** — gratuitement, sur votre machine, en **5 minutes** :
> `./run_all.sh --mock && npm run dev` 🔥

> 📖 **Documentation principale :** **[`foundations/README.md`](foundations/README.md)** ·
> ⚙️ **Setup (apportez vos clés) :** [`foundations/pipeline/SETUP.md`](foundations/pipeline/SETUP.md) ·
> 📊 **KPI :** [`foundations/KPIs.md`](foundations/KPIs.md) / [`foundations/KPIs_README.md`](foundations/KPIs_README.md)

---

## 📑 Sommaire

- [🌅 Pourquoi cela change la donne](#-pourquoi-cela-change-la-donne)
- [📈 Les preuves (Gartner · IDC · PwC · McKinsey · MIT)](#-les-preuves-gartner--idc--pwc--mckinsey--mit)
- [💥 Le coût de l'inaction](#-le-coût-de-linaction-faites-le-calcul-que-personne-ne-fait)
- [✨ Fonctionnalités](#-fonctionnalités)
- [📸 Captures (tableau de bord anonyme)](#-captures-tableau-de-bord-anonyme)
- [🚀 Démarrage rapide](#-démarrage-rapide-démo-sans-langfuse)
- [🏗️ Architecture](#️-architecture)
- [📊 Catalogue de KPI](#-catalogue-de-kpi-70)
- [💰 Analyse financière d'investissement](#-analyse-financière-dinvestissement)
- [🏆 Décision multicritère + Dossier](#-décision-multicritère-ahp-topsis-2n--dossier-du-joyau-de-la-couronne)
- [🎲 Monte-Carlo — le risque que la moyenne cache](#-monte-carlo--le-risque-que-la-moyenne-cache)
- [🧮 Cinq écoles de décision. Un seul verdict.](#-cinq-écoles-de-décision-un-seul-verdict)
- [🌐 12 langues](#-12-langues)
- [🙋 Objections (les questions que vous vous posez maintenant)](#-objections-les-questions-que-vous-vous-posez-maintenant)
- [🧩 Skills incluses](#-skills-incluses-build--analyze-your-own)
- [📚 Ressources & références](#-ressources--références-awesome)
- [🗺️ Feuille de route](#️-feuille-de-route)
- [🤝 Contribuer](#-contribuer)
- [📄 Licence & paternité](#-licence--paternité)

---

## 🌅 Pourquoi cela change la donne

**Il existe deux types de personnes à l'ère de l'IA.** Les premières s'abonnent à tout, dépensent gros et
**prient** pour que ça marche — et grossissent la cruelle statistique des projets qui meurent au pilote. Les
secondes font ce que Wall Street fait avec tout actif sérieux : elles **mesurent, comparent, priorisent et
réallouent** — et transforment chaque dollar d'abonnement en **retour composé**. La seule différence entre elles
**n'est ni le talent ni le budget. C'est l'instrumentation.**

L'IA générative a créé une nouvelle classe de dépense récurrente — **abonnements et tokens** — et, avec elle, le
gaspillage le plus coûteux de la décennie : **l'invisible.** Ce que vous ne voyez pas, vous ne le corrigez pas.
Ce que vous ne mesurez pas, vous ne le déployez pas. Et ce que vous ne prouvez pas, le conseil ne l'approuve pas.

**Ce projet vous fait passer de la première tribu à la seconde.** Il instrumente chaque projet d'IA comme un
**actif financier** et le mesure sous le **Balanced Scorecard**, l'**analyse d'investissement (VAN, TRI, TRIM,
AÉ, IP, délai de récupération)** et le **Lean Six Sigma** — et il **élit même le meilleur projet de votre
portefeuille** par un modèle multicritère (**AHP-TOPSIS 2n**). La facture mensuelle opaque devient une **thèse
d'investissement auditable** : vous découvrez, avec des chiffres, où déployer, où couper, où l'abonnement se
rembourse en **semaines** — et où il saigne sans couverture.

Nous sommes les **pionniers** d'un territoire nouveau — la **frontière entre l'intelligence artificielle et la
comptabilité de la valeur**. Tels des explorateurs cartographiant des terres encore vierges, ce framework est la
**boussole** (🧭) qui transforme le brouillard des abonnements en **routes claires de retour** : chaque token, un
mille ; chaque projet, une expédition vers le profit. Là où il y avait un coût aveugle naît une **opportunité
mesurable** ; là où il y avait un tableur mort fleurit une **thèse d'investissement vivante**.

> **La promesse :** transformer celui qui *paie pour l'IA* en celui qui *profite de l'IA* — et celui qui *utilise
> l'IA* en celui qui la **maîtrise, la mesure et la multiplie en pionnier**. Avec des chiffres, pas avec la foi.

---

## 📈 Les preuves (Gartner · IDC · PwC · McKinsey · MIT)

Ne me croyez pas sur parole. **Croyez les instituts qui étudient cela depuis des décennies** — et dont le verdict
est unanime : **l'IA crée une valeur immense, mais ne la livre qu'à ceux qui mesurent et gouvernent.** Ceux qui
« utilisent l'IA sans la maîtriser » deviennent une statistique d'abandon ; ceux qui instrumentent le retour
**gardent le prix**.

- 🧭 **Gartner** — a prévu que **≥ 30 % des projets d'IA générative seraient abandonnés après la preuve de concept
  d'ici fin 2025**, avec la **valeur métier peu claire** comme cause centrale (outre des données médiocres, des
  coûts croissants et des contrôles fragiles). *→ sans mesure, le projet meurt au pilote.*
- 🔬 **MIT** (rapport *« The GenAI Divide / State of AI in Business 2025 »*, initiative NANDA) — largement rapporté
  que la **grande majorité des pilotes GenAI en entreprise ne génère aucun impact mesurable sur le P&L** ; la
  minorité qui livre de la valeur combine l'IA avec **processus et mesure**. *→ la différence, c'est mesurer, pas
  adopter.*
- 💵 **IDC** (étude *« The Business Opportunity of AI »*, sponsorisée par Microsoft) — les organisations qui
  **mesurent et optimisent** ont déclaré un retour de l'ordre de **plusieurs dollars pour chaque 1 US$** investi
  en IA, avec une forte dispersion entre leaders et retardataires. *→ le ROI existe — et favorise ceux qui
  instrumentent.*
- 🌍 **PwC** (*« Sizing the Prize »*) — estime que l'IA pourrait ajouter jusqu'à **~15,7 billions US$** à l'économie
  mondiale d'ici 2030 ; mais le prix va à ceux qui **capturent** la valeur, pas à ceux qui la consomment seulement.
  *→ le gâteau est gigantesque ; la part revient à ceux qui mesurent.*
- 🏆 **McKinsey** (*« The State of AI »*) et **BCG × MIT Sloan** — un groupe minoritaire d'**« AI high performers »**
  capture un retour disproportionné ; le tournant survient lorsque l'IA est couplée à **des métriques, une
  gouvernance et un réinvestissement** là où le retour est prouvé. *→ les gagnants mesurent, priorisent et
  réallouent.*

> **C'est exactement ce fossé que ce framework franchit :** il vous fait quitter le côté qui *abandonne au pilote*
> pour rejoindre le côté qui a des **résultats concrets et prouvés** — avec BSC, analyse d'investissement et
> décision multicritère.

> ⚠️ **Note d'honnêteté (à lire) :** les chiffres ci-dessus reflètent de vrais titres de ces instituts, mais **les
> rapports et pourcentages sont mis à jour** — vérifiez les valeurs exactes et l'année dans les **sources
> primaires** (Gartner Newsroom ; IDC/Microsoft *Business Opportunity of AI* ; PwC *Sizing the Prize* ; McKinsey
> *State of AI* ; MIT *State of AI in Business*) avant de les citer dans un document officiel. Ils servent ici de
> **fondement directionnel**, non de garantie chiffrée.

---

## 💥 Le coût de l'inaction (faites le calcul que personne ne fait)

Un abonnement **PRO d'IA** coûte entre **20 et 200 US$ par mois, par siège**. Multipliez par le nombre de
personnes de votre équipe. Multipliez par 12 mois. Appliquez maintenant ce que les instituts ont **déjà prouvé** :
**Gartner** projette **≥ 30 % d'abandon** et le **MIT** montre que la **majorité des pilotes ne rapporte pas**.
Une part énorme de ce total n'est pas un investissement — c'est une **hémorragie pure**.

> **Exemple direct (remplacez par vos chiffres) :** 10 sièges × 30 US$/mois × 12 = **3 600 US$/an**. Si ~30 %
> devient du gaspillage invisible, ce sont **~1 080 US$/an qui s'évaporent** — pour UNE petite équipe, en UN an.
> Avec votre chiffre réel, le choc est plus grand.

Et voici ce qui fait mal : **ce coût est composé et n'attend pas.** Chaque mois sans mesure est un mois de fuite
qui **ne revient pas** — pendant que le concurrent qui a instrumenté **réalloue déjà son capital vers ce qui
rapporte**. L'avantage du pionnier se construit tôt : **qui mesure le premier, déploie le premier.**

Le moment le moins coûteux pour commencer était hier. Le deuxième meilleur, c'est **maintenant** — et cela coûte
**0 US$** et **5 minutes**. La question n'est pas *« puis-je me permettre de mesurer ? »*. C'est ***« combien de
temps encore puis-je me permettre de NE PAS mesurer ? »***

---

## ✨ Fonctionnalités

- **📊 KPI (4 perspectives BSC) + économie d'API :** maturité, capital humain, financier et efficacité des tokens
  — `IEET`, `IOLI`, `ITR`, `IITA`, `PEUC`, `ICCA`, `IDLS`, `IBMT` — plus **EVM** (CPI/SPI/EAC).
- **🪙 Concepts de frontière :** **VRT/kTR** (unité de récupération de coût tokenisable — *« le m² de Gitman »*) et
  **PSR** (Project Score 0–5 ⭐) pour classer la santé de chaque projet.
- **🔬 Diagnostic opérationnel :** **VRT en 5 blocs**, **HCI** (heure critique d'interruption), **gaspillages Lean
  Six Sigma** (tokens pondérés) et **RCA d'hallucination par taxonomie de prompt** (goulot par projet +
  intersection).
- **💰 Suite financière complète :** **VAN, TRI, TRIM (TRI modifié), AÉ (annuité équivalente), IP (indice de
  profitabilité), délai de récupération** simple et actualisé, **dollarisation** et comparaison avec le **SELIC**
  et les **taux américains**.
- **🏆 Décision multicritère :** **AHP-TOPSIS 2n** (double normalisation) élit le **meilleur projet** du
  portefeuille avec **test de robustesse** — et génère un **dossier administratif** (SWOT, PESTELC, 5W4H, Pareto,
  GUT, Radar).
- **🗺️ Visuel C-Level :** **carte 5D interactive**, donuts avec profondeur, quadrant de durabilité, tendances et
  **pitch decks** LaTeX des projets éligibles.
- **⚙️ Pipeline réel :** **Langfuse → SQLite → Evidence**, avec sync **asynchrone concurrent** et classification
  accélérée en **Rust (PyO3)**.
- **💳 FinOps de l'IA :** catalogue de **plans d'abonnement** (OpenAI, Anthropic, Google, Perplexity, xAI, Mistral,
  DeepSeek, Kimi, Qwen…) avec **change + IOF** et base de répartition (burn rate).
- **🌐 12 langues** dans le tableau de bord **et dans les images des graphiques** (dont Devanagari, Hébreu et CJK).

---

## 📸 Captures (tableau de bord anonyme)

> Démo 100 % anonyme (projets affichés comme *Project A…J*). Les données/noms réels n'accompagnent jamais le paquet.

**🌐 Carte 5D du portefeuille** — 5 dimensions par projet : **X**=tokens · **Y**=PEUC (qualité) · **Z**=PSR (santé)
· **taille**=Burn Rate · **couleur**=ICCA (durabilité). *Où déployer ? Droite/fond, haut et vert. Où couper ?
Grand et rouge.*

![Carte 5D du portefeuille de projets d'IA](docs/screenshots/5d-portfolio-map.png)

**🏆 Dossier du « Joyau de la Couronne »** (projet élu par AHP-TOPSIS) — généré par un pipeline Python concurrent :

| SWOT | Radar concurrentiel |
|---|---|
| ![SWOT](docs/screenshots/swot.png) | ![Radar concurrentiel](docs/screenshots/radar.png) |

| PESTELC (macro-environnement) | Matrice GUT (priorisation) |
|---|---|
| ![PESTELC](docs/screenshots/pestel.png) | ![GUT](docs/screenshots/gut.png) |

| 5W4H (plan d'action) | Pareto des défaillances (80/20) |
|---|---|
| ![5W4H](docs/screenshots/5w4h.png) | ![Pareto](docs/screenshots/pareto.png) |

---

## 🚀 Démarrage rapide (démo, sans Langfuse)

**Zéro risque. Zéro coût. 5 minutes.** Lancez-le sur votre machine et voyez le tableau de bord complet avec des
données anonymes :

```bash
cd foundations/pipeline
pip install -r requirements.txt
cd ../evidence && npm install && cd ../pipeline
./run_all.sh --mock          # données anonymes (Project A..J) -> KPI -> VAN/TRIM/AÉ -> 5D -> pitch decks -> tableau de bord
cd ../evidence && npm run dev # http://localhost:3000
```

Pour des **données réelles**, remplissez `foundations/pipeline/.env` avec **vos propres** clés Langfuse (voir
[`SETUP.md`](foundations/pipeline/SETUP.md)) et lancez `./run_all.sh`. Chaque utilisateur utilise son **propre
compte** — aucune clé de l'auteur n'accompagne le paquet.

---

## 🏗️ Architecture

```
   Vos applis d'IA              Observabilité          Analytics-as-Code           Vous
 (ChatGPT, Claude, API…)   ┌──────────────┐   ┌──────────────────┐   ┌──────────────────────┐
        │ traces           │   Langfuse   │   │  SQLite (schéma  │   │  Evidence (BI as     │
        └─────────────────▶│  (SDK v4)    │──▶│  + requêtes KPI) │──▶│  Code) · 12 langues  │
                           └──────────────┘   └──────────────────┘   └──────────┬───────────┘
   sync asynchrone concurrent          classification en Rust (PyO3)           │
                                                                    ┌───────────┴───────────┐
                                                                    │ AHP-TOPSIS · Dossier  │
                                                                    │ 5D · Pitch decks (TeX)│
                                                                    └───────────────────────┘
```

**Stack :** Python 3.13 · SQLite/DuckDB · Evidence.dev (SvelteKit) · Rust + PyO3 + maturin · matplotlib ·
tectonic (LaTeX) · polices Noto/WenQuanYi pour l'i18n des images.

---

## 📊 Catalogue de KPI (70+)

Échantillon (catalogue complet dans [`foundations/KPIs_Lean6s_BSC.md`](foundations/KPIs_Lean6s_BSC.md)) :

| Sigle | Nom | Ce à quoi il répond |
|---|---|---|
| **PSR** | Project Score Rating (0–5) | Santé globale du projet d'IA |
| **PEUC** | % de Livraison Utile par Consommation | Quelle part de la dépense est devenue livraison utile |
| **IITA** | Indice d'Incidence de Tokens Hallucinés | % d'hallucination/reprise |
| **IDLS** | Indice de Gaspillage Lean | Muda (tokens pondérés par gravité) |
| **VRT/kTR** | Valeur de Récupération Tokenisable | « m² de Gitman » — coût pour 1k tokens |
| **ICCA** | Indice de Couverture de Coût par Abonnement | Couvre-t-il le coût ? (>3× sain) |
| **CPP** | Coût par Point de Progression | Indicateur maître (plus c'est bas, mieux c'est) |

---

## 💰 Analyse financière d'investissement

Chaque projet devient une **thèse d'investissement** : à partir de votre flux de trésorerie (CSV), le framework
calcule **VAN**, **TRI**, **TRIM (réinvestit au coût du projet)**, **AÉ (annuité équivalente de la VAN)**, **IP
(indice de profitabilité)** et le **délai de récupération** simple/actualisé — en **dollarisant** le flux et en le
comparant au **SELIC** et aux **taux américains**. Il génère un **pitch deck** LaTeX pour tout projet avec **VAN >
0 et IP > 1** en BRL **et** USD. L'objectif est brutalement pratique : **savoir si votre abonnement d'IA se
rembourse — et en combien de temps.**

---

## 🏆 Décision multicritère (AHP-TOPSIS 2n) + Dossier du Joyau de la Couronne

Avec plusieurs projets, lequel déployer d'abord ? Le modèle **AHP-TOPSIS 2n** pondère les indicateurs comme
critères (poids par **AHP** avec ratio de cohérence **CR ≤ 0,10**) et classe par **TOPSIS** sur **deux
normalisations** (vectorielle + min-max), en rapportant la **robustesse** (concordance entre normalisations). Le
gagnant — le **« Joyau de la Couronne »** — reçoit un **dossier administratif** complet (SWOT · PESTELC · 5W4H ·
Pareto · GUT · Radar) généré de zéro par le code, avec un **Bottom-Line** exécutif et des **insights C-Level**
honnêtes. **Vous ne présentez pas un tableur. Vous présentez un verdict.**

---

## 🎲 Monte-Carlo — le risque que la moyenne cache

Une VAN positive **en moyenne** ne protège personne. La moyenne est le mensonge le plus confortable de la finance :
elle décrit un scénario qui n'arrivera peut-être jamais. Ce qui décide de votre sort, c'est la **queue** — le mauvais jour.

Ce framework simule **10 000 futurs** pour chaque projet (moteur compatible **SimulAr v2.5**, de Luciano Machain,
UNR/Argentine) : chaque flux de trésorerie devient une **variable aléatoire** et tout le portefeuille est recalculé
itération après itération. À la fin, vous n'avez pas un nombre — vous avez **toute la distribution de votre argent** :

- **`P(VAN < 0)`** — la probabilité réelle de perte. Le nombre que personne ne vous montre.
- **VaR 5 %** — le pire scénario plausible : *« dans 19 futurs sur 20, je gagne au moins cela. »*
- **CVaR 5 %** — quand le désastre survient, combien il coûte en moyenne.
- **Tornado de sensibilité** — régression multiple et corrélation de Pearson : quelle variable meut vraiment votre VAN.
- **20 distributions** d'entrée, **matrice de corrélation** validée (Iman-Conover, qui préserve exactement les
  marginales) et **percentiles de 1 % à 99 %**, avec un histogramme à 100 classes identique à celui du manuel SimulAr.

Graine fixe : relancez et vous obtenez **exactement** le même résultat. Auditable — pas « magique ».

> **Le basculement :** vous cessez de choisir le projet à la plus forte VAN pour choisir **celui qui survit au mauvais
> scénario**. C'est la gestion du risque — ce qui sépare l'investisseur du parieur.

![Histograma de Monte Carlo do VPL — 10.000 iterações, 100 classes](docs/screenshots/mc-histograma.png)

| Distribution cumulée de la VAN | Tornado de sensibilité |
|---|---|
| ![Distribution cumulée de la VAN](docs/screenshots/mc-acumulado.png) | ![Tornado de sensibilité](docs/screenshots/mc-tornado.png) |

---

## 🧮 Cinq écoles de décision. Un seul verdict.

Une méthode peut se tromper. Cinq méthodes d'accord, non.

Suivant l'architecture de **John (2025)** — *Integration of DEMATEL with Other MCDM Methods* —, **DEMATEL** cartographie
la structure causale entre les critères et sépare les **causes** (leviers où agir) des **effets** (thermomètres de ce qui
a déjà été fait). De ces boucles d'influence naissent les **poids** : non arbitrés, mais **dérivés de la structure du
problème**. Ils alimentent quatre écoles rivales :

| Méthode | École | Ce qu'elle demande |
|---|---|---|
| **ELECTRE I** | Surclassement | « Qui surclasse qui — et qui survit sans être dominé ? » |
| **PROMETHEE II** | Surclassement | « Quel est le flux net de préférence de chaque projet ? » |
| **MAUT** | Utilité | « Lequel maximise l'utilité d'un décideur averse au risque ? » |
| **MCDA-C** | Constructiviste | « Qui est au-dessus du niveau *Bon* — et qui sous le *Neutre* ? » |
| **AHP-TOPSIS 2n** | Distance à l'idéal | « Qui est le plus proche de la solution idéale dans les deux normalisations ? » |

Le gagnant sort du **consensus de Borda** des cinq, déjà **ajusté au risque** par Monte-Carlo. Et quand les méthodes
**divergent**, le tableau de bord montre la divergence — car c'est une information : le choix est sensible à l'école de
décision et mérite l'œil du décideur.

| DEMATEL — causes × effets | Rang par méthode |
|---|---|
| ![DEMATEL — causes × effets](docs/screenshots/dematel.png) | ![Rang par méthode](docs/screenshots/mcdm-metodos.png) |

### 💼 Ce que cela change au quotidien — de l'indépendant à la corporation

Peu importe que vous payiez **20 US$ sur un plan PRO** ou **200 000 US$ en contrats entreprise** : les mathématiques du
gaspillage sont les mêmes — seul le nombre de zéros change.

| | **PME / indépendant** | **Grande entreprise** |
|---|---|---|
| **La vraie douleur** | 3 abonnements, zéro visibilité, trésorerie tendue | 40 pilotes d'IA, aucun avec un P&L attribué |
| **Monte-Carlo livre** | *« ce projet a 12 % de risque de perdre de l'argent, et le mauvais mois coûte 3 400 US$ »* | VaR/CVaR par unité d'affaires : risque agrégé et auditable, pas une anecdote |
| **Le MCDM livre** | lequel des 3 projets déployer **en premier**, avec l'argent qui existe | lequel des 40 pilotes devient un produit — défendable en comité, méthode explicite |
| **Le gain dès demain** | résilier l'abonnement qui ne se rembourse pas, dès cette semaine | réallouer le budget sur **preuve**, non sur politique interne |

**En pratique :** le **tornado** désigne la variable qui meut le résultat — donc **où investir votre prochaine heure de
travail**. Le **DEMATEL** révèle que réduire l'hallucination (IITA) est une **cause**, pas un symptôme : agissez là et
VAN, TRI et risque s'améliorent *ensemble*. C'est la gestion de l'IA qui cesse d'être une opinion pour devenir de
l'**ingénierie**.


---

## 🌐 12 langues

Le tableau de bord, les pages par projet **et le texte à l'intérieur des images** des graphiques sont localisés en
**12 langues** : Português · English · Español · Français · Deutsch · 中文 · 한국어 · हिन्दी · עברית · Svenska · Русский · Suomi.
La traduction est pilotée par une **Translation Memory** (style SDL Trados) qui standardise et accélère les nouvelles langues.

---

## 🙋 Objections (les questions que vous vous posez maintenant)

- **« Je n'ai pas le temps. »** → Cinq minutes avec `./run_all.sh --mock` et le tableau de bord tourne sur votre
  écran. Mesurer vous **rend** les heures que vous perdez déjà en reprises et hallucinations.
- **« C'est trop complexe. »** → Une ligne. Le framework fait l'ETL, les calculs, le classement et les images ;
  **vous lisez juste le verdict.**
- **« Mon opération d'IA est petite. »** → Justement, chaque dollar pèse davantage. Petit aujourd'hui, portefeuille
  demain — **mesurez avant de déployer le gaspillage.**
- **« Je n'utilise pas Langfuse. »** → La démo tourne **100 % sans Langfuse**. Pour des données réelles, vous
  branchez **votre** compte (jamais le mien).
- **« Ce n'est qu'un tableau de bord de plus. »** → Non. C'est **Balanced Scorecard + analyse d'investissement
  (VAN/TRI/TRIM/AÉ) + décision multicritère (AHP-TOPSIS)** — des instruments de conseil, pas de la décoration.
- **« Et la confidentialité de mes données ? »** → La démo est **100 % anonyme** (Project A…J) ; données/noms réels
  et clés restent **hors du paquet**. Vous exécutez **en local**, avec **votre** compte.
- **« Combien ça coûte ? »** → **Rien.** Open source, sur votre machine. Le seul prix, c'est de continuer à **ne
  pas mesurer** — et celui-là, vous le payez déjà.

---

## 🧩 Skills incluses (*build & analyze your own*)

Ce dépôt embarque des **Skills** réutilisables (Claude Code) :

- **`measuring-ai-projects`** — définir/mesurer/rapporter les KPI de projets d'IA (le cœur de ce framework).
- **`github-benchmark-analyzer`** — analyser et benchmarker **n'importe quel** dépôt/profil GitHub (étoiles, forks,
  abonnés, hashtags, style de README, mots-clés, langages) et extraire ce que les leaders ont en commun.
  **Construisez et analysez votre propre portefeuille** — même face au marché.

---

## 📚 Ressources & références (Awesome)

Les épaules de géants sur lesquelles ce framework s'appuie :

- **Stratégie & mesure :** Kaplan & Norton — *The Balanced Scorecard* · Peter Drucker (management par objectifs).
- **Lean Six Sigma :** taxonomie des 8 gaspillages (Muda), PDCA/Kaizen, Ishikawa/RCA.
- **Finance d'entreprise :** Lawrence Gitman — *Principes de gestion financière* (VAN, TRI, TRIM, IP).
- **Décision multicritère :** Thomas Saaty (**AHP**) · Hwang & Yoon (**TOPSIS**).
- **Stack technique :** [Langfuse](https://langfuse.com) (LLM observability) · [Evidence](https://evidence.dev)
  (BI as Code) · [Rust/PyO3](https://pyo3.rs) · [Tectonic](https://tectonic-typesetting.github.io) (LaTeX).

---

## 🗺️ Feuille de route

- [x] Pipeline Langfuse → SQLite → Evidence + Rust
- [x] 70+ KPI (BSC + économie d'API + Lean) · EVM
- [x] Financier (VAN, TRI, TRIM, AÉ, IP, délai de récupération, dollarisation)
- [x] AHP-TOPSIS 2n + Dossier administratif (6 outils)
- [x] Tableau de bord et images en **12 langues**
- [ ] Connecteurs d'observabilité supplémentaires (OpenTelemetry, Helicone)
- [ ] Mode SaaS multi-tenant + planification native
- [ ] Publication du tableau de bord statique (GitHub Pages)

---

## 🤝 Contribuer

Les contributions sont **très bienvenues** ! Ouvrez une *issue* décrivant votre proposition (nouveau KPI,
connecteur, langue, correction) et envoyez une *pull request*. Standards : code lisible et cohérent avec son
environnement, aucune donnée personnelle dans le paquet (la démo est anonyme). Nouvelles langues : ajoutez les
cibles à la Translation Memory et lancez le générateur.

## 📄 Licence & paternité

© **Bruno Penedo** — 2026. Usage, étude et contribution encouragés ; pour un usage commercial/redistribution,
consultez l'auteur. *(Une licence OSS formelle peut être ajoutée — ouvrez une issue avec votre préférence.)*

## 🏷️ Topics
`awesome-list` · `education` · `resources` · `computer-science` · `python` · `business-intelligence` ·
`llmops` · `finops` · `aiops` · `programming` · `development` · `lists` · `free` · `unicorns` · `dashboard` ·
`balanced-scorecard` · `langfuse` · `llm-observability` · `kpi` · `project-management`

---

⭐ **Si ce framework éclaire votre dépense en IA, laissez une étoile — et commencez à tirer profit de ce que vous payez déjà.**

---

**Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard** · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
