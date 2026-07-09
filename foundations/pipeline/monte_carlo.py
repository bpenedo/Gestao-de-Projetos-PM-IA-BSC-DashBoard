"""
Simulador de Monte Carlo dos fluxos de caixa do portfólio — compatível com o
SimulAr v2.5 (Luciano Machain, Universidad Nacional de Rosario, Argentina).

Replica a especificação do manual do usuário (foundations/mc/simularusermanual.pdf):

  • 20 distribuições de entrada (tela "Select Input Variable Probability Distribution").
  • Matriz de correlação entre variáveis de entrada + validação de consistência
    (a matriz precisa ser positiva definida). Correlação imposta por Iman-Conover,
    que preserva EXATAMENTE as distribuições marginais.
  • Estatísticas descritivas na ordem e definição do manual (p. 59-60):
    mínimo, média, máximo, mediana, variância, desvio-padrão, amplitude,
    curtose, assimetria, coeficiente de variação e percentis de 1% a 99% (passo 1%).
    Curtose e assimetria usam as fórmulas do Excel (KURT/SKEW), que é o que o
    SimulAr — um add-in de Excel — reporta.
  • Histograma de frequência com 100 classes e coluna "Cumul. %" (p. 60-62).
  • "Probability less than" — P(X < v) (p. 62).
  • Tornado de sensibilidade (p. 63-64), nas duas formas do manual:
      1) Regressão: coeficientes beta da regressão múltipla das entradas contra a
         saída, ordenados pelo valor absoluto.
      2) Correlação: coeficiente de correlação de Pearson entrada × saída.

O default de 10.000 iterações e 100 classes reproduz o exemplo do manual (uma
frequência de 1 aparece como 0,01% e as classes vão do mínimo ao máximo).

Saídas simuladas por projeto: VPL, TIR, TIRM, VUL e ILL. As métricas de risco
(P(VPL<0), VaR 5% e CVaR 5%) alimentam a decisão multicritério em mcdm.py.

Uso:  python3 monte_carlo.py
Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
"""
import numpy as np

from db import get_conn, init_schema
from config import MC_ITERACOES, MC_BINS, MC_SEED, MC_VAR_PCT

SAIDAS = ("VPL", "TIR", "TIRM", "VUL", "ILL")


# ---------------------------------------------------------------------------
# 1) As 20 distribuições de entrada do SimulAr.
#    Cada função recebe (rng, n, **params) e devolve um vetor de n amostras.
# ---------------------------------------------------------------------------
DISTRIBUICOES = {
    "Normal":          lambda rng, n, media, desvio: rng.normal(media, desvio, n),
    "Triangular":      lambda rng, n, minimo, moda, maximo: rng.triangular(minimo, moda, maximo, n),
    "Uniform":         lambda rng, n, minimo, maximo: rng.uniform(minimo, maximo, n),
    "Beta":            lambda rng, n, alfa, beta, minimo=0.0, maximo=1.0: minimo + (maximo - minimo) * rng.beta(alfa, beta, n),
    "ChiSquare":       lambda rng, n, gl: rng.chisquare(gl, n),
    # LogNormal  -> parametrizada pela média/desvio DA PRÓPRIA lognormal.
    "LogNormal":       lambda rng, n, media, desvio: rng.lognormal(
                            np.log(media ** 2 / np.sqrt(desvio ** 2 + media ** 2)),
                            np.sqrt(np.log(1 + (desvio / media) ** 2)), n),
    # LogNormal2 -> parametrizada pela média/desvio da normal SUBJACENTE.
    "LogNormal2":      lambda rng, n, mu, sigma: rng.lognormal(mu, sigma, n),
    "Gamma":           lambda rng, n, forma, escala: rng.gamma(forma, escala, n),
    "Logistic":        lambda rng, n, loc, escala: rng.logistic(loc, escala, n),
    "Exponential":     lambda rng, n, lam: rng.exponential(1.0 / lam, n),
    "StudentT":        lambda rng, n, gl: rng.standard_t(gl, n),
    "Pareto":          lambda rng, n, xm, alfa: xm * (1 + rng.pareto(alfa, n)),
    "Weibull":         lambda rng, n, forma, escala: escala * rng.weibull(forma, n),
    "Rayleigh":        lambda rng, n, sigma: rng.rayleigh(sigma, n),
    "Binomial":        lambda rng, n, ensaios, p: rng.binomial(ensaios, p, n).astype(float),
    "NegativeBinomial": lambda rng, n, sucessos, p: rng.negative_binomial(sucessos, p, n).astype(float),
    "Geometric":       lambda rng, n, p: rng.geometric(p, n).astype(float),
    "Poisson":         lambda rng, n, lam: rng.poisson(lam, n).astype(float),
    "Discrete":        lambda rng, n, valores, probs: rng.choice(np.asarray(valores, float), size=n, p=np.asarray(probs, float)),
    "DiscreteUniform": lambda rng, n, minimo, maximo: rng.integers(minimo, maximo + 1, n).astype(float),
}


