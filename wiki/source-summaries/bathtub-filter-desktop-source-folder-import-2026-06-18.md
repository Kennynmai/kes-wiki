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
domains: [bathtub-filter, kes-internal, raw-snapshot, structure, tests, supplier-reports]
source_type: internal-doc
extraction_mode: folder-snapshot
source_date: 2026-06-18
raw_path: ../../raw/products/bathtub-filter/2026-06-18-desktop-source-folder-import/
verification_status: imported_unverified
related:
  - ../products/bathtub-filter/bathtub-filter.md
  - ../products/bathtub-filter/bathtub-filter-research-coverage-gaps.md
  - ../products/bathtub-filter/bathtub-filter-2026-06-18-source-import-index.md
  - ../products/bathtub-filter/site/bathtub-filter-kes-structure-overview.md
---

# Source Summary - 桌面「浴缸过滤」源文件夹快照（2026-06-18）

> 补记（2026-09-06）：本批次有导入索引但无 source summary。

## 来源
42 个文件（manifest 见 raw 目录），来自桌面工作文件夹：产品结构图与爆炸图、结构视频、余氯试纸测试视频与图片、排水速度 / 导流模块 / 活性炭测试记录、宗立滤料报告、NSF / 食品级 / KDF / 亚硫酸钙球资料、竞品评论与 listing 导出。视频文件按 repo 规则不入库（.gitignore）。

## 分类
internal-doc + vendor-material 混合快照，**未逐件提取**。

## 已被引用的文件
- `爆炸图.png` → [[bathtub-filter-kes-structure-overview]]
- 《浴缸过滤器_城市市政自来水版202602讲解》→ [[bathtub-filter-kes-v1-definition-and-not-for-list]]、[[bathtub-filter-kes-pack-contents-spec]] 的一手来源
- `90g无内分隔的效果20260420.JPG` 等导流模块对照图 → [[bathtub-filter-kes-structure-flow-diversion-module]]

## 边界
- 快照 ≠ 结论；测试类文件缺样品版本、流速、水温、读数方法字段，引用前需补。
- Filterbaby `B0FNVDJRSQ` 资料已剔除且未保留在任何 repo（见 hub「已知缺口」）。

## 后续
- 排水速度、活性炭、试纸测试三类内部记录尚未逐件建 summary；若 Gate 1 或维护口径需要引用，再按件提取。
