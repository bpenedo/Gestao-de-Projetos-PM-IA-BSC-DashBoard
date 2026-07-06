---
title: "Проект: {params.projeto}"
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
select CASE categoria_waste WHEN 'Defeito (Defects) - Alucinacao/Retrabalho' THEN 'Дефект - Галлюцинация/Переделка' WHEN 'Defeito - Alucinacao' THEN 'Дефект - Галлюцинация' WHEN 'Espera (Waiting) - Cota/429' THEN 'Ожидание - Квота/429' WHEN 'Espera - Cota/429' THEN 'Ожидание - Квота/429' WHEN 'Espera (Waiting) - Latencia Alta' THEN 'Ожидание - Высокая задержка' WHEN 'Espera - Latencia Alta' THEN 'Ожидание - Высокая задержка' WHEN 'Superprocessamento - Prompt Inflado' THEN 'Переобработка - Раздутый промпт' ELSE categoria_waste END as categoria_waste, waste_tokens, pct_do_projeto, CASE solucao WHEN 'Fila com backoff + fallback por cota + upgrade de Tier (meta IOLI abaixo de 1%)' THEN 'Очередь с backoff + fallback по квоте + апгрейд Tier (цель IOLI < 1%)' WHEN 'System prompt rigido + saida JSON + validacao LLM-as-judge (meta IITA abaixo de 10%)' THEN 'Строгий system prompt + JSON-вывод + валидация LLM-as-judge (цель IITA < 10%)' WHEN 'RAG/embeddings + sumarizacao + poda de historico (meta ITR estavel ou em queda)' THEN 'RAG/эмбеддинги + резюмирование + обрезка истории (цель ITR стабилен/снижается)' WHEN 'Streaming/TTFT + modelo rapido + cache (meta latencia abaixo de 3s)' THEN 'Стриминг/TTFT + быстрая модель + кэш (цель задержка < 3s)' WHEN 'Converter aberto em estruturado: system prompt restritivo + few-shot + guardrails de escopo' THEN 'Преобразовать открытое в структурированное: строгий system prompt + few-shot + guardrails области' WHEN 'Few-shot valido + exigir testes + validacao de sintaxe/execucao + RAG das docs da lib' THEN 'Валидный few-shot + требовать тесты + проверка синтаксиса/выполнения + RAG документации lib' WHEN 'Decomposicao em etapas + verificacao por etapa + self-consistency' THEN 'Пошаговая декомпозиция + проверка на шаге + self-consistency' WHEN 'JSON mode/schema + regex de validacao + exemplos entrada-saida' THEN 'JSON mode/schema + regex валидации + примеры вход-выход' WHEN 'Melhorar retrieval (re-rank) + citar fontes + grounding obrigatorio' THEN 'Улучшить retrieval (re-rank) + цитировать источники + обязательный grounding' WHEN 'Templates fixos + exemplos de saida + JSON mode' THEN 'Фиксированные шаблоны + примеры вывода + JSON mode' WHEN 'Limites de tamanho + instrucoes de fidelidade + QA factual' THEN 'Ограничения размера + инструкции точности + фактическая проверка' ELSE solucao END as solucao from bsc.wastes_lean where project_name = '${params.projeto}' order by waste_tokens desc
```

```sql aluc_proj
select CASE prompt_categoria WHEN 'Conversa/Aberto' THEN 'Диалог/Открытый' WHEN 'RAG/Busca' THEN 'RAG/Поиск' WHEN 'Transformacao/Formato' THEN 'Преобразование/Формат' WHEN 'Raciocinio/Analise' THEN 'Рассуждение/Анализ' WHEN 'Sumarizacao' THEN 'Резюмирование' WHEN 'Geracao de Codigo' THEN 'Генерация кода' WHEN 'Extracao de Dados' THEN 'Извлечение данных' ELSE prompt_categoria END as prompt_categoria, alucinacoes, taxa_aluc, CASE solucao WHEN 'Fila com backoff + fallback por cota + upgrade de Tier (meta IOLI abaixo de 1%)' THEN 'Очередь с backoff + fallback по квоте + апгрейд Tier (цель IOLI < 1%)' WHEN 'System prompt rigido + saida JSON + validacao LLM-as-judge (meta IITA abaixo de 10%)' THEN 'Строгий system prompt + JSON-вывод + валидация LLM-as-judge (цель IITA < 10%)' WHEN 'RAG/embeddings + sumarizacao + poda de historico (meta ITR estavel ou em queda)' THEN 'RAG/эмбеддинги + резюмирование + обрезка истории (цель ITR стабилен/снижается)' WHEN 'Streaming/TTFT + modelo rapido + cache (meta latencia abaixo de 3s)' THEN 'Стриминг/TTFT + быстрая модель + кэш (цель задержка < 3s)' WHEN 'Converter aberto em estruturado: system prompt restritivo + few-shot + guardrails de escopo' THEN 'Преобразовать открытое в структурированное: строгий system prompt + few-shot + guardrails области' WHEN 'Few-shot valido + exigir testes + validacao de sintaxe/execucao + RAG das docs da lib' THEN 'Валидный few-shot + требовать тесты + проверка синтаксиса/выполнения + RAG документации lib' WHEN 'Decomposicao em etapas + verificacao por etapa + self-consistency' THEN 'Пошаговая декомпозиция + проверка на шаге + self-consistency' WHEN 'JSON mode/schema + regex de validacao + exemplos entrada-saida' THEN 'JSON mode/schema + regex валидации + примеры вход-выход' WHEN 'Melhorar retrieval (re-rank) + citar fontes + grounding obrigatorio' THEN 'Улучшить retrieval (re-rank) + цитировать источники + обязательный grounding' WHEN 'Templates fixos + exemplos de saida + JSON mode' THEN 'Фиксированные шаблоны + примеры вывода + JSON mode' WHEN 'Limites de tamanho + instrucoes de fidelidade + QA factual' THEN 'Ограничения размера + инструкции точности + фактическая проверка' ELSE solucao END as solucao from bsc.alucinacao_categoria where project_name = '${params.projeto}' and alucinacoes > 0 order by alucinacoes desc
```

# 🛠️ {params.projeto}

<BigValue data={proj} value=kpi_psr title="PSR (0-5)" fmt=num2/>
<BigValue data={proj} value=kpi_peuc title="PEUC (%)" fmt=num1/>
<BigValue data={proj} value=total_tokens title="Tokens" fmt=num0/>
<BigValue data={proj} value=kpi_cpp title="CPP (R$/%)" fmt='$#,##0.00'/>

## Диагностика эффективности

<DataTable data={proj}>
  <Column id=kpi_iita title="IITA % (галлюцинация)" fmt=num1/>
  <Column id=kpi_idls_lean title="IDLS % (Lean-потери)" fmt=num1/>
  <Column id=kpi_ioli title="IOLI % (простой)" fmt=num1/>
  <Column id=kpi_itr title="ITR (tok/req)" fmt=num0/>
  <Column id=kpi_ieet_hh_por_mtoken title="IEET (HH/M-tok)" fmt=num2/>
</DataTable>

## Финансовое здоровье (Gitman & Startup)

<DataTable data={proj}>
  <Column id=vrt_por_ktoken title="VRT/kT (R$/1k)" fmt='$#,##0.0000'/>
  <Column id=burn_rate_ia title="Burn Rate ИИ (R$)" fmt='$#,##0.00'/>
  <Column id=kpi_icca title="ICCA (x)" fmt=num2/>
  <Column id=kpi_ibmt title="IBMT (x)" fmt=num3/>
</DataTable>

## Парето сбоев этого проекта

<BarChart data={falhas_proj} x=categoria_falha y=quantidade title="Сбои по категориям" swapXY=true/>

## 🪙 Возмещение затрат (VRT) — 5 блоков + среднее
<DataTable data={proj}>
  <Column id=vrt_50t title="50 tok" fmt='#,##0.00000'/>
  <Column id=vrt_100t title="100 tok" fmt='#,##0.00000'/>
  <Column id=vrt_250t title="250 tok" fmt='#,##0.00000'/>
  <Column id=vrt_500t title="500 tok" fmt='#,##0.00000'/>
  <Column id=vrt_por_ktoken title="1.000 tok" fmt='#,##0.00000'/>
  <Column id=vrt_media_blocos title="СРЕДН." fmt='#,##0.00000'/>
</DataTable>

## ⏰ Критический час прерываний (BRT)
<BarChart data={hora_proj} x=hora_brt y=interrupcoes title="Прерывания по часам (BRT)" xAxisTitle="Час (0-23)"/>

## ♻️ Таксономия потерь (Lean Six Sigma)
<BarChart data={waste_proj} x=categoria_waste y=waste_tokens title="Потери по категориям (взвеш. токены)" swapXY=true labels=true/>

## 🔬 RCA — галлюцинации по типу промпта (что задерживает этот проект)
<BarChart data={aluc_proj} x=prompt_categoria y=alucinacoes title="Галлюцинации по типу промпта" swapXY=true labels=true sort=true/>

<DataTable data={aluc_proj}>
  <Column id=prompt_categoria title="Тип промпта"/>
  <Column id=alucinacoes title="Галлюцинации" fmt=num0/>
  <Column id=taxa_aluc title="Доля %" fmt=num1/>
</DataTable>

---

# 📌 Итог — заключительный диагноз и окончательное решение
_Стандарт непрерывного улучшения — канонический источник: `foundations/solucoes_relatorios.md`._

## a) Разбор потерь (Lean Six Sigma)
{#if waste_proj.length > 0}
**Доминирующая потеря** этого проекта — **{waste_proj[0].categoria_waste}**, дающая **{waste_proj[0].pct_do_projeto}%** взвешенных потерь. Она тратит токены/деньги без прогресса и **толкает CPP вверх**. Окончательное решение и прочие категории — в таблице (применять по влиянию):

<DataTable data={waste_proj}>
  <Column id=categoria_waste title="Обнаруженная потеря"/>
  <Column id=waste_tokens title="Потрач. токены" fmt=num0/>
  <Column id=pct_do_projeto title="% потерь" fmt=num1/>
  <Column id=solucao title="🛠️ Окончательное решение (PDCA)" wrap=true/>
</DataTable>
{:else}
✅ Значимых потерь за период не зафиксировано.
{/if}

## b) Разбор галлюцинаций промптов (RCA по таксономии)
{#if aluc_proj.length > 0}
**Тип промпта, сильнее всего задерживающий** проект — **{aluc_proj[0].prompt_categoria}**, с **{aluc_proj[0].taxa_aluc}%** галлюцинаций — **корневое узкое место**. Каждая категория и её окончательная контрмера:

<DataTable data={aluc_proj}>
  <Column id=prompt_categoria title="Тип промпта"/>
  <Column id=alucinacoes title="Галлюцинации" fmt=num0/>
  <Column id=taxa_aluc title="Доля %" fmt=num1/>
  <Column id=solucao title="🛠️ Окончательное решение (RCA)" wrap=true/>
</DataTable>
{:else}
✅ Галлюцинаций за период нет — узких мест не обнаружено.
{/if}

## c) Непрерывное улучшение (PDCA / Kaizen)
1. **Plan** — сначала атаковать доминирующую потерю и узкое место выше.
2. **Do** — применить окончательные решения из таблиц.
3. **Check** — на следующей неделе измерить: IITA, IDLS, IOLI, ITR и задержку.
4. **Act** — закрепить сработавшее в system prompt/пайплайне и повторить.

> **Ориентир:** **снижение CPP** неделя за неделей. Каждое сокращение потерь и галлюцинаций снижает CPP.
