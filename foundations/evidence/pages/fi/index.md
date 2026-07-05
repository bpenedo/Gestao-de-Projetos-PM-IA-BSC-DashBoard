---
title: BSC-paneeli — tekoälyprojektien hallinta (PM)
---

🌐 [Português](/) · [English](/en) · [Español](/es) · [Français](/fr) · [Deutsch](/de) · [中文](/zh) · [한국어](/ko) · [हिन्दी](/hi) · [עברית](/he) · [Svenska](/sv) · [Русский](/ru) · **Suomi**


🌐 **Português** · [English](/en) · [Español](/es) · [Français](/fr) · [Deutsch](/de) · [中文](/zh) · [한국어](/ko) · [हिन्दी](/hi)


_Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com_
**Viikkotarkistus — joka perjantai klo 09:00.**

> ⚠️ **DEMO-data** (anonymisoitu portfolio). Muuttuu todelliseksi, kun Langfuse synkronoi.

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

## 📈 Salkun yhteenveto

<BigValue data={kpis} value=total_tokens title="Tokenit yhteensä" agg=sum fmt=num0/>
<BigValue data={kpis} value=kpi_psr title="Keskim. PSR (0-5)" agg=mean fmt=num1/>
<BigValue data={kpis} value=kpi_idls_lean title="Keskim. Lean-hukka %" agg=mean fmt=num1/>
<BigValue data={kpis} value=burn_rate_ia title="Kokonais-Burn Rate" agg=sum fmt='$#,##0.00'/>

## 🌐 Salkun 5D-kartta (johtotaso)
> 3D-pallot (5dchart-tyyli) — **5 ulottuvuutta per projekti**: **X**=volyymi/mittakaava (tokenit) · **Y**=PEUC/laatu (%) · **Z**=PSR/terveys (0–5) · **koko**=Burn Rate (R$) · **väri**=ICCA/kestävyys (🟢 yli 3x kattaa kulun · 🔴 alle 1x = tappio).
>
> **Hallituksen näkökulma:** ihanteellinen projekti on **oikealla/takana** (mittakaava+laatu), **korkealla** (PSR) ja **vihreä** (kestävä). **Suuri punainen** pallo = paljon poltettua rahaa ilman katetta → korjaa ennen skaalausta.

![Mapa 5D do Portfólio de Projetos de IA](/5d_projetos.png?v=5)

### 🖱️ Interaktiivinen 5D-kartta — vie hiiri kunkin pallon päälle
> **X** = tokenit (mittakaava) · **Y** = PEUC (%) · **koko** = PSR (0–5) · **väri** = ICCA (🟢 kestävä · 🟠 rajalla · 🔴 tappio). Vie hiiri kunkin **kiiltävän pallon** päälle nähdäksesi **projektin nimen, PSR, PEUC ja tokenit**.

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

## 📉 Pääindikaattorin (CPP) ja pisteytyksen (PSR) trendi
> Johtotasolle tärkeintä: **suunta**. Laskeva CPP = salkku tehostuu.

<LineChart data={tendencia} x=data_snapshot y=cpp_medio yAxisTitle="CPP médio (R$/%)" title="Kustannus edistymispistettä kohden — salkun trendi" markers=true/>

<LineChart data={tendencia} x=data_snapshot y=psr_medio yAxisTitle="PSR médio" yMin=0 yMax=5 title="Salkun keskipisteet (PSR 0-5)" markers=true/>

## ⭐ Pisteet (PSR) projekteittain

<BarChart data={kpis} x=project_name y=kpi_psr swapXY=true title="PSR (0-5) projekteittain — lajiteltu" sort=true labels=true/>

## 🍩 Koostumus ja jakauma (syvyysdonitsi)

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

## 🧭 Kestävyyden nelikenttä (skaalaa vai korjaa?)
> X-akseli = **ICCA** (kate: yli 3x = terve) · Y-akseli = **IBMT** (rajaburn: alle 0,33 = hyvä) · koko = Burn Rate.
> Oikea alanurkka = **skaalaa voitolla**; vasen ylänurkka = **korjaa ennen kasvua**.

<ScatterPlot data={kpis} x=kpi_icca y=kpi_ibmt series=project_name size=burn_rate_ia xAxisTitle="ICCA — cobertura de custo (x)" yAxisTitle="IBMT — burn marginal (x)" title="Taloudellinen kestävyys projekteittain"/>

## 📊 Vikojen Pareto projekteittain

<BarChart data={falhas} x=project_name y=percentual_dominancia series=categoria_falha type=stacked100 swapXY=true title="Vikojen osuus (%) projekteittain"/>

