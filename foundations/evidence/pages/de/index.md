---
title: BSC-Panel — KI-Projektmanagement (PM)
---

🌐 [Português](/) · [English](/en) · [Español](/es) · [Français](/fr) · **Deutsch** · [中文](/zh) · [한국어](/ko) · [हिन्दी](/hi) · [עברית](/he) · [Svenska](/sv) · [Русский](/ru) · [Suomi](/fi)


🌐 **Português** · [English](/en) · [Español](/es) · [Français](/fr) · [Deutsch](/de) · [中文](/zh) · [한국어](/ko) · [हिन्दी](/hi)


_Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com_
**Wöchentlicher Checkpoint — jeden Freitag um 09:00 Uhr.**

> ⚠️ **DEMO-Daten** (anonymisiertes Portfolio). Werden real, sobald Langfuse synchronisiert.

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
select * exclude (prompt_categoria), CASE prompt_categoria WHEN 'Conversa/Aberto' THEN 'Chat/Offen' WHEN 'RAG/Busca' THEN 'RAG/Suche' WHEN 'Transformacao/Formato' THEN 'Transformation/Format' WHEN 'Raciocinio/Analise' THEN 'Schlussfolgern/Analyse' WHEN 'Sumarizacao' THEN 'Zusammenfassung' WHEN 'Geracao de Codigo' THEN 'Codegenerierung' WHEN 'Extracao de Dados' THEN 'Datenextraktion' ELSE prompt_categoria END as prompt_categoria from bsc.alucinacao_categoria
```
```sql rca_proj
select * exclude (prompt_gargalo), CASE prompt_gargalo WHEN 'Conversa/Aberto' THEN 'Chat/Offen' WHEN 'RAG/Busca' THEN 'RAG/Suche' WHEN 'Transformacao/Formato' THEN 'Transformation/Format' WHEN 'Raciocinio/Analise' THEN 'Schlussfolgern/Analyse' WHEN 'Sumarizacao' THEN 'Zusammenfassung' WHEN 'Geracao de Codigo' THEN 'Codegenerierung' WHEN 'Extracao de Dados' THEN 'Datenextraktion' ELSE prompt_gargalo END as prompt_gargalo from bsc.rca_projeto
```
```sql rca_inter
select * exclude (prompt_categoria), CASE prompt_categoria WHEN 'Conversa/Aberto' THEN 'Chat/Offen' WHEN 'RAG/Busca' THEN 'RAG/Suche' WHEN 'Transformacao/Formato' THEN 'Transformation/Format' WHEN 'Raciocinio/Analise' THEN 'Schlussfolgern/Analyse' WHEN 'Sumarizacao' THEN 'Zusammenfassung' WHEN 'Geracao de Codigo' THEN 'Codegenerierung' WHEN 'Extracao de Dados' THEN 'Datenextraktion' ELSE prompt_categoria END as prompt_categoria from bsc.rca_intersecao
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

## 📈 Portfolio-Zusammenfassung

<BigValue data={kpis} value=total_tokens title="Tokens gesamt" agg=sum fmt=num0/>
<BigValue data={kpis} value=kpi_psr title="Ø PSR (0-5)" agg=mean fmt=num1/>
<BigValue data={kpis} value=kpi_idls_lean title="Ø Lean-Verschwendung %" agg=mean fmt=num1/>
<BigValue data={kpis} value=burn_rate_ia title="Burn Rate gesamt" agg=sum fmt='$#,##0.00'/>

## 🌐 5D-Portfoliokarte (C-Level-Sicht)
> 3D-Kugeln (5dchart-Stil) — **5 Dimensionen je Projekt**: **X**=Volumen/Skala (Tokens) · **Y**=PEUC/Qualität (%) · **Z**=PSR/Gesundheit (0–5) · **Größe**=Burn Rate (R$) · **Farbe**=ICCA/Nachhaltigkeit (🟢 über 3x deckt Kosten · 🔴 unter 1x = Verlust).
>
> **Vorstands-Lesart:** das ideale Projekt liegt **rechts/hinten** (Skala+Qualität), **hoch** (PSR) und **grün** (nachhaltig). Große **rote** Kugel = viel Cash verbrannt ohne Deckung → vor dem Skalieren korrigieren.

