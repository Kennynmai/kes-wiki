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
domains: [drinking-faucet, air-gap, evidence, sources, patents, compliance]
source_count: 40
review_cycle: monthly
verification_status: working
related:
  - ./drinking-faucet-air-gap-go-no-go-memo-v1.md
  - ./drinking-faucet-assumption-register.md
---

# Air-Gap RO 龙头 证据台账

每条论断的来源与置信度。**标注 INFERENCE 的是推断不是事实，不要当数据引用。**

## 1. 内部一手数据（置信度：高）

来源：prod 只读查询，2026-07-21。

| 论断 | 数据 |
|---|---|
| `air gap ro faucet` 排名 1,270,126 | `fact_ba_search_terms_weekly`，amz_us，近 8 周 |
| 品类头词 `water filter faucet` 154,856 | 同上 |
| 其余 air-gap 词全为噪声（1–3 周出现） | 同上，42 个匹配词 |
| 五季度横盘（2025Q2 126万 → 2026Q2 149万） | `fact_ba_search_terms_monthly`（历史仅从 2025-05 起） |
| KES 在 42 个词上 `is_own_asin` 全 False | 同上 |
| Z506 三个 ASIN 反查全周期仅 2 行 | 同上 |
| 词域由 B09XXL2PQB / B07MLSVLZH 占据 | 同上，按 click share |
| Z506 七条在售 listing、三条负毛利 | `mart_listing_health` snapshot 2026-07-17 |
| BS/BZ 2026-07-15 转 oos | 同上 + 库存历史 |
| 2026 run-rate 约为 2025 的两倍 | `fact_product_business_monthly` + `_daily` |
| 在售变体无 NSF61/372/cUPC 记录 | `dim_sku_certification` |
| 无 air-gap 相关立项 | `project` / `rc_*` |

## 2. 专利（置信度：高 — Google Patents 直取）

### 已失效（核心构型进入公有领域）

