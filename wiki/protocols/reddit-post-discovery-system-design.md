---
type: protocol
status: draft
created: 2026-06-07
updated: 2026-06-09
domain: marketing-infrastructure
domains: [reddit-monitoring, post-discovery, arctic-shift, last30days, community-marketing, intent-classification, keyword-strategy, quality-scoring, feedback-loop]
confidence: high
verification_status: designed
related:
  - wiki/syntheses/kes-community-marketing-implementation-2026.md
  - wiki/syntheses/community-marketing-cross-platform-2026.md
  - wiki/protocols/kes-community-question-sourcing.md
---

# KES Reddit 帖子发现系统设计

> 用 Arctic Shift（每日微观发现）+ last30days（每周宏观研究）构成双轨帖子发现系统。
> 本文档描述流程设计、数据流向、输出格式与人工审核衔接——不含代码。

---

## 系统总览

### 双轨定位

```
┌─────────────────────────────────────────────────────────┐
│                 帖子发现双轨系统                        │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Track A：last30days（宏观 · 每周一次）                    │
│  ┌─────────────────────────────────────────────┐       │
│  │ 目的：发现「哪些话题/子版块在讨论 KES 相关议题」│       │
│  │ 频率：每周一早上                               │       │
│  │ 输出：subreddit 优先级清单 + 痛点语言库更新     │       │
│  │ 数据源：Reddit + HN + X + YouTube           │       │
│  └─────────────────────────────────────────────┘       │
│                         ↓                               │
│                 输入到 KES 产品知识库                    │
│                                                         │
│  Track B：Arctic Shift（微观 · 每日多次）                │
│  ┌─────────────────────────────────────────────┐       │
│  │ 目的：「找到今天具体要回复的帖子」               │       │
│  │ 频率：每日 08:00 / 13:00 / 18:00（3 次）    │       │
│  │ 输出：待回复帖子清单（标题 + 作者 + 链接）       │       │
│  │ 数据源：Arctic Shift API（Reddit 全站搜索）    │       │
│  └─────────────────────────────────────────────┘       │
│                         ↓                               │
│                 输入到 AI 起草 → 人工审核 → 发送        │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### 为什么需要双轨

| 维度 | last30days（宏观） | Arctic Shift（微观） |
|------|---------------------|----------------------|
| 时间颗粒度 | 过去 30 天趋势 | 过去 24 小时新帖 |
| 输出类型 | 话题地图、语言模式 | 具体帖子 URL 清单 |
| 使用频率 | 每周一次 | 每日 2-3 次 |
| 决策价值 | 「应该关注哪些社区」 | 「今天回哪条帖」 |
| 数据延迟 | 依赖平台 API（通常 < 1h） | < 2h（Arctic Shift 数据延迟） |
| 费用 | 免费（消耗 API quota 但无现金成本）| 完全免费 |

**单一工具无法覆盖：** last30days 不返回「今天刚发的帖」；Arctic Shift 不告诉你「这个话题的整体趋势」。

---

## Track A：last30days 宏观研究流程

### 触发时机

- **每周一 08:00**（定期）
- **产品上线前 2 周**（一次性）
- **竞品有重大动作时**（触发式）

### 执行步骤（人工驱动）

```
Step 1：确定本周研究主题
  ├── 卫浴五金线：/last30days bathroom faucet metal vs plastic valve
  ├── 窗帘系统（Egypt）：/last30days roller blind curtain egypt heat resistant
  └── 竞品监控：/last30days grohe faucet review 2026

Step 2：运行 last30days skill
  └── 输出：综合报告（Reddit + HN + X + YouTube 聚合）

Step 3：从报告中提取三类信息
  ├── 高频 subreddit 清单（哪些版块在讨论这个话题）
  ├── 用户原话（痛点语言，直接存入知识库 pain-points.md）
  └── 竞品提及频率（哪些竞品被正面/负面提及）

Step 4：更新 KES 产品知识库
  ├── community-questions/reddit-xxx-qs.md（新增问题）
  ├── pain-points.md（新增用户原话）
  └── competitor-comparisons.md（更新竞品主张）

Step 5：更新 Arctic Shift 监控配置
  └── 将新发现的 subreddit 加入监控清单
```

### 输出格式（存入 wiki）

```markdown
<!-- 文件：wiki/syntheses/last30days-reports/2026-W23-bathroom-faucet.md -->

# last30days 报告：bathroom faucet（2026-W23）

## 高频 Subreddit（按提及次数排序）
| Subreddit | 提及次数 | 讨论焦点 |
|-----------|----------|----------|
| r/HomeImprovement | 47 | 安装DIY、品牌推荐 |
| r/Plumbing | 23 | 阀芯漏水、维修 |
| r/BathroomRemodel | 18 | 翻新选购 |

## 用户痛点原话（直接引用）
- "my $30 faucet handle fell off after 6 months" （r/HomeImprovement）
- "plastic valve cracked in cold weather" （r/Plumbing）
- ...

## 竞品提及
| 品牌 | 正面 | 负面 | 中性 |
|------|------|------|------|
| GROHE | 12 | 3 | 8 |
| Moen | 8 | 7 | 15 |
...
```

---

## Track B：Arctic Shift 微观发现流程

### 设计目标

> 每天 3 次自动扫描，输出一份「待回复帖子清单」，直接可供人工审核决定是否回复。

### 输入：监控任务清单（三层关键词架构）

每个监控任务 = 一个 subreddit + 一组关键词。关键词分三层设计（逻辑分层，实际查询时 OR 合并为一次 Arctic Shift 调用）：

```
Layer 1 品类词：搜「什么东西」
  → 高召回，低保真 → faucet / shower / valve / curtain / blind
  → 用于：确保不因品类词缺失而漏帖

Layer 2 意图信号：搜「用户在干嘛」
  → 中召回，高保真 → recommend / best / leaking / install / expensive / vs
  → 用于：捕捉不用品类词但意图明确的帖

Layer 3 竞品 + 技术词：搜「谁/什么技术被提到了」
  → 低召回，极高保真 → Moen / Delta / Kohler / GROHE / PVD / ceramic
  → 用于：竞品投诉、技术对比（最高转化场景）