![Mapa 5D do Portfólio de Projetos de IA](/5d_de.png?v=5)

### 🖱️ Interaktive 5D-Karte — mit der Maus über jede Kugel fahren
> **X** = Tokens (Skala) · **Y** = PEUC (%) · **Größe** = PSR (0–5) · **Farbe** = ICCA (🟢 nachhaltig · 🟠 grenzwertig · 🔴 Verlust). Mit der Maus über jede **glänzende Kugel** fahren, um **Projektname, PSR, PEUC und Tokens** zu sehen.

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

## 📉 Trend des Leitindikators (CPP) und Scores (PSR)
> Was für das C-Level am wichtigsten ist: **die Richtung**. Sinkender CPP = effizienteres Portfolio.

<LineChart data={tendencia} x=data_snapshot y=cpp_medio yAxisTitle="CPP médio (R$/%)" title="Kosten je Fortschrittspunkt — Portfolio-Trend" markers=true/>

<LineChart data={tendencia} x=data_snapshot y=psr_medio yAxisTitle="PSR médio" yMin=0 yMax=5 title="Ø Portfolio-Score (PSR 0-5)" markers=true/>

## ⭐ Score (PSR) je Projekt

<BarChart data={kpis} x=project_name y=kpi_psr swapXY=true title="PSR (0-5) je Projekt — sortiert" sort=true labels=true/>

## 🍩 Zusammensetzung & Mix (Donut mit Tiefe)

<Grid cols=2>
<Group>

**Wo das KI-Cash verbrannt wird** (Burn Rate je Projekt)

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

**Globaler Fehlermix** (Pareto-Donut)

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

## 🧭 Nachhaltigkeitsquadrant (skalieren oder korrigieren?)
> X-Achse = **ICCA** (Deckung: über 3x = gesund) · Y-Achse = **IBMT** (marginaler Burn: unter 0,33 = gut) · Größe = Burn Rate.
> Unten rechts = **profitabel skalieren**; oben links = **vor dem Wachstum korrigieren**.

<ScatterPlot data={kpis} x=kpi_icca y=kpi_ibmt series=project_name size=burn_rate_ia xAxisTitle="ICCA — cobertura de custo (x)" yAxisTitle="IBMT — burn marginal (x)" title="Finanzielle Nachhaltigkeit je Projekt"/>

## 📊 Fehler-Pareto je Projekt

<BarChart data={falhas} x=project_name y=percentual_dominancia series=categoria_falha type=stacked100 swapXY=true title="Fehlerdominanz (%) je Projekt"/>

## 🗂️ Score & finanzielle Gesundheit (Tabelle)

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

## 🚨 Kritische Warnungen

<DataTable data={alertas} rows=8>
  <Column id=project_name title="Projekt"/>
  <Column id=tipo_erro title="Fehler"/>
  <Column id=tokens_desperdicados title="Tokens" fmt=num0/>
  <Column id=data_evento title="Wann"/>
</DataTable>

## 📅 Agenda des wöchentlichen Meetings

<DataTable data={reuniao} rows=all>
  <Column id=project_name title="Projekt"/>
  <Column id=sumario_executivo title="Zusammenf."/>
  <Column id=acoes_corretivas_lean title="Lean-Maßnahmen (PDCA)"/>
</DataTable>

## 🪙 Kostendeckung (VRT) — 5 Blöcke + Mittelwert (2. Sicht)
> Gleiche Umlagebasis in **5 Granularitäten** (R$ pro 50/100/250/500/1.000 Tokens) + der **Blockdurchschnitt** — eine zweite Sicht auf den Verbrauch je Projekt.

