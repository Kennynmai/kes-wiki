---
type: synthesis
status: draft
owner: strategy
created: 2026-04-12
updated: 2026-04-17
visibility: team
confidence: medium
officiality: draft
domain: strategy
domains: [bathtub-filter, patents, technical-landscape, product-architecture]
source_count: 20
review_cycle: monthly
verification_status: spot-checked
related:
  - ../products/bathtub-filter/bathtub-filter.md
  - ../products/bathtub-filter/bathtub-filter-patent-table.md
  - ../products/bathtub-filter/bathtub-filter-technology-notes.md
  - ../syntheses/bathtub-filter-research-map.md
---

# 浴缸过滤器（Bathtub Filter）专利与技术版图

## Obsidian links
- [[bathtub-filter]]
- [[bathtub-filter-patent-table]]
- [[bathtub-filter-technology-notes]]
- [[bathtub-filter-kes-product-architecture-hypotheses]]
- [[bathtub-filter-route-clusters-and-kes-opportunity-spaces]]
- [[bathtub-filter-normal-flow-vs-reduced-flow-evidence-table]]
- [[bathtub-filter-complaint-taxonomy-and-risk-by-route]]

## 为什么有这页
这页把 bathtub filter 从“市场上有没有人卖”推进到“公开可见的技术路线、专利祖先、以及 brand-level technical posture（品牌层技术姿态）到底是什么”。

它不是 FTO（freedom to operate）意见，也不尝试给出侵权判断。
它更像一张用于产品定义的地图：
- 哪些技术路线确实有 prior art（现有技术）积累
- 哪些品牌像是在继承旧 shower / bath-treatment 路线
- 哪些 claims 更像 engineering-grounded（工程上站得住）
- 哪些 claims 更像 marketing overreach（营销外溢）

## 核心结论（Main takeaway）
当前 bathtub filter 市场，不像一个从零长出的新品类；更像是以下几条旧路线的重组：
1. **tub-spout inline**：直接挂在 bathtub spout / faucet 上的 inline housing
2. **shower-lineage cartridge**：从 shower filter 继承下来的 cartridge + media 逻辑
3. **dissolvable / vitamin C dechlorination**：通过 water-soluble / reactive media 做 dechlorination
4. **immersion / hanging filter**：悬挂式、浸泡式、软袋式或 bath-ball 变体
5. **softening-adjacent storytelling**：把 scale / hard-water / softening 语言混入 bath use case

这意味着：
> KES 若进入该类目，真正的产品问题不是“能不能做一个 bath filter 外观”，而是“要站在哪条成熟路线旁边，并把 claim discipline（宣称纪律）守住”。

---

## 公开可见的 early patent clusters（早期专利簇）

### 1) tub-spout inline：最直接的 bathtub-specific hardware route
**代表性专利**
- `US6145670A` — *Bathtub spout with removable filter*

**可见技术信号**
- 明确是 bathtub-spout specific architecture
- 强调 compact bathtub spout filter
- 包含 removable / disposable cartridge thinking
- 甚至提到给 standard bathtub spout 的 DIY conversion kit 逻辑

**战略意义**
- 这是最接近今天“装在 tub faucet 上”的 bath filter 祖先之一
- 对 KES 最有参考价值的不是 chemistry，而是：
  - compatibility
  - attachment geometry
  - leakage control
  - refill / cartridge accessibility

### 2) shower-lineage cartridge：很多 bathtub filter 实际上是 shower filter 近亲
**代表性专利**
- `US6096197A` — *Shower filter for chlorine removal and scale deposit prevention*
- `US6267887B1` — 同族延续

**可见技术信号**
- multi-purpose shower/tub filter unit
- chlorine-removal media + scale-inhibiting media
- universal attachment framing
- replaceable cartridge logic

**战略意义**
- 这类 prior art 强烈暗示：很多 bathtub filter 不是全新核心技术，而是 shower filtration route 的再包装 / 再适配
- 也是为什么“适配大多数 faucet / tub spout”这类话术需要谨慎：旧专利就已经把 universal / multi-purpose attachment 当成主要问题来处理

