---
type: protocol
status: active
created: 2026-06-05
updated: 2026-06-05
tags: [kes, brand24, awario, social-listening, trial-test]
domain: business-strategy
domains: [cross-border-ecommerce, social-media-monitoring, competitive-intelligence, marketing-ops]
confidence: high
review_cycle: monthly
verification_status: unverified
related:
  - ../syntheses/kes-awario-brand24-testing-plan.md
  - ../syntheses/kes-social-media-monitoring-tool-evaluation.md
  - ../syntheses/awario-data-capabilities-for-kes-2026-06-04.md
  - ../syntheses/kes-sns-monitoring-master-doc.md
---

# KES Brand24 / Awario 试用版测试协议

## Trigger / scope

当 Brand24 和 Awario 试用账号已经开通，且需要在试用期内决定是否购买、购买哪一个、或是否继续双工具验证时，使用本协议。

本轮测试从 2026-06-05 开始。核心窗口是 7 天，因为 Awario 试用期较短；如果 Brand24 仍可继续试用，则第 8-14 天只验证 Brand24 独有增量，不再把它与 Awario 做全量公平对比。

本协议不验证“哪个工具理论上更强”，只验证 KES 当前业务下的四个问题：

1. 哪个工具能抓到更多真实相关的 KES / 竞品 / 埃及市场信号？
2. 哪个工具的噪音率更低，日常维护成本更低？
3. Brand24 的 LinkedIn / TikTok / Telegram / AI 报告是否构成实际溢价？
4. Awario 的 Boolean 搜索和 Leads 能否产生可操作线索？

## Decision rule

最终不要用“功能多”决策，用以下阈值决策：

| 结果 | 决策 |
|---|---|
| Awario 相关 mention 量 >= Brand24 的 80%，且噪音率低 20 个百分点以上 | 优先 Awario |
| Awario 相关 mention 量明显更低，但 Brand24 相关 mention 量高、独有来源真实有效 | 优先 Brand24 |
| Brand24 的 LinkedIn / TikTok / Telegram / LLM 提及在 7 天内几乎为 0 或业务无关 | 不把这些功能计入溢价 |
| Brand24 噪音率 > 40%，且无法通过排除词显著降低 | Brand24 不适合作为主监控工具 |
| Awario API / CSV / Zapier 都无法导出可用数据 | Awario 严重扣分，只能当人工 UI 工具 |
| 两者都抓不到足够有效数据 | 暂不购买，改为 Reddit / YouTube / Google Alerts / Meta Ad Library 的轻量组合 |

## Inputs

### 账号与权限

- Brand24 试用账号：已创建 project `kes` 或 `KES`
- Awario 试用账号：已创建 project / alert `KES`
- 截图证据：保留每次配置页、dashboard、导出页截图
- 数据记录表：建议用 Google Sheet 或本地 Markdown 表，字段见下方

### 试用版限制先验

以下都必须在测试中验证，不要当作已确认事实：

| 限制项 | Awario | Brand24 | 验证动作 |
|---|---|---|---|
| 可建 alert / project 数 | 待验证 | 待验证 | Day 0 创建时记录上限 |
| 是否支持 Boolean | 待验证 | 基本不按 Boolean 设计 | Day 0 输入复杂条件，看是否接受 |
| 是否支持排除词 | 待验证 | 截图显示有 Excluded keywords | Day 0 填入排除词并记录效果 |
| API 是否可用 | 待验证 | 待验证 | Day 1 查设置页和文档入口 |
| CSV / Excel 导出 | 待验证 | 待验证 | Day 3 和 Day 7 各导出一次 |
| 历史数据 | 待验证 | 待验证 | Day 0 记录是否能选择 historical data |

## Test design

### North America-first form filling

如果本轮先主要针对北美市场，优先填两个项目：`KES North America Brand` 和 `North America Competitor Pain Points`。不要把品牌词、竞品词、线索词、埃及阿拉伯语词全部混在一个 alert 里，否则后续无法判断噪音来自哪里。

#### Form 1: KES North America Brand

用于测试 KES 在北美公开网络上的品牌提及、噪音率和渠道分布。

Awario:

| Field | Fill with |
|---|---|
| Project name | `KES North America Brand` |
| Keyword | `"KES" OR "KES Home" OR "keshome" OR "keshome.com"` |
| Required keywords | 留空 |
| Excluded keywords | `Kenya shilling, school, exam, football, soccer, election, politics, knowledge exchange, key enabling, KES unit, general mills` |
| Language | `English`；若想保留多语言网页则选 `All languages`，但记录噪音可能更高 |

Awario early test result: bare `KES` is also too noisy. It matched `strikes`, Kenya real estate, music/artist `Kes`, film `Kes`, animal sanctuary abbreviations, and non-US news. For actual monitoring, switch to this stricter brand-intent Boolean:

