-- Planos de assinatura com custo total mensal em R$ (câmbio + IOF).
SELECT provedor, plano, usd_mes,
       ROUND(usd_mes*cambio, 2)                       AS r_base,
       ROUND(usd_mes*cambio*iof_pct/100.0, 2)         AS iof_reais,
       ROUND(usd_mes*cambio*(1+iof_pct/100.0), 2)     AS total_iof
FROM planos_assinatura
ORDER BY total_iof DESC;
