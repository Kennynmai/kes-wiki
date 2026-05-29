---
type: synthesis
status: draft
owner: strategy
created: 2026-04-19
updated: 2026-04-19
visibility: company
confidence: medium
officiality: draft
domain: strategy
domains: [geo, aeo, ai-search, search, generative-ai]
source_count: 7
review_cycle: monthly
verification_status: spot-checked
related:
  - ../source-summaries/geo-paper-aggarwal-et-al-2024.md
  - ../source-summaries/e-geo-paper-bagga-et-al-2025.md
  - ../source-summaries/agentic-ecommerce-paper-allouah-et-al-2025.md
  - ../source-summaries/geo-platform-guidance-2025-2026.md
  - ../source-summaries/openai-shopping-official-docs-2025-2026.md
  - ../source-summaries/geo-ecosystem-operational-examples-2026.md
  - ./geo-tactics-taxonomy.md
  - ./geo-noise-and-hype-map.md
  - ./kes-geo-experiment-backlog.md
  - ./kes-geo-evidence-scoring-rubric.md
---

# GEO 研究全景｜截至 2026-04-19

## What this page is for
这页用于回答一个更基础的问题：

`GEO` 到底已经发展到什么程度了？

不是只看一个论文或一批营销博客，而是把目前可见材料拆成：
- 学术定义
- 学术扩展
- 攻击 / 操纵与鲁棒性研究
- 平台官方 guidance
- 商业服务与行业叙事

## Executive view
`GEO` 目前已经不是单篇论文概念，但也远没到稳定、标准化、可审计的成熟行业阶段。

更准确地说，它处于：
- 学术概念已成形
- 平台流量变化已真实发生
- 商业服务正在快速包装
- 官方平台 guidance 仍偏保守
- 可复制、稳定、跨平台的最佳实践仍不充分

## Layer 1｜Academic core
### GEO original paper
2024 年 KDD 的 `GEO: Generative Engine Optimization` 是核心起点。

它贡献的不是某个技巧，而是三件事：
- 给 generative-engine visibility 下定义
- 提出 impression metrics
- 用 benchmark + black-box optimization 测方法

目前看，这仍是 GEO 领域最关键的概念起点。

### E-GEO
`E-GEO` 把问题推进到 e-commerce：
- query 更长
- intent / constraints / preferences 更丰富
- 评价目标更接近 product reranking

它的重要贡献是把 GEO 从 web citation visibility 推到 product ranking improvement。

## Layer 2｜Academic expansion
### Agentic commerce line
`What Is Your AI Agent Buying?` 这篇论文把问题再推进一步：
- 不只是被引用
- 不只是被重排
- 而是 AI agent 直接做选择时会发生什么

这条线说明：
- GEO 很可能只是更大一套 `agent-mediated commerce optimization` 的前半段

### Robustness / manipulation line
`Ranking Manipulation for Conversational Search Engines` 这类研究提醒：
- 只研究“如何优化可见性”不够
- 还必须研究对抗性操纵、prompt injection、ranking manipulation

这意味着 GEO 领域从第一天起就不只是增长问题，也是鲁棒性与治理问题。

## Layer 3｜Official platform guidance
### Google
Google 官方目前最清楚的立场是：
- AI Overviews / AI Mode 没有额外 special optimization requirement
- classic SEO best practices still matter
- people-first content is still core
- page must be crawlable / indexable / snippet-eligible

但 Google 同时也明确披露：
- AI features may use query fan-out
- supporting links can be more diverse than classic search

这意味着：
- 平台官方话术是 “no special GEO hacks”
- 但底层机制已足够不同，不能把 classic SEO 原样照搬

### Bing
Bing 官方更明确给了 creator-side control：
- `data-nosnippet` 可控制哪些内容不进入 snippets / AI answers
- 但内容仍可被发现、索引、用于 ranking

这说明生成式搜索时代已经出现一个新分层：
- visible to the engine
- eligible for ranking
- eligible for preview / quoting

### OpenAI
OpenAI 这条线现在已经不只是“官方页面存在”。

当前可核对的一手文档已经明确写到：
- merchants can provide product feeds
- ChatGPT shopping 会使用 first-party / third-party structured metadata
- merchant ranking 会看 availability、price、quality、maker / primary seller、Instant Checkout
- ChatGPT search may rewrite prompts into more targeted queries
- inclusion 与 `OAI-SearchBot` / allowlisting 有关

这说明 OpenAI 在 commerce GEO 上已经公开覆盖了：
- crawler access
- feed ingestion
- merchant metadata
- merchant ranking
- signed-agent traffic

### Perplexity
Perplexity 这一层仍以抓取受限和官方可见摘要为主。

当前更稳妥的判断仍是：
- premium data source integration 是真实方向
- 但公开、可细读的一手 guidance 仍弱于 Google / Bing / OpenAI

## Layer 4｜Operational examples in the ecosystem
### Shopify merchant guidance
Shopify 官方 merchant guidance 说明，AI-search commerce 已经进入实际经营层：
- 可按 `ChatGPT` referrer 跟踪流量与订单
- 可手动监控高价值 prompts
- 官方推荐的 tactics 包括：
  - fact-rich PDP
  - pre-purchase tools
  - original research
  - trusted publication mentions

