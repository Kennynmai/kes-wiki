---
type: source-summary
status: draft
owner: strategy
created: 2026-04-12
updated: 2026-04-12
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, academic-search, patents, api-fetch]
source_type: api-fetch
extraction_mode: direct-api
review_cycle: monthly
verification_status: spot-checked
related:
  - ../products/bathtub-filter.md
  - ../products/bathtub-filter-patent-table.md
  - ../syntheses/bathtub-filter-patent-and-technical-landscape.md
  - ../playbooks/academic-search-workflow.md
---

# Source Summary — Bathtub Filter API-Backed Academic and Patent Fetch (2026-04-12)

## Why this source matters
This source upgrades the bathtub-filter topic from manual browsing/search-only work to repeatable API-backed retrieval plus direct patent-page fetching.

It demonstrates that the topic can now be supported by a lightweight research tooling layer rather than only ad hoc searching.

## Academic stack actually used
- OpenAlex API
- Crossref API
- Europe PMC API

## Patent retrieval actually used
- direct public Google Patents page fetch for known patent IDs

## Important tooling note
A direct PatentsView-style patent API call was attempted, but the legacy endpoint now returns a migration message because PatentsView is moving into the USPTO Open Data Portal.

So the practical state is:
- academic APIs are already directly usable and integrated
- public patent detail fetching is currently working through Google Patents page retrieval
- USPTO/PatentsView migration should be revisited later if a stable new patent-search endpoint becomes available

## High-value academic results confirmed via API
### Targeted PMID lookups confirmed
- PMID 12692355: chlorine in bathing water / atopic skin paper confirmed with DOI metadata
- PMID 22591883: 2012 infant swimming / hard water / atopy paper confirmed with DOI metadata, still non-OA in the returned metadata
- PMID 27241890: early-life water hardness/chlorine / AD study confirmed with DOI metadata
- PMID 33259122: systematic review / meta-analysis confirmed with DOI metadata
- PMID 37029288: swimming / AD review confirmed with PMCID `PMC10946598`, OA = yes, and Europe PMC fullTextXML available

### Strategic academic implication
The academic API layer is already useful for:
- DOI/PMID/PMCID normalization
- OA status checking
- manuscript/full-text opportunity checking
- broad related-paper expansion around hard water / chlorine / swimming / eczema

## High-value patent results confirmed via direct fetch
### Strongest direct category hit
- `US6145670A` — *Bathtub spout with removable filter*
  - direct bathtub-spout architecture
  - strong relevance to tub-fill compatibility and removable filter housing logic

### Strongest shower/tub crossover hits
- `US6096197A` — *Shower filter for chlorine removal and scale deposit prevention*
- `US6267887B1` — *Shower filter for chlorine removal and scale deposit prevention*
  - strong evidence that bathtub-filter architecture overlaps with shower/tub dual-purpose cartridge logic

### Strongest alternative dechlorination route hit
- `US7682513B2` — *Water dechlorination means*
  - notable because the claims point to water-soluble dechlorination media and explicitly mention ascorbic acid in sampled claims

### Strongest immersion-style bath treatment hit
- `JP3002925U` — *Chlorine remover for bath water*
  - strong signal that immersion dechlorination accessories belong in the category map, not only inline filter units

## Strategic implication
The research base now has a real tooling layer underneath it.

That means future bathtub-filter work can be more systematic in three ways:
1. academic verification can be repeated instead of re-searched manually every time
2. patent detail capture can be normalized into comparable rows
3. topic expansion can now happen from API-backed evidence rather than only web snippets

## Files produced in this run
- `tools/bathtub_filter_api_fetch.py`
- `data/products/bathtub-filter/api-fetch/2026-04-12-academic.json`
- `data/products/bathtub-filter/api-fetch/2026-04-12-academic.md`
- `data/products/bathtub-filter/api-fetch/2026-04-12-patents.json`
- `data/products/bathtub-filter/api-fetch/2026-04-12-patents.md`

## Sources
- `raw/products/bathtub-filter/2026-04-12-academic-search-and-patent-scouting.md`
- `data/products/bathtub-filter/api-fetch/2026-04-12-academic.json`
- `data/products/bathtub-filter/api-fetch/2026-04-12-patents.json`