```text
(
  "KES Home" OR "keshome" OR "keshome.com" OR
  ("KES" AND (faucet OR faucets OR shower OR "shower head" OR bathroom OR kitchen OR sink OR "towel bar" OR "bathroom hardware" OR "bathroom fixtures" OR Amazon OR "Home Depot" OR Wayfair))
)
AND NOT
(
  strikes OR strike OR missile OR Iran OR Israel OR Pakistan OR Kenya OR Kenyan OR "Kenya shilling" OR
  "Kes the Band" OR "Kes The Band" OR "Khaolak Ethical Elephant Sanctuary" OR elephant OR sanctuary OR
  "Barry Hines" OR "film Kes" OR movie OR music OR song OR band OR concert OR soca OR dance OR
  "real estate" OR realtor OR apartment OR apartments OR condo OR land OR plots OR subdivision OR
  school OR university OR college OR exam OR football OR politics OR election
)
```

If this still returns too much unrelated content, remove the `("KES" AND ...)` block and monitor only:

```text
"KES Home" OR "keshome" OR "keshome.com"
```

Brand24:

| Field | Fill with |
|---|---|
| Project name | `KES North America Brand` |
| Keywords | `"KES"` / `#KES` / `"KES Home"` / `keshome` / `keshome.com` |
| Excluded keywords | `"Kenya shilling"` / `school` / `exam` / `football` / `soccer` / `election` / `politics` / `"knowledge exchange"` / `"key enabling"` / `"KES unit"` / `"general mills"` |
| Languages | `English` |
| Locations | `United States`, `Canada` |
| Sources | `All` for first 48 hours; if noise is too high, keep Web/News/Blogs/Forums/Reddit/YouTube and separately note any social-source limitation |
| Include Historical Data | `Any Time` if free in trial; otherwise `Now onward` is acceptable, but record the limitation |

If Brand24 returns mostly unrelated `KES` mentions, change the project into a stricter brand-intent monitor:

| Field | Fill with |
|---|---|
| Keywords | `KES Home, keshome, keshome.com, KES faucet, KES shower, KES bathroom, KES kitchen, KES towel bar, KES hardware, KES sanitary, KES Amazon, KES Home Depot, KES Wayfair` |
| Excluded keywords | `Kenya shilling, KES, Kes, kes, school, exam, football, soccer, election, politics, knowledge exchange, key enabling, KES unit, general mills, market cap, stock, stocks, shares, earnings, dividend, crypto, NASDAQ, NYSE, OTC, bank, loan, careers, jobs, hiring, music, concert, song, band, anime, game, gaming, coupon, book fair, TEDx, Indian, India, Turkey, Turkish, Korea, Korean, Siberia, Columbia, Manhattan, charities, nonprofit, university, college, hospital, clinic, MD, apartments, relocation, exchange rate` |

Important: only exclude bare `KES` if Brand24 still keeps returning unrelated mentions after the stronger positive keyword list is saved. If excluding bare `KES` blocks all results, remove `KES` from excluded keywords and rely on the other exclusions.

If the stricter Brand24 setup returns only a small set of ecommerce/SEO pages, keep it as the precision monitor but add one discovery project or loosen keywords slightly:

```text
KES Home, keshome, keshome.com, KES faucet, KES faucets, KES shower, KES shower system, KES sink faucet, KES kitchen faucet, KES bathroom faucet, KES towel warmer, KES towel bar, KES drain, KES bidet, KES matte black, KES brushed gold, KES Amazon, KES Walmart, KES Home Depot, KES Wayfair
```

Use a lighter exclusion list first:

```text
Kenya shilling, school, exam, football, soccer, election, politics, knowledge exchange, key enabling, KES unit, general mills, market cap, stock, earnings, dividend, crypto, NASDAQ, NYSE, bank, loan, careers, jobs, hiring, music, concert, song, band, anime, game, gaming, book fair, TEDx, India, Indian, Turkey, Turkish, Korea, Korean, Siberia, Columbia, Manhattan, charities, nonprofit, university, college, hospital, clinic, apartments, relocation, exchange rate
```

Do not exclude bare `KES` in this discovery configuration. Instead, judge the project by noise rate after 24-48 hours. If noise rises above 50%, return to the precision configuration.

Brand24 KES brand-monitor interpretation:

| Observation | Interpretation |
|---|---|
| 10-20 mostly relevant mentions in 30 days | The precision setup works, but it is too narrow for broad brand listening. |
| Results are mostly Amazon/Walmart/keshome/product pages | Good for brand asset/index monitoring; weak for user discussion and reputation monitoring. |
| Almost no Reddit/forum/social conversation | Do not conclude "no one discusses KES"; conclude only that this Brand24 setup is not broad enough or Brand24 has limited discoverability for KES discussion. |

