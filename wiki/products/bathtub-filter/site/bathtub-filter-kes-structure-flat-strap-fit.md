---
type: product
status: draft
owner: strategy
created: 2026-07-01
updated: 2026-09-05
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, product-architecture, industrial-design, flat-strap, spout-fit, compatibility]
source_count: 5
review_cycle: monthly
verification_status: partial_sample_validated_test_pending
related:
  - ./bathtub-filter-kes-structure-overview.md
  - ../bathtub-filter-supported-spout-matrix.md
  - ../bathtub-filter-compatibility-engineering-breakpoints.md
  - ../bathtub-filter-kes-flat-strap-spout-fit-design-2026-06-03.md
  - ./bathtub-filter-kes-page-replacement-and-lifespan.md
  - ./bathtub-filter-kes-marketing-site-content-map.md
---

# KES 浴缸过滤器 · 扁硅胶挂带 / 适配（Flat Silicone Strap & Fit）

## 这一页是什么

这是「产品本体」内容簇的适配子页（D4）。它讲 KES 怎么把滤仓**装稳**在浴缸出水嘴上：21mm 宽扁硅胶挂带、多孔调节、中央提拉头挂孔，以及**有边界的兼容矩阵**（S-01~S-08）。

> **承重护栏 + 铁律**：🔴 **禁「通用适配 / 所有浴缸 / universal fit / fits all tubs」**。每一条兼容 claim **必带「不支持」边界**。不支持的 spout 做**诚实劝退**，不硬卖。适配是安装稳定性问题，不代表任何健康结果。

---

## 一、扁硅胶挂带（vs 圆线带）

- **21mm 宽**扁硅胶主挂带；左右各 **4 个长度调节孔**；**中央圆形提拉头挂孔**（拉开后套过提拉分水器的提拉头，形成天然定位点，让滤体中心线对准出水口）。
- **vs 圆线带的稳定性优势**：圆线带与 spout 接触面积小，浴缸高流量注水时水流冲击会放大滤体摇晃；扁带 21mm 宽 → 接触面积更大、摩擦更稳，设计意图是降低高流量下的摆动（[扁挂带适配设计](../bathtub-filter-kes-flat-strap-spout-fit-design-2026-06-03.md)）。
- 无提拉头的直型 spout：配 **3M 贴挂钩** 模拟挂位。
- 弧面 / 异形 spout：配**短硅胶扎带（5 孔、总长 125 mm、宽 20mm）**扎住 3M 贴挂钩；主固定力来自**硅胶扎带的拉力与摩擦力**，3M 胶只作辅助防滑层（🔴 不得写成主要承重 / 长期粘接结构）。

---

## 二、无溢水 envelope

- 顶部 fiber 盘配置下，**35 L/min 内无溢水**（1 mesh + 1~2 非织造 fiber 盘均不溢水；3 盘因流阻过大反而溢水）。美国典型龙头 18–25 L/min，2-盘配置在 no-overflow envelope 内有显著余量（2024-11-07 内部实测，非 V1 滤材条件，作结构 envelope 参考，见 [技术说明](../bathtub-filter-technology-notes.md)）。

---

## 三、墙距边界（居中美观线，不是功能限制线）

横向包络 ~120mm → 居中安装需 60mm 半宽；滤体允许相对出水口偏心约 20mm，因此：

| 出水嘴中心到墙面距离 | 判定 | 说明 |
|---|---|---|
| **≥60mm** | 居中安装最佳 | 外观与对准效果最好 |
| **40–60mm** | 偏心可用 | 功能不受限，但出水不在滤体正中、视觉不完美，需记录偏心量/溅水/绕流 |
| **<40mm** | 理论极端 | 用户观察实际浴缸嘴基本没有少于 40mm；遇到应作异常样本记录，非 V1 常规限制 |

> 60mm 是**居中美观线**，不是「不支持」线。

---

## 四、兼容矩阵 S-01~S-08（已实测标 🟢、未完成动态注水标 🟡）

> **状态口径**：整表当前为 partial-sample validated / broader test-pending。**已有 first-party 正向实测样本的标 🟢（限于已测子集）**；**未完成动态注水测试的标 🟡**。**每条 GO 都带「不支持」边界**。出处：[supported-spout-matrix](../bathtub-filter-supported-spout-matrix.md)、[扁挂带适配设计](../bathtub-filter-kes-flat-strap-spout-fit-design-2026-06-03.md)。

| # | Spout 类型 | 固定方案 | 状态 | 已测边界 / 「不支持」边界 |
|---|---|---|---|---|
| S-01 | Straight non-diverter | 短硅胶扎带 + 3M 贴挂钩模拟挂位 + 21mm 扁带 | 🟢周长边界内已实测 / 🟡动态注水待验 | 末端折弯位置周长 **≤18cm** 已实测可用（常规 15–17cm；125 mm 扎带可拉伸到 22cm）。**不支持**：周长 >22cm 或无稳定贴钩/扎带路径 |
| S-02 | Straight + 提拉分水器 knob | 中央圆孔套过提拉头 + 21mm 扁带 | 🟢2 组 RV/mobile-home 样本已实测 / 🟡广测待验 | 已测 Mobile Home RV center-set faucet、RV valve-diverter faucet。**不支持外推**：不等于所有 RV/center-set/S-02 都已支持；不同提拉头直径待测 |
| S-03 | Curved / gooseneck / freestanding | 3M 贴挂钩 + 短硅胶扎带 + 扁带 | 🟢freestanding 非瀑布 2kg 承重已实测 / 🟡动态注水待验 | freestanding tub filler 弧形/异型管**非瀑布出水**已测 2kg 静态承重；扎带需扎在**距出水嘴末端 60mm**处。**不支持**：waterfall / 宽体片状出水 |
| S-04 | Short-projection（近墙） | S-01/S-02 方案 + 偏心 | 🟡偏心待验 | 墙距 ≥60mm 居中 / 40–60mm 偏心可用。**不支持**：需先确认偏心量/溅水/手部空间/视觉接受度 |
| S-05 | Wide-body decorative | 贴挂钩不保证居中 | 🔴默认不支持 / 🟡个案 | **不支持**（默认）：宽体表面让贴钩、挂带路径、居中不可控；未单独实测通过前 V1 不承诺 |
| S-06 | Slip-fit + 可见晃动 | 挂带无法消除 spout 本体晃动 | 🔴不支持 | **不支持**：即使挂住，spout base wobble 会放大滤体摆动、触发漏水/绕流/脱落 |
| S-07 | Threaded + 出水口不一 | 按外形套 S-01/S-02/S-03 | 🟡按子类型待验 | threaded base 更稳是正向因素，但仍取决于是否有提拉头、出水口截面。**不支持**：不得单写成 universal fit |
| S-08 | Low-clearance / off-center | 允许偏心约 20mm | 🟡偏心待验 | 40–60mm 偏心可用（美观折中）。**不支持**：<40mm 仅作理论极端 |

