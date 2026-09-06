---
type: product
status: draft
owner: strategy
created: 2026-07-01
updated: 2026-09-05
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, subscription, refill, auto-ship, skip-if-still-good, ltv, account, policy, clean-honest]
review_cycle: monthly
related:
  - ../bathtub-filter-kes-v1-pricing-channel-launch-geo-subscription.md
  - ./bathtub-filter-kes-bundles-and-multipacks.md
  - ./bathtub-filter-kes-pricing-and-refill-economics.md
  - ./bathtub-filter-kes-returns-and-warranty.md
  - ./bathtub-filter-kes-page-replacement-and-lifespan.md
  - ./bathtub-filter-kes-post-purchase-verification.md
  - ../bathtub-filter-claim-register.md
  - ./bathtub-filter-kes-marketing-site-content-map.md
---

# 补芯订阅（Refill Subscription）· Skip-if-still-good

> 方案结构已写实；**所有价格 / 折扣 / 周期数字留 `[____ 待补]`**，由运营 / 财务 / 法务定稿后回填，未定稿不上线。

## 这页干什么

面向客户的补芯订阅（auto-ship）方案页：订阅怎么运转、**为什么每次发货前我们先让你自己测一测**（Skip-if-still-good，本订阅的招牌设计）、怎么暂停 / 跳过 / 取消、订阅 vs 一次性 vs bundle 怎么选、以及**什么情况我们劝你别订阅**。

> **口径纪律**：订阅框架参考 [V1 定价 / 订阅经济学页 §4](../bathtub-filter-kes-v1-pricing-channel-launch-geo-subscription.md)，但**具体价格 / 周期 / 折扣数字一律留空**——那页是 GTM 建议非最终定价（最终价由 finance / 供应链定）。订阅 messaging 守 [claim-register](../bathtub-filter-claim-register.md)：**复购触发靠「你自己测到该换」，不靠黑箱倒计时 lock-in**；🔴 不 scarcity、不 "best value/cheapest"、不夸大。寿命口径以 [T3 更换与寿命页](./bathtub-filter-kes-page-replacement-and-lifespan.md) 为准（**用 baths/gallons 不用月**）。

---

## 一、订阅机制（Subscription Mechanics）

| 项 | 设定 | 状态 |
|---|---|---|
| 默认周期 | `[____ 建议：2 ppm 城市 9 个月 / 1 ppm 城市 12 个月，由 ZIP 诊断分档]`（2026-09-05 由「建议 90 天」改——90 天为 T3 寿命模型消耗量的 3–6 倍；**具体档位待运营定**） | 🟡 |
| 可调周期 | 用户可自选档位 `[____ 待补]`（建议至少提供长于默认的档——低氯地区寿命更长，见 §四） | 🟡 |
| 订阅价 | `[____ 待补]`（vs 单件 `[____]`，折扣 `[____]`） | 🟡 |
| 寿命口径依据 | 以 [T3 页](./bathtub-filter-kes-page-replacement-and-lifespan.md) baths/gallons 口径为准，**不用「月」承诺**；周期档位须与真实用量假设一致 | 🟢 结构 |

> 🟡 待 [运营] 补：默认周期与可选档位；须与 T3 寿命口径一致（**用 baths/gallons 不用 months**，定价页 §4.2）。
> **护栏**：不做 long-cycle「超长寿命」故事（已被 lab 证伪，register / 定价页 §4.2）。

### 暂停 / 跳过 / 取消（承诺结构：自助、无障碍、无挽留墙）

以下三条写为**对外承诺的结构**（细节规则待补，但方向不可退让）：

1. **随时可暂停 / 跳过 / 取消**——全部**自助完成**，在账户页 `[____ 入口待补]` 点几下即可，**不需要打电话、不需要和客服周旋、没有挽留墙**（不设「确定要走吗」多层拦截漏斗）。
2. **取消不比订阅难**——订阅几步，取消就几步。
3. **无最低订阅期、无取消费** `[____ 待法务确认后写死]`。

- 暂停：`[____ 待补]`（可暂停多久 / 恢复方式）
- 跳过单次发货：一键（见 §二 Skip-if-still-good，这是主路径不是隐藏功能）
- 取消：`[____ 待补]`（入口 / 生效时点 / 已发货单如何处理，与 [退货保修页](./bathtub-filter-kes-returns-and-warranty.md) 联动）
- 修改周期 / 发货日 / 地址 / 支付方式：`[____ 待补]`

