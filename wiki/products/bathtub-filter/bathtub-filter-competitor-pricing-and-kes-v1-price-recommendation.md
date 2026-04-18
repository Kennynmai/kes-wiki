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
domains: [bathtub-filter, pricing, unit-economics, refill, kes-v1, gtm]
source_count: 9
review_cycle: quarterly
verification_status: working
related:
  - ./bathtub-filter-pricing-refill-flow-fit-table-v2.md
  - ./bathtub-filter-channel-positioning-table-v2.md
  - ./bathtub-filter-kes-concept-brief-v1.md
  - ./bathtub-filter-competitor-review-corpus-2026-04.md
  - ./bathtub-filter-research-coverage-gaps.md
---

# Bathtub Filter — 竞品定价 & KES V1 价格建议（2026-04）

## 为什么有这页

Gap doc D 层（pricing/unit econ）此前是 🟡 框架——只列结构，没有 KES V1 的推荐 MSRP 起点。这页用 2026-04 实际抓取的**6 个竞品 unit + refill + cycle**数据，建一张可比表，并给 KES V1 一个**可辩护的价格区间起点**。

> ⚠️ 这是 GTM-side 价格建议，**不是 COGS 模型**。最终 V1 价格取决于 BOM + 渠道 margin 要求 + CAC，那些数据需供应链 + finance 提供，本页不能替代。

## 1. 竞品定价速查表（2026-04 抓取）

| 品牌 | Unit MSRP | Refill MSRP | Refill 周期（厂商声明）| 估算每浴成本 | 订阅折扣 | 渠道 |
|---|---|---|---|---|---|---|
| **Santevia** Organic Cotton | $19.99 | ~$20（替换整个 filter，无 housing/cartridge 分离） | 2 月 / ~100 baths | **~$0.20/bath** | bulk discount | DTC + Amazon |
| **Sprite** BB-WH/BB-TB | $32.99 | $15.99 (BBC cartridge) | 25–30 baths（~30 天）| **~$0.55/bath** | n/a | Home Depot + Amazon + DIY 渠道 |
| **Crystal Quest** Bath Ball | ~$65 | ~$40 ($43.45 retail) | 12–18 月 / 2,000–2,500 gal | **~$0.40/bath**（按 50gal/浴）| n/a | DTC + Amazon |
| **Tubo** 2.0 | ~$65 | ~$35 | 6–8 月 / 2,500 gal | **~$0.35/bath**（声明若成立）| 2-yr supply bundle | DTC + Amazon |
| **Canopy** Bath Tub Filter | **$89** | $37 (one-time) / $27 (subscription) | 90 天 | **$0.41/bath**（one-time）/ **$0.30/bath**（sub）| **$10/cartridge** off | DTC + Babylist + Amazon |
| **Kinder** / Curety / Beati 同源白牌 | $20–35（Walmart clearance $15+） | 不透明 | 厂商声明 10–12 月 | 不可计算 | 不透明 | Amazon + Walmart |

**FilterBaby**（faucet filter，非 bath）作为 reference：subscription 90-day cycle，定价不透明但目标人群 / 价位 premium DTC（~$60 unit + ~$25/refill 估算）。

## 2. 关键 pattern

### 2.1 价位的 3 个 cluster

```
Cluster 1 — 入门/Amazon 白牌      $15 – $35     Sprite BB / Santevia / Kinder OEM 群
Cluster 2 — DTC mid-premium       $50 – $75     Tubo / Crystal Quest
Cluster 3 — Premium DTC + retail  $85+          Canopy
```

**没有品牌占据 $35–$50 区间**——这是 Cluster 1 的天花板和 Cluster 2 的地板之间的间隙。

### 2.2 Refill 经济性差异极大

按"厂商声明寿命"算 per-bath 成本：

