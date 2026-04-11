---
source_type: market-brief
extraction_mode: direct-fetch
created: 2026-04-11
updated: 2026-04-11
status: captured
domain: product
domains: [bathtub-filter, fetch-attempts, evidence-access]
confidence: medium
visibility: team
officiality: working
verification_status: unverified
---

# Raw Capture — Bathtub Filter Web Content Fetch Attempts and Results (2026-04-11)

## Purpose
Track attempts to obtain fuller web content for key evidence sources beyond search snippets and short visible summaries.

## Methods attempted
- web search for alternative web versions
- direct page HTML retrieval
- 12ft.io
- Unpaywall-style route
- RemovePaywall-style route
- direct extraction from public HTML metadata / paragraphs / abstract blocks

## Summary of results
### Successful / partially successful
#### 1. PubMed — residual chlorine in bathing water and atopic skin
URL:
- `https://pubmed.ncbi.nlm.nih.gov/12692355/`

Result:
- page accessible
- long abstract successfully extracted from HTML

High-value extracted content:
- study included 20 patients with AD and 10 normal controls
- tested comfortably hot water at 40°C with residual chlorine concentrations of 0, 0.5, 1.0, and 2.0 mg/L
- in AD patients, average stratum corneum hydration after immersion at 1.0 and 2.0 mg/L chlorine was significantly lower than after negligible chlorine water

Usefulness:
- stronger than snippet-level evidence
- still abstract-level, but materially more informative

#### 2. PubMed — domestic water hardness, chlorine, and AD risk in early life
URL:
- `https://pubmed.ncbi.nlm.nih.gov/27241890/`

Result:
- page accessible
- long abstract successfully extracted from HTML

High-value extracted content:
- 1303 three-month-old infants recruited
- domestic water CaCO3 and chlorine concentration data gathered from local water suppliers
- visible AD more common in all three non-baseline water-quality groups vs baseline low CaCO3/low chlorine group
- effect estimates greater in children carrying FLG mutations according to abstract text

Usefulness:
- materially strengthens evidence on water-quality relevance in infancy
- still not product-level evidence

#### 3. National Eczema Society — swimming and eczema
URL:
- `https://eczema.org/information-and-advice/triggers-for-eczema/swimming-and-eczema/`

Result:
- page accessible
- substantial visible paragraphs extracted from HTML

High-value extracted content:
- swimming is described as reasonably skin-friendly exercise because it does not involve getting too hot and sweaty
- pools maintain hygiene with chlorine and other chemicals
- pool water can irritate the skin of some people with eczema
- not everyone with eczema experiences the same degree of irritation

Usefulness:
- strong authority-style nuance source
- good for balanced education / claim restraint

#### 4. EPA — CCR information for consumers
URL:
- `https://www.epa.gov/ccr/ccr-information-consumers`

Result:
- page accessible
- basic content visible in HTML

High-value extracted content:
- EPA requires community water systems to deliver Consumer Confidence Reports, also known as annual water quality reports
- EPA provides an online search tool and quick reference materials

Usefulness:
- good official source for water-quality awareness framing

### Unsuccessful / constrained
#### 5. PMC review — Pooling the evidence: A review of swimming and atopic dermatitis
URL:
- `https://pmc.ncbi.nlm.nih.gov/articles/PMC10946598/`

Result:
- direct HTML attempt hit reCAPTCHA / browser check page
- no reliable article-body retrieval obtained in this session

Usefulness:
- can still rely on title / search snippet level for now
- should revisit later via browser workflow or alternative access path

## Tool/path-specific notes
### 12ft.io
- encountered SSL / certificate verification issue in this environment
- no dependable output obtained

### Unpaywall-style route
- no useful response for these targets in this session

### RemovePaywall-style route
- landing content available but not dependable article-body retrieval for target pages in this session

## Working conclusion
Direct HTML retrieval can improve evidence quality for some sources, especially PubMed and simpler institutional pages. For dynamic or protected pages (e.g. PMC browser checks), fallback to snippets / citations remains necessary until a better retrieval path is available.
