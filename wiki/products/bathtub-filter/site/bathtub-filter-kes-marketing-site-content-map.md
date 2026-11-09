---
type: product
status: draft
owner: strategy
created: 2026-06-30
updated: 2026-07-14
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, content-architecture, information-architecture, site-map, marketing, claims, free-chlorine, chloramine, well-water, custom-formula, anti-scale, diagnosis-kit]
source_count: 8
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
  - ./bathtub-filter-kes-hub-design-review-2026-07-14.md
---

# KES 浴缸过滤器 · 自有营销站内容地图（Hub-and-Spoke IA）

## 为什么有这页

现有文档已经分别覆盖了：

- **单一表面文案/版式**：[[bathtub-filter-kes-website-copy-v1]]（Homepage + PDP + About 完整文案）、[[bathtub-filter-kes-homepage-and-about-page-layout]]（首屏版式）
- **产品/滤材逻辑**：[[bathtub-filter-kes-media-stack-options-by-water-type]]（三套标准配方 + 一个 guided custom → media → structure → claim/禁）
- **claim 护栏**：[[bathtub-filter-claim-register]]（Banned / Conditional / Allowed + 表面→claim 映射）
- **外部内容层**：[[bathtub-filter-content-ecosystem-by-layer]]（评测/媒体/社区）

但需要一张把多页串起来的总图：**交易型 Hub → 四个购买出口 → 结构/滤材/测试等决策证据 Spoke → 教育与售后层**，并明确每个点击点、返回购买器规则、内容 owner、claim 状态和公开/内部边界。这页承担这个总调度角色，不重复各页面正文。

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

三套标准水源配方 = 三个 problem = 三套独立 claim；第四个 Build Your Formula 只允许组合这些已批准模块的 claim 交集。任何一页不得拿 Free-Chlorine 的证据替 Chloramine、Well-Water 或自定义成品 claim 背书。滤材页是料级真理源，性能数字仍以完整成品组合测试为准。

---

## 二、优化后的站点地图（Hub-and-Spoke）

### 2.1 核心结构

```
┌──────────────────────────────────────────────────────────────────┐
│ HUB · /bathtub-filter                                            │
│ clean-formula 情感冲突 → 四版本购买器 → 产品证据摘要 → 就地加购 │
└──────────────┬───────────────────────────────────────────────────┘
               │
        ┌──────▼──────────────────────────────────────────┐
        │ 决策 / 交易层                                   │
        │ SVC10 Water Match → S1 / S2 / S3 / SVC13       │
        │ 三个标准 Formula PDP + 一个 guided custom      │
        └──────┬──────────────────────────────────────────┘
               │ 双向深链；始终保留 selected_formula
   ┌───────────┼───────────────────┬────────────────────────┐
   │           │                   │                        │
┌──▼──────┐ ┌──▼────────┐     ┌────▼───────┐          ┌────▼────────┐
│ 产品证据 │ │ 水质教育   │     │ 服务与售后  │          │ 外部内容层   │
│ D / M / T│ │ E / S4/S5 │     │ P / SVC     │          │ 评测/社区     │
└─────────┘ └───────────┘     └────────────┘          └─────────────┘
```

### 2.2 每层只承担一个角色

| 层 | 页面角色 | 核心任务 | 不应该做 |
|---|---|---|---|
| **Hub** | 主交易页 + 品类定位页 | 首屏建立 clean-formula / black-box 差异；第二屏完成四版本选择和购买；后续摘要回答关键疑问 | 不写成纯品牌故事；不复制所有 spoke 正文 |
| **Water Match / Configurator** | 决策工具 | 根据水源、ZIP/CCR、井水红旗与附加问题返回合法版本或 `formula_id` | 不注册后才能看结果；不绕过 claim/红旗规则 |
| **Formula PDP** | 标准版本购买页 | 解释当前配方、结构、适配、测试、价格、套装内容并购买 | 不另建一套与场景页重复的 PDP 文案 |
| **Evidence Spoke** | 单问题深度证明 | 一页只回答一个高意图问题：材料、结构、水路、流速、适配、测试或寿命 | 不自己创造价格、数字或跨配方 claim |
| **Education Spoke** | 上游发现与诚实分流 | 解释水质、术语、CCR、井水/硬水边界，并导向 Water Match 或正确 Formula | 不用恐吓制造需求；不把教育页做成强卖页 |
| **Service / Aftercare** | 降低购买与使用阻力 | FAQ、内容物、安装、维护、验证、补芯、退保和客服 | 不重复定义产品性能 |

