---
title: BSC 面板 — AI 项目管理（PM）
---

🌐 [Português](/) · [English](/en) · [Español](/es) · [Français](/fr) · [Deutsch](/de) · **中文** · [한국어](/ko) · [हिन्दी](/hi) · [עברית](/he) · [Svenska](/sv) · [Русский](/ru) · [Suomi](/fi)


🌐 **Português** · [English](/en) · [Español](/es) · [Français](/fr) · [Deutsch](/de) · [中文](/zh) · [한국어](/ko) · [हिन्दी](/hi)


_Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com_
**每周检查点 — 每周五 09:00。**

> ⚠️ **演示数据**（匿名组合）。Langfuse 同步后即为真实数据。

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

## 📈 组合执行摘要

<BigValue data={kpis} value=total_tokens title="总 Token 数" agg=sum fmt=num0/>
<BigValue data={kpis} value=kpi_psr title="平均 PSR (0-5)" agg=mean fmt=num1/>
<BigValue data={kpis} value=kpi_idls_lean title="平均精益浪费 %" agg=mean fmt=num1/>
<BigValue data={kpis} value=burn_rate_ia title="总消耗率" agg=sum fmt='$#,##0.00'/>

## 🌐 组合 5D 地图（C 级视图）
> 3D 球体（5dchart 风格）——**每项目 5 维**：**X**=规模（Token）· **Y**=PEUC/质量 (%) · **Z**=PSR/健康 (0–5) · **大小**=消耗率 (R$) · **颜色**=ICCA/可持续性（🟢 高于 3x 覆盖成本 · 🔴 低于 1x = 亏损）。
>
> **董事会解读：** 理想项目位于**右/后**（规模+质量）、**高**（PSR）且**绿色**（可持续）。**又大又红**的球 = 大量现金消耗且无覆盖 → 先修复再扩展。

![Mapa 5D do Portfólio de Projetos de IA](/5d_projetos.png?v=5)

### 🖱️ 交互式 5D 地图 — 将鼠标悬停在每个球体上
> **X** = Token（规模）· **Y** = PEUC (%) · **大小** = PSR (0–5) · **颜色** = ICCA（🟢 可持续 · 🟠 临界 · 🔴 亏损）。将鼠标悬停在每个**光泽球体**上，可见**项目名称、PSR、PEUC 和 Token**。

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

## 📉 主指标 (CPP) 与评分 (PSR) 趋势
> 对 C 级最重要的是**方向**。CPP 下降 = 组合更高效。

<LineChart data={tendencia} x=data_snapshot y=cpp_medio yAxisTitle="CPP médio (R$/%)" title="每进度点成本 — 组合趋势" markers=true/>

<LineChart data={tendencia} x=data_snapshot y=psr_medio yAxisTitle="PSR médio" yMin=0 yMax=5 title="组合平均评分 (PSR 0-5)" markers=true/>

## ⭐ 各项目评分 (PSR)

<BarChart data={kpis} x=project_name y=kpi_psr swapXY=true title="各项目 PSR (0-5) — 已排序" sort=true labels=true/>

## 🍩 构成与占比（带景深的环形图）

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

## 🧭 可持续性象限（扩展还是修复？）
> X 轴 = **ICCA**（覆盖：高于 3x = 健康）· Y 轴 = **IBMT**（边际消耗：低于 0.33 = 好）· 大小 = 消耗率。
> 右下角 = **盈利扩展**；左上角 = **增长前先修复**。

<ScatterPlot data={kpis} x=kpi_icca y=kpi_ibmt series=project_name size=burn_rate_ia xAxisTitle="ICCA — cobertura de custo (x)" yAxisTitle="IBMT — burn marginal (x)" title="各项目财务可持续性"/>

## 📊 各项目故障帕累托

<BarChart data={falhas} x=project_name y=percentual_dominancia series=categoria_falha type=stacked100 swapXY=true title="各项目故障占比 (%)"/>

