---
type: synthesis
status: active
created: 2026-05-10
updated: 2026-05-10
tags: [ecommerce, marketplace, north-america, homedepot, wayfair, walmart, kes]
domain: ecommerce
domains: [ecommerce, marketplace, operations, channel-strategy, north-america]
source_count: 18
confidence: medium
review_cycle: monthly
verification_status: spot-checked
related:
  - ../protocols/cross-border-ecommerce-operations-performance-framework.md
  - ../projects/kes-product-market-research-tooling.md
  - ../protocols/llm-product-market-research-for-kes-categories.md
---

# 北美增长平台组机会研究：Home Depot / Wayfair / Walmart

## Core thesis

北美增长平台组不能再被整体视为“新平台探索”。按 2026-05-10 用户补充的经营现状和 V2/V3 绩效文件：
- Wayfair 已是稳定收入平台，V2 里 2026 年 1-3 月销售约 5.7-6.6 万美元/月。
- Home Depot 已有稳定业务收入，但当前更接近 2.5 万美元/月，阶段目标是 6 月稳定到 3 万美元/月。
- Walmart 仍然只有每月几百美元收入，属于早期冷启动。

因此三平台应分层管理：

```text
Wayfair / Home Depot：从已有收入盘走向稳定增长、利润优化、库存稳定和可复制经营
Walmart：从几百美元/月走向可运营 marketplace 的基础闭环验证
```

这意味着北美增长平台组的第一阶段目标不是简单判断“能不能做”，而是判断：

```text
哪些 KES 产品，适合在哪个平台，以什么合作/履约/内容方式，进入 US 和 CA 市场。
```

这三类平台的入口机制不同：
- `Walmart` 更接近开放 marketplace：Seller Center、referral fee、WFS/自发货、绩效指标清晰。
- `Home Depot` 更接近零售 merchant / supplier 选择机制：通过 New Product Submission 或 Supplier Pipeline，被 merchant team 审核。
- `Wayfair` 更接近家居垂直 supplier partner 体系：强调家居品类、供应商合规、内容质量、物流与平台体验。

因此北美增长平台组的绩效不能一刀切：
- Wayfair / Home Depot 应纳入经营结果、贡献利润、订单质量、内容效率和规模化能力。
- Walmart 应先围绕平台基础建设、有效 SKU、Listing Quality、履约、早期流量和首批订单质量。
- 三个平台还必须纳入“产品版本与价格分层”约束，避免跨平台同款比价把利润打穿。

## Strategic constraint: product and price tiering

2026-05-10 与 team lead 沟通形成一个关键判断：KES 多平台销售不能继续依赖“同一 SKU 多平台复制”。原因是跨平台比价机制会把不同平台的价格和利润绑在一起。

已观察到的平台机制：
- Wayfair 存在全平台比价机制，若同款价格高于其他平台，会降低自然流量分发和账号价格竞争力评分。
- Walmart 是强价格导向平台，会对标 Amazon 形成价格压制。
- Home Depot 暂无同样透明的系统性比价提示，但买手可能调整前台价格；若价格被判定无竞争力，会压缩买手利润空间，并影响后续上架审批。

旧模式的问题：
- 同一 SKU 跨平台销售，完全可比，价格成为唯一竞争维度。
- Walmart 低价会反向压低 Amazon / Wayfair / Home Depot 的价格空间。
- Wayfair / Home Depot 这种本应有溢价的平台失去意义。
- Amazon Buy Box 也可能被低价平台反向影响。

新的产品策略：

```text
开发 1 个产品能力，而不是开发 1 个完全相同 SKU
同一产品能力同步设计 3 个渠道版本
```

建议版本分层：

| 平台 | 版本 | 价格锚点 | 设计逻辑 |
|---|---|---:|---|
| Amazon | Core / 标准版 | 100% | 主流配置，作为市场价格锚 |
| Walmart | Entry / 减配版 | 95%-100% | 降低配置或包装成本，适配价格敏感用户 |
| Home Depot | Premium / 项目版 | 105%-115% | 强化安装、认证、配件、Pro/DIY 项目价值 |
| Wayfair | Premium / 场景版 | 110%-130% | 强化场景、材质、套装、风格和家居表达 |

关键不是机械涨价，而是让价格差异有可解释的产品差异：
- 配件数量不同。
- 尺寸不同。
- 材质/表面处理不同。
- 包装/说明书/安装支持不同。
- 套装组合不同。
- 保修、认证、测试验证或 Pro 场景资料不同。

## Platform map

### Walmart US / Walmart Canada

Walmart 是三者中最像可系统化运营的 marketplace。

