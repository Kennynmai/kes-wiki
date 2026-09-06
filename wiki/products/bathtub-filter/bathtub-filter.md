---
type: product
status: active
owner: product
created: 2026-04-11
updated: 2026-09-05
visibility: company
confidence: medium
officiality: draft
aliases: [浴缸过滤器, 泡澡过滤器, Bathtub Filter]
name_zh: 浴缸过滤器
name_en: Bathtub Filter
domain: product
domains: [bathtub-filter, water-filtration, bathroom, product-research]
source_count: 28
review_cycle: monthly
verification_status: working
related:
  - ./bathtub-filter-final-executive-summary-2026-04-14.md
  - ../../syntheses/bathtub-filter-research-map.md
  - ../../syntheses/bathtub-filter-competitor-and-demand-scan.md
  - ./bathtub-filter-user-segments.md
  - ./bathtub-filter-product-forms.md
  - ./bathtub-filter-technology-notes.md
  - ./bathtub-filter-atmospheric-vacuum-breaker-avb.md
  - ./bathtub-filter-chloramine-media-research.md
  - ./bathtub-filter-point-of-use-hardness-softening-feasibility.md
  - ./bathtub-filter-kes-media-stack-options-by-water-type.md
  - ./bathtub-filter-buying-criteria.md
  - ./bathtub-filter-claims-and-certifications.md
  - ./bathtub-filter-certification-and-testing-pathways.md
  - ./bathtub-filter-evidence-bibliography.md
  - ./bathtub-filter-academic-paper-research-summary.md
  - ./bathtub-filter-evidence-matrix.md
  - ./bathtub-filter-institutional-guidance.md
  - ./bathtub-filter-review-patterns-and-return-risk.md
  - ./bathtub-filter-competitor-review-corpus-2026-04.md
  - ./bathtub-filter-customer-water-quality-test-methods-2026-06-03.md
  - ./bathtub-filter-content-ecosystem-by-layer.md
  - ./bathtub-filter-2026-06-17-desktop-strategy-doc-import-index.md
  - ./bathtub-filter-kes-v1-execution-roadmap-2026-06-15.md
  - ./bathtub-filter-kes-v1-selling-points-and-pack-contents.md
  - ./bathtub-filter-kes-media-eeat-and-clean-formula-narrative.md
  - ./bathtub-filter-supplier-report-zongli-calcium-sulfite-chloramine-2023-07.md
  - ./bathtub-filter-kes-clean-formula-emotional-positioning.md
  - ./bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md
  - ./bathtub-filter-kes-acquisition-engine-mvp-spec.md
  - ./bathtub-filter-acf-supplier-research.md
  - ./bathtub-filter-north-america-special-water-sources.md
  - ./bathtub-filter-north-america-canada-asia-europe-water-report-2024-final.md
  - ./bathtub-filter-v1-full-chain-critical-review-2026-09-05.md
  - ./bathtub-filter-kes-patent-19-281644-modular-terminal-water-treatment.md
  - ./bathtub-filter-v1-free-chlorine-removal-dimensions-materials.md
  - ./bathtub-filter-kes-positioning-and-problem-layer-decision-2026-06-15.md
  - ./bathtub-filter-kes-v1-pricing-channel-launch-geo-subscription.md
  - ./bathtub-filter-25lpm-dechlorination-bench-test-spec.md
  - ./bathtub-filter-point-of-use-pfas-removal-feasibility.md
  - ./site/bathtub-filter-kes-marketing-site-content-map.md
  - ./bathtub-filter-2026-06-18-source-import-index.md
  - ../curtains.md
---

# 浴缸过滤器（Bathtub Filter）

## 页面定位
这是 bathtub filter 主题的 **canonical page（总页）**。

它的用途不是承载全部细节，而是回答三件事：
1. 这个品类到底在研究什么
2. KES 当前对这个品类的主判断是什么
3. 应该先看哪些页面，才能快速完成决策阅读

