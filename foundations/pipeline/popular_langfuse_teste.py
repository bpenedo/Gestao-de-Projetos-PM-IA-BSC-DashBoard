"""
Envia TRACES DE TESTE para o SEU Langfuse Cloud (SDK v4), para validar o pipeline real
ponta a ponta quando ainda não há aplicações instrumentadas.

⚠️ Este script ESCREVE na sua conta Langfuse (cria observations de teste). Use só com as suas chaves.
Depois rode `./run_all.sh` → o ETL puxa esses dados de volta → dashboard com dados reais.

Uso:  python3 popular_langfuse_teste.py [N_por_projeto]   (default 60)
Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
"""
import random
import sys
import uuid

from config import LANGFUSE_PUBLIC_KEY, LANGFUSE_SECRET_KEY, LANGFUSE_HOST

PROJETOS = ["Demo-Backtest", "Demo-RPA-n8n", "Demo-Extensao-Chrome"]
# (prompt, resposta) variando para exercitar a classificação (NENHUM/RATE_LIMIT/ALUCINACAO)
AMOSTRAS = [
    ("gere um codigo python para somar", "def soma(a,b): return a+b  # ok"),
    ("extrair json da tabela de precos", '{"preco": 10.5}'),
    ("resuma este relatorio", "Resumo: resultados positivos no trimestre."),
    ("corrija o erro do script", "Traceback (most recent call last): SyntaxError:"),
    ("rode o backtest", "rate limit exceeded, error 429"),
    ("analise por que a estrategia falhou", "A estrategia falhou por overfitting nos dados."),
    ("converse comigo sobre o mercado", "..."),
]


def _valida():
    if not (LANGFUSE_PUBLIC_KEY and LANGFUSE_SECRET_KEY) \
            or "PLACEHOLDER" in LANGFUSE_PUBLIC_KEY or "SUA_" in LANGFUSE_PUBLIC_KEY \
            or "PLACEHOLDER" in LANGFUSE_SECRET_KEY or "SUA_" in LANGFUSE_SECRET_KEY:
        print("⚠️  .env ainda com placeholders. Cole as SUAS chaves reais antes de rodar.")
        return False
    return True


def main(n=60):
    if not _valida():
        return
    from langfuse import Langfuse
    client = Langfuse(public_key=LANGFUSE_PUBLIC_KEY, secret_key=LANGFUSE_SECRET_KEY,
                      host=LANGFUSE_HOST)
    # Teste de auth
    try:
        client.api.observations.get_many(type="GENERATION", limit=1)
    except Exception as e:
        if "401" in str(e) or "Unauthorized" in type(e).__name__:
            print("⚠️  401 — credenciais inválidas. Confira pk-lf-/sk-lf-/HOST no .env.")
        else:
            print(f"⚠️  Falha de conexão: {type(e).__name__}: {str(e)[:200]}")
        return

    total = 0
    for proj in PROJETOS:
        for _ in range(n):
            prompt, resp = random.choice(AMOSTRAS)
            pt, ct = random.randint(400, 8000), random.randint(100, 3000)
            sess = f"{proj}-sess-{random.randint(1, n // 4 + 1)}"
            with client.start_as_current_observation(
                    name=proj, as_type="generation",
                    input=prompt, output=resp, model="gpt-4o-mini",
                    usage_details={"input": pt, "output": ct},
                    metadata={"project_name": proj, "session": sess}) as gen:
                try:
                    client.update_current_trace(session_id=sess, name=proj)
                except Exception:
                    pass
            total += 1
    client.flush()
    print(f"✅ Enviados {total} traces de teste para {LANGFUSE_HOST} "
          f"({len(PROJETOS)} projetos). Agora rode: ./run_all.sh")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 60)
