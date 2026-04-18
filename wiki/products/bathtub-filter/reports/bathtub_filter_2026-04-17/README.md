# Bathtub Filter 市场研究报告（综合版）

**日期**：2026-04-17
**数据源**：Amazon BA (Brand Analytics) + Rainforest API + Brave Search API + SerpAPI (Google Trends + Shopping) + 第三方测评 Web 抓取
**作者**：Claude via kes-ops-platform

---

## 📁 目录结构

| 文件 | 内容 |
|---|---|
| `README.md` | **本文件 — 综合报告** |
| `step1_ba_keyword_scan.md` | BA 关键词扫描（市场规模、竞争格局）|
| `step1.5_shower_filter_comparison.md` | 相邻品类 shower filter 对比 |
| `step2_rainforest_competitor_scan.md` | Rainforest 竞品 PDP + 搜索排序 |
| `step3_consumer_voice.md` | 第三方测评 + 消费者动机定性 |
| `step4_google_trends_serpapi.md` | Google Trends 5 年趋势 + Google Shopping 渠道 |
| `raw/*.csv / *.json` | 原始数据（可重跑分析）|

### 原始数据清单
```
raw/ba_search_terms_bathtub_filter_all_weeks.csv    # BA 命中全量 277 行
raw/ba_search_terms_shower_filter_all_weeks.csv     # shower filter 命中 3286 行
raw/us_trend_core_terms.csv                          # 核心 8 词时序
raw/step1_summary.json                               # 结构化摘要
raw/rainforest_search_bathtub_filter_us.json         # US Top 65 搜索结果
raw/rainforest_search_bathtub_filter_ca.json         # CA Top 60 搜索结果
raw/rainforest_pdp_B0GFQ1JRSK_us.json                # Canopy PDP
raw/rainforest_pdp_B0CXT5KL5Z_us.json                # Beati Faucet (BSR #1)
raw/rainforest_pdp_B0DC3JQ34R_us.json                # SHLLKTTRY 白牌
raw/rainforest_pdp_B0742KFY9R_ca.json                # Santevia CA
raw/rainforest_pdp_B0FKH16TZR_ca.json                # PUREPLUS CA Top1
raw/brave_reddit_bathtub_filter_experience.json      # Brave 搜索：Reddit 真实用户体验
raw/brave_reddit_baby_eczema_bathtub_filter.json     # Brave 搜索：婴儿湿疹 + bath filter
raw/brave_reddit_site_bathtub_filter.json            # Brave site:reddit.com 专搜
raw/brave_product_comparison.json                    # Brave 搜索：多品牌横向对比
raw/brave_market_size_growth.json                    # Brave 搜索：市场规模数据
raw/serpapi_trends_bathtub_vs_shower_us_12m.json     # SerpAPI: 12 个月三词对比
raw/serpapi_trends_bathtub_filter_5y_us.json         # SerpAPI: bathtub filter 5 年趋势
raw/serpapi_trends_bathtub_filter_related_queries.json  # SerpAPI: 相关词 Rising/Top
raw/serpapi_shopping_bathtub_filter_us.json          # SerpAPI: Google Shopping 40 条
```

---

## 🔑 Executive Summary（5 分钟阅读）

### 市场体量
- **Bathtub filter 是一个北美集中、小众但快速上升的品类**
- US 最高搜索热度 rank ≈ **6.6 万位**（头部品类在 1-5K）
- 相比邻近品类 **shower filter（rank 3,328），bathtub 小 20 倍**，但 Canopy 品牌词在 **8 个月内热度涨 7.4 倍**
- UK / DE 尚无规模化搜索，**加拿大有但市场薄**

### 竞争格局：三层 + 一个心智赢家

| 层 | 代表玩家 | 价格 | 真实市场地位 |
|---|---|---|---|
| **Premium / Lifestyle** | Canopy ($89, 2026-01 上市) | $89 | **BA 心智 Top1**（30/31 词），但 Amazon 搜索 pos=14，仅 57 reviews |
| **Mid Mainstream** | **Beati Faucet** ($25, 1811 reviews) | $25 | **BSR 实际 #1**（Bathtub Faucet Replacement Parts）|
| | Santevia ($20, 2218 reviews, since 2017) | $20 | **CA 老大 + 第三方测评冠军** |
| **Chinese White-Label** | Tubo / SHLLKTTRY / PUREPLUS / Cobbe / Kinder | $15-25 | 同质化价格战 + 广告位 |