## 当前一句话结论（2026-09-05 刷新）
**这题已经从"desk research / go-no-go 评估"进入"V1 定义已锁、内容体系已建、等待物理验证与成本闭环"阶段。** 2026-07-02 之后的权威事实是：KES 自有专利申请 `19/281,644` 已提交（patent pending，未授权）；V1 除游离氯版 27 项 BOM 已裁定为全站真理源；自有营销站 53 页内容体系已按 claim 证据标签建好。**仍未闭环的只剩三件外部事**：Gate 1 第三方 DPD 去氯测试（25 L/min 特征曲线）、COGS / 渠道 margin 模型、更多 spout 实物安装与泄漏/溢流记录。desk research 不再扩写；Filterbaby `B0FNVDJRSQ` 已从 bathtub 语料剔除。其 99 条评论原文、客户图、scorecard 子集与 competitor brief **未保留在任何 repo**（源头为 ops-platform `dev_competitor_review` 库，可按需重新导出）；Filterbaby 品牌研究见 kenny-wiki `wiki/brand-studies/filterbaby-dtc-case-study.md` 与本 repo [[kes-shower-filter-positioning-patent-analysis]]。

> 历史口径（2026-06-24 前）："研究阶段已完成，可停止扩写；若推进，仅进入公开竞品资料补全、测试验证准备与概念收窄。" 该判断仍成立，只是后续工作已实际推进到 V1 定义与内容层。

## 范围与定义
这里的 bathtub filter，指用于 **浴缸注水 / 泡澡场景**、试图降低某些不希望出现的水中成分，或改善 bathing comfort（水感 / 气味 / 皮肤体感）的产品。

这个主题应与以下类别相关但分开处理：
- shower filters（淋浴过滤器）
- faucet filters（水龙头过滤器）
- whole-house filtration（全屋过滤）
- under-sink systems（台下系统）
- bath additives（非真正过滤逻辑的浴盐 / 添加剂 / bath treatment）

## 为什么值得研究
对 KES 来说，这个方向之所以值得看，不是因为它像一个普通五金件，而是因为它兼具：
- bathroom adjacency（浴室邻近品类）
- stronger problem language（更强的问题驱动叙事）
- premium storytelling potential（较强的高端叙事空间）
- refill / consumable logic（潜在耗材逻辑）

但它同时也带来更高门槛：
- trust burden（信任负担）
- claims risk（宣称风险）
- compatibility complexity（适配复杂度）
- review fragility（评论脆弱性）

## 当前最稳定的研究判断
### 1. 这是一个真实但碎片化的 niche
公开市场已经显示 bathtub filter 不是虚构需求。
但它仍然更像一个 **fragmented niche（碎片化小类目）**，而不是成熟、标准化、清晰分层的大类。

### 2. 问题故事强于功效证据
当前研究最清楚的一点是：
- 用户为什么会关心水质、氯、硬水、敏感肌、baby bathing，这个逻辑已经较为清楚
- 但 generic bathtub filters 是否真的在 realistic tub-fill conditions（真实浴缸注水条件）下稳定有效，仍缺硬验证

换句话说：
> **problem story is stronger than product-efficacy story**

### 3. 这个品类最大的风险是“高承诺、低验证”
目前市场上最容易出问题的地方，不是没人买，而是：
- overclaim（过度宣称）
- fit ambiguity（适配边界不清）
- normal-flow disappointment（正常流速下效果不及营销期待）
- leak / overflow / maintenance burden（漏水 / 溢流 / 维护负担）

### 4. 2026-06-02 / 2026-06-18 的 10-ASIN / 2562 条逐条标签分析进一步确认：评论风险已从“待量化”变成“可排序”
新增逐条标签证据链覆盖 Amazon US bathtub active 10 个 ASIN、2562 条评论。2026-06-18 已从 bathtub-filter 评论语料中删除 Filterbaby `B0FNVDJRSQ` 的 99 条评论，因为它属于 shower-filter / showerhead inline 产品；该 ASIN 已从 bathtub 语料剔除。其 99 条评论原文、客户图、scorecard 子集与 competitor brief **未保留在任何 repo**（源头为 ops-platform `dev_competitor_review` 库，可按需重新导出）；Filterbaby 品牌研究见 kenny-wiki `wiki/brand-studies/filterbaby-dtc-case-study.md` 与本 repo [[kes-shower-filter-positioning-patent-analysis]]。当前 bathtub-filter 竞品、价格、安装对象、图评和 claim 准确率口径均为 10 个 ASIN。该批证据把 2026-04-22 的 10-ASIN 项目级宽口径进一步收紧为可用于产品决策的标签口径。

稳定人群线索：
- 婴幼儿 / 儿童家庭：601 条（22.6%）
- 硬水 / 矿物残留困扰用户：556 条（20.9%）
- 敏感肌 / 干痒 / 湿疹困扰人群：524 条（19.7%）
- 氯味 / 泳池味困扰用户：479 条（18.0%）

