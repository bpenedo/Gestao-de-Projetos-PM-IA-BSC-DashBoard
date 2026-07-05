---
title: BSC-panel — AI-projektledning (PM)
---

🌐 [Português](/) · [English](/en) · [Español](/es) · [Français](/fr) · [Deutsch](/de) · [中文](/zh) · [한국어](/ko) · [हिन्दी](/hi) · [עברית](/he) · **Svenska** · [Русский](/ru) · [Suomi](/fi)


🌐 **Português** · [English](/en) · [Español](/es) · [Français](/fr) · [Deutsch](/de) · [中文](/zh) · [한국어](/ko) · [हिन्दी](/hi)


_Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com_
**Veckoavstämning — varje fredag kl. 09:00.**

> ⚠️ **DEMO-data** (anonymiserad portfölj). Blir verkliga när Langfuse synkroniserar.

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

## 📈 Portföljens sammanfattning

<BigValue data={kpis} value=total_tokens title="Totala tokens" agg=sum fmt=num0/>
<BigValue data={kpis} value=kpi_psr title="Snitt-PSR (0-5)" agg=mean fmt=num1/>
<BigValue data={kpis} value=kpi_idls_lean title="Snitt Lean-slöseri %" agg=mean fmt=num1/>
<BigValue data={kpis} value=burn_rate_ia title="Total Burn Rate" agg=sum fmt='$#,##0.00'/>

## 🌐 5D-karta över portföljen (C-nivå)
> 3D-sfärer (5dchart-stil) — **5 dimensioner per projekt**: **X**=Volym/skala (tokens) · **Y**=PEUC/kvalitet (%) · **Z**=PSR/hälsa (0–5) · **storlek**=Burn Rate (R$) · **färg**=ICCA/hållbarhet (🟢 över 3x täcker kostnad · 🔴 under 1x = förlust).
>
> **Styrelseläsning:** det ideala projektet ligger **höger/bak** (skala+kvalitet), **högt** (PSR) och **grönt** (hållbart). En **stor röd** sfär = mycket bränd kassa utan täckning → åtgärda före uppskalning.

![Mapa 5D do Portfólio de Projetos de IA](/5d_projetos.png?v=5)

### 🖱️ Interaktiv 5D-karta — hovra över varje sfär
> **X** = Tokens (skala) · **Y** = PEUC (%) · **storlek** = PSR (0–5) · **färg** = ICCA (🟢 hållbar · 🟠 gräns · 🔴 förlust). Hovra över varje **glansig sfär** för att se **Projektnamn, PSR, PEUC och Tokens**.

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

## 📉 Trend för nyckelindikator (CPP) och poäng (PSR)
> Det viktigaste för C-nivån: **riktningen**. Fallande CPP = portföljen blir effektivare.

<LineChart data={tendencia} x=data_snapshot y=cpp_medio yAxisTitle="CPP médio (R$/%)" title="Kostnad per framstegspoäng — portföljtrend" markers=true/>

<LineChart data={tendencia} x=data_snapshot y=psr_medio yAxisTitle="PSR médio" yMin=0 yMax=5 title="Portföljens snittpoäng (PSR 0-5)" markers=true/>

## ⭐ Poäng (PSR) per projekt

<BarChart data={kpis} x=project_name y=kpi_psr swapXY=true title="PSR (0-5) per projekt — sorterat" sort=true labels=true/>

## 🍩 Sammansättning & mix (donut med djup)

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

## 🧭 Hållbarhetskvadrant (skala upp eller åtgärda?)
> X-axel = **ICCA** (täckning: över 3x = sund) · Y-axel = **IBMT** (marginell burn: under 0,33 = bra) · storlek = Burn Rate.
> Nedre högra = **skala med vinst**; övre vänstra = **åtgärda före tillväxt**.

<ScatterPlot data={kpis} x=kpi_icca y=kpi_ibmt series=project_name size=burn_rate_ia xAxisTitle="ICCA — cobertura de custo (x)" yAxisTitle="IBMT — burn marginal (x)" title="Finansiell hållbarhet per projekt"/>

## 📊 Felpareto per projekt

<BarChart data={falhas} x=project_name y=percentual_dominancia series=categoria_falha type=stacked100 swapXY=true title="Feldominans (%) per projekt"/>

