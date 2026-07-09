# 🧭 Gestão de Projetos PM IA BSC DashBoard (Build and Analyze Your Own AI Portfolio Projects)

🌐 **Português** · [English](README.en.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [中文](README.zh.md) · [한국어](README.ko.md) · [हिन्दी](README.hi.md) · [עברית](README.he.md) · [Svenska](README.sv.md) · [Русский](README.ru.md) · [Suomi](README.fi.md)

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

### 💸 Você paga pela IA todo mês. Mas a IA está pagando **você**?

Toda vez que o cartão é debitado por **ChatGPT, Claude, Copilot, Gemini, Perplexity, DeepSeek, Kimi, Qwen…**,
uma pergunta de **milhões** fica sem resposta: **cadê o retorno?** Quantas horas-homem foram realmente
poupadas? Quanto do seu dinheiro **evaporou** em alucinação, retrabalho e espera? Qual projeto de IA **merece
escalar hoje** — e qual está **sangrando caixa** enquanto você aplaude a "inovação"?

Você não tem um custo de IA. Você tem um **vazamento silencioso** — e está de olhos vendados. Porque
*"o que não é medido não pode ser gerenciado nem melhorado"* — e o mercado mede por você, cobrando a conta.

**Este framework acende a luz.** Ele transforma o **gasto invisível** das suas assinaturas de IA em **retorno
mensurável, comparável e auditável** — sob o rigor do **Balanced Scorecard** (Kaplan & Norton), da **análise
de investimentos de nível Wall Street** e da **decisão multicritério**. É a diferença entre *torcer* e *saber*.
Entre pagar pela IA e **lucrar** com ela.

> *"O que não é medido não pode ser gerenciado nem melhorado."* — Kaplan & Norton

> *"Quem mede com precisão, constrói com excelência."* — Pierre Vernier

> *Quando você ora e estuda, não deixe [minhas palavras] te abandonarem. Com cada palavra e expressão que sai de seus lábios, tenha em mente trazer uma Unificação.* — Aryeh Kaplan

> *A metafísica pura, situando-se, por essência, acima e além de todas as formas e de todas as contingências, não é nem oriental nem ocidental: é universal.* — René Guénon

> *Conhecer a si mesmo é conhecer a própria linhagem e o próprio poder.* — Harvey Spencer Lewis

> *Scientia es Lux Lucis* ∞ Sapere Aude S∴A∴☬ ☿

> 🐺 **Pare de PAGAR por IA no escuro.** Enquanto o mercado assina IA na fé — e vira a estatística da
> **Gartner** (≥30% dos projetos de GenAI abandonados após o piloto) —, **você** vai medir cada token, eleger
> o projeto vencedor e converter gasto invisível em **retorno auditável**: VPL · TIR · MIRR · VUL · 70+ KPIs ·
> decisão multicritério · dashboard C-Level em **12 idiomas**. **A IA já é sua. Agora torne-a LUCRATIVA** —
> de graça, na sua máquina, em **5 minutos**: `./run_all.sh --mock && npm run dev` 🔥

> 📖 **Documentação principal:** **[`foundations/README.md`](foundations/README.md)** ·
> ⚙️ **Setup (traga suas chaves):** [`foundations/pipeline/SETUP.md`](foundations/pipeline/SETUP.md) ·
> 📊 **KPIs:** [`foundations/KPIs.md`](foundations/KPIs.md) / [`foundations/KPIs_README.md`](foundations/KPIs_README.md)

---

## 📑 Índice

- [🌅 Por que isto muda o jogo](#-por-que-isto-muda-o-jogo)
- [📈 A evidência (Gartner · IDC · PwC · McKinsey · MIT)](#-a-evidência-gartner--idc--pwc--mckinsey--mit)
- [💥 O custo da inação](#-o-custo-da-inação-faça-a-conta-que-ninguém-faz)
- [✨ Funcionalidades](#-funcionalidades)
- [📸 Telas (dashboard anônimo)](#-telas-dashboard-anônimo)
- [🚀 Início rápido](#-início-rápido-demo-sem-langfuse)
- [🏗️ Arquitetura](#️-arquitetura)
- [📊 Catálogo de KPIs](#-catálogo-de-kpis-70)
- [💰 Análise financeira de investimento](#-análise-financeira-de-investimento)
- [🏆 Decisão multicritério + Dossiê](#-decisão-multicritério-ahp-topsis-2n--dossiê-da-jóia-da-coroa)
- [🎲 Monte Carlo — o risco que a média esconde](#-monte-carlo--o-risco-que-a-média-esconde)
- [🧮 Cinco escolas de decisão. Um único veredito.](#-cinco-escolas-de-decisão-um-único-veredito)
- [🌐 12 idiomas](#-12-idiomas)
- [🙋 Objeções (as perguntas que você está se fazendo agora)](#-objeções-as-perguntas-que-você-está-se-fazendo-agora)
- [🧩 Skills incluídas](#-skills-incluídas-build--analyze-your-own)
- [📚 Recursos & referências](#-recursos--referências-awesome)
- [🗺️ Roadmap](#️-roadmap)
- [🤝 Contribuindo](#-contribuindo)
- [📄 Licença & autoria](#-licença--autoria)

---

## 🌅 Por que isto muda o jogo

**Existem dois tipos de pessoas na era da IA.** As primeiras assinam tudo, gastam alto e **rezam** para dar
certo — e engrossam a estatística cruel dos projetos que morrem no piloto. As segundas fazem o que Wall Street
faz com qualquer ativo sério: **medem, comparam, priorizam e realocam** — e transformam cada dólar de assinatura
em **retorno composto**. A única diferença entre elas **não é talento nem orçamento. É instrumentação.**

A IA generativa criou uma nova classe de despesa recorrente — **assinaturas e tokens** — e, com ela, o
desperdício mais caro da década: **o invisível.** O que você não vê, você não corrige. O que você não mede,
você não escala. E o que você não prova, o board não aprova.

**Este projeto te move da primeira tribo para a segunda.** Ele instrumenta cada projeto de IA como um **ativo
financeiro** e o mede sob o **Balanced Scorecard**, a **análise de investimentos (VPL, TIR, MIRR, VUL, ILL,
Payback)** e o **Lean Six Sigma** — e ainda **elege o melhor projeto do seu portfólio** por um modelo
multicritério (**AHP-TOPSIS 2n**). O boleto mensal opaco vira uma **tese de investimento auditável**: você
descobre, com números, onde escalar, onde cortar, onde a assinatura se paga em **semanas** — e onde ela sangra
sem cobertura.

Somos **pioneiros** de um território novo — a **fronteira entre a inteligência artificial e a contabilidade do
valor**. Como exploradores que cartografam terras ainda sem mapa, este framework é a **bússola** (🧭) que
converte a névoa das assinaturas em **rotas claras de retorno**: cada token, uma milha; cada projeto, uma
expedição rumo ao lucro. Onde havia custo cego, nasce **oportunidade mensurável**; onde havia planilha morta,
floresce uma **tese de investimento viva**.

> **A promessa:** transformar quem *paga por IA* em quem *lucra com IA* — e quem *usa IA* em quem
> **pioneiramente a domina, mede e multiplica**. Com números, não com fé.

---

## 📈 A evidência (Gartner · IDC · PwC · McKinsey · MIT)

Não peça para acreditar em mim. **Acredite nos institutos que estudam isso há décadas** — e cujo veredito é
unânime: **a IA cria um valor imenso, mas só entrega para quem mede e governa.** Quem "usa IA sem dominar"
vira estatística de abandono; quem instrumenta o retorno **fica com o prêmio**.

- 🧭 **Gartner** — previu que **≥ 30% dos projetos de IA generativa seriam abandonados após a prova de conceito
  até o fim de 2025**, tendo como causa central o **valor de negócio pouco claro** (além de dados ruins, custos
  crescentes e controles frágeis). *→ sem medição, o projeto morre no piloto.*
- 🔬 **MIT** (relatório *"The GenAI Divide / State of AI in Business 2025"*, iniciativa NANDA) — amplamente
  noticiado que a **grande maioria dos pilotos corporativos de GenAI não gera impacto mensurável no P&L**; a
  minoria que entrega valor combina IA com **processo e medição**. *→ a diferença é medir, não adotar.*
- 💵 **IDC** (estudo *"The Business Opportunity of AI"*, patrocinado pela Microsoft) — organizações que **medem
  e otimizam** reportaram retorno na ordem de **vários dólares para cada US$ 1** investido em IA, com forte
  dispersão entre líderes e retardatários. *→ o ROI existe — e favorece quem instrumenta.*
- 🌍 **PwC** (*"Sizing the Prize"*) — estima que a IA pode adicionar até **~US$ 15,7 trilhões** à economia
  global até 2030; mas o prêmio vai para quem **captura** o valor, não para quem apenas o consome. *→ o bolo é
  gigante; a fatia é de quem mensura.*
- 🏆 **McKinsey** (*"The State of AI"*) e **BCG × MIT Sloan** — um grupo minoritário de **"AI high performers"**
  captura retorno desproporcional; a virada acontece quando a IA é acoplada a **métricas, governança e
  reinvestimento** onde há retorno comprovado. *→ vencedores medem, priorizam e realocam.*

> **É exatamente esse fosso que este framework atravessa:** ele te tira do lado que *abandona no piloto* e te
> coloca no lado que tem **resultado propriamente dito e provado** — com BSC, análise de investimento e decisão
> multicritério.

> ⚠️ **Nota de honestidade (leia):** os números acima refletem manchetes reais desses institutos, mas
> **relatórios e percentuais são atualizados** — confirme os valores exatos e o ano nas **fontes primárias**
> (Gartner Newsroom; IDC/Microsoft *Business Opportunity of AI*; PwC *Sizing the Prize*; McKinsey *State of AI*;
> MIT *State of AI in Business*) antes de citar em material oficial. Aqui eles servem como **fundamentação
> direcional**, não como garantia numérica.

---

## 💥 O custo da inação (faça a conta que ninguém faz)

Uma assinatura **PRO de IA** custa entre **US$ 20 e US$ 200 por mês, por assento**. Multiplique pelo número de
pessoas do seu time. Multiplique por 12 meses. Agora aplique o que os institutos **já provaram**: a **Gartner**
projeta **≥ 30% de abandono** e o **MIT** mostra que a **maioria dos pilotos não retorna**. Uma fatia enorme
desse total não é investimento — é **sangria pura**.

> **Exemplo direto (troque pelos seus números):** 10 assentos × US$ 30/mês × 12 = **US$ 3.600/ano**. Se ~30%
> viram desperdício invisível, são **~US$ 1.080/ano evaporando** — de UM time pequeno, em UM ano. No seu número
> real, o susto é maior.

E aqui está a parte que dói: **esse custo é composto e não espera.** Cada mês sem medir é um mês de vazamento
que **não volta** — enquanto o concorrente que instrumentou já está **realocando capital para o que rende**.
Vantagem de pioneiro se constrói cedo: **quem mede primeiro, escala primeiro.**

O momento de menor custo para começar foi ontem. O segundo melhor é **agora** — e custa **US$ 0** e **5
minutos**. A pergunta não é *"posso pagar para medir?"*. É ***"quanto tempo mais posso pagar para NÃO medir?"***

---

## ✨ Funcionalidades

- **📊 KPIs (4 perspectivas BSC) + economia de APIs:** maturidade, capital humano, financeiro e eficiência de
  tokens — `IEET`, `IOLI`, `ITR`, `IITA`, `PEUC`, `ICCA`, `IDLS`, `IBMT` — mais **EVM** (CPI/SPI/EAC).
- **🪙 Conceitos de fronteira:** **VRT/kTR** (unidade de recuperação de custo tokenizável — *"o m² de Gitman"*)
  e **PSR** (Project Score 0–5 ⭐) para ranquear a saúde de cada projeto.
- **🔬 Diagnóstico operacional:** **VRT em 5 blocos**, **HCI** (horário crítico de interrupção), **Wastes Lean
  Six Sigma** (tokens ponderados) e **RCA de alucinação por taxonomia de prompt** (gargalo por projeto + interseção).
- **💰 Financeiro completo:** **VPL/NPV, TIR/IRR, TIRM (TIR Modificada/MIRR), VUL (Valor Uniforme Líquido),
  ILL (PI), Payback** simples e descontado, **dolarização** e comparação com **SELIC** e os **juros dos EUA**.
- **🏆 Decisão multicritério (5 métodos):** **DEMATEL** (estrutura causal + pesos por influência) alimentando
  **ELECTRE I · PROMETHEE II · MAUT · MCDA-C · AHP-TOPSIS 2n**, com **consenso de Borda** e **dossiê administrativo**
  (SWOT, PESTELC, 5W4H, Pareto, GUT, Radar).
- **🎲 Risco (Monte Carlo, estilo SimulAr v2.5):** **10.000 iterações** por projeto, **20 distribuições**, matriz de
  correlação (Iman-Conover), **P(VPL<0)**, **VaR/CVaR 5%**, percentis 1–99% e **tornado** (regressão + correlação).
- **🗺️ Visual C-Level:** **mapa 5D interativo**, donuts com profundidade, quadrante de sustentabilidade,
  tendências e **pitch decks** em LaTeX dos projetos elegíveis.
- **⚙️ Pipeline real:** **Langfuse → SQLite → Evidence**, com sync **assíncrono concorrente** e classificação
  acelerada em **Rust (PyO3)**.
- **💳 FinOps de IA:** catálogo de **planos de assinatura** (OpenAI, Anthropic, Google, Perplexity, xAI,
  Mistral, DeepSeek, Kimi, Qwen…) com **câmbio + IOF** e base de **rateio** (burn rate).
- **🌐 12 idiomas** no dashboard **e nas imagens dos gráficos** (incl. Devanagari, Hebraico e CJK).

---

## 📸 Telas (dashboard anônimo)

> Demonstração 100% anônima (projetos exibidos como *Project A…J*). Os dados/nomes reais nunca acompanham o pacote.

**🌐 Mapa 5D do portfólio** — 5 dimensões por projeto: **X**=tokens · **Y**=PEUC (qualidade) · **Z**=PSR (saúde)
· **tamanho**=Burn Rate · **cor**=ICCA (sustentabilidade). *Onde escalar? Direita/fundo, alto e verde. Onde
cortar? Grande e vermelho.*

![Mapa 5D do portfólio de projetos de IA](docs/screenshots/5d-portfolio-map.png)

**🏆 Dossiê da "Jóia da Coroa"** (projeto eleito pelo AHP-TOPSIS) — gerado por pipeline Python concorrente:

| SWOT | Radar competitivo |
|---|---|
| ![SWOT](docs/screenshots/swot.png) | ![Radar competitivo](docs/screenshots/radar.png) |

| PESTELC (macroambiente) | Matriz GUT (priorização) |
|---|---|
| ![PESTELC](docs/screenshots/pestel.png) | ![GUT](docs/screenshots/gut.png) |

| 5W4H (plano de ação) | Pareto de falhas (80/20) |
|---|---|
| ![5W4H](docs/screenshots/5w4h.png) | ![Pareto](docs/screenshots/pareto.png) |

---

## 🚀 Início rápido (demo, sem Langfuse)

**Zero risco. Zero custo. 5 minutos.** Rode na sua máquina e veja o dashboard completo com dados anônimos:

```bash
cd foundations/pipeline
pip install -r requirements.txt
cd ../evidence && npm install && cd ../pipeline
./run_all.sh --mock          # dados anônimos (Project A..J) -> KPIs -> VPL/TIRM/VUL -> 5D -> pitch decks -> dashboard
cd ../evidence && npm run dev # http://localhost:3000
```

Para **dados reais**, preencha `foundations/pipeline/.env` com **as suas chaves** do Langfuse
(ver [`SETUP.md`](foundations/pipeline/SETUP.md)) e rode `./run_all.sh`. Cada usuário usa a **própria conta** —
nenhuma chave do autor acompanha o pacote.

---

## 🏗️ Arquitetura

```
   As suas apps de IA            Observabilidade        Analytics-as-Code           Você
 (ChatGPT, Claude, API…)   ┌──────────────┐   ┌──────────────────┐   ┌──────────────────────┐
        │ traces           │   Langfuse   │   │  SQLite (schema  │   │  Evidence (BI as     │
        └─────────────────▶│  (SDK v4)    │──▶│  + queries KPI)  │──▶│  Code) · 12 idiomas  │
                           └──────────────┘   └──────────────────┘   └──────────┬───────────┘
   sync assíncrono concorrente        classificação em Rust (PyO3)              │
                                                                    ┌───────────┴───────────┐
                                                                    │ AHP-TOPSIS · Dossiê   │
                                                                    │ 5D · Pitch decks (TeX)│
                                                                    └───────────────────────┘
```

**Stack:** Python 3.13 · SQLite/DuckDB · Evidence.dev (SvelteKit) · Rust + PyO3 + maturin · matplotlib ·
tectonic (LaTeX) · fontes Noto/WenQuanYi para i18n de imagem.

---

## 📊 Catálogo de KPIs (70+)

Amostra (catálogo completo em [`foundations/KPIs_Lean6s_BSC.md`](foundations/KPIs_Lean6s_BSC.md)):

| Sigla | Nome | O que responde |
|---|---|---|
| **PSR** | Project Score Rating (0–5) | Saúde geral do projeto de IA |
| **PEUC** | % de Entrega Útil por Consumo | Quanto do gasto virou entrega útil |
| **IITA** | Índice de Incidência de Tokens Alucinados | % de alucinação/retrabalho |
| **IDLS** | Índice de Desperdício Lean | Muda (tokens ponderados por severidade) |
| **VRT/kTR** | Valor de Recuperação Tokenizável | "m² de Gitman" — custo por 1k tokens |
| **ICCA** | Índice de Cobertura de Custo por Assinatura | Cobre o custo? (>3× saudável) |
| **CPP** | Custo por Ponto de Progresso | Indicador-mestre (quanto menor, melhor) |

---

## 💰 Análise financeira de investimento

Cada projeto vira uma **tese de investimento**: a partir do seu fluxo de caixa (CSV), o framework calcula
**VPL/NPV**, **TIR/IRR**, **TIRM (MIRR — reinveste ao custo do projeto)**, **VUL (anuidade equivalente do
VPL)**, **ILL (índice de lucratividade)** e **Payback** simples/descontado — **dolarizando** o fluxo e
comparando com a **SELIC** e os **juros dos EUA**. Gera **pitch deck** em LaTeX para todo projeto com **VPL > 0
e ILL > 1** em BRL **e** USD. O objetivo é brutalmente prático: **descobrir se a sua assinatura de IA se paga —
e em quanto tempo.**

---

## 🏆 Decisão multicritério (AHP-TOPSIS 2n) + Dossiê da Jóia da Coroa

Quando há vários projetos, qual escalar primeiro? O modelo **AHP-TOPSIS 2n** pondera os indicadores como
critérios (pesos por **AHP** com razão de consistência **CR ≤ 0,10**) e ranqueia por **TOPSIS** em **duas
normalizações** (vetorial + min-max), reportando a **robustez** (concordância entre normalizações). O vencedor
— a **"Jóia da Coroa"** — recebe um **dossiê administrativo** completo (SWOT · PESTELC · 5W4H · Pareto · GUT ·
Radar) gerado do zero por código, com um **Bottom-Line executivo** e **insights C-Level** honestos. **Você não
apresenta uma planilha. Você apresenta um veredito.**

---

## 🎲 Monte Carlo — o risco que a média esconde

Um VPL positivo **na média** não protege ninguém. A média é a mentira mais confortável das finanças: descreve
um cenário que talvez nunca aconteça. Quem decide o seu destino é a **cauda** — o dia ruim.

Este framework simula **10.000 futuros** para cada projeto (motor compatível com o **SimulAr v2.5**, de Luciano
Machain, UNR/Argentina): cada fluxo de caixa vira uma **variável aleatória** e o portfólio é reprocessado iteração
a iteração. No fim você não tem um número — você tem **a distribuição inteira do seu dinheiro**:

- **`P(VPL < 0)`** — a probabilidade real de prejuízo. O número que ninguém te mostra.
- **VaR 5%** — o pior cenário plausível: *"em 19 de cada 20 futuros, eu ganho pelo menos isto."*
- **CVaR 5%** — quando o desastre acontece, quanto ele custa em média.
- **Tornado de sensibilidade** — regressão múltipla e correlação de Pearson: qual variável realmente move o seu VPL.
- **20 distribuições** de entrada, **matriz de correlação** validada (Iman-Conover, que preserva as marginais exatas)
  e **percentis de 1% a 99%**, com histograma de 100 classes idêntico ao do manual do SimulAr.

Semente fixa: rodar de novo dá **exatamente** o mesmo resultado. Auditável — não "mágico".

> **A virada:** você para de escolher o projeto de maior VPL e passa a escolher **o que sobrevive ao cenário ruim**.
> Isso é gestão de risco — é o que separa o investidor do apostador.

![Histograma de Monte Carlo do VPL — 10.000 iterações, 100 classes](docs/screenshots/mc-histograma.png)

| Distribuição acumulada do VPL | Tornado de sensibilidade |
|---|---|
| ![Distribuição acumulada do VPL](docs/screenshots/mc-acumulado.png) | ![Tornado de sensibilidade](docs/screenshots/mc-tornado.png) |

---

## 🧮 Cinco escolas de decisão. Um único veredito.

Um método pode errar. Cinco métodos concordando, não.

Seguindo a arquitetura de **John (2025)** — *Integration of DEMATEL with Other MCDM Methods* —, o **DEMATEL** mapeia
a estrutura causal entre os critérios e separa **causas** (alavancas onde agir) de **efeitos** (termômetros do que já
foi feito). Desses laços de influência nascem os **pesos**: não arbitrados, mas **derivados da estrutura do problema**.
Eles alimentam quatro escolas rivais:

| Método | Escola | O que pergunta |
|---|---|---|
| **ELECTRE I** | Sobreclassificação | "Quem domina quem — e quem sobrevive sem ser dominado?" |
| **PROMETHEE II** | Sobreclassificação | "Qual o fluxo líquido de preferência de cada projeto?" |
| **MAUT** | Utilidade | "Qual maximiza a utilidade de um decisor avesso a risco?" |
| **MCDA-C** | Construtivista | "Quem está acima do nível *Bom* — e quem está abaixo do *Neutro*?" |
| **AHP-TOPSIS 2n** | Distância ao ideal | "Quem está mais perto da solução ideal nas duas normalizações?" |

O vencedor sai do **consenso de Borda** entre os cinco, já **ajustado ao risco** do Monte Carlo. E quando os métodos
**discordam**, o dashboard mostra a discordância — porque isso é informação: a escolha é sensível à escola de decisão
e merece o olho do decisor.

| DEMATEL — causas × efeitos | Posição por método |
|---|---|
| ![DEMATEL — causas × efeitos](docs/screenshots/dematel.png) | ![Posição por método](docs/screenshots/mcdm-metodos.png) |

### 💼 O que isso muda no seu dia — do autônomo à corporação

Não importa se você paga **US$ 20 num plano PRO** ou **US$ 200 mil em contratos enterprise**: a matemática do
desperdício é a mesma — só muda o número de zeros.

| | **SMB / autônomo** | **Grande empresa** |
|---|---|---|
| **A dor real** | 3 assinaturas, zero visibilidade, caixa curto | 40 pilotos de IA, nenhum com P&L atribuído |
| **O Monte Carlo entrega** | *"este projeto tem 12% de chance de dar prejuízo, e o mês ruim custa R$ 3,4 mil"* | VaR/CVaR por unidade de negócio: risco agregado e auditável, não anedota |
| **O MCDM entrega** | qual dos 3 projetos escalar **primeiro**, com o dinheiro que existe | qual dos 40 pilotos vira produto — defensável em comitê, com o método explícito |
| **O ganho no dia seguinte** | cancela a assinatura que não se paga, ainda nesta semana | realoca orçamento por **evidência**, não por política interna |

**Na prática:** o **tornado** aponta a variável que move o resultado — ou seja, **onde investir a sua próxima hora de
trabalho**. O **DEMATEL** revela que reduzir alucinação (IITA) é **causa**, não sintoma: você mexe ali e VPL, TIR e
risco melhoram *juntos*. É a gestão de IA deixando de ser opinião e virando **engenharia**.


---

## 🌐 12 idiomas

Dashboard, páginas por projeto **e o texto interno das imagens** dos gráficos estão localizados em **12
idiomas**: Português · English · Español · Français · Deutsch · 中文 · 한국어 · हिन्दी · עברית · Svenska · Русский · Suomi.
A tradução é dirigida por uma **Translation Memory** (estilo SDL Trados) que padroniza e agiliza novas línguas.

---

## 🙋 Objeções (as perguntas que você está se fazendo agora)

- **"Não tenho tempo."** → Cinco minutos com `./run_all.sh --mock` e o dashboard está rodando na sua tela.
  Medir **devolve** as horas que você já perde em retrabalho e alucinação.
- **"É complexo demais."** → Uma linha. O framework faz o ETL, os cálculos, o ranking e as imagens; **você só
  lê o veredito.**
- **"Minha operação de IA é pequena."** → Por isso mesmo cada dólar pesa mais. Pequeno hoje, portfólio amanhã —
  **meça antes de escalar o desperdício.**
- **"Não uso Langfuse."** → A demo roda **100% sem Langfuse**. Quando quiser dados reais, você pluga a **sua**
  conta (nunca a minha).
- **"É só mais um dashboard bonito."** → Não. É **Balanced Scorecard + análise de investimento (VPL/TIR/MIRR/VUL)
  + decisão multicritério (AHP-TOPSIS)** — instrumentos de board, não enfeite.
- **"E a privacidade dos meus dados?"** → A demo é **100% anônima** (Project A…J); dados/nomes reais e chaves
  ficam **fora do pacote**. Você roda **local**, com a **sua** conta.
- **"Quanto custa?"** → **Nada.** Open source, na sua máquina. O único preço é continuar **sem medir** — e esse,
  você já está pagando.

---

## 🧩 Skills incluídas (*build & analyze your own*)

Este repositório embute **Skills** reutilizáveis (Claude Code):

- **`measuring-ai-projects`** — definir/medir/reportar KPIs de projetos de IA (o núcleo deste framework).
- **`github-benchmark-analyzer`** — analisar e fazer benchmark de **qualquer** repositório/perfil do GitHub
  (estrelas, forks, seguidores, hashtags, estilo de README, palavras-chave, linguagens) e extrair o que os
  líderes têm em comum. **Construa e analise o seu próprio portfólio** — inclusive contra o mercado.

---

## 📚 Recursos & referências (Awesome)

Ombros de gigantes sobre os quais este framework se apoia:

- **Estratégia & medição:** Kaplan & Norton — *The Balanced Scorecard* · Peter Drucker (gestão por objetivos).
- **Lean Six Sigma:** taxonomia dos 8 desperdícios (Muda), PDCA/Kaizen, Ishikawa/RCA.
- **Finanças corporativas:** Lawrence Gitman — *Princípios de Administração Financeira* (VPL, TIR, MIRR, PI).
- **Decisão multicritério:** Thomas Saaty (**AHP**) · Hwang & Yoon (**TOPSIS**).
- **Stack técnico:** [Langfuse](https://langfuse.com) (LLM observability) · [Evidence](https://evidence.dev)
  (BI as Code) · [Rust/PyO3](https://pyo3.rs) · [Tectonic](https://tectonic-typesetting.github.io) (LaTeX).

---

## 🗺️ Roadmap

- [x] Pipeline Langfuse → SQLite → Evidence + Rust
- [x] 70+ KPIs (BSC + economia de APIs + Lean) · EVM
- [x] Financeiro (VPL, TIR, TIRM, VUL, ILL, Payback, dolarização)
- [x] AHP-TOPSIS 2n + Dossiê administrativo (6 ferramentas)
- [x] Dashboard e imagens em **12 idiomas**
- [ ] Conectores extras de observabilidade (OpenTelemetry, Helicone)
- [ ] Modo SaaS multi-tenant + agendamento nativo
- [ ] Publicação do dashboard estático (GitHub Pages)

---

## 🤝 Contribuindo

Contribuições são **muito bem-vindas**! Abra uma *issue* descrevendo a proposta (novo KPI, conector, idioma,
correção) e envie um *pull request*. Padrões: código legível e consistente com o entorno, sem dados pessoais
no pacote (a demo é anônima). Novos idiomas: acrescente os alvos na Translation Memory e rode o gerador.

## 📄 Licença & autoria

© **Bruno Penedo** — 2026. Uso, estudo e contribuição encorajados; para uso comercial/redistribuição,
consulte o autor. *(Uma licença OSS formal pode ser adicionada — abra uma issue com a sua preferência.)*

## 🏷️ Topics
`awesome-list` · `education` · `resources` · `computer-science` · `python` · `business-intelligence` ·
`llmops` · `finops` · `aiops` · `programming` · `development` · `lists` · `free` · `unicorns` · `dashboard` ·
`balanced-scorecard` · `langfuse` · `llm-observability` · `kpi` · `project-management`

---

⭐ **Se este framework acende uma luz sobre o seu gasto com IA, deixe uma estrela — e comece a lucrar com o que já paga.**

---

**Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard** · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
