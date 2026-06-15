---
type: source-summary
status: active
created: 2026-05-16
updated: 2026-05-16
domain: operations
domains: [operations, egypt, company-finance, partnership, startup-capital]
source_type: pdf-spreadsheet-bundle
extraction_mode: full-table-conversion-and-reconciliation
source_title: 埃及项目第一批启动资金 / Zhang支出与工资抵扣
source_date: 2026-05-15
source_author: Zhang Taotao
confidence: medium
verification_status: unverified
related:
  - ../projects/egypt-partnership-capital-and-expense-ledger.md
  - ./aj-company-daily-expense-record-2025-2026.md
---

# Egypt Startup Capital and Zhang Reconciliation - 2026-05-15

## Why this source bundle matters

This bundle connects three separate finance questions:

- First-batch Egypt startup capital now estimated at RMB 879,500.
- Zhang Taotao's actual personal cash outlay is summarized at RMB 47,294.81 through 2026-04-30.
- Zhang's wage-offset contribution is summarized at RMB 32,678.57 through 2026-04-30, separate from cash outlay.

It also provides a check against the existing AJ company daily expense detail sheet.

## Key numbers

| item | amount_RMB | treatment |
|---|---:|---|
| First-batch startup capital estimate | 879,500.00 | expected future funding need |
| Zhang cumulative personal outlay | 47,294.81 | cash or cash-like outlay, subject to receipt/settlement review |
| Zhang wage-offset contribution | 32,678.57 | non-cash contribution credit, subject to contract treatment |
| Zhang unpaid salary + meal allowance | 26,142.86 | liability/payable to Zhang if salary policy is accepted |

## Startup capital estimate

The updated first-batch capital estimate totals RMB 879,500. The largest components are:

| category | updated_amount_RMB |
|---|---:|
| 原材料、辅料 | 350,000 |
| 生产设备 | 200,000 |
| 买车 | 150,000 |
| 租厂房 | 60,000 |
| 办公设备 | 40,000 |

Under the current 80/20 stage-2 contribution reference, RMB 879,500 implies:

| party | implied_share | amount_RMB |
|---|---:|---:|
| Mai / Kenny side | 80% | 703,600 |
| Zhang Taotao | 20% | 175,900 |

This is only a ratio calculation. The cooperation agreement's cash installment and wage-offset rules still need to govern final settlement.

## Reconciliation against existing AJ detail sheet

Existing AJ detail sheet totals Zhang source-converted expenses at RMB 41,769. The new Zhang personal expense summary reaches RMB 47,294.81 because it nets a RMB 2,000 hotel-deposit return and adds two items not present in the detailed daily expense ledger: RMB 6,698.63 deposited into the company account and RMB 832 paid on behalf of the tax company.

| reconciliation step | amount_RMB |
|---|---:|
| Existing AJ Zhang detail total | 41,769.00 |
| Less hotel-deposit return recognized in summary | -2,000.00 |
| Add 2026-04-20 company-account deposit | 6,698.63 |
| Add 2026-04-28 tax-company payment | 832.00 |
| Reconstructed total from AJ detail basis | 47,299.63 |
| Zhang summary PDF total | 47,294.81 |
| Residual difference | 4.82 |

The RMB 4.82 residual appears consistent with month-level rounding/detail differences, but it is not closed until the underlying spreadsheet or receipts are reviewed.

Month-level check:

| month | AJ detail amount_RMB | Zhang summary amount_RMB | difference_RMB | note |
|---|---:|---:|---:|---|
| 2026-02 | 17,514.00 | 17,513.27 | 0.73 | likely rounding/detail conversion |
| 2026-03 gross expense | 14,920.00 | 14,916.01 | 3.99 | summary also records RMB 2,000 income |
| 2026-04 daily expense | 9,335.00 | 9,334.90 | 0.10 | likely rounding/detail conversion |

## Contribution-credit view

If Zhang's summarized personal outlay and wage-offset amount are both accepted as contribution credit, the provisional credit would be:

| component | amount_RMB |
|---|---:|
| Personal outlay summary | 47,294.81 |
| Wage-offset contribution | 32,678.57 |
| Provisional total contribution credit | 79,973.38 |

Against the implied 20% share of the RMB 879,500 first-batch startup capital, Zhang's provisional remaining contribution would be RMB 95,926.62. If only actual cash outlay is counted before wage-offset eligibility, the remaining cash gap would be RMB 128,605.19.

This distinction matters because the cooperation framework says Zhang must participate in the first two installments in cash, while wage-offset use belongs to later agreed arrangements.

## Caveats / verification needs

- PDF summaries are one-page rollups. They validate totals directionally but do not replace receipt-level review.
- The new personal expense summary uses exact decimals; the existing AJ detail sheet uses rounded RMB amounts in many rows.
- The RMB 6,698.63 company-account deposit and RMB 832 tax-company payment should be added to the detailed ledger or linked as separate settlement items.
- The wage-offset contribution is not cash. Keep it separate from reimbursement, operating expense, and capital contribution until a settlement rule is approved.

## Sources

- ../../raw/egypt/company-finance/2026-05-15-egypt-first-batch-startup-capital-summary.md
- ../../raw/egypt/company-finance/2026-05-15-egypt-first-batch-startup-capital-summary.pdf
- ../../raw/egypt/company-finance/2026-05-15-zhang-personal-expense-summary.md
- ../../raw/egypt/company-finance/2026-05-15-zhang-personal-expense-summary.pdf
- ../../raw/egypt/company-finance/2026-05-15-zhang-wage-offset-contribution-detail.md
- ../../raw/egypt/company-finance/2026-05-15-zhang-wage-offset-contribution-detail.pdf
- ../../raw/egypt/company-finance/2026-05-15-aj-company-daily-expense-record.md
