---
type: product
status: draft
owner: strategy
created: 2026-04-12
updated: 2026-09-06
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, research-coverage, gaps, workflow]
source_count: 0
review_cycle: monthly
verification_status: working
related:
  - ./bathtub-filter.md
  - ../../syntheses/bathtub-filter-research-map.md
  - ../../syntheses/bathtub-filter-brand-and-content-landscape.md
---
# 浴缸过滤器研究覆盖差距

## 当前状态速览（2026-09-06）

> 本节是唯一需要读的部分；下面的分层说明与批次记录是历史归档。

| 类别 | 项 | 状态 | 负责 |
|---|---|---|---|
| 硬卡点 | Gate 1 第三方 DPD（V1 配置 25 L/min 特征曲线） | spec 已按 BOM 更正，未送测 | 产品 |
| 硬卡点 | COGS / 渠道 margin 模型 | 部件 BOM 有，无单价 | 供应链 + finance |
| 硬卡点 | C3 认证 binding quote（NSF/WQA/IAPMO RFQ） | 未发 | 产品 |
| 工程复核 | KDF 仓装填高度 / 床层位移（D-10） | 待实测 | 工程 |
| 工程复核 | V1 配置溢流包络复测 | 待实测 | 工程 |
| 工程复核 | 动态挂重与挂点位移 | 待实测 | 工程 |
| 工程复核 | 在位滴干 30 天霉变观察 | 待观察 | 工程 |
| 工程复核 | 三个 O 圈线径 / 压缩量 | BOM 待确认 | 工程 |
| 决策 | D-09 refill 形态 / D-11 试纸量程 / D-12 订阅 LTV / D-13 性能锚点 / D-14 产品线节奏 / D-15 卡片进 BOM | open | 见 [[bathtub-filter-decision-register]] |
| 感知（新） | 感知策略：测什么 / 不测什么（TDS 选型作废、判据精度论证） | ✅ 决策可用 | 见 [[bathtub-filter-sensing-strategy]] |
| 感知（新） | App 功能规划（Web PWA 优先、试纸相机读数、可解释寿命） | 🟡 仅框架 | 见 [[bathtub-filter-app-functional-plan]]；**D-16 参比色卡已裁定进 BOM**，仅剩 D-11 阻塞 |
| 感知（新） | **参比色卡进包装 BOM（D-16）** | ✅ **已裁定 2026-09-06** | 转供应链执行：打样 + 目标机型实拍验证 + 与 D-15 合并刀模；**工艺规格见 [[bathtub-filter-decision-register]]** |
| 感知（新） | 手机比色读试纸准确度自建验证集 | ❌ 未做 | 决定进水读数能否进模型；产品 + 工程 |
| 感知（新） | 相机管线跨品类复用（spout 归类 / 地漏盖识别） | 🟡 已评估，不单独立项 | 见 [[us-eu-home-hardware-mass-customization-2026]] §9.6；等 L2 管线跑通后再评估 |
| 感知（新） | 样本盘硬件规格与 ODM 询价（流量+压差+温度, BLE） | ❌ 未做 | 工程 + 供应链 |
| 感知（新） | FCC Part 15 / UL / 电池运输认证 RFQ | ❌ 未发 | 建议与 C3 认证 RFQ 合并发；产品 |
| 内容 | site/ 326 个占位（法务 / 运营 / 供应链输入） | 见 [[bathtub-filter-site-placeholder-register-2026-09-06]] | 各负责方 |
| 归档 | 专利 7 份原件、BOM xlsx 未入 raw | 待用户提供 | strategy |
| 已关闭 | A 层评论量化、B 渠道、C/C1/C2/C4 合规、F 水质辖区、G IP、H 视觉结构、D 市场侧与 BOM 部件表、site/ 内容体系、三层营销模型与故事版 | ✅ | — |

## 为什么有这份页面
本页回答了一个实际问题：**现在涵盖了哪些类别的研究，以及可能仍然缺少哪些？**

## 到目前为止涵盖的研究层
### 1.学术/机构证据
覆盖足以支持：
- 水/皮肤/湿疹问题框架
- 硬水与氯的细微差别
- 游泳+湿疹解释层
- 证据访问审核
- 学术论文总汇见 [[bathtub-filter-academic-paper-research-summary]]（8 篇 peer-reviewed + 综述；总判断：**问题存在 ≫ 产品有效**，学术层是 claim guardrail 而非 launch proof）

### 2. 专利/技术路线图
覆盖足以支持：
- 路线分类
- 种子专利表格
- 早期的架构思考
- 初始可溶性介质/浴球/浴缸喷嘴路线区分

### 3.品牌/产品线勘察
现在部分涵盖：
- 精灵/淋浴过滤器原点扩展逻辑
- 水晶探索/沐浴球逻辑
- Santevia / 优质生活方式逻辑
- 婴儿/湿疹前向品牌姿势线索

### 4.内容生态系统
现在已按四层拆解，见 [[bathtub-filter-content-ecosystem-by-layer]]：
- 评论（review）发布者层 ✓（5 个 URL 已记录）
- 养育/生活方式层 ✓（5 个 URL 已记录）
- 经销商/博客层 ✓（6 个 URL，其中 2 个 WebFetch 过 verbatim）
- Reddit/社区信号层 ⚠️ 仅有 Reddit-adjacent surfaces（Inspire / Quora / Amazon Q&A），**Reddit 原帖仍是剩余 gap**——需要人工抽样 r/eczema / r/Parenting / r/beyondthebump / r/SkincareAddiction

## 可能缺失或仍然薄弱的层
### A. 市场评论（review）挖掘
还是很弱。

