---
type: product
status: draft
owner: strategy
created: 2026-07-21
updated: 2026-07-21
visibility: team
confidence: high
officiality: draft
domain: product
domains: [drinking-faucet, z506, baseline, margin, inventory, kes]
source_count: 6
review_cycle: weekly
verification_status: verified-internal
related:
  - ./drinking-faucet.md
  - ./drinking-faucet-air-gap-go-no-go-memo-v1.md
  - ./drinking-faucet-compliance-exposure-p0.md
---

# Z506 经营基线与毛利审计 — 2026-07-21

数据源：prod 只读查询（`mart_listing_health` snapshot 2026-07-17、
`fact_product_business_monthly` / `_daily`、`dim_sku_certification`、`project`）。
置信度高 —— 全部为一手内部数据。

## 一句话

**Z506 是活的，但很薄：需求在长，供给在断，毛利在漏。**

## 1. Listing 全貌（snapshot 2026-07-17）

三个 ASIN：**B0D66NBMJL**（BK）、**B0D66FPSSX**（BS）、**B0GHX4VHBJ**（BZ）。
共 31 条 listing 行，**仅 7 条在售**，其余 24 条是 EU / MX 上的 L9 空壳（无数据）。

| site | SKU | tier | price | rev_30d | rev_90d | rev_180d | u_30d | u_180d | GM_30d | BEP | qty | MOS | inv |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| amz_us | Z506LF-BS | L3 | 38.96 | 1,416 | 8,157 | **14,351** | 37 | 382 | **7.9%** | 28.22 | **0** | – | **oos** |
| amz_us | Z506LF-BK | L3 | 39.21 | 1,142 | 4,217 | 9,938 | 30 | 269 | **−15.5%** | 31.87 | 136 | 4.53 | healthy |
| amz_ca | Z506LF-BK | L2 | 49.32 | 1,350 | 4,689 | 9,007 | 27 | 187 | 3.8% | 44.97 | 67 | 2.48 | healthy |
| amz_us | Z506LF-BZ | L2 | 42.07 | 76 | 2,435 | 6,165 | 1 | 148 | 6.0% | 38.89 | **0** | – | **oos** |
| amz_ca | Z506LF-BS | L3 | 43.99 | 491 | 1,502 | 3,017 | 11 | 71 | **−5.5%** | 39.82 | 14 | 1.40 | healthy |
| amz_uk | Z506LF-BK | L2 | 25.68 | 296 | 712 | 1,365 | 8 | 38 | 22.6% | 27.79 | 13 | 1.62 | healthy |
| amz_uk | Z506LF-BS | L2 | 24.36 | 294 | 887 | 1,303 | 9 | 39 | **−28.8%** | 24.53 | 10 | 1.25 | healthy |

`hd_us` 有一条 Z506LF-BK，oos 且零营收。

⚠️ **金额是本币，CA / UK 不是 USD，不要跨站直接 SUM。**
US 单站 180 天约 **$30.5k**；全站 180 天约 **1,134 件**。

## 2. 毛利：结构性问题，不是波动

**七条在售 listing 中三条低于盈亏平衡：**

- **amz_uk Z506LF-BS：−28.8%**（售价 24.36 vs BEP 24.53）
- **amz_us Z506LF-BK：−15.5%**（售价 39.21 vs BEP 31.87）
- **amz_ca Z506LF-BS：−5.5%**（售价 43.99 vs BEP 39.82）

最好的 amz_us BS 也只有 **7.9%**。amz_uk BK 的 22.6% 是唯一健康的，但量最小（8 件/30天）。

⚠️ 注意 US BK 的怪异之处：售价 39.21 **高于** BEP 31.87，GM 却是 −15.5%。
这说明 GM_30d 的计算里含有 BEP 未覆盖的成本项（大概率是广告费 / TACoS）。
**修毛利前必须先拆清楚这两个口径的差**，否则会误判成"提价就能解决"。

**量增救不了负毛利。** 这条线现在跑得越多，亏得越多的那几个 SKU 亏得越多。

## 3. 趋势：需求在长，4 月后的跌是断货不是衰退

全站月度件数 / 营收：

