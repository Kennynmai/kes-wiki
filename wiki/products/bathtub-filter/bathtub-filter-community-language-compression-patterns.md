---
type: product
status: draft
owner: strategy
created: 2026-04-17
updated: 2026-04-17
visibility: team
confidence: medium-low
officiality: draft
domain: product
domains: [bathtub-filter, language, copy, voice-of-customer, conversion, claim-risk]
source_count: 14
review_cycle: monthly
verification_status: working
related:
  - ./bathtub-filter-reddit-community-signal-sampling.md
  - ./bathtub-filter-sns-creator-and-visual-taxonomy.md
  - ./bathtub-filter-marketplace-negative-review-signals.md
  - ./bathtub-filter-review-patterns-and-return-risk.md
  - ./bathtub-filter-complaint-taxonomy-and-risk-by-route.md
  - ./bathtub-filter-claim-risk-audit-v2.md
  - ./bathtub-filter-research-coverage-gaps.md
---

# Bathtub Filter — 社区语言压缩 / 情感转换模式

## 为什么有这页

Gap doc Tier 3 #9 列出"社区语言压缩和情感转换模式"为遗漏层。该层的目的：

> **把分散在 Reddit / 评论 / TikTok / 育儿媒体的真实用户语言，压缩成 KES 可直接套用的 page copy / ad copy / packaging copy 句式骨架——同时给每个骨架打上 claim-risk tag，告诉 copy 团队哪些可用、哪些必须改、哪些必须避开。**

不做这一步的代价：copy 团队要不就**模仿 FilterBaby/Canopy 句式（继承别人的合规风险）**，要不就**写工程语言转化不动**。

## 1. 数据基础边界

本页 verbatim 来自 4 个来源，confidence 区分如下：

| 来源 | 数量 | Confidence |
|---|---|---|
| 现有 review-patterns / complaint-taxonomy 页 | ~30 短语 | 中（已二次综合） |
| Reddit / 社区 indirect 引用（详见 reddit-sampling 页） | ~15 短语 | 低（间接来源 + selection bias） |
| 品牌官网 customer review（Canopy / Tubo / FilterBaby / Santevia） | ~12 短语 | 中（品牌已 curated） |
| TikTok 视频标题 + 创作者 caption（filter.baby / Ciara Deanne / jazzybsway / mindbodygreen） | ~10 短语 | 高（直接抓取） |

> ⚠️ Reddit 直接采样未完成（见 reddit-sampling 页协议）。本页**不是 voice-of-customer 的最终版**——人工 Reddit 采样完成后必须回写更新。

## 2. 情感骨架（语言压缩成 6 个核心 emotion arc）

每个骨架包含：触发情绪 / 高频句式模板 / 真实出处 / 改写候选 / claim-risk tag。

---

### 骨架 1 — "我之前不知道" (revelation / 震惊)

**触发情绪：** 信息差被打破。"原来这件事一直在我家里发生我都不知道。"

**高频模板：**
- "I can't believe how much [X] was in my [Y]"
- "I had no idea [Y] was this [adjective]"
- "Y'all I just found out [statement]"

**Verbatim 出处：**
- "I can't believe how much Chlorine was in my tap water 😳" — @filter.baby (TikTok)
- "the chlorine test that shocked me" — Ciara Deanne (blog title)
- "essentially feels like pool water" — listicle 引用 r/SkincareAddiction

**改写候选（KES 可用）：**
- "我之前根本不知道自来水里的氯能多到这种程度"
- "做了一次氯检测才知道我之前洗澡用的水是这个状态"
- "看到测试结果之后，洗澡这件事再也回不去了"

**Claim-risk tag：** 🟢 **低** — 描述事实（自来水含氯），不暗示效果

**视觉配套：** chlorine drop test 视频 / GIF 必须同框

---

### 骨架 2 — "终于不再 [负面状态]" (relief / 解脱)

**触发情绪：** 长期忍受 → 终于松口气。是 high-LTV mom 用户最强情感锚。

**高频模板：**
- "noticed [X-time] later [my Y is less Z]"
- "since [installing X], [problem] has been [reduced]"
- "[problem] stopped being a trigger"

**Verbatim 出处：**
- "noticed fewer flare-ups once using it consistently" — Ciara Deanne (Canopy 60-day review)
- "since [installing softener], I've only used steroids twice on areas that used to be covered in eczema" — softener vendor 引用 personal account
- "bath time stopped being such a trigger" — softener marketing 引用
- "feels less dry / softer / gentler" — review-patterns 综合

