---
type: product
status: draft
owner: strategy
created: 2026-07-01
updated: 2026-07-01
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, consumer-education, hard-water, hardness, units, gpg, ppm, scale]
source_count: 4
review_cycle: monthly
verification_status: spot-checked
related:
  - ../bathtub-filter-na-water-profile-and-target-market-analysis.md
  - ../bathtub-filter-utility-service-map-by-metro.md
  - ../bathtub-filter-point-of-use-hardness-softening-feasibility.md
  - ../bathtub-filter-water-source-types-guide.md
  - ../bathtub-filter-claim-register.md
---

# E3 · 美国硬水地图 + 硬度单位

## 这一页帮你搞懂什么

洗完澡皮肤有点干涩、玻璃门上老是白斑、龙头结白垢——很多人第一反应是"水太脏"，其实更可能是**硬水**。这一页帮你：
1. 搞懂"硬水"到底是什么、美国哪些地方硬；
2. 看懂硬度的几个单位（ppm / mg/L / gpg）怎么对照；
3. 明白硬水在洗浴里意味着什么（水垢 + 干涩感，comfort 口径），以及怎么测。

> 口径提醒：硬水**不是"有毒水"**，它是水里钙镁多而已。这一页讲的是**舒适度和设备水垢**层面的事，不做健康疗效声称。术语不懂查 [E4 术语表](./bathtub-filter-kes-edu-water-glossary.md)。

---

## 一、硬水是什么

- **硬度 = 水里溶解的钙（Ca²⁺）和镁（Mg²⁺）的量**。多了就是硬水，少了就是软水。
- 硬度**跟氯是两回事**：一个城市可以既硬水又用游离氯（如拉斯维加斯），也可以软水又用游离氯（如纽约）。两个维度分开看（[北美水质分析 §1.2](../bathtub-filter-na-water-profile-and-target-market-analysis.md)）。
- 硬水在美国西南部（NV / AZ / 南 CA / TX 部分）尤其常见（[城市速查表 §1](../bathtub-filter-utility-service-map-by-metro.md)）。

---

## 二、硬度单位怎么对照

硬度常见两个单位，搞混了会看错自己的水：

| 单位 | 说明 |
|---|---|
| **ppm / mg/L** | 最常用。1 ppm ≈ 1 mg/L。硬度通常写作 "mg/L as CaCO₃"（以碳酸钙计） |
| **gpg（grains per gallon）** | 美国很多软水机、硬水试纸用这个单位 |

源文件里两个单位成对出现过，可以照抄参照：

- 拉斯维加斯 **~290 ppm / 16 gpg**
- 凤凰城 **~285 ppm / 16 gpg**
- 印第安纳波利斯 **20 gpg**（极硬）

出处：[城市速查表 §2.1/§2.2](../bathtub-filter-utility-service-map-by-metro.md)。

> 🟡 **精确换算系数（常被引用为 1 gpg ≈ 17.1 mg/L）源文件中未单独给出。** 上面的 ppm/gpg 成对值可直接引用；但如果你要在对外页面印一条"× 17.1"的换算公式，需另找权威来源（如 USGS / WQA）核实后再用，不要凭这几个成对值反推系数当权威。

---

## 三、美国硬水地图（用实测城市数据）

下面是源文件里**有实测硬度数字**的城市（[北美水质分析 §1.2](../bathtub-filter-na-water-profile-and-target-market-analysis.md)）。分档标注沿用源文件对各城市的写法：

| 城市 | 州 | 硬度（ppm as CaCO₃） | 源文件分档 | 消毒剂 |
|---|---|---|---|---|
| 圣地亚哥 | CA | 749 | 极硬 | 氯胺 |
| 迈阿密 | FL | 383 | 极硬 | 氯胺 |
| 拉斯维加斯 | NV | 318 | 极硬 | 游离氯 |
| 圣安东尼奥 | TX | 314 | 极硬 | 游离氯 |
| 埃尔帕索 | TX | ~300 | 极硬 | 游离氯 |
| 明尼阿波利斯 | MN | 280.5 | 极硬 | 氯胺 |
| 凤凰城 | AZ | 278 | 极硬 | 游离氯 |
| 坦帕 | FL | 190 | 极硬 | 氯胺 |
| 芝加哥 | IL | 183 | 极硬 | 游离氯 |
| 洛杉矶 | CA | 162 | 硬 | 氯胺 |
| 达拉斯 | TX | 135 | 硬 | 游离氯/氯胺 ⚠️ |
| 萨克拉门托 | CA | ~100–150 | 中等 | 游离氯 |
| 杰克逊维尔 | FL | ~100–150 | 中等 | 游离氯 |
| 科罗拉多斯普林斯 | CO | 80 | 略硬 | 游离氯 |
| 休斯顿 | TX | 71.9 | 中等 | 氯胺 |
| 亚特兰大 | GA | 30 | 软 ⚠️ | 游离氯/氯胺 ⚠️ |
| 纽约 | NY | 25 | 软 | 游离氯 |
| 西雅图 | WA | 24.4 | 软 | 游离氯/氯胺 ⚠️ |

