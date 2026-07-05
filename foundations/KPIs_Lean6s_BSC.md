# 📊 Catálogo Completo — KPIs, Lean Six Sigma & BSC

> **Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard** · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
>
> Lista **TODOS** os indicadores do projeto: KPIs das 4 perspectivas do Balanced Scorecard,
> economia de tokens/APIs, EVM, financeiro de investimento, conceitos de fronteira, RCA e os
> desperdícios (Wastes) do Lean Six Sigma — com acrônimos, descrições e fórmulas.
>
> Referências: [`KPIs.md`](KPIs.md) · [`KPIs_README.md`](KPIs_README.md) · [`BSC_Dashboard.md`](BSC_Dashboard.md) · [`solucoes_relatorios.md`](solucoes_relatorios.md) · [`pipeline/queries/`](pipeline/README.md)

**Legenda:** ↓ = quanto menor melhor · ↑ = quanto maior melhor · R$ = reais · US$ = dólares

---

## ⭐ Indicador-Mestre

| Sigla | Nome | Descrição / Funcionalidade | Fórmula | Meta |
|---|---|---|---|---|
| **CPP** | Custo por Ponto de Progresso | Quanto custa avançar 1% do projeto; funde custo + progresso. Acompanha-se a **tendência**. | `TCO-IA acumulado ÷ % progresso` | ↓ |
| **PSR** | Project Score Rating (0–5 ⭐) | Nota única de saúde do projeto (progresso + interrupção + entrega). | `0,40·S_prog + 0,25·S_int + 0,35·S_entrega` | ≥ 3,5 |

---

## 🏦 BSC — Perspectiva 1: FINANCEIRA

| Sigla | Nome | Descrição / Funcionalidade | Fórmula | Meta |
|---|---|---|---|---|
| GTP | Gasto de Tokens por Projeto | Custo direto de IA (input+output) por projeto. | `Σ(tok_in×preço_in + tok_out×preço_out)` | orçamento |
| CAA | Custo de Assinatura Alocado | Rateio da assinatura fixa por projeto. | `assinatura × (uso_proj ÷ uso_total)` | — |
| TCO-IA | Custo Total de IA por Projeto | Tokens + assinatura rateada + infra. | `tokens + assinatura_alocada + infra` | orçamento |
| CPPE | Custo por Prompt Efetivo | Eficiência financeira da interação. | `custo_tokens ÷ prompts_aceitos` | ↓ |
| ROI | Retorno sobre Investimento | Retorno percentual do projeto. | `(valor_gerado − custo) ÷ custo` | > 100% |
| — | Payback (simples) | Tempo de recuperação do investimento. | `custo_total ÷ ganho_mensal` | ≤ 6 m |
| VPL/NPV | Valor Presente Líquido | Valor presente dos fluxos menos investimento. | `Σ[fluxo_t ÷ (1+i)^t] − investimento` | > 0 |
| Burn Rate | Taxa de Queima de Caixa | Velocidade de consumo de caixa de IA por período. | `custo_no_período ÷ período` | plano |

## 👥 BSC — Perspectiva 2: CLIENTE / ENTREGA

| Sigla | Nome | Descrição / Funcionalidade | Fórmula | Meta |
|---|---|---|---|---|
| **PEUC** | Percentual de Entregáveis Úteis por Sessão | % de sessões que terminaram sem falha (entrega útil). | `sessões_sem_falha ÷ total_sessões ×100` | > 90% |
| SF | Scope Fidelity | Aderência da entrega ao escopo especificado. | `requisitos_atendidos ÷ planejados` | ≥ 90% |
| TEP | Taxa de Entrega no Prazo | Cumprimento de prazos das entregas. | `entregas_no_prazo ÷ total` | ≥ 90% |
| CV% | Cobertura de Validação | Saídas revisadas antes do uso. | `saídas_validadas ÷ usadas` | 100% |
| THR | Throughput | Volume entregue por período. | `entregas_aceitas ÷ período` | ↑ |
| VpT | Valor por Token | Retorno gerado por token gasto. | `valor_gerado ÷ total_tokens` | ↑ |

## ⚙️ BSC — Perspectiva 3: PROCESSOS INTERNOS

