---
title: Панель BSC — управление ИИ-проектами (PM)
---

🌐 [Português](/) · [English](/en) · [Español](/es) · [Français](/fr) · [Deutsch](/de) · [中文](/zh) · [한국어](/ko) · [हिन्दी](/hi) · [עברית](/he) · [Svenska](/sv) · **Русский** · [Suomi](/fi)


🌐 **Português** · [English](/en) · [Español](/es) · [Français](/fr) · [Deutsch](/de) · [中文](/zh) · [한국어](/ko) · [हिन्दी](/hi)


_Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com_
**Еженедельная сверка — каждую пятницу в 09:00.**

> ⚠️ **ДЕМО-данные** (анонимизированный портфель). Становятся реальными после синхронизации Langfuse.

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

## 📈 Сводка по портфелю

<BigValue data={kpis} value=total_tokens title="Всего токенов" agg=sum fmt=num0/>
<BigValue data={kpis} value=kpi_psr title="Средний PSR (0-5)" agg=mean fmt=num1/>
<BigValue data={kpis} value=kpi_idls_lean title="Средние Lean-потери %" agg=mean fmt=num1/>
<BigValue data={kpis} value=burn_rate_ia title="Общий Burn Rate" agg=sum fmt='$#,##0.00'/>

## 🌐 5D-карта портфеля (уровень C)
> 3D-сферы (стиль 5dchart) — **5 измерений на проект**: **X**=объём/масштаб (токены) · **Y**=PEUC/качество (%) · **Z**=PSR/здоровье (0–5) · **размер**=Burn Rate (R$) · **цвет**=ICCA/устойчивость (🟢 выше 3x покрывает затраты · 🔴 ниже 1x = убыток).
>
> **Взгляд совета:** идеальный проект — **справа/в глубине** (масштаб+качество), **высоко** (PSR) и **зелёный** (устойчивый). **Большая красная** сфера = много сожжённых денег без покрытия → исправить до масштабирования.

![Mapa 5D do Portfólio de Projetos de IA](/5d_projetos.png?v=5)

### 🖱️ Интерактивная 5D-карта — наведите курсор на каждую сферу
> **X** = токены (масштаб) · **Y** = PEUC (%) · **размер** = PSR (0–5) · **цвет** = ICCA (🟢 устойчиво · 🟠 на грани · 🔴 убыток). Наведите курсор на каждую **глянцевую сферу**, чтобы увидеть **название проекта, PSR, PEUC и токены**.

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

## 📉 Тренд ключевого индикатора (CPP) и оценки (PSR)
> Самое важное для C-уровня: **направление**. Падающий CPP = портфель становится эффективнее.

<LineChart data={tendencia} x=data_snapshot y=cpp_medio yAxisTitle="CPP médio (R$/%)" title="Стоимость на пункт прогресса — тренд портфеля" markers=true/>

<LineChart data={tendencia} x=data_snapshot y=psr_medio yAxisTitle="PSR médio" yMin=0 yMax=5 title="Средняя оценка портфеля (PSR 0-5)" markers=true/>

## ⭐ Оценка (PSR) по проектам

<BarChart data={kpis} x=project_name y=kpi_psr swapXY=true title="PSR (0-5) по проектам — сортировка" sort=true labels=true/>

## 🍩 Состав и структура (кольцевая диаграмма с глубиной)

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

## 🧭 Квадрант устойчивости (масштабировать или исправить?)
> Ось X = **ICCA** (покрытие: выше 3x = здорово) · Ось Y = **IBMT** (предельный burn: ниже 0,33 = хорошо) · размер = Burn Rate.
> Нижний правый угол = **масштабировать с прибылью**; верхний левый = **исправить до роста**.

<ScatterPlot data={kpis} x=kpi_icca y=kpi_ibmt series=project_name size=burn_rate_ia xAxisTitle="ICCA — cobertura de custo (x)" yAxisTitle="IBMT — burn marginal (x)" title="Финансовая устойчивость по проектам"/>

## 📊 Парето сбоев по проектам

<BarChart data={falhas} x=project_name y=percentual_dominancia series=categoria_falha type=stacked100 swapXY=true title="Доминирование сбоев (%) по проектам"/>

