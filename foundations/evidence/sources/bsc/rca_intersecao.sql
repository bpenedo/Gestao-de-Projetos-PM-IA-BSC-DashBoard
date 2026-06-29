-- INTERSEÇÃO: qual TIPO DE PROMPT é o gargalo #1 de alucinação no MAIOR número de projetos
-- (o que atrasa COMUMENTE a todos). pct_portfolio = % dos projetos em que é o gargalo principal.
WITH ac AS (
  SELECT project_name, prompt_categoria,
    SUM(CASE WHEN tipo_erro='ALUCINACAO_CODIGO' THEN 1 ELSE 0 END) AS aluc
  FROM logs_langfuse GROUP BY project_name, prompt_categoria
),
mx AS (SELECT project_name, MAX(aluc) AS top FROM ac GROUP BY project_name),
top1 AS (
  SELECT ac.project_name, ac.prompt_categoria
  FROM ac JOIN mx ON ac.project_name=mx.project_name AND ac.aluc=mx.top AND ac.aluc>0
)
SELECT prompt_categoria,
       COUNT(*) AS projetos_onde_e_top1,
       ROUND(COUNT(*)*100.0/(SELECT COUNT(DISTINCT project_name) FROM logs_langfuse),1) AS pct_portfolio,
       (SELECT SUM(CASE WHEN l.tipo_erro='ALUCINACAO_CODIGO' THEN 1 ELSE 0 END)
        FROM logs_langfuse l WHERE l.prompt_categoria = top1.prompt_categoria) AS alucinacoes_totais
FROM top1
GROUP BY prompt_categoria
ORDER BY projetos_onde_e_top1 DESC, alucinacoes_totais DESC;