## 🗂️ Pisteet ja taloudellinen terveys (taulukko)

<DataTable data={kpis} rows=all rowShading=true>
  <Column id=project_name title="Projekti"/>
  <Column id=kpi_psr title="PSR" fmt=num2/>
  <Column id=kpi_peuc title="PEUC %" fmt=num1/>
  <Column id=kpi_iita title="IITA %" fmt=num1/>
  <Column id=kpi_idls_lean title="IDLS %" fmt=num1/>
  <Column id=vrt_por_ktoken title="VRT/kT" fmt='$#,##0.0000'/>
  <Column id=kpi_icca title="ICCA x" fmt=num2/>
  <Column id=kpi_ibmt title="IBMT x" fmt=num3/>
  <Column id=kpi_cpp title="CPP R$/%" fmt='$#,##0.00'/>
</DataTable>

## 🚨 Kriittiset hälytykset

<DataTable data={alertas} rows=8>
  <Column id=project_name title="Projekti"/>
  <Column id=tipo_erro title="Vika"/>
  <Column id=tokens_desperdicados title="Tokens" fmt=num0/>
  <Column id=data_evento title="Milloin"/>
</DataTable>

## 📅 Viikkopalaverin asialista

<DataTable data={reuniao} rows=all>
  <Column id=project_name title="Projekti"/>
  <Column id=sumario_executivo title="Yhteenveto"/>
  <Column id=acoes_corretivas_lean title="Lean-toimet (PDCA)"/>
</DataTable>

## 🪙 Kustannusten kattaminen (VRT) — 5 lohkoa + keskiarvo (toinen näkymä)
> Sama jakoperuste **5 tarkkuudella** (R$ per 50/100/250/500/1 000 tokenia) + **lohkojen keskiarvo** — toinen näkökulma projektin kulutukseen.

<DataTable data={kpis} rows=all rowShading=true>
  <Column id=project_name title="Projekti"/>
  <Column id=vrt_50t title="50 tok" fmt='#,##0.00000'/>
  <Column id=vrt_100t title="100 tok" fmt='#,##0.00000'/>
  <Column id=vrt_250t title="250 tok" fmt='#,##0.00000'/>
  <Column id=vrt_500t title="500 tok" fmt='#,##0.00000'/>
  <Column id=vrt_por_ktoken title="1.000 tok" fmt='#,##0.00000'/>
  <Column id=vrt_media_blocos title="KESKIM. lohkot" fmt='#,##0.00000' contentType=colorscale/>
</DataTable>

## ⏰ Kriittinen keskeytys-/vaikutustunti (HCI)
> Minä **vuorokauden tuntina (BRT)** kukin projekti kärsii eniten — jotta toimit oikeassa ikkunassa (Tier-päivitys, backoff, ajoitus).

<BarChart data={hora_total} x=hora_brt y=interrupcoes title="Keskeytykset vuorokauden tunneittain (BRT) — salkku" xAxisTitle="Hora (0-23, BRT)"/>

<DataTable data={horario_critico} rows=all rowShading=true>
  <Column id=project_name title="Projekti"/>
  <Column id=hora_pico title="Huipputunti (BRT)" fmt='0"h"'/>
  <Column id=interrupcoes_pico title="Keskeytykset huipussa" fmt=num0/>
</DataTable>

## ♻️ Hukan taksonomia (Lean Six Sigma) — missä eniten hukkaa
> Hukka mitataan **painotetuilla tokeneilla** (Vika 2,0× · Kiintiö 1,5× · Ylikäsittely 1,0× · Viive 0,5×), ei vain määränä.

<Grid cols=2>
<Group>

**Salkun hukkajakauma**
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

**Hallitseva hukka projekteittain**
<DataTable data={waste_dom} rows=all>
  <Column id=project_name title="Projekti"/>
  <Column id=waste_dominante title="Hallitseva hukka"/>
  <Column id=waste_tokens title="Hukatut tokenit" fmt=num0/>
</DataTable>

</Group>
</Grid>

<BarChart data={wastes} x=project_name y=waste_tokens series=categoria_waste type=stacked swapXY=true title="Hukan koostumus (painotetut tokenit) projekteittain"/>

## 🔬 RCA — hallusinaatio prompttyypeittäin (mikä VIIVÄSTYTTÄÄ kutakin projektia)
> Juurisyyanalyysi: luokittelemme promptit **kategorioihin** ja mittaamme kunkin hallusinaation.
> Objektiivinen diagnoosi siitä, **mikä viivästyttää kutakin projektia** ja **mikä viivästyttää kaikkia YHTEISESTI (leikkaus)**.

