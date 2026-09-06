# 活性黄铜（Unlacquered Brass）饰面立项评估报告 — NO-GO

**创建日期**: 2026-07-20
**调研范围**: 美国市场（amz_us 为主，含 Etsy / DTC / showroom 渠道）
**产品类别**: 活性黄铜（unlacquered / living finish）厨卫龙头与卫浴五金配件
**调研状态**: 已完成
**验证状态**: 已验证（内部授权数据 + 7 路网研 + 8 credits Rainforest 实测）
**结论**: **不做** — 龙头端否，配件端亦否
**替代方向**: 复古造型（antique brass 电镀）加在现有 304 不锈钢配件平台 — 见 §7

---

## 执行摘要

发起假设："US `unlacquered brass kitchen faucet` ratio 0.36（637/月）、`aged brass kitchen faucet` 0.30 —— 活性铜饰面在龙头品类有真实劝退信号，而 KES 有 KITCHEN_FAUCET 产线。"

**该假设的每一层均未成立**：

| 层 | 原假设 | 实际 |
|---|---|---|
| 数字 | ratio 0.36 / 0.30 | 实际 **0.561**；`aged brass kitchen faucet` 无 share 数据 |
| 解读 | 低 ratio = 劝退信号 | 低 ratio = **搜索量集中度伪影**，corr(ln 量, ratio) = **−0.411** |
| 规模 | 有真实搜索入口 | ABA rank 762,740–1,493,112；点击份额是 1/12 级整数分数 |
| 渠道 | — | 真实需求在 showroom / 设计师指定，KES 进不去 |
| 材质 | KES 有 KITCHEN_FAUCET 产线 | KES 龙头本体是 **304 不锈钢**，UB 必须实心黄铜 |
| 配件退路 | 去掉涉水即可行 | 亚马逊上 UB 配件 SKU 评论数 **0–14** |

**核心发现**：

- 亚马逊侧整个 UB 关键词簇仅 **1,775 次/月**（全品类），厨房龙头口径 **796 次/月** —— 是 `gold kitchen faucet` 的 2.7%
- Etsy 摩洛哥手工渠道全渠道约 **5,500 件/年、GMV $2M**，且龙头老大三年跑量 **-31%**，品类在快速碎片化
- UB 是**溢价品类而非降本品类**：Rohl +50%、Brizo +60%、Crosswater 拉丝黄铜 +23~31%
- **供给早于需求 15–25 年**（Rejuvenation 1999 / Newport Brass 2006 / Waterworks 2010），25 年无人成功下沉到大众价位
- Masco 把 UB 给了 Brizo（$907）不给 Delta；Ferguson 的 Signature Hardware 在 $273–728 主动选 PVD；Kingston Brass 在 $150–400 不碰 —— **三家不同层级公司独立判断它不属于自己的价位，而它们全在 KES 之上（龙头 ASP $90）**
- 该品类**无评论飞轮**（靠 showroom / trade 售卖），KES 最强的站内执行能力在此失效

**方法论警示**：本次调查最初用亚马逊 ABA rank 判断一个主要不在亚马逊销售的品类，属方法错误，由用户指出 Etsy 线索后纠正。纠正渠道后结论未变，但该错误已记入 §2。

---

## 1. 三个方法论坑（本报告最主要的复用价值）

### 1.1 低 conversion/click ratio 不是"劝退信号"，是集中度伪影

`fact_ba_search_terms_weekly` / `dim_keyword_merged` 的 `top3_avg_conversion_share ÷ top3_avg_click_share` 与搜索量**强负相关**：

```
corr(ln(ss_search_volume_month), ratio) = -0.411   (n=796, faucet 词域)
```

全类目 ratio 分布（faucet，n=1,681）：p10 0.332 / p25 0.588 / **p50 0.779** / p75 0.944 / p90 1.149

龙头饰面里**卖得最好的三个词 ratio 最低**：

| 关键词 | 月搜索 | ratio |
|---|---|---|
| brushed gold bathroom faucet | 42,177 | **0.133** |
| matte black bathroom faucet | 39,866 | **0.170** |
| brushed nickel bathroom faucet | 33,733 | **0.265** |

若把低 ratio 读作劝退，结论会是"哑光黑和拉丝镍劝退消费者"。机制：头部词点击被 top3 吃掉，转化摊薄到长尾。