### 3) hot-water dechlorination media：Sprite / Chlorgon lineage 的真正护城河更像 media story
**代表性专利 / 邻近专利**
- `US5914043A` — hot-water chlorine removal method using non-soluble ceramic-type calcium sulfite beads（与 Chlorgon lineage 高度相关）
- `US6056875A` — *Shower filter media*
- `US6325930B2` — *Filtered showerhead*，公开文本直接引用 Sprite Industries 的 ChlorgonTM

**可见技术信号**
- 强调 hot water / high flow 场景下 chlorine / chloramine reduction
- 强调 ceramic-type calcium sulfite beads
- 强调与 copper-zinc / KDF-like media 的组合效应
- `US6325930B2` 公开文本直接写到：preferred media 可以是 Sprite Industries 的 ChlorgonTM，并指向 `US5914043A`

**战略意义**
- Sprite 的“patented media”叙事，比纯外观或 bath-ball 外形更像真正的 IP anchor（知识产权锚点）
- 对 KES 来说，这一簇更像提醒：
  - 热水场景下，**media-choice + contact-time + insolubility** 才是可辩护的技术核心
  - 不是“stage 数越多越高级”

### 4) dissolvable / vitamin C dechlorination：不是标准滤芯，但确实是独立技术路线
**代表性专利**
- `US7682513B2` — *Means for dechlorinating water*
- `CN101102961A` — *Vitamin C emitting filter*（LG Electronics Inc）

**可见技术信号**
- 通过 water-soluble / reactive media neutralize chlorine / chloramines
- 公开文本可见 ascorbic acid / vitamin C 路线信号
- 更像 controlled-contact treatment，而不完全是 classic particulate filtration

**战略意义**
- 解释了为什么 market 上会出现 vitamin C、gentle bath、baby / sensitive-skin framing
- 也解释了为什么有些产品其实更像 treatment accessory，而不是严格意义的 particulate / adsorption filter
- 这条路线技术上能支撑“dechlorination”叙事，但通常更难支撑 broad contaminant-removal 叙事

### 5) immersion / hanging / bathwater accessory：filter 与 treatment accessory 的边界本来就模糊
**代表性专利**
- `JP3002925U` — *Bathwater dechlorinating agent*

**可见技术信号**
- 公开记录显示为 bathwater dechlorinating accessory / agent 路线
- 说明产品不一定要 inline，也可以是放入或挂入 bath water 的处理装置

**战略意义**
- Santevia、Crystal Quest Bath Ball 这类 today’s forms，不应只拿 faucet hardware 逻辑评估
- 这一簇的重要意义是：它证明“浴缸过滤器”本来就有 accessory 化祖先，不只是 plumbing hardware

### 6) softening-adjacent：技术可讲，但宣称很容易过界
**代表性专利**
- `FR2480822A1` — *Ion-exchange resin water softener for shower bath sprays*

**可见技术信号**
- softener / ion-exchange / shower-bath spray adjacency
- 说明 softening 语言并非凭空而来，而是长期存在于相邻水处理叙事中

**战略意义**
- 这不是说 today’s small bath filters 真能有效软化整缸 bath water
- 它更像提醒：softening 是一块老话术区，但在小体积、短接触时间、快流量下，**真实有效性门槛远高于 marketing 语气**

---

## Brand × route × patent signal（品牌 × 路线 × 专利信号）

### Sprite
**公开可见关联最强**
- 与 `US5914043A` / `US6056875A` / `US6325930B2` 所代表的 hot-water dechlorination media lineage 高度相关
- 市场页面持续强调 patented Chlorgon filtration media
- 公开专利文本中可见 ChlorgonTM 被其他 showerhead/filter 专利直接引用

**更像什么**
- 更像 **media-IP-led brand（滤材 / 方法驱动）**，而不是单纯 bath-specific housing brand