def amostrar(nome, n, rng, **params):
    """Gera n amostras da distribuição `nome` com os parâmetros informados."""
    if nome not in DISTRIBUICOES:
        raise ValueError(f"Distribuição desconhecida: {nome}. Disponíveis: {sorted(DISTRIBUICOES)}")
    return np.asarray(DISTRIBUICOES[nome](rng, n, **params), float)


# ---------------------------------------------------------------------------
# 2) Matriz de correlação: validação de consistência + imposição por Iman-Conover.
# ---------------------------------------------------------------------------
def validar_matriz(R):
    """'Validate Matrix Consistency' do SimulAr: simétrica, diagonal 1, positiva definida.

    Retorna (ok, mensagem).
    """
    R = np.asarray(R, float)
    if R.ndim != 2 or R.shape[0] != R.shape[1]:
        return False, "a matriz não é quadrada"
    if not np.allclose(R, R.T, atol=1e-8):
        return False, "a matriz não é simétrica"
    if not np.allclose(np.diag(R), 1.0, atol=1e-8):
        return False, "a diagonal principal precisa ser 1"
    autovalores = np.linalg.eigvalsh(R)
    if autovalores.min() <= 0:
        return False, f"a matriz não é positiva definida (menor autovalor = {autovalores.min():.6f})"
    return True, "matriz consistente"


def iman_conover(X, R, rng):
    """Impõe a correlação de postos alvo R às colunas de X, preservando as marginais.

    Iman & Conover (1982). Reordena cada coluna de X segundo os postos de uma
    referência normal multivariada com a correlação desejada — por isso as
    distribuições marginais sorteadas continuam EXATAS.
    """
    X = np.asarray(X, float)
    n, k = X.shape
    ok, msg = validar_matriz(R)
    if not ok:
        raise ValueError(f"matriz de correlação inválida: {msg}")

    # Escores de van der Waerden, embaralhados de forma independente por coluna.
    escores = np.sort(_norm_ppf((np.arange(1, n + 1)) / (n + 1)))
    M = np.column_stack([rng.permutation(escores) for _ in range(k)])

    P = np.linalg.cholesky(np.asarray(R, float))       # alvo
    Q = np.linalg.cholesky(np.corrcoef(M, rowvar=False))  # correlação acidental de M
    S = M @ np.linalg.solve(Q, P).T                     # S tem, aproximadamente, a correlação R

    saida = np.empty_like(X)
    for j in range(k):
        ordem_alvo = np.argsort(np.argsort(S[:, j]))    # postos desejados
        saida[:, j] = np.sort(X[:, j])[ordem_alvo]
    return saida


def _norm_ppf(p):
    """Quantil da normal padrão (Acklam), sem exigir SciPy."""
    from math import sqrt, log
    p = np.asarray(p, float)
    a = [-3.969683028665376e+01, 2.209460984245205e+02, -2.759285104469687e+02,
         1.383577518672690e+02, -3.066479806614716e+01, 2.506628277459239e+00]
    b = [-5.447609879822406e+01, 1.615858368580409e+02, -1.556989798598866e+02,
         6.680131188771972e+01, -1.328068155288572e+01]
    c = [-7.784894002430293e-03, -3.223964580411365e-01, -2.400758277161838e+00,
         -2.549732539343734e+00, 4.374664141464968e+00, 2.938163982698783e+00]
    d = [7.784695709041462e-03, 3.224671290700398e-01, 2.445134137142996e+00, 3.754408661907416e+00]
    plow, phigh = 0.02425, 1 - 0.02425
    out = np.empty_like(p)
    lo, hi = p < plow, p > phigh
    mid = ~(lo | hi)
    q = np.sqrt(-2 * np.log(p[lo])) if lo.any() else np.array([])
    if lo.any():
        out[lo] = (((((c[0]*q+c[1])*q+c[2])*q+c[3])*q+c[4])*q+c[5]) / ((((d[0]*q+d[1])*q+d[2])*q+d[3])*q+1)
    q = np.sqrt(-2 * np.log(1 - p[hi])) if hi.any() else np.array([])
    if hi.any():
        out[hi] = -(((((c[0]*q+c[1])*q+c[2])*q+c[3])*q+c[4])*q+c[5]) / ((((d[0]*q+d[1])*q+d[2])*q+d[3])*q+1)
    if mid.any():
        q = p[mid] - 0.5
        r = q * q
        out[mid] = (((((a[0]*r+a[1])*r+a[2])*r+a[3])*r+a[4])*r+a[5])*q / (((((b[0]*r+b[1])*r+b[2])*r+b[3])*r+b[4])*r+1)
    return out


