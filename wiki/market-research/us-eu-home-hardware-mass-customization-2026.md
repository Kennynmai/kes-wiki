---
type: market
status: active
owner: product-strategy
created: 2026-09-06
updated: 2026-09-06
visibility: company
confidence: medium
officiality: draft
domain: market
domains: [market, product-strategy, bathroom-hardware, metal-storage, north-america, europe, manufacturing, ai-commerce]
source_count: 5
review_cycle: quarterly
verification_status: spot-checked
related:
  - unlacquered-brass-finish-gonogo-2026
  - north-america-growth-marketplace-opportunity-research
  - kes-ai-era-amazon-content-strategy-judgment
  - amazon-rufus-cosmo-e-geo-kes-response
---

# 美欧家装五金 Mass Customization 机会评估 — AI 接单 / 参数化设计 / 在地加工 / 快速交付

**调研日期**：2026-09-06
**调研范围**：US + EU（DE / UK / FR / NL / DK / IT）；亚马逊 US / DE / UK 站关键词实测 + 4 路桌面调研（美国供给、欧洲供给、技术与运营底座、市场规模与需求信号）
**结论**：**整体模式不做；窄切片有条件试点。** "AI 接单 → 在地加工成品 → 天级交付"在装饰五金上不成立，卡在饰面工艺而非 AI。KES 可切入的是两层更窄的东西：① 零固定成本的"尺寸阶梯 + AI 选配助手"（现有平台内做）；② 哑光黑粉末涂层的平板/折弯钣金品类走美国按需激光网络试点（通风口盖、搁架支架）。毛巾杆 / 扶手的切长定制只在 ① 验证出信号后，以 Emtek 式"中国预饰面 + 美国组装"进入。**EU 不作为首发市场。**

---

## 执行摘要

发起问题：美欧家装五金定制市场是否有 mass customization 机会，能否依赖 AI 建立接单 / 设计 / 在地加工 / 快速交付模式，KES 是否有切入机会，哪些品类合适。

**六条核心发现**：

| # | 发现 | 证据强度 |
|---|---|---|
| 1 | **亚马逊上不存在"定制"搜索意图。** US / DE / UK 三站所有 custom / nach Maß / made to measure 修饰的五金词 ABA 全部无排名；需求集中在通用大词（curtain rods 17.2 万/周、gardinenstange 2.5 万/周、radiator cover 2.5 万/周），亚马逊上"定制"的替代品是**伸缩杆 / 通用尺寸**。 | 高（一手 ABA 数据） |
| 2 | **站外定制需求真实但碎片化、小作坊化。** 美欧两地"尺寸按单"供给全是单点小厂（Highland Forge、Semi Exact、PHOS、Stahldeko、Signostar…），价格 $90–$500，交期 2–6 周，多数 call for quote。没有一个消费品牌使用分布式在地制造网络。 | 高（供给侧直接观察） |
| 3 | **唯一做到"定制 + 天级"的是 Emtek（Assa Abloy）：海外预饰面模块件 + 洛杉矶按单组装 2–3 天。** 不切割、不本地饰面。Rustica 全定制 3–5 天是另一例，自有工厂。 | 高 |
| 4 | **在地加工底座已成熟，但只到"裸件 + 粉末涂层"。** SendCutSend 2025 营收破 $1 亿，304 不锈钢 2–4 天 qty 1 无 MOQ；EU 247TailorSteel 48 h、Laserhub 有 API。**拉丝镍 / 拉丝金 / 黑 PVD 在 qty 1 天级不存在**——这正是 KES 核心饰面。 | 高 |
| 5 | **AI 在这条链里是最便宜的一环，不是差异化。** 无任何五金品牌用 LLM 接单；毛巾杆 / 支架不需要 text-to-CAD，只需 3–6 参数模板。AI 在家装商务的真实落点是零售商侧选购助手（Lowe's Mylow 2,500 万次提问、转化 3 倍；Home Depot Magic Apron 每月数百万次）。 | 高 |
| 6 | **Made-to-order 的死法有两种且 KES 两种都暴露：** 固定成本节点扛不起 42% 毛利（Shapeways）；海外长链 MTO 的交期 + 营运资金陷阱（Made.com、Interior Define）。 | 高 |

