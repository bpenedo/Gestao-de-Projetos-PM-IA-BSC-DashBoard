"""
DEMO ANONIMIZADA para o pacote público: gera projetos fictícios "Project A", "Project B", ...
com todas as features (KPIs, wastes, RCA de alucinação, snapshots), SEM qualquer dado pessoal.

Reutiliza a lógica determinística de seed_from_folders (perfil/gerar), apenas trocando os nomes.
Use ESTE seed (e não seed_from_folders.py) ao publicar — ver github_load.md.

Uso:  python3 seed_demo.py [N]   (N = nº de projetos, default 10 -> Project A..J)
Framework "Gestão de Projetos (PM) IA com Painel BSC e DashBoard" · (c) Bruno Teixeira Penedo — 2026. Todos os direitos reservados. E-mail: bpenedo@gmail.com
"""
import sys
from datetime import datetime, timedelta

import seed_from_folders as sf
from db import get_conn, init_schema

TABELAS = ["logs_langfuse", "alertas_criticos", "assinaturas_infra",
           "horas_desenvolvimento", "projetos_status", "kpi_snapshots", "reuniao_weekly"]


def nomes(n):
    return [f"Project {chr(65 + i)}" for i in range(n)]  # A, B, C, ...


def main(n=10):
    init_schema()
    projetos = nomes(n)
    conn = get_conn()
    cur = conn.cursor()
    for t in TABELAS:
        cur.execute(f"DELETE FROM {t}")
    for item, valor in sf.INFRA:
        cur.execute("INSERT OR REPLACE INTO assinaturas_infra VALUES (?,?)", (item, valor))
    for proj in projetos:
        sf.gerar(cur, proj, sf.perfil(proj))
    # Pauta semanal mínima (evita tabela vazia no Evidence).
    hoje = datetime.now()
    sexta = (hoje + timedelta(days=(4 - hoje.weekday()) % 7)).strftime("%Y-%m-%d")
    for proj in projetos[:3]:
        cur.execute("""INSERT OR REPLACE INTO reuniao_weekly
            (data_reuniao, project_name, sumario_executivo, insights_clevel,
             mapeamento_tesouro, joia_da_coroa, acoes_corretivas_lean)
            VALUES (?,?,?,?,?,?,?)""",
            (sexta, proj, "Demo — status executivo.", "Demo — insight C-Level.",
             "Demo — ativo de dados.", "Demo — salto quantico.",
             "Reduzir alucinacao em prompts abertos (RCA)."))
    conn.commit()
    conn.close()
    print(f"✅ DEMO ANÔNIMA gerada: {', '.join(projetos)}")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 10)
