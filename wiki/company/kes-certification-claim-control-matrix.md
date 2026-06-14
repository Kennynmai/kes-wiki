---
type: synthesis
status: draft
owner: operations
created: 2026-05-30
updated: 2026-05-30
visibility: team
confidence: medium
officiality: draft
domain: operations
domains: [kes, certification, compliance, claims, sku-governance, product-listings]
source_count: 4
review_cycle: monthly
verification_status: unverified
related:
  - ./kes-certifications-and-compliance-register.md
  - ./kes-sku-certification-mapping-table.md
  - ./kes-certification-evidence-pack-checklist.md
  - ../source-summaries/kes-public-certification-model-pattern-inventory-2026-05-30.md
  - ../source-summaries/kes-official-online-certification-verification-2026-05-30.md
  - ../source-summaries/kes-certification-source-table-readout-2026-05-30.md
  - ../source-summaries/kes-certification-public-reference-scan-2026-05-30.md
aliases:
  - KES certification claim control
  - KES certificate claim matrix
  - KES SKU certification mapping
  - KES 认证话术管控
name_zh: KES 认证 Claim-Control Matrix
name_en: KES Certification Claim-Control Matrix
---

# KES 认证 Claim-Control Matrix

## Purpose
这页用于把 KES certification / compliance 证据转成运营可用的 claim-control 规则。

当前版本是 **public listing / model-pattern level**，不是最终 SKU-level 表。最终安全使用还需要把内部 SKU 映射到公开 model pattern / filing / certificate id。可填的 SKU 工作表见 [KES SKU Certification Mapping Table](./kes-sku-certification-mapping-table.md)，资料归档清单见 [KES Certification Evidence Pack Checklist](./kes-certification-evidence-pack-checklist.md)。

## Claim-Control Principle
每条页面、包装、A+、客服、经销商资料里的认证话术，都应至少能落到这个链条：

`SKU -> product model / public model pattern -> certificate or filing id -> issuer / authority -> allowed wording -> evidence URL / screenshot`

如果只能落到公司级证书或源表总数，不能写成单个 SKU 的产品认证 claim。

## Public Evidence Anchor Table

| Evidence anchor | Entity / brand | Public-current status | Product families visible | Public model-pattern count | Internal source-table coverage | Claim-control role |
|---|---|---|---|---:|---:|---|
| IAPMO cUPC file `10664` | `KES HOME (U.S.) LIMITED` | Active; ASME A112.18.1-2024 / CSA B125.1-24; expires 2029-12-31 in certificate-preview data | lavatory / bathroom sink faucets, kitchen / pull-out kitchen faucets, pot fillers, beverage / drinking-water faucets, showerheads, handheld showers, shower valves, shower faucet sets, tub spouts, bathtub faucets | 124 | 335 SKU | Plumbing-code / plumbing fixture fitting listing anchor |
| IAPMO NSF/ANSI/CAN 372 file `10666` | `KES HOME (U.S.) LIMITED` | Active; NSF/ANSI/CAN 372-2024; expires 2029-12-31 in certificate-preview data | drinking-water-contact faucets, pot fillers, kitchen / pull-out kitchen faucets, beverage / drinking-water faucets | 80 | 202 SKU | Lead-free / lead-content anchor |
| IAPMO NSF/ANSI/CAN 61 file `N-10665` | `KES HOME (U.S.) LIMITED` | Active; NSF/ANSI/CAN 61-2023; expires 2029-11-30 in certificate-preview data | same 80 public model-pattern families as 372 file, with many `Q` optional lower lead markers | 80 | 202 SKU | Drinking-water health-effects anchor |
| IAPMO WaterSense file `16508` + EPA API | IAPMO entity `KES HOME (U.S.) LIMITED`; EPA brand `KES` | IAPMO listing current as of 2026-05-30; EPA API returns active public rows | bathroom sink faucets at 1.2 gpm | 12 | 31 combined WaterSense SKU | Lavatory faucet WaterSense anchor |
| IAPMO WaterSense file `16509` + EPA API | IAPMO entity `KES HOME (U.S.) LIMITED`; EPA brand `KES` | IAPMO listing current as of 2026-05-30; EPA API returns active public rows | fixed showerhead, handheld shower, shower faucet sets at 1.8 gpm | 6 | 31 combined WaterSense SKU | Showerhead WaterSense anchor |
| DOE CCMS | not publicly captured in this pass | internal source-table only | faucets / showerheads expected | not captured | 493 SKU | Legal compliance filing anchor, pending public export |
| CEC MAEDbS | not publicly captured in this pass | internal source-table only | California Title 20 plumbing fittings expected | not captured | 828 SKU | California compliance listing anchor, pending public export |
| CE certificate | not publicly captured in this pass | internal source-table only | EN 817 / EN 1112 product scope expected | not captured | 705 SKU | EU conformity evidence, pending certificate package |
| UKCA certificate | not publicly captured in this pass | internal source-table only | BS EN 817 / BS EN 1112 product scope expected | not captured | 1,142 SKU | GB conformity evidence, pending certificate package |
| ISO 9001:2015 | not publicly captured in this pass | internal source-table only | company / site / QMS scope | company-level | no SKU granularity | Company QMS credibility only |

