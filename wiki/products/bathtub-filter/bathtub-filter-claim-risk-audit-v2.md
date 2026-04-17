---
type: product
status: draft
owner: strategy
created: 2026-04-12
updated: 2026-04-17
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, claims, compliance, normalized]
source_count: 12
review_cycle: monthly
verification_status: spot-checked
related:
  - ./bathtub-filter-claim-risk-audit.md
  - ./bathtub-filter-evidence-matrix.md
  - ./bathtub-filter-content-ecosystem-by-layer.md
  - ../../source-summaries/bathtub-filter-content-ecosystem-url-harvest-2026-04-17.md
---
# 浴缸过滤器（bathtub filter）宣称风险审核 — V2

## 页面定位（与相关页面的分工）
> **本页关注：** 市场上真实出现的宣称措辞的逐条风险评估与 KES 姿势（"这句话能不能用？"）
> **Claim Evidence Ladder** 关注：宣称等级框架（"什么证据对应什么等级宣称？"）
> **Evidence Matrix** 关注：当前已有证据的覆盖范围（"我们有什么证据？"）
> **Claim Register** 关注：KES 正式批准 / 条件允许 / 禁用宣称清单（最终操作 reference，待竞品调查后完善）

## 版本链接
- 早期页面：[[bathtub-filter-claim-risk-audit]]

|宣称类别 |出现的措辞示例 |来源主播|证据姿势|风险| KES姿势|
|---|---|---|---|---|---|
|游离氯减少 | “有助于去除游离氯” |雪碧/NSF-177-相邻淋浴环境|相对最强|低-中 |可使用精确的措辞|
|更快的氯性能 | “唯一能够以更快的流量（flow）减少 100% 氯的产品” | Santevia 上的 WaterFilterGuru |如果独立复制的话，比一般的氯声称更强 |中等|如果可重复，则有价值的差异化因素|
|广泛的污染物堆栈|重金属、VOC、PFAS、农药、数百种污染物 | Crystal Quest / 市场通用内容 |常常是宽泛且不具体的路线 |高|除非经过严格验证，否则应避免 |
|敏感肌肤舒适 |沐浴更温和，水疗般更舒适| Canopy / 生活方式/社论/产品页面 |商业但间接|中等|如果不接受医疗也可以使用|
|婴儿安全/家长放心 |婴儿沐浴用品“每个父母都需要的沐浴过滤器”/“价值 89 美元”| Instagram / 母亲 / Canopy |情感强大，证据充足|高|高度谨慎|
|改善肌肤水合作用 | “经过临床测试，可改善皮肤水合作用” |金德浮出水面副本 |需要比本次传递中出现的更强有力的证据|非常高|视为危险信号语言 |
|湿疹改善| “缓解……湿疹”/湿疹友好型挂钩 | Kinder / Tubo / 社交挂钩 |最强商业诱惑，最弱清晰验证的成品证明|非常高|避免直接功效声明|
|临床/已证实的优越性 | “经过临床测试”/“经过验证”|吐博/金德|上下文常常不够明显 |非常高|积极审计|
|硬水软化|软化硬水/平衡硬水|市场和一些广泛的内容|对紧凑型浴缸过滤系统的支持薄弱高|可能避免 |
|认证与测试歧义 | “经过 NSF 177 测试”与经过认证 | WaterFilterGuru 谈 Canopy 淋浴环境 |批评性措辞的区别|高|始终将测试与认证分开 |

## 经销商 / 品牌博客层（Layer C）观察到的 claim-stacking 模式
2026-04-17 新增。单条宣称的风险在上表已评估，但**多条宣称叠加在同一页**才是 Layer C 的真正风险形态。
以下三种 stacking 模式来自 [[bathtub-filter-content-ecosystem-url-harvest-2026-04-17]] 的 WebFetch verbatim 抽取，
不是推测。

