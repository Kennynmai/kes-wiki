---
type: product
status: draft
owner: strategy
created: 2026-07-02
updated: 2026-07-02
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, email, lifecycle, crm, retention, referral, verification, subscription, waitlist, ugc, can-spam, compliance]
review_cycle: monthly
related:
  - ./bathtub-filter-kes-post-purchase-verification.md
  - ./bathtub-filter-kes-referral-program.md
  - ./bathtub-filter-kes-refill-subscription.md
  - ./bathtub-filter-kes-water-match-selector-spec.md
  - ./bathtub-filter-kes-proof-and-testimonials.md
  - ./bathtub-filter-kes-install-and-compatibility-guide.md
  - ./bathtub-filter-kes-page-replacement-and-lifespan.md
  - ./bathtub-filter-kes-privacy-terms-and-consent.md
  - ../bathtub-filter-claim-register.md
  - ./bathtub-filter-kes-marketing-site-content-map.md
---

# SVC11 · 邮件生命周期 spec（Email Lifecycle）· 全站邮件时点唯一 owner

> **定位声明（为什么有这页）**：终审发现 [推荐计划页 §四](./bathtub-filter-kes-referral-program.md) 与 [买后验证页 §四](./bathtub-filter-kes-post-purchase-verification.md) 互相把「T+10–14 验证邮件」的时点推给对方——循环引用、无主。**从本页起，全站所有生命周期邮件的触发、时点与去向只在本页定义一次**；referral / 买后验证 / 订阅 / 选购器各页只引用本页时点，**不各自定义**。任何页要改邮件时序，改这里（回链修正见 §四）。

## 〇、全局规则（适用于每一封）

1. **CAN-SPAM（不可协商）**：每封含**一键可退订链接**（10 个工作日内生效，`[____ 待法务确认表述]`）+ **真实发件人 / 可回复地址** + **物理邮寄地址**；主题行不得误导；commercial 与 transactional（订单/发货确认）区分标识。
2. **红线继承全站**（[claim-register](../bathtub-filter-claim-register.md)）：🔴 禁 eczema 疗效 / 软化 / toxin-panic（「滤芯可能已失效、家人正暴露在氯中」式反向恐吓）/ scarcity 倒计时（"limited time / last chance"）/ "best value / cheapest"。读数只说**滤芯是否在工作 / 水的类型与适配**。
3. **寿命与更换口径**：一律 baths / gallons，🔴 **禁按月承诺**（[T3](./bathtub-filter-kes-page-replacement-and-lifespan.md) 口径）；「your local tap chlorine affects lifespan — verify with test strip」随行。
4. **一信一目的**：每封只有一个主 CTA；referral / UGC 只在 E3 信任峰值邮件里递，不刷屏到每封。
5. **劝退邮箱只用于承诺的那件事**（选购器 spec §五-7）：reason 枚举决定这条邮箱能收什么，不得挪作泛营销名单——数据承诺见 [SVC12 隐私页 §一](./bathtub-filter-kes-privacy-terms-and-consent.md)。
6. **频率上限 / 偏好中心**：全局频控 `[____ 待运营]`；退订粒度（全退 vs 按类退）与偏好中心 `[____ 待运营]`。
7. **ESP 选型**：`[____ 待工程]`（须支持事件触发流、referral app / 电商平台事件对接、退订同步）。
8. **时点锚定义**：T+N 的 T+0 = **物流妥投日（delivered）**，非下单日；订阅类锚 = 下期发货日。

---

## 一、生命周期总表