问题：
- 什么是重复的一星级和三星级投诉？
- 流量（flow）、配合、泄漏、滤芯（cartridge）寿命和过度宣称挫败感在哪里表格现得最多？
- 哪种细分语言与正面评价与退货（return）风险相关？

### B. 渠道/零售商格局
还是很弱。

问题：
- 这个类别真正存在于哪里：亚马逊、DTC、家得宝式公用事业零售、健康零售、婴儿零售？
- 哪些渠道支持优质定位与商品定位？

### C. 标准/认证/合规层
仍然薄弱且具有战略重要性。

问题：
- 合法引用了哪些标准？
- 品牌在哪些方面倾向于“经过测试”和“经过认证”的语言？
- 哪些宣称在美国/欧盟/日本表格面上存在风险？

### D. 定价/单位经济/更换逻辑
还是很弱。

问题：
- 滤芯（cartridge）节奏和经济性
- 利润结构与投诉风险
- 补充/消耗品逻辑对于品类吸引力是否是必要的

### E.安装/兼容性（compatibility）工程
还是很弱。

问题：
- 浴缸喷嘴安装类型
- 租户友好性与泄漏风险
- 架构填充速度权衡
- “适用于大多数浴缸”不再可信的断点

### F. 监管/水质管辖权的细微差别
还是很弱。

问题：
- 哪些当地水务实际情况真正改变了用户需求？
- 类别强度是否取决于氯/氯胺重市场、硬水市场或两者？

### G.竞争IP/品牌标记深度
还是很弱。

问题：
- 哪些领先品牌公开标记专利？
- 当前产品是否有实用专利、设计专利或主要是营销语言的支持？
- 是否有明显的受让人集群或许可线索？

### H.视觉营销/创意策略
大多失踪了。

问题：
- 哪些图像、故事前后或“婴儿沐浴仪式”视觉效果可以推动转化？
- 品牌如何在视觉上传达信任和柔和的信号？

## 当前推荐
所有三个层现在都在本主题的范围内。

### 第 1 层 — 最高优先级/已在进行中
1. 市场评论（review）
2. 标准/认证/合规性
3.品牌专利标记/IP深度

### 第 2 层 — 现已正式纳入
4.安装/兼容性（compatibility）工程
5. 定价/单位经济性/替换逻辑
6. 渠道/零售商格局

### 第 3 级 — 现已正式纳入
7. SNS/创作者/短篇话语
8.视觉营销/创意策略
9. 社区语言压缩和情感转换模式

## 覆盖状态深度审计（2026-04-17 重写）

> **重要修正：** 之前的版本把"页面存在"当作"已覆盖"。2026-04-17 深度审计按"能否真正用于产品决策"重新评级。
>
> 评级标准：
> - ✅ **决策可用**：现有页面足以驱动 KES 产品/工程/营销决策
> - 🟡 **仅框架**：分类正确但缺数据，做不出具体决策
> - 🔴 **stub/placeholder**：未真正覆盖
> - ❌ **未建/缺失**：表中引用但文件不存在，或根本没建

