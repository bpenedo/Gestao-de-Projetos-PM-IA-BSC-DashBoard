---
title: Panneau BSC — Gestion de Projets (PM) IA
---

🌐 [Português](/) · [English](/en) · [Español](/es) · **Français** · [Deutsch](/de) · [中文](/zh) · [한국어](/ko) · [हिन्दी](/hi) · [עברית](/he) · [Svenska](/sv) · [Русский](/ru) · [Suomi](/fi)


🌐 **Português** · [English](/en) · [Español](/es) · [Français](/fr) · [Deutsch](/de) · [中文](/zh) · [한국어](/ko) · [हिन्दी](/hi)


_Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com_
**Point Hebdomadaire — chaque vendredi à 09h00.**

> ⚠️ **Données DÉMO** (portefeuille anonymisé). Deviennent réelles dès la synchro Langfuse.

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

## 📈 Résumé Exécutif du Portefeuille

<BigValue data={kpis} value=total_tokens title="Tokens totaux" agg=sum fmt=num0/>
<BigValue data={kpis} value=kpi_psr title="PSR moyen (0-5)" agg=mean fmt=num1/>
<BigValue data={kpis} value=kpi_idls_lean title="Gaspillage Lean moyen %" agg=mean fmt=num1/>
<BigValue data={kpis} value=burn_rate_ia title="Burn Rate total" agg=sum fmt='$#,##0.00'/>

## 🌐 Carte 5D du Portefeuille (vue C-Level)
> Sphères 3D (style 5dchart) — **5 dimensions par projet** : **X**=Volume/échelle (tokens) · **Y**=PEUC/qualité (%) · **Z**=PSR/santé (0–5) · **taille**=Burn Rate (R$) · **couleur**=ICCA/durabilité (🟢 au-dessus de 3x couvre le coût · 🔴 sous 1x = perte).
>
> **Lecture pour le conseil :** le projet idéal est à **droite/au fond** (échelle+qualité), **haut** (PSR) et **vert** (durable). Sphère **grande et rouge** = beaucoup de trésorerie brûlée sans couverture → corriger avant de passer à l'échelle.

![Mapa 5D do Portfólio de Projetos de IA](/5d_projetos.png?v=5)

### 🖱️ Carte 5D Interactive — survolez chaque sphère
> **X** = Tokens (échelle) · **Y** = PEUC (%) · **taille** = PSR (0–5) · **couleur** = ICCA (🟢 durable · 🟠 limite · 🔴 perte). Survolez chaque **sphère glossy** pour voir **Nom du projet, PSR, PEUC et Tokens**.

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

## 📉 Tendance de l'Indicateur Maître (CPP) et du Score (PSR)
> Ce qui compte le plus pour le C-Level : **la direction**. CPP en baisse = portefeuille plus efficient.

<LineChart data={tendencia} x=data_snapshot y=cpp_medio yAxisTitle="CPP médio (R$/%)" title="Coût par Point de Progrès — tendance du portefeuille" markers=true/>

<LineChart data={tendencia} x=data_snapshot y=psr_medio yAxisTitle="PSR médio" yMin=0 yMax=5 title="Score moyen du portefeuille (PSR 0-5)" markers=true/>

## ⭐ Score (PSR) par Projet

<BarChart data={kpis} x=project_name y=kpi_psr swapXY=true title="PSR (0-5) par projet — trié" sort=true labels=true/>

## 🍩 Composition et Mix (donut avec profondeur)

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

## 🧭 Quadrant de Durabilité (passer à l'échelle ou corriger ?)
> Axe X = **ICCA** (couverture : au-dessus de 3x = sain) · Axe Y = **IBMT** (burn marginal : sous 0,33 = bon) · taille = Burn Rate.
> En bas à droite = **passer à l'échelle avec profit** ; en haut à gauche = **corriger avant de croître**.

<ScatterPlot data={kpis} x=kpi_icca y=kpi_ibmt series=project_name size=burn_rate_ia xAxisTitle="ICCA — cobertura de custo (x)" yAxisTitle="IBMT — burn marginal (x)" title="Durabilité financière par projet"/>

## 📊 Pareto des Défaillances par Projet

