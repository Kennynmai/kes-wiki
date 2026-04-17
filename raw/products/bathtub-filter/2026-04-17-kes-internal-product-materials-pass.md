# Bathtub Filter — KES Internal Product Materials Pass (2026-04-17)

## Purpose
Capture of **KES's own first-party product development materials**, provided by the product strategist on 2026-04-17. These are different in class from the external research previously captured in this cluster — they document:

1. the **Version A product explanation / sales training doc** (urban municipal tap water, dated 2026-02)
2. the **original 2024-02 market research baseline** that led to the current product
3. three **internal engineering test logs** (acid-washed activated carbon, flow/overflow + filter-disc layering, diversion module vs. none)
4. one **exploded-view product photo** (KES bathtub filter, showing strap handle, reservoir, filter disc, KDF layer, calcium sulfite layer, bottom mesh disc)

The materials together constitute the **authoritative internal reference** for:
- confirmed product architecture (supersedes "architecture hypotheses")
- confirmed Version A positioning and sales language
- confirmed internal test baselines (flow, overflow, turbulence, carbon behaviour)
- confirmed competitor teardown that shaped the product

The raw files are preserved below. Source input had Chinese UTF-8 rendering issues on parts of the body text; the **extracted English summary of specific facts and numbers** appears in the wiki source-summary at `wiki/source-summaries/bathtub-filter-kes-internal-product-materials-2026-04-17.md`. The source-summary is the page future agents should rely on; this raw file is kept as provenance.

---

## Source documents list

1. `浴缸过滤器_城市市政自来水版202602讲解.md` — Version A product explanation doc, urban municipal tap water, stable/compliant tone, bath temperature 38–42°C
2. `浴缸嘴过滤市场调查20240218.md` — original market survey (dated 2024-02-18, cost breakdown updated 2025-09-14)
3. `活性炭测试.md` — activated carbon variety comparison + acid-washed coconut-shell carbon test log (20240730–20240807)
4. `排水速度与过滤棉测试20241107.md` — flow rate / overflow / filter-disc stacking test (2024-11-07)
5. `导流模块与无的效果20251022.md` — diversion module presence/absence test at KDF and calcium sulfite layers (2025-10-22)

Plus one product photograph: exploded view of the KES bathtub filter — strap handle (grey TPU, perforated for adjustable length), reservoir/outer housing (white), cotton-layer top disc, clear canister with gold KDF media visible, clear canister with white calcium sulfite media visible, bottom mesh retention disc with white polymer frame. Described rather than embedded in raw.

---

## Key facts preserved (for provenance; full synthesis in source-summary)

### From Doc 1 (Version A, 2026-02)
- **Product positioning statement (must be restated across every customer-facing surface):** "This is not a water purifier; it does not target TDS reduction. It is an end-stage harm-reduction module for the bath-fill scenario."
- **Primary goal:** rapid dechlorination (fresh filter, best experience segment: ≥99% total chlorine removal).
- **Secondary goal:** sediment/particle capture via a visible filter disc (so the user can see the filter working — trust anchor).
- **Safety layer:** KDF55 acts as end-stage risk backstop + biofilm inhibition inside the media column.
- **Optional expansion:** bath-salt loading (240 mL cavity) for dispersal; mineral enhancement (may raise TDS — disclosed).
- **Media stack (bottom → top per flow path):** PP filter disc → calcium sulfite 130g (3–4 mm granule, held by 15 mm high chamber with 40-mesh 304 stainless retaining screen) → KDF55 110g (5–10 mesh, 15 mm chamber, 60-mesh 304 screen) → optional loading cavity → overflow trough + wide inlet → strap.
- **Flow regime:** 15–30 L/min typical bath-fill; EBCT per layer 0.48–0.95 s. Too short for KDF to be the dominant dechlorinator; therefore CaSO₃ is the primary dechlorination KPI; KDF is positioned as safety/longevity layer.
- **Life model (130g CaSO₃, η=0.9, 38–42°C, 2 ppm free chlorine):**
  - ≥99% stage: ~3,481 L cumulative ≈ 19.6 bath-fills (178 L/fill) ≈ 6.5 weeks at 3 baths/week
  - ≥95% stage: ~17,672 L ≈ 99.3 fills ≈ 33.1 weeks
  - ≥90% stage: ~20,124 L ≈ 113.1 fills ≈ 37.7 weeks
  - ≥50% (mandatory-replace) stage: ~25,467 L ≈ 143.1 fills ≈ 47.7 weeks (~1 year)
