---
type: source-summary
status: active
owner: operations
created: 2026-05-30
updated: 2026-05-30
visibility: team
confidence: high
officiality: draft
domain: operations
domains: [kes, certification, compliance, public-records, product-listings]
source_type: public-record
extraction_mode: targeted-official-online-verification
source_title: KES official online certification verification pass
source_date: 2026-05-30
source_author: agent
raw_path: ../../raw/company/certifications/2026-05-30-kes-official-online-certification-verification.md
verification_status: spot-checked
related:
  - ../company/kes-certifications-and-compliance-register.md
  - ../source-summaries/kes-doe-cec-public-database-access-2026-05-30.md
  - ../source-summaries/kes-public-certification-model-pattern-inventory-2026-05-30.md
---

# Source Summary — KES Official Online Certification Verification (2026-05-30)

## Why this source matters
This pass upgrades the KES certification register from general verification routes to specific public evidence where available. It identifies which certifications have official online KES records, which entity is listed, what product/model families are visible, and where public evidence is still missing.

## Strongest KES-specific findings
- IAPMO PLD currently lists 5 active records for `KES HOME (U.S.) LIMITED`: cUPC file `10664`, NSF/ANSI/CAN 372 / lead-free file `10666`, WaterSense lavatory faucet file `16508`, WaterSense showerhead file `16509`, and NSF/ANSI/CAN 61 file `N-10665`.
- The current IAPMO cUPC record uses `ASME A112.18.1-2024 / CSA B125.1-24`, is active, and the certificate-preview data shows effective date `2024-12-31`, revised date `2026-03-19`, expiration date `2029-12-31`, and 124 listed model patterns.
- The current IAPMO NSF/ANSI/CAN 372 record is active under file `10666`, covers lead-free plumbing products, references `NSF/ANSI/CAN 372-2024`, and shows 80 listed model patterns.
- The current IAPMO NSF/ANSI/CAN 61 record is active under file `N-10665`, references `NSF/ANSI/CAN 61-2023`, and shows 80 listed model patterns.
- IAPMO WaterSense files `16508` and `16509` state that the listings are current as of `05/30/2026`. They list 12 KES bathroom sink faucet model patterns and 6 KES showerhead / shower faucet set model patterns.
- EPA WaterSense public API independently returns the same KES model sets: 12 faucet rows and 6 showerhead rows.

## Evidence boundaries
- IAPMO public model-pattern counts are not the same as internal SKU counts. Internal SKU coverage includes finish, package, marketplace, or variant-level mapping.
- Exact string matching is not reliable across public KES listings. WaterSense rows use flow-specific strings such as `F12` / `F18`, while IAPMO product certificates use broader `***` / `**` model-pattern slots; NSF 61 rows may also display a `Q` marker. The dedicated model-pattern inventory records these normalization rules.
- Historical IAPMO PDF certificates found on public Amazon media are useful for prior entity / model evidence, but they are not current-listing proof. The PDFs themselves direct users to PLD for current listing status.
- DOE and CEC are still internally evidenced only in this pass. No KES-specific public DOE CCMS or CEC MAEDbS rows were retrieved.
- A follow-up DOE / CEC access pass confirmed that CEC Advanced Search exposes the relevant `Plumbing Products -> Plumbing Fittings / Plumbing Fixtures` path, while DOE still returned HTTP `403`; this still did not produce KES-specific public rows.
- CE, UKCA, and ISO 9001 remain internally evidenced only in this pass. No public KES-specific issuer verification pages were found.

## Affected pages
- [KES Certifications and Compliance Register](../company/kes-certifications-and-compliance-register.md)
- [Source Summary — KES DOE / CEC Public Database Access (2026-05-30)](kes-doe-cec-public-database-access-2026-05-30.md)
- [Source Summary — KES Public Certification Model-Pattern Inventory (2026-05-30)](kes-public-certification-model-pattern-inventory-2026-05-30.md)

## Sources
- IAPMO R&T Product Listing Directory: <https://pld.iapmo.org/>
- IAPMO PLD API endpoint observed from public app: <https://pld-api.iapmo.org/api/search/myplc>
- IAPMO WaterSense file 16508: <https://mirobase.iapmo.org/pld/listing_watersense.aspx?file=16508>
- IAPMO WaterSense file 16509: <https://mirobase.iapmo.org/pld/listing_watersense.aspx?file=16509>
- EPA WaterSense Product Search: <https://lookforwatersense.epa.gov/>
- EPA WaterSense API base: <https://api.epa.gov/watersense>
- DOE implementation, certification, and enforcement: <https://www.energy.gov/cmei/buildings/implementation-certification-and-enforcement>
- CEC appliance regulations certification assistance: <https://www.energy.ca.gov/rules-and-regulations/appliance-efficiency-regulations-title-20/appliance-regulations-certification>
- CEC Public Search Help PDF: <https://cacertappliances.energy.ca.gov/Help/PublicSearchHelp.pdf>
