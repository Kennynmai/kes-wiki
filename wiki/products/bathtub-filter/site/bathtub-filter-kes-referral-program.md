---
type: product
status: draft
owner: strategy
created: 2026-07-01
updated: 2026-07-01
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, referral, share-the-test, test-strip, acquisition, growth, waitlist, compliance]
review_cycle: monthly
related:
  - ../bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md
  - ./bathtub-filter-kes-pack-contents-spec.md
  - ./bathtub-filter-kes-post-purchase-verification.md
  - ./bathtub-filter-kes-page-water-test-diagnosis.md
  - ./bathtub-filter-kes-bundles-and-multipacks.md
  - ./bathtub-filter-kes-proof-and-testimonials.md
  - ../bathtub-filter-kes-acquisition-engine-mvp-spec.md
  - ./bathtub-filter-kes-refill-subscription.md
  - ../bathtub-filter-claim-register.md
  - ./bathtub-filter-kes-marketing-site-content-map.md
---

# KES 浴缸过滤器 · 推荐计划（Referral Program）· Share-the-Test 分享试纸卡

> 方案结构已写实；**所有奖励 / 折扣数字留 `[____ 待补]`**，由市场 / 财务定稿后回填，未定稿不上线。

## 这页干什么

把「推荐朋友」做成 KES 的主获客通道之一（承接 [获客引擎 §七](../bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md) referral 漏斗）。核心机制是**分享试纸卡（Share-the-Test）**：推荐的载体不是裸的「推荐有礼」链接，而是**一件有用的小物**——一张能让朋友 30 秒看见自家水里游离氯档位的卡。**推荐链接本身就是一份有用的诊断入口，这是它能转起来的原因**（获客引擎 §7.1 逻辑的实体化）。

> 🟡 待 [市场/运营] 补：本页定稿前先确认推荐计划纳入 V1 首发还是 post-launch（获客引擎 §7.6 分期：MVP ~2–4 周可用现成 referral app 起步）。

---

## 一、核心机制：分享试纸卡（Share-the-Test Card）

