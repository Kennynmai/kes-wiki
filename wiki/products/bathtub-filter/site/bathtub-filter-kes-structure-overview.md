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
domains: [bathtub-filter, kes, product-architecture, industrial-design, structure, specs]
source_count: 6
review_cycle: monthly
verification_status: spot-checked
related:
  - ./bathtub-filter-kes-structure-flow-diversion-module.md
  - ./bathtub-filter-kes-structure-transparent-housing.md
  - ./bathtub-filter-kes-structure-flat-strap-fit.md
  - ./bathtub-filter-kes-structure-ip-and-patent-governance.md
  - ./bathtub-filter-kes-page-replacement-and-lifespan.md
  - ./bathtub-filter-kes-scenario-free-chlorine.md
  - ./bathtub-filter-kes-marketing-site-content-map.md
  - ../bathtub-filter-kes-v1-selling-points-and-pack-contents.md
  - ../bathtub-filter-technology-notes.md
---

# KES 浴缸过滤器 · 结构总览（Structure Overview）

## 这一页是什么

这是「产品本体 / 工业设计」内容簇的**总入口页（D1）**。上层内容地图（[内容地图](./bathtub-filter-kes-marketing-site-content-map.md)）此前覆盖了滤材（M 页）、场景（S 页）、方法信任（T 页），但缺了「产品长什么样、为什么这么设计」这一层。本页补齐产品本体总览，并把三个创新点分别导航到子页：

- **D2 导流模块 / 防沟槽** → [结构·导流模块](./bathtub-filter-kes-structure-flow-diversion-module.md)
- **D3 透明滤仓** → [结构·透明滤仓](./bathtub-filter-kes-structure-transparent-housing.md)
- **D4 扁硅胶挂带 / 适配** → [结构·扁挂带适配](./bathtub-filter-kes-structure-flat-strap-fit.md)

本页只做总览与规格收编，不重复子页正文。规格数字口径以真理源页为准（去氯数字→[更换/寿命页 T3](./bathtub-filter-kes-page-replacement-and-lifespan.md) 与 T2；结构/IP claim→[IP 治理页](./bathtub-filter-kes-structure-ip-and-patent-governance.md)）。

> **承重护栏（本页每次出现结构叙事都随行）**：这不是净水器，不以降低 TDS 为目标。它是浴缸注水场景的**末端除游离氯模块**，主 KPI 是游离氯去除。结构设计讲的是「水怎么走、料怎么放、怎么装稳」，不代表任何健康疗效。

---

## 一、三条设计原则

### 1. Metal-first（料级诚实，不是廉价填充）

高品质铜锌合金（KDF55）与亚硫酸钙（CaSO₃）是真实可见的料，不是藏在不透明塑料后面的廉价填充。**这是料级 / 质感叙事，不是健康声称**——不得译成「去重金属保护皮肤」（无经皮证据，见 [claim-register](../bathtub-filter-claim-register.md) 与 [IP 治理页](./bathtub-filter-kes-structure-ip-and-patent-governance.md)）。

- 客户可见英文：`Premium copper-zinc alloy media you can see — not the cheap filler hiding behind opaque plastic.`

### 2. 透明可视（Clean is what you can see）

透明硬壳滤仓让用户看到真实的料名、料量、顺序。**可见是 trust 钩子，不等于「更有效」**；efficacy 另由去氯实测支撑（详见 [D3 透明滤仓](./bathtub-filter-kes-structure-transparent-housing.md)）。

### 3. 分层不混（Layered, not mixed）

（2026-07-02 按 [V1 BOM 表](../bathtub-filter-v1-free-chlorine-removal-dimensions-materials.md) 裁定更正：克数互换、滤棉 PET、O 圈 NBR、浴盐仓 250 mL）

沿水流方向严格分层：**过滤棉（PET）→ KDF55（130g）→ CaSO₃（110g）**，不是 mixed-bead / bath-ball 黑箱。分层的工程理由是防 channeling、防介质互扰、可分段更换、失效可诊断（详见 [D2 导流模块](./bathtub-filter-kes-structure-flow-diversion-module.md)）。

---

## 二、结构分解图（占位）

已有原始爆炸图（见下）。🟡 **待补**的是**带层序标注的正式版**（把 过滤棉（PET）→ KDF55 → CaSO₃ → 导流模块 → 浴盐腔逐层标注 + 尺寸引线），以及结构分解渲染。补正式版前，本页用下方原始爆炸图 + 文字描述结构层序。