## Allowed / Blocked Wording

| Certification | Safer wording when SKU is mapped | Blocked or high-risk wording | Why |
|---|---|---|---|
| cUPC | "Listed by IAPMO R&T to ASME A112.18.1 / CSA B125.1 under file 10664" | "NSF certified", "WaterSense certified", "lead-free certified" | cUPC supports plumbing fixture fitting listing, not drinking-water health effects, lead content, or water efficiency |
| NSF/ANSI/CAN 61 | "Certified to NSF/ANSI/CAN 61 for drinking-water system component health effects under IAPMO file N-10665" | "removes lead", "filters contaminants", "purifies water" | NSF 61 is material/contact health-effects certification, not contaminant-reduction performance |
| NSF/ANSI/CAN 372 | "Lead-free certified / certified to NSF/ANSI/CAN 372 under IAPMO file 10666" | "removes lead from water", "lead reduction certified" | 372 is lead-content / lead-free, not lead-removal |
| WaterSense lavatory faucet | "WaterSense labeled bathroom sink faucet, 1.2 gpm, file 16508" | "WaterSense certified drinking-water safety", "NSF certified", "CEC compliant" | WaterSense supports water-efficiency / performance labeling only |
| WaterSense showerhead | "WaterSense labeled showerhead / shower faucet set, 1.8 gpm, file 16509" | "NSF 177 certified", "filter certified", "lead-free certified" | WaterSense showerhead is not a filtration or drinking-water standard |
| DOE | "DOE compliance certification filed for this basic model" only after CCMS proof is attached | "DOE certified quality", "DOE approved" | DOE is legal compliance reporting, not a quality approval badge |
| CEC | "Listed / certified in CEC MAEDbS for California Title 20" only after MAEDbS proof is attached | "CEC certified nationally", "California approved product quality" | CEC is California appliance efficiency compliance |
| CE / UKCA | "Conformity certificate / DoC available for the listed model and applicable standards" only after certificate package is attached | "EU approved", "UK approved", "CE certified quality" | CE / UKCA are marking regimes tied to applicable legislation and declaration files |
| ISO 9001 | "Manufactured / managed under an ISO 9001:2015 certified quality management system" if entity/scope matches | "ISO-certified product", "ISO-certified faucet" | ISO 9001 certifies QMS scope, not SKU performance or compliance |

## Product-Family Claim Map