主要购买动机：
- 改善泡澡后皮肤 / 头发体感：627 条（23.6%）
- 安装方便 / 挂上就能用：627 条（23.6%）
- 适合宝宝 / 敏感肌场景：625 条（23.5%）
- 缓解硬水导致的干涩 / 刺激感：550 条（20.7%）

1-2 星高杀伤投诉排序：
- 整体无效 / 不符合预期：191 条（占 1-2 星 46.5%）
- 质量破损 / 做工问题：80 条（19.5%）
- 绕流 / 溢流 / 过滤路径失效：78 条（19.0%）
- 敏感肌 / 宝宝场景效果不稳定：76 条（18.5%）
- 宣传口径争议（重金属 / TDS 等）：71 条（17.3%）

对应的判断修正：
- 旧的 50+ verbatim 和 10-ASIN 项目统计仍保留为历史证据，但当前评论风险排序以 [[bathtub-filter-competitor-review-labeling-analysis-2026-06-02]] 为准。
- “100+ Amazon 评论直采 / NLP 待做”已关闭；真实 SKU 退货率、退款原因和客服工单属于非公开后台数据，不再作为公开补资料任务。

## KES 当前建议姿态
### 可以继续
- concept narrowing（概念收窄）——2026-06-15 已收敛为「一个壳体三套配方」，见 [[bathtub-filter-kes-positioning-and-problem-layer-decision-2026-06-15]]
- validation testing（验证测试）——以 [[bathtub-filter-25lpm-dechlorination-bench-test-spec]] 为 Gate 1
- claim-boundary design（宣称边界设计）——以 [[bathtub-filter-claim-register]] 为唯一口径
- 已有样品 / 人工记录的实物拆解、安装与泄漏/溢流记录追加（不新开样品采购任务）

### 不建议继续
- 无上限追加 desk research 页面
- 在没有真实测试前写成 launch-ready 结论
- 走 aggressive eczema / baby-outcome claim route（激进湿疹 / 婴儿功效宣称路线）

## 当前最值得保留的路线
### 主保留路线
- **hybrid premium-but-disciplined route**  
  偏高端、但克制、适合 KES 做成 bathroom product language 的路线

- **narrow chlorine-focused / technically disciplined route**  
  以 chlorine reduction、适配边界、测试透明度为核心的技术克制路线

- **mid-price structural route / baby-safe solution route**  
  10-ASIN 的项目级评论与竞品分组补强了这两条路线：中价专业结构款与母婴安全方案款，是当前最值得继续拆解的两支

### 仅条件保留
- soft-hanging ritual route（偏柔和生活方式 / ritual 感的路线）

### 不建议作为主路线
- commodity broad-claim bath-ball clone（泛化大宣称 bath ball 路线）
- aggressive eczema / baby-outcome DTC route（激进湿疹 / 婴儿功效导向路线）

## 还没有真正闭环的关键问题
这几项如果不做实测，继续扩写 wiki 的价值会明显下降：
1. normal-flow proof（正常流速表现）
2. fit realism（适配边界）
3. leak / overflow / stability（漏水 / 溢流 / 稳定性）
4. refill economics（替换成本与频率）
5. claim boundary（不用夸大宣称时是否仍可转化）

## 当前推荐的正式表述
建议内部将这题定义为：

> **Bathtub filter 研究阶段已完成，V1（除游离氯版）产品定义与内容体系已建立；当前工作只剩三项外部闭环：第三方 DPD 去氯测试、COGS / margin 模型、spout 实物安装与泄漏/溢流记录。不再扩写 desk research，不新开样品采购任务。**

## 2026-06-18 → 2026-07-02 状态更新（V1 定义锁定批次）
这一批把 wiki 从"研究结论"推进到"产品事实"，以下页面是 **V1 的真理源（single source of truth）**，其他页面与之冲突时以这些页为准：

