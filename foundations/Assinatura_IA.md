# Assinaturas de IA — Planos, Descrição e Custo Mensal

> Cadastro de **todas as assinaturas de IA** em uso. Alimenta o KPI **Custo de Assinatura
> Alocado** e o **TCO-IA por Projeto** em [`KPIs.md`](KPIs.md). O custo mensal aqui é rateado
> por projeto conforme o uso (`assinatura mensal × uso do projeto ÷ uso total`).

---

## Como cadastrar

Uma seção por assinatura. Campos obrigatórios:
- **IA assinada** (provedor/produto)
- **Nome do plano**
- **Descrição íntegra do que o plano oferece** (na íntegra, com detalhes)
- **Preço / custo mensal** (e moeda)
- Campos de apoio: seats/licenças, ciclo de cobrança, data de início, projetos atendidos.

---

## Assinatura 1 — [EXEMPLO]

| Campo | Valor |
|---|---|
| **IA assinada** | _ex.: Anthropic — Claude_ |
| **Nome do plano** | _ex.: Claude Pro / Max / Team / API_ |
| **Preço / custo mensal** | _ex.: R$ 0,00 / mês_ |
| **Moeda** | _BRL / USD_ |
| **Ciclo de cobrança** | _Mensal / Anual_ |
| **Nº de seats/licenças** | _ex.: 1_ |
| **Data de início** | _AAAA-MM-DD_ |
| **Projetos atendidos** | _tags de projeto que usam esta assinatura_ |

**Descrição do plano (na íntegra):**

> _Cole aqui a descrição completa e detalhada do que o plano oferece: limites de uso, modelos
> incluídos, número de mensagens/tokens, acesso a recursos (ex.: Projects, Claude Code, API,
> prioridade, janela de contexto), suporte, e quaisquer condições. Mantenha o texto na íntegra._

---

## Assinatura 2 — [adicionar]

| Campo | Valor |
|---|---|
| **IA assinada** | |
| **Nome do plano** | |
| **Preço / custo mensal** | |
| **Moeda** | |
| **Ciclo de cobrança** | |
| **Nº de seats/licenças** | |
| **Data de início** | |
| **Projetos atendidos** | |

**Descrição do plano (na íntegra):**

> _..._

---

## Consolidação — Custo Mensal Total de Assinaturas

| Assinatura | Plano | Seats | Custo Mensal | Moeda | Projetos |
|---|---|---|---|---|---|
| _ex.: Claude_ | _Pro_ | _1_ | _0,00_ | _BRL_ | _EXEMPLO-IA_ |
| **TOTAL** | | | **0,00** | | |

### Rateio por Projeto (para o TCO-IA)

`Custo de Assinatura Alocado = Custo Mensal Total × (uso do projeto ÷ uso total)`

| Projeto | Critério de uso | % de uso | Custo alocado |
|---|---|---|---|
| EXEMPLO-IA | _ex.: nº de prompts ou tokens_ | _40%_ | _0,00_ |

> O **% de uso** ideal vem da proporção de tokens/prompts do projeto sobre o total —
> os mesmos dados usados em [`KPIs.md`](KPIs.md). Sem a **tag de projeto** no consumo,
> use uma estimativa (ex.: nº de seats dedicados) e marque como aproximação.

---

> 🔄 **Atualização:** revise este arquivo quando um plano mudar de preço, escopo, ou quando
> uma assinatura for adicionada/cancelada. O custo aqui entra direto no **TCO-IA** e, por
> consequência, no **Custo por Ponto de Progresso (CPP)**.
