---
type: product
status: draft
owner: strategy
created: 2026-04-17
updated: 2026-04-18
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, amazon, category, keyword, listing, gtm, marketplace]
source_count: 6
review_cycle: quarterly
verification_status: working
related:
  - ./bathtub-filter-marketplace-claim-policing-layer.md
  - ./bathtub-filter-channel-admission-requirements.md
  - ./bathtub-filter-competitor-pricing-and-kes-v1-price-recommendation.md
  - ./bathtub-filter-research-coverage-gaps.md
---

# Bathtub Filter — Amazon 类目 & 关键词 baseline（2026-04 抓取）

## 为什么有这页

Gap doc C4 层（marketplace claim policing）此前在框架层判定 Amazon 是 KES 第一战场，但**没列具体类目分配 + 竞品 listing 关键词 baseline**。这页用 2026-04 实际 ASIN 抓取数据填上。

## 1. 竞品 ASIN × Amazon 类目分配

| 竞品 | ASIN | Amazon 类目 breadcrumb（实测）|
|---|---|---|
| Sprite Showers BB-WH | B08Y8GSVJS | Tools & Home Improvement → Plumbing → Faucet Water Filters |
| Sprite Showers BB-TB Ball | B016M167GG | Tools & Home Improvement → Plumbing → Faucet Water Filters |
| Crystal Quest Premium Bath Ball | B008A4AG2U | Tools & Home Improvement → Plumbing → Faucet Water Filters |
| Tubo 2.0 Bath Filter | B0FZCR8VGB / B0DTQ8H23D | **Tools & Home Improvement** |
| Santevia Organic Cotton | B0742KFY9R | Tools & Home Improvement / Health & Household 跨类 |
| Canopy Bath Tub Filter | (DTC + Babylist 主) | Health & Household → Health Care |
| FilterBaby Skincare 2.0（参照非 bath）| B0FDKQJMJY | **Tools & Home Improvement** |
| Kinder / Curety / Beati 同源白牌 | B0DLZ4KD26 / B0DHX993MV / B0CXT5KL5Z | Tools & Home Improvement |

## 2. KES V1 类目选择

**默认推荐：Tools & Home Improvement → Plumbing → Faucet Water Filters**

理由：
- 当前 5 个主竞品（Sprite, Crystal Quest, Tubo, Santevia, Kinder 同源）都驻扎在此
- A9 search relevance：用户搜 "bath filter" / "bathtub filter" / "faucet filter" → 这个类目直接命中
- 不触发 Health & Personal Care brand-gating 风险

**避免：**
- ❌ Health & Household → Health Care（Canopy 占据，但触发 brand approval 流程更严，Amazon 对 health claim 审查更严格）
- ❌ Beauty & Personal Care（FilterBaby skincare 路线，但 KES 是 bath 不是 face → 错位）
- ❌ Baby Products（CPSIA + 严格审查 + 与 Canopy 直撞）

## 3. 竞品 listing 关键词 baseline

提取自竞品 listing title + bullet：

### 3.1 高频核心词（≥3 个竞品共用）

| 关键词 | Sprite | Tubo | Santevia | Crystal Quest | Canopy | Kinder | KES 推荐 |
|---|---|---|---|---|---|---|---|
| bath filter / bathtub filter | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✅ 必带 |
| chlorine | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✅ 必带（V1 唯一可 claim 的去除目标）|
| faucet | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✅ 带（A9 SEO；但参考 [[bathtub-filter-filterbaby-patent-fto-analysis]] 留意 patent 语义） |
| skin / hair | ✓ | ✓ | ✓ | — | ✓ | ✓ | ⚠️ 可带"sensitive skin" / "softer skin"，避"healthier skin" claim |
| BPA-free | — | ✓ | — | ✓ | — | — | ✅ 带（材料 spec 实事陈述）|
| baby | — | ✓ | — | — | ✓ | — | ⚠️ 触发 CPSIA 路径——若包装出现 baby 字样必须做 lead test |
| 99% / 99.9% removes | — | ✓ | — | ✓ | — | ✓ | ❌ **不带**（无 NSF cert 是 FTC substantiation 风险）|
| eczema | — | ✓ (官网) | — | — | — | ✓ (官网) | ❌ **不带**（FDA medical claim）|

