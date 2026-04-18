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
domains: [bathtub-filter, channel, retail, gtm, compliance, admission, gate]
source_count: 11
review_cycle: quarterly
verification_status: working
related:
  - ./bathtub-filter-channel-positioning-table-v2.md
  - ./bathtub-filter-marketplace-claim-policing-layer.md
  - ./bathtub-filter-certification-and-testing-pathways.md
  - ./bathtub-filter-competitor-pricing-and-kes-v1-price-recommendation.md
  - ./bathtub-filter-research-coverage-gaps.md
---

# Bathtub Filter — 渠道准入要求速查（公开文档汇总）

## 为什么有这页

Gap doc B 层（channel/retailer landscape）此前是 🟡 框架——只有 6 个 channel identity 分类，没有"哪个渠道实际让 KES 进、需要交什么文档、什么时间点"的可执行清单。

这页用 2026-04 公开文档抓取的**5 个候选渠道的真实准入要求**，给 KES GTM 团队一份预审清单：哪些渠道**今天就能投递**，哪些**必须先做 cert / legal / 资本结构调整**才能投递。

> ⚠️ 本页只覆盖**公开**部分。每个渠道还有 buyer-side 的非公开 margin / minimum order / promo cadence 要求，那些只能通过实际 buyer outreach 拿到，**不在本页范围**。

## 1. 候选渠道 × 准入要求矩阵

| 渠道 | 准入难度 | 关键 gate | KES 当前能否投递？ |
|---|---|---|---|
| Amazon (3P FBA) | 🟢 低 | 类目 ungated，但 brand-level approval 可能触发 | ✅ V1 出货即可投 |
| Walmart Marketplace (3P) | 🟡 中 | WERCS chemical review（介质涉及氯/硫酸钙）| ⚠️ 出 BOM + supplier file 后可投 |
| Walmart 1P (Supplier One) | 🔴 高 | EDI + audit + cert + 大批量 commitment | ❌ KES 太早 |
| Home Depot | 🔴 高 | **51% US ownership** + $2M liability + UL/cert | ❌ 若 KES 非 51% 美资必须先解决 |
| Target (physical + Target Clean) | 🟡 中 | Target Clean 配方门槛 + buyer 关系 | ⚠️ 申请 Target Clean icon 可，进货架需 buyer |
| Babylist (registry/co-shop) | 🟢 低 | 无强公开门槛，brand 可申请上 registry | ✅ V1 launch 即可申请 |
| DTC (Shopify) | 🟢 自营 | 无渠道 gate；自担 Stripe / Shop Pay 合规 | ✅ 任意时点 |
| 高端 spa retail (Erewhon/Heaven on Earth Aspen 类) | 🟡 中 | curated buyer 关系 | ⚠️ 需走 wholesale outreach |

## 2. 各渠道详细准入要求

### 2.1 Amazon（3P FBA Seller Central）

**类目分配（基于现有竞品 ASIN）：**

| 竞品 | Amazon 类目 |
|---|---|
| Canopy Bath Tub Filter | Health & Household → Health Care |
| Tubo 2.0 (B0FZCR8VGB) | **Tools & Home Improvement → Plumbing → Faucet Water Filters** |
| Sprite BB-WH | Tools & Home Improvement → Plumbing |
| Crystal Quest (B008A4AG2U) | Tools & Home Improvement → Plumbing → Faucet Water Filters |
| Santevia | Tools & Home Improvement / Health & Household 跨 |
| FilterBaby Skincare Filter | Beauty & Personal Care + Health & Household 跨 |

**KES 含义：** "Faucet Water Filters" 类目（ASIN B016M167GG, B0DTQ8H23D 等驻扎）是 KES 默认类目。Amazon 不要求该类目预 approval。

**仍可能触发 gating 的情况：**
- 若 KES 在 listing 中使用 "skincare" / "baby" / "eczema" / "skin treatment" 等词 → 跨入 Health & Household 子类目 → 可能触发 brand approval
- 若 KES 声称"99.X% removes [list]" 无 supporting documentation → A+ content review 卡审

**准入文档清单：**
- [x] Brand Registry（必做，否则无法享受 A+ content + Sponsored Brands）
  - 需求：USPTO/CIPO/EUIPO 已 issued trademark
  - KES 必须**先**注册 trademark（约 8–12 月周期）
- [x] FBA setup（包装、SKU、UPC/GTIN）
- [x] Compliance documents（safety datasheet）
- [x] Brand authority documents（若被 brand-gating 触发）