| # | 邮件 | 触发 | 时点 | 目的 | 关键内容 | 红线 | 埋点（utm_campaign + 下游事件） |
|---|---|---|---|---|---|---|---|
| E1 | 欢迎 / 订单确认 | 下单成功 | 即时 | 确认订单、定预期 | 订单摘要；「先别急，到货前有一件事要做（见 E2）」；定位承重句（not a water purifier / doesn't target TDS） | 不塞促销、不 upsell | `order_confirm`（transactional） |
| E2 | 发货 / 安装引导 | 物流揽收 | 发货即时 | 备好安装 + **先测「前」水** | 追踪号；[P4 安装指南](./bathtub-filter-kes-install-and-compatibility-guide.md) 链接；**关键动作：装芯前先用试纸测一杯「前」水**（没有 before 就没有 before/after） | 兼容性话术带「不支持」边界，🔴 禁 universal fit | `ship_install`；`install_guide_clicked` |
| E3 | **验证峰值邮件** ★ | 妥投后定时 | **T+10–14**（窗口内具体天数 `[____ 待运营]`） | 信任峰值收割：递分享卡话术 + 激活归因 + UGC 投稿邀请 | 见 §二 E3 详规（本页核心） | 🔴 禁 toxin-panic / 刷屏压力 / 绑好评 | `verify_peak`；`card_activated` / `ugc_submit_clicked` / `referral_share_clicked` |
| E4 | 弃购（诚实版） | 购物车放弃 | T+`[____ 待运营，建议 24h 内单封]` | 帮犹豫者**先确认适配**再买 | 「先过一遍选购器，确认 KES 适合你家水」；答疑链接（SVC1 FAQ）；如带优惠须真实非限时 | 🔴 禁倒计时 / 假库存 / scarcity；不连发轰炸（上限 `[____ 待运营]` 封） | `cart_recovery`；`selector_started` |
| E5 | 订阅发货前提醒（Skip-if-still-good） | 下期发货日前 | 发货前 `[____ 建议 7–10 天，待运营]` | 先测再决定发不发（[SVC4 §二](./bathtub-filter-kes-refill-subscription.md)） | 30 秒测法链接；**一键 Skip**（不扣款、周期顺延、无惩罚）；不操作默认行为 `[____ 待运营/法务，过 negative-option 合规]` | 🔴 禁反向恐吓催发货 | `skip_reminder`；`skip_clicked` / `ship_confirmed` |
| E6 | 换芯提醒（非订阅） | 按 baths 估算接近 soft trigger | 估算 bath 数达 `[____ 待 T3 定稿，2 ppm/周 3 泡口径 soft ≈96 baths]` 前夕 | 提示**测了再换** | 「你大概泡到第 [__] 缸了——先测，读数回升才换」；T3 触发档位链接；复购入口 | 🔴 禁按月倒计时 / 禁「已失效」断言——试纸是 ground truth | `replace_reminder`；`refill_purchased` |
| E7 | 诚实 win-back | 订阅取消 / 复购断档 | `[____ 待运营]` | 问真实原因，不打折轰炸 | 「上期滤芯还没用完？告诉我们，帮你暂停」（[SVC4 §5.3](./bathtub-filter-kes-refill-subscription.md) 拍板口径）；一键暂停 / 改周期 | 🔴 禁 toxin-panic 催回订 / 禁折扣连炸 | `winback`；`pause_clicked` / `resubscribed` |
| E8 | 劝退候补通知 | 选购器 email_capture（按 reason） | 事件驱动（V1.5 上市 / 覆盖上新 / 定期复测），见 §二 E8 | 兑现劝退时的承诺 | 按 reason 分流，见 E8 详规 | 只发承诺内容，🔴 不挪作泛营销；氯胺 claim 守 V1.5 conditional | `waitlist_{reason}`；`waitlist_converted` |

---

## 二、各邮件详规（主题行示例 EN + 正文要点）

### E1 · 欢迎 / 订单确认

> Subject: **"Order confirmed — here's what happens next."**

- 正文要点：订单摘要与预计送达；预告 E2 的「装芯前先测一杯」动作；一句定位承重句（"This is not a water purifier — it doesn't target TDS."）；客服入口。
- Transactional 属性，不塞营销内容。

### E2 · 发货 / 安装引导

> Subject: **"Your filter is on its way — do one thing before it arrives."**

- 正文要点：① 追踪链接；② **装芯前接一杯「前」水、用随盒游离氯试纸测并记下档位**（这是 [买后验证](./bathtub-filter-kes-post-purchase-verification.md) 前后对比的第一半，错过就补不回）；③ [P4 安装指南](./bathtub-filter-kes-install-and-compatibility-guide.md)（spout 兼容自查 + 不支持边界）；④ 🔴 提醒别用 TDS 笔验证。

### E3 · 验证峰值邮件（T+10–14）★ 本页核心

