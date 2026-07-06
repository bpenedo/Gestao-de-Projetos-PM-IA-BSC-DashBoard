---
title: "פרויקט: {params.projeto}"
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
select CASE categoria_waste WHEN 'Defeito (Defects) - Alucinacao/Retrabalho' THEN 'פגם - הזיה/עבודה חוזרת' WHEN 'Defeito - Alucinacao' THEN 'פגם - הזיה' WHEN 'Espera (Waiting) - Cota/429' THEN 'המתנה - מכסה/429' WHEN 'Espera - Cota/429' THEN 'המתנה - מכסה/429' WHEN 'Espera (Waiting) - Latencia Alta' THEN 'המתנה - השהיה גבוהה' WHEN 'Espera - Latencia Alta' THEN 'המתנה - השהיה גבוהה' WHEN 'Superprocessamento - Prompt Inflado' THEN 'עיבוד-יתר - פרומפט מנופח' ELSE categoria_waste END as categoria_waste, waste_tokens, pct_do_projeto, CASE solucao WHEN 'Fila com backoff + fallback por cota + upgrade de Tier (meta IOLI abaixo de 1%)' THEN 'תור עם backoff + fallback לפי מכסה + שדרוג Tier (יעד IOLI מתחת ל-1%)' WHEN 'System prompt rigido + saida JSON + validacao LLM-as-judge (meta IITA abaixo de 10%)' THEN 'system prompt נוקשה + פלט JSON + אימות LLM-as-judge (יעד IITA מתחת ל-10%)' WHEN 'RAG/embeddings + sumarizacao + poda de historico (meta ITR estavel ou em queda)' THEN 'RAG/embeddings + תמצות + גיזום היסטוריה (יעד ITR יציב/יורד)' WHEN 'Streaming/TTFT + modelo rapido + cache (meta latencia abaixo de 3s)' THEN 'Streaming/TTFT + מודל מהיר + מטמון (יעד השהיה מתחת ל-3s)' WHEN 'Converter aberto em estruturado: system prompt restritivo + few-shot + guardrails de escopo' THEN 'המרת פתוח למובנה: system prompt מגביל + few-shot + guardrails להיקף' WHEN 'Few-shot valido + exigir testes + validacao de sintaxe/execucao + RAG das docs da lib' THEN 'few-shot תקף + דרישת בדיקות + אימות תחביר/הרצה + RAG של תיעוד הספרייה' WHEN 'Decomposicao em etapas + verificacao por etapa + self-consistency' THEN 'פירוק לשלבים + אימות לכל שלב + self-consistency' WHEN 'JSON mode/schema + regex de validacao + exemplos entrada-saida' THEN 'JSON mode/schema + regex אימות + דוגמאות קלט-פלט' WHEN 'Melhorar retrieval (re-rank) + citar fontes + grounding obrigatorio' THEN 'שיפור retrieval (re-rank) + ציטוט מקורות + grounding חובה' WHEN 'Templates fixos + exemplos de saida + JSON mode' THEN 'תבניות קבועות + דוגמאות פלט + JSON mode' WHEN 'Limites de tamanho + instrucoes de fidelidade + QA factual' THEN 'מגבלות גודל + הנחיות נאמנות + QA עובדתי' ELSE solucao END as solucao from bsc.wastes_lean where project_name = '${params.projeto}' order by waste_tokens desc
```

```sql aluc_proj
select CASE prompt_categoria WHEN 'Conversa/Aberto' THEN 'שיחה/פתוח' WHEN 'RAG/Busca' THEN 'RAG/חיפוש' WHEN 'Transformacao/Formato' THEN 'המרה/פורמט' WHEN 'Raciocinio/Analise' THEN 'הסקה/ניתוח' WHEN 'Sumarizacao' THEN 'תמצות' WHEN 'Geracao de Codigo' THEN 'יצירת קוד' WHEN 'Extracao de Dados' THEN 'חילוץ נתונים' ELSE prompt_categoria END as prompt_categoria, alucinacoes, taxa_aluc, CASE solucao WHEN 'Fila com backoff + fallback por cota + upgrade de Tier (meta IOLI abaixo de 1%)' THEN 'תור עם backoff + fallback לפי מכסה + שדרוג Tier (יעד IOLI מתחת ל-1%)' WHEN 'System prompt rigido + saida JSON + validacao LLM-as-judge (meta IITA abaixo de 10%)' THEN 'system prompt נוקשה + פלט JSON + אימות LLM-as-judge (יעד IITA מתחת ל-10%)' WHEN 'RAG/embeddings + sumarizacao + poda de historico (meta ITR estavel ou em queda)' THEN 'RAG/embeddings + תמצות + גיזום היסטוריה (יעד ITR יציב/יורד)' WHEN 'Streaming/TTFT + modelo rapido + cache (meta latencia abaixo de 3s)' THEN 'Streaming/TTFT + מודל מהיר + מטמון (יעד השהיה מתחת ל-3s)' WHEN 'Converter aberto em estruturado: system prompt restritivo + few-shot + guardrails de escopo' THEN 'המרת פתוח למובנה: system prompt מגביל + few-shot + guardrails להיקף' WHEN 'Few-shot valido + exigir testes + validacao de sintaxe/execucao + RAG das docs da lib' THEN 'few-shot תקף + דרישת בדיקות + אימות תחביר/הרצה + RAG של תיעוד הספרייה' WHEN 'Decomposicao em etapas + verificacao por etapa + self-consistency' THEN 'פירוק לשלבים + אימות לכל שלב + self-consistency' WHEN 'JSON mode/schema + regex de validacao + exemplos entrada-saida' THEN 'JSON mode/schema + regex אימות + דוגמאות קלט-פלט' WHEN 'Melhorar retrieval (re-rank) + citar fontes + grounding obrigatorio' THEN 'שיפור retrieval (re-rank) + ציטוט מקורות + grounding חובה' WHEN 'Templates fixos + exemplos de saida + JSON mode' THEN 'תבניות קבועות + דוגמאות פלט + JSON mode' WHEN 'Limites de tamanho + instrucoes de fidelidade + QA factual' THEN 'מגבלות גודל + הנחיות נאמנות + QA עובדתי' ELSE solucao END as solucao from bsc.alucinacao_categoria where project_name = '${params.projeto}' and alucinacoes > 0 order by alucinacoes desc
```

# 🛠️ {params.projeto}

<BigValue data={proj} value=kpi_psr title="PSR (0-5)" fmt=num2/>
<BigValue data={proj} value=kpi_peuc title="PEUC (%)" fmt=num1/>
<BigValue data={proj} value=total_tokens title="Tokens" fmt=num0/>
<BigValue data={proj} value=kpi_cpp title="CPP (R$/%)" fmt='$#,##0.00'/>

## אבחון יעילות

<DataTable data={proj}>
  <Column id=kpi_iita title="IITA % (הזיה)" fmt=num1/>
  <Column id=kpi_idls_lean title="IDLS % (בזבוז Lean)" fmt=num1/>
  <Column id=kpi_ioli title="IOLI % (חוסר-פעילות)" fmt=num1/>
  <Column id=kpi_itr title="ITR (tok/req)" fmt=num0/>
  <Column id=kpi_ieet_hh_por_mtoken title="IEET (HH/M-tok)" fmt=num2/>
</DataTable>

## בריאות פיננסית (Gitman & Startup)

<DataTable data={proj}>
  <Column id=vrt_por_ktoken title="VRT/kT (R$/1k)" fmt='$#,##0.0000'/>
  <Column id=burn_rate_ia title="Burn Rate של AI (R$)" fmt='$#,##0.00'/>
  <Column id=kpi_icca title="ICCA (x)" fmt=num2/>
  <Column id=kpi_ibmt title="IBMT (x)" fmt=num3/>
</DataTable>

## פארטו כשלים לפרויקט זה

<BarChart data={falhas_proj} x=categoria_falha y=quantidade title="כשלים לפי קטגוריה" swapXY=true/>

## 🪙 עלות השבה (VRT) — 5 בלוקים + ממוצע
<DataTable data={proj}>
  <Column id=vrt_50t title="50 tok" fmt='#,##0.00000'/>
  <Column id=vrt_100t title="100 tok" fmt='#,##0.00000'/>
  <Column id=vrt_250t title="250 tok" fmt='#,##0.00000'/>
  <Column id=vrt_500t title="500 tok" fmt='#,##0.00000'/>
  <Column id=vrt_por_ktoken title="1.000 tok" fmt='#,##0.00000'/>
  <Column id=vrt_media_blocos title="ממוצע" fmt='#,##0.00000'/>
</DataTable>

## ⏰ שעת ההפרעה הקריטית (BRT)
<BarChart data={hora_proj} x=hora_brt y=interrupcoes title="הפרעות לפי שעה ביום (BRT)" xAxisTitle="שעה (0-23)"/>

## ♻️ טקסונומיית בזבוזים (Lean Six Sigma)
<BarChart data={waste_proj} x=categoria_waste y=waste_tokens title="בזבוז לפי קטגוריה (טוקנים משוקללים)" swapXY=true labels=true/>

## 🔬 RCA — הזיה לפי סוג פרומפט (מה שמעכב פרויקט זה)
<BarChart data={aluc_proj} x=prompt_categoria y=alucinacoes title="הזיות לפי סוג פרומפט" swapXY=true labels=true sort=true/>

<DataTable data={aluc_proj}>
  <Column id=prompt_categoria title="סוג פרומפט"/>
  <Column id=alucinacoes title="הזיות" fmt=num0/>
  <Column id=taxa_aluc title="שיעור %" fmt=num1/>
</DataTable>

---

# 📌 שורה תחתונה — אבחון מסכם ופתרון מוחלט
_תקן שיפור מתמיד — מקור קנוני: `foundations/solucoes_relatorios.md`._

## a) מסת בזבוזים (Lean Six Sigma)
{#if waste_proj.length > 0}
ה**בזבוז הדומיננטי** של פרויקט זה הוא **{waste_proj[0].categoria_waste}**, האחראי ל-**{waste_proj[0].pct_do_projeto}%** מהבזבוז המשוקלל. הוא צורך טוקנים/מזומן ללא קידום ולכן **מעלה את ה-CPP**. הפתרון המוחלט ושאר הקטגוריות בטבלה (ליישם לפי השפעה):

<DataTable data={waste_proj}>
  <Column id=categoria_waste title="בזבוז שזוהה"/>
  <Column id=waste_tokens title="טוקנים מבוזבזים" fmt=num0/>
  <Column id=pct_do_projeto title="% מהבזבוז" fmt=num1/>
  <Column id=solucao title="🛠️ פתרון מוחלט (PDCA)" wrap=true/>
</DataTable>
{:else}
✅ לא נרשם בזבוז רלוונטי בתקופה זו.
{/if}

## b) מסת הזיות פרומפט (RCA לפי טקסונומיה)
{#if aluc_proj.length > 0}
**סוג הפרומפט שהכי מעכב** פרויקט זה הוא **{aluc_proj[0].prompt_categoria}**, עם **{aluc_proj[0].taxa_aluc}%** הזיה — **צוואר הבקבוק השורשי**. כל קטגוריה עם הזיה ונגד-הצעד המוחלט:

<DataTable data={aluc_proj}>
  <Column id=prompt_categoria title="סוג פרומפט"/>
  <Column id=alucinacoes title="הזיות" fmt=num0/>
  <Column id=taxa_aluc title="שיעור %" fmt=num1/>
  <Column id=solucao title="🛠️ פתרון מוחלט (RCA)" wrap=true/>
</DataTable>
{:else}
✅ לא נרשמו הזיות בתקופה זו — לא זוהה צוואר בקבוק.
{/if}

## c) שיפור מתמיד (PDCA / Kaizen)
1. **Plan** — לתקוף תחילה את הבזבוז הדומיננטי וצוואר הבקבוק שלמעלה.
2. **Do** — ליישם את הפתרונות המוחלטים מהטבלאות.
3. **Check** — למדוד בשבוע הבא: IITA, IDLS, IOLI, ITR והשהיה.
4. **Act** — לתקנן את מה שעבד ב-system prompt/pipeline ולחזור.

> **כוכב הצפון:** **CPP יורד** שבוע אחר שבוע. כל בזבוז והזיה שמצטמצמים מורידים את ה-CPP.
