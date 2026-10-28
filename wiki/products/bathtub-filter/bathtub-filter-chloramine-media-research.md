---
type: product
status: draft
owner: product
created: 2026-04-17
updated: 2026-10-28
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, chloramine, filtration-media, evidence, research, KDF, catalytic-carbon, ascorbic-acid, NSF, contradiction-event]
source_count: 40
review_cycle: monthly
verification_status: spot-checked
related:
  - ./bathtub-filter-disinfectant-types-and-media-guide.md
  - ./bathtub-filter-evidence-bibliography.md
  - ./bathtub-filter-certification-and-testing-pathways.md
  - ./bathtub-filter-claim-register.md
  - ./bathtub-filter-technology-notes.md
  - ./bathtub-filter-supplier-report-zongli-calcium-sulfite-chloramine-2023-07.md
  - ../../source-summaries/bathtub-filter-caso3-chloramine-contradiction-event-2026-10-09.md
---

# 浴缸过滤器滤材的氯胺去除证据

## Purpose of This Page

This page documents quantitative empirical evidence on chloramine (specifically monochloramine, NH₂Cl) removal by filter media used in bath/shower water filters. The goal is to distinguish what is empirically demonstrated from what is industry assumption or marketing claim.

**Critical context:** US municipal systems using chloramines represent ~35–40% of the market. Standard media (KDF-55, calcium sulfite) that handle free chlorine well are widely believed to be largely ineffective for chloramines. This page gathers the best available evidence to support or contradict that belief, with source quality rated.

**Source quality tiers used in this document:**
- **Tier 1 — Peer-reviewed:** Published in indexed journal, DOI available, methods described
- **Tier 2 — Industry/technical:** Manufacturer technical data, trade press with quantitative data, standards bodies
- **Tier 3 — Secondary/consumer:** Industry blogs, product pages, consumer sources that cite Tier 1 or 2 sources but add no original data

---

## TL;DR — 两个关键结论（2026-06-15 提炼，细节见 §2 / §4）

> 全页核心可压缩成两句，且两句都指向同一个变量——**接触时间（EBCT / soak time）**。

### 结论 1：催化活性炭是固相除氯胺最可信的路线，但氯胺比游离氯「更难、更慢」是有 Tier 1 支持的事实
- **Tier 1**：Kochany & Lipczynska-Kochany (2008, *Water Environ Res* 80(4):339–345, PMID 18536485) —— 催化炭把单氯胺分解为 N₂；20°C 比 5°C 快得多。
- **「更慢」是量化的**：除单氯胺所需 EBCT = 标准 GAC ≥10 min / 催化炭 3–7 min，而游离氯几乎瞬时（<1 秒）。慢 2–3 个数量级，机理是「表面活性位的慢催化分解」vs 游离氯的「快速吸附/还原」（Jacobi 柱测：催化炭击穿时间 5×、去除率 +65%）。
- **设计含义**：单一 compact 滤芯在 bath-fill（更别说 25 L/min）下 EBCT 不够 → 催化炭「必要但不自动充分」。

### 结论 2：维C / 抗坏血酸钠**能**中和氯胺，但**不是「快」**——文献的表面矛盾由「接触时间」化解
- **表面矛盾**：Basu & De Souza (2011, Tier 1, *Aqua* 60(3):167–177) 测得抗坏血酸对单氯胺**「无效」**；而 SFPUC（Tier 2 政府）+ AWWA C655 认定 1,000 mg 维C 在 40 加仑浴缸里**完全去除**单氯胺。
- **化解 = 接触时间**：维C 对**游离氯**瞬时；对**氯胺需要 4–8 分钟**。Basu 的「无效」反映**短接触/inline**条件；SFPUC 的「完全去除」靠**浴缸 4–8 分钟停留**。淋浴（<1 秒）实测零效果，浴缸恰好够。
- **精确表述**：不是「维C 快」，而是「**浴缸 format 提供了维C 需要的 4–8 分钟窗口**」——这正是浴缸相对淋浴的结构性优势。
- **claim 纪律**：可防守 = 「在注水+浸泡阶段中和氯胺」（SFPUC + AWWA 背书）；**不可说**「快速」或用淋浴/纯 inline 单芯主张。抗坏血酸钠 > 抗坏血酸（中性、不降 pH）。

### 对 KES 的合流结论
双段方案（**inline 催化炭先降一部分 + 缸内抗坏血酸钠浸泡件利用停留完成**）有 **Tier 1（Kochany）+ Tier 1 机理（Basu/Yiin）+ 政府（SFPUC）+ 标准（AWWA C655）** 多层背书，是氯胺版 V1.5 配置的科学基础。两段都在用「时间换去除率」，而浴缸是唯一天然提供这段时间的 format。

---

## 1. KDF Media (KDF-55, KDF-85) and Chloramine Removal

### Summary verdict: Largely ineffective for monochloramine at practical flow rates

**Mechanism of action for free chlorine:**
KDF (Kinetic Degradation Fluxion) is a 50:50 copper-zinc alloy (KDF-55) or 85:15 copper-zinc alloy (KDF-85) that removes free chlorine via a galvanic/redox reaction: Cl₂ + Zn → Zn²⁺ + 2Cl⁻. This electrochemical mechanism is highly effective for free chlorine (HOCl, OCl⁻).

**Why chloramine is different:**
Monochloramine (NH₂Cl) has a much lower oxidation potential than free chlorine. The N–Cl bond in NH₂Cl is not readily reduced by the Cu-Zn galvanic couple at the reaction rates achievable in a filter cartridge. KDF Fluid Treatment, Inc. itself has acknowledged that monochloramine's low degradation rate makes it persistent and challenging for KDF media to handle.

### Quantitative test data found

