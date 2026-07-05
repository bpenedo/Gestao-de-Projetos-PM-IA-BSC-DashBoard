---
title: BSC 패널 — AI 프로젝트 관리(PM)
---

🌐 [Português](/) · [English](/en) · [Español](/es) · [Français](/fr) · [Deutsch](/de) · [中文](/zh) · **한국어** · [हिन्दी](/hi) · [עברית](/he) · [Svenska](/sv) · [Русский](/ru) · [Suomi](/fi)


🌐 **Português** · [English](/en) · [Español](/es) · [Français](/fr) · [Deutsch](/de) · [中文](/zh) · [한국어](/ko) · [हिन्दी](/hi)


_Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com_
**주간 체크포인트 — 매주 금요일 09:00.**

> ⚠️ **데모 데이터**(익명 포트폴리오). Langfuse 동기화 시 실제 데이터가 됩니다.

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

## 📈 포트폴리오 요약 보고

<BigValue data={kpis} value=total_tokens title="총 토큰" agg=sum fmt=num0/>
<BigValue data={kpis} value=kpi_psr title="평균 PSR (0-5)" agg=mean fmt=num1/>
<BigValue data={kpis} value=kpi_idls_lean title="평균 린 낭비 %" agg=mean fmt=num1/>
<BigValue data={kpis} value=burn_rate_ia title="총 소진율" agg=sum fmt='$#,##0.00'/>

## 🌐 포트폴리오 5D 지도 (C-레벨 관점)
> 3D 구체(5dchart 스타일) — **프로젝트당 5차원**: **X**=규모(토큰) · **Y**=PEUC/품질 (%) · **Z**=PSR/건전성 (0–5) · **크기**=Burn Rate (R$) · **색**=ICCA/지속가능성 (🟢 3x 이상 비용 회수 · 🔴 1x 미만 = 손실).
>
> **경영진 관점:** 이상적 프로젝트는 **오른쪽/뒤**(규모+품질), **높음**(PSR), **초록**(지속가능). **크고 빨간** 구체 = 커버리지 없이 많은 현금 소진 → 확장 전 개선.

![Mapa 5D do Portfólio de Projetos de IA](/5d_projetos.png?v=5)

### 🖱️ 인터랙티브 5D 지도 — 각 구체에 마우스를 올리세요
> **X** = 토큰(규모) · **Y** = PEUC (%) · **크기** = PSR (0–5) · **색** = ICCA (🟢 지속가능 · 🟠 경계 · 🔴 손실). 각 **글로시 구체**에 마우스를 올리면 **프로젝트명, PSR, PEUC, 토큰**이 표시됩니다.

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

## 📉 핵심 지표(CPP) 및 점수(PSR) 추세
> C-레벨에 가장 중요한 것: **방향**. CPP 하락 = 포트폴리오 효율화.

<LineChart data={tendencia} x=data_snapshot y=cpp_medio yAxisTitle="CPP médio (R$/%)" title="진척 포인트당 비용 — 포트폴리오 추세" markers=true/>

<LineChart data={tendencia} x=data_snapshot y=psr_medio yAxisTitle="PSR médio" yMin=0 yMax=5 title="포트폴리오 평균 점수 (PSR 0-5)" markers=true/>

## ⭐ 프로젝트별 점수 (PSR)

<BarChart data={kpis} x=project_name y=kpi_psr swapXY=true title="프로젝트별 PSR (0-5) — 정렬" sort=true labels=true/>

## 🍩 구성 및 믹스 (입체 도넛)

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

## 🧭 지속가능성 사분면 (확장 vs 개선?)
> X축 = **ICCA**(커버리지: 3x 이상 = 건전) · Y축 = **IBMT**(한계 소진: 0.33 미만 = 양호) · 크기 = Burn Rate.
> 우하단 = **수익성 있게 확장**; 좌상단 = **성장 전 개선**.

<ScatterPlot data={kpis} x=kpi_icca y=kpi_ibmt series=project_name size=burn_rate_ia xAxisTitle="ICCA — cobertura de custo (x)" yAxisTitle="IBMT — burn marginal (x)" title="프로젝트별 재무 지속가능성"/>

## 📊 프로젝트별 실패 파레토