### 2.3 页面合并与去重决定

- **S1、S2、S3 同时是场景真理源和三个标准 Formula PDP 的内容 owner**。公开站只建一个对应 URL，不再另外创建“场景介绍页 + PDP”两套近似页面。
- **S4 硬水、S5 沉积重不是独立主机 SKU PDP**。它们是 Water Match / Build Your Formula 的附加问题解释页，负责说明可加模块与能力边界。
- **SVC13 是第四个购买出口**，但不是任意选料商城；它只生成白名单结构、固定层序和合法 `formula_id`。
- **M/D/T 页面是证据 Spoke，不承担主购买叙事**。页面可以显示当前选中 Formula 的 sticky cart，但主 CTA 是返回已选配方。
- **P5、CH1–CH3、OPS1、结构 IP 页为内部规格，不公开进入消费者导航**。
- **外部评测/社区不复制到自有站**，统一由 [[bathtub-filter-content-ecosystem-by-layer]] 管理。

### 2.4 建议公开 URL 与 wiki owner

| 公开页面 | 建议 URL | 唯一 wiki owner |
|---|---|---|
| Bathtub Filter Hub | `/bathtub-filter` | 本页 + [[bathtub-filter-kes-website-copy-v1]] |
| Water Match | `/bathtub-filter/match` | [SVC10](./bathtub-filter-kes-water-match-selector-spec.md) |
| Free-Chlorine Formula PDP | `/bathtub-filter/free-chlorine` | [S1](./bathtub-filter-kes-scenario-free-chlorine.md) |
| Chloramine + Soak Kit PDP | `/bathtub-filter/chloramine` | [S2](./bathtub-filter-kes-scenario-chloramine.md) |
| Well-Water Formula PDP | `/bathtub-filter/well-water` | [S3](./bathtub-filter-kes-scenario-well-water.md) |
| Build Your Formula | `/bathtub-filter/custom` | [SVC13](./bathtub-filter-kes-custom-formula-builder-spec.md) |
| How It Works / exploded structure | `/bathtub-filter/how-it-works` | [D1](./bathtub-filter-kes-structure-overview.md) |
| Engineered Flow | `/bathtub-filter/how-it-works/engineered-flow` | [D2](./bathtub-filter-kes-structure-flow-diversion-module.md) |
| Transparent Formula | `/bathtub-filter/how-it-works/transparent-formula` | [D3](./bathtub-filter-kes-structure-transparent-housing.md) + M1–M7 |
| Fit Guide | `/bathtub-filter/fit` | [P4](./bathtub-filter-kes-install-and-compatibility-guide.md) |
| How We Test | `/bathtub-filter/testing` | [T2](./bathtub-filter-kes-page-how-we-test-and-certify.md) |
| Test Your Water | `/bathtub-filter/test-your-water` | [T1](./bathtub-filter-kes-page-water-test-diagnosis.md) + [E5](./bathtub-filter-kes-edu-how-to-test-your-water.md) |
| Replacement & Lifespan | `/bathtub-filter/replacement` | [T3](./bathtub-filter-kes-page-replacement-and-lifespan.md) |
| FAQ | `/bathtub-filter/faq` | [SVC1](./bathtub-filter-kes-faq-is-kes-right-for-you.md) |
| Refill | `/bathtub-filter/refill` | [SVC4](./bathtub-filter-kes-refill-subscription.md) |

---

## 页面索引（本图 + 53 个内容/运营节点）

> 从本图直达 53 个已建节点，按方法 T / 滤材 M / 场景与 Formula S / 结构 D / 科普 E / 产品 P / 服务 SVC / 渠道 CH / 运维 OPS 分组。[Hub Design Review](./bathtub-filter-kes-hub-design-review-2026-07-14.md) 是评审输入，[53 页面内容审计](./bathtub-filter-kes-page-content-audit-2026-07-14.md) 记录逐页优化与上线阻断；两者均不计入公开内容节点。

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

