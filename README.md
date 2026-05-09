<p align="center">
  <img src="https://img.shields.io/badge/AlphaForge-投资分析框架-FF6B35?style=for-the-badge" alt="AlphaForge"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="MIT"/>
  <img src="https://img.shields.io/badge/AI-Claude-8A2BE2?style=for-the-badge" alt="Claude"/>
</p>

<h1 align="center">⚒️ AlphaForge</h1>

<p align="center">
  <b>AI 驱动 · 多市场 · 综合投资分析系统</b><br>
  <i>把你的投资逻辑，变成可复用的工业化流水线</i>
</p>

<p align="center">
  <i>AI-Powered Multi-Market Investment Analysis Framework</i>
</p>

---

## 💡 一句话认识 AlphaForge

> **AlphaForge 是一个由 AI（Claude）驱动的投资分析工作流，覆盖 A 股全市场。**
>
> 你只需要写一句判断，它就会自动完成：宏观环境扫描 → 板块动量检测 → 产业数据深挖 → 正反方辩论 → 三策略选股 → 输出完整报告。
>
> 整个过程 21 步，全部自动化、可追溯、可复现。

---

## 🤔 为什么要用 AlphaForge？

### 你平时做投资分析，是不是这样？

| 你的痛点 | 怎么解决 |
|---------|---------|
| 😫 每天看几十篇研报，信息过载 | **AI 帮你扫**，只输出关键结论 |
| 🤯 板块太多，不知道资金在往哪走 | **数据驱动**，板块动量一目了然 |
| 😬 看多一个票，但总担心漏了什么风险 | **正反方辩论**，压力测试每个假设 |
| 😵 持仓好几个，不知道哪个该留哪个该砍 | **三策略分流**，追最强 / 高弹性 / 安全边际 |
| 📝 做完分析还要写报告，太费时间 | **自动生成**，.md + .html 一键输出 |

### 一句话：**AlphaForge 让你从"到处找信息"变成"直接看结论"。**

---

## 🎯 FABE 法则：为什么选 AlphaForge

### 🔹 Feature 1：21 步自动化流水线

**特点（Feature）**：从你的判断到最终推荐，共 21 个结构化步骤，AI 自动执行。

**优势（Advantage）**：别人花一天搜集信息 + 半天写报告，你只需要输入一句话，5 分钟拿到完整分析。

**利益（Benefit）**：**你的时间花在决策上，而不是搜集信息上。**

**证据（Evidence）**：每一份报告都有完整的逻辑总图、数据来源、推理过程，经得起回溯验证。

### 🔹 Feature 2：正反方 4 轮对抗辩论

**特点（Feature）**：在推荐之前，AI 会模拟"多方"和"空方"进行 4 轮辩论。

**优势（Advantage）**：传统分析只有一个视角，很容易陷入"确认偏误"——只看到支持自己观点的证据。辩论机制强制你听到反方声音。

**利益（Benefit）**：**减少冲动决策，让你对每一笔交易更有信心。**

**证据（Evidence）**：辩论结果会明确标注"共识区"（多方空方一致看好的方向）和"分歧区"（需要附加条件的判断）。

### 🔹 Feature 3：三大策略并行

**特点（Feature）**：每只候选股会从 3 个不同策略维度独立评估。

| 策略 | 适合你什么时候用 | 核心逻辑 |
|:----:|----------------|---------|
| 🏆 **追最强** | 市场趋势明确，你想要"上车" | 板块增速前 5 + 资金龙头 + 近期催化 |
| 🚀 **高弹性** | 你想"博一把"，愿意承担波动换高赔率 | 小市值 + 刚过拐点 + 经营杠杆 |
| 🛡️ **安全边际** | 你想"稳稳拿"，不想每天盯盘 | 低 PE + 行业前 3 + 现金流为正 |

**优势（Advantage）**：同一只票，不同策略看到的维度不同。你可以根据自己当下的风险偏好，选择最适合的"入场姿势"。

**利益（Benefit）**：**同一个分析，同时满足你的激进和稳健需求。**

**证据（Evidence）**：每只推荐都附带验证清单——PE、市值、增速、催化，逐条过筛。

### 🔹 Feature 4：双数据源混合

**特点（Feature）**：AKShare 提供结构化数据（板块资金流向、宏观指标、财务数据）+ WebSearch 提供定性信息（新闻、政策、产业催化）。

**优势（Advantage）**：单纯靠搜索不够精确（"大约 30 亿" vs "精确 32.17 亿"），单纯靠 API 又漏掉新闻。两者互补，兼得精度和广度。

**利益（Benefit）**：**数据更准，信息更全。**

