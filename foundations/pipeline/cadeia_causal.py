"""
🔗 CADEIA CAUSAL — o diferencial que nenhum concorrente consegue emitir.

    "O modelo derivou (KS 0,27). Isso empurrou o risco de qualidade de 3 para 5,
     alargou a duração de 'Avaliação & guardrails', moveu o P80 de 42 para 46 dias,
     e derrubou o VPL em R$ 18 mil. Aqui está a corrente."

Nem o Jira, nem o MS Project, nem o Langfuse, nem o CloudZero dizem isso — nenhum tem
as quatro pontas. Este script LIGA os quatro motores que já existiam soltos:

  elo 1 · TELEMETRIA  exec_drift.ks_stat   (KS de 2 amostras nos tokens REAIS)
  elo 2 · RISCO       probabilidade do risco "Modelo" sobe com o drift observado
  elo 3 · PRAZO       a incerteza da tarefa de avaliação/guardrails ALARGA
                      -> cronograma Monte Carlo re-simulado -> novo P80
  elo 4 · DINHEIRO    os fluxos positivos são EMPURRADOS pelos dias perdidos
                      -> novo VPL -> custo do atraso, em R$

Modelo do elo 3 (explícito, para poder ser criticado):
  a duração pessimista (b) da tarefa de avaliação é multiplicada por (1 + K·intensidade),
  onde intensidade ∈ [0,1] combina a fração de dias com drift e o KS máximo. Só a cauda
  pessimista alarga — o otimista e o mais provável não mudam. É a hipótese honesta:
  drift não deixa a tarefa mais lenta *em média*, deixa o pior caso **pior**.

Modelo do elo 4: cada dia perdido empurra os fluxos POSITIVOS em `dias/365` de período.
VPL recalculado à mesma taxa. Sem drift, dias_perdidos = 0 e custo_atraso = 0 (identidade).

Uso:  python3 cadeia_causal.py
Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026.
"""
import numpy as np

from db import get_conn, init_schema
from config import MC_CRONO_ITER, MC_CRONO_CONF, MC_SEED
from cronograma_mc import simular
from risco import _prob_ancorada

TAREFA_ALVO = "Avaliação & guardrails"   # a tarefa de IA que o drift realmente machuca
K_ALARGA = 0.60                          # quanto a cauda pessimista alarga no drift máximo
DIAS_POR_PERIODO = 365.0                 # os fluxos de caixa são anuais


def intensidade_drift(conn, projeto):
    """[0,1] — combina fração de dias com drift e o KS máximo observado."""
    rows = conn.execute(
        "SELECT ks_stat, drift_alerta FROM exec_drift WHERE project_name=?", (projeto,)
    ).fetchall()
    if not rows:
        return 0.0, 0, 0.0
    ks = [r[0] for r in rows]
    dias = sum(r[1] for r in rows)
    frac = dias / len(rows)
    ks_max = max(ks)
    # média geométrica suave: precisa de drift frequente E forte para dar intensidade alta
    return float(np.clip(frac * min(1.0, ks_max / 0.5), 0.0, 1.0)), int(dias), float(ks_max)


def _tarefas(conn, projeto, mult_pess=1.0):
    """WBS do projeto; opcionalmente alarga a cauda pessimista da tarefa de avaliação."""
    rows = conn.execute(
        "SELECT tarefa_id, nome, dur_min, dur_prob, dur_max, predecessoras "
        "FROM cronograma_tarefas WHERE project_name=? ORDER BY tarefa_id", (projeto,)
    ).fetchall()
    tar = {}
    for tid, nome, a, m, b, preds in rows:
        if nome == TAREFA_ALVO and mult_pess != 1.0:
            b = b * mult_pess
        tar[tid] = {"nome": nome, "a": a, "m": m, "b": b,
                    "preds": [int(x) for x in preds.split(",") if x]}
    return tar


def _p80(tarefas, rng):
    fim, _crit, _lay = simular(tarefas, MC_CRONO_ITER, rng)
    return float(np.percentile(fim, MC_CRONO_CONF))


def _vpl(fluxos, taxa, atraso_dias=0.0):
    """
    VPL com os fluxos POSITIVOS empurrados por `atraso_dias`. O investimento inicial
    (fluxo negativo no período 0) não se move: você já gastou.
    """
    d = atraso_dias / DIAS_POR_PERIODO
    v = 0.0
    for t, f in fluxos:
        expoente = t + (d if f > 0 and t > 0 else 0.0)
        v += f / ((1 + taxa) ** expoente)
    return float(v)


