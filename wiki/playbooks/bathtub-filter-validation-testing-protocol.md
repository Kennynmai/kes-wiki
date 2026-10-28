---
type: playbook
status: draft
owner: strategy
created: 2026-04-12
updated: 2026-10-28
visibility: company
confidence: medium
officiality: draft
domain: operations
domains: [bathtub-filter, validation, testing, protocol, chloramine]
source_count: 1
review_cycle: monthly
verification_status: spot-checked
related:
  - ../products/bathtub-filter/bathtub-filter-kes-go-no-go-memo-v1.md
  - ../products/bathtub-filter/bathtub-filter-kes-route-screening-memo-v2.md
  - ../products/bathtub-filter/bathtub-filter-chloramine-media-research.md
  - ../source-summaries/bathtub-filter-kes-internal-product-materials-2026-04-17.md
  - ../source-summaries/bathtub-filter-onlyzone-supplier-material-evidence-2026-04-17.md
  - ../source-summaries/bathtub-filter-caso3-chloramine-contradiction-event-2026-10-09.md
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
| ⏳ 内部待补（2026-09-05 新增） | **V1 配置溢流包络复测** | 单片 PET 盘 + KDF55 130 g + CaSO₃ 110 g，20 / 25 / 30 / 35 L/min | 现有 35 L/min 数据来自 204 g KDF + 45 g 炭配置；V1 复测前 PDP / Amazon 不写 35 |
| ⏳ 内部待补（2026-09-05 新增） | **KDF 仓装填高度 / 床层位移** | 实测装填高度；25 L/min 下透明仓观察床层是否位移 | 几何核算填充率 36–44%，见 [[bathtub-filter-decision-register]] D-10 |
| ⏳ 内部待补（2026-09-06 新增） | **动态挂重与挂点位移** | V1 整机 + 介质 + 防溢仓满水（~0.6 L）称重；25 L/min 注水下路线 A（提拉头）/ B（3M 挂钩）/ C（扎带）各记录位移与回弹 | 估计湿重 1.5–2 kg 全经硅胶挂带落在挂点；现有只有 freestanding 静态 2 kg |
| ⏳ 内部待补（2026-09-05 新增） | **泡泡浴 / bath bomb 通过浴盐仓** | 0.7 mm × 3,846 孔板起泡与顶溢观察 | 卖点页 §5 三条浴盐卖点无测试记录 |

### Module 4 — Maintenance / refill economics
| 状态 | 测试项 | 方法 / 条件 | 结果 / 依赖 |
|---|---|---|---|
| ✅ 内部已完成 | 活性碳 pre-rinse 验证 | acid-washed coconut shell 8–10 目，0.3 MPa / 29 L/min，200 L 穿过后复测 | 2 min pre-rinse 即清除初始粉；干燥一天后无粉末 → 支持 "no pre-rinse required" claim |
| ✅ 内部已完成 | 导流模块必要性 | KDF 层 vs CaSO₃ 层 有无导流的冲蚀对比 | KDF 层无差异；CaSO₃ 层无导流则中心冲蚀形成 crater → 导流模块为 CaSO₃ 层 operational requirement |
| ⏳ 外部待补 | 订阅节奏与家庭经济 | 1 child / 2 child / family mixed-use 场景下的 refill cadence 与年度成本 | 阻塞订阅方案设计；与寿命口径（水量/次数/周）直接挂钩 |
| ⏳ 外部待补 | 长期霉变测试 | Version A 在湿润浴室环境 4–8 周存放下的内部霉变倾向 | Doc 2 B0742KFY9R 布袋霉变 16 赞差评——Version A 硬壳方案需要验证同类风险已消除 |

