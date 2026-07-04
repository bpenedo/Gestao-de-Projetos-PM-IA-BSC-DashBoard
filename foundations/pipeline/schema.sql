-- ============================================================================
-- Framework "Gestão de Projetos (PM) IA com Painel BSC e DashBoard"
-- Framework "Gestão de Projetos (PM) IA com Painel BSC e DashBoard" · (c) Bruno Teixeira Penedo — 2026. Todos os direitos reservados. E-mail: bpenedo@gmail.com
-- Schema do banco SQLite que alimenta o Balanced Scorecard de Projetos de IA.
-- ============================================================================

-- 1. Logs granulares (origem: Langfuse / aplicações). Uma linha por geração (LLM call).
CREATE TABLE IF NOT EXISTS logs_langfuse (
    id                      TEXT PRIMARY KEY,
    project_name            TEXT NOT NULL,
    session_id              TEXT,
    prompt_tokens           INTEGER DEFAULT 0,
    completion_tokens       INTEGER DEFAULT 0,
    tipo_erro               TEXT DEFAULT 'NENHUM',   -- NENHUM | RATE_LIMIT | ALUCINACAO_CODIGO
    prompt_categoria        TEXT DEFAULT 'Outros',   -- taxonomia do prompt (RCA de alucinação)
    tempo_bloqueado_minutos REAL DEFAULT 0,          -- Waste de Espera (Rate Limit)
    latency_seconds         REAL DEFAULT 0,          -- Cycle Time (latência da resposta)
    updated_at              TEXT                     -- ISO timestamp (carga incremental)
);

-- 2. Esforço humano por projeto (origem: timesheet/estimativa).
CREATE TABLE IF NOT EXISTS horas_desenvolvimento (
    project_name                 TEXT PRIMARY KEY,
    horas_trabalhadas            REAL DEFAULT 0,
    custo_hora_dev               REAL DEFAULT 0,
    custo_total_desenvolvimento  REAL DEFAULT 0,
    faturamento_mrr_incremental  REAL DEFAULT 0,      -- Δ MRR do mês (para IBMT)
    cac_planejado                REAL DEFAULT NULL,   -- futuro (em aberto)
    payback_meses                REAL DEFAULT NULL    -- futuro (em aberto)
);

-- 3. Custos fixos de ferramentas = base de rateio (origem: Assinatura_IA.md).
CREATE TABLE IF NOT EXISTS assinaturas_infra (
    item_ferramenta TEXT PRIMARY KEY,
    valor_mensal    REAL DEFAULT 0
);

-- 4. Estado de progresso/interrupções por projeto (origem: projeto_main.md / Interrupcoes.md).
--    Necessário para CPP e para o PSR (Score 0-5).
CREATE TABLE IF NOT EXISTS projetos_status (
    project_name              TEXT PRIMARY KEY,
    progresso_pct_delta_real  REAL DEFAULT 0,   -- avanço de % no período
    progresso_pct_delta_plan  REAL DEFAULT 0,   -- avanço de % planejado no período
    progresso_pct_acumulado   REAL DEFAULT 0,   -- % total atingido (denominador do CPP)
    tco_ia_acumulado          REAL DEFAULT 0,   -- custo de IA acumulado (numerador do CPP)
    interrupcoes_periodo      INTEGER DEFAULT 0,
    interrupcoes_teto         INTEGER DEFAULT 20
);

-- 5. Alertas críticos isolados para triagem rápida no topo do dashboard.
CREATE TABLE IF NOT EXISTS alertas_criticos (
    id                  TEXT PRIMARY KEY,
    project_name        TEXT,
    session_id          TEXT,
    tipo_erro           TEXT,
    prompt_truncado     TEXT,
    resposta_truncada   TEXT,
    tokens_desperdicados INTEGER,
    data_evento         TEXT
);

