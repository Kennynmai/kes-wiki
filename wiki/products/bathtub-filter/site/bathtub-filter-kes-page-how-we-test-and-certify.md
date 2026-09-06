---
type: product
status: draft
owner: strategy
created: 2026-06-30
updated: 2026-09-05
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, testing, certification, nsf, dechlorination, flow-rate, 15lpm, 25lpm, dpd, single-source-of-truth]
source_count: 6
review_cycle: monthly
verification_status: spot-checked
related:
  - ./bathtub-filter-kes-marketing-site-content-map.md
  - ../bathtub-filter-claim-register.md
  - ../bathtub-filter-25lpm-dechlorination-bench-test-spec.md
  - ../bathtub-filter-evidence-bibliography.md
  - ./bathtub-filter-kes-page-water-test-diagnosis.md
  - ./bathtub-filter-kes-page-replacement-and-lifespan.md
---

# T2 · How We Test & Certify（我们怎么测 / 认证）

## 这一页是什么

这是 KES 自有站的**方法/信任页**，讲我们怎么测这只过滤器、认证到底认证了什么、去氯数字怎么来的。

> **单一真理源声明**：全站的「去氯数字 / NSF 口径 / 15 → 25 L/min 流量口径」**只在本页定义一次**，其他页（Hub / PDP / 场景页 S1–S5 / 滤材页 M1–M7）**一律引用本页，不各写各的**。这是防 claim 漂移的核心机制（见 [内容地图 §四](./bathtub-filter-kes-marketing-site-content-map.md)）。任何页面若出现与本页不一致的去氯数字或认证措辞，以本页为准并回改那一页。

---

## 一、我们的性能口径：15 L/min bath-fill 是主线

我们讲去氯性能，**主口径永远是 15 L/min 的浴缸注水流速（bath-fill）**——这是慢速、接触时间最充分的锚点，也是 register 允许的措辞里绑死的限定词。

**对外可用措辞（照 register Allowed 原文保留英文）：**

> "Fresh-filter, best-experience segment: **≥99% system-total chlorine reduction** at 15 L/min bath-fill flow."
>
> ⚠️ 2026-09-05：这句的数字部分在 Gate 1 前为 🟡，对外表面一律用 `[去氯率·待第三方实测]` 占位（与 website-copy / Amazon 一致）；只有"free chlorine / fresh-filter / 15 L/min"三个限定词是 🟢 结构。

两个限定词**不可删**：

- **"free chlorine"**（游离氯）——不是 total chlorine，不是 chloramine。V1 媒体（KDF55 + CaSO₃）只处理游离氯。
- **"fresh-filter / best-experience segment" + "15 L/min"**——系统总去除率随滤芯寿命衰减、随流量升高而下降，去掉限定词就成了兑不了现的承诺。

> KPI 是**系统总**（KDF55 × CaSO₃ 链），不是单一介质。CaSO₃ 是游离氯去除主力，KDF55 是末端安全层/抑生物膜层（见 [M1 亚硫酸钙](./bathtub-filter-kes-media-calcium-sulfite.md) / [M2 KDF55](./bathtub-filter-kes-media-kdf55-copper-zinc.md)）。

---

## 二、25 L/min 只是「最大通过流量」，不上性能承诺

很多美式龙头出水在 18–25 L/min。我们的壳体**能通过 25 L/min**（V1 设计防溢目标 ≤30 L/min；曾有 35 L/min 无溢流的内部测试，但那是 204 g KDF + 45 g 炭 + 两层纤维盘的旧配置，🟡 V1 配置复测待做），但**25 L/min 只作为「最大通过流量 / 兼容性说明」**，**不承载去氯性能承诺**。

**25 L/min 下的具体去氯率 = 🟡 待验证**，pending Gate 1 第三方 DPD 实测。在实测通过门槛之前，**25 L/min 的任何去氯数字都不上首屏、不作对外承诺**。

**Gate 1 通过门槛**（照 [25 L/min 测试 spec §4](../bathtub-filter-25lpm-dechlorination-bench-test-spec.md)）：

- 流量 **25 L/min**、进水**真实 2 ppm** 游离氯（不是内部单测用的 5 ppm）、**新芯**
- 去氯率 **≥85%**
- **25 → 27 L/min 斜率平缓**（<5pp），确认离失效边缘有安全裕度
- 方法：独立第三方实验室 **DPD 分光/比色法**（氯试纸目视只作现场预读，不作最终证据）

