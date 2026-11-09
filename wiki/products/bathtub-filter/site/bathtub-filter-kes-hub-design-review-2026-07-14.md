---
type: product
status: draft
owner: strategy
created: 2026-07-14
updated: 2026-07-14
visibility: team
confidence: high
officiality: draft
domain: product
domains: [bathtub-filter, kes, website, hub, design-review, conversion, content]
source_count: 6
review_cycle: monthly
verification_status: working
related:
  - ./bathtub-filter-kes-marketing-site-content-map.md
  - ../bathtub-filter-kes-website-copy-v1.md
  - ../bathtub-filter-kes-clean-formula-emotional-positioning.md
  - ./bathtub-filter-kes-water-match-selector-spec.md
  - ./bathtub-filter-kes-custom-formula-builder-spec.md
  - ../bathtub-filter-claim-register.md
---

# KES Bathtub Filter Hub 页面设计修改反馈

## 给设计同事的总体结论

当前稿的画面干净、产品也有基本露出，但它更像一个通用 wellness 品牌首页，还没有完成“产品 Hub 页”的核心任务。用户看完第一屏仍不知道自己该买哪个版本、价格是多少、是否适配自家出水嘴，也不能直接加入购物车；继续往下看，页面主要重复生活方式和品牌故事，没有把 KES 最有差异化的透明滤材、分层配方、强制水路、防沟槽、正常流速和可验证机制讲透。

这轮不要只做局部换文案。建议重排前两屏，并把第二屏后的页面改成“卖点总览 + 进入详细 spoke 页”的结构。

## 修改目标与优先级

### P0：必须在下一稿解决

1. **前两屏必须能下单**：首屏建立情感冲突和产品差异；紧接着展示四个可购买版本，并提供价格、适用水质、适配检查和 `Add to cart`。
2. **四版本必须真实出现**：Free-Chlorine Formula、Chloramine + Soak Kit、Well-Water Formula、Build Your Formula。不能继续用一个固定 `Triple-Layer Filtration` 代表全部产品。
3. **补上核心工程差异**：真实爆炸图、每一步过滤、针对滤材设计的分仓和导流、水流必须经过滤材而不是从沟槽绕走。
4. **补上正常流速卖点**：说明这是为 bathtub fill flow 设计，不靠把水流压得很小来制造效果；具体数字只有在测试闭环后才能出现。
5. **补上 spout 适配**：不要只写 `Fits most bathtub faucets`。展示支持的 spout 类型、安装方式、不支持类型和 `Check my spout`。
6. **删除或降级高风险结果 claim**：`Gentle on Skin & Hair`、`Softer Skin`、`Healthier Hair`、`Less dryness`、`targets ... heavy metals`、`leak-proof` 均需按 claim register 重写或等待证据。
7. **品牌统一**：页尾 `PURELOOP.` 与页头 KES 冲突，必须统一为 KES 品牌体系。

### P1：本轮应一并解决

1. 删除重复出现的 `OUR STORY / Radically Honest. Made for Your Bath.` 模块，只保留一次，并放到购买和产品证据之后。
2. 把当前四个泛化 icon 卖点改成可验证的产品事实，不用 wellness 结果充数。
3. 增加测试、替换、评价/证据、FAQ 和不适用边界，但保持摘要化，每个模块链接到详细页。
4. 调整照片选择。当前洗头图像像 shower-filter 使用场景，容易混淆产品用途；应优先使用浴缸注水、透明滤仓、安装细节和真实水路图。

### P2：视觉精修

1. 减少过大的空白和过小的说明文字，提高信息扫描效率。
2. 保持克制的 editorial / bathroom aesthetic，但不要让米白色生活方式照片覆盖工程信息。
3. 让真实滤材颜色成为视觉识别资产；版本差异用材料色带、名称和标签表达，不依赖四个相似的产品渲染图。

## 建议页面结构

### 第一屏：情感诉求 + 产品实物 + 购买起点

当前 `Bathe in Water You Can Trust` 方向不算错，但太泛，无法建立 KES 独有的冲突。核心情感不是“我们也关心健康”，而是：消费者会认真检查护肤品的 clean ingredients，却每天让浴缸水通过一个看不见里面装什么、也不知道水怎么走的黑盒。

