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
domains: [kes, geo, evidence, governance, ai-search]
source_count: 6
review_cycle: monthly
verification_status: spot-checked
related:
  - ./geo-research-landscape.md
  - ./geo-noise-and-hype-map.md
  - ./geo-tactics-taxonomy.md
  - ./kes-geo-experiment-backlog.md
---

# KES GEO Evidence Scoring Rubric

## What this page is for
这页用来给任何 GEO / AEO / AI-search 说法打分。

目标是避免以下情况：
- 某篇营销文章被当研究
- 某个 case study 数字被当作通用事实
- 某个 tactic 因为听起来合理就直接变成 KES 标准

## Scoring dimensions
每条说法按 8 个维度打分，每项 `0-3` 分。

总分范围：`0-24`

## Dimension 1｜Source Type
### 3
peer-reviewed paper / official platform documentation

### 2
arXiv / SSRN / official company technical blog / reproducible benchmark

### 1
vendor case study / agency article / expert opinion piece

### 0
anonymous post / unattributed claim / no-methodology marketing page

## Dimension 2｜Method Transparency
### 3
query set、evaluation、metrics、procedure 明确公开

### 2
部分公开，但仍有重要黑箱

### 1
只给高层描述，细节不完整

### 0
无可验证方法

## Dimension 3｜Measurement Quality
### 3
measurement 定义清晰，可复现，可区分 visibility / rerank / choice

### 2
measurement 基本清晰，但仍混合多个目标

### 1
只给模糊 “visibility score” / “AI presence”

### 0
无可解释 measurement

## Dimension 4｜Platform Specificity
### 3
明确指出是哪个平台 / 模型 /环境

### 2
有平台范围，但不完全明确

### 1
笼统写 “AI search” / “LLMs”

### 0
完全不清楚适用对象

## Dimension 5｜Transferability
### 3
明确讨论跨平台 / 跨查询 / 跨场景限制

### 2
有一定边界说明

### 1
边界说明很弱

### 0
把个案直接包装成通用规律

## Dimension 6｜Factual Safety
### 3
明确避免虚假、操纵、越界 claim

### 2
基本安全，但未充分讨论风险

### 1
存在鼓励夸张或过度承诺倾向

### 0
明显依赖误导、操纵或攻击性方法

## Dimension 7｜Commercial Bias
### 3
非销售导向，或利益关系披露充分

### 2
存在商业角色，但论证仍较克制

### 1
明显带服务导流

### 0
核心目的就是销售 GEO 服务 / 工具

## Dimension 8｜KES Relevance
### 3
直接可映射到 KES 的 content / commerce / governance 决策

### 2
间接有帮助

### 1
更多是行业背景

### 0
几乎不影响 KES 实操

## Score bands
### 20-24
`High-confidence input`

可进入：
- KES working assumptions
- experiment design
- synthesis pages

### 15-19
`Useful but bounded`

可进入：
- backlog hypotheses
- supporting context

但必须保留限制说明。

### 10-14
`Weak signal`

可进入：
- noise watchlist
- exploratory notes

不应直接驱动标准化动作。

### 0-9
`Do not operationalize`

最多记录，不作为决策依据。

## Statement classification
除总分外，每条 GEO 说法还要标 1 个 statement type：

- `fact`
- `inference`
- `hypothesis`
- `vendor claim`
- `marketing narrative`

## Required metadata for any GEO claim entered into KES
至少记录：
- statement
- source URL
- source type
- platform / model
- metric type
- evidence score
- statement type
- reviewer
- review date

## Fast scoring questions
面对任意一条 GEO 说法，先问：

1. 这是谁说的？
2. 它测量的是什么？
3. 在哪个平台？
4. 是 visibility、rerank 还是 actual choice？
5. 方法有没有公开？
6. 是否承认边界？
7. 是否存在卖服务动机？
8. 对 KES 有直接可执行价值吗？

## Example scoring
### Example A｜GEO 原论文
- Source Type: 3
- Method Transparency: 3
- Measurement Quality: 3
- Platform Specificity: 2
- Transferability: 2
- Factual Safety: 3
- Commercial Bias: 3
- KES Relevance: 3

Total: `22`
Classification: `High-confidence input`
Statement type: `fact / bounded inference`

### Example B｜某 agency 的 “visibility +340%” case study
- Source Type: 1
- Method Transparency: 1
- Measurement Quality: 1
- Platform Specificity: 1
- Transferability: 0
- Factual Safety: 2
- Commercial Bias: 0
- KES Relevance: 2

Total: `8`
Classification: `Do not operationalize`
Statement type: `vendor claim`

### Example C｜Google AI features 官方文档
- Source Type: 3
- Method Transparency: 2
- Measurement Quality: 2
- Platform Specificity: 3
- Transferability: 1
- Factual Safety: 3
- Commercial Bias: 3
- KES Relevance: 3

Total: `20`
Classification: `High-confidence input`
Statement type: `fact`

## KES decision rules
### Rule 1
低于 `15` 分的 GEO 说法，不进入标准化 playbook。

### Rule 2
`vendor claim` 默认不能直接升级为 `fact`。

### Rule 3
若一条说法高分，但只适用于单一平台，也只能进入 platform-specific notes。

### Rule 4
即使高分，只要 tactic 违反 claim discipline，也不能 operationalize。

## Recommended workflow
### Step 1
先做 statement extraction

### Step 2
按 8 维打分

### Step 3
标注 statement type

### Step 4
决定进入哪一层：
- synthesis
- backlog hypothesis
- noise map
- discard

## Sources
- [GEO 研究全景](./geo-research-landscape.md)
- [GEO 噪音与营销包装地图](./geo-noise-and-hype-map.md)
- [GEO Tactics Taxonomy](./geo-tactics-taxonomy.md)
- [KES GEO Experiment Backlog](./kes-geo-experiment-backlog.md)