![[raw/products/bathtub-filter/2026-06-18-desktop-source-folder-import/source-files/爆炸图.png]]

> 原始件：`raw/products/bathtub-filter/2026-06-18-desktop-source-folder-import/source-files/爆炸图.png`（KES 内部产品讲解原件附带）。

沿水流方向（自上而下）：

```
浴缸龙头出水
   │
[ 防溢接水仓（含主挂带、宽入口、顶部 overflow trough）]
   │  ← 内置导流模块（把水流铺开，防 CaSO₃ 层中心冲蚀）
[ 过滤棉（PET）物理前置层（拦截可见颗粒/沉积） ]
   │
[ KDF55 滤料仓 130g（末端安全层 + 生物膜抑制层 + 寿命稳定层） ]
   │
[ CaSO₃ 滤料仓 110g（主力去游离氯 KPI） ]
   │
[ 整流浴盐仓（1 cup / 250mL，底层高流速冲散） ]
   │
进入浴缸
```

料量与分工出处：[V1 卖点与套装内容](../bathtub-filter-kes-v1-selling-points-and-pack-contents.md)、[技术说明](../bathtub-filter-technology-notes.md)。

---

## 三、规格表（收编视觉稿 Technical Details）

| 项 | 规格 | 状态 | 口径 / 出处 |
|---|---|---|---|
| 主 KPI | 游离氯去除（free chlorine），非总氯/氯胺/TDS/软化 | 🟢 | [S1 场景页](./bathtub-filter-kes-scenario-free-chlorine.md)、claim-register |
| 性能流量口径 | 15 L/min bath-fill 为性能口径 | 🟢结构 / 数字🟡 | 去氯数字待 Gate 1 DPD；口径见 T3/T2 |
| 最大通过流量 | up to 25 L/min 作**最大通过流量**，非性能承诺流量 | 🟡 | 25 L/min 数字未坐实不上首屏（[T3](./bathtub-filter-kes-page-replacement-and-lifespan.md)、内容地图 T2 行） |
| 无溢水 envelope | **两个口径并存勿混**：V1 设计防溢目标 **≤30 L/min**（讲解件 §3.11，P2 #1 同口径）；**35 L/min** 为结构包络上限（2024-11-07 内部实测，非 V1 滤材条件）——35 对 30 有余量，二者不矛盾 | 🟢结构 | [技术说明](../bathtub-filter-technology-notes.md)；对外表面用 ≤30 设计目标口径 |
| 横向包络尺寸 | ~120mm | 🟢 | [扁挂带适配设计](../bathtub-filter-kes-flat-strap-spout-fit-design-2026-06-03.md)、[supported-spout-matrix](../bathtub-filter-supported-spout-matrix.md) |
| 滤材栈 | 过滤棉（PET）→ KDF55 130g → CaSO₃ 110g（分层不混） | 🟢 | [V1 BOM 表](../bathtub-filter-v1-free-chlorine-removal-dimensions-materials.md)、[V1 卖点页](../bathtub-filter-kes-v1-selling-points-and-pack-contents.md) |
| 安装 | 免工具安装（tool-free），扁硅胶主挂带 + 3M 贴挂钩 + 短硅胶扎带 | 🟢结构 | [D4 扁挂带适配](./bathtub-filter-kes-structure-flat-strap-fit.md) |
| 更换 / 寿命 | 按 baths/gallons 表达，分段衰减曲线（99%→95%→90%→80%→<50%），非「月」 | 🟢 | 唯一口径见 [T3 更换/寿命页](./bathtub-filter-kes-page-replacement-and-lifespan.md)，本页不改写 |
| 固定 / 接口方式 | **无螺纹接口**——直接**挂在龙头出水嘴下方**：21mm 扁硅胶主挂带 + 中央提拉头挂孔；无提拉头用 3M 贴挂钩 + 短硅胶扎带 | 🟢结构 | 非 inline 螺纹件（**无 NPT/IPS**）；固定方式与兼容边界见 [D4](./bathtub-filter-kes-structure-flat-strap-fit.md)、[supported-spout-matrix](../bathtub-filter-supported-spout-matrix.md) |
| 部件材质 | **27 部件全 BOM 已入库（2026-07-02）**：滤料仓外壳 = Eastman Tritan TX1001（透明）Ø120×35mm 壁厚 1.5mm；防溢仓/浴盐仓 = ABS；溶解孔板 = PC；滤网 = 304 不锈钢；挂带/调节筋 = 硅胶；挂钩 = ABS；滤棉 = 聚酯纤维（PET）；O 圈 = 丁腈（NBR） | 🟢 BOM 已定 / ✅ 4 分歧已裁定（2026-07-02）/ 🟡 O 圈线径 | 唯一口径源 = [V1 尺寸与材质表](../bathtub-filter-v1-free-chlorine-removal-dimensions-materials.md)。✅ 原 4 处分歧（KDF/CaSO₃ 克数互换、PET vs PP 滤棉、丁腈 vs 硅胶 O 圈、250 vs 240ml）**已裁定全部按 BOM 表为准**，本页与营销页已更正，见该页 §7 |
| 成品认证 | KDF55 有供应商 NSF/ANSI 42 **料级** listing；**成品未 NSF 认证** | 🟢 | 每处随「成品未认证」免责，见 claim-register |
| 浴盐腔体 | 底层 1 cup / 250mL 装载腔，15–30 L/min 高流速冲散 | 🟢结构 | [V1 BOM 表](../bathtub-filter-v1-free-chlorine-removal-dimensions-materials.md)、[V1 卖点页](../bathtub-filter-kes-v1-selling-points-and-pack-contents.md) |

