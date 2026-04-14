---
type: source-summary
status: draft
owner: strategy
created: 2026-04-12
updated: 2026-04-14
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, academic-search, patents, api-fetch]
source_type: api-fetch
extraction_mode: direct-api
review_cycle: monthly
verification_status: spot-checked
related:
  - ../products/bathtub-filter.md
  - ../products/bathtub-filter-patent-table.md
  - ../syntheses/bathtub-filter-patent-and-technical-landscape.md
  - ../playbooks/academic-search-workflow.md
---

# 来源摘要｜Bathtub Filter 基于 API 的学术与专利抓取（2026-04-12）

## Obsidian links
- [[bathtub-filter]]
- [[bathtub-filter-patent-table]]
- [[bathtub-filter-patent-and-technical-landscape]]
- [[academic-search-workflow]]

## 这份来源为什么重要
这份来源把 bathtub-filter 主题从“手工浏览 / 仅搜索式研究”升级为“可重复的 API-backed retrieval + 直接专利页抓取”。

它证明，这个主题现在可以由一层轻量 research tooling 支撑，而不再只能依赖 ad hoc 搜索。

## 实际使用的 academic stack
- OpenAlex API
- Crossref API
- Europe PMC API

## 实际使用的 patent retrieval
- 对已知 patent ID 直接抓取公开 Google Patents 页面

## Important tooling note
曾尝试直接调用 PatentsView 风格的 patent API，但 legacy endpoint 现在返回迁移提示，因为 PatentsView 正在迁入 USPTO Open Data Portal。

所以当前可行状态是：
- academic APIs 已可直接使用并完成整合
- patent detail fetching 目前通过 Google Patents 页面抓取来实现
- 如果未来出现稳定的新 patent-search endpoint，应重新评估 USPTO / PatentsView 迁移后的接入方式

## 通过 API 确认的高价值 academic results
### 已确认的 targeted PMID lookups
- PMID 12692355：关于 bathing water 中 chlorine / atopic skin 的论文，已确认 DOI metadata
- PMID 22591883：2012 年 infant swimming / hard water / atopy 论文，已确认 DOI metadata，但返回 metadata 中仍为 non-OA
- PMID 27241890：关于 early-life water hardness/chlorine / AD 的研究，已确认 DOI metadata
- PMID 33259122：systematic review / meta-analysis，已确认 DOI metadata
- PMID 37029288：swimming / AD review，已确认 PMCID `PMC10946598`，OA = yes，且 Europe PMC fullTextXML 可用

### Strategic academic implication
academic API 层已经适合用于：
- DOI / PMID / PMCID 规范化
- OA 状态检查
- manuscript / full-text 获取机会检查
- 围绕 hard water / chlorine / swimming / eczema 做相关论文扩展

## 通过 direct fetch 确认的高价值 patent results
### 最强的 direct category hit
- `US6145670A` — *Bathtub spout with removable filter*
  - 直接对应 bathtub-spout 架构
  - 与 tub-fill 兼容性及 removable filter housing 逻辑高度相关

### 最强的 shower / tub crossover hits
- `US6096197A` — *Shower filter for chlorine removal and scale deposit prevention*
- `US6267887B1` — *Shower filter for chlorine removal and scale deposit prevention*
  - 强烈表明 bathtub-filter 架构与 shower/tub 双用途 cartridge 逻辑存在重叠

### 最强的 alternative dechlorination route hit
- `US7682513B2` — *Water dechlorination means*
  - 值得注意，因为抽样 claims 明确指向 water-soluble dechlorination media，并提到 ascorbic acid

### 最强的 immersion-style bath treatment hit
- `JP3002925U` — *Chlorine remover for bath water*
  - 强信号表明，品类地图里不仅应包含 inline filter units，也应包含 immersion dechlorination accessories

## Strategic implication
该研究底座现在已经有一层真实可用的 tooling 支撑。

这意味着未来的 bathtub-filter 工作可以在三个方面更系统化：
1. academic verification 可以重复执行，而不是每次都手工重搜
2. patent detail capture 可以标准化成可比较的行记录
3. topic expansion 可以基于 API-backed evidence，而不只依赖网页 snippets

## 本次运行产出的文件
- `tools/bathtub_filter_api_fetch.py`
- `data/products/bathtub-filter/api-fetch/2026-04-12-academic.json`
- `data/products/bathtub-filter/api-fetch/2026-04-12-academic.md`
- `data/products/bathtub-filter/api-fetch/2026-04-12-patents.json`
- `data/products/bathtub-filter/api-fetch/2026-04-12-patents.md`

## Sources
- `raw/products/bathtub-filter/2026-04-12-academic-search-and-patent-scouting.md`
- `data/products/bathtub-filter/api-fetch/2026-04-12-academic.json`
- `data/products/bathtub-filter/api-fetch/2026-04-12-patents.json`
