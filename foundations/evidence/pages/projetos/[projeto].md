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

```sql mc_proj
select * from bsc.mc_estatisticas where project_name = '${params.projeto}' and variavel = 'VPL'
```

```sql mc_hist_proj
select bin_inferior, frequencia, cumul_pct from bsc.mc_histograma
where project_name = '${params.projeto}' and variavel = 'VPL' order by bin_idx
```

```sql mc_perc_proj
select percentil, valor from bsc.mc_percentis
where project_name = '${params.projeto}' and variavel = 'VPL' order by percentil
```

```sql mc_torn_proj
select variavel_entrada, beta_regressao, coef_correlacao from bsc.mc_tornado
where project_name = '${params.projeto}' and variavel_saida = 'VPL' order by ordem
```

```sql mc_todas_proj
select variavel, media, desvio_padrao, minimo, maximo, prob_menor_zero, var_5, cvar_5
from bsc.mc_estatisticas where project_name = '${params.projeto}'
```

```sql mcdm_proj
select metodo, score, rank_ from bsc.decisao_mcdm where project_name = '${params.projeto}' order by metodo
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

## 🎲 Simulação de Monte Carlo do VPL (10.000 iterações)

> Cada fluxo periódico deste projeto vira uma **variável aleatória Triangular** (±30% em torno do valor base).
> Método e gráficos replicam o **SimulAr v2.5**. A semente é fixa: rodar de novo dá o mesmo resultado.

<BigValue data={mc_proj} value=media title="VPL médio (R$)" fmt='$#,##0'/>
<BigValue data={mc_proj} value=desvio_padrao title="Desvio-padrão (R$)" fmt='$#,##0'/>
<BigValue data={mc_proj} value=prob_menor_zero title="P(VPL < 0) %" fmt=num2/>
<BigValue data={mc_proj} value=var_5 title="VaR 5% (R$)" fmt='$#,##0'/>

**Histograma de frequência do VPL** — 100 classes, do mínimo ao máximo simulados (a "curva de risco" do projeto).

<BarChart data={mc_hist_proj} x=bin_inferior y=frequencia title="Distribuição do VPL simulado" yAxisTitle="Frequência" xAxisTitle="VPL (R$)" colorPalette={['#FF0000']}>
  <ReferenceLine x=0 color=negative label="prejuízo"/>
</BarChart>

**Distribuição acumulada** — leia a probabilidade de o VPL ficar abaixo de qualquer valor.

<LineChart data={mc_hist_proj} x=bin_inferior y=cumul_pct title="Probabilidade acumulada do VPL (%)" yAxisTitle="Acumulado (%)" xAxisTitle="VPL (R$)">
  <ReferenceLine x=0 color=negative label="break-even"/>
</LineChart>

**Percentis do VPL (1% a 99%)** — o percentil 5% é o VaR: o pior cenário plausível.

<LineChart data={mc_perc_proj} x=percentil y=valor title="Percentis do VPL simulado" yAxisTitle="VPL (R$)" xAxisTitle="Percentil (%)">
  <ReferenceLine y=0 color=negative label="break-even"/>
</LineChart>

**Análise de sensibilidade (tornado)** — qual período mais move o VPL. O **beta** é o efeito de +R$ 1 no fluxo
daquele período sobre o VPL; a **correlação** mede o quanto a incerteza daquele período dita a incerteza do VPL.

<DataTable data={mc_torn_proj} rows=all rowShading=true>
  <Column id=variavel_entrada title="Variável de entrada"/>
  <Column id=beta_regressao title="Beta da regressão" fmt=num4 contentType=colorscale/>
  <Column id=coef_correlacao title="Coef. de correlação" fmt=num4 contentType=colorscale/>
</DataTable>

<BarChart data={mc_torn_proj} x=variavel_entrada y=coef_correlacao title="Tornado — correlação de cada período com o VPL" yAxisTitle="Correlação" swapXY=true sort=true colorPalette={['#FF0000']}/>

**Todas as saídas simuladas** (VPL, TIR, TIRM, VUL e ILL sob incerteza)

<DataTable data={mc_todas_proj} rows=all rowShading=true>
  <Column id=variavel title="Indicador"/>
  <Column id=media title="Média" fmt=num4/>
  <Column id=desvio_padrao title="Desvio-padrão" fmt=num4/>
  <Column id=minimo title="Mínimo" fmt=num4/>
  <Column id=maximo title="Máximo" fmt=num4/>
  <Column id=prob_menor_zero title="P(X<0) %" fmt=num2/>
  <Column id=var_5 title="VaR 5%" fmt=num4/>
  <Column id=cvar_5 title="CVaR 5%" fmt=num4/>
</DataTable>

## 🧮 Posição deste projeto em cada método multicritério

> **DEMATEL** deriva os pesos por influência; **ELECTRE I** e **PROMETHEE II** ranqueiam por sobreclassificação;
> **MAUT** por utilidade com aversão a risco; **MCDA-C** por função de valor ancorada em Neutro/Bom; e o
> **AHP-TOPSIS 2n** por proximidade à solução ideal. A posição final vem do consenso de Borda entre os cinco.

<DataTable data={mcdm_proj} rows=all rowShading=true>
  <Column id=metodo title="Método"/>
  <Column id=score title="Score" fmt=num4/>
  <Column id=rank_ title="Posição" contentType=colorscale/>
</DataTable>

<BarChart data={mcdm_proj} x=metodo y=rank_ title="Posição deste projeto por método (menor = melhor)" yAxisTitle="Posição" swapXY=true/>

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