建议文案方向：

> **You check every ingredient. Why bathe through a black box?**
>
> A transparent, layered bath filter with media you can see, a water path designed around every layer, and a formula matched to your water.

首屏视觉要求：

- 产品透明滤仓必须比人物更清楚，用户一眼能看到分层真料。
- 不要只让模特手持产品；至少同时出现安装后的出水状态或透明仓近景。
- 首屏保留一个主 CTA：`Shop your formula`。
- 次 CTA：`Check your water` 或 `Check my spout`，二选一，避免两个同权按钮分散。
- 首屏底部用三条事实型短句：`See every layer` / `Engineered flow path` / `Test it yourself`。
- 不在首屏写未经验证的去除率、皮肤结果或 universal fit。

### 第二屏：四版本就地购买

这是当前稿最重要的缺失。建议使用四 tab 或桌面四列、移动端两列，不跳转到另一个产品列表页后才选择。

| 版本 | 卡片必须显示 | 主动作 |
|---|---|---|
| Free-Chlorine Formula | `For city water using free chlorine`、滤材摘要、对应试纸、价格、适配状态 | `Add to cart` |
| Chloramine + Soak Kit | `For chloramine-treated city water`、inline catalytic carbon + required soak step、总氯试纸、价格 | `Add to cart` |
| Well-Water Formula | `For low-to-moderate iron / sulfur nuisance`、红旗筛查、价格 | `Check & add` |
| Build Your Formula | `Choose your water and visible problems`、guided custom 说明 | `Customize yours` |

购买模块上方只需一句：`Choose what is used in your water, or let us match it for you.`

每张卡必须同时显示：

- 适用对象和明确不适用项。
- 简化滤材层序，不用泛称 “3-stage / 8-stage”。
- `Check your water` 和 `Check my spout` 的轻量入口。
- 主机/补芯范围、价格与订阅选项。
- 就地加入购物车；自定义版生成合法 `formula_id` 后回到同一 sticky cart。

### 第三屏：Clean Formula，不再是黑盒

把当前 `Triple-Layer Filtration` 和第一次 `OUR STORY` 合并成一个强模块：

- 左侧：透明滤仓实拍，能看清材料、用量和层序。
- 右侧：`What is inside / How much / Why it is there / What it does not claim`。
- 可用标题：`Clean should not stop at your skincare shelf.`
- 可用承接句：`We name every material, keep it in visible layers, and never ask you to trust a mystery blend.`
- 不需要攻击性地展示某个竞品 logo；可以用“opaque mixed-media cartridge”作为品类问题示意，但必须基于可证明的结构事实。

### 第四屏：真正的产品爆炸图

当前右侧产品标注图不是爆炸图，只是四个外观 callout，而且没有解释每一步过滤。

新图需要把部件沿纵向拆开并标号：

1. spout attachment / retention system
2. sealed inlet and spreader
3. prefilter layer
4. formula-specific media chambers
5. flow-diversion / compression structure
6. bottom outlet
7. formula-specific test strip or soak accessory

每一步只回答四件事：水先到哪里、接触什么材料、这个材料负责什么、边界是什么。四个标准/自定义版本切换时，爆炸图中的滤材层和附件随之变化。

### 第五屏：为滤材设计的水路，避免沟槽效应

这个卖点必须从爆炸图中独立出来，因为“用了什么滤材”和“水有没有真正经过滤材”是两个问题。

建议标题：

> **The media only works when water actually passes through it.**

视觉使用剖面水路图或透明原型视频，对比：

- KES：进水被铺开，按固定顺序穿过每个独立滤材层，再从底部均匀流出。
- 典型混装结构：滤料混在一个腔体，水可能沿阻力较小的沟槽快速通过，接触不充分。

注意不要做无法证明的竞品性能结论。重点讲 KES 自己的结构设计、测试方法和观察指标：flow distribution、contact path、pressure drop、bypass / shortcut flow。

### 第六屏：真实浴缸流速