**最快投递时间：** trademark issued 后约 **2–4 周**。Trademark 未 issued 时仍可上架，但无 Brand Registry 保护。

---

### 2.2 Walmart Marketplace（3P）

**关键 gate — WERCS Chemical Assessment：**

> 任何"包含 chemical, aerosol, or pesticide"或含 lithium/lead 电池的产品，必须完成 WERCS Chemical Assessment Review。

**KES 触发条件：** KDF + CaSO₃ + 可能 silver-ion 等介质组合 → **必触发 WERCS**。

**WERCS 流程（推断）：**
- 提交 formulation 信息（介质组分 + 浓度 + 供应商）
- 评估周期：4–8 周（行业 typical）
- 通过后获得 WERCS ID，可挂在 Walmart Item Setup

**准入文档清单：**
- [x] Onlyzone supplier file 完整版（介质 SDS + 供应链 declaration）
- [x] Supplier One 账号（取代 2024 前的 Item 360）
- [x] EDI 不强制（3P）但 1P 必须
- [x] 美国/州/联邦法规符合声明

**最快投递时间：** WERCS 通过后约 **4–10 周**。**KES 必须把 WERCS 作为 V1 launch checklist 项**。

---

### 2.3 Walmart 1P（Supplier One，仅供大体量品牌参考）

不推荐 KES V1 进入，除非有：
- EDI 自动化能力（成本约 $5k–$20k 起步）
- 1M+ 单位/年 commitment 能力
- 完整 supply chain audit 能力
- 自有 logistics 或 3PL 能 hit Walmart OTIF（On Time In Full）99%

**KES 时机：** V2 / B-line 跑通 + DTC + 3P 站稳后再考虑。

---

### 2.4 Home Depot（Supplier Hub）

**关键 gate — 51% US ownership：**

> Your company must be at least 51% owned by a U.S. Citizen(s) or a person(s) with U.S. Permanent Resident Alien Status.

**KES 含义：** **必须先确认资本结构**。如 KES 主体是非美资公司：
- 选项 A：成立美国子公司，确保 51%+ 由 US person 持有
- 选项 B：通过 US-owned distributor / agent
- 选项 C：放弃 Home Depot，专注 DTC + Amazon + Babylist

**其他 gate：**
- $2M liability insurance, naming The Home Depot U.S.A., Inc. additional insured
- W-9 (US entity) 或 W-8BEN (foreign)
- UL / SDS / 必要 cert（**水过滤产品大概率要求 NSF 42/61 cert**——参考 [[bathtub-filter-certification-and-testing-pathways]]）
- Vendor safety standards 遵守

**准入流程：** 填 Prospective Non-Merch Supplier Template → email potential_suppliers@homedepot.com → 等待 buyer 回应（**90 天内无回应可重交**——意味着默认拒绝是常态）。

**KES 时机：** 不在 V1 范围。需先有 NSF cert + 美资结构 + 至少 12 个月 DTC + Amazon track record。

---

### 2.5 Target（physical store + Target Clean icon）

**Target Clean criteria（公开）：**

> 产品必须 **formulated without** 以下 chemical groups（< 100 ppm of finished product）：
> - phthalates
> - propyl- & butyl-parabens
> - formaldehyde donors
> - musks
> - nonylphenol ethoxylates
> - ethanolamines
> - glycol ethers
> - siloxanes
> - PFAS

**KES 含义：** KES 是**hardware 产品而非 formulated personal care**——Target Clean icon 主要给护肤/化妆品/家清。但**KES 介质（KDF + CaSO₃ + housing 材料）**也需符合：
- 无 PFAS（housing 塑料 / 密封件）
- 无 phthalates（housing 塑料增塑剂）
- 无 nonylphenol ethoxylates（清洁/脱模剂残留）

**实际进 Target 货架** 是另一回事——需通过 Target buyer / EVP 关系。Target Clean icon 是申请，不是上架保证。

**KES 时机：** 
- 配方/材料 audit 可在 V1 出货前做
- Target Clean icon 申请可与 Amazon / DTC launch 并行
- 物理货架进入 = 12–24 月窗口（不在 V1 范围）

---

### 2.6 Babylist（registry + Babylist Shop）

**门槛（公开）：** 任何 brand 可被加入 registry（用户自加）。Babylist Shop（直销）和 Best of Babylist editorial 是 curated。

**Canopy 已进 Babylist Shop**（货号 74871/2519863）—— KES 直接对位入选有先例。

