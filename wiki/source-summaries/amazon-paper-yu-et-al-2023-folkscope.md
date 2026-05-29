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
domains: [amazon, ecommerce-search, intention-knowledge, commonsense, knowledge-graph]
source_type: academic-paper
extraction_mode: abstract-plus-detailed-notes
source_title: FolkScope: Intention knowledge graph construction for e-commerce commonsense discovery
source_date: 2023
source_author: Changlong Yu et al.
raw_path: https://www.amazon.science/publications/folkscope-intention-knowledge-graph-construction-for-e-commerce-commonsense-discovery
verification_status: spot-checked
related:
  - ../platforms/amazon-rufus-and-cosmo.md
  - ./amazon-paper-yu-et-al-2024-cosmo.md
  - ../syntheses/amazon-rufus-cosmo-e-geo-kes-response.md
---

# 来源摘要｜Yu et al. 2023｜FolkScope

## Why this source matters
如果 `COSMO` 是 Amazon 已公开的较成熟 intention / commonsense system，那么 `FolkScope` 更像它的前置研究脉络。

它的重要性在于：
- 它更清楚地说明 Amazon 这条研究线并不是从 Rufus 开始
- 它把“用户为什么买、买来做什么、适合谁”提升为可结构化知识对象

## Extracted facts / observations
- 论文目标是构建 e-commerce intention knowledge graph。
- 它试图从购物行为中恢复用户背后的 commonsense intention，而不是只停留在商品属性。
- 论文采用：
  - LLM generation
  - human-in-the-loop annotation
  - plausibility / typicality labeling
  - pattern mining and conceptualization
- relation categories 与更一般 commonsense graph 对齐，包括：
  - `IsA`
  - `MadeOf`
  - `UsedFor`
  - 以及其他开放原因 / intention predicates
- 作者明确说这类知识可用于下游 e-commerce applications。
- 论文附带公开代码 / 数据集链接。

## What this source supports
- Amazon / 合作者对 e-commerce commonsense 的研究线是连续的，不是突然为 Rufus 拼凑出来的。
- 平台更重视的并不只是：
  - brand
  - keyword
  - literal attribute
  而是用户购买意图与商品能力之间的结构化关系。
- 对 seller 更稳妥的启发不是“学会某个 GEO trick”，而是更清楚表达：
  - 用途
  - 适配人群
  - 场景
  - 限制条件

## What this source does not support
- 不支持把 FolkScope 直接等同于 Amazon 线上搜索系统。
- 不支持直接推出 Rufus 当前实现。
- 不支持将任意 seller 文案解释成 intention KG optimization。

## Caveats / ambiguity
- 这是一篇前置研究，更偏知识构建框架。
- 它对 seller 的价值是解释平台为什么越来越重视 query intent 和 commonsense relation，而不是直接给运营 playbook。

## Sources
- https://www.amazon.science/publications/folkscope-intention-knowledge-graph-construction-for-e-commerce-commonsense-discovery
- https://github.com/HKUST-KnowComp/FolkScope
