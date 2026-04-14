---
type: synthesis
status: draft
owner: strategy
created: 2026-04-12
updated: 2026-04-14
visibility: team
confidence: medium
officiality: draft
domain: strategy
domains: [bathtub-filter, patents, technical-landscape, product-architecture]
source_count: 5
review_cycle: monthly
verification_status: spot-checked
related:
  - ../products/bathtub-filter.md
  - ../syntheses/bathtub-filter-research-map.md
  - ../playbooks/academic-search-workflow.md
---

# 浴缸过滤器（Bathtub Filter）专利与技术版图

## Obsidian links
- [[bathtub-filter]]
- [[bathtub-filter-patent-table]]
- [[bathtub-filter-kes-product-architecture-hypotheses]]
- [[bathtub-filter-normal-flow-vs-reduced-flow-evidence-table]]
- [[bathtub-filter-complaint-taxonomy-and-risk-by-route]]
- [[academic-search-workflow]]

## 为什么会有这页
这页为 bathtub-filter 主题补上 patent / technical-route lens（专利 / 技术路径视角）。

学术证据（academic evidence base）可以解释用户为什么关心水质、skin comfort，或 baby-sensitive-skin use cases，但仅靠这些并不能回答：一个 bathtub-filter 产品在技术上是否可信、在结构上是否有差异化、以及是否被 prior art（现有技术）挤满。

## 核心结论（Main takeaway）
这个品类现在看起来已经有一条真实的 **technical-route research branch（技术路径研究支线）**，而不只是 market-story branch（市场叙事支线）。

早期专利信号显示，bathtub-filter 的开发至少与四类 engineering / IP zones（工程 / 知识产权区域）重叠：
1. bathtub-spout / tub-faucet attached inline filters
2. dual-purpose shower / tub cartridge systems
3. immersion dechlorination accessories
4. 更广义的 bath-water treatment / recirculation / sanitization systems

这很重要，因为商业上的品类表面看似简单，实际上可能继承了 shower filters、faucet filters 与 bath-treatment devices 的技术与 IP 包袱。

## 早期专利簇（Early patent clusters）
### 1. Bathtub-spout / tub-faucet attached inline filter
代表性信号：
- **US6145670A — Bathtub spout with removable filter**

为什么重要：
- 这是 bathtub-specific faucet / spout filtration 作为独立 use case 被申请专利的直接证据
- 对 compatibility、housing geometry、user installation simplicity，以及 chlorine / odor / sediment 相关 claims 都有参考意义

### 2. Shower / tub dual-purpose chlorine + scale systems
代表性信号：
- **US6096197A — Shower filter for chlorine removal and scale deposit prevention**
- **US6267887B1 — Shower filter for chlorine removal and scale deposit prevention**

为什么重要：
- 这说明许多 bathtub-filter 概念在技术上可能更像 shower-filter 的“表亲”，而不是完全独立的产品架构
- 也指向一种常见模式：在可更换 cartridges 中组合 chlorine-reduction media 与 scale-related media
- 进一步提示 “bathtub filter” 可能部分是 reapplication / packaging problem（重新应用 / 包装问题），而不是净新增的 core technology problem（核心技术问题）

### 3. Immersion dechlorination accessory
代表性信号：
- **JP3002925U — Chlorine remover for bath water**

为什么重要：
- 它揭示了另一条路线：产品不一定是 inline filtration，也可能是浸泡式的 dechlorination accessory，通过 consumable medium（消耗性介质）来处理水
- 从战略上看很重要，因为许多 consumer bath products 可能会模糊 filter、treatment accessory、以及 additive-like device 之间的界线

### 4. Broad dechlorination-media device
代表性信号：
- **US7682513B2 — Water dechlorination means**

为什么重要：
- 它表明 dechlorination 可以围绕 soluble media transfer（可溶介质转移）与 controlled water contact（受控接触）来构建，而不只是固定滤芯的 flow-through system
- 对理解 classic faucet-mounted housings 之外的替代架构与 claim language 很有帮助

### 5. Point-of-use softening / chlorine-reduction adjacency
代表性信号：
- **FR2480822A1 — Ion exchange resin water softener for shower bath sprays**

为什么重要：
- 它为 softening 与 chlorine reduction 混合宣称的 claim spaces（宣称空间）提供背景信号
- 也提醒我们，“hard water softener” 语言对应的是与单纯 chlorine reduction 不同的技术负担

## 这对产品现实意味着什么
### KES 应该关心的工程问题
- faucet / tub-spout compatibility across installations
- 对 tub fill 时 pressure / flow-rate 的影响
- leakage risk 与 connection stability
- 产品到底更像 true filtration，还是 treatment media contact
- cartridge replacement logic 与 economics
- “softening” 是否真实可实现，还是更多只是 marketing shorthand

### KES 应该关心的宣称问题
- chlorine reduction 在技术上可能比 broad contaminant-removal storytelling 更可信
- chloramine、fluoride、heavy metals、hard-water claims 在技术可信度上可能差异极大
- softening 语言尤其需要纪律，因为很多小型 point-of-use devices 在 bathtub-fill 场景中，未必能提供临床或技术上有意义的软化效果

## 战略解读
专利层让我们更有把握地支持一个结论：

> bathtub filter 应该被研究为一个混合主题：既是 category research，也是 technical architecture research，同时还是 claim-discipline research。

它不应只被当成一个 keyword-demand question（关键词需求问题）。

## 已经直接抓取到的专利信号
这个主题现在不再只停留在 search snippets。当前 seed set 已经通过公开 patent pages 直接抓取了 title / date / description / claim samples。

示例：
- `US6145670A` 确认了直接的 bathtub-spout removable-filter architecture
- `US6096197A` / `US6267887B1` 确认了强烈的 shower / tub crossover architecture 与 cartridge logic
- `US7682513B2` 确认了一条 dechlorination 路径，且抽样 claims 明确提到 water-soluble media 与 ascorbic-acid relevance
- `JP3002925U` 确认了 immersion-style bath-water chlorine-removal route

这让 route taxonomy（路径分类）比之前更可信，也更少依赖猜测。

## 仍然缺什么
这页目前仍是一张 early map，而不是完整的 patent landscape。

缺失工作包括：
- 按 assignee 聚类 patent families
- 绘制 filing dates 与可能 expiry windows
- 把 consumer-relevant patents 与 spa / whirlpool / medical bath treatment patents 区分开
- 检查当前 Amazon / DTC 产品是否像是旧 shower / tub prior art 的衍生路线
- 将 patent clusters 与当前 product-form hypotheses 关联起来

## 建议下一步
- 建一个 patent table，字段包括：patent number / family / assignee / route type / likely relevance / notes
- 将 patent route clusters 与当前 marketplace product forms 对照
- 判断当前品类领导者在 signal 上强调的是 patented media，还是只是 patented branding / packaging
- 如果这个品类进一步变得严肃，再补一页轻量版 FTO-risk heuristic

## Sources
- `raw/products/bathtub-filter/2026-04-12-academic-search-and-patent-scouting.md`
- `https://patents.google.com/patent/US6145670`
- `https://patents.google.com/patent/US6096197`
- `https://patents.google.com/patent/US6267887B1/en`
- `https://patents.google.com/patent/US7682513`
- `https://patents.google.com/patent/JP3002925U/en`
- `https://patents.google.com/patent/FR2480822A1/en`
