---
type: product
status: draft
owner: strategy
created: 2026-04-17
updated: 2026-04-17
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, standards, certification, compliance, jurisdiction, eu, japan, uk, australia, canada, china]
source_count: 16
review_cycle: monthly
verification_status: working
related:
  - ./bathtub-filter.md
  - ./bathtub-filter-certification-and-testing-pathways.md
  - ./bathtub-filter-certification-authority-tiers-and-workflow.md
  - ./bathtub-filter-compliance-framework-and-evidence-boundaries.md
  - ./bathtub-filter-claims-and-certifications.md
---
# 浴缸过滤器（bathtub filter）跨辖区标准 / 认证 / 合规对位图

## 为什么有这页
现有 C 层文档（certification-and-testing-pathways / certification-authority-tiers-and-workflow / compliance-framework-and-evidence-boundaries）基本只覆盖北美（NSF / WQA / IAPMO / EPA / FTC）。

但 research-coverage-gaps 原本的问题是：
> **哪些宣称在美国 / 欧盟 / 日本（及其他主要辖区）表面上存在风险？**

这页把北美之外的对位层补齐，回答：
1. 欧盟 / 英国 / 日本 / 澳新 / 加拿大 / 中国对 bathtub filter 这类产品的分类与监管抓手是什么
2. 每个辖区的"正式认证路径"各自是什么、是否强制
3. 一个最关键的 cross-jurisdiction 结构性事实，如何影响 KES 路径选择
4. 跨辖区 claim 风险对照表

## 最关键的一句话
对 bathtub filter 来说，**几乎所有主要辖区的正式认证体系，都是围绕"饮用水接触（potable / drinking-water contact）"建立的**。

但浴缸水按绝大多数辖区的法律定义，**不是饮用水**。

这造成一个结构性张力：
> **正规认证路径对 bathtub filter 天然"不合身"——不是因为产品差，而是因为现行法规框架不是为 bath water 设计的。同时，任何从"去除污染物"跨越到"改善健康结果"的 claim，都会把产品从"日用品"归类一阶跳到更严的 化妆品 / 医疗器械 / 药械 / 广告 监管领域。**

这不只是北美问题，是所有主要辖区的共同结构。

---

## 一、北美基线（简要回顾，详见 C 层既有文档）
| 辖区 | 最相关标准 / 体系 | 适用对象 | 强制性 |
|---|---|---|---|
| 美国 | `NSF/ANSI 177`（shower）/ 42 / 53 / 61 / 372；WQA Gold Seal；IAPMO R&T | 饮用水 POU / POE；shower-filter；lead-content | 自愿为主（部分渠道事实强制）|
| 加拿大 | `NSF/ANSI/CAN` 双范围（同上标准但加 CAN 后缀时适用加拿大 plumbing code） | 同上 | 自愿（部分省 plumbing code 要求）|

北美细节详见 [[bathtub-filter-certification-and-testing-pathways]]。加拿大特殊性：若 SKU 被分类为 plumbing fitting，部分省（BC / Ontario）plumbing code 实际要求认证 mark。

---

## 二、欧盟 / EEA
### 2.1 结构性事实
欧盟**没有一个专门的"浴缸过滤器"成品认证体系**。对 bathtub filter 类产品，监管抓手分散在以下几条线：

#### a) 材料 - 与饮用水接触（4MS 倡议）
**4MS Initiative**（Germany / France / Netherlands，以前含 UK）建立了与饮用水接触材料的认可机制。

- **德国**：`KTW-BWGL`（2021 年起取代 KTW-Leitlinie）评估 organic 材料；`DVGW W 270` 评估 microbial growth
- **法国**：`ACS`（Attestation de Conformité Sanitaire）由 ANSES 认可的实验室出具
- **荷兰**：`Kiwa ATA`（Attest-met-productcertificaat）
- **英国（脱欧后单列，见第三节）**：`Regulation 31`（通常通过 WRAS approval 体现）

**关键边界：**
> 这些认证的法律基础都是"与饮用水（water intended for human consumption）接触的材料"。bath water 按 EU Drinking Water Directive (EU) 2020/2184 的定义**不属于该范围**。

所以：
- 严格来说，KTW / ACS / Kiwa 不是 bathtub filter 的"强制认证"
- 但品牌仍可能自愿去做，作为"材料安全"的信任锚点
- **不能**拿来暗示"水质效能已被认证"——这是材料认证，不是功效认证