## 🗂️ Poäng & finansiell hälsa (tabell)

<DataTable data={kpis} rows=all rowShading=true>
  <Column id=project_name title="Projekt"/>
  <Column id=kpi_psr title="PSR" fmt=num2/>
  <Column id=kpi_peuc title="PEUC %" fmt=num1/>
  <Column id=kpi_iita title="IITA %" fmt=num1/>
  <Column id=kpi_idls_lean title="IDLS %" fmt=num1/>
  <Column id=vrt_por_ktoken title="VRT/kT" fmt='$#,##0.0000'/>
  <Column id=kpi_icca title="ICCA x" fmt=num2/>
  <Column id=kpi_ibmt title="IBMT x" fmt=num3/>
  <Column id=kpi_cpp title="CPP R$/%" fmt='$#,##0.00'/>
</DataTable>

## 🚨 Kritiska varningar

<DataTable data={alertas} rows=8>
  <Column id=project_name title="Projekt"/>
  <Column id=tipo_erro title="Fel"/>
  <Column id=tokens_desperdicados title="Tokens" fmt=num0/>
  <Column id=data_evento title="När"/>
</DataTable>

## 📅 Agenda för veckomötet

<DataTable data={reuniao} rows=all>
  <Column id=project_name title="Projekt"/>
  <Column id=sumario_executivo title="Sammanf."/>
  <Column id=acoes_corretivas_lean title="Lean-åtgärder (PDCA)"/>
</DataTable>

## 🪙 Kostnadsåtervinning (VRT) — 5 block + medel (andra vyn)
> Samma fördelningsbas i **5 granulariteter** (R$ per 50/100/250/500/1 000 tokens) + **blockmedelvärdet** — en andra bild av förbrukningen per projekt.

<DataTable data={kpis} rows=all rowShading=true>
  <Column id=project_name title="Projekt"/>
  <Column id=vrt_50t title="50 tok" fmt='#,##0.00000'/>
  <Column id=vrt_100t title="100 tok" fmt='#,##0.00000'/>
  <Column id=vrt_250t title="250 tok" fmt='#,##0.00000'/>
  <Column id=vrt_500t title="500 tok" fmt='#,##0.00000'/>
  <Column id=vrt_por_ktoken title="1.000 tok" fmt='#,##0.00000'/>
  <Column id=vrt_media_blocos title="MEDEL block" fmt='#,##0.00000' contentType=colorscale/>
</DataTable>

## ⏰ Kritisk avbrotts-/påverkanstimme (HCI)
> Vid vilken **timme på dygnet (BRT)** varje projekt påverkas mest — för att agera i rätt fönster (Tier-uppgradering, backoff, schemaläggning).

<BarChart data={hora_total} x=hora_brt y=interrupcoes title="Avbrott per timme på dygnet (BRT) — portfölj" xAxisTitle="Hora (0-23, BRT)"/>

<DataTable data={horario_critico} rows=all rowShading=true>
  <Column id=project_name title="Projekt"/>
  <Column id=hora_pico title="Topptimme (BRT)" fmt='0"h"'/>
  <Column id=interrupcoes_pico title="Avbrott vid topp" fmt=num0/>
</DataTable>

## ♻️ Slöseritaxonomi (Lean Six Sigma) — var mest slöseri sker
> Slöseri mätt i **viktade tokens** (Defekt 2,0× · Kvot 1,5× · Överbearbetning 1,0× · Latens 0,5×), inte bara antal.

<Grid cols=2>
<Group>

**Portföljens slöserimix**
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

**Dominant slöseri per projekt**
<DataTable data={waste_dom} rows=all>
  <Column id=project_name title="Projekt"/>
  <Column id=waste_dominante title="Dominant slöseri"/>
  <Column id=waste_tokens title="Slösade tokens" fmt=num0/>
</DataTable>

</Group>
</Grid>

<BarChart data={wastes} x=project_name y=waste_tokens series=categoria_waste type=stacked swapXY=true title="Slöserisammansättning (viktade tokens) per projekt"/>

