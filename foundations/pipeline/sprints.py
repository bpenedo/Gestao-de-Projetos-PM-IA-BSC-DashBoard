"""
🏃 SPRINTS — o debate do progresso que o Project Manager Agent leva para a weekly de sexta.

A sprint NÃO é inventada aqui. Ela é o **período do EVM** — a cadência que o projeto já tem,
com PV/EV/AC reais. Sprint passada tem EV e AC (o que aconteceu); sprint futura tem só PV
(o plano). Inventar um calendário de sprint paralelo ao cronograma seria criar uma segunda
verdade sobre o mesmo projeto, e duas verdades é o mesmo que nenhuma.

AS TRÊS MÉTRICAS QUE ABREM A DISCUSSÃO NA SEXTA:

  1. SAY-DO RATIO = entregue ÷ comprometido  (ΔEV ÷ ΔPV)
     Um time com say-do 0,7 **não é lento**: ele está *prometendo 30% a mais do que
     consegue*. O remédio é diferente — não se conserta capacidade com cobrança, se
     conserta compromisso com previsibilidade. É a métrica que muda o tom da reunião.

  2. CPI DA SPRINT (local) = entregue ÷ custo NAQUELA sprint
     Separado do CPI acumulado DE PROPÓSITO: o acumulado é uma média, e média **esconde**
     a sprint ruim recente. Um CPI acumulado de 1,05 pode abrigar uma última sprint a 0,6.
     O local denuncia; o acumulado consola.

  3. PREVISÃO POR VELOCIDADE = trabalho restante ÷ velocidade média das últimas 3
     Compara com quantas sprints ainda existem no plano. Se o time precisa de 6 e só
     restam 4, a data já morreu — e ninguém percebeu, porque o burndown acumulado
     ainda "parece" perto do ideal.

⚠️ CONFORMIDADE — o que isto É e o que NÃO É (triple-check contra o Scrum Guide 2020):

  ① "Velocity" e "burndown chart" **NÃO constam do Scrum Guide**. São prática de mercado
     consagrada — ágil praticado —, não artefato oficial de Scrum. Chamá-los de "conformes
     ao Scrum" seria falso, e aqui não se vende etiqueta que o material não sustenta.

  ② O Scrum Guide trocou o "commitment" do Sprint Backlog pelo **Sprint Goal**, e chama o
     Sprint Backlog de **forecast** (previsão), não de compromisso. Logo "say-do ratio
     (entregue ÷ comprometido)" é vocabulário da INDÚSTRIA, não de Scrum canônico. A
     métrica é útil e defensável; a etiqueta "Scrum" é que seria mentira.

  ③ A "sprint" daqui é o **período do EVM**: não há Sprint Goal, nem Sprint Review, nem
     Retrospective, nem time auto-gerenciado se comprometendo. É uma **cadência de medição**
     com métricas de inspiração ágil — e não uma Sprint de Scrum. Dizer o contrário
     enganaria quem tem a certificação e não ajudaria quem não tem.

  O que ISTO é, com precisão: **relatório de progresso por cadência, com base em EVM
  (ANSI/EIA-748) e métricas de fluxo de inspiração ágil.** É honesto, é útil, e é auditável.

Uso:  python3 sprints.py
Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026.
"""
from db import get_conn, init_schema

JANELA_VELOCIDADE = 3     # média móvel das últimas N sprints concluídas
SAY_DO_ALVO = 0.85        # abaixo disto o time promete mais do que entrega
SAY_DO_TETO = 1.15        # ACIMA disto o problema não é o time — é o plano (linha de base furada)