def processar(conn, projeto, rng):
    inten, dias_drift, ks_max = intensidade_drift(conn, projeto)

    # elo 2 — risco: probabilidade do risco "Modelo" com e sem o drift observado.
    prob_nova = _prob_ancorada(conn, projeto, "Modelo")
    prob_base = 1                                     # sem nenhum dia de drift, a âncora é 1

    # elo 3 — prazo: alarga só a cauda pessimista da tarefa de avaliação.
    mult = 1.0 + K_ALARGA * inten
    base = _tarefas(conn, projeto)
    if not base:
        return None
    alvo = next((t for t in base.values() if t["nome"] == TAREFA_ALVO), None)
    if not alvo:
        return None
    p80_base = _p80(base, np.random.default_rng(MC_SEED))
    p80_novo = _p80(_tarefas(conn, projeto, mult), np.random.default_rng(MC_SEED))
    dias_perdidos = max(0.0, p80_novo - p80_base)

    # elo 4 — dinheiro: empurra os fluxos positivos e recalcula o VPL.
    fx = conn.execute(
        "SELECT periodo, fluxo, taxa FROM fluxo_caixa WHERE project_name=? ORDER BY periodo",
        (projeto,)).fetchall()
    if not fx:
        return None
    taxa = fx[0][2]
    fluxos = [(r[0], r[1]) for r in fx]
    vpl_base = _vpl(fluxos, taxa, 0.0)
    vpl_novo = _vpl(fluxos, taxa, dias_perdidos)
    delta_vpl = vpl_base - vpl_novo   # efeito do desconto: pequeno em fluxos ANUAIS

    # COST OF DELAY — o número que a diretoria sente (Reinertsen).
    # Cada dia de atraso: (a) um dia de MRR que não entra; (b) o time continua custando;
    # (c) o burn de tokens continua queimando. Honesto e padrão em gestão de produto.
    row = conn.execute(
        "SELECT COALESCE(h.faturamento_mrr_incremental,0), COALESCE(h.custo_total_desenvolvimento,0) "
        "FROM horas_desenvolvimento h WHERE h.project_name=?", (projeto,)).fetchone()
    mrr, custo_dev = (row[0], row[1]) if row else (0.0, 0.0)
    burn = conn.execute(
        "SELECT COALESCE(AVG(burn_rate_ia),0) FROM kpi_snapshots WHERE project_name=?",
        (projeto,)).fetchone()[0]
    dur_planejada = max(1.0, p80_base)
    cod_dia = (mrr / 30.0) + (custo_dev / dur_planejada) + float(burn)
    custo = dias_perdidos * cod_dia

    return dict(dias_com_drift=dias_drift, ks_max=ks_max,
                risco_prob_base=prob_base, risco_prob_nova=prob_nova,
                tarefa_afetada=TAREFA_ALVO,
                dur_pess_base=alvo["b"], dur_pess_nova=alvo["b"] * mult,
                p80_base=p80_base, p80_novo=p80_novo, dias_perdidos=dias_perdidos,
                vpl_base=vpl_base, vpl_novo=vpl_novo, delta_vpl=delta_vpl,
                cod_dia=cod_dia, custo_atraso=custo)


def main():
    init_schema()
    conn = get_conn()
    rng = np.random.default_rng(MC_SEED)
    projetos = [r[0] for r in conn.execute(
        "SELECT DISTINCT project_name FROM cronograma_tarefas ORDER BY project_name")]
    cur = conn.cursor()
    print(f"🔗 Cadeia causal (telemetria → risco → prazo → dinheiro) — {len(projetos)} projetos")
    for p in projetos:
        d = processar(conn, p, rng)
        if not d:
            continue
        cur.execute("DELETE FROM cadeia_causal WHERE project_name=?", (p,))
        cur.execute("INSERT INTO cadeia_causal VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (p, d["dias_com_drift"], d["ks_max"], d["risco_prob_base"],
                     d["risco_prob_nova"], d["tarefa_afetada"], d["dur_pess_base"],
                     d["dur_pess_nova"], d["p80_base"], d["p80_novo"], d["dias_perdidos"],
                     d["vpl_base"], d["vpl_novo"], d["delta_vpl"], d["cod_dia"],
                     d["custo_atraso"]))
        print(f"   {p:<12} drift={d['dias_com_drift']}d (KS {d['ks_max']:.2f})  "
              f"risco {d['risco_prob_base']}→{d['risco_prob_nova']}  "
              f"P80 {d['p80_base']:.1f}→{d['p80_novo']:.1f} ({d['dias_perdidos']:+.1f}d)  "
              f"CoD R$ {d['cod_dia']:,.0f}/dia  →  CUSTO R$ {d['custo_atraso']:,.0f}")
    conn.commit()
    conn.close()
    print("✅ Cadeia causal calculada — o elo que nenhum concorrente tem.")


if __name__ == "__main__":
    main()