#### b) 物质 - REACH / CLP
`REACH` (EC) 1907/2006 覆盖化学物质注册、评估、授权和限制。对 bathtub filter 有意义的点：
- 滤芯所用 activated carbon / KDF / ion exchange resin 等介质成分须符合 REACH
- 附件 XVII 限制物质清单（如某些 phthalates、重金属）
- `CLP` (EC) 1272/2008 处理分类、标签与包装

#### c) 产品责任 - General Product Safety Regulation（GPSR）
2024-12 生效的 `GPSR` (EU) 2023/988 取代旧 GPSD，对"所有非食品消费品"设立安全基线与市场监督义务。bathtub filter 在覆盖范围内，**这是基础门槛不是可选项**。

#### d) 广告 / 宣称 - UCPD + 成员国消费者保护法
`Unfair Commercial Practices Directive` 2005/29/EC 禁止误导性宣称。成员国执法机构各异（英国 ASA、德国 Wettbewerbszentrale、法国 DGCCRF 等）。

#### e) 医疗器械边界 - MDR
`Medical Device Regulation` (EU) 2017/745。一旦 bathtub filter 声称"治疗 / 预防湿疹"或其他医学结果，会被推向 MDR 范围——从消费品品类跳到医疗器械，合规成本跳一个数量级。

### 2.2 欧盟对 KES 的实务含义
- **没有一个"拿到它就能讲很多"的成品认证**——相比北美 NSF 177，欧盟更碎
- **材料合规（KTW / ACS / Kiwa）成本相对可控**，可作为信任锚点，但不能当效能证明
- **GPSR 合规是必做项**
- **任何 medical-outcome claim 都会触发 MDR 风险**——这比 FTC 风险严重一个量级

---

## 三、英国（脱欧后独立体系）
### 3.1 监管体系
- `Water Supply (Water Fittings) Regulations 1999` Reg 4 要求管件符合安全与水质标准；行业常见符合方式是 `WRAS Approval`
- `UKCA` 标志逐步替代 CE（部分类别仍接受 CE 过渡期）
- `General Product Safety Regulations 2005`（英国版）
- `ASA`（Advertising Standards Authority）自律执法，尤其对 health claim 敏感
- `MHRA` 对 medical-device 化宣称执法

### 3.2 对 KES 的实务含义
- WRAS 行业识别度高，适合"材料安全 + 管件合规"叙事
- 但 WRAS 的法律口径是"接触饮用水"，若 bath filter 走 WRAS，理由要写成"材料安全",**不是**"处理了 bath water"
- ASA 对 "helps eczema / baby-safe" 类措辞审查密度很高，历史上 adjudication 很多

---

## 四、日本
### 4.1 结构性事实
日本对 household 水处理产品的监管分为几条主线：

#### a) JIS S 3201 - 家庭用浄水器試験方法
`JIS S 3201` 是家庭用净水器的**试验方法标准**，覆盖自由残余氯、总三卤甲烷、溶解铅、农药、铁、溶解盐、pH 等参数。

**关键边界：**
- JIS S 3201 明确定位是"家庭用浄水器"——饮用水用
- bath filter 不在其标准对象范围内
- 和 NSF 177 一样，是 **"邻近但不匹配"** 的参照物

#### b) JWPA 浄水器協会自主基準
`JWPA`（日本浄水器協会）维护的自主基準，行业内认可度高。同样聚焦家庭用（饮用）净水器。

#### c) 食品衛生法
对"与食品接触的器具、容器包装"有强制要求。若 bath filter 宣称其出水可用于食品料理或饮用，会触发。单纯 bath 用途通常不触发。

#### d) 家庭用品品質表示法
对日用品标签内容有强制要求。bath filter 若进入日本家电 / 日用品渠道，标签语言须符合。

#### e) 薬機法（医薬品医療機器等法）
若 bath filter 宣称治疗 / 预防 / 改善湿疹、アトピー、皮膚炎，会触发 **医薬品 / 医療機器 / 医薬部外品** 分类风险——与 EU MDR 同结构的风险。

#### f) 景品表示法
禁止"不当表示"，包括夸大 / 误导性宣称。消費者庁是主要执法机构，近年对 "科学的根拠" 类 claim 执法显著加强。

