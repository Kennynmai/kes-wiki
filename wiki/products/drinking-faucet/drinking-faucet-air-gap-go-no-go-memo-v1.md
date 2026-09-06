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
domains: [drinking-faucet, air-gap, go-no-go, memo, kes]
source_count: 40
review_cycle: monthly
verification_status: working
related:
  - ./drinking-faucet.md
  - ./drinking-faucet-air-gap-evidence-register.md
  - ./drinking-faucet-assumption-register.md
  - ./drinking-faucet-z506-baseline-and-margin-audit.md
---

# Air-Gap RO 龙头 Go / No-Go 备忘录 — V1

## 决策状态

**当前答案：No-Go。** 不是 conditional，不是"再看看"。

三条独立证据链同向，且没有一条被反向证据推翻。

## 触发问题与它的错误框架

原始提问附带了一份结论，主张：*"图纸能解决管路怎么连接，但无法可靠解决关键量产问题……建议购买至少 3 类样板（常规集成式 / 设计型 / 独立合规装置）。"*

**这份结论回答的是「如果做，怎么降低量产风险」，它已经默认了「做」。** 而待答问题是「值不值得做」。两者的承重假设不同：前者不依赖需求判断，后者依赖。

本备忘录不采信该结论作为前提，并在下文第 3 节直接证伪它的核心主张。

## No-Go 的三条腿

### 1. 需求池不存在 —— 这是最硬的一条

一手数据（`fact_ba_search_terms_weekly`，`amz_us`，近 8 周，42 个匹配词）：

| 词 | search_frequency_rank（越小越热） |
|---|---|
| `pur water filter faucet` | 101,076 |
| `water filter faucet` | 154,856 |
| `drinking water faucet` | 179,824 |
| `reverse osmosis faucet` | 215,089 |
| `ro faucet` | 252,650 |
| **`air gap ro faucet`** | **1,270,126** |

`air gap ro faucet` 是**唯一**有连续存在（36/36 周）的 air-gap 词。其余全是噪声：
`airgap ro faucet` 2,505,820（3 周）、`ro faucet with air gap` 2,742,430（3 周）、
`reverse osmosis faucet with air gap` 2,521,048（**1 周**）。

**比品类头词弱约 8 倍，比裸 `ro faucet` 弱约 5 倍。**

趋势（`fact_ba_search_terms_monthly` 季度最佳排名）：
2025Q2 1,260,222 → Q3 1,368,260 → Q4 1,369,123 → 2026Q1 1,110,567 → 2026Q2 1,488,574。
**五个季度横盘，没有变热。**

KES 份额：42 个词上 `is_own_asin_1/2/3` **全为 False**。三个 Z506 ASIN 的反查在**所有周**只返回 2 行，都在约 250 万排名词的 slot 2/3。词域由 B09XXL2PQB 和 B07MLSVLZH（PUR）占据。

**结论：air-gap 不是需求池，是长尾限定词。**

### 2. 架构性差评不可控 —— 这是对亚马逊卖家最致命的一条

air-gap 的排水段**靠重力不靠压力**（进 1/4"、出 3/8"，中间在龙头底座内破断至大气）。下游任何阻塞都会让水从底座通气孔喷到台面上。

已验证的失效链条：
- RO 浓水析出胶状物（"jelly"）堵管 —— Fresh Water Systems 称此为**最常见原因**
- 水槽食物碎屑倒堵排水鞍座
- 排水管打圈 / 下垂 / 过长 / 压扁
- 缺流量限制器导致过量水进入龙头
- 进水 TDS 越高，堆积概率越大

**这些主因全部是安装质量、水质和下水道状况，不在工厂控制范围内。**

且**咕噜声是架构固有属性，不是缺陷**：每次储水罐补水都有水自由落入槽体再泄流。有用户记录取 16 oz 水后厨房里响 10–12 分钟。Delta 和 Whirlpool 均常设「空气隙噪音/漏水」故障排除文档 —— 大厂长期维护此类页面本身即投诉量的证据。

应用限制：不宜配下嵌水槽（只能配台上盆）；需下水道有足够排量，否则"会从空气隙窗口倒流"。

**风险结构：失效你不负责，差评全记你头上。** 观察到 SpiroPure air-gap 变体评分
4.2★ / 3.6★（快照数据，低置信），已低于硬件类目健康线。

### 3. 同赛道的中国品牌已集体用脚投票

**所有**中国背景 RO 龙头品牌的标题里**直接写着 "Non-Air Gap"**：
VMASSTONE、ESOW、GIMILI、Bifordo、iSpring（GA1-BN / GA1-SS / GB1）、Waterdrop（G3P600/G3P800 配非空气隙智能 LED 龙头）。
未找到 iSpring、Express Water、Home Master、Frizzlife、Geekpure、PureDrop、Hydronix、Waterdrop 的任何 air-gap 变体。

Made-in-China 约 60–70 个 listing tile 中，**没有一条把空气隙当卖点营销**，凡出现该词均为否定式。
**供应商愿意花标题字符去否定一个功能，只发生在买家会主动筛掉它的时候。**