| Sigla | Nome | Descrição / Funcionalidade | Fórmula | Meta |
|---|---|---|---|---|
| PY | Prompt Yield | Quão direto se chega ao resultado. | `entregas_aceitas ÷ total_prompts` | ≥ 40% |
| FPY | First-Pass Yield | Acerto na 1ª tentativa (sem reprompt). | `ok_1º_prompt ÷ tarefas` | ≥ 30% |
| TRIA | Taxa de Retrabalho de IA | Saídas refeitas/corrigidas. | `prompts_correção ÷ total_prompts` | ≤ 25% |
| **ITR** | Intensidade de Tokens por Requisição | Peso médio (tokens) de cada interação. | `Σ tokens ÷ total_prompts` | estável/↓ |
| **IITA** | Índice de Inflação de Tokens por Alucinação | % de tokens queimados em loops de correção. | `tokens_desperdiçados ÷ total ×100` | < 10% |
| DI | Densidade de Interrupção | Quebras de fluxo por hora de foco. | `nº_interrupções ÷ horas_foco` | ≤ 1,5/h |
| **HCI** | Horário Crítico de Interrupção/Impacto | Hora do dia (BRT) de pico de interrupções por projeto. | `argmax_hora(COUNT falhas)` | diagnóstico |
| MTTR | Mean Time To Recovery (interrupção) | Tempo médio de recuperação após interrupção. | `Σ tempo_retomada ÷ nº_interrupções` | ↓ |
| ITC | Índice de Troca de Contexto | Penalidade de multitarefa. | `interrupções × penalidade_retomada` | ↓ |
| LT | Lead Time | Da solicitação à entrega. | `data_entrega − data_solicitação` | ↓ |
| CT | Cycle Time | Do início ao fim da execução. | `data_conclusão − data_início` | ↓ |
| VEL | Velocity | Entrega por sprint. | `Σ pontos/entregas na sprint` | estável/↑ |
| TA | Taxa de Automação | Trabalho feito por IA vs. manual. | `tarefas_via_IA ÷ total` | ↑ |
| TAL | Taxa de Alucinação | Saídas factualmente erradas da IA. | `saídas_incorretas ÷ verificadas` | ≤ 5% |
| DD | Densidade de Defeitos | Erros por entrega. | `nº_defeitos ÷ entregas` | ↓ |
| R O/I | Razão Output/Input | Densidade de geração por token de entrada. | `tokens_out ÷ tokens_in` | baseline |
| TDT | Taxa de Desperdício de Tokens | Fração de tokens sem valor. | `tokens_desperdiçados ÷ total` | ≤ 15% |

## 🌱 BSC — Perspectiva 4: APRENDIZADO & CRESCIMENTO

| Sigla | Nome | Descrição / Funcionalidade | Fórmula | Meta |
|---|---|---|---|---|
| HEIA | Horas Economizadas por IA | Ganho vs. fazer manual. | `horas_manuais_est − horas_reais_IA` | > 0 |
| LEV | Leverage / Fator de Aceleração | Multiplicador de produtividade da IA. | `horas_manuais ÷ horas_reais_IA` | ≥ 2,0x |
| FR | Focus Ratio | Foco vs. interrupção. | `horas_focadas ÷ (focadas+interrompidas)` | ≥ 75% |
| CHE | Custo-Hora Efetivo Humano | Custo da hora produtiva entregue. | `custo_RH ÷ horas_produtivas` | baseline |
| RP | Reuso de Prompt | Maturidade de versionamento de prompt. | `prompts_reaproveitados ÷ criados` | ≥ 50% |
| PHH | Prompts por Hora-Homem | Intensidade de uso da IA. | `total_prompts ÷ horas-homem` | baseline |
| PgHH | Progresso por Hora-Homem | Avanço por hora investida. | `Δ%_progresso ÷ horas-homem` | ↑ |
| **IEET** | Índice de Eficiência de Esforço por Token | Horas-homem por 1 milhão de tokens. | `horas ÷ (tokens ÷ 1.000.000)` | ↓ |

---

## 💸 CUSTO DE INTERRUPÇÕES & OPORTUNIDADE

