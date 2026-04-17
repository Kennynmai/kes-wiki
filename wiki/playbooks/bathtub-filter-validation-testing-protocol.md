---
type: playbook
status: draft
owner: strategy
created: 2026-04-12
updated: 2026-04-17
visibility: company
confidence: medium
officiality: draft
domain: operations
domains: [bathtub-filter, validation, testing, protocol]
review_cycle: monthly
verification_status: spot-checked
related:
  - ../products/bathtub-filter/bathtub-filter-kes-go-no-go-memo-v1.md
  - ../products/bathtub-filter/bathtub-filter-kes-route-screening-memo-v2.md
  - ../source-summaries/bathtub-filter-kes-internal-product-materials-2026-04-17.md
  - ../source-summaries/bathtub-filter-onlyzone-supplier-material-evidence-2026-04-17.md
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

---

## Validation log — Version A（urban municipal tap water，38–42°C）

> 来源：[KES 内部产品材料 2026-04-17](../source-summaries/bathtub-filter-kes-internal-product-materials-2026-04-17.md)
>
> 遵循用户 feedback：测试先于写入 docs。以下表格记录每个 test module 的内部已完成项与外部待补项。

### Module 1 — Normal-flow chlorine reduction
| 状态 | 测试项 | 方法 / 条件 | 结果 / 依赖 |
|---|---|---|---|
| ✅ 内部已完成 | KDF 去氯贡献系数 | 15 / 20 / 25 / 30 L/min 下经验系数 | 43% / 32% / 26% / 21%；EBCT 0.95 / 0.71 / 0.57 / 0.48 s |
| ✅ 内部已完成 | CaSO₃ 寿命模型 | 130 g，η=0.9（缩放自 40 g 宁立参考报告）| 2 ppm：≥99% ≈ 3,481 L / mandatory ≈ 25,467 L；1 ppm：×2 |
| ✅ 供应商侧已完成 | **CaSO₃ reference report 已 math-validated**（2026-04-17）| Zibo Onlyzone ZONET20251113001（2025-12-26 完成）= 40g / 0.5–1mm / 8 L/min / 2 ppm 自由氯，12 点采样。η=0.9 × 3.25 = 2.925× 缩放规则对 ≥99/95/90/50% 四档逐点验证吻合 Version A 表内数字 | η=0.9 的 **数学可追溯性已建立**；**物理假设仍未第三方验证**（见 [[bathtub-filter-media-efficacy-at-bath-conditions]] Section 9）。供应商内部实验室，非独立第三方。粒径差异（0.5–1mm reference vs. 3–4mm 生产）未在此测试中处理 |
| ✅ 内部已完成 | 系统总去氯链式公式 | 1 − (1 − KDF) × (1 − CaSO₃) | 15 L/min × 99% CaSO₃ 段 → 99.43% 系统 |
| ✅ 内部已完成 | **Version A 系统级去氯直测（5 ppm 高压力，2026-03-20）** | 35孔 PP 棉盘 15 mm + KDF55 110 g + CaSO₃ 130 g；原水 **5 mg/L 自由氯**（≈2.5× 寿命模型 2 ppm 基线）；**压力 0.2 / 0.3 / 0.4 / ~0.5 MPa** 产生 **16.5 / 21 / 27 / 30 L/min** 四点；**氯试纸比色法**（5 条试纸照片 + 3 段视频 20260320.mp4 存档）。详见 [2026-03-20 内部直测](../../raw/products/bathtub-filter/2026-04-17-kes-internal-chlorine-removal-bench-test.md)。**温度 / 新旧滤芯累计通水量未标；无重复测量** | 16.5 L/min → 0.5 mg/L (~90%)；21 L/min → 0.7 mg/L (~86%)；27 L/min → 0.8 mg/L (~84%)；30 L/min → 1.5 mg/L (~70%)。US 典型龙头出水 18–25 L/min 段保持 84–86%。27→30 L/min 斜率陡增（14pp），可能是 envelope 上缘 breakthrough 征兆，**也可能是压力升到 ~0.5 MPa 后床压实 / 局部 channeling 所致**，需重复 |
| ⏳ 外部待补 | 第三方 DPD 法 free-chlorine 前后对比 | US tap water 1–2 ppm 条件下，独立实验室（非 WaterFilterGuru 比色法）| 需要用于替换 η=0.9 缩放假设；或 WQA Gold Seal 申请过程自带测试 |
| ⏳ 外部待补 | EBCT-分辨率测试 | 同一滤芯在 15 / 20 / 25 / 30 L/min 下独立测定去氯率 | 需用于验证内部 KDF 贡献经验系数（43/32/26/21%）是否在新批次 KDF 上保持 |
| ⏳ 外部待补 | 寿命曲线末段验证 | 实测 CaSO₃ 进入 <50% 段时的 breakthrough 曲线是否与"η=0.9 线性模型"一致 | 与寿命口径承诺（143 次泡 / 1 年）直接挂钩 |
| ⏳ 外部待补 | **3–4mm 生产规格粒径复测** | 供应商 reference 用 0.5–1mm CaSO₃；Version A 生产用 3–4mm。更大粒径 = 更少比表面 = 动力学更慢。η=0.9 是否已隐式吸收此差异未知 | 需在 Version A 实际滤芯上做一轮独立测试，或用 3–4mm 规格重复供应商协议 |