**对 KES 的判断**：KES 的三项核心资产（304 不锈钢 + 拉丝饰面平台、亚马逊评论飞轮、$25–90 ASP）与"在地定制成品"模式**逐项相斥**：拉丝饰面是在地不可做的工艺；评论飞轮在 custom SKU 上失效（Amazon 定制品不可退，且 listing 结构不同）；ASP 撑不起美国组装节点。所以不是"做不做"，而是**把"定制"重新定义为 KES 能做的形态**——见 §6。

---

## 1. 需求：定制需求以什么形态存在

### 1.1 亚马逊（KES 主渠道）— 定制意图为零

一手数据（2026-08-23 ~ 08-29 周，`2026-09-06-amazon-keyword-customization-signal.md`）：

| 站点 | 通用大词（周搜索量） | 具体尺寸词 | custom / nach Maß / made to measure 词 |
|---|---|---|---|
| US | curtain rods 172,002 / towel bar 6,982 / cabinet pulls 5,394 / grab bars for bathroom 4,210 | cabinet pulls 3 inch 651、5 inch 429；其余 < 110 或无排名 | **全部无排名**（仅 custom house numbers 75/周） |
| DE | gardinenstange 25,434 / handtuchhalter 18,348 / möbelgriffe 1,983 | 全部无排名 | **全部无排名** |
| UK | radiator cover 25,011 / curtain pole 6,646 / towel rail 5,444 | 全部无排名 | **全部无排名** |

三个读法：
- 亚马逊用户遇到尺寸问题时，搜通用词然后**在变体里挑**，或买伸缩 / 可调节产品。这是"尺寸不确定"品类（窗帘杆、散热器罩）反而成为最大头部词的原因。
- UK radiator cover 每周 2.5 万次值得单独记：这是一个传统上 made-to-measure 的品类（本地木工），在亚马逊上被标准尺寸 MDF 罩吞掉。**定制品类被标准化是可以发生的**，也反向说明定制需求确实转移到了站外。
- grab bars for bathroom CPC $3.63、转化率 0.229 是这批最高，需求明确且购买决心强，但同样没有尺寸词。

> 方法论提醒（沿用 [[unlacquered-brass-finish-gonogo-2026]] §1）：ABA 只反映站内表达，不能推断站外定制需求规模。本节结论是"亚马逊不是定制的入口"，不是"定制需求不存在"。

### 1.2 站外 — 需求真实，但只有定性证据

| 信号 | 内容 | 来源 |
|---|---|---|
| Etsy 10-K FY2025 | "Custom or made-to-order merchandise comprised about 30% of total GMS"；31% 访问者在找 custom / personalized。**但** Home & Living 切片未披露，且该类增长来自 vintage decor / rugs / lighting，非五金 | SEC 原文，高信任 |
| 孔距非标 | 老北美柜 3" CTC vs 96 mm 公制；3.125" 孔距"Ain't no such thing"，解法是背板遮孔 / 填孔重钻 | WoodWeb 论坛、零售内容站 |
| 通风口非标 | Reggio / Ventiques 把"3x10、6x14、8x12 等尺寸难买"写成营销语；多家专门商以"hard to find sizes"为卖点 | 商家页面（痛点已被商业化验证） |
| Bay window 窗帘杆（UK） | Mumsnet ≥ 9 个求助帖；John Lewis 定制 ~£300–600、专业金属轨 ~£700、Screwfix 通用杆 £74 —— 价格断层明显 | Mumsnet 原帖 |
| 毛巾杆长度 | 主流只有 18"/24" 两档；市场解法是 16–27.6" 伸缩杆；"a wrong-size order means patching drywall" | Knobs.co 指南 |
| 房龄 | US 自住房中位房龄 42 年，~47% 建于 1980 前，2020–24 新建仅占 4%；England 自住 pre-1919 占 20% | NAHB / ACS 2024、EHS 2023-24 |
| 老龄化 | Houzz 2025 US Bathroom：41% 为现有老龄成员、49% 为提前规划改造浴室 | Houzz，n=1,737 |

**缺失的证据**：没有任何来源量化"非标尺寸的普及率"，也没有任何"定长卫浴五金付费意愿"调查。Deloitte "1/5 愿多付 20%"是 2015 年 UK 泛品类数字且原文不可达。**"老房 → 非标 → 定制需求"是从房龄推出的推论，不是测量结果。**

---

## 2. 供给：谁在做定制五金、怎么做

### 2.1 三种模式，只有一种做到天级

