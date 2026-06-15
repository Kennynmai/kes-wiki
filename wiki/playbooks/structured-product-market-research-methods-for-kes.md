---
type: synthesis
status: active
created: 2026-05-08
updated: 2026-05-08
tags: [market-research, product-discovery, ai, llm, ecommerce, kes]
domain: product
domains: [product, market-research, ecommerce, ai, workflow]
source_count: 5
confidence: medium
review_cycle: quarterly
verification_status: spot-checked
related:
  - ../projects/kes-product-market-research-tooling.md
  - ../protocols/llm-product-market-research-for-kes-categories.md
  - ../topics/ai-agents.md
  - ../questions/电商页面图片生成与内容规划研究.md
---

# KES 结构化产品市场研究方法论

## Core thesis

KES 的产品市场研究流程不应该照搬咨询式市场报告，也不应该变成 LLM 自由发挥的“机会生成器”。更合适的结构是：

```text
市场研究严谨性 + 产品发现收敛性 + 电商运营证据 + KES 能力过滤 + 小实验验证
```

传统 market research 提供研究问题、样本、数据、分析和行动的纪律；Double Diamond 提供发散/收敛的节奏；JTBD 提醒不要只看人群画像，而要看客户在具体情境中要完成的任务；Opportunity Solution Tree 提供从业务目标到机会、方案、实验的可追溯链条。

对 KES 来说，关键不是“有没有完整市场认知”，而是能否把一个细分品类快速转成一组可验证的产品假设。

## Method map

### 1. 传统市场研究：保证研究可信

传统市场研究流程的价值在于防止研究变成随意观察。基本顺序是：
- 定义问题和研究目标。
- 设计研究方案。
- 选择样本。
- 收集信息和数据。
- 组织、分析、解释。
- 呈现结论。
- 做决策并采取行动。

它对 KES 的启发：
- 先把“想找机会”翻译成明确研究问题。
- 区分管理问题和研究问题。例如“这个品类能不能做”不是好问题；更好的问题是“这个价格带里，用户最不满意的任务失败点是什么，KES 有没有能力以可感知方式解决？”
- 区分探索性、描述性、因果性研究。早期不要假装能做因果判断，先做探索和描述；真正要判断转化/价格/包装影响时，再做实验。
- 同时使用 O-data 和 X-data：销量、广告、价格、排名是 O-data；评论、访谈、Q&A、客服反馈是 X-data。

### 2. Double Diamond：控制发散和收敛

Double Diamond 的四步是：
- `Discover`：广泛理解问题和用户。
- `Define`：把洞察收敛成清晰问题。
- `Develop`：生成多种解决方案。
- `Deliver`：小规模测试、淘汰、改进。

它对 KES 的启发：
- 前半段不能太早跳到产品方案，否则会变成“找理由支持已有想法”。
- 后半段不能停在洞察，要转成样品、页面 mock、BOM、供应商验证或小批量测试。
- 流程不是线性的。验证失败后要回到 Discover/Define，而不是强推原方案。

### 3. JTBD：把需求从“人群”改成“任务”

JTBD 的核心是：客户不是购买一个产品类别，而是在某个情境下“雇佣”一个产品完成任务。任务通常同时有功能、情绪和社会维度。

它对 KES 的启发：
- 不要只问“目标用户是谁”，要问“用户在什么情境下，需要完成什么任务？”
- 评论挖掘的核心不是情绪分类，而是找任务失败：安装失败、适配失败、清洁失败、安全感失败、审美失败、送礼失败、耐用性失败。
- 产品机会通常出现在“现有产品完成任务不稳定”的地方，而不是“竞品没有写某个卖点”的地方。

### 4. Opportunity Solution Tree：把机会和方案分开

Opportunity Solution Tree 的基本链条是：

```text
Outcome -> Opportunities -> Solutions -> Experiments
```

它对 KES 的启发：
- 顶层先定义业务结果，例如提高某类目新品成功率、提高毛利、降低退货、进入新价格带。
- 机会是用户需求、痛点、欲望或任务失败，不是产品方案。
- 一个机会下面必须生成多个方案，避免第一想法锁死。
- 每个方案都要拆成可测试假设，例如需求真实存在、用户能感知差异、供应链能做、页面能表达、毛利能成立。

### 5. Lean / experiment thinking：把研究压到可验证动作

