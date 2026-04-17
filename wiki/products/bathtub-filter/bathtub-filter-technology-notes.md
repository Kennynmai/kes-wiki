---
type: product
status: draft
owner: product
created: 2026-04-11
updated: 2026-04-17
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, filtration-media, technology]
source_count: 9
review_cycle: monthly
verification_status: spot-checked
related:
  - ./bathtub-filter.md
  - ./bathtub-filter-claims-and-certifications.md
  - ./bathtub-filter-media-efficacy-at-bath-conditions.md
  - ../../source-summaries/bathtub-filter-kes-internal-product-materials-2026-04-17.md
---
# 浴缸过滤器（bathtub filter）技术说明

## Obsidian links
- [[bathtub-filter]]
- [[bathtub-filter-claims-and-certifications]]
- [[bathtub-filter-kes-concept-brief-v1]]
- [[bathtub-filter-patent-and-technical-landscape]]
- [[bathtub-filter-kes-product-architecture-hypotheses]]

## 为什么有这页
当前 bathtub filter 市场，明显大量借用了 shower filter 的 media storytelling（滤材叙事）。

这页用来记录：
- 市场上反复出现的技术构件
- 各种 media / chemistry route 的直觉优缺点
- KES 在把这些技术词当成“产品差异化”之前，应该先问哪些问题

## ⚠️ KES Version A 内部实测数据（2026-04-17 补充）

> 详见完整来源：[KES 内部产品材料 2026-04-17](../../source-summaries/bathtub-filter-kes-internal-product-materials-2026-04-17.md)

以下为 KES 自己的 Version A（urban municipal tap water，38–42°C）架构内部测试数据。这是本页第一次载入 **first-party empirical data**（此前只有外部 literature 与 marketplace 信号）。

### Version A 媒体栈（已确认架构，非候选）
沿水流方向顶 → 底：**PP fiber 盘（顶 2 张 + 底 1 张 mesh）→ 可选 loading cavity（240 mL）→ KDF55 层（110 g，5–10 目，15 mm 高腔，60-mesh 304 网夹）→ CaSO₃ 层（130 g，3–4 mm 粒，15 mm 高腔，40-mesh 304 网夹）→ outlet**。顶部设 overflow trough + 宽入口；内腔带 **导流模块**（已验证必要性，见下）。

### EBCT 与 KDF 去氯贡献（内部经验系数，38–42°C）
| 注水流速 | 单层 EBCT | KDF 去氯贡献 |
|---|---|---|
| 15 L/min | 0.95 s | 43% |
| 20 L/min | 0.71 s | 32% |
| 25 L/min | 0.57 s | 26% |
| 30 L/min | 0.48 s | 21% |

**关键含义**：浴缸注水的 EBCT（<1 秒）对 KDF 来说太短，**KDF 不可能做主力去氯**。这直接推翻了市场上"KDF = 核心去氯"的叙事，并把 **CaSO₃ 正式定位为主力去氯 KPI**，KDF 定位为 **末端风险兜底层 + 寿命稳定层 + 生物膜抑制层**。

### 系统总去氯链式公式
> **总去氯 = 1 − (1 − KDF) × (1 − CaSO₃)**

| 注水流速 | CaSO₃ @ 99% 段 | CaSO₃ @ 95% 段 | CaSO₃ @ 90% 段 | CaSO₃ @ 50% 段 |
|---|---|---|---|---|
| 15 L/min | 99.43% | 97.15% | 94.30% | 71.50% |
| 20 L/min | 99.32% | 96.60% | 93.20% | 66.00% |
| 25 L/min | 99.26% | 96.30% | 92.60% | 63.00% |
| 30 L/min | 99.21% | 96.05% | 92.10% | 60.50% |

详细寿命模型见 [[bathtub-filter-media-efficacy-at-bath-conditions]] Section 9。

### Version A 系统级去氯直测（2026-03-20 内部 bench test，5 mg/L 压力条件）
首次系统级直测（此前只有分媒体的经验系数 + 缩放自 40 g 宁立参考的寿命模型，没有 "X ppm in → Y ppm out" 的端到端实测）。原始数据：[2026-03-20 内部直测](../../../raw/products/bathtub-filter/2026-04-17-kes-internal-chlorine-removal-bench-test.md)（2026-04-17 交付）。

