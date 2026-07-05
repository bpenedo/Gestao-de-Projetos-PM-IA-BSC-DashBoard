# 🧭 Framework VPL — BSC 패널 및 대시보드를 갖춘 AI 프로젝트 관리(PM)

🌐 [Português](README.md) · [English](README.en.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [中文](README.zh.md) · **한국어** · [हिन्दी](README.hi.md) · [עברית](README.he.md) · [Svenska](README.sv.md) · [Русский](README.ru.md) · [Suomi](README.fi.md)

![Method](https://img.shields.io/badge/method-Balanced%20Scorecard-1F3A5F)
![AI](https://img.shields.io/badge/AI-LLM%20observability-45a1bf)
![Finance](https://img.shields.io/badge/finance-NPV%20·%20IRR%20·%20PI-46a485)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-PyO3-orange?logo=rust&logoColor=white)
![Dashboard](https://img.shields.io/badge/dashboard-Evidence-236aa4)
![PDF](https://img.shields.io/badge/pitch%20deck-LaTeX-008080)
![status](https://img.shields.io/badge/status-v1-success)

> **모든 AI 프로젝트를 처음부터 끝까지 측정**하기 위한 프레임워크 — 토큰 소비에서
> 재무 수익까지 — **균형성과표(Balanced Scorecard)**(Kaplan & Norton)의 4가지 관점에 따라.
>
> *"측정되지 않는 것은 관리할 수도, 개선할 수도 없다."*

> 📖 **주요 문서:** **[`foundations/README.md`](foundations/README.md)** ·
> ⚙️ **설정(본인 키 사용):** [`foundations/pipeline/SETUP.md`](foundations/pipeline/SETUP.md) ·
> 📊 **KPI:** [`foundations/KPIs.md`](foundations/KPIs.md) / [`foundations/KPIs_README.md`](foundations/KPIs_README.md)

---

## ✨ 프레임워크가 제공하는 것

- **KPI(BSC 4가지 관점):** 성숙도, 인적 자본, 재무 + API 경제성
  (`IEET`, `IOLI`, `ITR`, `IITA`, `PEUC`, `ICCA`, `IDLS`, `IBMT`) 및 **EVM**(CPI/SPI/EAC).
- **최전선 개념:** **VRT/kTR**(토큰화 가능한 비용 회수 단위 — "Gitman의 m²")
  와 **PSR**(프로젝트 점수 0–5 ⭐).
- **운영 진단:** **VRT 5블록**, **HCI**(핵심 중단 시간대),
  **린 식스 시그마 낭비**, **프롬프트 분류별 환각 RCA(근본 원인 분석)**(프로젝트별 병목 + 교집합).
- **재무:** **NPV, IRR, PI, 회수기간**(단순/할인), **달러화**, 그리고 **SELIC** 및 **미국 금리**와의 비교.
- **시각화:** 포트폴리오 **5D 지도**, **Evidence 대시보드**(BI as Code), 적격 프로젝트의 LaTeX **피치덱**.
- **파이프라인:** **Langfuse → SQLite → Evidence**, **비동기 동시** 동기화 및 **Rust(PyO3)**로 가속된 분류.

## 🚀 빠른 시작(데모, Langfuse 불필요)
```bash
cd foundations/pipeline
pip install -r requirements.txt
cd ../evidence && npm install && cd ../pipeline
./run_all.sh --mock          # 익명 데이터 (Project A..J) -> KPI -> NPV -> 5D -> pitch decks -> 대시보드
cd ../evidence && npm run dev # http://localhost:3000
```
실제 데이터의 경우: `foundations/pipeline/.env`에 **본인의** Langfuse 키를 입력하고
([`SETUP.md`](foundations/pipeline/SETUP.md) 참조) `./run_all.sh`를 실행하세요.

## 🗂️ 구조
```
foundations/
├── README.md            ← 주요 문서
├── KPIs.md · KPIs_README.md · BSC_Dashboard.md · solucoes_relatorios.md
├── pipeline/            ← ETL, 쿼리, seed, Rust, 생성기(5D, 피치덱), SETUP.md
├── evidence/            ← Evidence 대시보드(BI as Code)
└── pitchdeck/           ← 표준 템플릿 + 생성된 피치덱
```

## 🏷️ Topics
`project-management` · `kanban` · `task-management` · `dashboard` · `executive-dashboard` ·
`business-intelligence` · `analytics` · `data-visualization` · `kpi` · `metrics` ·
`balanced-scorecard` · `llm` · `ai` · `llm-observability` · `llmops` · `langfuse` · `roi` ·
`agile` · `scrum` · `python`

---

**Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard** · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
