# 💳 Planos de Assinatura de IA — Base de Rateio & Referência de Preços

> **Framework "Gestão de Projetos (PM) IA com Painel BSC e DashBoard"** · ©️ Bruno Teixeira Penedo — 2026. Todos os direitos reservados. E-mail: bpenedo@gmail.com

> ⚠️ **Preços aproximados** (referência jul/2026, base de conhecimento). Provedores cobram em **USD**;
> o valor em **R$** é indicativo (câmbio ≈ **R$ 5,40/US$**, ajustável em `USD_BRL` no `.env`).
> **Confirme sempre no site oficial** antes de decidir — planos e preços mudam com frequência.

---

## 🔗 Como isto alimenta o Framework
Estes valores abastecem duas variáveis do pipeline:
1. **`assinaturas_infra`** (tabela SQLite) — a base de rateio fixo mensal (**CR**). Coloque aqui o valor
   mensal do seu plano + ferramentas (n8n, servidores, etc.).
2. **`PRECO_API_POR_1K`** (`.env`) — o custo **marginal** por 1.000 tokens (só para uso **pay-per-use** de API).

## ✅ Validação do rateio para o SEU plano PRO (resposta à pergunta)
A álgebra do burn rate é: **`burn = (API_cost + CR) × FIA + CDO`** — ou seja, o custo fixo da assinatura
(**CR**) entra **integralmente** no burn, distribuído entre projetos **proporcionalmente ao uso de tokens**
(rateio estilo Gitman/m²). Isso é **matematicamente correto** (validado no triple-check).

**Porém, configure conforme o TIPO de plano:**
| Situação | `assinaturas_infra` (CR) | `PRECO_API_POR_1K` |
|---|---|---|
| **Plano PRO/flat** (ChatGPT Plus/Pro, Claude Pro/Max…) | valor mensal do plano | **≈ 0** (não há cobrança por token no flat) |
| **API pay-per-use** (paga por token) | só infra fixa (n8n, servidores) | preço por 1k tokens do provedor (tabela abaixo) |
| **Híbrido** (flat + estouros por API) | plano flat | preço marginal só do excedente |

> **Adequação:** para o seu **PRO**, a base de rateio (por tokens) é adequada — mas **coloque o valor do
> PRO em `assinaturas_infra`** e **`PRECO_API_POR_1K ≈ 0`**. Se deixar `0.025` (pay-per-use), você adiciona
> um custo-por-token fantasma que o flat não tem (super-contagem). No mais, o burn reflete 100% do plano.

---

## 📋 Planos de Assinatura (consumidor / mensal)

### 🟢 OpenAI — ChatGPT
| Plano | O que oferece | US$/mês | R$/mês (≈) |
|---|---|---|---|
| Free | GPT básico, limites | 0 | 0 |
| **Plus** | GPT-5/4o, mais uso, ferramentas | 20 | ~108 |
| **Pro** | uso quase ilimitado, modelos de raciocínio | 200 | ~1.080 |
| Team | por assento, workspace | ~30/assento | ~162 |
| Enterprise | SSO, controle, custom | sob consulta | — |

### 🟣 Anthropic — Claude
| Plano | O que oferece | US$/mês | R$/mês (≈) |
|---|---|---|---|
| Free | acesso básico | 0 | 0 |
| **Pro** | mais uso, Projects, Claude Code | 20 | ~108 |
| **Max 5×** | 5× o Pro | 100 | ~540 |
| **Max 20×** | 20× o Pro | 200 | ~1.080 |
| Team | por assento | ~30/assento | ~162 |

### 🔵 Google — Gemini
| Plano | O que oferece | US$/mês | R$/mês (≈) |
|---|---|---|---|
| Free | Gemini básico | 0 | 0 |
| **Google AI Pro** | Gemini avançado, 2 TB, apps | 20 | ~108 |
| **Google AI Ultra** | topo, mais limites, Veo | 250 | ~1.350 |

### 🟠 Perplexity
| Plano | O que oferece | US$/mês | R$/mês (≈) |
|---|---|---|---|
| Free | buscas limitadas | 0 | 0 |
| **Pro** | buscas Pro, modelos premium | 20 | ~108 |
| **Max** | uso intensivo, Labs | 200 | ~1.080 |
| Enterprise | equipe/segurança | sob consulta | — |

### ⚫ xAI — Grok
| Plano | O que oferece | US$/mês | R$/mês (≈) |
|---|---|---|---|
| **SuperGrok** | Grok avançado | ~30 | ~162 |
| X Premium+ | inclui Grok + X | ~40 | ~216 |
| SuperGrok Heavy | topo | ~300 | ~1.620 |

### 🟡 Mistral — Le Chat
| Plano | O que oferece | US$/mês | R$/mês (≈) |
|---|---|---|---|
| Free | acesso básico | 0 | 0 |
| **Pro** | mais uso, modelos premium | ~15 | ~81 |
| Team/Enterprise | equipe | sob consulta | — |

### 🔴 DeepSeek · 🌙 Kimi (Moonshot) · 🐉 Qwen (Alibaba)
> **Sem assinatura mensal “ocidental” de consumidor** — o app/chat é **gratuito**; a monetização é via **API pay-per-use** (ver tabela de API). Excelentes para custo baixo.
| Provedor | Chat consumidor | Modelo de cobrança |
|---|---|---|
| **DeepSeek** | gratuito (app/web) | API por token (muito barata) |
| **Kimi (Moonshot AI)** | gratuito (kimi.com) | API por token (RMB) |
| **Qwen (Alibaba)** | gratuito (Qwen Chat) | API via Alibaba Cloud Model Studio |

