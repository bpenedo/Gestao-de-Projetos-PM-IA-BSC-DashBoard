---
title: Painel BSC — Gestão de Projetos (PM) IA
---

_Framework "Gestão de Projetos (PM) IA com Painel BSC e DashBoard" · ©️ Bruno Teixeira Penedo — 2026. Todos os direitos reservados. E-mail: bpenedo@gmail.com_
**Weekly Checkpoint — toda sexta-feira às 09:00.**

> ⚠️ **Dados DEMO** dos 10 projetos reais de `~/devparetoprojects/*`. Tornam-se reais quando o Langfuse sincronizar.

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
  <Column id=ill title="ILL (PI)" fmt=num2/>
  <Column id=payback_simples title="PB simples" fmt=num2/>
  <Column id=payback_descontado title="PB descontado" fmt=num2/>
  <Column id=supera_selic title="TIR>SELIC?" fmt=boolean/>
  <Column id=supera_us title="TIR>EUA?" fmt=boolean/>
  <Column id=vpl_usd title="VPL US$" fmt='$#,##0'/>
  <Column id=payback_desc_usd title="PB desc. US$" fmt=num2/>
</DataTable>

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

### 📌 Bottom-Line — Sumário Executivo & Insights C-Level

**Veredito.** O modelo **AHP-TOPSIS 2n** elege **`Project F`** como o melhor projeto do portfólio
(**Ci = 0,96** de 1,00), com **robustez confirmada**: as duas normalizações (vetorial e min-max)
concordam na **1ª posição** e em 8/10 do ranking — o topo é estável, não é artefato de método.

**Por que `Project F` venceu.** Os critérios **financeiros** (VPL R$ 5.973 · TIR 32,9% · ILL 1,75)
estão **empatados** entre os projetos (fluxo de caixa ainda em *placeholder* uniforme). Com o
financeiro neutralizado, a decisão migra para a **eficiência operacional**, e aí `Project F` domina:
tem a **menor taxa de alucinação (IITA 9,1%)** e o **menor desperdício Lean (IDLS 15,0%)** de
todo o portfólio — praticamente **metade** do desperdício do 2º colocado. Em outras palavras:
**mesmo retorno projetado, executando com muito menos desperdício de tokens/caixa.**

**Insights C-Level.**
- 🥇 **Eficiência é o desempate:** quando o retorno é parecido, quem **queima menos** (menor IITA/IDLS)
  entrega o mesmo valor com maior margem — é o ativo mais escalável.
- 🛡️ **Robustez decisória:** a concordância entre as duas normalizações (8/10) dá **segurança** ao board
  para agir no topo do ranking; a zona sensível (posições 6–7) exige análise qualitativa antes de cortar.
- 📉 **Cauda de risco:** `Project C` (Ci 0,01) reúne o pior desempenho combinado — candidato a
  **refatoração ou descontinuação** (cruzar com a Matriz BCG).

**⚠️ Ressalva de honestidade decisória.** Os critérios financeiros carregam **75% do peso AHP**
(VPL 37% + TIR 24% + ILL 14%), mas hoje **não diferenciam** porque o fluxo de caixa é placeholder.
**O veredito só é definitivo com os fluxos de caixa REAIS por projeto** — ao inseri-los, o ranking
pode mudar substancialmente (o financeiro voltará a dominar).

**Recomendação.** (1) Aprovar `Project F` como **piloto de escala** pela eficiência comprovada; (2) inserir
os **fluxos de caixa reais** e re-rodar o `ahp_topsis.py` para o veredito financeiro definitivo;
(3) acionar plano de melhoria na cauda (`Project C`).

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
<img src="/admtools/swot.png" alt="SWOT do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🌐 PESTELC — macroambiente**
Sete fatores externos (Político, Econômico, Social, Tecnológico, Ecológico, Legal, Cultural).
<img src="/admtools/pestel.png" alt="PESTELC do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🗺️ 5W4H — plano de ação (5W + 4H)**
What/Why/Where/When/Who + How/How much/How many/How long — roteiro de escala do eleito.
<img src="/admtools/5w4h.png" alt="5W4H do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**📊 Pareto de falhas (80/20)**
Categorias de prompt que concentram 80% das falhas — onde atacar primeiro (dados reais do Langfuse).
<img src="/admtools/pareto.png" alt="Pareto de falhas do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🔥 Matriz GUT — priorização (heatmap)**
Gravidade × Urgência × Tendência das ações; maior GUT = agir primeiro.
<img src="/admtools/gut.png" alt="Matriz GUT do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🕸️ Radar competitivo — diferencial**
Impressão digital do eleito **vs média do portfólio** (a área azul domina a cinza em quase todo eixo).
<img src="/admtools/radar.png" alt="Radar competitivo do projeto eleito" style="width:100%;border-radius:8px;"/>

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
