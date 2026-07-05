"""
Carrega o FLUXO DE CAIXA do portfólio (CSV/planilha fornecida pelo usuário) e calcula:
- VPL (Valor Presente Líquido)
- Payback Simples (por variação temporal — interpolado)
- Payback Descontado (interpolado)
- Fluxo período a período com acumulados (para o gráfico no dashboard)

Formato do CSV (ver fluxo_caixa_template.csv): colunas
    project_name, periodo, fluxo, taxa
onde periodo 0 = investimento inicial (fluxo negativo) e taxa = desconto por período (0.10 = 10%).

Uso:
    python3 carregar_fluxo.py caminho/do/arquivo.csv     # carrega o SEU CSV
    python3 carregar_fluxo.py --demo                      # gera fluxo de DEMO (Project A..J)
Sem argumento, tenta 'fluxo_caixa.csv' no diretório; se não houver, usa --demo.
Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
"""
import csv
import sys
from pathlib import Path

from db import get_conn, init_schema
from config import PIPELINE_DIR, SELIC_ANUAL, US_RATE_ANUAL, USD_BRL


def _vpl(fluxos, taxa):
    return sum(f / ((1 + taxa) ** t) for t, f in enumerate(fluxos))


def _tir(fluxos):
    """TIR por bisseção (raiz de VPL=0). Retorna None se não convergir no intervalo."""
    lo, hi = -0.95, 10.0
    flo, fhi = _vpl(fluxos, lo), _vpl(fluxos, hi)
    if flo * fhi > 0:
        return None
    for _ in range(200):
        mid = (lo + hi) / 2
        fm = _vpl(fluxos, mid)
        if abs(fm) < 1e-7:
            return mid
        if flo * fm < 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2


def _payback_desc(fluxos, taxa):
    """Payback descontado interpolado (períodos). None se nunca recupera."""
    cum = 0.0
    for t, f in enumerate(fluxos):
        fd = f / ((1 + taxa) ** t)
        novo = cum + fd
        if novo >= 0 and t > 0:
            return (t - 1) + (abs(cum) / fd if fd else 0)
        cum = novo
    return None


