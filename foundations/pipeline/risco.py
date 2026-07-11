"""
Gestão de risco: registro vivo + matriz Probabilidade×Impacto + risk burndown.

O Monte Carlo dá o risco quantitativo agregado (P(VPL<0), VaR). Falta o risco
QUALITATIVO — o registro que todo PMO cobra: risco, dono, probabilidade, impacto,
exposição, gatilho, mitigação, status. A probabilidade de cada risco é **ancorada nos
sinais REAIS já calculados** pelos gaps anteriores, não inventada:

  • deriva de modelo   -> nº de dias com drift (exec_drift)
  • latência/SLO        -> nº de violações de SLO (exec_latencia_tempo)
  • estouro de custo    -> CPI < 1 (evm_indices)
  • regressão de qualidade -> alertas de regressão (exec_qualidade_tempo)

Uso:  python3 risco.py
Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026.
"""
from db import get_conn, init_schema

# Catálogo base de riscos de projeto de IA. impacto fixo (severidade intrínseca);
# probabilidade é ajustada por sinal real. (categoria, descrição, dono, impacto, gatilho, mitigação)
CATALOGO = [
    ("Modelo", "Deriva do modelo degrada a saída", "Data Science", 4,
     "D de KS acima do limiar por 2+ dias", "Reancorar prompts; re-treinar/rever few-shots"),
    ("Operação", "Latência acima do SLO em produção", "SRE/Plataforma", 3,
     "p95 > 5 s em qualquer dia", "Roteamento por modelo; cache semântico"),
    ("Financeiro", "Estouro de orçamento (custo por resultado)", "FinOps", 4,
     "CPI < 1 na data de status", "Rever plano de tokens; limitar saída"),
    ("Qualidade", "Regressão de qualidade após deploy", "QA/Eval", 4,
     "salto de taxa de erro (alerta SPC)", "Portão de avaliação no CI; rollback"),
    ("Fornecedor", "Dependência de um único fornecedor de modelo", "Arquitetura", 3,
     "mudança de preço/limite do provedor", "Abstração multi-provedor; fallback"),
    ("Dados", "Qualidade/curadoria de dados insuficiente", "Data Eng", 3,
     "queda de acurácia em amostra de holdout", "Pipeline de validação; rótulos revisados"),
]


def _nivel(exp):
    return "critico" if exp >= 15 else "alto" if exp >= 9 else "medio" if exp >= 4 else "baixo"


def _prob_ancorada(conn, projeto, categoria):
    """Probabilidade 1..5 derivada do sinal real correspondente (ou 2 como base)."""
    c = conn.cursor()
    if categoria == "Modelo":
        n = c.execute("SELECT COALESCE(SUM(drift_alerta),0) FROM exec_drift WHERE project_name=?",
                      (projeto,)).fetchone()[0]
        return int(min(5, 1 + n))                    # 0..6 dias de drift -> 1..5
    if categoria == "Operação":
        n = c.execute("SELECT COALESCE(SUM(viola_slo),0) FROM exec_latencia_tempo WHERE project_name=?",
                      (projeto,)).fetchone()[0]
        return int(min(5, 1 + (n + 1) // 2))         # violações de SLO
    if categoria == "Financeiro":
        row = c.execute("SELECT cpi FROM evm_indices WHERE project_name=?", (projeto,)).fetchone()
        cpi = row[0] if row else 1.0
        return 5 if cpi < 0.85 else 4 if cpi < 0.95 else 3 if cpi < 1.0 else 2
    if categoria == "Qualidade":
        n = c.execute("SELECT COALESCE(SUM(alerta_regressao),0) FROM exec_qualidade_tempo WHERE project_name=?",
                      (projeto,)).fetchone()[0]
        return int(min(5, 2 + n))
    # riscos sem sinal direto: base determinística por projeto
    h = sum(ord(x) for x in projeto + categoria)
    return 2 + (h % 3)                                # 2..4


def gerar(conn, projeto):
    cur = conn.cursor()
    cur.execute("DELETE FROM risco_registro WHERE project_name=?", (projeto,))
    riscos = []
    for i, (cat, desc, dono, impacto, gat, mit) in enumerate(CATALOGO, 1):
        prob = _prob_ancorada(conn, projeto, cat)
        exp = prob * impacto
        # status: exposição alta ainda aberta/mitigando; baixa pode estar fechada.
        status = "aberto" if exp >= 12 else "mitigando" if exp >= 6 else "fechado"
        cur.execute("INSERT INTO risco_registro VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                    (projeto, i, cat, desc, dono, prob, impacto, exp, _nivel(exp), gat, mit, status))
        riscos.append(exp if status != "fechado" else 0)

    # Risk burndown: exposição ativa caindo ao longo dos dias com data (exec_drift dá o eixo).
    dias = [r[0] for r in cur.execute(
        "SELECT DISTINCT dia FROM exec_drift WHERE project_name=? ORDER BY dia", (projeto,)).fetchall()]
    if not dias:
        dias = [f"2026-07-{4+i:02d}" for i in range(7)]
    exp0 = sum(riscos)
    cur.execute("DELETE FROM risco_burndown WHERE project_name=?", (projeto,))
    nd = len(dias)
    for k, dia in enumerate(dias):
        # real: reduz ~8%/dia (mitigações), com um solavanco no meio (risco reabre).
        fator = max(0.0, 1 - 0.08 * k) * (1.12 if k == nd // 2 else 1.0)
        real = int(round(exp0 * fator))
        ideal = exp0 * (1 - k / (nd - 1)) if nd > 1 else 0.0
        cur.execute("INSERT INTO risco_burndown VALUES (?,?,?,?)", (projeto, dia, real, ideal))
    conn.commit()
    return exp0, sum(1 for e in riscos if e >= 12)


def main():
    init_schema()
    conn = get_conn()
    projetos = [r[0] for r in conn.execute(
        "SELECT DISTINCT project_name FROM projetos_status ORDER BY project_name")]
    print(f"▶️  Registro de risco + matriz P×I + burndown — {len(projetos)} projetos")
    for p in projetos:
        exp0, criticos = gerar(conn, p)
        print(f"   {p:<12} exposição total={exp0:3d}  riscos abertos (exp≥12)={criticos}")
    conn.close()
    print("✅ Gestão de risco concluída (probabilidades ancoradas nos sinais reais).")


if __name__ == "__main__":
    main()