```

```yaml
#
# 监控任务清单（概念格式，实际存储于 wiki/protocol 目录下）
# 文件：wiki/protocols/reddit-monitor-tasks.yaml（概念设计）
# 更新于 2026-06-09：三层关键词 + Amazon 竞品补充 + r/DIY/r/Home 实验频道

tasks:
  # ========================================================================
  # 卫浴五金 — 高优先级
  # ========================================================================
  - subreddit: HomeImprovement
    keywords: [
      # Layer 1 品类
      faucet, shower, valve, bathroom hardware, towel bar, sink,
      # Layer 2 意图
      recommend, best, leaking, broken, install, replace, expensive, worth it, vs,
      # Layer 3 竞品 Tier 1
      Moen, Delta, Kohler, American Standard, Pfister, GROHE, Hansgrohe,
      # Layer 3 竞品 Tier 2
      Glacier Bay, KRAUS, Kingston Brass
    ]
    priority: high
    product_line: bathroom-hardware

  - subreddit: Plumbing
    keywords: [
      faucet, valve, cartridge, shower, drain, sink,
      leaking, broken, stuck, install, replace, fix,
      Moen, Delta, Kohler, Pfister, American Standard, GROHE,
      PVD, ceramic, pressure balance, thermostatic
    ]
    priority: high
    product_line: bathroom-hardware

  - subreddit: BathroomRemodel
    keywords: [
      faucet, shower, hardware, remodel, towel bar,
      recommend, best, worth it, cost, vs,
      Kohler, Moen, Delta, GROHE, Hansgrohe
    ]
    priority: medium
    product_line: bathroom-hardware

  # ========================================================================
  # 卫浴五金 — 实验频道（低优先 + 噪声压制）
  # ========================================================================
  - subreddit: DIY
    keywords: [
      # 仅用组合（品类+意图），不用纯品类词
      faucet install, faucet replace, shower install, shower replace,
      valve replace, leaking faucet, broken shower
    ]
    priority: low
    product_line: bathroom-hardware
    noise_filter:
      exclude_title_containing: [week, update, progress, tour]

  - subreddit: Home
    keywords: [
      recommend bathroom faucet, best shower, bathroom remodel cost,
      new bathroom fixtures, upgrade bathroom
    ]
    priority: low
    product_line: bathroom-hardware
    noise_filter:
      exclude_title_containing: [sqft, bedroom, bath, just bought, closed]

  # ========================================================================
  # 厨房龙头线（KES pot filler + RO 龙头）
  # ========================================================================
  - subreddit: HomeImprovement
    keywords: [
      kitchen faucet, pot filler, pull down faucet, RO faucet,
      KRAUS, Moen kitchen, Delta kitchen, Kohler kitchen
    ]
    priority: medium
    product_line: kitchen-faucets

  # ========================================================================
  # 浴缸过滤芯线（KES bathtub filter — 挂浴缸龙头出水嘴除氯）
  # 讨论场景：湿疹/宝宝皮肤/敏感肌 → r/eczema, r/SkincareAddiction, r/beyondthebump
  # ========================================================================
  - subreddit: eczema
    keywords: [
      bathtub filter, bath filter, bath water filter, chlorine bath,
      eczema bath, baby bath filter, toddler eczema,
      recommend, worth it, which, help
    ]
    priority: high
    product_line: bathtub-filter

  - subreddit: SkincareAddiction
    keywords: [
      bathtub filter, bath filter, chlorine removal, shower filter,
      hard water, skin irritation, eczema,
      recommend, which, review
    ]
    priority: medium
    product_line: bathtub-filter

  - subreddit: beyondthebump
    keywords: [
      bathtub filter, baby bath filter, bath water, chlorine,
      eczema baby, sensitive skin baby,
      recommend, safe, which
    ]
    priority: high
    product_line: bathtub-filter

  - subreddit: NewParents
    keywords: [
      bathtub filter, baby bath, bath water filter,
      eczema, sensitive skin, chlorine,
      recommend, safe
    ]
    priority: medium
    product_line: bathtub-filter

  - subreddit: BathroomRemodel
    keywords: [
      bathtub filter, bath water filter, chlorine removal,
      recommend, which
    ]
    priority: low
    product_line: bathtub-filter

  # ========================================================================
  # 窗帘系统（Egypt）
  # ========================================================================
  - subreddit: egypt
    keywords: [curtain, blind, roller, window covering,
               install, recommend, best, expensive, heat, sun]
    priority: high
    product_line: curtain-roller-blind-egypt

  - subreddit: interiordecorating
    keywords: [curtain, blind, roller shade, window treatment]
    priority: medium
    product_line: curtain-roller-blind-egypt
