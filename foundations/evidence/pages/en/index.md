---
title: BSC Panel — AI Project Management (PM)
---

🌐 [Português](/) · **English** · [Español](/es) · [Français](/fr) · [Deutsch](/de) · [中文](/zh) · [한국어](/ko) · [हिन्दी](/hi) · [עברית](/he) · [Svenska](/sv) · [Русский](/ru) · [Suomi](/fi)


🌐 **Português** · [English](/en) · [Español](/es) · [Français](/fr) · [Deutsch](/de) · [中文](/zh) · [한국어](/ko) · [हिन्दी](/hi)


_Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com_
**Weekly Checkpoint — every Friday at 09:00.**

> ⚠️ **DEMO data** (anonymized portfolio). Becomes real once Langfuse syncs.

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
select * exclude (prompt_categoria), CASE prompt_categoria WHEN 'Conversa/Aberto' THEN 'Chat/Open' WHEN 'RAG/Busca' THEN 'RAG/Search' WHEN 'Transformacao/Formato' THEN 'Transformation/Format' WHEN 'Raciocinio/Analise' THEN 'Reasoning/Analysis' WHEN 'Sumarizacao' THEN 'Summarization' WHEN 'Geracao de Codigo' THEN 'Code Generation' WHEN 'Extracao de Dados' THEN 'Data Extraction' ELSE prompt_categoria END as prompt_categoria from bsc.alucinacao_categoria
```
```sql rca_proj
select * exclude (prompt_gargalo), CASE prompt_gargalo WHEN 'Conversa/Aberto' THEN 'Chat/Open' WHEN 'RAG/Busca' THEN 'RAG/Search' WHEN 'Transformacao/Formato' THEN 'Transformation/Format' WHEN 'Raciocinio/Analise' THEN 'Reasoning/Analysis' WHEN 'Sumarizacao' THEN 'Summarization' WHEN 'Geracao de Codigo' THEN 'Code Generation' WHEN 'Extracao de Dados' THEN 'Data Extraction' ELSE prompt_gargalo END as prompt_gargalo from bsc.rca_projeto
```
```sql rca_inter
select * exclude (prompt_categoria), CASE prompt_categoria WHEN 'Conversa/Aberto' THEN 'Chat/Open' WHEN 'RAG/Busca' THEN 'RAG/Search' WHEN 'Transformacao/Formato' THEN 'Transformation/Format' WHEN 'Raciocinio/Analise' THEN 'Reasoning/Analysis' WHEN 'Sumarizacao' THEN 'Summarization' WHEN 'Geracao de Codigo' THEN 'Code Generation' WHEN 'Extracao de Dados' THEN 'Data Extraction' ELSE prompt_categoria END as prompt_categoria from bsc.rca_intersecao
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

## 📈 Portfolio Executive Summary

<BigValue data={kpis} value=total_tokens title="Total Tokens" agg=sum fmt=num0/>
<BigValue data={kpis} value=kpi_psr title="Avg PSR (0-5)" agg=mean fmt=num1/>
<BigValue data={kpis} value=kpi_idls_lean title="Avg Lean Waste %" agg=mean fmt=num1/>
<BigValue data={kpis} value=burn_rate_ia title="Total Burn Rate" agg=sum fmt='$#,##0.00'/>

## 🌐 Portfolio 5D Map (C-Level view)
> 3D spheres (5dchart style) — **5 dimensions per project**: **X**=Volume/scale (tokens) · **Y**=PEUC/quality (%) · **Z**=PSR/health (0–5) · **size**=Burn Rate (R$) · **color**=ICCA/sustainability (🟢 above 3x covers cost · 🔴 below 1x = loss).
>
> **Board reading:** the ideal project sits **right/back** (scale+quality), **high** (PSR) and **green** (sustainable). A **large red** sphere = lots of cash burned without coverage → fix before scaling.

![Mapa 5D do Portfólio de Projetos de IA](/5d_en.png?v=5)

### 🖱️ Interactive 5D Map — hover over each sphere
> **X** = Tokens (scale) · **Y** = PEUC (%) · **size** = PSR (0–5) · **color** = ICCA (🟢 sustainable · 🟠 borderline · 🔴 loss). Hover over each **glossy sphere** to see **Project name, PSR, PEUC and Tokens**.

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