**改写候选（KES 可用）：**
- "用了几周之后，孩子洗完澡不再频繁挠"（⚠️ 仍需 legal）
- "皮肤洗完不再那么紧绷"
- "洗澡这件事不再是每天担心的事"
- "孩子开始喜欢洗澡了"

**Claim-risk tag：** 🟡 **中** — "less flare-up" 是 medical implication 边界。**安全替代：用 sensory 词（紧绷 / 干 / 痒感觉）替代 medical 词（湿疹 / 红疹 / 病情）**

**绝对避开：**
- ❌ "cleared up my eczema"
- ❌ "got rid of my eczema"
- ❌ "no more flare-ups"
- ❌ "treats / cures / heals"

---

### 骨架 3 — "现在终于安心了" (peace of mind / 父母焦虑解压)

**触发情绪：** 父母责任焦虑被卸下。**这是 KES baby-line 最高转化情感**。

**高频模板：**
- "peace of mind knowing [problem] won't [bad outcome]"
- "I don't worry about [Y] anymore"
- "one less thing to think about during [routine]"

**Verbatim 出处：**
- "peace of mind knowing bath time isn't going to compromise their child's skin" — Canopy customer review
- "after five months of use ... peace of mind" — Canopy customer
- "the best parenting decisions are the ones that just make life a tiny bit easier" — Motherly on Canopy

**改写候选（KES 可用）：**
- "洗澡时间不再是每天要担心的一件事"
- "晚上给孩子洗澡时，至少水这件事我不用再想"
- "做父母要操心的事够多了，水至少不再是其中之一"

**Claim-risk tag：** 🟢 **低**（情绪而非效果） — 但配图若用 baby/eczema 患处，立即升 🔴

**视觉配套：** 浴缸内 toddler 背影 / 侧面（避正面 + 患处特写）

---

### 骨架 4 — "我决定不再让 [X] 接触我的 [Y]" (主权 / boundary)

**触发情绪：** 用户从被动接受 → 主动选择。Skincare-aware 女性用户最强情绪。

**高频模板：**
- "I'm not letting [X] touch my [Y]"
- "I decided [X] isn't going near my [Y] anymore"
- "[X] doesn't get to [verb] my [Y]"

**Verbatim 出处：**
- "You're mistaken if you think I'm letting that and Chlorine onto my skin 🙅🏻‍♀️" — @filter.baby
- Reddit 引用：parent-to-parent 互劝 "don't let chlorine on baby skin"

**改写候选（KES 可用）：**
- "我决定不让自来水里的氯继续接触我家孩子"
- "孩子的皮肤不应该每天泡在含氯的水里"

**Claim-risk tag：** 🟢 **低** — 价值观陈述。**仅当配「治愈了 X」类后续陈述时升 🔴**

---

### 骨架 5 — "[设计/安装]居然这么 [简单/低调]" (design-relief / 反惊喜)

**触发情绪：** 对类目预期是"丑 / 复杂 / 妨碍设计"，结果反差。

**高频模板：**
- "blends seamlessly into your space rather than screaming '[category]'"
- "easier than I thought"
- "doesn't look like [stereotype]"

**Verbatim 出处：**
- "blends seamlessly into your space rather than screaming 'baby gear'" — Motherly (Canopy)
- "installation takes less than 5 minutes" — multiple reviews
- "comes in colors like Oat, Jade, and Lavender, designed to blend seamlessly" — Motherly

**改写候选（KES 可用）：**
- "装上去看起来不像母婴产品"
- "5 分钟装好，跟浴室原本的金属件融合"
- "不刺眼、不抢戏，是浴室里 hide in plain sight 的一件家具"

**Claim-risk tag：** 🟢 **低** — 美学陈述，可自由用

---

### 骨架 6 — "X 比我以为的更值/不值" (price legitimacy)

**触发情绪：** 用户对价格的事后合理化。**决定 review 的 star + word-of-mouth**。

**高频模板：**
- "$X is worth it if [condition]"
- "you can get one for $X — not bad"
- "$X is a lot, but [reason]"

**Verbatim 出处：**
- "if your hair feels stiff no matter how much conditioner you use, [a filter] is worth the $50–$150" — Reddit aggregator
- "You can get one on Amazon for like $30 ... made a big difference ... worth it" — Reddit aggregator
- "Canopy filter costs $89 ... four times more expensive than Santevia ... don't think it offers the best value" — Water Filter Guru

**改写候选（KES 可用）：**
- 价格 anchor 必须**主动给条件**：
  - "如果你家是硬水/重氯地区，这个价格值"
  - "如果你 routine 里水占比很高（baby / eczema / skincare），这个价格 vs 你年付的护肤品/药费 是低的"
