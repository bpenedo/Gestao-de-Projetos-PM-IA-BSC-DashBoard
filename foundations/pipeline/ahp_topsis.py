"""
Decisão multicritério AHP-TOPSIS com DUPLA NORMALIZAÇÃO (2n) — escolha do melhor projeto.

- AHP (Saaty): pesos dos critérios a partir de uma matriz de comparação par a par
  + verificação de consistência (CR < 0,10).
- TOPSIS: ranqueia os projetos pela proximidade à solução ideal, em DUAS normalizações:
    (1) vetorial / Euclidiana   (2) min-max / linear
  Cada projeto recebe dois coeficientes de proximidade (Ci); o ranking final usa a média,
  e reportamos a CONCORDÂNCIA entre as duas (robustez do resultado).

Critérios (dos KPIs já calculados): VPL, TIR, ILL (benefício ↑), PSR (↑),
                                    IITA, IDLS (custo ↓).
Grava em decisao_mcda. Uso:  python3 ahp_topsis.py
Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
"""
import numpy as np

from db import get_conn, init_schema
from config import QUERIES_DIR

# Critério -> (rótulo, direção). benefit = maior é melhor; cost = menor é melhor.
CRITERIOS = [("vpl", "VPL", "benefit"), ("tir", "TIR", "benefit"), ("ill", "ILL", "benefit"),
             ("kpi_psr", "PSR", "benefit"), ("kpi_iita", "IITA", "cost"), ("kpi_idls_lean", "IDLS", "cost")]

# Matriz de comparação par a par de Saaty (ordem = CRITERIOS). Prioriza retorno financeiro.
AHP = np.array([
    # VPL  TIR  ILL  PSR  IITA IDLS
    [1,   2,   3,   3,   5,   5],   # VPL
    [1/2, 1,   2,   2,   4,   4],   # TIR
    [1/3, 1/2, 1,   1,   3,   3],   # ILL
    [1/3, 1/2, 1,   1,   3,   3],   # PSR
    [1/5, 1/4, 1/3, 1/3, 1,   1],   # IITA
    [1/5, 1/4, 1/3, 1/3, 1,   1],   # IDLS
], float)
RI = {1: 0, 2: 0, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41}


def pesos_ahp(A):
    """Autovetor principal -> pesos; retorna (pesos, CR)."""
    val, vec = np.linalg.eig(A)
    k = int(np.argmax(val.real))
    w = np.abs(vec[:, k].real); w = w / w.sum()
    lmax = val.real[k]
    n = A.shape[0]
    ci = (lmax - n) / (n - 1)
    cr = ci / RI[n] if RI.get(n) else 0.0
    return w, cr


def _topsis(X, w, dirs, modo):
    """Retorna Ci por alternativa para uma normalização ('vector' | 'minmax')."""
    X = X.astype(float)
    if modo == "vector":
        norm = np.sqrt((X ** 2).sum(axis=0))
        R = X / np.where(norm == 0, 1, norm)
        V = R * w
        ideal_pos = np.array([V[:, j].max() if dirs[j] == "benefit" else V[:, j].min() for j in range(V.shape[1])])
        ideal_neg = np.array([V[:, j].min() if dirs[j] == "benefit" else V[:, j].max() for j in range(V.shape[1])])
    else:  # min-max: direção embutida (maior sempre melhor)
        R = np.zeros_like(X)
        for j in range(X.shape[1]):
            col = X[:, j]; lo, hi = col.min(), col.max()
            rng = hi - lo if hi > lo else 1.0
            R[:, j] = (col - lo) / rng if dirs[j] == "benefit" else (hi - col) / rng
        V = R * w
        ideal_pos = V.max(axis=0)
        ideal_neg = V.min(axis=0)
    d_pos = np.sqrt(((V - ideal_pos) ** 2).sum(axis=1))
    d_neg = np.sqrt(((V - ideal_neg) ** 2).sum(axis=1))
    return d_neg / np.where((d_pos + d_neg) == 0, 1, (d_pos + d_neg))


def main():
    init_schema()
    conn = get_conn()
    kpis = {r["project_name"]: r for r in conn.execute((QUERIES_DIR / "kpis_bsc_ia.sql").read_text())}
    vpl = {r["project_name"]: r for r in conn.execute("SELECT * FROM vpl_resultado")}
    projetos = [p for p in kpis if p in vpl and vpl[p]["vpl"] is not None and kpis[p]["kpi_psr"] is not None]
    if len(projetos) < 2:
        print("⚠️  Precisa de ≥2 projetos com VPL e PSR para o ranking MCDA.")
        return

    def val(p, k):
        return (vpl[p][k] if k in ("vpl", "tir", "ill") else kpis[p][k]) or 0.0
    X = np.array([[val(p, k) for k, _, _ in CRITERIOS] for p in projetos], float)
    dirs = [d for _, _, d in CRITERIOS]

    w, cr = pesos_ahp(AHP)
    ci_v = _topsis(X, w, dirs, "vector")
    ci_m = _topsis(X, w, dirs, "minmax")
    ci_f = (ci_v + ci_m) / 2

    def ranks(ci):
        order = np.argsort(-ci)
        rk = np.empty(len(ci), int)
        for pos, idx in enumerate(order):
            rk[idx] = pos + 1
        return rk
    rk_v, rk_m, rk_f = ranks(ci_v), ranks(ci_m), ranks(ci_f)

    conn.execute("DELETE FROM decisao_mcda")
    for i, p in enumerate(projetos):
        conn.execute("""INSERT OR REPLACE INTO decisao_mcda
            (project_name, ci_vector, ci_minmax, ci_final, rank_final, rank_vector, rank_minmax, concordante)
            VALUES (?,?,?,?,?,?,?,?)""",
            (p, round(float(ci_v[i]), 4), round(float(ci_m[i]), 4), round(float(ci_f[i]), 4),
             int(rk_f[i]), int(rk_v[i]), int(rk_m[i]), int(rk_v[i] == rk_m[i])))
    conn.commit()

    print(f"AHP — pesos: " + " · ".join(f"{lab}={w[j]:.3f}" for j, (_, lab, _) in enumerate(CRITERIOS)))
    print(f"AHP — Razão de Consistência (CR) = {cr:.4f} " + ("✅ (< 0,10, consistente)" if cr < 0.10 else "⚠️ (rever julgamentos)"))
    concord = int((rk_v == rk_m).sum())
    print(f"TOPSIS 2n — concordância de posição entre as normalizações: {concord}/{len(projetos)}")
    vencedor = projetos[int(np.argmax(ci_f))]
    print(f"\n🏆 MELHOR PROJETO (AHP-TOPSIS 2n): {vencedor}  (Ci_final={ci_f.max():.4f})")
    conn.close()


if __name__ == "__main__":
    main()
