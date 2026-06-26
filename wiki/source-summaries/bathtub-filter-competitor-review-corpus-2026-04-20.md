---
type: source-summary
status: draft
owner: strategy
created: 2026-06-02
updated: 2026-06-18
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, competitor-reviews, amazon-reviews, review-mining]
source_type: review-corpus
extraction_mode: xlsx-normalization-plus-keyword-screen
source_date: 2026-04-20
review_count: 2562
asin_count: 10
raw_path: ../../raw/products/bathtub-filter/2026-04-20-competitor-review-corpus/
verification_status: structured-import-checked
related:
  - ../products/bathtub-filter/bathtub-filter-research-coverage-gaps.md
  - ../products/bathtub-filter/bathtub-filter-complaint-taxonomy-and-risk-by-route.md
  - ./bathtub-filter-competitor-review-labeling-analysis-2026-06-02.md
---

# 来源摘要 - Bathtub Filter 竞品评论语料（2026-04-20）

> 2026-06-18 口径修正：Filterbaby `B0FNVDJRSQ` 属于 shower-filter / showerhead inline 产品，已从本 bathtub-filter 评论语料中删除；对应评论数据保留在 shower-filter 项目。本页现在只统计 bathtub active 10 ASIN / 2562 条评论。

## Why this source matters
这批资料补上了此前 `research-coverage-gaps` 中提到的 Amazon review 直采评论缺口：本次共有 10 个 bathtub active ASIN、2562 条评论，可用于量化常见好评/差评模式。

## Source
- 原始来源：`C:/Users/KEVIN/Desktop/浴缸过滤/浴缸过滤器_竞品评论原始资料`
- raw 目标位置：`raw/products/bathtub-filter/2026-04-20-competitor-review-corpus/`
- Excel 是完整语料；`评论分析.md` 是人工挑选的典型评论笔记。

## Extracted facts / observations
- 评论总数：2562
- ASIN 数：10
- 平均评分：4.30（2562 条有评分）
- 4-5 星：2086；3 星：76；1-2 星：400
- VP 评论：1818
- Vine 评论：132

## ASIN coverage
- B0D3X39378：1410 条，平均 4.53 星，1-2 星 164 条
- B0742KFY9R：456 条，平均 3.32 星，1-2 星 169 条
- B0CXT5KL5Z：356 条，平均 4.70 星，1-2 星 24 条
- B0FL24SLM5：90 条，平均 4.74 星，1-2 星 5 条
- B0DTQ8H23D：76 条，平均 3.55 星，1-2 星 17 条
- B0G5NZBW6W：69 条，平均 4.33 星，1-2 星 7 条
- B0FT7R9ZQ9：47 条，平均 4.62 星，1-2 星 4 条
- B0GFQ1JRSK：26 条，平均 4.19 星，1-2 星 2 条
- B008A4AG2U：19 条，平均 3.21 星，1-2 星 8 条
- B0GKT5CHYL：13 条，平均 4.38 星，1-2 星 0 条

## First-pass topic screen
以下是关键词初筛，不是人工精标；适合用于确定优先阅读区，不适合直接作为最终市场结论。

- 易用/方便/推荐：1506 条；其中 1-2 星 61 条；覆盖 10 个 ASIN
- 皮肤/头发表现改善：1442 条；其中 1-2 星 58 条；覆盖 10 个 ASIN
- 安装/适配/出水口兼容：1366 条；其中 1-2 星 133 条；覆盖 10 个 ASIN
- 婴幼儿/儿童/敏感肌使用场景：613 条；其中 1-2 星 38 条；覆盖 10 个 ASIN
- 氯味/泳池味降低：567 条；其中 1-2 星 55 条；覆盖 10 个 ASIN
- 流量/注水速度/溢流/飞溅：406 条；其中 1-2 星 62 条；覆盖 10 个 ASIN
- 硬水/TDS/重金属等过度宣称风险：345 条；其中 1-2 星 31 条；覆盖 10 个 ASIN
- 漏水/脱落/稳定性：208 条；其中 1-2 星 66 条；覆盖 10 个 ASIN

## Caveats / ambiguity
- 主题命中基于中英关键词初筛，会有漏判和误判；逐条标签复核已在 2026-06-02 完成，见 [[bathtub-filter-competitor-review-labeling-analysis-2026-06-02]]。本页 topics 只保留为初筛语料池。
- 这批数据可量化评论模式，但不能代表真实退货率；退货率仍需要 Amazon 后台或 Brand Registry/卖家数据。
- `评论分析.md` 与本批 Excel 的 ASIN 不完全一致：仅在笔记中出现但不在 Excel 中的 ASIN 为 B0012045EO, B08Y8GSVJS, B0C5D7NLC7。

## Best use in KES wiki
- 更新 `bathtub-filter-research-coverage-gaps`：将 “Amazon review 100+ 直采缺口” 改为 “已有 10 ASIN / 2562 条 bathtub active 评论语料 + 2026-06-02 逐条标签证据链；仍缺真实 SKU 退货率、退款原因和客服工单”。
- 更新 `bathtub-filter-complaint-taxonomy-and-risk-by-route`：用 2026-06-02 逐条标签的负面评论主题频次校准投诉优先级。
- 保留 raw 语料，不把全量评论正文直接复制进 wiki 结论页。

## Sources
- `raw/products/bathtub-filter/2026-04-20-competitor-review-corpus/README.md`
- `raw/products/bathtub-filter/2026-04-20-competitor-review-corpus/bathtub-filter-competitor-review-corpus-2026-04-20.normalized.csv`
