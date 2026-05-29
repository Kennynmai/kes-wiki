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
domains: [geo, generative-engine, content-visibility, search, ecommerce]
source_type: academic-paper
extraction_mode: abstract-plus-detailed-notes
source_title: GEO: Generative Engine Optimization
source_date: 2024
source_author: Pranjal Aggarwal et al.
raw_path: ../../raw/platforms/amazon/rufus-cosmo/2026-04-19/external-papers/geo-kdd-2024-arxiv-2311.09735.pdf
verification_status: spot-checked
related:
  - ../platforms/amazon-rufus-and-cosmo.md
  - ../syntheses/amazon-rufus-cosmo-e-geo-kes-response.md
  - ../../raw/platforms/amazon/rufus-cosmo/2026-04-19/raw-capture-log.md
---

# 来源摘要｜Aggarwal et al. 2024｜GEO 原论文

## Why this source matters
这是 `E-GEO` 之前更一般的一篇开创性论文。它定义了什么是 `Generative Engine Optimization`，并强调：
- generative engine 的 visibility 不是传统 SEO 排名的简单延伸
- citation / position / presentation style 会共同影响可见性

## Extracted facts / observations
- 论文把 generative engines 抽象为：
  - retrieve documents
  - use LLMs to generate attributed responses
- 它认为 content creator 面临的新问题是：
  - 被系统如何引用
  - 在生成式回答里出现多少
  - 出现在什么位置
- 论文提出一套比传统 SERP 排名更复杂的 visibility metrics，包括：
  - word count
  - position-adjusted word count
  - subjective impression
- 论文引入 GEO-bench，含 10K queries。
- 作者报告 GEO 方法可带来：
  - up to 40% visibility improvement
  - 在 Perplexity.ai 上最高约 37% 改善
- 论文还发现不同方法在不同 domain 上效果不同，强调 domain-specific optimization。
- 论文点名有效方法包括：
  - citations
  - quotations
  - statistics
  - fluency / easy-to-understand improvements

## How GEO is defined in the paper
论文中的 `GEO` 不是“让页面看起来更会卖货”的泛说法，而是一个更正式的定义：

- `GEO = content creators optimize website content to increase visibility in generative engine responses`
- 优化对象不是传统 SERP 排名，而是 generative response 里的 visibility / impression

作者强调 generative engine 和传统 search engine 的差别在于：
- 一个回答里可能交错引用多个来源
- 引用长度、位置、呈现方式都影响 visibility
- 因此不能只用传统排名来表示曝光

## How GEO measures visibility
论文提出三类核心 impression metrics：

### 1. Word Count
- 某来源被引用到的相关句子字数占比
- 直觉：引用越多、越长，来源在答案里越重要

### 2. Position-Adjusted Word Count
- 在字数基础上，对更靠前的引用给更高权重
- 直觉：越早出现，用户越可能读到

### 3. Subjective Impression
- 用 LLM-based evaluation 去综合评估：
  - relevance
  - influence
  - uniqueness
  - subjective position
  - subjective count
  - click probability
  - diversity

## What GEO methods the paper actually tests
论文不是只给概念，而是直接列了 9 类 content modifications：

1. `Authoritative`
2. `Statistics Addition`
3. `Keyword Stuffing`
4. `Cite Sources`
5. `Quotation Addition`
6. `Easy-to-Understand`
7. `Fluency Optimization`
8. `Unique Words`
9. `Technical Terms`

## What worked best in the paper
- Top performers：
  - `Cite Sources`
  - `Quotation Addition`
  - `Statistics Addition`
- 这些方法在 Position-Adjusted Word Count 上带来约 30%–40% relative improvement
- 在 Subjective Impression 上带来约 15%–30% improvement
- `Fluency Optimization` 和 `Easy-to-Understand` 也有 15%–30% 的可见性提升
- 传统 SEO 式 `Keyword Stuffing` 表现较差，甚至可能更差

## Combination effects
- 论文进一步测试 method combinations
- 结论之一是：
  - `Fluency Optimization + Statistics Addition` 的组合优于任何单一 GEO strategy
- 作者还指出：
  - `Cite Sources` 单独不一定最强
  - 但与其他方法组合时会明显抬升表现

## How to operationalize GEO from this paper
如果严格按论文精神转成执行，不是“多堆关键词”，而是：

### A. Make the content citable
- 补具体事实
- 补具体数字
- 补可归因来源

### B. Make the content easier to reuse in an answer
- 提高流畅度
- 提高可读性
- 让关键句更完整、更独立可引用

### C. Match query-intent better
- 不是粗暴 stuffing
- 而是让 query-relevant facts、terms、comparisons 更明显

### D. Combine structure + evidence
- 只改文风不够
- 只加数字也不够
- 论文更支持 evidence-rich + readable 的组合

## What the paper does not justify
- 不支持“关键词越多越好”
- 不支持“只要 authoritative tone 就能赢”
- 不支持把 GEO 直接等同于 Amazon 内部 in-store reranking
- 不支持脱离 factuality 做 manipulative rewriting

## What this source supports
- generative answer visibility 与传统 keyword ranking 不是同一个优化问题。
- 被引用的方式、位置和答案结构重要。
- “结构化、可引用、带证据的内容” 对生成式可见性更重要。

## What this source does not support
- 不支持把 GEO 原论文直接视为 Amazon / Rufus / COSMO 的真实内部机制。
- 不支持把 web citation optimization 与 Amazon in-store ranking 直接等同。

## Caveats / ambiguity
- 论文面向的是更广义 generative engines。
- 使用的实验引擎与 Amazon 线上 shopping stack 并不等同。
- 但它为理解 `E-GEO` 和 Amazon 时代的内容优化提供了上游框架。

## Sources
- https://arxiv.org/pdf/2311.09735
- `raw/platforms/amazon/rufus-cosmo/2026-04-19/external-papers/geo-kdd-2024-arxiv-2311.09735.pdf`