**这是 referral 与 proof 两条漏斗的共同触发点**——用户此刻大概率已完成安装并亲眼看过前后对比（[买后验证 §四](./bathtub-filter-kes-post-purchase-verification.md)：验证成功 = 信任峰值；[referral §四触发②](./bathtub-filter-kes-referral-program.md)：最强递卡时刻；[proof §4.3](./bathtub-filter-kes-proof-and-testimonials.md)：UGC 素材从这里长出来）。一封邮件按序做三件事：

> Subject: **"You saw the before-and-after. Someone you know is on the same water."**

**正文结构（按信任逻辑排序）：**

1. **锚定验证事实**（先确认，再开口）："You tested your water before and after the filter — you watched the number drop yourself."（没测的分支：先给 30 秒补测指引，不跳分享——**未验证不递卡**，分支判定 `[____ 待工程：是否可依据激活/购买数据分流]`）。
2. **递分享卡话术**（referral 触发②）："Know someone on the same water? There are two extra test cards in your box — hand one over."（话术池照 [referral §六 ✅ 区](./bathtub-filter-kes-referral-program.md)，逐条过 register §D「Referral 卡」行）。
3. **激活分享卡**（referral §8.1 路线 B 的关键一步）：**「Activate my cards」按钮**——点击即把盒内卡组序号归到买家名下，此后朋友扫码才计奖励；不激活的卡扫码仍进诊断漏斗，只是不计奖励。
4. **UGC 投稿邀请**（proof §4.3/§4.6）："Grab the before/after card in your box, stick your two strips on, and share it — every submission gets `[____ 奖励待市场/财务]`, whatever your result shows."——🔴 **只奖投稿不奖好评**（FTC）；附 #gifted 披露指引与 rights license 链接；可带 QR 生成器入口（proof §4.7.3）。

**红线（本封逐条核销）：**
- 🔴 禁 toxin-panic（不说「你朋友的水有危害」，只说 same water / see for yourself）；
- 🔴 禁刷屏压力（不设「转发 N 个朋友」目标）；
- 🔴 禁绑好评（奖励话术不出现 "share your great results"——负面对比同样计奖）；
- 🔴 禁 scarcity（激活与投稿均无倒计时）。

**埋点**：`verify_peak` 打开/点击、`card_activated`、`referral_share_clicked`、`ugc_submit_clicked`；下游归因沿 referral app + GA4（MVP spec §3.3）。

### E4 · 弃购（诚实版）

> Subject: **"Still deciding? First, check if KES fits your water."**

- 正文要点：不催单，先给**选购器链接**——「先确认你家是游离氯城市再买」（不适配的人被劝退掉 = 少一单错卖）；常见疑问 3 条（SVC1 FAQ 链接）；如带首单优惠，金额 `[____ 待市场/财务]` 且**长期有效不倒计时**。
- 🔴 禁：倒计时、假库存、"almost gone"、连发序列超过 `[____ 待运营]` 封。

### E5 · 订阅发货前提醒（Skip-if-still-good）

> Subject: **"Your next refill ships soon — test first. Still good? Skip it."**

- 正文要点：① 30 秒测法（前后对比链接）；② 读数仍达标 → **一键 Skip**（不扣款、顺延、不掉折扣档）；③ 读数回升 → 确认发货；④ 承重句照 [SVC4 §二](./bathtub-filter-kes-refill-subscription.md)："We'd rather you skip than replace a filter that's still good."
- 不操作的默认行为 `[____ 待运营/法务：默认发货 or 再提醒一次，须过 FTC negative-option]`。
- 🔴 禁反向恐吓催发货（"你的滤芯可能已失效"）。

### E6 · 换芯提醒（非订阅用户）

> Subject: **"Around bath [96]? Time to test your filter."**（数字 `[____ 待 T3 定稿]`）

- 触发估算：按购买日 + 用量假设（自报或默认 `[____ 待运营]` baths/周）推算接近 T3 soft trigger（2 ppm、周 3 泡口径 soft ≈96 baths）的时点——**内部用时间调度，对外话术只讲 baths**。
- 正文要点：① 「先测，别按日历换」——「后」水档位回升接近「前」水才换（[T3 触发档位](./bathtub-filter-kes-page-replacement-and-lifespan.md)）；② 你家 tap 氯浓度影响寿命（1 ppm ≈ 2× 寿命），所以试纸是 ground truth；③ 复购 / 订阅入口（可提 Skip-if-still-good 作为订阅理由）。
- 🔴 禁按月口径、禁「已失效」断言、禁 toxin-panic。

