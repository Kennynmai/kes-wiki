---
type: playbook
status: draft
owner: strategy
created: 2026-04-12
updated: 2026-04-14
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

# Bathtub Filter 验证 / 测试协议

## Obsidian links
- [[bathtub-filter]]
- [[bathtub-filter-normal-flow-vs-reduced-flow-evidence-table]]
- [[bathtub-filter-installation-risk-matrix-v2]]
- [[bathtub-filter-kes-go-no-go-memo-v1]]
- [[bathtub-filter-kes-route-elimination-memo-v1]]
- [[bathtub-filter-test-gating-checklist-for-kes]]

## Goal
定义：如果 KES 要把 bathtub filter 当作一个真实产品机会认真评估，至少需要做哪些测试。

## Core principle
这个品类必须按 **真实 bath use** 来测试，而不是用理想化的 slow trickle 场景来测试。

## Required test modules
### 1. Normal-flow chlorine reduction
问题：
- 在真实 tub-fill flow 下，自由氯能降低多少？
- 当流量高于某些阈值时，性能是否会明显塌陷？

建议 setup：
- 至少两种 faucet-flow 条件：`normal / realistic` 与 `slow / max-contact-time`
- 多轮重复测量
- 记录起始 chlorine ppm 与结束 chlorine ppm
- 明确记录 fill time 影响

最低有用输出：
- 各流量下的 % chlorine reduction
- 标准 bathtub 容积估算下的 fill time

### 2. Installation / compatibility test
问题：
- 产品实际能适配哪些 tub-spout 类型？
- 现实世界中有多少比例的 spouts 属于 out-of-scope？

建议 setup：
- 对 diverter 与 non-diverter spouts 做矩阵测试
- 在相关情况下覆盖 threaded、slip-fit 与变体几何
- 测量安装时间、稳定性、漏水情况，以及是否需要 workaround

最低有用输出：
- 支持的 spout types
- 不支持的 spout types
- install failure modes

### 3. Leak / stability durability test
问题：
- 在重复使用下，设备是否会滑脱、晃动或漏水？
- 多次装卸后，性能是否会退化？

建议 setup：
- 重复 mount / unmount cycles
- 重复 bath-fill runs
- 记录 seam、seal 与悬挂稳定性

### 4. Maintenance / refill economics
问题：
- 按真实家庭 bath usage 来看，合理的 replacement cadence 是什么？
- 用户是否会觉得维护负担可接受？

建议 setup：
- 把 gallons / baths claims 换算为具体 usage scenarios
- 对比 1-child、2-child 与 family mixed-use 场景
- 估算年度 replacement cost

### 5. Claims validation
问题：
- 哪些 claims 可以被测试直接支持？
- 哪些 claims 仍只能停留在 educational / contextual 层面？

建议规则：
- product proof claims 必须来自产品测试
- category-explanation claims 不能被转换成 finished-product efficacy promises

## Suggested pass / fail thresholds
### 更强的 pass indicators
- 在真实 normal flow 下仍有有意义的 chlorine reduction
- 重复使用中没有 leak / stability 问题
- fit scope 定义清晰
- 年度 refill cost 在商业上仍可接受

### Fail indicators
- 只有在不现实的慢流速下才表现强
- 反复出现 slip / leak / fit 问题
- 没有清晰、合规的 claims 路径
- refill economics 相对用户价值过于痛苦

## Why this matters
这个品类对以下两者之间的落差异常敏感：
- 文案听起来多好
- 产品在真实浴室里到底能不能工作
