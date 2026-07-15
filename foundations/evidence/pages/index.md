---
title: Painel BSC — Gestão de Projetos (PM) IA
---

🌐 **Português** · [English](/en) · [Español](/es) · [Français](/fr) · [Deutsch](/de) · [中文](/zh) · [한국어](/ko) · [हिन्दी](/hi)


_Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com_
**Weekly Checkpoint — toda sexta-feira às 09:00.**

> ⚠️ **Dados DEMO** (portfólio anonimizado). Tornam-se reais quando o Langfuse sincronizar.

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
```sql orc_global
select * from bsc.orcamento_global
```

```sql orc_rateio
select * from bsc.orcamento_rateio order by tokens_mes desc
```

```sql orc_cota
select * from bsc.orcamento_cota order by pct_uso desc
```

```sql orc_admissao
select * from bsc.orcamento_admissao order by cenario
```

```sql cont_cenario
select * from bsc.contencao_cenario
```

```sql cont_projeto
select * from bsc.contencao_projeto order by saldo desc
```

```sql admissao
select * from bsc.admissao_politica order by ordem_corte
```

```sql orc_loop
select * from bsc.pm_agent_orcamento order by whatif_brl desc
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
```sql mc_vpl
select project_name, iteracoes, media, desvio_padrao, minimo, maximo,
       assimetria, curtose, coef_variacao, prob_menor_zero, var_5, cvar_5
from bsc.mc_estatisticas where variavel = 'VPL' order by var_5 desc
```
```sql mc_percentis_vpl
select project_name, percentil, valor from bsc.mc_percentis
where variavel = 'VPL' and percentil % 5 = 0 order by percentil
```
```sql dematel
select rotulo, r, c, prominencia, relacao, papel, peso
from bsc.dematel_criterio order by prominencia desc
```
```sql mcdm_rank
select project_name, metodo, score, rank_ from bsc.decisao_mcdm order by metodo, rank_
```
```sql consenso
select c.project_name, c.rank_medio, c.borda, c.rank_final, c.unanime,
       m.prob_menor_zero, m.var_5
from bsc.decisao_consenso c
left join bsc.mc_estatisticas m
  on m.project_name = c.project_name and m.variavel = 'VPL'
order by c.rank_final
```
```sql consenso_top
select * from bsc.decisao_consenso where rank_final = 1
```
```sql robustez
select project_name, prob_vitoria, prob_top3, rank_medio, rank_p05, rank_p95
from bsc.mcdm_robustez where metodo = 'CONSENSO (Borda)' order by prob_vitoria desc
```
```sql robustez_metodos
select project_name, metodo, prob_vitoria from bsc.mcdm_robustez
where metodo <> 'CONSENSO (Borda)' order by metodo
```
```sql robustez_lider
select project_name, prob_vitoria, rank_p95 from bsc.mcdm_robustez
where metodo = 'CONSENSO (Borda)' order by prob_vitoria desc limit 1
```
```sql ajustes
select a.project_name, a.distribuicao, a.aic, a.ks_stat, a.ks_pvalue,
       c.media as custo_medio, c.maximo as custo_max, c.cvar_5 as custo_cvar
from bsc.mc_ajuste_distribuicao a
left join bsc.mc_estatisticas c
  on c.project_name = a.project_name and c.variavel = 'CUSTO_TOKENS'
where a.variavel = 'TOKENS' and a.escolhida = 1
order by a.project_name
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

![Mapa 5D do Portfólio de Projetos de IA](/5d_projetos.png?v=5)

### 🖱️ Mapa 5D Interativo — passe o mouse sobre cada esfera
> **X** = Tokens (escala) · **Y** = PEUC (%) · **tamanho** = PSR (0–5) · **cor** = ICCA (🟢 sustentável · 🟠 limítrofe · 🔴 prejuízo). Ao passar o mouse em cada **esfera glossy**, aparece **Nome do projeto, PSR, PEUC e Tokens**.

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
  <Column id=tirm title="TIRM" fmt=pct1/>
  <Column id=ill title="ILL (PI)" fmt=num2/>
  <Column id=vul title="VUL (R$)" fmt='$#,##0'/>
  <Column id=payback_simples title="PB simples" fmt=num2/>
  <Column id=payback_descontado title="PB descontado" fmt=num2/>
  <Column id=supera_selic title="TIR>SELIC?" fmt=boolean/>
  <Column id=supera_us title="TIR>EUA?" fmt=boolean/>
  <Column id=vpl_usd title="VPL US$" fmt='$#,##0'/>
  <Column id=payback_desc_usd title="PB desc. US$" fmt=num2/>
</DataTable>

