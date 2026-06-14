---
type: product
status: draft
owner: strategy
created: 2026-05-31
updated: 2026-05-31
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [rv-bathroom-sink-faucet, compatibility, installation, engineering, leak-risk]
source_count: 4
review_cycle: monthly
verification_status: working
related:
  - ./rv-bathroom-sink-faucet.md
  - ./rv-bathroom-sink-faucet-complaint-taxonomy-and-risk-matrix.md
  - ./rv-bathroom-sink-faucet-test-gating-checklist-for-kes.md
---

# RV Bathroom Sink Faucet 兼容性工程断点

## 为什么有这页
这页回答：

> RV bathroom faucet 到底会在哪些 compatibility / installation / leak 条件下，从“direct replacement”变成“退货风险”？

## 1. `4-inch centerset` 只是起点，不是完整适配定义
页面常写 2-hole / 4-inch centerset，但真实安装至少还包括：
- 台面厚度
- 孔径
- shank 有效长度
- thread 规格和强度
- lock nut 空间
- 柜下手部操作空间
- 供水软管 / PEX / adapter 连接
- faucet base 与小台面后挡边距离
- spout reach 与小 basin 落水点

## 2. 需要的最低 fit taxonomy
### Vanity / deck
1. thin RV plastic vanity top
2. laminate / lightweight composite vanity top
3. thicker retrofit countertop
4. countersunk underside / uneven underside
5. tight cabinet access

### Sink / basin
1. very small oval RV sink
2. shallow rectangular RV basin
3. corner / compact vanity basin
4. small boat / wet-bar basin

### Supply connection
1. standard flexible supply line
2. RV PEX with adapter
3. short existing line with limited slack
4. nonstandard prior owner modification

## 3. “easy install” 最容易失真的地方
`easy install` 开始失真，通常不是孔位没对上，而是：
- shank 穿过台面后剩余螺纹不够
- lock nut 没空间拧紧
- 塑料牙一拧就滑
- 供水管角度被迫扭曲
- 台面底部沉孔导致连接不稳
- 用户无法看到慢漏点

所以 KES 的安装定义应从：
> fits 4-inch centerset

升级为：
> fits 4-inch centerset with stated deck thickness, thread length, lock-nut clearance, and supply connection boundary.

## 4. “leak” 至少应拆成 6 类
### A. Shutoff drip
阀芯关不严，表现为持续滴水。

### B. Cartridge / stem leak
开关处渗水，常被用户描述为 hot/cold knob leaking。

### C. Body / base internal leak
水从本体或底座内部进入台面或柜体，最危险。

### D. Supply connection leak
shank / thread / washer / supply line 连接处漏。

### E. Aerator / spout leak
起泡器或出水口接口漏，通常与螺纹和装配相关。

### F. Swivel joint leak
高弧旋转款独有风险，旋转后开始漏。

## 5. RV-specific durability 不是普通静态寿命
RV 环境还会增加：
- road vibration
- seasonal storage
- pressure regulator 不稳定或用户忘记使用
- campground pressure variation
- winterization / de-winterization
- intermittent use: 长时间不用后再通水

这意味着 KES 不能只做 household static water test。

## 6. Metal-first 的兼容性新风险
金属化能解决塑料牙和廉价感，但也带来：
- 重量增加
- rigid connection 增加装配容差要求
- 金属表面与水斑 / cleaner / corrosion 预期提高
- brass / stainless / plating 与 lead-free claim 证据要求提高

所以 metal-first 不是无条件加金属，而是优先加在：
- shank
- thread
- cartridge seat
- handle/stem
- body stress points

## 7. 更可防守的兼容承诺
页面应明确：
- 4-inch centerset, 2-hole
- required hole size
- deck thickness range
- shank length
- thread specification
- included adapters / supply hoses if any
- spout height and reach
- recommended basin size / water landing illustration
- not compatible conditions if identified

## 8. 对 KES 的直接启发
### 不该追求
- `universal RV faucet` 幻觉
- 只写 4-inch centerset
- 只靠 lifestyle image 展示高弧
- 不展示 underside 和 thread length

### 更该追求
- bounded-fit matrix
- installation tolerance test
- leak taxonomy validation
- measured reach / water landing proof
- RV vibration and intermittent-use testing

