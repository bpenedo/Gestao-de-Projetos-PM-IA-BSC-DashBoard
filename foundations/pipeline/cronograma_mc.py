"""
Cronograma Monte Carlo (Schedule Risk Analysis / PERT) + CPM com índice de criticidade.

Reusa o motor de Monte Carlo (monte_carlo.amostrar / histograma / percentis): em vez de
simular fluxos de caixa, simula DURAÇÕES de tarefas com estimativa de 3 pontos (Triangular
min/moda/max), propaga pelo grafo de dependências (forward pass), e devolve:

  • a distribuição da DATA DE TÉRMINO do projeto (dias);
  • P80 — a data com 80% de confiança (compromisso recomendável, PMI);
  • P(no prazo) contra a deadline baseline;
  • o ÍNDICE DE CRITICIDADE de cada tarefa: em quantos % das simulações ela caiu no
    caminho crítico (mais honesto que o CPM determinístico, que aponta um caminho só).

Se `cronograma_tarefas` estiver vazia, gera uma WBS demo determinística por projeto
(dados anônimos Project A..J), no mesmo espírito dos demais seeders do pacote.

Uso:  python3 cronograma_mc.py            # todos os projetos com tarefas
Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026.
"""
import numpy as np

from db import get_conn, init_schema
from config import MC_CRONO_ITER, MC_CRONO_CONF, MC_SEED
from monte_carlo import amostrar, histograma, MC_BINS

# --- WBS demo: 8 tarefas típicas de um projeto de IA, com dependências (FS). ---
# (id, nome, a, m, b, [predecessoras])  — durações em dias.
WBS_BASE = [
    (1, "Descoberta & escopo",        3,  5,  9,  []),
    (2, "Curadoria de dados",         4,  7, 14, [1]),
    (3, "Prompt/modelo — baseline",   3,  6, 12, [1]),
    (4, "Engenharia de features",     5,  9, 18, [2]),
    (5, "Avaliação & guardrails",     4,  6, 11, [3, 4]),
    (6, "Integração & observab.",     3,  5, 10, [4]),
    (7, "Piloto com usuários",        5,  8, 15, [5, 6]),
    (8, "Go-live & handover",         2,  4,  8, [7]),
]


def _perfil(projeto):
    """Fator determinístico por projeto: alguns projetos são mais folgados que outros."""
    h = sum(ord(c) for c in projeto)
    return 0.85 + (h % 7) * 0.06      # 0.85 .. 1.21


def seed_tarefas(cur, projeto):
    fator = _perfil(projeto)
    for tid, nome, a, m, b, preds in WBS_BASE:
        cur.execute(
            "INSERT OR REPLACE INTO cronograma_tarefas VALUES (?,?,?,?,?,?,?)",
            (projeto, tid, nome, round(a * fator, 1), round(m * fator, 1),
             round(b * fator, 1), ",".join(map(str, preds))),
        )


def _ordem_topologica(tarefas):
    """tarefas: dict id -> preds(list). Devolve ids em ordem topológica (Kahn)."""
    grau = {i: len(t["preds"]) for i, t in tarefas.items()}
    fila = [i for i, g in grau.items() if g == 0]
    saida = []
    sucessores = {i: [] for i in tarefas}
    for i, t in tarefas.items():
        for p in t["preds"]:
            sucessores[p].append(i)
    while fila:
        i = fila.pop(0)
        saida.append(i)
        for s in sucessores[i]:
            grau[s] -= 1
            if grau[s] == 0:
                fila.append(s)
    if len(saida) != len(tarefas):
        raise ValueError("Ciclo no grafo de dependências (não é um DAG).")
    return saida, sucessores


def simular(tarefas, n_iter, rng):
    """
    tarefas: dict id -> {nome, a, m, b, preds}.
    Retorna (fim_projeto[n_iter], criticidade{id: %}, layout_p50{id: (es, ef, dur, folga, crit)}).
    """
    ids = list(tarefas)
    ordem, sucessores = _ordem_topologica(tarefas)

    # Amostra as durações de todas as tarefas de uma vez (matriz n_iter x n_tarefas).
    # Guarda o caso degenerado (a==b, tarefa sem incerteza): a Triangular do numpy
    # exige left < right, então uma duração fixa vira um vetor constante.
    def _dur(t):
        if t["a"] >= t["b"]:
            return np.full(n_iter, float(t["m"]))
        return amostrar("Triangular", n_iter, rng, minimo=t["a"], moda=t["m"], maximo=t["b"])
    dur = {i: _dur(tarefas[i]) for i in ids}

    # Forward pass vetorizado: ES = max(EF dos predecessores); EF = ES + dur.
    ES = {i: np.zeros(n_iter) for i in ids}
    EF = {i: np.zeros(n_iter) for i in ids}
    for i in ordem:
        preds = tarefas[i]["preds"]
        ES[i] = np.maximum.reduce([EF[p] for p in preds]) if preds else np.zeros(n_iter)
        EF[i] = ES[i] + dur[i]
    fim_proj = np.maximum.reduce([EF[i] for i in ids])

    # Backward pass -> folga -> tarefa crítica nesta iteração (folga ~ 0).
    LF = {i: fim_proj.copy() for i in ids}
    LS = {i: np.zeros(n_iter) for i in ids}
    for i in reversed(ordem):
        sucs = sucessores[i]
        LF[i] = np.minimum.reduce([LS[s] for s in sucs]) if sucs else fim_proj
        LS[i] = LF[i] - dur[i]
    crit_conta = {i: float((np.abs(LS[i] - ES[i]) < 1e-6).mean() * 100.0) for i in ids}

    # Layout p50 para o Gantt: usa a MÉDIA PERT (a+4m+b)/6 num único forward pass.
    pert = {i: (tarefas[i]["a"] + 4 * tarefas[i]["m"] + tarefas[i]["b"]) / 6 for i in ids}
    es, ef = {}, {}
    for i in ordem:
        preds = tarefas[i]["preds"]
        es[i] = max((ef[p] for p in preds), default=0.0)
        ef[i] = es[i] + pert[i]
    fim_det = max(ef.values())
    lf, ls = {}, {}
    for i in reversed(ordem):
        sucs = sucessores[i]
        lf[i] = min((ls[s] for s in sucs), default=fim_det)
        ls[i] = lf[i] - pert[i]
    layout = {i: (es[i], ef[i], pert[i], ls[i] - es[i], int(abs(ls[i] - es[i]) < 1e-6))
              for i in ids}
    return fim_proj, crit_conta, layout