> 🆕 **TIRM** (TIR Modificada) reinveste as entradas à taxa do projeto — mais realista que a TIR. **VUL** (Valor Uniforme Líquido) converte o VPL em série anual equivalente.

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

## 🎲 Simulação de Monte Carlo — risco do fluxo de caixa

> Cada fluxo de caixa periódico é tratado como **variável aleatória Triangular** (±30% em torno do valor base) e o
> portfólio é simulado com **10.000 iterações** por projeto (semente fixa ⇒ resultado reprodutível). Assim a escolha
> final deixa de olhar apenas o valor esperado e passa a **precificar o risco**.

<BigValue data={consenso_top} value=project_name title="Vencedor (consenso de 5 métodos)"/>
<BigValue data={mc_vpl} value=prob_menor_zero title="P(VPL<0) média do portfólio %" agg=mean fmt=num2/>
<BigValue data={mc_vpl} value=var_5 title="VaR 5% médio (R$)" agg=mean fmt='$#,##0'/>
<BigValue data={mc_vpl} value=iteracoes title="Iterações por projeto" agg=max fmt=num0/>

**Risco por projeto** — `VaR 5%` é o pior VPL plausível (percentil 5%); `CVaR 5%` é a média da cauda abaixo dele.
Prefira quem tem **VaR alto** e `P(VPL<0)` **baixa**: entrega retorno mesmo no cenário ruim.

<DataTable data={mc_vpl} rows=all rowShading=true>
  <Column id=project_name title="Projeto"/>
  <Column id=media title="VPL médio (R$)" fmt='$#,##0'/>
  <Column id=desvio_padrao title="Desvio-padrão" fmt='$#,##0'/>
  <Column id=minimo title="Mínimo" fmt='$#,##0'/>
  <Column id=maximo title="Máximo" fmt='$#,##0'/>
  <Column id=coef_variacao title="Coef. variação" fmt=num3/>
  <Column id=assimetria title="Assimetria" fmt=num3/>
  <Column id=curtose title="Curtose" fmt=num3/>
  <Column id=prob_menor_zero title="P(VPL<0) %" fmt=num2 contentType=colorscale/>
  <Column id=var_5 title="VaR 5% (R$)" fmt='$#,##0' contentType=colorscale/>
  <Column id=cvar_5 title="CVaR 5% (R$)" fmt='$#,##0'/>
</DataTable>

**Pior cenário plausível por projeto** (quanto mais alto o VaR 5%, mais resiliente o projeto)

<BarChart data={mc_vpl} x=project_name y=var_5 title="VaR 5% do VPL por projeto (percentil 5% de 10.000 simulações)" yAxisTitle="VaR 5% (R$)" sort=true>
  <ReferenceLine y=0 color=negative label="prejuízo"/>
</BarChart>

**Curvas de percentis do VPL** — a inclinação revela a dispersão: curva achatada = projeto previsível; curva íngreme = projeto volátil.

<LineChart data={mc_percentis_vpl} x=percentil y=valor series=project_name title="Distribuição acumulada do VPL simulado (percentis 5% a 95%)" yAxisTitle="VPL (R$)" xAxisTitle="Percentil (%)">
  <ReferenceLine y=0 color=negative label="break-even"/>
</LineChart>

## 🧮 Decisão Multicritério — DEMATEL · ELECTRE · PROMETHEE · MAUT · MCDA-C

> A arquitetura segue **John (2025)**, *"Integration of DEMATEL with Other MCDM Methods"*: o **DEMATEL** revela a
> estrutura causal entre os critérios e deriva os **pesos por influência**, que alimentam os quatro métodos de
> ranqueamento. Cada método é uma escola distinta — **sobreclassificação** (ELECTRE, PROMETHEE), **utilidade**
> (MAUT) e **construtivista** (MCDA-C) —, e o vencedor final sai do **consenso de Borda** entre os cinco.

**DEMATEL — quem é causa e quem é efeito.** Proeminência `R+C` = importância no sistema; Relação `R−C > 0` = **causa**
(alavanca: mexa aqui) e `R−C < 0` = **efeito** (termômetro: resultado do que se fez antes).

<DataTable data={dematel} rows=all rowShading=true>
  <Column id=rotulo title="Critério"/>
  <Column id=r title="R (influência exercida)" fmt=num3/>
  <Column id=c title="C (influência recebida)" fmt=num3/>
  <Column id=prominencia title="Proeminência (R+C)" fmt=num3 contentType=colorscale/>
  <Column id=relacao title="Relação (R−C)" fmt=num3 contentType=colorscale/>
  <Column id=papel title="Papel"/>
  <Column id=peso title="Peso derivado" fmt=pct2/>
</DataTable>

