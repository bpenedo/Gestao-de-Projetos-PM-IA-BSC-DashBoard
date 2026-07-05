# 🌐 translation.md — Guia de Internacionalização (i18n)

> **Framework "Gestão de Projetos (PM) IA com Painel BSC e DashBoard"** · ©️ Bruno Teixeira Penedo — 2026. Todos os direitos reservados. E-mail: bpenedo@gmail.com
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
```json
{
  "meta": {
    "langs": [
      "en",
      "es",
      "fr",
      "de",
      "zh",
      "ko",
      "hi",
      "he"
    ],
    "winner_var": "{mcda_top[0].project_name}",
    "leverage": "exact-match (100%)",
    "tool": "TM estilo SDL Trados Studio"
  },
  "selector_labels": {
    "pt": "Português",
    "en": "English",
    "es": "Español",
    "fr": "Français",
    "de": "Deutsch",
    "zh": "中文",
    "ko": "한국어",
    "hi": "हिन्दी",
    "he": "עברית"
  },
  "title": {
    "en": "BSC Panel — AI Project Management (PM)",
    "es": "Panel BSC — Gestión de Proyectos (PM) de IA",
    "fr": "Panneau BSC — Gestion de Projets (PM) IA",
    "de": "BSC-Panel — KI-Projektmanagement (PM)",
    "zh": "BSC 面板 — AI 项目管理（PM）",
    "ko": "BSC 패널 — AI 프로젝트 관리(PM)",
    "hi": "BSC पैनल — AI परियोजना प्रबंधन (PM)",
    "he": "לוח BSC — ניהול פרויקטים (PM) של AI"
  },
  "strings": {
    "**Weekly Checkpoint — toda sexta-feira às 09:00.**": {
      "en": "**Weekly Checkpoint — every Friday at 09:00.**",
      "es": "**Checkpoint Semanal — todos los viernes a las 09:00.**",
      "fr": "**Point Hebdomadaire — chaque vendredi à 09h00.**",
      "de": "**Wöchentlicher Checkpoint — jeden Freitag um 09:00 Uhr.**",
      "zh": "**每周检查点 — 每周五 09:00。**",
      "ko": "**주간 체크포인트 — 매주 금요일 09:00.**",
      "hi": "**साप्ताहिक चेकपॉइंट — हर शुक्रवार 09:00 बजे।**",
      "he": "**נקודת ביקורת שבועית — כל יום שישי בשעה 09:00.**"
    },
    "> ⚠️ **Dados DEMO** dos 10 projetos reais de `~/devparetoprojects/*`. Tornam-se reais quando o Langfuse sincronizar.": {
      "en": "> ⚠️ **DEMO data** (anonymized portfolio). Becomes real once Langfuse syncs.",
      "es": "> ⚠️ **Datos DEMO** (portafolio anonimizado). Se vuelven reales cuando Langfuse sincroniza.",
      "fr": "> ⚠️ **Données DÉMO** (portefeuille anonymisé). Deviennent réelles dès la synchro Langfuse.",
      "de": "> ⚠️ **DEMO-Daten** (anonymisiertes Portfolio). Werden real, sobald Langfuse synchronisiert.",
      "zh": "> ⚠️ **演示数据**（匿名组合）。Langfuse 同步后即为真实数据。",
      "ko": "> ⚠️ **데모 데이터**(익명 포트폴리오). Langfuse 동기화 시 실제 데이터가 됩니다.",
      "hi": "> ⚠️ **डेमो डेटा** (अनाम पोर्टफोलियो)। Langfuse सिंक होने पर वास्तविक बन जाता है।",
      "he": "> ⚠️ **נתוני הדגמה** (תיק מנוטרל). הופכים לאמיתיים לאחר סנכרון Langfuse."
    },
    "Todos os direitos reservados.": {
      "en": "All rights reserved.",
      "es": "Todos los derechos reservados.",
      "fr": "Tous droits réservés.",
      "de": "Alle Rechte vorbehalten.",
      "zh": "保留所有权利。",
      "ko": "모든 권리 보유.",
      "hi": "सर्वाधिकार सुरक्षित।",
      "he": "כל הזכויות שמורות."
    },
    "## 📈 Sumário Executivo do Portfólio": {
      "en": "## 📈 Portfolio Executive Summary",
      "es": "## 📈 Resumen Ejecutivo del Portafolio",
      "fr": "## 📈 Résumé Exécutif du Portefeuille",
      "de": "## 📈 Portfolio-Zusammenfassung",
      "zh": "## 📈 组合执行摘要",
      "ko": "## 📈 포트폴리오 요약 보고",
      "hi": "## 📈 पोर्टफोलियो कार्यकारी सारांश",
      "he": "## 📈 תקציר מנהלים של התיק"
    },
    "## 🌐 Mapa 5D do Portfólio (visão C-Level)": {
      "en": "## 🌐 Portfolio 5D Map (C-Level view)",
      "es": "## 🌐 Mapa 5D del Portafolio (visión C-Level)",
      "fr": "## 🌐 Carte 5D du Portefeuille (vue C-Level)",
      "de": "## 🌐 5D-Portfoliokarte (C-Level-Sicht)",
      "zh": "## 🌐 组合 5D 地图（C 级视图）",
      "ko": "## 🌐 포트폴리오 5D 지도 (C-레벨 관점)",
      "hi": "## 🌐 पोर्टफोलियो 5D मानचित्र (C-लेवल दृश्य)",
      "he": "## 🌐 מפת 5D של התיק (מבט דרג בכיר)"
    },
    "### 🖱️ Mapa 5D Interativo — passe o mouse sobre cada esfera": {
      "en": "### 🖱️ Interactive 5D Map — hover over each sphere",
      "es": "### 🖱️ Mapa 5D Interactivo — pasa el mouse sobre cada esfera",
      "fr": "### 🖱️ Carte 5D Interactive — survolez chaque sphère",
      "de": "### 🖱️ Interaktive 5D-Karte — mit der Maus über jede Kugel fahren",
      "zh": "### 🖱️ 交互式 5D 地图 — 将鼠标悬停在每个球体上",
      "ko": "### 🖱️ 인터랙티브 5D 지도 — 각 구체에 마우스를 올리세요",
      "hi": "### 🖱️ इंटरैक्टिव 5D मानचित्र — प्रत्येक गोले पर माउस ले जाएँ",
      "he": "### 🖱️ מפת 5D אינטראקטיבית — העבירו את העכבר מעל כל כדור"
    },
    "## 📉 Tendência do Indicador-Mestre (CPP) e do Score (PSR)": {
      "en": "## 📉 Master Indicator (CPP) & Score (PSR) Trend",
      "es": "## 📉 Tendencia del Indicador Maestro (CPP) y del Score (PSR)",
      "fr": "## 📉 Tendance de l'Indicateur Maître (CPP) et du Score (PSR)",
      "de": "## 📉 Trend des Leitindikators (CPP) und Scores (PSR)",
      "zh": "## 📉 主指标 (CPP) 与评分 (PSR) 趋势",
      "ko": "## 📉 핵심 지표(CPP) 및 점수(PSR) 추세",
      "hi": "## 📉 मुख्य संकेतक (CPP) और स्कोर (PSR) की प्रवृत्ति",
      "he": "## 📉 מגמת המדד המרכזי (CPP) והציון (PSR)"
    },
    "## ⭐ Score (PSR) por Projeto": {
      "en": "## ⭐ Score (PSR) by Project",
      "es": "## ⭐ Score (PSR) por Proyecto",
      "fr": "## ⭐ Score (PSR) par Projet",
      "de": "## ⭐ Score (PSR) je Projekt",
      "zh": "## ⭐ 各项目评分 (PSR)",
      "ko": "## ⭐ 프로젝트별 점수 (PSR)",
      "hi": "## ⭐ प्रति परियोजना स्कोर (PSR)",
      "he": "## ⭐ ציון (PSR) לפי פרויקט"
    },
    "## 🍩 Composição & Mix (donut com profundidade)": {
      "en": "## 🍩 Composition & Mix (donut with depth)",
      "es": "## 🍩 Composición y Mix (donut con profundidad)",
      "fr": "## 🍩 Composition et Mix (donut avec profondeur)",
      "de": "## 🍩 Zusammensetzung & Mix (Donut mit Tiefe)",
      "zh": "## 🍩 构成与占比（带景深的环形图）",
      "ko": "## 🍩 구성 및 믹스 (입체 도넛)",
      "hi": "## 🍩 संरचना और मिश्रण (गहराई वाला डोनट)",
      "he": "## 🍩 הרכב ותמהיל (תרשים דונאט עם עומק)"
    },
    "## 🧭 Quadrante de Sustentabilidade (escalar ou corrigir?)": {
      "en": "## 🧭 Sustainability Quadrant (scale or fix?)",
      "es": "## 🧭 Cuadrante de Sostenibilidad (¿escalar o corregir?)",
      "fr": "## 🧭 Quadrant de Durabilité (passer à l'échelle ou corriger ?)",
      "de": "## 🧭 Nachhaltigkeitsquadrant (skalieren oder korrigieren?)",
      "zh": "## 🧭 可持续性象限（扩展还是修复？）",
      "ko": "## 🧭 지속가능성 사분면 (확장 vs 개선?)",
      "hi": "## 🧭 संधारणीयता चतुर्थांश (स्केल करें या सुधारें?)",
      "he": "## 🧭 רביע הקיימות (להרחיב או לתקן?)"
    },
    "## 📊 Pareto de Falhas por Projeto": {
      "en": "## 📊 Failure Pareto by Project",
      "es": "## 📊 Pareto de Fallas por Proyecto",
      "fr": "## 📊 Pareto des Défaillances par Projet",
      "de": "## 📊 Fehler-Pareto je Projekt",
      "zh": "## 📊 各项目故障帕累托",
      "ko": "## 📊 프로젝트별 실패 파레토",
      "hi": "## 📊 प्रति परियोजना विफलता पैरेटो",
      "he": "## 📊 פארטו של כשלים לפי פרויקט"
    },
    "## 🗂️ Score & Saúde Financeira (tabela)": {
      "en": "## 🗂️ Score & Financial Health (table)",
      "es": "## 🗂️ Score y Salud Financiera (tabla)",
      "fr": "## 🗂️ Score et Santé Financière (tableau)",
      "de": "## 🗂️ Score & finanzielle Gesundheit (Tabelle)",
      "zh": "## 🗂️ 评分与财务健康（表格）",
      "ko": "## 🗂️ 점수 및 재무 건전성 (표)",
      "hi": "## 🗂️ स्कोर और वित्तीय स्वास्थ्य (तालिका)",
      "he": "## 🗂️ ציון ובריאות פיננסית (טבלה)"
    },
    "## 🚨 Alertas Críticos": {
      "en": "## 🚨 Critical Alerts",
      "es": "## 🚨 Alertas Críticas",
      "fr": "## 🚨 Alertes Critiques",
      "de": "## 🚨 Kritische Warnungen",
      "zh": "## 🚨 关键告警",
      "ko": "## 🚨 중요 경고",
      "hi": "## 🚨 महत्वपूर्ण अलर्ट",
      "he": "## 🚨 התראות קריטיות"
    },
    "## 📅 Pauta da Reunião Semanal": {
      "en": "## 📅 Weekly Meeting Agenda",
      "es": "## 📅 Agenda de la Reunión Semanal",
      "fr": "## 📅 Ordre du Jour de la Réunion Hebdomadaire",
      "de": "## 📅 Agenda des wöchentlichen Meetings",
      "zh": "## 📅 每周会议议程",
      "ko": "## 📅 주간 회의 안건",
      "hi": "## 📅 साप्ताहिक बैठक एजेंडा",
      "he": "## 📅 סדר יום לפגישה השבועית"
    },
    "## 🪙 Custo de Recuperação (VRT) — 5 blocos + média (2ª ótica)": {
      "en": "## 🪙 Cost Recovery (VRT) — 5 blocks + average (2nd lens)",
      "es": "## 🪙 Recuperación de Costos (VRT) — 5 bloques + promedio (2ª óptica)",
      "fr": "## 🪙 Récupération de Coût (VRT) — 5 blocs + moyenne (2e optique)",
      "de": "## 🪙 Kostendeckung (VRT) — 5 Blöcke + Mittelwert (2. Sicht)",
      "zh": "## 🪙 成本回收 (VRT) — 5 个分块 + 平均值（第二视角）",
      "ko": "## 🪙 비용 회수 (VRT) — 5블록 + 평균 (제2 관점)",
      "hi": "## 🪙 लागत वसूली (VRT) — 5 ब्लॉक + औसत (दूसरा दृष्टिकोण)",
      "he": "## 🪙 עלות השבה (VRT) — 5 בלוקים + ממוצע (מבט שני)"
    },
    "## ⏰ Horário Crítico de Interrupção/Impacto (HCI)": {
      "en": "## ⏰ Critical Interruption/Impact Hour (HCI)",
      "es": "## ⏰ Hora Crítica de Interrupción/Impacto (HCI)",
      "fr": "## ⏰ Heure Critique d'Interruption/Impact (HCI)",
      "de": "## ⏰ Kritische Unterbrechungs-/Auswirkungsstunde (HCI)",
      "zh": "## ⏰ 关键中断/影响时段 (HCI)",
      "ko": "## ⏰ 핵심 중단/영향 시간대 (HCI)",
      "hi": "## ⏰ महत्वपूर्ण व्यवधान/प्रभाव समय (HCI)",
      "he": "## ⏰ שעת ההפרעה/ההשפעה הקריטית (HCI)"
    },
    "## ♻️ Taxonomia de Wastes (Lean Six Sigma) — onde mais se desperdiça": {
      "en": "## ♻️ Waste Taxonomy (Lean Six Sigma) — where most is wasted",
      "es": "## ♻️ Taxonomía de Desperdicios (Lean Six Sigma) — dónde se desperdicia más",
      "fr": "## ♻️ Taxonomie des Gaspillages (Lean Six Sigma) — où l'on gaspille le plus",
      "de": "## ♻️ Verschwendungs-Taxonomie (Lean Six Sigma) — wo am meisten verschwendet wird",
      "zh": "## ♻️ 浪费分类 (Lean Six Sigma) — 浪费最多之处",
      "ko": "## ♻️ 낭비 분류 (Lean Six Sigma) — 가장 많이 낭비되는 곳",
      "hi": "## ♻️ अपव्यय वर्गीकरण (Lean Six Sigma) — सबसे अधिक अपव्यय कहाँ",
      "he": "## ♻️ טקסונומיית בזבוזים (Lean Six Sigma) — היכן מבזבזים הכי הרבה"
    },
    "## 🔬 RCA — Alucinação por Tipo de Prompt (o que ATRASA cada projeto)": {
      "en": "## 🔬 RCA — Hallucination by Prompt Type (what DELAYS each project)",
      "es": "## 🔬 RCA — Alucinación por Tipo de Prompt (qué RETRASA cada proyecto)",
      "fr": "## 🔬 RCA — Hallucination par Type de Prompt (ce qui RETARDE chaque projet)",
      "de": "## 🔬 RCA — Halluzination nach Prompt-Typ (was jedes Projekt VERZÖGERT)",
      "zh": "## 🔬 RCA — 按提示词类型的幻觉（是什么在拖慢每个项目）",
      "ko": "## 🔬 RCA — 프롬프트 유형별 환각 (각 프로젝트를 지연시키는 요인)",
      "hi": "## 🔬 RCA — प्रॉम्प्ट प्रकार अनुसार मतिभ्रम (हर परियोजना को क्या धीमा करता है)",
      "he": "## 🔬 RCA — הזיות לפי סוג פרומפט (מה שמעכב כל פרויקט)"
    },
    "### 🎯 Interseção — o gargalo comum ao portfólio": {
      "en": "### 🎯 Intersection — the bottleneck common to the portfolio",
      "es": "### 🎯 Intersección — el cuello de botella común al portafolio",
      "fr": "### 🎯 Intersection — le goulot commun au portefeuille",
      "de": "### 🎯 Schnittmenge — der portfolioweite Engpass",
      "zh": "### 🎯 交集 — 组合共有的瓶颈",
      "ko": "### 🎯 교집합 — 포트폴리오 공통 병목",
      "hi": "### 🎯 प्रतिच्छेदन — पोर्टफोलियो का साझा अड़चन",
      "he": "### 🎯 חיתוך — צוואר הבקבוק המשותף לתיק"
    },
    "### 🧭 Gargalo de alucinação por projeto (RCA individual)": {
      "en": "### 🧭 Hallucination bottleneck per project (individual RCA)",
      "es": "### 🧭 Cuello de botella de alucinación por proyecto (RCA individual)",
      "fr": "### 🧭 Goulot d'hallucination par projet (RCA individuel)",
      "de": "### 🧭 Halluzinations-Engpass je Projekt (individuelle RCA)",
      "zh": "### 🧭 各项目的幻觉瓶颈（单项 RCA）",
      "ko": "### 🧭 프로젝트별 환각 병목 (개별 RCA)",
      "hi": "### 🧭 प्रति परियोजना मतिभ्रम अड़चन (व्यक्तिगत RCA)",
      "he": "### 🧭 צוואר בקבוק של הזיות לפי פרויקט (RCA פרטני)"
    },
    "### 📊 Taxonomia de alucinação por categoria × projeto": {
      "en": "### 📊 Hallucination taxonomy by category × project",
      "es": "### 📊 Taxonomía de alucinación por categoría × proyecto",
      "fr": "### 📊 Taxonomie d'hallucination par catégorie × projet",
      "de": "### 📊 Halluzinations-Taxonomie nach Kategorie × Projekt",
      "zh": "### 📊 按类别 × 项目的幻觉分类",
      "ko": "### 📊 카테고리 × 프로젝트별 환각 분류",
      "hi": "### 📊 श्रेणी × परियोजना अनुसार मतिभ्रम वर्गीकरण",
      "he": "### 📊 טקסונומיית הזיות לפי קטגוריה × פרויקט"
    },
    "## 💰 VPL, Payback & Fluxo de Caixa do Portfólio": {
      "en": "## 💰 NPV, Payback & Portfolio Cash Flow",
      "es": "## 💰 VAN, Payback y Flujo de Caja del Portafolio",
      "fr": "## 💰 VAN, Payback et Flux de Trésorerie du Portefeuille",
      "de": "## 💰 Kapitalwert, Amortisation & Portfolio-Cashflow",
      "zh": "## 💰 NPV、回收期与组合现金流",
      "ko": "## 💰 NPV, 회수기간 및 포트폴리오 현금흐름",
      "hi": "## 💰 NPV, पेबैक और पोर्टफोलियो नकदी प्रवाह",
      "he": "## 💰 NPV, החזר וזרם מזומנים של התיק"
    },
    "## 💳 Planos de Assinatura de IA — Custo Total com IOF": {
      "en": "## 💳 AI Subscription Plans — Total Cost with IOF",
      "es": "## 💳 Planes de Suscripción de IA — Costo Total con IOF",
      "fr": "## 💳 Abonnements IA — Coût Total avec IOF",
      "de": "## 💳 KI-Abonnements — Gesamtkosten mit IOF",
      "zh": "## 💳 AI 订阅计划 — 含 IOF 总成本",
      "ko": "## 💳 AI 구독 요금제 — IOF 포함 총비용",
      "hi": "## 💳 AI सदस्यता योजनाएँ — IOF सहित कुल लागत",
      "he": "## 💳 תוכניות מנוי ל-AI — עלות כוללת עם IOF"
    },
    "### 📌 Bottom-Line — Sumário Executivo & Insights C-Level": {
      "en": "### 📌 Bottom-Line — Executive Summary & C-Level Insights",
      "es": "### 📌 Bottom-Line — Resumen Ejecutivo e Insights C-Level",
      "fr": "### 📌 Bottom-Line — Résumé Exécutif et Insights C-Level",
      "de": "### 📌 Bottom-Line — Zusammenfassung & C-Level-Insights",
      "zh": "### 📌 结论 — 执行摘要与 C 级洞察",
      "ko": "### 📌 결론 — 요약 보고 및 C-레벨 인사이트",
      "hi": "### 📌 निष्कर्ष — कार्यकारी सारांश और C-लेवल इनसाइट्स",
      "he": "### 📌 שורה תחתונה — תקציר מנהלים ותובנות דרג בכיר"
    },
    "## 🔗 Painéis Individuais por Projeto": {
      "en": "## 🔗 Individual Panels by Project",
      "es": "## 🔗 Paneles Individuales por Proyecto",
      "fr": "## 🔗 Tableaux Individuels par Projet",
      "de": "## 🔗 Einzelpanels je Projekt",
      "zh": "## 🔗 各项目独立面板",
      "ko": "## 🔗 프로젝트별 개별 패널",
      "hi": "## 🔗 प्रति परियोजना अलग पैनल",
      "he": "## 🔗 לוחות נפרדים לפי פרויקט"
    },
    "🏆 AHP-TOPSIS 2N — Modelo Multi-Critério Decisório (MCDM)": {
      "en": "🏆 AHP-TOPSIS 2N — Multi-Criteria Decision Model (MCDM)",
      "es": "🏆 AHP-TOPSIS 2N — Modelo de Decisión Multicriterio (MCDM)",
      "fr": "🏆 AHP-TOPSIS 2N — Modèle de Décision Multicritère (MCDM)",
      "de": "🏆 AHP-TOPSIS 2N — Multikriterielles Entscheidungsmodell (MCDM)",
      "zh": "🏆 AHP-TOPSIS 2N — 多准则决策模型 (MCDM)",
      "ko": "🏆 AHP-TOPSIS 2N — 다기준 의사결정 모델 (MCDM)",
      "hi": "🏆 AHP-TOPSIS 2N — बहु-मानदंड निर्णय मॉडल (MCDM)",
      "he": "🏆 AHP-TOPSIS 2N — מודל החלטה רב-קריטריוני (MCDM)"
    },
    "## 👑 Dossiê Administrativo da **Jóia da Coroa** —": {
      "en": "## 👑 Administrative Dossier of the **Crown Jewel** —",
      "es": "## 👑 Dossier Administrativo de la **Joya de la Corona** —",
      "fr": "## 👑 Dossier Administratif du **Joyau de la Couronne** —",
      "de": "## 👑 Verwaltungsdossier des **Kronjuwels** —",
      "zh": "## 👑 **皇冠明珠**行政档案 —",
      "ko": "## 👑 **왕관의 보석** 행정 도시에 —",
      "hi": "## 👑 **ताज के रत्न** का प्रशासनिक डोसियर —",
      "he": "## 👑 תיק מנהלי של **תכשיט הכתר** —"
    },
    "**🎯 SWOT — posição estratégica**": {
      "en": "**🎯 SWOT — strategic position**",
      "es": "**🎯 SWOT — posición estratégica**",
      "fr": "**🎯 SWOT — position stratégique**",
      "de": "**🎯 SWOT — strategische Position**",
      "zh": "**🎯 SWOT — 战略定位**",
      "ko": "**🎯 SWOT — 전략적 위치**",
      "hi": "**🎯 SWOT — रणनीतिक स्थिति**",
      "he": "**🎯 SWOT — מיצוב אסטרטגי**"
    },
    "**🌐 PESTELC — macroambiente**": {
      "en": "**🌐 PESTELC — macro-environment**",
      "es": "**🌐 PESTELC — macroentorno**",
      "fr": "**🌐 PESTELC — macro-environnement**",
      "de": "**🌐 PESTELC — Makroumfeld**",
      "zh": "**🌐 PESTELC — 宏观环境**",
      "ko": "**🌐 PESTELC — 거시환경**",
      "hi": "**🌐 PESTELC — वृहद परिवेश**",
      "he": "**🌐 PESTELC — סביבת מאקרו**"
    },
    "**🗺️ 5W4H — plano de ação (5W + 4H)**": {
      "en": "**🗺️ 5W4H — action plan (5W + 4H)**",
      "es": "**🗺️ 5W4H — plan de acción (5W + 4H)**",
      "fr": "**🗺️ 5W4H — plan d'action (5W + 4H)**",
      "de": "**🗺️ 5W4H — Aktionsplan (5W + 4H)**",
      "zh": "**🗺️ 5W4H — 行动计划（5W + 4H）**",
      "ko": "**🗺️ 5W4H — 실행 계획 (5W + 4H)**",
      "hi": "**🗺️ 5W4H — कार्य योजना (5W + 4H)**",
      "he": "**🗺️ 5W4H — תוכנית פעולה (5W + 4H)**"
    },
    "**📊 Pareto de falhas (80/20)**": {
      "en": "**📊 Failure Pareto (80/20)**",
      "es": "**📊 Pareto de fallas (80/20)**",
      "fr": "**📊 Pareto des défaillances (80/20)**",
      "de": "**📊 Fehler-Pareto (80/20)**",
      "zh": "**📊 故障帕累托（80/20）**",
      "ko": "**📊 실패 파레토 (80/20)**",
      "hi": "**📊 विफलता पैरेटो (80/20)**",
      "he": "**📊 פארטו של כשלים (80/20)**"
    },
    "**🔥 Matriz GUT — priorização (heatmap)**": {
      "en": "**🔥 GUT Matrix — prioritization (heatmap)**",
      "es": "**🔥 Matriz GUT — priorización (heatmap)**",
      "fr": "**🔥 Matrice GUT — priorisation (heatmap)**",
      "de": "**🔥 GUT-Matrix — Priorisierung (Heatmap)**",
      "zh": "**🔥 GUT 矩阵 — 优先级排序（热力图）**",
      "ko": "**🔥 GUT 매트릭스 — 우선순위 (히트맵)**",
      "hi": "**🔥 GUT मैट्रिक्स — प्राथमिकता (हीटमैप)**",
      "he": "**🔥 מטריצת GUT — תעדוף (מפת חום)**"
    },
    "**🕸️ Radar competitivo — diferencial**": {
      "en": "**🕸️ Competitive radar — differentiator**",
      "es": "**🕸️ Radar competitivo — diferencial**",
      "fr": "**🕸️ Radar concurrentiel — différenciateur**",
      "de": "**🕸️ Wettbewerbsradar — Differenzierung**",
      "zh": "**🕸️ 竞争雷达 — 差异化**",
      "ko": "**🕸️ 경쟁 레이더 — 차별점**",
      "hi": "**🕸️ प्रतिस्पर्धी रडार — विभेदक**",
      "he": "**🕸️ ראדאר תחרותי — בידול**"
    },
    "title=\"Projeto\"": {
      "en": "title=\"Project\"",
      "es": "title=\"Proyecto\"",
      "fr": "title=\"Projet\"",
      "de": "title=\"Projekt\"",
      "zh": "title=\"项目\"",
      "ko": "title=\"프로젝트\"",
      "hi": "title=\"परियोजना\"",
      "he": "title=\"פרויקט\""
    },
    "title=\"Falha\"": {
      "en": "title=\"Failure\"",
      "es": "title=\"Falla\"",
      "fr": "title=\"Défaillance\"",
      "de": "title=\"Fehler\"",
      "zh": "title=\"故障\"",
      "ko": "title=\"실패\"",
      "hi": "title=\"विफलता\"",
      "he": "title=\"כשל\""
    },
    "title=\"Quando\"": {
      "en": "title=\"When\"",
      "es": "title=\"Cuándo\"",
      "fr": "title=\"Quand\"",
      "de": "title=\"Wann\"",
      "zh": "title=\"时间\"",
      "ko": "title=\"시점\"",
      "hi": "title=\"कब\"",
      "he": "title=\"מתי\""
    },
    "title=\"Provedor\"": {
      "en": "title=\"Provider\"",
      "es": "title=\"Proveedor\"",
      "fr": "title=\"Fournisseur\"",
      "de": "title=\"Anbieter\"",
      "zh": "title=\"提供商\"",
      "ko": "title=\"제공자\"",
      "hi": "title=\"प्रदाता\"",
      "he": "title=\"ספק\""
    },
    "title=\"Plano\"": {
      "en": "title=\"Plan\"",
      "es": "title=\"Plan\"",
      "fr": "title=\"Forfait\"",
      "de": "title=\"Plan\"",
      "zh": "title=\"计划\"",
      "ko": "title=\"요금제\"",
      "hi": "title=\"योजना\"",
      "he": "title=\"תוכנית\""
    },
    "title=\"Sumário\"": {
      "en": "title=\"Summary\"",
      "es": "title=\"Resumen\"",
      "fr": "title=\"Résumé\"",
      "de": "title=\"Zusammenf.\"",
      "zh": "title=\"摘要\"",
      "ko": "title=\"요약\"",
      "hi": "title=\"सारांश\"",
      "he": "title=\"תקציר\""
    },
    "title=\"Ações Lean (PDCA)\"": {
      "en": "title=\"Lean Actions (PDCA)\"",
      "es": "title=\"Acciones Lean (PDCA)\"",
      "fr": "title=\"Actions Lean (PDCA)\"",
      "de": "title=\"Lean-Maßnahmen (PDCA)\"",
      "zh": "title=\"精益行动 (PDCA)\"",
      "ko": "title=\"린 액션 (PDCA)\"",
      "hi": "title=\"लीन क्रियाएँ (PDCA)\"",
      "he": "title=\"פעולות Lean (PDCA)\""
    },
    "title=\"Waste dominante\"": {
      "en": "title=\"Dominant waste\"",
      "es": "title=\"Desperdicio dominante\"",
      "fr": "title=\"Gaspillage dominant\"",
      "de": "title=\"Dominante Verschwendung\"",
      "zh": "title=\"主要浪费\"",
      "ko": "title=\"주요 낭비\"",
      "hi": "title=\"प्रमुख अपव्यय\"",
      "he": "title=\"בזבוז דומיננטי\""
    },
    "title=\"Alucinações\"": {
      "en": "title=\"Hallucinations\"",
      "es": "title=\"Alucinaciones\"",
      "fr": "title=\"Hallucinations\"",
      "de": "title=\"Halluzinationen\"",
      "zh": "title=\"幻觉数\"",
      "ko": "title=\"환각 수\"",
      "hi": "title=\"मतिभ्रम\"",
      "he": "title=\"הזיות\""
    },
    "title=\"Prompt que mais alucina (gargalo)\"": {
      "en": "title=\"Most-hallucinating prompt (bottleneck)\"",
      "es": "title=\"Prompt que más alucina (cuello de botella)\"",
      "fr": "title=\"Prompt qui hallucine le plus (goulot)\"",
      "de": "title=\"Am stärksten halluzinierender Prompt (Engpass)\"",
      "zh": "title=\"最易幻觉的提示词（瓶颈）\"",
      "ko": "title=\"환각이 가장 많은 프롬프트(병목)\"",
      "hi": "title=\"सर्वाधिक मतिभ्रम वाला प्रॉम्प्ट (अड़चन)\"",
      "he": "title=\"הפרומפט עם הכי הרבה הזיות (צוואר בקבוק)\""
    },
    "title=\"🏆 Melhor Projeto\"": {
      "en": "title=\"🏆 Best Project\"",
      "es": "title=\"🏆 Mejor Proyecto\"",
      "fr": "title=\"🏆 Meilleur Projet\"",
      "de": "title=\"🏆 Bestes Projekt\"",
      "zh": "title=\"🏆 最佳项目\"",
      "ko": "title=\"🏆 최고 프로젝트\"",
      "hi": "title=\"🏆 सर्वश्रेष्ठ परियोजना\"",
      "he": "title=\"🏆 הפרויקט הטוב ביותר\""
    },
    "title=\"Robusto?\"": {
      "en": "title=\"Robust?\"",
      "es": "title=\"¿Robusto?\"",
      "fr": "title=\"Robuste ?\"",
      "de": "title=\"Robust?\"",
      "zh": "title=\"稳健？\"",
      "ko": "title=\"견고?\"",
      "hi": "title=\"मज़बूत?\"",
      "he": "title=\"חסין?\""
    },
    "title=\"Hora de pico (BRT)\"": {
      "en": "title=\"Peak hour (BRT)\"",
      "es": "title=\"Hora pico (BRT)\"",
      "fr": "title=\"Heure de pointe (BRT)\"",
      "de": "title=\"Spitzenstunde (BRT)\"",
      "zh": "title=\"高峰时段 (BRT)\"",
      "ko": "title=\"피크 시간 (BRT)\"",
      "hi": "title=\"चरम समय (BRT)\"",
      "he": "title=\"שעת שיא (BRT)\""
    },
    "title=\"Interrupções no pico\"": {
      "en": "title=\"Interruptions at peak\"",
      "es": "title=\"Interrupciones en pico\"",
      "fr": "title=\"Interruptions au pic\"",
      "de": "title=\"Unterbrechungen im Peak\"",
      "zh": "title=\"高峰中断数\"",
      "ko": "title=\"피크 중단 수\"",
      "hi": "title=\"चरम पर व्यवधान\"",
      "he": "title=\"הפרעות בשיא\""
    }
  }
}
```
