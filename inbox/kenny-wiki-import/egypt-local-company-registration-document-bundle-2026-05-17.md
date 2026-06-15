---
type: source-summary
status: active
created: 2026-05-22
updated: 2026-05-22
source_type: company-registration-document-bundle
extraction_mode: document-inventory-and-key-field-extraction
source_title: Egypt local company registration, tax, bank, and lease documents
source_date: 2026-05-17
domain: operations
domains: [operations, egypt, company-registration, banking, tax, legal, lease, partnership]
confidence: medium
verification_status: unverified
source:
  - ../../raw/egypt/company-registration/2026-05-17-egypt-company-registration-document-bundle.md
related:
  - ../projects/egypt-local-company-profile.md
  - ../questions/egypt-project-open-investigation-questions.md
  - ../questions/egypt-curtain-manufacturing-investment-research.md
---

# Egypt Local Company Registration Document Bundle - 2026-05-17

## Why this source matters
This document bundle is the current source of record for KES Egypt's local company identity, ownership, tax registration, commercial registration, bank account, and lease file. It establishes that a local Egyptian company exists and has at least some tax, commercial, and bank setup completed.

It does not establish that the company is ready for manufacturing, production-supplies import, factory operation, or industrial licensing.

## Document package
- Incorporation contract PDF and Word file.
- Commercial register certificate.
- Tax card.
- Taxpayer basic data document.
- VAT registration certificate.
- Bank information letter from Kuwait Financing House - Egypt, TEDA Branch.
- Company lease contract.

## Key extracted facts
- Company: `KESliving for retail and wholesale trade` / `كيسلافينج لتجارة التجزئة والجملة`.
- Legal form: limited liability company.
- Legal framework referenced: Egypt Law 72 of 2017.
- Registered purpose from incorporation contract: retail and wholesale trade; trade of furniture and household tools.
- Registered capital: EGP 2,800,000, divided into 2,800 quotas of EGP 1,000 each.
- Ownership:
  - MAI Holdings Limited: 90%.
  - MAI KEFENG: 4%.
  - DENG JIECONG: 3%.
  - ZHANG TAOTAO: 3%.
- Manager: MAI KEFENG.
- Commercial register visually read number: `283540`.
- Tax registration number visually read: `773934154`.
- Tax-card activity visually read: `4649`, wholesale trade of other household tools.
- Bank: Kuwait Financing House - Egypt, TEDA Branch.
- Bank branch address supplied by user: Suez Canal Economic Zone, 3rd Sector, north west Suez Gulf, TEDA Zone, Ain Sokhna, TEDA Branch.
- Bank accounts exist in EGP and USD, with SWIFT code `DEIBEGCXXXX`; see raw bundle for full account and IBAN fields.
- `Date 17052026.pdf` was supplied as a continuation file and is hash-identical to the already archived KFH Egypt bank letter.

## Important interpretation
The company setup appears to support a trading/retail/wholesale commercial entity. This is consistent with the current strategy of starting light, using sales/channel validation, and keeping factory production as a later or separate capability.

For the Egypt curtain/furnishing project, the key implication is negative evidence as much as positive evidence:
- positive: company, tax, commercial registration, bank, and lease documents exist;
- not yet proven: industrial production permission, factory address registration, IDA operating license, industrial register, GOEIC production-supplies basis, and customs/NAFEZA/ACI readiness for production inputs.

## Caveats / tensions
- Most PDFs are scanned and not machine-readable. Field extraction is partly visual and must be verified.
- The Word incorporation contract is machine-readable and should be preferred for company name, purpose, capital, ownership, and manager fields.
- Address fields appear to vary across documents and should be reconciled before bank, tax, import, IDA, GOEIC, NAFEZA, or contract use.
- User supplied the company address as: Cairo, Maadi, apartment 31, 3rd floor, building 141, street 18, Sarayt elmaadi. This should be reconciled against the incorporation contract and tax documents before use.
- The lease contract is archived but not yet extracted or legally reviewed.
- The VAT registration certificate is archived but not reliably extracted.

## Suggested wiki updates
- Maintain a single company profile page for KES Egypt local company facts.
- Update the open investigation page to distinguish `registered trading company` from `production-ready industrial company`.
- Use the registration documents as inputs to the import-readiness and lease/IDA review protocols.

## Sources
- ../../raw/egypt/company-registration/2026-05-17-egypt-company-registration-document-bundle.md