## 🗂️ Оценка и финансовое здоровье (таблица)

<DataTable data={kpis} rows=all rowShading=true>
  <Column id=project_name title="Проект"/>
  <Column id=kpi_psr title="PSR" fmt=num2/>
  <Column id=kpi_peuc title="PEUC %" fmt=num1/>
  <Column id=kpi_iita title="IITA %" fmt=num1/>
  <Column id=kpi_idls_lean title="IDLS %" fmt=num1/>
  <Column id=vrt_por_ktoken title="VRT/kT" fmt='$#,##0.0000'/>
  <Column id=kpi_icca title="ICCA x" fmt=num2/>
  <Column id=kpi_ibmt title="IBMT x" fmt=num3/>
  <Column id=kpi_cpp title="CPP R$/%" fmt='$#,##0.00'/>
</DataTable>

## 🚨 Критические оповещения

<DataTable data={alertas} rows=8>
  <Column id=project_name title="Проект"/>
  <Column id=tipo_erro title="Сбой"/>
  <Column id=tokens_desperdicados title="Tokens" fmt=num0/>
  <Column id=data_evento title="Когда"/>
</DataTable>

## 📅 Повестка еженедельного совещания

<DataTable data={reuniao} rows=all>
  <Column id=project_name title="Проект"/>
  <Column id=sumario_executivo title="Резюме"/>
  <Column id=acoes_corretivas_lean title="Lean-действия (PDCA)"/>
</DataTable>

## 🪙 Возмещение затрат (VRT) — 5 блоков + среднее (второй ракурс)
> Одна база распределения в **5 гранулярностях** (R$ за 50/100/250/500/1 000 токенов) + **среднее по блокам** — второй ракурс потребления по проектам.

<DataTable data={kpis} rows=all rowShading=true>
  <Column id=project_name title="Проект"/>
  <Column id=vrt_50t title="50 tok" fmt='#,##0.00000'/>
  <Column id=vrt_100t title="100 tok" fmt='#,##0.00000'/>
  <Column id=vrt_250t title="250 tok" fmt='#,##0.00000'/>
  <Column id=vrt_500t title="500 tok" fmt='#,##0.00000'/>
  <Column id=vrt_por_ktoken title="1.000 tok" fmt='#,##0.00000'/>
  <Column id=vrt_media_blocos title="СРЕДН. блоки" fmt='#,##0.00000' contentType=colorscale/>
</DataTable>

## ⏰ Критический час прерываний/влияния (HCI)
> В какой **час суток (BRT)** каждый проект затрагивается сильнее всего — чтобы действовать в нужном окне (апгрейд Tier, backoff, планирование).

<BarChart data={hora_total} x=hora_brt y=interrupcoes title="Прерывания по часам суток (BRT) — портфель" xAxisTitle="Hora (0-23, BRT)"/>

<DataTable data={horario_critico} rows=all rowShading=true>
  <Column id=project_name title="Проект"/>
  <Column id=hora_pico title="Пиковый час (BRT)" fmt='0"h"'/>
  <Column id=interrupcoes_pico title="Прерывания в пик" fmt=num0/>
</DataTable>

## ♻️ Таксономия потерь (Lean Six Sigma) — где больше всего потерь
> Потери измеряются **взвешенными токенами** (Дефект 2,0× · Квота 1,5× · Переобработка 1,0× · Задержка 0,5×), а не только количеством.

<Grid cols=2>
<Group>

**Структура потерь портфеля**
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

**Осн. потеря по проектам**
<DataTable data={waste_dom} rows=all>
  <Column id=project_name title="Проект"/>
  <Column id=waste_dominante title="Осн. потеря"/>
  <Column id=waste_tokens title="Потрач. токены" fmt=num0/>
</DataTable>

</Group>
</Grid>

<BarChart data={wastes} x=project_name y=waste_tokens series=categoria_waste type=stacked swapXY=true title="Состав потерь (взвешенные токены) по проектам"/>

