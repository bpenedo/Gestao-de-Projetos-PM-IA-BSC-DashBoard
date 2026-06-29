---
title: "Projeto: {params.projeto}"
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
select categoria_waste, waste_tokens, pct_do_projeto, solucao from bsc.wastes_lean where project_name = '${params.projeto}' order by waste_tokens desc
```

```sql aluc_proj
select prompt_categoria, alucinacoes, taxa_aluc, solucao from bsc.alucinacao_categoria where project_name = '${params.projeto}' and alucinacoes > 0 order by alucinacoes desc
```

# 🛠️ {params.projeto}

<BigValue data={proj} value=kpi_psr title="PSR (0-5)" fmt=num2/>
<BigValue data={proj} value=kpi_peuc title="PEUC (%)" fmt=num1/>
<BigValue data={proj} value=total_tokens title="Tokens" fmt=num0/>
<BigValue data={proj} value=kpi_cpp title="CPP (R$/%)" fmt='$#,##0.00'/>

## Diagnóstico de Eficiência

<DataTable data={proj}>
  <Column id=kpi_iita title="IITA % (alucinação)" fmt=num1/>
  <Column id=kpi_idls_lean title="IDLS % (waste Lean)" fmt=num1/>
  <Column id=kpi_ioli title="IOLI % (ociosidade)" fmt=num1/>
  <Column id=kpi_itr title="ITR (tok/req)" fmt=num0/>
  <Column id=kpi_ieet_hh_por_mtoken title="IEET (HH/M-tok)" fmt=num2/>
</DataTable>

## Saúde Financeira (Gitman & Startup)

<DataTable data={proj}>
  <Column id=vrt_por_ktoken title="VRT/kT (R$/1k)" fmt='$#,##0.0000'/>
  <Column id=burn_rate_ia title="Burn Rate IA (R$)" fmt='$#,##0.00'/>
  <Column id=kpi_icca title="ICCA (x)" fmt=num2/>
  <Column id=kpi_ibmt title="IBMT (x)" fmt=num3/>
</DataTable>

## Pareto de Falhas deste Projeto

<BarChart data={falhas_proj} x=categoria_falha y=quantidade title="Falhas por categoria" swapXY=true/>

## 🪙 Custo de Recuperação (VRT) — 5 blocos + média
<DataTable data={proj}>
  <Column id=vrt_50t title="50 tok" fmt='#,##0.00000'/>
  <Column id=vrt_100t title="100 tok" fmt='#,##0.00000'/>
  <Column id=vrt_250t title="250 tok" fmt='#,##0.00000'/>
  <Column id=vrt_500t title="500 tok" fmt='#,##0.00000'/>
  <Column id=vrt_por_ktoken title="1.000 tok" fmt='#,##0.00000'/>
  <Column id=vrt_media_blocos title="MÉDIA" fmt='#,##0.00000'/>
</DataTable>

## ⏰ Horário Crítico de Interrupção (BRT)
<BarChart data={hora_proj} x=hora_brt y=interrupcoes title="Interrupções por hora do dia (BRT)" xAxisTitle="Hora (0-23)"/>

## ♻️ Taxonomia de Wastes (Lean Six Sigma)
<BarChart data={waste_proj} x=categoria_waste y=waste_tokens title="Waste por categoria (tokens ponderados)" swapXY=true labels=true/>

## 🔬 RCA — Alucinação por Tipo de Prompt (o que atrasa este projeto)
<BarChart data={aluc_proj} x=prompt_categoria y=alucinacoes title="Alucinações por tipo de prompt" swapXY=true labels=true sort=true/>

<DataTable data={aluc_proj}>
  <Column id=prompt_categoria title="Tipo de prompt"/>
  <Column id=alucinacoes title="Alucinações" fmt=num0/>
  <Column id=taxa_aluc title="Taxa %" fmt=num1/>
</DataTable>

---

# 📌 Bottom-Line — Diagnóstico Conclusivo & Solução Definitiva
_Padrão de melhoria contínua — fonte canônica: `foundations/solucoes_relatorios.md`._

## a) Dissertação de Wastes (Lean Six Sigma)
{#if waste_proj.length > 0}
O **desperdício dominante** deste projeto é **{waste_proj[0].categoria_waste}**, responsável por
**{waste_proj[0].pct_do_projeto}%** do waste ponderado. Esse desperdício consome tokens/caixa sem
avançar o progresso e, portanto, **pressiona o CPP para cima**. A solução definitiva e as demais
categorias detectadas estão na tabela abaixo (aplicar em ordem de impacto):

<DataTable data={waste_proj}>
  <Column id=categoria_waste title="Waste detectado"/>
  <Column id=waste_tokens title="Tokens desperd." fmt=num0/>
  <Column id=pct_do_projeto title="% do waste" fmt=num1/>
  <Column id=solucao title="🛠️ Solução definitiva (PDCA)" wrap=true/>
</DataTable>
{:else}
✅ Sem waste relevante registrado neste período.
{/if}

## b) Dissertação de Alucinação de Prompts (RCA por taxonomia)
{#if aluc_proj.length > 0}
O **tipo de prompt que mais atrasa** este projeto é **{aluc_proj[0].prompt_categoria}**, com
**{aluc_proj[0].taxa_aluc}%** de alucinação — é o **gargalo-raiz** das entregas. Cada categoria com
alucinação detectada e sua contramedida definitiva:

<DataTable data={aluc_proj}>
  <Column id=prompt_categoria title="Tipo de prompt"/>
  <Column id=alucinacoes title="Alucinações" fmt=num0/>
  <Column id=taxa_aluc title="Taxa %" fmt=num1/>
  <Column id=solucao title="🛠️ Solução definitiva (RCA)" wrap=true/>
</DataTable>
{:else}
✅ Sem alucinações registradas neste período — nenhum gargalo de prompt detectado.
{/if}

## c) Melhoria Contínua (PDCA / Kaizen)
1. **Plan** — atacar primeiro o waste dominante e o prompt-gargalo apontados acima.
2. **Do** — aplicar as soluções definitivas das tabelas.
3. **Check** — medir na semana seguinte: IITA, IDLS, IOLI, ITR e latência.
4. **Act** — padronizar no system prompt/pipeline o que funcionou e repetir o ciclo.

> **Norte:** **CPP decrescente** semana a semana. Cada waste e cada alucinação reduzidos derrubam o CPP.