If the KES project returns too few results, loosen in this order:

1. Add channel phrases:

```text
KES Amazon, KES Walmart, KES Home Depot, KES Wayfair, KES faucet Amazon, KES shower Amazon, KES bathroom faucet Amazon
```

2. Add review / discussion phrases:

```text
KES review, KES reviews, KES faucet review, KES shower review, KES bathroom review, KES faucet install, KES shower install, KES faucet leaking, KES shower leaking, KES replacement, KES warranty
```

3. Add likely product descriptors:

```text
KES matte black faucet, KES brushed gold faucet, KES rain shower, KES shower system, KES kitchen faucet, KES sink faucet, KES towel warmer, KES bidet, KES drain
```

Do not add bare `KES` back unless running a separate short diagnostic test, because it previously produced severe noise.

If Brand24 trial allows only 10 keywords, use the project in two phases instead of trying to cover everything at once:

Phase A: pain-point evaluation keywords, run for 24-48 hours.

```text
Moen faucet, Moen shower, Delta faucet, Delta shower, Kohler faucet, Kohler shower, American Standard faucet, American Standard toilet, Pfister faucet, GROHE shower
```

Use the mentions search box for pain-point filters:

```text
leak{OR}leaking{OR}drip{OR}dripping
rust{OR}corrosion{OR}corroded
broken{OR}broke{OR}crack{OR}cracked
warranty{OR}replacement{OR}cartridge
pressure{OR}"low pressure"{OR}"water pressure"
```

Phase B: after pain-point evaluation, switch the same 10 keyword slots to KES brand monitoring:

```text
KES Home, keshome, keshome.com, KES faucet, KES shower, KES shower system, KES kitchen faucet, KES bathroom faucet, KES Amazon, KES Walmart
```

If marketplace monitoring matters more than product breadth, replace `KES bathroom faucet` and `KES Walmart` with:

```text
KES Home Depot, KES Wayfair
```

Do not mix Phase A and Phase B keywords in one 10-keyword project. It makes both pain-point and brand-monitoring metrics hard to interpret.

Brand24 pain-point early quality assessment:

| Dimension | Assessment |
|---|---|
| Raw recall | High. Brand24 can collect many competitor mentions quickly. |
| Raw precision | Low to medium. A broad pain term such as `rust`, `corrosion`, or `leak` brings in many unrelated mentions. |
| Main noise source | `Kohler` is highly ambiguous: engines, generators, hotels, manufacturing, tiles, jobs, corporate/news items. News/Web sources add a lot of non-product noise. |
| Useful pocket | Reddit and product-context web pages are the most useful. Generic news, corporate pages, jobs, and non-English posts are often low value. |
| Business value | Useful after filtering. Good for spot-finding complaints and Reddit threads; weaker than Awario for clean Boolean collection. |
| Keep testing? | Yes, but only with narrow searches and exclusions. Do not judge it from broad `rust OR corrosion` searches. |

For Brand24 pain-point filtering, prefer narrow pair searches:

```text
leak{AND}faucet
leaking{AND}faucet
drip{AND}shower
rust{AND}faucet
corrosion{AND}faucet
broken{AND}faucet
crack{AND}shower
warranty{AND}faucet
replacement{AND}cartridge
pressure{AND}shower
```

Add or keep these exclusions in project settings:

```text
Kohler engine, Kohler engines, generator, generators, mower, lawn mower, tractor, carburetor, horsepower, hotel, resort, spa, hospitality, hiring, job, careers, stock, investor, earnings, acquisition, plant, factory, manufacturing jobs, watch, clock, furniture, tile
```

When evaluating Brand24 pain points, report three separate rates:

```text
raw_mentions
product_context_mentions
true_pain_point_mentions
```

Do not count corporate news, product catalogs, coupon pages, generic repair services, or Kohler engine/generator results as true pain points.

#### Form 2: North America Competitor Pain Points

用于测试竞品投诉、产品弱点、内容营销素材。这个项目比 `KES` 品牌词更可能产出有效信息。

Awario:

| Field | Fill with |
|---|---|
| Project name | `North America Competitor Pain Points` |
| Keyword | `"GROHE" OR "Moen" OR "Delta Faucet" OR "Kohler" OR "Hansgrohe" OR "American Standard" OR "Pfister"` |
| Required keywords | `leaking, rust, poor quality, stopped working, disappointed, waste of money, lasted only, broke after, defective, cheap plastic, hard to install` |
| Excluded keywords | `stock, investor, earnings, hiring, job, football, school` |
| Language | `English` |

Awario Boolean mode exact query:

