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

-- ===========================================================================
-- 🔗 CADEIA CAUSAL — o fosso: telemetria → risco → prazo → dinheiro.
-- Nenhuma ferramenta do mercado liga um token do Langfuse a um VPL, a uma data
-- P80 e a uma probabilidade de risco. Langfuse diz que o modelo derivou; ele NÃO
-- diz que o projeto atrasou 4 dias e o VPL caiu R$ 18 mil por causa disso.
-- Exige os QUATRO motores juntos (observabilidade + risco + cronograma MC + VPL).
-- ===========================================================================
-- NÃO usar DROP aqui: o schema sobe em TODO script (init_schema), e um DROP apagaria
-- a cadeia para quem rodasse depois — foi exatamente assim que o pm_agent.py achou
-- zero projetos. Quem regrava é o cadeia_causal.py, com DELETE por projeto.
CREATE TABLE IF NOT EXISTS cadeia_causal (
    project_name    TEXT PRIMARY KEY,
    -- elo 1: TELEMETRIA (logs reais do Langfuse)
    dias_com_drift  INTEGER,  -- dias em que o D de KS passou do limiar
    ks_max          REAL,     -- maior distância KS observada vs a baseline
    -- elo 2: RISCO
    risco_prob_base INTEGER,  -- probabilidade do risco "Modelo" sem drift (1..5)
    risco_prob_nova INTEGER,  -- probabilidade com o drift observado
    -- elo 3: PRAZO (Monte Carlo re-simulado com a incerteza alargada)
    tarefa_afetada  TEXT,     -- a tarefa cuja duração alarga (avaliação/guardrails)
    dur_pess_base   REAL,     -- duração pessimista (b) antes
    dur_pess_nova   REAL,     -- duração pessimista depois do drift
    p80_base        REAL,     -- P80 do cronograma antes
    p80_novo        REAL,     -- P80 depois
    dias_perdidos   REAL,     -- p80_novo - p80_base
    -- elo 4: DINHEIRO (fluxos empurrados pelos dias perdidos)
    vpl_base        REAL,
    vpl_novo        REAL,
    delta_vpl       REAL,     -- vpl_base - vpl_novo (efeito do desconto; pequeno em fluxos anuais)
    -- COST OF DELAY: o número que a diretoria sente. Receita não faturada + burn que
    -- continua queimando, por dia de atraso. É o padrão de produto (Reinertsen).
    cod_dia         REAL,     -- MRR/30 + custo de desenvolvimento por dia + burn de IA por dia
    custo_atraso    REAL      -- dias_perdidos × cod_dia, em R$ — o CUSTO REAL do drift
);

-- ===========================================================================
-- 🤖 PROJECT MANAGER AGENT — feedback conclusivo + MOTOR DE REAPRENDIZAGEM
--    POR PROJETO. Não é "IA genérica": é um reforço de alavancas por projeto.
--
-- A cada ciclo o agente (1) mede o dano de cada alavanca pela CADEIA CAUSAL,
-- (2) pondera pelo PESO APRENDIDO daquele projeto, (3) recomenda a alavanca de
-- maior dano×peso, e (4) no ciclo seguinte VERIFICA se a métrica-alvo melhorou:
--   melhorou -> peso sobe (a alavanca funciona NESTE projeto)
--   piorou   -> peso cai (aqui ela não move o ponteiro)
-- É um bandit contextual simples e auditável, não deep RL. Cada projeto
-- desenvolve o seu próprio perfil de alavancas ao longo dos ciclos.
-- ===========================================================================

-- Memória do agente: o peso de cada alavanca, POR PROJETO (o que ele aprendeu).
CREATE TABLE IF NOT EXISTS pm_agent_pesos (
    project_name TEXT,
    -- 9 alavancas, uma por DIMENSÃO do projeto: 'prazo' | 'roi' | 'risco' | 'tokens'
    -- | 'custo' | 'drift' | 'slo' | 'qualidade' | 'fluxo'
    alavanca     TEXT,
    peso         REAL,     -- começa em 1.0; sobe quando a alavanca funciona NESTE projeto
    acertos      INTEGER,  -- ciclos em que a métrica-alvo melhorou após a recomendação
    erros        INTEGER,  -- ciclos em que piorou/não melhorou
    metrica_ant  REAL,     -- valor da métrica-alvo no ciclo anterior (para o reforço)
    PRIMARY KEY (project_name, alavanca)
);

