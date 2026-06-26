---
type: source-summary
status: draft
owner: strategy
created: 2026-06-18
updated: 2026-06-18
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, competitor-intelligence, amazon, sales-estimates]
source_type: competitor-material
extraction_mode: xlsx-merge-and-summary
source_date: 2026-06-18
asin_count: 10
raw_path: ../../raw/products/bathtub-filter/2026-06-18-competitor-listing-sales/
verification_status: spot-checked
related:
  - ../products/bathtub-filter/bathtub-filter-competitor-pricing-and-kes-v1-price-recommendation.md
  - ../products/bathtub-filter/bathtub-filter-amazon-category-and-keyword-baseline.md
  - ../products/bathtub-filter/bathtub-filter-research-coverage-gaps.md
---

# Source Summary - Bathtub Filter Competitor Listing + Sales（2026-06-18）

## Why this source matters
这批 SellerSprite 导出补上了 bathtub filter 竞品的 listing、价格、评分、BSR、月销量、月销售额和历史月度销量/销售额/价格。它适合用于校准竞品规模、价格带、Top ASIN 排序、销量趋势和 KES V1 定价参考。

## Source
- raw 数据包：`raw/products/bathtub-filter/2026-06-18-competitor-listing-sales/`
- 整理工作簿：`raw/products/bathtub-filter/2026-06-18-competitor-listing-sales/bathtub-filter-competitor-listing-sales-2026-06-18.xlsx`
- 原始 listing 导出：`source-files/Search(...)-10-US-20260618.xlsx`
- 原始销量导出：`source-files/US-product-sales-20260618.xlsx`

## Scope
本批 bathtub filter 口径为 10 个 ASIN：

`B0CXT5KL5Z`, `B0D3X39378`, `B0742KFY9R`, `B0GFQ1JRSK`, `B0FT7R9ZQ9`, `B0DTQ8H23D`, `B008A4AG2U`, `B0G5NZBW6W`, `B0FL24SLM5`, `B0GKT5CHYL`

`B0FNVDJRSQ` 已明确剔除：它是 Filterbaby shower filter / showerhead inline 产品，保留在 `raw/products/shower-filter/` 与 `wiki/products/shower-filter/`，不进入 bathtub filter 竞品、价格、评论或销量口径。

## Extracted facts
- Listing 月销量合计：15,347
- Listing 月销售额合计：$609,805
- 历史销量表 `2026-06` 销量合计：15,330
- 历史销量表 `2026-06` 销售额合计：$617,149
- 近 12 月销量合计：176,739
- 近 12 月销售额合计：$6,315,297
- `2026-06` 当前均价：$42.73
- 月度长表行数：270

## Top ASIN by `2026-06` units
| Rank | ASIN | Brand | `2026-06` units | `2026-06` revenue | `2026-06` price |
|---:|---|---|---:|---:|---:|
| 1 | `B0CXT5KL5Z` | Beati Faucet | 4,320 | $113,832 | $26.35 |
| 2 | `B0D3X39378` | SHLLKTTRY | 3,150 | $82,625 | $26.23 |
| 3 | `B0GFQ1JRSK` | Canopy | 2,220 | $197,580 | $89.00 |
| 4 | `B0742KFY9R` | Santevia | 1,980 | $45,520 | $22.99 |
| 5 | `B008A4AG2U` | Crystal Quest | 1,800 | $116,910 | $64.95 |

## Top ASIN by `2026-06` revenue
| Rank | ASIN | Brand | `2026-06` units | `2026-06` revenue | `2026-06` price |
|---:|---|---|---:|---:|---:|
| 1 | `B0GFQ1JRSK` | Canopy | 2,220 | $197,580 | $89.00 |
| 2 | `B008A4AG2U` | Crystal Quest | 1,800 | $116,910 | $64.95 |
| 3 | `B0CXT5KL5Z` | Beati Faucet | 4,320 | $113,832 | $26.35 |
| 4 | `B0D3X39378` | SHLLKTTRY | 3,150 | $82,625 | $26.23 |
| 5 | `B0742KFY9R` | Santevia | 1,980 | $45,520 | $22.99 |

## Caveats
- SellerSprite 销量/销售额应视为第三方估算或导出字段，不等于 Amazon 后台真实销量。
- `2026-06` 是 2026-06-18 导出时的月度字段；用于完整月同比/环比判断时，需要确认 SellerSprite 的月度估算口径。
- 历史销量源表中有额外变体 ASIN，已保留在整理工作簿原始页；本 source summary 的汇总只按 listing 文件中的 10 个 bathtub ASIN 统计。

## Best use in KES wiki
- 更新 `bathtub-filter-competitor-pricing-and-kes-v1-price-recommendation` 的竞品价格带和高端/低端对照。
- 更新 `bathtub-filter-amazon-category-and-keyword-baseline` 的竞品规模和 ASIN 排序。
- 在 `bathtub-filter-research-coverage-gaps` 中把竞品销量/销售额历史数据标为已补入，但保留“真实后台销量/退货率仍不可得”的限制。

