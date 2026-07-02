---
type: product
status: draft
owner: product
created: 2026-04-19
updated: 2026-06-30
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, hard-water, softening, ion-exchange, hardness, resin, antiscale, scale-inhibitor, tds, evidence]
source_count: 8
review_cycle: monthly
verification_status: spot-checked
related:
  - ./bathtub-filter-technology-notes.md
  - ./bathtub-filter-water-source-types-guide.md
  - ./bathtub-filter-evidence-matrix.md
  - ./bathtub-filter-claim-register.md
  - ./bathtub-filter-kes-product-architecture-hypotheses.md
---

# 浴缸过滤器就地软水可行性

## 为什么有这页
现有 wiki 已经反复提示“不要轻易说 softens hard water”，但还缺一个更工程化的回答：

> **如果接受更高换芯频率，浴缸端 point-of-use 软水到底能不能做？**

本页只回答“真实去除硬度（Ca²⁺ / Mg²⁺）”这件事，不讨论“water feels softer”这类感受性语言。

---

## 一句话结论

**可以，但只有离子交换树脂这一路线是 point-of-use 真软化的可信方案；代价是体积大、容量消耗快、通常必须可再生。**

更具体地说：

- **KDF、活性炭、亚硫酸钙、维生素 C、矿化球、陶瓷球**都不是“软化硬水”的有效滤材
- **离子交换阳树脂（sodium-cycle cation exchange resin）**可以真实去除硬度
- 如果做成**一次性小滤芯**，在浴缸每次 80–150 L 的用水量下，容量会消耗得非常快
- 因此可行形态更像**小型可再生 softener / 外挂 canister**，而不是常见 compact bath-ball

---

## 1. 什么算“有效软水”

对 bathtub filter 来说，只有下列两类路线算“真实软化”：

1. **离子交换**：用 Na⁺ 或 H⁺ 交换 Ca²⁺ / Mg²⁺
2. **膜法**：RO / NF 直接去除溶解盐

在浴缸末端场景里：

- **RO / NF** 需要高压、排浓水、体积大，不适合挂在 tub spout
- 所以 **真正可讨论的 point-of-use 软化路线，基本只剩离子交换**

---

## 2. 唯一可信滤材：离子交换树脂

### 原理

强酸性阳离子交换树脂在钠型（Na-form）状态下，会把水里的 Ca²⁺ / Mg²⁺ 换成 Na⁺：

- 2R-Na + Ca²⁺ → R₂-Ca + 2Na⁺
- 2R-Na + Mg²⁺ → R₂-Mg + 2Na⁺

这是真正的硬度去除，不是体感修饰。

### 为什么别的滤材不算软化

- **活性炭**：主要处理氯、异味、有机物，不去除溶解硬度
- **KDF**：主要是氧化还原与部分重金属逻辑，不是 Ca/Mg 容量型捕获
- **亚硫酸钙 / 维生素 C**：是去消毒剂路线，不是去硬度路线
- **矿化球 / 碱性球 / 陶瓷球**：常常反而改变 TDS 或增加矿物，不能当作软化

---

## 3. 容量估算：为什么小滤芯很快就会耗尽

### 可引用的树脂容量基线

- ResinTech 住宅软化树脂 `CGS` 的 **total exchange capacity = 1.9 meq/mL**
- Purolite 说明：**operating capacity 往往只有 theoretical capacity 的 50–60%**

把 1.9 meq/mL 换算成 CaCO₃ 硬度当量：

- 1 meq hardness = **50 mg/L as CaCO₃**
- 1.9 meq/mL ≈ **95 mg CaCO₃ / mL resin**（理论上限）
- 按 50–60% 的可运行容量， practical capacity ≈ **48–57 mg CaCO₃ / mL resin**

### 按一缸浴水来算

| 场景 | 水量 | 硬度 | 总硬度负荷 | 需要树脂体积（按 48–57 mg/mL practical） |
|---|---|---:|---:|---:|
| 中等硬水小浴缸 | 80 L | 150 mg/L as CaCO₃ | 12,000 mg | **210–250 mL** |
| 硬水标准浴缸 | 100 L | 250 mg/L as CaCO₃ | 25,000 mg | **440–520 mL** |
| 很硬水大浴缸 | 150 L | 250 mg/L as CaCO₃ | 37,500 mg | **660–780 mL** |
| 很硬水大浴缸 | 150 L | 400 mg/L as CaCO₃ | 60,000 mg | **1.05–1.25 L** |

