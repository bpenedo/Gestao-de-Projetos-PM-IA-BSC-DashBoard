# KPIs — Framework de Mensuração de Projetos com IA

> **Framework "Gestão de Projetos (PM) IA com Painel BSC e DashBoard"** · ©️ Bruno Teixeira Penedo — 2026. Todos os direitos reservados. E-mail: bpenedo@gmail.com

> **Princípio (Kaplan & Norton):** *"O que não é medido não pode ser gerenciado nem melhorado."*
> Sem métrica não há eficiência — há opinião. Todo KPI aqui é **calculável** (fórmula explícita),
> **rastreável** (fonte de dados) e **acionável** (meta/benchmark).

Este arquivo concentra **TODOS os KPIs** do framework, em 3 categorias:
1. Boas Práticas (maturidade de execução)
2. Capital Humano (retorno de horas-homem)
3. Retorno Financeiro

Relacionado: [`projeto_main.md`](projeto_main.md) — cronograma, Gantt, stages e sprints.

---

## ⭐ KPI-Mestre — Custo por Ponto de Progresso (CPP)

**`CPP = Custo total de IA acumulado ÷ % de progresso atingido`** → **R$/%**

Funde as 3 categorias num único número. Sobe quando há inflação de escopo, retrabalho ou
interrupções (que forçam re-prompt). **Acompanhe a tendência**, não só o valor: CPP em queda =
projeto ficando mais eficiente conforme avança.

---

## Categoria 1 — Boas Práticas (Maturidade e Qualidade de Execução)

| KPI | O que mede | Fórmula | Unidade | Fonte | Meta | Freq. |
|---|---|---|---|---|---|---|
| Prompt Yield | Quão direto se chega ao resultado | `entregas aceitas ÷ total de prompts` | % | logs | ≥ 40% | Semanal |
| Taxa de Retrabalho de IA | Saídas refeitas/corrigidas | `prompts de correção ÷ total de prompts` | % | logs | ≤ 25% | Semanal |
| First-Pass Yield | Acerto na 1ª tentativa | `ok no 1º prompt ÷ tarefas` | % | logs | ≥ 30% | Semanal |
| Densidade de Interrupção | Quebras de fluxo por hora | `nº interrupções ÷ horas de foco` | int/h | registro | ≤ 1,5/h | Diária |
| Scope Fidelity | Entrega bate com o spec | `requisitos atendidos ÷ planejados` | % | backlog | ≥ 90% | Sprint |
| Cobertura de Validação | Saídas revisadas antes do uso | `saídas validadas ÷ saídas usadas` | % | QA | 100% | Contínua |
| Reuso de Prompt | Maturidade de versionamento | `prompts reaproveitados ÷ criados` | % | biblioteca | ≥ 50% | Mensal |

## Categoria 2 — Capital Humano (Retorno de Horas-Homem)

| KPI | O que mede | Fórmula | Unidade | Fonte | Meta | Freq. |
|---|---|---|---|---|---|---|
| Horas Economizadas por IA | Ganho vs. manual | `horas manuais estimadas − horas reais com IA` | h | timesheet | > 0 | Entrega |
| Fator de Aceleração (Leverage) | Multiplicador de produtividade | `horas manuais ÷ horas reais com IA` | x | timesheet | ≥ 2,0x | Mensal |
| Custo-Hora Efetivo Humano | Custo da hora entregue | `custo total RH ÷ horas produtivas` | R$/h | folha+timesheet | baseline | Mensal |
| Focus Ratio | Foco vs. interrupção | `horas focadas ÷ (focadas + interrompidas)` | % | registro | ≥ 75% | Semanal |
| Custo das Interrupções | Perda do contexto quebrado | `nº interrupções × tempo retomada × custo-hora` | R$ | registro+folha | minimizar | Semanal |
| **Custo de Oportunidade por Interrupção** | Valor NÃO entregue por cada quebra | `(duração + retomada em h) × valor gerado por hora-homem` | R$ | registro+financeiro | minimizar | Semanal |
| Custo de Oportunidade Acumulado | Soma do valor perdido no período | `Σ custo de oportunidade de todas as interrupções` | R$ | Interrupcoes.md | minimizar | Semanal |
| Prompts por Hora-Homem | Intensidade de uso da IA | `total de prompts ÷ horas-homem` | int/h | logs+timesheet | baseline | Semanal |
| Progresso por Hora-Homem | Avanço por hora investida | `Δ% progresso ÷ horas-homem` | %/h | PM+timesheet | crescente | Semanal |

