-- Taxonomia de WASTES (Lean Six Sigma) por projeto + SOLUÇÃO DEFINITIVA (padrão solucoes_relatorios.md).
SELECT
  project_name, categoria_waste,
  COUNT(*)          AS ocorrencias,
  SUM(waste_tokens) AS waste_tokens,
  ROUND(SUM(waste_tokens)*100.0/SUM(SUM(waste_tokens)) OVER (PARTITION BY project_name),1) AS pct_do_projeto,
  CASE categoria_waste
    WHEN 'Espera (Waiting) - Cota/429'              THEN 'Fila com backoff + fallback por cota + upgrade de Tier (meta IOLI abaixo de 1%)'
    WHEN 'Defeito (Defects) - Alucinacao/Retrabalho' THEN 'System prompt rigido + saida JSON + validacao LLM-as-judge (meta IITA abaixo de 10%)'
    WHEN 'Superprocessamento - Prompt Inflado'      THEN 'RAG/embeddings + sumarizacao + poda de historico (meta ITR estavel ou em queda)'
    WHEN 'Espera (Waiting) - Latencia Alta'         THEN 'Streaming/TTFT + modelo rapido + cache (meta latencia abaixo de 3s)'
  END AS solucao
FROM (
  SELECT project_name,
    CASE
      WHEN tipo_erro='RATE_LIMIT'                   THEN 'Espera (Waiting) - Cota/429'
      WHEN tipo_erro='ALUCINACAO_CODIGO'            THEN 'Defeito (Defects) - Alucinacao/Retrabalho'
      WHEN (prompt_tokens+completion_tokens)>15000  THEN 'Superprocessamento - Prompt Inflado'
      WHEN latency_seconds>3.0                      THEN 'Espera (Waiting) - Latencia Alta'
    END AS categoria_waste,
    CASE
      WHEN tipo_erro='RATE_LIMIT'                   THEN (prompt_tokens+completion_tokens)*1.5
      WHEN tipo_erro='ALUCINACAO_CODIGO'            THEN (prompt_tokens+completion_tokens)*2.0
      WHEN (prompt_tokens+completion_tokens)>15000  THEN (prompt_tokens+completion_tokens)*1.0
      WHEN latency_seconds>3.0                      THEN (prompt_tokens+completion_tokens)*0.5
    END AS waste_tokens
  FROM logs_langfuse
)
WHERE categoria_waste IS NOT NULL
GROUP BY project_name, categoria_waste
ORDER BY project_name, waste_tokens DESC;