| Product family | Public evidence currently supporting product-level claims | Safer claim cluster | Open mapping need |
|---|---|---|---|
| Bathroom / lavatory sink faucets | cUPC file `10664`; NSF 61 file `N-10665`; NSF 372 file `10666`; WaterSense file `16508` for the 12 listed 1.2 gpm patterns only | plumbing listing, health-effects, lead-free, and WaterSense only when model pattern matches | map each internal SKU to `L...` public model pattern and category-specific WaterSense row |
| Kitchen / pull-out kitchen faucets | cUPC file `10664`; NSF 61 file `N-10665`; NSF 372 file `10666` | plumbing listing, health-effects, lead-free | verify DOE / CEC filings; map SKU to public pattern |
| Pot fillers | cUPC file `10664`; NSF 61 file `N-10665`; NSF 372 file `10666` for drinking-water-contact listed patterns | plumbing listing, health-effects, lead-free | distinguish kitchen pot filler / pot filler patterns; verify DOE / CEC applicability |
| Beverage / drinking-water faucets | cUPC file `10664`; NSF 61 file `N-10665`; NSF 372 file `10666` | plumbing listing, health-effects, lead-free | map SKU to `Z...` public pattern; avoid filtration / contaminant-removal wording |
| Fixed showerheads / handheld showers | cUPC file `10664`; WaterSense file `16509` for `J215F18-**` and `P300F18-**` only | plumbing listing; WaterSense efficiency if exact pattern matches | verify DOE / CEC filings; avoid NSF 61 / 372 unless product also appears in those files |
| Shower faucet sets | cUPC file `10664`; WaterSense file `16509` for `XB6202F18-**`, `XB6223F18-**`, `XB6230F18-**`, `XB6305F18-**` only | plumbing listing; WaterSense efficiency if exact pattern matches | verify DOE / CEC filings; avoid broad WaterSense claim for non-`F18` patterns |
| Shower valves / trim kits | cUPC file `10664` | plumbing listing | confirm whether DOE / CEC apply; avoid WaterSense unless listed as showerhead / shower outlet |
| Tub spouts / bathtub faucets | cUPC file `10664` | plumbing listing | no WaterSense / NSF 61 / 372 claim unless separately mapped |
| Company / QMS | ISO 9001 source-table record only | company-level QMS credibility after certificate details are collected | collect entity, site, scope, certificate number, verification link |

## WaterSense Exact Public Model Patterns

### Lavatory Faucets — IAPMO file `16508` / EPA faucet rows

All listed at `1.2 gpm`.

| Model pattern | Product label |
|---|---|
| `L3156ALFF12-**` | bathroom sink faucet |
| `L3156BLFF12-**` | bathroom sink faucet |
| `L3209LFF12-**` | bathroom sink faucet |
| `L3210LFF12-**` | bathroom sink faucet |
| `L4117LFF12-**` | bathroom sink faucet |
| `L4150LFF12-**` | bathroom sink faucet |
| `L4317ALFF12-**` | bathroom sink faucet |
| `L4317LFF12-**` | bathroom sink faucet |
| `L4327ALFF12-**` | bathroom sink faucet |
| `L4327BLFF12-**` | bathroom sink faucet |
| `L4350LFF12-**` | bathroom sink faucet |
| `L4355LFF12-**` | bathroom sink faucet |

### Showerheads — IAPMO file `16509` / EPA showerhead rows

All listed at `1.8 gpm`.

| Model pattern | Product label |
|---|---|
| `J215F18-**` | Fixed Showerhead |
| `P300F18-**` | Handheld Shower |
| `XB6202F18-**` | Shower Faucet Set |
| `XB6223F18-**` | Shower Faucet Set |
| `XB6230F18-**` | Shower Faucet Set |
| `XB6305F18-**` | Shower Faucet Set |

## Public Model-Pattern Inventory Findings

2026-05-30 model-pattern inventory across IAPMO cUPC, NSF 61, NSF 372, and EPA / IAPMO WaterSense records found an important matching issue: exact string matching is too strict for KES certification control because public certificate rows use wildcard pattern slots.