```text
(
  ("GROHE" OR "Moen" OR "Delta Faucet" OR "Kohler" OR "Hansgrohe" OR "American Standard" OR "Pfister")
  AND
  (faucet OR faucets OR "shower head" OR "shower system" OR "shower valve" OR bathroom OR kitchen OR sink OR tap OR toilet OR "towel bar" OR "bathroom fixtures" OR plumbing)
  AND
  (leak OR leaking OR leaked OR rust OR rusty OR corrosion OR corroded OR "poor quality" OR "stopped working" OR broken OR broke OR defective OR disappointed OR "waste of money" OR "lasted only" OR "cheap plastic" OR "hard to install" OR "low water pressure" OR "no water pressure" OR warranty OR replacement)
)
AND NOT
(
  "Delta Air" OR "Delta Airlines" OR "Delta flight" OR airline OR airport OR
  "Kohler engine" OR generator OR engines OR
  stock OR investor OR earnings OR hiring OR job OR football OR school
)
```

If results are too sparse after 24 hours, remove the pain-point block and keep only competitor + product context:

```text
(
  ("GROHE" OR "Moen" OR "Delta Faucet" OR "Kohler" OR "Hansgrohe" OR "American Standard" OR "Pfister")
  AND
  (faucet OR faucets OR "shower head" OR "shower system" OR bathroom OR kitchen OR sink OR tap OR toilet OR plumbing)
)
AND NOT
(
  "Delta Air" OR "Delta Airlines" OR "Delta flight" OR airline OR airport OR
  "Kohler engine" OR generator OR engines OR
  stock OR investor OR earnings OR hiring OR job OR football OR school
)
```

Awario early result evaluation:

| Dimension | Assessment |
|---|---|
| Relevance | Usable, but mixed. It finds real competitor/product repair issues, especially leaking, low water pressure, cartridge, replacement, warranty, and corrosion. |
| Source mix | Strongly skewed toward YouTube and indexed web pages. It is weaker so far for direct consumer complaint sources such as Reddit/forums/reviews. |
| Noise | Moderate. Noise includes product catalogs, coupon pages, generic plumbing services, HVAC/plumbing companies, unrelated Kohler engines, and generic bathroom advice. |
| Business value | Good for content topics and competitor defect taxonomy. Medium for brand-reputation/consumer-complaint monitoring. Weak for sales leads. |
| Keep testing? | Yes. Continue for 7 days, but score it as a content/SEO intelligence source unless Reddit/forum/share-of-voice improves. |

Critical risk: if Awario remains concentrated in indexed webpages and YouTube, its paid-tool value is limited. In that case it is not acting as differentiated social listening; it is mostly repackaging discoverable Google/YouTube results with alerting, sentiment, and export convenience. The buying case then requires evidence of at least one of:

```text
meaningful Reddit/forum/review coverage
material time savings versus manual Google/YouTube search
useful export/API automation into KES workflows
consistent weekly content-topic discovery that manual search would miss
```

If none of these appear by Day 7, do not buy Awario for pain-point monitoring; use Google/YouTube manual search plus Reddit search/export instead.

Treat as valid pain-point examples:

```text
Leaking Kohler faucet
Delta faucet corroded / squeaky
Moen low water pressure
Moen cartridge replacement due to leaking
Hansgrohe shower valve leaking
Kohler / Pfister warranty or replacement issue
```

Treat as noise or low-value:

```text
product catalog pages with warranty language only
generic plumbing company service pages
coupon/promo code pages
HVAC pages
Kohler engine / generator / mower content
generic how-to pages without a named competitor defect
```

Brand24:

| Field | Fill with |
|---|---|
| Project name | `North America Competitor Pain Points` |
| Keywords | `"GROHE"` / `"Moen"` / `"Delta Faucet"` / `"Kohler"` / `"Hansgrohe"` / `"American Standard"` / `"Pfister"` |
| Excluded keywords | `stock` / `investor` / `earnings` / `hiring` / `job` / `football` / `school` |
| Languages | `English` |
| Locations | `United States`, `Canada` |
| Sources | `All` |
| Include Historical Data | `Any Time` if free in trial |

For Brand24, if the trial project cannot express "competitor AND pain point" in the setup form, keep the competitor brands as keywords and use the mention search/filter layer later to count pain-point terms. Do not add generic terms like `leaking` or `rust` as standalone keywords, or the project will collect unrelated plumbing noise.

Brand24 pain-point filtering in Mentions:

1. Open the competitor project.
2. Set date range to `Last 30 days` for the first pass.
3. In the top `Search through mentions, authors & domains` box, search pain-point terms inside the collected competitor mentions.
4. Start with `Sentiment = Negative`, then repeat without sentiment filter because some complaints are misclassified as neutral or positive.
5. Save or tag useful results with tags such as `pain-leak`, `pain-rust`, `pain-install`, `pain-warranty`, `content-material`.

