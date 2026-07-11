"""
Métricas de FLUXO (Kanban/ágil): Cumulative Flow Diagram, cycle time, lead time,
throughput e WIP. Fecha o lado de execução/entrega que faltava — o dashboard media
custo e valor, não o fluxo do trabalho.

Modela itens de trabalho por projeto fluindo entre estados (backlog → doing → review →
done) ao longo dos dias. O nº de itens e o ritmo são ancorados no throughput real
implícito no progresso (projetos_status.progresso_pct_delta_real) e no volume de
atividade (logs por dia). Cycle time por item -> percentis P50/P85 (previsão por
percentil, não por chute), e o CFD mostra WIP e gargalos de relance.

Uso:  python3 fluxo.py
Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026.
"""
import numpy as np

from db import get_conn, init_schema

N_DIAS = 7
ESTADOS = ["backlog", "doing", "review", "done"]


def _perfil(conn, projeto, rng):
    """Escopo e ritmo do projeto, ancorados no progresso real."""
    row = conn.execute(
        "SELECT progresso_pct_delta_real, progresso_pct_acumulado FROM projetos_status "
        "WHERE project_name=?", (projeto,)).fetchone()
    rate = float(row[0]) if row and row[0] else 12.0
    # nº de itens de trabalho ~ proporcional ao ritmo (mais ritmo, mais itens fluindo)
    n_itens = int(np.clip(round(rate * 1.6), 10, 30))
    # throughput-alvo por dia (itens/dia): projetos mais rápidos entregam mais
    thr = max(1.0, rate / 6.0)
    return n_itens, thr


def simular(conn, projeto, rng):
    n_itens, thr = _perfil(conn, projeto, rng)
    dias = [f"2026-07-{4+d:02d}" for d in range(N_DIAS)]

    # Cada item: dia de entrada no backlog, no doing, no review, no done.
    # Chegadas ao longo dos dias; cycle time (doing->done) log-normalish via Triangular.
    itens = []
    for i in range(1, n_itens + 1):
        t_backlog = rng.integers(0, N_DIAS)                     # entra no backlog
        espera = rng.triangular(0, 0.5, 2)                       # backlog -> doing
        ct = float(rng.triangular(0.5, 1.5 / (thr / 2 + 0.5), 4))  # cycle time (doing->done)
        review = float(rng.triangular(0.2, 0.5, 1.5))
        t_doing = t_backlog + espera
        t_review = t_doing + ct
        t_done = t_review + review
        lead = t_done - t_backlog
        itens.append(dict(id=i, tb=t_backlog, td=t_doing, tr=t_review, tf=t_done,
                          cycle=ct + review, lead=lead))

    # CFD: para cada dia, conta itens em cada estado (acumulado por definição do estado).
    cur = conn.cursor()
    cur.execute("DELETE FROM fluxo_cfd WHERE project_name=?", (projeto,))
    for d, dia in enumerate(dias):
        backlog = sum(1 for it in itens if it["tb"] <= d < it["td"])
        doing = sum(1 for it in itens if it["td"] <= d < it["tr"])
        review = sum(1 for it in itens if it["tr"] <= d < it["tf"])
        done = sum(1 for it in itens if it["tf"] <= d)
        # itens ainda não chegados contam como backlog futuro
        nao_chegou = sum(1 for it in itens if d < it["tb"])
        backlog += nao_chegou
        wip = doing + review
        cur.execute("INSERT INTO fluxo_cfd VALUES (?,?,?,?,?,?,?)",
                    (projeto, dia, backlog, doing, review, done, wip))

    # Itens concluídos dentro da janela -> cycle/lead time.
    cur.execute("DELETE FROM fluxo_itens WHERE project_name=?", (projeto,))
    concluidos = [it for it in itens if it["tf"] <= N_DIAS]
    for it in concluidos:
        dia_c = f"2026-07-{4 + int(min(N_DIAS-1, it['tf'])):02d}"
        cur.execute("INSERT INTO fluxo_itens VALUES (?,?,?,?,?)",
                    (projeto, it["id"], dia_c, round(it["lead"], 2), round(it["cycle"], 2)))

    # Resumo: throughput, percentis de cycle time, WIP médio.
    cts = np.array([it["cycle"] for it in concluidos]) if concluidos else np.array([0.0])
    leads = np.array([it["lead"] for it in concluidos]) if concluidos else np.array([0.0])
    wips = [row for row in cur.execute(
        "SELECT wip FROM fluxo_cfd WHERE project_name=?", (projeto,)).fetchall()]
    wip_medio = float(np.mean([w[0] for w in wips])) if wips else 0.0
    throughput = len(concluidos) / N_DIAS
    cur.execute("DELETE FROM fluxo_resumo WHERE project_name=?", (projeto,))
    cur.execute("INSERT INTO fluxo_resumo VALUES (?,?,?,?,?,?)",
                (projeto, round(throughput, 2), float(np.percentile(cts, 50)),
                 float(np.percentile(cts, 85)), round(wip_medio, 2),
                 float(np.percentile(leads, 50))))
    conn.commit()
    return len(concluidos), throughput, float(np.percentile(cts, 85))


def main():
    init_schema()
    conn = get_conn()
    projetos = [r[0] for r in conn.execute(
        "SELECT DISTINCT project_name FROM projetos_status ORDER BY project_name")]
    rng = np.random.default_rng(42)
    print(f"▶️  Métricas de fluxo (CFD/cycle time/throughput/WIP) — {len(projetos)} projetos")
    for p in projetos:
        n, thr, p85 = simular(conn, p, rng)
        print(f"   {p:<12} concluídos={n:2d}  throughput={thr:.1f}/dia  cycle_time P85={p85:.1f}d")
    conn.close()
    print("✅ Métricas de fluxo concluídas.")


if __name__ == "__main__":
    main()
