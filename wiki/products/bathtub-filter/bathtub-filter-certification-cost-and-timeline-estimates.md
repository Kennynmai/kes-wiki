---
type: product
status: draft
owner: strategy
created: 2026-04-17
updated: 2026-04-17
visibility: team
confidence: low
officiality: draft
domain: product
domains: [bathtub-filter, certification, cost, timeline, budgeting, compliance]
source_count: 6
review_cycle: monthly
verification_status: working
related:
  - ./bathtub-filter.md
  - ./bathtub-filter-certification-and-testing-pathways.md
  - ./bathtub-filter-certification-authority-tiers-and-workflow.md
  - ./bathtub-filter-cross-jurisdiction-standards-map.md
  - ./bathtub-filter-us-state-federal-compliance-sidelines.md
---
# 浴缸过滤器（bathtub filter）认证 / 测试成本与周期参考区间

## 为什么有这页
现有 C 层文档对认证流程的描述是**定性的**："时间长、费用高"。

但 KES 做 go / no-go 决策时，需要的是**可以直接写进 execution plan 的数量级**：
- 一次 NSF 177 对位测试大概是 5 位数还是 6 位数美元？
- 走到 full certification 是 6 个月还是 18 个月？
- 先 third-party testing、之后再升级到 certification，省多少？

这页提供**基于公开信息与行业常见区间的数量级参考**，用于早期预算与路径选择。

## ⚠️ 使用本页前必读
### 1. 这些数字不是报价单
本页所有数字都是**行业常见区间**，来源包括：
- 认证机构公开费用表（部分）
- 二级行业文献 / 合规顾问公开表述
- 可比品类（shower filter / drinking water POU）的历史 benchmark

**真实费用必须通过向认证机构 / 第三方 lab 直接 RFQ 获得**，并受以下变量显著影响：
- 产品 BOM 复杂度
- 被认证 claim 的数量
- 工厂审核频率
- 是否涉及多 SKU 家族
- 是否涉及 contested / novel claim

### 2. 数字是"下单那一刻"的成本，不是总投入
真正的 total cost of compliance 还包括：
- 送样前的工程迭代
- 文案 / 包装 re-design
- 供应商合规文件收集
- 律师审核
- 失败重测

经验上，**"下单费用"通常只占总合规投入的 30-50%**。

### 3. 下表所有数字仅供 order-of-magnitude 判断
**不要直接写进合同 / 预算报告 / 投资人材料。**

---

## 一、北美认证路径 - 数量级参考

### 1.1 NSF 认证（shower-adjacent SKU 走 NSF 177）
| 环节 | 数量级（USD）| 备注 |
|---|---|---|
| 申请 / 工程评审 fee | $5k – $15k | 一次性 |
| Performance testing（chlorine reduction claim only）| $10k – $30k | claim 越多越贵 |
| Toxicology / extraction testing（材料安全）| $10k – $40k | 与 BOM 复杂度相关 |
| Facility audit（首次）| $3k – $8k | + 工厂差旅 |
| 年审 / Listing fee（年度）| $3k – $10k/年 | 永续 |
| **首年 total 下单费用 - 典型区间** | **$30k – $100k** | 单 SKU、窄 claim |
| Timeline（送样到出 listing）| 6 – 12 个月 | claim 越多越慢 |

**扩 SKU 家族成本**：相同平台、不同规格的 SKU 往往可以 grouping，每新增 SKU 的增量成本在 $5k – $20k，不是线性重新计费。

### 1.2 WQA Gold Seal
WQA 官方公开的是 **fee schedule framework**，实际价格与 NSF 大致同档，**部分环节 10-30% 偏低**，但依测试项目而定。

Timeline 与 NSF 近似（6 – 12 个月）。

### 1.3 IAPMO R&T
IAPMO 对 plumbing / fixture-adjacent 产品的 pricing 与 NSF / WQA 可比。对 fixture-adjacent route 有时是**更便宜的合规路径**，但消费者识别度较低。

### 1.4 NSF/ANSI 372 lead-content 单项
作为独立项，费用数量级 **$5k – $15k**，timeline 2 – 4 个月。很多品牌先做这一项，其他延后。

---

## 二、第三方测试（不走 certification）- 数量级参考

若只做 accredited third-party lab testing、不走 full certification：

| 场景 | 数量级（USD）| Timeline |
|---|---|---|
| Chlorine reduction only（按 NSF 177 protocol）| $3k – $8k | 3 – 8 周 |
| 多参数扩展（chlorine + chloramine + heavy metals 抽样）| $10k – $25k | 6 – 12 周 |
| Leachate / material safety 单项 | $2k – $6k | 3 – 6 周 |
| Realistic-flow 自定义 protocol | $5k – $15k | 4 – 10 周 |

常见 North America lab 包括：Eurofins、IAPMO R&T、SGS、Intertek、NSF Labs（可做 testing only，不发 listing）。

**这条路的好处：**
- 成本低一个档
- 时间快
- 适合 early-stage feasibility / R&D
- 可作为未来 full certification 的数据基础

**这条路的限制：**
- **不能在包装上写 "certified"**
- 可以写 "tested to [standard] under specified conditions"（但要有边界描述）
- 不能享受 listing database 的消费者核验信任

---

## 三、欧盟合规 - 数量级参考

### 3.1 材料合规（按市场选 4MS 中的一个或多个）
| 方案 | 数量级 | Timeline |
|---|---|---|
| 德国 KTW-BWGL | €5k – €20k | 3 – 9 个月 |
| 法国 ACS | €8k – €25k | 6 – 12 个月 |
| 荷兰 Kiwa ATA | €5k – €18k | 3 – 9 个月 |
| 英国 WRAS Approval | £4k – £15k | 3 – 9 个月 |

