"""
🤖 PROJECT MANAGER AGENT — o gerente que lê TODAS as dimensões e APRENDE com cada projeto.

O dashboard diagnostica. A cadeia causal quantifica. O AGENTE decide o que fazer agora —
e, ciclo após ciclo, descobre qual alavanca de fato move o ponteiro *naquele* projeto.
Taylor-made: cada projeto termina com o SEU perfil, que não serve para o vizinho.

AS 10 ALAVANCAS — uma por dimensão do projeto, cada uma com métrica-alvo objetiva e uma
PRÁTICA DE REFERÊNCIA nomeada (a ação não é opinião minha; é o estado da arte):

  dimensão      métrica-alvo (menor é melhor)          prática que sustenta a ação
  ─────────────────────────────────────────────────────────────────────────────────────
  prazo       P80 acima do prazo prometido           PMBOK 7 / SRA — comprometer no P80
  roi         P(VPL < 0) na simulação                WSJF-CD3 (Reinertsen/SAFe)
  risco       exposição dos riscos abertos           PMI Risk Mgmt — EMV do registro
  tokens      consumo ÷ orçamento de tokens          FinOps Framework — unit economics
  custo       ineficiência de custo (1/CPI − 1)      EVM ANSI/EIA-748 — EAC = BAC/CPI
  drift       dias de prazo perdidos pela deriva     MLOps — KS 2-amostras + reancoragem
  slo         p95 acima do SLO                       Google SRE — orçamento de erro
  qualidade   taxa de erro da avaliação              DORA — change failure rate + eval gate
  fluxo       lead time acima do prometido           Lei de Little + limite de WIP (Kanban)
  desperdício fração do token queimada em FALHA      Lean/muda — retrabalho é perda

A UNIDADE COMUM — como comparar drift com ROI sem trapacear:
  cada alavanca é convertida em **dias-equivalentes de projeto** e multiplicada pelo
  Cost of Delay/dia DAQUELE projeto (cadeia_causal.cod_dia). Assim tudo vira R$ na mesma
  régua. É uma EQUIVALÊNCIA declarada, não uma peça contábil — e está escrita aqui para
  poder ser criticada. Drift, prazo e fluxo já nascem em dias (P80 e Lei de Little); as
  demais são frações de um ciclo de gestão (CICLO_DIAS).

O QUE O AGENTE FAZ QUE NENHUMA FERRAMENTA FAZ:
  · NOMEIA a tarefa culpada e denuncia a ARMADILHA — tarefa que o Gantt determinístico
    mostra com folga, mas que está no caminho crítico na maioria das simulações.
  · SOMA o token queimado em chamada que FALHOU (alucinação, rate-limit): dinheiro no chão
    que nem o Langfuse nem o CloudZero agregam.
  · COBRA A DERIVADA DO RISCO: exposição que não cai é teatro de mitigação, não gestão.
  · DUVIDA DO PRÓPRIO NÚMERO: se o ajuste da distribuição reprova no KS, ele avisa que o
    P80 dele é frágil — antes que você decida com base nele.

O MOTOR DE REAPRENDIZAGEM (bandit contextual — simples e auditável, não é deep RL):
  ciclo N   : prioridade = dano_R$ × peso_aprendido → recomenda a maior; guarda a métrica
  ciclo N+1 : a métrica-alvo DAQUELA recomendação melhorou?
                sim  -> peso × 1.25   (nesta casa, essa alavanca funciona)
                não  -> peso × 0.80   (aqui ela não move o ponteiro; priorizo outra)
                nem  -> variação < BANDA_MORTA é RUÍDO: não se aprende com ruído
  Só a alavanca RECOMENDADA é avaliada: o agente responde pelo que mandou fazer, não
  leva crédito pelo que o acaso melhorou.

TESTADO E REJEITADO (fica registrado para ninguém tentar de novo):
  usar o tornado (sensibilidade do VPL) como PRIOR dos pesos, para nascer taylor-made no
  ciclo 1. Medido nos 10 projetos: dá o MESMO resultado para todos (custo ~0% / tempo
  ~100%, amplitude de 0,1 ponto). Prior que não separa projeto de projeto não é
  taylor-made — é enfeite. Os pesos partem de 1.0; o taylor-made vem do REFORÇO real.

Uso:  python3 pm_agent.py
Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026.
"""
import numpy as np

from db import get_conn, init_schema

CICLO_DIAS = 10.0      # um ciclo de gestão (sprint) — a janela em que a ação vai agir
SLO_SEG = 5.0          # o mesmo SLO de exec_metricas.py
WIP_SAUDAVEL = 8.0

