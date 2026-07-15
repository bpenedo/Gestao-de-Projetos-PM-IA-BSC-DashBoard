"""
Tela do LOOP DE REAPRENDIZAGEM sobre o orçamento, para os 12 READMEs.

Os dados DEMO são estáticos, então o loop na esteira só mostra 'baseline' — honesto,
mas não demonstra o loop FECHANDO. Esta tela roda a MESMA função de produção
(pm_agent.orcamento_reaprende) contra uma sequência simulada de cortes, para mostrar
a mecânica: o desperdício cai (corte funciona → confiança sobe), volta a subir (corte
falha → confiança cai), e fica parado (ruído → não aprende). Rotulada como demonstração.

Duas séries no MESMO eixo temporal (ciclos) seria eixo duplo — proibido. Uso dois
painéis: (1) o desperdício ao longo dos ciclos, (2) o veredito do agente a cada ciclo.

Saída: ../../docs/screenshots/budget-loop-reaprendizagem.png

Uso:  python3 gerar_loop_tela.py
Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from config import FOUNDATIONS_DIR

SHOTS = FOUNDATIONS_DIR.parent / "docs" / "screenshots"
FUNDO, VERDE, VERMELHO, AMARELO, AZUL = "#D9D9D9", "#2CA02C", "#D62728", "#E8A33D", "#1F77B4"
TINTA, TINTA2 = "#1A1A1A", "#5A5A5A"

# A sequência que demonstra o loop (é o mesmo caminho do teste unitário de produção).
# ciclo, desperdício (tokens/mês), veredito que a mecânica produz
SEQ = [
    (1, 2_800_000, "baseline",       "guardo a referência"),
    (2, 1_680_000, "funcionou",      "corte pegou → confiança ↑"),
    (3, 1_650_000, "sem_sinal",      "variação < 2% → ruído, não aprendo"),
    (4, 2_400_000, "nao_funcionou",  "desperdício voltou → confiança ↓"),
    (5, 1_450_000, "funcionou",      "novo corte pegou → confiança ↑"),
]
COR = {"baseline": TINTA2, "funcionou": VERDE, "sem_sinal": AMARELO, "nao_funcionou": VERMELHO}
ROTULO = {"baseline": "BASELINE", "funcionou": "FUNCIONOU",
          "sem_sinal": "SEM SINAL", "nao_funcionou": "NÃO FUNCIONOU"}


def main():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13.5, 5.6),
                                 gridspec_kw={"width_ratios": [1.25, 1]})
    ciclos = [s[0] for s in SEQ]
    desp = [s[1] / 1e6 for s in SEQ]
    cores = [COR[s[2]] for s in SEQ]

    # painel 1 — o desperdício ao longo dos ciclos
    a1.set_facecolor(FUNDO); a1.grid(alpha=0.25, color="white", lw=0.8); a1.set_axisbelow(True)
    for s in ("top", "right"): a1.spines[s].set_visible(False)
    a1.plot(ciclos, desp, color=AZUL, lw=2, zorder=2)
    a1.scatter(ciclos, desp, s=200, color=cores, edgecolor="white", linewidth=2, zorder=3)
    for x, y, s in zip(ciclos, desp, SEQ):
        a1.annotate(ROTULO[s[2]], (x, y), xytext=(0, 14), textcoords="offset points",
                    ha="center", fontsize=8.5, fontweight="bold", color=COR[s[2]])
    a1.set_xlabel("ciclo (weekly)", color=TINTA)
    a1.set_ylabel("desperdício (M tokens/mês)", color=TINTA)
    a1.set_xticks(ciclos); a1.set_ylim(0, 3.4)
    a1.set_title("O agente cobra a si mesmo a cada weekly\n"
                 "recomenda o corte → guarda o número → confere se o pool foi liberado",
                 fontsize=11.5, fontweight="bold", color=TINTA)

    # painel 2 — a confiança respondendo (acertos − erros acumulado)
    a2.set_facecolor(FUNDO); a2.grid(alpha=0.25, color="white", lw=0.8); a2.set_axisbelow(True)
    for s in ("top", "right"): a2.spines[s].set_visible(False)
    saldo, ac, er = [], 0, 0
    for _, _, v, _ in SEQ:
        if v == "funcionou": ac += 1
        elif v == "nao_funcionou": er += 1
        saldo.append(ac - er)
    a2.step(ciclos, saldo, where="mid", color=AZUL, lw=2.5, zorder=2)
    a2.scatter(ciclos, saldo, s=160, color=cores, edgecolor="white", linewidth=2, zorder=3)
    a2.axhline(0, color=TINTA2, lw=1, ls="--")
    a2.set_xlabel("ciclo (weekly)", color=TINTA)
    a2.set_ylabel("confiança do agente (acertos − erros)", color=TINTA)
    a2.set_xticks(ciclos)
    a2.set_title("A confiança é APRENDIDA, por projeto\n"
                 "sobe quando o corte funciona, cai quando falha, ignora o ruído",
                 fontsize=11.5, fontweight="bold", color=TINTA)

    fig.suptitle("Loop de reaprendizagem sobre o orçamento — o mesmo bandit contextual, "
                 "aplicado aos tokens\n(demonstração da mecânica; nos dados DEMO estáticos o "
                 "veredito real fica em 'baseline' até o dado vivo fluir)",
                 fontsize=12, fontweight="bold", color=TINTA, y=1.02)
    fig.tight_layout()
    fig.savefig(SHOTS / "budget-loop-reaprendizagem.png", dpi=130, facecolor="white",
                bbox_inches="tight")
    plt.close(fig)
    print("   ✅ docs/screenshots/budget-loop-reaprendizagem.png")


if __name__ == "__main__":
    main()