```

### 竞品词选择依据（Amazon 调查）

> KES 在 Amazon 卫浴龙头 / 淋浴系统 / 毛巾架 Top 30 中均不在列。
> Amazon Best Seller ≠ Reddit 讨论品牌。竞品词选择以 **Reddit 被讨论的频次** 为第一优先级，Amazon 销量榜上的品牌（FORIOUS、Hurran、Cobbe）在 Reddit 上几乎零讨论——搜索它们找不到可回复帖子。

**Tier 1 — Reddit 高频讨论 + KES 有明确差异化机会（7 个必搜）：**

| 品牌 | Reddit 讨论特征 | KES 差异化切入 |
|------|----------------|---------------|
| **Moen** | 最常被讨论，安装求助多，投诉中等 | KES 同价位但全金属阀芯优势 |
| **Delta** | 淋浴系统极强（Amazon Top 30 占 10），DIY 讨论多 | KES 淋浴系统直接对标 |
| **Kohler** | 高端对比标杆，"值不值这个价"讨论多 | KES 性价比叙事入口 |
| **American Standard** | 中端可靠性讨论，常与 Moen/Delta 并列 | 中端替代选项 |
| **Pfister** | 低价位，投诉多（"leaked after 6 months"） | KES 质量差异故事 |
| **GROHE** | 高端欧洲品牌，"值不值 3 倍价格" | KES 技术对标叙事 |
| **Hansgrohe** | 高端欧洲，设计讨论 | 同上 |

**Tier 2 — 偶尔出现在 Reddit 性价比讨论中（3 个选搜，仅 HomeImprovement + Plumbing）：**

| 品牌 | 定位 |
|------|------|
| **Glacier Bay** | Home Depot 自营，DIY 入门选择，投诉极多 |
| **KRAUS** | Amazon 中端，厨房龙头强，Reddit 讨论增长中 |
| **Kingston Brass** | 中档装饰性品牌，"好看但质量呢？" |

**不监控的竞品：**
- FORIOUS / Hurran / Cobbe / OWOFAN / KLJKPA — Amazon 爆款但在 Reddit 零讨论
- 毛巾架/卫浴配件品牌 — Reddit 不按品牌讨论毛巾架，靠品类词自然覆盖

**厨房龙头线竞品：** KRAUS + 复用 Moen/Delta/Kohler（厨房与卫浴共用搜索词）

**窗帘线：** 不加竞品关键词（用户确认）

**浴缸过滤芯线竞品（Reddit 讨论）：**

> bathtub filter 是一个非常细分的市场，Reddit 讨论集中在 r/eczema、r/SkincareAddiction、r/beyondthebump。
> 用户核心诉求：**氯/硬水加重湿疹/宝宝皮肤敏感**，不是"哪个品牌好"，而是"有没有用/安不安全"。
> 竞品以专业滤水品牌为主，不是卫浴五金品牌。

**Tier 1 — Reddit 有讨论 + KES 有差异化机会：**

| 品牌 | 产品形态 | Reddit 讨论特征 | KES 差异化切入 |
|------|----------|----------------|---------------|
| **CuZn** | Bath Ball（挂出水嘴） | 最知名的 bath ball，KDF-55 滤材，Amazon 评论多 | KES 同形态，更好设计/更低价格 |
| **Crystal Quest** | Bath Ball（挂出水嘴） | Made in USA 卖点，Reddit 偶尔提及 | KES 同形态，更好设计 |
| **Canopy** | Bath Tub Filter（挂出水嘴） | 新兴品牌，$49，设计感强，Instagram 营销强 | KES 性价比优势 |
| **Sonaki** | 淋浴/浴缸过滤器 | 维生素 C 滤材，Reddit 偶尔提及 | KES 滤材技术对标 |
| **AquaBliss** | 淋浴过滤器（也可用于浴缸） | 中端主流，Amazon 销量高 | KES 专做浴缸场景 |

**Tier 2 — 偶尔讨论 / 相关但不直接竞争：**
| 品牌 | 定位 |
|------|------|
| **Berkey** | 淋浴过滤器，KDF 滤材，寿命长（1 年） |
| **Pelican** | 淋浴过滤器，NSF 认证 |
| **Waterdrop** | 主要做 RO 系统，有淋浴过滤器 |

**Bathtub filter 在 Reddit 的讨论特征：**
- 不是"哪个品牌好"，而是"有没有用"（效果验证）
- 核心场景：湿疹宝宝、成人湿疹、敏感肌
- 决策关键因素：滤材类型（KDF-55 vs 维生素 C）、寿命、安装是否方便、是否含 BPA
- KES 的差异化切入点：**专业 bathtub 场景**（不是淋浴过滤器的副产品）+ **更好设计** + **合理价格**

### 噪声压制策略

r/DIY 和 r/Home 的噪声来源与分析：

```
r/DIY 噪声模式：
  ✅ 相关 → "help installing new bathroom faucet"
  ❌ 噪声 → "week 3: painted walls, bought faucet, installed..."（流水账）
  ❌ 噪声 → "outdoor faucet frozen over winter"（非卫浴场景）

r/Home 噪声模式：
  ✅ 相关 → "what shower system for master bath?"
  ❌ 噪声 → "house has 2.5 baths with stand-up shower"（户型描述）
```

**压制规则：**

| 频道 | 规则 | 原理 |
|------|------|------|
| r/DIY | 仅用品类+意图组合词（如 `faucet install`），不用纯品类词 | 纯 `faucet` 会匹配流水账 |
| r/DIY | 标题含 `week / update / progress / tour` 自动排除 | 这些是翻新日志，不是求助 |
| r/Home | 仅用 Layer 2 + 品类（如 `recommend bathroom faucet`） | 户型帖不含意图信号 |
| r/Home | 标题含 `sqft / bedroom / bath / just bought / closed` 自动排除 | 这些是房产交易帖 |
| r/Home | priority = low | 审核时优先看 HomeImprovement/Plumbing |

---

### 处理流程（概念设计）

```
每次运行（每日 3 次）
│
├── Phase 1：拉取新帖
│   └── 对每个监控任务调用 Arctic Shift API
│       POST /api/posts/search
│         subreddit = {subreddit}
│         query      = {keywords 用 OR 连接}
│         after      = "1d"          ← 过去 24 小时
│         sort       = "desc"         ← 最新的在前
│         limit      = 20
│
├── Phase 2：去重过滤
│   ├── 已推送过的帖子（存在 seen-posts.json）→ 跳过
│   ├── 已回复过的帖子（存在 replied-posts.json）→ 跳过
│   └── 帖子得分 < -5（已被踩）→ 跳过
│
├── Phase 3：意图分类（核心，10 类意图分类法）
│   └── 对每条新帖按意图分类 → 匹配回复策略（详见下文「意图分类法」节）
│
├── Phase 4：帖子质量评分
│   └── 对已分类帖子按 5 维度评分 → 同类意图内排序（详见下文「质量评分」节）
│
├── Phase 5：生成待回复清单
│   └── 输出 Markdown 表格（见下方格式），附带 AI 分类 + 人工修正列
│
└── Phase 6：推送通知
    ├── 方案 A：写入 wiki/protocols/pending-replies.md（打开 wiki 即见）
    ├── 方案 B：发送邮件/微信通知（需要配置）
    └── 方案 C：打印到 stdout（cron 运行 + 邮件转发）
```
```

---

## Phase 3：意图分类法（10 类 × 3 层优先级）

