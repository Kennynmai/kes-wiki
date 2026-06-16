---
type: product
status: draft
owner: strategy
created: 2026-06-15
updated: 2026-06-15
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, validation, testing, bench-spec, dechlorination, flow-rate, 25lpm]
source_count: 4
review_cycle: monthly
verification_status: working
related:
  - ./bathtub-filter-kes-product-architecture-hypotheses.md
  - ./bathtub-filter-media-efficacy-at-bath-conditions.md
  - ./bathtub-filter-assumption-register.md
  - ../../playbooks/bathtub-filter-validation-testing-protocol.md
---

# 浴缸过滤器 25L/min 去氯特征测试 spec（去氯率 × 流量 × 压降 × 床体积）

## 为什么有这页

这份 spec 是 KES bathtub filter 当前 **唯一卡住 go/no-go 与产品形态的物理未知** 的测试规格：

> **在 25 L/min+ 的客户要求流量下，系统能守住多高的去氯率？为守住目标去氯率，CaSO₃ 床要做多大？由此决定的壳体体积，挂篮形态能不能稳挂不溢流？**

它**不是从零设计**，而是把 2026-03-20 的内部比色单测（见下）**硬化为第三方、可重复、DPD、真实浓度的特征曲线**。

**与「首要价值」的关系**：KES bathtub filter 的首要价值定为「**看得见·测得到的诚实过滤**」。这份测试就是「测得到」那一半的 **proof obligation #1**——没有它，首要价值是空头支票，和我们鄙视的对手（in-progress 认证说成 Certified、内部比色说成 clinically tested）是同一种放大。

---

## 0. 已有数据基线（不要从零重测）

### 已完成（内部，2026-03-20 系统级直测）
配置：35 孔 PP 棉盘 15 mm + KDF55 110 g + CaSO₃ 130 g；原水 **5 mg/L 自由氯**（≈2.5× 寿命模型 2 ppm 基线）；氯试纸比色法。

| 压力 (MPa) | 流量 (L/min) | 去氯率 |
|---|---|---|
| 0.2 | 16.5 | ~90% |
| 0.3 | 21 | ~86% |
| 0.4 | 27 | ~84% |
| ~0.5 | 30 | ~70%（断崖 −14pp）|

EBCT 经验系数（KDF 贡献）：15 / 20 / 25 / 30 L/min → 43% / 32% / 26% / 21%；EBCT 0.95 / 0.71 / 0.57 / 0.48 s。
溢流包络：204 g KDF + 45 g carbon，0.5 MPa 瞬时 38–40 L/min；1 mesh + 2 fiber 盘下 **35 L/min 无溢流**。

### 这组数据的六个缺口（本 spec 要逐一关闭）
1. **单次无重复** → 无法判断 27→30 断崖是真 breakthrough 还是偶发
2. **氯试纸比色法**，非 DPD → 不可作第三方可核查证据
3. **水温未记** → CaSO₃/碳动力学随温变化，38–42℃ 洗澡水未隔离
4. **累计通水量未记** → 不知是新芯还是已部分耗尽，去氯率无寿命坐标
5. **粒径未对齐**：生产 3–4 mm vs 供应商参考 0.5–1 mm（比表面更小 = 动力学更慢，η=0.9 是否已隐式吸收未知）
6. **进水浓度 5 ppm**，非北美真实龙头 1–2 ppm → 真实浓度下的去氯率与寿命会不同

---

## 1. 测试要回答的三个判定问题

| # | 问题 | 判定它的目的 |
|---|---|---|
| Q1 | **25 L/min、真实 1–2 ppm、第三方 DPD 下，去氯率是多少？** | 决定「25L/min 不牺牲去氯」能不能上首屏；锁定 claim 数字 |
| Q2 | **27→30 L/min 断崖是 breakthrough 还是床压实/沟流？** | 决定 25L/min 离失效边缘有多远（安全裕度）；呼应防沟槽②、leak A 类 bypass |
| Q3 | **为在 25L/min 守住目标去氯率，CaSO₃ 床要多大？** | 床体积 → 壳体尺寸/重量 → 挂篮可挂载性（第二块②的闭环） |

---

## 2. 测试矩阵

### 2.1 主矩阵：流量 × 进水浓度（DPD，每点 ≥3 重复）
固定基准配置（生产规格）：PP 盘 + KDF55 110 g + CaSO₃ 130 g，**3–4 mm 生产粒径**，水温 **40±2℃**，新芯（throughput=0）。

| 流量 (L/min) | 进水 1 ppm | 进水 2 ppm | 备注 |
|---|---|---|---|
| 15 | ☐ | ☐ | 慢速/最大接触时间锚点 |
| 20 | ☐ | ☐ | US 龙头常见下沿 |
| **25** | ☐ | ☐ | **客户目标，主判定点** |
| 27 | ☐ | ☐ | 断崖前沿 |
| 30 | ☐ | ☐ | 断崖点，复现 2026-03-20 |
| 33 | ☐ | ☐ | 断崖后，确认形状 |

> 每格 ≥3 次重复，报告均值 + 极差。进出口同一 DPD 方法、同一操作者、同一批试剂。

### 2.2 床体积梯度（回答 Q3）
固定 25 L/min、2 ppm、40℃、新芯，只变 CaSO₃ 质量：

| CaSO₃ 质量 | 100 g | 130 g（基准）| 160 g | 200 g |
|---|---|---|---|---|
| 去氯率 | ☐ | ☐ | ☐ | ☐ |
| 床高/截面 | ☐ | ☐ | ☐ | ☐ |
| 压降 ΔP | ☐ | ☐ | ☐ | ☐ |

