#!/bin/bash
# ============================================================================
# Esteira DataOps do BSC de Projetos de IA
# Framework "Gestão de Projetos (PM) IA com Painel BSC e DashBoard" · (c) Bruno Teixeira Penedo — 2026. Todos os direitos reservados. E-mail: bpenedo@gmail.com
# 1) Sincroniza dados (Langfuse real OU mock)  2) publica o .db no Evidence
# 3) recompila o dashboard estático do Evidence.
#
# Uso:
#   ./run_all.sh           -> usa Langfuse (sync_langfuse.py); cai em aviso se sem credenciais
#   ./run_all.sh --mock    -> regenera dados mock (seed_mock.py)
#
# Agendar no cron (ex.: a cada 15 min):
#   */15 * * * * /ABS/foundations/pipeline/run_all.sh >> /ABS/foundations/pipeline/run.log 2>&1
# ============================================================================
set -euo pipefail
PIPELINE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EVIDENCE_DIR="$(cd "$PIPELINE_DIR/../evidence" && pwd)"
DB="$PIPELINE_DIR/bsc_ia.db"

cd "$PIPELINE_DIR"
if [[ "${1:-}" == "--mock" ]]; then
  echo "▶️  Gerando dados DEMO anônimos (Project A..J)..."
  python3 seed_demo.py
else
  echo "▶️  Sincronizando do Langfuse..."
  python3 sync_langfuse.py
fi

echo "▶️  Validando KPIs..."
python3 compute_kpis.py | tail -n 5

echo "▶️  Calculando VPL/Payback (fluxo_caixa.csv se existir, senão demo)..."
python3 carregar_fluxo.py || echo "  (VPL pulado)"

echo "▶️  Gerando Mapa 5D do portfólio..."
python3 gerar_5d_projetos.py || echo "  (5D pulado)"

echo "▶️  Gerando Pitch Decks dos projetos elegíveis (VPL+ILL positivos)..."
python3 gerar_pitchdeck.py || echo "  (pitch decks pulados)"

echo "▶️  Publicando banco no Evidence..."
cp "$DB" "$EVIDENCE_DIR/sources/bsc/bsc_ia.db"

echo "▶️  Recompilando dashboard Evidence..."
cd "$EVIDENCE_DIR"
npm run sources
npm run build

echo "✅ Esteira concluída. Dashboard em: $EVIDENCE_DIR/build/index.html"
