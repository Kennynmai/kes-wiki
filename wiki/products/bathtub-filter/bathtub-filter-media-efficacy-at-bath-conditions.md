---
type: product
status: draft
owner: product
created: 2026-04-17
updated: 2026-04-17
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, filtration-media, technology, bath-conditions, flow-rate, temperature, lifespan]
source_count: 19
review_cycle: monthly
verification_status: spot-checked
related:
  - ./bathtub-filter-technology-notes.md
  - ./bathtub-filter-disinfectant-types-and-media-guide.md
  - ./bathtub-filter-chloramine-media-research.md
  - ./bathtub-filter-certification-and-testing-pathways.md
  - ../../source-summaries/bathtub-filter-kes-internal-product-materials-2026-04-17.md
  - ../../source-summaries/bathtub-filter-onlyzone-supplier-material-evidence-2026-04-17.md
---

# Bathtub Filter 媒体在浴缸条件下的效能

## 为什么有这页

NSF/ANSI 177 是针对淋浴过滤器的标准，其测试条件是：2.0 mg/L 游离氯、40°C、**≥1.0 GPM**。浴缸注水场景与这些条件**截然不同**——尤其是流速（0.3–0.8 GPM，远低于 1.0 GPM 的测试底线）。

这页回答的是：**同一个过滤器，在浴缸注水条件下，表现是更好还是更差？**

---

## 一句话结论（最重要的逆直觉发现）

> **浴缸注水的低流速实际上有利于氯去除**——独立测试数据显示，多数浴缸过滤器在快速流速下去除率极低（甚至 0%），但在慢速流速（接近浴缸注水条件）下达到 85–100%。

---

## 1. 浴缸注水 vs. 淋浴的工作参数对比

| 参数 | 淋浴（NSF 177 测试标准）| 浴缸注水（实际使用）| 差异显著性 |
|------|------|------|------|
| 温度 | 40°C（±2°C） | ~37–42°C | 基本相同 |
| 流速 | **≥1.0 GPM**（测试最低要求）| **0.3–0.8 GPM**（典型）| **显著不同** |
| 每次用水量 | 约 60–75 升（8 分钟 × 2 GPM）| 约 120–200 升（整缸）| **显著不同** |
| 滤材接触时间 | 数毫秒至 <1 秒 | 每单位水接触时间更长 | **显著更长** |
| 使用模式 | 高流速短时间 | 低流速长时间填满 | 不同 |

---

## 2. 流速效应：最关键变量

### 独立产品测试数据（waterfilterguru.com，2026，非认证实验室，使用比色法测试，常温水）

| 过滤器 | 媒体 | 快速流速 | 快速流速氯去除率 | 慢速流速 | 慢速流速氯去除率 |
|------|------|------|------|------|------|
| Santevia | 亚硫酸钙 + 炭 | 1.65 GPM | **100%** | 0.36 GPM | **100%** |
| Canopy | 亚硫酸钙 + 炭 + KDF-55 | 3.60 GPM | **50%（1 ppm）** | 0.60 GPM | **100%** |
| Sprite Chlorgon | Cu + Zn + 亚硫酸钙 | 2.53 GPM | **50%（1 ppm）** | 1.01 GPM | **100%** |
| Crystal Quest | 亚硫酸钙 + 炭 + KDF-55 | 3.79 GPM | **0%** | 0.97 GPM | **85%** |
| Tubo（8阶段，KDF）| KDF + 未披露 | 3.61 GPM | **0%** | 0.87 GPM | **100%** |

**关键推断：** 浴缸注水流速（0.3–0.8 GPM）处于或低于上表"慢速流速"范围，多数产品在此流速下达到 85–100% 去除率。这意味着浴缸注水条件**对氯去除有利，而非不利**。

### 机制解释

**KDF（电化学氧化还原）：**
- KDF 通过铜锌合金的电化学氧化还原反应去除游离氯：Zn + Cl₂ → ZnCl₂
- 较低流速 = 更长的空床接触时间（EBCT）= 每个氯分子有更多时间在媒体表面进行电子转移反应
- Clack Corporation 的实验室数据：45 in³ KDF-55 滤芯在 1 GPM 下测试至 82,640 加仑仍保持 94% 去除率

