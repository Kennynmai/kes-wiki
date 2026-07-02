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
domains: [bathtub-filter, kes, consumer-education, testing, test-strip, tds, chlorine-strip, confidence]
source_count: 4
review_cycle: monthly
verification_status: spot-checked
related:
  - ../bathtub-filter-customer-water-quality-test-methods-2026-06-03.md
  - ../bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md
  - ../bathtub-filter-disinfectant-types-and-media-guide.md
  - ../bathtub-filter-institutional-guidance.md
  - ../bathtub-filter-claim-register.md
---

# E5 · 怎么测我家洗澡水 + 工具置信度

## 这一页帮你搞懂什么

网上一搜"怎么测自来水"，蹦出来试纸、TDS 笔、送实验室一堆工具，价格从几块钱到上百块。问题是：**它们测的根本不是同一个东西**。用错工具，很容易得出"这产品没用"的错误结论。

这一页帮你：
1. 搞清试纸 / TDS 笔 / 专业实验室**各测什么、不测什么**；
2. 学会用**对的工具**验证过滤器有没有用；
3. 避开最常见的坑——**"我用 TDS 笔测数字没变 = 产品无效"**。

> 口径提醒：家用工具是**粗筛指路，不是实验室检测**——给你方向和档位，不给精确诊断。术语不懂查 [E4 术语表](./bathtub-filter-kes-edu-water-glossary.md)。

---

## 一、三种工具，各测什么（先看这张表）

| 工具 | 测什么 | 测**不**了什么 | 置信 |
|---|---|---|---|
| **游离氯试纸** | 游离氯浓度（档位） | 氯胺、硬度、TDS | 🟡 粗筛指路 |
| **总氯试纸** | 总氯（游离氯 + 氯胺） | 单独看不出哪部分是氯胺 | 🟡 粗筛指路 |
| **硬水试纸 / 色块** | 硬度档位（软/中/硬/极硬） | 氯、TDS | 🟡 粗筛指路 |
| **TDS 笔** | 溶解固体总量（矿物质、盐等） | 🔴 **测不出氯**、不等于硬度 | 只反映总固体，非氯非硬度 |
| **专业实验室** | 铅 / 重金属 / 细菌 / 砷 / 硝酸盐等具体项 | —— | 🟢 最准，但贵、慢 |

出处：[自测套件 §二](../bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md)、[客户测试方法页](../bathtub-filter-customer-water-quality-test-methods-2026-06-03.md)。

---

## 二、TDS 笔的大坑（差评高发点，务必看）

TDS 笔便宜、有个数字显示、看起来"科学"——所以很多人拿它测过滤器有没有用。**这是错的。**

🔴 **TDS 笔测的是"溶解固体总量"，它测不出氯。**

- 去氯过滤器**本来就不该让 TDS 明显下降**——因为它的工作是去氯，不是降低溶解固体总量。
- 所以"我用 TDS 笔测，装过滤器前后数字没变，说明产品没用"是**用错工具得出的错误结论**。
- 真实数据：在竞品评论里，用工具测试的用户中 **TDS/PPM 比测氯还常见**（借助外物测试的评论里，TDS/PPM 被提 14 次，氯只 9 次）——很多人拿 TDS 当"是否真过滤"的判据，结果误判（[客户测试方法页](../bathtub-filter-customer-water-quality-test-methods-2026-06-03.md)）。

> **一句话记住：验证去氯要用游离氯试纸，不是 TDS 笔。**（[自测套件 §五](../bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md)）

如果你装的是**阻垢层**（针对硬水），TDS 前后不变**更是正常的**——因为阻垢不软化、钙镁还留在水里（[E3 硬水页](./bathtub-filter-kes-edu-hard-water-map-and-units.md)）。

---

## 三、怎么正确验证过滤器有没有用

**用匹配你水型的试纸，装芯前后各测一次**（[自测套件 §五](../bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md)）：

| 你的水型 | 验证工具 | 看什么 |
|---|---|---|
| **游离氯水** | 游离氯试纸 | 装芯后游离氯档位有没有降下来 |
| **氯胺水** | **总氯试纸**（不是游离氯试纸） | 游离氯试纸测不出氯胺，氯胺要看总氯 |
| **硬水（阻垢层）** | 不用 TDS 验证 | 阻垢不改变硬度 / TDS，别拿 TDS 当判据 |

**标准化对比（否则测了也不算数）**——照 [客户测试方法页](../bathtub-filter-customer-water-quality-test-methods-2026-06-03.md) 的建议：同一水源、同一流速、同一接触时间、同一批试纸，才能比得出前后差异。

⚠️ **氯胺 / 维生素 C 版的一个坑**：刚加完维生素 C / 抗坏血酸钠就立即测，残余还原剂会干扰比色，让读数**偏低、高估效果**——要按说明书指引的时机、充分反应混匀后再取样（[自测套件 §五](../bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md)）。

---

## 四、每种工具的置信度（诚实边界）

