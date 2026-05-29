---
source_type: screenshot-set + web-scan
extraction_mode: progressive
created: 2026-05-18
domain: product
domains: [bathtub-filter, atmospheric-vacuum-breaker, backflow-prevention, plumbing-safety]
verification_status: spot-checked
---

# Raw Capture｜大气式真空破坏器 AVB 部件调查（2026-05-18）

## Capture
用户提供两张中文示意图，核心标签包括：
- 大气式真空破坏器（AVB）
- 大气进来
- 排气孔
- 浮子 / 阀芯
- 进水口 / 进口
- 负压状态下吸入空气，使管道压力与大气压力平衡，达到平衡后阀门自动关闭
- 防止污水倒吸

## Classification
- source_type: screenshot-set + web-scan
- material type: engineering component illustration
- likely component: Atmospheric Vacuum Breaker, AVB
- adjacent category: backflow prevention / backsiphonage protection

## Narrow Reading Notes
### What the component is
AVB 是一种非加压、依靠空气入口打开来破坏真空的防倒流部件。它主要应对 backsiphonage（倒虹吸 / 负压倒吸），而不是持续背压。

### What it is not
- 不是过滤器
- 不是止回阀的完整替代
- 不是可长期承压的 inline shutoff 后端部件
- 通常不应放在下游还有关闭阀的结构里

### Design relevance for bathtub-filter
AVB 对 KES 的直接意义不是“要把 AVB 当作滤芯卖点”，而是提醒：
- faucet / tub-spout 外接产品存在倒吸、负压、污染回吸的 plumbing-safety 维度
- 如果产品有软管、容器、浸没出口、过滤腔残水或下游可关闭结构，需要更谨慎地评估 backflow / backsiphonage risk
- 对外宣称上应避免把 AVB 说成“过滤能力”或“净水能力”

## External Sources Checked
- ASSE product standards overview: https://asse-plumbing.org/standards/product-standards/
- Watts 288A atmospheric vacuum breaker product page: https://www.watts.com/products/plumbing-flow-control-solutions/backflow-preventers/vacuum-breakers/288a
- Watts atmospheric vacuum breaker brochure / installation guidance: https://www.watts.com/dfsmedia/0533dbba17714b1ab581ab07a4cbb521/23525-source/es-wq-288a-pdf
- Zurn Wilkins 35XL atmospheric vacuum breaker product documentation: https://www.zurn.com/products/water-control/backflow-preventers/35xl

## Open Verification Needs
- Confirm applicable standard and jurisdiction for target market: ASSE 1001 / CSA B64.1.1 / local plumbing code.
- Confirm whether any KES candidate bathtub-filter architecture creates an AVB-relevant hazard: submerged outlet, downstream shutoff, hose connection, reservoir, or cleaning/backwash workflow.
- Confirm with plumbing / compliance reviewer before treating AVB as required or sufficient.