**证据（Evidence）**：M2、CPI、PPI 等宏观数据从 AKShare 直接读表，精确到亿元级别。

---

## 🚀 快速上手（3 分钟跑通）

### 第一步：拉代码

```bash
git clone https://github.com/FR3ZEEZ/AlphaForge.git
cd AlphaForge
```

### 第二步：装依赖

```bash
pip install akshare pandas
```

### 第三步：跑数据

```bash
python scripts/run_all.py
```

### 第四步：出报告

在 Claude Code 里输入：

```
综投 <你对市场的判断，比如：PPI转正，人形机器人量产，存储有点高了>
```

AI 会自动执行 21 步流水线，输出：

- 📄 `xxx-三策略推荐.md` — 完整分析报告（14 个章节）
- 🌐 `xxx-三策略推荐.html` — 网页版报告

---

## 📁 项目结构

```
AlphaForge/
├── 📄 README.md                ← 就是这个文件
├── 📄 CLAUDE.md                ← AI 工作流定义（核心！）
├── 📄 策略配置.md               ← 你想怎么选股，在这里设
├── 📄 思路大纲.md               ← 写你的判断
├── 📄 持仓.md                  ← 记你的持仓
├── 📁 scripts/                 ← 数据采集
│   ├── run_all.py              ← 一键跑
│   ├── fetch_macro.py          ← CPI/PPI/M2
│   ├── fetch_sectors.py        ← 板块资金流向
│   └── fetch_candidates.py     ← 个股财务
├── 📁 examples/                ← 示例报告
└── 📁 wiki/                    ← 知识库（可选）
```

---

## 📊 一份报告长什么样？

每次分析会生成 14 个章节：

| 章节 | 内容 |
|:----:|------|
| 一 | **逻辑总图** — 你输入啥 → AI 搜到啥 → 推荐啥，一张图看完 |
| 二 | **判断验证** — 你的每一个想法，数据支不支持？知识库怎么说？ |
| 三 | **宏观环境** — 流动性、风险偏好、市场风格 |
| 四 | **产业深挖** — 供需格局、订单数据、机构观点 |
| 五 | **候选股池** — 每板块 6 只，带 PE 和信心评级 |
| 六 | **催化时间轴** — 未来 1-2 个月的重大事件 |
| 七 | **三策略推荐** — 每板块 3 只 → 🏆 精选 1 只 |
| 八 | **辩论摘要** — 多方 vs 空方，结论是什么 |
| 九 | **跨板块精选** — 追最强 2 只 / 高弹性 3 只 / 安全边际 4 只 |
| 十~十四 | 交叉信号 / 风险提示 / 验证清单 |

> 📖 想看真实的？[点这里查看示例报告](examples/2026-05-10-商业航天崛起与存储高位-三策略推荐.md)

---

## ⚙️ 配置你的策略

打开 `策略配置.md`，你可以控制：

```yaml
# 数据源开关
akshare_enabled: false   # true = 读AKShare数据，false = 只用WebSearch

# 辩论开关
debate_enabled: true     # 开启正反方辩论
debate_rounds: 4         # 辩论轮数

# 三策略参数
追最强最终: 2            # 最终推荐几只追最强
高弹性最终: 3            # 最终推荐几只高弹性
安全边际最终: 4          # 最终推荐几只安全边际
```

需要回退？把 `akshare_enabled` 改为 `false` 就行，什么都不影响。

---

## ❓ 常见问题

**Q：我需要会编程吗？**
A：不需要。你只需要会写一句话的市场判断，剩下的 AI 自动完成。

**Q：我需要自己准备数据吗？**
A：不需要。`python scripts/run_all.py` 一键采集所有数据。

**Q：这跟普通的炒股软件有什么区别？**
A：炒股软件给你的是数据，AlphaForge 给你的是**决策**。它还模拟辩论帮你避开盲区。

**Q：我的持仓信息安全吗？**
A：持仓只有你本地能看到。上传 GitHub 的版本已脱敏，不包含任何个人信息。

**Q：只能用 A 股吗？**
A：目前 A 股支持最完善。港股和美股通过 WebSearch 辅助覆盖。

---

## ⚠️ 免责声明

> 本项目仅供学术研究和教育目的。所有分析不构成投资建议。投资有风险，入市需谨慎。数据来源于公开市场数据，准确性不作保证。
>
> *This project is for academic research and educational purposes only. Not financial advice.*

---

<p align="center">
  ⭐ 如果这个项目对你有帮助，点个 Star 吧<br>
  <a href="https://github.com/FR3ZEEZ/AlphaForge">github.com/FR3ZEEZ/AlphaForge</a>
</p>
