# 🛠️ solucoes_relatorios.md — Padrão de Conclusão de Relatórios (Melhoria Contínua)

> **Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard** · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
>
> **STANDARD obrigatório:** todo relatório de projeto (página individual no Evidence) **deve** terminar
> com um **Bottom-Line / Rodapé conclusivo** contendo: (1) dissertação de **Wastes**, (2) dissertação
> de **Alucinação de Prompts por categoria**, e (3) a **Solução Definitiva** de melhoria contínua.
> Este arquivo é a **fonte canônica** das soluções — aplique a TODO e QUALQUER projeto futuro.

---

## 1. Princípio de Melhoria Contínua (PDCA / Kaizen)

Cada desperdício e cada alucinação detectados entram num ciclo **PDCA**:
- **Plan** — identificar o waste/categoria dominante (o relatório já aponta via RCA).
- **Do** — aplicar a contramedida-padrão da tabela abaixo.
- **Check** — medir o KPI correspondente na semana seguinte (IITA, IDLS, IOLI, ITR, latência).
- **Act** — padronizar o que funcionou (atualizar o system prompt / pipeline) e repetir.

> Meta-mãe: **CPP decrescente** semana a semana. Todo waste/alucinação reduzido empurra o CPP para baixo.

---

## 2. Solução Definitiva por WASTE (Lean Six Sigma)

| Waste (taxonomia) | Causa-raiz típica | Solução definitiva | KPI de controle (meta) |
|---|---|---|---|
| **Defeito — Alucinação/Retrabalho** (peso 2,0×) | Saída não-determinística, prompt sem contrato | System prompt rígido + **saída estruturada (JSON schema)** + **validação automática (LLM-as-judge)** + testes de regressão de prompt | IITA **< 10%** |
| **Espera — Cota/429** (peso 1,5×) | Rajada de requisições acima do TPM/RPD | **Fila com backoff exponencial** (Temporal/n8n) + **roteamento de fallback** por cota + upgrade de Tier | IOLI **< 1%** |
| **Superprocessamento — Prompt Inflado** (peso 1,0×) | Contexto bruto excessivo (scrapers/histórico) | **RAG/embeddings** + **sumarização de contexto** + poda de histórico (janela deslizante) | ITR **estável/↓** |
| **Espera — Latência Alta (>3s)** (peso 0,5×) | Modelo pesado para tarefa simples | **Streaming (TTFT)** + modelo rápido para tarefas triviais + **cache** de respostas | Latência **< 3s** |

---

## 3. Solução Definitiva por ALUCINAÇÃO de PROMPT (taxonomia)

| Categoria de prompt | Por que alucina | Solução definitiva (redução) | Reforço de melhoria contínua |
|---|---|---|---|
| **Conversa/Aberto** | Entrada livre, sem escopo | **Converter aberto em estruturado**: system prompt restritivo + few-shot + guardrails de escopo | Catalogar intenções recorrentes e criar templates |
| **Geração de Código** | Bibliotecas/APIs inventadas | **Few-shot com exemplos válidos** + exigir testes + **validação de sintaxe/execução** + RAG das docs da lib | Banco de snippets aprovados reutilizáveis |
| **Raciocínio/Análise** | Saltos lógicos não verificados | **Decomposição em etapas** + chain-of-thought estruturado + verificação por etapas + self-consistency | Checklists de raciocínio por domínio |
| **Extração de Dados** | Campos ambíguos | **JSON mode / schema** + regex de validação + exemplos de entrada→saída | Dicionário de campos canônicos |
| **RAG/Busca** | Recuperação fraca / sem grounding | Melhorar **retrieval (re-rank)** + **citar fontes** + grounding obrigatório | Avaliar recall do retriever semanalmente |
| **Transformação/Formato** | Formato de saída solto | **Templates fixos** + exemplos de saída + JSON mode | Versionar os templates de saída |
| **Sumarização** | Perda/invenção de fato | Limites de tamanho + **instruções de fidelidade** + verificação factual | Amostragem de QA factual |

---

## 4. Modelo do Bottom-Line (como cada relatório deve concluir)

Todo relatório de projeto termina com:

> **📌 Bottom-Line — Diagnóstico Conclusivo**
>
> **a) Wastes:** "O desperdício dominante deste projeto é **`<waste dominante>`**. [dissertação: o que isso
> custa em tokens/caixa e por que ocorre]. **Solução definitiva:** [contramedida da seção 2] →
> acompanhar **`<KPI>`** rumo à meta."
>
> **b) Alucinação de Prompts:** "O tipo de prompt que mais atrasa é **`<categoria gargalo>`**
> (`<taxa>`% de alucinação). [dissertação: por que essa categoria falha aqui]. **Solução definitiva:**
> [contramedida da seção 3]."
>
> **c) Melhoria Contínua (PDCA):** Plan → Do → Check → Act, medindo o KPI na semana seguinte até a meta;
> padronizar o que funcionou no system prompt/pipeline. **Norte: CPP decrescente.**

---

## 5. Aplicação automática

- A página individual de cada projeto (`evidence/pages/projetos/[projeto].md`) implementa este rodapé,
  **lendo dinamicamente** o waste dominante e o prompt-gargalo do projeto e referenciando as soluções acima.
- Para **qualquer projeto novo**, nada precisa ser reescrito: ao aparecer no pipeline, o relatório já
  conclui com o Bottom-Line padrão baseado nos dados dele.
- Revise este arquivo quando uma nova categoria de waste ou de prompt for incorporada ao framework.
