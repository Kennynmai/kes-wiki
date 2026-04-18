---
type: product
status: draft
owner: strategy
created: 2026-04-17
updated: 2026-04-17
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, creative, ab-testing, creator-partnership, gtm, brief, contract-template]
source_count: 4
review_cycle: as-needed
verification_status: working
related:
  - ./bathtub-filter-visual-merchandising-and-creative-strategy.md
  - ./bathtub-filter-sns-creator-and-visual-taxonomy.md
  - ./bathtub-filter-community-language-compression-patterns.md
  - ./bathtub-filter-claim-risk-audit-v2.md
  - ./bathtub-filter-research-coverage-gaps.md
---

# Bathtub Filter — A/B 创意测试 brief + 创作者合作模板

## 为什么有这页

Gap doc H 层（视觉营销 / 创意策略）此前是 🟡 框架 + ❌ 缺页。SNS creator taxonomy 已建（[[bathtub-filter-sns-creator-and-visual-taxonomy]]），language compression 已建（[[bathtub-filter-community-language-compression-patterns]]），但**没有把策略落到可执行 artifact**。

这页落两件事：

1. **A/B 创意测试 brief 模板**——KES launch 前后必须执行的 split test，确定 winning narrative
2. **创作者合作 brief + 合同条款骨架**——product seeding 时直接发给创作者的标准模板，含 claim-risk black list

## 1. A/B 创意测试 brief 模板

### 1.1 测试目标

> 确定 KES V1 在目标受众上**单条创意 → 转化**最强的 narrative，并定位 "winning hook + winning visual + winning closer" 组合，作为 6 个月内 paid 内容的 master template。

### 1.2 测试结构（recommended：3×3 factorial，最少 9 cells）

| Hook 维度（3 选）| Closer 维度（3 选）|
|---|---|
| H1 — Revelation：Chlorine drop test demo | C1 — Peace of mind：父母焦虑解压 |
| H2 — Boundary：" 我决定不让 X 接触我家孩子" | C2 — Sensory relief：洗完不紧绷 |
| H3 — Design surprise："不像母婴产品" | C3 — Price legitimacy：$59 < 1 月护肤品 |

每个 cell = 1 个 15-30 秒 video + 1 个 carousel + 1 个 static image。

### 1.3 各维度 verbatim 起手稿（直接来自 [[bathtub-filter-community-language-compression-patterns]] 6 个 emotion arc）

**H1 — Revelation hook（3 秒内）：**
- video 开头：DPD 试剂滴入透明杯 → 自来水变黄
- 字幕："I had no idea my tap water was *this* much chlorine"
- 切：滴入过滤后的水 → 不变色
- 字幕："and the same drop, after our filter"

**H2 — Boundary hook：**
- video 开头：成人 POV 看自来水流出
- 字幕："I'm not letting *that* into my kid's bath anymore"
- 切：装上 KES，水流过
- 字幕："this is what we use now"

**H3 — Design surprise hook：**
- video 开头：浴室广角镜头
- 字幕："you wouldn't even know there's a filter here"
- 切：zoom in 到 KES 在 spout 上
- 字幕："5 minutes, no tools, looks like part of the tub"

**C1 — Peace of mind closer：**
- 静止画面 + 字幕："One less thing to worry about during bath time"
- 不出现 baby 正脸 / 患处特写

**C2 — Sensory relief closer：**
- 字幕："Skin feels less tight after every bath"
- ❌ **不可写** "no more eczema" / "cleared up"

**C3 — Price legitimacy closer：**
- 字幕："$59. About 30¢ per bath when you subscribe."
- ❌ **不可写** "best value" / "cheapest premium filter"

### 1.4 测试规则

| 字段 | 规范 |
|---|---|
| 平台 | TikTok + Meta（IG Reels + Feed）—— 同 cell 双平台跑 |
| 受众定义 | A. mom 25–40 + parenting interests；B. female skincare 22–40；C. wellness 30–55 — 三 audience × 9 cell = 27 ad sets |
| 预算 | $25–50/day per ad set，3 天数据点最低 |
| 总预算 estimate | 27 × $40 × 3 = **~$3,200**（baseline 实验） |
| KPI | hook rate (3-sec view %), CTR, add-to-cart rate, ROAS |
| Stop rule | 任何 cell 在 72 小时内 ROAS < 0.5 → 关停；ROAS > 1.5 → 加预算 |
| 决策点 | 第 7 天 → 选 winning combo，concentrate 80% 预算 |