> Phase 3 核心：用 10 种意图取代原来的 4 类粗糙分类，每类匹配独立回复策略。
> 分类原则：**按最急迫的意图回复**，覆盖 OP 最痛的问题，顺便覆盖隐含意图。

### 总览

| # | 意图 | 优先级 | 时间窗口 | KES 提及规则 | 回复目标 |
|---|------|:---:|:---:|------|------|
| 1 | 显性求推荐 | P0 | 6h | 可以 | 转化 |
| 2 | 问题诊断 | P0 | 6h | 仅替换时 | 信任 |
| 3 | 竞品投诉 | P1 | 24h | 不主动 | 情报 |
| 4 | 产品对比 | P1 | 24h | 可以 | 定位 |
| 5 | 安装求助 | P1 | 24h | 可选 | 权威 |
| 6 | 装修计划 | P1 | 24h | 作为选项 | 信任 |
| 7 | 成本/价值讨论 | P1 | 24h | 可以 | 透明度 |
| 8 | 技术深问 | P2 | 48h | 背景可提 | 权威 |
| 9 | 炫耀帖 | P3 | 48h | 绝不 | 社区存在感 |
| 10 | 翻车现场 | P3 | 48h | 绝不 | 幽默+教育 |

### P0 层：6h 黄金窗口

#### 1. 显性求推荐 — explicit purchase intent
```
帖子样本：  "What's the best bathroom faucet under $100?"
          "Anyone recommend a shower system that won't leak?"
          "Help me choose: Kohler vs something cheaper but good"

回复策略：  直接推荐 + 给出理由 + 标注 KES 身份
KES 提及：  可以，产品和问题直接匹配
语气：      温和推荐，不带推销腔
典型坑：    "ONLY KES can solve this!" → 最低级的社区营销
关键信号：  recommend, best, should I buy, worth it, which one
```

#### 2. 问题诊断 — problem diagnosis
```
帖子样本：  "Why is water dripping from my shower head?"
          "Faucet handle won't turn, what's wrong?"
          "Low water pressure after installing new valve"

回复策略：  先诊断（不要推荐产品）。走排除法：密封圈？阀芯？水压？
          只在你确定问题 = 需要更换部件时才提 KES
KES 提及：  仅当「换」是解决方案时。诊断阶段不提
语气：      像水管工朋友帮你排查问题
典型坑：    用户问「怎么修」，你回「买 KES 的」→ 罔顾语境
关键信号：  leaking, won't turn, low pressure, dripping, stuck, broken
```

### P1 层：12-24h 窗口

#### 3. 竞品投诉 — competitor complaint
```
帖子样本：  "My Moen faucet leaked after 8 months, customer service useless"
          "Never buying Delta again, third replacement in 2 years"
          "GROHE shower system not worth the $800"

回复策略：  先共情（"that sucks, especially with what they charge"）
          分享行业知识解释为什么可能出现这种情况（不攻击竞品）
          绝对不主动推销。等 OP 或其他人问「有什么替代」才自然提到 KES
KES 提及：  仅当有人明确问「那该买什么」时，才接话
语气：      同行，不是竞品销售
典型坑：    "that's because Moen uses cheap plastic" → 攻击竞品，显得 low
关键信号：  never buying X, broke after, customer service horrible
```

#### 4. 产品对比 — product comparison
```
帖子样本：  "Moen vs Delta vs Kohler — who makes the best shower valve?"
          "Is GROHE really worth 3x the price of a normal brand?"

回复策略：  技术视角对比，正面评价每个品牌的优势
          然后在性价比维度自然引入 KES
          「每个品牌有自己的定位。Moen 强在…GROHE 强在…如果你的预算
          在 x-y 之间，有一个叫 KES 的品牌做全金属阀芯…」
KES 提及：  可以，通过「预算选项」定位
语气：      行业分析师，不是品牌粉丝
典型坑：    "KES is better than all of them" → 不客观，信用归零
关键信号：  vs, versus, or, worth the extra, difference between
```

#### 5. 安装求助 — installation help
```
帖子样本：  "How do I mount a shower valve in a 2x4 wall?"
          "New faucet won't fit my existing plumbing, adapter needed?"

回复策略：  纯安装建议，不提产品
          可以自然带出「我们做这个天天碰到这种安装场景」建立可信度
KES 提及：  不提产品链接，只用「我们做这方面的」建立权威背景
语气：      老安装师傅
典型坑：    在安装教程中间插入产品链接 → 信任粉碎
关键信号：  how to install, won't fit, adapter, tools needed, DIY
```

#### 6. 装修计划 — DIY project planning
```
帖子样本：  "I'm remodeling my bathroom, what hardware do I need?"
          "First time homeowner — shower system buying checklist?"

回复策略：  帮 OP 梳理选购标准（预算、材质要求、安装难度）
          在标准中提到 KES 作为一个选项（和其他品牌并列）
KES 提及：  作为选项之一推荐
语气：      热心邻居帮你列清单
典型坑：    把清单变成 KES 产品目录
关键信号：  remodel, renovation, checklist, what do I need, planning
```

#### 7. 成本/价值讨论 — cost/value discussion
```
帖子样本：  "Why the hell do bathroom faucets cost $500?"
          "Plumber quoted me $2000 for shower install, is this normal?"

回复策略：  行业透明度——解释成本构成（铜料、加工、品牌溢价、分销层级）
          诚实解释为什么有的贵有的便宜
          自然解释 KES 怎么做到降低价格的同时保持质量
KES 提及：  可以，且「解释成本」叙事天然适合 KES 价值定位
语气：      剥洋葱，行业揭秘
典型坑：    只说「因为我们便宜」没解释「为什么便宜」→ 显得廉价
关键信号：  why so expensive, is this fair price, quoted, cost, rip off
```

### P2-P3 层：权威建设 + 社会资本

#### 8. 技术深问 — technical deep question
```
帖子样本：  "Ceramic disc vs compression cartridge — which lasts longer?"
          "What's the difference between PVD and electroplated finish?"
          "Why do some shower valves have pressure balancing?"

回复策略：  深度技术回答，引用工程原理 + 实际测试
          可以带「我们做过 xxx 测试」但不放链接
          这些帖子搜索引擎 rank 极高 → 长期被动流量
KES 提及：  「我们设计时选择了 xxx」作为背景提及，不是推销
语气：      科普作者 / 工程师
典型坑：    简化为产品广告 → 浪费一次做永久权威内容的机会
关键信号：  how does X work, what's the difference between, why do
```

