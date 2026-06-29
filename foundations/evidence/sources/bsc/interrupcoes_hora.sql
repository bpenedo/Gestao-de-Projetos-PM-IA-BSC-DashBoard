-- Interrupções (falhas) por projeto e HORA do dia (BRT = UTC-3) — base do heatmap/critico.
SELECT
  project_name,
  ((CAST(substr(updated_at,12,2) AS INTEGER) + 21) % 24) AS hora_brt,
  COUNT(*) AS interrupcoes
FROM logs_langfuse
WHERE tipo_erro <> 'NENHUM'
GROUP BY project_name, hora_brt
ORDER BY project_name, hora_brt;