### 1.5 必须避开的创意 element（合规 black-list）

参考 [[bathtub-filter-community-language-compression-patterns]] §4：

- ❌ "eczema" / "cleared up" / "treats" / "heals" / "prevents"
- ❌ "safe for babies" 单独（触发 CPSIA labeling）
- ❌ "doctor-recommended" 无具体来源
- ❌ "99.X%" 无 NSF cert
- ❌ "best" / "cheapest" / "most" 比较级
- ❌ baby 正脸特写（FDA implication + child image consent risk）
- ❌ before/after eczema 患处图
- ❌ "limited time" / "while supplies last"（FTC scarcity guides）

### 1.6 测试结果存档

测试结束 7 天后，把 winning combo 写入：
- `bathtub-filter-ab-creative-test-results-[YYYY-MM].md`（新建）
- 回写到 [[bathtub-filter-visual-merchandising-and-creative-strategy]] 作为 evidence
- 6 个月后 retest（受众疲劳 + 平台算法漂移）

## 2. 创作者合作 brief 模板

### 2.1 合作分级

| Tier | 定义 | 合作模式 | 期望 deliverable |
|---|---|---|---|
| **Lab reviewer** | Water Filter Guru, mindbodygreen, Interior Medicine | 送测，免费 sample，**不付费** | 独立测试 + 评测文章 / 视频 |
| **Mom nano** (5K–25K) | Eczema mom / parenting nano | 送 sample + $300–600 honorarium | 1 reel + 1 carousel + 3 stories，60 天后续 |
| **Mom micro** (25K–100K) | Established parenting micro | $1,000–3,000 + sample | 1 reel + 1 longform + 3 stories + UGC rights |
| **Skincare micro** (50K–250K) | Skincare-focused micro | $2,000–5,000 + sample | 1 reel + 1 carousel + 1 IG live mention |
| **Macro / mega** | (>250K) | **V1 不投**（CAC > LTV） | n/a |

### 2.2 创作者 brief 文档骨架

```
SUBJECT: KES Bath Filter — Creator Partnership Brief [Creator Name]

PRODUCT
KES Bath Filter — designed for sensitive skin routines.
Reduces free chlorine in bath water. Tool-free, 5-minute install.
$59 retail / $0.30 per bath with subscription.

SHIP DATE: [date]
CONTENT DUE: [date + 60 days for long-cycle, +14 days for short-cycle]

WHAT WE'RE LOOKING FOR
- 1 Reel (15–60 sec) showing: install + first use + 14-day or 60-day check-in
- 1 carousel (5–10 slides) showing: chlorine test demo OR install OR before-after sensory
- 3 stories: unboxing, daily use, follow-up

WHAT TO EMPHASIZE
- Visible chlorine reduction (use included DPD test strip)
- Tool-free install
- Designed for sensitive-skin / hard-water routines
- Honest experience — KES wants real reactions, not scripted

🚫 LANGUAGE TO AVOID (CRITICAL — KES legal compliance)
Please DO NOT use any of these phrases or imply them:
- "eczema" / "cleared up my eczema" / "cured" / "healed" / "treats"
- "FDA approved" / "doctor-recommended" / "dermatologist-tested"
  (unless KES sends you specific verified documentation to cite)
- "safe for babies" as a standalone claim
- "removes 99%" or any specific % unless KES provides cert documentation
- "best" / "cheapest" / "only one that works"

These restrictions exist because of FDA / FTC compliance requirements
for water filtration products. KES will reject content using these phrases
even if the rest is great.

✅ SAFE PHRASES
- "feels less tight" / "feels softer"
- "less worry about water during bath time"
- "designed for routines that need gentle water"
- "tested compatible with [specific spout type]"

DELIVERABLES + RIGHTS
- All content delivered as raw + edited files
- KES gets 6-month organic + paid usage rights on KES owned channels
- Creator retains posting rights on own channels in perpetuity
- Creator commits to NOT working with: Canopy, Santevia, Crystal Quest, Tubo,
  Sprite, FilterBaby, Kinder, Curety, Beati for 90 days post-content

PAYMENT
- $[X] honorarium, payable Net 15 after content goes live
- + product value $[Y] (housing + 4 cartridges)

CONTACT
[KES partnership manager email]
```