**对 KES 的启发**
- 如果没有独特 media logic 或测试 story，只模仿 Sprite 的“patented filtration media”口气会显得虚
- Sprite 路线最值得学的是：**窄 claim + 热水语境 + 技术名词长期一致**

### Crystal Quest
**公开可见关联中等，偏 product-form / configuration 叙事**
- Bath Ball® 页面强调 unique drop-down filter design、more contact time、chloramine removal ceramic spheres、cartridge replacement
- 公开搜索里没有轻易看到强 brand-specific patent 锚点直接绑定 Bath Ball®

**更像什么**
- 更像 **product-form + filtration-media configuration brand（形态 / 结构叙事）**
- bath-ball / hanging-ball route 很鲜明

**对 KES 的启发**
- Crystal Quest 最强的可学习点不是“专利护城河明显”，而是把“contact time”讲成购买理由
- 但“fits all tubs / any temperature”这类语言值得保守看待

### Santevia
**公开可见专利锚点较弱**
- 公开页面主叙事是 hanging / fabric-like bath filter、99.9% chlorine reduction、restores minerals、skin/hair comfort
- 没有像 Sprite 那样明显把某个 patent family 挂在前台

**更像什么**
- 更像 **lifestyle-mineralization + ritual-use brand**
- 路线接近 immersion / hanging filter，而不是 plumbing-heavy inline hardware

**对 KES 的启发**
- 该路线的优势是审美、低硬件感、可进入 wellness 语境
- 但 mineralization / nourishes skin 这类表述，若无强产品级数据，证据边界比单纯 dechlorination 更脆弱

### Canopy
**公开可见 patent-forward 信号不强**
- 现阶段公开页面更强调 design-led、easy install、chlorine / odor reduction、baby-friendly extension
- 外部评论与媒体提及其 media stack 可能包括 KDF、activated carbon、calcium sulfite，但品牌页面前台并不明显突出 patent lineage

**更像什么**
- 更像 **design-first inline cartridge brand**
- 是目前最接近“把 shower/faucet filter 的可信度语言，转译成 premium baby/wellness bath object”的路线

**对 KES 的启发**
- Canopy 证明了 bath filter 可以做成更像 premium bathroom product，而不是廉价 bath ball
- 但其真正难点仍然是：如何在优雅外观下保证 water path 被强制通过 enough media

### Kinder Filter
**公开可见 patent signal 弱，clinical / skin-outcome signal 强**
- 主站前台更强调 clinically tested、skin hydration、eczema / dry skin comfort、99% impurities
- 公开专利搜索里没有快速看到明确 brand-owned bath-filter patent family 与之绑定

**更像什么**
- 更像 **clinical-positioning DTC brand**，而不是明显的 patent-led brand

**对 KES 的启发**
- 这条路线在商业上很诱人，因为能直接打 baby / eczema / dry skin 人群
- 但也是 claim-risk 最高的一条：
  - clinical tested 不等于 broad contaminant claims 自动成立
  - skin outcome claim 需要比材料名词更高等级的证据

### Tubo
**公开可见 patent signal 弱，Amazon-native performance claim 强**
- 页面强调 8-stage、up to 99% chlorine / heavy metals / bacteria、clinically tested、healthy skin & hair
- 暂未看到明确 brand-owned patent family 被公开高频展示

**更像什么**
- 更像 **performance-claim-heavy marketplace/DTC hybrid brand**

**对 KES 的启发**
- 这条路线流量语言很强，但技术可信度压力也最大
- 尤其“bacteria + heavy metals + skin outcomes + 99%”同时出现时，最容易触发证据与合规张力

---

## 哪些 technical claims 看起来更站得住，哪些更弱

### 相对更 grounded（前提仍是有产品级测试）
1. **chlorine reduction / dechlorination**
   - 有长期 prior art
   - 与 shower / bath hot-water routes 对得上
   - 与 calcium sulfite、KDF、carbon、vitamin C 等 media 叙事都有连接点

