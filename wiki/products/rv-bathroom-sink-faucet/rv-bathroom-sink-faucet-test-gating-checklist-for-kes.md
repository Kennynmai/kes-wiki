---
type: product
status: draft
owner: strategy
created: 2026-05-31
updated: 2026-05-31
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [rv-bathroom-sink-faucet, kes, test-gating, checklist]
source_count: 5
review_cycle: monthly
verification_status: working
related:
  - ./rv-bathroom-sink-faucet.md
  - ./rv-bathroom-sink-faucet-kes-go-no-go-memo-v1.md
  - ./rv-bathroom-sink-faucet-compatibility-engineering-breakpoints.md
  - ./rv-bathroom-sink-faucet-compliance-framework-and-evidence-boundaries.md
  - ./rv-bathroom-sink-faucet-sample-shortlist-and-pricing.md
  - ./rv-bathroom-sink-faucet-assumption-register.md
  - ./rv-bathroom-sink-faucet-claim-register.md
---

# RV Bathroom Sink Faucet 测试闸门清单

## 为什么有这页
This page turns the research into a practical gate.

If a route cannot pass these checks, KES should not treat it as a serious product candidate.

## Gate 1 — shutoff / drip proof
### Must have
- hot and cold shutoff test
- drip test immediately after installation
- drip test after lifecycle cycling
- cartridge seat inspection

### Fail if
- any side cannot shut off completely
- drip begins after limited cycling
- valve performance depends on over-tightening handles

## Gate 2 — pressure and leak proof
### Must have
- static pressure test
- pressure cycling test
- burst-pressure margin
- body/base internal leak inspection
- supply connection leak inspection

### Fail if
- leak appears inside body or base
- leak is hidden under vanity
- pressure variation causes instability

## Gate 3 — thread / shank proof
### Must have
- shank effective length defined
- deck thickness range defined
- thread specification defined
- torque-to-strip or torque-to-failure test
- lock nut installation test

### Fail if
- supply line cannot lock securely across target vanity thickness
- normal installer torque strips thread
- product needs an unplanned extension kit

## Gate 4 — RV fit realism
### Must have
- 4-inch centerset fit bench
- multiple RV vanity thicknesses
- tight cabinet underside simulation
- common PEX / supply-line scenarios
- unsupported conditions list

### Fail if
- direct replacement works only on ideal demo sinks
- install requires hidden workaround
- support burden depends on photo-by-photo manual diagnosis

## Gate 5 — spout reach and basin proof
### Must have
- spout height and reach dimensions
- water landing test across small RV basins
- splash check at target flow
- swivel range test if swivel is included

### Fail if
- high arc looks good but water lands too close to basin edge
- swivel movement causes leakage
- splash risk is high in shallow RV sinks

## Gate 6 — metal-first proof
### Must have
- metal parts map
- material stack list
- corrosion / water-spot exposure test
- interface leak test between metal and non-metal parts
- weight and installation burden check

### Fail if
- metal is mostly cosmetic
- user-facing claim implies full metal but product is hybrid
- metal-first makes install worse

## Gate 7 — finish durability
### Must have
- water spot and wipe-down test
- cleaner exposure test
- corrosion / oxidation screening
- scratch / abrasion sanity check

### Fail if
- matte black or brushed nickel quickly spots, flakes, or stains
- finish cannot survive ordinary bathroom cleaning

## Gate 8 — claim / evidence route clarity
### Must have
- evidence card for every certification claim
- clear distinction between internal test and certification
- SKU-level lead-free / NSF / cUPC / WaterSense / CEC mapping if used

### Fail if
- page copy is written before evidence mapping
- certification language borrows from other KES SKUs
- `universal fit`, `never leaks`, or `lifetime drip-free` appears without proof

## Gate 9 — economics
### Must have
- landed cost model
- FBA fee model
- target retail price
- warranty / replacement allowance
- expected margin by route

### Fail if
- metal-first requires price above plausible willingness-to-pay
- margin only works by removing the very parts that create differentiation

## Current default KES rule
Do not move this product from concept diligence to product development unless it passes:
1. shutoff / drip proof
2. pressure and leak proof
3. thread / shank proof
4. RV fit realism
5. spout reach and basin proof
6. metal-first proof
7. finish durability
8. claim / evidence route clarity
9. economics