## 🔬 RCA — hallucination per prompttyp (vad som FÖRSENAR varje projekt)
> Root Cause Analysis: vi klassificerar prompterna i **kategorier** och mäter hallucinationen för var och en.
> Objektiv diagnos av **vad som försenar varje projekt** och **vad som GEMENSAMT försenar alla (skärning)**.

### 🎯 Skärning — flaskhalsen gemensam för portföljen
> Prompttypen som är **hallucinationsflaskhals nr 1** i flest projekt. Att angripa den först ger störst systemisk effekt.

<BarChart data={rca_inter} x=prompt_categoria y=projetos_onde_e_top1 title="Prompttyp som mest försenar portföljen (flaskhals #1 i N projekt)" yAxisTitle="Nº de projetos onde é o gargalo #1" labels=true sort=true/>

### 🧭 Hallucinationsflaskhals per projekt (individuell RCA)

<DataTable data={rca_proj} rows=all rowShading=true>
  <Column id=project_name title="Projekt"/>
  <Column id=prompt_gargalo title="Mest hallucinerande prompt (flaskhals)"/>
  <Column id=alucinacoes title="Hallucinationer" fmt=num0/>
</DataTable>

### 📊 Hallucinationstaxonomi per kategori × projekt

<BarChart data={aluc_cat} x=project_name y=alucinacoes series=prompt_categoria type=stacked swapXY=true title="Hallucinationer per prompttyp i varje projekt"/>

## 💰 NPV, återbetalning & portföljens kassaflöde
> Beräknat från **ditt kassaflöde** (CSV/kalkylark — se `pipeline/fluxo_caixa_template.csv` och `python3 carregar_fluxo.py DITT.csv`). NPV = Σ flöde ÷ (1+i)ᵗ · Payback **enkel** (tidsvariation) och **diskonterad**, båda interpolerade. _Demodata tills du tillhandahåller din CSV._

<DataTable data={vpl} rows=all rowShading=true>
  <Column id=project_name title="Projekt"/>
  <Column id=vpl title="VPL (R$)" fmt='$#,##0' contentType=colorscale/>
  <Column id=tir title="TIR" fmt=pct1/>
  <Column id=tirm title="TIRM" fmt=pct1/>
  <Column id=ill title="ILL (PI)" fmt=num2/>
  <Column id=vul title="VUL (R$)" fmt='$#,##0'/>
  <Column id=payback_simples title="Enkel PB" fmt=num2/>
  <Column id=payback_descontado title="Diskonterad PB" fmt=num2/>
  <Column id=supera_selic title="TIR>SELIC?" fmt=boolean/>
  <Column id=supera_us title="TIR>EUA?" fmt=boolean/>
  <Column id=vpl_usd title="VPL US$" fmt='$#,##0'/>
  <Column id=payback_desc_usd title="PB desc. US$" fmt=num2/>
</DataTable>

> 🆕 **TIRM** (modifierad IRR) återinvesterar inflöden till projektets ränta — mer realistiskt än IRR. **VUL** (jämnt nettovärde) omvandlar NPV till en likvärdig årlig serie.

> **TIR** = retorno do projeto · **ILL (PI)** acima de 1 = cria valor · comparados à **SELIC** e aos **juros dos EUA** (valores reais por projeto na tabela acima — colunas `TIR>SELIC?`/`TIR>EUA?`). O fluxo é **dolarizado** (USD/BRL) e descontado à taxa americana → colunas **VPL US$** e **PB desc. US$**. _Benchmarks (SELIC, juros EUA, câmbio) são placeholders — ajuste no `.env`._

**IRR per projekt vs. alternativkostnad (SELIC × USA)**

<BarChart data={vpl} x=project_name y=tir title="TIR por projeto comparada à SELIC e aos juros dos EUA" yAxisTitle="TIR (por período)" sort=true>
  <ReferenceLine y=0.105 color=warning label="SELIC (BR) ~10,5%"/>
  <ReferenceLine y=0.045 color=info label="Juros EUA ~4,5%"/>
</BarChart>

**Recuperação do investimento ao longo do tempo** (acumulado descontado — cruza zero = payback descontado)

<LineChart data={vpl_fluxo} x=periodo y=cum_desc series=project_name title="Fluxo de caixa acumulado descontado por período" yAxisTitle="Acumulado descontado (R$)" markers=true>
  <ReferenceLine y=0 color=negative label="break-even"/>