## 🔬 RCA — галлюцинации по типу промпта (что ЗАДЕРЖИВАЕТ каждый проект)
> Анализ первопричин: мы классифицируем промпты по **категориям** и измеряем галлюцинацию каждой.
> Объективная диагностика **того, что задерживает каждый проект** и **что ОБЩЕ задерживает все (пересечение)**.

### 🎯 Пересечение — общее узкое место портфеля
> Тип промпта, являющийся **узким местом галлюцинаций №1** в наибольшем числе проектов. Устранение его первым даёт наибольший системный эффект.

<BarChart data={rca_inter} x=prompt_categoria y=projetos_onde_e_top1 title="Тип промпта, больше всего задерживающий портфель (узкое место #1 в N проектах)" yAxisTitle="Nº de projetos onde é o gargalo #1" labels=true sort=true/>

### 🧭 Узкое место галлюцинаций по проекту (индивидуальный RCA)

<DataTable data={rca_proj} rows=all rowShading=true>
  <Column id=project_name title="Проект"/>
  <Column id=prompt_gargalo title="Промпт с макс. галлюцинациями (узкое место)"/>
  <Column id=alucinacoes title="Галлюцинации" fmt=num0/>
</DataTable>

### 📊 Таксономия галлюцинаций по категории × проекту

<BarChart data={aluc_cat} x=project_name y=alucinacoes series=prompt_categoria type=stacked swapXY=true title="Галлюцинации по типу промпта в каждом проекте"/>

## 💰 NPV, окупаемость и денежный поток портфеля
> Рассчитано из **вашего денежного потока** (CSV/таблица — см. `pipeline/fluxo_caixa_template.csv` и `python3 carregar_fluxo.py ВАШ.csv`). NPV = Σ поток ÷ (1+i)ᵗ · Payback **простой** (временная вариация) и **дисконтированный**, оба интерполированы. _Демоданные, пока вы не предоставите свой CSV._

<DataTable data={vpl} rows=all rowShading=true>
  <Column id=project_name title="Проект"/>
  <Column id=vpl title="VPL (R$)" fmt='$#,##0' contentType=colorscale/>
  <Column id=tir title="TIR" fmt=pct1/>
  <Column id=tirm title="TIRM" fmt=pct1/>
  <Column id=ill title="ILL (PI)" fmt=num2/>
  <Column id=vul title="VUL (R$)" fmt='$#,##0'/>
  <Column id=payback_simples title="Простой PB" fmt=num2/>
  <Column id=payback_descontado title="Дисконт. PB" fmt=num2/>
  <Column id=supera_selic title="TIR>SELIC?" fmt=boolean/>
  <Column id=supera_us title="TIR>EUA?" fmt=boolean/>
  <Column id=vpl_usd title="VPL US$" fmt='$#,##0'/>
  <Column id=payback_desc_usd title="PB desc. US$" fmt=num2/>
</DataTable>

> 🆕 **TIRM** (модифицированная IRR) реинвестирует притоки по ставке проекта — реалистичнее IRR. **VUL** (чистая равномерная стоимость) переводит NPV в эквивалентный годовой ряд.

> **TIR** = retorno do projeto · **ILL (PI)** acima de 1 = cria valor · comparados à **SELIC** e aos **juros dos EUA** (valores reais por projeto na tabela acima — colunas `TIR>SELIC?`/`TIR>EUA?`). O fluxo é **dolarizado** (USD/BRL) e descontado à taxa americana → colunas **VPL US$** e **PB desc. US$**. _Benchmarks (SELIC, juros EUA, câmbio) são placeholders — ajuste no `.env`._

**IRR по проектам vs. альтернативные издержки (SELIC × США)**

<BarChart data={vpl} x=project_name y=tir title="TIR por projeto comparada à SELIC e aos juros dos EUA" yAxisTitle="TIR (por período)" sort=true>
  <ReferenceLine y=0.105 color=warning label="SELIC (BR) ~10,5%"/>
  <ReferenceLine y=0.045 color=info label="Juros EUA ~4,5%"/>
</BarChart>

**Recuperação do investimento ao longo do tempo** (acumulado descontado — cruza zero = payback descontado)

<LineChart data={vpl_fluxo} x=periodo y=cum_desc series=project_name title="Fluxo de caixa acumulado descontado por período" yAxisTitle="Acumulado descontado (R$)" markers=true>
  <ReferenceLine y=0 color=negative label="break-even"/>
