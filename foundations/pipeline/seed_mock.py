"""
Gerador de DADOS MOCK para validar o pipeline e os dashboards do Evidence
ANTES de plugar o Langfuse real. Popula todas as tabelas com 3 projetos
representativos do ecossistema (Backtest, Automações RPA/n8n, Extensões/PWAs),
cada um com um perfil de falha característico (Pareto).

Uso:  python3 seed_mock.py
"""
import random
import uuid
from datetime import datetime, timedelta, timezone

from db import get_conn, init_schema

random.seed(42)  # reprodutível

# Perfil de cada projeto: (peso_rate_limit, peso_alucinacao, faixa_tokens, faixa_latencia)
PERFIS = {
    "Ferramentas de Backtest": dict(p_rate=0.04, p_aluc=0.10, tok=(8000, 22000), lat=(2.0, 7.5)),
    "Automacoes RPA n8n":      dict(p_rate=0.22, p_aluc=0.08, tok=(800, 4000),   lat=(0.4, 2.5)),
    "Extensoes Chrome PWAs":   dict(p_rate=0.03, p_aluc=0.28, tok=(500, 3500),   lat=(0.3, 3.2)),
}

# Custos fixos de infraestrutura (base de rateio).
INFRA = [
    ("n8n Cloud", 250.00),
    ("Temporal Cloud", 400.00),
    ("Servidor Banco de Dados", 350.00),
    ("Licencas Dev / IDE", 300.00),
    ("Langfuse (observabilidade)", 200.00),
]

# Esforço humano + MRR incremental por projeto.
HORAS = {
    "Ferramentas de Backtest": dict(horas=40, custo_hora=50, mrr_inc=3500),
    "Automacoes RPA n8n":      dict(horas=32, custo_hora=55, mrr_inc=2200),
    "Extensoes Chrome PWAs":   dict(horas=48, custo_hora=45, mrr_inc=9000),
}

# Status de progresso/interrupções por projeto (para CPP e PSR).
STATUS = {
    "Ferramentas de Backtest": dict(d_real=12, d_plan=12, acum=60, tco=2700, interr=6,  teto=20),
    "Automacoes RPA n8n":      dict(d_real=8,  d_plan=12, acum=45, tco=1800, interr=18, teto=20),
    "Extensoes Chrome PWAs":   dict(d_real=15, d_plan=12, acum=72, tco=3100, interr=9,  teto=20),
}

LOGS_POR_PROJETO = 300

# Taxonomia de prompt + propensão à alucinação (código/raciocínio alucinam mais).
CATS = {"Geracao de Codigo": 1.9, "Raciocinio/Analise": 1.6, "Conversa/Aberto": 1.4,
        "Extracao de Dados": 1.0, "RAG/Busca": 0.9, "Transformacao/Formato": 0.7, "Sumarizacao": 0.5}


def gerar_logs(cursor):
    agora = datetime.now(timezone.utc)
    total = 0
    for projeto, perfil in PERFIS.items():
        n_sessoes = LOGS_POR_PROJETO // 4
        for _ in range(LOGS_POR_PROJETO):
            cat = random.choice(list(CATS))
            p_h = min(0.6, perfil["p_aluc"] * CATS[cat])
            r = random.random()
            if r < p_h:
                tipo_erro, bloqueado = "ALUCINACAO_CODIGO", 0.0
            elif r < p_h + perfil["p_rate"]:
                tipo_erro, bloqueado = "RATE_LIMIT", 5.0
            else:
                tipo_erro, bloqueado = "NENHUM", 0.0

            prompt_tokens = random.randint(*perfil["tok"])
            completion_tokens = random.randint(int(perfil["tok"][0] * 0.2), int(perfil["tok"][1] * 0.5))
            latency = round(random.uniform(*perfil["lat"]), 2)
            ts = (agora - timedelta(minutes=random.randint(0, 60 * 24 * 6))).isoformat()
            session_id = f"{projeto[:4].lower()}-sess-{random.randint(1, n_sessoes)}"
            gid = str(uuid.uuid4())

            cursor.execute("""
                INSERT OR REPLACE INTO logs_langfuse
                (id, project_name, session_id, prompt_tokens, completion_tokens,
                 tipo_erro, prompt_categoria, tempo_bloqueado_minutos, latency_seconds, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (gid, projeto, session_id, prompt_tokens, completion_tokens,
                  tipo_erro, cat, bloqueado, latency, ts))

            if tipo_erro != "NENHUM":
                cursor.execute("""
                    INSERT OR REPLACE INTO alertas_criticos
                    (id, project_name, session_id, tipo_erro, prompt_truncado,
                     resposta_truncada, tokens_desperdicados, data_evento)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (gid, projeto, session_id, tipo_erro,
                      f"[mock] prompt do usuario ({tipo_erro})"[:150],
                      f"[mock] resposta com falha {tipo_erro}"[:150],
                      prompt_tokens + completion_tokens, ts))
            total += 1
    return total