| 模式 | 代表 | 定制维度 | 交期 | 产地结构 |
|---|---|---|---|---|
| **A. 模块化组合（assemble-to-order）** | Emtek SELECT、Rocky Mountain、Sun Valley、Modern Matter | 部件 × 饰面组合；十档杆长 | **Emtek 2–3 工作日**；铸造类 10–12 周 | 海外预饰面部件 + 美国单点组装 |
| **B. 尺寸按单（fabricate-to-order）** | US：Highland Forge、Morgik、Semi Exact、Vault、Allied Brass、Kul Grilles、SteelCrest；DE：PHOS、Stahldeko、BFB、HS-Mechanik、bauhaus-crafts、Signostar；UK：Swarf、Made by the Forge | 长度连续、L×W、RAL 色 | 2–6 周（Kul Grilles 定制 5.5–6 周、SteelCrest 4 周、Highland Forge 3–4 周、bauhaus-crafts 3 周）；例外：Signostar 门牌 10–12 天、The Curtain Pole and Track Company 48 h express、Rustica 3–5 天 | **全部单点自有小厂**，无人用分布式网络 |
| **C. 图案个性化（POD）** | YouCustomizeIt 把手、Etsy 3D 打印把手 | 表面图案 | 数天 | 打印 |

**关键观察**：
- UK 设计品牌（Armac Martin、Buster + Punch、Corston、Formani）的 "made to order" 是**批量按单 + 饰面选择**，尺寸固定，不是参数化。只有 Swarf（小作坊）卖定制长度 + 定制色（£30 起，定制色 £120，5 工作日）。
- 德语区真有"nach Maß"到 2500 mm 的杆拉手供给（HS-Mechanik、BFB、Häfele），但**全部询价制**，无 D2C 配置器——这是欧洲最明显的"配置器缺口"，但客群是 B2B 家具厂。
- 定长不加价是常态：Curtarra 任意宽度 $159–199 各饰面同价；Etsy 黄铜毛巾杆 "custom cuts at no extra charge"。**客户预期定长是免费的，溢价在饰面 / 设计层。**
- 配置器最成熟的品类是**门牌**（Signostar €20 起 / LETTERCUT $15.48/字符、2–5 天）和**玻璃淋浴隔断**（One Bath 3D 实时报价 €122–1,062；Duschenprofis 7 天）。前者竞争充分，后者不是 KES 材料。

### 2.2 AI 使用：零

美欧所有五金厂商页面均无 AI 声明。仅见 B2B 配置器服务商（Leading Systems、Zolak）在卖"KI-gestützt"。AI 在家装商务的实际落点是零售商选购助手，不在品牌接单端。

---

## 3. 技术与运营底座：哪一环真的卡

```
AI 接单 ──→ 参数化设计 ──→ 在地加工 ──→ 饰面 ──→ 组装 ──→ 交付
  便宜        便宜         成熟(钣金)    ✗ 墙     ✗ 无网络   天级(仅裸件/粉末)
```

| 环节 | 现状 | 对 KES 的含义 |
|---|---|---|
| **AI 接单** | Amazon Custom 免费提供 Personalize / Configure / Assemble 三模式（≤100 options、可预览）；LLM 前端填 3–6 参数即可，不需要 text-to-CAD | 不是壁垒，也不是差异化 |
| **在地切割 / 折弯** | US：SendCutSend（304 SS 2–4 天、无 MOQ、$100M 营收）、OSH Cut（2 工作日、管激光）、Xometry（有 API）；EU：247TailorSteel 48 h、Laserhub 有 API、Fractory < 9 工作日 | 平板 / 折弯 / 管切裸件可以按单、天级、qty 1 |
| **成本差** | 铝支架带黑粉末 qty 10：SendCutSend ~$28.50 vs 中国工厂 ~$22.00（运费前）；盈亏平衡 ~50 件 | qty 1–10 只贵 20–30%，加工经济性不是阻碍 |
| **装饰饰面** | 粉末涂层（哑光黑）即时报价 +3–5 天；**PVD 拉丝镍 / 拉丝金 / 黑：MASIC "not available for single product coatings"，Providence 2–4 周** | **KES 核心饰面在地不可做**。只有哑光黑走得通 |
| **组装 / 焊接** | 无任何网络即时报价"管 + 座 + 紧固件"总成 | 毛巾杆 / 扶手需要自有或合同组装单元（Emtek 式固定成本节点） |
| **退货** | Amazon 2023-02 起定制品不可退；EU Directive 2011/83/EU Art.16(c) 定制品排除 14 天撤回 | 毛利友好，但测量错误的成本全在品牌 |

