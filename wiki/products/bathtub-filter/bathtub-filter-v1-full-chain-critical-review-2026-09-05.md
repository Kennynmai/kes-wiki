---
type: product
status: draft
owner: strategy
created: 2026-09-05
updated: 2026-09-05
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, v1, critical-review, bom, parameters, packaging, marketing, copy, claim-discipline]
source_count: 18
review_cycle: monthly
verification_status: desk-review-with-calculations
related:
  - ./bathtub-filter.md
  - ./bathtub-filter-v1-free-chlorine-removal-dimensions-materials.md
  - ./bathtub-filter-kes-patent-19-281644-modular-terminal-water-treatment.md
  - ./bathtub-filter-25lpm-dechlorination-bench-test-spec.md
  - ./bathtub-filter-media-efficacy-at-bath-conditions.md
  - ./bathtub-filter-kes-v1-selling-points-and-pack-contents.md
  - ./bathtub-filter-kes-v1-pricing-channel-launch-geo-subscription.md
  - ./bathtub-filter-kes-website-copy-v1.md
  - ./bathtub-filter-claim-register.md
  - ./site/bathtub-filter-kes-pack-contents-spec.md
  - ./site/bathtub-filter-kes-packaging-design-spec.md
  - ./site/bathtub-filter-kes-page-how-we-test-and-certify.md
  - ./site/bathtub-filter-kes-page-replacement-and-lifespan.md
  - ./site/bathtub-filter-kes-amazon-listing-spec.md
  - ./site/bathtub-filter-kes-refill-subscription.md
  - ./site/bathtub-filter-kes-care-and-maintenance-guide.md
---

# KES Bathtub Filter V1 · 配置 / 参数 / 包装 / 营销 / 文案 全链路批判审查（2026-09-05）

## 0. 先回答"核心页是不是 hub 页"

不是。[[bathtub-filter]] 是**入口和导航**，它只负责告诉读者"先看哪几页"。真正承载事实的核心页按层分开：

| 层 | 真理源页面 | 作用 |
|---|---|---|
| 产品结构 / IP | [[bathtub-filter-kes-patent-19-281644-modular-terminal-water-treatment]] | 专利申请着录事项与结构权威事实 |
| 产品配置（部件 / 尺寸 / 材质） | [[bathtub-filter-v1-free-chlorine-removal-dimensions-materials]] | 27 项 BOM，2026-07-02 裁定为全站口径 |
| 性能参数 / 寿命模型 | [[bathtub-filter-media-efficacy-at-bath-conditions]] §9 / §9.5，[[bathtub-filter-kes-page-how-we-test-and-certify]] | 去氯数字、寿命曲线、NSF 口径的唯一定义处 |
| 验证门槛 | [[bathtub-filter-25lpm-dechlorination-bench-test-spec]] | Gate 1 第三方 DPD 的测试矩阵与判定阈值 |
| 宣称边界 | [[bathtub-filter-claim-register]] | Allowed / Conditional / Banned 与表面映射 |
| 内容体系 | [[bathtub-filter-kes-marketing-site-content-map]] | 53 页 site/ 的施工蓝图 |
| 包装 / 套装 | [[bathtub-filter-kes-pack-contents-spec]]，[[bathtub-filter-kes-packaging-design-spec]] | 盒内物与印刷口径 |
| 对外文案 | [[bathtub-filter-kes-website-copy-v1]]，[[bathtub-filter-kes-amazon-listing-spec]] | ship 级英文文案 |

本页是对以上八层的**交叉审查**，方法是：把每层的数字和口径互相对照，做了几处独立计算（滤仓填充率、试纸分辨率、订阅节奏），并从需求数据反推营销定位。**本页不做实测，所有计算基于 wiki 内已有参数加明示假设。**

---

## 1. 总判断