```
最便宜:  Santevia    ~$0.20/bath   （但实际 mold/odor 投诉，真实寿命可能 <声明）
中位数:  Tubo / CQ   ~$0.35–0.40   （但实测 chlorine 不去，相当于"为没用的服务付钱"）
中位数:  Canopy sub  ~$0.30/bath   （订阅锁定 + 真实 90 天 cycle）
最贵:    Sprite BBC  ~$0.55/bath   （25-30 bath cycle 短，refill cost 频率高）
```

**关键发现：用户感知的"贵"不是 MSRP 而是 refill cadence × refill cost。** Sprite 表面 $33 便宜，但 30-day cycle 让 12 个月 refill 总支出超过 $190。Canopy 表面 $89 贵，但 12 个月 refill (sub) 是 $89 + $108 = $197——**两者 12 个月 TCO 差不多**。

### 2.3 Refill cycle 的"诚实差距"

| 品牌 | 厂商声明 cycle | review/lab 反映的真实 cycle |
|---|---|---|
| Santevia | 60 天 / 100 baths | **mold/odor 在 ~45–60 天出现**——上限其实就是声明时间 |
| Sprite | 25–30 baths | 一致 |
| Crystal Quest | 12–18 月 | **Lab 显示一开始就不去氯**——cycle 概念本身无意义 |
| Tubo | 6–8 月 | **Lab 显示一开始就不去氯**——同上 |
| Canopy | 90 天 | 一致（fast-flow 性能差，但 90 天 cycle 本身一致） |

**KES V1 含义：** 不要在声明 cycle 上做 marketing 优势。Santevia / Canopy 的 90 天 cycle + 实际表现是市场上最诚实的——KES 应**至少持平**，理想是用 silver-ion / 强媒介组合做到"90 天 cycle 同时 fast-flow 100% 去氯"。

### 2.4 订阅模式只有 1 家做透

只有 **Canopy** 和 **FilterBaby** 跑通订阅。Tubo 走"2-yr bundle"（一次性大单，不是 recurring）。这意味着：

- KES V1 进 DTC 时，订阅是 **未充分饱和的 LTV 工具**
- 但订阅模型要求 product 必须 **足够诚实**（用户不会订阅一个让他们失望的产品）
- 订阅折扣 baseline：Canopy 给 $10/cartridge off（约 27% off）

## 3. KES V1 推荐价格区间（GTM-side 建议）

> ⚠️ 这是 **市场对位建议**，不替代 COGS 反推。最终价格由 BOM + 30–45% 渠道 margin + CAC payback 决定。

### 3.1 推荐定位：Cluster 2 顶 / Cluster 3 底

**单元 MSRP 区间：$59 – $79**

理由：
- 低于 Canopy ($89) 8–25%——直接攻 Canopy 价格 vs 性能 gap
- 高于 Tubo / Crystal Quest 0–22%——避开"OEM 白牌"价位陷阱
- 占据当前空缺的 $35–$50 vs $85+ gap——**$59 是这个 gap 的中点**
- 给 wholesale margin 留空间（若进 Target / babylist）

### 3.2 Refill 价格区间：$24 – $32（标准），$19 – $27（订阅）

理由：
- Canopy 标 $37 / 订阅 $27 — KES 持平或低 5–10% 是直接对标击杀
- Per-bath 目标：**$0.27–0.35/bath（订阅）** —— 与 Canopy 订阅持平
- 90 天 cycle baseline 必须持平，**不要尝试 long-cycle 故事**（Crystal Quest / Tubo 已被 lab 证伪）

### 3.3 SKU 结构推荐

```
Starter Kit            $59–$79      Housing + 1 cartridge
Refill 1-pack          $24–$32
Refill Subscription    $19–$27/90 天      Auto-ship
Refill 4-pack bundle   $79–$99       (~22% bulk discount，对标 Tubo bundle)
```

### 3.4 为什么不应进 Cluster 1（$15–$35）