---

## 四、创新点导览（各链到 D2/D3/D4）

| 创新点 | 一句话 | 子页 |
|---|---|---|
| 导流模块 / 防沟槽 ★最核心差异 | **两级防沟流结构**（2026-07-02 按 BOM 对齐）：KDF 仓入口 Ø50mm 导流锥管「进水铺开」+ CaSO₃ 仓 6 分区管「主力层不塌」——CaSO₃ 层怕沟流是测试结论，两级结构是生产实现 | [D2 §一A →](./bathtub-filter-kes-structure-flow-diversion-module.md) |
| 透明滤仓 | clean-honest 的物理实现；料可见、可替换 | [D3 →](./bathtub-filter-kes-structure-transparent-housing.md) |
| 扁硅胶挂带 / 适配 | 21mm 宽带 + 多孔调节 + 中央提拉头挂孔；比圆线带更抗摇晃 | [D4 →](./bathtub-filter-kes-structure-flat-strap-fit.md) |
| 回洗自清洁 / 再生 **（升级款可选）** | 回洗口 + 1/4 转拆芯 → 反冲 10 L/min×15s → 复位，全程 ≤30s；专利实施例显示可恢复压降与去氯性能（数字 🟡 待第三方） | [专利参考页 §二/§四 →](../bathtub-filter-kes-patent-19-281644-modular-terminal-water-treatment.md)｜维护步骤见 [P3 §二A](./bathtub-filter-kes-care-and-maintenance-guide.md) |

> **回洗（backflush）是什么**：处理模块带可选**回洗口**（专利 Fig.1 元件 107 + claim 16），把自来水**反向**通过滤床，冲出截留的细粉/沉积——是「换滤料」之外的第二种维护手段。**基础款不带回洗**（靠换滤料维护）；升级款可选。专利实施例（内部口径，🟡 非第三方）：3200L≈80 缸后回洗，ΔP 9.4→4.8 kPa（恢复 ~49%）、去氯 86%→>92%；20 循环 / 累计 64,000L 无壳裂、O 圈老化 ≤5%。**这些数字不上对外页**，待第三方复测（归 [T2/Gate 1](./bathtub-filter-kes-page-how-we-test-and-certify.md) 口径纪律）。

---

## claim / 证据状态表

