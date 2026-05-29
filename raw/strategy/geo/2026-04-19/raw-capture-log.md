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
domains: [geo, aeo, ai-search, search, generative-ai]
source_type: mixed-source-capture
extraction_mode: direct-fetch
verification_status: spot-checked
---

# Raw Capture Log｜GEO Research Expansion｜2026-04-19

## Purpose
保存本轮针对 GEO / AEO / AI-search visibility 的扩展研究原始材料。

## Captured files
### Papers
- `../amazon/rufus-cosmo/2026-04-19/external-papers/geo-kdd-2024-arxiv-2311.09735.pdf`
- `../amazon/rufus-cosmo/2026-04-19/external-papers/geo-kdd-2024-arxiv-2311.09735.txt`
- `../amazon/rufus-cosmo/2026-04-19/papers/e-geo-arxiv-2511.20867.pdf`
- `../amazon/rufus-cosmo/2026-04-19/papers/e-geo-arxiv-2511.20867.txt`
- `../amazon/rufus-cosmo/2026-04-19/external-papers/agentic-ecommerce-aces-arxiv-2508.02630.pdf`
- `../amazon/rufus-cosmo/2026-04-19/external-papers/agentic-ecommerce-aces-arxiv-2508.02630.txt`

### Official pages
- `official-pages/google-ai-features-and-your-website.html`
- `official-pages/google-product-structured-data.html`
- `official-pages/bing-data-nosnippet-ai-answers.html`
- `official-pages/openai-help-chatgpt-discover-products.html`
- `official-pages/openai-shopping-docs-web-capture.md`
- `official-pages/perplexity-premium-data-sources.html`

### Operational / ecosystem examples
- `ops-pages/shopify-aeo-for-ecommerce.html`
- `ops-pages/vercel-gptbot-edge-requests-thread.html`

## Source URLs
### Academic
- https://arxiv.org/pdf/2311.09735
- https://arxiv.org/pdf/2511.20867
- https://arxiv.org/pdf/2508.02630
- https://aclanthology.org/2024.emnlp-main.534/
- https://aclanthology.org/2024.emnlp-main.534.pdf

### Official platform / ecosystem
- https://developers.google.com/search/docs/appearance/ai-overviews
- https://developers.google.com/search/docs/appearance/structured-data/product
- https://blogs.bing.com/webmaster/October-2025/Bing-Introduces-Support-for-the-data-nosnippet-HTML-Attribute
- https://openai.com/chatgpt/search-product-discovery/
- https://help.openai.com/en/articles/11128490-shopping-with-chatgpt-search
- https://help.openai.com/en/articles/12911370-using-shopping-research-in-chatgpt
- https://help.openai.com/en/articles/9237897-chatgpt-search
- https://help.openai.com/en/articles/11845367-chatgpt-agent-allowlisting
- https://www.perplexity.ai/help-center/en/articles/12870803-premium-data-sources
- https://www.shopify.com/my/blog/aeo-for-ecommerce
- https://community.vercel.com/t/unexpected-spike-in-vercel-edge-requests-without-traffic-increase/33857

## Capture notes
- Google / Bing 官方文档可直接抓取。
- OpenAI 的 `openai.com` / `help.openai.com` 直抓在当前环境中仍常触发防护页，已保存响应体，但这些 HTML 不是可用正文。
- 同日通过网页正文访问可核对 OpenAI shopping / merchant / search / allowlisting 页面，关键信息已转存到 `official-pages/openai-shopping-docs-web-capture.md`。
- Perplexity 官方帮助页在当前环境仍主要停留在防护页 / 可见摘要层。
- 这轮 GEO 扩展研究包含四条线：
  - visibility optimization
  - platform merchant guidance
  - seller / agent strategic response
  - ranking manipulation / robustness risk