- [P1 · 四版本产品定义与「不适用」清单（primary-source）](./bathtub-filter-kes-v1-definition-and-not-for-list.md)
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
- [SVC13 · Build Your Formula 自定义配方器](./bathtub-filter-kes-custom-formula-builder-spec.md)

**渠道规格页（CH · 2026-07-02 新增）**

- [CH1 · Amazon listing 规格](./bathtub-filter-kes-amazon-listing-spec.md)
- [CH2 · 印刷版说明书 IFU 规格](./bathtub-filter-kes-print-ifu-spec.md)
- [CH3 · 移动端 / 响应式规格](./bathtub-filter-kes-mobile-responsive-spec.md)

**系统运维（OPS）**

- [OPS1 · 内容系统运维 SOP（新页/审批/销项/传播 checklist）](./bathtub-filter-kes-content-ops-sop.md)

---

## 三、页面清单（Page Inventory）

> 每页固定填 5 块：`① problem 框定 → ② 用哪套 media 配置 → ③ 有界 claim（带🟢🟡🔴）→ ④ 承重护栏/disclaim → ⑤ 诚实劝退（能力外明说）`。下表给每页的归属 claim 区、必带护栏、关键 claim 证据状态、真理源指针。

### A. Hub · 主交易与品类定位页

| 项 | 内容 |
|---|---|
| 页面任务 | 让用户在第一屏理解 KES 为什么不同，在第二屏完成版本选择与购买；其后用证据摘要解除材料、结构、流速、适配、验证和更换疑虑 |
| 主用 claim 区 | Transparency/clean-formula + Structure/flow + Formula match；不使用 skin/hair outcome 作为主转化 |
| 关键 claim 状态 | 「看得见的料/层序」🟢；结构与导流逻辑🟢；具体 performance 数字按 T2 状态；未经闭环数字不进 Hero |
| 必带承重句 | `We won't tell you it "treats" anything.` + `This is not a water purifier / doesn't target TDS.` |
| 首发购买路由 | S1 Free-Chlorine / S2 Chloramine + Soak / S3 Well-Water / SVC13 Build Your Formula；前三者原位加购，井水先过红旗筛查，自定义生成合法 `formula_id` 后加购 |
| 真理源 | [[bathtub-filter-kes-website-copy-v1]]、[Hub Design Review](./bathtub-filter-kes-hub-design-review-2026-07-14.md)、[[bathtub-filter-kes-homepage-and-about-page-layout]] |

#### Hub 屏序与深链

Hub 每个模块使用同一最小结构：**一个购买问题 → 一句结论 → 一个真实证据视觉 → 一个边界 → 一个明确深链或交易动作**。不得恢复成四个泛 icon 或 lifestyle result 图。