Use this strict query first:

```text
(leak OR leaking OR leaked OR dripping OR drip OR rust OR rusty OR corrosion OR corroded OR broken OR broke OR defective OR "poor quality" OR "stopped working" OR "waste of money" OR "lasted only" OR "cheap plastic" OR "hard to install" OR "low water pressure" OR "no water pressure" OR warranty OR replacement)
AND
(faucet OR faucets OR "shower head" OR shower OR bathroom OR kitchen OR sink OR tap OR toilet OR plumbing)
```

If Brand24 search does not accept parentheses reliably, run category searches one by one:

```text
leak OR leaking OR leaked OR dripping OR drip
rust OR rusty OR corrosion OR corroded
broken OR broke OR defective OR "stopped working"
"poor quality" OR "waste of money" OR "lasted only" OR "cheap plastic"
"hard to install" OR "low water pressure" OR "no water pressure"
warranty OR replacement
```

For unrelated Grohe/Darmstadt/music results, add exclusions in the project settings or mute the specific sites:

```text
darmstadt, "Grohe Hell", music, album, concert, football, school, stock, hiring, job
```

If all pain-point searches return zero, first test whether the project contains product-context mentions at all:

```text
faucet
shower
bathroom
plumbing
sink
toilet
```

If these product-context searches also return zero or almost zero, the Brand24 project was configured too broadly around competitor brand names and is collecting irrelevant brand/name matches. Reconfigure Brand24 keywords as product-context phrases:

```text
GROHE faucet, GROHE shower, GROHE bathroom, GROHE kitchen faucet, Moen faucet, Moen shower, Moen bathroom, Moen kitchen faucet, Delta Faucet, Delta shower, Delta bathroom faucet, Kohler faucet, Kohler shower, Kohler bathroom, Kohler toilet, Hansgrohe faucet, Hansgrohe shower, American Standard faucet, American Standard toilet, Pfister faucet, Pfister shower
```

Keep these exclusions:

```text
darmstadt, Grohe Hell, music, album, concert, football, school, stock, investor, earnings, hiring, job, airline, airport, Delta Air, Delta Airlines, Kohler engine, generator
```

After reconfiguration, wait for new mentions or historical backfill, then re-run the pain-point searches. Treat the original broad competitor project as unusable for pain-point analysis if it has many mentions but zero product-context hits.

### 优先只做 3 个核心监控对象

如果试用版关键词或项目数量有限，先不要建 5 个 alert。用 3 个就够：

| 优先级 | 测试对象 | 目的 | 是否必须 |
|---|---|---|---|
| 1 | KES 品牌噪音测试 | 验证 `KES` 这个短词能否被工具有效过滤 | 必须 |
| 2 | 北美竞品与痛点 | 验证竞品覆盖、投诉素材、内容营销信号 | 必须 |
| 3 | 埃及市场阿拉伯语 | 验证非英语市场覆盖和本地源质量 | 必须 |
| 4 | 销售线索 | 验证 Awario Leads / Brand24 关键词匹配 | 可选 |
| 5 | 品类趋势 | 验证趋势洞察 | 可选 |

### 公平性原则

- 两个平台尽量同一天、同一时间创建。
- 同一测试对象使用同一组核心关键词。
- Awario 可以使用 Boolean；Brand24 使用最接近的关键词 + excluded keywords。记录差异，而不是强行抹平差异。
- 每个平台每天固定同一时间记录一次数据，建议香港时间 10:00-11:00。
- 只比较 2026-06-05 至 2026-06-11 的并行窗口；2026-06-12 以后只评价 Brand24 独有能力。

## Keyword setup

### Alert 1: KES 品牌噪音测试

目的：测试 `KES` 作为短品牌词时的真实可用性。

Awario 建议配置：

```text
"KES" OR "keshome" OR "KES Home" OR "keshome.com"
```

Awario 排除词：

```text
election, politics, school, football, soccer, exam, "Kenya shilling", "key enabling", "knowledge exchange", "KES unit", "general mills"
```

Brand24 建议配置：

```text
"KES"
#KES
"KES Home"
keshome
keshome.com
```

Brand24 排除词：

```text
"general mills"
"Kenya shilling"
"knowledge exchange"
"key enabling"
school
exam
football
soccer
```

记录重点：

| 字段 | 说明 |
|---|---|
| total_mentions | 总提及 |
| relevant_mentions | 与 KES 品牌、产品、网站、销售渠道相关 |
| noise_mentions | Kenya shilling / school / unrelated KES 等 |
| noise_rate | noise_mentions / 抽样数 |
| missed_obvious_mentions | 手动搜索能找到但工具没抓到的明显提及 |

