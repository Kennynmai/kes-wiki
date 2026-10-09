---
type: decision
status: active
owner: 张艳娟
created: 2026-10-09
updated: 2026-10-09
visibility: company
confidence: medium
officiality: reviewed
domain: operations
domains: [operations, wayfair, promotion, north-america]
name_zh: Wayfair US/CA 促销前 24h 任务钉钉推送取消
name_en: Wayfair US/CA promo pre-check DingTalk push cancellation
aliases: [WF US, WF CA, Wayfair 促销任务, 新任务分配 促销开始前 24h, 钉钉推送取消, coupon Deal 抽查]
review_cycle: quarterly
verification_status: spot-checked
related:
  - ./north-america-growth-marketplace-opportunity-research.md
---

# Wayfair US / CA 取消促销前 24h 任务钉钉推送（保留 coupon / Deal 抽查）

## Decision

1. 取消 WF US、WF CA 的【新任务分配——促销开始前 24h】任务的**下发及通知**，具体指**取消该任务的钉钉推送**。
2. 取消的是**推送与自动通知**，不是运营动作本身：促销开始后**仍可继续人工抽查**优惠券（Coupon）、Deal 是否正确生效。

## Status

- 生效范围：Wayfair US、Wayfair CA 两个站点。
- 取消对象：钉钉推送 / 自动通知（含任务提醒触达）。
- 保留动作：人工抽查 coupon / Deal 生效（频率与责任人未指定）。
- 未覆盖：Amazon、Home Depot、Walmart 及 DTC / WooCommerce 的促销流程不变。

## Context

- Wayfair 已是 KES 稳定收入平台（V2 中 2026-01 至 2026-03 月销售约 5.7–6.6 万美元），促销是常规经营动作。
- 现有运营流程中存在一个「促销开始前 24h」的新任务分配与钉钉通知环节，以及促销开始后对优惠券 / Deal 生效状态的检查动作。
- 该要求来自张艳娟（2026-10-09），属于流程触达噪声的削减决定，不是平台能力或合规问题。
- 同日澄清：`WF` 确认为 Wayfair；取消范围限于钉钉推送，抽查保留。

## Evidence considered

- 需求原文与同日澄清（raw/company/2026-10-09-wayfair-us-ca-promo-task-cancellation-request.md）。
- Wayfair 平台定位与经营现状：wiki/markets/north-america-growth-marketplace-opportunity-research.md。
- 未获得：取消推送的收益量化（触达打扰量）与抽查频率 / 责任人。

## Alternatives considered

- 取消推送并同时取消生效检查——未采纳（需求方澄清后确认抽查保留）。
- 降频而非取消推送（如仅在重点促销期下发）——未采纳，但可作为回退选项。
- 用报表端异常信号替代人工抽查——未采纳，抽查保留。

## Risks

- 促销上线时间点不再有系统提醒，完全依赖运营自行排期；漏上线的暴露时间变长。
- 抽查为人工动作，若无频率与责任人约定，实际执行率不可观测，可能退化为零抽查。
- 该决定会与后续新建的 Wayfair 促销 SOP / 平台运营页面产生冲突，需要在建立 Wayfair 运营主页时同步引用本页。

## Implementation implications

- 任务 / 通知系统：停止向 WF US、WF CA 派发【新任务分配——促销开始前 24h】的钉钉推送；其他站点保持原逻辑。
- 检查动作：促销开始后 coupon / Deal 生效仍可人工抽查，不做系统级强制。
- 待补齐（尚未决定）：抽查频率、执行人、是否需要留痕。
- 若后续要恢复推送，应作为新的 decision 页面记录，不要直接覆盖本页。

## Review trigger

- 出现促销未生效或价格错误导致的实际订单 / 毛利损失。
- WF 促销频次或活动复杂度显著上升。
- Wayfair 运营 SOP 建立，需要重写促销章节。

## Sources

- raw/company/2026-10-09-wayfair-us-ca-promo-task-cancellation-request.md
- wiki/markets/north-america-growth-marketplace-opportunity-research.md