### 这意味着什么

**推论：**

- 如果目标是“接近真正软水”，一个仅有 **50–150 mL** 树脂的小挂件通常只够处理 **不到一缸到半缸** 的硬水
- 即使用户接受“高换芯频率”，想做成 **每 1–3 次泡澡换一芯**，树脂床也通常要来到 **数百 mL** 量级
- 想把更换节奏做到可接受，实际上就会逼近 **0.5–1.5 L 树脂** 的小型 softener 体量

这已经不是“装一点滤材顺手改善”了，而是一个真正的小型软水设备

---

## 4. 工程边界：可做，但不适合一次性 compact bath filter

### 4a. 最可能成立的形态

如果 KES 真要做 bathtub 端软化，最可信的是：

- **可再生离子交换树脂**
- **独立 canister / mini tank**
- **明确的再生流程**（盐水再生）
- **明确的容量口径**（按 CaCO₃ mg/L × gallons / baths）

它更像“bathroom point-of-use softener”，而不是传统 bathtub filter。

### 4b. 一次性替换型能不能做

**可以做，但商业上很吃力。**

只有在以下条件下，替换型才可能勉强成立：

- 面向 **中低硬度** 区域
- 用户接受 **极高换芯频率**
- 宣称只做 **partial softening / hardness reduction**，而不是“turns hard water into soft water”
- 树脂量至少来到 **数百 mL**

如果只有几十克或一小撮 mixed media，基本不可信。

---

## 5. 还有两个经常被忽略的现实问题

### 氯会伤树脂寿命

ResinTech 对住宅软化树脂的应用说明明确写到：

- 这类树脂用于 **“waters that do not contain significant chlorine residual”**

对 bathtub 场景的含义：

- 在市政供水里直接做软化，**前面最好先有去氯层**
- 否则树脂寿命会被氯 / 氯胺加速损耗

这使得“氯胺城市 + 软化”尤其麻烦，因为前处理本身就更难。

### 可再生几乎是必需的

树脂耗尽后，不是简单“洗一洗”就恢复，而是要用盐水再生。

这意味着真正可用的浴室端软水方案通常需要：

- 盐盒 / 再生液
- 排放管理
- 用户操作教育

如果完全没有再生环节，就只能接受“容量很快烧完”的事实。

---

## 5.5 阻垢剂 / 阻垢条为什么不等于软化

2026-04-20 新增了一份宗立的阻垢条扫描件（见 [Onlyzone 宗立阻垢条材料](../../source-summaries/bathtub-filter-onlyzone-antiscale-strip-2025-08.md)），很适合作为一个边界澄清案例。

### 它是什么

这份材料描述的是：

- **陶瓷阻垢条**
- 宣称口径是 **阻垢率**
- 适合加到各类净水滤芯里

它的测试条件包括：

- 350 ppm 硬度自来水
- 20–25 g 添加量
- 1.6 L/min 或 8 L/min
- 输出的是 **74–100% 阻垢率**

### 它没有证明什么

这类报告**没有给出**：

- 出水硬度下降多少
- Ca²⁺ / Mg²⁺ 去除多少
- 是否发生 Na⁺/K⁺ 交换
- 是否把 hard water 变成 soft water

所以它只能说明：

- 可能**减少结垢**
- 或改变矿物析出/沉积行为

但**不能说明“真实软化”成立**。

### 为什么工程上要分开

按 EPA 对 drinking-water treatment 的公开定义，**真正软化**主要是：

- **cation exchange** 去除 Ca/Mg
- 或 **NF/RO** 这类膜法降低 hardness

阻垢剂常见逻辑则是：

- sequestration
- threshold inhibition
- crystal modification

这些路线的目标是 **减少 scale deposition**，不是证明 hardness ions 已离开水相。

### 对 bathtub filter 的实际含义

对 bathtub filter 来说，把阻垢剂加进滤芯，并不会自动回答用户最关心的问题：

- 泡澡水是不是**真的更软**
- 起泡性/皂感是不是接近软水
- 硬度数字是不是明显下降

如果这些问题答不上来，就不应把阻垢条当成 softening media。

### 补充：这款阻垢料的「涉水卫生安全报告」（2026-06-30 登记）

