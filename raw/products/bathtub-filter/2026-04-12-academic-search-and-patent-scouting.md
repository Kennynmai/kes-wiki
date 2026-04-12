---
source_type: market-brief
extraction_mode: web-search
created: 2026-04-12
updated: 2026-04-12
status: captured
domain: product
domains: [bathtub-filter, academic-search, patents, technical-scouting]
confidence: medium
visibility: team
officiality: working
verification_status: unverified
---

# Raw Capture — Bathtub Filter Academic Search and Patent Scouting (2026-04-12)

## Purpose
Capture two new research directions for the bathtub-filter topic:
1. whether a dedicated academic-search API stack is worth adding
2. what early patent signals reveal about bathtub-filter technical routes and claim patterns

## Academic-search infrastructure signals
### Current conclusion
A dedicated academic-search layer appears worth adding for this topic, but Google Scholar should not be the first choice.

### Why not start with Google Scholar-style APIs
- official Google Scholar API availability is poor
- many third-party options are crawler wrappers with stability / captcha / compliance risks
- ongoing maintenance burden is likely high relative to metadata quality

### Better first-stack candidates
- Crossref: DOI / citation metadata backbone
- OpenAlex: work graph, author graph, OA status, repository/full-text signals
- Europe PMC: especially useful for biomedical and skin / eczema / chlorine topics
- Semantic Scholar: useful for expansion / related-paper discovery, but lower priority than the three above

## Patent scouting queries used
- `bathtub filter patent chlorine reduction bath water filter tub faucet patent`
- `site:patents.google.com bathtub filter chlorine bath water filter patent`
- `site:patents.google.com tub faucet filter bath water chlorine patent`
- focused result checks for `Bathtub spout with removable filter` and `Water dechlorination means`

## Early patent hits observed
### 1. JP3002925U — Chlorine remover for bath water
- Signal:
  - soak-in-bath-water format
  - refill bag with calcium sulfite
- Relevance:
  - supports that dechlorination can be framed as an immersion accessory, not only an inline faucet attachment

### 2. US6145670A — Bathtub spout with removable filter
- Signal:
  - bathtub-specific spout/filter concept exists
  - framed around chlorine, odor, heavy metals, and sediment
- Relevance:
  - strong direct category-relevance patent hit

### 3. US6096197A / US6267887B1 — Shower/tub filter for chlorine removal and scale deposit prevention
- Signal:
  - dual-purpose shower/tub architecture
  - replaceable cartridge logic
  - chlorine-removal media plus scale-inhibiting media
- Relevance:
  - suggests bathtub-filter technical paths may overlap heavily with shower-filter IP and engineering logic

### 4. US7682513B2 — Water dechlorination means
- Signal:
  - housing with water-soluble dechlorination media and fluid transfer media
  - broad bath / bathing-facility treatment relevance class surfaced in search snippet
- Relevance:
  - indicates alternative dechlorination route beyond classic inline cartridge concepts

### 5. FR2480822A1 — Ion exchange resin water softener for shower bath sprays
- Signal:
  - point-of-use treatment for showerhead or tap
  - addresses limestone and/or chlorine in water used for shower/bathtub fill
- Relevance:
  - useful background signal for “softening + chlorine” combined claim space

## Early technical-route interpretation
The patent layer suggests at least four technical families worth separating in the wiki:
1. bathtub-spout / tub-faucet attached inline filters
2. shower/tub dual-purpose cartridge systems
3. immersion dechlorination accessories (e.g. sulfite-media bath products)
4. broader bath-water treatment / recirculation / sanitization systems (lower direct consumer relevance, but useful adjacency)

## Strategic implication
The topic should no longer be treated as only a market/evidence question.
It now clearly has a patent / technical-route branch that may be important for:
- feasibility
- claim credibility
- cartridge architecture
- compatibility strategy
- IP crowding / adjacency to shower-filter prior art

## Suggested next actions
- create a reusable academic-search protocol page
- create a bathtub-filter patent / technical landscape page
- separate direct-consumer bathtub-filter patents from broader whirlpool / spa / bath-treatment patents
- later, move from hit discovery into clustered patent families / assignees / expiry review
