---
type: product
status: draft
owner: strategy
created: 2026-07-14
updated: 2026-07-14
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, custom-formula, configurator, modular-media, conversion, claims]
source_count: 5
review_cycle: monthly
verification_status: working
related:
  - ./bathtub-filter-kes-marketing-site-content-map.md
  - ./bathtub-filter-kes-water-match-selector-spec.md
  - ../bathtub-filter-kes-media-stack-options-by-water-type.md
  - ../bathtub-filter-kes-positioning-and-problem-layer-decision-2026-06-15.md
  - ../bathtub-filter-claim-register.md
  - ./bathtub-filter-kes-structure-flow-diversion-module.md
---

# Build Your Formula · 自定义配方版本规格

## 产品定义

`Build Your Formula` 是 KES Bathtub Filter 的第四个首发购买版本，与 Free-Chlorine Formula、Chloramine + Soak Kit、Well-Water Formula 并列。

它允许顾客按自己家的水质与浴缸痛点组合模块，但不是散料商城，也不是任意拖拽滤材。前端收集需求，规则引擎只生成经过批准的材料、顺序和结构组合；不合法或证据不足的组合不能加入购物车。

> **客户感受是自行定制；工程事实是 guided configuration。** 用户决定要解决什么，KES 决定哪些材料能同时使用、按什么顺序、需要什么导流结构，以及哪些 claim 可以随配置出现。

## Hub 入口

- 卡片名：`Build Your Formula`
- 一句话：`Choose what you see in your water. We'll build the media stack in the order it needs.`
- CTA：`Customize yours`
- 辅助句：`Only compatible, testable combinations can be ordered.`
- 展示结果：材料爆炸图、固定水流顺序、对应试纸、适用边界、价格、配置编号与 `Add custom formula to cart`。

## 配置流程

1. 选择水源：市政 / 私人井水 / 不确定。
2. 市政水输入 ZIP 或手动选择 free chlorine / chloramine；井水进入症状与红旗筛查。
3. 选择附加问题：可见沉积、硬水水垢困扰、低中度铁锈、低中度 H2S 气味。
4. 系统生成白名单 media stack、固定顺序和必需附件。
5. 页面显示完整爆炸图与水路，解释每个模块的作用与边界。
6. 用户确认 spout 适配、试纸类型、维护要求和不覆盖项后加购。

## 白名单规则

| 输入条件 | 可加入模块 | 固定规则 | 禁止组合 / 护栏 |
|---|---|---|---|
| 市政 + free chlorine | PET + KDF55 + CaSO3 | 沿 Free-Chlorine Formula 的验证顺序与导流结构 | 不加入 chloramine claim；不声称软化 |
| 市政 + chloramine | PET + catalytic carbon + small KDF55 + sodium-ascorbate soak step | 浸泡件为必选，不得删除 | 禁单芯全除、fast/instant、未验证百分比 |
| 私人井水 + low/moderate nuisance | coarse PET + KDF85 + catalytic carbon | 先过红旗筛查；固定粗滤前置 | 高铁 >2–3 ppm、砷、硝酸盐、铀、细菌直接劝退 |
| 可见沉积 | 强化 PET 前置 | 必须位于第一层 | 不将颗粒拦截写成 broad purification |
| 硬水水垢困扰 | anti-scale adjunct | 必带 `It does not soften your water.` | 不生成 softening / hardness reduction claim |

## 不能做的“自定义”

- 用户不能自行改变滤材顺序。
- 用户不能删除某条路线的必需组件，例如氯胺套装的 soak step。
- 用户不能把所有滤材都加入同一腔体。
- 用户不能选择软化、PFAS、杀菌、除砷/硝酸盐、医疗或皮肤疗效目标。
- 未经过兼容性与 claim 审核的新组合只可进入人工评估，不可直接结账。

## 爆炸图与导流要求

每个自定义结果必须实时生成两张图：

1. **Exploded formula**：逐件展示 housing、前置层、每个 media chamber、导流结构、出口和独立浸泡附件。
2. **Flow path**：展示水如何被铺开、按固定顺序经过各层，避免 channeling / shortcut flow。

