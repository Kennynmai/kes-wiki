---
type: product
status: draft
owner: strategy
created: 2026-04-13
updated: 2026-04-14
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, test-gating, checklist]
source_count: 7
review_cycle: monthly
verification_status: working
related:
  - ./bathtub-filter-kes-go-no-go-memo-v1.md
  - ./bathtub-filter-kes-route-elimination-memo-v1.md
  - ./bathtub-filter-kes-next-step-execution-plan-v1.md
  - ./bathtub-filter-normal-flow-vs-reduced-flow-evidence-table.md
  - ./bathtub-filter-certification-and-testing-pathways.md
  - ./bathtub-filter-certification-authority-tiers-and-workflow.md
  - ../playbooks/bathtub-filter-validation-testing-protocol.md
---

# Bathtub Filter Test-Gating Checklist for KES

## Why this page exists
This page turns the research into a practical gate.
If a route cannot pass these checks, KES should not treat it as a serious product candidate.

## Gate 1 — normal-flow proof
### Must have
- evidence under realistic tub-fill flow, not only slowed flow
- explicit fill-time data
- repeated measurements, not one lucky run

### Fail if
- performance only looks good at impractically slow flow
- the tub takes too long to fill for normal family use

## Gate 2 — fit realism
### Must have
- defined supported tub-spout types
- defined unsupported tub-spout types
- no reliance on vague “fits all tubs” language

### Fail if
- fit scope is unclear
- product depends on ad-hoc workaround behavior
- slip / attachment instability is common or unresolved

## Gate 3 — leak / overflow / stability control
### Must have
- no recurring leak or overflow issue in repeated use
- stable attachment through repeated fill cycles
- clear user setup logic

### Fail if
- overflow is easy to trigger
- product shifts, slips, or leaks too easily
- stable use requires awkward faucet tuning

## Gate 4 — complaint-pattern survivability
### Must have
- complaint profile that seems survivable at scale
- no obvious route-level mismatch between promise and lived use

### Fail if
- the route’s natural complaint class is too severe
- likely 1-star patterns are structural rather than fixable

## Gate 5 — refill economics
### Must have
- annual replacement burden that feels tolerable
- maintenance routine that users can realistically sustain

### Fail if
- refill cadence is too frequent for perceived value
- maintenance burden is likely to create drop-off or regret

## Gate 6 — claim discipline
### Must have
- chlorine/comfort-first language if that is the strongest proof zone
- strict separation between educational context and product proof

### Fail if
- route depends on eczema-improvement, baby-safety, heavy-metal fantasy stack, or broad medical implication to convert

## Gate 7 — certification / evidence route clarity
### Must have
- clear decision on whether the route is pursuing **official certification**, **third-party testing**, or only **materials / component compliance**
- no mixing of `certified`, `tested`, and `uses certified media`
- no external borrowing of shower-standard authority onto bathtub claims without boundary language
- for every authority signal, a one-line evidence card with:
  - issuer
  - object
  - scope
  - proof

### Fail if
- route depends on certification-adjacent wording to create trust
- route cannot explain exactly what is product-certified vs media-level vs internally tested
- route needs EPA / medical / vague lab language to feel credible
- sales / packaging / Amazon copy are likely to widen the claim beyond the evidence card

## Gate 8 — KES route fit
### Must have
- route is compatible with KES brand discipline
- route can be explained clearly without overclaiming
- route looks differentiated enough from generic marketplace clones

### Fail if
- route only works as hype, not as a disciplined product story
- route is too generic or too legally fragile

## Current default KES rule
A bathtub-filter route should not move forward unless it can satisfy all of the following:
1. normal-flow proof
2. fit realism
3. leak/overflow stability
4. survivable complaint pattern
5. acceptable refill burden
6. disciplined claim boundary
7. clear certification / evidence route

## 建议新增内部 deliverables（立项前必须齐）
- **claim-evidence register**：每条 claim 对应一条证据卡
- **authority map**：NSF / WQA / IAPMO / lab / supplier 各自扮演什么角色
- **copy red-lines**：客服、包装、Amazon A+、FAQ 禁止出现的词
- **SKU boundary note**：bathtub SKU 与 future shower SKU 不能互借的 authority list

## Best current survivors
Based on current research, the strongest survivors are still:
- [[bathtub-filter-kes-route-elimination-memo-v1|hybrid premium-but-disciplined route]]
- [[bathtub-filter-kes-route-elimination-memo-v1|narrow chlorine-focused / technically disciplined route]]

## Obsidian links
- [[bathtub-filter]]
- [[bathtub-filter-kes-go-no-go-memo-v1]]
- [[bathtub-filter-kes-route-elimination-memo-v1]]
- [[bathtub-filter-kes-concept-brief-v1]]
- [[bathtub-filter-kes-next-step-execution-plan-v1]]
- [[bathtub-filter-normal-flow-vs-reduced-flow-evidence-table]]
- [[bathtub-filter-complaint-taxonomy-and-risk-by-route]]
- [[bathtub-filter-validation-testing-protocol]]
- [[bathtub-filter-certification-and-testing-pathways]]

## Sources
- [[bathtub-filter-kes-go-no-go-memo-v1]]
- [[bathtub-filter-kes-route-elimination-memo-v1]]
- [[bathtub-filter-normal-flow-vs-reduced-flow-evidence-table]]
- [[bathtub-filter-validation-testing-protocol]]
- [[bathtub-filter-certification-and-testing-pathways]]
