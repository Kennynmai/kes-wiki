---
type: raw-research
status: collected
owner: strategy
created: 2026-11-08
updated: 2026-11-08
visibility: company
confidence: high
officiality: raw
domain: product-development
domains: [products, compliance, legal, quality-system, scm]
verification_status: cross-checked
related:
  - ../../../wiki/products/bathroom-caddy/kes-ceramic-shelf-existing-product-risk-2026-11-08.md
  - ../../../wiki/products/bathroom-caddy/decorative-ceramic-riser-product-liability-2026-11-08.md
  - ../../../wiki/products/bathroom-caddy/food-contact-materials-decision-2026-11-08.md
---

# 原始取证｜KES 现有浴室陶瓷层架产品风险评估（2026-11-08）

## 0. 取证方法与口径

**问题**：Kenny 要求「深入评估我们目前的浴室陶瓷层架产品是否有风险」。

**方法**：只读查询 OPS 生产库（`DATABASE_URL`，读取 `product` / `product_variant` / `dim_sku_platform_code` / `listing` / `dim_sp_listing_item_scd2` / `dim_asin_catalog_profile` / `fact_amazon_sku_monthly` / `product_test_record` / `dim_sku_certification` / `fact_product_spec_canonical_fact` / `product_selling_point`），未做任何写入；另核 HS 编码官方口径。

**重要局限（先说）**：
1. **未操作 Amazon Seller Central 或任何平台后台**（按项目规则须事前许可），listing 文案取自 OPS 已落库的 SP-API 快照，快照时点未逐条核。
2. **工艺完全未知**：全库没有任何字段记录「大理石纹是怎么上的」（水转印花纸／釉上彩／釉中彩／釉下彩／数码喷墨／烤花温度）。这是本次评估最大的缺口，也是第一优先要补的信息。
3. 销量毛利取自 `fact_amazon_sku_monthly` 的 PnL 口径，含分摊逻辑，不等于财务确认数。

标记：【库】OPS 生产库只读查询｜【官】官方/权威来源｜【推】本人推断，需实测确认。

---

## 1. 找到的产品：5 个 SKU，其中 4 个在售

判据：`product_variant.cn_export_hs_code LIKE '6911%'` + `fact_product_spec_canonical_fact.material = ceramic` + `product_selling_point` 含 ceramic。

| SKU | ASIN | 子类 | 毛重 | HS | 上架站点数 | 状态 |
|---|---|---|---|---|---|---|
| BSC901B-CH | B0DT9PFTS3 | corner_shelf | 1,610 g | 6911102900 | **23** | Active（含 amz_us/ca/uk/de/fr/es/it/nl/pl/se/be/ie/tr/br/mx + **hd_us + wf_us + wmt_us + wc_us/uk/ca/eu**） |
| BSC900B-CH | B0DT9QVSB7 | bathroom_shelf | 1,460 g | 6911102900 | 6 | Active（amz_us/ca/br/mx + wf_us） |
| BSC901B-PG | B0DT9NLSNP | corner_shelf | 1,600 g | 6911102900 | 9 | Active（amz_us/ca/uk/br/mx + hd_us + wf_us + wmt_us） |
| BSC900B-PG | B0DT9RN9CQ | bathroom_shelf | 1,480 g | 6911102900 | 6 | Active（amz_us/ca/br/mx + wf_us） |
| BSC223S4-2 | 无 ASIN | bathroom_shelf | 4,000 g | 6911102900 | 0 | 无 listing |

**全库只有这 5 个 SKU 用 6911 章 HS**，其余陶瓷类 SKU 未登记 HS。【库】

### 1.1 商品实质（来自 listing 原文）【库】

US 标题（B0DT9PFTS3）：
> "KES **Hancrafted Ceramic** Corner Bathroom Counter Organizer, 2-Tier Bathroom Countertop Organizer with **Marble Pattern**, Vanity Skincare Perfume and Makeup Storage, Polished Chrome, BSC901-CH"

五点关键句：
- "Made with high-quality ceramic that undergoes **high-temperature firing**"
- "Each skincare organizer is meticulously **handcrafted, undergoing careful polishing and multiple firings**... unique **hand-finished marble pattern**"
- "Built with **ceramic trays and polished aluminum handles**... resists rust, corrosion, and moisture"
- "**The raised edges act as a barrier**, preventing small items from falling" ← 有围边的托盘形态
- "Undergo **drop tests** to guarantee it arrives at your doorstep in perfect condition"
- product_description: "Premium ceramic trays, durable and **crack-resistant**"

