---
title: לוח BSC — ניהול פרויקטים (PM) של AI
---

🌐 [Português](/) · [English](/en) · [Español](/es) · [Français](/fr) · [Deutsch](/de) · [中文](/zh) · [한국어](/ko) · [हिन्दी](/hi) · **עברית** · [Svenska](/sv) · [Русский](/ru) · [Suomi](/fi)


🌐 **Português** · [English](/en) · [Español](/es) · [Français](/fr) · [Deutsch](/de) · [中文](/zh) · [한국어](/ko) · [हिन्दी](/hi)


_Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com_
**נקודת ביקורת שבועית — כל יום שישי בשעה 09:00.**

> ⚠️ **נתוני הדגמה** (תיק מנוטרל). הופכים לאמיתיים לאחר סנכרון Langfuse.

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

## 📈 תקציר מנהלים של התיק

<BigValue data={kpis} value=total_tokens title="סה״כ טוקנים" agg=sum fmt=num0/>
<BigValue data={kpis} value=kpi_psr title="PSR ממוצע (0-5)" agg=mean fmt=num1/>
<BigValue data={kpis} value=kpi_idls_lean title="בזבוז Lean ממוצע %" agg=mean fmt=num1/>
<BigValue data={kpis} value=burn_rate_ia title="סה״כ Burn Rate" agg=sum fmt='$#,##0.00'/>

## 🌐 מפת 5D של התיק (מבט דרג בכיר)
> כדורים תלת-ממדיים (סגנון 5dchart) — **5 ממדים לכל פרויקט**: **X**=נפח (טוקנים) · **Y**=PEUC/איכות (%) · **Z**=PSR/בריאות (0–5) · **גודל**=Burn Rate (R$) · **צבע**=ICCA/קיימות (🟢 מעל 3x מכסה עלות · 🔴 מתחת ל-1x = הפסד).
>
> **קריאה לדירקטוריון:** הפרויקט האידיאלי נמצא **ימין/עומק** (היקף+איכות), **גבוה** (PSR) ו**ירוק** (בר-קיימא). כדור **גדול ואדום** = הרבה מזומן שנשרף ללא כיסוי → לתקן לפני הרחבה.

![Mapa 5D do Portfólio de Projetos de IA](/5d_projetos.png?v=5)

### 🖱️ מפת 5D אינטראקטיבית — העבירו את העכבר מעל כל כדור
> **X** = טוקנים (היקף) · **Y** = PEUC (%) · **גודל** = PSR (0–5) · **צבע** = ICCA (🟢 בר-קיימא · 🟠 גבולי · 🔴 הפסד). מעבר עכבר מעל כל **כדור מבריק** מציג **שם הפרויקט, PSR, PEUC וטוקנים**.

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

## 📉 מגמת המדד המרכזי (CPP) והציון (PSR)
> מה שהכי חשוב לדרג הבכיר: **הכיוון**. CPP יורד = התיק נעשה יעיל יותר.

<LineChart data={tendencia} x=data_snapshot y=cpp_medio yAxisTitle="CPP médio (R$/%)" title="עלות לנקודת התקדמות — מגמת התיק" markers=true/>

<LineChart data={tendencia} x=data_snapshot y=psr_medio yAxisTitle="PSR médio" yMin=0 yMax=5 title="ציון ממוצע של התיק (PSR 0-5)" markers=true/>

## ⭐ ציון (PSR) לפי פרויקט

<BarChart data={kpis} x=project_name y=kpi_psr swapXY=true title="PSR (0-5) לפי פרויקט — ממוין" sort=true labels=true/>

## 🍩 הרכב ותמהיל (תרשים דונאט עם עומק)

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

## 🧭 רביע הקיימות (להרחיב או לתקן?)
> ציר X = **ICCA** (כיסוי: מעל 3x = בריא) · ציר Y = **IBMT** (שריפה שולית: מתחת ל-0.33 = טוב) · גודל = Burn Rate.
> פינה ימנית-תחתונה = **הרחבה עם רווח**; שמאלית-עליונה = **לתקן לפני צמיחה**.

<ScatterPlot data={kpis} x=kpi_icca y=kpi_ibmt series=project_name size=burn_rate_ia xAxisTitle="ICCA — cobertura de custo (x)" yAxisTitle="IBMT — burn marginal (x)" title="קיימות פיננסית לפי פרויקט"/>

## 📊 פארטו של כשלים לפי פרויקט

<BarChart data={falhas} x=project_name y=percentual_dominancia series=categoria_falha type=stacked100 swapXY=true title="דומיננטיות כשלים (%) לפי פרויקט"/>

