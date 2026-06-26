---
type: product
status: draft
owner: strategy
created: 2026-06-02
updated: 2026-06-03
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, competitor-claims, amazon-reviews, scorecard]
source_count: 3
review_cycle: monthly
verification_status: review_evidence_scorecard
related:
  - ./bathtub-filter-11-asin-public-competitor-evidence-2026-06-02.md
  - ./bathtub-filter-amazon-review-image-installation-packaging-leads-2026-06-02.md
  - ./bathtub-filter-competitor-review-corpus-2026-04.md
  - ../shower-filter/shower-filter-filterbaby-b0fnvdjrsq-competitor-brief-2026-06-03.md
---

# 竞品卖点 vs 实际评论准确率评分（2026-06-02）

## 口径

本页评分的是 **卖点与评论证据的一致程度**，满分 100，不是产品质量总分，也不是实验室净化性能分。

评分使用三类本地证据：

- Amazon PDP 快照：标题、feature bullets、价格和公开销量信号。
- 2562 条 bathtub active 评论语料：星级、正文、图片数、review link。Filterbaby `B0FNVDJRSQ` 已从 bathtub 评论语料删除并保留在 shower-filter 项目。
- 第二轮评论标签：正向证据、1-2 星高杀伤投诉、高星轻微吐槽、claim dispute、overflow、mold、refill 等。

不纳入评分：真实退货率、退款原因、客服工单、实测氯/硬度/TDS/流速、真实滤材配比。这些目前没有公开可核验证据。

**2026-06-03 口径修正：** Filterbaby `B0FNVDJRSQ` 是 shower filter / showerhead inline 产品，已拆到 shower-filter 项目。下表只保留 active bathtub-filter 竞品，Filterbaby 的评分子集见 `raw/products/shower-filter/filterbaby-claim-review-accuracy-scorecard-2026-06-02.csv` 和 `wiki/products/shower-filter/`。

## 评分方法

| 评分层 | 说明 |
|---|---|
| 评论支持 | 星级、4-5 星比例、正向标签是否支持核心卖点，例如安装方便、皮肤/头发体感、宝宝/敏感肌、氯味降低、水流稳定。 |
| 评论反证 | 1-2 星高杀伤投诉、整体无效、绕流/溢流、宣传口径争议、安装不稳、滤芯寿命、发霉卫生、掉砂/脏污、宝宝/敏感肌效果不稳定。 |
| 卖点过度承诺 | 对 `99% removal`、重金属/lead/fluoride、hard water softener、limescale、universal fit、zero overflow、no leak、超长寿命、医学/湿疹改善等高风险 claim 扣分。 |
| 样本置信度 | review_count 越小，分数越保守。`very_low` 不是说产品差，而是当前评论证据不够稳。 |

## 总表