<BarChart data={dematel} x=rotulo y=relacao title="Diagrama causa–efeito do DEMATEL (R−C): acima de zero = causa" yAxisTitle="R − C" sort=false>
  <ReferenceLine y=0 color=info label="fronteira causa / efeito"/>
</BarChart>

**Ranking de cada método** — divergências entre métodos são informação, não ruído: elas mostram que o projeto é
sensível à escola de decisão adotada.

<BarChart data={mcdm_rank} x=project_name y=rank_ series=metodo type=grouped title="Posição de cada projeto por método MCDM (1º = melhor)" yAxisTitle="Posição" swapXY=true/>

**Consenso final (Borda)** — soma dos pontos de todos os métodos, cruzada com o risco do Monte Carlo.

<DataTable data={consenso} rows=all rowShading=true>
  <Column id=project_name title="Projeto"/>
  <Column id=rank_final title="Posição final" contentType=colorscale/>
  <Column id=borda title="Pontos de Borda" fmt=num0/>
  <Column id=rank_medio title="Posição média" fmt=num2/>
  <Column id=unanime title="Unânime?" fmt=boolean/>
  <Column id=prob_menor_zero title="P(VPL<0) %" fmt=num2/>
  <Column id=var_5 title="VaR 5% (R$)" fmt='$#,##0'/>
</DataTable>


## 🔎 Distribuições ajustadas aos tokens reais + 🎯 Robustez da decisão

> **Onde está o sinal.** O VPL é *linear* nos fluxos de caixa: simular só os fluxos devolve um tornado com os
> próprios fatores de desconto `1/(1+i)ᵗ` — informação nenhuma. O motor estocástico de verdade está **a montante**,
> no **consumo de tokens**, que tem cauda pesada. Por isso ajustamos 11 distribuições candidatas à série real de
> `logs_langfuse` (*ajuste de distribuições a dados*) e usamos a vencedora — a de **menor AIC** — como
> variável de entrada do Monte Carlo.

<DataTable data={ajustes} rows=all rowShading=true>
  <Column id=project_name title="Projeto"/>
  <Column id=distribuicao title="Distribuição ajustada"/>
  <Column id=aic title="AIC" fmt=num0/>
  <Column id=ks_stat title="KS D" fmt=num4/>
  <Column id=ks_pvalue title="KS p-valor" fmt=num4 contentType=colorscale/>
  <Column id=custo_medio title="Custo de tokens médio (R$)" fmt='$#,##0.00'/>
  <Column id=custo_max title="Pior caso (R$)" fmt='$#,##0.00'/>
  <Column id=custo_cvar title="CVaR 5% (R$)" fmt='$#,##0.00'/>
</DataTable>

> ⚠️ **p-valor abaixo de 0,05 = ajuste ruim.** O framework reporta em vez de esconder: naquele projeto a
> distribuição escolhida não descreve bem os dados — colete mais amostras ou trate a série como multimodal.

**Robustez do ranking (perturbação de Dirichlet).** Os pesos dos critérios são estimativas, não verdades. Perturbamos
os pesos do DEMATEL com `w' ~ Dir(κ·w)` — que preserva `E[w'] = w` — e **reranqueamos 2.000 vezes**. O veredito deixa
de ser *"X é o melhor"* e passa a ser **"X vence em P% dos universos de preferência plausíveis"**: um intervalo de
confiança sobre a **própria decisão**.

<BigValue data={robustez_lider} value=project_name title="Líder sob pesos perturbados"/>
<BigValue data={robustez_lider} value=prob_vitoria title="Vence em (% dos universos)" fmt=num1/>
<BigValue data={robustez_lider} value=rank_p95 title="Pior posição plausível do líder" fmt=num0/>

<DataTable data={robustez} rows=all rowShading=true>
  <Column id=project_name title="Projeto"/>
  <Column id=prob_vitoria title="Vence o consenso (%)" fmt=num1 contentType=colorscale/>
  <Column id=prob_top3 title="Top-3 (%)" fmt=num1/>
  <Column id=rank_medio title="Posição típica" fmt=num2/>
  <Column id=rank_p05 title="Melhor caso (p05)" fmt=num0/>
  <Column id=rank_p95 title="Pior caso (p95)" fmt=num0/>
</DataTable>

<BarChart data={robustez} x=project_name y=prob_vitoria title="Probabilidade de vencer o consenso sob pesos perturbados" yAxisTitle="% dos universos" sort=true/>

**Concordância entre escolas.** Se um método elege o líder em poucos universos, o consenso de Borda está *mascarando*
uma divergência de escola — e a decisão merece o olho do decisor, não só o número.

<BarChart data={robustez_metodos} x=project_name y=prob_vitoria series=metodo type=grouped title="Probabilidade de vitória por método (pesos perturbados)" yAxisTitle="% dos universos"/>

