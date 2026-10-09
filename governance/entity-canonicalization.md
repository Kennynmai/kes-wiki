# Entity Canonicalization Policy — KES Company Wiki

Important recurring business entities should have one canonical page.

## Canonical entity classes
- platform
- market
- product family
- category
- project
- organization / partner
- internal role / team

## Non-canonical support pages
Usually support canonical entities rather than replace them:
- source-summary
- decision
- playbook
- synthesis
- risk
- meeting-summary
- metric
- assumption

## Naming rules
Use stable, descriptive, kebab-case names.
Examples:
- `platforms/amazon-jp.md`
- `markets/japan.md`
- `projects/japan-market-entry.md`
- `products/curtains.md`

## Rule of thumb
If people will ask for the same object more than once, it likely deserves one canonical page.

---

## Registered entity pairs

Aliases and language variants that refer to **one** canonical entity. Use the first form in new pages; accept any form when reading older ones.

| canonical (zh) | canonical (en) | also seen on | status |
|---|---|---|---|
| 淄博宗立新材料科技有限公司 | Zibo Onlyzone Water Treatment Technology Co., Ltd. | 宗立 / Onlyzone / Zibo Onlyzone / ZONE 宗立科技 / 淄博宗立 | confirmed same entity 2026-10-09 (KES) |

**Note on the zh/en difference.** The Chinese legal name reads 淄博宗立**新材料**科技有限公司 while the English reads **Water Treatment** Technology. This was briefly logged on 2026-10-09 as a possible certificate-holder ambiguity and then closed: KES confirmed a single entity. It is a translation variance, not two companies — do not re-raise it as an open question.

**Note on report identifiers.** Supplier test reports carry a `ZONET`-prefixed sample number (`ZONET20230707001`, `ZONET20251113001`). These are per-report, not per-product, and several carry **no machine-readable analyst or approver name** — traceability varies by report and should be checked before citing.
