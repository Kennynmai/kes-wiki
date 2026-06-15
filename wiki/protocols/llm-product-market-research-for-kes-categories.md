---
type: protocol
status: active
created: 2026-05-08
updated: 2026-05-08
tags: [ai, llm, product-research, ecommerce, kes, opportunity]
domain: ai
domains: [ai, ecommerce, product, market-research, workflow]
confidence: medium
review_cycle: monthly
verification_status: unverified
related:
  - ../projects/kes-product-market-research-tooling.md
  - ../syntheses/structured-product-market-research-methods-for-kes.md
  - ../topics/ai-agents.md
  - ../questions/电商页面图片生成与内容规划研究.md
---

# LLM 驱动的 KES 细分品类产品市场研究协议

## Trigger / scope

当需要基于一个 KES 已经营或相邻的细分产品市场，快速建立整体认知、识别真实用户需求、判断竞争结构，并找到可执行的产品切入点时，使用本协议。

本协议的目标不是让 LLM 直接给出“爆品答案”，而是让 LLM 帮人更快完成三件事：
- 建立品类地图。
- 暴露需求、供给和渠道之间的不匹配。
- 把机会收敛成可验证的产品假设。

适用场景：
- 已有品类，但想找升级款、差异化款、套装、配件、替代方案。
- 想进入相邻品类，但还没有足够市场直觉。
- 已有若干竞品链接、评论、广告词、搜索词、客服反馈，需要快速结构化。
- 想把 KES 的现有供应链、内容生产、Amazon 运营和 AI 系统能力转化为产品开发优势。

不适用场景：
- 需要即时销售数据、平台后台数据或供应商报价的最终判断。
- 高监管、高安全责任、强认证依赖的产品最终决策。
- 仅凭公开网页就能直接定版的产品开发决策。

## Inputs

最低输入：
- 品类名称和目标平台，例如 Amazon US 某类目。
- 5-20 个代表性竞品链接或 ASIN。
- 目标价格带或可接受毛利区间。
- KES 当前可利用的能力边界：供应链、材料、工艺、认证、内容、渠道、库存、售后。
- 明确的约束：不能做什么、供应链短板、合规风险、资金/交期限制。

增强输入：
- review 抓取文本。
- ads search term / organic search term。
- 退货、差评、客服、安装问题。
- 竞品图片、A+ 页面、说明书。
- 供应商目录、BOM、报价区间。
- KES 已有产品 attributes / selling points / context / certifications。

## Output contract

每次研究应输出 7 个结果，而不是一份泛泛的市场总结：

1. `category map`：品类边界、子类、使用场景、购买人群、价格带。
2. `demand map`：用户任务、痛点、焦虑、未满足需求、显性/隐性约束。
3. `competition map`：主要玩家、同质化点、差异化点、页面表达方式、评论结构。
4. `value gaps`：用户真正抱怨但供给没有解决好的地方。
5. `KES fit`：哪些机会符合 KES 能力，哪些看似好但不适合。
6. `opportunity shortlist`：3-7 个可执行切入点，每个都有理由、风险、验证方式。
7. `next validation plan`：下一轮要查什么、问谁、买什么样品、测什么指标。

## Steps

## Operating model: workflow first, agent second

第一版不应追求全自动 agent。更稳妥的设计是：

```text
structured workflow + LLM subagents + human decision gates
```

原因是产品机会判断里有几类东西不能交给 LLM 自动拍板：
- KES 真实供应链能力。
- 毛利、现金流、库存和交期约束。
- 平台后台数据、广告数据、实际转化数据。
- 合规、安全、认证和售后责任。
- 老板/团队对战略方向和风险的偏好。

LLM 可以自动做大量研究和整理，但关键决策应由人确认。系统的价值不是“替人决定做什么产品”，而是把人的决策前置条件准备得更完整、更快、更可审计。

### Recommended architecture

第一版应设计为一个可重复运行的研究系统，而不是一个自由聊天 agent：

1. `Project setup`
   - 人输入品类、平台、价格带、KES 能力、约束、竞品列表。
   - 系统生成研究任务和数据需求清单。

2. `Data ingestion`
   - 系统收集/导入竞品、reviews、Q&A、search terms、页面图片、供应链资料。
   - 人确认数据是否足够、是否代表目标市场。

3. `LLM extraction`
   - LLM 自动抽取需求、痛点、竞品卖点、页面表达、差评结构、规格和风险。
   - 系统保留证据引用和原文片段。

4. `Human gate 1: market boundary`
   - 人确认研究边界是否正确：是不是同一个市场、价格带、用户场景。
   - 如果边界错，回到数据和分类阶段。

5. `LLM synthesis`
   - LLM 生成 category map、demand map、competition map、value gaps。
   - Skeptic agent 同时找反证、伪机会和风险。