> **为什么不把内部数字写死**：我们有过 2026-03-20 内部单测（5 ppm 高浓度、氯试纸比色、单次无重复），但那是**内部比色单测**，不是第三方 DPD、不是真实龙头浓度。把它说成坐实的对外数字，就成了我们批评对手（in-progress 说成 Certified、内部比色说成 clinically tested）的同一种放大。所以 25 L/min 的去氯率一律标 🟡，等 Gate 1。

---

## 三、第三方 DPD 报告（游离氯口径）

对外发布的去氯数字，**必须用第三方 DPD 实测值回填**，指标是**自由氯（free chlorine）**、mg/L 进出口、% reduction =（in − out）/ in。

- **禁**用内部模型的「≥92%@25 L/min」——那是 5 ppm 系统总氯的比色单测，不是真实浓度 DPD（见 [register Conditional · Fast-flow 行](../bathtub-filter-claim-register.md)）。
- 每条件 ≥3 次重复，报告均值 + 极差；必记水温、累计通水量、进水浓度、流量实测值。

DPD 报告到位前，这一节的所有 25 L/min 具体数字保持 🟡。

---

## 四、NSF/ANSI 42 = KDF55 料级 listing（成品/CaSO₃ 未认证）

这是全站最容易被读错的地方，本页把口径写死，其他页照抄。

**对外可用措辞（照 register 原文保留英文）：**

> "KDF55 media is backed by supplier NSF/ANSI 42 **material-level** listing (Zibo Onlyzone, Cert# C0843384-01). CaSO3 has NSF/ANSI 177-protocol free-chlorine reference testing, but **CaSO3 itself is not NSF-certified and the finished KES product is not NSF-certified.** Verify with the included free-chlorine test strip."

**每一处提到 NSF 的地方，必带这两句免责，一句都不能少：**

- **成品未 NSF 认证**（the finished KES product is not itself NSF-certified）
- **CaSO₃ 未 NSF 认证**（CaSO3 itself is not NSF-certified）

**禁用措辞**：任何会被读成成品认证的话，例如 "certification for safety and performance"、"NSF certified bath filter"、把 KDF55 的料级 listing 写成整机认证。

- E1 出处：NSF International Certificate# **C0843384-01**（2025-04-10 签发），范围是 **Zibo Onlyzone 组织级** NSF/ANSI 42 listing，**不代表** KES 成品入 NSF Official Listing（见 [证据书目 E1](../bathtub-filter-evidence-bibliography.md)）。
- 相关料级背书可一并引（都是**料级、非成品**）：EU food-contact 合规（E2，TÜV SÜD 721682290C）；KDF 柱内 24h 抑菌（E3）——**禁**说「杀浴缸水里的菌」；除铅静态浸泡（E4）——**建议不进营销**。详见各滤材页。

---

## 五、CaSO₃ 供应商参考报告 + 寿命模型缩放（对外只引导试纸自测）

我们的寿命模型有一个**供应商参考基线**，但**对外不直接甩数字曲线**，只引导用户「用游离氯试纸自测」。

**内部口径（🟡 供应商内部实验室，非独立第三方）：**

- E5 = 淄博宗立内部实验室 **ZONET20251113001**（2025-12-26）：40g / 0.5–1 mm CaSO₃ / 8 L/min / 2 ppm 游离氯的去氯 reference baseline。
- Version A 寿命模型按 **2.75×（质量比）× 0.9（效率 η）** 缩放，得到「系统总游离氯 ≥99% → ≥50% 约跨 **~21,550 L** @2 ppm」的曲线（见 [register Conditional · life-model traceability 行](../bathtub-filter-claim-register.md)）。（2026-07-02 按 [V1 BOM 表](../bathtub-filter-v1-free-chlorine-removal-dimensions-materials.md) 裁定更正：CaSO₃ 130g→110g，质量比 3.25×→2.75×，容量连锁重算；证据等级不变，仍 🟡 待 Gate 1 DPD）

**为什么对外不直接引曲线（🟡）：**

- E5 是**供应商内部实验室**出具，**非独立第三方**（CNAS/ilac/NSF）；若要对外发布寿命曲线，需补第三方复测。
- 参考测试用 **0.5–1 mm** 粒径，生产用 **3–4 mm**，粒径差异对动力学的影响未在该测试中单独解决。

**所以对外一律引导**：

> "Verify with the included free-chlorine test strip — compare before- and after-filter water."

数字曲线留在内部/spec 页，不放首屏，不当坐实数字宣传（呼应 register「prefer the user-facing 'verify with test strip' language rather than quoting the numeric curve directly」）。更换触发口径见 [T3 更换/寿命页](./bathtub-filter-kes-page-replacement-and-lifespan.md)。