-- Feedback conclusivo do agente, por ciclo (é o que aparece no Bottom-Line).
CREATE TABLE IF NOT EXISTS pm_agent_feedback (
    project_name    TEXT,
    ciclo           INTEGER,
    veredito        TEXT,    -- a frase que nenhuma outra ferramenta consegue emitir
    dimensao        TEXT,    -- Prazo | ROI | Risco | Tokens | Custo | Qualidade | Fluxo | Confiabilidade
    causa_raiz      TEXT,    -- a alavanca de maior dano×peso
    acao            TEXT,    -- o que fazer AGORA
    pratica         TEXT,    -- a prática de referência que sustenta a ação (não é opinião)
    impacto_rs      REAL,    -- quanto se recupera, em R$, se a ação funcionar
    confianca       TEXT,    -- baixa | média | alta (vem do histórico de acertos)
    aprendizado     TEXT,    -- o que o agente aprendeu SOBRE ESTE PROJETO até aqui
    perfil          TEXT,    -- o perfil taylor-made: pesos aprendidos deste projeto
    -- PRINCE2 — management by exception. O agente só escala quando a PREVISÃO estoura a
    -- tolerância. NORMAL = dentro do acordado, nada a fazer, e ele CALA.
    status          TEXT,    -- NORMAL | EXCECAO
    zona_buffer     TEXT,    -- VERDE | AMARELO | VERMELHO (fever chart do CCPM)
    excecao         TEXT,    -- Exception Report: causa, impacto, OPÇÕES, recomendação
    PRIMARY KEY (project_name, ciclo)
);

-- Radar de TODAS as dimensões no ciclo corrente: o agente não olha só a vencedora,
-- ele mostra a bancada inteira — e o cliente vê por que a escolhida ganhou.
CREATE TABLE IF NOT EXISTS pm_agent_radar (
    project_name TEXT,
    ciclo        INTEGER,
    alavanca     TEXT,
    dimensao     TEXT,
    metrica      TEXT,    -- nome legível da métrica-alvo
    valor        REAL,    -- valor medido agora
    dias_eq      REAL,    -- dano convertido em DIAS-EQUIVALENTES de projeto
    dano_rs      REAL,    -- dias_eq × Cost of Delay/dia (R$)
    peso         REAL,    -- peso APRENDIDO desta alavanca NESTE projeto
    prioridade   REAL,    -- dano_rs × peso  (o critério de decisão)
    escolhida    INTEGER, -- 1 = é a alavanca recomendada neste ciclo
    PRIMARY KEY (project_name, ciclo, alavanca)
);

-- ===========================================================================
-- 🌡️ CCPM — BUFFER MANAGEMENT & FEVER CHART (Goldratt / Critical Chain)
-- O sinal de QUANDO AGIR. Cruza "% da cadeia concluída" com "% do buffer
-- consumido". Queimar buffer no fim é normal; queimar no começo é grave — é
-- por isso que as fronteiras são DIAGONAIS, e não linhas horizontais.
--   verde/amarelo:  y = 1/3 + (1/3)·x      amarelo/vermelho: y = 2/3 + (1/3)·x
-- VERDE = não faça nada.  AMARELO = planeje a recuperação.  VERMELHO = aja.
-- O valor aqui não é o gráfico: é dar ao agente o DIREITO DE FICAR CALADO.
-- ===========================================================================
CREATE TABLE IF NOT EXISTS buffer_fever (
    project_name    TEXT PRIMARY KEY,
    p50             REAL,  -- cadeia agressiva (sem buffer)
    p80             REAL,  -- compromisso
    p95             REAL,
    buffer_dias     REAL,  -- P80 − P50: o buffer do projeto
    previsao_dias   REAL,  -- P50 ÷ SPI(t): onde a cadeia termina no ritmo atual
    consumido_dias  REAL,  -- max(0, previsão − P50)
    pct_cadeia      REAL,  -- % da cadeia concluída (EV/BAC)
    pct_buffer      REAL,  -- % do buffer consumido
    lim_verde       REAL,  -- fronteira verde/amarelo NESTE ponto da cadeia
    lim_vermelho    REAL,  -- fronteira amarelo/vermelho NESTE ponto da cadeia
    zona            TEXT   -- VERDE | AMARELO | VERMELHO
);