</LineChart>

## 💳 AI-abonnemang — total kostnad med IOF
> Växelkurs **R$ 5,40/US$** · **IOF 3,5%** på internationell transaktion (kort). `Total = US$ × kurs × (1 + IOF)`.
> Detta är den verkliga kostnaden som matar fördelningsbasen (`assinaturas_infra`). Ungefärliga priser — kontrollera officiella sidor.

<DataTable data={planos} rows=all rowShading=true>
  <Column id=provedor title="Leverantör"/>
  <Column id=plano title="Plan"/>
  <Column id=usd_mes title="US$/mês" fmt=num0/>
  <Column id=r_base title="R$ base" fmt='$#,##0.00'/>
  <Column id=iof_reais title="IOF" fmt='$#,##0.00'/>
  <Column id=total_iof title="Total c/ IOF (R$)" fmt='$#,##0.00'/>
</DataTable>

<BarChart data={planos_pagos} x=plano y=total_iof title="Custo total mensal com IOF por plano (R$)" swapXY=true sort=true/>

<div style="display:flex;align-items:center;justify-content:center;gap:1rem;flex-wrap:wrap;margin:1.4rem 0 0.4rem;">
  <img src="/shark.svg" alt="tubarão investidor" width="120" height="82" style="flex:0 0 auto;"/>
  <h2 style="text-align:center;margin:0;font-weight:800;">🏆 AHP-TOPSIS 2N — flerkriteriebeslutsmodell (MCDM)</h2>
  <img src="/gekko_photo.png" alt="Gordon Gekko fumando charuto (terno azul)" width="100" height="100" style="flex:0 0 auto;border-radius:50%;box-shadow:0 2px 8px rgba(0,0,0,.25);"/>
</div>

> **Val av det BÄSTA projektet** genom att vikta indikatorerna som kriterier. Vikter via **AHP**
> (VPL 37% · TIR 24% · ILL 14% · PSR 14% · IITA 5,6% · IDLS 5,6% — CR = 0,012, consistente).
> Ranking por **TOPSIS** em **duas normalizações** (vetorial/Euclidiana + min-max/linear); o
> **Slutlig Ci** är medelvärdet. Kolumnen **Robust?** = båda normaliseringarna är överens om positionen.

**🥇 Vinnande projekt (högsta slutliga Ci):**
<DataTable data={mcda_top}>
  <Column id=project_name title="🏆 Bästa projekt"/>
  <Column id=ci_final title="Ci final" fmt=num4/>
</DataTable>

<BarChart data={mcda} x=project_name y=ci_final title="Ranking AHP-TOPSIS 2n (Ci final, 0–1)" swapXY=true sort=true labels=true/>

<DataTable data={mcda} rows=all rowShading=true>
  <Column id=rank_final title="#"/>
  <Column id=project_name title="Projekt"/>
  <Column id=ci_vector title="Ci vetorial" fmt=num4/>
  <Column id=ci_minmax title="Ci min-max" fmt=num4/>
  <Column id=ci_final title="Ci final" fmt=num4/>
  <Column id=concordante title="Robust?" fmt=boolean/>
</DataTable>

> Vinnaren har ett genererat **pitch deck** (se mappen Projekt / `pitchdeck/`). Där positionerna 6–7 skiljer sig mellan normaliseringar är rankingen känsligast — besluta med försiktighet där.

### 📌 Slutsats — sammanfattning & insikter för C-nivå

**Utlåtande.** Modellen **AHP-TOPSIS 2n** väljer **{mcda_top[0].project_name}** som portföljens bästa projekt (**Ci = 0,96** av 1,00), med **bekräftad robusthet**: båda normaliseringarna (vektor och min-max) är överens om **1:a platsen** och om 8/10 av rankingen — toppen är stabil, inte en metodartefakt.

**Varför {mcda_top[0].project_name} vann.** De **finansiella** kriterierna (NPV R$ 5 973 · IRR 32,9% · ILL 1,75) är **lika** mellan projekten (kassaflödet fortfarande en enhetlig *platshållare*). Med det finansiella neutraliserat flyttas beslutet till **operativ effektivitet**, och där dominerar {mcda_top[0].project_name}: lägst **hallucinationsgrad (IITA 9,1%)** och lägst **Lean-slöseri (IDLS 15,0%)** i hela portföljen — nästan **hälften** av tvåans. Med andra ord: **samma projicerade avkastning, med långt mindre token-/kassaslöseri.**

