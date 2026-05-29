---
type: source-summary
status: draft
owner: strategy
created: 2026-04-19
updated: 2026-04-19
visibility: team
confidence: medium
officiality: draft
domain: platform
domains: [amazon, rufus, conversational-shopping, agentic-ai, ecommerce-search]
source_type: official-company-material
extraction_mode: progressive
source_title: Amazon official Rufus launch and capability updates
source_date: 2024-02 to 2026
source_author: Amazon / About Amazon
raw_path: ../../raw/platforms/amazon/rufus-cosmo/2026-04-19/official-pages/aboutamazon-rufus-launch.html
verification_status: spot-checked
related:
  - ../platforms/amazon-rufus-and-cosmo.md
  - ../../raw/platforms/amazon/rufus-cosmo/2026-04-19/raw-capture-log.md
---

# 来源摘要｜Amazon 官方 Rufus 更新（2024-2026）

## Why this source matters
这组官方页面用来回答三个问题：
- Rufus 对外是怎么定义的
- 它从 2024 首发到 2026 演进了哪些能力
- Amazon 官方目前公开承认了哪些模型与业务指标

## Extracted facts / observations
### 2024-02-01 launch framing
- Amazon 把 Rufus 定义为 generative AI-powered expert shopping assistant。
- 官方描述的训练 / grounding 来源包括：
  - Amazon product catalog
  - customer reviews
  - community Q&As
  - information from across the web
- 首发支持的典型场景包括：
  - broad category research
  - comparison
  - recommendation
  - PDP-specific questions
- 2024-02-01 的上线范围是：
  - U.S. mobile app 小范围 beta

### 2024-07 usage update
- Amazon 官方称 Rufus 已在 2024 年向 all U.S. customers 开放。
- 入口扩展到：
  - Amazon Shopping app
  - desktop
- 官方使用案例还扩展到：
  - order tracking
  - access to past orders
  - broader pre-shopping questions

### 2026 capability update
- 官方最新公开表述把 Rufus 定义为：
  - powered by generative and agentic AI
  - in the app and website
- 官方称其通过 Amazon Bedrock 调用多模型组合：
  - Anthropic Claude Sonnet
  - Amazon Nova
  - custom-built model
- 官方还说 Rufus 使用 RAG，并会引用一些外部流行来源回答产品 / 趋势问题。
- 2026 年公开的新能力包括：
  - account memory / preference memory
  - reorder past items
  - image-based search / problem solving
  - price history, price alerts, auto-buy
  - Buy for Me / off-Amazon purchase support
  - customer-service-like order / return support

### latest official adoption signals seen in 2026 material
- 官方说 2026 年内已有超过 250 million customers 用过 Rufus。
- 官方说 monthly users up 140%+ YoY，interactions up 210% YoY。
- 官方说使用 Rufus 的 shopping journey，conversion 更高，公开口径为 60%+ more likely to convert。

## What this source supports
- Rufus 已经从 2024 的 shopping Q&A assistant，演化为更广义的 personalized / agentic shopping interface。
- 官方已不再把 Rufus仅描述成单一模型，而是 mix-of-models + Bedrock + RAG + custom model 的系统。
- Rufus 是一个持续扩展的 shopping surface，而不是单点功能。

## What this source does not support
- 不支持据此精确重构 Rufus 的内部 routing、ranking、tool-use 或 memory architecture。
- 不支持把 Amazon 对 adoption / conversion 的对外数字直接当作审计级财务口径。
- 不支持把所有 2026 新能力都推断为所有国家 / 所有用户已一致可用。

## Caveats / ambiguity
- 这些页面是官方产品传播材料，不是系统论文。
- 业务指标和能力描述具有对外宣传属性。
- 对具体 feature rollout 范围、地域覆盖、实验组定义仍需谨慎。

## Related pages
- [Amazon Rufus and COSMO](../platforms/amazon-rufus-and-cosmo.md)

## Sources
- https://www.aboutamazon.com/news/retail/amazon-rufus
- https://www.aboutamazon.com/news/retail/how-to-use-amazon-rufus
- https://www.aboutamazon.com/news/retail/amazon-agentic-ai-gen-ai-shopping
- https://www.aboutamazon.com/news/retail/amazon-rufus-ai-assistant-personalized-shopping-features
- `raw/platforms/amazon/rufus-cosmo/2026-04-19/official-pages/aboutamazon-rufus-launch.html`
