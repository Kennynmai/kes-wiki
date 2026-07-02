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
domains: [bathtub-filter, kes, media, calcium-sulfite, free-chlorine, claims, version-a]
source_count: 5
review_cycle: monthly
verification_status: spot-checked
related:
  - ./bathtub-filter-kes-marketing-site-content-map.md
  - ../bathtub-filter-claim-register.md
  - ../bathtub-filter-kes-media-stack-options-by-water-type.md
  - ../bathtub-filter-evidence-bibliography.md
  - ../bathtub-filter-media-efficacy-at-bath-conditions.md
  - ../bathtub-filter-25lpm-dechlorination-bench-test-spec.md
  - ./bathtub-filter-kes-scenario-free-chlorine.md
---

# 滤材页 · 亚硫酸钙 CaSO₃（游离氯去除主 KPI）

## 这一页是什么

本页是 KES 浴缸过滤器里 **亚硫酸钙（CaSO₃）** 这一滤材的**唯一口径来源（single source of truth）**。任何场景页、PDP、Hub、广告里出现的 CaSO₃ claim，都必须引用本页，不得各写各的。若本页与其他表面冲突，以本页为准。

> 单一真理源规则（见 [内容地图 §四](./bathtub-filter-kes-marketing-site-content-map.md)）：去氯数字只在 T2「我们怎么测/认证页」定义一次；每种 media 的 claim 只在对应 M 页定义一次。本页负责 CaSO₃ 的机理口径与护栏，**具体去氯数字最终仍以第三方 DPD（Gate 1）为准**。

## 这是什么料 / 机理

亚硫酸钙是一种**化学还原**去氯滤材。反应式：

`CaSO₃ + Cl₂ + H₂O → CaSO₄ + 2HCl`（不可逆）

- 亚硫酸根（SO₃²⁻）与游离氯反应速率极快——有文献称接触时间约 0.8 秒即可达 99%+ 去除（[bath 条件效能页 §2](../bathtub-filter-media-efficacy-at-bath-conditions.md)）。
- 浴缸注水的低流速（0.3–0.8 GPM）延长了每单位水的接触时间，对去氯**有利而非不利**（同页 §1–§2）。
- 高温不劣化：AquaBliss 制造商文档显示热水下媒体溶出率反而更低（<0.01%）；反应放热、不可逆，温度升高有利速率（同页 §3）。
- **重要边界**：亚硫酸盐与一氯胺的反应在 pH > 7.5 时速率极低（Yiin/Walker/Margerum 1987，见 [证据参考 §24](../bathtub-filter-evidence-bibliography.md)）——市政水典型 pH 下 CaSO₃ 几乎**无法去除氯胺**。

## 在 KES 里的定位（别写反）

- **CaSO₃ = 游离氯去除的主 KPI 层。** 这是 Version A 主 KPI 所在层（[media-stack §方案 A](../bathtub-filter-kes-media-stack-options-by-water-type.md)）。
- 别写反：**KDF55 不是去氯主力**——KDF55 是"末端安全层 + 抑生物膜层"（见 [M2 KDF55 页](./bathtub-filter-kes-media-kdf55-copper-zinc.md)）。当前视觉稿把"铜锌=去氯主力"写反了，本页与 M2 页一起负责修正。
- 系统总游离氯去除是 KDF × CaSO₃ 链式结果（`1 − (1−KDF)×(1−CaSO₃)`），但**主力贡献来自 CaSO₃**。

## Claim 与证据状态表

| claim（客户可见英文保留原文） | 🟢🟡🔴 | 证据出处 | 护栏 |
|---|---|---|---|
| CaSO₃ is the primary free-chlorine reduction KPI（去游离氯主力层） | 🟢 | media-stack §方案A；[claim register] Media transparency 行 | 只讲 **free chlorine**；不得写 total chlorine / chloramine |
| "System-total free-chlorine reduction follows a posted curve（99%→95%→90%→80%→<50%）" | 🟢（结构）/ 🟡（数字） | 内部寿命模型 @110 g CaSO₃ + η=0.9（[efficacy §9](../bathtub-filter-media-efficacy-at-bath-conditions.md)，2026-07-02 按 [V1 BOM 表](../bathtub-filter-v1-free-chlorine-removal-dimensions-materials.md) 裁定更正克数，容量重算 ~21,550 L @2ppm）；缩放自 E5 供应商参考 | 数字待 Gate 1 第三方 DPD 回填；「fresh-filter / best-experience segment」「15 L/min」限定词不可删 |
| 具体去氯百分比 / 曲线数值 | 🟡 待验证 | E5（ZONET20251113001，供应商内部实验室，非独立第三方）；粒径 0.5–1 mm 参考 vs 生产 3–4 mm 未解耦 | **补 Gate 1**：25 L/min、真实 1–2 ppm、DPD、3–4 mm 生产粒径复测（[25lpm spec](../bathtub-filter-25lpm-dechlorination-bench-test-spec.md)）。对外优先引导「用试纸验证」，不直接甩曲线 |
| CaSO₃ removes chloramine（去氯胺） | 🔴 禁 | Yiin 1987（[证据 §24](../bathtub-filter-evidence-bibliography.md)）：pH>7.5 反应速率极低 | V1 禁认领氯胺——化学机制不支持；claim register Banned 区「Chloramine for V1」 |
| CaSO₃ 经 NSF 认证 | 🔴 禁 | — | CaSO₃ 有 NSF/ANSI 177 协议下的 free-chlorine reference testing，但 **CaSO₃ 本身未 NSF 认证，成品也未 NSF 认证**（见 [M2 页] 与 T2） |

## 必带承重护栏 / disclaim

- **「free chlorine」限定词不可删**——不得升级成 total chlorine 或 chloramine。
- 去氯曲线数字对外用 **"verify with the included free-chlorine test strip"** 引导，不直接甩内部模型曲线（[claim register] Life-model traceability 行明示）。
- 承重口径句：`CaSO3 as primary free-chlorine reduction KPI. KDF55 as end-stage safety layer.`——反写即错。
- 寿命/更换用 baths / gallons，不用 months（口径见 T3）。

## 用到我的场景（反链）

- [S1 · 游离氯·市政场景页](./bathtub-filter-kes-scenario-free-chlorine.md) — CaSO₃ 是该 SKU 的去氯主力层（过滤棉（PET）→ KDF55 → CaSO₃）。

## Sources / 内部依据

- [Claim register](../bathtub-filter-claim-register.md)
- [按水源类型的滤材方案（方案 A）](../bathtub-filter-kes-media-stack-options-by-water-type.md)
- [证据参考书目（E5 供应商参考 / §24 氯胺化学）](../bathtub-filter-evidence-bibliography.md)
- [浴缸条件下滤材效能（§2 机制 / §9 寿命模型）](../bathtub-filter-media-efficacy-at-bath-conditions.md)
- [25L/min 去氯台架测试 spec（Gate 1）](../bathtub-filter-25lpm-dechlorination-bench-test-spec.md)

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-kes-marketing-site-content-map]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-kes-media-stack-options-by-water-type]]
- [[bathtub-filter-evidence-bibliography]]
- [[bathtub-filter-media-efficacy-at-bath-conditions]]
- [[bathtub-filter-25lpm-dechlorination-bench-test-spec]]
- [[bathtub-filter-kes-scenario-free-chlorine]]
- [[bathtub-filter-kes-media-kdf55-copper-zinc]]
