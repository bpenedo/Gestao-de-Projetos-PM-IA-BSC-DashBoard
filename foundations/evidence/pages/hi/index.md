---
title: BSC पैनल — AI परियोजना प्रबंधन (PM)
---

🌐 [Português](/) · [English](/en) · [Español](/es) · [Français](/fr) · [Deutsch](/de) · [中文](/zh) · [한국어](/ko) · **हिन्दी** · [עברית](/he) · [Svenska](/sv) · [Русский](/ru) · [Suomi](/fi)


🌐 **Português** · [English](/en) · [Español](/es) · [Français](/fr) · [Deutsch](/de) · [中文](/zh) · [한국어](/ko) · [हिन्दी](/hi)


_Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com_
**साप्ताहिक चेकपॉइंट — हर शुक्रवार 09:00 बजे।**

> ⚠️ **डेमो डेटा** (अनाम पोर्टफोलियो)। Langfuse सिंक होने पर वास्तविक बन जाता है।

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

## 📈 पोर्टफोलियो कार्यकारी सारांश

<BigValue data={kpis} value=total_tokens title="कुल टोकन" agg=sum fmt=num0/>
<BigValue data={kpis} value=kpi_psr title="औसत PSR (0-5)" agg=mean fmt=num1/>
<BigValue data={kpis} value=kpi_idls_lean title="औसत लीन अपव्यय %" agg=mean fmt=num1/>
<BigValue data={kpis} value=burn_rate_ia title="कुल बर्न रेट" agg=sum fmt='$#,##0.00'/>

## 🌐 पोर्टफोलियो 5D मानचित्र (C-लेवल दृश्य)
> 3D गोले (5dchart शैली) — **प्रति परियोजना 5 आयाम**: **X**=आयतन (टोकन) · **Y**=PEUC/गुणवत्ता (%) · **Z**=PSR/स्वास्थ्य (0–5) · **आकार**=Burn Rate (R$) · **रंग**=ICCA/संधारणीयता (🟢 3x से ऊपर लागत कवर · 🔴 1x से नीचे = हानि)।
>
> **बोर्ड की दृष्टि:** आदर्श परियोजना **दाएँ/पीछे** (पैमाना+गुणवत्ता), **ऊँची** (PSR) और **हरी** (संधारणीय) होती है। **बड़ा लाल** गोला = कवरेज बिना बहुत नकदी जली → स्केल से पहले सुधारें।

![Mapa 5D do Portfólio de Projetos de IA](/5d_projetos.png?v=5)

### 🖱️ इंटरैक्टिव 5D मानचित्र — प्रत्येक गोले पर माउस ले जाएँ
> **X** = टोकन (पैमाना) · **Y** = PEUC (%) · **आकार** = PSR (0–5) · **रंग** = ICCA (🟢 संधारणीय · 🟠 सीमांत · 🔴 हानि)। प्रत्येक **ग्लॉसी गोले** पर माउस ले जाने पर **परियोजना नाम, PSR, PEUC और टोकन** दिखते हैं।

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

## 📉 मुख्य संकेतक (CPP) और स्कोर (PSR) की प्रवृत्ति
> C-लेवल के लिए सबसे महत्वपूर्ण: **दिशा**। CPP गिरना = पोर्टफोलियो अधिक कुशल।

<LineChart data={tendencia} x=data_snapshot y=cpp_medio yAxisTitle="CPP médio (R$/%)" title="प्रति प्रगति बिंदु लागत — पोर्टफोलियो प्रवृत्ति" markers=true/>

<LineChart data={tendencia} x=data_snapshot y=psr_medio yAxisTitle="PSR médio" yMin=0 yMax=5 title="पोर्टफोलियो औसत स्कोर (PSR 0-5)" markers=true/>

## ⭐ प्रति परियोजना स्कोर (PSR)

<BarChart data={kpis} x=project_name y=kpi_psr swapXY=true title="प्रति परियोजना PSR (0-5) — क्रमबद्ध" sort=true labels=true/>

## 🍩 संरचना और मिश्रण (गहराई वाला डोनट)

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