| 层                 | 对应页面                                                                                                                                      | 真实状态                                                                 | 缺口（用来卡住哪类决策）                                                                                                                                                                                                                                            |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A. 市场评论挖掘 | marketplace-negative-review-signals、review-patterns-and-return-risk、complaint-taxonomy-and-risk-by-route、competitor-review-corpus-2026-04、source-summary 逐条标签分析（2026-06-02） | ✅ 决策可用（评论 taxonomy）/ 🚫 退货率非公开补资料 | 2026-06-18：当前口径为 active 10 ASIN / 2562 条 Amazon 评论逐条标签证据链；Filterbaby `B0FNVDJRSQ` 已剔除（资料未保留在 repo，见 hub「已知缺口」）。含 1-2 星高杀伤投诉排序、QA 复核列、严重度/置信度。**口径修正：真实 SKU 退货率、退款原因、客服工单 / Brand Registry / DTC 后台数据属于平台或内部后台数据，不列入公开补资料任务；未来仅在拿到内部数据时追加。** |
| B. 渠道/零售商格局       | channel-positioning-table-v2、channel-admission-requirements                                                                               | 🟡→✅ 接近可决策                                                           | 2026-04-18 补：Canopy 多渠道定价反推 margin 结构、MOQ 估算、category reset 窗口、buyer 期望矩阵。**仍缺：真实 buyer outreach 结果（margin / promo cadence 非公开）**                                                                                                                       |
| C. NA 合规          | certification-and-testing-pathways、certification-authority-tiers-and-workflow、compliance-framework-and-evidence-boundaries                | ✅ 决策可用                                                               | 关键发现：NSF 177 不适用 spout-mount，需 NSF 42+61 路径。Action：实际 RFQ                                                                                                                                                                                               |
| C1. 跨辖区           | cross-jurisdiction-standards-map                                                                                                          | ✅ 决策可用                                                               | 缺 V1 是否进 EU/JP 的市场范围决策                                                                                                                                                                                                                                  |
| C2. 美国州/联邦副线      | us-state-federal-compliance-sidelines                                                                                                     | ✅ 决策可用                                                               | 缺：legal review 已对 KES 实际文案执行                                                                                                                                                                                                                            |
| C3. 认证成本/周期       | certification-cost-and-timeline-estimates                                                                                                 | 🟡→✅ 接近可决策                                                           | 2026-04-18 补：4 阶段合规时间表（Phase 0–3）、KES V1 最小可行路径（$7k–$22k）、认证路径 × 渠道门槛矩阵、Target 2027 RFQ 启动截止。**数字仍是 order-of-magnitude，binding quote 须实际 RFQ**                                                                                                          |
| C4. 平台 claim 审查   | marketplace-claim-policing-layer                                                                                                          | ✅ 决策可用                                                               | 缺：Amazon Seller Central 当前类目分配                                                                                                                                                                                                                          |
| D. 定价/单位经济        | pricing-refill-flow-fit-table-v2、competitor-pricing-and-kes-v1-price-recommendation、kes-v1-pricing-channel-launch-geo-subscription、v1-free-chlorine-removal-dimensions-materials | ✅ 决策可用（市场侧 + GTM）/ ✅ BOM 部件表 / 🟡 COGS 侧 | 2026-04-18：MSRP $59–$79 + refill $24–32 有市场依据；13 ASIN × 5 站点矩阵。2026-06-15：V1 GTM（单 SKU、DTC 首发、首发地理、订阅）已收敛。**2026-07-02：27 项 BOM（部件 / 尺寸 / 材质 / 水接触）已裁定为真理源，"全 BOM 待补"关闭；但表内无单价，COGS / 渠道 margin 模型仍缺（供应链 + finance 提供）** |
| E. 安装/兼容性         | compatibility-engineering-breakpoints、installation-risk-matrix-v2、supported-spout-matrix、kes-flat-strap-spout-fit-design-2026-06-03        | 🟡 partial-sample validated / broader test-pending                        | 2026-06-03 已补入 KES 扁硅胶挂带、中央提拉头挂孔、3M 贴挂钩、附赠的5孔总长124mm，宽20mm的扎带方案；墙距口径已修正为出水嘴中心到墙面 >=60 mm 是居中美观线，40-60 mm 可偏心使用，<40 mm 为理论极端。2026-06-17 已补 S-01 non-diverter 末端折弯位置周长 <=18 cm 的实测边界、2 组 RV / mobile-home center-set / valve-diverter faucet 正向适配样本，以及 freestanding tub filler 弧形/异型管非瀑布出水 2 kg 承重记录。freestanding waterfall / wide-body outlet 仍按 NO-GO 处理。**仍卡住：不同 spout 类型覆盖、动态注水稳定性、泄漏/溢流、流量冲击、滤材可见形态记录。** |
| F. 水质辖区           | water-jurisdiction-demand-map、kes-concept-brief-v1                                                                                        | ✅ 决策可用（NA scope 已声明）                                                 | 缺：top-50 metro 的 utility 消毒剂/硬度查表 → 见新增 [[bathtub-filter-utility-service-map-by-metro]]                                                                                                                                                                 |
| G. 竞争 IP / 品牌标记   | ip-depth-and-brand-marker-map、patent-table、filterbaby-patent-fto-analysis、kes-patent-19-281644-modular-terminal-water-treatment | ✅ 决策可用（含自有专利申请） | 2026-04-17 法律状态扫描：Sprite Chlorgon (`US5914043A` `US6056875A`) 2015 expired；`US6145670A` `US6096197A` 2012 lapsed。**KES 在经典 spout-mount + KDF/CaSO₃ 架构上 freedom-to-operate**。`US12534389B2` (FilterBaby) 到期 2044，skincare DTC 定位有 blocking risk。**2026-07-01：KES 自有申请 `19/281,644`（2025-07-26 提交，patent pending）已作为 primary source 入库，可对外写 "Patent pending"，禁写 "patented"** |
| H. 视觉营销/创意策略      | visual-merchandising-and-creative-strategy；sns-creator-and-visual-taxonomy；creative-test-brief                                            | 🟡→✅ 结构完整，无实测 creative                                               | 2026-04-18 补：竞品视觉坐标图、Amazon PDP 8 槽位蓝图、DTC hero 结构、TikTok 视频格式规范、视觉合规边界表。**仍缺：真实 A/B 测试结果（需 launch 后执行）**                                                                                                                                               |
| Tier 3 #9. 社区语言压缩 | （之前未列入表）                                                                                                                                  | ❌ 未建 → 已建 [[bathtub-filter-community-language-compression-patterns]] |                                                                                                                                                                                                                                                         |
| Reddit 原帖采样       | （第 4 节标 ⚠️）                                                                                                                               | ❌ 未做 → 已建 [[bathtub-filter-reddit-community-signal-sampling]]        |                                                                                                                                                                                                                                                         |

## 决策可用性总览

- **11 层 ✅ 可决策**：C / C1 / C2 / C4 / F / G / D（市场侧）/ A（pattern 层）/ B（接近）/ C3（接近）/ H（结构完整）
- **1 层 🟡 仍框架**：D（COGS / 渠道 margin 模型——供应链 + finance 提供；BOM 部件表已于 2026-07-02 关闭）
- **1 层 🟡 partial-sample validated / broader test-pending**：E（spout matrix）——2026-06-03 已补入 KES 扁硅胶挂带、中央提拉头挂孔、3M 贴挂钩、附赠的5孔总长124mm，宽20mm的扎带方案；墙距口径已修正为 >=60 mm 居中、40-60 mm 偏心可用、<40 mm 理论极端；2026-06-17 已有 S-01 non-diverter 周长边界实测记录、2 组 RV / mobile-home center-set / valve-diverter faucet 正向适配样本，以及 freestanding tub filler 非瀑布出水 2 kg 承重记录；仍必须用更多 spout 实物安装/动态注水/稳定性/泄漏/溢流测试关闭
- **3 项原本 ❌**：sns-creator / community-language / reddit-sampling——**2026-04-17 已补**
- **4 项 2026-04-18 升级**：B / C3 / H / A + complaint-taxonomy 重写——见下方批次记录

