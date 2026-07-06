---
title: "프로젝트: {params.projeto}"
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
select CASE categoria_waste WHEN 'Defeito (Defects) - Alucinacao/Retrabalho' THEN '결함 - 환각/재작업' WHEN 'Defeito - Alucinacao' THEN '결함 - 환각' WHEN 'Espera (Waiting) - Cota/429' THEN '대기 - 쿼터/429' WHEN 'Espera - Cota/429' THEN '대기 - 쿼터/429' WHEN 'Espera (Waiting) - Latencia Alta' THEN '대기 - 높은 지연' WHEN 'Espera - Latencia Alta' THEN '대기 - 높은 지연' WHEN 'Superprocessamento - Prompt Inflado' THEN '과처리 - 부풀린 프롬프트' ELSE categoria_waste END as categoria_waste, waste_tokens, pct_do_projeto, CASE solucao WHEN 'Fila com backoff + fallback por cota + upgrade de Tier (meta IOLI abaixo de 1%)' THEN '큐+백오프 + 쿼터 폴백 + Tier 업그레이드(목표 IOLI 1% 미만)' WHEN 'System prompt rigido + saida JSON + validacao LLM-as-judge (meta IITA abaixo de 10%)' THEN '엄격한 시스템 프롬프트 + JSON 출력 + LLM-as-judge 검증(목표 IITA 10% 미만)' WHEN 'RAG/embeddings + sumarizacao + poda de historico (meta ITR estavel ou em queda)' THEN 'RAG/임베딩 + 요약 + 히스토리 가지치기(목표 ITR 안정/하락)' WHEN 'Streaming/TTFT + modelo rapido + cache (meta latencia abaixo de 3s)' THEN '스트리밍/TTFT + 빠른 모델 + 캐시(목표 지연 3s 미만)' WHEN 'Converter aberto em estruturado: system prompt restritivo + few-shot + guardrails de escopo' THEN '개방형을 구조화로: 제한적 시스템 프롬프트 + few-shot + 범위 가드레일' WHEN 'Few-shot valido + exigir testes + validacao de sintaxe/execucao + RAG das docs da lib' THEN '유효 few-shot + 테스트 요구 + 구문/실행 검증 + 라이브러리 문서 RAG' WHEN 'Decomposicao em etapas + verificacao por etapa + self-consistency' THEN '단계 분해 + 단계별 검증 + self-consistency' WHEN 'JSON mode/schema + regex de validacao + exemplos entrada-saida' THEN 'JSON mode/schema + 검증 regex + 입출력 예시' WHEN 'Melhorar retrieval (re-rank) + citar fontes + grounding obrigatorio' THEN '검색 개선(re-rank) + 출처 인용 + 필수 grounding' WHEN 'Templates fixos + exemplos de saida + JSON mode' THEN '고정 템플릿 + 출력 예시 + JSON mode' WHEN 'Limites de tamanho + instrucoes de fidelidade + QA factual' THEN '크기 제한 + 충실성 지침 + 사실 QA' ELSE solucao END as solucao from bsc.wastes_lean where project_name = '${params.projeto}' order by waste_tokens desc
```

```sql aluc_proj
select CASE prompt_categoria WHEN 'Conversa/Aberto' THEN '대화/개방' WHEN 'RAG/Busca' THEN 'RAG/검색' WHEN 'Transformacao/Formato' THEN '변환/형식' WHEN 'Raciocinio/Analise' THEN '추론/분석' WHEN 'Sumarizacao' THEN '요약' WHEN 'Geracao de Codigo' THEN '코드 생성' WHEN 'Extracao de Dados' THEN '데이터 추출' ELSE prompt_categoria END as prompt_categoria, alucinacoes, taxa_aluc, CASE solucao WHEN 'Fila com backoff + fallback por cota + upgrade de Tier (meta IOLI abaixo de 1%)' THEN '큐+백오프 + 쿼터 폴백 + Tier 업그레이드(목표 IOLI 1% 미만)' WHEN 'System prompt rigido + saida JSON + validacao LLM-as-judge (meta IITA abaixo de 10%)' THEN '엄격한 시스템 프롬프트 + JSON 출력 + LLM-as-judge 검증(목표 IITA 10% 미만)' WHEN 'RAG/embeddings + sumarizacao + poda de historico (meta ITR estavel ou em queda)' THEN 'RAG/임베딩 + 요약 + 히스토리 가지치기(목표 ITR 안정/하락)' WHEN 'Streaming/TTFT + modelo rapido + cache (meta latencia abaixo de 3s)' THEN '스트리밍/TTFT + 빠른 모델 + 캐시(목표 지연 3s 미만)' WHEN 'Converter aberto em estruturado: system prompt restritivo + few-shot + guardrails de escopo' THEN '개방형을 구조화로: 제한적 시스템 프롬프트 + few-shot + 범위 가드레일' WHEN 'Few-shot valido + exigir testes + validacao de sintaxe/execucao + RAG das docs da lib' THEN '유효 few-shot + 테스트 요구 + 구문/실행 검증 + 라이브러리 문서 RAG' WHEN 'Decomposicao em etapas + verificacao por etapa + self-consistency' THEN '단계 분해 + 단계별 검증 + self-consistency' WHEN 'JSON mode/schema + regex de validacao + exemplos entrada-saida' THEN 'JSON mode/schema + 검증 regex + 입출력 예시' WHEN 'Melhorar retrieval (re-rank) + citar fontes + grounding obrigatorio' THEN '검색 개선(re-rank) + 출처 인용 + 필수 grounding' WHEN 'Templates fixos + exemplos de saida + JSON mode' THEN '고정 템플릿 + 출력 예시 + JSON mode' WHEN 'Limites de tamanho + instrucoes de fidelidade + QA factual' THEN '크기 제한 + 충실성 지침 + 사실 QA' ELSE solucao END as solucao from bsc.alucinacao_categoria where project_name = '${params.projeto}' and alucinacoes > 0 order by alucinacoes desc
```

# 🛠️ {params.projeto}

<BigValue data={proj} value=kpi_psr title="PSR (0-5)" fmt=num2/>
<BigValue data={proj} value=kpi_peuc title="PEUC (%)" fmt=num1/>
<BigValue data={proj} value=total_tokens title="Tokens" fmt=num0/>
<BigValue data={proj} value=kpi_cpp title="CPP (R$/%)" fmt='$#,##0.00'/>

## 효율 진단

<DataTable data={proj}>
  <Column id=kpi_iita title="IITA % (환각)" fmt=num1/>
  <Column id=kpi_idls_lean title="IDLS % (린 낭비)" fmt=num1/>
  <Column id=kpi_ioli title="IOLI % (유휴)" fmt=num1/>
  <Column id=kpi_itr title="ITR (tok/req)" fmt=num0/>
  <Column id=kpi_ieet_hh_por_mtoken title="IEET (HH/M-tok)" fmt=num2/>
</DataTable>

## 재무 건전성 (Gitman & Startup)

<DataTable data={proj}>
  <Column id=vrt_por_ktoken title="VRT/kT (R$/1k)" fmt='$#,##0.0000'/>
  <Column id=burn_rate_ia title="AI Burn Rate (R$)" fmt='$#,##0.00'/>
  <Column id=kpi_icca title="ICCA (x)" fmt=num2/>
  <Column id=kpi_ibmt title="IBMT (x)" fmt=num3/>
</DataTable>

## 이 프로젝트의 실패 파레토

<BarChart data={falhas_proj} x=categoria_falha y=quantidade title="카테고리별 실패" swapXY=true/>

## 🪙 비용 회수 (VRT) — 5블록 + 평균
<DataTable data={proj}>
  <Column id=vrt_50t title="50 tok" fmt='#,##0.00000'/>
  <Column id=vrt_100t title="100 tok" fmt='#,##0.00000'/>
  <Column id=vrt_250t title="250 tok" fmt='#,##0.00000'/>
  <Column id=vrt_500t title="500 tok" fmt='#,##0.00000'/>
  <Column id=vrt_por_ktoken title="1.000 tok" fmt='#,##0.00000'/>
  <Column id=vrt_media_blocos title="평균" fmt='#,##0.00000'/>
</DataTable>

## ⏰ 핵심 중단 시간대 (BRT)
<BarChart data={hora_proj} x=hora_brt y=interrupcoes title="시간대별 중단 (BRT)" xAxisTitle="시간 (0-23)"/>

## ♻️ 낭비 분류 (Lean Six Sigma)
<BarChart data={waste_proj} x=categoria_waste y=waste_tokens title="카테고리별 낭비(가중 토큰)" swapXY=true labels=true/>

## 🔬 RCA — 프롬프트 유형별 환각 (이 프로젝트를 지연시키는 요인)
<BarChart data={aluc_proj} x=prompt_categoria y=alucinacoes title="프롬프트 유형별 환각" swapXY=true labels=true sort=true/>

<DataTable data={aluc_proj}>
  <Column id=prompt_categoria title="프롬프트 유형"/>
  <Column id=alucinacoes title="환각 수" fmt=num0/>
  <Column id=taxa_aluc title="비율 %" fmt=num1/>
</DataTable>

---

# 📌 결론 — 종합 진단 및 확정 해법
_지속적 개선 표준 — 정식 출처: `foundations/solucoes_relatorios.md`._

## a) 낭비 논술 (Lean Six Sigma)
{#if waste_proj.length > 0}
이 프로젝트의 **주요 낭비**는 **{waste_proj[0].categoria_waste}**로, 가중 낭비의 **{waste_proj[0].pct_do_projeto}%**. 진척 없이 토큰/현금을 소모해 **CPP를 끌어올림**. 확정 해법과 나머지 카테고리는 아래 표에(영향 순으로 적용):

<DataTable data={waste_proj}>
  <Column id=categoria_waste title="검출된 낭비"/>
  <Column id=waste_tokens title="낭비 토큰" fmt=num0/>
  <Column id=pct_do_projeto title="낭비 %" fmt=num1/>
  <Column id=solucao title="🛠️ 확정 해법 (PDCA)" wrap=true/>
</DataTable>
{:else}
✅ 이 기간 관련 낭비 없음.
{/if}

## b) 프롬프트 환각 논술 (분류별 RCA)
{#if aluc_proj.length > 0}
이 프로젝트를 가장 지연시키는 **프롬프트 유형**은 **{aluc_proj[0].prompt_categoria}**(환각 **{aluc_proj[0].taxa_aluc}%**) — 납품의 **근본 병목**. 환각이 검출된 각 카테고리와 확정 대책:

<DataTable data={aluc_proj}>
  <Column id=prompt_categoria title="프롬프트 유형"/>
  <Column id=alucinacoes title="환각 수" fmt=num0/>
  <Column id=taxa_aluc title="비율 %" fmt=num1/>
  <Column id=solucao title="🛠️ 확정 해법 (RCA)" wrap=true/>
</DataTable>
{:else}
✅ 이 기간 환각 없음 — 프롬프트 병목 미검출.
{/if}

## c) 지속적 개선 (PDCA / Kaizen)
1. **Plan** — 위의 주요 낭비와 프롬프트 병목을 먼저 공략.
2. **Do** — 표의 확정 해법 적용.
3. **Check** — 다음 주 측정: IITA, IDLS, IOLI, ITR, 지연.
4. **Act** — 효과 있던 것을 시스템 프롬프트/파이프라인에 표준화하고 반복.

> **북극성:** 주마다 **CPP 감소**. 낭비·환각을 줄일 때마다 CPP 하락.
