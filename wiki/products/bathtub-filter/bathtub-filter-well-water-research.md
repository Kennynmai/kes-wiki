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
domains: [bathtub-filter, water-quality, well-water, private-wells, iron, hardness, hydrogen-sulfide]
source_count: 22
review_cycle: monthly
verification_status: working
related:
  - ./bathtub-filter-water-jurisdiction-demand-map.md
  - ./bathtub-filter-evidence-matrix.md
  - ./bathtub-filter-user-segments.md
  - ./bathtub-filter-disinfectant-types-and-media-guide.md
  - ./bathtub-filter-technology-notes.md
---
# Bathtub Filter — Private Well Water Research

## Why this page exists

The existing water-jurisdiction demand map focuses on municipal water — chlorine, chloramine, hard water in city systems. This page addresses the separate question:

> **What are the realistic water quality conditions in US private well households, and what does that mean for a bath-focused filter product?**

Private wells represent ~23 million US households (~15% of the population). They share some water quality concerns with municipal users (hardness) but have a completely different contaminant profile and a completely different regulatory context. This makes them either a distinct product segment or a product-design edge-case that needs explicit handling.

---

## Task 1 — Scale and Geography of US Private Well Use

### Core numbers

| Metric | Figure | Source |
|--------|--------|--------|
| Households on private wells | ~23 million | EPA |
| People on private wells | ~43 million (~15% of US population) | USGS / CDC |
| "1 in 8 American residents" framing | ~12.5% | CDC |

The ~23 million household figure (EPA) and ~43 million people figure (USGS/CDC) are consistent — they reflect ~1.9 people per household on average, or are measuring slightly different populations (wells used for drinking vs. all domestic use).

### Geographic concentration

Well use is concentrated in rural areas and specific regional geographies:

- **Northeast corridor**: Maine, New Hampshire, Vermont, New York — high well-use density along the I-95 corridor from Maryland to New Hampshire
- **Great Lakes / Upper Midwest**: Michigan stands out; many counties where two-thirds or more of residents use wells
- **Southeast / Carolinas**: High well-use counties in the Carolinas and northern Florida
- **Florida**: High private well density, particularly in rural and exurban areas

**Maine** is a notable example: more than half the state's population gets drinking water from private residential wells.

**Key geographic insight for product**: Well users are disproportionately in the rural-to-exurban band, not dense urban cores. This is roughly the inverse of the chloramine-heavy municipal markets already mapped.

### Demographics

From a PMC study on private well stewardship:

- Well users skew **older**, with slightly less formal education
- Household income cluster: **$50,000–$100,000** (moderate middle income, not poverty-line, not affluent)
- **46% of rural well-using households** are in high-poverty block groups (vs. 24% of urban well households)
- **25.3% of well-using households** identify as BIPOC
- **14.9%** have incomes below the poverty threshold
- Socioeconomic status predicts well stewardship: lower-SES households are least likely to test or treat their water

**Product implication**: The well-water segment is not the same premium demographic as urban chloramine-conscious buyers. It skews rural, middle-income, and older. This affects price sensitivity, purchase channel (retail vs. DTC), and trust framing.

---

## Task 2 — Typical Water Quality Problems in US Private Wells

### The headline number

A USGS national study of ~2,100 private wells found:
- **~23% of wells** contained at least one contaminant at concentrations exceeding a human health benchmark
- **~50% of well samples** had at least one contaminant above recommended levels (health + aesthetic combined)
- **43.2% of tested wells** in a Maryland study did not meet at least one federal health-based standard

### Contaminant categories: health vs. aesthetic

#### Health-significant contaminants (regulated standards)

