---
type: product
status: draft
owner: strategy
created: 2026-07-02
updated: 2026-07-02
visibility: team
confidence: low
officiality: placeholder
domain: product
domains: [bathtub-filter, kes, privacy, terms, consent, compliance, ccpa, gdpr, coppa, can-spam, cookies, accessibility, wcag, data-map]
review_cycle: monthly
related:
  - ./bathtub-filter-kes-water-match-selector-spec.md
  - ./bathtub-filter-kes-referral-program.md
  - ./bathtub-filter-kes-proof-and-testimonials.md
  - ./bathtub-filter-kes-refill-subscription.md
  - ./bathtub-filter-kes-email-lifecycle-spec.md
  - ./bathtub-filter-kes-returns-and-warranty.md
  - ../bathtub-filter-claim-register.md
  - ./bathtub-filter-kes-marketing-site-content-map.md
---

# SVC12 · 隐私 / ToS / 同意 / 无障碍（Privacy, Terms & Consent）

> ⚠️ **占位骨架 · 法律上线阻断项** — 全站采集邮箱/归因/埋点，无隐私底座不得上线；条款 `[____]` 待法务。

## 这页干什么

全站的**数据与法律底座**：选购器收邮箱、referral 做归因、生成器回传读数、GA4 埋点、订阅存账户、UGC 收人像授权——每一项都是数据处理行为，没有隐私政策 / 同意机制 / ToS 兜底，任何一页都不能上线。本页章节全搭：**数据地图与无障碍基线为实质内容（现在就能写死）**，法律条款留 `[____ 待法务]`。

---

## 一、数据地图（全站在哪采什么 · 实质内容）

> 这是给法务起草隐私政策的**事实输入**，也是对内的「最小化承诺」清单。各采集点的产品级承诺（零 PII、看结果不需注册、邮箱只用于承诺用途）已在各 spec 定死，此处汇总为唯一台账。

| # | 采集点 | 采什么 | 为什么（承诺用途） | 存哪 | 保留多久 |
|---|---|---|---|---|---|
| 1 | **选购器劝退邮箱**（[SVC10 §2.3/§3.3](./bathtub-filter-kes-water-match-selector-spec.md)） | 邮箱 + reason 枚举（6 种：`out_of_coverage / chloramine_wait / ro_no_value / carbon_retest_reminder / well_waitlist / well_out_of_scope`）+ ZIP 前缀 | **只兑现劝退时承诺的那类通知**（V1.5 上市 / 覆盖上新 / 复测提醒），时点归 [SVC11 E8](./bathtub-filter-kes-email-lifecycle-spec.md)；🔴 不挪作泛营销名单 | ESP 列表 + `email_capture` 表 `[____ 待工程]` | `[____]`（建议：承诺兑现后 N 月未转化即清 `[____ 待运营]`） |
| 2 | **Referral 归因**（[SVC5 §五/§八](./bathtub-filter-kes-referral-program.md)） | 卡上唯一码（**卡面零 PII**）；服务端「码→盒→订单→推荐人」映射；归因 cookie；防自荐比对用的**收货地址 / 支付指纹** | 奖励归因与防刷；地址/支付指纹**仅用于同址拦截判定**，不作画像 | referral app + 服务端映射表 `[____ 待工程]` | 码有效期 `[____ 待运营]`；映射与比对记录 `[____]` |
| 3 | **分享图生成器回传**（[proof §4.7.3](./bathtub-filter-kes-proof-and-testimonials.md)） | **可选**匿名 `{zip3, before, after, ts}`——零 PII、ZIP 只取前 3 位、**不回传也能出图**（纯前端渲染） | 城市对比钩子 / 匿名聚合统计（未来水质地图） | 匿名聚合存储 `[____ 待工程]` | `[____]`（匿名数据，建议聚合后即弃原始记录 `[____ 待法务确认是否够格「匿名」]`） |
| 4 | **GA4 埋点**（[SVC10 §四](./bathtub-filter-kes-water-match-selector-spec.md) 事件表 + share 事件） | 事件流（`zip_hit / email_captured / add_to_cart / share_image_generated`…）、设备信息、粗粒度地理、cookie 标识符 | 漏斗与转化度量（KPI 见 MVP spec §6） | GA4（Google = 数据处理者，DPA `[____ 待法务]`） | GA4 保留期设置 `[____ 待运营，建议 14 个月]` |
| 5 | **订阅 / 订单账户**（[SVC4 §一](./bathtub-filter-kes-refill-subscription.md)） | 姓名、地址、邮箱、订单史、订阅状态与 skip 历史；**支付卡号由支付处理商持有，站内不存** | 履约、订阅管理、退货保修（SVC3） | 电商平台（Woo/Shopify `[____ 待定]`）+ 支付处理商 `[____]` | `[____]`（税务/会计法定期限 `[____ 待法务]`） |
| 6 | **UGC 投稿**（[proof §4.3](./bathtub-filter-kes-proof-and-testimonials.md)） | 照片/视频（**可能含人像**）、卡面手写城市/日期、社交 handle、rights license 勾选记录、#gifted 披露记录、奖励发放记录 | gallery 墙 / 官号转发 / 广告（**以 license 勾选范围为限**）；奖励兑付 | 投稿渠道定型后 `[____ 待运营]` | license 期限 `[____ 待法务]`；未勾选授权的素材**不存不转发** |