## Categoria 3 — Retorno Financeiro

| KPI | O que mede | Fórmula | Unidade | Fonte | Meta | Freq. |
|---|---|---|---|---|---|---|
| Gasto de Tokens por Projeto | Custo direto de IA | `Σ(tokens_in×preço_in + tokens_out×preço_out)` | R$ | billing (com tag) | no orçamento | Diária/Mensal |
| Custo de Assinatura Alocado | Rateio da assinatura | `assinatura mensal × (uso projeto ÷ uso total)` | R$ | faturas | — | Mensal |
| TCO-IA por Projeto | Custo total de IA | `tokens + assinatura alocada + infra` | R$ | consolidado | no orçamento | Mensal |
| **Custo por Ponto de Progresso** | Custo de avançar 1% | `custo total IA ÷ % progresso` | R$/% | billing+PM | decrescente | Semanal |
| Custo por Prompt Efetivo | Eficiência da interação | `custo total tokens ÷ prompts aceitos` | R$/prompt | billing+logs | decrescente | Semanal |
| ROI | Retorno sobre investimento | `(valor gerado − custo total) ÷ custo total` | % | financeiro | > 100% | Projeto |
| Payback | Tempo de recuperação | `custo total ÷ ganho mensal` | meses | financeiro | ≤ 6 | Projeto |
| VPL (NPV) | Valor presente líquido | `Σ[fluxo_t ÷ (1+i)^t] − investimento` | R$ | financeiro | > 0 | Projeto |
| Custo por Interrupção | Impacto monetário das quebras | `interrupções × (tempo retomada + tokens re-contexto × preço)` | R$ | registro+billing | minimizar | Semanal |

## Categoria 4 — KPIs Avançados (EVM, Eficiência de Tokens, Fluxo e Risco)

### 4.1 Valor Agregado (Earned Value Management — EVM)

| KPI | O que mede | Fórmula | Unidade | Fonte | Meta | Freq. |
|---|---|---|---|---|---|---|
| Valor Planejado (PV) | Custo orçado do trabalho previsto até a data | `% planejado × orçamento total` | R$ | PM+orçamento | baseline | Semanal |
| Valor Agregado (EV) | Custo orçado do que foi entregue | `% progresso real × orçamento total` | R$ | PM+orçamento | — | Semanal |
| Custo Real (AC) | Quanto efetivamente foi gasto | `TCO-IA acumulado` | R$ | Tokens.md | — | Semanal |
| CPI (Índice de Custo) | Eficiência de custo | `EV ÷ AC` | ratio | EVM | ≥ 1,0 | Semanal |
| SPI (Índice de Prazo) | Eficiência de cronograma | `EV ÷ PV` | ratio | EVM | ≥ 1,0 | Semanal |
| EAC (Custo na Conclusão) | Projeção do custo final | `orçamento total ÷ CPI` | R$ | EVM | ≤ orçamento | Mensal |
| Variação de Custo (CV) | Desvio orçamentário | `EV − AC` | R$ | EVM | ≥ 0 | Semanal |

### 4.2 Eficiência de Tokens & IA