| Contaminant | Prevalence | Geographic pattern | Notes |
|-------------|------------|-------------------|-------|
| Total coliform bacteria | 25.4% of wells (Maryland study) | Widespread, near septic systems and agriculture | Most common microbiological contaminant |
| Fecal coliform | 15.3% (Maryland) | Near septic, agricultural areas | |
| E. coli | 3.4% (Maryland) | Same | |
| Arsenic | ~7% of wells nationally exceed 10 ppb | New England (ME, NH, VT most elevated), upper Midwest, Southwest (NV, AZ, CA, TX) | Carcinogenic; ~2.1 million people on high-arsenic wells |
| Nitrate | ~3.4% exceed 10 mg/L (Maryland); ~4.1% nationally (USGS) | Agricultural areas, near septic systems | "Blue baby syndrome" risk for infants |
| Uranium | ~4% exceed 30 ppb | Western US; geologic | Kidney toxicity + cancer risk |
| Radon | 65% exceed 300 pCi/L (proposed standard); 2.7% exceed 4,000 pCi/L | Northeast, Appalachian, Colorado | Inhalation risk during showering is the main pathway (89% of radon-water cancer deaths are from inhalation) |
| Manganese | ~7% of domestic wells at potentially risky health levels (~2.6 million people) | Eastern wells; glacial aquifer regions | Neurotoxic at high concentrations; also aesthetic at lower levels |

#### Aesthetic / nuisance contaminants (secondary standards, not enforceable health limits)

| Contaminant | Prevalence | Geographic pattern | Effects |
|-------------|------------|-------------------|---------|
| Iron | Most common aesthetic contaminant in US private wells; 32–57% of wells in regional PA studies exceed 0.3 ppm SMCL | Midwest, Mid-Atlantic, glacial aquifer system | Staining (orange/rust), metallic taste, clogged pipes; EPA secondary MCL 0.3 mg/L |
| Manganese (aesthetic) | 12% exceed 50 ppb in USGS national study | Eastern US | Taste/color issues at lower levels than health threshold |
| pH (corrosive) | 26% of wells (Maryland); 83.8% of pH violations were acidic (<6.5) | Widespread, especially granite/crystalline rock geology | Acidic water leaches metals from pipes; corrosive to fixtures |
| Hardness (calcium / magnesium) | ~85% of the US has hard water; groundwater is typically harder than surface water | Midwest, Southwest, Texas, Great Plains hardest; New England, Pacific Northwest softest | Scale buildup, soap scum, dry skin/hair, fixture damage |
| Hydrogen sulfide | Up to ~20% of private wells may have seasonal sulfur odors; more common in shale/sandstone geology | Indiana (northwestern and northeastern), coal/oil field regions, acidic bedrock areas | "Rotten egg" smell; classified as aesthetic (no drinking water standard); detectable well below harmful concentrations |
| Fluoride | 10.9% of domestic wells exceed recommended levels | Aquifer-specific | Dental/skeletal fluorosis at high levels |
| Lithium | 37% of domestic wells at potentially concerning levels | Widespread | Emerging concern; no enforceable standard |

### Summary view for product purposes

**Three-tier contaminant map for bath-relevant concerns:**

1. **Primarily health-significant (bathing is a secondary exposure pathway)**: Arsenic, nitrate, uranium, bacteria — ingestion-route primary, bathing is minor exposure route. Not the core bath-filter story.

2. **Health-significant with a meaningful bathing pathway**: Radon — the USGS/EPA explicitly note that showering is the dominant inhalation exposure route. 89% of radon-in-water cancer deaths are from aerosolized radon during bathing/cooking, not drinking.

3. **Aesthetic / comfort (the bath-filter relevant tier)**: Iron, manganese, hardness, hydrogen sulfide, pH — these directly affect bath experience: staining, smell, skin/hair dryness, soap scum, pipe/fixture damage.

---

## Task 3 — Well Water vs. Municipal Water: What's Different for a Bath Filter

### The fundamental substitution

Municipal water users have **chlorine or chloramine** as the primary concern for a bath filter. Private well water users have **no added disinfectant** — the bath filter concern is entirely different.

| Dimension | Municipal water | Private well water |
|-----------|----------------|-------------------|
| Primary disinfectant concern | Free chlorine (most cities) or chloramine (~20–40% of systems) | None — no added disinfectant |
| Iron / manganese | Treated out at municipal level; rarely an issue | Major aesthetic concern; 32–57% of regional wells exceed SMCL |
| Hardness | Varies (municipal may partially treat); ~85% of US has some hard water | Groundwater is typically harder than surface water; same or worse |
| Hydrogen sulfide | Very rare in municipal distribution | Affects ~20% of wells seasonally; geology-dependent |
| Bacteria | Killed by chlorination | Real risk (25.4% of Maryland wells had total coliform) |
| Radon | Very rare in surface-water municipalities | Elevated in crystalline rock geology (NE, Appalachians, CO); bathing is primary inhalation route |
| Arsenic | Regulated and treated in municipal systems | 7% of wells exceed standard; 2.1 million people affected |

