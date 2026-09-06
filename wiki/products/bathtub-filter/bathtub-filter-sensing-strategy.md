---
type: product
status: draft
owner: product
created: 2026-09-06
updated: 2026-09-06
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, sensing, sensor, iot, data, subscription, life-model, chloramine, instrumentation]
aliases: [传感策略, 水质传感, 智能模块, sensing strategy, smart module]
name_zh: 浴缸过滤器感知策略
name_en: Bathtub Filter Sensing Strategy
source_count: 6
review_cycle: quarterly
verification_status: working
related:
  - ./bathtub-filter-25lpm-dechlorination-bench-test-spec.md
  - ./bathtub-filter-chloramine-media-research.md
  - ./bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md
  - ./bathtub-filter-kes-patent-19-281644-modular-terminal-water-treatment.md
  - ./bathtub-filter-kes-v1-pricing-channel-launch-geo-subscription.md
  - ./bathtub-filter-v1-free-chlorine-removal-dimensions-materials.md
  - ./bathtub-filter-app-functional-plan.md
  - ../../market-research/hybrid-water-softener-design-2026.md
---

# KES Bathtub Filter · 感知策略（测什么 / 不测什么）

> **一句话**：**测进水，不测出水；测剂量，不测水质。**
> 判据精度决定一切——「还能用 vs 该换了」的差值落在 **0.1 mg/L**，低于任何消费级测量方法的分辨率；而进水浓度差 4 倍，是寿命模型的主误差项，用已经在包装里的试纸就能测。

> ⚠️ **本页推翻既有智能模块方案**：[hybrid-water-softener-design-2026](../../market-research/hybrid-water-softener-design-2026.md) §3.2 与淋浴棒方案选用的 **TDS 传感器测不出 KES 任何产品做的事**，该选型作废，理由见 §1。

---

## 一、为什么 TDS 选型必须作废（化学错误，非成本问题）

既有两份概念稿把 TDS 传感器当作水质感知核心。这在化学上不成立，而且**方向是反的**：

### 1.1 浴缸滤芯（V1 = KDF55 130 g + CaSO₃ 110 g）

| 反应 | 对 TDS 的影响 |
|---|---|
| CaSO₃ + HOCl → CaSO₄ + HCl | 亚硫酸钙把氯还原成氯离子，**同时把硫酸根溶进水里** → TDS **上升** |
| KDF55 铜锌氧化还原 | 释放锌离子 → TDS **上升** |
| 游离氯本身 2 ppm | 在 150–400 ppm 市政 TDS 背景里 = 噪声 |

→ **装 TDS 屏，会向用户显示"过滤后水变差了"。**

### 1.2 软水机（离子交换）

Ca²⁺ ⇄ 2Na⁺，溶解总量基本不变。[hybrid 稿](../../market-research/hybrid-water-softener-design-2026.md) 写的「出水硬度: 15 ppm ← TDS 传感器」**物理上读不出来**，软化后 TDS 仍在原量级。

### 1.3 全站口径本已划线，只是没打通

- [水质自测套件 §八](./bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md) 红线：**❌ 不用 TDS 笔**（测总溶解固体，非氯非硬度，常被用来伪精确恐吓）
- [客户测试方法分析](./bathtub-filter-customer-water-quality-test-methods-2026-06-03.md)：真实评论里 TDS/PPM 是最常见工具（14 条），**已标为反噬风险**——「我用 TDS 笔测了没变化」

**两份文档此前处于直接冲突状态。以本页为准：任何 KES 产品不得以 TDS 作为效果指示。**

---

## 二、核心论证：出水判据落在消费级方法的分辨率以下

### 2.1 判据换算

[台架 spec 判定阈值](./bathtub-filter-25lpm-dechlorination-bench-test-spec.md)：新芯 25 L/min、2 ppm 下 **≥85%** 去氯；寿命终点 ~2,945 L（110 g 口径）。换算成出水浓度：

| 状态 | 去氯率 | 进水 2 ppm → 出水 | 进水 1 ppm → 出水 |
|---|---|---|---|
| 良好 | 90% | 0.20 mg/L | 0.10 mg/L |
| 临界 | 85% | 0.30 mg/L | 0.15 mg/L |

