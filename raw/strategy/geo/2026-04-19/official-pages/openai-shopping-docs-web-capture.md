---
type: source-capture
status: draft
owner: strategy
created: 2026-04-19
updated: 2026-04-19
visibility: team
confidence: medium
officiality: draft
domain: strategy
domains: [geo, ai-search, openai, chatgpt-search, shopping]
source_type: official-company-material
extraction_mode: web-open
verification_status: spot-checked
---

# Raw Capture Note｜OpenAI Shopping Docs｜2026-04-19

## Purpose
保存本轮通过官方网页正文可见内容确认的 OpenAI shopping / search / merchant guidance 关键信息。

## Access note
- 本地 `curl` 对 `openai.com` 与 `help.openai.com` 多个页面仍返回 Cloudflare challenge。
- 同日通过网页正文访问可读到这些官方页面的实际内容。
- 因此此文件不是 HTML 原文副本，而是对官方页面正文的 capture note，用于保留当日可核对的事实层。

## Official URLs checked
- https://openai.com/chatgpt/search-product-discovery/
- https://help.openai.com/en/articles/11128490-shopping-with-chatgpt-search
- https://help.openai.com/en/articles/12911370-using-shopping-research-in-chatgpt
- https://help.openai.com/en/articles/9237897-chatgpt-search
- https://help.openai.com/en/articles/11845367-chatgpt-agent-allowlisting

## Captured observations
### Merchant discovery / feed page
- OpenAI merchant page states that merchants can share product feeds so products show up more effectively in ChatGPT discovery moments.
- The page says feeds can improve:
  - catalog coverage
  - richer product details
  - placement accuracy
  - freshness of pricing / availability
- The page states shopping in ChatGPT is currently live in the U.S.
- The page states that if a merchant sells through Shopify or Etsy, the catalog is already integrated.
- The page frames ACP as the infrastructure for product discovery and more accurate, personalized recommendations.

### Shopping with ChatGPT Search
- OpenAI help says product results are selected independently by ChatGPT and are not ads.
- The article says surfaced products depend on query intent and user context.
- It explicitly says ChatGPT considers:
  - structured metadata from first-party and third-party providers
  - model responses generated before new search results are considered
  - OpenAI safety standards and product policies
- The article says ChatGPT may simplify product titles and descriptions.
- Merchant ranking factors listed in the article include:
  - availability
  - price
  - quality
  - whether the merchant is the maker or primary seller
  - whether Instant Checkout is enabled

### Shopping research
- OpenAI help says shopping research is a multi-step product discovery flow.
- It may use:
  - merchant product data through ACP
  - publicly available product information
  - other relevant retail sources
- The article says results are organic and based on public retail sites, reading product pages directly and citing sources.
- The article also says merchants can follow an allowlisting process to ensure they can appear in shopping research results.

### ChatGPT search
- OpenAI help says ChatGPT search may rewrite a user prompt into one or more targeted queries and send them to search partners.
- The article says there is no way to guarantee top placement.
- It explicitly states that inclusion depends in part on allowing `OAI-SearchBot` and ensuring the host or CDN allows traffic from published IPs.

### Agent allowlisting
- OpenAI help says ChatGPT agent signs outbound HTTP requests.
- The document provides allowlisting guidance for Akamai, Cloudflare, HUMAN, and Vercel.
- The article states Vercel has added ChatGPT Agent to its Verified Bot Directory and allows access by default.

## Interpretation boundary
- These notes confirm that OpenAI shopping visibility is not just a vague “AI may cite you” problem.
- OpenAI is explicitly operating at:
  - crawler access
  - feed ingestion
  - merchant metadata
  - merchant ranking
  - signed-agent allowlisting
- The notes do not reveal exact ranking weights or guarantee inclusion.