1. **纪律层做得很好，工程闭环没跟上。** claim register、承重句、禁词、表面映射、证据标签这套机制在同类产品里极少见，文案本身几乎挑不出违规。但把这套机制往下压到 BOM 和台架 spec 时，出现了**四处口径与物理事实脱节**（§2 F1–F4），其中两处足以让当前 🟢 标签失效。
2. **2026-07-02 的 BOM 裁定只被当成"寿命重算"处理，没有被当成"性能重算"处理。** 主力去氯介质 CaSO₃ 从 130 g 降到 110 g，全站只把容量按 2.75/3.25 缩放，去氯率随流量的曲线、Gate 1 的 ≥85% 阈值、台架基准配置都还停在旧配置。
3. **用户自验证机制是整个信任叙事的地基，但试纸分辨率支撑不了它承诺的三档触发。** 这是产品与内容之间最硬的一个矛盾（§2 F6）。
4. **订阅经济学与寿命模型互相打架。** 90 天节奏对应的消耗量是寿命模型的约 3 倍，"skip-if-still-good" 一旦真实执行，LTV 模型就不成立（§4 M3）。
5. **定位在合规上是对的，在需求覆盖上偏弱。** "看得见"回应的是不信任者（宣传口径争议占 1–2 星的 17.3%），而四大购买动机里没有一个被首屏直接回应（§4 M2）。

---

## 2. 配置与参数层

### F1 · Gate 1 台架 spec 仍以裁定前配置为基准（P0）

[[bathtub-filter-25lpm-dechlorination-bench-test-spec]] §2.1 写的固定基准配置是 `PP 盘 + KDF55 110 g + CaSO₃ 130 g`，§2.2 床体积梯度以 130 g 为基准，§2.3 寿命坐标用 `3,481 L（≥99% 段末模型值）`，§5 引用「143 次泡 / 1 年」。这四个数全部是 2026-07-02 之前的口径。裁定后的口径是 KDF55 130 g / CaSO₃ 110 g / PET 滤棉 / ≥99% 段末 2,945 L / mandatory 121 baths。

后果：这是全站唯一决定 go/no-go 的测试，如果按现 spec 送第三方，测的不是要出货的产品。

处理：spec 逐项改到 BOM 口径；床体积梯度改为 90 / 110 / 130 / 160 g，把 110 g 设为基准并保留 130 g 作为回归对照点（顺带回答 F2）。

### F2 · 唯一的系统级实测来自旧配置，去氯率曲线从未按新配置重推（P0）

[[bathtub-filter-media-efficacy-at-bath-conditions]] §9.5 的 2026-03-20 直测架构是 `KDF55 110 g + CaSO₃ 130 g`。裁定后 CaSO₃ 减少 15%，KDF55 增加 18%。CaSO₃ 是短 EBCT 下的去氯主力，KDF 在 25 L/min 只贡献约 26%。按 wiki 自己的分工逻辑，这个互换应当**降低**流量段的去氯率，而不只是缩短寿命。

现状：T2 把「≥99% @15 L/min fresh filter」标 🟢结构，Gate 1 的 ≥85% 及格线"来自 27 L/min 在 5 ppm 下仍达 84%"，这两个数都是旧配置测出来的。裁定后没有任何页面重新推算或标注这一点。

处理：在 efficacy §9.5 和 T2 各加一行"该实测为 110/130 配置，与 V1 出货配置不同，方向性参考、幅度不可沿用"；≥85% 阈值在 Gate 1 前标为待校准。

### F3 · KDF55 滤仓按 BOM 尺寸只能装到四成满（P0，需工程确认）

用 BOM 参数做几何核算（假设：外径 120 mm、壁厚 1.5 mm → 内径 117 mm；中心支撑柱 Ø50 mm；有效高度 14 mm；KDF55 堆积密度 2.4–2.9 g/cm³，取 Kymera 公开规格约 2.7；CaSO₃ 堆积密度按 BOM 0.9–1.1）：

| 滤仓 | 环形截面 | 14 mm 床容积 | 介质体积 | 填充率 | 摊平床厚 |
|---|---:|---:|---:|---:|---:|
| KDF55 130 g | ~88 cm² | ~123 cm³ | 45–54 cm³ | **36–44%** | **5–6 mm** |
| CaSO₃ 110 g | ~88 cm² | ~123 cm³ | 100–122 cm³ | 81–99% | 11–14 mm |

三个推论：

- P1 / P2 写的「KDF55 床厚 15 mm」在这个壳体里装不出来，除非 KDF 用量翻倍或壳体缩小。
- **透明滤仓会让用户看到一个半空的 KDF 仓。** "看得见的料"这个主张在 KDF 仓上会反噬：半空的仓在货架开窗和 PDP 解剖图里都会被读成"料不足"。
- 松散床在 25 L/min 下会随水流位移，正是 D2 导流页想防的 channeling。