### Alert 2: 北美竞品与痛点

目的：验证工具能否捕捉可用于竞品情报和内容营销的真实消费者信号。

核心竞品词：

```text
GROHE
Moen
Delta Faucet
Kohler
Hansgrohe
American Standard
Pfister
```

痛点词：

```text
leaking
rust
poor quality
stopped working
disappointed
waste of money
lasted only
broke after
defective
cheap plastic
hard to install
```

Awario 如果支持 Boolean，用：

```text
("GROHE" OR "Moen" OR "Delta Faucet" OR "Kohler" OR "Hansgrohe" OR "American Standard" OR "Pfister")
AND
(leaking OR rust OR "poor quality" OR "stopped working" OR disappointed OR "waste of money" OR "lasted only" OR "broke after" OR defective OR "cheap plastic" OR "hard to install")
```

Brand24 如果不能做 Boolean，用两层办法：

1. 先把竞品品牌词作为 keywords。
2. 用过滤、search in mentions、或手工抽样统计痛点词命中。

记录重点：

| 字段 | 说明 |
|---|---|
| competitor_mentions | 竞品总提及 |
| pain_point_mentions | 明确投诉 / 缺陷 / 安装痛点 |
| useful_quotes | 可用于内容策略的高质量原文，不超过短摘录 |
| source_mix | Reddit / YouTube / News / Blog / Forum / X / TikTok 等 |
| actionability_score | 1-5，能否转化为产品、内容、客服、竞品策略动作 |

### Alert 3: 埃及市场阿拉伯语

目的：验证两个工具对埃及市场、本地语言、本地源的覆盖。

建议关键词：

```text
ستائر
اكسسوارات ستائر
مفصلات
قضبان ستائر
ستائر رول
بلاك اوت
رايف تكستايل
شتا
```

可补充英文转写：

```text
curtain Egypt
curtain rods Egypt
blackout curtains Egypt
Raif Textile
Shatta curtains
```

记录重点：

| 字段 | 说明 |
|---|---|
| arabic_mentions | 阿拉伯语 mention 总量 |
| egypt_relevant_mentions | 与埃及市场相关的数量 |
| local_source_count | 埃及本地媒体、论坛、社媒、店铺、页面数量 |
| category_relevance | 是否真的是窗帘 / 轨道 / 五金 / 软装 |
| sentiment_quality | 阿拉伯语情感识别是否明显错误 |

### Optional Alert 4: 销售线索

只有在试用版允许更多项目时创建。

```text
"looking for bathroom faucet"
"recommend shower system"
"best kitchen faucet"
"bathroom renovation need"
"wholesale bathroom fixtures"
"property manager bathroom upgrade"
"airbnb bathroom fixtures"
```

Awario 如果支持 Boolean：

```text
("looking for" OR recommend OR "which" OR "best" OR "should I buy" OR "anyone tried")
AND
("bathroom faucet" OR "shower system" OR "kitchen faucet" OR "towel warmer" OR "bidet" OR "rain shower")
```

### Optional Alert 5: 品类趋势

只有在试用版允许更多项目时创建。

```text
"bathroom trends"
"kitchen trends"
"bathroom renovation"
"kitchen renovation"
"matte black"
"brushed gold"
"smart bathroom"
"water saving"
"low flow"
"ADA compliant bathroom"
```

## Daily plan

### Day 0: 2026-06-05 配置与基线

目标：把两个工具放到同一个起跑线，并记录所有试用限制。

步骤：

1. 在 Brand24 和 Awario 创建同名项目 / alert。
2. 优先只创建 3 个核心对象：KES 品牌、北美竞品、埃及阿拉伯语。
3. 填入排除词，截图保存。
4. 记录每个平台的限制：项目数、关键词数、是否支持排除词、是否支持 Boolean、是否能选历史数据、是否有 API / export。
5. 等 30-60 分钟，看是否有初始数据。
6. 建立记录表。

Day 0 结论必须回答：

| 问题 | 记录 |
|---|---|
| 两个平台都成功建好 3 个核心监控了吗？ |  |
| 是否有任何一个工具因为 trial 限制无法完成公平对测？ |  |
| Brand24 排除词是否能保存并生效？ |  |
| Awario Boolean 是否能保存并生效？ |  |
| 是否能导出 CSV / Excel？ |  |

### Day 1: 2026-06-06 初始噪音校准

目标：先解决噪音，不急着评价覆盖。

步骤：

1. 每个平台每个 alert 记录 mention 总数。
2. 对 KES 品牌 alert 抽样 20 条，人工标注 relevant / noise / unclear。
3. 如果 KES 噪音率 > 50%，立即补排除词。
4. 对埃及 alert 抽样 10 条，看是否真的与埃及和窗帘 / 五金相关。
5. 截图源分布。