### 4.2 对 KES 的实务含义
- **日本市场最容易被 "clinically tested / 皮膚科学" 类措辞拖进景品表示法 + 薬機法双重风险**
- **日本消费者对 "エビデンス" 的要求实际上很高**——若走日本渠道，claim discipline 要比北美更严
- **JIS S 3201 可作为内部 benchmark**，但不能写成产品认证

---

## 五、澳大利亚 / 新西兰
### 5.1 监管体系
- `WaterMark Certification Scheme`（ABCB 管理）对 plumbing products 强制认证；bath filter 若被分类为 plumbing fitting 可能触发
- `AS/NZS 3497` drinking water treatment units（参照 NSF/ANSI 体系）
- `ACCC` 在澳大利亚消费者法（ACL）下执法误导性宣称
- `TGA` 对 therapeutic claims 执法

### 5.2 对 KES 的实务含义
- WaterMark 的分类判断需直接询问 ABCB / 认证机构；bath-tap-attached 产品有被判为 plumbing fitting 的历史
- ACCC 对 "eczema / baby-safe / clinically proven" 执法密度在英语市场里属于较高

---

## 六、中国（参考）
### 6.1 监管体系
- `GB 5749` 生活饮用水卫生标准（对饮用水本身，不直接覆盖产品）
- `涉及饮用水卫生安全产品卫生许可批件`（"涉水批件"）——饮用水接触产品的行政许可
- `保健食品 / 医疗器械 / 化妆品` 分类边界——任何健康功效宣称会被推进这几个分类
- `广告法`对绝对化用语、医疗用语有严格限制

### 6.2 对 KES 的实务含义
- 单纯 bath filter 若不接触饮用水，不必然需要涉水批件，但渠道可能仍要求；须单案咨询省疾控 + 海关
- "宝宝安心 / 湿疹 / 治疗" 类措辞在中国基本直接触发广告法 + 医疗器械分类
- 跨境电商（保税、直邮）与一般贸易合规口径差异大

---

## 七、跨辖区 claim 风险对照表

对 KES 当前最常见的 6 类 claim，各辖区风险锚点速查：

| Claim 原型 | 美国 | 加拿大 | 欧盟 | 英国 | 日本 | 澳新 | 中国 |
|---|---|---|---|---|---|---|---|
| "reduces free available chlorine" | 低（NSF 177 / 42 / WQA 可对位）| 低（同左）| 中（无对位成品认证；可引 DIN EN / 实验室 protocol）| 中（ASA 可能要 substantiation）| 中（JIS S 3201 是 benchmark 非认证）| 低（AS/NZS 3497 可对位）| 中（广告法要 substantiation）|
| "removes heavy metals / fluoride / PFAS" | 高（需对应 NSF 53 / 58 / P473 认证；外推会被 FTC 盯）| 高 | 高（需 substantiation；无直接成品认证路径）| 高（ASA 会要 evidence）| 高（景表法）| 高（ACCC）| 高（广告法 + 涉水批件）|
| "uses NSF-certified media" | 中（object switching 风险；FTC 指引）| 中 | 中（需澄清材料级还是成品级）| 中（ASA）| 中 | 中（ACCC）| 中 |
| "clinically tested / dermatologically tested" | 高（FTC substantiation 要求严）| 高 | 高（UCPD）| 高（ASA 密集执法）| **很高**（景表法 + 薬機法双触发）| 高（ACCC + TGA 边界）| **很高**（广告法 + 医疗器械边界）|
| "helps eczema / safe for babies" | **很高**（FDA cosmetic/device 边界 + FTC）| **很高**（Health Canada）| **很高**（可能触发 MDR）| **很高**（MHRA + ASA）| **很高**（薬機法）| **很高**（TGA）| **很高**（广告法 + 医疗器械）|
| "premium bath ritual / gentler bath water"（软表达）| 低 | 低 | 低 | 低（ASA 仍看是否暗示健康结果）| 低（避免具体医学语）| 低 | 低（避开绝对化用语）|

**读图规则：** "低"不等于零风险；"高"意味着在该辖区如果没有具体证据，写上去就容易出事。

---

## 八、结构性张力：越往健康结果走，分类越跳类
bath filter 在各辖区的分类不是线性的，而是**阶梯跳跃**：

