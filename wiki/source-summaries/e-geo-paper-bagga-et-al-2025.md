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
domains: [geo, ecommerce, generative-ai, amazon, ranking]
source_type: academic-paper
extraction_mode: abstract-plus-detailed-notes
source_title: E-GEO: A Testbed for Generative Engine Optimization in E-Commerce
source_date: 2025-11-25
source_author: Puneet S. Bagga; Vivek F. Farias; Tamar Korkotashvili; Tianyi Peng; Yuhang Wu
raw_path: ../../raw/platforms/amazon/rufus-cosmo/2026-04-19/papers/e-geo-arxiv-2511.20867.pdf
verification_status: spot-checked
related:
  - ../platforms/amazon-rufus-and-cosmo.md
  - ../../raw/platforms/amazon/rufus-cosmo/2026-04-19/raw-capture-log.md
---

# 来源摘要｜Bagga et al. 2025｜E-GEO

## Why this source matters
这篇论文不是 Amazon 官方资料，但它给了一个很有价值的外部视角：如果购物入口逐步转向 generative engine / shopping assistant，商品内容被“生成式系统”重排的机制该如何被测量与优化。

## Extracted facts / observations
- 论文把电商 generative engine 抽象成 RAG 式流程：
  - retrieval
  - generative engine re-ranking / synthesis
- 它提出 E-GEO benchmark：
  - 7,000+ long-form Reddit product queries
  - paired with Amazon listings
- 论文评估了 15 种 heuristic rewriting strategies。
- 论文进一步把 GEO 形式化为 optimization problem，并提出 iterative prompt-optimization algorithm。
- 作者声称优化后的 prompt 显示出相对稳定、跨领域的 pattern，即所谓 “universally effective” GEO strategy。
- 开源仓库 README 说明项目包含：
  - `data/`
  - 15 个初始 prompts
  - prompt optimization loop
  - experiment runner
  - analysis / visualiser

## What this source supports
- “面向生成式购物入口的内容优化” 已经开始被学术化、可实验化。
- 传统 SEO / keyword stuffing 逻辑不足以解释 generative shopping visibility。
- 如果平台把 query 理解、重排和推荐更多交给生成式层，listing 文本结构、属性表达、约束表达会更重要。

## What this source does not support
- 不支持把 E-GEO 的实验结果直接当作 Rufus 或 COSMO 的真实线上排序逻辑。
- 不支持把 Amazon listings + 外部实验框架等同于 Amazon 官方推荐系统披露。
- 不支持宣称存在一套对 Amazon 真实线上系统已验证有效的通用 seller playbook。

## Caveats / ambiguity
- 这是 arXiv 预印本，不是 Amazon 官方研究。
- benchmark 使用 Amazon listings，但研究框架是外部团队构建。
- 它更适合作为 “外部压力测试 / 方法论参照”，而非 Amazon 内部架构证据。

## Related pages
- [Amazon Rufus and COSMO](../platforms/amazon-rufus-and-cosmo.md)

## Sources
- https://arxiv.org/pdf/2511.20867
- https://github.com/psbagga17/E-GEO
- `raw/platforms/amazon/rufus-cosmo/2026-04-19/papers/e-geo-arxiv-2511.20867.pdf`
- `raw/platforms/amazon/rufus-cosmo/2026-04-19/code/E-GEO-README.md`