## 📉 Master Indicator (CPP) & Score (PSR) Trend
> What matters most to the C-Level: **the direction**. Falling CPP = portfolio getting more efficient.

<LineChart data={tendencia} x=data_snapshot y=cpp_medio yAxisTitle="CPP médio (R$/%)" title="Cost per Progress Point — portfolio trend" markers=true/>

<LineChart data={tendencia} x=data_snapshot y=psr_medio yAxisTitle="PSR médio" yMin=0 yMax=5 title="Portfolio avg score (PSR 0-5)" markers=true/>

## ⭐ Score (PSR) by Project

<BarChart data={kpis} x=project_name y=kpi_psr swapXY=true title="PSR (0-5) by project — sorted" sort=true labels=true/>

## 🍩 Composition & Mix (donut with depth)

<Grid cols=2>
<Group>

**Where AI cash is being burned** (Burn Rate by project)

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

**Global failure mix** (Pareto donut)

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

## 🧭 Sustainability Quadrant (scale or fix?)
> X axis = **ICCA** (coverage: above 3x = healthy) · Y axis = **IBMT** (marginal burn: below 0.33 = good) · size = Burn Rate.
> Bottom-right = **scale with profit**; top-left = **fix before growing**.

<ScatterPlot data={kpis} x=kpi_icca y=kpi_ibmt series=project_name size=burn_rate_ia xAxisTitle="ICCA — cobertura de custo (x)" yAxisTitle="IBMT — burn marginal (x)" title="Financial sustainability by project"/>

## 📊 Failure Pareto by Project

<BarChart data={falhas} x=project_name y=percentual_dominancia series=categoria_falha type=stacked100 swapXY=true title="Failure dominance (%) by project"/>

## 🗂️ Score & Financial Health (table)

<DataTable data={kpis} rows=all rowShading=true>
  <Column id=project_name title="Project"/>
  <Column id=kpi_psr title="PSR" fmt=num2/>
  <Column id=kpi_peuc title="PEUC %" fmt=num1/>
  <Column id=kpi_iita title="IITA %" fmt=num1/>
  <Column id=kpi_idls_lean title="IDLS %" fmt=num1/>
  <Column id=vrt_por_ktoken title="VRT/kT" fmt='$#,##0.0000'/>
  <Column id=kpi_icca title="ICCA x" fmt=num2/>
  <Column id=kpi_ibmt title="IBMT x" fmt=num3/>
  <Column id=kpi_cpp title="CPP R$/%" fmt='$#,##0.00'/>
</DataTable>

## 🚨 Critical Alerts

<DataTable data={alertas} rows=8>
  <Column id=project_name title="Project"/>
  <Column id=tipo_erro title="Failure"/>
  <Column id=tokens_desperdicados title="Tokens" fmt=num0/>
  <Column id=data_evento title="When"/>
</DataTable>

## 📅 Weekly Meeting Agenda

<DataTable data={reuniao} rows=all>
  <Column id=project_name title="Project"/>
  <Column id=sumario_executivo title="Summary"/>
  <Column id=acoes_corretivas_lean title="Lean Actions (PDCA)"/>
</DataTable>

## 🪙 Cost Recovery (VRT) — 5 blocks + average (2nd lens)
> Same allocation base at **5 granularities** (R$ per 50/100/250/500/1,000 tokens) + the **block average** — a second view of consumption per project.

<DataTable data={kpis} rows=all rowShading=true>
  <Column id=project_name title="Project"/>
  <Column id=vrt_50t title="50 tok" fmt='#,##0.00000'/>
  <Column id=vrt_100t title="100 tok" fmt='#,##0.00000'/>
  <Column id=vrt_250t title="250 tok" fmt='#,##0.00000'/>
  <Column id=vrt_500t title="500 tok" fmt='#,##0.00000'/>
  <Column id=vrt_por_ktoken title="1.000 tok" fmt='#,##0.00000'/>
  <Column id=vrt_media_blocos title="AVG blocks" fmt='#,##0.00000' contentType=colorscale/>
</DataTable>

## ⏰ Critical Interruption/Impact Hour (HCI)
> At which **hour of day (BRT)** each project is most impacted — to act in the right window (Tier upgrade, backoff, scheduling).