| 专利 | 标题 | 受让人 | 状态 |
|---|---|---|---|
| [US4454891A](https://patents.google.com/patent/US4454891A/en) | Air gap drain module for RO system | Emerson Electric | **EXPIRED**（1996 失效） |
| [US5305778A](https://patents.google.com/patent/US5305778A/en) | Air gap apparatus | Paul L. Traylor | **EXPIRED — Lifetime**（2011-10-23） |
| [US5713385A](https://patents.google.com/patent/US5713385A/en) | Air gap body for RO system | Paul L. Traylor | **EXPIRED**（2006，费用相关） |
| [US7357147B2](https://patents.google.com/patent/US20060118171A1/en) | **Modular air gap device and faucet including same** | Foodservices Brand Group (Tomlinson) | **EXPIRED — Lifetime（2025-09-09）** |

US7357147B2 是最贴题的一条，权利要求原文：
*"a modular air gap device adapted for selective insertion into an associated faucet body …
the air gap mechanism remains housed completely within the faucet body's internal chamber …
maintaining the faucet's original external appearance."*

**这正是「空气隙藏在龙头底座内」，且已于 2025-09 到期。**

其他失效相关件：[US6971400B1](https://patents.google.com/patent/US6971400B1/en)、
[US5915406A](https://patents.google.com/patent/US5915406A/en)、
[US6651272B2](https://patents.google.com/patent/US6651272B2/en)。

### 在世（需绕开）

**[US11634897B2 — Integrated airgap retrofit body](https://patents.google.com/patent/US11634897B2/en)**
Watkins James David Jr. / Casimir Sienkiewicz。2021-08-05 申请，2023-04-25 授权，
**预计到期 2040-12-13，状态 ACTIVE**。

权利要求 1 指向 *"a retrofit body for a faucet"* —— 一个穿台面的**独立**组件。
龙头本体/手柄内集成出现在从属权利要求与实施例中。

**INFERENCE**：常规集成式设计（按已失效的 Tomlinson art）**应当**不落入其权利要求 1，
因为该权利要求要求一个分立的 retrofit body。**但这需要律师出 claim chart，不能凭本文件开模。**

### 真正的 IP 风险：外观专利

Delta 等持续获授龙头外观专利：[USD969970S1](https://patents.google.com/patent/USD969970S1/en)（2020）、
[USD1013116S1](https://patents.google.com/patent/USD1013116S1/en)（2022）、
[USD1029192S1](https://patents.google.com/patent/USD1029192)、
[USD993364S1](https://patents.google.com/patent/USD993364)。

**INFERENCE（高置信）**：对中国制造商而言，air gap 的实用专利 FTO 是干净的，
但抄 Waterstone / Delta / Tomlinson 的**形态**是实打实的外观专利与商业外观风险，
且外观专利是 Amazon 龙头类目下架投诉的主要武器。**功能可自由做，造型必须原创。**

## 3. 法规（置信度：高 — 条文原文；加州部分为推断）

| 规范 | 条号 | 原文要点 |
|---|---|---|
| **UPC** | §611.2 Air Gap Discharge | "…through an air gap in accordance with Table 603.3.1 **or an air gap device** in accordance with Table 603.2, **NSF 58 or IAPMO PS 65**" |
| **IPC** | §611.2 Reverse Osmosis Systems | "…through an air gap **or an air gap device** that meets the requirements of **CSA B483.1 or NSF 58**" |

来源：[up.codes/s/reverse-osmosis-systems](https://up.codes/s/reverse-osmosis-systems)（2018/2021/2024 三版同文）、
[up.codes/s/air-gap-discharge](https://up.codes/s/air-gap-discharge)。

**唯一实质分歧**：IPC 不认 IAPMO PS 65，UPC 不认 CSA B483.1。合规声明必须同时点明标准与辖区。

州采纳（**likely，口径有出入**）：IPC 约 34–37 州；UPC 约 11–12 州
（AK/CA/HI/ID/IA/MN/MT/NM/ND/SD/WA/OR）。ICC 官方 map 403 抓不到。
**但对本议题不重要 —— 两码都要求。**

位置约束：**空气隙须高于水槽溢流边缘**（MN Rules 4714.603.4.4）。
纯柜下、低于台面的装置无论是否认证都不合规。
明令禁止：排水鞍座直连（MN 4714.310.1）、high loop / standpipe（air break 不够）。
来源：[MN DOH POU RO factsheet](https://www.health.state.mn.us/communities/environment/water/docs/factsheet/pointofuse.pdf)。

演进方向：2021 UPC 第 611 节**扩容**（新增 Table 611.1、611.1.1 碱性设备须符 IAPMO IGC 322、
611.1.2 阻垢须符 Z601），611.2 未松动。**无任何放宽动向。**

⚠️ **已证伪的错误说法**（曾在初轮调研中出现，存档以防复发）：
- 「条款在 UPC 第 8 章 807.4」—— 第 8 章全文 grep，water treatment / osmosis 零命中，`807.4` 不存在
- 「加州洗碗机空气隙条款延伸到 RO」—— CPC 807.3 是洗碗机条款，不延伸
- 「MN 否定柜下空气隙装置」—— 被否的是 air **break** 不是 air gap **device**

⚠️ **未直读**：CPC §611.2 原文（IAPMO epubs / UpCodes / ICC 三路被墙），加州结论属类推。
2027 UPC ROP monograph >10MB 抓取失败，未确认是否有 §611.2 提案。

## 4. 认证（置信度：中高 — 要求已验证，成本未验证）

必需项：NSF/ANSI/CAN 61（材料浸出）、NSF/ANSI 372（≤0.25% 铅）、
cUPC/IAPMO R&T listing（压力/密封/结构/流量）、CA AB1953 / Prop 65。
**北美所有示范规范均要求第三方列名认证。**

**air gap 额外拉进：**
- **ASME A112.1.2**（Air Gaps in Plumbing Systems）、**ASME A112.1.3**（Air Gap Fittings）
- 空气隙尺寸 = **不小于出口有效开口直径的 2 倍，或 1 英寸，取大者**
- **NSF/ANSI 58 的空气隙龙头专项测试**：龙头浸水，出口侧抽 **85 kPa（25 inHg）** 真空验证无回吸
  （来源 [WC&P](https://wcponline.com/2017/09/15/requirements-air-gap-faucets/) 页面 403，
  内容经搜索索引恢复 —— **中置信，建议购买标准原文确认**）

**INFERENCE**：air gap 不需要**另开一张 listing**，但增加了测试项、试样数和失败面。

⚠️ **成本与周期：多数未公开。**
- IAPMO R&T **不公开报价单**（[FAQ](https://iapmort.org/certification-services/frequently-asked-questions)）
- 初次工厂审核在提交后 **30 天内**；证书 **1 年有效、年费**；**龙头类工厂审核每年两次**
- 周期"**several months**"
- WQA Gold Seal 是可接受的替代认证机构，同样不公开报价

⚠️ **不要使用的数字**：某聚合站称"单项净水认证 $100,000–$200,000" ——
那是**净水系统性能认证（NSF 42/53/58）**的数字，不适用于龙头，**应丢弃**。

⚠️ **INFERENCE（估算，非来源）**：NSF61 + 372 + cUPC + ASME A112.1.2/.3 + NSF 58 真空测试，
加每年两次工厂审核，量级**可能**是初次数万美元、每年数千美元、周期 3–6 个月。
**进商业计划前必须向 IAPMO R&T、WQA 和国内代理直接询价。**

### 欧盟 / 英国（时机很差）

- **UK WRAS**：Water Supply (Water Fittings) Regulations 1999 第 4 条强制，材料测试 BS 6920
- **德国 DVGW / KTW-BWGL**：化学迁移测试 **8–12 周**；DVGW W270 / EN 16421 微生物测试 **4 个月**
- **EU 制度更替迫近**：Directive (EU) 2020/2184 第 11 条的欧盟正面清单（EUPL）
  **2026-12-31 立法定稿**，**2027-01-01 起**从各国方案（ACS / DVGW / WRAS / KIWA）过渡

**INFERENCE**：2026 年为新品做欧盟饮用水认证 = 认证一个即将被取代的旧体系，
可能需要重新资质化。**窗口很差** —— 这一条对在跑的 `Z506EU.V1.0` 同样适用，值得单独评估。

## 5. 竞争格局（置信度：中 — 专业渠道已验证，Amazon 为快照）

⚠️ **Amazon 商品页与搜索页无法直接抓取**（HTTP 500/503，或仅返回无价格/评分的头部 HTML）。
下文 Amazon 的价格、评分、评论数**来自 Google 搜索快照与零售商镜像，属低置信**。
零售商站点（Fresh Water Systems、Waterstone、US Water Systems、SupplyHouse）与
Google Patents 抓取干净，为最高置信来源。

**最干净的量化点**（专业渠道明确区分两类）：

| 类别 | SKU 数 | 品牌 | 价格带 |
|---|---|---|---|
| [RO 空气隙龙头](https://www.freshwatersystems.com/collections/ro-drinking-water-air-gap-faucets) | **23**（14 有货） | neoPure, Watts, Tomlinson, LiKuan, QMP, Mountain Plumbing | **$26.30 – $126.70** |
| [非空气隙饮水龙头](https://www.freshwatersystems.com/collections/drinking-water-faucets) | **37** | Tomlinson, neoPure, Mountain Plumbing, LiKuan, Waste King, Solventum, Waterstone, Watts, Everpure | $3.80 – $353.99 |

**点名品牌核查结果**：

| 品牌 | 实情 |
|---|---|
| Kraus / Delta / Ultra Faucets | **无 air-gap 专用产品** |
| Moen | RO 龙头的空气隙为**单独配件 #105895**；Sip 系列 F7660/F7620/F7600 有内置 |
| Westbrass | 只卖空气隙**盖/维修件**（D201-1 系列） |
| Mountain Plumbing | 只卖**外挂**空气隙装置（AG600S 已停产、AG1800/AG1850 需**两个**台面孔） |
| Waterstone | **唯一真正的集成式玩家**，$291–$697；但 RO 专用 2100 已下架 |
| Kohler | 71 款饮水龙头中**零**空气隙 |
| Watts | **本体内置，仅存的坚持者**（PWFCT303 双版本） |

**中国背景品牌**：VMASSTONE、ESOW、GIMILI、Bifordo、iSpring、Waterdrop 等
**全部在标题里写 "Non-Air Gap"**。Made-in-China 约 60–70 个 tile 无一以空气隙为卖点。

**渠道分野（本次最重要的机制修正）**：

- **DIY / DTC 电商**已基本完成去空气隙化 —— Waterdrop G3P800、iSpring RCC7、
  APEC ROES-50（空气隙为 **$40.95 选配**）、Home Master TMAFC（"upon request"）、
  Frizzlife PD600（全手册 "air gap" 零命中）、Express Water、Aquasana AQ-SFRO2
- **经销商 / 大牌渠道**仍默认装 —— Culligan Aqua-Cleer、EcoWater ERO-375、
  Pentair FreshPoint GRO-350B、AO Smith AOS-HERO-CHR、RainSoft Ultrefiner Elite
  （**2025 年 2 月修订版手册仍写 "require an air gap faucet"**）
- **最干净的反证**：A.O. Smith SmartFlow（Lowe's，标配空气隙）与
  Aquasana AQ-SFRO2（DTC，不带）是**同一膜平台**贴牌
- **Kinetico K5** 并行给出两条路径，空气隙套件为独立料号 #12961A（选配）

**台面式 RO 结构性归零**：AquaTru、Waterdrop A1/N1、Bluevua ROPOT、SimPure Y7P、
APEC ROCT-Plus **完全不接排水管**，物理上不可能有空气隙龙头。

**无罐 RO 的流量不兼容**（EcoWater 官方支持库，经 Zendesk 公共 JSON API 直取双重确认）：
> "We don't recommend using the faucet air gap if installing an ERO Tankless 485 — **it will flow too fast and the faucet won't be able to keep up.**"
> "Do not connect drain tubing to the RO faucet's air gap. **The drain flow rate from this system is too high for it.**"

行业应对是出**独立空气隙配件**：AirGap International AG200-X07（2.5 GPM）明确标注
"**not** compatible with reverse osmosis faucets with air gap"。

⚠️ **反向数据**：Waterdrop G3P800 手册同时收录两种安装法。
流量不兼容目前是 **EcoWater 单厂立场，未确证为行业共识**。

## 6. 失效模式（置信度：高 — 厂商自建故障排查内容）

- **GE Appliances** 专设知识库条目「Reverse Osmosis - Air Gap Hole Leaking」
- **Delta** 专设「[Air Gap Hissing](https://support.deltafaucet.com/s/article/Air-Gap-Hissing)」
- **Whirlpool** 专设「Leaking Faucet / Noisy Air Gap」
- **[Fresh Water Systems](https://www.freshwatersystems.com/blogs/blog/air-gap-leak)**：
  *"The **most common cause** of an air gap leak is a clogged drain line… Gravity is the only force that moves water… so any resistance causes the water to back up and leak from the air gap hole."* 点名生物膜/"jelly"堆积机制
- **[Frizzlife（厂商）直接劝退](https://www.frizzlife.com/blogs/guide/should-you-buy-a-reverse-osmosis-air-gap-faucet)**：
  *"You **should not** choose it if… code does not require an air gap and you want the simplest, quietest setup."*
- **FilterDealers** 的 "non air gap faucets" 分类根本不是产品线，而是一篇
  《Air Gap Faucet Bypass》改装教程，理由是"可以让吵闹的空气隙龙头安静下来"

**INFERENCE**：大厂长期维护此类专题页本身即慢性投诉量的证据。

⚠️ **反向证据（不能只讲一边）**：
- Filters Fast 论坛专家 Gary Slusser：*"The gurgling is **not a problem, it's normal**… You **should not** change the air gap faucet."*
- WOWOW（龙头厂商）承认三项缺点后仍称"管道工强烈推荐 RO 系统使用空气隙龙头"
- Houzz 案例：用户为降噪换成柜下装置，**半年后柜下装置堵塞漏成一滩水**；另一案例换成非空气隙后**仍然咕噜 10–12 分钟**
- QMP 把「空气隙漏水/噪音」列为 RO 四大问题的**第 4 位**（第 1 位是流量慢）

**诚实判读**：跨 Terry Love / Houzz / Filters Fast 约半打独立主题帖 ——
**真实存在但量级温和**，不是压倒性痛点。
且**「专业人士反对空气隙龙头」这一假设不成立** ——
反对声主要来自零售商，装维方仍推荐。

## 7. 市场规模（置信度：低 — 仅一条可用）

**唯一 VERIFIED**：北美 POU 水处理 **$2.36B (2025) → $3.03B (2030)，CAGR 5.12%**，
RO 为技术端最大，**免安装 free-standing 设备在 2024 年占设备类型最大份额**
（[MarketsandMarkets](https://www.marketsandmarkets.com/PressReleases/north-america-point-of-use-water-treatment.asp)）。

方向参考（**低层级发布商**）：无罐 RO ~9.2% CAGR、台面 RO ~10.1% CAGR。
**模式**：增长最快的两个细分（~9–10%）都是"少龙头"或"无龙头"的，整体基线仅 ~5%。

**反向拉力（真实）**：EPA 2024 年 PFOA/PFOS 4.0 ppt 强制限值落地，RO 是住宅端主流对策；
WQA 2025 报告称水处理产品保有量较 2021 年 **+35%**；
且 **WQA 2025 年文档中仍将 "air gap faucet" 列为 RO 系统标准组件**。

⚠️ **明确拒绝引用**：verifiedmarketreports / snsinsider 等内容农场级报告，
数字内部自相矛盾（"无罐 RO $1.5B" vs "RO Tanks $4.19B" 口径不可比）。

⚠️ **清晰的空结果**：**没有任何厂商、标准机构、行业协会或行业媒体声明空气隙龙头正在被淘汰。**

## 8. 本调查未能填上的窟窿

见[假设台账 C 组](./drinking-faucet-assumption-register.md)。摘要：

Google Trends 全部 429 · `air gap faucet` 关键词量全网无来源 ·
Amazon/HD/Lowe's 评论与 BSR 全部 403/503 · Reddit 工具层被封 ·
2027 UPC monograph 抓取失败 · CPC 原文被墙 · Alibaba 返回空 JS 壳 ·
IAPMO/NSF/WQA 报价不公开。

**这些窟窿影响"萎缩幅度"，不影响"方向"判断 ——
因为方向判断的承重腿是内部 BA 数据，不受抓取失败影响。**
