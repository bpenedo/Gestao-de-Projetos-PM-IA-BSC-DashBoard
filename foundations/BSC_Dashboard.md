# 🧭 Painel BSC — Balanced Scorecard de Projetos com IA

> **Framework "Gestão de Projetos (PM) IA com Painel BSC e DashBoard"** · ©️ Bruno Teixeira Penedo — 2026. Todos os direitos reservados. E-mail: bpenedo@gmail.com

> **Visão gerencial final.** Consolida os KPIs das fundações nas **4 perspectivas de Kaplan &
> Norton**. Gerado/atualizado no **Checkpoint Gerencial de toda sexta-feira** (agendado via cron).
> Fonte dos dados: [`KPIs.md`](KPIs.md) · [`Tokens.md`](Tokens.md) · [`Interrupcoes.md`](Interrupcoes.md) · [`Assinatura_IA.md`](Assinatura_IA.md) · [`projeto_main.md`](projeto_main.md)
>
> *"O que não é medido não pode ser gerenciado nem melhorado."* — Kaplan & Norton

**Legenda de status:** 🟢 No alvo · 🟡 Atenção · 🔴 Crítico · ⚪ Sem dado · ▲ melhora · ▼ piora · ▬ estável

---

## 🗓️ Cabeçalho do Checkpoint

| Campo | Valor |
|---|---|
| **Data do checkpoint** | _AAAA-MM-DD (sexta)_ |
| **Período coberto** | _semana NN_ |
| **Projeto(s)** | _tag(s)_ |
| **Stage / Sprint atual** | _ver projeto_main.md_ |
| **Saúde geral** | 🟢 / 🟡 / 🔴 |

---

## 📊 Visão de Topo — Indicador-Mestre

```
┌──────────────────────────────────────────────────────────────────────┐
│   CUSTO POR PONTO DE PROGRESSO (CPP)          % PROGRESSO              │
│                                                                        │
│      R$  ____ /%        [ ▲ ▼ ▬ ]            [▓▓▓▓▓▓░░░░] __%          │
│      meta: decrescente                        meta: conforme cronograma│
│                                                                        │
│   CPI ____ (≥1,0)   SPI ____ (≥1,0)   ROI ____% (>100%)   Saúde: 🟢/🟡/🔴│
│                                                                        │
│   PSR ⭐ _,_ /5     VRT/kT R$ _,____     IBMT __% (<33%)   IDLS __%(<15)│
└──────────────────────────────────────────────────────────────────────┘
```

---

## 🎯 As 4 Perspectivas do BSC

```
                          ┌─────────────────────────┐
                          │   1. FINANCEIRA          │
                          │   "Como entregamos valor │
                          │    aos stakeholders?"    │
                          └────────────┬────────────┘
                                       │
        ┌──────────────────────────────┼──────────────────────────────┐
        │                              │                               │
┌───────┴────────┐          ┌──────────┴─────────┐          ┌──────────┴────────┐
│ 4. APRENDIZADO │◄────────►│   VISÃO &          │◄────────►│ 2. CLIENTE        │
│  & CRESCIMENTO │          │   ESTRATÉGIA       │          │  (Entrega/Valor)  │
└───────┬────────┘          └──────────┬─────────┘          └──────────┬────────┘
        │                              │                               │
        └──────────────────────────────┼──────────────────────────────┘
                                       │
                          ┌────────────┴────────────┐
                          │ 3. PROCESSOS INTERNOS    │
                          │  (Execução com IA)       │
                          └─────────────────────────┘
```

### 1️⃣ Perspectiva FINANCEIRA
> *Custo, retorno e eficiência de capital.*

| KPI | Valor | Meta | Status | Tend. |
|---|---|---|---|---|
| Custo por Ponto de Progresso (CPP) | | decrescente | ⚪ | ▬ |
| ROI | | > 100% | ⚪ | ▬ |
| TCO-IA | | no orçamento | ⚪ | ▬ |
| CPI (Índice de Custo) | | ≥ 1,0 | ⚪ | ▬ |
| Burn Rate | | dentro do plano | ⚪ | ▬ |
| Payback / VPL | | ≤ 6m / > 0 | ⚪ | ▬ |
| Custo de Oportunidade Acumulado | | minimizar | ⚪ | ▬ |
| VRT/kT (recuperação por 1k tokens) | | decrescente | ⚪ | ▬ |
| ICCA (cobertura de custo) | | > 3,0x | ⚪ | ▬ |
| IBMT (burn rate marginal) | | < 33% | ⚪ | ▬ |
| **PSR — Score do Projeto (0–5)** | | ≥ 3,5 ⭐ | ⚪ | ▬ |

