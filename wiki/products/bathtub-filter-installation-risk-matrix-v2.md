---
type: product
status: draft
owner: strategy
created: 2026-04-12
updated: 2026-04-15
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, installation, compatibility, risk, normalized]
source_count: 9
review_cycle: monthly
verification_status: spot-checked
related:
  - ./bathtub-filter-installation-risk-matrix.md
  - ./bathtub-filter-pricing-refill-flow-fit-table-v2.md
  - ./bathtub-filter-compatibility-engineering-breakpoints.md
---
# 浴缸过滤器（bathtub filter）安装风险矩阵 — V2

## 版本链接
- 早期页面：[[bathtub-filter-installation-risk-matrix]]

|风险领域|归一化类别|当前关键判断|风险等级|为什么重要|
|---|---|---|---|---|
|原生 tub-spout compatibility|geometry / fit variance|tub spout 并不是单一安装环境；至少要区分 slip-fit / threaded、diverter / non-diverter、straight / curved、short / decorative 等不同几何|高|一旦适配成功依赖隐藏条件，“fits most tubs” 就会开始失真|
|fill-speed penalty|performance / UX tradeoff|高流速带来更低接触时间与更高 overflow 风险；低流速则带来等待成本|高|用户不愿为了可信过滤长期忍受极慢注水|
|slip / swing / weak retention|attachment stability|市场评论与 Q&A 已反复出现 slips off / hangs well for some 的高方差模式|高|滑脱会在用户判断有效性之前先摧毁信任|
|bypass flow|water-path integrity|有些 route 看似安装成功，但并不能保证大部分水真的走了 intended media path|高|这会直接破坏“过滤”本身的可信感|
|top overflow / splash|live-fill failure|在更快流速 / 更高压力下，housing 顶部溢出或喷溅是结构性风险|高|这是最容易触发 immediate return 的 failure mode 之一|
|seam / housing leak|housing integrity|接缝、接口、卡扣处漏水不一定常被单独描述，但在浴室产品里不可原谅|高|浴室场景对 leak tolerance 极低|
|tenant-friendly vs engineering robustness|installation UX tradeoff|tool-free / renter-friendly 并不等于 sealing、retention、pressure stability 更强|中高|太强调“无工具 + 广泛适配”往往意味着工程上有取舍|
|drying / care burden|maintenance burden|尤其 soft-hanging route 会引入晾干、卫生、反复处理负担|中|增加 ritual friction，也可能引发卫生质疑|
|universal-fit overclaim|marketing / support risk|一旦需要 workaround、照片判断、奇怪调流，universal-fit 就不再可信|高|广告承诺与真实家庭环境不匹配，会放大售后与差评压力|

## 当前阶段性结论
### 1. 安装问题不只是“能不能挂上去”
真正决定 bathtub filter 是否成立的，是以下几件事能否同时过关：
- geometry fit
- retention stability
- forced water path
- overflow discipline
- acceptable fill speed

### 2. 兼容性（compatibility）应该被视为 product architecture 问题
这不是包装页上的小 FAQ，
而是决定 route 是否 survive 的核心工程层。

### 3. 更合理的目标不是 universal fit，而是 bounded fit
比起“适用于大多数浴缸”，更可防守的是：
- 明确 supported spouts
- 明确 unsupported spouts
- 明确推荐流速范围
- 明确不需要 workaround 的前提条件

## Sources
- [Bathtub Filter 兼容性（compatibility）工程断点](./bathtub-filter-compatibility-engineering-breakpoints.md)
- `../../raw/products/bathtub-filter/2026-04-15-compatibility-engineering-and-water-jurisdiction-pass.md`
