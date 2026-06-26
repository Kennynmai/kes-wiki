# Bathtub Filter 评论语料 wiki 更新说明（2026-04-20）

## 建议写入位置
- raw：`raw/products/bathtub-filter/2026-04-20-competitor-review-corpus/`
- source summary：`wiki/source-summaries/bathtub-filter-competitor-review-corpus-2026-04-20.md`

## 应更新页面
1. `wiki/products/bathtub-filter/bathtub-filter-research-coverage-gaps.md`
   - 将 “Amazon review 100+ 直采评论待补 / Rainforest reviews 返回为空” 更新为：已补入 11 ASIN / 2661 条 2026-04-20 截止评论语料；仍缺真实 SKU 退货率和人工复核后的投诉频次。
2. `wiki/products/bathtub-filter/bathtub-filter-complaint-taxonomy-and-risk-by-route.md`
   - 用 `topic-counts` 和 `topic-examples` 校准 R3/spout-mount 路线的安装、漏水、流量、效果质疑等投诉优先级。
3. `wiki/products/bathtub-filter/bathtub-filter-kes-go-no-go-memo-v1.md`
   - 把评论数据状态从 “待补” 调整为 “已有语料，待人工复核和真实退货率”。

## 不建议直接写入
- 不建议把全量评论正文写进 wiki 产品页；正文保留在 raw 的 normalized CSV。
- 不建议把关键词初筛当成最终 NLP/人工编码结论。
