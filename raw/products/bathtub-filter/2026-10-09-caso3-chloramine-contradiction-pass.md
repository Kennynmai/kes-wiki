---
source_type: vendor-material
source_vendor: Zibo Onlyzone Water Treatment Technology Co., Ltd. (seal reads 淄博宗立新材料科技有限公司)
source_file: /Users/moltbot/Downloads/宗立测试-一氯胺及三氯铵 50g亚硫酸钙球.docx
created: 2026-10-09
domain: bathtub-filter
status: extracted
source_count: 2
---

# Bathtub Filter — CaSO₃ × Chloramine Contradiction Pass (2026-10-09)

## Purpose

Capture and critically assess **two new data points that run directly against the wiki's current Tier-1-anchored position that calcium sulfite does not remove chloramine.**

1. A **supplier report** from 淄博宗立 (Onlyzone) — `ZONET20230707001`, dated 2023-07, claiming 93–100% monochloramine removal through a 50 g 2–3 mm CaSO₃ shower filter.
2. A **KES first-party bench test** — 4 ppm chloramine through 130 g CaSO₃ at 24 L/min / 38 °C / 60 s, read near-zero on a total-chlorine color card.

**This is a contradiction event, not a gap fill.** The existing wiki position (see `wiki/products/bathtub-filter/bathtub-filter-chloramine-media-research.md` Section 3) is that CaSO₃ is `❌ No removal expected` for NH₂Cl, and chloramine claims are in the **banned zone** of the claim register.

The purpose of this pass is **not** to overturn that position. It is to record both data points precisely, establish exactly what they do and do not support, and specify the one test that would settle the question.

---

## Source 1 — Supplier report ZONET20230707001

> **Prior ingestion note.** This same report was already ingested into the wiki on **2026-06-17** from another workstation: raw archive `raw/products/bathtub-filter/2026-06-17-zongli-calcium-sulfite-chloramine-test/`, archive page [[bathtub-filter-supplier-report-zongli-calcium-sulfite-chloramine-2023-07]], and source-summary `wiki/source-summaries/bathtub-filter-zongli-calcium-sulfite-chloramine-test-2023-07.md`. That pass assessed it as a *signal worth validating* and drafted the supplier question list (including the 三氯铵 naming question). **What this pass adds:** the quantitative critique (influent-decay confound, capacity utilization, EBCT math, removal-rate provenance), the KES first-party bench test as a second data point, the contradiction-event framing, and the Module 7 controlled-test spec.

### Report header (verbatim)

```
淄博宗立新材料科技有限公司
检测报告

样品编号：ZONET20230707001
样品接收时间：2023年07月07日
样品名称：沐浴过滤器
检测完成时间：2023年07月13日
```

