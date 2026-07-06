---
title: "Proyecto: {params.projeto}"
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
select CASE categoria_waste WHEN 'Defeito (Defects) - Alucinacao/Retrabalho' THEN 'Defecto - Alucinación/Retrabajo' WHEN 'Defeito - Alucinacao' THEN 'Defecto - Alucinación' WHEN 'Espera (Waiting) - Cota/429' THEN 'Espera - Cuota/429' WHEN 'Espera - Cota/429' THEN 'Espera - Cuota/429' WHEN 'Espera (Waiting) - Latencia Alta' THEN 'Espera - Latencia Alta' WHEN 'Espera - Latencia Alta' THEN 'Espera - Latencia Alta' WHEN 'Superprocessamento - Prompt Inflado' THEN 'Sobreprocesamiento - Prompt Inflado' ELSE categoria_waste END as categoria_waste, waste_tokens, pct_do_projeto, CASE solucao WHEN 'Fila com backoff + fallback por cota + upgrade de Tier (meta IOLI abaixo de 1%)' THEN 'Cola con backoff + fallback por cuota + upgrade de Tier (meta IOLI < 1%)' WHEN 'System prompt rigido + saida JSON + validacao LLM-as-judge (meta IITA abaixo de 10%)' THEN 'System prompt rígido + salida JSON + validación LLM-as-judge (meta IITA < 10%)' WHEN 'RAG/embeddings + sumarizacao + poda de historico (meta ITR estavel ou em queda)' THEN 'RAG/embeddings + resumen + poda de historial (meta ITR estable o en baja)' WHEN 'Streaming/TTFT + modelo rapido + cache (meta latencia abaixo de 3s)' THEN 'Streaming/TTFT + modelo rápido + caché (meta latencia < 3s)' WHEN 'Converter aberto em estruturado: system prompt restritivo + few-shot + guardrails de escopo' THEN 'Convertir abierto en estructurado: system prompt restrictivo + few-shot + guardrails de alcance' WHEN 'Few-shot valido + exigir testes + validacao de sintaxe/execucao + RAG das docs da lib' THEN 'Few-shot válido + exigir pruebas + validación de sintaxis/ejecución + RAG de docs de la lib' WHEN 'Decomposicao em etapas + verificacao por etapa + self-consistency' THEN 'Descomposición en etapas + verificación por etapa + self-consistency' WHEN 'JSON mode/schema + regex de validacao + exemplos entrada-saida' THEN 'JSON mode/schema + regex de validación + ejemplos entrada-salida' WHEN 'Melhorar retrieval (re-rank) + citar fontes + grounding obrigatorio' THEN 'Mejorar retrieval (re-rank) + citar fuentes + grounding obligatorio' WHEN 'Templates fixos + exemplos de saida + JSON mode' THEN 'Plantillas fijas + ejemplos de salida + JSON mode' WHEN 'Limites de tamanho + instrucoes de fidelidade + QA factual' THEN 'Límites de tamaño + instrucciones de fidelidad + QA factual' ELSE solucao END as solucao from bsc.wastes_lean where project_name = '${params.projeto}' order by waste_tokens desc
```

```sql aluc_proj
select CASE prompt_categoria WHEN 'Conversa/Aberto' THEN 'Conversación/Abierto' WHEN 'RAG/Busca' THEN 'RAG/Búsqueda' WHEN 'Transformacao/Formato' THEN 'Transformación/Formato' WHEN 'Raciocinio/Analise' THEN 'Razonamiento/Análisis' WHEN 'Sumarizacao' THEN 'Resumen' WHEN 'Geracao de Codigo' THEN 'Generación de Código' WHEN 'Extracao de Dados' THEN 'Extracción de Datos' ELSE prompt_categoria END as prompt_categoria, alucinacoes, taxa_aluc, CASE solucao WHEN 'Fila com backoff + fallback por cota + upgrade de Tier (meta IOLI abaixo de 1%)' THEN 'Cola con backoff + fallback por cuota + upgrade de Tier (meta IOLI < 1%)' WHEN 'System prompt rigido + saida JSON + validacao LLM-as-judge (meta IITA abaixo de 10%)' THEN 'System prompt rígido + salida JSON + validación LLM-as-judge (meta IITA < 10%)' WHEN 'RAG/embeddings + sumarizacao + poda de historico (meta ITR estavel ou em queda)' THEN 'RAG/embeddings + resumen + poda de historial (meta ITR estable o en baja)' WHEN 'Streaming/TTFT + modelo rapido + cache (meta latencia abaixo de 3s)' THEN 'Streaming/TTFT + modelo rápido + caché (meta latencia < 3s)' WHEN 'Converter aberto em estruturado: system prompt restritivo + few-shot + guardrails de escopo' THEN 'Convertir abierto en estructurado: system prompt restrictivo + few-shot + guardrails de alcance' WHEN 'Few-shot valido + exigir testes + validacao de sintaxe/execucao + RAG das docs da lib' THEN 'Few-shot válido + exigir pruebas + validación de sintaxis/ejecución + RAG de docs de la lib' WHEN 'Decomposicao em etapas + verificacao por etapa + self-consistency' THEN 'Descomposición en etapas + verificación por etapa + self-consistency' WHEN 'JSON mode/schema + regex de validacao + exemplos entrada-saida' THEN 'JSON mode/schema + regex de validación + ejemplos entrada-salida' WHEN 'Melhorar retrieval (re-rank) + citar fontes + grounding obrigatorio' THEN 'Mejorar retrieval (re-rank) + citar fuentes + grounding obligatorio' WHEN 'Templates fixos + exemplos de saida + JSON mode' THEN 'Plantillas fijas + ejemplos de salida + JSON mode' WHEN 'Limites de tamanho + instrucoes de fidelidade + QA factual' THEN 'Límites de tamaño + instrucciones de fidelidad + QA factual' ELSE solucao END as solucao from bsc.alucinacao_categoria where project_name = '${params.projeto}' and alucinacoes > 0 order by alucinacoes desc
```

# 🛠️ {params.projeto}

<BigValue data={proj} value=kpi_psr title="PSR (0-5)" fmt=num2/>
<BigValue data={proj} value=kpi_peuc title="PEUC (%)" fmt=num1/>
<BigValue data={proj} value=total_tokens title="Tokens" fmt=num0/>
<BigValue data={proj} value=kpi_cpp title="CPP (R$/%)" fmt='$#,##0.00'/>

## Diagnóstico de Eficiencia

<DataTable data={proj}>
  <Column id=kpi_iita title="IITA % (alucinación)" fmt=num1/>
  <Column id=kpi_idls_lean title="IDLS % (desperdicio Lean)" fmt=num1/>
  <Column id=kpi_ioli title="IOLI % (ociosidad)" fmt=num1/>
  <Column id=kpi_itr title="ITR (tok/req)" fmt=num0/>
  <Column id=kpi_ieet_hh_por_mtoken title="IEET (HH/M-tok)" fmt=num2/>
</DataTable>

## Salud Financiera (Gitman & Startup)

<DataTable data={proj}>
  <Column id=vrt_por_ktoken title="VRT/kT (R$/1k)" fmt='$#,##0.0000'/>
  <Column id=burn_rate_ia title="Burn Rate IA (R$)" fmt='$#,##0.00'/>
  <Column id=kpi_icca title="ICCA (x)" fmt=num2/>
  <Column id=kpi_ibmt title="IBMT (x)" fmt=num3/>
</DataTable>

## Pareto de Fallas de este Proyecto

<BarChart data={falhas_proj} x=categoria_falha y=quantidade title="Fallas por categoría" swapXY=true/>

## 🪙 Recuperación de Costos (VRT) — 5 bloques + promedio
<DataTable data={proj}>
  <Column id=vrt_50t title="50 tok" fmt='#,##0.00000'/>
  <Column id=vrt_100t title="100 tok" fmt='#,##0.00000'/>
  <Column id=vrt_250t title="250 tok" fmt='#,##0.00000'/>
  <Column id=vrt_500t title="500 tok" fmt='#,##0.00000'/>
  <Column id=vrt_por_ktoken title="1.000 tok" fmt='#,##0.00000'/>
  <Column id=vrt_media_blocos title="PROM." fmt='#,##0.00000'/>
</DataTable>

## ⏰ Hora Crítica de Interrupción (BRT)
<BarChart data={hora_proj} x=hora_brt y=interrupcoes title="Interrupciones por hora del día (BRT)" xAxisTitle="Hora (0-23)"/>

## ♻️ Taxonomía de Desperdicios (Lean Six Sigma)
<BarChart data={waste_proj} x=categoria_waste y=waste_tokens title="Desperdicio por categoría (tokens ponderados)" swapXY=true labels=true/>

## 🔬 RCA — Alucinación por Tipo de Prompt (qué retrasa este proyecto)
<BarChart data={aluc_proj} x=prompt_categoria y=alucinacoes title="Alucinaciones por tipo de prompt" swapXY=true labels=true sort=true/>

<DataTable data={aluc_proj}>
  <Column id=prompt_categoria title="Tipo de prompt"/>
  <Column id=alucinacoes title="Alucinaciones" fmt=num0/>
  <Column id=taxa_aluc title="Tasa %" fmt=num1/>
</DataTable>

---

# 📌 Bottom-Line — Diagnóstico Conclusivo y Solución Definitiva
_Estándar de mejora continua — fuente canónica: `foundations/solucoes_relatorios.md`._

## a) Disertación de Desperdicios (Lean Six Sigma)
{#if waste_proj.length > 0}
El **desperdicio dominante** de este proyecto es **{waste_proj[0].categoria_waste}**, responsable del **{waste_proj[0].pct_do_projeto}%** del waste ponderado. Consume tokens/caja sin avanzar el progreso y **presiona el CPP hacia arriba**. La solución definitiva y las demás categorías están en la tabla (aplicar por impacto):

<DataTable data={waste_proj}>
  <Column id=categoria_waste title="Desperdicio detectado"/>
  <Column id=waste_tokens title="Tokens desperd." fmt=num0/>
  <Column id=pct_do_projeto title="% del desperdicio" fmt=num1/>
  <Column id=solucao title="🛠️ Solución definitiva (PDCA)" wrap=true/>
</DataTable>
{:else}
✅ Sin desperdicio relevante registrado este período.
{/if}

## b) Disertación de Alucinación de Prompts (RCA por taxonomía)
{#if aluc_proj.length > 0}
El **tipo de prompt que más retrasa** este proyecto es **{aluc_proj[0].prompt_categoria}**, con **{aluc_proj[0].taxa_aluc}%** de alucinación — el **cuello de botella raíz**. Cada categoría con alucinación y su contramedida definitiva:

<DataTable data={aluc_proj}>
  <Column id=prompt_categoria title="Tipo de prompt"/>
  <Column id=alucinacoes title="Alucinaciones" fmt=num0/>
  <Column id=taxa_aluc title="Tasa %" fmt=num1/>
  <Column id=solucao title="🛠️ Solución definitiva (RCA)" wrap=true/>
</DataTable>
{:else}
✅ Sin alucinaciones registradas este período — ningún cuello de botella detectado.
{/if}

## c) Mejora Continua (PDCA / Kaizen)
1. **Plan** — atacar primero el desperdicio dominante y el cuello de botella arriba.
2. **Do** — aplicar las soluciones definitivas de las tablas.
3. **Check** — medir la semana siguiente: IITA, IDLS, IOLI, ITR y latencia.
4. **Act** — estandarizar lo que funcionó en el system prompt/pipeline y repetir.

> **Norte:** **CPP decreciente** semana a semana. Cada desperdicio y alucinación reducidos bajan el CPP.