### 🎯 Leikkaus — salkun yhteinen pullonkaula
> Prompttyyppi, joka on **hallusinaatioiden pullonkaula nro 1** useimmissa projekteissa. Sen ratkaiseminen ensin tuo suurimman järjestelmävaikutuksen.

<BarChart data={rca_inter} x=prompt_categoria y=projetos_onde_e_top1 title="Salkkua eniten viivästyttävä prompttyyppi (pullonkaula #1 N projektissa)" yAxisTitle="Nº de projetos onde é o gargalo #1" labels=true sort=true/>

### 🧭 Hallusinaatiopullonkaula projekteittain (yksittäinen RCA)

<DataTable data={rca_proj} rows=all rowShading=true>
  <Column id=project_name title="Projekti"/>
  <Column id=prompt_gargalo title="Eniten hallusinoiva prompt (pullonkaula)"/>
  <Column id=alucinacoes title="Hallusinaatiot" fmt=num0/>
</DataTable>

### 📊 Hallusinaatiotaksonomia kategoria × projekti

<BarChart data={aluc_cat} x=project_name y=alucinacoes series=prompt_categoria type=stacked swapXY=true title="Hallusinaatiot prompttyypeittäin kussakin projektissa"/>

## 💰 NPV, takaisinmaksu ja salkun kassavirta
> Laskettu **kassavirrastasi** (CSV/taulukko — ks. `pipeline/fluxo_caixa_template.csv` ja `python3 carregar_fluxo.py OMASI.csv`). NPV = Σ virta ÷ (1+i)ᵗ · Payback **yksinkertainen** (aikavaihtelu) ja **diskontattu**, molemmat interpoloitu. _Demodataa, kunnes annat oman CSV:si._

<DataTable data={vpl} rows=all rowShading=true>
  <Column id=project_name title="Projekti"/>
  <Column id=vpl title="VPL (R$)" fmt='$#,##0' contentType=colorscale/>
  <Column id=tir title="TIR" fmt=pct1/>
  <Column id=tirm title="TIRM" fmt=pct1/>
  <Column id=ill title="ILL (PI)" fmt=num2/>
  <Column id=vul title="VUL (R$)" fmt='$#,##0'/>
  <Column id=payback_simples title="Yksink. PB" fmt=num2/>
  <Column id=payback_descontado title="Diskontattu PB" fmt=num2/>
  <Column id=supera_selic title="TIR>SELIC?" fmt=boolean/>
  <Column id=supera_us title="TIR>EUA?" fmt=boolean/>
  <Column id=vpl_usd title="VPL US$" fmt='$#,##0'/>
  <Column id=payback_desc_usd title="PB desc. US$" fmt=num2/>
</DataTable>

> 🆕 **TIRM** (muokattu IRR) sijoittaa tulovirrat uudelleen projektin korolla — realistisempi kuin IRR. **VUL** (tasainen nettoarvo) muuntaa NPV:n vastaavaksi vuosisarjaksi.

> **TIR** = retorno do projeto · **ILL (PI)** acima de 1 = cria valor · comparados à **SELIC** e aos **juros dos EUA** (valores reais por projeto na tabela acima — colunas `TIR>SELIC?`/`TIR>EUA?`). O fluxo é **dolarizado** (USD/BRL) e descontado à taxa americana → colunas **VPL US$** e **PB desc. US$**. _Benchmarks (SELIC, juros EUA, câmbio) são placeholders — ajuste no `.env`._

**IRR projekteittain vs. vaihtoehtoiskustannus (SELIC × USA)**

<BarChart data={vpl} x=project_name y=tir title="TIR por projeto comparada à SELIC e aos juros dos EUA" yAxisTitle="TIR (por período)" sort=true>
  <ReferenceLine y=0.105 color=warning label="SELIC (BR) ~10,5%"/>
  <ReferenceLine y=0.045 color=info label="Juros EUA ~4,5%"/>
</BarChart>

**Recuperação do investimento ao longo do tempo** (acumulado descontado — cruza zero = payback descontado)

<LineChart data={vpl_fluxo} x=periodo y=cum_desc series=project_name title="Fluxo de caixa acumulado descontado por período" yAxisTitle="Acumulado descontado (R$)" markers=true>
  <ReferenceLine y=0 color=negative label="break-even"/>
</LineChart>