输出：**「25L/min 守住 X% 所需的最小 CaSO₃ 床体积」**，直接喂第二块②的壳体尺寸/挂载性判断。

### 2.3 寿命坐标（回答缺口④⑤）
固定 25 L/min、2 ppm、40℃、基准床，沿累计通水量采样：

| 累计通水量 | 0 L（新芯）| 1,000 L | 2,000 L | 3,481 L（≥99% 段末模型值）| 寿命口径终点 |
|---|---|---|---|---|---|
| 去氯率 | ☐ | ☐ | ☐ | ☐ | ☐ |

输出：实测寿命衰减曲线，验证/证伪 η=0.9 线性模型与「143 次泡 / 1 年」承诺。

### 2.4 断崖诊断（回答 Q2）
在 27 / 30 / 33 L/min 三点，加做：
- **逐级进出口浓度**（PP 后、KDF 后、CaSO₃ 后各取样）→ 看是哪一层先失效
- **染色/示踪短路测试**（30 L/min）→ 区分「接触时间不足的均匀 breakthrough」vs「床压实/沟流的旁通」
- 升压至断崖后**回落复测**→ 若回落不可逆 = 床结构破坏（压实/沟道固化）

---

## 3. 测量方法（可核查硬性要求）

- **方法**：DPD 比色/分光法（Hach 或等效），**禁用氯试纸目视比色作为最终证据**（比色仅可作现场预读）
- **实验室**：独立第三方实验室；若走 WQA Gold Seal / NSF 42 申请，优先用申请过程自带测试
- **指标**：自由氯（free chlorine），mg/L 进出口；报告 % reduction = (in−out)/in
- **重复**：每条件 ≥3 次，报告均值 + 极差 + 是否落在 ±5pp 内
- **必记元数据**（缺一作废）：水温、累计通水量、进水浓度、流量实测值、压力、CaSO₃ 批次与粒径、试剂批次
- **控制**：空壳（无滤料）同流量跑一遍作 bypass 基线 → 量化「水没穿过料」的本底

---

## 4. 判定阈值（与 claim 直接挂钩）

| 结果 | 判定 | 触发的 claim / 决策 |
|---|---|---|
| 25 L/min、2 ppm、新芯 **≥85%**，且 25→27 斜率平缓（<5pp） | **PASS** | 可上首屏「25L/min 仍守住 ~85% 去氯（标注条件）」；25L/min 形态成立 |
| 25 L/min **70–85%**，但加大床（§2.2）可达 ≥85% | **CONDITIONAL** | 25L/min 要换更大壳体 → 回到第二块②评估挂载性；或首屏降流量、25 作上限标注 |
| 25 L/min **<70%**，或断崖前移到 25 以下 | **FAIL（route-breaking）** | 25L/min 不能当卖点；首屏改主打「合理流量 + 高实测去氯率」，25 仅作峰值上限 |
| 断崖为不可逆床压实/沟流（§2.4） | 形态红旗 | 必须改导流/装填结构，否则 leak A 类 bypass 会进真实差评 |

> 阈值里的「≥85%」基线来自 2026-03-20 在 5 ppm 高压力下 27L/min 仍达 84%；真实 1–2 ppm 下应不低于此，故 85% 是合理且偏保守的及格线。**若第三方实测显著低于此，说明 5 ppm 比色单测高估，正是必须早发现的事。**

---

## 5. 这份测试解锁什么（下游依赖）

- **首要价值「测得到」那一半** → proof obligation #1 兑现
- **A-01 / A-08 假设**（normal-flow 可行性、注水流速挑战）→ 从 weak/logic-only 升级为实测
- **产品形态（第二块②）** → 床体积定了，挂篮尺寸/重量/挂载性才能定
- **claim register** → 「≥X% at 25 L/min under stated conditions」的 wording 才有外部证据
- **WS2 竞品头对头** → 同一第三方 DPD 协议可顺带跑竞品样品，喂「Unlike mixed-bead products」差异化

---

## 6. 不在本 spec 范围（避免 scope 蔓延）

- 氯胺去除（Version B/V1.5，催化炭 + 浸泡件，另立）—— 含「混合/传质 vs 反应」原理与**氯胺版台架自变量设计**，见 [氯胺证据页 §9](./bathtub-filter-chloramine-media-research.md)
- 井水 Fe/H₂S（Version C，KDF85，另立）
- 龙头兼容矩阵 / 漏水耐久 / 霉变（[[bathtub-filter-validation-testing-protocol]] Module 2–4，并行但独立）
- 重金属去除（metal-first 是料级叙事，非健康声称，**不测、不宣称**）

---

## Sources / 内部依据

- [产品架构假设与确认记录](./bathtub-filter-kes-product-architecture-hypotheses.md)（EBCT 0.48–0.95s；KDF 降级 / CaSO₃ 去氯 KPI）
- [Bathtub Filter 验证 / 测试协议](../../playbooks/bathtub-filter-validation-testing-protocol.md)（Validation log — Version A，2026-03-20 直测 + 待补项）
- [研究假设台账](./bathtub-filter-assumption-register.md)（A-01 / A-08 route-breaking 敏感度）
- [媒体在 bath 条件下的效率](./bathtub-filter-media-efficacy-at-bath-conditions.md)（η=0.9 缩放与寿命模型）

## Obsidian links
- [[bathtub-filter]]
- [[bathtub-filter-kes-product-architecture-hypotheses]]
- [[bathtub-filter-validation-testing-protocol]]
- [[bathtub-filter-assumption-register]]
- [[bathtub-filter-media-efficacy-at-bath-conditions]]