### 消费者动机（按强度）
1. **婴儿湿疹 / 敏感肌**（最强 — 付费意愿最高，$89 能卖）
   - Reddit 原话：*"I was mortified knowing we'd been bathing in that water"*（过滤器变黑 = 视觉冲击 = 强转化）
   - 核心社区：`r/moderatelygranolamoms`（多帖讨论）、`r/eczema`、`r/toddlers`
2. **成人护肤 / 除氯**（中 — FilterBaby 品类证明独立付费心智）
   - Reddit：*"I hate coming out of my shower or bath smelling like I swam in a pool"*
3. **硬水 / 头发**（弱 — 且产品实际不除硬度，是认知错配）

### 产品同质化真相（独立测评）
- 所有品牌都用 **KDF 55 + 活性炭 + 多级滤材**，标称 **2,500 gallons** 寿命
- **快流速下 90% 产品除氯效果崩盘**（Canopy 只除 50%）
- **只有 Santevia** 在正常流速下除氯 100%（但品牌力最弱）
- **全行业都无法去除 DBPs（消毒副产物）** — 真正的健康威胁未被解决

### Google Trends 爆发信号（SerpAPI 2026-04-17）
- **2026-03-29 那周 Google 搜索量创 5 年历史最高（100/100）** — 是 2022 年历史峰值（9/100）的 **11 倍**；4 月高位回落但仍维持在基线 5 倍（43/100）
- `canopy bath tub filter` 搜索 **Breakout（>5000% 增速）** — 品牌词已超越品类词，Canopy 驱动整个品类上涨
- **Canopy 多渠道铺货**：Amazon $89 / Target $69.99（实体零售比 Amazon 便宜 20%）/ **Sephora $89**（美妆渠道，定位护肤工具）/ Babylist $89（新生儿礼品单）
- `shower filter` 同期 12 个月均值 32，`bathtub filter` 仅 1，品类仍在早期快速教育期

### 战略洞察
1. **Canopy 正在用品牌 + 3-in-1 gadget 化设计 重塑品类**：把"过滤器"升级成"婴儿洗澡安全解决方案"
2. **Amazon BSR #1（Beati Faucet）完全没有品牌资产** — 消费者不记得它
3. **品类接近早期大众化临界点**：品牌词热度爆发 + 测评媒体集中出现 + 多 DTC 品牌切入
4. **欧洲 / CA 存在空白**：Canopy 还没进入非 US 市场
5. **租房人群是被低估的需求来源**：Reddit 反复出现 "rental" 场景 — 无法安装全屋过滤的租客是天然目标用户
6. **氯胺（chloramine）是被忽视的技术空位**：`r/WaterTreatment` 专帖提到，许多市政水用氯胺消毒（难于氯），但所有主流产品都不明确标注是否处理氯胺

### 空位机会（如果 KES 要进入）
1. **NSF 53 认证 + DBP 去除**：真正的技术护城河（所有在位玩家都没做到）
2. **快流速除氯保证**：独立测评的明确痛点
3. **氯胺处理**：Reddit r/WaterTreatment 专帖需求明确，无品牌专门覆盖
4. **孕妇 / 月子 / 宠物**细分场景：现有品牌都没专门打
5. **租房人群**：无法安装全屋过滤的高频次目标用户，Reddit 反复验证
6. **加拿大 / 欧洲市场**：US 已卷，其他市场处于教育早期
7. **B2B**：儿童早教机构、月子中心、美容院

---

## ⚠️ 限制说明
- BA 数据周次到 **2026-03-22**（2 周前）
- Rainforest 快照为 **2026-04-17 实时**
- Reddit PRAW 未配置，Reddit 定性数据通过 **Brave Search API** 间接获取（snippet 级别）— 如需完整帖子内容可补配 PRAW 凭据或换用 Brave 的 Discussions API
- 未分析 reviews 原文（Rainforest reviews API 本次返回为空）—— 如需深度 review 情感分析可补做

## 🔜 可以继续的深化方向
- **Amazon review 采集 + LLM 分类**（Canopy / Beati / Santevia 的 review 各 500 条，做痛点 / 动机 / 不满 聚类）
- **Rainforest 搜索历史快照**（跟踪 6 个月内 Top 20 位置变化，看新玩家入场速度）
- **Canopy DTC 网站分析**（getcanopy.co — 看他们产品矩阵、定价策略、CRM 内容线索）
- **Google Trends 地理分布**（`GEO_MAP` 需 SerpAPI 更高级计划，可手动查 Google Trends 或升级后补跑）
- **Home Depot / Walmart / Wayfair 对标**（Google Shopping 已发现 Wayfair $104.99 高端线，可深挖）
- **专利数据检索**（看 NSF DBP-removal filter 是否有专利壁垒）
