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
domains: [bathtub-filter, kes, positioning, problem-layer, product-definition, decision]
source_count: 6
related:
  - ./bathtub-filter-na-water-profile-and-target-market-analysis.md
  - ./bathtub-filter-kes-media-stack-options-by-water-type.md
  - ./bathtub-filter-kes-product-architecture-hypotheses.md
  - ./bathtub-filter-compatibility-engineering-breakpoints.md
  - ./bathtub-filter-25lpm-dechlorination-bench-test-spec.md
  - ./bathtub-filter-product-definition-language.md
review_cycle: monthly
verification_status: working
---

# KES Bathtub Filter 定位与问题层决策（2026-06-15）

## 为什么有这页

这页把 2026-06-15 一次产品策略讨论收敛成可执行决策，覆盖三块：
1. **问题层结论 + 红线**（哪些水源问题值得打、哪些是禁区）
2. **三个最易翻车的工程问题**（产品形态）
3. **首要价值定位骨架**（四层主次 + 证明义务）

**输入的产品定义**（客户给定）：通用壳体 + 滤材自由组合；大流量 25 L/min+；挂篮式不浸泡、水逐级完整流经；KDF+亚硫酸钙一年寿命；metal-first 高级铜锌合金料级；透明滤盒可见真料；真 multi-stage 全接触；每芯流道优化防沟槽。

**关键调和**：客户的「自由组合」≠ wiki 反对的「一根滤芯通吃」。它是 **同一平台上的按水源配方菜单**，把 wiki 的 A/B/C 三 SKU 从「三个产品」变成「一个壳体三套配方」。这化解了既有冲突。

---

## 一、问题层结论 + 红线

### 真问题强度（断层式，非平铺）

| 水源 | 真问题 | 证据强度 | 角色 |
|---|---|---|---|
| **游离氯城市**（~60% 大城市） | 游离氯 0.5–2.0 mg/L，已达 AD 皮肤损伤阈值（Seki 0.5） | **中到强**（机制级，唯一硬证据 + 大市场）| **主战场，品牌 all-in** |
| 氯胺城市（~40%）| 一氯胺，更难去除 | 问题强但固态滤芯单独搞不定 | 双段式（inline + 浸泡件）诚实覆盖 |
| 井水（~13% 户）| 铁/H₂S/锈味 | 真实但 nuisance 级 | 复用配方，nuisance/odor 叙事 |
| RV/房车 | 软管异味/余氯/沉积 | 真实 comfort 级 | 配方复用，不单列战场 |
| 雨水 | 软水低氯，但颗粒/微生物 | 弱，且真问题落在禁区（微生物）| 被动覆盖，不单列卖点 |

### 红线（不可核查 = 不说）
- ❌ 泡澡场景「去重金属保护皮肤」健康声称（无经皮暴露证据）
- ❌ 改善/治疗湿疹、baby-safe 医疗式安心
- ❌ 硬水「软化」（阻垢 ≠ 软化；A-13）
- ❌ 雨水/井水的杀菌、除砷/硝酸盐等安全级声称
- ✅ 可说且可第三方实测：**指定流量下的游离氯去除率、透明可见的真实料量料级、龙头兼容性**

### 两个已拍板的定性
- **25 L/min** = 真实客户需求（注水慢体验差），不是参数竞赛。但它与去氯率是物理对冲（流量↑→EBCT↓），**唯一解是加大 CaSO₃ 床**，代价转移到体积/压降/挂载性 → 见 [25L/min 测试 spec](./bathtub-filter-25lpm-dechlorination-bench-test-spec.md)。
- **metal-first** = 品牌理念/料级工程叙事（高级铜锌合金 vs 廉价 KDF），**不是去重金属健康声称**。与 EBCT 数据自洽：KDF 当可见英雄料（料级/抑菌/寿命），CaSO₃ 当幕后去氯主力。

---

## 二、三个最易翻车的工程问题（产品形态）

### ① 逐级全接触 vs 防沟槽（客户 1.7 + 1.8）
与已确认的 Version A 同向（反混合介质 + 严格分层 + 导流模块）。挂篮式低压流下真正风险是 **leak A 类 bypass——水没穿过料但用户看不出**。三杠杆：环隙密封（料盒-壳壁无环缝）、顶部布水板（避免单点射流冲沟）、分层装填密度（防上游压实结块）。**EBCT 只有在活塞流下才算数。** 验证：染色示踪 + 逐级进出口浓度。

