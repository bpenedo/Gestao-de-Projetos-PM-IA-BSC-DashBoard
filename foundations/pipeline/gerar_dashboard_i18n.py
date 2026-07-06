"""
gerar_dashboard_i18n.py — Gera as versões LOCALIZADAS do dashboard Evidence a partir do
CADASTRO-CHAVE em foundations/translation.md (bloco JSON após `<!-- i18n:dashboard -->`).

Padroniza e agiliza a tradução: copia pages/index.md e substitui APENAS as strings
registradas no cadastro (título, blockquotes, títulos de gráficos/colunas, Bottom-Line,
legendas). Todo o código (SQL, ECharts, componentes, bindings) permanece intacto. Strings
não-registradas simplesmente permanecem em PT (degradação graciosa — nunca quebra o build).

Também DES-IDENTIFICA: as traduções do Bottom-Line no cadastro usam o binding dinâmico
{mcda_top[0].project_name} e termos genéricos — nenhuma página localizada carrega nome real.

Saída: pages/<lang>/index.md  (rotas /en, /es, /fr, /de, /zh, /ko, /hi)

Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard · ©️ Bruno Penedo — 2026.
https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
"""
import json
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
IDX = os.path.join(BASE, "..", "evidence", "pages", "index.md")
TRANS = os.path.join(BASE, "..", "translation.md")
PAGES = os.path.join(BASE, "..", "evidence", "pages")

ROUTES = {"pt": "/", "en": "/en", "es": "/es", "fr": "/fr",
          "de": "/de", "zh": "/zh", "ko": "/ko", "hi": "/hi", "he": "/he", "sv": "/sv", "ru": "/ru", "fi": "/fi"}
ORDER = ["pt", "en", "es", "fr", "de", "zh", "ko", "hi", "he", "sv", "ru", "fi"]

# DES-IDENTIFICAÇÃO (privacidade): o index.md JÁ é anônimo na fonte (usa {mcda_top[0].project_name}).
# Isto é apenas uma REDE DE SEGURANÇA local: pares real->anônimo vindos de _private/deident.json
# (git-ignored). Ausente => lista vazia. NENHUM nome real fica no código versionado.
def _load_deident():
    p = os.path.join(BASE, "..", "_private", "deident.json")
    try:
        return [tuple(x) for x in json.load(open(p, encoding="utf-8"))]
    except Exception:
        return []


DEIDENT = _load_deident()


# TM (Translation Memory) PRIVADA — fora do pacote público (git-ignored).
TM_PRIVATE = os.path.join(BASE, "..", "_private", "translation_memory.json")
IMG_I18N = os.path.join(BASE, "..", "_private", "image_i18n.json")
_IMG = {}
if os.path.exists(IMG_I18N):
    try:
        _IMG = json.load(open(IMG_I18N, encoding="utf-8"))
    except Exception:
        _IMG = {}
# queries do Evidence cujas categorias de prompt devem ser traduzidas (DuckDB EXCLUDE+CASE)
CAT_SQL = {
    "select * from bsc.alucinacao_categoria": ("prompt_categoria", "bsc.alucinacao_categoria"),
    "select * from bsc.rca_intersecao": ("prompt_categoria", "bsc.rca_intersecao"),
    "select * from bsc.rca_projeto": ("prompt_gargalo", "bsc.rca_projeto"),
}


def _cat_case(lang, col, tbl):
    cats = {k[4:]: v for k, v in _IMG.get(lang, {}).items() if k.startswith("cat_")}
    if not cats:
        return None
    whens = " ".join("WHEN '{}' THEN '{}'".format(sc.replace("'", "''"), tg.replace("'", "''"))
                     for sc, tg in cats.items())
    return "select * exclude ({c}), CASE {c} {w} ELSE {c} END as {c} from {t}".format(c=col, w=whens, t=tbl)

def load_registry():
    if os.path.exists(TM_PRIVATE):
        return json.load(open(TM_PRIVATE, encoding="utf-8"))
    # fallback legado: bloco JSON embutido no translation.md
    txt = open(TRANS, encoding="utf-8").read()
    m = re.search(r"<!--\s*i18n:dashboard\s*-->\s*```json\s*(\{.*?\})\s*```", txt, re.S)
    if not m:
        raise SystemExit("⚠️  TM não encontrada: falta _private/translation_memory.json (ou bloco em translation.md)")
    return json.loads(m.group(1))


