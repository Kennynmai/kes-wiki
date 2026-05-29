---
type: synthesis
status: draft
owner: strategy
created: 2026-04-19
updated: 2026-04-23
visibility: company
confidence: medium
officiality: draft
domain: strategy
domains: [kes, geo, experimentation, ai-search, content-operations]
source_count: 7
review_cycle: monthly
verification_status: spot-checked
related:
  - ./geo-tactics-taxonomy.md
  - ./geo-noise-and-hype-map.md
  - ./geo-research-landscape.md
  - ./amazon-rufus-cosmo-e-geo-kes-response.md
  - ../playbooks/amazon-rufus-geo-audit-and-corroboration-playbook.md
  - ../source-summaries/kes-independent-site-content-ai-visibility-note-2026-04-23.md
---

# KES GEO Experiment Backlog

## What this page is for
这页把 GEO 相关想法从“原则”推进到“可排期测试的 backlog”。

目标不是证明某个 GEO 理论，而是建立一套：
- 可测
- 可复盘
- 可逐步淘汰伪信号

的实验序列。

## How to read this backlog
每个实验都按五个维度看：
- `goal`
- `hypothesis`
- `change`
- `metric`
- `risk`

## Priority model
### P1
低风险、高通用性、跨平台更可能成立

### P2
中风险，需要更具体场景或品类支持

### P3
高不确定性，偏 sandbox / exploratory

## New write-back｜2026-04-23 operator note
本轮新增的 user-provided operator note，给 backlog 补了四个更适合独立站 / 出海内容的执行重心：
- 不再只做 keyword list，而是建立 high-value question map
- 不再只做页面存在，而是做可被 AI 引用的 answer asset
- 不再只经营官网单点，而是补 external signal stack
- 不再只看 SEO / traffic / CVR，而是加 AI visibility scoreboard

这四点不是新理论，更像是把现有 GEO 研究翻译成更适合 KES 的 operating layer。

## Experiment 1｜Eligibility Audit
### Priority
`P1`

### Goal
先排除“页面根本不具备 AI-visible eligibility”的低级问题。

### Hypothesis
很多所谓 GEO 问题，本质是 crawl / index / snippet / schema 基础层缺失。

### Change
- audit important pages for crawlability
- audit snippet controls
- audit canonical / duplicate setup
- audit product structured data

### Metric
- pages eligible for indexing
- pages eligible for snippets
- structured-data completeness rate
- duplicate / canonical conflict count

### Risk
低。主要是排查，不改文案结论。

## Experiment 2｜Fact Density Upgrade
### Priority
`P1`

### Goal
验证“更多可引用事实”是否改善 AI-visible answer quality。

### Hypothesis
相比纯营销叙述，带明确数字、条件、边界的页面更容易被 AI 引用和复用。

### Change
- 补充 quantitative facts
- 补充 explicit conditions
- 补充 source-backed statements

### Metric
- answer inclusion rate in sandbox
- citation reuse rate in internal AI tests
- human judgment on answer completeness

### Risk
中低。需要证据充足，避免为了数字而数字。

## Experiment 3｜Readable Chunking Rewrite
### Priority
`P1`

### Goal
验证更清晰的 sectioning / chunking 是否提高 answer-surface 表现。

### Hypothesis
独立、短小、完整的答案单元比大段混合叙述更容易被生成式系统抽取。

### Change
- break long paragraphs
- add explicit section labels
- turn vague copy into short answer units

### Metric
- answer extraction quality
- summary faithfulness
- inclusion stability across prompts

### Risk
低。主要是结构调整。

## Experiment 4｜Product-Type Noun Exposure
### Priority
`P1`

### Goal
验证缺失的 product-type noun 是否是 commerce GEO 的核心 blocker。

### Hypothesis
商品标题 / PDP 若没明确 product-type noun，会同时伤害 retrieval 和 rerank。

### Change
- add missing product-type noun to title / top section
- align title with query-native object name

### Metric
- retrieval coverage proxy
- rerank score in sandbox
- comparison-query fit

### Risk
中。可能影响现有 SEO / title length tradeoff。

## Experiment 5｜Use-Case Front-Loading
### Priority
`P2`

### Goal
测试 decisive use-case token 提前是否改善 shopping-agent alignment。

### Hypothesis
对于 scenario-driven query，前部 use-case token 比后部长文解释更有效。

### Change
- front-load use-case term
- compare title variants with and without early use-case emphasis

### Metric
- choice share in sandbox
- rerank change
- prompt-family sensitivity

### Risk
中。可能牺牲更广泛泛化性。

## Experiment 6｜Spec Exposure Test
### Priority
`P2`

### Goal
测试 missing specs 暴露是否改善 agent-choice。

### Hypothesis
显式规格词能帮助 agent 更快做 match 与 elimination。

