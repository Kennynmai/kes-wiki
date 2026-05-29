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
domains: [amazon, rufus, geo, agentic-ecommerce, ecommerce-search]
source_count: 8
review_cycle: monthly
verification_status: spot-checked
related:
  - ../platforms/amazon-rufus-and-cosmo.md
  - ./amazon-rufus-cosmo-e-geo-kes-response.md
  - ../source-summaries/amazon-paper-yu-et-al-2023-folkscope.md
  - ../source-summaries/amazon-paper-yu-et-al-2024-cosmo.md
  - ../source-summaries/amazon-paper-kuzi-malmasi-2024-qa-recommendation.md
  - ../source-summaries/amazon-science-rufus-technology-2024.md
  - ../source-summaries/amazon-paper-agrawal-sembium-2025-rtsm.md
  - ../source-summaries/amazon-paper-guo-et-al-2025-negation-product-search.md
  - ../source-summaries/e-geo-paper-bagga-et-al-2025.md
  - ../source-summaries/agentic-ecommerce-paper-allouah-et-al-2025.md
---

# Amazon / Rufus / GEO / Agentic Commerce｜8 篇核心材料

## What this page is for
这页不追求“最全”，而是给 KES 一份更稳的阅读起点：

如果只读 8 篇，哪些材料最值得优先读？

筛选标准是：
- 一手或强一手来源优先
- 能改变结构性判断，而不是只给技巧
- 能覆盖：
  - intent layer
  - retrieval layer
  - answer layer
  - agent-choice layer

## Executive view
如果把 seller 圈常见的 Amazon AI 讨论压缩一下，真正值得读的不是更多“模板”，而是下面这 8 篇：

1. `FolkScope`
2. `COSMO`
3. `Kuzi & Malmasi`
4. `Amazon Science Rufus technology`
5. `RTSM`
6. `Negation queries`
7. `E-GEO`
8. `ACES`

它们组合起来，能比单独读微信文更完整地回答四个问题：
- 平台在理解什么
- 平台在召回什么
- 生成式层如何解释和比较
- agent 直接买时会发生什么

## The 8 readings
### 1. FolkScope｜先看平台为什么研究 intention KG
最适合回答：
- 为什么 Amazon 会从属性知识图谱走向 intention / commonsense
- 为什么 seller 只写品牌词和参数词越来越不够

核心价值：
- 提前揭示 `used_for / audience / reason / scenario` 这类关系会变重要

什么时候读：
- 当团队还停留在“Rufus 只是聊天框”时，先读它

读后应得结论：
- 电商平台在建模“为什么买”，不是只建模“是什么”

### 2. COSMO｜看意图知识如何进入系统层
最适合回答：
- Amazon 到底公开过什么真正硬的后台系统证据

核心价值：
- 说明 commonsense / intent layer 不是卖家圈想象，而是 Amazon 已公开部署的 search application infrastructure

读后应得结论：
- `COSMO` 更像 backstage knowledge layer，不是 seller 可直接操控的排名秘籍

### 3. Kuzi & Malmasi｜看 Rufus 背后的购物阶段问题定义
最适合回答：
- 为什么 Rufus 会覆盖 exploration / comparison / final consideration

核心价值：
- 它给出最稳的 shopping-stage framing

读后应得结论：
- 更好的内容不是“更会卖”，而是更会回答不同购物阶段的问题

### 4. Amazon Science Rufus technology｜看官方公开的证据面
最适合回答：
- Rufus 到底公开承认会用哪些证据源

核心价值：
- 明确公开：
  - catalog
  - reviews
  - community Q&A
  - web
  - internal APIs

读后应得结论：
- 不能只优化标题和 bullet；要把 answer corpus 当成系统工程

### 5. RTSM｜看基础召回层为什么没消失
最适合回答：
- AI 时代为什么仍不能跳过 semantic retrieval

核心价值：
- 它提醒 KES：生成式层之前，仍有 query reformulation 和 product retrieval 这道门

读后应得结论：
- `recall layer` 不是旧时代残留，而是前置基础设施

### 6. Negation Queries｜看复杂自然语言需求如何被理解
最适合回答：
- 用户说“不要什么”时，平台如何理解

