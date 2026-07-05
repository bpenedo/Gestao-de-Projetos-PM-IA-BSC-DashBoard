# 🌐 translation.md — Guia de Internacionalização (i18n)

> **Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard** · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
>
> **Fonte canônica** de palavras-chave e boas práticas de tradução. Toda tradução — atual ou futura —
> deve seguir este guia para manter **consistência terminológica** e **estabilidade de build**.

Idiomas-alvo: **Inglês (en)**, **Espanhol (es)**, **Francês (fr)**, **Alemão (de)**, **Mandarim (zh)**,
**Coreano (ko)**, **Hindi (hi)**, **Hebraico (he — RTL)** — além do original **Português (pt)**.

> ↔️ **RTL:** o **Hebraico (he)** é escrito da direita para a esquerda. O texto flui RTL naturalmente
> no navegador; o layout dos componentes permanece LTR. Para novos idiomas RTL (ex.: Árabe), seguir o mesmo padrão.

---

## 1. Regra de ouro — o que NUNCA se traduz

Preserve **exatamente** (case-sensitive), pois são identificadores técnicos/marca:

- **Siglas de KPI:** `VRT`, `kTR`, `PSR`, `IEET`, `IOLI`, `ITR`, `IITA`, `PEUC`, `ICCA`, `IDLS`, `IBMT`, `CPP`, `HCI`.
- **EVM:** `EVM`, `CPI`, `SPI`, `EAC`, `CPP`.
- **Métodos/ferramentas:** `BSC` (Balanced Scorecard), `Lean Six Sigma`, `PDCA`, `Kaizen`, `GUT`, `SWOT`,
  `PESTELC`, `AHP-TOPSIS 2n`, `BCG`, `RACI`, `5W2H`, `5W4H`, `RCA`, `Ishikawa`.
- **Stack:** `Langfuse`, `Evidence`, `SQLite`, `DuckDB`, `Python`, `Rust`, `PyO3`, `maturin`, `LaTeX`,
  `tectonic`, `Node`, `npm`, `ECharts`, `matplotlib`.
- **Blocos de código, SQL, config ECharts, tags de componentes** (`<BarChart>`, `<DataTable>`, `<Column>`,
  `<ECharts>`), nomes de coluna/campo (`project_name`, `kpi_psr`, …), badges, URLs e caminhos de arquivo.
- **Carimbo de copyright (stamp):** o **nome do framework permanece em português** em todos os idiomas
  (é a marca). Traduz-se apenas a frase de direitos:

| Idioma | "Todos os direitos reservados" |
|---|---|
| en | All rights reserved. |
| es | Todos los derechos reservados. |
| fr | Tous droits réservés. |
| de | Alle Rechte vorbehalten. |
| zh | 保留所有权利。 |
| ko | 모든 권리 보유. |
| hi | सर्वाधिकार सुरक्षित। |

---

## 2. Siglas financeiras — localizar a sigla, manter o conceito

Diferente dos KPIs internos, as siglas financeiras **têm equivalente consagrado** em cada idioma:

| PT | EN | ES | FR | DE | ZH | KO | HI |
|---|---|---|---|---|---|---|---|
| VPL | NPV | VAN | VAN | Kapitalwert (NPV) | 净现值 (NPV) | 순현재가치 (NPV) | NPV |
| TIR | IRR | TIR | TRI | IRR | 内部收益率 (IRR) | 내부수익률 (IRR) | IRR |
| ILL | PI | IR | IP | PI | 盈利指数 (PI) | 수익성지수 (PI) | PI |
| Payback | Payback | Payback | Payback | Amortisation | 回收期 | 회수기간 | पेबैक |
| Fluxo de Caixa | Cash Flow | Flujo de Caja | Flux de trésorerie | Cashflow | 现金流 | 현금흐름 | नकदी प्रवाह |
| Burn Rate | Burn Rate | Burn Rate | Burn Rate | Burn Rate | 消耗率 | 소진율 | बर्न रेट |

> `SELIC` e `IOF` são termos regulatórios brasileiros — **mantidos** com breve aposto explicativo
> (ex.: "SELIC (taxa básica brasileira)").

---

## 3. Glossário de termos de domínio recorrentes

| PT | EN | ES | FR | DE | ZH | KO | HI |
|---|---|---|---|---|---|---|---|
| Projeto Eleito / Jóia da Coroa | Elected Project / Crown Jewel | Proyecto Electo / Joya de la Corona | Projet Élu / Joyau de la Couronne | Auserwähltes Projekt / Kronjuwel | 当选项目 / 皇冠明珠 | 선정 프로젝트 / 왕관의 보석 | चयनित परियोजना / ताज का रत्न |
| Desperdício (Muda) | Waste | Desperdicio | Gaspillage | Verschwendung | 浪费 | 낭비 | अपव्यय |
| Alucinação | Hallucination | Alucinación | Hallucination | Halluzination | 幻觉 | 환각 | मतिभ्रम |
| Gargalo | Bottleneck | Cuello de botella | Goulot | Engpass | 瓶颈 | 병목 | अड़चन |
| Retorno financeiro | Financial return | Retorno financiero | Retour financier | Finanzielle Rendite | 财务回报 | 재무 수익 | वित्तीय प्रतिफल |
| Portfólio | Portfolio | Portafolio | Portefeuille | Portfolio | 组合 | 포트폴리오 | पोर्टफोलियो |
| Sustentabilidade (custo) | Sustainability | Sostenibilidad | Durabilité | Nachhaltigkeit | 可持续性 | 지속가능성 | संधारणीयता |
| Priorização | Prioritization | Priorización | Priorisation | Priorisierung | 优先级排序 | 우선순위 지정 | प्राथमिकता |
| Reunião semanal | Weekly meeting | Reunión semanal | Réunion hebdomadaire | Wöchentliches Meeting | 每周会议 | 주간 회의 | साप्ताहिक बैठक |
| Sumário Executivo | Executive Summary | Resumen Ejecutivo | Résumé Exécutif | Zusammenfassung | 执行摘要 | 요약 보고 | कार्यकारी सारांश |
| Diferencial competitivo | Competitive edge | Ventaja competitiva | Avantage concurrentiel | Wettbewerbsvorteil | 竞争优势 | 경쟁 우위 | प्रतिस्पर्धात्मक बढ़त |

