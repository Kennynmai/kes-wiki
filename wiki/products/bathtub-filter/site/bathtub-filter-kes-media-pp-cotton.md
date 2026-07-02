---
type: product
status: draft
owner: strategy
created: 2026-06-30
updated: 2026-07-02
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, media, pp-cotton, sediment, physical-prefilter, claims, version-a]
source_count: 3
review_cycle: monthly
verification_status: spot-checked
related:
  - ./bathtub-filter-kes-marketing-site-content-map.md
  - ../bathtub-filter-claim-register.md
  - ../bathtub-filter-kes-media-stack-options-by-water-type.md
  - ./bathtub-filter-kes-scenario-free-chlorine.md
  - ./bathtub-filter-kes-scenario-sediment.md
---

# 滤材页 · 过滤棉（PET 聚酯纤维）（物理前置 / 沉积层）

> （2026-07-02 按 [V1 BOM 表](../bathtub-filter-v1-free-chlorine-removal-dimensions-materials.md) 裁定更正：滤棉材质由 PP（聚丙烯）更正为**聚酯纤维（PET）**，120 g/m²、直径 112 × 厚 10mm。本页文件名 slug `media-pp-cotton` 保留不改以防断链。）

## 这一页是什么

本页是 KES 浴缸过滤器里 **过滤棉（PET 聚酯纤维沉积棉）** 这一滤材的**唯一口径来源（single source of truth）**。任何场景页、PDP、Hub、广告里出现的过滤棉 claim，都必须引用本页。若冲突，以本页为准。

## 这是什么料 / 机理

过滤棉是**聚酯纤维（PET）**物理拦截层，靠机械筛滤截留颗粒物、锈渣、沉积物。它的作用是**物理拦截 + 稳定水路**，减少下游主媒体过快堵塞（[media-stack 各层职责表](../bathtub-filter-kes-media-stack-options-by-water-type.md)）。2026-03-20 内部 bench 的被测架构前置层为「35 孔 棉盘 15 mm」（[efficacy §9.5](../bathtub-filter-media-efficacy-at-bath-conditions.md)，当时记录以 PP 棉表述）。

## 在 KES 里的定位（别写反）

- **过滤棉（PET）= 物理前置 / 沉积层。它不是活性成分，不是去氯 / 去污的主 KPI。**
- 去游离氯主力是 CaSO₃（[M1](./bathtub-filter-kes-media-calcium-sulfite.md)）；末端安全层是 KDF55（[M2](./bathtub-filter-kes-media-kdf55-copper-zinc.md)）。过滤棉是这两种**活性 media 之外**的一层物理前置。
- **修正 Hub 的"只有两种料 / no third thing"**：正确口径是 **"两种活性 media（KDF55 + CaSO₃）+ 一层物理前置（过滤棉 PET）"**。有了本独立页，"just two ingredients / no third thing you can't name" 必须诚实改口——这层物理前置是可命名、可解释的，不冲突 clean-formula 叙事，但不能被隐去（见 [内容地图 §三C M7 行](./bathtub-filter-kes-marketing-site-content-map.md)）。

## Claim 与证据状态表

| claim（客户可见英文保留原文） | 🟢🟡🔴 | 证据出处 | 护栏 |
|---|---|---|---|
| "Polyester (PET) fiber physically traps particulates / sediment and stabilizes flow." | 🟢 | media-stack 各层职责；[efficacy §9.5] 架构描述 | 讲**物理拦截**；不是主 KPI |
| "Layered: polyester (PET) fiber → KDF55 → CaSO3, each layer replaceable separately." | 🟢 | [claim register] Media transparency 行 | 结构透明叙事，非 efficacy |
| 过滤棉（PET）是"活性成分"/ 去氯 / 去污主力 | 🔴 禁（写反） | — | 过滤棉非活性成分、非主去污 KPI（[claim register] 强化物理层 Conditional 行：不得当主去污 KPI） |

## 必带承重护栏 / disclaim

- 过滤棉（PET）**不是活性成分**——在 Hub / S1 页明确把"只有两种料"改口为「两种活性 media + 一层物理前置」。
- 强化过滤棉层作为沉积卖点时**不得当主去污 KPI 讲**（[claim register] 强化物理层 Conditional 行）。

## 用到我的场景（反链）

- [S1 · 游离氯·市政](./bathtub-filter-kes-scenario-free-chlorine.md) — 过滤棉（PET）作第一层物理前置（过滤棉（PET）→ KDF55 → CaSO₃）。
- [S5 · 沉积重水](./bathtub-filter-kes-scenario-sediment.md) — 强化过滤棉层作颗粒拦截。
- [S2 · 氯胺·市政](./bathtub-filter-kes-scenario-chloramine.md) · [S3 · 井水](./bathtub-filter-kes-scenario-well-water.md) — 各自前置沉积层同样用过滤棉（S3 用粗规格前置沉积层）。

## Sources / 内部依据

- [Claim register（Media transparency / 强化物理层 行）](../bathtub-filter-claim-register.md)
- [按水源类型的滤材方案（各层职责）](../bathtub-filter-kes-media-stack-options-by-water-type.md)
- [浴缸条件下滤材效能（§9.5 被测架构）](../bathtub-filter-media-efficacy-at-bath-conditions.md)

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-kes-marketing-site-content-map]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-kes-media-stack-options-by-water-type]]
- [[bathtub-filter-kes-media-calcium-sulfite]]
- [[bathtub-filter-kes-media-kdf55-copper-zinc]]
- [[bathtub-filter-kes-scenario-free-chlorine]]
- [[bathtub-filter-kes-scenario-sediment]]
- [[bathtub-filter-kes-scenario-chloramine]]
- [[bathtub-filter-kes-scenario-well-water]]
