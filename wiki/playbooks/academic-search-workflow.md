---
type: playbook
status: draft
owner: strategy
created: 2026-04-12
updated: 2026-04-17
visibility: company
confidence: medium
officiality: draft
domain: operations
domains: [research, academic-search, evidence, product-research]
review_cycle: quarterly
verification_status: spot-checked
related:
  - ../playbooks/market-research-workflow.md
  - ../products/bathtub-filter/bathtub-filter.md
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
### First-line infrastructure (metadata backbone)
1. **Crossref**
   - DOI metadata backbone
   - useful for normalization, titles, journals, dates, and reference metadata
   - query pattern: `https://api.crossref.org/works?query=<terms>&rows=N`

2. **OpenAlex**
   - work graph, author graph, cited-by graph
   - especially useful for open-access status and repository/full-text discovery signals
   - **correct usage**: look up by DOI (`/works/doi:<DOI>`) to get W-ID, then traverse `related_works` and `cited_by_api_url`
   - free-text search is noisy for older papers — prefer Crossref → OpenAlex-by-DOI chain

3. **Europe PMC**
   - especially strong for biomedical topics
   - useful for PMCID/PMID mapping and fullTextXML retrieval when direct PMC body access is awkward
   - **also the de-facto preprint search** — append `AND SRC:PPR` to cover bioRxiv / medRxiv / Preprints.org in one query (see preprint-layer note below)

4. **Unpaywall** *(added 2026-04-17)*
   - OA-location resolver — given a DOI, returns `is_oa`, `oa_status`, `best_oa_location`, license
   - query pattern: `https://api.unpaywall.org/v2/<DOI>?email=<your-email>`
   - runs right after Crossref to decide access state before any scraping
   - catches OA-status drift that OpenAlex's snapshot misses (e.g. a hybrid journal flipping an article to cc-by)

### Second line (coverage extenders)
5. **CORE API** *(added 2026-04-17)*
   - aggregator of OA repositories — surfaces theses, protocols, accepted manuscripts that Crossref/OpenAlex miss
   - anonymous search works without a key: `https://api.core.ac.uk/v3/search/works?q=<terms>&limit=N`
   - in our 2026-04-17 test, surfaced the SOFTER trial protocol (hardness + AD prevention, BMJ Open 2019) that the mainline chain did not prioritize

6. **Epistemonikos** *(added 2026-04-17)*
   - systematic-review and guideline aggregator — best entry point for claim-discipline evidence
   - use the web search UI (`epistemonikos.org/en/search?q=<terms>&classification=systematic-review`) — the public JSON API returns 405 on GET
   - in our 2026-04-17 test, surfaced five AD-bathing SRs (Gittler 2016, Koutroulis 2015, daily-bathing 2020, bleach-bath MAs) that were absent from the institutional-guidance layer

7. **Semantic Scholar**
   - useful for related-paper expansion and citation-neighborhood discovery
   - not the first choice for authoritative metadata normalization
   - increasingly overlapped by OpenAlex `related_works`, so demote unless OpenAlex graph is thin for the target

### Preprint layer *(added 2026-04-17)*
- **Primary path**: Europe PMC with `SRC:PPR` filter — covers bioRxiv, medRxiv, Preprints.org, Research Square, Authorea in one query
- **Do not rely on** the bioRxiv/medRxiv HTML search (returns 403 to scripted access) or their native JSON APIs (DOI-lookup only, no keyword search)
- Preprints demand extra care — flag them as `preprint` in the bibliography and re-check for peer-reviewed version before promoting to a canonical page

### Discovery-only layer — use, do not cite *(added 2026-04-17)*
These tools aid hypothesis expansion and screening but **must not be cited as evidence sources**. Always resolve back to a DOI and re-verify through Crossref / OpenAlex / Europe PMC before writing to a bibliography or evidence matrix.

- **ResearchRabbit** — citation-neighborhood exploration; Zotero sync; free account
- **Connected Papers** — similarity-graph visualization from a DOI seed; limited free queries
- **Elicit** — structured extraction across 100s–1000s of papers (study design, effect size, sample); useful for the *source-summary* stage when scanning many abstracts
- **Scite** — "supporting / contrasting / mentioning" citation classification; direct value for claim-discipline but paywalled beyond a small free quota

