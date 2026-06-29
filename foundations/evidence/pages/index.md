---
title: Painel BSC — Gestão de Projetos (PM) IA
---

_Framework "Painel BSC Dashboard — Gestão de Projetos (PM) IA" · Bruno Teixeira Penedo · 27/06/2026._
**Weekly Checkpoint — toda sexta-feira às 09:00.**

> ⚠️ **Dados DEMO** dos 10 projetos reais de `~/devparetoprojects/*`. Tornam-se reais quando o Langfuse sincronizar.

```sql kpis
select * from bsc.kpis_bsc_ia
```
```sql tendencia
select * from bsc.tendencia
```
```sql falhas_mix
select * from bsc.falhas_mix
```
```sql falhas
select * from bsc.dominancia_erros
```
```sql alertas
select * from bsc.alertas_topo
```
```sql reuniao
select * from bsc.reuniao_weekly
```
```sql hora_total
select hora_brt, sum(interrupcoes) as interrupcoes from bsc.interrupcoes_hora group by hora_brt order by hora_brt
```
```sql horario_critico
select * from bsc.horario_critico
```
```sql wastes
select * from bsc.wastes_lean
```
```sql waste_dom
select * from bsc.waste_dominante
```
```sql waste_mix
select categoria_waste, sum(waste_tokens) as waste_tokens from bsc.wastes_lean group by categoria_waste order by waste_tokens desc
```
```sql aluc_cat
select * from bsc.alucinacao_categoria
```
```sql rca_proj
select * from bsc.rca_projeto
```
```sql rca_inter
select * from bsc.rca_intersecao
```
```sql vpl
select * from bsc.vpl_resultado
```
```sql vpl_fluxo
select * from bsc.vpl_fluxo
```

## 📈 Sumário Executivo do Portfólio

<BigValue data={kpis} value=total_tokens title="Tokens Totais" agg=sum fmt=num0/>
<BigValue data={kpis} value=kpi_psr title="PSR Médio (0-5)" agg=mean fmt=num1/>
<BigValue data={kpis} value=kpi_idls_lean title="Desperdício Lean Médio %" agg=mean fmt=num1/>
<BigValue data={kpis} value=burn_rate_ia title="Burn Rate Total" agg=sum fmt='$#,##0.00'/>

## 🌐 Mapa 5D do Portfólio (visão C-Level)
> Esferas 3D estilo 5dchart — **5 dimensões por projeto**: **X**=Volume/escala (tokens) · **Y**=PEUC/qualidade (%) · **Z**=PSR/saúde (0–5) · **tamanho**=Burn Rate (R$) · **cor**=ICCA/sustentabilidade (🟢 acima de 3x cobre custo · 🔴 abaixo de 1x = prejuízo).
>
> **Leitura de conselho:** o projeto ideal fica à **direita/fundo** (escala+qualidade), **alto** (PSR) e **verde** (sustentável). Esfera **grande e vermelha** = muito caixa queimado sem cobertura → corrigir antes de escalar.

![Mapa 5D do Portfólio de Projetos de IA](/5d_projetos.png?v=4)

## 📉 Tendência do Indicador-Mestre (CPP) e do Score (PSR)
> O que mais importa para o C-Level: **a direção**. CPP caindo = portfólio ficando mais eficiente.

<LineChart data={tendencia} x=data_snapshot y=cpp_medio yAxisTitle="CPP médio (R$/%)" title="Custo por Ponto de Progresso — tendência do portfólio" markers=true/>

<LineChart data={tendencia} x=data_snapshot y=psr_medio yAxisTitle="PSR médio" yMin=0 yMax=5 title="Score médio do portfólio (PSR 0-5)" markers=true/>

## ⭐ Score (PSR) por Projeto

<BarChart data={kpis} x=project_name y=kpi_psr swapXY=true title="PSR (0-5) por projeto — ordenado" sort=true labels=true/>