一个可能的解释：130 g CaSO₃（约 118–144 cm³）装不进 123 cm³ 的仓，所以 xlsx 把克数互换了。如果是这样，互换是**装配驱动**而非性能驱动，应当写进 BOM 页 §7 的裁定理由，并触发 F2 的重推。

处理：工程确认实际装填高度和是否有压料结构；若确实四成满，要么改 KDF 仓有效高度，要么在 KDF 仓加透明填充隔板，要么把可视化主张只落在 CaSO₃ 仓上。

### F4 · "35 L/min 无溢流包络"来自非 V1 配置（P0）

技术笔记记录的 2024-11-07 溢流测试配置是 `204 g KDF + 45 g 炭 + 1 层网 + 2 层纤维盘`。V1 是 `1 片 PET 盘 10 mm 120 g/m² + KDF 130 g + CaSO₃ 110 g`，滤棉的透水性和层数都不同。但这个 35 L/min 出现在 PDP key facts、Amazon B4、T2 §七，均标 🟢。

处理：用 V1 实机重做溢流包络；在此之前 PDP / Amazon 的 35 L/min 降为 🟡，或改写为"设计目标 ≤30 L/min 不溢出"（这是讲解件 §3.11 的原始口径）。

### F5 · "≥99% @15 L/min" 在 T2 是 🟢，在 website copy 是占位符（P1）

同一个数字在四个表面有三种状态：T2 §一 允许原文引用 ≥99%；P1 §二 标"🟢 定位 / 🟡 数字"；website copy 全部用 `[去氯率·待第三方实测]`；Amazon B1 用占位。而 wiki 内在 ~15 L/min 的唯一实测（16.5 L/min，5 ppm）是 ~90%，不是 99%。99% 来自寿命模型对"最佳体验段"的定义，不是流量段实测。

处理：T2 §一 的 ≥99% 降为 🟡，与其余表面统一为"Gate 1 前占位"。Gate 1 矩阵已含 15 L/min，测完回填即可。

### F6 · 试纸分辨率支撑不了 90 / 80 / 50% 三档触发（P0）

T3、买后验证页、skip-if-still-good 订阅都建立在"用户用游离氯试纸看到去除率掉到 ~90% / ~80% / <50%"上。把触发档换算成出水浓度：

| 进水游离氯 | 90% 软触发时出水 | 80% 强触发时出水 | 50% 强制时出水 |
|---:|---:|---:|---:|
| 2 ppm | 0.2 ppm | 0.4 ppm | 1.0 ppm |
| 1 ppm | 0.1 ppm | 0.2 ppm | 0.5 ppm |

常见游离氯试纸色阶是 0 / 0.5 / 1 / 2 / 4 / 10 ppm 一类的粗档。在这种分辨率下，软触发和强触发在 1–2 ppm 进水时都落在"0 与 0.5 之间"，用户看不出差别；只有 50% 强制点在 ≥1 ppm 进水时才可见。也就是说，用户能看到的只有"还在工作"和"基本失效"两态，看不到 wiki 承诺的三档。

后果：T3 的"你自己看到该换了"、订阅的"读数仍达标就 skip"在 1 ppm 城市几乎不可执行，用户会一直 skip 到滤芯彻底失效。

处理三选一：① 把触发口径改成试纸可执行语言（"当滤后试纸第一次显出 0.5 档颜色时更换"），同时把 T3 三档曲线留作内部口径；② 选用 0–1 ppm 低量程细分试纸（0 / 0.1 / 0.25 / 0.5 / 1）并在 P2 写明规格；③ 随盒改配 DPD 滴剂比色管。任何一种都要先在 P2 / T3 / 订阅页同步。

### F7 · BOM 与内容页的残留不一致（P2）

