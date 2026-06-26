---
type: product
status: draft
owner: strategy
created: 2026-04-17
updated: 2026-06-17
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, decisions, tracker]
source_count: 4
review_cycle: weekly
verification_status: working
related:
  - ./bathtub-filter-kes-next-step-execution-plan-v1.md
  - ./bathtub-filter-kes-go-no-go-memo-v1.md
  - ./bathtub-filter-test-gating-checklist-for-kes.md
---

# 浴缸过滤器决策与工作流台账

## 这页的用途

这页是整个 bathtub filter KES diligence 过程中的**决策与工作流追踪器**。

它不替代 go/no-go memo 或 execution plan，而是作为一个持续更新的工作状态视图：
- 哪些决策仍然 open，谁负责，下一步是什么
- 每条 workstream 当前在哪里
- 已完成的决策（防止重复讨论）
- 决策历史存档

**更新频率：** weekly（至少在 workstream 有进展时同步更新）

---

## Open Decisions

这些决策目前尚未有明确答案，需要验证数据或明确的判断调用才能关闭。

| # | Decision | Owner | Input required | Due | Status |
|---|---|---|---|---|---|
| D-01 | Confirm or re-rank lead concept: Hybrid premium-but-disciplined route vs Narrow chlorine-focused route — current ranking is provisional pending Workstream 2 and 3 results | strategy | Public competitor evidence (WS2) + normal-flow test results if existing samples/records are available (WS3) | After WS2+WS3 evidence review | not-started |
| D-02 | Define exact supported tub-spout types — which spout configurations are in scope for V1, which are explicitly out | strategy | 2026-06-17 已在 [[bathtub-filter-supported-spout-matrix]] 补入 8 类安装场景 + KES GO/GO（条件）/NO-GO 矩阵；S-01 non-diverter terminal-bend circumference <=18 cm 为正向边界；两组 RV / mobile-home center-set / valve-diverter faucet 为 S-02-adjacent 正向证据；freestanding tub filler 弧形/异型管非瀑布出水已补 2 kg 承重正向证据。仍需动态注水、漏水/溢流和更多 spout 类型实测记录。 | Before fit/testing scope finalized | in-progress |
| D-03 | Set pass/fail thresholds for normal-flow chlorine reduction test — what performance level is required for the route to remain viable | strategy | Validation protocol design (WS3) | Before testing begins | not-started |
| D-04 | Resolve renter-friendly vs engineering robustness priority — if they cannot be simultaneously achieved, which takes precedence in V1 concept | strategy | Sample testing + engineering assessment (WS3) | After WS3 results | not-started |
| D-05 | Determine acceptable refill cadence and cost ceiling — what refill interval and price point will the target segment accept without triggering maintenance fatigue or lived-economics collapse | strategy | Consumer research or benchmark review; refill economics sanity check (WS3) | After WS3 | not-started |
| D-06 | Decide whether chlorine/comfort story converts without eczema-forward language — is the disciplined claim set commercially sufficient | strategy | Content testing or competitive signal review (WS2+WS4) | After WS2+WS4 | not-started |
| D-07 | Select primary geo / water-profile for V1 launch targeting — confirm free-chlorine North America as primary, or refine sub-geo further | strategy | Water jurisdiction demand map review + WS2 competitive observation | Before concept finalization | not-started |
| D-08 | Final continue / pause / archive decision after early validation | strategy | All WS1–WS4 outputs; gate checklist passage | After WS5 | not-started |

---

## Workstream Status

来自执行计划（execution plan v1）的 5 条工作流，当前状态如下。