#### 9. 炫耀帖 — show-off / brag post
```
帖子样本：  "Finally finished my $15k bathroom renovation!" [照片]
          "Check out my new brushed gold shower set"

回复策略：  真诚赞美 + 一个技术小观察（建立社交存在）
          「漂亮！那个 brushed gold finish 跟你的 tile 色系配得很好」
KES 提及：  绝不
语气：      同好，不是销售
典型坑：    "nice bathroom, by the way we sell..." → 让人恶心
关键信号：  just finished, check out my, look at my new, finally done
```

#### 10. 翻车现场 — WTF / bad install
```
帖子样本：  "Look at this 'landlord special' plumbing job" [照片]
          "Is this even code compliant?" [浴室管路照片]

回复策略：  幽默 + 教育（解释为什么这种装法有问题/不合规）
          不推销。纯建立社区存在感
KES 提及：  绝不
语气：      水管工段子手
典型坑：    严肃说教（"this violates IPC section xxx"）→ 不好玩
关键信号：  landlord special, is this code, look at this, WTF
```

### 混合意图处理

真实帖子经常混合多种意图。按 **「最急迫意图」** 原则分类：

```
案例："My faucet is leaking after 2 years — should I fix or replace?"

意图分析：
  显性：问题诊断（50%）→ 「为什么漏」
  隐性：显性求推荐（30%）→ 「如果换，换什么」
  辅助：成本讨论（20%）→ 「修 vs 换哪个划算」

分类结果：主意图 = 问题诊断（P0）
回复策略：先诊断 → 结论为「换」→ 自然触发显性求推荐的回复策略
```

**决策规则：**
1. 有含 "recommend / best / buy / worth it" + 具体产品类别 → 显性求推荐优先
2. 有含 "leaking / broken / won't work / stuck" +  诊断语气 → 问题诊断优先
3. 竞品名称 + 负面情绪 → 竞品投诉优先
4. 多个品牌用 "vs / or" 并列 → 产品对比优先

### 误判修正反馈循环

```
每次人工审核时，在 pending-replies.md 的「人工修正」列记录：

  ✓ 正确    → 不记
  ✗ 实际是 {真实意图}  → 月末统计

月末回顾流程：
  1. 统计误判率 = 误判数 / 总分类数
  2. 识别高频混淆对（如「竞品投诉」常被分类为「显性求推荐」）
  3. 修订分类关键词
     例：若两类频繁混淆 → 
       "never buying {brand}" 强制 = 竞品投诉（不是求推荐）
       "{brand} broke after"  强制 = 竞品投诉（不是求推荐）
  4. 人工抽查遗漏：
     每月手动浏览 2-3 个关键 subreddit 的过去 24h 新帖，
     对比 AI 清单 → 找出被「不相关」过滤的遗漏帖 → 分析遗漏原因
```

---

## Phase 4：帖子质量评分框架

> 对通过意图分类的帖子，计算 5 维度复合得分，在同类意图内排序。
> 不评分的后果：花时间回 OP 已跑的帖 / 竞品已高质量回复的帖 / 低价值 subreddit 的平庸帖挤掉高价值帖。

### 五维度详解

#### D1：OP 活跃度（权重 ×1.0）

| 分数 | 判定标准 | 获取方式 |
|---:|------|---------|
| 4 | OP 在过去 2h 内回复了 3+ 条评论 | `GET /api/comments/search?author=<OP>&after=1d` |
| 3 | OP 在过去 6h 内回复了 1-2 条 | 同上 |
| 2 | OP 无回复，但帖子 <6h | 帖子 `created_utc` 计算 |
| 1 | OP 无回复，帖子 6-24h | 同上 |
| 0 | OP 的 Reddit 最后活跃 >48h | `/api/users/search` 或搜 OP 近期评论 |

⚠️ OP 活跃度 ≤1 时，即使帖子很好，优先级降到 P3。

#### D2：新鲜度（权重 ×1.0）

| 分数 | 时间 | 说明 |
|---:|------|------|
| 4 | <2h | 黄金窗口，帖子正在排序上升 |
| 3 | 2-6h | 仍在流量期 |
| 2 | 6-12h | 开始下沉 |
| 1 | 12-24h | 只有搜索来的流量 |
| 0 | >24h | 几乎不会再有新读者 |

与意图交叉规则：P0 帖 + 新鲜度 0-2 → 降级到 P2。

#### D3：现有评论质量（权重 ×1.0）

| 分数 | 场景 | 我们的边际价值 |
|---:|------|---------------|
| 4 | 无评论 | 占第一个回复位，最大曝光 |
| 3 | 1-3 条评论但全是废话 | 实质内容立竿见影 |
| 2 | 有几条有用评论但都不完整 | 可补充差异化额外价值 |
| 1 | 已有 1-2 条高质量回答 | 增量价值有限 |
| 0 | 评论区已变战场 / 全是 meme | 进去会被溅一身泥 |

**「竞品投诉」意图的特殊规则：** 评论多但全是情绪发泄（无实质信息）→ 仍打 3-4 分（我们给的是行业解释，不是更多吐槽）。

#### D4：竞品在场度（权重 ×1.0）

| 分数 | 场景 | 策略 |
|---:|------|------|
| 4 | 无任何品牌回复，无竞品提及 | 完全空白，最好 |
| 3 | 有人提了竞品，但无人代表品牌回复 | 可以顺接讨论 |
| 2 | 竞品销售 / 代表回了但回答很烂 | 用「实质性对比」碾压 |
| 1 | 竞品给了高质量回答 | 很难超越，除非有明显遗漏点 |
| 0 | 多个竞品代表在场 / 已有品牌吵架 | 不要进火场 |

⚠️ **竞品识别降级方案**（实测 `author_flair_text` 几乎全为 `null`）：
- 扫描评论 `body` 中的品牌名（Moen, Delta, Kohler, GROHE 等）
- 扫描「I work for」「we sell」「our product」等信号词
- 检查评论者是否密集回复同一帖子（品牌销售行为模式）
- 调用 `/api/comments/tree?link_id=<post_id>` 获取完整评论树