被测架构：35 孔 PP 棉盘 15 mm + KDF55 110 g + CaSO₃ 130 g（与 Version A 媒体栈一致）；原水自由氯 **5 mg/L**（约为寿命模型 2 ppm 基线的 2.5×，属压力条件而非名义条件）；方法：**氯试纸比色法**（非 DPD，5 条试纸照片 + 3 段 20260320.mp4 视频存档）。

| 进水压力 | 流速 | 出水余氯 | 去除率 | 注释 |
|---|---|---|---|---|
| 0.2 MPa | 16.5 L/min | 0.5 mg/L | ~90% | 接近寿命模型 15 L/min 段 |
| 0.3 MPa | 21 L/min | 0.7 mg/L | ~86% | US 典型龙头下限 |
| 0.4 MPa | 27 L/min | 0.8 mg/L | ~84% | US 典型龙头上限 |
| ~0.5 MPa | 30 L/min | 1.5 mg/L | ~70% | envelope 上缘，斜率陡增 |

**关键含义**：
- 在 **2.5× 压力条件下**（5 mg/L vs. 寿命模型用的 2 ppm），Version A 在美国典型龙头出水 18–25 L/min 段仍能保持 84–86% 去除；30 L/min 段显著下落（70%），提示 envelope 上缘可能接近 breakthrough
- 压力是独立变量、流速是 downstream——27→30 L/min 之间的陡降可能有两种成因叠加：（a）EBCT 进一步缩短触及 breakthrough；（b）压力升至 ~0.5 MPa 引起床压实或局部 channeling（0.5 MPa 也是 2024-11-07 overflow envelope 测试的上限起步压力，与本测试 30 L/min 段重合）
- 单测量、无复测、试纸比色刻度粗（典型 0.5 / 1.0 / 1.5 mg/L 档位 → 0.7 / 0.8 mg/L 为内插读数）、新旧滤芯累计通水量未标注 → 无法将数据点落到寿命模型曲线上；**不能作为 label claim 证据**，但可作为 Version A 在高压力输入下的方向性闭环
- 需要第三方 DPD 法复测（2 ppm 基线 + 5 ppm 压力双条件）以替换 η=0.9 缩放假设并确认 27→30 L/min 斜率

见 [[bathtub-filter-validation-testing-protocol]] Module 1 对此测试的闭环标注。

### 导流模块的必要性（2025-10-22 测试结论）
- 在 **KDF 层**：有无导流无可见差异（KDF 粒大床密，抗冲刷）
- 在 **CaSO₃ 层**：**无导流时中心形成冲蚀 crater**；加导流后水流均匀铺开
- → 导流模块是 **CaSO₃ 层的 operational requirement**，不是可选项

### 流速 / 溢水 envelope（2024-11-07 内部实测）
204 g KDF（10–40 目）+ 45 g acid-washed coconut-shell carbon（8–10 目），0.5 MPa，瞬时 38–40 L/min，目标 178 L：
- **无顶部 fiber 盘**：35 L/min 即溢水；多次冲击后床压实 → 间歇性溢水
- **1 mesh + 1 非织造 fiber 盘**：35 L/min **不溢水**
- **1 mesh + 2 非织造 fiber 盘**：35 L/min **不溢水**（已达 envelope 上限）
- **1 mesh + 3 非织造 fiber 盘**：开始溢水（流阻过大）

美国典型浴缸龙头出水 18–25 L/min，**2-盘配置在 no-overflow envelope 内有显著余量**。

### 活性碳选型（2024-07–08 commissioning 验证）
- 选择：**acid-washed coconut shell 8–10 目**（ash ≤0.5%，hardness ≥95%，iodine 1,000–1,200 mg/g）
- 验证：2-min pre-rinse 后，0.3 MPa / 29 L/min 穿 200 L 水已无粉末溢出；干燥一天后复测仍无粉末
- → 对标 B008A4AG2U 差评 "carbon powder all over tub"（10 赞），KES 出厂即通过 pre-rinse 验证，**可在 onboarding 写 "no pre-rinse required"**

---

## ⚠️ 先读这个：消毒剂种类对媒体选择有根本性影响
> 详见：[[bathtub-filter-disinfectant-types-and-media-guide]]