**准入流程（推断）：**
- 申请 Babylist brand partnership：`brands@babylist.com`（公开）
- 提供产品资料 + brand story + samples
- Babylist editorial team review

**KES 时机：** V1 launch 即可申请。**Babylist 是 KES baby/parent 心智的最高 leverage 入口**——比 Target 物理货架更快、比 Amazon Search 更高质量流量。

## 3. KES V1 推荐 GTM 渠道节奏

```
Phase 1 — Soft launch (V1 launch + 0–3 月)
├── DTC (Shopify)                 ✅ 立即
├── Amazon 3P FBA                 ✅ trademark issued 后 2–4 周
├── Babylist application          ✅ 立即申请
└── Send-test for SNS reviewers   ✅ 立即（送 Water Filter Guru / mindbodygreen / Interior Medicine）

Phase 2 — Channel expansion (3–9 月)
├── Walmart Marketplace 3P        ⚠️ WERCS 通过后
├── Babylist Shop direct          ⚠️ Babylist 编辑流程后
├── Target Clean icon application ⚠️ 配方/材料 audit 后
└── 高端 spa retail (Erewhon 类)   ⚠️ buyer outreach

Phase 3 — Scale (9–24 月)
├── Home Depot Supplier Hub       ⚠️ NSF cert + 美资结构后
├── Target physical placement     ⚠️ buyer 关系 + 12mo DTC traction
└── Walmart 1P Supplier One       ⚠️ V2/B-line 跑通后
```

## 4. KES 必须立即开始的非 gate 行动

为避免在 12 个月后才发现某些 gate 是结构性 blocker，**KES 现在就该启动**：

1. **Trademark 注册**（USPTO + WIPO Madrid Protocol）—— 8–12 月周期，越早越好
2. **WERCS 注册账号 + 介质 SDS 收集**（与 Onlyzone 对接）
3. **资本结构审视**——如计划进 Home Depot/Lowes/Costco，**今天**就需评估 51% US ownership 路径
4. **NSF 42/61 cert RFQ 启动**——见 [[bathtub-filter-certification-and-testing-pathways]]，是 Home Depot / 多 retail 渠道的 hard gate
5. **$2M liability insurance quote**——retail 渠道通用门槛，提前知道成本
6. **包装 / 材料 PFAS / phthalate / paraben 审计**——Target Clean + EU REACH + CA Prop 65 同时满足

## 5. 还卡在哪里（必须人工/外部完成）

- [ ] 实际 buyer outreach（Target / Home Depot / Babylist / Erewhon / Heaven on Earth Aspen 等）
- [ ] Margin / wholesale discount 谈判（不公开）
- [ ] OTIF 物流能力评估（Walmart 1P 必备）
- [ ] EDI 系统选型（如计划进 Walmart 1P / Target）
- [ ] 资本结构调整（如需 Home Depot 但当前不满 51% 美资）
- [ ] Trademark 国际注册顺序（先美国还是同步多国）

## 6. 复查节奏

每季度复查渠道 admission 文档（retailer 偶尔修改）。特别监测：
- **Walmart Supplier One** 平台变化（2024 替换 Item 360，可能继续迭代）
- **Amazon brand gating 标准** 变化
- **Target Clean** 化学品清单扩充（PFAS 持续被监管收紧）
- **WERCS** 评估流程更新

---

## 7. 渠道 buyer 行为推断（基于 2026-04 竞品定价校准）

> 本节不是 buyer outreach 记录，而是基于 Canopy 多渠道实测价格反推的**结构化推断**。  
> 真实 margin / MOQ 谈判数字只能通过实际 buyer 接触获得——见 §5。

### 7.1 Canopy 渠道定价作为行业校准基准

来源：[[bathtub-filter-competitor-pricing-and-kes-v1-price-recommendation]] §7.3

| 渠道 | Canopy 价格 | vs Canopy DTC ($89) | 推断 Canopy 实得 |
|---|---|---|---|
| DTC | $89 | baseline | ~$89 - 处理/物流 |
| Amazon (3P) | $89 | 持平 | ~$75（FBA fee 扣后）|
| Target | **$69.99** | **-21%** | Target 以 50–55% 折扣批发 → Canopy 实得约 **$35–38/unit** |
| Sephora | $89 | 持平 | Sephora 扣约 40% commission → Canopy 实得约 **$53** |
| Babylist | $89 | 持平 | Babylist 扣约 30–40% co-op → Canopy 实得约 **$53–62** |