| Sigla | Nome | Descrição / Funcionalidade | Fórmula | Meta |
|---|---|---|---|---|
| CI | Custo das Interrupções | Perda direta (tempo + tokens de re-contexto). | `Σ[(dur+retomada)/60×custo_h] + tokens×preço` | ↓ |
| **CDO** | Custo do Desenvolvimento Ocioso | R$ perdido com time/infra parados por trava de cota. | `min_bloqueados × (custo_hora ÷ 60)` | ↓ |
| COI | Custo de Oportunidade por Interrupção | Valor NÃO entregue por cada quebra. | `(dur+retomada em h) × valor/hora-homem` | ↓ |
| COA | Custo de Oportunidade Acumulado | Soma do valor perdido no período. | `Σ COI` | ↓ |

---

## 📐 EVM — Earned Value Management (Valor Agregado)

| Sigla | Nome | Descrição / Funcionalidade | Fórmula | Meta |
|---|---|---|---|---|
| PV | Planned Value (Valor Planejado) | Custo orçado do trabalho previsto até a data. | `%_planejado × orçamento` | baseline |
| EV | Earned Value (Valor Agregado) | Custo orçado do que foi entregue. | `%_real × orçamento` | — |
| AC | Actual Cost (Custo Real) | Quanto foi efetivamente gasto. | `TCO-IA acumulado` | — |
| CPI | Cost Performance Index | Eficiência de custo. | `EV ÷ AC` | ≥ 1,0 |
| SPI | Schedule Performance Index | Eficiência de cronograma. | `EV ÷ PV` | ≥ 1,0 |
| EAC | Estimate At Completion | Projeção do custo final. | `orçamento ÷ CPI` | ≤ orçamento |
| CV | Cost Variance (Variação de Custo) | Desvio orçamentário. | `EV − AC` | ≥ 0 |

---

## 💰 FINANCEIRO DE INVESTIMENTO (BRL & USD)

| Sigla | Nome | Descrição / Funcionalidade | Fórmula | Meta |
|---|---|---|---|---|
| VPL | Valor Presente Líquido | Valor presente dos fluxos − investimento (R$ e US$). | `Σ fluxo_t ÷ (1+i)^t` | > 0 |
| **TIR** | Taxa Interna de Retorno | Taxa que zera o VPL (retorno do projeto). | raiz de `VPL(r)=0` (bisseção) | > taxa/SELIC |
| **ILL** | Índice de Lucratividade Líquida (Profitability Index) | VP das entradas ÷ investimento. > 1 = cria valor. | `Σ VP_entradas ÷ |investimento|` | > 1 |
| PBS | Payback Simples | Períodos até o acumulado ficar positivo (interpolado). | cruzamento de `Σ fluxo ≥ 0` | ↓ |
| PBD | Payback Descontado | Idem, sobre fluxo descontado (BRL e US$). | cruzamento de `Σ fluxo_desc ≥ 0` | ↓ |
| — | Comparação SELIC / Juros EUA | TIR vs. SELIC (BR) e Fed funds (EUA); dolarização do fluxo. | `TIR > SELIC?` · `TIR > US?` | supera |

---

## 🪙 FRONTEIRA DA CIÊNCIA DE KPI (proprietários)

| Sigla | Nome | Descrição / Funcionalidade | Fórmula | Meta |
|---|---|---|---|---|
| **kTR** | quilo-Token de Recuperação | Unidade base de rateio (bloco de 1.000 tokens) — "o m² de Gitman" da era da IA. | unidade (1.000 tokens) | — |
| **VRT** | Valor de Recuperação por kT | Custo de recuperação por 1.000 tokens (API + rateio + desperdício). | `(preço_API/1k + CRI) × FIA` | ↓ |
| CRI | Custo de Rateio de Infra por 1k | Rateio das assinaturas fixas por 1.000 tokens. | `CR_mensal ÷ (tokens_mês ÷ 1.000)` | ↓ |
| FIA | Fator de Inflação por Alucinação | Multiplicador de custo por desperdício. | `100 ÷ (100 − IITA)` | → 1 |
| VRT-5B | VRT em 5 blocos + média | 2ª ótica: VRT em 50/100/250/500/1.000 tok + média. | `VRT/kT × (N ÷ 1.000)` | — |
| **PSR** | Project Score Rating (0–5) | Nota única de saúde (ver Indicador-Mestre). | ver acima | ≥ 3,5 |
| **ICCA** | Índice de Cobertura de Custo de IA | Receita cobre o custo recuperado? | `MRR ÷ (tokens × VRT/1.000)` | > 3,0x |
| **IBMT** | Índice de Burn Rate Marginal do Token | Queima de caixa por R$ de nova receita. | `Burn Rate IA ÷ Δ MRR` | < 0,33 |