| KPI | O que mede | Fórmula | Unidade | Fonte | Meta | Freq. |
|---|---|---|---|---|---|---|
| Razão Output/Input | Densidade de geração por token de entrada | `tokens_out ÷ tokens_in` | ratio | Tokens.md | baseline | Semanal |
| Valor por Token | Retorno gerado por token gasto | `valor gerado ÷ total de tokens` | R$/token | finance+Tokens.md | crescente | Mensal |
| Tokens por Entrega | Custo cognitivo de cada entregável | `total de tokens ÷ entregas aceitas` | tok/entrega | Tokens.md+logs | decrescente | Semanal |
| Tokens Desperdiçados | Tokens em retrabalho + re-contexto | `tokens_retrabalho + tokens_recontexto` | tokens | Tokens.md | minimizar | Semanal |
| Taxa de Desperdício de Tokens | Fração de tokens sem valor | `tokens desperdiçados ÷ total de tokens` | % | Tokens.md | ≤ 15% | Semanal |
| Taxa de Automação | Trabalho feito por IA vs. manual | `tarefas via IA ÷ total de tarefas` | % | logs+PM | crescente | Mensal |

### 4.3 Fluxo & Entrega (Lean/Ágil)

| KPI | O que mede | Fórmula | Unidade | Fonte | Meta | Freq. |
|---|---|---|---|---|---|---|
| Velocity | Entrega por sprint | `Σ pontos/entregas concluídas na sprint` | pts/sprint | PM | estável/crescente | Sprint |
| Lead Time | Da solicitação à entrega | `data entrega − data solicitação` | dias | PM | decrescente | Por entrega |
| Cycle Time | Do início ao fim da execução | `data conclusão − data início` | dias | PM | decrescente | Por entrega |
| Throughput | Volume entregue por período | `nº entregas aceitas ÷ período` | entregas/sem | PM | crescente | Semanal |
| Burn Rate | Velocidade de queima do orçamento | `custo no período ÷ período` | R$/sem | Tokens.md | dentro do plano | Semanal |
| Taxa de Entrega no Prazo | Cumprimento de prazos | `entregas no prazo ÷ total de entregas` | % | PM | ≥ 90% | Sprint |

### 4.4 Qualidade & Risco

| KPI | O que mede | Fórmula | Unidade | Fonte | Meta | Freq. |
|---|---|---|---|---|---|---|
| Taxa de Alucinação | Saídas factualmente erradas da IA | `saídas incorretas ÷ saídas verificadas` | % | QA | ≤ 5% | Semanal |
| Densidade de Defeitos | Erros por entrega | `nº defeitos ÷ entregas` | def/entrega | QA | decrescente | Sprint |
| MTTR de Interrupção | Tempo médio de recuperação | `Σ tempo de retomada ÷ nº interrupções` | min | Interrupcoes.md | decrescente | Semanal |
| Índice de Troca de Contexto | Penalidade de multitarefa | `interrupções × penalidade média de retomada` | min | Interrupcoes.md | minimizar | Semanal |
| Exposição ao Risco | Impacto esperado de riscos abertos | `Σ (probabilidade × impacto R$)` | R$ | registro de risco | minimizar | Mensal |

## Categoria 5 — Economia de Tokens & APIs de Terceiros (OpenAI/Anthropic)

> KPIs específicos do modelo de consumo via API + assinatura (SaaS multicanal). Fonte primária
> recomendada: **Langfuse** (tags por `userId`/`projectId`) → ETL → SQLite → painel.

| Sigla | KPI | Fórmula | Unidade | Meta | Persp. BSC |
|---|---|---|---|---|---|
| **IEET** | Eficiência de Esforço por Token | `horas trabalhadas ÷ (tokens ÷ 1.000.000)` | HH/M-tok | decrescente | Processos/Financeira |
| **IOLI** | Ociosidade por Limite de IA | `CDO acumulado ÷ custo total de desenvolvimento` | % | < 1% | Processos/Financeira |
| **ITR** | Intensidade de Tokens por Requisição | `Σ tokens (in+out) ÷ total de prompts` | tok/req | estável/↓ | Financeira |
| **IITA** | Inflação de Tokens por Alucinação | `tokens em loops de correção ÷ total de tokens` | % | < 10% | Processos/Financeira |
| **PEUC** | % de Entregáveis Úteis por Sessão | `Σ entregáveis úteis (nota 1) ÷ Σ sessões` | % | > 90% | Cliente |
| **ICCA** | Cobertura de Custo de IA | `MRR do projeto ÷ (tokens × VRT/1.000)` | x | > 3,0x | Financeira |
| **IDLS** | Desperdício Lean por Sessão | `(tokens ponderados por erro + custo do tempo bloqueado) ÷ custo total da sessão` | % | < 15% | Processos (Lean) |
| **IBMT** | Burn Rate Marginal do Token | `Burn Rate de IA ÷ Δ MRR` | x | < 0,33 | Financeira (Gitman) |
| **CDO** | Custo do Desenvolvimento Ocioso | `minutos bloqueados × (custo-hora projeto ÷ 60)` | R$ | minimizar | Financeira |

