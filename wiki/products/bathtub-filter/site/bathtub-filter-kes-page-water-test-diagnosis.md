---
type: product
status: draft
owner: strategy
created: 2026-06-30
updated: 2026-06-30
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, self-diagnosis, test-strip, ccr, zip-lookup, water-type, acquisition]
source_count: 5
review_cycle: monthly
verification_status: spot-checked
related:
  - ./bathtub-filter-kes-marketing-site-content-map.md
  - ../bathtub-filter-claim-register.md
  - ../bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md
  - ./bathtub-filter-kes-page-how-we-test-and-certify.md
  - ../bathtub-filter-kes-media-stack-options-by-water-type.md
---

# T1 · Test Your Water（水质自测 / 试纸页）

## 这一页是什么

这是 KES 自有站的**方法/信任页**，教用户在下单前**先搞清自己家的水是什么类型**，好选对滤材组合、别买错。

> 定位口径：**ZIP → 水务 CCR 查询 = 消毒剂类型的权威判定；多垫试纸 = 浓度/硬度的粗筛。** 类型判定始终以 ZIP/CCR 为准，试纸只作交叉验证与浓度分档。这一页是 register「Self-diagnosis」Allowed 行 + [获客引擎 §二/§八](../bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md) 的对外表面。
>
> 认证/去氯数字口径不在本页定义——引用 [T2 我们怎么测/认证页](./bathtub-filter-kes-page-how-we-test-and-certify.md)。

**承重钩子（照 register 原文保留英文）：**

> "Find out what's in your water — so you pick the right media. **A quick guide, not a lab test.**"

---

## 一、两条路径（按认知负担分层）

照 [获客引擎 §三](../bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md)，给两条路，用户自选深度，默认推路径 A 降摩擦。

### 路径 A — 快速（30 秒，多数市政用户够用）

**只输 ZIP** → 立即得：消毒剂类型（权威）+ 基线硬度 + 推荐主配方。

> 对游离氯城市的大多数人，这一步就够给出「游离氯版 + 是否加阻垢」的可靠建议，**不需要任何试纸**。

### 路径 B — 深度（想确认 / 复杂水 / 井水）

**ZIP + 多垫试纸 + 观察指引** → 确认类型、量化浓度档、抓硬度/铁/沉积/氯胺 flag → 完整组合处方。井水、老房子、想精挑、或 ZIP 数据异常时走这条。

---

## 二、工具 × 参数 × 置信（诚实边界写死在页面上）

照 [获客引擎 §二](../bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md) 的判断矩阵。**每个判断都明说「有多确定」，绝不让粗筛冒充实验室。**

| 要判断的 | 最该用的工具 | 置信 | 诚实边界 |
|---|---|---|---|
| **消毒剂类型（游离氯 / 氯胺）** | **ZIP → 水务 CCR 查询** | 🟢 高（权威） | 类型的权威判定 |
| 类型的**家庭自测交叉验证** | 试纸**游离氯 + 总氯**双垫 | 🟡 中 | **总氯 − 游离氯 = 结合氯（氯胺）**；总氯≫游离氯 → 很可能氯胺。**减法放大误差，只作 flag，类型仍以 ZIP 为准** |
| 游离氯**浓度** | 游离氯试纸垫 | 🟡 中 | 粗筛档位足够（决定去氯负荷/寿命） |
| **硬度** | 试纸色块分档；要数字→滴定小瓶 | 🟡 中 | 给软/中/硬/极硬档；CCR 有基线硬度可交叉 |
| **铁** | 试纸（粗）+ 锈染观察 | 🟠 中低 | 低浓度试纸不稳，锈黄染色更可靠 |
| **硫化氢 / 硫味** | 气味指引（臭鸡蛋味） | 🟠 症状 | 嗅觉信号，无试纸 |
| **沉积物 / 浊度** | 肉眼清澈度 | 🟠 症状 | 看得见的颗粒不需仪器 |

---

## 三、读卡 = 路由到场景页（or 劝退）

诊断结果直接映射到该看的场景页；每个模块的声称**各自如实**（去氯 ✅ / 软化 ❌ / 阻垢只保设备 / 井水只到 nuisance）。

