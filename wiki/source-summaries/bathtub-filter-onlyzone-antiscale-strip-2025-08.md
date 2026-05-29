---
type: source-summary
status: draft
owner: strategy
created: 2026-04-20
updated: 2026-04-20
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, supplier-evidence, onlyzone, antiscale, hardness, softening, ceramic-media]
source_type: vendor-material
extraction_mode: structured
review_cycle: one-shot
verification_status: spot-checked
source_count: 5
related:
  - ../products/bathtub-filter/bathtub-filter-point-of-use-hardness-softening-feasibility.md
  - ../products/bathtub-filter/bathtub-filter-kes-media-stack-options-by-water-type.md
  - ../products/bathtub-filter/bathtub-filter-technology-notes.md
  - ../products/bathtub-filter/bathtub-filter-claim-register.md
  - ../products/bathtub-filter/bathtub-filter-evidence-bibliography.md
  - ../../raw/products/bathtub-filter/2026-04-20-onlyzone-antiscale-strip-review.md
---

# 来源摘要｜Onlyzone 宗立阻垢条材料（2025-08 扫描件，2026-04-20 提取）

## Source
- 本地文件：`/Users/kennymak/Downloads/阻垢条_宗立.pdf`
- 原始提取：[2026-04-20-onlyzone-antiscale-strip-review.md](../../raw/products/bathtub-filter/2026-04-20-onlyzone-antiscale-strip-review.md)
- 文件形态：单页扫描 PDF，创建时间 2025-08-06
- 供应商抬头：`ZONE / 宗立科技`

## 这份来源是什么
这是宗立提供的一份 **阻垢条 / antiscale strip** 产品介绍页。它的角色不是 finished-product 证据，而是一个 **供应商材料信号**：宗立除了 KDF55、CaSO3 以外，也在销售一类以“阻垢率”为核心口径的陶瓷介质。

这份材料对 KES 的价值不在于“证明软化成立”，而在于帮助我们把三类常被混淆的路线分开：

1. **去氯 / 氯胺**：处理消毒剂
2. **真软化**：去除 Ca²⁺ / Mg²⁺
3. **阻垢**：减少矿物结垢或改变结垢行为

## 提取出的关键信息

### 1）产品不是树脂，而是陶瓷阻垢介质
- 型号：`ZONE-ZG-A01`
- 材质：`陶瓷`
- 规格：`1.2–1.5 mm`
- 堆积密度：`0.7 g/cm³`

这使它在技术直觉上更接近 **晶体调控 / 表面诱导 / 抑垢型添加介质**，而不是容量型去硬度材料。

### 2）供应商口径是“阻垢率”，不是“硬度去除率”
扫描件的核心文案包括：
- `过水寿命8吨`
- `阻垢率可达85%`
- `本产品适用各类净水滤芯`

测试页两组数据都使用 **自来水硬度 350 ppm** 作为进水条件，但披露的是 **阻垢率** 随通水量衰减，而不是出水硬度下降多少。

### 3）两组供应商测试都没有证明“软化”

#### 4.1 阻垢滤芯测试
- 20 g 介质
- 1.6 L/min
- 350 ppm 硬度自来水
- 20,000 L 时仍报 `88% 阻垢率`

#### 4.2 阻垢花洒测试
- 25 g 介质
- 8 L/min
- 350 ppm 硬度自来水
- 4,000 L 时报 `85% 阻垢率`
- 8,000 L 时报 `74% 阻垢率`

**关键缺口：**
- 没有 Ca²⁺ / Mg²⁺ 去除数据
- 没有硬度 as CaCO3 的前后对比
- 没有 soap-use / lather / conductivity / sodium-exchange 证据

因此它不能被解释成 water softening 证据。

### 4）涉水安全材料只能支持“可接触水”，不能支持功效
扫描件写到符合《生活饮用水输配水设备及防护材料卫生安全评价规范》(2001)，展示的放大框主要是外观、浑浊度、臭和味、肉眼可见物等项目。

这类材料安全信息可以支持：
- 介质可被作为涉水部件的一部分讨论

但不能支持：
- 真软化
- 去氯
- 敏感肌功效
- bathtub finished-product effectiveness

## 与外部证据的合并判断

### 1）官方与工程定义里的“软化”不是这个路线
EPA 对软化的当前公开定义是：**cation exchange** 通过交换去除硬水中的钙镁离子；EPA 的 treatment overview 也把 **cation exchange** 明确列为 water softening route，并把 NF 也列入 hardness removal 方案。

因此，按较稳的工程口径，**真软化需要 Ca/Mg removal**，而不是只给出阻垢率。

### 2）阻垢剂更像 scale-control，而不是 hardness removal
学术与工程文献中，antiscalants 常见机制是：
- sequestration
- crystal modification
- inhibition of precipitation / growth sites

这些机制的共同点是 **延缓或改变结垢行为**，而不是证明 hardness ions 已经被移出水相。

### 3）对 bathtub filter 用户价值不天然成立
即使某种阻垢介质真能降低表面结垢，也还要额外回答三个 bathtub-specific 问题：

1. 益处发生在 **龙头/壳体内部**，还是 **用户整缸浴水体验**？
2. 在 bath-fill 这种 **高总水量、短过水时间** 条件下，它是否值得占用主力去氯媒体体积？
3. 用户会不会把“阻垢”误读成“软化水”？

在 KES 当前产品定义下，这三个问题都偏不利。

## 对 KES 的产品判断

### 可成立的判断
- 宗立这类阻垢条 **可以被视为候选辅助介质信号**
- 它可能适合被研究为：
  - device-internal scale management
  - hard-water narrative adjunct
  - 某些 shower / faucet / appliance route 的防垢补充层

### 不可成立的判断
- 不能把它当成 **softening media**
- 不能据此说 bathtub filter **软化硬水**
- 不能把 `85% 阻垢率` 直接翻译成用户层面的 “water feels soft”

### 当前最稳结论
对 KES bathtub filter 来说，**阻垢条不应被视为核心滤材路线**，更不应被并入“软化水”叙事。

如果未来要试：
- 只能作为 **次级 adjunct layer**
- 只能用 **anti-scale / scale-control** 语言
- 必须先完成 finished-product 级 bath-fill 测试

在 Version A/B/C 当前路线里，它更像 **可选研究项**，不是应进入首发 stack 的主媒体。

## Sources
- Local vendor file: `/Users/kennymak/Downloads/阻垢条_宗立.pdf`
- [US EPA — Cation Exchange Water Softeners](https://www.epa.gov/watersense/cation-exchange-water-softeners)
- [US EPA — Overview of Drinking Water Treatment Technologies](https://www.epa.gov/sdwa/overview-drinking-water-treatment-technologies)
- [US EPA — Why do water systems add phosphate to drinking water?](https://www.epa.gov/lead/why-do-water-systems-add-phosphate-drinking-water-what-are-health-effects-drinking-water)
- [ACS ES&T Water — Simultaneous Use of Polyphosphate for Sequestration and Antiscaling](https://pubs.acs.org/doi/10.1021/acsestwater.3c00553)