### 3.1 失败案例的两种死法

| 案例 | 死法 | KES 是否暴露 |
|---|---|---|
| Shapeways（Ch.7 2024）：营收 $34.5M、毛利 42%、净亏 $43.9M | 固定开销 + 外协稀释质量 | 若建美国组装节点 → 暴露 |
| Made.com（2022）、Interior Define（2023） | 海外 MTO 长链：客户等数月 + 现金压库存 / 卡港口 | 若从中国按单发货 → 暴露 |
| Opendesk | 分布式 maker 网络做不出电商级一致性和毛利，退出电商 | 若走分布式网络 → 暴露 |
| Tylko（挣扎）：€60M 营收但最新融资是 EIB 债务、交期 3–6 周、10x IKEA 价 | 参数化 CNC 可行但慢且贵 | 参照上限 |

---

## 4. 市场规模：无法自上而下引用

- 无任何可打开的来源披露美 / 欧单独的 decorative hardware 或 bath accessories TAM。研究公司全球数字（builder hardware $52.8B、bathroom accessories $25.6B 含地垫垃圾桶）低信任。
- 可用锚点（上市公司）：Hillman "~$6B" 美国五金市场（含紧固件、builders hardware、wall hanging；75% DIY）；Masco Plumbing $5.2B（含 bath hardware）；HHI $1.3B；Hettich €1.4B（-2%）；Häfele €1.72B。
- 2025 住宅五金需求全行业 flat-to-weak（ASSA ABLOY、Masco、Hettich 口径一致）。
- **定制切片规模：无任何来源。** 唯一可参照的是 Etsy 全站 30% custom GMS，但不能映射到五金。

---

## 5. KES 适配性诊断

| KES 资产 / 约束 | 对在地定制成品模式 | 对"尺寸阶梯 + 选配助手"模式 | 对钣金粉末试点 |
|---|---|---|---|
| 304 不锈钢 + 拉丝饰面平台 | ✗ 拉丝饰面在地不可做 | ✓ 直接复用 | ○ 不同材料（碳钢 / 铝 + 粉末），需新供应逻辑 |
| 亚马逊评论飞轮 | ✗ 定制 SKU 无评论积累结构 | ✓ 变体挂在父 ASIN 下共享评论 | ○ 新品类从零起 |
| $25–90 ASP | ✗ 撑不起美国组装节点 | ✓ | ○ 支架 $40、通风口盖 $84 有空间 |
| 无美 / 欧物理节点 | ✗ 必须新建 | ✓ 不需要 | ✓ 用 SendCutSend / OSH Cut 代工，无固定成本 |
| Wayfair / Home Depot 渠道（[[north-america-growth-marketplace-opportunity-research]]） | ○ Home Depot 项目型场景可能接受较长交期 | ✓ 变体矩阵正是 Wayfair 心智 | ✓ 通风口盖是 Home Depot 品类 |
| EU 无既有渠道 | ✗ 双重新（新市场 + 新模式） | — | ✗ PPWR 每国授权代表 + €3/件关税 + 无渠道 |

---

## 6. 品类筛选矩阵

评分维度：需求形态（亚马逊大词 / 站外定性）、定制变量真实性、在地工艺可达性（粉末 vs PVD）、KES 平台复用、现有竞争、进入形态。

