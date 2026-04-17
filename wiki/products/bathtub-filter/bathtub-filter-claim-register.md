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
domains: [bathtub-filter, kes, claims, compliance, marketing, version-a]
source_count: 4
review_cycle: monthly
verification_status: spot-checked
related:
  - ./bathtub-filter-claim-risk-audit-v2.md
  - ./bathtub-filter-evidence-matrix.md
  - ./bathtub-filter-compliance-framework-and-evidence-boundaries.md
  - ../../source-summaries/bathtub-filter-kes-internal-product-materials-2026-04-17.md
  - ../../source-summaries/bathtub-filter-onlyzone-supplier-material-evidence-2026-04-17.md
---

# Bathtub Filter — Claim Register

## Status note

**2026-04-17 更新：Version A 内部产品讲解文档到位后，Allowed / Conditional 区的 example wording 已从占位符填入 Version A 实际语言。**

禁区仍保持不变（非谈判性）。Version B / C（氯胺城市 / 软水器下游 / well water / 仪式浸浴）的 claim wording 仍 pending。Workstream 2 的竞品样品差异化审核，仍可在 Version A 的 wording 上做二次优化（确保不被竞品语言占领），但不再阻塞首次使用。

---

## Claim categories

基于 claim-risk-audit-v2 和 evidence-matrix（宣称阶梯）识别出的 7 个主要宣称类别：

1. **Chlorine reduction** — 游离氯去除，当前最可防守的技术宣称核心
2. **Sensory / comfort benefit** — "浴水更柔和 / 更舒适"等感官层面表达，不带医疗结果含义
3. **Skin-comfort framing** — 针对敏感肌肤的非结果型 framing，需要与 eczema claim 严格区隔
4. **Baby / infant segment** — 针对婴儿洗澡场景的 framing，商业价值高但 trust burden 也最高
5. **Fit / compatibility** — 适配范围宣称，包括支持的 spout types 和明确的不支持说明
6. **Performance / testing** — 关于测试条件、测试结果和认证的宣称，需要清晰区分 certified vs tested vs media-credibility
7. **Environmental / sustainability** — 如有可替换滤芯等，可能涉及的环保/可持续相关表达

---

## Allowed claim zone (structure)

这些宣称类别在满足对应证据要求后可以使用。**"Example wording" 列当前为占位符，等待 Workstream 2 竞品研究后填入。**

