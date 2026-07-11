-- ============================================================================
-- Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard
-- Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
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
    supera_us              INTEGER,-- 1 se TIR > juros EUA
    tirm                   REAL,   -- TIRM (TIR Modificada / MIRR, %/período)
    vul                    REAL    -- VUL (Valor Uniforme Líquido / anuidade equivalente do VPL, R$)
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

-- ===========================================================================
-- 7. DEMATEL — matriz de relação total, proeminência (R+C), relação (R-C).
--    Arquitetura de integração conforme John, J. (2025), "Integration of
--    DEMATEL with Other MCDM Methods for Comprehensive Techno-Economic
--    Analysis": DEMATEL deriva pesos por influência que alimentam os
--    métodos de ranqueamento (ELECTRE, PROMETHEE, MAUT, MCDA-C, TOPSIS).
-- ===========================================================================
CREATE TABLE IF NOT EXISTS dematel_criterio (
    criterio     TEXT PRIMARY KEY,
    rotulo       TEXT,
    r            REAL,     -- soma da linha da matriz total T (influência exercida)
    c            REAL,     -- soma da coluna da matriz total T (influência recebida)
    prominencia  REAL,     -- R + C  (importância no sistema)
    relacao      REAL,     -- R - C  (> 0 = causa; < 0 = efeito)
    papel        TEXT,     -- 'causa' | 'efeito'
    peso         REAL      -- peso normalizado derivado de sqrt((R+C)^2 + (R-C)^2)
);

CREATE TABLE IF NOT EXISTS dematel_relacao (
    origem        TEXT,
    destino       TEXT,
    intensidade   REAL,     -- t_ij da matriz de relação total
    acima_limiar  INTEGER,  -- 1 se t_ij > limiar alpha (aresta do diagrama de influência)
    PRIMARY KEY (origem, destino)
);

-- 8. Ranking por método MCDM (formato longo) + consenso entre métodos.
CREATE TABLE IF NOT EXISTS decisao_mcdm (
    project_name TEXT,
    metodo       TEXT,     -- 'ELECTRE I' | 'PROMETHEE II' | 'MAUT' | 'MCDA-C' | 'AHP-TOPSIS 2n'
    score        REAL,
    rank_        INTEGER,
    PRIMARY KEY (project_name, metodo)
);

CREATE TABLE IF NOT EXISTS decisao_consenso (
    project_name  TEXT PRIMARY KEY,
    rank_medio    REAL,     -- média das posições entre os métodos
    borda         INTEGER,  -- pontos de Borda (n - posição), somados
    rank_final    INTEGER,
    unanime       INTEGER   -- 1 se todos os métodos deram a mesma posição
);

-- ===========================================================================
-- 9. Monte Carlo: estatísticas, percentis,
--    histograma (100 bins) e tornado de sensibilidade (beta + correlação).
-- ===========================================================================
CREATE TABLE IF NOT EXISTS mc_estatisticas (
    project_name    TEXT,
    variavel        TEXT,    -- 'VPL' | 'TIR' | 'TIRM' | 'VUL' | 'ILL'
    iteracoes       INTEGER,
    minimo          REAL,
    media           REAL,
    maximo          REAL,
    mediana         REAL,
    variancia       REAL,
    desvio_padrao   REAL,
    amplitude       REAL,
    curtose         REAL,
    assimetria      REAL,
    coef_variacao   REAL,
    prob_menor_zero REAL,    -- P(X < 0) em %  (probabilidade acumulada em zero)
    var_5           REAL,    -- Value at Risk: percentil 5%
    cvar_5          REAL,    -- Conditional VaR: média da cauda abaixo do percentil 5%
    PRIMARY KEY (project_name, variavel)
);

CREATE TABLE IF NOT EXISTS mc_percentis (
    project_name TEXT,
    variavel     TEXT,
    percentil    INTEGER,   -- 1..99, incrementos de 1%
    valor        REAL,
    PRIMARY KEY (project_name, variavel, percentil)
);

CREATE TABLE IF NOT EXISTS mc_histograma (
    project_name  TEXT,
    variavel      TEXT,
    bin_idx       INTEGER,
    bin_inferior  REAL,
    bin_superior  REAL,
    frequencia    INTEGER,
    cumul_pct     REAL,
    PRIMARY KEY (project_name, variavel, bin_idx)
);

