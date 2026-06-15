# 产品需求文档（PRD）
## KES Bathtub Filter（浴缸过滤器）— Version A

---

## 文档信息

| 字段 | 内容 |
|------|------|
| **产品名称** | KES Bathtub Filter（浴缸过滤器）|
| **版本** | Version A（游离氯城市版）|
| **文档状态** | v1.1（已纳入 v2.1 竞品深度批判分析建议）|
| **更新日期** | 2026-06-15 |
| **基于报告** | `kes-bathtub-filter-deep-competitive-analysis-v2.md` |
| **负责人** | 产品策略 / KES 团队 |
| **Confidence** | 高（High）|
| **来源文件** | `~/dev/kes-wiki/wiki/products/bathtub-filter/` |

---

## 一、产品概述（Overview）

### 1.1 产品定位

KES Bathtub Filter 是**浴缸注水场景的末端减害模块**，不是全功能净水器。

> **核心定义（v1.1 更新）**：  
> 一种 **premium but disciplined**（高端但克制）的 bath-water comfort product，  
> 目标是在真实沐浴使用条件下，降低与 chlorine 相关的刺激负担，  
> 但不把自己包装成医疗解决方案，也不做宽泛的污染物结果承诺。
>
> **情感钩子（v1.1 新增）**：  
> "让你的浴缸水像 spa 一样温和"——在 disciplined 框架内增加情感共鸣，  
> 避免 FilterBaby 的高风险宣称（"改善湿疹"），但提升定位清晰度（5/10 → 8/10）。

### 1.2 产品形态

**龙头端内联过滤器（tub-spout inline）**

- 安装在浴缸龙头出水口
- 水在注水过程中穿过滤芯
- TPU 可调 strap 适配多种 tub-spout 类型

### 1.3 市场范围（V1）

| 范围 | 说明 |
|------|------|
| **主要目标** | 北美，free-chlorine 主导地区（CA、FL、TX、Southeast、Mountain West 的大部分区域）|
| **V1 明确不覆盖** | chloramine 为主的市场（Northeast US 部分地区、Chicago metro）；以及主要水质挑战为硬水而非氯的地区 |

### 1.4 价格策略（v1.1 新增）

> **基于竞品批判分析 v2.1 的建议 P0-2：明确价格策略，支撑营销叙事**

| 产品 | 价格 | 滤芯价格 | 滤芯寿命 | 年拥有成本 | 对标竞品 |
|------|------|---------|---------|------------|---------|
| **KES Bathtub Filter（本体）** | **$59.99** | — | — | — | Envig $59.99 |
| **KES 替换滤芯** | — | **$24.99** | 3 个月 / 30-40 次泡澡 | **~$100/年** | Envig $50.99/6个月 |

**价格叙事（v1.1 新增）**：

1. **"3× 滤芯寿命"** —— Frizzlife 滤芯仅 30 天，KES 为 3 个月（竞品对比图）
2. **"年拥有成本 $100，低于 Frizzlife 的 $323-$431"** —— 经济算账
3. **"NSF 认证材料（KDF55），非普通 PP 棉"** —— 技术价值解释

**价格测试策略（Launch 后 3 个月）**：

- 测试 $49.99 vs. $59.99 转化率
- 测试滤芯 $19.99 vs. $24.99 复购率
- 目标：本体毛利率 ≥60%，滤芯毛利率 ≥70%

---

## 二、用户研究（User Research）

### 2.1 目标用户细分

| 优先级 | 用户细分 | 需求强度 | 支付意愿 | 宣称风险 |
|--------|---------|---------|---------|---------|
| P0 | 有氯意识的沐浴者（chlorine-conscious bathers）| 中高 | 中 | 低 |
| P1 | 敏感肌肤/湿疹/干性肌肤使用者 | 高 | 高 | 高 |
| P2 | 家庭/婴儿沐浴场景 | 中 | 高 | 极高 |
| P3 | 硬水舒适寻求者 | 中 | 中 | 中高 |
| P4 | 健康/高端沐浴用户 | 低 | 高 | 低 |

### 2.2 核心用户旅程