| Finding | Count / result | Meaning |
|---|---:|---|
| cUPC file `10664` public patterns | 124 | Broad plumbing fixture fitting pattern set. |
| NSF/ANSI/CAN 372 file `10666` public patterns | 80 | Lead-free pattern set; all 80 appear exactly in cUPC file `10664`. |
| NSF/ANSI/CAN 61 file `N-10665` public patterns | 80 | Same base model set as NSF 372 after normalizing the displayed `Q` marker. |
| WaterSense exact public patterns | 18 | 12 lavatory faucet rows and 6 showerhead / shower faucet set rows. |
| WaterSense exact-string overlap with cUPC | 0 of 18 | False-negative risk caused by flow-specific model strings such as `F12` / `F18` versus broader `***` certificate patterns. |
| WaterSense wildcard-normalized overlap with cUPC | 18 of 18 | Every public WaterSense row has a likely broader cUPC pattern match after treating `***` and `**` as pattern slots. |
| WaterSense lavatory faucet overlap with NSF 372 / NSF 61 after normalization | 12 of 12 | The WaterSense faucet rows align with broader lead-free and health-effects faucet patterns after wildcard and `Q` normalization. |
| WaterSense showerhead overlap with NSF 372 / NSF 61 | 0 of 6 | Expected boundary in the observed public data: these rows are WaterSense + cUPC, not NSF 61 / 372 rows. |

## WaterSense To Broader IAPMO Pattern Map

These rows are model-pattern normalization observations, not final SKU approvals. They should be used to guide SKU mapping and owner review.

| WaterSense model pattern | Product label | Broader cUPC pattern | Broader NSF 372 pattern | Broader NSF 61 pattern after `Q` normalization |
|---|---|---|---|---|
| `L3156ALFF12-**` | bathroom sink faucet | `L3156ALF***-**` | `L3156ALF***-**` | `QL3156ALF***-**` |
| `L3156BLFF12-**` | bathroom sink faucet | `L3156BLF***-**` | `L3156BLF***-**` | `QL3156BLF***-**` |
| `L3209LFF12-**` | bathroom sink faucet | `L3209LF***-**` | `L3209LF***-**` | `QL3209LF***-**` |
| `L3210LFF12-**` | bathroom sink faucet | `L3210LF***-**` | `L3210LF***-**` | `QL3210LF***-**` |
| `L4117LFF12-**` | bathroom sink faucet | `L4117LF***-**` | `L4117LF***-**` | `QL4117LF***-**` |
| `L4150LFF12-**` | bathroom sink faucet | `L4150LF***-**` | `L4150LF***-**` | `QL4150LF***-**` |
| `L4317ALFF12-**` | bathroom sink faucet | `L4317ALF***-**` | `L4317ALF***-**` | `QL4317ALF***-**` |
| `L4317LFF12-**` | bathroom sink faucet | `L4317LF***-**` | `L4317LF***-**` | `QL4317LF***-**` |
| `L4327ALFF12-**` | bathroom sink faucet | `L4327ALF***-**` | `L4327ALF***-**` | `QL4327ALF***-**` |
| `L4327BLFF12-**` | bathroom sink faucet | `L4327BLF***-**` | `L4327BLF***-**` | `QL4327BLF***-**` |
| `L4350LFF12-**` | bathroom sink faucet | `L4350LF***-**` | `L4350LF***-**` | `QL4350LF***-**` |
| `L4355LFF12-**` | bathroom sink faucet | `L4355LF***-**` | `L4355LF***-**` | `QL4355LF***-**` |
| `J215F18-**` | Fixed Showerhead | `J215***-**` | not observed | not observed |
| `P300F18-**` | Handheld Shower | `P300***-**` | not observed | not observed |
| `XB6202F18-**` | Shower Faucet Set | `XB6202***-**` | not observed | not observed |
| `XB6223F18-**` | Shower Faucet Set | `XB6223***-**` | not observed | not observed |
| `XB6230F18-**` | Shower Faucet Set | `XB6230***-**` | not observed | not observed |
| `XB6305F18-**` | Shower Faucet Set | `XB6305***-**` | not observed | not observed |

