---
type: checklist
status: draft
owner: operations
created: 2026-05-30
updated: 2026-05-30
visibility: team
confidence: medium
officiality: draft
domain: operations
domains: [kes, certification, compliance, evidence-pack, audit, claims]
source_count: 5
review_cycle: monthly
verification_status: unverified
related:
  - ./kes-certifications-and-compliance-register.md
  - ./kes-certification-claim-control-matrix.md
  - ./kes-sku-certification-mapping-table.md
  - ../source-summaries/kes-official-online-certification-verification-2026-05-30.md
  - ../source-summaries/kes-doe-cec-public-database-access-2026-05-30.md
aliases:
  - KES certification evidence pack
  - KES certificate archive checklist
  - KES 认证证据包清单
name_zh: KES 认证 Evidence Pack Checklist
name_en: KES Certification Evidence Pack Checklist
---

# KES 认证 Evidence Pack Checklist

## Purpose
这页定义 KES certification / compliance 资料包应该归档什么。

它解决两个问题：

- 对外 claim 前，运营能快速找到当前官方证据。
- 证书续期、客户审核、平台合规、页面抽检时，不需要重新追溯证据来源。

## Evidence Pack Naming

建议每个证据包按这个结构归档：

`certifications/{cert_family}/{file_or_certificate_id}/{YYYY-MM-DD}/`

示例：

- `certifications/iapmo-cupc/10664/2026-05-30/`
- `certifications/iapmo-nsf-372/10666/2026-05-30/`
- `certifications/iapmo-nsf-61/N-10665/2026-05-30/`
- `certifications/watersense/16508/2026-05-30/`
- `certifications/watersense/16509/2026-05-30/`
- `certifications/doe-ccms/faucets/2026-05-30/`
- `certifications/cec-maedbs/plumbing-fittings/2026-05-30/`
- `certifications/ce-gts/{certificate-number}/2026-05-30/`
- `certifications/ukca-gts/{certificate-number}/2026-05-30/`
- `certifications/iso-9001-xqc/{certificate-number}/2026-05-30/`

## Master Evidence Checklist

| Certification family | Required evidence files | Status | Notes |
|---|---|---|---|
| cUPC file `10664` | PLD screenshot; certificate-preview JSON/export; current certificate PDF if available; model list export; standard / expiry metadata; mark-usage rules | partially captured | Public online evidence found; archive package still needs screenshots / final file paths. |
| NSF/ANSI/CAN 372 file `10666` | PLD screenshot; certificate-preview JSON/export; current certificate PDF if available; 80-model list; standard / expiry metadata; lead-free wording guidance | partially captured | Public online evidence found; current PDF package still pending. |
| NSF/ANSI/CAN 61 file `N-10665` | PLD screenshot; certificate-preview JSON/export; current certificate PDF if available; 80-model list; `Q` marker explanation; health-effects wording guidance | partially captured | Public online evidence found; preserve `Q` marker details. |
| WaterSense lavatory faucet file `16508` | IAPMO listing screenshot; EPA rows export; model table; max-flow evidence; label-usage guidance | partially captured | 12 public model patterns found. |
| WaterSense showerhead file `16509` | IAPMO listing screenshot; EPA rows export; model table; max-flow evidence; label-usage guidance | partially captured | 6 public model patterns found. |
| DOE CCMS | CCMS export / screenshot; basic model mapping; submitter; certified rating; test pressure; submission confirmation; withdrawn / discontinued check | missing public rows | Official endpoint returned HTTP 403 in command-line access. |
| CEC MAEDbS | MAEDbS export / screenshot; approved / archived status; manufacturer / brand; model number; flow rate; product type; California Title 20 mapping | missing public rows | Advanced Search path identified; KES rows not captured. |
| CE GTS | Certificate PDF; certificate number; test report; model list; standard edition; EU DoC / DoP; applicable legislation; responsible person / importer details | missing package | Source table says valid, but public verification not found. |
| UKCA GTS | Certificate PDF; certificate number; test report; model list; BS EN edition; UK DoC; applicable UK legislation; GB / NI treatment | missing package | Source table says valid, but public verification not found. |
| ISO 9001 XQC | Certificate PDF; certificate number; legal entity; site address; scope; issue / expiry; accreditation body; public verification URL | missing package | Company-level only; no SKU claim. |

## Per-File Evidence Metadata

Every archived evidence file should have a short metadata row:

| Field | Required? | Notes |
|---|---|---|
| evidence_id | yes | Stable ID such as `iapmo-cupc-10664-pld-screenshot-2026-05-30`. |
| certification_family | yes | cUPC, NSF61, NSF372, WaterSense, DOE, CEC, CE, UKCA, ISO. |
| file_or_certificate_id | yes | `10664`, `N-10665`, `16508`, CCMS basic model, certificate number, etc. |
| source_url | yes when public | Official URL or issuer portal URL. |
| captured_at | yes | Date/time of screenshot/export. |
| captured_by | yes | Person or agent. |
| legal_entity_shown | yes | Prevent entity mismatch. |
| brand_shown | yes when relevant | EPA lists brand `KES`; IAPMO lists legal entity. |
| model_scope | yes | Model list, basic model, product family, or company scope. |
| status_shown | yes | Active, Approved, Archived, expired, withdrawn, etc. |
| issue_revised_expiry | yes when available | Needed for renewal tracking. |
| archive_path | yes | Local or shared-drive path. |
| used_by_pages | recommended | Product pages, Amazon listings, packaging, dealer docs. |
| owner_review | yes before external claim | Reviewer and date. |

## Evidence Strength Tiers

| Tier | Evidence type | Use |
|---|---|---|
| Tier 1 | Current official public database row or issuer directory listing | Strongest external claim anchor. |
| Tier 2 | Current certificate PDF from issuer or official certificate portal | Strong evidence, but still check directory for current status when available. |
| Tier 3 | Internal regulatory submission confirmation or source-table export | Good internal status evidence; external claims need stronger proof where possible. |
| Tier 4 | Historical PDF, marketplace-hosted PDF, sales deck, screenshot without date | Useful context only; not enough for current claim without current verification. |
| Tier 5 | Verbal confirmation, uncited spreadsheet total, marketing copy | Not acceptable as claim evidence. |

## Current Evidence Pack Gaps

| Gap | Why it matters | Next action |
|---|---|---|
| IAPMO screenshots / exports not archived into repo/shared evidence path | Public online evidence was found, but audit package needs stable files. | Capture PLD / myPLC / WaterSense screenshots and store with file IDs. |
| DOE CCMS KES rows not captured | DOE source-table status cannot support external per-SKU wording alone. | Obtain CCMS export, screenshot, or submission confirmation by basic model. |
| CEC MAEDbS KES rows not captured | California compliance claim requires model-level MAEDbS evidence. | Browser-search `KES`, `KES HOME`, and known models under `Plumbing Fittings` / `Plumbing Fixtures`. |
| WaterSense 31 internal SKU count not split | Current public rows are 12 faucet patterns + 6 shower patterns; internal count is combined. | Split SKU count by product family and map each row to file `16508` or `16509`. |
| CE / UKCA certificate packages missing | Cannot know whether evidence is full conformity basis or only test/certificate scope. | Collect GTS certificate numbers, reports, model lists, DoC / UK DoC, legislation basis. |
| ISO 9001 XQC certificate package missing | Company-level QMS claim needs entity, site, scope, expiry, and accreditation chain. | Collect certificate PDF and verification URL. |

## Claim Release Gate

A certification claim is not ready for page, packaging, A+, customer support, or dealer use unless all are true:

| Gate | Required result |
|---|---|
| Evidence exists | Public row, certificate package, or regulatory filing is archived. |
| Entity matches | Legal entity / brand in evidence supports the intended claim. |
| Model matches | SKU printed model maps to public pattern / filing model. |
| Scope matches | Product family and certification claim scope are aligned. |
| Date valid | Current status and expiry / revised dates are checked. |
| Wording approved | Claim uses allowed wording from claim-control matrix. |
| Owner review complete | Domain owner or compliance owner has reviewed the row. |

## Sources
- [KES Certifications and Compliance Register](./kes-certifications-and-compliance-register.md)
- [KES Certification Claim-Control Matrix](./kes-certification-claim-control-matrix.md)
- [KES SKU Certification Mapping Table](./kes-sku-certification-mapping-table.md)
- [Source Summary — KES Official Online Certification Verification (2026-05-30)](../source-summaries/kes-official-online-certification-verification-2026-05-30.md)
- [Source Summary — KES Public Certification Model-Pattern Inventory (2026-05-30)](../source-summaries/kes-public-certification-model-pattern-inventory-2026-05-30.md)
- [Source Summary — KES DOE / CEC Public Database Access (2026-05-30)](../source-summaries/kes-doe-cec-public-database-access-2026-05-30.md)