**亚硫酸钙（化学还原）：**
- 反应：CaSO₃ + Cl₂ + H₂O → CaSO₄ + 2HCl（不可逆反应）
- 亚硫酸根（SO₃²⁻）和游离氯的反应速率极快——有研究称 0.8 秒接触时间即可达到 99%+ 去除率
- 对于亚硫酸钙，流速降低带来的额外接触时间收益比 KDF 更有限（因为反应本身已经很快）

**活性炭（吸附 + 表面还原）：**
- 标准 GAC 在高温下面临热脱附风险——已吸附的氯可能在浴缸温度下重新释放
- 催化活性炭通过化学降解（而非吸附）去除氯，不存在热脱附问题

---

## 3. 温度效应

### KDF 在 37–40°C 下的表现

- 从热力学角度：电化学反应遵循 Arrhenius 动力学——温度每升高 10°C，反应速率约翻倍
- 多个制造商和分销商文档明确指出：KDF 在热水中效果优于冷水（不同于活性炭）
- KDF-55 额定工作温度范围：4–60°C（浴缸温度 37–40°C 处于最优区间中段）
- **数据缺口：** 没有任何公开的量化曲线（去除率 vs. 温度）存在；制造商宣称是方向性描述，非实验测量

### 亚硫酸钙在 37–40°C 下的表现

- AquaBliss 产品文档（制造商数据）：冷水（0°C）下媒体溶出率 <0.06%；热水下溶出率 <0.01%——热水下媒体反而更稳定
- 反应是放热、不可逆的——温度升高有利于反应速率
- 亚硫酸钙不存在活性炭的热脱附问题
- **数据缺口：** 无经同行评审的 CaSO₃ 在浴缸温度下的定量去除效率测量

### 活性炭在 37–40°C 下的表现（负面）

- 标准 GAC 的游离氯去除主要依赖物理吸附
- 温度升高会降低 GAC 的吸附容量（热脱附效应）——吸附的氯可能在热水中重新释放到水中
- 热水浴缸中使用标准 GAC 的产品性能可能低于测试标准（测试多在冷水或 40°C 下进行）
- 催化活性炭（通过化学分解，非吸附）不受热脱附影响

---

## 4. NSF/ANSI 177 认证与浴缸注水条件的关系

### 标准测试条件（已确认）

| 参数 | NSF/ANSI 177 要求 |
|------|------|
| 挑战浓度 | 2.0 mg/L ±0.2 mg/L 游离氯 |
| 温度 | 40°C ±2°C |
| 压力 | 80 psi 动态 |
| 流速 | **≥1.0 GPM**（低于此即判定失败）|
| 通过标准 | 整个额定寿命内 ≥50% 去除率 |
| 氯胺 | 测试水氯胺 <0.1 mg/L（**明确排除**）|

### 关键推断

- NSF 177 在 ≥1.0 GPM 下通过的产品，在 0.3–0.8 GPM 的浴缸注水条件下，**性能不会变差，方向上会更好**（接触时间更长）
- 但这仅是推断性证据，**没有认证标准覆盖浴缸注水（sub-1.0 GPM）的场景**
- 目前没有任何监管机构、标准机构或制造商发布过分析 NSF 177 认证结果是否可转移至浴缸注水条件的文件
- **数据缺口：** 这是一个完全未被研究的问题

---

## 5. 滤芯寿命：淋浴 vs. 浴缸注水

**这是浴缸过滤器产品设计中最重要的工程约束之一。**

### 基本换算

- 淋浴假设：2.0 GPM，8 分钟/次 = **~60 升/次**
- 浴缸注水假设：标准浴缸 ~115–190 升（30–50 加仑）= **~115–190 升/次**

同一个 10,000 加仑额定滤芯：
- 淋浴使用：~625 次（每天一次 ≈ 约 2 年）
- 浴缸注水使用（40 加仑/次）：~250 次（每月 30 次 ≈ 约 8 个月）
- **浴缸模式下耗材成本约为淋浴模式的 2–3 倍**

### 主要竞品滤芯寿命对比