- **试纸（氯 / 总氯 / 硬度）**：🟡 **粗筛指路 ≠ 实验室检测**。它给你档位、告诉你大方向（是不是有氯、大概多硬），但不给实验室级精确数字。够用来选滤材、验证前后变化。
- **TDS 笔**：只反映溶解固体总量，**不是氯、不是硬度**，也不代表"有害/无害"。别用它做去氯验证（🔴）。
- **专业实验室**：🟢 最准。要查铅 / 重金属 / 细菌 / 砷 / 硝酸盐这类具体污染物，只有实验室能给可靠答案——这些**不是家用试纸能测**的，也不是 compact 浴缸滤芯声称能处理的（[水源类型指南](../bathtub-filter-water-source-types-guide.md)）。
- 🔴 **不做铅 / 重金属试纸**：低浓度不可靠，且不是我们声称的能力范围（[自测套件 §八](../bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md)）。真担心铅，送实验室或用认证的专项检测。

> 大多数人其实**不需要动手测**：查一次 CCR（[E7](./bathtub-filter-kes-edu-how-to-read-your-ccr.md)）就能拿到消毒剂类型 + 硬度基线，够选滤材了。试纸是"想更准 / 想亲眼验证前后变化"时的升级项。

---

## claim / 证据状态表

| 说法 | 🟢🟡🔴 | 依据 / 护栏 |
|---|---|---|
| 试纸是粗筛指路，不是实验室检测 | 🟢 | [自测套件 §八](../bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md)、[客户测试方法页](../bathtub-filter-customer-water-quality-test-methods-2026-06-03.md) |
| 游离氯试纸验证去氯（前后对比） | 🟢 | [自测套件 §五](../bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md) |
| 氯胺用总氯试纸验证 | 🟢 | 游离氯试纸测不出氯胺（[自测套件 §五](../bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md)） |
| TDS 笔测不出氯 / 不能验证去氯 | 🔴 禁把 TDS 当去氯验证 | [客户测试方法页](../bathtub-filter-customer-water-quality-test-methods-2026-06-03.md)、[自测套件 §八](../bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md) |
| 铅 / 重金属试纸作卖点或验证 | 🔴 禁 | 低浓度不可靠、非我们声称（[自测套件 §八](../bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md)） |
| "测出你水里的危害" / 健康恐吓 | 🔴 禁 | 试纸只说类型/适配，不诊断危害健康 |

---

## 诚实边界 / 护栏

- 家用工具是**粗筛指路，不是实验室检测**——给方向和档位，不给精确诊断，更不诊断"危害健康"。
- 🔴 **TDS 笔测不出氯，不能验证去氯**（本页最重要的一条）。验证去氯用**游离氯试纸**；氯胺用**总氯试纸**。
- 🔴 不做铅 / 重金属试纸（低浓度不可靠）；真要查具体污染物请送实验室。
- 前后对比必须标准化（同水源 / 流速 / 接触时间 / 试纸），否则主观差异不能算数。

---

## 下一步

- 想先查权威的类型 + 硬度（多数人够用）→ [E7 怎么读你的 CCR](./bathtub-filter-kes-edu-how-to-read-your-ccr.md)
- 不确定自己是游离氯还是氯胺 → [E1 你的城市用游离氯还是氯胺](./bathtub-filter-kes-edu-chlorine-vs-chloramine-geography.md)
- 想搞懂硬度单位和地图 → [E3 美国硬水地图 + 硬度单位](./bathtub-filter-kes-edu-hard-water-map-and-units.md)
- 想做 KES 的完整选型自测 → [T1 水质自测 / 选型页](./bathtub-filter-kes-page-water-test-diagnosis.md)
- 想知道滤芯什么时候该换（用试纸判断）→ [T3 更换与寿命页](./bathtub-filter-kes-page-replacement-and-lifespan.md)

## Sources

- [客户如何判断水质是否改善（测试方式排序、TDS 误解、标准化对比）](../bathtub-filter-customer-water-quality-test-methods-2026-06-03.md)
- [水质自测套件 / 获客引擎（工具×参数×置信、验证试纸、抗坏血酸干扰、禁 TDS/铅试纸）](../bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md)
- [消毒剂种类与滤材指南（游离氯 vs 氯胺测试口径）](../bathtub-filter-disinfectant-types-and-media-guide.md)
- [机构指南（CCR 作为权威来源）](../bathtub-filter-institutional-guidance.md)

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-kes-marketing-site-content-map]]
- [[bathtub-filter-customer-water-quality-test-methods-2026-06-03]]
- [[bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine]]
- [[bathtub-filter-disinfectant-types-and-media-guide]]
- [[bathtub-filter-institutional-guidance]]
- [[bathtub-filter-kes-edu-water-glossary]]
- [[bathtub-filter-kes-edu-chlorine-vs-chloramine-geography]]
- [[bathtub-filter-kes-edu-hard-water-map-and-units]]
- [[bathtub-filter-kes-edu-how-to-read-your-ccr]]
- [[bathtub-filter-kes-page-water-test-diagnosis]]
- [[bathtub-filter-kes-page-replacement-and-lifespan]]
