-- Mix global de falhas (para donut). Cada log cai em UMA categoria (1ª que casar).
SELECT categoria, COUNT(*) AS qtd FROM (
  SELECT CASE
    WHEN tipo_erro='RATE_LIMIT'                     THEN 'Erro de Cota (429)'
    WHEN tipo_erro='ALUCINACAO_CODIGO'              THEN 'Alucinacao / Retrabalho'
    WHEN latency_seconds > 3.0                      THEN 'Latencia Alta (>3s)'
    WHEN (prompt_tokens+completion_tokens) > 15000  THEN 'Alto Custo (Prompt Inflado)'
    ELSE 'OK'
  END AS categoria
  FROM logs_langfuse
)
WHERE categoria <> 'OK'
GROUP BY categoria
ORDER BY qtd DESC;