当前页面完全没讲流速，这是购买浴缸过滤器时非常实际的决策因素。

建议内容：

- 标题：`Made to fill a bath, not turn your faucet into a trickle.`
- 展示正常注水的视频或时间对比，而不是只放静态生活方式图。
- 解释流速、接触时间和滤材结构之间如何平衡。
- 只有完成成品台架测试后才写具体 L/min、注满时间或 reduction 数字；测试前使用 `designed for normal bath-filling flow` 这类受控表述。
- 链接到 `How we test` spoke 页。

### 第七屏：Spout compatibility

当前 `Faucet Adapter — Fits most bathtub faucets` 太笼统，也没有帮助用户判断自己能否安装。

建议改成三类可视卡片：

- `Fits directly`
- `Fits with included support`
- `Not compatible`

每类显示真实 spout 照片、关键尺寸和安装方式。增加上传照片/选择轮廓的 `Check my spout`，结果应在购买卡附近回显。不要写 `universal` 或模糊的 `fits most`，只给具体支持/条件支持/不支持结果。

### 第八屏：自己验证，不只相信广告

保留 `Test Strips in Every Box`，这是当前稿里方向最正确的模块之一，但要进一步解释：

- 不同配方匹配不同试纸：游离氯版用游离氯试纸；氯胺版用总氯试纸并说明正确测量时机。
- 三步呈现：test before → install/use correctly → test after。
- 替换逻辑继续使用 `Replace by baths, not months`，并链接 lifespan 详细页。
- 不使用 TDS 笔或铅试纸作为效果证明。

### 第九屏以后：Hub 摘要 + Spoke 深入

第二屏之后可以把所有卖点概括列出，但不要再做一排没有信息密度的 icon。建议每个模块采用“一个结论 + 一个证据视觉 + 一个 Learn more”：

| Hub 摘要 | 深入页面 |
|---|---|
| 四种水质配方 | Water Match / 各 formula PDP |
| 透明 clean formula | Media pages |
| 爆炸结构 | Product architecture |
| 强制水路 / 防沟槽 | Flow engineering |
| 正常注水流速 | How we test |
| 出水嘴适配 | Fit guide |
| 试纸验证与更换 | Test / lifespan |
| 能力边界 | FAQ / Is KES right for you |

品牌故事、环保承诺和订阅邮箱可以保留，但应放在这些产品决策信息之后。`Our Commitment` 目前是泛品牌语言，不应占据核心产品 Hub 的中上部位置。

## 页面链接实施表

### 链接使用原则

1. **交易动作不跳内容页**：`Add to cart`、订阅选择和数量选择在 Hub 原位完成；不能把用户送到文章页后再找购买入口。
2. **选购动作进入工具**：`Check your water` / `Find my formula` 进入 Water-Match Selector；`Customize yours` 进入 Build Your Formula。
3. **解释型内容进入 spoke**：模块标题、证据图和 `Learn how...` 链到对应详细页。链接文字必须说清目的，不统一写模糊的 `Learn more`。
4. **图片只在有明确预期时可点击**：爆炸图、材料近照、水路图、spout 类型图可以点击；模特和氛围照片不加链接。
5. **整卡与卡内 CTA 分工**：产品卡标题/产品图进入对应 Formula PDP；`Add to cart` 原位加购；`Check fit` 打开适配流程。不要让整张卡点击与按钮产生冲突。
6. **所有 spoke 页保留返回购买器路径**：桌面右侧或移动端底部显示 sticky `Back to your formula / Add to cart`，返回 Hub 的 `#choose-your-formula` 锚点并保留用户已选版本。

### Header 与首屏