## 🗂️ ציון ובריאות פיננסית (טבלה)

<DataTable data={kpis} rows=all rowShading=true>
  <Column id=project_name title="פרויקט"/>
  <Column id=kpi_psr title="PSR" fmt=num2/>
  <Column id=kpi_peuc title="PEUC %" fmt=num1/>
  <Column id=kpi_iita title="IITA %" fmt=num1/>
  <Column id=kpi_idls_lean title="IDLS %" fmt=num1/>
  <Column id=vrt_por_ktoken title="VRT/kT" fmt='$#,##0.0000'/>
  <Column id=kpi_icca title="ICCA x" fmt=num2/>
  <Column id=kpi_ibmt title="IBMT x" fmt=num3/>
  <Column id=kpi_cpp title="CPP R$/%" fmt='$#,##0.00'/>
</DataTable>

## 🚨 התראות קריטיות

<DataTable data={alertas} rows=8>
  <Column id=project_name title="פרויקט"/>
  <Column id=tipo_erro title="כשל"/>
  <Column id=tokens_desperdicados title="Tokens" fmt=num0/>
  <Column id=data_evento title="מתי"/>
</DataTable>

## 📅 סדר יום לפגישה השבועית

<DataTable data={reuniao} rows=all>
  <Column id=project_name title="פרויקט"/>
  <Column id=sumario_executivo title="תקציר"/>
  <Column id=acoes_corretivas_lean title="פעולות Lean (PDCA)"/>
</DataTable>

## 🪙 עלות השבה (VRT) — 5 בלוקים + ממוצע (מבט שני)
> אותו בסיס הקצאה ב-**5 רזולוציות** (R$ ל-50/100/250/500/1,000 טוקנים) + **ממוצע הבלוקים** — מבט שני על הצריכה לכל פרויקט.

<DataTable data={kpis} rows=all rowShading=true>
  <Column id=project_name title="פרויקט"/>
  <Column id=vrt_50t title="50 tok" fmt='#,##0.00000'/>
  <Column id=vrt_100t title="100 tok" fmt='#,##0.00000'/>
  <Column id=vrt_250t title="250 tok" fmt='#,##0.00000'/>
  <Column id=vrt_500t title="500 tok" fmt='#,##0.00000'/>
  <Column id=vrt_por_ktoken title="1.000 tok" fmt='#,##0.00000'/>
  <Column id=vrt_media_blocos title="ממוצע בלוקים" fmt='#,##0.00000' contentType=colorscale/>
</DataTable>

## ⏰ שעת ההפרעה/ההשפעה הקריטית (HCI)
> באיזו **שעה ביום (BRT)** כל פרויקט מושפע ביותר — כדי לפעול בחלון הנכון (שדרוג Tier, backoff, תזמון).

<BarChart data={hora_total} x=hora_brt y=interrupcoes title="הפרעות לפי שעה ביום (BRT) — התיק" xAxisTitle="Hora (0-23, BRT)"/>

<DataTable data={horario_critico} rows=all rowShading=true>
  <Column id=project_name title="פרויקט"/>
  <Column id=hora_pico title="שעת שיא (BRT)" fmt='0"h"'/>
  <Column id=interrupcoes_pico title="הפרעות בשיא" fmt=num0/>
</DataTable>

## ♻️ טקסונומיית בזבוזים (Lean Six Sigma) — היכן מבזבזים הכי הרבה
> בזבוז נמדד לפי **טוקנים משוקללים** (פגם 2.0× · מכסה 1.5× · עיבוד-יתר 1.0× · השהיה 0.5×), לא רק לפי כמות.

<Grid cols=2>
<Group>

**תמהיל בזבוז בתיק**
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

**בזבוז דומיננטי לפי פרויקט**
<DataTable data={waste_dom} rows=all>
  <Column id=project_name title="פרויקט"/>
  <Column id=waste_dominante title="בזבוז דומיננטי"/>
  <Column id=waste_tokens title="טוקנים מבוזבזים" fmt=num0/>
</DataTable>

</Group>
</Grid>

<BarChart data={wastes} x=project_name y=waste_tokens series=categoria_waste type=stacked swapXY=true title="הרכב בזבוז (טוקנים משוקללים) לפי פרויקט"/>

## 🔬 RCA — הזיות לפי סוג פרומפט (מה שמעכב כל פרויקט)
> ניתוח שורש: מסווגים את הפרומפטים ל-**קטגוריות** ומודדים את ההזיה של כל אחת.
> אבחון אובייקטיבי של **מה מעכב כל פרויקט** ו**מה מעכב את כולם במשותף (חיתוך)**.

