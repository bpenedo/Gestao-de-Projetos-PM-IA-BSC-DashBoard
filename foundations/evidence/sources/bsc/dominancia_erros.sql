-- Pareto (80/20): dominância das categorias de falha por projeto on-going.
WITH falhas_mapeadas AS (
    SELECT
        project_name,
        CASE
            WHEN tipo_erro = 'RATE_LIMIT'                       THEN 'Erro de Cota (429)'
            WHEN tipo_erro = 'ALUCINACAO_CODIGO'               THEN 'Alucinacao / Retrabalho'
            WHEN (prompt_tokens + completion_tokens) > 15000   THEN 'Alto Custo (Prompt Inflado)'
            WHEN latency_seconds > 3.0                          THEN 'Latencia Alta (> 3s)'
            ELSE 'Outros'
        END AS categoria_falha,
        COUNT(*) AS quantidade
    FROM logs_langfuse
    WHERE tipo_erro <> 'NENHUM' OR latency_seconds > 3.0 OR (prompt_tokens + completion_tokens) > 15000
    GROUP BY project_name, categoria_falha
)
SELECT
    project_name,
    categoria_falha,
    quantidade,
    ROUND(quantidade * 100.0 / SUM(quantidade) OVER (PARTITION BY project_name), 1) AS percentual_dominancia
FROM falhas_mapeadas
ORDER BY project_name, quantidade DESC;