-- ===========================================================================
-- 🏦 PMI — RESERVE ANALYSIS (contingência × reserva gerencial)
-- Responde a pergunta que ninguém faz: "você está SEQUER reservado o bastante?"
--   contingência      = P80 − P50   (conhecidos-desconhecidos: a variabilidade)
--   reserva gerencial = P95 − P80   (desconhecidos-desconhecidos: o susto)
-- E confronta a contingência com o que o REGISTRO DE RISCO justifica (EMV em
-- dias, Integrated Cost-Schedule Risk Analysis / Hulett). Se o risco justifica
-- mais dias do que você reservou, você está SUB-RESERVADO — e não sabia.
-- ===========================================================================
CREATE TABLE IF NOT EXISTS reserva_analise (
    project_name      TEXT PRIMARY KEY,
    contingencia      REAL,  -- P80 − P50
    reserva_gerencial REAL,  -- P95 − P80
    consumido          REAL, -- dias de contingência já queimados
    pct_consumido     REAL,
    exaustao_pct_cadeia REAL, -- em que % da cadeia a contingência acaba no ritmo atual
    emv_risco_dias    REAL,  -- contingência que o registro de risco JUSTIFICA (suposição declarada)
    emv_conservador   REAL,  -- o mesmo EMV com METADE do impacto suposto (teste de estresse)
    sub_reservado     INTEGER, -- 1 = o risco justifica mais do que você reservou
    robusto           INTEGER, -- 1 = a conclusão SOBREVIVE ao corte pela metade da suposição
    buffer_pct_cadeia REAL,  -- (P80−P50)/P50 — FATO, não depende de suposição alguma
    veredito          TEXT
);

-- ===========================================================================
-- 🚦 PRINCE2 — MANAGEMENT BY EXCEPTION (tolerâncias por dimensão)
-- O gerente NÃO é incomodado enquanto a PREVISÃO estiver dentro da tolerância.
-- Estourou a previsão -> Exception Report: causa, impacto, OPÇÕES, recomendação.
-- É o que separa um agente confiável de um alarme que toca toda semana.
-- ===========================================================================
CREATE TABLE IF NOT EXISTS pm_agent_tolerancia (
    project_name TEXT,
    ciclo        INTEGER,
    dimensao     TEXT,
    metrica      TEXT,
    previsto     REAL,    -- a PREVISÃO (não o realizado: PRINCE2 escala por previsão)
    limite       REAL,    -- a tolerância acordada
    unidade      TEXT,
    estourou     INTEGER, -- 1 = exceção
    folga_pct    REAL,    -- quanto ainda cabe dentro da tolerância (negativo = estourou)
    PRIMARY KEY (project_name, ciclo, dimensao)
);

-- ===========================================================================
-- 🏃 SPRINTS — o debate do progresso da weekly de sexta-feira.
-- A sprint NÃO é inventada aqui: ela é o PERÍODO do EVM, a cadência que o
-- projeto já tem, com PV/EV/AC reais. Sprint futura tem só PV (o plano);
-- sprint passada tem EV e AC (o que de fato aconteceu).
--
-- A métrica que abre a discussão é o SAY-DO RATIO (entregue ÷ comprometido).
-- Um time com say-do de 0,7 não é lento: ele está PROMETENDO 30% a mais do
-- que consegue. O remédio é diferente, e é por isso que a métrica importa.
--
-- E o CPI DA SPRINT (local) é separado do CPI acumulado de propósito: o
-- acumulado é uma média que ESCONDE a sprint ruim recente. O local denuncia.
-- ===========================================================================
CREATE TABLE IF NOT EXISTS sprints (
    project_name  TEXT,
    sprint        INTEGER,
    status        TEXT,     -- CONCLUIDA | ATUAL | FUTURA
    comprometido  REAL,     -- ΔPV: o que o time se comprometeu a entregar
    entregue      REAL,     -- ΔEV: o que de fato entregou (NULL no futuro)
    custo         REAL,     -- ΔAC: o que custou
    say_do        REAL,     -- entregue ÷ comprometido — a métrica do debate
    cpi_sprint    REAL,     -- entregue ÷ custo NA SPRINT (o acumulado esconde)
    restante      REAL,     -- BAC − EV acumulado (o burndown real)
    restante_ideal REAL,    -- BAC − PV acumulado (o burndown planejado)
    PRIMARY KEY (project_name, sprint)
);

-- A pauta que o Project Manager Agent leva para a weekly. Uma linha = um ponto
-- de debate, com o número que o sustenta. Reunião sem número é opinião.
CREATE TABLE IF NOT EXISTS sprint_debate (
    project_name TEXT,
    ordem        INTEGER,
    tema         TEXT,
    ponto        TEXT,     -- o que debater, com o número na frente
    severidade   TEXT,     -- 🔴 | 🟡 | 🟢
    PRIMARY KEY (project_name, ordem)
);