```
感知氯气味 → 搜索解决方案 → 发现 KES Bathtub Filter 
→ 检查兼容性 → 购买 → 安装 → 首次使用（感知气味/体感变化）
→ 重复购买滤芯
```

### 2.3 用户购买标准（Buying Criteria）

1. **需求是否明确** — 搜索意图是否足够强且足够具体？
2. **宣称是否可信** — 不靠高风险医疗式措辞，产品故事还能不能成立？
3. **兼容性是否可解释** — 是否适配足够多的常见浴缸龙头？
4. **效果是否可感知** — 用户是否能感知到气味、体感或舒适度变化？
5. **换芯经济性是否成立** — 有没有合理、可解释的换芯逻辑？
6. **使用脆弱性是否过高** — 差评是否会集中在适配、漏水、慢流、没效果？
7. **是否适合 KES 当前能力** — 是否会引入明显超出当前能力的化学、测试或合规负担？

---

## 三、产品功能需求（Functional Requirements）

### 3.1 核心功能

| 功能编号 | 功能名称 | 描述 | 优先级 |
|---------|---------|------|---------|
| F-01 | 氯去除 | 系统总去氯 ≥99%（新滤芯，最佳体验段）| P0 |
| F-02 | 可更换滤芯 | replaceable filtration media | P0 |
| F-03 | 龙头兼容性 | TPU 可调 strap，适配多种 tub-spout | P0 |
| F-04 | 防溢水设计 | no-overflow envelope 35 L/min | P0 |
| F-05 | 导流模块 | 确保水真穿过滤材，避免 bypass | P0 |
| F-06 | 可视化滤芯 | 让用户看到滤芯在工作（**v1.1 升级：P1 → P0**）| **P0** |
| F-07 | 氯测试条赠品 | 让用户自验证效果（**v1.1 升级：P1 → P0**）| **P0** |
| F-08 | 兼容性预检工具 | 产品页内置工具，用户输入 tub-spout 类型，系统判断兼容性（**v1.1 新增**）| **P0** |

### 3.2 滤材栈（Media Stack）

**沿水流方向（顶 → 底）**：

```
PP fiber 盘（顶 2 张 + 底 1 张 mesh）
    ↓
optional loading cavity（240 mL，可选）
    ↓
KDF55 层（110 g，5–10 目，15 mm 高腔，60-mesh 304 网夹）
    ↓
CaSO₃ 层（130 g，3–4 mm 粒，15 mm 高腔，40-mesh 304 网夹）
    ↓
outlet mesh
```

**各层职责**：

| 层 | 角色 | 备注 |
|---|---|---|
| PP fiber | 截留颗粒 / 稳定水路 | 不是主 KPI |
| KDF55 | 末端安心层 / 生物膜抑制层 / 寿命稳定层 | 不再当主力去氯层 |
| CaSO₃ | **主力去游离氯 KPI** | 当前 Version A 的主 KPI 所在层 |

### 3.3 性能参数

| 参数 | 值 | 测试条件 |
|------|-----|---------|
| **系统总去氯率（新滤芯）** | ≥99% | 最佳体验段 |
| **系统总去氯率（压力条件）** | ~84–90% | 5 mg/L 进水，18–27 L/min |
| **EBCT（空床接触时间）** | 0.48–0.95 s | 15–30 L/min |
| **流量信封（no-overflow）** | 35 L/min | US 典型 18–25 L/min 有充足余量 |
| **滤芯寿命** | 按累计水量 / 泡澡次数 / 周期 | 不用月数 |
| **工作温度** | 38–42°C | 浴缸注水典型温度 |

### 3.4 兼容性需求

| 需求编号 | 描述 | 优先级 |
|---------|------|---------|
| C-01 | 支持主流直管龙头（straight spout）| P0 |
| C-02 | 支持 TPU 可调 strap 适配多种几何 | P0 |
| C-03 | 明确不支持列表（diverter / curved / decorative spout）| P0 |
| C-04 | 提供兼容性矩阵页面 | P1 |

---

## 四、非功能需求（Non-Functional Requirements）

### 4.1 性能需求