## 🍩 Composição & Mix (donut com profundidade)

<Grid cols=2>
<Group>

**Onde o caixa de IA está sendo queimado** (Burn Rate por projeto)

<ECharts config={{
  tooltip: { trigger: 'item', valueFormatter: (v) => 'R$ ' + Number(v).toFixed(2) },
  legend: { type: 'scroll', bottom: 0, textStyle: { fontSize: 10 } },
  series: [{
    type: 'pie', radius: ['45%','72%'], center: ['50%','45%'], avoidLabelOverlap: true,
    itemStyle: { borderRadius: 8, borderColor: '#fff', borderWidth: 2,
                 shadowBlur: 20, shadowColor: 'rgba(0,0,0,0.35)', shadowOffsetY: 8 },
    label: { formatter: '{d}%' },
    emphasis: { scaleSize: 12, itemStyle: { shadowBlur: 30 } },
    data: kpis.map(d => ({ name: d.project_name, value: Number(d.burn_rate_ia) }))
  }]
}} />

</Group>
<Group>

**Mix global de falhas** (Pareto em donut)

<ECharts config={{
  tooltip: { trigger: 'item' },
  legend: { type: 'scroll', bottom: 0, textStyle: { fontSize: 10 } },
  series: [{
    type: 'pie', radius: ['45%','72%'], center: ['50%','45%'], roseType: 'radius',
    itemStyle: { borderRadius: 8, borderColor: '#fff', borderWidth: 2,
                 shadowBlur: 20, shadowColor: 'rgba(0,0,0,0.35)', shadowOffsetY: 8 },
    label: { formatter: '{b}\n{d}%', fontSize: 10 },
    data: falhas_mix.map(d => ({ name: d.categoria, value: Number(d.qtd) }))
  }]
}} />

</Group>
</Grid>

## 🧭 Quadrante de Sustentabilidade (escalar ou corrigir?)
> Eixo X = **ICCA** (cobertura: acima de 3x = saudável) · Eixo Y = **IBMT** (queima marginal: abaixo de 0,33 = bom) · tamanho = Burn Rate.
> Canto inferior-direito = **escalar com lucro**; superior-esquerdo = **corrigir antes de crescer**.

<ScatterPlot data={kpis} x=kpi_icca y=kpi_ibmt series=project_name size=burn_rate_ia xAxisTitle="ICCA — cobertura de custo (x)" yAxisTitle="IBMT — burn marginal (x)" title="Sustentabilidade financeira por projeto"/>

## 📊 Pareto de Falhas por Projeto

<BarChart data={falhas} x=project_name y=percentual_dominancia series=categoria_falha type=stacked100 swapXY=true title="Dominância de falhas (%) por projeto"/>

## 🗂️ Score & Saúde Financeira (tabela)

<DataTable data={kpis} rows=all rowShading=true>
  <Column id=project_name title="Projeto"/>
  <Column id=kpi_psr title="PSR" fmt=num2/>
  <Column id=kpi_peuc title="PEUC %" fmt=num1/>
  <Column id=kpi_iita title="IITA %" fmt=num1/>
  <Column id=kpi_idls_lean title="IDLS %" fmt=num1/>
  <Column id=vrt_por_ktoken title="VRT/kT" fmt='$#,##0.0000'/>
  <Column id=kpi_icca title="ICCA x" fmt=num2/>
  <Column id=kpi_ibmt title="IBMT x" fmt=num3/>
  <Column id=kpi_cpp title="CPP R$/%" fmt='$#,##0.00'/>
</DataTable>

## 🚨 Alertas Críticos

<DataTable data={alertas} rows=8>
  <Column id=project_name title="Projeto"/>
  <Column id=tipo_erro title="Falha"/>
  <Column id=tokens_desperdicados title="Tokens" fmt=num0/>
  <Column id=data_evento title="Quando"/>
</DataTable>

## 📅 Pauta da Reunião Semanal