## 🗂️ 评分与财务健康（表格）

<DataTable data={kpis} rows=all rowShading=true>
  <Column id=project_name title="项目"/>
  <Column id=kpi_psr title="PSR" fmt=num2/>
  <Column id=kpi_peuc title="PEUC %" fmt=num1/>
  <Column id=kpi_iita title="IITA %" fmt=num1/>
  <Column id=kpi_idls_lean title="IDLS %" fmt=num1/>
  <Column id=vrt_por_ktoken title="VRT/kT" fmt='$#,##0.0000'/>
  <Column id=kpi_icca title="ICCA x" fmt=num2/>
  <Column id=kpi_ibmt title="IBMT x" fmt=num3/>
  <Column id=kpi_cpp title="CPP R$/%" fmt='$#,##0.00'/>
</DataTable>

## 🚨 关键告警

<DataTable data={alertas} rows=8>
  <Column id=project_name title="项目"/>
  <Column id=tipo_erro title="故障"/>
  <Column id=tokens_desperdicados title="Tokens" fmt=num0/>
  <Column id=data_evento title="时间"/>
</DataTable>

## 📅 每周会议议程

<DataTable data={reuniao} rows=all>
  <Column id=project_name title="项目"/>
  <Column id=sumario_executivo title="摘要"/>
  <Column id=acoes_corretivas_lean title="精益行动 (PDCA)"/>
</DataTable>

## 🪙 成本回收 (VRT) — 5 个分块 + 平均值（第二视角）
> 相同分摊基准的 **5 种粒度**（每 50/100/250/500/1000 Token 的 R$）+ **分块平均** — 项目消耗的第二视角。

<DataTable data={kpis} rows=all rowShading=true>
  <Column id=project_name title="项目"/>
  <Column id=vrt_50t title="50 tok" fmt='#,##0.00000'/>
  <Column id=vrt_100t title="100 tok" fmt='#,##0.00000'/>
  <Column id=vrt_250t title="250 tok" fmt='#,##0.00000'/>
  <Column id=vrt_500t title="500 tok" fmt='#,##0.00000'/>
  <Column id=vrt_por_ktoken title="1.000 tok" fmt='#,##0.00000'/>
  <Column id=vrt_media_blocos title="平均分块" fmt='#,##0.00000' contentType=colorscale/>
</DataTable>

## ⏰ 关键中断/影响时段 (HCI)
> 每个项目在**一天中的哪个时段 (BRT)** 受影响最大 — 以便在正确窗口行动（升级 Tier、退避、排程）。

<BarChart data={hora_total} x=hora_brt y=interrupcoes title="按小时的中断 (BRT) — 组合" xAxisTitle="Hora (0-23, BRT)"/>

<DataTable data={horario_critico} rows=all rowShading=true>
  <Column id=project_name title="项目"/>
  <Column id=hora_pico title="高峰时段 (BRT)" fmt='0"h"'/>
  <Column id=interrupcoes_pico title="高峰中断数" fmt=num0/>
</DataTable>

## ♻️ 浪费分类 (Lean Six Sigma) — 浪费最多之处
> 浪费以**加权 Token** 衡量（缺陷 2.0× · 配额 1.5× · 过度处理 1.0× · 延迟 0.5×），而非仅按数量。

<Grid cols=2>
<Group>

**组合浪费构成**
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

**各项目主要浪费**
<DataTable data={waste_dom} rows=all>
  <Column id=project_name title="项目"/>
  <Column id=waste_dominante title="主要浪费"/>
  <Column id=waste_tokens title="浪费的 Token" fmt=num0/>
</DataTable>

</Group>
</Grid>

<BarChart data={wastes} x=project_name y=waste_tokens series=categoria_waste type=stacked swapXY=true title="浪费构成（加权 Token）按项目"/>