| 需求编号 | 描述 | 目标值 |
|---------|------|--------|
| NFR-01 | 去氯性能 | 新滤芯 ≥99%，寿命期内 ≥50% |
| NFR-02 | 流量保持 | 在 no-overflow envelope（35 L/min）内 |
| NFR-03 | 滤芯寿命 | 按累计水量标注，而非月数 |

### 4.2 可用性与用户体验

| 需求编号 | 描述 | 优先级 |
|---------|------|---------|
| UX-01 | tool-free 安装 | P0 |
| UX-02 | 换芯逻辑简单到支持重复购买 | P0 |
| UX-03 | 可视化滤芯（让用户看到工作）| P1 |
| UX-04 | 氯测试条赠品（让用户自验证）| P1 |

### 4.3 合规性需求（Compliance）

| 需求编号 | 描述 | 优先级 |
|---------|------|---------|
| CR-01 | KDF55 继承 NSF/ANSI 42 material-side | P0 |
| CR-02 | CaSO₃ 内部参照 NSF/ANSI 177 protocol 测试 | P1 |
| CR-03 | **成品本身不声称 NSF 认证** | P0 |
| CR-04 | 遵守 Claim Risk Audit v2 的禁用语言清单 | P0 |

### 4.4 宣称纪律（Claim Discipline）

#### ✅ KES 可以优先使用的语言

- chlorine-conscious bath-water comfort（氯意识型沐浴水舒适体验）
- 更温和的沐浴体验
- 为真实 bath use（沐浴使用场景）而设计
- 可更换过滤介质（replaceable filtration media）
- premium bath-time upgrade（高端沐浴升级）
- family bath-water comfort（家庭沐浴水舒适度）

#### ⚠️ KES 只有在证据足够强时才应使用的语言

- 在明确 stated conditions（声明条件）下，可减少 X% free chlorine
- 兼容这些特定 tub-spout formats（浴缸出水口类型）
- 在 realistic tub-fill conditions（真实浴缸注水条件）下完成测试

#### ❌ KES 应避免使用的语言

- improves eczema
- 对婴儿更安全，因为去除了有害化学物质
- 以临床相关方式 softens hard water
- 在缺乏明确技术路线证明时，声称去除大量污染物
- clinically proven skin improvement

### 4.5 用户满意度目标（v1.1 新增）

> **基于竞品批判分析 v2.1 的建议 P2-10：建立"用户满意度监控"机制**

| 指标 | 目标值（Launch 后 6 个月）| 测量方法 |
|------|---------------------------|---------|
| **Amazon/官网评价平均分** | ≥4.3/5 | 每月统计 |
| **正面评价占比** | ≥75% | 每月 sentiment 分析 |
| **负面评价核心痛点** | ≤2 个（且非兼容性或滤芯寿命）| 每月 thematic 分析 |
| **"效果不明显"抱怨占比** | <10% | 评价关键词统计 |
| **NPS（净推荐值）** | ≥40 | 季度问卷 |

**用户满意度提升措施**：

1. **量化效果图** —— 制作"滤芯颜色变化"图示（让用户直观看到滤芯在工作）
2. **氯测试条使用教程** —— 视频 + 图文，让用户自验证效果
3. **兼容性预检工具** —— 降低"买错"退货率
4. **滤芯寿命提醒** —— Email/SMS 提醒，降低"忘记换芯"抱怨

### 4.6 客服体验设计（v1.1 新增）

> **基于竞品批判分析 v2.1 的建议 P3-11：投资客服体验（参考 Frizzlife 教训）**

| 客服指标 | 目标值 | 参考竞品 |
|---------|--------|---------|
| **响应时间** | <24 小时（工作日）| Frizzlife 差评："客服联系不上" |
| **首次解决率** | ≥85% | — |
| **兼容性失败退货率** | <5% | 行业平均 ~8% |
| **滤芯寿命抱怨率** | <10% | Frizzlife 痛点："滤芯 30 天就坏" |

**客服体验设计措施**：

1. **"24 小时响应承诺"** —— 在产品页和包装上明示
2. **兼容性预检工具** —— 内置在产品页，用户输入 tub-spout 类型，系统判断兼容性
3. **"安装失败全额退款"政策** —— 降低购买顾虑
4. **滤芯寿命透明标注** —— 按累计水量（加仑）/ 泡澡次数 / 周期（不用月数）