<DataTable data={kpis} rows=all rowShading=true>
  <Column id=project_name title="Projekt"/>
  <Column id=vrt_50t title="50 tok" fmt='#,##0.00000'/>
  <Column id=vrt_100t title="100 tok" fmt='#,##0.00000'/>
  <Column id=vrt_250t title="250 tok" fmt='#,##0.00000'/>
  <Column id=vrt_500t title="500 tok" fmt='#,##0.00000'/>
  <Column id=vrt_por_ktoken title="1.000 tok" fmt='#,##0.00000'/>
  <Column id=vrt_media_blocos title="Ø Blöcke" fmt='#,##0.00000' contentType=colorscale/>
</DataTable>

## ⏰ Kritische Unterbrechungs-/Auswirkungsstunde (HCI)
> Zu welcher **Tagesstunde (BRT)** jedes Projekt am stärksten betroffen ist — um im richtigen Fenster zu handeln (Tier-Upgrade, Backoff, Planung).

<BarChart data={hora_total} x=hora_brt y=interrupcoes title="Unterbrechungen nach Tagesstunde (BRT) — Portfolio" xAxisTitle="Hora (0-23, BRT)"/>

<DataTable data={horario_critico} rows=all rowShading=true>
  <Column id=project_name title="Projekt"/>
  <Column id=hora_pico title="Spitzenstunde (BRT)" fmt='0"h"'/>
  <Column id=interrupcoes_pico title="Unterbrechungen im Peak" fmt=num0/>
</DataTable>

## ♻️ Verschwendungs-Taxonomie (Lean Six Sigma) — wo am meisten verschwendet wird
> Verschwendung nach **gewichteten Tokens** (Defekt 2,0× · Quote 1,5× · Überverarbeitung 1,0× · Latenz 0,5×), nicht nur nach Anzahl.

<Grid cols=2>
<Group>

**Portfolio-Verschwendungsmix**
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

**Dominante Verschwendung je Projekt**
<DataTable data={waste_dom} rows=all>
  <Column id=project_name title="Projekt"/>
  <Column id=waste_dominante title="Dominante Verschwendung"/>
  <Column id=waste_tokens title="Verschw. Tokens" fmt=num0/>
</DataTable>

</Group>
</Grid>

<BarChart data={wastes} x=project_name y=waste_tokens series=categoria_waste type=stacked swapXY=true title="Verschwendungszusammensetzung (gewichtete Tokens) je Projekt"/>

## 🔬 RCA — Halluzination nach Prompt-Typ (was jedes Projekt VERZÖGERT)
> Root Cause Analysis: Wir klassifizieren Prompts in **Kategorien** und messen die Halluzination jeder.
> Objektive Diagnose, **was jedes Projekt verzögert** und **was ALLE gemeinsam verzögert (Schnittmenge)**.

### 🎯 Schnittmenge — der portfolioweite Engpass
> Der Prompt-Typ, der in den meisten Projekten der **Halluzinations-Engpass Nr. 1** ist. Ihn zuerst anzugehen hat den größten systemischen Effekt.

<BarChart data={rca_inter} x=prompt_categoria y=projetos_onde_e_top1 title="Prompt-Typ mit größter Verzögerung (Engpass #1 in N Projekten)" yAxisTitle="Nº de projetos onde é o gargalo #1" labels=true sort=true/>

### 🧭 Halluzinations-Engpass je Projekt (individuelle RCA)

<DataTable data={rca_proj} rows=all rowShading=true>
  <Column id=project_name title="Projekt"/>
  <Column id=prompt_gargalo title="Am stärksten halluzinierender Prompt (Engpass)"/>
  <Column id=alucinacoes title="Halluzinationen" fmt=num0/>
</DataTable>

### 📊 Halluzinations-Taxonomie nach Kategorie × Projekt

<BarChart data={aluc_cat} x=project_name y=alucinacoes series=prompt_categoria type=stacked swapXY=true title="Halluzinationen nach Prompt-Typ je Projekt"/>