<BarChart data={hora_total} x=hora_brt y=interrupcoes title="Interruptions by hour of day (BRT) — portfolio" xAxisTitle="Hora (0-23, BRT)"/>

<DataTable data={horario_critico} rows=all rowShading=true>
  <Column id=project_name title="Project"/>
  <Column id=hora_pico title="Peak hour (BRT)" fmt='0"h"'/>
  <Column id=interrupcoes_pico title="Interruptions at peak" fmt=num0/>
</DataTable>

## ♻️ Waste Taxonomy (Lean Six Sigma) — where most is wasted
> Waste measured by **weighted tokens** (Defect 2.0× · Quota 1.5× · Overprocessing 1.0× · Latency 0.5×), not just by count.

<Grid cols=2>
<Group>

**Portfolio waste mix**
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

**Dominant waste by project**
<DataTable data={waste_dom} rows=all>
  <Column id=project_name title="Project"/>
  <Column id=waste_dominante title="Dominant waste"/>
  <Column id=waste_tokens title="Wasted tokens" fmt=num0/>
</DataTable>

</Group>
</Grid>

<BarChart data={wastes} x=project_name y=waste_tokens series=categoria_waste type=stacked swapXY=true title="Waste composition (weighted tokens) by project"/>

## 🔬 RCA — Hallucination by Prompt Type (what DELAYS each project)
> Root Cause Analysis: we classify prompts into **categories** and measure the hallucination of each.
> Objective diagnosis of **what delays each project** and **what COMMONLY delays them all (intersection)**.

### 🎯 Intersection — the bottleneck common to the portfolio
> The prompt type that is the **#1 hallucination bottleneck** across the most projects. Attacking this first has the greatest systemic effect.

<BarChart data={rca_inter} x=prompt_categoria y=projetos_onde_e_top1 title="Prompt type that most delays the portfolio (#1 bottleneck in N projects)" yAxisTitle="Nº de projetos onde é o gargalo #1" labels=true sort=true/>

### 🧭 Hallucination bottleneck per project (individual RCA)

<DataTable data={rca_proj} rows=all rowShading=true>
  <Column id=project_name title="Project"/>
  <Column id=prompt_gargalo title="Most-hallucinating prompt (bottleneck)"/>
  <Column id=alucinacoes title="Hallucinations" fmt=num0/>
</DataTable>

### 📊 Hallucination taxonomy by category × project

<BarChart data={aluc_cat} x=project_name y=alucinacoes series=prompt_categoria type=stacked swapXY=true title="Hallucinations by prompt type in each project"/>

## 💰 NPV, Payback & Portfolio Cash Flow
> Computed from **your cash flow** (CSV/spreadsheet — see `pipeline/fluxo_caixa_template.csv` and `python3 carregar_fluxo.py YOURS.csv`). NPV = Σ flow ÷ (1+i)ᵗ · Payback **simple** (temporal variation) and **discounted**, both interpolated. _Demo data until you provide your CSV._

<DataTable data={vpl} rows=all rowShading=true>
  <Column id=project_name title="Project"/>
  <Column id=vpl title="VPL (R$)" fmt='$#,##0' contentType=colorscale/>
  <Column id=tir title="TIR" fmt=pct1/>
  <Column id=tirm title="TIRM" fmt=pct1/>
  <Column id=ill title="ILL (PI)" fmt=num2/>
  <Column id=vul title="VUL (R$)" fmt='$#,##0'/>
  <Column id=payback_simples title="Simple PB" fmt=num2/>
  <Column id=payback_descontado title="Discounted PB" fmt=num2/>
  <Column id=supera_selic title="TIR>SELIC?" fmt=boolean/>
  <Column id=supera_us title="TIR>EUA?" fmt=boolean/>
  <Column id=vpl_usd title="VPL US$" fmt='$#,##0'/>
  <Column id=payback_desc_usd title="PB desc. US$" fmt=num2/>
</DataTable>

> 🆕 **TIRM** (Modified IRR) reinvests inflows at the project rate — more realistic than IRR. **VUL** (Net Uniform Value) converts NPV into an equivalent annual series.