### Day 2: 2026-06-07 来源覆盖检查

目标：看两个工具抓到的数据来自哪里。

步骤：

1. 记录每个 alert 的 source breakdown。
2. 单独记录 Reddit、YouTube、News/Blog、Forum、X、Facebook/Instagram、TikTok、LinkedIn、Telegram 是否出现。
3. 对北美竞品 alert 抽样 20 条，标注是否有痛点词和可行动信息。
4. 记录每个平台从打开 dashboard 到找到 3 条有用 mention 的耗时。

### Day 3: 2026-06-08 导出与数据结构测试

目标：验证它们能否进入 KES ops / research workflow。

步骤：

1. 尝试 CSV / Excel / PDF 导出。
2. 记录导出字段：url、date、source、author、language、country、sentiment、reach、engagement、snippet。
3. 如果有 API 设置页，记录是否可生成 token，但不要把 token 写入 wiki。
4. 比较导出数据是否足以做下游分析。

最低可接受字段：

```text
date
source
url
title or text/snippet
sentiment
language
```

如果连这些都没有，工具只能作为人工 dashboard，不能作为数据管道。

### Day 4: 2026-06-09 情感分析与 AI 摘要测试

目标：验证自动判断是否可信。

步骤：

1. 每个平台各抽样 30 条 mention。
2. 人工标注 sentiment: positive / neutral / negative / unclear。
3. 对比工具自动 sentiment。
4. 如果 Brand24 有 AI summary / insight，记录它是否提出了真实有用的模式，而不是泛泛总结。
5. 对阿拉伯语 mention 单独检查 10 条 sentiment。

通过标准：

| 指标 | 可接受 |
|---|---|
| 英文 sentiment 准确率 | >= 70% |
| 阿拉伯语 sentiment 准确率 | >= 50%，低于此只能作为参考 |
| AI summary | 至少产生 3 条可验证、可行动观察 |

### Day 5: 2026-06-10 线索与内容素材测试

目标：看工具是否能产生业务动作，而不只是 dashboard 数字。

步骤：

1. 从每个平台找 10 条“最有业务价值”的 mention。
2. 分类为：品牌声誉、竞品弱点、销售线索、内容选题、产品痛点、埃及市场情报。
3. 记录每条 mention 的下一步动作。
4. 统计每个平台找到 10 条有效素材所需时间。

判断：

| 结果 | 含义 |
|---|---|
| 30 分钟内找不到 5 条有效素材 | 日常业务价值偏低 |
| 有效素材多但噪音也高 | 需要算人工筛选成本 |
| 能稳定出现竞品痛点 / 线索 | 可进入周度情报流程 |

### Day 6: 2026-06-11 公平对测收口

目标：结束 7 天并行窗口，准备初判。

步骤：

1. 导出两个工具 2026-06-05 至 2026-06-11 的全部数据。
2. 汇总三大核心 alert 的 mention 数、相关数、噪音率、源分布、有效素材数。
3. 标记两个工具的独有 mention：只在 Awario 出现、只在 Brand24 出现。
4. 写出临时结论：继续 Brand24 独有测试 / 购买 Awario / 购买 Brand24 / 暂不购买。

### Day 7: 2026-06-12 决策检查点

目标：避免试用期结束前没有动作。

输出一页短报告：

1. 哪个工具暂时领先？
2. 领先原因是覆盖、噪音、导出、AI、独有来源，还是使用体验？
3. 是否需要在 Awario 试用结束前购买或取消？
4. Brand24 是否值得继续测试到 Day 14？

### Day 8-14: 2026-06-13 至 2026-06-19 Brand24 独有能力

如果 Brand24 试用仍有效，后半段只测它的溢价来源：

| 能力 | 验证问题 |
|---|---|
| LinkedIn | 是否抓到 KES / 竞品 / B2B 相关真实提及？ |
| TikTok | 是否比手动 TikTok / Creative Center 有实质增量？ |
| Telegram | 是否出现与家居、五金、窗帘、埃及市场有关的信号？ |
| Podcast | 是否有真实品牌 / 竞品提及，还是几乎为空？ |
| AI reports | 是否能节省人工周报时间？ |
| Influencer / Source ranking | 是否能找到值得跟进的账号 / 网站 / 作者？ |

## Recording template

### Daily counts

| Date | Tool | Alert | Total mentions | Relevant | Noise | Unclear | Noise rate | Notes |
|---|---|---|---:|---:|---:|---:|---:|---|
| 2026-06-05 | Awario | KES Brand |  |  |  |  |  |  |
| 2026-06-05 | Brand24 | KES Brand |  |  |  |  |  |  |

