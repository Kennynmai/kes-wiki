---
type: playbook
status: draft
owner: strategy
created: 2026-04-19
updated: 2026-04-19
visibility: company
confidence: medium
officiality: draft
domain: operations
domains: [amazon, rufus, geo, ai-search, content-operations]
review_cycle: monthly
verification_status: spot-checked
related:
  - ../platforms/amazon-rufus-and-cosmo.md
  - ../syntheses/amazon-rufus-cosmo-e-geo-kes-response.md
  - ../syntheses/kes-ai-era-amazon-content-strategy-judgment.md
  - ../syntheses/kes-geo-experiment-backlog.md
  - ../source-summaries/amazon-rufus-official-updates-2024-2026.md
  - ../source-summaries/openai-shopping-official-docs-2025-2026.md
---

# Amazon / Rufus GEO 审计与站外佐证执行手册

## Trigger / scope
这页用于把三件事落成固定操作：
- `monthly Rufus query audit`
- `用 Rufus 做 GEO maturity test`
- `build off-Amazon FAQ / comparison pages as corroboration`

适用触发条件：
- 新 ASIN / 新类目准备 launch
- 标题、bullets、A+、Q&A 有重大改版
- review 结构出现明显变化
- competitor 页面明显改版
- Amazon / Rufus surface 出现新能力或新展示方式

不适用的情况：
- 没有 evidence registry 就想先写 comparison / FAQ
- 高风险 claim 尚未完成合规复核
- 想从单次 Rufus 回答反推出稳定 ranking rule

## Inputs
- target ASIN set
- fixed competitor basket
- current Amazon surfaces snapshot
  - title
  - bullets
  - structured attributes
  - A+ / comparison module
  - Q&A
  - reviews
- evidence registry / claim register
- 上月 audit 记录
- brand site 已有 FAQ / comparison / guide 页面清单
- platform change log

## Steps
### Step 1｜Freeze the audit basket
每次审计先冻结四个变量：
- marketplace / locale
- KES ASIN set
- competitor set
- operator context

最低建议：
- 1 个 hero ASIN
- 2 到 5 个 closest competitors
- 1 个核心 locale

如果这些变量没冻结，月度对比通常会失真。

### Step 2｜Build the monthly query deck
query deck 必须覆盖不同决策阶段，而不是只测“产品词 + best”。

| Query family | Why it matters | Minimum count | Example angle |
|---|---|---:|---|
| broad discovery | 看能否进入候选集 | 2 | 这是什么产品 / 哪类人会买 |
| use-case / scenario | 看 intent alignment | 2 | 什么场景适合 |
| comparison | 看 mid-funnel 决策能力 | 2 | A vs B / 哪个更适合 |
| negation / exclusion | 看 non-fit 表达 | 2 | 不适合谁 / 不要什么 |
| fit / compatibility | 看边界条件是否清楚 | 2 | 和什么兼容 / 不兼容 |
| objection / risk | 看信任与证据强度 | 2 | 值不值得 / 会不会有问题 |
| maintenance / support | 看 post-purchase answer surface | 1 | 买后怎么维护 |

最低不要少于 `13` 条 query。

### Step 3｜Run the Rufus scorecard
每条 query 都按同一张 scorecard 记录，不要只留截图。

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| inclusion | 未出现或完全不相关 | 出现但边缘 / 不稳定 | 稳定出现且相关 |
| product-type accuracy | 说错产品类型 | 方向对但模糊 | 类型清楚准确 |
| use-case accuracy | 场景理解明显偏 | 提到部分场景 | 场景与受众清楚 |
| non-fit clarity | 不会排除错误人群 | 有边界但不完整 | 能明确说出不适合谁 |
| comparison quality | 只给空泛推荐 | 有比较但 tradeoff 弱 | 比较清楚且有 tradeoff |
| objection fidelity | 回答带明显幻觉或空话 | 部分可用 | 回答有证据边界且可行动 |

单条 query 满分 `12` 分。

### Step 4｜Map score to maturity level
不要只看平均分，更要看最弱项卡在哪里。

| Total score | Maturity read | Meaning |
|---|---|---|
| 0–2 | `Level 0` | 基本 invisible 或被误解 |
| 3–5 | `Level 1` | 能出现，但只会复述模糊卖点 |
| 6–8 | `Level 2` | 基础用途能说清，但 comparison / objection 弱 |
| 9–10 | `Level 3` | 大部分核心 query 可正确回答 |
| 11–12 | `Level 4` | 高价值 comparison / objection 也较稳定 |

同一 ASIN 不应只给总等级，还应标一条最弱层：
- `retrieval weak`
- `description weak`
- `comparison weak`
- `trust weak`
- `external corroboration weak`

### Step 5｜Translate symptoms into action surfaces
发现问题后，不要默认去改 title。先判断问题属于哪一层。

| Observed symptom | Likely root cause | First fix surface |
|---|---|---|
| 完全不出现或经常被错类 | product-type noun / category / attributes 弱 | title + category + structured attributes |
| 出现但讲不清是什么 | noun 清楚度不足 / top bullets 太虚 | title + first 2 bullets |
| 会讲用途，但不会讲限制 | non-fit / exclusion 没写 | bullets + Q&A + FAQ |
| 会出现，但 comparison 总被 competitor 带节奏 | 缺 comparison-ready facts | A+ comparison + comparison page |
| objection 回答常空泛或幻觉 | proof points 弱 / evidence boundary 没写 | FAQ + Q&A + evidence-backed bullets |
| maintenance/support 说不清 | 买后信息埋得太深 | FAQ + care guide + Q&A |
| 常引用 competitor 的 framing 来解释 KES | KES 自己的 answer surface 不够完整 | comparison page + fit/non-fit guide |