> **TIR** = project return · **ILL (PI)** above 1 = creates value · compared to **SELIC** and the **US interest rate** (real per-project values in the table above — columns `TIR>SELIC?`/`TIR>EUA?`). The flow is **dollarized** (USD/BRL) and discounted at the US rate → columns **VPL US$** and **PB desc. US$**. _Benchmarks (SELIC, US rate, FX) are placeholders — adjust in `.env`._

**IRR by project vs. opportunity cost (SELIC × US)**

<BarChart data={vpl} x=project_name y=tir title="TIR by project vs. SELIC and US interest" yAxisTitle="TIR (per period)" sort=true>
  <ReferenceLine y=0.105 color=warning label="SELIC (BR) ~10,5%"/>
  <ReferenceLine y=0.045 color=info label="US interest ~4.5%"/>
</BarChart>

**Investment recovery over time** (discounted cumulative — crossing zero = discounted payback)

<LineChart data={vpl_fluxo} x=periodo y=cum_desc series=project_name title="Discounted cumulative cash flow per period" yAxisTitle="Discounted cumulative (R$)" markers=true>
  <ReferenceLine y=0 color=negative label="break-even"/>
</LineChart>

## 💳 AI Subscription Plans — Total Cost with IOF
> FX **R$ 5.40/US$** · **IOF 3.5%** on international operations (card). `Total = US$ × FX × (1 + IOF)`.
> This is the real cost feeding the allocation base (`assinaturas_infra`). Approximate prices — check official sites.

<DataTable data={planos} rows=all rowShading=true>
  <Column id=provedor title="Provider"/>
  <Column id=plano title="Plan"/>
  <Column id=usd_mes title="US$/mês" fmt=num0/>
  <Column id=r_base title="R$ base" fmt='$#,##0.00'/>
  <Column id=iof_reais title="IOF" fmt='$#,##0.00'/>
  <Column id=total_iof title="Total c/ IOF (R$)" fmt='$#,##0.00'/>
</DataTable>

<BarChart data={planos_pagos} x=plano y=total_iof title="Total monthly cost with IOF per plan (R$)" swapXY=true sort=true/>

<div style="display:flex;align-items:center;justify-content:center;gap:1rem;flex-wrap:wrap;margin:1.4rem 0 0.4rem;">
  <img src="/shark.svg" alt="tubarão investidor" width="120" height="82" style="flex:0 0 auto;"/>
  <h2 style="text-align:center;margin:0;font-weight:800;">🏆 AHP-TOPSIS 2N — Multi-Criteria Decision Model (MCDM)</h2>
  <img src="/gekko_photo.png" alt="Gordon Gekko fumando charuto (terno azul)" width="100" height="100" style="flex:0 0 auto;border-radius:50%;box-shadow:0 2px 8px rgba(0,0,0,.25);"/>
</div>

> **Choosing the BEST project** by weighting the indicators as criteria. Weights via **AHP**
> (VPL 37% · TIR 24% · ILL 14% · PSR 14% · IITA 5,6% · IDLS 5,6% — CR = 0,012, consistente).
> Ranking by **TOPSIS** in **two normalizations** (vector/Euclidean + min-max/linear); the
> **Final Ci** is the average. **Robust?** column = both normalizations agree on the position.

**🥇 Winning project (highest final Ci):**
<DataTable data={mcda_top}>
  <Column id=project_name title="🏆 Best Project"/>
  <Column id=ci_final title="Ci final" fmt=num4/>
</DataTable>

<BarChart data={mcda} x=project_name y=ci_final title="Ranking AHP-TOPSIS 2n (Ci final, 0–1)" swapXY=true sort=true labels=true/>

<DataTable data={mcda} rows=all rowShading=true>
  <Column id=rank_final title="#"/>
  <Column id=project_name title="Project"/>
  <Column id=ci_vector title="Ci vetorial" fmt=num4/>
  <Column id=ci_minmax title="Ci min-max" fmt=num4/>
  <Column id=ci_final title="Ci final" fmt=num4/>
  <Column id=concordante title="Robust?" fmt=boolean/>
</DataTable>

> The winner has a **pitch deck** generated (see the Projects folder / `pitchdeck/`). Where positions 6–7 diverge between normalizations, the ranking is most sensitive — decide with caution there.

### 📌 Bottom-Line — Executive Summary & C-Level Insights

