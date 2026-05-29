---
type: source-summary
status: draft
owner: strategy
created: 2026-04-19
updated: 2026-04-19
visibility: team
confidence: medium
officiality: draft
domain: strategy
domains: [agentic-ecommerce, ai-shopping-agent, amazon, marketplace, geo]
source_type: academic-paper
extraction_mode: abstract-plus-detailed-notes
source_title: What Is Your AI Agent Buying? Evaluation, Biases, Model Dependence, and Emerging Implications for Agentic E-Commerce
source_date: 2025-12-15
source_author: Amine Allouah et al.
raw_path: ../../raw/platforms/amazon/rufus-cosmo/2026-04-19/external-papers/agentic-ecommerce-aces-arxiv-2508.02630.pdf
verification_status: spot-checked
related:
  - ../platforms/amazon-rufus-and-cosmo.md
  - ../syntheses/amazon-rufus-cosmo-e-geo-kes-response.md
  - ../../raw/platforms/amazon/rufus-cosmo/2026-04-19/raw-capture-log.md
---

# 来源摘要｜Allouah et al. 2025｜AI Shopping Agents Buy What?

## Why this source matters
这篇论文把问题从 “生成式回答如何引用内容” 往前推了一步，研究：
- 当 AI agent 直接代替用户买东西时，会出现什么偏差
- 卖家与平台还能如何博弈

它对 KES 的价值在于：未来不只是 `Rufus` 这类 assistant 回答问题，还可能出现 agent 直接做选择。

## Extracted facts / observations
- 论文构建了 ACES（Agentic e-CommercE Simulator）来评估 AI shopping agents。
- 研究发现 AI agents 会出现：
  - strong but heterogeneous position effects
  - choice homogeneity
  - model dependence
  - model-upgrade-driven market share swings
- 论文指出：
  - sponsored tags generally depress selection
  - platform endorsements create strong lifts
  - price / ratings / reviews sensitivities vary by model
- 这些效应在：
  - headless / API-style interface
  - prompt variation
  - model upgrades
  
  下仍然存在。
- 作者还测试了 seller-side agent，对 description 做 query-conditional tweaks，可带来显著 market-share gains。
- 文中给出的平均市场份额增量示例包括：
  - +3.66 p.p. 到 +14.89 p.p.，视不同 buying model 而定

## What the seller-side agent actually changed
论文并不是笼统说 “优化文案”，而是给了更具体的改动模式。

### 1. Front-loading the query-critical token
- Office lamp 案例里，原始标题起手是：
  - `SUNMORY Floor Lamps for Living Room...`
- seller agent 改成：
  - `SUNMORY Office Floor Lamp...`
- 论文作者明确将其解释为：
  - 把 `Office` 从后部移到前五个 token
  - 减少 buying agent 对 query `office lamp` 的 semantic friction

### 2. Keyword enrichment, not generic fluff
- Fitness watch：
  - 原始是 `GPS Running Watch`
  - 改成显式包含 `Fitness Smartwatch` 或 `Fitness Running Tracker`
- Toothpaste：
  - 从较长的品牌味型叙述，改成更直接的 `Whitening Toothpaste`
- Toilet paper：
  - 补入 `2-Ply`、`Septic-Safe`、`Fragrance-Free`
- Washing machine：
  - 补入 `Top-Load`、`Stainless Steel Tub`

### 3. Accessory / bundle information moved earlier
- Stapler 案例：
  - 把 `with 1,250 Staples` 这类配件 / bundle 信息前置
  - 作者将其视为带来 +9.5 p.p. gain 的关键因素之一

### 4. Technical spec density increased in the title
- Office lamp 优化里，seller agent 不只是加 `Office`
- 还把 `32W`、`3000LM`、`Stepless Dimmable` 等 spec 往标题前部集中
- 论文作者推断，这会更符合 buying agent 对“workspace suitability / quality”的内部启发式

### 5. Semantic realignment, not just shortening
- 论文明确说，提升不主要来自 shorter copy
- 更主要的 driver 是：
  - information reordering
  - keyword alignment
  - semantic realignment

## Prompt / setup notes
- seller agent 不是凭空编造关键词
- prompt 明确要求：
  - title changes must align with provided product features
  - do not make up product features
  - do not add spurious keywords
- 还会提供：
  - focal product details
  - listing screenshot
  - competitors
  - simulated sales data from 200 experiments

## Practical reading
这篇论文给出的 seller-side tweak，更接近以下模式：
- move the right word earlier
- replace vague phrase with query-native phrase
- expose missing product-type noun
- expose missing structural / functional attributes
- expose bundle / accessory count earlier

而不是：
- 夸张形容词
- 冗长品牌故事
- 空泛 persuasive copy

## What this source supports
- AI-mediated shopping 不是简单复刻 human shopping。
- 平台排序、endorsement、界面结构、模型版本会显著改变需求分配。
- 卖家侧也会出现新一轮 description optimization / seller-agent 博弈。
- 因此 KES 不能只做静态 listing 优化，而需要持续监测模型漂移与可见性漂移。

## What this source does not support
- 不支持把论文里的 agent behavior 直接当作 Amazon Rufus 当前真实生产表现。
- 不支持把某个模型观察到的 position bias 当作普遍规律。

## Caveats / ambiguity
- 这是 sandbox research，不是 Amazon 官方线上实验。
- 但它很适合补足 `Rufus` 官方资料里没有披露的 “agentic market dynamics”。

## Sources
- https://arxiv.org/pdf/2508.02630
- https://business.columbia.edu/faculty/research/what-your-ai-agent-buying-evaluation-implications-and-emerging-questions-agentic-e
- `raw/platforms/amazon/rufus-cosmo/2026-04-19/external-papers/agentic-ecommerce-aces-arxiv-2508.02630.pdf`
