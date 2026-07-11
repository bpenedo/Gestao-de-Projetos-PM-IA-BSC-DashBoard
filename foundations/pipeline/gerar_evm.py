"""
Curva S do Earned Value Management: PV (planejado), EV (agregado) e AC (custo real)
ao longo dos períodos, com a data de status marcada. É o gráfico canônico do EVM.

Saída: ../evidence/static/mc/<projeto>_evm.png  (dados anônimos, git-ignored).

Uso:  python3 gerar_evm.py            # todos os projetos
Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026.
"""
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from db import get_conn
from config import FOUNDATIONS_DIR

STATIC = FOUNDATIONS_DIR / "evidence" / "static" / "mc"
STATIC.mkdir(parents=True, exist_ok=True)
FUNDO_PLOT = "#D9D9D9"
AZUL, VERDE, VERMELHO = "#1F77B4", "#2CA02C", "#D62728"


def _slug(nome):
    return nome.replace(" ", "_")


def evm_curva(conn, projeto):
    rows = conn.execute(
        "SELECT periodo, pv, ev, ac FROM evm_serie WHERE project_name=? ORDER BY periodo",
        (projeto,)
    ).fetchall()
    if not rows:
        return None
    meta = conn.execute(
        "SELECT bac, at_periodo, spi, cpi, eac, sv_t FROM evm_indices WHERE project_name=?",
        (projeto,)
    ).fetchone()
    bac, at, spi, cpi, eac, sv_t = meta

    ts = [r[0] for r in rows]
    pv = [r[1] for r in rows]
    ev = [r[2] for r in rows if r[2] is not None]
    ac = [r[3] for r in rows if r[3] is not None]
    ev_t = [r[0] for r in rows if r[2] is not None]
    ac_t = [r[0] for r in rows if r[3] is not None]

    fig, ax = plt.subplots(figsize=(9.5, 4.6))
    ax.set_facecolor(FUNDO_PLOT)
    ax.plot(ts, pv, color=AZUL, lw=2.0, marker="o", ms=3, label="PV — valor planejado")
    ax.plot(ev_t, ev, color=VERDE, lw=2.0, marker="o", ms=3, label="EV — valor agregado")
    ax.plot(ac_t, ac, color=VERMELHO, lw=2.0, marker="o", ms=3, label="AC — custo real")
    ax.axhline(bac, color="#333", ls=":", lw=1.2)
    ax.text(0, bac, " BAC", va="bottom", ha="left", fontsize=8, color="#333")
    ax.axhline(eac, color="#C0392B", ls=":", lw=1.2)
    ax.text(0, eac, " EAC", va="bottom", ha="left", fontsize=8, color="#C0392B")
    ax.axvline(at, color="#555", ls="--", lw=1.4)
    ax.text(at, ax.get_ylim()[1] * 0.02, " data de status", rotation=90, fontsize=8, va="bottom")

    situacao = "ADIANTADO" if sv_t >= 0 else "ATRASADO"
    ax.set_title(f"Curva S do EVM — {projeto}   SPI={spi:.2f} · CPI={cpi:.2f} · {situacao}",
                 fontweight="bold")
    ax.set_xlabel("período (semana)", fontstyle="italic")
    ax.set_ylabel("valor acumulado (R$)", fontstyle="italic")
    ax.grid(color="white", lw=0.8); ax.set_axisbelow(True)
    ax.legend(fontsize=8, loc="upper left", framealpha=0.9)
    fig.tight_layout()
    out = STATIC / f"{_slug(projeto)}_evm.png"
    fig.savefig(out, dpi=110); plt.close(fig)
    return out


def main():
    conn = get_conn()
    alvo = sys.argv[sys.argv.index("--projeto") + 1] if "--projeto" in sys.argv else None
    projetos = [alvo] if alvo else [
        r[0] for r in conn.execute("SELECT project_name FROM evm_indices ORDER BY project_name")]
    n = sum(1 for p in projetos if evm_curva(conn, p))
    conn.close()
    print(f"✅ Curva S do EVM gerada para {n} projeto(s) em {STATIC}")


if __name__ == "__main__":
    main()