| 主题 | 真理源页面 | 关键事实 | 证据等级 |
|---|---|---|---|
| 自有专利 | [[bathtub-filter-kes-patent-19-281644-modular-terminal-water-treatment]] | 申请号 19/281,644，申请日 2025-07-26，Modular Terminal Water Treatment System；**patent pending，未授权**。红线：专利写得宽（软化 / 重金属 / UV / 护肤活性物）≠ V1 营销可以写宽 | primary-source-verified |
| V1 BOM | [[bathtub-filter-v1-free-chlorine-removal-dimensions-materials]] | 27 项部件（24 确认 / 3 待确认）；结构顺序 挂带 → 防溢水仓 → KDF55 仓 → CaSO₃ 仓 → 浴盐仓；**2026-07-02 裁定 KDF55 130g / CaSO₃ 110g、滤棉 PET、O 圈 NBR、浴盐仓 250 mL**；寿命模型连锁重算为 ~21,550 L @2ppm（soft ≈96 / mandatory ≈121 baths） | xlsx-imported；寿命数字仍是内部模型 🟡 |
| 定位与问题层 | [[bathtub-filter-kes-positioning-and-problem-layer-decision-2026-06-15]] | 游离氯城市为主战场；氯胺走双段式；井水 / RV 复用配方；首要价值「看得见·测得到的诚实过滤」 | working |
| V1 GTM | [[bathtub-filter-kes-v1-pricing-channel-launch-geo-subscription]] | 单 SKU、MSRP $59–79、DTC 首发 + Amazon 引流、首发地理 Las Vegas / Phoenix / San Antonio、90 天诚实订阅；**非 COGS 模型** | working |
| Gate 1 测试 | [[bathtub-filter-25lpm-dechlorination-bench-test-spec]] | 把 2026-03-20 内部比色单测硬化为第三方 DPD 特征曲线（去氯率 × 流量 × 压降 × 床体积） | spec，未执行 |
| 产品线决策 | [[bathtub-filter-kes-media-stack-options-by-water-type]]、[[bathtub-filter-point-of-use-hardness-softening-feasibility]]、[[bathtub-filter-point-of-use-pfas-removal-feasibility]] | 氯胺版（催化炭）与井水版 GO；**不做软化**，硬水只给阻垢剂选项；**PFAS 禁写**（催化炭对 PFAS 无贡献，浴缸端短 EBCT 是最差工况） | spot-checked / deep-research-verified |
| 卖点与套装 | [[bathtub-filter-kes-v1-selling-points-and-pack-contents]] | V1 = PET 滤棉 + KDF55 130g + CaSO₃ 110g；不含活性炭；不写氯胺去除 | working |
| 自有营销站内容体系 | [[bathtub-filter-kes-marketing-site-content-map]]（`site/` 目录 53 页入口） | Hub-and-Spoke IA，9 层（T/M/S/D/E/P/SVC/CH/OPS）；每条 claim 挂 🟢/🟡/🔴 证据标签；滤材页是唯一真理源，场景页只引用 | draft，内容先行 |
| 资料导入索引 | [[bathtub-filter-2026-06-17-desktop-strategy-doc-import-index]]、[[bathtub-filter-2026-06-18-source-import-index]] | 桌面策略文档 10 份、桌面源文件夹 42 份、10-ASIN listing + 销量包（近 12 月合计 176,739 件 / $6.3M） | source-index |

## 已知缺口（2026-09-05 lint）
- **全链路审查 5 项 P0 的桌面侧已处理（2026-09-05）**：Gate 1 spec 已改到 BOM 配置；35 L/min 溢流数字全站降 🟡；试纸触发改为可执行单触发；订阅周期改为按水型分档。**仍开放的是工程侧**：KDF 仓装填高度（D-10）、V1 溢流复测、在位滴干霉变观察、试纸量程（D-11）、refill 形态（D-09）。详见 [[bathtub-filter-v1-full-chain-critical-review-2026-09-05]] §8。
- **Filterbaby 剥离资料不在任何 repo（2026-09-05 已改口径）**：此前多页写"已迁到 `wiki/products/shower-filter/`"，经查 kes-wiki 与 kenny-wiki 及各自 git 历史都没有该目录。现统一口径为：已从 bathtub 语料剔除。其 99 条评论原文、客户图、scorecard 子集与 competitor brief **未保留在任何 repo**（源头为 ops-platform `dev_competitor_review` 库，可按需重新导出）；Filterbaby 品牌研究见 kenny-wiki `wiki/brand-studies/filterbaby-dtc-case-study.md` 与本 repo [[kes-shower-filter-positioning-patent-analysis]]。
- **COGS 仍缺**：BOM 已有部件 / 尺寸 / 材质，但没有单价与渠道 margin，D 层 COGS 侧仍 🟡。
- **寿命 / 去氯数字全部是内部模型或内部比色**：在 Gate 1 第三方 DPD 完成前不得作为 label claim。

## 2026-06-17 桌面资料导入批次
2026-06-17 已把桌面提供的 10 个 bathtub filter 策略 / 介质 / 水源 / 宣称资料文件导入 wiki，并在 raw 中保留原始文件与旧版备份。详见 [[bathtub-filter-2026-06-17-desktop-strategy-doc-import-index]]。

