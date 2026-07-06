---
title: "Projekti: {params.projeto}"
---

```sql proj
select * from bsc.kpis_bsc_ia where project_name = '${params.projeto}'
```

```sql falhas_proj
select * from bsc.dominancia_erros where project_name = '${params.projeto}'
```

```sql hora_proj
select hora_brt, interrupcoes from bsc.interrupcoes_hora where project_name = '${params.projeto}' order by hora_brt
```

```sql waste_proj
select CASE categoria_waste WHEN 'Defeito (Defects) - Alucinacao/Retrabalho' THEN 'Vika - Hallusinaatio/Uusinta' WHEN 'Defeito - Alucinacao' THEN 'Vika - Hallusinaatio' WHEN 'Espera (Waiting) - Cota/429' THEN 'Odotus - Kiintiö/429' WHEN 'Espera - Cota/429' THEN 'Odotus - Kiintiö/429' WHEN 'Espera (Waiting) - Latencia Alta' THEN 'Odotus - Suuri viive' WHEN 'Espera - Latencia Alta' THEN 'Odotus - Suuri viive' WHEN 'Superprocessamento - Prompt Inflado' THEN 'Ylikäsittely - Paisunut prompt' ELSE categoria_waste END as categoria_waste, waste_tokens, pct_do_projeto, CASE solucao WHEN 'Fila com backoff + fallback por cota + upgrade de Tier (meta IOLI abaixo de 1%)' THEN 'Jono + backoff + kiintiö-fallback + Tier-päivitys (tavoite IOLI alle 1%)' WHEN 'System prompt rigido + saida JSON + validacao LLM-as-judge (meta IITA abaixo de 10%)' THEN 'Tiukka system prompt + JSON-tuloste + LLM-as-judge-validointi (tavoite IITA alle 10%)' WHEN 'RAG/embeddings + sumarizacao + poda de historico (meta ITR estavel ou em queda)' THEN 'RAG/embeddings + tiivistys + historian karsinta (tavoite ITR vakaa/laskeva)' WHEN 'Streaming/TTFT + modelo rapido + cache (meta latencia abaixo de 3s)' THEN 'Streaming/TTFT + nopea malli + välimuisti (tavoite viive alle 3s)' WHEN 'Converter aberto em estruturado: system prompt restritivo + few-shot + guardrails de escopo' THEN 'Muunna avoin rakenteiseksi: rajoittava system prompt + few-shot + laajuuden guardrails' WHEN 'Few-shot valido + exigir testes + validacao de sintaxe/execucao + RAG das docs da lib' THEN 'Kelvollinen few-shot + vaadi testit + syntaksi-/suoritustarkistus + kirjaston docs-RAG' WHEN 'Decomposicao em etapas + verificacao por etapa + self-consistency' THEN 'Vaiheittainen hajotus + vaihekohtainen todennus + self-consistency' WHEN 'JSON mode/schema + regex de validacao + exemplos entrada-saida' THEN 'JSON mode/schema + validointi-regex + syöte-tuloste-esimerkit' WHEN 'Melhorar retrieval (re-rank) + citar fontes + grounding obrigatorio' THEN 'Paranna retrievaliä (re-rank) + lähdeviitteet + pakollinen grounding' WHEN 'Templates fixos + exemplos de saida + JSON mode' THEN 'Kiinteät mallit + tulosteesimerkit + JSON mode' WHEN 'Limites de tamanho + instrucoes de fidelidade + QA factual' THEN 'Kokorajat + tarkkuusohjeet + faktapohjainen QA' ELSE solucao END as solucao from bsc.wastes_lean where project_name = '${params.projeto}' order by waste_tokens desc
```