> **规则：用该 ratio 判断任何词之前，必须先对搜索量做分层对照。单点 ratio 无意义。**

### 1.2 小分母产生的整数分数是噪声，不是信号

`unlacquered brass kitchen faucet` 最新周 top3 点击份额 = 0.15、**0.0833、0.0833**。0.0833 = 1/12，0.15 = 3/20 —— 一周仅十几个点击。三个 ASIN 的 `conversion_share` 全为 NULL（亚马逊测不出）。

> **规则：看到 click_share 是简单整数分数（1/12、1/8、3/20），先算绝对量级再解读。**

### 1.3 网络检索会返回全网无源的"权威数字"

调查中反复出现："黄铜五金占北美高端浴室/门五金规格的 28%，2021 年仅 17%，来源 NKBA"。

抓取被指为出处的页面（kaseysmithinteriors.com）**页面内根本没有这些数字**，NKBA 2026 报告原文亦无。**这是幻觉/营销话术。** 同类需拒绝的还有 `unlacquered brass "hit a fever pitch of popularity in 2023 and 2024"`。

> **规则：任何"X% vs Y%"的行业数字，必须打开原始页面看到才可引用。**
>
> 补充事实：**从未有任何读者调查或 Houzz / NKBA 数据把 unlacquered brass 单列过**，所有数字都是 "gold/bronze" 聚合口径。声称有 UB 量化需求数字的，要么在引聚合数，要么在编。

---

## 2. 规模：三个独立渠道全部收敛在"很小"

### 2.1 亚马逊（Helium10 授权数据）

整个活性黄铜关键词簇 **仅 7 个词、合计 1,775 次/月**：

```
unlacquered brass kitchen faucet      637
unlacquered brass bathroom faucet     422
unlacquered brass hooks               234
unlacquered brass toilet paper holder 172
aged brass kitchen faucet             159
unlacquered brass faucet              122
aged brass bathroom sink faucet        29
```

厨房龙头口径 = **796/月**。对照 `gold kitchen faucet` 29,988/月、`brass kitchen faucet` 12,037/月。

ABA rank 对照（amz_us）：

| 关键词 | best rank |
|---|---|
| kitchen faucet | 3,692 |
| gold kitchen faucet | 50,661 |
| brass kitchen faucet | 84,058 |
| antique brass kitchen faucet | 160,260 |
| **unlacquered brass kitchen faucet** | **762,740** |
| aged brass kitchen faucet | 1,428,917 |

趋势：词数 2025Q3 的 1 个 → 2026Q1 的 5 个，best rank 从 2,070,481 改善到 762,740（约 2.4x）。**但最近两季已平**（762k → 876k → 876k）。同期主流暖色金属簇有 166 个词。

### 2.2 Etsy 手工渠道（经 Wayback 存档店铺页取得，Etsy 本体全面 403）

| 店铺 | 累计销量（快照） | 开店 | 年化 |
|---|---|---|---|
| InsidEast | 17,420 (2026-01) | 2018 | 3,786 → 2,622 → 1,741 |
| MetalWorksMorocco | 8,644 (2025-12) | 2021 | ~2,489 |
| BrassPure | 8,602 (2025-10) | 2022 | ~2,600 |
| BRASSLIK | 1,840 (2025-12) | 2020 | ~1,869（旺季高估） |
| ChokranBrass | 1,101 (2025-07) | 2022 | ~370 |
| LuxBrass / Brassry / BrassGate | 213 / 118 / 7 | — | 小 |

推算链：8 家约 9,000–9,500 sales/年（全品类）→ 补未观测店铺 12,000–16,000 → 水龙头占件数 30–45%（listing 占比 37–62%，但走量的是 $38–90 的皂液器/下水器/侧喷头）：

> **≈ 3,600–7,200 件/年，中枢 5,500；误差带 3,000–11,000。ASP $300–400 → GMV $1.5M–2.8M/年。**
> **量级约等于一个中型 Amazon listing 的年销售额。**

关键结构：**老大在减速（-31%），新进入者在抢份额。** 品类总量持平到温和增长 + **快速碎片化**，利润在被竞掉。

### 2.3 行业规格调查

Kitchen & Bath Business 2026-05-01 读者调查：厨房**拉丝/缎面镍 33.9%**（第一）、**金/古铜 28.4%**；卫浴金/古铜 29.4%（第一）。