## 💳 Tekoälytilaukset — kokonaiskustannus IOF:llä
> Valuuttakurssi **R$ 5,40/US$** · **IOF 3,5%** kansainvälisestä tapahtumasta (kortti). `Yhteensä = US$ × kurssi × (1 + IOF)`.
> Tämä on todellinen kustannus, joka syöttää jakoperustan (`assinaturas_infra`). Hinnat likimääräisiä — tarkista viralliset sivut.

<DataTable data={planos} rows=all rowShading=true>
  <Column id=provedor title="Palveluntarjoaja"/>
  <Column id=plano title="Suunnitelma"/>
  <Column id=usd_mes title="US$/mês" fmt=num0/>
  <Column id=r_base title="R$ base" fmt='$#,##0.00'/>
  <Column id=iof_reais title="IOF" fmt='$#,##0.00'/>
  <Column id=total_iof title="Total c/ IOF (R$)" fmt='$#,##0.00'/>
</DataTable>

<BarChart data={planos_pagos} x=plano y=total_iof title="Custo total mensal com IOF por plano (R$)" swapXY=true sort=true/>

<div style="display:flex;align-items:center;justify-content:center;gap:1rem;flex-wrap:wrap;margin:1.4rem 0 0.4rem;">
  <img src="/shark.svg" alt="tubarão investidor" width="120" height="82" style="flex:0 0 auto;"/>
  <h2 style="text-align:center;margin:0;font-weight:800;">🏆 AHP-TOPSIS 2N — monikriteerinen päätösmalli (MCDM)</h2>
  <img src="/gekko_photo.png" alt="Gordon Gekko fumando charuto (terno azul)" width="100" height="100" style="flex:0 0 auto;border-radius:50%;box-shadow:0 2px 8px rgba(0,0,0,.25);"/>
</div>

> **Parhaan projektin valinta** painottamalla indikaattoreita kriteereinä. Painot **AHP**:lla
> (VPL 37% · TIR 24% · ILL 14% · PSR 14% · IITA 5,6% · IDLS 5,6% — CR = 0,012, consistente).
> Ranking por **TOPSIS** em **duas normalizações** (vetorial/Euclidiana + min-max/linear); o
> **Lopullinen Ci** on keskiarvo. Sarake **Vankka?** = molemmat normalisoinnit ovat samaa mieltä sijainnista.

**🥇 Voittajaprojekti (korkein lopullinen Ci):**
<DataTable data={mcda_top}>
  <Column id=project_name title="🏆 Paras projekti"/>
  <Column id=ci_final title="Ci final" fmt=num4/>
</DataTable>

<BarChart data={mcda} x=project_name y=ci_final title="Ranking AHP-TOPSIS 2n (Ci final, 0–1)" swapXY=true sort=true labels=true/>

<DataTable data={mcda} rows=all rowShading=true>
  <Column id=rank_final title="#"/>
  <Column id=project_name title="Projekti"/>
  <Column id=ci_vector title="Ci vetorial" fmt=num4/>
  <Column id=ci_minmax title="Ci min-max" fmt=num4/>
  <Column id=ci_final title="Ci final" fmt=num4/>
  <Column id=concordante title="Vankka?" fmt=boolean/>
</DataTable>

> Voittajalle on luotu **pitch deck** (ks. Projektit-kansio / `pitchdeck/`). Missä sijat 6–7 eroavat normalisointien välillä, sijoitus on herkin — päätä siellä varoen.

### 📌 Loppupäätelmä — yhteenveto ja johtotason oivallukset

**Tuomio.** Malli **AHP-TOPSIS 2n** valitsee **{mcda_top[0].project_name}** salkun parhaaksi projektiksi (**Ci = 0,96** / 1,00), **vahvistetulla vankkuudella**: molemmat normalisoinnit (vektori ja min-max) ovat yhtä mieltä **1. sijasta** ja 8/10 sijoituksesta — kärki on vakaa, ei menetelmän artefakti.

**Miksi {mcda_top[0].project_name} voitti.** **Taloudelliset** kriteerit (NPV R$ 5 973 · IRR 32,9% · ILL 1,75) ovat projektien kesken **tasoissa** (kassavirta yhä yhtenäinen *paikkamerkki*). Kun talous on neutraloitu, päätös siirtyy **operatiiviseen tehokkuuteen**, ja siinä {mcda_top[0].project_name} hallitsee: matalin **hallusinaatioaste (IITA 9,1%)** ja pienin **Lean-hukka (IDLS 15,0%)** koko salkussa — lähes **puolet** kakkosen hukasta. Toisin sanoen: **sama ennustettu tuotto huomattavasti pienemmällä token-/kassahukalla.**

