---
type: source-summary
status: active
owner: strategy
created: 2026-07-18
updated: 2026-07-18
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [kitchen-farmhouse-sink, fireclay, amazon-us, market-analysis, review-analysis, supply-chain]
source_type: audit
extraction_mode: workbook-reconciliation-pdf-visual-review-and-live-listing-spot-check
source_title: US 单槽 Fireclay Farmhouse Sink 调查资料审核
source_date: 2026-07-18
source_author: Codex
raw_path: ../../raw/products/kitchen-farmhouse-sink/2026-07-16-us-single-bowl-market-research/
verification_status: spot-checked
related:
  - ../market-research/kitchen-fireclay-farmhouse-sink-single-bowl-market-report-2026-07-16.md
  - ../products/kitchen-farmhouse-sink/kitchen-fireclay-farmhouse-sink-single-bowl.md
  - ./kitchen-fireclay-farmhouse-sink-single-bowl-market-report-2026-07-16.md
---

# US 单槽 Fireclay Farmhouse Sink 调查审核（2026-07-18）

## 审核结论

**结论从 `unverified` 提升为 `spot-checked`，但不能提升为 `verified` 或正式立项结论。**

市场页中可由归档工作簿直接复算的核心市场、价格、品牌、内容分布与评分总数已通过。评论主题频数、销量工具估算、实时价格、MMP 和供应商模具 / MOQ 仍未获得足够的独立证据。

## 已通过复算的证据

| 主张 | 审核结果 | 原始证据与复算 |
|---|---|---|
| 目标市场为 11 个商品；月均销量 143；月均销售额 $37,846；平均价 $380.38 | 通过 | `US-Market-keywords` 的 `市场分析概况`；11 个商品销量合计 1,578，1,578 / 11 = 143.45（工作簿显示为 143） |
| Miuara、HOMLYLINK、TUKTUK 占约 82% 销量 | 通过 | `品牌集中度`：492 + 491 + 314 = 1,297；1,297 / 1,578 = 82.19% |
| $150–200、$200–250、$250–300、$300–350、$600+ 的销量分别为 428、829、126、87、108 | 通过 | 按 `商品集中度` 的 11 个商品价格和销量重算；合计 1,578。工作簿的粗分段亦确认 $200–300 为 955 / 60.52% |
| FBA 4 / 11 个商品、1,297 / 1,578 销量；有 A+ 和视频的商品 9 / 11、1,503 / 1,578 销量 | 通过 | `卖家类型分布` 与 `A+视频分布`；即 FBA 82.19%、A+视频 95.25% 样本销量 |
| 评论文件合计 386 条，4–5 星 347 条，1–3 星 39 条 | 通过 | 五个 Review 工作表逐行汇总：1 星 23、2 星 6、3 星 10、4 星 35、5 星 312 |
| 主流方向为 33 inch、白色、fireclay、单槽 | 通过（样本内） | 15-ASIN 竞品导出的标题、规格、材质字段与 11 商品目标市场的标题字段相互一致；不能外推为整个 kitchen sink 类目 |

## 已做的外部交叉检查

2026-07-18 直接查看了三个仍在售的 Amazon 页面。它们确认该产品群的基础产品定义与工作台路线仍存在：