⚠️ **源文件自己标注的待核实项**：亚特兰大 30 ppm（与"乔治亚是硬水州"预期不符，源文件建议人工核实官方 CCR）；达拉斯 / 西雅图 / 洛杉矶等消毒剂类型源文件标注待核实（[北美水质分析 §1.2 / §8.2](../bathtub-filter-na-water-profile-and-target-market-analysis.md)）。

> 🟡 **各分档（软 / 中等 / 略硬 / 硬 / 极硬）的统一 ppm 边界，源文件未给出阈值表**——上面只是逐城市照抄源文件的分档标注，不是一套可套用全国的通用阈值。你要判断自己城市，查它的实测硬度 + CCR 最靠谱。

**注意：不在此表的城市请自己查**，别按"同州"猜（同一州内硬度差异很大）。

---

## 四、硬水在洗浴里意味着什么（comfort 口径）

硬水带来两类**能感知的**现象：

1. **设备结垢 / 水渍**：龙头、缸壁、玻璃门上的白色钙镁沉积（[硬水场景页 ①](./bathtub-filter-kes-scenario-hard-water-scale.md)、[可行性页 §8a](../bathtub-filter-point-of-use-hardness-softening-feasibility.md)）。
2. **洗浴干涩感**：很多人在硬水区洗完觉得皮肤 / 头发干涩。

> **护栏（重要）**：这里说的是**舒适度和设备水垢**，不是健康疗效。硬水**不是"有毒水"**；我们**不声称改善湿疹 / 护肤**（[claim register Banned 区](../bathtub-filter-claim-register.md)）。

### 关键区分：阻垢 ≠ 软化

- **软化**：把钙镁**从水里拿走** → 硬度数字真下降。需要**离子交换软水机**，**不是** compact 浴缸滤芯能做到的（[可行性页 §6 / §8b](../bathtub-filter-point-of-use-hardness-softening-feasibility.md)）。
- **阻垢**：钙镁**留在水里**，只是不让它结垢 / 挂垢 → 硬度基本不变。
- compact 浴缸滤芯（若带阻垢层）做的是**阻垢**，🔴 **不软化你的水**（[硬水场景页 ③](./bathtub-filter-kes-scenario-hard-water-scale.md)）。

**已经装了全屋软水机？** 软水机去了水垢，但**氯 / 氯胺仍然 100% 保留在浴水里**（软水机只去钙镁、不去氯，[水源类型指南 §1](../bathtub-filter-water-source-types-guide.md)）——这时"去氯"和"软化"是两件互补的事。看 [E8 装了软水机的家庭](./bathtub-filter-kes-edu-water-softener-households.md)。

---

## 五、怎么测硬度

- **查 CCR**：你的水质年报里通常有硬度基线数字（[E7 怎么读你的 CCR](./bathtub-filter-kes-edu-how-to-read-your-ccr.md)）。
- **硬水试纸 / 色块**：蘸水对色卡，给你软 / 中 / 硬 / 极硬的**档位**（🟡 粗筛，不给精确数字）。
- **要精确数字**：用滴定小瓶（[自测套件 §二](../bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md)）。
- 🔴 **别用 TDS 笔判硬度**：TDS 是所有溶解固体总量，**不等于硬度**（[E4 术语表](./bathtub-filter-kes-edu-water-glossary.md)、[客户测试方法页](../bathtub-filter-customer-water-quality-test-methods-2026-06-03.md)）。而且如果你装了阻垢层，TDS 前后不变是**正常的**（因为它没在软化），这不是缺陷（[硬水场景页 ④](./bathtub-filter-kes-scenario-hard-water-scale.md)）。

怎么测的完整置信度对比见 [E5](./bathtub-filter-kes-edu-how-to-test-your-water.md)。

