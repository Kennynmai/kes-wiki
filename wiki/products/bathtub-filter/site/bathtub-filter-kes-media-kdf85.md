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
domains: [bathtub-filter, kes, media, kdf85, well-water, iron, hydrogen-sulfide, manganese, claims, version-c]
source_count: 4
review_cycle: monthly
verification_status: spot-checked
related:
  - ./bathtub-filter-kes-marketing-site-content-map.md
  - ../bathtub-filter-claim-register.md
  - ../bathtub-filter-kes-media-stack-options-by-water-type.md
  - ../bathtub-filter-well-water-research.md
  - ../bathtub-filter-evidence-bibliography.md
  - ./bathtub-filter-kes-scenario-well-water.md
---

# 滤材页 · KDF85（井水铁 / 硫 / 部分锰主力）

## 这一页是什么

本页是 KES 浴缸过滤器里 **KDF85（高纯铜锌合金颗粒）** 这一滤材的**唯一口径来源（single source of truth）**。任何场景页、PDP、Hub、广告里出现的 KDF85 claim，都必须引用本页，不得各写各的。若本页与其他表面冲突，以本页为准。

> 单一真理源规则（见 [内容地图 §四](./bathtub-filter-kes-marketing-site-content-map.md)）：每种 media 的 claim 只在对应 M 页定义一次。本页负责 KDF85 的机理口径与护栏；井水 SKU 的整体配置在 [S3 井水场景页](./bathtub-filter-kes-scenario-well-water.md)。

## 这是什么料 / 机理

KDF85 是**高纯铜锌合金颗粒**，与 [KDF55](./bathtub-filter-kes-media-kdf55-copper-zinc.md) 是同一氧化还原（redox）交换机制，但配比偏向井水污染物：

- **溶解性（亚铁）铁去除**：把 Fe²⁺ 氧化为不溶的氢氧化铁沉淀（[井水研究 Task 4](../bathtub-filter-well-water-research.md)）。
- **硫化氢（H₂S）去除**：通过电子转移把 H₂S 转成不溶的硫化铜，缓解「臭鸡蛋味」（同页 Task 4）。
- **部分锰 / 部分重金属**：redox 路线有一定去除，但数据弱于铁。
- **抑生物膜倾向**：合金产生羟基自由基 / 过氧化氢，柱内有抑菌倾向（与 KDF55 同类，属柱内性质，非浴水杀菌）。

**关键操作边界**（[井水研究 Task 4](../bathtub-filter-well-water-research.md)）：

- KDF85 在**铁 / H₂S 低于约 3 ppm** 时最有效；
- 适用 pH **6.5–8.5**，需要一定溶解氧维持 redox；
- 热稳定，热水不劣化。

## 在 KES 里的定位（别写反）

- **KDF85 = 井水线（方案 C）的主力去铁 / 去硫 / 部分锰媒体层。** 这是 well-water 主 KPI 所在层（[media-stack §方案 C](../bathtub-filter-kes-media-stack-options-by-water-type.md)）。
- **不是去氯主力**：井水通常无游离氯 / 氯胺，所以市政线的 CaSO₃ 在这里失去主要任务、KDF55 也不是最相关媒体——井水线应换成 KDF85 主导（[井水研究 Task 3](../bathtub-filter-well-water-research.md)）。
- **定位是 nuisance（气味 / 锈渍舒适）级，不是 health-grade remediation**：只覆盖低到中等铁 / 硫气味，不是全屋替代。

## Claim 与证据状态表

| claim（客户可见英文保留原文） | 🟢🟡🔴 | 证据出处 | 护栏 |
|---|---|---|---|
| "Targets iron / sulfur-related bath odor and rust nuisance (low-to-moderate)." | 🟡 待验证 | KDF85 机理（[井水研究 Task 4](../bathtub-filter-well-water-research.md)）；[claim register §B 井水 KDF85 行](../bathtub-filter-claim-register.md) | 仅低中度；nuisance 级，非 health remediation。**具体去除率待 KES 成品铁 / H₂S / 锰 challenge test**（🟡 无 finished-product 数据） |
| 具体铁 / H₂S / 锰去除百分比 | 🟡 待验证 | 井水研究引供应商级数据（如 Santé「铁 99.9% / H₂S 90–99%」为**竞品供应商料级值**，非 KES 成品） | **禁**直接搬竞品百分比当 KES 成品 claim；补 KES 成品 challenge test（[media-stack §SKU C 推荐测试](../bathtub-filter-kes-media-stack-options-by-water-type.md)） |
| KDF85 kills bacteria in bath water（浴水杀菌） | 🔴 禁 | 抑菌是柱内性质、静态长接触；浴缸 EBCT 极短（[claim register / KDF 抑菌行](../bathtub-filter-claim-register.md)） | 只能说柱内抑生物膜倾向，**禁**「杀浴缸水里的菌」 |
| KDF85 removes arsenic / nitrate / uranium（除砷 / 硝酸盐 / 铀） | 🔴 禁 | 机制不支持；这些是 health-significant、须全屋 RO / 专材（[井水研究 Task 4 表](../bathtub-filter-well-water-research.md)） | claim register §B「禁除砷 / 硝酸盐 / 铀」 |
| KDF85 softens water / 降硬度 | 🔴 禁 | redox 不去 Ca / Mg（[可行性页 §8b](../bathtub-filter-point-of-use-hardness-softening-feasibility.md)） | 软化是 Banned 区；井水线不认领软化 |
| 高铁（>2–3 ppm）全屋替代 | 🔴 禁 | >2–3 ppm 滤芯数天到数周即堵、压降剧增（[井水研究 Task 4](../bathtub-filter-well-water-research.md)） | 高铁**劝退**，不是产品能力 |

## 必带承重护栏 / disclaim

- **高铁劝退**：铁 / H₂S 约 **>2–3 ppm 不建议用 compact bath filter**——会快速堵塞、差评。这是硬 spec 边界，须在前端就排除买错。
- **禁**杀菌 / 除砷 / 硝酸盐 / 铀 / 高铁全屋替代 / 软化——见上表 🔴 行。
- 覆盖口径统一写 **low-to-moderate**，不得升级为「treats well water」。
- 寿命 / 更换用 baths / gallons，不用 months（口径见 T3）。

## 用到我的场景（反链）

- [S3 · 井水场景页](./bathtub-filter-kes-scenario-well-water.md) — KDF85 是该 SKU 的去铁 / 去硫主力层（粗 PP → KDF85 → 催化炭）。

## Sources / 内部依据

- [Claim register（§B 井水 KDF85 行）](../bathtub-filter-claim-register.md)
- [按水源类型的滤材方案（方案 C 井水）](../bathtub-filter-kes-media-stack-options-by-water-type.md)
- [井水场景研究（Task 3 / Task 4 KDF85 机理与边界）](../bathtub-filter-well-water-research.md)
- [就地软水可行性（§8 三路线边界）](../bathtub-filter-point-of-use-hardness-softening-feasibility.md)
- [内容地图（真理源规则）](./bathtub-filter-kes-marketing-site-content-map.md)

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-kes-marketing-site-content-map]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-kes-media-stack-options-by-water-type]]
- [[bathtub-filter-well-water-research]]
- [[bathtub-filter-point-of-use-hardness-softening-feasibility]]
- [[bathtub-filter-kes-scenario-well-water]]
- [[bathtub-filter-kes-media-kdf55-copper-zinc]]
