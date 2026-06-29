"""
Camada de auditoria textual (Lean Six Sigma): classifica cada geração em
NENHUM | RATE_LIMIT | ALUCINACAO_CODIGO a partir do texto bruto de input/output.

Backend ACELERADO por Rust (PyO3) quando o módulo compilado `analise_rs` está presente
(ver pipeline/analise_rs/ + `maturin develop --release`). Caso contrário, usa o
fallback puro-Python — comportamento idêntico, ZERO-ERRO (o pipeline nunca quebra).
"""
import re

PADRAO_RATE_LIMIT = re.compile(r"(error 429|rate limit|quota exceeded|too many requests)")
PADROES_CORRECAO_USUARIO = [
    "está errado", "esta errado", "nao funcionou", "não funcionou", "corrija o erro",
    "corrija", "esta quebrado", "está quebrado", "gerou erro", "refaca", "refaça",
]
PADROES_ERRO_IA = [
    "traceback (most recent call last)", "syntaxerror:", "nameerror:",
    "exception occurred", "internal server error", "unhandled exception", "nullpointer",
]


def _classificar_py(prompt_text, resposta_text):
    """Fallback puro-Python. Retorna (tipo_erro, tempo_bloqueado_minutos)."""
    p = (str(prompt_text) if prompt_text else "").lower()
    r = (str(resposta_text) if resposta_text else "").lower()
    if PADRAO_RATE_LIMIT.search(p) or PADRAO_RATE_LIMIT.search(r):
        return "RATE_LIMIT", 5.0
    if (any(t in p for t in PADROES_CORRECAO_USUARIO)
            or any(t in r for t in PADROES_ERRO_IA)):
        return "ALUCINACAO_CODIGO", 0.0
    if len(r.strip()) < 10 or r.endswith("..."):
        return "ALUCINACAO_CODIGO", 0.0
    return "NENHUM", 0.0


# Taxonomia de prompt (RCA de alucinação) inferida por palavras-chave do texto do prompt.
_CAT_KEYS = [
    ("Geracao de Codigo", ["codigo", "código", "code", "funcao", "função", "function", "classe",
                            "script", "def ", "import ", "bug", "compil", "python", "javascript", "sql"]),
    ("Extracao de Dados", ["extrair", "extract", "json", "csv", "tabela", "campo", "parse",
                           "scrap", "raspagem", "planilha"]),
    ("Sumarizacao", ["resum", "summar", "sintetiz", "tl;dr", "tldr"]),
    ("Transformacao/Formato", ["format", "converter", "convert", "traduz", "translate",
                               "reescrev", "rewrite"]),
    ("RAG/Busca", ["busca", "buscar", "search", "pesquis", "documento", "fonte", "retriev", "consulta"]),
    ("Raciocinio/Analise", ["analis", "analyz", "explic", "por que", "porque", "compar",
                            "avalia", "raciocin", "estrateg", "diagnostic"]),
]


def classificar_categoria(prompt_text):
    """Infere a categoria/taxonomia do prompt a partir do texto. Default: Conversa/Aberto."""
    p = (str(prompt_text) if prompt_text else "").lower()
    for nome, chaves in _CAT_KEYS:
        if any(k in p for k in chaves):
            return nome
    return "Conversa/Aberto"


# Seleciona o backend mais rápido disponível (Rust se compilado).
try:
    from analise_rs import classificar as _classificar_rs

    def classificar(prompt_text, resposta_text):
        return _classificar_rs(str(prompt_text or ""), str(resposta_text or ""))

    BACKEND = "rust"
except Exception:
    classificar = _classificar_py
    BACKEND = "python"
