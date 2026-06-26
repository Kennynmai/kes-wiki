---
type: product
status: draft
owner: product
created: 2026-06-03
updated: 2026-06-17
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, spout-fit, attachment, flat-strap]
source_count: 5
review_cycle: monthly
verification_status: partial_sample_validated_test_pending
related:
  - ./bathtub-filter-supported-spout-matrix.md
  - ./bathtub-filter-installation-risk-matrix-v2.md
  - ./bathtub-filter-test-gating-checklist-for-kes.md
---

# KES 扁硅胶挂带适配方案（2026-06-03）

## 结论

KES 已有一套针对 bathtub spout 安装稳定性的设计方案，不是空白：

- 21 mm 宽扁硅胶挂带
- 左右各 4 个长度调节孔
- 中央圆形挂位孔，用于套过提拉分水器的提拉头
- 无提拉分水器 spout 使用 3M 贴挂钩模拟挂位
- 弧面 / 异形 spout 使用附赠的5孔总长124mm，宽20mm的扎带固定 3M 贴挂钩

这套方案可以把 `supported spout matrix` 从“无方案 TBD”推进到“有设计覆盖，待实测验证”。2026-06-17 已补入 2 组 RV / mobile-home center-set / valve-diverter faucet 正向适配样本、S-01 non-diverter 周长边界实测记录，以及 freestanding tub filler 弧形/异型管非瀑布出水 2 kg 承重记录；但它还不是完整的 `supported / conditional / not-supported` 结论。

## 设计逻辑

### 1. 扁挂带 vs. 圆线挂带

竞品常见圆线挂带在 bathtub 场景有一个结构弱点：浴缸注水需要较高流量，水流冲击会放大滤体摇晃；圆线与 spout 接触面积小，更容易让滤体左右摆动，导致水流打到滤体侧面或绕过滤体。

KES 的扁硅胶挂带宽 21 mm，与 bathtub spout 接触面积更大。设计意图是增加接触面和摩擦稳定性，降低高流量下的摆动。

### 2. 带提拉分水器的 tub spout

挂带正中间有圆形孔。硅胶有弹性，可拉开后套过提拉分水器的提拉头。

这个方案的核心价值：

- 用提拉头形成天然定位点
- 让滤体中心线对准 spout 出水口
- 减少偏心冲击
- 降低水流冲到滤体侧面的概率

![[raw/products/bathtub-filter/2026-06-03-kes-flat-strap-spout-fit-design/01-flat-silicone-strap-diverter-spout-render.png]]

### 2.1 已实测可用样本：RV / mobile-home center-set / valve-diverter faucet

2026-06-17 用户补充：**Mobile Home RV Tub Shower Center-Set Faucet 已实测可以用**。

![[raw/products/bathtub-filter/2026-06-17-rv-center-set-faucet-fit-evidence/01-mobile-home-rv-tub-shower-center-set-faucet.jpg]]

2026-06-17 用户补充：**RV Tub & Shower Faucet Valve Diverter 已实测可以用**。

![[raw/products/bathtub-filter/2026-06-17-rv-center-set-faucet-fit-evidence/02-rv-tub-shower-faucet-valve-diverter-black.jpg]]

![[raw/products/bathtub-filter/2026-06-17-rv-center-set-faucet-fit-evidence/03-rv-tub-shower-faucet-valve-diverter-ivory.jpg]]

归类：

- fixture type：Mobile Home RV Tub Shower Center-Set Faucet
- fixture type：RV Tub & Shower Faucet Valve Diverter
- spout feature：中央 tub spout + pull-up diverter knob
- taxonomy：S-02 straight spout with diverter knob 的 RV / mobile-home center-set 变体
- fit result：上述 2 组样本正向通过，可作为 S-02 路线的 first-party fit evidence

证据边界：这说明已测试的样本可用，不能直接扩大为所有 RV 龙头、所有 center-set 龙头或所有 S-02 spout 均已支持。仍需补出水嘴中心到墙面距离、提拉头直径、挂带孔位、测试流速、是否漏水/溢流/绕流和重复注水周期稳定性。

### 3. 无提拉分水器的 tub spout

对于没有提拉头的 bathtub spout，KES 配 3M 贴挂钩，贴在 spout 上，用它模拟提拉头的挂位作用。

2026-06-17 用户补充：S-01 straight non-diverter, stable 已实测。适配边界为：**末端折弯位置周长 <=18 cm 可用**；常规末端折弯位置周长约 **15-17 cm**。

此处的附件组合为：

- 附赠的5孔总长124mm，宽20mm的扎带
- 附赠 3M 贴挂钩
- 21 mm 扁硅胶挂带

结构逻辑：附赠的 124mm 硅胶扎带可拉伸到 22 cm，与 3M 贴挂钩组合后，可在 non-diverter spout 上模拟 diverter 的悬挂位置。这里的主固定力来自 **5 孔硅胶扎带的拉力与硅胶对 spout 表面的摩擦力**；3M 胶不是主要承重件，主要作用是防止 ABS 挂钩与金属浴缸嘴接触面之间发生硬碰硬滑移。

