"""
WatchDog de sessões do Claude Code (leve).
Registra cada evento de sessão (início/fim) em projetos monitorados, sem rodar o
build pesado do Evidence (esse roda via cron / run_all.sh). Pensado para ser
chamado por um hook do Claude Code (SessionStart / Stop) configurado no settings.json.

Lê o JSON do hook em STDIN (campos como cwd, hook_event_name, session_id) e:
  1. Garante o schema do SQLite.
  2. Registra/atualiza o projeto (pela pasta cwd) na tabela projetos_status.
  3. Acrescenta uma linha no log do watchdog (foundations/watchdog.log).

Uso (manual de teste):
  echo '{"cwd":"/x/Projeto","hook_event_name":"SessionStart","session_id":"abc"}' | python3 watchdog_session.py
Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
"""
import json
import sys
from datetime import datetime
from pathlib import Path

from db import get_conn, init_schema
from config import FOUNDATIONS_DIR

LOG = FOUNDATIONS_DIR / "watchdog.log"


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        payload = {}

    cwd = payload.get("cwd") or str(Path.cwd())
    evento = payload.get("hook_event_name", "manual")
    sessao = payload.get("session_id", "")
    projeto = Path(cwd).name  # nome da pasta = tag do projeto monitorado
    agora = datetime.now().isoformat(timespec="seconds")

    # OPT-IN por projeto: só monitora se houver marcador explícito de permissão.
    #   - arquivo .bscwatch na raiz do projeto, OU
    #   - pasta foundations/ deste framework (projeto-sede).
    cwd_path = Path(cwd)
    monitorado = (cwd_path / ".bscwatch").exists() or (cwd_path / "foundations" / "KPIs.md").exists()
    if not monitorado:
        # Projeto não opt-in: encerra silenciosamente sem tocar no banco.
        return

    init_schema()
    conn = get_conn()
    # Registra o projeto se ainda não existir (não zera dados já coletados).
    conn.execute("""
        INSERT INTO projetos_status (project_name)
        VALUES (?)
        ON CONFLICT(project_name) DO NOTHING
    """, (projeto,))
    conn.commit()
    conn.close()

    with open(LOG, "a", encoding="utf-8") as f:
        f.write(f"{agora}\t{evento}\t{projeto}\t{sessao}\t{cwd}\n")

    # Saída silenciosa (hooks não devem poluir a UI); código 0 = sucesso.
    print(f"[watchdog] {evento} registrado para projeto '{projeto}'", file=sys.stderr)


if __name__ == "__main__":
    main()