---

## 🏛️ IOF & Custo Total Mensal (com imposto)
As assinaturas são cobradas em **US$ no exterior** → incide **IOF sobre compras internacionais com cartão**.
> **Alíquota usada: IOF ≈ 3,5%** (referência 2026 — **sujeita a alteração**; houve mudanças por decreto em 2025.
> Verifique a alíquota vigente). Fórmula: **`Total = US$ × câmbio × (1 + IOF)`** = `US$ × 5,40 × 1,035`.

| Provedor | Plano | US$/mês | R$ base (×5,40) | IOF 3,5% | **Total R$/mês c/ IOF** |
|---|---|---:|---:|---:|---:|
| OpenAI | ChatGPT Plus | 20 | 108,00 | 3,78 | **111,78** |
| OpenAI | ChatGPT Pro | 200 | 1.080,00 | 37,80 | **1.117,80** |
| OpenAI | ChatGPT Team (assento) | 30 | 162,00 | 5,67 | **167,67** |
| Anthropic | Claude Pro | 20 | 108,00 | 3,78 | **111,78** |
| Anthropic | Claude Max 5× | 100 | 540,00 | 18,90 | **558,90** |
| Anthropic | Claude Max 20× | 200 | 1.080,00 | 37,80 | **1.117,80** |
| Anthropic | Claude Team (assento) | 30 | 162,00 | 5,67 | **167,67** |
| Google | Google AI Pro | 20 | 108,00 | 3,78 | **111,78** |
| Google | Google AI Ultra | 250 | 1.350,00 | 47,25 | **1.397,25** |
| Perplexity | Pro | 20 | 108,00 | 3,78 | **111,78** |
| Perplexity | Max | 200 | 1.080,00 | 37,80 | **1.117,80** |
| xAI | SuperGrok | 30 | 162,00 | 5,67 | **167,67** |
| xAI | X Premium+ | 40 | 216,00 | 7,56 | **223,56** |
| xAI | SuperGrok Heavy | 300 | 1.620,00 | 56,70 | **1.676,70** |
| Mistral | Le Chat Pro | 15 | 81,00 | 2,84 | **83,84** |
| DeepSeek / Kimi / Qwen | Chat consumidor | 0 | 0,00 | 0,00 | **0,00** (grátis; API à parte) |

> 💡 O **IOF também incide sobre o gasto de API pay-per-use** (também operação internacional em US$):
> `custo_API_total = tokens × preço × câmbio × (1 + IOF)`. No pipeline, embuta o IOF no `PRECO_API_POR_1K`
> (ex.: `0.025 × 1.035 ≈ 0.0259`) ou no rateio de `assinaturas_infra` já com o total c/ IOF.

## 🔧 API pay-per-use — preço por **1 milhão de tokens** (input / output)
> Alimenta `PRECO_API_POR_1K`. Conversão: `US$/1M ÷ 1000 = US$/1k`; `× 5,40 = R$/1k`.

| Provedor / Modelo | US$ in /1M | US$ out /1M | R$/1k (in, ≈) |
|---|---|---|---|
| OpenAI GPT-4o | 2,50 | 10,00 | ~0,0135 |
| OpenAI GPT-4o-mini | 0,15 | 0,60 | ~0,0008 |
| Anthropic Claude Sonnet | 3,00 | 15,00 | ~0,0162 |
| Anthropic Claude Haiku | 0,80 | 4,00 | ~0,0043 |
| Anthropic Claude Opus | 15,00 | 75,00 | ~0,081 |
| Google Gemini 2.5 Flash | 0,15 | 0,60 | ~0,0008 |
| Google Gemini 2.5 Pro | 1,25 | 10,00 | ~0,0068 |
| **DeepSeek-V3** | 0,27 | 1,10 | ~0,0015 |
| **DeepSeek-R1** | 0,55 | 2,19 | ~0,0030 |
| **Kimi (Moonshot k2)** | ~0,15 | ~2,50 | ~0,0008 |
| **Qwen-Plus** | ~0,40 | ~1,20 | ~0,0022 |
| **Qwen-Turbo** | ~0,05 | ~0,20 | ~0,0003 |
| Perplexity Sonar | ~1,00 | ~1,00 | ~0,0054 + taxa de busca |
| xAI Grok | ~2,00 | ~10,00 | ~0,0108 |
| Mistral Large | ~2,00 | ~6,00 | ~0,0108 |

> Para o framework, o `PRECO_API_POR_1K` costuma usar uma **mistura in+out** (ex.: 3:1). Ex.: GPT-4o
> blended ≈ `(2,50×0,75 + 10×0,25)/1000 × 5,40 ≈ R$ 0,024/1k` — próximo do default `0.025`.

---

## 🧮 Como preencher no pipeline
```sql
-- exemplo: plano PRO flat + ferramentas fixas (base de rateio CR)
INSERT OR REPLACE INTO assinaturas_infra VALUES ('ChatGPT Pro', 1080.00);   -- R$/mês
INSERT OR REPLACE INTO assinaturas_infra VALUES ('n8n Cloud', 250.00);
-- e no .env, para plano FLAT: PRECO_API_POR_1K=0
```
> Depois rode `./run_all.sh` — VRT, Burn Rate, ICCA e IBMT passam a refletir o **custo real** do seu plano.

---
> _Preços de referência jul/2026 — **verifique os sites oficiais**. Relacionado: [`Assinatura_IA.md`](Assinatura_IA.md), [`KPIs.md`](KPIs.md)._