| 品类 | 需求信号 | 定制变量 | 在地工艺 | KES 复用 | 竞争 | **判断** |
|---|---|---|---|---|---|---|
| **通风口 / 回风格栅（US）** | 痛点被多家商家写成卖点；Amazon 尺寸词无量 | 高（L×W 连续） | ✓ 平板激光 + 粉末，SendCutSend 标准能力 | 低（新品类） | 现有定制交期 4–6 周 + 电话报价，差距最大 | **试点 #1**：输入尺寸 → 即时价 → 一周到货 |
| **悬浮架 / 搁架支架** | US floating shelves for bathroom 3,606/周；heavy duty brackets 249/周 | 高（10"–86"） | ✓ 冲压 / 激光 + 粉末 | 中（metal storage 相邻） | Semi Exact $41、Vault $46–316 均"contact for custom" | **试点 #2** |
| **毛巾杆（切长）** | US 6,982/周、DE 18,348/周大词；长度痛点由伸缩杆承接 | 中 | ✗ 拉丝 304 在地不可饰面；需 Emtek 式预饰面管 + 美国切长组装 | ✓ 核心品类 | 定制供给全是 $92–115 小作坊 | **先做尺寸阶梯（12/18/24/30/36"）+ 选配助手；组装节点仅在阶梯验证后考虑** |
| **扶手 / grab bar** | US 4,210/周，CPC $3.63 最高，转化 0.229 最高；aging-in-place 41–49% | 中（长度）；**但 Doc M 450/600 mm、DIN 18040 偏好标准长度** | ✗ 同毛巾杆 | ✓ | Allied Brass $223–319 装饰扶手档存在 | **尺寸 + 饰面阶梯（装饰化扶手），不做定长** |
| **柜门拉手（任意 CTC）** | US cabinet pulls 5,394/周；3"/5" 尺寸词是唯一成型的尺寸词（651/429） | 中（CTC 孔距） | ○ | ○ | Emtek SELECT 已做十档长度 1–3 天 | **做英制孔距阶梯（3"/3.75"/5"/6"）+ 背板选配，不做任意 CTC** |
| **定长窗帘杆** | US curtain rods 172,002/周（最大）；DE 25,434；UK bay window 痛点明确 | 高 | ✗ 管 + 饰面同毛巾杆问题 | ○（curtains 有品类） | 伸缩杆已吞掉 70–85%；定长 DTC 按平价卖 | **观察**：需求最大但溢价最弱，且伸缩杆已是"够用的定制" |
| **门牌 / 地址牌** | US modern house numbers 1,188/周；DE hausnummer edelstahl 805/周 | 高（字体 / 高度 / 饰面） | ✓ 激光 + 粉末 | 低 | Signostar €20 / LETTERCUT $15/字符 / 2–5 天，已被高效做好 | **不做**：进入空间只剩黄铜饰面（3–4 周） |
| 散热器罩（UK） | radiator cover 25,011/周 | 高 | ✓ 金属穿孔板激光 | 低 | MDF 标准罩主导亚马逊 | **观察**：金属版定制是欧洲缺口，但 KES 无 UK 渠道 |
| Stangengriffe 到 2500 mm（DE） | B2B | 高 | ○ | ○ | 全询价制，配置器缺口 | **不做**：客群是家具厂 |
| 玻璃淋浴隔断 / 门锁把手 / 活性黄铜 | — | — | — | ✗ | — | **不做**（材料 / 工艺 / 已有 NO-GO） |

---

## 7. 建议路径与 Gate

### Tier 0 — 零固定成本，现有平台内（建议立即做）

**把"定制"翻译成"更密的尺寸阶梯 + AI 选配助手"。** 依据：亚马逊需求只以通用词 + 变体挑选表达；父 ASIN 变体共享评论飞轮；Amazon Custom Configure 模式免费。

- 毛巾杆 12 / 18 / 24 / 30 / 36" 全阶梯（现在主流只有 18 / 24）；扶手 16 / 24 / 32 / 36 / 48" × 拉丝 / 哑光黑 / 拉丝金；柜门拉手英制孔距 3" / 3.75" / 5" / 6" 补齐。
- AI 选配助手放在 listing 内容 + 官网：拍照 / 输入旧孔距或墙面宽度 → 推荐档位 → 说明公差与安装。这与 [[kes-ai-era-amazon-content-strategy-judgment]] 的 Rufus 结构化内容路线是同一件事——把"尺寸怎么选"写成 Rufus 能引用的问答。
- **Gate 0**：新增长尾尺寸 SKU 6 个月内的销量 / 父 ASIN 占比、"尺寸不合"退货率变化、选配助手使用率。

### Tier 1 — 钣金粉末试点，代工无节点（Gate 0 无关，可并行小额验证）

- 品类：通风口 / 回风格栅（US 优先）、搁架支架。材料：碳钢 / 铝 + 哑光黑粉末，不用 304。
- 形态：DTC 或 Amazon Custom Configure（输入 L×W → 报价 → SendCutSend / OSH Cut 代工直发）。承诺交期 7–10 天（对手 4–6 周）。
- **前置字段工作**：上传 3 个真实图纸到 SendCutSend / OSH Cut / Xometry 拿 qty 1 / 10 / 100 即时报价；确认粉末色与 KES 哑光黑一致性；确认 API / 批量下单方式（SendCutSend 无公开 API）。
- **Gate 1**：单件毛利 ≥ 40%、交付准时率 ≥ 95%、测量错误退货 ≤ 5%（EU 与 Amazon 定制品不可退，但品牌口碑会承担）。