| ⏳ 内部待补（2026-09-05 新增） | **在位滴干防霉观察** | V1 挂在龙头上、每日一次注水、不取下，观察 30 天霉变 / 异味 | 决定维护指令能否从"每次取下晾干"降级为"在位滴干 + 每周深晾"（维护指南 §一）|
| ⏳ 内部待补（2026-09-05 新增） | **试纸触发可读性** | 用候选试纸在 1 / 2 ppm 进水、滤芯 90 / 80 / 50% 三档出水下盲读 | 决定 D-11；粗档试纸预期只能读出 50% 点 |

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
| ❌ 明确不覆盖 | 氯胺城市去除率 | Version A 媒体对 NH₂Cl 效率 | Version A 不声称氯胺去除，Version B 待规划。**2026-10-09 措辞修订**：本行原写「CaSO₃ 对氯胺基本无效」——该表述过强。CaSO₃ 在氯胺场景下的表现目前是**未知**，不是已知为零；无对照观测（供应商 `ZONET20230707001`）指向相反方向但不足以支撑延展。**2026-10-28**：KES 一方 bench test 因加标物种从未确认而退出该证据，KES 自有的物种确认氯胺数据点为 **0**。**边界本身不变**——Version A 依然不覆盖氯胺场景；变的是理由。见 [[bathtub-filter-caso3-chloramine-contradiction-event-2026-10-09]] |
| ⏳ 外部待补 | **受控 CaSO₃ × 氯胺测试**（2026-10-09 新开）| 见下方 Module 7 规格 | **不阻塞 Version A launch**，但它是决定 KES 是否具备氯胺城市能力的唯一未解问题。若结果为阳性，将影响 Version B 架构与 A-14 地区优先级假设 |
| ❌ 明确不覆盖 | Well water iron / H₂S / hardness | Version A 媒体对 Fe²⁺ / Mn²⁺ / H₂S | KDF55 + CaSO₃ 非此路径；需要 KDF85 + 催化炭。见 [[bathtub-filter-well-water-research]] |
| ❌ 明确不覆盖 | 日式 45°C+ 高温浸浴 | Version A 媒体在 >42°C 下的稳定性 | 测试覆盖 38–42°C；偏离此范围未验证 |
| ⏳ 外部待补 | 软水器下游用户（14–22M US 户）| 对软水器处理后水的去氯效果 | 软水器不去氯，标称 chlorine 含量应与 untreated tap 相近，理论上 Version A 适用，但未实测 |

### Module 7 — CaSO₃ × 氯胺受控测试规格（2026-10-09 新开）

> 触发来源：亚硫酸钙 × 氯胺矛盾事件。完整分析见 [[bathtub-filter-caso3-chloramine-contradiction-event-2026-10-09]]。

**这个测试要解决的问题**：现有的**一份**数据（供应商 `ZONET20230707001`）**无法区分「介质去除了氯胺」与「氯胺自己降解了」**。因为它测的就是待去除物本身，而该物种在温水中本就不稳定。

> **2026-10-28 前提修正**：本 Module 原写「现有的两份数据」。其中 KES 一方台架的**加标物种身份不可确认**，已退出氯胺证据（推定为游离氯路径）。**KES 自有的物种确认氯胺数据点现为 0。** 见 [raw pass｜2026-10-28 加标试剂身份回查](../../raw/products/bathtub-filter/2026-10-28-caso3-2026-10-09-reagent-identity-check.md)。**这不改变本 Module 的规格，但改变了它的紧迫性**：现在没有任何己方数据能替代这份供应商报告的位置。


**决定性对照 — 氯离子质量平衡**：氯胺若被真实还原为氨，每 1 mol NH₂Cl 破坏释放 1 mol Cl⁻。离子色谱测氯离子成熟、廉价、且**对物种不敏感，完全免疫于加标衰减这个混淆因素**——它测的是反应的**产物**，不是底物。测进水 Cl⁻、无介质空白在配对时间/温度下的 Cl⁻、出水 Cl⁻。若出水氯离子增量恰好等于比色所隐含的去除量 → 结论成立；若无增量 → 颜色下降是衰减或干扰。

**最小规格：**