**Pesos punitivos de falha (precificação interna):** `RATE_LIMIT (cota) = 1,5×` · `ALUCINAÇÃO/CÓDIGO = 2,0×`
sobre os tokens da iteração defeituosa. **Latência excedente (Lean):** `LE = max(0; latência − 3s)`.

---

# 🔬 Fronteira da Ciência de KPI

> Conceitos proprietários deste framework. **©️ Bruno Teixeira Penedo — 2026. Todos os direitos reservados. E-mail: bpenedo@gmail.com**

## 5.A — Unidade de Recuperação Tokenizável (kTR) — "o m² da era da IA"

Na obra *Administração Financeira e Orçamentária* de **Lawrence Gitman**, o **metro quadrado (m²)**
é a **base de rateio** que consolida e recupera custos heterogêneos de um estabelecimento —
energia, água, gás, internet, IPTU, aluguel — distribuindo-os por uma única unidade física comum.

Estabelecemos aqui o equivalente para projetos de IA: o **kTR — quilo-Token de Recuperação**
(bloco de **1.000 tokens**). Assim como o m² rateia o custo do espaço, o **kTR rateia e recupera
todo o custo do trabalho cognitivo de IA** numa única unidade tokenizável e comparável entre projetos.

### Valor de Recuperação por kT (VRT/kT) — a unidade monetária

```
VRT/kT  =  ( Preço médio da API por 1k tokens  +  CRI )  ×  FIA
```
| Componente | Significado | Fórmula | Análogo no m² de Gitman |
|---|---|---|---|
| Preço API/1k | Custo bruto do fornecedor (OpenAI/Anthropic) | tabela do provedor | Custo direto do espaço |
| **CRI** | Custo de Rateio de Infra por 1k tokens | `Custo de Rateio mensal (CR) ÷ (tokens do mês ÷ 1.000)` | Rateio de energia/água/IPTU por m² |
| **FIA** | Fator de Inflação por Alucinação | `100 ÷ (100 − IITA)` | Provisão para perdas/ociosidade |

> **CR** = soma das assinaturas fixas (ver [`Assinatura_IA.md`](Assinatura_IA.md)). **IITA** = ver Categoria 5.

**Exemplo (Gitman aplicado):** Preço API = R$ 0,025/1k · CRI = R$ 0,010/1k · IITA = 20% → FIA = 1,25.
`VRT/kT = (0,025 + 0,010) × 1,25 =` **R$ 0,04375 por 1.000 tokens.** Cada kTR deste projeto precisa
recuperar ~4,4 centavos para cobrir API + infraestrutura rateada + desperdício.

> **Ficha:** Perspectiva BSC = Financeira (sustentabilidade) · Meta = decrescente · Unidade-base de
> todo rateio financeiro do framework (alimenta ICCA, IBMT e o CPP).

## 5.B — Score / Rating de Projeto (PSR 0–5 ⭐)

Índice **individual** que classifica cada projeto de **0 a 5**, composto por três eixos exigidos:
**avanço de progresso**, **número de interrupções** e **soluções entregues com sucesso integral por sessão**.