### Iron and manganese: the dominant bath complaint

Iron is described as "the most common contaminant in US private wells." Specific bath/bathing effects documented:

- Orange/rust staining on bathtubs, sinks, toilets, shower doors, grout
- Metallic odor in bath water
- Skin and hair dryness/irritation (iron deposits on skin)
- Possible eczema flare-up association (low evidence, mostly anecdotal)
- Concentration thresholds for bath relevance:
  - **0.3 ppm**: EPA secondary MCL; staining and taste begin
  - **0.3–3 ppm**: Light to moderate staining; treatment recommended
  - **3–7 ppm**: Significant staining; priority treatment zone
  - **7+ ppm**: Urgent; will clog fixtures rapidly
- Regional studies: 32% of Pennsylvania wells exceed 0.3 ppm SMCL; some county studies show 49–57%

### Hardness: similar story, different geology

- ~85% of US households have some hard water regardless of source
- Well water is typically harder than surface water (longer contact time with rock)
- Effects on bathing: filmy residue on skin, soap scum buildup, hair/nail brittleness, dry/tight skin post-shower, interference with moisturizer absorption
- Hard water is particularly associated with eczema exacerbation in sensitive-skin households
- Hard water states with high well use overlap: Indiana, parts of Texas, Florida

### Hydrogen sulfide: the "rotten egg" bath experience

- An aesthetic concern, not a health hazard at typical well concentrations
- Detection threshold: humans can smell H2S well below 0.5 mg/L — it becomes "aesthetically undrinkable" before it becomes dangerous
- No EPA drinking water standard set for H2S because the smell forces abandonment before health risk
- For bathing: odor is the issue — the shower becomes an unpleasant experience, smell may linger on skin/hair
- Affects up to ~20% of private wells seasonally; higher in shale/sandstone geology, near coal/oil fields

### Radon: the less-obvious bathing risk

- 65% of US private wells exceed 300 pCi/L (proposed EPA standard)
- 89% of radon-in-water cancer deaths are from inhalation during showering/cooking (not drinking)
- Concentrated in Northeast and Appalachian regions
- Bath/shower filter relevance: activated carbon (GAC) or aeration can reduce waterborne radon; this is a legitimate claim space for well water filter products in affected regions

### The absence of chlorine/chloramine in well water

Well water typically contains **no free chlorine or chloramine**. This has two implications for a bath filter product:

1. **KDF-55 and calcium sulfite**, the dominant media in current shower/bath filter products, are designed to remove chlorine. They provide less value to well water users for their primary function.
2. **KDF-85**, designed for iron/hydrogen sulfide removal, is the relevant media for well water — but it requires different product architecture and marketing.

A product designed for municipal water (chlorine removal) will not address the primary concerns of a well water user, and vice versa. These are functionally different product problems.

---

## Task 4 — Filter Media for Well Water Bath Concerns

### KDF-85: the core well water media

KDF-85 (high-purity copper-zinc granules, same redox exchange mechanism as KDF-55) is specifically engineered for well water:

| Function | Mechanism | Effectiveness |
|----------|-----------|--------------|
| Ferrous (dissolved) iron removal | Converts Fe²⁺ → ferric hydroxide (insoluble precipitate) | Up to 99% of soluble iron |
| Hydrogen sulfide removal | Converts H₂S → insoluble copper sulfide via electron transfer | 90–99% reduction (per Santé product data) |
| Bacteriostatic / microorganism inhibition | Produces hydroxyl radicals and hydrogen peroxide | Inhibits bacteria/fungi/algae growth |
| Heavy metals (manganese, lead, etc.) | Redox exchange | Significant reduction |

**Critical operating limits for KDF-85 in shower/bath applications:**
- Most effective at iron and H2S levels **below 3 ppm**
- pH should be between **6.5 and 8.5**
- Requires some dissolved oxygen for optimal redox function
- Heat-stable: does not degrade in hot shower water (unlike some activated carbon)

### KDF-55 vs. KDF-85 — what's different