| 要求 | 规格 |
|---|---|
| 分析方法 | DPD 电流滴定区分游离/化合氯 **+ 离子色谱测氯离子**。声明 LOD 与 LOQ |
| 实验臂（≥4）| (a) 介质 + 挑战水；(b) 无介质挑战水，时间/温度配对（衰减空白）；(c) 惰性介质，床体积与 ΔP 配对（水力空白）；(d) **量产规格 3–4 mm `ZONE-CL-A02 Gen-3`，130 g** |
| pH | 受控并报告 7.0 / 7.8 / 8.5。Yiin 1987 预测该区间出现分化；只测单一 pH 无法区分化学与假象 |
| 温度 | 20 / 38 / 42 °C |
| 通水量 | **做连续序列直到突破**，不是单点。这是唯一能产出与寿命模型兼容结果的方式 |
| 复测 | 每个条件 n ≥ 3 |
| 物种定义 | 测试前**先书面澄清**供应商报告中的「三氯铵」实为一氯胺、二氯铵还是三氯胺 |
| **加标试剂身份（2026-10-15 新增，最高优先级；2026-10-28 补来源并收紧为硬门槛）** | **投加前必须书面确认试剂的 CAS 号与物种。**「氯胺 T」（CAS 127-65-1，固体有机氯胺衍生物，溶于水水解生成 HOCl / OCl⁻）**≠ 一氯胺**（CAS 10599-90-3，NH₂Cl，市政水真实结合氯）。用氯胺 T 做加标测的是**游离氯**去除，不是氯胺去除。若目标是市政水氯胺，用一氯胺标准液，或次氯酸+氨按 **Cl₂:NH₃-N ≈ 4.5:1（质量比）** 现场配比（In-Situ：最优 4.5:1，水厂常规 3:1–5:1；Snoeyink & Jenkins 经 Curry & Associates 引用：化学计量 5.06 mg Cl₂/mg NH₃-N；**> 5:1 才向二氯胺/三氯胺偏移，< 4.5:1 留下游离氨**），**并立即测 pH**（pH 6.5–8.5 为一氯胺优势区，**< 7 有利于二氯胺/三氯胺**，投加的氯胺 T 自身水溶液呈弱碱性、pH 通常约 8.5）。**配好后必须用 DPD 法分别测游离氯与一氯胺确认物种**，配比、pH、读数一并写入测试记录。**2026-10-28 升级为硬门槛**：**物种未经「物种特异性方法」确认的加标测试，不得进入证据库**——不是「事后补个记录」的问题，而是该数据点直接作废（KES 三次自测：无一次确认过物种）。|
| **标称浓度必须由方法读出（2026-10-28 新增）** | **挑战液的标称浓度不得由配比推算，必须由方法读出并记录。** 2026-10-09 标称 4 ppm、色卡目视落点 1–2 区；2026-10-15 标称 2 ppm、读数 0.5–1 ppm —— **两次挑战液的标称值都比卡上读数高 2–4 倍**，而稀释误差、配液后衰减、色卡读低三者均未排除。配液记录里必须写「读数」，不是写「目标值」。|
| **挑战液不得就地自制（2026-10-28 新增）** | **在没有一氯胺标准液的情况下，不得用「现场配比」做正式加标测试**。KES 内部至今没有一氯胺标准液（操作者 2026-10-12 原话：「没有实验室氯胺标液准」）。自配挑战液可以作为**预试**（探索介质是否有反应倾向），但**结果只能作为内部线索，不能进入证据库，也不能进任何对外材料**。|
| **第三方实验室：物种拆分是加项（2026-10-28 新增）** | **按国标 `GB/T 5750.11-2023` 做的氯胺测试只给「总氯胺」，不拆一氯胺 / 二氯铵 / 三氯化氮**（实验室口径，2026-10-12）。即：**花钱做国标氯胺测试，仍然无法证明测的是一氯胺**。本 Module 需要的 **DPD 自由/化合区分 + 离子色谱测 Cl⁻ 是国标之外的加项**，询价时必须逐项写明，否则会拿到一份「总氯胺」数字而误当作物种确认。**2026-10 报价锚点**：游离氯 800 元/点位、氯胺 1000 元/点位；另有「全程加标」与「点加标」两档（游离氯 9000 / 4000 元；氯胺 10000 / 5000 元）。排期时须重新询价。|
| 介质规格 | 用 3–4 mm 生产规格，不用 2–3 mm（后者是 Gen-4 旧代 SKU）|