-- ===========================================================================
-- 💰 ORÇAMENTO GLOBAL DE TOKENS — o pool é COMPARTILHADO e FINITO.
-- Nenhuma ferramenta do mercado modela isso. Langfuse/CloudZero dão custo POR
-- PROJETO, como se cada um tivesse a própria torneira. Não tem: existe UM plano
-- contratado, e cada token que um projeto queima é um token que outro não terá.
-- É a tragédia dos comuns aplicada ao orçamento de IA — e ela tem preço.
-- ===========================================================================
CREATE TABLE IF NOT EXISTS orcamento_global (
    referencia          TEXT PRIMARY KEY,  -- 'mensal'
    tokens_contratados  INTEGER,  -- quota mensal do plano (soma dos assentos)
    custo_plano_brl     REAL,     -- USD × câmbio × (1+IOF)
    custo_infra_brl     REAL,     -- assinaturas fixas (n8n, Temporal, DB, IDE, Langfuse)
    tco_brl             REAL,     -- custo total mensal de IA
    custo_por_mtoken    REAL,     -- R$ por milhão de tokens CONTRATADOS
    consumo_run_rate    INTEGER,  -- tokens/mês na velocidade atual
    pct_utilizacao      REAL,     -- consumo ÷ contratado
    folga_tokens        INTEGER,  -- contratado − consumo (negativo = estouro)
    dias_ate_exaustao   REAL,     -- em quantos dias o pool acaba no ritmo atual
    desperdicio_rr      INTEGER,  -- tokens/mês queimados em chamadas que FALHARAM
    desperdicio_brl     REAL,     -- o mesmo, em R$
    desperdicio_vs_folga REAL     -- ⚠️ >1 = o desperdício é MAIOR que a folga contratual
);

-- Base de rateio por projeto. O rateio POR CONSUMO é o padrão do mercado — e é
-- AUTO-JUSTIFICANTE: quem mais queima recebe a maior cota, o que legitima o
-- desperdício. O rateio honesto é por VALOR ENTREGUE (EV). A diferença entre os
-- dois é o SUBSÍDIO CRUZADO: quem está sendo bancado por quem, em R$/mês.
CREATE TABLE IF NOT EXISTS orcamento_rateio (
    project_name     TEXT PRIMARY KEY,
    tokens_mes       INTEGER,  -- run-rate mensal deste projeto
    pct_pool         REAL,     -- fatia do pool que ele consome
    ev               REAL,     -- valor agregado (EVM)
    pct_valor        REAL,     -- fatia do valor que ele entrega
    eficiencia       REAL,     -- EV por milhão de tokens — a métrica que ninguém calcula
    cota_consumo     REAL,     -- R$: rateio pelo que consome (o padrão, e o errado)
    cota_valor       REAL,     -- R$: rateio pelo valor que entrega (FinOps)
    cota_progresso   REAL,     -- R$: rateio pelo avanço declarado
    cota_igual       REAL,     -- R$: rateio igualitário (a base ingênua)
    subsidio_brl     REAL,     -- cota_consumo − cota_valor  (>0 = É subsidiado)
    papel            TEXT,     -- SUBSIDIADO | PAGADOR | NEUTRO
    desperdicio_tok  INTEGER,  -- tokens que ESTE projeto queimou em falha
    desperdicio_brl  REAL
);

-- ===========================================================================
-- 🔄 COTA ADAPTATIVA — o budget de cada projeto é FATIADO do pool global, e
-- REDIMENSIONADO sempre que N muda. Cadastrou projeto novo? Todo mundo encolhe.
-- Isto substitui o orçamento circular antigo (consumo × 1,10), que era um RECIBO
-- disfarçado de orçamento: nenhum projeto podia estourar, por construção.
-- ===========================================================================
CREATE TABLE IF NOT EXISTS orcamento_cota (
    project_name   TEXT PRIMARY KEY,
    n_portfolio    INTEGER,  -- quantos projetos dividiam o pool quando isto foi calculado
    piso_tokens    INTEGER,  -- o mínimo vital (nenhum projeto entrega valor com zero token)
    variavel_tokens INTEGER, -- a parte distribuída por VALOR ENTREGUE (EV)
    cota_tokens    INTEGER,  -- piso + variável = o orçamento REAL deste projeto
    cota_brl       REAL,
    consumo_tokens INTEGER,  -- run-rate mensal
    pct_uso        REAL,     -- consumo ÷ cota  (>1 = ESTOUROU)
    excedente      INTEGER,  -- consumo − cota (positivo = rouba do pool dos outros)
    excedente_brl  REAL,
    estourou       INTEGER
);