### Deprioritized
- **Google Scholar-style APIs**
  - weak official API path
  - many options are crawler wrappers
  - stability / captcha / compliance burden too high for the first implementation

- **Trip Database** *(added 2026-04-17 — now downgraded)*
  - public search blocked for scripted access (`ECONNREFUSED` / Cloudflare) and serious usage requires a paid plan
  - Epistemonikos covers most of the overlap; only return to Trip if a manual UI session is justified

## Core workflow
1. define the exact evidence question
2. separate **problem-level evidence** from **product-level evidence**
3. search metadata systems first (Crossref / OpenAlex-by-DOI / Europe PMC)
4. **append preprint sweep** — run the same query against Europe PMC with `AND SRC:PPR` to catch recent preprint-only mechanism studies
5. **append synthesis sweep** — run the topic against Epistemonikos to pull systematic reviews and guidelines before trusting any single primary study
6. **resolve access** via Unpaywall for each target DOI; fall back to CORE for repository copies when Unpaywall reports closed
7. (optional) use Elicit / ResearchRabbit as discovery aids; always round-trip back to a DOI before citing
8. capture best-access state for each target
9. pull only the amount of text needed for interpretation
10. write source-summary pages before upgrading canonical product pages
11. record access level explicitly

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

## Validation log

### 2026-04-17 — tool-stack expansion dry-run
Anchor question: *free residual chlorine, bathing, atopic skin barrier* (the central evidence lane for the bathtub-filter product concept).

Anchors used: Seki et al. 2003 (DOI `10.1111/j.1346-8138.2003.tb00371.x`) and Lei et al. 2025 (DOI `10.1155/dth/3695790`).

**New signal actually surfaced by the expanded stack, beyond what the original Crossref+OpenAlex+Europe PMC chain produced:**

| Source | Finding | Why it matters |
|---|---|---|
| Unpaywall | Lei 2025 is OA `hybrid`, cc-by, publisher-hosted PDF | The existing evidence bibliography marks Lei 2025 as "全文 paywall" — stale. Needs correction. |
| Europe PMC `SRC:PPR` | Bergera Virassamnaik et al. 2025, Preprints.org, *Comparative Impact of Hard and Chlorinated Water on Biometrological Parameters of Atopic Skin* — directly measures TEWL under hard vs chlorinated vs soft water, plus a dermocosmetic intervention arm | Directly on-question and not in current bibliography. Treat as preprint-tier pending peer review. |
| Europe PMC `SRC:PPR` | Standl et al. 2025, medRxiv, *Gene-environment interaction analysis in atopic eczema* | Gene × environment context; secondary priority but relevant for segment logic. |
| CORE API | SOFTER trial protocol (Briley 2019, BMJ Open) — ion-exchange water softener for AD prevention | Hardens the hardness-vs-chlorine discussion with an RCT-protocol record; adds a registered-trial anchor for the water-hardness pathway. |
| Epistemonikos | Five AD-bathing systematic reviews (Gittler 2016; Koutroulis 2015; Cardona 2020 daily-bathing; Chopra bleach-bath SR 2017; Bakaa bleach-bath MA 2022) | Raises the synthesis layer above single primary studies and provides claim-discipline ceilings — important for the claim-evidence ladder. |

**Tools that did not pay off in this test (but should stay on the list):**
- **ResearchRabbit / Connected Papers / Elicit / Scite** — not tested against live data in this pass (UI-only). Landing-page review confirms they are discovery aids, not citation sources. Use when screening high-volume neighborhoods.
- **Trip Database** — blocked for scripted access; deprioritized above.

**Action items flowing out of this test:**
- [x] Update `bathtub-filter-evidence-bibliography.md` to correct Lei 2025 access state (OA cc-by, not paywall). *(Done 2026-04-17 round 2)*
- [x] Pull Bergera 2025 full abstract via Europe PMC core resultType; added as preprint-tier entry (section 8f). *(Done 2026-04-17 round 2; Preprints.org direct PDF blocked by Cloudflare)*
- [x] Cross-check the five Epistemonikos SRs; all confirmed closed access and added to institutional-guidance.md section 3B. *(Done 2026-04-17 round 2)*
- [x] Review the SOFTER protocol + BEEP trial records — SOFTER protocol (Briley 2019) and SOFTER results (Jabbar-Lopez 2022) both now integrated into evidence-bibliography.md section 8d. *(Done 2026-04-17 round 2)*