ALAVANCAS = {
    "prazo": dict(
        dimensao="Prazo", nome="Prazo em risco",
        metrica="P80 acima da data prometida (dias)",
        acao="Recomprometer a data no P80 — não na média, que é otimista por construção — e "
             "comprimir o caminho crítico onde há o que comprimir.",
        pratica="PMBOK 7 + Schedule Risk Analysis: a soma dos mais-prováveis é otimista "
                "por viés de fusão; o compromisso se faz no P80.",
        dono="Gerência do Projeto"),
    "roi": dict(
        dimensao="ROI", nome="Retorno em risco",
        metrica="P(VPL < 0) na simulação de Monte Carlo",
        acao="Repriorizar por CD3 (Cost of Delay ÷ duração): entregar antes a fatia que paga, "
             "ou encerrar o projeto enquanto o investimento ainda é recuperável.",
        pratica="WSJF/CD3 (Reinertsen, SAFe): sequenciar pelo custo do atraso dividido pela "
                "duração maximiza o valor econômico do portfólio.",
        dono="Product/Portfólio"),
    "risco": dict(
        dimensao="Risco", nome="Exposição de risco aberta",
        metrica="Exposição (probabilidade × impacto) dos riscos abertos",
        acao="Executar a mitigação do risco de maior exposição e mover o gatilho para "
             "monitoramento automático — risco sem gatilho não é gerenciado, é torcido.",
        pratica="PMI Practice Standard for Risk Management: EMV sobre o registro de risco, "
                "com dono e gatilho explícitos.",
        dono="Gerência do Projeto"),
    "tokens": dict(
        dimensao="Tokens", nome="Cota do pool global estourada",
        metrica="Consumo ÷ COTA do pool compartilhado (não o próprio consumo)",
        acao="Cortar o modelo premium onde o menor resolve, limitar o tamanho de saída e "
             "ligar cache. E entender o que está em jogo: o pool é FINITO — cada token "
             "acima da cota é um token que outro projeto do portfólio não terá.",
        pratica="FinOps Framework: unit economics — o que importa é R$ por resultado útil, "
                "não a fatura absoluta. O rateio por CONSUMO é auto-justificante (premia "
                "quem queima); o rateio honesto é por VALOR ENTREGUE.",
        dono="FinOps"),
    "custo": dict(
        dimensao="Custo", nome="Eficiência de custo (CPI)",
        metrica="Ineficiência de custo (1/CPI − 1)",
        acao="Refazer a projeção com EAC = BAC/CPI e negociar escopo ou orçamento AGORA — "
             "CPI abaixo de 1 no meio do projeto quase nunca se recupera sozinho.",
        pratica="EVM (ANSI/EIA-748): o CPI é notoriamente estável após ~20% de execução; "
                "EAC = BAC/CPI é a projeção defensável.",
        dono="PMO/Financeiro"),
    "drift": dict(
        dimensao="Qualidade do modelo", nome="Deriva do modelo",
        metrica="Dias de prazo perdidos pela deriva (via cadeia causal)",
        acao="Reancorar os prompts, revisar os few-shots e congelar a versão do modelo até a "
             "distribuição voltar à baseline.",
        pratica="MLOps / monitoramento contínuo: KS de 2 amostras contra a baseline; deriva "
                "detectada é deriva que se congela antes de propagar.",
        dono="Data Science"),
    "slo": dict(
        dimensao="Confiabilidade", nome="Latência acima do SLO",
        metrica="p95 de latência acima do SLO (s)",
        acao="Rotear as chamadas simples para um modelo menor, ligar cache semântico e, se o "
             "orçamento de erro estourou, congelar feature nova até pagar a confiabilidade.",
        pratica="Google SRE: orçamento de erro — quando ele zera, confiabilidade vira a "
                "prioridade, por política, não por discussão.",
        dono="SRE/Plataforma"),
    "qualidade": dict(
        dimensao="Qualidade", nome="Regressão de qualidade",
        metrica="Taxa de erro da avaliação (%)",
        acao="Instalar portão de avaliação no CI (bloqueia deploy que piora o eval) e preparar "
             "rollback da última versão.",
        pratica="DORA: change failure rate cai quando o portão é automático; qualidade que "
                "depende de disciplina humana regride.",
        dono="QA/Eval"),
    "fluxo": dict(
        dimensao="Fluxo", nome="WIP e gargalo de fluxo",
        metrica="Lead time acima do prometido (dias, pela Lei de Little)",
        acao="Limitar o WIP e desobstruir a faixa que engorda no CFD antes de puxar item novo — "
             "começar mais coisa não entrega mais rápido, entrega mais tarde.",
        pratica="Lei de Little (lead = WIP ÷ throughput) + limite de WIP (Kanban/Anderson).",
        dono="Time/Delivery"),
    "desperdicio": dict(
        dimensao="Desperdício", nome="Tokens queimados em falha",
        metrica="Fração do consumo gasta em chamadas que falharam",
        acao="Atacar o tipo de erro que mais queima token: alucinação pede guardrail e schema "
             "de saída; rate-limit pede backoff e fila. É dinheiro no chão, não é custo de operar.",
        pratica="Lean — muda/desperdício: retrabalho não é custo, é perda. O gasto com retry, "
                "timeout e alucinação não aparece somado em nenhuma ferramenta do mercado.",
        dono="Engenharia de IA"),
}

REFORCO_ACERTO = 1.25
REFORCO_ERRO = 0.80
PESO_MIN, PESO_MAX = 0.25, 4.0
BANDA_MORTA = 0.02     # <2% de variação é ruído: o agente NÃO aprende com ruído