---

## ♻️ LEAN SIX SIGMA — Desperdícios (Wastes / Muda) & Índices

Mapeamento dos **8 desperdícios** do Lean para o ciclo de IA, medidos por **tokens ponderados**.

| Sigla | Waste (taxonomia) | Descrição / Funcionalidade no contexto de IA | Peso | KPI/Meta |
|---|---|---|---|---|
| **IDLS** | Índice de Desperdício Lean por Sessão | % de tokens/tempo em atividades sem valor (defeito+cota+latência). | — | < 15% |
| D | **Defeito (Defects)** | Alucinação / código quebrado / retrabalho. | 2,0× | IITA < 10% |
| W1 | **Espera (Waiting) — Cota/429** | Fila travada por Rate Limit / estouro de cota (TPM/RPD). | 1,5× | IOLI < 1% |
| O | **Superprocessamento (Overprocessing)** | Prompt inflado; contexto bruto excessivo (>15k tokens). | 1,0× | ITR ↓ |
| W2 | **Espera (Waiting) — Latência Alta** | Latência de resposta acima de 3s (Muda de espera). | 0,5× | latência < 3s |
| — | Superprodução (Overproduction) | Respostas longas além do necessário (tokens de saída extras). | — | ITR controlado |
| — | Talento Subutilizado (Non-utilized talent) | Dev corrigindo prompt manualmente em vez de arquitetar. | — | LEV ↑ |
| — | Movimentação / Transporte | Re-contexto por troca de sessão (tokens de re-explicação). | — | FR ↑ |

### Índices Lean derivados
| Sigla | Nome | Descrição / Funcionalidade | Fórmula | Meta |
|---|---|---|---|---|
| **IOLI** | Índice de Ociosidade por Limite de IA | % do orçamento perdido com sistema travado esperando cota resetar. | `CDO ÷ custo_total_dev ×100` | < 1% |
| LE | Latência Excedente | Tempo de espera além do limite aceitável de 3s. | `max(0; latência − 3)` | 0 |
| ER | Exposição ao Risco | Impacto esperado de riscos abertos. | `Σ(probabilidade × impacto R$)` | ↓ |

---

## 🔬 RCA — Root Cause Analysis (Alucinação por Taxonomia de Prompt)

Classifica os prompts em **7 categorias** e mede a alucinação de cada uma, por projeto e na interseção.

| Métrica | Descrição / Funcionalidade | Fórmula |
|---|---|---|
| Taxa de alucinação por categoria | % de alucinação de cada tipo de prompt no projeto. | `alucinações_cat ÷ prompts_cat ×100` |
| Gargalo do projeto | Tipo de prompt que mais alucina (atrasa o projeto). | `argmax_cat(alucinações)` |
| Interseção do portfólio | Tipo de prompt que é gargalo nº1 no maior nº de projetos. | `argmax_cat(nº projetos onde é top-1)` |

**Taxonomia de prompts:** `Geração de Código` · `Raciocínio/Análise` · `Conversa/Aberto` · `Extração de Dados` · `RAG/Busca` · `Transformação/Formato` · `Sumarização`.

---

## 🧰 Ferramentas Administrativas (no BSC_Dashboard)

Matriz **BCG** (Star/Cash Cow/Question Mark/Dog) · **GUT** (Gravidade×Urgência×Tendência) · **Eisenhower**
(Urgente×Importante) · **Matriz de Riscos** (Probabilidade×Impacto) · **Pareto 80/20** · **SWOT/FOFA** ·
**5W2H** · **RACI** · **PDCA/Kaizen** (ciclo de melhoria contínua).

---

# 📖 GLOSSÁRIO — Função Passo a Passo de Cada Indicador

