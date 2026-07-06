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
select CASE categoria_waste WHEN 'Defeito (Defects) - Alucinacao/Retrabalho' THEN 'Defekt - Halluzination/Nacharbeit' WHEN 'Defeito - Alucinacao' THEN 'Defekt - Halluzination' WHEN 'Espera (Waiting) - Cota/429' THEN 'Warten - Quote/429' WHEN 'Espera - Cota/429' THEN 'Warten - Quote/429' WHEN 'Espera (Waiting) - Latencia Alta' THEN 'Warten - Hohe Latenz' WHEN 'Espera - Latencia Alta' THEN 'Warten - Hohe Latenz' WHEN 'Superprocessamento - Prompt Inflado' THEN 'Überverarbeitung - Aufgeblähter Prompt' ELSE categoria_waste END as categoria_waste, waste_tokens, pct_do_projeto, CASE solucao WHEN 'Fila com backoff + fallback por cota + upgrade de Tier (meta IOLI abaixo de 1%)' THEN 'Queue mit Backoff + Quoten-Fallback + Tier-Upgrade (Ziel IOLI unter 1%)' WHEN 'System prompt rigido + saida JSON + validacao LLM-as-judge (meta IITA abaixo de 10%)' THEN 'Striktes System-Prompt + JSON-Ausgabe + LLM-as-judge-Validierung (Ziel IITA unter 10%)' WHEN 'RAG/embeddings + sumarizacao + poda de historico (meta ITR estavel ou em queda)' THEN 'RAG/Embeddings + Zusammenfassung + Verlaufsbereinigung (Ziel ITR stabil oder fallend)' WHEN 'Streaming/TTFT + modelo rapido + cache (meta latencia abaixo de 3s)' THEN 'Streaming/TTFT + schnelles Modell + Cache (Ziel Latenz unter 3s)' WHEN 'Converter aberto em estruturado: system prompt restritivo + few-shot + guardrails de escopo' THEN 'Offen in strukturiert wandeln: restriktives System-Prompt + Few-Shot + Scope-Guardrails' WHEN 'Few-shot valido + exigir testes + validacao de sintaxe/execucao + RAG das docs da lib' THEN 'Gültiges Few-Shot + Tests fordern + Syntax-/Ausführungsvalidierung + RAG der Lib-Docs' WHEN 'Decomposicao em etapas + verificacao por etapa + self-consistency' THEN 'Schrittzerlegung + Schrittverifikation + Self-Consistency' WHEN 'JSON mode/schema + regex de validacao + exemplos entrada-saida' THEN 'JSON-Mode/Schema + Validierungs-Regex + Eingabe-Ausgabe-Beispiele' WHEN 'Melhorar retrieval (re-rank) + citar fontes + grounding obrigatorio' THEN 'Retrieval verbessern (Re-Rank) + Quellen zitieren + verpflichtendes Grounding' WHEN 'Templates fixos + exemplos de saida + JSON mode' THEN 'Feste Templates + Ausgabebeispiele + JSON-Mode' WHEN 'Limites de tamanho + instrucoes de fidelidade + QA factual' THEN 'Größenlimits + Treue-Anweisungen + faktisches QA' ELSE solucao END as solucao from bsc.wastes_lean where project_name = '${params.projeto}' order by waste_tokens desc
```

```sql aluc_proj
select CASE prompt_categoria WHEN 'Conversa/Aberto' THEN 'Chat/Offen' WHEN 'RAG/Busca' THEN 'RAG/Suche' WHEN 'Transformacao/Formato' THEN 'Transformation/Format' WHEN 'Raciocinio/Analise' THEN 'Schlussfolgern/Analyse' WHEN 'Sumarizacao' THEN 'Zusammenfassung' WHEN 'Geracao de Codigo' THEN 'Codegenerierung' WHEN 'Extracao de Dados' THEN 'Datenextraktion' ELSE prompt_categoria END as prompt_categoria, alucinacoes, taxa_aluc, CASE solucao WHEN 'Fila com backoff + fallback por cota + upgrade de Tier (meta IOLI abaixo de 1%)' THEN 'Queue mit Backoff + Quoten-Fallback + Tier-Upgrade (Ziel IOLI unter 1%)' WHEN 'System prompt rigido + saida JSON + validacao LLM-as-judge (meta IITA abaixo de 10%)' THEN 'Striktes System-Prompt + JSON-Ausgabe + LLM-as-judge-Validierung (Ziel IITA unter 10%)' WHEN 'RAG/embeddings + sumarizacao + poda de historico (meta ITR estavel ou em queda)' THEN 'RAG/Embeddings + Zusammenfassung + Verlaufsbereinigung (Ziel ITR stabil oder fallend)' WHEN 'Streaming/TTFT + modelo rapido + cache (meta latencia abaixo de 3s)' THEN 'Streaming/TTFT + schnelles Modell + Cache (Ziel Latenz unter 3s)' WHEN 'Converter aberto em estruturado: system prompt restritivo + few-shot + guardrails de escopo' THEN 'Offen in strukturiert wandeln: restriktives System-Prompt + Few-Shot + Scope-Guardrails' WHEN 'Few-shot valido + exigir testes + validacao de sintaxe/execucao + RAG das docs da lib' THEN 'Gültiges Few-Shot + Tests fordern + Syntax-/Ausführungsvalidierung + RAG der Lib-Docs' WHEN 'Decomposicao em etapas + verificacao por etapa + self-consistency' THEN 'Schrittzerlegung + Schrittverifikation + Self-Consistency' WHEN 'JSON mode/schema + regex de validacao + exemplos entrada-saida' THEN 'JSON-Mode/Schema + Validierungs-Regex + Eingabe-Ausgabe-Beispiele' WHEN 'Melhorar retrieval (re-rank) + citar fontes + grounding obrigatorio' THEN 'Retrieval verbessern (Re-Rank) + Quellen zitieren + verpflichtendes Grounding' WHEN 'Templates fixos + exemplos de saida + JSON mode' THEN 'Feste Templates + Ausgabebeispiele + JSON-Mode' WHEN 'Limites de tamanho + instrucoes de fidelidade + QA factual' THEN 'Größenlimits + Treue-Anweisungen + faktisches QA' ELSE solucao END as solucao from bsc.alucinacao_categoria where project_name = '${params.projeto}' and alucinacoes > 0 order by alucinacoes desc
```

# 🛠️ {params.projeto}

<BigValue data={proj} value=kpi_psr title="PSR (0-5)" fmt=num2/>
<BigValue data={proj} value=kpi_peuc title="PEUC (%)" fmt=num1/>
<BigValue data={proj} value=total_tokens title="Tokens" fmt=num0/>
<BigValue data={proj} value=kpi_cpp title="CPP (R$/%)" fmt='$#,##0.00'/>

## Effizienzdiagnose

<DataTable data={proj}>
  <Column id=kpi_iita title="IITA % (Halluzination)" fmt=num1/>
  <Column id=kpi_idls_lean title="IDLS % (Lean-Verschwendung)" fmt=num1/>
  <Column id=kpi_ioli title="IOLI % (Leerlauf)" fmt=num1/>
  <Column id=kpi_itr title="ITR (tok/req)" fmt=num0/>
  <Column id=kpi_ieet_hh_por_mtoken title="IEET (HH/M-tok)" fmt=num2/>
</DataTable>

## Finanzielle Gesundheit (Gitman & Startup)

<DataTable data={proj}>
  <Column id=vrt_por_ktoken title="VRT/kT (R$/1k)" fmt='$#,##0.0000'/>
  <Column id=burn_rate_ia title="KI-Burn-Rate (R$)" fmt='$#,##0.00'/>
  <Column id=kpi_icca title="ICCA (x)" fmt=num2/>
  <Column id=kpi_ibmt title="IBMT (x)" fmt=num3/>
</DataTable>

## Fehler-Pareto dieses Projekts

<BarChart data={falhas_proj} x=categoria_falha y=quantidade title="Fehler nach Kategorie" swapXY=true/>

## 🪙 Kostendeckung (VRT) — 5 Blöcke + Mittelwert
<DataTable data={proj}>
  <Column id=vrt_50t title="50 tok" fmt='#,##0.00000'/>
  <Column id=vrt_100t title="100 tok" fmt='#,##0.00000'/>
  <Column id=vrt_250t title="250 tok" fmt='#,##0.00000'/>
  <Column id=vrt_500t title="500 tok" fmt='#,##0.00000'/>
  <Column id=vrt_por_ktoken title="1.000 tok" fmt='#,##0.00000'/>
  <Column id=vrt_media_blocos title="Ø" fmt='#,##0.00000'/>
</DataTable>

## ⏰ Kritische Unterbrechungsstunde (BRT)
<BarChart data={hora_proj} x=hora_brt y=interrupcoes title="Unterbrechungen nach Tagesstunde (BRT)" xAxisTitle="Stunde (0-23)"/>

## ♻️ Verschwendungs-Taxonomie (Lean Six Sigma)
<BarChart data={waste_proj} x=categoria_waste y=waste_tokens title="Verschwendung nach Kategorie (gewichtete Tokens)" swapXY=true labels=true/>

## 🔬 RCA — Halluzination nach Prompt-Typ (was dieses Projekt verzögert)
<BarChart data={aluc_proj} x=prompt_categoria y=alucinacoes title="Halluzinationen nach Prompt-Typ" swapXY=true labels=true sort=true/>

<DataTable data={aluc_proj}>
  <Column id=prompt_categoria title="Prompt-Typ"/>
  <Column id=alucinacoes title="Halluzinationen" fmt=num0/>
  <Column id=taxa_aluc title="Rate %" fmt=num1/>
</DataTable>

---

# 📌 Bottom-Line — Abschließende Diagnose & endgültige Lösung
_Standard der kontinuierlichen Verbesserung — kanonische Quelle: `foundations/solucoes_relatorios.md`._

## a) Verschwendungs-Abhandlung (Lean Six Sigma)
{#if waste_proj.length > 0}
Die **dominante Verschwendung** dieses Projekts ist **{waste_proj[0].categoria_waste}**, verantwortlich für **{waste_proj[0].pct_do_projeto}%** der gewichteten Verschwendung. Sie verbraucht Tokens/Cash ohne Fortschritt und **treibt den CPP nach oben**. Die endgültige Lösung und weitere Kategorien in der Tabelle (nach Impact anwenden):

<DataTable data={waste_proj}>
  <Column id=categoria_waste title="Erkannte Verschwendung"/>
  <Column id=waste_tokens title="Verschw. Tokens" fmt=num0/>
  <Column id=pct_do_projeto title="% der Verschwendung" fmt=num1/>
  <Column id=solucao title="🛠️ Endgültige Lösung (PDCA)" wrap=true/>
</DataTable>
{:else}
✅ Kein relevanter Verschwendung in diesem Zeitraum.
{/if}

## b) Prompt-Halluzinations-Abhandlung (RCA nach Taxonomie)
{#if aluc_proj.length > 0}
Der **Prompt-Typ mit größter Verzögerung** ist **{aluc_proj[0].prompt_categoria}**, mit **{aluc_proj[0].taxa_aluc}%** Halluzination — der **Wurzel-Engpass**. Jede Kategorie mit Halluzination und ihre endgültige Gegenmaßnahme:

<DataTable data={aluc_proj}>
  <Column id=prompt_categoria title="Prompt-Typ"/>
  <Column id=alucinacoes title="Halluzinationen" fmt=num0/>
  <Column id=taxa_aluc title="Rate %" fmt=num1/>
  <Column id=solucao title="🛠️ Endgültige Lösung (RCA)" wrap=true/>
</DataTable>
{:else}
✅ Keine Halluzinationen in diesem Zeitraum — kein Prompt-Engpass erkannt.
{/if}

## c) Kontinuierliche Verbesserung (PDCA / Kaizen)
1. **Plan** — zuerst dominante Verschwendung und Prompt-Engpass angehen.
2. **Do** — die endgültigen Lösungen aus den Tabellen anwenden.
3. **Check** — nächste Woche messen: IITA, IDLS, IOLI, ITR und Latenz.
4. **Act** — Bewährtes im System-Prompt/Pipeline standardisieren und wiederholen.

> **Leitstern:** **sinkender CPP** Woche für Woche. Jede reduzierte Verschwendung/Halluzination senkt den CPP.
