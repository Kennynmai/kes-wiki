---
type: playbook
status: draft
owner: strategy
created: 2026-04-17
updated: 2026-04-17
visibility: company
confidence: medium
officiality: draft
domain: operations
domains: [research, patents, ip, freedom-to-operate, product-research]
review_cycle: quarterly
verification_status: spot-checked
related:
  - ./academic-search-workflow.md
  - ./market-research-workflow.md
  - ../products/bathtub-filter/bathtub-filter-patent-table.md
  - ../products/bathtub-filter/bathtub-filter-ip-depth-and-brand-marker-map.md
---

# Patent Investigation Workflow

## Trigger / scope

Use this workflow when a KES product decision starts depending on **who owns what IP in the category** — specifically:

- when an initial Google Patents scan has surfaced a list of candidate patents and we need to upgrade from "what these abstracts say" to "what is actually still enforceable and who actually owns it"
- when a brand public-facing a "patented" or "patent pending" claim needs to be checked against corroborating filings
- when we are deciding whether to route-avoid, design-around, or license a specific technical path
- when the prior-art pressure on a proposed KES route is unclear

This is **not a substitute for formal freedom-to-operate (FTO) legal review**. It is a strategic research workflow that produces the input a lawyer would need, and often resolves the question before a lawyer is needed.

## Goal

Convert a loose list of "patents that might matter" into a structured picture of:

1. **What is actually alive** — which patents are still in force, and when they expire
2. **Who actually owns it** — individual vs. corporate, recently assigned, pledged as collateral
3. **What the live IP protects** — claim-level structure, not abstract-level summary
4. **Where the real technical lineage runs** — via forward-citation networks, not keyword clusters
5. **Where the coverage gaps are** — jurisdictions / languages / classifications the initial scan missed

## Recommended stack priority

### First-line (free, WebFetch-friendly)

1. **Google Patents** (`patents.google.com/patent/<pub_num>`)
   - Single-patent view is the most reliable free source for: legal status, anticipated expiration, assignee chain, CPC classifications, forward citations ("Cited by")
   - **Works well via WebFetch** for known publication numbers; individual pages render as static HTML
   - **Does not work well via WebFetch for list/search pages** — the search UI is JavaScript-rendered and returns an empty shell. Use WebSearch or manual browser for list queries.

2. **Espacenet (EPO)** (`worldwide.espacenet.com`)
   - Best source for **same-family (INPADOC) analysis** — tells you how many jurisdictions a filer actually committed to
   - Best source for **legal-status timelines across jurisdictions** (US expiry vs. EP grant vs. JP grant)
   - CPC classifier search is more reliable than Google Patents for class-based scans

3. **Lens.org** (`lens.org`)
   - Best free source for **forward-citation network visualization** — shows who cites whom across a tech area
   - Links patent literature to scholarly literature (useful when the technical claim depends on an academic reference)

### Second-line (jurisdiction-specific)

4. **USPTO Patent Public Search** (`ppubs.uspto.gov/pubwebapp`)
   - Authoritative US legal status, maintenance-fee payment events, assignment chain
   - Use when Google Patents' status string is ambiguous

5. **USPTO Patent Center / Public PAIR** (`patentcenter.uspto.gov`)
   - **File wrapper access** — Office Actions, applicant responses, examiner search strategies, interview summaries
   - This is where you learn how a claim **narrowed during prosecution** — often the real technical boundary of the patent
   - Browser-based; hard to script

6. **J-PlatPat** (`www.j-platpat.inpit.go.jp`)
   - Japanese Patent Office — essential for categories with mature JP market activity (bath, shower, kitchen — Japanese filers dominate)
   - Many JP utility models do not surface in default English Google Patents queries

7. **CNIPA / 专利之星** (`pss-system.cponline.cnipa.gov.cn`)
   - China — indispensable when the target category has Chinese OEM manufacturing density
   - Look for cluster filings by small regional factories; these shadow US design patents and sometimes predate them

### Trademark layer