**含义：KES V1 MSRP $59–$79 下的渠道收入估算**

| 渠道 | KES MSRP $59 → 估算实得 | KES MSRP $79 → 估算实得 |
|---|---|---|
| Target (50% margin) | ~$30 | ~$40 |
| Sephora / 高端 spa (~40%) | ~$35 | ~$47 |
| Babylist (~35%) | ~$38 | ~$51 |
| Amazon FBA (~15% fee) | ~$50 | ~$67 |
| DTC | ~$57（扣处理）| ~$76（扣处理）|

**BOM 含义：** 若 KES 进 Target，unit BOM 必须 < $12–$15 才能在 $30 wholesale 上维持 20%+ GM。这是供应链设计的上限约束，不是优化目标。

### 7.2 各渠道 buyer 期望推断（基于品类知识 + 竞品格局）

| 渠道 | Buyer 核心评估维度 | KES 匹配难度 | 关键准备 |
|---|---|---|---|
| **Amazon** | 关键词竞争力、review 积累速度、BSR 前景 | 🟢 可行 | Brand Registry（需 trademark）；listing 质量；review 生态启动 |
| **Babylist** | Brand story fit（家长安全 + 设计）、Category whitespace | 🟢 高机会 | Canopy 已进但有 performance gap；KES 有"实测有效"的差异化空间 |
| **Target** | 渠道 exclusivity 偏好、SKU 精简（1–2 SKU）、稳定 MOQ 承诺 | 🟡 需准备 | Category reset 窗口有限；buyer 偏爱有 Amazon/DTC traction 的品牌 |
| **Sephora** | Beauty 叙事、clean 成分、设计溢价 | 🟡 中等 | FilterBaby 已在 Sephora 对位布局；KES 需更强的 skincare narrative |
| **Home Depot** | NSF cert + 51% US ownership + OTIF 供应链 | 🔴 需结构调整 | 核心 gate 见 §2.4；V1 不推荐尝试 |

### 7.3 MOQ 估算（行业典型区间）

| 渠道 | 典型首单 MOQ | 说明 |
|---|---|---|
| Amazon FBA | 无硬性 MOQ（受 IPI score 限仓） | 建议首批 200–500 units 测算 sell-through |
| Babylist curated | 50–200 units | 编辑 curation 为主，不是大批采购模式 |
| Target 新品类 | 500–2,000 units（per SKU） | 若 2 个配色 × 1,000 = 2,000 units |
| Home Depot | 1,000–5,000+（按门店数）| 不适合 V1 阶段 |

**KES V1 推荐首批生产量：500–1,000 units**，先在 DTC + Amazon 跑 3–6 个月，用 traction 数据开 Babylist / Target 谈判。

### 7.4 渠道 category reset 时间窗口（推断）

| 渠道 | 典型 category review 节奏 | KES 行动截止 |
|---|---|---|
| Target | 每年 2 次（春季 + 秋季 reset）| **2026 Q2** → 秋季 reset buyer submission |
| Sephora | 每年 1–2 次（视品类）| **2026 Q3** → 春季 planogram 准备 |
| Home Depot | 1 次/年（秋季准备，次年春上架）| 2027 春（需先完成 NSF cert） |
| Babylist | 滚动（小品牌随时申请）| V1 launch 后即申请 |
| Amazon | 滚动 | 随时 |

**关键时间约束：** Target 2026 秋季 reset 的 buyer submission 需在 **2026-Q2（4–6 月）** 完成。这与 trademark + WERCS 时间线高度耦合——若 V1 无法在 Q2 就绪，下一窗口是 2027 秋（晚 12 个月）。

### 7.5 KES 仍无法靠桌面研究获得的数据

以下数据只能通过实际 buyer outreach 获得，不在本页范围：
- 各渠道真实 margin / discount 要求（非推断）
- 各渠道 promo cadence 要求（TPR / endcap / co-op marketing 频率）
- Babylist / Sephora 实际 editorial review 标准（非公开）
- Target Vendor Manager 当前是否开放浴缸过滤器类目新供应商

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-channel-positioning-table-v2]]
- [[bathtub-filter-marketplace-claim-policing-layer]]
- [[bathtub-filter-certification-and-testing-pathways]]
- [[bathtub-filter-cross-jurisdiction-standards-map]]
- [[bathtub-filter-us-state-federal-compliance-sidelines]]
- [[bathtub-filter-competitor-pricing-and-kes-v1-price-recommendation]]
- [[bathtub-filter-research-coverage-gaps]]
