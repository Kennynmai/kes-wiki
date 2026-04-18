# Bathtub Filter — ops-platform 维度矩阵 + 跨站点覆盖（2026-04-18）

来源：`kes-ops-platform` Rainforest PDP + LLM 聚类 + BA + SerpAPI  
原始报告：`/reports/bathtub_filter_2026-04-18/`（dimension_matrix.md + cross_site_matrix.md + README.md）

---

## 扫描范围

- 关键词：`bathtub filter` / `bath filter` / `tub filter` / `bathtub water filter` / `bathtub filter for baby` / `bathtub filter for tub faucet` / `canopy bathtub filter`
- 站点：US / CA / UK / DE / JP
- ASIN 样本：13

---

## LLM 发现的三个切分维度

### 维度 1：installation_type

| 值 | ASIN 数 | 月销合计 (US) | 均价 (US) | 代表品牌 |
|---|---|---|---|---|
| `velcro_strap` | 1 | 1K+ | $16 | JYFJYF |
| `faucet_mount` | 2 | 1K+ | $101 | Filterbaby / Canopy |
| `overflow_integrated` | 3 | 2K+ | $21 | SHLLKTTRY / Yolycen |
| `ball_style` | 1 | 500+ | $65 | Crystal Quest |
| `other` | 6 | 4K+ | $41 | Syvahome / Beati Faucet / Tubo / Santevia |

ASIN 明细：

| ASIN | 品牌 | US 价格 | US 月销 | 评论数 | installation_type |
|---|---|---|---|---|---|
| B008A4AG2U | Crystal Quest | $65 | 500+ | 1,165 | `ball_style` |
| B0GFQ1JRSK | Canopy | $89 | 500+ | 57 | `faucet_mount` |
| B0FNVDJRSQ | Filterbaby | $113 | 1K+ | 133 | `faucet_mount` |
| B0CXT5KL5Z | Beati Faucet | $30 | 2K+ | 1,812 | `other` |
| B0742KFY9R | Santevia | $23 | 1K+ | 2,259 | `other` |
| B0D78XBHSW | Beati Faucet | $24 | 1K+ | 1,812 | `other` |
| B0DTQ8H23D | Tubo | $65 | 800+ | 174 | `other` |
| B0G5NZBW6W | Syvahome | $30 | 50+ | 95 | `other` |
| B0GKT5CHYL | Uiuaquas | $72 | — | 21 | `other` |
| B0D3X39378 | SHLLKTTRY | $26 | 1K+ | 1,562 | `overflow_integrated` |
| B0DC3JQ34R | SHLLKTTRY | $20 | 1K+ | 1,563 | `overflow_integrated` |
| B0FL24SLM5 | Yolycen | $16 | 50+ | 128 | `overflow_integrated` |
| B0FT7R9ZQ9 | JYFJYF | $16 | 1K+ | 80 | `velcro_strap` |

---

### 维度 2：housing_material

| 值 | ASIN 数 | 月销合计 (US) | 均价 (US) | 代表品牌 |
|---|---|---|---|---|
| `plastic_abs` | 4 | 3K+ | $44 | Tubo / Crystal Quest / SHLLKTTRY |
| `metal_titanium` | 1 | 1K+ | $113 | Filterbaby |
| `silicone` | 1 | 500+ | $89 | Canopy |
| `fabric_cotton` | 1 | 1K+ | $23 | Santevia |
| `other` | 6 | 4K+ | $31 | Syvahome / Yolycen / Beati Faucet |

ASIN 明细：

| ASIN | 品牌 | US 价格 | US 月销 | 评论数 | housing_material |
|---|---|---|---|---|---|
| B0742KFY9R | Santevia | $23 | 1K+ | 2,259 | `fabric_cotton` |
| B0FNVDJRSQ | Filterbaby | $113 | 1K+ | 133 | `metal_titanium` |
| B0CXT5KL5Z | Beati Faucet | $30 | 2K+ | 1,812 | `other` |
| B0D78XBHSW | Beati Faucet | $24 | 1K+ | 1,812 | `other` |
| B0FT7R9ZQ9 | JYFJYF | $16 | 1K+ | 80 | `other` |
| B0G5NZBW6W | Syvahome | $30 | 50+ | 95 | `other` |
| B0FL24SLM5 | Yolycen | $16 | 50+ | 128 | `other` |
| B0GKT5CHYL | Uiuaquas | $72 | — | 21 | `other` |
| B0D3X39378 | SHLLKTTRY | $26 | 1K+ | 1,562 | `plastic_abs` |
| B0DC3JQ34R | SHLLKTTRY | $20 | 1K+ | 1,563 | `plastic_abs` |
| B0DTQ8H23D | Tubo | $65 | 800+ | 174 | `plastic_abs` |
| B008A4AG2U | Crystal Quest | $65 | 500+ | 1,165 | `plastic_abs` |
| B0GFQ1JRSK | Canopy | $89 | 500+ | 57 | `silicone` |