- BOM 有效高度 14 mm，P1 / P2 写床厚 15 mm。
- BOM 调节筋 125×20×3 mm，卖点页 / 安装指南 / P2 写 124 mm。
- BOM 已把 3M 挂钩（部件 2）和调节筋（部件 3）列为确认项，P2 #8 / #9 仍标"🟡 讲解件未列，待 BOM 确认"，应升 🟢。
- 三个 O 型圈线径 / 压缩量待确认，这是防旁通的关键件，Gate 1 前必须关闭。
- CaSO₃ 堆积密度单位 g/cm² 应为 g/cm³，BOM 页已注但源表未改。
- PET 滤棉 120 g/m² × 10 mm → 体积密度约 12 kg/m³，极其蓬松。要确认 25 L/min 冲击下不会压实成流阻，这直接影响 F4。

### F8 · "补芯"到底是换整个 Tritan 滤仓还是只换介质，没有决策（P1）

P2 §三 写"透明滤仓可替换"，订阅页叫"补芯"，专利页写处理腔"可重复开启"，BOM 上下盖是 33° 卡扣。没有任何页面回答用户买的 refill 是整仓还是散装介质。这决定 refill COGS、refill 价格、包装体积、可持续性措辞，以及"看得见的料"是否延伸为"自己装的料"。

处理：产品拍板并写进 P2 §三 与订阅页。

---

## 3. 包装层

P5 是这批内容里最成熟的一页：开窗对准滤仓、试纸在最上层、单一 QR、Prop 65 不藏 QR、竞品差评反写，逻辑都成立。问题集中在包装承载的**使用负担**和**未拍板项**：

### K1 · 维护指令与第一购买动机冲突（P1）

维护指南和 IFU 的承重句是 `After each fill, remove the cartridge, drain it, and let it air-dry. Do not store it wet.` 而 2562 条评论里"安装方便 / 挂上就能用"是并列第一购买动机（23.6%）。V1 是四段式叠层，每次泡澡后取下、倒水、晾干，再挂回去，这个负担会直接落进"维护负担"投诉簇。

处理：优先在结构上解决（底部排水口 / 快拆卡扣 / 在位滴干设计），其次把指令降级为"注水结束后让它在龙头上滴干，不要收进柜子"，把"取下晾干"留给长期不用的情形。

### K2 · 浴盐仓是不透明 ABS，可视化在最容易脏的地方停了（P2）

浴盐 / 精油 / bath bomb 全部在浴盐仓接触水流，3,846 个 0.7 mm 孔是最容易积垢发霉的位置，而这一仓是白壳。"看得见"在真正需要看的地方看不见。另外泡泡浴通过孔板起泡是否会顶溢，没有任何测试记录。

### K3 · 包装 L3 层依赖两个未进 BOM 的提案（P2）

分享试纸卡 ×3 和 Before/After 对比卡在 P2 是 🟡 提案，但 P5 §二 已把它们排进开箱层序。若产品不批，包装刀模要改。

### K4 · 动态重量与挂点（待数据）

四段壳体 + 240 g 介质 + 防溢水仓在用时的 ~0.6 L 水，动态挂重估计接近 1.5–2 kg，全部经硅胶挂带落在提拉头或 3M 挂钩上。现有记录是 freestanding 静态 2 kg。需要 25 L/min 动态注水下的挂点位移记录，这在 E 层卡点里已有，此处只提醒它同时是包装"tool-free strap install"文案的前提。

---

## 4. 营销层

### M1 · 承重定位句自己带了健康框架（P1）

register 要求每个表面都出现 `It is an end-stage harm-reduction module for the bath-fill scenario.` "harm-reduction" 是公共卫生用语，隐含"水有害"。这与 register 禁 toxin-panic、禁健康暗示的方向相反，而且它出现在每一个表面。建议改为 `a bath-fill dechlorination module` 或 `an end-stage free-chlorine reduction module`。

### M2 · 首屏主张服务的是怀疑者，不是主要购买动机（P1）

| 购买动机（2562 条评论） | 占比 | V1 首屏是否直接回应 |
|---|---:|---|
| 改善泡澡后皮肤 / 头发体感 | 23.6% | 否，只在 FAQ 与 Conditional sensory 行 |
| 安装方便 / 挂上就能用 | 23.6% | 部分（tool-free strap），但被 K1 抵消 |
| 适合宝宝 / 敏感肌场景 | 23.5% | 主动不回应（正确） |
| 缓解硬水干涩 | 20.7% | 主动不回应（正确），但 21% 提到硬水的人被"阻垢不软化"劝退 |
| 宣传口径争议（1–2 星内） | 17.3% | **是**，这是"看得见"的真正靶点 |

