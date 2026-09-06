---
type: product
status: draft
owner: strategy
created: 2026-07-21
updated: 2026-07-21
visibility: team
confidence: medium-high
officiality: draft
domain: product
domains: [drinking-faucet, air-gap, assumptions, risk, tracker]
source_count: 40
review_cycle: monthly
verification_status: working
related:
  - ./drinking-faucet-air-gap-go-no-go-memo-v1.md
  - ./drinking-faucet-air-gap-evidence-register.md
  - ./drinking-faucet-z506-baseline-and-margin-audit.md
---

# Drinking Faucet / Air-Gap 假设台账

## 这页为什么存在

记录 [No-Go 备忘录](./drinking-faucet-air-gap-go-no-go-memo-v1.md) 建立在哪些假设上。
**任一 Critical 假设被推翻，必须更新备忘录，而不是私下重新解释。**

## A 组：支撑 No-Go 的假设

| ID | 假设 | 重要性 | 当前置信度 | 如何验证 | 若为假的后果 |
|---|---|---|---|---|---|
| A-01 | BA `search_frequency_rank` 能代表美国站真实需求量级 | Critical | high | 平台已长期使用该口径；可与 Keepa / 第三方词量交叉 | 整个需求侧论证失效，需重做 |
| A-02 | `air gap ro faucet` 约 127 万排名意味着盘子太小、不足以支撑一个 SKU | Critical | medium-high | 找一个已知量级的对照 SKU，看其主词排名与实际月销的映射关系 | 可能低估长尾变现能力；需重新评估 |
| A-03 | air-gap 的主导失效模式（堵塞、喷溅、噪声）源自架构与安装，工厂无法通过设计消除 | Critical | medium-high | 样板拆解 + 台架测试（若翻案才做） | "架构性差评不可控"这条腿倒塌，风险可控性上升 |
| A-04 | 中国品牌标题写 "Non-Air Gap" 是因为买家会主动筛掉它 | High | medium | 需要卖家访谈或 A/B 证据；目前是推断 | 该信号改为中性，但不影响 A-01/A-02 |
| A-05 | 法规只要求 "air gap or air gap device"，不要求龙头形态 | Critical | high | UPC/IPC §611.2 原文已直读（2018/2021/2024 三版） | 若某辖区强制龙头形态，出现合规刚需位，需重评 |
| A-06 | KES 无法在架构上消除喷溅/噪声 | High | medium | 工程可行性研究（未做） | 若能消除且可专利化，这将是真正的差异化，No-Go 应翻案 |
| A-07 | Z506 当前的断货 + 负毛利 + 认证三个问题，优先级高于任何新变体 | Critical | high | 已由内部数据验证 | 若三者已解决，研发产能释放，可重议 |

## B 组：已被本次调查证伪的假设（存档，防止翻案）

| ID | 原假设 | 判定 | 证伪依据 |
|---|---|---|---|
| B-01 | 存在 Kraus / Moen / Delta / Ultra Faucets 等强势 air-gap 竞品 | **证伪** | 七个点名品牌六个无 air-gap 专用产品；仅 Waterstone 真做集成式，$291–$697 |
| B-02 | "air gap 藏在龙头底座内"被在世专利覆盖，有 IP 风险 | **证伪** | US7357147B2（Tomlinson 系，权利要求正是该构型）2025-09-09 Expired-Lifetime；US4454891A / US5305778A / US5713385A 均失效 |
| B-03 | 无桶 RO 的崛起在架构上消灭了空气隙龙头 | **证伪** | 主变量是销售渠道非有无水箱。A.O. Smith SmartFlow（Lowe's，标配空气隙）与 Aquasana AQ-SFRO2（DTC，不带）为同一膜平台贴牌 |
| B-04 | air-gap 只在部分辖区（如加州）强制 | **证伪** | UPC §611.2 与 IPC §611.2 均强制，三版原文未变。真正的分歧只是认可标准不同 |
| B-05 | 加州洗碗机空气隙条款（CPC 807.3）延伸到 RO | **证伪** | 该条不延伸到 RO。UPC 2015 第 8 章全文 grep，water treatment / osmosis 零命中；`807.4` 不存在 |
| B-06 | Minnesota DOH 明确否定柜下空气隙装置 | **证伪（属选择性引用）** | 被否的是 under-sink air **break**（直连下水道），不是 air gap **device**。同一文件把 "Air Gap Device Installation Example" 作为**正确**示例 |
| B-07 | 专业人士（装维方）普遍反对空气隙龙头 | **证伪** | 反对声主要来自零售商（Pure Water Products、Frizzlife）；装维方（Filters Fast 论坛 Gary Slusser、WOWOW）仍推荐 |
| B-08 | 空气隙龙头正在被行业淘汰 | **部分证伪** | 无任何厂商 / 标准机构 / 行业协会声明淘汰；WQA 2025 文档仍将其列为 RO 标准组件。正确表述是「份额萎缩」而非「品类消失」 |

## C 组：未能验证、必须当作未知的项

**这些是本次调查的诚实缺口，不要在商业计划中填入猜测数字。**

| ID | 未知项 | 为何重要 | 为何没查到 |
|---|---|---|---|
| C-01 | air-gap vs non-air-gap 在美国 RO 新装中的**数值市占率** | 决定萎缩的**幅度** | 全网无任何可信来源发布过。经销商博客互相打架 |
| C-02 | `air gap faucet` 的第三方关键词月搜索量 | 交叉验证 A-01 | Ahrefs / Semrush / 任何可访问来源均无。Google Trends 全部 HTTP 429 |
| C-03 | 大卖场（Home Depot / Lowe's / Ferguson）的货架 SKU 结构 | 专业电商信号不能替代大卖场 | 全部 403 |
| C-04 | Amazon 上 air-gap vs non-air-gap 的**评分分布对比** | 直接量化 A-03 | Amazon 评论页 403/503；Keepa / camelcamelcamel 不可达 |
| C-05 | 无桶 vs 罐式 RO 的美国市场份额 | 支撑 B-03 的修正 | 仅有内容农场级报告，口径自相矛盾，已拒绝引用 |
| C-06 | 2027 UPC 是否有针对 §611.2 的提案 | 判断法规走向 | ROP monograph >10MB 抓取失败 |
| C-07 | CPC（加州）§611.2 原文 | 加州结论目前是类推 | IAPMO epubs / UpCodes / ICC 三路均被墙 |
| C-08 | IAPMO / NSF / WQA 的实际认证报价 | 任何认证预算 | 三家均不公开报价单 |

## 结论稳健性说明

**No-Go 结论的承重腿是 A-01 / A-02（内部 BA 数据）和 A-03（失效模式），
不依赖 C 组任何未知项。**

C 组的窟窿影响的是"萎缩得多快"这个**幅度**问题，而 No-Go 是个**方向**判断。
外部调研在本次的作用是**解释**为什么内部数据这么冷，不是**证明**它冷。

**若未来有人用"外部数据不全"质疑本结论，正确的回应是：请先反驳 A-01 到 A-03。**

## 复核规则

- Critical 假设在任何"重议 air-gap"的提议出现时必须逐条复核
- 不得仅凭外部博客或供应商说辞关闭 Critical 假设
- C 组任一项若拿到可信数据，应回填本表并评估是否触发翻案条件
