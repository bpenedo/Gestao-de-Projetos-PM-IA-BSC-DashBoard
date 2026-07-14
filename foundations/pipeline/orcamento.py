"""
💰 ORÇAMENTO GLOBAL DE TOKENS + BASE DE RATEIO — a tragédia dos comuns tem preço.

O ERRO ESTRUTURAL QUE ISTO CONSERTA
───────────────────────────────────
O `exec_tokens_burndown` definia o orçamento de cada projeto como `consumo × 1.10`.
Circular. Auto-justificante. **Nenhum projeto podia estourar o orçamento, por construção** —
a razão consumo/orçamento dava exatamente 0,909 nos dez, sempre. A alavanca "tokens" do
PM Agent era, portanto, **incapaz de disparar**: dano R$ 0 para sempre.

Orçamento que sai do próprio gasto não é orçamento. É recibo.

O QUE O MERCADO NÃO MODELA
─────────────────────────
Langfuse, CloudZero, Vantage e afins dão **custo por projeto**, como se cada projeto tivesse
a sua própria torneira. Não tem. Existe **UM plano contratado**, com uma quota mensal finita,
e **cada token que um projeto queima é um token que outro não terá**. É a tragédia dos comuns
aplicada ao orçamento de IA — e ela tem preço, em R$.

AS TRÊS CAMADAS
───────────────
1. GLOBAL — a quota contratada, o TCO mensal (assinaturas × câmbio × IOF + infra fixa), o
   run-rate de consumo, a data de exaustão do pool, e o **desperdício contra a folga**.

2. RATEIO — a cota de cada projeto sob QUATRO bases. E aqui está o ponto:
   · por CONSUMO   → é o padrão do mercado, e é **auto-justificante**: quem mais queima
                     recebe a maior cota, o que *legitima* o desperdício.
   · por VALOR (EV)→ FinOps unit economics: paga quem entrega.
   · por PROGRESSO → o avanço declarado.
   · IGUALITÁRIO   → a base ingênua.

3. SUBSÍDIO CRUZADO — a diferença entre a cota por consumo e a cota por valor. É a resposta
   em R$/mês para a pergunta que nenhuma ferramenta faz: **quem está bancando quem.**

⚠️ SUPOSIÇÃO DECLARADA: os planos de assinatura (ChatGPT Pro, Claude Max…) não publicam
quota de tokens — são assentos com limite de uso. O mapeamento assento → tokens/mês em
TOKENS_POR_ASSENTO é **nosso**, não do fornecedor, e está aqui à vista para ser contestado.
Troque pelos SEUS números de contrato e tudo se recalcula.

Uso:  python3 orcamento.py
Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026.
"""
from db import get_conn, init_schema

DIAS_MES = 30.0

# ⚠️ POLÍTICA DECLARADA: fatia do pool distribuída como PISO igualitário. O resto vai por
# VALOR ENTREGUE. Sem piso, um projeto novo (EV=0) receberia ZERO tokens e jamais poderia
# produzir valor — um ovo-e-galinha que mataria todo projeto recém-cadastrado.
PISO_PCT = 0.50

# O contrato: (provedor, plano, assentos). Troque pelo SEU.
CONTRATO = [
    ("Anthropic", "Claude Max 20x", 2),
    ("OpenAI", "ChatGPT Pro", 1),
    ("Google", "Google AI Ultra", 1),
    ("Anthropic", "Claude Team", 6),
    ("OpenAI", "ChatGPT Team", 6),
    ("xAI", "SuperGrok", 2),
]
# ⚠️ DECLARADO (é nosso, não do fornecedor): tokens/mês que cada assento entrega.
TOKENS_POR_ASSENTO = {
    "Claude Max 20x": 20_000_000,
    "ChatGPT Pro": 15_000_000,
    "Google AI Ultra": 12_000_000,
    "Claude Team": 2_500_000,
    "ChatGPT Team": 2_500_000,
    "SuperGrok": 1_500_000,
}


