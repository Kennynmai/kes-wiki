---
type: product
status: draft
owner: strategy
created: 2026-07-02
updated: 2026-09-05
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, ifu, manual, print, instructions, packaging, review-prevention, channel-spec, ch2]
review_cycle: monthly
related:
  - ./bathtub-filter-kes-care-and-maintenance-guide.md
  - ./bathtub-filter-kes-install-and-compatibility-guide.md
  - ./bathtub-filter-kes-packaging-design-spec.md
  - ./bathtub-filter-kes-pack-contents-spec.md
  - ./bathtub-filter-kes-page-replacement-and-lifespan.md
  - ./bathtub-filter-kes-page-water-test-diagnosis.md
  - ../bathtub-filter-claim-register.md
  - ../bathtub-filter-marketplace-negative-review-signals.md
  - ./bathtub-filter-kes-marketing-site-content-map.md
---

# CH2 · 印刷版说明书（Print IFU）规格

## 这一页是什么

**盒内印刷说明书（IFU, Instructions For Use）的版式与内容规格。** [P3 维护指南](./bathtub-filter-kes-care-and-maintenance-guide.md) 与 [P4 安装指南](./bathtub-filter-kes-install-and-compatibility-guide.md) 是**网页版**真理源；本页定义它们如何压缩成一份**印刷品**——折页形态、图文比例、内容清单、印刷规格、QR 策略。