---

### 5.1 系统架构

```
[浴缸龙头] 
    ↓
[TPU 可调 strap 接口]
    ↓
[外壳（no-overflow envelope 35 L/min）]
    ↓
[PP fiber 盘（顶 2 + 底 1）]
    ↓
[optional loading cavity（240 mL）]
    ↓
[KDF55 层（110 g）+ 导流模块]
    ↓
[CaSO₃ 层（130 g）+ 导流模块]  ← 主力去氯 KPI
    ↓
[outlet mesh]
    ↓
[浴缸]
```

### 5.2 关键技术参数

#### EBCT 与 KDF 去氯贡献（内部经验系数，38–42°C）

| 注水流速 | 单层 EBCT | KDF 去氯贡献 |
|---------|-------------|----------------|
| 15 L/min | 0.95 s | 43% |
| 20 L/min | 0.71 s | 32% |
| 25 L/min | 0.57 s | 26% |
| 30 L/min | 0.48 s | 21% |

**关键含义**：浴缸注水的 EBCT（<1 秒）对 KDF 来说太短，KDF 不可能做主力去氯。

#### 系统总去氯链式公式

> **总去氯 = 1 − (1 − KDF) × (1 − CaSO₃)**

| 注水流速 | CaSO₃ @ 99% 段 | CaSO₃ @ 95% 段 | CaSO₃ @ 90% 段 |
|---------|-------------------|-------------------|-------------------|
| 15 L/min | 99.43% | 97.15% | 94.30% |
| 20 L/min | 99.32% | 96.60% | 93.20% |
| 25 L/min | 99.26% | 96.30% | 92.60% |
| 30 L/min | 99.21% | 96.05% | 92.10% |

### 5.3 导流模块的必要性

- 在 **KDF 层**：有无导流无可见差异（KDF 粒大床密，抗冲刷）
- 在 **CaSO₃ 层**：**无导流时中心形成冲蚀 crater**；加导流后水流均匀铺开
- → 导流模块是 **CaSO₃ 层的 operational requirement**，不是可选项

### 5.4 活性碳选型

- 选择：**acid-washed coconut shell 8–10 目**（ash ≤0.5%，hardness ≥95%，iodine 1,000–1,200 mg/g）
- 验证：2-min pre-rinse 后，0.3 MPa / 29 L/min 穿 200 L 水已无粉末溢出
- → 可在 onboarding 写 "no pre-rinse required"

---

## 六、产品路线（Product Roadmap）

### 6.1 Version A（当前主线 — 游离氯城市版）

| 字段 | 内容 |
|------|------|
| **状态** | ✅ 已确认架构 |
| **目标水源** | US urban municipal tap water（free-chlorine）|
| **主媒体** | `PP fiber → KDF55 → CaSO₃` |
| **主 KPI** | free chlorine reduction |
| **主宣称方向** | `free chlorine reduction` / `bath-water comfort` / `less pool-smell bath fill` |
| **禁止宣称** | chloramine removal / hard-water softening / broad contaminant removal |

### 6.2 Version B（氯胺城市版 — P1 优先级）

> **v1.1 更新：基于竞品批判分析 v2.1 的建议 P1-7，将 Version B 从"待立项"升级到 P1 优先级**
> **依据**：Envig 专门主打氯胺市场，证明氯胺城市用户痛点更强（氯胺比游离氯更难去除，用户更绝望）

| 字段 | 内容 |
|------|------|
| **状态** | ⏳ P1 优先级（Launch 后 3 个月立项）|
| **目标水源** | chloramine-city bathers（Northeast US、Chicago metro）|
| **推荐结构** | inline bath-spout filter + 浴缸内浸泡配件（抗坏血酸钠 / 维生素 C）|
| **主媒体** | `PP fiber → catalytic activated carbon → small KDF55 layer` |
| **主 KPI** | chloramine reduction during fill + soak |
| **关键决策点** | 是否接受"滤芯 + 浸泡配件"双组件体验 |
| **市场验证** | Envig CloraClear 在氯胺市场成功（Amazon $59.99，催化碳技术是核心壁垒）|