| claim | 状态 | 出处 | 护栏 |
|---|---|---|---|
| 分层不混结构 过滤棉（PET）→KDF55 130g→CaSO₃ 110g | 🟢 | [V1 BOM 表](../bathtub-filter-v1-free-chlorine-removal-dimensions-materials.md)、[V1 卖点页](../bathtub-filter-kes-v1-selling-points-and-pack-contents.md) | 料级/工程叙事；不译成健康结果 |
| 内置导流模块（CaSO₃ 层 operational requirement） | 🟢 | 2025-10-22 内部测试（[技术说明](../bathtub-filter-technology-notes.md)） | 讲机理，不作疗效背书 |
| 横向包络 ~120mm、免工具安装 | 🟢结构 | 扁挂带适配设计 | 兼容 claim 必带「不支持」边界（见 D4） |
| 无溢水 35 L/min envelope | 🟡 待 V1 复测 | 2024-11-07 内部实测（204 g KDF + 45 g 炭 + 两层纤维盘，非 V1 滤材） | 对外只写设计目标 ≤30 L/min；35 数字 V1 复测前不上表面 |
| 15 L/min 性能 / up to 25 L/min 最大通过 | 🟢结构 / 数字🟡 | T2/T3 | 25 L/min 去氯数字未坐实不上首屏 |
| `Patent pending`（U.S. App. 19/281,644，申请日 2025-07-26） | 🟢 可用 | [专利参考页](../bathtub-filter-kes-patent-19-281644-modular-terminal-water-treatment.md)、[IP 治理页](./bathtub-filter-kes-structure-ip-and-patent-governance.md) | 现可对外写 "Patent pending"（有申请号背书）。🔴 仍禁 patented / granted / 专利技术（是 pending 非授权） |
| 固定方式 = 挂在出水口下（非螺纹接口） | 🟢结构 | [D4](./bathtub-filter-kes-structure-flat-strap-fit.md)、[supported-spout-matrix](../bathtub-filter-supported-spout-matrix.md) | 无 NPT/IPS；每条兼容 claim 必带「不支持」边界 |
| 部件材质：外壳 PP/PC(Tritan)/PPSU 2mm FDA §177、密封丁腈（NBR）O 圈（生产 BOM 裁定；专利说明书列硅胶为示例材料） | 🟢 外壳/密封已定（O 圈线径 🟡 待工程） | [V1 BOM 表](../bathtub-filter-v1-free-chlorine-removal-dimensions-materials.md)、[专利参考页 §材质](../bathtub-filter-kes-patent-19-281644-modular-terminal-water-treatment.md) | 挂带以硅胶为准（旧 TPU 待更正）；金属/涂层件对照 BOM 做 Prop65 排查 |
| 回洗自清洁 / 再生（**升级款可选**，基础款靠换滤料） | 🟢结构 / **数字🟡 待第三方** | [专利参考页 §二/§四 Embodiment 6](../bathtub-filter-kes-patent-19-281644-modular-terminal-water-treatment.md)（专利实施例：ΔP 恢复 ~49%、去氯 86%→>92%、64,000L 耐久） | 数字为**专利实施例（内部口径）**，不上对外页；对外只可讲「支持回洗自清洁（升级款）」结构事实；性能数字归 T2/Gate 1 纪律 |

---

## 承重护栏（必带）

> **This is not a water purifier. It does not target TDS reduction.** 它是浴缸注水场景的末端除游离氯模块，主 KPI 是**游离氯**去除。看得见的料是 trust 钩子，不等于更有效——efficacy 由去氯实测支撑。任何结构叙事都不得暗示治疗皮肤 / 健康结果。

---

## 相关页链接

- [D2 · 导流模块 / 防沟槽](./bathtub-filter-kes-structure-flow-diversion-module.md)
- [D3 · 透明滤仓](./bathtub-filter-kes-structure-transparent-housing.md)
- [D4 · 扁硅胶挂带 / 适配](./bathtub-filter-kes-structure-flat-strap-fit.md)
- [IP 与专利治理（内部）](./bathtub-filter-kes-structure-ip-and-patent-governance.md)
- [T3 · 更换 / 寿命](./bathtub-filter-kes-page-replacement-and-lifespan.md)
- [S1 · 游离氯场景（场景入口）](./bathtub-filter-kes-scenario-free-chlorine.md)
- [内容地图（父）](./bathtub-filter-kes-marketing-site-content-map.md)

## Sources

- [KES V1 卖点与套装内容](../bathtub-filter-kes-v1-selling-points-and-pack-contents.md)
- [技术说明（导流必要性 / 无溢水 envelope / 媒体分工）](../bathtub-filter-technology-notes.md)
- [扁硅胶挂带适配方案 2026-06-03](../bathtub-filter-kes-flat-strap-spout-fit-design-2026-06-03.md)
- [支持的龙头兼容矩阵](../bathtub-filter-supported-spout-matrix.md)
- [宣称台账（护栏总表）](../bathtub-filter-claim-register.md)
- [内容地图（真理源规则 §四）](./bathtub-filter-kes-marketing-site-content-map.md)

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-kes-structure-flow-diversion-module]]
- [[bathtub-filter-kes-structure-transparent-housing]]
- [[bathtub-filter-kes-structure-flat-strap-fit]]
- [[bathtub-filter-kes-structure-ip-and-patent-governance]]
- [[bathtub-filter-kes-page-replacement-and-lifespan]]
- [[bathtub-filter-kes-scenario-free-chlorine]]
- [[bathtub-filter-kes-marketing-site-content-map]]
- [[bathtub-filter-kes-v1-selling-points-and-pack-contents]]
- [[bathtub-filter-technology-notes]]