CREATE TABLE IF NOT EXISTS mc_tornado (
    project_name      TEXT,
    variavel_saida    TEXT,
    variavel_entrada  TEXT,
    beta_regressao    REAL,   -- coeficiente da regressão múltipla (não padronizado)
    coef_correlacao   REAL,   -- correlação de Pearson entrada x saída
    ordem             INTEGER,
    PRIMARY KEY (project_name, variavel_saida, variavel_entrada)
);

-- ===========================================================================
-- 10. Ajuste de distribuições aos dados (fit distributions to data): distribuições
--     candidatas ajustadas por MLE à série real de tokens, ordenadas por AIC.
--     A vencedora (escolhida=1) vira a variável de entrada do Monte Carlo.
-- ===========================================================================
CREATE TABLE IF NOT EXISTS mc_ajuste_distribuicao (
    project_name TEXT,
    variavel     TEXT,      -- 'TOKENS'
    distribuicao TEXT,      -- rótulo legível (Normal, LogNormal, Gamma, ...)
    parametros   TEXT,      -- JSON: {scipy, params, n_obs}
    loglik       REAL,
    aic          REAL,      -- 2k - 2·logL  (menor = melhor)
    ks_stat      REAL,      -- estatística D de Kolmogorov-Smirnov
    ks_pvalue    REAL,      -- p-valor (alto = não rejeitamos a aderência)
    rank_        INTEGER,
    escolhida    INTEGER,   -- 1 = menor AIC
    PRIMARY KEY (project_name, variavel, distribuicao)
);

-- ===========================================================================
-- 11. Robustez do ranking: perturbação de Dirichlet nos pesos do DEMATEL.
--     w' ~ Dirichlet(κ·w) preserva E[w']=w e κ controla a dispersão.
--     Reranqueamos N vezes: o veredito deixa de ser "X é o melhor" e passa a
--     ser "X vence em P% dos universos de preferência".
-- ===========================================================================
CREATE TABLE IF NOT EXISTS mcdm_robustez (
    project_name  TEXT,
    metodo        TEXT,     -- método de ranqueamento ou 'CONSENSO (Borda)'
    prob_vitoria  REAL,     -- % das simulações em que ficou em 1º
    prob_top3     REAL,     -- % em que ficou entre os 3 primeiros
    rank_medio    REAL,
    rank_p05      REAL,     -- percentil 5% da posição (melhor caso plausível)
    rank_p95      REAL,     -- percentil 95% da posição (pior caso plausível)
    PRIMARY KEY (project_name, metodo)
);

CREATE TABLE IF NOT EXISTS mcdm_robustez_dist (
    project_name TEXT,
    posicao      INTEGER,
    frequencia   INTEGER,
    pct          REAL,
    PRIMARY KEY (project_name, posicao)
);

-- ===========================================================================
-- Cronograma Monte Carlo (Schedule Risk Analysis / PERT) + Gantt + CPM.
-- Reusa o motor de Monte Carlo (monte_carlo.py) apontado para DURAÇÕES de tarefas
-- em vez de fluxos de caixa: devolve a distribuição da data de término, a data com
-- 80% de confiança (P80), P(no prazo) e o índice de criticidade de cada tarefa.
-- ===========================================================================

-- WBS mínima por projeto: estimativa de 3 pontos (PERT) + dependências.
CREATE TABLE IF NOT EXISTS cronograma_tarefas (
    project_name  TEXT,
    tarefa_id     INTEGER,   -- id local da tarefa dentro do projeto (1..n)
    nome          TEXT,
    dur_min       REAL,      -- otimista  (a)   — dias
    dur_prob      REAL,      -- mais provável (m)
    dur_max       REAL,      -- pessimista (b)
    predecessoras TEXT,      -- ids separados por vírgula, '' se nenhuma (FS = finish-to-start)
    PRIMARY KEY (project_name, tarefa_id)
);

-- Resultado da simulação do cronograma por projeto (duração total, em dias).
CREATE TABLE IF NOT EXISTS mc_cronograma (
    project_name  TEXT PRIMARY KEY,
    iteracoes     INTEGER,
    prazo_alvo    REAL,      -- deadline planejada (dias) — baseline
    media         REAL,
    minimo        REAL,
    maximo        REAL,
    p10           REAL,
    p50           REAL,      -- mediana
    p80           REAL,      -- data com 80% de confiança (compromisso recomendável)
    p95           REAL,
    prob_no_prazo REAL       -- P(término <= prazo_alvo), em %
);

