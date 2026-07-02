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
domains: [bathtub-filter, kes, replacement, lifespan, replacement-trigger, verification, test-strip, baths, gallons]
source_count: 5
review_cycle: monthly
verification_status: spot-checked
related:
  - ./bathtub-filter-kes-marketing-site-content-map.md
  - ../bathtub-filter-claim-register.md
  - ./bathtub-filter-kes-page-how-we-test-and-certify.md
  - ../bathtub-filter-evidence-bibliography.md
  - ./bathtub-filter-kes-page-water-test-diagnosis.md
---

# T3 · Replacement & Lifespan（更换 / 寿命页）

## 这一页是什么

这是 KES 自有站的**方法/信任页**，讲这只滤芯什么时候该换、怎么自己验证「该换了」。

> 定位口径：**更换触发曲线（99% → 95% → 90% → 80% → <50%）+ 用户用游离氯试纸验证。** 这一页是 register「Replacement-trigger」+「Verification-by-user」Allowed 行的对外表面。
>
> 去氯数字/寿命曲线的口径**不在本页新造**——引用 [T2 我们怎么测/认证页](./bathtub-filter-kes-page-how-we-test-and-certify.md)。本页只把它翻成「什么时候换 + 怎么验证」。

**承重口径：用 baths / gallons，不用月。**「你家自来水的氯浓度直接影响寿命——用游离氯试纸验证。」

---

## 一、更换触发曲线（贴一条明示曲线）

系统总**游离氯**去除率随滤芯寿命衰减；我们不用黑箱倒计时，用一条明示的衰减曲线 + 你自己用试纸看到的读数。

| 系统总游离氯去除率 | 状态 | 动作 |
|---|---|---|
| ~99% | 新芯 / best-experience | 正常使用 |
| ~95% | 仍良好 | 正常使用 |
| **~90%** | **soft trigger（软触发）** | 可以开始备芯 |
| **~80%** | **strong trigger（强触发）** | 建议更换 |
| **<50%** | **mandatory（强制）** | 必须更换 |

**对外可用措辞（照 register 原文保留英文）：**

> "Replace when system-total chlorine reduction drops to ~90% (soft trigger) / ~80% (strong trigger) / ~50% (mandatory)."

---

## 二、寿命讲成 baths，不讲月

照 register Replacement-trigger 行，用 gallons / baths / weeks，**不换算成月**（口径决策）。

**对外可用措辞（照 register 原文保留英文，🟢 结构）：**

> "At 2 ppm tap chlorine, 3 baths/week: soft trigger ≈ 96 baths; mandatory ≈ 121 baths (~9–10 months). At 1 ppm tap: approximately 2× lifespan."

（2026-07-02 按 [V1 BOM 表](../bathtub-filter-v1-free-chlorine-removal-dimensions-materials.md) 裁定更正：CaSO₃ 130g→110g，寿命模型缩放 3.25×→2.75×，本页全部寿命数字连锁重算；证据等级不变，仍为内部模型 🟡 待 Gate 1 DPD。）

**承重限定句必带：**

> "Your local tap chlorine affects lifespan — verify with the included free-chlorine test strip."

> 这些 baths 数来自内部寿命模型（E5 缩放，见 [T2 §五](./bathtub-filter-kes-page-how-we-test-and-certify.md)）。**「~9–10 months」只作 2 ppm / 3 baths/week 情形下的换算参照，不作独立时间承诺**——氯浓度翻倍/减半，寿命随之变。

---

## 三、「50,000 L 裸容量」这个数需溯源（🟡 待溯源）

如果任何视觉稿/文案里出现「**50,000 L 裸容量**」这类寿命数字：

> ⚠️ **🟡 待溯源，不得直接写死当 🟢。**
>
> 我们内部**有来源**的寿命模型是 **~21,550 L @2 ppm 游离氯**（系统总游离氯 ≥99% → ≥50%，E5 缩放：40g/0.5–1mm CaSO₃/8 L/min/2 ppm 供应商参考 × 2.75 质量比 × 0.9 效率；见 [register life-model traceability 行](../bathtub-filter-claim-register.md) + [证据书目 E5](../bathtub-filter-evidence-bibliography.md)）。
>
> **50,000 L ≈ 重算后内部模型 ~21,550 L 的 2.3 倍**，当前**无来源**。在补到来源之前：
> - 不上首屏、不作对外承诺；
> - 若要用，必须标 🟡 待溯源并写明补哪个测试（第三方 DPD 寿命曲线，参照 [Gate 1 / T2 §三](./bathtub-filter-kes-page-how-we-test-and-certify.md)）；
> - 对外优先讲 baths（§二）+ 引导试纸自测，而不是甩裸容量升数。

