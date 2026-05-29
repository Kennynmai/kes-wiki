---
type: product
status: draft
owner: strategy
created: 2026-04-19
updated: 2026-04-19
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, compliance, us, california, prop65, warnings, marketplaces]
source_count: 12
review_cycle: monthly
verification_status: spot-checked
related:
  - ./bathtub-filter.md
  - ./bathtub-filter-us-state-federal-compliance-sidelines.md
  - ./bathtub-filter-compliance-framework-and-evidence-boundaries.md
  - ./bathtub-filter-certification-authority-tiers-and-workflow.md
  - ./bathtub-filter-claim-risk-audit-v2.md
---
# 浴缸过滤器 California Prop 65 调查与应对

## 为什么单独成页
`Prop 65` 在 KES 的美国上市路径里不是泛合规背景，而是一个单独的运营门槛：

- 它影响包装、网页、Amazon / marketplace 上架字段、客服话术与州内销售策略
- 它和 `NSF/ANSI/CAN 372`、材料合规声明、supplier certificate 不是一回事
- 它有明显的 private enforcement 机制，出错成本往往先表现为律师函、和解、下架，而不是监管机构预沟通

这页的目标不是给法律定性，而是把 KES 当前最需要的 `调查路径 + 决策口径 + 执行动作` 放到一个独立工作面。

## 一句话判断
截至 `2026-04-19`，对 bathtub filter 这类含金属件、塑料件、密封件、可能含软管的消费品，**KES 不应把 Prop 65 当作“拿到某个材料证书就自动完成”的事项**。  
在缺少整机级化学成分与暴露评估之前，**最稳妥的运营默认应是：要么暂不卖加州，要么按 Prop 65 warning 路径准备包装与线上告知。**

## 一、当前监管快照
### 1.1 基本机制
根据加州 OEHHA 与 `Proposition 65 Warnings` 官方说明，企业在明知并故意导致加州居民接触清单化学物质时，需要提供 `clear and reasonable warning`，除非能证明暴露低于 safe harbor。

- 癌症端阈值是 `NSRL`（No Significant Risk Level）
- 生殖/发育毒性端阈值是 `MADL`（Maximum Allowable Dose Level）
- “没有警示”的举证负担实际上在企业一侧

### 1.2 两个必须记住的时间点
- `2025-01-01`：OEHHA 新版 short-form warning 规则生效
- `2028-01-01`：旧短版 “Cancer and Reproductive Harm” 文案退出过渡；对 `2028-01-01` 及之后制造并贴标的产品，短版 warning 需要写出至少一个化学品名

这意味着：KES 如果现在就做美国 SKU，不应再按“旧短版长期可用”的假设设计包装。

### 1.3 当前清单状态
OEHHA Proposition 65 首页显示，当前清单日期为 `2025-12-08`。  
这说明 list 本身仍在变动，化学品筛查不能只做一次后永久冻结。

## 二、哪些情况必须有 Prop 65 警示
### 2.1 法律上的严格答案
严格按法规说，并不是“某个品类天然必须有 warning”，而是满足下面这组条件时必须有：

1. 产品、包装、票据、标签、使用过程或经营场景会让加州个人接触到 `Prop 65` 清单化学物质
2. 该接触是企业“knowingly and intentionally”导致的，例如销售、分销、交付、张贴、提供使用环境
3. 企业不能证明暴露低于相应 `safe harbor`  
   癌症端看 `NSRL`，生殖/发育毒性端看 `MADL`
4. 该化学品已过 `12` 个月 warning 生效期

换句话说，**真正触发“必须 warning”的不是品类名，而是“有 listed chemical exposure，且你拿不出低暴露证明”。**

### 2.2 行业实务上的答案
行业里真正的操作逻辑更直接：

- 如果企业知道产品里有高频目标化学物，且没有完整 exposure defense，通常就会把 warning 视为“必须”
- 如果产品卖到加州电商，warning 不仅要出现在实物/包装上，还要在下单完成前出现在网页或明确链接上
- 如果上游给不出稳定、可追溯、可复核的材料与测试文件，进口商/品牌方往往直接按 warning 路线处理
- 如果已经有同类产品的大量 `60-day notice`、settlement、平台字段要求或零售商采购要求，实务上也接近“必须”

所以对运营团队来说，应该区分两个概念：

- **法律上的 must**：无法证明低于 safe harbor 时必须 warning
- **商业上的 effectively must**：即使理论上可争辩，实际也不值得裸奔

## 三、行业实际常见的“几乎等同必须 warning”的场景
### 3.1 产品里有高频执法化学物，且没有 exposure defense
这是最常见场景。典型组合包括：

