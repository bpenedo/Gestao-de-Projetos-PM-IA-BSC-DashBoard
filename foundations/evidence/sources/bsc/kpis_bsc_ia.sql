-- ============================================================================
-- Query MESTRA do BSC de Projetos de IA  (dialeto SQLite)
-- Calcula todos os KPIs por projeto: IITA, PEUC, ITR, IEET, IOLI, CDO, VRT/kT,
-- IDLS, ICCA, IBMT, Burn Rate, CPP e o PSR (Score 0-5).
-- Preço médio da API por 1k tokens parametrizado em 0.025 (ajuste conforme provider).
-- Framework "Gestão de Projetos (PM) IA com Painel BSC e DashBoard" · (c) Bruno Teixeira Penedo — 2026. Todos os direitos reservados. E-mail: bpenedo@gmail.com
-- ============================================================================
WITH sessao AS (
    -- Status por sessão: a sessão é útil se NÃO teve nenhuma falha.
    SELECT project_name, session_id,
           MAX(CASE WHEN tipo_erro <> 'NENHUM' THEN 1 ELSE 0 END) AS teve_falha
    FROM logs_langfuse
    GROUP BY project_name, session_id
),
sessao_agg AS (
    SELECT project_name,
           COUNT(*)                                       AS total_sessoes,
           SUM(CASE WHEN teve_falha = 0 THEN 1 ELSE 0 END) AS sessoes_uteis
    FROM sessao
    GROUP BY project_name
),
dados_ia AS (
    SELECT
        project_name,
        COUNT(DISTINCT session_id)                    AS total_sessoes,
        COUNT(id)                                     AS total_prompts,
        SUM(prompt_tokens + completion_tokens)        AS total_tokens,
        AVG(latency_seconds)                          AS latencia_media,
        SUM(CASE WHEN tipo_erro = 'RATE_LIMIT'        THEN (prompt_tokens + completion_tokens) * 1.5 ELSE 0 END) AS tokens_waste_cota,
        SUM(CASE WHEN tipo_erro = 'ALUCINACAO_CODIGO' THEN (prompt_tokens + completion_tokens) * 2.0 ELSE 0 END) AS tokens_waste_codigo,
        SUM(CASE WHEN tipo_erro <> 'NENHUM'           THEN (prompt_tokens + completion_tokens) ELSE 0 END)       AS tokens_desperdicados_brutos,
        SUM(CASE WHEN tipo_erro = 'NENHUM'            THEN 1 ELSE 0 END)                                         AS total_entregaveis_uteis,
        SUM(tempo_bloqueado_minutos)                  AS total_minutos_bloqueados
    FROM logs_langfuse
    GROUP BY project_name
),
custo_fixo AS (
    SELECT SUM(valor_mensal) AS total_rateio_infra FROM assinaturas_infra
),
total_horas_empresa AS (
    SELECT SUM(horas_trabalhadas) AS total_hh_geral FROM horas_desenvolvimento
)
SELECT
    q.*,
    -- 2ª ótica de consumo: VRT recalculado em 5 bases de bloco (R$ por N tokens) + média.
    ROUND(q.vrt_por_ktoken * 0.05, 5)                               AS vrt_50t,
    ROUND(q.vrt_por_ktoken * 0.10, 5)                               AS vrt_100t,
    ROUND(q.vrt_por_ktoken * 0.25, 5)                               AS vrt_250t,
    ROUND(q.vrt_por_ktoken * 0.50, 5)                               AS vrt_500t,
    ROUND(q.vrt_por_ktoken * (0.05 + 0.10 + 0.25 + 0.50 + 1.0) / 5.0, 5) AS vrt_media_blocos
