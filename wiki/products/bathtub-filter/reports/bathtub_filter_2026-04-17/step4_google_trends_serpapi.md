# Step 4: Google Trends + Google Shopping（SerpAPI）

- **工具**：`kes_ops_platform.integrations.serpapi_client`（SerpAPI）
- **报告日期**：2026-04-17
- **本步骤消耗配额**：serp_api ×6 次（250/月上限）
- **原始数据**：
  - `raw/serpapi_trends_bathtub_vs_shower_us_12m.json` — 12 个月三词对比
  - `raw/serpapi_trends_bathtub_filter_5y_us.json` — 5 年趋势
  - `raw/serpapi_trends_bathtub_filter_related_queries.json` — 相关词
  - `raw/serpapi_shopping_bathtub_filter_us.json` — Google Shopping 40 条

---

## 1. Google Trends 三词对比（12 个月，美国）

| 词 | 12 个月平均 | 2025-04 首周 | 2026-04 最新周 | 变化 |
|---|---|---|---|---|
| `shower filter` | **32** | 20 | **56** | +180% |
| `bath filter` | 5 | 3 | 13 | +333% |
| `bathtub filter` | 1 | 1 | **3** | +200% |

> 说明：Google Trends 分数是相对指数（最高词=100），三词同框比较时 shower filter 压制了其他两词。

---

## 2. ⭐⭐⭐ Google Trends 5 年趋势（bathtub filter 单独，美国）

这是**最重要的一张图**：

| 时期 | 趋势值（0-100）| 备注 |
|---|---|---|
| 2021-2024 历史 | **0-9** | 几乎无搜索 |
| 2022-03 历史峰值 | 9 | 当时的最高点 |
| 2026-03-08 | 26 | 突然起飞 |
| 2026-03-15 | 36 | |
| 2026-03-22 | 34 | |
| **2026-03-29** | **100** | 🚀 **历史最高，是 2022 年峰值的 11 倍** |
| 2026-04-05 | 42 | 高位回落 |
| 2026-04-12 | 43 | 仍是 5 倍于历史基线 |

**解读**：
- Canopy 于 2026-01-08 上市 → 品牌营销效果在 2026-03 末触发了全品类搜索量的**指数级暴涨**
- 2026-03-29 那周的 Google 搜索量是 **整个 5 年历史的最高点**
- 这与 BA 数据的发现完全吻合（brand 词 rank 从 487K → 65K）

---

## 3. Google Trends 相关词（Rising = 近期增速最快）

### 🔥 Rising（增速排名）
| 词 | 增速 | 备注 |
|---|---|---|
| `how to install bathtub faucet` | **Breakout** (>5000%) | 安装类需求被带动 |
| `canopy bath tub filter` | **Breakout** | Canopy 品牌词爆发 |
| `canopy` | +1,450% | 品牌整体上升 |
| `canopy bath filter` | +800% | |
| `filter baby` | +100% | 竞品 FilterBaby 也在上升 |

### 📊 Top（搜索量绝对排名）
| 词 | 相对量 | 含义 |
|---|---|---|
| `bathtub water filter` | 100 | 主力变体词 |
| `water filter` | 99 | 泛词 |
| `water filter for bathtub` | 54 | |
| `bathtub faucet` | 43 | 安装相关 |
| `tub filter` | 33 | |
| `filter for bathtub faucet` | 23 | 精准词 |
| `filter baby` | 23 | 竞品品牌 |
| `canopy` | 23 | 竞品品牌 |
| `shower water filter` | 15 | 跨品类 |

---

## 4. Google Shopping 渠道分布（40 条结果）

### 🏬 关键发现：Canopy 是多渠道品牌，不只是 Amazon DTC

| 渠道 | 品牌 | 价格 | 备注 |
|---|---|---|---|
| **Target** | Canopy 2-in-1 | **$69.99** | 实体零售渠道！比 Amazon $89 便宜 |
| **Target** | Canopy 2-pack | $65.99/ea | 多件装 |
| **Sephora** | Canopy Bath Tub Filter | $89 | 🎯 美妆/护肤渠道，定位清晰 |
| **Babylist** | Canopy Bath Tub Filter | $89 | 宝宝注册礼品单平台 |
| Amazon | (通过 Rainforest 已覆盖) | $89 | |
| **Walmart** | PUREPLUS | $17.90 | 白牌低端线 |
| **Walmart** | AmzDoer generic | $23.99 | |
| **Wayfair** | TENicas premium | **$104.99** | 高价位入局 |
| eBay | WETRBWEH | $5 | 超低价 |
| DTC: Tubo | Tubo 2.0 | $64.99 | 独立站 |
| DTC: Crystal Quest | Bath Ball | $64.95 | 独立站 |
| DTC: pureplusfilter.com | PUREPLUS | $22.99 | 独立站 |

### Sephora 分销的战略意义
- **Sephora 是美妆/护肤专业渠道**，Canopy 进入 Sephora 意味着：
  1. 产品已被定位为"护肤工具"而非"水管配件"
  2. 消费者认知 = 护肤 > 净水器
  3. 目标客群 = Sephora 的女性护肤消费者（高端、对成分敏感）
- **Babylist** = 美国最大宝宝注册礼品单平台，Canopy 在上面 = 正在拿下"新生儿家庭"场景

---

## 5. 综合结论

### Google Trends 三大信号
1. **2026-03-29 创 5 年历史搜索峰值**：Canopy 发布 + 媒体报道触发全品类爆发
2. **`canopy bath tub filter` 搜索 Breakout（>5000% 增速）**：品牌词已超越品类词，说明是品牌驱动
3. **安装类词 `how to install bathtub faucet` 也 Breakout**：新消费者不知道怎么装，是教育机会

### Google Shopping 三大信号
1. **Canopy Target 价格（$69.99）< Amazon（$89）**：零售渠道比 Amazon 便宜 20% → Amazon 不是 Canopy 的主战场，可能只是品牌曝光渠道
2. **Sephora 上架**：品类正式进入"美妆护肤"赛道，不是"家居维修"
3. **价格带完整**：$5（eBay）→ $18（Walmart）→ $25-65（Amazon 中段）→ $89（Canopy/Sephora）→ $105（Wayfair 高端）— 全价格带均有占位，市场分层明显

### ⚠️ GEO_MAP（地理分布）未成功
SerpAPI 的 `GEO_MAP` 数据类型在当前计划下返回 400 错误（需更高级计划）。
可通过 Google Trends 网页手动查，或等待升级 SerpAPI 计划。
