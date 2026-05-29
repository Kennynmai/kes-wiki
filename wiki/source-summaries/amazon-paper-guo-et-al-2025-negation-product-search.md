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
domains: [amazon, ecommerce-search, query-understanding, negation, retrieval]
source_type: academic-paper
extraction_mode: abstract-plus-detailed-notes
source_title: Learning to rewrite negation queries in product search
source_date: 2025
source_author: Mengtian Guo et al.
raw_path: https://www.amazon.science/publications/learning-to-rewrite-negation-queries-in-product-search
verification_status: spot-checked
related:
  - ../platforms/amazon-rufus-and-cosmo.md
  - ../syntheses/amazon-rufus-cosmo-e-geo-kes-response.md
---

# 来源摘要｜Guo et al. 2025｜Negation Queries in Product Search

## Why this source matters
这篇论文解决的是 seller 视角经常低估的一类 query：
用户并不只会说自己想要什么，也会明确说自己不要什么。

例如：
- no laces
- without fragrance
- not plastic
- no drilling

## Extracted facts / observations
- 论文指出 negation queries 在 product search 中很常见。
- 困难不只是识别否定词，还包括 vocabulary gap：
  - query 说 `no laces`
  - product 可能写 `slip-on`
- 方法上，论文先用 LLM 从 product text 抽取 rewrites，再训练 Seq2Seq model 生成未见 query 的 rewrite。
- 公开结果：
  - 对 negation queries，precision@30 提升 3.17%

## What this source supports
- query understanding 仍然是核心战场。
- 用户自然语言里的：
  - negative constraints
  - exclusion criteria
  - edge-case needs
  不应被 seller copy 忽视。
- 对 KES 更有价值的启发是：
  - 只写正向卖点不够
  - 还要明确表达不含什么、不适合什么、替代什么

## What this source does not support
- 不支持把 negation rewrite 当作 seller 可直接操控的字段权重规则。
- 不支持由此推出所有 constraint language 都会提升曝光。

## Caveats / ambiguity
- 这是 query rewrite 论文，不是内容优化论文。
- 但它说明平台对复杂自然语言 constraint 的理解正在增强，卖家侧表达也应更接近真实 constraint language。

## Sources
- https://www.amazon.science/publications/learning-to-rewrite-negation-queries-in-product-search
