"""
Individualiza o dashboard pelos PROJETOS REAIS: varre as subpastas de
~/devparetoprojects/* e registra cada uma como um projeto monitorado, gerando
dados DEMO determinísticos (por hash do nome) até o Langfuse real fornecer dados.

Também grava 6 snapshots semanais por projeto (tabela kpi_snapshots) para os
gráficos de TENDÊNCIA do CPP/PSR.

⚠️ Os números são SINTÉTICOS (demonstração). Quando o sync real do Langfuse rodar,
   logs_langfuse passa a refletir o consumo verdadeiro.

Uso:  python3 seed_from_folders.py
Autor: Bruno Teixeira Penedo.
"""
import hashlib
import random
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path

from db import get_conn, init_schema

RAIZ = Path.home() / "devparetoprojects"
LOGS_POR_PROJETO = 220

# Taxonomia de prompts + peso de PROPENSÃO À ALUCINAÇÃO (código/raciocínio alucinam mais).
CATS = {
    "Geracao de Codigo": 1.9,
    "Raciocinio/Analise": 1.6,
    "Conversa/Aberto": 1.4,
    "Extracao de Dados": 1.0,
    "RAG/Busca": 0.9,
    "Transformacao/Formato": 0.7,
    "Sumarizacao": 0.5,
}

INFRA = [
    ("n8n Cloud", 250.00), ("Temporal Cloud", 400.00),
    ("Servidor Banco de Dados", 350.00), ("Licencas Dev / IDE", 300.00),
    ("Langfuse (observabilidade)", 200.00),
]


def listar_projetos():
    if not RAIZ.exists():
        return []
    return sorted([p.name for p in RAIZ.iterdir()
                   if p.is_dir() and not p.name.startswith(".")])


def perfil(nome):
    """Perfil determinístico por nome: define probabilidade de falha e tamanho de tokens."""
    h = int(hashlib.md5(nome.encode()).hexdigest(), 16)
    rng = random.Random(h)
    p_rate = round(rng.uniform(0.02, 0.20), 3)
    p_aluc = round(rng.uniform(0.05, 0.28), 3)
    tok_lo = rng.choice([500, 800, 2000, 6000])
    tok_hi = tok_lo + rng.choice([3000, 8000, 16000])
    lat_hi = round(rng.uniform(1.5, 7.0), 1)
    mrr = rng.choice([0, 1500, 2500, 4000, 9000])
    horas = rng.randint(20, 60)
    custo_hora = rng.choice([45, 50, 55, 60])
    d_real = rng.randint(6, 16)
    d_plan = 12
    acum = rng.randint(20, 85)
    return dict(rng=rng, p_rate=p_rate, p_aluc=p_aluc, tok=(tok_lo, tok_hi),
                lat=(0.3, lat_hi), mrr=mrr, horas=horas, custo_hora=custo_hora,
                d_real=d_real, d_plan=d_plan, acum=acum)