### 3.2 其他必做 EU 合规
- REACH 合规咨询 / 文件整理：€3k – €10k 一次性
- GPSR 合规文件（self-declaration + technical file）：€2k – €8k
- CE / UKCA marking（如适用，视分类）

### 3.3 欧盟总合规量级
若目标是"欧盟材料合规 + REACH + GPSR"做基础：**典型首年 $30k – $80k**，Timeline 6 – 12 个月。

---

## 四、日本合规 - 数量级参考
### 4.1 JIS S 3201 对位测试
若仅做 benchmark（非正式 JWPA 认证）：
- 约 ¥1M – ¥4M（约 $7k – $30k），Timeline 2 – 4 个月

### 4.2 JWPA 认证（若选走）
JWPA 自主基準认证的公开费用表不完全透明，行业常见区间 **¥3M – ¥10M**（约 $20k – $70k），Timeline 6 – 12 个月。

### 4.3 薬機法 / 景表法咨询
合规律师 / 药機コンサル 咨询：¥500k – ¥2M / 项目，视 claim 复杂度。

---

## 五、中国合规 - 数量级参考
### 5.1 涉水批件（如被判定需要）
- 送检 + 许可：约 ¥50k – ¥200k（约 $7k – $28k），Timeline 6 – 12 个月
- 注：bath filter 是否需涉水批件需省疾控 + 海关确认

### 5.2 广告法合规
- 入驻天猫 / 京东需平台审核，单独成本较低但审核周期拉长上架

---

## 六、隐性成本清单
以下常被遗漏：
1. **样品 / 送检样机成本**：几十个 SKU 级别的送检可能占 $5k – $20k
2. **BOM 变更导致的重测**：任何材料供应商更换，通常需重测（或至少提交 engineering change notice）
3. **包装 / 说明书 re-design**：过了 certifier literature review 后经常需要改版，内部或外包设计 $3k – $15k
4. **供应商合规文件收集**：物料级 SDS / RoHS / REACH / Prop 65 declaration 收集耗时大，外包代办 $3k – $10k
5. **年审 / 监督**：认证不是一次性，年费 + facility audit 是永续成本
6. **法律审查**：每轮 claim / 包装 / 广告 语言审查，$2k – $10k/轮
7. **失败重测**：首次测试失败率行业估计 20 - 40%，一旦失败，重测成本 + 时间全部再来一遍

---

## 七、KES go / no-go 决策参考
### 7.1 如果预算 < $20k
现实选择是：**仅做 accredited third-party testing + 窄 claim + 先上北美一个市场**。不要冲 formal certification。

### 7.2 如果预算 $20k – $100k
可考虑：
- 一个市场的正式认证（NSF 177 或 WQA）或
- 两个市场的 third-party testing + 材料合规

### 7.3 如果预算 > $100k
可考虑：
- 北美 formal certification + 欧盟材料合规 + 日本合规咨询 并行启动

### 7.4 成本相对于品类的现实感
bath filter 是相对 low-ASP（年销售额）的品类，很多 SKU 全年收入可能就在 $100k – $500k 级别。这意味着：
> **正式认证投入回收可能需要 2 - 4 年，不是 2 - 4 个月**。

这把认证路径推向两极：
- **要么只做最窄 claim 的 NSF 177 / WQA 一家认证**（与 premium 定位匹配）
- **要么完全不做认证、只做 third-party testing**（与 mainstream 定位匹配）

中间路线（多家认证但 SKU 数量小）在经济上通常划不来。

---

## 八、RFQ 前需要先定清楚的 8 件事
直接向 NSF / WQA / IAPMO / Eurofins / SGS / Intertek 询价前，以下问题先内部定清楚，否则报价偏差可能 ±100%：

1. 被认证对象：**整机 / cartridge / media**？
2. 目标 claim 列表：**逐条写清楚**
3. BOM：完整物料清单 + 供应商
4. SKU 数量：**是否 grouping**
5. 工厂地点 + 数量
6. 年产量量级
7. 目标市场（影响 standard 选择）
8. 时间窗口：**首批上市 deadline**

这 8 个字段直接决定 quote 的准确性。**越模糊，报价越保守（偏贵）**。

---

## Obsidian links
- [[bathtub-filter]]
- [[bathtub-filter-certification-and-testing-pathways]]
- [[bathtub-filter-certification-authority-tiers-and-workflow]]
- [[bathtub-filter-cross-jurisdiction-standards-map]]
- [[bathtub-filter-us-state-federal-compliance-sidelines]]
- [[bathtub-filter-marketplace-claim-policing-layer]]
- [[bathtub-filter-kes-rd-and-validation-roadmap]]
- [[bathtub-filter-test-gating-checklist-for-kes]]

## Sources
- NSF Product Certification overview: <https://www.nsf.org/certification-services/consumer-products>
- WQA Product Certification fee schedule framework: <https://wqa.org/grow/product-certification/>
- IAPMO R&T certification services: <https://iapmort.org/certification-services/water-systems-certification>
- Eurofins consumer products testing catalogue: <https://www.eurofins.com>
- Intertek water product testing: <https://www.intertek.com>
- WRAS Approval scheme overview: <https://www.wras.co.uk>
- 注：行业 practitioner forums / trade publications 为辅助信息源，不作为权威 pricing 依据