## 💳 Planos de Assinatura de IA — Custo Total com IOF
> Câmbio **R$ 5,40/US$** · **IOF 3,5%** sobre operação internacional (cartão). `Total = US$ × câmbio × (1 + IOF)`.
> Este é o custo real que alimenta a base de rateio (`assinaturas_infra`). Preços aproximados — verifique os sites oficiais.

<DataTable data={planos} rows=all rowShading=true>
  <Column id=provedor title="Provedor"/>
  <Column id=plano title="Plano"/>
  <Column id=usd_mes title="US$/mês" fmt=num0/>
  <Column id=r_base title="R$ base" fmt='$#,##0.00'/>
  <Column id=iof_reais title="IOF" fmt='$#,##0.00'/>
  <Column id=total_iof title="Total c/ IOF (R$)" fmt='$#,##0.00'/>
</DataTable>

<BarChart data={planos_pagos} x=plano y=total_iof title="Custo total mensal com IOF por plano (R$)" swapXY=true sort=true/>

<div style="display:flex;align-items:center;justify-content:center;gap:1rem;flex-wrap:wrap;margin:1.4rem 0 0.4rem;">
  <img src="/shark.svg" alt="tubarão investidor" width="120" height="82" style="flex:0 0 auto;"/>
  <h2 style="text-align:center;margin:0;font-weight:800;">🏆 AHP-TOPSIS 2N — Modelo Multi-Critério Decisório (MCDM)</h2>
  <img src="/gekko_photo.png" alt="Gordon Gekko fumando charuto (terno azul)" width="100" height="100" style="flex:0 0 auto;border-radius:50%;box-shadow:0 2px 8px rgba(0,0,0,.25);"/>
</div>

> **Escolha do MELHOR projeto** ponderando os indicadores como critérios. Pesos por **AHP**
> (VPL 37% · TIR 24% · ILL 14% · PSR 14% · IITA 5,6% · IDLS 5,6% — CR = 0,012, consistente).
> Ranking por **TOPSIS** em **duas normalizações** (vetorial/Euclidiana + min-max/linear); o
> **Ci final** é a média. Coluna **Robusto?** = as duas normalizações concordam na posição.

**🥇 Projeto vencedor (maior Ci final):**
<DataTable data={mcda_top}>
  <Column id=project_name title="🏆 Melhor Projeto"/>
  <Column id=ci_final title="Ci final" fmt=num4/>
</DataTable>

<BarChart data={mcda} x=project_name y=ci_final title="Ranking AHP-TOPSIS 2n (Ci final, 0–1)" swapXY=true sort=true labels=true/>

<DataTable data={mcda} rows=all rowShading=true>
  <Column id=rank_final title="#"/>
  <Column id=project_name title="Projeto"/>
  <Column id=ci_vector title="Ci vetorial" fmt=num4/>
  <Column id=ci_minmax title="Ci min-max" fmt=num4/>
  <Column id=ci_final title="Ci final" fmt=num4/>
  <Column id=concordante title="Robusto?" fmt=boolean/>
</DataTable>

> O vencedor tem **pitchdeck** gerado (ver pasta Projetos / `pitchdeck/`). Se as posições 6–7
> divergem entre normalizações, é onde o ranking é mais sensível — decida com cautela ali.

## 💰 Budget Global de Tokens — cada projeto é um CENTRO DE CUSTO

### 🧭 Leia isto antes de olhar qualquer número

**Existe UM único budget: o do plano que você assina.** Todo o resto **desce dele**.

Cada projeto do portfólio é um **centro de custo** — ele **não tem verba própria**. A verba dele é uma
**fatia do Budget Global**, e essa fatia é **recalculada automaticamente** toda vez que um projeto
entra ou sai do portfólio. **Nada é criado; tudo é repartido.**

```text
   ASSINATURA DO PLANO  (Claude Max · ChatGPT Pro · Google Ultra · assentos Team)
              │
              ▼
   💰 BUDGET GLOBAL/PRINCIPAL   ──────────  a quota mensal contratada. É FINITA.
              │
              ├── piso igualitário (50%)  ── o mínimo vital de cada centro de custo
              └── por VALOR entregue (50%) ── quem entrega mais, recebe mais
              │
              ▼
   🏷️ CENTRO DE CUSTO 1 … N   ──────────  a cota de CADA projeto
```

> ⚠️ **A consequência que ninguém enxerga.** Como o pool é **finito**, **um projeto que estoura a
> própria cota não “gasta mais” — ele TOMA a verba dos outros centros de custo.** É a tragédia dos
> comuns aplicada ao orçamento de IA. Langfuse, CloudZero e afins mostram **custo por projeto**, como
> se cada um tivesse a sua própria torneira. **Não tem. A torneira é uma só.**