### Step 6｜Decide whether to build an off-Amazon page
站外页不是默认动作。只有当 Amazon 内部 surface 很难完整表达，或者外部 corroboration 明显缺位时才建。

| Repeated problem  | Best page type             | Why                   |
| ----------------- | -------------------------- | --------------------- |
| 高频 objection 反复出现 | `high-objection FAQ`       | 适合回答边界、误解、维护、限制       |
| 常被拿去和相邻替代方案比较     | `comparison page`          | 适合写 tradeoff，而不只是卖点   |
| 兼容性 / 适配性经常被误判    | `fit / non-fit guide`      | 适合把谁适合、谁不适合写清         |
| 买后维护问题多           | `care / maintenance guide` | 适合沉淀使用、保养、替换规则        |
| 用户先要做路线选择         | `selection guide`          | 适合 scenario A vs B 决策 |

### Step 7｜Use the correct page archetype
不同 page type 写法不一样，不能全部写成 blog post。

#### FAQ archetype
最小结构：
1. 明确问题句
2. 先给结论句
3. 再给条件句
4. 明确 non-fit / 例外
5. 给 evidence boundary

#### Comparison archetype
最小结构：
1. 先写 “谁适合 A / 谁适合 B”
2. side-by-side tradeoff table
3. `when to choose A`
4. `when not to choose A`
5. 不夸张的总结句

#### Fit / non-fit guide archetype
最小结构：
1. 先列适合人群 / 场景
2. 再列不适合人群 / 场景
3. 说明为什么
4. 说明替代路径

### Step 8｜Publish with cross-surface discipline
站外页上线前必须对三件事：
- Amazon PDP wording
- Q&A wording
- FAQ / comparison wording

任何一处说法更强、更绝对、边界更模糊，都视为不通过。

### Step 9｜Measure with the right window
不要只看 pageview。至少跟踪四周，并同时看五类结果：
- `AI citation / mention rate`
- `answer completeness`
- `cross-surface consistency`
- `assisted click-through`
- `support deflection`

### Step 10｜Apply stop rules
有三种情况要停止继续加内容：
- 连续 `2` 个 audit cycle 没改善，说明 root cause 可能不在 page surface
- citation 变多但 hallucination / support complaints 变高，说明 trust 失真
- 为了提高回答完整度开始触碰 unsupported claims，必须停

## Quality checks
### Monthly audit quality bar
- 同一 query deck 至少连续沿用 `2` 个 cycle
- 同一 ASIN 至少保留 `1` 个固定 competitor basket
- 每条 query 都有文字记录，不只截图
- 每条问题都有 `score + likely cause + next action`

### Page quality bar
- first screen 就能看懂这是什么、适合谁、不适合谁
- 至少有一处明确 tradeoff，不是纯单边夸赞
- 高风险 claim 能追溯到 evidence registry
- Amazon 与站外 wording 不冲突

## Exceptions
### New product with thin review history
如果产品刚 launch、review 和 Q&A 都很薄：
- 不要把“没有 review signal”误判成 GEO 失败
- 优先补 PDP / A+ / FAQ 基础层

### High-regulation or high-claim categories
如果类目涉及健康、功效、合规敏感：
- comparison / FAQ 页必须先过 claim review
- 宁可少写，也不要把 educational layer 写成 efficacy promise

### Locale-specific instability
如果不同 marketplace 差异很大：
- 不要把一个 locale 的 query deck 直接复制到全部市场

## Failure modes
### Failure mode 1｜Overfitting to one query
看到一条 query 赢了，就大改整套文案。

### Failure mode 2｜Confusing mention with recommendation
被提到不等于被公平理解，更不等于被优先选择。

### Failure mode 3｜Writing FAQ filler
FAQ 看起来很多，但没有真实结论、条件和 non-fit。

### Failure mode 4｜Using comparison pages as disguised ads
没有 tradeoff、没有边界、没有 “when not to choose us”，通常很难形成可信 corroboration。

### Failure mode 5｜Ignoring platform drift
页面没变，不代表结果应该不变。Rufus、search partners、AI surfaces 都可能改。

### Failure mode 6｜Cross-surface contradiction
Amazon 写得保守，站外写得更猛，会直接削弱可信度。

## Sources
- [Amazon Rufus / COSMO / E-GEO｜KES 如何利用与应对](../syntheses/amazon-rufus-cosmo-e-geo-kes-response.md)
- [KES 版判断｜AI 时代 Amazon 内容策略](../syntheses/kes-ai-era-amazon-content-strategy-judgment.md)
- [KES GEO Experiment Backlog](../syntheses/kes-geo-experiment-backlog.md)
- [Amazon Rufus 与 COSMO](../platforms/amazon-rufus-and-cosmo.md)
- [来源摘要｜Amazon 官方 Rufus 更新（2024-2026）](../source-summaries/amazon-rufus-official-updates-2024-2026.md)
- [来源摘要｜OpenAI 官方购物文档（2025-2026）](../source-summaries/openai-shopping-official-docs-2025-2026.md)