# ═══════════════════════════════════════════════════════════════════════════════════════
# 🚦 PRINCE2 — MANAGEMENT BY EXCEPTION
#
# A regra: o gerente NÃO é incomodado enquanto a PREVISÃO estiver dentro da tolerância.
# Note "previsão", não "realizado" — PRINCE2 escala pelo que se PROJETA estourar, e é por
# isso que o P80 do Monte Carlo e o EAC do EVM servem tão bem aqui.
#
# Por que isto importa mais do que parece: sem tolerância, o agente pega o max() do radar e
# grita TODO ciclo. Um agente que grita toda semana vira ruído, e ruído é ignorado — logo
# ele não muda nada, por mais certo que esteja. A tolerância lhe dá o DIREITO DE CALAR, e é
# calando quando não há o que dizer que ele ganha o direito de ser ouvido quando há.
# ═══════════════════════════════════════════════════════════════════════════════════════
# ⚠️ TOLERÂNCIA BOA É TOLERÂNCIA ANCORADA. A primeira versão destas usava números que eu
# inventei ("erro acima de 10%", "exposição acima de 12") — e reprovava 9 e 10 projetos,
# o que fazia o agente gritar em TODOS e destruía o propósito do management by exception.
# Uma tolerância só é legítima se sair de algo que o PROJETO já declarou:
#   · prazo  -> a data que o time PROMETEU (mc_cronograma.prazo_alvo)
#   · custo  -> o orçamento que o time APROVOU (evm_indices.bac)
#   · risco  -> a classificação que o PRÓPRIO registro de risco atribui ('critico')
#   · qualid -> a BASELINE do próprio projeto (regressão contra si mesmo, à la DORA)
# Só o ROI carrega uma política declarada (20% de chance de destruir valor), porque não há
# âncora natural — e está aqui, à vista, para o board discordar.
TOL_FOLGA = 0.10          # +10% sobre o compromisso (prazo e custo)
TOL_CRITICOS_ABERTOS = 1  # até 1 risco 'crítico' aberto é tolerado; o 2º é exceção
TOL_REGRESSAO_QUAL = 1.10 # 10% pior que a própria baseline = regressão
TOL_ROI_PNEG = 0.20       # política: até 20% de chance de VPL negativo
TOL_COTA = 1.10           # +10% sobre a COTA do pool global; acima disso, escala

TOLERANCIAS = {
    "prazo":     dict(dimensao="Prazo", metrica="P80 vs a data prometida", unidade="dias"),
    "custo":     dict(dimensao="Custo", metrica="EAC vs o orçamento aprovado (BAC)", unidade="R$"),
    "risco":     dict(dimensao="Risco", metrica="Riscos 'críticos' abertos (classificação do "
                                                "próprio registro)", unidade="riscos"),
    "qualidade": dict(dimensao="Qualidade", metrica="Taxa de erro vs a baseline DESTE projeto",
                      unidade="%"),
    "roi":       dict(dimensao="ROI", metrica="P(VPL < 0)", unidade="prob."),
    # Sem esta, um projeto podia queimar 167% da cota do pool e o agente dizia "nada a
    # escalar" — o Project D fazia exatamente isso. Tolerância que não cobre o recurso
    # mais escasso do portfólio não é tolerância: é ponto cego.
    "tokens":    dict(dimensao="Tokens", metrica="Consumo vs a COTA do pool global",
                      unidade="tokens"),
}
P_AJUSTE_MIN = 0.05    # abaixo disto o ajuste da distribuição é ruim -> não confie no P80

# O tornado mede o que dirige a VARIÂNCIA do VPL. As entradas se agrupam em dois blocos,
# e cada bloco empurra as alavancas que agem sobre ele.
GRUPOS_TORNADO = {
    "custo": ("CustoTokens", ("tokens", "custo", "desperdicio")),
    "tempo": ("Periodo", ("prazo", "roi", "fluxo")),
}


def medir(conn, p):
    """
    Lê TODAS as dimensões do projeto e devolve, por alavanca:
      valor    — a métrica-alvo, medida (menor é sempre melhor)
      dias_eq  — o dano convertido em dias-equivalentes de projeto
    """
    u = lambda s, d=0.0: (conn.execute(s, (p,)).fetchone() or [None])[0] or d

    cod_dia = u("SELECT cod_dia FROM cadeia_causal WHERE project_name=?")
    drift_dias = u("SELECT dias_perdidos FROM cadeia_causal WHERE project_name=?")

    # prazo — P80 do cronograma contra a data prometida à diretoria
    row = conn.execute("SELECT p80, prazo_alvo FROM mc_cronograma WHERE project_name=?", (p,)).fetchone()
    p80, alvo = row if row else (0.0, 0.0)
    prazo_excesso = max(0.0, p80 - alvo)

    # roi — probabilidade de o VPL virar negativo na simulação
    pneg = u("SELECT prob_menor_zero FROM mc_estatisticas WHERE project_name=? AND variavel='VPL'")

    # risco — exposição média dos riscos que ainda expõem o projeto (escala 1..25).
    # LOWER() de propósito: o registro grava 'aberto' minúsculo, e um status='Aberto'
    # devolvia NULL — o risco ficou INVISÍVEL nos 10 projetos até isto ser corrigido.
    # 'mitigando' entra: mitigação em curso é risco vivo, não risco resolvido.
    expo = u("SELECT AVG(exposicao) FROM risco_registro WHERE project_name=? "
             "AND LOWER(status) IN ('aberto','mitigando')")

    # tokens — consumo contra o orçamento, no último dia da série
    tk = conn.execute(
        "SELECT tokens_acum, orcamento_acum FROM exec_tokens_burndown "
        "WHERE project_name=? ORDER BY dia DESC LIMIT 1", (p,)).fetchone()
    razao_tk = (tk[0] / tk[1]) if tk and tk[1] else 1.0

    # custo — ineficiência via CPI do EVM
    cpi = u("SELECT cpi FROM evm_indices WHERE project_name=?", 1.0) or 1.0
    inef = max(0.0, (1.0 / cpi) - 1.0)

    # slo / qualidade
    p95 = u("SELECT AVG(p95) FROM exec_latencia_tempo WHERE project_name=?")
    terr = u("SELECT AVG(taxa_erro) FROM exec_qualidade_tempo WHERE project_name=?")

    # fluxo — Lei de Little: lead esperado = WIP / throughput, contra o CT prometido (p85)
    fl = conn.execute(
        "SELECT wip_medio, throughput_dia, ct_p85 FROM fluxo_resumo WHERE project_name=?", (p,)).fetchone()
    if fl and fl[1]:
        lead_little = fl[0] / fl[1]
        fluxo_excesso = max(0.0, lead_little - fl[2])
    else:
        lead_little = fluxo_excesso = 0.0

    # desperdício — tokens queimados em chamadas que FALHARAM, como fração do consumo
    desp = u("SELECT SUM(tokens_desperdicados) FROM alertas_criticos WHERE project_name=?")
    tot_tk = u("SELECT SUM(prompt_tokens + completion_tokens) FROM logs_langfuse "
               "WHERE project_name=?")
    frac_desp = (desp / tot_tk) if tot_tk else 0.0

    m = {
        "prazo":       (prazo_excesso, prazo_excesso),                    # já em dias
        "roi":         (pneg, pneg * CICLO_DIAS),
        "risco":       (expo, (expo / 25.0) * CICLO_DIAS),
        "tokens":      (razao_tk, max(0.0, razao_tk - 1.0) * CICLO_DIAS),
        "custo":       (inef, inef * CICLO_DIAS),
        "drift":       (drift_dias, drift_dias),                          # já em dias
        "slo":         (p95, max(0.0, (p95 / SLO_SEG) - 1.0) * CICLO_DIAS),
        "qualidade":   (terr, (terr / 100.0) * CICLO_DIAS),
        "fluxo":       (fluxo_excesso, fluxo_excesso),                    # já em dias
        "desperdicio": (frac_desp, frac_desp * CICLO_DIAS),
    }
    valores = {k: float(v[0]) for k, v in m.items()}
    dias_eq = {k: float(v[1]) for k, v in m.items()}
    danos = {k: dias_eq[k] * cod_dia for k in m}
    return valores, dias_eq, danos, float(cod_dia)