**Test 1 — KDF-55 alone (Pure Water Gazette, industry testing, Tier 2):**
- What was tested: 1.5 lbs of KDF-55 in a cartridge (no carbon), 1 gpm flow rate
- Result: **18.2% chloramine reduction**
- Conditions: Municipal chloraminated water, flow rate 1 gpm
- Conclusion by tester: "KDF, unless it is followed by carbon, is not an effective chloramine treatment"
- Comparison: A MatriKX CTO Plus carbon cartridge after the same KDF achieved 97.7% reduction — demonstrating the carbon, not KDF, was responsible for chloramine removal
- Source: Pure Water Gazette, industry blog citing test data — [KDF and Chloramines](http://www.purewatergazette.net/blog/kdf-and-chloramines/)
- **Quality: Tier 2 (industry testing, non-peer-reviewed; no methodology publication)**

**Note on KDF-85 (from same source, Tier 2):**
KDF-85 reportedly showed even worse chloramine removal than KDF-55 (the disinfectant-types guide elsewhere in this wiki cites 1.4% for KDF-85). The mechanism makes this plausible: KDF-85 has a higher copper fraction (85%), meaning less zinc available for the reductive reaction that free chlorine relies on.

**KDF Fluid Treatment's own research (Tier 2):**
Kymera International (the KDF manufacturer) lists on their website a study titled "Reductive Dechloramination: Finalized Study of KDF® 85 in POE and POU Applications." The company acknowledges investigating KDF-85 specifically as a monochloramine reductant, establishing operating parameters. However, the full study PDF is not publicly extractable, and no removal rate data is available in the public domain from this source. The existence of the study implies KDF-85 can have some effect under optimized POE conditions but the consumer-cartridge data (18.2%) is the only publicly available quantitative figure.
- Source: [KDF Research Page, Kymera International](https://kdf.kymerainternational.com/research)

**Peer-reviewed literature (Tier 1):**
A search of PubMed and Google Scholar found **no peer-reviewed studies specifically measuring KDF-55 or KDF-85 chloramine removal efficiency** in consumer-filter conditions. One ScienceDirect paper used KDF media in multi-layer filters but focused on biological and heavy metal reduction, not chloramine. The absence of Tier 1 data for KDF + chloramine is itself a significant finding.

### Temperature effects on KDF and chloramine
No quantitative data found for temperature effects on KDF chloramine removal specifically. For free chlorine removal, KDF-55 is cited as effective from 55°F to over 100°F — but this electrochemical property does not extend meaningfully to the different NH₂Cl reduction problem.

### Contact time
At shower flow rates (~2 gpm through a small cartridge), contact time is under 1 second. The 18.2% removal figure above was at 1 gpm — a relatively slow flow. Higher flow rates will produce even lower removal.

---

## 2. Catalytic Activated Carbon and Chloramine Removal

### Summary verdict: Catalytic carbon is the only credible solid media route for inline chloramine reduction, but bath-spout cartridges still face severe contact-time constraints (EBCT ≥ 4–5 min for catalytic; ≥10 min for standard GAC)

**Mechanism:**
Standard activated carbon removes free chlorine primarily via adsorption and surface reduction. For monochloramine, the mechanism is catalytic decomposition at active surface sites:
- Step 1: NH₂Cl + H₂O + C* → NH₃ + H⁺ + Cl⁻ + CO* (catalytically active site creates carbon-oxide intermediate)
- Step 2: NH₂Cl + CO* → N₂ + 2H⁺ + 2Cl⁻ + H₂O + C* (intermediate further decomposes chloramine)

Byproducts are ammonia, chloride, nitrogen gas — no chlorinated organics. Catalytic carbons have surface sites specifically engineered (via steam activation under specific conditions) to enhance this reaction; standard GAC has fewer such sites.

### Key peer-reviewed study (Tier 1)

**Kochany & Lipczynska-Kochany (2008) — Two-stage process:**
- Full citation: Kochany J, Lipczynska-Kochany E. "Catalytic Destruction of Chloramine to Nitrogen Using Chlorination and Activated Carbon — Case Study." *Water Environ Res.* 2008 Apr;80(4):339–45. PMID: 18536485
- DOI: Available via PubMed (18536485)
- What was tested: Pre-chlorination of water at sub-breakpoint chlorine doses, followed by catalytic activated carbon treatment
- Variables: Cl:N ratios, temperature (5°C vs 20°C), contact time (5, 10, 15, 20, 30 minutes)
- Key results:
  - At 7:1 Cl:N ratio, "practically all monochloramine was destroyed" at both temperatures
  - At 20°C, monochloramine removal rates were significantly higher than at 5°C
  - Main product was nitrogen gas (not ammonia), eliminating need for separate ammonia removal step
  - The two-stage approach was described as "simple and cost-effective"
- **Relevance to bath filters:** This is a two-stage industrial process (pre-chlorination + catalytic carbon), not a single-stage consumer filter. The temperature data (worse at 5°C) is relevant: bath water ~38–40°C should favor faster reaction.
- **Quality: Tier 1 (peer-reviewed, indexed)**

### Industry/technical data on EBCT (Tier 2)

**Standard GAC vs. catalytic carbon EBCT comparison:**

| Carbon type | EBCT for chloramine removal | Notes |
|---|---|---|
| Standard GAC | ≥10 minutes minimum | Breakthrough often within 10 min column test |
| Catalytic carbon (coal-based) | 4–7 minutes | Improved surface sites |
| Catalytic carbon (coconut-based, e.g., Jacobi CX-MCA) | ~3–5 minutes | Best chloramine performance; highest catalytic activity |

Sources: 
- Everfilt technical article: EBCT table showing chloramines require 4–10 min for catalytic carbon — [Everfilt: What Is Catalytic Carbon](https://www.everfilt.com/post/what-is-catalytic-carbon-understanding-ebct-why-it-matters-in-water-filtration)
- WCP Online (trade press): "At least two to four times more EBCT will be required for monochloramine removal with traditional GAC" — [Activated Carbon Chlorine & Chloramine Removal, WCP Online](https://wcponline.com/2009/06/13/chlorine-chloramine-removal-activated-carbon/)

**Column test data (Jacobi / industry, Tier 2):**
- Test protocol: ANSI-NSF 42-2002, 25 cm³ bed, 2.5 cm column, 3.3 bed volumes/min, pH 9, ~3 mg/L inlet chloramine
- Jacobi AquaSorb CX-MCA (coconut catalytic) vs. standard coal GAC: **65% improvement in chloramine reduction** after treating 10,000 bed volumes
- Same product vs. catalytic coal-based carbon: **24% improvement** after 10,000 bed volumes
- Source: [Jacobi Carbon 101 — Chloramines](https://www.jacobi.net/chloramines/)
- **Quality: Tier 2 (manufacturer test data using NSF 42 protocol, not independently published)**

**WaterWorld/Filtrex Technologies comparative column test (Tier 2):**
- Standard GAC carbon block: breakthrough within 10 minutes
- Catalytic carbon block: breakthrough at 50 minutes (5× longer)
- Peroxide decomposition capacity as proxy: standard GAC ~20%; catalytic carbon >95% under identical 10-min contact time
- Source: [WaterWorld — Catalytic Carbon for Chloramine Removal](https://www.waterworld.com/residential-commercial/article/14309145/filtrex-technologies-usa-catalytic-carbon-for-chloramine-removal)
- **Quality: Tier 2 (manufacturer/trade press, testing methodology described but not peer-reviewed)**

### Temperature effects on catalytic carbon and chloramine

**From peer-reviewed data (Kochany 2008):** Monochloramine removal was faster at 20°C than 5°C. Bath water (~40°C) is above the 20°C test temperature, suggesting bath conditions should be favorable for catalytic carbon — though no study has directly tested catalytic carbon at bath-water temperatures (~38–42°C).

**Implication:** Bath fill conditions (warm water, 5–10 minute fill time, catalytic carbon in the filter path) are structurally more favorable for chloramine removal by catalytic carbon than shower conditions (cold-to-warm, <1 second contact time).

### Bath filter vs. shower filter contact time analysis

| Application | Typical flow rate | Filter path volume | Approx. EBCT |
|---|---|---|---|
| Shower filter (standard) | 2 gpm through small cartridge | ~50–100 mL carbon | <0.1 min (<6 sec) |
| Bath spout filter (2 gpm flow) | 2 gpm through larger bed | ~300–500 mL carbon | 0.5–1.5 min |
| Bath fill (low flow, large bed) | 0.5–1 gpm | 300–500 mL | 2–5 min |

**Key insight:** Even a bath spout filter at normal bath-fill flow rates falls short of the 4–5 minute EBCT recommended for catalytic carbon to reliably remove chloramines. The contact time advantage of a bath filter over a shower filter is real but may still be insufficient without significant media volume or reduced flow rate.

### Practical design implication for bathtub filters

For KES, the evidence now supports a narrower conclusion than the generic phrase "catalytic carbon removes chloramine":

- **Yes, catalytic activated carbon is the most credible inline media for monochloramine.**
- **No, a normal small bath-ball / compact spout cartridge should not assume that catalytic carbon alone is enough.**

At bath-fill flows, catalytic carbon becomes plausible only when at least one of the following is true:

1. **Large carbon bed volume** — closer to a mini-canister / external housing than a compact ornament-sized cartridge
2. **Reduced flow** — roughly the 0.5–1.0 gpm range, not wide-open tub-spout flow
3. **Hybrid chemistry** — catalytic carbon handles part of the inline load, while a dissolved reductant such as sodium ascorbate finishes the reaction in the tub during the 4–8 minute standing period

### KES-specific verdict

For a chloramine-city bathtub SKU, the most defensible design posture is:

- **Do not rely on KDF or calcium sulfite**
- **Do not rely on standard GAC**
- **Treat catalytic carbon as necessary but not automatically sufficient**
- **Prefer a hybrid route: catalytic carbon inline + bath-compatible vitamin C / sodium ascorbate finishing step**

This is a stronger engineering position than the current shower-filter market pattern of putting a token amount of carbon into a cartridge and broadly claiming "chloramine removal."

---

## 3. Calcium Sulfite (Bisulfite) and Chloramine Removal

### Summary verdict: Effective for free chlorine; not chemically suited for monochloramine at neutral-to-alkaline pH — **but see Section 3.5. This verdict's stated basis has been challenged as of 2026-10-09.**

> ⚠️ **2026-10-09 status change (updated 2026-10-28).** The verdict above was reached partly on an inference from absence of data (see Section 7, Gap 2). Two new uncontrolled observations — a supplier report and a KES first-party bench test — both pointed the other way. **2026-10-28: the KES bench test is removed from that count** — its challenge species was never established, so it is not a chloramine observation ([raw pass](../../../raw/products/bathtub-filter/2026-10-28-caso3-2026-10-09-reagent-identity-check.md)). One uncontrolled observation remains. The verdict may still be correct, but it is not supported by a clean evidence base. Read Section 3.5 before relying on this section.


**Mechanism for free chlorine:**
Calcium sulfite (CaSO₃) reacts with free chlorine via direct chemical reduction: CaSO₃ + Cl₂ + H₂O → CaSO₄ + 2HCl. This is fast, efficient, and effective at all shower temperatures. It is the mechanism behind Sprite's Chlorgon media and most calcium sulfite shower filters.

**Why monochloramine is different:**
The N–Cl bond in NH₂Cl is not readily reduced by SO₃²⁻ (sulfite anion) at neutral or alkaline pH typical of municipal water (pH 7–8.5).

### Key chemistry study (Tier 1)

**Yiin, Walker, and Margerum (1987):**
- Full citation: Yiin BS, Walker DM, Margerum DW. "Nonmetal redox kinetics: general-acid-assisted reactions of chloramine with sulfite and hydrogen sulfite." *Inorganic Chemistry.* 1987;26(21):3435–3441
- DOI: 10.1021/ic00268a006
- What was measured: Rate constants for NH₂Cl reaction with SO₃²⁻ (sulfite) and HSO₃⁻ (bisulfite/hydrogen sulfite) at various pH values
- Key finding: Reaction rate for chloramine + sulfite is strongly pH-dependent and is significantly **slower at alkaline pH** (pH 7–8.5, typical of municipal water) than at acidic pH
- Practical implication: At pH 8.5, sodium bisulfite was "ineffective at reducing chloramines and then maintaining an entirely reduced state"
- At acidic pH (4.0), the reaction is fast (SBS reduces 4 ppm chloramine rapidly)
- **Quality: Tier 1 (peer-reviewed, indexed in Inorganic Chemistry)**

### Industry technical data (Tier 2)

**Stoichiometry from AWWA guidance:**
- 2.0 mg sodium bisulfite (SBS) removes 1.0 mg monochloramine (stoichiometric)
- In practice, 2.0–4.0× stoichiometric excess is required due to slower reaction kinetics
- At pH > 7.5–8.0, SBS can become ineffective for complete chloramine removal
- Source: Industry/trade sources citing AWWA dechlorination guidance; [Alliance Chemical — Sodium Bisulfite Dechlorination Guide](https://alliancechemical.com/blogs/articles/an-engineers-guide-to-sodium-bisulfite-for-dechlorination)

**Calcium sulfite specifically (Tier 3):**
No peer-reviewed study found specifically measuring CaSO₃ performance against NH₂Cl. The AquaBliss product page for calcium sulfite does not mention chloramine removal at all — it only describes free chlorine performance. Multiple industry sources state calcium sulfite "only handles chlorine, not chloramine."

The chemistry inference: CaSO₃ dissolves slowly into Ca²⁺ and SO₃²⁻. The SO₃²⁻ anion faces the same pH-dependent rate limitation against NH₂Cl as sodium sulfite. At the contact times available in a shower filter (<1 second) and at neutral-to-alkaline municipal water pH, calcium sulfite chloramine removal is expected to be negligible.

**No public peer-reviewed quantitative data found** for CaSO₃ + NH₂Cl removal rate in any peer-reviewed or high-quality industry source. The absence is meaningful: if calcium sulfite worked reliably for chloramine under practical high-flow inline conditions, manufacturers would normally measure and publicize it.

### Supplier-provided test signal added 2026-06-17

New supplier material was archived as [[bathtub-filter-supplier-report-zongli-calcium-sulfite-chloramine-2023-07]]. It reports 50g 宗立 2-3mm 亚硫酸钙球 tested at 3 L/min and 5 L/min with high removal of 一氯胺 and the source document's `三氯铵`.

Extracted results:
- 5 L/min, 300L: 一氯胺 0.46 -> 0.0184 mg/L, 96% removal; `三氯铵` 1 -> 0 mg/L, 100% removal.
- 5 L/min, 500L: 一氯胺 0.341 -> 0.023 mg/L, 93.26% removal; `三氯铵` 0.728 -> 0 mg/L, 100% removal.
- 3 L/min, 300L and 500L: both reported as 100% removal for 一氯胺 and `三氯铵`.

Evidence status: useful supplier screening signal, but not enough to revise the main conclusion or claim boundary yet. The report does not provide full analytical method, detection limit, pH, water temperature, replicate count, contact time, or third-party lab accreditation in the extracted text. It also uses the wording `三氯铵`, which should be confirmed with the supplier before treating it as `三氯胺 / trichloramine`.

KES implication: this result should become a follow-up verification item for KES bench testing, especially against target bathtub-fill flow and contact-time conditions. Until KES reproduces it, do not use it as public proof that calcium sulfite removes chloramine in normal bathtub-fill use.

> **2026-10-09 correction to the paragraph above.** The inference in the bolded sentence — "the absence is meaningful" — is the specific logical step that Section 3.5 invalidates. A manufacturer not having publicized a result is not evidence that the result is negative; it is only evidence that the supplier chose not to run or not to disclose the test. Two data points now exist, and they point the other way. Treat the Tier-1 Yiin (1987) chemistry as the load-bearing evidence for this section, and **not** the argument-from-silence.

---

## 3.5 Contradiction event (2026-10-09): uncontrolled observations against the Section 3 verdict

> Source: [来源摘要｜亚硫酸钙 × 氯胺 矛盾事件（2026-10-09）](../../source-summaries/bathtub-filter-caso3-chloramine-contradiction-event-2026-10-09.md)
> Raw extraction: [2026-10-09-caso3-chloramine-contradiction-pass.md](../../../raw/products/bathtub-filter/2026-10-09-caso3-chloramine-contradiction-pass.md)
> **2026-10-28 更新（试剂身份回查完成）**：本节原为「**两个**方向相反的无对照观测」。其中 KES 一方 bench test 的**加标液物种身份不可确认**，已退出氯胺证据 —— **现在只剩供应商报告一条**。KES 自有的氯胺数据点为 **0**。详见 [raw pass](../../../raw/products/bathtub-filter/2026-10-28-caso3-2026-10-09-reagent-identity-check.md) 与本节末「2026-10-28 追记」。


### What arrived

> Note: data point 1 was already archived on 2026-06-17 ([[bathtub-filter-supplier-report-zongli-calcium-sulfite-chloramine-2023-07]]) and assessed there as a *signal worth validating*. What is new on 2026-10-09 is data point 2, the quantitative critique of both, and the contradiction-event framing.

**1. Supplier report `ZONET20230707001`** — 淄博宗立 internal lab, sample received 2023-07-07, completed 2023-07-13. Sample: 沐浴过滤器 with 内置滤料为50g宗立（2-3mm）亚硫酸钙球. Test: 加标测试(氯胺), outlet flow 5 L/min and 3 L/min.

| Cumulative L | Flow | Species | In (mg/L) | Out (mg/L) | Removal % |
|---|---|---|---|---|---|
| 300 | 5 L/min | 一氯胺 | 0.46 | 0.0184 | 96 |
| | | 三氯铵 | 1 | 0 | 100 |
| 500 | | 一氯胺 | 0.341 | 0.023 | 93.26 |
| | | 三氯铵 | 0.728 | 0 | 100 |
| 300 | 3 L/min | 一氯胺 | 0.43 | 0 | 100 |
| | | 三氯铵 | 1 | 0 | 100 |
| 500 | | 一氯胺 | 0.341 | 0 | 100 |
| | | 三氯铵 | 0.728 | 0 | 100 |

**2. KES first-party bench test (reported 2026-10-09; run on or before 2026-09-24)** — 4 ppm chloramine water through **130 g CaSO₃** (Version A loading), **24 L/min**, **60 s**, **38 °C**, read near-zero on a 总氯比色卡 (0.1–10 mg/L).

> **2026-10-28 reclassification.** This challenge's species was never established. The operator's own words on 2026-10-12: the solution was *"mixed by another method — there is no laboratory chloramine standard — and it is possible what we made is wrong"*; on 2026-10-14 he stated that the only "chloramine" reagent KES holds is **chloramine-T**, and that *"this chloramine cannot be confirmed as monochloramine or whatever"*. **This data point is therefore reclassified as an unidentified-species chlorine spike test, presumptively exercising free-chlorine removal, and carries zero information about chloramine.** It is no longer counted as a chloramine observation. Full record: [raw pass](../../../raw/products/bathtub-filter/2026-10-28-caso3-2026-10-09-reagent-identity-check.md).


### Why these two do not overturn the verdict — and why they still matter

Neither test is capable of supporting a chloramine claim. Four disqualifying properties:

| Property | ZONET20230707001 | KES bench test |
|---|---|---|
| **pH not reported** | ✗ | ✗ |
| **No influent-only decay control** | ✗ | ✗ |
| **Species-specific method** | ✗ not stated | ✗ total-chlorine strip, not chloramine-specific |
| **Detection limit stated** | ✗ | ✗ (card low end 0.1 mg/L) |
| **Capacity utilization** | **0.61%** | **0.13%** |
| **EBCT** | ≈0.60 s @5 L/min; ≈1.00 s @3 L/min | **≈0.33 s** |
| **Replicates** | none | n = 1 |
| **Challenge species established** | partly (一氯胺 named; `三氯铵` label in doubt) | **✗ — never established (2026-10-28)** |

The capacity-utilization figures are computed from the disclosed media mass, the CaSO₃ bulk density of 0.9–1.1 g/cm³ from the Onlyzone brochure, and the stoichiometry 1 mol SO₃ per mol NH₂Cl (1.19 g SO₃ / g NH₂Cl). **Both tests consume well under 1% of the media's theoretical capacity.** They are existence proofs at large reagent excess — the weakest available form of efficacy evidence, and unscaleable into any life model.

**Sharpest defect in the supplier report — the decay confound.** The influent is not constant:

| Species | 300 L | 500 L | Change |
|---|---|---|---|
| 一氯胺 | 0.46 | 0.341 | **−25.9%** |
| 三氯铵 | 1.0 | 0.728 | **−27.2%** |

Both species decayed ~26% over the run, with no influent-only blank at matched timestamps. A self-decaying spiked solution produces exactly this signature — and also produces `0` effluent readings. Nothing in the report separates media removal from spike decay.

**Sharpest defect in the KES test — the challenge species was never established (2026-10-28, superseding the original reading of this defect).** The original note on this test was method non-specificity: a 总氯比色卡 responds to total chlorine, free chlorine was never measured, so a near-zero reading could not be attributed to chloramine. That defect stands — but it turned out to be the **second** defect, not the first. The first is upstream of it: **nothing in any record identifies what was dosed.** The reagent name, CAS number, mix ratio, and pH were never written down; the operator stated on 2026-10-12 that the solution was self-mixed without any laboratory chloramine standard and *"it is possible what we made is wrong"*, and on 2026-10-14 that the only chloramine reagent KES holds is chloramine-T and that *"this chloramine cannot be confirmed as monochloramine or whatever"*. "接近 0" therefore means **≤0.1–0.2 mg/L of total chlorine on a 0.1 mg/L-floor card** — of an unidentified species.

**On the photographic record (2026-10-28 correction).** An earlier version of this page stated that the three photos are *"internally inconsistent"* because the second, captioned 原水 ("raw water"), reads clearer than the first, captioned 4 ppm 绿氨水, and that "both captions cannot describe the same water". **That inference was wrong and is withdrawn.** 原水 is unspiked tap water — which is clear (the operator: *"our tap water is 0.x, it basically doesn't colour"*); the 4 ppm spike is pink; the filtrate is clear. **The three photos match the stated protocol step for step, and there is no contradiction.** The real limitation is narrower: photos 2 and 3 are both colourless and cannot be told apart by eye, so **the photos still cannot establish before/after on their own** — because they cannot be distinguished, not because the captions conflict.

> **A second, smaller correction — the influent number is a label, not a measurement.** The card has swatches at 0.1 / 0.2 / 0.5 / 1 / 2 / 5 / 10 and **no 4 swatch**; a nominal 4 ppm sample should sit between the 2 and 5 swatches. The 2026-10-09 pass placed it at "2–5"; a re-inspection on 2026-10-28 lands closer to 1–2. **Two independent eyeball reads of the same frame disagree**, so the photograph does not fix the influent concentration — "4 ppm" is the operator's label, nothing more. (The 2026-10-15 report shows the same pattern: nominal 2 ppm against a 0.5–1 ppm card read. Both challenges read 2–4× below nominal. Dilution error, chlorine loss after mixing, and systematic card under-reading are all unexcluded — which is why Module 7 now requires nominal concentrations to be read out by a species-specific method rather than computed from a mix ratio.)

### The point that was recorded as favouring the hypothesis — withdrawn (2026-10-28)

> **Withdrawn.** This section previously said: *"The KES bench test ran at roughly one-third the contact time of the supplier's slowest point (≈0.33 s vs ≈1.00 s), at production media mass, at production bath-fill flow, and at bath temperature. If the supplier's result is real, the KES result is the harder case to explain. This should not be discarded — it is the strongest pro-evidence argument available."*
>
> **Why it no longer holds.** That argument only had force if the near-zero reading was chloramine removal under adverse conditions. With the challenge species unidentified and presumptively free-chlorine, the same reading is **what KES's own free-chlorine data predicts**: 2026-03-20, 5 ppm free chlorine, 16.5–30 L/min, **84–90% removal** ([[bathtub-filter-25lpm-dechlorination-bench-test-spec]]). A near-zero result from an unidentified challenge that was most likely free-chlorine-generating is **not a hard case to explain — it is the expected case.** It carries no weight for the chloramine hypothesis, and the argument must not be cited.


### Why the Section 3 verdict is nonetheless no longer adequately grounded

Section 7 Gap 2 states the basis plainly: *"No peer-reviewed study measuring CaSO₃ + NH₂Cl reaction rate. **The expected ineffectiveness is inferred.**"*

> **2026-10-28 update — this now rests on one observation, not two.** The KES bench test has been removed from the count (its challenge species was never established). One uncontrolled observation still runs against the inference: the supplier report, which names 一氯胺 explicitly. It is a weak observation — no pH, no control arm, no analytical method, no detection limit, influent decaying ~26% across the run, and a removal-percentage column arithmetically back-calculated from the inlet/outlet pair. **But it does mean the wiki cannot say "CaSO₃ does not remove chloramine — established".** What it can say is "uncontrolled, method-less, pH-less — contested and unresolved".


Neither Tier 1 anchor was retracted:
- **Yiin et al. (1987)** — sulfite/bisulfite + NH₂Cl is general-acid-assisted and strongly pH-dependent; ineffective at pH 8.5, fast at pH 4.0. **Neither new data point reports pH**, so the report cannot distinguish (a) an acidic-pH test that is real chemistry and irrelevant to pH 7.5–8.5 municipal water, from (b) a genuinely effective result at municipal pH that contradicts the Tier-1 anchor for CaSO₃ specifically.
- **Basu & De Souza (2011)** — ascorbic acid ineffective for monochloramine under short-contact conditions. Unaffected by this event.

### Species-naming risk that must be resolved before any citation

**三氯铵 (nitrogen trichloride, NCl₃) at 0.728–1.0 mg/L is not a realistic drinking-water species.** NCl₃ is a trace chlorination byproduct reported at ng/L–µg/L in distribution systems — roughly three orders of magnitude below the challenge concentrations here — and is unstable in concentrated form. Either the supplier means **二氯铵 (dichloramine, NCl₂H)** and has mislabeled it, or the challenge is unrepresentative.

This matters because [[bathtub-filter-disinfectant-types-and-media-guide]] has already scoped dichloramine and trichloramine out of the product model. If the label is wrong, the four `100%` results in this report belong to a species KES has never modeled. **Written clarification from the supplier is required before this report is cited anywhere.**

### Position adopted (2026-10-09)

| Item | Decision |
|---|---|
| Section 3 conclusion "not chemically suited for monochloramine" | **Not reversed.** Retained provisionally, now flagged as resting on Tier-1 chemistry alone rather than on any KES- or supplier-held evidence. |
| Summary table CaSO₃ row (Section 6) | **Re-labelled** ❌ → ⚠️ with explicit "uncontrolled, unresolved" wording |
| Section 7 Gap 2 | **Reframed** from "no data exists" to "no *controlled* data exists" |
| Claim-register banned zone | **Unchanged — stays banned.** Reason recorded against it is updated. |
| Version A life model | **Unchanged.** Free-chlorine model only. |
| Assumption A-14 (chloramine geos deferred) | **Unchanged.** It was never a chemistry assumption. |
| New R&D item | **Opened** — see below |

### Position adopted (2026-10-28, after the reagent-identity check)

| Item | Decision |
|---|---|
| KES first-party bench test (reported 2026-10-09) | **Removed from the chloramine evidence count.** Challenge species never established; reclassified as an unidentified-species chlorine spike test, presumptively free-chlorine. Zero chloramine information. |
| "Two opposing observations" | **Withdrawn.** The contradiction event now rests on the supplier report alone. |
| The "hardest case to explain" pro-evidence argument | **Withdrawn** — it described free-chlorine removal, which KES's own data already predicts. |
| "Photos are internally inconsistent" | **Withdrawn as a misreading.** The photos match the protocol step for step; the surviving limitation is that two colourless tubes cannot be told apart by eye. |
| Summary table CaSO₃ row (Section 6) | **Stays `⚠️ Untested`**, but the supporting text changes from "two uncontrolled observations" to "one uncontrolled supplier observation; KES has produced no species-identified chloramine data point". |
| Section 7 Gap 2 / Gap 6 | Gap 2 stays "no *controlled* data" with the count corrected to one; Gap 6 sharpened — **no KES run has ever had its challenge species confirmed in writing.** |
| Claim-register banned zone | **Unchanged — stays banned.** Reason updated again (now: one uncontrolled observation, no KES-side data at all). |
| Section 3 conclusion, Version A life model, A-14 | **All unchanged.** |
| R&D item | **Still open**, and its scope is now sharper: one uncontrolled observation to settle, not two. |

**Why `⚠️` survives and does not revert to `❌`:** the argument-from-silence in Gap 2 was always invalid, and the supplier report is a species-named observation, however weak. **What changed is the count of evidence for the hypothesis, not its existence.** Reverting to `❌` would restore an inference that the wiki has already admitted was never an inference.

> **Owner sign-off (2026-10-28, same day):** the position above was **accepted** by the product owner. Also confirmed the same day: **no "除氯胺 / chloramine removal / 秒去" wording is in circulation on packaging or e-commerce pages.** The 09-24 architecture statement ("直接亚硫酸钙即可，无需要 ACF") is left open for product review — its evidentiary basis is now empty, but re-opening it is a product judgment, not an agent call.

### The control that would settle it

Both tests fail on the same root cause: they measure the species they are trying to remove, using a method that the same species can independently degrade.

> **Chloride mass balance.** If chloramine is genuinely reduced, every mole of NH₂Cl destroyed releases one mole of Cl⁻. Ion chromatography for chloride is cheap, mature, species-blind, and completely immune to the spike-decay confound — it measures the **product** of the reaction, not the substrate. Measure Cl⁻ in, Cl⁻ in the media-free blank at matched time/temperature, and Cl⁻ out. If effluent chloride rises by exactly the amount the color card implies was removed, the claim is real. If not, the colour drop was decay or interference.

Minimum decisive protocol: 4 arms (media + challenge / challenge without media at matched time and temperature / inert media of matched bed volume and ΔP / production-spec 3–4 mm `ZONE-CL-A02 Gen-3` at 130 g), pH controlled and reported at 7.0 / 7.8 / 8.5, temperature at 20 / 38 / 42 °C, a **throughput series run to breakthrough** rather than single points, n ≥ 3, and DPD amperometric free/combined differentiation in addition to IC chloride. Full specification in [[bathtub-filter-validation-testing-protocol]].

### Third data point (2026-10-15): the challenge species was the wrong compound

> Source: [来源摘要｜氯胺T 实测报告评估（2026-10-15）](../../source-summaries/bathtub-filter-chloramine-T-measurement-2026-10-15.md)

A third KES first-party test was run on 2026-10-15. It reports **no chloramine removal** — the reading does not fall: 0.5–1 ppm at start, 0.5–1 ppm at 178 L, then 1 ppm at 356 L, 712 L and 1068 L. Flow 19 L/min, 29 °C, total-chlorine color card.

**This one is more consequential than a null result, because the challenge species was misidentified.** The reagent was **chloramine-T** (CAS 127-65-1, N-chloro-*p*-toluenesulfonamide sodium) — a **solid slow-release disinfectant that hydrolyses in water to hypochlorous acid (HOCl)**. It is **not monochloramine** (CAS 10599-90-3, NH₂Cl), which is the species actually present in chloraminated municipal water.

| | Chloramine-T | Monochloramine |
|---|---|---|
| CAS | 127-65-1 (anhydrous; trihydrate 7080-50-4) | 10599-90-3 |
| Formula | C₇H₇ClNNaO₂S (MW 227.64) | NH₂Cl (MW 51.47) |
| Nature | Solid **organic chloramine derivative** (sodium salt of N-chloro-*p*-toluenesulfonamide) | Chlorine–ammonia reaction product in treated water |
| In water | **Hydrolyses to HOCl / OCl⁻** (reactivity similar to sodium hypochlorite); acts as available chlorine, slow release | Is itself the combined-chlorine residual |
| Solution pH | **Slightly basic — pH typically 8.5** | Varies with dosing |
| Designed for | Medical / instrument surface disinfection (antiseptic, disinfectant); drinking-water and pool disinfection are vendor- and industry-level claims | Municipal secondary disinfection |

The Spanish Wikipedia entry (*Cloraminas*) actually reads: *«La Cloramina-T se denomina cloramina, pero es realmente una sal (CH₃C₆H₄SO₂NClNa) derivada de una cloramina.»* — Chloramine-T is named "chloramine" but is really a salt derived from one.

> **Correction (2026-10-28, wording review).** This section previously carried a Spanish Wikipedia quotation — *"no debe ser confundida con monocloramina"* — that **cannot be located on es.wikipedia** (MediaWiki `insource` search returns 0 hits; an exact-phrase web search returns 0 hits). The quotation is removed and replaced with the sentence above. Two further fixes: the solution pH was recorded as "8–10 (alkaline)" with no source behind that range — en.wikipedia gives "slightly basic (**pH typically 8.5**)" and the 8–10 range traces to a Chinese popular-science secondary source whose original text could not be re-verified — so the page now states pH ~8.5; and the CAS numbers are now backed by registry records (PubChem CID 3641960 → 127-65-1, CID 25423 → 10599-90-3). The dosing ratio that used to sit here without a citation (**Cl₂:NH₃-N ≈ 4.5:1**) was checked and is **correct in direction and magnitude** (In-Situ: optimum 4.5:1, utilities run 3:1–5:1; Snoeyink & Jenkins via Curry & Associates: stoichiometric 5.06 mg Cl₂ per mg NH₃-N), and now carries those citations. Full review record: [[bathtub-filter-disinfectant-types-and-media-guide]] §1b-bis.

**Consequence.** What this test actually exercised was the path `chloramine-T → slow release → HOCl → rapid reduction by CaSO₃`, i.e. **free-chlorine removal, not chloramine removal**. KES has already measured free-chlorine removal independently: 2026-03-20, 5 ppm free chlorine, 16.5–30 L/min, **84–90%** ([[bathtub-filter-25lpm-dechlorination-bench-test-spec]]). A "no drop" result at 19 L/min therefore **contradicts KES's own established free-chlorine performance** — pointing at bypass, sampling error, or misreading, rather than at a real null. Either way the data set carries **zero information about chloramine**.

Two further defects compound it. The same physical color-card swatch (the 0.1 mg/L block) is photographed in all five shots under different lighting conditions (indoor lamp, outdoor shade, direct sunlight) and with visible perspective distortion, so the photos are not comparable with each other — the apparent *upward* trend is within photometric noise. (The per-swatch ΔE figures computed for this were withdrawn on 2026-10-15 — see the correction note below.)

> **Correction (2026-10-15, author self-audit).** The ΔE figures above were originally flagged as the one robust finding. That flag was **wrong** — the sampling had systematic defects (shadow across one card, tilted parallelogram swatches vs rectangular sampling boxes, sampling band clipping the numeric labels). Two re-implementations both failed, the second because perspective merges adjacent swatches into 4 column-groups instead of 7 — a fundamental limit of photo colorimetry, not a fixable bug. **The specific ΔE numbers should not be cited.** What survives: across-image perturbation exceeds within-image adjacent-swatch separation by about an order of magnitude, so cross-image comparison carries more error than signal; and the card's 0.1–1 ppm region is structurally too crowded to resolve. The qualitative point needs no numbers — five photographs shot under different lights with visible perspective are not comparable, full stop. Full record in [[bathtub-filter-chloramine-T-measurement-2026-10-15]]. And at 0.4 s EBCT — roughly **1/600–1/800** of the ≥ 4–5 min the catalytic-carbon literature requires — this was a weakly-powered design choice independent of any media question.

**What this does and does not move.** The Section 6 CaSO₃ row **stays** `⚠️ Untested`. The banned zone stays banned. Assumption A-14 is unaffected. Gap 6 in Section 7 is now stronger than "no controlled data exists": **the identity of the challenge species was itself never confirmed.** See Section 7 for the standing requirement that reagent identity be established in writing before any spike test.

### The generalized lesson (2026-10-15): confirm the spike reagent's identity before dosing

**Chloramine-T and monochloramine are trivially confused in Chinese-language practice, and they test two entirely different things.** A spike test that names a reagent loosely is not a weaker test — it is a test of a different species.

This has a retroactive consequence: the **2026-10-09 KES bench test recorded its challenge as "4 ppm 氯胺" with no species stated.** If that run used the same reagent, its near-zero result may also be free-chlorine removal rather than chloramine removal. **The 2026-10-09 reagent identity must be re-established from the operator before that result is cited as chloramine evidence.**

> **Resolved 2026-10-28.** The reagent identity was re-established from the operator's own records — and the answer is not "chloramine-T" but **"not establishable"**: the challenge was self-mixed without a laboratory chloramine standard, and the operator wrote on 2026-10-12 that *"it is possible what we made is wrong"*. The 2026-10-09 result has been **removed from the chloramine evidence count**. See [raw pass](../../../raw/products/bathtub-filter/2026-10-28-caso3-2026-10-09-reagent-identity-check.md).
>
> **The lesson therefore generalises one step further than it was first written.** "Confirm the reagent's identity" was the 2026-10-15 formulation. The 2026-10-28 evidence says the stronger version: **for KES, an unconfirmed reagent identity is not a paperwork gap — it voids the data point.** Two of KES's three first-party chloramine runs (2026-09-24 and 2026-10-15) had a challenge that was either the wrong compound or unidentified, and the third had none recorded at all. **KES currently has zero species-identified chloramine data points.** The standing requirement in Section 7 is therefore not "write the CAS down" but **"no spike test enters the evidence base unless the species was confirmed by a species-specific method at the time of dosing"**.


---

## 4. Ascorbic Acid (Vitamin C) and Chloramine Removal

### Summary verdict: Effective in bath (tub) applications; not effective in shower applications due to contact time requirements

**Mechanism:**
Ascorbic acid (C₆H₈O₆) reduces NH₂Cl: C₆H₈O₆ + NH₂Cl → C₆H₆O₆ (dehydroascorbic acid) + NH₄⁺ + Cl⁻
The N–Cl bond in monochloramine is reduced, releasing ammonium and chloride. Dehydroascorbic acid and inorganic halides are the byproducts (no halogenated organics).

Sodium ascorbate (the sodium salt form) reacts identically but at neutral pH, avoiding the slight acidification that ascorbic acid causes.

### Key peer-reviewed finding (Tier 1)

**Basu and De Souza (2011) — Primary peer-reviewed source on ascorbic acid ineffectiveness for monochloramine:**
- Full citation: Basu OD, De Souza NP. "Comparison of dechlorination rates and water quality impacts for sodium bisulfite, sodium thiosulfate and ascorbic acid." *Journal of Water Supply: Research and Technology–Aqua.* 2011;60(3):167–177. IWA Publishing.
- DOI: Available at [IWA Publishing / Aqua](https://iwaponline.com/aqua/article-abstract/60/3/167/31172/Comparison-of-dechlorination-rates-and-water)
- What was tested: Dechlorination rates and water quality impacts for SBS, STS, and ascorbic acid against both free chlorine and monochloramine
- **Key finding for ascorbic acid: "ascorbic acid was found to be ineffective for the removal of monochloramine"**
- Context: This finding appears to apply to short-contact-time conditions or dissolved-phase testing. It is widely cited and is Tier 1 evidence.
- **Quality: Tier 1 (peer-reviewed, IWA indexed journal)**

**Critical nuance — bath vs. instantaneous dechlorination:**
The Basu & De Souza finding of "ineffective" likely reflects short contact time conditions (inline dechlorination). Multiple other sources suggest ascorbic acid *does* reduce monochloramine with sufficient contact time (4–8 minutes), which is achievable in a bathtub but not a shower. The apparent contradiction may reflect a time-dependent distinction rather than a complete inability to react.

**Rate constant data (Tier 1, but note: amino acid chloramine, not NH₂Cl):**
- Peskin & Winterbourn (2001): Rate constant for ascorbate + taurine chloramine = **13 M⁻¹ s⁻¹** at pH 7.4
- Full citation: Peskin AV, Winterbourn CC. "Kinetics of the reactions of hypochlorous acid and amino acid chloramines with thiols, methionine, and ascorbate." *Free Radical Biology and Medicine.* 2001 Mar 1;30(5):572–579. PMID: 11182528
- **Important caveat:** This measured *amino acid* chloramines (taurine chloramine specifically), not inorganic monochloramine (NH₂Cl). Taurine chloramine and NH₂Cl have different bond dissociation energies. The 13 M⁻¹ s⁻¹ figure cannot be directly applied to NH₂Cl removal in water systems, but gives a mechanistic lower bound for reactivity.
- At 13 M⁻¹ s⁻¹, the reaction is orders of magnitude slower than ascorbate + hypochlorous acid (HOCl), consistent with the practical observation that chloramine removal requires longer contact time than free chlorine removal.
- **Quality: Tier 1 (peer-reviewed), but indirect applicability to NH₂Cl**

### San Francisco PUC practical data (Tier 2)

**SFPUC determination (widely cited, Tier 2/government source):**
- Finding: 1,000 mg of vitamin C tablets, crushed and dissolved in bath water, **completely removes monochloramine** in a medium-size bathtub (~40 gallons) without significantly depressing pH
- Contact time required: **4–8 minutes**
- Dosing: ~1,000 mg ascorbic acid per 1 ppm chloramine per 40–50 gallons of water
- Source: San Francisco Public Utilities Commission, cited in multiple sources including [Inspired Living — Vitamin C Best for Chloramines](https://inspiredliving.com/chloramine-filters/vitamin-c-removes-chloramines.htm) and SFPUC Q&A document (March 2015)
- **Quality: Tier 2 (government utility recommendation, not peer-reviewed trial)**

**AWWA Standard (Tier 2):**
The American Water Works Association includes vitamin C (ascorbic acid) as an approved dechlorination method in AWWA C655 (Field Dechlorination standard, 2009 and updates). EPA and APHA also use ascorbic acid in lab-sample dechlorination protocols. This confirms institutional acceptance for dechlorination — though these are bulk dechlorination (full neutralization) contexts, not point-of-use filter ratings.

### Shower filter application — why it fails

Multiple sources confirm vitamin C shower filters are fundamentally limited by contact time:

- Shower water contact time with filter media: **<1 second** (estimated <0.5 sec for most shower cartridges)
- Required contact time for ascorbic acid to reduce monochloramine: **4–8 minutes**
- Result: Vitamin C can remove free chlorine in a shower (free chlorine reacts almost instantly) but cannot reliably remove monochloramine at shower flow rates
- Quantified: One Australian water filter company tested vitamin C shower performance on chloramine with a Hach Pocket Colorimeter and found "ZERO effects" on chloramine — consistent with the contact time analysis
- Source: [Envig — Can Vitamin C Remove Chloramine in Shower Water?](https://www.envig.cc/blogs/blog/can-vitamin-c-remove-chloramine-in-shower-water)
- NSF note: "There has never been a vitamin C shower filter capable of being certified to meet NSF Standard 177" [water filters Australia, Sprite Industries citation]
- **Quality: Tier 3 (industry/consumer testing, no formal methodology)**

### Bath tub application — why it works

The bath-fill scenario is structurally favorable:
- Water contacts vitamin C (or vitamin C–dosed water) for 5–10+ minutes during fill
- Static bath water maintains contact as long as user is in the tub
- 1,000 mg ascorbic acid per bathtub (40–50 gal) at 1 ppm chloramine is a feasible dose for a tablet or filter media

**Implication for filter design:** A bath spout filter that doses sufficient ascorbic acid or sodium ascorbate into the fill stream can achieve chloramine reduction because the water sits in the tub for minutes before and during use. This is a genuine structural advantage of the bath format over a shower filter.

---

## 5. NSF/ANSI Standards and Chloramine Testing

### NSF/ANSI 177 (Shower Filter Standard)

**Confirmed: NSF/ANSI 177 does NOT include chloramine testing.**

Key facts:
- NSF/ANSI 177 tests only **free available chlorine (FAC) reduction**
- Challenge water must have total chloramines concentration of **<0.1 mg/L** — specifically to avoid chloramine interference with the free chlorine test
- Pass/fail criterion: Reduce 2.0 mg/L free chlorine by at least 50% throughout rated service life
- Test water temperature: 40±2°C (104±4°F)
- The standard explicitly **requires manufacturers to disclose**: "This system has not been evaluated for free available chlorine reduction performance in the presence of chloramines" and "free available chlorine reduction performance may be impacted by the presence of chloramines in the water supply"
- Source: NSF/ANSI 177-2019 standard; preview at [ANSI Webstore](https://webstore.ansi.org/preview-pages/NSF/preview_NSF+ANSI+177-2019.pdf); and [PM Magazine — NSF/ANSI 177 Level Playing Field](https://www.pmmag.com/articles/87589-web-exclusive-br-nsf-ansi-standard-177-a-level-playing-field-for-shower-filter-claims)

**Implication:** Any shower or bath filter that claims chloramine removal and cites NSF/ANSI 177 is misapplying the standard. The standard was not designed to evaluate chloramine performance and explicitly disclaims it.

### NSF/ANSI 42 (Aesthetic Effects, Point of Use / Point of Entry)

**NSF/ANSI 42 can include chloramine reduction — but it is a separate, specific certification claim.**

Key facts:
- NSF/ANSI 42 covers aesthetic-effect contaminants including chlorine taste/odor, and **optionally chloramine reduction** if claimed
- Certification is contaminant-specific: a filter certified for chlorine reduction under NSF 42 is **not** automatically certified for chloramine reduction
- Challenge water for chloramine testing: typically ~3.0 mg/L total chloramines; required effluent ≤0.5 mg/L
- Catalytic carbon filters can and do achieve NSF 42 chloramine reduction certification (e.g., Aquasana Rhino Chloramines: certified to reduce 83% of chloramines; CB Tech: >97.5% reduction)
- Source: [NSF — NSF/ANSI 42, 53, and 401 Standards Overview](https://www.nsf.org/knowledge-library/nsf-ansi-42-53-and-401-filtration-systems-standards)

**Implication for KES:** If KES makes a chloramine removal claim, NSF/ANSI 42 chloramine reduction certification is the appropriate standard to pursue, not NSF/ANSI 177. No shower filter to date holds NSF certification specifically for chloramine reduction.

### NSF/ANSI 61 (Drinking Water System Components — Health Effects)

NSF/ANSI 61 covers materials and components that contact drinking water and ensures they don't leach harmful contaminants. It is **not a performance standard** — it does not test or certify contaminant removal rates.

- Scope: Material safety of pipes, fittings, coatings, treatment chemicals, mechanical devices
- Explicitly excludes: Performance, taste and odor, microbial growth support, and point-of-use drinking water treatment device performance
- Relevance to chloramine claims: None — NSF 61 cannot be used to support chloramine removal claims
- Source: [NSF — NSF/ANSI/CAN 61](https://www.nsf.org/water-systems/nsf-ansi-can-61-testing-and-certification)

---

## 6. Summary Evidence Table

| Media | Free Chlorine | Monochloramine (NH₂Cl) | Best Evidence Quality | Key Quantitative Finding |
|---|---|---|---|---|
| KDF-55 | ✅ Excellent (≥95%) | ❌ 18.2% max in test | Tier 2 (industry test, Pure Water Gazette) | 18.2% removal at 1 gpm; 97.7% with catalytic carbon added |
| KDF-85 | ✅ Excellent | ❌ ~1.4% in test | Tier 2 (industry) | Worse than KDF-55 for chloramine |
| Standard GAC | ✅ Good | ⚠️ Poor-to-marginal | Tier 2 (trade press) | Requires EBCT ≥10 min; typical shower EBCT <0.1 min |
| Catalytic activated carbon | ✅ Excellent | ✅ Good-to-excellent | Tier 1 (Kochany 2008) + Tier 2 | EBCT 4–5 min adequate; 5× longer breakthrough than standard GAC; 65% better than standard coal GAC |
| Calcium sulfite | ✅ Excellent (hot water) | ⚠️ **Untested — unresolved** (was ❌ "No removal expected" prior to 2026-10-09) | Tier 1 chemistry (Yiin 1987), **contested** by **one** uncontrolled observation (2023 supplier report) | Sulfite-chloramine reaction is pH-dependent and ineffective above pH 7.5; no controlled CaSO₃-specific data exists. The supplier spike test (2023) reports near-total removal with no pH, no control, and no stated LOD. **KES itself has produced no species-identified chloramine data point** (2026-09-24 run: species never established; 2026-10-15 run: chloramine-T, i.e. free chlorine) — see Section 3.5 |
| Ascorbic acid (bath) | ✅ Instantaneous | ✅ Complete in 4–8 min | Tier 2 (SFPUC) + Tier 1 partial | 1,000 mg per 40–50 gal removes all NH₂Cl; 4–8 min contact required |
| Ascorbic acid (shower) | ✅ Instantaneous | ❌ ~0% in shower | Tier 3 (field test) + logic | Contact time <1 sec vs. 4–8 min required; field test showed "ZERO effects" |

---

## 7. Key Evidence Gaps

1. **No peer-reviewed study measuring KDF-55 or KDF-85 chloramine removal in consumer-filter conditions.** The 18.2% figure is Tier 2 only.

2. **No peer-reviewed study measuring CaSO₃ + NH₂Cl reaction rate. The expected ineffectiveness is inferred.**
   > **2026-10-09 update.** This gap no longer reads "no data exists anywhere" — a supplier spike test (`ZONET20230707001`) and a KES first-party bench test now exist, and both report near-total removal. The gap has changed character from **no data** to **no controlled data**. Neither new data point reports pH, includes a decay control, uses a species-specific method, or states a detection limit, and both consumed under 1% of media capacity. See Section 3.5. The Tier-1 anchor (Yiin 1987) is unretracted; what has been withdrawn is the argument-from-silence that sat on top of it.
   > **2026-10-28 correction to the above.** The KES first-party bench test has been **removed from the count** — its challenge species was never established. **One** uncontrolled observation remains (the supplier report). The gap statement therefore simplifies to: *no controlled data exists, and the single uncontrolled observation that does exist names its species but reports no pH, no control, no analytical method, no detection limit, an influent that decays ~26% across the run, and a removal-percentage column that is back-calculated from the inlet/outlet pair.* The Tier-1 anchor remains unretracted; the argument-from-silence remains withdrawn.

3. **Basu & De Souza (2011) finding that ascorbic acid is "ineffective" for monochloramine** is Tier 1 but may describe short-contact or inline conditions. No peer-reviewed study specifically validates the SFPUC's bathtub finding (1,000 mg/40 gal, 4–8 min = complete removal) with controlled methodology.

4. **No published catalytic carbon EBCT data at bath-water temperature (~40°C).** Kochany (2008) showed faster rates at 20°C vs 5°C; extrapolation to 40°C suggests favorable kinetics but is not measured.

5. **Ascorbic acid rate constant data (Peskin & Winterbourn 2001) was for taurine chloramine (an amino acid chloramine), not inorganic NH₂Cl.** The 13 M⁻¹ s⁻¹ figure should not be directly applied to bath filter calculations without caveat.

6. **No controlled CaSO₃ + chloramine test exists at any pH, temperature, flow rate, or throughput.** Newly named 2026-10-09. The decisive design is a chloride mass balance with a media-free decay control — see Section 3.5 and [[bathtub-filter-validation-testing-protocol]]. Until this is run, CaSO₃ × chloramine is genuinely unknown rather than known-negative.
   - **Sharpened 2026-10-15.** The third first-party test (chloramine-T, 19 L/min, 29 °C) reported no removal, but its challenge reagent was **chloramine-T, not monochloramine** — so it does not close this gap and does not even bear on it. The gap is now wider than "no controlled data": **the identity of the challenge species has never been confirmed in writing for any KES run.** The 2026-10-09 reagent must be re-identified before it is cited. See Section 3.5 and [[bathtub-filter-chloramine-T-measurement-2026-10-15]].
   - **Closed on the re-identification question, 2026-10-28 — and the answer voids the data point.** The 2026-10-09 reagent could not be re-identified from any record; the operator's own account is that it was self-mixed without a laboratory chloramine standard and *"it is possible what we made is wrong"*. **KES therefore has zero species-identified chloramine data points**, and the gap is now precise: *not merely "no controlled data" — no KES-run data point about chloramine exists at all, and the only species-named observation on file is a supplier report whose challenge, method, pH, and control arms are all undocumented.* The standing requirement added 2026-10-28: **a spike test does not enter the evidence base unless the species was confirmed by a species-specific method at the time of dosing** (Module 7). One practical constraint on closing this gap: labs working to the national standard `GB/T 5750.11-2023` return **total chloramine only, with no split into monochloramine / dichloramine / NCl₃** — so species attribution is an *add-on* (DPD free/combined differentiation, IC for Cl⁻), not part of the standard test.

7. **No supplier report on CaSO₃ + chloramine discloses pH, analytical method, or detection limit.** `ZONET20230707001` is the only such report on file and omits all three. This is a recurring supplier-reporting gap, not a one-off omission, and should be raised with the vendor as a documentation requirement for any future CaSO₃ testing.

### 2026-06-15 文献刷新（时效戳）
- **无推翻性新证据**：针对「催化炭除氯胺 EBCT」与「抗坏血酸/抗坏血酸钠除单氯胺动力学」做了 2024–2026 web 检索，**未发现新的同行评审研究**改变 Kochany (2008) / Basu & De Souza (2011) 的基准结论。本页科学结论仍 current。
- **「抗坏血酸钠比抗坏血酸省 50×」= 已证伪（2026-06-15 追到一手来源）**：
  - 网传「50× 更省」只来自 hobbyist 圈循环引用（permies / planted tank / dude grows / LinkedIn）+ 一页无引用的 LibreTexts 教学页（Diablo Valley College, *Chloramine Processing Protocols*，原文 "requires 50x more concentration than Sodium Ascorbate"，**零引用**）。无任何一手研究。
  - **一手权威反驳**：AWWARF/EBMUD *Guidance Manual for the Disposal of Chlorinated Water*（Tikkanen, Schroeter, Leong & Ganesh）实测化学计量表（@ pH 8.0）：**抗坏血酸 2.48 / 抗坏血酸钠 2.78 份** 中和 1 份氯。抗坏血酸钠按质量需要的反而**略多**（MW 198 vs 176），与「两者活性还原物相同（抗坏血酸根）」一致。**「50× 更省」与一手数据相差约 140×，系网络谣传。**
  - **选抗坏血酸钠的真正理由 = pH 不是效率**：AWWARF 实测，抗坏血酸粉末过量把 pH 从 8.9 拉到 5.07、现场降 0.3–0.6 单位；抗坏血酸钠 pH≈7.0、降幅 <0.1 单位 → bath comfort 该选中性的抗坏血酸钠。
  - **一个值得 V1.5 验证、但证据有三条保留的信号**：AWWARF 的 Portland 实测用 combined chlorine（氯胺，~1.05 mg/L）。原文：抗坏血酸/抗坏血酸钠（化学计量、溶液，经 **100 英尺软管**混合——非扩散器，扩散器是 Tacoma 的游离氯测试）把总氯降到 <0.1 mg/L 的首个采样点是「mixing hose 下游 2 英尺（约 2 秒）」。**三条保留**：① 那「2 秒」只是软管**出口后**的 2 英尺，**管内还有未量化的接触时间**（混合与初始反应在管内发生），故非「2 秒总接触」；② 测的是 Hach 比色法总余氯，**抗坏血酸作为还原剂可能干扰比色读数**、使「中和」被高估；③ 单次现场测试、未重复，且与 Basu (2011) Tier 1「对单氯胺无效」冲突。**净结论**：只能说「充分混合下氯胺中和**可能是亚分钟级**、远快于静态浸泡」，**不能说「2 秒」或「充分混合即秒解」**。消费者浴缸（静态浸泡件）仍以 SFPUC **4–8 分钟**为规划值；「混合到底能压到多快」**必须 KES 自己台架定**，不能拿此现场数据当承诺。
  - **附带**：该 AWWARF 文末点名 **Industrial Test Systems (Rock Hill, SC)** 的「游离氯+总氯」监测试纸（0.02–750 mg/L）——印证 [获客引擎页](./bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md) 的定制试纸 OEM 路径，且总氯试纸正是氯胺版「自己测」所需。

---

## 8. Implications for KES Product Design and Claims

### What is empirically supportable

- "Reduces free chlorine" — supportable with any standard media (KDF, calcium sulfite, GAC, vitamin C)
- "Reduces monochloramine" using **catalytic activated carbon** — supportable only with citation to Kochany (2008) and column test data **plus product geometry that genuinely delivers adequate EBCT**
- "Reduces monochloramine" using **ascorbic acid / sodium ascorbate in bath applications** — supportable with SFPUC guidance, AWWA approval, and mechanistic rationale; needs bath-format product (not shower) to satisfy 4–8 min contact time requirement

### What is not supportable with current evidence

- "Reduces chloramine" for KDF-only or KDF-55-based shower/bath filters — 18.2% removal is insufficient to claim "reduction"
- "Reduces chloramine" for calcium sulfite–based products — **still not supportable.** The 2026-10-09 contradiction event (Section 3.5) changed the *reasoning* behind this exclusion, not the exclusion itself: it is no longer "the chemistry does not work" but "no controlled evidence exists in either direction, and the one uncontrolled observation on file (a 2023 supplier report with no pH, no control, no method and a back-calculated removal column) is not capable of supporting a claim." **2026-10-28: KES has produced no species-identified chloramine data point at all**, so nothing in the company's own hands supports the claim either. See also [[bathtub-filter-claim-register]] banned zone.

- **Any claim resting on a spike test whose reagent species was not confirmed in writing** — added 2026-10-15. The chloramine-T measurement showed that a loosely-named reagent produces a valid-looking dataset for the wrong species. "We spiked chloramine" is not a species statement.
- "NSF/ANSI 177 certified for chloramine removal" — 177 explicitly does not test chloramine
- Vitamin C shower filter claiming chloramine removal — contact time is 2–3 orders of magnitude too short

### Recommended claim architecture by media

| Product formula | Defensible chloramine claim | Required condition |
|---|---|---|
| Catalytic carbon (adequate bed size) | "Reduces combined chlorine (chloramine)" | Must achieve EBCT ≥4–5 min in bath fill flow; this likely implies a larger canister-style bed, not a compact bath-ball |
| Ascorbic acid / sodium ascorbate (bath format) | "Neutralizes chloramine in bath water" | Bath application only; note 4+ min contact needed |
| KDF-55 + catalytic carbon | "Reduces both free and combined chlorine" | Catalytic carbon does the chloramine work; KDF contributes primarily to free chlorine; claim still depends on real catalytic-carbon EBCT |
| Catalytic carbon + sodium ascorbate | "Reduces chloramine during fill and soak" | Strongest bath-format route; inline reduction plus in-tub completion |
| KDF-55 alone or + standard GAC | Free chlorine only | Cannot claim chloramine without data |
| Calcium sulfite alone | Free chlorine only | Cannot claim chloramine without data. **2026-10-09:** a supplier spike test and a KES bench test now report near-total chloramine removal, but neither reports pH, includes a control, or states a detection limit. This row is unchanged — the evidence still cannot carry a claim — but the rationale is now "unresolved" rather than "chemically implausible". |

---

## 9. 混合/传质 vs 反应：为什么「氯胺中和要多久」是个工程变量，不是固定值

> 2026-06-15 新增。这节解释 §4 的两个数据点（SFPUC 4–8 分钟 vs AWWARF Portland 亚分钟）为什么差这么多，以及由此引出的氯胺版台架自变量设计。这是把「混合能把氯胺压到多快」变成可测、可设计的问题。

### 9.1 一个反应「实际多快完成」由两个串联环节决定

抗坏血酸钠中和氯胺，**观测到的速度**取决于两个串联步骤，整体由更慢的那个（限速步骤）决定：

1. **化学反应速率**——抗坏血酸根 + NH₂Cl，N–Cl 键被还原。有个固有速率。
2. **传质 / 混合**——试剂要先溶解、再扩散分布到整缸每一滴水，才能碰到氯胺。

> 固有反应可能很快，但若试剂以固体形式慢慢溶、又在静水里慢慢扩散，**观测速度被传质拖慢**——此时是「传质限速」，不是「反应限速」。

### 9.2 §4 的两个数据点是两个极端，差的主要是混合不是化学

| 场景 | 试剂状态 | 混合 | 观测中和时间 | 限速环节 |
|---|---|---|---|---|
| **SFPUC 浴缸**（§4） | 固体药片/浸泡件，慢慢溶 | **静态**，不搅动 | **4–8 分钟** | **传质**（溶解+扩散慢）|
| **AWWARF Portland**（§4 / §7 保留版） | **已溶成溶液** | **流动 + 100 ft 软管湍流** | 亚分钟级（含未量化的管内接触时间）| 接近**反应**（混合已快）|

**关键洞察**：4–8 分钟 vs 亚分钟，主要不是「化学变快了」，是**试剂被送到水里的方式不同**。静态浸泡件的瓶颈是「药片溶得慢 + 溶出物自己慢慢扩散」；充分混合的溶液让试剂瞬间铺满，反应该多快就多快。
（注：Portland 那条仍带 §7 的三条保留——管内接触时间未隔离、比色法可能被抗坏血酸干扰、单次未重复且与 Basu 2011 冲突——故只能作「上行信号」，不作承诺。）

### 9.3 对 KES 双段设计的含义（决定第二段形态、UX 与 claim）

氯胺版 = inline 催化炭 + 缸内抗坏血酸钠浸泡件。「混合」直接决定第二段怎么做：

| 方案 | 投放方式 | 规划接触时间 | UX | 可守 claim |
|---|---|---|---|---|
| **A 静态浸泡件** | 丢进缸、不搅 | **4–8 分钟**（SFPUC 保守值）| 注水时放入 + 等几分钟再泡 | 「浸泡数分钟中和氯胺」|
| **B 溶进注水流** | 预溶液/快溶剂型，借注水湍流 | 有望逼近亚分钟 | 注水阶段即处理，少等待 | 「注水时即中和」（**须台架坐实**）|

→ **「混合能把氯胺压到多快」= KES 能否靠剂型/投放设计，把第二段从慢的静态传质区推向快的充分混合区。** 这是可工程争取的性能空间，不是固定值。

### 9.4 安全规划值

KES 自己台架测出前，产品定义与 claim **保守按 4–8 分钟**，不按亚分钟承诺。快的数是**要靠测试挣的上行**，不能默认拥有（呼应 §7 对 Portland 数据的三条保留）。

### 9.5 氯胺版台架自变量设计（把「混合」当自变量）

在浴缸条件下，把**混合/投放方式**作为主自变量，测「到达总氯达标所需时间」：

- **固定条件**：水温 **40±2℃**；进水单氯胺 **1 / 2 / 3 mg/L**；抗坏血酸钠化学计量剂量（参考 AWWARF 2.78 份/份氯，含适度过量）；典型浴缸水量。
- **自变量（混合/投放）**：
  1. 静态浸泡件（不搅）—— 复现 SFPUC 基线
  2. 溶进注水流（出水口处投放 / 预溶液计量入流）—— 湍流混合
  3. 中间态（浸泡件置于出水口下方，借注水冲刷）
- **测量**：总氯（total chlorine）随时间曲线；**必须正确处理抗坏血酸对 DPD/比色法的还原干扰**（否则「中和」被高估）——用经验证的方法或扣除空白，必要时第三方。
- **重复**：每条件 ≥3 次。
- **输出**：「哪种投放剂型 + 多长接触时间」达标 → 直接决定 ① 浸泡件形态（药片/网袋/出水口套件）；② 用户等待时间（UX）；③ claim 能否从「泡 N 分钟」升级到「注水时中和」。

> 本节为氯胺版（V1.5）专属；游离氯版 V1 的去氯×流量×压降曲线见 [25L/min 去氯特征测试 spec](./bathtub-filter-25lpm-dechlorination-bench-test-spec.md)（该 spec 明确把氯胺排除在范围外，指向本节）。

---

## Sources

**Tier 1 — Peer-reviewed:**
1. Kochany J, Lipczynska-Kochany E. "Catalytic Destruction of Chloramine to Nitrogen Using Chlorination and Activated Carbon — Case Study." *Water Environ Res.* 2008;80(4):339–345. PMID: 18536485 — [PubMed](https://pubmed.ncbi.nlm.nih.gov/18536485/) | [ResearchGate](https://www.researchgate.net/publication/5320060_Catalytic_Destruction_of_Chloramine_to_Nitrogen_Using_Chlorination_and_Activated_Carbon-Case_Study)
2. Basu OD, De Souza NP. "Comparison of dechlorination rates and water quality impacts for sodium bisulfite, sodium thiosulfate and ascorbic acid." *J Water Supply Res Technol-Aqua.* 2011;60(3):167–177 — [IWA Publishing](https://iwaponline.com/aqua/article-abstract/60/3/167/31172/Comparison-of-dechlorination-rates-and-water) | [Semantic Scholar](https://www.semanticscholar.org/paper/Comparison-of-dechlorination-rates-and-water-for-Basu-Souza/8097193f7e178027196061931719aaef04c63444)
3. Peskin AV, Winterbourn CC. "Kinetics of the reactions of hypochlorous acid and amino acid chloramines with thiols, methionine, and ascorbate." *Free Radical Biology and Medicine.* 2001;30(5):572–579. PMID: 11182528 — [PubMed](https://pubmed.ncbi.nlm.nih.gov/11182528/) | [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0891584900005062)
4. Yiin BS, Walker DM, Margerum DW. "Nonmetal redox kinetics: general-acid-assisted reactions of chloramine with sulfite and hydrogen sulfite." *Inorganic Chemistry.* 1987;26(21):3435–3441 — [ACS Publications](https://pubs.acs.org/doi/10.1021/ic00268a006)

**Tier 2 — Industry/technical/standards:**
5. NSF/ANSI 177-2019 Standard (Shower Filtration Systems) — Preview: [ANSI Webstore](https://webstore.ansi.org/preview-pages/NSF/preview_NSF+ANSI+177-2019.pdf)
6. NSF/ANSI 42 Standard Overview — [NSF International](https://www.nsf.org/knowledge-library/nsf-ansi-42-53-and-401-filtration-systems-standards)
7. NSF/ANSI/CAN 61 Overview — [NSF International](https://www.nsf.org/water-systems/nsf-ansi-can-61-testing-and-certification)
8. Jacobi Carbon 101 — Chloramines (column test data, ANSI-NSF 42-2002 protocol) — [jacobi.net](https://www.jacobi.net/chloramines/)
9. Everfilt — What Is Catalytic Carbon? EBCT Table — [everfilt.com](https://www.everfilt.com/post/what-is-catalytic-carbon-understanding-ebct-why-it-matters-in-water-filtration)
10. KDF Research Page — Reductive Dechloramination Study listing — [Kymera International](https://kdf.kymerainternational.com/research)
11. KDF Chlorine Removal Case Study (free chlorine only) — [Kymera International](https://kdf.kymerainternational.com/research/success_chlorine)
12. WaterWorld — Catalytic Carbon for Chloramine Removal (Filtrex Technologies column test) — [waterworld.com](https://www.waterworld.com/residential-commercial/article/14309145/filtrex-technologies-usa-catalytic-carbon-for-chloramine-removal)
13. WCP Online — Reduction of Chloramines Using Catalytic Carbon (2012) — [wcponline.com](https://wcponline.com/2012/02/24/reduction-of-chloramines-in-drinking-water-using-catalytic-carbon/)
14. WCP Online — Activated Carbon Chlorine & Chloramine Removal (EBCT data) — [wcponline.com](https://wcponline.com/2009/06/13/chlorine-chloramine-removal-activated-carbon/)
15. Alliance Chemical — Sodium Bisulfite Dechlorination Guide (stoichiometry, pH effects) — [alliancechemical.com](https://alliancechemical.com/blogs/articles/an-engineers-guide-to-sodium-bisulfite-for-dechlorination)
16. SFPUC Chloramine Q&A 2015 (vitamin C bathtub dosing) — [SFPUC via freshwatersystems.com](https://assets.freshwatersystems.com/image/upload/s--be0B3AdP--/iftklwwcuxt6ei8qey6t.pdf)
16a. **Tikkanen MW, Schroeter JH, Leong LYC, Ganesh R. *Guidance Manual for the Disposal of Chlorinated Water.* AWWARF / EBMUD.** —— 一手脱氯化学计量与 Tacoma/Portland/EBMUD 三地实测（抗坏血酸 2.48 / 抗坏血酸钠 2.78 份/份氯 @ pH 8.0；Portland combined-chlorine 实测；pH 影响）。用于证伪「抗坏血酸钠省 50×」谣传。— [PDF (vita-d-chlor.com)](https://www.vita-d-chlor.com/specs/AWWARFDechlorGuides.pdf)
17. Inspired Living — Vitamin C Is Best for Chloramines (SFPUC citation, 1,000 mg dosing) — [inspiredliving.com](https://inspiredliving.com/chloramine-filters/vitamin-c-removes-chloramines.htm)
18. PM Magazine — NSF/ANSI 177: Level Playing Field for Shower Filter Claims — [pmmag.com](https://www.pmmag.com/articles/87589-web-exclusive-br-nsf-ansi-standard-177-a-level-playing-field-for-shower-filter-claims)

**Tier 3 — Secondary/consumer (cited for field observation only):**
19. Pure Water Gazette — KDF and Chloramines (18.2% test result at 1 gpm) — [purewatergazette.net](http://www.purewatergazette.net/blog/kdf-and-chloramines/)
20. Envig — Can Vitamin C Remove Chloramine in Shower Water? (field colorimeter test: zero effect) — [envig.cc](https://www.envig.cc/blogs/blog/can-vitamin-c-remove-chloramine-in-shower-water)
21. AquaBliss — Calcium Sulfite and Water Filters (no chloramine claim made) — [aquabliss.com](https://aquabliss.com/blogs/healthy-water/calcium-sulfite-and-water-filters)
22. Water Filters Australia — Chloramines and Vitamin C (1,000 mg/1 ppm/50 gal dosing; 4–8 min contact) — [waterfiltersaustralia.com.au](https://www.waterfiltersaustralia.com.au/blog/chloramines-and-vitamin-c/)

**Tier 4 — Supplier-provided / imported internal material:**
23. 淄博宗立新材料科技有限公司 — `宗立测试-一氯胺及三氯铵 50g亚硫酸钙球.docx`，检测报告，样品编号 `ZONET20230707001`，检测完成时间 2023-07-13。Raw archive: `raw/products/bathtub-filter/2026-06-17-zongli-calcium-sulfite-chloramine-test/`；报告归档页 [[bathtub-filter-supplier-report-zongli-calcium-sulfite-chloramine-2023-07]]
24. [来源摘要｜亚硫酸钙 × 氯胺 矛盾事件（2026-10-09）](../../source-summaries/bathtub-filter-caso3-chloramine-contradiction-event-2026-10-09.md) — 对 #23 的定量批判（进水衰减混淆 / 容量利用率 0.61% / 三氯铵物种存疑）与矛盾事件裁定
25. KES first-party chloramine bench test (reported 2026-10-09; run on or before 2026-09-24) — 130 g CaSO₃ / 4 ppm "chloramine" / 24 L/min / 60 s / 38 °C, 总氯比色卡 readout — **reclassified 2026-10-28: challenge species never established, no longer a chloramine observation** — see source-summary #24, [[bathtub-filter-evidence-bibliography]] E7, and the raw pass below
34. [Raw pass｜2026-10-09 KES bench test 加标试剂身份回查（2026-10-28）](../../../raw/products/bathtub-filter/2026-10-28-caso3-2026-10-09-reagent-identity-check.md) — 原始钉钉会话取证、三张一手照片归档、裁定与影响面 — evidence tier: **internal-experience / first-party records**


**Tier 2 — added 2026-10-28 for the §1b-bis wording review (chloramine-T species identity, dosing ratio, pH window):**
26. PubChem CID 3641960 — Chloramine-T (CAS 127-65-1, C₇H₇ClNNaO₂S) — [pubchem](https://pubchem.ncbi.nlm.nih.gov/compound/3641960)
27. PubChem CID 25423 — Monochloramine (CAS 10599-90-3, ClH₂N) — [pubchem](https://pubchem.ncbi.nlm.nih.gov/compound/25423)
28. Wikipedia (EN) — Chloramine-T ("slightly basic, pH typically 8.5"; reactivity similar to sodium hypochlorite) — [en.wikipedia](https://en.wikipedia.org/wiki/Chloramine-T)
29. Wikipedia (DE) — Chloramin T ("In wässriger Lösung entsteht Hypochlorit durch Hydrolyse") — [de.wikipedia](https://de.wikipedia.org/wiki/Chloramin_T)
30. Wikipedia (ES) — Cloraminas ("…es realmente una sal … derivada de una cloramina") — [es.wikipedia](https://es.wikipedia.org/wiki/Cloraminas)
31. In-Situ / ChemScan — Water Chloramination Process Control (optimum Cl₂:NH₃-N 4.5:1; utilities run 3:1–5:1) — [PDF](https://in-situ.com/pub/media/support/documents/water-chloramination.pdf)
32. Curry & Associates — Using the Correct Arithmetic to Form Monochloramine (2015, rev. 2023), quoting Snoeyink & Jenkins 1980 (stoichiometric 5.06 mg Cl₂ : 1 mg NH₃-N) — [PDF (ILRWA)](https://www.ilrwa.org/Downloads/ChloraminationMath.pdf)
33. Halogen Systems — Measuring Monochloramine Without Reagents (ratio 4.5:1–5:1; pH 6.5–8.5 monochloramine-dominant, < 7 favours di/trichloramine) — [PDF](https://halogensys.com/docs/White%20Papers/monochloramine-whitepaper.pdf)