- 直接对位 Sprite / Santevia / Kinder OEM——**KES 没有 cost-base 优势打败 OEM 白牌**
- 价位决定 review 严格度——$25 用户对失败 forgiving，$60+ 用户严格
- premium 价位才能支撑 DTC CAC + 订阅 LTV
- baby/skincare 心智不能与 $20 white-label 共存

### 3.5 为什么不应进 $90+（Canopy 价位）

- Canopy 已用 $89 + premium 美学 + Babylist + Motherly 锁定 premium baby 心智
- KES 进入此价位需要 **持平** Canopy 的零售面 + brand authority + 设计语言——**12 个月内做不到**
- $80+ 触发"我必须每件事都不出错"压力（参考 Canopy 实际 review：fast-flow 50% 翻车）
- $89 → 99 跳跃几乎无 ROI（消费者 friction 锐增，渠道也会 push back）

## 4. Wholesale / 渠道含义

按推荐 $59–$79 MSRP 反推渠道经济：

| 渠道 | Margin 期望 | KES 收入（per unit） |
|---|---|---|
| DTC (Shopify) | 100% retain | $59–$79 - 处理成本 |
| Amazon FBA | ~85%（FBA fee 取决于尺寸） | $50–$67 |
| Target / Babylist 直采 | 50–55% wholesale discount | $27–$38 |
| Home Depot category（1P） | 45–50% | $30–$43 |
| Costco（如适用） | 45%+ | $32–$43 |

**反推 BOM 上限：** 若 KES 想保留 30%+ EBIT 在 wholesale，**unit BOM 必须低于 $15**（含包装），refill BOM 低于 $5。这与 [[bathtub-filter-pricing-refill-flow-fit-table-v2]] 早期假设区间一致。

## 5. 价格 messaging（基于已有 community language compression）

参考 [[bathtub-filter-community-language-compression-patterns]] 骨架 6（"price legitimacy"）：

**推荐 messaging：**
- ✅ "$59 — less than 2 months of [premium baby moisturizer / 你目前的护肤品]"
- ✅ "$0.27 / bath when you subscribe — about the cost of a coffee per week"
- ✅ "Designed for hard-water + chlorine-heavy regions: see if your zip qualifies"
- ❌ 不要 "best value" / "cheapest premium" — 直接触发 Water Filter Guru 比较
- ❌ 不要 "limited time" / "while supplies last" — 触发 FTC scarcity guides

## 6. 还卡在哪里（必须人工/外部完成）

- [ ] 实际 BOM / COGS 反推（供应链团队）
- [ ] CAC payback 模型（marketing 团队）
- [ ] Wholesale margin 谈判（实际 buyer 反馈，不是公开 spec）
- [ ] 订阅 churn 假设建模（需上市 60 天后真实数据）
- [ ] EU/UK 价格本地化（VAT + 不同 wholesale 习惯）
- [ ] 中文消费者市场价格（如 KES 进 CN/TW，价格逻辑完全重排）

## 7. 竞品全景扩充（2026-04-18 Rainforest 13 ASIN 扫描）

> 来源：`kes-ops-platform` report 04-18 cross_site_matrix + dimension_matrix（US / CA / UK / DE / JP 5 站点）。

### 7.1 新增 ASIN（之前未覆盖）

| ASIN | 品牌 | US 价格 | US 月销估算 | housing_material | filtration_approach | 备注 |
|---|---|---|---|---|---|---|
| B0FNVDJRSQ | **Filterbaby** | **$113** | 1K+ | metal_titanium | baby_sensitive_skin | 最高价位，faucet_mount 安装 |
| B0FT7R9ZQ9 | JYFJYF | $16 | 1K+ | other | multi_stage | velcro_strap 安装，最低价入门 |
| B0G5NZBW6W | Syvahome | $30 | 50+ | other | vitamin_mineral | 新品，销量低 |
| B0FL24SLM5 | Yolycen | $16 | 50+ | other | vitamin_mineral | overflow_integrated 安装 |
| B0GKT5CHYL | Uiuaquas | $72 | — | other | multi_stage | 无 US BSR，CA 有少量 |
| B0D3X39378 | SHLLKTTRY | $26 | 1K+ | plastic_abs | multi_stage | overflow_integrated，CA 主场 |
| B0D78XBHSW | Beati Faucet | $24 | 1K+ | other | multi_stage | US BSR 与 B0CXT5KL5Z 同 #1178 |