> 另注：E5 本身是**供应商内部实验室**（非独立第三方），且用 0.5–1 mm 粒径 vs 生产 3–4 mm；即使 ~21,550 L 也应以「引导试纸自测」为对外主措辞，数字曲线留内部（见 T2 §五）。

---

## 四、用户验证（信任锚）

照 register「Verification-by-user」Allowed 行——这是 Version A 相对回避用户验证的对手的独特信任锚。

**对外可用措辞（照 register 原文保留英文）：**

> "Verify with the included **free-chlorine** test strip: compare before- and after-filter water. **Do not use a TDS pen** — this product does not target TDS."

- 装芯前后各测一次游离氯 → 你自己看到氯降下来；
- 读数掉到软/强/强制触发档 → 你自己看到该换了，不靠黑箱倒计时 lock-in；
- **游离氯版用游离氯试纸**验证（氯胺版才用总氯试纸，见 [T1](./bathtub-filter-kes-page-water-test-diagnosis.md)）。

---

## 五、承重护栏（必带）

- **用 baths / gallons，不用月**；「~9–10 months」只作 2 ppm / 3 baths/week 换算参照。
- **「你家氯浓度影响寿命，用游离氯试纸验证」限定句必随行。**
- **禁 TDS 笔**作验证（register Banned）。
- **「50,000 L 裸容量」= 🟡 待溯源**，内部有来源的是 ~21,550 L @2 ppm；无来源不写死。
- 寿命曲线对外只引导试纸自测，不甩数字曲线（口径同 [T2 §五](./bathtub-filter-kes-page-how-we-test-and-certify.md)）。

---

## 六、claim / 证据状态表

| Claim | 状态 | 证据 | 护栏 |
|---|---|---|---|
| 更换触发曲线 99→95→90→80→<50% | 🟢 结构 | register Allowed · Replacement-trigger | 用去除率档位，不用黑箱倒计时 |
| "soft ≈ 96 baths / mandatory ≈ 121 baths (~9–10 months) @2 ppm, 3 baths/wk；~2× @1 ppm" | 🟢 结构 | register Replacement-trigger（内部 life model E5 缩放，2026-07-02 按 BOM 重算） | 用 baths 不用月；「~9–10 months」仅作 2 ppm 换算参照 |
| "Verify with included **free-chlorine** test strip; do not use TDS pen" | 🟢 | register Allowed · Verification-by-user | 游离氯版用游离氯试纸；禁 TDS 笔 |
| 内部寿命容量 ~21,550 L @2 ppm | 🟡 待验证 | register life-model traceability + E5（供应商内部实验室，非第三方；0.5–1mm vs 生产 3–4mm）× 2.75 × 0.9 | 对外引导试纸自测，不甩曲线；发布需第三方复测 |
| **「50,000 L 裸容量」** | 🟡 待溯源 | **无来源**——约为重算后内部模型 ~21,550 L 的 **2.3 倍** | 不写死当 🟢；补第三方 DPD 寿命曲线前不上首屏 |
| TDS 笔作验证工具 | 🔴 禁 | register Banned（TDS 非氯非硬度） | 明确 steer away |

---

## Sources / 内部依据

- [内容地图（§三 D · T3 行 = 本页 spec）](./bathtub-filter-kes-marketing-site-content-map.md)
- [Claim register（Replacement-trigger、Verification-by-user、life-model traceability；Banned：TDS 笔）](../bathtub-filter-claim-register.md)
- [T2 我们怎么测 / 认证页（去氯数字 / 寿命曲线 / NSF 口径唯一真理源）](./bathtub-filter-kes-page-how-we-test-and-certify.md)
- [证据书目（E5 CaSO₃ 寿命 reference baseline ZONET20251113001）](../bathtub-filter-evidence-bibliography.md)
- [T1 水质自测 / 试纸页（游离氯 vs 总氯试纸区分）](./bathtub-filter-kes-page-water-test-diagnosis.md)

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-kes-marketing-site-content-map]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-kes-page-how-we-test-and-certify]]
- [[bathtub-filter-evidence-bibliography]]
- [[bathtub-filter-kes-page-water-test-diagnosis]]