| 页面元素 | 是否加链接 / 点击行为 | 消费者目的地 | 对应 wiki 文档（内容 owner） |
|---|---|---|---|
| Header `KES` logo | 整个 logo 可点击 | Hub 顶部 `/bathtub-filter` | [Marketing Site Content Map](./bathtub-filter-kes-marketing-site-content-map.md) |
| Header `Shop` | 下拉而不是单一跳转；列四版本 + Refill | 对应 Formula PDP / 自定义器 / Refill | [Content Map](./bathtub-filter-kes-marketing-site-content-map.md)、[Refill Subscription](./bathtub-filter-kes-refill-subscription.md) |
| Header `Find My Formula`（建议替换 Home 后的泛化入口） | 文字链接 | Water-Match Selector | [Water-Match Selector Spec](./bathtub-filter-kes-water-match-selector-spec.md) |
| Header `How It Works` | 文字链接 | 结构总览页 | [D1 Structure Overview](./bathtub-filter-kes-structure-overview.md) |
| Header `Fit`（建议新增） | 文字链接 | 安装与兼容性页 | [P4 Installation & Compatibility](./bathtub-filter-kes-install-and-compatibility-guide.md) |
| Header `Support` | 文字链接 | Support hub | [SVC6 Support & Contact](./bathtub-filter-kes-support-and-contact.md) |
| Hero 主标题 | 不加链接 | — | [Clean Formula Emotional Positioning](../bathtub-filter-kes-clean-formula-emotional-positioning.md) |
| Hero 产品透明滤仓近照 | 可点击；hover/焦点态提示 `See what's inside` | 透明滤仓详细页 | [D3 Transparent Housing](./bathtub-filter-kes-structure-transparent-housing.md) |
| Hero 主 CTA `Shop your formula` | 同页平滑滚动并聚焦购买器 | Hub `#choose-your-formula` | [Website Copy](../bathtub-filter-kes-website-copy-v1.md) |
| Hero 次 CTA `Check your water` | 打开全页或抽屉式选购器 | Water-Match Selector | [SVC10 Water-Match Selector](./bathtub-filter-kes-water-match-selector-spec.md) |
| Hero `See every layer` | 文字链接 | 透明滤仓详细页 | [D3 Transparent Housing](./bathtub-filter-kes-structure-transparent-housing.md) |
| Hero `Engineered flow path` | 文字链接 | 导流/防沟槽详细页 | [D2 Flow Diversion Module](./bathtub-filter-kes-structure-flow-diversion-module.md) |
| Hero `Test it yourself` | 文字链接 | 怎么测试自家水 | [E5 How to Test Your Water](./bathtub-filter-kes-edu-how-to-test-your-water.md) |

### 四版本购买器

| 页面元素 | 是否加链接 / 点击行为 | 消费者目的地 | 对应 wiki 文档（内容 owner） |
|---|---|---|---|
| 模块标题 `Choose your formula` | 不加链接 | — | [Website Copy](../bathtub-filter-kes-website-copy-v1.md) |
| `Not sure? Check your water` | 文字链接，保留返回购买器状态 | Water-Match Selector | [SVC10 Water-Match Selector](./bathtub-filter-kes-water-match-selector-spec.md) |
| Free-Chlorine 产品图和标题 | 可点击 | Free-Chlorine Formula PDP | [S1 Free-Chlorine Scenario](./bathtub-filter-kes-scenario-free-chlorine.md) |
| Free-Chlorine `Add to cart` | 原位加购，不跳页 | Mini-cart / cart drawer | [S1 Free-Chlorine Scenario](./bathtub-filter-kes-scenario-free-chlorine.md)、[P2 Pack Contents](./bathtub-filter-kes-pack-contents-spec.md) |
| Chloramine 产品图和标题 | 可点击 | Chloramine + Soak Kit PDP | [S2 Chloramine Scenario](./bathtub-filter-kes-scenario-chloramine.md) |
| Chloramine `Why the soak step?` | 文字链接 | 抗坏血酸钠浸泡件页 | [M4 Sodium Ascorbate Soak](./bathtub-filter-kes-media-sodium-ascorbate-soak.md) |
| Chloramine `Add to cart` | 原位加购；soak step 必须随套装 | Mini-cart / cart drawer | [S2 Chloramine Scenario](./bathtub-filter-kes-scenario-chloramine.md) |
| Well-Water 产品图和标题 | 可点击 | Well-Water Formula PDP | [S3 Well-Water Scenario](./bathtub-filter-kes-scenario-well-water.md) |
| Well-Water `Check your well first` | 打开红旗筛查，不直接进入泛文章 | Well-water pre-check | [E2 Well-Water Basics](./bathtub-filter-kes-edu-well-water-basics.md)、[SVC10 Selector](./bathtub-filter-kes-water-match-selector-spec.md) |
| Well-Water `Check & add` | 筛查通过后原位加购；红旗命中则不显示购买按钮 | Pre-check → mini-cart | [S3 Well-Water Scenario](./bathtub-filter-kes-scenario-well-water.md) |
| Build Your Formula 产品图/标题/`Customize yours` | 三者均进入配置器 | Guided configurator | [SVC13 Build Your Formula](./bathtub-filter-kes-custom-formula-builder-spec.md) |
| 任一标准版本 `Check my spout` | 打开适配抽屉；结果回写当前产品卡 | Spout compatibility checker | [P4 Installation & Compatibility](./bathtub-filter-kes-install-and-compatibility-guide.md) |
| `Refill / subscription` | 文字链接；不干扰首次 Add to cart | Refill 与订阅说明 | [SVC4 Refill Subscription](./bathtub-filter-kes-refill-subscription.md) |
| 价格旁 `What's included?` | 抽屉或轻量 modal，不离开购买器 | Pack contents | [P2 Pack Contents](./bathtub-filter-kes-pack-contents-spec.md) |