```
【日用品 / 普通消费品】
  ↓ 加 "tested to 某标准"
【声称具备特定水处理效能的产品】（仍在日用品）
  ↓ 加 "helps skin / helps hair / comfort"
【美容 / 护肤邻近话术】（开始接近化妆品边界）
  ↓ 加 "treats / prevents / relieves eczema"
【医疗器械 / 药品 宣称】（合规成本跳一个数量级）
```

**这个阶梯在所有主要辖区都成立。**

跨辖区的 KES 原则因此是一致的：
> **越往上一阶走，对应合规成本不是"多做一份测试"，而是"进入完全不同的监管体系"。**

---

## 九、对 KES 的实务结论
### 9.1 如果产品是 bathtub filter（非 shower）
- **不存在"一次认证打遍所有辖区"的路径**。NSF 177 / WRAS / KTW / JIS S 3201 都是 shower-filter 或 drinking-water 邻近路径，不是 bathtub 本体路径
- **最现实的跨辖区合规组合**：
  1. 材料合规（按市场选 KTW / WRAS / REACH / 涉水批件 / 日本食品衛生法）
  2. 窄 claim（chlorine-focused + 软 comfort）
  3. GPSR / ACL / 景表法 / 广告法 level 的通用消费品合规
  4. 明确规避 health-outcome claim

### 9.2 claim 跨辖区的最强共识
- "reduce / 降低" 比 "remove / 去除" 在所有辖区都更安全
- "designed for / may help / supports" 比 "treats / prevents / proven" 在所有辖区都更安全
- "clinically tested" 在日本 / 中国 / 澳新的风险显著高于美国
- "baby-safe / infant-safe / for eczema" 在所有辖区都是高风险

### 9.3 最不建议的路线
把 "NSF 177" / "WRAS" 这类**北美或英国的名字印在包装上并行销欧盟、日本、澳新**——这些名字在当地不会提供正面的合规保护，反而可能被认定为对本地消费者的误导性权威 impression。

---

## 当前开放问题
1. 若 KES 走日本或欧盟作为首发市场，材料合规路径的具体成本和周期需单独 RFQ（详见 [[bathtub-filter-certification-cost-and-timeline-estimates]]）
2. WaterMark 对 bath-tap-attached 产品的具体分类判例需直接询问 ABCB
3. 中国涉水批件是否强制，取决于产品是否被判定为"涉及饮用水卫生安全产品"，需渠道 / 海关 / 省疾控三方确认

## Obsidian links
- [[bathtub-filter]]
- [[bathtub-filter-certification-and-testing-pathways]]
- [[bathtub-filter-certification-authority-tiers-and-workflow]]
- [[bathtub-filter-compliance-framework-and-evidence-boundaries]]
- [[bathtub-filter-us-state-federal-compliance-sidelines]]
- [[bathtub-filter-certification-cost-and-timeline-estimates]]
- [[bathtub-filter-marketplace-claim-policing-layer]]
- [[bathtub-filter-claims-and-certifications]]
- [[bathtub-filter-claim-risk-audit-v2]]

## Sources
- EU Drinking Water Directive (EU) 2020/2184: <https://eur-lex.europa.eu/eli/dir/2020/2184/oj>
- 4MS Initiative overview (UBA): <https://www.umweltbundesamt.de/en/topics/water/drinking-water/drinking-water-installation/4ms-initiative>
- German UBA KTW-BWGL guidance: <https://www.umweltbundesamt.de>
- DVGW W 270: <https://www.dvgw.de>
- French ANSES ACS: <https://www.anses.fr/fr>
- Dutch Kiwa ATA: <https://www.kiwa.com>
- UK WRAS Approval: <https://www.wras.co.uk>
- REACH Regulation (EC) 1907/2006
- EU GPSR (EU) 2023/988
- EU MDR (EU) 2017/745
- UK Water Supply (Water Fittings) Regulations 1999
- JIS S 3201 abstract via JSA catalogue: <https://www.jsa.or.jp>
- JWPA 浄水器協会: <https://www.jwpa.or.jp>
- 日本 消費者庁 景品表示法: <https://www.caa.go.jp>
- ABCB WaterMark Certification Scheme: <https://www.abcb.gov.au/certification/watermark>
- AS/NZS 3497 Drinking water treatment units overview
- ACCC Australian Consumer Law: <https://www.accc.gov.au>
- 中国《涉及饮用水卫生安全产品卫生许可管理办法》
- 中国《广告法》（2021 修正）
