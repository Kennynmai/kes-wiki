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
domains: [bathtub-filter, marketplace, amazon, walmart, target, claim, compliance, ecommerce, retail-policy]
source_count: 8
review_cycle: monthly
verification_status: working
related:
  - ./bathtub-filter.md
  - ./bathtub-filter-claims-and-certifications.md
  - ./bathtub-filter-certification-and-testing-pathways.md
  - ./bathtub-filter-claim-risk-audit-v2.md
  - ./bathtub-filter-us-state-federal-compliance-sidelines.md
  - ./bathtub-filter-cross-jurisdiction-standards-map.md
---
# 浴缸过滤器（bathtub filter）零售 / 电商平台 claim 审查层

## 为什么有这页
KES 做 claim 合规时，很容易只看**法规 + 第三方认证**这两层，忽略一个事实：

> **实际上把 claim 拦下来的"第一道门"是零售平台自家的政策**，不是 FTC 或 FDA。

Amazon 一次 policy violation 导致的 listing takedown，**比 FTC 发 warning letter 发生得早、发生得频繁、影响更直接**。

这页把 bath filter 会遇到的主要平台审查规则集中起来。

## 一句话结论
> **法规管"你能不能卖"，平台管"你能不能上架"。这两件事的阈值、速度、申诉成本完全不同。做 claim 时，平台政策通常比 FTC 更严，也更快。**

---

## 一、Amazon
Amazon 对 water filter 类产品的审查覆盖多个维度，KES 主要会遇到：

### 1.1 Restricted Products（限售产品）政策
Water filters 本身**不是 Restricted Products**，但以下场景会触发限制：
- 声称可用于 "medical / therapeutic" 用途 → 触发 Medical Device policy
- 声称 removes specific contaminants without certification → 触发 "claims that require certification" 审查
- 包装或 listing 图片含婴儿 + 医疗术语 → 触发 Children's Products + health-claim 双审

### 1.2 Health & Personal Care 类目政策
若 bath filter 走 Health & Personal Care（而非 Home & Kitchen），审查级别更高：
- 任何 disease claim → 必要求 FDA registration / clearance 证明
- "clinical" 类措辞需 clinical trial 文档
- Before / after 图片触发额外审查

### 1.3 A+ Content / Brand Registry 审查
Brand Registry 保护下的 A+ content 会被 Amazon 主动审核：
- 医疗术语（eczema / dermatitis / rash / psoriasis）几乎必被拒
- "clinically proven" 要求上传 substantiation
- 认证 logo 使用要求 certifier 证书

### 1.4 Prop 65 合规字段
Seller Central 的 Prop 65 合规字段未正确填写会导致**加州买家无法下单 / Listing 隐藏**。

### 1.5 典型 takedown 触发链
1. 竞争对手或消费者在 listing 点 "Report a violation"
2. Amazon 自动化审核比对 claim 与 category policy
3. Listing 被 suspend，Seller 收到 Performance Notification
4. 申诉流程：补充 substantiation 文件
5. 申诉成功率在 bath / health-adjacent 类目历来较低，因为通常品牌**本来就没有过硬 substantiation**

### 1.6 对 KES 的实务含义
- **claim 要按 Amazon listing 审核而非仅按 FTC 审核的标准来写**
- **保存好每条 claim 对应的 substantiation 文件，随时可上传**
- **避免走 Health & Personal Care 类目，除非已做好全套合规**——走 Home & Kitchen 审查相对宽松
- **A+ content 里图片中的文字也会被审**——不要把高风险 claim 藏在图片中

---

## 二、Walmart Marketplace / Walmart.com
Walmart 的 Restricted / Prohibited Products 政策与 Amazon 近似，但有差异：

### 2.1 Health claim 审查
Walmart 对 health-adjacent 类目审查密度低于 Amazon（因为 Walmart 这类目营销体量相对低），但一旦 trigger，后果更严：
- Suspend 比 Amazon 更难申诉
- Walmart 一旦下架，对 brand 的长期影响大（因为 Walmart 的 buying process 更人工）

### 2.2 直供（1P）vs. 第三方（3P）
- **1P（Walmart.com 直采）**：buyer 会在上柜前做 compliance package 审查，非常严
- **3P（Marketplace）**：上架门槛较低，但 post-launch 审查可能更突然

### 2.3 对 KES 的实务含义
- 若目标是 Walmart 直供，claim + packaging compliance 要**在上柜前**就达到 buyer 的标准
- 否则 buyer 可能直接不进货——没有"先上再改"的机会

---

## 三、Target
Target 对 bath / personal care / baby 类目审查严格：

### 3.1 Target 的 baby 类目专属审核
若 bath filter 进 Target baby aisle：
- 需通过 Target **Vendor Compliance Program**
- CPSIA 合规证明强制
- Prop 65 + 州级合规文件齐全
- 包装要过 Target design review

### 3.2 Target clean / wellness 话术审查
Target 近年推 "Target Clean" / "clean beauty" 标签体系，对 bath-adjacent 产品 ingredient transparency 要求较高，但**不是认证体系**，是 Target 自家 curator 规则。

---

## 四、Home Depot / Lowe's
plumbing / water filtration 类目在 big-box DIY 渠道：

### 4.1 Home Depot / Lowe's buyer 期望
- NSF 或 WQA 认证（认证 logo 实际影响货架位置）
- UPC / plumbing code compliance（bath-tap-mount 类产品）
- 包装打印 certifier logo 的使用权利证明