---

## claim / 证据状态表

| 说法 | 🟢🟡🔴 | 依据 / 护栏 |
|---|---|---|
| 各城市实测硬度 ppm | 🟢/🟡 | [北美水质分析 §1.2](../bathtub-filter-na-water-profile-and-target-market-analysis.md)；亚特兰大 / 达拉斯 / 西雅图等源文件标注待核实（⚠️） |
| ppm/gpg 成对值（LV 290/16、Phoenix 285/16、Indy 20 gpg） | 🟢 | [城市速查表 §2](../bathtub-filter-utility-service-map-by-metro.md) |
| 1 gpg ≈ 17.1 mg/L 换算公式 | 🟡 | 源文件未单独给出系数，对外用需另核实 |
| 软/中/硬/极硬统一阈值表 | 🟡 | 源文件只有逐城市分档，无通用阈值表 |
| 硬水 = 结垢 + 干涩感（comfort） | 🟢 | [硬水场景页](./bathtub-filter-kes-scenario-hard-water-scale.md)、[可行性页 §8a](../bathtub-filter-point-of-use-hardness-softening-feasibility.md) |
| compact 滤芯"软化你的水"/降硬度 | 🔴 禁 | 无 Ca/Mg 去除；软化必须走独立软水机（[可行性页 §8b](../bathtub-filter-point-of-use-hardness-softening-feasibility.md)、Banned 区） |
| 硬水改善 / 恶化湿疹（健康疗效） | 🔴 禁 | 不做健康声称（[claim register Banned](../bathtub-filter-claim-register.md)） |

---

## 诚实边界 / 护栏

- 硬水是**舒适度 + 设备水垢**问题，不是"有毒水"。这一页不做健康恐吓、不声称护肤 / 改善湿疹。
- 🔴 **阻垢 ≠ 软化**：compact 浴缸滤芯不软化你的水、不降硬度。想真软化要用独立软水机。
- 🔴 **TDS 笔不判硬度**；装阻垢层后 TDS 前后不变是正常现象。
- 标 🟡 的两处（gpg 精确换算系数、统一分档阈值表）源文件未给出；⚠️ 的城市（亚特兰大等）源文件自己标了待核实——对外引用前需二次确认。

---

## 下一步

- 硬水但想搞清消毒剂 → [E1 你的城市用游离氯还是氯胺](./bathtub-filter-kes-edu-chlorine-vs-chloramine-geography.md)
- 想测自己家硬度 → [E5 怎么测我家洗澡水](./bathtub-filter-kes-edu-how-to-test-your-water.md)
- 硬水结垢，想看 KES 怎么处理（阻垢 ≠ 软化）→ [S4 硬水 / 水垢场景页](./bathtub-filter-kes-scenario-hard-water-scale.md)
- 家里装了软水机 → [E8 装了软水机的家庭](./bathtub-filter-kes-edu-water-softener-households.md)
- 想做完整选型自测 → [T1 水质自测 / 选型页](./bathtub-filter-kes-page-water-test-diagnosis.md)

## Sources

- [北美水质与目标市场分析（逐城市实测硬度 + 分档 + 待核实标注）](../bathtub-filter-na-water-profile-and-target-market-analysis.md)
- [美国主要城市消毒剂与硬度速查表（ppm/gpg 成对值、西南硬水叠加）](../bathtub-filter-utility-service-map-by-metro.md)
- [就地软水可行性（阻垢≠软化、软化需离子交换）](../bathtub-filter-point-of-use-hardness-softening-feasibility.md)
- [特殊水源类型指南（软水机不去氯）](../bathtub-filter-water-source-types-guide.md)

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-kes-marketing-site-content-map]]
- [[bathtub-filter-na-water-profile-and-target-market-analysis]]
- [[bathtub-filter-utility-service-map-by-metro]]
- [[bathtub-filter-point-of-use-hardness-softening-feasibility]]
- [[bathtub-filter-water-source-types-guide]]
- [[bathtub-filter-kes-edu-water-glossary]]
- [[bathtub-filter-kes-edu-chlorine-vs-chloramine-geography]]
- [[bathtub-filter-kes-edu-how-to-test-your-water]]
- [[bathtub-filter-kes-edu-water-softener-households]]
- [[bathtub-filter-kes-scenario-hard-water-scale]]
- [[bathtub-filter-kes-page-water-test-diagnosis]]