## 💰 Kapitalwert, Amortisation & Portfolio-Cashflow
> Berechnet aus **Ihrem Cashflow** (CSV/Tabelle — siehe `pipeline/fluxo_caixa_template.csv` und `python3 carregar_fluxo.py IHRE.csv`). Kapitalwert = Σ Fluss ÷ (1+i)ᵗ · Amortisation **einfach** (zeitliche Variation) und **diskontiert**, beide interpoliert. _Demodaten, bis Sie Ihre CSV bereitstellen._

<DataTable data={vpl} rows=all rowShading=true>
  <Column id=project_name title="Projekt"/>
  <Column id=vpl title="VPL (R$)" fmt='$#,##0' contentType=colorscale/>
  <Column id=tir title="TIR" fmt=pct1/>
  <Column id=tirm title="TIRM" fmt=pct1/>
  <Column id=ill title="ILL (PI)" fmt=num2/>
  <Column id=vul title="VUL (R$)" fmt='$#,##0'/>
  <Column id=payback_simples title="PB einfach" fmt=num2/>
  <Column id=payback_descontado title="PB diskontiert" fmt=num2/>
  <Column id=supera_selic title="TIR>SELIC?" fmt=boolean/>
  <Column id=supera_us title="TIR>EUA?" fmt=boolean/>
  <Column id=vpl_usd title="VPL US$" fmt='$#,##0'/>
  <Column id=payback_desc_usd title="PB desc. US$" fmt=num2/>
</DataTable>

> 🆕 **TIRM** (modifizierter IRR) reinvestiert Zuflüsse zum Projektzins — realistischer als IRR. **VUL** (gleichmäßiger Nettowert) wandelt den Kapitalwert in eine äquivalente Jahresreihe um.

> **TIR** = Projektrendite · **ILL (PI)** über 1 = schafft Wert · verglichen mit **SELIC** und dem **US-Zins** (reale Werte je Projekt in der Tabelle oben — Spalten `TIR>SELIC?`/`TIR>EUA?`). Der Fluss ist **dollarisiert** (USD/BRL) und zum US-Satz diskontiert → Spalten **VPL US$** und **PB desc. US$**. _Benchmarks (SELIC, US-Zins, Wechselkurs) sind Platzhalter — im `.env` anpassen._

**IRR je Projekt vs. Opportunitätskosten (SELIC × USA)**

<BarChart data={vpl} x=project_name y=tir title="TIR je Projekt vs. SELIC und US-Zins" yAxisTitle="TIR (pro Periode)" sort=true>
  <ReferenceLine y=0.105 color=warning label="SELIC (BR) ~10,5%"/>
  <ReferenceLine y=0.045 color=info label="US-Zins ~4,5%"/>
</BarChart>

**Investitionsrückgewinnung über die Zeit** (diskontiert kumuliert — Nulldurchgang = diskontierte Amortisation)

<LineChart data={vpl_fluxo} x=periodo y=cum_desc series=project_name title="Diskontierter kumulativer Cashflow je Periode" yAxisTitle="Diskontiert kumuliert (R$)" markers=true>
  <ReferenceLine y=0 color=negative label="break-even"/>
</LineChart>

## 💳 KI-Abonnements — Gesamtkosten mit IOF
> Wechselkurs **R$ 5,40/US$** · **IOF 3,5%** auf internationale Operationen (Karte). `Total = US$ × Kurs × (1 + IOF)`.
> Dies sind die realen Kosten für die Umlagebasis (`assinaturas_infra`). Ungefähre Preise — offizielle Seiten prüfen.

<DataTable data={planos} rows=all rowShading=true>
  <Column id=provedor title="Anbieter"/>
  <Column id=plano title="Plan"/>
  <Column id=usd_mes title="US$/mês" fmt=num0/>
  <Column id=r_base title="R$ base" fmt='$#,##0.00'/>
  <Column id=iof_reais title="IOF" fmt='$#,##0.00'/>
  <Column id=total_iof title="Total c/ IOF (R$)" fmt='$#,##0.00'/>