-- Histograma da data de término (para o gráfico de risco + curva S acumulada).
CREATE TABLE IF NOT EXISTS mc_cronograma_hist (
    project_name  TEXT,
    classe_inf    REAL,      -- borda inferior da classe (dias)
    frequencia    INTEGER,
    cumulativo    REAL,      -- % acumulado
    PRIMARY KEY (project_name, classe_inf)
);

-- CPM + índice de criticidade por tarefa (posições p50 para o Gantt).
CREATE TABLE IF NOT EXISTS cronograma_critico (
    project_name       TEXT,
    tarefa_id          INTEGER,
    nome               TEXT,
    inicio             REAL,   -- early start no cenário mediano (dias desde o início)
    fim                REAL,   -- early finish no cenário mediano
    duracao            REAL,   -- duração esperada (PERT) usada no layout
    folga              REAL,   -- folga total (float); 0 = crítica no cenário mediano
    indice_criticidade REAL,   -- % das simulações em que a tarefa caiu no caminho crítico
    eh_critico         INTEGER,-- 1 se folga ~ 0 no cenário mediano
    PRIMARY KEY (project_name, tarefa_id)
);

-- ===========================================================================
-- Earned Value Management (EVM) + Earned Schedule (ES).
-- Unifica CUSTO + PRAZO + ESCOPO num só quadro. Ancorado em campos reais:
-- BAC = horas_desenvolvimento.custo_total_desenvolvimento; progresso real vs
-- planejado = projetos_status; duração planejada (PD) = mc_cronograma.prazo_alvo.
-- ===========================================================================

-- Série temporal PV/EV/AC por período (para a curva S clássica do EVM).
CREATE TABLE IF NOT EXISTS evm_serie (
    project_name TEXT,
    periodo      INTEGER,   -- período (semana) desde o início
    pv           REAL,      -- Planned Value acumulado (R$)
    ev           REAL,      -- Earned Value acumulado (R$) — só até a data de status
    ac           REAL,      -- Actual Cost acumulado (R$) — só até a data de status
    PRIMARY KEY (project_name, periodo)
);

-- Índices do EVM/ES na data de status (snapshot).
CREATE TABLE IF NOT EXISTS evm_indices (
    project_name TEXT PRIMARY KEY,
    bac          REAL,   -- Budget At Completion
    pd           INTEGER,-- Planned Duration (períodos)
    at_periodo   INTEGER,-- Actual Time (data de status, em períodos)
    pv           REAL,   -- PV na data de status
    ev           REAL,   -- EV na data de status
    ac           REAL,   -- AC na data de status
    sv           REAL,   -- Schedule Variance = EV - PV
    cv           REAL,   -- Cost Variance     = EV - AC
    spi          REAL,   -- Schedule Performance Index = EV/PV
    cpi          REAL,   -- Cost Performance Index     = EV/AC
    eac          REAL,   -- Estimate At Completion = BAC/CPI
    etc          REAL,   -- Estimate To Complete   = EAC - AC
    vac          REAL,   -- Variance At Completion = BAC - EAC
    tcpi         REAL,   -- To-Complete Perf. Index = (BAC-EV)/(BAC-AC)
    es           REAL,   -- Earned Schedule (períodos)
    spi_t        REAL,   -- SPI(t) = ES/AT (não converge para 1 no fim, ao contrário do SPI)
    sv_t         REAL,   -- SV(t)  = ES - AT (adiantado/atrasado, em períodos)
    ieac_t       REAL    -- Independent EAC de prazo = PD/SPI(t)
);

-- ===========================================================================
-- Métricas de EXECUÇÃO de IA no tempo (a partir de logs_langfuse REAIS).
-- Diferencia de um framework financeiro genérico: saúde operacional ao longo do
-- tempo, não só valor/custo. Bucketizado por DIA.
-- ===========================================================================

-- Latência p50/p95/p99 por dia — tendência e violação de SLO.
CREATE TABLE IF NOT EXISTS exec_latencia_tempo (
    project_name TEXT,
    dia          TEXT,
    p50          REAL,
    p95          REAL,
    p99          REAL,
    n            INTEGER,
    viola_slo    INTEGER,   -- 1 se p95 > SLO (limite de serviço)
    PRIMARY KEY (project_name, dia)
);