```sql aluc_proj
select CASE prompt_categoria WHEN 'Conversa/Aberto' THEN 'Keskustelu/Avoin' WHEN 'RAG/Busca' THEN 'RAG/Haku' WHEN 'Transformacao/Formato' THEN 'Muunnos/Muoto' WHEN 'Raciocinio/Analise' THEN 'Päättely/Analyysi' WHEN 'Sumarizacao' THEN 'Tiivistäminen' WHEN 'Geracao de Codigo' THEN 'Koodin luonti' WHEN 'Extracao de Dados' THEN 'Tietojen poiminta' ELSE prompt_categoria END as prompt_categoria, alucinacoes, taxa_aluc, CASE solucao WHEN 'Fila com backoff + fallback por cota + upgrade de Tier (meta IOLI abaixo de 1%)' THEN 'Jono + backoff + kiintiö-fallback + Tier-päivitys (tavoite IOLI alle 1%)' WHEN 'System prompt rigido + saida JSON + validacao LLM-as-judge (meta IITA abaixo de 10%)' THEN 'Tiukka system prompt + JSON-tuloste + LLM-as-judge-validointi (tavoite IITA alle 10%)' WHEN 'RAG/embeddings + sumarizacao + poda de historico (meta ITR estavel ou em queda)' THEN 'RAG/embeddings + tiivistys + historian karsinta (tavoite ITR vakaa/laskeva)' WHEN 'Streaming/TTFT + modelo rapido + cache (meta latencia abaixo de 3s)' THEN 'Streaming/TTFT + nopea malli + välimuisti (tavoite viive alle 3s)' WHEN 'Converter aberto em estruturado: system prompt restritivo + few-shot + guardrails de escopo' THEN 'Muunna avoin rakenteiseksi: rajoittava system prompt + few-shot + laajuuden guardrails' WHEN 'Few-shot valido + exigir testes + validacao de sintaxe/execucao + RAG das docs da lib' THEN 'Kelvollinen few-shot + vaadi testit + syntaksi-/suoritustarkistus + kirjaston docs-RAG' WHEN 'Decomposicao em etapas + verificacao por etapa + self-consistency' THEN 'Vaiheittainen hajotus + vaihekohtainen todennus + self-consistency' WHEN 'JSON mode/schema + regex de validacao + exemplos entrada-saida' THEN 'JSON mode/schema + validointi-regex + syöte-tuloste-esimerkit' WHEN 'Melhorar retrieval (re-rank) + citar fontes + grounding obrigatorio' THEN 'Paranna retrievaliä (re-rank) + lähdeviitteet + pakollinen grounding' WHEN 'Templates fixos + exemplos de saida + JSON mode' THEN 'Kiinteät mallit + tulosteesimerkit + JSON mode' WHEN 'Limites de tamanho + instrucoes de fidelidade + QA factual' THEN 'Kokorajat + tarkkuusohjeet + faktapohjainen QA' ELSE solucao END as solucao from bsc.alucinacao_categoria where project_name = '${params.projeto}' and alucinacoes > 0 order by alucinacoes desc
```

# 🛠️ {params.projeto}

<BigValue data={proj} value=kpi_psr title="PSR (0-5)" fmt=num2/>
<BigValue data={proj} value=kpi_peuc title="PEUC (%)" fmt=num1/>
<BigValue data={proj} value=total_tokens title="Tokens" fmt=num0/>
<BigValue data={proj} value=kpi_cpp title="CPP (R$/%)" fmt='$#,##0.00'/>

## Tehokkuusdiagnoosi

<DataTable data={proj}>
  <Column id=kpi_iita title="IITA % (hallusinaatio)" fmt=num1/>
  <Column id=kpi_idls_lean title="IDLS % (Lean-hukka)" fmt=num1/>
  <Column id=kpi_ioli title="IOLI % (jouto)" fmt=num1/>
  <Column id=kpi_itr title="ITR (tok/req)" fmt=num0/>
  <Column id=kpi_ieet_hh_por_mtoken title="IEET (HH/M-tok)" fmt=num2/>
</DataTable>

## Taloudellinen terveys (Gitman & Startup)

<DataTable data={proj}>
  <Column id=vrt_por_ktoken title="VRT/kT (R$/1k)" fmt='$#,##0.0000'/>
  <Column id=burn_rate_ia title="Tekoälyn Burn Rate (R$)" fmt='$#,##0.00'/>
  <Column id=kpi_icca title="ICCA (x)" fmt=num2/>
  <Column id=kpi_ibmt title="IBMT (x)" fmt=num3/>
</DataTable>

## Tämän projektin vikojen Pareto

<BarChart data={falhas_proj} x=categoria_falha y=quantidade title="Viat kategorioittain" swapXY=true/>