### 🎯 חיתוך — צוואר הבקבוק המשותף לתיק
> סוג הפרומפט שהוא **צוואר בקבוק ההזיה מס' 1** במרב הפרויקטים. תקיפתו ראשון בעלת האפקט המערכתי הגדול ביותר.

<BarChart data={rca_inter} x=prompt_categoria y=projetos_onde_e_top1 title="סוג הפרומפט שהכי מעכב את התיק (צוואר בקבוק #1 ב-N פרויקטים)" yAxisTitle="Nº de projetos onde é o gargalo #1" labels=true sort=true/>

### 🧭 צוואר בקבוק של הזיות לפי פרויקט (RCA פרטני)

<DataTable data={rca_proj} rows=all rowShading=true>
  <Column id=project_name title="פרויקט"/>
  <Column id=prompt_gargalo title="הפרומפט עם הכי הרבה הזיות (צוואר בקבוק)"/>
  <Column id=alucinacoes title="הזיות" fmt=num0/>
</DataTable>

### 📊 טקסונומיית הזיות לפי קטגוריה × פרויקט

<BarChart data={aluc_cat} x=project_name y=alucinacoes series=prompt_categoria type=stacked swapXY=true title="הזיות לפי סוג פרומפט בכל פרויקט"/>

## 💰 NPV, החזר וזרם מזומנים של התיק
> מחושב מ**תזרים המזומנים שלך** (CSV/גיליון — ראו `pipeline/fluxo_caixa_template.csv` ו-`python3 carregar_fluxo.py שלך.csv`). NPV = Σ תזרים ÷ (1+i)ᵗ · Payback **פשוט** (וריאציה בזמן) ו**מהוון**, שניהם באינטרפולציה. _נתוני הדגמה עד שתספק CSV משלך._

<DataTable data={vpl} rows=all rowShading=true>
  <Column id=project_name title="פרויקט"/>
  <Column id=vpl title="VPL (R$)" fmt='$#,##0' contentType=colorscale/>
  <Column id=tir title="TIR" fmt=pct1/>
  <Column id=tirm title="TIRM" fmt=pct1/>
  <Column id=ill title="ILL (PI)" fmt=num2/>
  <Column id=vul title="VUL (R$)" fmt='$#,##0'/>
  <Column id=payback_simples title="PB פשוט" fmt=num2/>
  <Column id=payback_descontado title="PB מהוון" fmt=num2/>
  <Column id=supera_selic title="TIR>SELIC?" fmt=boolean/>
  <Column id=supera_us title="TIR>EUA?" fmt=boolean/>
  <Column id=vpl_usd title="VPL US$" fmt='$#,##0'/>
  <Column id=payback_desc_usd title="PB desc. US$" fmt=num2/>
</DataTable>

> 🆕 **TIRM** (IRR מתוקן) משקיע מחדש את התקבולים בריבית הפרויקט — ריאלי יותר מ-IRR. **VUL** (ערך אחיד נטו) ממיר את ה-NPV לסדרה שנתית שקולה.

> **TIR** = retorno do projeto · **ILL (PI)** acima de 1 = cria valor · comparados à **SELIC** e aos **juros dos EUA** (valores reais por projeto na tabela acima — colunas `TIR>SELIC?`/`TIR>EUA?`). O fluxo é **dolarizado** (USD/BRL) e descontado à taxa americana → colunas **VPL US$** e **PB desc. US$**. _Benchmarks (SELIC, juros EUA, câmbio) são placeholders — ajuste no `.env`._

