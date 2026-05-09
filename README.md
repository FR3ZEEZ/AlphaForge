# AlphaForge · 阿尔法锻造

> **AI-Driven Comprehensive Investment Analysis Framework**
> **AI驱动的综合投资分析系统**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

AlphaForge is a systematic investment analysis framework powered by LLM (Claude). It transforms raw market data into structured investment decisions through a **21-step pipeline** — macro analysis, sector momentum scanning, multi-round adversarial debate, and three-strategy portfolio construction.

阿尔法锻造是一个由大语言模型驱动的系统性投资分析框架。通过 **21 步流水线** — 宏观分析、板块动量扫描、多轮对抗辩论、三策略组合构建 — 将原始市场数据转化为结构化投资决策。

---

## ✨ Features / 功能

- **21-Step Automated Pipeline** — From macro environment to final stock picks, all steps are structured and traceable
- **Multi-Round Adversarial Debate** — Bull vs Bear 4-round debate to stress-test every hypothesis before recommendation
- **Three Parallel Strategies** — Momentum chasing | High-elasticity speculation | Value with safety margin
- **Dual Data Source** — AKShare for precise structured data (sector flows, macro, financials) + WebSearch for qualitative intelligence
- **Self-Check Mechanism** — Every recommendation is automatically verified against predefined screening criteria
- **Bilingual Output** — Both `.md` and `.html` reports generated automatically

---

## 📋 Workflow Overview / 工作流程

```
User Judgment → Read History → [AKShare Data] → Macro Summary 
→ Trend Detection → [Parallel] Sector Momentum + Overseas Mapping + Negative Signals 
→ Industry Deep Dive → Catalyst Timeline → [4-Round Adversarial Debate] 
→ AI Synthesis → Sector Recommendation → 6 Candidates/Sector 
→ Wiki Cross-Validation → 3 Strategies × 3 Stocks → Cross-Sector Final Picks 
→ Self-Check → Sync Config → Output .md + .html
```

### 21 Steps / 21 步详解

| Step | Phase | Description |
|:----:|-------|-------------|
| 1-5 | **Input** | Read user judgment, holdings, config, last report |
| 6 | **Data** | Read AKShare structured data (macro/sector/financials) |
| 7 | **Macro** | Liquidity, risk appetite, market style summary |
| 8 | **Trend** | Detect changes vs last report |
| 9 | **Scan** | [Parallel] Sector momentum + Overseas mapping + Negative signals |
| 10 | **Industry** | Supply-demand, orders, macro, expectations gap analysis |
| 11 | **Catalyst** | Timeline for next 1-2 months |
| 12 | **Debate** | Bull vs Bear 4-round adversarial debate |
| 13 | **Synthesis** | Consensus/disagreement extraction, confidence adjustment |
| 14 | **Recommend** | AI recommends sectors based on all data (independent of user hints) |
| 15 | **Candidates** | 6 candidates per sector with confidence levels |
| 16 | **Validation** | Cross-validate with knowledge base (Obsidian wiki) |
| 17 | **Strategies** | 3 stocks per strategy per sector → 🏆 1 final pick |
| 18 | **Cross-Sector** | Final picks across sectors: Momentum 2 | Elasticity 3 | Safety 4 |
| 19 | **Self-Check** | Verify every pick against strategy screening criteria |
| 20 | **Sync** | Update thought outline + strategy config |
| 21 | **Output** | Save `.md` + `.html`, return summary |

---

## 🎯 Three Strategies / 三策略体系

All strategies follow **Buy the rumor, sell the news**:

### 🏆 Momentum Chasing / 追最强
- **定位**：当前市场最强板块+最强个股，不潜伏不抄底不猜方向
- **选股**：板块业绩增速TOP5，涨幅龙头或资金龙头，1个月内有明确催化
- **排除**：PE>300x纯概念、连续亏损无收入增长、日均成交<5亿

### 🚀 High-Elasticity / 高弹性博弈
- **定位**：小市值+高经营杠杆+刚过拐点，赔率优先
- **市值**：50-1000亿
- **弹性来源**：①经营杠杆(收入增10%→利润增30%+) ②产能释放(产量翻倍) ③价格弹性(价涨7%→利润涨20%+)

### 🛡️ Value with Safety Margin / 弹性+安全边际
- **定位**：好行业+好公司+合理价格
- **PE**：15-30x
- **壁垒**：细分行业前3，资源/技术/牌照壁垒
- **逻辑持续性**：半衰期>6个月，经营现金流为正

---

## 🔧 Quick Start / 快速开始

### Prerequisites / 前置要求

```bash
# Install dependencies / 安装依赖
pip install akshare pandas

# For LLM integration, configure your CLAUDE.md
# 集成 AI 需配置 CLAUDE.md 文件
```

### Usage / 使用

```bash
# 1. Fetch latest market data with AKShare
python scripts/run_all.py

# 2. Run the analysis via AI (e.g., Claude Code)
# Input: 综投 <your market judgment>
```

### Configuration / 配置

Edit `策略配置.md` to control:

```yaml
# Enable/disable AKShare data source
akshare_enabled: false  # true = CSV data, false = pure WebSearch

# Toggle debate module
debate_enabled: true    # multi-round adversarial debate
debate_rounds: 4        # number of debate rounds
```

---

## 📁 Project Structure / 项目结构

```
AlphaForge/
├── README.md                 # This file
├── CLAUDE.md                 # Workflow definition for AI
├── 策略配置.md                # Strategy config (filtering criteria)
├── 思路大纲.md                # Thought outline template
├── 持仓.md                   # Holdings template
├── scripts/                  # AKShare data collection pipeline
│   ├── run_all.py
│   ├── fetch_macro.py        # CPI/PPI/M2/LPR/GDP
│   ├── fetch_sectors.py      # Sector fund flow rankings
│   └── fetch_candidates.py   # Stock financials
├── examples/                 # Example analysis reports
│   └── 2026-05-10-*-三策略推荐.md
└── wiki/                     # Knowledge base structure (Obsidian)
    ├── entity/               # People, companies, products
    ├── concept/              # Principles, methodologies
    └── source/               # Source summaries
```

---

## 📊 Example Output / 输出示例

Each analysis generates:
- `.md` — Full report with 13 sections
- `.html` — Formatted web version

Report structure:
1. Logic Map
2. Judgment → Search → Wiki Cross-Validation
3. Macro Environment Summary
4. Sector & Industry Data
5. Candidate Pool (6 stocks/sector)
6. Catalyst Timeline
7. Three-Strategy Recommendations
8. Adversarial Debate Summary
9. Cross-Sector Final Picks
10. Risk Warnings
11. Verification Checklist

---

## 🧠 How It Differs / 与众不同

| Feature | AlphaForge | Traditional Research |
|---------|-----------|-------------------|
| Data Source | AKShare + WebSearch hybrid | Single source |
| Decision Process | Adversarial debate (Bull vs Bear) | Single analyst opinion |
| Strategy Framework | 3 parallel strategies | Single approach |
| Verification | Automated self-check | Manual review |
| Output | `.md` + `.html` bilingual | Text report |

---

## ⚠️ Disclaimer / 免责声明

**中文**：本项目仅供学术研究和教育目的。所有分析不构成投资建议。投资有风险，入市需谨慎。数据来源为公开市场数据，准确性不保证。

**English**: This project is for academic research and educational purposes only. All analyses do not constitute investment advice. Investing involves risk. Data is from public sources and accuracy is not guaranteed.

---

## 📄 License

MIT