- **Issuer:** 淄博宗立新材料科技有限公司, seal reads 淄博宗立新材料科技有限公司 **检验专用章** (supplier's own internal lab seal)
- **Brand mark:** `ZONE 宗立科技` (header logo)
- **Sample ID:** `ZONET20230707001`
- **Sample received:** 2023-07-07 · **Test completed:** 2023-07-13 (6 days)
- **Sample name:** 沐浴过滤器 (shower filter)
- **Sample description (verbatim):** 内置滤料为50g宗立（2-3mm）亚硫酸钙球。
- **Test item (verbatim):** 加标测试(氯胺）
- **Test method (verbatim):** 样品出水流速分别为5L/min、3L/min。将样品滤芯接入通水设备。
- **Signature block:** 检测 / 批准 / 检测盖章 are present as **handwritten signatures only**. No typed analyst or approver names. (Contrast: `ZONET20251113001` names 马艳华 tested / 陈加森 approved.)
- **Tested / approved names:** not machine-readable in the document.

### Results table (verbatim)

| 测试点位 (cumulative L) | 流速 | 检测项目 | 过滤前 (mg/L) | 过滤后 (mg/L) | 去除率 (%) |
|---|---|---|---|---|---|
| 300L | 5L/min | 一氯胺 | 0.46 | 0.0184 | 96 |
| | | 三氯铵 | 1 | 0 | 100 |
| 500L | | 一氯胺 | 0.341 | 0.023 | 93.26 |
| | | 三氯铵 | 0.728 | 0 | 100 |
| 300L | 3L/min | 一氯胺 | 0.43 | 0 | 100 |
| | | 三氯铵 | 1 | 0 | 100 |
| 500L | | 一氯胺 | 0.341 | 0 | 100 |
| | | 三氯铵 | 0.728 | 0 | 100 |

*Anomalous note: the flow-rate column merges visually in the original table — 5 L/min carries the 300L and 500L rows, 3 L/min carries its own 300L and 500L rows. This reading is consistent with the stated method ("出水流速分别为5L/min、3L/min").*

### Not disclosed in the report

- **No analytical method.** Only "加标测试(氯胺)" — no DPD / IC / titration reference.
- **No detection limit or quantitation limit.** Every "0" therefore means only "below an undisclosed threshold".
- **No pH.** This is the single most consequential omission — see chemistry analysis below.
- **No temperature, no TDS, no alkalinity, no water matrix.**
- **No chlorine-species confirmation.** Nothing establishes that the challenge water actually contained monochloramine rather than free chlorine, or that free chlorine was absent.
- **No replicates.** One column per flow rate.
- **No control arm.** No influent-only blank, no media-free column, no inert-media hydrodynamic control.
- **No breakthrough curve.** Only two throughput points (300 L, 500 L) per flow rate — no capacity endpoint.

---

## Source 2 — KES first-party bench test (2026-10-09, verbal + photographic)

Reported by KES product side with three photographs of a 总氯比色卡 (total chlorine color card, 0.1–10 mg/L, swatches at 0.1 / 0.2 / 0.5 / 1 / 2 / 5 / 10).

### Stated protocol (as reported)

| Parameter | Value |
|---|---|
| Test sequence | 1) measure raw water chloramine; 2) prepare 4 ppm chloramine water; 3) pass through 130 g CaSO₃; 4) measure filtrate |
| Media mass | 130 g CaSO₃ (matches Version A loading) |
| Flow rate | 24 L/min |
| Contact time | 60 s |
| Water temperature | 38 °C |
| Influent | 4 ppm chloramine |
| Reported result | chloramine **接近 0** (near zero) |

### Photographic record

1. **Influent** — sample tube reads a deep pink/magenta, visually in the 2–5 region of the 0.1–10 mg/L card.
2. **"原水" (raw water, pre-filter)** — sample tube reads essentially colourless / faint, against the card; caption "原水" (raw water).
3. **Effluent** — sample tube reads colourless against the card; caption "经过亚硫酸钙130g, 24L/min, 60s".

> **Caution on photo 2:** the second photo is captioned 原水 ("raw water") yet shows a *clearer* sample than the first, which is captioned 4 ppm 绿氨水. These two captions cannot both describe the same water. The photograph order is ambiguous and should not be relied on as before/after evidence. Treat only the reported protocol numbers as usable, not the photo sequence.

### What the test does and does not establish

**Does establish (as an observation):**
- A measurable colour drop consistent with strong chlorine-species removal at a **genuine bath-fill flow rate (24 L/min)**, **genuine bath temperature (38 °C)**, and **Version A media loading (130 g)**.
- These are the most adverse realistic conditions available. This is the strongest single point in favour of the hypothesis, because it argues against a pure contact-time artifact.

**Does not establish:**

| # | Gap | Consequence |
|---|---|---|
| 1 | **总氯比色卡 is a total-chlorine strip, not a chloramine-specific method** | Cannot attribute the drop to chloramine specifically. Free chlorine was never measured. If the 4 ppm challenge carried co-existing free chlorine, CaSO₃ would have consumed the free chlorine first and the strip would read near-zero regardless of chloramine fate. |
| 2 | **Card low end is 0.1 mg/L** | "接近 0" means **≤0.1–0.2 mg/L**, i.e. removal **>95–97.5%** — not 100%, and not a measured zero. |
| 3 | **No influent-only control** | A 4 ppm chloramine solution held at 38 °C decays on its own. With no media-free blank run in parallel, media contribution cannot be separated from spike decay. |
| 4 | **No inert-media control** | No column of matched bed volume and matched hydrodynamic resistance. Pressure-drop/flow-restriction effects are uncontrolled. |
| 5 | **No pH** | The one variable Yiin et al. (1987) identifies as controlling the sulfite–chloramine rate. |
| 6 | **Single point, single replicate** | No rate constant, no dose-response, no throughput series. |
| 7 | **No chloride mass balance** | See "The decisive control" below — the cheapest available falsification check was not run. |
| 8 | **Capacity utilization 0.13%** | 24 L × 4 mg/L = 96 mg monochloramine against ~73 g theoretical capacity. The test consumed essentially none of the media. It cannot support any efficiency, dose, or lifetime figure. |

