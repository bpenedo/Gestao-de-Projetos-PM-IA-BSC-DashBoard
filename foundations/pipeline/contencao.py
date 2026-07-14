"""
🔒 CONTENÇÃO DE RECURSO PRECIFICADA — a cadeia causal aplicada ao PORTFÓLIO.

A cadeia causal original liga, DENTRO de um projeto:
    token que derivou → risco → prazo (P80) → dinheiro (Cost of Delay).

Isto liga ENTRE projetos:
    excedente de um → exaustão do pool → estrangulamento dos OUTROS
    → o P80 DELES escorrega → o Cost of Delay DELES cobra a conta.

Exige, ao mesmo tempo: FinOps (a quota), EVM (o valor entregue), risco (a exposição) e
cronograma simulado (o P80). É por isso que nenhuma ferramenta do mercado faz — nenhuma tem
os quatro motores juntos. Langfuse vê o token. O Jira vê a tarefa. O CloudZero vê a fatura.
**Nenhum deles consegue dizer que o projeto J está custando R$ X de atraso ao projeto F.**

⚠️ A HONESTIDADE QUE SUSTENTA O NÚMERO
──────────────────────────────────────
Enquanto o consumo total **couber na quota**, NÃO há estrangulamento físico: ninguém para,
ninguém atrasa. O dano é **alocativo** (subsídio cruzado), não **operacional**. Dizer "o J
está atrasando o C" com folga no pool seria **mentira com cara de rigor**.

Por isso este módulo é **CENARIZADO**: ele responde *a partir de que ponto* o pool vira, e
*quanto custa quando virar*. É previsão, e está rotulada como previsão. O cenário mais
importante não é o pessimista — é o **"sem desperdício"**, que mostra quanta capacidade
existe escondida em chamadas que falharam.

Uso:  python3 contencao.py
Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026.
"""
from db import get_conn, init_schema

DIAS_MES = 30.0
CENARIOS = [
    ("atual", 0.00),
    ("+10% de consumo", 0.10),
    ("+25% de consumo", 0.25),
    ("+50% de consumo", 0.50),
]


def _base(conn):
    g = conn.execute(
        "SELECT tokens_contratados, consumo_run_rate, desperdicio_rr, custo_por_mtoken "
        "FROM orcamento_global").fetchone()
    cod = dict(conn.execute("SELECT project_name, cod_dia FROM cadeia_causal"))
    rat = {r[0]: dict(exc=0, efic=r[1], tok=r[2], ev=r[3]) for r in conn.execute(
        "SELECT project_name, eficiencia, tokens_mes, ev FROM orcamento_rateio")}
    for p, exc in conn.execute("SELECT project_name, excedente FROM orcamento_cota"):
        if p in rat:
            rat[p]["exc"] = exc
    return g, cod, rat


def cenarios(conn, g, cod):
    """A que ponto o pool vira — e quanto custa quando virar."""
    quota, consumo, desp, _ = g
    cod_total = sum(cod.values())          # R$/dia de TODO o portfólio parado
    cur = conn.cursor()
    cur.execute("DELETE FROM contencao_cenario")

    linhas = list(CENARIOS) + [("sem desperdício", -desp / consumo if consumo else 0)]
    for nome, cres in linhas:
        c = consumo * (1 + cres)
        dia = (quota / (c / DIAS_MES)) if c else 999.0
        parados = max(0.0, DIAS_MES - dia)
        custo = parados * cod_total

        if nome == "sem desperdício":
            livre = quota - c
            v = (f"Eliminando o desperdício ({desp:,} tokens/mês em chamadas que FALHARAM), o "
                 f"consumo cai para {c:,.0f} — apenas {c/quota:.0%} da quota. Sobram "
                 f"{livre:,.0f} tokens/mês de capacidade **que você já paga e não usa**. "
                 f"É a alavanca mais barata do portfólio: não custa um centavo a mais.")
        elif parados <= 0:
            v = (f"O pool aguenta: exaustão projetada no dia {dia:.1f} de um mês de 30. "
                 f"**Não há estrangulamento físico** — o dano hoje é alocativo (subsídio "
                 f"cruzado), não operacional. Folga de {quota - c:,.0f} tokens.")
        else:
            v = (f"⚠️ O pool SECA no dia {dia:.1f}. O portfólio INTEIRO para por "
                 f"{parados:.1f} dia(s) — inclusive os projetos eficientes, que não causaram "
                 f"o problema. A conta, pelo Cost of Delay somado de todos: "
                 f"**R$ {custo:,.0f}**.")
        cur.execute("INSERT INTO contencao_cenario VALUES (?,?,?,?,?,?,?,?)",
                    (nome, cres, int(c), c / quota, dia, parados, custo, v))
    conn.commit()
    return cod_total


def por_projeto(conn, g, cod, rat, cenario="+25% de consumo"):
    """
    Quem CAUSA e quem SOFRE. No cenário em que o pool seca, TODOS param — inclusive os
    eficientes, que não causaram nada. A culpa é rateada pelo EXCEDENTE de cada um.
    """
    row = conn.execute("SELECT dias_parados FROM contencao_cenario WHERE cenario=?",
                       (cenario,)).fetchone()
    parados = row[0] if row else 0.0
    exc_total = sum(max(0, v["exc"]) for v in rat.values()) or 1

    cur = conn.cursor()
    cur.execute("DELETE FROM contencao_projeto")
    # O dano total do estrangulamento é o CoD somado de todos, pelos dias parados.
    dano_total = parados * sum(cod.values())

    for p, v in rat.items():
        cd = cod.get(p, 0.0)
        sofrido = parados * cd                                    # o que ELE perde
        culpa = dano_total * (max(0, v["exc"]) / exc_total)       # o que ELE causa aos outros
        saldo = culpa - sofrido
        papel = ("ALGOZ" if saldo > dano_total * 0.03 else
                 "VÍTIMA" if saldo < -dano_total * 0.03 else "NEUTRO")
        cur.execute("INSERT INTO contencao_projeto VALUES (?,?,?,?,?,?,?,?)",
                    (p, cd, v["exc"], v["efic"], sofrido, culpa, saldo, papel))
    conn.commit()
    return parados, dano_total


