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
domains: [bathtub-filter, kes, content-architecture, information-architecture, site-map, marketing, claims, version-a, chloramine, well-water, anti-scale, diagnosis-kit]
source_count: 6
review_cycle: monthly
verification_status: spot-checked
related:
  - ../bathtub-filter-claim-register.md
  - ../bathtub-filter-kes-media-stack-options-by-water-type.md
  - ../bathtub-filter-kes-website-copy-v1.md
  - ../bathtub-filter-kes-homepage-and-about-page-layout.md
  - ../bathtub-filter-point-of-use-hardness-softening-feasibility.md
  - ../bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md
  - ../bathtub-filter-kes-v1-execution-roadmap-2026-06-15.md
  - ../bathtub-filter-content-ecosystem-by-layer.md
---

# KES 浴缸过滤器 · 自有营销站内容地图（Hub-and-Spoke IA）

## 为什么有这页

现有文档已经分别覆盖了：

- **单一表面文案/版式**：[[bathtub-filter-kes-website-copy-v1]]（Homepage + PDP + About 完整文案）、[[bathtub-filter-kes-homepage-and-about-page-layout]]（首屏版式）
- **产品/滤材逻辑**：[[bathtub-filter-kes-media-stack-options-by-water-type]]（A/B/C 场景 → media → claim/禁）
- **claim 护栏**：[[bathtub-filter-claim-register]]（Banned / Conditional / Allowed + 表面→claim 映射）
- **外部内容层**：[[bathtub-filter-content-ecosystem-by-layer]]（评测/媒体/社区）

但**缺一张把多页串起来的总图**：Hub 简版页 → 各水场景配置页 → 各滤材独立页 → 水质自测/测试页，彼此如何链接、每个 spoke 归哪个 claim 区、必带哪句承重护栏、关键 claim 的证据状态是什么。这页补这个空白，并作为整批内容页的**施工蓝图**。它坐在上面单表面文档之上做总调度，不重复它们的正文。

> 工作方式（本轮定的）：**内容页先做全，再倒推产品定义与包装。** 产出形态 = kes-wiki markdown 内容规格页；本页是第一块，先出总架构，再逐页填。

---

## 一、治理原则（内容先行的护栏）

内容先行是用文案去发现产品；风险是写出产品兑不了现的 claim。所以三条铁律绑死：

### 1. 每条 claim 挂证据状态标签

- 🟢 **坐实** — 有第三方/内部证据，可直接写、可上首屏
- 🟡 **待验证** — 有方向但证据未闭环（如 25 L/min 去氯待 Gate 1 DPD；50,000 L 容量待溯源）。**可以先写进 spec 页，但标黄、不上 Hub 首屏、不作对外承诺**
- 🔴 **禁** — eczema / baby-safe / 软化 / 氯胺"秒解" / TDS 笔 / toxin-panic（见 register Banned 区）

### 2. 内容页 = 产品规格书

每页写完那一刻，SKU 定义自动生成："某场景 = 哪几个 media 模块 + 哪些 claim 已清（🟢）+ 哪些待验证（🟡）"。倒推出的是**可出货 spec**，不是愿望清单。见 §五。

### 3. 问题 → 产品 → claim 三层不混用背书

三条水源路线 = 三个 problem = 三套独立 claim（[[bathtub-filter-point-of-use-hardness-softening-feasibility]] §8）。任何一页不得拿 A 的证据替 B/C 的 claim 背书。滤材页是唯一"真理源"（§三），场景页只引用、不改写口径。

---

## 二、站点地图（Hub-and-Spoke）

```
                        ┌─────────────────────────────┐
                        │  HUB · 简版产品介绍页        │
                        │  「看得见的料 / clean-honest」│
                        │  通用定位 + 承重 disclaim     │
                        │  + Match-Your-Water 路由      │
                        └──────────────┬──────────────┘
                                       │
        ┌──────────────────┬───────────┼───────────┬──────────────────┐
        │                  │           │           │                  │
   ┌────▼─────┐      ┌─────▼────┐  ┌───▼────┐  ┌───▼─────┐     ┌──────▼──────┐
   │ Spoke A  │      │ Spoke A  │  │ Spoke A│  │ Spoke B │     │  Spoke C    │
   │ 场景配置页│◄────►│ 滤材独立页│  │ PDP    │  │ 方法/信任│     │  外部内容层  │
   │ (5 页)   │ 复用 │ (7 页)   │  │(购买页)│  │ (3 页)  │     │ (已有专页)   │
   └──────────┘      └──────────┘  └────────┘  └─────────┘     └─────────────┘
```