</DataTable>

<BarChart data={planos_pagos} x=plano y=total_iof title="Monatliche Gesamtkosten mit IOF je Plan (R$)" swapXY=true sort=true/>

<div style="display:flex;align-items:center;justify-content:center;gap:1rem;flex-wrap:wrap;margin:1.4rem 0 0.4rem;">
  <img src="/shark.svg" alt="tubarão investidor" width="120" height="82" style="flex:0 0 auto;"/>
  <h2 style="text-align:center;margin:0;font-weight:800;">🏆 AHP-TOPSIS 2N — Multikriterielles Entscheidungsmodell (MCDM)</h2>
  <img src="/gekko_photo.png" alt="Gordon Gekko fumando charuto (terno azul)" width="100" height="100" style="flex:0 0 auto;border-radius:50%;box-shadow:0 2px 8px rgba(0,0,0,.25);"/>
</div>

> **Auswahl des BESTEN Projekts** durch Gewichtung der Indikatoren als Kriterien. Gewichte per **AHP**
> (VPL 37% · TIR 24% · ILL 14% · PSR 14% · IITA 5,6% · IDLS 5,6% — CR = 0,012, consistente).
> Ranking per **TOPSIS** in **zwei Normalisierungen** (Vektor/Euklidisch + Min-Max/linear); der
> **Finaler Ci** ist der Durchschnitt. Spalte **Robust?** = beide Normalisierungen stimmen bei der Position überein.

**🥇 Siegerprojekt (höchster finaler Ci):**
<DataTable data={mcda_top}>
  <Column id=project_name title="🏆 Bestes Projekt"/>
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

> Der Sieger hat ein **Pitch Deck** generiert (siehe Ordner Projekte / `pitchdeck/`). Wo die Positionen 6–7 zwischen Normalisierungen abweichen, ist das Ranking am empfindlichsten — dort mit Vorsicht entscheiden.

### 📌 Bottom-Line — Zusammenfassung & C-Level-Insights

**Urteil.** Das Modell **AHP-TOPSIS 2n** wählt **{mcda_top[0].project_name}** als bestes Projekt des Portfolios (**Ci = 0,96** von 1,00), mit **bestätigter Robustheit**: Beide Normalisierungen (Vektor und Min-Max) stimmen beim **1. Platz** und in 8/10 des Rankings überein — die Spitze ist stabil, kein Methodenartefakt.

**Warum {mcda_top[0].project_name} gewann.** Die **finanziellen** Kriterien (Kapitalwert R$ 5.973 · IRR 32,9% · PI 1,75) sind projektübergreifend **gleichauf** (Cashflow noch ein einheitlicher *Platzhalter*). Mit neutralisiertem Finanzteil verlagert sich die Entscheidung auf die **operative Effizienz**, und dort dominiert {mcda_top[0].project_name}: niedrigste **Halluzinationsrate (IITA 9,1%)** und geringste **Lean-Verschwendung (IDLS 15,0%)** im Portfolio — fast **die Hälfte** des Zweitplatzierten. Mit anderen Worten: **gleiche projizierte Rendite bei weit weniger Token-/Cash-Verschwendung.**

**C-Level-Insights.**
- 🥇 **Effizienz ist der Tiebreaker:** bei ähnlicher Rendite liefert, wer **weniger verbrennt** (niedrigere IITA/IDLS), denselben Wert mit höherer Marge — das am besten skalierbare Asset.
- 🛡️ **Entscheidungsrobustheit:** die Übereinstimmung beider Normalisierungen (8/10) gibt dem Board **Sicherheit**, an der Spitze des Rankings zu handeln; die sensible Zone (Positionen 6–7) erfordert qualitative Analyse vor dem Streichen.
- 📉 **Risiko-Ausläufer:** der Letztplatzierte (Ci 0,01) hat die schlechteste Gesamtleistung — Kandidat für **Refactoring oder Einstellung** (mit der BCG-Matrix abgleichen).

