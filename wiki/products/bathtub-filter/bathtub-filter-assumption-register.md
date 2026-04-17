---
type: product
status: draft
owner: strategy
created: 2026-04-17
updated: 2026-04-17
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, assumptions, hypotheses]
source_count: 6
review_cycle: monthly
verification_status: working
related:
  - ./bathtub-filter.md
  - ./bathtub-filter-kes-concept-brief-v1.md
  - ./bathtub-filter-kes-go-no-go-memo-v1.md
---

# Bathtub Filter KES — Assumption & Hypothesis Register

## Why this page exists

这页把散落在整个 research cluster 各处的**隐含假设**集中到一个地方。

每一条假设都经过某些 memo 或分析页面的"使用"——有时是显式讲出来的，有时是嵌入到判断逻辑里、没有单独拆出来验证的。把它们显式化的目的，是让这些假设可以被挑战、被更新、被单独追踪，而不是默默影响路线决策却无人负责审核。

**使用说明：** 每次有新的测试结果、竞品样品观察、或 go/no-go memo 更新时，应同步回来复核相关假设。证据等级从 strong / weak / logic-only 三档评估，不是好坏之分，而是说明当前支撑这条假设的基础性质。

---

## Assumption table

| # | Assumption | Source page(s) | Evidence backing | Sensitivity if wrong |
|---|---|---|---|---|
| A-01 | Normal-flow performance is technically achievable — i.e., a compact tub-spout filter can deliver meaningful chlorine reduction at realistic tub-fill flow rates, not only under reduced/controlled conditions | go-no-go-memo-v1, compatibility-engineering-breakpoints | weak — flagged as unverified, the most critical open question | Route-breaking. If performance is only credible at reduced flow, the entire hybrid-premium-but-disciplined route loses its claim foundation. |
| A-02 | North America (free-chlorine-dominant markets: CA, FL, TX, Southeast, Mountain West) is the correct V1 primary target, and chloramine-heavy or hard-water-dominant markets can be deferred | kes-concept-brief-v1, go-no-go-memo-v1 | logic-only — based on claim defensibility logic, not validated demand signal | Moderate. If primary demand in target geo turns out to be chloramine or hard-water driven, the narrower chlorine story may not convert. |
| A-03 | Free-chlorine claim is the most defensible claim category currently available, and can anchor a premium positioning without requiring eczema or clinical language | go-no-go-memo-v1, kes-route-screening-memo-v2, claim-risk-audit-v2 | weak-to-medium — supported by NSF-177 shower-filter lineage and review signal, but not yet validated for tub-specific conditions | High. If chlorine story is too narrow to convert without eczema/skin-outcome language, the disciplined route may be commercially unviable. |
| A-04 | Premium pricing will increase review scrutiny and proof burden, not just marketing ambition | go-no-go-memo-v1, kes-route-screening-memo-v2 | medium — Canopy case study referenced as precedent | Low-medium. Broadly accepted; the sensitivity is in how much scrutiny, not whether scrutiny exists. |
| A-05 | "Fits most tubs" / universal-fit is not credibly deliverable — the correct posture is a bounded-fit matrix with explicit supported and unsupported spout types | compatibility-engineering-breakpoints, installation-risk-matrix-v2, go-no-go-memo-v1 | medium — supported by tub-spout taxonomy analysis and complaint pattern review | High. If some attachment mechanism genuinely covers a very wide spout range with no meaningful failure modes, this assumption is over-cautious. But if wrong in the other direction, universal-fit marketing will create support and return volume. |
| A-06 | The four distinct leak failure modes (bypass flow, top overflow, seam/housing leak, retention failure) must be tested and reported separately — treating them as a single "leak test" is insufficient | compatibility-engineering-breakpoints, installation-risk-matrix-v2 | logic-only — engineering taxonomy not yet empirically validated on physical samples | Medium. If in practice one failure mode dominates and others are negligible, the taxonomy is still useful but less operationally urgent. |
| A-07 | Renter-friendly / tool-free installation is in tension with engineering robustness (retention stability, forced water path, overflow discipline) — achieving both simultaneously is difficult | compatibility-engineering-breakpoints, installation-risk-matrix-v2 | weak-to-medium — inferred from complaint patterns and engineering reasoning, not yet confirmed by sample testing | High. If a design solution can genuinely combine renter-friendly removal with robust sealing, this tension dissolves. If the tension is real and unavoidable, KES must make an explicit priority call. |
| A-08 | Consumers bathing in North America typically fill a tub under conditions that create a meaningful flow-rate challenge for compact inline filters — i.e., realistic fill speed is high enough to reduce contact time significantly | compatibility-engineering-breakpoints | logic-only — no direct measurement cited | Route-breaking. If typical tub fill is slow enough to make contact time acceptable, flow-rate is less of a constraint. If fill is typically fast, chlorine-reduction claims become much harder to defend. |
| A-09 | Baby / infant segment is commercially real and conversion-capable, but incurs higher trust and proof burden than the adult sensitive-skin segment | evidence-matrix, go-no-go-memo-v1, claim-risk-audit-v2 | medium — baby/infant segment supported by domestic-water-hardness research and parenting market context | Moderate. The segment is real either way; the sensitivity is in how far KES can lean into it without triggering claim exposure. |
| A-10 | Eczema / skin-improvement language is not defensible at current evidence levels — using it as a primary conversion mechanism would create more liability than commercial benefit | go-no-go-memo-v1, kes-route-elimination-memo-v1, claim-risk-audit-v2, evidence-matrix | medium — consistent across all pages, multiple source types | High (if wrong in a surprising direction). The assumption is well-supported. Sensitivity runs the other way: if a future study establishes stronger product-level efficacy, this constraint could loosen. |
| A-11 | Refill cadence and cost are a real consumer decision factor, and a too-frequent or too-expensive replacement cycle will erode lived economics and trigger negative reviews | go-no-go-memo-v1, kes-next-step-execution-plan-v1 | weak — flagged as a required validation item, not yet measured | Moderate-high. Refill economics are listed as a required sanity check precisely because this assumption is unverified. |
| A-12 | The hybrid premium-but-disciplined route (Concept Candidate A) is currently the strongest survivable path — outranking the narrow-technical route on commercial appeal while remaining more defensible than baby/eczema DTC | kes-concept-brief-v1, kes-route-elimination-memo-v1, kes-route-screening-memo-v2 | logic-only — judgment call based on route comparison, not empirical | High. This is the master strategic assumption. If normal-flow proof fails, or fit matrix turns out too narrow, the hybrid route collapses and the narrow-technical route becomes the only defensible option. |
| A-13 | Hard-water softening is not achievable by compact bath filters at the levels needed to make a credible softening claim — compact filter media does not deliver clinically meaningful water softening | evidence-matrix, claim-risk-audit-v2 | medium — supported by evidence-matrix assessment and claim-risk audit | Medium. If a filtration media innovation changes what is achievable, this constraint shifts. Currently it is well-supported. |
| A-14 | Chloramine-dominant markets (Northeast US, Chicago metro) should not be prioritized in V1 because compact bath filters cannot make an honest chloramine-removal claim at realistic flow rates | kes-concept-brief-v1, go-no-go-memo-v1 | logic-only — based on chemistry reasoning and claim-defense logic, not chloramine-specific product testing | Medium. If a media is identified that credibly addresses chloramine under realistic conditions, the geo-priority assumption should be revisited. |
| A-15 | Demand strength in a water-quality concern segment does not automatically translate into a product story that is commercially and defensibly sustainable | go-no-go-memo-v1 | logic-only — strategic reasoning | Low-medium. This is a meta-assumption; it shapes how much weight to give high-anxiety segments. Hard to be "wrong" in an empirical sense, but it can be misapplied to justify being overly restrictive. |
| A-16 | The five workstreams in the execution plan (concept narrowing, competitor sample acquisition, validation test setup, claim guardrails, decision checkpoint) are sufficient to answer the survivability question within a single diligence cycle | kes-next-step-execution-plan-v1 | logic-only — planning judgment | Low. The plan is deliberately structured and scoped; the main sensitivity is whether tests reveal unexpected complexity that requires more rounds. |

---

## Review checklist

다음 이벤트가 발생할 때 이 레지스터를 검토해야 합니다:

- Workstream 3 validation test results are returned (especially A-01, A-06, A-07, A-08)
- Competitor samples are acquired and examined (A-05, A-06, A-07)
- Refill economics sanity check is completed (A-11)
- Any go/no-go memo is revised (A-03, A-12)
- A new geo / water-profile screen is completed (A-02, A-14)

---

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-kes-concept-brief-v1]]
- [[bathtub-filter-kes-go-no-go-memo-v1]]
- [[bathtub-filter-kes-route-screening-memo-v2]]
- [[bathtub-filter-kes-route-elimination-memo-v1]]
- [[bathtub-filter-evidence-matrix]]
- [[bathtub-filter-claim-risk-audit-v2]]
- [[bathtub-filter-compatibility-engineering-breakpoints]]
- [[bathtub-filter-installation-risk-matrix-v2]]
- [[bathtub-filter-kes-next-step-execution-plan-v1]]
- [[bathtub-filter-test-gating-checklist-for-kes]]