#### D5：子版块价值（权重 ×1.5）※ 唯一加权维度

| 分数 | 标准 | KES 对应 subreddit |
|---:|------|------|
| 4 | 50 万+ 会员，购买意图强 | r/HomeImprovement, r/Plumbing |
| 3 | 5-50 万会员，与 KES 品类相关 | r/BathroomRemodel, r/DIY, r/egypt |
| 2 | 5000-5 万会员，精准 niche | r/Home, r/interiordecorating |
| 1 | <5000 会员 | 小 niche 论坛 |
| 0 | 社区文化与 KES 参与完全冲突 | r/Frugal（极端省钱） |

### 复合评分计算

```
复合分 = (D1×1.0) + (D2×1.0) + (D3×1.0) + (D4×1.0) + (D5×1.5)
       = 最高 22 分
```

**阈值与决策：**

| 复合分 | 决策 | 说明 |
|---:|------|------|
| 0-5 | 跳过 | 低质量帖，不值得回复 |
| 6-11 | 低优先级 | 有时间再说，否则跳过 |
| 12-22 | 必须回复 | 高质量帖，优先安排 |

**与意图优先级的交叉规则：**
- 意图优先级 > 质量分 > KES 资源预算
- P0 帖 + 质量分 0-5 → 降级到 P2（不值得浪费黄金窗口）
- P2-P3 帖 + 质量分 18+ → 可升级到 P1（evergreen 高价值）

### Arctic Shift 字段映射

| 维度 | 需要的 API 调用 | 返回字段 |
|------|---------------|----------|
| D1 (OP 活跃度) | `/api/comments/search?author=<OP>&after=1d` | `created_utc` |
| D2 (新鲜度) | 已有 | `created_utc` |
| D3 (评论质量) | `/api/comments/tree?link_id=<post_id>` | `body`, `score` |
| D4 (竞品在场) | 同上（评论树） | `body`（扫描品牌名） |
| D5 (子版块价值) | 已有（subreddit 名称） | 需维护 subreddit 价值对照表 |

---

## Phase 5：生成待回复清单

> 对通过意图分类 + 质量评分的帖子，按优先级 + 质量分排序，输出 Markdown 清单。

### 输出格式：待回复帖子清单

```markdown
<!-- 文件：wiki/protocols/pending-replies.md（每次运行覆盖更新） -->

# 待回复帖子清单（更新于 2026-06-09 13:00）

## 🔴 P0 · 6h 黄金窗口

| # | Subreddit | 标题 | OP | ↑ | 💬 | AI 分类 | 人工修正 | 链接 |
|---|-----------|------|----|---|---|---------|---------|------|
| 1 | r/HomeImprovement | "best bathroom faucet under $100?" | u/xxx | 15 | 8 | 显性求推荐 | — | [链接] |
| 2 | r/Plumbing | "shower valve leaking after 2 years" | u/yyy | 22 | 14 | 问题诊断 | — | [链接] |

## 🟠 P1 · 12-24h 窗口

| # | Subreddit | 标题 | OP | ↑ | 💬 | AI 分类 | 人工修正 | 链接 |
|---|-----------|------|----|---|---|---------|---------|------|
| 3 | r/HomeImprovement | "Moen vs Delta shower valve" | u/zzz | 8 | 6 | 产品对比 | — | [链接] |
| 4 | r/Plumbing | "how to mount shower valve in 2x4 wall" | u/aaa | 5 | 3 | 安装求助 | — | [链接] |
| 5 | r/HomeImprovement | "my Moen broke, never buying again" | u/bbb | 42 | 28 | 竞品投诉 | — | [链接] |

## 🔵 P2-P3 · 权威建设 / 社会资本

| # | Subreddit | 标题 | OP | ↑ | 💬 | AI 分类 | 人工修正 | 链接 |
|---|-----------|------|----|---|---|---------|---------|------|
| 6 | r/Plumbing | "ceramic vs compression cartridge?" | u/ccc | 3 | 5 | 技术深问 | — | [链接] |

## 📝 建议回复角度（AI 辅助草稿）

### 帖子 #1｜显性求推荐
- **用户原话：** 想要 durable bathroom faucet under $100
- **KES 知识库匹配：** pain-points.md → "plastic valve cracked" / competitor-comparisons.md → Moen/Delta 对比
- **建议回复结构：**
  1. 承认：选 faucet 确实容易踩坑
  2. 实质建议：金属阀芯 vs 塑料阀芯的差异（附测试数据链接）
  3. 自然提及：KES 用全金属阀芯，测试 xxx 小时
  4. 标注局限：如果预算极低，塑料阀芯也有选项

### 帖子 #2｜问题诊断
- **诊断路径：** 1) 检查密封圈 → 2) 检查阀芯 → 3) 检查水压
- **KES 知识库匹配：** 仅在诊断结果为「需更换」时 match pain-points.md
- **回复原则：** 先诊断，不提产品。等 OP 追问「那换什么」再推荐

### 帖子 #5｜竞品投诉
- **策略：** 先共情 → 行业解释 → 不主动推销
- **KES 提及：** 仅当有人问「那该买什么」时接话

---
*此清单由 Arctic Shift 自动生成，AI 分类列仅供参考。请人工审核修改后决定是否回复。*
*月末统计误判率：误判数 / 总分类数，识别分类模糊模式，修订分类关键词。*
```

---


## Phase 6：推送通知

> 生成待回复清单后，通过以下方案通知人工审核。

### 方案 A：写入 wiki/protocols/pending-replies.md（推荐）

- 每次运行覆盖更新 `pending-replies.md`
- 打开 wiki 即见，无需额外配置
- 适合：每日查看 wiki 的运营人员

### 方案 B：发送邮件/微信通知（需要配置）

- 配置邮件服务或企业微信 Webhook
- 每次更新 `pending-replies.md` 后触发通知
- 适合：需要实时提醒的运营人员

### 方案 C：打印到 stdout（cron 运行 + 邮件转发）

