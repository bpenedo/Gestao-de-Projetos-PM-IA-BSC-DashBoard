# 📈 Pitch Deck — TEMPLATE PADRÃO (Standard)

> **Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard** · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
>
> Padrão canônico de geração de pitch deck. O gerador `pipeline/gerar_pitchdeck.py` produz, para cada
> projeto **elegível**, os arquivos `pitchdeck_<nome_do_projeto>_DDMMAAAA.md` e `.pdf` (LaTeX/tectonic)
> nesta pasta, seguindo EXATAMENTE a estrutura abaixo (modelo do `pitch sample.jpg`).

---

## ✅ Critério de elegibilidade
O pitch deck só é gerado se o projeto tiver **VPL > 0 e ILL (PI) > 1 em BRL e em USD**
(ILL é adimensional → idêntico nas duas moedas; exige-se `vpl > 0` **e** `vpl_usd > 0`).

## 🗂️ Nomenclatura
`pitchdeck_<nome_do_projeto>_DDMMAAAA.pdf` (+ `.md`). Ex.: `pitchdeck_project_a_29062026.pdf`.

---

## 🧱 Layout (1 página A4)

```
┌──────────────────────────────────────────────────────────────┐
│  [BANNER NAVY]   <NOME DO PROJETO>                             │
│                  EXECUTIVE SUMMARY – PITCH DECK                │
├───────────────────────┬──────────────────────────────────────┤
│  SIDEBAR NAVY (33%)    │  COLUNA PRINCIPAL (63%)               │
│                        │                                       │
│  FINANCIAL INFORMATION │  > PITCH                              │
│   Stage / VPL BRL/USD  │  ? PROBLEMA / OPORTUNIDADE            │
│   TIR / ILL            │  * SOLUCAO / PRODUTO                  │
│   Payback desc BRL/USD │  $ MODELO DE NEGOCIO                  │
│   SELIC / EUA          │  # MERCADO                            │
│                        │  = CONCORRENTES                       │
│  KPIs (BSC)            │  + VANTAGEM COMPETITIVA               │
│   PSR / CPP / Burn     │  > EXECUCAO / GO-TO-MARKET            │
│   PEUC / ICCA          │  @ TRACAO                             │
│                        │   (espaçamento generoso entre tópicos)│
│  USE OF FUNDS          │                                       │
│   40/25/20/15 %        │                                       │
│                        │                                       │
│  TEAM                  │                                       │
├───────────────────────┴──────────────────────────────────────┤
│        [BANNER NAVY centralizado] FINANCIALS – Fluxo de Caixa  │
│        Descontado                                              │
│        (tabela CENTRALIZADA) Periodo | Fluxo | Fluxo desc. |   │
│        Acum. desc.  + números                                 │
│        (rodapé CENTRALIZADO) Framework BSC PM IA ©Bruno        │
│        Teixeira Penedo – 2026.                                 │
└──────────────────────────────────────────────────────────────┘
```

## 📋 Campos — o que cada bloco contém

### Sidebar (esquerda, navy, texto branco)
| Bloco | Conteúdo | Fonte de dados |
|---|---|---|
| FINANCIAL INFORMATION | Stage, VPL (BRL), VPL (USD), TIR, ILL, Payback descontado (BRL/USD), SELIC, juros EUA | `vpl_resultado` |
| KPIs (BSC) | PSR, CPP, Burn Rate, PEUC, ICCA | `kpis_bsc_ia` |
| USE OF FUNDS | 40% Produto/IA · 25% Go-to-Market · 20% Operação · 15% Reserva | template (editável) |
| TEAM | Fundadores/PM | template (editável) |

### Coluna principal (direita) — 9 tópicos
| Tópico | Descrição |
|---|---|
| **PITCH** | Visão/missão da iniciativa de IA |
| **PROBLEMA / OPORTUNIDADE** | Dor do mercado-alvo |
| **SOLUCAO / PRODUTO** | Como o projeto resolve (KPIs do framework) |
| **MODELO DE NEGOCIO** | Como gera receita/margem |
| **MERCADO** | Tamanho e perfil do mercado |
| **CONCORRENTES** | Concorrentes e riscos externos |
| **VANTAGEM COMPETITIVA** | Diferenciais (kTR, PSR, RCA…) |
| **EXECUCAO / GO-TO-MARKET** | Plano de execução e milestones |
| **TRACAO** | Resultados/KPIs alcançados |

### Rodapé
- Banner **FINANCIALS – Fluxo de Caixa Descontado** (centralizado).
- Tabela **centralizada**: `Período | Fluxo | Fluxo desc. | Acum. desc.` (de `vpl_fluxo`).
- Linha final **centralizada**: `Framework BSC PM IA ©Bruno Penedo – 2026.`

## ⚙️ Especificações de formatação (LaTeX)
- A4, margens 1 cm · fonte `extarticle` 10pt · cor navy `#1F3A5F`.
- Espaçamento entre tópicos da direita: **`\\[12pt]`** (leitura confortável — "três ENTER").
- Sidebar: `\parbox` altura `0.62\textheight` (mantém 1 página).
- Tabela e rodapé: ambientes `center`.
- Unicode normalizado (—, ·, →, aspas) para evitar glifos ausentes.

## ▶️ Como gerar
```bash
cd foundations/pipeline
python3 carregar_fluxo.py SEU_FLUXO.csv   # ou --demo
python3 gerar_pitchdeck.py                # todos os elegíveis
python3 gerar_pitchdeck.py "Nome do Projeto"   # um específico
```
Requer **tectonic** (compilador LaTeX). Os campos qualitativos vêm como template editável —
ajuste-os por projeto antes de apresentar a investidores.