---

## 六、承重护栏（照内容地图 §三 D · T2 行）

- **"for safety and performance" 这类会读成成品认证的措辞一律去掉。** 成品未 NSF 认证、CaSO₃ 未认证，两句免责每处必带。
- **性能口径回 15 L/min；25 L/min 仅作最大通过流量**，不上去氯性能承诺。
- **25 L/min 数字未达 Gate 1 门槛前不上首屏、不作对外承诺。**
- 去氯只讲 **free chlorine**；V1 不认领氯胺、不认领软化。
- 寿命曲线对外只引导试纸自测，不甩数字曲线。

---

## 七、claim / 证据状态表

| Claim | 状态 | 证据 | 护栏 |
|---|---|---|---|
| "≥99% system-total **free chlorine** reduction @ **15 L/min** bath-fill, fresh-filter" | 🟡 待验证（2026-09-05 由 🟢 降级：99% 来自寿命模型对最佳体验段的定义，非 15 L/min 实测；唯一近似实测 16.5 L/min / 5 ppm / 旧配置为 ~90%）| register Allowed · Chlorine reduction；内部 life model（E5 缩放） | 三个限定词（free chlorine / fresh-filter / 15 L/min）不可删；数字对外引导试纸自测 |
| 25 L/min 下具体去氯率（%） | 🟡 待验证 | pending Gate 1 第三方 DPD（真实 2 ppm、新芯 **≥85%**、25→27 斜率平缓）；[25 L/min spec §4](../bathtub-filter-25lpm-dechlorination-bench-test-spec.md) | 门槛前不上首屏；不用内部 5 ppm 比色单测数字 |
| "25 L/min max pass-through flow / 设计防溢 ≤30 L/min" | 🟢 结构 / 🟡 35 L/min 数字 | 35 L/min 来自非 V1 配置（204 g KDF + 45 g 炭）内部测试；V1 复测前不对外写 35 | 只作最大通过流量，**不**当性能承诺 |
| KDF55 = NSF/ANSI 42 **material-level** listing | 🟢 料级 | E1（NSF Cert# C0843384-01, 2025-04-10） | **每处必带**「成品未 NSF 认证、CaSO₃ 未认证」；禁读成整机认证 |
| 成品 / CaSO₃ 通过 NSF 认证 | 🔴 禁 | 无——只有 KDF55 料级 listing | 禁 "certification for safety and performance" 等成品认证误读措辞 |
| KDF55 EU food-contact 料级合规 | 🟢 料级 | E2（TÜV SÜD 721682290C） | 料级，不转成品 food-contact claim |
| CaSO₃ 寿命曲线（~21,550 L @2 ppm 数字曲线） | 🟡 待验证 | E5（供应商内部实验室 ZONET20251113001，非第三方；0.5–1 mm vs 生产 3–4 mm）× 2.75 × 0.9 缩放 | 对外不甩曲线，只引导游离氯试纸自测；发布需第三方复测 |
| 内部模型「≥92%@25 L/min」作对外数字 | 🔴 禁 | 5 ppm 系统总氯比色单测，非真实浓度 DPD | 对外数字必须用第三方 DPD 回填 |

---

## Sources / 内部依据

- [内容地图（§三 D · T2 行 = 本页 spec）](./bathtub-filter-kes-marketing-site-content-map.md)
- [Claim register（Performance/testing、NSF 料级、Fast-flow、life-model traceability）](../bathtub-filter-claim-register.md)
- [25 L/min 去氯台架 spec（Gate 1 门槛 §4）](../bathtub-filter-25lpm-dechlorination-bench-test-spec.md)
- [证据书目（E1 NSF Cert / E2 EU food-contact / E3 抑菌 / E4 除铅 / E5 CaSO₃ 寿命基线）](../bathtub-filter-evidence-bibliography.md)
- [T3 更换 / 寿命页（寿命曲线与试纸验证口径）](./bathtub-filter-kes-page-replacement-and-lifespan.md)
- [T1 水质自测 / 试纸页](./bathtub-filter-kes-page-water-test-diagnosis.md)

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-kes-marketing-site-content-map]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-25lpm-dechlorination-bench-test-spec]]
- [[bathtub-filter-evidence-bibliography]]
- [[bathtub-filter-kes-page-water-test-diagnosis]]
- [[bathtub-filter-kes-page-replacement-and-lifespan]]
