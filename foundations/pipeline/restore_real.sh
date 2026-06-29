#!/bin/bash
# Restaura LOCALMENTE o seu dashboard REAL (10 projetos) a partir do snapshot privado.
# NÃO publique a saída — é privada (real). Para o pacote público use seed_demo.py.
set -euo pipefail
P="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp "$P/../_private/bsc_ia_real.db" "$P/bsc_ia.db"
cp "$P/../_private/5d_real.png" "$P/../evidence/static/5d_projetos.png"
cp "$P/bsc_ia.db" "$P/../evidence/sources/bsc/bsc_ia.db"
cd "$P/../evidence" && npm run sources && npm run build
echo "✅ Dashboard REAL restaurado localmente (privado). NÃO commitar."
