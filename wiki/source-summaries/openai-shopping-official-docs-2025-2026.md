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
domains: [geo, ai-search, openai, chatgpt-search, shopping, merchant-discovery]
source_type: official-company-material
extraction_mode: progressive
source_title: OpenAI official shopping, merchant discovery, search, and allowlisting guidance
source_date: 2025-2026
source_author: OpenAI
raw_path: ../../raw/strategy/geo/2026-04-19/official-pages/openai-shopping-docs-web-capture.md
verification_status: spot-checked
related:
  - ../syntheses/geo-research-landscape.md
  - ../source-summaries/geo-platform-guidance-2025-2026.md
  - ../../raw/strategy/geo/2026-04-19/raw-capture-log.md
---

# 来源摘要｜OpenAI 官方购物文档（2025-2026）

## Why this source matters
这组材料把 `ChatGPT shopping / search / merchant discoverability` 从“存在相关页面”推进到了更明确的一手事实层。

它说明 OpenAI 现在公开谈的已经不只是：
- 能不能被爬

而是同时包括：
- 商品 feed
- merchant ranking
- shopping discovery
- signed-agent allowlisting

## Extracted facts / observations
### Merchant discovery is partly a feed problem
- OpenAI merchant page明确说 merchants 可以分享 product feeds，让商品在 ChatGPT discovery moments 中出现得更完整、更准确。
- 官方列出的直接收益包括：
  - 更大 catalog coverage
  - 更丰富 product details
  - 更准确的 result placement
  - 更及时的 price / availability 更新
- 官方还明确说：
  - shopping in ChatGPT 当前 live in the U.S.
  - Shopify / Etsy catalogs 已经集成
  - ACP 是当前 product discovery 的基础连接层

### Product surfacing is explicitly metadata-driven
- `Shopping with ChatGPT Search` 页面明确说：
  - product results are selected independently by ChatGPT and are not ads
  - surfaced products depend on user intent and context
- 页面明确列出 ChatGPT 会考虑：
  - structured metadata from first-party and third-party providers
  - model responses generated before new search results are considered
  - safety standards and product policies
- 这意味着对 merchant 来说，`metadata quality` 不是边缘问题，而是官方明说的输入面。

### Merchant ranking factors are already stated at a high level
- OpenAI help 明确说 merchant list ranking 会看：
  - availability
  - price
  - quality
  - whether the merchant is the maker or primary seller
  - whether Instant Checkout is enabled
- 官方还明确说 merchant ranking 未来可能继续向 user preference personalization 演进。

### OpenAI may rewrite search queries
- `ChatGPT search` 页面明确说 ChatGPT search 可能把用户提示改写成一个或多个更具体的查询，再发送给搜索合作方。
- 这与 Google 官方的 `query fan-out` 有结构相似性，说明“用户原 query”和“系统内部执行 query”不应被视为同一件事。

### Inclusion still depends on crawl / allow
- OpenAI help 明确说没有办法保证 top placement。
- 但 inclusion 至少要求：
  - 不阻拦 `OAI-SearchBot`
  - host / CDN 允许 OpenAI published IPs
- `Shopping research` 页面还明确说 merchants 可以走 allowlisting 流程，以确保商品可在 shopping research 结果中出现。

### Shopping research is presented as organic, cited, and multi-source
- OpenAI help 明确说 shopping research 可能使用：
  - merchant product data via ACP
  - publicly available product information
  - other relevant retail sources
- 官方还明确写到：
  - results are organic
  - reads product pages directly
  - cites sources
  - avoids low-quality or spammy sites

### Signed-agent traffic is an operational reality
- `ChatGPT agent allowlisting` 页面明确说 agent 会对 outbound HTTP requests 进行签名。
- 官方给出 Akamai、Cloudflare、HUMAN、Vercel 的 allowlisting 做法。
- 对运维层的含义是：
  - merchant visibility 不是纯内容问题
  - 也是 CDN / firewall / bot policy 问题

## What this source supports
- 对 `commerce GEO` 的更稳妥定义应该包括：
  - crawlability
  - allowlisting
  - structured product data
  - feed participation
  - merchant-level ranking inputs
- “AI shopping optimization” 不只是写文案，更是数据分发和可接入性问题。

## What this source does not support
- 不支持断言 OpenAI 的 merchant ranking 已经稳定。
- 不支持反推出精确 ranking weights。
- 不支持把 feed access 等同于 guaranteed visibility。

## Caveats / ambiguity
- 官方文档是高层 guidance，不是 ranking spec。
- 本地直抓正文仍常被 Cloudflare challenge 拦截，因此 raw 以 capture note 形式保存，而不是完整正文副本。
- 这些页面更新频率可能较高，应持续复核。

## Sources
- https://openai.com/chatgpt/search-product-discovery/
- https://help.openai.com/en/articles/11128490-shopping-with-chatgpt-search
- https://help.openai.com/en/articles/12911370-using-shopping-research-in-chatgpt
- https://help.openai.com/en/articles/9237897-chatgpt-search
- https://help.openai.com/en/articles/11845367-chatgpt-agent-allowlisting
- `raw/strategy/geo/2026-04-19/official-pages/openai-shopping-docs-web-capture.md`