-- 💥 O CUSTO DE ADMITIR UM PROJETO NOVO. Ninguém no mercado precifica isto: num pool
-- FINITO, cadastrar o projeto N+1 tira tokens de todos os N que já estavam lá. A diluição
-- não é abstrata — ela vira menos capacidade, menos entrega e, pela cadeia causal, atraso
-- em R$. É a pergunta que o comitê de portfólio nunca consegue responder:
-- "o que custa dizer SIM a mais um projeto?"
CREATE TABLE IF NOT EXISTS orcamento_admissao (
    cenario          TEXT PRIMARY KEY,  -- 'n+1', 'n+2', 'n+3'
    n_atual          INTEGER,
    n_novo           INTEGER,
    cota_media_antes INTEGER,
    cota_media_depois INTEGER,
    diluicao_pct     REAL,     -- quanto CADA projeto existente perde de cota
    tokens_perdidos  INTEGER,  -- total tirado dos projetos existentes
    custo_diluicao   REAL,     -- em R$ do plano
    veredito         TEXT
);

-- ===========================================================================
-- 🔒 CONTENÇÃO DE RECURSO PRECIFICADA — a cadeia causal aplicada ao PORTFÓLIO.
--
-- A cadeia causal original liga, DENTRO de um projeto: token → risco → prazo → R$.
-- Isto liga ENTRE projetos: o excedente de um → exaustão do pool → estrangulamento
-- dos outros → o P80 DELES escorrega → o Cost of Delay DELES cobra a conta.
--
-- ⚠️ HONESTIDADE OBRIGATÓRIA: enquanto o consumo total couber na quota, NÃO há
-- estrangulamento físico — o dano é ALOCATIVO (subsídio cruzado), não operacional.
-- Dizer "o projeto J está atrasando o C" com folga no pool seria mentira. Por isso
-- este módulo é CENARIZADO: ele mostra a que ponto de crescimento o pool vira, e
-- quanto custa quando virar. É previsão, e está rotulada como tal.
-- ===========================================================================
CREATE TABLE IF NOT EXISTS contencao_cenario (
    cenario          TEXT PRIMARY KEY,  -- 'atual' | '+10%' | '+25%' | 'sem desperdício'
    crescimento      REAL,
    consumo_mes      INTEGER,
    pct_quota        REAL,
    dia_exaustao     REAL,     -- em que dia do mês o pool acaba
    dias_parados     REAL,     -- 30 − dia_exaustao (0 se não esgota)
    custo_cod_total  REAL,     -- Σ (dias parados × CoD/dia de CADA projeto)  -- em R$
    veredito         TEXT
);

-- Quem paga a conta do estrangulamento, projeto a projeto. Quando o pool seca, TODOS
-- param — inclusive (e sobretudo) os eficientes, que não causaram o problema.
CREATE TABLE IF NOT EXISTS contencao_projeto (
    project_name     TEXT PRIMARY KEY,
    cod_dia          REAL,     -- Cost of Delay/dia DESTE projeto (da cadeia causal)
    excedente        INTEGER,  -- quanto ele toma do pool (negativo = cede)
    eficiencia       REAL,     -- EV por milhão de tokens
    custo_sofrido    REAL,     -- R$ que ELE perde no cenário de exaustão
    culpa_rs         REAL,     -- R$ de dano que ELE causa aos OUTROS (rateado pelo excedente)
    saldo            REAL,     -- culpa − sofrido: >0 = causa mais dano do que sofre
    papel            TEXT      -- ALGOZ | VÍTIMA | NEUTRO
);

-- 🪓 POLÍTICA DE ADMISSÃO E CORTE. Se o portfólio precisa de espaço, QUEM sai?
-- A resposta honesta não é "o que gasta mais" — é "o que entrega menos POR TOKEN".
-- Ordena os candidatos por eficiência (EV/Mtoken) e mostra o trade-off explícito:
-- quanto de pool se libera contra quanto de valor se sacrifica.
CREATE TABLE IF NOT EXISTS admissao_politica (
    project_name     TEXT PRIMARY KEY,
    ordem_corte      INTEGER,  -- 1 = primeiro candidato ao corte
    eficiencia       REAL,
    tokens_liberados INTEGER,  -- quanto do pool volta se ele sair
    pct_pool_liberado REAL,
    valor_sacrificado REAL,    -- EV que se perde
    pct_valor_perdido REAL,
    projetos_novos   REAL,     -- quantos projetos novos cabem no espaço liberado
    troca            TEXT      -- o veredito do trade-off
);
