# 🧭 CHECKPOINT — Ponto de Retomada

> **Framework "Gestão de Projetos (PM) IA com Painel BSC e DashBoard"** · ©️ Bruno Teixeira Penedo — 2026. Todos os direitos reservados. E-mail: bpenedo@gmail.com
>
> Snapshot do estado do projeto para **continuar daqui**. Atualizado em **04/07/2026**.

## ✅ O que está PRONTO
- **Pipeline completo:** Langfuse (async + Rust) → SQLite → Evidence; corrigido p/ SDK v4 (`fields=core,io,usage,metadata`, `project_name` via metadata).
- **KPIs (70+):** 4 perspectivas BSC + economia de tokens (IEET/IOLI/ITR/IITA/PEUC/ICCA/IDLS/IBMT) + EVM + fronteira (VRT/kTR, PSR) + diagnóstico (HCI, Wastes Lean, RCA de alucinação).
- **Financeiro:** VPL, TIR, ILL, Payback simples/descontado, dolarização vs SELIC/EUA.
- **Decisão:** **AHP-TOPSIS 2n** (dupla normalização) — pesos AHP (CR=0,012) + ranking robusto (8/10). Vencedor atual: **`Project F`** (Ci=0,96) — *com ressalva* (financeiro placeholder empatado).
- **Visual:** dashboard Evidence, mapa 5D, donuts, quadrante, figuras estilizadas (gekko/shark) no MCDA, pitch decks (LaTeX).
- **Planos & impostos:** `planos_assinatura_IA.md` + tabela no dashboard com câmbio + **IOF 3,5%**.
- **Validação:** triple-check matemático (13 KPIs + VPL/TIR/ILL) — todos conferem à mão.
- **Publicado:** GitHub **privado** `bpenedo/Framework_VPL_ProjetosIA` (5+ commits).

## 📊 Dados em uso AGORA
- **Dashboard local:** banco **privado** dos **10 projetos reais** (restaurado de `_private/`).
- ⚠️ **Financeiro/progresso = PLACEHOLDER** (só tokens/RCA são reais). Langfuse conectado (região **US**), mas **vazio** (traces de teste já removidos).

## ⏳ PENDÊNCIAS para continuar (prioridade)
1. **Fluxos de caixa REAIS por projeto** → re-rodar `ahp_topsis.py` para o **veredito MCDA definitivo** (o financeiro carrega 75% do peso e hoje está empatado).
2. **Dados reais do Langfuse** → instrumentar apps com `metadata.project_name`; depois `./run_all.sh`.
3. **Config do plano PRO (flat):** pôr o valor do PRO em `assinaturas_infra` e `PRECO_API_POR_1K≈0` (ver `planos_assinatura_IA.md`).
4. **Verificar alíquota de IOF vigente** (mudou por decreto em 2025).

## ▶️ Como RETOMAR
```bash
cd foundations/pipeline
# ver o dashboard privado (10 projetos reais):
./restore_real.sh && cd ../evidence && npm run dev      # http://localhost:3000
# OU esteira completa (demo anônima Project A..J):  ../pipeline/run_all.sh --mock
# re-rodar só a decisão MCDA:  cd ../pipeline && python3 ahp_topsis.py
# gerar pitch decks:  python3 gerar_pitchdeck.py
```

## 🗂️ Mapa de arquivos-chave (pipeline/)
| Arquivo | Função |
|---|---|
| `run_all.sh` | esteira: sync → KPIs → VPL → seed_planos → **ahp_topsis** → 5D → pitch → build |
| `sync_langfuse.py` | ETL async + Rust (v4 corrigido) |
| `ahp_topsis.py` | decisão multicritério (AHP-TOPSIS 2n) |
| `carregar_fluxo.py` | VPL/TIR/ILL/Payback (lê `fluxo_caixa.csv`) |
| `gerar_pitchdeck.py` | pitch deck LaTeX dos elegíveis |
| `gerar_5d_projetos.py` | mapa 5D (lib vendorizada) |
| `seed_dimensoes.py` / `seed_demo.py` / `seed_from_folders.py` | seeds |
| `queries/kpis_bsc_ia.sql` | query mestra dos KPIs |
| `_private/` (git-ignored) | banco real + 5D real + transcripts de sessão |

## 📌 Estado git
- Repo **privado**, branch `main`. Docs/código versionados; **dados/segredos git-ignored** (`.db`, `.env`, `_private/`, `pitchdeck_*`, 5D png, Rust build).
- Antes de publicar mais amplamente: rodar sanitização do `github_load.md` + triple-check de privacidade.

> _Retome pela pendência #1 (fluxos de caixa reais) para fechar o veredito de investimento._