6. `Human gate 2: opportunity framing`
   - 人选择哪些缺口值得继续研究。
   - 人剔除不符合 KES 战略或能力边界的方向。

7. `KES fit and product hypothesis`
   - 系统把机会转成产品假设：产品变化、内容变化、供应链变化、验证成本。
   - LLM 辅助生成评分和验证计划。

8. `Human gate 3: validation decision`
   - 人决定进入哪一种验证：买样品、找供应商、抓更多评论、做页面 mock、算 BOM、做小批量测试。
   - 这里是 go / no-go / more research 的真正决策点。

9. `Execution tracking`
   - 系统追踪验证动作、负责人、截止时间、结果。
   - 验证完成后更新机会评分和结论。

### What can be automated

适合自动化：
- 抓取和整理公开信息。
- review / Q&A / search term 聚类。
- 竞品页面结构拆解。
- 用户需求、痛点、焦虑、场景抽取。
- 机会候选生成。
- 初版评分。
- 风险清单和反证信号生成。
- 研究报告和 wiki 页面草稿。

### What should require human approval

必须有人参与：
- 研究边界确认。
- 数据是否足够的判断。
- KES fit 评分确认。
- 是否涉及合规、安全、认证风险。
- 是否值得投入样品、供应商沟通或开发资源。
- 是否进入上架测试、小批量采购或正式开发。

### Agent framework implication

可以用 agent 框架，但 agent 框架只是执行层，不是产品判断层。

更合理的顺序是：
1. 先定义每个步骤的输入、输出、评分表、决策闸口。
2. 再把部分步骤交给 LLM agent 自动执行。
3. 最后把研究结果写入数据库/wiki/项目管理系统，供人 review 和追踪。

不要一开始就做一个“全自动市场研究 agent”。那会很快遇到三个问题：
- agent 会把证据不足的地方补成合理叙事。
- 人很难知道哪些结论来自原始证据，哪些只是模型推断。
- 最终机会建议无法直接进入产品开发会议，因为缺少责任边界和决策记录。

更好的第一版产品形态是 `guided research cockpit`：系统自动跑研究，人按闸口确认，所有结论可追溯。

### 1. 定义研究边界

先让 LLM 固定研究边界：
- 产品是什么，不是什么。
- 对应哪些搜索词、类目、替代品。
- 用户在什么场景下购买。
- 购买决策由谁做、使用者是谁、安装/维护者是谁。
- 本次只研究哪个价格带、渠道和地区。

如果边界不清，LLM 很容易把多个市场混在一起，输出看似完整但不可执行的结论。

### 2. 建立品类地图

让 LLM 把品类拆成：
- 子品类。
- 使用场景。
- 材料/结构/规格。
- 价格带。
- 渠道表达方式。
- 关键属性。
- 替代方案。

关键不是“分类漂亮”，而是看清不同子市场的购买逻辑是否不同。例如：有的按安装兼容性买，有的按审美买，有的按耐用性买，有的按安全/认证买。

### 3. 把评论和搜索词转成需求地图

对 review、search term、Q&A、客服反馈做抽取：
- 用户要完成什么任务。
- 用户为什么不满意现有产品。
- 用户在购买前担心什么。
- 用户收到货后在哪里失望。
- 哪些问题是产品问题，哪些是说明/安装/预期管理问题。
- 哪些抱怨高频但低价值，哪些抱怨低频但可能指向高利润机会。

LLM 输出时必须保留证据来源和代表性原文片段，避免把少数噪音包装成“大趋势”。

### 4. 拆竞争供给

对竞品做结构化比较：
- 产品形态。
- 核心卖点。
- 页面叙事。
- 图片/A+ 表达。
- 价格与套装。
- 规格覆盖。
- 评论优势。
- 评论缺陷。
- 供应链复杂度。
- 是否容易被复制。

重点找三类信号：
- `overcrowded parity`：大家都在讲同样的卖点。
- `unclaimed value`：用户在意，但页面很少讲清楚。
- `structural weakness`：不是改文案能解决，而是产品结构、配件、说明、安装、质量控制的问题。

### 5. 识别机会，不直接相信机会

LLM 生成机会时必须按以下格式输出：
- 机会名称。
- 对应用户任务。
- 当前供给缺口。
- 为什么 KES 可能做得更好。
- 所需产品变化。
- 所需内容/页面变化。
- 供应链复杂度。
- 合规/认证/安全风险。
- 预计验证成本。
- 反证信号：看到什么证据就应该放弃。

这里的重点是反证信号。没有反证条件的“机会”只是想法。

### 6. 用 KES fit 过滤

机会必须经过 KES fit 过滤：
- 是否利用现有品类知识。
- 是否利用现有供应商或工艺。
- 是否可以用现有内容系统表达清楚。
- 是否适合 Amazon 页面竞争。
- 是否有可控库存和变体复杂度。
- 是否能被现有团队运营和售后承接。
- 是否有足够毛利承受测试和迭代。