- **Spoke A（场景配置页）** 和 **Spoke B（滤材独立页）** 之间是**多对多复用**：一个场景页引用它用到的 media 页；一个 media 页被所有用到它的场景页反链。
- **PDP** 是购买表面，从 Hub / 场景页收口；文案照 [[bathtub-filter-kes-website-copy-v1]] "二、产品页"。
- **方法/信任页** 被所有场景页和 PDP 共享引用。
- **Spoke D（产品结构/工业设计页）** 是「产品本体」层——透明滤仓/导流模块/挂带适配，是 clean-honest 母题的物理载体；被 Hub 与场景页引用，另配 1 个内部 IP/专利治理页管措辞红线（见 §三 E）。
- **Spoke E（消费者水质科普页）** 是「消费者背景知识」层——氯胺地理/硬水/井水/术语/自测/CCR，帮小白搞懂"我家水什么情况、该买哪个"；是场景页的**上游漏斗**，多由现有内部研究直接转化（见 §三 F）。
- **产品/运营文档（P）** 是 primary-source 与说明书/客服支撑层（V1 定义与不适用清单、pack-contents、维护指南、安装与兼容指南）；喂 PDP/说明书/客服（见 §三 G）。
- **服务/交易层（SVC）** 是转化漏斗 + 售后（买前 FAQ、买后验证、退货保修、订阅、referral、客服、定价、社会证明）；实质页已建，条款/价格/素材类为 `officiality: placeholder` 占位，待业务/法务补（见 §三 H）。
- **外部内容层**（评测/社区）不在自有站里建，指针到 [[bathtub-filter-content-ecosystem-by-layer]]。

---

## 页面索引（本图 + 52 个页）

> 从本图直达每个已建页的硬链接（相对 markdown），按 方法页 T / 滤材页 M / 场景页 S / 结构页 D / 消费者科普 E / 产品文档 P 分组。

**方法/信任页（T）**

- [T1 · 水质自测 / 试纸](./bathtub-filter-kes-page-water-test-diagnosis.md)
- [T2 · 我们怎么测 / 认证](./bathtub-filter-kes-page-how-we-test-and-certify.md)
- [T3 · 更换 / 寿命](./bathtub-filter-kes-page-replacement-and-lifespan.md)

**滤材独立页（M · 唯一真理源）**

- [M1 · 亚硫酸钙 CaSO₃](./bathtub-filter-kes-media-calcium-sulfite.md)
- [M2 · 铜锌合金 KDF55](./bathtub-filter-kes-media-kdf55-copper-zinc.md)
- [M3 · 催化活性炭](./bathtub-filter-kes-media-catalytic-carbon.md)
- [M4 · 抗坏血酸钠浸泡件](./bathtub-filter-kes-media-sodium-ascorbate-soak.md)
- [M5 · KDF85](./bathtub-filter-kes-media-kdf85.md)
- [M6 · 阻垢粒](./bathtub-filter-kes-media-anti-scale-granule.md)
- [M7 · 过滤棉（PET）](./bathtub-filter-kes-media-pp-cotton.md)

**水场景配置页（S）**

- [S1 · 游离氯·市政](./bathtub-filter-kes-scenario-free-chlorine.md)
- [S2 · 氯胺·市政](./bathtub-filter-kes-scenario-chloramine.md)
- [S3 · 井水](./bathtub-filter-kes-scenario-well-water.md)
- [S4 · 硬水 / 水垢](./bathtub-filter-kes-scenario-hard-water-scale.md)
- [S5 · 沉积重水](./bathtub-filter-kes-scenario-sediment.md)

**产品结构 / 工业设计页（D）**

- [D1 · 结构总览](./bathtub-filter-kes-structure-overview.md)
- [D2 · 导流模块 / 防沟槽](./bathtub-filter-kes-structure-flow-diversion-module.md)
- [D3 · 透明滤仓](./bathtub-filter-kes-structure-transparent-housing.md)
- [D4 · 扁硅胶挂带 / 适配](./bathtub-filter-kes-structure-flat-strap-fit.md)
- [结构·IP / 专利治理页（内部）](./bathtub-filter-kes-structure-ip-and-patent-governance.md)

**消费者水质科普页（E）**