上面的阻垢**条**（1.2–1.5mm，阻垢率）与阻垢**颗粒**（0.5–5mm）经供应商确认**是同一款料**的不同粒径档。颗粒档另有一份第三方检测报告（青岛环湾 CMA，青环检字 CP210620，2021-07-01；原件见 [2026-06-30 宗立阻垢颗粒涉水检测报告](../../../raw/products/bathtub-filter/2026-06-30-zongli-antiscale-granule-hygiene-report.md)）。要点：

- **性质是卫生安全，不是功效**：23 项涉水析出全部合格（重金属、酚、消毒副产物均 < 检出限），只证明材料**接触饮用水安全**。
- **TDS 增量仅 +5–6 mg/L**（220 → 225/226），再次印证阻垢材料**几乎不动 TDS/硬度**——TDS 笔测不出变化是正常的，恰证「没在软化」。
- **合规红线**：报告说明第 8 条明写「**不得用于各类广告宣传**」，且系自送样仅对来样负责——只能作内部供应商合规存档，不得进任何营销语境。

**证据配对现状（同一款料）**：这款料现有第三方**安全**背书（颗粒报告 ✅）+ 供应商自测**阻垢率**（条 ~85%）。比"各缺一半"强，但**两份都没测硬度**——「泡澡水会不会真变软」答案不变：**不会**（与同料无关，纯因无人测 Ca/Mg）。另注：阻垢率测的是 1.2–1.5mm 档、安全测的是 0.5–5mm 档，粒径影响接触动力学，效能须按实际出货粒径复核；阻垢率亦为供应商自测、非第三方。

---

## 6. 对 KES 的产品判断

### 可成立的判断

- **“有没有有效滤材可以软化？”**
  - 有：**离子交换树脂**
- **“能不能接受更高换芯频率来换取软化？”**
  - 能，但会很快走向 **大体积、高耗材成本、最好可再生** 的设备逻辑

### 不成立的判断

- 用 KDF / 炭 / 亚硫酸钙 / 维生素 C 做“软化”
- 用阻垢剂 / 阻垢条 / antiscale ceramic media 做“软化”
- 用少量 mixed media 做“true hard-water softening”
- 把整户软水器（SOFTER trial 那类）证据外推到紧凑 bathtub filter

### KES 当前最稳的结论

对 KES 来说，**“去氯 / 氯胺”与“真软化”应视为两条不同 SKU 路线**：

- **Route A：bath filter**
  - 解决游离氯 / 氯胺 / 气味 / bath comfort
- **Route B：bathroom POU softener**
  - 用离子交换树脂解决硬度

如果未来想探索 **Route C：anti-scale adjunct**，也应单独命名为阻垢/防垢路线，而不是软化路线。

把两条路线硬塞进一个小型一次性 bathtub filter，工程和商业压力都会很大。

---

## 7. 推荐的 claim boundary

### 可以说

- "uses ion-exchange resin to reduce hardness minerals"
- "partial hardness reduction"（如果容量和测试只支持部分去除）
- "best suited to low-to-moderate hardness water and higher refill frequency"

### 不应直接说

- "softens hard water"（除非有 finished-product 测试证明到接近软水）
- "anti-scale media softens water"
- "works like a whole-house softener"
- "supports eczema prevention"（SOFTER 证据不能外推）

---

## 8. 技术路线对照表（软化 / 阻垢 / 过滤）

前面几节把三条路线的边界分散讲了，这里把它们并排放，**严格按 problem → product → claim 三层拆开**，方便做 SKU 决策和 copy 审查时直接查。

### 8a. 一句话区分

- **软化**：把 Ca²⁺ / Mg²⁺ **从水里拿走** → 硬度真下降
- **阻垢**：钙镁**留在水里**，只是不让它结垢/挂垢 → 硬度基本不变
- **过滤**：处理的是**别的东西**（消毒剂、异味、有机物、部分重金属、颗粒），**不碰硬度**

三者解决的是三个不同 problem，任何一条都不能替另一条背书。

### 8b. 对照表

