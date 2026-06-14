---
source_type: public-record
captured: 2026-05-30
source_title: KES official online certification verification pass
source_author: agent
classification: public-record
extraction_mode: targeted-official-online-verification
verification_status: spot-checked
---

# KES Official Online Certification Verification Pass — 2026-05-30

## Scope
This capture records official or issuer-hosted online evidence found for KES certification / compliance records on 2026-05-30.

It is not a replacement for internal certificate PDFs, regulatory filing confirmations, SKU mappings, or renewal trackers.

## Official KES-specific evidence found

### IAPMO R&T Product Listing Directory

Public query:

- Directory: <https://pld.iapmo.org/>
- API endpoint observed in the PLD web app: `https://pld-api.iapmo.org/api/search/myplc`
- Query used: `searchCategory=listee`, `query=KES HOME`, `searchType=all`

Result: 5 active KES HOME (U.S.) LIMITED records.

| File / project number | Product description | Standard / specification | Status | Public certificate / listing URL |
|---|---|---|---|---|
| 10664 | Plumbing Fixture Fittings | ASME A112.18.1-2024 / CSA B125.1-24 | Active | <http://myplc.iapmo.org/certificate#/18134> |
| 10666 | Lead Free Plumbing Products | Section 1417(d) of the Safe Drinking Water Act; California Health & Safety Code section 116875; NSF/ANSI/CAN 372-2024 | Active | <http://myplc.iapmo.org/certificate#/18135> |
| 16508 | EPA WaterSense High Efficiency Lavatory Faucets | EPA WaterSense High Efficiency Lavatory Faucet Specification, Version 1.0, 2007-10-01 | Active | <https://mirobase.iapmo.org/pld/listing_watersense.aspx?file=16508> |
| 16509 | EPA WaterSense High Efficiency Showerheads | EPA WaterSense Specification for Showerheads, Version 1.1, 2018-07-26 | Active | <https://mirobase.iapmo.org/pld/listing_watersense.aspx?file=16509> |
| N-10665 | Drinking Water System Components - Health Effects | NSF/ANSI/CAN 61-2023 | Active | <http://myplc.iapmo.org/certificate#/18651> |

The IAPMO public certificate-preview API returned these additional current-listing details:

| File / project number | Effective date | Revised date | Expiration date | Current model-pattern count observed | Product family count summary |
|---|---:|---:|---:|---:|---|
| 10664 | 2024-12-31 | 2026-03-19 | 2029-12-31 | 124 | bath / bathroom sink faucets, widespread bathroom sink faucets, kitchen and pull-out kitchen faucets, pot fillers, drinking-water / beverage faucets, showerheads, handheld showers, shower valves, shower faucet sets, tub spouts, bathtub faucets and related plumbing fixture fittings |
| 10666 | 2024-12-31 | 2026-03-18 | 2029-12-31 | 80 | bath / bathroom sink faucets, widespread bathroom sink faucets, kitchen and pull-out kitchen faucets, pot fillers, drinking-water / beverage faucets |
| N-10665 | 2024-11-30 | 2026-03-19 | 2029-11-30 | 80 | same public model-pattern families as 10666 |

Important count note: IAPMO listing model patterns are not the same unit as internal SKU coverage. Internal SKU counts include finish / packaging / SKU variants and source-table mapping.

### IAPMO R&T WaterSense listing pages

The IAPMO WaterSense pages for files 16508 and 16509 state: `This IAPMO R&T Listing is current as of 05/30/2026`.

Issued to:

`KES HOME (U.S.) LIMITED`, `FLAT/RM 5 8F ENTERPRISE SQUARE`, `TWO, 3 SHEUNG YUET ROAD`, `KOWLOON BAY KL HONG KONG`.

Lavatory faucet listing 16508:

