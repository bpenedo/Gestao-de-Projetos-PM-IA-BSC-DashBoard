---
title: "Project: {params.projeto}"
---

```sql proj
select * from bsc.kpis_bsc_ia where project_name = '${params.projeto}'
```

```sql falhas_proj
select * from bsc.dominancia_erros where project_name = '${params.projeto}'
```

```sql hora_proj
select hora_brt, interrupcoes from bsc.interrupcoes_hora where project_name = '${params.projeto}' order by hora_brt
```

```sql waste_proj
select CASE categoria_waste WHEN 'Defeito (Defects) - Alucinacao/Retrabalho' THEN 'Defect - Hallucination/Rework' WHEN 'Defeito - Alucinacao' THEN 'Defect - Hallucination' WHEN 'Espera (Waiting) - Cota/429' THEN 'Waiting - Quota/429' WHEN 'Espera - Cota/429' THEN 'Waiting - Quota/429' WHEN 'Espera (Waiting) - Latencia Alta' THEN 'Waiting - High Latency' WHEN 'Espera - Latencia Alta' THEN 'Waiting - High Latency' WHEN 'Superprocessamento - Prompt Inflado' THEN 'Overprocessing - Inflated Prompt' ELSE categoria_waste END as categoria_waste, waste_tokens, pct_do_projeto, CASE solucao WHEN 'Fila com backoff + fallback por cota + upgrade de Tier (meta IOLI abaixo de 1%)' THEN 'Queue with backoff + quota fallback + Tier upgrade (target IOLI below 1%)' WHEN 'System prompt rigido + saida JSON + validacao LLM-as-judge (meta IITA abaixo de 10%)' THEN 'Strict system prompt + JSON output + LLM-as-judge validation (target IITA below 10%)' WHEN 'RAG/embeddings + sumarizacao + poda de historico (meta ITR estavel ou em queda)' THEN 'RAG/embeddings + summarization + history pruning (target ITR stable or falling)' WHEN 'Streaming/TTFT + modelo rapido + cache (meta latencia abaixo de 3s)' THEN 'Streaming/TTFT + fast model + cache (target latency below 3s)' WHEN 'Converter aberto em estruturado: system prompt restritivo + few-shot + guardrails de escopo' THEN 'Convert open to structured: restrictive system prompt + few-shot + scope guardrails' WHEN 'Few-shot valido + exigir testes + validacao de sintaxe/execucao + RAG das docs da lib' THEN 'Valid few-shot + require tests + syntax/execution validation + RAG of lib docs' WHEN 'Decomposicao em etapas + verificacao por etapa + self-consistency' THEN 'Step decomposition + per-step verification + self-consistency' WHEN 'JSON mode/schema + regex de validacao + exemplos entrada-saida' THEN 'JSON mode/schema + validation regex + input-output examples' WHEN 'Melhorar retrieval (re-rank) + citar fontes + grounding obrigatorio' THEN 'Improve retrieval (re-rank) + cite sources + mandatory grounding' WHEN 'Templates fixos + exemplos de saida + JSON mode' THEN 'Fixed templates + output examples + JSON mode' WHEN 'Limites de tamanho + instrucoes de fidelidade + QA factual' THEN 'Size limits + fidelity instructions + factual QA' ELSE solucao END as solucao from bsc.wastes_lean where project_name = '${params.projeto}' order by waste_tokens desc
```

```sql aluc_proj
select CASE prompt_categoria WHEN 'Conversa/Aberto' THEN 'Chat/Open' WHEN 'RAG/Busca' THEN 'RAG/Search' WHEN 'Transformacao/Formato' THEN 'Transformation/Format' WHEN 'Raciocinio/Analise' THEN 'Reasoning/Analysis' WHEN 'Sumarizacao' THEN 'Summarization' WHEN 'Geracao de Codigo' THEN 'Code Generation' WHEN 'Extracao de Dados' THEN 'Data Extraction' ELSE prompt_categoria END as prompt_categoria, alucinacoes, taxa_aluc, CASE solucao WHEN 'Fila com backoff + fallback por cota + upgrade de Tier (meta IOLI abaixo de 1%)' THEN 'Queue with backoff + quota fallback + Tier upgrade (target IOLI below 1%)' WHEN 'System prompt rigido + saida JSON + validacao LLM-as-judge (meta IITA abaixo de 10%)' THEN 'Strict system prompt + JSON output + LLM-as-judge validation (target IITA below 10%)' WHEN 'RAG/embeddings + sumarizacao + poda de historico (meta ITR estavel ou em queda)' THEN 'RAG/embeddings + summarization + history pruning (target ITR stable or falling)' WHEN 'Streaming/TTFT + modelo rapido + cache (meta latencia abaixo de 3s)' THEN 'Streaming/TTFT + fast model + cache (target latency below 3s)' WHEN 'Converter aberto em estruturado: system prompt restritivo + few-shot + guardrails de escopo' THEN 'Convert open to structured: restrictive system prompt + few-shot + scope guardrails' WHEN 'Few-shot valido + exigir testes + validacao de sintaxe/execucao + RAG das docs da lib' THEN 'Valid few-shot + require tests + syntax/execution validation + RAG of lib docs' WHEN 'Decomposicao em etapas + verificacao por etapa + self-consistency' THEN 'Step decomposition + per-step verification + self-consistency' WHEN 'JSON mode/schema + regex de validacao + exemplos entrada-saida' THEN 'JSON mode/schema + validation regex + input-output examples' WHEN 'Melhorar retrieval (re-rank) + citar fontes + grounding obrigatorio' THEN 'Improve retrieval (re-rank) + cite sources + mandatory grounding' WHEN 'Templates fixos + exemplos de saida + JSON mode' THEN 'Fixed templates + output examples + JSON mode' WHEN 'Limites de tamanho + instrucoes de fidelidade + QA factual' THEN 'Size limits + fidelity instructions + factual QA' ELSE solucao END as solucao from bsc.alucinacao_categoria where project_name = '${params.projeto}' and alucinacoes > 0 order by alucinacoes desc
```