**`unlacquered brass` 仅作为自由填答项出现，不在预设选项里。**

反向缺席证据：Houzz 2025 与 2026 两年水龙头趋势榜**均零提及**；LUXE 的 KBIS 2025 综述零提及（唯一黄铜条目是 Kallista 的**有涂层** "Blush Brass"）；Pinterest Predicts 2026 涨的是宽泛 "brass aesthetic"（+35%），非 UB。

---

## 3. 经济与合规：UB 是溢价品类，不是降本品类

三个独立来源同一方向：

| 来源 | 对照 | 溢价 |
|---|---|---|
| Rohl U.4718X | ULB $2,970 vs Polished Chrome $1,980 | **+50%** |
| Brizo 61346LF-C | ULB $907 vs Polished Chrome $567 | **+60%** |
| Crosswater Mpro | 拉丝黄铜 £193 vs 镀铬 £147 | **+23~31%** |

原因结构性：**patina 就是基材本身，没有"廉价基材 + 镀层"这个成本逃生口。** 必须实心无铅黄铜；无铅合金（C87850 硅黄铜 / C89833 铋锡黄铜）比含铅料贵 **10–25%**，可切削性仅 C36000 的 **70–80%**。

**合规（仅适用于涉水产品）**：

- **NSF/ANSI/CAN 61** 浸出测试收紧约 5 倍，2024-01-01 全面生效（标记 `Q ≤ 1`）
- **NSF/ANSI/CAN 372** 含铅量 ≤0.25% 湿表面加权平均
- **cUPC**（IAPMO R&T）在 UPC/IPC 辖区事实强制
- **2025 年 CPSC 连续 warning 亚马逊在售中国产龙头铅浸出超标**，点名 VESLA HOME、HGN、Kicimpro、VFAUOSIT、Qomolangma（厨房）、KZH、CEINOL、NICTIE、Rainsworth（卫浴），叫消费者停用丢弃

> KES 若以**中国制造 + 亚马逊渠道 + 价值价位**进入涉水黄铜品类，画像与被点名者高度重合。

行业对"会变色"的标准解法是**排除保修**：Newport Brass 原文 *"'Living' finishes have no warranty"*（其他饰面 10 年保修）；ROHL 同样列为不保修。

运营坑：Watermark 公开声明产品**在仓库存放期间即氧化变深** —— 与 FBA 慢周转 + 30 天退货窗口直接冲突。

---

## 4. 供给史：不是拐点前，是反复下沉失败

| 年份 | 品牌 | 证据 |
|---|---|---|
| 1999-08 | Rejuvenation | 站上已有 UB 饰面 |
| **2006-02** | **Newport Brass** | "Polished Brass Uncoated"，**已标注 "Living finish"** |
| 2010-07 | Waterworks | UB 已是在售 SKU 可选饰面 |
| 2016-01 | Kallista (Kohler) | UB 扩展到厨卫龙头（原文 "expands"，之前已有） |
| 2018 | Jaclo | ULB，明确 "living" |
| 2019 | Rohl | Satin ULB |
| **2026-05-13** | **Brizo** | **品牌首个 living finish**，$907，6-15 出货 |

> **供给比需求早 15–25 年。2025–2026 的"拐点"不是厂商加 SKU，是大众市场终于发现了早就存在的 SKU。**

Newport Brass 2006 年即使用 "living finish" 一词；Rejuvenation、Waterworks、Kohler 均握有充足资本与渠道 —— **25 年里无一家成功把它推下沉到大众价位。这是反复尝试下沉失败的结构性小众，不是拐点前的蓝海。**

### 分层证据（最干净的一条）

| 公司 | 大众品牌 | 轻奢/高端品牌 | UB 放在哪 |
|---|---|---|---|
| Masco | Delta（16 个厨房饰面，**一个黄铜都没有**） | Brizo（$567–907） | **Brizo** |
| Ferguson | Signature Hardware（$273–728，**主动选 PVD**） | — | **不做** |
| — | Kingston Brass（$150–400，唯一 living finish 是**油摩擦青铜**） | — | **不做** |

---

## 5. KES 自身位置（内部数据）

### 5.1 材质：全线 304 不锈钢，不是黄铜