def gerar(cur, projeto, pf):
    rng = pf["rng"]
    agora = datetime.now(timezone.utc)
    n_sessoes = LOGS_POR_PROJETO // 4
    tco = 0.0
    for _ in range(LOGS_POR_PROJETO):
        cat = rng.choice(list(CATS))            # tipo de prompt
        p_h = min(0.6, pf["p_aluc"] * CATS[cat])  # alucinação enviesada pela categoria
        r = rng.random()
        if r < p_h:
            tipo, bloq = "ALUCINACAO_CODIGO", 0.0
        elif r < p_h + pf["p_rate"]:
            tipo, bloq = "RATE_LIMIT", 5.0
        else:
            tipo, bloq = "NENHUM", 0.0
        pt = rng.randint(*pf["tok"])
        ct = rng.randint(int(pf["tok"][0] * 0.2), int(pf["tok"][1] * 0.5))
        lat = round(rng.uniform(*pf["lat"]), 2)
        ts = (agora - timedelta(minutes=rng.randint(0, 60 * 24 * 6))).isoformat()
        sess = f"{projeto[:6].lower()}-s{rng.randint(1, n_sessoes)}"
        gid = str(uuid.uuid4())
        tco += (pt + ct) * 0.025 / 1000.0
        cur.execute("""INSERT OR REPLACE INTO logs_langfuse
            (id, project_name, session_id, prompt_tokens, completion_tokens,
             tipo_erro, prompt_categoria, tempo_bloqueado_minutos, latency_seconds, updated_at)
            VALUES (?,?,?,?,?,?,?,?,?,?)""",
            (gid, projeto, sess, pt, ct, tipo, cat, bloq, lat, ts))
        if tipo != "NENHUM":
            cur.execute("""INSERT OR REPLACE INTO alertas_criticos
                (id, project_name, session_id, tipo_erro, prompt_truncado,
                 resposta_truncada, tokens_desperdicados, data_evento)
                VALUES (?,?,?,?,?,?,?,?)""",
                (gid, projeto, sess, tipo, f"[demo] prompt {tipo}"[:150],
                 f"[demo] resposta {tipo}"[:150], pt + ct, ts))

    custo_total = pf["horas"] * pf["custo_hora"]
    cur.execute("""INSERT OR REPLACE INTO horas_desenvolvimento
        (project_name, horas_trabalhadas, custo_hora_dev, custo_total_desenvolvimento,
         faturamento_mrr_incremental, cac_planejado, payback_meses)
        VALUES (?,?,?,?,?,NULL,NULL)""",
        (projeto, pf["horas"], pf["custo_hora"], custo_total, pf["mrr"]))

    tco_acum = round(tco + custo_total * 0.0, 2) or 1.0
    cur.execute("""INSERT OR REPLACE INTO projetos_status
        (project_name, progresso_pct_delta_real, progresso_pct_delta_plan,
         progresso_pct_acumulado, tco_ia_acumulado, interrupcoes_periodo, interrupcoes_teto)
        VALUES (?,?,?,?,?,?,?)""",
        (projeto, pf["d_real"], pf["d_plan"], pf["acum"], round(tco, 2),
         rng.randint(2, 22), 20))

    # 6 snapshots semanais (tendência) — CPP decrescente/ruidoso, PSR variando.
    hoje = datetime.now()
    for k in range(6, 0, -1):
        dia = (hoje - timedelta(weeks=k - 1)).strftime("%Y-%m-%d")
        fator = 1.0 + (k - 1) * rng.uniform(0.04, 0.12)   # passado mais caro
        cpp = round((round(tco, 2) / max(pf["acum"], 1)) * fator, 2)
        psr = round(max(0.5, min(5.0, rng.uniform(1.5, 4.8) - (k - 1) * 0.05)), 2)
        burn = round(tco * fator, 2)
        cur.execute("""INSERT OR REPLACE INTO kpi_snapshots
            (data_snapshot, project_name, cpp, psr, burn_rate_ia, iita, peuc)
            VALUES (?,?,?,?,?,?,?)""",
            (dia, projeto, cpp, psr, burn,
             round(pf["p_aluc"] * 100, 1), round((1 - pf["p_rate"] - pf["p_aluc"]) * 100, 1)))


def main():
    init_schema()
    projetos = listar_projetos()
    if not projetos:
        print(f"⚠️  Nenhuma subpasta encontrada em {RAIZ}")
        return
    conn = get_conn()
    cur = conn.cursor()
    for tbl in ["logs_langfuse", "alertas_criticos", "assinaturas_infra",
                "horas_desenvolvimento", "projetos_status", "kpi_snapshots"]:
        cur.execute(f"DELETE FROM {tbl}")
    for item, valor in INFRA:
        cur.execute("INSERT OR REPLACE INTO assinaturas_infra VALUES (?,?)", (item, valor))
    for proj in projetos:
        gerar(cur, proj, perfil(proj))
    # Pauta semanal mínima (evita tabela vazia que quebra o conector do Evidence).
    hoje = datetime.now()
    sexta = (hoje + timedelta(days=(4 - hoje.weekday()) % 7)).strftime("%Y-%m-%d")
    cur.execute("DELETE FROM reuniao_weekly")
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
    print(f"✅ {len(projetos)} projetos reais registrados (dados DEMO): {', '.join(projetos)}")


if __name__ == "__main__":
    main()
