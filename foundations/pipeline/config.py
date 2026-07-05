"""
Configuração central do pipeline BSC de Projetos de IA.
Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
Lê variáveis do ambiente (.env opcional) e expõe caminhos e parâmetros.
"""
import os
from pathlib import Path

# Carrega .env se python-dotenv estiver disponível (opcional, sem quebrar se faltar).
try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent / ".env")
except Exception:
    pass

PIPELINE_DIR = Path(__file__).resolve().parent
FOUNDATIONS_DIR = PIPELINE_DIR.parent
QUERIES_DIR = PIPELINE_DIR / "queries"

# Banco SQLite (compartilhado com o Evidence).
DB_PATH = os.environ.get("BSC_DB_PATH", str(PIPELINE_DIR / "bsc_ia.db"))

# Credenciais Langfuse (preencha no .env para sincronização real).
LANGFUSE_PUBLIC_KEY = os.environ.get("LANGFUSE_PUBLIC_KEY", "")
LANGFUSE_SECRET_KEY = os.environ.get("LANGFUSE_SECRET_KEY", "")
LANGFUSE_HOST = os.environ.get("LANGFUSE_HOST", "https://cloud.langfuse.com")

# Parâmetros financeiros do framework.
PRECO_API_POR_1K = float(os.environ.get("PRECO_API_POR_1K", "0.025"))  # R$ por 1k tokens

# Benchmarks macro para VPL/TIR/ILL (PLACEHOLDERS — ajuste no .env com valores correntes).
SELIC_ANUAL = float(os.environ.get("SELIC_ANUAL", "0.105"))    # taxa SELIC a.a. (BR) — ex.: 10,5%
US_RATE_ANUAL = float(os.environ.get("US_RATE_ANUAL", "0.045"))  # Fed funds a.a. (EUA) — ex.: 4,5%
USD_BRL = float(os.environ.get("USD_BRL", "5.40"))             # câmbio BRL por USD (dolarização)
IOF_PCT = float(os.environ.get("IOF_PCT", "3.5"))              # IOF % sobre compras internacionais (cartão)
PESO_RATE_LIMIT = 1.5   # penalidade de cota
PESO_ALUCINACAO = 2.0   # penalidade de código/alucinação
LIMITE_LATENCIA_S = 3.0  # latência aceitável (Lean); excedente = waste
THRESHOLD_ALERTA_DIA = 10  # nº de falhas/24h que dispara alerta consolidado no cron