# ---------------------------------------------------------------------------
# 3) Estatísticas descritivas — definições do Excel (o SimulAr é um add-in dele).
# ---------------------------------------------------------------------------
def estatisticas(x):
    """Devolve as 10 estatísticas do manual (p.59-60) + VaR/CVaR de 5%."""
    x = np.asarray(x, float)
    n = x.size
    media = float(x.mean())
    desvio = float(x.std(ddof=1))                       # DESVPAD.A do Excel (n-1)
    z = (x - media) / desvio if desvio > 0 else np.zeros_like(x)
    # SKEW do Excel
    assimetria = float(n / ((n - 1) * (n - 2)) * np.sum(z ** 3)) if n > 2 and desvio > 0 else 0.0
    # KURT do Excel (curtose em EXCESSO)
    if n > 3 and desvio > 0:
        curtose = float(n * (n + 1) / ((n - 1) * (n - 2) * (n - 3)) * np.sum(z ** 4)
                        - 3 * (n - 1) ** 2 / ((n - 2) * (n - 3)))
    else:
        curtose = 0.0
    p5 = float(np.percentile(x, 5))
    cauda = x[x <= p5]
    return {
        "iteracoes": n,
        "minimo": float(x.min()),
        "media": media,
        "maximo": float(x.max()),
        "mediana": float(np.median(x)),
        "variancia": float(x.var(ddof=1)),
        "desvio_padrao": desvio,
        "amplitude": float(x.max() - x.min()),
        "curtose": curtose,
        "assimetria": assimetria,
        "coef_variacao": float(desvio / media) if media != 0 else float("nan"),
        "prob_menor_zero": prob_menor_que(x, 0.0),
        "var_5": p5,
        "cvar_5": float(cauda.mean()) if cauda.size else p5,
    }


def percentis(x):
    """Percentis de 1% a 99%, passo 1% (PERCENTIL.INC do Excel = interpolação linear)."""
    ps = np.arange(1, 100)
    return list(zip(ps.tolist(), np.percentile(np.asarray(x, float), ps).tolist()))


def prob_menor_que(x, valor):
    """'Probability less than' do SimulAr, em porcentagem."""
    return float((np.asarray(x, float) < valor).mean() * 100.0)


# ---------------------------------------------------------------------------
# 4) Histograma de frequência (100 classes do mínimo ao máximo) + Cumul. %.
# ---------------------------------------------------------------------------
def histograma(x, bins=MC_BINS):
    x = np.asarray(x, float)
    bordas = np.linspace(x.min(), x.max(), bins + 1)
    freq, _ = np.histogram(x, bins=bordas)
    cumul = np.cumsum(freq) / x.size * 100.0
    return bordas, freq, cumul


# ---------------------------------------------------------------------------
# 5) Tornado de sensibilidade: regressão múltipla (betas) e correlação (Pearson).
# ---------------------------------------------------------------------------
def tornado(entradas, saida):
    """entradas: dict {nome: vetor}; saida: vetor. Ordena por |beta| decrescente."""
    nomes = list(entradas)
    A = np.column_stack([np.asarray(entradas[k], float) for k in nomes])
    y = np.asarray(saida, float)

    # Regressão múltipla com intercepto -> betas NÃO padronizados: "se a entrada
    # sobe 1, a saída sobe beta" (interpretação do manual, p. 64).
    Xd = np.column_stack([np.ones(len(y)), A])
    betas = np.linalg.lstsq(Xd, y, rcond=None)[0][1:]

    corrs = np.array([
        np.corrcoef(A[:, j], y)[0, 1] if A[:, j].std() > 0 else 0.0
        for j in range(A.shape[1])
    ])
    ordem = np.argsort(-np.abs(betas))
    return [(nomes[i], float(betas[i]), float(np.nan_to_num(corrs[i]))) for i in ordem]


