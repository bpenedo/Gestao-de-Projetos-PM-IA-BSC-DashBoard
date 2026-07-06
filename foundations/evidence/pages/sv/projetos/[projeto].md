---
title: "Projekt: {params.projeto}"
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
select CASE categoria_waste WHEN 'Defeito (Defects) - Alucinacao/Retrabalho' THEN 'Defekt - Hallucination/Omarbete' WHEN 'Defeito - Alucinacao' THEN 'Defekt - Hallucination' WHEN 'Espera (Waiting) - Cota/429' THEN 'Väntan - Kvot/429' WHEN 'Espera - Cota/429' THEN 'Väntan - Kvot/429' WHEN 'Espera (Waiting) - Latencia Alta' THEN 'Väntan - Hög latens' WHEN 'Espera - Latencia Alta' THEN 'Väntan - Hög latens' WHEN 'Superprocessamento - Prompt Inflado' THEN 'Överbearbetning - Uppblåst prompt' ELSE categoria_waste END as categoria_waste, waste_tokens, pct_do_projeto, CASE solucao WHEN 'Fila com backoff + fallback por cota + upgrade de Tier (meta IOLI abaixo de 1%)' THEN 'Kö med backoff + kvot-fallback + Tier-uppgradering (mål IOLI under 1%)' WHEN 'System prompt rigido + saida JSON + validacao LLM-as-judge (meta IITA abaixo de 10%)' THEN 'Strikt system prompt + JSON-utdata + LLM-as-judge-validering (mål IITA under 10%)' WHEN 'RAG/embeddings + sumarizacao + poda de historico (meta ITR estavel ou em queda)' THEN 'RAG/embeddings + sammanfattning + historikbeskärning (mål ITR stabil/fallande)' WHEN 'Streaming/TTFT + modelo rapido + cache (meta latencia abaixo de 3s)' THEN 'Streaming/TTFT + snabb modell + cache (mål latens under 3s)' WHEN 'Converter aberto em estruturado: system prompt restritivo + few-shot + guardrails de escopo' THEN 'Konvertera öppet till strukturerat: restriktiv system prompt + few-shot + scope-guardrails' WHEN 'Few-shot valido + exigir testes + validacao de sintaxe/execucao + RAG das docs da lib' THEN 'Giltig few-shot + kräv tester + syntax-/exekveringsvalidering + RAG av lib-dokument' WHEN 'Decomposicao em etapas + verificacao por etapa + self-consistency' THEN 'Stegvis dekomposition + verifiering per steg + self-consistency' WHEN 'JSON mode/schema + regex de validacao + exemplos entrada-saida' THEN 'JSON mode/schema + validerings-regex + in-utdata-exempel' WHEN 'Melhorar retrieval (re-rank) + citar fontes + grounding obrigatorio' THEN 'Förbättra retrieval (re-rank) + citera källor + obligatorisk grounding' WHEN 'Templates fixos + exemplos de saida + JSON mode' THEN 'Fasta mallar + utdataexempel + JSON mode' WHEN 'Limites de tamanho + instrucoes de fidelidade + QA factual' THEN 'Storleksgränser + trohetsinstruktioner + faktabaserad QA' ELSE solucao END as solucao from bsc.wastes_lean where project_name = '${params.projeto}' order by waste_tokens desc
```

```sql aluc_proj
select CASE prompt_categoria WHEN 'Conversa/Aberto' THEN 'Chatt/Öppen' WHEN 'RAG/Busca' THEN 'RAG/Sökning' WHEN 'Transformacao/Formato' THEN 'Transformation/Format' WHEN 'Raciocinio/Analise' THEN 'Resonemang/Analys' WHEN 'Sumarizacao' THEN 'Sammanfattning' WHEN 'Geracao de Codigo' THEN 'Kodgenerering' WHEN 'Extracao de Dados' THEN 'Datautvinning' ELSE prompt_categoria END as prompt_categoria, alucinacoes, taxa_aluc, CASE solucao WHEN 'Fila com backoff + fallback por cota + upgrade de Tier (meta IOLI abaixo de 1%)' THEN 'Kö med backoff + kvot-fallback + Tier-uppgradering (mål IOLI under 1%)' WHEN 'System prompt rigido + saida JSON + validacao LLM-as-judge (meta IITA abaixo de 10%)' THEN 'Strikt system prompt + JSON-utdata + LLM-as-judge-validering (mål IITA under 10%)' WHEN 'RAG/embeddings + sumarizacao + poda de historico (meta ITR estavel ou em queda)' THEN 'RAG/embeddings + sammanfattning + historikbeskärning (mål ITR stabil/fallande)' WHEN 'Streaming/TTFT + modelo rapido + cache (meta latencia abaixo de 3s)' THEN 'Streaming/TTFT + snabb modell + cache (mål latens under 3s)' WHEN 'Converter aberto em estruturado: system prompt restritivo + few-shot + guardrails de escopo' THEN 'Konvertera öppet till strukturerat: restriktiv system prompt + few-shot + scope-guardrails' WHEN 'Few-shot valido + exigir testes + validacao de sintaxe/execucao + RAG das docs da lib' THEN 'Giltig few-shot + kräv tester + syntax-/exekveringsvalidering + RAG av lib-dokument' WHEN 'Decomposicao em etapas + verificacao por etapa + self-consistency' THEN 'Stegvis dekomposition + verifiering per steg + self-consistency' WHEN 'JSON mode/schema + regex de validacao + exemplos entrada-saida' THEN 'JSON mode/schema + validerings-regex + in-utdata-exempel' WHEN 'Melhorar retrieval (re-rank) + citar fontes + grounding obrigatorio' THEN 'Förbättra retrieval (re-rank) + citera källor + obligatorisk grounding' WHEN 'Templates fixos + exemplos de saida + JSON mode' THEN 'Fasta mallar + utdataexempel + JSON mode' WHEN 'Limites de tamanho + instrucoes de fidelidade + QA factual' THEN 'Storleksgränser + trohetsinstruktioner + faktabaserad QA' ELSE solucao END as solucao from bsc.alucinacao_categoria where project_name = '${params.projeto}' and alucinacoes > 0 order by alucinacoes desc
```

# 🛠️ {params.projeto}

<BigValue data={proj} value=kpi_psr title="PSR (0-5)" fmt=num2/>
<BigValue data={proj} value=kpi_peuc title="PEUC (%)" fmt=num1/>
<BigValue data={proj} value=total_tokens title="Tokens" fmt=num0/>
<BigValue data={proj} value=kpi_cpp title="CPP (R$/%)" fmt='$#,##0.00'/>

## Effektivitetsdiagnos

<DataTable data={proj}>
  <Column id=kpi_iita title="IITA % (hallucination)" fmt=num1/>
  <Column id=kpi_idls_lean title="IDLS % (Lean-slöseri)" fmt=num1/>
  <Column id=kpi_ioli title="IOLI % (inaktivitet)" fmt=num1/>
  <Column id=kpi_itr title="ITR (tok/req)" fmt=num0/>
  <Column id=kpi_ieet_hh_por_mtoken title="IEET (HH/M-tok)" fmt=num2/>
</DataTable>

## Finansiell hälsa (Gitman & Startup)

<DataTable data={proj}>
  <Column id=vrt_por_ktoken title="VRT/kT (R$/1k)" fmt='$#,##0.0000'/>
  <Column id=burn_rate_ia title="AI Burn Rate (R$)" fmt='$#,##0.00'/>
  <Column id=kpi_icca title="ICCA (x)" fmt=num2/>
  <Column id=kpi_ibmt title="IBMT (x)" fmt=num3/>
</DataTable>

## Felpareto för detta projekt

<BarChart data={falhas_proj} x=categoria_falha y=quantidade title="Fel per kategori" swapXY=true/>

## 🪙 Kostnadsåtervinning (VRT) — 5 block + medel
<DataTable data={proj}>
  <Column id=vrt_50t title="50 tok" fmt='#,##0.00000'/>
  <Column id=vrt_100t title="100 tok" fmt='#,##0.00000'/>
  <Column id=vrt_250t title="250 tok" fmt='#,##0.00000'/>
  <Column id=vrt_500t title="500 tok" fmt='#,##0.00000'/>
  <Column id=vrt_por_ktoken title="1.000 tok" fmt='#,##0.00000'/>
  <Column id=vrt_media_blocos title="MEDEL" fmt='#,##0.00000'/>
</DataTable>

## ⏰ Kritisk avbrottstimme (BRT)
<BarChart data={hora_proj} x=hora_brt y=interrupcoes title="Avbrott per timme (BRT)" xAxisTitle="Timme (0-23)"/>

## ♻️ Slöseritaxonomi (Lean Six Sigma)
<BarChart data={waste_proj} x=categoria_waste y=waste_tokens title="Slöseri per kategori (viktade tokens)" swapXY=true labels=true/>

## 🔬 RCA — hallucination per prompttyp (vad som försenar detta projekt)
<BarChart data={aluc_proj} x=prompt_categoria y=alucinacoes title="Hallucinationer per prompttyp" swapXY=true labels=true sort=true/>

<DataTable data={aluc_proj}>
  <Column id=prompt_categoria title="Prompttyp"/>
  <Column id=alucinacoes title="Hallucinationer" fmt=num0/>
  <Column id=taxa_aluc title="Andel %" fmt=num1/>
</DataTable>

---

# 📌 Slutsats — avgörande diagnos & definitiv lösning
_Standard för ständig förbättring — kanonisk källa: `foundations/solucoes_relatorios.md`._

## a) Slöseriutläggning (Lean Six Sigma)
{#if waste_proj.length > 0}
Projektets **dominerande slöseri** är **{waste_proj[0].categoria_waste}**, som står för **{waste_proj[0].pct_do_projeto}%** av det viktade slöseriet. Det förbrukar tokens/kassa utan framsteg och **driver upp CPP**. Definitiv lösning och övriga kategorier i tabellen (tillämpa efter påverkan):

<DataTable data={waste_proj}>
  <Column id=categoria_waste title="Upptäckt slöseri"/>
  <Column id=waste_tokens title="Slösade tokens" fmt=num0/>
  <Column id=pct_do_projeto title="% av slöseri" fmt=num1/>
  <Column id=solucao title="🛠️ Definitiv lösning (PDCA)" wrap=true/>
</DataTable>
{:else}
✅ Inget relevant slöseri registrerat denna period.
{/if}

## b) Prompthallucination (RCA per taxonomi)
{#if aluc_proj.length > 0}
**Prompttypen som mest försenar** projektet är **{aluc_proj[0].prompt_categoria}**, med **{aluc_proj[0].taxa_aluc}%** hallucination — leveransernas **rotflaskhals**. Varje kategori med hallucination och dess definitiva motåtgärd:

<DataTable data={aluc_proj}>
  <Column id=prompt_categoria title="Prompttyp"/>
  <Column id=alucinacoes title="Hallucinationer" fmt=num0/>
  <Column id=taxa_aluc title="Andel %" fmt=num1/>
  <Column id=solucao title="🛠️ Definitiv lösning (RCA)" wrap=true/>
</DataTable>
{:else}
✅ Inga hallucinationer denna period — ingen promptflaskhals.
{/if}

## c) Ständig förbättring (PDCA / Kaizen)
1. **Plan** — angrip först det dominerande slöseriet och promptflaskhalsen ovan.
2. **Do** — tillämpa de definitiva lösningarna från tabellerna.
3. **Check** — mät nästa vecka: IITA, IDLS, IOLI, ITR och latens.
4. **Act** — standardisera det som fungerade i system prompt/pipeline och upprepa.

> **Ledstjärna:** **sjunkande CPP** vecka för vecka. Varje minskat slöseri och hallucination sänker CPP.