<BarChart data={falhas} x=project_name y=percentual_dominancia series=categoria_falha type=stacked100 swapXY=true title="프로젝트별 실패 우세도 (%)"/>

## 🗂️ 점수 및 재무 건전성 (표)

<DataTable data={kpis} rows=all rowShading=true>
  <Column id=project_name title="프로젝트"/>
  <Column id=kpi_psr title="PSR" fmt=num2/>
  <Column id=kpi_peuc title="PEUC %" fmt=num1/>
  <Column id=kpi_iita title="IITA %" fmt=num1/>
  <Column id=kpi_idls_lean title="IDLS %" fmt=num1/>
  <Column id=vrt_por_ktoken title="VRT/kT" fmt='$#,##0.0000'/>
  <Column id=kpi_icca title="ICCA x" fmt=num2/>
  <Column id=kpi_ibmt title="IBMT x" fmt=num3/>
  <Column id=kpi_cpp title="CPP R$/%" fmt='$#,##0.00'/>
</DataTable>

## 🚨 중요 경고

<DataTable data={alertas} rows=8>
  <Column id=project_name title="프로젝트"/>
  <Column id=tipo_erro title="실패"/>
  <Column id=tokens_desperdicados title="Tokens" fmt=num0/>
  <Column id=data_evento title="시점"/>
</DataTable>

## 📅 주간 회의 안건

<DataTable data={reuniao} rows=all>
  <Column id=project_name title="프로젝트"/>
  <Column id=sumario_executivo title="요약"/>
  <Column id=acoes_corretivas_lean title="린 액션 (PDCA)"/>
</DataTable>

## 🪙 비용 회수 (VRT) — 5블록 + 평균 (제2 관점)
> 동일 배분 기준의 **5개 세분화**(50/100/250/500/1,000 토큰당 R$) + **블록 평균** — 프로젝트 소비의 두 번째 관점.

<DataTable data={kpis} rows=all rowShading=true>
  <Column id=project_name title="프로젝트"/>
  <Column id=vrt_50t title="50 tok" fmt='#,##0.00000'/>
  <Column id=vrt_100t title="100 tok" fmt='#,##0.00000'/>
  <Column id=vrt_250t title="250 tok" fmt='#,##0.00000'/>
  <Column id=vrt_500t title="500 tok" fmt='#,##0.00000'/>
  <Column id=vrt_por_ktoken title="1.000 tok" fmt='#,##0.00000'/>
  <Column id=vrt_media_blocos title="평균 블록" fmt='#,##0.00000' contentType=colorscale/>
</DataTable>

## ⏰ 핵심 중단/영향 시간대 (HCI)
> 각 프로젝트가 **하루 중 어느 시간대(BRT)**에 가장 영향받는지 — 올바른 창에서 대응(Tier 업그레이드, 백오프, 스케줄링).

<BarChart data={hora_total} x=hora_brt y=interrupcoes title="시간대별 중단 (BRT) — 포트폴리오" xAxisTitle="Hora (0-23, BRT)"/>

<DataTable data={horario_critico} rows=all rowShading=true>
  <Column id=project_name title="프로젝트"/>
  <Column id=hora_pico title="피크 시간 (BRT)" fmt='0"h"'/>
  <Column id=interrupcoes_pico title="피크 중단 수" fmt=num0/>
</DataTable>

## ♻️ 낭비 분류 (Lean Six Sigma) — 가장 많이 낭비되는 곳
> 낭비는 **가중 토큰**으로 측정(결함 2.0× · 쿼터 1.5× · 과처리 1.0× · 지연 0.5×), 단순 개수가 아님.

<Grid cols=2>
<Group>

**포트폴리오 낭비 믹스**
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

**프로젝트별 주요 낭비**
<DataTable data={waste_dom} rows=all>
  <Column id=project_name title="프로젝트"/>
  <Column id=waste_dominante title="주요 낭비"/>
  <Column id=waste_tokens title="낭비 토큰" fmt=num0/>
</DataTable>

</Group>
</Grid>

<BarChart data={wastes} x=project_name y=waste_tokens series=categoria_waste type=stacked swapXY=true title="낭비 구성(가중 토큰) 프로젝트별"/>

