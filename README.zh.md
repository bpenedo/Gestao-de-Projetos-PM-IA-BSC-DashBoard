# 🧭 Gestão de Projetos PM IA BSC DashBoard (Build and Analyze Your Own AI Portfolio Projects)

🌐 [Português](README.md) · [English](README.en.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · **中文** · [한국어](README.ko.md) · [हिन्दी](README.hi.md) · [עברית](README.he.md) · [Svenska](README.sv.md) · [Русский](README.ru.md) · [Suomi](README.fi.md)

![Method](https://img.shields.io/badge/method-Balanced%20Scorecard-1F3A5F)
![AI](https://img.shields.io/badge/AI-LLM%20observability-45a1bf)
![Finance](https://img.shields.io/badge/finance-NPV%20·%20IRR%20·%20MIRR%20·%20PI-46a485)
![Decision](https://img.shields.io/badge/MCDM-DEMATEL%20·%20ELECTRE%20·%20PROMETHEE%20·%20MAUT%20·%20MCDA--C-8E44AD)
![Risk](https://img.shields.io/badge/risk-Monte%20Carlo%2010k%20·%20VaR%20·%20CVaR-DC143C)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-PyO3-orange?logo=rust&logoColor=white)
![Dashboard](https://img.shields.io/badge/dashboard-Evidence-236aa4)
![PDF](https://img.shields.io/badge/pitch%20deck-LaTeX-008080)
![i18n](https://img.shields.io/badge/i18n-12%20languages-0E7C86)
![status](https://img.shields.io/badge/status-v1-success)

### 💸 你每月为 AI 付费。但 AI 在给**你**回报吗？

每当 **ChatGPT、Claude、Copilot、Gemini、Perplexity、DeepSeek、Kimi、Qwen……** 从你的卡上扣款时，一个价值**百万**的问题
始终没有答案：**回报在哪里？** 到底节省了多少人时？你的钱有多少**蒸发**在幻觉、返工和等待里？哪个 AI 项目**今天值得扩张**——而
哪个正在**烧掉现金**，你却还在为「创新」鼓掌？

你没有「AI 成本」，你有一处**无声的漏洞**——而且蒙着眼。因为*「无法度量的东西，就无法管理，也无法改进」*——市场会替你度量，并把
账单递给你。

**这个框架把灯打开。** 它把 AI 订阅的**隐形支出**转化为**可度量、可比较、可审计的回报**——以**平衡计分卡**（Kaplan & Norton）、
**华尔街级别的投资分析**和**多准则决策**的严谨为标尺。这是「祈祷」与「知道」之间的差别，是为 AI 付费与用 AI **赚钱**之间的差别。

> *「无法度量的东西，就无法管理，也无法改进。」* — Kaplan & Norton

> *「以精准度量者，必以卓越建造。」* — Pierre Vernier

> *当你祈祷和学习时，别让[我的话语]离开你。你唇间吐出的每一个字、每一句话，都要念念不忘去成就一次合一。* — Aryeh Kaplan

> *纯粹的形而上学，就其本质而言居于一切形式与一切偶然之上、之外，它既非东方也非西方：它是普世的。* — René Guénon

> *认识你自己，就是认识你自身的血脉与力量。* — Harvey Spencer Lewis

> *Scientia es Lux Lucis* ∞ Sapere Aude S∴A∴☬ ☿

> 🐺 **别再在黑暗中为 AI 付费。** 当市场凭信念订阅 AI——沦为 **Gartner** 的统计数字（≥30% 的 GenAI 项目在试点后被放弃）——**你**
> 将度量每一个 token，选出获胜项目，把隐形支出转化为**可审计的回报**：NPV · IRR · MIRR · EAA · 70+ KPI · 多准则决策 · **12 种
> 语言**的 C 级仪表盘。**AI 已经是你的了，现在让它变得有利可图**——免费、在你的机器上、只需 **5 分钟**：
> `./run_all.sh --mock && npm run dev` 🔥

> 📖 **主文档：** **[`foundations/README.md`](foundations/README.md)** ·
> ⚙️ **配置（使用你自己的密钥）：** [`foundations/pipeline/SETUP.md`](foundations/pipeline/SETUP.md) ·
> 📊 **KPI：** [`foundations/KPIs.md`](foundations/KPIs.md) / [`foundations/KPIs_README.md`](foundations/KPIs_README.md)

---

## 📑 目录

- [🌅 为何这将改变格局](#-为何这将改变格局)
- [📈 证据（Gartner · IDC · PwC · McKinsey · MIT）](#-证据gartner--idc--pwc--mckinsey--mit)
- [💥 不作为的代价](#-不作为的代价算一算没人算的那笔账)
- [✨ 功能](#-功能)
- [📸 截图（匿名仪表盘）](#-截图匿名仪表盘)
- [🚀 快速开始](#-快速开始演示无需-langfuse)
- [🏗️ 架构](#️-架构)
- [📊 KPI 目录](#-kpi-目录70)
- [💰 投资级财务分析](#-投资级财务分析)
- [🏆 多准则决策 + 档案](#-多准则决策ahp-topsis-2n-皇冠明珠档案)
- [🎲 蒙特卡洛 — 平均值掩盖的风险](#-蒙特卡洛--平均值掩盖的风险)
- [🧮 五种决策学派，一个裁决](#-五种决策学派一个裁决)
- [🔬 信号在上游 —— 杠杆就藏在那里](#-信号在上游--杠杆就藏在那里)
- [🌐 12 种语言](#-12-种语言)
- [🙋 异议（你此刻正在问自己的问题）](#-异议你此刻正在问自己的问题)
- [🧩 内置 Skills](#-内置-skillsbuild--analyze-your-own)
- [📚 资源与参考](#-资源与参考awesome)
- [🗺️ 路线图](#️-路线图)
- [🤝 贡献](#-贡献)
- [📄 许可与署名](#-许可与署名)

---

## 🌅 为何这将改变格局

**在 AI 时代，人分两种。** 第一种订阅一切、大手笔花钱，然后**祈祷**成功——并壮大了那条残酷的统计：项目死在试点。第二种做的，是华尔街
对任何严肃资产所做的：**度量、比较、排序、再配置**——把每一美元订阅变成**复利回报**。她们之间唯一的差别**不是天赋，也不是预算，
而是「仪表化」。**

生成式 AI 造出了一类新的经常性支出——**订阅与 token**——并随之带来了这十年最昂贵的浪费：**隐形的浪费。** 看不见，就修不了；不度量，
就扩不了；证明不了，董事会就不批。

**这个项目把你从第一部落带到第二部落。** 它把每一个 AI 项目当作**金融资产**来仪表化，并在**平衡计分卡**、**投资分析（NPV、IRR、
MIRR、EAA、PI、回收期）**和 **精益六西格玛** 下度量它——甚至用多准则模型（**AHP-TOPSIS 2n**）**选出你投资组合中最好的项目**。
不透明的月度账单变成一份**可审计的投资论证**：你用数字看清在哪里扩张、在哪里砍掉、订阅在哪几**周**内回本——又在哪里毫无遮盖地
失血。

我们是新疆域的**拓荒者**——**人工智能与价值会计之间的边界**。像绘制未标记之地的探险家，这个框架就是那枚**指南针**（🧭），把订阅的
迷雾化为**清晰的回报航线**：每个 token 是一英里，每个项目是一次奔向利润的远征。原本盲目的成本处，诞生**可度量的机会**；原本
一张死表格处，绽放**鲜活的投资论证**。

> **承诺：** 把*为 AI 付费的人*变成*用 AI 赚钱的人*——把*使用 AI 的人*变成**开创性地驾驭、度量并放大它的人**。用数字，而非用信念。

---

## 📈 证据（Gartner · IDC · PwC · McKinsey · MIT）

别只信我。**去信那些研究此事数十年的机构**——它们的结论一致：**AI 创造巨大价值，但只交付给那些度量并治理的人。** 「用 AI 却不
驾驭 AI」的人沦为放弃统计；而仪表化回报的人**赢得奖赏**。

- 🧭 **Gartner** — 预测**到 2025 年底，≥ 30% 的生成式 AI 项目会在概念验证后被放弃**，核心原因是**业务价值不清晰**（此外还有劣质
  数据、成本攀升与控制薄弱）。*→ 没有度量，项目就死在试点。*
- 🔬 **MIT**（报告 *「The GenAI Divide / State of AI in Business 2025」*，NANDA 计划）— 广泛报道称**绝大多数企业 GenAI 试点
  对损益没有可度量的影响**；少数交付价值者，是把 AI 与**流程和度量**结合。*→ 差别在于度量，而非采用。*
- 💵 **IDC**（研究 *「The Business Opportunity of AI」*，由微软赞助）— **度量并优化**的组织报告，每投入 **1 美元** AI 就有
  **数美元**量级的回报，且领先者与落后者之间差异巨大。*→ ROI 确实存在——并偏爱仪表化的人。*
- 🌍 **PwC**（*「Sizing the Prize」*）— 估计到 2030 年 AI 可为全球经济增加高达 **~15.7 万亿美元**；但奖赏归于**捕获**价值者，
  而非仅仅消费者。*→ 蛋糕巨大，而那块属于度量的人。*
- 🏆 **McKinsey**（*「The State of AI」*）与 **BCG × MIT Sloan** — 少数派 **「AI high performers」** 捕获了不成比例的回报；
  转折点在于把 AI 与已被证明有回报之处的**指标、治理与再投资**耦合起来。*→ 赢家度量、排序并再配置。*

> **这道鸿沟，正是本框架要跨越的：** 它把你从*在试点放弃*的一侧，带到拥有**实打实且经证明结果**的一侧——用 BSC、投资分析与多准则决策。

> ⚠️ **诚实声明（请阅读）：** 上述数字反映这些机构的真实报道，但**报告与百分比会更新**——在正式材料中引用前，请到**原始来源**
> （Gartner Newsroom；IDC/Microsoft *Business Opportunity of AI*；PwC *Sizing the Prize*；McKinsey *State of AI*；
> MIT *State of AI in Business*）核实确切数值与年份。此处它们用作**方向性依据**，而非数字保证。

---

## 💥 不作为的代价（算一算没人算的那笔账）

一份 **AI PRO** 订阅每月每席位在 **20 至 200 美元**之间。乘以团队人数，再乘以 12 个月。现在套用机构**已经证明**的事实：**Gartner**
预测**≥ 30% 被放弃**，**MIT** 显示**多数试点没有回报**。这笔总额中很大一块不是投资——是**纯粹的失血**。

> **直接举例（换成你自己的数字）：** 10 席位 × 30 美元/月 × 12 = **3,600 美元/年**。若 ~30% 变成隐形浪费，就是
> **~1,080 美元/年在蒸发**——仅一个小团队，仅一年。换成你的真实数字，惊吓更大。

而最扎心的部分是：**这项成本会复利，且不会等你。** 每一个不度量的月份，都是一个**回不来**的漏损月份——而那位已仪表化的竞争者，
**早已把资本再配置到能赚钱的地方**。先发优势要趁早建立：**谁先度量，谁先扩张。**

开始的最低成本时刻是昨天。第二好的是**现在**——而它只花 **0 美元**和 **5 分钟**。问题不是*「我付得起去度量吗？」*，而是
***「我还能付得起多久『不』度量？」***

---

## ✨ 功能

- **📊 KPI（BSC 四视角）+ API 经济学：** 成熟度、人力资本、财务与 token 效率——`IEET`、`IOLI`、`ITR`、`IITA`、`PEUC`、`ICCA`、
  `IDLS`、`IBMT`——外加 **EVM**（CPI/SPI/EAC）。
- **🪙 前沿概念：** **VRT/kTR**（可代币化的成本回收单位——*「Gitman 的每平方米」*）与 **PSR**（Project Score 0–5 ⭐），用于给每个
  项目的健康度排名。
- **🔬 运营诊断：** **VRT 五区块**、**HCI**（关键中断时刻）、**精益六西格玛浪费**（加权 token）与**按提示词分类学的幻觉 RCA**
  （每项目瓶颈 + 交集）。
- **💰 完整财务套件：** **NPV、IRR、MIRR、EAA（等额年金）、PI、回收期**（简单与折现）、**美元化**及与 **SELIC** 和**美国利率**的对比。
- **🏆 多准则决策：** **AHP-TOPSIS 2n**（双重归一化）以**稳健性检验**选出组合中的**最佳项目**——并生成**管理档案**
  （SWOT、PESTELC、5W4H、Pareto、GUT、Radar）。
- **🗺️ C 级视觉：** **交互式 5D 地图**、带深度的甜甜圈图、可持续性象限、趋势，以及合格项目的 LaTeX **pitch deck**。
- **⚙️ 真实管线：** **Langfuse → SQLite → Evidence**，具备**异步并发**同步与 **Rust（PyO3）**加速的分类。
- **💳 AI FinOps：** **订阅计划**目录（OpenAI、Anthropic、Google、Perplexity、xAI、Mistral、DeepSeek、Kimi、Qwen……），含
  **汇率 + IOF** 与分摊基准（burn rate）。
- **🌐 12 种语言**——仪表盘**以及图表图片内的文字**（含天城文、希伯来文与 CJK）。

---

## 📸 截图（匿名仪表盘）

> 100% 匿名演示（项目显示为 *Project A…J*）。真实数据/名称从不随包分发。

**🌐 组合 5D 地图** — 每个项目 5 个维度：**X**=token · **Y**=PEUC（质量）· **Z**=PSR（健康）· **大小**=Burn Rate ·
**颜色**=ICCA（可持续性）。*在哪里扩张？右/后、高且绿。在哪里砍掉？大且红。*

![AI 项目组合 5D 地图](docs/screenshots/5d-portfolio-map.png)

**🏆「皇冠明珠」档案**（由 AHP-TOPSIS 选出的项目）— 由并发 Python 管线生成：

| SWOT | 竞争雷达 |
|---|---|
| ![SWOT](docs/screenshots/swot.png) | ![竞争雷达](docs/screenshots/radar.png) |

| PESTELC（宏观环境） | GUT 矩阵（优先级） |
|---|---|
| ![PESTELC](docs/screenshots/pestel.png) | ![GUT](docs/screenshots/gut.png) |

| 5W4H（行动计划） | 故障 Pareto（80/20） |
|---|---|
| ![5W4H](docs/screenshots/5w4h.png) | ![Pareto](docs/screenshots/pareto.png) |

---

## 🚀 快速开始（演示，无需 Langfuse）

**零风险。零成本。5 分钟。** 在你的机器上运行，用匿名数据查看完整仪表盘：

```bash
cd foundations/pipeline
pip install -r requirements.txt
cd ../evidence && npm install && cd ../pipeline
./run_all.sh --mock          # 匿名数据 (Project A..J) -> KPI -> NPV/MIRR/EAA -> 5D -> pitch deck -> 仪表盘
cd ../evidence && npm run dev # http://localhost:3000
```

若要使用**真实数据**，请在 `foundations/pipeline/.env` 中填入**你自己的** Langfuse 密钥（见
[`SETUP.md`](foundations/pipeline/SETUP.md)）并运行 `./run_all.sh`。每位用户使用**自己的账户**——包内不含作者密钥。

---

## 🏗️ 架构

```
     你的 AI 应用                 可观测性               Analytics-as-Code            你
 (ChatGPT, Claude, API…)   ┌──────────────┐   ┌──────────────────┐   ┌──────────────────────┐
        │ traces           │   Langfuse   │   │  SQLite (schema  │   │  Evidence (BI as     │
        └─────────────────▶│  (SDK v4)    │──▶│  + KPI 查询)     │──▶│  Code) · 12 种语言   │
                           └──────────────┘   └──────────────────┘   └──────────┬───────────┘
     异步并发同步                     Rust (PyO3) 分类                          │
                                                                    ┌───────────┴───────────┐
                                                                    │ AHP-TOPSIS · 档案     │
                                                                    │ 5D · Pitch deck (TeX) │
                                                                    └───────────────────────┘
```

**技术栈：** Python 3.13 · SQLite/DuckDB · Evidence.dev (SvelteKit) · Rust + PyO3 + maturin · matplotlib ·
tectonic (LaTeX) · 用于图片 i18n 的 Noto/WenQuanYi 字体。

---

## 📊 KPI 目录（70+）

样例（完整目录见 [`foundations/KPIs_Lean6s_BSC.md`](foundations/KPIs_Lean6s_BSC.md)）：

| 缩写 | 名称 | 回答什么 |
|---|---|---|
| **PSR** | Project Score Rating (0–5) | AI 项目的整体健康度 |
| **PEUC** | 每消耗的有用交付百分比 | 支出中有多少变成了有用交付 |
| **IITA** | 幻觉 token 发生率指数 | 幻觉/返工的百分比 |
| **IDLS** | 精益浪费指数 | Muda（按严重度加权的 token） |
| **VRT/kTR** | 可代币化回收价值 | 「Gitman 的每平方米」——每 1k token 的成本 |
| **ICCA** | 每订阅成本覆盖指数 | 是否覆盖成本？（>3× 为健康） |
| **CPP** | 每进度点成本 | 主指标（越低越好） |

---

## 💰 投资级财务分析

每个项目都成为一份**投资论证**：从你的现金流（CSV）出发，框架计算 **NPV**、**IRR**、**MIRR（按项目成本再投资）**、**EAA
（NPV 的等额年金）**、**PI（盈利指数）**与**回收期**（简单/折现）——把现金流**美元化**，并与 **SELIC** 和**美国利率**对比。它为每一个
**NPV > 0 且 PI > 1**（在 BRL **与** USD 两种货币下）的项目生成 LaTeX **pitch deck**。目标极其务实：**弄清你的 AI 订阅是否
回本——以及多快回本。**

---

## 🏆 多准则决策（AHP-TOPSIS 2n）+ 皇冠明珠档案

有多个项目时，先扩张哪个？**AHP-TOPSIS 2n** 模型把各指标作为准则加权（用 **AHP**，一致性比率 **CR ≤ 0.10**），并在**两种归一化**
（向量 + 最小-最大）下用 **TOPSIS** 排名，报告**稳健性**（两种归一化之间的一致度）。获胜者——**「皇冠明珠」**——获得一份由代码从零
生成的完整**管理档案**（SWOT · PESTELC · 5W4H · Pareto · GUT · Radar），附带高管级 **Bottom-Line** 与诚实的 **C 级洞察**。
**你呈上的不是一张表格。你呈上的是一份裁决。**

---

## 🎲 蒙特卡洛 — 平均值掩盖的风险

**平均**为正的 NPV 保护不了任何人。平均值是金融里最舒适的谎言：它描述的场景也许永远不会发生。决定你命运的是**尾部**——那个糟糕的日子。

本框架为每个项目模拟 **10,000 个未来**：每一笔现金流都成为
**随机变量**，整个组合逐次迭代重算。最后你得到的不是一个数字，而是**你金钱的完整分布**：

- **`P(NPV < 0)`** — 真实的亏损概率。没人给你看的那个数字。
- **VaR 5%** — 最坏的合理情形：*「在 20 个未来中的 19 个里，我至少赚这么多。」*
- **CVaR 5%** — 灾难真的发生时，平均要付出多少代价。
- **敏感性龙卷风图** — 多元回归与皮尔逊相关：究竟哪个变量在真正牵动你的 NPV。
- **20 种输入分布**、经校验的**相关矩阵**（Iman-Conover，精确保留边缘分布）以及 **1% 至 99% 的百分位**，
  以及 100 类直方图。

固定随机种子：再跑一次得到**完全相同**的结果。可审计——而非「魔法」。

> **转折点：** 你不再挑 NPV 最高的项目，而是挑**在坏情形下仍能存活的项目**。这就是风险管理——投资者与赌徒的分界线。

![Histograma de Monte Carlo do VPL — 10.000 iterações, 100 classes](docs/screenshots/mc-histograma.png)

| NPV 的累积分布 | 敏感性龙卷风图 |
|---|---|
| ![NPV 的累积分布](docs/screenshots/mc-acumulado.png) | ![敏感性龙卷风图](docs/screenshots/mc-tornado.png) |

---

## 🧮 五种决策学派，一个裁决

一个方法可能出错。五个方法一致，则不会。

依循 **John (2025)** 的架构 —— *Integration of DEMATEL with Other MCDM Methods* —— **DEMATEL** 绘制准则之间的因果结构，
把**因**（可施力的杠杆）与**果**（既有作为的温度计）分开。由这些影响回路生成**权重**：不是拍脑袋定的，而是**由问题结构导出的**。
它们供给四个相互竞争的学派：

| 方法 | 学派 | 它在问什么 |
|---|---|---|
| **ELECTRE I** | 级别高于关系 | 「谁胜过谁——谁能不被支配地存活？」 |
| **PROMETHEE II** | 级别高于关系 | 「每个项目的净偏好流是多少？」 |
| **MAUT** | 效用 | 「哪个能最大化风险厌恶决策者的效用？」 |
| **MCDA-C** | 建构主义 | 「谁高于「好」的水平——谁低于「中性」？」 |
| **AHP-TOPSIS 2n** | 到理想解的距离 | 「在两种归一化下，谁离理想解最近？」 |

最终赢家来自五者的 **Borda 共识**，并已由蒙特卡洛做过**风险调整**。当各方法**意见不一**时，仪表盘会把分歧显示出来——
因为那正是信息：该选择对决策学派敏感，值得决策者亲自过目。

| DEMATEL — 因 × 果 | 各方法下的排名 |
|---|---|
| ![DEMATEL — 因 × 果](docs/screenshots/dematel.png) | ![各方法下的排名](docs/screenshots/mcdm-metodos.png) |

### 💼 这在你的日常中改变了什么 —— 从自由职业者到大型企业

无论你付的是 **PRO 计划的每月 20 美元**，还是 **20 万美元的企业合同**：浪费的数学是同一套，变的只是零的个数。

| | **中小企业 / 自由职业者** | **大型企业** |
|---|---|---|
| **真正的痛点** | 3 个订阅、零可见性、现金紧张 | 40 个 AI 试点，无一能归因到损益 |
| **蒙特卡洛给出** | *「这个项目有 12% 的概率亏损，糟糕的那个月要花 3,400 美元」* | 按业务单元的 VaR/CVaR：可聚合、可审计的风险，而非轶事 |
| **多准则决策给出** | 用现有的钱，先扩张 3 个项目中的哪一个 | 40 个试点中哪个变成产品 —— 方法公开，可在委员会上站得住脚 |
| **第二天的收益** | 本周就砍掉那个回不了本的订阅 | 依**证据**重新分配预算，而非依内部政治 |

**实操上：** **龙卷风图**指出真正牵动结果的变量 —— 也就是**你下一个小时该投在哪里**。**DEMATEL** 揭示：降低幻觉（IITA）是**因**，
不是症状 —— 在那里发力，NPV、IRR 和风险会*一起*变好。这就是 AI 管理从「意见」变成「**工程**」。


---

## 🔬 信号在上游 —— 杠杆就藏在那里

这是我测量框架本身时发现的：NPV 的敏感性龙卷风图返回的竟然**恰好**是
`1.0 · 0.9091 · 0.8264 · 0.7513…` —— 折现因子 `1/(1+i)ᵗ`。因为 NPV 对现金流是**线性**的，只模拟现金流除了折现率之外
什么也告诉不了你。**真正的随机信号在上游：在 token 里。**

### 1️⃣ 别再拍脑袋定分布。把它拟合到你的数据上。

十一种候选分布以**最大似然**拟合你真实的 token 消耗序列（`logs_langfuse`）。**AIC 最小者**获胜 —— AIC 会惩罚每一个多余
参数、防止过拟合 —— 而 **Kolmogorov-Smirnov** 检验衡量拟合优度。这正是经典的*将分布拟合到数据*，
它揭示消耗的**厚尾**：有些提示词的成本是典型值的 10 倍，而正是这条尾巴撑爆预算 —— 对只看平均值的人完全不可见。

**而当拟合很差时，框架会大声喊出来。** 若 KS 的 p 值低于 0.05，界面会以红色标注 `拟合不佳`，而不是假装精确。
一个诚实的数字胜过一个漂亮的数字。

![将分布拟合到真实 token —— 11 个候选、按 AIC 选择、以 Kolmogorov-Smirnov 检验拟合优度](docs/screenshots/ajuste-distribuicoes.png)

### 2️⃣ 权重差 2 个百分点，你的排名还站得住吗？

任何多准则方法给出赢家时，都隐含着**100% 的置信度**。但准则权重是估计值，不是被揭示的真理。如果 IITA 权重上的两个百分点
就能让第一和第二互换，那么这个「赢家」不过是标定的产物。

于是我们用 **Dirichlet** 扰动 DEMATEL 的权重 —— `w' ~ Dir(κ·w)`，它恰好生活在单纯形上并保持 `E[w'] = w`，
即**无偏扰动** —— 然后重排 **2,000 次**。裁决的性质就变了：

> *「Project C 最好」* ⟶ **「Project C 在 99.9% 的合理偏好宇宙中胜出」**

这是一个**关于决策本身的置信区间**。它还揭穿了共识所掩盖的事：在下图中，**PROMETHEE II 仅在 25.4% 的宇宙里选出该领先者**。
四个学派同意，一个正面反对。这不是噪声 —— 这是警示：你的选择取决于你更偏爱*级别高于关系*还是*效用*。
任何单一排名都不会告诉你这一点。

![以 Dirichlet 扰动检验排名稳健性 —— 胜出概率与学派间的分歧](docs/screenshots/robustez-dirichlet.png)

### ⚡ 具体的杠杆

| 资源 | 之前 | 之后 |
|---|---|---|
| **时间** | 为「该扩张哪个项目」争论数周 | 裁决自带概率 —— 一次会议就能结束争论 |
| **算力** | 10,000 次迭代 × 10 个项目，NumPy 向量化 | 数秒，在你自己的机器上，无需云、无需花钱 |
| **资本** | 凭信念分配预算 | 依 `P(胜出)` 与 `VaR` 分配 —— 最坏情形已定价 |
| **声誉** | *「我觉得这个最好」* | *「它在 99.9% 的情形中胜出；而持异议的是这个方法，原因如下」* |
| **可审计性** | 无法复现的表格 | 固定随机种子：任何人重跑都得到**完全相同**的数字 |

### 💼 从每月 20 美元的套餐到 20 万美元的合同

**如果你是自由职业者或中小企业：** 拟合出的分布会在糟糕的月份到来之前告诉你**它会花掉多少 token 成本** ——
而稳健性告诉你，把精力转到另一个项目是否真的值得，还是说两者在误差范围内其实打平。你不再在现金紧张时盲目优化。

**如果你是大型企业：** `P(胜出)` 正是投资委员会缺失的那一块。它把*「A 团队力挺项目 X」*变成
**「在 99.9% 站得住脚的权重标定下，项目 X 都胜出；唯一持异议的学派是级别高于关系，依据的是准则 Y」**。
政治争论变成**技术讨论** —— 而 CFO 拿到了一个经得起审计的数字。

> **最后的转折：** 框架不再只度量**金钱**的风险，而开始度量**决策本身**的风险。全世界能做到这一点的地方寥寥无几。

---

## 🌐 12 种语言

仪表盘、各项目页面**以及图表图片内的文字**均已本地化为**12 种语言**：
Português · English · Español · Français · Deutsch · 中文 · 한국어 · हिन्दी · עברית · Svenska · Русский · Suomi。
翻译由**翻译记忆库**（SDL Trados 风格）驱动，使新语言标准化并加速。

---

## 🙋 异议（你此刻正在问自己的问题）

- **「我没时间。」** → 用 `./run_all.sh --mock` 五分钟，仪表盘就在你屏幕上运行。度量会**归还**你已经在返工与幻觉上损失的时间。
- **「太复杂了。」** → 一行命令。框架完成 ETL、计算、排名与图像；**你只需读裁决。**
- **「我的 AI 规模很小。」** → 正因如此，每一美元更重。今天小，明天就是组合——**在把浪费扩张之前先度量。**
- **「我不用 Langfuse。」** → 演示**完全无需 Langfuse**。想用真实数据时，你接入**你自己的**账户（绝非我的）。
- **「不过是又一个漂亮仪表盘。」** → 不。它是**平衡计分卡 + 投资分析（NPV/IRR/MIRR/EAA）+ 多准则决策（AHP-TOPSIS）**——董事会
  级的工具，而非装饰。
- **「我的数据隐私呢？」** → 演示**100% 匿名**（Project A…J）；真实数据/名称与密钥都在**包外**。你在**本地**运行，用**你自己的**账户。
- **「多少钱？」** → **零。** 开源，在你自己的机器上。唯一的代价是继续**不度量**——而这笔，你已经在付了。

---

## 🧩 内置 Skills（*build & analyze your own*）

本仓库内置可复用的 **Skills**（Claude Code）：

- **`measuring-ai-projects`** — 为 AI 项目定义/度量/报告 KPI（本框架的核心）。
- **`github-benchmark-analyzer`** — 对**任意** GitHub 仓库/主页做分析与基准（星标、fork、关注者、话题标签、README 风格、关键词、
  语言），提炼领先者的共性。**构建并分析你自己的组合**——甚至对标市场。

---

## 📚 资源与参考（Awesome）

本框架所立足的巨人之肩：

- **战略与度量：** Kaplan & Norton — *The Balanced Scorecard* · Peter Drucker（目标管理）。
- **精益六西格玛：** 8 大浪费（Muda）分类学、PDCA/Kaizen、Ishikawa/RCA。
- **公司金融：** Lawrence Gitman — *Principles of Managerial Finance*（NPV、IRR、MIRR、PI）。
- **多准则决策：** Thomas Saaty（**AHP**）· Hwang & Yoon（**TOPSIS**）。
- **技术栈：** [Langfuse](https://langfuse.com)（LLM observability）· [Evidence](https://evidence.dev)
  （BI as Code）· [Rust/PyO3](https://pyo3.rs) · [Tectonic](https://tectonic-typesetting.github.io)（LaTeX）。

---

## 🗺️ 路线图

- [x] Langfuse → SQLite → Evidence 管线 + Rust
- [x] 70+ KPI（BSC + API 经济学 + Lean）· EVM
- [x] 财务（NPV、IRR、MIRR、EAA、PI、回收期、美元化）
- [x] AHP-TOPSIS 2n + 管理档案（6 种工具）
- [x] 仪表盘与图片支持 **12 种语言**
- [ ] 更多可观测性连接器（OpenTelemetry、Helicone）
- [ ] 多租户 SaaS 模式 + 原生调度
- [ ] 静态仪表盘发布（GitHub Pages）

---

## 🤝 贡献

**非常欢迎**贡献！请开一个 *issue* 描述你的提案（新 KPI、连接器、语言、修复），并提交 *pull request*。规范：代码可读、与周边一致，
包内不含个人数据（演示为匿名）。新增语言：把目标加入翻译记忆库并运行生成器。

## 📄 许可与署名

© **Bruno Penedo** — 2026。鼓励使用、学习与贡献；商业使用/再分发请咨询作者。*（可添加正式 OSS 许可证——开个 issue 说明你的偏好。）*

## 🏷️ Topics
`awesome-list` · `education` · `resources` · `computer-science` · `python` · `business-intelligence` ·
`llmops` · `finops` · `aiops` · `programming` · `development` · `lists` · `free` · `unicorns` · `dashboard` ·
`balanced-scorecard` · `langfuse` · `llm-observability` · `kpi` · `project-management`

---

⭐ **如果这个框架照亮了你的 AI 支出，请留个星——并开始从你已经在付费的东西上获利。**

---

**Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard** · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
