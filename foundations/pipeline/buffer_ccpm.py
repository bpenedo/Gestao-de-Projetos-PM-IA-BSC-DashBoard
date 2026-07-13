"""
🌡️ CCPM (Goldratt) + 🏦 PMI RESERVE ANALYSIS — o direito de ficar calado.

A maior fraqueza de um agente de gestão não é falta de métrica: é que ele SEMPRE recomenda
alguma coisa. Um agente que grita toda semana vira ruído, e ruído é ignorado. Estes dois
métodos existem para dar ao agente um critério objetivo de QUANDO NÃO FALAR.

──────────────────────────────────────────────────────────────────────────────────────────
1) FEVER CHART (Critical Chain / Buffer Management)

   buffer do projeto = P80 − P50   (o compromisso menos a cadeia agressiva)
   consumido         = atraso do Earned Schedule, em dias = max(0, −SV(t)) × (P50 ÷ PD)

   ⚠️ CUIDADO COM UNIDADE: o EVM vive em PERÍODOS (PD) e o cronograma Monte Carlo em DIAS
   (P50). A primeira versão fazia P50 ÷ SPI(t) — o que extrapola a cadeia inteira pelo
   índice e estourava 800% de buffer. Converter o atraso do ES para dias é o certo.

   Cruza "% da cadeia concluída" (x) com "% do buffer consumido" (y). As fronteiras são
   DIAGONAIS de propósito — queimar buffer no fim do projeto é normal; queimar no começo
   é grave, porque ainda falta projeto inteiro pela frente:

       verde/amarelo:    y = 1/3 + (1/3)·x
       amarelo/vermelho: y = 2/3 + (1/3)·x

   VERDE = não faça nada (e o agente CALA).   AMARELO = planeje a recuperação.
   VERMELHO = aja agora.

2) RESERVE ANALYSIS (PMI)

   contingência      = P80 − P50    conhecidos-desconhecidos (a variabilidade que você mediu)
   reserva gerencial = P95 − P80    desconhecidos-desconhecidos (o susto)

   O FATO, sem suposição nenhuma: aqui o buffer P80−P50 dá **~9% da cadeia**, quando o CCPM
   trabalha com 25–50%. Isto é aritmética sobre o seu cronograma, e é o achado que sustenta
   a conversa toda.

   O confronto com o REGISTRO DE RISCO (EMV em dias — Integrated Cost-Schedule Risk
   Analysis, Hulett) é mais delicado, e sou explícito: as escalas são 1–5, e converter
   "impacto 4" em dias exige um mapeamento que é MEU, não seu (IMPACTO_PCT_CADEIA abaixo).

   ⚠️ E TESTEI A MINHA PRÓPRIA SUPOSIÇÃO: cortando o impacto suposto pela METADE, a
   conclusão "sub-reservado" vira de 10/10 projetos para 1/10. Ou seja: ela é um FIO DE
   NAVALHA apoiado num número que eu inventei, e por isso **não é vendida como achado**.
   Cada projeto carrega o campo `robusto`, e o veredito diz na cara quando a leitura não
   sobrevive ao teste de estresse. Número frágil apresentado com cara de rigor é pior do
   que número nenhum.

Uso:  python3 buffer_ccpm.py
Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026.
"""
from db import get_conn, init_schema

# ⚠️ Mapeamentos DECLARADOS (não são dado seu — são hipótese minha, discutível de propósito).
# O impacto é % DA CADEIA, não dias absolutos: um risco "impacto 4" num projeto de 20 dias
# não pode custar o mesmo que num de 200. A primeira versão usava dias fixos e reprovava
# 10 de 10 projetos — quando todo mundo reprova, o errado costuma ser o teste.
IMPACTO_PCT_CADEIA = {1: 0.005, 2: 0.015, 3: 0.03, 4: 0.06, 5: 0.10}
PROB_PCT = {1: 0.10, 2: 0.30, 3: 0.50, 4: 0.70, 5: 0.90}  # probabilidade (1-5) -> chance


