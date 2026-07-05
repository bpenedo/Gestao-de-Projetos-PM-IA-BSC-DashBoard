# 🚀 github_load.md — Checklist de Publicação (de-personalização)

> **Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard** · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
>
> **OBJETIVO:** antes de **qualquer** publicação no GitHub, remover **todas as informações pessoais**
> e referências aos projetos reais de testes localizados em `~/devparetoprojects/*`. Esses dados
> (nomes de projetos, consumo, logs, imagens) são **privados** e **não** podem entrar no pacote final.
>
> **Princípio:** o pacote público deve rodar **só com os dados de demonstração genéricos**
> (`seed_mock.py` → projetos "Ferramentas de Backtest", "Automacoes RPA n8n", "Extensoes Chrome PWAs"),
> nunca com os 10 projetos reais varridos de `~/devparetoprojects/*`.

---

## 1. Inventário de artefatos com dados pessoais

| Artefato | O que vaza | Ação antes do commit |
|---|---|---|
| `pipeline/bsc_ia.db` | nomes reais dos 10 projetos + consumo | **NÃO versionar** (gitignore `*.db`) — regenerar com `seed_mock.py` |
| `evidence/sources/bsc/bsc_ia.db` | idem (cópia para o Evidence) | **NÃO versionar** (gitignore) |
| `evidence/static/5d_projetos.png` | mapa 5D com **nomes reais** visíveis | **Apagar** e regerar a partir do `seed_mock.py` (nomes genéricos) |
| `evidence/build/` | HTML renderizado com nomes reais (`projetos/<nome real>/`) | **NÃO versionar** (gitignore `build/`) |
| `evidence/.evidence/` | cache/parquet com os dados | **NÃO versionar** (gitignore) |
| `foundations/watchdog.log` | caminhos e nomes de pastas de sessões reais | **Apagar** + **NÃO versionar** (gitignore) |
| `pipeline/weekly_reports/` | relatórios semanais (podem citar projetos reais) | **NÃO versionar** (gitignore) |
| `pipeline/.env` | **chaves Langfuse** (segredo) | **NUNCA versionar** (gitignore `.env`) |
| `pipeline/gerar_5d_projetos.py` | (resolvido) lib 5D **já vendorizada** em `pipeline/` | Nada — sem dependência externa (ver passo 4) |
| `pipeline/seed_from_folders.py` | **varre** `~/devparetoprojects/*` (máquina pessoal) | Manter como ferramenta **local-only**, mas **não** usá-la para gerar dados do pacote público |
| `~/.claude/settings.json` (hook) | caminho absoluto pessoal do watchdog | Fora do repo — **não** incluir; documentar como passo de instalação local |

---

## 2. `.gitignore` consolidado (raiz do repositório)

Garanta que o `.gitignore` do projeto contenha:

```gitignore
# Dados pessoais / segredos — NUNCA publicar
**/*.db
**/*.db-journal
**/.env
foundations/watchdog.log
foundations/pipeline/weekly_reports/
foundations/pipeline/__pycache__/
**/*.pyc

# Evidence (build e cache)
foundations/evidence/build/
foundations/evidence/.evidence/
foundations/evidence/node_modules/

# Artefato 5D com dados reais (regerar a partir do seed genérico)
foundations/evidence/static/5d_projetos.png

# Build do módulo Rust (recompilável via `maturin build --release`)
foundations/pipeline/analise_rs/target/
**/*.whl
**/*.so
```

> Versione o **código-fonte** do Rust (`analise_rs/Cargo.toml`, `src/lib.rs`, `pyproject.toml`) —
> só o build (`target/`, `.whl`, `.so`) fica de fora. O `analise.py` tem fallback puro-Python,
> então o pacote funciona mesmo sem compilar o Rust.

---

## 3. Procedimento de sanitização (rodar antes do `git init`/push)

```bash
cd foundations

# 3.1 Apagar artefatos com dados reais
rm -f watchdog.log
rm -f pipeline/bsc_ia.db evidence/sources/bsc/bsc_ia.db
rm -f evidence/static/5d_projetos.png
rm -rf evidence/build evidence/.evidence
rm -rf pipeline/weekly_reports pipeline/__pycache__

# 3.2 Regerar SOMENTE com dados de DEMONSTRAÇÃO genéricos (3 projetos fictícios)
cd pipeline
python3 seed_mock.py          # NÃO usar seed_from_folders.py (varre projetos reais)
python3 compute_kpis.py | head -5
python3 gerar_5d_projetos.py  # 5D com nomes genéricos (após o passo 4)

# 3.3 Reconstruir o Evidence com os dados genéricos
cp bsc_ia.db ../evidence/sources/bsc/bsc_ia.db
cd ../evidence && npm run sources && npm run build
```

> ⚠️ Após sanitizar, o `.db` e o `.png` voltam a existir — por isso eles ficam no `.gitignore`
> (passo 2). O **PNG genérico** pode ser commitado se desejar um preview no README; nesse caso,
> remova a linha do PNG do `.gitignore` **somente após** confirmar que ele foi gerado do `seed_mock`.

---

## 4. Biblioteca 5D (já vendorizada — autossuficiente)

A lib do mapa 5D **já está vendorizada** em `pipeline/fivedchart_lib.py` e o
`gerar_5d_projetos.py` a importa localmente — **sem dependência de projeto externo**:
```python
from fivedchart_lib import render_5d   # vendorizada localmente em pipeline/
```
Nada a fazer aqui. (Se um dia precisar re-vendorizar de outra fonte sua, basta copiar o
seu `fivedchart_lib.py` para `foundations/pipeline/`.)

---

## 5. Varredura final — nada pessoal pode restar

Antes do push, rode e confirme **zero ocorrências** dos nomes reais:

```bash
cd /caminho/do/Framework
# Liste OS SEUS nomes reais a checar (preencha — NÃO versione nomes reais aqui)
PESSOAIS="SEU_PROJETO_1|SEU_PROJETO_2|SEU_PROJETO_N|devparetoprojects"
grep -rInE "$PESSOAIS" . \
  --exclude-dir=node_modules --exclude-dir=.evidence --exclude-dir=build \
  --exclude=github_load.md --exclude=*.db || echo "✅ LIMPO — nenhuma referência pessoal"
```
> Se aparecer algo fora de `github_load.md`, remova/neutralize antes de publicar.
> Também rode `git status --ignored` e confirme que `*.db`, `.env`, `watchdog.log`, `build/`,
> `.evidence/` estão **ignorados**.

---

## 6. Checklist final (marque antes do `git push`)

- [ ] `.gitignore` do passo 2 aplicado.
- [ ] `bsc_ia.db` (ambos), `watchdog.log`, `evidence/build`, `.evidence`, `weekly_reports/` removidos e ignorados.
- [ ] `.env` **fora** do commit (chaves Langfuse nunca publicadas).
- [ ] Dados regenerados via `seed_mock.py` (genéricos), **não** `seed_from_folders.py`.
- [ ] `fivedchart_lib.py` vendorizada em `pipeline/` (sem import de projeto pessoal).
- [ ] 5D PNG regenerado com nomes genéricos (ou removido).
- [ ] Varredura do passo 5 retornou **LIMPO**.
- [ ] Hook do watchdog documentado como **instalação local** (não vai no repo).
- [ ] README do pacote aponta apenas para o fluxo de demonstração genérico.

> ✅ Só publique no GitHub depois que **todos** os itens acima estiverem marcados.