</LineChart>

## 💳 Подписки на ИИ — полная стоимость с IOF
> Курс **R$ 5,40/US$** · **IOF 3,5%** на международную операцию (карта). `Итого = US$ × курс × (1 + IOF)`.
> Это реальная стоимость, питающая базу распределения (`assinaturas_infra`). Цены приблизительные — проверьте официальные сайты.

<DataTable data={planos} rows=all rowShading=true>
  <Column id=provedor title="Провайдер"/>
  <Column id=plano title="План"/>
  <Column id=usd_mes title="US$/mês" fmt=num0/>
  <Column id=r_base title="R$ base" fmt='$#,##0.00'/>
  <Column id=iof_reais title="IOF" fmt='$#,##0.00'/>
  <Column id=total_iof title="Total c/ IOF (R$)" fmt='$#,##0.00'/>
</DataTable>

<BarChart data={planos_pagos} x=plano y=total_iof title="Custo total mensal com IOF por plano (R$)" swapXY=true sort=true/>

<div style="display:flex;align-items:center;justify-content:center;gap:1rem;flex-wrap:wrap;margin:1.4rem 0 0.4rem;">
  <img src="/shark.svg" alt="tubarão investidor" width="120" height="82" style="flex:0 0 auto;"/>
  <h2 style="text-align:center;margin:0;font-weight:800;">🏆 AHP-TOPSIS 2N — многокритериальная модель принятия решений (MCDM)</h2>
  <img src="/gekko_photo.png" alt="Gordon Gekko fumando charuto (terno azul)" width="100" height="100" style="flex:0 0 auto;border-radius:50%;box-shadow:0 2px 8px rgba(0,0,0,.25);"/>
</div>

> **Выбор ЛУЧШЕГО проекта** путём взвешивания индикаторов как критериев. Веса через **AHP**
> (VPL 37% · TIR 24% · ILL 14% · PSR 14% · IITA 5,6% · IDLS 5,6% — CR = 0,012, consistente).
> Ranking por **TOPSIS** em **duas normalizações** (vetorial/Euclidiana + min-max/linear); o
> **Итоговый Ci** — среднее. Столбец **Устойчиво?** = обе нормализации согласны в позиции.

**🥇 Проект-победитель (наибольший итоговый Ci):**
<DataTable data={mcda_top}>
  <Column id=project_name title="🏆 Лучший проект"/>
  <Column id=ci_final title="Ci final" fmt=num4/>
</DataTable>

<BarChart data={mcda} x=project_name y=ci_final title="Ranking AHP-TOPSIS 2n (Ci final, 0–1)" swapXY=true sort=true labels=true/>

<DataTable data={mcda} rows=all rowShading=true>
  <Column id=rank_final title="#"/>
  <Column id=project_name title="Проект"/>
  <Column id=ci_vector title="Ci vetorial" fmt=num4/>
  <Column id=ci_minmax title="Ci min-max" fmt=num4/>
  <Column id=ci_final title="Ci final" fmt=num4/>
  <Column id=concordante title="Устойчиво?" fmt=boolean/>
</DataTable>

> У победителя сгенерирован **питч-дек** (см. папку Проекты / `pitchdeck/`). Там, где позиции 6–7 расходятся между нормализациями, ранжирование наиболее чувствительно — решайте осторожно.

### 📌 Итог — резюме и выводы для C-уровня

**Вердикт.** Модель **AHP-TOPSIS 2n** выбирает **{mcda_top[0].project_name}** лучшим проектом портфеля (**Ci = 0,96** из 1,00), с **подтверждённой устойчивостью**: обе нормализации (векторная и min-max) сходятся на **1-м месте** и в 8/10 рейтинга — вершина стабильна, а не артефакт метода.

**Почему победил {mcda_top[0].project_name}.** **Финансовые** критерии (NPV R$ 5 973 · IRR 32,9% · ILL 1,75) **равны** между проектами (денежный поток пока единый *заполнитель*). При нейтрализованных финансах решение смещается к **операционной эффективности**, и там {mcda_top[0].project_name} доминирует: наименьшая **доля галлюцинаций (IITA 9,1%)** и наименьшие **Lean-потери (IDLS 15,0%)** во всём портфеле — почти **половина** от второго места. Иначе говоря: **та же прогнозная доходность при куда меньших потерях токенов/денег.**