| 排名 | ASIN | 品牌/路线 | 准确率 | 置信度 | 评论样本 | 平均星级 | 4-5 星 | 1-2 星 | 判断 |
|---:|---|---|---:|---|---:|---:|---:|---:|---|
| 1 | `B0GFQ1JRSK` | Canopy / premium baby tub-spout | 78 | low | 26 | 4.19 | 76.9% | 7.7% | 形态、安装、spout-cover 卖点较匹配；水质/皮肤结果仍是感知型证据。 |
| 2 | `B0FT7R9ZQ9` | JYFJYF / Velcro strap low-price | 75 | low | 47 | 4.62 | 91.5% | 8.5% | Velcro/easy-use 可信；10-stage、pH、重金属等技术 claim 偏大。 |
| 3 | `B0FL24SLM5` | Yolycen / ultra-low-price long-life | 73 | medium | 90 | 4.74 | 94.4% | 5.6% | 星级支持强；8,000 gallon、10-12 month、99%/硬水/多滤材 claim 过度。 |
| 4 | `B0CXT5KL5Z` | Beati Faucet / high-sales low-price | 72 | high | 356 | 4.70 | 92.4% | 6.7% | 易用和体感改善被支持；`fits all`、fluoride、hard-water softener 等不能按事实写。 |
| 5 | `B0G5NZBW6W` | Syvahome / KDF55 overflow route | 69 | low | 69 | 4.33 | 88.4% | 10.1% | 评论支持易用；99% elimination、limescale、no drip/no splash/no leak 过度。 |
| 6 | `B0D3X39378` | SHLLKTTRY / overflow low-price | 68 | high | 1410 | 4.53 | 87.4% | 11.6% | 正向样本很强，但 overflow、refill、claim dispute 和整体无效也很集中。 |
| 7 | `B0GKT5CHYL` | Uiuaquas / all-metal tub-spout | 64 | very_low | 13 | 4.38 | 84.6% | 0.0% | 负面少但样本太小；99% removal、100% filtering、zero overflow、99% faucet fit 太激进。 |
| 8 | `B008A4AG2U` | Crystal Quest / bath-ball technical | 55 | very_low | 19 | 3.21 | 57.9% | 42.1% | 实物形态可确认；评论样本小且负面比例高，lead/impurity/long-life claim 支撑弱。 |
| 9 | `B0DTQ8H23D` | Tubo / premium-ish baby bath | 49 | medium | 76 | 3.55 | 59.2% | 22.4% | `prevents overflow even with strong water pressure` 与评论投诉直接冲突。 |
| 10 | `B0742KFY9R` | Santevia / soft-hanging cloth | 43 | high | 456 | 3.32 | 54.6% | 37.1% | soft cloth 形态真实，但 99.9% chlorine、minerals、敏感肌/宝宝和卫生维护被大量挑战。 |

## 逐项判断

| ASIN | 核心卖点 | 评论支持 | 评论反证 | 评分理由 |
|---|---|---|---|---|
| `B0GFQ1JRSK` | baby/sensitive skin、chlorine/irritants、硅胶 spout cover、温度条、tool-free install、90 天滤芯 | 20/26 条 4-5 星；安装/适配 9，宝宝/敏感肌 7；图评确认 spout-cover、manual、盒内件 | overflow/flow 3，refill 5，claim dispute 2，整体无效 2 | 形态和安装较准；净化和皮肤结果仍缺实测，且有流量/滤芯成本疑点 |
| `B0FT7R9ZQ9` | Velcro strap、10-stage/8 media、fluoride/chlorine/heavy metals/rust、pH、2500 gallon、first-use residue/overflow disclaimer | 91.5% 4-5 星；宝宝/敏感肌 7，安装/适配 6，皮肤/头发 4 | claim dispute 4，refill 3，overflow/flow 2，掉砂/残留 3 | 易用卖点相对可信；技术 claim 偏大，但页面 warning 降低误导性 |
| `B0FL24SLM5` | 8000 gallon、10-12 月寿命、99% chlorine/heavy metals、hard-water softener、vitamin C/mineral/magnetic、universal install | 94.4% 4-5 星；安装/适配 16，宝宝/敏感肌 9 | refill 7，quality 4，claim dispute 3，宝宝/敏感肌不稳定 3 | 星级好，但寿命、硬水、重金属、多滤材都不应写成已验证事实 |
| `B0CXT5KL5Z` | hard-water softener、contaminants/chlorine/fluoride、skin/hair/nails、fits all tubs、fast uninterrupted filtration | 92.4% 4-5 星；安装/适配 71，皮肤/头发 29 | high-kill 22，整体无效 16，overflow 7，claim dispute 7，quality 7 | 用户满意度高；但 `fits all` 和去 fluoride/硬水软化属于高风险话术 |
| `B0G5NZBW6W` | Vitamin C/minerals、8-stage/KDF55、99% heavy metals/rust/limescale、nearly any faucet、no drip/no splash/no wait/no leak | 88.4% 4-5 星；安装/适配 12，氯味 4 | claim dispute 6，refill 7，整体无效 4，overflow 2 | 易用可信度中等；99%、limescale、no drip/no leak 类绝对化 claim 不稳 |
| `B0D3X39378` | overflow/splash guard、2500 gallon、chlorine/fluoride/hard-water softener、two suspension cords、almost any faucet、skin/hair | 1410 条大样本；安装/适配 352，皮肤/头发 205，宝宝/敏感肌 186，氯味 34 | high-kill 133；整体无效 79，refill 66，overflow 61，claim dispute 44，宝宝/敏感肌不稳 32 | 转化卖点有效，但关键技术承诺和结构风险也最清晰 |
| `B0GKT5CHYL` | all-metal lead-free、99% removal、15L/min、100% filtering efficiency、zero overflow、99% faucet fit、3 秒安装 | 13 条中无 1-2 星；宝宝/敏感肌 3，安装/适配 2 | 样本极小；claim dispute 2，refill 2，mold 1 | 不足以验证强技术承诺；低负面只能作为初步信号 |
| `B008A4AG2U` | bath-ball、chlorine/lead/impurities、pH-balanced、2500 gallon、easy install、fits most but not universal、BPA-free | 图评确认 bath-ball、挂绳、top grille、refill/handle 包；安装/适配 5，皮肤/头发 3 | 19 条中 42.1% 为 1-2 星；high-kill 8，整体无效 6，overflow 3，refill 2 | 形态真实，但评论支撑弱，且 lead/impurity/long-life 无法靠评论验证 |
| `B0DTQ8H23D` | 8-stage、99% chlorine/heavy metals、baby/sensitive、strong-pressure no-overflow、most faucets、travel-friendly | 宝宝/敏感肌 6，安装/适配 4，水流稳定 3 | high-kill 14/76；整体无效 11，claim dispute 8，quality 8，overflow 7，refill 6 | no-overflow 和强水压卖点与投诉冲突，准确率低 |
| `B0742KFY9R` | organic cotton、99.9% chlorine、magnesium/zinc、sensitive skin/baby/eczema、anti-slip、easy install、2 月/4755 gallon、air dry | 图评确认 cloth/mesh/pouch/loofah-like 形态；安装/适配 21，宝宝/敏感肌 16 | high-kill 142；整体无效 65，mold 57，claim dispute 34，宝宝/敏感肌不稳定 29，quality 29，overflow 25 | soft pouch 形态准确，但净化、矿物、敏感肌和卫生维护承诺被大量评论反证 |