| 品牌 | 额定容量 | 对应次数（40 加仑/次浴）| 对应月数（30 次/月）|
|------|------|------|------|
| Santevia | ~3,000 加仑 | ~75 次 | ~2.5 个月 |
| Canopy | 2,700 加仑 | ~67 次 | ~2.2 个月（90 天）|
| Crystal Quest | 2,500 加仑 | ~62 次 | ~2 个月 |
| Tubo | 2,500 加仑 | ~62 次 | ~2 个月 |
| **Sprite** | **~900 加仑** | **~22–25 次** | **<1 个月（最短）** |

**Sprite 的案例：** 官方声称 25–30 次浴的使用寿命，一个标准浴缸注水就消耗约 30–40 加仑，这意味着 Sprite 滤芯仅能维持约 22–25 次洗澡——不足一个月。这是品类内耗材年均成本最高的原因（约 $240/年）。

### 对 KES 产品设计的含义

- 以淋浴使用寿命标准（月数）来标注的浴缸过滤器滤芯，会导致用户实际使用寿命远短于预期
- **必须基于加仑数（gallons）而非月数来标注滤芯寿命**，并明确注明每次浴缸注水的推荐水量
- 滤芯媒体体积必须为浴缸应用场景专门设计——直接套用淋浴滤芯规格会造成过早失效和消费者投诉

---

## 6. KDF 制造商针对浴缸/水龙头应用的技术指导

**调查结论：KDF Fluid Treatment（现属 Kymera International）没有任何公开可获取的技术文件专门针对浴缸水龙头（tub spout）或 sub-1.0 GPM 龙头过滤器应用场景。**

- KDF 官网仅提及"热水应用，包括莲蓬头过滤器"
- 公司 POE 技术公告针对全屋系统（10 英寸床层深度，15 GPM/ft² 服务流速）——与浴缸水龙头无关
- 这是一个**已确认的知识空白**：浴缸注水过滤是没有相应行业技术标准的应用场景

---

## 7. 现有知识的置信度汇总

| 问题 | 结论 | 置信度 | 数据质量 |
|------|------|------|------|
| 37–40°C 时 KDF 表现优于室温？ | 是，方向性 | 中等 | 仅制造商宣称；无公开实验数据 |
| 低流速（0.3–0.8 GPM）改善去除率？ | **是，显著**——这是最关键的发现 | **高** | 第三方消费评测；与电化学理论一致 |
| NSF 177 认证在 <1.0 GPM 下仍适用？ | 形式上不适用；推断方向为正 | 中等 | 无已发布的转移性分析 |
| 亚硫酸钙在 37–40°C 下劣化？ | **否**——高温下更稳定 | 中等 | 制造商规格；无独立实验室数据 |
| 淋浴滤芯寿命标注在浴缸中有效？ | **否**——浴缸使用会加速 2–4 倍消耗 | **高** | 多个产品规格一致；基础数学推算 |
| KDF 有针对浴缸水龙头的技术指导？ | **不存在**（已验证的否定性发现）| **高** | 对 KDF/Kymera 公开文件的全面检索 |

---

## 8. 主要知识缺口（需要 KES 自行测试验证）

1. **无任何同行评审研究**在 37–42°C 对 KDF-55 或亚硫酸钙的氯去除效率进行定量测量（对比室温条件）
2. **无任何 NSF、AWWA 或 WQA 的发布分析**讨论 NSF 177 结果是否可转移至 <1.0 GPM 浴缸注水条件
3. **无任何亚硫酸钙与 NH₂Cl 反应速率的动力学研究**在浴缸相关温度下（期望：接近零效果）
4. **浴缸注水过滤**是当前学术上未被研究的空白应用场景——消费者评测（waterfilterguru.com）是目前唯一有比色法实测数据的来源
5. **没有任何生产商比较同一滤芯在淋浴流速 vs. 浴缸注水流速下的头对头性能数据**

---

## 9. KES Version A 寿命模型（2026-04-17 内部数据）

> 详见完整来源：[KES 内部产品材料 2026-04-17](../../source-summaries/bathtub-filter-kes-internal-product-materials-2026-04-17.md)

