# 🗂️ BSC Dashboard Gerencial — Registro de Checkpoints

> **Log histórico dos Checkpoints Gerenciais** (toda sexta-feira). Enquanto
> [`BSC_Dashboard.md`](BSC_Dashboard.md) é o **painel vivo** (estado atual), este arquivo
> **acumula** cada checkpoint executado — para análise de tendência ao longo do tempo.
> Alimentado pela rotina cron `bsc-checkpoint-semanal`. **Nunca sobrescreva** — sempre acrescente.

---

## Como registrar

A cada sexta-feira (ou evento gerencial relevante), o WatchDog **acrescenta um bloco** abaixo,
copiando o modelo de entrada. Mantém-se também a tabela-resumo para leitura rápida da evolução.

---

## 📈 Resumo Evolutivo (uma linha por checkpoint)

| Data | Período | Projeto | Saúde | CPP (R$/%) | % Progr. | CPI | SPI | ROI | TCO-IA | Custo Oport. (sem) | Veredito |
|------|---------|---------|-------|-----------|----------|-----|-----|-----|--------|--------------------|----------|
| _AAAA-MM-DD_ | _sem NN_ | _tag_ | 🟢/🟡/🔴 | | | | | | | | Continuar/Ajustar/Escalar/Pausar |

---

## 🧾 Entradas de Checkpoint (histórico detalhado)

> Copie o modelo abaixo para cada novo checkpoint. Mais recente no topo.

### ▶️ Checkpoint — AAAA-MM-DD (sexta) — Período: semana NN

**Projeto(s):** _tag_ · **Stage/Sprint:** _..._ · **Saúde geral:** 🟢/🟡/🔴

**Indicadores-mestre**
| Indicador | Semana anterior | Esta semana | Δ | Status |
|---|---|---|---|---|
| CPP (R$/%) | | | | |
| % Progresso | | | | |
| CPI | | | | |
| SPI | | | | |
| ROI | | | | |
| TCO-IA acumulado | | | | |
| Custo de Oportunidade (semana) | | | | |

**Termômetro das 4 perspectivas**
- Financeira: __% 🟢/🟡/🔴
- Cliente/Entrega: __% 🟢/🟡/🔴
- Processos Internos: __% 🟢/🟡/🔴
- Aprendizado & Crescimento: __% 🟢/🟡/🔴

**Top alertas 🔴**
1. _..._
2. _..._

**Decisões / ações (responsável · prazo)**
- [ ] _..._

**Veredito:** _Continuar / Ajustar / Escalar / Pausar_ — _justificativa em 1 linha (base: CPP, CPI, SPI)._

**Eventos relevantes da semana** _(alterações, soluções, entregas — ref. `<projeto>.md`)_
- _..._

---

> 🔁 **Origem dos dados:** [`KPIs.md`](KPIs.md) (cálculos) · [`Tokens.md`](Tokens.md) (custo) ·
> [`Interrupcoes.md`](Interrupcoes.md) (foco/oportunidade) · [`projeto_main.md`](projeto_main.md) (progresso/cronograma).
> 🤖 **Automação:** rotina `bsc-checkpoint-semanal` — toda sexta-feira.