2. **odor reduction**
   - 常是 chlorine reduction 的邻接结果
   - 比 broad health benefit 更容易解释

3. **replaceable cartridge / removable filter architecture**
   - 属于结构性陈述
   - 最容易验证，也最少依赖生化夸张

4. **bath-specific attachment / hanging use / spout-fit system**
   - 本质是 form-factor 与 use-case claim
   - 前提是 compatibility 不被过度承诺

### 中间地带：可讲，但需要非常收口
1. **chloramine reduction**
   - 某些 media / chemistry route 有依据
   - 但不同产品差异会非常大，不能轻易泛化

2. **scale deposit mitigation / hard-water feel improvement**
   - 在 shower-adjacent prior art 中能看到
   - 但不应轻易升级成“water softener”

3. **mineralizing / restoring minerals**
   - 在 hanging / wellness route 里常见
   - 但对整缸 bath water 的可测意义与一致性，通常比文案看起来更复杂

### 当前最弱、最容易过界
1. **broad contaminant removal story**
   - 尤其同时声称 chlorine、fluoride、lead、heavy metals、bacteria、PFAS、microplastics 等一长串
   - 小体积 bath filter 在高流速 / 高温 / 短接触时间下，很难让这种“大而全”叙事显得舒服

2. **true hard-water softening**
   - 若无真正 ion-exchange capacity 设计与强测试，通常应高警惕

3. **eczema / baby-safety / skin barrier / hydration outcomes**
   - 这些可以成为 brand story，但不能被误当成 media 名词自然推出的结果
   - 证据要求高，合规风险也高

4. **universal fit / fits all tubs**
   - 这是最常见也最可疑的结构类话术之一
   - bathtub spout geometry 差异是真问题，不是小问题

---

## 对 KES 的现实产品含义

### 如果 KES 追求更稳的第一代路线
更建议优先考虑：
- **inline tub-spout / spout-adapter route** 或 **premium hanging route** 二选一
- 用 **narrow chlorine / odor / bath comfort** 作为前台 story
- 把 “refill cadence + compatibility boundary + flow penalty” 说清楚

### 不建议第一代就重仓的方向
- “17-stage / 20-stage” 复杂滤材堆叠竞赛
- “heavy metals + fluoride + bacteria + eczema + softener” 全包式叙事
- 没有强 attachment engineering 的 universal-fit 大承诺

---

## KES 仍可能存在的 technology / patent opportunity spaces（非 FTO）
以下是**产品开发与专利方向机会假设**，不是法律可实施性意见。

### 机会 1：compatibility-first tub-spout architecture
现有市场普遍把“适配”说得太轻。
如果 KES 能把以下问题系统化，反而更像真实创新：
- 不同 spout geometry 的 adapter logic
- 快装 / 快拆且低漏水风险
- 与 overflow / splash 的关系
- 不同 fill angle 下的稳定出水路径

### 机会 2：forced-water-path + visible flow assurance
很多 bath filter 的最大怀疑点是：水到底有没有被强制穿过 enough media。
可探索：
- 防 bypass 结构
- 透明 / 半透明 flow confirmation window
- 明确的 max-flow guidance
- 滤芯装反 / 未锁紧提示

### 机会 3：bath-specific refill logic，而非照搬 shower cartridge
shower 与 tub fill 的使用方式不同。
可探索：
- 按 tub-fill event 计数或按 gallon band 提示更换
- 快速排干 / 防霉 / dry-out 设计
- bath-only 的 media volume / pressure-drop 平衡

### 机会 4：claim-light premium route
不是在滤材数量上创新，而是在 **可信体验** 上创新：
- 更清晰的 “what it does / what it does not do”
- 更好的 premium bathroom-object design
- 更少但更可信的 claims
- 更强的 installation UX

### 机会 5：hanging / immersion route 的 hygiene upgrade
如果做软性 / hanging 路线，可考虑：
- drying geometry
- anti-mildew storage logic
- replaceable pouch / core module
- 更明确的 contact-time control