> 🟡 待 [法务/运营] 补：暂停 / 跳过 / 取消的具体规则与操作路径。
> 🟡 待 [法务] 复核：自动续订须符合 FTC「negative option」/ click-to-cancel 及各州自动续订披露要求——取消不得比订阅更难（上面第 2 条即为此承诺的对外化）。

### 账户入口

- 管理入口：`[____ 待补]`（DTC 账户页 / 订阅门户 / 客服兜底）
- 可自助操作项：改周期 / 改地址 / 暂停 / 跳过 / 取消 / 换支付方式 `[____ 范围待补]`
- Amazon 渠道订阅（如启用 Subscribe & Save）是否分开管理：`[____ 待补]`

> 🟡 待 [运营] 补：账户管理入口与自助操作范围；DTC (Shopify) 与 Amazon 管理路径可能不同（渠道见 [定价/渠道页 §2](../bathtub-filter-kes-v1-pricing-channel-launch-geo-subscription.md)）。

---

## 二、核心差异化机制：Skip-if-still-good（先测，再决定发不发）

**这是 clean-honest 订阅的招牌设计**：一般订阅的续费逻辑是「时间到了就扣款发货」；KES 的逻辑是**「你先用试纸测一下，滤芯还达标就跳过这期」**。复购触发 = **你自己测到该换了**（对应 [T3 更换触发曲线](./bathtub-filter-kes-page-replacement-and-lifespan.md) 的 soft/strong 触发档），不是黑箱倒计时。

**流程（每个订阅周期跑一遍）：**

```
发货前 X 天 [____ 建议 7–10 天，待运营定]
    │
    ▼
① 提醒邮件："Your next refill ships soon — test first."
   附 30 秒指引：用随盒游离氯试纸测一次滤后水
    │
    ▼
② 你测（前后对比法见 [买后验证页](./bathtub-filter-kes-post-purchase-verification.md)）
    │
    ├─ 读数仍达标（去氯档位未回升）──▶ ③a 邮件里一键 Skip：
    │                                    本期跳过、不扣款、周期顺延
    │                                    （跳过不惩罚、不涨价、不掉折扣档）
    │
    └─ 读数回升（接近 soft/strong 触发）──▶ ③b 确认发货：
                                          "你自己看到它衰减了" = 诚实复购
    │
    ▼
④ 不操作的默认行为：`[____ 待补：默认发货还是默认再提醒一次]`
   > 🟡 待 [运营/法务] 定：默认行为须过 negative-option 合规（不能把「沉默」当同意得太狠）
```

**对外可用措辞（英文 claim 保留）：**

> "Before every shipment, we remind you to test. **If your strip says the filter's still working, skip with one click.** We'd rather you skip than replace a filter that's still good."

**为什么这是差异化而不是自损**：
- 它把 register「Verification-by-user」信任锚从卖点延伸成**订阅机制本身**——用户不会订阅让自己失望的东西（GTM 页 §4.1）。
- 跳过省下的那期 = 用户对品牌诚实度的一次亲身验证 → 留存与转介绍资产（信任峰值逻辑同 [买后验证页 §四](./bathtub-filter-kes-post-purchase-verification.md)）。
- 财务上：跳过率假设 `[____ 待补]` 须进订阅 LTV 模型（churn 假设见 GTM 页 §6，上市 60 天后回填真实数）。

> **护栏**：提醒邮件只说「测一下再决定」，🔴 不得反向恐吓（"你的滤芯可能已失效，家人正暴露在氯中"式话术 = toxin-panic，register Banned）。读数只说滤芯是否在工作，不说健康危害。

---

## 三、订阅 vs 一次性 vs Bundle（对比框架）

| 维度 | 一次性单件 | Refill 多件装（[bundle 页 B3](./bathtub-filter-kes-bundles-and-multipacks.md)） | 订阅 |
|---|---|---|---|
| 单件价格 | `[____ 待补]` | `[____ 待补]`（多件让利来源如实，见 bundle 页 §三） | `[____ 待补]`（订阅折扣 `[____]`） |
| Per-bath 成本 | `[____ 待补]` | `[____ 待补]` | `[____ 待补]`（框架见 [SVC7](./bathtub-filter-kes-pricing-and-refill-economics.md)） |
| 发货 | 单次 | 单次（N 件一箱） | 按周期自动，**每期可测后跳过** |
| 承诺 | 无 | 无 | 可随时暂停/跳过/取消（§一） |
| 复购触发 | 自己下单 | 自己下单 | 试纸提示该换 + Skip-if-still-good |
| 适合 | 先验证 / 低频 | 用量可预测、不想绑自动扣款 | 用量稳定、想省心且按需跳过 |