<BarChart data={falhas} x=project_name y=percentual_dominancia series=categoria_falha type=stacked100 swapXY=true title="Dominance des défaillances (%) par projet"/>

## 🗂️ Score et Santé Financière (tableau)

<DataTable data={kpis} rows=all rowShading=true>
  <Column id=project_name title="Projet"/>
  <Column id=kpi_psr title="PSR" fmt=num2/>
  <Column id=kpi_peuc title="PEUC %" fmt=num1/>
  <Column id=kpi_iita title="IITA %" fmt=num1/>
  <Column id=kpi_idls_lean title="IDLS %" fmt=num1/>
  <Column id=vrt_por_ktoken title="VRT/kT" fmt='$#,##0.0000'/>
  <Column id=kpi_icca title="ICCA x" fmt=num2/>
  <Column id=kpi_ibmt title="IBMT x" fmt=num3/>
  <Column id=kpi_cpp title="CPP R$/%" fmt='$#,##0.00'/>
</DataTable>

## 🚨 Alertes Critiques

<DataTable data={alertas} rows=8>
  <Column id=project_name title="Projet"/>
  <Column id=tipo_erro title="Défaillance"/>
  <Column id=tokens_desperdicados title="Tokens" fmt=num0/>
  <Column id=data_evento title="Quand"/>
</DataTable>

## 📅 Ordre du Jour de la Réunion Hebdomadaire

<DataTable data={reuniao} rows=all>
  <Column id=project_name title="Projet"/>
  <Column id=sumario_executivo title="Résumé"/>
  <Column id=acoes_corretivas_lean title="Actions Lean (PDCA)"/>
</DataTable>

## 🪙 Récupération de Coût (VRT) — 5 blocs + moyenne (2e optique)
> Même base de répartition à **5 granularités** (R$ par 50/100/250/500/1 000 tokens) + la **moyenne des blocs** — une seconde vision de la consommation par projet.

<DataTable data={kpis} rows=all rowShading=true>
  <Column id=project_name title="Projet"/>
  <Column id=vrt_50t title="50 tok" fmt='#,##0.00000'/>
  <Column id=vrt_100t title="100 tok" fmt='#,##0.00000'/>
  <Column id=vrt_250t title="250 tok" fmt='#,##0.00000'/>
  <Column id=vrt_500t title="500 tok" fmt='#,##0.00000'/>
  <Column id=vrt_por_ktoken title="1.000 tok" fmt='#,##0.00000'/>
  <Column id=vrt_media_blocos title="MOY. blocs" fmt='#,##0.00000' contentType=colorscale/>
</DataTable>

## ⏰ Heure Critique d'Interruption/Impact (HCI)
> À quelle **heure de la journée (BRT)** chaque projet est le plus impacté — pour agir dans la bonne fenêtre (upgrade de Tier, backoff, planification).

<BarChart data={hora_total} x=hora_brt y=interrupcoes title="Interruptions par heure (BRT) — portefeuille" xAxisTitle="Hora (0-23, BRT)"/>

<DataTable data={horario_critico} rows=all rowShading=true>
  <Column id=project_name title="Projet"/>
  <Column id=hora_pico title="Heure de pointe (BRT)" fmt='0"h"'/>
  <Column id=interrupcoes_pico title="Interruptions au pic" fmt=num0/>
</DataTable>

## ♻️ Taxonomie des Gaspillages (Lean Six Sigma) — où l'on gaspille le plus
> Gaspillage mesuré par **tokens pondérés** (Défaut 2,0× · Quota 1,5× · Surtraitement 1,0× · Latence 0,5×), pas seulement par le nombre.

<Grid cols=2>
<Group>

**Mix de gaspillage du portefeuille**
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

**Gaspillage dominant par projet**
<DataTable data={waste_dom} rows=all>
  <Column id=project_name title="Projet"/>
  <Column id=waste_dominante title="Gaspillage dominant"/>
  <Column id=waste_tokens title="Tokens gaspillés" fmt=num0/>
</DataTable>

</Group>
</Grid>

<BarChart data={wastes} x=project_name y=waste_tokens series=categoria_waste type=stacked swapXY=true title="Composition du gaspillage (tokens pondérés) par projet"/>