### 2026-04-17 round 2 — deep-drive on the bathtub-filter evidence question

After integrating the round-1 tools into the workflow, ran a multi-angle deep search against the same anchor question (chlorine / hardness / bathing / AD skin barrier) to test yield at scale.

**Material new findings beyond round-1 (and beyond the existing bibliography):**

| # | Paper | Access | Why it changed the picture |
|---|---|---|---|
| 1 | **Jabbar-Lopez et al. 2022 — SOFTER trial results** (Clin Exp Allergy, DOI `10.1111/cea.14071`) | OA bronze | First **RCT-level evidence** on water softening for infant eczema prevention. Round 1 only surfaced the protocol paper; round 2 found the results. Non-significant but directional: 33% softener vs 48% control visible eczema at 6 months. |
| 2 | **Bradshaw et al. 2026 — weekly vs daily bathing RCT** (Br J Dermatol, DOI `10.1093/bjd/ljaf417`) | OA hybrid cc-by | First **large RCT (n=438)** on bathing frequency for eczema. POEM diff -0.4 (95% CI -1.3, 0.4, P=0.30) — **no effect**. Upgrades what was previously only SR-level evidence. |
| 3 | **Davis et al. 2026 — AAD pediatric AD guideline** (JAAD, DOI `10.1016/j.jaad.2026.02.113`) | Closed, abstract only | Replaces the 2014 AAD guideline as the US gold-standard reference for claim discipline. Bathing = conditional recommendation. |
| 4 | **Alshalhoob et al. 2025 — seawater therapy SR** (Cureus, DOI `10.7759/cureus.95450`) | OA gold cc-by | Cross-validates Lei 2025's seawater-for-AD mechanism claim at SR level. |
| 5 | **Kortekaas Krohn et al. 2024 — lifestyle + skin microbiota** (Allergy, DOI `10.1111/all.16378`) | OA hybrid cc-by-nc-nd | New angle: bathing / cleansing behaviors interact with skin microbiota homeostasis. |
| 6 | **Kato et al. 2026 — fine bubble shower RCT** (J Dermatol, DOI `10.1111/1346-8138.70117`) | OA hybrid cc-by | Adjacent technology reference for AD-safe cleansing innovation. |

**Yield summary:** one 4-week RCT, one multi-month pilot RCT, one 2026 US clinical guideline, three OA supporting references. All six were missed by the pre-expansion Crossref+OpenAlex+Europe PMC(peer-reviewed only) chain. Europe PMC's `SRC:PPR` filter and an Epistemonikos sweep on "atopic dermatitis + bathing" were the two highest-yield additions.

**Tool-level observations for the workflow:**
- OpenAlex free-text search is noisy for older papers — use Crossref → DOI → `OpenAlex /works/doi:<DOI>` instead.
- OpenAlex `cites:` filter returned empty / unrelated results through WebFetch in this pass — debug before relying on it; meanwhile use Europe PMC's citation API.
- Preprints.org direct PDFs are Cloudflare-blocked; Europe PMC `resultType=core` gives a structured abstract + key findings that is sufficient for the source-summary stage.
- Epistemonikos public JSON API returns 405 on GET; use its web search UI.
- Unpaywall correctly caught one stale access-state claim in the existing bibliography (Lei 2025 marked as paywalled → actually OA cc-by). Add Unpaywall to every DOI resolve, not just new candidates.

**Output trail:** see [Source Summary — Bathtub Filter 扩展学术栈检索 (2026-04-17)](../source-summaries/bathtub-filter-expanded-stack-academic-retrieval-2026-04-17.md) for the full set of DOIs, Unpaywall results, and editorial decisions.

## Sources
- [Market Research Workflow](./market-research-workflow.md)
- `raw/products/bathtub-filter/2026-04-12-academic-search-and-patent-scouting.md`