现在的 Hero（`You read your food labels… What about your bath water?` / `Clean is what you can see.`）把透明当主张。透明是**证明层**，不是**收益层**。register 已经允许感官层表达（"氯味不刺鼻、刺激感更低、feels different"），这才是与最大动机对上的合法收益。建议结构改为：收益句（感官）→ 机制句（去游离氯）→ 证明句（看得见、测得到）。透明保留为品牌骨架，但不再独占首屏。

### M3 · 订阅节奏与寿命模型互相矛盾（P0）

GTM 页：90 天 auto-ship，$19–27 / 期，per-bath $0.27–0.35，TCO 对比按一年 4 次补芯（$69 + 4×$23）。T3 / 寿命模型：2 ppm、3 次/周下 mandatory ≈121 baths ≈ 40 周；1 ppm 下约 2 倍。

核算：一年 4 次补芯 = 模型消耗量的约 3 倍（2 ppm）到 6 倍（1 ppm）。$23 / 90 天 ÷ 39 baths ≈ $0.59 / bath，不是 $0.27–0.35。两种结局只能取一：要么用户按"skip-if-still-good"跳过 2/3 的发货，LTV 模型和 TCO 对比全部失效；要么用户不跳，产品在"诚实订阅"的名义下多卖了 3 倍滤芯。

处理：默认周期改为与 T3 一致（2 ppm 城市约 9 个月，1 ppm 城市 12 个月以上，由 ZIP 诊断分档）；90 天节奏只留给 PET 滤棉 + 试纸的耗材包；TCO 对比按 1–1.5 次/年重算。订阅页已把周期留空 🟡，是对的，但 GTM 页的 90 天与 $161 TCO 需要同步撤回。

### M4 · 性能锚点定在 15 L/min，低于典型使用流量（P1）

T2 把 15 L/min 作为性能主口径，同时承认美国龙头常见 18–25 L/min。在诚实叙事的品牌里，这会被读成 cherry-pick，而且"test it yourself"会让用户在自家 22 L/min 龙头上验证到低于宣传的读数。Gate 1 矩阵已含 15 / 20 / 25，建议对外发布时直接给三点曲线，不用单点。

### M5 · 产品线在 V1 未过 Gate 1 前已横向展开（P2）

氯胺版、井水版被标 GO，site/ 有 S2 / S3 / M3–M6 等页面为不存在的 SKU 建了内容。诚实劝退 + 留邮箱的路径是对的，但内容维护成本已经在增加，且氯胺版依赖抗坏血酸浸泡步骤，用户负担比 K1 更重，这点在决策页里没有被权衡。

### M6 · Amazon 五点把 🟡 内部模型数字放到了最严的表面（P2）

Amazon B5 写 `soft trigger ≈ 96 baths, replace by ≈ 121 baths`，这两个数在 T3 自己的证据表里是"内部模型 🟡 待 Gate 1"。网站可以带限定语讲，Amazon 表面的 substantiation 要求更高。建议 Amazon 只写"replace when your after-strip shows chlorine again; typical range printed in the manual"，数字留在 PDP 网页版。

---

## 5. 文案层

website copy 是这批材料里执行最好的一页，上线自检清单本身就是资产。以下是剩余问题：

### C1 · 主 tagline 把"clean"和"可见"绑在一起（P2）
`Clean is what you can see.` 中的 clean 会被读成"水更干净"。register 自己写了"可见不得暗示更有效"，tagline 却在做这件事。`Filter media you can see. A formula you can read.` 已经足够，clean 这句可以删。

### C2 · 对照竞品的语气与"不贬竞品"规则有张力（P2）
`They're betting you won't look.`、`not the cheap filler hiding behind opaque plastic` 属于指向性贬损，虽未点名，但 PDP 护栏写的是"讲设计选择、非贬竞品"。建议保留对照结构，去掉动机归因（"betting"）和"cheap filler"。

### C3 · PDP key facts 把流量当适配属性（P2）
`Fits standard US tub spouts (18–25 L/min); no-overflow envelope up to 35 L/min` 混了两件事，且 35 L/min 有 F4 问题。拆成"适配：见 fit guide"和"流量：设计目标 ≤30 L/min"。