- **Life model at 1 ppm free chlorine:** ≈ 2× the 2-ppm numbers above → ≥99% ≈ 6,962 L, mandatory-replace ≈ 50,934 L ≈ 95.4 weeks (~2 years).
- **KDF contribution by flow rate (internal empirical coefficients):** 43% / 32% / 26% / 21% at 15 / 20 / 25 / 30 L/min respectively.
- **System total dechlorination (chain formula):** 1 − (1−KDF) × (1−CaSO₃). At flow 15 L/min with CaSO₃ at 99% stage, system = 99.43%; at 30 L/min same stage = 99.21%. Degrades to 60.5–71.5% when CaSO₃ hits its ≥50% point.
- **Replacement anchors:**
  - soft trigger: system total dechlorination drops to 90% (still good experience)
  - strong trigger: drops to 80% (entering rapid decay)
  - mandatory: drops to 50% (deemed failed)
- **Standards reference (for honesty, not certified-claim):** KDF55 has NSF/ANSI 42 certification from supplier; calcium sulfite is not NSF-certified (tested against NSF/ANSI 177 protocol). The product does NOT claim its own third-party certification; it invites user verification via included chlorine test strips and water-before/after comparison.
- **Anti-competitor framing — mixed-media vs. layered:** the category default is a mixed bead bed (channeling, cross-reaction, no segmented replacement, no diagnosability). KES uses strict PP / KDF / CaSO₃ layering with an inner flow-distribution reservoir + top overflow trough to force the water through each bed without impingement channeling.
- **Video demo script (30-sec retail floor):** whiteness → bubbles → chlorine test strip (strongest trust closure) → TDS pen to damp the "does it drop TDS?" objection.
- **FAQ anchors (verbatim positions):** (a) no, it does not reduce TDS/PPM; (b) dechlorination verified by chlorine strip / DPD reagent, not by TDS; (c) KDF is safety-layer + biofilm suppression, not marketed as a bacteria filter; (d) lifespan quoted in cumulative water / bath-fills / weekly-bath-count, not months.
- **Bath-fill size convention used throughout:** 70 US gallons full bathtub, 2/3 fill = 47 gal = 178 L; 3 baths/week = 12/month.