## 🔬 RCA — 按提示词类型的幻觉（是什么在拖慢每个项目）
> 根因分析：将提示词分为**类别**并测量每类的幻觉。
> 客观诊断**是什么拖慢每个项目**以及**共同拖慢所有项目的是什么（交集）**。

### 🎯 交集 — 组合共有的瓶颈
> 在最多项目中作为**头号幻觉瓶颈**的提示词类型。优先攻克它具有最大的系统性效果。

<BarChart data={rca_inter} x=prompt_categoria y=projetos_onde_e_top1 title="最拖慢组合的提示词类型（N 个项目中的头号瓶颈）" yAxisTitle="Nº de projetos onde é o gargalo #1" labels=true sort=true/>

### 🧭 各项目的幻觉瓶颈（单项 RCA）

<DataTable data={rca_proj} rows=all rowShading=true>
  <Column id=project_name title="项目"/>
  <Column id=prompt_gargalo title="最易幻觉的提示词（瓶颈）"/>
  <Column id=alucinacoes title="幻觉数" fmt=num0/>
</DataTable>

### 📊 按类别 × 项目的幻觉分类

<BarChart data={aluc_cat} x=project_name y=alucinacoes series=prompt_categoria type=stacked swapXY=true title="各项目按提示词类型的幻觉"/>

## 💰 NPV、回收期与组合现金流
> 根据**您的现金流**计算（CSV/表格 — 见 `pipeline/fluxo_caixa_template.csv` 与 `python3 carregar_fluxo.py 您的.csv`）。NPV = Σ 流量 ÷ (1+i)ᵗ · 回收期**简单**（时间插值）与**贴现**，均为插值。_在您提供 CSV 之前为演示数据。_

<DataTable data={vpl} rows=all rowShading=true>
  <Column id=project_name title="项目"/>
  <Column id=vpl title="VPL (R$)" fmt='$#,##0' contentType=colorscale/>
  <Column id=tir title="TIR" fmt=pct1/>
  <Column id=tirm title="TIRM" fmt=pct1/>
  <Column id=ill title="ILL (PI)" fmt=num2/>
  <Column id=vul title="VUL (R$)" fmt='$#,##0'/>
  <Column id=payback_simples title="简单回收期" fmt=num2/>
  <Column id=payback_descontado title="贴现回收期" fmt=num2/>
  <Column id=supera_selic title="TIR>SELIC?" fmt=boolean/>
  <Column id=supera_us title="TIR>EUA?" fmt=boolean/>
  <Column id=vpl_usd title="VPL US$" fmt='$#,##0'/>
  <Column id=payback_desc_usd title="PB desc. US$" fmt=num2/>
</DataTable>

> 🆕 **TIRM**（修正内部收益率）以项目利率再投资流入 — 比 IRR 更现实。**VUL**（净均一价值）将 NPV 转换为等额年金序列。

> **TIR** = retorno do projeto · **ILL (PI)** acima de 1 = cria valor · comparados à **SELIC** e aos **juros dos EUA** (valores reais por projeto na tabela acima — colunas `TIR>SELIC?`/`TIR>EUA?`). O fluxo é **dolarizado** (USD/BRL) e descontado à taxa americana → colunas **VPL US$** e **PB desc. US$**. _Benchmarks (SELIC, juros EUA, câmbio) são placeholders — ajuste no `.env`._

**各项目 IRR vs. 机会成本（SELIC × 美国）**

<BarChart data={vpl} x=project_name y=tir title="TIR por projeto comparada à SELIC e aos juros dos EUA" yAxisTitle="TIR (por período)" sort=true>
  <ReferenceLine y=0.105 color=warning label="SELIC (BR) ~10,5%"/>
  <ReferenceLine y=0.045 color=info label="Juros EUA ~4,5%"/>
</BarChart>

**Recuperação do investimento ao longo do tempo** (acumulado descontado — cruza zero = payback descontado)