**盒内附 3 张独立封装分享卡**（已提案进 [P2 套装内容规格页 #10](./bathtub-filter-kes-pack-contents-spec.md)，🟡 待产品确认进 BOM）。每张卡 =

| 组成 | 说明 |
|---|---|
| 1 条**游离氯试纸** | 独立铝箔封装（防潮，可放钱包/口袋）——**粗筛教育工具，不是实验室检测** |
| 极简读色说明 | 卡面印色阶条 + 一句读法；30 秒完成 |
| **唯一二维码** | 每卡一个唯一推荐码 → 扫码进 ZIP 诊断流程（归因见 §五） |

**设计要点（给设计的 brief 方向）：**

- **是「可赠予的小物」，不是散耗材**：独立封装、卡片质感、能塞进钱包——递出去像送一件小东西，不像撕给朋友一条耗材。
- **卡面文案方向 = 教育框架**："See what's in your water."（「看看你家的水」）——好奇心钩子，🔴 **非恐吓**（不出现毒/危害/伤害字样）。
- 卡面自带诚实边界一句：**"A quick guide, not a lab test."**（register Self-diagnosis 原文）。
- 卡面设计稿：`[____ 待补]`

> 🟡 待 [设计] 补：卡面视觉与文案稿；定稿前逐条过 [claim-register §D「Referral 卡」行](../bathtub-filter-claim-register.md)。
> 🟡 待 [产品/供应链] 补：分享卡进 BOM 确认（数量 3 张为提案值；成本分币级，复用既有试纸供应链，获客引擎 §7.3：免费试纸 ≈ $0.3 + 邮费，远低于付费 CAC）。

---

## 二、朋友旅程（Friend Journey）

```
① 拿到卡（朋友/邻居递的一件小物）
    ▼
② 测自家龙头水：试纸蘸水 → 对卡面色阶 → 看到自家游离氯档位
   （30 秒、零门槛；教育框架："huh, so that's my water"）
    ▼
③ 扫卡上二维码（带唯一推荐码）
    ▼
④ ZIP 诊断（路径 A，30 秒；流程见 [T1 诊断页](./bathtub-filter-kes-page-water-test-diagnosis.md)）
   → 消毒剂类型（权威）+ 硬度档 + 「你家水型」结果
    ▼
⑤ 分岔（诚实路由）：
   ├─ 游离氯城市（适配）──▶ 适配建议 + 首单优惠 `[____ 待补]`
   │                        > 🟡 待 [市场/财务] 补：朋友端首单激励形式与额度
   │
   ├─ 氯胺城市──▶ 诚实劝退："V1 isn't for your water yet."
   │              → 留邮箱等氯胺版（V1.5 候补名单）
   │
   └─ 软化需求──▶ 说明只阻垢不软化（"It does not soften your water."）
                  → 如实给方向（真软化 = 全屋软水器品类）
```

**劝退也是获客（这层价值写明）**：氯胺城市的劝退邮箱 = **V1.5 上市当天的种子名单**——这些人已经完成了「朋友背书 + 亲手测过 + 被诚实对待」三重预热，是转化率最高的候补池。劝退不是漏斗损耗，是**把不能卖的今天变成能卖的明天**，同时让推荐人放心递卡（不会坑朋友买错）。

> **护栏**：⑤ 的所有分支话术守 register：读数只说**水的类型 / 产品适配**，🔴 不说「你的水有危害」；试纸 = 粗筛教育工具，不冒充检测。

---

## 三、推荐人旅程（Referrer Journey）

| 环节 | 设定 | 状态 |
|---|---|---|
| 拿到卡 | 随盒 3 张（§一）；补领渠道 `[____ 待补]` | 🟡 |
| 奖励形式 | `[____ 建议方向：refill credit（下次换芯抵扣）]`——挂**复购**不挂现金，把转介绍接进复购飞轮（获客引擎 §7.3） | 🟡 |
| 奖励额度 / 上限 | `[____ 待补]`（需与 CAC/margin 对齐） | 🟡 |
| 发放时点 | `[____ 待补]`（建议过退货期后发放，防刷） | 🟡 |
| 追踪面板 | `[____ 待补]`（账户页看每张卡状态：已扫码 / 已诊断 / 已下单 / 奖励已发；技术栈建议用现成 referral app——Friendbuy / Refersion / Yotpo，获客引擎 §7.5） | 🟡 |

> 🟡 待 [市场/财务] 补：奖励形式、额度、上限、发放时点。
> 🟡 待 [工程/运营] 补：追踪面板与状态口径（pending / 已确认 / 已发放）。

---

## 四、双触发：什么时候递卡话术（Timing）

照获客引擎 §7.2「验证峰值是最强触发点」：

| 触发点 | 载体与话术方向 | 强度 |
|---|---|---|
| **① 开箱** | 说明书一句话："Three test cards are in the box — one for you to keep, two for friends who wonder about their water." + 指向卡袋 | 中（种下认知） |
| **② T+10–14 买后验证邮件** | 用户刚按 [买后验证流程](./bathtub-filter-kes-post-purchase-verification.md) 亲眼看过前后对比、**信念最强**的时刻递话术："You just saw the before-and-after yourself. Know someone on the same water? Hand them a test card." | **最高（信任峰值）** |

- ②的时点（T+10–14，T+0=妥投日）**归 [邮件生命周期 spec E3](./bathtub-filter-kes-email-lifecycle-spec.md) 唯一定义**——本页只引用、不定义（2026-07-02 收编，改时序去那页改）。
- 同 metro 协同（获客引擎 §7.4）：首发 P1 城市内邻居同水务，「你邻居家也是同样的水」是最强社会证明——但话术只说**同样的水**，🔴 不说危害。

> 邮件时序唯一 owner = [SVC11 邮件生命周期 spec](./bathtub-filter-kes-email-lifecycle-spec.md)（2026-07-02 起；此前本页与买后验证页循环引用已收编）。

---

## 五、归因（Attribution）

- **每卡唯一码**：二维码即推荐码，扫码落地即绑定推荐人；无需朋友手动输码。
- 卡→扫码→诊断→下单全链路状态回写推荐人面板（§三）。
- 线上分享兜底：账户页可生成个人链接（给没拿到实体卡的场景）`[____ 待补]`。
- 技术实现：referral app + UTM + GA4（获客引擎 §7.5，不自研）。

> 🟡 待 [工程] 补：二维码码池生成 / 绑定 / 防滥用规则。

---

## 六、话术红线表（🔴 禁 / ✅ 可用）

推荐是对外表面，**继承 [claim-register](../bathtub-filter-claim-register.md) 全部红线**（§D「Referral 卡」行 + 广告行）。分享话术与朋友端落地页 ship 前逐条核销：

| 类型 | 规则 |
|---|---|
| 🔴 toxin-panic / 健康恐吓 | 禁「你朋友家的水有毒 / 伤害宝宝 / 家人在暴露中」式话术促分享；读数只说类型/适配 |
| 🔴 夸大 claim | 禁 eczema 疗效 / 软化 / 除 PFAS / 除「上百种污染物」/ 杀菌 / baby-safe；成品未 NSF 认证口径继承 |
| 🔴 刷屏压力 | 不制造「快转发给 10 个朋友」式社交压力；framing = 帮朋友搞清自家水，不是「赚钱刷朋友」 |
| 🔴 伪精确 | 试纸 = 粗筛教育工具；禁把分享卡说成「检测你水里的危害」；禁 TDS 笔 / 铅试纸 |
| 🔴 scarcity | 奖励不做「限时冲刺 / 名额有限」倒计时 |
| ✅ 教育 / 好奇心框架 | 类型与适配、透明、「自己测得到」叙事；social proof 须真实可核（[proof 页](./bathtub-filter-kes-proof-and-testimonials.md)） |

**✅ 可用示例话术（英文，供卡面 / 邮件 / 用户转述参考）：**

> "Curious what's in your water? This strip shows your free-chlorine level in about 30 seconds — a quick guide, not a lab test."

> "I tested my bath water before and after the filter and watched the number drop. Try the strip on your own tap and see what you're working with."

> "It's not for everyone — scan the code, and if it doesn't fit your water, it'll tell you that too."

> 🟡 待 [法务/市场] 补：话术模板定稿后逐条过 claim-register §D「Referral 卡」行签署。

---

## 七、待补清单（谁补什么）

| 项 | 待补 | 负责 |
|---|---|---|
| 朋友端首单激励 | 形式与额度 `[____]` | 市场 + 财务 |
| 推荐人奖励 | refill credit 额度 / 上限 / 发放时点 `[____]` | 市场 + 财务 |
| 追踪系统 | referral app 选型、码池、面板、防滥用 | 工程 + 运营 |
| 卡面设计 | 视觉 + 文案稿（过 register §D） | 设计 + 法务 |
| 分享卡进 BOM | 数量 / 封装 / 成本确认（P2 #10 提案） | 产品 + 供应链 |
| 邮件时序 | 归 [SVC11 E3](./bathtub-filter-kes-email-lifecycle-spec.md) 唯一定义 | 运营（在 SVC11 定稿） |
| 首发范围 | V1 首发即开 or post-launch | 市场 + 运营 |

> **上线门槛**：以上 `[____]` 填实 + 话术全量过 register §D 签署 + 归因链路工程验收后，方可上线。

---

## 八、归因码技术实现（2026-07-01 拍板）

> 本节细化 §五 归因：把「每卡唯一码」从一句话落成可执行的技术方案。选型基线沿用 [获客引擎 MVP spec](../bathtub-filter-kes-acquisition-engine-mvp-spec.md)（现成 referral app + §4 数据模型，不自研核心）。

### 8.1 两条实现路线（MVP 建议 B，量大转 A）

| | **路线 A：履约扫码绑定** | **路线 B：激活式（MVP 建议）** |
|---|---|---|
| 卡与推荐人怎么绑 | 印刷时每卡唯一码（VDP / 标签唯一码）→ 派生**盒序列号 + 卡位 A/B/C**；打包时**扫盒码绑订单** → 朋友扫卡即可解析 **码 → 盒 → 订单 → 推荐人** 全链 | 卡上码**不预绑任何人**；买家在 **T+10–14 验证邮件**里点一下「激活我的分享卡」，把自己盒内卡组序号归到自己名下 |
| 履约改造 | 需要（打包环节加一次扫码动作） | **零履约改造** |
| 归因率 | 高（无需买家动作） | 略降（依赖买家激活；未激活的卡扫码仍进诊断漏斗，只是不计推荐奖励） |
| 适用阶段 | 量大 / 履约流程可控后切换 | 试点 / MVP 首选 |

> 🟡 待 [工程/运营] 定：A/B 切换的量级阈值与履约方评估。

### 8.2 自印设备三档（唯一码怎么印出来）

**核心原则：卡主体批量印刷、零变量；唯一性只集中在一枚小标签上——把可变成本压到最低。**

| 档 | 方案 | 成本 | 适用 |
|---|---|---|---|
| ① | 办公激光打印机 + Avery 标签纸 + CSV 邮件合并（mail merge） | ≈ 0（现有设备） | 试点 / 几百张以内 |
| ② | 热敏标签机（Zebra ZD421 / Brother QL-820）+ ZebraDesigner / BarTender，从 CSV 批量出唯一码小标签，**贴到批量印刷的卡主体上** | $150–400 一次性 | **推荐**：起量前的主力方案 |
| ③ | CSV 交印厂做 VDP（可变数据印刷），码直接印进卡 | 按印厂计价 | 数千张以上 / 与路线 A 配套 |

### 8.3 码规格与防滥用

- **码格式**：8 位 base32（去易混字符）+ 校验位——**防顺序猜测**，扫错/输错可即时判无效。
- **URL**：`kes.com/t/{code}`（短、可手输兜底）。
- **卡上零 PII**：卡面只有码，码 → 盒 → 订单 → 推荐人的映射**只存服务端**；卡丢了不泄露任何人信息。
- **防滥用规则**（结构 🟢，阈值 🟡 待运营）：
  - 一码一兑（每码只能兑现一次奖励）；
  - 每盒 3 张 = 每单奖励上限的物理天花板；
  - 码有效期 `[____ 待运营]`；
  - **同址 / 支付指纹拦自荐**：朋友订单与推荐人订单同收货地址或同支付指纹 → 不计奖励。

> 🟡 待 [工程] 补：码池生成脚本、服务端映射表、防滥用阈值落库（数据模型对齐 [MVP spec §4](../bathtub-filter-kes-acquisition-engine-mvp-spec.md)）。

---

## 九、双边奖励机制（具体，2026-07-01 拍板）

> 机制结构已拍板（🟢）；**所有额度数字留 `[____]`**，负责方标注在行内。本节把 §三 表格里的「奖励形式建议方向」落成确定机制。

### 9.1 朋友端（Friend side）

- 路径：扫码 → ZIP 诊断 → 判定适配 → **首单减免在结账自动带入**（码已在 URL 里，**无需手输**）；额度 `[____ 待市场/财务]`。
- **劝退分岔也有交代**：氯胺城市 / 不适配 → 诚实劝退 + 留邮箱，**这张券自动转为 V1.5 预售资格**（券不作废，跟人走到氯胺版上市日）。

### 9.2 推荐人端（Referrer side）

| 机制 | 设定 | 状态 |
|---|---|---|
| 单次奖励 | 朋友首单**过退货窗（`[__]` 天）后**，自动记一笔 **refill credit** `[____ 待市场/财务]` | 结构 🟢 / 额度 🟡 |
| 可叠加 | credit 可累计，**叠至一支免费 refill** | 🟢 |
| 里程碑 | **3 位朋友成交 → 免费 refill 套装** | 机制已拍板 🟢 / 套装内容与额度 `[____ 待市场/财务]` |

**为什么用 refill credit 而不是现金**（写明，供内部对齐）：

1. **成本 = COGS 不是面值**：一笔 credit 的真实成本是滤芯成本，远低于等面值现金；
2. **贴合换芯周期**：奖励在用户下一次换芯时兑现，等于把转介绍**接进复购节奏**；
3. **强留存**：credit 只在 KES 体系内有价值——推荐得越多，越没有理由流失（获客引擎 §7.3 飞轮逻辑）。

### 9.3 发放与叠加规则

- **发放时点 = 朋友订单过退货窗**（`[__]` 天，与 [退货保修页] 口径对齐）——**防刷单**：下单即发会被「下单-退货」套利。
- 奖励与**订阅折扣**的互斥 / 叠加规则：`[____ 待运营]`（须与 [订阅页](./bathtub-filter-kes-refill-subscription.md) 定价定稿同步，别出现双重折上折漏洞）。

> 🔴 护栏继承 §六：奖励机制不做 scarcity 倒计时、不做「冲刺排行榜」社交压力；奖励只挂**成交**，不挂好评（FTC 红线详见 [proof 页 UGC 节](./bathtub-filter-kes-proof-and-testimonials.md)）。

---

## Sources / 内部依据

- [水质自测套件 / 模块化获客引擎（§五 生命周期、§七 referral 机制 / 触发 / 激励 / 技术栈）](../bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md)
- [P2 套装内容规格页（分享试纸卡 #10 提案行）](./bathtub-filter-kes-pack-contents-spec.md)
- [买后验证流程（T+10–14 信任峰值触发、验证方法）](./bathtub-filter-kes-post-purchase-verification.md)
- [T1 水质自测 / 诊断页（扫码后 ZIP 诊断与诚实劝退口径）](./bathtub-filter-kes-page-water-test-diagnosis.md)
- [Bundle 页（Gift bundle 含额外分享卡）](./bathtub-filter-kes-bundles-and-multipacks.md)
- [社会证明 / testimonials（落地页 social proof 须真实可核；UGC 投稿 FTC 红线）](./bathtub-filter-kes-proof-and-testimonials.md)
- [获客引擎 MVP spec（referral app 选型 §3.3、数据模型 §4、KPI §6）](../bathtub-filter-kes-acquisition-engine-mvp-spec.md)
- [补芯订阅页（奖励与订阅折扣叠加规则联动）](./bathtub-filter-kes-refill-subscription.md)
- [claim-register（§D Referral 卡行、广告行；Banned：toxin-panic / 夸大 / scarcity）](../bathtub-filter-claim-register.md)
- [营销站内容地图（IA）](./bathtub-filter-kes-marketing-site-content-map.md)

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine]]
- [[bathtub-filter-kes-pack-contents-spec]]
- [[bathtub-filter-kes-post-purchase-verification]]
- [[bathtub-filter-kes-page-water-test-diagnosis]]
- [[bathtub-filter-kes-bundles-and-multipacks]]
- [[bathtub-filter-kes-proof-and-testimonials]]
- [[bathtub-filter-kes-acquisition-engine-mvp-spec]]
- [[bathtub-filter-kes-refill-subscription]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-kes-marketing-site-content-map]]
