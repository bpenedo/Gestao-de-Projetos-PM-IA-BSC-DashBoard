"""
Gera o MAPA 5D do portfólio de projetos de IA (estilo 5dchart.com — esferas 3D
glossy) usando a lib render_5d vendorizada localmente (pipeline/fivedchart_lib.py).

5 dimensões escolhidas (ortogonais, visão C-Level):
  X = Volume de tokens        -> ESCALA do trabalho de IA
  Y = PEUC %                  -> QUALIDADE / EFICÁCIA de entrega
  Z = PSR (0-5)               -> SAÚDE geral do projeto
  tamanho (dim4) = Burn Rate de IA (R$)  -> PESO FINANCEIRO (caixa em jogo)
  cor (dim5) = ICCA (RdYlGn)  -> SUSTENTABILIDADE (verde > 3x cobre custo; vermelho < 1x prejuízo)

Saída: foundations/evidence/static/5d_projetos.png  (servida pelo Evidence em /5d_projetos.png)
Autor: Bruno Teixeira Penedo.
"""
from db import get_conn
from config import QUERIES_DIR, FOUNDATIONS_DIR

# Lib 5DCHART vendorizada localmente em pipeline/ (sem dependência de projeto pessoal).
from fivedchart_lib import render_5d

OUT = FOUNDATIONS_DIR / "evidence" / "static" / "5d_projetos.png"
OUT.parent.mkdir(parents=True, exist_ok=True)


def main():
    sql = (QUERIES_DIR / "kpis_bsc_ia.sql").read_text(encoding="utf-8")
    conn = get_conn()
    rows = conn.execute(sql).fetchall()
    conn.close()
    if not rows:
        print("⚠️  Sem dados — rode seed_from_folders.py ou ./run_all.sh primeiro.")
        return

    items = []
    for r in rows:
        items.append(dict(
            x=float(r["total_tokens"] or 0),
            y=float(r["kpi_peuc"] or 0),
            z=float(r["kpi_psr"] or 0),
            s=max(float(r["burn_rate_ia"] or 0), 1.0),
            c=float(r["kpi_icca"] or 0),
            lbl=r["project_name"],
        ))

    render_5d(
        items,
        ["Volume (tokens) — escala", "PEUC % — qualidade", "PSR (0-5) — saude"],
        "Mapa 5D do Portfolio de Projetos de IA — visao C-Level",
        str(OUT),
        color_mode="value", cmap="RdYlGn",
        color_label="Dim.5 — ICCA (sustentabilidade: verde > 3x)",
        size_legend_title="Dim.4 — Burn Rate de IA (R$)",
        size_fmt=lambda v: f"R$ {v:,.0f}",
        note="X=escala(tokens)  Y=qualidade(PEUC)  Z=saude(PSR)  |  tamanho=burn rate  cor=ICCA",
    )
    print("✅ 5D gerado:", OUT, f"({len(items)} projetos)")


if __name__ == "__main__":
    main()
