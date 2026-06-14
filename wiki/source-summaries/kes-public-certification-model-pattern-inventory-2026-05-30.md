---
type: source-summary
status: active
owner: operations
created: 2026-05-30
updated: 2026-05-30
visibility: team
confidence: medium
officiality: draft
domain: operations
domains: [kes, certification, compliance, model-patterns, sku-governance, public-records]
source_type: public-record
extraction_mode: model-pattern-inventory
source_title: KES public certification model-pattern inventory notes
source_date: 2026-05-30
source_author: agent
raw_path: ../../raw/company/certifications/2026-05-30-kes-public-model-pattern-inventory-notes.md
verification_status: spot-checked
related:
  - ../company/kes-certification-claim-control-matrix.md
  - ../company/kes-certifications-and-compliance-register.md
---

# Source Summary — KES Public Certification Model-Pattern Inventory (2026-05-30)

## Why this source matters
This pass turns the public KES certification records into a model-pattern inventory for claim control. It identifies which model-pattern sets overlap, where exact matching produces false gaps, and what normalization rules are needed before a SKU-level certification table can be trusted.

## Key findings
- IAPMO cUPC file `10664` contains 124 public model patterns.
- IAPMO NSF/ANSI/CAN 372 file `10666` contains 80 public model patterns, and all 80 also appear in cUPC file `10664`.
- IAPMO NSF/ANSI/CAN 61 file `N-10665` contains the same 80 base model patterns as NSF 372 after normalizing the displayed `Q` marker used on many NSF 61 model rows.
- The 18 WaterSense model patterns do not exactly match cUPC model strings, but all 18 map to broader cUPC wildcard patterns after treating `***` and `**` as pattern slots.
- The 12 WaterSense lavatory faucet patterns also map to NSF 372 and NSF 61 faucet patterns after wildcard and `Q` normalization.
- The 6 WaterSense showerhead / shower faucet set patterns map to cUPC wildcard patterns only in this public dataset; they do not map to NSF 61 / 372 public rows observed in this pass.

## Claim-control consequence
The biggest operational risk is false certainty from exact-string matching. For example, `L3156ALFF12-**` does not exactly equal `L3156ALF***-**`, but it is likely a flow-specific row under the broader certificate pattern. SKU mapping should therefore use normalized pattern matching, then preserve the original evidence strings for audit.

This does not make wildcard matching a final approval rule. External claims still require SKU-level mapping and owner review.

## Affected pages
- [KES Certification Claim-Control Matrix](../company/kes-certification-claim-control-matrix.md)
- [KES Certifications and Compliance Register](../company/kes-certifications-and-compliance-register.md)

## Sources
- [Raw capture — KES public certification model-pattern inventory notes](../../raw/company/certifications/2026-05-30-kes-public-model-pattern-inventory-notes.md)
- IAPMO R&T Product Listing Directory: <https://pld.iapmo.org/>
- EPA WaterSense Product Search: <https://lookforwatersense.epa.gov/>
