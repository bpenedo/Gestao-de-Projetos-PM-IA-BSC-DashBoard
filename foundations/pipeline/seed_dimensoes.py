"""
Semeia DIMENSÕES PLACEHOLDER (progresso, horas, infra, snapshots, reunião, fluxo de caixa)
para os projetos REAIS já sincronizados em logs_langfuse — de modo que o dashboard completo
RENDERIZE. Os KPIs de TOKEN/qualidade/RCA continuam REAIS (vindos do Langfuse); apenas
progresso e financeiro são placeholders a substituir pelos seus números reais.

Remove o lote 'Projeto_Nao_Identificado' (traces enviados antes do tagueamento por metadata).

Uso:  python3 seed_dimensoes.py
Framework "Gestão de Projetos (PM) IA com Painel BSC e DashBoard" · (c) Bruno Teixeira Penedo — 2026. Todos os direitos reservados. E-mail: bpenedo@gmail.com
"""
from datetime import datetime, timedelta

from db import get_conn, init_schema
import carregar_fluxo

INFRA = [("n8n Cloud", 250.0), ("Temporal Cloud", 400.0), ("Servidor BD", 350.0),
         ("Licencas Dev", 300.0), ("Langfuse", 200.0)]


def main():
    init_schema()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM logs_langfuse WHERE project_name='Projeto_Nao_Identificado'")
    cur.execute("DELETE FROM alertas_criticos WHERE project_name='Projeto_Nao_Identificado'")
    projetos = [r[0] for r in cur.execute(
        "SELECT DISTINCT project_name FROM logs_langfuse ORDER BY 1")]
    if not projetos:
        print("⚠️  Nenhum projeto real em logs_langfuse. Rode o sync primeiro.")
        return

    # infra (rateio) — placeholder
    for item, v in INFRA:
        cur.execute("INSERT OR REPLACE INTO assinaturas_infra VALUES (?,?)", (item, v))

    hoje = datetime.now()
    sexta = (hoje + timedelta(days=(4 - hoje.weekday()) % 7)).strftime("%Y-%m-%d")
    cur.execute("DELETE FROM reuniao_weekly")
    cur.execute("DELETE FROM fluxo_caixa")

    for i, proj in enumerate(projetos):
        tok = cur.execute("SELECT COALESCE(SUM(prompt_tokens+completion_tokens),0) FROM logs_langfuse WHERE project_name=?",
                          (proj,)).fetchone()[0]
        tco = round(tok * 0.025 / 1000.0, 2) or 1.0  # custo REAL de tokens
        # progresso/horas/mrr = PLACEHOLDER (substitua pelos reais)
        cur.execute("""INSERT OR REPLACE INTO horas_desenvolvimento
            (project_name,horas_trabalhadas,custo_hora_dev,custo_total_desenvolvimento,faturamento_mrr_incremental)
            VALUES (?,?,?,?,?)""", (proj, 40, 50, 2000, 4000 + i * 1500))
        cur.execute("""INSERT OR REPLACE INTO projetos_status
            (project_name,progresso_pct_delta_real,progresso_pct_delta_plan,progresso_pct_acumulado,
             tco_ia_acumulado,interrupcoes_periodo,interrupcoes_teto)
            VALUES (?,?,?,?,?,?,?)""", (proj, 10, 12, 50 + i * 8, tco, 6 + i * 3, 20))
        for k in range(6, 0, -1):
            dia = (hoje - timedelta(weeks=k - 1)).strftime("%Y-%m-%d")
            cur.execute("""INSERT OR REPLACE INTO kpi_snapshots
                (data_snapshot,project_name,cpp,psr,burn_rate_ia,iita,peuc)
                VALUES (?,?,?,?,?,?,?)""",
                (dia, proj, round(tco / max(50 + i * 8, 1) * (1 + (k - 1) * 0.08), 2),
                 round(3.5 - (k - 1) * 0.05, 2), round(tco * (1 + (k - 1) * 0.08), 2), 20.0, 70.0))
        cur.execute("""INSERT OR REPLACE INTO reuniao_weekly
            (data_reuniao,project_name,sumario_executivo,insights_clevel,mapeamento_tesouro,joia_da_coroa,acoes_corretivas_lean)
            VALUES (?,?,?,?,?,?,?)""",
            (sexta, proj, "Dados de TOKEN reais (Langfuse).", "Progresso/financeiro: PLACEHOLDER.",
             "(preencher)", "(preencher)", "Reduzir alucinacao em prompts (RCA real)."))
        # fluxo de caixa PLACEHOLDER (investimento ~ custo real de tokens × 10)
        inv = -max(round(tco * 10), 8000)
        cur.execute("INSERT OR REPLACE INTO fluxo_caixa VALUES (?,?,?,?)", (proj, 0, float(inv), 0.10))
        for t in range(1, 6):
            cur.execute("INSERT OR REPLACE INTO fluxo_caixa VALUES (?,?,?,?)",
                        (proj, t, float(round(abs(inv) / 4 + t * 600)), 0.10))

    conn.commit()
    carregar_fluxo._calcular(conn)  # calcula VPL/TIR/ILL do fluxo placeholder
    conn.close()
    print(f"✅ Dimensões placeholder semeadas para {len(projetos)} projetos reais: {', '.join(projetos)}")
    print("   (KPIs de token/RCA = REAIS; progresso/financeiro = placeholder a substituir)")


if __name__ == "__main__":
    main()