## 结论

1. **最高可信卖点不是“净化百分比”，而是可见结构和操作体验。** Canopy 的 spout-cover、JYFJYF 的 Velcro、Crystal Quest 的 bath-ball 这些形态类卖点更容易被图评/评论验证。
2. **白牌低价产品星级高，不代表 claim 准确。** Beati、Yolycen、JYFJYF、Syvahome 的星级不错，但 `99%`、`heavy metals`、`fluoride`、`hard water softener`、`universal fit` 不能照搬。
3. **最危险的卖点是绝对化结构承诺。** `zero overflow`、`prevents overflow even with strong water pressure`、`fits all tubs` 这类话术一旦评论出现反例，准确率掉得很快。
4. **Santevia 是反面教材。** 它的 soft cloth 形态真实，但用户对内部结构、发霉、效果和敏感肌/宝宝承诺的质疑非常集中。
5. **KES 文案应优先讲可证明边界。** 可讲安装方式、适配范围、过滤路径、可维护性、去氯味体感；不要把硬水软化、TDS、重金属、湿疹改善写成未经验证的确定事实。

## Sources

- Raw scorecard：`raw/products/bathtub-filter/2026-06-02-competitor-claim-review-accuracy-scorecard.csv`
- PDP snapshots：`raw/products/bathtub-filter/reports/bathtub_filter_2026-04-18/raw/rainforest_pdp_{ASIN}_amz_us.json`
- Review evidence chain：`raw/products/bathtub-filter/2026-04-20-competitor-review-corpus/bathtub-filter-competitor-review-labeling-evidence-chain-2026-06-02.csv`
- ASIN review summary：`raw/products/bathtub-filter/2026-04-20-competitor-review-corpus/bathtub-filter-competitor-review-asin-summary-2026-04-20.csv`
- Amazon review image archive：`raw/products/bathtub-filter/2026-06-02-amazon-review-images/`
- Filterbaby moved-out scorecard：`raw/products/shower-filter/filterbaby-claim-review-accuracy-scorecard-2026-06-02.csv`