## 真正的产品开发卡点

**仍然卡住 KES go/no-go 的不是页面数量，而是：**

1. **A 层真实退货/售后数据**——评论语料与逐条标签证据链已补（active 10 ASIN / 2562 条，1-2 星高杀伤投诉排序已完成）；真实 SKU 退货率、退款原因、客服工单 / Brand Registry 数据属于非公开后台数据，**不作为公开补资料任务**
2. **C3 binding quote**——必须向 NSF/WQA/IAPMO 实际 RFQ 才能定预算（数量级已有，binding 价格未知）
3. **D 层 COGS 模型**——必须有 BOM 数据 + 渠道 margin 谈判结果才能验证 $59–79 MSRP 的利润可行性（MSRP 已建议，COGS 还缺）
4. **E 层实物拆解/物理测试证据**——2026-06-03 已补入 KES 扁挂带安装设计方案，并把墙距口径修正为出水嘴中心到墙面 >=60 mm 可居中、40-60 mm 可偏心使用、<40 mm 属理论极端；2026-06-17 已补入 S-01 non-diverter 末端折弯位置周长 <=18 cm 的实测边界、2 组 RV / mobile-home center-set / valve-diverter faucet 正向适配样本，以及 freestanding tub filler 弧形/异型管非瀑布出水 2 kg 承重记录；但这仍无法替代完整 V1 fit scope、动态注水稳定性、泄漏/溢流和滤材可见形态记录；“样品采购”不列入本轮补资料任务，若已有样品或人工记录，应补入开箱、结构、滤材可见形态、安装、包装文案、说明书和测试结果

**当前 active 卡点不是页面数量。** C3 binding quote、D 层 COGS/BOM、E 层实物拆解/测试记录仍需要外部询价、供应链或人工记录；A 层真实退货/售后数据只作为内部后台可选证据，不再作为公开补资料任务。把这些标作"已覆盖"是假阳性，会让 go/no-go 决策被错误的"完成度"信号误导。

## 2026-04-17 / 04-18 ops-platform 报告批次

> 来源：`kes-ops-platform` BA + Rainforest + Brave + SerpAPI 全量扫描，存入 `reports/bathtub_filter_2026-04-17` 和 `reports/bathtub_filter_2026-04-18`。

以下 gap 层状态因此批次更新：

| 层 | 更新前 | 更新后 | 说明 |
|---|---|---|---|
| A. 市场评论挖掘 | 🟡 仅框架 | 🟡 仅框架（历史状态） | 2026-04-18 Rainforest reviews 返回为空；**2026-06-18 当前口径已由 active 10 ASIN / 2562 条评论语料与逐条标签分析补上。** |
| B. 渠道/零售商格局 | 🟡 仅框架 | 🟡→✅ 接近可决策 | 确认 Canopy 多渠道：Target $69.99 / Sephora $89 / Babylist $89；Google Shopping 40 条价格带完整 |
| D. 定价/单位经济 | 🟡 仅框架 | ✅ 决策可用 | 13 ASIN 跨 5 站点价格矩阵、BSR、月销估算；2026-06-03 已将 Filterbaby 剔除出 bathtub 口径，bathtub active pricing 不再使用其 $113 / 1K+ 数据；Canopy $89 是当前 premium tub-spout 主要锚点 |
| F. 水质辖区 | ✅ | ✅ | 无变化 |
| 关键词 / BA | 🟡 推断 | ✅ 实测 | BA SFR 2026-03-22 窗口数据：`bathtub filter` 105,780；Canopy 垄断全词 Top-1 click share 14–76% |
| Google Trends | ❌ 未做 | ✅ 5 年数据 | 2026-03-29 历史峰 100/100（= 2022 峰值 11 倍）；2026-04-12 仍在 43/100 |
| 消费者声音 / Reddit | 🔴 间接 | 🟡 Brave snippet | Brave Search API 抓到 r/moderatelygranolamoms 等真实 verbatim；完整原帖采样仍待人工 |
| 产品维度分类 | ❌ 未做 | ✅ LLM 标注 | installation_type / housing_material / filtration_approach 三维度 × 13 ASIN |
| 跨站点覆盖 | ❌ 未做 | ✅ 完成 | US / CA / UK / DE / JP 5 市场覆盖矩阵（13 ASIN × 5 sites）|

### 此批次仍未解决的卡点（不变）

1. **Amazon review 原文 / 情感标签**——2026-06-18 当前口径已补入 active 10 ASIN / 2562 条评论语料与逐条标签证据链；真实退货率与售后原因属于非公开后台数据，不作为公开补资料任务
2. **C3 binding quote**——NSF/WQA/IAPMO 实际 RFQ 尚未执行
3. **D 层 COGS 模型**——BOM 数据 + 渠道 margin 表仍待供应链提供
4. **E 层实物拆解/物理测试记录**——KES 扁挂带方案已补；墙距口径已从 >=60 mm 硬边界修正为 >=60 mm 居中、40-60 mm 偏心可用、<40 mm 理论极端；仍需已有样品或人工记录关闭安装稳定性、泄漏/溢流、流量冲击和滤材可见形态；不列“样品采购”为本轮补资料任务

## 2026-04-17 桌面研究补足批次

新增以下 desk-research-fillable 页面（不替代上面四项 field-work 卡点，但把原本 ❌/🟡 的层向 ✅ 推进）：