## 🔬 RCA — 프롬프트 유형별 환각 (각 프로젝트를 지연시키는 요인)
> 근본 원인 분석: 프롬프트를 **카테고리**로 분류하고 각각의 환각을 측정.
> **각 프로젝트를 지연시키는 것**과 **모두를 공통으로 지연시키는 것(교집합)**의 객관적 진단.

### 🎯 교집합 — 포트폴리오 공통 병목
> 가장 많은 프로젝트에서 **환각 병목 1위**인 프롬프트 유형. 이것을 먼저 공략하면 시스템적 효과가 가장 큼.

<BarChart data={rca_inter} x=prompt_categoria y=projetos_onde_e_top1 title="포트폴리오를 가장 지연시키는 프롬프트 유형(N개 프로젝트의 1위 병목)" yAxisTitle="Nº de projetos onde é o gargalo #1" labels=true sort=true/>

### 🧭 프로젝트별 환각 병목 (개별 RCA)

<DataTable data={rca_proj} rows=all rowShading=true>
  <Column id=project_name title="프로젝트"/>
  <Column id=prompt_gargalo title="환각이 가장 많은 프롬프트(병목)"/>
  <Column id=alucinacoes title="환각 수" fmt=num0/>
</DataTable>

### 📊 카테고리 × 프로젝트별 환각 분류

<BarChart data={aluc_cat} x=project_name y=alucinacoes series=prompt_categoria type=stacked swapXY=true title="각 프로젝트의 프롬프트 유형별 환각"/>

## 💰 NPV, 회수기간 및 포트폴리오 현금흐름
> **당신의 현금흐름**으로 계산(CSV/스프레드시트 — `pipeline/fluxo_caixa_template.csv` 및 `python3 carregar_fluxo.py 당신.csv` 참조). NPV = Σ 흐름 ÷ (1+i)ᵗ · 회수기간 **단순**(시간 보간) 및 **할인**, 둘 다 보간. _CSV 제공 전까지는 데모 데이터._

<DataTable data={vpl} rows=all rowShading=true>
  <Column id=project_name title="프로젝트"/>
  <Column id=vpl title="VPL (R$)" fmt='$#,##0' contentType=colorscale/>
  <Column id=tir title="TIR" fmt=pct1/>
  <Column id=tirm title="TIRM" fmt=pct1/>
  <Column id=ill title="ILL (PI)" fmt=num2/>
  <Column id=vul title="VUL (R$)" fmt='$#,##0'/>
  <Column id=payback_simples title="단순 PB" fmt=num2/>
  <Column id=payback_descontado title="할인 PB" fmt=num2/>
  <Column id=supera_selic title="TIR>SELIC?" fmt=boolean/>
  <Column id=supera_us title="TIR>EUA?" fmt=boolean/>
  <Column id=vpl_usd title="VPL US$" fmt='$#,##0'/>
  <Column id=payback_desc_usd title="PB desc. US$" fmt=num2/>
</DataTable>

> 🆕 **TIRM**(수정 IRR)은 유입을 프로젝트 금리로 재투자 — IRR보다 현실적. **VUL**(순균등가치)은 NPV를 등가 연간 시리즈로 변환.

> **TIR** = retorno do projeto · **ILL (PI)** acima de 1 = cria valor · comparados à **SELIC** e aos **juros dos EUA** (valores reais por projeto na tabela acima — colunas `TIR>SELIC?`/`TIR>EUA?`). O fluxo é **dolarizado** (USD/BRL) e descontado à taxa americana → colunas **VPL US$** e **PB desc. US$**. _Benchmarks (SELIC, juros EUA, câmbio) são placeholders — ajuste no `.env`._

**프로젝트별 IRR vs. 기회비용 (SELIC × 미국)**

<BarChart data={vpl} x=project_name y=tir title="TIR por projeto comparada à SELIC e aos juros dos EUA" yAxisTitle="TIR (por período)" sort=true>
  <ReferenceLine y=0.105 color=warning label="SELIC (BR) ~10,5%"/>
  <ReferenceLine y=0.045 color=info label="Juros EUA ~4,5%"/>
</BarChart>

**Recuperação do investimento ao longo do tempo** (acumulado descontado — cruza zero = payback descontado)

<LineChart data={vpl_fluxo} x=periodo y=cum_desc series=project_name title="Fluxo de caixa acumulado descontado por período" yAxisTitle="Acumulado descontado (R$)" markers=true>
  <ReferenceLine y=0 color=negative label="break-even"/>