已确认事实：
- Walmart Marketplace 使用 Seller Center 管理注册、账号设置、报告和商品表现。
- Walmart Marketplace 官方强调没有 setup、monthly 或 hidden fees，主要按成交收 referral fee；不同品类费率不同。
- Walmart US 要求 catalog 符合 prohibited products policy，并通过 WFS 或有 B2C US warehouse、退货能力、并能遵守 seller performance standards。
- Walmart US 的 performance standards 包括取消率、准时送达、有效 tracking、seller response、return、item not received、negative feedback 等。
- Walmart Canada 是 curated marketplace；卖家可管理目录、订单、发货和客服。官方 Canada learn 页面显示，接受 Canada、US、UK、China、Hong Kong、India 卖家，但需要 Canadian Business Number 和 Non-resident Importer 设置。

对 KES 的含义：
- Walmart 当前仍是早期冷启动平台，月收入只有几百美元；它的优先级不是“短期收入贡献”，而是验证 KES 能否把 Amazon 成熟 SKU 迁移成 Walmart 可运营 SKU。
- US 和 CA 要分开验证：US 关键是 B2C 仓/退货/WFS 和绩效；CA 关键是 BN、NRI、CAD 收款和跨境履约。
- Walmart 适合建立 SKU 级利润模型和平台 scorecard，较早进入“可运营指标”阶段。
- Walmart 的 Listing Quality 机制把内容、价格竞争力、配送、库存、ratings/reviews 等放进同一个质量评分视角，说明它不是只看关键词和广告，而是把商品页、offer 和履约一起决定曝光与转化。

优先验证：
- KES 是否已有适合 Walmart 的 UPC/GTIN、合规资料和品牌/授权资料。
- US 仓、WFS 或第三方 B2C 仓是否能满足准时送达、tracking、退货。
- CA 是否能完成 Canadian BN / NRI / Payoneer / CAD 结算路径。
- Amazon 成熟 SKU 中哪些在 Walmart 上仍有价格带和评价空位，而不是只复制同质化 SKU。

### Home Depot US / Canada

Home Depot 不是普通开放 marketplace 逻辑，更像通过 merchant team 审核进入线上/线下零售供应体系。

已确认事实：
- Prospective suppliers for US stores or homedepot.com should use New Product Submission; Home Depot merchant team will contact within 60 days if there are next steps.
- Home Depot Canada prospective suppliers for stores or homedepot.ca 使用 Canada New Product Submission。
- Home Depot 还有 Supplier Pipeline Program，定位是扩大供应商基础、促进创新，并覆盖 merchandising 和 non-merchandising suppliers。

对 KES 的含义：
- Home Depot 当前约 2.5 万美元/月，6 月阶段目标是稳定到 3 万美元/月；它不能再按纯探索期处理，应从“能不能进”转为“如何提高销售质量、利润、库存稳定和可扩展 SKU 池”。
- 机会更偏 home improvement / DIY / project-based purchase，而不是一般家居装饰搜索流量。
- 如果 KES 产品需要安装、测量、工程场景、B2B/Pro 需求或项目化购买，Home Depot 价值更大。
- 对已有收入 SKU，应重点优化项目型内容、价格/毛利、履约质量和 retail media；对新增 SKU，仍适合用 merchant-ready proposal 控制质量，而不是大批量铺货。
- Home Depot 的 Orange Apron Media 已经形成 onsite/offsite、Product Listing Ads、Brand Pages、display 和自助广告平台 Orange Access；这意味着一旦进入渠道，后续增长不只是“被采购上架”，还要能用项目场景、品牌页和零售媒体承接高意图流量。

优先验证：
- KES 哪些产品能被讲成 Home Depot 语境下的 DIY / pro / project solution，而不是 Amazon 单品。
- 产品是否有清晰包装、说明书、安装支持、认证、质保、售后能力。
- 是否适合 homedepot.com online-only，还是需要进入门店/Pro 体系。
- US 与 Canada 是否需要分别准备提案、价格、认证、物流和售后资料。

### Wayfair US / Canada

Wayfair 是家居垂直平台，不是纯通用 marketplace。

已确认事实：
- Wayfair 官方 Partner With Us 页面把 supplier partner 定位为销售 home goods online 的新渠道，强调 merchandising、tech 和 home-category experience。
- Wayfair corporate fast facts 显示其产品和供应商规模很大，并在 North America 与 Europe 有物流、delivery、service 网络。
- Wayfair Supplier Code of Conduct 要求供应商遵守法律、平台政策和诚信/伦理/可持续商业实践；违规可能导致产品下架或账号暂停/终止。
- Supplier Code 中明确要求 one listing per product，禁止重复或近似重复 listing；Wayfair 可审计供应商，并要求 48 小时内提供所需文件。
- Wayfair 对 catalog findability 有专门平台，目标是减少不可展示商品、降低法律责任、提高供应商和内部团队解决路径清晰度。

