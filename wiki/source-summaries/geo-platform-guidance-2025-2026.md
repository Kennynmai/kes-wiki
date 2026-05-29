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
domains: [geo, ai-search, google, bing, openai, perplexity]
source_type: official-company-material
extraction_mode: progressive
source_title: Official platform guidance relevant to GEO and AI search visibility
source_date: 2025-2026
source_author: Google; Microsoft Bing; OpenAI; Perplexity
raw_path: ../../raw/strategy/geo/2026-04-19/official-pages/google-ai-features-and-your-website.html
verification_status: spot-checked
related:
  - ../syntheses/geo-research-landscape.md
  - ./openai-shopping-official-docs-2025-2026.md
  - ../../raw/strategy/geo/2026-04-19/raw-capture-log.md
---

# 来源摘要｜GEO 平台官方 guidance（2025-2026）

## Why this source matters
GEO 相关讨论里最容易缺的一层是：平台自己到底怎么说。

这组材料的价值不在于提供完整“打法”，而在于给出平台允许、鼓励、或明示不必额外做的边界。

## Extracted facts / observations
### Google Search Central
- Google 官方明确说：
  - AI Overviews / AI Mode 没有额外 special optimization requirement
  - foundational SEO best practices remain relevant
- 但同一页面也明确披露：
  - AI features may use `query fan-out`
  - supporting links can be wider / more diverse than classic search
- Google 官方还强调：
  - page must be indexed and eligible with snippet
  - people-first content remains core
  - site owners can use `nosnippet` / `data-nosnippet` / `max-snippet` / `noindex` to control previews
- Product structured data 页面则表明：
  - Google explicitly values product details such as price, availability, ratings, shipping, return policy
  - merchant listings + structured data + Merchant Center feeds expand visibility surfaces

### Bing Webmaster
- Bing 官方 2025 年明确支持 `data-nosnippet`
- 并明确说：
  - 被标记内容仍可被发现和用于 ranking
  - 但不会出现在 Bing Search snippets 或 AI-generated answers
- 这说明 Bing 把 “discoverability” 与 “what can be previewed / quoted in AI answers” 分开处理

### OpenAI
- OpenAI 官方文档现在已可通过正文访问确认更具体的事实：
  - merchants can share product feeds to improve catalog coverage, richer product details, placement accuracy, and freshness
  - shopping in ChatGPT 当前 live in the U.S.
  - Shopify / Etsy catalogs 已经集成
- `Shopping with ChatGPT Search` 官方帮助页还明确说：
  - product results are selected independently and are not ads
  - ChatGPT 会考虑 first-party / third-party structured metadata
  - merchant ranking 会看 availability、price、quality、是否 maker / primary seller、是否启用 Instant Checkout
- `ChatGPT search` 页面明确说：
  - ChatGPT may rewrite a prompt into one or more targeted queries
  - there is no way to guarantee top placement
  - inclusion 至少要求允许 `OAI-SearchBot` 与相关 IP
- `Using shopping research in ChatGPT` 页面明确说：
  - shopping research may use ACP merchant data、public product information、other retail sources
  - results are organic
  - product pages may be read directly and cited
- `ChatGPT agent allowlisting` 页面则说明：
  - signed-agent traffic 已进入 Akamai / Cloudflare / HUMAN / Vercel 等基础设施层
  - merchant visibility 也是 bot policy / allowlisting 问题

### Perplexity
- 当前环境未能直接抓到 Perplexity help 正文
- 但官方帮助中心公开存在 `Premium data sources` 相关页面
- 可见摘要显示：
  - Perplexity 正在把 Wiley、PitchBook、Statista、CB Insights 等 premium data source 接入回答系统
- 即便抓取受限，也足以说明：
  - 一部分 AI answer engine 正在主动建设 “authoritative data partnerships”

## What this source supports
- 平台官方并不普遍支持“有一套 AI 特供作弊技巧”这种说法。
- 但平台确实在强调：
  - crawl / index / snippet eligibility
  - structure / machine readability
  - richer product attributes
  - feed participation and freshness
  - merchant metadata quality
  - allowlisting / bot access
  - preview controls
  - authoritative data integration

## What this source does not support
- 不支持把 schema / snippet control 等同于生成式流量必然提升。
- 不支持据此断言某个平台内部真实 ranking weight。

## Caveats / ambiguity
- Google / Bing 官方文档可直接核对。
- OpenAI 官方正文已可核对，但本地直抓仍常落到 Cloudflare challenge，因此 raw 以 capture note 形式补存。
- Perplexity 在当前环境仍偏抓取受限，因此相关判断仍应比 Google / Bing / OpenAI 更克制。

## Sources
- https://developers.google.com/search/docs/appearance/ai-overviews
- https://developers.google.com/search/docs/appearance/structured-data/product
- https://blogs.bing.com/webmaster/October-2025/Bing-Introduces-Support-for-the-data-nosnippet-HTML-Attribute
- https://openai.com/chatgpt/search-product-discovery/
- https://help.openai.com/en/articles/11128490-shopping-with-chatgpt-search
- https://help.openai.com/en/articles/12911370-using-shopping-research-in-chatgpt
- https://help.openai.com/en/articles/9237897-chatgpt-search
- https://help.openai.com/en/articles/11845367-chatgpt-agent-allowlisting
- https://www.perplexity.ai/help-center/en/articles/12870803-premium-data-sources
- `raw/strategy/geo/2026-04-19/official-pages/google-ai-features-and-your-website.html`
