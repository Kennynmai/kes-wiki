---
type: synthesis
status: draft
owner: strategy
created: 2026-04-19
updated: 2026-04-19
visibility: company
confidence: medium
officiality: draft
domain: strategy
domains: [geo, aeo, ai-search, content-operations, generative-ai]
source_count: 6
review_cycle: monthly
verification_status: spot-checked
related:
  - ./geo-research-landscape.md
  - ../source-summaries/geo-paper-aggarwal-et-al-2024.md
  - ../source-summaries/e-geo-paper-bagga-et-al-2025.md
  - ../source-summaries/agentic-ecommerce-paper-allouah-et-al-2025.md
  - ../source-summaries/geo-platform-guidance-2025-2026.md
---

# GEO Tactics Taxonomy

## What this page is for
这页不回答 “GEO 是什么”，而回答：

如果把目前较可信的 GEO / E-GEO / agentic commerce 研究压成一组可测试动作，应该怎么分类？

## Core distinction
GEO 相关动作至少分成四类：

1. `Eligibility tactics`
让内容可被抓、可被索引、可被展示

2. `Answer-surface tactics`
让内容更容易被引用、被摘要、被重用

3. `Commerce-rerank tactics`
让商品内容更容易被购物型生成系统理解和比较

4. `Agent-choice tactics`
让 agent 在做明确选择时更容易选你

这四类动作不应混成 “一个 GEO checklist”。

## 1. Eligibility tactics
### Definition
不直接改变答案质量或排序偏好，而是确保内容先进入候选集。

### Typical examples
- crawl access
- robots / snippet settings
- indexability
- canonical hygiene
- structured data eligibility
- product feed availability

### Evidence level
- 平台官方 guidance 最强
- Google / Bing / OpenAI 的相关页面都指向这层基础面

### KES-ready actions
- 检查 crawler access
- 检查重要页面是否 snippet-eligible
- 检查 product schema / merchant listing completeness
- 检查 canonical / duplicate content hygiene

### Failure mode
- 团队过早讨论“怎么让 AI 喜欢”，但页面先天不可见

## 2. Answer-surface tactics
### Definition
让内容更容易在 generative answer 中被抽取、拼接、引用。

### Typical examples
- better standalone answer units
- factual statistics
- quotations
- citations / references
- readable formatting
- easier-to-understand rewriting
- clearer sectioning

### Evidence level
- `GEO` 原论文最强
- `Cite Sources`、`Quotation Addition`、`Statistics Addition`、`Fluency Optimization` 都属于这一层

### KES-ready actions
- 给关键页面补事实密度
- 补独立可引用的短段答案
- 补数字、条件、边界
- 把 FAQ 做成真正可引用的回答，而不是 marketing FAQ

### Failure mode
- 只加文风，不加信息
- 只加“authoritative”口吻，不加证据

## 3. Commerce-rerank tactics
### Definition
让商品在进入候选集后，更容易被购物型生成系统理解、比较、排前。

### Typical examples
- intent alignment
- clearer constraints
- better scenario framing
- explicit product-type noun
- attribute-to-benefit mapping
- comparison framing

### Evidence level
- `E-GEO` 最强
- 它把问题明确建模成 e-commerce reranking，而不是 web citation visibility

### KES-ready actions
- 在标题 / PDP 中补 product-type noun
- 显式补 audience / scenario / constraint
- 强化 comparison-ready expression
- 把 vague marketing copy 改成 decision-oriented copy

### Failure mode
- 拿 commerce rerank tactic 替代基础召回
- 误以为“更像答案”就等于“更容易被召回”

## 4. Agent-choice tactics
### Definition
不是让系统更愿意“引用你”，而是更愿意“选你”。

### Typical examples
- front-loading decisive noun
- front-loading use-case token
- exposing missing specs
- exposing bundle / accessory count
- query-conditional title / description emphasis

### Evidence level
- `ACES / What Is Your AI Agent Buying?` 最强
- 目前仍偏 sandbox research，但已经足够说明这一层与 reranking 不同

### KES-ready actions
- 在实验环境里测试 early-token alignment
- 在 query family 下测试不同 title emphasis
- 记录哪些 specs 在不同任务里是 decisive

### Failure mode
- 把 agent-choice tactics 误判成普适 GEO 规律
- 忽略 model drift

