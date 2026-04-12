---
type: playbook
status: draft
owner: strategy
created: 2026-04-12
updated: 2026-04-12
visibility: company
confidence: medium
officiality: draft
domain: operations
domains: [bathtub-filter, validation, testing, protocol]
review_cycle: monthly
verification_status: working
related:
  - ../products/bathtub-filter-kes-go-no-go-memo-v1.md
  - ../products/bathtub-filter-kes-route-screening-memo-v2.md
---

# Bathtub Filter Validation / Testing Protocol

## Goal
Define what KES would need to test before taking bathtub filters seriously as a real product opportunity.

## Core principle
The category should be tested for **real bath use**, not idealized slow trickle scenarios.

## Required test modules
### 1. Normal-flow chlorine reduction
Questions:
- At realistic tub-fill flow, how much free chlorine reduction occurs?
- Does performance collapse above certain flow thresholds?

Suggested setup:
- at least two faucet-flow conditions: “normal/realistic” and “slow/max-contact-time”
- repeated measurements across multiple runs
- record starting chlorine ppm and ending chlorine ppm
- explicitly record fill time impact

Minimum useful output:
- % chlorine reduction at each flow
- fill time for standard bathtub volume estimate

### 2. Installation / compatibility test
Questions:
- Which tub-spout types can the product actually fit?
- What fraction of real-world spouts would be out of scope?

Suggested setup:
- test against a matrix of diverter vs non-diverter spouts
- threaded vs slip-fit vs variant geometries where relevant
- measure install time, stability, leak, and need for workaround

Minimum useful output:
- supported spout types
- unsupported spout types
- install failure modes

### 3. Leak / stability durability test
Questions:
- Does the device slip, wobble, or leak under repeated use?
- Does performance degrade after multiple attachment cycles?

Suggested setup:
- repeated mount / unmount cycles
- repeated bath-fill runs
- document seam, seal, and hang stability

### 4. Maintenance / refill economics
Questions:
- What is realistic replacement cadence under actual family bath usage?
- Does maintenance burden feel acceptable?

Suggested setup:
- convert gallons/baths claims into usage scenarios
- compare 1-child, 2-child, and family mixed-use scenarios
- estimate annual replacement cost

### 5. Claims validation
Questions:
- Which claims can be supported directly by testing?
- Which claims remain only educational/contextual?

Suggested rule:
- product proof claims must come from product testing
- category-explanation claims must not be converted into finished-product efficacy promises

## Suggested pass/fail thresholds
### Stronger pass indicators
- meaningful chlorine reduction at realistic normal flow
- no leak/stability issues in repeated use
- clearly defined fit scope
- annual refill cost remains commercially tolerable

### Fail indicators
- only strong performance at impractically slow flow
- repeated slip/leak/fit problems
- no clear route to disciplined claims
- refill economics too painful relative to user value

## Why this matters
This category is unusually sensitive to the gap between:
- what sounds good in copy
- what actually works in a bathroom