### Clean Formula 与滤材

| 页面元素 | 是否加链接 / 点击行为 | 消费者目的地 | 对应 wiki 文档（内容 owner） |
|---|---|---|---|
| `Clean should not stop at your skincare shelf` | 标题可链接，也可只让下方 CTA 可点击 | Clean-formula / transparent design 页面 | [D3 Transparent Housing](./bathtub-filter-kes-structure-transparent-housing.md)、[Clean Formula Narrative](../bathtub-filter-kes-media-eeat-and-clean-formula-narrative.md) |
| 透明滤仓整体近照 | 可点击，打开材料标注大图或进入详情 | 透明滤仓页 | [D3 Transparent Housing](./bathtub-filter-kes-structure-transparent-housing.md) |
| `Calcium Sulfite` 材料名/颗粒近照 | 文字和近照均可点击 | 材料详情 | [M1 Calcium Sulfite](./bathtub-filter-kes-media-calcium-sulfite.md) |
| `KDF55` 材料名/颗粒近照 | 文字和近照均可点击 | 材料详情 | [M2 KDF55](./bathtub-filter-kes-media-kdf55-copper-zinc.md) |
| `Catalytic Carbon` 材料名/颗粒近照 | 文字和近照均可点击 | 材料详情 | [M3 Catalytic Carbon](./bathtub-filter-kes-media-catalytic-carbon.md) |
| `KDF85` 材料名/颗粒近照 | 文字和近照均可点击 | 材料详情 | [M5 KDF85](./bathtub-filter-kes-media-kdf85.md) |
| `Anti-scale adjunct` | 文字链接；`It does not soften your water` 同屏但不做链接 | 材料与边界详情 | [M6 Anti-Scale Granule](./bathtub-filter-kes-media-anti-scale-granule.md) |
| `PET prefilter` | 文字和结构近照可点击 | 材料详情 | [M7 PET Prefilter](./bathtub-filter-kes-media-pp-cotton.md) |
| 模块 CTA | 使用明确文字 `See every material and its role` | 透明滤仓/材料索引 | [D3 Transparent Housing](./bathtub-filter-kes-structure-transparent-housing.md) |

### 爆炸图与水路工程

