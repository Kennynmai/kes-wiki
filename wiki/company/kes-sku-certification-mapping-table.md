---
type: working-table
status: draft
owner: operations
created: 2026-05-30
updated: 2026-05-30
visibility: team
confidence: medium
officiality: draft
domain: operations
domains: [kes, certification, compliance, sku-governance, claims, product-listings]
source_count: 5
review_cycle: monthly
verification_status: unverified
related:
  - ./kes-certifications-and-compliance-register.md
  - ./kes-certification-claim-control-matrix.md
  - ./kes-certification-evidence-pack-checklist.md
  - ../source-summaries/kes-public-certification-model-pattern-inventory-2026-05-30.md
  - ../source-summaries/kes-official-online-certification-verification-2026-05-30.md
  - ../source-summaries/kes-doe-cec-public-database-access-2026-05-30.md
aliases:
  - KES SKU certification mapping
  - KES SKU claim-control table
  - KES SKU 认证映射表
name_zh: KES SKU 级认证映射表
name_en: KES SKU Certification Mapping Table
---

# KES SKU 级认证映射表

## Purpose
这页是 KES 后续填充 SKU-level certification / compliance 的工作表骨架。

它的目标不是重复证书登记册，而是把每个可对外使用的认证 claim 落到可审计链条：

`SKU -> printed model -> normalized public pattern / filing model -> certificate or filing id -> evidence file -> allowed wording`

在 SKU 行没有填完整前，不应把公司级、品类级、源表总数直接写成单个 SKU 的对外认证 claim。

## Status Legend

| Status | Meaning |
|---|---|
| `ready-to-claim` | SKU、printed model、public pattern / filing id、证据 URL 或截图、allowed wording 都已填，并完成 owner review。 |
| `mapped-pending-evidence` | SKU 与 public pattern / filing id 已能匹配，但截图、导出或证书包还没归档。 |
| `source-table-only` | 只有内部源表状态，没有 SKU-level public proof。 |
| `needs-model-normalization` | SKU / printed model 与 public pattern 需要解析 `**`、`***`、`F12`、`F18`、`Q` 等标记。 |
| `blocked` | 证据冲突、型号不匹配、证书过期、或 claim scope 不支持该 SKU。 |

## Master SKU Certification Mapping Table

先按一行一个 `SKU + certification family` 建表。一个 SKU 同时有 cUPC、NSF61、NSF372、WaterSense、DOE、CEC 时，应拆成多行，而不是把多个 claim 挤在一格里。

