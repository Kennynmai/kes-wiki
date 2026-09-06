---
type: source-summary
status: draft
owner: strategy
created: 2026-09-06
updated: 2026-09-06
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, strategy-docs, import]
source_type: internal-doc
extraction_mode: copy-and-wrap
source_date: 2026-06-17
raw_path: ../../raw/products/bathtub-filter/2026-06-17-desktop-strategy-doc-import/
verification_status: imported_unverified
related:
  - ../products/bathtub-filter/bathtub-filter.md
  - ../products/bathtub-filter/bathtub-filter-research-coverage-gaps.md
  - ../products/bathtub-filter/bathtub-filter-2026-06-17-desktop-strategy-doc-import-index.md
---

# Source Summary - 桌面策略文档导入（2026-06-17）

> 补记（2026-09-06）：本批次当时直接写入 wiki 页并生成导入索引，未建 source summary。本页补 provenance 层，不改内容。

## 来源
- 桌面 10 份 bathtub filter 策略 / 介质 / 水源 / 宣称文档，manifest 见 raw 目录 `import-manifest.csv`（Source / Target / Status / Mode / hash 三列）。
- 旧版 wiki 页备份在 `previous-wiki-versions/`。

## 分类
internal-doc（KES 策略与研究文档），高 officiality 影响：其中两份是对既有 wiki 页的 upgrade（chloramine-media-research、claim-register），其余为新页。

## 写入位置
| 源文件 | wiki 页 | 模式 |
|---|---|---|
| V1 执行路线图 | [[bathtub-filter-kes-v1-execution-roadmap-2026-06-15]] | new |
| media E-E-A-T 叙事 | [[bathtub-filter-kes-media-eeat-and-clean-formula-narrative]] | new |
| clean-formula 情感定位 | [[bathtub-filter-kes-clean-formula-emotional-positioning]] | new |
| ACF 供应商研究 | [[bathtub-filter-acf-supplier-research]] | wrap（加 frontmatter） |
| 氯胺介质研究 | [[bathtub-filter-chloramine-media-research]] | upgrade_existing |
| 水诊断 kit / 获客引擎 | [[bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine]] | new |
| 北美特殊水源 | [[bathtub-filter-north-america-special-water-sources]] | wrap |
| 获客引擎 MVP spec | [[bathtub-filter-kes-acquisition-engine-mvp-spec]] | new |
| claim register | [[bathtub-filter-claim-register]] | upgrade_existing |
| 北美 / 加 / 亚 / 欧水质报告 | [[bathtub-filter-north-america-canada-asia-europe-water-report-2024-final]] | wrap |

## 边界
- 这批文档是策略产出，不是证据；其中引用的去氯数字、寿命数字仍以 T2 / T3 与 Gate 1 为准。
- 2026-09-05 lint 删除了无 frontmatter 的重复副本 `acf-supplier-research.md`，保留带前缀版本。

## 后续
- 导入索引：[[bathtub-filter-2026-06-17-desktop-strategy-doc-import-index]]
