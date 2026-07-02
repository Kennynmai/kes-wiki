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
domains: [bathtub-filter, kes, chloramine, sodium-ascorbate, vitamin-c, media, filtration-media, clean-formula, version-a]
source_count: 5
review_cycle: monthly
verification_status: spot-checked
related:
  - ./bathtub-filter-kes-marketing-site-content-map.md
  - ../bathtub-filter-claim-register.md
  - ../bathtub-filter-kes-media-stack-options-by-water-type.md
  - ../bathtub-filter-chloramine-media-research.md
  - ./bathtub-filter-kes-media-catalytic-carbon.md
  - ./bathtub-filter-kes-scenario-chloramine.md
  - ../bathtub-filter-evidence-bibliography.md
---

# KES 滤材页 · 抗坏血酸钠浸泡件（Sodium Ascorbate Soak）

> **这一页是「抗坏血酸钠浸泡件」这一料在 KES 站内的唯一口径源（single source of truth）。**
> 任何场景页 / PDP / 说明书提到浸泡件的定位、机理、剂量、claim、验证方法，都引用本页。浸泡件是**氯胺红线区最敏感的一块**——它是「时间换去除率」的第二段，**天生慢**，因此本页从头到尾禁「秒解」，所有 claim 默认 🟡 Conditional，仅限 V1.5 双段配置。

---

## 一、是什么料 / 机理

抗坏血酸钠（sodium ascorbate，维生素 C 的钠盐）是一个**溶解态还原剂浸泡件**（drop-in bath accessory，形态可为药片 / 网袋 / 出水口套件，最终形态待定）。丢进浴缸后溶解，在**浴缸停留段**中和一氯胺：

- C₆H₇O₆⁻（抗坏血酸根）+ NH₂Cl → 脱氢抗坏血酸 + NH₄⁺ + Cl⁻
- N–Cl 键被还原，释放铵与氯离子；副产物无卤代有机物。

**它对游离氯瞬时；对氯胺需要 4–8 分钟。** 这不是缺陷，是浴缸 format 的结构性优势：淋浴接触 <1 秒（实测对氯胺零效果），而浴缸注水+浸泡恰好提供 4–8 分钟窗口。

**为何选抗坏血酸钠而非抗坏血酸？** 理由是 **pH，不是效率**：

- 两者活性还原物相同（抗坏血酸根），**中和氯的化学计量几乎一样**（AWWARF 一手实测 @ pH 8.0：抗坏血酸 2.48 份 / 抗坏血酸钠 2.78 份 / 份氯——抗坏血酸钠按质量反而**略多**，MW 198 vs 176）。
- **「抗坏血酸钠省 50×」是网络谣传，已证伪**（与一手数据差约 140×，见 [氯胺证据页 §7 刷新](../bathtub-filter-chloramine-media-research.md)）——**本页与营销文案不得使用此说法**。
- 真正理由：抗坏血酸粉末过量会把 pH 拉低（AWWARF 实测降到 5.07 / 现场降 0.3–0.6 单位）；抗坏血酸钠更近中性（pH≈7.0，降幅 <0.1），**更贴合 bath comfort 叙事**。

---

## 二、在 KES 的定位

**抗坏血酸钠浸泡件 = 氯胺版（V1.5）第二段：在浴缸停留段完成氯胺中和。**

- 与 [催化炭（M3）](./bathtub-filter-kes-media-catalytic-carbon.md) 组成双段：inline 催化炭先降一部分，浸泡件用 4–8 分钟停留收尾。**两段都在用「时间换去除率」**，浴缸是唯一天然提供这段时间的 format。
- 用户须**接受「额外把配件放进浴缸」**这个前提——这是氯胺 SKU 与游离氯 SKU 的根本 UX 差异，也是诚实劝退的分岔点（见 [S2 场景页 ⑤](./bathtub-filter-kes-scenario-chloramine.md)）。

---

## 三、claim 与证据状态表