<DataTable data={reuniao} rows=all>
  <Column id=project_name title="Projeto"/>
  <Column id=sumario_executivo title="Sumário"/>
  <Column id=acoes_corretivas_lean title="Ações Lean (PDCA)"/>
</DataTable>

## 🪙 Custo de Recuperação (VRT) — 5 blocos + média (2ª ótica)
> Mesma base de rateio em **5 granularidades** (R$ por 50/100/250/500/1.000 tokens) + a **média dos blocos** — uma segunda percepção do consumo por projeto.

<DataTable data={kpis} rows=all rowShading=true>
  <Column id=project_name title="Projeto"/>
  <Column id=vrt_50t title="50 tok" fmt='#,##0.00000'/>
  <Column id=vrt_100t title="100 tok" fmt='#,##0.00000'/>
  <Column id=vrt_250t title="250 tok" fmt='#,##0.00000'/>
  <Column id=vrt_500t title="500 tok" fmt='#,##0.00000'/>
  <Column id=vrt_por_ktoken title="1.000 tok" fmt='#,##0.00000'/>
  <Column id=vrt_media_blocos title="MÉDIA blocos" fmt='#,##0.00000' contentType=colorscale/>
</DataTable>

## ⏰ Horário Crítico de Interrupção/Impacto (HCI)
> Em que **hora do dia (BRT)** cada projeto é mais impactado — para agir na janela certa (upgrade de Tier, backoff, agendamento).

<BarChart data={hora_total} x=hora_brt y=interrupcoes title="Interrupções por hora do dia (BRT) — portfólio" xAxisTitle="Hora (0-23, BRT)"/>

<DataTable data={horario_critico} rows=all rowShading=true>
  <Column id=project_name title="Projeto"/>
  <Column id=hora_pico title="Hora de pico (BRT)" fmt='0"h"'/>
  <Column id=interrupcoes_pico title="Interrupções no pico" fmt=num0/>
</DataTable>

## ♻️ Taxonomia de Wastes (Lean Six Sigma) — onde mais se desperdiça
> Desperdício medido por **tokens ponderados** (Defeito 2,0× · Cota 1,5× · Superproc. 1,0× · Latência 0,5×), não só por contagem.

<Grid cols=2>
<Group>

**Mix de waste do portfólio**
<ECharts config={{
  tooltip: { trigger: 'item', valueFormatter: (v) => Number(v).toLocaleString() + ' tok' },
  legend: { type: 'scroll', bottom: 0, textStyle: { fontSize: 9 } },
  series: [{
    type: 'pie', radius: ['45%','72%'], center: ['50%','42%'], roseType: 'radius',
    itemStyle: { borderRadius: 8, borderColor: '#fff', borderWidth: 2,
                 shadowBlur: 20, shadowColor: 'rgba(0,0,0,0.35)', shadowOffsetY: 8 },
    label: { formatter: '{d}%', fontSize: 10 },
    data: waste_mix.map(d => ({ name: d.categoria_waste, value: Number(d.waste_tokens) }))
  }]
}} />

</Group>
<Group>

**Waste dominante por projeto**
<DataTable data={waste_dom} rows=all>
  <Column id=project_name title="Projeto"/>
  <Column id=waste_dominante title="Waste dominante"/>
  <Column id=waste_tokens title="Tokens desperd." fmt=num0/>
</DataTable>

</Group>
</Grid>

<BarChart data={wastes} x=project_name y=waste_tokens series=categoria_waste type=stacked swapXY=true title="Composição de waste (tokens ponderados) por projeto"/>

## 🔬 RCA — Alucinação por Tipo de Prompt (o que ATRASA cada projeto)
> Root Cause Analysis: classificamos os prompts em **categorias** e medimos a alucinação de cada uma.
> Diagnóstico objetivo de **o que atrasa cada projeto** e **o que atrasa COMUMENTE a todos (interseção)**.

