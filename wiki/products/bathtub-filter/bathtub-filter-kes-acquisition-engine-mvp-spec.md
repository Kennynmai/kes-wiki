---
type: product
status: draft
owner: strategy
created: 2026-06-15
updated: 2026-06-15
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, acquisition, mvp, spec, referral, zip-lookup, growth]
source_count: 5
related:
  - ./bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md
  - ./bathtub-filter-utility-service-map-by-metro.md
  - ./bathtub-filter-kes-v1-pricing-channel-launch-geo-subscription.md
  - ./bathtub-filter-claim-register.md
  - ./bathtub-filter-kes-website-copy-v1.md
review_cycle: monthly
verification_status: working
---

# KES Bathtub Filter · 获客引擎 MVP 规格（可交付 build）

> 把 [获客引擎 §7.6](./bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md) 的 MVP 落成 2–4 周可开发的规格。
> **MVP 一句话**：**ZIP 诊断当前门 + 现成 referral app + 验证峰值触发 + 换芯抵扣奖励**——不含物理试纸套件/寄试纸/动态个性化报告卡（全在完整版）。

---

## 0. MVP 边界（圈死，防 scope 蔓延）

| | MVP（这版做） | Deferred（完整版） |
|---|---|---|
| 诊断 | **ZIP-only 快速路径**（路径 A）→ 类型+硬度+推荐组合 | 多参数试纸套件、观察指引（路径 B）、寄免费试纸 |
| 结果展示 | **轻量结果页**（模板化，可分享，带推荐码） | 动态个性化 OG 报告卡（每份渲染图） |
| 转介绍 | **现成 referral app** + 换芯抵扣 | 物理「一起测」寄试纸、多触点深度编排 |
| 覆盖 | **首发 metro**（P1+P2）权威，其余诚实 fallback | 全 ZIP 覆盖 |
| 验证 | 盒内**游离氯试纸**（已是产品标配）+ 验证后触发邮件 | 总氯/氯胺验证、报告卡二次分享 |

---

## 1. 核心循环（MVP 版）

```
首页 ZIP 诊断 ──→ 结果页(类型+推荐+加购) ──→ 购买 starter
                                                  │
                          盒内游离氯试纸自测(装芯前后看氯降)
                                                  │
                        ★验证峰值邮件「你看到它有用了——分享给同样水的人」
                                                  │
                  referral 链接 ──→ 朋友落「测你家的水」(带归因) ──→ 朋友购买
                                                  │
                        推荐人得【下次换芯抵扣】 · 朋友得【首单折扣】
```

---

## 1.5 两个工作 + 设计原则（避免 KPI 失真）

**这台引擎做两件不同的事，埋点与 KPI 必须分开：**
- **转化（convert）**：把已到站访客（付费/社媒/内容引来）用 **ZIP 诊断**变成订单——这是 conversion 工具。
- **获客（acquire）**：用 **referral 循环**低成本带来**新**访客——这才是「获客引擎」本体。

> 混在一起会让 referral CAC 失真。§6 埋点必须区分来源（referral vs 付费 vs 自然）。

**设计原则：**
1. **极低摩擦**：ZIP 单字段、即时出结果、**看结果不需注册**；邮箱只在「价值时刻」（劝退/等待）才要。
2. **诚实优先**：诊断说「水的类型/适配」，不说健康危害；**ZIP 是近似，试纸是地面真相**。
3. **可分享 ≠ 必奖励**：结果页谁都能分享（自然流量/SEO）；带奖励的 referral 仅限已购客（防刷）。

---

## 2. 三个用户流（step-by-step）

### 流 A — 诊断获客（冷访客 → 购买）
1. 首页区块 6「Find your water」输入 ZIP。
2. 后端查 ZIP→水质映射，返回：消毒剂类型（游离氯/氯胺/未知）+ 硬度档 + 推荐组合。
3. 结果页展示（§4.2），CTA「加入购物车」直挂推荐 SKU。
4. **氯胺/未覆盖 ZIP → 诚实劝退**：「V1 还不适合你家的水，留邮箱等氯胺版」→ 收邮箱（不强卖）。

### 流 B — 验证 → 转介绍（已购客 → 邀请）
1. 购买后进入邮件序列。
2. **T+10~14 天**（够用几次、用试纸看到氯降）发**验证峰值邮件**：「你刚亲眼看到它有用——把它分享给也用同样水的人」+ 专属 referral 链接。
3. 客户点「分享」→ referral app 生成/取出其码与链接。