### 🏷️ Tabela prévia — os centros de custo e a origem da verba

<DataTable data={orc_cota} rows=all>
  <Column id=project_name title="🏷️ Centro de custo"/>
  <Column id=cota_tokens title="Verba recebida do Budget Global (tokens/mês)" fmt=num0/>
  <Column id=cota_brl title="Verba (R$/mês)" fmt='$#,##0'/>
  <Column id=consumo_tokens title="Consumo real (tokens/mês)" fmt=num0/>
  <Column id=pct_uso title="Uso da verba" fmt=pct0 contentType=colorscale/>
  <Column id=estourou title="Estourou?" contentType=colorscale/>
</DataTable>

_Note que a soma das verbas **é** o Budget Global — não sobra nem falta. **Quem estoura, tira de quem
não estourou.**_

---

### 📊 O Budget Global, em números

<BigValue data={orc_global} value=tokens_contratados title="Contratado (tokens/mês)" fmt=num0/>
<BigValue data={orc_global} value=consumo_run_rate title="Consumo (run-rate/mês)" fmt=num0/>
<BigValue data={orc_global} value=pct_utilizacao title="Utilização da quota" fmt=pct1/>
<BigValue data={orc_global} value=tco_brl title="TCO mensal de IA (R$)" fmt='$#,##0'/>

<BigValue data={orc_global} value=folga_tokens title="Folga contratual (tokens/mês)" fmt=num0/>
<BigValue data={orc_global} value=desperdicio_rr title="🔥 Desperdício (tokens/mês)" fmt=num0/>
<BigValue data={orc_global} value=desperdicio_brl title="🔥 Desperdício (R$/mês)" fmt='$#,##0'/>
<BigValue data={orc_global} value=desperdicio_vs_folga title="Desperdício ÷ Folga" fmt=num1/>

### 🔥 O número que dói

O **desperdício** — tokens queimados em chamadas que **falharam e não devolveram nada**
(alucinação, rate-limit) — é **{orc_global[0].desperdicio_vs_folga.toFixed(1)}× maior que toda a sua folga contratual**.

**Traduzindo:** você vai ser empurrado a **contratar um plano maior por causa de chamadas que não
entregaram resposta**. Cortar metade do desperdício libera mais capacidade do que a folga inteira do
contrato — **sem gastar um centavo a mais**.

### 🍩 Budget Global utilizado por Projeto (ótica do Burn Token Rate)

<ECharts config={{
    tooltip: { trigger: 'item', formatter: '{b}<br/>{c} tokens/mês ({d}%)' },
    legend: { bottom: 0, type: 'scroll' },
    series: [{
      name: 'Burn de tokens',
      type: 'pie',
      radius: ['42%', '70%'],
      avoidLabelOverlap: true,
      itemStyle: { borderRadius: 6, borderColor: '#fff', borderWidth: 2 },
      label: { show: true, formatter: '{b}\n{d}%' },
      data: orc_rateio.map(r => ({ name: r.project_name, value: r.tokens_mes }))
    }]
}}/>

_Cada fatia é a parcela do **pool global** que o projeto queima por mês. Não é "o custo dele" — é **a
capacidade que ele retira dos outros**._

### ⚖️ Quem consome, quem entrega — e quem banca quem

O rateio **por consumo** é o padrão do mercado, e é **auto-justificante**: quem mais queima recebe a
maior cota, o que **legitima o desperdício**. O rateio honesto é por **valor entregue (EV)**. A
diferença entre os dois é o **subsídio cruzado** — a resposta, em R$/mês, para a pergunta que nenhuma
ferramenta faz: **quem está bancando quem.**

<DataTable data={orc_rateio} rows=all>
  <Column id=project_name title="Projeto"/>
  <Column id=tokens_mes title="Tokens/mês" fmt=num0/>
  <Column id=pct_pool title="% do pool" fmt=pct1 contentType=colorscale/>
  <Column id=pct_valor title="% do valor" fmt=pct1 contentType=colorscale/>
  <Column id=eficiencia title="EV por milhão de tokens" fmt=num0 contentType=colorscale/>
  <Column id=cota_consumo title="Cota por CONSUMO (R$)" fmt='$#,##0'/>
  <Column id=cota_valor title="Cota por VALOR (R$)" fmt='$#,##0'/>
  <Column id=subsidio_brl title="Subsídio cruzado (R$/mês)" fmt='$#,##0' contentType=colorscale/>
  <Column id=papel title="Papel"/>
</DataTable>

<BarChart data={orc_rateio} x=project_name y=subsidio_brl title="Subsídio cruzado (R$/mês) — positivo = É subsidiado · negativo = PAGA a conta dos outros" yAxisTitle="R$/mês" swapXY=true/>