**判别带宽 = 0.1 mg/L（1 ppm 城市仅 0.05），且基质含皂液、体油、沐浴露。**

### 2.2 方法分辨率对照

> ⚠️ 下表**成本与分辨率为通用工程估算，非 KES 实测**，属待工程复核项；结论方向（消费级方法够不着 0.1 mg/L 判别带）不依赖于精确数值。

| 方法 | 分辨率 | 成本 | 干湿循环工况 | 能否分辨 0.20 vs 0.30 |
|---|---|---|---|---|
| 目视试纸 | ±0.1–0.2，色带跳档 | ~$0.3 | 好 | ❌ |
| 手机比色读试纸 | ±0.05–0.1（清洁基质） | $0 | 好 | ⚠️ 边缘，皂液基质下不可靠 |
| ORP 电极 | 该区间仅差 10–20 mV | $15–40/支 | ❌ 参比结干裂 | ❌ 淹没在漂移/生物污损里 |
| 安培法电极 | ±0.02–0.05 | $150–400 | ❌ 不能干置 | ✅ 精度够，工况死 |
| 实验室 DPD 分光 | ±0.02–0.03 | $300+/台 | — | ✅ |

### 2.3 两条独立的死因

1. **精度**：判别带 0.1 mg/L 在消费级方法分辨率之下。
2. **工况**：浴缸滤芯是**一天用 10 分钟、23 小时干置**。所有电化学电极（ORP / 安培法）的参比结与电解液**不能干**，且浴水的皂液体油会快速污损电极。

### 2.4 并且没有"穿透断崖"这个大信号可抓

[台架 2026-03-20 单测](./bathtub-filter-25lpm-dechlorination-bench-test-spec.md)显示衰减是 **90% → 86% → 84% → 70%** 的连续曲线，加一个待复现的 27→30 L/min 断崖（且[已存疑](./bathtub-filter-25lpm-dechlorination-bench-test-spec.md)：单次无重复，可能是床压实/沟流而非真 breakthrough）。

**不存在 0 → 2 ppm 的阶跃信号。** 任何"靠检测突变来报警"的方案在此失效。

### 2.5 反向推论：终点观测不到，但可以积分到它

CaSO₃ 的氯容量是化学计量已知量，累计负荷是**单调良态量**。[寿命模型 21,550 L @2ppm](./bathtub-filter-v1-free-chlorine-removal-dimensions-materials.md) 本身就是一个剂量积分：

```
滤芯消耗 = ∫(流量 × 进水[Cl] × 温度修正) dt ÷ 容量
```

**剂量积分优于在线测量，不是退而求其次，是这个判据形态下的正解。**

---

## 三、进水是完全不同的问题，而且它是主误差项

### 3.1 为什么进水更重要

整个寿命模型压在**「进水 2 ppm」这一个假设**上。[台架 spec 自己标了这个风险](./bathtub-filter-25lpm-dechlorination-bench-test-spec.md)：「进水浓度 5 ppm，非北美真实龙头 1–2 ppm → 真实浓度下的去氯率与寿命会不同」。

真实龙头余氯在**同一水务内**即可差数倍：离厂距离、季节、水温、中途补氯站。而 CCR 是**年均值、按系统报、有滞后**。

> **一户实际是 0.8 还是 3.5 ppm，寿命差 4 倍。** 这比家庭用水量方差更致命——它是**系统性误差**，会让整个 metro 的订阅档期一起偏。

### 3.2 进水的测量条件好得多

| | 出水 | **进水** |
|---|---|---|
| 待测浓度 | 0.1–0.3 mg/L | **0.8–3.5 mg/L** |
| 需要分辨率 | ±0.05 | **±0.3 即够用** |
| 基质 | 皂液 / 体油 | **干净自来水** |
| 采样频率 | 需连续 | **一次性 + 每季一次** |
| 可行方法 | 实验室 DPD | **试纸即可；手机比色更准** |
| 硬件成本 | $150+ | **$0（试纸已在包装预算内）** |

### 3.3 进水读数同时喂两件事

1. **修正该户换芯档期**（订阅时点）
2. **★ 反向校正 [ZIP 水质图谱](./bathtub-filter-utility-service-map-by-metro.md)**——而该图谱正是[诊断获客引擎路径 A](./bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md) 的输入