def politica_de_corte(conn, g, rat):
    """
    🪓 Se o portfólio precisa de espaço, QUEM sai?
    A resposta honesta NÃO é "o que gasta mais" — é "o que entrega menos POR TOKEN".
    Cortar por consumo bruto puniria um projeto grande e produtivo. Cortar por eficiência
    (EV ÷ milhão de tokens) libera o máximo de pool ao mínimo custo de valor.
    """
    quota, _, _, por_mtoken = g
    n = len(rat)
    cota_media = quota / n if n else 1
    tot_tok = sum(v["tok"] for v in rat.values()) or 1
    tot_ev = sum(v["ev"] for v in rat.values()) or 1

    cur = conn.cursor()
    cur.execute("DELETE FROM admissao_politica")
    ordem = sorted(rat.items(), key=lambda kv: kv[1]["efic"])     # pior eficiência primeiro
    for i, (p, v) in enumerate(ordem, start=1):
        pct_pool = v["tok"] / tot_tok
        pct_val = v["ev"] / tot_ev
        novos = v["tok"] / cota_media
        if pct_val <= 0.001:
            t = (f"Libera {pct_pool:.1%} do pool e sacrifica ~0% do valor. "
                 f"**Corte óbvio.**")
        else:
            razao = pct_pool / pct_val
            t = (f"Libera **{pct_pool:.1%} do pool** e sacrifica **{pct_val:.1%} do valor** "
                 f"(razão {razao:.1f}×). Abre espaço para **{novos:.1f} projeto(s) novo(s)** "
                 f"sem diluir ninguém." if razao > 1.3 else
                 f"Libera {pct_pool:.1%} do pool mas sacrifica {pct_val:.1%} do valor "
                 f"(razão {razao:.1f}×). **Cortar aqui destrói mais valor do que libera "
                 f"capacidade — não corte.**")
        cur.execute("INSERT INTO admissao_politica VALUES (?,?,?,?,?,?,?,?,?)",
                    (p, i, v["efic"], v["tok"], pct_pool, v["ev"], pct_val, novos, t))
    conn.commit()
    return ordem


def main():
    init_schema()
    conn = get_conn()
    g, cod, rat = _base(conn)
    if not g:
        print("⚠️ rode orcamento.py antes"); return
    quota, consumo, desp, _ = g

    cod_total = cenarios(conn, g, cod)
    print("🔒 CONTENÇÃO DE RECURSO — a cadeia causal aplicada ao PORTFÓLIO")
    print(f"   quota {quota:,} · consumo {consumo:,} · CoD somado do portfólio: "
          f"R$ {cod_total:,.0f}/dia parado\n")
    print(f"   {'cenário':<20}{'consumo/mês':>14}{'% quota':>9}{'exaustão':>10}"
          f"{'dias parados':>14}{'custo (CoD)':>14}")
    for r in conn.execute("SELECT cenario,consumo_mes,pct_quota,dia_exaustao,dias_parados,"
                          "custo_cod_total FROM contencao_cenario"):
        flag = "  ⚠️" if r[4] > 0 else ""
        print(f"   {r[0]:<20}{r[1]:>14,}{r[2]:>9.0%}{r[3]:>9.1f}d{r[4]:>14.1f}"
              f"{r[5]:>14,.0f}{flag}")

    parados, dano = por_projeto(conn, g, cod, rat)
    print(f"\n   Cenário de estrangulamento (+25%): pool seca, portfólio para {parados:.1f} dia(s), "
          f"dano total R$ {dano:,.0f}")
    print(f"   {'projeto':<11}{'CoD/dia':>9}{'excedente':>12}{'EV/Mtok':>9}"
          f"{'sofre':>9}{'causa':>9}{'saldo':>9}  papel")
    for r in conn.execute("SELECT * FROM contencao_projeto ORDER BY saldo DESC"):
        print(f"   {r[0]:<11}{r[1]:>9,.0f}{r[2]:>+12,}{r[3]:>9.0f}"
              f"{r[4]:>9,.0f}{r[5]:>9,.0f}{r[6]:>+9,.0f}  {r[7]}")

    politica_de_corte(conn, g, rat)
    print("\n🪓 POLÍTICA DE CORTE — se o portfólio precisa de espaço, quem sai?")
    print("   (ordenado por EFICIÊNCIA, não por consumo bruto)")
    for r in conn.execute("SELECT ordem_corte,project_name,eficiencia,pct_pool_liberado,"
                          "pct_valor_perdido,projetos_novos FROM admissao_politica "
                          "ORDER BY ordem_corte LIMIT 3"):
        print(f"   {r[0]}º {r[1]:<11} {r[2]:>4.0f} EV/Mtok · libera {r[3]:>5.1%} do pool · "
              f"sacrifica {r[4]:>5.1%} do valor · abre {r[5]:.1f} vaga(s)")
    conn.close()
    print("\n✅ Contenção precificada e política de corte calculadas.")


if __name__ == "__main__":
    main()