### Tier 2 — Emtek 式切长组装（仅在 Gate 0 出信号后）

- 中国预饰面 304 管（拉丝 / PVD）+ 通用端座 → 美国 3PL 或合同组装切长 + 装配 → 2–3 天发货。"定制"限于长度 + 饰面组合，不含表面按单。
- 需要产品重新设计为"切长友好"（滑套端座、不外露切口）。
- **Gate 2**：Tier 0 长尾尺寸占父 ASIN ≥ 15% 且客服中"没有我要的长度"出现频次可量化；组装节点固定成本 < 预计毛利的 50%。

### 不做

- 在地制造成品拉丝 / PVD 五金；任意 CTC 拉手；门牌；玻璃隔断；活性黄铜（[[unlacquered-brass-finish-gonogo-2026]]）。
- **EU 首发**：加工网络更快（48 h、有 API）但 PPWR 每目的国授权代表、2026-07 起 €3/件临时关税、KES 无既有渠道，是"新市场 × 新模式"双重风险。EU 只在 US Tier 1 跑通后作为第二站，且 Art.16(c) 定制品排除退货是有利条件。

---

## 8. 不确定性与待字段工作

**桌面研究无法填补的卡点**（沿用 "字段工作"标注）：

1. **真实图纸的即时报价**：KES 毛巾杆 / 扶手 / 一款通风口盖在 SendCutSend、OSH Cut、Xometry、Laserhub 的 qty 1 / 10 / 100 价格与交期。所有公开价格都是示例件。
2. **小批装饰 PVD 供应商**：美 / 欧是否存在 ≤ 5 天、每件最小量可接受的拉丝镍 / 金 / 黑 PVD 服务。本次调研结论是"未找到"，不是"不存在"。
3. **定长卫浴五金付费意愿**：无任何专项调查；DTC 现状是定长不加价。需要 A/B（同款 24" vs "选你的长度"）实测。
4. **非标尺寸普及率**：老房 → 非标 → 定制需求是推论。需要从 KES 自有客服 / 退货记录中量化"尺寸不合"占比。
5. **Amazon Custom 在五金的转化与测量错误率**：无公开数据。

**方法论限制**：Etsy 市场页、Amazon 商品页、多家品牌官网 403，Etsy 结果数 / 销量未获得；Google Trends 未查；Reddit / Houzz 一手抱怨仅零星（WoodWeb 一例、Mumsnet 9 帖）。本页 confidence = medium：供给结构和工艺卡点是直接证据（高），需求规模与溢价是定性推断（低）。

---

## Related pages

- [[unlacquered-brass-finish-gonogo-2026]] — 同一方法论坑（用亚马逊判断站外品类）与"KES 是不锈钢平台"的材料约束
- [[north-america-growth-marketplace-opportunity-research]] — Home Depot 项目型 / Wayfair 变体矩阵心智，是 Tier 0 / Tier 1 的渠道落点
- [[kes-ai-era-amazon-content-strategy-judgment]] / [[amazon-rufus-cosmo-e-geo-kes-response]] — AI 选配助手与 Rufus 结构化内容是同一路线

## Sources

- `raw/strategy/custom-hardware/2026-09-06-amazon-keyword-customization-signal.md` — US / DE / UK 站 ABA 周数据（xydc-mcp，2026-08-23 ~ 08-29）
- `raw/strategy/custom-hardware/2026-09-06-us-custom-hardware-supply-scan.md` — 美国供给侧 45 次抓取
- `raw/strategy/custom-hardware/2026-09-06-eu-custom-hardware-supply-scan.md` — 欧洲供给侧 + 法规（Directive 2011/83/EU Art.16(c)、IOSS / €3 关税、PPWR、EN 1906、DIN 18040）
- `raw/strategy/custom-hardware/2026-09-06-ai-configurator-and-local-fab-stack.md` — Tylko / Emtek / SendCutSend / PVD 瓶颈 / Shapeways 等失败案例
- `raw/strategy/custom-hardware/2026-09-06-market-size-and-demand-signals.md` — Etsy 10-K、Masco / Hillman / ASSA 财报、Houzz 2025、NAHB 房龄、Lowe's Mylow / Home Depot Magic Apron