```
PSR = (0,40 × S_progresso) + (0,25 × S_interrupcao) + (0,35 × S_entrega)
```
| Sub-score (0–5) | Mede | Fórmula | Fonte |
|---|---|---|---|
| **S_progresso** | Avanço de % no período vs. planejado | `min(5; (Δ% real ÷ Δ% planejado) × 5)` | [`projeto_main.md`](projeto_main.md) |
| **S_interrupcao** | Poucas interrupções = melhor | `5 × (1 − min(1; nº interrupções ÷ teto))` | [`Interrupcoes.md`](Interrupcoes.md) |
| **S_entrega** | Sessões com solução 100% útil (PEUC) | `(PEUC% ÷ 100) × 5` | logs/Langfuse |

**Faixas de classificação:**
| PSR | Estrelas | Status |
|---|---|---|
| 4,5 – 5,0 | ⭐⭐⭐⭐⭐ | Excelente (escalar) |
| 3,5 – 4,4 | ⭐⭐⭐⭐ | Bom |
| 2,5 – 3,4 | ⭐⭐⭐ | Regular (ajustar) |
| 1,5 – 2,4 | ⭐⭐ | Crítico (intervir) |
| 0 – 1,4 | ⭐ | Insustentável (pausar/refatorar) |

**Exemplo:** Δ%real/planejado = 100% → S_prog 5 · 5 interrupções / teto 20 → S_int = 5×(1−0,25)=3,75 ·
PEUC 80% → S_entrega 4,0. `PSR = 0,40×5 + 0,25×3,75 + 0,35×4,0 = 2,0+0,94+1,4 =` **4,34 → ⭐⭐⭐⭐ Bom.**

> **Ficha:** registra-se no snapshot de cada `<projeto>.md` e no [`BSC_Dashboard.md`](BSC_Dashboard.md).
> O `teto` de interrupções é parametrizável por projeto (default 20/semana).

---

## Categoria 6 — Diagnóstico Operacional, Wastes & RCA