---

### 维度 3：filtration_approach

| 值 | ASIN 数 | 月销合计 (US) | 均价 (US) | 代表品牌 |
|---|---|---|---|---|
| `multi_stage_chemical_removal` | 8 | 7K+ | $40 | Crystal Quest / Beati Faucet / SHLLKTTRY / Tubo |
| `vitamin_mineral_infusion` | 3 | 1K+ | $23 | Yolycen / Syvahome / Santevia |
| `baby_sensitive_skin_specialized` | 2 | 1K+ | $101 | Filterbaby / Canopy |

ASIN 明细：

| ASIN | 品牌 | US 价格 | US 月销 | 评论数 | filtration_approach |
|---|---|---|---|---|---|
| B0GFQ1JRSK | Canopy | $89 | 500+ | 57 | `baby_sensitive_skin_specialized` |
| B0FNVDJRSQ | Filterbaby | $113 | 1K+ | 133 | `baby_sensitive_skin_specialized` |
| B0CXT5KL5Z | Beati Faucet | $30 | 2K+ | 1,812 | `multi_stage_chemical_removal` |
| B0D3X39378 | SHLLKTTRY | $26 | 1K+ | 1,562 | `multi_stage_chemical_removal` |
| B0DC3JQ34R | SHLLKTTRY | $20 | 1K+ | 1,563 | `multi_stage_chemical_removal` |
| B0D78XBHSW | Beati Faucet | $24 | 1K+ | 1,812 | `multi_stage_chemical_removal` |
| B0FT7R9ZQ9 | JYFJYF | $16 | 1K+ | 80 | `multi_stage_chemical_removal` |
| B0DTQ8H23D | Tubo | $65 | 800+ | 174 | `multi_stage_chemical_removal` |
| B008A4AG2U | Crystal Quest | $65 | 500+ | 1,165 | `multi_stage_chemical_removal` |
| B0GKT5CHYL | Uiuaquas | $72 | — | 21 | `multi_stage_chemical_removal` |
| B0742KFY9R | Santevia | $23 | 1K+ | 2,259 | `vitamin_mineral_infusion` |
| B0G5NZBW6W | Syvahome | $30 | 50+ | 95 | `vitamin_mineral_infusion` |
| B0FL24SLM5 | Yolycen | $16 | 50+ | 128 | `vitamin_mineral_infusion` |

---

## 三个交叉切分视图（README 汇总）

### 视图 A — 品牌 × filtration_approach
（每格：ASIN 数 / 美区月销合计 / 均价）

| 品牌 | multi_stage_chemical_removal | vitamin_mineral_infusion | baby_sensitive_skin_specialized |
|---|---|---|---|
| Beati Faucet | 2 / 3K+ / $27 | — | — |
| SHLLKTTRY | 2 / 2K+ / $23 | — | — |
| Santevia | — | 1 / 1K+ / $23 | — |
| JYFJYF | 1 / 1K+ / $16 | — | — |
| Filterbaby | — | — | 1 / 1K+ / $113 |
| Tubo | 1 / 800+ / $65 | — | — |
| Canopy | — | — | 1 / 500+ / $89 |
| Crystal Quest | 1 / 500+ / $65 | — | — |
| Syvahome | — | 1 / 50+ / $30 | — |
| Yolycen | — | 1 / 50+ / $16 | — |
| Uiuaquas | 1 / 0+ / $72 | — | — |

### 视图 B — 价格带 × installation_type
（每格：ASIN 数 / 美区月销合计）

| 价格带 | velcro_strap | faucet_mount | overflow_integrated | ball_style | other |
|---|---|---|---|---|---|
| <$20 | 1 / 1K+ | — | 2 / 1K+ | — | — |
| $20–40 | — | — | 1 / 1K+ | — | 4 / 4K+ |
| $40–80 | — | — | — | 1 / 500+ | 2 / 800+ |
| >$80 | — | 2 / 1K+ | — | — | — |

