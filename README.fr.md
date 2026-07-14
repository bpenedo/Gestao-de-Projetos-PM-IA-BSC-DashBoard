# 🧭 Gestão de Projetos PM IA BSC DashBoard (Build and Analyze Your Own AI Portfolio Projects)

<p align="center">
  <img src="docs/hero.jpg" alt="Gestion de Projets PM IA BSC DashBoard" width="820">
</p>

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
- [🔬 Le signal est en amont — et c'est là que réside le levier](#-le-signal-est-en-amont--et-cest-là-que-réside-le-levier)
- [🎓 Fondements : ce qu'est Monte-Carlo et ce qu'est la décision multicritère](#-fondements--ce-quest-monte-carlo-et-ce-quest-la-décision-multicritère)
- [🌐 12 langues](#-12-langues)
- [🙋 Objections (les questions que vous vous posez maintenant)](#-objections-les-questions-que-vous-vous-posez-maintenant)
- [🧩 Skills incluses](#-skills-incluses-build--analyze-your-own)
- [📚 Ressources & références](#-ressources--références-awesome)
- [🗺️ Feuille de route](#️-feuille-de-route)
- [🧰 Installation pas à pas (en local, depuis zéro)](#-installation-pas-à-pas-en-local-depuis-zéro)
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

Nous sommes les **pionniers** d'un territoire nouveau — la **frontière entre l'intelligence artificielle et l'intelligence financière à haute valeur**. Tels des explorateurs cartographiant des terres encore vierges, ce framework est la
**boussole** (🧭) qui transforme le brouillard des abonnements en **routes claires de retour** : chaque token, un
mille ; chaque projet, une expédition vers le profit. Là où il y avait un coût aveugle naît une **opportunité
mesurable** ; là où il y avait un tableur mort fleurit une **thèse d'investissement vivante**.

### 🚀 Pour les Micro-SaaS, SaaS, startups et solopreneurs

Voici ce que personne ne vous a dit quand vous avez intégré l'IA à votre produit : **vous venez de déplacer l'IA
de votre budget marketing vers votre COGS.** Et un COGS qui croît avec l'usage n'est pas une dépense — c'est une
**hypothèque sur votre marge brute**. Chaque nouvel utilisateur coûte désormais des tokens. Chaque relance due à
une hallucination brûle la marge deux fois. Et la facture n'arrive qu'en fin de mois, trop tard pour défaire.

| Vous êtes… | La douleur que personne ne mesure | Ce que ce framework vous rend |
|---|---|---|
| **Solopreneur** | vous *êtes* l'équipe ; votre heure est l'actif le plus cher qui soit | le **tornado** désigne la variable qui meut le résultat — donc **où investir votre prochaine heure** |
| **Micro-SaaS** | le coût des tokens croît avec l'usage et ronge la marge en silence | une distribution **ajustée à vos tokens réels** + **CVaR** : le mauvais mois a un prix *avant* d'arriver |
| **SaaS à l'échelle** | chaque fonctionnalité d'IA est un projet qui se bat pour la même feuille de route | **cinq méthodes** élisent laquelle sort — et la **robustesse** dit si la 1re place survit à une erreur de 2 points sur un poids |
| **Startup en levée** | l'investisseur n'achète pas *« on utilise l'IA »* | il achète **VAN, TRI, délai de récupération et `P(VAN<0)`** — et le **pitch deck sort prêt**, en LaTeX |

**Ce qui change vraiment.** Votre marge brute cesse d'être une estimation et devient une **distribution à queue
valorisée**. Votre runway cesse d'être une simple division et gagne une **VaR** : *« dans 19 scénarios sur 20,
ma trésorerie tient au moins N mois. »* Et à l'heure du board deck ou de la due diligence, vous n'ouvrez pas un
tableur irreproductible — vous ouvrez un chiffre à **graine fixe**, que n'importe quel associé, investisseur ou
auditeur relance et obtient **exactement identique**.

> **Repositionnement brutal :** le solopreneur se met à décider comme un directeur financier. Et le directeur
> financier se met à décider à la vitesse d'un solopreneur.

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
<!-- eixo-execucao -->
- **📅 Planning Monte-Carlo (PERT) + Gantt :** le même moteur de Monte-Carlo appliqué aux **durées des tâches** — distribution de la date de fin, **P80** (l'engagement recommandé par le PMI), `P(dans les délais)` et **chemin critique** avec **indice de criticité** (dans quel % des 10 000 simulations chaque tâche est critique — ce que le CPM déterministe cache).
- **📐 Earned Value Management + Earned Schedule :** **SPI · CPI · EAC · ETC · VAC · TCPI** et la **courbe en S** (PV/EV/AC). Unit **coût + délai + périmètre** dans un seul cadre. Le **SPI(t)** corrige le défaut connu du SPI, qui converge vers 1 à la fin même si le projet est en retard.
- **⚙️ Santé d'exécution de l'IA dans le temps :** latence **p50/p95/p99** face à un **SLO**, **token budget burndown**, **régression de qualité** (règle type SPC) et **dérive du modèle** par **Kolmogorov-Smirnov** — le tout depuis les logs **réels** de Langfuse.
- **🚨 Registre des risques + matrice Probabilité × Impact :** le risque *qualitatif* exigé par tout PMO, avec propriétaire, déclencheur et mitigation. Les probabilités sont **ancrées dans des signaux réels** (violations de SLO, CPI, dérive), pas devinées.
- **🌊 Métriques de flux (Kanban) :** **CFD**, **cycle time P50/P85** (prévision par percentile, pas au doigt mouillé), **throughput** et **WIP**.

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

### 📅 Axe d'exécution — planning, valeur acquise, santé de l'IA, risque et flux

**Gantt avec chemin critique** — les barres rouges sont le chemin critique ; le **%** sur chaque tâche est l'*indice de criticité* : dans quel pourcentage des 10 000 simulations cette tâche a dicté le délai.

![Gantt avec chemin critique — les barres rouges sont le chemin critique](docs/screenshots/cronograma-gantt.png)

**Risque de délai** — la distribution de la date de fin, avec l'échéance, le **P50** et le **P80**. Engagez-vous sur le P80, pas sur l'estimation déterministe (optimiste à cause du biais de convergence).

![Risque de délai — la distribution de la date de fin, avec l'échéance, ](docs/screenshots/cronograma-risco-prazo.png)

**Courbe en S de l'EVM** — PV (planifié) · EV (acquis) · AC (coût réel). EV sous PV = retard ; AC au-dessus d'EV = dépassement.

![Courbe en S de l'EVM — PV (planifié) · EV (acquis) · AC (coût réel). E](docs/screenshots/evm-curva-s.png)

**Latence sous SLO** — p50/p95/p99 par jour, depuis les logs réels. Ligne franchie, service dégradé.

![Latence sous SLO — p50/p95/p99 par jour, depuis les logs réels. Ligne ](docs/screenshots/exec-latencia-slo.png)

**Matrice de risque P × I** — bulle = exposition (P×I). Probabilité ancrée dans les signaux réels du projet.

![Matrice de risque P × I — bulle = exposition (P×I). Probabilité ancrée](docs/screenshots/risco-matriz-pi.png)

**Cumulative Flow Diagram** — bandes parallèles = flux sain ; une bande qui grossit = goulot / WIP bloqué.

![Cumulative Flow Diagram — bandes parallèles = flux sain ; une bande qu](docs/screenshots/fluxo-cfd.png)

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

Ce framework simule **10 000 futurs** pour chaque projet : chaque flux de trésorerie devient une **variable aléatoire** et tout le portefeuille est recalculé
itération après itération. À la fin, vous n'avez pas un nombre — vous avez **toute la distribution de votre argent** :

- **`P(VAN < 0)`** — la probabilité réelle de perte. Le nombre que personne ne vous montre.
- **VaR 5 %** — le pire scénario plausible : *« dans 19 futurs sur 20, je gagne au moins cela. »*
- **CVaR 5 %** — quand le désastre survient, combien il coûte en moyenne.
- **Tornado de sensibilité** — régression multiple et corrélation de Pearson : quelle variable meut vraiment votre VAN.
- **20 distributions** d'entrée, **matrice de corrélation** validée (Iman-Conover, qui préserve exactement les
  marginales) et **percentiles de 1 % à 99 %**, avec un histogramme à 100 classes.

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

## 🔬 Le signal est en amont — et c'est là que réside le levier

Je l'ai découvert en mesurant le framework lui-même : le tornado de sensibilité de la VAN renvoyait
**exactement** `1,0 · 0,9091 · 0,8264 · 0,7513…` — les facteurs d'actualisation `1/(1+i)ᵗ`. Comme la VAN est
**linéaire** dans les flux, simuler les seuls flux n'apprend rien au-delà du taux. **Le vrai signal stochastique est
en amont : dans les tokens.**

### 1️⃣ Cessez d'arbitrer la distribution. Ajustez-la à vos données.

Onze distributions candidates sont ajustées par **maximum de vraisemblance** à votre série réelle de consommation de
tokens (`logs_langfuse`). Celle au **plus faible AIC** l'emporte — l'AIC pénalise chaque paramètre superflu et évite
le surajustement — et le test de **Kolmogorov-Smirnov** mesure l'adéquation. C'est le classique *ajustement de distributions aux données*, et c'est ce qui révèle la **queue lourde** de la consommation : certains prompts coûtent 10× le typique,
et c'est cette queue qui fait exploser le budget — invisible pour qui utilise la moyenne.

**Et quand l'ajustement est mauvais, le framework crie.** Si la p-valeur du KS tombe sous 0,05, l'écran affiche
`ADÉQUATION FAIBLE` en rouge, plutôt que de feindre la précision. Un chiffre honnête vaut mieux qu'un beau chiffre.

![Ajustement de distributions aux tokens réels — 11 candidates, sélection par AIC, adéquation par Kolmogorov-Smirnov](docs/screenshots/ajuste-distribuicoes.png)

### 2️⃣ Votre classement survit-il à une erreur de 2 points sur un poids ?

Toute méthode multicritère renvoie un gagnant avec une **confiance implicite de 100 %**. Mais les poids sont des
estimations, pas des vérités révélées. Si deux points de pourcentage sur le poids de l'IITA échangent la 1re et la
2e place, le « gagnant » est un artefact de la calibration.

Nous perturbons donc les poids du DEMATEL par une **Dirichlet** — `w' ~ Dir(κ·w)`, qui vit exactement sur le simplexe
et préserve `E[w'] = w`, perturbant **sans biaiser** — et nous reclassons **2 000 fois**. Le verdict change de nature :

> *« Project C est le meilleur »* ⟶ **« Project C gagne dans 99,9 % des univers de préférence plausibles »**

C'est un **intervalle de confiance sur la décision elle-même**. Et il expose ce que le consensus masquait : sur
l'écran ci-dessous, **PROMETHEE II élit le leader dans seulement 25,4 % des univers**. Quatre écoles s'accordent ;
une dissent frontalement. Ce n'est pas du bruit — c'est l'avertissement que le choix dépend de votre préférence pour
le *surclassement* plutôt que l'*utilité*. Aucun classement seul ne vous le dirait.

![Robustesse du classement par perturbation de Dirichlet — probabilité de victoire et divergence entre écoles](docs/screenshots/robustez-dirichlet.png)

### ⚡ Le levier concret

| Ressource | Avant | Après |
|---|---|---|
| **Temps** | des semaines à débattre du projet à déployer | le verdict arrive avec une probabilité — le débat s'achève en une réunion |
| **Calcul** | 10 000 itérations × 10 projets, vectorisées en NumPy | quelques secondes, sur votre machine, sans cloud ni coût |
| **Capital** | budget alloué par conviction | alloué par `P(victoire)` et `VaR` — le pire cas déjà valorisé |
| **Réputation** | *« je pense que c'est celui-ci »* | *« il gagne dans 99,9 % des scénarios ; voici la méthode qui dissent, et pourquoi »* |
| **Auditabilité** | un tableur irreproductible | graine fixe : n'importe qui relance et obtient **exactement** le même nombre |

### 💼 Du forfait à 20 US$ au contrat à 200 000 US$

**Si vous êtes indépendant ou PME :** la distribution ajustée vous dit **ce que coûtera le mauvais mois de tokens**
avant qu'il n'arrive — et la robustesse vous dit s'il vaut vraiment la peine de basculer l'effort sur l'autre projet,
ou si les deux sont à égalité dans la marge d'erreur. Vous cessez d'optimiser à l'aveugle avec une trésorerie tendue.

**Si vous êtes une grande entreprise :** `P(victoire)` est la pièce manquante du comité d'investissement. Elle
transforme *« l'équipe A défend le projet X »* en **« le projet X gagne sous 99,9 % des calibrations de poids
défendables, et la seule école dissidente est le surclassement, sur le critère Y »**. Le débat politique devient
**débat technique** — et le directeur financier obtient un chiffre qui survit à l'audit.

> **Le basculement final :** le framework cesse de mesurer le risque de l'**argent** et se met à mesurer le risque de
> la **décision elle-même**. Très peu d'endroits au monde le font.

---

## 🎓 Fondements : ce qu'est Monte-Carlo et ce qu'est la décision multicritère

### 🎲 Simulation mathématique de Monte-Carlo

#### 📖 Le concept

Monte-Carlo est une méthode numérique qui répond aux questions sur les systèmes incertains **par échantillonnage
aléatoire**. L'idée inverse l'instinct du mathématicien : au lieu de déduire la réponse sous **forme fermée** — résoudre
l'intégrale, la combinatoire, l'équation différentielle —, on construit un **modèle**, on tire des milliers de
réalisations des variables incertaines et l'on **compte simplement ce qui s'est passé**. Ce que l'on obtient au bout
n'est pas un nombre : c'est la **loi de probabilité du résultat**.

Deux lois la soutiennent. La **loi des grands nombres** garantit que la moyenne des simulations converge vers la vraie
valeur. Le **théorème central limite** en donne la vitesse : l'erreur-type décroît en `1/√N`. La conséquence est honnête
et un peu cruelle — **pour doubler la précision, il faut quadrupler les itérations**. Monte-Carlo n'est pas rapide. Sa
vertu est ailleurs : l'erreur **ne dépend pas de la dimension du problème**. Les méthodes déterministes de quadrature
souffrent du *fléau de la dimension* et s'effondrent avec des dizaines de variables ; Monte-Carlo, non. Elle l'emporte
précisément là où les mathématiques analytiques meurent.

#### 📖 Où et quand elle est née

**Los Alamos, Nouveau-Mexique, 1946.** Le mathématicien polonais **Stanisław Ulam**, convalescent d'une encéphalite,
passait ses journées à jouer au solitaire. Il se demanda quelle était la probabilité de gagner une partie. Il tenta la
combinatoire et renonça : intraitable. Puis lui vint une idée si simple qu'elle ressemblait à une triche — **jouer cent
parties, compter les victoires et diviser**. Il comprit aussitôt que ce n'était pas un tour de cartes : c'était une
**méthode générale d'intégration** pour des problèmes que nul ne savait résoudre.

Il porta l'idée à **John von Neumann**, qui vit immédiatement son application au problème qui les occupait dans le projet
Manhattan : la **diffusion des neutrons** en milieu fissile. Simuler la marche aléatoire de milliers de neutrons —
diffusion, absorption, fission — était faisable ; résoudre l'équation de transport ne l'était pas. **Nicholas Metropolis**
proposa le nom **« Monte-Carlo »**, en référence au casino monégasque où un oncle d'Ulam empruntait de l'argent pour
jouer. L'**ENIAC** rendit les premiers calculs possibles, et en **1949** Metropolis et Ulam publièrent *« The Monte Carlo
Method »* dans le *Journal of the American Statistical Association*.

La méthode est née, littéralement, de la rencontre d'un **jeu de cartes** et de la **bombe atomique**. Peu d'idées
scientifiques ont un acte de naissance aussi déconcertant.

#### 📖 La méthodologie, en cinq étapes

1. **Modéliser.** Écrire la sortie comme fonction des entrées : `y = f(x₁, …, xₙ)`.
2. **Attribuer des lois.** Chaque entrée incertaine reçoit une loi. S'il existe des **données historiques**, elle y est
   *ajustée* ; sinon, elle est postulée — et cela doit être **déclaré**.
3. **Échantillonner.** Tirer `N` scénarios. Si les variables sont **corrélées**, le tirage doit respecter cette structure :
   tirer indépendamment là où existe une dépendance réelle est l'erreur la plus courante de la méthode.
4. **Propager.** Calculer `f` dans chaque scénario. C'est ici que l'incertitude des entrées **devient** celle de la
   sortie, sans aucune approximation linéaire.
5. **Analyser.** Étudier la distribution : moyenne et écart-type, **percentiles**, probabilité d'événements (`P(y < 0)`),
   la **queue** (VaR, CVaR) et la **sensibilité** (quel `xᵢ` meut `y`).

#### 📖 Usages et applications dans le monde

- **Finance :** valorisation d'options exotiques (sans forme fermée), **VaR** et **CVaR** de portefeuilles, tests de
  résistance réglementaires (Bâle), risque de crédit.
- **Ingénierie :** fiabilité structurelle, tolérances de fabrication, analyse de défaillances des systèmes complexes.
- **Gestion de projet :** risque de délai et de coût (l'évolution probabiliste du PERT), courbes en S d'achèvement.
- **Physique et chimie :** transport de particules, blindage contre les rayonnements, mécanique statistique.
- **Opérations et chaînes d'approvisionnement :** files d'attente, stocks, capacité sous demande incertaine.
- **Épidémiologie :** propagation des maladies et évaluation des politiques sous incertitude.
- **Au sein même de l'IA :** **MCMC** (inférence bayésienne), **MCTS** — la recherche arborescente qui mena AlphaGo à
  battre Lee Sedol — et le *Monte Carlo dropout* pour estimer l'incertitude des réseaux de neurones.

#### 🔒 Méthodologie, usage et application EXCLUSIFS à ce projet

Ici, Monte-Carlo n'est pas un ornement académique : c'est le **moteur de risque** du portefeuille.

- **Les entrées.** Chaque flux de trésorerie périodique devient une variable **triangulaire** (`min`, `mode`, `max`), de
  mode égal à la valeur déterministe et de queues à ±30 %. La **consommation de tokens** — la seule variable vraiment à
  queue lourde — **n'est pas postulée** : onze lois candidates sont **ajustées par maximum de vraisemblance** à votre
  série réelle `logs_langfuse`, celle au **plus faible AIC** l'emporte, et l'adéquation est mesurée par
  **Kolmogorov-Smirnov**. Si la p-valeur tombe sous 0,05, l'écran affiche `ADÉQUATION FAIBLE` en rouge au lieu de feindre
  la précision.
- **La corrélation.** Quand les flux sont dépendants, l'échantillonnage utilise **Iman-Conover**, qui impose la
  corrélation des rangs **en préservant exactement les lois marginales**. La matrice est validée au préalable : symétrique,
  diagonale unitaire, définie positive.
- **La propagation.** **10 000 itérations** par projet, avec **graine fixe (42)** : relancer redonne exactement le même
  nombre. Ce n'est pas un détail — c'est ce qui rend le résultat **auditable** par un associé, un investisseur ou un
  auditeur.
- **Les sorties.** Pas seulement la VAN : nous simulons **VAN, TRI, TRIM, AÉ, IP** et le **coût des tokens**, chacun avec
  les dix statistiques descriptives classiques (asymétrie et aplatissement selon les définitions d'Excel), les
  **percentiles de 1 % à 99 %** et un **histogramme à 100 classes**.
- **Le risque qui compte.** `P(VAN < 0)` est la vraie probabilité de perte. La **VaR 5 %** est le pire scénario plausible
  — *« dans 19 futurs sur 20, je gagne au moins cela »*. La **CVaR 5 %** répond à ce que personne ne demande : quand le
  désastre survient, **combien coûte-t-il en moyenne**.
- **La sensibilité.** Le **tornado** est calculé sous ses deux formes classiques : les **bêtas d'une régression multiple**
  (l'effet de +1 sur une entrée sur la VAN) et la **corrélation de Pearson** (à quel point l'incertitude de cette entrée
  dicte celle de la VAN). Lectures complémentaires ; le tableau de bord montre les deux.
- **Une découverte du framework sur lui-même.** En se mesurant, le tornado a renvoyé des bêtas **exactement égaux aux
  facteurs d'actualisation** `1/(1+i)ᵗ` — car la VAN est *linéaire* dans les flux. Simuler les seuls flux n'apprend donc
  rien au-delà du taux. **Le vrai signal stochastique est en amont, dans les tokens.** C'est ce constat qui a motivé
  l'ajustement des lois aux données réelles.
- **Le risque nourrit la décision.** Deux sorties de Monte-Carlo entrent comme **critères** dans le modèle multicritère :
  `P(VAN<0)` comme critère de **coût** et la **VaR 5 %** comme critère de **bénéfice**. Le choix final naît donc déjà
  **ajusté au risque**, et non seulement à l'espérance.


**Ce que c'est.** Une méthode qui répond aux questions difficiles **par tirage au sort**. Au lieu de résoudre sous
forme fermée les mathématiques d'un système incertain — souvent impossible —, on attribue des **lois de
probabilité** aux variables d'entrée, on tire des milliers de scénarios, on calcule le résultat de chacun et l'on
observe la **distribution entière** des sorties. La loi des grands nombres garantit la convergence ; l'erreur décroît
en `1/√N`, autrement dit **quadrupler les itérations divise l'erreur par deux**.

**Comment c'est né.** Los Alamos, 1946. **Stanisław Ulam**, en convalescence, jouait au solitaire et se demanda
quelle était la probabilité de gagner. Il comprit que résoudre la combinatoire était brutal — mais que **simuler**
des centaines de parties et simplement compter était trivial. Il porta l'idée à **John von Neumann**, et tous deux
l'appliquèrent au problème qui les occupait dans le projet Manhattan : la **diffusion des neutrons** dans un matériau
fissile. **Nicholas Metropolis** baptisa la méthode « Monte-Carlo », en référence au casino monégasque où un oncle
d'Ulam jouait. L'**ENIAC** rendit les premiers calculs possibles. La méthode est née, littéralement, de la rencontre
entre un jeu de cartes et la bombe atomique.

**Où l'utilise-t-on aujourd'hui.** Valorisation d'options et calcul de **VaR** en finance ; fiabilité structurelle en
ingénierie ; risque de délai et de coût en gestion de projet ; physique des particules ; chaînes d'approvisionnement ;
épidémiologie. Et au sein même de l'IA : **MCMC** (inférence bayésienne) et **MCTS** — la recherche arborescente qui
a mené AlphaGo à battre Lee Sedol.

**Ce que cela nous apporte ici.** Chaque flux de trésorerie devient une variable aléatoire, et la consommation de
tokens reçoit la loi **ajustée à vos données réelles**. Nous lançons 10 000 scénarios et, au bout, vous n'avez pas une
VAN — vous avez la **distribution de votre argent** : `P(VAN < 0)` (la vraie probabilité de perte), **VaR 5 %** (le
pire scénario plausible), **CVaR 5 %** (ce que cela coûte quand le désastre survient) et le **tornado** (quelle
variable meut réellement le résultat). La moyenne ment ; la queue décide.

### 🧮 Analyse de décision multicritère (MCDA)

#### 📖 Le concept et son utilité

Choisir entre des projets est difficile pour deux raisons qu'aucun tableur ne résout. D'abord, les critères
**s'opposent** : le projet à la plus forte VAN est souvent le plus risqué. Ensuite, ils sont **incommensurables** : aucune
arithmétique honnête n'additionne des euros, un pourcentage d'hallucination et des heures de reprise.

La MCDA (*Multi-Criteria Decision Analysis*) est le champ — né dans les années 1960-70, à la frontière de la recherche
opérationnelle et de la théorie de la décision — qui affronte précisément cela. Elle **ne promet pas la bonne réponse**.
Elle promet mieux : rendre le choix **explicite, auditable et défendable**.

Sa thèse fondatrice est inconfortable et libératrice : **il n'existe pas de « meilleur » dans le vide.** Il existe un
meilleur *étant donné un système de préférences que quelqu'un a explicité*. Tout décideur opère déjà avec un système de
préférences — la différence est que, sans MCDA, il est **implicite, incohérent et non auditable**. Échanger l'opinion
tacite contre un modèle explicite : voilà tout le gain.

#### 📖 Usages et applications dans le monde

Sélection de fournisseurs et priorisation de portefeuille ; choix de technologies énergétiques (solaire × éolien ×
biomasse) ; implantation d'usines, d'hôpitaux et de décharges ; évaluation d'impact environnemental ; politiques publiques
et allocation budgétaire ; sélection du personnel ; priorisation de la maintenance ; et — de plus en plus — **évaluation
technico-économique** des technologies émergentes, ce qui est exactement le cas d'un portefeuille de projets d'IA.

#### 📖 Les trois écoles de décision

- **École américaine (valeur et utilité).** Agrège tout en un **nombre unique**. Suppose qu'une mauvaise note sur un
  critère peut être **compensée** par d'excellentes ailleurs. Simple, puissante — et parfois dangereuse. `AHP`, `MAUT`.
- **École européenne (surclassement).** Fondée par **Bernard Roy**. Admet que deux alternatives puissent être
  **incomparables** et autorise le **veto** : une performance catastrophique sur un critère **ne s'achète pas** avec
  l'excellence ailleurs. Elle modélise l'hésitation réelle du décideur par des **seuils**. `ELECTRE`, `PROMETHEE`.
- **École constructiviste.** Le modèle n'est pas *découvert*, il est **construit avec le décideur**, par la structuration
  du problème et des échelles ancrées sur des niveaux de référence. `MCDA-C`.

#### 📖 1. DEMATEL — *Decision-Making Trial and Evaluation Laboratory*

**Ce que c'est.** Créé par **Gabus & Fontela** au **Battelle Memorial Institute** (Genève, 1972-73) pour étudier des
problèmes mondiaux complexes et enchevêtrés. Il **ne classe pas les alternatives** : il cartographie la **structure
causale entre les critères**.

**Comment ça marche.** Des experts remplissent une **matrice de relation directe** `Z` (à quel point le critère *i*
influence *j*, de 0 à 4). On normalise par `s = max(plus grande somme de ligne, plus grande somme de colonne)`, ce qui
donne la **matrice de relation totale** `T = X(I − X)⁻¹`, qui somme l'influence directe **et toutes les indirectes**, par
n'importe quel chemin. On en tire `R` (sommes des lignes) et `C` (sommes des colonnes) : **`R+C` est la proéminence**
(importance dans le système) et **`R−C` la relation** (positif = **cause** ; négatif = **effet**).

**Usage général.** Chaînes d'approvisionnement durables, freins à l'adoption technologique, analyse des risques systémiques.

**🔒 Dans ce projet.** DEMATEL répond à la question qui **précède** le classement : *« où dois-je agir ? »*. Il révèle que
**IITA (hallucination), PSR (santé) et IDLS (gaspillage Lean) sont des CAUSES**, tandis que **VAN, TRI, IP et les mesures
de risque sont des EFFETS**. C'est contre-intuitif et libérateur : poursuivre la VAN ne sert à rien — c'est un
**thermomètre**. Agissez sur l'hallucination et VAN, TRI et risque s'améliorent *ensemble*. De plus, les **poids** des
critères ne sont pas postulés : ils sont **dérivés de la structure d'influence**, via `wᵢ ∝ √((R+C)ᵢ² + (R−C)ᵢ²)`. Ces
poids alimentent les **cinq autres méthodes** — c'est le schéma d'intégration décrit par John (2025).

#### 📖 2. AHP-TOPSIS 2n — *Analytic Hierarchy Process* + *Technique for Order Preference by Similarity to Ideal Solution*

**Ce que c'est.** **Saaty (1977)** propose l'AHP : dériver les poids de **comparaisons par paires** entre critères, avec un
**test de cohérence** qui dénonce les jugements contradictoires (`CR ≤ 0,10`). **Hwang & Yoon (1981)** proposent TOPSIS :
la meilleure alternative est celle **la plus proche de la solution idéale** et **la plus éloignée de l'anti-idéale**.

**Comment ça marche.** On normalise la matrice de décision, on multiplie les colonnes par les poids, on calcule les
distances euclidiennes aux solutions idéale et anti-idéale, et le **coefficient de proximité** `Ci = d⁻/(d⁺+d⁻)` ordonne
le tout.

**Usage général.** Le duo le plus utilisé au monde en MCDM — de la sélection de fournisseurs à l'évaluation de performance.

**🔒 Dans ce projet.** Nous exécutons TOPSIS sous **deux normalisations** — vectorielle (euclidienne) et min-max (linéaire)
—, d'où le **« 2n »**. Chaque projet reçoit deux coefficients et le classement final est leur moyenne. On y gagne une
mesure que presque personne ne rapporte : la **concordance entre les normalisations**. Quand les deux divergent sur la
position d'un projet, son résultat est **fragile face à un choix technique arbitraire** — et le tableau de bord le montre.
La matrice de Saaty de ce projet a `CR = 0,0119`, bien en deçà de la limite de 0,10.

#### 📖 3. ELECTRE I — *ÉLimination Et Choix Traduisant la REalité*

**Ce que c'est.** **Bernard Roy (1968)**, au cabinet SEMA, à Paris. C'est le point zéro de l'école européenne du
surclassement. La question n'est pas *« quelle est la note de chacun ? »* mais *« **a** est-il au moins aussi bon que
**b** ? »*.

**Comment ça marche.** Pour chaque paire `(a, b)`, deux indices. La **concordance** `C(a,b)` somme les poids des critères
où `a` est au moins aussi bon que `b`. La **discordance** `D(a,b)` mesure le **plus grand désavantage** de `a` face à `b`.
On dit que `a` **surclasse** `b` si la concordance est élevée **et** la discordance faible. L'ensemble des alternatives que
**personne ne surclasse** est le **noyau** (*kernel*) — le menu des choix défendables.

**Usage général.** Décisions publiques et environnementales, où compenser un critère catastrophique serait inacceptable.

**🔒 Dans ce projet.** ELECTRE est la méthode qui **refuse de mentir par commodité**. Un projet à VAN stratosphérique et à
hallucination scandaleuse **n'achète pas** sa place : la **discordance** le bloque. Le framework rapporte le **noyau** —
les projets qu'aucun autre ne domine — et prend pour score le **degré de surclassement net** (combien il domine, moins
combien le dominent). C'est aussi la seule des six qui s'autorise à dire : *« ces deux projets sont tout simplement
**incomparables** »*.

#### 📖 4. PROMETHEE II — *Preference Ranking Organization METHod for Enrichment Evaluation*

**Ce que c'est.** **Jean-Pierre Brans (1982)**, affiné avec **Bernard Mareschal et Philippe Vincke (1985)**. Surclassement
également, mais avec une élégante bascule : au lieu d'un seuil binaire, on mesure **de combien** `a` est préféré à `b`.

**Comment ça marche.** Pour chaque critère, l'écart `d = g(a) − g(b)` passe par une **fonction de préférence** qui le
convertit en un degré entre 0 et 1. Brans a proposé **six fonctions généralisées** (usuelle, quasi-critère, seuil de
préférence, niveau, linéaire avec indifférence, gaussienne), paramétrées par un **seuil d'indifférence `q`** (en deçà
duquel l'écart est sans importance) et un **seuil de préférence `p`** (au-delà duquel la préférence est totale). On somme
les degrés pondérés : `φ⁺` mesure combien `a` domine les autres, `φ⁻` combien il est dominé, et le **flux net**
`φ = φ⁺ − φ⁻` produit un **préordre complet** (PROMETHEE II).

**Usage général.** Énergie, logistique, santé — chaque fois que graduer l'**intensité** de la préférence importe.

**🔒 Dans ce projet.** Nous employons la fonction **linéaire avec indifférence**, `q` et `p` étant estimés sur les quantiles
10 % et 90 % des écarts observés pour chaque critère. PROMETHEE répond *« de combien le gagnant est-il meilleur ? »*, et
non seulement *« est-il meilleur ? »*. Et c'est lui qui a produit la découverte la plus intéressante du portefeuille :
dans l'analyse de robustesse, **PROMETHEE II élit le leader du consensus dans seulement 25,4 % des univers de préférence**
— alors que les quatre autres écoles s'accordent. Le consensus **masquait une divergence d'école**.

#### 📖 5. MAUT — *Multi-Attribute Utility Theory*

**Ce que c'est.** **Ralph Keeney & Howard Raiffa (1976)**, héritiers directs de von Neumann et Morgenstern. C'est l'école
américaine sous forme axiomatique : si vos préférences obéissent à certains axiomes de rationalité, alors il existe une
**fonction d'utilité** qui les représente, et décider consiste à **maximiser l'utilité espérée**.

**Comment ça marche.** Chaque critère reçoit une **fonction d'utilité** `uⱼ` qui transforme la performance en satisfaction.
L'utilité globale est additive : `U(a) = Σ wⱼ · uⱼ(a)` — valable sous **indépendance additive** en préférence. Le point
crucial est la **forme** de la fonction : une `u` **concave** représente l'**aversion au risque** (le deuxième million vaut
moins que le premier) ; linéaire, la neutralité ; convexe, le goût du risque.

**Usage général.** Décisions médicales, politiques énergétiques, négociation — tout contexte où l'attitude face au risque
doit être **explicitée et défendue**.

**🔒 Dans ce projet.** Nous utilisons l'utilité **exponentielle** `u(z) = (1 − e^(−r·z)) / (1 − e^(−r))`, avec un coefficient
d'aversion `r = 2`. C'est un **choix éthique déclaré** : le framework est **conservateur**. Un gain incertain vaut moins
qu'un gain certain de même espérance — exactement comme l'évaluerait un directeur financier prudent. Là où TOPSIS traite
tous les gains comme fongibles, MAUT **pénalise la promesse élevée et incertaine**.

#### 📖 6. MCDA-C — *Aide multicritère à la décision — constructiviste*

**Ce que c'est.** Formalisée par **Leonardo Ensslin, Gilberto Montibeller et Sandra Noronha (2001)**, avec des racines chez
Roy et Bana e Costa. La prémisse est philosophique : le modèle **ne préexiste pas** au décideur. Il est **construit avec
lui**, en trois phases — **structuration** (cartes cognitives, descripteurs), **évaluation** (fonctions de valeur, taux de
substitution) et **recommandations**.

**Comment ça marche.** Chaque critère reçoit un **descripteur** à niveaux, dont deux sont des ancres : le niveau **Neutre**
(sous lequel la performance compromet) et le niveau **Bon** (au-dessus duquel il y a excellence). La fonction de valeur est
ancrée : `V = 0` au Neutre, `V = 100` au Bon, et elle **extrapole** librement hors de l'intervalle.

**Usage général.** Évaluation de la performance organisationnelle, gestion publique, contextes où le décideur doit
**apprendre** sur son propre problème.

**🔒 Dans ce projet.** Faute d'une session de structuration avec le décideur, nous ancrons les niveaux sur les **quartiles
observés** du portefeuille : `Neutre = Q1`, `Bon = Q3`. Cela préserve ce que MCDA-C a d'unique : elle ne fait pas
qu'**ordonner**, elle **classe** : `V < 0` est **compromettant**, `0 ≤ V ≤ 100` est **compétitif**, `V > 100` est
**excellence**. Un projet peut être premier au classement et se trouver malgré tout dans la bande compromettante. Aucune
autre méthode de cet ensemble ne vous le dirait.

#### 📖 Pourquoi cinq méthodes, et non une

Parce que **chaque école se trompe autrement**, et qu'une méthode seule renvoie un gagnant avec une **confiance implicite de
100 %** — ce qui est toujours un mensonge. AHP-TOPSIS compense trop ; ELECTRE parfois refuse de trancher ; MAUT dépend de la
forme de l'utilité ; MCDA-C dépend des ancres.

Nous exécutons les cinq avec les **mêmes poids** (ceux de DEMATEL) et concluons par un **consensus de Borda**. Dès lors, la
divergence entre elles cesse d'être une gêne et devient de l'**information** : quand quatre s'accordent et qu'une dissent
frontalement, ce n'est pas du bruit — c'est l'avertissement que votre choix **dépend de l'école de décision** que vous avez
implicitement adoptée.

#### 📖 La question finale : le verdict survit-il ?

Tout l'édifice ci-dessus repose sur des **poids**, et les poids sont des **estimations**. Si deux points de pourcentage sur
le poids de l'IITA échangent la 1re et la 2e place, le « gagnant » est un **artefact du calibrage**, non un fait du
portefeuille.

C'est pourquoi nous perturbons les poids de DEMATEL par une **Dirichlet** — `w' ~ Dir(κ·w)`, qui vit exactement sur le
simplexe et préserve `E[w'] = w`, perturbant **sans biaiser** — et reclassons **2 000 fois**. Le verdict change de nature :

> *« Project C est le meilleur »* ⟶ **« Project C gagne dans 99,9 % des univers de préférence plausibles »**

C'est un **intervalle de confiance sur la décision elle-même**. Ainsi, le framework cesse de mesurer seulement le risque de
l'**argent** et se met à mesurer le risque de la **décision**.


**Ce que c'est et à quoi ça sert.** Lorsque vous choisissez entre des projets, les critères **s'opposent** (une VAN
élevée s'accompagne souvent d'un risque élevé) et sont **incommensurables** (comment additionner des euros et un
pourcentage d'hallucination ?). La MCDA est le champ qui rend ce choix explicite, auditable et défendable. Sa thèse
fondatrice est inconfortable et libératrice : **il n'existe pas de « meilleur » dans le vide.** Il existe un meilleur
*étant donné un système de préférences que vous avez explicité*. Échanger l'opinion implicite contre un modèle
explicite : voilà tout le gain.

**Les trois écoles.** L'**américaine**, de valeur et d'utilité (AHP, MAUT) : agrège tout en un seul nombre.
L'**européenne**, du surclassement (ELECTRE, PROMETHEE), de Bernard Roy : admet que deux alternatives puissent être
**incomparables** et autorise le **veto** — une note désastreuse sur un critère ne s'achète pas avec d'excellentes
notes ailleurs. La **constructiviste** (MCDA-C) : le modèle n'est pas découvert, il est **construit avec le décideur**.

| Méthode | Origine | Question centrale | Ce qu'elle seule apporte | Dans le portefeuille d'IA |
|---|---|---|---|---|
| **DEMATEL** | Gabus & Fontela, Battelle (1972-73) | *« Qui influence qui ? »* | sépare **cause** et **effet** et dérive les **poids** de la structure d'influence elle-même | montre que réduire l'hallucination (IITA) est une **cause** — agissez là et VAN, TRI et risque s'améliorent ensemble |
| **AHP-TOPSIS 2n** | Saaty (1977) · Hwang & Yoon (1981) | *« Qui est le plus proche de la solution idéale ? »* | poids par comparaisons par paires avec **test de cohérence** (CR ≤ 0,10) | classe sous **deux normalisations** et rapporte leur concordance |
| **ELECTRE I** | Bernard Roy (1968) | *« Qui surclasse qui — et qui survit sans être dominé ? »* | **incomparabilité** et **veto** : un critère désastreux ne s'achète pas | isole le **noyau** des projets qu'aucun autre ne domine |
| **PROMETHEE II** | Brans & Vincke (1985) | *« Quel est le flux net de préférence ? »* | **six fonctions de préférence** avec seuils d'indifférence et de préférence | gradue *de combien* un projet est meilleur, pas seulement *s'il* l'est |
| **MAUT** | Keeney & Raiffa (1976) | *« Qu'est-ce qui maximise l'utilité du décideur ? »* | modélise l'**aversion au risque** par une utilité concave | pénalise les gains incertains — un décideur prudent ne les paie pas au même prix |
| **MCDA-C** | Ensslin, Montibeller & Noronha (2001) | *« Où est le niveau Bon, et où le Neutre ? »* | **fonction de valeur ancrée** : `V=0` au Neutre, `V=100` au Bon, avec extrapolation | classe en **compromettant / compétitif / excellence** au lieu de seulement ordonner |

**Pourquoi cinq, et non une.** Chaque école se trompe autrement. Une méthode seule renvoie un gagnant avec une
**confiance implicite de 100 %** — toujours un mensonge. En lançant les cinq et en concluant par un **consensus de
Borda**, la divergence devient de l'**information** : quand quatre s'accordent et qu'une dissent frontalement, ce
n'est pas du bruit — c'est l'avertissement que votre choix dépend de votre préférence pour le *surclassement* plutôt
que l'*utilité*. Et la **perturbation de Dirichlet** sur les poids répond à la question finale : *« la 1re place
survit-elle à une erreur de deux points de pourcentage dans le calibrage ? »*


### 🧪 Les quatre rouages : Iman-Conover, Kolmogorov-Smirnov, Dirichlet et le tornado

Les deux grandes méthodes ci-dessus reposent sur quatre pièces plus petites — et c'est en elles que se loge la différence
entre une simulation honnête et un joli chiffre. Elles méritent d'être connues.

#### 🔗 Iman-Conover — imposer la corrélation **sans détruire les lois**

**Ce que c'est.** Proposé par **Ronald Iman et William Conover (1982)**. Il résout un problème qui paraît trivial et ne
l'est pas : *comment tirer des variables corrélées lorsque les lois marginales ne sont pas normales ?* La voie naïve —
générer des normales corrélées par Cholesky puis les transformer — **déforme les marginales**. Or si vous venez d'ajuster
une LogNormale à vos données, la déformer jette précisément le travail accompli.

**Comment ça marche.** C'est une **réordination par rangs**, non une transformation de valeurs. On construit une référence
à partir des **scores de van der Waerden** `Φ⁻¹(i/(n+1))`, mélangés par colonne ; on calcule `P = chol(R)` (la cible) et
`Q = chol(corr(M))` (la corrélation accidentelle de la référence) ; on forme `S = M·(Q⁻¹P)ᵀ`. Chaque colonne de
l'échantillon initial est alors **réordonnée selon les rangs de `S`**. Comme seul l'*ordre* des valeurs déjà tirées change,
les **lois marginales restent exactes** — au bit près.

**Un détail fin, et honnête.** `R` est la corrélation de la *référence normale*, non celle de Pearson du résultat. La
corrélation des rangs induite suit la copule normale : `ρ_S = (6/π)·arcsin(R/2)`. Pour `R = 0,80`, cela donne **0,7859** —
exactement ce que nous avons mesuré en test (0,786). Ce n'est pas une erreur de la méthode ; c'est sa mathématique.

**Usages généraux.** Risque financier (actifs corrélés), fiabilité structurelle, échantillonnage par hypercube latin.

**🔒 Dans ce projet.** C'est ce qui permet de corréler les flux de trésorerie **sans sacrifier** la loi ajustée à vos tokens.
Avant usage, la matrice est validée : symétrique, diagonale unitaire et **définie positive** (via Cholesky). Une matrice de
corrélation incohérente est rejetée avec la plus petite valeur propre indiquée — plutôt que de produire silencieusement des
nombres dénués de sens.

#### 📏 Kolmogorov-Smirnov — la distance entre ce que vous **supposez** et ce que les données **disent**

**Ce que c'est.** Un test d'adéquation **non paramétrique**. La statistique est simple et belle : `D = sup |Fₙ(x) − F(x)|`,
le plus grand écart vertical entre la **fonction de répartition empirique** de vos données et la **théorique** que vous avez
proposée. Sous l'hypothèse nulle, la loi de `D` **ne dépend pas de quelle est `F`** — d'où *distribution-free*.

**Une réserve d'honnêteté méthodologique.** La p-valeur classique du KS suppose que les paramètres de `F` ont été fixés
**avant** de voir les données. Lorsqu'ils sont **estimés sur les mêmes données** (comme ici, par maximum de vraisemblance),
le test devient **optimiste** : il accepte trop facilement. La rigueur exigerait la correction de **Lilliefors** ou un
**bootstrap paramétrique**. Nous traitons donc le KS comme un **diagnostic**, non comme une preuve — et ne l'employons que
pour **rejeter** de mauvais ajustements, jamais pour déclarer un ajustement « correct ».

**Usages généraux.** Qualité d'ajustement ; comparaison de deux échantillons (KS à deux échantillons) ; détection de *drift*
de données dans les systèmes d'apprentissage automatique en production.

**🔒 Dans ce projet.** Il mesure à quel point la loi gagnante par AIC décrit réellement votre série de tokens. Quand la
p-valeur tombe sous 0,05, l'écran affiche **`ADÉQUATION FAIBLE` en rouge** — dans le portefeuille de démonstration cela se
produit pour l'un des projets, et le framework le **montre** au lieu de le cacher. Un chiffre honnête vaut mieux qu'un beau
chiffre.

#### 🎲 Perturbation de Dirichlet — l'**intervalle de confiance de la décision**

**Ce que c'est.** La loi de **Dirichlet** est la loi naturelle sur le **simplexe** : des vecteurs de nombres positifs dont la
somme vaut 1 — exactement ce qu'est un vecteur de poids. Elle est la conjuguée de la multinomiale et la généralisation de la
loi Bêta.

**Pourquoi elle, et non un bruit gaussien.** Ajouter un bruit normal à des poids produit des valeurs négatives et rompt la
somme unitaire. La Dirichlet vit *à l'intérieur* de l'espace valide. Et, paramétrée comme `w' ~ Dir(κ·w)`, elle possède deux
propriétés qui la rendent parfaite : `E[w'] = w` (elle perturbe **sans biaiser**) et `Var(w'ᵢ) = wᵢ(1−wᵢ)/(κ+1)` (la
dispersion se règle avec un seul bouton). Quand `κ → ∞`, elle s'effondre sur les poids d'origine.

**Usages généraux.** *Prior* bayésien pour des proportions ; allocation de Dirichlet latente (**LDA**) en modélisation de
thèmes ; le **bootstrap bayésien** de Rubin (1981) ; et l'analyse de sensibilité des poids en décision multicritère.

**🔒 Dans ce projet.** Avec `κ = 200`, un poids de 13 % oscille d'environ **±2,37 points de pourcentage** — la marge d'erreur
plausible d'un jugement d'expert. Nous reclassons **2 000 fois** et obtenons `P(victoire)` pour chaque projet. C'est ce rouage
qui a révélé la découverte la plus inconfortable du portefeuille : le consensus est robuste (99,9 %), mais **PROMETHEE II élit
le leader dans seulement 25,4 % des univers**. Sans la Dirichlet, cette divergence resterait invisible.

#### 🌪️ Tornado de sensibilité — quelle variable meut **vraiment** le résultat

**Ce que c'est.** Un graphique en barres horizontales, trié par effet absolu, qui répond : *parmi toutes les entrées
incertaines, lesquelles meuvent la sortie ?* Le nom vient de la forme — barres larges en haut, étroites en bas.

**Deux mesures qui semblent identiques et ne le sont pas.**
- Le **bêta** d'une régression multiple répond : *« si cette entrée augmente d'une unité, de combien augmente la sortie ? »*
  C'est un effet **unitaire**, indifférent à l'ampleur réelle de la variation de cette entrée.
- La **corrélation de Pearson** répond : *« quelle part de l'incertitude de la sortie est dictée par cette entrée ? »* Elle
  intègre déjà l'**échelle de l'incertitude** (approximativement `β·σᵢ/σ_y`).

Une variable peut avoir un bêta énorme et une corrélation nulle : elle *ferait* beaucoup bouger le résultat, mais en pratique
elle **ne varie presque pas**. Ne rapporter qu'une des deux, c'est une demi-vérité.

**Usages généraux.** Risque projet, modèles financiers, ingénierie de la fiabilité, calibration de simulateurs.

**🔒 Dans ce projet.** Ici, le tornado a fait quelque chose de rare : il a **dénoncé une limite du modèle lui-même**. Appliqué
à la VAN, les bêtas sont sortis **exactement égaux à `1/(1+i)ᵗ`** — les facteurs d'actualisation — car la VAN est *linéaire*
dans les flux. Le tornado de régression est alors **dégénéré** : il n'apprend rien au-delà du taux. C'est la **corrélation** qui
porte le signal. Et lorsque le coût des tokens est entré comme variable, son bêta a donné `−1/(1+i)ᵗ` (le coût entre avec un
signe négatif) et sa corrélation est restée proche de zéro. La lecture conjointe est précise et honnête : *« chaque unité de
plus en tokens retire 0,91 à la VAN — mais, dans ce projet, l'incertitude de la VAN ne vient pas des tokens. »* Aucune des deux
mesures, seule, ne dirait cela.

---

<!-- budget-global-section -->

## 💰 Budget Global de Tokens — chaque projet est un CENTRE DE COÛT

**Il existe UN seul budget : celui du plan que vous souscrivez.** Tout le reste en **découle**. Chaque projet est un **centre de coût** — il **n'a pas de budget propre**. Son allocation est une **part du Budget Global**, et cette part est **recalculée automatiquement** dès qu'un projet entre ou sort du portefeuille. **Rien n'est créé ; tout est réparti.**

> **Le bug structurel que ceci a corrigé.** Le budget de tokens de chaque projet valait `consommation × 1,10` — exactement 1,100 sur les **dix**. Circulaire. Auto-justifiant. **Aucun projet ne pouvait dépasser son budget, par construction.** *Un budget issu de sa propre dépense n'est pas un budget : c'est un reçu.* Aujourd'hui, avec le quota issu du pool réel, **6 projets sur 10 le dépassent**.

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

### 🍩 Concept — le pool est PARTAGÉ et FINI

**Concept.** Langfuse, CloudZero, Vantage et consorts donnent un **coût par projet**, comme si chacun avait son propre robinet. **Ce n'est pas le cas.** Il existe **un plan souscrit**, à quota mensuel fini, et **chaque token qu'un projet brûle est un token qu'un autre n'aura pas**. C'est la **tragédie des communs** appliquée au budget IA.

**Méthodologie.** Le Budget Global sort du contrat : `sièges × US$ × change × (1+IOF)` plus l'infra fixe, d'où le **TCO mensuel** et le **coût par million de tokens**. La consommation réelle vient des logs, projetée en **run-rate mensuel**. On en tire le **taux d'utilisation du quota**, la **marge** et la **date d'épuisement du pool**.

**Application — et le chiffre qui fait mal.** **31 % de la consommation est du GASPILLAGE** : 29 millions de tokens/mois brûlés dans des appels **qui ont échoué et n'ont rien rendu** (hallucination, rate-limit). C'est **4,7× toute votre marge contractuelle**. En clair : **on vous pousserait vers un plan plus gros à cause d'appels qui n'ont pas livré de réponse.** Couper la moitié du gaspillage libère plus de capacité que la marge entière — **sans dépenser un centime de plus**.

![Budget Global utilisé par projet (Burn Token Rate) — chaque part n'est pas « son coût » : c'est la capacité qu'il retire aux autres](docs/screenshots/budget-donut-burn-token.png)

### ⚖️ Répartition adaptative et SUBVENTION CROISÉE — qui paie pour qui

**Concept.** La répartition **par consommation** est le standard du marché, et elle est **auto-justifiante** : celui qui brûle le plus reçoit le plus gros quota, ce qui **légitime le gaspillage**. La répartition honnête se fait par **valeur livrée (EV)**.

**Méthodologie.** Le quota de chaque centre de coût vaut `plancher égalitaire (50 %) + valeur livrée (50 %)`, **redimensionné dès que N change** — un projet neuf a EV = 0 et, sans plancher, recevrait **zéro token** et ne pourrait jamais produire de valeur. La **subvention croisée** est l'écart entre le quota qu'il aurait pour ce qu'il **consomme** et celui pour ce qu'il **livre**. La somme des subventions vaut **exactement zéro** : c'est un transfert, pas une création de valeur.

**Application.** L'amplitude d'efficacité est de **68×** : le Project F livre **642** de valeur par million de tokens ; le Project J, **10**. Et la répartition révèle l'addition : **R$ 3 431/mois — 40 % du TCO — sont transférés des efficaces vers les inefficaces, chaque mois, dans le noir.** Le Project F, le moins cher du portefeuille, **paie la note du Project J**.

![Subvention croisée — qui consomme plus qu'il ne livre est subventionné ; qui livre plus qu'il ne consomme paie la note des autres](docs/screenshots/budget-subsidio-cruzado.png)

### 🔒 Contention CHIFFRÉE — la chaîne causale appliquée au PORTEFEUILLE

**Concept.** La chaîne causale relie, **à l'intérieur** d'un projet : `token qui a dérivé → risque → délai (P80) → argent`. Ceci relie **ENTRE** projets : `l'excédent de l'un → épuisement du pool → étranglement des AUTRES → leur P80 glisse → leur Cost of Delay envoie la facture`.

**Méthodologie.** Cela exige **simultanément** FinOps (le quota), l'EVM (la valeur livrée), le risque (l'exposition) et un planning simulé (le P80). Voilà pourquoi **aucun outil du marché ne le fait** — aucun n'a les quatre moteurs réunis. Langfuse voit le token. Jira voit la tâche. CloudZero voit la facture. **Aucun ne peut dire que le projet J coûte R$ X de retard au projet F.**

**Application — et l'honnêteté qui soutient le chiffre.** Dans le scénario d'étranglement, le **Project J cause R$ 3 730 de dommage aux autres et n'en subit que R$ 853** — solde +2 877 : c'est le **BOURREAU**. Le **Project C, 30× plus efficace, subit R$ 867 et ne cause rien** — c'est une **VICTIME**. La somme des soldes vaut **zéro** : tout bourreau a une victime.

> ⚠️ **Mais aujourd'hui le pool TIENT** (94 % du quota). **Il n'y a pas d'étranglement physique** — personne ne s'arrête, personne ne glisse. Le dommage est **allocatif**, pas **opérationnel**. Dire *« J retarde C »* alors que le pool a encore de la marge serait **un mensonge déguisé en rigueur**. C'est pourquoi le module est **scénarisé** et **étiqueté comme prévision** : il montre *à partir de quand* le pool bascule (+10 % de consommation → tout le portefeuille s'arrête 0,9 jour, R$ 1 497) et *ce que cela coûte quand il bascule*.

![Contention chiffrée — qui cause le dommage et qui le paie ; quand le pool s'assèche TOUS s'arrêtent, y compris les efficaces qui n'ont rien causé](docs/screenshots/budget-contencao.png)

### 🪓 Politique de coupe — si le portefeuille a besoin de place, QUI part ?

**Concept.** C'est la question à laquelle le comité de portefeuille **n'arrive jamais à répondre**. Dans un pool fini, admettre le projet N+1 **retire des tokens à tous les N déjà là** — admettre un projet **dilue tout le monde de 9,1 %**.

**Méthodologie.** La réponse honnête **n'est pas « celui qui dépense le plus »** — couper à la consommation brute punirait un projet **gros et productif**. La réponse est **« celui qui livre le moins PAR TOKEN »** : trier par **efficacité** (EV ÷ million de tokens) libère le maximum de pool au **coût minimal en valeur**. La diagonale `y = x` sépare la coupe qui **rapporte** de celle qui **détruit plus qu'elle ne libère**.

**Application.** Couper le **Project J** libère **20,5 % du pool** en sacrifiant **1,9 % de la valeur** — cela ouvre près de 2 places sans diluer personne. Couper le **Project F** libérerait 3,4 % et sacrifierait **21,2 % de la valeur** : cela **détruirait plus de valeur qu'il ne libérerait de capacité**. **Ce n'est pas « coupez les coûts » — c'est un arbitrage explicite, chiffré.**

![Politique de coupe — % du pool libéré face au % de valeur sacrifiée ; la diagonale sépare la coupe qui rapporte de celle qui détruit](docs/screenshots/budget-politica-corte.png)

---
<!-- pm-agent-section -->

## 🤖 Project Manager Agent — il lit 10 dimensions, apprend et **sait se taire**

Le tableau de bord **diagnostique**. La chaîne causale **quantifie**. L'agent **décide quoi faire maintenant** — et, cycle après cycle, découvre quel levier fait vraiment bouger l'aiguille *sur ce projet-là*. Il balaie **10 dimensions** (délai, ROI, risque, tokens, coût, dérive du modèle, fiabilité, qualité, flux et gaspillage), convertit chacune en **jours-équivalents de projet × le coût du retard de ce projet**, et répond à la seule question qui compte : **quoi faire maintenant, et combien cela vaut.**

> **La faiblesse qu'il fallait corriger.** L'agent recommandait **toujours** quelque chose : à chaque cycle il prenait le plus gros dommage et criait. **Un agent qui crie chaque semaine devient du bruit, et le bruit est ignoré** — il ne change donc rien, aussi juste soit-il. **Il lui manquait le droit de se taire.** C'est ce que livrent les trois méthodologies ci-dessous.

### 🚦 PRINCE2 — *management by exception* : le droit de se taire

**Concept.** Le *management by exception* de PRINCE2 dit que le manager **ne doit pas être dérangé** tant que le projet reste dans les tolérances convenues. Quand la **prévision** dépasse la tolérance — pas le réalisé, la **prévision** — un **Exception Report** se déclenche.

**Méthodologie.** Une tolérance par dimension (délai, coût, risque, qualité, bénéfice). L'escalade est déclenchée par la **prévision** : le P80 de Monte-Carlo et l'EAC de l'EVM. L'Exception Report comporte quatre parties obligatoires — **cause, impact, OPTIONS et recommandation**. C'est la ligne des *options* qui distingue un rapport d'exception d'une alarme : escalader sans proposer d'alternatives, c'est pousser le problème vers le haut, pas le gérer.

**Application ici.** Les tolérances **ne sont pas des chiffres que nous avons inventés** — elles sortent de ce que le projet **a déjà déclaré** : la date promise (`prazo_alvo`), le budget approuvé (`BAC`), la classification du **registre des risques lui-même** (`nivel='critico'`) et la **ligne de base qualité du projet lui-même** (régression contre soi, à la DORA). Seule la limite de ROI est une politique explicite — et elle est affichée, pour que le board puisse la contester. Les options offertes sont **absorber** (brûler la réserve de management), **récupérer** (comprimer le chemin critique) ou **renégocier** (déplacer la date ou couper le périmètre).

![Tolérances PRINCE2 — la marge de chaque dimension avant l'exception ; seule la Qualité a dépassé, et seule elle est escaladée](docs/screenshots/prince2-tolerancias.png)

### 🌡️ CCPM (Goldratt) — *buffer management* et le fever chart

**Concept.** Dans la *Chaîne Critique* de Goldratt, le buffer n'est pas du gras caché dans chaque tâche : c'est un **coussin explicite en fin de projet**. Le **fever chart** croise *la part de chaîne achevée* avec *la part de buffer consommée*, et indique dans laquelle des trois zones vous êtes.

**Méthodologie.** Les frontières sont **diagonales**, et c'est l'essence de la méthode : brûler du buffer **à la fin** est normal — le brûler **au début** est grave, car il reste un projet entier devant. **VERT = ne faites rien. JAUNE = planifiez la reprise. ROUGE = agissez maintenant.**

```
verde/amarelo:    y = 1/3 + (1/3)·x
amarelo/vermelho: y = 2/3 + (1/3)·x
```

**Application ici.** Le buffer, c'est `P80 − P50` du **planning Monte-Carlo** que nous exécutions déjà. La consommation, c'est le **retard de l'Earned Schedule** converti en jours. Et c'est le fever chart qui donne à l'agent le déclencheur objectif du silence : **zone verte et dans les tolérances = rien à escalader.** Aujourd'hui **3 des 10 projets** reçoivent exactement cela — et c'est en se taisant quand il n'y a rien à dire que l'agent gagne le droit d'être écouté quand il y a quelque chose.

![Fever chart du CCPM — les 10 projets dans les trois zones ; les frontières diagonales rendent la même consommation de buffer bénigne en fin de projet et grave au début](docs/screenshots/ccpm-fever-chart.png)

### 🏦 PMI — *reserve analysis* : contingence × réserve de management

**Concept.** Le PMI sépare deux réserves que presque tout le monde confond : la **contingence** couvre les *connus-inconnus* (la variabilité que vous avez **mesurée**), et la **réserve de management** couvre les *inconnus-inconnus* (le choc).

**Méthodologie.** `contingence = P80 − P50` et `réserve de management = P95 − P80`. Plus la confrontation que presque personne ne fait : la contingence que vous **avez** contre celle que votre **registre des risques justifie** (EMV — *Integrated Cost-Schedule Risk Analysis*, Hulett). Un buffer de durée est **aveugle aux événements de risque** ; c'est là que presque tout planning se découvre optimiste.

**Application ici — et une leçon d'honnêteté.** Convertir « impact 4 » (échelle 1–5) en jours exige un mapping qui est **le nôtre, pas le vôtre**. Nous avons donc **testé notre propre hypothèse** : en divisant par deux l'impact supposé, la conclusion « sous-réservé » passe de **10/10 à 1/10 projets**. C'est un **fil du rasoir**, et c'est pourquoi elle **n'est pas vendue comme un constat** — chaque projet porte le champ `robusto`, et l'agent **prévient quand sa propre lecture ne survit pas au test de résistance**. Ce qui **reste sans aucune hypothèse** est de l'arithmétique pure, et c'est le vrai constat : **le buffer vaut ~9 % de la chaîne, contre les 25–50 % avec lesquels travaille le CCPM.**

### 🏃 Sprints et le débat du weekly du vendredi

**Concept.** Le débat d'avancement du *weekly* du vendredi a besoin de **chiffres**, pas d'opinions. L'opinion ne déplace pas un projet.

**Méthodologie.** Trois métriques ouvrent la discussion. **(1) Say-do ratio** (`ΔEV ÷ ΔPV`) : une équipe à 0,7 **n'est pas lente** — elle *promet 30 % de plus qu'elle ne peut livrer*. On ne répare pas la capacité en tapant du poing ; on répare l'engagement par la prévisibilité. Et un say-do **très au-dessus de 1** n'est pas non plus de l'héroïsme : c'est une **ligne de base cassée**. **(2) Le CPI local du sprint**, séparé du cumulé **à dessein** — le cumulé est une moyenne, et la moyenne **cache** le mauvais sprint récent : un CPI cumulé de 1,05 peut abriter un dernier sprint à 0,60. **Le local accuse ; le cumulé console.** **(3) Prévision par vélocité** : s'il faut 6 sprints à l'équipe et qu'il n'en reste que 4, **la date est déjà morte** et personne ne l'a vu, car le burndown cumulé *semble* encore proche du plan.

**Application ici.** Le sprint **n'est pas inventé** : c'est la **période de l'EVM**, la cadence que le projet possède déjà, avec de vrais PV/EV/AC. Créer un calendrier de sprints parallèle au planning reviendrait à créer une **seconde vérité** sur le même projet — et deux vérités, c'est comme aucune.

> **⚠️ Conformité, dite franchement.** Ceci est un **rapport d'avancement par cadence, fondé sur l'EVM (ANSI/EIA-748) avec des métriques d'inspiration agile** — **ce n'est pas Scrum**. Le *Scrum Guide 2020* **ne contient ni** « velocity » **ni** « burndown chart » (ce sont des pratiques du marché, pas des artefacts officiels), et il a remplacé le *commitment* du Sprint Backlog par le **Sprint Goal**, traitant le backlog comme une **prévision**. Donc « say-do ratio (livré ÷ engagé) » est du vocabulaire **de l'industrie**, pas du Scrum canonique. **La métrique est honnête ; c'est l'étiquette qui mentirait.**

![Sprints — say-do ratio par sprint et le burndown réel face au plan ; la cadence est la période de l'EVM](docs/screenshots/sprints-weekly.png)

### 🎯 Le radar et le moteur de réapprentissage — pourquoi cette dimension et pas une autre

L'agent **ne regarde pas que la gagnante** — il montre tout le banc. Chaque dimension devient des **jours-équivalents**, les jours deviennent de l'**argent** au coût du retard de *ce* projet, et le poids est ce que l'agent **y a appris**. La priorité, c'est `dommage × poids`.

Le **moteur de réapprentissage** est un *bandit contextuel* — simple et auditable, et nous le disons franchement : **ce n'est pas du deep learning**. À chaque cycle l'agent recommande un levier et **mémorise sa métrique cible** ; au cycle suivant il **se demande des comptes**. Amélioration → le poids **monte**. Dégradation → il **descend**. Une variation inférieure à 2 % est du bruit, et **l'agent n'apprend pas du bruit**. Seul le levier qu'il a **recommandé** est jugé : il répond de ce qu'il a demandé et **ne s'attribue pas ce que le hasard a amélioré**. Le résultat est un profil qui **ne vaut pas pour le projet d'à côté** — et c'est précisément le but.

![Radar des 10 dimensions — le dommage de chacune sur la même règle (R$), et celle que l'agent a choisi d'attaquer](docs/screenshots/pm-agent-radar.png)

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

## 🧰 Installation pas à pas (en local, depuis zéro)

> Tout tourne **sur votre machine**. Aucune clé de l'auteur n'accompagne le paquet et aucune donnée ne quitte votre ordinateur.

### Étape 0 — Prérequis

| Prérequis | Version | Obligatoire ? | Pour quoi |
|---|---|---|---|
| **Python** | 3.10+ | ✅ | pipeline, KPI, Monte-Carlo, MCDM |
| **Node.js + npm** | 18+ | ✅ | tableau de bord (Evidence) |
| **git** | n'importe | ✅ | cloner le dépôt |
| **Rust + maturin** | stable | ⬜ optionnel | accélère la classification des logs |
| **tectonic** | n'importe | ⬜ optionnel | génère les pitch decks en PDF |

*Sous Windows, utilisez **WSL** ou **Git Bash** — la chaîne est un script `bash`.*

### Étape 1 — Cloner le dépôt
```bash
git clone https://github.com/bpenedo/Gestao-de-Projetos-PM-IA-BSC-DashBoard.git
cd Gestao-de-Projetos-PM-IA-BSC-DashBoard
```

### Étape 2 — Environnement Python isolé
```bash
cd foundations/pipeline
python3 -m venv .venv
source .venv/bin/activate        # Windows (PowerShell): .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Étape 3 — Dépendances du tableau de bord
```bash
cd ../evidence
npm install
```

### Étape 4 — Lancer la démo (anonyme, sans identifiants)
```bash
cd ../pipeline
./run_all.sh --mock
```

Dans l'ordre, la chaîne exécute : données de démo anonymes → KPI → VAN/TRI/TRIM/AÉ/IP → **ajustement de distributions
aux tokens** → **Monte-Carlo (10 000 itérations)** → AHP-TOPSIS 2n → **DEMATEL · ELECTRE · PROMETHEE · MAUT · MCDA-C**
→ **robustesse du classement (Dirichlet)** → graphiques → dossier administratif → carte 5D → pitch decks → build.

### Étape 5 — Ouvrir le tableau de bord
```bash
cd ../evidence
npm run dev          # http://localhost:3000
npm run preview      # (alternativa) serve o estático já compilado em build/
```

### Étape 6 — Passer à VOS données

**6.1 — Identifiants et paramètres** (tous optionnels ; sans `.env` la chaîne utilise les valeurs par défaut) :
```bash
cd ../pipeline
cp .env.example .env      # edite: LANGFUSE_PUBLIC_KEY, LANGFUSE_SECRET_KEY, SELIC_ANUAL, USD_BRL...
```

**6.2 — Votre flux de trésorerie** (c'est lui qui alimente VAN, TRI et le Monte-Carlo) :
```bash
cp fluxo_caixa_template.csv fluxo_caixa.csv
```
Format : `periodo 0` est l'investissement (flux négatif) et `taxa` le taux d'actualisation par période (`0.10` = 10 %).
```csv
project_name,periodo,fluxo,taxa
Project A,0,-12000,0.10
Project A,1,3000,0.10
Project A,2,4000,0.10
```

**6.3 — Lancer avec des données réelles :**
```bash
./run_all.sh          # sem --mock: sincroniza do Langfuse e usa fluxo_caixa.csv
```

### Étape 7 (optionnel) — Accélération et PDF
```bash
cd analise_rs && maturin develop --release && cd ..   # Rust (PyO3): classificação mais rápida
```
Pour les pitch decks, installez **tectonic** (ex. `cargo install tectonic` ou le gestionnaire de votre distribution).

### Étape 8 (optionnel) — Planifier la mise à jour
```bash
crontab -e
*/15 * * * * /CAMINHO/ABSOLUTO/foundations/pipeline/run_all.sh >> /tmp/bsc.log 2>&1
```

### 🩺 Problèmes courants

| Symptôme | Cause probable | Solution |
|---|---|---|
| `no such table: ...` | base non initialisée | `python3 db.py` |
| Le build du tableau de bord échoue | artefacts obsolètes | `rm -rf ../evidence/build && npm run build` |
| `findfont: Failed to find font weight` | avertissement matplotlib | inoffensif, ignorez-le |
| `Precisa de ≥2 projetos` | portefeuille à un seul projet | le MCDM compare des alternatives ; ajoutez-en une |
| `KS p-valeur < 0,05` à l'écran | la distribution décrit mal vos données | collectez plus d'échantillons ; le framework prévient au lieu de cacher |
| Les nombres changent d'une exécution à l'autre | la graine a été modifiée | gardez `MC_SEED` fixe pour la reproductibilité |

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
