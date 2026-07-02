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
domains: [bathtub-filter, kes, scenario, free-chlorine, municipal, version-a, claims]
source_count: 6
review_cycle: monthly
verification_status: spot-checked
related:
  - ./bathtub-filter-kes-marketing-site-content-map.md
  - ../bathtub-filter-claim-register.md
  - ../bathtub-filter-kes-media-stack-options-by-water-type.md
  - ./bathtub-filter-kes-media-calcium-sulfite.md
  - ./bathtub-filter-kes-media-kdf55-copper-zinc.md
  - ./bathtub-filter-kes-media-pp-cotton.md
  - ../bathtub-filter-25lpm-dechlorination-bench-test-spec.md
---

# 场景页 · 游离氯·市政（Free-Chlorine Municipal）

> 这是唯一 🟢 结构成熟、应先做的主 SKU（Version A）。滤材口径以 M 页为准，本页只引用、不改写。

## ① 这类水的 problem

- 适用：**US urban municipal tap water**，龙头端主问题是 **free chlorine**（游离氯）。
- 市政自来水典型游离氯 0.5–2.0 mg/L（EPA 最低 0.2、MRDL 上限 4.0 mg/L），正好落在会削弱 AD 皮肤角质层保水能力的浓度区（Seki 2003，见 [证据参考 §A.1](../bathtub-filter-evidence-bibliography.md)）。
- 体感层面：pool smell、注水时的氯味与干涩感。
- **不适用**：氯胺城市（走 S2/V1.5）、硬水软化、井水。

## ② 用哪套 media 配置（V1）

**过滤棉（PET）→ KDF55 → CaSO₃**（[media-stack 方案 A](../bathtub-filter-kes-media-stack-options-by-water-type.md)），配比 过滤棉（PET）+ KDF55 130 g + CaSO₃ 110 g + 导流模块。（2026-07-02 按 [V1 BOM 表](../bathtub-filter-v1-free-chlorine-removal-dimensions-materials.md) 裁定更正：克数互换、滤棉 PET）

| 层 | 角色 | 真理源 M 页 |
|---|---|---|
| [过滤棉（PET）](./bathtub-filter-kes-media-pp-cotton.md) | 物理前置 / 颗粒拦截，**非活性成分** | M7 |
| [KDF55](./bathtub-filter-kes-media-kdf55-copper-zinc.md) | **末端安全层 + 抑生物膜层**（非去氯主力） | M2 |
| [CaSO₃](./bathtub-filter-kes-media-calcium-sulfite.md) | **游离氯去除主 KPI** | M1 |

> **口径修正（本页负责）**：这套是 **"两种活性 media（KDF55 + CaSO₃）+ 一层物理前置（过滤棉 PET）"**。当前视觉稿的「只有两种料 / no third thing」须改口为此——过滤棉是可命名、可解释的第三层，不隐去。同时：**别把 KDF55 写成去氯主力**，去氯主力是 CaSO₃。

## ③ 有界 claim 表

照 [claim register] Chlorine reduction「Allowed」行（客户可见英文保留原文）：

| claim | 🟢🟡🔴 | 出处 / 状态 | 护栏 |
|---|---|---|---|
| "Fresh-filter, best-experience segment: free-chlorine reduction at 15 L/min bath-fill flow." | 🟢 结构 | [claim register] Chlorine reduction 行 | **「free chlorine」「fresh-filter/best-experience」「15 L/min」限定词不可删** |
| 具体去氯百分比（如 ≥99% / ≥85% @流量） | 🟡 待 Gate 1 DPD | 内部寿命模型 + E5 供应商参考；数字未坐实 | 未过 [25L/min Gate 1](../bathtub-filter-25lpm-dechlorination-bench-test-spec.md)（真实 1–2 ppm、第三方 DPD、新芯 ≥85%）**前不上首屏**；对外用「用试纸验证」引导 |
| "System-total reduction follows a posted curve（99%→95%→90%→80%→<50% 换芯触发）." | 🟢 结构 / 🟡 数字 | [efficacy §9] 寿命模型 | 用 baths/gallons 不用 months；数字待 Gate 1 |
| "Verify with the included free-chlorine test strip. Do not use a TDS pen." | 🟢 | [claim register] Verification-by-user 行 | 明确 steer away from TDS pen |
| "Bath-water without the pool smell." / "Gentler-feeling bath-fill." | 🟢 | [claim register] Sensory/comfort 行 | 感官/舒适语言；不得暗示 improves skin / eczema |
| chloramine removal / water softening | 🔴 禁 | [claim register] Banned 区 | 不认领氯胺、不认领软化 |

## ④ 承重护栏 / disclaim

- **「free chlorine」限定词不可删**——不得写 total chlorine / chloramine。
- **不认领氯胺、不认领软化**（V1 化学不支持）。
- 成品不冒认 NSF：KDF55 只有供应商料级 NSF/ANSI 42 listing（E1），**成品未 NSF 认证**（见 [M2 页](./bathtub-filter-kes-media-kdf55-copper-zinc.md)与 [T2 认证页](./bathtub-filter-kes-page-how-we-test-and-certify.md)）。
- 去氯数字未过 Gate 1 前不上 Hub 首屏；对外优先「用试纸验证」，不直接甩曲线。
- 定位承重句：`This is not a water purifier. It does not target TDS reduction.`

> **验证与口径**：去氯数字 / 认证口径见 [T2 我们怎么测/认证](./bathtub-filter-kes-page-how-we-test-and-certify.md)，更换 / 寿命见 [T3 更换/寿命](./bathtub-filter-kes-page-replacement-and-lifespan.md)，水质自测见 [T1 水质自测](./bathtub-filter-kes-page-water-test-diagnosis.md)。

## ⑤ 诚实劝退

- **你的城市用氯胺** → V1 不适合你的水。`Your city uses chloramine — V1 isn't for your water yet. Leave your email and we'll tell you when the chloramine version ships.`
- **你想软化硬水** → 这个产品不软化水，请勿以此为目的购买。
- **井水 / 高铁 / 杀菌** → 均在能力外，明说不适合。
- 留邮箱：把能力外坦白做成候补承诺（[claim register] Honest disqualification 行）。

## Sources / 内部依据

- [Claim register（Chlorine reduction / Verification / Sensory / Honest disqualification）](../bathtub-filter-claim-register.md)
- [按水源类型的滤材方案（方案 A）](../bathtub-filter-kes-media-stack-options-by-water-type.md)
- [M1 亚硫酸钙](./bathtub-filter-kes-media-calcium-sulfite.md)｜[M2 KDF55](./bathtub-filter-kes-media-kdf55-copper-zinc.md)｜[M7 过滤棉（PET）](./bathtub-filter-kes-media-pp-cotton.md)
- [25L/min 去氯台架 spec（Gate 1）](../bathtub-filter-25lpm-dechlorination-bench-test-spec.md)
- [证据参考书目（Seki 2003 / E1 / E5）](../bathtub-filter-evidence-bibliography.md)

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-kes-marketing-site-content-map]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-kes-media-calcium-sulfite]]
- [[bathtub-filter-kes-media-kdf55-copper-zinc]]
- [[bathtub-filter-kes-media-pp-cotton]]
- [[bathtub-filter-25lpm-dechlorination-bench-test-spec]]
- [[bathtub-filter-kes-page-water-test-diagnosis]]
- [[bathtub-filter-kes-page-how-we-test-and-certify]]
- [[bathtub-filter-kes-page-replacement-and-lifespan]]
