---
type: product
status: draft
owner: strategy
created: 2026-04-17
updated: 2026-04-17
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, compliance, us, california, prop65, fda, cpsc, ftc, state-law]
source_count: 10
review_cycle: monthly
verification_status: working
related:
  - ./bathtub-filter.md
  - ./bathtub-filter-certification-and-testing-pathways.md
  - ./bathtub-filter-certification-authority-tiers-and-workflow.md
  - ./bathtub-filter-compliance-framework-and-evidence-boundaries.md
  - ./bathtub-filter-cross-jurisdiction-standards-map.md
---
# 浴缸过滤器（bathtub filter）美国州级 / 联邦合规副线

## 为什么有这页
现有 C 层文档把北美认证体系（NSF / WQA / IAPMO）和广告监管（FTC）讲清了，但没有独立覆盖以下这组**法定合规门槛**：

- California Prop 65 和其他州级化学品披露法
- CPSC 消费品安全（尤其 baby / infant 语境）
- FDA：bath filter 什么时候会被推过 cosmetic / medical device 红线
- 州级消费者保护副线（NY / WA / ME / OR / MN）

这些不是"加分项"，而是**进入美国市场的事实门槛**，少一条都会出事。

## 一句话结论
> **NSF / WQA / IAPMO 是"让你显得专业"的正向路径；Prop 65 / CPSC / FDA 是"不做就会被下架 / 起诉"的底线路径。两条路径并行，但底线路径更便宜、犯错代价更高。**

---

## 一、California Prop 65（加州 1986 年 65 号提案）
### 1.1 机制
Prop 65（正式名 Safe Drinking Water and Toxic Enforcement Act of 1986）要求：
- 任何让加州居民暴露于 OEHHA 清单（目前约 900 余种化学品）中物质的产品
- 必须提供 **"clear and reasonable warning"**（明确且合理的警示）
- 除非暴露量低于 **"safe harbor level"**（NSRL / MADL）

### 1.2 对 bathtub filter 最相关的化学品
| 物质 | 为什么相关 | 在 bath filter 可能的来源 |
|---|---|---|
| 铅 Lead | Prop 65 最常见 target | 黄铜件、焊点、某些滤芯材料 |
| 邻苯二甲酸酯（DEHP / DBP / BBP / DIDP）| 软 PVC / 软管常见 | hose / seal / gasket |
| 双酚 A（BPA）| 某些塑料 | 塑料外壳 / fittings |
| NDMA（N-Nitrosodimethylamine）| 橡胶部件反应物 | rubber hoses / seals |
| 结晶二氧化硅 | 某些滤芯矿物介质粉尘 | 滤芯制造工序 |
| 镍 | 某些金属件 | metal fittings |

### 1.3 执法结构
- 加州总检察长 + 地方检察官
- **60-day notice 私人诉讼**（"bounty hunter" 机制）：任何公民可先发 60 天通知函，若被告 60 天内不和解可直接起诉
- 2023-2024 年间 Prop 65 和解金额行业常见在 $10k – $150k 不等，律师费通常另计

### 1.4 对 KES 的实务含义
- **不能依赖"我们有 NSF 372 lead-free 认证"就跳过 Prop 65**——372 是材料合规基线，Prop 65 要求的是 warning label，两套体系
- **标签语言要过律师审**：Prop 65 warning 有官方标准模板，自创表述被判不合规的案例很多
- **供应商合规 ≠ 自己合规**——最终责任在"把产品卖到加州的那一方"
- **默认假设要加 Prop 65 warning**，除非有第三方 XRF / ICP-MS 测试证明低于 safe harbor

### 1.5 典型出错方式
- Amazon listing 没加 Prop 65 warning → Seller Central 自动警示或被 takedown
- 包装加了但用了旧版（pre-2018 格式仍在用）
- 只测了滤芯介质、没测整机 leachate → 测试 scope 和实际暴露 scope 不匹配

---

## 二、其他州级化学品披露法
### 2.1 New York Child Safe Products Act
纽约州 2020 年起生效的 `Children's Safe Products Act`（NY CSPA）要求在"儿童使用产品"中披露若干 high-priority chemicals。bath filter 若标记"for babies / for children" 可能触发。