### 视图 C — filtration_approach × installation_type
（每格：ASIN 数 / 月销合计 / 均价）

| filtration_approach \ installation_type | velcro_strap | faucet_mount | overflow_integrated | ball_style | other |
|---|---|---|---|---|---|
| multi_stage_chemical_removal | 1 / 1K+ / $16 | — | 2 / 2K+ / $23 | 1 / 500+ / $65 | 4 / 3K+ / $48 |
| vitamin_mineral_infusion | — | — | 1 / 50+ / $16 | — | 2 / 1K+ / $26 |
| baby_sensitive_skin_specialized | — | 2 / 1K+ / $101 | — | — | — |

---

## 跨站点覆盖矩阵

✓ = 有 listing  ✗ = 无  ~ = 有但无 BSR

| ASIN | 品牌 | US 价格 | US 月销 | US | CA | UK | DE | JP |
|---|---|---|---|---|---|---|---|---|
| B0CXT5KL5Z | Beati Faucet | $30 | 2K+ | ✓ BSR#1178 | ✓ BSR#64100 | ✗ | ~ | ~ |
| B0GFQ1JRSK | Canopy | $89 | 500+ | ✓ BSR#4173 | ~ | ✓ BSR#184191 | ~ | ~ |
| B0D3X39378 | SHLLKTTRY | $26 | 1K+ | ~ | ✓ BSR#27911 | ~ | ~ | ~ |
| B0DC3JQ34R | SHLLKTTRY | $20 | 1K+ | ~ | ✓ BSR#27912 | ~ | ~ | ~ |
| B0742KFY9R | Santevia | $23 | 1K+ | ~ | ✓ BSR#259 | ✓ BSR#12572 | ✓ BSR#387542 | ~ |
| B0D78XBHSW | Beati Faucet | $24 | 1K+ | ✓ BSR#1178 | ✓ BSR#478944 | ~ | ~ | ~ |
| B0FT7R9ZQ9 | JYFJYF | $16 | 1K+ | ~ | ~ | ~ | ~ | ~ |
| B0FNVDJRSQ | Filterbaby | $113 | 1K+ | ~ | ✓ BSR#429475 | ✓ BSR#149031 | ~ | ~ |
| B0DTQ8H23D | Tubo | $65 | 800+ | ~ | ✓ BSR#80673 | ✓ BSR#84403 | ✓ BSR#1280679 | ~ |
| B008A4AG2U | Crystal Quest | $65 | 500+ | ~ | ✓ BSR#53583 | ✓ BSR#125925 | ~ | ~ |
| B0G5NZBW6W | Syvahome | $30 | 50+ | ~ | ✗ | ~ | ✗ | ~ |
| B0FL24SLM5 | Yolycen | $16 | 50+ | ~ | ~ | ~ | ✗ | ~ |
| B0GKT5CHYL | Uiuaquas | $72 | — | ~ | ✓ BSR#395924 | ✗ | ✗ | ✗ |

覆盖率：CA 92% / UK 85% / DE 77% / JP 92%

---

## Amazon BA 关键词信号

| 词 | SFR | Top Click ASIN | Click Share |
|---|---|---|---|
| canopy bathtub filter | 63,844 | B0GFQ1JRSK (Canopy) | 17.0% |
| bath filter for tub | 88,333 | B0GFQ1JRSK | 20.0% |
| bathtub filter | 105,780 | B0GFQ1JRSK | 21.8% |
| bath filter | 118,720 | B0GFQ1JRSK | 14.4% |
| bathtub water filter | 140,301 | B0GFQ1JRSK | 13.2% |
| bathtub filter for tub faucet | 225,764 | B0GFQ1JRSK | 22.1% |
| canopy bath filter | 282,995 | B0GFQ1JRSK | **75.9%** |
| tub filter | 306,991 | B0GFQ1JRSK | 20.2% |
| bath filter for baby | 311,326 | B0GFQ1JRSK | 17.7% |

---

## 限制

- `recent_sales` 是 Amazon 前台"X+ purchased"下限值
- SP-API attributes 依赖卖家填写
- LLM 标注基于 title/bullet，可能有误分；详见 `raw/llm_clustering_result.json`
- Rainforest reviews 返回为空，review 情感分析待补
