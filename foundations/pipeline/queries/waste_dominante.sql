-- WASTE DOMINANTE por projeto (categoria Lean com maior token-desperdício ponderado).
WITH w AS (
  SELECT project_name,
    CASE
      WHEN tipo_erro = 'RATE_LIMIT'                    THEN 'Espera - Cota/429'
      WHEN tipo_erro = 'ALUCINACAO_CODIGO'             THEN 'Defeito - Alucinacao'
      WHEN (prompt_tokens+completion_tokens) > 15000   THEN 'Superprocessamento - Prompt Inflado'
      WHEN latency_seconds > 3.0                       THEN 'Espera - Latencia Alta'
    END AS categoria_waste,
    CASE
      WHEN tipo_erro = 'RATE_LIMIT'                    THEN (prompt_tokens+completion_tokens) * 1.5
      WHEN tipo_erro = 'ALUCINACAO_CODIGO'             THEN (prompt_tokens+completion_tokens) * 2.0
      WHEN (prompt_tokens+completion_tokens) > 15000   THEN (prompt_tokens+completion_tokens) * 1.0
      WHEN latency_seconds > 3.0                       THEN (prompt_tokens+completion_tokens) * 0.5
    END AS waste_tokens
  FROM logs_langfuse
),
agg AS (SELECT project_name, categoria_waste, SUM(waste_tokens) AS wt
        FROM w WHERE categoria_waste IS NOT NULL GROUP BY project_name, categoria_waste),
mx AS (SELECT project_name, MAX(wt) AS pico FROM agg GROUP BY project_name)
SELECT a.project_name, a.categoria_waste AS waste_dominante, ROUND(a.wt,0) AS waste_tokens
FROM agg a JOIN mx ON a.project_name=mx.project_name AND a.wt=mx.pico
ORDER BY waste_tokens DESC;