def sensibilidade(conn, p):
    """
    Contribuição de cada bloco de entrada para a VARIÂNCIA do VPL, via r² do tornado
    (a correlação ao quadrado é a fração de variância explicada — o beta padronizado, aqui,
    só reflete o fator de desconto e não diz nada sobre força real).

    ⚠️ TESTADO E REJEITADO COMO PRIOR DOS PESOS. A ideia era nascer taylor-made no ciclo 1
    inclinando os pesos pela sensibilidade. Medido nos 10 projetos: o resultado é o MESMO
    para todos (custo ~0%, tempo ~100%; amplitude de 0,1 ponto). Um prior que não separa
    projeto de projeto não é taylor-made — é enfeite com nome bonito. Os pesos voltam a
    partir de 1.0 e o taylor-made vem de onde ele realmente existe: do REFORÇO por projeto.

    O que sobrou é melhor que o prior: uma FRASE que ninguém no mercado emite — se o custo
    de token não explica a variância do VPL, espremer token não muda o VPL. Ver perfil_texto.

    Devolve (share_custo, share_tempo) — somam 1.
    """
    rows = conn.execute(
        "SELECT variavel_entrada, coef_correlacao FROM mc_tornado "
        "WHERE project_name=? AND variavel_saida='VPL'", (p,)).fetchall()
    if not rows:
        return 0.5, 0.5
    forca = {g: 0.0 for g in GRUPOS_TORNADO}
    for var, corr in rows:
        for g, (prefixo, _) in GRUPOS_TORNADO.items():
            if var.startswith(prefixo):
                forca[g] += float(corr) ** 2      # r² = fração da variância explicada
    tot = sum(forca.values())
    if tot <= 0:
        return 0.5, 0.5
    return forca["custo"] / tot, forca["tempo"] / tot


def carregar_pesos(conn, p):
    rows = conn.execute(
        "SELECT alavanca, peso, acertos, erros, metrica_ant FROM pm_agent_pesos "
        "WHERE project_name=?", (p,)).fetchall()
    m = {r[0]: dict(peso=r[1], acertos=r[2], erros=r[3], ant=r[4]) for r in rows}
    for k in ALAVANCAS:
        m.setdefault(k, dict(peso=1.0, acertos=0, erros=0, ant=None))
    return m


CRIT_ARMADILHA = 20.0    # criticidade (%) a partir da qual folga no Gantt é ARMADILHA


def tarefa_culpada(conn, p):
    """
    #2 — Não basta dizer "ataque o prazo": o agente NOMEIA a tarefa. Duas coisas distintas,
    e confundi-las dá conselho inútil:

    ALAVANCA — a espinha do projeto costuma ter várias tarefas com criticidade 100% (são
      sequenciais e obrigatórias; mandar "ataque a primeira" não ajuda ninguém). Entre as
      críticas, a que de fato move a data é a de MAIOR DURAÇÃO: é ela que dá o que comprimir.

    ARMADILHA — tarefa que o Gantt determinístico mostra COM FOLGA (o MS Project diz que
      pode esperar) mas que aparece no caminho crítico numa fatia relevante das simulações.
      Esta é a que pega o gerente de surpresa, e só a SRA enxerga.

    `indice_criticidade` está em PERCENTUAL (0–100), não em fração.
    """
    rows = conn.execute(
        "SELECT nome, indice_criticidade, folga, duracao FROM cronograma_critico "
        "WHERE project_name=?", (p,)).fetchall()
    if not rows:
        return None
    criticas = [r for r in rows if r[1] >= 50.0] or rows
    alav = max(criticas, key=lambda r: r[3])          # maior duração entre as críticas
    trap = [r for r in rows if r[1] >= CRIT_ARMADILHA and r[2] > 0.5]
    trap = max(trap, key=lambda r: r[1]) if trap else None
    return dict(nome=alav[0], crit=float(alav[1]), dur=float(alav[3]),
                trap=(dict(nome=trap[0], crit=float(trap[1]), folga=float(trap[2]))
                      if trap else None))