对 KES 的含义：
- Wayfair 已经是稳定收入平台，V2 中 2026 年 1-3 月销售约 5.7-6.6 万美元/月；当前重点不是证明平台可行，而是把收入盘做成可复盘、可扩 SKU、可控退货和可控利润的经营系统。
- Wayfair 更适合家居、软装、家具、窗帘、装饰、空间解决方案类产品，而不是泛标品。
- 内容、图片、属性、变体、风格、尺寸、材料、合规和物流体验会比 Amazon 上的关键词打法更重要。
- Wayfair 对重复 listing、资料真实性、供应商审计和产品可展示性较敏感，不能用 Amazon 多 listing、多变体试错方式粗暴迁移。
- 对 KES 来说，Wayfair 的机会可能在“家居场景表达 + 变体/尺寸/风格组织 + 供应链稳定性”。
- Wayfair 对 catalog accuracy、attribute tags、findability 和 supplier support 投入很重；这说明 Wayfair 的增长基础是结构化商品数据质量，而不是单纯广告加预算。
- CastleGate 提供国际物流、履约、两日达覆盖和 multichannel fulfillment 能力；对大件、长件、家居类产品，Wayfair 的物流能力本身可能是平台机会的一部分。

优先验证：
- KES 哪些产品在 Wayfair 的 home category 心智下更自然。
- 是否能提供足够专业的图片、尺寸、材质、安装、风格、场景和 packaging 信息。
- 是否具备审计资料、供应链文件、合规证明和 48 小时响应能力。
- 大件/长件/易损件的破损率、退货率和 delivery experience 是否可控。

## Operating strategies

### Walmart strategy: cold-start the marketplace operating loop

战略定位：
- Walmart 是北美增长平台组里的早期冷启动项目，当前月收入只有几百美元。
- 它的短期目标不是利润贡献，而是把平台基础闭环从 0 跑到可判断。
- 当前已筛选小件产品发往 WFS 仓，预计 6 月完成首批入仓并启动销售；6 月核心是首批 SKU 的转化率和履约稳定性验证。
- 它可以承接 Amazon 已验证 SKU，但不能只做复制粘贴；Walmart 的增长机制把 listing quality、价格、配送、库存、评价和绩效放在一起。
- Walmart US 应先做标准化运营闭环，Walmart Canada 暂时只做路径准备，除非 US 已出现可复制信号。

#### Product selection

优先选择：
- Amazon US/CA 已经验证需求、退货率低、评分稳定的 SKU。
- 体积和重量适合 WFS 或稳定 B2C 仓发货的 SKU。
- 基于体积和履约成本优化的小件 SKU。
- 不依赖复杂安装或重客服解释的 SKU。
- 在 Walmart 搜索结果里存在价格带、评价数或内容质量空位的 SKU。
- 适合家庭日用品、家居改善、收纳、软装、工具配件、低售后复杂度的 SKU。
- 与 Amazon / Wayfair / Home Depot 形成配置差异，避免完全同款比价。

暂缓选择：
- 大件、长件、破损率高、退货运费高的 SKU。
- 需要大量售前咨询或安装判断的 SKU。
- Amazon 已高度同质化、只靠最低价竞争的 SKU。
- 需要复杂合规认证但资料未齐的 SKU。

#### Content and listing strategy

Walmart listing 不应直接复制 Amazon 文案。应建立 Walmart 专用字段和质量检查：
- 标题：清楚、直接、包含核心属性，不堆关键词。
- Key features：用用户能理解的功能/规格/使用场景表达，不写泛泛卖点。
- 图片：主图清晰，辅图解释尺寸、安装、使用场景、包装和兼容性。
- Attributes：优先补齐类目属性，因为 attributes 影响 discoverability 和筛选。
- Offer：价格、配送速度、库存和退货承诺要和内容一起管理。

最低运营标准：
- 每个 pilot SKU 建立 listing quality baseline。
- 上架后每周看质量分、曝光、点击、转化、退货原因、价格竞争力。
- 对低分 SKU，优先修 content / attributes / shipping / price，而不是先加广告。

#### Fulfillment and price strategy