- [Miuara B0B8SWHQ1G](https://www.amazon.com/dp/B0B8SWHQ1G)：33x18、Glossy White、Fireclay、单槽 apron-front，页面给出柜体 / 处置器安装边界与包装、支撑主张。
- [HOMLYLINK B0D5V4XZ3S](https://www.amazon.com/dp/B0D5V4XZ3S)：33x20、Fireclay、workstation；页面列出集成 ledge 和配件路线。
- [DeerValley B0DTHHRSBX](https://www.amazon.com/dp/B0DTHHRSBX)：33x20、Fireclay、workstation；页面列出 cutting board、roll-up rack、bottom grid 与 basket strainer。

这些页面在未登录状态下把价格隐藏在“加入购物车后显示”，所以**没有**用本次公开页面审核确认实时价格、实时销量、评分数或 Amazon's Choice 状态。它们只验证产品存在、路线和页面所列规格；页面自身的材质、耐污、抗划或包装主张不是独立性能证明。

## 未通过或只能部分支持的主张

| 主张 | 审核结果 | 原因与处理 |
|---|---|---|
| 主题编码中的“外观 191、釉面污渍 71、运输破损 32”等频数 | 部分支持 | 386 条和星级分布已复算；但没有提供人工标注规则、逐条标签或可复现脚本。保留为方向性信号，不能视为严格缺陷率。 |
| 评论来自 5 个精确 ASIN | 不通过 | 两个 Review 文件没有 ASIN 列；另有多个空 ASIN 或变体 ASIN。应称“5 个 listing review export pools”，不要称“5 个精确 ASIN 的评论”。 |
| 每个 ASIN 的单一月销量 / 销售额 | 部分支持 | `Market-keywords` 与 15-ASIN `Competitor` 导出对个别同一 ASIN 有轻微差异，例如 B0B8SWHQ1G 492 vs 493、B0C7H1PGD6 391 vs 390、B0D5V4XZ3S 100 vs 108。价格和销量只能按对应表格、对应快照使用。 |
| 当前 Amazon 价格、销量、排名和转化 | 不通过 | 原始数据为第三方工具导出；本次公开 Amazon 页面不显示可审计价格，亦不公开销量 / 转化。保留为 2026-07 的工具快照。 |
| 基础款 MMP $418.89、workstation MMP $458.94 | 不通过 | 这些数值只见于派生市场报告；供应商表可读出人民币出厂价、包装和重量，但没有 MMP 计算表、汇率、头程、FBA、广告、破损或目标利润参数。 |
| 新模具 30–40 万 RMB、首年 MOQ 3,000、连续生产约束 | 不通过 | 供应商 PDF 是产品目录；报价表无这几项。继续作为待确认的采购假设，不能用于 ROI 或库存承诺。 |

## 供应商附件审核

- `A3xin.pdf` 已进行双页视觉审核。它是唐山市丰华陶瓷有限公司的厨房 / 卫浴水槽目录，展示多个型号、图片和尺寸图；不包含报价、MOQ、模具费、认证或质量测试结果。
- `7.25报价20241007（环至美海外仓） .xls` 已转换后读取。其 `Sheet1` 有 8 个产品行，列出光瓷价、包装价、下水器、网格、菜板、卷帘、含税价、出厂价、包装尺寸和重量。用户于 2026-07-18 确认币种为人民币、报价已经过期，但可暂作规划输入。FH-3319K 的过期出厂价为 ¥630.66、包装 960×600×380 mm、重量 36.7 kg；FH-3322SK 为 ¥754.86、包装 960×680×390 mm、重量 40 kg。它们可用于比较基础 / workstation 的相对工厂成本，不用于下单、正式 MMP 或利润承诺。

## 对 wiki 的修订规则

1. 所有市场指标保留为“归档工具快照”并注明样本，而非市场规模或收入事实。
2. 评论主题保留为方向性发现；禁止写成退货率、故障率或整体比例。
3. 成本、MMP、模具与 MOQ 一律维持“待内部财务 / 供应链复核”。
4. 在同一结论中不混用 `Market-keywords` 和 `Competitor` 两份导出的单 ASIN 数值。
5. 只有复算过的市场统计、产品定义和评论总数标为已抽查；产品进入、定价和采购决定仍需人审。

## Sources

- [市场画像页](../market-research/kitchen-fireclay-farmhouse-sink-single-bowl-market-report-2026-07-16.md)
- [原始资料快照](../../raw/products/kitchen-farmhouse-sink/2026-07-16-us-single-bowl-market-research/README.md)
- [Miuara Amazon 页面](https://www.amazon.com/dp/B0B8SWHQ1G)
- [HOMLYLINK Amazon 页面](https://www.amazon.com/dp/B0D5V4XZ3S)
- [DeerValley Amazon 页面](https://www.amazon.com/dp/B0DTHHRSBX)
