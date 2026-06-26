---
type: source-index
status: draft
owner: strategy
created: 2026-06-18
updated: 2026-06-18
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, raw-ingestion, competitor-intelligence]
source_type: mixed-raw-import
verification_status: spot-checked
---

# Bathtub Filter 2026-06-18 资料写入索引

## 写入位置
本次把桌面和工作区中尚未进入正式 `kes-wiki` 的 bathtub filter 资料补入正式知识库：

- 桌面源资料快照：`raw/products/bathtub-filter/2026-06-18-desktop-source-folder-import/`
- 竞品 listing + 历史销量数据包：`raw/products/bathtub-filter/2026-06-18-competitor-listing-sales/`
- source summary：`wiki/source-summaries/bathtub-filter-competitor-listing-sales-2026-06-18.md`

## 口径修正
`B0FNVDJRSQ` 是 Filterbaby shower filter / showerhead inline 产品，不属于 bathtub filter。本次复核后：

- 不纳入 2026-06-18 bathtub competitor listing/sales 10-ASIN 口径。
- 不保留在 bathtub filter 的 2026-04-20 评论语料 source-files 中。
- 对应资料保留在 `raw/products/shower-filter/2026-04-20-filterbaby-review-corpus/` 和 `wiki/products/shower-filter/`。

## Raw 包说明
| Raw package | 用途 | 文件数 | 备注 |
|---|---|---:|---|
| `2026-06-18-desktop-source-folder-import` | 桌面“浴缸过滤”资料快照 | 42 | 保留产品结构、测试、供应商报告、竞品资料源文件；不等于已验证结论 |
| `2026-06-18-competitor-listing-sales` | 10 个 bathtub 竞品 ASIN 的 listing + 历史销量分析包 | 3 | 含两个原始 Excel 和一个整理工作簿 |

## 竞品销量快照关键数
- Bathtub ASIN：10 个
- Listing 月销量合计：15,347
- Listing 月销售额合计：$609,805
- 历史销量表 `2026-06` 销量合计：15,330
- 历史销量表 `2026-06` 销售额合计：$617,149
- 近 12 月销量合计：176,739
- 近 12 月销售额合计：$6,315,297

## 下一步建议
- 将 `bathtub-filter-competitor-pricing-and-kes-v1-price-recommendation` 与这批 2026-06-18 竞品价格/销量快照对齐。
- 将测试、供应商报告和结构视频按主题拆成 source summaries，再决定是否更新 claim register、R&D roadmap、testing protocol。

