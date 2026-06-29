"""
Helper de banco: conexão e inicialização do schema.
"""
import sqlite3
from pathlib import Path
from config import DB_PATH, PIPELINE_DIR


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_schema():
    """Executa schema.sql (idempotente: CREATE TABLE IF NOT EXISTS)."""
    schema_sql = (PIPELINE_DIR / "schema.sql").read_text(encoding="utf-8")
    conn = get_conn()
    try:
        conn.executescript(schema_sql)
        conn.commit()
    finally:
        conn.close()
    print(f"✅ Schema inicializado em: {DB_PATH}")


if __name__ == "__main__":
    init_schema()