-- 7. Snapshots semanais de KPIs (para gráficos de TENDÊNCIA: CPP, PSR, burn rate ao longo do tempo).
CREATE TABLE IF NOT EXISTS kpi_snapshots (
    data_snapshot   TEXT,        -- 'YYYY-MM-DD' (sexta do checkpoint)
    project_name    TEXT,
    cpp             REAL,        -- Custo por Ponto de Progresso (R$/%)
    psr             REAL,        -- Score 0-5
    burn_rate_ia    REAL,        -- R$
    iita            REAL,        -- %
    peuc            REAL,        -- %
    PRIMARY KEY (data_snapshot, project_name)
);

-- 8. Fluxo de caixa por projeto (fornecido pelo usuário via CSV/planilha) → VPL/Payback.
CREATE TABLE IF NOT EXISTS fluxo_caixa (
    project_name TEXT,
    periodo      INTEGER,   -- 0 = investimento inicial; 1,2,3... = períodos seguintes
    fluxo        REAL,      -- fluxo de caixa do período (investimento = negativo)
    taxa         REAL,      -- taxa de desconto por período (ex.: 0.10 = 10%)
    PRIMARY KEY (project_name, periodo)
);

-- Resultados financeiros consolidados (calculados por carregar_fluxo.py).
CREATE TABLE IF NOT EXISTS vpl_resultado (
    project_name           TEXT PRIMARY KEY,
    taxa                   REAL,
    vpl                    REAL,   -- Valor Presente Líquido (R$)
    payback_simples        REAL,   -- períodos (interpolado, variação temporal)
    payback_descontado     REAL,   -- períodos (interpolado)
    tir                    REAL,   -- Taxa Interna de Retorno (%/período)
    ill                    REAL,   -- Índice de Lucratividade Líquida (PI): VP entradas / |investimento|
    vpl_usd                REAL,   -- VPL dolarizado (US$, descontado à taxa dos EUA)
    payback_desc_usd       REAL,   -- payback descontado em US$ (períodos)
    selic                  REAL,   -- benchmark SELIC a.a.
    us_rate                REAL,   -- benchmark Fed funds a.a.
    usd_brl                REAL,   -- câmbio usado
    supera_selic           INTEGER,-- 1 se TIR > SELIC
    supera_us              INTEGER -- 1 se TIR > juros EUA
);

-- Fluxo período a período com acumulados (simples e descontado) para o gráfico.
CREATE TABLE IF NOT EXISTS vpl_fluxo (
    project_name TEXT,
    periodo      INTEGER,
    fluxo        REAL,
    fluxo_desc   REAL,   -- fluxo descontado = fluxo / (1+i)^periodo
    cum_simples  REAL,   -- acumulado simples
    cum_desc     REAL,   -- acumulado descontado
    PRIMARY KEY (project_name, periodo)
);

-- 9. Planos de assinatura de IA (US$ + câmbio + IOF -> custo total mensal em R$).
CREATE TABLE IF NOT EXISTS planos_assinatura (
    provedor   TEXT,
    plano      TEXT,
    usd_mes    REAL,
    cambio     REAL,   -- BRL por USD
    iof_pct    REAL,   -- % de IOF sobre operação internacional
    PRIMARY KEY (provedor, plano)
);

-- 10. Decisão multicritério AHP-TOPSIS (2 normalizações) — ranking final dos projetos.
CREATE TABLE IF NOT EXISTS decisao_mcda (
    project_name  TEXT PRIMARY KEY,
    ci_vector     REAL,     -- closeness coefficient (normalização vetorial/Euclidiana)
    ci_minmax     REAL,     -- closeness coefficient (normalização min-max/linear)
    ci_final      REAL,     -- média das duas (ranking final)
    rank_final    INTEGER,
    rank_vector   INTEGER,
    rank_minmax   INTEGER,
    concordante   INTEGER    -- 1 se as duas normalizações concordam na posição
);

-- 6. Pauta da reunião semanal (Weekly Checkpoint - sexta 09:00).
CREATE TABLE IF NOT EXISTS reuniao_weekly (
    data_reuniao          TEXT,
    project_name          TEXT,
    sumario_executivo     TEXT,
    insights_clevel       TEXT,
    mapeamento_tesouro    TEXT,
    joia_da_coroa         TEXT,
    acoes_corretivas_lean TEXT,
    PRIMARY KEY (data_reuniao, project_name)
);
