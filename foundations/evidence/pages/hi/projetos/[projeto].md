---
title: "परियोजना: {params.projeto}"
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
select CASE categoria_waste WHEN 'Defeito (Defects) - Alucinacao/Retrabalho' THEN 'दोष - मतिभ्रम/पुनःकार्य' WHEN 'Defeito - Alucinacao' THEN 'दोष - मतिभ्रम' WHEN 'Espera (Waiting) - Cota/429' THEN 'प्रतीक्षा - कोटा/429' WHEN 'Espera - Cota/429' THEN 'प्रतीक्षा - कोटा/429' WHEN 'Espera (Waiting) - Latencia Alta' THEN 'प्रतीक्षा - उच्च विलंब' WHEN 'Espera - Latencia Alta' THEN 'प्रतीक्षा - उच्च विलंब' WHEN 'Superprocessamento - Prompt Inflado' THEN 'अतिप्रसंस्करण - फूला प्रॉम्प्ट' ELSE categoria_waste END as categoria_waste, waste_tokens, pct_do_projeto, CASE solucao WHEN 'Fila com backoff + fallback por cota + upgrade de Tier (meta IOLI abaixo de 1%)' THEN 'कतार+बैकऑफ + कोटा फॉलबैक + Tier अपग्रेड (लक्ष्य IOLI 1% से नीचे)' WHEN 'System prompt rigido + saida JSON + validacao LLM-as-judge (meta IITA abaixo de 10%)' THEN 'सख्त सिस्टम प्रॉम्प्ट + JSON आउटपुट + LLM-as-judge सत्यापन (लक्ष्य IITA 10% से नीचे)' WHEN 'RAG/embeddings + sumarizacao + poda de historico (meta ITR estavel ou em queda)' THEN 'RAG/embeddings + सारांश + इतिहास छँटाई (लक्ष्य ITR स्थिर/घटता)' WHEN 'Streaming/TTFT + modelo rapido + cache (meta latencia abaixo de 3s)' THEN 'स्ट्रीमिंग/TTFT + तेज़ मॉडल + कैश (लक्ष्य विलंब 3s से नीचे)' WHEN 'Converter aberto em estruturado: system prompt restritivo + few-shot + guardrails de escopo' THEN 'खुले को संरचित में बदलें: प्रतिबंधात्मक सिस्टम प्रॉम्प्ट + few-shot + स्कोप गार्डरेल' WHEN 'Few-shot valido + exigir testes + validacao de sintaxe/execucao + RAG das docs da lib' THEN 'मान्य few-shot + परीक्षण अनिवार्य + सिंटैक्स/निष्पादन सत्यापन + lib docs का RAG' WHEN 'Decomposicao em etapas + verificacao por etapa + self-consistency' THEN 'चरणबद्ध विघटन + प्रति-चरण सत्यापन + self-consistency' WHEN 'JSON mode/schema + regex de validacao + exemplos entrada-saida' THEN 'JSON mode/schema + सत्यापन regex + इनपुट-आउटपुट उदाहरण' WHEN 'Melhorar retrieval (re-rank) + citar fontes + grounding obrigatorio' THEN 'retrieval सुधार (re-rank) + स्रोत उद्धृत + अनिवार्य grounding' WHEN 'Templates fixos + exemplos de saida + JSON mode' THEN 'निश्चित टेम्पलेट + आउटपुट उदाहरण + JSON mode' WHEN 'Limites de tamanho + instrucoes de fidelidade + QA factual' THEN 'आकार सीमा + निष्ठा निर्देश + तथ्यात्मक QA' ELSE solucao END as solucao from bsc.wastes_lean where project_name = '${params.projeto}' order by waste_tokens desc
```

```sql aluc_proj
select CASE prompt_categoria WHEN 'Conversa/Aberto' THEN 'वार्ता/खुला' WHEN 'RAG/Busca' THEN 'RAG/खोज' WHEN 'Transformacao/Formato' THEN 'रूपांतरण/प्रारूप' WHEN 'Raciocinio/Analise' THEN 'तर्क/विश्लेषण' WHEN 'Sumarizacao' THEN 'सारांश' WHEN 'Geracao de Codigo' THEN 'कोड जनरेशन' WHEN 'Extracao de Dados' THEN 'डेटा निष्कर्षण' ELSE prompt_categoria END as prompt_categoria, alucinacoes, taxa_aluc, CASE solucao WHEN 'Fila com backoff + fallback por cota + upgrade de Tier (meta IOLI abaixo de 1%)' THEN 'कतार+बैकऑफ + कोटा फॉलबैक + Tier अपग्रेड (लक्ष्य IOLI 1% से नीचे)' WHEN 'System prompt rigido + saida JSON + validacao LLM-as-judge (meta IITA abaixo de 10%)' THEN 'सख्त सिस्टम प्रॉम्प्ट + JSON आउटपुट + LLM-as-judge सत्यापन (लक्ष्य IITA 10% से नीचे)' WHEN 'RAG/embeddings + sumarizacao + poda de historico (meta ITR estavel ou em queda)' THEN 'RAG/embeddings + सारांश + इतिहास छँटाई (लक्ष्य ITR स्थिर/घटता)' WHEN 'Streaming/TTFT + modelo rapido + cache (meta latencia abaixo de 3s)' THEN 'स्ट्रीमिंग/TTFT + तेज़ मॉडल + कैश (लक्ष्य विलंब 3s से नीचे)' WHEN 'Converter aberto em estruturado: system prompt restritivo + few-shot + guardrails de escopo' THEN 'खुले को संरचित में बदलें: प्रतिबंधात्मक सिस्टम प्रॉम्प्ट + few-shot + स्कोप गार्डरेल' WHEN 'Few-shot valido + exigir testes + validacao de sintaxe/execucao + RAG das docs da lib' THEN 'मान्य few-shot + परीक्षण अनिवार्य + सिंटैक्स/निष्पादन सत्यापन + lib docs का RAG' WHEN 'Decomposicao em etapas + verificacao por etapa + self-consistency' THEN 'चरणबद्ध विघटन + प्रति-चरण सत्यापन + self-consistency' WHEN 'JSON mode/schema + regex de validacao + exemplos entrada-saida' THEN 'JSON mode/schema + सत्यापन regex + इनपुट-आउटपुट उदाहरण' WHEN 'Melhorar retrieval (re-rank) + citar fontes + grounding obrigatorio' THEN 'retrieval सुधार (re-rank) + स्रोत उद्धृत + अनिवार्य grounding' WHEN 'Templates fixos + exemplos de saida + JSON mode' THEN 'निश्चित टेम्पलेट + आउटपुट उदाहरण + JSON mode' WHEN 'Limites de tamanho + instrucoes de fidelidade + QA factual' THEN 'आकार सीमा + निष्ठा निर्देश + तथ्यात्मक QA' ELSE solucao END as solucao from bsc.alucinacao_categoria where project_name = '${params.projeto}' and alucinacoes > 0 order by alucinacoes desc
```

# 🛠️ {params.projeto}

<BigValue data={proj} value=kpi_psr title="PSR (0-5)" fmt=num2/>
<BigValue data={proj} value=kpi_peuc title="PEUC (%)" fmt=num1/>
<BigValue data={proj} value=total_tokens title="Tokens" fmt=num0/>
<BigValue data={proj} value=kpi_cpp title="CPP (R$/%)" fmt='$#,##0.00'/>

## दक्षता निदान

<DataTable data={proj}>
  <Column id=kpi_iita title="IITA % (मतिभ्रम)" fmt=num1/>
  <Column id=kpi_idls_lean title="IDLS % (लीन अपव्यय)" fmt=num1/>
  <Column id=kpi_ioli title="IOLI % (निष्क्रियता)" fmt=num1/>
  <Column id=kpi_itr title="ITR (tok/req)" fmt=num0/>
  <Column id=kpi_ieet_hh_por_mtoken title="IEET (HH/M-tok)" fmt=num2/>
</DataTable>

## वित्तीय स्वास्थ्य (Gitman & Startup)

<DataTable data={proj}>
  <Column id=vrt_por_ktoken title="VRT/kT (R$/1k)" fmt='$#,##0.0000'/>
  <Column id=burn_rate_ia title="AI बर्न रेट (R$)" fmt='$#,##0.00'/>
  <Column id=kpi_icca title="ICCA (x)" fmt=num2/>
  <Column id=kpi_ibmt title="IBMT (x)" fmt=num3/>
</DataTable>

## इस परियोजना का विफलता पैरेटो

<BarChart data={falhas_proj} x=categoria_falha y=quantidade title="श्रेणी अनुसार विफलताएँ" swapXY=true/>

## 🪙 लागत वसूली (VRT) — 5 ब्लॉक + औसत
<DataTable data={proj}>
  <Column id=vrt_50t title="50 tok" fmt='#,##0.00000'/>
  <Column id=vrt_100t title="100 tok" fmt='#,##0.00000'/>
  <Column id=vrt_250t title="250 tok" fmt='#,##0.00000'/>
  <Column id=vrt_500t title="500 tok" fmt='#,##0.00000'/>
  <Column id=vrt_por_ktoken title="1.000 tok" fmt='#,##0.00000'/>
  <Column id=vrt_media_blocos title="औसत" fmt='#,##0.00000'/>
</DataTable>

## ⏰ महत्वपूर्ण व्यवधान समय (BRT)
<BarChart data={hora_proj} x=hora_brt y=interrupcoes title="दिन के घंटे अनुसार व्यवधान (BRT)" xAxisTitle="घंटा (0-23)"/>

## ♻️ अपव्यय वर्गीकरण (Lean Six Sigma)
<BarChart data={waste_proj} x=categoria_waste y=waste_tokens title="श्रेणी अनुसार अपव्यय (भारित टोकन)" swapXY=true labels=true/>

## 🔬 RCA — प्रॉम्प्ट प्रकार अनुसार मतिभ्रम (इस परियोजना को क्या धीमा करता है)
<BarChart data={aluc_proj} x=prompt_categoria y=alucinacoes title="प्रॉम्प्ट प्रकार अनुसार मतिभ्रम" swapXY=true labels=true sort=true/>

<DataTable data={aluc_proj}>
  <Column id=prompt_categoria title="प्रॉम्प्ट प्रकार"/>
  <Column id=alucinacoes title="मतिभ्रम" fmt=num0/>
  <Column id=taxa_aluc title="दर %" fmt=num1/>
</DataTable>

---

# 📌 निष्कर्ष — निर्णायक निदान व निश्चित समाधान
_सतत सुधार मानक — विहित स्रोत: `foundations/solucoes_relatorios.md`._

## a) अपव्यय विवेचन (Lean Six Sigma)
{#if waste_proj.length > 0}
इस परियोजना का **प्रमुख अपव्यय** **{waste_proj[0].categoria_waste}** है, जो भारित अपव्यय का **{waste_proj[0].pct_do_projeto}%**। यह प्रगति बढ़ाए बिना टोकन/नकदी खर्च करता है और **CPP ऊपर धकेलता है**। निश्चित समाधान व अन्य श्रेणियाँ नीचे तालिका में (प्रभाव क्रम में लागू):

<DataTable data={waste_proj}>
  <Column id=categoria_waste title="पाया गया अपव्यय"/>
  <Column id=waste_tokens title="बर्बाद टोकन" fmt=num0/>
  <Column id=pct_do_projeto title="अपव्यय का %" fmt=num1/>
  <Column id=solucao title="🛠️ निश्चित समाधान (PDCA)" wrap=true/>
</DataTable>
{:else}
✅ इस अवधि में कोई प्रासंगिक अपव्यय दर्ज नहीं।
{/if}

## b) प्रॉम्प्ट मतिभ्रम विवेचन (वर्गीकरण अनुसार RCA)
{#if aluc_proj.length > 0}
इस परियोजना को सर्वाधिक धीमा करने वाला **प्रॉम्प्ट प्रकार** **{aluc_proj[0].prompt_categoria}** है (**{aluc_proj[0].taxa_aluc}%** मतिभ्रम) — डिलीवरी की **मूल अड़चन**। प्रत्येक श्रेणी व उसका निश्चित प्रतिकार:

<DataTable data={aluc_proj}>
  <Column id=prompt_categoria title="प्रॉम्प्ट प्रकार"/>
  <Column id=alucinacoes title="मतिभ्रम" fmt=num0/>
  <Column id=taxa_aluc title="दर %" fmt=num1/>
  <Column id=solucao title="🛠️ निश्चित समाधान (RCA)" wrap=true/>
</DataTable>
{:else}
✅ इस अवधि में कोई मतिभ्रम नहीं — कोई प्रॉम्प्ट अड़चन नहीं।
{/if}

## c) सतत सुधार (PDCA / Kaizen)
1. **Plan** — पहले ऊपर बताए प्रमुख अपव्यय व प्रॉम्प्ट-अड़चन पर हमला।
2. **Do** — तालिकाओं के निश्चित समाधान लागू करें।
3. **Check** — अगले सप्ताह मापें: IITA, IDLS, IOLI, ITR व विलंब।
4. **Act** — जो काम किया उसे system prompt/pipeline में मानकीकृत कर दोहराएँ।

> **ध्रुवतारा:** सप्ताह-दर-सप्ताह **घटता CPP**। हर अपव्यय व मतिभ्रम घटने से CPP गिरता है।