- cron 运行脚本，输出到 stdout
- 通过系统邮件转发功能发送结果
- 适合：服务器环境，无需 wiki 写入权限

---

## 回复效果反馈闭环（Gap 3）

> 没有反馈循环，系统永远无法改进意图匹配规则和评分权重。

### 为什么需要反馈闭环？

```
开环系统（当前设计）：
  发现 → 分类 → 评分 → 审核 → 回复 → 【结束】
  → 不知道回复效果 → 无法改进规则

闭环系统（本设计）：
  发现 → 分类 → 评分 → 审核 → 回复
  → 追踪效果 → 分析模式 → 更新规则 + 调整权重
  → 下一轮发现（用更新后的规则）
```

### 追踪指标

回复后 24-48h 追踪以下指标，存入 `replied-posts.json`：

| 指标 | 获取方式 | 意义 |
|------|---------|------|
| 回复 upvote 数 | Reddit API 或次日 Arctic Shift | 社区认可度 |
| 回复评论数 | 同上 | 引发讨论的能力 |
| OP 是否致谢 | 扫描评论中 OP 回复是否含 thanks / helped | 是否真正帮到人 |
| OP 是否追问 | OP 回复中是否提了后续问题 | 信任建立成功 |
| 转化事件 | 人工记录（OP 私信 / 提到购买了 KES） | 最终业务价值 |

### 存储格式（扩展 replied-posts.json）

```json
{
  "post_id": "1u0e128",
  "intent_type": "显性求推荐",
  "quality_score": 18,
  "replied_at": "2026-06-09T14:00:00Z",
  "outcome": {
    "reply_upvotes": 12,
    "reply_comments": 3,
    "op_acknowledged": true,
    "op_follow_up": false,
    "conversion": false
  },
  "review": {
    "intent_correct": true,
    "notes": ""
  }
}
```

### 分析周期

**每周快速回顾（15 分钟）：**
- 本周回复中，哪些意图类型得分最高？（调整该意图的回复策略）
- 有没有误判？（在 `review.intent_correct` 标记）

**每月深度分析（1 小时）：**

1. **意图分类效果**：哪类意图的回复 upvote 均值最高？
   - 「竞品投诉」upvote 均值 <2 → 回复策略太 defensive，需改进
   - 「技术深问」upvote 均值 >8 → 增加这类意图的监控权重
2. **质量评分准确性**：质量分 ≥18 的帖，实际回复效果是否显著更好？
   - 若否 → D1-D5 的权重需要调整
3. **遗漏分析**：手动浏览目标 subreddit，找出「该回但没进清单」的帖
   - 分析为什么漏了（关键词缺失？意图分类错误？）

### 闭环更新规则

| 发现 | 更新动作 |
|------|---------|
| 「竞品投诉」误判率高（常被分为「显性求推荐」） | 增加硬规则：`"never buying {brand}"` → 强制 = 竞品投诉 |
| D5 权重过低（r/DIY 的帖效果比预期好） | 调整权重：D5 从 ×1.5 调为 ×2.0 |
| 遗漏帖因关键词缺失 | 更新监控任务 YAML，增加关键词 |
| 「安装求助」回复效果差（upvote 均值 <1） | 修改该意图的回复策略（更偏技术，减少 KES 提及） |

### 人工审核衔接

在 `pending-replies.md` 增加「回复后评分」列：

| # | AI 分类 | 人工修正 | 回复后 upvote | OP 致谢 | 效果 |
|---|---------|---------|-------------|--------|------|
| 1 | 显性求推荐 | ✓ 正确 | 12 | Y | good |
| 2 | 问题诊断 | ✗ 实为竞品投诉 | 2 | N | bad |

人工回复后 48h 填写，月末导出分析，更新意图规则和评分权重。

---

## 去重与状态管理（概念设计）

### 状态文件设计

```
状态文件存放在 wiki/protocols/reddit-monitor-state/（git 跟踪）

seen-posts.json        ← 已推送过的帖子 ID（避免重复出现在清单）
replied-posts.json    ← 已实际回复过的帖子 ID（避免重复回复）
last-run-timestamp    ← 上次运行时间（用于增量拉取）
```

### 去重逻辑

```
对新发现的帖子 P：
  if P.id in seen-posts.json:
      skip（已推送过，等人工处理）
  else if P.id in replied-posts.json:
      skip（已回复过，不要重复）
  else if P.score < -5:
      skip（已被社区踩，回复效果差）
  else:
      add to seen-posts.json
      add to 今日待回复清单
```

### replied-posts.json 的更新时机

```
人工审核 → 决定回复 → 实际在 Reddit 发送
  ↓
  手动或自动将帖子 ID 写入 replied-posts.json
  ↓
  下次运行自动跳过
```

---

## 人工审核衔接设计

### 审核触发

每次 Arctic Shift 运行完成后，生成 `pending-replies.md`，人工打开即见。

### 审核决策树

```
打开 pending-replies.md
  │
  ├── 这条帖值得回复吗？
  │   ├── 是 → 复制到知识库 assistant-drafts/ 目录下
  │   │        → AI 起草回复草稿（见下节）
  │   │        → 人工修改 → 发送 → 记录到 replied-posts.json
  │   │
  │   ├── 不值得但值得关注 → 复制到 pain-points.md（仅记录用户原话）
  │   │
  │   └── 完全不相关 → 在 seen-posts.json 中标记 "ignore"
  │
  └── 清单为空？
      └── 正常，说明过去 24h 没有匹配的新帖（好现象，说明不是所有帖都要回）
```

### 审核 SOP（标准操作流程）

```
每日 08:30 / 13:30 / 18:30（每次 Arctic Shift 运行后 30 分钟）
  │
  ├── Step 1：打开 pending-replies.md
  ├── Step 2：逐条判断（每条约 30 秒）
  ├── Step 3：决定回复的帖子 → 交给 AI 起草（输入：帖子 URL + 知识库对应条目）
  ├── Step 4：审核 AI 草稿（修改语气/补充细节）
  ├── Step 5：在 Reddit 发送
  └── Step 6：将帖子 ID 写入 replied-posts.json
```

