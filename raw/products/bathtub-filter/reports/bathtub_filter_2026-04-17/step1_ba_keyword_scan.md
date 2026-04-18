# Bathtub Filter — Step 1: Amazon BA 关键词扫描

- **报告日期**：2026-04-17
- **数据源**：`fact_ba_search_terms_weekly`（Amazon Brand Analytics Search Terms weekly）
- **站点覆盖**：amz_us / amz_ca / amz_uk / amz_de
- **数据窗口**：2025-05-04 ~ 2026-03-22（最新周）
- **匹配词数**：51 个相关长尾词（US 最新周）
- **原始数据**：
  - `raw/ba_search_terms_bathtub_filter_all_weeks.csv` — 全站点全周次命中行（277 行）
  - `raw/us_trend_core_terms.csv` — US 核心 8 词 52 周时序
  - `raw/step1_summary.json` — 结构化摘要

---

## 1. 市场规模 & 增长

| 词 | US 最新周 rank | 备注 |
|---|---|---|
| `bathtub filter` | 102,223 | 品类主关键词 |
| `bath tub filter` | 110,413 | |
| `bathtub water filter` | 125,285 | |
| `canopy bathtub filter` | **65,874** | 品牌词已超品类词 |
| `baby bath filter` | 598,096 | 场景词 |

> 参考尺度：头部品类主词 rank 通常在 1-5K 位。**bathtub filter 是小众品类**（10 万位量级），但正在上升。

**增长信号**：品牌词 `canopy bathtub filter` 在 8 个月内 rank 从 **487,651（2025-07）→ 65,874（2026-03）**，搜索热度涨了 **7.4 倍**。通用词 rank 基本持平，说明是**品牌驱动的品类扩张**（Canopy 通过社媒 / 广告推动消费者形成品类认知）。

---

## 2. 竞争格局：单寡头垄断

### US 市场
| ASIN | 品牌（推测）| Top-1 出现次数 / 31 | 平均点击份额 | 备注 |
|---|---|---|---|---|
| **B0GFQ1JRSK** | **Canopy** | **30** | **24.6%** | 几乎所有相关搜索词都由它拿下 Top-1 |
| B01MUBU0YC | Santevia | 1 | 1.0% | 只在 `santevia bath filter` / `hard water faucet filter` 出现 |

**关键观察**：所有搜索词的 Top-2、Top-3 ASIN 字段全部为空 → **没有第 2、第 3 玩家能上到 Amazon BA 阈值**。品类由 Canopy 一家独大。

### 加拿大市场
- Top-1 是 **B0FKH16TZR**（**不是 Canopy**）→ 待 Step 2 Rainforest 抓取确认身份。

### 欧洲（UK / DE）
- 最新周**未出现** `bathtub filter` 类搜索词 → 品类尚未在欧洲形成规模化搜索需求，或未达到 BA 最小报告阈值。
- **结论：品类目前是北美（US > CA）独占**。

---

## 3. 使用场景（从 51 个长尾词反推）

| 场景分类 | 代表搜索词 | 信号强度 |
|---|---|---|
| **婴儿洗澡水安全** | `baby bath filter`, `baby bathtub filter`, `baby bath tub filter`, `canopy baby bath tub filter`, `bath filter for baby`, `bathtub filter for baby`, `baby bath water filter` | **🔥 强**（某些词 CVR 达 83%+） |
| **硬水 / 除氯** | `hard water faucet filter`, `bath tub water filter` | 中 |
| **替换耗材** | `canopy bathtub filter replacement` | 中（复购已成型）|
| **浴缸安装位置** | `bathtub filter for tub faucet`, `tub faucet filter`, `bath tub filter for tub faucet` | 高 |

**推断**：主消费者心智 = "我想给宝宝 / 家人一个更干净（除氯）的洗澡水"。婴儿场景是**转化率最高**的细分。

---

## 4. 与邻近品类的区分

| 品类 | 代表词 | 主导 ASIN | 结论 |
|---|---|---|---|
| **Bathtub filter** | bathtub filter | B0GFQ1JRSK (Canopy) | 本次研究对象 |
| **Kitchen faucet filter** | faucet filter, brita faucet filter, pur faucet filter | B07MLSVLZH / B082TJ7XRV | **不同品类**，千万不要合并分析 |
| **Shower filter** | — | 待 Step 1.5 扫描 | 更大的相邻品类，预计有溢出效应 |

---

## 5. 一句话结论

> **Bathtub filter 是 Canopy 用品牌教育正在推动的北美上升品类，当前搜索规模小（~10 万 rank 量级）但 8 个月内热度涨 7 倍；几乎无第二玩家；婴儿洗澡水安全是最强的细分场景与转化心智。**

---

## 下一步
- **Step 1.5**：扫描 `shower filter` 做对比，判断是否为 Canopy 的品类延伸方向
- **Step 2**：Rainforest 抓 Canopy PDP + CA 市场领导者身份 + Top 20 搜索位
- **Step 3**：抓 Reddit / Amazon review，看消费者"为什么买"