### ② 25L/min 床尺寸 vs 挂篮可挂载性（客户 1.1 + 1.2）
**唯一硬约束，闭环张力**：25L/min → EBCT 更短 → CaSO₃ 床更大 → 壳体更重 → 挂篮越难稳挂（retention failure D 类 + 顶部溢流 B 类，25 已近 35L/min 包络边缘）。这是品类「第一性矛盾」。核心题：挂篮形态能否物理容纳 25L/min 去氯所需料量而不滑脱/溢流？不能则 25L/min 反逼换形态。→ 测试 spec §2.2 床体积梯度直接回答。

### ③ 自由组合防呆（客户 1.5）
模块化把「买错 SKU」转成「组错顺序/漏装层」，更隐蔽：顺序错（PP 必须最前、CaSO₃ 去氯主力、维C 是缸内独立步骤非滤层）= 效果归零，差评算 KES 头上；且无限组合 = 无法第三方测全，与可核查性 USP 冲突。**解法：后端模块化平台，前端引导式选择**——卖按水源命名的预配方（游离氯版/氯胺版/井水版）+ 物理防呆（异形/色标卡盒，唯一正确顺序）+ 前端水质自测问答。「自由组合」是工程真相，不该是首屏购买动作。

---

## 三、首要价值定位骨架

**首要价值（已拍板）= 「看得见·测得到的诚实过滤」**

> 别的滤芯把滤料藏起来、把数字吹起来；KES 把真料摆给你看、把去氯率测给你查。

### 四层主次（锁死，支撑层不抢首屏）

| 层级 | 内容 | 载体 |
|---|---|---|
| **首要价值** | 看得见（透明盒真料）+ 测得到（标注流量第三方去氯率）| 透明滤盒 + 实测数据 + 赠氯试纸自验 |
| **支撑结构** | 按你家水源配方（游离氯/氯胺/井水）| 模块化，但前端引导式选择，不卖散料 |
| **质感层** | metal-first 高级铜锌合金料级（可见英雄料）| KDF 可见英雄料；CaSO₃ 幕后去氯主力 |
| **证明点** | 大流量不牺牲去氯 | 25L/min，**待台架曲线坐实后**才能上首屏 |

### 证明义务（选了「可核查」= 必须兑现，否则沦为对手）
1. **第三方 DPD 去氯率测试**（标注流量+寿命段），非内部比色自说自话 → [测试 spec](./bathtub-filter-25lpm-dechlorination-bench-test-spec.md)
2. **逐级进出口数据**——透明盒看得见料，更要证明水真穿过料
3. **认证口径如实**：KDF55 继承 NSF/ANSI 42 材料端、CaSO₃ 内部参照 177 protocol、**成品不冒认 NSF**
4. **可见 ≠ 有效的防杠**：透明是信任钩子，文案要把「可见」与「实测有效」分开讲（防假设 4 陷阱）

### 对手开战位
- FilterBaby：藏滤芯、in-progress 认证说成 Certified、4 专利吹成 45+ → **KES：摆出来、测出来、口径如实**
- Canopy：美学优先、站外 BBB F + 霉变 → **KES：硬壳防霉（已拒软悬挂霉变路线）+ 工程可信**

---

## 四、下一步

1. ✅ 本决策落盘（本页）
2. ⏳ **执行 [25L/min 去氯特征测试 spec](./bathtub-filter-25lpm-dechlorination-bench-test-spec.md)** —— go/no-go 与形态总开关
3. ⏳ 第三块讨论：媒体 / EE-A-T 策略（「可核查」如何用内容兑现，对手 EEAT 弱点怎么打）

## Obsidian links
- [[bathtub-filter]]
- [[bathtub-filter-na-water-profile-and-target-market-analysis]]
- [[bathtub-filter-kes-media-stack-options-by-water-type]]
- [[bathtub-filter-kes-product-architecture-hypotheses]]
- [[bathtub-filter-compatibility-engineering-breakpoints]]
- [[bathtub-filter-25lpm-dechlorination-bench-test-spec]]
- [[bathtub-filter-product-definition-language]]