- `KITCHEN_FAUCET` 主体材质：**304 Stainless Steel**（全库仅 1 个 `FAUCET` SKU 的 `body_material` 是 Lead-Free Brass）
- 卫浴配件（`TOWEL_HOLDER` / `TOILET_PAPER_HOLDER` / `SHELF_AND_CADDY`）：**304 不锈钢 + 大理石**
- 黄铜仅出现在下水器、阀芯、支架等配件件上

**UB 需要实心黄铜本体 → 换料 + 换模 +（涉水则）重新认证。不是加色号。**

### 5.2 金色业务在配件，不在龙头（180 天，已按 `(amazon_order_id, sku)` 去重）

| 品类 | 饰面 | 件数 | 收入 | ASP |
|---|---|---|---|---|
| **马桶纸巾架** | **BZ 拉丝金** | **6,854** | $274,418 | **$40.0** |
| 毛巾架 | BZ 拉丝金 | 1,320 | $92,908 | $70.4 |
| 厨房龙头 | BZ 拉丝金 | 539 | $48,652 | $90.2 |

**纸巾架金色款 1,142 件/月 = 厨房龙头金色款（90 件/月）的 12.7 倍。**

参考：即使 KES 拿到 UB 龙头统治级份额（796 搜索/月 × 25% 点击 × 8% 转化）≈ **16 件/月** —— **低于现有单个金色 SKU。**

### 5.3 关键词占位：现代赢、复古全输

ABA `is_own_asin_*` 检查（amz_us）：

```
brass toilet paper holder free standing   KES 在 top3  ✓
brass toilet paper holder stand           KES 在 top3  ✓  (2026-07-17)
brass toilet paper stand                  KES 在 top3  ✓
────────────────────────────────────────────────────────
所有 antique brass * 词                    KES 全部缺席  ✗
所有 brass * faucet 词                     KES 从未进过 top3  ✗
```

---

## 6. 配件端亦否 —— 以及真正该做的事

### 6.1 假设：去掉涉水，监管负担消失 → 成立

NSF 61 / 372 / cUPC / CPSC 铅风险**仅适用于饮用水接触**。毛巾杆 = 管 + 法兰 + 支架，无阀芯、无水道、无承压。

### 6.2 但 Rainforest 实测否决（8 credits，amz_us，2026-07-20）

`unlacquered brass towel bar`（**总结果仅 175 条**），所有声明 UB / 实心黄铜的：

| 产品 | 价格 | 评论数 |
|---|---|---|
| Van Dyke's Restorers 19" Unlacquered Brass | $69.58 | **无** |
| Set of 2 Unlacquered Brass Wall Hooks | $42.99 | **无** |
| Van Dyke's Restorers 19" Antique Brass Solid | $78.58 | **无** |
| Antique Brass Towel Ring – Solid Brass | $24.99 | **无** |
| Alno Contemporary UNLACQUERED Brass | $151.96 | **5** |
| Alno Double Robe Hook, UNLACQUERED Brass | $12.76 | **14** |
| Unlacquered Polished Brass Louie 挂钩 | $12.99 | **3** |

同页有量的全是非 UB：Kingston Classic $47.99 n=105、Leyden Antique $29.99 n=192、Kingston BA311BB $53.68 n=132。

**`antique brass towel bar`、`antique brass hooks`、`brass toilet paper holder` 三词的 top16 中，声明实心/无涂层黄铜的：0 个。**

`unlacquered brass kitchen faucet` 仅 273 条结果，top16 **无一真 UB 产品** —— 返回 Kingston 抛光黄铜、KRAUS 拉丝黄铜、Moen 拉丝金、Delta。**亚马逊上不存在 UB 龙头供给。**

### 6.3 同一次扫描证明"复古造型"卖得很好 —— 全是电镀

`antique brass toilet paper holder`（811 条）：

| 产品 | 价格 | 评分 | 评论数 |
|---|---|---|---|
| Flybath Brushed Brass Antique | $15.98 | 4.5 | **2,013** |
| Leyden Antique Brass | $18.99 | 4.5 | **559** |
| Antique Brass TPH 壁挂 | $19.80 | 4.6 | **336** |
| Antique Bronze 带置物架 | $18.99 | 4.6 | **300** |
| BESy 防锈壁挂 | $23.74 | 4.4 | **271** |

`antique brass hooks`（2,000 条）：IBosins 12 件 **$9.99 / n=5,583**、IBosins 15 件 **$11.99 / n=3,354**、khtumeware **$24.99 / n=470** —— 标题直接写 **zinc Alloy**。

