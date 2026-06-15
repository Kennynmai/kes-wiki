---
type: protocol
status: active
created: 2026-06-07
section: knowledge-base
related:
  - wiki/products/kes-product-knowledge-base/KNOWLEDGE-BASE-BUILD-GUIDE.md
  - wiki/protocols/reddit-post-discovery-system-design.md
  - wiki/protocols/ai-draft-pipeline-design.md
---

# 社区问题采集方案：知识库层 1 的数据管线

> 问题：知识库需要「用户原话」填充层 1。这些原话从哪里来？
> 答案：七条采集管线，各有不同的产出类型和使用场景。

---

## 管线总图

| # | 管线 | 产出 | 采集频率 | 适合的问题类型 | 当前状态 |
|---|------|------|:--:|------|:--:|
| 1 | Reddit 搜索（手动） | 历史高赞帖子 | 一次性 / 季度 | 高频问题（evergreen） | ✅ 随时可用 |
| 2 | Arctic Shift（自动） | 新帖实时推送 | 每日 | 热点问题（timely） | ⚠️ 待配置 |
| 3 | Amazon 评论 + Q&A | 购买者真实表述 | 一次性 / 季度 | 购买决策类问题 | ✅ 随时可用 |
| 4 | Quora 话题搜索 | 长尾深度问题 | 一次性 / 月度 | 选购指南类问题 | ✅ 随时可用 |
| 5 | YouTube 评论区 | 安装/使用后的痛点 | 一次性 / 季度 | 安装问题 | ✅ 随时可用 |
| 6 | last30days skill | 最近 30 天讨论趋势 | 每周 | 趋势发现 | ✅ 已安装 |
| 7 | 专业论坛 | 水管工/承包商视角 | 一次性 / 月度 | 技术深度问题 | ✅ 随时可用 |

---

## 管线 1：Reddit 搜索（手动）—— 最大的问题金矿

### 为什么 Reddit 是第一优先

- Reddit 是英语世界最大的「真实用户在家装后提问」的平台
- 帖子天然包含用户原话，不需要翻译或改写
- 高 upvote 数 = 这个问题的普遍性已经验证

### 操作方法

**Step 1：在 Google 搜索（比 Reddit 内置搜索更好用）**

```
site:reddit.com bathroom faucet leaking reddit
site:reddit.com "shower head" "hard water" replacement
site:reddit.com "how to choose" faucet OR "shower head"
site:reddit.com plumber recommended faucet
site:reddit.com "worst faucet" OR "faucet regret"
```

**Step 2：筛选标准**

| 筛选维度 | 标准 |
|----------|------|
| 时间 | 最近 3 年内的帖子（产品和技术变化慢，旧帖依然有价值） |
| upvote | 50+ 表示这个问题有普遍性 |
| 评论数 | 20+ 表示社区参与度高 |
| 情绪 | 优先选「求助」「困惑」「踩坑」类帖子（购买意图最强） |

**Step 3：录入知识库的格式**

```markdown
## 问题：花洒/水龙头用了 1-2 年开始滴水

**来源：** Reddit r/HomeImprovement, 2025-11
**原帖标题：** "Installed a new shower head last year, now it drips constantly"
**Upvote:** 230 ｜ **评论数:** 87
**URL:** https://reddit.com/r/HomeImprovement/comments/xxx

**用户原话：**
"标题这句话就是用户原话。另外评论区高赞回复也收录：
- 'Same here, every faucet in my house started dripping after 18 months'
- 'Is this a hard water thing or did I buy cheap fixtures?'"

**意图判断：** 购买意图（用户已在使用中遇到问题，可能寻找替代品）
**KES 可切入角度：** 解释「塑料阀芯 vs 陶瓷阀芯」的寿命差异
```

### 工作量估算

一次 Google 搜索 = 5-10 分钟 → 产出 5-15 条可录入的问题。

50-100 条问题 = 约 10 次搜索 × 5-10 分钟 = **1-2 小时可完成初始采集**。

---

## 管线 2：Arctic Shift（自动）—— 每日新问题的实时水源

### 与管线 1 的区别

| | 管线 1（手动搜索） | 管线 2（Arctic Shift） |
|---|---|---|
| 采集内容 | 历史高赞帖（evergreen） | 实时新帖（timely） |
| 用途 | 构建初始知识库 | 每日推送可回复帖子 + 发现新问题类型 |
| 问题质量 | 经过社区投票验证 | 未经验证（需要人工判断） |

