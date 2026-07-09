"""
Decisão multicritério integrada: DEMATEL → ELECTRE I · PROMETHEE II · MAUT · MCDA-C.

ARQUITETURA (de onde vem cada coisa)
------------------------------------
A ARQUITETURA de integração segue John, J. (2025), "Integration of DEMATEL with
Other MCDM Methods for Comprehensive Techno-Economic Analysis"
(foundations/mcda/): o DEMATEL revela a estrutura causal entre os critérios e
deriva PESOS POR INFLUÊNCIA, que então alimentam os métodos de ranqueamento —
em vez de pesos arbitrados. O artigo é uma revisão conceitual e não traz as
equações; ele demonstra o padrão DEMATEL → (pesos) → método de ranqueamento.

As EQUAÇÕES de cada método vêm da literatura canônica:
  • DEMATEL     — Gabus & Fontela (Battelle, 1972-73).
  • ELECTRE I   — Roy, B. (1968), concordância/discordância e núcleo (kernel).
  • PROMETHEE II— Brans & Vincke (1985), 6 funções de preferência e fluxo líquido φ.
  • MAUT        — Keeney & Raiffa (1976), utilidade aditiva com aversão a risco.
  • MCDA-C      — Ensslin, Montibeller & Noronha (2001), função de valor ancorada
                  em níveis Neutro (0) e Bom (100), com taxas de substituição.

O AHP-TOPSIS 2n já existente (ahp_topsis.py) entra no consenso como 5º método.

RISCO
-----
Dois critérios vêm do simulador de Monte Carlo (monte_carlo.py), de modo que a
escolha final seja ajustada a risco, e não apenas ao valor esperado:
  • P(VPL < 0)  — probabilidade de prejuízo (critério de custo).
  • VaR 5%      — percentil 5% do VPL, o pior cenário plausível (critério de benefício).

Uso:  python3 mcdm.py     (requer carregar_fluxo.py e monte_carlo.py antes)
Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
"""
import numpy as np

from db import get_conn, init_schema
from config import QUERIES_DIR

# Critério -> (rótulo, direção). benefit = maior é melhor; cost = menor é melhor.
CRITERIOS = [
    ("vpl",           "VPL",       "benefit"),
    ("tir",           "TIR",       "benefit"),
    ("ill",           "ILL",       "benefit"),
    ("kpi_psr",       "PSR",       "benefit"),
    ("kpi_iita",      "IITA",      "cost"),
    ("kpi_idls_lean", "IDLS",      "cost"),
    ("prob_vpl_neg",  "P(VPL<0)",  "cost"),      # Monte Carlo
    ("var_5",         "VaR 5%",    "benefit"),   # Monte Carlo
]

# Matriz de RELAÇÃO DIRETA do DEMATEL (julgamento de especialista).
# Z[i][j] = intensidade com que o critério i INFLUENCIA o critério j:
#   0 = nenhuma · 1 = baixa · 2 = média · 3 = alta · 4 = muito alta.
# Leitura: PSR (saúde do projeto) e IITA/IDLS (alucinação e desperdício) são
# CAUSAS — degradam o fluxo de caixa e, por consequência, VPL/TIR/ILL e o risco.
# VPL/TIR/ILL são EFEITOS: resultados finais, que não retroagem sobre a operação.
DEMATEL_Z = np.array([
    #        VPL TIR ILL PSR IITA IDLS P(VPL<0) VaR
    [0,   3,  3,  0,  0,  0,  3,  3],   # VPL
    [3,   0,  2,  0,  0,  0,  2,  2],   # TIR
    [3,   2,  0,  0,  0,  0,  2,  2],   # ILL
    [3,   3,  3,  0,  2,  2,  3,  3],   # PSR
    [3,   3,  2,  4,  0,  3,  3,  3],   # IITA  (alucinação)
    [3,   2,  2,  3,  2,  0,  2,  2],   # IDLS  (desperdício Lean)
    [1,   1,  1,  0,  0,  0,  0,  1],   # P(VPL<0) — é sobretudo um resultado
    [2,   1,  1,  0,  0,  0,  3,  0],   # VaR 5%   — a cauda dita a chance de prejuízo
], float)


# ---------------------------------------------------------------------------
# DEMATEL — Gabus & Fontela (Battelle).
# ---------------------------------------------------------------------------
def dematel(Z):
    """Z (relação direta) -> R, C, proeminência (R+C), relação (R-C), pesos, T, limiar.

    Passos: normaliza por s = max(maior soma de linha, maior soma de coluna);
    matriz de relação TOTAL T = X(I - X)^-1; R = somas das linhas, C = somas das
    colunas. Peso_i = sqrt((R+C)_i^2 + (R-C)_i^2), normalizado para somar 1.
    O limiar alpha = média de T define as arestas do diagrama de influência.
    """
    Z = np.asarray(Z, float)
    s = max(Z.sum(axis=1).max(), Z.sum(axis=0).max())
    X = Z / s
    n = X.shape[0]
    T = X @ np.linalg.inv(np.eye(n) - X)

    R, C = T.sum(axis=1), T.sum(axis=0)
    prominencia, relacao = R + C, R - C
    pesos = np.sqrt(prominencia ** 2 + relacao ** 2)
    pesos = pesos / pesos.sum()
    return R, C, prominencia, relacao, pesos, T, float(T.mean())