核心价值：
- 说明 constraint / exclusion / edge-case language 正在成为真实 query-understanding 对象

读后应得结论：
- listing / Q&A 需要覆盖 non-fit、negative constraints、边界条件

### 7. E-GEO｜看生成式重排层会奖励什么
最适合回答：
- 如果商品进入候选集，description rewrite 会如何影响生成式排序

核心价值：
- 把问题推进到 e-commerce reranking

读后应得结论：
- 结构化、可比较、可解释、早位置信息前置，通常比空泛 persuasive copy 更稳

### 8. ACES｜看 AI 直接替用户购物时的市场行为
最适合回答：
- 如果 agent 直接选商品，市场会如何重新分配

核心价值：
- 把问题从 answer visibility 推进到 choice dynamics

读后应得结论：
- position bias、endorsement、model drift、seller-side tweaks 都会影响 agentic market share

## Why these 8 are better than most seller summaries
### 1. 它们不是单一层面的材料
seller 文常把所有问题压成：
- “怎么写文案”

这 8 篇会把问题拆开：
- intention modeling
- retrieval
- shopping-stage QA
- evidence grounding
- reranking
- agent choice

### 2. 它们更接近一手证据
这组材料里，至少有一半来自：
- Amazon Science
- Amazon 研究作者
- 正式论文 / OpenReview / arXiv 原文

### 3. 它们更能防止误判
只读 seller 文，最容易出现三种误判：
- 以为关键词没用了
- 以为 E-GEO 就是 Amazon 真实排序
- 以为一次性 rewrite 就够了

这 8 篇都会把这些误判拆掉。

## Two strong adjacent readings
如果读完 8 篇还要补两篇，建议优先：

### Cold-start product search
- 用来强化新品 / 新类目启动问题
- 结论：别把 answer-surface 优化当作新品启动的全部

### ShoppingComp
- 用来强化“真实购物代理还远未成熟”
- 结论：agent 能写报告，不等于 agent 能稳定、安全地选对商品

## KES reading order
如果团队时间有限，建议顺序：

1. `Kuzi & Malmasi`
2. `Amazon Science Rufus technology`
3. `COSMO`
4. `RTSM`
5. `E-GEO`
6. `ACES`
7. `FolkScope`
8. `Negation queries`

这个顺序最适合先建立整体结构，再补底层机制和边角 query 类型。

## Bottom line
更好的读法不是：
> 再找几个 GEO 技巧

而是：
> 先把 Amazon AI 时代的电商问题拆成意图、召回、证据、重排、代理选择五层，再分别看证据。

## Sources
- [来源摘要｜Yu et al. 2023｜FolkScope](../source-summaries/amazon-paper-yu-et-al-2023-folkscope.md)
- [来源摘要｜Yu et al. 2024｜Amazon COSMO](../source-summaries/amazon-paper-yu-et-al-2024-cosmo.md)
- [来源摘要｜Kuzi & Malmasi 2024｜Rufus 背后的 Q&A 推荐问题定义](../source-summaries/amazon-paper-kuzi-malmasi-2024-qa-recommendation.md)
- [来源摘要｜Amazon Science 2024｜Rufus 技术栈补充披露](../source-summaries/amazon-science-rufus-technology-2024.md)
- [来源摘要｜Agrawal & Sembium 2025｜RTSM](../source-summaries/amazon-paper-agrawal-sembium-2025-rtsm.md)
- [来源摘要｜Guo et al. 2025｜Negation Queries in Product Search](../source-summaries/amazon-paper-guo-et-al-2025-negation-product-search.md)
- [来源摘要｜Bagga et al. 2025｜E-GEO](../source-summaries/e-geo-paper-bagga-et-al-2025.md)
- [来源摘要｜Allouah et al. 2025｜AI Shopping Agents Buy What?](../source-summaries/agentic-ecommerce-paper-allouah-et-al-2025.md)
- [来源摘要｜Jagatap et al. 2025｜Cold-Start Product Search](../source-summaries/amazon-paper-jagatap-et-al-2025-cold-start-product-search.md)
- [来源摘要｜ShoppingComp｜真实购物代理评测](../source-summaries/shoppingcomp-openreview-2025-2026.md)