**IRR לפי פרויקט מול עלות אלטרנטיבית (SELIC × ארה"ב)**

<BarChart data={vpl} x=project_name y=tir title="TIR por projeto comparada à SELIC e aos juros dos EUA" yAxisTitle="TIR (por período)" sort=true>
  <ReferenceLine y=0.105 color=warning label="SELIC (BR) ~10,5%"/>
  <ReferenceLine y=0.045 color=info label="Juros EUA ~4,5%"/>
</BarChart>

**Recuperação do investimento ao longo do tempo** (acumulado descontado — cruza zero = payback descontado)

<LineChart data={vpl_fluxo} x=periodo y=cum_desc series=project_name title="Fluxo de caixa acumulado descontado por período" yAxisTitle="Acumulado descontado (R$)" markers=true>
  <ReferenceLine y=0 color=negative label="break-even"/>
</LineChart>

## 💳 תוכניות מנוי ל-AI — עלות כוללת עם IOF
> שער **R$ 5.40/US$** · **IOF 3.5%** על פעולה בינלאומית (כרטיס). `סה"כ = US$ × שער × (1 + IOF)`.
> זו העלות האמיתית שמזינה את בסיס ההקצאה (`assinaturas_infra`). מחירים משוערים — בדקו באתרים הרשמיים.

<DataTable data={planos} rows=all rowShading=true>
  <Column id=provedor title="ספק"/>
  <Column id=plano title="תוכנית"/>
  <Column id=usd_mes title="US$/mês" fmt=num0/>
  <Column id=r_base title="R$ base" fmt='$#,##0.00'/>
  <Column id=iof_reais title="IOF" fmt='$#,##0.00'/>
  <Column id=total_iof title="Total c/ IOF (R$)" fmt='$#,##0.00'/>
</DataTable>

<BarChart data={planos_pagos} x=plano y=total_iof title="Custo total mensal com IOF por plano (R$)" swapXY=true sort=true/>

<div style="display:flex;align-items:center;justify-content:center;gap:1rem;flex-wrap:wrap;margin:1.4rem 0 0.4rem;">
  <img src="/shark.svg" alt="tubarão investidor" width="120" height="82" style="flex:0 0 auto;"/>
  <h2 style="text-align:center;margin:0;font-weight:800;">🏆 AHP-TOPSIS 2N — מודל החלטה רב-קריטריוני (MCDM)</h2>
  <img src="/gekko_photo.png" alt="Gordon Gekko fumando charuto (terno azul)" width="100" height="100" style="flex:0 0 auto;border-radius:50%;box-shadow:0 2px 8px rgba(0,0,0,.25);"/>
</div>

> **בחירת הפרויקט הטוב ביותר** על ידי שקלול המדדים כקריטריונים. משקלים לפי **AHP**
> (VPL 37% · TIR 24% · ILL 14% · PSR 14% · IITA 5,6% · IDLS 5,6% — CR = 0,012, consistente).
> Ranking por **TOPSIS** em **duas normalizações** (vetorial/Euclidiana + min-max/linear); o
> **Ci סופי** הוא הממוצע. עמודת **חסין?** = שתי הנרמולים מסכימים על המיקום.

**🥇 הפרויקט המנצח (Ci סופי הגבוה ביותר):**
<DataTable data={mcda_top}>
  <Column id=project_name title="🏆 הפרויקט הטוב ביותר"/>
  <Column id=ci_final title="Ci final" fmt=num4/>
</DataTable>

<BarChart data={mcda} x=project_name y=ci_final title="Ranking AHP-TOPSIS 2n (Ci final, 0–1)" swapXY=true sort=true labels=true/>

<DataTable data={mcda} rows=all rowShading=true>
  <Column id=rank_final title="#"/>
  <Column id=project_name title="פרויקט"/>
  <Column id=ci_vector title="Ci vetorial" fmt=num4/>
  <Column id=ci_minmax title="Ci min-max" fmt=num4/>
  <Column id=ci_final title="Ci final" fmt=num4/>
  <Column id=concordante title="חסין?" fmt=boolean/>
</DataTable>

> למנצח נוצר **פיצ'דק** (ראו תיקיית פרויקטים / `pitchdeck/`). היכן שמיקומים 6–7 מתפצלים בין הנרמולים, הדירוג הכי רגיש — החליטו שם בזהירות.

### 📌 שורה תחתונה — תקציר מנהלים ותובנות דרג בכיר

**פסק דין.** המודל **AHP-TOPSIS 2n** בוחר ב-**{mcda_top[0].project_name}** כפרויקט הטוב בתיק (**Ci = 0.96** מתוך 1.00), עם **חוסן מאושר**: שני הנרמולים (וקטורי ו-min-max) מסכימים על **המקום ה-1** ועל 8/10 מהדירוג — הצמרת יציבה, לא תוצר שיטה.

**מדוע {mcda_top[0].project_name} ניצח.** הקריטריונים ה**פיננסיים** (NPV R$ 5,973 · IRR 32.9% · ILL 1.75) **שווים** בין הפרויקטים (תזרים עדיין *מציין מיקום* אחיד). משנוטרל הפיננסי, ההחלטה עוברת ל**יעילות תפעולית**, ושם {mcda_top[0].project_name} שולט: **שיעור ההזיה הנמוך ביותר (IITA 9.1%)** וה**בזבוז הרזה הנמוך ביותר (IDLS 15.0%)** בתיק — כמעט **מחצית** מהמקום ה-2. במילים אחרות: **אותה תשואה צפויה, בביצוע עם הרבה פחות בזבוז טוקנים/מזומן.**

**תובנות דרג בכיר.**
- 🥇 **היעילות היא השובר-שוויון:** כשהתשואה דומה, מי ש**שורף פחות** (IITA/IDLS נמוכים) מספק אותו ערך במרווח גבוה יותר — הנכס בר-ההרחבה ביותר.
- 🛡️ **חוסן החלטה:** ההסכמה בין שני הנרמולים (8/10) מעניקה לדירקטוריון **ביטחון** לפעול בראש הדירוג; האזור הרגיש (מיקומים 6–7) דורש ניתוח איכותני לפני קיצוץ.
- 📉 **זנב סיכון:** המדורג האחרון (Ci 0.01) בעל הביצוע המשולב הגרוע ביותר — מועמד ל**רפקטורינג או הפסקה** (הצלבה עם מטריצת BCG).

**⚠️ הסתייגות של יושר החלטה.** הקריטריונים הפיננסיים נושאים **75% ממשקל ה-AHP** (NPV 37% + IRR 24% + ILL 14%), אך היום **אינם מבחינים** כי התזרים הוא מציין מיקום. **הפסיקה סופית רק עם תזרימי מזומנים אמיתיים לכל פרויקט** — עם הזנתם הדירוג עשוי להשתנות מהותית (הפיננסי ישוב לשלוט).

**המלצה.** (1) לאשר את {mcda_top[0].project_name} כ**פיילוט הרחבה** בזכות היעילות המוכחת; (2) להזין את **תזרימי המזומנים האמיתיים** ולהריץ מחדש את `ahp_topsis.py` לפסיקה פיננסית סופית; (3) להפעיל תוכנית שיפור בזנב (המדורג האחרון).

---
## 👑 תיק מנהלי של **תכשיט הכתר** — {mcda_top[0].project_name}

> כלים ניהוליים קלאסיים המיושמים **אך ורק על הפרויקט הנבחר** כדי להעשירו, להבליטו ולהדגיש את ה**יתרון התחרותי** שלו. כולם נוצרים על ידי **צינור Python מקבילי** (`gerar_admtools.py`) — ללא תבנית חיצונית. פירוט ונימוק ב-`foundations/admtools/ferramentas_administrativas.md`.

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:1.2rem;margin:1rem 0;">

<div>

**🎯 SWOT — מיצוב אסטרטגי**
חוזקות/חולשות/הזדמנויות/איומים מ-KPI אמיתיים (IITA ו-IDLS הנמוכים = חוזקה דומיננטית).
<img src="/admtools/swot.png" alt="SWOT do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🌐 PESTELC — סביבת מאקרו**
שבעה גורמים חיצוניים (פוליטי, כלכלי, חברתי, טכנולוגי, אקולוגי, משפטי, תרבותי).
<img src="/admtools/pestel.png" alt="PESTELC do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🗺️ 5W4H — תוכנית פעולה (5W + 4H)**
What/Why/Where/When/Who + How/How much/How many/How long — מפת דרכים להרחבת הפרויקט הנבחר.
<img src="/admtools/5w4h.png" alt="5W4H do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**📊 פארטו של כשלים (80/20)**
קטגוריות פרומפט המרכזות 80% מהכשלים — היכן לתקוף ראשון (נתוני Langfuse אמיתיים).
<img src="/admtools/pareto.png" alt="Pareto de falhas do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🔥 מטריצת GUT — תעדוף (מפת חום)**
חומרה × דחיפות × מגמה של הפעולות; GUT גבוה = לפעול ראשון.
<img src="/admtools/gut.png" alt="Matriz GUT do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🕸️ ראדאר תחרותי — בידול**
טביעת האצבע של הנבחר **מול ממוצע התיק** (השטח הכחול שולט באפור כמעט בכל ציר).
<img src="/admtools/radar.png" alt="Radar competitivo do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>

</div>

> **📌 קריאה ניהולית.** ה**ראדאר** מצייר את היתרון התחרותי: תכשיט הכתר עולה על הממוצע באנטי-הזיה, Lean ומסירה מועילה. **SWOT/PESTEL/5W4H** הופכים אבחון זה ל**אסטרטגיה ותוכנית פעולה**; **Pareto + GUT** אומרים **בדיוק היכן** לפעול ראשון כדי להמיר מנהיגות תפעולית לתשואה פיננסית סופית.

---
## 🔗 לוחות נפרדים לפי פרויקט

{#each kpis as p}
<a href="/projetos/{p.project_name}">▶️ {p.project_name} — PSR {p.kpi_psr}</a>
{/each}