| 页面元素 | 是否加链接 / 点击行为 | 消费者目的地 | 对应 wiki 文档（内容 owner） |
|---|---|---|---|
| 完整产品爆炸图 | 整图可点击放大；放大层内各编号可继续点击 | Structure overview | [D1 Structure Overview](./bathtub-filter-kes-structure-overview.md) |
| 爆炸图 #1 `Spout attachment / retention` | 编号和部件名可点击 | 挂带与适配结构 | [D4 Flat Strap Fit](./bathtub-filter-kes-structure-flat-strap-fit.md) |
| 爆炸图 #2 `Sealed inlet and spreader` | 编号和部件名可点击 | 结构总览 | [D1 Structure Overview](./bathtub-filter-kes-structure-overview.md) |
| 爆炸图 #3 `Prefilter` | 编号和材料名可点击 | PET 材料页 | [M7 PET Prefilter](./bathtub-filter-kes-media-pp-cotton.md) |
| 爆炸图 #4 `Media chambers` | 每层独立 hotspot；链接随当前 formula 切换 | 对应 M1–M7 材料页 | [Content Map · Media Pages](./bathtub-filter-kes-marketing-site-content-map.md) |
| 爆炸图 #5 `Flow-diversion structure` | 编号和结构剖面可点击 | 防沟槽详细页 | [D2 Flow Diversion Module](./bathtub-filter-kes-structure-flow-diversion-module.md) |
| 爆炸图 #6 `Bottom outlet` | 编号可点击 | 结构总览中的出水路径 | [D1 Structure Overview](./bathtub-filter-kes-structure-overview.md) |
| 水路剖面图/动画 | 整张图或视频封面可点击，进入详细解释；不要给装饰性播放按钮 | Flow engineering 页面 | [D2 Flow Diversion Module](./bathtub-filter-kes-structure-flow-diversion-module.md) |
| `Why mixed media can channel` | 明确文字链接 | 防沟槽详细页 | [D2 Flow Diversion Module](./bathtub-filter-kes-structure-flow-diversion-module.md) |
| `See how we test the flow path` | CTA 链接 | 测试与认证页 | [How We Test and Certify](./bathtub-filter-kes-page-how-we-test-and-certify.md) |

### 流速、适配、验证与更换

| 页面元素 | 是否加链接 / 点击行为 | 消费者目的地 | 对应 wiki 文档（内容 owner） |
|---|---|---|---|
| 浴缸正常注水视频/缩略图 | 可点击播放；视频结束显示详细页入口 | Flow rate explanation | [E10 Flow Rate & Lifespan](./bathtub-filter-kes-edu-flow-rate-and-lifespan.md) |
| `Made to fill a bath, not turn your faucet into a trickle` | 文字链接 | Flow rate explanation | [E10 Flow Rate & Lifespan](./bathtub-filter-kes-edu-flow-rate-and-lifespan.md) |
| `See the test method` | CTA 链接 | How we test | [How We Test and Certify](./bathtub-filter-kes-page-how-we-test-and-certify.md) |
| 三类 spout 实拍卡 | 每张可点击；进入相应兼容性段落并保留返回购买器 | Compatibility guide 对应锚点 | [P4 Installation & Compatibility](./bathtub-filter-kes-install-and-compatibility-guide.md) |
| `Check my spout` | 打开检查器/上传照片流程 | Spout checker | [P4 Installation & Compatibility](./bathtub-filter-kes-install-and-compatibility-guide.md) |
| 挂带结构特写 | 可点击 | Flat strap fit detail | [D4 Flat Strap Fit](./bathtub-filter-kes-structure-flat-strap-fit.md) |
| 试纸 before/after 图片 | 可点击；进入正确测试步骤，不进入 testimonials | How to test | [E5 How to Test Your Water](./bathtub-filter-kes-edu-how-to-test-your-water.md) |
| `Test before and after` | 文字链接 | 买后验证流程 | [SVC2 Post-Purchase Verification](./bathtub-filter-kes-post-purchase-verification.md) |
| `Replace by baths, not months` | 文字链接 | Replacement & lifespan | [T3 Replacement and Lifespan](./bathtub-filter-kes-page-replacement-and-lifespan.md) |
| `Get the right refill` | CTA 链接 | Refill/subscription | [SVC4 Refill Subscription](./bathtub-filter-kes-refill-subscription.md) |

### 页面后段与 Footer

