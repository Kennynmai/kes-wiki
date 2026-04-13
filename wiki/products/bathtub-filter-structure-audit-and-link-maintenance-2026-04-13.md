---
type: product
status: draft
owner: strategy
created: 2026-04-13
updated: 2026-04-13
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, structure, obsidian, maintenance, audit]
source_count: 0
review_cycle: monthly
verification_status: working
related:
  - ./bathtub-filter.md
  - ./bathtub-filter-obsidian-map.md
  - ./bathtub-filter-review-patterns-and-return-risk.md
  - ./bathtub-filter-normal-flow-vs-reduced-flow-evidence-table.md
---

# Bathtub Filter Structure Audit and Link Maintenance (2026-04-13)

## Obsidian links
- [[bathtub-filter]]
- [[bathtub-filter-obsidian-map]]
- [[bathtub-filter-kes-route-elimination-memo-v1]]
- [[bathtub-filter-marketplace-negative-review-signals]]
- [[bathtub-filter-swimming-eczema-explanation-layer-2026-04-12]]
- [[bathtub-filter-web-content-fetch-attempts-2026-04-11]]

## Why this page exists
This page tracks structural maintenance needs for the bathtub-filter cluster so the topic remains easy to browse in Obsidian and easy to maintain over time.

## Current structural findings
### 1. Core pages are now noticeably better linked
The canonical page plus the newest decision-support pages now contain `[[wikilinks]]` and a dedicated navigation hub exists at [[bathtub-filter-obsidian-map]].

### 2. Many older pages still have weak Obsidian connectivity
A large number of bathtub-filter pages still have:
- zero `[[wikilinks]]`
- only sparse markdown links
- low backlink counts

This means the cluster is still navigable, but not yet graph-friendly.

### 3. Some pages are structurally weak despite likely importance
Examples surfaced in audit:
- [[bathtub-filter-validation-testing-protocol]] has very low backlink depth
- [[bathtub-filter-swimming-eczema-explanation-layer-2026-04-12]] currently appears to have zero backlinks
- several v1 pages still exist but are not clearly marked as superseded in the graph layer

### 4. v1 / v2 relationships need explicit handling
Observed pairs that should be made clearer:
- [[bathtub-filter-brand-operating-matrix]] ↔ [[bathtub-filter-brand-operating-matrix-v2]]
- [[bathtub-filter-channel-positioning-table]] ↔ [[bathtub-filter-channel-positioning-table-v2]]
- [[bathtub-filter-claim-risk-audit]] ↔ [[bathtub-filter-claim-risk-audit-v2]]
- [[bathtub-filter-installation-risk-matrix]] ↔ [[bathtub-filter-installation-risk-matrix-v2]]
- [[bathtub-filter-pricing-refill-flow-fit-table]] ↔ [[bathtub-filter-pricing-refill-flow-fit-table-v2]]
- [[bathtub-filter-kes-route-screening-memo-v1]] ↔ [[bathtub-filter-kes-route-screening-memo-v2]]

## Maintenance recommendations
### Priority 1 — graph usability
- add `[[wikilinks]]` to all high-value product, synthesis, and source-summary pages
- add one short “Obsidian links” section near the bottom of each important page

### Priority 2 — version hygiene
- add explicit `Supersedes` / `Superseded by` sections for v1/v2 pairs
- reduce ambiguity about which page should be read first

### Priority 3 — orphan reduction
- add backlinks to low-linked but strategically useful pages
- especially testing, evidence-access, and explanation-layer pages

### Priority 4 — cluster hubs
- keep [[bathtub-filter]] as the canonical page
- keep [[bathtub-filter-obsidian-map]] as the click-through hub
- optionally add sub-hubs later for claims/compliance and technical/testing

## Suggested next structure pass
1. add version-crosslinks to all v1/v2 pairs
2. add `[[wikilinks]]` to source-summary pages
3. add backlinks to weak pages from [[bathtub-filter-obsidian-map]] and [[bathtub-filter]]
4. later consider archiving or visually de-emphasizing outdated v1 surfaces