- `lead` in brass / plated metal / solder / ceramic coating
- `DEHP` 等 phthalates in PVC / soft plastic / bag / hose / seal
- `BPS` in thermal receipt paper / packing slip / shipping label

行业里只要碰到这些高频对象，而企业又没有一套能扛住质疑的测试与暴露论证，通常就直接给 warning，或者先改配方/改材料。

### 3.2 卖到加州，而且是互联网/目录销售
这是容易被低估的一类。官方 FAQ 明确要求：

- 产品 warning 之外，互联网购买也要有 warning
- warning 必须在用户完成购买前可见
- 不能把 warning 藏成需要用户自己主动寻找的内容
- `QR code` 这类需要用户自己额外扫码寻找的方式，不属于 safe harbor 的自动呈现

因此，**凡是卖加州的 Amazon、Shopify、catalog、分销 feed，只要底层产品需要 warning，线上展示面也几乎必做。**

### 3.3 进口商 / private label / distributor 自己不知道最终成分
行业里非常常见：supplier 说“compliant”，但不给到足够细的 `BOM + material declaration + test basis + change control`。  
这时法律责任并不会因为“是供应商生产的”就消失。官方 FAQ 也明确把 warning 主责任放在 manufacturer / importer / supplier / distributor 这一链条上。

实务结果通常只有三种：

1. 补文件并补测试
2. 先给 warning
3. 不卖加州

### 3.4 同类品类已经被集中执法
一旦某类化学物+品类组合已经进入高频 notice / settlement 区，行业实践会迅速转向保守。

官方与公开案例能看到几种典型模式：

- 黄铜/含铅金属件：如门钥匙中的 lead 暴露，历史上已触发和解与降铅要求
- 软塑料/包袋：`DEHP` notice 与 settlement 很常见，很多结果都是“重配方或 warning 二选一”
- 热敏纸：`BPS` 自 `2024-12` 起进入 warning 语境后，收据、packing slip、shipping label 已出现专门 warning 场景
- 食品/补剂/海鲜：只要 heavy metal 暴露过阈值，公开 enforcement 也很活跃

这类场景下，企业即便还没收到 notice，也往往会把 warning 当默认防线。

### 3.5 零售平台或大客户把它当入场条件
很多品牌不是先被法院逼着做，而是先被渠道逼着做。

常见场景：
- Amazon / marketplace 有 `Prop 65` 属性、合规字段或内容审核
- 零售商/分销商要求供应商提供 warning language 或 Prop 65 representation
- 客服/票据/packing slip 需要同步 warning 逻辑

这类情况下，哪怕法律上还在分析 exposure，商业上也已经接近“必须”。

### 3.6 多语言 consumer information 已经存在
如果产品标签、网站或相关 consumer information 使用了英语以外语言，官方 FAQ 说明 warning 也要以相应语言提供。  
这意味着不是只有“要不要 warning”的问题，还有“要不要多语言 warning”的问题。

## 四、对 bathtub filter 最有现实意义的 must-warning 场景
把上面的通用逻辑压缩到 bathtub filter，最接近“必须 warning”的实际情形是：

### 4.1 含黄铜 / 金属接液件，且无可辩护的 lead 暴露论证
这类情形在用水 hardware 里最现实。  
只要有 brass fitting、接头、阀件、焊点，且没有完整的 lead exposure assessment，运营上通常应视为 warning-ready。

### 4.2 含软管 / 软 PVC / 柔性密封件，且未排清 phthalates
bathtub filter 若带软连接件、软胶圈、柔性 hose，这类部件天然落在 phthalates 高关注区。  
如果没有明确材料替代或测试闭环，实务上也很难主张“肯定无需 warning”。

### 4.3 加州线上销售已开启，但 PDP / listing 没有 warning
若产品已判定或高概率需要 warning，那么：

- Amazon PDP
- Shopify product page
- 第三方零售 product page
- catalog / line sheet

都应在购买完成前把 warning 呈现出来。  
行业里这不是“可选优化”，而是明显的执行缺口。

### 4.4 使用热敏纸 packing slip / receipt，且企业已判断存在 BPS 暴露
这不是 bathtub filter 本体问题，但它是真实的订单履约副线。  
如果出货链路涉及热敏纸，且企业判断会造成 `BPS` 暴露，warning 可能出现在票据/packing slip，而不是产品本体。

### 4.5 无法及时完成测试，但仍准备卖加州
这基本是最现实的管理判断：

- 你要卖加州
- 你知道部件里大概率有高风险化学物
- 你来不及证明低于 safe harbor

那实务上就不该继续把“无 warning”当默认。

## 五、对 bathtub filter 最相关的暴露假设
下面是基于 bathtub filter 典型 BOM 的**工作假设**，不是对 KES 现品的法律结论：