### Change
- add missing structural / functional specs
- move specs higher in title / bullets

### Metric
- rank delta in e-commerce sandbox
- choice delta in agent-choice sandbox
- human evaluator relevance score

### Risk
中。要防止 spec overload。

## Experiment 7｜Bundle / Accessory Exposure
### Priority
`P2`

### Goal
验证 bundle / included items 是否是被低估的 agent-choice feature。

### Hypothesis
像 `with X accessories` 这类信息如果埋得太后，agent 会低估 total offer value。

### Change
- move included accessories into early title / bullets
- test with / without bundle front-loading

### Metric
- agent-choice share
- comparison-query performance
- offer clarity score

### Risk
中。只适合 bundle-sensitive products。

## Experiment 8｜Comparison Module Test
### Priority
`P2`

### Goal
验证显式 comparison block 是否提高 mid-funnel answer visibility。

### Hypothesis
比较问题是 AI shopping assistant 的高频场景，页面若已有 comparison-ready content，更容易被系统复用。

### Change
- add “who is this for / not for”
- add adjacent alternative comparison
- add tradeoff section

### Metric
- inclusion in comparison-style prompts
- reduction in answer ambiguity
- human evaluator judgment on decision support

### Risk
中。需要控制 claim discipline。

## Experiment 9｜FAQ as Real Answer Surface
### Priority
`P2`

### Goal
验证 FAQ 从营销模板改成真实问题回答后是否提升 AI reuse。

### Hypothesis
多数品牌 FAQ 目前太像 filler，真实 FAQ 才是 answer-surface asset。

### Change
- rewrite FAQ with specific, bounded answers
- remove fluff questions
- add objection-driven questions

### Metric
- answer reuse rate
- unresolved objection rate
- Q&A overlap quality

### Risk
低中。需要较多人工整理问题。

## Experiment 10｜Structured Attribute / Merchant Data Alignment
### Priority
`P1`

### Goal
把页面可见信息与 structured product data 对齐。

### Hypothesis
AI-search / rich product surfaces 会奖励：
- visible attributes
- machine-readable attributes

同时一致。

### Change
- align page content with schema / merchant data
- fill missing shipping / return / availability / ratings fields

### Metric
- attribute completeness score
- rich result eligibility proxy
- consistency error count

### Risk
低。偏数据治理。

## Experiment 11｜External Corroboration Page
### Priority
`P2`

### Goal
测试品牌站上的 comparison / FAQ / care page 是否能反向支撑 AI visibility。

### Hypothesis
如果外部可引用页面更清晰，AI systems 更容易把品牌当成 authority source。

### Change
- publish one high-quality corroboration page
- publish one high-objection FAQ or comparison page, not generic blog copy
- align with on-platform product claims
- wire the page to target query families: comparison / non-fit / objection / maintenance

### Metric
- external citation appearance in search-based AI tools
- consistency across surfaces
- assisted answer quality
- support-deflection proxy
- assisted click-through to commerce surface

### Risk
中。需要跨 surface governance。

## Experiment 12｜Snippet Control Audit
### Priority
`P2`

### Goal
找出哪些内容不该被 AI preview。

### Hypothesis
并非所有被引内容都值得暴露；有些表格、实验性内容、内部术语应该控制预览。

### Change
- audit candidate content for `nosnippet` / `data-nosnippet`
- test selective hiding on non-essential sections

### Metric
- preview quality
- leakage of low-value content
- discoverability preserved vs preview reduced

### Risk
中。错误设置可能伤可见性。

## Experiment 13｜Model-Drift Watchlist
### Priority
`P1`

### Goal
把 GEO 变成连续观测，而不是一次性优化。

### Hypothesis
内容表现变化可能更多来自 model drift 而不是页面本身。

### Change
- fixed prompt set
- fixed competitor set
- periodic reruns

### Metric
- week-over-week inclusion delta
- model-drift delta
- rank / choice volatility

### Risk
低。主要是监测成本。

## Experiment 14｜Query-Family Matrix
### Priority
`P1`

### Goal
不要只测单一 query。

### Hypothesis
同一内容在不同 query family 下表现差异很大。

### Change
build query matrix:
- broad
- comparison
- scenario
- objection
- support / post-purchase

### Metric
- coverage by query family
- weakest-family score
- variance across families

### Risk
低。偏实验设计。

## Experiment 15｜Agent-Choice Sandbox
### Priority
`P3`

### Goal
验证在更接近 ACES 的环境里，哪些 title / description tweak 影响 actual choice。

### Hypothesis
部分 tactic 对 answer visibility 有用，但对 agent-choice 未必有效。

### Change
- construct fixed product set
- randomized order
- evaluate choice under multiple model families

### Metric
- choice share
- concentration ratio
- sensitivity to position / endorsement / labels