### 3.2 高级 SEO 词（差异化）

| 词 | 竞品已占 | KES 可借力？ |
|---|---|---|
| "hard water softener" | Kinder / Curety | ⚠️ 不可（KDF/CaSO₃ 不软化） |
| "removes fluoride" | Tubo / Kinder | ❌ 不可（KDF 不去 fluoride，FTC 风险） |
| "removes chloramine" | Crystal Quest | ⚠️ 不可（V1 KDF/CaSO₃ 对 chloramine 弱） |
| "vitamin C bath filter" | Sprite (Chlorgon) 间接 | ❌ 不带（KES 无 vit C 介质则虚假宣传） |
| "BPA-free silicone soft cover" | Canopy 独占 | ✅ 若 KES 有类似 cover 可借 |
| "tested by [lab]" | 多 | ✅ 推荐（具体到 lab name） |
| "tool-free install" | Canopy / Tubo | ✅ 若 KES 满足可借 |
| "fits standard tub spout" | 多 | ⚠️ "fits most tubs" 是结构性谎言（见 [[bathtub-filter-competitor-review-corpus-2026-04]]）—— 改用 "tested compatible with [list]" |

### 3.3 KES V1 推荐 listing title 框架

```
KES Bath Tub Filter — Removes Free Chlorine | Tool-Free Install,
BPA-Free, Tested for [Specific Spout Types] | Designed for
Sensitive Skin Routines
```

注意：
- 不出现 "99%" 数字（除非 NSF cert）
- 不出现 "eczema" / "baby" / "skin treatment"
- 主动列 spout compatibility 边界
- 用 sensory 词替代 medical 词

## 4. Sponsored / PPC 关键词起手包

按 KES V1 类目 + 心智优先级：

**Tier 1（必投 head terms）：**
- bath filter / bathtub filter
- chlorine bath filter
- bath water filter
- bathtub water filter

**Tier 2（mid-tail conversion）：**
- bath filter for sensitive skin
- bath water filter chlorine reduction
- tool-free bath filter
- bath spout filter
- bathtub faucet filter

**Tier 3（long-tail，低 CPC + 高意图）：**
- bath filter for hard water area chlorine
- bath spout chlorine filter renter friendly
- bath filter does not require tools

**避投：**
- ❌ "bath filter eczema" / "baby bath filter" / "skincare bath filter" — 高 CPC + Canopy/FilterBaby 占位 + KES claim 风险
- ❌ "chloramine bath filter" — V1 不去 chloramine
- ❌ "fluoride bath filter" — V1 不去

## 5. BA 关键词实测更新（2026-04-17 / 04-18）

> 来源：`kes-ops-platform` BA 扫描（report 04-17 step1 + report 04-18 README）。数据窗口最新到 2026-03-22。

### 5.1 核心词 SFR（Search Frequency Rank，US）

| 关键词 | SFR（04-17）| SFR（04-18）| Canopy click share |
|---|---|---|---|
| `canopy bathtub filter` | 65,874 | 63,844 | 17.0% |
| `bath filter for tub` | — | 88,333 | 20.0% |
| `bathtub filter` | 102,223 | 105,780 | 21.8% |
| `bath tub filter` | 110,413 | 109,598 | 30.3% |
| `bath filter` | — | 118,720 | 14.4% |
| `bathtub water filter` | 125,285 | 140,301 | 13.2% |
| `bathtub filter for tub faucet` | — | 225,764 | 22.1% |
| `canopy bath filter` | — | 282,995 | **75.9%** |
| `tub filter` | — | 306,991 | 20.2% |
| `bath filter for baby` | — | 311,326 | 17.7% |