| 暴露对象 | 为什么 relevant | bathtub filter 里的常见风险点 | 当前判断 |
|---|---|---|---|
| Lead | Prop 65 高频执法对象 | 黄铜接头、焊点、金属电镀件、来料波动 | 高优先级排查 |
| DEHP / DBP / BBP / DIDP 等 phthalates | 软 PVC / 软胶件常见 | 软管、密封圈、gasket、柔性连接件 | 高优先级排查 |
| BPA / BPS 类双酚 | 塑料与热敏纸场景常见 | 部分塑料件；另外票据/packing slip 是独立副线 | 中优先级排查 |
| Nickel | 某些金属件会碰到 | 不锈钢件、镀层件、金属 fitting | 中优先级排查 |
| Carbon black / silica / process residue | 更偏制造与粉尘场景 | 介质粉尘、填料、加工残留 | 低到中优先级，按材料决定 |

这里最重要的不是把化学品名单写长，而是先把**哪些部件最可能触发 warning**钉住。对 bathtub filter，优先级通常不是滤材理论性能，而是 `金属接液件 + 软胶/软管 + 任何可迁移的添加剂`。

## 六、KES 现在最需要回答的四个问题
### 3.1 我们是否会卖到加州
如果 KES 的美国电商/marketplace 不排除加州地址，就不能把 Prop 65 当作“以后再看”的问题。

### 3.2 我们是否真的知道成分
若现阶段只有 supplier 口头承诺、`SDS`、或泛化的 `compliance certificate`，通常还不足以支撑 “no warning required”。

### 3.3 我们准备走哪种 warning 路线
对当前阶段的 KES，运营上至少要在以下两条里选一条：

1. `California-holdout`：美国卖，但不卖加州
2. `Warning-ready`：允许卖加州，并准备包装/页面/渠道 warning

第三条“证明无需 warning”路线不是不能走，但前提是测试与暴露论证已经先完成，而不是把它当默认前提。

### 3.4 我们的 warning 是否覆盖线上交易
官方 FAQ 明确把互联网销售纳入 safe harbor warning transmission 规则；warning 需要在消费者完成购买前被清楚看到。  
对 KES 来说，这直接影响 Amazon、Shopify PDP、catalog、第三方分销商 feed。

## 七、建议的 KES 应对策略
### 4.1 建议默认路线：`Warning-ready`
若 KES 仍把美国作为候选市场，我建议当前默认按 `Warning-ready` 路线推进，而不是先赌 “肯定不需要 warning”。

原因：
- bathtub filter 的部件构成天然落在 `lead + phthalates` 高风险区
- 线上销售 warning 是独立执行面，晚补会拖慢上架
- `2025-01-01` 规则已更新，现在做包材和 PDP，直接按新规则准备更干净

### 4.2 只有在以下条件同时满足时，才考虑走 `No-warning` 路线
- BOM 已锁定到具体材质、供应商、牌号、颜色与工艺
- 对高风险部件完成第三方测试或可辩护的 exposure assessment
- 法务/外部顾问明确接受该结论
- 渠道 side 也接受不加 warning 的口径

### 4.3 若资源不足，次优路线是 `California-holdout`
如果短期内还不能完成测试与标签准备，**不要在美国开放加州地址同时继续裸奔销售**。  
运营上更可控的方式是：

- 暂不开放加州配送
- 先把其余州销售路径跑通
- 把 Prop 65 作为美国上市前 gating item，而不是售后补洞项

## 八、具体调查清单
### 5.1 BOM / 来料层
- 拉出整机 `BOM`，不是只看滤材
- 给每个接液件、金属件、软胶件、包装件编号
- 向 supplier 索要 `SDS`、材质声明、restricted substance 声明、Prop 65 声明、变更通知机制
- 明确哪些部件是 brass、PVC、TPR、silicone、ABS、PP、POM、epoxy、涂层件

### 5.2 测试层
- 先测高风险部件，不要平均发力
- Lead / heavy metals：针对金属接液件与可迁移路径
- Phthalates：针对 hose / seal / gasket / flexible polymer parts
- 必要时做整机视角的 migration / exposure assessment，而不是只做材料含量

### 5.3 文案与包装层
- 包装 warning、说明书 warning、产品页 warning、Amazon 字段要统一
- 新做包材时，优先按 `2025-01-01` 生效后的规则准备
- 不要把 `lead-free`、`NSF 372`、`BPA free` 误写成 “因此不需要 Prop 65”

### 5.4 渠道层
- Amazon：确认是否需要 `Prop 65` 属性/字段、图片或 PDP 告知
- Shopify / DTC：warning 要在完成购买前可见，而不是藏在 FAQ / terms
- 分销：若由他方零售，warning notice 与材料传递责任要可留痕