> Para cada indicador: **1) o que coletar → 2) como calcular → 3) como interpretar → 4) como agir.**
> Cada acrônimo vem com o **nome completo entre parênteses**.

## ⭐ Indicador-Mestre
- **CPP (Custo por Ponto de Progresso).** 1) Colete o TCO-IA acumulado (tokens+assinatura+infra) e o % de progresso. 2) Divida `TCO ÷ %progresso`. 3) Leia a **tendência** semanal, não o valor isolado. 4) Se sobe → há retrabalho/interrupção/escopo inflando; ataque a causa até o CPP cair.
- **PSR (Project Score Rating, 0–5).** 1) Calcule 3 sub-notas 0–5: S_progresso (avanço vs. plano), S_interrupção (`5×(1−interr/teto)`), S_entrega (`PEUC/100×5`). 2) Pondere `0,40·S_prog + 0,25·S_int + 0,35·S_entrega`. 3) Enquadre na faixa (⭐ a ⭐⭐⭐⭐⭐). 4) Projetos < 2,5 vão para a pauta de intervenção.

## 🏦 BSC — Financeira
- **GTP (Gasto de Tokens por Projeto).** 1) Some tokens in/out por projeto (tag no Langfuse). 2) Multiplique pelos preços. 3) Compare ao orçamento. 4) Estourou → otimize prompt/modelo.
- **CAA (Custo de Assinatura Alocado).** 1) Pegue o custo mensal das assinaturas. 2) Rateie pela fração de uso do projeto. 3) Some ao TCO. 4) Reavalie planos caros/subutilizados.
- **TCO-IA (Custo Total de IA por Projeto).** 1) Some tokens + assinatura alocada + infra. 2) É o "custo total de IA" do projeto. 3) Compare entre projetos. 4) Base do CPP e do ROI.
- **CPPE (Custo por Prompt Efetivo).** 1) Custo total de tokens ÷ prompts que geraram entrega aceita. 2) Mostra o gasto por resultado real. 3) Alto → muitos prompts desperdiçados. 4) Melhore Prompt Yield.
- **ROI (Retorno sobre Investimento).** 1) Estime o valor gerado (economia/receita). 2) `(valor − custo) ÷ custo`. 3) > 100% = retorno positivo. 4) Decisão de continuar/escalar.
- **Payback (Prazo de Retorno do Investimento).** 1) Custo total ÷ ganho mensal. 2) Tempo de recuperação. 3) ≤ 6m é bom. 4) Longo → rever modelo de receita.
- **VPL/NPV (Valor Presente Líquido / Net Present Value).** 1) Liste os fluxos por período + taxa. 2) Traga a valor presente e subtraia o investimento. 3) > 0 = cria valor. 4) Compare projetos pelo VPL.
- **Burn Rate (Taxa de Queima de Caixa).** 1) Custo do período ÷ período. 2) Velocidade de queima de caixa. 3) Cresce sem receita → risco. 4) Controle antes de escalar.

## 👥 BSC — Cliente/Entrega
- **PEUC (Percentual de Entregáveis Úteis por Sessão).** 1) Marque cada sessão como "útil" se terminou sem falha. 2) `sessões_úteis ÷ total ×100`. 3) < 90% = usuário frustrado (churn). 4) Revise system prompt/modelo.
- **SF (Scope Fidelity — Fidelidade ao Escopo).** 1) Conte requisitos atendidos vs. planejados. 2) Divida. 3) < 90% = escopo escorregando. 4) Reforce Definition of Done.
- **TEP (Taxa de Entrega no Prazo).** 1) Entregas no prazo ÷ total. 2) Mede confiabilidade. 3) Baixo → replaneje sprints. 4) Ajuste cronograma/Gantt.
- **CV% (Cobertura de Validação).** 1) Saídas validadas ÷ usadas. 2) Deve ser 100% para itens críticos. 3) < 100% = risco de defeito em produção. 4) Institua QA/LLM-judge.
- **THR (Throughput — Vazão de Entregas).** 1) Conte entregas aceitas por período. 2) Volume de valor entregue. 3) Caindo → gargalo. 4) Investigue via Pareto.
- **VpT (Valor por Token).** 1) Valor gerado ÷ total de tokens. 2) Retorno por token. 3) Crescente = eficiência. 4) Otimize contexto.