| Claim category | Allowed | Example wording (Version A) | Evidence requirement | Notes |
|---|---|---|---|---|
| Positioning (category-level) | Yes — **leading** with this | "This is not a water purifier. It does not target TDS reduction. It is an end-stage harm-reduction module for the bath-fill scenario." | Verbatim from Doc 1 positioning statement; no efficacy claim embedded | Must appear on every customer-facing surface (page, pack, manual, rep script) to pre-empt "does it drop TDS?" objection |
| Chlorine reduction | Yes — with precision | "Fresh-filter, best-experience segment: **≥99% system-total chlorine reduction** at 15 L/min bath-fill flow." / "System-total chlorine reduction follows a posted curve over the filter life (99% → 95% → 90% → 80% → <50% replacement trigger)." | Internal life model at 130 g CaSO₃ + η=0.9 scaling (see [[bathtub-filter-media-efficacy-at-bath-conditions]] Section 9); **"free chlorine" must be specified — NOT "total chlorine" or "chloramine"**; flow rate and "fresh-filter / best-experience segment" qualifiers are non-optional | KPI is system-total (KDF × CaSO₃ chain), not single-media; must not re-use this wording for chloramine markets |
| Verification-by-user | Yes — with physical tool | "Verify with the included chlorine test strip: compare before- and after-filter water. Do not use a TDS pen — this product does not target TDS." | Test strip included in pack; FAQ explicitly steers user away from TDS pen as verification tool | This is a trust-building anchor unique to Version A vs. competitors who avoid user verification |
| Replacement-trigger language | Yes — with posted schedule | "Replace when system-total chlorine reduction drops to ~90% (soft trigger) / ~80% (strong trigger) / ~50% (mandatory)." / "At 2 ppm tap chlorine, 3 baths/week: soft trigger ≈ 113 baths; mandatory ≈ 143 baths (~1 year). At 1 ppm tap: approximately 2× lifespan." | Internal life model (see [[bathtub-filter-media-efficacy-at-bath-conditions]] Section 9) | Use gallons / baths / weeks — **do not convert to months** (per Doc 1 口径决策); add "your local tap chlorine affects lifespan — verify with test strip" |
| Sensory / comfort benefit | Yes — with non-medical framing | "Bath-water without the pool smell." / "Gentler-feeling bath-fill." / "A cleaner bath starting experience." | Stays in sensory/comfort language; no therapeutic outcome implied | Verbatim guardrail from Doc 1 sales script: "feels different" OK; "improves your skin" NOT OK |
| Media transparency | Yes — with specific framing | "Layered media: PP fiber disc → KDF55 (110 g) → calcium sulfite (130 g) → optional loading cavity. Each layer replaceable separately." / "KDF55 as end-stage safety layer and biofilm-inhibition layer. Calcium sulfite as primary dechlorination KPI." | Doc 1 media stack spec | Explicitly reframes KDF as safety-layer, not "dechlorination main media" — reduces "KDF = cure-all" misread |
| Fit / compatibility | Yes — with explicit scope | "Designed for standard US tub spouts 18–25 L/min; adjustable TPU strap fits most spout diameters; no-overflow envelope up to 35 L/min." | Internal flow-overflow test Doc 4; supported-spout matrix needs external sample sweep before launch (see [[bathtub-filter-supported-spout-matrix]]) | Every compatibility claim must ship with a "not supported" boundary (e.g., "swan-neck spouts without a pull-diverter may need aftermarket strap") |
| Performance / testing | Yes — with test/certified distinction | "KDF55 media inherits NSF/ANSI 42 material-level listing from supplier. Calcium sulfite tested against NSF/ANSI 177 protocol. **The finished product is not NSF-certified**; verify with the included chlorine test strip." | Doc 1 standards-口径; supplier cert docs on hand | See compliance-framework-and-evidence-boundaries for the 5 common misreads to avoid; this wording is **deliberately conservative** — it does not claim NSF certification of the finished product |
| No-pre-rinse | Yes — product-specific | "No pre-rinse required. Our coconut-shell carbon is acid-washed and factory pre-rinsed; no carbon dust in your tub on first use." | Doc 3 commissioning test (2-min rinse + 200 L pass-through, no powder); differentiator vs. B008A4AG2U "carbon powder all over tub" complaint cluster | This is a unique-to-KES claim — other products in category consistently fail here |
| Environmental / sustainability | Conditional — only if substantiated | TBD — pending replaceable-cartridge final design + supply-chain sourcing verification | Requires specific data on cartridge lifespan, material composition, and disposal or recycling pathway | Do not use vague "eco" language without specific backing |

---

## Conditional claim zone (structure)

这些宣称在特定条件或免责说明下可以考虑使用，但需要更高审慎度，且必须在使用前通过内部 evidence review。**"Example wording" 列待 WS2 填入。**