### 流 C — 转介绍转化（朋友 → 购买 → 双端奖励）
1. 朋友点 referral 链接 → 落「测你家的水」页（带 referral 归因 cookie）。
2. 朋友走流 A 诊断 → 购买 starter。
3. referral app 归因成功 → **推荐人得下次换芯抵扣**、**朋友首单折扣**自动兑付。

---

## 3. 组件规格

### 3.1 ZIP 水质查询
- **输入**：5 位 ZIP。
- **数据源**：[按 metro 水务图谱](./bathtub-filter-utility-service-map-by-metro.md) 整理成 `zip_prefix → {disinfectant_type, hardness_band, metro}` 静态表（MVP 先覆盖 P1 拉斯维加斯/凤凰城/圣安东尼奥 + P2 芝加哥/埃尔帕索）。
- **返回**：`{type: free_chlorine | chloramine | unknown, hardness: soft|moderate|hard|very_hard, recommended_stack: [...], serviceable: bool}`。
- **覆盖外 fallback**：`unknown` → 不猜，给「我们还没覆盖你的城市」+ 留邮箱 + 通用教育。
- **精度诚实**：ZIP→类型是 **metro/水务级近似**（一个 ZIP 可能跨水系），文案用「based on your city's water utility data」，并指明**盒内试纸才是你家水的地面真相**（接 claim register 精度行）。
- **零摩擦**：单字段、即时、**无需注册看结果**。
- **合规**：返回只说「水的类型/产品适配」，**不说健康危害**（claim register: 诊断禁 toxin-panic）。
- **劝退池=资产**：氯胺/未覆盖留下的邮箱是**下一个 metro 扩张信号 + V1.5 氯胺 waitlist**，不是死数据。

### 3.2 结果页（轻量，可分享，带码）
- 模板化页（非动态图）：城市/类型/硬度 + 推荐组合 + 「为什么」一句 + 加购 CTA。
- **多条件一键加购**：游离氯+极硬 → 推荐「去游离氯主芯 + 阻垢」，**一键把推荐组合整套加入购物车**（接 stack_mapping，cross-sell 入口）。
- **分享分两层**：① 结果页**任何人可分享**（自然流量/SEO，无奖励）；② **referral 奖励链接**仅已购客有（app 生成），防刷。
- 文案照 [website-copy](./bathtub-filter-kes-website-copy-v1.md) 区块 6 + claim register「诊断报告卡」行：精度如实「a quick guide, not a lab test」；硬度推荐阻垢必带「does not soften your water」。

### 3.3 转介绍机制（现成 app）
- **app**：WooCommerce → AutomateWoo Referrals / ReferralCandy / Refersion；Shopify → Friendbuy / Yotpo Referrals（等价替换）。
- **码/链接**：app 自动按客户生成。
- **奖励**：
  - 推荐人 = **账户 credit $X，下一单即可用（换芯或任意模块）**——比等 90 天换芯更快兑现，且**推动模块采用**（接 cross-sell）。不发现金。
  - 朋友 = **首单 starter 折扣**。
- **防刷**：防自荐（同邮箱/同支付）、每推荐人奖励上限、归因 cookie 窗口（app 默认）。
- **触发授予**：朋友订单完成且**过退货窗**后 → 兑付（防退货套利）。

### 3.4 触发邮件（验证峰值序列）
- ESP（Klaviyo / Mailchimp / AutomateWoo flows）。
- 序列：T+0 订单确认（含「装好后用试纸测一次」引导）→ **T+10–14 验证峰值邮件** → T+45 复购提醒（试纸该换信号）。
- **验证峰值邮件先驱动行为再 ask**（关键）：MVP 测不到用户是否真用了试纸，所以邮件**先 prompt 验证**——「测了吗？你应该看到氯降下来」+ 预期读数 → **再**接「你刚亲眼看到它有用，分享给同样水的人」+ 专属 referral 链接。让邮件本身制造「验证时刻」，而非假设它已发生。
- **文案护栏**：referral 文案 = 「帮朋友搞清自己家水里有什么」，不 toxin-panic、不健康声称、不刷屏压力。

---

## 4. 数据模型（MVP 最小）

```
zip_water_lookup:  zip_prefix(PK) → disinfectant_type, hardness_band, metro, serviceable
stack_mapping:     {type, hardness} → recommended_sku[]   # 游离氯→去游离氯主芯; +极硬→加阻垢; 氯胺→不可售(留邮箱)
referral:          由 app 托管(referrer_id, code, friend_order, reward_status)
email_capture:     email, zip, reason(out_of_coverage | chloramine_wait)  # 诚实劝退收集
```

---

