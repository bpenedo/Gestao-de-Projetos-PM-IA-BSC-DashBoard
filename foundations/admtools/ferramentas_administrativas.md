# 🛠️ Ferramentas Administrativas — Dossiê da Jóia da Coroa

> **Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard** · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com

Este documento descreve o **conjunto de ferramentas administrativas** aplicadas **exclusivamente ao
Projeto Eleito** ("Jóia da Coroa") — o vencedor do modelo multicritério **AHP-TOPSIS 2n**. O objetivo é
**enriquecer, enaltecer e evidenciar o diferencial competitivo** do projeto escolhido, transformando os
KPIs do framework em **estratégia, priorização e plano de ação**.

Todas as figuras são geradas **do zero, por código**, pela **pipeline administrativa concorrente**
`pipeline/gerar_admtools.py` (6 ferramentas renderizadas em paralelo via `ProcessPoolExecutor`), **sem
depender de nenhum template/imagem externa**. A saída fica em `evidence/static/admtools/*.png` (regenerável,
por isso *git-ignored* — contém o nome real do projeto eleito) e é exibida no **Dashboard Central**.

---

## Por que estas ferramentas (visão de portfólio)

A escolha segue uma **cadeia lógica de decisão** — do diagnóstico externo/interno até o "onde agir primeiro":

| Camada | Pergunta que responde | Ferramenta |
|---|---|---|
| **Ambiente interno/externo** | Onde estamos fortes/vulneráveis? | **SWOT** |
| **Macroambiente** | Que forças externas nos afetam? | **PESTELC** |
| **Execução** | O que faremos, como, quanto e quando? | **5W4H** |
| **Foco (80/20)** | Onde estão os poucos problemas vitais? | **Pareto** |
| **Priorização** | Qual ação atacar primeiro? | **GUT (heatmap)** |
| **Diferencial** | Por que este projeto é superior? | **Radar competitivo** |

Juntas, elas cobrem **diagnóstico → estratégia → priorização → prova de superioridade**, que é
exatamente o que um board precisa para **aprovar o piloto de escala** com segurança.

---

## 1. SWOT (Strengths, Weaknesses, Opportunities, Threats)
**O que faz:** mapeia **Forças** e **Fraquezas** (ambiente interno) frente a **Oportunidades** e **Ameaças**
(ambiente externo). Aqui é **orientada a dados**: as forças saem dos KPIs reais (menor IITA e menor IDLS do
portfólio), e as fraquezas/ameaças apontam riscos concretos (PSR abaixo da meta, fluxo real ainda não medido).
**Por que escolhida:** é o ponto de partida canônico de qualquer análise estratégica — sintetiza em um quadro
único a posição competitiva do eleito e conecta diretamente aos indicadores do framework.

## 2. PESTELC (Político, Econômico, Social, Tecnológico, Ecológico, Legal, Cultural)
**O que faz:** analisa **7 fatores macroambientais** que o projeto **não controla**, mas aos quais deve se
adaptar. Inclui as extensões **Ecológico** (consumo computacional/energético dos tokens) e **Cultural**
(cultura *data-driven*, Kaplan).
**Por que escolhida:** o SWOT olha "para dentro"; o PESTELC garante que a decisão considere **tendências
externas** (regulação de IA, LGPD, evolução de modelos, sustentabilidade) — essencial para um ativo de IA.

## 3. 5W4H (5W + 4H)
**O que faz:** converte a estratégia em **plano de ação executável** respondendo **5 W** (What, Why, Where,
When, Who) e **4 H** (How, How much, How long, How many). É a evolução do 5W2H com **+2H** (How long, How many),
conforme o template de referência.
**Por que escolhida:** transforma "o que decidimos" em "quem faz o quê, como, quanto custa, em quanto tempo e
com que meta" — fecha o ciclo entre diagnóstico e execução.

## 4. Gráfico de Pareto (Princípio 80/20)
**O que faz:** ordena as **categorias de prompt por número de falhas** e traça a **curva de acumulado**,
revelando os **poucos vitais** que concentram ~80% dos problemas. Usa **dados reais** do Langfuse do eleito.
**Por que escolhida:** é a ferramenta Lean Six Sigma para **focar esforço** — em vez de tentar corrigir tudo,
mostra onde a redução de alucinação/retrabalho gera **maior impacto no CPP**.

## 5. Matriz GUT (Gravidade × Urgência × Tendência) — *Heatmap*
**O que faz:** prioriza as ações do plano atribuindo notas 1–5 a **Gravidade**, **Urgência** e **Tendência**;
o produto **G×U×T** (0–125) define a ordem de ataque. Renderizada como **heatmap** para leitura imediata.
**Por que escolhida:** o Pareto diz *onde* estão os problemas; a GUT diz *em que ordem resolvê-los*. O heatmap
dá ao C-Level uma priorização visual e defensável (a ação "inserir fluxos de caixa reais" emerge como GUT máx).

## 6. Radar Competitivo (Spider / impressão digital)
**O que faz:** projeta o eleito contra a **média do portfólio** em 6 eixos normalizados (PSR, PEUC,
anti-alucinação, Lean, estabilidade, custo-eficiência). A **área** representa a superioridade agregada.
**Por que escolhida:** é a **prova visual do diferencial competitivo** — mostra, de relance, que a área do
eleito **domina** a média em quase todos os eixos, justificando por que ele é a Jóia da Coroa.

---

## Ferramentas extras disponíveis no framework
Estas ferramentas complementam o dossiê e já constam do arcabouço (aplicáveis a qualquer projeto):
**BCG** (crescimento × participação), **RACI** (responsabilidades), **PDCA/Kaizen** (melhoria contínua),
**Ishikawa/RCA** (causa-raiz da alucinação), **EVM** (CPI/SPI). Ver `foundations/KPIs_Lean6s_BSC.md` e
`foundations/bscdashboardgerencial.md`.

## ▶️ Como (re)gerar
```bash
cd foundations/pipeline
python3 ahp_topsis.py       # define o projeto eleito (Jóia da Coroa)
python3 gerar_admtools.py   # gera as 6 ferramentas em paralelo → evidence/static/admtools/
```
Também roda automaticamente na esteira `run_all.sh`, logo após a decisão AHP-TOPSIS.

> **Nota de privacidade:** as imagens geradas contêm o **nome real** do projeto eleito e por isso são
> *git-ignored*. No pacote público/demo (seed anônimo `Project A..J`), o eleito é um projeto fictício.
