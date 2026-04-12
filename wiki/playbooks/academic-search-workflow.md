---
type: playbook
status: draft
owner: strategy
created: 2026-04-12
updated: 2026-04-12
visibility: company
confidence: medium
officiality: draft
domain: operations
domains: [research, academic-search, evidence, product-research]
review_cycle: quarterly
verification_status: spot-checked
related:
  - ../playbooks/market-research-workflow.md
  - ../products/bathtub-filter.md
---

# Academic Search Workflow

## Trigger / scope
Use this workflow when a product/category question starts depending on academic literature, institutional guidance, or manuscript / repository retrieval rather than ordinary web content alone.

This became relevant for the bathtub-filter topic because:
- the category logic depends partly on water / skin / eczema evidence
- PubMed/PMC alone did not fully solve access and discovery needs
- manuscript / repository availability became a practical research issue

## Goal
Build an evidence base that is:
- traceable
- updateable
- access-aware
- separated from product-claim overreach

## Recommended stack priority
### First-line infrastructure
1. **Crossref**
   - DOI metadata backbone
   - useful for normalization, titles, journals, dates, and reference metadata

2. **OpenAlex**
   - work graph, author graph, cited-by graph
   - especially useful for open-access status and repository/full-text discovery signals

3. **Europe PMC**
   - especially strong for biomedical topics
   - useful for PMCID/PMID mapping and fullTextXML retrieval when direct PMC body access is awkward

### Optional second line
4. **Semantic Scholar**
   - useful for related-paper expansion and citation-neighborhood discovery
   - not the first choice for authoritative metadata normalization

### Deprioritized for initial build
- Google Scholar-style APIs

Reason:
- weak official API path
- many options are crawler wrappers
- stability / captcha / compliance burden is likely too high for the first implementation

## Core workflow
1. define the exact evidence question
2. separate **problem-level evidence** from **product-level evidence**
3. search metadata systems first (Crossref / OpenAlex / Europe PMC)
4. capture best-access state for each target
5. pull only the amount of text needed for interpretation
6. write source-summary pages before upgrading canonical product pages
7. record access level explicitly

## Access-state vocabulary
Use one of these when summarizing evidence retrieval:
- full text obtained
- accepted manuscript / near-full text obtained
- long abstract obtained
- detailed repository abstract obtained
- body paragraphs obtained
- snippet only
- blocked

## Quality guardrails
### Keep these separate
- what the study says
- what the study does not say
- what the study helps explain
- what the study can support commercially

### Red flags
- converting problem relevance into product efficacy
- using authority guidance as proof of finished-product performance
- overstating repository/manuscript access when only snippet or abstract was obtained

## Best use cases
This workflow is strongest when KES needs:
- category relevance validation
- claim-discipline support
- segment plausibility checks
- evidence access auditing

It is weaker as a direct substitute for:
- product testing
- certification review
- patent / technical freedom-to-operate review

## Write-back outputs
Expected outputs include:
- raw capture note
- source-summary page
- bibliography update
- evidence matrix update
- canonical page update only after synthesis is clear

## Sources
- [Market Research Workflow](./market-research-workflow.md)
- `raw/products/bathtub-filter/2026-04-12-academic-search-and-patent-scouting.md`
