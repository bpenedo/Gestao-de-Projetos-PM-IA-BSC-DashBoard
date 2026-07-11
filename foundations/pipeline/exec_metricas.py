"""
Métricas de EXECUÇÃO de IA no tempo, a partir dos logs REAIS do Langfuse.

O dashboard já mede valor e custo; falta a saúde OPERACIONAL ao longo do tempo — o que
diferencia de um framework financeiro genérico. Bucketiza `logs_langfuse` por dia e calcula:

  • Latência p50/p95/p99 por dia + violação de SLO (p95 acima do limite de serviço).
  • Token budget burndown: consumo acumulado vs orçamento acumulado (over/under).
  • Tendência de qualidade: taxa de erro por dia + alerta de regressão (regra tipo SPC:
    salto acima da média móvel + 2σ dos dias anteriores).
  • Drift da distribuição de tokens vs a janela-baseline (1º dia) pelo D de Kolmogorov-
    Smirnov de 2 amostras — reusa a ideia do KS de ajuste_distribuicoes para detectar
    quando o comportamento do modelo mudou.

Uso:  python3 exec_metricas.py
Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026.
"""
import numpy as np

from db import get_conn, init_schema

SLO_P95_SEG = 5.0        # limite de serviço: p95 de latência não deve passar de 5 s
DRIFT_KS = 0.20          # D de KS acima disto sinaliza mudança de distribuição
ORC_FATOR = 1.10         # orçamento de tokens = 110% do consumo médio planejado


def _ks_2amostras(a, b):
    """D de Kolmogorov-Smirnov de 2 amostras = sup|F_a(x) - F_b(x)|."""
    a = np.sort(np.asarray(a, float))
    b = np.sort(np.asarray(b, float))
    if a.size == 0 or b.size == 0:
        return 0.0
    grade = np.concatenate([a, b])
    fa = np.searchsorted(a, grade, side="right") / a.size
    fb = np.searchsorted(b, grade, side="right") / b.size
    return float(np.max(np.abs(fa - fb)))


def _por_dia(rows):
    """rows: (dia, latency, tokens, erro?) -> dict dia -> listas."""
    dias = {}
    for dia, lat, tok, err in rows:
        d = dias.setdefault(dia, {"lat": [], "tok": [], "err": 0, "n": 0})
        d["lat"].append(lat)
        d["tok"].append(tok)
        d["err"] += int(err)
        d["n"] += 1
    return dict(sorted(dias.items()))


def processar(conn, projeto):
    rows = conn.execute(
        "SELECT date(updated_at) AS dia, latency_seconds, "
        "       (prompt_tokens + completion_tokens) AS tok, "
        "       CASE WHEN tipo_erro != 'NENHUM' THEN 1 ELSE 0 END AS err "
        "FROM logs_langfuse WHERE project_name=? ORDER BY updated_at", (projeto,)
    ).fetchall()
    if not rows:
        return None
    dias = _por_dia(rows)
    ordem = list(dias)
    baseline_tokens = dias[ordem[0]]["tok"]        # 1º dia = janela-baseline do drift

    # orçamento diário de tokens = média × fator; acumulado linear.
    total_tok = sum(sum(d["tok"]) for d in dias.values())
    orc_dia = (total_tok / len(dias)) * ORC_FATOR

    lat, burn, qual, drift = [], [], [], []
    tokens_acum = 0
    taxas_ant = []
    for k, dia in enumerate(ordem, 1):
        d = dias[dia]
        p50, p95, p99 = np.percentile(d["lat"], [50, 95, 99])
        lat.append((dia, float(p50), float(p95), float(p99), d["n"], int(p95 > SLO_P95_SEG)))

        tok_dia = int(sum(d["tok"]))
        tokens_acum += tok_dia
        burn.append((dia, tok_dia, tokens_acum, orc_dia * k))

        taxa = 100.0 * d["err"] / d["n"] if d["n"] else 0.0
        # alerta de regressão: taxa acima de média + 2σ dos dias anteriores (>=2 dias).
        alerta = 0
        if len(taxas_ant) >= 2:
            mu, sd = np.mean(taxas_ant), np.std(taxas_ant)
            if taxa > mu + 2 * sd and taxa > mu:
                alerta = 1
        qual.append((dia, d["n"], d["err"], float(taxa), alerta))
        taxas_ant.append(taxa)

        ks = _ks_2amostras(d["tok"], baseline_tokens)
        drift.append((dia, float(ks), int(ks > DRIFT_KS)))
    return lat, burn, qual, drift


def gravar(conn, projeto, dados):
    lat, burn, qual, drift = dados
    cur = conn.cursor()
    for tab, col in [("exec_latencia_tempo", lat), ("exec_tokens_burndown", burn),
                     ("exec_qualidade_tempo", qual), ("exec_drift", drift)]:
        cur.execute(f"DELETE FROM {tab} WHERE project_name=?", (projeto,))
    for r in lat:
        cur.execute("INSERT INTO exec_latencia_tempo VALUES (?,?,?,?,?,?,?)", (projeto, *r))
    for r in burn:
        cur.execute("INSERT INTO exec_tokens_burndown VALUES (?,?,?,?,?)", (projeto, *r))
    for r in qual:
        cur.execute("INSERT INTO exec_qualidade_tempo VALUES (?,?,?,?,?,?)", (projeto, *r))
    for r in drift:
        cur.execute("INSERT INTO exec_drift VALUES (?,?,?,?)", (projeto, *r))
    conn.commit()


def main():
    init_schema()
    conn = get_conn()
    projetos = [r[0] for r in conn.execute(
        "SELECT DISTINCT project_name FROM logs_langfuse ORDER BY project_name")]
    print(f"▶️  Métricas de execução (latência/tokens/qualidade/drift) — {len(projetos)} projetos")
    for p in projetos:
        d = processar(conn, p)
        if not d:
            continue
        gravar(conn, p, d)
        lat, burn, qual, drift = d
        slo = sum(r[5] for r in lat)
        reg = sum(r[4] for r in qual)
        dft = sum(r[2] for r in drift)
        print(f"   {p:<12} dias={len(lat)}  p95_max={max(r[2] for r in lat):.2f}s  "
              f"viola_SLO={slo}  regressões={reg}  drift={dft}")
    conn.close()
    print("✅ Métricas de execução concluídas.")


if __name__ == "__main__":
    main()