**Выводы для C-уровня.**
- 🥇 **Эффективность — решающий фактор:** при схожей доходности тот, кто **сжигает меньше** (ниже IITA/IDLS), даёт ту же ценность с большей маржой — самый масштабируемый актив.
- 🛡️ **Устойчивость решения:** согласие обеих нормализаций (8/10) даёт совету **уверенность** действовать в верхушке рейтинга; чувствительная зона (позиции 6–7) требует качественного анализа перед отсечением.
- 📉 **Хвост риска:** последний в рейтинге (Ci 0,01) имеет худшую совокупную результативность — кандидат на **рефакторинг или прекращение** (сверить с матрицей BCG).

**⚠️ Оговорка о честности решения.** Финансовые критерии несут **75% веса AHP** (NPV 37% + IRR 24% + ILL 14%), но сегодня **не различают**, так как денежный поток — заполнитель. **Вердикт окончателен лишь с РЕАЛЬНЫМИ денежными потоками по проектам** — после ввода рейтинг может существенно измениться (финансы снова возьмут верх).

**Рекомендация.** (1) Утвердить {mcda_top[0].project_name} как **пилот масштабирования** за доказанную эффективность; (2) ввести **реальные денежные потоки** и перезапустить `ahp_topsis.py` для окончательного финансового вердикта; (3) запустить план улучшения для хвоста (последнего в рейтинге).

---
## 👑 Административное досье **Жемчужины короны** — {mcda_top[0].project_name}

> Классические административные инструменты, применённые **исключительно к выбранному проекту**, чтобы обогатить, возвысить и показать его **конкурентное преимущество**. Все генерируются **конкурентным Python-конвейером** (`gerar_admtools.py`) — без внешних шаблонов. Детали и обоснование в `foundations/admtools/ferramentas_administrativas.md`.

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:1.2rem;margin:1rem 0;">

<div>

**🎯 SWOT — стратегическая позиция**
Сильные/слабые стороны/возможности/угрозы, выведенные из реальных KPI (наименьшие IITA и IDLS = доминирующая сила).
<img src="/admtools/swot.png" alt="SWOT do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🌐 PESTELC — макросреда**
Семь внешних факторов (политические, экономические, социальные, технологические, экологические, правовые, культурные).
<img src="/admtools/pestel.png" alt="PESTELC do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🗺️ 5W4H — план действий (5W + 4H)**
What/Why/Where/When/Who + How/How much/How many/How long — дорожная карта масштабирования выбранного проекта.
<img src="/admtools/5w4h.png" alt="5W4H do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**📊 Парето сбоев (80/20)**
Категории промптов, дающие 80% сбоев — куда бить в первую очередь (реальные данные Langfuse).
<img src="/admtools/pareto.png" alt="Pareto de falhas do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🔥 Матрица GUT — приоритизация (тепловая карта)**
Тяжесть × Срочность × Тенденция действий; выше GUT = действовать первым.
<img src="/admtools/gut.png" alt="Matriz GUT do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🕸️ Конкурентный радар — отличие**
Отпечаток выбранного проекта **против среднего по портфелю** (синяя область доминирует над серой почти по каждой оси).
<img src="/admtools/radar.png" alt="Radar competitivo do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>

</div>

> **📌 Управленческое чтение.** **Радар** отражает конкурентное преимущество: Жемчужина короны превосходит среднее по анти-галлюцинации, Lean и полезной отдаче. **SWOT/PESTEL/5W4H** превращают диагноз в **стратегию и план действий**; **Pareto + GUT** указывают, **где именно** действовать в первую очередь, чтобы превратить операционное лидерство в окончательную финансовую отдачу.

---
## 🔗 Отдельные панели по проектам

{#each kpis as p}
<a href="/projetos/{p.project_name}">▶️ {p.project_name} — PSR {p.kpi_psr}</a>
{/each}
