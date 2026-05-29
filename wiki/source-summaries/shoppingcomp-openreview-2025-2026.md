---
type: source-summary
status: draft
owner: strategy
created: 2026-04-19
updated: 2026-04-19
visibility: team
confidence: medium
officiality: draft
domain: strategy
domains: [agentic-ecommerce, shopping-agents, benchmark, evaluation, safety]
source_type: academic-paper
extraction_mode: abstract-plus-detailed-notes
source_title: ShoppingComp: Are LLMs Really Ready for Your Shopping Cart?
source_date: 2025-09-17 / 2026-02-12
source_author: Huaixiao Tou et al.
raw_path: https://openreview.net/forum?id=ggAJSyCAKf
verification_status: spot-checked
related:
  - ../syntheses/amazon-rufus-cosmo-e-geo-kes-response.md
  - ./agentic-ecommerce-paper-allouah-et-al-2025.md
---

# 来源摘要｜ShoppingComp｜真实购物代理评测

## Why this source matters
如果 `ACES` 更像“agentic market behavior audit”，那么 `ShoppingComp` 更像“真实购物代理能力 benchmark”。

它的价值在于提醒 KES：
不要因为模型能写漂亮购物报告，就误以为它已经擅长真实选品与风险判断。

## Extracted facts / observations
- OpenReview 页面显示：
  - submitted on 2025-09-17
  - modified on 2026-02-12
- benchmark 覆盖三类能力：
  - precise product retrieval
  - expert-level report generation
  - safety-critical decision making
- 任务集规模：
  - 120 tasks
  - 1,026 scenarios
  - curated by 35 experts
- 作者强调它采用 real products / easy verifiability / safety hazard identification。
- 摘要中报告：
  - 当前前沿模型与 human performance gap 仍很大
  - 常见错误包括 retrieval failure、unsafe recommendation、被 promotional misinformation 误导

## What this source supports
- “AI 能购物” 不等于 “AI 已经能可靠购物”。
- 未来 agentic commerce 的关键不只是生成文案，而是：
  - retrieval correctness
  - safety reasoning
  - trustworthy evaluation
- 对 KES 更好的启发是：
  - 不要高估 shopping agent 的现状
  - 要区分回答漂亮和决策可靠

## What this source does not support
- 不支持把 OpenReview submission 当作稳定共识。
- 不支持把 benchmark 分数直接映射到 Amazon Rufus 当前体验。

## Caveats / ambiguity
- 当前可见来源以 OpenReview 摘要为主，不是正式期刊定稿。
- 但它已经足够说明：真实购物代理评测比 seller 圈文案模板复杂得多，也更值得长期关注。

## Sources
- https://openreview.net/forum?id=ggAJSyCAKf
