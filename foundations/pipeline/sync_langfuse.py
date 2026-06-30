"""
ETL CONCORRENTE Langfuse -> SQLite (assíncrono).
Como a paginação do Langfuse é por cursor (sequencial), a concorrência vem de
DIVIDIR o intervalo de tempo em N janelas e buscá-las EM PARALELO (asyncio.gather)
via o cliente async oficial (`async_api.observations.get_many`). Ganho real de I/O.

A classificação de falhas usa `analise.classificar` (acelerada por Rust se disponível).
As escritas no SQLite são feitas no fim, de forma serial (sqlite3 não é concorrente).

Sem credenciais -> avisa e sai 0. Credencial inválida (401) -> mensagem clara, sem traceback.
Autor: Bruno Teixeira Penedo.
"""
import asyncio
from datetime import datetime, timedelta, timezone

from db import get_conn, init_schema
from analise import classificar, classificar_categoria, BACKEND
from config import (LANGFUSE_PUBLIC_KEY, LANGFUSE_SECRET_KEY, LANGFUSE_HOST,
                    THRESHOLD_ALERTA_DIA)

N_JANELAS = 4  # concorrência (≈ nº de núcleos)


def _cliente():
    if not (LANGFUSE_PUBLIC_KEY and LANGFUSE_SECRET_KEY):
        print("⚠️  Credenciais Langfuse ausentes (.env). Pulei a sincronização real.")
        print("    Use 'python3 seed_mock.py' para popular dados de teste.")
        return None
    try:
        from langfuse import Langfuse
    except ImportError:
        print("⚠️  Pacote 'langfuse' não instalado. Rode: pip install -r requirements.txt")
        return None
    return Langfuse(public_key=LANGFUSE_PUBLIC_KEY, secret_key=LANGFUSE_SECRET_KEY,
                    host=LANGFUSE_HOST)


def _ultima_sincronizacao(conn):
    res = conn.execute("SELECT MAX(updated_at) FROM logs_langfuse").fetchone()
    if res and res[0]:
        return datetime.fromisoformat(res[0])
    return datetime.now(timezone.utc) - timedelta(days=30)


async def _fetch_janela(cliente, inicio, fim):
    """Pagina UMA janela de tempo sequencialmente (cursor). Retorna lista de observações."""
    out, cursor = [], None
    while True:
        pagina = await cliente.async_api.observations.get_many(
            type="GENERATION", from_start_time=inicio, to_start_time=fim,
            limit=100, cursor=cursor, fields="core,io,usage,metadata")
        if not pagina.data:
            break
        out.extend(pagina.data)
        cursor = getattr(pagina.meta, "cursor", None)
        if not cursor:
            break
    return out


async def _fetch_concorrente(cliente, data_limite, agora):
    passo = (agora - data_limite) / N_JANELAS
    janelas = [(data_limite + passo * i, data_limite + passo * (i + 1)) for i in range(N_JANELAS)]
    resultados = await asyncio.gather(
        *[_fetch_janela(cliente, s, e) for s, e in janelas], return_exceptions=True)
    obs = []
    for r in resultados:
        if isinstance(r, Exception):
            raise r
        obs.extend(r)
    return obs


def _gravar(conn, observacoes):
    cur = conn.cursor()
    total = 0
    for gen in observacoes:
        md = gen.metadata if isinstance(gen.metadata, dict) else {}
        # project_name: metadata.project_name (recomendado) > trace name > observation name.
        project_name = (md.get("project_name") or md.get("project")
                        or getattr(gen, "trace_name", None) or gen.name
                        or "Projeto_Nao_Identificado")
        session = md.get("session") or gen.session_id
        usage = gen.usage_details or {}
        pt = int(usage.get("input", 0) or 0)
        ct = int(usage.get("output", 0) or 0)
        latency = gen.latency or 0.0
        input_bruto = gen.input or ""
        output_bruto = gen.output or ""
        tipo_erro, bloqueado = classificar(str(input_bruto), str(output_bruto))
        categoria = classificar_categoria(str(input_bruto))
        ts = gen.updated_at or gen.start_time
        ts = ts.isoformat() if ts else datetime.now(timezone.utc).isoformat()
        cur.execute("""INSERT OR REPLACE INTO logs_langfuse
            (id, project_name, session_id, prompt_tokens, completion_tokens,
             tipo_erro, prompt_categoria, tempo_bloqueado_minutos, latency_seconds, updated_at)
            VALUES (?,?,?,?,?,?,?,?,?,?)""",
            (gen.id, project_name, session, pt, ct, tipo_erro, categoria, bloqueado, latency, ts))
        if tipo_erro != "NENHUM":
            cur.execute("""INSERT OR REPLACE INTO alertas_criticos
                (id, project_name, session_id, tipo_erro, prompt_truncado,
                 resposta_truncada, tokens_desperdicados, data_evento)
                VALUES (?,?,?,?,?,?,?,?)""",
                (gen.id, project_name, gen.session_id, tipo_erro,
                 str(input_bruto)[:150], str(output_bruto)[:150], pt + ct, ts))
        total += 1
    conn.commit()
    return total


def verificar_picos(conn):
    desde = (datetime.now(timezone.utc) - timedelta(days=1)).isoformat()
    rows = conn.execute("""SELECT project_name, tipo_erro, COUNT(*) AS n
        FROM alertas_criticos WHERE data_evento >= ? GROUP BY project_name, tipo_erro""",
        (desde,)).fetchall()
    criticos = [r for r in rows if r["n"] > THRESHOLD_ALERTA_DIA]
    if criticos:
        print("\n" + "=" * 60 + "\n🚨 CRON LEAN ALERT: PICOS (ÚLTIMAS 24H) 🚨\n" + "=" * 60)
        for r in criticos:
            print(f"⚠️  '{r['project_name']}' gerou {r['n']} falhas [{r['tipo_erro']}].")
        print("=" * 60 + "\n")


def extrair_e_carregar():
    init_schema()
    cliente = _cliente()
    if cliente is None:
        return
    conn = get_conn()
    data_limite = _ultima_sincronizacao(conn)
    agora = datetime.now(timezone.utc)
    print(f"🔄 Sync CONCORRENTE ({N_JANELAS} janelas, backend de análise: {BACKEND.upper()}) "
          f"desde {data_limite.isoformat()} ...")
    try:
        observacoes = asyncio.run(_fetch_concorrente(cliente, data_limite, agora))
    except Exception as e:
        nome, msg = type(e).__name__, str(e)
        if "401" in msg or "Invalid credentials" in msg or "Unauthorized" in nome:
            print("⚠️  Langfuse recusou as credenciais (HTTP 401). Verifique "
                  "LANGFUSE_PUBLIC_KEY / LANGFUSE_SECRET_KEY / LANGFUSE_HOST no .env.")
        else:
            print(f"⚠️  Falha ao consultar o Langfuse: {nome}: {msg[:200]}")
        conn.close()
        return
    total = _gravar(conn, observacoes)
    verificar_picos(conn)
    conn.close()
    print(f"✅ Sync concluído: {total} generations auditadas (concorrência {N_JANELAS}x).")


if __name__ == "__main__":
    extrair_e_carregar()