8. **USPTO TSDR** (`tsdr.uspto.gov`)
   - Trademark Status & Document Retrieval — definitive for US mark status
   - **Known limitation: blocks scripted WebFetch access (HTTP 403)**. Must be used manually or via uspto.report / trademarkia as a mirror.

9. **WIPO Global Brand Database** (`branddb.wipo.int`)
   - Cross-jurisdiction trademark scan — useful when a brand claims to be international

### Paid / enterprise (not used here, flagged for the moment a decision depends on legal certainty)

- Derwent Innovation, PatSnap, IncoPat — same-family merge, semantic claim comparison, FTO analysis
- Questel Orbit — deepest legal-status and litigation history

### Deprioritized / blocked for our harness

- **TSDR and Justia Patents direct search** — blocked for scripted access
- **Google Patents search/list URLs via WebFetch** — return empty shell; use WebSearch for list discovery and Google Patents direct URLs only for single-patent details

## Core workflow

The five-stage pattern below is the durable flow. Each stage produces an artifact that feeds the next.

### Stage 1 — establish the hub patents

Pick 2–4 patents from the initial scan that the rest of the technical story seems to cluster around. A hub patent is usually:
- cited by many downstream filings in the same category, and/or
- referenced by brand marketing as the technical anchor, and/or
- authored by a repeat inventor in the category

**Output:** a short list of hub publication numbers.

### Stage 2 — pull the forward-citation network

For each hub patent, extract the "Cited by" list. This is the single highest-leverage action in the whole workflow.

**Why:** downstream citers are declaring "this hub is my technical ancestor." That declaration is more reliable than any brand marketing claim. The citation network tells you:
- who is still actively filing in the lineage
- which companies treat themselves as legitimate successors
- which lineage splits off into adjacent-but-unrelated tech (industrial vs. consumer, outdoor vs. bath, etc.)

**Output:** a union-list of citing publication numbers, de-duplicated, with assignee labels.

### Stage 3 — verify legal status on every relevant patent

For each patent on the union list, record:
- current legal status (Active / Expired lifetime / Lapsed fee-related / Withdrawn / Pending)
- anticipated expiration date
- current assignee (not original applicant — they diverge)
- any unusual assignment events (collateral pledges, bankruptcy-era transfers, multiple reassignments)

**Why:** the abstract of an expired patent looks identical to the abstract of a live one. Until legal status is verified, every downstream decision is built on sand.

**Output:** a legal-status-augmented table replacing the initial scan table.

### Stage 4 — read the file wrapper on the still-live patents

For patents that are **still in force** and that cover the KES candidate route, pull the USPTO file wrapper (or equivalent in EP / JP / CN). Extract:
- Office Action rejections — what the examiner thought was anticipated or obvious
- applicant amendments — how the claims narrowed
- cited prior art — what the examiner pointed to as closest
- any terminal disclaimers, reissue, or reexamination events

**Why:** the issued claim is always narrower than the original application. The narrowing is where the real technical boundary lives. A competitor who reads only the issued patent often over-estimates how much is protected.

**Output:** a one-page note per live patent covering "what is actually protected" vs. "what the marketing implies is protected."

### Stage 5 — fill jurisdictional and classification gaps

Two systematic gaps to fill before concluding:

**Classification gap.** Run a CPC-class-based search (e.g., `A47K3/00`, `C02F1/003`, `C02F1/70` for bath filtration; adjust per category) **without the brand-name or category-name keyword.** This surfaces filings whose title/abstract does not contain the obvious keyword but whose claims occupy the same technical space.

**Jurisdictional gap.** For any category with known non-US market activity, scan at least JP and CN directly — not via English-keyword Google Patents. Use the same CPC classes + native-language keywords.

Separately, scan for **trademark deposits** matching the brand marketing terms (e.g., "Chlorgon", "Bath Ball", branded media names) — these corroborate or contradict the "technology trademark" claim a brand is making.

**Output:** an "IP coverage gap" section appended to the patent table, naming the classes and jurisdictions that were not fully scanned and why.

## Artifact pattern