def contrato(conn):
    """Quota mensal contratada e custo do plano em R$ (USD × câmbio × (1+IOF))."""
    tokens = custo = 0.0
    for prov, plano, n in CONTRATO:
        r = conn.execute(
            "SELECT usd_mes, cambio, iof_pct FROM planos_assinatura WHERE provedor=? AND plano=?",
            (prov, plano)).fetchone()
        if not r:
            continue
        usd, cambio, iof = r
        custo += n * usd * cambio * (1 + iof / 100.0)
        tokens += n * TOKENS_POR_ASSENTO.get(plano, 0)
    infra = conn.execute("SELECT COALESCE(SUM(valor_mensal),0) FROM assinaturas_infra").fetchone()[0]
    return int(tokens), float(custo), float(infra)


def consumo(conn):
    """Run-rate mensal por projeto, e o desperdício (tokens queimados em chamadas que FALHARAM)."""
    dias = conn.execute("SELECT COUNT(DISTINCT date(updated_at)) FROM logs_langfuse").fetchone()[0] or 1
    tok = dict(conn.execute(
        "SELECT project_name, SUM(prompt_tokens + completion_tokens) FROM logs_langfuse GROUP BY 1"))
    desp = dict(conn.execute(
        "SELECT project_name, COALESCE(SUM(tokens_desperdicados),0) FROM alertas_criticos GROUP BY 1"))
    f = DIAS_MES / dias                       # fator de projeção para o mês
    return ({p: int(v * f) for p, v in tok.items()},
            {p: int(desp.get(p, 0) * f) for p in tok}, dias)


def processar(conn):
    tokens_contr, custo_plano, custo_infra = contrato(conn)
    tok_mes, desp_mes, dias = consumo(conn)
    total_tok = sum(tok_mes.values())
    total_desp = sum(desp_mes.values())
    tco = custo_plano + custo_infra
    por_mtoken = custo_plano / (tokens_contr / 1e6) if tokens_contr else 0.0

    folga = tokens_contr - total_tok
    dia_a_dia = total_tok / DIAS_MES
    exaustao = (tokens_contr / dia_a_dia) if dia_a_dia else 999.0
    desp_brl = (total_desp / 1e6) * por_mtoken
    # ⭐ O número que dói: o desperdício contra a folga contratual.
    d_vs_f = (total_desp / folga) if folga > 0 else float("inf")

    cur = conn.cursor()
    cur.execute("INSERT OR REPLACE INTO orcamento_global VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                ("mensal", tokens_contr, custo_plano, custo_infra, tco, por_mtoken,
                 total_tok, total_tok / tokens_contr if tokens_contr else 0,
                 folga, exaustao, total_desp, desp_brl, d_vs_f))

    # ── RATEIO
    ev = dict(conn.execute("SELECT project_name, ev FROM evm_indices"))
    prog = dict(conn.execute(
        "SELECT project_name, progresso_pct_acumulado FROM projetos_status"))
    projs = sorted(tok_mes)
    tot_ev = sum(ev.get(p, 0) for p in projs) or 1
    tot_pr = sum(prog.get(p, 0) for p in projs) or 1
    n = len(projs)

    for p in projs:
        t = tok_mes[p]
        pct_pool = t / total_tok if total_tok else 0
        pct_val = ev.get(p, 0) / tot_ev
        efic = (ev.get(p, 0) / (t / 1e6)) if t else 0        # EV por MILHÃO de tokens
        c_cons, c_val = tco * pct_pool, tco * pct_val
        c_prog = tco * (prog.get(p, 0) / tot_pr)
        c_igual = tco / n
        sub = c_cons - c_val                                  # >0 = consome mais do que entrega
        papel = ("SUBSIDIADO" if sub > tco * 0.02 else
                 "PAGADOR" if sub < -tco * 0.02 else "NEUTRO")
        cur.execute("INSERT OR REPLACE INTO orcamento_rateio VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (p, t, pct_pool, ev.get(p, 0), pct_val, efic, c_cons, c_val, c_prog,
                     c_igual, sub, papel, desp_mes[p], (desp_mes[p] / 1e6) * por_mtoken))
    conn.commit()
    return dict(tokens_contr=tokens_contr, custo_plano=custo_plano, infra=custo_infra, tco=tco,
                por_mtoken=por_mtoken, total_tok=total_tok, folga=folga, exaustao=exaustao,
                desp=total_desp, desp_brl=desp_brl, d_vs_f=d_vs_f, dias=dias)