| | KDF-55 | KDF-85 |
|---|---|---|
| Primary target | Free chlorine, heavy metals | Iron, hydrogen sulfide |
| Removes chlorine | Yes (~98%) | Partial |
| Removes iron | No | Yes (up to 99% of soluble iron) |
| Removes H2S | No | Yes (90–99%) |
| Municipal water use case | Primary fit | Secondary |
| Well water use case | Limited value | Primary fit |
| Bacteria inhibition | Some | Stronger |

Most current shower/bath filter products on the market use KDF-55. Products marketed specifically for well water use KDF-85, often combined with catalytic carbon.

### Hardness in compact filters: the honest limitation

There is no effective compact shower/bath filter media that meaningfully softens hard water at realistic flow rates. Ion exchange (the mechanism used in whole-house softeners) requires significant contact time and media volume. The honest product position on hardness is:

- A compact bath filter **cannot materially soften water** in the way a water softener does
- Some products claim "scale reduction" which is a lower bar than softening
- This is consistent with the claim-risk analysis already in the bathtub filter wiki: hardness is a demand amplifier but a claim-risk zone for compact products

### Products currently marketed for well water bath use

**Santé Ultimate Dual KDF Shower Filter for Well Water** (representative example):
- Media: KDF-85 + KDF-55 + catalytic carbon
- Claims: removes iron (99.9%), hydrogen sulfide (90–99%), heavy metals, chlorine, VOCs
- Filter life: 9–12 months
- Does not claim hardness softening
- Price range: $50–$100+ for the dual-stage configuration

**Whole-house systems as the "real" solution for well water:**
Industry guidance consistently states that compact shower/bath filters are insufficient for significant iron levels:
- Cartridge filters "clog within days or weeks" at iron levels above ~1–2 ppm
- Causing dramatic pressure drop and frequent cartridge replacement
- For iron levels 3+ ppm, whole-house backwashing filtration is the standard recommendation
- Whole-house AIO (air injection oxidation) systems handle up to 7–30 ppm iron

**Product design implication**: A compact bath filter for well water is a viable product only when iron and H2S levels are moderate (below ~2–3 ppm). At higher concentrations, the product fails in use and generates negative reviews. This is a critical product specification boundary.

### What a compact well water bath filter can honestly address

| Concern | Compact bath filter can address? | Notes |
|---------|----------------------------------|-------|
| Low-moderate iron (<3 ppm) | Yes, with KDF-85 | Filter life shortens at higher concentrations |
| Hydrogen sulfide smell | Yes, KDF-85 + catalytic carbon | Good performance at typical well levels |
| Moderate manganese | Partially, KDF-85 | Less data than iron |
| Hardness | No | No viable compact media |
| High iron (>3 ppm) | No — whole-house system needed | Cartridge will clog rapidly |
| Bacteria | Bacteriostatic only (inhibition, not elimination) | Not an NSF-certified disinfection claim |
| Radon | GAC (activated carbon) can help | Requires specific media and contact time |
| Arsenic, nitrate, uranium | No | Whole-house RO or specialized media required |

---

## Task 5 — Regulatory Context for Private Wells

### The foundational fact: no federal regulation

Private wells are **explicitly excluded** from the EPA's Safe Drinking Water Act (SDWA). The SDWA regulates public water systems serving 25 or more people or 15 or more service connections. A private well serving a single household is outside federal jurisdiction entirely.

Practical implications:
- EPA does not test, inspect, treat, or monitor private well water
- EPA sets no enforceable quality standards for private wells
- No federal requirement to test — ever
- No federal notification if contamination is detected

### Who is responsible

**The homeowner, entirely.**

From the EPA: "As a water well owner, you are responsible for testing your well to make sure the water is safe to drink."

From the CDC: "Government officials do not regulate, treat, or monitor tap water from private wells."

Only **56% of local health departments** regulate, inspect, or license private drinking water wells — meaning nearly half of US localities provide zero oversight.

### CDC / EPA testing recommendations (voluntary, not mandated)

**Annual minimum tests:**
- Total coliform bacteria
- Nitrates
- Total dissolved solids (TDS)
- pH level