1. [[bathtub-filter-reddit-community-signal-sampling]] — r/eczema、r/Parenting、r/beyondthebump、r/SkincareAddiction 真实采样
2. [[bathtub-filter-sns-creator-and-visual-taxonomy]] — TikTok/IG/YouTube 创作者地图 + 话语模式
3. [[bathtub-filter-community-language-compression-patterns]] — review + Reddit 原话压缩成 page/ad copy 模式
4. [[bathtub-filter-utility-service-map-by-metro]] — top-50 美国 metro 的消毒剂/硬度查表 → V1 launch 地理优先级

## 2026-04-18 三层补全批次

以下三层从 🟡 仅框架升级为"结构完整 / 接近可决策"：

| 层 | 文件 | 补入内容 |
|---|---|---|
| B. 渠道/零售商格局 | [[bathtub-filter-channel-admission-requirements]] §7 | Canopy 定价反推 margin 结构；各渠道 MOQ 估算；buyer 期望矩阵；category reset 时间窗口 |
| C3. 认证成本/周期 | [[bathtub-filter-certification-cost-and-timeline-estimates]] §九 | 4 阶段 GTM 联动合规时间表；Phase 1 最小可行路径（$7k–$22k）；认证路径 × 渠道门槛矩阵；Target RFQ 截止推算 |
| H. 视觉营销/创意策略 | [[bathtub-filter-visual-merchandising-and-creative-strategy]] §7–9 | 竞品视觉坐标图；Amazon PDP 8 槽位蓝图；DTC hero 页面组件；TikTok/Reels 视频格式规范；视觉合规边界表 |
| A. 市场评论挖掘（synthesis 层）| [[bathtub-filter-complaint-taxonomy-and-risk-by-route]]（全文重写）| 4 产品路线 × 10 投诉模式交叉矩阵；R3 spout-mount 路线防御优先级；退货率定性估算区间（R3 好设计目标 5–12%）；P0/P1 工程+文案双层行动清单 |
| D. 定价/单位经济（主表）| 审计表 D 行更新 | 从 🟡 修正为 ✅（市场侧）/ 🟡（COGS 侧），反映 competitor-pricing 文件已建 |

### 此批次仍未解决的卡点（不变）

1. **A 层量化数据**——Amazon review 逐条标签分析已补；return-risk 只能作为评论风险定性/排序，不再追补公开不可得的真实退货率
2. **C3 binding quote**——NSF/WQA/IAPMO 实际 RFQ（现有数字仍是 order-of-magnitude）
3. **D 层 COGS 模型**——BOM 数据 + 渠道 margin 实际谈判结果
4. **E 层物理测试**——KES 扁挂带方案和 40-60 mm 偏心安装口径已补；如已有样品或人工记录，再补开箱、结构、安装、泄漏/溢流、滤材可见形态和测试结果；不列“样品采购”任务
5. **H 层实测 creative**——A/B 测试结果（须 V1 launch 后执行 $3,200 baseline 实验）

## 2026-04-19 → 2026-05-18 桌面研究补足批次

> 来源：bulk wiki update（与 GEO/Rufus 研究包同批次并入）。本批次为**桌面研究深化，未解决任何 field-work 卡点**。2026-06-18 口径修正：A 层评论量化已由 active 10 ASIN / 2562 条逐条标签补上，Filterbaby `B0FNVDJRSQ` 已剔除；真实退货/售后数据移出公开补资料任务。剩余硬卡点为 C3 binding quote、D COGS/BOM、E 实物拆解/测试记录。

| 层 | 新增页面 | 补入内容 | 评级影响 |
|---|---|---|---|
| 学术/机构证据（§1） | [[bathtub-filter-academic-paper-research-summary]] + 8 篇论文摘要（Seki 2003 / Perkin 2016 / Engebretsen 2020 / Danby 2018 / Jabbar-Lopez 2022 / Lei 2025 / Bradshaw 2026 / Bergera 2025） | 学术栈结论收敛为"问题存在 ≫ 产品有效"；硬水线比泛氯线更厚；学术层定位为 claim guardrail | 强化 claim 纪律，**不升级任何功效宣称** |
| C2. 美国州/联邦合规 | [[bathtub-filter-california-prop65-investigation-and-response]] | Prop 65 清单波动性、safe-harbor 三条路线、典型 BOM 暴露工作假设、KES warning 应对策略 | C2 仍 ✅，Prop 65 维度补齐；**实际化学品测试 + legal review 仍待做** |
| 产品架构 / 技术 | [[bathtub-filter-kes-media-stack-options-by-water-type]]、[[bathtub-filter-point-of-use-hardness-softening-feasibility]] | 按水源类型（游离氯 / 氯胺 / 高铁井水）的滤材方案；就地软水可行性结论：紧凑挂式 bath-ball **无法真正软化硬水**，真实软化需小型可再生 canister | 杀掉"bath-ball 软化硬水"路线假设；与学术硬水线纪律一致 |
| E. 安装/兼容性（安全维度） | [[bathtub-filter-atmospheric-vacuum-breaker-avb]] | AVB / 防倒吸 / anti-siphon 设计 review 维度；明确"AVB 不能包装成过滤能力""防倒吸不替代兼容性工程" | 历史状态为 E 🔴；2026-06-03 后更新为 🟡 design-covered / test-pending，AVB 仍不解决 WS2 物理测试卡点 |
| B/D. 市场/关键词基线 | [[bathtub-filter-amazon-category-and-keyword-baseline]]、source-summary 10-ASIN 项目市场调查（2026-04-22） | Amazon 类目与关键词基线、10-ASIN 项目级市场调查 | B/D 市场侧加厚；**A 层 100+ verbatim NLP 已由 2026-06-18 当前口径的 2562 条逐条标签分析补上** |