### 6.3 Version C（私人井水版 — 待立项）

| 字段 | 内容 |
|------|------|
| **状态** | 🔄 候选路线（conditional）|
| **目标水源** | private well households with low-to-moderate iron / sulfur smell / rust nuisance |
| **主媒体** | `coarse PP sediment → KDF85 → catalytic carbon` |
| **主 KPI** | iron / H2S / odor relief |
| **关键决策点** | KDF85 供应与粒径是否稳定；高铁 / 高硫用户如何在前端就被排除 |

---

## 七、竞品分析（Competitive Analysis）

### 7.1 竞品对比矩阵

| 品牌 | 形态 | 主滤材 | 价格 | 核心优势 | 核心弱点 |
|------|------|-------|------|---------|---------|
| **Sprite** | inline | Cu+Zn + CaSO₃ | ~$30–50 | NSF 177 认证，品牌认知度高 | 滤芯寿命短（~22–25 次浴）|
| **Canopy** | inline | CaSO₃ + 炭 + KDF-55 | ~$60–80 | premium 设计，全渠道零售 | 快速流速下去除率低（50%）|
| **Santevia** | bath-ball | CaSO₃ + 炭 | ~$40–60 | 慢速流速下 100% 去除率 | 功效怀疑（bypass 嫌疑）|
| **Crystal Quest** | bath-ball | CaSO₃ + 炭 + KDF-55 | ~$50–70 | 广谱污染物宣称 | 快速流速下 0% 去除率 |
| **Tubo** | bath-ball | KDF + 未披露 | ~$80–100 | 8 阶段过滤宣称 | 缺乏透明技术解释 |
| **KES（目标）** | **inline** | **PP + KDF55 + CaSO₃** | **TBD** | **可视化滤芯 + 氯测试条赠品 +  disciplined claim** | **待验证** |

### 7.2 差异化机会

1. **可视化滤芯** — 让用户看到滤芯在工作（竞品无此设计）
2. **氯测试条赠品** — 让用户自验证效果（竞品无此配套）
3. ** disciplined claim** — 不做 broad-contaminant / eczema / baby-safe 类语言（竞品普遍过度宣称）
4. **寿命口径创新** — 按累计水量 / 泡澡次数 / 周期（不用月数）|

---

## 八、成功指标（Success Metrics）

### 8.1 产品指标

| 指标 | 目标值 | 测量方法 |
|------|--------|---------|
| **系统总去氯率（新滤芯）** | ≥99% | DPD 法 free chlorine in/out |
| **寿命期内去氯率** | ≥50% | DPD 法，累计水量终点 |
| **流量信封** | 35 L/min no-overflow | 压力-流量曲线测试 |
| **兼容性覆盖率** | >70% 主流 tub-spout | 兼容性矩阵测试 |

### 8.2 商业指标

| 指标 | 目标值（Launch 后 6 个月）| 测量方法 |
|------|---------------------------|---------|
| **官网转化率** | +50% vs. 品类平均 | Google Analytics |
| **复购率** | +50% vs. 品类平均 | 订阅数据 |
| **客单价** | +25% vs. 品类平均 | 销售数据 |
| **获客成本** | -20% vs. 品类平均 | Meta/Google Ads |
| **差评率** | <15% | Amazon / 官网评价 |

---

## 九、风险评估（Risk Assessment）

### 9.1 产品风险

| 风险 | 影响 | 概率 | 缓解措施 |
|------|------|------|---------|
| 兼容性失败 | 高（差评、退货）| 中 | 明确的兼容性矩阵 + 不支持列表 |
| 流量过慢 | 中（用户体验差）| 低 | no-overflow envelope 35 L/min 验证 |
| 滤芯寿命短于预期 | 高（复购信任崩溃）| 中 | 按累计水量标注 + 透明寿命模型 |
| 功效不可感知 | 中（价值失望）| 中 | 可视化滤芯 + 氯测试条赠品 |

### 9.2 合规风险