### 模式 1：广谱污染物 × 无限定的"rejuvenate / free from dryness" × 隐含健康护盾
- 典型页面：[Carbon Wellness MD — Crystal Quest Bath Ball](https://carbonwellnessmd.com/products/crystal-quest-bath-ball-filter)
- 页面 verbatim 要素：
  - "eliminates chlorine, chloramines, VOCs, THMs, pesticides, sulfur, heavy metals..."（12 类广谱清单）
  - "rejuvenate your skin and hair texture"（无限定 cosmetic 承诺）
  - "shields you from potential health hazards"（隐含健康保护）
- 为什么危险：该页**没有**任何 certification / clinical testing / 第三方验证语言。
  三类高风险宣称（广谱污染物 + cosmetic 结果 + 健康保护）被堆在同一页，
  在用户心里合成出"这是经过验证的"印象，哪怕证据链未给出。
- KES 姿势：**禁用这种组合**。任一单项 KES 想使用时必须附带限定词与证据锚点；
  尤其不应在同一页**同时**出现三类语言。

### 模式 2：专利滤材 × 皮肤补水 × 呼吸保护 × 头发 ×（缺席）fit 边界
- 典型页面：[PureShowers blog — Sprite Bath Ball](https://www.pureshowers.co.uk/shower-filter-blog/revitalise_your_bath_experience_with_the_sprite_bath_ball_bath_filter)
- 页面 verbatim 要素：
  - "patented water filter medium called Chlorgon"（专利锚点）
  - "maintain the skin's moisture balance, reducing the risk of dryness"
  - "promoting healthier-looking skin"
  - "reducing the risk of respiratory irritation"（从皮肤扩展到呼吸）
  - "bathing in filtered water significantly improved skin hydration"（科研化口吻）
  - 页面**不写** tub compatibility / 龙头几何 / 合适流速
- 为什么危险：专利语言被当作"证据替身"，然后被用来支撑跨系统（皮肤 → 呼吸）的承诺；
  同时完全不交代适配边界——这是 marketplace 上 slip / overflow / universal-fit 投诉的**上游文案起点**
  （详见 [[bathtub-filter-marketplace-negative-review-signals]]）。
- KES 姿势：
  - 专利 / Chlorgon 式"patented media"语言**不得**与身体系统跨级承诺（皮肤→呼吸→头发）同页出现
  - 任何 product / blog 页必须包含 fit & flow 边界段落，不留白

### 模式 3：lab-tested × clinically proven × clinically tested × eczema 直接功效
2026-04-17 **更新：本模式已由 WebFetch verbatim 抽取独立确认**，不再是从搜索摘要推测。

#### 典型页面 A：[Kinder Filter — Skincare Bath Filter](https://www.kinderfilter.com/products/skincare-bath-filter)
- 页面 verbatim 要素（同一页内同时出现）：
  - "Lab-tested to remove up to 99% of chlorine, heavy metals & irritants"（benchmark 测试）
  - "Clinically proven to calm sensitive, eczema-prone skin"（人体结果）
  - "clinically tested to remove 99.5% of impurities while enriching water"（前两者的混合）
  - "87% noticed their child stopped itching and scratching after one week"（survey %）
  - "88% reported in improved hydration and reduced redness of skin"（survey %）
  - "designed by healthcare professionals"（权威光环）
  - "certified third-party skin hydration lab measurement testing"（novel phrase，非任何公认标准名称）
- 证据质量：**没有任何研究名、样本量规范（页面仅暗示"100 families / 2 weeks"）、peer-review 状态或发表引用。**
  87% / 88% 实为 user survey，不是 controlled clinical trial；但页面语言暗示同等可信度。

#### 典型页面 B：[Tubo 2.0 Bath Filter](https://trytubo.com/products/new-tubo-2-0-bath-filter)
- 页面 verbatim 要素：
  - "CLINICALLY TESTED"（header claim，无下方支撑）
  - "Removes up to 99% of chlorine, heavy metals, and bacteria"
  - "Removes up to 99.9% of bacteria and viruses"（**高风险**：bath-ball 做到 viral-level removal 通常需 NSF P231 级证据，页面上没有）
  - "Filters out harmful heavy metals like lead, mercury, and arsenic"（具名金属更激进）
  - "Within 2 baths using the filter his eczema is 90% better!"（testimonial，承担 eczema 功效举证）
  - "if your baby has a specific skin condition, we always recommend consulting with your pediatrician or dermatologist"（部分法律对冲）
- Tubo 的替代路径：Kinder 用 survey %，Tubo 用 testimonial——**目的相同（未验证 eczema 功效），修辞路径不同。**

#### Kinder vs Tubo 要素对比（全部来自 2026-04-17 verbatim 抽取）
| 要素 | Kinder | Tubo |
|---|---|---|
| "clinically tested" 语言 | ✓（"clinically tested" + "clinically proven"）| ✓（"CLINICALLY TESTED" header）|
| 支撑研究 | 无；仅 survey % | 无；仅 testimonial |
| 氯去除 % | "up to 99%" | "up to 99%" |
| 重金属 | "heavy metals & irritants" | "lead, mercury, arsenic"（更具名）|
| 细菌 / 病毒 | 未声称 | "99.9% of bacteria and viruses" **(高风险)** |
| Eczema 功效 | "Clinically proven to calm... eczema-prone skin" | 由 testimonial 承担 |
| 医疗权威 | "designed by healthcare professionals" | "consult with your pediatrician or dermatologist"（对冲）|
| 第三方认证 | "certified third-party skin hydration lab measurement testing"（novel phrase）| 无 |

#### 为什么危险
把 **lab-tested**（滤材台架测试）、**clinically tested**（上下文模糊）、**clinically proven**（人体终点结果）
并列放在同一页——三种语言在用户心里合成"被权威验证过"的感觉。
实际上：
- lab-tested 指的是把滤材放在 bench test 上跑污染物去除
- clinically proven（bathtub filter 上）通常是某种 user-survey 或小样本 hydration 测试
- 两者证据等级差距一个数量级，但放在一起就被均质化

#### KES 姿势
- "clinically proven"、"clinically tested"、"clinically validated" **在 bathtub filter 品类下默认禁用**，
  除非 KES 自己有设计良好、第三方主持、引用得当的人体试验（当前证据条件不允许）
- "lab-tested" 若使用，**必须**同页声明测试对象（滤材 or 产品）、测试条件（flow rate, 水样）、出具方
- 任何 eczema 相关语言只能在 comfort-framing 下使用，**不得**与 "proven / tested / validated" 类语言同页
- testimonials 可用，但**不得**作为 eczema 功效的唯一证据（Tubo 路径不可复制）
- "designed by healthcare professionals" 类**权威光环语**建议默认禁用，除非可点名、可链接
- "99.9% bacteria / virus" 类声明**默认禁用**；若使用必须附 NSF P231 或同等标准证明

### 跨模式共性：证据等级混用是 Layer C 的核心风险放大器
三种模式虽然堆叠对象不同，但核心风险机制相同：
> **把不同证据等级（patented / tested / independently tested / clinically tested / clinically proven）
> 当作同义词并列使用**——用户读到的是一团模糊的"可信感"，而监管、评测层（A）与社区层（D）
> 看到的是可以逐条反击的把柄。

### 对应的 KES 文案红线（初稿，待 claim-register 正式化）
1. 同一页最多出现一个证据等级语言锚点；不并列。
2. 广谱污染物清单若使用，必须分行标注每类的证据强度与测试条件（"tested at X flow"）。
3. "rejuvenate / free from dryness / healthier-looking skin" 类无限定 cosmetic 承诺，
   在 bathtub filter 品类下默认**不单独出现**——必须与具体、可验证机制绑定。
4. "shields / protects / defends" 类健康护盾语言默认禁用。
5. 任何 product / blog 页必须有 fit & flow 边界段落。

## 工作总结
这一类别中最具商业吸引力的措辞往往是最没有辩护意义的。 KES 应将婴儿/湿疹/临床语言视为最严格的审查区域。

更重要的是：Layer C 的**单条宣称风险**并不新，但**单页内的 stacking** 才是实际被监管、评测与社区反击的命中点。
因此 [[bathtub-filter-claim-register]] 的下一轮更新应当在"逐条宣称"之外，增加"单页 stacking 规则"一节。