这说明 merchant-side GEO 正在从“写法技巧”扩展到：
- instrumentation
- product-surface design
- proprietary utility
- external authority building

### Vercel GPTBot incident
Vercel 社区的公开案例则补上了另一层现实：
- AI crawler visibility 可能带来真实 infra cost / load
- blocking GPTBot 可以止损
- 但也可能失去 ChatGPT search visibility

这说明 merchant / publisher 的 GEO 决策，不只是增长问题，也是：
- bot policy
- infra cost
- access-control tradeoff

## Layer 5｜Commercial market narrative
商业市场上已经出现大量：
- GEO agency
- GEO audit tool
- AI visibility report
- answer engine optimization consulting

但这一层目前噪音很大，主要问题有三个：
- case study 多缺少严谨归因
- 平台与 query set 往往不透明
- 很多服务把 SEO、PR、brand search、schema、citation、FAQ、LLM mention rate 混写成一个指标

因此商业材料可以当 signal，看“市场在卖什么”，但不适合直接当方法学事实。

## What appears to be real across the ecosystem
### 1. Crawlability still matters
无论是 Google、OpenAI 还是一般研究框架，前提都还是：
- content can be found
- content can be accessed

### 2. Structure matters more
比起传统 SEO，AI search / GEO 更重视：
- clean segmentation
- standalone answer units
- explicit attributes
- structured product details

### 3. Evidence density matters
学术 GEO 里高表现方法高度集中在：
- citations
- quotations
- statistics
- readability

### 3.5 Merchant data quality matters
OpenAI 的 shopping docs 已经把另一类现实写得更清楚：
- feed completeness
- metadata quality
- freshness
- merchant-level supply information

对 commerce GEO 来说，这一层不能再被压缩成“只是 schema”。

### 4. Reranking and agent-choice are separate layers
`E-GEO` 与 `ACES` 共同说明：
- 被召回
- 被重排
- 被 agent 选中

不是同一件事。

### 5. Manipulation pressure is real
GEO 越被商业化，越会引出：
- ranking manipulation
- prompt injection
- AI-SEO arms race

所以平台、品牌、研究者都会越来越重视：
- guardrails
- robustness
- provenance

## What is still weak / unresolved
### 1. Measurement is unstable
目前没有统一、平台无关、广泛被接受的 GEO measurement standard。

### 2. Cross-platform transfer is uncertain
在 Google AI Overviews 有效的方法，未必对 ChatGPT Search、Perplexity、Rufus 或未来 agent marketplace 同样有效。

### 3. Commercial case studies are still under-evidenced
市场上已很多 “visibility increased 300%” 之类说法，但大多不够可审计。

### 4. Official platform guidance remains conservative
平台官方通常不会给出：
- detailed ranking weights
- concrete GEO playbook

所以“行业实践”与“官方口径”之间天然有落差。

## Working taxonomy for KES
如果 KES 要继续研究 GEO，建议把它分成五个子问题：

1. `visibility GEO`
内容如何更容易被引用 / 摘要

2. `commerce GEO`
商品文本如何更容易被 generative reranker 看懂

3. `agentic commerce`
AI buyer / assistant 如何直接影响选择

4. `control layer`
哪些内容能被 preview / snippet / quote，哪些可以控制

5. `robustness / abuse`
哪些做法已经接近操纵、注入、攻击，而不是正常优化

## Current best reading
截至 2026-04-19，更稳妥的判断是：

- `GEO` 是真实存在的研究与商业化方向
- 但不能被当作稳定成熟的行业标准
- 真正可靠的做法仍然集中在：
  - crawlability
  - structure
  - evidence density
  - machine-readable product attributes
  - clear answer units
- 而不是：
  - keyword stuffing
  - hype tone
  - 一套平台通杀秘籍

## Sources
- [来源摘要｜Aggarwal et al. 2024｜GEO 原论文](../source-summaries/geo-paper-aggarwal-et-al-2024.md)
- [来源摘要｜Bagga et al. 2025｜E-GEO](../source-summaries/e-geo-paper-bagga-et-al-2025.md)
- [来源摘要｜Allouah et al. 2025｜AI Shopping Agents Buy What?](../source-summaries/agentic-ecommerce-paper-allouah-et-al-2025.md)
- [来源摘要｜GEO 平台官方 guidance（2025-2026）](../source-summaries/geo-platform-guidance-2025-2026.md)
- [来源摘要｜OpenAI 官方购物文档（2025-2026）](../source-summaries/openai-shopping-official-docs-2025-2026.md)
- [来源摘要｜GEO 生态实操案例（2026）](../source-summaries/geo-ecosystem-operational-examples-2026.md)
- [GEO Tactics Taxonomy](./geo-tactics-taxonomy.md)
- [GEO 噪音与营销包装地图](./geo-noise-and-hype-map.md)
- [KES GEO Experiment Backlog](./kes-geo-experiment-backlog.md)
- [KES GEO Evidence Scoring Rubric](./kes-geo-evidence-scoring-rubric.md)
- `raw/strategy/geo/2026-04-19/raw-capture-log.md`