### 7.2 更新竞品核心数据（2026-04-18 实测）

| ASIN | 品牌 | US 价格 | US BSR | CA BSR | UK BSR | 月销 | housing |
|---|---|---|---|---|---|---|---|
| B0CXT5KL5Z | **Beati Faucet** | $30 | **#1178** | #64100 | ✗ | 2K+ | other |
| B0GFQ1JRSK | **Canopy** | $89 | #4173 | ~ | #184191 | 500+ | silicone |
| B0742KFY9R | **Santevia** | $23 | ~ | **#259** | #12572 | 1K+ | fabric_cotton |
| B0FNVDJRSQ | **Filterbaby** | $113 | ~ | #429475 | #149031 | 1K+ | metal_titanium |
| B0DTQ8H23D | **Tubo** | $65 | ~ | #80673 | #84403 | 800+ | plastic_abs |
| B008A4AG2U | **Crystal Quest** | $65 | ~ | #53583 | #125925 | 500+ | plastic_abs |

**关键发现：**
- Beati Faucet 实际 BSR #1178（比 Canopy #4173 高得多），是 Amazon 上**真正的销量冠军**
- Santevia CA BSR #259——加拿大市场绝对领导者
- Canopy UK BSR #184191——已进入 UK 但销量很薄
- Filterbaby $113 月销仍达 1K+，证明 $100+ 价位在此品类有市场
- 13 个 ASIN 中 12 个（92%）在 CA 有 listing——CA 市场参与度高但 Canopy 尚未建立统治

### 7.3 Canopy 渠道价格差异（重要）

| 渠道 | 价格 | vs Amazon |
|---|---|---|
| Amazon | $89 | baseline |
| **Target** | **$69.99** | -21% |
| Target 2-pack | $65.99/ea | -26% |
| Sephora | $89 | 持平 |
| Babylist | $89 | 持平 |

Target 比 Amazon 低 21%——Canopy 明显把实体零售作为主销渠道，Amazon 主要做品牌曝光和流量入口。

### 7.4 filtration_approach × 价格带

| 方法 | ASIN 数 | 月销合计 | 均价 |
|---|---|---|---|
| multi_stage_chemical_removal | 8 | 7K+ | $40 |
| vitamin_mineral_infusion | 3 | 1K+ | $23 |
| **baby_sensitive_skin_specialized** | **2** | **1K+** | **$101** |

baby_sensitive_skin 定位（Canopy + Filterbaby）均价 $101，是 multi_stage 通用路线的 2.5 倍——**场景特化定位的溢价空间已被市场验证**。

## 8. 复查节奏

每季度复查竞品价格 + refill cadence。特别监测：
- **Canopy 是否调整 $89 价位**（若降到 $69 = 直接挤 KES）
- **Tubo / Kinder 是否被 FTC 警告**（释放定位窗口）
- **新进入者**（FilterBaby 已进 Erewhon / Target，下一个会进入 bath 类目吗？）
- **Amazon 类目里白牌爆发**（KDF/CaSO₃ 同源 OEM 数量）

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-pricing-refill-flow-fit-table-v2]]
- [[bathtub-filter-channel-positioning-table-v2]]
- [[bathtub-filter-kes-concept-brief-v1]]
- [[bathtub-filter-competitor-review-corpus-2026-04]]
- [[bathtub-filter-community-language-compression-patterns]]
- [[bathtub-filter-utility-service-map-by-metro]]
- [[bathtub-filter-research-coverage-gaps]]
