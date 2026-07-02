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
domains: [bathtub-filter, kes, chloramine, scenario, media-stack, clean-formula, version-a, honest-disqualification]
source_count: 5
review_cycle: monthly
verification_status: spot-checked
related:
  - ./bathtub-filter-kes-marketing-site-content-map.md
  - ../bathtub-filter-claim-register.md
  - ../bathtub-filter-kes-media-stack-options-by-water-type.md
  - ../bathtub-filter-chloramine-media-research.md
  - ./bathtub-filter-kes-media-catalytic-carbon.md
  - ./bathtub-filter-kes-media-sodium-ascorbate-soak.md
  - ./bathtub-filter-kes-media-kdf55-copper-zinc.md
  - ./bathtub-filter-kes-media-pp-cotton.md
---

# KES 场景页 · 氯胺城市（Chloramine City）

> 本页是**氯胺城市**用户的配置与劝退页（Spoke A · S2）。它**只引用**各滤材页的口径，不改写：机理与 claim 的真理源是 [催化炭 M3](./bathtub-filter-kes-media-catalytic-carbon.md) 与 [抗坏血酸钠浸泡件 M4](./bathtub-filter-kes-media-sodium-ascorbate-soak.md)。
> 氯胺是**红线区**：全页 claim 默认 🟡 Conditional，仅限 V1.5 双段配置，**未闭环前不上 Hub 首屏**。

---

## ① Problem — 氯胺不是游离氯

如果你所在城市用**一氯胺（monochloramine, NH₂Cl）**消毒（约占美国市政 35–40%），你面对的问题和游离氯城市**不是同一个**：

- **化学不同**：一氯胺氧化势低、N–Cl 键难还原，游离氯版的媒体（KDF55、亚硫酸钙）对它**基本无效**（KDF-55 单料实测仅 ~18% 去除；亚硫酸钙在市政 pH 下无机理支撑）。
- **接触时间不同**：游离氯几乎瞬时去除；一氯胺去除慢 2–3 个数量级，需要 **4–8 分钟**级别的接触时间。这正是浴缸（水会停留几分钟）相对淋浴（<1 秒）的结构优势。

所以氯胺城市**不能**用游离氯 SKU 硬套，需要一套**不同的媒体 + 一个用户要接受的额外步骤**。

---

## ② 配置 — inline 双段（V1.5）

**过滤棉（PET）→ 催化活性炭 → 小层 KDF55 ＋ 抗坏血酸钠浸泡件（drop-in）**（滤棉材质 2026-07-02 按 [V1 BOM 表](../bathtub-filter-v1-free-chlorine-removal-dimensions-materials.md) 裁定更正为 PET）

| 组件 | 角色 | 真理源 |
|---|---|---|
| 过滤棉（PET） | 物理前置层 / 稳定水路（非活性成分、非主 KPI） | [M7 过滤棉（PET）](./bathtub-filter-kes-media-pp-cotton.md) |
| 催化活性炭 | **inline 氯胺主力**：必要非充分，先降一部分 | [M3 催化炭](./bathtub-filter-kes-media-catalytic-carbon.md) |
| 小层 KDF55 | free-chlorine residual / 稳定层——**不承担氯胺主 KPI** | [M2 KDF55](./bathtub-filter-kes-media-kdf55-copper-zinc.md) |
| 抗坏血酸钠浸泡件 | **完成段**：浴缸停留 4–8 分钟中和氯胺 | [M4 浸泡件](./bathtub-filter-kes-media-sodium-ascorbate-soak.md) |

**逻辑 = inline 先降一部分 + 浴缸浸泡完成反应。** 催化炭开局，浸泡件收尾；两段都在用「时间换去除率」。小层 KDF55 只做游离氯 residual 和稳定层，**不是氯胺 KPI**。

---

## ③ 有界 claim 表（🟡 Conditional）

