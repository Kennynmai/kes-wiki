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
domains: [kes, certification, compliance, sku-data, internal-source]
source_type: internal-doc
extraction_mode: direct-readout
source_title: KES certification / compliance source-table readout
source_date: 2026-05-30
source_author: user-provided DingTalk Notable and local database readout
raw_path: raw/company/certifications/2026-05-30-kes-certification-source-table-readout.md
verification_status: unverified
related:
  - ../company/kes-certifications-and-compliance-register.md
---

# Source Summary — KES Certification / Compliance Source-Table Readout (2026-05-30)

## Why this source matters
This is the current internal anchor for KES certification and compliance coverage by certification family. It is more current than the local `dim_sku_certification` table for DOE status because the source-table read was performed on 2026-05-30 while local sync was last recorded on 2026-05-25.

## Extracted facts / observations
- KES currently has 10 certification / compliance surfaces in the source-table readout:
  - cUPC
  - NSF/ANSI/CAN 61
  - NSF/ANSI/CAN 372
  - DOE Compliance Certification
  - CEC Compliance
  - CE Certificate of Conformity
  - UKCA Certificate of Conformity
  - EPA WaterSense lavatory faucets
  - EPA WaterSense showerheads
  - ISO 9001:2015 QMS certification
- All 10 are reported as valid.
- SKU-level coverage is highest for UKCA (1,142), CEC (828), CE (705), DOE (493), and cUPC (335).
- NSF/ANSI/CAN 61 and 372 each cover 202 SKUs.
- WaterSense is reported as 31 total SKUs, but the source SKU table does not distinguish lavatory faucets from showerheads.
- ISO 9001 is company-level and does not have SKU granularity.
- DOE status differs from the local table: local `dim_sku_certification` still had 24 pending SKUs, while direct source-table read shows DOE fully certified.

## Caveats / ambiguity
- Verification status remains `unverified` until certificate PDFs, listing pages, DOE CCMS, CEC MAEDbS, WaterSense product search, and ISO certificate details are checked and linked.
- The internal readout provides coverage counts and status, but not certificate numbers, issue dates, expiration dates, factory scope, report numbers, or SKU lists.
- CE and UKCA need special handling because conformity certificates, test reports, declarations of conformity, and statutory CE/UKCA marking are not interchangeable evidence types.

## Affected pages
- [KES Certifications and Compliance Register](../company/kes-certifications-and-compliance-register.md)

## Sources
- [Raw capture — KES certification / compliance source-table readout](../../raw/company/certifications/2026-05-30-kes-certification-source-table-readout.md)
