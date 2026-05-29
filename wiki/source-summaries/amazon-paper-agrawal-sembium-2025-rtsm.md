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
domains: [amazon, ecommerce-search, semantic-matching, retrieval, cold-start]
source_type: academic-paper
extraction_mode: abstract-plus-detailed-notes
source_title: RTSM: Knowledge distillation with diverse signals for efficient real-time semantic matching in e-commerce
source_date: 2025
source_author: Sanjay Agrawal; Vivek Sembium
raw_path: https://www.amazon.science/publications/rtsm-knowledge-distillation-with-diverse-signals-for-efficient-real-time-semantic-matching-in-e-commerce
verification_status: spot-checked
related:
  - ../platforms/amazon-rufus-and-cosmo.md
  - ../syntheses/amazon-rufus-cosmo-e-geo-kes-response.md
---

# 来源摘要｜Agrawal & Sembium 2025｜RTSM

## Why this source matters
这篇论文比 seller 圈常谈的 GEO 话题更底层，因为它研究的是：
在大规模电商场景下，平台如何在严格延迟约束下做实时语义匹配。

换句话说，它更接近 `recall layer`，而不是 `generative reranking layer`。

## Extracted facts / observations
- 论文聚焦两类 semantic matching task：
  - semantic query reformulation
  - semantic product retrieval
- 它明确把问题定义为：
  - 把 poorly constructed queries 映射到更好的 query / product neighborhood
- 方法上，RTSM 用 knowledge distillation 训练低延迟 student model。
- 训练信号不仅来自 teacher soft labels，还来自多类 ground truth：
  - direct audits
  - synthetic examples created by LLMs
  - user interaction data
  - taxonomy-based datasets
- 论文报告：
  - student model 相比直接训练有约 2-2.5% ROC-AUC 提升
  - 在部分设置下 outperform teacher / prior KD baselines

## What this source supports
- 电商平台仍然高度重视低延迟 retrieval / reformulation 基础设施。
- LLM 在这里更多是：
  - 生成训练信号
  - 补充语义覆盖
  而不是直接替代整个搜索栈。
- 更稳妥的 KES 判断是：
  - 先进入候选集仍然关键
  - 生成式优化不能替代 semantic retrieval foundation

## What this source does not support
- 不支持把 semantic matching 等同于 Rufus。
- 不支持据此推出 seller 只要“语义对齐”就能得到生成式曝光。
- 不支持忽略 title / attributes / category / structured fields 的基础召回工作。

## Caveats / ambiguity
- 这是 retrieval infrastructure 论文，不是前台 shopping assistant 论文。
- 但它对纠正 “AI 时代关键词已没用” 这种说法非常有帮助。

## Sources
- https://www.amazon.science/publications/rtsm-knowledge-distillation-with-diverse-signals-for-efficient-real-time-semantic-matching-in-e-commerce
