# Foundations — WatchDog de Projetos com IA

> **Framework "Painel BSC Dashboard — Gestão de Projetos (PM) IA"**
> **Autor:** Bruno Teixeira Penedo · **Criação:** 27/06/2026 às 18:00 · Todos os direitos reservados.

> Base de mensuração e monitoramento de projetos construídos com IA. Operada pela skill
> **`measuring-ai-projects`**, que age como **WatchDog**: a cada projeto informado, cria
> `foundations/<nome_do_projeto>.md` e passa a registrar alterações, soluções e resultados,
> medindo as entregas pelos indicadores em `KPIs.md`, as interrupções em `Interrupcoes.md`
> e os demais arquivos acessórios.
>
> **Princípio (Kaplan & Norton):** *"O que não é medido não pode ser gerenciado nem melhorado."*

---

## 📂 Índice de Arquivos

### Arquivos centrais (framework)
| Arquivo | Papel |
|---|---|
| [`KPIs.md`](KPIs.md) | **Todos os KPIs** das 4 categorias + Fronteira (VRT/kT, PSR), KPI-mestre (CPP) e correlações |
| [`KPIs_README.md`](KPIs_README.md) | **Guia prático**: o que cada KPI faz, com exemplos reais do pipeline |
| [`projeto_main.md`](projeto_main.md) | Cronologia, **gráfico de Gantt**, stages/etapas e **sprints** |
| [`BSC_Dashboard.md`](BSC_Dashboard.md) | Painel BSC (4 perspectivas) + ferramentas (BCG, GUT, SWOT, Pareto…) |

### Implementação executável
| Caminho | Papel |
|---|---|
| [`pipeline/`](pipeline/README.md) | ETL **Langfuse → SQLite** + queries dos KPIs + dados mock + scripts |
| `evidence/` | Dashboard **Evidence** (BI as Code) lendo o SQLite; `npm run dev` para visualizar |
| `pipeline/run_all.sh` | Esteira completa: sincroniza → publica `.db` → recompila o dashboard |

### Arquivos acessórios (dados que alimentam os KPIs)
| Arquivo | Registra | KPIs que alimenta |
|---|---|---|
| [`Tokens.md`](Tokens.md) | Consumo de tokens por projeto _(pré-requisito #1)_ | Gasto de Tokens, Custo/Prompt, TCO-IA, CPP |
| [`Interrupcoes.md`](Interrupcoes.md) | Interrupções detectadas + grau de impacto | Densidade, Focus Ratio, Custo de Interrupções |
| [`Assinatura_IA.md`](Assinatura_IA.md) | Planos de IA, descrição íntegra e custo mensal | Assinatura Alocada, TCO-IA |

### Por projeto (gerado pelo WatchDog)
| Arquivo | Papel |
|---|---|
| [`_TEMPLATE_projeto.md`](_TEMPLATE_projeto.md) | Template copiado a cada novo projeto |
| `<nome_do_projeto>.md` | **Fonte de verdade** do projeto: histórico, entregas, snapshot de KPIs |

---

## 🔄 Fluxo do WatchDog

```
1. ONBOARD   →  usuário informa um projeto (novo ou já iniciado)
                 → cria foundations/<nome_do_projeto>.md (a partir do _TEMPLATE_projeto.md)
                 → registra a tag em Tokens.md, Interrupcoes.md, Assinatura_IA.md

2. WATCH     →  a cada alteração / solução / resultado / interrupção:
                 → acrescenta no Histórico de <projeto>.md
                 → roteia o dado para o arquivo acessório certo

3. MEASURE   →  calcula os KPIs (KPIs.md) e reporta os 6 prioritários,
                 liderados pela TENDÊNCIA do Custo por Ponto de Progresso (CPP)
```

## 🔗 Como os arquivos conversam

```
Assinatura_IA.md ─┐
                  ├─► TCO-IA ──► Custo por Ponto de Progresso (CPP) ◄── % progresso
Tokens.md ────────┤                         │                          (projeto_main.md
Interrupcoes.md ──┘                         │                           + <projeto>.md)
   (tokens + horas perdidas)                └──► KPIs.md (dashboard, ROI) ──► <projeto>.md
```

O **CPP** (`custo total de IA ÷ % de progresso`) é o nó central: tokens, assinatura,
interrupções e cronograma desembocam todos nele.

---

## ▶️ Como usar

Peça à skill, por exemplo:
- *"Monitore o projeto **VPL-Alpha**"* → cria `foundations/VPL-Alpha.md` e inicia o registro.
- *"Registre o consumo de tokens de hoje do VPL-Alpha"* → atualiza `Tokens.md`.
- *"Meça os KPIs do VPL-Alpha"* → calcula e reporta os indicadores prioritários.

> ⚠️ **Pré-requisito #1:** sempre use a **mesma tag de projeto** em todos os arquivos.
> Sem ela, os KPIs financeiros por projeto não fecham.
