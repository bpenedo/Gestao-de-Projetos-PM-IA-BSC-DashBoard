---
title: "项目：{params.projeto}"
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
select CASE categoria_waste WHEN 'Defeito (Defects) - Alucinacao/Retrabalho' THEN '缺陷 - 幻觉/返工' WHEN 'Defeito - Alucinacao' THEN '缺陷 - 幻觉' WHEN 'Espera (Waiting) - Cota/429' THEN '等待 - 配额/429' WHEN 'Espera - Cota/429' THEN '等待 - 配额/429' WHEN 'Espera (Waiting) - Latencia Alta' THEN '等待 - 高延迟' WHEN 'Espera - Latencia Alta' THEN '等待 - 高延迟' WHEN 'Superprocessamento - Prompt Inflado' THEN '过度处理 - 提示词膨胀' ELSE categoria_waste END as categoria_waste, waste_tokens, pct_do_projeto, CASE solucao WHEN 'Fila com backoff + fallback por cota + upgrade de Tier (meta IOLI abaixo de 1%)' THEN '队列+退避 + 配额回退 + 升级 Tier（目标 IOLI < 1%）' WHEN 'System prompt rigido + saida JSON + validacao LLM-as-judge (meta IITA abaixo de 10%)' THEN '严格 system prompt + JSON 输出 + LLM-as-judge 校验（目标 IITA < 10%）' WHEN 'RAG/embeddings + sumarizacao + poda de historico (meta ITR estavel ou em queda)' THEN 'RAG/嵌入 + 摘要 + 历史裁剪（目标 ITR 稳定或下降）' WHEN 'Streaming/TTFT + modelo rapido + cache (meta latencia abaixo de 3s)' THEN '流式/TTFT + 快速模型 + 缓存（目标延迟 < 3s）' WHEN 'Converter aberto em estruturado: system prompt restritivo + few-shot + guardrails de escopo' THEN '将开放转为结构化：限制性 system prompt + few-shot + 范围护栏' WHEN 'Few-shot valido + exigir testes + validacao de sintaxe/execucao + RAG das docs da lib' THEN '有效 few-shot + 要求测试 + 语法/执行校验 + 库文档 RAG' WHEN 'Decomposicao em etapas + verificacao por etapa + self-consistency' THEN '分步分解 + 逐步验证 + self-consistency' WHEN 'JSON mode/schema + regex de validacao + exemplos entrada-saida' THEN 'JSON mode/schema + 校验正则 + 输入-输出示例' WHEN 'Melhorar retrieval (re-rank) + citar fontes + grounding obrigatorio' THEN '改进检索（re-rank）+ 引用来源 + 强制 grounding' WHEN 'Templates fixos + exemplos de saida + JSON mode' THEN '固定模板 + 输出示例 + JSON mode' WHEN 'Limites de tamanho + instrucoes de fidelidade + QA factual' THEN '大小限制 + 保真指令 + 事实性 QA' ELSE solucao END as solucao from bsc.wastes_lean where project_name = '${params.projeto}' order by waste_tokens desc
```

```sql aluc_proj
select CASE prompt_categoria WHEN 'Conversa/Aberto' THEN '对话/开放' WHEN 'RAG/Busca' THEN 'RAG/检索' WHEN 'Transformacao/Formato' THEN '转换/格式' WHEN 'Raciocinio/Analise' THEN '推理/分析' WHEN 'Sumarizacao' THEN '摘要' WHEN 'Geracao de Codigo' THEN '代码生成' WHEN 'Extracao de Dados' THEN '数据提取' ELSE prompt_categoria END as prompt_categoria, alucinacoes, taxa_aluc, CASE solucao WHEN 'Fila com backoff + fallback por cota + upgrade de Tier (meta IOLI abaixo de 1%)' THEN '队列+退避 + 配额回退 + 升级 Tier（目标 IOLI < 1%）' WHEN 'System prompt rigido + saida JSON + validacao LLM-as-judge (meta IITA abaixo de 10%)' THEN '严格 system prompt + JSON 输出 + LLM-as-judge 校验（目标 IITA < 10%）' WHEN 'RAG/embeddings + sumarizacao + poda de historico (meta ITR estavel ou em queda)' THEN 'RAG/嵌入 + 摘要 + 历史裁剪（目标 ITR 稳定或下降）' WHEN 'Streaming/TTFT + modelo rapido + cache (meta latencia abaixo de 3s)' THEN '流式/TTFT + 快速模型 + 缓存（目标延迟 < 3s）' WHEN 'Converter aberto em estruturado: system prompt restritivo + few-shot + guardrails de escopo' THEN '将开放转为结构化：限制性 system prompt + few-shot + 范围护栏' WHEN 'Few-shot valido + exigir testes + validacao de sintaxe/execucao + RAG das docs da lib' THEN '有效 few-shot + 要求测试 + 语法/执行校验 + 库文档 RAG' WHEN 'Decomposicao em etapas + verificacao por etapa + self-consistency' THEN '分步分解 + 逐步验证 + self-consistency' WHEN 'JSON mode/schema + regex de validacao + exemplos entrada-saida' THEN 'JSON mode/schema + 校验正则 + 输入-输出示例' WHEN 'Melhorar retrieval (re-rank) + citar fontes + grounding obrigatorio' THEN '改进检索（re-rank）+ 引用来源 + 强制 grounding' WHEN 'Templates fixos + exemplos de saida + JSON mode' THEN '固定模板 + 输出示例 + JSON mode' WHEN 'Limites de tamanho + instrucoes de fidelidade + QA factual' THEN '大小限制 + 保真指令 + 事实性 QA' ELSE solucao END as solucao from bsc.alucinacao_categoria where project_name = '${params.projeto}' and alucinacoes > 0 order by alucinacoes desc
```

# 🛠️ {params.projeto}

<BigValue data={proj} value=kpi_psr title="PSR (0-5)" fmt=num2/>
<BigValue data={proj} value=kpi_peuc title="PEUC (%)" fmt=num1/>
<BigValue data={proj} value=total_tokens title="Tokens" fmt=num0/>
<BigValue data={proj} value=kpi_cpp title="CPP (R$/%)" fmt='$#,##0.00'/>

## 效率诊断

<DataTable data={proj}>
  <Column id=kpi_iita title="IITA %（幻觉）" fmt=num1/>
  <Column id=kpi_idls_lean title="IDLS %（精益浪费）" fmt=num1/>
  <Column id=kpi_ioli title="IOLI %（空闲）" fmt=num1/>
  <Column id=kpi_itr title="ITR (tok/req)" fmt=num0/>
  <Column id=kpi_ieet_hh_por_mtoken title="IEET (HH/M-tok)" fmt=num2/>
</DataTable>

## 财务健康（Gitman & Startup）

<DataTable data={proj}>
  <Column id=vrt_por_ktoken title="VRT/kT (R$/1k)" fmt='$#,##0.0000'/>
  <Column id=burn_rate_ia title="AI 消耗率 (R$)" fmt='$#,##0.00'/>
  <Column id=kpi_icca title="ICCA (x)" fmt=num2/>
  <Column id=kpi_ibmt title="IBMT (x)" fmt=num3/>
</DataTable>

## 本项目故障帕累托

<BarChart data={falhas_proj} x=categoria_falha y=quantidade title="各类别故障" swapXY=true/>

## 🪙 成本回收 (VRT) — 5 分块 + 平均
<DataTable data={proj}>
  <Column id=vrt_50t title="50 tok" fmt='#,##0.00000'/>
  <Column id=vrt_100t title="100 tok" fmt='#,##0.00000'/>
  <Column id=vrt_250t title="250 tok" fmt='#,##0.00000'/>
  <Column id=vrt_500t title="500 tok" fmt='#,##0.00000'/>
  <Column id=vrt_por_ktoken title="1.000 tok" fmt='#,##0.00000'/>
  <Column id=vrt_media_blocos title="平均" fmt='#,##0.00000'/>
</DataTable>

## ⏰ 关键中断时段 (BRT)
<BarChart data={hora_proj} x=hora_brt y=interrupcoes title="按小时的中断 (BRT)" xAxisTitle="小时 (0-23)"/>

## ♻️ 浪费分类 (Lean Six Sigma)
<BarChart data={waste_proj} x=categoria_waste y=waste_tokens title="各类别浪费（加权 Token）" swapXY=true labels=true/>

## 🔬 RCA — 按提示词类型的幻觉（是什么在拖慢本项目）
<BarChart data={aluc_proj} x=prompt_categoria y=alucinacoes title="按提示词类型的幻觉" swapXY=true labels=true sort=true/>

<DataTable data={aluc_proj}>
  <Column id=prompt_categoria title="提示词类型"/>
  <Column id=alucinacoes title="幻觉数" fmt=num0/>
  <Column id=taxa_aluc title="比率 %" fmt=num1/>
</DataTable>

---

# 📌 结论 — 结论性诊断与最终解决方案
_持续改进标准 — 规范来源：`foundations/solucoes_relatorios.md`。_

## a) 浪费论述 (Lean Six Sigma)
{#if waste_proj.length > 0}
本项目的**主要浪费**是 **{waste_proj[0].categoria_waste}**，占加权浪费的 **{waste_proj[0].pct_do_projeto}%**。它消耗 Token/现金却不推进进度，从而**推高 CPP**。最终解决方案与其他类别见下表（按影响顺序处理）：

<DataTable data={waste_proj}>
  <Column id=categoria_waste title="检测到的浪费"/>
  <Column id=waste_tokens title="浪费的 Token" fmt=num0/>
  <Column id=pct_do_projeto title="浪费占比" fmt=num1/>
  <Column id=solucao title="🛠️ 最终解决方案 (PDCA)" wrap=true/>
</DataTable>
{:else}
✅ 本期未记录相关浪费。
{/if}

## b) 提示词幻觉论述（按分类 RCA）
{#if aluc_proj.length > 0}
最拖慢本项目的**提示词类型**是 **{aluc_proj[0].prompt_categoria}**，幻觉率 **{aluc_proj[0].taxa_aluc}%** — 交付的**根本瓶颈**。每个有幻觉的类别及其最终对策：

<DataTable data={aluc_proj}>
  <Column id=prompt_categoria title="提示词类型"/>
  <Column id=alucinacoes title="幻觉数" fmt=num0/>
  <Column id=taxa_aluc title="比率 %" fmt=num1/>
  <Column id=solucao title="🛠️ 最终解决方案 (RCA)" wrap=true/>
</DataTable>
{:else}
✅ 本期未记录幻觉 — 未检测到提示词瓶颈。
{/if}

## c) 持续改进（PDCA / Kaizen）
1. **Plan** — 先攻克上面指出的主要浪费与提示词瓶颈。
2. **Do** — 应用表中的最终解决方案。
3. **Check** — 下周测量：IITA、IDLS、IOLI、ITR 与延迟。
4. **Act** — 将有效做法固化到 system prompt/流水线并循环。

> **北极星：** **CPP 逐周下降**。每减少一处浪费与幻觉都压低 CPP。