**诚实劝退（对不支持的 spout 明说）**，客户可见英文（对照 supported-spout-matrix 结语，去掉 "fits most tubs"）：

> `Designed for standard tub spouts with pull-up diverters, stable non-diverter spouts when the terminal bend circumference is 18 cm or less, and curved / special-shaped freestanding tub fillers with non-waterfall outlets when secured about 60 mm from the outlet end using the included 3M hook and silicone tie. Close-to-wall spouts can be used off-center when the outlet center is about 40–60 mm from the wall (appearance may be less centered). Not designed for loose / wobbly slip-fit spouts or waterfall / wide-body decorative outlets unless fit-confirmed.`

---

## claim / 证据状态表

| claim | 状态 | 出处 | 护栏 |
|---|---|---|---|
| 21mm 扁硅胶挂带，左右各 4 调节孔，中央提拉头挂孔 | 🟢 | [扁挂带适配设计](../bathtub-filter-kes-flat-strap-spout-fit-design-2026-06-03.md) | — |
| 扁带接触面积大于圆线带，设计上更抗摇晃 | 🟢结构判断 | 同上 | 设计意图，非「不摇晃」保证 |
| S-01 周长 ≤18cm 已实测可用 | 🟢（子集） | supported-spout-matrix | 必带「>22cm 不支持」边界 |
| S-02 RV/center-set/valve-diverter 2 组样本已实测 | 🟢（子集） | 扁挂带适配设计 2026-06-17 | 🔴 不外推为「所有 RV/S-02 支持」 |
| S-03 freestanding 非瀑布 2kg 承重已实测 | 🟢（子集） | 扁挂带适配设计 2026-06-17 | 必带「waterfall/宽体不支持」边界 |
| S-05 wide-body / S-06 wobble | 🔴不支持 | supported-spout-matrix | 诚实劝退，不硬卖 |
| S-04/S-07/S-08 动态注水稳定性 | 🟡待验 | supported-spout-matrix | 未完成动态注水前标黄 |
| 无溢水 35 L/min envelope | 🟡 待 V1 复测 | 2024-11-07 内部实测（204 g KDF + 45 g 炭，非 V1 滤材） | 对外只写设计目标 ≤30 L/min |
| 通用适配 / fits all tubs | 🔴禁 | claim-register Banned 区 | 每条兼容 claim 必带「不支持」边界 |

---

## 承重护栏（必带）

> 🔴 **绝不写「通用适配 / 所有浴缸 / universal fit / fits all」**。KES 讲的是**有边界的适配**：明确支持哪些 spout、在什么条件下、并让用户**买前就能自我识别不支持的配置**。适配是安装稳定性问题，与去氯效能、健康结果无关。3M 胶只作辅助防滑，🔴 不得写成主要承重结构。

---

## 相关页链接

- [D1 · 结构总览](./bathtub-filter-kes-structure-overview.md)
- [支持的龙头兼容矩阵（真理源）](../bathtub-filter-supported-spout-matrix.md)
- [兼容性工程断点（backflow/AVB/leak taxonomy）](../bathtub-filter-compatibility-engineering-breakpoints.md)
- [扁硅胶挂带适配方案 2026-06-03](../bathtub-filter-kes-flat-strap-spout-fit-design-2026-06-03.md)
- [T3 · 更换 / 寿命](./bathtub-filter-kes-page-replacement-and-lifespan.md)
- [内容地图（父）](./bathtub-filter-kes-marketing-site-content-map.md)

## Sources

- [扁硅胶挂带适配方案 2026-06-03（尺寸/适配/墙距实测）](../bathtub-filter-kes-flat-strap-spout-fit-design-2026-06-03.md)
- [支持的龙头兼容矩阵 S-01~S-08](../bathtub-filter-supported-spout-matrix.md)
- [兼容性工程断点](../bathtub-filter-compatibility-engineering-breakpoints.md)
- [技术说明（无溢水 envelope）](../bathtub-filter-technology-notes.md)
- [宣称台账（Fit/compatibility + Universal-fit Banned）](../bathtub-filter-claim-register.md)

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-kes-structure-overview]]
- [[bathtub-filter-supported-spout-matrix]]
- [[bathtub-filter-compatibility-engineering-breakpoints]]
- [[bathtub-filter-kes-flat-strap-spout-fit-design-2026-06-03]]
- [[bathtub-filter-kes-page-replacement-and-lifespan]]
- [[bathtub-filter-kes-marketing-site-content-map]]
