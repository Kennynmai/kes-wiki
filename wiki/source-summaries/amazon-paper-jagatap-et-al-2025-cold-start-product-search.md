---
type: source-summary
status: draft
owner: strategy
created: 2026-04-19
updated: 2026-04-19
visibility: team
confidence: medium
officiality: draft
domain: platform
domains: [amazon, ecommerce-search, cold-start, query-classification, retrieval]
source_type: academic-paper
extraction_mode: abstract-plus-detailed-notes
source_title: Reinforcement learning for adversarial query generation to enhance relevance in cold-start product search
source_date: 2025
source_author: Akshay Jagatap et al.
raw_path: https://www.amazon.science/publications/reinforcement-learning-for-adversarial-query-generation-to-enhance-relevance-in-cold-start-product-search
verification_status: spot-checked
related:
  - ../platforms/amazon-rufus-and-cosmo.md
  - ../syntheses/amazon-rufus-cosmo-e-geo-kes-response.md
---

# 来源摘要｜Jagatap et al. 2025｜Cold-Start Product Search

## Why this source matters
seller 圈常说“新 listing 没流量”，但这篇论文把问题说得更技术化：
新品 / 新类目 / 新表达之所以吃亏，往往首先是 query-to-category mapping 和 retrieval 本身在冷启动时变差。

## Extracted facts / observations
- 论文聚焦 cold-start 场景下的 query classification。
- 问题定义是：
  - 新品或新类目缺少历史交互数据
  - 导致 query-to-category mapping 不准
  - 进一步伤害 retrieval 与 ranking
- 方法上，作者用 RL 驱动的 adversarial synthetic query generation 来暴露 relevance model 弱点，再回灌训练数据。
- 公开结果：
  - benchmark 平均 PR-AUC 提升 1.82%
  - proprietary dataset 提升 3.26%

## What this source supports
- “先被理解为哪类商品” 仍然是新品流量的基础门槛。
- 在 AI 时代，冷启动问题没有消失，只是更多借助 LLM 生成训练信号去缓解。
- KES 不应把 GEO / answer-surface 优化当成新品启动的全部。

## What this source does not support
- 不支持由此推出 seller 文案 tweak 可以替代冷启动基础工作。
- 不支持忽视类目、属性、产品类型命名、变体结构与 product-type language。

## Caveats / ambiguity
- 这是 query-classification 论文，不是 seller content 论文。
- 但它对 KES 非常重要，因为它强化了一个结论：
  `recall layer` 不是旧时代遗留物，而是新旧时代都必须先过的门槛。

## Sources
- https://www.amazon.science/publications/reinforcement-learning-for-adversarial-query-generation-to-enhance-relevance-in-cold-start-product-search
