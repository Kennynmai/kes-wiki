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
domains: [rv-bathroom-sink-faucet, compliance, standards, certification, framework]
source_count: 7
review_cycle: monthly
verification_status: working
related:
  - ./rv-bathroom-sink-faucet.md
  - ../../company/kes-certifications-and-compliance-register.md
  - ../../company/kes-certification-claim-control-matrix.md
  - ../../company/kes-sku-certification-mapping-table.md
---

# RV Bathroom Sink Faucet 合规框架与证据边界

## 为什么有这页
这页不是列证书，而是建立一个审核框架。

RV bathroom faucet 虽然在 Amazon 可能落在 Automotive / RV parts 语境，但本质上仍是接入供水系统、用于 bathroom sink / lavatory 的 plumbing fixture fitting。页面、包装和客服不能随意使用认证语言。

## 一套最重要的拆解顺序
### 第 1 层：证据对象是什么？
- finished product / SKU
- model family / wildcard pattern
- material or component
- supplier claim
- internal test

### 第 2 层：证据性质是什么？
- official certification / listing
- third-party test report
- legal compliance filing
- internal QA test
- marketing statement only

### 第 3 层：覆盖范围是什么？
- drinking-water health effects
- lead content
- plumbing performance / code listing
- flow rate / water efficiency
- finish durability
- leak / pressure performance

## 关键合规与声明边界
### ASME A112.18.1 / CSA B125.1
这是 plumbing supply fittings 的核心性能/设计类标准范围，覆盖 kitchen, sink, and lavatory supply fittings 等。

KES 使用时必须说明是：
- certified/listed to standard
- tested to standard
- designed with reference to standard

三者不能混写。

### cUPC / IAPMO
cUPC 是 plumbing code / listing trust signal。KES 已有公司层面的 public cUPC 证据页，但具体 RV faucet SKU 仍需要 model pattern mapping。

不能把公司已有 faucet family 证书自动外推给新品。

### NSF/ANSI/CAN 61
NSF consumer guidance states kitchen and bathroom faucets sold in the US should meet lead leaching requirements under NSF/ANSI/CAN 61. For KES, this means any drinking-water-contact faucet claim needs SKU-level support.

### NSF/ANSI/CAN 372 / Lead-free
`lead-free` 是高风险但必要的 claim。必须区分：
- material lead content
- NSF 372 certification
- NSF 61 health-effects certification
- Prop 65 warning context

### DOE flow
Federal faucet water-conservation standards list lavatory faucets at 2.2 gpm measured at 60 psi. Competitor pages often advertise 2.0-2.2 gpm.

### WaterSense
EPA WaterSense bathroom faucet guidance centers around water-efficient lavatory faucets, historically max 1.5 gpm; EPA's draft Version 2.0 proposed 1.2 gpm but was paused in February 2025 for review.

If KES wants WaterSense language, it must use exact WaterSense-labeled model evidence. KES existing WaterSense lavatory faucet public rows cannot be borrowed for an unmapped RV SKU.

### California / CEC / state flow limits
State-level flow requirements may be stricter than federal. Do not write broad `CEC compliant` unless SKU and flow evidence support it.

## Allowed / Conditional / Banned Language
### Allowed if true by design or test
- `4-inch centerset`
- `2-hole installation`
- `ceramic cartridges`
- `metal threaded connections`
- `tested for leaks before packing`
- `spout reach: X inches`

### Conditional, needs SKU evidence
- `lead-free`
- `NSF/ANSI/CAN 61`
- `NSF/ANSI/CAN 372`
- `cUPC`
- `ASME A112.18.1 / CSA B125.1`
- `WaterSense`
- `CEC compliant`
- `ADA compliant`

### Avoid unless legally and technically supported
- `universal fit`
- `never leaks`
- `lifetime drip-free`
- `certified safe`
- `meets all US standards`
- `drinking-water safe` without specific standard basis

## Evidence Card Template
For every authority signal, create a card:

| Field | Required answer |
|---|---|
| claim | Exact phrase to use |
| object | SKU / model family / component |
| issuer | IAPMO / NSF / EPA / DOE / lab / supplier |
| standard | Exact standard or rule |
| proof | certificate, listing, test report, filing, or none |
| scope | What it supports |
| non-scope | What it does not support |
| page wording | Final allowed wording |

## KES Practical Recommendation
Do compliance mapping during prototype sourcing, not after listing copy is written.

For V1, the cleanest path is:
1. Decide material stack.
2. Map to existing KES faucet model patterns if possible.
3. If not possible, create new SKU certification path.
4. Only then write lead-free / cUPC / NSF / WaterSense / CEC copy.