### 配置关键词（与 post-discovery 系统共用）

已在 `reddit-post-discovery-system-design.md` 中定义：

| 监控任务 | Subreddit | 关键词 | KES 产品线 |
|----------|-----------|--------|-----------|
| 卫浴五金-选购 | r/HomeImprovement | faucet, shower head, bathroom hardware, best faucet | 卫浴五金 |
| 卫浴五金-维修 | r/Plumbing | leak, drip, replace faucet, valve | 卫浴五金 |
| 硬水问题 | r/HomeImprovement, r/Plumbing | hard water, limescale, calcium, aerator clogged | 卫浴五金 |
| 窗帘-Egypt | r/Egypt, r/interiordecorating | curtain, roller blind, window shade, Egypt | 窗帘 Egypt |
| 装修-Egypt | r/Egypt | renovation, apartment, furnishing | 窗帘 Egypt |

### 从 Arctic Shift 到知识库的流水线

```
Arctic Shift 每日推送 (约 50-80 条)
    │
    ├──→ 高优先（匹配关键词 + 购买意图）→ 立即回复
    │
    ├──→ 新问题类型（之前没见过）→ 加入知识库层 1（新增条目）
    │
    └──→ 已匹配问题的新表述 → 加入知识库层 1（补充变体）
```

---

## 管线 3：Amazon 评论与 Q&A —— 购买者的真实表述

### 为什么 Amazon 是独特的来源

- 评论者已经付过钱了——他们的表述最贴近购买决策时的心理
- Q&A 部分直接显示「潜在买家在纠结什么」
- 负面评论（1-3 星）是竞品弱点的直接证据

### 操作方法

**搜索 KES 自营产品评论区（了解 KES 用户语言）：**

> 进任意一个 KES Amazon listing → 看 Q&A 区 + 1-3 星评论
> 问题不是「产品怎么样」，而是「用户用的是什么词在描述问题」

**搜索竞品评论区（了解竞品弱点 + 行业通用问题）：**
> 找 GROHE、Moen、Delta 在 Amazon 上卖得最好的 listing
> → 读 1-2 星评论（用户不满什么）
> → 读 Q&A（潜在买家在犹豫什么）

### 采集示例

```markdown
## 问题：「水龙头安装后水压明显变小」

**来源：** Amazon Q&A, Delta Faucet 某型号, 2025-08
**用户原话：**
"Does anyone else feel the water pressure dropped a lot after installing this?"
"I have good pressure everywhere else in the house but this faucet is like a trickle."

**意图判断：** 安装后问题 → 已购买但不满（可能换品牌）
**KES 可切入角度：** 解释水压限制器 + KES 产品的流量设计
```

---

## 管线 4：Quora 话题搜索 —— 长尾「选购指南」问题

### Quora 问题的特点

| 特点 | 对知识库的价值 |
|------|---------------|
| 问题表述完整 | 用户写了完整的句子，不像 Reddit 帖子有时很碎 |
| 生命周期长 | 一条 Quora 问题 5 年后依然有人搜索 |
| SEO 价值高 | Google 搜索「best faucet for hard water」→ Quora 链接常排第 1 页 |

### 操作方法

在 Quora 搜索框输入（不需要登录）：

```
bathroom faucet
best shower head
plumbing DIY
renovation tips
hard water solution
```

筛选：回答数 > 5 + 最后活跃 < 1 年 + 浏览量大。

### Quora 独有价值

不同于 Reddit 的「我正在遇到这个问题」，Quora 的问题是「我想提前了解这个问题」——这两种意图在知识库中需要区分对待。

---

## 管线 5：YouTube 评论区 —— 看不见的痛点

### 为什么 YouTube 评论有独特价值

- 用户在视频下方详细描述自己的具体问题（比 Reddit 帖子更具体）
- 安装教程视频的评论区是「安装痛点」的最大聚合点
- 竞品测评视频的评论区是「竞品弱点」的直接来源

### 操作方法

**找视频：**
```
YouTube 搜索：
- "faucet installation common mistakes"
- "shower head replacement DIY"
- "GROHE faucet review"  /  "Moen faucet review"
- "best bathroom faucet 2025"
```

**采集评论区：**
- 不看 creator 回复，只看观众评论
- 高赞评论 = 「这是很多人有的问题」
- 注意用户的语言——那种「我都装了 3 个了还是不行」的情绪

---

## 管线 6：last30days skill（每周）—— 趋势发现

### last30days 的独特价值