### C4 · 浴盐相关卖点没有任何测试（P2）
"无需手动搅拌、减少沉底、减少 floating filter 堵塞"三条在卖点页 §5 是叙述，没有对应验证记录，且 K2 的起泡顶溢未测。建议这三条降 🟡，或只保留"250 mL 装载仓"这个结构事实。

### C5 · Maker note 是占位（P1）
About 页 `Designed and tested by [Name], [N]-year water-filtration engineer` 承载 E-E-A-T 的 Experience 维度。若没有可署名的真实工程师，整段删除比留占位安全。

### C6 · 同一数字在各表面的状态不统一（P1）
去氯率、寿命 baths、35 L/min、床厚 15 mm、124/125 mm 五组数字在 T2 / P1 / P2 / website / Amazon / spec 之间各有版本。内容 SOP 里有"数字传播检查表"，建议把本页 F1 / F4 / F5 / F7 / M6 逐条跑一遍。

---

## 6. 优先修复清单

| 优先级 | 项 | 涉及页 | 负责 |
|---|---|---|---|
| P0 | Gate 1 spec 改到 BOM 配置，床体积梯度以 110 g 为基准（F1） | 25lpm spec | 产品 |
| P0 | 工程确认 KDF 仓实际装填高度；决定是否改壳、加隔板或放弃 KDF 仓可视化（F3） | BOM、D3、P5 | 工程 |
| P0 | 用 V1 实机重做溢流包络；此前 35 L/min 降 🟡（F4） | T2、PDP、Amazon B4 | 工程 |
| P0 | 触发口径改成试纸可执行语言，或换低量程试纸 / DPD 滴剂（F6） | T3、P2、订阅页、买后验证页 | 产品 + 运营 |
| P0 | 订阅默认周期与 T3 对齐；撤回 90 天 / $161 TCO 口径（M3） | GTM 页、订阅页、bundle 页 | 运营 + 财务 |
| P1 | efficacy §9.5 与 T2 标注"实测为旧配置"；≥85% 阈值待校准（F2） | efficacy、T2、spec | 产品 |
| P1 | T2 的 ≥99% 降 🟡，与 website / Amazon 统一（F5） | T2、P1 | 内容 |
| P1 | 定位句去掉 harm-reduction（M1） | register、所有表面 | 策略 |
| P1 | 首屏改为收益 → 机制 → 证明（M2） | website copy、版式页 | 市场 |
| P1 | 维护指令降级或结构解决排水（K1） | 维护指南、IFU、结构 | 工程 + 内容 |
| P1 | 拍板 refill = 整仓 / 介质（F8） | P2、订阅页 | 产品 |
| P1 | Maker note 落实或删除（C5） | website copy | 市场 |
| P2 | P2 #8 / #9 升 🟢；床厚 14 vs 15、124 vs 125 统一（F7） | P1、P2、卖点页 | 内容 |
| P2 | 浴盐仓卖点降 🟡；起泡顶溢加入测试协议（C4、K2） | 卖点页、validation protocol | 产品 |
| P2 | tagline 与竞品对照语气微调（C1、C2） | website copy | 市场 |
| P2 | Amazon B5 去内部模型数字（M6） | Amazon spec | 运营 |

---

## 8. 2026-09-05 处理记录