Walmart 的经营重心要从“能发货”提高到“发货体验能提升转化”：
- 优先评估 WFS，尤其是标准件、轻小件、高复购或稳定销量 SKU。
- 自发货 SKU 必须确认 tracking、准时送达、取消率和退货处理能力。
- US 与 CA 分开建利润模型：CA 不能只套 US 成本，需要考虑 BN/NRI、CAD 收款、进口责任、退货路径和汇率。

定价原则：
- 不以低于 Amazon 的裸价作为唯一策略。
- 对比 Walmart 站内、Amazon 和其他零售渠道的 landed price。
- 把 WFS 成本、referral fee、退货、广告、价格竞争力统一进 SKU P&L。

#### Traffic and advertising

Walmart Connect 可以作为第二阶段工具，不是第一天的主要增长手段。

广告前置条件：
- Listing Quality 达到内部最低线。
- 库存稳定。
- 价格有竞争力。
- 配送承诺可靠。
- 至少有一批 SKU 已经能自然产生曝光/点击信号。

广告打法：
- 先用 Sponsored Search 验证关键词和平台需求。
- 广告指标不只看 ROAS，还看是否带来 listing quality、自然排名、评价和稳定订单。
- 对广告亏损 SKU，先判断是内容/价格/配送问题，还是平台需求不匹配。

#### Walmart KPI

探索期 KPI：
- 账号/后台/税务/付款/退货路径完成。
- pilot SKU 上架成功率。
- 首批 WFS SKU 入仓及时率。
- Listing Quality baseline 和提升幅度。
- WFS eligible / WFS active SKU 数。
- 有曝光、有点击、有订单的有效 SKU 比例。
- 月收入从几百美元提升到第一个可复盘台阶，例如 3,000-5,000 美元/月。
- 至少找出 5-10 个能持续产生曝光/点击/订单的有效 SKU。

稳定期 KPI：
- 贡献利润。
- WFS vs seller fulfilled 表现差异。
- 准时送达、取消率、退货率、客服响应。
- 广告带来的新增订单和自然流量改善。
- Walmart 专属有效 SKU 数。

### Wayfair strategy: win through catalog depth, home-context content, and delivery trust

战略定位：
- Wayfair 已经是 KES 的稳定收入平台，V2 文件显示 2026 年 1-3 月约 5.7-6.6 万美元/月。
- 下一阶段目标是把 Wayfair 从“有收入”推进到“有稳定贡献利润、可扩品类、可控退货、可复用内容系统”。
- 近期管理动作应聚焦三件事：类目扶持策略、线下门店/展示资源、新品冷启动机制。
- Wayfair 应被当作家居垂直渠道，不是 Amazon 的流量复制。
- 它更适合 KES 中“家居场景强、审美/尺寸/风格/安装解释重要、可做变体矩阵”的产品。
- Wayfair 的核心经营能力是 catalog data + visual merchandising + fulfillment reliability。

#### Product selection

优先选择：
- 窗帘、软装、装饰、收纳、家居改善中视觉和风格权重高的 SKU。
- 可以用尺寸、颜色、材质、风格、空间场景形成系统化变体的 SKU。
- 适合 room scene、installation guide、style guide 表达的 SKU。
- 退货原因主要可通过更好内容和尺寸说明减少的 SKU。
- 能承担 Wayfair 促销和供应商配合机制的 SKU。

暂缓选择：
- 缺少稳定供应链资料、材质说明和合规文件的 SKU。
- 容易破损、尺寸误解严重、退货运费高但内容无法解释清楚的 SKU。
- 只靠低价和关键词竞争的泛标品。

#### Catalog and content strategy

Wayfair 的内容不是 PDP 文案，而是一个 structured catalog asset。

每个 SKU/变体组应建立：
- `attribute map`：颜色、材质、尺寸、安装方式、适用空间、风格、功能、护理方式。
- `variant logic`：哪些应合并为变体，哪些必须拆开，避免重复/近似重复 listing。
- `visual set`：主图、空间图、尺寸图、材质细节图、安装图、包装图。
- `decision support`：测量指南、安装指南、搭配建议、常见误区。
- `trust file`：质保、认证、测试、供应商文件、合规文件。

内容策略目标：
- 提高可搜索、可筛选、可理解、可比较。
- 减少因尺寸、颜色、材质、安装预期错误导致的退货。
- 让平台系统和人工审核都能快速理解产品。

#### Fulfillment and operations strategy

Wayfair 的家居产品履约体验本身就是竞争力：
- 对标准件，评估直接履约 vs CastleGate Fulfillment。
- 对跨境或大件，评估 CastleGate forwarding / fulfillment 是否能降低配送时效和破损风险。
- 对多平台大件履约，关注 CastleGate multichannel fulfillment 是否能成为北美家居物流基础设施的一部分。