# ---------------------------------------------------------------------------
# Normalizações auxiliares.
# ---------------------------------------------------------------------------
def _minmax_dir(X, dirs):
    """Normaliza para [0,1] embutindo a direção (maior sempre melhor)."""
    X = np.asarray(X, float)
    Z = np.zeros_like(X)
    for j in range(X.shape[1]):
        col = X[:, j]
        lo, hi = col.min(), col.max()
        rng = hi - lo if hi > lo else 1.0
        Z[:, j] = (col - lo) / rng if dirs[j] == "benefit" else (hi - col) / rng
    return Z


# ---------------------------------------------------------------------------
# ELECTRE I — Roy (1968).
# ---------------------------------------------------------------------------
def electre_i(X, w, dirs, c_limiar=0.65, d_limiar=0.35):
    """Concordância/discordância -> relação de sobreclassificação e núcleo.

    C(a,b) = soma dos pesos dos critérios em que a é ao menos tão bom quanto b.
    D(a,b) = maior desvantagem de a frente a b, normalizada pela amplitude do critério.
    a sobreclassifica b  <=>  C(a,b) >= c_limiar  e  D(a,b) <= d_limiar.

    Devolve (score, nucleo, S) onde score = grau de sobreclassificação líquido
    (quantos a domina, menos quantos o dominam) e nucleo = alternativas não dominadas.
    """
    X = np.asarray(X, float)
    m, k = X.shape
    w = np.asarray(w, float) / np.sum(w)
    G = _minmax_dir(X, dirs)                       # tudo vira "maior é melhor"
    amplitude_col = np.ptp(G, axis=0)
    amplitudes = np.where(amplitude_col > 0, amplitude_col, 1.0)

    C = np.zeros((m, m))
    D = np.zeros((m, m))
    for a in range(m):
        for b in range(m):
            if a == b:
                continue
            C[a, b] = w[G[a] >= G[b]].sum()
            desvantagem = (G[b] - G[a]) / amplitudes
            D[a, b] = max(desvantagem.max(), 0.0)

    S = (C >= c_limiar) & (D <= d_limiar)          # matriz de sobreclassificação
    np.fill_diagonal(S, False)
    score = S.sum(axis=1) - S.sum(axis=0)          # grau líquido
    dominadas = S.any(axis=0)
    nucleo = [i for i in range(m) if not dominadas[i]]
    return score.astype(float), nucleo, S


# ---------------------------------------------------------------------------
# PROMETHEE II — Brans & Vincke (1985).
# ---------------------------------------------------------------------------
def _preferencia(d, tipo, q=0.0, p=1.0, s=0.5):
    """As 6 funções de preferência generalizadas de Brans. d = g(a) - g(b), já orientado."""
    d = np.maximum(d, 0.0)
    if tipo == "usual":
        return (d > 0).astype(float)
    if tipo == "u-shape":
        return (d > q).astype(float)
    if tipo == "v-shape":
        return np.clip(d / p, 0, 1) if p > 0 else (d > 0).astype(float)
    if tipo == "level":
        return np.where(d <= q, 0.0, np.where(d <= p, 0.5, 1.0))
    if tipo == "linear":                            # v-shape com indiferença
        return np.where(d <= q, 0.0, np.where(d <= p, (d - q) / (p - q) if p > q else 1.0, 1.0))
    if tipo == "gaussian":
        return 1 - np.exp(-(d ** 2) / (2 * s ** 2)) if s > 0 else (d > 0).astype(float)
    raise ValueError(f"função de preferência desconhecida: {tipo}")


def promethee_ii(X, w, dirs, tipo="linear"):
    """Fluxo líquido φ = φ⁺ − φ⁻ (pré-ordem completa).

    Default: função 'linear' (V-shape com indiferença), com q e p tirados dos
    quantis 10% e 90% dos desvios |d| de cada critério — prática usual quando não
    há limiares definidos por especialista.
    """
    X = np.asarray(X, float)
    m, k = X.shape
    w = np.asarray(w, float) / np.sum(w)
    G = _minmax_dir(X, dirs)

    PI = np.zeros((m, m))
    for j in range(k):
        d = G[:, j][:, None] - G[:, j][None, :]     # d[a,b] = g_j(a) - g_j(b)
        fora_diag = np.abs(d[~np.eye(m, dtype=bool)])
        q = float(np.quantile(fora_diag, 0.10)) if fora_diag.size else 0.0
        p = float(np.quantile(fora_diag, 0.90)) if fora_diag.size else 1.0
        if p <= q:
            p = q + 1e-9
        PI += w[j] * _preferencia(d, tipo, q=q, p=p)

    np.fill_diagonal(PI, 0.0)
    phi_mais = PI.sum(axis=1) / (m - 1)             # o quanto a domina os demais
    phi_menos = PI.sum(axis=0) / (m - 1)            # o quanto os demais dominam a
    return phi_mais - phi_menos