| 页面元素 | 是否加链接 / 点击行为 | 消费者目的地 | 对应 wiki 文档（内容 owner） |
|---|---|---|---|
| `Is KES right for your water?` | 标题/CTA 可点击 | 买前 FAQ | [SVC1 Is KES Right for You](./bathtub-filter-kes-faq-is-kes-right-for-you.md) |
| `What KES does not do` | 文字链接 | 不适用清单 | [P1 V1 Definition & Not-for List](./bathtub-filter-kes-v1-definition-and-not-for-list.md) |
| 用户评价头像/引文 | 仅当有可审核的完整评价页时可点击；当前占位阶段不做假链接 | Proof & testimonials | [SVC8 Proof and Testimonials](./bathtub-filter-kes-proof-and-testimonials.md) |
| 唯一保留的 `Our Story` 模块 | 图片不加链接；`Read our story` 文字 CTA 可点击 | About 页面 | [Homepage & About Layout](../bathtub-filter-kes-homepage-and-about-page-layout.md) |
| `Our Commitment` 三项 | 目前不要加链接；先建立有 owner、有事实的 Sustainability 页面再开放 | 暂无 | 当前没有可用 spoke；不得把泛口号链到空页 |
| Newsletter `Subscribe` | 表单提交，不跳转；提交后显示明确 consent/result | Email lifecycle | [SVC11 Email Lifecycle](./bathtub-filter-kes-email-lifecycle-spec.md)、[SVC12 Privacy & Consent](./bathtub-filter-kes-privacy-terms-and-consent.md) |
| Footer `All Products` | 进入 Hub `#choose-your-formula`，而不是另建重复列表页 | 四版本购买器 | [Website Copy](../bathtub-filter-kes-website-copy-v1.md) |
| Footer 四版本名称 | 各自链接对应 PDP/配置器 | S1 / S2 / S3 / SVC13 | [Content Map](./bathtub-filter-kes-marketing-site-content-map.md) |
| Footer `Replacement Filter` | 链接 | Refill/subscription | [SVC4 Refill Subscription](./bathtub-filter-kes-refill-subscription.md) |
| Footer `FAQs` | 链接 | 买前 FAQ | [SVC1 FAQ](./bathtub-filter-kes-faq-is-kes-right-for-you.md) |
| Footer `Shipping & Returns` | 链接；条款未定稿前不标具体承诺 | Returns & warranty | [SVC3 Returns and Warranty](./bathtub-filter-kes-returns-and-warranty.md) |
| Footer `Contact Us` | 链接 | Support | [SVC6 Support and Contact](./bathtub-filter-kes-support-and-contact.md) |
| Footer `Privacy Policy / Terms` | 分别链接法律页对应锚点 | Privacy / ToS | [SVC12 Privacy, Terms and Consent](./bathtub-filter-kes-privacy-terms-and-consent.md) |

### 不应添加链接的元素

- Hero 模特、泡澡人物、石墙、毛巾等纯氛围照片。
- 无独立内容 owner 的 `Better for You / Better for the Planet` 泛口号。
- 皮肤、头发结果图片；这些内容本身应替换，而不是链接到更多结果 claim。
- `Radically Honest` 等品牌形容词本身；链接应落在可验证事实或明确命令上。
- 每个段落正文中的重复关键词。一个模块保留一个主深链和必要的材料 hotspot 即可，避免满页下划线。

### 设计稿交付时的链接标注格式

设计文件中每个可点击元素统一使用以下注释，前端不需要猜：

```text
Link ID: HUB-D2-01
Clickable: section title + flow diagram
Destination: /how-it-works/engineered-flow
Wiki owner: bathtub-filter-kes-structure-flow-diversion-module.md
Return behavior: back to /bathtub-filter#engineered-flow; preserve selected_formula
Analytics: hub_flow_detail_click
```

建议 ID 规则：`HUB-HERO-*`、`HUB-BUY-*`、`HUB-MEDIA-*`、`HUB-D1-*`、`HUB-D2-*`、`HUB-FIT-*`、`HUB-TEST-*`、`HUB-FOOTER-*`。所有购买按钮另用 `BUY-*`，避免与内容深链混淆。

## 当前页面逐项修改

