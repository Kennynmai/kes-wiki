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
domains: [bathtub-filter, kes, media, kdf55, copper-zinc, nsf-42, biofilm, claims, version-a]
source_count: 5
review_cycle: monthly
verification_status: spot-checked
related:
  - ./bathtub-filter-kes-marketing-site-content-map.md
  - ../bathtub-filter-claim-register.md
  - ../bathtub-filter-kes-media-stack-options-by-water-type.md
  - ../bathtub-filter-evidence-bibliography.md
  - ./bathtub-filter-kes-media-calcium-sulfite.md
  - ./bathtub-filter-kes-scenario-free-chlorine.md
---

# 滤材页 · 铜锌合金 KDF55（末端安全层 + 抑生物膜层）

## 这一页是什么

本页是 KES 浴缸过滤器里 **铜锌合金 KDF55** 这一滤材的**唯一口径来源（single source of truth）**。任何场景页、PDP、Hub、广告里出现的 KDF55 claim，都必须引用本页，不得各写各的。若冲突，以本页为准。

## 这是什么料 / 机理

KDF55 是**铜锌合金**颗粒，通过电化学氧化还原去除游离氯：`Zn + Cl₂ → ZnCl₂`（[bath 条件效能页 §2](../bathtub-filter-media-efficacy-at-bath-conditions.md)）。它在热水中方向性优于冷水，额定工作温度 4–60°C，浴缸 37–40°C 处于最优区间中段（同页 §3）。此外，KDF 合金颗粒有**柱内抑菌 / 抑生物膜**特性。

## 在 KES 里的定位（别写反）

- **KDF55 = 末端安全层 + 抑生物膜层 + 寿命稳定层。它不是去氯主力。**
- 别写反：**去游离氯的主 KPI 是 CaSO₃**（见 [M1 亚硫酸钙页](./bathtub-filter-kes-media-calcium-sulfite.md)）。当前视觉稿把"铜锌=去氯主力"写反了——本页与 M1 页负责修正为「CaSO₃ 主力去氯 / KDF55 安全层」。
- 承重口径句（来自 [claim register] Media transparency 行）：`KDF55 as end-stage safety layer and biofilm-inhibition layer. CaSO3 as primary free-chlorine reduction KPI.`

## Claim 与证据状态表

| claim（客户可见英文保留原文） | 🟢🟡🔴 | 证据出处 | 护栏 |
|---|---|---|---|
| "KDF55 media is backed by supplier NSF/ANSI 42 material-level listing." | 🟢 | E1：NSF Cert# C0843384-01（Zibo Onlyzone，2025-04-10，组织级 listing） | **料级 listing only**；**每处必带「the finished KES product is not itself NSF-certified」**免责 |
| "KDF55 media tested compliant with EU food-contact standards（CM/RES 2013/9 + Reg 1935/2004 Ch.III）— 22 heavy metals below max limits, sensory 0/4." | 🟢 | E2：TÜV SÜD 721682290C，2023-07-13 | **料级 material-safety only**；不得外推为成品 food-contact 认证 |
| "KDF media supports biofilm inhibition inside the filter column. 24h dynamic-contact test (ASTM E 2149-2020) vs *S. aureus*, reduction >99.99%." | 🟡 | E3：广州微生物研究所 WJ20221264，2022-04-20，CNAS L0823 | **只讲柱内 24h**；**禁**"kills bacteria in your bath water"——浴缸 EBCT 仅 0.48–0.95 s，比测试短 5–6 个数量级 |
| "KDF55 media documented 92.6% lead reduction in a 24h static soak test (FSDA M250616-30)." | 🟡 高误读风险 | E4：Zhejiang Fries FSDA M250616-30，2025-06-23（静态浸泡 24h） | **建议只进 spec-sheet，不进营销**；静态浸泡 ≠ 浴缸注水；成品未做 lead-by-flow-through 测试；不得写"product removes X% lead" |
| KDF55 是去游离氯主力 | 🔴 禁（写反） | — | 去氯主力是 CaSO₃；KDF55 写"安全层"。修当前视觉稿 |
| 成品 / KDF55 经 NSF 成品认证 | 🔴 禁 | — | 只有供应商组织级 NSF/ANSI 42 listing（E1）；成品未认证免责必带 |

## 必带承重护栏 / disclaim

- **NSF/ANSI 42 每一处引用都必带**：`The finished KES product is not itself NSF-certified.`（[claim register] Supplier material credibility 行强制）。
- 抑菌 claim **禁**"杀浴缸水里的菌"——只能讲柱内 24h 静态测试（E3）。
- 除铅（E4）是静态浸泡 24h，**建议整条不进营销、只作 spec-sheet 一行**；高误读风险，标 🟡。
- 承重口径句不可写反：KDF55 = 安全层，CaSO₃ = 去氯主力。

## 用到我的场景（反链）

- [S1 · 游离氯·市政](./bathtub-filter-kes-scenario-free-chlorine.md) — KDF55 作末端安全层（过滤棉（PET）→ KDF55 → CaSO₃）。
- [S2 · 氯胺·市政（V1.5）](./bathtub-filter-kes-scenario-chloramine.md) — 小层 KDF55 作 free-chlorine residual / 稳定层，非氯胺主 KPI。
- S3 · 井水 — 井水线以 KDF85 为主媒体；KDF55 在此线非主角。

## Sources / 内部依据

- [Claim register（Supplier credibility / EU food-contact / 抑菌 / 除铅 行）](../bathtub-filter-claim-register.md)
- [证据参考书目（E1–E4）](../bathtub-filter-evidence-bibliography.md)
- [按水源类型的滤材方案](../bathtub-filter-kes-media-stack-options-by-water-type.md)
- [浴缸条件下滤材效能（§2–§3 机制）](../bathtub-filter-media-efficacy-at-bath-conditions.md)

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-kes-marketing-site-content-map]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-evidence-bibliography]]
- [[bathtub-filter-kes-media-stack-options-by-water-type]]
- [[bathtub-filter-kes-media-calcium-sulfite]]
- [[bathtub-filter-kes-scenario-free-chlorine]]
- [[bathtub-filter-kes-scenario-chloramine]]