### Module 2 — Installation / compatibility
| 状态 | 测试项 | 方法 / 条件 | 结果 / 依赖 |
|---|---|---|---|
| ✅ 内部已完成 | Overflow envelope | 204 g KDF + 45 g carbon，0.5 MPa，瞬时 38–40 L/min | 无 fiber 盘：溢水；1 mesh + 2 fiber 盘：35 L/min 无溢 |
| ⏳ 外部待补 | Supported spout matrix | 对 diverter / non-diverter / swan-neck / slip-fit 真实龙头做矩阵测试 | 阻塞 [[bathtub-filter-supported-spout-matrix]] stub；必须在 launch 前完成 |
| ⏳ 外部待补 | TPU strap 长期耐用 | 重复 mount / unmount 100+ 周期 | Doc 2 竞品差评中 B008A4AG2U "strap 断裂" 42 赞，需避免同类问题 |

### Module 3 — Leak / stability durability
| 状态 | 测试项 | 方法 / 条件 | 结果 / 依赖 |
|---|---|---|---|
| ⏳ 外部待补 | 完整压测 | 重复 mount / bath-fill 循环，seam / seal / 悬挂稳定性 | Doc 2 B008A4AG2U "外壳漏水" 7 赞差评，B0012045EO "安装问题" 67 赞差评 |
| ⏳ 外部待补 | 高水压测试 | US 高楼层 70+ PSI 条件 | 需要验证 Version A 在非典型高水压下不爆 |

### Module 4 — Maintenance / refill economics
| 状态 | 测试项 | 方法 / 条件 | 结果 / 依赖 |
|---|---|---|---|
| ✅ 内部已完成 | 活性碳 pre-rinse 验证 | acid-washed coconut shell 8–10 目，0.3 MPa / 29 L/min，200 L 穿过后复测 | 2 min pre-rinse 即清除初始粉；干燥一天后无粉末 → 支持 "no pre-rinse required" claim |
| ✅ 内部已完成 | 导流模块必要性 | KDF 层 vs CaSO₃ 层 有无导流的冲蚀对比 | KDF 层无差异；CaSO₃ 层无导流则中心冲蚀形成 crater → 导流模块为 CaSO₃ 层 operational requirement |
| ⏳ 外部待补 | 订阅节奏与家庭经济 | 1 child / 2 child / family mixed-use 场景下的 refill cadence 与年度成本 | 阻塞订阅方案设计；与寿命口径（水量/次数/周）直接挂钩 |
| ⏳ 外部待补 | 长期霉变测试 | Version A 在湿润浴室环境 4–8 周存放下的内部霉变倾向 | Doc 2 B0742KFY9R 布袋霉变 16 赞差评——Version A 硬壳方案需要验证同类风险已消除 |

### Module 5 — Claims validation
| 状态 | 测试项 | 方法 / 条件 | 结果 / 依赖 |
|---|---|---|---|
| ✅ 内部已完成 | FAQ 与定位语 claim-level 映射 | Doc 1 FAQ verbatim → [[bathtub-filter-claim-register]] allowed / conditional wording | Version A 首批 wording 已填入；WS2 竞品差异化仍可二次优化 |
| ✅ 内部已完成 | "≥99% in fresh-filter best-experience segment at 15 L/min" 有界性审核 | 寿命模型 + 系统链式公式 + EBCT 系数三者闭环 | 闭环成立；但依赖 η=0.9 假设（待外部复测） |
| ⏳ 外部待补 | chlorine test strip 赠品的 lot-to-lot 一致性 | 3 批试纸在同一 tap water 上读数一致性 | 与 "Verify with the included chlorine test strip" claim 直接挂钩 |
| ⏳ 外部待补 | 竞品样品 chlorine-removal 头对头 | KES Version A vs B008A4AG2U / B0742KFY9R / B08Y8GSVJS / B0C5D7NLC7 / B0012045EO 在同一 tap water 上的 DPD 法前后对比 | 阻塞 "Unlike mixed-bead products" conditional claim 的公开 wording；用作 WS2 差异化证据 |

### Module 6 — Version A scope boundary verification（新增）
| 状态 | 测试项 | 方法 / 条件 | 结果 / 依赖 |
|---|---|---|---|
| ❌ 明确不覆盖 | 氯胺城市去除率 | Version A 媒体对 NH₂Cl 效率 | CaSO₃ 对氯胺基本无效；Version A 不声称氯胺去除。Version B 待规划 |
| ❌ 明确不覆盖 | Well water iron / H₂S / hardness | Version A 媒体对 Fe²⁺ / Mn²⁺ / H₂S | KDF55 + CaSO₃ 非此路径；需要 KDF85 + 催化炭。见 [[bathtub-filter-well-water-research]] |
| ❌ 明确不覆盖 | 日式 45°C+ 高温浸浴 | Version A 媒体在 >42°C 下的稳定性 | 测试覆盖 38–42°C；偏离此范围未验证 |
| ⏳ 外部待补 | 软水器下游用户（14–22M US 户）| 对软水器处理后水的去氯效果 | 软水器不去氯，标称 chlorine 含量应与 untreated tap 相近，理论上 Version A 适用，但未实测 |

### Summary — Version A 测试缺口排序（按阻塞度）
1. **Supported spout matrix**（Module 2）：阻塞 launch，必须在 shipping 前完成
2. **第三方 DPD 法 free-chlorine 前后对比**（Module 1）：阻塞 "≥99% in fresh-filter best-experience segment" claim 的外部证据
3. **竞品样品头对头**（Module 5）：阻塞 WS2 差异化语言，也阻塞 "Unlike mixed-bead products" conditional claim
4. **长期霉变测试**（Module 4）：阻塞硬壳方案的 trust 外部验证（竞品痛点）
5. **寿命曲线末段验证**（Module 1）：阻塞 "143 次 / 1 年" 寿命承诺的 late-stage 行为
6. **TPU strap 长期耐用**（Module 2）：次级阻塞，但直接关系差评风险