## Matching Rules For SKU Mapping

| Rule | Use |
|---|---|
| Exact model-pattern match beats family inference | If SKU model string directly matches public pattern after resolving finish / flow suffixes, claim can inherit that listing subject to category limits |
| Wildcard-normalized match is required before declaring a gap | Do not conclude that a WaterSense row lacks cUPC / NSF backing just because the exact string differs from a broader `***` certificate pattern |
| Finish suffix `**` must be resolved | Do not treat unrelated finish / marketplace codes as evidence; map finish tokens to the listing suffix table |
| Flow suffix matters | WaterSense is especially flow-specific: `F12` faucet patterns and `F18` shower patterns are not interchangeable with higher-flow variants |
| `Q` marker must be preserved in evidence but normalized for base-model comparison | NSF 61 rows may display a `Q` marker; strip it only for cross-file comparison and keep the original model string in audit evidence |
| Category must match | A shower valve in cUPC file `10664` does not inherit WaterSense showerhead status unless it appears in file `16509` or EPA rows |
| Company-level evidence cannot become SKU evidence | ISO 9001 and source-table totals cannot support product-specific certification wording |
| Internal source-table status needs public proof for external claims | DOE / CEC / CE / UKCA / ISO should remain internal compliance status until filing exports or certificate verification are attached |

## Minimum SKU-Level Table To Build Next

独立工作表已建在 [KES SKU Certification Mapping Table](./kes-sku-certification-mapping-table.md)。本节保留最低字段定义，便于理解表结构。

| Field | Required? | Notes |
|---|---|---|
| SKU | yes | internal SKU / marketplace SKU |
| Model number printed on product / package | yes | needed for matching to public pattern |
| Product family | yes | faucet, showerhead, shower valve, tub spout, etc. |
| Finish / color | yes | resolves `**` where applicable |
| Flow rate suffix | yes where applicable | especially `F12`, `F18`, `F22` |
| Public model pattern | yes | copied from IAPMO / EPA / DOE / CEC |
| Certification family | yes | one row per claim family |
| File / listing / filing id | yes | e.g. `10664`, `10666`, `N-10665`, `16508`, `16509`, CCMS basic model |
| Evidence URL / screenshot path | yes | public URL or internal archived screenshot |
| Allowed wording | yes | short marketing-safe phrase |
| Blocked wording | recommended | prevents accidental overclaiming |
| Owner / review date | yes | renewal and page-audit owner |

## Sources
- [KES Certifications and Compliance Register](./kes-certifications-and-compliance-register.md)
- [KES SKU Certification Mapping Table](./kes-sku-certification-mapping-table.md)
- [KES Certification Evidence Pack Checklist](./kes-certification-evidence-pack-checklist.md)
- [Source Summary — KES Public Certification Model-Pattern Inventory (2026-05-30)](../source-summaries/kes-public-certification-model-pattern-inventory-2026-05-30.md)
- [Source Summary — KES Official Online Certification Verification (2026-05-30)](../source-summaries/kes-official-online-certification-verification-2026-05-30.md)
- [Source Summary — KES Certification / Compliance Source-Table Readout (2026-05-30)](../source-summaries/kes-certification-source-table-readout-2026-05-30.md)
- [Source Summary — KES Certification Public Reference Scan (2026-05-30)](../source-summaries/kes-certification-public-reference-scan-2026-05-30.md)
- IAPMO R&T Product Listing Directory: <https://pld.iapmo.org/>
- IAPMO WaterSense file 16508: <https://mirobase.iapmo.org/pld/listing_watersense.aspx?file=16508>
- IAPMO WaterSense file 16509: <https://mirobase.iapmo.org/pld/listing_watersense.aspx?file=16509>
- EPA WaterSense Product Search: <https://lookforwatersense.epa.gov/>