### 基础参数
- CaSO₃ 质量：**130 g**（3–4 mm 颗粒）
- 效率系数：**η = 0.9**（放大自"宁立"40g / 0.5–1mm / 8 L/min / 2 ppm 自由氯 参考报告，按质量比 3.25 × 0.9 缩放）
- 水温：38–42°C
- 泡澡基准：70 gal 满缸，2/3 填充 = 47 gal = **178 L/次**；3 次/周 = 12 次/月
- KDF 贡献系数：见 [[bathtub-filter-technology-notes]] EBCT 表
- 系统总去氯：**1 − (1 − KDF) × (1 − CaSO₃)**

### 2 ppm 自由氯条件（US 典型偏高段）— "系统总去氯" 寿命表

| 阶段 | 累计水量 | 泡澡次数（178 L/次）| 周数（3 次/周）|
|---|---|---|---|
| 系统 ≥99%（最佳体验段） | ~3,481 L | 19.6 | 6.5 |
| 系统 ≥95% | ~17,672 L | 99.3 | 33.1 |
| 系统 ≥90%（软换触发） | ~20,124 L | 113.1 | 37.7 |
| 系统 ≥80%（强换触发） | ~24,916 L | 46.6 | 15.5 月 |
| 系统 <50%（强制换） | ~25,467 L | 143.1 | 47.7（~1 年）|

### 1 ppm 自由氯条件（US 典型常见段）— 寿命约 ×2

| 阶段 | 累计水量 | 泡澡次数 | 周数 |
|---|---|---|---|
| 系统 ≥99% | ~6,962 L | 39.1 | 13.0 |
| 系统 ≥95% | ~35,343 L | 198.6 | 66.2 |
| 系统 ≥90% | ~40,248 L | 226.1 | 75.4 |
| 系统 <50%（强制换） | ~50,934 L | 286.1 | 95.4（~2 年）|

### 替换触发语义（非月数口径）
- **Soft trigger**：系统总去氯跌至 90% → 体验仍好，提示用户开始准备替换
- **Strong trigger**：跌至 80% → 进入快速衰减区，强烈建议替换
- **Mandatory**：跌至 50% → 视为失效，必须替换

### 口径设计决策（反品类默认）
Version A 的寿命口径使用 **累计水量 / 泡澡次数 / 周期**，**不使用月数**。原因：
1. 月数口径是淋浴产品沿袭（2.0 GPM × 8 min × 30 days = ~60 L/次 vs. 浴缸 178 L/次），套用到浴缸会让用户实际寿命短于预期 → 差评风险（见 [[bathtub-filter-review-patterns-and-return-risk]] 的 B0012045EO 时长不符投诉）
2. 水量口径与体验挂钩更紧，用户可以用 chlorine test strip 直接验证"我现在到哪个阶段"
3. 可直接用于订阅节奏设计：99% 段约 20 次浴 ≈ 6 周 → 小批量早期订阅；90%/80% 段约 113/140 次浴 ≈ 每 9 个月一次常规订阅

### 这段数据的已知限制（2026-04-17 更新：供应商 reference report 已到位）

**η = 0.9 缩放数学已逐点验证**（见 [Onlyzone 供应商材料证据 2026-04-17](../../source-summaries/bathtub-filter-onlyzone-supplier-material-evidence-2026-04-17.md)）：
供应商宗立 2025-12-26 报告 ZONET20251113001（40g / 0.5–1mm / 8 L/min / 2.0±0.2 mg/L 自由氯）的 4 个插值档 × 2.925 后，全部与 Version A 表内数字吻合：
- ≥99%: 1,190 L × 2.925 = **3,481 L** ✅
- ≥95%: 6,042 L × 2.925 = **17,673 L** ✅
- ≥90%: 6,880 L × 2.925 = **20,124 L** ✅
- ≥50%: 8,707 L × 2.925 = **25,467 L** ✅

状态升级：η=0.9 从"未验证的假设"→"**数学一致，物理假设未第三方复测**"。