**跨项承诺（产品级已定，写进隐私政策）：**

- **看结果不需注册**：选购器全部结果（含劝退结论）无注册墙（SVC10 §四）。
- **邮箱只在价值时刻、且说清给什么**：reason 枚举 = 用途白名单（SVC10 §五-7）。
- **卡上零 PII**：referral 卡丢失不泄露任何人信息（SVC5 §8.3）。
- **不卖数据**：`[____ 待法务确认后写死为对外承诺]`。

---

## 二、隐私政策 `[____ 待法务]`

- **CCPA/CPRA（加州——首发 P1 市场即适用性评估 `[____ 待法务：是否达门槛，未达也建议按达标准建]`）**：告知/删除/更正/限制敏感信息权；"Do Not Sell or Share My Personal Information" 链接 `[____]`；GPC（Global Privacy Control）信号处理 `[____ 待工程]`。
- **GDPR**：仅当接欧盟订单/流量 `[____ 待业务定：V1 是否收欧盟订单——不收则声明并做地理围栏]`。
- **COPPA 不适用声明**：站点与服务不面向 13 岁以下儿童、不有意收集儿童信息 `[____ 待法务措辞]`。⚠️ 注意：婴儿洗澡**场景营销**（register Conditional「Baby/infant framing」）≠ 面向儿童的服务，但措辞须避免被读成后者。
- **第三方处理者清单**：ESP `[____]`、referral app `[____]`、GA4、支付处理商 `[____]`、电商平台 `[____]`——各签 DPA `[____ 待法务]`。
- 政策正文、生效日、变更通知机制：`[____ 待法务]`。

## 三、Cookie / 同意横幅策略 `[____]`

- GA4 与 referral 归因 cookie = **非必要 cookie** → 横幅策略选型 `[____ 待法务：加州 opt-out 模式 vs GDPR opt-in 模式，取决于 §二 地域结论]`。
- Google Consent Mode / 横幅工具选型与埋点联动：`[____ 待工程]`。
- referral 归因在拒绝 cookie 时的降级路径（码在 URL 里，可无 cookie 归因到落地会话）：`[____ 待工程]`。

## 四、CAN-SPAM 合规要点（可写实质）

- **每封可退订**：一键退订链接，10 个工作日内生效；退订状态跨 ESP/平台同步 `[____ 待工程]`。
- **真实发件人**：From/回复地址真实可达；**物理邮寄地址**每封页脚必带 `[____ 地址待运营]`。
- 主题行不误导；commercial vs transactional 区分。
- 邮件触发与时点的唯一真理源 = [SVC11 邮件生命周期 spec](./bathtub-filter-kes-email-lifecycle-spec.md)（本页管合规要件，SVC11 管发什么/何时发）。

## 五、ToS `[____ 待法务]`

条款骨架（正文全留 `[____]`）：

- 订阅自动续订披露（FTC negative-option / click-to-cancel；「取消不比订阅难”承诺的法务化——链 [SVC4 §一](./bathtub-filter-kes-refill-subscription.md)）`[____]`
- Referral 计划条款（资格、防滥用与取消资格、奖励非现金/不可转让——链 [SVC5 §8.3/§9](./bathtub-filter-kes-referral-program.md)）`[____]`
- UGC 投稿 T&C（rights license 范围/期限、**不以好评为条件**白纸黑字、#gifted 披露义务——链 [proof §4.3](./bathtub-filter-kes-proof-and-testimonials.md)）`[____]`
- 月度精选/抽选类奖励的 sweepstakes 合规（no-purchase-necessary 等各州规——proof §4.5-4 已点名）`[____]`
- 退货/保修援引（链 [SVC3](./bathtub-filter-kes-returns-and-warranty.md)）`[____]`
- 免责、责任限制、争议解决/仲裁 `[____]`

## 六、无障碍基线（可写实质）· WCAG 2.1 AA

**全站目标 = WCAG 2.1 AA。** 两个交互组件是重点核查对象：

### 6.1 色阶点选 UI（🔴 最高风险——试纸色块选择器对色盲用户）