## 🔬 RCA — Hallucination par Type de Prompt (ce qui RETARDE chaque projet)
> Root Cause Analysis : nous classons les prompts en **catégories** et mesurons l'hallucination de chacune.
> Diagnostic objectif de **ce qui retarde chaque projet** et **ce qui retarde COMMUNÉMENT tous (intersection)**.

### 🎯 Intersection — le goulot commun au portefeuille
> Le type de prompt qui est le **goulot d'hallucination nº1** dans le plus de projets. L'attaquer en premier a le plus grand effet systémique.

<BarChart data={rca_inter} x=prompt_categoria y=projetos_onde_e_top1 title="Type de prompt qui retarde le plus le portefeuille (goulot #1 dans N projets)" yAxisTitle="Nº de projetos onde é o gargalo #1" labels=true sort=true/>

### 🧭 Goulot d'hallucination par projet (RCA individuel)

<DataTable data={rca_proj} rows=all rowShading=true>
  <Column id=project_name title="Projet"/>
  <Column id=prompt_gargalo title="Prompt qui hallucine le plus (goulot)"/>
  <Column id=alucinacoes title="Hallucinations" fmt=num0/>
</DataTable>

### 📊 Taxonomie d'hallucination par catégorie × projet

<BarChart data={aluc_cat} x=project_name y=alucinacoes series=prompt_categoria type=stacked swapXY=true title="Hallucinations par type de prompt dans chaque projet"/>

## 💰 VAN, Payback et Flux de Trésorerie du Portefeuille
> Calculé à partir de **votre flux de trésorerie** (CSV/tableur — voir `pipeline/fluxo_caixa_template.csv` et `python3 carregar_fluxo.py VOTRE.csv`). VAN = Σ flux ÷ (1+i)ᵗ · Payback **simple** (variation temporelle) et **actualisé**, tous deux interpolés. _Données de démo jusqu'à ce que vous fournissiez votre CSV._

<DataTable data={vpl} rows=all rowShading=true>
  <Column id=project_name title="Projet"/>
  <Column id=vpl title="VPL (R$)" fmt='$#,##0' contentType=colorscale/>
  <Column id=tir title="TIR" fmt=pct1/>
  <Column id=tirm title="TIRM" fmt=pct1/>
  <Column id=ill title="ILL (PI)" fmt=num2/>
  <Column id=vul title="VUL (R$)" fmt='$#,##0'/>
  <Column id=payback_simples title="PB simple" fmt=num2/>
  <Column id=payback_descontado title="PB actualisé" fmt=num2/>
  <Column id=supera_selic title="TIR>SELIC?" fmt=boolean/>
  <Column id=supera_us title="TIR>EUA?" fmt=boolean/>
  <Column id=vpl_usd title="VPL US$" fmt='$#,##0'/>
  <Column id=payback_desc_usd title="PB desc. US$" fmt=num2/>
</DataTable>

> 🆕 **TIRM** (TRI modifié) réinvestit les entrées au taux du projet — plus réaliste que le TRI. **VUL** (valeur uniforme nette) convertit la VAN en série annuelle équivalente.

> **TIR** = retorno do projeto · **ILL (PI)** acima de 1 = cria valor · comparados à **SELIC** e aos **juros dos EUA** (valores reais por projeto na tabela acima — colunas `TIR>SELIC?`/`TIR>EUA?`). O fluxo é **dolarizado** (USD/BRL) e descontado à taxa americana → colunas **VPL US$** e **PB desc. US$**. _Benchmarks (SELIC, juros EUA, câmbio) são placeholders — ajuste no `.env`._

**TRI par projet vs. coût d'opportunité (SELIC × USA)**

<BarChart data={vpl} x=project_name y=tir title="TIR por projeto comparada à SELIC e aos juros dos EUA" yAxisTitle="TIR (por período)" sort=true>
  <ReferenceLine y=0.105 color=warning label="SELIC (BR) ~10,5%"/>
  <ReferenceLine y=0.045 color=info label="Juros EUA ~4,5%"/>
</BarChart>

**Recuperação do investimento ao longo do tempo** (acumulado descontado — cruza zero = payback descontado)

<LineChart data={vpl_fluxo} x=periodo y=cum_desc series=project_name title="Fluxo de caixa acumulado descontado por período" yAxisTitle="Acumulado descontado (R$)" markers=true>
  <ReferenceLine y=0 color=negative label="break-even"/>