**⚠️ Vorbehalt zur Entscheidungsehrlichkeit.** Die finanziellen Kriterien tragen **75% des AHP-Gewichts** (Kapitalwert 37% + IRR 24% + PI 14%), differenzieren aber heute **nicht**, da der Cashflow ein Platzhalter ist. **Das Urteil ist erst mit REALEN projektbezogenen Cashflows endgültig** — nach Eingabe kann sich das Ranking erheblich ändern (der Finanzteil wird wieder dominieren).

**Empfehlung.** (1) {mcda_top[0].project_name} als **Skalierungs-Pilot** aufgrund nachgewiesener Effizienz genehmigen; (2) die **realen Cashflows** eingeben und `ahp_topsis.py` für das endgültige Finanzurteil erneut ausführen; (3) einen Verbesserungsplan für den Ausläufer (Letztplatzierten) anstoßen.

---
## 👑 Verwaltungsdossier des **Kronjuwels** — {mcda_top[0].project_name}

> Klassische Verwaltungswerkzeuge, **ausschließlich auf das auserwählte Projekt** angewandt, um es zu bereichern, hervorzuheben und seinen **Wettbewerbsvorteil** sichtbar zu machen. Alle werden von einer **nebenläufigen Python-Pipeline** (`gerar_admtools.py`) erzeugt — ohne externe Vorlage. Details und Begründung in `foundations/admtools/ferramentas_administrativas.md`.

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:1.2rem;margin:1rem 0;">

<div>

**🎯 SWOT — strategische Position**
Stärken/Schwächen/Chancen/Risiken aus realen KPIs (niedrigste IITA und IDLS = dominante Stärke).
<img src="/admtools/de/swot.png" alt="SWOT do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🌐 PESTELC — Makroumfeld**
Sieben externe Faktoren (Politisch, Ökonomisch, Sozial, Technologisch, Ökologisch, Rechtlich, Kulturell).
<img src="/admtools/de/pestel.png" alt="PESTELC do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🗺️ 5W4H — Aktionsplan (5W + 4H)**
What/Why/Where/When/Who + How/How much/How many/How long — Skalierungs-Fahrplan des Auserwählten.
<img src="/admtools/de/5w4h.png" alt="5W4H do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**📊 Fehler-Pareto (80/20)**
Prompt-Kategorien mit 80% der Fehler — wo zuerst anzugreifen (echte Langfuse-Daten).
<img src="/admtools/de/pareto.png" alt="Pareto de falhas do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🔥 GUT-Matrix — Priorisierung (Heatmap)**
Schwere × Dringlichkeit × Tendenz der Maßnahmen; höherer GUT = zuerst handeln.
<img src="/admtools/de/gut.png" alt="Matriz GUT do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🕸️ Wettbewerbsradar — Differenzierung**
Fingerabdruck des Auserwählten **vs Portfolio-Durchschnitt** (die blaue Fläche dominiert die graue auf fast jeder Achse).
<img src="/admtools/de/radar.png" alt="Radar competitivo do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>

</div>

> **📌 Executive-Lesart.** Das **Radar** zeigt den Wettbewerbsvorteil: das Kronjuwel übertrifft den Durchschnitt bei Anti-Halluzination, Lean und nützlicher Lieferung. **SWOT/PESTEL/5W4H** überführen diese Diagnose in **Strategie und Aktionsplan**; **Pareto + GUT** sagen **genau, wo** zuerst zu handeln ist, um operative Führung in eine endgültige finanzielle Rendite umzuwandeln.

---
## 🔗 Einzelpanels je Projekt

{#each kpis as p}
<a href="/de/projetos/{p.project_name}">▶️ {p.project_name} — PSR {p.kpi_psr}</a>
{/each}