本批次对现有 wiki 的影响：
- 新增 V1 执行路线图、clean formula 情绪定位、media E-E-A-T 叙事、水诊断 kit、获客引擎 MVP、ACF 供应商、特殊水源和跨区域水质报告等页面。
- 升级 [[bathtub-filter-chloramine-media-research]]，补入 2026-06-15 TL;DR、KES V1 介质路线判断和混合 / 传质工程更新。
- 升级 [[bathtub-filter-claim-register]]，补入 2026-06-15 操作化增补 A-D，包括宣传语拆解、25 LPM test linkage 和 listing / website 口径。
- 没有发现完全重复可跳过的源文件；部分被导入文档内部引用的相关页面本批次未提供，暂保留引用，不凭标题补造。

## 建议阅读顺序
### 先看这几页
-1. [[bathtub-filter-v1-full-chain-critical-review-2026-09-05]]（2026-09-05 全链路批判审查：配置 / 参数 / 包装 / 营销 / 文案的交叉一致性问题与修复清单）
0. [[bathtub-filter-kes-patent-19-281644-modular-terminal-water-treatment]] 与 [[bathtub-filter-v1-free-chlorine-removal-dimensions-materials]]（V1 产品事实真理源）
1. [[bathtub-filter-kes-v1-execution-roadmap-2026-06-15]]
2. [[bathtub-filter-2026-06-17-desktop-strategy-doc-import-index]]
3. [[bathtub-filter-final-executive-summary-2026-04-14]]
4. [[bathtub-filter-competitor-review-labeling-analysis-2026-06-02]]
5. [[bathtub-filter-competitor-review-corpus-2026-04]]（legacy verbatim）
6. [[bathtub-filter-kes-go-no-go-memo-v1]]
7. [[bathtub-filter-kes-route-elimination-memo-v1]]
8. [[bathtub-filter-kes-concept-brief-v1]]
9. [[bathtub-filter-test-gating-checklist-for-kes]]
10. [[bathtub-filter-kes-rd-and-validation-roadmap]]

### 如果要继续做产品判断，再看
- [[bathtub-filter-kes-next-step-execution-plan-v1]]
- [[bathtub-filter-kes-media-eeat-and-clean-formula-narrative]]
- [[bathtub-filter-supplier-report-zongli-calcium-sulfite-chloramine-2023-07]]
- [[bathtub-filter-kes-clean-formula-emotional-positioning]]
- [[bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine]]
- [[bathtub-filter-kes-acquisition-engine-mvp-spec]]
- [[bathtub-filter-decision-register]] — 开放决策 × workstream 追踪
- [[bathtub-filter-assumption-register]] — 检查研究假设是否仍然成立
- [[bathtub-filter-normal-flow-vs-reduced-flow-evidence-table]]
- [[bathtub-filter-review-patterns-and-return-risk]]
- [[bathtub-filter-customer-water-quality-test-methods-2026-06-03]]
- [[bathtub-filter-competitor-review-labeling-analysis-2026-06-02]]
- [[bathtub-filter-competitor-review-corpus-2026-04]]（legacy verbatim）
- [[bathtub-filter-pricing-refill-flow-fit-table-v2]]
- [[bathtub-filter-installation-risk-matrix-v2]]
- [[bathtub-filter-claim-risk-audit-v2]]
- [[bathtub-filter-kes-product-architecture-hypotheses]]
- [[bathtub-filter-route-clusters-and-kes-opportunity-spaces]]

### 工程部件补充
- [[bathtub-filter-atmospheric-vacuum-breaker-avb]]：大气式真空破坏器 / AVB，作为 faucet / tub-spout 外接产品的防倒吸与 plumbing-safety 检查点。