## ⚙️ BSC — Processos Internos
- **PY (Prompt Yield — Rendimento de Prompt).** 1) Entregas aceitas ÷ total de prompts. 2) Quão direto se chega ao resultado. 3) < 40% = prompts fracos. 4) Melhore engenharia de prompt.
- **FPY (First-Pass Yield — Acerto na Primeira Tentativa).** 1) Ok no 1º prompt ÷ tarefas. 2) Acerto sem reprompt. 3) Baixo = retrabalho. 4) Few-shot/estrutura.
- **TRIA (Taxa de Retrabalho de IA).** 1) Prompts de correção ÷ total. 2) % de refação. 3) > 25% = alto. 4) Ataque a causa (RCA).
- **ITR (Intensidade de Tokens por Requisição).** 1) Σ tokens ÷ prompts. 2) "Custo por clique". 3) Subiu sem nova feature = contexto inflado. 4) RAG/sumarização.
- **IITA (Índice de Inflação de Tokens por Alucinação).** 1) Marque tokens de loops de correção/erro. 2) `desperdiçados ÷ total ×100`. 3) 40% = R$0,40 de cada R$1 jogado fora. 4) Modelo melhor/prompt rígido.
- **DI (Densidade de Interrupção).** 1) Conte interrupções ÷ horas de foco. 2) Frequência de quebras. 3) > 1,5/h = fluxo ruim. 4) Reduza fontes de interrupção.
- **HCI (Horário Crítico de Interrupção/Impacto).** 1) Agrupe falhas por hora do dia (BRT). 2) Pegue a hora de pico. 3) Diagnostica *quando* o projeto sofre. 4) Aja na janela (Tier/backoff/agenda).
- **MTTR (Mean Time To Recovery — Tempo Médio de Recuperação).** 1) Σ tempo de retomada ÷ nº interrupções. 2) Tempo médio de recuperação. 3) Alto = contexto caro de reconstruir. 4) Automação/checkpoints.
- **ITC (Índice de Troca de Contexto).** 1) Interrupções × penalidade de retomada. 2) Custo da multitarefa. 3) Minimize. 4) Blocos de foco.
- **LT/CT (Lead Time / Cycle Time — Tempo de Espera / Ciclo).** 1) Meça datas (solicitação→entrega; início→fim). 2) Subtraia. 3) Decrescente = fluxo saudável. 4) Remova gargalos.
- **VEL (Velocity — Velocidade de Sprint).** 1) Some entregas/pontos por sprint. 2) Ritmo de entrega. 3) Estável/crescente. 4) Base de previsão.
- **TA (Taxa de Automação).** 1) Tarefas via IA ÷ total. 2) % automatizado. 3) Crescente = escala. 4) Amplie automações.
- **TAL (Taxa de Alucinação).** 1) Saídas incorretas ÷ verificadas. 2) % de erro factual. 3) ≤ 5%. 4) Grounding/validação.
- **DD (Densidade de Defeitos).** 1) Defeitos ÷ entregas. 2) Qualidade técnica. 3) Decrescente. 4) Testes de regressão.
- **R O/I (Razão Output/Input — Saída sobre Entrada).** 1) Tokens out ÷ in. 2) Densidade de geração. 3) Baseline por tipo de tarefa. 4) Detecta prompt inflado.
- **TDT (Taxa de Desperdício de Tokens).** 1) Tokens desperdiçados ÷ total. 2) Fração sem valor. 3) ≤ 15%. 4) RAG/poda de histórico.