产品研究最终要落到小实验，而不是更长报告。对 KES 来说，实验不一定是软件 A/B test，也可以是：
- 买 5 个竞品样品拆解。
- 找 3 个供应商确认工艺和 BOM。
- 做 2 版页面 mock 让运营/用户比较。
- 抓 500 条 review 验证痛点频率。
- 用广告搜索词验证需求语言。
- 做一个最小套装或配件组合测试。
- 小批量采购看退货/差评/转化。

## Recommended KES research flow

### Phase 0: Research brief

输出一个研究 brief：
- 品类和平台。
- 地区和价格带。
- 目标业务结果。
- 已知约束。
- KES 可用能力。
- 主要研究问题。
- 决策标准。

决策闸口：人确认这个问题值得研究，且边界足够窄。

### Phase 1: Category discovery

目标是建立品类地图：
- 子品类。
- 使用场景。
- 关键属性。
- 价格带。
- 替代方案。
- 购买/使用/安装/维护角色。
- 平台类目和搜索词。

LLM 适合做初版分类，但人要确认是否混入不同市场。

### Phase 2: Demand and job discovery

目标是建立 demand/JTBD map：
- 用户任务。
- 任务情境。
- 成功标准。
- 失败点。
- 购买前焦虑。
- 收货后失望。
- 功能、情绪、社会维度。

主要输入：
- reviews。
- Q&A。
- search terms。
- 客服/退货/差评。
- 用户访谈或运营经验。

输出必须保留证据片段，标注高频、强烈、低频高价值和推断。

### Phase 3: Competition and offer mapping

目标是建立竞品供给地图：
- 谁在卖。
- 卖什么形态。
- 价格/套装/变体。
- 页面怎么讲。
- 图片和 A+ 怎么表达。
- 好评来自哪里。
- 差评集中在哪里。
- 哪些卖点同质化。
- 哪些用户问题没有被结构性解决。

这里要区分三种缺口：
- `communication gap`：产品可能有，但页面没讲清。
- `configuration gap`：套装、规格、配件、说明不匹配。
- `product gap`：材料、结构、工艺、耐用性、安装体验本身有问题。

### Phase 4: Opportunity definition

把需求和供给缺口收敛成机会，而不是方案：
- 机会名称。
- 对应任务。
- 用户证据。
- 竞品供给缺口。
- 为什么现在没被解决。
- 可能的价值大小。
- 反证信号。

好机会应该是“用户任务失败 + 现有供给不足 + KES 有能力改进”的交集。

### Phase 5: KES fit filter

每个机会都要过 KES fit：
- 供应链是否可做。
- 工艺/材料是否熟悉。
- BOM 和物流是否可控。
- 是否能用现有内容系统表达。
- 是否适合 Amazon 页面竞争。
- 售后和退货风险是否可控。
- 变体复杂度是否可管理。
- 毛利是否支持测试和质量投入。

如果 KES fit 低，即使市场机会看起来大，也不应优先。

### Phase 6: Solution ideation

对每个通过过滤的机会生成多个方案：
- 产品结构改进。
- 配件/套装方案。
- 规格覆盖方案。
- 包装/说明书方案。
- 页面内容和图片表达方案。
- 定价/变体/组合方案。
- 供应链或 QC 方案。

这里要防止一个机会只对应一个方案。多个方案才能比较成本、差异感和验证速度。

### Phase 7: Assumption and risk mapping

每个方案拆成假设：
- 用户是否真的在意。
- 用户是否愿意为此付费。
- 用户是否能在页面上理解差异。
- 供应链是否稳定。
- 质量风险是否可控。
- 平台规则是否允许。
- 毛利是否成立。
- 竞品是否容易复制。

优先测试最危险、最便宜可测的假设。

### Phase 8: Validation plan

输出验证计划：
- 要验证什么假设。
- 用什么方法。
- 样本或数据来源。
- 负责人。
- 时间。
- 成本。
- 通过阈值。
- 失败后动作。

验证动作必须能在 1-4 周内产生下一步决策价值。

### Phase 9: Decision record

每轮研究结束必须留下决策记录：
- 继续。
- 暂停。
- 放弃。
- 回到前一阶段。
- 进入样品/供应商/页面 mock/小批量测试。

记录理由和证据，防止以后重复研究同一问题。

## Research methods by question