### 🔄 Cota adaptativa — o budget é redimensionado a cada projeto cadastrado

A cota de cada projeto é **fatiada do pool global** e **recalculada sempre que N muda**: cadastrou um
projeto novo, **todos encolhem**. A regra é declarada — **piso igualitário de 50%** (um projeto novo
tem EV = 0; sem piso ele receberia zero tokens e jamais poderia produzir valor) **+ 50% por valor
entregue**.

<DataTable data={orc_cota} rows=all>
  <Column id=project_name title="Projeto"/>
  <Column id=n_portfolio title="N do portfólio"/>
  <Column id=cota_tokens title="Cota (tokens/mês)" fmt=num0/>
  <Column id=consumo_tokens title="Consumo (tokens/mês)" fmt=num0/>
  <Column id=pct_uso title="Uso da cota" fmt=pct0 contentType=colorscale/>
  <Column id=excedente title="Excedente (tomado dos outros)" fmt=num0 contentType=colorscale/>
  <Column id=excedente_brl title="Excedente (R$/mês)" fmt='$#,##0'/>
</DataTable>

### 💥 O que custa dizer "SIM" a mais um projeto

Esta é a pergunta que o comitê de portfólio **nunca consegue responder**. Num pool **finito**, admitir
o projeto N+1 **tira tokens de todos os N que já estavam lá**. A diluição não é abstrata: ela vira
menos capacidade, menos entrega e — pela cadeia causal — **atraso em R$**.

<DataTable data={orc_admissao} rows=all>
  <Column id=cenario title="Cenário"/>
  <Column id=n_atual title="N atual"/>
  <Column id=n_novo title="N novo"/>
  <Column id=cota_media_antes title="Cota média ANTES" fmt=num0/>
  <Column id=cota_media_depois title="Cota média DEPOIS" fmt=num0/>
  <Column id=diluicao_pct title="Diluição de CADA projeto" fmt=pct1 contentType=colorscale/>
  <Column id=custo_diluicao title="Capacidade diluída (R$/mês)" fmt='$#,##0'/>
</DataTable>

> **Ou o plano cresce, ou alguém entrega menos.** Não existe terceira via num pool finito — e agora
> isso está na mesa do board **com número**, não com opinião.

## 🔒 Contenção de recurso PRECIFICADA — a cadeia causal aplicada ao PORTFÓLIO

A cadeia causal, **dentro** de um projeto, liga: `token que derivou → risco → prazo (P80) → R$`.
Isto liga **ENTRE** projetos:

```text
   excedente de um  →  exaustão do pool  →  estrangulamento dos OUTROS
                    →  o P80 DELES escorrega  →  o Cost of Delay DELES cobra a conta
```

Exige, **ao mesmo tempo**, FinOps (a quota), EVM (o valor entregue), risco (a exposição) e cronograma
simulado (o P80). É por isso que **nenhuma ferramenta do mercado faz** — nenhuma tem os quatro motores
juntos. O Langfuse vê o token. O Jira vê a tarefa. O CloudZero vê a fatura. **Nenhum deles consegue
dizer que o projeto J está custando R$ X de atraso ao projeto F.**

> ⚠️ **A honestidade que sustenta o número.** Enquanto o consumo **couber na quota**, **não há
> estrangulamento físico** — ninguém para, ninguém atrasa. O dano é **alocativo** (subsídio cruzado),
> não **operacional**. Dizer "o J está atrasando o C" com folga no pool seria **mentira com cara de
> rigor**. Por isso isto é **cenarizado**: mostra *a partir de que ponto* o pool vira, e *quanto custa
> quando virar*. **É previsão, e está rotulada como previsão.**

### 📉 Os cenários — a que ponto o pool vira

<DataTable data={cont_cenario} rows=all>
  <Column id=cenario title="Cenário"/>
  <Column id=consumo_mes title="Consumo (tokens/mês)" fmt=num0/>
  <Column id=pct_quota title="% da quota" fmt=pct0 contentType=colorscale/>
  <Column id=dia_exaustao title="Pool seca no dia" fmt=num1/>
  <Column id=dias_parados title="Dias de portfólio PARADO" fmt=num1 contentType=colorscale/>
  <Column id=custo_cod_total title="Custo (Cost of Delay somado)" fmt='$#,##0' contentType=colorscale/>
  <Column id=veredito title="Veredito" wrap=true/>
</DataTable>

**O cenário mais importante não é o pessimista — é o `sem desperdício`.** Ele mostra quanta capacidade
está escondida em **chamadas que falharam**: a alavanca mais barata do portfólio, porque **não custa um
centavo a mais**.

### ⚔️ Algozes e vítimas — quem causa o dano, e quem paga por ele