运营重点：
- 建立 damage / return / replacement reason taxonomy。
- 对每个 SKU 记录破损点、包装改进、图片误解点、尺寸误解点。
- 用内容和包装共同降退货，而不是只靠客服补救。

#### Promotion and economics

Wayfair 的促销需要单独建模。供应商很可能要承担促销折扣的一部分，不能只看标价毛利。

每个 SKU 应测算：
- 平时价毛利。
- 促销价毛利。
- 平台活动参与成本。
- 退货/破损/换货成本。
- CastleGate 或自履约成本。
- 促销带来的非促销 SKU 联动是否存在。

经营原则：
- 不参加看似有曝光但会破坏毛利和退货结构的活动。
- 优先用高质量内容和组合变体提高转化，而不是长期低价。

#### Wayfair KPI

当前阶段 KPI：
- 月收入稳定性和环比增长。
- 价格竞争力评分和自然流量变化。
- SKU/变体组贡献利润。
- 退货率、破损率、replacement rate。
- 内容修正后转化、曝光、搜索表现变化。
- CastleGate vs 自履约表现。
- 活动参与后的真实利润和长期排名/曝光变化。
- supplier / compliance / audit 文件齐套率。
- content issue / findability issue 关闭时效。
- 新增有效 SKU/变体组数量，而不是单纯新增 listing 数量。

### Home Depot strategy: build merchant-ready project solutions, not a SKU dump

战略定位：
- Home Depot 当前约 2.5 万美元/月，6 月阶段目标是稳定到 3 万美元/月。
- 下一阶段目标不是进入渠道，而是提高现有收入质量，解决上新审核慢和核心 SKU 缺货，并围绕 DIY / Pro / project solution 扩大有效 SKU 和项目型内容。
- Home Depot 的核心机会是 home improvement、DIY、Pro、项目型采购和高意图零售流量。
- 对 KES 来说，Home Depot 的新增机会仍然不是大批量铺货，而是把已有成功经验转成少数强 SKU 的项目型扩张。

#### Product selection

优先选择：
- 能解决明确 home improvement / installation / project problem 的产品。
- 有工程、安装、测量、耐用、安全、节省时间等明确价值的 SKU。
- 可面向 DIY 用户或 Pro 用户讲清楚使用场景。
- 包装、说明书、质保、认证和售后路径成熟的 SKU。
- 与 Home Depot 类目/季节/项目流量有自然关系的 SKU。
- 能快速过审、能维持库存、能与既有核心 SKU 形成类目梯队的 SKU。

暂缓选择：
- 只是家居装饰，没有 project / improvement 语境的 SKU。
- 依赖 Amazon 搜索词和低价竞争的 SKU。
- 说明书、安装支持、包装强度、认证和售后未成熟的 SKU。

#### Merchant proposal strategy

Home Depot 的核心输出物不是 listing，而是 merchant-ready proposal。

每个候选产品要形成一份提案包：
- 产品解决什么 home improvement / DIY / Pro 问题。
- 目标用户：DIY homeowner、contractor、property manager、installer 或 decorator。
- 为什么适合 Home Depot，而不是只适合 Amazon。
- 类目和货架/线上位置假设。
- 价格带、竞品、差异化、毛利结构。
- 包装、安装说明、质保、客服和退货承诺。
- US/CA 版本差异。
- 线上 only、门店、Pro desk 或 mixed path 的建议。

提案原则：
- 用项目语言写，而不是 Amazon 卖点语言。
- 强调质量、可靠性、安装成功率、项目完成效率和售后责任。
- 准备少数最强 SKU 的完整资料，而不是先追求广覆盖。

#### Content and retail media strategy

一旦进入 Home Depot 渠道，增长应围绕“项目型购物路径”设计：
- PDP 内容要帮助用户判断适配、安装、材料、耐用性和项目完成方案。
- Brand Page 可作为品牌/系列/项目解决方案承接页，而不是只展示产品列表。
- Product Listing Ads 适合捕捉高意图搜索和类目页流量。
- Display / offsite / Reddit / Pinterest 等能力更适合在用户项目研究期种草和召回。