第 2 条是复利层：**装机 → 校正水质图谱 → 诊断更准 → 转化更高 → 装机更多。**

### 3.4 手机比色是 AI 真正有位置的地方

拍照读试纸 + **画面内印刷色卡做白平衡校正**，需要解决：未知光源下的色彩恒常、试纸定位、色垫分割、对参比色块标定。这是有真实数据需求的 CV 问题。

- 目视试纸只能跳档读；机读可到 ±0.1 mg/L 量级（**待 KES 自行验证**）
- **不要求用户做新动作**——[「自己测、看得见」本就是核心定位](./bathtub-filter-kes-clean-formula-emotional-positioning.md)，这是把既有品牌动作做准

---

## 四、氯胺：问题结构不同，不要套用

### 4.1 硬约束：inline 段对氯胺基本不做功

| 项 | 值 | 来源 |
|---|---|---|
| 除单氯胺所需 EBCT | 催化炭 3–7 min / 标准 GAC ≥10 min | [氯胺证据页](./bathtub-filter-chloramine-media-research.md) |
| KES 实际 EBCT | **0.48–0.95 s**（15–30 L/min） | [产品架构假设](./bathtub-filter-kes-product-architecture-hypotheses.md) |

**差 2–3 个数量级。** 这正是 V1.5 必须走「缸内抗坏血酸钠浸泡 4–8 分钟」的原因。

### 4.2 三个后果

1. **失效模式变了**：不是滤芯耗尽，而是**这一缸水剂量够不够、泡够时间没有** → 感知目标是**验证单次剂量**，不是预测寿命。
2. **测量反而容易**：总氯 1.0 → <0.1 mg/L 是 **10 倍动态范围**，不是 0.2 vs 0.3。试纸/手机比色绰绰有余。
3. **但 DPD 被干扰**：[抗坏血酸作为还原剂会干扰比色读数、使"中和"被高估](./bathtub-filter-chloramine-media-research.md)（该页 §7 与 §测量要求已两次记录）。**这对任何比色法成立，含手机读**，须靠"按指引时机测"+ 扣空白解决，并列入台架验证项。

### 4.3 claim 约束继承

[「快速 / 秒解」是明确禁区](./bathtub-filter-chloramine-media-research.md)；AWWARF Portland 那条"亚分钟"有三条保留（管内接触时间未隔离 / 比色可能被干扰 / 单次未重复且与 Basu 2011 冲突）。**规划值仍以 SFPUC 4–8 分钟为准。** 任何 UI 计时器不得暗示秒解。

---

## 五、修正后的方案：三个感知手段，各补一个盲区

| 手段 | 测什么 | 补的盲区 | 成本 | 覆盖范围 |
|---|---|---|---|---|
| **① 进水试纸 + 手机比色** | 进水游离氯 / 总氯 | 剂量模型**主误差项**；校正 CCR | **$0** | **全量客户** |
| **② 流量计**（霍尔） | 累计过水量 | 家庭用量方差（假设 3 次/周 → 实测） | ~¥10–20 | 样本盘 |
| **③ 压差** | 床压实 / 沟流 | ★ **剂量模型完全看不见的物理旁通** | ~¥10–30 | 样本盘 |

### 5.1 为什么 ③ 不可替代

[台架 spec Q2](./bathtub-filter-25lpm-dechlorination-bench-test-spec.md) 明确在问「27→30 断崖是 breakthrough 还是床压实/沟流」。

**沟流是旁通失效——水没充分反应就过去了，但累计通水量一切正常，剂量模型对此完全失明。** 而沟流有清晰水力签名：同流量下 ΔP 低于预期。这也正是[专利 CaSO₃ 仓 6 分区防沟流结构](./bathtub-filter-kes-patent-19-281644-modular-terminal-water-treatment.md)需要现场验证的对象。

### 5.2 三者是互补，不是替代

**① 定标定（进水浓度） → ② 定进度（累计剂量） → ③ 抓异常（结构失效）。**
没有任何一项需要在线水质电极。

---

## 六、落地形态：装样本盘，不装全量

### 6.1 两条硬约束