def cotas_adaptativas(conn, tokens_contr, tok_mes, por_mtoken):
    """
    🔄 A COTA ADAPTATIVA. O orçamento de cada projeto é FATIADO do pool global — e
    redimensionado sempre que N muda. Cadastrou projeto novo? Todo mundo encolhe, e o
    sistema recalcula sozinho, porque N sai do banco, não de uma constante.

    A regra de fatiamento (declarada, para poder ser contestada):

        cota_i = PISO + (pool_livre × fatia_de_VALOR_i)

    · PISO = PISO_PCT × (pool ÷ N). Um projeto novo tem EV = 0; se o rateio fosse 100%
      por valor, ele receberia ZERO tokens e nunca poderia produzir valor. O piso é o
      mínimo vital que quebra esse ovo-e-galinha.
    · O resto vai por VALOR ENTREGUE (EV), não por consumo. Ratear por consumo é
      auto-justificante: premia quem queima. É o erro que o mercado inteiro comete.
    """
    ev = dict(conn.execute("SELECT project_name, ev FROM evm_indices"))
    projs = sorted(tok_mes)
    n = len(projs)
    if not n:
        return

    piso_total = tokens_contr * PISO_PCT
    piso = int(piso_total / n)
    livre = tokens_contr - piso_total
    tot_ev = sum(ev.get(p, 0) for p in projs) or 1

    cur = conn.cursor()
    cur.execute("DELETE FROM orcamento_cota")
    for p in projs:
        var = int(livre * (ev.get(p, 0) / tot_ev))
        cota = piso + var
        cons = tok_mes[p]
        exc = cons - cota
        cur.execute("INSERT INTO orcamento_cota VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                    (p, n, piso, var, cota, (cota / 1e6) * por_mtoken, cons,
                     cons / cota if cota else 0, exc, (exc / 1e6) * por_mtoken,
                     1 if exc > 0 else 0))

    # ⚠️ CONSERTA O ORÇAMENTO CIRCULAR: o burndown de tokens passa a comparar o consumo
    # com a COTA REAL do pool, e não com o próprio consumo × 1,10. Sem isto, a alavanca
    # "tokens" do PM Agent é incapaz de disparar — dano R$ 0 para sempre.
    dias = conn.execute("SELECT COUNT(DISTINCT dia) FROM exec_tokens_burndown").fetchone()[0] or 1
    for p in projs:
        cota_dia = (conn.execute("SELECT cota_tokens FROM orcamento_cota WHERE project_name=?",
                                 (p,)).fetchone()[0] / DIAS_MES)
        for i, (d,) in enumerate(conn.execute(
                "SELECT dia FROM exec_tokens_burndown WHERE project_name=? ORDER BY dia",
                (p,)).fetchall(), start=1):
            cur.execute("UPDATE exec_tokens_burndown SET orcamento_acum=? "
                        "WHERE project_name=? AND dia=?", (cota_dia * i, p, d))
    conn.commit()


def custo_da_admissao(conn, tokens_contr, por_mtoken):
    """
    💥 O QUE CUSTA DIZER "SIM" A MAIS UM PROJETO.
    Num pool FINITO, admitir o projeto N+1 tira tokens de todos os N que já estavam lá.
    Nenhuma ferramenta do mercado precifica isso — o comitê de portfólio decide no escuro.
    """
    n = conn.execute("SELECT COUNT(*) FROM orcamento_cota").fetchone()[0]
    if not n:
        return
    cur = conn.cursor()
    cur.execute("DELETE FROM orcamento_admissao")
    media_antes = tokens_contr // n
    for k in (1, 2, 3):
        n2 = n + k
        media_depois = tokens_contr // n2
        dil = (media_antes - media_depois) / media_antes
        perdidos = (media_antes - media_depois) * n
        custo = (perdidos / 1e6) * por_mtoken
        v = (f"Admitir {k} projeto(s) dilui a cota média de cada um dos {n} existentes em "
             f"{dil:.1%} ({media_antes:,} → {media_depois:,} tokens/mês). Isso retira "
             f"{perdidos:,} tokens/mês do portfólio atual — R$ {custo:,.0f}/mês de capacidade "
             f"que já estava alocada. Ou o plano cresce, ou alguém entrega menos.")
        cur.execute("INSERT INTO orcamento_admissao VALUES (?,?,?,?,?,?,?,?,?)",
                    (f"n+{k}", n, n2, media_antes, media_depois, dil, perdidos, custo, v))
    conn.commit()