# ---------------------------------------------------------------------------
# MAUT — Keeney & Raiffa (1976).
# ---------------------------------------------------------------------------
def maut(X, w, dirs, aversao=2.0):
    """Utilidade aditiva U(a) = Σ w_j·u_j(a) com utilidade exponencial.

    u(z) = (1 - e^{-r·z}) / (1 - e^{-r}),  z ∈ [0,1] já orientado ao benefício.
    r > 0 => côncava => AVERSÃO A RISCO (ganhos marginais decrescentes).
    Válida sob independência aditiva em preferência/utilidade entre os critérios.
    """
    w = np.asarray(w, float) / np.sum(w)
    Z = _minmax_dir(X, dirs)
    r = float(aversao)
    U = (1 - np.exp(-r * Z)) / (1 - np.exp(-r)) if r != 0 else Z
    return U @ w


# ---------------------------------------------------------------------------
# MCDA-C — Ensslin, Montibeller & Noronha (2001).
# ---------------------------------------------------------------------------
def mcda_c(X, w, dirs, q_neutro=0.25, q_bom=0.75):
    """Função de valor ancorada: V=0 no nível Neutro, V=100 no nível Bom.

    Na ausência de descritores construídos com o decisor (fase de estruturação),
    ancoramos os níveis nos quartis observados do portfólio: Neutro = Q1 e Bom = Q3
    (invertidos nos critérios de custo). A função é linear por partes e EXTRAPOLA
    fora das âncoras — é isso que produz as faixas de diagnóstico do MCDA-C:
        V < 0      -> comprometedor
        0 ≤ V ≤ 100 -> competitivo
        V > 100    -> excelência
    """
    X = np.asarray(X, float)
    w = np.asarray(w, float) / np.sum(w)
    V = np.zeros_like(X)
    for j in range(X.shape[1]):
        col = X[:, j]
        if dirs[j] == "benefit":
            neutro, bom = np.quantile(col, q_neutro), np.quantile(col, q_bom)
        else:
            neutro, bom = np.quantile(col, 1 - q_neutro), np.quantile(col, 1 - q_bom)
        span = bom - neutro
        V[:, j] = 100.0 * (col - neutro) / span if span != 0 else 0.0
    return V @ w


# ---------------------------------------------------------------------------
# Ranking e consenso.
# ---------------------------------------------------------------------------
def _ranks(score):
    """Posição 1 = melhor (maior score)."""
    ordem = np.argsort(-np.asarray(score, float))
    rk = np.empty(len(score), int)
    for pos, idx in enumerate(ordem):
        rk[idx] = pos + 1
    return rk