| 屏序 | 用户问题 / 商业任务 | 主要文字与视觉 | 点击和交易行为 | wiki owner |
|---|---|---|---|---|
| **1 Hero** | 为什么不是普通 bath filter？ | `You check every ingredient. Why bathe through a black box?` + 透明滤仓近照 + 安装出水状态；三条事实 `See every layer / Engineered flow path / Test it yourself` | `Shop your formula` → `#choose-your-formula`；`Check your water` → SVC10；产品近照 → D3；三条事实分别 → D3/D2/E5 | Website Copy + Hub Design Review + D2/D3/E5 |
| **2 Choose your formula** | 我应该买哪一个？能否现在下单？ | 四 tab/四卡，显示适用水质、真实层序、试纸、价格、fit 状态、套装/补芯范围 | S1/S2 直接 Add to cart；S3 红旗筛查后加购；SVC13 生成 `formula_id` 后加购；`Not sure?` → SVC10；`Check my spout` → P4 | S1/S2/S3/SVC10/SVC13/P2/P4/SVC7 |
| **3 Visible clean formula** | 里面到底装了什么？ | 透明滤仓实拍；材料名、用量、层序、作用与不认领项；版本切换同步更新 | 整体图 → D3；每种材料名称/近照 → 对应 M 页；CTA `See every material and its role` → D3 | D3 + M1–M7 |
| **4 Exploded walkthrough** | 每一步如何工作？ | BOM 对齐的纵向爆炸图：挂带/入口/铺流/前置/分仓/导流/出口/试纸或 soak accessory | 整图 → D1；部件 hotspot → D4、M1–M7、D2；当前 formula 切换时换图 | D1 + P2 + D4 + M1–M7 |
| **5 Engineered flow** | 水真的经过滤材，还是从缝隙绕走？ | KES 分仓铺流剖面；与 generic mixed-bed shortcut 示意并列；讲 flow distribution/contact path，不直接推导去除率 | 标题与水路图 → D2；`See how we test the flow path` → T2 | D2 + T2 |
| **6 Bath-filling flow** | 会不会慢得无法正常放满浴缸？ | 实际注水视频；解释 flow/contact-time/pressure-drop 平衡；数字只引用 T2 | 视频/标题 → E10；`See the test method` → T2 | E10 + T2 |
| **7 Fits your spout** | 能装在我家出水嘴上吗？ | `Fits directly / Fits with included support / Not compatible` 三类真实 spout 图与关键尺寸 | 每张图 → P4 对应锚点；`Check my spout` 打开 checker；挂带特写 → D4；fit 结果同步购买器 | P4 + D4 |
| **8 Test and replace honestly** | 怎么知道有效、什么时候更换？ | formula-specific 试纸 before/after + `Replace by baths, not months` + 使用次数/结果触发 | 试纸图 → E5；验证 CTA → SVC2；更换句 → T3；`Get the right refill` → SVC4 | T1/E5/SVC2/T3/SVC4 |
| **9 Boundaries and proof** | 哪些能做、哪些不能做？依据是什么？ | 简短 not-for 清单、测试/认证事实、真实评价占位；不得用 skin/hair before-after | FAQ → SVC1；能力边界 → P1；测试 → T2；评价仅在 SVC8 有真实素材后上线 | SVC1/P1/T2/SVC8 |
| **10 Story and service** | 我是否信任这个品牌，买后怎么办？ | 唯一一次 Our Story + support/returns/refill；Our Commitment 下移且只写有事实 owner 的内容 | `Read our story` → About；Support → SVC6；Returns → SVC3；Refill → SVC4；无 sustainability owner 前不设空链接 | Homepage/About + SVC3/SVC4/SVC6 |

**屏序约束**：Screen 1–2 是转化承重区，不插入 `Our Story`、环保承诺、评价轮播或大段科普。Screen 3–8 依次回答材料、结构、水路、流速、适配、验证六个产品问题。品牌故事只能在这些问题回答后出现。

**爆炸图与防沟槽必须分开**：爆炸图回答「里面有什么、每一步做什么」；Engineered Flow 回答「为什么水会真实经过这些料」。相邻呈现，但不合成一张无法同时读清的泛结构图。

#### Hub 购买状态模型

| 状态 | 保存内容 | 离开 Hub 进入 spoke 后 | 返回 Hub |
|---|---|---|---|
| `selected_formula` | `free_chlorine / chloramine / well_water / custom:{formula_id}` | 作为 URL/session 参数透传，spoke 的 sticky CTA 显示同一版本 | 回到 `#choose-your-formula` 或原阅读位置，版本不重置 |
| `fit_status` | `pass / conditional / fail / unchecked` + spout type | 所有购买 CTA 可读取；`fail` 不允许用普通提示掩盖 | 购买卡显示原状态；改变版本后重新校核重量/配件规则 |
| `water_match` | source/type/confidence/red flags | Formula PDP 显示推荐理由，不把推断写成实验室检测 | 购买器将推荐版本置顶，但仍允许查看其他版本边界 |
| `cart_context` | starter/refill/subscription + quantity | 内容 deep link 不清空 cart | sticky cart 保持可见；不得要求重新配置 |

### B. 水场景配置页（Spoke A，一场景一页）