| Certification date | Brand | Model name | Model number | Type | Max rated flow |
|---|---|---|---|---|---:|
| 2024-07-18 | KES | bathroom sink faucet | L3156ALFF12-** | Faucet | 1.2 gpm |
| 2024-07-18 | KES | bathroom sink faucet | L3156BLFF12-** | Faucet | 1.2 gpm |
| 2024-07-18 | KES | bathroom sink faucet | L4117LFF12-** | Faucet | 1.2 gpm |
| 2024-07-18 | KES | bathroom sink faucet | L4317ALFF12-** | Faucet | 1.2 gpm |
| 2024-07-18 | KES | bathroom sink faucet | L4317LFF12-** | Faucet | 1.2 gpm |
| 2024-07-18 | KES | bathroom sink faucet | L4350LFF12-** | Faucet | 1.2 gpm |
| 2024-07-18 | KES | bathroom sink faucet | L4150LFF12-** | Faucet | 1.2 gpm |
| 2024-07-18 | KES | bathroom sink faucet | L4355LFF12-** | Faucet | 1.2 gpm |
| 2024-07-18 | KES | bathroom sink faucet | L4327ALFF12-** | Faucet | 1.2 gpm |
| 2024-07-18 | KES | bathroom sink faucet | L4327BLFF12-** | Faucet | 1.2 gpm |
| 2024-07-18 | KES | bathroom sink faucet | L3209LFF12-** | Faucet | 1.2 gpm |
| 2024-07-18 | KES | bathroom sink faucet | L3210LFF12-** | Faucet | 1.2 gpm |

Showerhead listing 16509:

| Certification date | Brand | Model name | Model number | Max rated flow |
|---|---|---|---|---:|
| 2024-07-18 | KES | Shower Faucet Set | XB6305F18-** | 1.8 gpm |
| 2024-07-18 | KES | Shower Faucet Set | XB6230F18-** | 1.8 gpm |
| 2024-07-18 | KES | Shower Faucet Set | XB6223F18-** | 1.8 gpm |
| 2024-07-18 | KES | Shower Faucet Set | XB6202F18-** | 1.8 gpm |
| 2024-07-18 | KES | Handheld Shower | P300F18-** | 1.8 gpm |
| 2024-07-18 | KES | Fixed Showerhead | J215F18-** | 1.8 gpm |

### EPA WaterSense product-search API

Public page and endpoint:

- Product search: <https://lookforwatersense.epa.gov/>
- API base: `https://api.epa.gov/watersense`
- Endpoints used:
  - `/products/faucets/?offset=0&limit=50&keyword=KES`
  - `/products/showerheads/?offset=0&limit=50&keyword=KES`

EPA returned 12 KES faucet rows and 6 KES showerhead rows. The model sets match the IAPMO WaterSense files 16508 and 16509.

EPA faucet rows:

| Brand | Model name | Model number | Type | Max flow |
|---|---|---|---|---:|
| KES | bathroom sink faucet | L3156ALFF12-** | Faucet | 1.2 |
| KES | bathroom sink faucet | L3156BLFF12-** | Faucet | 1.2 |
| KES | bathroom sink faucet | L3209LFF12-** | Faucet | 1.2 |
| KES | bathroom sink faucet | L3210LFF12-** | Faucet | 1.2 |
| KES | bathroom sink faucet | L4117LFF12-** | Faucet | 1.2 |
| KES | bathroom sink faucet | L4150LFF12-** | Faucet | 1.2 |
| KES | bathroom sink faucet | L4317ALFF12-** | Faucet | 1.2 |
| KES | bathroom sink faucet | L4317LFF12-** | Faucet | 1.2 |
| KES | bathroom sink faucet | L4327ALFF12-** | Faucet | 1.2 |
| KES | bathroom sink faucet | L4327BLFF12-** | Faucet | 1.2 |
| KES | bathroom sink faucet | L4350LFF12-** | Faucet | 1.2 |
| KES | bathroom sink faucet | L4355LFF12-** | Faucet | 1.2 |

EPA showerhead rows:

| Brand | Model name | Model number | Max flow |
|---|---|---|---:|
| KES | Fixed Showerhead | J215F18-** | 1.8 |
| KES | Handheld Shower | P300F18-** | 1.8 |
| KES | Shower Faucet Set | XB6202F18-** | 1.8 |
| KES | Shower Faucet Set | XB6223F18-** | 1.8 |
| KES | Shower Faucet Set | XB6230F18-** | 1.8 |
| KES | Shower Faucet Set | XB6305F18-** | 1.8 |

### Static historical IAPMO PDFs

Public Amazon media URLs surfaced historical IAPMO certificate PDFs:

- cUPC file 10664: <https://m.media-amazon.com/images/I/815DAbv7D9L.pdf>
- NSF/ANSI/CAN 61 file N-10665: <https://m.media-amazon.com/images/I/91xsgXoce3L.pdf>

These PDFs confirm historical KES entity / product scope / model lists, but they explicitly state that the certificate is not evidence of current listing and that current listing status must be checked in the IAPMO R&T Product Listing Directory.

Key extracted NSF/ANSI/CAN 61 historical PDF details:

| Field | Value |
|---|---|
| Issued to | KES HOME (U.S.) LIMITED |
| Address | FLAT/RM 5 8F ENTERPRISE SQUARE TWO, 3 SHEUNG YUET ROAD, KOWLOON BAY, KL, HONG KONG |
| Product | Drinking Water System Components - Health Effects |
| Standard | NSF/ANSI/CAN 61-2022 |
| File number | N-10665 |
| Effective date | November 2019 |
| Revised date | 2024-05-13 |
| Void after | November 2024 |
| Scope note | Lead-free requirements are addressed under a separate certificate of listing |

Key extracted cUPC historical PDF details:

| Field | Value |
|---|---|
| Issued to | KES HOME (U.S.) LIMITED |
| Product | Plumbing Fixture Fittings |
| Standard | ASME A112.18.1-2018 / CSA B125.1-18 |
| File number | 10664 |
| Effective date | December 2019 |
| Void after | December 2024 |

## KES-specific official evidence not found in this pass

### DOE Compliance Certification

The DOE public Compliance Certification Database is the expected source for KES faucet / showerhead basic model records. This pass did not retrieve KES-specific DOE rows.

Attempted official access:

- <https://www.regulations.doe.gov/certification-data/CCMS-4-Faucets.html>
- <https://www.regulations.doe.gov/certification-data/CCMS-4-Showerheads.html>

The endpoint returned HTTP 403 in command-line access. Web search did not surface indexed KES-specific DOE rows. Internal DOE source-table status therefore remains the current KES claim source until a CCMS export, screenshot, or browser-based public search record is captured.

### CEC Compliance / MAEDbS

The California Energy Commission certification assistance page says regulated appliance performance must be certified to CEC and that this information is public through MAEDbS. The public search help PDF confirms Quick Search / Advanced Search flows using model number, manufacturer, and brand.

This pass did not retrieve KES-specific MAEDbS rows. Command-line requests to Quick Search / Advanced Search redirected to a login page or timed out. Internal CEC source-table status therefore remains the current KES claim source until a MAEDbS export or screenshots are captured.

### CE / UKCA

Public web search did not find a KES-specific official Global Testing Services verification page, certificate PDF, or issuer database result for the KES CE / UKCA certificates. Internal certificate PDFs, GTS report / certificate numbers, and any GTS verification channel are still required.

### ISO 9001:2015

Public web search did not find a KES-specific XQC / ISO 9001:2015 official verification page. The XQC certificate number, legal entity, site scope, accreditation chain, and verification URL are still required.

## Sources
- IAPMO R&T Product Listing Directory: <https://pld.iapmo.org/>
- IAPMO PLD API endpoint observed from public app: <https://pld-api.iapmo.org/api/search/myplc>
- IAPMO WaterSense file 16508: <https://mirobase.iapmo.org/pld/listing_watersense.aspx?file=16508>
- IAPMO WaterSense file 16509: <https://mirobase.iapmo.org/pld/listing_watersense.aspx?file=16509>
- EPA WaterSense Product Search: <https://lookforwatersense.epa.gov/>
- EPA WaterSense API base: <https://api.epa.gov/watersense>
- DOE implementation, certification, and enforcement: <https://www.energy.gov/cmei/buildings/implementation-certification-and-enforcement>
- DOE faucet product page: <https://www.energy.gov/cmei/buildings/faucets>
- DOE showerhead product page: <https://www.energy.gov/cmei/buildings/showerheads>
- CEC appliance regulations certification assistance: <https://www.energy.ca.gov/rules-and-regulations/appliance-efficiency-regulations-title-20/appliance-regulations-certification>
- CEC Public Search Help PDF: <https://cacertappliances.energy.ca.gov/Help/PublicSearchHelp.pdf>