### 2️⃣ Perspectiva CLIENTE / ENTREGA
> *Valor percebido e cumprimento do prometido.*

| KPI | Valor | Meta | Status | Tend. |
|---|---|---|---|---|
| Scope Fidelity | | ≥ 90% | ⚪ | ▬ |
| Taxa de Entrega no Prazo | | ≥ 90% | ⚪ | ▬ |
| Cobertura de Validação | | 100% | ⚪ | ▬ |
| Throughput (entregas/sem) | | crescente | ⚪ | ▬ |
| Valor por Token | | crescente | ⚪ | ▬ |

### 3️⃣ Perspectiva PROCESSOS INTERNOS
> *Eficiência da execução com IA.*

| KPI | Valor | Meta | Status | Tend. |
|---|---|---|---|---|
| Prompt Yield | | ≥ 40% | ⚪ | ▬ |
| First-Pass Yield | | ≥ 30% | ⚪ | ▬ |
| Taxa de Retrabalho de IA | | ≤ 25% | ⚪ | ▬ |
| Tokens por Entrega | | decrescente | ⚪ | ▬ |
| Taxa de Desperdício de Tokens | | ≤ 15% | ⚪ | ▬ |
| Densidade de Interrupção | | ≤ 1,5/h | ⚪ | ▬ |
| MTTR de Interrupção | | decrescente | ⚪ | ▬ |
| Cycle Time / Lead Time | | decrescente | ⚪ | ▬ |
| Taxa de Alucinação | | ≤ 5% | ⚪ | ▬ |

### 4️⃣ Perspectiva APRENDIZADO & CRESCIMENTO
> *Capital humano, produtividade e maturidade.*

| KPI | Valor | Meta | Status | Tend. |
|---|---|---|---|---|
| Leverage (Aceleração) | | ≥ 2,0x | ⚪ | ▬ |
| Horas Economizadas por IA | | > 0 | ⚪ | ▬ |
| Focus Ratio | | ≥ 75% | ⚪ | ▬ |
| Reuso de Prompt | | ≥ 50% | ⚪ | ▬ |
| Taxa de Automação | | crescente | ⚪ | ▬ |
| Velocity | | estável/crescente | ⚪ | ▬ |

---

## 🩺 Simulação de Checkpoint Gerencial (toda sexta)

> Roteiro que o WatchDog executa no checkpoint semanal. Preencha cada bloco com os dados da semana.

### A. Termômetro semanal
```
Financeira      [▓▓▓▓▓▓▓░░░]  __%   🟢/🟡/🔴
Cliente         [▓▓▓▓▓▓▓░░░]  __%   🟢/🟡/🔴
Processos       [▓▓▓▓▓▓▓░░░]  __%   🟢/🟡/🔴
Aprendizado     [▓▓▓▓▓▓▓░░░]  __%   🟢/🟡/🔴
─────────────────────────────────────────
SAÚDE GERAL DO PORTFÓLIO:           🟢/🟡/🔴
```

### B. Variação vs. semana anterior
| Indicador-mestre | Semana anterior | Esta semana | Δ | Veredito |
|---|---|---|---|---|
| CPP (R$/%) | | | | |
| % Progresso | | | | |
| TCO-IA acumulado | | | | |
| Custo de Oportunidade (semana) | | | | |

### C. Top 3 alertas 🔴 da semana
1. _..._
2. _..._
3. _..._

### D. Decisões gerenciais recomendadas
- [ ] _Ação corretiva 1 (responsável / prazo)_
- [ ] _Ação corretiva 2_
- [ ] _Ajuste de cronograma/escopo, se SPI < 1,0_

### E. Veredito do checkpoint
> **Continuar / Ajustar / Escalar / Pausar** — justificativa em 1 linha baseada em CPP, CPI e SPI.

---

## 🧰 Ferramentas Administrativas (visão estratégica do portfólio)

> Complementam o BSC com lentes clássicas de gestão, aplicadas ao **portfólio de projetos de IA**.

