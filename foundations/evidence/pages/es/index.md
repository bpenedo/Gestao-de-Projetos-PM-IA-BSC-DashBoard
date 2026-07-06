---
title: Panel BSC — Gestión de Proyectos (PM) de IA
---

🌐 [Português](/) · [English](/en) · **Español** · [Français](/fr) · [Deutsch](/de) · [中文](/zh) · [한국어](/ko) · [हिन्दी](/hi) · [עברית](/he) · [Svenska](/sv) · [Русский](/ru) · [Suomi](/fi)


🌐 **Português** · [English](/en) · [Español](/es) · [Français](/fr) · [Deutsch](/de) · [中文](/zh) · [한국어](/ko) · [हिन्दी](/hi)


_Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com_
**Checkpoint Semanal — todos los viernes a las 09:00.**

> ⚠️ **Datos DEMO** (portafolio anonimizado). Se vuelven reales cuando Langfuse sincroniza.

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
select * exclude (prompt_categoria), CASE prompt_categoria WHEN 'Conversa/Aberto' THEN 'Conversación/Abierto' WHEN 'RAG/Busca' THEN 'RAG/Búsqueda' WHEN 'Transformacao/Formato' THEN 'Transformación/Formato' WHEN 'Raciocinio/Analise' THEN 'Razonamiento/Análisis' WHEN 'Sumarizacao' THEN 'Resumen' WHEN 'Geracao de Codigo' THEN 'Generación de Código' WHEN 'Extracao de Dados' THEN 'Extracción de Datos' ELSE prompt_categoria END as prompt_categoria from bsc.alucinacao_categoria
```
```sql rca_proj
select * exclude (prompt_gargalo), CASE prompt_gargalo WHEN 'Conversa/Aberto' THEN 'Conversación/Abierto' WHEN 'RAG/Busca' THEN 'RAG/Búsqueda' WHEN 'Transformacao/Formato' THEN 'Transformación/Formato' WHEN 'Raciocinio/Analise' THEN 'Razonamiento/Análisis' WHEN 'Sumarizacao' THEN 'Resumen' WHEN 'Geracao de Codigo' THEN 'Generación de Código' WHEN 'Extracao de Dados' THEN 'Extracción de Datos' ELSE prompt_gargalo END as prompt_gargalo from bsc.rca_projeto
```
```sql rca_inter
select * exclude (prompt_categoria), CASE prompt_categoria WHEN 'Conversa/Aberto' THEN 'Conversación/Abierto' WHEN 'RAG/Busca' THEN 'RAG/Búsqueda' WHEN 'Transformacao/Formato' THEN 'Transformación/Formato' WHEN 'Raciocinio/Analise' THEN 'Razonamiento/Análisis' WHEN 'Sumarizacao' THEN 'Resumen' WHEN 'Geracao de Codigo' THEN 'Generación de Código' WHEN 'Extracao de Dados' THEN 'Extracción de Datos' ELSE prompt_categoria END as prompt_categoria from bsc.rca_intersecao
```
```sql vpl
select * from bsc.vpl_resultado
```
```sql vpl_fluxo
select * from bsc.vpl_fluxo
```
```sql planos
select * from bsc.planos_assinatura
```
```sql planos_pagos
select * from bsc.planos_assinatura where usd_mes > 0 order by total_iof desc
```
```sql mcda
select * from bsc.decisao_mcda order by rank_final
```
```sql mcda_top
select * from bsc.decisao_mcda where rank_final = 1
```

## 📈 Resumen Ejecutivo del Portafolio

<BigValue data={kpis} value=total_tokens title="Tokens Totales" agg=sum fmt=num0/>
<BigValue data={kpis} value=kpi_psr title="PSR promedio (0-5)" agg=mean fmt=num1/>
<BigValue data={kpis} value=kpi_idls_lean title="Desperdicio Lean promedio %" agg=mean fmt=num1/>
<BigValue data={kpis} value=burn_rate_ia title="Burn Rate total" agg=sum fmt='$#,##0.00'/>

## 🌐 Mapa 5D del Portafolio (visión C-Level)
> Esferas 3D estilo 5dchart — **5 dimensiones por proyecto**: **X**=Volumen/escala (tokens) · **Y**=PEUC/calidad (%) · **Z**=PSR/salud (0–5) · **tamaño**=Burn Rate (R$) · **color**=ICCA/sostenibilidad (🟢 sobre 3x cubre costo · 🔴 bajo 1x = pérdida).
>
> **Lectura de directorio:** el proyecto ideal está a la **derecha/fondo** (escala+calidad), **alto** (PSR) y **verde** (sostenible). Esfera **grande y roja** = mucho efectivo quemado sin cobertura → corregir antes de escalar.

![Mapa 5D do Portfólio de Projetos de IA](/5d_es.png?v=5)

### 🖱️ Mapa 5D Interactivo — pasa el mouse sobre cada esfera
> **X** = Tokens (escala) · **Y** = PEUC (%) · **tamaño** = PSR (0–5) · **color** = ICCA (🟢 sostenible · 🟠 límite · 🔴 pérdida). Al pasar el mouse por cada **esfera glossy**, aparece **Nombre del proyecto, PSR, PEUC y Tokens**.

<ECharts config={{
  tooltip: {
    trigger: 'item',
    backgroundColor: 'rgba(17,28,42,0.96)',
    borderColor: '#3a4a5e',
    borderWidth: 1,
    padding: 12,
    textStyle: { color: '#ffffff', fontSize: 14 },
    extraCssText: 'box-shadow:0 6px 24px rgba(0,0,0,.45);border-radius:8px;',
    formatter: (p) => {
      const d = p.data;
      return `<div style="font-size:16px;font-weight:700;margin-bottom:6px;color:#7ec8ff">${d.name}</div>`
        + `<div style="font-size:13px;line-height:1.6">`
        + `⭐ <b>PSR</b>: ${Number(d.psr).toFixed(2)} / 5<br/>`
        + `✅ <b>PEUC</b>: ${Number(d.peuc).toFixed(1)}%<br/>`
        + `🔢 <b>Tokens</b>: ${Number(d.tokens).toLocaleString('pt-BR')}`
        + `</div>`;
    }
  },
  grid: { left: 62, right: 40, top: 24, bottom: 58 },
  xAxis: {
    type: 'value', name: 'Tokens (escala) →', nameLocation: 'middle', nameGap: 34,
    scale: true, nameTextStyle: { fontSize: 12, fontWeight: 600 },
    axisLabel: { formatter: (v) => v >= 1000 ? (v/1000) + 'k' : v, fontSize: 11 },
    splitLine: { lineStyle: { color: 'rgba(140,150,165,0.18)' } }
  },
  yAxis: {
    type: 'value', name: 'PEUC (%)', min: 0, max: 100,
    nameTextStyle: { fontSize: 12, fontWeight: 600 },
    axisLabel: { fontSize: 11 },
    splitLine: { lineStyle: { color: 'rgba(140,150,165,0.18)' } }
  },
  series: [{
    type: 'scatter',
    data: kpis.map(d => {
      const icca = Number(d.kpi_icca) || 0;
      const psr = Number(d.kpi_psr) || 0;
      const base = icca >= 3 ? '#1f9d55' : (icca >= 1 ? '#e0a52b' : '#c0392b');
      const hi   = icca >= 3 ? '#8fe8b4' : (icca >= 1 ? '#ffdd93' : '#f2988f');
      return {
        name: d.project_name,
        value: [Number(d.total_tokens) || 0, Number(d.kpi_peuc) || 0],
        psr: psr, peuc: Number(d.kpi_peuc) || 0, tokens: Number(d.total_tokens) || 0,
        symbolSize: 16 + psr * 8,
        itemStyle: {
          color: { type: 'radial', x: 0.35, y: 0.30, r: 0.72,
                   colorStops: [ { offset: 0, color: hi }, { offset: 0.55, color: base }, { offset: 1, color: base } ] },
          borderColor: 'rgba(255,255,255,0.65)', borderWidth: 1,
          shadowBlur: 14, shadowColor: 'rgba(0,0,0,0.35)', shadowOffsetY: 6
        }
      };
    }),
    label: {
      show: true, formatter: (p) => p.data.name, position: 'top', distance: 7,
      fontSize: 14, fontWeight: 700, color: '#16222e',
      textBorderColor: 'rgba(255,255,255,0.95)', textBorderWidth: 3.5
    },
    labelLayout: { hideOverlap: false, moveOverlap: 'shiftY' },
    emphasis: {
      scale: 1.4, focus: 'self',
      itemStyle: { shadowBlur: 30, shadowColor: 'rgba(0,0,0,0.55)', borderColor: '#fff', borderWidth: 2 },
      label: { fontSize: 17, fontWeight: 'bold', color: '#000', textBorderColor: '#fff', textBorderWidth: 4 }
    }
  }]
}} />

## 📉 Tendencia del Indicador Maestro (CPP) y del Score (PSR)
> Lo que más importa al C-Level: **la dirección**. CPP bajando = portafolio más eficiente.

<LineChart data={tendencia} x=data_snapshot y=cpp_medio yAxisTitle="CPP médio (R$/%)" title="Costo por Punto de Progreso — tendencia del portafolio" markers=true/>

<LineChart data={tendencia} x=data_snapshot y=psr_medio yAxisTitle="PSR médio" yMin=0 yMax=5 title="Score promedio del portafolio (PSR 0-5)" markers=true/>

## ⭐ Score (PSR) por Proyecto

<BarChart data={kpis} x=project_name y=kpi_psr swapXY=true title="PSR (0-5) por proyecto — ordenado" sort=true labels=true/>

## 🍩 Composición y Mix (donut con profundidad)

<Grid cols=2>
<Group>

**Dónde se está quemando el efectivo de IA** (Burn Rate por proyecto)

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

**Mix global de fallas** (Pareto en donut)

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

## 🧭 Cuadrante de Sostenibilidad (¿escalar o corregir?)
> Eje X = **ICCA** (cobertura: sobre 3x = sano) · Eje Y = **IBMT** (quema marginal: bajo 0,33 = bueno) · tamaño = Burn Rate.
> Inferior derecha = **escalar con ganancia**; superior izquierda = **corregir antes de crecer**.

<ScatterPlot data={kpis} x=kpi_icca y=kpi_ibmt series=project_name size=burn_rate_ia xAxisTitle="ICCA — cobertura de custo (x)" yAxisTitle="IBMT — burn marginal (x)" title="Sostenibilidad financiera por proyecto"/>

## 📊 Pareto de Fallas por Proyecto

<BarChart data={falhas} x=project_name y=percentual_dominancia series=categoria_falha type=stacked100 swapXY=true title="Dominancia de fallas (%) por proyecto"/>

## 🗂️ Score y Salud Financiera (tabla)

<DataTable data={kpis} rows=all rowShading=true>
  <Column id=project_name title="Proyecto"/>
  <Column id=kpi_psr title="PSR" fmt=num2/>
  <Column id=kpi_peuc title="PEUC %" fmt=num1/>
  <Column id=kpi_iita title="IITA %" fmt=num1/>
  <Column id=kpi_idls_lean title="IDLS %" fmt=num1/>
  <Column id=vrt_por_ktoken title="VRT/kT" fmt='$#,##0.0000'/>
  <Column id=kpi_icca title="ICCA x" fmt=num2/>
  <Column id=kpi_ibmt title="IBMT x" fmt=num3/>
  <Column id=kpi_cpp title="CPP R$/%" fmt='$#,##0.00'/>
</DataTable>

## 🚨 Alertas Críticas

<DataTable data={alertas} rows=8>
  <Column id=project_name title="Proyecto"/>
  <Column id=tipo_erro title="Falla"/>
  <Column id=tokens_desperdicados title="Tokens" fmt=num0/>
  <Column id=data_evento title="Cuándo"/>
</DataTable>

## 📅 Agenda de la Reunión Semanal

<DataTable data={reuniao} rows=all>
  <Column id=project_name title="Proyecto"/>
  <Column id=sumario_executivo title="Resumen"/>
  <Column id=acoes_corretivas_lean title="Acciones Lean (PDCA)"/>
</DataTable>

## 🪙 Recuperación de Costos (VRT) — 5 bloques + promedio (2ª óptica)
> Misma base de prorrateo en **5 granularidades** (R$ por 50/100/250/500/1.000 tokens) + el **promedio de bloques** — una segunda percepción del consumo por proyecto.

<DataTable data={kpis} rows=all rowShading=true>
  <Column id=project_name title="Proyecto"/>
  <Column id=vrt_50t title="50 tok" fmt='#,##0.00000'/>
  <Column id=vrt_100t title="100 tok" fmt='#,##0.00000'/>
  <Column id=vrt_250t title="250 tok" fmt='#,##0.00000'/>
  <Column id=vrt_500t title="500 tok" fmt='#,##0.00000'/>
  <Column id=vrt_por_ktoken title="1.000 tok" fmt='#,##0.00000'/>
  <Column id=vrt_media_blocos title="PROM. bloques" fmt='#,##0.00000' contentType=colorscale/>
</DataTable>

## ⏰ Hora Crítica de Interrupción/Impacto (HCI)
> En qué **hora del día (BRT)** cada proyecto es más impactado — para actuar en la ventana correcta (upgrade de Tier, backoff, programación).

<BarChart data={hora_total} x=hora_brt y=interrupcoes title="Interrupciones por hora del día (BRT) — portafolio" xAxisTitle="Hora (0-23, BRT)"/>

<DataTable data={horario_critico} rows=all rowShading=true>
  <Column id=project_name title="Proyecto"/>
  <Column id=hora_pico title="Hora pico (BRT)" fmt='0"h"'/>
  <Column id=interrupcoes_pico title="Interrupciones en pico" fmt=num0/>
</DataTable>

## ♻️ Taxonomía de Desperdicios (Lean Six Sigma) — dónde se desperdicia más
> Desperdicio medido por **tokens ponderados** (Defecto 2,0× · Cuota 1,5× · Sobreproc. 1,0× · Latencia 0,5×), no solo por conteo.

<Grid cols=2>
<Group>

**Mix de desperdicio del portafolio**
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

**Desperdicio dominante por proyecto**
<DataTable data={waste_dom} rows=all>
  <Column id=project_name title="Proyecto"/>
  <Column id=waste_dominante title="Desperdicio dominante"/>
  <Column id=waste_tokens title="Tokens desperd." fmt=num0/>
</DataTable>

</Group>
</Grid>

<BarChart data={wastes} x=project_name y=waste_tokens series=categoria_waste type=stacked swapXY=true title="Composición de desperdicio (tokens ponderados) por proyecto"/>

## 🔬 RCA — Alucinación por Tipo de Prompt (qué RETRASA cada proyecto)
> Root Cause Analysis: clasificamos los prompts en **categorías** y medimos la alucinación de cada una.
> Diagnóstico objetivo de **qué retrasa cada proyecto** y **qué retrasa EN COMÚN a todos (intersección)**.

### 🎯 Intersección — el cuello de botella común al portafolio
> El tipo de prompt que es el **cuello de botella nº1 de alucinación** en el mayor número de proyectos. Atacar esto primero tiene el mayor efecto sistémico.

<BarChart data={rca_inter} x=prompt_categoria y=projetos_onde_e_top1 title="Tipo de prompt que más retrasa el portafolio (cuello de botella #1 en N proyectos)" yAxisTitle="Nº de projetos onde é o gargalo #1" labels=true sort=true/>

### 🧭 Cuello de botella de alucinación por proyecto (RCA individual)

<DataTable data={rca_proj} rows=all rowShading=true>
  <Column id=project_name title="Proyecto"/>
  <Column id=prompt_gargalo title="Prompt que más alucina (cuello de botella)"/>
  <Column id=alucinacoes title="Alucinaciones" fmt=num0/>
</DataTable>

### 📊 Taxonomía de alucinación por categoría × proyecto

<BarChart data={aluc_cat} x=project_name y=alucinacoes series=prompt_categoria type=stacked swapXY=true title="Alucinaciones por tipo de prompt en cada proyecto"/>

## 💰 VAN, Payback y Flujo de Caja del Portafolio
> Calculado a partir de **tu flujo de caja** (CSV/planilla — ver `pipeline/fluxo_caixa_template.csv` y `python3 carregar_fluxo.py TUYO.csv`). VAN = Σ flujo ÷ (1+i)ᵗ · Payback **simple** (variación temporal) y **descontado**, ambos interpolados. _Datos de demostración hasta que proporciones tu CSV._

<DataTable data={vpl} rows=all rowShading=true>
  <Column id=project_name title="Proyecto"/>
  <Column id=vpl title="VPL (R$)" fmt='$#,##0' contentType=colorscale/>
  <Column id=tir title="TIR" fmt=pct1/>
  <Column id=tirm title="TIRM" fmt=pct1/>
  <Column id=ill title="ILL (PI)" fmt=num2/>
  <Column id=vul title="VUL (R$)" fmt='$#,##0'/>
  <Column id=payback_simples title="PB simple" fmt=num2/>
  <Column id=payback_descontado title="PB descontado" fmt=num2/>
  <Column id=supera_selic title="TIR>SELIC?" fmt=boolean/>
  <Column id=supera_us title="TIR>EUA?" fmt=boolean/>
  <Column id=vpl_usd title="VPL US$" fmt='$#,##0'/>
  <Column id=payback_desc_usd title="PB desc. US$" fmt=num2/>
</DataTable>

> 🆕 **TIRM** (TIR Modificada) reinvierte las entradas a la tasa del proyecto — más realista que la TIR. **VUL** (Valor Uniforme Neto) convierte el VAN en una serie anual equivalente.

> **TIR** = retorno del proyecto · **ILL (PI)** por encima de 1 = crea valor · comparados con **SELIC** y con los **intereses de EE. UU.** (valores reales por proyecto en la tabla de arriba — columnas `TIR>SELIC?`/`TIR>EUA?`). El flujo está **dolarizado** (USD/BRL) y descontado a la tasa estadounidense → columnas **VPL US$** y **PB desc. US$**. _Los benchmarks (SELIC, interés EE. UU., cambio) son placeholders — ajusta en `.env`._

**TIR por proyecto vs. costo de oportunidad (SELIC × EE. UU.)**

<BarChart data={vpl} x=project_name y=tir title="TIR por proyecto vs. SELIC e intereses de EE. UU." yAxisTitle="TIR (por período)" sort=true>
  <ReferenceLine y=0.105 color=warning label="SELIC (BR) ~10,5%"/>
  <ReferenceLine y=0.045 color=info label="Interés EE. UU. ~4,5%"/>
</BarChart>

**Recuperación de la inversión en el tiempo** (acumulado descontado — cruza cero = payback descontado)

<LineChart data={vpl_fluxo} x=periodo y=cum_desc series=project_name title="Flujo de caja acumulado descontado por período" yAxisTitle="Acumulado descontado (R$)" markers=true>
  <ReferenceLine y=0 color=negative label="break-even"/>
</LineChart>

## 💳 Planes de Suscripción de IA — Costo Total con IOF
> Cambio **R$ 5,40/US$** · **IOF 3,5%** sobre operación internacional (tarjeta). `Total = US$ × cambio × (1 + IOF)`.
> Este es el costo real que alimenta la base de prorrateo (`assinaturas_infra`). Precios aproximados — verifica los sitios oficiales.

<DataTable data={planos} rows=all rowShading=true>
  <Column id=provedor title="Proveedor"/>
  <Column id=plano title="Plan"/>
  <Column id=usd_mes title="US$/mês" fmt=num0/>
  <Column id=r_base title="R$ base" fmt='$#,##0.00'/>
  <Column id=iof_reais title="IOF" fmt='$#,##0.00'/>
  <Column id=total_iof title="Total c/ IOF (R$)" fmt='$#,##0.00'/>
</DataTable>

<BarChart data={planos_pagos} x=plano y=total_iof title="Costo mensual total con IOF por plan (R$)" swapXY=true sort=true/>

<div style="display:flex;align-items:center;justify-content:center;gap:1rem;flex-wrap:wrap;margin:1.4rem 0 0.4rem;">
  <img src="/shark.svg" alt="tubarão investidor" width="120" height="82" style="flex:0 0 auto;"/>
  <h2 style="text-align:center;margin:0;font-weight:800;">🏆 AHP-TOPSIS 2N — Modelo de Decisión Multicriterio (MCDM)</h2>
  <img src="/gekko_photo.png" alt="Gordon Gekko fumando charuto (terno azul)" width="100" height="100" style="flex:0 0 auto;border-radius:50%;box-shadow:0 2px 8px rgba(0,0,0,.25);"/>
</div>

> **Elección del MEJOR proyecto** ponderando los indicadores como criterios. Pesos por **AHP**
> (VPL 37% · TIR 24% · ILL 14% · PSR 14% · IITA 5,6% · IDLS 5,6% — CR = 0,012, consistente).
> Ranking por **TOPSIS** en **dos normalizaciones** (vectorial/Euclidiana + min-max/lineal); el
> **Ci final** es el promedio. Columna **¿Robusto?** = ambas normalizaciones coinciden en la posición.

**🥇 Proyecto ganador (mayor Ci final):**
<DataTable data={mcda_top}>
  <Column id=project_name title="🏆 Mejor Proyecto"/>
  <Column id=ci_final title="Ci final" fmt=num4/>
</DataTable>

<BarChart data={mcda} x=project_name y=ci_final title="Ranking AHP-TOPSIS 2n (Ci final, 0–1)" swapXY=true sort=true labels=true/>

<DataTable data={mcda} rows=all rowShading=true>
  <Column id=rank_final title="#"/>
  <Column id=project_name title="Proyecto"/>
  <Column id=ci_vector title="Ci vetorial" fmt=num4/>
  <Column id=ci_minmax title="Ci min-max" fmt=num4/>
  <Column id=ci_final title="Ci final" fmt=num4/>
  <Column id=concordante title="¿Robusto?" fmt=boolean/>
</DataTable>

> El ganador tiene un **pitch deck** generado (ver carpeta Proyectos / `pitchdeck/`). Donde las posiciones 6–7 divergen entre normalizaciones, el ranking es más sensible — decide con cautela ahí.

### 📌 Bottom-Line — Resumen Ejecutivo e Insights C-Level

**Veredicto.** El modelo **AHP-TOPSIS 2n** elige a **{mcda_top[0].project_name}** como el mejor proyecto del portafolio (**Ci = 0,96** de 1,00), con **robustez confirmada**: ambas normalizaciones (vectorial y min-max) coinciden en el **1.º puesto** y en 8/10 del ranking — la cima es estable, no un artefacto del método.

**Por qué ganó {mcda_top[0].project_name}.** Los criterios **financieros** (VAN R$ 5.973 · TIR 32,9% · ILL 1,75) están **empatados** entre proyectos (flujo de caja aún en *placeholder* uniforme). Con lo financiero neutralizado, la decisión pasa a la **eficiencia operativa**, y ahí {mcda_top[0].project_name} domina: tiene la **menor tasa de alucinación (IITA 9,1%)** y el **menor desperdicio Lean (IDLS 15,0%)** del portafolio — casi **la mitad** del 2.º. En otras palabras: **mismo retorno proyectado, con mucho menos desperdicio de tokens/caja.**

**Insights C-Level.**
- 🥇 **La eficiencia es el desempate:** cuando el retorno es parecido, quien **quema menos** (menor IITA/IDLS) entrega el mismo valor con mayor margen — el activo más escalable.
- 🛡️ **Robustez decisoria:** la concordancia entre ambas normalizaciones (8/10) da **seguridad** al board para actuar en la cima del ranking; la zona sensible (posiciones 6–7) exige análisis cualitativo antes de cortar.
- 📉 **Cola de riesgo:** el último clasificado (Ci 0,01) reúne el peor desempeño combinado — candidato a **refactorización o discontinuación** (cruzar con la Matriz BCG).

**⚠️ Salvedad de honestidad decisoria.** Los criterios financieros cargan **75% del peso AHP** (VAN 37% + TIR 24% + ILL 14%), pero hoy **no diferencian** porque el flujo de caja es placeholder. **El veredicto solo es definitivo con los flujos de caja REALES por proyecto** — al ingresarlos, el ranking puede cambiar sustancialmente (lo financiero volverá a dominar).

**Recomendación.** (1) Aprobar {mcda_top[0].project_name} como **piloto de escala** por su eficiencia comprobada; (2) ingresar los **flujos de caja reales** y re-ejecutar `ahp_topsis.py` para el veredicto financiero definitivo; (3) activar un plan de mejora en la cola (el último clasificado).

---
## 👑 Dossier Administrativo de la **Joya de la Corona** — {mcda_top[0].project_name}

> Herramientas administrativas clásicas aplicadas **exclusivamente al proyecto electo** para enriquecerlo, enaltecerlo y evidenciar su **diferencial competitivo**. Todas se generan por **pipeline Python concurrente** (`gerar_admtools.py`) — sin ningún template externo. Detalle y justificación en `foundations/admtools/ferramentas_administrativas.md`.

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:1.2rem;margin:1rem 0;">

<div>

**🎯 SWOT — posición estratégica**
Fortalezas/debilidades/oportunidades/amenazas derivadas de KPIs reales (menor IITA e IDLS = fortaleza dominante).
<img src="/admtools/es/swot.png" alt="SWOT do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🌐 PESTELC — macroentorno**
Siete factores externos (Político, Económico, Social, Tecnológico, Ecológico, Legal, Cultural).
<img src="/admtools/es/pestel.png" alt="PESTELC do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🗺️ 5W4H — plan de acción (5W + 4H)**
What/Why/Where/When/Who + How/How much/How many/How long — hoja de ruta de escalado del electo.
<img src="/admtools/es/5w4h.png" alt="5W4H do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**📊 Pareto de fallas (80/20)**
Categorías de prompt que concentran 80% de las fallas — dónde atacar primero (datos reales de Langfuse).
<img src="/admtools/es/pareto.png" alt="Pareto de falhas do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🔥 Matriz GUT — priorización (heatmap)**
Gravedad × Urgencia × Tendencia de las acciones; mayor GUT = actuar primero.
<img src="/admtools/es/gut.png" alt="Matriz GUT do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🕸️ Radar competitivo — diferencial**
Huella del electo **vs promedio del portafolio** (el área azul domina la gris en casi todo eje).
<img src="/admtools/es/radar.png" alt="Radar competitivo do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>

</div>

> **📌 Lectura ejecutiva.** El **radar** retrata el diferencial competitivo: la Joya de la Corona supera la media en anti-alucinación, Lean y entrega útil. **SWOT/PESTEL/5W4H** convierten ese diagnóstico en **estrategia y plan de acción**; **Pareto + GUT** dicen **exactamente dónde** actuar primero para convertir el liderazgo operativo en retorno financiero definitivo.

---
## 🔗 Paneles Individuales por Proyecto

{#each kpis as p}
<a href="/es/projetos/{p.project_name}">▶️ {p.project_name} — PSR {p.kpi_psr}</a>
{/each}