| Claim category | Condition required | Example wording (Version A) | Evidence requirement | Notes |
|---|---|---|---|---|
| Skin-comfort framing (sensitive skin) | Must not imply eczema improvement or clinical outcome; must stay in "may be gentler for" or "designed with sensitive-skin users in mind" territory | "Designed with sensitive-skin bathers in mind." / "May be gentler for users who find highly-chlorinated tap water drying." (Never: "improves eczema" / "heals your skin" / "clinical results for sensitive skin") | EPA literature + Seki 2003 + Danby 2018 support that chlorine ≥ 0.5 mg/L affects compromised skin; this supports the problem framing, **not** finished-product efficacy | The distinction between "for sensitive-skin users" vs "improves sensitive skin" is non-negotiable. Doc 1 FAQ verbatim: do not market as eczema product |
| Baby / infant framing | Only if product has clear scope definition, no medical safety implication, and no "baby-safe" equivalents without substantiation | "Filters the bath-water before it reaches your tub." / "Many families use a bath filter for chlorine-sensitive bathtime routines." (Never: "safe for babies" / "safe for newborns" / "pediatrician-approved") | Doc 2 review evidence: infant / small-child segment is the single largest positive review cluster across 5 ASINs — segment relevance is real, safety-claim burden is not met | Premium pricing will increase scrutiny on any baby-adjacent claim; do not write "baby-safe" without explicit evidence base |
| Head-to-head with mixed-media competitors | With technical explanation, non-disparaging | "Unlike mixed-bead products, Version A uses strict layered media (PP → KDF → CaSO₃) with an internal flow-diversion module. This prevents channeling, prevents media cross-reaction, and lets you replace each layer separately." | Doc 5 diversion-module test + Doc 4 flow-overflow test + Doc 2 competitor complaint teardown | Safe framing because it explains a technical design choice, not disparages a competitor; do not name specific competitor ASINs in marketing copy |
| Fast-flow chlorine performance | Only if independently replicated for the specific KES product at the stated flow rate | "Performance at fast fill: system-total chlorine reduction remains ≥90% at 30 L/min / ≥92% at 25 L/min when CaSO₃ is in its 90%-stage (see replacement schedule)." | Internal life model (Version A) + third-party replication still pending — see [[bathtub-filter-validation-testing-protocol]] Validation log | Directionally encouraging but needs third-party DPD replication before this wording goes to public copy |
| Reduced water irritation | Only with careful framing — comfort framing acceptable, skin-barrier claim is not | "Less chlorine in your bath water means less chlorine contacting your skin — that's the comfort difference many bathers notice." (Never: "restores skin barrier" / "prevents eczema flares") | Chlorine / bathing / skin-barrier evidence supports cautious problem framing; does not support product-level skin outcome promise | Use 3rd-level claim evidence ladder language (education framing), not 5th-level (clinical result language) — see [[bathtub-filter-evidence-matrix]] Section 9 |
| Supplier material credibility (NSF/ANSI 42) | Only as a media/material-level statement, never as a finished-product certification | "Our KDF55 media comes from a supplier listed under NSF/ANSI 42 (Zibo Onlyzone, Cert# C0843384-01). The finished KES product is not itself NSF-certified." | [[bathtub-filter-evidence-bibliography]] E1 (NSF cert C0843384-01, 2025-04-10) | Must always include the "finished product is not itself NSF-certified" disclaimer — otherwise the claim reads as a product cert |
| Supplier material safety (EU food-contact) | Only as a media-level statement about extractable heavy metals | "KDF55 media tested compliant with EU food-contact standards (CM/RES 2013/9 + Regulation 1935/2004 Ch. III) — 22 heavy metals below maximum limits, sensory rating 0 / 4 for taste and odor." | [[bathtub-filter-evidence-bibliography]] E2 (TÜV SÜD 721682290C, 2023-07-13) | Supports material-safety credibility; do not transfer this to finished-product food-contact claim without separate testing |
| KDF bacteriostatic property (biofilm inhibition) | Only as an internal-column property, never as a bath-water kill claim | "KDF media supports biofilm inhibition inside the filter column. In a 24-hour dynamic-contact test (ASTM E 2149-2020) against *S. aureus*, reduction exceeded 99.99%." | [[bathtub-filter-evidence-bibliography]] E3 (Guangzhou Institute of Microbiology WJ20221264, 2022-04-20; CNAS L0823) | **Must NOT claim** "kills bacteria in your bath water" — the test is 24h static; bath EBCT is 0.48–0.95 s (5-6 orders of magnitude shorter). Positioning must stay column-internal |
| KDF lead-reduction capability | Only as a material-level static-test reference; never as a "product removes X% lead" claim | "KDF55 media documented 92.6% lead reduction in a 24-hour static soak test (FSDA M250616-30, 2025-06-23)." | [[bathtub-filter-evidence-bibliography]] E4 (Zhejiang Fries FSDA M250616-30) | **High misread risk** — customers may assume this applies to bath-fill conditions. Recommend avoiding this claim in marketing copy entirely for V1; keep it as a specification-sheet line only |
| Life-model / dechlorination claim traceability | Only with full caveat chain | "Version A life model (system total dechlorination ≥99% → ≥50% over ~25,467 L at 2 ppm free chlorine) scales from a supplier reference report (40g / 0.5-1mm CaSO₃ / 8 L/min / 2 ppm; ZONET20251113001, 2025-12-26) by a factor of 3.25× (mass ratio) × 0.9 (efficiency)." | [[bathtub-filter-evidence-bibliography]] E5 + [[bathtub-filter-media-efficacy-at-bath-conditions]] Section 9 | Supplier internal lab; particle-size delta (0.5–1 mm reference → 3–4 mm production) not separately resolved. For external marketing copy, prefer the user-facing language "verify with included chlorine test strip" rather than quoting the numeric curve directly |