### Source mix

| Date | Tool | Alert | Reddit | YouTube | News/Blog | Forum/Web | X | FB/IG | TikTok | LinkedIn | Telegram | Other |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|

### Mention quality sample

| Date | Tool | Alert | URL | Source | Language | Tool sentiment | Human sentiment | Label | Actionability | Note |
|---|---|---|---|---|---|---|---|---|---:|---|

Label options:

```text
brand-relevant
competitor-pain
lead
content-idea
product-insight
egypt-market
noise
unclear
```

Actionability score:

| Score | Meaning |
|---|---|
| 1 | 无动作价值 |
| 2 | 可读但不值得记录 |
| 3 | 可进入周报 |
| 4 | 可转为内容 / 产品 / 销售动作 |
| 5 | 需要立即跟进 |

### Export / API audit

| Tool | CSV export | Excel export | PDF report | API token | API accessible in trial | Required fields present | Notes |
|---|---|---|---|---|---|---|---|
| Awario |  |  |  |  |  |  |  |
| Brand24 |  |  |  |  |  |  |  |

## Scoring model

总分 100 分。

| 维度 | 权重 | 评分方法 |
|---|---:|---|
| 相关覆盖 | 25 | 三个核心 alert 的 relevant_mentions，按相对领先打分 |
| 噪音控制 | 20 | KES 品牌噪音率越低越高分 |
| 来源质量 | 15 | Reddit / YouTube / Forum / Egypt local / B2B sources 的真实有用程度 |
| 数据导出与集成 | 15 | CSV/API 字段完整、可自动化、可进入 ops |
| 独有功能增量 | 10 | Brand24 独有来源或 Awario Boolean/Leads 是否产生实际素材 |
| 使用效率 | 10 | 找到有效 mention 的时间、过滤体验、dashboard 可读性 |
| 成本匹配 | 5 | 以当前业务规模是否值得付费 |

评分表：

| Dimension | Awario | Brand24 | Notes |
|---|---:|---:|---|
| 相关覆盖 /25 |  |  |  |
| 噪音控制 /20 |  |  |  |
| 来源质量 /15 |  |  |  |
| 数据导出与集成 /15 |  |  |  |
| 独有功能增量 /10 |  |  |  |
| 使用效率 /10 |  |  |  |
| 成本匹配 /5 |  |  |  |
| Total /100 |  |  |  |

## Final report outline

第 7 天输出：

```text
# KES Brand24 / Awario Trial Test Result

## Recommendation

Buy / do not buy / continue testing / defer.

## Why

1. Coverage:
2. Noise:
3. Source quality:
4. Integration:
5. Cost:

## Evidence

- 7-day counts
- Top useful mentions
- Noise sample
- Export/API audit
- Screenshots

## Decision

- Primary tool:
- Backup / supplemental tools:
- Monthly cost:
- First 30-day operating routine:
```

## Failure modes

| Failure mode | Response |
|---|---|
| KES keyword returns mostly unrelated `KES` results | Add exclusions; if still high, monitor `keshome` / `KES Home` / URL instead of bare KES |
| Trial version blocks enough projects | Keep only 3 core tests: KES, competitors, Egypt |
| One tool starts historical backfill and the other does not | Separate historical data from forward-looking 7-day test |
| Export not available | Screenshot and manual sample only; mark integration score low |
| Sentiment looks wrong | Treat sentiment as directional only; use human labels for final decision |
| Arabic data is low quality | Do not infer “Egypt has no demand”; infer only “this tool is weak for Arabic/Egypt sources” |
| Brand24独有来源为0 | 不为 LinkedIn/TikTok/Telegram 付溢价 |
| Awario Boolean 太复杂导致漏数据 | 建一个宽松版本和一个精确版本，分别记录 coverage 与 noise |

## Review notes

- 本协议基于 2026-06-05 的试用界面截图与既有 wiki 调研整理。
- 具体套餐权限、API 权限、历史数据权限必须以当次试用账号实测为准。
- 不把工具官方宣传直接当事实；只把实际抓到的数据、导出字段、人工标注结果作为购买依据。

## Related pages

- [Awario vs Brand24 对测计划（深度版）](../syntheses/kes-awario-brand24-testing-plan.md)
- [KES 社媒监控工具深度评估](../syntheses/kes-social-media-monitoring-tool-evaluation.md)
- [Awario 能为 KES 提供什么数据](../syntheses/awario-data-capabilities-for-kes-2026-06-04.md)
- [KES SNS 社媒监控全案整合文档](../syntheses/kes-sns-monitoring-master-doc.md)

## Sources

- Kenny provided screenshots of Brand24 and Awario trial project settings, 2026-06-05.
- Existing wiki synthesis pages listed above.