| 维度 | 软化（离子交换） | 阻垢（防垢） | 过滤（除消毒剂/杂质/重金属） |
|---|---|---|---|
| **解决的 problem** | 硬水本身（起皮、皂感差、真实硬度高） | 结垢 / 挂垢 / 水渍白斑 | 游离氯·氯胺、异味、部分重金属、颗粒物 |
| **作用机理** | Na 型强酸阳树脂 2R-Na + Ca²⁺ → R₂-Ca + 2Na⁺，真实去除 | 阈值效应 + 晶格畸变 + 分散 + 螯合，抑制结晶与附着 | 吸附（活性炭/ACF）、氧化还原（KDF）、化学还原（亚硫酸钙/维C） |
| **常见 media** | 离子交换树脂 | 聚磷酸盐晶球（Siliphos）、有机膦酸、陶瓷阻垢条 | GAC / 炭块 / ACF、KDF-55/85、亚硫酸钙、维C |
| **硬度变化** | ↓ 真下降 | ≈ 不变 | ≈ 不变 |
| **TDS 变化** | ↓（钙镁换成钠，略降或持平） | ≈ 不变 | ≈ 不变（可能因 media 溶出略动） |
| **可行 product 形态** | 数百 mL–1.5 L 树脂、最好可再生 canister（不是 compact bath-ball） | 微量晶球可塞进滤芯，属**消耗型添加层** | compact bath-ball / spout 滤芯的主力路线 |
| **可以 claim** | "ion-exchange resin to reduce hardness minerals"、"partial hardness reduction" | "抑制水垢生成 / 减少水垢附着 / anti-scale" | "reduces free chlorine / chloramine / odor"（按 finished-product 测试口径） |
| **不能 claim** | "softens hard water"（除非成品测试到接近软水）；"works like whole-house softener" | "软化水质 / softens water"；"降低硬度"；"除已生成的老垢" | 任何"软化""降硬度""除垢"表述 |
| **本页对应** | §2 / §3 / §6 Route B | §5.5 / §6 Route C | §6 Route A（详见 [[bathtub-filter-technology-notes]]） |

### 8c. 阻垢机理补充（为什么"阻垢 ≠ 软化"在化学上成立）

阻垢剂靠**亚化学计量**起效——用远少于钙镁等比例的量就能防垢，因为它并不"锁走"钙镁，而是干预结晶过程：

1. **阈值效应**：吸附在晶核上阻止其长大，让过饱和水保持稳定（聚磷酸盐、有机膦酸主打）
2. **晶格畸变**：把致密硬垢搅成松散、易冲走的形态
3. **分散作用**：给微粒带同种电荷，静电排斥使其悬浮不沉积（聚羧酸主打）
4. **螯合**：把 Ca/Mg 络合成可溶物，但等比例消耗、只作辅助

关键推论：以上四条**没有一条会让 Ca²⁺/Mg²⁺ 离开水相**，所以出水硬度和 TDS 基本不变。用 TDS 笔测阻垢滤芯前后读数几乎不变是**正常现象**，不代表无效——它证明的恰恰是"没在软化"。这也是为什么宗立那份阻垢条报告只给"阻垢率"、给不出"硬度下降值"（见 §5.5）。

### 8d. 对 KES 的直接含义

- 三条路线 = 三个 problem = **三种独立 claim**，不可混用背书
- V1 bath filter 的主力仍是**过滤路线**（去氯/氯胺/comfort）；阻垢晶球最多作为**防垢附加层**、且只能挂"anti-scale"口径的 claim；真软化必须走独立 SKU（Route B）
- Copy 审查红线：任何把阻垢层或过滤层说成"软化/降硬度"的表述，直接判不合规

---

## Sources

- [ResinTech CGS — residential softening resin, total exchange capacity 1.9 meq/mL](https://www.resintech.com/product/cgs/)
- [Purolite / Ecolab — Ion Exchange Resin Characteristics (operating capacity typically 50–60% of theoretical)](https://www.purolite.com/index/core-technologies/industry/food-and-beverage/sweetener-applications/corn-sweetener-refining-with-ion-exchange-resins/ion-exchange-resin-characteristics)
- [LANXESS Lewatit S 1567 — drinking-water softening resin](https://lanxess.com/en-us/products/products/l/lewatit--s-1567)
- [SOFTER pilot RCT note in bibliography](./bathtub-filter-evidence-bibliography.md)
- [Bathtub filter evidence matrix](./bathtub-filter-evidence-matrix.md)
- [Water source types guide](./bathtub-filter-water-source-types-guide.md)
- [KES product architecture hypotheses](./bathtub-filter-kes-product-architecture-hypotheses.md)
