---
type: product
status: draft
owner: product
created: 2026-06-03
updated: 2026-06-03
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, reviews, water-quality, testing, customer-evidence]
source_count: 1
review_cycle: monthly
verification_status: keyword_coded_review_analysis
related:
  - ./bathtub-filter.md
  - ./bathtub-filter-competitor-review-labeling-analysis-2026-06-02.md
  - ./bathtub-filter-review-patterns-and-return-risk.md
  - ./bathtub-filter-test-gating-checklist-for-kes.md
---

# 客户如何判断 bathtub filter 是否改善水质（2026-06-03）

## 口径

本页分析 bathtub-filter raw 评论中，客户如何判断“水质是否变好”，以及他们具体在测试什么。

数据源：`raw/products/bathtub-filter/2026-04-20-competitor-review-corpus/bathtub-filter-competitor-review-corpus-2026-04-20.normalized.csv`

处理口径：

- 排除已拆到 shower-filter 项目的 Filterbaby `B0FNVDJRSQ`。
- active bathtub-filter 样本为 10 个 ASIN、2562 条评论。
- 统计单位是“评论条数”，不是关键词出现总次数。
- 一条评论可以同时计入多个类别，例如同时提到 TDS、chlorine 和 before/after。
- 这是关键词初筛，不等于人工逐条编码；用于判断客户测试语言和测试习惯。

## 核心结论

1. 客户绝大多数不是用专业工具测试，而是用皮肤/头发触感、氯味、视觉清澈度判断。
2. 真正借助外物测试的评论只有 29 条；工具类测试里，TDS/PPM 比 chlorine 更常见。
3. TDS/PPM 经常被客户拿来判断 filter 是否有效，但 TDS 不能直接证明去氯能力。KES 后续测试和文案必须主动解释测试边界，避免被“我用 TDS 笔测了没变化”这类评论反噬。
4. 客户最在意的“水质”并不是单一化学指标，而是皮肤/头发体感、氯味、硬水感、宝宝/敏感肌表现和可见脏污的组合。

## 测试 / 判断方式排序

| 排名 | 方法 | 提及次数 |
|---:|---|---:|
| 1 | 触觉：皮肤、头发、水感、干痒、柔软度 | 1562 |
| 2 | 嗅觉：氯味、泳池味、异味 | 361 |
| 3 | 视觉：清澈/浑浊、颜色、颗粒、残留、霉斑、锈迹 | 320 |
| 4 | 前后对比：before/after、with/without、filtered vs unfiltered | 20 |
| 5 | TDS 仪 / water quality meter / PPM 读数 | 16 |
| 6 | 试纸：chlorine strip、hard-water strip、pool/spa strip | 9 |
| 7 | 其他 tester / water quality test / heavy-metal tester | 4 |
| 8 | water/chlorine test kit | 2 |
| 9 | RO / reverse-osmosis 水作为对照 | 2 |
| 10 | lab / 第三方实验室测试 | 2 |
| 11 | reagents / 试剂 | 2 |

## 借助外物时，客户测试什么

借助外物测试的唯一评论数是 29 条。下表有重叠，因为同一条评论可能同时用了试纸、RO 对照，并记录 PPM。

| 排名 | 测试对象 | 提及次数 |
|---:|---|---:|
| 1 | TDS / PPM / dissolved solids | 14 |
| 2 | 泛化 water quality / contaminants / impurities，未说清具体指标 | 12 |
| 3 | 氯 / chlorine / residual chlorine | 9 |
| 4 | 皮肤、头发、刺激感、柔软度 | 6 |
| 5 | 硬水 / hardness / softening | 5 |
| 6 | 气味 / chlorine smell / pool smell | 3 |
| 7 | 铅 / heavy metals | 1 |
| 8 | pH | 1 |
| 9 | fluoride | 0 |
| 10 | 颗粒/沉淀/残留 | 0 |

## 全评论中被拿来判断水质的对象

| 排名 | 判断对象 | 提及次数 |
|---:|---|---:|
| 1 | 皮肤/头发/刺激/柔软度 | 1424 |
| 2 | 氯 / chlorine | 436 |
| 3 | 硬水/硬度/软化 | 396 |
| 4 | 气味/泳池味 | 361 |
| 5 | 沉淀/颗粒/残留/脏水 | 73 |
| 6 | 霉菌/卫生风险 | 68 |
| 7 | 铅/重金属 | 43 |
| 8 | 铁/锈 | 26 |
| 9 | fluoride | 20 |
| 10 | TDS/PPM | 14 |
| 11 | pH | 5 |
| 12 | chloramine | 2 |

## 借助外物测试的 ASIN 分布

| ASIN | 借助外物测试评论数 |
|---|---:|
| `B0D3X39378` | 12 |
| `B0DTQ8H23D` | 7 |
| `B0742KFY9R` | 5 |
| `B0CXT5KL5Z` | 1 |
| `B0FL24SLM5` | 1 |
| `B0G5NZBW6W` | 1 |
| `B0GFQ1JRSK` | 1 |

## 对 KES 测试设计的含义

1. **必须测 chlorine，但不能只测 chlorine。** 评论里 chlorine 是高频问题词，但用户实际感知还包括气味、肤感和硬水感。
2. **必须准备 TDS 解释。** 很多用户会用 TDS/PPM 判断产品是否“真的过滤”。如果 KES 的核心能力是去氯而非降低 TDS，页面和说明书要明确：TDS 不是去氯测试。
3. **建议在说明书里给出用户可复现的简易测试方法。** 例如 chlorine strip 的使用边界、取样方式、正常流速/慢流速分别测什么，避免用户用错误工具得出“无效”结论。
4. **前后对比要标准化。** 评论里大量 before/after 是主观对比；如果 KES 要引用用户测试，必须要求同一水源、同一流速、同一接触时间、同一试纸/试剂。
5. **文案不要把 hard water、TDS、heavy metals 写成未经验证的确定去除。** 这些是最容易被工具测试挑战的 claim。

## Sources

- Review corpus：`raw/products/bathtub-filter/2026-04-20-competitor-review-corpus/bathtub-filter-competitor-review-corpus-2026-04-20.normalized.csv`
- Related review analysis：[[bathtub-filter-competitor-review-labeling-analysis-2026-06-02]]
- Review risk context：[[bathtub-filter-review-patterns-and-return-risk]]
- Validation planning：[[bathtub-filter-test-gating-checklist-for-kes]]