`fact_product_spec_canonical_fact` 中的材质事实（8 条，全部指向 BSC901B-CH，confidence 0.8，review_status = **unreviewed**）：
- high_temperature_fired_ceramic_trays
- handcrafted_marble_pattern_ceramic
- ceramic_trays_and_polished_aluminum_handles
- smooth_premium_ceramic_surface
- 2_tier_storage_with_8_06_inch_height
- 90_triangular_fan_shaped_design

⇒ 商品是**双层陶瓷托盘 + 抛光铝手柄的浴室转角/台面收纳架，表面为"手工大理石纹"**。与 Kenny 口述的「浴室陶瓷层架」一致。

---

## 2. Listing 属性：平台给它的定性（关键，44 项原文）

来自 `dim_sp_listing_item_scd2.attrs_json`（US 站，66 个属性）【库】：

| 属性 | B0DT9PFTS3 | B0DT9QVSB7 | B0DT9NLSNP | B0DT9RN9CQ |
|---|---|---|---|---|
| `item_type_keyword` | bathroom-trays | bathroom-trays | bathroom-trays | bathroom-trays |
| `tray_type` | Bathroom Tray | Bathroom Tray | Bathroom Tray | Bathroom Tray |
| `shelf_type` | — | Corner Shelf | Vanity Shelf | Corner Shelf |
| `specific_uses_for_product` | **Decorative Items** | — | — | — |
| `recommended_uses_for_product` | Skincare Storage, Makeup Organization, Perfume Display, Countertop Convenience | Bathroom Countertop Storage | Skincare Organization, Perfume Display, Makeup Storage | Skincare Storage, Makeup Organization, Cosmetic Display |
| `pattern` | Marble | Marble | Marble | Marble |
| `material` | Ceramic + Aluminum | Ceramic + Aluminum | Ceramic + Aluminum | Ceramic + Aluminum |
| `frame.material` | Aluminum | — | — | — |
| `special_feature` | Tiered, Handle, **Heat Resistant**, Non Slip | Heat Resistant, Non Slip, Tiered, Handle | — | — |
| `care_instructions` | Wipe With Damp Cloth | Wipe With Damp Cloth | Wipe With Damp Cloth | Wipe With Damp Cloth |
| `maximum_weight_recommendation` | （未填） | 13.00 | （未填） | 13.00 |
| `country_of_origin` | CN | CN | CN | CN |
| `cpsia_cautionary_statement` | no_warning_applicable | no_warning_applicable | no_warning_applicable | no_warning_applicable |
| `required_product_compliance_certificate` | **Not Applicable** | Not Applicable | Not Applicable | Not Applicable |

**关键否定发现**：66 个属性中**不存在** `safety_warning`、`prop_65`、`supplier_declared_chemical_compliance` 这三个字段 —— 即**没有任何 Prop 65 警示申报，也没有化学品合规申报**。全库所有表也**没有任何 prop65 / california 字段**（`information_schema.columns` 检索结果为 0）。【库】

---

## 3. 合规文件：两条都空

### 3.1 测试记录 = 0

`product_test_record`（shelf 三子类 252 个 SKU）情况【库】：

| test_category | 条数 |
|---|---|
| durability | 108 |
| performance | 54 |
| material | 24 |
| (null) | 19 |

按 `test_name / test_standard ~* 'ceramic|lead|釉|陶瓷|镉|食品|food'` 检索：**0 条**。

⇒ 陶瓷层架**没有任何铅镉溶出、材料成分、食品接触相关测试记录**。全库 `material` 类测试 24 条也未覆盖陶瓷。

### 3.2 认证记录 = 0

`dim_sku_certification` 全表 cert_type 分布【库】：

| cert_type | 条数 |
|---|---|
| domestic_water_efficiency_filing | 64 |
| cec | 26 |
| doe | 12 |

⇒ 认证体系**只覆盖水效/能效**（水龙头、花洒类），**完全没有材料安全、食品接触、Prop 65、CPSIA 以外的化学合规类别**。BSC 系列 4 个 SKU 在 `dim_sku_certification` 中**一条记录都没有**。

---

## 4. HS 归类：归错章了（本次最具体的可修问题）

5 个 SKU 全部登记 `cn_export_hs_code = 6911102900`。【库】

### 4.1 6911102900 的真实含义【官】

来源：hsbianma.com、hgsj.com、i5a6、e-to-china（多个独立 HS 查询站口径一致）

| 项 | 内容 |
|---|---|
| 商品名称 | **其他瓷厨房器具** |
| 归类路径 | 第 13 类 → 69 章 → 6911（瓷餐具、厨房器具及其他家用或盥洗用瓷器）→ 691110（瓷餐具及厨房器具）→ 69111029（瓷制其他厨房器具） |
| **CIQ 代码** | `6911102900101` **其他瓷厨房器具（食品接触陶瓷产品）**；`6911102900102` 其他瓷厨房器具（食品用陶瓷包装） |
| **监管条件** | **A** —— 入境货物通关单 |
| **检验检疫类别** | **R** —— 进口食品卫生监督检验 |
| 申报要素第 3 项 | 种类（**餐具、厨房器具等**） |