### 🎯 Interseção — o gargalo comum ao portfólio
> O tipo de prompt que é o **gargalo nº1 de alucinação** no maior número de projetos. Atacar este primeiro tem o maior efeito sistêmico.

<BarChart data={rca_inter} x=prompt_categoria y=projetos_onde_e_top1 title="Tipo de prompt que mais atrasa o portfólio (gargalo #1 em N projetos)" yAxisTitle="Nº de projetos onde é o gargalo #1" labels=true sort=true/>

### 🧭 Gargalo de alucinação por projeto (RCA individual)

<DataTable data={rca_proj} rows=all rowShading=true>
  <Column id=project_name title="Projeto"/>
  <Column id=prompt_gargalo title="Prompt que mais alucina (gargalo)"/>
  <Column id=alucinacoes title="Alucinações" fmt=num0/>
</DataTable>

### 📊 Taxonomia de alucinação por categoria × projeto

<BarChart data={aluc_cat} x=project_name y=alucinacoes series=prompt_categoria type=stacked swapXY=true title="Alucinações por tipo de prompt em cada projeto"/>

## 💰 VPL, Payback & Fluxo de Caixa do Portfólio
> Calculado a partir do **seu fluxo de caixa** (CSV/planilha — ver `pipeline/fluxo_caixa_template.csv` e
> `python3 carregar_fluxo.py SEU.csv`). VPL = Σ fluxo ÷ (1+i)ᵗ · Payback **simples** (variação temporal) e
> **descontado**, ambos interpolados. _Dados de demonstração até você fornecer o seu CSV._

<DataTable data={vpl} rows=all rowShading=true>
  <Column id=project_name title="Projeto"/>
  <Column id=vpl title="VPL (R$)" fmt='$#,##0' contentType=colorscale/>
  <Column id=tir title="TIR" fmt=pct1/>
  <Column id=ill title="ILL (PI)" fmt=num2/>
  <Column id=payback_simples title="PB simples" fmt=num2/>
  <Column id=payback_descontado title="PB descontado" fmt=num2/>
  <Column id=supera_selic title="TIR>SELIC?" fmt=boolean/>
  <Column id=supera_us title="TIR>EUA?" fmt=boolean/>
  <Column id=vpl_usd title="VPL US$" fmt='$#,##0'/>
  <Column id=payback_desc_usd title="PB desc. US$" fmt=num2/>
</DataTable>

> **TIR** = retorno do projeto · **ILL (PI)** acima de 1 = cria valor · comparados à **SELIC** e aos **juros dos EUA** (valores reais por projeto na tabela acima — colunas `TIR>SELIC?`/`TIR>EUA?`). O fluxo é **dolarizado** (USD/BRL) e descontado à taxa americana → colunas **VPL US$** e **PB desc. US$**. _Benchmarks (SELIC, juros EUA, câmbio) são placeholders — ajuste no `.env`._

**TIR por projeto vs. custo de oportunidade (SELIC × EUA)**

<BarChart data={vpl} x=project_name y=tir title="TIR por projeto comparada à SELIC e aos juros dos EUA" yAxisTitle="TIR (por período)" sort=true>
  <ReferenceLine y=0.105 color=warning label="SELIC (BR) ~10,5%"/>
  <ReferenceLine y=0.045 color=info label="Juros EUA ~4,5%"/>
</BarChart>

**Recuperação do investimento ao longo do tempo** (acumulado descontado — cruza zero = payback descontado)

<LineChart data={vpl_fluxo} x=periodo y=cum_desc series=project_name title="Fluxo de caixa acumulado descontado por período" yAxisTitle="Acumulado descontado (R$)" markers=true>
  <ReferenceLine y=0 color=negative label="break-even"/>
</LineChart>

---
## 🔗 Painéis Individuais por Projeto

{#each kpis as p}
<a href="/projetos/{p.project_name}">▶️ {p.project_name} — PSR {p.kpi_psr}</a>
{/each}