---

## 4. Boas práticas de tradução (checklist)

1. **Só prosa.** Traduza cabeçalhos (`#`), blockquotes (`>`), `title=`/`name`/`xAxisTitle`/`yAxisTitle`,
   `<Column title="…">` e texto narrativo. **Nunca** toque em SQL, JS de ECharts, IDs ou fórmulas.
2. **Preserve emojis e formatação** (negrito, tabelas, listas) — só o texto entre eles muda.
3. **De-identificação (privacidade):** em material anônimo/demo, **nunca hardcode nome real de projeto**.
   Use o binding dinâmico `{mcda_top[0].project_name}` ou termo genérico ("o último colocado"). Ver
   `github_load.md`. Nomes reais só existem no dashboard local privado do autor.
4. **Números e moeda:** mantenha os valores; adapte só o separador quando o idioma exigir. `R$` permanece
   (moeda de origem); acrescente conversão quando já existir no original.
5. **Não quebre palavras longas** em rótulos de figura (ver lição do PESTELC "computacional/energético").
6. **Build-safe:** após gerar páginas traduzidas do Evidence, rode `npm run build` e confirme `exit 0`
   antes de commitar.

---

## 5. Estrutura de arquivos i18n

| Conteúdo | Convenção | Rota/uso |
|---|---|---|
| README raiz | `README.<lang>.md` na raiz | GitHub mostra seletor de idioma |
| Docs de `foundations/` | `i18n/<lang>/<caminho-espelhado>.md` | leitura por idioma |
| Dashboard (Evidence) | `pages/<lang>/index.md` | rotas `/en`, `/es`, … |
| Seletor de idioma | 1ª linha de cada arquivo | `🌐 [Português](…) · [English](…) · …` |

**Fases:** (1) README ×7 ✅ · (2) Dashboard anônimo ×7 + docs-chave (`README`, `KPIs_README`, `SETUP`) ·
(3) demais docs técnicas (`KPIs`, `KPIs_Lean6s_BSC`, `BSC_Dashboard`, `planos_assinatura_IA`, …).

---

## 6. Necessidades futuras / roadmap de automação

- **Seletor de idioma no dashboard:** componente de topo com links para `/`, `/en`, `/es`, …
- **Pipeline de tradução assistida:** script que copia o `index.md`, aplica um **mapa de strings**
  (deste guia) por idioma e mantém o código intacto — evita retype e divergência.
- **Chave-valor central (`i18n/strings.<lang>.json`):** futura extração de todas as strings visíveis para
  um único dicionário por idioma, consumido pelas páginas.
- **CI de consistência:** verificação de que toda sigla da seção 1 permaneceu intacta nas traduções.
- **Novos idiomas:** basta acrescentar coluna nas tabelas 2–3 e um novo `README.<lang>.md` / `pages/<lang>/`.
- **Locale de formatação:** avaliar `Intl.NumberFormat` por idioma no ECharts (tooltips) quando houver
  demanda de público local.

> **Regra viva:** ao introduzir um novo KPI, ferramenta ou termo de domínio, **atualize as tabelas 1–3
> deste arquivo antes** de traduzir qualquer documento novo.

---

## 7. 🧠 Memória de Tradução (TM) do Dashboard — estilo SDL Trados Studio

Esta seção é a **TM (Translation Memory)** do projeto, no espírito de um `.sdltm`/TMX do **SDL Trados
Studio**: um repositório de **unidades de tradução (segmentos)** com o **source (PT)** e os **targets**
em cada idioma. O gerador `pipeline/gerar_dashboard_i18n.py` faz o **leverage por correspondência exata
(100% match)** — cada segmento encontrado no `index.md` é substituído pelo alvo do idioma; segmentos sem
correspondência permanecem em PT (degradação graciosa, nunca quebra o build). **Só prosa entra na TM;
código/SQL/ECharts nunca.** Alvos do Bottom-Line já vêm **des-identificados** (usam
`{mcda_top[0].project_name}` e termos genéricos), garantindo dashboards localizados **anônimos**.

**Como reaproveitar (padronizar e agilizar):** ao criar/editar uma string do dashboard, **adicione o
segmento aqui** (source + 7 targets). Rode o gerador para propagar a todos os idiomas. Novos idiomas =
nova chave em cada segmento.

<!-- i18n:dashboard -->
> 🔐 **A Translation Memory (segmentos source→target) foi movida para `foundations/_private/translation_memory.json`** (git-ignored, não publicada). É a referência privada de pré-publicação; o gerador `pipeline/gerar_dashboard_i18n.py` a consome de lá. As páginas localizadas já geradas (`pages/<lang>/index.md`) permanecem versionadas.