- [分享图生成器（proof §4.7.3）](./bathtub-filter-kes-proof-and-testimonials.md) 的 BEFORE/AFTER 输入 = 「复刻试纸色阶为按钮，点颜色即输入」——试纸读数本质是**颜色编码**，对色觉障碍用户（男性约 8%）纯色块不可用。**要求：每个色块必须带非颜色冗余标识**（ppm 数值 / 档位文字直接标在块上或旁边），并以 radio group 语义实现、可键盘选择、选中态不只靠色变（加勾选标记/描边）。
- 同理延伸到**印刷面**：对比卡色阶尺 / Pool→Spa 表盘建议并印数值刻度（与 proof §4.2 低氯城市「数值刻度」方案天然协同）；网页上展示的试纸读数对比图须在 alt/正文给出数值。

### 6.2 选购器（SVC10）

- 表单语义：Q1–Q3 用 fieldset/legend + label；分岔跳转对屏幕阅读器可感知（结果区 aria-live）。
- 全键盘可达：整棵决策树到加购/留邮箱可纯键盘走完；焦点可见且不丢失。
- 错误与状态不只靠颜色（ZIP 错误、confidence 提示需图标+文字）。

### 6.3 全站通用

- **对比度**：正文 ≥4.5:1、大字与 UI 图形 ≥3:1——试纸色带、结果卡、表盘弧的品牌配色逐一核 `[____ 待设计]`。
- **键盘可达 + 可见 focus**；触控目标尺寸 ≥44×44px（与 [CH3 移动端/响应式规格](./bathtub-filter-kes-mobile-responsive-spec.md) 协同——该页移动 a11y 基线反向引用本节）。
- **alt 文本规范**：前后对比照 alt 须写出读数信息（如 "Before-filter strip reading about 2 ppm free chlorine; after-filter strip near 0"），不得只写 "before and after photo"；纯装饰图 `alt=""`。
- **邮件无障碍**：语义 HTML、图片 alt、提供纯文本版（与 SVC11 全局规则联动）。
- **视频**（proof §三 证言、UGC 视频）：上站须配字幕 `[____ 待运营流程]`。
- **验收**：axe 自动扫 + 键盘走查 + 色盲模拟，纳入选购器/生成器工程验收清单（挂 [SVC10 §六](./bathtub-filter-kes-water-match-selector-spec.md)）`[____ 待工程]`。

---

## 七、待补清单（谁填什么）

| 章节 | 待补项 | 负责 |
|---|---|---|
| §一 数据地图 | 各项存储位置、保留期、清理规则 | 工程 + 运营 + 法务 |
| §二 隐私政策 | 正文、CCPA/CPRA 适用性、GDPR 地域结论、COPPA 声明、处理者 DPA | 法务 |
| §三 Cookie | 横幅策略选型、Consent Mode、无 cookie 归因降级 | 法务 + 工程 |
| §四 CAN-SPAM | 物理地址、退订同步机制 | 运营 + 工程 |
| §五 ToS | 全部条款正文（订阅/referral/UGC/sweepstakes/争议） | 法务 |
| §六 无障碍 | 品牌色对比度核查、字幕流程、验收纳入工程清单 | 设计 + 运营 + 工程 |
| 全页 | 隐私政策/ToS 页脚全站挂链 | 工程 |

> **上线门槛（阻断项）**：隐私政策 + ToS 定稿挂站 + Cookie 同意机制可用 + §一数据地图与实际实现一致性核验后，采集类功能（选购器邮箱/归因/生成器/埋点）方可开流。

---

## Sources / 内部依据

- [选购器 spec（email_capture reason 枚举、无注册墙、埋点事件表）](./bathtub-filter-kes-water-match-selector-spec.md)
- [推荐计划页（归因码零 PII、同址/支付指纹防自荐、码池规则）](./bathtub-filter-kes-referral-program.md)
- [社会证明页（生成器 {zip3,before,after,ts} 零 PII 设计、UGC rights license、FTC/#gifted、sweepstakes 点名）](./bathtub-filter-kes-proof-and-testimonials.md)
- [补芯订阅页（账户数据、negative-option / click-to-cancel）](./bathtub-filter-kes-refill-subscription.md)
- [SVC11 邮件生命周期 spec（CAN-SPAM 执行面、邮箱用途承诺）](./bathtub-filter-kes-email-lifecycle-spec.md)
- [退货 / 保修页（ToS 援引）](./bathtub-filter-kes-returns-and-warranty.md)
- [claim-register（婴儿场景 framing 边界等，防隐私文案联动误读）](../bathtub-filter-claim-register.md)
- [营销站内容地图（SVC12 索引位）](./bathtub-filter-kes-marketing-site-content-map.md)

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-kes-water-match-selector-spec]]
- [[bathtub-filter-kes-referral-program]]
- [[bathtub-filter-kes-proof-and-testimonials]]
- [[bathtub-filter-kes-refill-subscription]]
- [[bathtub-filter-kes-email-lifecycle-spec]]
- [[bathtub-filter-kes-returns-and-warranty]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-kes-marketing-site-content-map]]
