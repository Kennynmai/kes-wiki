---
type: product
status: draft
owner: product
created: 2026-05-18
updated: 2026-05-18
visibility: team
confidence: medium
officiality: draft
aliases: [AVB, 大气式真空破坏器, 真空破坏器, 防倒吸阀, atmospheric vacuum breaker]
name_zh: 大气式真空破坏器
name_en: Atmospheric Vacuum Breaker
domain: product
domains: [bathtub-filter, atmospheric-vacuum-breaker, backflow-prevention, plumbing-safety, product-architecture]
source_count: 5
review_cycle: monthly
verification_status: spot-checked
related:
  - ./bathtub-filter.md
  - ./bathtub-filter-compatibility-engineering-breakpoints.md
  - ./bathtub-filter-installation-risk-matrix-v2.md
  - ./bathtub-filter-kes-product-architecture-hypotheses.md
  - ../../source-summaries/atmospheric-vacuum-breaker-avb-component-scan-2026-05-18.md
---

# 大气式真空破坏器（AVB）

## Obsidian links
- [[bathtub-filter]]
- [[bathtub-filter-compatibility-engineering-breakpoints]]
- [[bathtub-filter-installation-risk-matrix-v2]]
- [[bathtub-filter-kes-product-architecture-hypotheses]]

## 页面定位
这页记录用户提供图片中的部件：**大气式真空破坏器（Atmospheric Vacuum Breaker, AVB）**。

它是 plumbing safety / backflow prevention 部件，不是滤芯，也不是提升水质的过滤介质。对 bathtub filter 的价值在于提醒 KES：一切连接在 faucet / tub spout / hose / 容器旁边的产品，都需要检查是否存在倒吸、负压回流、污染水回吸的风险。

## 一句话定义
AVB 是一种在管路发生负压时自动打开空气入口、让空气进入管道并破坏真空的防倒吸部件，主要用于防止下游液体通过虹吸被吸回供水侧。

## 工作逻辑
### 平时有水压
- 供水侧处于正压
- 阀芯 / 浮子关闭空气入口
- 水流按设计方向通过

### 出现负压 / 倒虹吸风险
- 上游压力下降，管路内形成真空或相对负压
- 空气入口打开
- 外部空气进入管道，破坏虹吸条件
- 下游污染水更难被吸回供水侧

用户图中“负压状态，管道内产生真空，阀门打开，吸入空气，使管道压力与大气压力平衡”的说明，符合 AVB 的基本机理。

## 适用边界
### AVB 主要解决什么
- backsiphonage（倒虹吸 / 负压倒吸）
- 非加压、非连续压力场景下的回吸风险
- 下游出口可能接触污染源时的基础隔断需求

### AVB 不等于什么
- 不等于过滤器
- 不等于消毒或净水能力
- 不等于所有 backflow 风险的完整解决方案
- 不等于可以长期承压的 inline check valve
- 不等于可以随意放在下游有关闭阀的结构中

## 设计限制与合规提醒
公开 manufacturer / standard-adjacent 资料对 AVB 的共同提醒是：AVB 的安装方式很关键，尤其是高度、下游阀门、连续压力和污染源位置。

对 KES 来说，现阶段应把这些作为设计 review 问题，而不是直接写成官方合规结论：
- 产品是否会被安装在下游有 shutoff / spray valve / hose valve 的位置？
- 出水口是否可能浸没在浴缸、桶、盆、清洁液或残水中？
- 产品内部是否会保留残水，并在负压时有回吸路径？
- 用户是否可能把产品接到软管、喷头或其他非预期附件上？
- 如果需要防倒流，目标市场要求 AVB、hose-bibb vacuum breaker、dual check、RPZ，还是其他装置？

## 对 bathtub filter 的直接启发
### 1. 它是安全部件，不是卖点滤材
AVB 不能被包装为“过滤能力”。如果在产品中使用，应表述为 plumbing-safety / anti-siphon / backflow-prevention 相关结构，并由合规证据支持。

### 2. faucet 外接产品要关注倒吸路径
Bathtub filter 若只是从 tub spout 接水并向开放浴缸出水，风险判断与带软管、可关闭喷头、浸没出口或储水腔的产品不同。设计不能只看“正常注水”，还要看异常负压条件。

### 3. “防倒吸”不能替代兼容性工程
AVB 只处理负压倒吸的一个维度，不能解决：
- 适配失败
- 漏水 / 溢水
- 高流速下绕流
- 滤材接触时间不足
- 用户误装导致的机械脱落

### 4. 如果 Version A 继续走 tub-spout route，应加一个 safety checkpoint
建议在样机 / 合规 review 中增加：
- backflow / backsiphonage hazard review
- downstream shutoff risk review
- submerged outlet scenario review
- local plumbing code / ASSE 1001 applicability review

## Fact vs inference
### 事实
- 用户图示部件与 AVB 的典型结构和工作逻辑一致：正压关闭空气入口，负压打开空气入口，破坏真空。
- AVB 属于 backflow-prevention / backsiphonage protection 相关部件。
- 公开资料普遍将 AVB 与 ASSE 1001 等产品标准、非连续压力、安装高度、下游阀门限制等问题关联。

### 推论
- bathtub filter 若存在软管、浸没出口、下游关闭阀或残水腔，AVB / backflow-prevention review 的重要性会上升。
- 对 KES 的当前设计阶段而言，AVB 最适合作为架构风险检查点，而不是马上作为必须内置的 BOM 决策。

## Open questions
- KES 目标销售市场是否要求特定 anti-siphon / backflow prevention 装置？
- 目标产品架构是否有任何下游关闭点？
- 用户是否可能把出水端浸入浴缸水面以下？
- 使用 AVB 是否会引入漏水、噪音、排气孔溅水或外观集成问题？
- 若产品面向美国市场，是否需要 ASSE 1001、CSA B64.1.1 或其他认证 / listing？

## Sources
- [来源摘要｜大气式真空破坏器 AVB 部件调查（2026-05-18）](../../source-summaries/atmospheric-vacuum-breaker-avb-component-scan-2026-05-18.md)
- `../../../raw/products/bathtub-filter/2026-05-18-atmospheric-vacuum-breaker-avb-component-scan.md`
- [ASSE Product Standards](https://asse-plumbing.org/standards/product-standards/)
- [Watts 288A Atmospheric Vacuum Breaker](https://www.watts.com/products/plumbing-flow-control-solutions/backflow-preventers/vacuum-breakers/288a)
- [Watts 288A specification / installation sheet](https://www.watts.com/dfsmedia/0533dbba17714b1ab581ab07a4cbb521/23525-source/es-wq-288a-pdf)
- [Zurn Wilkins 35XL Atmospheric Vacuum Breaker](https://www.zurn.com/products/water-control/backflow-preventers/35xl)