**Verdict.** The **AHP-TOPSIS 2n** model elects **{mcda_top[0].project_name}** as the portfolio's best project (**Ci = 0.96** of 1.00), with **confirmed robustness**: both normalizations (vector and min-max) agree on **1st place** and on 8/10 of the ranking — the top is stable, not a method artifact.

**Why {mcda_top[0].project_name} won.** The **financial** criteria (NPV R$ 5,973 · IRR 32.9% · PI 1.75) are **tied** across projects (cash flow still a uniform *placeholder*). With finance neutralized, the decision shifts to **operational efficiency**, and there {mcda_top[0].project_name} dominates: it has the **lowest hallucination rate (IITA 9.1%)** and the **lowest Lean waste (IDLS 15.0%)** in the whole portfolio — nearly **half** the runner-up's waste. In other words: **same projected return, running with far less token/cash waste.**

**C-Level insights.**
- 🥇 **Efficiency is the tiebreaker:** when returns are similar, whoever **burns less** (lower IITA/IDLS) delivers the same value at higher margin — the most scalable asset.
- 🛡️ **Decision robustness:** agreement between both normalizations (8/10) gives the board **confidence** to act at the top of the ranking; the sensitive zone (positions 6–7) requires qualitative analysis before cutting.
- 📉 **Risk tail:** the last-ranked project (Ci 0.01) has the worst combined performance — a candidate for **refactoring or discontinuation** (cross-check with the BCG Matrix).

**⚠️ Decision-honesty caveat.** The financial criteria carry **75% of the AHP weight** (NPV 37% + IRR 24% + PI 14%), but today they **don't differentiate** because cash flow is a placeholder. **The verdict is only definitive with REAL per-project cash flows** — once entered, the ranking may change substantially (finance will dominate again).

**Recommendation.** (1) Approve {mcda_top[0].project_name} as a **scale-up pilot** for its proven efficiency; (2) enter the **real cash flows** and re-run `ahp_topsis.py` for the definitive financial verdict; (3) trigger an improvement plan on the tail (the last-ranked project).

---
## 👑 Administrative Dossier of the **Crown Jewel** — {mcda_top[0].project_name}

> Classic administrative tools applied **exclusively to the elected project** to enrich it, elevate it and highlight its **competitive edge**. All are generated by a **concurrent Python pipeline** (`gerar_admtools.py`) — with no external template. Details and rationale in `foundations/admtools/ferramentas_administrativas.md`.

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:1.2rem;margin:1rem 0;">

<div>

**🎯 SWOT — strategic position**
Strengths/weaknesses/opportunities/threats derived from real KPIs (lowest IITA and IDLS = dominant strength).
<img src="/admtools/en/swot.png" alt="SWOT do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🌐 PESTELC — macro-environment**
Seven external factors (Political, Economic, Social, Technological, Ecological, Legal, Cultural).
<img src="/admtools/en/pestel.png" alt="PESTELC do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🗺️ 5W4H — action plan (5W + 4H)**
What/Why/Where/When/Who + How/How much/How many/How long — the elected project's scale-up roadmap.
<img src="/admtools/en/5w4h.png" alt="5W4H do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**📊 Failure Pareto (80/20)**
Prompt categories concentrating 80% of failures — where to attack first (real Langfuse data).
<img src="/admtools/en/pareto.png" alt="Pareto de falhas do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🔥 GUT Matrix — prioritization (heatmap)**
Severity × Urgency × Tendency of actions; higher GUT = act first.
<img src="/admtools/en/gut.png" alt="Matriz GUT do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🕸️ Competitive radar — differentiator**
The elected project's fingerprint **vs portfolio average** (the blue area dominates the gray on almost every axis).
<img src="/admtools/en/radar.png" alt="Radar competitivo do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>

</div>

> **📌 Executive read.** The **radar** portrays the competitive edge: the Crown Jewel beats the average in anti-hallucination, Lean and useful delivery. **SWOT/PESTEL/5W4H** turn this diagnosis into **strategy and an action plan**; **Pareto + GUT** say **exactly where** to act first to convert operational leadership into a definitive financial return.

---
## 🔗 Individual Panels by Project

{#each kpis as p}
<a href="/en/projetos/{p.project_name}">▶️ {p.project_name} — PSR {p.kpi_psr}</a>
{/each}