![[raw/products/bathtub-filter/2026-06-17-s01-non-diverter-fit-evidence/01-round-black-downturned-non-diverter-spout.png]]

![[raw/products/bathtub-filter/2026-06-17-s01-non-diverter-fit-evidence/02-square-gold-downturned-non-diverter-spout.png]]

![[raw/products/bathtub-filter/2026-06-17-s01-non-diverter-fit-evidence/03-curved-black-non-diverter-spout.png]]

![[raw/products/bathtub-filter/2026-06-17-s01-non-diverter-fit-evidence/04-brushed-nickel-square-non-diverter-spout-kit.png]]

![[raw/products/bathtub-filter/2026-06-17-s01-non-diverter-fit-evidence/05-white-rectangular-non-diverter-spout.png]]

![[raw/products/bathtub-filter/2026-06-17-s01-non-diverter-fit-evidence/06-chrome-rounded-non-diverter-spout.png]]

这里需要记录 / 验证的不是 3M 胶承重，而是扎带固定后的整体稳定性：

- 5 孔硅胶扎带在常规孔位下是否能拉紧，并持续提供足够摩擦力
- ABS 挂钩被扎带压紧后是否发生位移或转动
- 动态注水下滤体是否因水流冲击而摆动、偏心或绕流
- 用户安装位置偏差下，扎带拉力是否仍能把挂钩稳定压在 spout 上

### 4. 弧面 / 异形 spout

对于弧面或异形 spout，KES 配附赠的5孔总长124mm，宽20mm的扎带，用来扎住 3M 贴挂钩。固定逻辑是硅胶扎带的拉力与摩擦力把挂钩压紧在 spout 上；3M 胶只作为辅助防滑层，避免 ABS 挂钩直接接触金属浴缸嘴时滑动。

![[raw/products/bathtub-filter/2026-06-03-kes-flat-strap-spout-fit-design/02-curved-spout-hook-and-short-tie-render.png]]

### 4.1 已实测可用样本：freestanding tub filler 弧形/异型管非瀑布出水

2026-06-17 用户补充：**Freestanding tub filler，弧形管、异型管、非瀑布出水都可以用**，已实测 **2 kg 承重**。

![[raw/products/bathtub-filter/2026-06-17-freestanding-tub-filler-fit-evidence/01-freestanding-curved-tub-filler-strap-hook-fit-test.jpg]]

安装方式：

- 使用附赠的5孔总长124mm，宽20mm的扎带 + 附赠 3M 贴挂钩。
- 扎带只扎到倒数第二个孔时，常规可通过拉扯扎带完成安装。
- 扎到倒数第三个孔会更紧，但需要较大拉力组装，对女性用户不太友好，不宜作为默认要求。
- 扎带需要扎在距离出水嘴末端 **60 mm** 处；重力会拉扯扎带向下变形，如果太靠近末端会滑落。

证据边界：该记录支持 freestanding tub filler 中弧形管 / 异型管 / 非瀑布出水的安装可行性，不自动支持 waterfall / 宽体片状出水，也不替代动态注水、溅水/绕流、重复注水后的长期稳定性记录。

## 墙距与偏心安装边界

墙距边界修正为：**出水嘴中心到墙面的距离 ≥60 mm 是居中美观线，不是功能限制线**。

计算口径：

- KES 当前结构横向包络尺寸参考值为 120 mm。
- 以中心对准出水口安装时，需要至少半宽空间：120 mm / 2 = 60 mm。
- 但滤体允许相对出水口偏心安装约 20 mm，因此出水嘴中心到墙面 **40-60 mm 仍可用**，只是出水不在滤体正中，视觉上不完美/不美观。
- 用户提供观察为：实际浴缸出水嘴基本没有少于 40 mm 的墙距；竞品也没有出现这方面的集中投诉。

使用边界：

- `>=60 mm`：居中安装，外观和对准效果最好。
- `40-60 mm`：偏心安装可用，功能上不是限制条件，但外观不完美，需记录偏心量、溅水/绕流和用户视觉接受度。
- `<40 mm`：理论极端值；用户观察为实际浴缸嘴基本没有少于 40 mm。若遇到，应作为异常样本记录，而不是当前 V1 的常规限制条件。
- 60 mm 不是“不支持”线，只是居中美观线。

## 对 spout taxonomy 的影响