## 5. 技术栈（WooCommerce 主，Shopify 等价）
- 商城：WooCommerce（[已有 GTM/GA4 setup](../../protocols/woocommerce-gtm-ga4-setup.md)）。
- ZIP quiz：轻量自建（前端表单 + 静态 JSON 查表）或 quiz 插件；结果页用 WooCommerce 模板。
- referral：见 §3.3。
- 邮件：Klaviyo/AutomateWoo。
- 追踪：GA4（已配）。

---

## 6. 追踪 & KPI（day-1 instrument）
- **GA4 事件**：`zip_diagnose`、`diagnose_result(type,serviceable)`、`add_to_cart_from_result`、`email_capture(reason)`、`referral_share`、`referral_signup`、`referral_reward_granted`。**每个订单打 source 标签（referral / paid / organic）** —— 否则 §1.5 的「转化 vs 获客」分不开。
- **KPI**：诊断完成率、结果页→加购转化、referral 分享率、k-factor（邀请×转化）、**referral CAC vs 付费 CAC**、**奖励→复购兑现率**、劝退邮箱量（氯胺/未覆盖需求池）。
- **what good looks like（粗目标，待真实数据校准）**：诊断完成率 >50%；结果页→加购 >15%；referral 分享率（已购客）>20%；**k-factor 趋近/超过 0.3**（每个客户带来 ~0.3 新客即显著摊低 blended CAC）；referral CAC 应 **<付费 CAC 的 1/2**，否则该砍。

---

## 7. 合规护栏（结果页/分享/邮件逐条照 claim register）
- [ ] 结果页/分享/邮件无 toxin-panic、无健康/疗效、无软化承诺
- [ ] 硬度推荐阻垢必带「does not soften your water」
- [ ] 诊断精度如实「快速指路 ≠ 实验室检测」
- [ ] 氯胺/未覆盖 = 诚实劝退 + 留邮箱，不强卖
- [ ] 无 TDS 笔/铅试纸；验证只引导游离氯试纸
- [ ] referral 文案不绑夸大、不刷屏压力
- [ ] 无 scarcity / best-value / cheapest

---

## 8. 构建顺序（2–4 周）
- **W1**：ZIP 查表数据（P1+P2 metro）+ 结果页 + 加购；GA4 事件埋点。
- **W2**：referral app 接入 + 双端奖励（换芯抵扣/首单折扣）+ 邮箱捕获（劝退池）。
- **W3**：验证峰值邮件序列（T+10–14 referral 邮件）+ 合规自检过一遍。
- **W4**：联调、A/B 钩子（结果页 CTA、referral 邮件主题）、上线 P1 三城。

---

## 9. 验收标准（Done 定义）
- 输入 P1 三城 ZIP → 正确返回类型/硬度/推荐 + 可加购。
- 氯胺/未覆盖 ZIP → 劝退 + 收邮箱，无强卖。
- 已购客 T+10–14 收到带专属 referral 链接的验证邮件。
- 朋友经链接购买 → 推荐人换芯抵扣 + 朋友首单折扣自动兑付。
- §6 全部 GA4 事件可见；§7 合规清单全绿。

---

## 10. 明确不在 MVP（→ 完整版）
- 多参数试纸自测套件 + 观察指引（路径 B）
- 寄免费试纸「一起测」
- 动态个性化 OG 报告卡
- 氯胺版相关流程（待 V1.5）
- 全 ZIP 覆盖

---

## 11. 开放问题 / 依赖（需人定）
- [ ] 商城确认 WooCommerce（影响 referral app 选型）
- [ ] referral 奖励金额（$X 抵扣 / 折扣%）— 需 finance 配合 LTV/margin
- [ ] ZIP→水质表谁维护、多久更新（接水务图谱）
- [ ] starter / refill SKU 与定价最终值（接 [定价页](./bathtub-filter-kes-v1-pricing-channel-launch-geo-subscription.md)）
- [ ] 验证邮件触发时点（T+10–14 假设，按真实使用频率校准）

## Sources / 内部依据
- [水质自测套件 + 模块化获客引擎](./bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md)（§7 机制与落地）
- [按 metro 水务图谱](./bathtub-filter-utility-service-map-by-metro.md)（ZIP 数据）
- [V1 定价/渠道/地理/订阅](./bathtub-filter-kes-v1-pricing-channel-launch-geo-subscription.md)（奖励/SKU）
- [claim register](./bathtub-filter-claim-register.md)（结果页/分享/邮件护栏）
- [网站文案](./bathtub-filter-kes-website-copy-v1.md)（区块 6 选择器文案）

## Obsidian links
- [[bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine]]
- [[bathtub-filter-utility-service-map-by-metro]]
- [[bathtub-filter-kes-v1-pricing-channel-launch-geo-subscription]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-kes-website-copy-v1]]