### E7 · 诚实 win-back

> Subject: **"Filter from last cycle still going? Tell us — we'll pause, not push."**

- 正文要点：① 先问真实原因（还没用完 / 不好用 / 价格 / 搬家），一键选项；② 「还没用完」→ 一键暂停 / 拉长周期（不是挽留墙，是真按钮）；③ 「不好用」→ 客服 / 退货入口（SVC3）；④ 不打折轰炸——如有回归优惠，一次性、无倒计时 `[____ 待市场]`。
- 序列时点与分支 `[____ 待运营]`（[SVC4 §5.3](./bathtub-filter-kes-refill-subscription.md) 的邮件化，机制真理源在那页，时点在本页）。

### E8 · 选购器劝退候补通知（reason 枚举对齐 [选购器 spec §2.3/§3.3](./bathtub-filter-kes-water-match-selector-spec.md)）

**原则：每条 reason 邮箱只收当初承诺的那类通知**，事件驱动、非日历驱动：

| reason | 承诺 | 触发事件 | 主题行示例 | 红线 / 备注 |
|---|---|---|---|---|
| `chloramine_wait` | V1.5 氯胺版上市通知 | 氯胺配置 flag 翻转（ship 日） | "The chloramine version is here — you asked us to tell you." | ship 前**零邮件**；ship 当日 claim 口径守 register V1.5 conditional（🔴 禁 fast/秒解）；referral 转来的券此时兑现（referral §9.1） |
| `out_of_coverage` | 覆盖你所在城市时通知 | 该 metro 数据入表（选购器 §3.2 档①→②） | "We've mapped your city's water — here's what it uses." | 结果只说消毒剂类型与适配；🔴 不 toxin-panic |
| `ro_no_value` | 仅可选复测提醒 | 留邮箱后 `[____ 待运营，建议 3–6 个月]` | "A friendly nudge: re-test your RO system." | **不推销**（选购器 §2.3 原则：RO 用户「不需要我们」——邮件只提醒复测，无加购 CTA） |
| `carbon_retest_reminder` | 几个月后提醒复测炭床 | 留邮箱后 `[____ 待运营，建议 3 个月]` | "Time to re-test your whole-house carbon — strips don't lie." | 测出氯才引到 ZIP 流；测不出 = 「your system is doing its job」，🔴 不做「再加一层更安心」推销（E11 §六口径） |
| `well_waitlist` | 井水版 GO 时通知 | 井水配置 flag 翻转 | "The well-water setup is ready — you're on the list." | GO 前零邮件；claim 守 KDF85 conditional（🔴 禁杀菌/除砷） |
| `well_out_of_scope` | 可选：专业检测指引跟进 | 留邮箱后一次性 | "Finding a certified water test near you." | 一次性资源邮件，无产品推销（能力外就是能力外） |

---

## 三、频率与冲突规则（全局调度）

- **同一收件人 7 天内营销邮件上限 `[____ 待运营]` 封**；transactional（E1/E2/发货类）不计入。
- **冲突让位**：E5（订阅提醒）与 E6（换芯提醒）互斥——订阅用户只走 E5；E3 与 E4 不可能同人同期（一个已购一个未购），但 referral 落地转化者的 E1 起点重算。
- 退订分层（全退 / 只退营销 / 只留候补通知）`[____ 待运营，偏好中心一并定]`。

---

## 四、回链修正指引（该改的两处——**本页只列不改，统一批量改**）

终审发现的循环引用，修正方向如下（改动时点：与本页首次评审同批）：

1. **[referral 页 §四](./bathtub-filter-kes-referral-program.md)**：
   - 行「②的时点 T+10–14 为建议值 `[____ 待运营与买后验证邮件序列对齐]`」→ 改为「**时点见 [[bathtub-filter-kes-email-lifecycle-spec]] E3，本页不定义时序**」；
   - 尾注「🟡 待 [运营] 补：邮件序列时点与买后验证页 §四 同步（两页别各写一套时序）」→ 删除，改为引用本页（§七 待补清单「邮件时序」行的负责方同步改为「引 SVC11」）。
