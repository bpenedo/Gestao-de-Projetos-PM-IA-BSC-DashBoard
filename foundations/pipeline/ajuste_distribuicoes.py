"""
Ajuste de distribuições aos dados reais de TOKENS ("Fit distributions to data").

Em vez de ARBITRAR a distribuição de uma variável de entrada, nós a INFERIMOS da
série histórica.
A série aqui é o consumo de tokens por geração (`logs_langfuse`), que é o
verdadeiro motor estocástico do custo de IA — e costuma ter CAUDA PESADA:
alguns prompts consomem 10× o típico, e é essa cauda que estoura o orçamento.

Por que isto importa (o "edge"):
  o VPL é LINEAR nos fluxos de caixa, então simular só os fluxos com uma
  Triangular simétrica produz um tornado que devolve os próprios fatores de
  desconto 1/(1+i)^t — informação nenhuma. O sinal está a montante: nos tokens.
  Ajustando a distribuição aos dados reais, a cauda de custo aparece no VPL.

Método:
  • Candidatas (MLE): Normal, LogNormal, Gama, Weibull, Exponencial, Uniforme,
    Logística, Rayleigh, Pareto, Triangular e Beta (reescalada).
  • Seleção por AIC = 2k − 2·log L (penaliza parâmetros a mais).
  • Aderência por Kolmogorov-Smirnov (estatística D e p-valor).
  A vencedora vira a distribuição de entrada usada no Monte Carlo.

Uso:  python3 ajuste_distribuicoes.py
Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
"""
import json
import warnings

import numpy as np
from scipy import stats

from db import get_conn, init_schema

# Candidatas: (rótulo, distribuição do scipy, kwargs de fit).
# `floc=0` fixa a locação em zero nas distribuições de suporte positivo — sem isso
# o MLE desliza a locação e o ajuste vira lixo numérico.
CANDIDATAS = [
    ("Normal",      stats.norm,        {}),
    ("LogNormal",   stats.lognorm,     {"floc": 0}),
    ("Gamma",       stats.gamma,       {"floc": 0}),
    ("Weibull",     stats.weibull_min, {"floc": 0}),
    ("Exponential", stats.expon,       {"floc": 0}),
    ("Uniform",     stats.uniform,     {}),
    ("Logistic",    stats.logistic,    {}),
    ("Rayleigh",    stats.rayleigh,    {"floc": 0}),
    ("Pareto",      stats.pareto,      {"floc": 0}),
    ("Triangular",  stats.triang,      {}),
    ("Beta",        stats.beta,        {}),
]

MIN_AMOSTRA = 10   # abaixo disso o ajuste por MLE não é confiável


def _serie_tokens(conn, projeto):
    """Tokens por geração (prompt + completion) do projeto."""
    linhas = conn.execute(
        "SELECT prompt_tokens + completion_tokens FROM logs_langfuse WHERE project_name = ?",
        (projeto,)).fetchall()
    return np.array([r[0] for r in linhas], float)


def ajustar(x):
    """Ajusta todas as candidatas a x e devolve a lista ordenada por AIC crescente."""
    x = np.asarray(x, float)
    x = x[np.isfinite(x) & (x > 0)]
    if x.size < MIN_AMOSTRA:
        return []

    resultados = []
    for rotulo, dist, kw in CANDIDATAS:
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                # Beta vive em [0,1]: reescalamos o suporte para o intervalo dos dados.
                if rotulo == "Beta":
                    lo, hi = x.min(), x.max()
                    kw = {"floc": lo, "fscale": (hi - lo) if hi > lo else 1.0}
                params = dist.fit(x, **kw)
                loglik = float(np.sum(dist.logpdf(x, *params)))
                if not np.isfinite(loglik):
                    continue
                # Parâmetros livres = total menos os que fixamos.
                k = len(params) - len(kw)
                aic = 2 * k - 2 * loglik
                ks = stats.kstest(x, dist.name, args=params)
        except Exception:
            continue
        resultados.append({
            "distribuicao": rotulo, "scipy": dist.name, "params": [float(p) for p in params],
            "loglik": loglik, "aic": float(aic),
            "ks_stat": float(ks.statistic), "ks_pvalue": float(ks.pvalue), "k": k,
        })

    resultados.sort(key=lambda r: r["aic"])
    return resultados


def melhor_ajuste(conn, projeto, variavel="TOKENS"):
    """Devolve (nome_scipy, params, n_obs) da distribuição escolhida — ou None."""
    linha = conn.execute("""SELECT distribuicao, parametros FROM mc_ajuste_distribuicao
                            WHERE project_name=? AND variavel=? AND escolhida=1""",
                         (projeto, variavel)).fetchone()
    if not linha:
        return None
    d = json.loads(linha["parametros"])
    return d["scipy"], d["params"], d["n_obs"]


def amostrar_ajustada(nome_scipy, params, n, rng):
    """Sorteia n valores da distribuição ajustada (usa o RNG do pipeline)."""
    return getattr(stats, nome_scipy).rvs(*params, size=n, random_state=rng)


def main():
    init_schema()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM mc_ajuste_distribuicao")

    projetos = [r[0] for r in cur.execute(
        "SELECT DISTINCT project_name FROM logs_langfuse ORDER BY project_name")]
    if not projetos:
        print("⚠️  Sem dados em logs_langfuse. Rode seed_demo.py ou sync_langfuse.py antes.")
        return

    for proj in projetos:
        x = _serie_tokens(conn, proj)
        ajustes = ajustar(x)
        if not ajustes:
            print(f"  {proj:12} amostra insuficiente ({x.size} < {MIN_AMOSTRA})")
            continue

        for i, r in enumerate(ajustes):
            payload = json.dumps({"scipy": r["scipy"], "params": r["params"], "n_obs": int(x.size)})
            cur.execute("""INSERT OR REPLACE INTO mc_ajuste_distribuicao
                (project_name, variavel, distribuicao, parametros, loglik, aic,
                 ks_stat, ks_pvalue, rank_, escolhida)
                VALUES (?,?,?,?,?,?,?,?,?,?)""",
                (proj, "TOKENS", r["distribuicao"], payload, r["loglik"], r["aic"],
                 r["ks_stat"], r["ks_pvalue"], i + 1, 1 if i == 0 else 0))

        v = ajustes[0]
        cauda = x.max() / np.median(x)
        print(f"  {proj:12} → {v['distribuicao']:11} AIC={v['aic']:11.1f}  "
              f"KS D={v['ks_stat']:.4f} (p={v['ks_pvalue']:.3f})  "
              f"n={x.size}  cauda(max/mediana)={cauda:.2f}×")

    conn.commit()
    conn.close()
    print(f"\n✅ Distribuições ajustadas a {len(projetos)} séries reais de tokens "
          f"({len(CANDIDATAS)} candidatas, seleção por AIC + aderência KS).")


if __name__ == "__main__":
    main()