- [E1 · 游离氯 vs 氯胺地理](./bathtub-filter-kes-edu-chlorine-vs-chloramine-geography.md)
- [E2 · 井水必读](./bathtub-filter-kes-edu-well-water-basics.md)
- [E3 · 硬水地图 + 硬度单位](./bathtub-filter-kes-edu-hard-water-map-and-units.md)
- [E4 · 术语表](./bathtub-filter-kes-edu-water-glossary.md)
- [E5 · 怎么测我家洗澡水](./bathtub-filter-kes-edu-how-to-test-your-water.md)
- [E6 · 氯/氯胺值得在意吗（comfort-first）](./bathtub-filter-kes-edu-chlorine-skin-worth-it.md)
- [E7 · 怎么读 CCR 年报](./bathtub-filter-kes-edu-how-to-read-your-ccr.md)
- [E8 · 软水器家庭](./bathtub-filter-kes-edu-water-softener-households.md)
- [E9 · PFAS 与浴缸过滤器（诚实边界）](./bathtub-filter-kes-edu-pfas-and-bath-filters.md)
- [E10 · 注水流速 × 去氯/寿命](./bathtub-filter-kes-edu-flow-rate-and-lifespan.md)
- [E11 · 特殊水源（RO/SCWS/雨水）](./bathtub-filter-kes-edu-special-water-sources.md)

**产品 / 运营文档页（P）**

- [P1 · V1 产品定义与「不适用」清单（primary-source）](./bathtub-filter-kes-v1-definition-and-not-for-list.md)
- [P2 · Pack-contents 规格](./bathtub-filter-kes-pack-contents-spec.md)
- [P3 · 使用与维护指南（防霉/清洁/排查）](./bathtub-filter-kes-care-and-maintenance-guide.md)
- [P4 · 安装与兼容性指南](./bathtub-filter-kes-install-and-compatibility-guide.md)
- [P5 · 包装设计 spec](./bathtub-filter-kes-packaging-design-spec.md)

**服务 / 交易页（SVC）** — 实质页 + 占位骨架（`officiality: placeholder` 待业务补）

- [SVC1 · 买前 FAQ「KES 适不适合你家水」](./bathtub-filter-kes-faq-is-kes-right-for-you.md)
- [SVC2 · 买后验证流程](./bathtub-filter-kes-post-purchase-verification.md)
- [SVC3 · 退货 / 保修 / 满意保证 ⚠️占位](./bathtub-filter-kes-returns-and-warranty.md)
- [SVC4 · 补芯订阅方案（Skip-if-still-good，数字待补）](./bathtub-filter-kes-refill-subscription.md)
- [SVC5 · Referral 方案（分享试纸卡，数字待补）](./bathtub-filter-kes-referral-program.md)
- [SVC6 · 客服与联系 ⚠️占位](./bathtub-filter-kes-support-and-contact.md)
- [SVC7 · 定价与 Refill 经济学 ⚠️占位](./bathtub-filter-kes-pricing-and-refill-economics.md)
- [SVC8 · 社会证明 / testimonials ⚠️占位](./bathtub-filter-kes-proof-and-testimonials.md)
- [SVC9 · Bundle / 多件装（结构实、价格待补）](./bathtub-filter-kes-bundles-and-multipacks.md)
- [SVC10 · 选购器（Water-Match Selector）产品 spec](./bathtub-filter-kes-water-match-selector-spec.md)
- [SVC11 · 邮件生命周期 spec（全站邮件时点唯一 owner）](./bathtub-filter-kes-email-lifecycle-spec.md)
- [SVC12 · 隐私 / ToS / 同意 / 无障碍 ⚠️占位·法律上线阻断项](./bathtub-filter-kes-privacy-terms-and-consent.md)

**渠道规格页（CH · 2026-07-02 新增）**

- [CH1 · Amazon listing 规格](./bathtub-filter-kes-amazon-listing-spec.md)
- [CH2 · 印刷版说明书 IFU 规格](./bathtub-filter-kes-print-ifu-spec.md)
- [CH3 · 移动端 / 响应式规格](./bathtub-filter-kes-mobile-responsive-spec.md)

**系统运维（OPS）**

- [OPS1 · 内容系统运维 SOP（新页/审批/销项/传播 checklist）](./bathtub-filter-kes-content-ops-sop.md)

---

## 三、页面清单（Page Inventory）

> 每页固定填 5 块：`① problem 框定 → ② 用哪套 media 配置 → ③ 有界 claim（带🟢🟡🔴）→ ④ 承重护栏/disclaim → ⑤ 诚实劝退（能力外明说）`。下表给每页的归属 claim 区、必带护栏、关键 claim 证据状态、真理源指针。