| 其他管线能看到 | last30days 能看到 |
|---------------|------------------|
| 历史问题 | 最近 30 天哪些问题突然多了 |
| 已知问题 | 新出现的问题类型 |
| 单个平台 | 跨平台热度对比 |

### 已配置的搜索任务

来自 `reddit-post-discovery-system-design.md` Track A：

```
"bathroom faucet leaking common causes"
"best shower head for hard water"
"how to choose bathroom hardware"
"DIY plumbing common mistakes"
"faucet brand comparison"
```

**产出：** 每周一跑一次 → 输出「本周趋势报告」→ 新出现的问题加入知识库层 1。

---

## 管线 7：专业论坛 —— 技术深度问题

### 为什么需要专业论坛

Reddit 和 Quora 的问题偏「普通消费者」。水管工、承包商的问题更技术、更刁钻——但这些回答的质量最高，也最容易被同行引用。

### 目标论坛

| 论坛 | URL | 采集方式 |
|------|-----|----------|
| ContractorTalk | contractortalk.com | Google site:搜索（开放访问） |
| TerryLove Plumbing | terrylove.com/forums | Google site:搜索（开放访问） |
| Houzz Discussions | houzz.com/discussions | Google site:搜索 |

### 搜索模板

```
site:contractortalk.com faucet recommendation
site:terrylove.com "best faucet" OR "faucet brand"
site:houzz.com bathroom hardware recommendation
```

**注意：** 这些论坛的问题，语气、术语和 Reddit 完全不同。录入知识库时保留原文——因为你要回复的对象也用的是这种语言。

---

## 采集优先级与时间分配

### Phase 0（本周，构建初始知识库）

| 管线 | 操作 | 预计时间 | 预期产出 |
|------|------|:--:|:--:|
| 管线 1（Reddit 搜索） | 10 次 Google 搜索 | 1-2 小时 | 50-100 条问题 |
| 管线 3（Amazon 评论） | KES + Delta + Moen 各 3 个 listing | 1 小时 | 30-50 条问题/痛点 |
| 管线 4（Quora 搜索） | 5 个关键词搜索 | 30 分钟 | 20-30 条问题 |

**总计：2.5-3.5 小时 → 产出 100-180 条问题候选 → 精选 20-30 条录入知识库。**

### Phase 1+（持续运营）

| 管线 | 频率 | 单次时间 | 方式 |
|------|:--:|:--:|------|
| Arctic Shift（管线 2） | 每日 | 5 分钟 | 看推送，标记新问题类型 |
| last30days（管线 6） | 每周 | 10 分钟 | 跑一次，看趋势 |
| YouTube（管线 5） | 每季度 | 1 小时 | 批量采集 |
| 专业论坛（管线 7） | 每月 | 30 分钟 | 补充技术深度问题 |

---

## 从采集到录入的判断标准

不是所有采集到的问题都值得录入知识库。用这个过滤器：

```
采集到一条「用户原话」
    │
    ├──→ 这个问题 KES 产品能解决吗？
    │       ├── 不能 → 放弃
    │       └── 能 ↓
    │
    ├──→ 这个问题出现频率高吗？
    │       ├── 单次出现 → 录入选做（标注「低频」）
    │       └── 高频（多个帖子/平台都出现）→ 必须录入
    │
    ├──→ 这个问题有明确的「购买意图」吗？
    │       ├── 纯聊天/观点 → 不一定录入
    │       └── 求助/比较/选购 → 优先录入
    │
    └──→ 这个问题有可验证的证据吗？
            ├── 没有 → 标注 [待补证据]
            └── 有 → 完整录入三层
```

---

## 快速启动：现在就产出第一批问题

以下搜索词可以直接用，现在登录 Google 就能出结果：

**卫浴五金（5 组搜索）：**
```
1. site:reddit.com bathroom faucet leaking hard water
2. site:reddit.com "shower head" replacement recommendation
3. site:reddit.com plumbing faucet brand worth it
4. site:reddit.com HomeImprovement "worst faucet"
5. site:reddit.com "water pressure dropped" faucet
```

**窗帘 Egypt（2 组搜索）：**
```
6. site:reddit.com Egypt curtain roller blind
7. site:reddit.com interiordecorating window treatment hot climate
```

**Amazon（直接访问 Amazon.com 搜索）：**
```
8. KES Faucet → Q&A section
9. Delta Faucet (best seller) → 1-2 star reviews
10. Moen Faucet (best seller) → Q&A section
```
