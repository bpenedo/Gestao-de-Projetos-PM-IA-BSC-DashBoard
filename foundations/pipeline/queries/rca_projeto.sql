-- RCA por projeto: o TIPO DE PROMPT que mais alucina (gargalo que atrasa cada projeto).
WITH ac AS (
  SELECT project_name, prompt_categoria,
    SUM(CASE WHEN tipo_erro='ALUCINACAO_CODIGO' THEN 1 ELSE 0 END) AS aluc
  FROM logs_langfuse GROUP BY project_name, prompt_categoria
),
mx AS (SELECT project_name, MAX(aluc) AS top FROM ac GROUP BY project_name)
SELECT ac.project_name,
       MIN(ac.prompt_categoria) AS prompt_gargalo,
       mx.top                   AS alucinacoes
FROM ac JOIN mx ON ac.project_name=mx.project_name AND ac.aluc=mx.top
WHERE mx.top > 0
GROUP BY ac.project_name, mx.top
ORDER BY alucinacoes DESC;