对 KES 的含义：
- Home Depot 内容系统要补“项目 brief”能力：用户项目、安装场景、前后步骤、所需工具、常见失败点。
- 广告是内容的放大器，不应为了测试广告而测试广告。应先完成 PDP 内容优化，再用广告验证内容是否能转化。
- HD 广告目前高 ROI 集中在少数产品，例如落地毛巾架 BTH501-BK 和吊顶锅架 KUR221S85-BK；探索品类广告亏损较多，应减少无结构的探索投放。
- HD 经验证更适合投大类搜索词；有效关键词应沉淀成 SST 表格进入团队知识库。
- L4327ALFF12-BK-C1 的案例说明 Pro 人群内容优化后，广告销售额从约 $100 提升到约 $610，平均月销从 8 提升到 17；这支持“先内容、后广告放大”的打法。

#### Fulfillment and channel strategy

Home Depot 要先判断路径：
- `online-only`：适合试水、长尾 SKU、变体多、门店不易陈列的产品。
- `store / aisle`：适合高动销、标准化、包装强、类目明确的产品。
- `Pro`：适合项目量、复购、安装/工程需求强的产品。
- `Canada path`：单独判断包装语言、认证、价格、税务、物流和售后。

运营重点：
- Merchant feedback pipeline。
- 提案提交状态和后续动作。
- 样品、包装、说明书和测试报告版本控制。
- SKU 被拒原因复盘。

#### Home Depot KPI

当前阶段 KPI：
- 月收入稳定性和环比增长。
- 6 月稳定达到 3 万美元/月。
- 贡献利润和 sell-through。
- online/store/Pro 路径表现。
- retail media 投入产出。
- 项目型内容带来的转化和退货下降。
- 现有 SKU 的价格、毛利、退货、缺货和广告效率。
- 新增被接受 SKU 数，以及新增 SKU 首 60-90 天表现。
- merchant-ready proposal 数量和质量。
- 核心 SKU 缺货率和补货响应。
- 可快速过审 SKU 池数量。

## Cross-platform operating model

北美增长平台组不应按平台各自孤立运营，而应建立一个 shared backbone：

### 1. SKU-platform fit matrix

每个 SKU 打三个平台的适配分：
- Walmart fit：marketplace demand、price competitiveness、fulfillment simplicity。
- Wayfair fit：home-context strength、attribute richness、visual/variant depth、delivery trust。
- Home Depot fit：project relevance、DIY/Pro usefulness、merchant readiness。

一个 SKU 可以适合多个平台，但必须解释“为什么适合”和“要如何改造”。

### 2. Platform packet library

建立三套资料包模板：
- Walmart packet：listing fields、attributes、WFS decision、price model、performance tracker。
- Wayfair packet：attribute map、variant map、visual set、compliance file、fulfillment plan。
- Home Depot packet：merchant proposal、project story、spec sheet、packaging/installation/support file。

### 3. Evidence review cadence

建议每两周做一次平台项目会：
- 入口/账号/合同阻塞项。
- SKU 选择和淘汰。
- 平台反馈。
- 内容质量和资料缺口。
- 履约、退货、毛利模型。
- 下一步实验。

每月做一次 scorecard：
- Wayfair / Home Depot：按收入质量、贡献利润、退货/破损、内容效率、SKU 扩张和广告/活动效率排名。
- Walmart：按平台基础建设、有效 SKU、Listing Quality、履约、早期流量和订单信号排名。
- 另设一个跨平台价格分层检查：是否存在完全同款跨平台互相压价；如有，必须进入配置差异化整改。

### 4. Kill criteria

每个平台都要有退出规则：
- Walmart：连续多个周期没有有效曝光/点击/订单，且 listing/price/shipping 已修正，进入淘汰。
- Wayfair：对新增 SKU，如果资料/属性/图片/履约无法达到平台要求，或退货/破损经济性长期不成立，进入淘汰；对既有收入 SKU，先进入整改而不是立即淘汰。
- Home Depot：对新增 SKU，如果 merchant feedback 连续表明类目/价格/包装/认证不匹配，且短期无法补齐，暂停推进；对既有收入 SKU，先做毛利、内容、履约和广告效率整改。

## Priority recommendation

建议执行顺序：

1. `Wayfair`：先把 3-5 万美元/月收入盘做成可增长、可控利润、可复盘的家居平台经营系统。
2. `Home Depot`：先把 2.5 万美元/月收入盘稳定到 3 万美元/月，解决缺货、快速过审 SKU 池和 PDP 内容放大模型。
3. `Walmart US`：作为冷启动项目，从几百美元/月推进到第一个可判断台阶，优先验证 5-10 个有效 SKU。
4. `Walmart Canada`：只做合规/结算/进口/退货路径准备，等 Walmart US 出现可复制信号后再规模化。

