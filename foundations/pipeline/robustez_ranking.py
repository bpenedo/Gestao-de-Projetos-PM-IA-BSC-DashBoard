"""
Robustez do ranking multicritério: perturbação de Dirichlet nos pesos do DEMATEL.

O PROBLEMA
----------
Todo método MCDM devolve um vencedor com uma confiança implícita de 100%. Mas os
pesos dos critérios nunca são exatos — são estimativas. Se um deslocamento de 2 pontos
percentuais no peso do IITA troca o 1º com o 2º colocado, o "vencedor" é um artefato
da estimativa, não um fato do portfólio. Ninguém reporta isso; e é onde as decisões
morrem no comitê.

A SOLUÇÃO
---------
Perturbamos os pesos e reranqueamos N vezes:

    w' ~ Dirichlet(κ · w)

A Dirichlet é a escolha natural: seu suporte é exatamente o simplex (pesos positivos
que somam 1), e ela tem a propriedade E[w'] = w — perturbamos SEM enviesar. O κ
(concentração) controla a dispersão: κ→∞ devolve os pesos originais; κ pequeno espalha.
Var(w'_i) = w_i(1-w_i)/(κ+1), então κ=200 dá ~±2 p.p. num peso de 13%.

O veredito deixa de ser *"Project C é o melhor"* e passa a ser
*"Project C vence em 78% dos universos de preferência plausíveis"* — um intervalo de
confiança sobre a própria decisão. É o que separa uma recomendação defensável de um
palpite com verniz matemático.

Uso:  python3 robustez_ranking.py     (requer mcdm.py antes)
Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
"""
import numpy as np

from db import get_conn, init_schema
from config import QUERIES_DIR, MC_SEED, MC_ROBUSTEZ_ITER, MC_ROBUSTEZ_KAPPA
from mcdm import CRITERIOS, electre_i, promethee_ii, maut, mcda_c, _ranks
from ahp_topsis import _topsis

METODOS = ("ELECTRE I", "PROMETHEE II", "MAUT", "MCDA-C", "AHP-TOPSIS 2n")


def _pontuacoes(X, w, dirs):
    """Score de cada método para um vetor de pesos. Maior = melhor, sempre."""
    ci_v = _topsis(X, w, dirs, "vector")
    ci_m = _topsis(X, w, dirs, "minmax")
    return {
        "ELECTRE I":     electre_i(X, w, dirs)[0],
        "PROMETHEE II":  promethee_ii(X, w, dirs),
        "MAUT":          maut(X, w, dirs),
        "MCDA-C":        mcda_c(X, w, dirs),
        "AHP-TOPSIS 2n": (ci_v + ci_m) / 2,
    }


def simular(X, dirs, w0, n_iter=MC_ROBUSTEZ_ITER, kappa=MC_ROBUSTEZ_KAPPA, seed=MC_SEED):
    """Reranqueia n_iter vezes com pesos perturbados. Devolve posições (método -> matriz)."""
    rng = np.random.default_rng(seed)
    n_alt = X.shape[0]
    posicoes = {m: np.empty((n_iter, n_alt), int) for m in METODOS}
    posicoes["CONSENSO (Borda)"] = np.empty((n_iter, n_alt), int)

    alpha = kappa * np.asarray(w0, float)
    for i in range(n_iter):
        w = rng.dirichlet(alpha)
        rks = {m: _ranks(s) for m, s in _pontuacoes(X, w, dirs).items()}
        for m, rk in rks.items():
            posicoes[m][i] = rk
        # consenso de Borda desta iteração
        borda = sum(n_alt - rk for rk in rks.values())
        posicoes["CONSENSO (Borda)"][i] = _ranks(borda)
    return posicoes