### 机会 6：test-method-led differentiation
这个类目最缺的是 product-level proof discipline。
可探索：
- bath-fill simulation protocol
- hot-water / fast-flow test method
- claims 只绑定已测试场景
- 将“tested under bath fill conditions”做成信任资产

---

## 目前最重要的判断
如果只看公开资料，当前更像真的技术护城河的是：
- Sprite / Chlorgon lineage 的 **hot-water dechlorination media story**
- 以及少数与 cartridge / attachment 结构有关的旧式 bathtub / shower prior art

而很多新品牌真正的差异化，更多来自：
- design
- baby / skin positioning
- clinical framing
- brand expression
- DTC content quality

这并不代表它们没有价值；只代表它们的“护城河种类”未必主要是公开可见 patent moat（专利护城河）。

## 新品牌 IP 状态（2026-04-17 补充专项搜索）

### 搜索方法
对 Canopy、Kinder Filter、Tubo 分别进行了 Google Patents assignee 搜索 + 品牌官网 IP 声明检查 + USPTO 文件查询。

### Canopy
- **官网 IP 声明**：产品页面上找不到专利号、”patent pending”或任何 IP 声明
- **USPTO 痕迹**：发现了一个与 Canopy 关联的 USPTO 文件编号（`data.uspto.gov/patent-file-wrapper/details/29986439`）——该编号对应设计专利申请格式（”D”字头），而非功能型实用专利（utility patent）
- **曾存在的 patents 页面**（`onecanopy.com/pages/patents`）：404 已失效
- **结论**：Canopy **可能持有至少一项设计专利**（外观专利），但具体内容不可确认；**没有公开可见的功能型 utility patent 与 bath filter 的过滤机制绑定**

### Kinder Filter
- **官网 IP 声明**：无任何专利声明、专利号或 “patent pending” 措辞
- **Google Patents 搜索**：在 Kinder Filter 名下未找到任何与 bath filter 相关的专利申请
- **结论**：**未见专利保护**

### Tubo
- **官网 IP 声明**：无专利声明；品牌以功效宣称（”clinically tested”、”99% chlorine removal”）为主
- **Google Patents 搜索**：未找到与 Tubo / trytubo 关联的 bath filter 专利申请
- **结论**：**未见专利保护**

### 2015–2025 新增专利观察
- **D1,034,899**（2024-07-09 授权）：”Bath Ball Filter” — 外观设计专利，受让人未完全确认，非功能 IP
- DTC 新品牌整体：IP 版图在 2015–2025 年没有明显新增 utility patent 活动；主要新进入者依赖品牌定位、设计差异化和 supply chain 而非专利护城河

### 修正后的整体 IP 版图判断
> 原有判断（以 Sprite/Chlorgon 为主的 hot-water dechlorination media lineage 是最强技术 IP）保持有效。

**新结论补充：**
- DTC 新品牌（Canopy、Kinder、Tubo）在公开可见层面**没有功能型专利保护**
- 这意味着 KES 进入此类目，在专利层面的压力主要来自 Sprite 旧有专利（大多临近或已过期），而非新品牌的 IP 壁垒
- 新品牌的护城河更像：**品牌认知 + 设计美学 + DTC 渠道建设**，而非专利

## 滤材化学证据更新（2026-04-17 P4/P5 专项调研）

> 完整数据见：[[bathtub-filter-chloramine-media-research]] 和 [[bathtub-filter-media-efficacy-at-bath-conditions]]

### 氯胺去除的 Tier 1 证据（关键补充）

之前分析的"chloramine reduction 需要更收口"现在有 Tier 1 实验支持：