> 🟡 待 [运营/财务] 补：三列价格、折扣、per-bath——**数字全部留空待定稿**（框架见 [定价页 §1.2 / §4.2](../bathtub-filter-kes-v1-pricing-channel-launch-geo-subscription.md)，建议区间非终价）。
> **护栏**：订阅折扣 messaging 讲「透明 TCO / 约一周一杯咖啡」类**价格诚实**，🔴 禁 "best value / cheapest"（触发比价）与 "limited time / while supplies last"（FTC scarcity）（定价页 §1.4、register 广告行）。

---

## 四、何时不该订阅（诚实劝退）

不是所有人都该订阅——**卖错订阅比少卖一单更贵**（churn + 信任损耗）。以下情形我们主动劝退或引导降档：

| 你的情况 | 我们的建议 | 为什么 |
|---|---|---|
| 低频使用（如每周 ≤1 次泡澡） | 拉长周期到 `[____ 档]` 或干脆一次性买 | 滤芯按 baths 计寿命（T3）；低频用户默认周期会让你囤芯 |
| 低氯地区（tap ~1 ppm） | 拉长周期或一次性 | T3 口径：1 ppm 下寿命约 2×——90 天档对你太密 |
| 还没装机验证 | 先买 Starter 测过再说 | 先确认适配与有效（[买后验证](./bathtub-filter-kes-post-purchase-verification.md)），再谈订阅 |
| 氯胺城市 | **别订**——V1 对氯胺基本无效；留邮箱等氯胺版 | 诚实劝退口径见 [T1 诊断页](./bathtub-filter-kes-page-water-test-diagnosis.md)（register Honest disqualification） |

**对外可用措辞（英文 claim 保留）：**

> "If you bathe less often, or your tap chlorine is low, a subscription may ship you more filters than you need. Stretch the cycle — or just buy one at a time. We'll tell you either way."

---

## 五、扩展方案（2026-07-01 拍板）

四个已拍板的订阅扩展机制（结构 🟢；价格 / 额度 / 细则 `[____]` 标负责方）：

### 5.1 预付年套（Prepaid Annual）

**= First-Year Kit 的订阅化**：一次预付一年滤芯（数量推导沿用 [bundle 页 B2](./bathtub-filter-kes-bundles-and-multipacks.md) 的 First-Year Kit 逻辑——按目标水型氯浓度 + 用量假设算，不拍脑袋 ×N），按订阅节奏分批发货，**每期仍走 Skip-if-still-good**（跳过则顺延，预付不等于强塞）。

- 价格：`[____ 待财务]`（vs 逐期订阅 `[____]`）
- 🔴 护栏同 bundle 页 B2：不承诺「保证一年」，限定句 + 试纸验证随行。

### 5.2 礼物订阅（Gift Subscription）

送人 **Starter + 订阅**：送礼人付款，**受赠人接管后可自由改期 / 暂停 / 取消**（§一的自助承诺对受赠人同样成立——不能让别人替你签一个你退不掉的订阅）。

- 受赠人接管流程 / 首期时点：`[____ 待运营]`
- 🟡 待 [法务] 复核：受赠人未主动同意前不得自动续扣（negative-option 合规同 §一）。

### 5.3 诚实 win-back（流失挽回）

流失挽回话术**反行业惯例**——不打折轰炸，先问真实原因（写为对外承诺）：

> "上期滤芯还没用完？告诉我们，帮你暂停。"（"Filter from last cycle still going? Tell us — we'll pause your plan, not push another box."）

- 挽回序列时点 / 分支：`[____ 待运营]`
- 🔴 挽回邮件禁 toxin-panic（不得用「你可能正暴露在氯中」催回订）。

### 5.4 订阅者特权：V1.5 氯胺版优先购名单

订阅者自动进入 **V1.5（氯胺催化炭版）与井水版的优先购名单**（产品线已 GO）。

- **口径纪律**：这里只讲**优先购资格**这一权益，🔴 **不提前认领任何氯胺去除 claim**——氯胺版效果口径仍守 [claim-register](../bathtub-filter-claim-register.md) V1.5 conditional 行，上市前不外说。
- 优先购规则（提前几天 / 是否锁价）：`[____ 待市场/运营]`

---

## 六、claim / 护栏表