def teatro_mitigacao(conn, p):
    """
    #3 — A derivada do risco. Todo mundo tem registro de risco; ninguém cobra se a
    exposição está de fato CAINDO. Risco 'mitigando' que não queima é torcida.
    """
    rows = conn.execute(
        "SELECT exposicao_total, exposicao_ideal FROM risco_burndown "
        "WHERE project_name=? ORDER BY dia", (p,)).fetchall()
    if len(rows) < 3:
        return None
    real = [r[0] for r in rows]
    atraso = real[-1] - rows[-1][1]                 # acima da linha ideal?
    queda = (real[0] - real[-1]) / max(real[0], 1e-9)
    return dict(acima_do_ideal=float(atraso), queda_pct=float(queda),
                teatro=(atraso > 0 and queda < 0.20))


def ajuste_fragil(conn, p):
    """
    #5 — O agente duvidando do próprio número. Se a distribuição ajustada aos dados passa
    mal no teste KS, o P80 e o VPL simulados DAQUELE projeto não merecem fé. Nenhuma
    ferramenta comercial diz isso. Dizer vende mais confiança do que esconder.
    """
    r = conn.execute(
        "SELECT distribuicao, ks_pvalue FROM mc_ajuste_distribuicao "
        "WHERE project_name=? AND rank_=1 ORDER BY ks_pvalue ASC LIMIT 1", (p,)).fetchone()
    if not r:
        return None
    return dict(dist=r[0], p=float(r[1]), fragil=float(r[1]) < P_AJUSTE_MIN)


def reaprender(pesos, valores, escolhida_ant):
    """
    O reforço. Duas regras que impedem o agente de aprender bobagem:

    1. Só a alavanca RECOMENDADA no ciclo anterior é avaliada — ele responde pelo que
       mandou fazer, e não leva crédito pelo que o acaso melhorou.
    2. BANDA MORTA: variação relativa abaixo de BANDA_MORTA é ruído, não resultado.
       Sem isso, reprocessar o mesmo dado (ou um jitter de 0,1%) punia a alavanca — e o
       peso caía de 1,00 para 0,80 sem que nada tivesse acontecido no projeto.

    Devolve True (acerto), False (erro) ou None (neutro: sem baseline ou sem sinal).
    """
    if not escolhida_ant:
        return None
    st = pesos[escolhida_ant]
    novo = valores[escolhida_ant]
    if st["ant"] is None:
        st["ant"] = novo
        return None

    base = max(abs(st["ant"]), 1e-9)
    delta_rel = (st["ant"] - novo) / base          # positivo = melhorou
    if abs(delta_rel) < BANDA_MORTA:               # nada material aconteceu: não aprende
        return None

    melhorou = delta_rel > 0
    st["peso"] = float(np.clip(st["peso"] * (REFORCO_ACERTO if melhorou else REFORCO_ERRO),
                               PESO_MIN, PESO_MAX))
    st["acertos" if melhorou else "erros"] += 1
    st["ant"] = novo
    return melhorou


def confianca(st):
    n = st["acertos"] + st["erros"]
    if n < 2:
        return "baixa"
    return "alta" if (st["acertos"] / n) >= 0.66 and n >= 3 else "média"


def escolha_anterior(conn, p):
    r = conn.execute("SELECT causa_raiz FROM pm_agent_feedback WHERE project_name=? "
                     "ORDER BY ciclo DESC LIMIT 1", (p,)).fetchone()
    if not r:
        return None
    return next((k for k, v in ALAVANCAS.items() if v["nome"] == r[0]), None)


def veredito_texto(conn, p, alav, danos, valores, cod, fit):
    """A frase conclusiva: começa pela corrente causal, que é o que ninguém mais tem."""
    c = conn.execute(
        "SELECT ks_max, risco_prob_base, risco_prob_nova, p80_base, p80_novo, "
        "       dias_perdidos, custo_atraso FROM cadeia_causal WHERE project_name=?", (p,)).fetchone()
    if c and c[5] > 0.05:
        corrente = (f"O modelo derivou (KS {c[0]:.2f}); isso empurrou o risco de qualidade de "
                    f"{c[1]} para {c[2]}, moveu o P80 de {c[3]:.1f} para {c[4]:.1f} dias "
                    f"(+{c[5]:.1f}) e já custou R$ {c[6]:,.0f}. ")
    else:
        corrente = "A deriva do modelo não cobrou prazo neste ciclo (custo do atraso = R$ 0). "

    a = ALAVANCAS[alav]
    txt = (corrente + f"Varrendo as {len(ALAVANCAS)} dimensões do projeto, o maior dano hoje está em "
           f"**{a['dimensao'].upper()}** — {a['nome'].lower()}: R$ {danos[alav]:,.0f} "
           f"a um custo de atraso de R$ {cod:,.0f}/dia.")

    # #5 — a dúvida honesta. Se o ajuste é ruim, eu aviso ANTES que você decida com meu número.
    if fit and fit["fragil"]:
        txt += (f" ⚠️ **Ressalva de integridade:** o ajuste {fit['dist']} aos dados deste projeto "
                f"passa mal no teste KS (p={fit['p']:.4f}). O P80 e o VPL simulados aqui são "
                f"**frágeis** — trate-os como ordem de grandeza, não como compromisso, até "
                f"recoletar dados.")
    return txt