## 主题导航
### 核心判断页
- [[bathtub-filter]]
- [[bathtub-filter-final-executive-summary-2026-04-14]]
- [[bathtub-filter-review-patterns-and-return-risk]]
- [[bathtub-filter-marketplace-negative-review-signals]]
- [[bathtub-filter-complaint-taxonomy-and-risk-by-route]]
- [[bathtub-filter-competitor-review-labeling-analysis-2026-06-02]]
- [[bathtub-filter-customer-water-quality-test-methods-2026-06-03]]
- [[bathtub-filter-kes-route-elimination-memo-v1]]
- [[bathtub-filter-kes-concept-brief-v1]]
- [[bathtub-filter-kes-next-step-execution-plan-v1]]
- [[bathtub-filter-test-gating-checklist-for-kes]]
- [[bathtub-filter-normal-flow-vs-reduced-flow-evidence-table]]
- [[bathtub-filter-review-and-compliance-landscape]]
- [[bathtub-filter-pricing-refill-flow-fit-table-v2]]
- [[bathtub-filter-installation-risk-matrix-v2]]
- [[bathtub-filter-compatibility-engineering-breakpoints]]
- [[bathtub-filter-atmospheric-vacuum-breaker-avb]]
- [[bathtub-filter-water-jurisdiction-demand-map]]
- [[bathtub-filter-ip-depth-and-brand-marker-map]]
- [[bathtub-filter-visual-merchandising-and-creative-strategy]]
- [[bathtub-filter-claim-risk-audit-v2]]
- [[bathtub-filter-compliance-framework-and-evidence-boundaries]]
- [[bathtub-filter-kes-go-no-go-memo-v1]]

### 执行追踪页
- [[bathtub-filter-2026-06-17-desktop-strategy-doc-import-index]]
- [[bathtub-filter-kes-v1-execution-roadmap-2026-06-15]]
- [[bathtub-filter-decision-register]]
- [[bathtub-filter-assumption-register]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-supported-spout-matrix]]

### 支撑研究页
- [[bathtub-filter-research-coverage-gaps]]
- [[bathtub-filter-kes-media-eeat-and-clean-formula-narrative]]
- [[bathtub-filter-kes-clean-formula-emotional-positioning]]
- [[bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine]]
- [[bathtub-filter-kes-acquisition-engine-mvp-spec]]
- [[bathtub-filter-acf-supplier-research]]
- [[bathtub-filter-north-america-special-water-sources]]
- [[bathtub-filter-north-america-canada-asia-europe-water-report-2024-final]]
- [[bathtub-filter-academic-paper-research-summary]]
- [[bathtub-filter-customer-water-quality-test-methods-2026-06-03]]
- [[bathtub-filter-claims-and-certifications]]
- [[bathtub-filter-certification-and-testing-pathways]]
- [[bathtub-filter-certification-authority-tiers-and-workflow]]
- [[bathtub-filter-compliance-framework-and-evidence-boundaries]]
- [[bathtub-filter-cross-jurisdiction-standards-map]]
- [[bathtub-filter-us-state-federal-compliance-sidelines]]
- [[bathtub-filter-california-prop65-investigation-and-response]]
- [[bathtub-filter-certification-cost-and-timeline-estimates]]
- [[bathtub-filter-marketplace-claim-policing-layer]]
- [[bathtub-filter-brand-operating-matrix-v2]]
- [[bathtub-filter-channel-positioning-table-v2]]
- [[bathtub-filter-kes-route-screening-memo-v2]]
- [[bathtub-filter-kes-product-architecture-hypotheses]]

### 研究模块
- 品牌与路线：[[bathtub-filter-brand-operating-matrix-v2]]
- 定价与单位经济：[[bathtub-filter-pricing-refill-flow-fit-table-v2]]
- 渠道与零售：[[bathtub-filter-channel-positioning-table-v2]]
- 安装与适配：[[bathtub-filter-installation-risk-matrix-v2]]
- 宣称与合规：[[bathtub-filter-claim-risk-audit-v2]]
- 内容与视觉：[[bathtub-filter-sns-creator-and-visual-taxonomy]]、[[bathtub-filter-visual-merchandising-and-creative-strategy]]

### V1 产品事实与 GTM（2026-06/07）
- [[bathtub-filter-kes-patent-19-281644-modular-terminal-water-treatment]]
- [[bathtub-filter-v1-free-chlorine-removal-dimensions-materials]]
- [[bathtub-filter-kes-positioning-and-problem-layer-decision-2026-06-15]]
- [[bathtub-filter-kes-v1-pricing-channel-launch-geo-subscription]]
- [[bathtub-filter-25lpm-dechlorination-bench-test-spec]]
- [[bathtub-filter-kes-v1-selling-points-and-pack-contents]]
- [[bathtub-filter-kes-website-copy-v1]]
- [[bathtub-filter-kes-homepage-and-about-page-layout]]
- [[bathtub-filter-kes-hero-film-storyboard-and-shooting-brief]]
- [[bathtub-filter-kes-transparent-box-hero-shot-script]]
- [[kes-bathtub-filter-PRD-v1]]
- [[bathtub-filter-kes-flat-strap-spout-fit-design-2026-06-03]]