| 风险 | 影响 | 概率 | 缓解措施 |
|------|------|------|---------|
| 过度宣称（eczema / baby-safe）| 极高（监管、信任崩溃）| 中 | Claim Risk Audit v2 禁用语言清单 |
| 认证歧义（tested vs. certified）| 高（监管、评测反击）| 中 | 始终将测试与认证分开 |
| 广谱污染物宣称 | 高（监管、评测反击）| 高 | 禁用 broad-contaminant 语言 |

### 9.3 市场风险

| 风险 | 影响 | 概率 | 缓解措施 |
|------|------|------|---------|
| 品类定义白空间（无行业标准）| 中（用户认知成本高）| 高 | 清晰的产品定义语言 + 教育内容 |
| 竞品价格战 | 中（利润压缩）| 中 | premium 定位 + disciplined claim 差异化 |
| 用户期望管理失败 | 高（差评、退货）| 中 | 透明性能条件 + 不承诺 universal fit |

---

## 十、发布标准（Release Criteria）

### 10.1 必须通过的测试

| 测试编号 | 测试名称 | 通过标准 |
|---------|---------|---------|
| T-01 | DPD 法 free chlorine reduction | 新滤芯 ≥99%，寿命期内 ≥50% |
| T-02 | bath-fill flow envelope | 35 L/min no-overflow |
| T-03 | 寿命与 replacement trigger | 累计水量 / 泡澡次数 / 周期标注准确 |
| T-04 | supported spout compatibility | >70% 主流 tub-spout 通过 |
| T-05 | 导流模块验证 | CaSO₃ 层无冲蚀 crater |
| T-06 | 碳粉溢出验证 | 2-min pre-rinse 后无粉末 |
| T-07 | Claim Risk Audit | 100% 通过 v2 清单 |

### 10.2 必须完成的文档

| 文档编号 | 文档名称 | 状态 |
|---------|---------|------|
| D-01 | 产品定义语言（Product Definition Language）| ✅ 已完成 |
| D-02 | 兼容性矩阵（Compatibility Matrix）| ⏳ 待完成 |
| D-03 | 安装指南（Installation Guide）| ⏳ 待完成 |
| D-04 | Claim Register（允许/条件/禁用宣称清单）| ⏳ 待完成 |
| D-05 | Validation Checklist（必须过的测试清单）| ⏳ 待完成 |
| D-06 | Front-end Qualification Logic（让用户先判断水源类型）| ⏳ 待完成 |

---

## 十二、竞品批判分析改进建议（Actionable Insights from v2.1）

> **基于**: `kes-bathtub-filter-deep-competitive-analysis-v2.md`（v2.1 竞品深度对比与批判分析）
> **目标**: 将 12 条可执行建议整合进 PRD，指导产品定义改进

### 12.1 P0 — 立即执行（本周内）

| # | 建议 | 对应 PRD 章节 | 完成标准 | 参考竞品 |
|---|------|----------------|---------|---------|
| 1 | **增加情感钩子**（替换"末端减害模块"）| 一、1.1 产品定位 | 定位清晰度 5/10 → 8/10 | FilterBaby "We clean the water that cleans you" |
| 2 | **明确价格策略**（$59.99 + $24.99）| 一、1.4（v1.1 新增）| 价格策略文档完成 | Envig $59.99 |
| 3 | **升级可视化滤芯优先级**（P1 → P0）| 三、3.1 F-06 | 可视化滤芯设计完成 | — |
| 4 | **升级氯测试条赠品优先级**（P1 → P0）| 三、3.1 F-07 | 氯测试条供应商确认 | — |
| 5 | **增加兼容性预检工具** | 三、3.1 F-08（v1.1 新增）| 预检工具上线 | — |

### 12.2 P1 — 1 个月内执行

| # | 建议 | 对应 PRD 章节 | 完成标准 | 参考竞品 |
|---|------|----------------|---------|---------|
| 6 | **最大化技术权威叙事**（在 disciplined 框架内）| 四、4.4 宣称纪律 | 技术权威评分 6/10 → 8/10 | Waterdrop "NSF/ANSI 42 & 372 Certified" |
| 7 | **将 Version B（氯胺版）提升到 P1** | 六、6.2（v1.1 已更新）| Version B 立项文档完成 | Envig 氯胺市场成功 |
| 8 | **启动临床测试**（解决"效果不明显"抱怨）| 八、8.2 商业指标 | 临床测试方案确认 | Qure Skincare "7+ 临床研究" |