### From Doc 2 (Market research baseline, 2024-02-18 → costs 2025-09-14)
- **Market failure mode identified:** mixed-media bath-ball category has structural unpredictability — channeling (water takes the path of least resistance), media cross-reaction (fast-reactive like CaSO₃ next to adsorption-dominant like KDF degrades both), no ability to segment-replace, no ability to diagnose failure mode.
- **Cost breakdown, urban version, 2025-09-14:** housing $49.248 + KDF-55 110g 5–10 mesh $8.25 + CaSO₃ 130g 4–5mm $4.20 + 10-pack filter disc = $72.45; expected MP $36.84; additional 5–8 yuan accessory pack possible.
- **Cost breakdown, rural/softened-water variant:** housing $49.248 + KDF-85 110g 5–10 mesh $11.55 + activated carbon 60g $5 + 10-pack filter disc = $77 total.
- **Competitor teardown (5 ASINs):**
  - B008A4AG2U Crystal Quest Bath Ball, $64.95, ~3,684 BSR (re-estimated 2025-01 at ~3,100), 5,522 days on market, claims 2,500 gal / 12–18 months lifespan
  - B0742KFY9R Santevia-type cloth pouch, $22.99, ~1,600 BSR, the QA page glosses the fact that the filter is a mineral-stone + beads mix inside a loofah-lined pouch (many customers didn't know), 2-month lifespan
  - B08Y8GSVJS, $17.80, ~218 BSR, 30-use lifespan
  - B0C5D7NLC7, $36.97, ~267 BSR, 12-month lifespan with 2 filter discs (each 6 months), KDF55
  - B0012045EO, $39.95, ~724 BSR, 6,810 days on market, 12-month lifespan, KDF55 (classic baseline)
- **Top complaint themes mined from reviews:**
  - carbon/media shed during pre-rinse (B008A4AG2U, 17 reviews)
  - chrome finish peels into the tub (B008A4AG2U, 7 reviews)
  - doesn't hang on modern faucet / slides off / strap snaps (B008A4AG2U: 31 reviews; others similar)
  - overflow during fill (B008A4AG2U: 10; B0742KFY9R: 8; B08Y8GSVJS: 38; B0C5D7NLC7: 9; B0012045EO: 63)
  - chlorine test strip shows no change before/after (B008A4AG2U: 18; B0012045EO: 422 helpful votes on one review)
  - no test data provided by manufacturer — customers demand third-party verified chlorine / heavy-metal reduction %
  - B0742KFY9R: loofah in the pouch molded between uses
- **Top positive themes mined:**
  - purchased for infants/kids/eczema parents (B008A4AG2U: 31; B0012045EO: 94)
  - chlorine smell gone
  - skin / hair improvement
  - long lifespan and travel portability (4 reviews mention travel use)
- **Customer verification methods currently in use (from Q&A and reviews):** chlorine test strips, DPD free-chlorine reagent, TDS pen (misleading for this product), pH meter, HDX pool chlorine test kit, RPC water test strips.

### From Doc 3 (Activated carbon test log)
- **Industry sizing conventions:** bulk/columnar carbon is cited in mm; granular in mesh count. Finer mesh → smaller particle → higher adsorption rate, higher filtration precision, higher flow resistance, longer effective life.
- **Carbon variety comparison** (ash / hardness / iodine):
  - Coconut shell: 2–4% ash / ≥95% hardness / 1,000–1,200 mg/g iodine
  - Fruit-shell (walnut/peach/apricot): 3–5% / 85–90% / 900–1,100
  - Wood-based: 2–6% / 60–75% / 600–1,000
  - Coal-based: 5–15% / 50–75% / 600–900
- **Selection:** acid-washed coconut shell; ash down to ~0.5% (hardness slightly reduced but still highest class); price ~0.0145 yuan/g including acid wash.
- **Wash/commissioning test (20240730, 8–10 mesh, 50g):** 2-min pre-rinse removes initial powder; 0.3 MPa / 29 L/min through 200 L of water, output initially minor powder, clears. After 1-day drying and re-test (20240731 and again 20240807), no further powder shed.
- **Activated-carbon dose sizing calculation** (assumes KDF-55 does ~70% dechlorination at 2 mg/L chlorine, carbon iodine 1,200 mg/g, ash 0.5%, BET 1,110 m²/g, moisture 7.76%, bulk density 0.49 g/mL):
  - if KDF-55 handles 70% of chlorine load: carbon needed 12.8g (cost ~0.19 yuan)
  - if KDF-55 handles only 50%: carbon needed 21.33g (cost ~0.31 yuan)

### From Doc 4 (Flow / overflow / filter-disc stacking test, 2024-11-07)
- **Test config:** 204g KDF (10–40 mesh) + 45g acid-washed carbon (8–10 mesh), 0.5 MPa, instantaneous flow 38–40 L/min, 2/3 fill target 178 L.
- **No fiber filter disc at top:** overflow starts around 35 L/min; 263 L passes without overflow only at reduced flow; by fourth pass the media bed has compacted enough that overflow begins intermittently.
- **1 mesh + 1 non-woven fiber disc at top:** 35 L/min no overflow.
- **1 mesh + 2 non-woven fiber discs:** 35 L/min no overflow; adding a 3rd disc begins to cause overflow (flow restriction exceeds inlet). Optional third disc offered to users who want slower fill.
- **Behavioral note:** as carbon is not uniform, repeated water surge compacts the bed over time; a top fiber disc both diffuses the incoming jet (preventing channel erosion) and acts as visible "work indicator" for the user.
- **US typical tub spout output:** 18–25 L/min; the two-disc config is comfortably inside the no-overflow envelope.

### From Doc 5 (Diversion module vs. none, 2025-10-22)
- **Conclusion:** a top-of-chamber diversion module materially reduces the scouring jet from the spout, redistributes water across the full cross-section of the filter bed, and makes more of the water actually pass through the media instead of impinging the center and channeling around the edges.
- **KDF layer:** diversion vs. none shows no visible difference (KDF is coarse and dense enough to resist jet scour).
- **CaSO₃ layer:** without diversion, the jet creates a visible crater and erodes the center; with diversion, water distributes evenly across the bed.

---

## Classification

| attribute | value |
|---|---|
| source_type | internal-doc (KES first-party product development) |
| extraction_mode | structured internal product spec + engineering test log |
| domain | product |
| domains | bathtub-filter, kes-product-architecture, engineering-tests, sales-training, competitor-teardown |
| officiality_impact | high — supersedes "architecture hypotheses" framing and calibrates the concept brief + technology notes + claim register |
| verification_status | unverified-by-agent (first-party; owned by product strategist) |
| owner | product strategist (user) |
| date_provided | 2026-04-17 |

---

## Pages the strategist and I should consider updating (proposed, not executed)

Held at this stage pending strategist direction. The source-summary page lists the specific updates per target page.

- `wiki/products/bathtub-filter/bathtub-filter-kes-concept-brief-v1.md` — elevate from "concept candidate" language to "confirmed Version A architecture" for the urban/municipal route
- `wiki/products/bathtub-filter/bathtub-filter-kes-product-architecture-hypotheses.md` — archive or convert hypothesis list into a confirmation log
- `wiki/products/bathtub-filter/bathtub-filter-technology-notes.md` — add internal empirical flow/EBCT/KDF-coefficient data (currently relies on external literature only)
- `wiki/products/bathtub-filter/bathtub-filter-normal-flow-vs-reduced-flow-evidence-table.md` — add internal flow-sweep data from Doc 4
- `wiki/products/bathtub-filter/bathtub-filter-media-efficacy-at-bath-conditions.md` — add internal life model (η=0.9, 130g CaSO₃, bath-fill units)
- `wiki/products/bathtub-filter/bathtub-filter-claim-register.md` — populate allowed claims from Doc 1 (e.g., "≥99% in the fresh-filter best-experience segment at 15 L/min" with bounded language)
- `wiki/products/bathtub-filter/bathtub-filter-product-forms.md` — confirm the layered architecture vs. mixed-bed differentiation
- `wiki/products/bathtub-filter/bathtub-filter-compatibility-engineering-breakpoints.md` — confirm overflow envelope (≤35 L/min with 2-disc top stack)
- `wiki/playbooks/bathtub-filter-validation-testing-protocol.md` — Validation log entry: internal tests already covered (overflow, carbon pre-rinse, diversion); remaining gap is third-party dechlorination-by-EBCT and chlorine-strip-before/after at typical US tap concentrations

---

## Next action (for user to direct)

Strategist decision needed on whether to:
1. Proceed with the deeper wiki integration above (estimated ~9 page updates), or
2. Hold at source-summary level and direct which specific downstream updates to do first, or
3. First decide on how to split "Version A stable / compliant product" vs. any downstream "Version B / more-aggressive claims" branch (Doc 1 explicitly labels itself Version A 稳妥合规, implying a Version B exists or is planned).
