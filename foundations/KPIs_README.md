# 📚 KPIs_README — Guia Prático dos Indicadores Implementados

> **Framework "Painel BSC Dashboard — Gestão de Projetos (PM) IA"**
> **Autor:** Bruno Teixeira Penedo · **Criação:** 27/06/2026 às 18:00.

Este documento **descreve cada KPI implementado** no pipeline ([`pipeline/queries/kpis_bsc_ia.sql`](pipeline/queries/kpis_bsc_ia.sql))
com **exemplos práticos** no contexto deste projeto. Os números dos exemplos vêm da execução real
com dados mock (`python3 compute_kpis.py`) sobre 3 projetos do ecossistema:

| Projeto | Perfil | PSR | Veredito |
|---|---|---|---|
| Ferramentas de Backtest | prompts grandes, alto custo | **3,82 ⭐⭐⭐⭐** | Bom |
| Extensões Chrome PWAs | muita alucinação, alto MRR | **3,31 ⭐⭐⭐** | Regular |
| Automações RPA n8n | estoura cota (429) | **1,93 ⭐⭐** | Crítico |

> Definição formal e fórmulas-mestre: [`KPIs.md`](KPIs.md). Aqui o foco é **o que cada número significa na prática.**

---

## 🪙 VRT/kT — Valor de Recuperação por 1.000 Tokens
**O que é:** a unidade monetária de recuperação de custo do framework — o *"m² de Gitman"* da era da IA.
Quanto cada bloco de 1.000 tokens precisa "devolver" para cobrir API + infraestrutura rateada + desperdício.
**Fórmula:** `(preço_API/1k + CRI) × FIA`.

**Exemplo prático:**
- *Ferramentas de Backtest:* **R$ 0,30684 / 1k tokens**.
- *Extensões Chrome:* **R$ 2,40912 / 1k tokens** — ~8× mais caro!
- **Por quê?** O backtest dilui o rateio fixo de infra em 6,4 milhões de tokens; as extensões dividem
  o mesmo custo fixo por apenas 880 mil tokens. Menos volume = cada token carrega mais "aluguel".
**Ação:** se o VRT/kT de um projeto dispara, ou falta volume para diluir a infra, ou o desperdício (FIA) subiu.

---

## ⭐ PSR — Project Score Rating (0–5)
**O que é:** nota individual do projeto, fundindo avanço de progresso, interrupções e entregas úteis.
**Fórmula:** `0,40·S_progresso + 0,25·S_interrupção + 0,35·S_entrega`.

**Exemplo prático — Automações RPA (PSR 1,93 ⭐⭐ Crítico):**
- Progresso abaixo do plano (8% real vs. 12% planejado) → S_progresso baixo.
- 18 interrupções (teto 20) → S_interrupção quase zerado.
- PEUC 27% → S_entrega baixo.
- **Resultado:** nota 1,93 ⭐⭐ → *intervir*. Contrasta com Backtest (3,82 ⭐⭐⭐⭐, no prazo e estável).
**Ação:** o PSR é o "semáforo" do portfólio — projetos < 2,5 vão para a pauta de intervenção da sexta.

---

## 📊 PEUC — % de Entregáveis Úteis por Sessão
**O que é:** das sessões (jornadas do usuário até um objetivo), quantas terminaram **sem nenhuma falha**.
**Exemplo:** Backtest **54%** vs. Automações **27%**. Em Automações, ~3 de 4 sessões esbarram em erro
antes de entregar — destrói a percepção de valor da assinatura (risco de churn).
**Meta:** > 90%. **Ação:** PEUC baixo → revisar prompts de sistema / escolha de modelo.

---

## 🧠 IITA — Inflação de Tokens por Alucinação
**O que é:** % dos tokens queimados em loops de correção/erro — dinheiro pago para a IA consertar a si mesma.
**Exemplo:** Extensões **28,19%** → de cada R$ 100 de fatura de API, ~R$ 28 são desperdiçados em retrabalho.
**Meta:** < 10%. **Ação:** IITA alto paga a migração para um modelo melhor (elimina o loop).

---

## 🧹 IDLS — Índice de Desperdício Lean por Sessão
**O que é:** % de tokens consumidos por atividades sem valor (defeito + cota), já com os **pesos punitivos**
(1,5× cota, 2,0× alucinação).
**Exemplo:** Extensões **55%** e Automações **51%** — mais da metade do "tráfego ponderado" é Muda (desperdício Lean).
**Meta:** < 15%. **Ação:** dispara o plano de Ações Corretivas Lean (PDCA) na reunião semanal.

---

## ⏳ IOLI — Índice de Ociosidade por Limite de IA
**O que é:** % do orçamento de desenvolvimento perdido com o sistema **travado** esperando a cota da IA resetar.
**Exemplo:** Automações **22,69%** — quase um quarto do custo da semana foi pago para ferramentas
**paradas** por rate limit (429). É o sintoma nº 1 desse projeto.
**Meta:** < 1%. **Ação:** upgrade de Tier da API ou fila com backoff no Temporal/n8n.

---

## 💸 ITR — Intensidade de Tokens por Requisição
**O que é:** peso médio (tokens) de cada interação. O "custo por clique" do usuário.
**Exemplo:** Backtest **21.307 tok/req** vs. Extensões **2.933 tok/req**. O backtest injeta histórico
financeiro pesado no prompt → alto custo de input.
**Ação:** ITR subindo sem nova feature = contexto inflado → aplicar RAG/sumarização.