**为什么单独立页**：竞品第一差评源之一就是**说明书难懂 / 缺失 / 配件不知何用**（[negative-review-signals](../bathtub-filter-marketplace-negative-review-signals.md) 适配失败簇 + [P5 §七 #2](./bathtub-filter-kes-packaging-design-spec.md) Canopy 案例 `RCU05OFYRKX5G`）。一份图优先、口径正确的 IFU 是**防差评资产**，不是合规附件。

**内容纪律**：本页**只做版式与选取，不新造任何口径**——每段内容都引用既有页；数字（寿命/流速/去氯）一律以 T3/T2 为源。印刷英文文案保留英文。

---

## 一、形态与语言

| 项 | 规格 | 说明 |
|---|---|---|
| 折页形态 | `[____ 待设计]`（建议方向：单张大折页（如 6 面风琴折）优于骑马钉小册——展开即全流程可视，符合「图优先」） | 与 P5 §二 L2 层位配合：说明书在主机之前到手 |
| 语言 | **EN 主**；ES 可选 `[____ 待市场决策]`（若加西语：同版面双语会挤压图优先原则，建议独立 ES 面或独立张） | 美国市场；西语人口占比高的零售渠道再评估 |
| **图优先原则（承重）** | **每步一图，文字 ≤2 行**；图能说清的不写字；文字只做动作指令（imperative），不做解释——解释全部走 QR 到网页版 | 直接反制「说明书难懂」差评：读图不读段落 |
| 视觉基线 | 实拍或线稿示意，与实物一致；🔴 不用与实物有出入的渲染图（P5 §一同款纪律） | 图-实物不符 = 信任崩塌 |

---

## 二、内容清单（六段，全部引用既有页）

> 每段标注：内容源（唯一口径）→ 印刷取用范围。**IFU 不得包含任何未在源页出现的数字或 claim。**

### ① 快速开始（3 步装机）

- 源：[P4 安装指南 §二](./bathtub-filter-kes-install-and-compatibility-guide.md) 三条安装路线。
- 取用：**三路线各一图**（A 提拉头套孔 / B 直嘴 + 3M 挂钩 / C 弧形 + 硅胶扎带），每图配 ≤2 行动作指令 + 一行边界小字（如路线 C："Strap ~60 mm from the spout tip."）。
- 配件逐件配图说用途（3M 挂钩 / 短硅胶带 / 挂带——数量规格引 [P2](./bathtub-filter-kes-pack-contents-spec.md)），反制「配件不知何用」差评。
- 🔴 不印 universal fit；印一行："Not for loose/wobbly spouts or wide waterfall spouts — check the fit guide [QR]."

### ② 首次使用 = 先测水

- 源：[T1 自测诊断页](./bathtub-filter-kes-page-water-test-diagnosis.md) + [买后验证流程](./bathtub-filter-kes-post-purchase-verification.md)；与 P5 §二 L1 层序（试纸物理上在主机前）互锁。
- 取用：试纸用法三图（接一杯龙头水 → 浸纸 → 对色卡读数），印：
  > `Test your tap water BEFORE installing — that's your "before" number.`
- 读色说明 + 一行精度句："A quick guide, not a lab test."
- 🔴 不印 TDS 笔；🔴 读数只对「水的类型/浓度」，不作健康解读（禁 toxin-panic）。

### ③ 维护（排水 / 晾干 / 清洁）

- 源：[P3 §一–§三](./bathtub-filter-kes-care-and-maintenance-guide.md)。
- 取用：排水晾干三步各一图 + 印刷句（P3 已定稿 EN）：
  > `After each fill, remove the cartridge, drain it, and let it air-dry. Do not store it wet.`
- 清洁表压缩为「外壳冲洗 / 滤棉直接换 / 滤仓外部冲洗不拆料」三行。
- 基础款不印回洗段（P3 §二A 仅升级款；若 SKU 含回洗口，另开版位 `[____ 按 SKU 定]`）。

### ④ 更换（T3 触发口径）

- 源：[T3 更换与寿命页](./bathtub-filter-kes-page-replacement-and-lifespan.md)（唯一数字源）。
- 取用：滤棉「变色即换」一图；滤仓更换印：
  > `Replace when your after-filter strip starts showing chlorine again — the first color step above zero. At 2 ppm tap free chlorine and about 3 baths/week that is typically around 100–120 baths; your local tap chlorine changes this, so trust the strip, not the calendar.`
- 🔴 **baths/gallons 口径，不换算成月**（register 包装/说明书行）；2026-09-05 起以试纸触发为主句，baths 只作"typically around"参照。

### ⑤ 排查（P3 五支排查树精简版）

- 源：[P3 §五](./bathtub-filter-kes-care-and-maintenance-guide.md) 症状 A–E。
- 取用：压缩为**一张五行表**（症状 → 一句处理 → 详见 QR），每行 ≤2 行文字：

| 症状（EN 印刷） | 一句处理 |
|---|---|
| Fiber disc turns dark | `That's the filter working — swap in a fresh disc (20 included).` |
| Water spills from the top | `Slow the fill. Check the strap and cup are seated.` |
| Slips off the spout | `Re-strap ~60 mm from the tip; some spouts aren't supported — see fit guide [QR].` |
| Can't smell a difference | `Don't trust your nose — test before/after with the strip.` |
| Musty smell / slime | `Drain, air-dry, replace the disc. Don't store it wet.` |

- 「变黑 = 在工作」定调照 P3 症状 A（把损耗讲成证据）；「测不出差别 → 用试纸」照 P3 症状 D（46.5% 最高杀伤投诉的第一道印刷防线）。

### ⑥ 安全与合规脚注

- 源：[claim-register](../bathtub-filter-claim-register.md) + [P5 §三 合规印刷清单](./bathtub-filter-kes-packaging-design-spec.md)（与包装同源同口径，一字不差）。
- 必印（承重，编辑/设计不得为版面删除）：
  - **定位承重句**：`This is not a water purifier. It does not target TDS reduction.`
  - **NSF 口径（二选一，与盒面同步）**：完整料级句含 `The finished product is not itself NSF-certified.`——或完全不出现 NSF 字样。
  - **Prop 65 位**：`[____ 待法务]`（warning 文字直接印刷，🔴 不得只靠 QR 呈现——P5 §三 #5）。
  - 阻垢仓若在 IFU 提及：`It does not soften your water.` 随行。
  - 防倒吸使用提示（P4 §五）：出水端保持在水面以上，不接软管/喷头。
  - 废滤料处置一句 `[____ 待合规确认]`（P5 §六 #5 同源）。
- 🔴 全文禁：eczema / baby-safe / chloramine 认领 / universal fit / 杀菌（柱内抑膜不得写成消毒）。

---

## 三、印刷规格

| 项 | 规格 | 负责 |
|---|---|---|
| 纸张 / 克重 / 涂布 | `[____ 待供应链]`（浴室场景建议考虑耐潮涂布） | 供应链 |
| 成品/展开尺寸 | `[____ 待设计]`（须适配 P5 §二 L2 层位与盒内尺寸） | 设计 + 供应链 |
| 正文字号 | `[____ 待设计]`；**建议最小 8pt**（合规脚注亦不小于此，防「小字免责」观感与可读性投诉） | 设计 |
| 色彩 | 试纸读色相关图（②⑤）如含色阶参考，**油墨须与试纸色卡打样比色一致** `[____ 待打样]`（同 SVC8 §4.7.1 工艺要求） | 设计 + 供应链 |
| 版式走查 | 每步一图 / 文字 ≤2 行逐版检查；六段全部有图 | 设计 + 产品 |

---

## 四、QR 策略（对齐 P5 §五：一码多锚，不多码）

- **IFU 上只用主 QR**（与盒面正面**同一个码**）：落地 Start-here 页（以 [P4 网页版](./bathtub-filter-kes-install-and-compatibility-guide.md) 为主体，首屏含水型确认入口 → T1 ZIP 诊断）。
- IFU 内不同段落引导到**同一落地页的不同锚点**（安装视频 / fit guide / 排查详版 / 换芯页）——一码多锚。
- 🔴 IFU 不出现第二个码（分享卡码只在 L3 卡上；Prop 65 不得以 QR 替代印刷）。

---

## 五、护栏总表（IFU 级）

| 规则 | 等级 |
|---|---|
| 内容全部引用既有页（P3/P4/T1/T3/P2/register），不新造口径与数字 | 🔴 承重 |
| 每步一图、文字 ≤2 行；解释走 QR 不走印刷 | 🟢 原则 |
| baths/gallons 不换算成月 | 🔴 |
| "not a water purifier" 承重句 + 成品未 NSF 句（如提 NSF）必印 | 🔴 |
| Prop 65 直接印刷、不藏 QR；措辞待法务 | 🔴 |
| 试纸验证、禁 TDS 笔；读数不作健康解读 | 🔴 |
| 禁 eczema / baby-safe / chloramine / universal fit / 杀菌 / 软化 | 🔴 |
| 与包装（P5 §三）合规清单同源同口径，一字不差 | 🔴 |
| ship 前全文逐条过 register §D「包装/说明书」行签署 | 🔴 |

### `[____]` 待补清单

| 项 | 负责 |
|---|---|
| 折页形态 / 尺寸 / 版式稿 `[____]` | 设计 |
| ES 西语版决策 `[____]` | 市场 |
| 纸张 / 涂布 / 色阶打样 `[____]` | 供应链 |
| Prop 65 措辞 `[____]` | 法务 |
| 废滤料处置措辞 `[____]` | 合规 |
| 升级款（回洗口）SKU 是否单开版位 `[____]` | 产品 |
| 全文逐条 register 签署 | 法务 + 市场 |

---

## Sources / 内部依据

- [P3 使用与维护指南（网页版真理源：晾干/清洁/排查树）](./bathtub-filter-kes-care-and-maintenance-guide.md)
- [P4 安装与兼容性指南（网页版真理源：三路线/矩阵/防倒吸）](./bathtub-filter-kes-install-and-compatibility-guide.md)
- [P5 包装设计 spec（层序 L2 / 合规印刷清单 / QR 一码多锚）](./bathtub-filter-kes-packaging-design-spec.md)
- [P2 套装内容规格（配件数量唯一口径）](./bathtub-filter-kes-pack-contents-spec.md)
- [T3 更换与寿命页（数字唯一口径）](./bathtub-filter-kes-page-replacement-and-lifespan.md)
- [T1 水质自测/诊断页（试纸口径）](./bathtub-filter-kes-page-water-test-diagnosis.md)
- [claim-register §D 包装/说明书行](../bathtub-filter-claim-register.md)
- [市场负面评论信号（说明书难懂 = 差评源）](../bathtub-filter-marketplace-negative-review-signals.md)

## Obsidian links

- [[bathtub-filter-kes-marketing-site-content-map]]
- [[bathtub-filter-kes-care-and-maintenance-guide]]
- [[bathtub-filter-kes-install-and-compatibility-guide]]
- [[bathtub-filter-kes-packaging-design-spec]]
- [[bathtub-filter-kes-pack-contents-spec]]
- [[bathtub-filter-kes-page-replacement-and-lifespan]]
- [[bathtub-filter-kes-page-water-test-diagnosis]]
- [[bathtub-filter-kes-post-purchase-verification]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-marketplace-negative-review-signals]]
- [[bathtub-filter-supported-spout-matrix]]
- [[bathtub-filter]]
