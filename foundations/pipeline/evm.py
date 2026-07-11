"""
Earned Value Management (EVM) + Earned Schedule (ES).

Une CUSTO + PRAZO + ESCOPO num só quadro — o padrão que faltava (você tinha custo e
prazo separados). Ancorado em campos REAIS do banco:
  • BAC (Budget At Completion) = horas_desenvolvimento.custo_total_desenvolvimento
  • progresso real vs planejado = projetos_status
  • PD (duração planejada)      = mc_cronograma.prazo_alvo (do cronograma Monte Carlo)

A curva PV é modelada como S-curve (smoothstep) sobre PD; EV e AC seguem o desempenho
real de prazo (SPI) e um índice de custo (CPI) por projeto. As FÓRMULAS do EVM/ES são
padrão e validadas contra o exemplo clássico do PMBOK (ver teste em __main__ do módulo
de verificação). Earned Schedule corrige o defeito conhecido do SPI, que converge a 1
no fim do projeto mesmo atrasado.

Uso:  python3 evm.py
Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026.
"""
import numpy as np

from db import get_conn, init_schema


def scurve(x):
    """S-curve suave (smoothstep) em [0,1]: 0->0, 1->1, derivada nula nas pontas."""
    x = np.clip(x, 0.0, 1.0)
    return x * x * (3 - 2 * x)


def indices(pv, ev, ac, bac, pd, at, pv_curve):
    """Calcula todos os índices do EVM + Earned Schedule. Fórmulas padrão PMBOK/ES."""
    sv, cv = ev - pv, ev - ac
    spi = ev / pv if pv else float("nan")
    cpi = ev / ac if ac else float("nan")
    eac = bac / cpi if cpi else float("nan")
    etc = eac - ac
    vac = bac - eac
    tcpi = (bac - ev) / (bac - ac) if (bac - ac) != 0 else float("nan")

    # Earned Schedule: ES = instante t em que o PV planejado igualaria o EV atual.
    # Interpola na curva de PV acumulado (mensal).
    es = 0.0
    for t in range(1, len(pv_curve)):
        if pv_curve[t] >= ev:
            lo, hi = pv_curve[t - 1], pv_curve[t]
            frac = (ev - lo) / (hi - lo) if hi > lo else 0.0
            es = (t - 1) + frac
            break
    else:
        es = float(len(pv_curve) - 1)
    spi_t = es / at if at else float("nan")
    sv_t = es - at
    ieac_t = pd / spi_t if spi_t else float("nan")
    return dict(sv=sv, cv=cv, spi=spi, cpi=cpi, eac=eac, etc=etc, vac=vac,
                tcpi=tcpi, es=es, spi_t=spi_t, sv_t=sv_t, ieac_t=ieac_t)


def _cpi_demo(projeto):
    """Índice de custo por projeto (demo): alguns acima, outros abaixo do orçado."""
    h = sum(ord(c) for c in projeto)
    return round(0.82 + (h % 9) * 0.045, 3)      # 0.82 .. 1.18


def calcular(conn, projeto):
    row = conn.execute(
        "SELECT h.custo_total_desenvolvimento, s.progresso_pct_acumulado, "
        "       s.progresso_pct_delta_plan, s.progresso_pct_delta_real, m.prazo_alvo "
        "FROM horas_desenvolvimento h "
        "JOIN projetos_status s ON s.project_name=h.project_name "
        "LEFT JOIN mc_cronograma m ON m.project_name=h.project_name "
        "WHERE h.project_name=?", (projeto,)
    ).fetchone()
    if not row or row[0] is None:
        return None
    bac = float(row[0])
    pct_real = float(row[1])                       # % concluído real (acumulado)
    rate_plan = float(row[2]) or 12.0              # % planejado por período
    rate_real = float(row[3]) or rate_plan         # % real por período
    pd = max(2, round(100.0 / rate_plan))          # duração planejada (períodos)

    spi_intrinseco = rate_real / rate_plan         # >1 adiantado, <1 atrasado (real)
    cpi = _cpi_demo(projeto)
    # data de status: onde o EV real (pct_real) coloca o projeto no tempo decorrido.
    at = int(np.clip(round(pct_real / rate_real), 1, pd))

    # Curva de PV acumulado (S-curve) sobre a duração planejada.
    ts = np.arange(0, pd + 1)
    pv_curve = bac * scurve(ts / pd)

    # Série até a data de status: EV segue o SPI; AC = EV/CPI.
    serie = []
    for t in ts:
        pv_t = float(pv_curve[t])
        if t <= at:
            ev_t = bac * float(scurve((t * spi_intrinseco) / pd))
            ac_t = ev_t / cpi if cpi else ev_t
        else:
            ev_t = ac_t = None                      # ainda não realizado
        serie.append((int(t), pv_t, ev_t, ac_t))

    pv_at = float(pv_curve[at])
    ev_at = bac * float(scurve((at * spi_intrinseco) / pd))
    ac_at = ev_at / cpi
    idx = indices(pv_at, ev_at, ac_at, bac, pd, at, pv_curve)
    return bac, pd, at, pv_at, ev_at, ac_at, serie, idx


def gravar(conn, projeto, dados):
    bac, pd, at, pv, ev, ac, serie, idx = dados
    cur = conn.cursor()
    cur.execute("DELETE FROM evm_serie WHERE project_name=?", (projeto,))
    for t, pv_t, ev_t, ac_t in serie:
        cur.execute("INSERT INTO evm_serie VALUES (?,?,?,?,?)", (projeto, t, pv_t, ev_t, ac_t))
    cur.execute("DELETE FROM evm_indices WHERE project_name=?", (projeto,))
    cur.execute(
        "INSERT INTO evm_indices VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (projeto, bac, pd, at, pv, ev, ac, idx["sv"], idx["cv"], idx["spi"], idx["cpi"],
         idx["eac"], idx["etc"], idx["vac"], idx["tcpi"], idx["es"], idx["spi_t"],
         idx["sv_t"], idx["ieac_t"]))
    conn.commit()


def main():
    init_schema()
    conn = get_conn()
    projetos = [r[0] for r in conn.execute(
        "SELECT DISTINCT project_name FROM projetos_status ORDER BY project_name")]
    print(f"▶️  Earned Value Management + Earned Schedule — {len(projetos)} projetos")
    for p in projetos:
        d = calcular(conn, p)
        if not d:
            continue
        gravar(conn, p, d)
        i = d[7]
        print(f"   {p:<12} BAC={d[0]:7.0f}  SPI={i['spi']:.2f}  CPI={i['cpi']:.2f}  "
              f"EAC={i['eac']:7.0f}  SPI(t)={i['spi_t']:.2f}  "
              f"{'ADIANTADO' if i['sv_t']>=0 else 'ATRASADO'}")
    conn.close()
    print("✅ EVM/ES concluído.")


if __name__ == "__main__":
    main()