**核心结论：** "氯"在龙头端有三种不同化学形态——游离氯（HOCl/OCl⁻）、一氯胺（NH₂Cl）、二氧化氯（ClO₂）。常见滤材对三者的去除效果**截然不同**：
- 亚硫酸钙、KDF 只对**游离氯**有效；对氯胺无效
- 维生素 C 同时对游离氯和氯胺有效，但氯胺需要 4+ 分钟接触时间（浴缸注水场景可满足，淋浴不行）
- 催化活性炭是目前对氯胺最有效的固态滤材，但仍需要充足接触时间

约 35–40% 的美国市政系统使用氯胺；在这些城市，标准 KDF + 亚硫酸钙组合**不足够**。

---

## 市场上反复出现的 media / technical signals
### KDF 55
常被当作核心信任信号，通常与以下表述一起出现：
- chlorine reduction
- heavy-metal reduction
- odor reduction

工作提醒：
- KDF 是该品类最常见的 credibility anchor（可信度锚点）之一
- 但“contains KDF” 不等于成品性能已经被证明

### activated carbon（活性炭）
常与 KDF 或 multi-stage system 组合出现。

工作提醒：
- 它是用户非常熟悉的默认过滤可信度信号
- 但在 warm / hot water 使用条件下，temperature 与 contact time（接触时间）问题都很关键

### vitamin C
常被放在 gentler / skin-friendly / baby-friendly 的语境中。
有时还会与 alkaline、skin / hair benefit 等语言绑定。

工作提醒：
- 在 beauty / skin / baby positioning 上更容易讲故事
- 即使工程细节差异很大，它对某些 segment 仍有商业吸引力

### calcium sulfite（亚硫酸钙）
常见于 shower-filter 风格的技术叙事，通常与 hot-water chlorine reduction 相关。

工作提醒：
- 这是值得重点深挖的 media route 之一
- 因为 bathtub use 往往就是 warm / hot water scenario

### zeolite / ceramic balls / mineral stones / alkaline balls
经常出现在 multi-stage、8-stage、15-stage、17-stage 这类 listing 里。

工作提醒：
- 它们会显著增强“复杂、高级”的感知
- 但真实边际收益，常常不如 marketing complexity 那么明显

## 这个品类的技术边界提醒
### 1. temperature matters（温度很重要）
浴缸注水通常是 warm / hot water。
所以任何在高温下性能明显衰减的路线，都必须谨慎处理。

### 2. contact time matters（接触时间很重要）
真实 tub-fill 往往意味着：
- 流速较高
- 接触时间较短

这会严重限制小体积 media 在实际使用中的效果。

### 3. device size matters（体积很重要）
如果产品很小，却同时宣称广泛去除多种污染物，就应该默认提高怀疑阈值。
除非有很强的产品级证据，否则不应轻易接受这类 broad-removal story。

### 4. water path matters（过水路径很重要）
如果设计并不能强制水流经过足够体积、足够有效的 media，
那么真实功效很可能远弱于 marketing story。

## 当前市场技术表达的典型模式
很多 listings 看起来都在把“滤材名称”本身当作说服机制：
- KDF
- activated carbon
- calcium sulfite
- vitamin C
- ceramic balls
- mineral stones
- multi-stage counts

这意味着：
- media stack 本身已经是一种主要 marketing language pattern
- stage count 很多时候更像“感知复杂度”，不一定是真正可靠的购买指标

## NSF/ANSI 177 的适用范围限制（2026-04-17 补充）

### 标准实际测试条件（已确认）
- 挑战浓度：**2.0 mg/L 游离有效氯（FAC）**
- 最低去除率：**50%**（须在整个额定使用寿命内保持）
- 测试水温：**40°C**
- 测试流速：**≥1.0 GPM**（低于此流速即判定失败）
- 测试压力：**80 psi 动态压力**

### 最关键的范围限制
**NSF/ANSI 177 的标题是"Shower Filtration Systems — Aesthetic Effects"，其适用范围是淋浴（shower）场景，不是浴缸水龙头（tub spout / bathtub filler）。**

对 KES 的直接含义：
- 安装在浴缸水龙头上的 bathtub filter，**不能声称通过 NSF/ANSI 177 认证**——该认证根本不适用于此产品形态
- 市场上部分 bath filter 使用"tested to NSF/ANSI 177"的表述，技术上超出了该标准的适用范围
- **目前没有专门针对 bathtub filler filter 的等效 performance 标准存在**（NSF 认证列表中没有"Bath Filter"分类）