def acao_texto(conn, p, alav, valores):
    """A ação genérica da alavanca, ESPECIALIZADA com o que este projeto tem de concreto."""
    a = ALAVANCAS[alav]
    txt = a["acao"]

    # #2 — nomeia a tarefa que dá alavancagem e denuncia a armadilha do Gantt determinístico.
    if alav in ("prazo", "drift"):
        t = tarefa_culpada(conn, p)
        if t:
            txt += (f" Comece por **{t['nome']}** ({t['dur']:.1f} dias, crítica em "
                    f"{t['crit']:.0f}% das simulações): entre as tarefas do caminho crítico é a "
                    f"mais longa, e portanto a única com o que comprimir.")
            if t["trap"]:
                q = t["trap"]
                txt += (f" ⚠️ E vigie **{q['nome']}**: o Gantt determinístico lhe dá "
                        f"{q['folga']:.1f} dia(s) de folga — o seu MS Project diria que ela pode "
                        f"esperar — mas ela decide a data em {q['crit']:.0f}% das simulações. "
                        f"É uma **armadilha**, e só a simulação a enxerga.")

    # 💰 ORÇAMENTO — a cota é fatiada de um pool FINITO. Estourar não é "gastar mais":
    # é TOMAR de outro projeto do portfólio. Nenhuma ferramenta do mercado diz isso.
    if alav in ("tokens", "custo", "desperdicio"):
        o = conn.execute(
            "SELECT cota_tokens, consumo_tokens, excedente, excedente_brl, n_portfolio "
            "FROM orcamento_cota WHERE project_name=?", (p,)).fetchone()
        if o and o[2] > 0:
            txt += (f" 💰 Este projeto estourou a **cota do pool global**: consumiu "
                    f"{o[1]:,} de {o[0]:,} tokens/mês (**{o[1]/o[0]:.0%}**). O excedente de "
                    f"{o[2]:,} tokens (R$ {o[3]:,.0f}/mês) **não vem do nada — vem dos outros "
                    f"{o[4]-1} projetos do portfólio**.")
        r = conn.execute(
            "SELECT papel, subsidio_brl, eficiencia FROM orcamento_rateio WHERE project_name=?",
            (p,)).fetchone()
        if r and r[0] == "SUBSIDIADO":
            txt += (f" E o rateio confirma: ele é **SUBSIDIADO** em R$ {r[1]:,.0f}/mês — consome "
                    f"mais do pool do que o valor que devolve (eficiência: {r[2]:.0f} de EV por "
                    f"milhão de tokens).")

    # #3 — nomeia o erro que mais queima token.
    if alav in ("desperdicio", "tokens", "custo"):
        e = conn.execute(
            "SELECT tipo_erro, SUM(tokens_desperdicados) FROM alertas_criticos "
            "WHERE project_name=? GROUP BY tipo_erro ORDER BY 2 DESC LIMIT 1", (p,)).fetchone()
        if e and e[1]:
            txt += (f" O maior ralo é **{e[0]}**: {e[1]:,.0f} tokens queimados em chamadas que "
                    f"nem entregaram resposta.")

    # #4 — denuncia o teatro de mitigação.
    if alav == "risco":
        t = teatro_mitigacao(conn, p)
        if t and t["teatro"]:
            txt += (f" ⚠️ E a exposição **não está queimando**: caiu só {t['queda_pct']:.0%} e "
                    f"segue {t['acima_do_ideal']:.0f} ponto(s) acima da linha ideal do burndown. "
                    f"Mitigação que não derruba a exposição é teatro — cobre o dono do risco.")
    return f"{txt} (dono: {a['dono']})"


def aprendizado_texto(pesos, melhorou, ant):
    if ant is None:
        return (f"Primeiro ciclo deste projeto: as {len(ALAVANCAS)} alavancas começam com peso "
                f"igual. A partir daqui o agente passa a se especializar **neste** projeto.")
    st, nome = pesos[ant], ALAVANCAS[ant]["nome"].lower()
    if melhorou is None:
        return (f"**{nome.capitalize()}** não se mexeu de forma material desde o último ciclo "
                f"(variação < {BANDA_MORTA:.0%}) — o agente **não aprende com ruído**: o peso "
                f"segue em {st['peso']:.2f} até haver sinal de verdade.")
    if melhorou:
        return (f"No ciclo passado recomendei **{nome}** e a métrica-alvo **melhorou** → peso desta "
                f"alavanca sobe para {st['peso']:.2f} ({st['acertos']}✓/{st['erros']}✗). "
                f"Neste projeto, essa alavanca funciona.")
    return (f"No ciclo passado recomendei **{nome}** e a métrica-alvo **não melhorou** → peso cai "
            f"para {st['peso']:.2f} ({st['acertos']}✓/{st['erros']}✗). Neste projeto ela não move o "
            f"ponteiro; priorizo outra dimensão.")