- ❌ 不要写 "best value" / "best in class" 这种比较级 — 直接触发 Water Filter Guru-style rebuttal

**Claim-risk tag：** 🟢 **低** — 但比较级触发 FTC substantiation 要求

---

## 3. 用法矩阵：哪个骨架放在哪个 surface

| Surface | 推荐骨架 | 避免 | 原因 |
|---|---|---|---|
| Product page hero | 骨架 1 (revelation) + 骨架 5 (design) | 骨架 2 (relief 太晚) | hero 必须解决 awareness 不解决 trust |
| Product page proof section | 骨架 6 (price legitimacy) + 骨架 3 (peace of mind) | 骨架 4 (主权太抽象) | 已被吸引的用户找理由 |
| Amazon listing bullet 1 | 骨架 5 (design + install) | 骨架 1 (Amazon 用户已 aware) | A9 SEO + 立即缓解购买犹豫 |
| Amazon listing bullet 2-3 | 骨架 6 (price + condition) | 骨架 2 (FDA 风险高 + Amazon 政策严) | 平台审查 |
| TikTok / Reels hook (3 秒) | 骨架 1 (revelation) | 骨架 3 (peace of mind 是 closer) | hook 必须有 "wait what" |
| TikTok / Reels closer | 骨架 4 (boundary) + 骨架 3 (peace of mind) | 骨架 6 (价格在 SNS 是 conversion-killer) | 情绪 close > 价格 close |
| Email nurture (post-purchase) | 骨架 2 (relief) + 骨架 3 (peace of mind) | 骨架 1 (用户已经买了) | 已下单用户需要"我做对了"确认 |
| Packaging copy | 骨架 5 (design) + 骨架 3 (peace of mind) | 骨架 1 (开箱已 too late) | 已购用户 unboxing 时 reinforce |
| Influencer brief | 骨架 1 + 骨架 5 必带；骨架 2 必须改写过 | 骨架 2 raw + 骨架 6 比较级 | 防止合作创作者带火 medical claim |
| FTC/legal review priority | 骨架 2 + 骨架 3 (config baby) | — | medical implication 风险最高 |

## 4. 必须避开的 12 个具体词（black list）

来自 [[bathtub-filter-claim-risk-audit-v2]] + 本页综合：

| 词 / 短语 | 风险 | 安全替代 |
|---|---|---|
| eczema | FDA medical | "sensitive skin" / "dry skin" / "skin that gets irritated" |
| cleared up / healed / cured | FDA medical | "felt softer" / "felt less tight" |
| treat / treats / treatment | FDA medical | "gentler routine" / "everyday care" |
| prevent / prevents | FDA medical | "supports" (lower-bar 但仍 risky) |
| safe for babies / baby-safe | CPSIA labeling trigger | "designed with families in mind" / "tool-free install" |
| doctor-recommended (无具体来源) | FTC endorsement | "tested by [specific lab name]" |
| 99.9% removes [list] (无 cert) | NSF/FTC substantiation | "in lab testing reduced free chlorine by [%] under [condition]" |
| best [anything] | FTC comparison | "designed to [function]" |
| dermatologist-tested (无文档) | FTC endorsement | "tested by [specific party]" |
| medical grade | FDA Class I/II 边界 | "consumer-grade" / "household" |
| natural / chemical-free | FTC green guides | "[specific ingredient]-free" |
| FDA-approved (无 510k) | FDA fraud | 不用 |

## 5. 已经够用的（不需再深挖的）

基于上述压缩，**KES copy team 现在可以做**：
- 6 个 emotion arc 的 first-draft Amazon listing
- 3 套差异化 product page hero
- 1 个 SNS hook 池子（10 条变体）
- packaging short-copy 候选
- influencer brief 模板（含 black-list）

## 6. 还卡在哪里（必须人工/外部完成）

- [ ] Reddit 真实采样完成 → 回写本页（情绪簇可能漂移）
- [ ] FTC + FDA 文案 legal review（外部 counsel）
- [ ] A/B 测：6 个 emotion arc 在实际广告中的 CTR / 转化率
- [ ] 中文消费者市场版本（如 KES 进 CN/TW，emotion arc 会重排）

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-reddit-community-signal-sampling]]
- [[bathtub-filter-sns-creator-and-visual-taxonomy]]
- [[bathtub-filter-marketplace-negative-review-signals]]
- [[bathtub-filter-review-patterns-and-return-risk]]
- [[bathtub-filter-complaint-taxonomy-and-risk-by-route]]
- [[bathtub-filter-claim-risk-audit-v2]]
- [[bathtub-filter-visual-merchandising-and-creative-strategy]]
- [[bathtub-filter-research-coverage-gaps]]
