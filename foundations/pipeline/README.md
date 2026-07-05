# Pipeline BSC de Projetos de IA

> Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
> ETL: **Langfuse → SQLite → Evidence**. Documentação dos KPIs: [`../KPIs_README.md`](../KPIs_README.md).

## Estrutura
```
pipeline/
├── schema.sql            # DDL das 6 tabelas do SQLite
├── config.py             # parâmetros + leitura do .env
├── db.py                 # conexão + init do schema
├── analise.py            # classificação Lean de falhas (texto bruto)
├── seed_mock.py          # popula dados MOCK (3 projetos) p/ validar
├── sync_langfuse.py      # ETL incremental real (Langfuse -> SQLite)
├── inserir_weekly.py     # cadastro interativo da pauta semanal + git deploy
├── compute_kpis.py       # roda as queries e imprime os KPIs (validação)
├── queries/
│   ├── kpis_bsc_ia.sql   # query mestra (todos os KPIs + VRT/kT + PSR)
│   ├── dominancia_erros.sql  # Pareto de falhas
│   └── alertas_topo.sql  # triagem de alertas críticos
├── requirements.txt
└── .env.example
```

## Início rápido (com dados MOCK)
```bash
cd foundations/pipeline
python3 seed_mock.py       # cria bsc_ia.db e popula 3 projetos de exemplo
python3 compute_kpis.py    # valida: imprime KPIs e Pareto no terminal
```

## Plugando o Langfuse (dados reais)
1. `pip install -r requirements.txt`
2. `cp .env.example .env` e preencha as chaves do Langfuse.
3. `python3 sync_langfuse.py` (carga incremental).
4. Agende no cron (a cada 15 min):
   ```
   */15 * * * * /usr/bin/python3 /ABS/foundations/pipeline/sync_langfuse.py >> sync.log 2>&1
   ```

### Como taguear as chamadas no seu app (atribuição por projeto/usuário)
```js
const trace = langfuse.trace({
  name: "extensao_chrome_resumo",   // vira project_name no SQLite
  userId: user.id,                   // cruza com Stripe/assinaturas
  metadata: { plan: user.plan, platform: "chrome_extension" }
});
```
> **Pré-requisito #1:** sem `name`/tag de projeto, os KPIs financeiros por projeto não fecham.

## Pauta semanal
```bash
python3 inserir_weekly.py   # gera registro no SQLite + Markdown + (opcional) git push
```

## WatchDog de sessões (hook do Claude Code)
`watchdog_session.py` registra cada sessão dos **projetos monitorados** em `foundations/watchdog.log`
e garante o projeto na tabela `projetos_status`. Está ligado a um hook **SessionStart** global em
`~/.claude/settings.json` — roda em toda sessão, mas é **opt-in por projeto**:

- O projeto é monitorado se a pasta contém **`.bscwatch`** (arquivo vazio) **ou** `foundations/KPIs.md`.
- Projetos sem marcador são ignorados silenciosamente (nada é gravado).

**Ativar em outro projeto:** `touch .bscwatch` na raiz dele.
**Revisar/desativar o hook:** rode `/hooks` no Claude Code, ou remova o bloco `hooks.SessionStart`
de `~/.claude/settings.json`. O hook fica ativo a partir da **próxima** sessão (recarregue com `/hooks`).