## Tactic families
### A. Surface the decisive noun
**定义**
把最关键的 product-type / task noun 尽早出现。

**例子**
- `Office Floor Lamp`
- `Fitness Smartwatch`
- `Whitening Toothpaste`

**证据**
- ACES seller-side agent 例子最直接

**适用层**
- commerce-rerank
- agent-choice

### B. Surface the decisive use case
**定义**
把真正驱动 query intent 的 usage context 提前。

**例子**
- office
- travel
- baby-safe
- beginner
- narrow feet

**证据**
- Rufus / Kuzi & Malmasi 的 comparison / shopping-stage framing
- ACES office lamp 案例

**适用层**
- answer-surface
- commerce-rerank
- agent-choice

### C. Surface missing attributes and specs
**定义**
把缺失但对筛选重要的结构化属性前置。

**例子**
- `2-Ply`
- `Septic-Safe`
- `Top-Load`
- `Stainless Steel Tub`
- `32W`
- `3000LM`

**证据**
- ACES 高 impact interventions
- Google product structured data guidance 与之方向一致

**适用层**
- commerce-rerank
- agent-choice

### D. Add evidence density
**定义**
增加 facts、numbers、references，使内容更“可引用”。

**例子**
- statistics
- source-backed claim
- factual comparison points

**证据**
- GEO 原论文最强

**适用层**
- answer-surface

### E. Improve readability without losing density
**定义**
让模型更容易 chunk / reuse 内容，而不是单纯缩短。

**例子**
- bullet hierarchy
- short independent sections
- clearer labels
- easier-to-understand rewrite

**证据**
- GEO 的 `Fluency Optimization` / `Easy-to-Understand`

**适用层**
- answer-surface
- commerce-rerank

### F. Expose comparison logic
**定义**
让产品更容易被放入 “A vs B” 的 reasoning frame。

**例子**
- who is this for
- when not to choose it
- what it trades off against
- why pick this over adjacent option

**证据**
- Kuzi / Malmasi 的 comparison-stage framing
- E-GEO 的 ranking logic

**适用层**
- answer-surface
- commerce-rerank

### G. Control preview surface
**定义**
控制哪些内容可被 snippet / AI answer 引用，哪些不应被 preview。

**例子**
- `data-nosnippet`
- snippet controls

**证据**
- Bing 官方最直接
- Google 也有 snippet controls

**适用层**
- eligibility
- answer-surface governance

## Tactics that are often oversold
### 1. Keyword stuffing
证据并不支持它是稳定有效的 GEO tactic。

### 2. Generic authoritative tone
单独使用并不可靠。

### 3. Long persuasive copy
对 AI 系统未必有利，尤其在 commerce 场景。

### 4. Query-conditional adaptation without guardrails
可能接近 manipulation 或 factual drift。

## Recommended testing order
### Tier 1｜Low-risk, high-signal
- improve crawl / index / snippet eligibility
- add structured product attributes
- add factual stats and evidence
- improve readability and sectioning

### Tier 2｜Commerce-specific
- front-load decisive nouns
- front-load decisive use cases
- add missing specs
- expose comparison logic

### Tier 3｜Higher-risk / higher-variance
- query-conditional title adaptation
- agent-choice experiments
- multi-model sandbox testing

## KES rule of thumb
一个 tactic 越接近以下特征，越值得优先测试：
- 更 factual
- 更 explicit
- 更 structured
- 更 query-relevant
- 更 reusable as an answer unit

一个 tactic 越接近以下特征，越应谨慎：
- 更 manipulative
- 更 model-specific
- 更 dependent on hype wording
- 更容易偏离真实产品边界

## Sources
- [GEO 研究全景](./geo-research-landscape.md)
- [来源摘要｜Aggarwal et al. 2024｜GEO 原论文](../source-summaries/geo-paper-aggarwal-et-al-2024.md)
- [来源摘要｜Bagga et al. 2025｜E-GEO](../source-summaries/e-geo-paper-bagga-et-al-2025.md)
- [来源摘要｜Allouah et al. 2025｜AI Shopping Agents Buy What?](../source-summaries/agentic-ecommerce-paper-allouah-et-al-2025.md)
- [来源摘要｜GEO 平台官方 guidance（2025-2026）](../source-summaries/geo-platform-guidance-2025-2026.md)