# 🛠️ {params.projeto}

<BigValue data={proj} value=kpi_psr title="PSR (0-5)" fmt=num2/>
<BigValue data={proj} value=kpi_peuc title="PEUC (%)" fmt=num1/>
<BigValue data={proj} value=total_tokens title="Tokens" fmt=num0/>
<BigValue data={proj} value=kpi_cpp title="CPP (R$/%)" fmt='$#,##0.00'/>

## Efficiency Diagnosis

<DataTable data={proj}>
  <Column id=kpi_iita title="IITA % (hallucination)" fmt=num1/>
  <Column id=kpi_idls_lean title="IDLS % (Lean waste)" fmt=num1/>
  <Column id=kpi_ioli title="IOLI % (idleness)" fmt=num1/>
  <Column id=kpi_itr title="ITR (tok/req)" fmt=num0/>
  <Column id=kpi_ieet_hh_por_mtoken title="IEET (HH/M-tok)" fmt=num2/>
</DataTable>

## Financial Health (Gitman & Startup)

<DataTable data={proj}>
  <Column id=vrt_por_ktoken title="VRT/kT (R$/1k)" fmt='$#,##0.0000'/>
  <Column id=burn_rate_ia title="AI Burn Rate (R$)" fmt='$#,##0.00'/>
  <Column id=kpi_icca title="ICCA (x)" fmt=num2/>
  <Column id=kpi_ibmt title="IBMT (x)" fmt=num3/>
</DataTable>

## Failure Pareto for This Project

<BarChart data={falhas_proj} x=categoria_falha y=quantidade title="Failures by category" swapXY=true/>

## 🪙 Cost Recovery (VRT) — 5 blocks + average
<DataTable data={proj}>
  <Column id=vrt_50t title="50 tok" fmt='#,##0.00000'/>
  <Column id=vrt_100t title="100 tok" fmt='#,##0.00000'/>
  <Column id=vrt_250t title="250 tok" fmt='#,##0.00000'/>
  <Column id=vrt_500t title="500 tok" fmt='#,##0.00000'/>
  <Column id=vrt_por_ktoken title="1.000 tok" fmt='#,##0.00000'/>
  <Column id=vrt_media_blocos title="AVG" fmt='#,##0.00000'/>
</DataTable>

## ⏰ Critical Interruption Hour (BRT)
<BarChart data={hora_proj} x=hora_brt y=interrupcoes title="Interruptions by hour of day (BRT)" xAxisTitle="Hour (0-23)"/>

## ♻️ Waste Taxonomy (Lean Six Sigma)
<BarChart data={waste_proj} x=categoria_waste y=waste_tokens title="Waste by category (weighted tokens)" swapXY=true labels=true/>

## 🔬 RCA — Hallucination by Prompt Type (what delays this project)
<BarChart data={aluc_proj} x=prompt_categoria y=alucinacoes title="Hallucinations by prompt type" swapXY=true labels=true sort=true/>

<DataTable data={aluc_proj}>
  <Column id=prompt_categoria title="Prompt type"/>
  <Column id=alucinacoes title="Hallucinations" fmt=num0/>
  <Column id=taxa_aluc title="Rate %" fmt=num1/>
</DataTable>

---

# 📌 Bottom-Line — Conclusive Diagnosis & Definitive Solution
_Continuous-improvement standard — canonical source: `foundations/solucoes_relatorios.md`._

## a) Waste Dissertation (Lean Six Sigma)
{#if waste_proj.length > 0}
This project's **dominant waste** is **{waste_proj[0].categoria_waste}**, accounting for **{waste_proj[0].pct_do_projeto}%** of weighted waste. It consumes tokens/cash without advancing progress and thus **pushes CPP up**. The definitive solution and the other detected categories are in the table below (apply in order of impact):

<DataTable data={waste_proj}>
  <Column id=categoria_waste title="Detected waste"/>
  <Column id=waste_tokens title="Wasted tokens" fmt=num0/>
  <Column id=pct_do_projeto title="% of waste" fmt=num1/>
  <Column id=solucao title="🛠️ Definitive solution (PDCA)" wrap=true/>
</DataTable>
{:else}
✅ No relevant waste recorded this period.
{/if}

## b) Prompt Hallucination Dissertation (RCA by taxonomy)
{#if aluc_proj.length > 0}
The **prompt type that most delays** this project is **{aluc_proj[0].prompt_categoria}**, with **{aluc_proj[0].taxa_aluc}%** hallucination — the **root bottleneck** of deliveries. Each category with detected hallucination and its definitive countermeasure:

<DataTable data={aluc_proj}>
  <Column id=prompt_categoria title="Prompt type"/>
  <Column id=alucinacoes title="Hallucinations" fmt=num0/>
  <Column id=taxa_aluc title="Rate %" fmt=num1/>
  <Column id=solucao title="🛠️ Definitive solution (RCA)" wrap=true/>
</DataTable>
{:else}
✅ No hallucinations recorded this period — no prompt bottleneck detected.
{/if}

## c) Continuous Improvement (PDCA / Kaizen)
1. **Plan** — attack first the dominant waste and prompt bottleneck above.
2. **Do** — apply the definitive solutions from the tables.
3. **Check** — measure next week: IITA, IDLS, IOLI, ITR and latency.
4. **Act** — standardize what worked in the system prompt/pipeline and repeat.

> **North star:** **decreasing CPP** week by week. Every waste and hallucination reduced pushes CPP down.