def montar_sprints(conn, p):
    serie = conn.execute(
        "SELECT periodo, pv, ev, ac FROM evm_serie WHERE project_name=? ORDER BY periodo",
        (p,)).fetchall()
    idx = conn.execute(
        "SELECT bac, at_periodo, pd FROM evm_indices WHERE project_name=?", (p,)).fetchone()
    if not serie or not idx:
        return []
    bac, at, pd = idx

    out = []
    for i in range(1, len(serie)):
        per, pv, ev, ac = serie[i]
        pv0, ev0, ac0 = serie[i - 1][1], serie[i - 1][2], serie[i - 1][3]
        d_pv = (pv or 0) - (pv0 or 0)
        d_ev = ((ev - ev0) if (ev is not None and ev0 is not None) else None)
        d_ac = ((ac - ac0) if (ac is not None and ac0 is not None) else None)

        status = "CONCLUIDA" if per < at else ("ATUAL" if per == at else "FUTURA")
        say_do = (d_ev / d_pv) if (d_ev is not None and d_pv) else None
        cpi_s = (d_ev / d_ac) if (d_ev is not None and d_ac) else None
        restante = (bac - ev) if ev is not None else None
        restante_ideal = bac - (pv or 0)

        out.append(dict(sprint=per, status=status, comprometido=d_pv, entregue=d_ev,
                        custo=d_ac, say_do=say_do, cpi_sprint=cpi_s,
                        restante=restante, restante_ideal=restante_ideal))
    return out