def _prazo_alvo(projeto, p50):
    """
    Prazo baseline = COMPROMISSO DE GESTÃO (promessa externa a um stakeholder), não a
    soma da estimativa. Em produção viria do plano; no demo é derivado do P50 com um
    buffer que varia por projeto (0,94..1,18), gerando um portfólio realista com
    projetos no prazo e em risco. A soma PERT determinística é sempre otimista por causa
    do viés de convergência (merge bias), então commitar nela seria a armadilha que este
    recurso justamente expõe.
    """
    h = sum(ord(c) for c in projeto)
    buffer = 0.94 + (h % 13) * 0.02      # 0.94 .. 1.18
    return round(float(p50) * buffer, 1)


def gravar(conn, projeto, fim_proj, crit, layout, tarefas, n_iter):
    cur = conn.cursor()
    p10, p50, p80, p95 = np.percentile(fim_proj, [10, 50, MC_CRONO_CONF, 95])
    prazo = _prazo_alvo(projeto, p50)
    prob = float((fim_proj <= prazo).mean() * 100.0)
    cur.execute("DELETE FROM mc_cronograma WHERE project_name=?", (projeto,))
    cur.execute("INSERT INTO mc_cronograma VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                (projeto, n_iter, prazo, float(fim_proj.mean()),
                 float(fim_proj.min()), float(fim_proj.max()),
                 float(p10), float(p50), float(p80), float(p95), prob))

    bordas, freq, cumul = histograma(fim_proj, bins=MC_BINS)
    cur.execute("DELETE FROM mc_cronograma_hist WHERE project_name=?", (projeto,))
    for b, f, c in zip(bordas[:-1], freq, cumul):
        cur.execute("INSERT INTO mc_cronograma_hist VALUES (?,?,?,?)",
                    (projeto, float(b), int(f), float(c)))

    cur.execute("DELETE FROM cronograma_critico WHERE project_name=?", (projeto,))
    for i in tarefas:
        es, ef, dur, folga, ehc = layout[i]
        cur.execute("INSERT INTO cronograma_critico VALUES (?,?,?,?,?,?,?,?,?)",
                    (projeto, i, tarefas[i]["nome"], float(es), float(ef), float(dur),
                     float(folga), float(crit[i]), ehc))
    conn.commit()
    return prazo, p50, p80, prob


def main():
    init_schema()
    conn = get_conn()
    cur = conn.cursor()

    projetos = [r[0] for r in cur.execute(
        "SELECT DISTINCT project_name FROM projetos_status ORDER BY project_name")]
    if not projetos:
        projetos = [f"Project {chr(65+i)}" for i in range(10)]

    # Semeia a WBS demo se ainda não houver tarefas.
    if not cur.execute("SELECT COUNT(*) FROM cronograma_tarefas").fetchone()[0]:
        for p in projetos:
            seed_tarefas(cur, p)
        conn.commit()

    rng = np.random.default_rng(MC_SEED)
    print(f"▶️  Cronograma Monte Carlo — {len(projetos)} projetos × {MC_CRONO_ITER:,} iterações")
    for proj in projetos:
        rows = cur.execute(
            "SELECT tarefa_id, nome, dur_min, dur_prob, dur_max, predecessoras "
            "FROM cronograma_tarefas WHERE project_name=? ORDER BY tarefa_id", (proj,)
        ).fetchall()
        if not rows:
            continue
        tarefas = {r[0]: {"nome": r[1], "a": r[2], "m": r[3], "b": r[4],
                          "preds": [int(x) for x in r[5].split(",") if x]} for r in rows}
        fim, crit, layout = simular(tarefas, MC_CRONO_ITER, rng)
        prazo, p50, p80, prob = gravar(conn, proj, fim, crit, layout, tarefas, MC_CRONO_ITER)
        print(f"   {proj:<12} baseline={prazo:5.1f}d  P50={p50:5.1f}  P80={p80:5.1f}  "
              f"P(no prazo)={prob:4.1f}%")
    conn.close()
    print("✅ Cronograma Monte Carlo concluído (semente 42, reprodutível).")


if __name__ == "__main__":
    main()
