---
type: product
status: draft
owner: strategy
created: 2026-04-15
updated: 2026-04-15
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, compatibility, installation, engineering, leak-risk]
source_count: 2
review_cycle: monthly
verification_status: working
related:
  - ./bathtub-filter-installation-risk-matrix-v2.md
  - ./bathtub-filter-route-clusters-and-kes-opportunity-spaces.md
  - ./bathtub-filter-kes-rd-and-validation-roadmap.md
  - ./bathtub-filter-normal-flow-vs-reduced-flow-evidence-table.md
---
# Bathtub Filter 兼容性（compatibility）工程断点

## 为什么有这页
这页不再泛泛讨论“安装有风险”，而是回答一个更具体的问题：

> **bathtub filter 到底会在哪些 compatibility / leak / flow 条件下，从“可卖”变成“不可信”？**

## 1. tub spout 不是一个标准化环境
浴缸喷嘴 / tub spout 至少沿着下面几个维度发生变化：
- slip-fit vs threaded
- diverter vs non-diverter
- straight vs curved outlet geometry
- 长喷嘴 vs 短喷嘴
- 是否有稳定 underside / lip 可供挂载或导流
- 离墙距离 / tile clearance
- 装饰型宽体造型 vs 简单圆柱型
- 现有喷嘴本体是否稳定，是否已有轻微松动

这意味着 bathtub filter 实际上是在继承一个 **fragmented plumbing environment（碎片化的浴室五金环境）**。

## 2. KES 需要的最低 tub-spout taxonomy
至少要区分：
1. straight non-diverter spout with stable underside/lip
2. straight spout with diverter knob
3. curved / gooseneck-like spout
4. short-projection spout close to wall
5. wide-body decorative spout
6. slip-fit spout with some wobble / lower confidence
7. threaded spout with better body retention but varied outlet geometry
8. low-clearance spout / wall geometry where adapters or hangers have little room

这不是为了做 plumbing encyclopedia，
而是因为 bathtub filter 的失败大多发生在 **live fill（真实注水）** 条件下，而不是静态摆拍里。

## 3. tenant-friendly（租户友好）不等于工程上更稳
一个 bathtub filter 可以是 renter-friendly，如果它：
- 不需要永久改 plumbing
- 不开墙、不换龙头
- 能无痕拆除
- 不依赖胶粘或破坏性固定

但这并不自动意味着它：
- sealing 更好
- retention 更稳
- leak risk 更低
- compatibility 更广

### 当前更真实的判断
**renter-friendly 是一条安装 UX 轴，不是一条性能保证轴。**

很多 bathtub filter 一旦同时追求：
- tool-free
- renter-friendly
- fits most tubs
- easy install

就很容易在下列维度让步：
- forced water path
- anti-slip retention
- overflow discipline
- pressure tolerance

## 4. “leak” 至少应拆成 4 类
用户嘴里的“漏水”，工程上其实可能是四件事：

### A. bypass leak
部分水根本没有走 intended media path（预期滤材路径）。

### B. top overflow
在高流速下，水从 housing 顶部或非预期开口溢出。

### C. seam / housing leak
外壳接缝、接口、卡扣位置渗漏。

### D. retention failure
装置滑脱、摆动、半脱落，导致导流失稳、喷溅或部分绕流。

### 为什么这重要
市场评论里这些都会被合并成：
- it leaks
- it doesn’t work
- slips off

但对产品工程与售后来说，根因完全不同。

## 5. fill-speed tradeoff 是这个类目的第一性矛盾
当前最关键的工程矛盾仍然是：
- 流速高 → 注水快，但接触时间短、overflow 风险上升、过滤可信度下降
- 流速低 → 接触时间更友好，但用户等待成本迅速上升

所以真正该问的问题不是：
- 最慢条件下能不能过滤得很好

而是：
- **在用户仍愿意接受的 fill speed 下，还剩多少可信 performance？**

这才是 bathtub filter route 的真实 engineering benchmark。

## 6. 不同架构的 fill-speed / compatibility 取舍
### tub-spout inline / forced-path route
优点：
- 最强的“水真的过了滤材”可信感
- 更适合窄化为 chlorine-conscious route

代价：
- compatibility burden 最大
- pressure / overflow / seam risk 更高
- 更容易在正常注水速度下变慢或失控

### hanging bath-ball / drop-down route
优点：
- 前台更容易讲 easy install
- 看起来更 renter-friendly

代价：
- bypass skepticism 更高
- 挂点位置差异会导致结果很不稳定
- slip / swing / partial miss 风险更高

### soft-hanging / pouch-like route
优点：
- 仪式感强、parenting / comfort story 好讲
- 最像轻量、柔和的 bath accessory

代价：
- hygiene / drying burden 最大
- forced-path credibility 最弱
- 最容易被质疑成“看起来在过滤”而不是真正 engineered filtering

## 7. “fits most tubs” 在什么情况下开始失真
一旦出现下列情况之一，这句话就开始不可信：
- 产品只在 reduced flow 下表现可接受
- 用户需要 workaround（胶带、发圈、奇怪调流）
- diverter spout compatibility 没有明确规则
- curved / short / decorative spout 上稳定性明显下降
- 产品依赖某种 underside/lip geometry，但没写清
- 高水压或快注水时 overflow / splash 风险明显上升
- 客服需要大量靠照片 / 人工判断用户家能不能装

也就是说，**“fits most tubs” 的失真点，不是绝对装不上，而是成功条件变得隐藏化。**

## 8. 更可防守的 compatibility 承诺应该长什么样
更稳的说法不是 universal fit，而应该是：
- supports clearly defined common spout types
- performs under stated fill-speed conditions
- no adhesive workaround required
- low slip / low overflow / low seam-leak under repeated use
- unsupported configurations are easy to self-identify before purchase

## 9. 对 KES 的直接启发
### 不该追求
- universal-fit 幻觉
- tool-free / renter-friendly / high-flow / premium filtering 同时全拿

### 更该追求
- bounded-fit matrix（有边界的适配矩阵）
- engineering-visible anti-slip / overflow logic
- normal-use fill-speed discipline
- unsupported spout types 的前置识别
- leak taxonomy 级别的内部验证，而不是笼统写 leak test passed

## Sources
- [Bathtub Filter 安装风险矩阵 — V2](./bathtub-filter-installation-risk-matrix-v2.md)
- `../../raw/products/bathtub-filter/2026-04-15-compatibility-engineering-and-water-jurisdiction-pass.md`