### 2.2 Washington State CSPA
华盛顿州 `Children's Safe Products Act`（RCW 70A.430）同样要求儿童产品化学品披露。

### 2.3 Maine LD 1503 / PFAS disclosure
缅因州 2021 年起实施的 PFAS 披露法（随后数次修订）要求销售含 intentionally added PFAS 的产品提交披露。某些 PFAS-targeting 滤材或涂层可能触发。

### 2.4 New Jersey / Oregon / Minnesota
均有各自程度的消费品化学品披露 / 限制法，细节各异。

### 2.5 对 KES 的实务含义
- **若路线包含 "baby-safe / infant bath / for children" 语言**，NY + WA 的儿童产品披露须单独评估
- **PFAS 相关表达要极其克制**：Maine 的披露义务即便不违法，也造成合规开销
- **州级差异会产生"多 SKU / 多 labeling" 需求**——对小批量品类是隐形成本

---

## 三、CPSC - 消费品安全委员会
### 3.1 一般消费品
bath filter 作为一般消费品，受 `Consumer Product Safety Act`（CPSA）覆盖。主要义务：
- `Section 15(b)`：发现产品可能造成伤害时 24 小时内上报
- `CPSIA` 合规（若涉及儿童产品）
- 召回执行配合

### 3.2 儿童产品专属义务
若 bath filter 被标记为"for children 12 years or younger / 婴儿 bath"：
- 触发 `CPSIA` 铅含量限制（总铅 ≤100 ppm）
- 需要 `Children's Product Certificate`（CPC）
- 需要 CPSC-accepted lab 的 third-party testing
- 永久追踪标签要求

**这是一个明显的阈值跳跃**：标 "baby bath" 就进入 CPSIA；不标就不进入。

### 3.3 对 KES 的实务含义
- **默认不要把产品标为 "for babies / for children"**——除非已经做好 CPSIA 合规
- **视觉营销里出现婴儿图片但包装不标 "for babies" 的法律判定是灰色的**——FTC / 州 AG 曾以"视觉暗示产品用于婴儿"为由要求合规
- **CPSC 的 Section 15(b) 上报义务是硬性的**——漏报罚款可达数百万美元

---

## 四、FDA - 什么时候 bath filter 跨进 FDA 管辖
### 4.1 默认：不归 FDA 管
单纯的水处理装置（非饮用水用）通常**不属于 FDA 管辖范围**。

### 4.2 会被推进 FDA 的触发条件
#### a) Cosmetic 触发
`FD&C Act §201(i)` 定义 cosmetic 为"施用于人体……用于清洁、美化、促进吸引力或改变外观"的物品。

- 若 bath filter 销售页宣称 "filtered bath water cleanses / softens / beautifies your skin"，产品本体仍是水过滤器，但**广告声明可能把产品的使用场景描述为化妆品**——FDA 执法的是**产品 - claim 组合**，不只是产品本身
- 更常见风险：销售页混入 bath additives / bath bombs 等 cosmetic 产品做 bundle

#### b) Medical device 触发
`FD&C Act §201(h)` 定义 medical device 为"用于诊断、治疗、缓解、处理、预防疾病"的物品。

**对 bath filter 最危险的 claim：**
- "treats eczema"
- "prevents atopic dermatitis"
- "relieves skin irritation from water"
- "helps with baby's skin condition"

一旦被 FDA 认定为 unapproved medical device，风险包括：
- Warning Letter（公开发布，经销商通常会下架）
- Seizure / injunction
- Recall
- Import refusal

#### c) Drug 触发（罕见但有案例）
若宣称 "detoxifies body through skin"，在极端案例里会被推进 drug 分类。

### 4.3 对 KES 的实务含义
- **"treats / prevents / cures / relieves + disease name" 几乎必然触发 FDA**
- **FDA 的 warning letter 记录是公开可查的**——competitor 分析时可看 `FDA Warning Letters database`
- **FDA 对 "water filter" 的执法密度低于保健品**，但一旦触发 warning letter，后续渠道清扫（Amazon / Target / Walmart）几乎必然跟进