## 🧭 संधारणीयता चतुर्थांश (स्केल करें या सुधारें?)
> X अक्ष = **ICCA** (कवरेज: 3x से ऊपर = स्वस्थ) · Y अक्ष = **IBMT** (सीमांत बर्न: 0.33 से नीचे = अच्छा) · आकार = Burn Rate।
> नीचे-दाएँ = **लाभ के साथ स्केल**; ऊपर-बाएँ = **बढ़ने से पहले सुधारें**।

<ScatterPlot data={kpis} x=kpi_icca y=kpi_ibmt series=project_name size=burn_rate_ia xAxisTitle="ICCA — cobertura de custo (x)" yAxisTitle="IBMT — burn marginal (x)" title="प्रति परियोजना वित्तीय संधारणीयता"/>

## 📊 प्रति परियोजना विफलता पैरेटो

<BarChart data={falhas} x=project_name y=percentual_dominancia series=categoria_falha type=stacked100 swapXY=true title="प्रति परियोजना विफलता प्रभुत्व (%)"/>

## 🗂️ स्कोर और वित्तीय स्वास्थ्य (तालिका)

<DataTable data={kpis} rows=all rowShading=true>
  <Column id=project_name title="परियोजना"/>
  <Column id=kpi_psr title="PSR" fmt=num2/>
  <Column id=kpi_peuc title="PEUC %" fmt=num1/>
  <Column id=kpi_iita title="IITA %" fmt=num1/>
  <Column id=kpi_idls_lean title="IDLS %" fmt=num1/>
  <Column id=vrt_por_ktoken title="VRT/kT" fmt='$#,##0.0000'/>
  <Column id=kpi_icca title="ICCA x" fmt=num2/>
  <Column id=kpi_ibmt title="IBMT x" fmt=num3/>
  <Column id=kpi_cpp title="CPP R$/%" fmt='$#,##0.00'/>
</DataTable>

## 🚨 महत्वपूर्ण अलर्ट

<DataTable data={alertas} rows=8>
  <Column id=project_name title="परियोजना"/>
  <Column id=tipo_erro title="विफलता"/>
  <Column id=tokens_desperdicados title="Tokens" fmt=num0/>
  <Column id=data_evento title="कब"/>
</DataTable>

## 📅 साप्ताहिक बैठक एजेंडा

<DataTable data={reuniao} rows=all>
  <Column id=project_name title="परियोजना"/>
  <Column id=sumario_executivo title="सारांश"/>
  <Column id=acoes_corretivas_lean title="लीन क्रियाएँ (PDCA)"/>
</DataTable>

## 🪙 लागत वसूली (VRT) — 5 ब्लॉक + औसत (दूसरा दृष्टिकोण)
> समान बंटवारा आधार **5 सूक्ष्मताओं** में (R$ प्रति 50/100/250/500/1,000 टोकन) + **ब्लॉक औसत** — प्रति परियोजना खपत का दूसरा दृष्टिकोण।

<DataTable data={kpis} rows=all rowShading=true>
  <Column id=project_name title="परियोजना"/>
  <Column id=vrt_50t title="50 tok" fmt='#,##0.00000'/>
  <Column id=vrt_100t title="100 tok" fmt='#,##0.00000'/>
  <Column id=vrt_250t title="250 tok" fmt='#,##0.00000'/>
  <Column id=vrt_500t title="500 tok" fmt='#,##0.00000'/>
  <Column id=vrt_por_ktoken title="1.000 tok" fmt='#,##0.00000'/>
  <Column id=vrt_media_blocos title="औसत ब्लॉक" fmt='#,##0.00000' contentType=colorscale/>
</DataTable>

## ⏰ महत्वपूर्ण व्यवधान/प्रभाव समय (HCI)
> प्रत्येक परियोजना **दिन के किस घंटे (BRT)** सबसे अधिक प्रभावित होती है — सही विंडो में कार्रवाई हेतु (Tier अपग्रेड, बैकऑफ, शेड्यूलिंग)।

<BarChart data={hora_total} x=hora_brt y=interrupcoes title="दिन के घंटे अनुसार व्यवधान (BRT) — पोर्टफोलियो" xAxisTitle="Hora (0-23, BRT)"/>