def pauta_da_weekly(conn, p, sp):
    """
    A pauta do Project Manager Agent para a sexta. Uma linha = um ponto de debate, com o
    NÚMERO na frente. Reunião sem número é opinião, e opinião não muda projeto.
    """
    idx = conn.execute(
        "SELECT bac, at_periodo, pd, cpi, spi_t FROM evm_indices WHERE project_name=?",
        (p,)).fetchone()
    if not idx:
        return []
    bac, at, pd, cpi_acum, spi_t = idx
    feitas = [s for s in sp if s["entregue"] is not None and s["comprometido"]]
    if not feitas:
        return []

    pauta = []
    ult = feitas[-JANELA_VELOCIDADE:]
    velocidade = sum(s["entregue"] for s in ult) / len(ult)

    # 1 — SAY-DO RATIO
    say = [s["say_do"] for s in ult if s["say_do"] is not None]
    if say:
        m = sum(say) / len(say)
        if m < SAY_DO_ALVO:
            pauta.append(("Say-do ratio",
                          f"Nas últimas {len(say)} sprints o time entregou **{m:.0%}** do que "
                          f"se comprometeu a entregar. Isso **não é lentidão** — é compromisso "
                          f"acima da capacidade. O debate de sexta não é 'corram mais', é "
                          f"'prometam {1 - m:.0%} a menos e cumpram'.", "🔴" if m < 0.7 else "🟡"))
        elif m > SAY_DO_TETO:
            # Entregar MUITO acima do combinado não é virtude — é linha de base errada.
            # Sem esta guarda, o agente parabenizava um time cujo PLANO estava furado, e o
            # planejamento continuava mentindo em silêncio.
            pauta.append(("Say-do ratio — a linha de base está errada",
                          f"O time entregou **{m:.0%}** do comprometido. Entregar {m - 1:.0%} "
                          f"**acima** do plano não é heroísmo: é **linha de base furada**. O PV "
                          f"está subestimando o que o time faz, e um plano que erra para menos "
                          f"erra para mais em outro lugar — provavelmente no fim. Rebaselinar "
                          f"antes que a folga vire dívida.", "🟡"))
        else:
            pauta.append(("Say-do ratio",
                          f"O time entregou **{m:.0%}** do comprometido nas últimas "
                          f"{len(say)} sprints. Compromisso e capacidade estão calibrados — "
                          f"pode planejar em cima disso.", "🟢"))

    # 2 — O CPI DA SPRINT QUE O ACUMULADO ESCONDE
    ultima = feitas[-1]
    if ultima["cpi_sprint"] and cpi_acum:
        loc, acu = ultima["cpi_sprint"], cpi_acum
        if loc < 0.9 <= acu:
            pauta.append(("Custo — o que a média esconde",
                          f"O CPI **acumulado** é {acu:.2f} e parece saudável, mas o CPI **da "
                          f"última sprint** foi {loc:.2f}. A média está consolando vocês: a "
                          f"sprint passada queimou caixa acima do valor que entregou. "
                          f"Debater o que mudou **nesta** sprint, não no projeto todo.", "🔴"))
        elif loc < 0.9:
            pauta.append(("Custo", f"CPI da última sprint em {loc:.2f} (acumulado {acu:.2f}): "
                                   f"o custo por unidade de valor entregue piorou.", "🟡"))
        else:
            pauta.append(("Custo", f"CPI da última sprint em {loc:.2f} — o custo acompanha o "
                                   f"valor entregue.", "🟢"))

    # 3 — PREVISÃO POR VELOCIDADE (a data que já morreu e ninguém viu)
    # EV acumulado = soma das entregas das sprints concluídas.
    restante = max(0.0, bac - sum(s["entregue"] for s in feitas))
    if velocidade > 0:
        precisa = restante / velocidade
        restam = max(0, pd - at)
        if precisa > restam:
            pauta.append(("Previsão por velocidade",
                          f"Sobram **{restante:,.0f}** de valor a entregar. Na velocidade das "
                          f"últimas {len(ult)} sprints (**{velocidade:,.0f}/sprint**), isso exige "
                          f"**{precisa:.1f} sprints** — mas só restam **{restam}** no plano. "
                          f"A data já não fecha: ou entra escopo a menos, ou entra sprint a "
                          f"mais. Decidir **nesta sexta**, não na última.", "🔴"))
        else:
            pauta.append(("Previsão por velocidade",
                          f"Restam {restante:,.0f} de valor. Na velocidade atual "
                          f"({velocidade:,.0f}/sprint) isso leva **{precisa:.1f} sprints**, e há "
                          f"**{restam}** no plano. A data fecha com folga de "
                          f"{restam - precisa:.1f} sprint(s).", "🟢"))

    # 4 — 💰 O ORÇAMENTO DE TOKENS. Monitorado TODA weekly, porque o pool é finito e o
    # estouro de um é o estrangulamento de outro. Isto não é "custo": é capacidade tomada.
    o = conn.execute(
        "SELECT cota_tokens, consumo_tokens, excedente, excedente_brl, n_portfolio "
        "FROM orcamento_cota WHERE project_name=?", (p,)).fetchone()
    r = conn.execute(
        "SELECT papel, subsidio_brl, eficiencia, desperdicio_tok, desperdicio_brl "
        "FROM orcamento_rateio WHERE project_name=?", (p,)).fetchone()
    if o and r:
        cota, cons, exc, exc_brl, n_port = o
        papel, sub, efic, desp_t, desp_brl = r
        if exc > 0:
            pauta.append(("Orçamento de tokens — o pool é de todos",
                          f"Consumo de **{cons:,}** tokens/mês contra uma cota de **{cota:,}** "
                          f"(**{cons/cota:.0%}**). O excedente de {exc:,} tokens "
                          f"(**R$ {exc_brl:,.0f}/mês**) **não vem do nada — vem dos outros "
                          f"{n_port-1} projetos**. E {desp_t:,} desses tokens "
                          f"(R$ {desp_brl:,.0f}) foram queimados em chamadas que **falharam**. "
                          f"Debater na sexta: cortar o desperdício antes de pedir mais cota.",
                          "🔴" if cons/cota > 1.5 else "🟡"))
        elif papel == "PAGADOR":
            pauta.append(("Orçamento de tokens — este projeto banca os outros",
                          f"Consumo em {cons/cota:.0%} da cota e eficiência de **{efic:.0f} de EV "
                          f"por milhão de tokens** — este projeto **paga R$ {abs(sub):,.0f}/mês** "
                          f"de subsídio cruzado para quem consome mais do que entrega. "
                          f"É o projeto mais barato do portfólio; proteja-o.", "🟢"))
        else:
            pauta.append(("Orçamento de tokens",
                          f"Consumo em {cons/cota:.0%} da cota do pool ({cons:,} de {cota:,}). "
                          f"Dentro do orçamento global.", "🟢"))

    # 4b — 🔁 O LOOP FECHADO: o agente presta contas do corte que ELE mandou fazer.
    lp = conn.execute(
        "SELECT veredito, acao, confianca, liberou_brl, whatif_brl, acertos, erros "
        "FROM pm_agent_orcamento WHERE project_name=? ORDER BY ciclo DESC LIMIT 1", (p,)).fetchone()
    if lp:
        vered, acao, conf, liberou, whatif, ac, er = lp
        if vered == "funcionou":
            pauta.append(("Loop de orçamento — o corte funcionou",
                          f"Na weekly passada mandei **{acao}**; o desperdício caiu e liberou "
                          f"**R$ {liberou:,.0f}/mês** de pool. **Subo a confiança** nessa recomendação "
                          f"({ac}✓/{er}✗). Manter o corte.", "🟢"))
        elif vered == "nao_funcionou":
            pauta.append(("Loop de orçamento — o corte NÃO pegou",
                          f"Na weekly passada mandei **{acao}** e o desperdício **não caiu** — "
                          f"**baixo a confiança** ({ac}✓/{er}✗). Debater por que o corte não landou "
                          f"antes de repeti-lo.", "🔴"))
        elif vered == "baseline":
            pauta.append(("Loop de orçamento — baseline registrada",
                          f"Recomendo **{acao}** e guardo o desperdício de hoje. What-if: o corte "
                          f"liberaria **R$ {whatif:,.0f}/mês** de pool. Cobro a mim mesmo na próxima "
                          f"weekly.", "🟡"))
        else:  # sem_sinal
            pauta.append(("Loop de orçamento — sem sinal material",
                          f"O desperdício não se mexeu desde o último corte recomendado — não aprendo "
                          f"com ruído. Confiança inalterada ({ac}✓/{er}✗).", "🟢"))

    # 5 — A ESCALAÇÃO DO AGENTE (PRINCE2): só entra na pauta se houver exceção
    fb = conn.execute(
        "SELECT status, dimensao, causa_raiz, acao, zona_buffer FROM pm_agent_feedback "
        "WHERE project_name=? ORDER BY ciclo DESC LIMIT 1", (p,)).fetchone()
    if fb and fb[0] == "EXCECAO":
        pauta.append((f"Exceção — {fb[1]}",
                      f"O agente escala **{fb[2]}** (buffer do cronograma: {fb[4]}). {fb[3]}",
                      "🔴"))
    elif fb:
        pauta.append(("Sem exceções",
                      "Todas as tolerâncias acordadas estão respeitadas e o buffer do "
                      "cronograma está verde. **Nada a escalar** — a sexta pode ser curta.",
                      "🟢"))
    return pauta