### 📦 Matriz BCG — Portfólio de Projetos
> Eixo X = **Eficiência/Retorno** (ROI ou CPP invertido) · Eixo Y = **Crescimento/Potencial** do projeto.

```
        ALTO  ┌───────────────────────────┬───────────────────────────┐
              │  ❓ QUESTION MARK          │  ⭐ STAR                  │
   C          │  (alto potencial,          │  (alto potencial,         │
   R          │   baixo ROI ainda)         │   alto ROI)               │
   E          │  → investir ou matar       │  → investir e escalar     │
   S          │  ex.: _projeto_            │  ex.: _projeto_           │
   C   ───────┼───────────────────────────┼───────────────────────────┤
   I          │  🐕 DOG                    │  🐄 CASH COW              │
   M          │  (baixo potencial,         │  (baixo crescimento,      │
   E          │   baixo ROI)               │   alto ROI estável)       │
   N          │  → descontinuar/arquivar   │  → manter, ordenhar caixa │
   T          │  ex.: _projeto_            │  ex.: _projeto_           │
   O   BAIXO  └───────────────────────────┴───────────────────────────┘
              BAIXO ◄──── EFICIÊNCIA / RETORNO (ROI, CPP↓) ────► ALTO
```
| Projeto | ROI | Crescimento | Quadrante | Ação |
|---|---|---|---|---|
| _tag_ | | | ⭐/🐄/❓/🐕 | |

### 🎯 Matriz GUT — Priorização (Gravidade × Urgência × Tendência)
> Score = G × U × T (escala 1–5). Maior score = atacar primeiro.

| Item / Alerta | G | U | T | **GUT** | Prioridade |
|---|---|---|---|---|---|
| _ex.: interrupções acima da meta_ | | | | | |

### 🗂️ Matriz de Eisenhower — Foco gerencial
```
              URGENTE                 NÃO URGENTE
        ┌──────────────────────┬──────────────────────┐
IMPORT. │ FAZER AGORA          │ AGENDAR              │
        │ (crises, bloqueios)  │ (planejar, melhorar) │
        ├──────────────────────┼──────────────────────┤
NÃO IMP.│ DELEGAR/AUTOMATIZAR  │ ELIMINAR             │
        │ (tarefas repetíveis) │ (desperdício)        │
        └──────────────────────┴──────────────────────┘
```

### 🔺 Matriz de Riscos (Probabilidade × Impacto)
```
   IMPACTO →   Baixo    Médio    Alto
   Alta P.  │   🟡   │   🟠   │   🔴   │
   Média P. │   🟢   │   🟡   │   🟠   │
   Baixa P. │   🟢   │   🟢   │   🟡   │
```
| Risco | Prob. | Impacto (R$) | Exposição | Mitigação | Dono |
|---|---|---|---|---|---|
| _..._ | | | | | |

### 📉 Análise de Pareto (80/20)
> Onde estão concentrados os custos/desperdícios? Atacar os poucos vitais.

| Causa (de custo/retrabalho/interrupção) | % do impacto | % acumulado |
|---|---|---|
| _ex.: re-contexto por interrupção_ | | |
| _ex.: retrabalho de prompt_ | | |

### 🧱 SWOT / FOFA (do portfólio de IA)
| ✅ Forças | ⚠️ Fraquezas |
|---|---|
| _..._ | _..._ |
| 🚀 **Oportunidades** | 🛑 **Ameaças** |
| _..._ | _..._ |

### 🛠️ 5W2H — Plano de Ação (decisões do checkpoint)
| What | Why | Who | When | Where | How | How much |
|---|---|---|---|---|---|---|
| _ação_ | _motivo_ | _dono_ | _prazo_ | _onde_ | _como_ | _custo_ |

### 👥 RACI — Responsabilidades
| Atividade | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| _..._ | | | | |

### 🔄 Ciclo PDCA (melhoria contínua do checkpoint)
`Plan` (metas da semana) → `Do` (executar) → `Check` (este BSC) → `Act` (ações 5W2H) → repete.

---

## 🤖 Automação

Este painel é regenerado **toda sexta-feira** pelo Checkpoint Gerencial agendado via cron
(rotina `bsc-checkpoint-semanal`). A rotina lê as fundações, recalcula os KPIs, atualiza este
arquivo e produz o veredito gerencial da semana.