---

## Quantitative cross-checks computed during this pass

Bulk density for CaSO₃ balls: **0.9–1.1 g/cm³** (from the Onlyzone CaSO₃ brochure, recorded in `raw/products/bathtub-filter/2026-04-17-onlyzone-supplier-material-evidence-pass.md`). Stoichiometry: CaSO₃ = 120.14 g/mol, SO₃ = 80.06 g/mol → 66.6% SO₃ by mass. One mol SO₃ reduces one mol NH₂Cl → **1.19 g SO₃ per g NH₂Cl**.

### Capacity utilization

| Source | Media | Theoretical NH₂Cl capacity | Cumulative load | **Utilization** |
|---|---|---|---|---|
| ZONET20230707001 | 50 g × 66.6% = 33.3 g SO₃ | ~28 g NH₂Cl | 500 L × 0.341 mg/L = 170.5 mg (+ 364 mg NCl₃) | **0.61%** |
| KES bench test | 130 g × 66.6% = 86.6 g SO₃ | ~73 g NH₂Cl | 24 L × 4 mg/L = 96 mg | **0.13%** |

**Neither test touches capacity.** Both are existence proofs at large reagent excess — the weakest possible evidence form for an efficacy claim, and the reason neither can be scaled into a life model.

### Contact time (EBCT)

Using the brochure bulk density (1.0 g/cm³ central):

| Case | Bed volume | Flow | **EBCT** |
|---|---|---|---|
| Vendor ZONET20230707001 | 50 g ÷ 1.0 = 50 cm³ | 5 L/min | **≈0.60 s** |
| Vendor ZONET20230707001 | 50 cm³ | 3 L/min | **≈1.00 s** |
| KES bench test | 130 g ÷ 1.0 = 130 cm³ | 24 L/min | **≈0.33 s** |

**Notable:** the KES bench test ran at roughly **one-third** the contact time of the vendor's slowest point, at the production media mass, and still read near-zero. If the vendor result is real, the KES result is the more surprising one — it is the harder case. This is the strongest pro-evidence argument available and should not be discarded.

### Decay confound in the vendor report

The influent itself is not constant:

| Species | at 300 L | at 500 L | Change |
|---|---|---|---|
| 一氯胺 | 0.46 mg/L | 0.341 mg/L | **−25.9%** |
| 三氯铵 | 1.0 mg/L | 0.728 mg/L | **−27.2%** |

Both species decayed ~26–27% across the run, over 60–167 minutes. **No influent-only blank was reported at matched timestamps.** A spiked chloramine solution decaying on its own at this magnitude would produce exactly this pattern — and would also produce "0" effluent readings. The report contains nothing that separates media removal from spike decay. This is the single largest defect in ZONET20230707001.

### Removal-percentage provenance

Both non-zero-percentage rows are exact arithmetic restatements of the inlet/outlet pair:
- 0.46 → 0.0184 gives exactly 96.00%
- 0.341 → 0.023 gives exactly 93.26%

The 去除率 column therefore carries no independent information. Note also the precision anomaly: `0.0184` (4 significant figures) sits amid inlet values given to 2–3 significant figures and every other outlet given to 2–3. This is consistent with the outlet having been **back-calculated to hit a target percentage** rather than read from an instrument.

---

## Chemistry reconciliation

The wiki's Tier-1 anchor (Yiin, Walker & Margerum 1987, *Inorg. Chem.* 26(21):3435–3441) reports that the NH₂Cl + sulfite/bisulfite reaction is general-acid-assisted and **strongly pH-dependent**, with bisulfite "ineffective at reducing chloramines and then maintaining an entirely reduced state" at pH 8.5, and fast at pH 4.0.

Neither new data point reports pH. Three possibilities, and the report cannot distinguish between them:

1. **The test ran at acidic pH.** Then the result is real chemistry, entirely consistent with Yiin 1987, and says nothing about pH 7.5–8.5 municipal water.
2. **The test ran at neutral–alkaline pH and the effect is real.** This would genuinely contradict Yiin 1987 for CaSO₃ specifically — possible via surface catalysis on the porous ball surface or trace-metal catalysis, but unproven.
3. **The effect is an artifact** — spike decay, free-chlorine interference, or sub-LOD reporting.

There is also a naming problem that must be resolved before any of this can be used:

**三氯铵 (nitrogen trichloride, NCl₃) at 0.728–1.0 mg/L is not a realistic drinking-water species.** NCl₃ is a trace chlorination byproduct, reported in distribution systems at ng/L–µg/L. A challenge concentration of ~1 mg/L is roughly three orders of magnitude above anything reported in potable water, and NCl₃ is unstable and shock-sensitive in concentrated form. Either the supplier means **二氯铵 (dichloramine, NCl₂H)** and has mislabeled it, or the challenge solution is not representative of anything KES would encounter. Note that `bathtub-filter-disinfectant-types-and-media-guide.md` has **already scoped dichloramine and trichloramine out of the product model** on the grounds that they are rare above pH 8 — so if the label is wrong, the report's most impressive numbers (100%, 100%, 100%, 100%) belong to a species KES has not modeled at all.

**This must be asked of the supplier before the report is cited anywhere.**

---

## The decisive control (why these two tests cannot settle it, and what would)

Both tests fail on the same root cause: **they measure the thing they are trying to remove, using a method that the thing being removed can also degrade.**

Chloramine in warm water is intrinsically unstable. Total-chlorine colorimetry is not species-specific. So neither test can distinguish "media removed it" from "it left on its own."

The fix is cheap and does not require the questionable chloramine spike at all:

> **Chloride mass balance.** If chloramine is genuinely reduced to ammonia, every mole of NH₂Cl destroyed releases one mole of Cl⁻. Ion chromatography for chloride is a mature, cheap, species-blind measurement that is completely immune to the spike-decay confound — because it measures the *product* of the reaction, not the *substrate*.

So: measure Cl⁻ in, Cl⁻ in the media-free blank at matched time/temperature, and Cl⁻ out. If effluent chloride rises by exactly the amount the color card implies was removed, the claim is real. If it does not, the color drop was decay or interference.

This single control would resolve the contradiction more definitively than any amount of additional colorimetry.

### Minimum protocol for a decisive test

| Requirement | Specification |
|---|---|
| **Analytical method** | DPD amperometric titration differentiating free / combined chlorine, **plus ion chromatography for chloride**. Report LOD and LOQ. |
| **Arms (minimum 4)** | (a) media + challenge; (b) challenge, no media, matched time/temperature — decay blank; (c) inert media of matched bed volume and matched ΔP — hydrodynamic blank; (d) production-spec 3–4 mm CaSO₃ |
| **pH** | Controlled and reported at 7.0 / 7.8 / 8.5. Yiin 1987 predicts divergence across this range; testing only one pH cannot distinguish chemistry from artifact. |
| **Temperature** | 20 / 38 / 42 °C |
| **Throughput** | A **series to breakthrough**, not a single point. This is the only way to produce a life-model-compatible result. |
| **Replicates** | n ≥ 3 per condition |
| **Species definition** | Resolve 一氯胺 vs 二氯铵 vs 三氯铵 with the supplier in writing before testing |
| **Media** | Production spec **3–4 mm ZONE-CL-A02 Gen-3** at 130 g — not 2–3 mm at 50 g |

---

## Derived observations for KES

### 1. The existing wiki position was overstated, and this is the important finding

`bathtub-filter-chloramine-media-research.md` Section 3 concludes "Effective for free chlorine; not chemically suited for monochloramine" and the summary table marks CaSO₃ as `❌ No removal expected`. Gap #2 states the basis plainly:

> "No peer-reviewed study measuring CaSO₃ + NH₂Cl reaction rate. **The expected ineffectiveness is inferred.**"

That is an **inference from absence of data presented as a measured negative**. The page's own text concedes it found "no quantitative data for CaSO₃ + NH₂Cl removal rate in **any** peer-reviewed or industry source" and then treated the silence as evidence of absence. Having now produced two independent observations pointing the other way — one of them at production media mass, bath-fill flow, and bath temperature — the ❌ cell's stated basis no longer holds even though its conclusion may still be true.

