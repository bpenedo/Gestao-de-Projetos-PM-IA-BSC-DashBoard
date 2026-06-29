-- Horário Crítico de Impacto (HCI): a hora (BRT) de pico de interrupções por projeto.
WITH h AS (
  SELECT project_name,
         ((CAST(substr(updated_at,12,2) AS INTEGER) + 21) % 24) AS hora_brt,
         COUNT(*) AS n
  FROM logs_langfuse WHERE tipo_erro <> 'NENHUM'
  GROUP BY project_name, hora_brt
),
mx AS (SELECT project_name, MAX(n) AS pico FROM h GROUP BY project_name)
SELECT h.project_name,
       MIN(h.hora_brt)  AS hora_pico,
       mx.pico          AS interrupcoes_pico
FROM h JOIN mx ON h.project_name = mx.project_name AND h.n = mx.pico
GROUP BY h.project_name, mx.pico
ORDER BY interrupcoes_pico DESC;