| SKU | Marketplace / channel SKU | Product family | Printed model number | Finish / color token | Flow suffix / rated flow | Certification family | Public pattern / basic model / filing model | Certificate / file / filing id | Issuer / authority | Entity shown | Evidence URL / archived path | Evidence status | Claim status | Allowed wording | Blocked wording | Owner | Review date | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TBD | TBD | bathroom sink faucet | TBD | TBD | TBD | cUPC | TBD | `10664` | IAPMO R&T | `KES HOME (U.S.) LIMITED` | TBD | pending | needs-model-normalization | Listed by IAPMO R&T to ASME A112.18.1 / CSA B125.1 under file 10664 | NSF / WaterSense / lead-free wording unless separately mapped | operations | TBD | Use wildcard rules before claim. |
| TBD | TBD | bathroom sink faucet | TBD | TBD | `F12` / `1.2 gpm` | WaterSense lavatory faucet | TBD | `16508` | IAPMO / EPA WaterSense | IAPMO entity `KES HOME (U.S.) LIMITED`; EPA brand `KES` | TBD | pending | needs-model-normalization | WaterSense labeled bathroom sink faucet, 1.2 gpm, file 16508 | drinking-water safety, NSF, CEC, or cUPC wording unless separately mapped | operations | TBD | Must match one of the 12 WaterSense faucet rows. |
| TBD | TBD | showerhead / shower faucet set | TBD | TBD | `F18` / `1.8 gpm` | WaterSense showerhead | TBD | `16509` | IAPMO / EPA WaterSense | IAPMO entity `KES HOME (U.S.) LIMITED`; EPA brand `KES` | TBD | pending | needs-model-normalization | WaterSense labeled showerhead / shower faucet set, 1.8 gpm, file 16509 | NSF 61 / 372, filter, or drinking-water wording | operations | TBD | Must match one of the 6 WaterSense shower rows. |
| TBD | TBD | kitchen / bathroom faucet | TBD | TBD | TBD | NSF/ANSI/CAN 61 | TBD | `N-10665` | IAPMO R&T | `KES HOME (U.S.) LIMITED` | TBD | pending | needs-model-normalization | Certified to NSF/ANSI/CAN 61 for drinking-water system component health effects under IAPMO file N-10665 | contaminant-removal, filtration, lead-reduction wording | operations | TBD | Preserve `Q` marker in evidence if present. |
| TBD | TBD | kitchen / bathroom faucet | TBD | TBD | TBD | NSF/ANSI/CAN 372 | TBD | `10666` | IAPMO R&T | `KES HOME (U.S.) LIMITED` | TBD | pending | needs-model-normalization | Lead-free certified / certified to NSF/ANSI/CAN 372 under IAPMO file 10666 | lead-removal / reduces lead in water wording | operations | TBD | Current public 372 set is 80 models. |
| TBD | TBD | faucet / showerhead | TBD | TBD | rated max flow TBD | DOE compliance | TBD | CCMS TBD | U.S. DOE | TBD | TBD | missing public export | source-table-only | DOE compliance certification filed for this basic model | DOE approved / DOE certified quality | operations | TBD | Requires CCMS export or screenshot. |
| TBD | TBD | plumbing fitting | TBD | TBD | rated max flow TBD | CEC compliance | TBD | MAEDbS TBD | California Energy Commission | TBD | TBD | missing public export | source-table-only | Listed / certified in CEC MAEDbS for California Title 20 | CEC certified nationally / California quality approved | operations | TBD | Search `Plumbing Products -> Plumbing Fittings / Plumbing Fixtures`. |
| TBD | TBD | tapware / shower outlet | TBD | TBD | TBD | CE conformity | TBD | certificate TBD | Global Testing Services | TBD | TBD | missing certificate package | source-table-only | Conformity certificate / DoC available for the listed model and applicable standards | EU approved / CE certified quality | operations | TBD | Requires certificate, test report, and DoC / legal basis. |
| TBD | TBD | tapware / shower outlet | TBD | TBD | TBD | UKCA conformity | TBD | certificate TBD | Global Testing Services | TBD | TBD | missing certificate package | source-table-only | UKCA conformity documentation available for the listed model and applicable standards | UK approved / UKCA certified quality | operations | TBD | Requires UK DoC and designated standards basis. |
| TBD | TBD | company / site | not SKU-specific | not applicable | not applicable | ISO 9001:2015 QMS | company scope TBD | certificate TBD | XQC | TBD | TBD | missing certificate package | source-table-only | Managed under an ISO 9001:2015 certified quality management system, if entity and scope match | ISO-certified product / ISO-certified faucet | operations | TBD | Do not use as SKU product certification. |

## Model Normalization Fields

These fields should be generated or manually checked before any row becomes `ready-to-claim`.

| Field | Example | Rule |
|---|---|---|
| `printed_model_raw` | `L3156ALFF12-BK` | Capture exactly from product, package, manual, listing, or source SKU table. |
| `model_family_base` | `L3156ALF` | Remove finish / flow suffix only after documenting the rule. |
| `flow_marker` | `F12`, `F18`, `F22` | Must stay attached to WaterSense / DOE / CEC claims. |
| `finish_marker` | `BK`, `CH`, `BN`, etc. | Must map to the public suffix slot represented by `**`. |
| `public_pattern_raw` | `L3156ALF***-**` | Preserve exactly as shown in IAPMO / EPA / DOE / CEC. |
| `public_pattern_normalized` | `L3156ALF[flow]-[finish]` | Use only for matching; do not replace original evidence string. |
| `marker_notes` | `Q marker displayed in NSF 61 row` | Preserve issuer-specific markers in the audit trail. |

## Certification-Specific Required Evidence