原因：
- Wayfair / Home Depot 已经有收入基础，最直接的机会是提升利润质量、降低退货/破损、扩展有效 SKU 和沉淀平台打法。
- Walmart 当前收入太小，不能用利润贡献考核；应该用冷启动指标管理。
- Walmart Canada 不应忽视，但不能把 US 经验直接复制过去。

## Recommended first 90 days

### Phase 1: Current business audit

输出三张表：
- `Wayfair / Home Depot business table`：近 6-12 个月收入、毛利、SKU、退货、破损、广告/活动、缺货、利润。
- `Walmart cold-start table`：账号、上架 SKU、Listing Quality、曝光、点击、订单、WFS/自发货、价格和阻塞项。
- `SKU-platform fit table`：现有 SKU 对 Home Depot / Wayfair / Walmart 的适配度和改造动作。
- `cross-platform price map`：Amazon / Walmart / Home Depot / Wayfair 同源产品的版本、配置、价格、毛利和比价风险。

第一阶段不是重新证明 Wayfair / Home Depot 能不能做，而是找出这两个平台的利润和增长杠杆，同时把 Walmart 的冷启动阻塞项拆清。

### Phase 2: Select pilot SKUs

分平台处理：
- Wayfair：从现有收入 SKU 中选出 top 10 做利润/退货/内容优化，再选 5-10 个相邻扩展 SKU。
- Home Depot：从现有收入 SKU 中选出 top 10 做项目型内容/广告/毛利/库存优化，再建立“可快速过审 SKU 池”。
- Walmart：优先选 20-50 个 Amazon 已验证、有价格带空间、适合 WFS/自发货的 SKU 做冷启动池。
- 跨平台：为同一产品能力设计 Core / Entry / Premium 版本，避免完全同款跨平台比价。

每个 SKU 都要写清：
- 为什么适合该平台。
- 目标用户和购买场景。
- 平台内容差异。
- 毛利和履约模型。
- 主要风险和 kill criteria。

### Phase 3: Build platform-specific operating packets

每个平台建立一套资料包：
- Walmart：Seller Center setup checklist、WFS/warehouse decision、performance dashboard、listing upload template、return SOP。
- Home Depot：merchant proposal deck、product spec sheet、packaging/installation/support file、pricing and margin file。
- Wayfair：supplier compliance file、content attribute schema、image/room scene requirements、variant rules、audit document folder。

### Phase 4: Pilot and evidence review

第一轮不要以销售额定胜负，而应看：
- 是否成功进入平台流程。
- 平台是否接受产品/资料。
- 是否能稳定发布商品。
- 是否出现自然曝光、点击、询盘、订单或 merchant 反馈。
- 履约、退货、客服和资料响应是否可控。
- 是否能形成可复制 SOP。

## Performance logic for the team

北美增长平台组建议拆成两套 scorecard，而不是一套平台探索表。

Wayfair / Home Depot 当前阶段 scorecard：

| 模块 | 权重 | 判断问题 |
|---|---:|---|
| 收入与贡献利润 | 30% | 3-5 万美元/月收入盘是否增长，利润质量是否改善 |
| SKU 经营质量 | 20% | top SKU 是否稳定，新增 SKU 是否真正有效 |
| 退货/破损/履约 | 20% | 退货、破损、缺货和售后是否可控 |
| 内容与转化效率 | 15% | 页面、属性、项目型内容、图片和资料是否提升转化 |
| 平台能力沉淀 | 10% | 是否形成 Wayfair / Home Depot 可复制打法 |
| 产品/价格分层 | 5% | 是否避免完全同款跨平台比价并形成版本策略 |

Walmart 当前阶段 scorecard：

| 模块 | 权重 | 判断问题 |
|---|---:|---|
| 基础闭环 | 25% | 账号、付款、退货、WFS/自发货、后台是否跑通 |
| 有效 SKU | 25% | 是否找出有曝光、点击、订单的 SKU |
| Listing Quality | 20% | 内容、属性、价格、配送和库存是否改善 |
| 首批订单质量 | 15% | 订单、取消、退货、tracking、客服是否可控 |
| 冷启动复盘 | 10% | 是否沉淀 Walmart 专属打法和淘汰规则 |
| 产品/价格分层 | 5% | 是否与 Amazon / WF / HD 形成配置差异，避免直接比价 |

Walmart 进入稳定期后，再逐步提高：
- 有效 SKU 数。
- 订单质量。
- 贡献利润。
- 退货率/取消率。
- 平台广告效率。
- 可复制类目数。

## Key risks