**Every 2–3 years (or based on local conditions):**
- Arsenic
- Uranium
- Radon (in high-risk regions)
- Volatile organic compounds
- Lead, copper, iron, manganese (if aesthetics suggest an issue)
- Pesticides/herbicides (agricultural areas)

**Test immediately after:**
- Changes in taste, color, or smell
- Flooding or nearby land disturbance
- Well repair or component replacement
- Pregnancy or new child in household
- Local water quality alerts

### State-level regulatory patchwork

From a 2019 PMC study of state policies:

- **All 50 states** require drilling/construction standards for new wells
- **Only 22% of states** have any policy addressing well testing when a property is sold
- **Only 6% of states** have policies for rental properties with wells
- **Connecticut** is the only state with policies covering all nine regulatory categories studied
- **New Jersey** has one of the strongest regimes: well water must be tested when property is sold or leased; landlords must test every 5 years
- **Texas** has three separate agencies overseeing well regulation — creating fragmentation
- **Wisconsin and Florida** have more comprehensive frameworks than most states

**The general state of play**: There is no coherent national baseline. Most well owners in most states are never required to test their water under any legally binding rule.

### The contamination discovery problem

How do well users typically discover contamination?

1. **Sensory changes** (taste, color, smell) — catches aesthetic problems (iron, H2S, hardness) but **misses** colorless/odorless health contaminants (arsenic, nitrate, radon, bacteria at low levels)
2. **Illness patterns** — recurring gastrointestinal illness may suggest bacterial contamination, but causation is often not traced to well water
3. **Testing at sale** (in the states that require it) — catches problems at home purchase, often the first test ever done
4. **Public health alerts** — covers agricultural or industrial events in a region, not routine natural contamination

**Key insight**: Most health-significant contaminants (arsenic, nitrate, radon, uranium) have no taste or smell. Well owners are unlikely to know they have a health-level problem without testing. For aesthetic contaminants (iron, H2S, hardness), the user knows immediately — these are self-announcing.

---

## Synthesis: What This Means for a Bath Filter Product

### Segment definition: well water is a distinct sub-segment, not a product variation