---

## 👷 IEET — Horas-Homem por Milhão de Tokens
**O que é:** esforço humano (já com rateio de infra) gasto para cada 1M de tokens em produção.
**Exemplo:** Backtest **6,26 HH/M-tok** (maduro/automatizado) vs. Extensões **54,56 HH/M-tok**
(exige muita mão humana por token entregue).
**Meta:** decrescente. **Ação:** IEET alto = arquitetura pouco escalável, precisa de automação.

---

## 🔥 Burn Rate de IA, IBMT e ICCA — a camada financeira (Gitman & Startup)
- **Burn Rate de IA (R$):** velocidade de queima de caixa do projeto (tokens valorados + ociosidade).
  *Ex.:* Automações **R$ 2.623,97/mês**.
- **ICCA (cobertura, x):** `MRR ÷ custo recuperado`. *Ex.:* Extensões **4,25x** (saudável) vs.
  Automações **0,99x** (< 1 = **prejuízo oculto**: gasta mais do que fatura).
- **IBMT (burn marginal, x):** `Burn Rate ÷ ΔMRR`. *Ex.:* Automações **1,19** (> 1 = quanto mais cresce,
  mais rápido o caixa seca — risco de "insolvência por crescimento") vs. Extensões **0,24** (escala lucrativa).
**Ações:** ICCA < 1 ou IBMT > 0,33 → reprecificar o plano ou cortar desperdício antes de escalar aquisição.

---

## 🎯 CPP — Custo por Ponto de Progresso (indicador-mestre)
**O que é:** `custo total de IA acumulado ÷ % de progresso`. Quanto custa avançar 1% do projeto.
**Exemplo:** Backtest **R$ 45,00/%** a 60% de progresso. **Acompanhe a tendência**: se o CPP sobe ao
longo das semanas, há inflação de escopo, retrabalho ou interrupções corroendo a eficiência.
**Meta:** decrescente.

---

## ⏱️ CDO — Custo do Desenvolvimento Ocioso
**O que é:** o R$ absoluto perdido com o time/infra parados por travas de limite (base do IOLI).
**Ação:** consolida, em reais, o prejuízo que justifica o upgrade de Tier.

---

## 📉 Pareto de Falhas (dominância)
**O que é:** isola, por projeto, qual categoria de falha domina (regra 80/20).
**Exemplo real do mock:**
- *Backtest:* **77% Alto Custo (prompt inflado)** → ação: RAG/embeddings.
- *Automações:* **75% Erro de Cota (429)** → ação: backoff/upgrade de Tier.
- *Extensões:* **80% Alucinação** → ação: system prompt rígido com saída JSON.
**Uso:** transforma a reunião de sexta em decisão objetiva — cada barra aponta a contramedida.

---

## 🪙 VRT em 5 blocos + média (2ª ótica)
**O que é:** a recuperação de custo vista em 50/100/250/500/1.000 tokens + a média dos blocos.
**Exemplo (Project A):** 50t = R$ 0,0584 · 100t = 0,1168 · 250t = 0,2919 · 500t = 0,5838 · 1.000t = 1,1676 · **média = 0,4437**.
**Para quê:** raciocinar em granularidades diferentes; a **média** dá um custo de bloco "mesclado" comparável entre projetos.

## ⏰ HCI — Horário Crítico de Interrupção
**O que é:** a hora do dia (BRT) em que cada projeto sofre mais interrupções.
**Exemplo:** `Project D` pico às **11h** (10 interrupções); `Project H` às **16h**; `Project E` às **2h** (madrugada → rate-limit).
**Ação:** atacar na janela certa — upgrade de Tier/backoff para picos de madrugada, escalonamento para picos comerciais.

## ♻️ Taxonomia de Wastes (Lean Six Sigma)
**O que é:** desperdício por categoria, medido em **tokens ponderados** (Defeito 2,0× · Cota 1,5× · Superproc. 1,0× · Latência 0,5×).
**Exemplo:** waste dominante de `Project E` = **Defeito/Alucinação** (1,72M tok); de `Project F` = **Superprocessamento/Prompt Inflado** (1,71M tok).
**Ação:** cada categoria tem solução definitiva em `solucoes_relatorios.md` (entram no Bottom-Line de cada projeto).

## 🔬 RCA — Alucinação por Tipo de Prompt
**O que é:** Root Cause Analysis — qual **categoria de prompt** mais alucina, por projeto e na **interseção** (comum a todos).
**Exemplo:** gargalo de `Project D` = **Geração de Código** (17 aluc.); **interseção do portfólio** = **Conversa/Aberto**, gargalo nº1 em **4/10 projetos (40%)**.
**Ação:** atacar o gargalo comum primeiro (maior efeito sistêmico) — ex.: converter prompts abertos em estruturados.

## 🔗 De onde vem cada dado

| KPI | Tabela/fonte no SQLite |
|---|---|
| VRT/kT, ITR, IITA, IDLS, PEUC, Pareto | `logs_langfuse` (via Langfuse) |
| IEET, IOLI, CDO, Burn Rate | `logs_langfuse` + `horas_desenvolvimento` |
| Rateio de infra (CRI) | `assinaturas_infra` |
| ICCA, IBMT | `horas_desenvolvimento.faturamento_mrr_incremental` |
| CPP, PSR (progresso/interrupções) | `projetos_status` |

> Reproduza todos estes números com: `cd foundations/pipeline && python3 seed_mock.py && python3 compute_kpis.py`