> **来源（2026-10-15）**：[氯胺T 实测报告评估](../source-summaries/bathtub-filter-chloramine-T-measurement-2026-10-15.md)。该次测试报告「无去除」，但挑战物身份错误，因此**对氯胺零信息量**。教训：一个名字写得松的加标试剂，产出的会是一份「看起来有效」的、属于另一个物种的数据集。
>
> **配比与 pH 来源（2026-10-28 补录）**：In-Situ / ChemScan《Water Chloramination Process Control》（最优 Cl₂:NH₃-N = 4.5:1，水厂常规 3:1–5:1）；Curry & Associates《Using the Correct Arithmetic to Form Monochloramine》（2015，rev. 2023），引 Snoeyink & Jenkins 1980（化学计量 5.06 mg Cl₂ : 1 mg NH₃-N）；Halogen Systems《Measuring Monochloramine Without Reagents》（配比 4.5:1–5:1；pH 6.5–8.5 一氯胺占优，< 7 偏向二氯胺/三氯胺）。物种身份一手登记：PubChem CID 3641960 / CID 25423。完整复核记录见 [[bathtub-filter-disinfectant-types-and-media-guide]] §1b-bis。
>
> **附带发现——照片本身就是数据。** 五张测试照片在室内灯 / 室外阴影 / 直射日光下拍摄，同一块印刷标准色块的跨图差异**量级上远大于同图相邻色阶之间的差异**（具体数值已于 2026-10-15 自查中撤回，见 [[../source-summaries/bathtub-filter-chloramine-T-measurement-2026-10-15]] §3.1）。**照片比色数据不得跨图比较**。若必须拍照存档，应固定光源、固定色温、每张画面内同时包含色卡与样品，且不做跨图趋势解读。
>
> **2026-10-28 补充：为什么「加标试剂身份」这一条要从「记录要求」升格为「准入门槛」。**
> KES 三次自测台架：① ≤2026-09-24 那次，试剂未记录、照片无试剂瓶、操作者自述「可能配错了」→ **数据点作废**；② 2026-10-15 那次，试剂写明是**氯胺 T**（测的是游离氯）→ **对氯胺零信息量**；③ 至今**没有一次**用物种特异性方法确认过物种。**结论不是「下次记得写」，而是「不确认就不算数据」。** 证据链见 [raw pass｜2026-10-28 加标试剂身份回查](../../raw/products/bathtub-filter/2026-10-28-caso3-2026-10-09-reagent-identity-check.md)。
>
> **本 Module 的排期含义**：目前全库唯一一条物种写明的 CaSO₃ × 氯胺 观测是供应商 2023 年那份报告。它同时是「唯一观测」和「不可采信观测」——**这个组合比它单独存在时更危险**，因为它很容易被当成「已有证据」。**在没有受控数据之前，任何对外材料都不得引用它。**

**通过标准（建议，待 owner 确认）**：出水氯离子增量与 DPD 测得的化合氯去除量在分析不确定度内闭合，且该结果在**有介质臂**与**无介质衰减空白臂**之间有统计显著差异。

**不通过怎么办**：CaSO₃ × 氯胺 这一格从「⚠️ 未验证」改回「❌ 无效」，且此次是**基于受控数据**——这才是它原本就应该有的证据基础。

### Summary — Version A 测试缺口排序（按阻塞度）
1. **Supported spout matrix**（Module 2）：阻塞 launch，必须在 shipping 前完成
2. **第三方 DPD 法 free-chlorine 前后对比**（Module 1）：阻塞 "≥99% in fresh-filter best-experience segment" claim 的外部证据
3. **竞品样品头对头**（Module 5）：阻塞 WS2 差异化语言，也阻塞 "Unlike mixed-bead products" conditional claim
4. **长期霉变测试**（Module 4）：阻塞硬壳方案的 trust 外部验证（竞品痛点）
5. **寿命曲线末段验证**（Module 1）：阻塞 "143 次 / 1 年" 寿命承诺的 late-stage 行为
6. **TPU strap 长期耐用**（Module 2）：次级阻塞，但直接关系差评风险
7. **受控 CaSO₃ × 氯胺测试**（Module 7，2026-10-09 新开）：**不阻塞 Version A**，但它是 Version B 氯胺架构与假设 A-14 地区优先级的唯一前置条件。成本低、有明确规格，应尽早排期。**2026-10-28 优先级上调**：KES 自有的物种确认氯胺数据点已归零，全库唯一一条物种写明的观测只剩供应商 2023 那份不可采信报告 —— 本 Module 从「验证一个已有争议」变成「建立第一份可用证据」。