Quando o pool seca, **todos param** — inclusive (e sobretudo) os **eficientes, que não causaram o
problema**. A culpa é rateada pelo **excedente** de cada um; o sofrimento, pelo **Cost of Delay** de
cada um.

<DataTable data={cont_projeto} rows=all>
  <Column id=project_name title="Projeto"/>
  <Column id=eficiencia title="EV por milhão de tokens" fmt=num0 contentType=colorscale/>
  <Column id=excedente title="Excedente (toma do pool)" fmt=num0 contentType=colorscale/>
  <Column id=cod_dia title="Cost of Delay (R$/dia)" fmt='$#,##0'/>
  <Column id=custo_sofrido title="R$ que ELE perde" fmt='$#,##0'/>
  <Column id=culpa_rs title="R$ de dano que ELE causa aos outros" fmt='$#,##0' contentType=colorscale/>
  <Column id=saldo title="Saldo (causa − sofre)" fmt='$#,##0' contentType=colorscale/>
  <Column id=papel title="Papel"/>
</DataTable>

<BarChart data={cont_projeto} x=project_name y=saldo title="Saldo de contenção (R$) — positivo = ALGOZ (causa mais dano do que sofre) · negativo = VÍTIMA" yAxisTitle="R$" swapXY=true/>

### 🪓 Política de corte — se o portfólio precisa de espaço, QUEM sai?

A resposta honesta **não é "o que gasta mais"** — cortar por consumo bruto puniria um projeto **grande
e produtivo**. A resposta é **"o que entrega menos POR TOKEN"**: cortar por **eficiência** libera o
máximo de pool ao **mínimo custo de valor**.

<DataTable data={admissao} rows=all>
  <Column id=ordem_corte title="Ordem de corte"/>
  <Column id=project_name title="Projeto"/>
  <Column id=eficiencia title="EV por milhão de tokens" fmt=num0 contentType=colorscale/>
  <Column id=pct_pool_liberado title="% do pool que LIBERA" fmt=pct1 contentType=colorscale/>
  <Column id=pct_valor_perdido title="% do valor que SACRIFICA" fmt=pct1 contentType=colorscale/>
  <Column id=projetos_novos title="Vagas que abre" fmt=num1/>
  <Column id=troca title="O trade-off" wrap=true/>
</DataTable>

> **Este é o quadro que o comitê de portfólio nunca teve.** Não é "cortem custos" — é: *este projeto
> libera 20,5% do pool sacrificando 1,9% do valor; aquele libera 6,9% mas sacrifica 20,1% — **cortar o
> segundo destrói mais valor do que libera capacidade**.*

## 🔁 Loop de reaprendizagem sobre o orçamento — o agente cobra a si mesmo

O PM Agent não só recomenda cortar desperdício — ele **guarda o número** e, na weekly seguinte, **cobra
a si mesmo** se o corte de fato liberou pool. É a **mesma mecânica do motor de reaprendizagem** (bandit
contextual), aplicada à dimensão de **tokens**: só a ação que **ele recomendou** é avaliada, ele
**não leva crédito pelo que o acaso liberou**, e variação abaixo de 2% é ruído — **não se aprende com
ruído**.

<DataTable data={orc_loop} rows=all>
  <Column id=project_name title="Projeto"/>
  <Column id=acao title="Ação recomendada" wrap=true/>
  <Column id=veredito title="Veredito do último corte"/>
  <Column id=liberou_brl title="Pool liberado (R$/mês)" fmt='$#,##0' contentType=colorscale/>
  <Column id=whatif_brl title="What-if do corte pendente (R$/mês)" fmt='$#,##0'/>
  <Column id=acertos title="Cortes ✓" fmt=num0/>
  <Column id=erros title="Cortes ✗" fmt=num0/>
  <Column id=confianca title="Confiança"/>
</DataTable>

> **O que fecha o loop:** hoje, com dados DEMO estáticos, o veredito é `baseline` — o agente registrou o
> desperdício e **cobra a si mesmo na próxima weekly**. Quando o dado real fluir e o corte de fato
> reduzir o desperdício, o veredito vira `funcionou` e a **confiança do agente naquela recomendação
> sobe**. Se o desperdício não ceder, vira `não funcionou` e a **confiança cai**. O agente aprende, por
> projeto, **quais cortes de fato liberam pool aqui**.

---

### 📌 Bottom-Line — Sumário Executivo & Insights C-Level

**Veredito.** O modelo **AHP-TOPSIS 2n** elege **{mcda_top[0].project_name}** como o melhor projeto do portfólio
(**Ci = 0,96** de 1,00), com **robustez confirmada**: as duas normalizações (vetorial e min-max)
concordam na **1ª posição** e em 8/10 do ranking — o topo é estável, não é artefato de método.