| Workstream | Description | Owner | Status | Next action |
|---|---|---|---|---|
| WS1 — Concept narrowing | 从现有 concept candidates 中锁定 1 lead + 1 backup，输出每条路线的 concept summary 和被淘汰路线的 rejection note | strategy | not-started | Confirm lead concept ranking (D-01); freeze route scope before WS2 begins |
| WS2 — Competitor public evidence integration | 整理原始 11 ASIN 中的 bathtub active 10 ASIN 官方/PDP 公开资料、价格/销量信号、claim、安装与结构线索；Filterbaby 已迁出 shower-filter；不做样品采购清单或预算估算 | strategy | in-progress | Use [[bathtub-filter-11-asin-public-competitor-evidence-2026-06-02]] as the evidence matrix |
| WS3 — Validation test setup | 建立并运行验证测试：normal-flow chlorine reduction, reduced-flow comparison, fit matrix across spout types, leak/overflow/stability, refill/maintenance burden | TBD | in-progress | 2026-06-17 已有 S-01 周长边界正向记录、2 组 S-02-adjacent 正向适配样本、freestanding tub filler 非瀑布出水 2 kg 承重记录，以及 8 类安装场景 GO/NO-GO 矩阵；仍需设计 test sheet template、定义 pass/fail thresholds (D-03)、补更多 spout 类型和动态注水记录 |
| WS4 — Claim & language guardrails | 完成 allowed / conditional / banned claim list，防止团队在这个品类滑向高风险语言；输出 claim register | strategy | in-progress | Complete [[bathtub-filter-claim-register]] stub; fill in example wording after WS2 competitor research |
| WS5 — Decision checkpoint | 在公开竞品资料复盘与验证测试准备后，做一次明确的 continue / pause / archive 决策；如无实物或人工测试记录，E 层安装/兼容性仍保持未关闭 | strategy | not-started | Depends on WS1–WS4 outputs; schedule decision review after WS2 evidence and any WS3 records |

---

## Completed Decisions

_这个区域目前为空。随着决策被关闭，将逐条移入此处。_

| # | Decision | Resolution | Date | Notes |
|---|---|---|---|---|
| — | — | — | — | — |

---

## Decision Log

_这个区域用来记录决策历史——每次重大判断调用、每次路线重排序、或每次 go/no-go memo 更新，都应在这里留下一条记录。_

_Format:_ `YYYY-MM-DD | Decision ID or topic | What was decided | Why | Who`

| Date | Topic | Decision | Rationale | Owner |
|---|---|---|---|---|
| 2026-04-14 | Route framing | Conditional GO for continued diligence — not product GO | Research package sufficient for continued concept exploration, but insufficient for launch conviction | strategy |
| 2026-04-14 | Route elimination | Eliminated: aggressive eczema/baby DTC, commodity broad-claim bath-ball as lead routes | Claim/compliance risk too high; no differentiation advantage | strategy |
| 2026-04-14 | Concept priority | Lead: Hybrid premium-but-disciplined tub-spout route. Backup: Narrow chlorine-focused technically disciplined route. Conditional reserve: soft-hanging ritual | Based on route comparison across commercial appeal, defensibility, and technical feasibility | strategy |
| 2026-04-14 | Market scope | V1 primary target: North America, free-chlorine-dominant regions | Chloramine and hard-water markets are harder to defend with current claim set | strategy |
| 2026-06-17 | D-02 supported spout scope | Added first V1 installation scenario GO/NO-GO matrix with 8 spout scenarios; S-01 <=18 cm and S-02 pull-up diverter are current GO cores; S-06 wobble and untested S-05 wide-body are NO-GO; S-08 low-clearance was later corrected to GO with off-center install for 40-60 mm wall distance | Combines KES flat-strap design, S-01 circumference evidence, RV/mobile-home S-02 evidence, and existing spout taxonomy estimates | strategy |
| 2026-06-17 | Wall-distance boundary correction | Changed outlet center-to-wall distance from a <60 mm NO-GO rule to a usability/aesthetics rule: >=60 mm centered/aesthetic, 40-60 mm off-center usable, <40 mm theoretical edge case | User clarified the water outlet need not be perfectly centered; KES can tolerate about 20 mm offset and typical bathtub spouts are not under 40 mm from wall | strategy |
| 2026-06-17 | Freestanding tub filler fit evidence | Updated freestanding tub filler from default NO-GO to GO for curved / special-shaped / non-waterfall outlets when the tie is installed 60 mm from the outlet end; waterfall / wide-body outlets remain NO-GO | User-provided photo and 2 kg load-bearing test using included 5-hole 124 mm x 20 mm tie + 3M hook | strategy |

---

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-kes-next-step-execution-plan-v1]]
- [[bathtub-filter-kes-go-no-go-memo-v1]]
- [[bathtub-filter-kes-concept-brief-v1]]
- [[bathtub-filter-kes-route-elimination-memo-v1]]
- [[bathtub-filter-test-gating-checklist-for-kes]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-assumption-register]]
- [[bathtub-filter-supported-spout-matrix]]