### 仍然 open 的限制
- **η = 0.9 作为物理效率假设** 仍未经第三方 finished-product 复测
- **粒径差异**：供应商参考报告用 **0.5–1 mm** CaSO₃；Version A 生产使用 **3–4 mm**（ZONE-CL-A02 Gen-3 3–4mm）。更大粒径 = 更少比表面 = 动力学更慢。η=0.9 是否已隐式吸收此差异是**未知的**——需要用 3–4 mm 生产规格复测一轮（见 [[bathtub-filter-validation-testing-protocol]] Module 1）
- KDF 贡献系数（43/32/26/21%）标注为"内部经验值"，无附带原始实验条件
- 模型假设 2 ppm / 1 ppm 自由氯线性响应；超出此范围或氯胺场景下**不可外推**（CaSO₃ 对氯胺基本无效，见 [[bathtub-filter-chloramine-media-research]]）
- 水温假设 38–42°C；偏离此范围（如日式 45°C+ 浸浴）未覆盖
- 供应商 reference report 由 **供应商内部实验室** 出具（非独立第三方 CNAS/ilac/NSF 实验室）；KES 如果要对外公开寿命曲线，建议再补一轮独立第三方复测
- 验证待补充项见 [[bathtub-filter-validation-testing-protocol]] Module 1

---

## 9.5 Version A 系统级去氯直测（2026-03-20 内部 bench test，5 mg/L 压力条件）

> 原始数据：[2026-03-20 内部直测](../../../raw/products/bathtub-filter/2026-04-17-kes-internal-chlorine-removal-bench-test.md)（2026-04-17 交付）

Section 9 的寿命模型是由 KDF 经验系数 + CaSO₃ 供应商 reference report（2 ppm / 40 g / 0.5–1 mm）缩放 + 链式公式推出的 **推算曲线**。下表是 KES 2026-03-20 内部 bench test 给出的 **系统级直接测量**——首次把 "X ppm 进 → Y ppm 出" 的端到端结果接到同一架构上。

**被测架构**：35 孔 PP 棉盘 15 mm + KDF55 110 g + CaSO₃ 130 g（与 Version A 一致）
**压力条件**：原水自由氯 **5 mg/L**（约为 Section 9 寿命模型 2 ppm 基线的 2.5×；属压力测试，而非名义工况）
**测量方法**：**氯试纸比色法**（非 DPD；5 条试纸照片存档 + 3 段 `20260320.mp4` 视频存档）
**独立变量**：**进水压力**（0.2 / 0.3 / 0.4 / ~0.5 MPa）；流速为 downstream 响应

| 进水压力 | 流速 | 出水余氯 | 实测去除率 | 对照 Section 9 模型预测 |
|---|---|---|---|---|
| 0.2 MPa | 16.5 L/min | 0.5 mg/L | ~90% | 模型 15 L/min × CaSO₃ ≥95% 段 → 97.15% |
| 0.3 MPa | 21 L/min | 0.7 mg/L | ~86% | 模型 20 L/min × CaSO₃ ≥95% 段 → 96.60% |
| 0.4 MPa | 27 L/min | 0.8 mg/L | ~84% | 模型 25 L/min × CaSO₃ ≥95% 段 → 96.30% |
| ~0.5 MPa | 30 L/min | 1.5 mg/L | ~70% | 模型 30 L/min × CaSO₃ ≥90% 段 → 92.10% |

### 读出来的几件事
1. **方向一致**：实测与模型都显示 "流速升高 → 去除率下降"，序号也一致
2. **绝对值偏低**：四个流速点上，实测均低于模型在 ≥95% CaSO₃ 段的预测值。两种可能——（a）输入 5 mg/L 本身在 Section 9 线性假设（1–2 ppm）的外推范围外，（b）被测滤芯非 fresh 状态。**未标注累计通水量，无法落到寿命曲线对应位置**
3. **27 → 30 L/min 斜率陡增**：实测下落 14 个百分点（84%→70%），模型只下落约 4 个（92.60%→92.10%）。有两种成因可能叠加——（a）EBCT 进一步缩短触及 breakthrough，（b）压力升到 ~0.5 MPa（与 2024-11-07 overflow envelope 起步压力重合）引起床压实 / 局部 channeling。复测需重点加密该段，并**分别控制压力与流速**以解耦两种成因