| 页 | 场景 | 配置（真理源=media 页） | 主 claim 区 · 状态 | 必带护栏 / 劝退 |
|---|---|---|---|---|
| **S1 游离氯·市政** | free chlorine municipal | 过滤棉（PET）→ KDF55 → CaSO₃（V1）（2026-07-02 按 [V1 BOM 表](../bathtub-filter-v1-free-chlorine-removal-dimensions-materials.md) 裁定更正滤棉材质） | Chlorine reduction（**free** chlorine, fresh-filter/best-experience, 15 L/min）🟢结构 / 具体数字🟡待 Gate 1 | 「free chlorine」限定词不可删；不认领氯胺/软化 |
| **S2 氯胺·市政** | monochloramine city | 过滤棉（PET）→ 催化炭 → 小层 KDF55 **＋抗坏血酸钠浸泡件**（首发双段 SKU） | 产品推出已确认；具体 Chloramine reduction claim 仍 Conditional 🟡 | 与 S1 并列可购买；**禁 fast/秒解**；按 4–8 min 讲；总氯试纸验证 + 抗坏血酸干扰时机；**"单芯不全除"**必说 |
| **S3 井水** | private well（低中度铁/H₂S） | 粗 PET → KDF85 → 催化炭（首发 Well-Water Formula） | 产品推出已确认；具体 Well-water performance claim 仍 Conditional 🟡 | 与 S1/S2 并列可购买；高铁 >2–3 ppm 劝退；**禁**杀菌/除砷/硝酸盐/铀/全屋替代/软化 |
| **S4 硬水·水垢** | scale nuisance | +阻垢粒（附加层，非主 KPI） | Anti-scale adjunct（Conditional）🟡 | **「It does not soften your water.」必随行**；阻垢率=供应商自测；宗立卫生报告**禁入营销**（自送样 + 报告第 8 条） |
| **S5 沉积重**（可选/可并入 S3） | particulate-heavy | +强化 PP 层 | 物理拦截 🟢 | 不当主去污 KPI 讲 |

> S1 是当前唯一 🟢 性能证据较成熟的路线；S2 氯胺套装与 S1 同步首发，但具体性能 claim 仍为 🟡，须经专属台架/证据闭环才转 🟢。S3–S4 继续按各自状态管理。**首发并列不代表证据等级相同。**

### C. 滤材独立页（Spoke B，一料一页 = 唯一真理源）

| 页 | 滤材 | 定位口径（**别写反**） | 关键 claim · 状态 | 必带护栏 |
|---|---|---|---|---|
| **M1 亚硫酸钙 CaSO₃** | 亚硫酸钙 | **游离氯去除主 KPI** | free chlorine 主力 🟢 | 不认领氯胺（V1）；数字待第三方 DPD |
| **M2 铜锌合金 KDF55** | KDF55 | **末端安全层 + 抑生物膜层**（非去氯主力） | NSF/ANSI 42 **料级** listing 🟢；EU 食品接触料级 🟢；抑菌=柱内 24h 🟡；除铅=静态浸泡 spec-sheet only 🟡 | **每处必带「成品未 NSF 认证」**；抑菌**禁**"杀浴缸水里的菌"；除铅**建议不进营销** |
| **M3 催化活性炭** | catalytic carbon | 氯胺 inline 主力（必要非充分） | Chloramine inline（Tier 1 机理）🟡 | 仅 Chloramine + Soak Kit；EBCT 不够 → 需配浸泡件 |
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
| **P1 产品定义与「不适用」清单** | primary-source：一个平台、四个购买版本 + 各版本不支持项（软化/高铁/杀菌/健康等） | 🟢结构 / 各性能证据分级 | 双向溯源 raw/decision register；"为什么这样分版本"的真理源 |
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
| **SVC5 Referral 方案** | 服务 | 🟢 方案结构 / 奖励`[____]` | **分享试纸卡 ×3（提案，见 P2 #10）**：独立封装卡（试纸+读色说明+唯一二维码）→朋友扫码诊断→匹配 S1/S2/S3 或合法自定义 `formula_id`；能力外照常劝退；🔴 禁 toxin-panic |
| **SVC9 Bundle/多件装** | 服务 | 🟢 结构 / 价格`[____]` | Starter / First-Year Kit / Refill 多件 / Gift bundle；**让利逻辑诚实**（省的是包装物流获客成本，如实让）；🔴 禁虚划线/scarcity/best-value |
| **SVC6 客服联系** | 服务 | ⚠️ 占位 | 渠道/SLA `[____]` 待运营 |
| **SVC7 定价/Refill 经济学** | 服务 | ⚠️ 占位 | 价格 `[____]` 待财务；clean-honest 不隐藏定价 |
| **SVC8 社会证明** | 服务 | ⚠️ 占位 | 真实素材 `[____]` 待市场；🔴 testimonials 禁 eczema/软化/PFAS/恐吓 |