```
2024-12   109u /  3,978
2025-04    75u            ← 谷底
2025-08   215u /  8,708
2026-01   106u /  4,191
2026-02   188u
2026-03   189u
2026-04   304u / 12,493   ← 峰值
2026-05   224u /  9,195
2026-06   139u /  5,731
2026-07    68u /  2,863   (19 天)
```

**2026 年 YTD 显著高于 2025**（2-4 月均 227 件/月 vs 2025 年约 130 件/月），
run-rate 大致翻倍。

**4→7 月的跌已在库存历史中确认为供给造成：**
- BZ：`sellable_qty` 3 → 1 → 0，4 月起 `low`，**07-15 转 oos**
- BS：52 → 38 → 8 → 0，**07-15 转 oos**。BS 有货时 5 月做到 **99–105 件/30天**
- BK 全程 healthy

⚠️ **但 BK 是个例外，需单独查**：它没断货，`units_30d` 却从 63 滑到 29。
这不是库存故事，可能是排名、广告或竞品挤压。**不要和断货一起归因。**

⚠️ 数据口径：`fact_product_business_monthly` **全平台性滞后**，
`max(month_start)` = 2026-04-01（落后约 3 个月）；5 月起的数字来自 daily 表（到 2026-07-19）。

## 4. 词域表现：KES 在这个品类基本不存在

`amz_us` 近 8 周，42 个 RO / 净水龙头相关词上，**`is_own_asin_1/2/3` 全为 False**。

三个 Z506 ASIN 的反查在**所有周**只返回 2 行，都在 slot 2/3、约 250 万排名的边缘词
（`black drinking water faucet`、`reverse osmosis water filter faucet`）。

词域由 **B09XXL2PQB**（多数头词点击份额第一）和 **B07MLSVLZH**（PUR）占据。

**含义**：Z506 目前的销量不是靠品类词拿到的。这条线的自然流量地基很薄，
增长可能高度依赖广告 —— 这与第 2 节 US BK "售价高于 BEP 但 GM 为负"的现象互相印证。
**建议下一步拉 `fact_ba_search_query_perf_weekly` 看这三个 ASIN 的真实流量来源构成。**

## 5. 研发注意力现状

`project` 表中 `category_id = drinking_faucet` 的仅 3 行，全是 Z507 / Z504 的
`listing_quick_fix` 类目美化，与 Z506 无关，与 air gap 无关。

按名称搜到的在跑项目：
- **`Z506EU.V1.0`**（open，2026-07-09 建）— EU 版本
- `Z50系列净水龙头包装优化`
- `厨房-Z507净水龙头-复古款式+金属接头`
- 若干素材 / 3D 任务

**当前研发注意力在 EU 扩张与 Z507，没有人在做 air gap —— 与数据结论一致。**

`rc_*` 表中该品类**零**竞品 / 细分 / 市场分析行。27 条匹配 air-gap / RO 词的
`rc_keyword` 属于两个无关的浴室过滤 workspace（浴缸过滤、顶喷除氯过滤），
且无一条带 `search_volume`。

## 6. 建议动作（按优先级）

| 优先级 | 动作 | 理由 |
|---|---|---|
| **P0** | 核实并补齐在售 SKU 的 NSF61 / NSF372 / cUPC | 见[合规敞口](./drinking-faucet-compliance-exposure-p0.md)，美国在售饮用水龙头的实质风险 |
| **P1** | 补货 BS / BZ | BS 有货时约 100 件/30天，现在归零。**这是当前最高杠杆的单一动作** |
| **P2** | 拆 US BK 的 GM 口径，定位 −15.5% 的成本项 | 提价还是砍广告，取决于这一步的结论，不要跳过 |
| **P2** | 重定价 UK BS（−28.8%）与 CA BS（−5.5%） | 或直接下架 UK BS —— 量只有 9 件/30天，不值得亏着卖 |
| **P3** | 查 BK 未断货却量滑 63→29 的原因 | 唯一无法用库存解释的负向信号 |
| **P3** | 清理 24 条 EU / MX L9 空壳 listing | 与 `Z506EU.V1.0` 项目合并处理 |
| **P3** | 修 `backfill_product_taxonomy.py:157` 的 L1 映射错误 | 见[总览](./drinking-faucet.md) |