### Bath filter 可以申请的替代认证路径
- **NSF/ANSI 42**（Drinking Water Treatment Units — Aesthetic Effects）：覆盖更广泛的家用水处理，包括游离氯去除，不限于淋浴场景——但测试条件不完全等同于浴缸使用场景
- **NSF/ANSI 61**（Drinking Water System Components — Health Effects）：材料安全认证，验证产品接触水的材料不释放有害物质——不评估过滤性能，但可作为材料安全背书
- **WQA Gold Seal**：行业协会认证，覆盖结构完整性、材料安全和文档，适合作为 NSF 路径的补充或替代

### 对宣称的操作含义
- ❌ 不能写："通过 NSF/ANSI 177 认证"（认证范围限于淋浴产品）
- ⚠️ 谨慎写："参照 NSF/ANSI 177 测试方法进行了内部测试"（需说明非官方认证）
- ✓ 可以追求：NSF/ANSI 42 listing，或 WQA 认证，或独立第三方测试报告（需明确测试条件）

## 浴缸条件下的滤材效能（2026-04-17 实测数据补充）

> 详见完整分析：[[bathtub-filter-media-efficacy-at-bath-conditions]]

### 最关键的逆直觉发现：低流速有利于氯去除

独立消费评测（waterfilterguru.com，2026，比色法）实测对比：

| 产品 | 快速流速氯去除率 | 慢速流速氯去除率 |
|------|------|------|
| Santevia（亚硫酸钙 + 炭）| 100% @ 1.65 GPM | 100% @ 0.36 GPM |
| Canopy（亚硫酸钙 + 炭 + KDF-55）| 50% @ 3.6 GPM | **100%** @ 0.6 GPM |
| Crystal Quest（同上）| **0%** @ 3.79 GPM | 85% @ 0.97 GPM |
| Tubo（KDF）| **0%** @ 3.61 GPM | 100% @ 0.87 GPM |

浴缸注水典型流速（0.3–0.8 GPM）处于"慢速流速"区间——多数产品在此条件下达到 85–100%。  
**结论：浴缸注水条件对氯去除有利，NSF 177 在 ≥1.0 GPM 下通过的产品，在浴缸注水条件下表现应更好，不会更差。**

### 滤芯寿命：浴缸使用比淋浴消耗快 2–4 倍

| 产品 | 额定容量 | 浴缸使用次数（40 加仑/次）|
|------|------|------|
| Santevia | ~3,000 加仑 | ~75 次（约 2.5 个月）|
| Canopy | 2,700 加仑 | ~67 次（约 2 个月）|
| **Sprite** | **~900 加仑** | **~22–25 次（< 1 个月）** |

**关键工程含义：** 标注淋浴使用寿命的滤芯规格，不能直接套用于浴缸产品。滤芯设计必须基于加仑数，而非月数。

### 温度效应总结
- KDF：热水（37–40°C）下电化学反应速率更高，效果好于冷水（Arrhenius 动力学）
- 亚硫酸钙：热水下媒体溶出率 <0.01%（冷水 <0.06%），高温更稳定，反应不可逆
- 标准 GAC：热水下面临热脱附风险；催化活性炭（化学降解机制）无此问题

## KES 最终应验证什么
- 哪些 media 真正适合 bathtub fill 的温度与流速条件？
- 哪种 media combination 能在 credibility 与 complexity 之间取得最好平衡？
- 哪些技术路线最适合支撑 legal-risk 较低的 claim language？
- 哪种技术故事最容易解释，而且不过度承诺？

## 当前早期判断
最有商业价值的路线，未必是 media 种类最多的那种。
它更可能是这样一种组合：
- water-path logic 最清晰
- hot-water story 讲得通
- claim language 更克制
- refill / maintenance 更简单

## Sources
- 公共片段中可见的 KDF、activated carbon、vitamin C、calcium sulfite、zeolite 与 multi-stage bath-filter 文案
- bathtub filter competitor scan
- [Best Bath Filters 2026 – Water Filter Guru](https://waterfilterguru.com/best-bath-filters/)
- [[bathtub-filter-media-efficacy-at-bath-conditions]]
- [[bathtub-filter-chloramine-media-research]]