`brass toilet paper holder`（2,000 条）：JQK **$12.99 / n=5,371**、FORIOUS **$19.94 / n=3,720**、RARXTR SUS304 **$19.99 / n=1,895** —— 全 304 不锈钢。

### 6.4 结论：把"饰面化学"与"复古造型"拆开

| 维度 | 需求 | 判断 |
|---|---|---|
| **饰面化学**（无涂层、会氧化） | 亚马逊 SKU 评论数 0–14 | **零需求，别碰** |
| **复古造型**（antique brass 外观、电镀） | $15–35 卖到 2,000–5,500 条评论 | **真需求，且 KES 缺席** |

> **建议动作：在现有 304 不锈钢配件平台上做「复古造型 + antique brass 电镀色」SKU 方向，价格带 $30–60。**
>
> - KES 纸巾架金色款现做 1,142 件/月、ASP $40 —— 价格带正好压在赢家（$15–35）上沿
> - 产线、模具、认证全部现成，**零新增材料、零新增认证**
> - KES 在现代 `brass * stand` 词上已是 top3，证明站内执行有效
> - 但在所有 `antique brass` 词上全部缺席 —— 这是缺口

> ⚠️ **未验证边界**：`brass kitchen faucet`（12,037/月）与 `antique brass kitchen faucet`（8,662/月）的需求究竟指向**桥式复古造型**还是**现代抽拉造型**，未做 PDP 级验证。若指向前者，则对龙头品类是"开新造型"而非"加色号"。**配件端造型结论已由 §6.3 实测支撑，龙头端未支撑。**

---

## 7. 重新审视的触发条件

出现以下任一，应重开评估：

1. **Brizo Faircroft（2026-06-15 起出货）在大众零售渠道出现可观测销量** —— 唯一能证明 UB 正在下沉的证据
2. **KES 获得 trade / showroom / 设计师指定渠道** —— 当前否定的核心理由之一是渠道不可达
3. **`unlacquered brass *` 关键词簇 h10 月搜索合计突破 ~5,000**（当前 1,775）
4. **亚马逊上出现 UB 配件 SKU 评论数破百**（当前上限 14）

---

## 8. 数据来源与复现

### 内部（免费）

| 表 | 用途 |
|---|---|
| `ods_bis_keyword_helium10` | UB 关键词簇月搜索量（唯一针对该品类的量化数字） |
| `ods_bis_keyword_seller_sprite` | 对照词月搜索量 |
| `dim_keyword_merged` | ratio 计算与基线分布 |
| `fact_ba_search_terms_weekly` | ABA rank 趋势、top3 归属、`is_own_asin_*` |
| `product` / `product_variant` / `listing` / `attribute_value` | KES 材质、SKU、饰面 |
| `fact_order_line_item` | 分饰面销量（⚠️ 须按 `(amazon_order_id, sku)` 去重，2025-11 起双摄入） |
| `competitor_daily_snapshot` | 竞品评论数（⚠️ 最新日仅 209 ASIN，是按本品配置的竞品集非市场扫描，"没有"是弱证据） |

### 外部（付费，已授权）

Rainforest `type=search`，amz_us，8 个词 × 1 页 = **8 credits**（2026-07-20）。词表见 §6.2 / §6.3。

### 未闭合的洞（均在 upper-mid 及以上，不影响结论）

- **Signature Hardware** 官网全程 403，UB 判定为四条间接证据推断（保修条款枚举、两个 PVD 型号码、站内检索零命中、营销语言），**非直接读取产品页**
- **Kohler / Kallista / Moen** 官网反复超时，"Kohler 品牌无 UB" 是强指示非铁证
- **欧洲/建筑五金未跑**（Dornbracht、Graff、Vola、THG、Rocky Mountain）
- **Google Trends 全程 429，无曲线数据**；本报告任何"趋势"判断均基于行业调查与媒体时间线，非 Trends
- 9 家已点名 Etsy 店铺无 Wayback 存档，销量缺失

---

## 9. 相关文档

- 平台侧 ratio 口径坑与 `fact_ba_search_terms_weekly` 是 Amazon 全站报表（非 KES 词域）这一事实互补
- KES 厨房龙头产品概况见 `kes-ops-platform/docs/product_brief_supplementals/KN927和KG927产品概况文档.md`
