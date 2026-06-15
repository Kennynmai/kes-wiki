---
type: protocol
status: active
created: 2026-06-02
updated: 2026-06-02
tags: [content-marketing, workflow, production, youtube, pinterest]
domain: marketing
domains: [marketing, content, social-media, youtube, pinterest, keshome]
confidence: high
review_cycle: monthly
verification_status: spot-checked
related:
  - ../syntheses/keshome-youtube-pinterest-content-marketing-plan-2026-06.md
  - llm-product-market-research-for-kes-categories.md
  - ../source-summaries/building-a-storybrand.md
---

# 内容生产工作流协议（YouTube + Pinterest）

## Trigger / scope

每条 keshome 内容营销资产（YouTube 长视频/Shorts、Pinterest Pin）从选题到发布到复盘的标准流水线。把 KES 8 阶段工作流（Capture→Classify→Narrow→Extract→Deepen→Update→Verify→Lint）映射到内容生产。本协议是 ops-platform 内容营销引擎的**人类语义规格**——引擎的 ContentTemplate / brief output_schema / 复盘 verdict 应一一对应本协议的阶段产物。

不适用于：付费广告投放（另见 KPI/归因章节）、纯品牌 VI 设计。

## Inputs

- 选题来源：关键词矩阵（[keyword-tracker](../../dashboards/keyword-tracker.md) Tier 1/2/3）、竞争缺口、季节性日历
- 产品证据：产品规格、卖点、认证、载重/安装数据、竞品对比
- 框架：[StoryBrand](../source-summaries/building-a-storybrand.md) Hero→Problem→Guide→Plan→CTA、STEPPS、Cialdini 7 原则
- 模板：[content-brief](../../templates/content-brief.md)、[youtube-script](../../templates/youtube-script.md)、[pin-brief](../../templates/pin-brief.md)

## Steps

| KES 阶段 | 内容阶段 | 动作 | 产物 |
|---|---|---|---|
| **Capture** | 选题捕获 | 抓竞品/搜索/Trends 入 inbox | 候选选题 |
| **Classify** | 选题分类 | 按支柱(A-F)+平台+Tier 归类，登记 ingestion-registry | Brief 入库 |
| **Narrow** | 机会评分 | 7-axis 评分(搜索量/竞争/转化意图/复用度…)定优先级 | 优先级矩阵 |
| **Extract** | Brief 生成 | 填 17 字段 Brief Schema(关键词/角色/形态/CTA/落地页) | Content Brief |
| **Deepen** | 内容生产 | 拍摄/剪辑/Pin 设计；50/30/20 复用结构 | 成品素材 |
| **Update** | 发布 | 排期发布(YouTube Studio / Pinterest)；带 UTM+下级 URL+优惠码 | 已发布内容 |
| **Verify** | 质量审核 | 5 维 Rubric + **安全声明事实核查 gate(见 Failure modes)** | 审批通过/打回 |
| **Lint** | 绩效复盘 | 7/14/30 天复盘窗口；赢家加码/输家归档；更新策略 | 优化决策 |

### 周节奏（月度集中生产）
- W1 Brief Week：周一关键词研究+选题确认；周二三 Brief 生成；周四 Brief Review Gate；周五素材清单确认
- W2 Production Week：周一二集中拍摄(1 天产 1 月素材)；周三五剪辑/Pin 设计
- W3 Publishing Week：周一三 YouTube 发布；每日 Pinterest 5-10 Pin；每日 Shorts 1-2
- W4 Review Week：周一二指标采集；周三绩效报告；周四月度回顾→更新日历/KPI；周五下月选题

## Failure modes

- **安全声明合规风险（强制 gate）**：grab bar 是安全产品，涉及载重、安装方式、ADA 标准。LLM 生成的任何 brief/脚本/描述若含**未经核实的载重数据、安装建议、合规声明**，必须过事实核查 gate：人工核对引用 **ADA 标准 / UK Building Regulations**，禁止发布未经核实的安全承诺。误导性安装指导可导致消费者人身伤害 + 法律/监管 + 品牌声誉风险。此 gate 不可跳过。
- **复用过激被算法削弱**：单素材 Pinterest 超 3-5 Pin/月、同 URL 当天多发、re-pin 间隔 <2 天 → 触发低价值重复标记，分发骤降。坚持 50/30/20。
- **Shorts 当 evergreen 误用**：Shorts 是 recency-biased 推荐流，A 安装/B 对比走 long-form，不靠 Shorts 承载搜索意图。
- **归因黑洞**：仅靠 UTM 丢 20-40% 转化。每条内容必须配下级落地页 URL + 渠道优惠码 + 进 Post-Purchase Survey 选项。
- **Brief 与产品事实脱节**：Brief 必须从真实产品证据(规格/认证/测试)生成，不可凭空。素材主图必须真实产品照片(非 AI mockup，Pinterest 2025 AI 检测)。

## Review notes

- 本协议月度复审，随平台算法变化更新。
- 复盘 verdict（effective/ineffective/extend）应反哺策划——赢家内容形态的角色/形态组合在下轮选题中加权。
- ops-platform 落地时，本协议 8 阶段对应引擎的 step pipeline，Verify gate 对应发布审批，Lint 对应 7/14/30 复盘窗口。

## Related pages
- [keshome YouTube + Pinterest 内容营销实施计划](../syntheses/keshome-youtube-pinterest-content-marketing-plan-2026-06.md)
- [LLM 驱动的 KES 细分品类产品市场研究协议](llm-product-market-research-for-kes-categories.md)
- [Building a StoryBrand](../source-summaries/building-a-storybrand.md)
- 模板：[content-brief](../../templates/content-brief.md) · [youtube-script](../../templates/youtube-script.md) · [pin-brief](../../templates/pin-brief.md)

## Sources
- [原始资料 3 — KES 内容营销整合计划](../../raw/marketing/2026-06-02-kes-content-marketing-integrated-plan.md)
- [原始资料 5 — 内容营销计划审核报告](../../raw/marketing/2026-06-02-content-marketing-plan-audit.md)