### 2.3 合同关键条款骨架（给 legal 起草用）

下面是 KES legal team 起草 creator agreement 时必须包含的条款骨架：

| 条款 | 关键 language |
|---|---|
| **FTC disclosure** | Creator must use #ad / #sponsored / "paid partnership" tag in compliance with FTC Endorsement Guides 16 CFR Part 255 |
| **Claim restrictions** | Creator agrees to use only language pre-approved by KES (per black-list above). Any non-approved claim = breach + content takedown + honorarium forfeit |
| **IP / usage rights** | KES gets 6-month organic + paid usage rights to all delivered content on KES-owned channels (web, email, Meta, TikTok, Amazon A+). Creator retains rights on own channels |
| **Exclusivity** | Creator commits to NOT working with named competitors for 90 days post-content live |
| **Indemnification** | Creator indemnifies KES against any FTC / FDA / state AG action arising from creator's deviation from approved claim language |
| **Termination** | Either party may terminate before content go-live with 7-day notice. Post go-live, content stays unless takedown is mutual |
| **Compensation** | Honorarium + product value, payment Net 15 post-go-live |
| **Performance reporting** | Creator provides analytics screenshots within 14 days of go-live |
| **Governing law** | [State of KES incorporation] |

> ⚠️ 这是 **brief 骨架**，不是 final contract。实际合同必须由 entertainment / influencer counsel 起草，covering local jurisdiction nuances（EU GDPR、CA AB-587 social media transparency、UK ASA standards）。

### 2.4 Creator outreach 优先级（基于 SNS taxonomy）

参考 [[bathtub-filter-sns-creator-and-visual-taxonomy]] §2 创作者 tier：

**Phase 1 — V1 launch + 0 月（送测，无付费）：**
- Water Filter Guru（直接对位，最高 leverage）
- mindbodygreen
- Interior Medicine
- Refinery29 beauty editor

**Phase 2 — V1 launch + 0–2 月（mom nano seeding）：**
- @jazzybsway 类似 nano mom（5K–25K）— 选 5–10 个
- Ciara Deanne 类似 longform blog—选 2–3 个

**Phase 3 — V1 launch + 2–4 月（micro 付费扩散）：**
- 选择 Phase 2 中表现最好的 nano → 升级到 micro 付费合作
- 同时寻找 skincare micro（与 mom 路线 split test）

**Phase 4 — V1 launch + 4–6 月（基于 A/B 数据放大）：**
- Winning narrative + winning creator type → concentrate budget
- 准备 UGC paid 素材库

## 3. 还卡在哪里（必须人工/外部完成）

- [ ] 实际 A/B 测试预算批准 + 投放执行（marketing / paid ops 团队）
- [ ] Influencer counsel 起草最终合同（外部 legal）
- [ ] FTC / FDA pre-launch 文案 review（外部 legal）
- [ ] Creator outreach pipeline 建立（marketing manager）
- [ ] DPD test strip / chlorine demo kit 包装 sourcing（KES product team）
- [ ] 测试结果分析 + 决策（A/B 第 7 天 + 第 30 天 review）

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-visual-merchandising-and-creative-strategy]]
- [[bathtub-filter-sns-creator-and-visual-taxonomy]]
- [[bathtub-filter-community-language-compression-patterns]]
- [[bathtub-filter-claim-risk-audit-v2]]
- [[bathtub-filter-marketplace-claim-policing-layer]]
- [[bathtub-filter-amazon-category-and-keyword-baseline]]
- [[bathtub-filter-channel-admission-requirements]]
- [[bathtub-filter-research-coverage-gaps]]