过滤后的优先级应高于原始市场吸引力。对 KES 来说，最好的机会不是“市场最大”，而是“有能力把小缺口做透”。

### 7. 形成验证计划

每个候选机会都要落到下一步验证动作：
- 买样品还是找供应商。
- 抓多少 review。
- 访谈哪类用户。
- 验证哪个规格或安装问题。
- 做哪种页面 mock。
- 测算哪个 BOM 或物流变量。
- 需要什么合规确认。
- 用什么阈值决定继续/暂停/放弃。

研究结束时，应能回答：
- 下周能做什么。
- 谁来做。
- 做完以后用什么标准判断。

## LLM agent roles

可把一次研究拆成几个 LLM 角色，但最终必须合并到同一张机会判断表：

- `Category cartographer`：画品类地图和替代方案地图。
- `Review miner`：从评论中抽需求、痛点、失望点和证据。
- `Competitor analyst`：拆竞品定位、卖点、页面和价格。
- `Product engineer proxy`：把需求翻译成产品结构、规格、配件、说明书和 QC 变化。
- `Amazon operator proxy`：判断页面表达、搜索词、图片、A+ 和转化路径。
- `Skeptic`：专门找反证、合规风险、供应链复杂度和伪机会。

## Prompt skeleton

```text
你是一个面向 Amazon 电商品类的产品开发研究助手。

研究对象：
- 品类：
- 地区/平台：
- 价格带：
- 目标用户：
- KES 可用能力：
- 明确约束：

输入材料：
- 竞品：
- reviews / Q&A：
- search terms：
- 供应链或产品资料：

请输出：
1. category map
2. demand map
3. competition map
4. value gaps
5. KES fit analysis
6. opportunity shortlist
7. next validation plan

要求：
- 每个判断都标注证据来源或说明它只是推断。
- 不要只给市场总结，要收敛到可验证的产品假设。
- 每个机会必须包含反证信号。
- 区分产品改进、内容表达改进、运营改进和供应链改进。
```

## Opportunity scoring

候选机会用 1-5 分粗筛：

| Axis | Question |
| --- | --- |
| Demand clarity | 用户任务和痛点是否清楚、反复出现？ |
| Supply gap | 现有产品是否真的没有解决好？ |
| KES fit | KES 是否有现实能力做得更好？ |
| Differentiability | 页面、产品、配件或体验是否能被用户感知？ |
| Validation speed | 是否能在 1-4 周内获得有效验证？ |
| Margin room | 是否有足够毛利覆盖试错和质量投入？ |
| Risk control | 合规、安全、售后、库存复杂度是否可控？ |

粗筛公式：

```text
Priority = Demand clarity + Supply gap + KES fit + Differentiability + Validation speed + Margin room + Risk control
```

但如果 `Risk control <= 2` 或 `KES fit <= 2`，默认降级，不因总分高而进入优先执行。

## Failure modes

- 把 LLM 的“合理叙事”误认为真实市场证据。
- 只分析页面，不分析产品结构、安装、配件、说明书、售后。
- 只看高频差评，忽略低频但高价值的深层缺口。
- 把搜索量大误认为机会好。
- 把竞品做得差误认为自己容易赢。
- 忽略 KES 自身能力边界，追逐不适合的机会。
- 没有反证信号，导致研究变成确认偏误。
- 没有下一步验证动作，导致研究停留在“有启发”。

## Review notes

- 本协议目前是方法框架，未绑定具体品类实证。
- 第一次使用时应选择一个 KES 已有资料较多、供应链可触达、评论量充足的细分品类。
- 第一次跑完后，应把输出沉淀成一个具体 `question` 或 `synthesis` 页面，而不是只保存对话。

## Related pages

- [KES 产品市场研究流程工具化落地蓝图](../projects/kes-product-market-research-tooling.md)
- [KES 结构化产品市场研究方法论](../syntheses/structured-product-market-research-methods-for-kes.md)
- [AI Agents](../topics/ai-agents.md)
- [电商页面图片生成与内容规划研究](../questions/电商页面图片生成与内容规划研究.md)

## Sources

- Internal synthesis from existing KES ecommerce and AI-agent workflow notes.
- [Qualtrics: 9 Key Stages In Your Marketing Research Process](https://www.qualtrics.com/articles/strategy-research/marketing-research-process/)
- [Design Council: Framework for Innovation / Double Diamond](https://www.designcouncil.org.uk/resources/framework-for-innovation/)
- [Harvard Business School: Know Your Customers' Jobs to Be Done](https://www.hbs.edu/faculty/Pages/item.aspx?num=51553)
- [Harvard Business School: Integrating Around the Job to Be Done](https://www.hbs.edu/faculty/Pages/item.aspx?num=39192)
- [IdeaPlan: Opportunity Solution Tree](https://www.ideaplan.io/frameworks/opportunity-solution-tree)