## 🪙 Kustannusten kattaminen (VRT) — 5 lohkoa + keskiarvo
<DataTable data={proj}>
  <Column id=vrt_50t title="50 tok" fmt='#,##0.00000'/>
  <Column id=vrt_100t title="100 tok" fmt='#,##0.00000'/>
  <Column id=vrt_250t title="250 tok" fmt='#,##0.00000'/>
  <Column id=vrt_500t title="500 tok" fmt='#,##0.00000'/>
  <Column id=vrt_por_ktoken title="1.000 tok" fmt='#,##0.00000'/>
  <Column id=vrt_media_blocos title="KESKIM." fmt='#,##0.00000'/>
</DataTable>

## ⏰ Kriittinen keskeytystunti (BRT)
<BarChart data={hora_proj} x=hora_brt y=interrupcoes title="Keskeytykset tunneittain (BRT)" xAxisTitle="Tunti (0-23)"/>

## ♻️ Hukan taksonomia (Lean Six Sigma)
<BarChart data={waste_proj} x=categoria_waste y=waste_tokens title="Hukka kategorioittain (painotetut tokenit)" swapXY=true labels=true/>

## 🔬 RCA — hallusinaatio prompttyypeittäin (mikä viivästyttää tätä projektia)
<BarChart data={aluc_proj} x=prompt_categoria y=alucinacoes title="Hallusinaatiot prompttyypeittäin" swapXY=true labels=true sort=true/>

<DataTable data={aluc_proj}>
  <Column id=prompt_categoria title="Prompttyyppi"/>
  <Column id=alucinacoes title="Hallusinaatiot" fmt=num0/>
  <Column id=taxa_aluc title="Osuus %" fmt=num1/>
</DataTable>

---

# 📌 Loppupäätelmä — lopullinen diagnoosi ja ratkaisu
_Jatkuvan parantamisen standardi — kanoninen lähde: `foundations/solucoes_relatorios.md`._

## a) Hukan käsittely (Lean Six Sigma)
{#if waste_proj.length > 0}
Projektin **hallitseva hukka** on **{waste_proj[0].categoria_waste}**, joka on **{waste_proj[0].pct_do_projeto}%** painotetusta hukasta. Se kuluttaa tokeneita/rahaa edistämättä ja **nostaa CPP:tä**. Lopullinen ratkaisu ja muut kategoriat taulukossa (sovella vaikutuksen mukaan):

<DataTable data={waste_proj}>
  <Column id=categoria_waste title="Havaittu hukka"/>
  <Column id=waste_tokens title="Hukatut tokenit" fmt=num0/>
  <Column id=pct_do_projeto title="% hukasta" fmt=num1/>
  <Column id=solucao title="🛠️ Lopullinen ratkaisu (PDCA)" wrap=true/>
</DataTable>
{:else}
✅ Ei merkittävää hukkaa tällä jaksolla.
{/if}

## b) Prompt-hallusinaation käsittely (RCA taksonomialla)
{#if aluc_proj.length > 0}
Projektia eniten viivästyttävä **prompttyyppi** on **{aluc_proj[0].prompt_categoria}**, **{aluc_proj[0].taxa_aluc}%** hallusinaatiolla — toimitusten **juuripullonkaula**. Kukin kategoria ja sen lopullinen vastatoimi:

<DataTable data={aluc_proj}>
  <Column id=prompt_categoria title="Prompttyyppi"/>
  <Column id=alucinacoes title="Hallusinaatiot" fmt=num0/>
  <Column id=taxa_aluc title="Osuus %" fmt=num1/>
  <Column id=solucao title="🛠️ Lopullinen ratkaisu (RCA)" wrap=true/>
</DataTable>
{:else}
✅ Ei hallusinaatioita tällä jaksolla — ei pullonkaulaa.
{/if}

## c) Jatkuva parantaminen (PDCA / Kaizen)
1. **Plan** — hyökkää ensin hallitsevaan hukkaan ja prompt-pullonkaulaan.
2. **Do** — sovella taulukoiden lopulliset ratkaisut.
3. **Check** — mittaa ensi viikolla: IITA, IDLS, IOLI, ITR ja viive.
4. **Act** — vakioi toiminut system prompt/putkeen ja toista.

> **Pohjantähti:** **laskeva CPP** viikoittain. Jokainen vähennetty hukka ja hallusinaatio laskee CPP:tä.