### 6.A — VRT em 5 blocos + média (2ª ótica de consumo)
A unidade de recuperação [[#5.A — Unidade de Recuperação Tokenizável (kTR)]] é reexpressa em **5 granularidades**
para uma segunda percepção do consumo por projeto: `VRT/N = VRT/kT × (N ÷ 1.000)`.

| Bloco | Fórmula | Uso |
|---|---|---|
| 50 / 100 / 250 / 500 tok | `VRT/kT × 0,05 / 0,10 / 0,25 / 0,50` | leitura fina por interação |
| 1.000 tok (padrão) | `VRT/kT` | base de rateio |
| **Média dos blocos** | `VRT/kT × (0,05+0,10+0,25+0,50+1,0) ÷ 5` | custo de bloco "mesclado" comparável entre projetos |

### 6.B — HCI: Horário Crítico de Interrupção/Impacto
| KPI | O que mede | Fórmula | Unidade | Fonte | Meta |
|---|---|---|---|---|---|
| **HCI** | Hora do dia (BRT) de pico de interrupções por projeto | `argmax_hora( COUNT(falhas) por hora )` | hora (0–23) | `logs_langfuse` (hora do timestamp, UTC−3) | diagnóstico |

Diagnóstico: aponta **quando** cada projeto é mais impactado (ex.: madrugada = rate-limit; horário comercial = uso intenso) → ação na janela certa (upgrade de Tier, backoff, agendamento).

### 6.C — Taxonomia de Wastes (Lean Six Sigma) por tokens ponderados
| Waste (taxonomia) | Origem | Peso | KPI/meta |
|---|---|---|---|
| Defeito (Defects) — Alucinação/Retrabalho | `tipo_erro=ALUCINACAO_CODIGO` | 2,0× | IITA < 10% |
| Espera (Waiting) — Cota/429 | `tipo_erro=RATE_LIMIT` | 1,5× | IOLI < 1% |
| Superprocessamento — Prompt Inflado | tokens > 15.000 | 1,0× | ITR ↓ |
| Espera (Waiting) — Latência Alta | latência > 3s | 0,5× | latência < 3s |

`waste_tokens = Σ (tokens da falha × peso)`. O **waste dominante** por projeto = categoria de maior `waste_tokens`.
Soluções definitivas: ver [`solucoes_relatorios.md`](solucoes_relatorios.md).

### 6.D — RCA: Alucinação por Tipo de Prompt (Root Cause Analysis)
Classifica os prompts numa **taxonomia** (Geração de Código, Raciocínio/Análise, Conversa/Aberto, Extração de
Dados, RAG/Busca, Transformação/Formato, Sumarização) e mede a alucinação de cada uma.

| KPI | O que mede | Fórmula |
|---|---|---|
| Taxa de alucinação por categoria | % de alucinação de cada tipo de prompt no projeto | `alucinações_categoria ÷ prompts_categoria × 100` |
| **Gargalo do projeto** | tipo de prompt que mais alucina (atrasa o projeto) | `argmax_categoria( alucinações )` |
| **Interseção (comum a todos)** | tipo de prompt que é gargalo nº1 no maior nº de projetos | `argmax_categoria( nº projetos onde é top-1 )` |

Diagnóstico objetivo: o que atrasa **cada** projeto e o que atrasa **comumente a todos**. Contramedidas por
categoria: ver [`solucoes_relatorios.md`](solucoes_relatorios.md).

> **Implementação:** todas estas métricas estão em [`pipeline/queries/`](pipeline/README.md) e no dashboard Evidence.

---

## ⭐ KPIs Prioritários (Dashboard Executivo)

1. **Custo por Ponto de Progresso (R$/%)** — o indicador-mestre.
2. **Prompt Yield (%)** — quantas interações até o resultado.
3. **Focus Ratio (%)** — interrupções traduzidas em saúde do projeto.
4. **Leverage (x)** — horas-homem realmente economizadas pela IA.
5. **TCO-IA (R$)** — custo total para comparar projetos.
6. **ROI (%)** — o investimento se pagou.

## 🔗 Correlações entre Categorias

```
INTERRUPÇÕES → quebram contexto → RE-PROMPT (re-explicar o estado)
   │                                   │
   ▼                                   ▼
 ↓ Focus Ratio                   ↑ Tokens consumidos
   │                                   │
   ▼                                   ▼
 ↓ Progresso/hora-homem ────────► ↑ Custo por Ponto de Progresso → ↓ ROI
```

- Cada interrupção costuma exigir re-explicar o estado à IA → tokens de input desperdiçados.
- Retrabalho de IA consome tokens sem avançar o `%` → empurra o CPP para cima.
- Leverage alto só vira ROI quando o Focus Ratio se mantém alto.

## 📥 Dependências de Dados (coletar primeiro)

| Dado | Alimenta | Como capturar |
|---|---|---|
| Tokens in/out **com tag de projeto** | Gasto de tokens, CPP, custo/prompt | tag por sessão + export do billing |
| Valor e nº de seats da assinatura | Assinatura alocada, TCO | faturas mensais |
| `%` de progresso por período | CPP, progresso/hora-homem | atualização manual no PM |
| Horas-homem por projeto | Leverage, custo-hora, Focus Ratio | timesheet |
| Log de prompts (total, correções, aceitos) | Yield, First-Pass, Retrabalho | histórico da ferramenta |
| Registro de interrupções (qtd, duração, retomada) | Densidade, Focus, Custo | anotação/app de foco |
| Valor gerado (economia/receita) | ROI, Payback, VPL | estimativa financeira |

> ⚠️ **Pré-requisito #1:** sem **tag de projeto** no consumo de tokens, nenhum KPI financeiro
> por projeto funciona. Estruture isso antes de tudo.

## Erros Comuns

| Erro | Correção |
|---|---|
| Medir tokens sem tag de projeto | Rotular toda sessão antes de medir. |
| Reportar o CPP uma vez só | Reportar a **tendência** entre períodos. |
| Contar todos os prompts como produtivos | Separar aceitos vs. correção (Prompt Yield). |
| Tratar interrupções como "subjetivas" | Quantificar: viram tokens + horas perdidas. |
| Medir custo sem medir valor gerado | Sem valor, ROI/Payback/VPL são impossíveis. |