def main():
    init_schema()
    conn = get_conn()
    cur = conn.cursor()

    kpis = {r["project_name"]: r for r in conn.execute((QUERIES_DIR / "kpis_bsc_ia.sql").read_text())}
    vpl = {r["project_name"]: r for r in conn.execute("SELECT * FROM vpl_resultado")}
    mc = {r["project_name"]: r for r in conn.execute(
        "SELECT project_name, prob_menor_zero, var_5 FROM mc_estatisticas WHERE variavel='VPL'")}
    pesos = {r["criterio"]: r["peso"] for r in conn.execute("SELECT criterio, peso FROM dematel_criterio")}

    if not pesos:
        print("⚠️  Rode mcdm.py antes (os pesos vêm do DEMATEL).")
        return

    projetos = [p for p in sorted(kpis)
                if p in vpl and p in mc and vpl[p]["vpl"] is not None and kpis[p]["kpi_psr"] is not None]
    if len(projetos) < 2:
        print("⚠️  Precisa de ≥2 projetos.")
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
    w0 = np.array([pesos[k] for k, _, _ in CRITERIOS], float)

    posicoes = simular(X, dirs, w0)
    n_iter, n_alt = posicoes["CONSENSO (Borda)"].shape

    cur.execute("DELETE FROM mcdm_robustez")
    cur.execute("DELETE FROM mcdm_robustez_dist")
    for metodo, M in posicoes.items():
        for j, p in enumerate(projetos):
            col = M[:, j]
            cur.execute("""INSERT OR REPLACE INTO mcdm_robustez
                (project_name, metodo, prob_vitoria, prob_top3, rank_medio, rank_p05, rank_p95)
                VALUES (?,?,?,?,?,?,?)""",
                (p, metodo, float((col == 1).mean() * 100), float((col <= 3).mean() * 100),
                 float(col.mean()), float(np.percentile(col, 5)), float(np.percentile(col, 95))))

    # Distribuição completa das posições no consenso (para o histograma do dashboard).
    C = posicoes["CONSENSO (Borda)"]
    for j, p in enumerate(projetos):
        for pos in range(1, n_alt + 1):
            freq = int((C[:, j] == pos).sum())
            if freq:
                cur.execute("""INSERT OR REPLACE INTO mcdm_robustez_dist
                    (project_name, posicao, frequencia, pct) VALUES (?,?,?,?)""",
                    (p, pos, freq, float(freq / n_iter * 100)))
    conn.commit()

    # ---- Relatório -----------------------------------------------------------
    print(f"Perturbação de Dirichlet: w' ~ Dir(κ·w), κ={MC_ROBUSTEZ_KAPPA}, {n_iter:,} universos de preferência.")
    print(f"Desvio-padrão induzido num peso de 13%: ±{np.sqrt(0.13*0.87/(MC_ROBUSTEZ_KAPPA+1))*100:.2f} p.p.\n")

    prob = {p: float((C[:, j] == 1).mean() * 100) for j, p in enumerate(projetos)}
    ordem = sorted(projetos, key=lambda p: -prob[p])
    print("Probabilidade de VENCER o consenso (Borda), sob pesos perturbados:")
    for p in ordem:
        j = projetos.index(p)
        col = C[:, j]
        if prob[p] < 0.05:
            continue
        barra = "█" * int(prob[p] / 2)
        print(f"  {p:12} {prob[p]:5.1f}%  {barra:<50} posição típica {col.mean():.2f} "
              f"[{np.percentile(col,5):.0f}–{np.percentile(col,95):.0f}]")

    lider = ordem[0]
    print(f"\n🏆 {lider} vence em {prob[lider]:.1f}% dos universos de preferência.")
    if prob[lider] >= 90:
        print("   Veredito ROBUSTO: a escolha não depende da calibração fina dos pesos.")
    elif prob[lider] >= 60:
        vice = ordem[1]
        print(f"   Veredito PROVÁVEL, mas {vice} vence em {prob[vice]:.1f}% — vale olhar os dois.")
    else:
        print("   ⚠️  Veredito FRÁGIL: o 1º lugar é um artefato dos pesos. "
              "Não decida só com o ranking — traga o decisor para calibrar os critérios.")

    # Concordância entre métodos sobre o líder.
    print("\nProbabilidade de cada método eleger o líder do consenso:")
    j = projetos.index(lider)
    for m in METODOS:
        print(f"  {m:15} {float((posicoes[m][:, j] == 1).mean()*100):5.1f}%")
    conn.close()


if __name__ == "__main__":
    main()