### 12.3 P2 — 3 个月内执行

| # | 建议 | 对应 PRD 章节 | 完成标准 | 参考竞品 |
|---|------|----------------|---------|---------|
| 9 | **制定全渠道策略图** | 一、1.3 市场范围（扩展）| 全渠道策略文档完成 | Brita Amazon + Target + Walmart |
| 10 | **建立用户满意度监控机制** | 四、4.5（v1.1 新增）| 满意度 dashboard 上线 | — |

### 12.4 P3 — 6 个月内执行（长期）

| # | 建议 | 对应 PRD 章节 | 完成标准 | 参考竞品 |
|---|------|----------------|---------|---------|
| 11 | **投资客服体验**（24 小时响应）| 四、4.6（v1.1 新增）| 客服响应 <24h | Frizzlife 反面教材（2/5 星）|
| 12 | **公示环保成就数字** | 七、7.2 差异化机会 | 环保数字公示在产品页 | Tapp Water "1.36 亿个塑料瓶" |

### 12.5 改进建议执行优先级排序

| 优先级 | 建议数 | 影响面 | 实现难度 | 预计完成 |
|---------|---------|---------|------------|----------|
| **P0** | 5 条 | 定位 + 价格 + 可感知效果 | 低-中 | 本周内 |
| **P1** | 3 条 | 技术权威 + Version B + 临床测试 | 中 | 1 个月 |
| **P2** | 2 条 | 全渠道 + 用户满意度 | 中-高 | 3 个月 |
| **P3** | 2 条 | 客服体验 + 环保成就 | 低-中 | 6 个月 |

**核心发现**：P0 建议全部与"可感知价值"相关——情感钩子、价格策略、可视化滤芯、兼容性预检，都是让用户"感知到价值"的设计。

---

## 十一、附录（Appendix）

### 11.1 相关文件清单

> **v1.1 更新**：新增 `kes-bathtub-filter-deep-competitive-analysis-v2.md` 和 `competitive-analysis-framework-v2.md`

| 文件 | 内容 |
|------|------|
| `bathtub-filter-product-definition-language.md` | 产品定义语言与表达边界 |
| `bathtub-filter-product-forms.md` | 产品形态分类与工程/支持影响 |
| `bathtub-filter-kes-concept-brief-v1.md` | KES 概念简报（Version A 已确认）|
| `bathtub-filter-kes-product-architecture-hypotheses.md` | KES 产品架构假设 |
| `bathtub-filter-kes-media-stack-options-by-water-type.md` | 三套水源型媒体方案 |
| `bathtub-filter-technology-notes.md` | 技术笔记（EBCT / KDF 系数）|
| `bathtub-filter-media-efficacy-at-bath-conditions.md` | 浴缸条件下滤材效能（含寿命表）|
| `bathtub-filter-claim-risk-audit-v2.md` | 宣称风险审核 |
| `bathtub-filter-buying-criteria.md` | 购买标准 |
| `bathtub-filter-user-segments.md` | 用户细分 |
| `deep-competitive-analysis-v2.md` | 竞品深度对比与批判分析（v2.1）|
| `competitive-analysis-framework-v2.md` | 竞品深度对比与批判分析框架（v2.0）|

### 11.2 变更日志

| 日期 | 版本 | 变更内容 | 作者 |
|------|------|---------|------|
| 2026-06-14 | v1.0 | 初始版本，基于 `~/dev/kes-wiki/` 研究整理 | AI |
| 2026-06-15 | v1.1 | 纳入 v2.1 竞品深度批判分析 12 条建议：新增价格策略(1.4)、用户满意度目标(4.5)、客服体验设计(4.6)、竞品改进建议(十二)；升级可视化滤芯/F-07 优先级(P1→P0)；升级 Version B 到 P1；新增 F-08 兼容性预检工具 | AI |

---

**文档结束**