| 约束 | 数据 | 来源 |
|---|---|---|
| **BOM 装不下** | unit BOM 须 **<$15** 才能保 wholesale 30% EBIT；流量+MCU+电池+BLE 小批量约 $6–9 | [定价页 §6](./bathtub-filter-kes-v1-pricing-channel-launch-geo-subscription.md) |
| **这个品类的人不测量** | 2562 条评论中仅 **29 条**用过任何工具；1562 条靠手感判断 | [客户测试方法分析](./bathtub-filter-customer-water-quality-test-methods-2026-06-03.md) |

→ 传感器**不能进主线机型**；App 依赖型智能设备在此品类 MAU 会很低；浴室里给 $69 配件配 2.4G WiFi 是退货率高发项。

### 6.2 设计取向

| | 不要 | 要 |
|---|---|---|
| 装机范围 | 全量出货 | **500–1000 台样本盘** |
| 传感对象 | TDS / 在线水质 | **流量 + 压差 + 温度** |
| 连接 | WiFi + 云 | **BLE 被动同步**（开 App 时） |
| 交付方式 | App 仪表盘 | **补货包按时出现在门口** |
| 用户动作 | 打开 App 看 | **零动作**（App 为可选增强） |

### 6.3 样本盘为什么就够

训练模型需要真值标签，而[验证试纸已在设计中](./bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md)（装芯前后、按配方分游离氯/总氯版）。样本盘产出带标签三元组：

```
(ZIP 水质, 实测流量曲线, 试纸观察到的穿透点)
```

拟合出消耗模型后，**对其余 100% 客户用 ZIP + 购买历史 + 家庭人数跑同一模型，一个传感器都不装。**

> **硬件在此的身份是训练集采集仪器，不是产品功能。** 这是唯一能同时满足 <$15 BOM 的版本。

### 6.4 专利已开好插槽

[19/281,644](./bathtub-filter-kes-patent-19-281644-modular-terminal-water-treatment.md)（2025-07-26 申请，pending）中三条直接支撑：

1. **1/4 转扣 + 磁定位、模块 1–100 可堆叠、变径连接环** → 传感器模块只是栈里多一节，**V1 出货硬件不用改**
2. **模块 3 权项已含「可选加热、可选 UV」** → 权利要求已涵盖**带电模块**，是带电模块的 FTO 掩护
3. **透明观察窗** → 「看得见」叙事的延伸，非另起炉灶

并天然支持**给已售用户加装**（磁吸 + 1/4 转，无工具）。

---

## 七、数据护城河：三层，越下越难抄

1. **家庭浴缸用水流量画像 × 地理** —— 水务公司只看到全屋总表，竞品什么都没有
2. **真实工况下的滤料穿透曲线** —— 间歇、干湿循环、40℃；[台架](./bathtub-filter-25lpm-dechlorination-bench-test-spec.md)是实验室条件，与现场不是一回事
3. **★ 用实测穿透点反向校正 CCR** —— 见 §3.3，唯一有复利的那层

> **诚实说明**：此处 AI 含量不高。消耗模型本质是带拟合系数的物理积分（回归，非 AI）。AI 真正有价值处：手机读试纸的色彩恒常（§3.4）、按户用量时序预测、跨同水务家庭分层池化校正 CCR、结合诊断问卷与退货文本预测 churn。**壁垒在数据集，不在算法。**

---

## 八、红线（继承全站 claim 纪律）

- ❌ **不得以 TDS 作为任何 KES 产品的效果指示**（§1）
- ❌ **不得声称在线检测水质 / 实时水质监测**（§2 判据精度不支持）
- ❌ 不得用感知数据做健康 / 皮肤功效声称（[claim-register](./bathtub-filter-claim-register.md) 禁区不变）
- ❌ 氯胺不得用「快速 / 秒解」措辞（§4.3）
- ❌ 试纸读数不得冒充实验室精度——**必须标注置信与量程**（继承[获客引擎 §二](./bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md)置信分层）
- ❌ 不做 toxin-panic 型推送

---

## 九、判据（一年后据此决定去留）

**主判据**：实测消耗模型对换芯时点的预测误差，是否**显著优于**「ZIP 分档 9/12 个月」基线。

- 优于 → 护城河成立，考虑扩样本盘 / 模型全量化
- 不优于 → 说明家庭方差小于预期，**关掉这条线**；该结论本身也值这笔钱