### A. Hub · 简版产品介绍页

| 项 | 内容 |
|---|---|
| 主用 claim 区 | Transparency/clean-formula + Positioning（category-level） |
| 关键 claim 状态 | 「看得见的料」🟢；「这不是净水器·不降 TDS」🟢（**必须在**）；具体去氯数字 🔴 不上 Hub（留给 PDP/场景页，且待 Gate 1） |
| 必带承重句 | 「We won't tell you it 'treats' anything.」+「This is not a water purifier / doesn't target TDS.」 |
| 诚实劝退 | Match-Your-Water 选择器里对氯胺/软化/高铁/杀菌能力外**明说不适合 + 留邮箱** |
| 真理源 | [[bathtub-filter-kes-website-copy-v1]] 一、首页；[[bathtub-filter-kes-homepage-and-about-page-layout]] |

### B. 水场景配置页（Spoke A，一场景一页）

| 页 | 场景 | 配置（真理源=media 页） | 主 claim 区 · 状态 | 必带护栏 / 劝退 |
|---|---|---|---|---|
| **S1 游离氯·市政** | free chlorine municipal | 过滤棉（PET）→ KDF55 → CaSO₃（V1）（2026-07-02 按 [V1 BOM 表](../bathtub-filter-v1-free-chlorine-removal-dimensions-materials.md) 裁定更正滤棉材质） | Chlorine reduction（**free** chlorine, fresh-filter/best-experience, 15 L/min）🟢结构 / 具体数字🟡待 Gate 1 | 「free chlorine」限定词不可删；不认领氯胺/软化 |
| **S2 氯胺·市政** | monochloramine city | 过滤棉（PET）→ 催化炭 → 小层 KDF55 **＋抗坏血酸钠浸泡件**（V1.5 双段） | Chloramine — V1.5 only（Conditional）🟡 | **禁 fast/秒解**；按 4–8 min 讲；总氯试纸验证 + 抗坏血酸干扰时机；**"单芯不全除"**必说 |
| **S3 井水** | private well（低中度铁/H₂S） | 粗 PP → KDF85 → 催化炭（V1 well 线） | Well-water KDF85 模块（Conditional）🟡 | 高铁 >2–3 ppm 劝退；**禁**杀菌/除砷/硝酸盐/铀/全屋替代/软化 |
| **S4 硬水·水垢** | scale nuisance | +阻垢粒（附加层，非主 KPI） | Anti-scale adjunct（Conditional）🟡 | **「It does not soften your water.」必随行**；阻垢率=供应商自测；宗立卫生报告**禁入营销**（自送样 + 报告第 8 条） |
| **S5 沉积重**（可选/可并入 S3） | particulate-heavy | +强化 PP 层 | 物理拦截 🟢 | 不当主去污 KPI 讲 |

> S1 是唯一 🟢 结构成熟、应先做的主 SKU；S2–S4 是 🟡，页面可先写但 claim 标黄、且需各自台架/证据闭环才转 🟢。SKU 排序照 media-stack doc：A → B → C。

### C. 滤材独立页（Spoke B，一料一页 = 唯一真理源）

| 页 | 滤材 | 定位口径（**别写反**） | 关键 claim · 状态 | 必带护栏 |
|---|---|---|---|---|
| **M1 亚硫酸钙 CaSO₃** | 亚硫酸钙 | **游离氯去除主 KPI** | free chlorine 主力 🟢 | 不认领氯胺（V1）；数字待第三方 DPD |
| **M2 铜锌合金 KDF55** | KDF55 | **末端安全层 + 抑生物膜层**（非去氯主力） | NSF/ANSI 42 **料级** listing 🟢；EU 食品接触料级 🟢；抑菌=柱内 24h 🟡；除铅=静态浸泡 spec-sheet only 🟡 | **每处必带「成品未 NSF 认证」**；抑菌**禁**"杀浴缸水里的菌"；除铅**建议不进营销** |
| **M3 催化活性炭** | catalytic carbon | 氯胺 inline 主力（必要非充分） | Chloramine inline（Tier 1 机理）🟡 | 仅 V1.5；EBCT 不够 → 需配浸泡件 |
| **M4 抗坏血酸钠浸泡件** | sodium ascorbate | 浴缸停留段完成氯胺中和 | combined chlorine，4–8 min 🟡 | 禁"秒解"；总氯试纸 + 比色干扰时机 |
| **M5 KDF85** | KDF85 | 井水铁/硫/部分锰主力 | 低中度铁/H₂S/味 🟡 | 高铁劝退；禁除砷/硝酸盐/杀菌 |
| **M6 阻垢粒** | 陶瓷/晶球阻垢料 | **防垢附加层，非软化** | anti-scale（阻垢率供应商自测）🟡；安全=第三方 CMA ✅ 但**禁入广告** | **「不软化 / 不降硬度」必随行**；TDS 笔测不出变化=正常（正证没在软化） |
| **M7 过滤棉（PET）** | PET 聚酯纤维沉积棉 | 物理前置层 | 颗粒拦截 🟢 | **不是"活性成分"**——修正 Hub 的"just two ingredients"→"两种活性 media + 一层物理前置" |