| 当前元素 | 问题 | 修改要求 |
|---|---|---|
| `Bathe in Water You Can Trust` | 泛化，任何过滤品牌都能使用 | 换成 clean ingredients vs black box 的冲突，副标题补透明分层与工程水路 |
| `Check Your Water` + `Shop Starter Kit` | 没有四版本、价格和直接加购 | 主 CTA 进入同页四版本购买器；首屏后立即显示可购买版本 |
| `Triple-Layer Filtration` | 只代表游离氯版，与四版本冲突 | 改为 `Formula matched to your water`，卡片或 tab 展示各自层序 |
| `Transparent Filter Chamber` | 方向正确但信息不足 | 展示料名、用量、顺序和更换状态；链接 clean-formula 详细页 |
| `Gentle on Skin & Hair` | 容易形成结果 claim | 改为 `Know what your bath water passes through` 或受证据支持的水质表述 |
| `targets chlorine & heavy metals` | 宽泛且证据不足 | 按具体配方与成品测试拆开；未闭环不写 heavy metals |
| `Fits most bathtub faucets` | 适配承诺不透明 | 改成支持/需配件/不支持矩阵，并提供 `Check my spout` |
| `Leak-proof` | 绝对化工程 claim | 测试闭环前用 `sealed housing design`；详细测试结果链接出去 |
| `Feel the Difference` 三图 | 依赖 softer skin / healthier hair，且洗头图误导用途 | 换成 bath fill、transparent media、flow path / test strip 三个产品事实场景 |
| 两个 `OUR STORY` | 重复，占用大量滚动长度 | 合并为一次，放到产品和证据之后 |
| `Our Commitment` | 泛 ESG 信息，转化贡献低 | 下移到接近 footer；用真实材料/包装事实替代泛口号 |
| Footer `PURELOOP.` | 品牌冲突 | 统一为 KES；Shop 导航也要包含四版本和 refill |

## 视觉执行原则

- 产品和真实结构是首要视觉，不要让模特成为唯一主角。
- 爆炸图、剖面水路和安装适配都应使用一致的真实产品比例与部件命名。
- 保留真实滤材的黄、铜、黑、白等材料色，页面不要只剩米白和灰。
- 卡片圆角控制克制；产品模块不做层层套卡。
- 小字目前偏小，尤其 icon 区与图片下说明；桌面和移动端都要保证无需放大即可阅读。
- 移动端首屏后四版本采用 2×2 或横向 tabs，必须保持价格和 CTA 可见，不能把 Add to cart 推到长页面末尾。
- 页面中段使用 sticky `Your formula / Fit status / Add to cart`，用户深入阅读后不必滚回顶部购买。

## 下一稿验收标准

- [ ] 用户在首屏理解“透明 clean formula vs 黑盒”的核心差异。
- [ ] 用户最多滚动两屏即可选择四个版本之一并加入购物车。
- [ ] 四个版本的适用水质、滤材摘要、试纸、价格和 CTA 都清晰。
- [ ] 页面存在真正的爆炸图，并逐步解释部件与过滤过程。
- [ ] 页面独立解释 media-specific flow path 和防沟槽设计。
- [ ] 页面解释正常浴缸注水流速，数字只使用已验证数据。
- [ ] 用户能在购买前判断 spout 是否适配。
- [ ] `Softer Skin / Healthier Hair / heavy metals / leak-proof / fits most` 等高风险文案已删除、收窄或附证据。
- [ ] 品牌统一为 KES，不再出现 PURELOOP。
- [ ] 重复品牌故事已合并，工程与购买信息位于品牌/环保内容之前。
- [ ] 每个 Hub 卖点都能进入对应详细 spoke 页，且详细页提供返回购买器的路径。

## Sources

- [Marketing Site Content Map](./bathtub-filter-kes-marketing-site-content-map.md)
- [Website Copy](../bathtub-filter-kes-website-copy-v1.md)
- [Clean Formula Emotional Positioning](../bathtub-filter-kes-clean-formula-emotional-positioning.md)
- [Water Match Selector](./bathtub-filter-kes-water-match-selector-spec.md)
- [Build Your Formula](./bathtub-filter-kes-custom-formula-builder-spec.md)
- [Claim Register](../bathtub-filter-claim-register.md)
