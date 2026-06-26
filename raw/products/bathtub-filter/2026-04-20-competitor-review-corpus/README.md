# Bathtub Filter 竞品评论原始语料归档（2026-04-20）

## 归档定位
- 目标 vault raw 位置：`raw/products/bathtub-filter/2026-04-20-competitor-review-corpus/`
- 本次暂存位置：`outputs/kes-wiki-staging/raw/products/bathtub-filter/2026-04-20-competitor-review-corpus/`
- 原始来源：`C:\Users\KEVIN\Desktop\浴缸过滤\浴缸过滤器_竞品评论原始资料`
- 评论截止日期：2026-04-20（按用户说明及文件批次命名）
- 整理日期：2026-06-02
- 2026-06-18 口径修正：Filterbaby `B0FNVDJRSQ` 是 shower filter / showerhead inline 产品，已从 bathtub-filter 评论语料中删除；对应原始 Excel、99 条 normalized 评论、99 条逐条标签记录和 ASIN 汇总行保留在 `raw/products/shower-filter/2026-04-20-filterbaby-review-corpus/` 和 `wiki/products/shower-filter/`。

## 文件说明
- `source-files/`：bathtub active ASIN 的原始 Excel 评论表，以及 `评论分析.md` 重命名后的人工典型评论笔记；Filterbaby `B0FNVDJRSQ` 原始 Excel 已从本目录删除并保留在 shower-filter raw。
- `bathtub-filter-competitor-review-corpus-2026-04-20.normalized.csv`：bathtub active 10 个 ASIN 的标准化评论总表，共 2562 条；不含 Filterbaby `B0FNVDJRSQ`。
- `bathtub-filter-competitor-review-asin-summary-2026-04-20.csv`：按 ASIN 汇总的评分、好中差评、VP/Vine、图片/视频、主题命中。
- `bathtub-filter-competitor-review-topic-counts-2026-04-20.csv`：关键词初筛的主题频次。
- `bathtub-filter-competitor-review-topic-examples-2026-04-20.md`：各主题的短摘录例证，用于回查原评论。
- `bathtub-filter-competitor-review-corpus-2026-04-20.metadata.json`：整理批次元数据。

## 重要口径
- Excel 表是完整评论语料；`评论分析.md` 只作为人工挑选的典型评论笔记，不应当代替全量数据。
- 主题统计是关键词初筛，不等于人工精标或真实退货率。
- 这批数据可以补上原 wiki 中 “Amazon review 100+ 直采/NLP 频次待补” 的一部分缺口，但不能补真实 SKU 退货率。
- 使用 bathtub-filter 当前结论、评分、安装和图片证据时，应以 active 10 ASIN 派生文件为准；Filterbaby 只在 shower-filter 项目中保留。

## ASIN 覆盖
- Excel ASIN：B008A4AG2U, B0742KFY9R, B0CXT5KL5Z, B0D3X39378, B0DTQ8H23D, B0FL24SLM5, B0FT7R9ZQ9, B0G5NZBW6W, B0GFQ1JRSK, B0GKT5CHYL
- `评论分析.md` 中出现的 ASIN：B0012045EO, B008A4AG2U, B0742KFY9R, B08Y8GSVJS, B0C5D7NLC7
- 仅在 `评论分析.md` 出现、未在本批 Excel 中出现：B0012045EO, B08Y8GSVJS, B0C5D7NLC7
- 在 Excel 中出现、未在 `评论分析.md` 出现：B0CXT5KL5Z, B0D3X39378, B0DTQ8H23D, B0FL24SLM5, B0FT7R9ZQ9, B0G5NZBW6W, B0GFQ1JRSK, B0GKT5CHYL

## 2026-06-02 逐条标签证据链维护
- `bathtub-filter-competitor-review-labeling-evidence-chain-2026-06-02.csv`：逐条评论标签证据链，含 Persona / Motivation / Positive / Negative 标签、QA 复核列、严重度与置信度。
- `bathtub-filter-competitor-review-labeling-method-note-2026-06-02.md`：标签规则、字段口径、用户确认的归因规则。
- `bathtub-filter-competitor-review-labeling-insight-report-2026-06-02.md`：标签分析报告，区分高杀伤投诉和高星轻微吐槽。
- 对应 source summary：`wiki/source-summaries/bathtub-filter-competitor-review-labeling-analysis-2026-06-02.md`