<LineChart data={vpl_fluxo} x=periodo y=cum_desc series=project_name title="Fluxo de caixa acumulado descontado por período" yAxisTitle="Acumulado descontado (R$)" markers=true>
  <ReferenceLine y=0 color=negative label="break-even"/>
</LineChart>

## 💳 AI 订阅计划 — 含 IOF 总成本
> 汇率 **R$ 5.40/US$** · 国际操作（信用卡）**IOF 3.5%**。`总额 = US$ × 汇率 × (1 + IOF)`。
> 这是喂入分摊基准（`assinaturas_infra`）的真实成本。价格为近似值 — 请查阅官方网站。

<DataTable data={planos} rows=all rowShading=true>
  <Column id=provedor title="提供商"/>
  <Column id=plano title="计划"/>
  <Column id=usd_mes title="US$/mês" fmt=num0/>
  <Column id=r_base title="R$ base" fmt='$#,##0.00'/>
  <Column id=iof_reais title="IOF" fmt='$#,##0.00'/>
  <Column id=total_iof title="Total c/ IOF (R$)" fmt='$#,##0.00'/>
</DataTable>

<BarChart data={planos_pagos} x=plano y=total_iof title="Custo total mensal com IOF por plano (R$)" swapXY=true sort=true/>

<div style="display:flex;align-items:center;justify-content:center;gap:1rem;flex-wrap:wrap;margin:1.4rem 0 0.4rem;">
  <img src="/shark.svg" alt="tubarão investidor" width="120" height="82" style="flex:0 0 auto;"/>
  <h2 style="text-align:center;margin:0;font-weight:800;">🏆 AHP-TOPSIS 2N — 多准则决策模型 (MCDM)</h2>
  <img src="/gekko_photo.png" alt="Gordon Gekko fumando charuto (terno azul)" width="100" height="100" style="flex:0 0 auto;border-radius:50%;box-shadow:0 2px 8px rgba(0,0,0,.25);"/>
</div>

> 通过将指标作为准则加权来**选择最佳项目**。权重由 **AHP**
> (VPL 37% · TIR 24% · ILL 14% · PSR 14% · IITA 5,6% · IDLS 5,6% — CR = 0,012, consistente).
> Ranking por **TOPSIS** em **duas normalizações** (vetorial/Euclidiana + min-max/linear); o
> **Ci 终值**为平均。**稳健？**列 = 两种归一化在位次上一致。

**🥇 获胜项目（最高 Ci 终值）：**
<DataTable data={mcda_top}>
  <Column id=project_name title="🏆 最佳项目"/>
  <Column id=ci_final title="Ci final" fmt=num4/>
</DataTable>

<BarChart data={mcda} x=project_name y=ci_final title="Ranking AHP-TOPSIS 2n (Ci final, 0–1)" swapXY=true sort=true labels=true/>

<DataTable data={mcda} rows=all rowShading=true>
  <Column id=rank_final title="#"/>
  <Column id=project_name title="项目"/>
  <Column id=ci_vector title="Ci vetorial" fmt=num4/>
  <Column id=ci_minmax title="Ci min-max" fmt=num4/>
  <Column id=ci_final title="Ci final" fmt=num4/>
  <Column id=concordante title="稳健？" fmt=boolean/>
</DataTable>

> 获胜者已生成**路演材料**（见 项目 文件夹 / `pitchdeck/`）。当第 6–7 位在归一化间分歧时，排名最敏感 — 在此谨慎决策。

### 📌 结论 — 执行摘要与 C 级洞察

**结论。** **AHP-TOPSIS 2n** 模型选出 **{mcda_top[0].project_name}** 为组合最佳项目（**Ci = 0.96**（满分 1.00）），且**稳健性已确认**：两种归一化（向量与 min-max）在**第 1 位**及排名的 8/10 上一致 — 榜首稳定，并非方法假象。