| 项 | 处理 | 状态 |
|---|---|---|
| F1 | 25lpm spec §0 / §2.1 / §2.2 / §2.3 / §4 / §5 改到 BOM 配置；新增 §2.5 装填与溢流复核 | ✅ 桌面完成 |
| F2 | efficacy §9.5、spec §0 / §4 标注"旧配置、幅度不可沿用" | ✅ |
| F3 | 登记 D-10；P1 / P2 床厚改为"仓有效高 14 mm、装填待确认"；测试项进 spec §2.5 与 validation protocol Module 3 | ⏳ 待工程实测 |
| F4 | T2、PDP key facts、Amazon B4、claim register Fit 行、结构总览、挂带页、技术笔记全部把 35 L/min 降 🟡；对外改写设计目标 ≤30 L/min；复测进 protocol | ⏳ 待 V1 复测 |
| F5 | T2 §一 / §七 的 ≥99% 数字降 🟡，与 website / Amazon 占位统一 | ✅ |
| F6 | T3 新增 §〇 试纸可执行触发；post-purchase、IFU、包装 §三 #2、Amazon B5、website PDP 全部改为该主句；96 / 121 只留说明书典型范围与 PDP 网页版；登记 D-11 试纸量程；P2 #7 加量程要求 | ✅ 文案 / ⏳ 试纸选型 |
| F7 | P2 #8 / #9 升 🟢；124 → 125 mm 按 BOM 全站统一；床厚 15 → 有效高 14 | ✅ |
| F8 | 登记 D-09，P2 §三 挂链 | ⏳ 待产品拍板 |
| K1 | 维护指南 §一 改为"在位滴干 + 每周深晾"两级（🟡 待 Module 4 霉变观察）；EN 句同步；IFU 引用 P3 自动跟随 | ⏳ 待观察验证 |
| K2 / C4 | 卖点页 §5 三条浴盐卖点降 🟡；起泡顶溢进 spec §2.5 | ✅ 降级 / ⏳ 测试 |
| M1 | register Positioning 行、P1、FAQ、结构总览：harm-reduction → free-chlorine reduction；「减害」→「除游离氯」 | ✅ |
| M2 | website copy Hero 改为 收益 → 机制 → 证明；原 H1 移入区块 2 | ✅（版式页需跟随） |
| M3 | GTM §0 / §1.2 / §4.2 / §5 按寿命分档重写；订阅页默认周期改；登记 D-12 让 finance 重跑 LTV | ✅ 口径 / ⏳ LTV |
| M6 | Amazon B5 去内部模型数字 | ✅ |
| C1 / C2 | tagline 删 "Clean is what you can see"；去 "betting you won't look" 与 "cheap filler" | ✅ |
| C5 | Maker note 改团队署名 | ✅ |

未处理：M4（15 L/min 锚点，等 Gate 1 三点曲线）、M5（产品线展开节奏，策略决定）、K3（分享卡 / 对比卡进 BOM，产品拍板）、K4（动态挂重，E 层既有卡点）。

## 7. 本页的边界

- 所有填充率、出水浓度、订阅消耗量都是**桌面核算**，输入来自 BOM 页、efficacy §9、T3、GTM 页；KDF55 堆积密度取公开规格 2.4–2.9 g/cm³，试纸色阶取市售常见规格。工程侧任何一个输入不同，F3 / F6 的结论要重算。
- 本页不替代 Gate 1、溢流复测、挂点动态测试；它只指出这些测试在现 spec 下测的是什么，以及测完要回改哪些页。
- 本页不改动被审查页面。修复由各负责方按 §6 执行后，在 [[bathtub-filter-research-coverage-gaps]] 追加批次记录。

## Sources

- [[bathtub-filter-v1-free-chlorine-removal-dimensions-materials]]（BOM 27 项、裁定 §7）
- [[bathtub-filter-kes-patent-19-281644-modular-terminal-water-treatment]]
- [[bathtub-filter-25lpm-dechlorination-bench-test-spec]]（§0 基线、§2 矩阵、§4 阈值）
- [[bathtub-filter-media-efficacy-at-bath-conditions]]（§9 寿命模型、§9.5 直测）
- [[bathtub-filter-technology-notes]]（2024-11-07 溢流测试配置）
- [[bathtub-filter-kes-v1-selling-points-and-pack-contents]]
- [[bathtub-filter-kes-v1-pricing-channel-launch-geo-subscription]]（§1.2、§4.2 订阅）
- [[bathtub-filter-kes-website-copy-v1]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-competitor-review-labeling-analysis-2026-06-02]]（购买动机与投诉占比）
- site/：[[bathtub-filter-kes-v1-definition-and-not-for-list]]、[[bathtub-filter-kes-pack-contents-spec]]、[[bathtub-filter-kes-packaging-design-spec]]、[[bathtub-filter-kes-page-how-we-test-and-certify]]、[[bathtub-filter-kes-page-replacement-and-lifespan]]、[[bathtub-filter-kes-amazon-listing-spec]]、[[bathtub-filter-kes-print-ifu-spec]]、[[bathtub-filter-kes-install-and-compatibility-guide]]、[[bathtub-filter-kes-refill-subscription]]、[[bathtub-filter-kes-care-and-maintenance-guide]]、[[bathtub-filter-kes-marketing-site-content-map]]