</LineChart>

## 💳 Abonnements IA — Coût Total avec IOF
> Change **R$ 5,40/US$** · **IOF 3,5%** sur opération internationale (carte). `Total = US$ × change × (1 + IOF)`.
> C'est le coût réel qui alimente la base de répartition (`assinaturas_infra`). Prix approximatifs — vérifiez les sites officiels.

<DataTable data={planos} rows=all rowShading=true>
  <Column id=provedor title="Fournisseur"/>
  <Column id=plano title="Forfait"/>
  <Column id=usd_mes title="US$/mês" fmt=num0/>
  <Column id=r_base title="R$ base" fmt='$#,##0.00'/>
  <Column id=iof_reais title="IOF" fmt='$#,##0.00'/>
  <Column id=total_iof title="Total c/ IOF (R$)" fmt='$#,##0.00'/>
</DataTable>

<BarChart data={planos_pagos} x=plano y=total_iof title="Custo total mensal com IOF por plano (R$)" swapXY=true sort=true/>

<div style="display:flex;align-items:center;justify-content:center;gap:1rem;flex-wrap:wrap;margin:1.4rem 0 0.4rem;">
  <img src="/shark.svg" alt="tubarão investidor" width="120" height="82" style="flex:0 0 auto;"/>
  <h2 style="text-align:center;margin:0;font-weight:800;">🏆 AHP-TOPSIS 2N — Modèle de Décision Multicritère (MCDM)</h2>
  <img src="/gekko_photo.png" alt="Gordon Gekko fumando charuto (terno azul)" width="100" height="100" style="flex:0 0 auto;border-radius:50%;box-shadow:0 2px 8px rgba(0,0,0,.25);"/>
</div>

> **Choix du MEILLEUR projet** en pondérant les indicateurs comme critères. Poids par **AHP**
> (VPL 37% · TIR 24% · ILL 14% · PSR 14% · IITA 5,6% · IDLS 5,6% — CR = 0,012, consistente).
> Ranking por **TOPSIS** em **duas normalizações** (vetorial/Euclidiana + min-max/linear); o
> **Ci final** est la moyenne. Colonne **Robuste ?** = les deux normalisations s'accordent sur la position.

**🥇 Projet gagnant (Ci final le plus élevé) :**
<DataTable data={mcda_top}>
  <Column id=project_name title="🏆 Meilleur Projet"/>
  <Column id=ci_final title="Ci final" fmt=num4/>
</DataTable>

<BarChart data={mcda} x=project_name y=ci_final title="Ranking AHP-TOPSIS 2n (Ci final, 0–1)" swapXY=true sort=true labels=true/>

<DataTable data={mcda} rows=all rowShading=true>
  <Column id=rank_final title="#"/>
  <Column id=project_name title="Projet"/>
  <Column id=ci_vector title="Ci vetorial" fmt=num4/>
  <Column id=ci_minmax title="Ci min-max" fmt=num4/>
  <Column id=ci_final title="Ci final" fmt=num4/>
  <Column id=concordante title="Robuste ?" fmt=boolean/>
</DataTable>

> Le gagnant a un **pitch deck** généré (voir le dossier Projets / `pitchdeck/`). Là où les positions 6–7 divergent entre normalisations, le classement est le plus sensible — décidez avec prudence.

### 📌 Bottom-Line — Résumé Exécutif et Insights C-Level

**Verdict.** Le modèle **AHP-TOPSIS 2n** élit **{mcda_top[0].project_name}** comme meilleur projet du portefeuille (**Ci = 0,96** sur 1,00), avec **robustesse confirmée** : les deux normalisations (vectorielle et min-max) s'accordent sur la **1re place** et sur 8/10 du classement — le sommet est stable, pas un artefact de méthode.

**Pourquoi {mcda_top[0].project_name} a gagné.** Les critères **financiers** (VAN R$ 5 973 · TRI 32,9% · IP 1,75) sont **à égalité** entre projets (flux de trésorerie encore un *placeholder* uniforme). Le financier neutralisé, la décision passe à l'**efficience opérationnelle**, et là {mcda_top[0].project_name} domine : il a le **plus faible taux d'hallucination (IITA 9,1%)** et le **plus faible gaspillage Lean (IDLS 15,0%)** du portefeuille — presque **la moitié** du 2e. Autrement dit : **même rendement projeté, avec bien moins de gaspillage de tokens/trésorerie.**