### 此批次仍未解决的卡点（与前两批一致，不变）

1. **A 层量化数据**——100+ Amazon 评论直采 + NLP/标签频次已补，并由 2026-06-18 当前口径的 active 10 ASIN / 2562 条逐条标签补强；真实 SKU 退货率移出公开补资料任务
2. **C3 binding quote**——NSF/WQA/IAPMO 实际 RFQ
3. **D 层 COGS 模型**——BOM + 渠道 margin 实际谈判结果
4. **E 层物理测试**——扁硅胶挂带、中央提拉头挂孔、3M 贴挂钩、附赠的5孔总长124mm，宽20mm的扎带方案和 40-60 mm 偏心安装口径已补；S-01/S-02 已有部分正向实测记录，freestanding tub filler 非瀑布出水已有 2 kg 承重记录；spout 兼容性、动态注水、泄漏/溢流、滤材可见形态和安装稳定性仍需更多实物或人工记录；不列“样品采购”任务

**纪律提醒：** 本批次大量加厚了"问题侧"与"合规/架构纪律侧"证据，但 go/no-go 仍卡在外部询价、供应链数据、实物拆解/测试记录上。学术层深化反而进一步**收紧了 claim 边界**（问题存在 ≠ 产品有效），不应被误读成"功效已被证明"。

---

## 2026-06-02 Amazon 评论语料与逐条标签补全批次

> 来源：用户提供的 11 个 Excel 评论表，已归档到 `raw/products/bathtub-filter/2026-04-20-competitor-review-corpus/`，并生成 [[bathtub-filter-competitor-review-labeling-analysis-2026-06-02]]。

> 2026-06-18 口径修正：Filterbaby `B0FNVDJRSQ` 是 shower filter / showerhead inline 产品，已从 bathtub 语料剔除。其 99 条评论原文、客户图、scorecard 子集与 competitor brief **未保留在任何 repo**（源头为 ops-platform `dev_competitor_review` 库，可按需重新导出）；Filterbaby 品牌研究见 kenny-wiki `wiki/brand-studies/filterbaby-dtc-case-study.md` 与本 repo [[kes-shower-filter-positioning-patent-analysis]]。当前 bathtub-filter 评论语料为 active 10 ASIN / 2562 条；竞品、价格、安装对象、图评和 claim 准确率口径均为 10 个 ASIN。

| 层 | 更新前 | 更新后 | 说明 |
|---|---|---|---|
| A. 市场评论挖掘 | 🟡 直采评论 / NLP 待补 | ✅ 评论 taxonomy 决策可用 | active 10 ASIN / 2562 条评论逐条标签，1-2 星高杀伤投诉排序已生成；高星轻微吐槽已单独标记 |
| A. 退货率 / 售后 | ❌ 外部不可见 | 🚫 不作为公开补资料任务 | 真实 return rate、退款原因、客服工单只能来自 Amazon 后台 / Brand Registry / DTC 后台；不再列入“继续找资料”任务 |

本批次关闭了“100+ Amazon 评论直采 + NLP/标签频次”缺口；真实退货率/售后后台数据因不可公开获取，已移出补资料清单。

## 2026-06-02 补资料任务口径修正：退货率移出，样品采购移出

| 项目 | 处理 | 说明 |
|---|---|---|
| 真实 SKU 退货率、退款原因、客服工单、Brand Registry / DTC 后台数据 | 移出公开补资料任务 | 这些数据不靠网页获取；未来只有拿到内部后台数据时才追加为运营证据。 |
| 样品采购 | 移出本轮补资料任务 | 不再生成采购优先级或预算清单。 |
| 实物拆解/测试记录 | 保留为证据边界，不由网页代替 | KES 扁挂带适配方案已补入 [[bathtub-filter-kes-flat-strap-spout-fit-design-2026-06-03]]；墙距口径已修正为 >=60 mm 居中、40-60 mm 偏心可用、<40 mm 理论极端；若已有样品或人工记录，再补开箱、结构、滤材可见形态、安装方式、包装文案、说明书和测试方法。 |
| active bathtub 10 ASIN 公开竞品资料 | 保留为可补资料 | 原始 11 ASIN 中的 Filterbaby 已剔除；剩余 bathtub active 10 ASIN 的官方页、Amazon PDP、公开价格/销量信号、公开 claim、可见结构/安装线索可整理到 [[bathtub-filter-11-asin-public-competitor-evidence-2026-06-02]]。 |

## 2026-06-18 → 2026-07-02 V1 定义锁定批次

> 来源：`raw/products/bathtub-filter/2026-06-18-desktop-source-folder-import/`、`2026-06-18-competitor-listing-sales/`、`2026-06-30-zongli-antiscale-granule-hygiene-report.md`、`2026-07-01-patent-application-19-281644/`、`2026-07-02-v1-free-chlorine-removal-dimensions-materials/`。本批次为 **first-party 产品事实入库 + 内容体系建设**，属于把 wiki 从研究层推进到产品层，不新增 desk research。