def gerar_dimensoes(cursor):
    for item, valor in INFRA:
        cursor.execute("INSERT OR REPLACE INTO assinaturas_infra VALUES (?, ?)", (item, valor))

    for projeto, h in HORAS.items():
        custo_total = h["horas"] * h["custo_hora"]
        cursor.execute("""
            INSERT OR REPLACE INTO horas_desenvolvimento
            (project_name, horas_trabalhadas, custo_hora_dev, custo_total_desenvolvimento,
             faturamento_mrr_incremental, cac_planejado, payback_meses)
            VALUES (?, ?, ?, ?, ?, NULL, NULL)
        """, (projeto, h["horas"], h["custo_hora"], custo_total, h["mrr_inc"]))

    for projeto, s in STATUS.items():
        cursor.execute("""
            INSERT OR REPLACE INTO projetos_status
            (project_name, progresso_pct_delta_real, progresso_pct_delta_plan,
             progresso_pct_acumulado, tco_ia_acumulado, interrupcoes_periodo, interrupcoes_teto)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (projeto, s["d_real"], s["d_plan"], s["acum"], s["tco"], s["interr"], s["teto"]))


def gerar_reuniao(cursor):
    # Próxima sexta-feira a partir de hoje.
    hoje = datetime.now()
    dias_ate_sexta = (4 - hoje.weekday()) % 7
    sexta = (hoje + timedelta(days=dias_ate_sexta)).strftime("%Y-%m-%d")
    linhas = [
        (sexta, "Ferramentas de Backtest",
         "Processamento intensivo de dados historicos via Temporal.",
         "Custo ponderado estabilizou; cache reduziu requisicoes redundantes.",
         "Banco proprietario de estrategias geradas (subproduto de dados).",
         "Execucao assincrona preditiva: IA antecipa o proximo passo do backtest.",
         "Implementar RAG/embeddings para reduzir prompt inflado (Alto Custo)."),
        (sexta, "Automacoes RPA n8n",
         "Monitoramento de scrapers e esteiras de alta frequencia.",
         "14% das execucoes batem Rate Limit na madrugada; avaliar upgrade de Tier.",
         "Conectores universais gerados por IA (-80% no setup de clientes).",
         "Auto-healing de workflows: IA reescreve seletor de scraper em runtime.",
         "Fila com backoff espacado no Temporal para zerar erros 429."),
        (sexta, "Extensoes Chrome PWAs",
         "Contato direto com usuario final via assinatura SaaS.",
         "IITA acima da meta em jogos mobile; usuarios cancelando iteracoes.",
         "Dados comportamentais de prompts de usabilidade.",
         "UI dinamica hiper-personalizada por recorrencia de prompts.",
         "System prompt rigido com saida JSON para reduzir alucinacao (peso 2.0)."),
    ]
    for ln in linhas:
        cursor.execute("""
            INSERT OR REPLACE INTO reuniao_weekly
            (data_reuniao, project_name, sumario_executivo, insights_clevel,
             mapeamento_tesouro, joia_da_coroa, acoes_corretivas_lean)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, ln)
    return sexta


def main():
    init_schema()
    conn = get_conn()
    cur = conn.cursor()
    # Limpa para um seed determinístico.
    for tbl in ["logs_langfuse", "alertas_criticos", "assinaturas_infra",
                "horas_desenvolvimento", "projetos_status", "reuniao_weekly"]:
        cur.execute(f"DELETE FROM {tbl}")
    n = gerar_logs(cur)
    gerar_dimensoes(cur)
    sexta = gerar_reuniao(cur)
    conn.commit()
    conn.close()
    print(f"✅ Mock gerado: {n} logs, {len(PERFIS)} projetos. Reuniao weekly em {sexta}.")


if __name__ == "__main__":
    main()
