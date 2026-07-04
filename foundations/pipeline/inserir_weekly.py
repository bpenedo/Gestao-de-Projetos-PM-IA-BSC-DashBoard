"""
Cadastro interativo da pauta da reunião semanal (Weekly Checkpoint - sexta 09:00).
Grava em reuniao_weekly (SQLite) e gera um Markdown padronizado em weekly_reports/.
Opcionalmente faz git add/commit/push do relatório (DataOps).

Uso:  python3 inserir_weekly.py
Framework "Gestão de Projetos (PM) IA com Painel BSC e DashBoard" · (c) Bruno Teixeira Penedo — 2026. Todos os direitos reservados. E-mail: bpenedo@gmail.com
"""
import os
import subprocess
from datetime import datetime

from db import get_conn, init_schema
from config import PIPELINE_DIR

OUTPUT_DIR = PIPELINE_DIR / "weekly_reports"


def _slug(nome):
    return "".join(c for c in nome if c.isalnum() or c == " ").strip().replace(" ", "_").lower()


def git_deploy(caminho, projeto):
    try:
        subprocess.run(["git", "add", str(caminho)], check=True, capture_output=True)
        msg = f"docs(weekly): status {projeto} - {datetime.now():%d/%m/%Y}"
        subprocess.run(["git", "commit", "-m", msg], check=True, capture_output=True)
        subprocess.run(["git", "push"], check=True, capture_output=True)
        print("✅ Git deploy concluído.")
    except subprocess.CalledProcessError as e:
        err = e.stderr.decode() if e.stderr else str(e)
        print(f"⚠️  Git deploy não realizado: {err.strip()}")


def main():
    init_schema()
    OUTPUT_DIR.mkdir(exist_ok=True)
    print("=" * 60)
    print("📝 CENTRAL WEEKLY C-LEVEL — ECOSSISTEMA IA (© Bruno Teixeira Penedo 2026)")
    print("=" * 60)

    projeto = input("📌 Nome do Projeto: ").strip()
    data_in = input("📅 Data da reunião (DD/MM/AAAA, vazio = hoje): ").strip()
    dt = datetime.strptime(data_in, "%d/%m/%Y") if data_in else datetime.now()
    data_sql = dt.strftime("%Y-%m-%d")

    sumario = input("📊 Sumário Executivo:\n  > ")
    insights = input("💡 Insights C-Level:\n  > ")
    tesouro = input("🪙 Mapeamento do Tesouro:\n  > ")
    joia = input("👑 A JÓIA DA COROA (Salto Quântico):\n  > ")
    print("\n⏱️  Projetos com latência média > 3s exigem contramedidas Lean.")
    acoes = input("🛠️  Ações Corretivas Lean (PDCA/Kaizen):\n  > ")

    conn = get_conn()
    conn.execute("""
        INSERT OR REPLACE INTO reuniao_weekly
        (data_reuniao, project_name, sumario_executivo, insights_clevel,
         mapeamento_tesouro, joia_da_coroa, acoes_corretivas_lean)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (data_sql, projeto, sumario, insights, tesouro, joia, acoes))
    conn.commit()
    conn.close()
    print("✅ Gravado no SQLite.")

    arquivo = OUTPUT_DIR / f"{_slug(projeto)}_weekly_{dt:%d%m%Y}.md"
    arquivo.write_text(f"""# 📝 Relatório Semanal de Projeto IA
> **Projeto:** {projeto}
> **Data:** {dt:%d/%m/%Y} · **Classificação:** Confidencial / C-Level
> **Framework "Gestão de Projetos (PM) IA com Painel BSC e DashBoard"** · ©️ Bruno Teixeira Penedo — 2026. Todos os direitos reservados. E-mail: bpenedo@gmail.com

---
## 📊 1. Sumário Executivo
{sumario}

## 💡 2. Insights C-Level
{insights}

## 🪙 3. Mapeamento do Tesouro
{tesouro}

## 👑 4. A JÓIA DA COROA (Salto Quântico)
{joia}

## 🛠️ 5. Ações Corretivas Lean (PDCA)
> {acoes or "Nenhum gargalo crítico identificado na janela."}

---
*Gerado via Central de Governança de Projetos PM IA.*
""", encoding="utf-8")
    print(f"💾 Markdown gerado: {arquivo}")

    if input("\n🚀 Fazer git push do relatório? (s/N): ").strip().lower() == "s":
        git_deploy(arquivo, projeto)


if __name__ == "__main__":
    main()