### 4.2 浴室置物架的正确归类【官】

来源：hsbianma.com / api.hsbianma.com / i5a6 / 7788ship / transcustoms

| 项 | 内容 |
|---|---|
| 编码 | **6911900000** |
| 商品名称 | **其他家用或盥洗用瓷器**（Other household articles and toilet articles, of porcelain or china） |
| CIQ 代码 | `6911900000999` 其他家用或盥洗用瓷器 |
| **监管条件** | **无** |
| **检验检疫类别** | **无** |
| 申报要素示例 | 「**卫浴套件；陶瓷制；卫生间用；无品牌**」← 与本产品完全对应 |

### 4.3 推论（需报关行确认，不要直接改）

【推】把浴室置物架报成「其他瓷厨房器具」，在报关层面**主动把产品定性为"食品接触陶瓷产品"并触发 R 类进口食品卫生监督检验**。这与 listing 端 `bathroom-trays` / `specific_uses = Decorative Items` / `required_product_compliance_certificate = Not Applicable` 三处表述**互相矛盾**。一旦被查验或平台/进口商追溯，需要解释「为什么一个按食品接触陶瓷报关的产品，没有任何铅镉溶出报告」。

**必须由报关行/合规确认后再改**，不得凭本文直接改单。改归类属于报关行为，须走正式变更流程并留痕。

---

## 5. 规模与毛利：风险敞口 vs 承受能力

`fact_amazon_sku_monthly`，US 站，2025-12 ~ 2026-11 共 12 个月【库】：

| ASIN | 有数据月数 | 件数 | 收入 USD | 毛利 USD | Sessions |
|---|---|---|---|---|---|
| B0DT9PFTS3（BSC901B-CH） | 12 | 813 | 32,166.95 | 3,057.39 | 13,004 |
| B0DT9QVSB7（BSC900B-CH） | 12 | 785 | 31,347.18 | 800.80 | 15,712 |
| B0DT9NLSNP（BSC901B-PG） | 12 | 316 | 12,484.87 | 1,300.11 | 4,460 |
| B0DT9RN9CQ（BSC900B-PG） | 12 | 218 | 8,224.26 | 472.71 | 4,703 |
| **合计（US）** | | **2,132** | **84,223.26** | **5,631.01** | **37,879** |

全站点合计（同 12 个月）：amz_us 2,132 件 / $84,223；amz_ca 263 / $12,670；amz_uk 16 / $686；amz_de 4 / $161；amz_mx 3 / $2,365。**约 2,420 件 / $10 万收入**。欧洲多站点多为 0 或个位数，部分站毛利为负（amz_uk 2026-10 毛利 −75.58、amz_de −37.29、amz_fr −20.12）。【库】

**毛利率 ≈ 6.7%**（5,631 / 84,223）。

对照：California Prop 65 同款陶瓷托盘和解案（Johnson v. Casa Collective，2024-03437S4964，生效 2025-03-05）付款为 **$1,000 民事罚款 + $11,000 律师费 = $12,000**；Sino Gifts 案 $800 + $11,200 = $12,000。

⇒ 【推】**一次 Prop 65 和解 ≈ 该产品线 US 全年毛利的 2.1 倍**。若叠加 FDA 扣留/召回（CPSC 估算平均直接成本 $540,000），量级完全不成比例。

---

## 6. 文案层的具体问题（逐条可改）

| # | 问题 | 位置 | 性质 |
|---|---|---|---|
| 1 | "Polished **brass** handles" vs `material: Aluminum` vs 五点 "polished **aluminum** handles" | B0DT9RN9CQ `product_description` | 三处自相矛盾，可被认定误导性描述（FTC net impression / 州 UDAP） |
| 2 | "**crack-resistant**"（抗裂） | 4 个 ASIN `product_description` | 绝对化承诺；陶瓷是脆性材料，无测试报告支撑 |
| 3 | "**Heat Resistant**" 作为 `special_feature` | B0DT9PFTS3 / B0DT9QVSB7 | 暗示可承热物，加强「可作餐盘/托盘」联想 |
| 4 | "**The raised edges act as a barrier**" | 五点 #7 | 自己描述了「有围边的托盘」形态，是与 21 CFR 109.16 "appears suitable for food use" 相关的形态特征 |
| 5 | `maximum_weight_recommendation: 13.00`（单位未标） | 2 个 SKU | 单位缺失（lb? kg?），承重无测试支撑 |
| 6 | "**Hancrafted**"（拼写错误，应为 Handcrafted） | 4 个标题 | 低级但影响专业形象 |
| 7 | `number_of_shelves` 在 BSC901B 为 1、BSC900B 为 2，但都叫 2-Tier | 属性表 | 属性不一致 |

