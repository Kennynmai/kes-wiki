---
source_type: public-record
captured: 2026-05-30
source_title: KES public certification model-pattern inventory notes
source_author: agent
classification: public-record
extraction_mode: model-pattern-inventory
verification_status: spot-checked
---

# KES Public Certification Model-Pattern Inventory Notes — 2026-05-30

## Scope
This capture records a model-pattern inventory built from public / issuer-hosted KES certification records already collected in the 2026-05-30 official online verification pass.

Sources used:

- IAPMO myPLC certificate-preview data for cUPC file `10664`
- IAPMO myPLC certificate-preview data for NSF/ANSI/CAN 372 file `10666`
- IAPMO myPLC certificate-preview data for NSF/ANSI/CAN 61 file `N-10665`
- EPA WaterSense API rows for KES faucets and showerheads

This is a public model-pattern inventory, not an internal SKU-level certification map.

## Inventory counts

| Public evidence set | Count observed | Notes |
|---|---:|---|
| IAPMO cUPC file `10664` | 124 | Plumbing Fixture Fittings public model patterns |
| IAPMO NSF/ANSI/CAN 372 file `10666` | 80 | Lead-free public model patterns |
| IAPMO NSF/ANSI/CAN 61 file `N-10665` | 80 | Health-effects public model patterns; many model numbers carry a `Q` lower-lead marker in HTML subscript form |
| WaterSense KES faucet rows | 12 | EPA / IAPMO WaterSense lavatory faucet patterns, all `1.2 gpm` |
| WaterSense KES showerhead rows | 6 | EPA / IAPMO WaterSense showerhead / shower faucet set patterns, all `1.8 gpm` |

## Cross-listing observations

| Observation | Result | Meaning |
|---|---:|---|
| NSF/ANSI/CAN 372 exact model patterns also appear in cUPC file `10664` | 80 of 80 | The public NSF 372 lead-free set is an exact subset of the current cUPC public pattern set. |
| NSF/ANSI/CAN 61 and NSF/ANSI/CAN 372 same base model set after `Q` marker normalization | yes | The public NSF 61 and 372 base model coverage aligns, but the NSF 61 display uses a `Q` marker on many rows. |
| WaterSense exact model strings that also appear exactly in cUPC file `10664` | 0 of 18 | This is a false-negative risk caused by wildcard / flow-suffix differences, not proof of no cUPC coverage. |
| WaterSense model strings covered by broader cUPC wildcard patterns | 18 of 18 | Each public WaterSense row has a likely broader cUPC pattern match after wildcard normalization. |
| WaterSense faucet rows covered by NSF/ANSI/CAN 372 wildcard patterns | 12 of 12 | The WaterSense lavatory faucet rows align with broader NSF 372 faucet patterns. |
| WaterSense faucet rows covered by NSF/ANSI/CAN 61 wildcard patterns after `Q` normalization | 12 of 12 | The WaterSense lavatory faucet rows align with broader NSF 61 faucet patterns after removing the `Q` marker for base-model comparison. |
| WaterSense showerhead rows covered by NSF/ANSI/CAN 61 / 372 | 0 of 6 | Expected boundary: these showerhead / shower faucet set rows are WaterSense + cUPC, not drinking-water NSF 61 / 372 rows in the public data observed. |

## Wildcard and marker normalization rules

The public records should not be matched with simple exact-string logic.

| Public notation | Working interpretation for mapping | Claim-control caution |
|---|---|---|
| `**` | Finish / suffix slot | Map the actual finish or variant token before making SKU claims. |
| `***` | Flow-rate or variant slot depending on product family | Do not infer that every possible variant is certified; compare against the listed certificate pattern and product category. |
| `F12` | WaterSense faucet flow marker for `1.2 gpm` rows | WaterSense faucet claims should remain tied to the specific `F12` patterns. |
| `F18` | WaterSense showerhead flow marker for `1.8 gpm` rows | WaterSense showerhead claims should remain tied to the specific `F18` patterns. |
| `<sub>Q</sub>` / `Q` | NSF 61 lower-lead marker shown in certificate-preview model strings | For cross-file base-model comparison, strip the marker; for claims, preserve the marker and its certificate meaning. |

## WaterSense to broader IAPMO pattern matches

These are model-pattern normalization observations, not final SKU approvals.

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

## Claim-control implications

- Exact matching alone will incorrectly mark all WaterSense rows as outside cUPC, because WaterSense records use explicit `F12` / `F18` flow-specific patterns while cUPC uses broader `***` wildcard patterns.
- WaterSense should remain an efficiency / performance claim. Even when a WaterSense faucet model aligns with cUPC, NSF 61, and NSF 372 base patterns, the wording must keep each certification's claim scope separate.
- WaterSense showerhead rows align with cUPC wildcard patterns, but not with NSF 61 / 372 public patterns in this pass.
- The current inventory can support a model-pattern-level claim-control table, but not final SKU-level permission. SKU permission still requires internal SKU, printed model number, finish, flow suffix, and certificate / filing row mapping.

## Remaining gaps

- Build a deterministic model-pattern matcher for internal SKU exports.
- Confirm IAPMO's official interpretation of `***`, `**`, and `Q` marker semantics before using wildcard inheritance in external-facing claims.
- Attach current IAPMO PLD screenshots / exports for each file.
- Split the internal WaterSense SKU count into lavatory faucet vs showerhead rows.
