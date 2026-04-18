# Step 2: Rainforest 竞品 PDP 扫描

- **工具**：`kes_ops_platform.integrations.rainforest` (Rainforest API)
- **报告日期**：2026-04-17
- **原始数据**：
  - `raw/rainforest_search_bathtub_filter_us.json` — US 搜索 Top 65 结果
  - `raw/rainforest_search_bathtub_filter_ca.json` — CA 搜索 Top 60 结果
  - `raw/rainforest_pdp_B0GFQ1JRSK_us.json` — Canopy PDP
  - `raw/rainforest_pdp_B0CXT5KL5Z_us.json` — Beati Faucet PDP（真正 BSR #1）
  - `raw/rainforest_pdp_B0DC3JQ34R_us.json` — SHLLKTTRY PDP
  - `raw/rainforest_pdp_B0742KFY9R_ca.json` — Santevia PDP
  - `raw/rainforest_pdp_B0FKH16TZR_ca.json` — PUREPLUS PDP（CA Top1）

---

## 1. 关键反直觉：BA 和 Amazon 搜索页显示的竞争格局不一致

BA（brand analytics）测量的是"消费者点进 Top3 的 ASIN 频次"—— Canopy 在 BA 里垄断 30/31 词。但**实际 Amazon 搜索 `bathtub filter` 的自然排序里，Canopy 只在 pos=14**。

这意味着：
- **消费者一旦点进搜索页，Canopy 品牌 pull 非常强**（即使排名第 14 仍拿走 24%+ 点击）
- **但 Amazon 算法没把 Canopy 排到自然位 Top1**（可能因为 review 数只有 57，太新）
- Amazon 搜索排序的 Top3 全被低价中国白牌拿下（Tubo $64、KDF55 $29、Cobbe $11）

## 2. 真正的市场领先者（按 BSR 排名）

| 排名 | ASIN | 品牌 | 价格 | Rating | Reviews | 上架日期 | BSR（Bathtub Faucet Replacement Parts）|
|---|---|---|---|---|---|---|---|
| **#1** | B0CXT5KL5Z | **Beati Faucet** | $25.49 | 4.4 | **1,811** | 2024-03-12 | **#1** |
| **#2** | B0GFQ1JRSK | **Canopy** | **$89** | 4.5 | 57 | **2026-01-08** | **#2** |
| — | B0DC3JQ34R | SHLLKTTRY (CN 白牌) | $19.99 | 4.4 | 1,562 | — | — |
| — | B0742KFY9R (CA) | **Santevia** | $24.99 (CAD) | 4.0 | 2,218 | 2017-07-19 | 北美 OG |
| — | B0FKH16TZR (CA) | PUREPLUS (CN 白牌) | $19.99 | 3.1 | 19 | 新 | — |

## 3. 三层定价 / 定位结构

### 🏆 Premium / Lifestyle 层（$80+）
**Canopy** — 2026-01 刚上市，已冲到 BSR #2
- **定位**：婴儿洗澡水安全，Gentler Bath for Delicate Skin
- **差异化**：3-in-1 设计 = 过滤器 + BPA-free 硅胶嘴套（防撞）+ 电池-free 温度变色指示
- **品牌策略**：母婴 / 生活方式品牌，和他们 shower filter (B0CJ3G16QZ) 共享品牌资产
- **弱点**：只有 57 reviews，价格是竞品 3-5 倍

### 🎯 Mid Mainstream 层（$20-30）
**Beati Faucet** $25.49（1811 reviews，BSR #1）
- 通用除氯卖点、KDF 55 + 多级滤材
- 没有特定场景 positioning，靠"大众性价比"

**Santevia** $24.99（2218 reviews，加拿大 OG）
- **独特卖点**：Organic Cotton 有机棉滤芯 / 敏感皮肤定位
- 2017 年上市 — 这个品类的老玩家
- 加拿大市场认可度很高（阿马逊 Water Filtration #5、Water Coolers Filters #11）

### 💰 Chinese White-Label 层（$15-20）
**SHLLKTTRY / PUREPLUS / Tubo / Cobbe / Kinder** 等
- 同质化产品：KDF55 + 活性炭 + 陶瓷球 + 8-11 级滤材
- 靠价格和广告卡位（搜索 Top 结果大部分是 sponsored）
- Review 数从数十到数千不等，新老混杂

## 4. 共性产品规格（跨品牌归并）

| 组件 | 普遍采用 | 备注 |
|---|---|---|
| 壳体材料 | ABS 塑料 | 所有品牌一致 |
| 核心滤材 | **KDF 55** | 全行业标配除氯核心 |
| 辅助滤材 | 活性炭 / 陶瓷球 / 钙亚硫酸盐 / 维生素 C | 不同品牌组合略不同 |
| 滤级数 | 8-11 级 | 越多级数 = 越贵，但实际差异未必显著 |
| 容量 | **2,500 gallons** | 几乎所有品牌标称一致 |
| 替换周期 | 90 天 | Canopy 明确标注 |
| 安装方式 | 无需工具，直接套到水龙头（spout cover） | 统一 |

**→ 产品本质上高度同质化，竞争维度已从"功能"移到"品牌 + 场景"。**

## 5. Canopy 的差异化解构

Canopy 在同质化品类里做到了差异化，核心三点：
1. **场景 = 婴儿专用**（title 里直接写 "Baby Bath Tub Filter"）— 锁定高价值 + 高焦虑消费者
2. **产品形态 = 3-in-1 硬件**（过滤 + 防撞套 + 温度计）— 拉升价格感知和使用场景密度
3. **品牌声誉 = Canopy 母品牌资产**（原本做加湿器 / 洁面仪 / shower filter 的 DTC 新锐品牌）

## 6. 加拿大市场独立观察

- Canopy 尚**未进入加拿大**（CA 搜索页 Top60 无此 ASIN）
- Top1 是中国白牌 **PUREPLUS**（review 只有 19 — 说明市场很薄）
- **Santevia 是 CA 的真实领先者**（2218 reviews）— 但仍是通用"敏感皮肤"路线
- **CA 存在品牌化窗口**：如果 Canopy 进入 CA 或 KES 推出更强场景化产品，有机会抢占