def zona_fever(pct_cadeia, pct_buffer):
    """As duas diagonais do fever chart. Devolve (zona, lim_verde, lim_vermelho)."""
    lim_verde = (1.0 / 3.0) + (1.0 / 3.0) * pct_cadeia
    lim_vermelho = (2.0 / 3.0) + (1.0 / 3.0) * pct_cadeia
    if pct_buffer <= lim_verde:
        z = "VERDE"
    elif pct_buffer <= lim_vermelho:
        z = "AMARELO"
    else:
        z = "VERMELHO"
    return z, lim_verde, lim_vermelho


def emv_risco_dias(conn, projeto, cadeia_dias, fator=1.0):
    """
    Contingência de prazo que o REGISTRO DE RISCO justifica (EMV, em dias).
    O buffer P80−P50 só captura a VARIABILIDADE das durações; ele é cego aos EVENTOS de
    risco do registro. Confrontar os dois é o ponto do Integrated Cost-Schedule Risk
    Analysis (Hulett) — e é onde quase todo cronograma se descobre otimista.
    """
    rows = conn.execute(
        "SELECT probabilidade, impacto FROM risco_registro WHERE project_name=? "
        "AND LOWER(status) IN ('aberto','mitigando')", (projeto,)).fetchall()
    return sum(PROB_PCT.get(int(p), 0.5) * IMPACTO_PCT_CADEIA.get(int(i), 0.03) * fator
               * cadeia_dias for p, i in rows)


def processar(conn, projeto):
    cr = conn.execute(
        "SELECT p50, p80, p95 FROM mc_cronograma WHERE project_name=?", (projeto,)).fetchone()
    ev = conn.execute(
        "SELECT ev, bac, sv_t, pd FROM evm_indices WHERE project_name=?", (projeto,)).fetchone()
    if not cr or not ev:
        return None
    p50, p80, p95 = cr
    ev_val, bac, sv_t, pd = ev
    buffer_dias = max(0.0, p80 - p50)
    if buffer_dias <= 0 or not pd:
        return None

    # ⚠️ UNIDADES: o EVM vive em PERÍODOS (PD) e o cronograma em DIAS (P50). A primeira
    # versão fazia P50/SPI(t), o que extrapola a cadeia inteira e estourava 800% de buffer.
    # O correto: o atraso do Earned Schedule (−SV(t), em períodos) convertido para dias.
    dias_por_periodo = p50 / pd
    atraso_periodos = max(0.0, -(sv_t or 0.0))       # SV(t) negativo = atrasado
    consumido = atraso_periodos * dias_por_periodo
    previsao = p50 + consumido
    pct_cadeia = min(1.0, (ev_val / bac) if bac else 0.0)
    pct_buffer = consumido / buffer_dias
    zona, lim_v, lim_r = zona_fever(pct_cadeia, pct_buffer)

    # PMI — reserve analysis
    conting = buffer_dias                       # P80 − P50
    reserva_ger = max(0.0, p95 - p80)           # P95 − P80
    # No ritmo atual, em que % da cadeia a contingência acaba?
    taxa = (consumido / pct_cadeia) if pct_cadeia > 0.01 else 0.0
    exaustao = min(1.0, conting / taxa) if taxa > 0 else 1.0
    # EMV sob a suposição declarada — e sob METADE dela. Se a conclusão vira ao cortar a
    # suposição pela metade, ela é um fio de navalha e NÃO pode ser vendida como achado.
    emv = emv_risco_dias(conn, projeto, p50)
    emv_cons = emv_risco_dias(conn, projeto, p50, fator=0.5)
    sub = 1 if emv > conting else 0
    robusto = 1 if (emv > conting) == (emv_cons > conting) else 0
    buf_pct = buffer_dias / p50 if p50 else 0.0

    # ⭐ O FATO que não depende de suposição alguma: o buffer contra a própria cadeia.
    # CCPM trabalha com buffer de 25–50% da cadeia. Isto aqui é aritmética, não hipótese.
    vered = (f"O buffer do projeto é {buffer_dias:.1f} dia(s) — **{buf_pct:.0%} da cadeia**, "
             f"contra os 25–50% com que o CCPM trabalha. ")
    if zona == "VERMELHO":
        vered += (f"E ele já foi **estourado**: o atraso do Earned Schedule consumiu "
                  f"{consumido:.1f} dia(s), {pct_buffer:.0%} do buffer, com {pct_cadeia:.0%} da "
                  f"cadeia pronta. A data P80 ({p80:.1f}d) não se sustenta; sobra a reserva "
                  f"gerencial de {reserva_ger:.1f} dia(s) até o P95.")
    elif zona == "AMARELO":
        vered += (f"Consumo em zona de atenção: {pct_buffer:.0%} do buffer com {pct_cadeia:.0%} "
                  f"da cadeia pronta — planeje a recuperação, ainda dá.")
    else:
        vered += (f"Consumo sob controle: {pct_buffer:.0%} do buffer com {pct_cadeia:.0%} da "
                  f"cadeia pronta. **Nada a escalar.**")

    # A suposição, com o seu próprio teste de estresse ao lado. Sem isto, seria número
    # inventado com cara de rigor.
    vered += (f" · Quanto ao registro de risco: sob o mapeamento declarado (impacto 1–5 → "
              f"0,5–10% da cadeia), ele justificaria {emv:.1f} dia(s) de contingência "
              f"{'ACIMA' if sub else 'DENTRO'} dos {conting:.1f} reservados.")
    vered += (" ⚠️ Mas esta leitura **não é robusta**: cortando o impacto suposto pela metade "
              f"({emv_cons:.1f} dia(s)), a conclusão se inverte. Trate-a como pergunta a fazer "
              f"ao time, não como fato."
              if not robusto else
              " Esta leitura **sobrevive** ao corte da suposição pela metade — é robusta.")

    return dict(p50=p50, p80=p80, p95=p95, buffer=buffer_dias, previsao=previsao,
                consumido=consumido, pct_cadeia=pct_cadeia, pct_buffer=pct_buffer,
                lim_v=lim_v, lim_r=lim_r, zona=zona, conting=conting, reserva_ger=reserva_ger,
                exaustao=exaustao, emv=emv, emv_cons=emv_cons, sub=sub, robusto=robusto,
                buf_pct=buf_pct, veredito=vered)