# ---------------------------------------------------------------------------
# 6) Modelo financeiro vetorizado (mesmas fórmulas de carregar_fluxo.py).
# ---------------------------------------------------------------------------
def _vpl(F, taxa):
    """F: (n_iter, n_periodos). Desconta cada período t por (1+taxa)^t."""
    t = np.arange(F.shape[1])
    return (F / (1 + taxa) ** t).sum(axis=1)


def _tir(F, lo=-0.95, hi=10.0, iters=200):
    """TIR por bisseção vetorizada (raiz de VPL=0). NaN onde não há troca de sinal."""
    lo = np.full(F.shape[0], lo)
    hi = np.full(F.shape[0], hi)
    f_lo, f_hi = _vpl(F, lo[:, None]), _vpl(F, hi[:, None])
    sem_raiz = f_lo * f_hi > 0
    for _ in range(iters):
        mid = (lo + hi) / 2
        f_mid = _vpl(F, mid[:, None])
        esquerda = f_lo * f_mid < 0
        hi = np.where(esquerda, mid, hi)
        lo = np.where(esquerda, lo, mid)
        f_lo = np.where(esquerda, f_lo, f_mid)
    out = (lo + hi) / 2
    out[sem_raiz] = np.nan
    return out


def _tirm(F, taxa):
    """TIRM/MIRR: FV das entradas reinvestidas ÷ PV das saídas, à taxa do projeto."""
    n = F.shape[1] - 1
    t = np.arange(F.shape[1])
    pos, neg = np.where(F > 0, F, 0.0), np.where(F < 0, F, 0.0)
    fv_pos = (pos * (1 + taxa) ** (n - t)).sum(axis=1)
    pv_neg = -(neg / (1 + taxa) ** t).sum(axis=1)
    with np.errstate(invalid="ignore", divide="ignore"):
        out = (fv_pos / pv_neg) ** (1.0 / n) - 1
    return np.where((pv_neg > 0) & (fv_pos > 0), out, np.nan)


def _vul(vpl, taxa, n):
    """VUL: anuidade equivalente do VPL (fator de recuperação de capital)."""
    if n <= 0:
        return np.full_like(vpl, np.nan)
    if taxa == 0:
        return vpl / n
    return vpl * (taxa / (1 - (1 + taxa) ** (-n)))


def _ill(F, taxa):
    """ILL/PI: VP das entradas ÷ investimento inicial."""
    t = np.arange(1, F.shape[1])
    vp_entradas = (np.where(F[:, 1:] > 0, F[:, 1:], 0.0) / (1 + taxa) ** t).sum(axis=1)
    invest = np.abs(np.where(F[:, 0] < 0, F[:, 0], np.nan))
    with np.errstate(invalid="ignore", divide="ignore"):
        return vp_entradas / invest


# ---------------------------------------------------------------------------
# 7) Simulação de um projeto.
# ---------------------------------------------------------------------------
def simular_projeto(fluxos_base, taxa, n_iter=MC_ITERACOES, rng=None, pct=MC_VAR_PCT, correlacao=None):
    """Cada fluxo de caixa periódico vira uma variável de entrada Triangular.

    Triangular(min, moda, max) com moda = fluxo determinístico e caudas a ±`pct`.
    É a escolha default do exemplo de projeto do manual do SimulAr; para um fluxo
    negativo (investimento) as caudas se invertem, mantendo min < moda < max.

    `correlacao`: matriz (n_periodos × n_periodos) opcional entre os fluxos.
    """
    rng = rng or np.random.default_rng(MC_SEED)
    fluxos_base = np.asarray(fluxos_base, float)
    n_per = fluxos_base.size

    colunas, entradas = [], {}
    for t, base in enumerate(fluxos_base):
        lo, hi = sorted((base * (1 - pct), base * (1 + pct)))
        col = amostrar("Triangular", n_iter, rng, minimo=lo, moda=float(base), maximo=hi)
        colunas.append(col)
        entradas[f"Periodo_{t}"] = col

    F = np.column_stack(colunas)
    if correlacao is not None:
        F = iman_conover(F, correlacao, rng)
        entradas = {f"Periodo_{t}": F[:, t] for t in range(n_per)}

    vpl = _vpl(F, taxa)
    resultados = {
        "VPL": vpl,
        "TIR": _tir(F),
        "TIRM": _tirm(F, taxa),
        "VUL": _vul(vpl, taxa, n_per - 1),
        "ILL": _ill(F, taxa),
    }
    return entradas, resultados