def main():
    init_schema()
    conn = get_conn()
    cur = conn.cursor()

    kpis = {r["project_name"]: r for r in conn.execute((QUERIES_DIR / "kpis_bsc_ia.sql").read_text())}
    vpl = {r["project_name"]: r for r in conn.execute("SELECT * FROM vpl_resultado")}
    mc = {r["project_name"]: r for r in conn.execute(
        "SELECT project_name, prob_menor_zero, var_5 FROM mc_estatisticas WHERE variavel='VPL'")}

    projetos = [p for p in sorted(kpis)
                if p in vpl and p in mc and vpl[p]["vpl"] is not None and kpis[p]["kpi_psr"] is not None]
    if len(projetos) < 2:
        print("⚠️  Precisa de ≥2 projetos com VPL, PSR e Monte Carlo. Rode carregar_fluxo.py e monte_carlo.py.")
        return

    def valor(p, chave):
        if chave == "prob_vpl_neg":
            return mc[p]["prob_menor_zero"]
        if chave == "var_5":
            return mc[p]["var_5"]
        if chave in ("vpl", "tir", "ill"):
            return vpl[p][chave] or 0.0
        return kpis[p][chave] or 0.0

    X = np.array([[valor(p, k) for k, _, _ in CRITERIOS] for p in projetos], float)
    dirs = [d for _, _, d in CRITERIOS]

    # --- 1) DEMATEL: estrutura causal + pesos por influência --------------------
    R, C, prom, rel, pesos, T, limiar = dematel(DEMATEL_Z)

    cur.execute("DELETE FROM dematel_criterio")
    cur.execute("DELETE FROM dematel_relacao")
    for i, (chave, rotulo, _) in enumerate(CRITERIOS):
        cur.execute("""INSERT OR REPLACE INTO dematel_criterio
            (criterio, rotulo, r, c, prominencia, relacao, papel, peso) VALUES (?,?,?,?,?,?,?,?)""",
            (chave, rotulo, float(R[i]), float(C[i]), float(prom[i]), float(rel[i]),
             "causa" if rel[i] > 0 else "efeito", float(pesos[i])))
    for i, (ci, _, _) in enumerate(CRITERIOS):
        for j, (cj, _, _) in enumerate(CRITERIOS):
            cur.execute("""INSERT OR REPLACE INTO dematel_relacao
                (origem, destino, intensidade, acima_limiar) VALUES (?,?,?,?)""",
                (ci, cj, float(T[i, j]), int(T[i, j] > limiar)))

    # --- 2) Quatro métodos de ranqueamento, todos com os pesos do DEMATEL -------
    sc_electre, nucleo, _S = electre_i(X, pesos, dirs)
    sc_promethee = promethee_ii(X, pesos, dirs)
    sc_maut = maut(X, pesos, dirs)
    sc_mcdac = mcda_c(X, pesos, dirs)

    metodos = {
        "ELECTRE I":     sc_electre,
        "PROMETHEE II":  sc_promethee,
        "MAUT":          sc_maut,
        "MCDA-C":        sc_mcdac,
    }

    # 5º método: AHP-TOPSIS 2n já calculado por ahp_topsis.py.
    topsis = {r["project_name"]: r["ci_final"] for r in conn.execute("SELECT * FROM decisao_mcda")}
    if all(p in topsis for p in projetos):
        metodos["AHP-TOPSIS 2n"] = np.array([topsis[p] for p in projetos], float)

    cur.execute("DELETE FROM decisao_mcdm")
    posicoes = {}
    for nome, score in metodos.items():
        rk = _ranks(score)
        posicoes[nome] = rk
        for i, p in enumerate(projetos):
            cur.execute("INSERT OR REPLACE INTO decisao_mcdm (project_name, metodo, score, rank_) VALUES (?,?,?,?)",
                        (p, nome, round(float(score[i]), 6), int(rk[i])))

    # --- 3) Consenso entre métodos: contagem de Borda --------------------------
    n_alt, n_met = len(projetos), len(metodos)
    matriz_rk = np.array([posicoes[m] for m in metodos], float)   # (n_metodos, n_alt)
    rank_medio = matriz_rk.mean(axis=0)
    borda = ((n_alt - matriz_rk).sum(axis=0)).astype(int)
    rank_final = _ranks(borda)
    unanime = (matriz_rk == matriz_rk[0]).all(axis=0)

    cur.execute("DELETE FROM decisao_consenso")
    for i, p in enumerate(projetos):
        cur.execute("""INSERT OR REPLACE INTO decisao_consenso
            (project_name, rank_medio, borda, rank_final, unanime) VALUES (?,?,?,?,?)""",
            (p, round(float(rank_medio[i]), 3), int(borda[i]), int(rank_final[i]), int(unanime[i])))
    conn.commit()

    # --- Relatório -------------------------------------------------------------
    print("DEMATEL — estrutura causal dos critérios (limiar α = %.4f):" % limiar)
    for i, (_, rotulo, _) in enumerate(CRITERIOS):
        papel = "CAUSA " if rel[i] > 0 else "efeito"
        print(f"  {rotulo:9} R+C={prom[i]:6.3f}  R-C={rel[i]:+6.3f}  {papel}  peso={pesos[i]:.4f}")

    print(f"\nELECTRE I — núcleo (não dominadas): {', '.join(projetos[i] for i in nucleo) or '(vazio)'}")
    print(f"\nRanking por método ({n_met} métodos, {n_alt} projetos):")
    cab = "  " + "PROJETO".ljust(12) + "".join(m.rjust(15) for m in metodos) + "CONSENSO".rjust(11)
    print(cab)
    for i, p in enumerate(projetos):
        linha = "  " + p.ljust(12)
        for m in metodos:
            linha += f"{posicoes[m][i]}º".rjust(15)
        linha += f"{rank_final[i]}º".rjust(11)
        print(linha)

    vencedor = projetos[int(np.argmax(borda))]
    concordancia = int(unanime.sum())
    print(f"\n🏆 MELHOR PROJETO (consenso Borda de {n_met} métodos): {vencedor}")
    print(f"   Concordância unânime entre métodos em {concordancia}/{n_alt} projetos.")
    print(f"   Risco do vencedor: P(VPL<0)={mc[vencedor]['prob_menor_zero']:.2f}%  "
          f"VaR 5%={mc[vencedor]['var_5']:,.2f}")
    conn.close()


if __name__ == "__main__":
    main()