| Spout type | 设计覆盖 | 仍需验证 |
|---|---|---|
| S-01 straight non-diverter | 附赠的5孔总长124mm，宽20mm的扎带 + 3M 贴挂钩模拟挂位；主固定力来自硅胶扎带拉力和摩擦力，3M 胶仅辅助防滑；末端折弯位置周长 <=18 cm 已实测可用，常规约 15-17 cm | 具体 spout 的实测周长、扎带孔位、挂钩是否位移、动态注水冲击、20 次 fill-cycle 后稳定性 |
| S-02 straight with diverter knob | 中央圆孔套过提拉头，是当前最强覆盖场景；2026-06-17 已有 2 组 RV / mobile-home center-set / valve-diverter faucet 样本实测可用 | 不同提拉头直径、硅胶撕裂、偏心、diverter 可操作性、动态注水表现 |
| S-03 curved / gooseneck-like | 3M 贴挂钩 + 附赠的5孔总长124mm，宽20mm的扎带；主固定力来自硅胶扎带拉力和摩擦力；freestanding tub filler 弧形/异型管非瀑布出水已实测 2 kg 承重，扎带位置为距离出水嘴末端 60 mm | 其他曲面形态、动态注水、溅水/绕流、重复注水后扎带变形或挂钩位移 |
| S-04 short projection | 出水嘴中心到墙面 >=60 mm 可居中安装；40-60 mm 可偏心使用 | 偏心量、溅水/绕流、安装手部空间、视觉接受度 |
| S-05 wide-body decorative | 有潜在风险 | 宽体表面是否能稳定贴钩或挂带是否偏移 |
| S-06 wobbling slip-fit | 设计不能消除 spout 本体晃动 | 即使挂住，spout base wobble 仍可能放大滤体摆动 |
| S-07 threaded varied outlet | 依具体外形，可能适用 S-01/S-02/S-03 方案 | 出水口截面和提拉结构差异 |
| S-08 low-clearance | 40-60 mm 可偏心使用；>=60 mm 居中更美观；<40 mm 为理论极端 | 偏心量、溅水/绕流、是否影响用户接受度 |

## 不应过度宣称

当前可写成内部判断：

- “KES 已有针对 diverter / non-diverter / curved spout 的附件设计方案。”
- “扁硅胶挂带通过更大接触面积，设计上比圆线挂带更抗摇晃。”
- “中央挂位孔可利用提拉分水器提拉头做定位点。”

当前不能写成对外结论：

- “fits all tubs”
- “支持所有 bathtub spout”
- “不漏水 / 不溢水 / 不摇晃”
- “3M 胶本身可作为主要承重或长期粘接结构”
- “wide-body / low-clearance / wobble spout 均支持”
- “40-60 mm 偏心安装自动等于稳定安装”

## 下一步测试

最小测试集：

- S-02 straight pull-up diverter：至少 3 个不同提拉头直径
- S-01 straight non-diverter：末端折弯位置周长 <=18 cm 的样本，附赠的5孔总长124mm，宽20mm的扎带 + 3M 贴挂钩；记录扎带孔位、拉紧难度、挂钩是否位移和 20 次 fill-cycle
- S-03 curved / gooseneck-like：3M 贴挂钩 + 附赠的5孔总长124mm，宽20mm的扎带；freestanding tub filler 非瀑布出水需要记录扎带距出水嘴末端 60 mm、扎带孔位、2 kg 承重和动态注水表现
- S-04 short projection：确认出水嘴中心到墙面 40-60 mm 时偏心安装的稳定性、溅水/绕流和视觉接受度
- S-08 low-clearance：验证 40-60 mm 偏心安装；<40 mm 仅作为理论极端记录
- S-06 wobbling slip-fit：确认是否明确排除

记录字段：

- 是否居中对准出水口
- 是否需要 workaround
- 18-25 L/min 是否摇晃
- 30-35 L/min 是否摇晃 / 溢流 / 绕流
- 20 次冷热湿循环后是否脱落
- 用户是否能无工具安装和移除

## Raw

Raw 目录：`raw/products/bathtub-filter/2026-06-03-kes-flat-strap-spout-fit-design/`

- `README.md`
- `01-flat-silicone-strap-diverter-spout-render.png`
- `02-curved-spout-hook-and-short-tie-render.png`

Fit evidence raw 目录：`raw/products/bathtub-filter/2026-06-17-rv-center-set-faucet-fit-evidence/`

- `README.md`
- `01-mobile-home-rv-tub-shower-center-set-faucet.jpg`
- `02-rv-tub-shower-faucet-valve-diverter-black.jpg`
- `03-rv-tub-shower-faucet-valve-diverter-ivory.jpg`

S-01 fit evidence raw 目录：`raw/products/bathtub-filter/2026-06-17-s01-non-diverter-fit-evidence/`

- `README.md`
- `01-round-black-downturned-non-diverter-spout.png`
- `02-square-gold-downturned-non-diverter-spout.png`
- `03-curved-black-non-diverter-spout.png`
- `04-brushed-nickel-square-non-diverter-spout-kit.png`
- `05-white-rectangular-non-diverter-spout.png`
- `06-chrome-rounded-non-diverter-spout.png`

Freestanding tub filler fit evidence raw 目录：`raw/products/bathtub-filter/2026-06-17-freestanding-tub-filler-fit-evidence/`

- `README.md`
- `01-freestanding-curved-tub-filler-strap-hook-fit-test.jpg`