For each category investigation, expect to produce or update:

1. **Patent table** (primary artifact) — rows = patents, columns now include legal status, expiration, current assignee, relevance-to-KES note
2. **Hub-patent citation map** — a short note per hub listing its forward citers and which are still alive
3. **Live-IP shortlist** — a dedicated section of the patent table naming only the patents KES must route-avoid or design-around
4. **Follow-up queue** — items that hit tool limitations (TSDR, Public PAIR, JP/CN native scans) and need a manual session

## Quality guardrails

### Keep these separate

- what the patent's **abstract** says (marketing-facing summary)
- what the patent's **issued claims** protect (legally enforceable scope)
- what the **file wrapper** reveals about how the claim narrowed
- what the **brand** is claiming publicly about its IP

The gap between the first and the last is where most IP-depth misreads happen.

### Red flags

- A "Sprite / Chlorgon lineage" type framing that turns out to be one individual's personal portfolio, not corporate IP. Single-inventor lineages die with the inventor.
- An assignee chain that ends in a pledge to a bank — usually a distress signal, not moat expansion.
- A brand website claiming "patented X technology" when no filing under that brand surfaces. The word "patented" is sometimes referring to licensed or expired foundational IP.
- A design patent (`USD######S`) interpreted as functional protection. Design patents protect ornamental shape only.
- Forward-citation clusters that drift into an adjacent-but-unrelated industry (e.g., industrial dechlorination tablets appearing in a consumer-shower citation tree). Filter these out explicitly.

### Do not over-claim

- A patent being expired does **not** mean the technology is easy to reimplement — know-how and trade secrets are separate.
- A patent being live does **not** mean the patent is valid — validity can only be tested in litigation or re-exam.
- A brand having "no visible patent" does **not** mean they have no filed applications — pending applications are only public 18 months after filing.

## Best use cases

This workflow is strongest when KES needs to:

- decide whether to enter a category where incumbents claim IP moats
- screen a candidate product architecture against active prior-art pressure
- decide whether a competitor's "technology moat" is real or mostly marketing posture
- scope the inputs a lawyer would need for a formal FTO opinion

It is weaker as a substitute for:

- formal FTO legal review
- patent litigation strategy
- patent valuation for licensing deals

## Known tool limitations in the current harness

Documented here so the next investigator does not waste time rediscovering them:

- **Google Patents search/list URLs** return an empty shell via WebFetch. Use WebSearch for list discovery.
- **USPTO TSDR, Justia Patents, and uspto.report** return HTTP 403 to scripted WebFetch. Trademark verification requires a manual browser session.
- **USPTO Public PAIR / Patent Center** is session-heavy and effectively requires a browser. File-wrapper pulls are manual.
- **J-PlatPat and CNIPA** are browser-and-form driven; scripted scans not currently feasible.

When these limitations hit, the workflow produces a **follow-up queue** entry rather than a fabricated result.

## Validation log

### 2026-04-17 — bathtub filter patent table expansion pass

Anchor question: *which patents in the bathtub filter category are actually live, who owns them, and what IP pressure does KES face?*

Starting artifact: [bathtub-filter-patent-table.md](../products/bathtub-filter/bathtub-filter-patent-table.md) — 10 utility patents + 1 design patent, all treated as approximately equivalent prior-art pressure.