def selector(active, labels):
    parts = []
    for l in ORDER:
        lab = labels.get(l, l)
        parts.append(f"**{lab}**" if l == active else f"[{lab}]({ROUTES[l]})")
    return "🌐 " + " · ".join(parts)



def _case_by_prefix(lang, col, prefix):
    cats = {k[len(prefix):]: v for k, v in _IMG.get(lang, {}).items() if k.startswith(prefix)}
    if not cats:
        return None
    whens = " ".join("WHEN '{}' THEN '{}'".format(sc.replace("'", "''"), tg.replace("'", "''"))
                     for sc, tg in cats.items())
    return "CASE {c} {w} ELSE {c} END as {c}".format(c=col, w=whens)


def _traduz_proj_categorias(out, lang):
    wc = _case_by_prefix(lang, "categoria_waste", "wcat_")
    if wc:
        out = out.replace("select categoria_waste,", "select " + wc + ",")
    pc = _case_by_prefix(lang, "prompt_categoria", "cat_")
    if pc:
        out = out.replace("select prompt_categoria,", "select " + pc + ",")
    so = _case_by_prefix(lang, "solucao", "sol_")
    if so:
        out = out.replace(", solucao from", ", " + so + " from")
    return out


def gerar_projeto_pages(strings, labels):
    src_path = os.path.join(PAGES, "projetos", "[projeto].md")
    if not os.path.exists(src_path):
        return
    src = open(src_path, encoding="utf-8").read()
    for lang in [l for l in ORDER if l != "pt"]:
        out = src
        for key in sorted(strings, key=len, reverse=True):
            val = strings[key].get(lang)
            if val and key in out:
                out = out.replace(key, val)
        for a, b in DEIDENT:
            out = out.replace(a, b)
        out = _traduz_proj_categorias(out, lang)
        d = os.path.join(PAGES, lang, "projetos")
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "[projeto].md"), "w", encoding="utf-8").write(out)
    print("  \u2713 paginas por projeto localizadas (pages/<lang>/projetos/)")


def main():
    reg = load_registry()
    src = open(IDX, encoding="utf-8").read()
    labels = reg["selector_labels"]
    strings = reg["strings"]
    langs = reg["meta"]["langs"]

    for lang in langs:
        out = src
        # substitui strings registradas — chaves mais longas primeiro (evita clobber parcial)
        miss = 0
        for key in sorted(strings, key=len, reverse=True):
            val = strings[key].get(lang)
            if not val:
                continue
            if key in out:
                out = out.replace(key, val)
            else:
                miss += 1
        # des-identificação (páginas localizadas = anônimas)
        for a, b in DEIDENT:
            out = out.replace(a, b)
        # imagem 5D localizada por idioma (Passo 2 i18n)
        out = out.replace("/5d_projetos.png", f"/5d_{lang}.png")
        # imagens do dossiê localizadas por idioma
        out = out.replace("/admtools/pt/", f"/admtools/{lang}/")
        out = out.replace('href="/projetos/', f'href="/{lang}/projetos/')
        # categorias de prompt traduzidas nos gráficos Evidence (DuckDB)
        for _orig, (_col, _tbl) in CAT_SQL.items():
            _case = _cat_case(lang, _col, _tbl)
            if _case:
                out = out.replace(_orig, _case)
        # título do front-matter
        out = re.sub(r"(?m)^title:.*$", "title: " + reg["title"][lang], out, count=1)
        # insere seletor de idioma logo após o front-matter
        fm = out.split("---", 2)
        if len(fm) >= 3:
            out = fm[0] + "---" + fm[1] + "---\n\n" + selector(lang, labels) + "\n" + fm[2]
        os.makedirs(os.path.join(PAGES, lang), exist_ok=True)
        with open(os.path.join(PAGES, lang, "index.md"), "w", encoding="utf-8") as f:
            f.write(out)
        print(f"  ✓ pages/{lang}/index.md   ({len(strings)-miss}/{len(strings)} strings aplicadas)")

    # adiciona/atualiza o seletor no topo da página PT (após front-matter), sem duplicar
    if "🌐 **Português**" not in src:
        fm = src.split("---", 2)
        if len(fm) >= 3:
            newpt = fm[0] + "---" + fm[1] + "---\n\n" + selector("pt", labels) + "\n" + fm[2]
            open(IDX, "w", encoding="utf-8").write(newpt)
            print("  ✓ seletor de idioma inserido na página PT")
    gerar_projeto_pages(strings, labels)
    print(f"✅ Dashboards localizados gerados para: {', '.join(langs)}")


if __name__ == "__main__":
    main()
