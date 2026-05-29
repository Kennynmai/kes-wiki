---
type: source-summary
status: draft
owner: product
created: 2026-05-18
updated: 2026-05-18
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, atmospheric-vacuum-breaker, backflow-prevention, plumbing-safety]
source_type: screenshot-set + web-scan
extraction_mode: progressive
source_title: 大气式真空破坏器 AVB 部件调查
source_date: 2026-05-18
source_author: KES internal + public web sources
raw_path: ../../raw/products/bathtub-filter/2026-05-18-atmospheric-vacuum-breaker-avb-component-scan.md
review_cycle: monthly
verification_status: spot-checked
related:
  - ../products/bathtub-filter/bathtub-filter-atmospheric-vacuum-breaker-avb.md
  - ../products/bathtub-filter/bathtub-filter-compatibility-engineering-breakpoints.md
---

# 来源摘要｜大气式真空破坏器 AVB 部件调查（2026-05-18）

## Obsidian links
- [[bathtub-filter-atmospheric-vacuum-breaker-avb]]
- [[bathtub-filter-compatibility-engineering-breakpoints]]
- [[bathtub-filter-kes-product-architecture-hypotheses]]

## Source
- 用户提供的 AVB 中文示意图两张
- 原始调查记录：`raw/products/bathtub-filter/2026-05-18-atmospheric-vacuum-breaker-avb-component-scan.md`
- 公开 manufacturer / standard-adjacent source spot check

## 提取出的关键信息
### 1. 部件身份
图中部件应归类为 **大气式真空破坏器（Atmospheric Vacuum Breaker, AVB）**。它属于 backflow prevention / backsiphonage protection 部件，主要通过在负压时引入空气来打断虹吸。

### 2. 工作逻辑
正常正压供水时，内部阀芯 / 浮子关闭空气入口，水流按预期通过。管道或上游出现负压时，空气入口打开，外部空气进入，破坏真空，避免下游污染水被倒吸回供水侧。

### 3. 关键边界
AVB 通常用于非连续压力场景，且不应被当成可任意内联承压的止回阀。公开资料普遍强调：AVB 不能承受持续压力，安装位置、下游阀门、出口高度和污染源关系都影响其适用性。

### 4. 对 bathtub filter 的含义
AVB 不提升过滤性能，但它提醒 bathtub-spout / faucet 外接产品要额外审视：
- 是否存在软管、浸没出口或残水腔
- 是否可能被用户接到下游可关闭阀 / 喷头 / 管路
- 是否可能在负压时发生非预期回吸
- 是否需要独立的 backflow-prevention 设计或合规评估

## 这份来源支持什么
- 将用户图中的部件正确归类为 AVB / backflow-prevention component
- 把 AVB 作为 bathtub filter 架构评估中的 plumbing-safety checkpoint
- 提醒 KES 不要把防倒吸部件误写成过滤或净水卖点

## 这份来源不支持什么
- 不支持得出“所有 bathtub filter 都必须内置 AVB”
- 不支持把 AVB 视为对所有倒流风险充分的保护
- 不支持替代目标市场的 plumbing code / certification review

## 建议回写
- 建立 AVB 工程部件词条
- 在兼容性 / 安装风险页面加入 backflow / backsiphonage 检查点
- 后续若进入样机阶段，应把 AVB / vacuum-breaker 相关问题纳入合规 review checklist

## Sources
- `raw/products/bathtub-filter/2026-05-18-atmospheric-vacuum-breaker-avb-component-scan.md`
- [ASSE Product Standards](https://asse-plumbing.org/standards/product-standards/)
- [Watts 288A Atmospheric Vacuum Breaker](https://www.watts.com/products/plumbing-flow-control-solutions/backflow-preventers/vacuum-breakers/288a)
- [Watts 288A specification / installation sheet](https://www.watts.com/dfsmedia/0533dbba17714b1ab581ab07a4cbb521/23525-source/es-wq-288a-pdf)
- [Zurn Wilkins 35XL Atmospheric Vacuum Breaker](https://www.zurn.com/products/water-control/backflow-preventers/35xl)