### 自有营销站内容体系（`site/`，入口）
- [[bathtub-filter-kes-marketing-site-content-map]] — 总图与治理原则
- [[bathtub-filter-kes-content-ops-sop]] — 页面模板、claim 审批链、数字传播检查表
- [[bathtub-filter-kes-v1-definition-and-not-for-list]] — V1 定义与「不适合谁」清单
- [[bathtub-filter-kes-structure-overview]] / [[bathtub-filter-kes-structure-ip-and-patent-governance]]
- [[bathtub-filter-kes-page-how-we-test-and-certify]] / [[bathtub-filter-kes-page-replacement-and-lifespan]]
- 其余 media / scenario / edu / service / channel 页见内容地图与 `index.md` 的 `Marketing Site Content System` 小节

### 介质与技术补充
- [[bathtub-filter-media-efficacy-at-bath-conditions]]
- [[bathtub-filter-disinfectant-types-and-media-guide]]
- [[bathtub-filter-water-source-types-guide]]
- [[bathtub-filter-well-water-research]]
- [[bathtub-filter-utility-service-map-by-metro]]
- [[bathtub-filter-na-water-profile-and-target-market-analysis]]
- [[bathtub-filter-point-of-use-pfas-removal-feasibility]]
- [[ascorbate-chloramine-kinetics-research-2026-06]]
- [[bathtub-filter-market-size-and-demand-data]]
- [[bathtub-filter-amazon-category-and-keyword-baseline]]
- [[bathtub-filter-competitor-pricing-and-kes-v1-price-recommendation]]
- [[bathtub-filter-channel-admission-requirements]]

### 竞品情报（2026-06 批次）
- [[bathtub-filter-competitive-intelligence-filterbaby-bath-haus-2026-06-13]]
- [[bathtub-filter-filterbaby-deep-dive-patent-agency-awards-2026-06-13]]
- [[bathtub-filter-filterbaby-website-deconstruction-2026-06-13]]
- [[bathtub-filter-filterbaby-patent-fto-analysis]]
- [[envig-competitor-intelligence-2026-06]] / [[envig-deep-research-2026-06]]
- [[bathtub-filter-shower-bath-softener-competitive-landscape-2026-06]]
- [[bathtub-filter-certification-landscape-2026-06-13]]
- [[bathtub-filter-competitor-commercial-intelligence]]
- [[bathtub-filter-11-asin-public-competitor-evidence-2026-06-02]]
- [[bathtub-filter-competitor-claim-review-accuracy-scorecard-2026-06-02]]
- [[bathtub-filter-competitor-customer-installation-target-matrix-2026-06-02]]
- [[bathtub-filter-amazon-review-image-installation-packaging-leads-2026-06-02]]
- [[kes-bathtub-filter-critical-analysis-v1]] / [[kes-bathtub-filter-deep-competitive-analysis-v2]]
- [[bathtub-filter-standards-and-certification-audit-by-brand]]
- [[bathtub-filter-brand-page-claim-compliance-audit]] / [[bathtub-filter-brand-page-pack-audit-v2]]
- [[bathtub-filter-patent-table]]

### 内容、社区与创意补充
- [[bathtub-filter-reddit-community-signal-sampling]]
- [[bathtub-filter-community-language-compression-patterns]]
- [[bathtub-filter-creative-test-brief-and-creator-partnership-template]]
- [[bathtub-filter-product-definition-language]] / [[bathtub-filter-category-boundary]]

### 历史 / 归档
- [[bathtub-filter-kes-route-screening-memo-v1]]（archived）
- [[bathtub-filter-claim-evidence-ladder]]（archived，已并入 evidence-matrix）
- [[bathtub-filter-review-corpus-wiki-update-note-2026-04-20]]（archived 流程留痕）

### 来源摘要页
- [[bathtub-filter-competitor-listing-sales-2026-06-18]]
- [[bathtub-filter-competitor-review-labeling-analysis-2026-06-02]]
- [[bathtub-filter-amazon-10-asin-project-market-survey-2026-04-22]]
- [[bathtub-filter-marketplace-review-and-editorial-review-pass-2026-04-13]]
- [[bathtub-filter-market-scan-2026-04-11]]
- [[bathtub-filter-academic-and-institutional-evidence-2026-04-11]]
- [[bathtub-filter-api-backed-academic-and-patent-fetch-2026-04-12]]
- [[bathtub-filter-paper-seki-2003-bathing-water-chlorine-atopic-skin]]
- [[bathtub-filter-paper-perkin-2016-water-hardness-chlorine-early-life-ad]]
- [[bathtub-filter-paper-engebretsen-2020-water-hardness-meta-analysis]]
- [[bathtub-filter-paper-danby-2018-hard-water-surfactant-irritation]]
- [[bathtub-filter-paper-jabbar-lopez-2022-softer-pilot-rct]]
- [[bathtub-filter-paper-lei-2025-water-bathing-ad-review]]
- [[bathtub-filter-paper-bradshaw-2026-weekly-vs-daily-bathing-rct]]
- [[bathtub-filter-paper-bergera-2025-hard-vs-chlorinated-water-preprint]]