- 把 Home Depot 当成开放 marketplace，结果用错误节奏考核团队。
- 把 Wayfair 当成 Amazon 变体铺货场，触发重复 listing、内容质量或供应商合规问题。
- 只看 Walmart 的低进入门槛，低估绩效指标、退货、tracking 和客服响应。
- 同一 SKU 不改内容、不改包装、不改履约承诺就跨平台复制。
- US/CA 混在一起算，忽略 Canada 的 BN、NRI、CAD 收款和进口责任。
- 用短期销售额考核早期平台验证，导致团队选择最容易但最没有战略意义的 SKU。

## Open questions

- KES 目前是否已经有 Walmart US / Walmart Canada / Wayfair / Home Depot 账号或供应商申请记录？
- 当前主力品类中，哪些是 home improvement / DIY / project-driven，哪些是 home decor / furnishings，哪些是通用 marketplace SKU？
- KES 是否有 US B2C warehouse、Canada fulfillment path、退货地址和客服响应能力？
- 是否已有 GS1 UPC/GTIN、品牌授权、认证、测试报告、安装说明书、质保政策？
- 哪些 SKU 在 Amazon 上已有稳定数据，可作为 Walmart 先导 SKU？
- 哪些 SKU 更适合打磨成 Home Depot merchant proposal？
- Wayfair 需要的图片、属性、场景、变体和合规资料，现有内容系统能否生成？

## Implications

当前优先级建议：
1. Wayfair：先把 3-5 万美元/月收入盘做成可增长、可控利润、可复盘的家居平台经营系统。
2. Home Depot：先把 3-5 万美元/月收入盘做成 project-solution 扩张模型，围绕 DIY / Pro / retail media 提升有效销售。
3. Walmart US：作为冷启动项目，从几百美元/月推进到第一个可判断台阶，优先验证 5-10 个有效 SKU。
4. Walmart Canada：只做合规/结算/进口/退货路径准备，等 Walmart US 出现可复制信号后再规模化。

北美增长平台组 team lead 的核心能力不是单纯广告投放，而是按平台成熟度配置资源：对 Wayfair / Home Depot 做经营质量提升，对 Walmart 做冷启动验证。

## Sources

- Home Depot prospective supplier guidance: https://supplierhub-prospective.homedepot.com/hc/en-us/articles/360034558452-Becoming-a-Supplier
- Home Depot Canada prospective supplier guidance: https://supplierhub-prospective.homedepot.com/hc/en-us/articles/360034559312-Prospective-Canada-Supplier
- Home Depot Supplier Pipeline Program: https://corporate.homedepot.com/page/supplier-pipeline-program
- Home Depot Orange Access / Orange Apron Media announcement: https://corporate.homedepot.com/news/company/orange-apron-media-announces-new-comprehensive-self-service-ad-platform-orange-access
- Home Depot Orange Apron Media 2026 InFronts: https://corporate.homedepot.com/news/company/orange-apron-media-unveils-new-partnerships-infronts-2026
- Orange Apron Media solutions: https://www.orangeapronmedia.com/solutions/
- Wayfair Partner With Us: https://www.aboutwayfair.com/partner-with-us
- Wayfair company facts: https://www.aboutwayfair.com/
- Wayfair Supplier Code of Conduct: https://sell.wayfair.co.uk/wayfair-supplier-code-of-conduct
- Wayfair catalog findability platform: https://www.aboutwayfair.com/careers/tech-blog/barrier-platform-powering-catalog-findability
- Wayfair CastleGate overview: https://sell.wayfair.com/operate-castlegate-overview
- Wayfair / OpenAI catalog and supplier support case study: https://openai.com/index/wayfair/
- Walmart Marketplace overview: https://marketplace.walmart.com/about-walmart-marketplace/
- Walmart Marketplace pricing: https://marketplace.walmart.com/pricing/
- Walmart Listing Quality: https://marketplace.walmart.com/listing-quality/
- Walmart Listing Quality overview: https://marketplacelearn.walmart.com/guides/Listing%20optimization/Items%20and%20inventory/Listing-quality-and-rewards-dashboard
- Walmart Fulfillment Services overview: https://marketplace.walmart.com/walmart-fulfillment-services/
- Walmart Marketplace advertising solutions: https://marketplacelearn.walmart.com/guides/Getting%20started/Advertising/walmart-connect-advertising-solutions-overview
- Walmart US seller performance standards: https://marketplacelearn.walmart.com/guides/Policies%20%26%20standards/Performance/Seller-performance-standards
- Walmart Canada Marketplace: https://www.walmart.ca/en/marketplace
- Walmart Canada seller onboarding and requirements: https://marketplacelearn.walmart.com/ca/guides/Getting%20started/Onboarding/before-you-start-selling-on-walmart-marketplace-canada