FROM (
SELECT
    i.project_name,
    sa.total_sessoes,
    i.total_prompts,
    i.total_tokens,
    ROUND(i.latencia_media, 2)                                                                   AS latencia_media_s,
    h.horas_trabalhadas,
    h.faturamento_mrr_incremental                                                               AS mrr_incremental,

    -- Custo da hora do projeto (dev + rateio de infra distribuído pelas horas da empresa)
    ROUND(h.custo_hora_dev + (f.total_rateio_infra / NULLIF(t.total_hh_geral, 0)), 2)            AS custo_hora_projeto,

    -- IITA: Inflação de Tokens por Alucinação (%)
    ROUND(i.tokens_desperdicados_brutos * 100.0 / NULLIF(i.total_tokens, 0), 2)                  AS kpi_iita,

    -- PEUC: % de Entregáveis Úteis por Sessão (sessões sem nenhuma falha)
    ROUND(sa.sessoes_uteis * 100.0 / NULLIF(sa.total_sessoes, 0), 2)                             AS kpi_peuc,

    -- ITR: Intensidade de Tokens por Requisição
    ROUND(i.total_tokens * 1.0 / NULLIF(i.total_prompts, 0), 0)                                  AS kpi_itr,

    -- IEET: Horas-Homem por 1 Milhão de Tokens
    ROUND(h.horas_trabalhadas / NULLIF(i.total_tokens / 1000000.0, 0), 2)                        AS kpi_ieet_hh_por_mtoken,

    -- CDO: Custo do Desenvolvimento Ocioso (R$)
    ROUND(i.total_minutos_bloqueados * ((h.custo_hora_dev + (f.total_rateio_infra / NULLIF(t.total_hh_geral,0))) / 60.0), 2) AS kpi_cdo,

    -- IOLI: Índice de Ociosidade por Limite de IA (%)
    ROUND((i.total_minutos_bloqueados * ((h.custo_hora_dev + (f.total_rateio_infra / NULLIF(t.total_hh_geral,0))) / 60.0)) * 100.0
          / NULLIF(h.custo_total_desenvolvimento, 0), 2)                                         AS kpi_ioli,

    -- VRT/kT: Unidade de Recuperação Tokenizável (R$ por 1.000 tokens) = (preço_api + CRI) * FIA
    ROUND((0.025 + (f.total_rateio_infra / NULLIF(i.total_tokens / 1000.0, 0)))
          * (100.0 / NULLIF(100.0 - (i.tokens_desperdicados_brutos * 100.0 / NULLIF(i.total_tokens,0)), 0)), 5) AS vrt_por_ktoken,

    -- IDLS: Índice de Desperdício Lean por Sessão (% de tokens ponderados por erro)
    ROUND((i.tokens_waste_cota + i.tokens_waste_codigo) * 100.0 / NULLIF(i.total_tokens, 0), 2)  AS kpi_idls_lean,

    -- Burn Rate de IA (R$): tokens valorados pelo VRT + custo ocioso
    ROUND(i.total_tokens * (
            (0.025 + (f.total_rateio_infra / NULLIF(i.total_tokens / 1000.0,0)))
            * (100.0 / NULLIF(100.0 - (i.tokens_desperdicados_brutos * 100.0 / NULLIF(i.total_tokens,0)),0))
          ) / 1000.0
        + (i.total_minutos_bloqueados * ((h.custo_hora_dev + (f.total_rateio_infra / NULLIF(t.total_hh_geral,0))) / 60.0)), 2) AS burn_rate_ia,

    -- ICCA: Índice de Cobertura de Custo de IA (x) = MRR / custo recuperado
    ROUND(h.faturamento_mrr_incremental / NULLIF(
            i.total_tokens * (
              (0.025 + (f.total_rateio_infra / NULLIF(i.total_tokens / 1000.0,0)))
              * (100.0 / NULLIF(100.0 - (i.tokens_desperdicados_brutos * 100.0 / NULLIF(i.total_tokens,0)),0))
            ) / 1000.0, 0), 2)                                                                   AS kpi_icca,

    -- IBMT: Burn Rate Marginal do Token (x) = Burn Rate de IA / Δ MRR
    ROUND((i.total_tokens * (
              (0.025 + (f.total_rateio_infra / NULLIF(i.total_tokens / 1000.0,0)))
              * (100.0 / NULLIF(100.0 - (i.tokens_desperdicados_brutos * 100.0 / NULLIF(i.total_tokens,0)),0))
            ) / 1000.0
          + (i.total_minutos_bloqueados * ((h.custo_hora_dev + (f.total_rateio_infra / NULLIF(t.total_hh_geral,0))) / 60.0)))
          / NULLIF(h.faturamento_mrr_incremental, 0), 3)                                         AS kpi_ibmt,

    -- CPP: Custo por Ponto de Progresso (R$/%) = TCO IA acumulado / % progresso
    ROUND(s.tco_ia_acumulado / NULLIF(s.progresso_pct_acumulado, 0), 2)                          AS kpi_cpp,
    s.progresso_pct_acumulado                                                                    AS progresso_pct,

    -- PSR: Score do Projeto (0-5) = 0.40*S_prog + 0.25*S_int + 0.35*S_entrega
    ROUND(
        0.40 * MIN(5.0, (s.progresso_pct_delta_real / NULLIF(s.progresso_pct_delta_plan,0)) * 5.0)
      + 0.25 * (5.0 * (1.0 - MIN(1.0, s.interrupcoes_periodo * 1.0 / NULLIF(s.interrupcoes_teto,0))))
      + 0.35 * ((sa.sessoes_uteis * 1.0 / NULLIF(sa.total_sessoes,0)) * 5.0)
    , 2)                                                                                         AS kpi_psr
FROM dados_ia i
LEFT JOIN sessao_agg            sa ON i.project_name = sa.project_name
LEFT JOIN horas_desenvolvimento h  ON i.project_name = h.project_name
LEFT JOIN projetos_status       s  ON i.project_name = s.project_name
CROSS JOIN custo_fixo f
CROSS JOIN total_horas_empresa t
) q
ORDER BY q.kpi_psr DESC;