RO 厂商 Pure Water Products 明说自己默认发非空气隙、用单向阀替代，且"法规要求经常被无视"。

## 三条被证伪的假设（含我方自己的）

记录在此，防止后续有人凭直觉翻案。

| 原假设 | 判定 | 修正 |
|---|---|---|
| 存在 Kraus / Moen / Delta / Ultra Faucets 等一批强势现有对手 | **证伪** | 七个点名品牌里六个是空的。Moen 的空气隙是单独配件 #105895；Westbrass 只卖配件盖；Mountain Plumbing 只卖外挂装置；Ultra Faucets 完全没有。唯一真做集成式的是 Waterstone，$291–$697 设计师层 |
| 公开专利已覆盖"集成在龙头底座内的 air gap"，有 IP 风险 | **证伪** | 最贴题的 US7357147B2（Tomlinson 系）**2025-09-09 已 Expired-Lifetime**，核心构型进入公有领域。详见证据台账 |
| 无桶 RO 的崛起在架构上消灭了空气隙龙头 | **证伪** | 分野的主变量是**销售渠道**不是有无水箱。反证：A.O. Smith SmartFlow（Lowe's）标配空气隙，同一膜平台贴牌为 Aquasana AQ-SFRO2（DTC）则不带 |
| air-gap 法规只在部分辖区强制 | **证伪** | UPC §611.2 与 IPC §611.2 **均强制**，2018/2021/2024 三版原文未变。但见下 |

## 法规为什么救不了这个 SKU

这是最容易被误读的一点，单独说明。

UPC §611.2 与 IPC §611.2 都要求 RO 排水"shall enter the drainage system through an
air gap **or an air gap device**"。**法规从来只要求「空气隙」这个功能，从未要求它长成龙头。**

合规的真实约束是两条：
1. 须列名认证（IAPMO PS 65 / NSF 58 / ASME A112.1.3 / CSA B483.1）
2. **位置必须高于水槽溢流边缘**（如 MN Rules 4714.603.4.4）

认证过的台面式/独立空气隙装置同样合规。**所以监管托的是品类地板，不是龙头形态的护城河。**

2021 UPC 第 611 节还在扩容（新增 Table 611.1、611.1.1、611.1.2），无任何放宽动向 ——
**方向是收紧，但收紧的是"要有空气隙"，不是"要有空气隙龙头"。**

## 为什么"买 3 类样板"解决不了问题

直接回应触发问题附带的结论。

样板拆解能测出：排水通道尺寸、溢流路径几何、装配公差、噪声基线、软管弯折半径。这些都是**真实且有价值**的工程信息。

**但它测不出你在亚马逊上会不会因为别人装错而被打差评。** 第 2 节列出的主导失效模式全部在工厂控制范围之外。一只加工完美的 air-gap 龙头照样会收到"漏水到我台面上"和"太吵"的一星评价，因为那是架构属性不是零件缺陷。

即：**样板投资降低的是"做不出来"的风险，而这个项目的主风险是"做出来没人搜、且被差评"。风险管理用错了地方。**

## 什么情况会让这个 No-Go 翻案

写下来是为了让翻案有门槛，不是靠拍脑袋。

1. `air gap ro faucet` 的 BA 排名进入 **40 万以内**并连续 2 个季度维持（当前 127 万）
2. 出现权威数据证明 air-gap 在美国 RO 新装中占比 **>30%**（当前**无任何可信来源**给出该数字）
3. 有辖区把法规从 "air gap **or** air gap device" 收紧为强制龙头形态
4. KES 找到能在架构上消除喷溅/噪声的方案，且该方案可专利化（这将是真正的差异化，但目前无线索）
5. 主线 Z506 已解决断货 + 负毛利 + 认证三个问题，且有闲置研发产能

**在 1–5 全部不成立时，任何"我们再看看 air-gap"的提议都应被本备忘录挡回。**

## 若仍要在 RO 龙头线上加码，正确方向

**非空气隙 + 高设计感外观 + 自有外观专利。**

理由：
- 需求在这一侧（头词 15 万 vs 长尾 127 万）
- 评价风险可控（无重力排水架构）
- Waterdrop / iSpring 正在打这个战场，说明它可成立
- 能与在跑的 `Z506EU.V1.0` 合流，共用认证栈
- ⚠️ **真正的 IP 风险在外观专利**：Delta 等持续获授 USD969970S1、USD1013116S1 等龙头外观专利，且外观专利是 Amazon 龙头类目下架投诉的主要武器。**功能可自由做，造型必须原创。**

## 顺带发现的、优先级高于本议题的三件事

见 [Z506 经营基线](./drinking-faucet-z506-baseline-and-margin-audit.md) 与
[P0 合规敞口](./drinking-faucet-compliance-exposure-p0.md)：

- **P0** 在售 SKU 的 NSF61 / NSF372 / cUPC 记录缺失
- **P1** BS / BZ 两个颜色 2026-07-15 起断货，正在吃掉一条增长中的线
- **P2** 七条在售 listing 中三条低于盈亏平衡（US BK −15.5%、UK BS −28.8%）