### I. 基建 / 渠道 / 运维层（2026-07-02 终审补建）

> 三路终审（一致性/机械全扫/缺口批判）后补的"从没建的节点"：邮件幽灵中枢、隐私法律底座、三个渠道规格、运维 SOP。

| 页 | 类型 | 状态 | 备注 |
|---|---|---|---|
| **SVC11 邮件生命周期 spec** | 基建 | 🟢 实质 | **全站邮件时点唯一 owner**（referral/买后验证/订阅/覆盖通知此前循环引用无主，现统一引本页）；四个首发版本不使用候补名单 |
| **SVC12 隐私/ToS/同意/a11y** | 基建 | ⚠️ 占位·**法律上线阻断项** | 数据地图 + WCAG 基线可写实；条款 `[____]` 待法务——全站采邮箱/归因/埋点，无此页不得上线 |
| **SVC13 Build Your Formula** | 交易/配置 | 🟢 规则结构 / 组合测试🟡 | 第四首发购买入口；只生成白名单模块、固定顺序与 `formula_id`；每个可售组合须单独过 flow/pressure/claim 校核 |
| **CH1 Amazon listing 规格** | 渠道 | 🟢 结构 | title/五点/A+/搜索词/Q&A 预置/差评预防映射；🔴 禁 universal/氯胺蹭词 |
| **CH2 印刷 IFU 规格** | 渠道 | 🟢 结构 | 盒内印刷说明书版式（竞品第一差评源反制资产）；内容全引 P3/P4/T3 不新造 |
| **CH3 移动端/响应式规格** | 渠道 | 🟢 结构 | 选购器/生成器/Hub/PDP 四表面；首屏承重句不折叠 |
| **OPS1 运维 SOP** | 运维 | 🟢 实质 | 新页模板/claim 审批链/🟡→🟢 销项流程/**数字改动传播 checklist**（BOM 裁定案例化）/月度巡检 |

---

## 四、导航 / 互链模型

### 4.1 全局导航

| 导航项 | 行为 | 目的地 / owner |
|---|---|---|
| `KES` logo | 返回 Hub 顶部 | `/bathtub-filter` / 本页 |
| `Shop` | 下拉：Free Chlorine / Chloramine + Soak / Well Water / Build Your Formula / Refills | S1 / S2 / S3 / SVC13 / SVC4 |
| `Find My Formula` | 进入选购器；比 `Home` 更有任务价值 | SVC10 |
| `How It Works` | 进入爆炸结构总览，并在页内继续到 transparent formula / engineered flow | D1 → D3/D2 |
| `Fit` | 进入 spout compatibility checker | P4 |
| `Support` | 下拉：FAQ / Installation / Care / Returns / Contact | SVC1 / P4 / P3 / SVC3 / SVC6 |

`About` 不占主导航高优先位，可放进二级菜单或 Footer。搜索与购物车保留 icon；购物车应支持 drawer，不强制离开当前 spoke。

### 4.2 购买路由

1. 冷流量落 Hub，在两屏内选购。
2. 不确定水质 → SVC10 → 返回 S1/S2/S3 或 SVC13；能力外返回明确劝退，不制造万能自定义组合。
3. S1/S2 可直接购买；S3 先完成 well red-flag；SVC13 完成白名单配置并生成 `formula_id`。
4. 任何 Formula PDP 都提供 `Check my spout`，fit fail 时不能继续以默认安装方式加购。
5. 进入 D/M/T/E/P/SVC spoke 后保留 `selected_formula`、`fit_status` 和 cart；sticky CTA 返回对应 PDP 或 Hub 购买器。

### 4.3 内容深链规则

- **Formula → Media**：S1 链 M1/M2/M7；S2 链 M3/M4/M2/M7；S3 链 M5/M3/M7；custom 结果只链实际使用的 M 页。
- **Media → Formula**：每个 M 页显示 `Used in`，仅反链真实采用该材料的标准 Formula；custom 用法显示为条件入口，不列举所有动态组合。
- **Formula / Hub → Structure**：产品爆炸图链 D1；透明滤仓链 D3；flow/channeling 只链 D2；fit 只链 P4/D4。
- **全站 → Method**：性能/认证链 T2；自己测链 T1/E5；买后 before/after 链 SVC2；更换链 T3；各页不重写这些口径。
- **Education → Decision**：E 页正文只解释问题，结尾主 CTA 为 `Match my water` → SVC10；仅在答案确定时直接推荐对应 S1/S2/S3。
- **Service → Purchase**：FAQ、退保、客服不强推；只有回答完成后显示上下文相关的 Formula 或 Refills CTA。
- **Custom → Single source**：SVC13 只组装 M/D/T/P4 已定义的材料、结构、验证和适配规则，不能在配置器里新造 claim。
- **External layer**：评测/社区不自建伪媒体页面，指针到 [[bathtub-filter-content-ecosystem-by-layer]]。

### 4.4 链接文案与点击面

- 使用任务型文案：`See how the flow path works`、`Check my spout`、`See the test method`、`Find the right refill`；禁全页重复 `Learn more`。
- 产品卡标题/产品图进入 PDP，`Add to cart` 原位交易，`Check fit` 打开工具；整卡不得同时承担三种行为。
- 爆炸图、材料近照、水路剖面、spout 类型图可以点击；模特、泡澡氛围图和品牌装饰不加链接。
- 每个 Hub 模块最多一个主 deep link，加必要的材料 hotspot；避免正文关键词到处可点。
- 设计交付逐项使用 `Link ID / Clickable / Destination / Wiki owner / Return behavior / Analytics`，完整定义见 [Hub Design Review · 页面链接实施表](./bathtub-filter-kes-hub-design-review-2026-07-14.md#页面链接实施表)。

### 4.5 单一真理源规则

- 性能数字和测试条件：T2。
- 更换/寿命：T3。
- 每种 media 的用途与 claim：对应 M1–M7。
- 结构、爆炸图部件和水路：D1/D2/D3/D4。
- 套装内容：P2。
- 适配：P4。
- 价格：SVC7；其他页面只调用，不手写。
- 产品 claims 的 Allowed/Conditional/Banned：claim register。

Hub、Formula PDP、配置器和渠道页只能调用这些 owner，不各写一套。这是防止数字、版本和 claim 漂移的核心机制。

---

## 五、页面规格如何收敛为可售版本

站点不能替代产品验证，但每个公开表面的内容必须由以下链条生成：

1. **标准 Formula 定义** = S1/S2/S3 的固定 media stack + D1/D2 结构 + P2 套装内容 + P4 适配边界。
2. **Custom Formula 定义** = SVC13 白名单模块 + 固定顺序 + 必需附件 + 完整组合的 flow/pressure/claim review + 唯一 `formula_id`。
3. **可展示 claim** = claim register 当前 Allowed/Conditional 状态；产品已决定上市不代表性能数字自动转绿。
4. **验证清单** = 每个 Formula 中全部 🟡 claim 的成品测试，不以单料证据替代成品流量/接触时间数据。
5. **前端分流** = SVC10 水源/ZIP/CCR/井水红旗 → S1/S2/S3/SVC13 或诚实劝退；S4/S5 作为附加模块解释，不作为第五/第六主机版本。
6. **包装与说明书** = Formula owner + P2/P3/P4/T3 + claim register 的投影；四版本包装必须可区分，custom 必须打印 `formula_id`。

### 页面发布前最小合同

每个公开页面必须声明：

- `Primary question`：本页只负责回答什么。
- `Entry points`：从 Hub、Formula、搜索或教育页中的哪些位置进入。
- `Evidence owner`：数字、材料、结构、适配、价格分别引用谁。
- `Boundary`：至少一个明确不适用项或证据限制。
- `Primary CTA`：购买、返回已选 Formula、Match Water、Support 四者只能选一个主动作。
- `Return behavior`：返回购买器时保留哪些状态。
- `Analytics event`：用来判断此 spoke 是否解除疑虑，而不是只看 pageview。

---

## 六、实施顺序与发布门槛

### Phase 1 · 转化骨架

1. Hub Screen 1–2：Hero + 四版本购买器。
2. SVC10 Water Match、S1/S2/S3 Formula PDP、SVC13 Custom Configurator。
3. P4 spout checker、SVC7 价格源、P2 套装内容源。
4. 购买状态 `selected_formula / fit_status / water_match / cart_context` 跨页保持。

**门槛**：用户最多两屏可下单；四版本路由无死路；能力外目标无法通过 custom 绕过。

### Phase 2 · 产品证据

1. D3 transparent formula + M1–M7 media hotspots。
2. D1 真实 BOM 爆炸图。
3. D2 engineered flow / 防沟槽独立模块。
4. E10/T2 正常浴缸流速与测试方法。
5. T1/E5/SVC2/T3 验证和更换闭环。

**门槛**：爆炸图与实际 BOM 一致；爆炸图和水路图职责分开；所有数字只有一个 owner；未验证数字不进入 Hero。

### Phase 3 · 降低购买阻力

1. SVC1 FAQ、P1 不适用清单。
2. P3 安装维护、SVC3 退保、SVC6 客服。
3. SVC4 refill/subscription、SVC9 bundles。
4. SVC8 只在真实评价素材齐备后上线。

**门槛**：Support 导航无空页面；价格/条款占位不得进入生产；评价无 skin/hair/medical 结果 claim。

### Phase 4 · 教育与获客

1. E1–E11 搜索教育簇，每页导向 SVC10 或明确 Formula。
2. SVC5 referral、SVC11 lifecycle、SVC12 privacy/consent。
3. CH1–CH3 将自有站口径投影到 Amazon、IFU 和移动端，不新造 claim。

**门槛**：教育页不使用 toxin-panic；邮箱用途分流；移动端仍在两屏内完成版本选择和购买。

### 当前文档状态（2026-07-14）

- 53 个内容/运营节点均已有 wiki 页面；其中价格、退保、客服、社会证明和法律条款仍含 placeholder，不能据此认定生产站 ready。
- 四版本购买架构、Hub 屏序、深链规则、返回购买器状态和内部/公开边界已在本页定义。
- 当前仍需外部/人工闭环的重点：各 Formula 成品性能测试、完整 spout 矩阵、价格/COGS、退保条款、真实 testimonials、隐私/ToS、可持续性事实 owner。
- 文献署名待修：`ascorbate-chloramine-kinetics-research-2026-06.md` 中 Peskin & Winterbourn 误署为 Tikkanen，需核原始文献后订正（owner：产品/研究）。

---

## 上线前合规自检（照 register 表面→claim 映射）

每页 ship 前逐条过 [[bathtub-filter-claim-register]] §D 表面→claim 映射对应行；本轮从当前视觉稿已抓到的 5 个触发项（氯胺认领、NSF 成品误读、25 L/min 上首屏、50,000 L 溯源、"两种料"矛盾）全部转成上表护栏，逐页 ship 时核销。

---

## Sources / 内部依据

- [Claim register（Banned/Conditional/Allowed + 表面→claim 映射）](../bathtub-filter-claim-register.md)
- [按水源类型的滤材方案（三套标准 Formula + guided custom）](../bathtub-filter-kes-media-stack-options-by-water-type.md)
- [完整网站文案 v1（Homepage+PDP+About）](../bathtub-filter-kes-website-copy-v1.md)
- [Hub 页面设计复盘与逐元素链接表](./bathtub-filter-kes-hub-design-review-2026-07-14.md)
- [首页+About 落地版式](../bathtub-filter-kes-homepage-and-about-page-layout.md)
- [就地软水可行性（硬水/阻垢边界 §8）](../bathtub-filter-point-of-use-hardness-softening-feasibility.md)
- [水质自测套件 / 模块化获客引擎](../bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md)
- [V1 执行路线图（Gate 1）](../bathtub-filter-kes-v1-execution-roadmap-2026-06-15.md)

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-kes-media-stack-options-by-water-type]]
- [[bathtub-filter-kes-website-copy-v1]]
- [[bathtub-filter-kes-hub-design-review-2026-07-14]]
- [[bathtub-filter-kes-homepage-and-about-page-layout]]
- [[bathtub-filter-point-of-use-hardness-softening-feasibility]]
- [[bathtub-filter-content-ecosystem-by-layer]]
- [[bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine]]
- [[bathtub-filter-kes-v1-execution-roadmap-2026-06-15]]
