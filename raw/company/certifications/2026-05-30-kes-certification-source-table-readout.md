---
source_type: internal-doc
captured: 2026-05-30
source_title: KES certification / compliance source-table readout
source_author: user-provided DingTalk Notable and local database readout
classification: internal-doc
extraction_mode: direct-readout
verification_status: unverified
---

# KES Certification / Compliance Source-Table Readout — 2026-05-30

## Context
The user reported that DingTalk Notable source tables and the local library had already been checked.

The user stated that the table below reflects direct source-table reads on 2026-05-30. It supersedes the local `dim_sku_certification` table for DOE status where the local table was last synced on 2026-05-25 and still showed 24 DOE SKUs as pending.

## Direct readout

| Certification | Type | Institution / standard | Current status | SKU coverage |
|---|---|---|---|---:|
| cUPC Certificate | 产品证书 | IAPMO / ASME A112.18.1, CSA B125.1 | 有效 | 335 |
| NSF/ANSI/CAN 61 Certificate – Health Effects | 产品证书 | IAPMO / NSF/ANSI/CAN 61 | 有效 | 202 |
| NSF/ANSI/CAN 372 Certificate – Lead Free | 产品证书 | IAPMO / NSF/ANSI/CAN 372 | 有效 | 202 |
| DOE Compliance Certification | 法定合规备案 | U.S. DOE / 10 CFR Part 429, 430 | 有效 | 493 |
| CEC Compliance | 法定合规备案 | California Energy Commission / California Title 20 | 有效 | 828 |
| CE Certificate of Conformity | 符合性认证 | Global Testing Services / EN 817, EN 1112 | 有效 | 705 |
| UKCA Certificate of Conformity | 符合性认证 | Global Testing Services / BS EN 817, BS EN 1112 | 有效 | 1,142 |
| EPA WaterSense Certification – Lavatory Faucets | 产品证书 | IAPMO / EPA WaterSense Specification | 有效 | 31* |
| EPA WaterSense Certification – Showerheads | 产品证书 | IAPMO / EPA WaterSense Specification | 有效 | 31* |
| ISO 9001:2015 Quality Management System Certification | 管理体系认证 | XQC / ISO 9001:2015 | 有效 | 公司级，无 SKU 粒度 |

`*` SKU table field `watersense` does not distinguish lavatory faucets from showerheads, so the WaterSense number is the total WaterSense SKU count.

## Source-system note
- Local `dim_sku_certification` was last synced on 2026-05-25.
- Local table still showed 24 DOE SKUs as waiting for certificate.
- Direct DingTalk Notable source-table read on 2026-05-30 showed all DOE SKUs as certified.
- For wiki purposes, current status should follow the source table unless later sync evidence contradicts it.