> 提醒：这层直接修掉当前视觉稿两个矛盾——① KDF55 别写成"去氯主力"（写"安全层"），CaSO₃ 才是主力；② 有了 M7 独立页，"no third thing / 只有两样"必须诚实改口。

### D. 方法/信任页（Spoke，共享引用）

| 页 | 内容 | claim 区 · 状态 | 必带护栏 |
|---|---|---|---|
| **T1 水质自测 / 试纸页** | ZIP→CCR（类型，权威）+ 多垫试纸（浓度/硬度，粗筛） | Self-diagnosis 🟢 | 「粗筛指路 ≠ 检测危害」；类型判定以 ZIP 为准；**禁 TDS 笔/铅试纸**；**禁 toxin-panic** |
| **T2 我们怎么测 / 认证页** | NSF/ANSI 42 **料级** + **成品未认证**免责 + DPD 报告 + 25 L/min 台架说明 | Performance/testing 🟢结构 / 25 L/min 数字🟡待 Gate 1 | "for safety and performance"这类会读成成品认证的措辞去掉；性能口径回 **15 L/min**，25 L/min 仅作最大通过流量 |
| **T3 更换 / 寿命页** | 更换触发（99→95→90→80→<50%）+ 验证 | Replacement-trigger + Verification 🟢 | 用 **baths/gallons 不用月**；「你家氯浓度影响寿命，用试纸验证」；**50,000 L 裸容量数需溯源**（≈ 重算后内部模型 ~21,550 L @2 ppm 的 2.3 倍；2026-07-02 按 BOM 裁定重算） |

### E. 产品结构 / 工业设计页（Spoke D · 2026-07-01 新增）

> 补「产品本体」这一层——clean-honest 母题的**物理载体**。客户页 D1–D4 + 1 个内部 IP/专利治理页（措辞规则真理源，喂 claim-register）。**专利红线**：只能 "Patent pending" 🟡（须受理文件），🔴 禁 "patented/专利技术/获专利"。

| 页 | 内容 | claim 区 · 状态 | 必带护栏 |
|---|---|---|---|
| **D1 结构总览** | 3 设计原则 + 结构分解图 + 规格表（收编视觉稿 Technical Details） | Structure/engineering 🟢 | 定位承重句随行；NPT 🟡待查；更换/性能口径引 T2/T3 |
| **D2 导流模块 / 防沟槽** | CaSO₃ 层 operational requirement（防中心冲蚀）；分层不混 vs mixed-bead | Structure 🟢 / Patent-pending 🟡 | **"Patent pending"须受理文件(🟡)，🔴禁 patented/专利技术**；解释设计非贬竞品 |
| **D3 透明滤仓** | clean-honest 物理实现、可替换、材质 | Transparency 🟢 | **可见≠更有效**（trust 钩子，非 efficacy） |
| **D4 扁硅胶挂带 / 适配** | 21mm 宽带 + 兼容矩阵 S-01~S-08 + 墙距边界 | Fit/compatibility 🟢结构 / 部分实测🟡 | **🔴禁 通用/所有浴缸适配**；每条兼容带"不支持"边界；无溢水 35 L/min |
| **结构·IP/专利治理页（内部）** | IP 事实库 + 措辞规则表 + FTO 状态 | 内部治理（喂 claim-register） | patent-pending 只以受理文件为准；CaSO₃+KDF 非 KES 专有；FilterBaby FTO 未决 🟡 |

### F. 消费者水质科普页（Spoke E · 2026-07-01 新增）