| Research question | Better methods | LLM role | Human role |
| --- | --- | --- | --- |
| 这个品类怎么分？ | desk research, category mapping, search term mapping | 初步分类、生成地图 | 确认边界是否正确 |
| 用户为什么买？ | JTBD interview, review mining, Q&A analysis | 抽取任务和情境 | 判断是否是真需求 |
| 用户哪里不满？ | review mining, return/customer-service data | 聚类痛点、保留证据 | 判断痛点价值和严重性 |
| 竞品怎么竞争？ | competitor teardown, price/offer mapping | 拆页面、卖点、变体 | 判断哪些差异可复制 |
| 机会在哪里？ | gap analysis, OST | 生成机会树和反证 | 选择值得继续的机会 |
| 方案是否可行？ | supplier inquiry, BOM, sample teardown | 生成问题清单 | 供应链/财务确认 |
| 用户会不会买？ | mock test, survey, ad/search test, small batch | 设计实验和指标 | 决定测试成本和阈值 |
| 是否进入开发？ | decision review, risk scoring | 汇总证据和风险 | 最终 go/no-go |

## What seems true

- 结构化研究流程的最小骨架应是：`Brief -> Discover -> Define -> Develop -> Validate -> Decide`。
- LLM 最适合放在信息抽取、结构化、候选生成和反证生成环节。
- 人应该控制边界、判断、资源投入和最终决策。
- KES 的优势不是比别人更会写 prompt，而是能把供应链、运营数据、页面内容和用户反馈放进同一个研究系统。
- 对电商品类，市场研究不能只看“需求”，还必须同时看“页面表达、产品配置、供应链可行性、退货风险和毛利”。

## Flow review and optimization

### Current flow is directionally sound

当前最小流程是合理的，因为它满足四个基本要求：

- `先发散再收敛`：先理解品类、需求、竞品，再定义机会和方案。
- `先机会后方案`：避免一开始就爱上某个产品想法。
- `先 KES fit 后投入`：避免追逐不适合自身能力的市场机会。
- `先假设后验证`：把研究压缩成可执行的小实验，而不是停留在报告。

它的问题不在方向，而在执行颗粒度还不够。如果直接照这个版本跑，容易出现三个风险：
- 每个阶段什么时候算完成不够清楚。
- 数据质量和证据强弱不够清楚。
- 机会进入产品开发前，缺少一个轻量商业 case 层。

### Missing piece 1: stage entry and exit criteria

每个阶段都应该有进入条件和退出条件，否则流程会变成“感觉差不多就进入下一步”。

建议增加 `entry / exit gate`：

| Phase | Entry condition | Exit condition |
| --- | --- | --- |
| Research brief | 有明确品类或方向 | 研究问题、边界、决策标准被人确认 |
| Category discovery | 有初始关键词/竞品 | 子品类、价格带、替代品、角色被拆清 |
| Demand discovery | 有 reviews/search terms/Q&A | 至少形成 5-10 个带证据的用户任务/痛点 |
| Competition mapping | 有代表性竞品集 | 竞品 offer、价格、页面、差评结构被比较 |
| Opportunity definition | 有需求和供给缺口 | 形成 3-7 个机会，每个有证据和反证 |
| KES fit filter | 有机会候选 | 排除不适合 KES 的机会，保留少数优先项 |
| Solution ideation | 有优先机会 | 每个机会至少 2-3 个方案 |
| Assumption/risk mapping | 有方案候选 | 找出每个方案的最危险假设 |
| Validation plan | 有关键假设 | 每个优先方案有 1-4 周可执行验证动作 |
| Decision record | 有验证结果或阶段结论 | 明确 continue / pause / kill / revisit |

### Missing piece 2: evidence quality scoring

LLM 很容易把不同强度的证据写成同等确定的结论。流程里应该要求所有关键判断标注证据等级。

建议用简单四档：

| Evidence level | Meaning | Example |
| --- | --- | --- |
| A | 直接强证据 | 大量 review、后台数据、供应商确认、样品拆解 |
| B | 直接弱证据 | 少量 review、少数 Q&A、单个竞品样品 |
| C | 间接证据 | 搜索词、页面表达、竞品定价、类比品类 |
| D | 推断 | LLM/团队基于经验的合理猜测 |

机会进入验证前，不要求全是 A/B 证据，但必须知道哪些判断只是 C/D。对 C/D 判断，validation plan 应优先验证。

### Missing piece 3: business case layer

当前流程从 `KES fit` 直接到 `solution ideation`，中间还应该加一个轻量商业 case 检查。否则可能出现产品上可行、用户也有需求，但经济账不成立。

建议在 KES fit 后增加 `Commercial sanity check`：
- 目标售价区间。
- 预估 landed cost。
- Amazon fee / FBA / referral / ads pressure。
- 包装尺寸和重量影响。
- 退货风险。
- 变体数量和库存压力。
- 预期毛利安全垫。
- MOQ 和现金占用。
- 是否需要认证、测试、模具、专利规避。