| 媒体 | 游离氯 | 一氯胺 | 最强证据等级 |
|------|------|------|------|
| KDF-55 | ✅ 优秀 | ❌ 18.2% | Tier 2（Pure Water Gazette 测试）|
| KDF-85 | ✅ 优秀 | ❌ 1.4% | Tier 2（同上）|
| 亚硫酸钙 | ✅ 优秀 | ❌ pH 依赖失效 | **Tier 1**（Yiin et al. 1987, Inorg Chem）|
| 标准 GAC | ✅ 良好 | ⚠️ 需 EBCT ≥10 min | Tier 2（贸易技术文献）|
| 催化活性炭 | ✅ 优秀 | ✅ 需 EBCT ≥4–5 min | **Tier 1**（Kochany 2008, Water Environ Res）|
| 维生素 C（淋浴）| ✅ 瞬时 | ❌ 接触时间不足 | **Tier 1**（Basu 2011, J Water Supply）|
| 维生素 C（浴缸）| ✅ 瞬时 | ✅ 4–8 min 完全去除 | Tier 2（SFPUC 政府建议）|

**最重要的修正**：之前标注为"中间地带"的氯胺宣称，现在有了更精确的媒体边界：
- 亚硫酸钙：**不能宣称氯胺去除**（有 Tier 1 化学证据）
- KDF-55/85：**不能宣称氯胺去除**（18.2% / 1.4%，实测数据）
- 催化活性炭 + 充足接触时间：**可以宣称**（有 Tier 1 证据支持）
- 维生素 C + 浴缸注水场景：**可以宣称**（有政府机构数据支持）

### 浴缸注水条件的逆直觉发现（P5）

之前对"contact time matters"的担忧是基于逻辑推断。现在有实测数据：

独立评测（waterfilterguru.com 2026）在不同流速下对主要产品进行了比色法测试：
- **快速流速（1.6–3.8 GPM）**：多数产品去除率 0–50%（部分产品完全失效）
- **慢速流速（0.36–1.0 GPM，接近浴缸注水条件）**：多数产品达到 85–100%

**结论：浴缸注水的低流速（0.3–0.8 GPM）对氯去除是有利条件，而非不利条件。** 这颠覆了之前基于"大体积水、短接触时间"的悲观预判。

### NSF/ANSI 177 氯胺确认

NSF/ANSI 177：
- 测试水中氯胺要求 <0.1 mg/L（明确将氯胺作为干扰物排除）
- **要求产品必须附加氯胺免责声明**："本产品未经评估在含氯胺水中的游离氯去除性能"
- **任何使用 KDF-55 + 亚硫酸钙 + 标准 GAC 的 NSF 177 认证产品，不能声称氯胺去除**

KES 若需氯胺宣称，正确认证路径是 **NSF/ANSI 42 氯胺去除认证**（需专门测试和申请）。

## 当前不确定性（Uncertainty）
- 这轮主要依赖公开可见 patent pages、品牌站文案、搜索可见片段；并未做完整 patent family legal-status review
- Canopy 的 USPTO 文件编号已确认，但设计专利具体内容、权利要求范围未完全审阅
- 一些媒体文章会把 brand claims 转述得更激进，不能直接等同于 brand 官方实证
- “clinical tested” 具体测试设计、样本量、终点与是否发表，公开信息仍有限
- Sprite 20+ 专利的具体到期状态未系统核查

## Sources
- `https://patents.google.com/patent/US6145670A/en`
- `https://patents.google.com/patent/US6096197A/en`
- `https://patents.google.com/patent/US6267887B1/en`
- `https://patents.google.com/patent/US5914043A/en`
- `https://patents.google.com/patent/US6056875A/en`
- `https://patents.google.com/patent/US6325930B2/en`
- `https://patents.google.com/patent/US7682513B2/en`
- `https://patents.google.com/patent/JP3002925U/en`
- `https://patents.google.com/patent/FR2480822A1/en`
- `https://patents.google.com/patent/CN101102961A/en`
- `https://crystalquest.com/products/bath-ball-filter`
- `https://santevia.com/products/bath-filter`
- `https://getcanopy.co/products/bath-tub-filter`
- `https://www.kinderfilter.com/`
- `https://trytubo.com/products/new-tubo-2-0-bath-filter`