---

## AI 起草衔接设计

### 输入

```
AI 起草输入包：
  ├── 帖子原文（URL → 抓取标题 + 正文 + 热门评论）
  ├── KES 知识库对应条目
  │   ├── pain-points.md（用户痛点原话）
  │   ├── test-data/xxx.md（测试数据）
  │   └── competitor-comparisons.md（竞品对比）
  └── 回复结构模板（见下方）
```

### 回复结构模板（输入给 AI）

```
你正在帮 KES 起草一条 Reddit 回复。严格遵守以下结构：

1. 承认具体处境（1-2 句）
   - 显示你读懂了他的帖子，不要套话
   - 例：「自己换阀芯确实容易卡住，尤其是老房子的管道…」

2. 给出实质建议（3-5 句）
   - 直接有用的信息，不绕弯子
   - 可以引用测试数据，但用自然语言，不要像数据表

3. 标注局限（1 句）
   - 诚实说什么情况下你的建议不适用
   - 例：「如果你的是 xxx 型号，这个方法可能不适用，因为…」

4. 自然提产品（0-1 句，可选）
   - 仅当产品确实解决了他问的问题时才写
   - 例：「我们做过类似场景的测试，KES 的 xxx 设计就是针对这个问题的…」
   - 如果不确定，跳过这步。

检验标准：删掉所有关于 KES 的部分，这条回复还有价值吗？
```

### 输出

```
AI 输出：
  ├── 草稿正文（Markdown 格式，可直接复制粘贴到 Reddit）
  ├── 置信度评分（高/中/低）
  └── 建议发送时机（例如：「等 2 小时再发，刚发帖就回复容易被当 bot」）
```

---

## 时间与频率设计

### Arctic Shift 运行频率

| 时段 | 原因 |
|------|------|
| **08:00** | 美国东海岸早上（Reddit 流量高峰） |
| **13:00** | 美国西海岸早上 + 欧洲下午 |
| **18:00** | 美国晚高峰 |

**数据延迟补偿：** Arctic Shift 数据延迟约 1-2 小时，所以 08:00 运行实际覆盖 06:00-08:00 的新帖，足够。

### last30days 运行频率

| 频率 | 时间 | 目的 |
|------|------|------|
| 每周一次 | 周一 08:00 | 更新知识库 + 调整监控任务 |
| 触发式 | 产品上线前 2 周 | 研究目标市场的社区话语 |
| 触发式 | 竞品有重大动作 | 监控竞品社区口碑变化 |

---

## 指标与迭代

### 跟踪指标

| 指标 | 定义 | 目标 |
|------|------|------|
| 扫描帖子数/天 | Arctic Shift 每次运行返回的帖子总数 | 50-100（足够覆盖） |
| 待回复清单数/天 | 通过意图过滤后剩余的帖子数 | 3-8（可人工处理） |
| 实际回复数/天 | 人工审核后实际发送的数 | 2-5 |
| 回复得分均值 | 每条回复的 upvote 数 | > 3（说明被社区认可） |
| 转化率（Egypt） | 从 Reddit 引导到 WhatsApp 的对话数 | 每月 10+ |
| 意图误判率 | 人工修正 / 总分类数（月末统计） | < 20% |
| P0 遗漏率 | 月度人工抽查发现的 P0 遗漏帖数 | < 2 |

### 迭代触发条件

```
if 扫描帖子数 < 20 for 3 天:
    → 扩大监控任务（增加 subreddit 或关键词）

if 待回复清单数 > 15:
    → 收紧意图过滤（提高匹配门槛）

if 回复得分均值 < 1:
    → 审核回复质量（AI 草稿问题？人工修改不足？）

if 重复看到同一用户发类似帖:
    → 考虑主动发帖（而非只评论）

if 意图误判率 > 30% for 某分类:
    → 修订该分类的关键词规则（参考月末误判修正流程）

if P0 遗漏率 > 2:
    → 审查 Arctic Shift 关键词覆盖 → 扩大搜索范围
```

---

## 风险与限制

| 风险 | 缓解措施 |
|------|----------|
| Arctic Shift 数据延迟 1-2h | 仍在 24-48h 黄金窗口内，可接受 |
| 意图误判（AI 分类错误） | 人工审核列记录修正；月末统计误判率 → 修订分类关键词；高混淆对加硬规则屏蔽 |
| 分类遗漏（该回未入清单） | 月度人工抽查 2-3 个 subreddit 新帖 → 对比 AI 清单 → 分析遗漏原因 |
| 多个账号回复同一帖 | replied-posts.json 共享；账号间每日同步状态文件 |
| Arctic Shift API 不可用 | 降级：手动浏览目标 subreddit 新帖；同时检查 API 状态 |
| 过度依赖 AI 草稿（语气像 bot） | 人工审核必须修改至少 1 处；禁止使用 AI 标志性措辞 |

---

## 后续演进方向

| 阶段 | 能力 | 说明 |
|------|------|------|
| v1（当前设计） | 人工驱动 + Arctic Shift 发现 | 人工审核每条回复 |
| v2 | AI 草稿自动生成 | Arctic Shift 发现 → 自动调用 AI 起草 → 人工审核 |
| v3 | 多平台聚合 | 不止 Reddit：Quora、Discord 同样流程 |
| v4 | 效果反馈循环 | 回复得分 → 反馈到知识库 → 改进未来回复质量 |

---

## 附录：Subreddit 优先级评估框架

用于 last30days 发现新 subreddit 后，决定是否加入 Arctic Shift 监控清单。

```
评分维度（每项 1-5 分）：

1. 流量：该 subreddit 的会员数 & 日发帖量
2. 意图匹配：该版块的帖子是否经常涉及 KES 能解决的问题
3. 竞争强度：竞品是否活跃（太活跃 → 难以脱颖而出）
4. 社区规则友好度：版规是否允许品牌参与（有些版块完全禁止）
5. 语言匹配：是否英语（Egypt 线可以是阿拉伯语）

总分 ≥ 15 → 高优先级，立即加入监控
总分 10-14 → 中优先级，观察 2 周再决定
总分 < 10 → 低优先级，不监控
```