def avaliar_tolerancias(conn, p, valores):
    """
    PRINCE2 — compara a PREVISÃO de cada dimensão contra a tolerância acordada.
    Devolve a lista de dimensões e quais estouraram.
    """
    cr = conn.execute("SELECT p80, prazo_alvo FROM mc_cronograma WHERE project_name=?",
                      (p,)).fetchone() or (0.0, 0.0)
    ev = conn.execute("SELECT eac, bac FROM evm_indices WHERE project_name=?",
                      (p,)).fetchone() or (0.0, 0.0)

    # risco — a classificação é do PRÓPRIO registro, não minha.
    criticos = conn.execute(
        "SELECT COUNT(*) FROM risco_registro WHERE project_name=? AND LOWER(nivel)='critico' "
        "AND LOWER(status) IN ('aberto','mitigando')", (p,)).fetchone()[0]

    # qualidade — regressão contra a BASELINE do próprio projeto (os 3 primeiros dias),
    # não contra um teto que eu tenha escolhido. É o espírito do DORA: o que importa é a
    # PIORA, não o nível absoluto (que varia enormemente por tipo de tarefa).
    dias = conn.execute(
        "SELECT taxa_erro FROM exec_qualidade_tempo WHERE project_name=? ORDER BY dia", (p,)
    ).fetchall()
    if len(dias) >= 6:
        base_q = sum(d[0] for d in dias[:3]) / 3.0
        atual_q = sum(d[0] for d in dias[-3:]) / 3.0
    else:
        base_q = atual_q = valores["qualidade"]

    # tokens — a cota vem do POOL GLOBAL, não do próprio consumo. É o recurso mais escasso
    # do portfólio: estourar aqui é tomar capacidade dos outros projetos.
    oc = conn.execute("SELECT consumo_tokens, cota_tokens FROM orcamento_cota "
                      "WHERE project_name=?", (p,)).fetchone() or (0.0, 0.0)

    plano = {
        "prazo":     (cr[0], cr[1] * (1 + TOL_FOLGA)),
        "custo":     (ev[0], ev[1] * (1 + TOL_FOLGA)),
        "risco":     (float(criticos), float(TOL_CRITICOS_ABERTOS)),
        "qualidade": (atual_q, base_q * TOL_REGRESSAO_QUAL),
        "roi":       (valores["roi"], TOL_ROI_PNEG),
        "tokens":    (oc[0], oc[1] * TOL_COTA),
    }

    out = []
    for k, cfg in TOLERANCIAS.items():
        prev, lim = (float(x or 0.0) for x in plano[k])
        folga = ((lim - prev) / lim) if lim else 0.0
        out.append(dict(alavanca=k, dimensao=cfg["dimensao"], metrica=cfg["metrica"],
                        previsto=prev, limite=lim, unidade=cfg["unidade"],
                        estourou=1 if prev > lim else 0, folga_pct=float(folga)))
    return out


def exception_report(conn, p, tols, zona, alav, danos, cod):
    """
    O Exception Report do PRINCE2: causa, impacto, OPÇÕES e recomendação. O que o diferencia
    de um alerta é justamente a linha das **opções** — escalar sem oferecer alternativas é
    empurrar o problema para cima, não gerenciar.
    """
    estouros = [t for t in tols if t["estourou"]]
    nomes = ", ".join(f"**{t['dimensao']}** (previsto {t['previsto']:,.1f} "
                      f"vs tolerância {t['limite']:,.1f} {t['unidade']})" for t in estouros)
    a = ALAVANCAS[alav]

    causa = (f"Tolerância estourada em: {nomes}." if estouros else
             f"Nenhuma tolerância estourada, mas o buffer do cronograma está em **{zona}** "
             f"no fever chart — o consumo de buffer não acompanha o avanço da cadeia.")
    impacto = (f"Ao ritmo atual, o dano da dimensão crítica ({a['dimensao']}) é de "
               f"R$ {danos[alav]:,.0f}, a um custo de atraso de R$ {cod:,.0f} por dia parado.")

    r = conn.execute("SELECT reserva_gerencial, contingencia FROM reserva_analise "
                     "WHERE project_name=?", (p,)).fetchone() or (0.0, 0.0)
    opcoes = (
        f"**(a) Absorver** — consumir a reserva gerencial de {r[0]:.1f} dia(s) e manter escopo "
        f"e data; só funciona se a causa for pontual, e queima o colchão do P95.  "
        f"**(b) Recuperar** — executar a ação recomendada abaixo e comprimir o caminho crítico; "
        f"custa esforço do time, preserva a data.  "
        f"**(c) Renegociar** — mover a data para o novo P80 ou cortar escopo; é a única opção "
        f"honesta se a tolerância estourou por mudança estrutural, e não por execução.")
    recom = (f"Recomendo **(b) Recuperar**, atacando {a['dimensao'].lower()} — é onde está o "
             f"maior dano×peso deste projeto. Se em um ciclo a métrica-alvo não ceder, "
             f"escale para **(c)**: insistir sem resultado é como o projeto perde a data "
             f"duas vezes.")
    return (f"**CAUSA.** {causa}\n\n**IMPACTO.** {impacto}\n\n**OPÇÕES.** {opcoes}\n\n"
            f"**RECOMENDAÇÃO.** {recom}")


def perfil_texto(conn, p, pesos):
    """O retrato taylor-made: como ESTE projeto respondeu — mais a verdade sobre o VPL."""
    sc, st = sensibilidade(conn, p)
    ord_ = sorted(ALAVANCAS, key=lambda k: -pesos[k]["peso"])
    top = " · ".join(f"{ALAVANCAS[k]['dimensao']} {pesos[k]['peso']:.2f}" for k in ord_[:4])
    n = sum(s["acertos"] + s["erros"] for s in pesos.values())

    txt = (f"Após {n} ciclo(s) com resultado medido, o perfil aprendido deste projeto é: {top}. "
           f"Os pesos partem todos de 1.00 e só se movem com resultado real — não há palpite "
           f"embutido.")
    # A frase que o instinto de corte de custo não quer ouvir.
    if sc < 0.10:
        txt += (f" 📌 E um aviso contraintuitivo: **{st:.0%} da variância do VPL deste projeto vem "
                f"dos fluxos de receita, e apenas {sc:.0%} do custo de token**. Espremer token aqui "
                f"não move o VPL — ataque a receita e a data. Corte custo por disciplina de caixa, "
                f"nunca esperando que o retorno mude.")
    return txt