**做得好、不要动的地方**：`pattern: Marble`（不是 material: Marble）、`item_type_keyword: bathroom-trays`（不是 food/serving tray）、`specific_uses: Decorative Items`、`recommended_uses` 全是化妆品语境、文案无 food/serving/dishwasher/microwave 字样、`care_instructions: Wipe With Damp Cloth`（未承诺洗碗机）。

---

## 7. 姊妹产品线：KES 已有真大理石底座

`product_selling_point` 检索发现另一组产品用的是**天然大理石**（非陶瓷）【库】：

| SKU | 卖点代码 |
|---|---|
| BPH284S1 / -2 / -BZ | 100_solid_natural_marble_base、handcrafted_natural_marble_base、weighted_100_solid_marble_base、natural_marble_patterns |
| BPH285S1-2 / -BZ | heavy_weighted_natural_marble_base、unique_natural_marble_patterns、unique_marble_patterns |
| BPS202S39-2 | 1_inch_thick_natural_marble_base、heavy_1_87_lbs_marble_base |

⇒ 说明 KES 同时具备「陶瓷」与「天然大理石」两条材料线，前几轮讨论的"陶瓷替代大理石"在供应链上并非从零开始。这些产品同样是非食品接触（浴室五金底座），但大理石多孔渗色与酸蚀问题在浴室场景（洗手液、洁面乳、酸性护肤品滴落）**可能比食品场景更常发生**，且此前未做任何密封/耐污测试记录。【推】

---

## 8. 「未查到」清单

1. **大理石纹的工艺**：水转印花纸/釉上彩、釉中彩、釉下彩、数码喷墨，以及烤花温度、是否过 1200℃ —— 全库零记录。
2. 釉料与彩料是否含铅、是否用无铅熔剂 —— 零记录。
3. 任何铅镉溶出检测报告（成品 6 件浸出，ASTM C738 / AOAC 973.32）—— 零记录。
4. 任何 Prop 65 评估或警示 —— 零记录，平台也无对应字段。
5. 供应商名称、产地工厂、是否通过 BSCI/验厂 —— 本报告未查（表里无对应字段）。
6. `maximum_weight_recommendation: 13.00` 的单位与测试依据。
7. 4 个 ASIN 的图片/视频素材内容（主图是否出现食物或餐桌场景）—— 未抓图，仅凭文案判断。
8. `BSC223S4-2` 为何无 listing（未上市／已停／套装件）—— 未查。
9. Amazon US 后台「增强安全类目」是否覆盖本产品、是否已触发保险要求 —— 需登录后台，未查。
10. 真实溶出数据下的实际超标概率 —— 需实测。

---

## 9. 来源

【库】OPS 生产库只读查询（`DATABASE_URL`），表：`product`、`product_variant`、`dim_sku_platform_code`、`listing`、`dim_sp_listing_item_scd2`、`dim_asin_catalog_profile`、`fact_amazon_sku_monthly`、`product_test_record`、`dim_sku_certification`、`fact_product_spec_canonical_fact`、`product_selling_point`、`sku_compliance_requirement_override`、`information_schema.columns`。查询时间 2026-11-08 22:59–23:20。

【官】HS 编码
- 6911102900 其他瓷厨房器具 <https://www.hsbianma.com/Code/6911102900.html>
- 6911102900 其他瓷厨房器具 <https://www.hgsj.com/hs-code/6911102900>
- 6911102900 中国 HS Code <https://www.ihscode.com/hscode/CN/6911102900.html>
- 6911900000 其他家用或盥洗用瓷器 <https://hsbianma.com/Code/6911900000.html>
- 6911900000 CIQ/申报要素 <https://www.i5a6.com/hscode/detail/6911900000>
- 6911900000 申报示例「卫浴套件；陶瓷制；卫生间用」 <https://www.7788ship.com/hscode/6911900000.html>
- 6911900000 检验检疫要求 <https://www.transcustoms.cn/China_HS_code/China_Customs_Declaration.asp?HS_Code=6911900000&word=27>

【官】法规（详见 [装饰陶瓷产品责任证据](./2026-11-08-decorative-ceramic-product-liability-evidence.md)）
- 21 CFR §109.16 <https://www.ecfr.gov/current/title-21/chapter-I/subchapter-B/part-109/section-109.16>
- Cal. H&S Code §25249.13
- Johnson v. Casa Collective 和解 2024-03437S4964

---

*本文件为内部风险取证，不构成法律意见，也不构成报关归类意见。*