**Recommended re-label, not reversal:** the cell should move from "❌ No removal expected" to "⚠️ Untested — two uncontrolled observations, both favourable, neither capable of support." The claim ban stays; the *reason* recorded for the ban changes from "chemistry mismatch" to "chemistry mismatch is contested and unresolved; no controlled evidence exists in either direction."

### 2. This does not change Version A's scope, model, or claims today

- [[bathtub-filter-media-efficacy-at-bath-conditions]] Section 9 remains a **free-chlorine** model. Two uncontrolled chloramine existence-probes do not extend it.
- The claim-register **chloramine entry stays in the banned zone**. No new evidence here clears any claim bar.
- Assumption **A-14** (chloramine geos deferred in V1) is untouched — it was never a chemistry assumption, it was a claim-defensibility assumption, and it remains exactly as true.

### 3. Two things did change

**The evidence-gap list is now smaller.** Gap #2 in the chloramine research page ("no CaSO₃ + NH₂Cl data anywhere") is no longer literally true — there are now two vendor/first-party data points. The gap changes character from "no data" to "no controlled data."

**A new high-value experiment became available.** The chloride mass-balance design above is cheap, fast, and settles the question. It was not on the R&D list before this pass because no one had a reason to believe CaSO₃ was worth testing.

### 4. Provenance notes

- **Entity name — RESOLVED 2026-10-09.** The seal reads 淄博宗立**新材料**科技有限公司; the wiki's canonical supplier name is 淄博宗立 / Zibo Onlyzone **Water Treatment** Technology Co., Ltd. **KES confirmed on 2026-10-09 that these are the same entity** — one company, two renderings of the Chinese/English legal name. This is **not** a certificate-holder ambiguity and no further legal-entity reconciliation is required. The canonical pairing to use going forward is recorded in `governance/entity-canonicalization.md`.
- **Report age:** ZONET20230707001 predates the dechlorination reference `ZONET20251113001` by ~2.3 years and the current date by ~3.3 years. It likely describes a **prior generation** of the media.
- **SKU mismatch:** 50 g at **2–3 mm** is the `ZONE-CL-A01 Gen-4` size band. KES Version A uses `ZONE-CL-A02 Gen-3` **3–4 mm** at 130 g. Different generation, different size band, different mass, different SKU.
- **Flow regime mismatch:** the vendor test is a shower/handheld regime (3–5 L/min). KES Version A is a bath-fill device (15–30 L/min, 18–25 L/min typical). The vendor's slower, longer-contact regime is **more favorable** than KES's design point.
- **Analyst traceability:** ZONET20230707001 has no machine-readable 测试 / 批准 names. ZONET20251113001 does (马艳华 / 陈加森). Traceability for this report is weaker.

---

## What this pass explicitly does NOT do

- It does not overturn the Tier-1 chemistry position.
- It does not lift any claim ban.
- It does not extend the Version A life model.
- It does not clear CaSO₃ for any chloramine market.
- It does not treat either data point as verified.

## Sources

- Supplier report `ZONET20230707001`, 淄博宗立新材料科技有限公司, received 2023-07-07, completed 2023-07-13 (local file: `/Users/moltbot/Downloads/宗立测试-一氯胺及三氯铵 50g亚硫酸钙球.docx`)
- KES first-party chloramine bench test, 130 g CaSO₃ / 24 L/min / 60 s / 38 °C / 4 ppm chloramine, 2026-10-09 (photographic record, verbal protocol)
- `raw/products/bathtub-filter/2026-04-17-onlyzone-supplier-material-evidence-pass.md` — supplier lab identity, CaSO₃ bulk density 0.9–1.1 g/cm³, SKU map, `ZONET20251113001`
- Yiin BS, Walker DM, Margerum DW. *Inorg. Chem.* 1987;26(21):3435–3441 — DOI 10.1021/ic00268a006
- `wiki/products/bathtub-filter/bathtub-filter-chloramine-media-research.md`
- `wiki/products/bathtub-filter/bathtub-filter-disinfectant-types-and-media-guide.md`
- `wiki/products/bathtub-filter/bathtub-filter-claim-register.md`
- `wiki/products/bathtub-filter/bathtub-filter-media-efficacy-at-bath-conditions.md`