> 补「消费者背景知识」层——帮对水质一无所知的零售消费者搞懂"我家水什么情况、该买哪个"。大部分由现有内部研究直接转化（0 新研究）。**E6 是全站最高合规风险页**（氯-皮肤），须 comfort-first、禁 eczema/toxin-panic。

| 页 | 内容 | 素材源 · 新研究 | 护栏 |
|---|---|---|---|
| **E1 游离氯 vs 氯胺地理** | 城市消毒剂分布 + 怎么查（ZIP→CCR） | metro-map + disinfectant-guide · 0 | 禁 toxin-panic；链 S1/S2 |
| **E2 井水必读** | 井水污染物 vs 市政 + 何时需专业系统 | well-water-research · 0 | 砷/菌需专业系统明说；不恐吓 |
| **E3 硬水地图 + 单位** | 硬水带 + gpg/mg-L/ppm | metro-map + na-water-profile · 0 | comfort 口径；链 S4/E8 |
| **E4 术语表** | 游离氯/总氯/氯胺/ppm/硬度/TDS | disinfectant-guide · 0 | 本簇术语真理源 |
| **E5 怎么测洗澡水 + 置信度** | 试纸/TDS笔各测什么 | test-methods · 0 | **禁 TDS 笔当去氯验证**；防差评 |
| **E6 氯值得在意吗** | 氯-皮肤诚实对话 | academic evidence · 0 | 🔴**最高**·comfort-first、禁 eczema/健康恐吓 |
| **E7 怎么读 CCR** | CCR 是什么/怎么读 | institutional-guidance · 🟡需样例 CCR | 官方中立、链 EPA |
| **E8 软水器家庭** | 软水器不去氯 | water-source-types · 0 | 纯教育、不侵略竞品 |

### G. 产品 / 运营文档页（P · 2026-07-01 新增）

| 页 | 内容 | 状态 | 备注 |
|---|---|---|---|
| **P1 V1 定义与「不适用」清单** | primary-source：V1 是什么 + 不支持清单（氯胺/井水/软化/健康） | 🟢（消化 raw 讲解原件） | 双向溯源 raw 原件；"为什么这么选"的真理源 |
| **P2 Pack-contents 规格** | 套装配件正式清单 | 🟢部分 / 🟡缺项 | 供 PDP/说明书/包装引用 |
| **P3 使用与维护指南** | 防霉/清洁/更换/排查树 | 🟢（消化竞品评论洞察） | 直接降退货；换芯口径引 T3 |

> **更新（2026-07-01 下批）**：安装说明书 → 已建 **P4 安装与兼容性指南**；退货保修/订阅/referral/客服/定价/proof → 已建为 **SVC 占位骨架页**（见 §H），结构就位、事实待业务补。仍纯待外部事实：BOM/COGS(财务)、Prop65 最终标签措辞(法务)、"如何读第三方报告"页(待 Gate 1 报告)。

### H. 补充科普 + 服务/交易层（2026-07-01 下批新增）

> 覆盖度审计（对照全 wiki）后补的两类：① 之前漏的**产品边界科普**（PFAS/流速权衡/特殊水源）；② 整个**服务/交易层**（转化漏斗 + 售后）。**软化决策同步硬化：本产品不做软化，硬水只提供阻垢剂选项。**