**Insights C-Level.**
- 🥇 **L'efficience départage :** à rendement comparable, celui qui **brûle moins** (IITA/IDLS plus faibles) livre la même valeur à meilleure marge — l'actif le plus scalable.
- 🛡️ **Robustesse décisionnelle :** l'accord entre les deux normalisations (8/10) donne au conseil la **confiance** d'agir en tête du classement ; la zone sensible (positions 6–7) exige une analyse qualitative avant de trancher.
- 📉 **Queue de risque :** le dernier classé (Ci 0,01) cumule la pire performance — candidat à la **refonte ou l'abandon** (croiser avec la matrice BCG).

**⚠️ Réserve d'honnêteté décisionnelle.** Les critères financiers portent **75% du poids AHP** (VAN 37% + TRI 24% + IP 14%), mais aujourd'hui ils **ne différencient pas** car le flux de trésorerie est un placeholder. **Le verdict n'est définitif qu'avec les flux de trésorerie RÉELS par projet** — une fois saisis, le classement peut changer substantiellement (le financier redominera).

**Recommandation.** (1) Approuver {mcda_top[0].project_name} comme **pilote de montée en charge** pour son efficience prouvée ; (2) saisir les **flux de trésorerie réels** et relancer `ahp_topsis.py` pour le verdict financier définitif ; (3) déclencher un plan d'amélioration sur la queue (le dernier classé).

---
## 👑 Dossier Administratif du **Joyau de la Couronne** — {mcda_top[0].project_name}

> Outils administratifs classiques appliqués **exclusivement au projet élu** pour l'enrichir, le valoriser et mettre en évidence son **avantage concurrentiel**. Tous sont générés par un **pipeline Python concurrent** (`gerar_admtools.py`) — sans aucun template externe. Détails et justification dans `foundations/admtools/ferramentas_administrativas.md`.

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:1.2rem;margin:1rem 0;">

<div>

**🎯 SWOT — position stratégique**
Forces/faiblesses/opportunités/menaces dérivées des KPI réels (IITA et IDLS les plus bas = force dominante).
<img src="/admtools/swot.png" alt="SWOT do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🌐 PESTELC — macro-environnement**
Sept facteurs externes (Politique, Économique, Social, Technologique, Écologique, Légal, Culturel).
<img src="/admtools/pestel.png" alt="PESTELC do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🗺️ 5W4H — plan d'action (5W + 4H)**
What/Why/Where/When/Who + How/How much/How many/How long — feuille de route de montée en charge de l'élu.
<img src="/admtools/5w4h.png" alt="5W4H do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**📊 Pareto des défaillances (80/20)**
Catégories de prompt concentrant 80% des défaillances — où attaquer d'abord (données réelles Langfuse).
<img src="/admtools/pareto.png" alt="Pareto de falhas do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🔥 Matrice GUT — priorisation (heatmap)**
Gravité × Urgence × Tendance des actions ; GUT plus élevé = agir en premier.
<img src="/admtools/gut.png" alt="Matriz GUT do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>
<div>

**🕸️ Radar concurrentiel — différenciateur**
Empreinte de l'élu **vs moyenne du portefeuille** (la zone bleue domine la grise sur presque chaque axe).
<img src="/admtools/radar.png" alt="Radar competitivo do projeto eleito" style="width:100%;border-radius:8px;"/>

</div>

</div>

> **📌 Lecture exécutive.** Le **radar** dépeint l'avantage concurrentiel : le Joyau de la Couronne dépasse la moyenne en anti-hallucination, Lean et livraison utile. **SWOT/PESTEL/5W4H** transforment ce diagnostic en **stratégie et plan d'action** ; **Pareto + GUT** disent **exactement où** agir d'abord pour convertir le leadership opérationnel en rendement financier définitif.

---
## 🔗 Tableaux Individuels par Projet

{#each kpis as p}
<a href="/projetos/{p.project_name}">▶️ {p.project_name} — PSR {p.kpi_psr}</a>
{/each}