<DataTable data={horario_critico} rows=all rowShading=true>
  <Column id=project_name title="परियोजना"/>
  <Column id=hora_pico title="चरम समय (BRT)" fmt='0"h"'/>
  <Column id=interrupcoes_pico title="चरम पर व्यवधान" fmt=num0/>
</DataTable>

## ♻️ अपव्यय वर्गीकरण (Lean Six Sigma) — सबसे अधिक अपव्यय कहाँ
> अपव्यय **भारित टोकन** से मापा गया (दोष 2.0× · कोटा 1.5× · अतिप्रसंस्करण 1.0× · विलंब 0.5×), केवल गिनती से नहीं।

<Grid cols=2>
<Group>

**पोर्टफोलियो अपव्यय मिश्रण**
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

**प्रति परियोजना प्रमुख अपव्यय**
<DataTable data={waste_dom} rows=all>
  <Column id=project_name title="परियोजना"/>
  <Column id=waste_dominante title="प्रमुख अपव्यय"/>
  <Column id=waste_tokens title="बर्बाद टोकन" fmt=num0/>
</DataTable>

</Group>
</Grid>

<BarChart data={wastes} x=project_name y=waste_tokens series=categoria_waste type=stacked swapXY=true title="अपव्यय संरचना (भारित टोकन) प्रति परियोजना"/>

## 🔬 RCA — प्रॉम्प्ट प्रकार अनुसार मतिभ्रम (हर परियोजना को क्या धीमा करता है)
> मूल कारण विश्लेषण: प्रॉम्प्ट्स को **श्रेणियों** में वर्गीकृत कर प्रत्येक का मतिभ्रम मापते हैं।
> **हर परियोजना को क्या धीमा करता है** और **सभी को समान रूप से क्या धीमा करता है (प्रतिच्छेदन)** का वस्तुनिष्ठ निदान।

### 🎯 प्रतिच्छेदन — पोर्टफोलियो का साझा अड़चन
> सर्वाधिक परियोजनाओं में **#1 मतिभ्रम अड़चन** वाला प्रॉम्प्ट प्रकार। इसे पहले हल करने का सबसे बड़ा प्रणालीगत प्रभाव।

<BarChart data={rca_inter} x=prompt_categoria y=projetos_onde_e_top1 title="पोर्टफोलियो को सर्वाधिक धीमा करने वाला प्रॉम्प्ट प्रकार (N परियोजनाओं में #1 अड़चन)" yAxisTitle="Nº de projetos onde é o gargalo #1" labels=true sort=true/>

### 🧭 प्रति परियोजना मतिभ्रम अड़चन (व्यक्तिगत RCA)

<DataTable data={rca_proj} rows=all rowShading=true>
  <Column id=project_name title="परियोजना"/>
  <Column id=prompt_gargalo title="सर्वाधिक मतिभ्रम वाला प्रॉम्प्ट (अड़चन)"/>
  <Column id=alucinacoes title="मतिभ्रम" fmt=num0/>
</DataTable>

### 📊 श्रेणी × परियोजना अनुसार मतिभ्रम वर्गीकरण

<BarChart data={aluc_cat} x=project_name y=alucinacoes series=prompt_categoria type=stacked swapXY=true title="प्रत्येक परियोजना में प्रॉम्प्ट प्रकार अनुसार मतिभ्रम"/>

## 💰 NPV, पेबैक और पोर्टफोलियो नकदी प्रवाह
> **आपके नकदी प्रवाह** से गणना (CSV/स्प्रेडशीट — देखें `pipeline/fluxo_caixa_template.csv` और `python3 carregar_fluxo.py आपका.csv`)। NPV = Σ प्रवाह ÷ (1+i)ᵗ · पेबैक **सरल** (समय प्रक्षेप) और **छूटयुक्त**, दोनों प्रक्षेपित। _जब तक आप अपना CSV न दें, डेमो डेटा।_