```
检出条件                     →  路由到
──────────────────────────────────────────────────────
ZIP=游离氯 / 游离氯高          →  S1 游离氯·市政场景页
ZIP=氯胺（总氯≫游离氯）        →  S2 氯胺场景页（V1.5；未上线则诚实劝退 + 留邮箱）
硬度 极硬                    →  S4 硬水·水垢场景页（附加阻垢层）
铁 / 锈染                    →  S3 井水场景页（低中度；高铁 >2–3 ppm 劝退）
看得见颗粒                   →  S5 沉积场景页（强化物理层）
```

**诚实叠加规则（防 claim-stacking）：**

- 检出多条件 → 可推多模块，但**逐条说边界**，不打包成一句大词。
- 置信低的条件用「建议确认」措辞，不用「你的水有 X」的断定。

---

## 四、诚实劝退（能力外明说 + 留邮箱）

照 register「Honest disqualification」Allowed 行——不卖错就是 clean-formula 的信任资产。

**对外可用措辞（照 register 原文保留英文）：**

> "Your city uses chloramine — V1 isn't for your water yet. Leave your email and we'll tell you when the chloramine version ships."

能力外一律明说「compact 浴缸滤芯做不到，这是会有用的方向」：**高铁（>2–3 ppm）/ 杀菌 / 除砷 / 硝酸盐 / 软化 / 氯胺未上线**。

---

## 五、承重护栏（必带）

- **「粗筛指路 ≠ 检测危害」**：试纸是粗筛，说「帮你找到对的组合」，不是「检测你水里的危害」（register「A quick guide, not a lab test.」）。
- **类型判定以 ZIP/CCR 为准**；试纸「总氯 − 游离氯」只作氯胺 **flag**，减法放大误差。
- **禁 TDS 笔**：TDS 测总溶解固体，非氯非硬度（伪精确），本产品不以 TDS 为目标（register Banned）。
- **禁铅/重金属试纸**：低浓度不可靠且非我们声称（register Banned）。
- **禁 toxin-panic / 健康恐吓**：读数只说水的**类型 / 产品适配**，不说「你的水有毒 / 伤害你宝宝」（register Banned）。
- **禁软化承诺 / 禁健康疗效**：硬度行写死「不软化」；clean 讲透明与料级诚实，非疗效。

---

## 六、claim / 证据状态表

| Claim | 状态 | 证据 | 护栏 |
|---|---|---|---|
| "Find out what's in your water — a quick guide, **not a lab test**" | 🟢 | register Allowed · Self-diagnosis | 精度如实；粗筛指路≠检测危害 |
| ZIP→CCR 判消毒剂类型（权威） | 🟢 高 | register Self-diagnosis（ZIP→CCR 权威）；[水务图谱](../bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md) | 类型以 ZIP 为准 |
| 试纸「总氯 − 游离氯」flag 氯胺 | 🟡 中 | register（减法只作 flag） | 减法放大误差，只作 flag，不作断定 |
| 游离氯浓度 / 硬度试纸分档 | 🟡 中 | register（粗筛档位） | 只给档位，不冒充实验室数字 |
| 铁 / H₂S / 沉积定性 | 🟠 症状 | register（症状级） | 置信低→「建议确认」，不断定 |
| TDS 笔 / 铅试纸作验证或卖点 | 🔴 禁 | register Banned（TDS 非氯非硬度；铅试纸低浓度不可靠） | 整页禁用 |
| toxin-panic / 健康恐吓 / 软化承诺 | 🔴 禁 | register Banned | 读数只说类型/适配，不说危害 |

---

## Sources / 内部依据

- [内容地图（§三 D · T1 行 = 本页 spec）](./bathtub-filter-kes-marketing-site-content-map.md)
- [Claim register（Self-diagnosis、Honest disqualification、Banned：TDS/铅/toxin-panic）](../bathtub-filter-claim-register.md)
- [水质自测套件 / 模块化获客引擎（§二 判断矩阵、§三 路径、§八 红线）](../bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md)
- [T2 我们怎么测 / 认证页（去氯数字 / NSF 口径唯一真理源）](./bathtub-filter-kes-page-how-we-test-and-certify.md)
- [按水源类型的滤材方案（A/B/C → 场景）](../bathtub-filter-kes-media-stack-options-by-water-type.md)

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-kes-marketing-site-content-map]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine]]
- [[bathtub-filter-kes-page-how-we-test-and-certify]]
- [[bathtub-filter-kes-media-stack-options-by-water-type]]
