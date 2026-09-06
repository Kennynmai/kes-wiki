---
type: product
status: draft
owner: strategy
created: 2026-04-13
updated: 2026-09-06
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, test-gating, checklist]
source_count: 9
review_cycle: monthly
verification_status: working
related:
  - ./bathtub-filter-kes-go-no-go-memo-v1.md
  - ./bathtub-filter-kes-route-elimination-memo-v1.md
  - ./bathtub-filter-kes-next-step-execution-plan-v1.md
  - ./bathtub-filter-normal-flow-vs-reduced-flow-evidence-table.md
  - ./bathtub-filter-certification-and-testing-pathways.md
  - ./bathtub-filter-certification-authority-tiers-and-workflow.md
  - ../../playbooks/bathtub-filter-validation-testing-protocol.md
---

# 浴缸过滤器测试闸门清单

> **2026-09-06 状态更新（V1 定义锁定后）**：本页写于 diligence 阶段，正文保留为历史判断。2026-07-02 之后的权威事实见 [[bathtub-filter]]「V1 真理源」表：专利申请 19/281,644（patent pending）、27 项 BOM 裁定（KDF55 130 g / CaSO₃ 110 g / PET）、53 页 site/ 内容体系、氯胺版与井水版 GO、不做软化、PFAS 禁写。2026-09-05 全链路审查（[[bathtub-filter-v1-full-chain-critical-review-2026-09-05]]）把剩余卡点收敛为：Gate 1 第三方 DPD（[[bathtub-filter-25lpm-dechlorination-bench-test-spec]]）、KDF 仓装填（D-10）、V1 溢流复测、试纸量程（D-11）、refill 形态（D-09）、订阅 LTV 重跑（D-12）、COGS。
>
> **Gate 与新登记测试项的映射（2026-09-06）**：
>
> | Gate | 对应 spec / protocol 项 | 状态 |
> |---|---|---|
> | Gate 1 normal-flow proof | 25lpm spec §2.1 主矩阵（V1 配置）+ §2.5 KDF 仓装填复核 | spec 已按 BOM 更正，未送测 |
> | Gate 2 fit realism | supported-spout-matrix S-01～S-08；protocol Module 2 | partial-sample validated |
> | Gate 3 leak / overflow / stability | protocol Module 3：V1 溢流复测、KDF 床层位移、**动态挂重**（新增）、在位滴干霉变 | 全部待做 |
> | Gate 4 complaint-pattern survivability | 2562 条标签分析已给排序；维护指令已改两级 | 评论侧 ✅ / 维护口径 🟡 待 Module 4 |
> | Gate 5 refill economics | GTM §4.2 按寿命分档；D-09 refill 形态；D-12 LTV 重跑 | 口径 ✅ / 数字 🟡 |
> | Gate 6 claim discipline | register + 2026-09-05 增补；三条故事逐句护栏 | ✅ |
> | Gate 7 certification route | NSF 42+61 / WQA 路径已定；RFQ 未发 | 🟡 |

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
- a minimum spout taxonomy (at least diverter / non-diverter, slip-fit / threaded, straight / curved, short / decorative)
- no reliance on vague “fits all tubs” language

### Fail if
- fit scope is unclear
- fit success depends on hidden geometry conditions
- product depends on ad-hoc workaround behavior
- slip / attachment instability is common or unresolved

## Gate 3 — leak / overflow / stability control
### Must have
- no recurring leak or overflow issue in repeated use
- stable attachment through repeated fill cycles
- clear user setup logic
- separate validation for bypass flow, top overflow, seam/housing leak, and retention failure

### Fail if
- overflow is easy to trigger
- product shifts, slips, or leaks too easily
- stable use requires awkward faucet tuning
- the team cannot tell which leak class is actually happening

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
- route can be paired with a realistic target water-profile / geography story

### Fail if
- route only works as hype, not as a disciplined product story
- route is too generic or too legally fragile
- route only converts in chloramine / hard-water anxiety markets that the product cannot honestly address

## Gate 9 — water-jurisdiction fit
### Must have
- a declared target demand map: chlorine-led, chloramine-led, hard-water-led, or dual-trigger market
- claim scope that matches the actual strongest defensible water story
- no hidden dependence on local water conditions the route cannot actually handle

### Fail if
- route relies on a free-chlorine proof set but is implicitly targeting chloramine-heavy markets
- route relies on hard-water demand but cannot honestly avoid softening overclaim
- target-market logic is vague or contradictory

## Current default KES rule
A bathtub-filter route should not move forward unless it can satisfy all of the following:
1. normal-flow proof
2. fit realism
3. leak/overflow stability
4. survivable complaint pattern
5. acceptable refill burden
6. disciplined claim boundary
7. clear certification / evidence route
8. KES route fit
9. water-jurisdiction fit

## 建议新增内部 deliverables（立项前必须齐）
- **claim-evidence register**：每条 claim 对应一条证据卡
- **authority map**：NSF / WQA / IAPMO / lab / supplier 各自扮演什么角色
- **copy red-lines**：客服、包装、Amazon A+、FAQ 禁止出现的词
- **SKU boundary note**：bathtub SKU 与 future shower SKU 不能互借的 authority list
- **spout-fit matrix**：supported / unsupported tub-spout taxonomy + photo examples
- **leak taxonomy log**：bypass / overflow / seam leak / retention failure 分开记录
- **water-profile screen**：目标市场属于 chlorine-led、chloramine-led、hard-water-led 还是 dual-trigger

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
- [[bathtub-filter-compatibility-engineering-breakpoints]]
- [[bathtub-filter-water-jurisdiction-demand-map]]
- [[bathtub-filter-validation-testing-protocol]]
- [[bathtub-filter-certification-and-testing-pathways]]

## Sources
- [[bathtub-filter-kes-go-no-go-memo-v1]]
- [[bathtub-filter-kes-route-elimination-memo-v1]]
- [[bathtub-filter-normal-flow-vs-reduced-flow-evidence-table]]
- [[bathtub-filter-compatibility-engineering-breakpoints]]
- [[bathtub-filter-water-jurisdiction-demand-map]]
- [[bathtub-filter-validation-testing-protocol]]
- [[bathtub-filter-certification-and-testing-pathways]]