def processar(conn, p):
    valores, dias_eq, danos, cod = medir(conn, p)
    pesos = carregar_pesos(conn, p)
    ant = escolha_anterior(conn, p)
    melhorou = reaprender(pesos, valores, ant)
    fit = ajuste_fragil(conn, p)

    prior = {k: danos[k] * pesos[k]["peso"] for k in ALAVANCAS}
    alav = max(prior, key=prior.get) if any(v > 0 for v in prior.values()) else "fluxo"

    if pesos[alav]["ant"] is None:
        pesos[alav]["ant"] = valores[alav]

    # A confiança NUNCA é "alta" se o ajuste da distribuição não passa no KS: o número que
    # sustenta a recomendação é frágil, e fingir convicção aqui seria desonesto.
    conf = confianca(pesos[alav])
    if fit and fit["fragil"] and conf == "alta":
        conf = "média"

    # ── PRINCE2 + CCPM: o agente só ESCALA se a previsão estourar a tolerância OU se o
    # buffer sair do verde. Caso contrário ele registra "NORMAL" e **cala a boca**.
    tols = avaliar_tolerancias(conn, p, valores)
    zr = conn.execute("SELECT zona FROM buffer_fever WHERE project_name=?", (p,)).fetchone()
    zona = zr[0] if zr else "VERDE"
    estourou = any(t["estourou"] for t in tols)
    status = "EXCECAO" if (estourou or zona != "VERDE") else "NORMAL"

    cur = conn.cursor()
    for k, s in pesos.items():
        cur.execute("INSERT OR REPLACE INTO pm_agent_pesos VALUES (?,?,?,?,?,?)",
                    (p, k, s["peso"], s["acertos"], s["erros"], s["ant"]))

    r = cur.execute("SELECT MAX(ciclo) FROM pm_agent_feedback WHERE project_name=?", (p,)).fetchone()
    ciclo = (r[0] or 0) + 1
    a = ALAVANCAS[alav]

    for t in tols:
        cur.execute("INSERT OR REPLACE INTO pm_agent_tolerancia VALUES (?,?,?,?,?,?,?,?,?)",
                    (p, ciclo, t["dimensao"], t["metrica"], t["previsto"], t["limite"],
                     t["unidade"], t["estourou"], t["folga_pct"]))

    if status == "EXCECAO":
        vered = veredito_texto(conn, p, alav, danos, valores, cod, fit)
        acao = acao_texto(conn, p, alav, valores)
        exc = exception_report(conn, p, tols, zona, alav, danos, cod)
        impacto = float(danos[alav])
    else:
        folga_min = min(tols, key=lambda t: t["folga_pct"])
        vered = (f"✅ **Nada a escalar.** As {len(tols)} tolerâncias acordadas estão respeitadas e "
                 f"o buffer do cronograma está **VERDE** no fever chart. A dimensão mais próxima "
                 f"do limite é **{folga_min['dimensao']}**, ainda com {folga_min['folga_pct']:.0%} "
                 f"de folga. O agente registra o ciclo e **não pede nada de você** — é assim que "
                 f"ele ganha o direito de ser ouvido quando de fato houver o que dizer.")
        acao = (f"Manter o curso. Vigiar **{folga_min['dimensao']}**, que é o que chega primeiro "
                f"à tolerância. (dono: {a['dono']})")
        exc = ""
        impacto = 0.0

    cur.execute("INSERT OR REPLACE INTO pm_agent_feedback VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (p, ciclo, vered, a["dimensao"], a["nome"], acao, a["pratica"], impacto, conf,
                 aprendizado_texto(pesos, melhorou, ant), perfil_texto(conn, p, pesos),
                 status, zona, exc))

    cur.execute("DELETE FROM pm_agent_radar WHERE project_name=? AND ciclo=?", (p, ciclo))
    for k, v in ALAVANCAS.items():
        cur.execute("INSERT INTO pm_agent_radar VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                    (p, ciclo, k, v["dimensao"], v["metrica"], valores[k], dias_eq[k],
                     danos[k], pesos[k]["peso"], prior[k], 1 if k == alav else 0))
    conn.commit()
    return ciclo, alav, impacto, conf, pesos[alav]["peso"], status, zona


def main():
    init_schema()
    conn = get_conn()
    projetos = [r[0] for r in conn.execute(
        "SELECT DISTINCT project_name FROM cadeia_causal ORDER BY project_name")]
    print(f"🤖 Project Manager Agent — {len(ALAVANCAS)} dimensões × {len(projetos)} projetos")
    n_calado = 0
    for p in projetos:
        ciclo, alav, dano, conf, peso, status, zona = processar(conn, p)
        a = ALAVANCAS[alav]
        if status == "NORMAL":
            print(f"   {p:<12} ciclo {ciclo} → 🟢 NORMAL   buffer {zona:<8} "
                  f"— dentro das tolerâncias, NADA A ESCALAR")
            n_calado += 1
        else:
            print(f"   {p:<12} ciclo {ciclo} → 🔴 EXCEÇÃO  buffer {zona:<8} "
                  f"[{a['dimensao']}] {a['nome']} · R$ {dano:,.0f} · conf. {conf}")
    conn.close()
    print(f"✅ PM Agent: {n_calado}/{len(projetos)} projetos sem nada a escalar — "
          f"o agente calou onde não havia o que dizer (PRINCE2 management by exception).")


if __name__ == "__main__":
    main()