爆炸图回答“选了什么”；水路图回答“为什么这些料会真正被水经过”。任何自定义组合都必须调用 [D2 导流模块](./bathtub-filter-kes-structure-flow-diversion-module.md) 的结构规则，不能只换滤料而不校核水路。

## Claim 与验证继承

- 每个模块的文案只从对应 M 页继承，不在配置器里新造 claim。
- 组合后的 claim 是各模块允许 claim 的交集，不是并集放大。
- 具体性能数字只在该完整组合已有 finished-product 测试时显示。
- 试纸与说明书随生成的配方匹配；自定义配置获得唯一 `formula_id`，用于补芯复购、客服和测试追溯。

## 交易与复购

- 商品行显示 `KES Bath Filter — Custom Formula / {formula_id}`。
- 购物车必须列出壳体、滤材模块、必需附件和对应试纸，不隐藏组件。
- 复购入口默认加载原 `formula_id`；如用户搬家或水质变化，提示重新运行 Water Match。
- 价格按实际模块汇总，禁止把自定义包装成虚假高价值 bundle。

## 与 Water Match / Fit / Cart 的状态合同

| 输入状态 | 来源 | Builder 行为 | 输出 |
|---|---|---|---|
| `water_match` | SVC10 | 锁定 municipal/free-chlorine/chloramine/well 基线；unknown 不允许猜默认配方 | `water_type + confidence + source` |
| `red_flags[]` | SVC10/E2 | 任一健康级/高负载红旗命中时停止生成，不允许用户删除答案后绕过 | `blocked_reason` 或通过时间戳 |
| `selected_problems[]` | 用户 | 只映射到白名单模块；显示为什么能/不能加入 | module list |
| `fit_status` | P4/D4 | 根据最终组合重量、附件和 spout 重新校核 | pass/conditional/fail/unknown |
| `pricing_version` | SVC7 | 按实际模块调用价格，不在前端写死 | price + effective_at |
| `formula_id` | Builder | 对规则版本、模块、顺序、附件和验证工具做不可变快照 | cart/order/refill/support 共用 |

用户从 Hub 进入时保留原购物车；生成合法 `formula_id` 后返回 Hub sticky cart 或直接打开 cart drawer。进入 M/D/T spoke 后，返回 Builder 必须恢复到同一结果，而不是重新运行问卷。

## 配置结果页内容顺序

1. `Your formula`：水质结论、置信度和一句适用理由。
2. 实时 exploded formula：只显示最终模块和固定层序。
3. flow path：说明铺流、逐层经过和必需附件。
4. `What each part does / does not do`：逐项继承 M 页 claim 与边界。
5. spout fit 与安装附件。
6. 对应试纸、验证方法和更换对象。
7. 价格、`formula_id`、一次性/补芯选择和 `Add custom formula to cart`。

结果页不展示“解决 X 个问题”“更高级/最全面”等 umbrella value；模块多不代表更有效。任何组合缺 finished-product 数字时，只展示结构与材料用途，不拼接单料百分比。

## 上线验收

- [ ] 所有可购买组合均有固定顺序、对应结构和 claim owner。
- [ ] 任何禁用目标都无法进入购物车。
- [ ] Chloramine 路线无法删除 soak step。
- [ ] Well-water 红旗命中后不生成 SKU。
- [ ] 每个结果都展示爆炸图、水路图、spout 适配、试纸和不覆盖项。
- [ ] `formula_id` 可贯穿订单、补芯、客服与分析事件。
- [ ] Water Match、red flags、fit、价格和 cart 状态可往返恢复。
- [ ] 结果页每个材料 hotspot 链到对应 M 页，返回后保持同一 `formula_id`。

## Sources

- [按水源类型的滤材方案](../bathtub-filter-kes-media-stack-options-by-water-type.md)
- [Water-Match Selector](./bathtub-filter-kes-water-match-selector-spec.md)
- [定位与自由组合防呆决策](../bathtub-filter-kes-positioning-and-problem-layer-decision-2026-06-15.md)
- [Claim register](../bathtub-filter-claim-register.md)
- [D2 导流模块 / 防沟槽](./bathtub-filter-kes-structure-flow-diversion-module.md)
