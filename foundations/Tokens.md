# Tokens — Consumo de IA por Projeto

> **Pré-requisito #1 dos KPIs financeiros.** Sem o consumo de tokens **com tag de projeto**,
> nenhum KPI financeiro por projeto funciona (Gasto de Tokens, Custo por Prompt, TCO-IA, CPP).
> Mantido pelo WatchDog. Alimenta [`KPIs.md`](KPIs.md).

---

## Como registrar

Uma linha por sessão/lote de consumo. Campos:

| Campo | Descrição |
|---|---|
| `Data` | AAAA-MM-DD |
| `Projeto` | **Tag do projeto** (igual à de `<projeto>.md`, `Interrupcoes.md`) |
| `Sprint` | Sprint corrente (ver [`projeto_main.md`](projeto_main.md)) |
| `Modelo` | Modelo usado (ex.: claude-opus-4-8, claude-sonnet-4-6) |
| `Tokens In` | Tokens de entrada (input) |
| `Tokens Out` | Tokens de saída (output) |
| `Preço In` | R$ por 1 token de input (ou ajuste a base) |
| `Preço Out` | R$ por 1 token de output |
| `Custo (R$)` | `tokens_in×preço_in + tokens_out×preço_out` |
| `Prompts` | Nº de prompts nessa sessão |
| `Prompts Aceitos` | Prompts que geraram entrega aceita |
| `Obs` | Contexto (re-prompt por interrupção? retrabalho?) |

> 💡 Marque na `Obs` quando o consumo for de **re-contexto por interrupção** — esse valor
> também entra no *Custo por Interrupção* em [`Interrupcoes.md`](Interrupcoes.md).

---

## Registro de Consumo

| Data | Projeto | Sprint | Modelo | Tokens In | Tokens Out | Preço In | Preço Out | Custo (R$) | Prompts | Aceitos | Obs |
|------|---------|--------|--------|-----------|------------|----------|-----------|------------|---------|---------|-----|
| 2026-06-27 | EXEMPLO-IA | S3 | claude-opus-4-8 | 500000 | 120000 | 0.00 | 0.00 | 0.00 | 50 | 18 | linha de exemplo |

> Substitua a linha de exemplo. Preencha os preços conforme sua assinatura/API
> (ver [`Assinatura_IA.md`](Assinatura_IA.md)).

---

## Consolidação por Projeto (para os KPIs)

| Projeto | Período | Σ Tokens In | Σ Tokens Out | Σ Custo (R$) | Σ Prompts | Σ Aceitos | Custo/Prompt Efetivo | % Progresso | CPP (R$/%) |
|---------|---------|-------------|--------------|--------------|-----------|-----------|----------------------|-------------|------------|
| EXEMPLO-IA | 2026-06 | 500000 | 120000 | 0.00 | 50 | 18 | 0.00 | — | — |

**Fórmulas:**
- Gasto de Tokens = `Σ Custo`
- Custo por Prompt Efetivo = `Σ Custo ÷ Σ Aceitos`
- TCO-IA = `Σ Custo + assinatura alocada` (ver [`Assinatura_IA.md`](Assinatura_IA.md))
- **CPP = `TCO-IA ÷ % progresso`** ← indicador-mestre ([`KPIs.md`](KPIs.md))

---

## Consolidação Global (todos os projetos)

| Projeto | Custo Mensal Tokens (R$) | % do Total | Usado p/ rateio de assinatura |
|---------|--------------------------|------------|-------------------------------|
| EXEMPLO-IA | 0.00 | 0% | ☑ |
| **TOTAL** | **0.00** | 100% | |

> O **% do Total** aqui é o critério de uso para ratear a assinatura entre projetos
> em [`Assinatura_IA.md`](Assinatura_IA.md).