def main():
    init_schema()
    conn = get_conn()
    cur = conn.cursor()
    projetos = [r[0] for r in conn.execute(
        "SELECT DISTINCT project_name FROM evm_serie ORDER BY project_name")]
    print(f"🏃 Sprints + pauta da weekly — {len(projetos)} projetos")
    for p in projetos:
        sp = montar_sprints(conn, p)
        for s in sp:
            cur.execute("INSERT OR REPLACE INTO sprints VALUES (?,?,?,?,?,?,?,?,?,?)",
                        (p, s["sprint"], s["status"], s["comprometido"], s["entregue"],
                         s["custo"], s["say_do"], s["cpi_sprint"], s["restante"],
                         s["restante_ideal"]))
        pauta = pauta_da_weekly(conn, p, sp)
        cur.execute("DELETE FROM sprint_debate WHERE project_name=?", (p,))
        for i, (tema, ponto, sev) in enumerate(pauta, 1):
            cur.execute("INSERT INTO sprint_debate VALUES (?,?,?,?,?)", (p, i, tema, ponto, sev))
        feitas = [s for s in sp if s["status"] == "CONCLUIDA"]
        say = [s["say_do"] for s in feitas if s["say_do"]]
        m = (sum(say) / len(say)) if say else 0
        n_red = sum(1 for _, _, s in pauta if s == "🔴")
        print(f"   {p:<12} {len(sp)} sprints ({len(feitas)} concluídas) · say-do médio "
              f"{m:>5.0%} · pauta: {len(pauta)} pontos ({n_red} 🔴)")
    conn.commit()
    conn.close()
    print("✅ Sprints e pauta da weekly prontas — o debate de sexta agora tem número.")


if __name__ == "__main__":
    main()