-- Token budget burndown/burnup — consumo acumulado vs orçamento acumulado.
CREATE TABLE IF NOT EXISTS exec_tokens_burndown (
    project_name  TEXT,
    dia           TEXT,
    tokens_dia    INTEGER,
    tokens_acum   INTEGER,
    orcamento_acum REAL,
    PRIMARY KEY (project_name, dia)
);

-- Tendência de qualidade (taxa de erro) por dia + alerta de regressão.
CREATE TABLE IF NOT EXISTS exec_qualidade_tempo (
    project_name    TEXT,
    dia             TEXT,
    n               INTEGER,
    erros           INTEGER,
    taxa_erro       REAL,     -- % de logs com tipo_erro != 'NENHUM'
    alerta_regressao INTEGER, -- 1 se a taxa saltou acima da média móvel + 2σ (SPC)
    PRIMARY KEY (project_name, dia)
);

-- Drift da distribuição de tokens vs a janela-baseline (1º dia), via Kolmogorov-Smirnov.
CREATE TABLE IF NOT EXISTS exec_drift (
    project_name TEXT,
    dia          TEXT,
    ks_stat      REAL,      -- D de KS (2 amostras) entre a distribuição do dia e a baseline
    drift_alerta INTEGER,   -- 1 se D > limiar (mudança de comportamento do modelo)
    PRIMARY KEY (project_name, dia)
);

-- ===========================================================================
-- Gestão de risco: registro vivo + matriz Probabilidade×Impacto + burndown.
-- Complementa o Monte Carlo (risco quantitativo agregado) com o risco QUALITATIVO
-- que todo PMO cobra. Probabilidade/impacto ancorados nos sinais REAIS já calculados
-- (drift, violação de SLO, CPI<1, regressão de qualidade).
-- ===========================================================================

-- Registro de risco (escala 1..5 para probabilidade e impacto; exposição = P×I, 1..25).
CREATE TABLE IF NOT EXISTS risco_registro (
    project_name  TEXT,
    risco_id      INTEGER,
    categoria     TEXT,
    descricao     TEXT,
    dono          TEXT,
    probabilidade INTEGER,   -- 1..5
    impacto       INTEGER,   -- 1..5
    exposicao     INTEGER,   -- P × I (1..25)
    nivel         TEXT,      -- 'baixo' | 'medio' | 'alto' | 'critico'
    gatilho       TEXT,
    mitigacao     TEXT,
    status        TEXT,      -- 'aberto' | 'mitigando' | 'fechado'
    PRIMARY KEY (project_name, risco_id)
);

-- Risk burndown: exposição total do projeto caindo (ou não) ao longo do tempo.
CREATE TABLE IF NOT EXISTS risco_burndown (
    project_name    TEXT,
    dia             TEXT,
    exposicao_total INTEGER,
    exposicao_ideal REAL,     -- trilha ideal de redução (baseline linear a zero)
    PRIMARY KEY (project_name, dia)
);

-- ===========================================================================
-- Métricas de FLUXO (Kanban/ágil): CFD, cycle time, throughput, WIP.
-- Fecha o lado de execução/entrega que faltava. Itens de trabalho por projeto
-- fluindo entre estados (backlog -> doing -> review -> done) ao longo dos dias.
-- ===========================================================================

-- Cumulative Flow Diagram: contagem acumulada por estado, por dia.
CREATE TABLE IF NOT EXISTS fluxo_cfd (
    project_name TEXT,
    dia          TEXT,
    backlog      INTEGER,
    doing        INTEGER,
    review       INTEGER,
    done         INTEGER,
    wip          INTEGER,   -- doing + review
    PRIMARY KEY (project_name, dia)
);

-- Itens concluídos com cycle time e lead time (para scatter + percentis).
CREATE TABLE IF NOT EXISTS fluxo_itens (
    project_name TEXT,
    item_id      INTEGER,
    dia_conclusao TEXT,
    lead_time    REAL,   -- dias do backlog ao done
    cycle_time   REAL,   -- dias do doing ao done
    PRIMARY KEY (project_name, item_id)
);

-- Métricas de fluxo resumidas por projeto (percentis de cycle time, throughput).
CREATE TABLE IF NOT EXISTS fluxo_resumo (
    project_name   TEXT PRIMARY KEY,
    throughput_dia REAL,   -- itens concluídos por dia (média)
    ct_p50         REAL,   -- cycle time mediano
    ct_p85         REAL,   -- cycle time P85 (compromisso de previsão)
    wip_medio      REAL,
    lead_p50       REAL
);