## Sources
- [Bathtub Filter 最终收尾摘要（2026-04-14）](./bathtub-filter-final-executive-summary-2026-04-14.md)
- [Bathtub Filter 学术论文研究总汇](./bathtub-filter-academic-paper-research-summary.md)
- [Bathtub Filter KES Go / No-Go Memo — V1](./bathtub-filter-kes-go-no-go-memo-v1.md)
- [Bathtub Filter KES Route Elimination Memo — V1](./bathtub-filter-kes-route-elimination-memo-v1.md)
- [Bathtub Filter KES Next-Step Execution Plan — V1](./bathtub-filter-kes-next-step-execution-plan-v1.md)
- [Bathtub Filter Test-Gating Checklist for KES](./bathtub-filter-test-gating-checklist-for-kes.md)
- [Bathtub Filter Review Patterns and Return Risk](./bathtub-filter-review-patterns-and-return-risk.md)
- [Bathtub Filter Competitor and Demand Scan](../../syntheses/bathtub-filter-competitor-and-demand-scan.md)
- [Bathtub Filter 2026-06-17 Desktop Strategy Doc Import Index](./bathtub-filter-2026-06-17-desktop-strategy-doc-import-index.md)
- [Bathtub Filter KES V1 Execution Roadmap 2026-06-15](./bathtub-filter-kes-v1-execution-roadmap-2026-06-15.md)
- [Bathtub Filter KES Media E-E-A-T and Clean Formula Narrative](./bathtub-filter-kes-media-eeat-and-clean-formula-narrative.md)
- [Bathtub Filter Supplier Report — Zongli Calcium Sulfite Chloramine Test 2023-07](./bathtub-filter-supplier-report-zongli-calcium-sulfite-chloramine-2023-07.md)
- [Bathtub Filter KES Clean Formula Emotional Positioning](./bathtub-filter-kes-clean-formula-emotional-positioning.md)
- [Bathtub Filter ACF Supplier Research](./bathtub-filter-acf-supplier-research.md)
- [Bathtub Filter Chloramine Media Research](./bathtub-filter-chloramine-media-research.md)
- [Bathtub Filter KES Water Diagnosis Kit and Modular Acquisition Engine](./bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md)
- [Bathtub Filter North America Special Water Sources](./bathtub-filter-north-america-special-water-sources.md)
- [Bathtub Filter KES Acquisition Engine MVP Spec](./bathtub-filter-kes-acquisition-engine-mvp-spec.md)
- [Bathtub Filter Claim Register](./bathtub-filter-claim-register.md)
- [Bathtub Filter North America / Canada / Asia / Europe Water Report 2024 Final](./bathtub-filter-north-america-canada-asia-europe-water-report-2024-final.md)
- [V1 全链路批判审查 2026-09-05](./bathtub-filter-v1-full-chain-critical-review-2026-09-05.md)
- [KES 专利申请 19/281,644](./bathtub-filter-kes-patent-19-281644-modular-terminal-water-treatment.md)
- [V1 除游离氯版尺寸与材质表（BOM）](./bathtub-filter-v1-free-chlorine-removal-dimensions-materials.md)
- [KES 定位与问题层决策 2026-06-15](./bathtub-filter-kes-positioning-and-problem-layer-decision-2026-06-15.md)
- [KES V1 定价 / 渠道 / 首发地理 / 订阅](./bathtub-filter-kes-v1-pricing-channel-launch-geo-subscription.md)
- [25 L/min 去氯特征测试 spec](./bathtub-filter-25lpm-dechlorination-bench-test-spec.md)
- [就地除 PFAS 可行性](./bathtub-filter-point-of-use-pfas-removal-feasibility.md)
- [自有营销站内容地图](./site/bathtub-filter-kes-marketing-site-content-map.md)
- [2026-06-18 资料写入索引](./bathtub-filter-2026-06-18-source-import-index.md)