The well water user has:
- Different primary concerns (iron, H2S, hardness, not chlorine)
- Different required media (KDF-85, not primarily KDF-55)
- Different awareness level (they already know their water is "different"; it's visible and smellable)
- Different purchase trigger (iron staining, rotten egg smell, skin issues from hard/iron water)
- Different regulatory context (no third-party that ever tested their water)
- Different demographics (rural, moderate income, older)

A bathtub filter product with a single formulation cannot honestly serve both a chloramine-city user and a high-iron well user. These are functionally different filtration problems.

### The viable well water bath filter case

A compact bath filter for well water **can work** when:
- Iron is **below ~2–3 ppm** (moderate, not severe contamination)
- H2S is the primary complaint (odor in bathing, aesthetics)
- The user wants a no-install, no-plumbing-modification solution (apartment, renter, or just wants to start somewhere)
- Hardness is not the dominant complaint (because no compact filter can address hardness)

**Market size context**: 23 million US well households. If ~30–50% have moderate iron issues (regional studies suggest this range), that's 7–11 million households with a potential unmet need for bath-specific iron/odor treatment.

### The claim boundary

For a well water positioned product:
- **Can claim**: iron reduction (specify ppm range), hydrogen sulfide odor reduction, heavy metal reduction, bacteriostatic action
- **Cannot claim**: water softening, arsenic/nitrate/uranium removal, bacteria elimination (disinfection), protection against health-level arsenic exposure
- **Must disclose**: product is not a substitute for a whole-house filtration system when iron exceeds 3 ppm; product does not treat health-significant contaminants; users should test their water annually

### The radon signal

Radon is an under-discussed bath filter opportunity for the well water segment:
- 65% of US private wells exceed the proposed 300 pCi/L standard
- 89% of waterborne radon cancer deaths are from inhalation during showering
- GAC (activated carbon) can reduce waterborne radon — this is a legitimate, defensible claim
- New England well users (high radon + high arsenic geology) are a specific addressable sub-segment

### The "first step" positioning angle

Many well water users know their water has a problem but do not have the budget or situation to install a whole-house system. A compact bath filter positions as:
- Affordable first step (while they evaluate whole-house options)
- Rental or apartment-friendly (no whole-house installation possible)
- Specific-use protection (baby bath, sensitive-skin family member) even if the whole house isn't treated

This is a more honest and more defensible product story than claiming whole-problem-solution.

---

## Open Questions and Gaps

- No national prevalence figure specifically for iron > 0.3 ppm in private wells (regional Pennsylvania studies suggest 32–57%; no confirmed national figure found)
- No data found on search volume or purchase intent for well-water-specific shower/bath filters vs. municipal-water filters
- Radon-specific bath filter claim has not been tested at the product level; contact-time and flow-rate constraints need engineering validation
- Demographics of well water users who actively seek bath filtration (vs. whole-house treatment) not quantified
- KDF-85 effective capacity (gallons per cartridge before breakthrough) at typical well iron concentrations needs product-specific validation

---

## Sources

- [EPA — Private Drinking Water Wells](https://www.epa.gov/privatewells)
- [USGS — Domestic (Private) Supply Wells](https://www.usgs.gov/mission-areas/water-resources/science/domestic-private-supply-wells)
- [USGS — Contamination in US Private Wells (20% finding)](https://www.usgs.gov/special-topics/water-science-school/science/contamination-us-private-wells)
- [USGS — Contaminants in 20% of US Private Wells (audio/article)](https://www.usgs.gov/media/audio/contaminants-20-percent-us-private-wells)
- [CDC — Private Drinking Water and Public Health](https://www.cdc.gov/environmental-health-services/php/water/private-water-public-health.html)
- [CDC — Guidelines for Testing Well Water](https://www.cdc.gov/drinking-water/safety/guidelines-for-testing-well-water.html)
- [PMC — Prevalence of Contaminants in Private Wells in Maryland, USA (PMC6121425)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6121425/)
- [PMC — State-Level Policies Concerning Private Wells in the United States (PMC6656387)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6656387/)
- [PMC — Private-Well Stewardship Among a General Population Sample (PMC5662198)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5662198/)
- [USGS — Study Estimates ~2.1 Million People Using High-Arsenic Wells](https://www.usgs.gov/news/national-news-release/study-estimates-about-21-million-people-using-wells-high-arsenic)
- [USGS — NAWQA Water Quality in US Private Wells](https://water.usgs.gov/nawqa/home_maps/domestic_wells.html)
- [USGS — Manganese in Groundwater (map)](https://water.usgs.gov/nawqa/home_maps/manganese_gw.html)
- [EWG — Private Wells and Contamination](https://www.ewg.org/tapwater/private-wells.php)
- [Circle of Blue — USGS Report: Trace Elements Exceed Health Standards in 20% of Wells](https://www.circleofblue.org/2011/world/water-testing-reveals-trace-elements-exceed-health-standards-in-20-percent-of-wells/)
- [Circle of Blue — Infographic: Household Wells in the United States](https://www.circleofblue.org/2018/supply/groundwater/infographic-household-wells-in-the-united-states/)
- [EPA — Secondary Drinking Water Standards (SMCLs)](https://www.epa.gov/sdwa/secondary-drinking-water-standards-guidance-nuisance-chemicals)
- [EPA — Protect Your Home's Water](https://www.epa.gov/privatewells/protect-your-homes-water)
- [NJ DEP — Private Well Testing Act](https://dep.nj.gov/privatewells/pwta/)
- [Penn State Extension — Hydrogen Sulfide in Water Wells](https://extension.psu.edu/hydrogen-sulfide-rotten-egg-odor-in-water-wells)
- [WaterFilterGuru — KDF Filter Media](https://waterfilterguru.com/kdf-filter-media/)
- [Santé — Ultimate Dual KDF Shower Filter for Well Water](https://santeforhealth.com/products/sante-ultimate-dual-kdf-shower-filter-for-well-water)
- [Mid Atlantic Water — Iron Filters for Well Water Complete Guide](https://midatlanticwater.net/blogs/guides/iron-filters-for-well-water-complete-guide)
- [NCBI Bookshelf — Risk Assessment of Radon in Drinking Water](https://www.ncbi.nlm.nih.gov/books/NBK230511/)
- [HomeWater101 — Hard Water Across the US](https://homewater101.com/articles/hard-water-across-us)