def _ler_csv(caminho):
    linhas = []
    with open(caminho, newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            linhas.append((str(row["project_name"]).strip(), int(row["periodo"]),
                           float(row["fluxo"]), float(row["taxa"])))
    return linhas


def _demo():
    """Fluxo fictício para Project A..J (determinístico)."""
    out = []
    for i in range(10):
        proj = f"Project {chr(65 + i)}"
        taxa = 0.10
        inv = -(8000 + i * 1500)
        out.append((proj, 0, float(inv), taxa))
        base = 2500 + i * 400
        for t in range(1, 6):
            out.append((proj, t, float(base + t * 600), taxa))
    return out


def _tirm(fluxos, taxa):
    """TIRM (TIR Modificada / MIRR): FV das entradas reinvestidas ÷ PV das saídas, à taxa do projeto."""
    n = len(fluxos) - 1
    if n <= 0:
        return None
    fv_pos = sum(f * (1 + taxa) ** (n - t) for t, f in enumerate(fluxos) if f > 0)
    pv_neg = -sum(f / (1 + taxa) ** t for t, f in enumerate(fluxos) if f < 0)
    if pv_neg <= 0 or fv_pos <= 0:
        return None
    return (fv_pos / pv_neg) ** (1.0 / n) - 1


def _vul(vpl, taxa, n):
    """VUL (Valor Uniforme Líquido / anuidade equivalente): VPL convertido em série uniforme por período."""
    if n <= 0:
        return None
    if taxa == 0:
        return vpl / n
    crf = taxa / (1 - (1 + taxa) ** (-n))   # fator de recuperação de capital
    return vpl * crf


def _calcular(conn):
    cur = conn.cursor()
    for col in ("tirm", "vul"):              # migração idempotente (bancos existentes)
        try:
            cur.execute(f"ALTER TABLE vpl_resultado ADD COLUMN {col} REAL")
        except Exception:
            pass
    cur.execute("DELETE FROM vpl_resultado")
    cur.execute("DELETE FROM vpl_fluxo")
    projetos = [r[0] for r in cur.execute(
        "SELECT DISTINCT project_name FROM fluxo_caixa ORDER BY project_name")]
    for proj in projetos:
        rows = cur.execute(
            "SELECT periodo, fluxo, taxa FROM fluxo_caixa WHERE project_name=? ORDER BY periodo",
            (proj,)).fetchall()
        taxa = rows[0]["taxa"]
        cum_s = cum_d = 0.0
        pb_s = pb_d = None
        prev_cum_s = prev_cum_d = 0.0
        for periodo, fluxo, _t in [(r["periodo"], r["fluxo"], r["taxa"]) for r in rows]:
            fdesc = fluxo / ((1 + taxa) ** periodo)
            novo_s = cum_s + fluxo
            novo_d = cum_d + fdesc
            # payback simples (interpolação temporal no cruzamento de zero)
            if pb_s is None and novo_s >= 0 and periodo > 0:
                pb_s = (periodo - 1) + (abs(cum_s) / fluxo if fluxo else 0)
            if pb_d is None and novo_d >= 0 and periodo > 0:
                pb_d = (periodo - 1) + (abs(cum_d) / fdesc if fdesc else 0)
            cum_s, cum_d = novo_s, novo_d
            cur.execute("""INSERT OR REPLACE INTO vpl_fluxo
                (project_name, periodo, fluxo, fluxo_desc, cum_simples, cum_desc)
                VALUES (?,?,?,?,?,?)""",
                (proj, periodo, round(fluxo, 2), round(fdesc, 2), round(cum_s, 2), round(cum_d, 2)))
        # --- TIR, ILL e dolarização ---
        fluxos = [r["fluxo"] for r in rows]
        invest = abs(fluxos[0]) if fluxos and fluxos[0] < 0 else 0.0
        vp_entradas = sum(f / ((1 + taxa) ** t) for t, f in enumerate(fluxos) if t > 0 and f > 0)
        ill = (vp_entradas / invest) if invest else None          # Índice de Lucratividade Líquida (PI)
        tir = _tir(fluxos)                                          # TIR por período
        tirm = _tirm(fluxos, taxa)                                  # TIRM (TIR Modificada / MIRR)
        vul = _vul(cum_d, taxa, len(fluxos) - 1)                    # VUL (anuidade equivalente do VPL)
        fluxos_usd = [f / USD_BRL for f in fluxos]                  # dolarização
        vpl_usd = _vpl(fluxos_usd, US_RATE_ANUAL)                   # descontado à taxa dos EUA
        pb_usd = _payback_desc(fluxos_usd, US_RATE_ANUAL)
        cur.execute("""INSERT OR REPLACE INTO vpl_resultado
            (project_name, taxa, vpl, payback_simples, payback_descontado,
             tir, ill, vpl_usd, payback_desc_usd, selic, us_rate, usd_brl, supera_selic, supera_us,
             tirm, vul)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (proj, taxa, round(cum_d, 2),
             round(pb_s, 2) if pb_s is not None else None,
             round(pb_d, 2) if pb_d is not None else None,
             round(tir, 4) if tir is not None else None,
             round(ill, 3) if ill is not None else None,
             round(vpl_usd, 2), round(pb_usd, 2) if pb_usd is not None else None,
             SELIC_ANUAL, US_RATE_ANUAL, USD_BRL,
             1 if (tir is not None and tir > SELIC_ANUAL) else 0,
             1 if (tir is not None and tir > US_RATE_ANUAL) else 0,
             round(tirm, 4) if tirm is not None else None,
             round(vul, 2) if vul is not None else None))
    conn.commit()
    return projetos


def main():
    init_schema()
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    if arg == "--demo":
        dados = _demo()
        origem = "DEMO (Project A..J)"
    else:
        caminho = arg or (PIPELINE_DIR / "fluxo_caixa.csv")
        if Path(caminho).exists():
            dados = _ler_csv(caminho)
            origem = str(caminho)
        else:
            dados = _demo()
            origem = "DEMO (nenhum CSV encontrado)"

    conn = get_conn()
    conn.execute("DELETE FROM fluxo_caixa")
    conn.executemany(
        "INSERT OR REPLACE INTO fluxo_caixa (project_name, periodo, fluxo, taxa) VALUES (?,?,?,?)",
        dados)
    conn.commit()
    projetos = _calcular(conn)
    conn.close()
    print(f"✅ Fluxo carregado de: {origem} | {len(projetos)} projetos | VPL/Payback calculados.")


if __name__ == "__main__":
    main()