**Por que {mcda_top[0].project_name} venceu.** Os critérios **financeiros** (VPL R$ 5.973 · TIR 32,9% · ILL 1,75)
estão **empatados** entre os projetos (fluxo de caixa ainda em *placeholder* uniforme). Com o
financeiro neutralizado, a decisão migra para a **eficiência operacional**, e aí {mcda_top[0].project_name} domina:
tem a **menor taxa de alucinação (IITA 9,1%)** e o **menor desperdício Lean (IDLS 15,0%)** de
todo o portfólio — praticamente **metade** do desperdício do 2º colocado. Em outras palavras:
**mesmo retorno projetado, executando com muito menos desperdício de tokens/caixa.**

**Insights C-Level.**
- 🥇 **Eficiência é o desempate:** quando o retorno é parecido, quem **queima menos** (menor IITA/IDLS)
  entrega o mesmo valor com maior margem — é o ativo mais escalável.
- 🛡️ **Robustez decisória:** a concordância entre as duas normalizações (8/10) dá **segurança** ao board
  para agir no topo do ranking; a zona sensível (posições 6–7) exige análise qualitativa antes de cortar.
- 📉 **Cauda de risco:** o último colocado (Ci 0,01) reúne o pior desempenho combinado — candidato a
  **refatoração ou descontinuação** (cruzar com a Matriz BCG).

**⚠️ Ressalva de honestidade decisória.** Os critérios financeiros carregam **75% do peso AHP**
(VPL 37% + TIR 24% + ILL 14%), mas hoje **não diferenciam** porque o fluxo de caixa é placeholder.
**O veredito só é definitivo com os fluxos de caixa REAIS por projeto** — ao inseri-los, o ranking
pode mudar substancialmente (o financeiro voltará a dominar).

**Recomendação.** (1) Aprovar {mcda_top[0].project_name} como **piloto de escala** pela eficiência comprovada; (2) inserir
os **fluxos de caixa reais** e re-rodar o `ahp_topsis.py` para o veredito financeiro definitivo;
(3) acionar plano de melhoria na cauda (o último colocado).

---
## 👑 Dossiê Administrativo da **Jóia da Coroa** — {mcda_top[0].project_name}

> Ferramentas administrativas clássicas aplicadas **exclusivamente ao projeto eleito** para
> enriquecê-lo, enaltecê-lo e evidenciar seu **diferencial competitivo**. Todas são geradas
> por **pipeline Python concorrente** (`gerar_admtools.py`) — não dependem de nenhum template
> externo. Detalhamento e justificativa em `foundations/admtools/ferramentas_administrativas.md`.

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:1.2rem;margin:1rem 0;">

<div>

**🎯 SWOT — posição estratégica**
Forças/fraquezas/oportunidades/ameaças derivadas dos KPIs reais (menor IITA e IDLS = força dominante).
<img src="/admtools/pt/swot.png" alt="SWOT do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🌐 PESTELC — macroambiente**
Sete fatores externos (Político, Econômico, Social, Tecnológico, Ecológico, Legal, Cultural).
<img src="/admtools/pt/pestel.png" alt="PESTELC do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🗺️ 5W4H — plano de ação (5W + 4H)**
What/Why/Where/When/Who + How/How much/How many/How long — roteiro de escala do eleito.
<img src="/admtools/pt/5w4h.png" alt="5W4H do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**📊 Pareto de falhas (80/20)**
Categorias de prompt que concentram 80% das falhas — onde atacar primeiro (dados reais do Langfuse).
<img src="/admtools/pt/pareto.png" alt="Pareto de falhas do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🔥 Matriz GUT — priorização (heatmap)**
Gravidade × Urgência × Tendência das ações; maior GUT = agir primeiro.
<img src="/admtools/pt/gut.png" alt="Matriz GUT do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🕸️ Radar competitivo — diferencial**
Impressão digital do eleito **vs média do portfólio** (a área azul domina a cinza em quase todo eixo).
<img src="/admtools/pt/radar.png" alt="Radar competitivo do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>

</div>

> **📌 Leitura executiva.** O **radar** é o retrato do diferencial competitivo: a Jóia da Coroa
> supera a média em anti-alucinação, Lean e entrega útil. **SWOT/PESTEL/5W4H** transformam esse
> diagnóstico em **estratégia e plano de ação**; **Pareto + GUT** dizem **exatamente onde** agir
> primeiro para converter a liderança operacional em retorno financeiro definitivo.

---
## 🔗 Painéis Individuais por Projeto

{#each kpis as p}
<a href="/projetos/{p.project_name}">▶️ {p.project_name} — PSR {p.kpi_psr}</a>
{/each}
