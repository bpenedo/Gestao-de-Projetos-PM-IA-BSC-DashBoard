"""
Executa as queries do BSC contra o SQLite e imprime os KPIs no terminal.
Serve para VALIDAR o pipeline sem depender do Evidence.

Uso:  python3 compute_kpis.py
"""
from db import get_conn
from config import QUERIES_DIR


def rodar_query(nome):
    sql = (QUERIES_DIR / nome).read_text(encoding="utf-8")
    conn = get_conn()
    try:
        rows = conn.execute(sql).fetchall()
    finally:
        conn.close()
    return rows


def imprimir_kpis():
    rows = rodar_query("kpis_bsc_ia.sql")
    print("\n" + "=" * 78)
    print("📊  KPIs BSC POR PROJETO  —  Framework PM IA (Bruno Teixeira Penedo)")
    print("=" * 78)
    for r in rows:
        print(f"\n🎯 {r['project_name']}")
        print(f"   Sessoes: {r['total_sessoes']}  | Prompts: {r['total_prompts']}  | Tokens: {r['total_tokens']:,}")
        print(f"   PSR (Score 0-5) ........ {r['kpi_psr']}  {'⭐' * int(round(r['kpi_psr'] or 0))}")
        print(f"   PEUC (entrega util %) .. {r['kpi_peuc']}%")
        print(f"   IITA (alucinacao %) .... {r['kpi_iita']}%")
        print(f"   IDLS (waste Lean %) .... {r['kpi_idls_lean']}%")
        print(f"   IOLI (ociosidade %) .... {r['kpi_ioli']}%")
        print(f"   ITR (tokens/req) ....... {r['kpi_itr']}")
        print(f"   IEET (HH/M-tokens) ..... {r['kpi_ieet_hh_por_mtoken']}")
        print(f"   VRT/kT (R$/1k tokens) .. R$ {r['vrt_por_ktoken']}")
        print(f"   Burn Rate IA ........... R$ {r['burn_rate_ia']}")
        print(f"   ICCA (cobertura x) ..... {r['kpi_icca']}x")
        print(f"   IBMT (burn marginal) ... {r['kpi_ibmt']}")
        print(f"   CPP (R$/% progresso) ... R$ {r['kpi_cpp']}  | Progresso: {r['progresso_pct']}%")


def imprimir_pareto():
    rows = rodar_query("dominancia_erros.sql")
    print("\n" + "=" * 78)
    print("📉  PARETO — DOMINANCIA DE FALHAS POR PROJETO")
    print("=" * 78)
    atual = None
    for r in rows:
        if r["project_name"] != atual:
            atual = r["project_name"]
            print(f"\n🎯 {atual}")
        print(f"   {r['categoria_falha']:<28} {r['quantidade']:>4}  ({r['percentual_dominancia']}%)")


if __name__ == "__main__":
    imprimir_kpis()
    imprimir_pareto()
    print("\n✅ Validacao concluida.\n")
