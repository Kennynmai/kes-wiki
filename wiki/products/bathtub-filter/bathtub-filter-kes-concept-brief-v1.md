---
type: product
status: draft
owner: strategy
created: 2026-04-14
updated: 2026-04-17
visibility: team
confidence: high
officiality: draft
domain: product
domains: [bathtub-filter, kes, concept-brief, version-a]
source_count: 5
review_cycle: monthly
verification_status: spot-checked
related:
  - ./bathtub-filter-kes-route-elimination-memo-v1.md
  - ./bathtub-filter-test-gating-checklist-for-kes.md
  - ./bathtub-filter-kes-next-step-execution-plan-v1.md
  - ./bathtub-filter-product-definition-language.md
  - ./bathtub-filter-kes-product-architecture-hypotheses.md
  - ../../source-summaries/bathtub-filter-kes-internal-product-materials-2026-04-17.md
---

# Bathtub Filter KES Concept Brief — V1

## 📌 Status update 2026-04-17：Version A 已落地

**Candidate B（狭义氯聚焦、技术纪律路线）已经从 concept candidate 升级为 Version A 确认架构**（urban municipal tap water，38–42°C）。

详见：
- 产品架构：[[bathtub-filter-kes-product-architecture-hypotheses]]（原假设 → 确认 log）
- 技术数据：[[bathtub-filter-technology-notes]]（EBCT / KDF 系数）
- 寿命模型：[[bathtub-filter-media-efficacy-at-bath-conditions]] Section 9（2 ppm / 1 ppm 双档寿命表）
- 来源：[KES 内部产品材料 2026-04-17](../../source-summaries/bathtub-filter-kes-internal-product-materials-2026-04-17.md)

Version A 的核心 commit：
- **定位**：不是净水器，不以 TDS 为目标；是**浴缸注水场景的末端减害模块**
- **主 KPI**：新滤芯 · 最佳体验段 **系统总去氯 ≥99%**；寿命口径按累计水量 / 泡澡次数 / 周期（不用月数）
- **媒体栈**：PP fiber 盘 → optional 240 mL cavity → KDF55 110 g → CaSO₃ 130 g → PP mesh 盘；内置导流模块
- **Claim discipline**：无 eczema / broad-contaminant / universal-fit / baby-safe / clinical 类语言；第三方 finished-product 认证暂不声称
- **Compatibility**：TPU 可调 strap；no-overflow envelope 35 L/min（US 典型 18–25 L/min 有充足余量）

### Candidate A / C 的当前状态
- **Candidate A（premium-but-disciplined hybrid）**：Version A 已吸收其"视觉可信 + 性能证明"主张（可视化 filter disc + chlorine strip 赠品），**无需独立 A 产品线**
- **Candidate C（soft-hanging ritual）**：**作为 Version A 非路径**，留作未来 beauty / ritual segment 探索；Doc 2 竞品 teardown 确认布袋式霉变风险（B0742KFY9R 16 赞差评），进入此路线前需要防霉方案

### Version B / C 尚未启动
Version A 明确的 **非覆盖范围** 等待 Version B/C 处理：
- **氯胺城市**（US 约 35–40% 系统）— 需要催化活性炭 + 接触时间重新设计
- **Well water**（US 约 23M 户）— 需要 KDF-85 + 铁/锰/H₂S 路径，见 [[bathtub-filter-well-water-research]]
- **软水器下游用户**（14–22M 户）— 最被忽视细分；问题在于"软水器不去氯"
- **日式高温浸浴**（45°C+）— 未验证

---

## 以下为 V1 concept 候选的原始记录（保留作 trail）

## Why this page exists
This page converts the current research into early KES concept candidates.
It is not a launch recommendation.
It is a narrowing tool for what KES should concept-test next.

## Concept candidate A — Hybrid premium-but-disciplined tub-spout route
### Core idea
A visually refined tub-spout bath filter with a narrow chlorine/comfort-first promise, explicit fit scope, and proof centered on realistic bath-fill conditions.

### Why this candidate survives
- best balance of credibility and premium appeal
- avoids generic bath-ball sameness
- avoids eczema-forward overclaim trap
- can fit KES-adjacent bathroom hardware language better than pure wellness fluff

### Core claim zone
- chlorine-conscious bath-water comfort
- gentler bath experience
- realistic bath-use design

### Hard requirements
- normal-flow proof
- fit matrix clarity
- low leak / low overflow risk
- disciplined price-to-refill story

### Main risk
- if flow reality underwhelms, premium styling will not save the route

## Concept candidate B — Narrow chlorine-focused technically disciplined route
### Core idea
A more technical, less emotional route built around credible chlorine-reduction logic, realistic fit boundaries, and transparent testing language.

### Why this candidate survives
- strongest defensible proof territory surfaced so far
- easiest route to keep claims disciplined
- best fit if KES wants to be trusted before being aspirational

### Core claim zone
- chlorine reduction under stated conditions
- supported tub-spout formats
- replaceable filtration media

### Hard requirements
- precise test language
- no vague universal-fit marketing
- no broad contaminant fantasy stack

### Main risk
- can become too dry or too utility-looking if KES does not add enough product/brand appeal

## Concept candidate C — Soft-hanging ritual route (conditional)
### Core idea
A softer, more comfort-ritual oriented bath filter with a low-hardware look and a more wellness-friendly visual expression.

### Why only conditional
- route has some encouraging performance signal in the current research
- but maintenance burden, drying, and overflow/fill-speed frustration are real risks

### KES posture
- keep as a secondary exploration route, not the lead concept

## Market scope — V1 declaration

- **Primary target:** North America，free-chlorine 主导地区（CA、FL、TX、Southeast、Mountain West 的大部分区域）
- **V1 明确不覆盖：** chloramine 为主的市场（Northeast US 部分地区、Chicago metro）；以及主要水质挑战为硬水而非氯的地区
- **原因：** 三条候选路线的宣称核心是氯去除化学机制。Chloramine 需要不同的滤材；硬水结垢是独立问题。进入这些市场会将产品推入其宣称防守不了的水质环境。
- **复核时间点：** 在 normal-flow 测试结果确认滤材机制后，再复核是否拓展市场覆盖范围。

## Current non-candidates
### Do not prioritize
- commodity broad-claim bath-ball clone
- aggressive eczema / baby-outcome DTC route

## Best current concept order for KES
1. Hybrid premium-but-disciplined tub-spout route
2. Narrow chlorine-focused technically disciplined route
3. Soft-hanging ritual route (conditional backup)

## Concept brief summary
If KES explores bathtub filters further, the best current concept should probably feel like:
- a bathroom product, not a panic product
- performance-serious, not theatrically scientific
- premium, but not soft-medical
- explicit about fit and limits
- optimized for realistic use, not idealized demo conditions

## Obsidian links
- [[bathtub-filter]]
- [[bathtub-filter-kes-route-elimination-memo-v1]]
- [[bathtub-filter-kes-next-step-execution-plan-v1]]
- [[bathtub-filter-test-gating-checklist-for-kes]]
- [[bathtub-filter-product-definition-language]]
- [[bathtub-filter-kes-product-architecture-hypotheses]]
- [[bathtub-filter-normal-flow-vs-reduced-flow-evidence-table]]

## Sources
- [[bathtub-filter-kes-route-elimination-memo-v1]]
- [[bathtub-filter-test-gating-checklist-for-kes]]
- [[bathtub-filter-product-definition-language]]
- [[bathtub-filter-kes-product-architecture-hypotheses]]