</LineChart>

## 💳 AI 구독 요금제 — IOF 포함 총비용
> 환율 **R$ 5.40/US$** · 국제 거래(카드) **IOF 3.5%**. `총액 = US$ × 환율 × (1 + IOF)`.
> 배분 기준(`assinaturas_infra`)에 입력되는 실제 비용. 대략적 가격 — 공식 사이트 확인.

<DataTable data={planos} rows=all rowShading=true>
  <Column id=provedor title="제공자"/>
  <Column id=plano title="요금제"/>
  <Column id=usd_mes title="US$/mês" fmt=num0/>
  <Column id=r_base title="R$ base" fmt='$#,##0.00'/>
  <Column id=iof_reais title="IOF" fmt='$#,##0.00'/>
  <Column id=total_iof title="Total c/ IOF (R$)" fmt='$#,##0.00'/>
</DataTable>

<BarChart data={planos_pagos} x=plano y=total_iof title="Custo total mensal com IOF por plano (R$)" swapXY=true sort=true/>

<div style="display:flex;align-items:center;justify-content:center;gap:1rem;flex-wrap:wrap;margin:1.4rem 0 0.4rem;">
  <img src="/shark.svg" alt="tubarão investidor" width="120" height="82" style="flex:0 0 auto;"/>
  <h2 style="text-align:center;margin:0;font-weight:800;">🏆 AHP-TOPSIS 2N — 다기준 의사결정 모델 (MCDM)</h2>
  <img src="/gekko_photo.png" alt="Gordon Gekko fumando charuto (terno azul)" width="100" height="100" style="flex:0 0 auto;border-radius:50%;box-shadow:0 2px 8px rgba(0,0,0,.25);"/>
</div>

> 지표를 기준으로 가중하여 **최고 프로젝트 선정**. 가중치는 **AHP**
> (VPL 37% · TIR 24% · ILL 14% · PSR 14% · IITA 5,6% · IDLS 5,6% — CR = 0,012, consistente).
> Ranking por **TOPSIS** em **duas normalizações** (vetorial/Euclidiana + min-max/linear); o
> **최종 Ci**는 평균. **견고?** 열 = 두 정규화가 순위에 동의.

**🥇 우승 프로젝트(최고 최종 Ci):**
<DataTable data={mcda_top}>
  <Column id=project_name title="🏆 최고 프로젝트"/>
  <Column id=ci_final title="Ci final" fmt=num4/>
</DataTable>

<BarChart data={mcda} x=project_name y=ci_final title="Ranking AHP-TOPSIS 2n (Ci final, 0–1)" swapXY=true sort=true labels=true/>

<DataTable data={mcda} rows=all rowShading=true>
  <Column id=rank_final title="#"/>
  <Column id=project_name title="프로젝트"/>
  <Column id=ci_vector title="Ci vetorial" fmt=num4/>
  <Column id=ci_minmax title="Ci min-max" fmt=num4/>
  <Column id=ci_final title="Ci final" fmt=num4/>
  <Column id=concordante title="견고?" fmt=boolean/>
</DataTable>

> 우승자는 **피치덱**이 생성됨(프로젝트 폴더 / `pitchdeck/` 참조). 6–7위가 정규화 간에 갈리는 지점이 순위가 가장 민감 — 그곳은 신중히 결정.

### 📌 결론 — 요약 보고 및 C-레벨 인사이트

**판정.** **AHP-TOPSIS 2n** 모델은 **{mcda_top[0].project_name}**을(를) 포트폴리오 최고 프로젝트로 선정(**Ci = 0.96**/1.00), **견고성 확인**: 두 정규화(벡터·min-max)가 **1위**와 순위의 8/10에서 일치 — 최상위는 안정적이며 방법의 산물이 아님.

**{mcda_top[0].project_name}이(가) 이긴 이유.** **재무** 기준(NPV R$ 5,973 · IRR 32.9% · ILL 1.75)은 프로젝트 간 **동률**(현금흐름은 여전히 균일 *플레이스홀더*). 재무가 상쇄되자 결정은 **운영 효율**로 이동, 여기서 {mcda_top[0].project_name}이(가) 우위: 포트폴리오 최저 **환각률(IITA 9.1%)**과 최저 **린 낭비(IDLS 15.0%)** — 2위의 거의 **절반**. 즉: **동일한 예상 수익을 훨씬 적은 토큰/현금 낭비로 실행.**

