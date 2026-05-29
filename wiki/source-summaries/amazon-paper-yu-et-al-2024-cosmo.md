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
domains: [amazon, cosmo, ecommerce-search, knowledge-graph, generative-ai]
source_type: academic-paper
extraction_mode: abstract-plus-detailed-notes
source_title: COSMO: A Large-Scale E-commerce Common Sense Knowledge Generation and Serving System at Amazon
source_date: 2024
source_author: Changlong Yu et al.
raw_path: ../../raw/platforms/amazon/rufus-cosmo/2026-04-19/papers/cosmo-sigmod-2024.pdf
verification_status: spot-checked
related:
  - ../platforms/amazon-rufus-and-cosmo.md
  - ../../raw/platforms/amazon/rufus-cosmo/2026-04-19/raw-capture-log.md
---

# 来源摘要｜Yu et al. 2024｜Amazon COSMO

## Why this source matters
这是目前最接近 Amazon 官方公开解释 COSMO 的核心论文。它不是 seller 圈二手解读，而是 Amazon / HKUST 作者直接发表的系统论文。

## Extracted facts / observations
- COSMO 被定义为 Amazon 的 large-scale e-commerce common sense knowledge generation and serving system。
- 它要解决的问题是：
  - 传统电商 KG 有商品属性，但缺少用户意图
  - 需要把用户行为背后的 commonsense intention 挖出来
- 系统输入的两类关键行为是：
  - co-buy
  - search-buy
- 论文示例显示，系统试图把模糊 query 与商品能力对齐，例如：
  - `shoes for pregnant women` -> `slip-resistant`
- 论文给出的规模信息：
  - 覆盖 18 个 major categories
  - 生成 6.3M nodes / 29M edges
  - 使用 15 relation types
  - 只用约 30k annotated instructions 扩展到百万级知识
- 论文说明 COSMO 已部署到 Amazon search applications，例如：
  - search navigation
- 论文报告的公开实验结果包括：
  - 在 public ESCI 英文子集上，intent-enhanced cross-encoder 达到 73.48% Macro F1 / 90.78% Micro F1
  - 在线 A/B 测试覆盖约 10% 美国流量，search navigation 场景带来 0.7% relative increase in product sales
  - 同一实验段还观察到 8% navigation engagement rate 提升

## What this source supports
- COSMO 是后台 intent / commonsense layer，不是前台聊天界面。
- COSMO 的重点不是 keyword matching，而是把 query、行为、产品能力、用途、场景、受众等语义关系结构化。
- COSMO 已被 Amazon 用于至少部分搜索导航与相关下游任务，不是纯研究 demo。

## What this source does not support
- 不支持直接断言 “Rufus 就是 COSMO”。
- 不支持直接断言 Rufus 的所有回答都由 COSMO 驱动。
- 不支持把 COSMO 简化成单一 ranking algorithm；论文更接近 knowledge generation + serving system。

## Caveats / ambiguity
- 论文只明确说 COSMO 部署在 search applications such as search navigation。
- 论文没有按名称讨论 Rufus。
- 因此 “COSMO 为 Rufus 提供部分知识 / 意图底座” 是合理推断，但不是论文直接明说。

## Related pages
- [Amazon Rufus and COSMO](../platforms/amazon-rufus-and-cosmo.md)

## Sources
- https://www.amazon.science/publications/cosmo-a-large-scale-e-commerce-common-sense-knowledge-generation-and-serving-system-at-amazon
- https://cdn.amazon.science/19/5d/bde30d0d4019be6421e79e50cda9/cosmo-paper.pdf
- https://www.amazon.science/blog/building-commonsense-knowledge-graphs-to-aid-product-recommendation
- `raw/platforms/amazon/rufus-cosmo/2026-04-19/papers/cosmo-sigmod-2024.pdf`