| 页 | 类型 | 状态 | 护栏 / 备注 |
|---|---|---|---|
| **E9 PFAS 诚实边界** | 科普 | 🟢 实质 | 🔴 禁"催化炭除 PFAS"；诚实说"我们不除、需 RO/IX" |
| **E10 流速 × 去氯/寿命** | 科普 | 🟢 结构 / 数字🟡 | 快注水→去氯↓寿命↓；数字待 Gate 1 |
| **E11 特殊水源（RO/SCWS/雨水）** | 科普 | 🟢 实质 | RO 用户主动劝退；🔴 不做软化 |
| **P4 安装与兼容性指南** | 产品 | 🟢结构 / 矩阵🟡 | 三安装路线 + spout 矩阵(部分待 Gate 2) + AVB；🔴禁通用适配 |
| **SVC1 买前 FAQ** | 服务 | 🟢 实质 | 收敛 P1+S1–S5；软化=不做只阻垢、PFAS 不除、不 baby-safe/eczema |
| **SVC2 买后验证** | 服务 | 🟢 半实质 | 试纸前后对比；referral 时序待补 |
| **SVC3 退货/保修** | 服务 | ⚠️ 占位 | 条款 `[____]` 待法务/运营 |
| **SVC4 补芯订阅方案** | 服务 | 🟢 方案结构 / 价格`[____]` | **Skip-if-still-good**：发货前提醒先测、达标一键跳过——复购靠"你自己测到该换"非黑箱倒计时；周期/暂停/取消无障碍；价格待运营 |
| **SVC5 Referral 方案** | 服务 | 🟢 方案结构 / 奖励`[____]` | **分享试纸卡 ×3（提案，见 P2 #10）**：独立封装卡（试纸+读色说明+唯一二维码）→朋友扫码 ZIP 诊断→适配建议或诚实劝退（劝退=V1.5 候补获客）；双触发（开箱+T+10–14 验证邮件）；🔴 禁 toxin-panic |
| **SVC9 Bundle/多件装** | 服务 | 🟢 结构 / 价格`[____]` | Starter / First-Year Kit / Refill 多件 / Gift bundle；**让利逻辑诚实**（省的是包装物流获客成本，如实让）；🔴 禁虚划线/scarcity/best-value |
| **SVC6 客服联系** | 服务 | ⚠️ 占位 | 渠道/SLA `[____]` 待运营 |
| **SVC7 定价/Refill 经济学** | 服务 | ⚠️ 占位 | 价格 `[____]` 待财务；clean-honest 不隐藏定价 |
| **SVC8 社会证明** | 服务 | ⚠️ 占位 | 真实素材 `[____]` 待市场；🔴 testimonials 禁 eczema/软化/PFAS/恐吓 |

### I. 基建 / 渠道 / 运维层（2026-07-02 终审补建）

> 三路终审（一致性/机械全扫/缺口批判）后补的"从没建的节点"：邮件幽灵中枢、隐私法律底座、三个渠道规格、运维 SOP。

