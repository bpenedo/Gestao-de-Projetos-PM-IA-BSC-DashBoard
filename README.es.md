# 🧭 Gestão de Projetos PM IA BSC DashBoard (Build and Analyze Your Own AI Portfolio Projects)

<p align="center">
  <img src="docs/hero.jpg" alt="Gestión de Proyectos PM IA BSC DashBoard" width="820">
</p>

🌐 [Português](README.md) · [English](README.en.md) · **Español** · [Français](README.fr.md) · [Deutsch](README.de.md) · [中文](README.zh.md) · [한국어](README.ko.md) · [हिन्दी](README.hi.md) · [עברית](README.he.md) · [Svenska](README.sv.md) · [Русский](README.ru.md) · [Suomi](README.fi.md)

![Method](https://img.shields.io/badge/method-Balanced%20Scorecard-1F3A5F)
![AI](https://img.shields.io/badge/AI-LLM%20observability-45a1bf)
![Finance](https://img.shields.io/badge/finance-VAN%20·%20TIR%20·%20TIRM%20·%20IR-46a485)
![Decision](https://img.shields.io/badge/MCDM-DEMATEL%20·%20ELECTRE%20·%20PROMETHEE%20·%20MAUT%20·%20MCDA--C-8E44AD)
![Risk](https://img.shields.io/badge/risk-Monte%20Carlo%2010k%20·%20VaR%20·%20CVaR-DC143C)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-PyO3-orange?logo=rust&logoColor=white)
![Dashboard](https://img.shields.io/badge/dashboard-Evidence-236aa4)
![PDF](https://img.shields.io/badge/pitch%20deck-LaTeX-008080)
![i18n](https://img.shields.io/badge/i18n-12%20idiomas-0E7C86)
![status](https://img.shields.io/badge/status-v1-success)

### 💸 Pagas por IA todos los meses. Pero ¿la IA te está pagando **a ti**?

Cada vez que la tarjeta es cobrada por **ChatGPT, Claude, Copilot, Gemini, Perplexity, DeepSeek, Kimi, Qwen…**,
una pregunta de **millones** queda sin respuesta: **¿dónde está el retorno?** ¿Cuántas horas-persona se
ahorraron de verdad? ¿Cuánto de tu dinero se **evaporó** en alucinación, retrabajo y espera? ¿Qué proyecto de IA
**merece escalar hoy** — y cuál está **desangrando caja** mientras aplaudes la "innovación"?

No tienes un costo de IA. Tienes una **fuga silenciosa** — y estás con los ojos vendados. Porque *"lo que no se
mide no se puede gestionar ni mejorar"* — y el mercado lo mide por ti, y te pasa la cuenta.

**Este framework enciende la luz.** Convierte el **gasto invisible** de tus suscripciones de IA en **retorno
medible, comparable y auditable** — con el rigor del **Balanced Scorecard** (Kaplan & Norton), del **análisis de
inversiones de nivel Wall Street** y de la **decisión multicriterio**. Es la diferencia entre *esperar* y
*saber*. Entre pagar por la IA y **lucrar** con ella.

> *"Lo que no se mide no se puede gestionar ni mejorar."* — Kaplan & Norton

> *"Quien mide con precisión, construye con excelencia."* — Pierre Vernier

> *Cuando ores y estudies, no dejes que [mis palabras] te abandonen. Con cada palabra y expresión que sale de tus labios, ten presente traer una Unificación.* — Aryeh Kaplan

> *La metafísica pura, situándose por esencia por encima y más allá de todas las formas y contingencias, no es ni oriental ni occidental: es universal.* — René Guénon

> *Conocerse a uno mismo es conocer el propio linaje y el propio poder.* — Harvey Spencer Lewis

> *Scientia es Lux Lucis* ∞ Sapere Aude S∴A∴☬ ☿

> 🐺 **Deja de PAGAR por IA a ciegas.** Mientras el mercado se suscribe a la IA por fe — y se vuelve la
> estadística de **Gartner** (≥30% de los proyectos de GenAI abandonados tras el piloto) —, **tú** vas a medir
> cada token, elegir el proyecto ganador y convertir el gasto invisible en **retorno auditable**: VAN · TIR ·
> TIRM · VAE · 70+ KPIs · decisión multicriterio · dashboard C-Level en **12 idiomas**. **La IA ya es tuya.
> Ahora hazla RENTABLE** — gratis, en tu máquina, en **5 minutos**: `./run_all.sh --mock && npm run dev` 🔥

> 📖 **Documentación principal:** **[`foundations/README.md`](foundations/README.md)** ·
> ⚙️ **Setup (usa tus claves):** [`foundations/pipeline/SETUP.md`](foundations/pipeline/SETUP.md) ·
> 📊 **KPIs:** [`foundations/KPIs.md`](foundations/KPIs.md) / [`foundations/KPIs_README.md`](foundations/KPIs_README.md)

---

## 📑 Índice

- [🌅 Por qué esto cambia el juego](#-por-qué-esto-cambia-el-juego)
- [📈 La evidencia (Gartner · IDC · PwC · McKinsey · MIT)](#-la-evidencia-gartner--idc--pwc--mckinsey--mit)
- [💥 El costo de la inacción](#-el-costo-de-la-inacción-haz-la-cuenta-que-nadie-hace)
- [✨ Funcionalidades](#-funcionalidades)
- [📸 Capturas (dashboard anónimo)](#-capturas-dashboard-anónimo)
- [🚀 Inicio rápido](#-inicio-rápido-demo-sin-langfuse)
- [🏗️ Arquitectura](#️-arquitectura)
- [📊 Catálogo de KPIs](#-catálogo-de-kpis-70)
- [💰 Análisis financiero de inversión](#-análisis-financiero-de-inversión)
- [🏆 Decisión multicriterio + Dossier](#-decisión-multicriterio-ahp-topsis-2n--dossier-de-la-joya-de-la-corona)
- [🎲 Monte Carlo — el riesgo que la media esconde](#-monte-carlo--el-riesgo-que-la-media-esconde)
- [🧮 Cinco escuelas de decisión. Un solo veredicto.](#-cinco-escuelas-de-decisión-un-solo-veredicto)
- [🔬 La señal está aguas arriba — y ahí vive el apalancamiento](#-la-señal-está-aguas-arriba--y-ahí-vive-el-apalancamiento)
- [🎓 Fundamentos: qué es Monte Carlo y qué es la Decisión Multicriterio](#-fundamentos-qué-es-monte-carlo-y-qué-es-la-decisión-multicriterio)
- [🌐 12 idiomas](#-12-idiomas)
- [🙋 Objeciones (las preguntas que te estás haciendo ahora)](#-objeciones-las-preguntas-que-te-estás-haciendo-ahora)
- [🧩 Skills incluidas](#-skills-incluidas-build--analyze-your-own)
- [📚 Recursos & referencias](#-recursos--referencias-awesome)
- [🗺️ Roadmap](#️-roadmap)
- [🧰 Setup paso a paso (local, desde cero)](#-setup-paso-a-paso-local-desde-cero)
- [🤝 Contribuir](#-contribuir)
- [📄 Licencia & autoría](#-licencia--autoría)

---

## 🌅 Por qué esto cambia el juego

**Hay dos tipos de personas en la era de la IA.** Las primeras se suscriben a todo, gastan mucho y **rezan** para
que funcione — y engrosan la cruel estadística de los proyectos que mueren en el piloto. Las segundas hacen lo
que Wall Street hace con cualquier activo serio: **miden, comparan, priorizan y reasignan** — y convierten cada
dólar de suscripción en **retorno compuesto**. La única diferencia entre ellas **no es talento ni presupuesto.
Es instrumentación.**

La IA generativa creó una nueva clase de gasto recurrente — **suscripciones y tokens** — y, con ella, el
desperdicio más caro de la década: **el invisible.** Lo que no ves, no lo corriges. Lo que no mides, no lo
escalas. Y lo que no pruebas, el directorio no lo aprueba.

**Este proyecto te mueve de la primera tribu a la segunda.** Instrumenta cada proyecto de IA como un **activo
financiero** y lo mide bajo el **Balanced Scorecard**, el **análisis de inversiones (VAN, TIR, TIRM, VAE, IR,
Payback)** y el **Lean Six Sigma** — y hasta **elige el mejor proyecto de tu portafolio** mediante un modelo
multicriterio (**AHP-TOPSIS 2n**). La factura mensual opaca se vuelve una **tesis de inversión auditable**:
descubres, con números, dónde escalar, dónde recortar, dónde la suscripción se paga en **semanas** — y dónde se
desangra sin cobertura.

Somos **pioneros** de un territorio nuevo — la **frontera entre la inteligencia artificial y la inteligencia financiera de alto valor**. Como exploradores que cartografían tierras aún sin mapa, este framework es la **brújula** (🧭) que
convierte la niebla de las suscripciones en **rutas claras de retorno**: cada token, una milla; cada proyecto,
una expedición hacia el lucro. Donde había costo ciego, nace **oportunidad medible**; donde había una planilla
muerta, florece una **tesis de inversión viva**.

### 🚀 Para Micro-SaaS, SaaS, Startups y Solopreneurs

Hay algo que nadie te contó cuando incrustaste IA en tu producto: **acabas de mover la IA de tu presupuesto de
marketing a tu COGS.** Y un COGS que crece con el uso no es un gasto — es una **hipoteca sobre tu margen
bruto**. Cada usuario nuevo ahora cuesta tokens. Cada reintento por alucinación quema margen dos veces. Y la
cuenta solo aparece a fin de mes, cuando ya no se puede deshacer.

| Eres… | El dolor que nadie mide | Lo que este framework te devuelve |
|---|---|---|
| **Solopreneur** | tú *eres* el equipo; tu hora es el activo más caro que existe | el **tornado** señala la variable que mueve el resultado — o sea, **dónde invertir tu próxima hora** |
| **Micro-SaaS** | el costo de token crece con el uso y se come el margen en silencio | distribución **ajustada a tus tokens reales** + **CVaR**: el mal mes tiene precio *antes* de llegar |
| **SaaS a escala** | cada feature de IA es un proyecto peleando por el mismo roadmap | **cinco métodos** eligen cuál entra — y la **robustez** dice si el 1º puesto sobrevive a un error de 2 puntos en un peso |
| **Startup levantando** | el inversor no compra *"usamos IA"* | compra **VAN, TIR, payback y `P(VAN<0)`** — y el **pitch deck sale listo**, en LaTeX |

**Lo que cambia de verdad.** Tu margen bruto deja de ser una estimación y se vuelve una **distribución con cola
valorada**. Tu runway deja de ser una división simple y gana un **VaR**: *"en 19 de cada 20 escenarios, mi caja
dura al menos N meses."* Y cuando llega el board deck o la due diligence, no abres una planilla que nadie puede
reproducir — abres un número con **semilla fija**, que cualquier socio, inversor o auditor reejecuta y obtiene
**exactamente igual**.

> **Reposicionamiento brutal:** el solopreneur empieza a decidir como un CFO. Y el CFO empieza a decidir a la
> velocidad de un solopreneur.

> **La promesa:** transformar a quien *paga por IA* en quien *lucra con IA* — y a quien *usa IA* en quien
> **pioneramente la domina, la mide y la multiplica**. Con números, no con fe.

---

## 📈 La evidencia (Gartner · IDC · PwC · McKinsey · MIT)

No me creas a mí. **Cree a los institutos que estudian esto desde hace décadas** — y cuyo veredicto es unánime:
**la IA crea un valor inmenso, pero solo lo entrega a quien mide y gobierna.** Quien "usa IA sin dominarla" se
vuelve estadística de abandono; quien instrumenta el retorno **se queda con el premio**.

- 🧭 **Gartner** — previó que **≥ 30% de los proyectos de IA generativa serían abandonados tras la prueba de
  concepto para fines de 2025**, con el **valor de negocio poco claro** como causa central (además de datos
  malos, costos crecientes y controles frágiles). *→ sin medición, el proyecto muere en el piloto.*
- 🔬 **MIT** (informe *"The GenAI Divide / State of AI in Business 2025"*, iniciativa NANDA) — ampliamente
  reportado que la **gran mayoría de los pilotos corporativos de GenAI no genera impacto medible en el P&L**; la
  minoría que entrega valor combina IA con **proceso y medición**. *→ la diferencia es medir, no adoptar.*
- 💵 **IDC** (estudio *"The Business Opportunity of AI"*, patrocinado por Microsoft) — las organizaciones que
  **miden y optimizan** reportaron un retorno del orden de **varios dólares por cada US$ 1** invertido en IA, con
  fuerte dispersión entre líderes y rezagados. *→ el ROI existe — y favorece a quien instrumenta.*
- 🌍 **PwC** (*"Sizing the Prize"*) — estima que la IA podría añadir hasta **~US$ 15,7 billones** a la economía
  global para 2030; pero el premio es para quien **captura** el valor, no para quien solo lo consume. *→ el
  pastel es gigante; la porción es de quien mide.*
- 🏆 **McKinsey** (*"The State of AI"*) y **BCG × MIT Sloan** — un grupo minoritario de **"AI high performers"**
  captura un retorno desproporcionado; el punto de inflexión llega cuando la IA se acopla a **métricas,
  gobernanza y reinversión** donde el retorno está probado. *→ los ganadores miden, priorizan y reasignan.*

> **Es exactamente esa brecha que este framework atraviesa:** te saca del lado que *abandona en el piloto* y te
> pone en el lado que tiene **resultados propiamente dichos y probados** — con BSC, análisis de inversión y
> decisión multicriterio.

> ⚠️ **Nota de honestidad (léela):** las cifras anteriores reflejan titulares reales de estos institutos, pero
> **los informes y porcentajes se actualizan** — confirma los valores exactos y el año en las **fuentes
> primarias** (Gartner Newsroom; IDC/Microsoft *Business Opportunity of AI*; PwC *Sizing the Prize*; McKinsey
> *State of AI*; MIT *State of AI in Business*) antes de citarlas en material oficial. Aquí sirven como
> **fundamentación direccional**, no como garantía numérica.

---

## 💥 El costo de la inacción (haz la cuenta que nadie hace)

Una suscripción **PRO de IA** cuesta entre **US$ 20 y US$ 200 por mes, por asiento**. Multiplica por el número de
personas de tu equipo. Multiplica por 12 meses. Ahora aplica lo que los institutos ya **probaron**: **Gartner**
proyecta **≥ 30% de abandono** y el **MIT** muestra que la **mayoría de los pilotos no retorna**. Una porción
enorme de ese total no es inversión — es **sangría pura**.

> **Ejemplo directo (cámbialo por tus números):** 10 asientos × US$ 30/mes × 12 = **US$ 3.600/año**. Si ~30% se
> vuelve desperdicio invisible, son **~US$ 1.080/año evaporándose** — de UN equipo pequeño, en UN año. Con tu
> número real, el susto es mayor.

Y aquí está la parte que duele: **este costo es compuesto y no espera.** Cada mes sin medir es un mes de fuga que
**no vuelve** — mientras el competidor que instrumentó ya está **reasignando capital a lo que rinde**. La ventaja
de pionero se construye temprano: **quien mide primero, escala primero.**

El momento de menor costo para empezar fue ayer. El segundo mejor es **ahora** — y cuesta **US$ 0** y **5
minutos**. La pregunta no es *"¿puedo permitirme medir?"*. Es ***"¿cuánto tiempo más puedo permitirme NO
medir?"***

---

## ✨ Funcionalidades

- **📊 KPIs (4 perspectivas BSC) + economía de APIs:** madurez, capital humano, financiero y eficiencia de tokens
  — `IEET`, `IOLI`, `ITR`, `IITA`, `PEUC`, `ICCA`, `IDLS`, `IBMT` — más **EVM** (CPI/SPI/EAC).
- **🪙 Conceptos de frontera:** **VRT/kTR** (unidad de recuperación de costo tokenizable — *"el m² de Gitman"*) y
  **PSR** (Project Score 0–5 ⭐) para rankear la salud de cada proyecto.
- **🔬 Diagnóstico operativo:** **VRT en 5 bloques**, **HCI** (hora crítica de interrupción), **desperdicios Lean
  Six Sigma** (tokens ponderados) y **RCA de alucinación por taxonomía de prompt** (cuello de botella por
  proyecto + intersección).
- **💰 Financiero completo:** **VAN, TIR, TIRM (TIR Modificada), VAE (Valor Anual Equivalente), IR (índice de
  rentabilidad), Payback** simple y descontado, **dolarización** y comparación con **SELIC** y los **intereses de
  EE. UU.**
- **🏆 Decisión multicriterio:** **AHP-TOPSIS 2n** (doble normalización) elige el **mejor proyecto** del
  portafolio con **prueba de robustez** — y genera un **dossier administrativo** (SWOT, PESTELC, 5W4H, Pareto,
  GUT, Radar).
- **🗺️ Visual C-Level:** **mapa 5D interactivo**, donas con profundidad, cuadrante de sostenibilidad, tendencias y
  **pitch decks** en LaTeX de los proyectos elegibles.
- **⚙️ Pipeline real:** **Langfuse → SQLite → Evidence**, con sync **asíncrono concurrente** y clasificación
  acelerada en **Rust (PyO3)**.
- **💳 FinOps de IA:** catálogo de **planes de suscripción** (OpenAI, Anthropic, Google, Perplexity, xAI, Mistral,
  DeepSeek, Kimi, Qwen…) con **cambio + IOF** y base de prorrateo (burn rate).
- **🌐 12 idiomas** en el dashboard **y en las imágenes de los gráficos** (incl. Devanagari, Hebreo y CJK).
<!-- eixo-execucao -->
- **📅 Cronograma Monte Carlo (PERT) + Gantt:** el mismo motor de Monte Carlo apuntado a **duraciones de tareas** — distribución de la fecha de término, **P80** (el compromiso que recomienda el PMI), `P(a tiempo)` y **ruta crítica** con **índice de criticidad** (en qué % de las 10.000 simulaciones cada tarea es crítica — lo que el CPM determinista esconde).
- **📐 Earned Value Management + Earned Schedule:** **SPI · CPI · EAC · ETC · VAC · TCPI** y la **curva S** (PV/EV/AC). Une **coste + plazo + alcance** en un solo cuadro. El **SPI(t)** corrige el defecto conocido del SPI, que converge a 1 al final incluso con el proyecto atrasado.
- **⚙️ Salud de ejecución de la IA en el tiempo:** latencia **p50/p95/p99** con **SLO**, **token budget burndown**, **regresión de calidad** (regla tipo SPC) y **drift del modelo** por **Kolmogorov-Smirnov** — todo de los logs **reales** de Langfuse.
- **🚨 Registro de riesgo + matriz Probabilidad × Impacto:** el riesgo *cualitativo* que exige el PMO, con dueño, disparador y mitigación. Las probabilidades están **ancladas en señales reales** (violación de SLO, CPI, drift), no son suposiciones.
- **🌊 Métricas de flujo (Kanban):** **CFD**, **cycle time P50/P85** (previsión por percentil, no por corazonada), **throughput** y **WIP**.

---

## 📸 Capturas (dashboard anónimo)

> Demostración 100% anónima (proyectos mostrados como *Project A…J*). Los datos/nombres reales nunca acompañan el paquete.

**🌐 Mapa 5D del portafolio** — 5 dimensiones por proyecto: **X**=tokens · **Y**=PEUC (calidad) · **Z**=PSR
(salud) · **tamaño**=Burn Rate · **color**=ICCA (sostenibilidad). *¿Dónde escalar? Derecha/fondo, alto y verde.
¿Dónde recortar? Grande y rojo.*

![Mapa 5D del portafolio de proyectos de IA](docs/screenshots/5d-portfolio-map.png)

**🏆 Dossier de la "Joya de la Corona"** (proyecto elegido por AHP-TOPSIS) — generado por pipeline Python
concurrente:

| SWOT | Radar competitivo |
|---|---|
| ![SWOT](docs/screenshots/swot.png) | ![Radar competitivo](docs/screenshots/radar.png) |

| PESTELC (macroentorno) | Matriz GUT (priorización) |
|---|---|
| ![PESTELC](docs/screenshots/pestel.png) | ![GUT](docs/screenshots/gut.png) |

| 5W4H (plan de acción) | Pareto de fallas (80/20) |
|---|---|
| ![5W4H](docs/screenshots/5w4h.png) | ![Pareto](docs/screenshots/pareto.png) |

### 📅 Eje de ejecución — cronograma, valor ganado, salud de la IA, riesgo y flujo

**Gantt con ruta crítica** — las barras rojas son la ruta crítica; el **%** de cada tarea es el *índice de criticidad*: en qué porcentaje de las 10.000 simulaciones esa tarea determinó el plazo.

![Gantt con ruta crítica — las barras rojas son la ruta crítica; el % de](docs/screenshots/cronograma-gantt.png)

**Riesgo de plazo** — la distribución de la fecha de término, con la *deadline*, el **P50** y el **P80** marcados. Comprométete con el P80, no con la estimación determinista (optimista por el sesgo de convergencia).

![Riesgo de plazo — la distribución de la fecha de término, con la deadl](docs/screenshots/cronograma-risco-prazo.png)

**Curva S del EVM** — PV (planificado) · EV (ganado) · AC (coste real). EV por debajo de PV = atraso; AC por encima de EV = sobrecoste.

![Curva S del EVM — PV (planificado) · EV (ganado) · AC (coste real). EV](docs/screenshots/evm-curva-s.png)

**Latencia bajo SLO** — p50/p95/p99 por día, de los logs reales. Si cruza la línea, el servicio se degradó.

![Latencia bajo SLO — p50/p95/p99 por día, de los logs reales. Si cruza ](docs/screenshots/exec-latencia-slo.png)

**Matriz de riesgo P × I** — burbuja = exposición (P×I). Probabilidad anclada en las señales reales del proyecto.

![Matriz de riesgo P × I — burbuja = exposición (P×I). Probabilidad ancl](docs/screenshots/risco-matriz-pi.png)

**Cumulative Flow Diagram** — bandas paralelas = flujo sano; una banda que engorda = cuello de botella / WIP atascado.

![Cumulative Flow Diagram — bandas paralelas = flujo sano; una banda que](docs/screenshots/fluxo-cfd.png)

---

## 🚀 Inicio rápido (demo, sin Langfuse)

**Cero riesgo. Cero costo. 5 minutos.** Ejecútalo en tu máquina y ve el dashboard completo con datos anónimos:

```bash
cd foundations/pipeline
pip install -r requirements.txt
cd ../evidence && npm install && cd ../pipeline
./run_all.sh --mock          # datos anónimos (Project A..J) -> KPIs -> VAN/TIRM/VAE -> 5D -> pitch decks -> dashboard
cd ../evidence && npm run dev # http://localhost:3000
```

Para **datos reales**, completa `foundations/pipeline/.env` con **tus propias** claves de Langfuse (ver
[`SETUP.md`](foundations/pipeline/SETUP.md)) y ejecuta `./run_all.sh`. Cada usuario usa su **propia cuenta** —
ninguna clave del autor acompaña el paquete.

---

## 🏗️ Arquitectura

```
   Tus apps de IA               Observabilidad          Analytics-as-Code           Tú
 (ChatGPT, Claude, API…)   ┌──────────────┐   ┌──────────────────┐   ┌──────────────────────┐
        │ traces           │   Langfuse   │   │  SQLite (schema  │   │  Evidence (BI as     │
        └─────────────────▶│  (SDK v4)    │──▶│  + queries KPI)  │──▶│  Code) · 12 idiomas  │
                           └──────────────┘   └──────────────────┘   └──────────┬───────────┘
   sync asíncrono concurrente        clasificación en Rust (PyO3)              │
                                                                    ┌───────────┴───────────┐
                                                                    │ AHP-TOPSIS · Dossier  │
                                                                    │ 5D · Pitch decks (TeX)│
                                                                    └───────────────────────┘
```

**Stack:** Python 3.13 · SQLite/DuckDB · Evidence.dev (SvelteKit) · Rust + PyO3 + maturin · matplotlib ·
tectonic (LaTeX) · fuentes Noto/WenQuanYi para i18n de imagen.

---

## 📊 Catálogo de KPIs (70+)

Muestra (catálogo completo en [`foundations/KPIs_Lean6s_BSC.md`](foundations/KPIs_Lean6s_BSC.md)):

| Sigla | Nombre | Qué responde |
|---|---|---|
| **PSR** | Project Score Rating (0–5) | Salud general del proyecto de IA |
| **PEUC** | % de Entrega Útil por Consumo | Cuánto del gasto se volvió entrega útil |
| **IITA** | Índice de Incidencia de Tokens Alucinados | % de alucinación/retrabajo |
| **IDLS** | Índice de Desperdicio Lean | Muda (tokens ponderados por severidad) |
| **VRT/kTR** | Valor de Recuperación Tokenizable | "m² de Gitman" — costo por 1k tokens |
| **ICCA** | Índice de Cobertura de Costo por Suscripción | ¿Cubre el costo? (>3× saludable) |
| **CPP** | Costo por Punto de Progreso | Indicador maestro (cuanto menor, mejor) |

---

## 💰 Análisis financiero de inversión

Cada proyecto se vuelve una **tesis de inversión**: a partir de tu flujo de caja (CSV), el framework calcula
**VAN**, **TIR**, **TIRM (reinvierte al costo del proyecto)**, **VAE (anualidad equivalente del VAN)**, **IR
(índice de rentabilidad)** y **Payback** simple/descontado — **dolarizando** el flujo y comparando con la
**SELIC** y los **intereses de EE. UU.** Genera un **pitch deck** en LaTeX para todo proyecto con **VAN > 0 e IR
> 1** en BRL **y** USD. El objetivo es brutalmente práctico: **descubrir si tu suscripción de IA se paga — y en
cuánto tiempo.**

---

## 🏆 Decisión multicriterio (AHP-TOPSIS 2n) + Dossier de la Joya de la Corona

Cuando hay varios proyectos, ¿cuál escalar primero? El modelo **AHP-TOPSIS 2n** pondera los indicadores como
criterios (pesos por **AHP** con razón de consistencia **CR ≤ 0,10**) y rankea por **TOPSIS** en **dos
normalizaciones** (vectorial + min-max), reportando la **robustez** (concordancia entre normalizaciones). El
ganador — la **"Joya de la Corona"** — recibe un **dossier administrativo** completo (SWOT · PESTELC · 5W4H ·
Pareto · GUT · Radar) generado desde cero por código, con un **Bottom-Line** ejecutivo e **insights C-Level**
honestos. **No presentas una planilla. Presentas un veredicto.**

---

## 🎲 Monte Carlo — el riesgo que la media esconde

Un VAN positivo **en promedio** no protege a nadie. El promedio es la mentira más cómoda de las finanzas: describe
un escenario que quizá nunca ocurra. Quien decide tu destino es la **cola** — el mal día.

Este framework simula **10.000 futuros** para cada proyecto: cada flujo de caja se vuelve una **variable aleatoria** y todo el portafolio se recalcula iteración a
iteración. Al final no tienes un número — tienes **la distribución entera de tu dinero**:

- **`P(VAN < 0)`** — la probabilidad real de pérdida. El número que nadie te muestra.
- **VaR 5%** — el peor escenario plausible: *"en 19 de cada 20 futuros, gano al menos esto."*
- **CVaR 5%** — cuando el desastre ocurre, cuánto cuesta en promedio.
- **Tornado de sensibilidad** — regresión múltiple y correlación de Pearson: qué variable realmente mueve tu VAN.
- **20 distribuciones** de entrada, **matriz de correlación** validada (Iman-Conover, que preserva las marginales
  exactas) y **percentiles del 1% al 99%**, con histograma de 100 clases.

Semilla fija: ejecutarlo de nuevo da **exactamente** el mismo resultado. Auditable — no "mágico".

> **El giro:** dejas de elegir el proyecto de mayor VAN y pasas a elegir **el que sobrevive al mal escenario**.
> Eso es gestión de riesgo — lo que separa al inversor del apostador.

![Histograma de Monte Carlo do VPL — 10.000 iterações, 100 classes](docs/screenshots/mc-histograma.png)

| Distribución acumulada del VAN | Tornado de sensibilidad |
|---|---|
| ![Distribución acumulada del VAN](docs/screenshots/mc-acumulado.png) | ![Tornado de sensibilidad](docs/screenshots/mc-tornado.png) |

---

## 🧮 Cinco escuelas de decisión. Un solo veredicto.

Un método puede equivocarse. Cinco métodos de acuerdo, no.

Siguiendo la arquitectura de **John (2025)** — *Integration of DEMATEL with Other MCDM Methods* —, **DEMATEL** mapea la
estructura causal entre los criterios y separa **causas** (palancas donde actuar) de **efectos** (termómetros de lo ya
hecho). De esos lazos de influencia nacen los **pesos**: no arbitrados, sino **derivados de la estructura del problema**.
Alimentan a cuatro escuelas rivales:

| Método | Escuela | Qué pregunta |
|---|---|---|
| **ELECTRE I** | Sobreclasificación | "¿Quién domina a quién — y quién sobrevive sin ser dominado?" |
| **PROMETHEE II** | Sobreclasificación | "¿Cuál es el flujo neto de preferencia de cada proyecto?" |
| **MAUT** | Utilidad | "¿Cuál maximiza la utilidad de un decisor averso al riesgo?" |
| **MCDA-C** | Constructivista | "¿Quién está por encima del nivel *Bueno* — y quién por debajo del *Neutro*?" |
| **AHP-TOPSIS 2n** | Distancia al ideal | "¿Quién está más cerca de la solución ideal en ambas normalizaciones?" |

El ganador surge del **consenso de Borda** entre los cinco, ya **ajustado al riesgo** del Monte Carlo. Y cuando los
métodos **discrepan**, el dashboard muestra la discrepancia — porque eso es información: la elección es sensible a la
escuela de decisión y merece el ojo del decisor.

| DEMATEL — causas × efectos | Posición por método |
|---|---|
| ![DEMATEL — causas × efectos](docs/screenshots/dematel.png) | ![Posición por método](docs/screenshots/mcdm-metodos.png) |

### 💼 Qué cambia en tu día — del autónomo a la corporación

No importa si pagas **US$ 20 en un plan PRO** o **US$ 200 mil en contratos enterprise**: la matemática del desperdicio
es la misma — solo cambia el número de ceros.

| | **PyME / autónomo** | **Gran empresa** |
|---|---|---|
| **El dolor real** | 3 suscripciones, cero visibilidad, caja corta | 40 pilotos de IA, ninguno con P&L atribuido |
| **Monte Carlo entrega** | *"este proyecto tiene 12% de probabilidad de perder dinero, y el mes malo cuesta US$ 3,4k"* | VaR/CVaR por unidad de negocio: riesgo agregado y auditable, no anécdota |
| **MCDM entrega** | cuál de los 3 proyectos escalar **primero**, con el dinero que existe | cuál de los 40 pilotos se vuelve producto — defendible en comité, con el método explícito |
| **La ganancia al día siguiente** | cancelar la suscripción que no se paga, esta misma semana | reasignar presupuesto por **evidencia**, no por política interna |

**En la práctica:** el **tornado** señala la variable que mueve el resultado — es decir, **dónde invertir tu próxima
hora de trabajo**. El **DEMATEL** revela que reducir la alucinación (IITA) es **causa**, no síntoma: actúas allí y VAN,
TIR y riesgo mejoran *juntos*. Es la gestión de IA dejando de ser opinión y volviéndose **ingeniería**.


---

## 🔬 La señal está aguas arriba — y ahí vive el apalancamiento

Lo descubrí midiendo el propio framework: el tornado de sensibilidad del VAN devolvía **exactamente**
`1,0 · 0,9091 · 0,8264 · 0,7513…` — los factores de descuento `1/(1+i)ᵗ`. Como el VAN es **lineal** en los flujos de
caja, simular solo los flujos no informa nada más allá de la tasa. **La señal estocástica real está aguas arriba: en
los tokens.**

### 1️⃣ Deja de arbitrar la distribución. Ajústala a tus datos.

Once distribuciones candidatas se ajustan por **máxima verosimilitud** a tu serie real de consumo de tokens
(`logs_langfuse`). Gana la de **menor AIC** — que penaliza cada parámetro extra y evita el sobreajuste — y la prueba
de **Kolmogorov-Smirnov** mide la bondad del ajuste. Es el clásico *ajuste de distribuciones a datos*, y es lo que
revela la **cola pesada** del consumo: algunos prompts cuestan 10× lo típico, y esa cola es la que revienta el
presupuesto — invisible para quien usa el promedio.

**Y cuando el ajuste es malo, el framework grita.** Si el p-valor del KS cae por debajo de 0,05, la pantalla avisa
`ADHERENCIA DÉBIL` en rojo, en lugar de fingir precisión. Un número honesto vale más que uno bonito.

![Ajuste de distribuciones a los tokens reales — 11 candidatas, selección por AIC, bondad de ajuste por Kolmogorov-Smirnov](docs/screenshots/ajuste-distribuicoes.png)

### 2️⃣ ¿Tu ranking sobrevive a un error de 2 puntos en un peso?

Todo método multicriterio devuelve un ganador con **confianza implícita del 100%**. Pero los pesos son estimaciones,
no verdades reveladas. Si dos puntos porcentuales en el peso del IITA intercambian el 1º y el 2º lugar, el "ganador"
es un artefacto de la calibración.

Así que perturbamos los pesos del DEMATEL con una **Dirichlet** — `w' ~ Dir(κ·w)`, que vive exactamente en el
símplex y preserva `E[w'] = w`, perturbando **sin sesgar** — y reranqueamos **2.000 veces**. El veredicto cambia de
naturaleza:

> *"Project C es el mejor"* ⟶ **"Project C gana en el 99,9% de los universos de preferencia plausibles"**

Es un **intervalo de confianza sobre la decisión misma**. Y expone lo que el consenso escondía: en la pantalla de
abajo, **PROMETHEE II elige al líder en apenas el 25,4% de los universos**. Cuatro escuelas concuerdan; una disiente
de frente. Eso no es ruido — es el aviso de que la elección depende de si prefieres *sobreclasificación* a
*utilidad*. Ningún ranking solo te diría eso.

![Robustez del ranking por perturbación de Dirichlet — probabilidad de victoria y divergencia entre escuelas](docs/screenshots/robustez-dirichlet.png)

### ⚡ El apalancamiento concreto

| Recurso | Antes | Después |
|---|---|---|
| **Tiempo** | semanas discutiendo qué proyecto escalar | el veredicto llega con probabilidad — la discusión termina en una reunión |
| **Procesamiento** | 10.000 iteraciones × 10 proyectos, vectorizado en NumPy | segundos, en tu máquina, sin nube y sin costo |
| **Capital** | presupuesto asignado por convicción | asignado por `P(victoria)` y `VaR` — con el peor caso ya valorado |
| **Reputación** | *"creo que este es el mejor"* | *"gana en el 99,9% de los escenarios; y este es el método que disiente, y por qué"* |
| **Auditoría** | una planilla imposible de reproducir | semilla fija: cualquiera la reejecuta y obtiene **exactamente** el mismo número |

### 💼 Del plan de US$ 20 al contrato de US$ 200 mil

**Si eres autónomo o PyME:** la distribución ajustada te dice **cuánto costará el mal mes de tokens** antes de que
llegue — y la robustez te dice si de verdad conviene mover el esfuerzo al otro proyecto, o si ambos están empatados
dentro del margen de error. Dejas de optimizar a ciegas con la caja corta.

**Si eres una gran empresa:** `P(victoria)` es la pieza que falta en el comité de inversión. Convierte *"el equipo A
defiende el proyecto X"* en **"el proyecto X gana bajo el 99,9% de las calibraciones de peso defendibles, y la única
escuela que disiente es la de sobreclasificación, por el criterio Y"**. El debate político se vuelve **debate
técnico** — y el CFO obtiene un número que sobrevive a la auditoría.

> **El giro final:** el framework deja de medir el riesgo del **dinero** y pasa a medir el riesgo de la **decisión
> misma**. Muy pocos lugares en el mundo hacen esto.

---

## 🎓 Fundamentos: qué es Monte Carlo y qué es la Decisión Multicriterio

### 🎲 Simulación Matemática de Monte Carlo

#### 📖 El concepto

Monte Carlo es un método numérico que responde preguntas sobre sistemas inciertos **mediante muestreo aleatorio**. La
idea invierte el instinto del matemático: en vez de deducir la respuesta en **forma cerrada** — resolver la integral, la
combinatoria, la ecuación diferencial —, construyes un **modelo**, sorteas miles de realizaciones de las variables
inciertas y simplemente **cuentas lo que pasó**. Lo que se obtiene al final no es un número: es la **distribución de
probabilidad del resultado**.

Dos leyes lo sostienen. La **Ley de los Grandes Números** garantiza que el promedio de las simulaciones converge al valor
verdadero. El **Teorema Central del Límite** informa a qué velocidad: el error estándar cae con `1/√N`. La consecuencia
es honesta y un poco cruel — **para duplicar la precisión hay que cuadruplicar las iteraciones**. Monte Carlo no es
rápido. Su virtud es otra: el error **no depende de la dimensión del problema**. Los métodos deterministas de cuadratura
sufren la *maldición de la dimensionalidad* y colapsan con decenas de variables; Monte Carlo no. Gana exactamente donde
la matemática analítica muere.

#### 📖 Dónde y cuándo surgió

**Los Álamos, Nuevo México, 1946.** El matemático polaco **Stanisław Ulam** convalecía de una encefalitis y pasaba los
días jugando solitario. Se preguntó cuál sería la probabilidad de ganar una partida. Intentó la combinatoria y desistió:
era intratable. Entonces se le ocurrió algo tan simple que parecía trampa — **jugar cien partidas, contar cuántas gana y
dividir**. Comprendió en el acto que aquello no era un truco de naipes: era un **método general de integración** para
problemas que nadie sabía resolver.

Llevó la idea a **John von Neumann**, quien vio de inmediato su aplicación al problema que los consumía en el Proyecto
Manhattan: la **difusión de neutrones** en material fisible. Simular la trayectoria aleatoria de miles de neutrones —
dispersión, absorción, fisión — era viable; resolver la ecuación de transporte no lo era. **Nicholas Metropolis** propuso
el nombre **"Monte Carlo"**, en referencia al casino de Mónaco donde un tío de Ulam solía pedir dinero prestado para
apostar. El **ENIAC** hizo posibles los primeros cálculos, y en **1949** Metropolis y Ulam publicaron *"The Monte Carlo
Method"* en el *Journal of the American Statistical Association*.

El método nació, literalmente, del encuentro entre un **juego de cartas** y la **bomba atómica**. Pocas ideas científicas
tienen una partida de nacimiento tan desconcertante.

#### 📖 La metodología, en cinco pasos

1. **Modelar.** Escribe la salida como función de las entradas: `y = f(x₁, …, xₙ)`.
2. **Asignar distribuciones.** Cada entrada incierta recibe una distribución. Si hay **datos históricos**, se *ajusta* a
   ellos; si no, se arbitra — y eso debe **declararse**.
3. **Muestrear.** Sortea `N` escenarios. Si las variables están **correlacionadas**, el muestreo debe respetar esa
   estructura: sortear de forma independiente donde hay dependencia real es el error más común del método.
4. **Propagar.** Calcula `f` en cada escenario. Aquí la incertidumbre de las entradas **se transforma** en la
   incertidumbre de la salida, sin ninguna aproximación lineal.
5. **Analizar.** Estudia la distribución: media y desviación, **percentiles**, probabilidad de eventos (`P(y < 0)`), la
   **cola** (VaR, CVaR) y la **sensibilidad** (qué `xᵢ` mueve `y`).

#### 📖 Usos y aplicaciones en el mundo

- **Finanzas:** valoración de opciones exóticas (donde no hay forma cerrada), **VaR** y **CVaR** de carteras, pruebas de
  estrés regulatorias (Basilea), riesgo de crédito.
- **Ingeniería:** confiabilidad estructural, tolerancias de fabricación, análisis de fallas en sistemas complejos.
- **Gestión de proyectos:** riesgo de plazo y costo (la evolución probabilística del PERT), curvas-S de conclusión.
- **Física y química:** transporte de partículas, blindaje de radiación, mecánica estadística.
- **Operaciones y cadenas de suministro:** colas, inventarios, capacidad bajo demanda incierta.
- **Epidemiología:** propagación de enfermedades y evaluación de políticas bajo incertidumbre.
- **Dentro de la propia IA:** **MCMC** (inferencia bayesiana), **MCTS** — la búsqueda en árbol que llevó a AlphaGo a
  vencer a Lee Sedol — y el *Monte Carlo dropout* para estimar incertidumbre en redes neuronales.

#### 🔒 Metodología, uso y aplicación EXCLUSIVOS en este proyecto

Aquí Monte Carlo no es adorno académico: es el **motor de riesgo** del portafolio.

- **Las entradas.** Cada flujo de caja periódico se vuelve una variable **Triangular** (`mín`, `moda`, `máx`), con moda en
  el valor determinista y colas a ±30%. El **consumo de tokens** — la única variable verdaderamente de cola pesada — **no
  se arbitra**: once distribuciones candidatas se **ajustan por máxima verosimilitud** a tu serie real de
  `logs_langfuse`, gana la de **menor AIC**, y la bondad del ajuste se mide con **Kolmogorov-Smirnov**. Si el p-valor cae
  por debajo de 0,05, la pantalla estampa `ADHERENCIA DÉBIL` en rojo en lugar de fingir precisión.
- **La correlación.** Cuando los flujos son dependientes, el muestreo usa **Iman-Conover**, que impone la correlación de
  rangos **preservando exactamente las distribuciones marginales**. La matriz se valida antes: simétrica, diagonal 1,
  definida positiva.
- **La propagación.** **10.000 iteraciones** por proyecto, con **semilla fija (42)**: ejecutarlo de nuevo devuelve
  exactamente el mismo número. No es un detalle — es lo que vuelve el resultado **auditable** por un socio, un inversor o
  un auditor.
- **Las salidas.** No solo el VAN: simulamos **VAN, TIR, TIRM, VAE, IR** y el **costo de tokens**, cada uno con las diez
  estadísticas descriptivas clásicas (asimetría y curtosis en las definiciones de Excel), **percentiles del 1% al 99%** e
  **histograma de 100 clases**.
- **El riesgo que importa.** `P(VAN < 0)` es la probabilidad real de pérdida. El **VaR 5%** es el peor escenario plausible
  — *"en 19 de cada 20 futuros gano al menos esto"*. El **CVaR 5%** responde lo que nadie pregunta: cuando el desastre
  ocurre, **cuánto cuesta en promedio**.
- **La sensibilidad.** El **tornado** se calcula en las dos formas clásicas: los **betas de una regresión múltiple** (el
  efecto de +1 unidad en una entrada sobre el VAN) y la **correlación de Pearson** (cuánto la incertidumbre de esa entrada
  dicta la del VAN). Son lecturas complementarias; el dashboard muestra ambas.
- **Un descubrimiento del propio framework.** Al medirse a sí mismo, el tornado devolvió betas **exactamente iguales a los
  factores de descuento** `1/(1+i)ᵗ` — porque el VAN es *lineal* en los flujos. Simular solo los flujos, por tanto, no
  informa nada más allá de la tasa. **La señal estocástica real está aguas arriba, en los tokens.** Esa constatación
  motivó el ajuste de distribuciones a los datos reales.
- **El riesgo alimenta la decisión.** Dos salidas del Monte Carlo entran como **criterios** en el modelo multicriterio:
  `P(VAN<0)` como criterio de **costo** y el **VaR 5%** como criterio de **beneficio**. La elección final nace ya
  **ajustada al riesgo**, y no solo al valor esperado.


**Qué es.** Un método que responde preguntas difíciles **sorteando**. En vez de resolver en forma cerrada la
matemática de un sistema incierto — a menudo imposible —, asignas **distribuciones de probabilidad** a las
variables de entrada, sorteas miles de escenarios, calculas el resultado en cada uno y observas la **distribución
entera** de las salidas. La Ley de los Grandes Números garantiza la convergencia; el error cae con `1/√N`, es
decir, **cuadruplicar las iteraciones reduce el error a la mitad**.

**Cómo surgió.** Los Álamos, 1946. **Stanisław Ulam**, convaleciente de una enfermedad, jugaba solitario y se
preguntó cuál sería la probabilidad de ganar. Se dio cuenta de que resolver la combinatoria era brutal — pero
**simular** cientos de partidas y simplemente contar era trivial. Llevó la idea a **John von Neumann**, y ambos la
aplicaron al problema que los ocupaba en el Proyecto Manhattan: la **difusión de neutrones** en material fisible.
**Nicholas Metropolis** bautizó el método como "Monte Carlo", en referencia al casino de Mónaco donde un tío de
Ulam solía apostar. El **ENIAC** hizo viables los primeros cálculos. El método nació, literalmente, del encuentro
entre un juego de cartas y la bomba atómica.

**Dónde se usa hoy.** Valoración de opciones y cálculo de **VaR** en finanzas; confiabilidad estructural en
ingeniería; riesgo de plazo y costo en gestión de proyectos; física de partículas; cadenas de suministro;
epidemiología. Y dentro de la propia IA: **MCMC** (inferencia bayesiana) y **MCTS** — la búsqueda en árbol que
llevó a AlphaGo a vencer a Lee Sedol.

**Cómo nos sirve aquí.** Cada flujo de caja de tu proyecto se vuelve una variable aleatoria, y el consumo de tokens
recibe la distribución **ajustada a tus datos reales**. Corremos 10.000 escenarios y, al final, no tienes un VAN —
tienes la **distribución de tu dinero**: `P(VAN < 0)` (la probabilidad real de pérdida), **VaR 5%** (el peor
escenario plausible), **CVaR 5%** (cuánto cuesta cuando el desastre ocurre) y el **tornado** (qué variable mueve de
verdad el resultado). El promedio miente; la cola decide.

### 🧮 Análisis de Decisión Multicriterio (MCDA)

#### 📖 El concepto y para qué sirve

Elegir entre proyectos es difícil por dos razones que ninguna planilla resuelve. Primero, los criterios **entran en
conflicto**: el proyecto de mayor VAN suele ser el de mayor riesgo. Segundo, son **inconmensurables**: no existe operación
aritmética honesta que sume pesos con porcentaje de alucinación y horas de retrabajo.

El MCDA (*Multi-Criteria Decision Analysis*) es el campo — nacido en los años 1960-70, en la frontera entre la
investigación operativa y la teoría de la decisión — que enfrenta exactamente eso. **No promete la respuesta correcta.**
Promete algo más útil: volver la elección **explícita, auditable y defendible**.

Su tesis fundadora es incómoda y liberadora a la vez: **no existe el "mejor" en el vacío.** Existe un mejor *dado un
sistema de preferencias que alguien hizo explícito*. Todo decisor ya opera con un sistema de preferencias — la diferencia
es que, sin MCDA, es **implícito, inconsistente y no auditable**. Cambiar la opinión tácita por un modelo explícito: ahí
está toda la ganancia.

#### 📖 Usos y aplicaciones en el mundo

Selección de proveedores y priorización de portafolio; elección de tecnologías de energía (solar × eólica × biomasa);
localización de plantas, hospitales y vertederos; evaluación de impacto ambiental; políticas públicas y asignación
presupuestaria; selección de personal; priorización de mantenimiento; y — cada vez más — **evaluación tecno-económica** de
tecnologías emergentes, que es exactamente el caso de un portafolio de proyectos de IA.

#### 📖 Las tres escuelas de decisión

- **Escuela americana (valor y utilidad).** Agrega todo en un **único número**. Asume que una nota mala en un criterio
  puede ser **compensada** por notas óptimas en otros. Simple, poderosa — y a veces peligrosa. `AHP`, `MAUT`.
- **Escuela europea (sobreclasificación).** Fundada por **Bernard Roy**. Acepta que dos alternativas puedan ser
  **incomparables** y admite el **veto**: un desempeño catastrófico en un criterio **no se compra** con excelencia en los
  demás. Modela la vacilación real del decisor mediante **umbrales**. `ELECTRE`, `PROMETHEE`.
- **Escuela constructivista.** El modelo no se *descubre*, se **construye junto con el decisor**, mediante la
  estructuración del problema y escalas ancladas en niveles de referencia. `MCDA-C`.

#### 📖 1. DEMATEL — *Decision-Making Trial and Evaluation Laboratory*

**Qué es.** Creado por **Gabus & Fontela** en el **Battelle Memorial Institute** (Ginebra, 1972-73) para estudiar problemas
mundiales complejos y enmarañados. **No rankea alternativas**: mapea la **estructura causal entre los criterios**.

**Cómo funciona.** Expertos completan una **matriz de relación directa** `Z` (cuánto el criterio *i* influye en el *j*, de
0 a 4). Se normaliza por `s = max(mayor suma de fila, mayor suma de columna)` y se obtiene la **matriz de relación total**
`T = X(I − X)⁻¹`, que suma la influencia directa **y todas las indirectas**, por cualquier camino. De ahí salen `R` (sumas
de filas) y `C` (sumas de columnas): **`R+C` es la prominencia** (importancia en el sistema) y **`R−C` es la relación**
(positivo = **causa**; negativo = **efecto**).

**Uso general.** Cadenas de suministro sostenibles, barreras a la adopción de tecnología, análisis de riesgos sistémicos.

**🔒 En este proyecto.** El DEMATEL responde la pregunta que **antecede** al ranking: *"¿dónde debo actuar?"*. Revela que
**IITA (alucinación), PSR (salud) e IDLS (desperdicio Lean) son CAUSAS**, mientras que **VAN, TIR, IR y las métricas de
riesgo son EFECTOS**. Es contraintuitivo y liberador: perseguir el VAN no sirve — es un **termómetro**. Actúa sobre la
alucinación y VAN, TIR y riesgo mejoran *juntos*. Además, los **pesos** de los criterios no se arbitran: se **derivan de la
estructura de influencia**, vía `wᵢ ∝ √((R+C)ᵢ² + (R−C)ᵢ²)`. Esos pesos alimentan los **otros cinco métodos** — el patrón
de integración descrito por John (2025).

#### 📖 2. AHP-TOPSIS 2n — *Analytic Hierarchy Process* + *Technique for Order Preference by Similarity to Ideal Solution*

**Qué es.** **Saaty (1977)** propuso el AHP: derivar pesos de **comparaciones par a par** entre criterios, con una **prueba
de consistencia** que delata juicios contradictorios (`CR ≤ 0,10`). **Hwang & Yoon (1981)** propusieron el TOPSIS: la mejor
alternativa es la que está **más cerca de la solución ideal** y **más lejos de la anti-ideal**.

**Cómo funciona.** Se normaliza la matriz de decisión, se multiplican las columnas por los pesos, se calculan las distancias
euclidianas a las soluciones ideal y anti-ideal, y el **coeficiente de proximidad** `Ci = d⁻/(d⁺+d⁻)` ordena todo.

**Uso general.** Es la dupla más usada del mundo en MCDM — de selección de proveedores a evaluación de desempeño.

**🔒 En este proyecto.** Corremos el TOPSIS en **dos normalizaciones** — vectorial (euclidiana) y min-max (lineal) —, de ahí
el **"2n"**. Cada proyecto recibe dos coeficientes y el ranking final es el promedio. Lo que se gana es una medida que casi
nadie reporta: la **concordancia entre las normalizaciones**. Cuando ambas discrepan sobre la posición de un proyecto, su
resultado es **frágil ante una elección técnica arbitraria** — y el dashboard lo muestra. La matriz de Saaty de este
proyecto tiene `CR = 0,0119`, muy por debajo del límite de 0,10.

#### 📖 3. ELECTRE I — *ÉLimination Et Choix Traduisant la REalité*

**Qué es.** **Bernard Roy (1968)**, en la consultora SEMA, en París. Es el punto cero de la escuela europea de
sobreclasificación. La pregunta no es *"¿cuál es la nota de cada uno?"*, sino *"¿es **a** al menos tan bueno como **b**?"*.

**Cómo funciona.** Para cada par `(a, b)` se calculan dos índices. La **concordancia** `C(a,b)` suma los pesos de los
criterios en que `a` es al menos tan bueno como `b`. La **discordancia** `D(a,b)` mide la **mayor desventaja** de `a`
frente a `b`. Se dice que `a` **sobreclasifica** a `b` si la concordancia es alta **y** la discordancia baja. El conjunto de
alternativas que **nadie sobreclasifica** es el **núcleo** (*kernel*) — el menú de elecciones defendibles.

**Uso general.** Decisiones públicas y ambientales, donde compensar un criterio catastrófico sería inaceptable.

**🔒 En este proyecto.** El ELECTRE es el método que **se niega a mentir por conveniencia**. Un proyecto con VAN
estratosférico y alucinación escandalosa **no compra** su lugar: la **discordancia** lo frena. El framework reporta el
**núcleo** — los proyectos que ningún otro domina — y usa como score el **grado de sobreclasificación neto** (cuántos domina,
menos cuántos lo dominan). Es también el único de los seis que se permite decir: *"estos dos proyectos son simplemente
**incomparables**"*.

#### 📖 4. PROMETHEE II — *Preference Ranking Organization METHod for Enrichment Evaluation*

**Qué es.** **Jean-Pierre Brans (1982)**, refinado con **Bernard Mareschal y Philippe Vincke (1985)**. También es
sobreclasificación, pero con un giro elegante: en vez de un umbral binario, se mide **cuánto** se prefiere `a` a `b`.

**Cómo funciona.** Para cada criterio, la diferencia `d = g(a) − g(b)` pasa por una **función de preferencia** que la
convierte en un grado entre 0 y 1. Brans propuso **seis funciones generalizadas** (usual, cuasi-criterio, umbral de
preferencia, nivel, lineal con indiferencia, gaussiana), parametrizadas por un **umbral de indiferencia `q`** (bajo el cual
la diferencia es irrelevante) y un **umbral de preferencia `p`** (sobre el cual la preferencia es total). Se suman los grados
ponderados: `φ⁺` es cuánto `a` domina a los otros, `φ⁻` cuánto es dominado, y el **flujo neto** `φ = φ⁺ − φ⁻` produce un
**preorden completo** (PROMETHEE II).

**Uso general.** Energía, logística, salud — siempre que graduar la **intensidad** de la preferencia importe.

**🔒 En este proyecto.** Usamos la función **lineal con indiferencia**, con `q` y `p` estimados de los cuantiles 10% y 90% de
las desviaciones observadas en cada criterio. El PROMETHEE responde *"¿cuánto mejor es el ganador?"*, y no solo *"¿es
mejor?"*. Y fue justamente él quien produjo el hallazgo más interesante del portafolio: en el análisis de robustez, el
**PROMETHEE II elige al líder del consenso en apenas el 25,4% de los universos de preferencia** — mientras las otras cuatro
escuelas concuerdan. El consenso estaba **enmascarando una divergencia de escuela**.

#### 📖 5. MAUT — *Multi-Attribute Utility Theory*

**Qué es.** **Ralph Keeney & Howard Raiffa (1976)**, herederos directos de von Neumann y Morgenstern. Es la escuela americana
en su forma axiomática: si tus preferencias obedecen ciertos axiomas de racionalidad, entonces existe una **función de
utilidad** que las representa, y decidir es **maximizar la utilidad esperada**.

**Cómo funciona.** Cada criterio recibe una **función de utilidad** `uⱼ` que mapea desempeño en satisfacción. La utilidad
global es aditiva: `U(a) = Σ wⱼ · uⱼ(a)` — válida bajo **independencia aditiva** en preferencia. El punto crucial es la
**forma** de la función: una `u` **cóncava** representa **aversión al riesgo** (el segundo millón vale menos que el primero);
lineal es neutralidad; convexa es propensión.

**Uso general.** Decisiones médicas, políticas energéticas, negociación — cualquier contexto en que la actitud ante el riesgo
deba ser **explicitada y defendida**.

**🔒 En este proyecto.** Usamos utilidad **exponencial** `u(z) = (1 − e^(−r·z)) / (1 − e^(−r))`, con coeficiente de aversión
`r = 2`. Es una **elección ética declarada**: el framework es **conservador**. Una ganancia incierta vale menos que una
ganancia cierta de la misma media — exactamente como la evaluaría un CFO prudente. Mientras el TOPSIS trata todas las
ganancias como fungibles, el MAUT **penaliza la promesa alta e incierta**.

#### 📖 6. MCDA-C — *Multicriterio de Apoyo a la Decisión — Constructivista*

**Qué es.** Formalizado por **Leonardo Ensslin, Gilberto Montibeller y Sandra Noronha (2001)**, con raíces en Roy y en Bana e
Costa. La premisa es filosófica: el modelo **no preexiste** al decisor. Se **construye con él**, en tres fases —
**estructuración** (mapas cognitivos, descriptores), **evaluación** (funciones de valor, tasas de sustitución) y
**recomendaciones**.

**Cómo funciona.** Cada criterio recibe un **descriptor** con niveles, y dos de ellos son anclas: el nivel **Neutro** (bajo el
cual el desempeño compromete) y el nivel **Bueno** (sobre el cual hay excelencia). La función de valor está anclada: `V = 0` en
Neutro, `V = 100` en Bueno, y **extrapola** libremente fuera del intervalo.

**Uso general.** Evaluación de desempeño organizacional, gestión pública, contextos en que el decisor necesita **aprender**
sobre su propio problema.

**🔒 En este proyecto.** En ausencia de una sesión de estructuración con el decisor, anclamos los niveles en los **cuartiles
observados** del portafolio: `Neutro = Q1`, `Bueno = Q3`. Esto preserva lo que el MCDA-C tiene de único — no solo **ordena**,
**clasifica**: `V < 0` es **comprometedor**, `0 ≤ V ≤ 100` es **competitivo**, `V > 100` es **excelencia**. Un proyecto puede
encabezar el ranking y aun así estar en la franja comprometedora. Ningún otro método de este conjunto te lo diría.

#### 📖 Por qué cinco métodos, y no uno

Porque **cada escuela se equivoca de forma distinta**, y un método solo devuelve un ganador con **confianza implícita del
100%** — lo cual es siempre mentira. El AHP-TOPSIS compensa de más; el ELECTRE a veces no decide; el MAUT depende de la forma
de la utilidad; el MCDA-C depende de las anclas.

Corremos los cinco con los **mismos pesos** (los del DEMATEL) y cerramos por **consenso de Borda**. Entonces la divergencia
entre ellos deja de ser un estorbo y se vuelve **información**: cuando cuatro concuerdan y uno disiente de frente, eso no es
ruido — es el aviso de que tu elección **depende de la escuela de decisión** que adoptaste implícitamente.

#### 📖 La pregunta final: ¿el veredicto sobrevive?

Todo el edificio anterior descansa sobre **pesos**, y los pesos son **estimaciones**. Si dos puntos porcentuales en el peso del
IITA intercambian el 1º con el 2º lugar, el "ganador" es un **artefacto de la calibración**, no un hecho del portafolio.

Por eso perturbamos los pesos del DEMATEL con una **Dirichlet** — `w' ~ Dir(κ·w)`, que vive exactamente en el símplex y
preserva `E[w'] = w`, perturbando **sin sesgar** — y reranqueamos **2.000 veces**. El veredicto cambia de naturaleza:

> *"Project C es el mejor"* ⟶ **"Project C gana en el 99,9% de los universos de preferencia plausibles"**

Es un **intervalo de confianza sobre la decisión misma**. Con eso, el framework deja de medir solo el riesgo del **dinero** y
pasa a medir el riesgo de la **decisión**.


**Qué es y para qué sirve.** Cuando eliges entre proyectos, los criterios **entran en conflicto** (un VAN alto suele
venir con riesgo alto) y son **inconmensurables** (¿cómo sumas pesos con porcentaje de alucinación?). El MCDA es el
campo que vuelve esa elección explícita, auditable y defendible. Su tesis fundadora es incómoda y liberadora: **no
existe el "mejor" en el vacío.** Existe un mejor *dado un sistema de preferencias que hiciste explícito*. Cambiar la
opinión implícita por un modelo explícito: esa es toda la ganancia.

**Las tres escuelas.** La **americana**, de valor y utilidad (AHP, MAUT): agrega todo en un único número. La
**europea**, de sobreclasificación (ELECTRE, PROMETHEE), de Bernard Roy: acepta que dos alternativas puedan ser
**incomparables** y permite el **veto** — una nota pésima en un criterio no se compensa con notas óptimas en los
demás. La **constructivista** (MCDA-C): el modelo no se descubre, se **construye junto con el decisor**.

| Método | Origen | Pregunta central | Lo que solo él aporta | En el portafolio de IA |
|---|---|---|---|---|
| **DEMATEL** | Gabus & Fontela, Battelle (1972-73) | *"¿Quién influye a quién?"* | separa **causa** de **efecto** y deriva los **pesos** de la propia estructura de influencia | muestra que reducir la alucinación (IITA) es **causa** — actúa allí y VAN, TIR y riesgo mejoran juntos |
| **AHP-TOPSIS 2n** | Saaty (1977) · Hwang & Yoon (1981) | *"¿Quién está más cerca de la solución ideal?"* | pesos por comparación par a par con **prueba de consistencia** (CR ≤ 0,10) | rankea en **dos normalizaciones** y reporta la concordancia entre ellas |
| **ELECTRE I** | Bernard Roy (1968) | *"¿Quién domina a quién — y quién sobrevive sin ser dominado?"* | **incomparabilidad** y **veto**: un criterio pésimo no se compra con otros óptimos | aísla el **núcleo** de proyectos que ningún otro domina |
| **PROMETHEE II** | Brans & Vincke (1985) | *"¿Cuál es el flujo neto de preferencia?"* | **seis funciones de preferencia** con umbrales de indiferencia y preferencia | gradúa *cuánto* mejor es un proyecto, no solo *si* lo es |
| **MAUT** | Keeney & Raiffa (1976) | *"¿Qué maximiza la utilidad de quien decide?"* | modela la **aversión al riesgo** con utilidad cóncava | penaliza ganancias inciertas — un decisor prudente no paga lo mismo por ellas |
| **MCDA-C** | Ensslin, Montibeller & Noronha (2001) | *"¿Dónde está el nivel Bueno y dónde el Neutro?"* | **función de valor anclada**: `V=0` en Neutro, `V=100` en Bueno, con extrapolación | clasifica en **comprometedor / competitivo / excelencia** en vez de solo ordenar |

**Por qué cinco, y no uno.** Cada escuela se equivoca de una forma distinta. Un método solo devuelve un ganador con
**confianza implícita del 100%** — lo cual es siempre mentira. Corriendo los cinco y cerrando por **consenso de
Borda**, la divergencia entre ellos se vuelve **información**: cuando cuatro concuerdan y uno disiente de frente, eso
no es ruido — es el aviso de que tu elección depende de si prefieres *sobreclasificación* a *utilidad*. Y la
**perturbación de Dirichlet** en los pesos responde la pregunta final: *"¿el 1º puesto sobrevive a un error de dos
puntos porcentuales en la calibración?"*


### 🧪 Los cuatro engranajes: Iman-Conover, Kolmogorov-Smirnov, Dirichlet y el tornado

Los dos grandes métodos de arriba descansan sobre cuatro piezas menores — y es en ellas donde vive la diferencia entre
una simulación honesta y un número bonito. Vale la pena conocerlas.

#### 🔗 Iman-Conover — imponer correlación **sin destruir las distribuciones**

**Qué es.** Propuesto por **Ronald Iman y William Conover (1982)**. Resuelve un problema que parece trivial y no lo es:
*¿cómo sortear variables correlacionadas cuando las marginales no son normales?* El camino ingenuo — generar normales
correlacionadas por Cholesky y transformarlas — **deforma las marginales**. Y si acabas de ajustar una LogNormal a tus
datos, deformarla tira exactamente el trabajo que hiciste.

**Cómo funciona.** Es una **reordenación por rangos**, no una transformación de valores. Se construye una referencia con
los **puntajes de van der Waerden** `Φ⁻¹(i/(n+1))`, barajados por columna; se calcula `P = chol(R)` (el objetivo) y
`Q = chol(corr(M))` (la correlación accidental de la referencia); se forma `S = M·(Q⁻¹P)ᵀ`. Entonces cada columna de la
muestra original se **reordena según los rangos de `S`**. Como solo cambia el *orden* de los valores ya sorteados, las
**distribuciones marginales permanecen exactas** — bit a bit.

**Un detalle fino, y honesto.** `R` es la correlación de la *referencia normal*, no la de Pearson del resultado. La
correlación de rangos inducida sigue la cópula normal: `ρ_S = (6/π)·arcsin(R/2)`. Para `R = 0,80` da **0,7859** — y es
exactamente lo que medimos al probar (0,786). No es un error del método; es su matemática.

**Usos generales.** Riesgo financiero (activos correlacionados), confiabilidad estructural, muestreo por hipercubo latino.

**🔒 En este proyecto.** Es lo que permite correlacionar los flujos de caja **sin sacrificar** la distribución ajustada a
tus tokens. Antes de usarla, la matriz se valida: simétrica, diagonal 1 y **definida positiva** (vía Cholesky). Una
matriz de correlación inconsistente se rechaza informando el menor autovalor — en vez de producir números sin sentido en
silencio.

#### 📏 Kolmogorov-Smirnov — la distancia entre lo que **supones** y lo que los datos **dicen**

**Qué es.** Una prueba **no paramétrica** de bondad de ajuste. El estadístico es simple y bello:
`D = sup |Fₙ(x) − F(x)|`, la mayor separación vertical entre la **función de distribución empírica** de tus datos y la
**teórica** que propusiste. Bajo la hipótesis nula, la distribución de `D` **no depende de cuál sea `F`** — de ahí
*distribution-free*.

**Una salvedad de honestidad metodológica.** El p-valor clásico del KS supone que los parámetros de `F` se fijaron
**antes** de ver los datos. Cuando se **estiman de los mismos datos** (como aquí, por máxima verosimilitud), la prueba se
vuelve **optimista**: acepta de más. El rigor pediría la corrección de **Lilliefors** o un **bootstrap paramétrico**. Por
eso tratamos el KS como **diagnóstico**, no como prueba — y lo usamos solo para **rechazar** ajustes malos, nunca para
declarar un ajuste "correcto".

**Usos generales.** Bondad de ajuste; comparación de dos muestras (KS de dos muestras); detección de *drift* de datos en
sistemas de aprendizaje automático en producción.

**🔒 En este proyecto.** Mide cuánto la distribución ganadora por AIC realmente describe tu serie de tokens. Cuando el
p-valor cae por debajo de 0,05, la pantalla estampa **`ADHERENCIA DÉBIL` en rojo** — en el portafolio de demostración eso
ocurre con uno de los proyectos, y el framework lo **muestra** en vez de esconderlo. Un número honesto vale más que uno
bonito.

#### 🎲 Perturbación de Dirichlet — el **intervalo de confianza de la decisión**

**Qué es.** La distribución **Dirichlet** es la distribución natural sobre el **símplex**: vectores de números positivos
que suman 1 — exactamente lo que es un vector de pesos. Es la conjugada de la multinomial y la generalización de la Beta.

**Por qué ella, y no ruido gaussiano.** Sumar ruido normal a los pesos produce valores negativos y rompe la suma unitaria.
La Dirichlet vive *dentro* del espacio válido. Y, parametrizada como `w' ~ Dir(κ·w)`, tiene dos propiedades que la hacen
perfecta para el trabajo: `E[w'] = w` (perturba **sin sesgar**) y `Var(w'ᵢ) = wᵢ(1−wᵢ)/(κ+1)` (la dispersión se controla
con una sola perilla). Cuando `κ → ∞`, colapsa en los pesos originales.

**Usos generales.** *Prior* bayesiano para proporciones; Asignación Latente de Dirichlet (**LDA**) en modelado de tópicos;
el **bootstrap bayesiano** de Rubin (1981); y análisis de sensibilidad de pesos en decisión multicriterio.

**🔒 En este proyecto.** Con `κ = 200`, un peso de 13% oscila cerca de **±2,37 puntos porcentuales** — el margen de error
plausible de un juicio de experto. Reranqueamos **2.000 veces** y obtenemos `P(victoria)` para cada proyecto. Fue este
engranaje el que reveló el hallazgo más incómodo del portafolio: el consenso es robusto (99,9%), pero el **PROMETHEE II
elige al líder en apenas el 25,4% de los universos**. Sin la Dirichlet, esa divergencia quedaría invisible.

#### 🌪️ Tornado de sensibilidad — qué variable **realmente** mueve el resultado

**Qué es.** Un gráfico de barras horizontales, ordenado por el efecto absoluto, que responde: *entre todas las entradas
inciertas, ¿cuáles mueven la salida?* El nombre viene de la forma — barras anchas arriba, estrechas abajo.

**Dos medidas que parecen lo mismo y no lo son.**
- El **beta** de una regresión múltiple responde: *"si esta entrada sube 1 unidad, ¿cuánto sube la salida?"* Es un efecto
  **unitario**, indiferente a cuánto varía de hecho esa entrada.
- La **correlación de Pearson** responde: *"¿cuánto de la incertidumbre de la salida es dictado por esta entrada?"* Ya
  incorpora la **escala de la incertidumbre** (aproximadamente `β·σᵢ/σ_y`).

Una variable puede tener beta enorme y correlación cero: *movería* mucho el resultado, pero en la práctica **casi no
varía**. Reportar solo una de las dos es media verdad.

**Usos generales.** Riesgo de proyecto, modelos financieros, ingeniería de confiabilidad, calibración de simuladores.

**🔒 En este proyecto.** Aquí el tornado hizo algo raro: **denunció una limitación del propio modelo**. Al correrlo sobre
el VAN, los betas salieron **exactamente iguales a `1/(1+i)ᵗ`** — los factores de descuento — porque el VAN es *lineal* en
los flujos. El tornado de regresión, en ese caso, es **degenerado**: no informa nada más allá de la tasa. Es la
**correlación** la que carga la señal. Y cuando el costo de tokens entró como variable, su beta dio `−1/(1+i)ᵗ` (el costo
entra con signo negativo) y su correlación quedó cerca de cero. La lectura conjunta es precisa y honesta: *"cada 1 unidad
más en tokens quita 0,91 del VAN — pero, en este proyecto, la incertidumbre del VAN no viene de los tokens."* Ninguna de
las dos medidas, sola, diría eso.

---

<!-- budget-global-section -->

<!-- budget-blueprint -->

> ## 🌿 Tu portafolio de IA es una **biosfera** — trátalo como tal
>
> Deja de pensar en cada proyecto como una hoja de cálculo aislada. **Viven en el mismo ecosistema, y ese
> ecosistema tiene un recurso finito circulando: el pool de tokens de tu plan.** Cada proyecto es una
> especie compitiendo por él. Y como toda biosfera, obedece dos leyes que nadie puede derogar:
>
> - **La capacidad de carga es finita.** Lo que una especie consume de más, otra deja de tener. No hay
>   crecimiento infinito en un pool cerrado — solo *quién se está comiendo el almuerzo de quién*.
> - **Sin frenos, el ecosistema colapsa en monocultivo.** La especie que gana retroalimentación positiva sin
>   límite ahoga a todas las demás — y muere con ellas, tras destruir la diversidad que la alimentaba.
>
> **Por eso existe este módulo.** Ninguna herramienta del mercado — Langfuse, CloudZero, Vantage — ve el
> portafolio como un organismo vivo: dan *coste por proyecto*, como si cada uno respirara su propio aire. No
> lo hace. **Aquí ves la biosfera entera** — quién prospera, quién parasita, quién financia a quién, y qué
> cuesta admitir una especie más en el ecosistema. En dinero, no en opinión.


## 💰 Budget Global de Tokens — cada proyecto es un CENTRO DE COSTE

**Existe UN único presupuesto: el del plan que contratas.** Todo lo demás **desciende de él**. Cada proyecto es un **centro de coste** — **no tiene partida propia**. Su asignación es una **porción del Budget Global**, y esa porción se **recalcula automáticamente** cada vez que un proyecto entra o sale del portafolio. **Nada se crea; todo se reparte.**

> **El bug estructural que esto corrigió.** El presupuesto de tokens de cada proyecto era `consumo × 1,10` — exactamente 1,100 en los **diez**. Circular. Auto-justificante. **Ningún proyecto podía pasarse del presupuesto, por construcción.** *Un presupuesto que sale del propio gasto no es presupuesto: es un recibo.* Hoy, con la cuota del pool real, **6 de 10 proyectos lo revientan**.

```text
   ASSINATURA DO PLANO / PLAN SUBSCRIPTION
              │
              ▼
   💰 BUDGET GLOBAL  ─────────  a quota mensal contratada. É FINITA.
              │
              ├── piso igualitário (50%)
              └── por VALOR entregue (50%)
              │
              ▼
   🏷️ CENTRO DE CUSTO 1 … N  ──  a cota de CADA projeto
```

### 🍩 Concepto — el pool es COMPARTIDO y FINITO

**Concepto.** Langfuse, CloudZero, Vantage y compañía dan **coste por proyecto**, como si cada uno tuviera su propio grifo. **No lo tiene.** Existe **un plan contratado** con cuota mensual finita, y **cada token que un proyecto quema es un token que otro no tendrá**. Es la **tragedia de los comunes** aplicada al presupuesto de IA.

**Metodología.** El Budget Global sale del contrato: `asientos × US$ × cambio × (1+IOF)` más la infra fija, dando el **TCO mensual** y el **coste por millón de tokens**. El consumo real viene de los logs, proyectado a **run-rate mensual**. De ahí salen la **utilización de la cuota**, el **margen** y la **fecha de agotamiento del pool**.

**Aplicación — y el número que duele.** **El 31% del consumo es DESPERDICIO**: 29 millones de tokens/mes quemados en llamadas que **fallaron y no devolvieron nada** (alucinación, rate-limit). Eso es **4,7× todo tu margen contractual**. Dicho claro: **te empujarían a contratar un plan mayor por culpa de llamadas que no entregaron respuesta.** Recortar la mitad del desperdicio libera más capacidad que el margen entero — **sin gastar un céntimo más**.

![Budget Global utilizado por proyecto (Burn Token Rate) — cada porción no es 'su coste': es la capacidad que le quita a los demás](docs/screenshots/budget-donut-burn-token.png)

### ⚖️ Reparto adaptativo y SUBSIDIO CRUZADO — quién financia a quién

**Concepto.** El reparto **por consumo** es el estándar del mercado, y es **auto-justificante**: quien más quema recibe la mayor cuota, lo que **legitima el desperdicio**. El reparto honesto es por **valor entregado (EV)**.

**Metodología.** La cuota de cada centro de coste es `suelo igualitario (50%) + valor entregado (50%)`, **redimensionada cada vez que N cambia** — un proyecto nuevo tiene EV = 0 y, sin el suelo, recibiría **cero tokens** y jamás podría producir valor. El **subsidio cruzado** es la diferencia entre la cuota que tendría por lo que **consume** y la que tendría por lo que **entrega**. La suma de los subsidios es **exactamente cero**: es transferencia, no creación de valor.

**Aplicación.** La amplitud de eficiencia es de **68×**: Project F entrega **642** de valor por millón de tokens; Project J, **10**. Y el reparto revela la factura: **R$ 3.431/mes — el 40% del TCO — se transfiere de los eficientes a los ineficientes, cada mes, a oscuras.** Project F, el más barato del portafolio, **está pagando la cuenta de Project J**.

![Subsidio cruzado — quien consume más de lo que entrega es subsidiado; quien entrega más de lo que consume paga la cuenta de los demás](docs/screenshots/budget-subsidio-cruzado.png)

### 🔒 Contención PRECIFICADA — la cadena causal aplicada al PORTAFOLIO

**Concepto.** La cadena causal liga, **dentro** de un proyecto: `token que derivó → riesgo → plazo (P80) → dinero`. Esto liga **ENTRE** proyectos: `excedente de uno → agotamiento del pool → estrangulamiento de los OTROS → su P80 se desliza → su Cost of Delay pasa la factura`.

**Metodología.** Exige, **a la vez**, FinOps (la cuota), EVM (el valor entregado), riesgo (la exposición) y cronograma simulado (el P80). Por eso **ninguna herramienta del mercado lo hace** — ninguna tiene los cuatro motores juntos. Langfuse ve el token. Jira ve la tarea. CloudZero ve la factura. **Ninguno puede decir que el proyecto J le está costando R$ X de retraso al proyecto F.**

**Aplicación — y la honestidad que sostiene el número.** En el escenario de estrangulamiento, **Project J causa R$ 3.730 de daño a los demás y solo sufre R$ 853** — saldo +2.877: es el **VERDUGO**. **Project C, 30× más eficiente, sufre R$ 867 y no causa nada** — es **VÍCTIMA**. La suma de los saldos es **cero**: todo verdugo tiene una víctima.

> ⚠️ **Pero hoy el pool CABE** (94% de la cuota). **No hay estrangulamiento físico** — nadie para, nadie se retrasa. El daño es **asignativo**, no **operativo**. Decir *"J está retrasando a C"* con margen en el pool sería **mentira con cara de rigor**. Por eso el módulo es **escenarizado** y **etiquetado como previsión**: muestra *a partir de qué punto* el pool vira (+10% de consumo → el portafolio entero para 0,9 días, R$ 1.497) y *cuánto cuesta cuando vira*.

![Contención precificada — quién causa el daño y quién lo paga; cuando el pool se seca TODOS paran, incluidos los eficientes que no causaron nada](docs/screenshots/budget-contencao.png)

### 🪓 Política de recorte — si el portafolio necesita espacio, ¿QUIÉN sale?

**Concepto.** Esta es la pregunta que el comité de portafolio **nunca logra responder**. En un pool finito, admitir el proyecto N+1 **quita tokens a todos los N que ya estaban** — admitir 1 proyecto **diluye a todos en un 9,1%**.

**Metodología.** La respuesta honesta **no es "el que más gasta"** — recortar por consumo bruto castigaría a un proyecto **grande y productivo**. La respuesta es **"el que menos entrega POR TOKEN"**: ordenar por **eficiencia** (EV ÷ millón de tokens) libera el máximo de pool al **mínimo coste de valor**. La diagonal `y = x` separa el recorte que **compensa** del que **destruye más de lo que libera**.

**Aplicación.** Recortar **Project J** libera el **20,5% del pool** sacrificando el **1,9% del valor** — abre casi 2 plazas nuevas sin diluir a nadie. Recortar **Project F** liberaría el 3,4% y sacrificaría el **21,2% del valor**: **destruiría más valor del que liberaría capacidad**. **No es "recorten costes" — es un trade-off explícito, con número.**

![Política de recorte — % del pool liberado frente a % del valor sacrificado; la diagonal separa el recorte que compensa del que destruye](docs/screenshots/budget-politica-corte.png)

---
<!-- budget-loop-section -->

## 🔁 Loop de reaprendizaje sobre el presupuesto — el agente que **evoluciona con el ecosistema**

**Un ecosistema sano tiene memoria.** El depredador aprende qué presa vale la caza; la planta aprende hacia dónde crecer. Sin ese aprendizaje no hay adaptación — solo ensayo y error ciego, para siempre. Era justo lo que le faltaba al agente: recomendaba *recortar el desperdicio*, pero **nunca comprobaba, a la semana siguiente, si el recorte que él mismo ordenó liberó pool de verdad.** Recomendar sin verificar no es gestión — es conjetura reciclada.

**Concepto.** El PM Agent cierra el loop: **guarda el número** la semana en que recomienda el recorte y, en el weekly siguiente, **se cobra a sí mismo**. ¿Cayó el desperdicio? La recomendación funcionó. ¿No? Falló. Es el mismo **bandit contextual** del motor de reaprendizaje — ahora aplicado a la dimensión de **tokens**, el recurso más escaso de la biosfera.

**Metodología.** Solo se evalúa la acción que **él recomendó** — responde por lo que ordenó y **no se apunta el mérito de lo que liberó el azar**. El recorte funcionó → su confianza en esa recomendación **sube**. No funcionó → **baja**. Una variación por debajo del 2% es ruido, y **no aprende del ruido**. La confianza es **por proyecto**: el agente descubre qué recortes liberan pool en *ese* ecosistema.

**Beneficio directo.** Cada viernes el agente llega al weekly con una rendición de cuentas de su propio consejo: *"la semana pasada ordené recortar ALUCINACION_CODIGO; liberó R$ X de pool — subo mi confianza"* o *"no cuajó — bajo mi confianza y reconsidero"*. Con el tiempo deja de repetir el recorte que no funciona en tu contexto y redobla el que sí. **Tu presupuesto deja de regirse por una regla fija y pasa a regirse por un agente que aprendió a jugar en tu tablero.**

![Loop de reaprendizaje sobre el presupuesto — el desperdicio sube y baja, y la confianza del agente responde: sube cuando el recorte funciona, baja cuando falla, ignora el ruido](docs/screenshots/budget-loop-reaprendizagem.png)

---
<!-- pm-agent-section -->

## 🤖 Project Manager Agent — lee 10 dimensiones, aprende y **sabe callarse**

El dashboard **diagnostica**. La cadena causal **cuantifica**. El agente **decide qué hacer ahora** — y, ciclo tras ciclo, descubre qué palanca mueve de verdad la aguja *en ese proyecto concreto*. Recorre **10 dimensiones** (plazo, ROI, riesgo, tokens, coste, deriva del modelo, fiabilidad, calidad, flujo y desperdicio), convierte cada una en **días-equivalentes de proyecto × el coste del retraso de ese proyecto**, y responde a la única pregunta que importa: **qué hacer ahora, y cuánto vale hacerlo.**

> **La debilidad que había que corregir.** El agente **siempre** recomendaba algo: cada ciclo cogía el mayor daño y gritaba. **Un agente que grita cada semana se convierte en ruido, y el ruido se ignora** — así que no cambia nada, por más razón que tenga. **Le faltaba el derecho a callarse.** Eso es lo que entregan las tres metodologías siguientes.

### 🚦 PRINCE2 — *management by exception*: el derecho a callarse

**Concepto.** El *management by exception* de PRINCE2 dice que al gestor **no se le debe molestar** mientras el proyecto esté dentro de las tolerancias acordadas. Cuando la **previsión** rebasa la tolerancia — no lo realizado, la **previsión** — se dispara un **Exception Report**.

**Metodología.** Una tolerancia por dimensión (plazo, coste, riesgo, calidad, beneficio). El escalado lo dispara la **previsión**: el P80 de Monte Carlo y el EAC del EVM. El Exception Report tiene cuatro partes obligatorias — **causa, impacto, OPCIONES y recomendación**. Es la línea de las *opciones* la que separa un informe de excepción de una alarma: escalar sin ofrecer alternativas es empujar el problema hacia arriba, no gestionarlo.

**Aplicación aquí.** Las tolerancias **no son números que nos inventamos** — salen de lo que el proyecto **ya declaró**: la fecha prometida (`prazo_alvo`), el presupuesto aprobado (`BAC`), la clasificación del **propio registro de riesgos** (`nivel='critico'`) y la **línea base de calidad del propio proyecto** (regresión contra sí mismo, al estilo DORA). Solo el límite de ROI es política explícita — y está a la vista, para que el board discrepe. Las opciones que ofrece el agente son **absorber** (quemar reserva de gestión), **recuperar** (comprimir el camino crítico) o **renegociar** (mover la fecha o recortar alcance).

![Tolerancias PRINCE2 — el margen de cada dimensión hasta la excepción; solo Calidad la rebasó, y solo ella se escala](docs/screenshots/prince2-tolerancias.png)

### 🌡️ CCPM (Goldratt) — *buffer management* y el fever chart

**Concepto.** En la *Cadena Crítica* de Goldratt, el búfer no es grasa escondida en cada tarea: es un **colchón explícito al final del proyecto**. El **fever chart** cruza *cuánto de la cadena está terminado* con *cuánto del búfer se ha consumido*, y dice en cuál de las tres zonas estás.

**Metodología.** Las fronteras son **diagonales**, y esa es la esencia del método: quemar búfer **al final** es normal — quemarlo **al principio** es grave, porque queda proyecto entero por delante. **VERDE = no hagas nada. AMARILLO = planifica la recuperación. ROJO = actúa ya.**

```
verde/amarelo:    y = 1/3 + (1/3)·x
amarelo/vermelho: y = 2/3 + (1/3)·x
```

**Aplicación aquí.** El búfer es `P80 − P50` del **cronograma Monte Carlo** que ya ejecutábamos. El consumo es el **retraso del Earned Schedule** convertido a días. Y es el fever chart lo que da al agente el gatillo objetivo del silencio: **zona verde y dentro de tolerancia = nada que escalar.** Hoy **3 de los 10 proyectos** reciben exactamente eso — y es callándose cuando no hay nada que decir como el agente gana el derecho a ser escuchado cuando sí lo hay.

![Fever chart del CCPM — los 10 proyectos en las tres zonas; las fronteras diagonales hacen que el mismo consumo de búfer sea benigno al final y grave al principio](docs/screenshots/ccpm-fever-chart.png)

### 🏦 PMI — *reserve analysis*: contingencia × reserva de gestión

**Concepto.** El PMI separa dos reservas que casi todo el mundo mezcla: la **contingencia** cubre los *conocidos-desconocidos* (la variabilidad que **mediste**), y la **reserva de gestión** cubre los *desconocidos-desconocidos* (el susto).

**Metodología.** `contingencia = P80 − P50` y `reserva de gestión = P95 − P80`. Y la confrontación que casi nadie hace: la contingencia que **tienes** contra la que tu **registro de riesgos justifica** (EMV — *Integrated Cost-Schedule Risk Analysis*, Hulett). El búfer de duración es **ciego a los eventos de riesgo**; ahí es donde casi todo cronograma se descubre optimista.

**Aplicación aquí — y una lección de honestidad.** Convertir “impacto 4” (escala 1–5) en días exige un mapeo que es **nuestro, no tuyo**. Así que **sometimos a estrés nuestra propia suposición**: al reducir a la mitad el impacto supuesto, la conclusión “infra-reservado” pasa de **10/10 a 1/10 proyectos**. Es un **filo de navaja**, y por eso **no se vende como hallazgo** — cada proyecto lleva el campo `robusto`, y el agente **avisa cuando su propia lectura no sobrevive al test de estrés**. Lo que **queda sin suposición alguna** es aritmética pura, y ese sí es el hallazgo: **el búfer es ~9% de la cadena, frente al 25–50% con que trabaja el CCPM.**

### 🏃 Sprints y el debate del weekly del viernes

**Concepto.** El debate de progreso del *weekly* del viernes necesita **números**, no opiniones. La opinión no mueve proyectos.

**Metodología.** Tres métricas abren la discusión. **(1) Say-do ratio** (`ΔEV ÷ ΔPV`): un equipo en 0,7 **no es lento** — está *prometiendo un 30% más de lo que puede entregar*. La capacidad no se arregla exigiendo; el compromiso se arregla con previsibilidad. Y un say-do **muy por encima de 1** tampoco es heroísmo: es una **línea base rota**. **(2) El CPI local del sprint**, separado del acumulado **a propósito** — el acumulado es una media, y la media **esconde** el sprint malo reciente: un CPI acumulado de 1,05 puede albergar un último sprint a 0,60. **El local acusa; el acumulado consuela.** **(3) Previsión por velocidad**: si el equipo necesita 6 sprints y solo quedan 4, **la fecha ya murió** y nadie se enteró, porque el burndown acumulado todavía *parece* cerca del plan.

**Aplicación aquí.** El sprint **no está inventado**: es el **período del EVM**, la cadencia que el proyecto ya tiene, con PV/EV/AC reales. Crear un calendario de sprints paralelo al cronograma sería crear una **segunda verdad** sobre el mismo proyecto — y dos verdades es lo mismo que ninguna.

> **⚠️ Conformidad, dicha de frente.** Esto es un **informe de progreso por cadencia, basado en EVM (ANSI/EIA-748) con métricas de inspiración ágil** — **no es Scrum**. La *Scrum Guide 2020* **no contiene** “velocity” ni “burndown chart” (son práctica de mercado, no artefactos oficiales), y sustituyó el *commitment* del Sprint Backlog por el **Sprint Goal**, tratando el backlog como **forecast**. Por tanto “say-do ratio (entregado ÷ comprometido)” es vocabulario de la **industria**, no Scrum canónico. **La métrica es honesta; sería la etiqueta la que mentiría.**

![Sprints — say-do ratio por sprint y el burndown real contra el plan; la cadencia es el período del EVM](docs/screenshots/sprints-weekly.png)

### 🎯 El radar y el motor de reaprendizaje — por qué esta dimensión y no otra

El agente **no mira solo a la ganadora** — enseña el banquillo entero. Cada dimensión se vuelve **días-equivalentes**, los días se vuelven **dinero** al coste de retraso de *ese* proyecto, y el peso es lo que el agente **aprendió allí**. La prioridad es `daño × peso`.

El **motor de reaprendizaje** es un *bandit contextual* — simple y auditable, y lo decimos de frente: **no es deep learning**. Cada ciclo el agente recomienda una palanca y **guarda su métrica objetivo**; al ciclo siguiente **se cobra a sí mismo**. Mejoró → el peso **sube**. Empeoró → **baja**. Una variación por debajo del 2% es ruido, y **el agente no aprende del ruido**. Solo se juzga la palanca que él **recomendó**: responde por lo que mandó hacer y **no se apunta el mérito de lo que mejoró por azar**. El resultado es un perfil que **no sirve para el proyecto de al lado** — y ese es exactamente el punto.

![Radar de las 10 dimensiones — el daño de cada una en la misma regla (R$), y la que el agente eligió atacar](docs/screenshots/pm-agent-radar.png)

---
## 🌐 12 idiomas

El dashboard, las páginas por proyecto **y el texto dentro de las imágenes** de los gráficos están localizados en
**12 idiomas**: Português · English · Español · Français · Deutsch · 中文 · 한국어 · हिन्दी · עברית · Svenska · Русский · Suomi.
La traducción es dirigida por una **Translation Memory** (estilo SDL Trados) que estandariza y agiliza nuevos idiomas.

---

## 🙋 Objeciones (las preguntas que te estás haciendo ahora)

- **"No tengo tiempo."** → Cinco minutos con `./run_all.sh --mock` y el dashboard está corriendo en tu pantalla.
  Medir te **devuelve** las horas que ya pierdes en retrabajo y alucinación.
- **"Es demasiado complejo."** → Una línea. El framework hace el ETL, los cálculos, el ranking y las imágenes;
  **tú solo lees el veredicto.**
- **"Mi operación de IA es pequeña."** → Justamente por eso cada dólar pesa más. Pequeño hoy, portafolio mañana —
  **mide antes de escalar el desperdicio.**
- **"No uso Langfuse."** → La demo corre **100% sin Langfuse**. Cuando quieras datos reales, conectas **tu**
  cuenta (nunca la mía).
- **"Es solo otro dashboard bonito."** → No. Es **Balanced Scorecard + análisis de inversión (VAN/TIR/TIRM/VAE) +
  decisión multicriterio (AHP-TOPSIS)** — instrumentos de directorio, no adorno.
- **"¿Y la privacidad de mis datos?"** → La demo es **100% anónima** (Project A…J); datos/nombres reales y claves
  quedan **fuera del paquete**. Corres **local**, con **tu** cuenta.
- **"¿Cuánto cuesta?"** → **Nada.** Open source, en tu máquina. El único precio es seguir **sin medir** — y ese,
  ya lo estás pagando.

---

## 🧩 Skills incluidas (*build & analyze your own*)

Este repositorio incluye **Skills** reutilizables (Claude Code):

- **`measuring-ai-projects`** — definir/medir/reportar KPIs de proyectos de IA (el núcleo de este framework).
- **`github-benchmark-analyzer`** — analizar y hacer benchmark de **cualquier** repositorio/perfil de GitHub
  (estrellas, forks, seguidores, hashtags, estilo de README, palabras clave, lenguajes) y extraer lo que los
  líderes tienen en común. **Construye y analiza tu propio portafolio** — incluso contra el mercado.

---

## 📚 Recursos & referencias (Awesome)

Hombros de gigantes sobre los que este framework se apoya:

- **Estrategia & medición:** Kaplan & Norton — *The Balanced Scorecard* · Peter Drucker (gestión por objetivos).
- **Lean Six Sigma:** taxonomía de los 8 desperdicios (Muda), PDCA/Kaizen, Ishikawa/RCA.
- **Finanzas corporativas:** Lawrence Gitman — *Principios de Administración Financiera* (VAN, TIR, TIRM, IR).
- **Decisión multicriterio:** Thomas Saaty (**AHP**) · Hwang & Yoon (**TOPSIS**).
- **Stack técnico:** [Langfuse](https://langfuse.com) (LLM observability) · [Evidence](https://evidence.dev)
  (BI as Code) · [Rust/PyO3](https://pyo3.rs) · [Tectonic](https://tectonic-typesetting.github.io) (LaTeX).

---

## 🗺️ Roadmap

- [x] Pipeline Langfuse → SQLite → Evidence + Rust
- [x] 70+ KPIs (BSC + economía de APIs + Lean) · EVM
- [x] Financiero (VAN, TIR, TIRM, VAE, IR, Payback, dolarización)
- [x] AHP-TOPSIS 2n + Dossier administrativo (6 herramientas)
- [x] Dashboard e imágenes en **12 idiomas**
- [ ] Conectores extra de observabilidad (OpenTelemetry, Helicone)
- [ ] Modo SaaS multi-tenant + agendamiento nativo
- [ ] Publicación del dashboard estático (GitHub Pages)

---

## 🧰 Setup paso a paso (local, desde cero)

> Todo corre **en tu máquina**. Ninguna clave del autor acompaña el paquete y ningún dato sale de tu computadora.

### Paso 0 — Prerrequisitos

| Requisito | Versión | ¿Obligatorio? | ¿Para qué? |
|---|---|---|---|
| **Python** | 3.10+ | ✅ | pipeline, KPIs, Monte Carlo, MCDM |
| **Node.js + npm** | 18+ | ✅ | dashboard (Evidence) |
| **git** | cualquiera | ✅ | clonar el repositorio |
| **Rust + maturin** | estable | ⬜ opcional | acelera la clasificación de logs |
| **tectonic** | cualquiera | ⬜ opcional | genera los pitch decks en PDF |

*En Windows, usa **WSL** o **Git Bash** — la línea de montaje es un script `bash`.*

### Paso 1 — Clonar el repositorio
```bash
git clone https://github.com/bpenedo/Gestao-de-Projetos-PM-IA-BSC-DashBoard.git
cd Gestao-de-Projetos-PM-IA-BSC-DashBoard
```

### Paso 2 — Entorno Python aislado
```bash
cd foundations/pipeline
python3 -m venv .venv
source .venv/bin/activate        # Windows (PowerShell): .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Paso 3 — Dependencias del dashboard
```bash
cd ../evidence
npm install
```

### Paso 4 — Ejecutar la demo (anónima, sin credenciales)
```bash
cd ../pipeline
./run_all.sh --mock
```

En orden, la línea de montaje ejecuta: datos demo anónimos → KPIs → VAN/TIR/TIRM/VAE/IR → **ajuste de distribuciones
a los tokens** → **Monte Carlo (10.000 iteraciones)** → AHP-TOPSIS 2n → **DEMATEL · ELECTRE · PROMETHEE · MAUT ·
MCDA-C** → **robustez del ranking (Dirichlet)** → gráficos → dossier administrativo → mapa 5D → pitch decks → build.

### Paso 5 — Abrir el dashboard
```bash
cd ../evidence
npm run dev          # http://localhost:3000
npm run preview      # (alternativa) serve o estático já compilado em build/
```

### Paso 6 — Cambiar a TUS datos

**6.1 — Credenciales y parámetros** (todos opcionales; sin `.env` el pipeline usa los valores por defecto):
```bash
cd ../pipeline
cp .env.example .env      # edite: LANGFUSE_PUBLIC_KEY, LANGFUSE_SECRET_KEY, SELIC_ANUAL, USD_BRL...
```

**6.2 — Tu flujo de caja** (es lo que alimenta VAN, TIR y el Monte Carlo):
```bash
cp fluxo_caixa_template.csv fluxo_caixa.csv
```
Formato: `periodo 0` es la inversión (flujo negativo) y `taxa` es el descuento por período (`0.10` = 10%).
```csv
project_name,periodo,fluxo,taxa
Project A,0,-12000,0.10
Project A,1,3000,0.10
Project A,2,4000,0.10
```

**6.3 — Ejecutar con datos reales:**
```bash
./run_all.sh          # sem --mock: sincroniza do Langfuse e usa fluxo_caixa.csv
```

### Paso 7 (opcional) — Aceleración y PDFs
```bash
cd analise_rs && maturin develop --release && cd ..   # Rust (PyO3): classificação mais rápida
```
Para los pitch decks, instala **tectonic** (p. ej. `cargo install tectonic` o el gestor de paquetes de tu distro).

### Paso 8 (opcional) — Programar la actualización
```bash
crontab -e
*/15 * * * * /CAMINHO/ABSOLUTO/foundations/pipeline/run_all.sh >> /tmp/bsc.log 2>&1
```

### 🩺 Problemas comunes

| Síntoma | Causa probable | Solución |
|---|---|---|
| `no such table: ...` | base no inicializada | `python3 db.py` |
| El build del dashboard falla | artefactos viejos | `rm -rf ../evidence/build && npm run build` |
| `findfont: Failed to find font weight` | aviso de matplotlib | inofensivo, ignóralo |
| `Precisa de ≥2 projetos` | portafolio con un solo proyecto | el MCDM compara alternativas; agrega otra |
| `KS p-valor < 0,05` en pantalla | la distribución no describe bien tus datos | recolecta más muestras; el framework avisa en vez de esconder |
| Los números cambian entre corridas | se cambió la semilla | mantén `MC_SEED` fijo para reproducibilidad |

---

## 🤝 Contribuir

¡Las contribuciones son **muy bienvenidas**! Abre un *issue* describiendo tu propuesta (nuevo KPI, conector,
idioma, corrección) y envía un *pull request*. Estándares: código legible y consistente con su entorno, sin datos
personales en el paquete (la demo es anónima). Nuevos idiomas: agrega los objetivos a la Translation Memory y
ejecuta el generador.

## 📄 Licencia & autoría

© **Bruno Penedo** — 2026. Uso, estudio y contribución alentados; para uso comercial/redistribución, consulta al
autor. *(Se puede añadir una licencia OSS formal — abre un issue con tu preferencia.)*

## 🏷️ Topics
`awesome-list` · `education` · `resources` · `computer-science` · `python` · `business-intelligence` ·
`llmops` · `finops` · `aiops` · `programming` · `development` · `lists` · `free` · `unicorns` · `dashboard` ·
`balanced-scorecard` · `langfuse` · `llm-observability` · `kpi` · `project-management`

---

⭐ **Si este framework arroja luz sobre tu gasto en IA, deja una estrella — y empieza a lucrar con lo que ya pagas.**

---

**Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard** · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
