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
domains: [bathtub-filter, competitor-reviews, review-labeling, complaint-taxonomy]
source_type: review-labeling-analysis
extraction_mode: normalized-corpus-plus-rule-reviewed-labeling
source_date: 2026-06-02
review_count: 2562
asin_count: 10
raw_path: ../../raw/products/bathtub-filter/2026-04-20-competitor-review-corpus/
verification_status: structured-import-checked
related:
  - ../products/bathtub-filter/bathtub-filter-research-coverage-gaps.md
  - ../products/bathtub-filter/bathtub-filter-complaint-taxonomy-and-risk-by-route.md
  - ../products/bathtub-filter/bathtub-filter-kes-go-no-go-memo-v1.md
---

# 来源摘要 - Bathtub Filter 竞品评论逐条标签分析（2026-06-02）

## Why this source matters
这批资料是在 2026-04-20 截止的 bathtub active 10 ASIN / 2562 条竞品评论语料基础上，完成的逐条标签证据链和二轮规则维护。它把原来的关键词初筛进一步推进为可用于产品风险判断的评论 taxonomy。

> 2026-06-18 口径修正：Filterbaby `B0FNVDJRSQ` 属于 shower-filter / showerhead inline 产品，已从本 evidence-chain 删除 99 条评论；对应数据保留在 shower-filter 项目。

## Source
- 原始语料 raw：`raw/products/bathtub-filter/2026-04-20-competitor-review-corpus/bathtub-filter-competitor-review-corpus-2026-04-20.normalized.csv`
- 逐条标签明细：`raw/products/bathtub-filter/2026-04-20-competitor-review-corpus/bathtub-filter-competitor-review-labeling-evidence-chain-2026-06-02.csv`
- 标签方法说明：`raw/products/bathtub-filter/2026-04-20-competitor-review-corpus/bathtub-filter-competitor-review-labeling-method-note-2026-06-02.md`
- 洞察报告：`raw/products/bathtub-filter/2026-04-20-competitor-review-corpus/bathtub-filter-competitor-review-labeling-insight-report-2026-06-02.md`

## Data coverage
- 评论总数：2562
- ASIN 数：10
- 5 星：1954；4 星：132；3 星：76；2 星：81；1 星：319
- 1-2 星：400（15.6%）
- 负面标签命中行：552

## User-confirmed labeling rules
- 低星标题可作为标签证据，但标为低置信度。
- 设计不好 / 水压太强 / 水流处理失败归入 `绕流/溢流/过滤路径失效`。
- 高星评论里的真实吐槽保留负面标签，但只作为轻微吐槽/混合评价，不计入高杀伤投诉。
- 到货像用过 / 二次销售 / 疑似退货品单独归入 `二次销售/疑似退货品`。
- `water quality` 单独不算硬水；`softer water / harsh water` 算硬水。
- 正面“不溢流 / 水都进入滤器”的评论从负面溢流移出，改为正面 `水流稳定/不易飞溅`。

## High-kill complaint ranking (1-2 star only)
| 标签 | 命中评论数 | 占比 |
|---|---:|---:|
| 整体无效/不符合预期 | 185 | 46.2% |
| 质量破损/做工问题 | 79 | 19.8% |
| 绕流/溢流/过滤路径失效 | 73 | 18.2% |
| 敏感肌/宝宝场景效果不稳定 | 71 | 17.8% |
| 宣传口径争议（重金属/TDS等） | 69 | 17.2% |
| 发霉/卫生清洁风险 | 56 | 14.0% |
| 掉砂/掉屑/包装脏污 | 30 | 7.5% |
| 硬水改善不明显/肤感无变化 | 24 | 6.0% |
| 二次销售/疑似退货品 | 22 | 5.5% |
| 滤芯更换麻烦/寿命不清 | 21 | 5.2% |
| 安装不稳/固定带打滑 | 13 | 3.2% |
| 去氯效果不明显/气味仍重 | 10 | 2.5% |

## Overall complaint labels
| 标签 | 命中评论数 | 占比 |
|---|---:|---:|
| 整体无效/不符合预期 | 188 | 7.3% |
| 滤芯更换麻烦/寿命不清 | 121 | 4.7% |
| 绕流/溢流/过滤路径失效 | 111 | 4.3% |
| 宣传口径争议（重金属/TDS等） | 110 | 4.3% |
| 质量破损/做工问题 | 83 | 3.2% |
| 发霉/卫生清洁风险 | 80 | 3.1% |
| 敏感肌/宝宝场景效果不稳定 | 74 | 2.9% |
| 掉砂/掉屑/包装脏污 | 51 | 2.0% |
| 硬水改善不明显/肤感无变化 | 25 | 1.0% |
| 二次销售/疑似退货品 | 22 | 0.9% |
| 安装不稳/固定带打滑 | 18 | 0.7% |
| 去氯效果不明显/气味仍重 | 11 | 0.4% |

## Positive labels
| 标签 | 命中评论数 | 占比 |
|---|---:|---:|
| 安装方便/适配性强 | 498 | 19.4% |
| 改善皮肤/头发感受 | 254 | 9.9% |
| 宝宝/敏感肌场景友好 | 251 | 9.8% |
| 减少氯味/泳池味 | 59 | 2.3% |
| 水流稳定/不易飞溅 | 20 | 0.8% |

## Persona labels
| 标签 | 命中评论数 | 占比 |
|---|---:|---:|
| 婴幼儿/儿童家庭 | 592 | 23.1% |
| 硬水/矿物残留困扰用户 | 538 | 21.0% |
| 敏感肌/干痒/湿疹困扰人群 | 512 | 20.0% |
| 氯味/泳池味困扰用户 | 462 | 18.0% |
| 泡澡护理/放松型用户 | 452 | 17.6% |

## QA status
- 低星未命中投诉点：0 条
- 低置信度标题归因：12 条
- 高星轻微吐槽：197 条
- 硬水标签需复核：0 条

## Strategic implication
- KES V1 的最高风险不只是安装，而是 `整体无效/不符合预期`、`绕流/溢流/过滤路径失效`、`质量破损/做工问题`、`敏感肌/宝宝场景效果不稳定`、`宣传口径争议` 的组合。
- 高星评论中的轻微吐槽应进入设计优化队列，但不应与 1-2 星高杀伤投诉混为同一优先级。
- 这批资料可以把原 gap 中 “Amazon review 直采量化/NLP 待做” 更新为 “已有逐条标签证据链”；但仍不能替代真实 SKU 退货率。

## Caveats
- 当前标签是规则化维护后的证据链，不等同于逐条人工精标。
- 真实退货率、退款原因、客服工单仍需卖家后台或 Brand Registry 数据。

## Best use in KES wiki
- 更新 `bathtub-filter-research-coverage-gaps`：评论语料和标签分析已补，真实退货率仍缺。
- 更新 `bathtub-filter-complaint-taxonomy-and-risk-by-route`：用高杀伤投诉排序替换旧的关键词初筛判断。
- 更新 `bathtub-filter-kes-go-no-go-memo-v1`：把评论风险从“待补”调整为“已有证据链，但需物理测试和真实退货率验证”。