| 页 | 类型 | 状态 | 备注 |
|---|---|---|---|
| **SVC11 邮件生命周期 spec** | 基建 | 🟢 实质 | **全站邮件时点唯一 owner**（referral/买后验证/订阅/劝退候补此前循环引用无主，现统一引本页）；8 类触发全表 |
| **SVC12 隐私/ToS/同意/a11y** | 基建 | ⚠️ 占位·**法律上线阻断项** | 数据地图 + WCAG 基线可写实；条款 `[____]` 待法务——全站采邮箱/归因/埋点，无此页不得上线 |
| **CH1 Amazon listing 规格** | 渠道 | 🟢 结构 | title/五点/A+/搜索词/Q&A 预置/差评预防映射；🔴 禁 universal/氯胺蹭词 |
| **CH2 印刷 IFU 规格** | 渠道 | 🟢 结构 | 盒内印刷说明书版式（竞品第一差评源反制资产）；内容全引 P3/P4/T3 不新造 |
| **CH3 移动端/响应式规格** | 渠道 | 🟢 结构 | 选购器/生成器/Hub/PDP 四表面；首屏承重句不折叠 |
| **OPS1 运维 SOP** | 运维 | 🟢 实质 | 新页模板/claim 审批链/🟡→🟢 销项流程/**数字改动传播 checklist**（BOM 裁定案例化）/月度巡检 |

---

## 四、导航 / 互链模型

- **入口收口**：冷流量落 Hub → Match-Your-Water 选择器 → 对应 S1–S4 场景页 → PDP 购买。
- **场景页 → 滤材页**：每个 S 页在"用哪套配置"处链到它引用的 M 页（如 S1 → M1/M2/M7；S2 → M3/M4/M2/M7）。
- **滤材页 → 场景页**：每个 M 页底部反链"用到我的场景"（如 M2 KDF55 → S1/S2/S3）。
- **全站 → 方法页**：任何提到"怎么验证 / 认证 / 换芯"的地方链到 T1/T2/T3，不在场景页里重复口径（避免口径漂移）。
- **自有站 → 外部层**：评测/社区不自建，指针到 [[bathtub-filter-content-ecosystem-by-layer]]。

> 单一真理源规则：**去氯数字只在 T2 定义一次、其他页引用**；**认证口径只在 T2 定义一次**；**每种 media 的 claim 只在对应 M 页定义一次**。场景页/ Hub / PDP 全部引用，不各写各的——这是防 claim 漂移的核心机制。

---

## 五、内容页 → 产品定义的倒推方法

填完上面每页后，SKU spec 按下式自动收敛（对接 media-stack doc 文末点名的三个配套页）：

1. **SKU 定义** = 场景页 ②配置 + ③里所有 🟢 claim（🟡 进 roadmap 不进首发文案）
2. **SKU 验证清单** = 每页所有 🟡 claim 的转正测试（S1 的 25 L/min→Gate 1 DPD；S2 的 with/without soak；S4 的实际出货粒径阻垢复核…）
3. **前端分流逻辑** = T1 自测页的 ZIP+试纸判定 → 路由到 S1/S2/S3/S4 或劝退
4. **包装/说明书** = 从 T3（更换/验证口径）+ 场景页承重护栏反推印刷内容

即：**先把站写对 → SKU 定义、测试清单、包装文案是站的投影**，而不是反过来先拍产品再补文案（那样最容易写出兑不了现的 claim）。

---

## 六、施工顺序（建议）

1. **本页（总架构）** ✅ — 先落地，作蓝图
2. **T2 我们怎么测/认证页** ✅ — 先定"去氯数字/认证/25→15 L/min"单一口径，后面所有页引用它，避免返工
3. **M1 + M2 两个滤材页** ✅ — 验证"证据标签 + 真理源"模式好不好用（呼应"测试后再推广"），再批量复制到 M3–M7
4. **S1 游离氯场景页** ✅ — 唯一 🟢 主 SKU，跑通"场景→配置→有界 claim→劝退"五段模板
5. 批量填 S2–S5、M3–M7、T1/T3 ✅
6. **Hub 收口** — ⚠️ **更正**：Hub 文案（[[bathtub-filter-kes-website-copy-v1]]）经核**已合规**（氯胺="Not this version"、逐层列出 polyester (PET) fiber、KDF55=safety layer/CaSO₃=primary workhorse、NSF 成品未认证免责、15 L/min + 去氯数字占位）。上轮 5 个合规问题**是视觉执行稿脱离该文案造成的**，不是文案的锅。所以收口动作是**让视觉设计稿回到 website-copy-v1 的口径**，而非回改文案。

### 构建状态（2026-06-30）

全部 15 个 spoke 页 + 本地图已建成并通过自审（禁用词 / 承重句 / 互链解析 / 无杜撰证据 / 口径一致，见 [[bathtub-filter-kes-marketing-site-content-map]] 无 broken link）。四簇分工：方法页 T1–T3｜游离氯簇 M1/M2/M7/S1/S5｜氯胺簇 M3/M4/S2｜井水+阻垢簇 M5/M6/S3/S4。自审发现的两处**既有文档**待修项：① CP210620 `../../raw/` 坏链 ✅ **已修**（2026-07-01，claim-register + feasibility 两处，全站链接扫描 0 broken）；② ascorbate-chloramine-kinetics-research-2026-06.md 把 Peskin & Winterbourn 误署为 Tikkanen —— 🟡 **仍待修**（需核原始文献后订正，owner：产品/研究）。

---

## 上线前合规自检（照 register 表面→claim 映射）

每页 ship 前逐条过 [[bathtub-filter-claim-register]] §D 表面→claim 映射对应行；本轮从当前视觉稿已抓到的 5 个触发项（氯胺认领、NSF 成品误读、25 L/min 上首屏、50,000 L 溯源、"两种料"矛盾）全部转成上表护栏，逐页 ship 时核销。

---

## Sources / 内部依据

- [Claim register（Banned/Conditional/Allowed + 表面→claim 映射）](../bathtub-filter-claim-register.md)
- [按水源类型的滤材方案（A/B/C SKU）](../bathtub-filter-kes-media-stack-options-by-water-type.md)
- [完整网站文案 v1（Homepage+PDP+About）](../bathtub-filter-kes-website-copy-v1.md)
- [首页+About 落地版式](../bathtub-filter-kes-homepage-and-about-page-layout.md)
- [就地软水可行性（三路线边界 §8）](../bathtub-filter-point-of-use-hardness-softening-feasibility.md)
- [水质自测套件 / 模块化获客引擎](../bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md)
- [V1 执行路线图（Gate 1）](../bathtub-filter-kes-v1-execution-roadmap-2026-06-15.md)

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-kes-media-stack-options-by-water-type]]
- [[bathtub-filter-kes-website-copy-v1]]
- [[bathtub-filter-kes-homepage-and-about-page-layout]]
- [[bathtub-filter-point-of-use-hardness-softening-feasibility]]
- [[bathtub-filter-content-ecosystem-by-layer]]
- [[bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine]]
- [[bathtub-filter-kes-v1-execution-roadmap-2026-06-15]]