Hub patents selected: `US5914043A` and `US6056875A` (the two media-chemistry patents the original table identified as Sprite's technical moat).

**New signal surfaced by applying the workflow:**

| Finding | Stage | Why it matters |
|---|---|---|
| **Every patent on the original table is expired, lapsed, or withdrawn.** US lifetime-expirations range 2015–2019; fee-lapses 2010–2022; LG's CN vitamin-C patent deemed withdrawn 2013. | Stage 3 | Original table implied live prior-art pressure; reality is the classic bath-filter architectures are public domain. Downgrade prior-art-risk assessment. |
| The **"Sprite Chlorgon lineage" is actually the Farley family lineage.** David K. Farley (Sprite's CEO), Michelle Farley, and David Aaron Farley personally hold the relevant patents; Sprite Industries as a corporate entity does not. `US6056875A` was pledged to Chase Manhattan 2001. | Stage 2 + 3 | Reframes "who is the technical moat holder" — it is an individual, not a company. License conversations would be with a person, not a legal team. |
| The **live IP set** consists of `US9504940B2` (2034), `US10737203B2` (2038), `US11458487B2` (2040) — all Farley — plus `US10159991B2` (2036, Homewerks, ex-Waxman) and **`US12534389B2`** (FilterBaby, granted 2026-01-27, expires 2044). | Stage 2 + 3 | This is what the original table missed entirely. KES route-avoidance must point at these five patents specifically. |
| **FilterBaby's `US12534389B2` is the single most important live patent** in the current landscape. Claims cover horizontally-oriented faucet filter + integrated dissolvable skin-treatment adapter + internal UV sterilization + mechanical filtered/unfiltered/eco mode + smart monitoring. Potentially covers the entire DTC skincare-filter category. | Stage 2 | This patent did not appear anywhere on the original Google Patents keyword scan. It was surfaced by following a 2025 citation thread and a WebSearch pivot to FilterBaby as a new entrant. |
| **Brita LP** (Clorox subsidiary) filed three bath-relevant design patents 2023–2025 (`D1055213`, `D1059541`, `D1067392`). Brita is not currently visible in DTC bath positioning but is building design-patent optionality. | Stage 5 | Competitive watch item — Brita entry would reshape the category. |
| "Eagle / Westlake US 2 LLC" citation cluster off of `US7682513B2` is **industrial dechlorination, not bath-relevant.** Filter out of future passes. | Stage 2 QA | Prevents false-positive citation noise. |
| **Kinder Filter, Tubo, Canopy have no visible utility patent filings** under their brand names. Their "patented advanced filtration" marketing language is not corroborated by USPTO records in this pass. | Stage 5 | Reinforces the existing IP-depth map: these brands are segment/channel moats, not IP moats. |

**Tools that did not pay off in this pass (and should go straight to follow-up next time):**
- USPTO TSDR direct access — blocked (HTTP 403)
- Justia Patents direct assignee search — blocked (HTTP 403)
- Google Patents list-view search URLs — empty shell via WebFetch
- JP/CN systematic scans — not feasible via this harness

**Follow-up queue generated:**
- [ ] Manual TSDR session for: CHLORGON, BATH BALL, KINDER FILTER, TUBO, FILTERBABY
- [ ] Pull full `US12534389B2` claim text and design-around scoping for KES skincare-positioned SKU
- [ ] Manual Public PAIR pull for `US6056875A` file wrapper to constrain what "Chlorgon-equivalent" media can claim
- [ ] J-PlatPat scan for JP bath-filter filings under A47K3 / C02F1 post-2015
- [ ] CNIPA scan on Yuyao Kangpu / Quanzhou Niuruilisi OEM cluster for shadow design-patent families

Downstream artifacts updated:
- [bathtub-filter-patent-table.md](../products/bathtub-filter/bathtub-filter-patent-table.md) — added 2026-04-17 expansion pass section with legal-status verification, Farley-lineage reframe, live-IP shortlist, follow-up queue
- Implications for [bathtub-filter-ip-depth-and-brand-marker-map.md](../products/bathtub-filter/bathtub-filter-ip-depth-and-brand-marker-map.md) — the map's "Sprite = technical lineage" conclusion holds but should be restated as "Farley family = technical lineage"; FilterBaby needs a new row as a **utility-patent-led** entrant (previously invisible)

## Sources
- [Academic Search Workflow](./academic-search-workflow.md)
- [Market Research Workflow](./market-research-workflow.md)
- [Bathtub Filter Patent Table](../products/bathtub-filter/bathtub-filter-patent-table.md)
- [Bathtub Filter IP Depth and Brand Marker Map](../products/bathtub-filter/bathtub-filter-ip-depth-and-brand-marker-map.md)
