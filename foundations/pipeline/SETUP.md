# ⚙️ SETUP — Comece em 5 minutos (traga as SUAS chaves)

> Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
> **Cada usuário usa a PRÓPRIA conta Langfuse.** Nenhuma chave do autor acompanha este pacote.

## Pré-requisitos
- Python 3.10+ · Node 18+ / npm · (opcional) Rust + maturin para acelerar a classificação.

## 1. Instale as dependências
```bash
cd foundations/pipeline
pip install -r requirements.txt
cd ../evidence && npm install && cd ../pipeline
```

## 2. 🔑 Traga as SUAS chaves do Langfuse
As chaves ficam **só na sua máquina** (no `.env`, que é git-ignored — nunca vai para o GitHub).

1. Pegue suas chaves em **https://cloud.langfuse.com → Settings → API Keys**.
2. Crie o `.env` a partir do template e preencha:
```bash
cp .env.example .env
```
3. Edite `.env` com as SUAS chaves (ou rode o one-liner abaixo trocando os valores):
```bash
printf 'LANGFUSE_PUBLIC_KEY=pk-lf-SUA_PUBLICA\nLANGFUSE_SECRET_KEY=sk-lf-SUA_SECRETA\nLANGFUSE_HOST=https://cloud.langfuse.com\nPRECO_API_POR_1K=0.025\n' > .env
```
> Use `https://us.cloud.langfuse.com` se sua conta for da região US.
> ⚠️ **Nunca** coloque chaves reais no `.env.example` (esse vai para o git). Só no `.env`.

## 3. Tag de projeto nas suas aplicações (pré-requisito #1)
No seu código que chama OpenAI/Anthropic via Langfuse, identifique o projeto:
```js
const trace = langfuse.trace({ name: "meu_projeto", userId: user.id,
  metadata: { plan: user.plan, platform: "app" } });
```
Sem o `name` (tag), os KPIs financeiros por projeto não fecham.

## 4. Rode a esteira
```bash
./run_all.sh            # sync REAL do Langfuse → SQLite → Evidence
# ou, para ver tudo funcionando SEM Langfuse (dados de demonstração anônimos):
./run_all.sh --mock
```

## 5. Abra o dashboard
```bash
cd ../evidence && npm run dev    # http://localhost:3000
```

## (Opcional) Acelerar a classificação com Rust
```bash
cd analise_rs && maturin build --release && pip install --force-reinstall target/wheels/*.whl
```
Sem isso, o `analise.py` usa o fallback puro-Python (idêntico, só mais lento). Zero-erro garantido.

## Segurança — resumo
- Suas chaves são **pessoais e intransferíveis**; o secret (`sk-lf-`) dá acesso aos **seus** dados.
- O `.env` (chaves reais) é **git-ignored** → quem baixar o projeto **não vê** suas chaves e usa as próprias.
- Se uma chave vazar, **rotacione** no painel do Langfuse (Settings → API Keys).
