-- Últimos alertas críticos (triagem no topo do dashboard).
SELECT
    project_name,
    tipo_erro,
    prompt_truncado,
    resposta_truncada,
    tokens_desperdicados,
    data_evento
FROM alertas_criticos
ORDER BY data_evento DESC
LIMIT 10;