def main():
    init_schema()
    conn = get_conn()
    g = processar(conn)
    tok_mes, _, _ = consumo(conn)
    cotas_adaptativas(conn, g["tokens_contr"], tok_mes, g["por_mtoken"])
    custo_da_admissao(conn, g["tokens_contr"], g["por_mtoken"])
    print("💰 ORÇAMENTO GLOBAL DE TOKENS (o pool é compartilhado e finito)")
    print(f"   contratado ........ {g['tokens_contr']:>14,} tokens/mês")
    print(f"   consumo (run-rate)  {g['total_tok']:>14,} tokens/mês  "
          f"({g['total_tok']/g['tokens_contr']:.1%} da quota, base {g['dias']} dias)")
    print(f"   folga ............. {g['folga']:>14,} tokens/mês")
    print(f"   exaustão do pool .. {g['exaustao']:>14.1f} dias "
          f"{'⚠️ ANTES do fim do mês' if g['exaustao'] < DIAS_MES else '(o mês fecha)'}")
    print(f"   TCO mensal ........ R$ {g['tco']:>11,.2f}  "
          f"(plano R$ {g['custo_plano']:,.2f} + infra R$ {g['infra']:,.2f})")
    print(f"   custo por Mtoken .. R$ {g['por_mtoken']:>11,.2f}")
    print(f"\n   🔥 DESPERDÍCIO .... {g['desp']:>14,} tokens/mês = R$ {g['desp_brl']:,.2f}")
    print(f"      desperdício ÷ folga = {g['d_vs_f']:.1f}×  "
          f"{'⚠️ VOCÊ VAI CONTRATAR UM PLANO MAIOR POR CAUSA DE CHAMADAS QUE FALHARAM' if g['d_vs_f'] > 1 else ''}")

    print("\n📊 BASE DE RATEIO — quem consome, quem entrega, quem banca quem")
    print(f"   {'projeto':<11}{'tokens/mês':>12}{'%pool':>7}{'%valor':>8}{'EV/Mtok':>9}"
          f"{'cota consumo':>14}{'cota valor':>12}{'subsídio':>11}  papel")
    for r in conn.execute("SELECT * FROM orcamento_rateio ORDER BY subsidio_brl DESC"):
        p, t, pp, ev, pv, ef, cc, cv, _, _, sub, papel, _, _ = r
        print(f"   {p:<11}{t:>12,}{pp:>7.1%}{pv:>8.1%}{ef:>9.0f}"
              f"{cc:>13,.0f} {cv:>11,.0f} {sub:>+10,.0f}  {papel}")
    print("\n🔄 COTA ADAPTATIVA — o pool fatiado entre os N projetos (piso 50% + valor 50%)")
    print(f"   {'projeto':<11}{'cota/mês':>12}{'consumo':>12}{'uso':>8}{'excedente':>12}  status")
    for r in conn.execute("SELECT project_name,cota_tokens,consumo_tokens,pct_uso,excedente,excedente_brl,estourou FROM orcamento_cota ORDER BY pct_uso DESC"):
        st = "🔴 ESTOUROU" if r[6] else "🟢 dentro da cota"
        print(f"   {r[0]:<11}{r[1]:>12,}{r[2]:>12,}{r[3]:>8.0%}{r[4]:>+12,}  {st}")
    n_est = conn.execute("SELECT COUNT(*) FROM orcamento_cota WHERE estourou=1").fetchone()[0]
    rouba = conn.execute("SELECT COALESCE(SUM(excedente_brl),0) FROM orcamento_cota WHERE estourou=1").fetchone()[0]
    print(f"   → {n_est}/10 estouraram a cota e juntos tomam R$ {rouba:,.0f}/mês do pool dos outros")

    print("\n💥 O CUSTO DE ADMITIR UM PROJETO NOVO (pool finito = todo mundo encolhe)")
    for r in conn.execute("SELECT cenario,n_atual,n_novo,cota_media_antes,cota_media_depois,diluicao_pct,custo_diluicao FROM orcamento_admissao"):
        print(f"   {r[0]}: {r[1]}→{r[2]} projetos · cota média {r[3]:,} → {r[4]:,} "
              f"(−{r[5]:.1%}) · R$ {r[6]:,.0f}/mês de capacidade diluída")
    conn.close()
    print("\n✅ Orçamento global, rateio e cotas adaptativas calculados.")


if __name__ == "__main__":
    main()