<DataTable data={vpl} rows=all rowShading=true>
  <Column id=project_name title="परियोजना"/>
  <Column id=vpl title="VPL (R$)" fmt='$#,##0' contentType=colorscale/>
  <Column id=tir title="TIR" fmt=pct1/>
  <Column id=tirm title="TIRM" fmt=pct1/>
  <Column id=ill title="ILL (PI)" fmt=num2/>
  <Column id=vul title="VUL (R$)" fmt='$#,##0'/>
  <Column id=payback_simples title="सरल PB" fmt=num2/>
  <Column id=payback_descontado title="छूटयुक्त PB" fmt=num2/>
  <Column id=supera_selic title="TIR>SELIC?" fmt=boolean/>
  <Column id=supera_us title="TIR>EUA?" fmt=boolean/>
  <Column id=vpl_usd title="VPL US$" fmt='$#,##0'/>
  <Column id=payback_desc_usd title="PB desc. US$" fmt=num2/>
</DataTable>

> 🆕 **TIRM** (संशोधित IRR) आवक को परियोजना दर पर पुनर्निवेश करता है — IRR से अधिक यथार्थवादी। **VUL** (शुद्ध समान मूल्य) NPV को समतुल्य वार्षिक श्रृंखला में बदलता है।

> **TIR** = retorno do projeto · **ILL (PI)** acima de 1 = cria valor · comparados à **SELIC** e aos **juros dos EUA** (valores reais por projeto na tabela acima — colunas `TIR>SELIC?`/`TIR>EUA?`). O fluxo é **dolarizado** (USD/BRL) e descontado à taxa americana → colunas **VPL US$** e **PB desc. US$**. _Benchmarks (SELIC, juros EUA, câmbio) são placeholders — ajuste no `.env`._

**प्रति परियोजना IRR बनाम अवसर लागत (SELIC × अमेरिका)**

<BarChart data={vpl} x=project_name y=tir title="TIR por projeto comparada à SELIC e aos juros dos EUA" yAxisTitle="TIR (por período)" sort=true>
  <ReferenceLine y=0.105 color=warning label="SELIC (BR) ~10,5%"/>
  <ReferenceLine y=0.045 color=info label="Juros EUA ~4,5%"/>
</BarChart>

**Recuperação do investimento ao longo do tempo** (acumulado descontado — cruza zero = payback descontado)

<LineChart data={vpl_fluxo} x=periodo y=cum_desc series=project_name title="Fluxo de caixa acumulado descontado por período" yAxisTitle="Acumulado descontado (R$)" markers=true>
  <ReferenceLine y=0 color=negative label="break-even"/>
</LineChart>

## 💳 AI सदस्यता योजनाएँ — IOF सहित कुल लागत
> विनिमय **R$ 5.40/US$** · अंतरराष्ट्रीय लेनदेन (कार्ड) पर **IOF 3.5%**। `कुल = US$ × विनिमय × (1 + IOF)`।
> यह वास्तविक लागत है जो बंटवारा आधार (`assinaturas_infra`) में जाती है। मूल्य अनुमानित — आधिकारिक साइट देखें।

<DataTable data={planos} rows=all rowShading=true>
  <Column id=provedor title="प्रदाता"/>
  <Column id=plano title="योजना"/>
  <Column id=usd_mes title="US$/mês" fmt=num0/>
  <Column id=r_base title="R$ base" fmt='$#,##0.00'/>
  <Column id=iof_reais title="IOF" fmt='$#,##0.00'/>
  <Column id=total_iof title="Total c/ IOF (R$)" fmt='$#,##0.00'/>
</DataTable>

<BarChart data={planos_pagos} x=plano y=total_iof title="Custo total mensal com IOF por plano (R$)" swapXY=true sort=true/>

<div style="display:flex;align-items:center;justify-content:center;gap:1rem;flex-wrap:wrap;margin:1.4rem 0 0.4rem;">
  <img src="/shark.svg" alt="tubarão investidor" width="120" height="82" style="flex:0 0 auto;"/>
  <h2 style="text-align:center;margin:0;font-weight:800;">🏆 AHP-TOPSIS 2N — बहु-मानदंड निर्णय मॉडल (MCDM)</h2>
  <img src="/gekko_photo.png" alt="Gordon Gekko fumando charuto (terno azul)" width="100" height="100" style="flex:0 0 auto;border-radius:50%;box-shadow:0 2px 8px rgba(0,0,0,.25);"/>
</div>