| # | Claim（英文为客户可见 wording） | 状态 | 证据 / 依据 | 备注护栏 |
|---|---|---|---|---|
| A1 | 「Neutralizes chloramine in bath water during fill and soak — give it a few minutes.」 | 🟡 Conditional | SFPUC（Tier 2 政府）+ AWWA C655（标准）；4–8 分钟接触（[证据页 §4](../bathtub-filter-chloramine-media-research.md)） | 必带「a few minutes / during soak」时间限定；禁去掉时间条件 |
| A2 | 「Sodium ascorbate stays near-neutral — no pool smell, no acid sting.」（近中性叙事） | 🟡 Conditional | AWWARF pH 实测（钠盐 pH≈7.0，降幅<0.1） | 仅料级/舒适；不得翻译成健康/护肤声称 |
| A3 | 具体**剂量表 / 完成度 %**（如「X mg / 加仑 → 总氯 <Y」） | 🔴 未验证 / 不得写 | SFPUC 有「~1,000 mg/1 ppm/40–50 gal」参考值，但**无 KES 成品台架复核** | 🟡 待验证：须**氯胺专属台架**（40±2°C、总氯口径、≥3 重复），见缺口。KES 复核前不印剂量承诺 |
| A4 | 「Fast / instant / 秒解 chloramine」 | 🔴 Banned | register Banned §C；文献为 4–8 分钟，亚分钟数据有三条保留、不可作承诺 | **全页最硬红线**：任何「快」字禁用 |
| A5 | 「Works in the shower too」 | 🔴 Banned（错场景） | 淋浴 <1 秒实测零效果（[证据页 §4](../bathtub-filter-chloramine-media-research.md)） | 浸泡件仅浴缸 format |

> 关于亚分钟：AWWARF Portland 现场有「充分混合下可能亚分钟」的**上行信号**，但带三条保留（管内接触时间未隔离 / 抗坏血酸干扰比色 / 单次未重复且与 Basu 2011 冲突）。**规划值仍按 SFPUC 4–8 分钟**；「混合能压多快」必须 KES 自己台架定，不能拿现场数据当承诺（[证据页 §7 / §9.4](../bathtub-filter-chloramine-media-research.md)）。

---

## 四、必带承重护栏

1. **禁 fast / instant / 秒解**（register Banned §C）——这是抗坏血酸浸泡件最容易被误写的红线。按 **4–8 分钟**规划。
2. **单芯不全除氯胺**：浸泡件是「完成段」，前提是有 [催化炭 inline（M3）](./bathtub-filter-kes-media-catalytic-carbon.md) 先降一部分。
3. **验证用总氯（total chlorine）试纸**，不用游离氯试纸（游离氯已被前段处理，看不出氯胺）。
4. **抗坏血酸干扰比色法的测量时机提示**（写进说明书）：抗坏血酸是还原剂，**会干扰 DPD/比色读数**、可能把「中和」高估。测量须用经验证的方法或扣空白，验证读数应在**充分反应并混匀后**取样，避免局部未反应/过量还原剂造成误读；必要时第三方复核。
5. **不得用「抗坏血酸钠省 50×」谣传**；选钠盐的理由如实写作「近中性、更舒适」。
6. 剂量数字**未经 KES 台架复核前不印为承诺**（🟡）。

---

## 五、用到我的场景（反链）

- [S2 · 氯胺城市场景](./bathtub-filter-kes-scenario-chloramine.md) —— 浸泡件是该配置的第二段（完成段）。

---

## Sources

- [Claim register（Banned §C 秒解禁 / Conditional §B 氯胺 V1.5）](../bathtub-filter-claim-register.md)
- [氯胺去除证据（SFPUC 4–8 min / AWWARF 化学计量 / pH / 亚分钟三保留）](../bathtub-filter-chloramine-media-research.md)
- [按水源类型的滤材方案（方案 B 双段：为何抗坏血酸钠）](../bathtub-filter-kes-media-stack-options-by-water-type.md)
- [内容地图（§三 C M4 行）](./bathtub-filter-kes-marketing-site-content-map.md)
- [证据参考书目（条目 23/25）](../bathtub-filter-evidence-bibliography.md)

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-chloramine-media-research]]
- [[bathtub-filter-kes-media-stack-options-by-water-type]]
- [[bathtub-filter-kes-media-catalytic-carbon]]
- [[bathtub-filter-kes-scenario-chloramine]]
- [[bathtub-filter-kes-marketing-site-content-map]]