| # | Claim（英文为客户可见 wording） | 状态 | 护栏 |
|---|---|---|---|
| S2-1 | 「For chloramine-city bathers: inline reduction + in-tub completion.」 | 🟡 Conditional | 必带「+ in-tub completion」；不得暗示单芯完成 |
| S2-2 | 「Reduces combined chlorine (chloramine) during fill and soak — give it a few minutes.」 | 🟡 Conditional | 时间限定不可删；按 4–8 分钟讲 |
| S2-3 | 具体去氯胺 **% / 剂量 / 完成度** | 🔴 未验证 / 不写 | 🟡 待**氯胺专属台架**（总氯口径）；无数不写 |
| S2-4 | 「Fast / instant / 秒解 chloramine」 | 🔴 Banned | register Banned §C——禁 |
| S2-5 | 「Single cartridge fully removes chloramine」/「NSF 177 chloramine」 | 🔴 Banned | 单芯不全除 + NSF 177 只测游离氯 |

---

## ④ 承重护栏 / disclaim

1. **禁 fast / instant / 秒解**（register Banned §C）——氯胺按 **4–8 分钟**讲。
2. **「单芯不全除氯胺」必须明说**：inline 催化炭必要非充分，全除靠浸泡件在浴缸停留段完成。
3. **禁「NSF/ANSI 177 支持氯胺」**：177 只测游离氯（challenge water 要求氯胺 <0.1 mg/L）。
4. **验证用总氯（total chlorine）试纸**，不用游离氯试纸；并在说明书提示**抗坏血酸对 DPD/比色法的还原干扰**——测量应在充分反应混匀后取样，避免高估「中和」（详见 [M4 §四](./bathtub-filter-kes-media-sodium-ascorbate-soak.md)）。
5. 全页 claim **🟡，不上 Hub 首屏**，不作对外承诺，直到氯胺台架闭环。

> **验证与口径**：总氯试纸自测见 [T1 水质自测](./bathtub-filter-kes-page-water-test-diagnosis.md)，去氯胺测试 / 认证口径见 [T2 我们怎么测/认证](./bathtub-filter-kes-page-how-we-test-and-certify.md)。

---

## ⑤ 诚实劝退（Honest Disqualification）

氯胺版有两个**先说清**的前提，任一不接受，V1.5 现在还不适合你：

- **你必须接受把浸泡件放进浴缸**。这不是「一颗炭芯搞定」——inline 只降一部分，剩下靠你等几分钟让浸泡件完成。不想多这一步，就别买这套。
- **证据尚未闭环**。氯胺去除率 / 剂量数字还等 KES 自己的**氯胺专属台架**坐实（总氯口径），我们**现在不给你百分比承诺**。

> **「Your city uses chloramine — this needs an in-tub soak step, and we won't quote you a removal number until our chloramine bench test closes. If that's not for you yet, leave your email and we'll tell you when the chloramine version (V1.5) is fully validated.」**
> 「你所在城市用氯胺——这套需要一个缸内浸泡步骤，且在氯胺台架闭环前我们不给去除率数字。如果现在不合适，留个邮箱，V1.5 证据齐了我们通知你。」

不卖错 = clean-formula 的信任资产。

---

## Sources

- [Claim register（Banned §C / Conditional §B 氯胺 V1.5）](../bathtub-filter-claim-register.md)
- [氯胺去除证据（媒体对比 / EBCT / 4–8 min / 双段结论）](../bathtub-filter-chloramine-media-research.md)
- [按水源类型的滤材方案（方案 B 氯胺双段）](../bathtub-filter-kes-media-stack-options-by-water-type.md)
- [内容地图（§三 B S2 行）](./bathtub-filter-kes-marketing-site-content-map.md)
- 真理源滤材页：[M3 催化炭](./bathtub-filter-kes-media-catalytic-carbon.md) · [M4 抗坏血酸钠浸泡件](./bathtub-filter-kes-media-sodium-ascorbate-soak.md) · [M2 KDF55](./bathtub-filter-kes-media-kdf55-copper-zinc.md) · [M7 过滤棉（PET）](./bathtub-filter-kes-media-pp-cotton.md)

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-chloramine-media-research]]
- [[bathtub-filter-kes-media-stack-options-by-water-type]]
- [[bathtub-filter-kes-media-catalytic-carbon]]
- [[bathtub-filter-kes-media-sodium-ascorbate-soak]]
- [[bathtub-filter-kes-media-kdf55-copper-zinc]]
- [[bathtub-filter-kes-media-pp-cotton]]
- [[bathtub-filter-kes-marketing-site-content-map]]
- [[bathtub-filter-kes-page-water-test-diagnosis]]
- [[bathtub-filter-kes-page-how-we-test-and-certify]]