> संकेतकों को मानदंड मानकर **सर्वश्रेष्ठ परियोजना का चयन**। भार **AHP**
> (VPL 37% · TIR 24% · ILL 14% · PSR 14% · IITA 5,6% · IDLS 5,6% — CR = 0,012, consistente).
> Ranking por **TOPSIS** em **duas normalizações** (vetorial/Euclidiana + min-max/linear); o
> **अंतिम Ci** औसत है। **मज़बूत?** स्तंभ = दोनों सामान्यीकरण स्थिति पर सहमत।

**🥇 विजेता परियोजना (उच्चतम अंतिम Ci):**
<DataTable data={mcda_top}>
  <Column id=project_name title="🏆 सर्वश्रेष्ठ परियोजना"/>
  <Column id=ci_final title="Ci final" fmt=num4/>
</DataTable>

<BarChart data={mcda} x=project_name y=ci_final title="Ranking AHP-TOPSIS 2n (Ci final, 0–1)" swapXY=true sort=true labels=true/>

<DataTable data={mcda} rows=all rowShading=true>
  <Column id=rank_final title="#"/>
  <Column id=project_name title="परियोजना"/>
  <Column id=ci_vector title="Ci vetorial" fmt=num4/>
  <Column id=ci_minmax title="Ci min-max" fmt=num4/>
  <Column id=ci_final title="Ci final" fmt=num4/>
  <Column id=concordante title="मज़बूत?" fmt=boolean/>
</DataTable>

> विजेता का **पिच डेक** जनरेट हुआ (परियोजनाएँ फ़ोल्डर / `pitchdeck/` देखें)। जहाँ स्थिति 6–7 सामान्यीकरणों में भिन्न होती है, रैंकिंग सबसे संवेदनशील है — वहाँ सावधानी से निर्णय लें।

### 📌 निष्कर्ष — कार्यकारी सारांश और C-लेवल इनसाइट्स

**निर्णय।** **AHP-TOPSIS 2n** मॉडल **{mcda_top[0].project_name}** को पोर्टफोलियो की सर्वश्रेष्ठ परियोजना चुनता है (**Ci = 0.96**/1.00), **पुष्ट मज़बूती** के साथ: दोनों सामान्यीकरण (वेक्टर और min-max) **पहले स्थान** व रैंकिंग के 8/10 पर सहमत — शीर्ष स्थिर, विधि का कृत्रिम परिणाम नहीं।

**{mcda_top[0].project_name} क्यों जीता।** **वित्तीय** मानदंड (NPV R$ 5,973 · IRR 32.9% · ILL 1.75) परियोजनाओं में **बराबर** हैं (नकदी प्रवाह अब भी एकसमान *प्लेसहोल्डर*)। वित्तीय निष्प्रभावी होने पर निर्णय **परिचालन दक्षता** पर जाता है, और वहाँ {mcda_top[0].project_name} हावी: पूरे पोर्टफोलियो में सबसे कम **मतिभ्रम दर (IITA 9.1%)** व सबसे कम **लीन अपव्यय (IDLS 15.0%)** — दूसरे स्थान का लगभग **आधा**। अर्थात्: **समान अनुमानित प्रतिफल, बहुत कम टोकन/नकदी अपव्यय के साथ।**

**C-लेवल इनसाइट्स।**
- 🥇 **दक्षता ही निर्णायक:** प्रतिफल समान होने पर जो **कम जलाता है** (कम IITA/IDLS) वही उच्च मार्जिन पर समान मूल्य देता है — सबसे स्केलेबल परिसंपत्ति।
- 🛡️ **निर्णय मज़बूती:** दोनों सामान्यीकरणों की सहमति (8/10) बोर्ड को रैंकिंग के शीर्ष पर कार्रवाई का **भरोसा** देती है; संवेदनशील क्षेत्र (स्थिति 6–7) कटौती से पहले गुणात्मक विश्लेषण माँगता है।
- 📉 **जोखिम पूँछ:** अंतिम स्थान (Ci 0.01) का संयुक्त प्रदर्शन सबसे खराब — **रीफैक्टरिंग या बंद करने** का उम्मीदवार (BCG मैट्रिक्स से मिलान)।