**Johtotason oivallukset.**
- 🥇 **Tehokkuus ratkaisee:** kun tuotto on samankaltainen, se joka **polttaa vähemmän** (matalampi IITA/IDLS) tuottaa saman arvon paremmalla katteella — skaalautuvin omaisuuserä.
- 🛡️ **Päätöksen vankkuus:** molempien normalisointien yksimielisyys (8/10) antaa hallitukselle **varmuuden** toimia sijoituksen kärjessä; herkkä alue (sijat 6–7) vaatii laadullista analyysiä ennen karsintaa.
- 📉 **Riskihäntä:** viimeiseksi sijoittunut (Ci 0,01) on yhdistetysti heikoin — ehdokas **refaktorointiin tai lopettamiseen** (ristiintarkista BCG-matriisiin).

**⚠️ Päätösrehellisyyden varaus.** Taloudelliset kriteerit kantavat **75% AHP-painosta** (NPV 37% + IRR 24% + ILL 14%), mutta tänään ne **eivät erottele**, koska kassavirta on paikkamerkki. **Tuomio on lopullinen vasta TODELLISILLA projektikohtaisilla kassavirroilla** — syötettyinä sijoitus voi muuttua merkittävästi (talous hallitsee jälleen).

**Suositus.** (1) Hyväksy {mcda_top[0].project_name} **skaalauspilotiksi** todistetun tehokkuuden vuoksi; (2) syötä **todelliset kassavirrat** ja aja `ahp_topsis.py` uudelleen lopullista talousarviota varten; (3) käynnistä parannussuunnitelma hännälle (viimeiseksi sijoittuneelle).

---
## 👑 **Kruununjalokiven** hallinnollinen kansio — {mcda_top[0].project_name}

> Klassiset hallinnolliset työkalut sovellettuna **yksinomaan valittuun projektiin** rikastuttamaan, korostamaan ja tuomaan esiin sen **kilpailuedun**. Kaikki tuotetaan **rinnakkaisella Python-putkella** (`gerar_admtools.py`) — ilman ulkoista mallia. Tiedot ja perustelut: `foundations/admtools/ferramentas_administrativas.md`.

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:1.2rem;margin:1rem 0;">

<div>

**🎯 SWOT — strateginen asema**
Vahvuudet/heikkoudet/mahdollisuudet/uhat johdettuina todellisista KPI:istä (matalimmat IITA ja IDLS = hallitseva vahvuus).
<img src="/admtools/swot.png" alt="SWOT do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🌐 PESTELC — makroympäristö**
Seitsemän ulkoista tekijää (poliittiset, taloudelliset, sosiaaliset, teknologiset, ekologiset, oikeudelliset, kulttuuriset).
<img src="/admtools/pestel.png" alt="PESTELC do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🗺️ 5W4H — toimintasuunnitelma (5W + 4H)**
What/Why/Where/When/Who + How/How much/How many/How long — valitun projektin skaalaussuunnitelma.
<img src="/admtools/5w4h.png" alt="5W4H do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**📊 Vikojen Pareto (80/20)**
Prompttikategoriat, jotka muodostavat 80% vioista — mihin hyökätä ensin (todelliset Langfuse-tiedot).
<img src="/admtools/pareto.png" alt="Pareto de falhas do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🔥 GUT-matriisi — priorisointi (lämpökartta)**
Vakavuus × Kiireellisyys × Suuntaus toimille; korkeampi GUT = toimi ensin.
<img src="/admtools/gut.png" alt="Matriz GUT do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🕸️ Kilpailututka — erottautuminen**
Valitun projektin sormenjälki **vs salkun keskiarvo** (sininen alue hallitsee harmaata lähes joka akselilla).
<img src="/admtools/radar.png" alt="Radar competitivo do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>

</div>

> **📌 Johdon luenta.** **Tutka** kuvaa kilpailuedun: Kruununjalokivi ylittää keskiarvon anti-hallusinaatiossa, Leanissä ja hyödyllisessä toimituksessa. **SWOT/PESTEL/5W4H** muuntavat diagnoosin **strategiaksi ja toimintasuunnitelmaksi**; **Pareto + GUT** kertovat **tarkalleen missä** toimia ensin, jotta operatiivinen johtoasema muuttuu lopulliseksi taloudelliseksi tuotoksi.

---
## 🔗 Projektikohtaiset paneelit

{#each kpis as p}
<a href="/projetos/{p.project_name}">▶️ {p.project_name} — PSR {p.kpi_psr}</a>
{/each}
