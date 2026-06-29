# Interrupções — Registro de Quebras de Contexto do Sistema de IA

> Log de **todas as interrupções** detectadas durante o trabalho com IA. Cada interrupção
> quebra o contexto e força **re-prompt** (re-explicar o estado ao modelo) → consome tokens e
> horas. Este arquivo alimenta os KPIs **Densidade de Interrupção**, **Focus Ratio** e
> **Custo das Interrupções** em [`KPIs.md`](KPIs.md).

---

## Como registrar

Adicione **uma linha por interrupção** na tabela abaixo. Campos:

| Campo | Descrição |
|---|---|
| `ID` | Identificador sequencial (INT-0001, INT-0002, …) |
| `Data` | AAAA-MM-DD |
| `Hora` | HH:MM (início da interrupção) |
| `Projeto` | Tag do projeto (mesma tag do billing de tokens) |
| `Sprint` | Sprint corrente (ver [`projeto_main.md`](projeto_main.md)) |
| `Tipo` | Categoria (ver tabela de tipos abaixo) |
| `Origem` | O que/quem causou (sistema, humano, externo, IA) |
| `Duração (min)` | Tempo até retomar o foco |
| `Tempo de Retomada (min)` | Tempo para reconstruir o contexto após voltar |
| `Tokens de Re-contexto` | Tokens gastos re-explicando o estado à IA |
| `Grau de Impacto` | Baixo / Médio / Alto / Crítico (ver escala) |
| `Descrição` | O que aconteceu |

---

## Escala de Grau de Impacto (direto no projeto)

| Grau | Critério | Efeito típico nos KPIs |
|---|---|---|
| 🟢 Baixo | < 5 min, sem perda de contexto | Quase nulo |
| 🟡 Médio | 5–20 min ou re-prompt leve | ↑ tokens, ↓ Focus Ratio |
| 🟠 Alto | 20–60 min ou re-explicar estado | ↑↑ tokens, ↓↓ Focus Ratio, atrasa sprint |
| 🔴 Crítico | > 60 min, perda de linha de raciocínio/escopo | Empurra o **CPP** para cima, risca o caminho crítico |

## Tipos de Interrupção

| Tipo | Exemplos |
|---|---|
| `Sistema` | Erro de API, timeout, rate limit, queda de serviço |
| `IA` | Resposta truncada, perda de contexto da janela, alucinação que exige refazer |
| `Humano` | Reunião não planejada, troca de prioridade, dúvida externa |
| `Externo` | Internet, energia, dependência de terceiros |
| `Processo` | Falta de spec, retrabalho, bloqueio por dependência |

---

## Registro de Interrupções

| ID | Data | Hora | Projeto | Sprint | Tipo | Origem | Duração (min) | Retomada (min) | Tokens Re-contexto | Grau | Descrição |
|----|------|------|---------|--------|------|--------|---------------|----------------|--------------------|------|-----------|
| INT-0001 | 2026-06-27 | 14:30 | EXEMPLO-IA | S3 | IA | Resposta truncada | 8 | 5 | 1200 | 🟡 Médio | Janela de contexto perdeu o estado; precisei re-explicar o escopo |

> Substitua a linha de exemplo pelos registros reais. Mantenha o histórico — a **tendência**
> de interrupções por sprint é o que importa.

---

## Consolidação para KPIs (atualizar por período)

| Métrica | Fórmula | Valor | Período |
|---|---|---|---|
| Total de interrupções | contagem de linhas | — | — |
| Densidade de Interrupção | `nº interrupções ÷ horas de foco` | — | Diária/Semanal |
| Tempo total perdido | `Σ(Duração + Retomada)` | — | Semanal |
| MTTR de Interrupção | `Σ(Tempo de Retomada) ÷ nº interrupções` | — | Semanal |
| Tokens de re-contexto | `Σ(Tokens de Re-contexto)` | — | Semanal |
| Custo das Interrupções | `Σ[(Duração+Retomada)/60 × custo_hora] + (tokens × preço_token)` | — | Semanal |
| **Custo de Oportunidade por Interrupção** | `(Duração+Retomada)/60 × valor gerado por hora-homem` | — | Por interrupção |
| **Custo de Oportunidade Acumulado** | `Σ custo de oportunidade de todas as interrupções` | — | Semanal |
| Focus Ratio | `horas focadas ÷ (focadas + interrompidas)` | — | Semanal |

> 💡 **Custo das Interrupções vs. Custo de Oportunidade:** o primeiro é o custo *direto*
> (horas pagas + tokens). O segundo é o *valor não entregue* — o que a hora teria produzido
> se aplicada ao projeto. Some os dois para o impacto real de cada quebra.

> ⚠️ Interrupções 🟠 Alto e 🔴 Crítico devem ser revisadas na **Retro** da sprint
> (ver [`projeto_main.md`](projeto_main.md)) para virar ação de melhoria.