**⚠️ निर्णय-ईमानदारी चेतावनी।** वित्तीय मानदंड **AHP भार का 75%** (NPV 37% + IRR 24% + ILL 14%) रखते हैं, पर आज **भेद नहीं करते** क्योंकि नकदी प्रवाह प्लेसहोल्डर है। **निर्णय केवल प्रति-परियोजना वास्तविक नकदी प्रवाह से निश्चित** — दर्ज करते ही रैंकिंग काफ़ी बदल सकती है (वित्तीय फिर हावी होगा)।

**अनुशंसा।** (1) सिद्ध दक्षता के लिए {mcda_top[0].project_name} को **स्केल पायलट** के रूप में मंज़ूरी; (2) **वास्तविक नकदी प्रवाह** दर्ज कर `ahp_topsis.py` पुनः चलाकर अंतिम वित्तीय निर्णय; (3) पूँछ (अंतिम स्थान) पर सुधार योजना सक्रिय करें।

---
## 👑 **ताज के रत्न** का प्रशासनिक डोसियर — {mcda_top[0].project_name}

> क्लासिक प्रशासनिक उपकरण **केवल चयनित परियोजना पर** लागू — इसे समृद्ध करने, उभारने और इसके **प्रतिस्पर्धात्मक अंतर** को दर्शाने हेतु। सभी **समवर्ती Python पाइपलाइन** (`gerar_admtools.py`) से जनरेट — किसी बाहरी टेम्पलेट पर निर्भर नहीं। विवरण व औचित्य `foundations/admtools/ferramentas_administrativas.md` में।

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:1.2rem;margin:1rem 0;">

<div>

**🎯 SWOT — रणनीतिक स्थिति**
वास्तविक KPI से व्युत्पन्न शक्ति/कमजोरी/अवसर/खतरे (न्यूनतम IITA व IDLS = प्रमुख शक्ति)।
<img src="/admtools/swot.png" alt="SWOT do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🌐 PESTELC — वृहद परिवेश**
सात बाहरी कारक (राजनीतिक, आर्थिक, सामाजिक, तकनीकी, पारिस्थितिक, कानूनी, सांस्कृतिक)।
<img src="/admtools/pestel.png" alt="PESTELC do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🗺️ 5W4H — कार्य योजना (5W + 4H)**
What/Why/Where/When/Who + How/How much/How many/How long — चयनित परियोजना का स्केल-अप रोडमैप।
<img src="/admtools/5w4h.png" alt="5W4H do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**📊 विफलता पैरेटो (80/20)**
80% विफलताओं वाली प्रॉम्प्ट श्रेणियाँ — पहले कहाँ हमला करें (Langfuse वास्तविक डेटा)।
<img src="/admtools/pareto.png" alt="Pareto de falhas do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🔥 GUT मैट्रिक्स — प्राथमिकता (हीटमैप)**
क्रियाओं की गंभीरता × तात्कालिकता × प्रवृत्ति; अधिक GUT = पहले कार्य करें।
<img src="/admtools/gut.png" alt="Matriz GUT do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🕸️ प्रतिस्पर्धी रडार — विभेदक**
चयनित का फिंगरप्रिंट **बनाम पोर्टफोलियो औसत** (नीला क्षेत्र लगभग हर अक्ष पर ग्रे पर हावी)।
<img src="/admtools/radar.png" alt="Radar competitivo do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>

</div>

> **📌 कार्यकारी पठन।** **रडार** प्रतिस्पर्धात्मक अंतर दर्शाता है: ताज का रत्न एंटी-मतिभ्रम, लीन व उपयोगी वितरण में औसत से बेहतर। **SWOT/PESTEL/5W4H** इस निदान को **रणनीति व कार्य-योजना** में बदलते हैं; **Pareto + GUT** बताते हैं कि परिचालन नेतृत्व को निश्चित वित्तीय प्रतिफल में बदलने हेतु **पहले कहाँ** कार्य करें।

---
## 🔗 प्रति परियोजना अलग पैनल

{#each kpis as p}
<a href="/projetos/{p.project_name}">▶️ {p.project_name} — PSR {p.kpi_psr}</a>
{/each}