| Certification family | SKU-level required fields | Minimum evidence before external claim |
|---|---|---|
| cUPC | SKU, printed model, product family, finish, public model pattern, file `10664` | Current IAPMO PLD row or certificate-preview export / screenshot showing `Active`, entity, standard, model pattern. |
| NSF/ANSI/CAN 61 | SKU, printed model, drinking-water-contact product family, public model pattern, file `N-10665`, `Q` marker note if shown | Current IAPMO PLD row or certificate-preview export / screenshot showing `Active`, entity, standard, model pattern. |
| NSF/ANSI/CAN 372 | SKU, printed model, drinking-water-contact product family, public model pattern, file `10666` | Current IAPMO PLD row or certificate-preview export / screenshot showing `Active`, entity, standard, model pattern. |
| WaterSense lavatory faucet | SKU, printed model, `F12`, max flow `1.2 gpm`, public WaterSense model row, file `16508` | IAPMO WaterSense page or EPA WaterSense row showing model, brand/entity, max flow, and current status. |
| WaterSense showerhead | SKU, printed model, `F18`, max flow `1.8 gpm`, public WaterSense model row, file `16509` | IAPMO WaterSense page or EPA WaterSense row showing model, brand/entity, max flow, and current status. |
| DOE | SKU, basic model, product type, max flow, test pressure, submitter, filing status | DOE CCMS export / screenshot or internal submission confirmation tied to basic model. |
| CEC | SKU, model, product type, manufacturer / brand, flow rate, status | CEC MAEDbS export / screenshot showing Approved or Archived status. |
| CE / UKCA | SKU, model, standard edition, certificate number, test report, DoC / UK DoC basis | Certificate package plus declaration file and applicable legal basis. |
| ISO 9001 | Legal entity, site, scope, certificate number, issue / expiry | Certificate PDF and verification route; not SKU-specific. |

## Import Checklist For Internal SKU Export

Before loading internal SKU data into this table, normalize these columns:

| Column | Required? | Notes |
|---|---|---|
| internal SKU | yes | Stable internal ID. |
| marketplace SKU / ASIN / listing ID | recommended | Needed for page-audit and marketplace compliance. |
| product family | yes | Must align with claim map. |
| printed model number | yes | Do not use marketing title as substitute. |
| finish / color | yes | Resolves `**`. |
| flow rate | required for faucets / showerheads | Needed for WaterSense, DOE, CEC, and FTC plumbing-product representations. |
| source-table certification flags | yes | cUPC / NSF61 / NSF372 / WaterSense / DOE / CEC / CE / UKCA / ISO. |
| source-table status | yes | Distinguish valid, pending, expired, archived, withdrawn, not applicable. |
| last sync timestamp | yes | Prevent stale local DB state from overriding newer DingTalk source table. |
| public evidence pointer | yes when available | URL, screenshot path, export path, or certificate package path. |

## Review Workflow

1. Load SKU export into the master table with all certification flags as `source-table-only`.
2. Normalize printed model numbers into base model, flow marker, finish marker, and public-pattern candidate.
3. Match against IAPMO / EPA public patterns first, because these are currently strongest public evidence.
4. Attach DOE / CEC exports only when retrieved; until then, keep DOE / CEC rows as `source-table-only`.
5. Attach CE / UKCA / ISO certificate package details only after original files are collected.
6. Owner reviews each row's allowed wording and blocked wording.
7. Mark a row `ready-to-claim` only after evidence path and review date are filled.

## Sources
- [KES Certifications and Compliance Register](./kes-certifications-and-compliance-register.md)
- [KES Certification Claim-Control Matrix](./kes-certification-claim-control-matrix.md)
- [KES Certification Evidence Pack Checklist](./kes-certification-evidence-pack-checklist.md)
- [Source Summary — KES Public Certification Model-Pattern Inventory (2026-05-30)](../source-summaries/kes-public-certification-model-pattern-inventory-2026-05-30.md)
- [Source Summary — KES Official Online Certification Verification (2026-05-30)](../source-summaries/kes-official-online-certification-verification-2026-05-30.md)
- [Source Summary — KES DOE / CEC Public Database Access (2026-05-30)](../source-summaries/kes-doe-cec-public-database-access-2026-05-30.md)
