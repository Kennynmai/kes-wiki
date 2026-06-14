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
domains: [kes, certification, compliance, doe, cec, public-records, database-access]
source_type: public-record
extraction_mode: targeted-public-database-access
source_title: KES DOE and CEC public database access notes
source_date: 2026-05-30
source_author: agent
raw_path: ../../raw/company/certifications/2026-05-30-kes-doe-cec-public-database-access-notes.md
verification_status: spot-checked
related:
  - ../company/kes-certifications-and-compliance-register.md
---

# Source Summary — KES DOE / CEC Public Database Access (2026-05-30)

## Why this source matters
This pass narrows the retrieval path for the two largest KES legal-compliance datasets: DOE and CEC. It does not add KES-specific public rows, but it records the official access behavior and the exact CEC search path needed for the next export/screenshot pass.

## Findings
- DOE certification-data endpoints for faucets and showerheads returned HTTP `403`, so no KES-specific CCMS rows were retrieved.
- CEC Quick Search redirected to a login URL in command-line access.
- CEC Advanced Search loaded publicly and exposes `Plumbing Products` as a category.
- Selecting `Plumbing Products` populated two relevant appliance types: `Plumbing Fittings` and `Plumbing Fixtures`.
- A follow-up post selecting `Plumbing Fittings` and `Approved` timed out before returning results; no KES-specific MAEDbS rows were captured.
- CEC Company Search loaded publicly, but the default visible company list was for `Test Lab` company type and should not be treated as manufacturer/product listing evidence.

## Practical next step
Use a browser-based CEC MAEDbS Advanced Search capture with:

| Search layer | Value |
|---|---|
| Category | `Plumbing Products` |
| Appliance | `Plumbing Fittings`, then `Plumbing Fixtures` |
| Status | `Approved`, then `Archived` |
| Query terms | `KES`, `KES HOME`, known internal model numbers |

For DOE, use browser-based CCMS access or internal submission exports for faucet and showerhead basic models.

## Affected pages
- [KES Certifications and Compliance Register](../company/kes-certifications-and-compliance-register.md)

## Sources
- [Raw capture — KES DOE and CEC public database access notes](../../raw/company/certifications/2026-05-30-kes-doe-cec-public-database-access-notes.md)
- DOE CCMS faucet certification-data page: <https://www.regulations.doe.gov/certification-data/CCMS-4-Faucets.html>
- DOE CCMS showerhead certification-data page: <https://www.regulations.doe.gov/certification-data/CCMS-4-Showerheads.html>
- CEC MAEDbS Advanced Search: <https://cacertappliances.energy.ca.gov/Pages/Search/AdvancedSearch.aspx>
- CEC MAEDbS Company Search: <https://cacertappliances.energy.ca.gov/Pages/CompanyInfo/CompanyList.aspx>
- CEC Public Search Help PDF: <https://cacertappliances.energy.ca.gov/Help/PublicSearchHelp.pdf>
