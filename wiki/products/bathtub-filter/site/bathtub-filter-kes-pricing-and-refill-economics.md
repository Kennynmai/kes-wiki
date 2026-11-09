---
type: product
status: draft
owner: strategy
created: 2026-07-01
updated: 2026-07-14
visibility: team
confidence: low
officiality: placeholder
domain: product
domains: [bathtub-filter, kes, pricing, refill, subscription, economics, clean-honest, placeholder]
review_cycle: monthly
related:
  - ../bathtub-filter-kes-v1-pricing-channel-launch-geo-subscription.md
  - ./bathtub-filter-kes-refill-subscription.md
  - ./bathtub-filter-kes-page-replacement-and-lifespan.md
  - ./bathtub-filter-kes-returns-and-warranty.md
  - ./bathtub-filter-kes-marketing-site-content-map.md
  - ./bathtub-filter-kes-scenario-free-chlorine.md
  - ./bathtub-filter-kes-scenario-chloramine.md
  - ./bathtub-filter-kes-scenario-well-water.md
  - ./bathtub-filter-kes-custom-formula-builder-spec.md
---

# KES 浴缸过滤器 · 定价与 Refill 经济学（Pricing & Refill Economics）

> ⚠️ **占位骨架** — 结构已搭好，标 [____] 的关键条款/数字/素材待 [对应团队] 补；未定稿前不上线。

## 这页干什么

面向客户如实展示价格结构：单价、几种购买方式对比、每次泡澡摊到多少钱、为什么订阅更省。价格框架参考 [[bathtub-filter-kes-v1-pricing-channel-launch-geo-subscription]]（内部 GTM），订阅 SOP 见 [[bathtub-filter-kes-refill-subscription]]，换芯寿命口径以 [[bathtub-filter-kes-page-replacement-and-lifespan]] 为单一真理源。

> 🟡 待 [财务/运营] 补：本页所有价格/成本数字须由 BOM + 渠道 margin 定稿后回填，未定稿不上线。

---

## 一、单价

| 价格对象 | 一次性 | Refill | 订阅 | 状态 |
|---|---:|---:|---:|---|
| Free-Chlorine Formula | `[____]` | `[____]` | `[____]` | 待财务/BOM |
| Chloramine + Soak Kit | `[____]` | inline cartridge `[____]` + soak consumable `[____]` | `[____]` | 必须拆清两种耗材 |
| Well-Water Formula | `[____]` | `[____]` | `[____]` | 待 challenge/BOM |
| Build Your Formula | modules 汇总 | 按 `formula_id` | 按实际最早到期组件 | 不允许一个统一 custom 价 |

> 🟡 待 [财务/运营] 补：Starter Kit 与 Refill 单件的最终对外价。

---

## 二、购买方式对比（1 件 / 4 件 / 订阅）

| 方式 | 价格 | 单件均价 | 适合谁 |
|---|---|---|---|
| Refill 1-pack | [____ 待补] | [____ 待补] | [____ 待补] |
| Refill 4-pack | [____ 待补] | [____ 待补] | [____ 待补] |
| Refill 订阅（auto-ship） | [____ 待补] | [____ 待补] | [____ 待补] |

> 🟡 待 [财务/市场] 补：三种方式的价格、单件均价、目标人群。

---

## 三、每次泡澡成本

- 换算依据（滤芯寿命 baths/gallons，口径引 [[bathtub-filter-kes-page-replacement-and-lifespan]]）：[____ 待补]
- 每次泡澡摊销成本：[____ 待补]

> 🟡 待 [财务] 补：以换芯寿命页的 baths 口径除单件价，得每次泡澡成本（用 baths/gallons，不用 months）。

---

## 四、为什么订阅更省

- 订阅 vs 单买价差：[____ 待补]
- 省的来源（bulk / 免运费 / 不断供）：[____ 待补]

> 🟡 待 [市场/财务] 补：订阅省钱的具体来源与幅度。

---

## 五、成本计算器（占位）

> [____ 待补] 成本计算器组件：输入本地氯浓度/泡澡频率 → 输出年成本与每次泡澡成本。

> 🟡 待 [工程/财务] 补：计算器逻辑与参数（寿命随本地氯浓度变化的口径引换芯寿命页）。

计算器必须先识别 Formula：Free-Chlorine 才能使用氯浓度/baths 模型；Chloramine 分开计算 inline 与 soak；Well-Water 按负载模型；Custom 按 `component_due[]`。禁止把游离氯寿命公式复制给全部版本。

## 六、价格数据合同与上线阻断

每个价格记录至少包含：`sku/formula_id`、`purchase_type`、`currency`、`list_price`、`actual_price`、`included_components`、`shipping/tax disclosure`、`effective_at`、`approved_by`。Hub、PDP、Bundle、Subscription、Amazon 只能调用这份记录。

以下任一为空即阻断购买页上线：实际成交价、包含内容、订阅续费价/频率、取消方式、运费披露、税费处理、价格生效时间。页面可以在内部保留 `[____]`，生产环境不得显示占位符、`$0` 或“联系客服询价”。

---

## 护栏：clean-honest 定价原则

KES 定价与「看得见的料」母题一致——**如实列，不做隐藏定价心理**：

- 不用锚定/诱导性倒计时/虚假原价/scarcity 制造紧迫感。
- 不写 "best value / cheapest"（触发比价，且与 clean-honest 冲突，见 claim-register 广告行）。
- 所有对比数字如实、可核；订阅省多少就写多少，不夸大。
- 价格锚点是「透明」不是「便宜」——溢价来自可核查，不来自婴儿/医疗声称。

> 🟡 待 [法务/市场] 补：本页对外文案定稿前过一遍 clean-honest 自检（无隐藏费用、无诱导定价）。

---

## Sources / 内部依据

- [V1 定价 / 渠道 / 订阅经济学（内部 GTM）](../bathtub-filter-kes-v1-pricing-channel-launch-geo-subscription.md)
- [Refill 订阅](./bathtub-filter-kes-refill-subscription.md)
- [更换 / 寿命页（寿命口径真理源）](./bathtub-filter-kes-page-replacement-and-lifespan.md)
- [退货与保修](./bathtub-filter-kes-returns-and-warranty.md)
- [营销站内容地图（IA）](./bathtub-filter-kes-marketing-site-content-map.md)

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-kes-v1-pricing-channel-launch-geo-subscription]]
- [[bathtub-filter-kes-refill-subscription]]
- [[bathtub-filter-kes-page-replacement-and-lifespan]]
- [[bathtub-filter-kes-returns-and-warranty]]
- [[bathtub-filter-kes-marketing-site-content-map]]