def main():
    init_schema()
    conn = get_conn()
    cur = conn.cursor()
    projetos = [r[0] for r in conn.execute(
        "SELECT DISTINCT project_name FROM mc_cronograma ORDER BY project_name")]
    print(f"🌡️ CCPM buffer/fever chart + 🏦 PMI reserve analysis — {len(projetos)} projetos")
    cont = {"VERDE": 0, "AMARELO": 0, "VERMELHO": 0}
    for p in projetos:
        d = processar(conn, p)
        if not d:
            continue
        cur.execute("INSERT OR REPLACE INTO buffer_fever VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                    (p, d["p50"], d["p80"], d["p95"], d["buffer"], d["previsao"], d["consumido"],
                     d["pct_cadeia"], d["pct_buffer"], d["lim_v"], d["lim_r"], d["zona"]))
        cur.execute("INSERT OR REPLACE INTO reserva_analise VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                    (p, d["conting"], d["reserva_ger"], d["consumido"], d["pct_buffer"],
                     d["exaustao"], d["emv"], d["emv_cons"], d["sub"], d["robusto"],
                     d["buf_pct"], d["veredito"]))
        cont[d["zona"]] += 1
        flag = ("" if d["robusto"] else " (não robusto)")
        print(f"   {p:<12} cadeia {d['pct_cadeia']:>4.0%} · buffer {d['pct_buffer']:>5.0%} "
              f"→ {d['zona']:<9} | buffer={d['buf_pct']:.0%} da cadeia · risco justifica "
              f"{d['emv']:.1f}d vs {d['conting']:.1f}d reservados{flag}")
    conn.commit()
    conn.close()
    print(f"✅ Fever chart: {cont['VERDE']} verde · {cont['AMARELO']} amarelo · "
          f"{cont['VERMELHO']} vermelho — o agente só fala fora do verde.")


if __name__ == "__main__":
    main()