# ---------------------------------------------------------------------------
# 8) Persistência.
# ---------------------------------------------------------------------------
def _gravar(conn, projeto, entradas, resultados):
    cur = conn.cursor()
    for var, bruto in resultados.items():
        x = np.asarray(bruto, float)
        x = x[np.isfinite(x)]
        if x.size < 10 or x.min() == x.max():
            continue   # TIR pode não convergir; sem variação não há histograma

        est = estatisticas(x)
        cur.execute("""INSERT OR REPLACE INTO mc_estatisticas
            (project_name, variavel, iteracoes, minimo, media, maximo, mediana, variancia,
             desvio_padrao, amplitude, curtose, assimetria, coef_variacao,
             prob_menor_zero, var_5, cvar_5)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (projeto, var, est["iteracoes"], est["minimo"], est["media"], est["maximo"],
             est["mediana"], est["variancia"], est["desvio_padrao"], est["amplitude"],
             est["curtose"], est["assimetria"], est["coef_variacao"],
             est["prob_menor_zero"], est["var_5"], est["cvar_5"]))

        cur.executemany(
            "INSERT OR REPLACE INTO mc_percentis (project_name, variavel, percentil, valor) VALUES (?,?,?,?)",
            [(projeto, var, p, v) for p, v in percentis(x)])

        bordas, freq, cumul = histograma(x)
        cur.executemany("""INSERT OR REPLACE INTO mc_histograma
            (project_name, variavel, bin_idx, bin_inferior, bin_superior, frequencia, cumul_pct)
            VALUES (?,?,?,?,?,?,?)""",
            [(projeto, var, i, float(bordas[i]), float(bordas[i + 1]), int(freq[i]), float(cumul[i]))
             for i in range(len(freq))])

        mascara = np.isfinite(np.asarray(bruto, float))
        ent_validas = {k: v[mascara] for k, v in entradas.items()}
        cur.executemany("""INSERT OR REPLACE INTO mc_tornado
            (project_name, variavel_saida, variavel_entrada, beta_regressao, coef_correlacao, ordem)
            VALUES (?,?,?,?,?,?)""",
            [(projeto, var, nome, beta, corr, i)
             for i, (nome, beta, corr) in enumerate(tornado(ent_validas, np.asarray(bruto, float)[mascara]))])


def main():
    init_schema()
    conn = get_conn()
    cur = conn.cursor()
    for tabela in ("mc_estatisticas", "mc_percentis", "mc_histograma", "mc_tornado"):
        cur.execute(f"DELETE FROM {tabela}")

    projetos = [r[0] for r in cur.execute(
        "SELECT DISTINCT project_name FROM fluxo_caixa ORDER BY project_name")]
    if not projetos:
        print("⚠️  Sem fluxo de caixa. Rode carregar_fluxo.py antes.")
        return

    rng = np.random.default_rng(MC_SEED)
    for proj in projetos:
        linhas = cur.execute(
            "SELECT periodo, fluxo, taxa FROM fluxo_caixa WHERE project_name=? ORDER BY periodo",
            (proj,)).fetchall()
        fluxos = [r["fluxo"] for r in linhas]
        taxa = linhas[0]["taxa"]
        entradas, resultados = simular_projeto(fluxos, taxa, rng=rng)
        _gravar(conn, proj, entradas, resultados)

        vpl = resultados["VPL"]
        print(f"  {proj:12} VPL médio={vpl.mean():10,.2f}  P(VPL<0)={prob_menor_que(vpl, 0):5.2f}%  "
              f"VaR5%={np.percentile(vpl, 5):10,.2f}")

    conn.commit()
    conn.close()
    print(f"\n✅ Monte Carlo: {len(projetos)} projetos × {MC_ITERACOES:,} iterações × {MC_BINS} classes "
          f"(semente {MC_SEED}, reprodutível).")


if __name__ == "__main__":
    main()