| 层 | 更新前 | 更新后 | 说明 |
|---|---|---|---|
| D. BOM | 🟡 全 BOM 待补 | ✅ 部件表已裁定 | [[bathtub-filter-v1-free-chlorine-removal-dimensions-materials]]：27 项、24 确认 / 3 待确认；2026-07-02 裁定 KDF55 130g / CaSO₃ 110g、PET 滤棉、NBR O 圈、250 mL 浴盐仓；寿命模型连锁重算 ~21,550 L @2ppm。**COGS 仍 🟡**（表内无单价） |
| G. 自有 IP | ❌ 无自有专利记录 | ✅ primary source | [[bathtub-filter-kes-patent-19-281644-modular-terminal-water-treatment]]：patent pending；红线「专利宽 ≠ 营销宽」写入 claim register |
| C2. Prop 65 | 🟡 缺水接触 BOM | 🟡→✅ 输入齐 | 水接触部件全清单已有，可启动整机成分 / 暴露评估；**实际化学品测试 + legal review 仍待做** |
| 技术边界 | PFAS 仅在 Banned 区 | ✅ 工程口径闭环 | [[bathtub-filter-point-of-use-pfas-removal-feasibility]]：催化炭对 PFAS 无贡献；PFAS 归 RO / IX 路线，浴缸端不写 |
| 产品线 | A/B/C 三 SKU 假设 | ✅ 一壳体三配方 | 氯胺版（催化炭）与井水版 GO；不做软化，硬水只给阻垢剂选项（[[bathtub-filter-point-of-use-hardness-softening-feasibility]] §8） |
| 内容层（新） | ❌ 无自有站内容 | ✅ 53 页内容规格 | `site/` 目录，入口 [[bathtub-filter-kes-marketing-site-content-map]]；每条 claim 挂 🟢/🟡/🔴 证据标签；🟡 不上 Hub 首屏 |
| B/D. 竞品销量 | 2026-04 估算 | ✅ 2026-06 快照 | [[bathtub-filter-competitor-listing-sales-2026-06-18]]：10 ASIN 近 12 月 176,739 件 / $6.3M |

### 此批次后仍未解决的卡点（收敛为三项）

1. **Gate 1 第三方 DPD 去氯测试**——[[bathtub-filter-25lpm-dechlorination-bench-test-spec]] 已写，未执行；在此之前所有去氯率与寿命数字都是内部模型 / 内部比色，不得作 label claim。C3 binding quote 与之并行（NSF/WQA/IAPMO RFQ 未发）。
2. **COGS / 渠道 margin 模型**——BOM 部件表已有，缺单价、模具摊销、渠道 margin，MSRP $59–79 的利润可行性仍未验证。
3. **E 层实物安装 / 泄漏 / 溢流记录**——扁挂带、S-01 周长边界、RV center-set、freestanding 承重已有部分记录；仍需更多 spout 类型的动态注水与泄漏/溢流记录。不新开样品采购任务。

### 本次 lint 发现的结构性缺口（2026-09-05）

- 此前 8 个页面把 Filterbaby `B0FNVDJRSQ` 资料标记为"已迁到 `wiki/products/shower-filter/`"，经查 kes-wiki 与 kenny-wiki 均无该目录。**2026-09-05 已统一改口径**：已从 bathtub 语料剔除。其 99 条评论原文、客户图、scorecard 子集与 competitor brief **未保留在任何 repo**（源头为 ops-platform `dev_competitor_review` 库，可按需重新导出）；Filterbaby 品牌研究见 kenny-wiki `wiki/brand-studies/filterbaby-dtc-case-study.md` 与本 repo [[kes-shower-filter-positioning-patent-analysis]]。
- 已清理：`acf-supplier-research.md` 无 frontmatter重复副本已删；inbox 中 3 份已入库的 bathtub 文档已删；5 页补齐 frontmatter；3 页去除 UTF-8 BOM；3 处断链修复；~95 页补进 `index.md`。

### 2026-09-05 全链路审查（新增卡点）

[[bathtub-filter-v1-full-chain-critical-review-2026-09-05]] 对 BOM、寿命模型、台架 spec、包装、GTM、文案做了交叉核算，新增 5 项 P0：Gate 1 spec 配置过期（F1）、KDF 仓填充率约 36–44%（F3）、溢流包络来自非 V1 配置（F4）、试纸分辨率不支持三档触发（F6）、订阅节奏与寿命模型矛盾（M3）。这些在 Gate 1 送测前必须先关闭，否则测的不是出货配置。**同日处理**：桌面侧口径已全部改到 BOM 配置与可执行触发（详见审查页 §8）；仍开放 D-09 refill 形态、D-10 KDF 仓装填、D-11 试纸量程、D-12 订阅 LTV 重跑，以及 V1 溢流复测、在位滴干霉变观察两项内部测试。

### 2026-09-06 感知 / 智能化层（新建层）

> 来源：本批次为**内部推演 + 既有页面交叉核算**，无新 raw 材料。触发问题：「KES 能否 pivot 到 AI 驱动、且有硬件与数据积累的护城河」。

新建两页：[[bathtub-filter-sensing-strategy]]（感知策略）、[[bathtub-filter-app-functional-plan]]（App 功能规划）。

**核心结论（三条，均由既有页面数字推出）**

