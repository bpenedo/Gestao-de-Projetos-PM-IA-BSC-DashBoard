"""
Semeia a tabela planos_assinatura (planos de IA dos concorrentes) para o dashboard,
usando câmbio (USD_BRL) e IOF (IOF_PCT) do config/.env. O custo total com IOF é
calculado na query do Evidence.  Fonte de preços: planos_assinatura_IA.md.

Uso:  python3 seed_planos.py
Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
"""
from db import get_conn, init_schema
from config import USD_BRL, IOF_PCT

# (provedor, plano, US$/mês) — planos pagos; preços aproximados (verifique).
PLANOS = [
    ("OpenAI", "ChatGPT Plus", 20), ("OpenAI", "ChatGPT Pro", 200), ("OpenAI", "ChatGPT Team", 30),
    ("Anthropic", "Claude Pro", 20), ("Anthropic", "Claude Max 5x", 100),
    ("Anthropic", "Claude Max 20x", 200), ("Anthropic", "Claude Team", 30),
    ("Google", "Google AI Pro", 20), ("Google", "Google AI Ultra", 250),
    ("Perplexity", "Pro", 20), ("Perplexity", "Max", 200),
    ("xAI", "SuperGrok", 30), ("xAI", "X Premium+", 40), ("xAI", "SuperGrok Heavy", 300),
    ("Mistral", "Le Chat Pro", 15),
    ("DeepSeek", "Chat (grátis) — API à parte", 0),
    ("Kimi (Moonshot)", "Chat (grátis) — API à parte", 0),
    ("Qwen (Alibaba)", "Chat (grátis) — API à parte", 0),
]


def main():
    init_schema()
    conn = get_conn()
    conn.execute("DELETE FROM planos_assinatura")
    conn.executemany(
        "INSERT OR REPLACE INTO planos_assinatura (provedor, plano, usd_mes, cambio, iof_pct) VALUES (?,?,?,?,?)",
        [(p, n, float(u), USD_BRL, IOF_PCT) for p, n, u in PLANOS])
    conn.commit()
    conn.close()
    print(f"✅ {len(PLANOS)} planos semeados (câmbio R$ {USD_BRL} · IOF {IOF_PCT}%).")


if __name__ == "__main__":
    main()