## 九、执行版响应方案
### 6.1 7 天内
- 决定美国 SKU 是否包含加州
- 形成 `Prop 65 risk BOM` 一页表
- 对高风险部件发 supplier 资料清单
- 确定包装是否预留 warning 区域

### 6.2 14 天内
- 收齐主要高风险部件材质文件
- 决定先测哪些件，哪些先按 warning 路线兜底
- 产出 KES 内部 `California sell / no-sell` 暂行口径
- 整理 Amazon / DTC warning placement 草案

### 6.3 30 天内
- 完成第一轮测试或外部顾问 review
- 确认最终是 `No-warning`、`Warning-ready`，还是 `California-holdout`
- 把结论写回包装、listing、客服 FAQ、分销通知模板

## 十、建议的内部决策口径
### 7.1 可以直接采用的工作口径
- `Prop 65` 是美国上市门槛，不是后补文案项
- `NSF/ANSI/CAN 372`、supplier certificate、材料合规，不自动等于 `Prop 65 complete`
- 没有完成成分/暴露判断前，不默认认为 “无需 warning”
- 卖加州就必须同时考虑包装 warning 与线上 warning

### 7.2 现阶段不建议采用的口径
- “supplier 说没问题，所以我们先不上 warning”
- “有 lead-free / BPA-free 说法，所以整个产品没 Prop 65 风险”
- “先上 Amazon，后面有人找再补”

## 十一、对现有 bathtub filter 项目的直接含义
基于当前 wiki 里已有信息，KES 已经对 `claims discipline`、`FDA/CPSC/FTC` 边界做了不少收敛，但 `Prop 65` 还缺三块真正决定能否上市的执行物：

1. 整机级 `risk BOM`
2. marketplace / DTC warning placement 方案
3. `California sell / no-sell` 的运营决策

因此，当前更准确的状态不是“已经研究过 Prop 65”，而是“已经识别出 Prop 65 是门槛，但尚未完成可执行闭环”。

## 十二、KES 当前建议
如果这条线要继续推进美国市场，我建议把下面这句话视为当前工作结论：

> 在 `2026-04-19` 这个时间点，KES 对 bathtub filter 的 California Prop 65 最稳妥应对，不是先争辩要不要 warning，而是先把 `risk BOM + warning-ready packaging/PDP + California go/no-go` 三件事做完。

## Obsidian links
- [[bathtub-filter]]
- [[bathtub-filter-us-state-federal-compliance-sidelines]]
- [[bathtub-filter-compliance-framework-and-evidence-boundaries]]
- [[bathtub-filter-certification-authority-tiers-and-workflow]]
- [[bathtub-filter-claim-risk-audit-v2]]
- [[bathtub-filter-test-gating-checklist-for-kes]]

## Sources
- OEHHA Proposition 65 overview / current list date: <https://oehha.ca.gov/proposition-65?page=1>
- OEHHA Proposition 65 law and regulations: <https://oehha.ca.gov/proposition-65/law/proposition-65-law-and-regulations>
- OEHHA warning rule update approved `2024-11-26`, effective `2025-01-01`: <https://oehha.ca.gov/proposition-65/crnr/proposition-65-clear-and-reasonable-warnings-safe-harbor-methods-and-content>
- OEHHA plain-language explanation of `NSRL` / `MADL` and burden logic: <https://oehha.ca.gov/proposition-65/general-info/proposition-65-plain-language>
- Proposition 65 Warnings site business FAQ: <https://www.p65warnings.ca.gov/business-resources/frequently-asked-questions-businesses>
- Proposition 65 Warnings sample consumer-product warnings: <https://www.p65warnings.ca.gov/node/1058>
- Proposition 65 Warnings FAQ on when a warning is required: <https://www.p65warnings.ca.gov/faq/businesses/how-can-businesses-determine-if-warning-required>
- Proposition 65 Warnings FAQ on BPS in receipts / packing slips / shipping labels: <https://www.p65warnings.ca.gov/faq/consumers/why-am-i-receiving-warning-bisphenol-s-bps-labels-and-packing-slips>
- California Attorney General enforcement reporting / 60-day notice process: <https://oag.ca.gov/prop65>
- California AG Prop 65 enforcement overview and example case patterns: <https://oag.ca.gov/environment/prop65>
- California AG door key lead settlement example: <https://oag.ca.gov/news/press-releases/major-manufacturers-agree-reduce-amount-lead-door-keys-under-settlement>
- California AG example DEHP settlement requiring reformulation or compliant warning: <https://oag.ca.gov/prop65/60-day-notice-2019-00665>