### 这份数据的已知限制
- 单次测量、无复测；4 个流速点各 1 个读数
- **测量方法为氯试纸比色法**（非 DPD / 仪表滴定）；典型刻度 0.5 / 1.0 / 1.5 mg/L，中间读数（0.7 / 0.8 mg/L）为内插，精度有限
- 水温、pH、TDS 未披露；Version A 基线 38–42°C，但本测试未标注
- 新旧滤芯状态未披露——无法把数据点放到寿命曲线对应位置
- 5 mg/L 高于寿命模型 2 ppm 基线（也高于 NSF 177 的 2 ppm 挑战浓度），属压力条件，**不能直接替换 Section 9 模型或用于 label claim**
- 与 Section 9 的差异属于 "方向性一致、幅度未定"，需第三方 DPD 法在 2 ppm 基线条件下复测以做定量校准

### 对 claim 语言的含义
- **可以暗示**（带条件）：Version A 在 US 典型龙头流速段（18–25 L/min）对自由氯有稳定的 >80% 去除能力
- **不能作为 label claim**：单次、非盲、试纸比色刻度粗、无累计通水量标注；任何 label-facing 数字仍需后续第三方 DPD 法复测或 Gold Seal 过程自带测试
- **可用作 internal alignment**：把 Section 9 推导出的寿命口径与实测做方向性闭环验证（在 2.5× 压力条件下仍保留 84–90% 量级 → 方向上不矛盾）

---

## Sources

**独立产品测试（比色法，非认证实验室）：**
1. [Best Bath Filters 2026 – Water Filter Guru](https://waterfilterguru.com/best-bath-filters/)
2. [Canopy Bath Tub Filter Review – Water Filter Guru](https://waterfilterguru.com/canopy-bath-tub-filter-review/)
3. [Sprite Bath Filter Review – Water Filter Guru](https://waterfilterguru.com/sprite-bath-filter-review/)
4. [Santevia Bath Filter Review – Water Filter Guru](https://waterfilterguru.com/santevia-bath-filter-review/)

**制造商技术文档（制造商二手数据）：**
5. [KDF Products – Kymera International](https://kdf.kymerainternational.com/products)
6. [KDF-55 Lab Test (Clack Corp) – Kymera International](https://kdf.kymerainternational.com/research/lab_clack)
7. [KDF Performance in Hot Water – Driplife Corp](https://driplifecorp.com/how-shower-filters-remove-chlorine-in-hot-water-conditions/)
8. [Sprite Chlorgon Filtration Technology](https://www.spriteshowers.com/knowledge-base/filtration-technology/)
9. [Calcium Sulfite and Water Filters – AquaBliss](https://aquabliss.com/blogs/healthy-water/calcium-sulfite-and-water-filters)
10. [Calcium Sulfite Balls – Onlyzonewater](https://www.onlyzonewater.com/Calcium-Sulfite-Balls-Revolutionizing-Water-Purification-Technology-A-New-Choice-for-Efficient-Chlorine-Removal-n.html)
11. [CaSO3 Ceramic Balls – Shandong Eternal World](https://www.eternalmineral.com/caso3-chlorine/dechlorination.html)

**NSF/ANSI 177 标准文件：**
12. [NSF/ANSI 177-2019 Preview – ANSI Webstore](https://webstore.ansi.org/standards/nsf/nsfansi1772019)
13. [NSF/ANSI 177 Level Playing Field Article – PM Magazine](https://www.pmmag.com/articles/87589-web-exclusive-br-nsf-ansi-standard-177-a-level-playing-field-for-shower-filter-claims)
14. [Why NSF/ANSI 177 Matters – JugFree](https://jugfree.com/why-nsf-ansi-standard-177-matters-for-your-home-water-system/)

**浴缸过滤器产品规格（滤芯寿命数据）：**
15. [Shower Filter Replacement Guide – JinkoFilter](https://jinkofilter.com/shower-filter-replacement-guide/)
16. [KDF-55 Shower Filter Lifespan Overview – AquaBliss](https://aquabliss.com/blogs/healthy-water/kdf-55-filters-kinetic-degradation-fluxion)
17. [Bath Bubble KDF Filter – Sante for Health](https://santeforhealth.com/products/bath-bubble-refillable-kdf-bathtub-filter)
18. [Water Filter Guru – Media Lifespan Comparison](https://waterfilterguru.com/best-bath-filters/)