## 🌱 BSC — Aprendizado & Crescimento
- **HEIA (Horas Economizadas por IA).** 1) Estime horas manuais e meça as reais com IA. 2) Subtraia. 3) > 0 = ganho. 4) Prove o valor da IA.
- **LEV (Leverage — Fator de Aceleração).** 1) Horas manuais ÷ horas reais com IA. 2) Multiplicador. 3) ≥ 2,0x. 4) Só vira ROI com Focus alto.
- **FR (Focus Ratio — Índice de Foco).** 1) Horas focadas ÷ (focadas+interrompidas). 2) Saúde do foco. 3) ≥ 75%. 4) Corte interrupções.
- **CHE (Custo-Hora Efetivo Humano).** 1) Custo RH ÷ horas produtivas. 2) Custo da hora entregue. 3) Baseline. 4) Compare projetos.
- **RP (Reuso de Prompt).** 1) Prompts reaproveitados ÷ criados. 2) Maturidade. 3) ≥ 50%. 4) Biblioteca de prompts.
- **PHH / PgHH (Prompts por Hora-Homem / Progresso por Hora-Homem).** 1) Prompts (ou Δ%progresso) ÷ horas-homem. 2) Intensidade/avanço por hora. 3) Baseline/crescente. 4) Ajuste alocação.
- **IEET (Índice de Eficiência de Esforço por Token).** 1) Horas ÷ (tokens ÷ 1M). 2) HH por milhão de tokens. 3) Decrescente = arquitetura madura. 4) Automatize o que exige mão humana.

## 💸 Interrupção & Oportunidade
- **CI (Custo das Interrupções).** 1) Some (duração+retomada)×custo-hora + tokens de re-contexto×preço. 2) Perda direta. 3) Minimize. 4) Backoff/foco.
- **CDO (Custo do Desenvolvimento Ocioso).** 1) Minutos bloqueados × custo-hora/60. 2) R$ do time parado por cota. 3) Justifica upgrade de Tier. 4) Fila/roteamento.
- **COI (Custo de Oportunidade por Interrupção).** 1) (duração+retomada em h) × valor/hora-homem. 2) Valor NÃO entregue. 3) Some ao CI para o impacto real. 4) Priorize eliminar as 🔴.
- **COA (Custo de Oportunidade Acumulado).** 1) Some os COI do período. 2) Perda total. 3) Tendência. 4) Meta de redução.

## 📐 EVM (Earned Value Management — Gestão do Valor Agregado)
- **PV/EV/AC (Planned Value / Earned Value / Actual Cost).** 1) PV = %planejado×orçamento; EV = %real×orçamento; AC = custo real (TCO). 2) Três âncoras do valor agregado. 3) Comparação diz custo e prazo. 4) Base de CPI/SPI.
- **CPI (Cost Performance Index — Índice de Desempenho de Custo).** 1) EV ÷ AC. 2) Eficiência de custo. 3) ≥ 1,0 (abaixo = gastando mais que o entregue). 4) Corte desperdício.
- **SPI (Schedule Performance Index — Índice de Desempenho de Prazo).** 1) EV ÷ PV. 2) Eficiência de prazo. 3) ≥ 1,0 (abaixo = atrasado). 4) Replaneje.
- **EAC (Estimate At Completion — Estimativa na Conclusão).** 1) Orçamento ÷ CPI. 2) Projeção do custo final. 3) > orçamento = estouro previsto. 4) Aja antes.
- **CV (Cost Variance — Variação de Custo).** 1) EV − AC. 2) Desvio orçamentário. 3) ≥ 0. 4) Corrija se negativo.

## 💰 Investimento (BRL & USD)
- **VPL (Valor Presente Líquido).** 1) Monte o fluxo (invest. negativo no t0 + entradas). 2) Desconte à taxa e some. 3) > 0 = cria valor. 4) Ranqueie projetos.
- **TIR (Taxa Interna de Retorno).** 1) Ache a taxa que zera o VPL (bisseção). 2) É o "retorno %" do projeto. 3) Compare com a taxa mínima. 4) TIR > SELIC/EUA = vale investir.
- **ILL (Índice de Lucratividade Líquida — Profitability Index).** 1) VP das entradas ÷ |investimento|. 2) Quanto cada R$ investido retorna em VP. 3) > 1 = viável. 4) Ordene por ILL sob restrição de capital.
- **PBS / PBD (Payback Simples / Payback Descontado).** 1) Acumule o fluxo (simples e descontado). 2) Ache o período que cruza zero (interpolado). 3) Descontado > simples (dinheiro no tempo). 4) Menor = recupera antes.
- **Comparação SELIC / Juros EUA (dolarização).** 1) Converta o fluxo a US$ (câmbio) e desconte à taxa americana. 2) Compare TIR com SELIC (BR) e Fed (EUA). 3) TIR acima de ambas = supera o custo de oportunidade. 4) Decisão de alocação.