---

## 五、FTC - 现有文档已覆盖（bath-specific 补充）
详见 [[bathtub-filter-certification-authority-tiers-and-workflow]] 第三节。本页只补 bath-specific 维度：

### 5.1 bath 专属易踩点
- **"clinically tested" without clinical trial record**——FTC substantiation 标准要求 "competent and reliable scientific evidence"
- **"dermatologist recommended" 需 survey / endorsement 基础**——FTC Endorsement Guides（2023 更新）对 material connection 披露要求更严
- **before / after 照片**——在 bath / 皮肤语境下很容易被判定为 health-outcome claim

---

## 六、KES 上市前副线合规清单
### 6.1 产品层
- [ ] 整机 XRF / ICP-MS 铅含量测试（不仅滤材，而是 leachate）
- [ ] 邻苯二甲酸酯含量确认（软管 / 密封件）
- [ ] BPA / NDMA 相关材料风险评估
- [ ] 若含介质：供应商 SDS + 成分声明
- [ ] PFAS free statement（如适用，且有测试支撑）

### 6.2 标签层
- [ ] Prop 65 warning label 正确版本（2018 后格式）
- [ ] 不标 "for babies / for children" 除非走 CPSIA
- [ ] 不使用 "treats / prevents / cures" + disease 语言
- [ ] 不使用 "FDA approved / EPA certified" 类伪权威
- [ ] 如有 endorsement，披露 material connection

### 6.3 渠道层
- [ ] Seller Central / Vendor Central 的 Prop 65 字段正确填
- [ ] 广告素材过一遍 FTC + Prop 65 双审
- [ ] 客服话术与页面 claim 一致（避免客服口头扩 claim）

### 6.4 文件留痕
- [ ] Section 15(b) 上报流程 + 责任人指定
- [ ] Substantiation file 每 claim 一档
- [ ] Supplier compliance certificates 存档

---

## 七、最常见的"不是认证没做好，是底线踩空"的出事模式
1. NSF 177 对位测试做了 → 包装没加 Prop 65 warning → 亚马逊被 takedown
2. 页面写 "dermatologist tested" → 没有测试记录 → FTC warning letter
3. 页面用婴儿图片 + "gentle for baby skin" → 没走 CPSIA → 州 AG 发函
4. 页面写 "helps eczema" → FDA warning letter → 所有大零售商同日清扫
5. 含 DEHP 软管但标 "BPA free" → 被诉 Prop 65 + 误导性宣称双起

## Obsidian links
- [[bathtub-filter]]
- [[bathtub-filter-cross-jurisdiction-standards-map]]
- [[bathtub-filter-certification-and-testing-pathways]]
- [[bathtub-filter-certification-authority-tiers-and-workflow]]
- [[bathtub-filter-compliance-framework-and-evidence-boundaries]]
- [[bathtub-filter-certification-cost-and-timeline-estimates]]
- [[bathtub-filter-marketplace-claim-policing-layer]]
- [[bathtub-filter-claim-risk-audit-v2]]

## Sources
- California Prop 65 OEHHA chemical list: <https://oehha.ca.gov/proposition-65/proposition-65-list>
- Prop 65 safe harbor levels (NSRL / MADL): <https://oehha.ca.gov/proposition-65/general-info/current-proposition-65-no-significant-risk-levels-nsrls-maximum>
- CPSC Consumer Product Safety Act: <https://www.cpsc.gov>
- CPSIA: <https://www.cpsc.gov/Regulations-Laws--Standards/Statutes/The-Consumer-Product-Safety-Improvement-Act>
- FDA FD&C Act §201: <https://www.fda.gov>
- FDA Warning Letters database: <https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/compliance-actions-and-activities/warning-letters>
- FTC Endorsement Guides (2023): <https://www.ftc.gov/legal-library/browse/rules/guides-concerning-use-endorsements-testimonials-advertising>
- NY CSPA: NY Environmental Conservation Law Article 37
- WA CSPA RCW 70A.430
- Maine PFAS disclosure LD 1503