| Claim / 表面 | 状态 | 护栏 |
|---|---|---|
| "Skip with one click if your strip says it's still good" | 🟢 结构（机制未建成前不上线） | 提醒邮件禁 toxin-panic；跳过无惩罚须真实成立 |
| 复购触发 = 试纸读数（不靠黑箱倒计时） | 🟢 | register Verification-by-user + Replacement-trigger；触发档位口径引 T3 |
| 周期档位与寿命口径 | 🟡 数字待补 | 用 baths/gallons 不用月；不做 long-cycle 故事 |
| "cancel anytime, no retention wall" | 🟢 结构承诺 | 🟡 法务复核 FTC negative option / click-to-cancel 后写死 |
| 订阅折扣叙事 | 🟡 数字待补 | 🔴 禁 scarcity / best-value / 虚划线；讲透明 TCO |
| 提醒邮件文案 | 🟡 待市场起草 | 读数只说滤芯是否在工作，🔴 不说健康危害；逐条过 register |
| 预付年套（§5.1） | 🟢 结构 / 🟡 价格待补 | 🔴 不承诺「保证一年」；限定句 + 试纸验证随行（同 bundle 页 B2） |
| 诚实 win-back 承诺（§5.3） | 🟢 结构承诺 | 挽回邮件 🔴 禁 toxin-panic；「帮你暂停」须真实可自助完成 |
| V1.5 优先购特权（§5.4） | 🟢 结构 | 只讲优先购资格，🔴 不提前认领氯胺去除 claim（register V1.5 conditional） |

---

## 七、待补清单（谁填什么）

| 章节 | 待补项 | 负责 |
|---|---|---|
| §一 机制 | 默认周期、档位、订阅价/折扣 | 运营 + 财务 |
| §一 暂停/跳过/取消 | 规则细节、入口、最低期（建议无）确认 | 运营 + 法务（自动续订合规） |
| §一 账户 | 管理路径、自助项、Amazon 渠道差异 | 运营 |
| §二 Skip-if-still-good | 提醒提前天数、不操作默认行为、跳过率进 LTV 模型 | 运营 + 法务 + 财务 |
| §二 提醒邮件 | 文案定稿（过 register） | 市场 + 法务 |
| §三 对比 | 三列价格与 per-bath（与 bundle 页 / SVC7 同步） | 运营 + 财务 |
| §四 劝退 | 低频/低氯档位建议值 | 运营（依 T3 定稿） |
| §五 预付年套 | 价格、分批发货节奏（与 bundle 页 B2 数量推导同步） | 财务 + 运营 |
| §五 礼物订阅 | 受赠人接管流程、首期时点、续扣合规 | 运营 + 法务 |
| §五 win-back | 挽回序列时点与分支、话术定稿（过 register） | 运营 + 市场 |
| §五 V1.5 优先购 | 优先购规则（提前期 / 锁价） | 市场 + 运营 |

> **上线门槛**：以上 `[____]` 填实 + 法务复核自动续订合规 + Skip 流程真实可用（工程验收）后，方可上线。

---

## Sources / 内部依据

- [V1 定价 / 渠道 / 首发地理 / 订阅经济学（§4 订阅框架 · 供参考，价格留空）](../bathtub-filter-kes-v1-pricing-channel-launch-geo-subscription.md)
- [T3 更换与寿命页（触发曲线 = Skip-if-still-good 的读数依据；周期须与寿命口径一致）](./bathtub-filter-kes-page-replacement-and-lifespan.md)
- [买后验证流程（前后对比测法 + 信任峰值逻辑）](./bathtub-filter-kes-post-purchase-verification.md)
- [Bundle 与多件装页（一次性多件 vs 订阅对比）](./bathtub-filter-kes-bundles-and-multipacks.md)
- [SVC7 定价与 Refill 经济学（per-bath 框架）](./bathtub-filter-kes-pricing-and-refill-economics.md)
- [T1 水质自测页（氯胺城市诚实劝退口径）](./bathtub-filter-kes-page-water-test-diagnosis.md)
- [退货 / 保修页（取消与退款联动）](./bathtub-filter-kes-returns-and-warranty.md)
- [claim-register（Verification-by-user、Replacement-trigger；Banned：scarcity / best-value / toxin-panic）](../bathtub-filter-claim-register.md)
- [内容地图（Hub-and-Spoke IA）](./bathtub-filter-kes-marketing-site-content-map.md)

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-kes-v1-pricing-channel-launch-geo-subscription]]
- [[bathtub-filter-kes-page-replacement-and-lifespan]]
- [[bathtub-filter-kes-post-purchase-verification]]
- [[bathtub-filter-kes-bundles-and-multipacks]]
- [[bathtub-filter-kes-pricing-and-refill-economics]]
- [[bathtub-filter-kes-page-water-test-diagnosis]]
- [[bathtub-filter-kes-returns-and-warranty]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-kes-marketing-site-content-map]]
