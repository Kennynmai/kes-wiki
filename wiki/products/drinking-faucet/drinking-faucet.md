---
type: product
status: draft
owner: strategy
created: 2026-07-21
updated: 2026-07-21
visibility: team
confidence: medium-high
officiality: draft
domain: product
domains: [drinking-faucet, ro-faucet, air-gap, kes, z506]
source_count: 40
review_cycle: monthly
verification_status: working
related:
  - ./drinking-faucet-air-gap-go-no-go-memo-v1.md
  - ./drinking-faucet-z506-baseline-and-margin-audit.md
  - ./drinking-faucet-compliance-exposure-p0.md
  - ./drinking-faucet-assumption-register.md
  - ./drinking-faucet-air-gap-evidence-register.md
  - ./drinking-faucet-new-product-opportunity-stress-test.md
  - ../bathtub-filter/
  - ../rv-bathroom-sink-faucet/
---

# Drinking Faucet（直饮龙头 / RO 龙头）— 品类总览

## 这个目录为什么存在

2026-07-21，一个问题触发了本次调查：**air-gap RO 龙头是否值得开发新品进入？**

调查过程中发现一件更重要的事：**KES 已经在卖这个品类**（SPU `Z506`），但平台里从未对它做过一次系统性研究。品类骨架（分类节点、SKU 规则、需求词典、合规规则、CS 故障本体）全都在，唯独没有研究资产。

所以本目录同时承担两件事：
1. 回答 air-gap 这个具体问题（答案：**No-Go**）
2. 补上 `drinking_faucet` 这个**在售品类**的研究基线

## 品类在 KES 内的坐标

| 项 | 值 |
|---|---|
| L2 code | `drinking_faucet`（`category_id` = `c6603169-fabe-4675-ac56-68bb3fbed8d8`） |
| L2 中文名 | 直饮龙头 |
| **真实 L1** | **`KITCHEN_FAUCET`**（L0 = KITCHEN） |
| SKU 规则组 | `Z5` — regex `^Z5\d{3}F\d{2}(-[A-Z]{2,3})?$` |
| 在售 SPU | `Z506`（变体 `-BK` / `-BS` / `-BZ`，`LF` = Lead Free） |
| 在研项目 | `Z506EU.V1.0`（open，2026-07-09 建）、Z507 复古款、Z50 系列包装优化 |

⚠️ **已知代码缺陷**：`scripts/adhoc/backfill_product_taxonomy.py:157` 把
`WATER_PURIFICATION_UNIT__Z506` 映射为 `("FAUCET", "drinking_faucet")`，但 `FAUCET`
是挂在 **BATHROOM** 下的 L1，不是 `drinking_faucet` 的祖先。真实 L1 是 `KITCHEN_FAUCET`
（`sku_rule_groups.py` 是对的）。另外 prod 里 Z506 的 `product_type` 实际是
`KITCHEN_FAUCET` 而非 `WATER_PURIFICATION_UNIT`，所以该 backfill 规则很可能从未触发。
按 L1 聚合的品类分布报表需要核对是否受影响。

## 本目录文件

| 文件 | 回答什么 |
|---|---|
| [go/no-go 备忘录](./drinking-faucet-air-gap-go-no-go-memo-v1.md) | air-gap 变体要不要立项 → **No-Go** |
| [新品机会压力测试](./drinking-faucet-new-product-opportunity-stress-test.md) | 除 air-gap 外还有什么新品机会 → **评论量差竞品150倍才是真根因**，finish 差异化机会大部分被推翻 |
| [Z506 经营基线与毛利审计](./drinking-faucet-z506-baseline-and-margin-audit.md) | 这条线现在是死是活 → 活但薄，且正在断货 |
| [P0 合规敞口](./drinking-faucet-compliance-exposure-p0.md) | 在售 SKU 的饮用水认证记录缺失 |
| [假设台账](./drinking-faucet-assumption-register.md) | 结论建立在哪些假设上，哪条塌了要翻案 |
| [证据台账](./drinking-faucet-air-gap-evidence-register.md) | 每条论断的来源、置信度、以及**没查到的窟窿** |

## 一句话结论

**air-gap 变体：No-Go。** 不是因为做不出来（工艺不难），也不是因为专利挡路（核心构型 2025-09 已过期进入公有领域），而是需求池是长尾限定词、架构性差评不可控、同赛道中国品牌已集体撤出。

**新品机会（非 air-gap）：真根因是评论量落后头部竞品 WEWE 约 150 倍（90-98 条 vs 14,362 条），不是颜色/关键词/类目。** 任何新变体开局评论都是零，会重复同样的命运。压力测试后唯一站得住的方向是"给 Z69 主龙头做过滤集成款，绝不加联网"；finish 差异化（香槟古铜/金色）已被真实竞品数据推翻。详见[压力测试文档](./drinking-faucet-new-product-opportunity-stress-test.md)。

**Z506 主线：值得投入，但方向是补货 + 修毛利 + 补认证 + 攒评论，不是开新变体。**

## 可复用的相邻研究

- `../bathtub-filter/` — 约 80 篇，北美水接触认证/合规/claim 方法论最完整的一套，**不要重跑**
- `../rv-bathroom-sink-faucet/` — 龙头域方法论模板（本目录结构照它来）
- `kenny-wiki/wiki/brand-studies/` — waterdrop / frizzlife / brita / coway 等净水品牌 DTC 案例
