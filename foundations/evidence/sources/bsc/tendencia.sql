-- Tendência semanal do portfólio (CPP/PSR/burn) a partir dos snapshots.
SELECT data_snapshot,
       ROUND(AVG(cpp),2)          AS cpp_medio,
       ROUND(AVG(psr),2)          AS psr_medio,
       ROUND(SUM(burn_rate_ia),2) AS burn_total
FROM kpi_snapshots
GROUP BY data_snapshot
ORDER BY data_snapshot;