## 🪙 Fronteira
- **kTR / VRT (quilo-Token de Recuperação / Valor de Recuperação por kT).** 1) Some assinaturas fixas (CR) e divida por (tokens÷1000) = CRI. 2) Calcule FIA = 100/(100−IITA). 3) `VRT = (preço_API/1k + CRI) × FIA`. 4) É o custo real de recuperar cada 1.000 tokens — decrescente é o alvo.
- **VRT-5B (VRT em 5 Blocos + média).** 1) Multiplique VRT/kT por 0,05/0,10/0,25/0,50/1,0. 2) Veja o custo em 5 granularidades. 3) Tire a média. 4) 2ª ótica de consumo por projeto.
- **ICCA (Índice de Cobertura de Custo de IA).** 1) MRR do projeto ÷ (tokens × VRT/1000). 2) A receita cobre o custo recuperado? 3) > 3,0x saudável; < 1 = prejuízo oculto. 4) Reprecifique o plano.
- **IBMT (Índice de Burn Rate Marginal do Token).** 1) Burn Rate de IA ÷ Δ MRR. 2) Quanto queima por R$ de nova receita. 3) > 0,33 = risco; > 1 = insolvência por crescimento. 4) Corrija desperdício antes de crescer.

## ♻️ Lean Six Sigma
- **IDLS (Índice de Desperdício Lean por Sessão).** 1) Some tokens ponderados por erro (peso 1,5/2,0) + custo de tempo bloqueado. 2) Divida pelo custo total da sessão. 3) > 15% = processo enxameado de Muda. 4) Ataque o waste dominante (tabela de soluções).
- **8 Wastes (Muda — os 8 Desperdícios do Lean).** 1) Classifique cada log: Defeito (alucinação, ×2,0), Espera-Cota (429, ×1,5), Superprocessamento (prompt inflado, ×1,0), Latência (>3s, ×0,5). 2) Some tokens×peso por categoria. 3) O de maior soma é o **waste dominante** do projeto. 4) Aplique a contramedida-padrão (`solucoes_relatorios.md`) e meça o KPI-alvo.
- **IOLI (Índice de Ociosidade por Limite de IA).** 1) CDO ÷ custo total de dev ×100. 2) % do orçamento perdido esperando cota. 3) < 1%. 4) Upgrade de Tier / fila com backoff.
- **LE (Latência Excedente).** 1) `max(0; latência − 3s)`. 2) Espera além do aceitável. 3) Zero é o alvo. 4) Streaming/cache/modelo rápido.
- **ER (Exposição ao Risco).** 1) Σ(probabilidade × impacto R$) dos riscos abertos. 2) Impacto esperado. 3) Minimize. 4) Plano de mitigação (matriz de riscos).

## 🔬 RCA (Root Cause Analysis — Análise de Causa-Raiz)
- **Gargalo do projeto.** 1) Classifique cada prompt em 1 das 7 categorias. 2) Conte alucinações por categoria. 3) A categoria com mais alucinação é o **gargalo** que atrasa o projeto. 4) Aplique a solução da categoria.
- **Interseção do portfólio.** 1) Para cada projeto, ache o gargalo #1. 2) Conte em quantos projetos cada categoria é o #1. 3) A mais recorrente é o **gargalo comum a todos**. 4) Atacá-la tem o maior efeito sistêmico.

---

## 📚 Metodologias que sustentam o framework
- **BSC (Balanced Scorecard)** (Kaplan & Norton) — as 4 perspectivas.
- **Lean Six Sigma** — 8 wastes (Muda) + PDCA/Kaizen.
- **EVM (Earned Value Management)** (PMI) — valor agregado (CPI/SPI/EAC).
- **Administração Financeira** (Lawrence Gitman) — rateio (kTR/VRT), Burn Rate, liquidez.
- **Análise de Investimentos** — VPL, TIR, ILL, Payback (BRL e USD vs. SELIC/EUA).

> _Total: 70+ indicadores. "O que não é medido não pode ser gerenciado nem melhorado." — Kaplan & Norton._