**次判据**：进水试纸读数对 CCR 的修正幅度（若普遍偏差 <±0.3 ppm，说明 CCR 够用，§3 的价值缩水）。

---

## 十、风险

| # | 风险 | 说明 |
|---|---|---|
| 1 | **周期长 = 迭代慢** | 9–12 个月才出一个真值点，模型需约一年现场数据才可信。**这是最大排期风险，也是"现在就起样本盘"的唯一理由** |
| 2 | 浴室带电 + 干湿循环 | 溅水区、IPX4 起步；本产品线[退货风险](./bathtub-filter-review-patterns-and-return-risk.md)本已紧 |
| 3 | 认证增量 | BLE = FCC Part 15 intentional radiator（约 $5–15k，**待 RFQ 确认**）；电池 + 涉水可能触发 UL 与运输要求 |
| 4 | 组织能力空白 | 全站无固件 / App / 云的团队或供应商记录。**但流量+BLE 数据记录器是成熟 ODM 品类**，样本盘阶段不需自建嵌入式团队 |
| 5 | 试纸读数完成率 | 品类不测量（§6.1）；若设置期完成率 <15%，§3 的全量覆盖假设不成立 |

---

## 下一步

- ⏳ **P0**：进水试纸手机比色 —— 零硬件、覆盖全量、修主误差项、可立即启动（不等硬件）→ 见 [App 功能规划](./bathtub-filter-app-functional-plan.md)
- ⏳ **P0**：把 [hybrid-softener 稿](../../market-research/hybrid-water-softener-design-2026.md) §3.2 TDS 选型标记作废（本页已同步该文件）
- ⏳ **P1**：样本盘硬件规格（流量 + 压差 + 温度，BLE，500–1000 台，首发三城）
- ⏳ **P1**：抗坏血酸对比色干扰的处理方法 → 并入[氯胺台架](./bathtub-filter-chloramine-media-research.md)验证项
- ⏳ **P2**：FCC/UL 认证 RFQ（与 [C3 认证 RFQ](./bathtub-filter-certification-cost-and-timeline-estimates.md) 合并发）
- 🔴 **待决策**：样本盘是否作为独立 SKU 售卖（$99–129 instrumented 版）vs 免费投放

---

## Sources / 内部依据

- [25L/min 去氯台架 spec](./bathtub-filter-25lpm-dechlorination-bench-test-spec.md) —— 判定阈值 ≥85%、衰减曲线、Q2 沟流问题、禁用目视比色作最终证据
- [V1 BOM 尺寸材质表](./bathtub-filter-v1-free-chlorine-removal-dimensions-materials.md) —— KDF55 130 g + CaSO₃ 110 g、21,550 L 寿命模型
- [氯胺介质研究](./bathtub-filter-chloramine-media-research.md) —— EBCT 3–7 min、抗坏血酸比色干扰、4–8 min 规划值、claim 禁区
- [水质自测套件 + 模块化获客引擎](./bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md) —— TDS 红线、置信分层、验证试纸设计、ITS OEM 路径
- [客户水质检测方法分析](./bathtub-filter-customer-water-quality-test-methods-2026-06-03.md) —— 29/2562 工具使用率、TDS 反噬风险
- [专利 19/281,644](./bathtub-filter-kes-patent-19-281644-modular-terminal-water-treatment.md) —— 模块化连接、可选加热/UV、6 分区防沟流
- [V1 定价/渠道/订阅](./bathtub-filter-kes-v1-pricing-channel-launch-geo-subscription.md) —— BOM <$15、9/12 月档期、1.3 次/年 refill

## Obsidian links

- [[bathtub-filter-25lpm-dechlorination-bench-test-spec]]
- [[bathtub-filter-chloramine-media-research]]
- [[bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine]]
- [[bathtub-filter-kes-patent-19-281644-modular-terminal-water-treatment]]
- [[bathtub-filter-kes-v1-pricing-channel-launch-geo-subscription]]
- [[bathtub-filter-v1-free-chlorine-removal-dimensions-materials]]
- [[bathtub-filter-customer-water-quality-test-methods-2026-06-03]]
- [[bathtub-filter-app-functional-plan]]
