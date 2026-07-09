# 🧭 Gestão de Projetos PM IA BSC DashBoard (Build and Analyze Your Own AI Portfolio Projects)

🌐 [Português](README.md) · [English](README.en.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [中文](README.zh.md) · **한국어** · [हिन्दी](README.hi.md) · [עברית](README.he.md) · [Svenska](README.sv.md) · [Русский](README.ru.md) · [Suomi](README.fi.md)

![Method](https://img.shields.io/badge/method-Balanced%20Scorecard-1F3A5F)
![AI](https://img.shields.io/badge/AI-LLM%20observability-45a1bf)
![Finance](https://img.shields.io/badge/finance-NPV%20·%20IRR%20·%20MIRR%20·%20PI-46a485)
![Decision](https://img.shields.io/badge/decision-AHP--TOPSIS%202n-8E44AD)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-PyO3-orange?logo=rust&logoColor=white)
![Dashboard](https://img.shields.io/badge/dashboard-Evidence-236aa4)
![PDF](https://img.shields.io/badge/pitch%20deck-LaTeX-008080)
![i18n](https://img.shields.io/badge/i18n-12%20languages-0E7C86)
![status](https://img.shields.io/badge/status-v1-success)

### 💸 당신은 매달 AI에 돈을 냅니다. 그런데 AI는 **당신에게** 돈을 돌려주고 있나요?

**ChatGPT, Claude, Copilot, Gemini, Perplexity, DeepSeek, Kimi, Qwen…**가 카드를 긁을 때마다 **수백만 달러짜리** 질문이
답을 얻지 못합니다: **수익은 어디 있나요?** 실제로 몇 인시(人時)를 절약했나요? 당신의 돈은 환각·재작업·대기 속에서 얼마나
**증발**했나요? 어떤 AI 프로젝트가 **오늘 확장할 자격**이 있고, 어떤 프로젝트가 "혁신"이라는 박수 속에서 **현금을 흘리고**
있나요?

당신에게는 'AI 비용'이 있는 게 아니라 **조용한 누수**가 있습니다 — 그것도 눈을 가린 채로. *"측정되지 않는 것은 관리할 수도,
개선할 수도 없다"* — 그리고 시장은 당신 대신 측정하고, 당신에게 청구서를 보냅니다.

**이 프레임워크는 불을 켭니다.** AI 구독의 **보이지 않는 지출**을 **측정 가능하고, 비교 가능하며, 감사 가능한 수익**으로
바꿉니다 — **균형성과표**(Kaplan & Norton), **월스트리트급 투자 분석**, **다기준 의사결정**의 엄밀함으로. 이것이 *바라는 것*과
*아는 것*의 차이, AI에 **돈을 내는 것**과 AI로 **돈을 버는 것**의 차이입니다.

> *"측정되지 않는 것은 관리할 수도, 개선할 수도 없다."* — Kaplan & Norton

> *"정밀하게 측정하는 자가 탁월하게 짓는다."* — Pierre Vernier

> *기도하고 공부할 때, [나의 말]이 너를 떠나지 않게 하라. 네 입술에서 나오는 모든 단어와 표현마다, 하나됨(Unification)을 이루려는 마음을 품으라.* — Aryeh Kaplan

> *순수 형이상학은 그 본질상 모든 형태와 모든 우연 위에, 그 너머에 위치하여 동양의 것도 서양의 것도 아니다: 그것은 보편적이다.* — René Guénon

> *자기 자신을 아는 것은 자신의 혈통과 자신의 힘을 아는 것이다.* — Harvey Spencer Lewis

> *Scientia es Lux Lucis* ∞ Sapere Aude S∴A∴☬ ☿

> 🐺 **어둠 속에서 AI에 돈 내는 것을 멈추세요.** 시장이 믿음으로 AI를 구독하며 **Gartner** 통계(파일럿 이후 폐기되는 GenAI
> 프로젝트 ≥30%)가 되는 동안, **당신**은 모든 토큰을 측정하고, 승자 프로젝트를 선정하며, 보이지 않는 지출을 **감사 가능한
> 수익**으로 바꿀 것입니다: NPV · IRR · MIRR · EAA · 70+ KPI · 다기준 의사결정 · **12개 언어** C-레벨 대시보드. **AI는 이미
> 당신의 것입니다. 이제 그것을 수익성 있게 만드세요** — 무료로, 당신의 컴퓨터에서, **5분** 만에:
> `./run_all.sh --mock && npm run dev` 🔥

> 📖 **주요 문서:** **[`foundations/README.md`](foundations/README.md)** ·
> ⚙️ **설정(자신의 키 사용):** [`foundations/pipeline/SETUP.md`](foundations/pipeline/SETUP.md) ·
> 📊 **KPI:** [`foundations/KPIs.md`](foundations/KPIs.md) / [`foundations/KPIs_README.md`](foundations/KPIs_README.md)

---

## 📑 목차

- [🌅 왜 이것이 판을 바꾸는가](#-왜-이것이-판을-바꾸는가)
- [📈 증거 (Gartner · IDC · PwC · McKinsey · MIT)](#-증거-gartner--idc--pwc--mckinsey--mit)
- [💥 아무것도 하지 않는 것의 비용](#-아무것도-하지-않는-것의-비용-아무도-하지-않는-계산을-해보라)
- [✨ 기능](#-기능)
- [📸 스크린샷 (익명 대시보드)](#-스크린샷-익명-대시보드)
- [🚀 빠른 시작](#-빠른-시작-데모-langfuse-불필요)
- [🏗️ 아키텍처](#️-아키텍처)
- [📊 KPI 카탈로그](#-kpi-카탈로그-70)
- [💰 투자급 재무 분석](#-투자급-재무-분석)
- [🏆 다기준 의사결정 + 도시에](#-다기준-의사결정-ahp-topsis-2n--왕관의-보석-도시에)
- [🌐 12개 언어](#-12개-언어)
- [🙋 반론 (지금 당신이 스스로에게 묻는 질문들)](#-반론-지금-당신이-스스로에게-묻는-질문들)
- [🧩 포함된 Skills](#-포함된-skills-build--analyze-your-own)
- [📚 리소스 & 참고문헌](#-리소스--참고문헌-awesome)
- [🗺️ 로드맵](#️-로드맵)
- [🤝 기여](#-기여)
- [📄 라이선스 & 저작권](#-라이선스--저작권)

---

## 🌅 왜 이것이 판을 바꾸는가

**AI 시대에는 두 종류의 사람이 있습니다.** 첫 번째는 모든 것을 구독하고, 크게 지출하며, 잘되기를 **기도**합니다 — 그리고 파일럿에서
죽는 프로젝트라는 잔인한 통계를 부풀립니다. 두 번째는 월스트리트가 진지한 자산에 하는 일을 합니다: **측정하고, 비교하고,
우선순위를 매기고, 재배분**합니다 — 그리고 모든 구독 달러를 **복리 수익**으로 바꿉니다. 둘 사이의 유일한 차이는 **재능도 예산도
아닌, '계기화(instrumentation)'**입니다.

생성형 AI는 새로운 종류의 반복 지출 — **구독과 토큰** — 을 만들었고, 그와 함께 이 시대 가장 값비싼 낭비를 가져왔습니다:
**보이지 않는 낭비.** 보이지 않는 것은 고칠 수 없고, 측정하지 않는 것은 확장할 수 없으며, 증명하지 못하는 것은 이사회가 승인하지
않습니다.

**이 프로젝트는 당신을 첫 번째 부족에서 두 번째 부족으로 옮깁니다.** 모든 AI 프로젝트를 **금융 자산**으로 계기화하고
**균형성과표**, **투자 분석(NPV, IRR, MIRR, EAA, PI, 회수기간)**, **린 식스 시그마** 아래에서 측정합니다 — 나아가 다기준
모델(**AHP-TOPSIS 2n**)로 **당신 포트폴리오에서 최고의 프로젝트를 선정**합니다. 불투명한 월 청구서가 **감사 가능한 투자
논거**가 됩니다: 어디를 확장할지, 어디를 끊을지, 구독이 어디서 **몇 주** 만에 회수되는지 — 그리고 어디서 무방비로 출혈하는지를
숫자로 알게 됩니다.

우리는 새로운 영토의 **개척자**입니다 — **인공지능과 가치 회계 사이의 경계**. 아직 지도에 없는 땅을 측량하는 탐험가처럼, 이
프레임워크는 구독의 안개를 **명확한 수익 항로**로 바꾸는 **나침반**(🧭)입니다: 토큰 하나하나가 1마일, 프로젝트 하나하나가 이익을
향한 원정입니다. 맹목적 비용이 있던 곳에 **측정 가능한 기회**가 태어나고, 죽은 스프레드시트가 있던 곳에 **살아있는 투자 논거**가
피어납니다.

> **약속:** *AI에 돈 내는 사람*을 *AI로 돈 버는 사람*으로 — *AI를 쓰는 사람*을 그것을 **개척적으로 통달하고, 측정하고,
> 배가하는 사람**으로 바꿉니다. 믿음이 아니라 숫자로.

---

## 📈 증거 (Gartner · IDC · PwC · McKinsey · MIT)

제 말을 믿지 마세요. **수십 년간 이를 연구해 온 기관들을 믿으세요** — 그 평결은 만장일치입니다: **AI는 막대한 가치를 창출하지만,
측정하고 지배하는 자에게만 전달한다.** "통달 없이 AI를 쓰는" 사람은 폐기 통계가 되고, 수익을 계기화하는 사람은 **상을 차지합니다.**

- 🧭 **Gartner** — **2025년 말까지 생성형 AI 프로젝트의 ≥ 30%가 개념 증명 이후 폐기**될 것이며, 핵심 원인은 **불분명한 비즈니스
  가치**(그 외 열악한 데이터, 치솟는 비용, 취약한 통제)라고 예측했습니다. *→ 측정 없이는 프로젝트가 파일럿에서 죽는다.*
- 🔬 **MIT** (보고서 *"The GenAI Divide / State of AI in Business 2025"*, NANDA 이니셔티브) — **기업 GenAI 파일럿의 절대
  다수가 손익(P&L)에 측정 가능한 영향을 주지 못한다**고 널리 보도되었습니다; 가치를 전달하는 소수는 AI를 **프로세스와 측정**과
  결합합니다. *→ 차이는 채택이 아니라 측정이다.*
- 💵 **IDC** (연구 *"The Business Opportunity of AI"*, Microsoft 후원) — **측정하고 최적화하는** 조직은 AI에 투자한 **1달러당
  여러 달러** 규모의 수익을 보고했으며, 선도자와 후발자 간 편차가 큽니다. *→ ROI는 존재한다 — 그리고 계기화하는 자를 편애한다.*
- 🌍 **PwC** (*"Sizing the Prize"*) — AI가 2030년까지 세계 경제에 최대 **~15.7조 달러**를 더할 수 있다고 추정합니다; 그러나
  상은 가치를 **포착**하는 자의 것이지 단지 소비하는 자의 것이 아닙니다. *→ 파이는 거대하다; 그 조각은 측정하는 자의 것이다.*
- 🏆 **McKinsey** (*"The State of AI"*)와 **BCG × MIT Sloan** — 소수의 **"AI high performers"** 집단이 불균형적인 수익을
  포착합니다; 전환점은 AI를 수익이 입증된 곳의 **지표·거버넌스·재투자**와 결합할 때 옵니다. *→ 승자는 측정하고, 우선순위를 매기고,
  재배분한다.*

> **이 프레임워크가 건너는 것이 바로 그 간극입니다:** 그것은 당신을 *파일럿에서 포기하는* 쪽에서 **실제로, 입증된 결과**를 가진
> 쪽으로 옮깁니다 — BSC, 투자 분석, 다기준 의사결정으로.

> ⚠️ **정직성 참고(꼭 읽어 주세요):** 위 수치는 이 기관들의 실제 헤드라인을 반영하지만 **보고서와 백분율은 갱신됩니다** — 공식
> 자료에 인용하기 전에 **1차 출처**(Gartner Newsroom; IDC/Microsoft *Business Opportunity of AI*; PwC *Sizing the Prize*;
> McKinsey *State of AI*; MIT *State of AI in Business*)에서 정확한 값과 연도를 확인하세요. 여기서는 **방향성 있는 근거**로
> 쓰였을 뿐, 숫자 보증이 아닙니다.

---

## 💥 아무것도 하지 않는 것의 비용 (아무도 하지 않는 계산을 해보라)

**AI PRO** 구독은 좌석당 월 **20~200달러**입니다. 팀 인원 수를 곱하세요. 12개월을 곱하세요. 이제 기관들이 **이미 입증한** 것을
적용하세요: **Gartner**는 **≥ 30% 폐기**를 전망하고, **MIT**는 **대다수 파일럿이 수익을 내지 못한다**는 것을 보여줍니다. 이
총액의 큰 부분은 투자가 아니라 **순수한 출혈**입니다.

> **직접적 예시(당신 숫자로 바꿔 보세요):** 10좌석 × 월 30달러 × 12 = **연 3,600달러**. 그중 ~30%가 보이지 않는 낭비가 되면
> **연 ~1,080달러가 증발**합니다 — 작은 팀 하나에서, 단 1년에. 당신의 실제 숫자라면 충격은 더 큽니다.

그리고 아픈 부분은 이것입니다: **이 비용은 복리로 불어나고, 기다려 주지 않습니다.** 측정 없는 매달은 **돌아오지 않는** 누수의
달입니다 — 그동안 계기화한 경쟁자는 이미 **수익 나는 곳으로 자본을 재배분**하고 있습니다. 선점 우위는 일찍 만들어집니다:
**먼저 측정하는 자가 먼저 확장한다.**

시작하기에 가장 비용이 낮은 순간은 어제였습니다. 두 번째로 좋은 때는 **지금**입니다 — 그리고 그 비용은 **0달러**와 **5분**입니다.
질문은 *"측정할 여유가 있는가?"*가 아니라 ***"'측정하지 않을' 여유가 얼마나 더 있는가?"***입니다.

---

## ✨ 기능

- **📊 KPI(BSC 4관점) + API 경제:** 성숙도, 인적 자본, 재무, 토큰 효율 — `IEET`, `IOLI`, `ITR`, `IITA`, `PEUC`, `ICCA`,
  `IDLS`, `IBMT` — 그리고 **EVM**(CPI/SPI/EAC).
- **🪙 프런티어 개념:** **VRT/kTR**(토큰화 가능한 비용 회수 단위 — *"Gitman의 ㎡"*)와 **PSR**(Project Score 0–5 ⭐)로 각
  프로젝트의 건강도를 순위화.
- **🔬 운영 진단:** **VRT 5블록**, **HCI**(임계 중단 시각), **린 식스 시그마 낭비**(가중 토큰), **프롬프트 분류학 기반 환각
  RCA**(프로젝트별 병목 + 교집합).
- **💰 완전한 재무 스위트:** **NPV, IRR, MIRR, EAA(등가 연금), PI, 회수기간**(단순 및 할인), **달러화** 및 **SELIC**와
  **미국 금리**와의 비교.
- **🏆 다기준 의사결정:** **AHP-TOPSIS 2n**(이중 정규화)이 **견고성 검정**과 함께 포트폴리오의 **최고 프로젝트**를 선정하고,
  **관리 도시에**(SWOT, PESTELC, 5W4H, Pareto, GUT, Radar)를 생성.
- **🗺️ C-레벨 비주얼:** **인터랙티브 5D 지도**, 심도 도넛, 지속가능성 사분면, 추세, 그리고 적격 프로젝트의 LaTeX **피치 덱**.
- **⚙️ 실제 파이프라인:** **Langfuse → SQLite → Evidence**, **비동기 동시** 동기화와 **Rust(PyO3)** 가속 분류.
- **💳 AI FinOps:** **구독 요금제** 카탈로그(OpenAI, Anthropic, Google, Perplexity, xAI, Mistral, DeepSeek, Kimi,
  Qwen…), **환율 + IOF** 및 배부 기준(burn rate) 포함.
- **🌐 12개 언어** — 대시보드 **및 차트 이미지 내부 텍스트**(데바나가리, 히브리어, CJK 포함).

---

## 📸 스크린샷 (익명 대시보드)

> 100% 익명 데모(프로젝트는 *Project A…J*로 표시). 실제 데이터/이름은 절대 패키지에 포함되지 않습니다.

**🌐 포트폴리오 5D 지도** — 프로젝트당 5차원: **X**=토큰 · **Y**=PEUC(품질) · **Z**=PSR(건강) · **크기**=Burn Rate ·
**색상**=ICCA(지속가능성). *어디를 확장? 오른쪽/뒤, 높고 초록. 어디를 끊을까? 크고 빨강.*

![AI 프로젝트 포트폴리오 5D 지도](docs/screenshots/5d-portfolio-map.png)

**🏆 "왕관의 보석" 도시에**(AHP-TOPSIS로 선정된 프로젝트) — 동시성 Python 파이프라인으로 생성:

| SWOT | 경쟁 레이더 |
|---|---|
| ![SWOT](docs/screenshots/swot.png) | ![경쟁 레이더](docs/screenshots/radar.png) |

| PESTELC(거시환경) | GUT 매트릭스(우선순위) |
|---|---|
| ![PESTELC](docs/screenshots/pestel.png) | ![GUT](docs/screenshots/gut.png) |

| 5W4H(실행 계획) | 실패 Pareto(80/20) |
|---|---|
| ![5W4H](docs/screenshots/5w4h.png) | ![Pareto](docs/screenshots/pareto.png) |

---

## 🚀 빠른 시작 (데모, Langfuse 불필요)

**제로 리스크. 제로 비용. 5분.** 당신의 컴퓨터에서 실행하고 익명 데이터로 전체 대시보드를 보세요:

```bash
cd foundations/pipeline
pip install -r requirements.txt
cd ../evidence && npm install && cd ../pipeline
./run_all.sh --mock          # 익명 데이터 (Project A..J) -> KPI -> NPV/MIRR/EAA -> 5D -> 피치 덱 -> 대시보드
cd ../evidence && npm run dev # http://localhost:3000
```

**실제 데이터**의 경우, `foundations/pipeline/.env`에 **당신 자신의** Langfuse 키를 채우고(참조:
[`SETUP.md`](foundations/pipeline/SETUP.md)) `./run_all.sh`를 실행하세요. 각 사용자는 **자신의 계정**을 사용합니다 —
작성자 키는 패키지에 포함되지 않습니다.

---

## 🏗️ 아키텍처

```
     당신의 AI 앱               관측 가능성            Analytics-as-Code           당신
 (ChatGPT, Claude, API…)   ┌──────────────┐   ┌──────────────────┐   ┌──────────────────────┐
        │ traces           │   Langfuse   │   │  SQLite (schema  │   │  Evidence (BI as     │
        └─────────────────▶│  (SDK v4)    │──▶│  + KPI 쿼리)     │──▶│  Code) · 12개 언어   │
                           └──────────────┘   └──────────────────┘   └──────────┬───────────┘
     비동기 동시 동기화                Rust (PyO3) 분류                          │
                                                                    ┌───────────┴───────────┐
                                                                    │ AHP-TOPSIS · 도시에   │
                                                                    │ 5D · 피치 덱 (TeX)    │
                                                                    └───────────────────────┘
```

**스택:** Python 3.13 · SQLite/DuckDB · Evidence.dev (SvelteKit) · Rust + PyO3 + maturin · matplotlib ·
tectonic (LaTeX) · 이미지 i18n용 Noto/WenQuanYi 폰트.

---

## 📊 KPI 카탈로그 (70+)

샘플(전체 카탈로그는 [`foundations/KPIs_Lean6s_BSC.md`](foundations/KPIs_Lean6s_BSC.md)):

| 약어 | 이름 | 무엇에 답하는가 |
|---|---|---|
| **PSR** | Project Score Rating (0–5) | AI 프로젝트의 전반적 건강도 |
| **PEUC** | 소비 대비 유용 산출 % | 지출 중 얼마가 유용한 산출이 되었는가 |
| **IITA** | 환각 토큰 발생 지수 | 환각/재작업의 % |
| **IDLS** | 린 낭비 지수 | Muda(심각도로 가중된 토큰) |
| **VRT/kTR** | 토큰화 가능 회수 가치 | "Gitman의 ㎡" — 1k 토큰당 비용 |
| **ICCA** | 구독 비용 커버리지 지수 | 비용을 커버하는가? (>3× 건강) |
| **CPP** | 진척 포인트당 비용 | 마스터 지표(낮을수록 좋음) |

---

## 💰 투자급 재무 분석

각 프로젝트는 **투자 논거**가 됩니다: 당신의 현금흐름(CSV)에서 프레임워크가 **NPV**, **IRR**, **MIRR(프로젝트 비용으로
재투자)**, **EAA(NPV의 등가 연금)**, **PI(수익성 지수)**, **회수기간**(단순/할인)을 계산합니다 — 흐름을 **달러화**하고
**SELIC** 및 **미국 금리**와 비교합니다. BRL **및** USD 양쪽에서 **NPV > 0 이고 PI > 1**인 모든 프로젝트에 대해 LaTeX
**피치 덱**을 생성합니다. 목표는 지극히 실용적입니다: **당신의 AI 구독이 회수되는지 — 그리고 얼마나 빨리 되는지 알아내는 것.**

---

## 🏆 다기준 의사결정 (AHP-TOPSIS 2n) + 왕관의 보석 도시에

프로젝트가 여럿일 때 무엇부터 확장할까요? **AHP-TOPSIS 2n** 모델은 지표들을 기준으로 가중(일관성 비율 **CR ≤ 0.10**의
**AHP**)하고 **두 가지 정규화**(벡터 + 최소-최대)에 걸쳐 **TOPSIS**로 순위를 매기며 **견고성**(정규화 간 일치도)을 보고합니다.
승자 — **"왕관의 보석"** — 은 코드로 처음부터 생성된 완전한 **관리 도시에**(SWOT · PESTELC · 5W4H · Pareto · GUT · Radar)를,
경영진용 **Bottom-Line**과 정직한 **C-레벨 인사이트**와 함께 받습니다. **당신은 스프레드시트를 내미는 게 아닙니다. 평결을
내밉니다.**

---

## 🌐 12개 언어

대시보드, 프로젝트별 페이지 **및 차트 이미지 내부 텍스트**가 **12개 언어**로 현지화됩니다:
Português · English · Español · Français · Deutsch · 中文 · 한국어 · हिन्दी · עברית · Svenska · Русский · Suomi.
번역은 새 언어를 표준화하고 가속하는 **번역 메모리**(SDL Trados 방식)로 구동됩니다.

---

## 🙋 반론 (지금 당신이 스스로에게 묻는 질문들)

- **"시간이 없어요."** → `./run_all.sh --mock`로 5분이면 대시보드가 화면에서 돕니다. 측정은 당신이 이미 재작업과 환각에
  잃고 있는 시간을 **돌려줍니다.**
- **"너무 복잡해요."** → 한 줄이면 됩니다. 프레임워크가 ETL, 계산, 순위, 이미지를 처리하고, **당신은 평결만 읽습니다.**
- **"제 AI 운영은 작아요."** → 바로 그래서 1달러가 더 무겁습니다. 오늘은 작아도 내일은 포트폴리오 — **낭비를 확장하기 전에
  측정하세요.**
- **"저는 Langfuse를 안 써요."** → 데모는 **Langfuse 없이 100% 작동**합니다. 실제 데이터를 원하면 **당신의** 계정을
  연결하세요(제 것이 아니라).
- **"그냥 또 하나의 예쁜 대시보드 아닌가요."** → 아닙니다. **균형성과표 + 투자 분석(NPV/IRR/MIRR/EAA) + 다기준
  의사결정(AHP-TOPSIS)** — 장식이 아니라 이사회급 도구입니다.
- **"제 데이터 프라이버시는요?"** → 데모는 **100% 익명**(Project A…J)이며, 실제 데이터/이름과 키는 **패키지 밖**에 있습니다.
  당신은 **로컬**에서, **당신의** 계정으로 실행합니다.
- **"얼마인가요?"** → **무료.** 오픈 소스, 당신의 컴퓨터에서. 유일한 대가는 계속 **측정하지 않는 것** — 그리고 그건 이미 내고
  있습니다.

---

## 🧩 포함된 Skills (*build & analyze your own*)

이 저장소는 재사용 가능한 **Skills**(Claude Code)를 함께 제공합니다:

- **`measuring-ai-projects`** — AI 프로젝트의 KPI를 정의/측정/보고(이 프레임워크의 핵심).
- **`github-benchmark-analyzer`** — **모든** GitHub 저장소/프로필을 분석·벤치마크(스타, 포크, 팔로워, 해시태그, README
  스타일, 키워드, 언어)하고 선도자들의 공통점을 추출. **당신 자신의 포트폴리오를 구축하고 분석하세요** — 시장과 견주어서도.

---

## 📚 리소스 & 참고문헌 (Awesome)

이 프레임워크가 딛고 선 거인들의 어깨:

- **전략 & 측정:** Kaplan & Norton — *The Balanced Scorecard* · Peter Drucker(목표에 의한 관리).
- **린 식스 시그마:** 8대 낭비(Muda) 분류학, PDCA/Kaizen, Ishikawa/RCA.
- **기업 재무:** Lawrence Gitman — *Principles of Managerial Finance*(NPV, IRR, MIRR, PI).
- **다기준 의사결정:** Thomas Saaty(**AHP**) · Hwang & Yoon(**TOPSIS**).
- **기술 스택:** [Langfuse](https://langfuse.com)(LLM observability) · [Evidence](https://evidence.dev)
  (BI as Code) · [Rust/PyO3](https://pyo3.rs) · [Tectonic](https://tectonic-typesetting.github.io)(LaTeX).

---

## 🗺️ 로드맵

- [x] Langfuse → SQLite → Evidence 파이프라인 + Rust
- [x] 70+ KPI(BSC + API 경제 + Lean) · EVM
- [x] 재무(NPV, IRR, MIRR, EAA, PI, 회수기간, 달러화)
- [x] AHP-TOPSIS 2n + 관리 도시에(6종 도구)
- [x] 대시보드와 이미지 **12개 언어**
- [ ] 추가 관측 가능성 커넥터(OpenTelemetry, Helicone)
- [ ] 멀티테넌트 SaaS 모드 + 네이티브 스케줄링
- [ ] 정적 대시보드 게시(GitHub Pages)

---

## 🤝 기여

기여를 **적극 환영합니다**! 제안(새 KPI, 커넥터, 언어, 수정)을 설명하는 *이슈*를 열고 *풀 리퀘스트*를 보내세요. 기준: 주변과
일관된 가독성 있는 코드, 패키지 내 개인 데이터 금지(데모는 익명). 새 언어: 번역 메모리에 대상을 추가하고 생성기를 실행하세요.

## 📄 라이선스 & 저작권

© **Bruno Penedo** — 2026. 사용·학습·기여 권장; 상업적 사용/재배포는 저작자에게 문의. *(정식 OSS 라이선스를 추가할 수 있습니다
— 선호하는 것으로 이슈를 열어 주세요.)*

## 🏷️ Topics
`awesome-list` · `education` · `resources` · `computer-science` · `python` · `business-intelligence` ·
`llmops` · `finops` · `aiops` · `programming` · `development` · `lists` · `free` · `unicorns` · `dashboard` ·
`balanced-scorecard` · `langfuse` · `llm-observability` · `kpi` · `project-management`

---

⭐ **이 프레임워크가 당신의 AI 지출을 밝혀 준다면, 별을 남겨 주세요 — 그리고 이미 내고 있는 것으로부터 수익을 내기 시작하세요.**

---

**Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard** · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