2. **[买后验证页 §四](./bathtub-filter-kes-post-purchase-verification.md)**：
   - 「待补的具体数字 / 时序」第一条「何时触发验证后邀请：`[____ 待补]`（验证成功后立即弹？还是次日邮件？）」→ 改为「**邮件触发时点见 [[bathtub-filter-kes-email-lifecycle-spec]] E3**（站内弹层时点仍归本页/产品）」。

> 另注（无需改文）：[SVC4 订阅页 §二](./bathtub-filter-kes-refill-subscription.md) 的「发货前 X 天」与 [选购器 spec §3.3](./bathtub-filter-kes-water-match-selector-spec.md) 的 reason 枚举本就单向待补、无循环——本页 E5/E8 已对齐其口径，后续数字在本页定稿后回填即可。

---

## 五、待补清单（谁填什么）

| 项 | 待补 | 负责 |
|---|---|---|
| E3 具体天数（10–14 窗口内） | `[____]` | 运营 |
| E4 弃购序列封数 / 优惠金额 | `[____]` | 运营 + 市场/财务 |
| E5 发货前提前天数 / 默认行为 | `[____]`（过 negative-option 合规） | 运营 + 法务 |
| E6 用量假设与触发 bath 数 | `[____]`（依 T3 定稿） | 运营 |
| E7 win-back 序列时点与分支 | `[____]` | 运营 + 市场 |
| E8 各 reason 提醒间隔 | `[____]` | 运营 |
| 频率上限 / 退订分层 / 偏好中心 | `[____]` | 运营 |
| ESP 选型与事件对接 | `[____]` | 工程 |
| 全量主题行 / 正文定稿 | `[____]`（逐封过 register §D） | 市场 + 法务 |
| 回链修正落地（§四两处） | `[____]` | 内容运维（OPS1 流程） |

> **上线门槛**：CAN-SPAM 要件（退订/发件人/物理地址）工程验收 + 每封文案过 [claim-register](../bathtub-filter-claim-register.md) 签署 + §四回链修正完成后，方可开流。

---

## Sources / 内部依据

- [买后验证流程（验证峰值 = E3 的信任逻辑；前后对比方法）](./bathtub-filter-kes-post-purchase-verification.md)
- [推荐计划页（分享卡机制、激活式归因 §8.1 路线 B、话术红线 §六）](./bathtub-filter-kes-referral-program.md)
- [补芯订阅页（Skip-if-still-good §二、诚实 win-back §5.3、negative-option 合规）](./bathtub-filter-kes-refill-subscription.md)
- [选购器 spec（email_capture reason 枚举 §2.3/§3.3、劝退不推销原则）](./bathtub-filter-kes-water-match-selector-spec.md)
- [社会证明页（UGC 投稿机制 §4.3、FTC 只奖投稿不奖好评、#gifted 披露）](./bathtub-filter-kes-proof-and-testimonials.md)
- [T3 更换与寿命页（baths 口径、soft/strong/mandatory 触发档）](./bathtub-filter-kes-page-replacement-and-lifespan.md)
- [P4 安装与兼容性指南（E2 引导目标页）](./bathtub-filter-kes-install-and-compatibility-guide.md)
- [SVC12 隐私页（劝退邮箱用途承诺、CAN-SPAM 底座）](./bathtub-filter-kes-privacy-terms-and-consent.md)
- [claim-register（Banned：toxin-panic / scarcity / best-value / eczema / 软化；§D 表面映射）](../bathtub-filter-claim-register.md)
- [营销站内容地图（SVC11 索引位）](./bathtub-filter-kes-marketing-site-content-map.md)

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-kes-post-purchase-verification]]
- [[bathtub-filter-kes-referral-program]]
- [[bathtub-filter-kes-refill-subscription]]
- [[bathtub-filter-kes-water-match-selector-spec]]
- [[bathtub-filter-kes-proof-and-testimonials]]
- [[bathtub-filter-kes-install-and-compatibility-guide]]
- [[bathtub-filter-kes-page-replacement-and-lifespan]]
- [[bathtub-filter-kes-privacy-terms-and-consent]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-kes-marketing-site-content-map]]