### Risk
高。最容易被过拟合和误读。

## Experiment 16｜Monthly Rufus Query Audit
### Priority
`P1`

### Goal
把 Amazon GEO 观察从偶发截图升级成固定 monthly operating rhythm。

### Hypothesis
很多所谓内容问题，只有在固定 query family、固定 competitor set、固定记录模板下，才看得出是页面问题还是 model drift。

### Change
- define fixed Rufus audit query set
- rerun monthly against fixed ASIN + competitor set
- score inclusion / factuality / decision usefulness / comparison quality

### Metric
- query-family coverage

## Experiment 17｜High-Value Question Map
### Priority
`P1`

### Goal
把内容规划入口从关键词池改成真实问题池。

### Hypothesis
对于独立站 / AI-search 场景，真实问题比短关键词更能同时服务：
- retrieval
- answer reuse
- comparison intent
- objection handling

### Change
- build a 50-question map from Amazon / customer service / reviews / search suggestions
- cluster by rust-proof / installation / small-space / renter-friendly / material-comparison / maintenance
- select 10 questions as first execution batch

### Metric
- question-family coverage
- % of priority questions with a dedicated answer page
- overlap rate between question map and support / review language

### Risk
低。主要风险是问题选择过泛或脱离真实用户语言。

## Experiment 18｜Best-Answer Page Template
### Priority
`P1`

### Goal
把单页内容从 generic SEO page 升级成 citable answer asset。

### Hypothesis
带有场景、步骤、参数、对比、适用边界、优缺点的页面，比泛营销 copy 更容易被 AI systems 复用。

### Change
- create a fixed answer-page template
- require title-as-question
- require scenario / steps / specs / comparison / fit-non-fit / common-problems blocks
- rewrite one existing FAQ or comparison page using the template

### Metric
- answer completeness score
- citation-style reuse in internal tests
- reduction in vague-copy ratio

### Risk
中低。需要约束 claim discipline，避免为了可引用而虚构参数。

## Experiment 19｜External Signal Stack
### Priority
`P2`

### Goal
不要把外部可见度理解成“做 Reddit”，而是建立多 surface 的 corroboration stack。

### Hypothesis
如果品牌只在官网自述，AI systems 更难在外部 comparison / recommendation 场景中持续引用该品牌。

### Change
- define a stack covering Reddit, Quora, YouTube review scripts, blog review partnerships, Amazon Q&A / review mining, home-improvement forums, and owned FAQ / comparison pages
- assign each target question family to one or more external surfaces
- track which surfaces actually mention KES vs competitors

### Metric
- external-surface coverage by question family
- brand mention share vs competitors
- corroboration diversity score

### Risk
中。不同 surface 的 governance 与 effort cost 差异较大。

## Experiment 20｜AI Visibility Scoreboard
### Priority
`P1`

### Goal
把 AI visibility 变成固定经营看板，而不是零散截图。

### Hypothesis
如果没有固定 scoreboard，团队会高估个别成功案例，低估 query-family gaps 与 competitor share-of-answer。

### Change
- run a fixed prompt set across ChatGPT, Perplexity, and Google AI Overviews
- record whether KES is mentioned, which page is cited, which claim is reused, and which competitors appear instead
- review the scoreboard on a fixed cadence

### Metric
- mention rate by tool
- cited-page distribution
- claim reuse distribution
- competitor-over-KES gap by question family

### Risk
低。主要风险是样本设计过窄。
- inclusion delta month-over-month
- repeated misunderstanding count
- competitor mention share
- drift volatility

### Risk
低。主要是执行纪律。

## Suggested execution order
### Phase 1
- Experiment 1
- Experiment 2
- Experiment 3
- Experiment 10
- Experiment 13
- Experiment 14
- Experiment 16

### Phase 2
- Experiment 4
- Experiment 5
- Experiment 6
- Experiment 8
- Experiment 9

### Phase 3
- Experiment 7
- Experiment 11
- Experiment 12
- Experiment 15

## Backlog rules
### Rule 1
任何实验都必须记录：
- original version
- modified version
- exact change type
- evidence basis

### Rule 2
任何 uplift 都至少要注明：
- tested on what model(s)
- tested on what query family
- tested on what competitor set

### Rule 3
任何 tactic 若违反 factual discipline，不进入 backlog。

### Rule 4
任何 tactic 若只在单一模型下有效，默认不升为 standard。

## Sources
- [GEO Tactics Taxonomy](./geo-tactics-taxonomy.md)
- [GEO 噪音与营销包装地图](./geo-noise-and-hype-map.md)
- [GEO 研究全景](./geo-research-landscape.md)
- [Amazon Rufus / COSMO / E-GEO｜KES 如何利用与应对](./amazon-rufus-cosmo-e-geo-kes-response.md)