**{mcda_top[0].project_name} 为何胜出。** **财务**准则（NPV R$ 5,973 · IRR 32.9% · ILL 1.75）在各项目间**打平**（现金流仍为统一*占位*）。财务被中和后，决策转向**运营效率**，此时 {mcda_top[0].project_name} 胜出：拥有全组合**最低幻觉率（IITA 9.1%）**与**最低精益浪费（IDLS 15.0%）**——几乎是第 2 名浪费的**一半**。换言之：**同等预期回报，却以远少的 Token/现金浪费执行。**

**C 级洞察。**
- 🥇 **效率是决胜点：** 回报相近时，谁**消耗更少**（更低 IITA/IDLS）就以更高利润率交付同等价值 — 最可扩展的资产。
- 🛡️ **决策稳健性：** 两种归一化的一致（8/10）让董事会有**把握**在榜首行动；敏感区间（第 6–7 位）在裁撤前需定性分析。
- 📉 **风险长尾：** 末位项目（Ci 0.01）综合表现最差 — **重构或停用**的候选（与 BCG 矩阵交叉验证）。

**⚠️ 决策诚实性提醒。** 财务准则占 **AHP 权重的 75%**（NPV 37% + IRR 24% + ILL 14%），但目前因现金流为占位而**无法区分**。**唯有各项目的真实现金流才能得出最终结论** — 一旦录入，排名可能大幅变化（财务将重新主导）。

**建议。**（1）以已验证的效率批准 {mcda_top[0].project_name} 作为**扩展试点**；（2）录入**真实现金流**并重跑 `ahp_topsis.py` 得出最终财务结论；（3）对长尾（末位项目）启动改进计划。

---
## 👑 **皇冠明珠**行政档案 — {mcda_top[0].project_name}

> 经典管理工具**专门应用于当选项目**，以丰富、彰显并凸显其**竞争优势**。全部由**并发 Python 流水线**（`gerar_admtools.py`）生成 — 不依赖任何外部模板。详见 `foundations/admtools/ferramentas_administrativas.md`。

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:1.2rem;margin:1rem 0;">

<div>

**🎯 SWOT — 战略定位**
基于真实 KPI 的优势/劣势/机会/威胁（最低 IITA 与 IDLS = 主导优势）。
<img src="/admtools/swot.png" alt="SWOT do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🌐 PESTELC — 宏观环境**
七个外部因素（政治、经济、社会、技术、生态、法律、文化）。
<img src="/admtools/pestel.png" alt="PESTELC do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🗺️ 5W4H — 行动计划（5W + 4H）**
What/Why/Where/When/Who + How/How much/How many/How long — 当选项目的扩展路线图。
<img src="/admtools/5w4h.png" alt="5W4H do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**📊 故障帕累托（80/20）**
集中 80% 故障的提示词类别 — 优先攻克之处（Langfuse 真实数据）。
<img src="/admtools/pareto.png" alt="Pareto de falhas do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🔥 GUT 矩阵 — 优先级排序（热力图）**
行动的严重性 × 紧急性 × 趋势；GUT 越高 = 越先行动。
<img src="/admtools/gut.png" alt="Matriz GUT do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🕸️ 竞争雷达 — 差异化**
当选项目的指纹**对比组合平均**（蓝色区域在几乎每个轴上都压制灰色）。
<img src="/admtools/radar.png" alt="Radar competitivo do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>

</div>

> **📌 高管解读。** **雷达**刻画竞争优势：皇冠明珠在抗幻觉、精益与有效交付上超过平均。**SWOT/PESTEL/5W4H** 将该诊断转化为**战略与行动计划**；**Pareto + GUT** 指出**优先在何处**行动，以将运营领先转化为最终财务回报。

---
## 🔗 各项目独立面板

{#each kpis as p}
<a href="/projetos/{p.project_name}">▶️ {p.project_name} — PSR {p.kpi_psr}</a>
{/each}