1. **TDS 传感器选型作废（化学错误，非成本问题）**。CaSO₃/KDF55 去氯会把硫酸根与锌离子溶进水里 → **过滤后 TDS 上升**；离子交换软化 Ca²⁺ ⇄ 2Na⁺ → **TDS 不变**。两条概念稿（[[hybrid-water-softener-design-2026]] §3.2、[[shower-stick-competitor-analysis-and-kes-product-line-transformation-2026-06]]）此前与 [[bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine]] §八「❌ 不用 TDS 笔」红线直接冲突，**已在两份原文就地标注作废**（软水机再生冲洗的电导率终点判据例外，该用法成立，已单独保留）。
2. **在线测出水不可行——判据精度问题，不是成本问题**。[[bathtub-filter-25lpm-dechlorination-bench-test-spec]] 的 ≥85% 阈值换算成出水浓度，「还能用 vs 该换了」只差 **0.1 mg/L**（1 ppm 城市 0.05），且基质含皂液体油、工况为一天 10 分钟干置 23 小时。所有消费级方法（目视试纸 / ORP / 便宜安培法）都够不着；且台架衰减曲线是 90→86→84→70% 的连续下降，**不存在可供报警的穿透阶跃**。→ 正解是**剂量积分**，不是在线测量。
3. **进水才是主误差项，且用已在包装里的试纸就能测**。整个寿命模型压在「进水 2 ppm」单一假设上；同一水务内真实龙头余氯可差数倍，**一户 0.8 vs 3.5 ppm 寿命差 4 倍**，且是系统性误差（整个 metro 档期一起偏）。进水场景待测 0.8–3.5 mg/L、基质干净、±0.3 够用 → 试纸/手机比色完全可行，**硬件成本 $0**。进水读数同时反哺 [[bathtub-filter-utility-service-map-by-metro]]，构成唯一有复利的那层。

**氯胺是另一个问题**：KES 实际 EBCT 0.48–0.95 s vs 除单氯胺所需 3–7 min，**差 2–3 个数量级 → inline 段对氯胺基本不做功**。失效模式是「这缸剂量够不够」而非滤芯寿命 → 做**剂量计算器**，不做传感器；且抗坏血酸干扰 DPD 比色，须并入台架验证。

**修正后方案**：① 进水试纸手机比色（$0，全量客户，P0）+ ② 流量计（剂量，样本盘）+ ③ 压差（抓沟流——剂量积分完全看不见的旁通失效，正对应台架 spec Q2 未决问题）。**装 500–1000 台样本盘而非全量**（unit BOM 须 <$15，电子件 $6–9 装不下；且 2562 条评论仅 29 条用过工具）。[[bathtub-filter-kes-patent-19-281644-modular-terminal-water-treatment]] 的 1/4 转扣+磁定位、1–100 模块、模块 3 已含「可选加热/UV」条款，**已为带电模块开好机械插槽与 FTO 掩护，V1 出货硬件不用改**。

**与既有卡点的接口**：App 的试纸相机读数直接卡在 **D-11 试纸量程**（且与 2026-09-05 审查的 **F6「试纸分辨率不支持三档触发」P0 同源——两者应合并决策**）与 **D-15 卡片进 BOM**（参比色卡是手机比色的前提）。

**一年期判据**：实测消耗模型对换芯时点的预测误差是否**显著优于** ZIP 分档 9/12 个月基线；不优于则关掉这条线。**最大排期风险是周期长达 9–12 个月 → 一个真值点要等一年**，这是"现在就起样本盘"的唯一理由。

**本批次未解决**：手机比色准确度无自建验证集；样本盘 ODM 未询价；FCC/UL 未 RFQ；样本盘是否作独立 SKU（$99–129）未决。

**同日追加（2026-09-06）**

- **D-16 参比色卡进包装 BOM — 已裁定**（用户）。解锁 App L2 全部功能，**MVP 仅剩 D-11 试纸量程一个硬阻塞**。⚠️ 该卡工艺约束严格（哑光禁覆亮膜 / 中性灰+白块 / DPD 色阶 / **批次码** / 防潮 / 可同框），做错任一条卡片照印但读数不可用且不报错——规格已写入 [[bathtub-filter-decision-register]]。**尚未进 [[bathtub-filter-v1-free-chlorine-removal-dimensions-materials]] 部件表**（该表源自最终版 xlsx，需供应链在下一版 BOM 增列）。
- **相机管线跨品类复用** —— 接入 [[us-eu-home-hardware-mass-customization-2026]]（该页 §9 由另一会话同日写入，覆盖同一批功能件 raw；本轮**未重复建页**，只补 §9.6 做接口）。该页 §9.5 #2 的未决卡点「拍照识别需参照物校准、未做原型」与本线 L2 手机读试纸**是同一条管线**：拍照 → 定位 → **对已知参照物标定** → 判读 → 拒答。**可迁移的是拍摄 UX 与坏图拒答逻辑（两条线共同的头号难点）；不可迁移的是判读物理**——试纸读准不证明螺孔距（1/4" 判别）能读准。**排序结论**：L2 先发且边际成本近零（色卡已进 BOM、随 V1 出货、有 DPD 真值），应由它先验证 UX 那一半风险，地漏识别复用其成果、不并行造两套；L2 若在拍摄 UX 上失败即为对该页 §9.4 切入点 #1 的**提前 kill signal**。⚠️ 但地漏识别发生在**购前**、用户手中无 KES 色卡（只能用硬币/银行卡，参照物不受控），这段风险 L2 验证不了，需单独原型。
- **浴缸滤芯自身的 spout 归类识别**：[[bathtub-filter-supported-spout-matrix]] S-01~S-08 购前拍照归类，标签可来自已有退货流。**诚实边界**：适配不是第一退货动因（整体无效 46.5% > 质量 19.5% > 绕流/溢流 19.0%），**不足以单独立项**，作 L2 跑通后的增量应用评估。

## 战略意义

话题不缺研究材料；V1 BOM、自有专利申请与内容体系也已入库。当前仍缺的是**Gate 1 第三方 DPD 测试、外部 RFQ、COGS / margin 模型、以及把扁挂带方案变成 supported / conditional / not-supported 的实物验证记录**。真实退货/售后后台数据不再作为公开补资料任务。

当前最大的风险不是"没有页面"，而是**把 🟡 当作 ✅** 进行决策。 此次重写确保 KES 团队后续看 gap doc 时，能区分"已经能决策了"和"还得做才能决策"。