这不是完整财务模型，而是早期否决机制。它的目的不是精确预测利润，而是排除明显不值得继续的方向。

### Missing piece 4: portfolio view

单个机会看起来好，不代表它是 KES 当前最该做的。流程最后应多一个 portfolio view：
- 是防守型改进，还是进攻型新品？
- 是低风险小优化，还是高不确定性新方向？
- 是快速测试，还是需要长期供应链投入？
- 是否和现有类目、图片系统、内容系统、供应链资产复用？
- 是否会分散团队注意力？

建议把机会分成四类：

| Type | Meaning | Action |
| --- | --- | --- |
| Core improvement | 改进现有品类/产品 | 优先验证，通常 ROI 更清楚 |
| Adjacent expansion | 相邻品类或配件 | 适合小样品/小批量测试 |
| Content-led opportunity | 产品变化小，页面/说明/组合变化大 | 适合快速 mock 和 listing 测试 |
| New capability bet | 需要新供应链/认证/工艺 | 慎重，只在证据很强时推进 |

### Optimized flow v2

更完整但仍保持轻量的版本应是：

```text
0. Research brief
1. Category discovery
2. Demand / JTBD discovery
3. Competition and offer mapping
4. Opportunity definition
5. Evidence quality review
6. KES fit filter
7. Commercial sanity check
8. Solution ideation
9. Assumption / risk mapping
10. Validation plan
11. Portfolio prioritization
12. Decision record
```

相比原版，v2 只增加三类检查：
- `Evidence quality review`：防止把推断当事实。
- `Commercial sanity check`：防止产品上可行但商业上不值得。
- `Portfolio prioritization`：防止单点机会抢走更重要的资源。

这三个环节不需要做重，但必须存在。

### Practical recommendation

第一版工具/流程可以不把 12 步全部做成复杂模块，但应在模板里保留这些字段。最小可执行形态是：

- 一张 `research brief` 表。
- 一张 `evidence table`。
- 一张 `opportunity table`。
- 一张 `KES fit + commercial sanity` 评分表。
- 一张 `validation plan` 表。
- 一页 `decision record`。

这样既不会过度产品化，也能防止 LLM 研究失控。

## What is still uncertain

- KES 第一版应优先从哪个品类试跑，取决于现有数据完整度和供应链响应速度。
- review/search term 的自动聚类质量需要用真实品类测试。
- Opportunity scoring 的权重需要用历史成功/失败产品回测。
- 哪些验证动作最便宜有效，需要按品类建立经验库。
- Commercial sanity check 的阈值需要结合 KES 的真实毛利、广告成本、库存资金和退货数据校准。
- Evidence quality scoring 是否足够简单，需要跑完 1-2 个品类后调整。

## Implications

- 下一步不是直接开发 agent，而是先定义研究对象、数据模型、阶段输出和 human gate。
- 每一阶段都应有固定输出模板，方便 LLM 自动填充、人类审核、wiki 留档。
- KES 可以先做一个手动+半自动流程：用 LLM 跑研究，用表格/wiki 记录结果，用人做闸口决策。
- 跑完 2-3 个品类后，再把高重复步骤产品化成 agent workflow。
- 结构化流程 v2 应优先产品化成模板和表格，而不是先写复杂 agent orchestration。
- 工具化落地应从 project/source/evidence/job/competitor/opportunity/validation/decision 这组数据对象开始，而不是从聊天界面开始。

## Related pages

- [KES 产品市场研究流程工具化落地蓝图](../projects/kes-product-market-research-tooling.md)
- [LLM 驱动的 KES 细分品类产品市场研究协议](../protocols/llm-product-market-research-for-kes-categories.md)
- [AI Agents](../topics/ai-agents.md)
- [电商页面图片生成与内容规划研究](../questions/电商页面图片生成与内容规划研究.md)

## Sources

- [Qualtrics: 9 Key Stages In Your Marketing Research Process](https://www.qualtrics.com/articles/strategy-research/marketing-research-process/)
- [Design Council: Framework for Innovation / Double Diamond](https://www.designcouncil.org.uk/resources/framework-for-innovation/)
- [Harvard Business School: Know Your Customers' Jobs to Be Done](https://www.hbs.edu/faculty/Pages/item.aspx?num=51553)
- [Harvard Business School: Integrating Around the Job to Be Done](https://www.hbs.edu/faculty/Pages/item.aspx?num=39192)
- [IdeaPlan: Opportunity Solution Tree](https://www.ideaplan.io/frameworks/opportunity-solution-tree)