**Insikter för C-nivå.**
- 🥇 **Effektivitet är avgörande:** vid liknande avkastning levererar den som **bränner mindre** (lägre IITA/IDLS) samma värde med högre marginal — den mest skalbara tillgången.
- 🛡️ **Beslutsrobusthet:** samstämmigheten mellan de två normaliseringarna (8/10) ger styrelsen **trygghet** att agera i toppen av rankingen; den känsliga zonen (positioner 6–7) kräver kvalitativ analys innan man skär.
- 📉 **Risksvans:** den sist rankade (Ci 0,01) har sämst kombinerad prestanda — kandidat för **refaktorering eller avveckling** (korskolla mot BCG-matrisen).

**⚠️ Förbehåll om beslutsärlighet.** De finansiella kriterierna bär **75% av AHP-vikten** (NPV 37% + IRR 24% + ILL 14%), men idag **särskiljer de inte** eftersom kassaflödet är en platshållare. **Utlåtandet är definitivt först med VERKLIGA kassaflöden per projekt** — när de anges kan rankingen ändras väsentligt (det finansiella dominerar igen).

**Rekommendation.** (1) Godkänn {mcda_top[0].project_name} som **uppskalningspilot** för dess bevisade effektivitet; (2) ange de **verkliga kassaflödena** och kör `ahp_topsis.py` igen för det definitiva finansiella utlåtandet; (3) initiera en förbättringsplan för svansen (den sist rankade).

---
## 👑 Administrativt dossier för **Kronjuvelen** — {mcda_top[0].project_name}

> Klassiska administrativa verktyg tillämpade **uteslutande på det utvalda projektet** för att berika, lyfta fram och visa dess **konkurrensfördel**. Alla genereras av en **samtidig Python-pipeline** (`gerar_admtools.py`) — utan någon extern mall. Detaljer och motivering i `foundations/admtools/ferramentas_administrativas.md`.

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:1.2rem;margin:1rem 0;">

<div>

**🎯 SWOT — strategisk position**
Styrkor/svagheter/möjligheter/hot härledda från verkliga KPI:er (lägst IITA och IDLS = dominerande styrka).
<img src="/admtools/swot.png" alt="SWOT do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🌐 PESTELC — makromiljö**
Sju externa faktorer (Politiska, Ekonomiska, Sociala, Teknologiska, Ekologiska, Legala, Kulturella).
<img src="/admtools/pestel.png" alt="PESTELC do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🗺️ 5W4H — handlingsplan (5W + 4H)**
What/Why/Where/When/Who + How/How much/How many/How long — det utvalda projektets uppskalningsplan.
<img src="/admtools/5w4h.png" alt="5W4H do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**📊 Felpareto (80/20)**
Promptkategorier som står för 80% av felen — var man ska angripa först (verkliga Langfuse-data).
<img src="/admtools/pareto.png" alt="Pareto de falhas do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🔥 GUT-matris — prioritering (värmekarta)**
Allvar × Brådska × Tendens för åtgärderna; högre GUT = agera först.
<img src="/admtools/gut.png" alt="Matriz GUT do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🕸️ Konkurrensradar — särskiljande**
Det utvalda projektets fingeravtryck **vs portföljsnittet** (det blå området dominerar det grå på nästan varje axel).
<img src="/admtools/radar.png" alt="Radar competitivo do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>

</div>

> **📌 Exekutiv läsning.** **Radarn** avbildar konkurrensfördelen: Kronjuvelen slår snittet i anti-hallucination, Lean och nyttig leverans. **SWOT/PESTEL/5W4H** omvandlar diagnosen till **strategi och handlingsplan**; **Pareto + GUT** anger **exakt var** man ska agera först för att omvandla operativt ledarskap till definitiv finansiell avkastning.

---
## 🔗 Individuella paneler per projekt

{#each kpis as p}
<a href="/projetos/{p.project_name}">▶️ {p.project_name} — PSR {p.kpi_psr}</a>
{/each}