### 4.2 对 KES 的实务含义
- **在这两家 big-box 渠道，无认证几乎意味着进不了**
- 这是和 Amazon / DTC 最大的不同

---

## 五、Costco / Sam's Club
Costco 对 bath / personal care 的 member product 审核高度严格：
- 需 full compliance package
- 通常要 third-party certification
- 承担 Costco member 满意度承诺

Costco 一般不是 bath filter 这个 SKU 体量的首选渠道，但值得了解。

---

## 六、DTC / Shopify
### 6.1 平台本身没有 claim 审查
Shopify 不会主动审你 claim。但：
- **Meta / Google / TikTok 广告审核**会执行类似平台 policy
- **Stripe / PayPal** 对 health claim 类产品有 underwriting review，偶尔触发账户冻结
- **州 AG / FTC 对 DTC 的 enforcement 是直接的**，没有"先下架再申诉"的缓冲

### 6.2 对 KES 的实务含义
DTC 反而不是"claim 自由"的避风港：
- 广告平台的 ad disapproval 实际和 Amazon listing takedown 同样频繁
- 州 AG 对 DTC 的起诉速度比对 Amazon seller 快（因为不用走平台中介）

---

## 七、中国跨境 / 国内电商平台
### 7.1 Tmall / 天猫国际 / JD 国际
- 跨境保税：进关审查相对宽松；平台内审查按广告法
- 一般贸易：涉水批件 + 中国强制认证（若适用）+ 广告法审查

### 7.2 小红书 / 抖音（营销侧）
- 对 "湿疹 / 治疗 / 医疗" 类话术审核密度极高
- 被平台限流 / 下架的速度比监管介入快很多

---

## 八、平台审查与法规审查的速度对比
| 维度 | 平台审查（Amazon / Target 等）| 法规审查（FTC / FDA / 州 AG）|
|---|---|---|
| 触发门槛 | 较低（算法 + 竞对举报）| 较高（需 pattern / 消费者投诉量）|
| 反应速度 | 24 – 72 小时 | 数月至数年 |
| 后果严重性 | Listing 下架、账户 suspend | Warning letter、罚款、consent decree、下架潮 |
| 申诉难度 | 中等（靠 substantiation）| 高（需律师）|
| 对品牌长期影响 | 短期（可 relaunch）| 长期（记录公开）|
| 发生频率 | 高 | 低，但放大效应强 |

---

## 九、KES 上市前平台合规清单
### 9.1 前期决策
- [ ] 确定主渠道是 Amazon / DTC / Big-box / 跨境
- [ ] 每个渠道的 claim 审查门槛单独评估
- [ ] 不同渠道是否允许不同 claim wording（通常不允许差异过大）

### 9.2 substantiation 文件包
对每个 claim 准备：
- [ ] 出具方（lab / certifier / supplier）名称
- [ ] 测试 / 认证的 exact scope
- [ ] 测试条件（flow / temperature / pressure / duration）
- [ ] 报告 / listing / certificate 原件扫描
- [ ] 有效期

### 9.3 Listing 层
- [ ] Amazon Prop 65 字段正确
- [ ] 类目选择合规（Home & Kitchen vs. Health & Personal Care 决策）
- [ ] A+ content 文字 + 图片文字双重过审
- [ ] Before / after 图如使用，有 substantiation

### 9.4 广告层
- [ ] Meta / Google / TikTok 广告草稿过 platform policy audit
- [ ] Stripe / PayPal 若 DTC，预先与支付方沟通产品类目

---

## 十、最常见的"不是没做合规，是没过平台"的出事模式
1. 全套 NSF 177 认证做了 → Amazon listing 因 A+ content 用了 "clinically proven" 被 suspend
2. 页面本身没问题 → Amazon 类目选错（选到 Health & Personal Care）→ 触发额外审查门槛
3. DTC 网站合规 → Meta 广告因 before / after 被反复 disapprove 无法投流
4. Walmart 1P buyer 看包装上 "for babies" → 直接不进货
5. 天猫国际上架成功 → 小红书内容被限流 → 无法引流

---

## Obsidian links
- [[bathtub-filter]]
- [[bathtub-filter-claims-and-certifications]]
- [[bathtub-filter-certification-and-testing-pathways]]
- [[bathtub-filter-certification-authority-tiers-and-workflow]]
- [[bathtub-filter-compliance-framework-and-evidence-boundaries]]
- [[bathtub-filter-cross-jurisdiction-standards-map]]
- [[bathtub-filter-us-state-federal-compliance-sidelines]]
- [[bathtub-filter-certification-cost-and-timeline-estimates]]
- [[bathtub-filter-claim-risk-audit-v2]]
- [[bathtub-filter-channel-positioning-table-v2]]

## Sources
- Amazon Seller Central Restricted Products: <https://sellercentral.amazon.com/help/hub/reference/external/200164330>
- Amazon Seller Central Health & Personal Care policy
- Amazon Brand Registry A+ Content guidelines
- Walmart Marketplace Prohibited Products: <https://sellerhelp.walmart.com>
- Target Vendor Compliance Program overview
- Meta Advertising Standards (health & wellness section): <https://www.facebook.com/policies/ads>
- Google Ads healthcare and medicines policy: <https://support.google.com/adspolicy>
- 小红书社区规范 / 抖音广告审核规则（公开版本）