---

## Banned claim zone

**这个区域现在就可以执行。** 禁区来自 go/no-go memo、execution plan、和 claim-risk-audit，在 WS2 完成之前不会改变。

以下类别的宣称语言对 KES 是**不可妥协的禁区（non-negotiable forbidden zones）**：

| Banned claim type | Why banned | Risk level |
|---|---|---|
| Eczema improvement / eczema benefit | "改善湿疹" / "缓解湿疹症状" / "减少湿疹发作" — finished-product efficacy for eczema has no credible evidence base in this category at realistic conditions | Very high — trust collapse + regulatory exposure |
| Broad contaminant stack without proof | Claiming removal of heavy metals, VOCs, PFAS, pesticides, bacteria, viruses, or "hundreds of contaminants" without specific, independent test data per contaminant | Very high — false advertising risk |
| Universal-fit / "fits all tubs" | Any claim that implies compatibility with all or virtually all tub types without a tested and bounded spout matrix | High — support burden, return volume, review collapse |
| Baby-safety implication without substantiation | "Safe for babies" / "safe for newborns" / "mom-approved for infant bathing" style claims that imply safety from harmful substances without specific evidence | Very high — regulatory and liability exposure |
| Clinical language without clinical-grade backing | "Clinically proven" / "clinically tested to improve skin" / "doctor-recommended for eczema-prone skin" without the specific clinical evidence base these phrases imply | Very high — FTC / consumer protection risk |
| Hard-water softening claims | Implying that a compact bath filter meaningfully softens hard water — current evidence does not support compact bath filters achieving clinically or practically meaningful water softening | High — evidence does not support this for compact filter form factors |
| Chloramine removal claims (for V1 chlorine-media products) | If filtration media is designed for free chlorine, claiming chloramine removal is not defensible without separate validation of chloramine-specific reduction | High — chemistry mismatch, demand/claim mismatch in target markets |
| Implied medical treatment or disease prevention | Any language that positions the product as treating, preventing, or managing a health condition (including skin conditions, respiratory sensitivity, etc.) | Very high — drug/device regulatory threshold risk |

---

## How to use this register

**For marketing and product copywriting:**

1. **Check the banned zone first.** If a draft claim matches any banned category, remove or rewrite before review — these are not negotiable regardless of market pressure.
2. **Check the conditional zone second.** If a claim falls in the conditional zone, verify the stated condition is met and documented before use.
3. **For allowed claims, confirm evidence requirement is satisfied.** "Allowed" means structurally safe — it does not mean "usable without checking." The evidence requirement column must be ticked off per claim.
4. **Version A example wording is now usable but still pending WS2 competitive-language optimization.** First-pass wording is drawn from Doc 1 (Version A product explanation 2026-02); WS2 competitor sample review should sharpen differentiation without changing meaning.
5. **The chlorine-reduction wording is bounded by "fresh-filter, best-experience segment" and "at 15 L/min."** Do not drop these qualifiers — the system-total reduction curve degrades with filter age, and degrades with flow rate.
6. **Version A scope is US urban municipal (free-chlorine) tap water only.** Any marketing surface that could be read globally or read as chloramine-city-compatible must be rewritten. See [[bathtub-filter-kes-concept-brief-v1]] for scope declaration.

**For internal research and strategy:**

- This register is a living document. Update it when: new test results are available, competitor samples reveal new language patterns, or a legal/compliance review changes the risk assessment on any category.
- The banned zone should be treated as unchangeable until there is a specific, documented rationale for reconsideration (e.g., new clinical evidence base, regulatory guidance change).

---

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-claim-risk-audit-v2]]
- [[bathtub-filter-compliance-framework-and-evidence-boundaries]]
- [[bathtub-filter-kes-next-step-execution-plan-v1]]
- [[bathtub-filter-kes-go-no-go-memo-v1]]
- [[bathtub-filter-evidence-matrix]]
- [[bathtub-filter-decision-register]]
- [[bathtub-filter-assumption-register]]
- [[bathtub-filter-supported-spout-matrix]]