**关键观察：**
- Canopy 垄断全部品类词 Top-1 点击，`canopy bath filter` 精准词 click share 高达 75.9%
- `bathtub filter` 主词 SFR 从 04-17 的 102K 到 04-18 的 105K（小幅波动，品类体量稳定）
- 品牌词 `canopy bathtub filter` SFR 63,844，持续领先品类通用词——**品牌驱动品类**格局确认

### 5.2 相邻品类对比：shower filter vs bathtub filter

| 品类 | 最优 SFR（US，最新周）| 相对体量 |
|---|---|---|
| `shower filter` | **3,328** | 基准 |
| `bathtub filter` | 65,874（Canopy 品牌词）| **~1/20** |

Shower filter 是成熟红海（Aquabliss 等 10+ 玩家，头部 click share 只有 27%）；bathtub filter 是 Canopy 主导的单寡头早期品类。两者核心技术相同（KDF/活性炭），只有安装位置不同。

### 5.3 Google Trends 5 年数据（SerpAPI 2026-04-17，bathtub filter，美国）

| 时期 | Trends 值（0–100）| 备注 |
|---|---|---|
| 2021–2025 历史基线 | 0–9 | 几乎无搜索 |
| 2022-03 历史峰值（之前）| 9 | 当时最高点 |
| 2026-03-08 | 26 | 开始起飞 |
| **2026-03-29** | **100** | 🚀 5 年历史最高，= 2022 峰值 **11 倍** |
| 2026-04-05 | 42 | 高位回落 |
| 2026-04-12 | 43 | 仍 = 历史基线 **5 倍** |

**Rising 词（增速最快）：**
- `canopy bath tub filter`：**Breakout（>5000%增速）**
- `how to install bathtub faucet`：Breakout（品类教育需求被带动）
- `canopy`：+1,450%
- `canopy bath filter`：+800%
- `filter baby`：+100%（竞品 FilterBaby 同步上升）

Canopy 2026-01 上市 → 2026-03 末全品类搜索量指数爆发。品类仍处于早期教育窗口期。

### 5.4 Canopy 多渠道分布（Google Shopping 2026-04-17）

| 渠道 | 价格 | 战略含义 |
|---|---|---|
| Amazon | $89 | 品牌曝光渠道（自然排名 pos=14，依靠 pull 拉流量）|
| **Target** | **$69.99** | 实体零售比 Amazon 便宜 **21%**——Amazon 不是主战场 |
| **Sephora** | $89 | 美妆/护肤渠道，产品被定位为"护肤工具"非"管道配件" |
| **Babylist** | $89 | 美国最大宝宝注册礼品单平台，锁定新生儿家庭场景 |
| Wayfair | $104.99（高端线 TENicas）| 价格带完整 |
| Walmart | $17.90（PUREPLUS）| 白牌低端线 |

**KES 含义：** Canopy 已完成 Amazon + 实体零售（Target）+ 美妆（Sephora）+ 母婴（Babylist）的多渠道布局，且 Target 价格故意低于 Amazon——KES 进入时若只铺 Amazon 将面对已多渠道成型的竞品。

## 6. 还卡在哪里（必须人工/外部完成）

- [ ] 真实 SEO tool（Helium 10 / JungleScout / Sellics）抓取竞品 keyword volume + CPC，验证本页推断
- [ ] Amazon Brand Registry 申请（trademark 必备 prereq）
- [ ] A+ content 定稿（视觉 + claim language 必须 legal review）
- [ ] Sponsored Brand video 制作（chlorine drop test demo）
- [ ] 实测 listing 上架后 30 天 ranking 起步状态

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-marketplace-claim-policing-layer]]
- [[bathtub-filter-channel-admission-requirements]]
- [[bathtub-filter-competitor-review-corpus-2026-04]]
- [[bathtub-filter-competitor-pricing-and-kes-v1-price-recommendation]]
- [[bathtub-filter-filterbaby-patent-fto-analysis]]
- [[bathtub-filter-claim-risk-audit-v2]]
- [[bathtub-filter-community-language-compression-patterns]]
- [[bathtub-filter-research-coverage-gaps]]