**C-레벨 인사이트.**
- 🥇 **효율이 결정타:** 수익이 비슷하면 **덜 태우는**(낮은 IITA/IDLS) 쪽이 더 높은 마진으로 같은 가치를 전달 — 가장 확장 가능한 자산.
- 🛡️ **결정 견고성:** 두 정규화의 일치(8/10)는 이사회가 순위 최상단에서 행동할 **확신**을 줌; 민감 구간(6–7위)은 컷 전에 정성 분석 필요.
- 📉 **리스크 꼬리:** 최하위(Ci 0.01)는 종합 성과 최악 — **리팩터링 또는 중단** 후보(BCG 매트릭스와 교차 확인).

**⚠️ 의사결정 정직성 유의.** 재무 기준은 **AHP 가중치의 75%**(NPV 37% + IRR 24% + ILL 14%)를 차지하나, 현금흐름이 플레이스홀더라 현재는 **차별화되지 않음**. **프로젝트별 실제 현금흐름이 있어야 판정이 확정** — 입력 시 순위가 크게 바뀔 수 있음(재무가 다시 지배).

**권고.** (1) 검증된 효율로 {mcda_top[0].project_name}을(를) **확장 파일럿**으로 승인; (2) **실제 현금흐름**을 입력하고 `ahp_topsis.py`를 재실행해 최종 재무 판정; (3) 꼬리(최하위)에 개선 계획 가동.

---
## 👑 **왕관의 보석** 행정 도시에 — {mcda_top[0].project_name}

> 고전 관리 도구를 **선정 프로젝트에만** 적용해 이를 풍부하게 하고 부각하며 **경쟁 우위**를 드러냄. 모두 **동시성 Python 파이프라인**(`gerar_admtools.py`)으로 생성 — 외부 템플릿 불필요. 상세·근거는 `foundations/admtools/ferramentas_administrativas.md`.

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:1.2rem;margin:1rem 0;">

<div>

**🎯 SWOT — 전략적 위치**
실제 KPI 기반 강점/약점/기회/위협(최저 IITA·IDLS = 지배적 강점).
<img src="/admtools/swot.png" alt="SWOT do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🌐 PESTELC — 거시환경**
일곱 가지 외부 요인(정치, 경제, 사회, 기술, 생태, 법률, 문화).
<img src="/admtools/pestel.png" alt="PESTELC do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🗺️ 5W4H — 실행 계획 (5W + 4H)**
What/Why/Where/When/Who + How/How much/How many/How long — 선정 프로젝트의 확장 로드맵.
<img src="/admtools/5w4h.png" alt="5W4H do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**📊 실패 파레토 (80/20)**
실패의 80%가 집중된 프롬프트 카테고리 — 먼저 공략할 곳(실제 Langfuse 데이터).
<img src="/admtools/pareto.png" alt="Pareto de falhas do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🔥 GUT 매트릭스 — 우선순위 (히트맵)**
조치의 심각도 × 긴급도 × 경향; GUT 높을수록 = 먼저 실행.
<img src="/admtools/gut.png" alt="Matriz GUT do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🕸️ 경쟁 레이더 — 차별점**
선정 프로젝트의 지문 **vs 포트폴리오 평균**(파란 영역이 거의 모든 축에서 회색을 압도).
<img src="/admtools/radar.png" alt="Radar competitivo do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>

</div>

> **📌 경영진 관점.** **레이더**는 경쟁 우위를 그려냄: 왕관의 보석은 안티-환각·린·유효 산출에서 평균을 능가. **SWOT/PESTEL/5W4H**는 이 진단을 **전략과 실행 계획**으로 전환; **Pareto + GUT**는 운영 리더십을 확정적 재무 수익으로 전환하기 위해 **정확히 어디서** 먼저 행동할지 제시.

---
## 🔗 프로젝트별 개별 패널

{#each kpis as p}
<a href="/projetos/{p.project_name}">▶️ {p.project_name} — PSR {p.kpi_psr}</a>
{/each}
