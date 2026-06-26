---
type: product
status: draft
owner: strategy
created: 2026-04-17
updated: 2026-06-17
visibility: team
confidence: low
officiality: draft
domain: product
domains: [bathtub-filter, kes, compatibility, installation, fit]
source_count: 7
review_cycle: monthly
verification_status: partial_sample_validated_test_pending
related:
  - ./bathtub-filter-compatibility-engineering-breakpoints.md
  - ./bathtub-filter-installation-risk-matrix-v2.md
  - ./bathtub-filter-test-gating-checklist-for-kes.md
  - ./bathtub-filter-kes-flat-strap-spout-fit-design-2026-06-03.md
---

# 浴缸龙头适配矩阵

## Why this page exists

这是 **Gate 2 必须完成的 artifact**，在安装/兼容性测试范围锁定前必须填充完整。

当前状态：**partial-sample validated / broader test-pending matrix**。2026-06-03 已补入 KES 扁硅胶挂带、中央提拉头挂孔、3M 贴挂钩和附赠的5孔总长124mm，宽20mm的扎带方案；2026-06-17 已补入 2 组 RV / mobile-home center-set / valve-diverter faucet 正向适配样本、S-01 non-diverter 周长边界实测记录，以及 freestanding tub filler 弧形/异型管非瀑布出水的 2 kg 承重正向记录。但 spout type support status 仍未经完整动态注水测试确认。

**不得在完成以下工作前将此页用于产品决策：**
1. 获得各类 spout 的实物样本
2. 实际测试每类 spout 的 attachment、retention stability、overflow risk
3. 将 support status 从 "design-covered / test pending" 更新为 "supported / conditional / not-supported"

## 2026-06-03 KES 扁挂带方案补充

详见 [[bathtub-filter-kes-flat-strap-spout-fit-design-2026-06-03]]。

设计方案：

- 主挂带为 21 mm 宽扁硅胶带，左右各 4 个长度调节孔。
- 对带提拉分水器的 tub spout，挂带中央圆孔可拉伸套过提拉头，使滤体中心线对准 spout 出水口。
- 对无提拉分水器的 straight spout，附赠 3M 贴挂钩，模拟提拉头挂位。
- 对弧面 / 异形 spout，使用附赠的5孔总长124mm，宽20mm的扎带扎住 3M 贴挂钩；主固定力来自硅胶扎带的拉力与摩擦力，3M 胶只作为辅助防滑层，避免 ABS 挂钩与金属浴缸嘴硬接触时滑动。
- 墙距边界修正为：**出水嘴中心到墙面距离 ≥60 mm 是居中美观线，不是功能限制线**。KES 产品横向包络尺寸为 120 mm；居中安装需要 60 mm 半宽空间，但滤体允许偏心安装约 20 mm，因此 **40-60 mm 可用，只是不完全居中 / 不完美美观**。用户观察为：实际浴缸出水嘴基本没有少于 40 mm 的墙距。

证据边界：这是 KES 设计意图和结构方案，不是最终实测通过记录。它能关闭“没有安装方案”的缺口，但不能关闭“不同 spout 类型已支持”的验证缺口。

---

## 2026-06-17 已实测可用样本：RV / mobile-home center-set / valve-diverter faucet

用户补充：**Mobile Home RV Tub Shower Center-Set Faucet 已实测可以用**。

![[raw/products/bathtub-filter/2026-06-17-rv-center-set-faucet-fit-evidence/01-mobile-home-rv-tub-shower-center-set-faucet.jpg]]

用户补充：**RV Tub & Shower Faucet Valve Diverter 已实测可以用**。

![[raw/products/bathtub-filter/2026-06-17-rv-center-set-faucet-fit-evidence/02-rv-tub-shower-faucet-valve-diverter-black.jpg]]

![[raw/products/bathtub-filter/2026-06-17-rv-center-set-faucet-fit-evidence/03-rv-tub-shower-faucet-valve-diverter-ivory.jpg]]

归类：

- fixture type：Mobile Home RV Tub Shower Center-Set Faucet
- fixture type：RV Tub & Shower Faucet Valve Diverter
- spout feature：中央 tub spout + pull-up diverter knob
- taxonomy：S-02 straight spout with diverter knob 的 RV / mobile-home center-set 变体
- fit result：上述 2 组样本正向通过，可作为 S-02 路线的 first-party fit evidence

证据边界：

- 这些记录支持“已测试的 RV / mobile-home center-set / valve-diverter + pull-up diverter 样本可用”
- 不自动扩大为“所有 RV 龙头 / 所有 center-set 龙头 / 所有 S-02 spout 都已支持”
- 仍需补：出水嘴中心到墙面距离、提拉头直径、挂带孔位、测试流速、是否漏水/溢流/绕流、重复注水周期稳定性

Raw：`raw/products/bathtub-filter/2026-06-17-rv-center-set-faucet-fit-evidence/`

---

## 2026-06-17 已实测可用样本：S-01 non-diverter circumference boundary

用户补充：**S-01 Straight non-diverter, stable 已实测**。适配边界为：**末端折弯位置周长 <=18 cm 可用**；常规 spout 末端折弯位置周长约 **15-17 cm**。

![[raw/products/bathtub-filter/2026-06-17-s01-non-diverter-fit-evidence/01-round-black-downturned-non-diverter-spout.png]]

![[raw/products/bathtub-filter/2026-06-17-s01-non-diverter-fit-evidence/02-square-gold-downturned-non-diverter-spout.png]]

![[raw/products/bathtub-filter/2026-06-17-s01-non-diverter-fit-evidence/03-curved-black-non-diverter-spout.png]]

![[raw/products/bathtub-filter/2026-06-17-s01-non-diverter-fit-evidence/04-brushed-nickel-square-non-diverter-spout-kit.png]]

![[raw/products/bathtub-filter/2026-06-17-s01-non-diverter-fit-evidence/05-white-rectangular-non-diverter-spout.png]]

![[raw/products/bathtub-filter/2026-06-17-s01-non-diverter-fit-evidence/06-chrome-rounded-non-diverter-spout.png]]

归类：

- taxonomy：S-01 straight non-diverter, stable
- fit boundary：末端折弯位置周长 <=18 cm
- common range：常规末端折弯位置周长约 15-17 cm
- accessory：附赠的5孔总长124mm，宽20mm的扎带 + 附赠 3M 贴挂钩
- accessory stretch：124mm 硅胶扎带可拉伸到 22 cm
- fit logic：扎带 + 3M 贴挂钩组合可模拟 diverter 的悬挂位置；主固定力来自硅胶扎带拉力与摩擦力，3M 胶只作为辅助防滑，不作为承重粘接结构
- fit result：该边界内已实测可用

证据边界：

- 这些记录支持“末端折弯位置周长 <=18 cm 的 S-01 non-diverter spout 可通过扎带 + 3M 贴挂钩模拟挂位”
- 不自动扩大为“所有 non-diverter spout 均支持”
- 仍需补：每张图对应的实测周长、3M 贴挂钩安装照片、扎带孔位、挂钩是否位移、测试流速、是否漏水/溢流/绕流、重复注水周期稳定性

Raw：`raw/products/bathtub-filter/2026-06-17-s01-non-diverter-fit-evidence/`

---

## 2026-06-17 已实测可用样本：freestanding tub filler curved / special-shaped non-waterfall outlet

用户补充：**Freestanding tub filler，弧形管、异型管、非瀑布出水都可以用**。已实测 **2 kg 承重**。

![[raw/products/bathtub-filter/2026-06-17-freestanding-tub-filler-fit-evidence/01-freestanding-curved-tub-filler-strap-hook-fit-test.jpg]]

归类：

- fixture type：freestanding tub filler
- geometry：弧形管 / 异型管
- outlet type：非瀑布出水
- taxonomy：S-03 curved / gooseneck-like spout 的 freestanding tub filler 子场景
- accessory：附赠的5孔总长124mm，宽20mm的扎带 + 附赠 3M 贴挂钩
- load result：2 kg static load-bearing tested
- fit result：该子场景已实测可用

安装边界：

- 扎带只扎到倒数第二个孔时，常规可通过拉扯扎带完成安装。
- 扎到倒数第三个孔会更紧，但需要较大拉力组装，对女性用户不太友好，不宜作为默认安装要求。
- 扎带需要扎在距离出水嘴末端 **60 mm** 处；重力会拉扯扎带向下变形，如果太靠近末端会滑落。

证据边界：

- 这些记录支持“freestanding tub filler 中的弧形管 / 异型管 / 非瀑布出水可通过扎带 + 3M 贴挂钩方案安装，并已通过 2 kg 静态承重测试”
- 不自动扩大为“所有 freestanding tub filler 均支持”
- 不支持外推到 waterfall / 宽体片状出水 / wide-body decorative outlet
- 仍需补：动态注水、高流量冲击、是否溅水/绕流/溢流、重复注水周期后扎带变形和贴钩稳定性

Raw：`raw/products/bathtub-filter/2026-06-17-freestanding-tub-filler-fit-evidence/`

---

## Spout type taxonomy

这套分类基于 compatibility-engineering-breakpoints 页面识别出的 minimum tub-spout taxonomy。8 个类别是工程断点分析建议的最低区分粒度——实际实物记录和测试时可能需要细化。

| # | Spout type | Description | Diverter? | Attachment method | KES support status | Notes |
|---|---|---|---|---|---|---|
| S-01 | Straight non-diverter, stable underside / lip | 最常见的无提拉头喷嘴，底面或末端折弯位置可形成稳定支撑 | No | 附赠的5孔总长124mm，宽20mm的扎带 + 3M 贴挂钩模拟提拉头挂位 + 21 mm 扁硅胶挂带 | Circumference-bounded validated / broader S-01 test pending | 2026-06-17 用户补充：末端折弯位置周长 <=18 cm 已实测可用，常规约 15-17 cm；124mm 硅胶扎带可拉伸到 22 cm；主固定力来自硅胶扎带拉力和摩擦力，3M 胶仅辅助防滑；仍需记录扎带孔位、挂钩是否位移、动态注水和 20 次 fill-cycle 后稳定性 |
| S-02 | Straight spout with diverter knob | 顶部有换向拨杆（用于切换到 showerhead）的直型喷嘴；含 RV / mobile-home center-set / valve-diverter faucet 变体 | Yes | 中央圆孔套过提拉头 + 21 mm 扁硅胶挂带 | 2 RV / mobile-home sample groups validated / broader S-02 test pending | 2026-06-17 用户补充 Mobile Home RV Tub Shower Center-Set Faucet、RV Tub & Shower Faucet Valve Diverter 已实测可用；仍需测不同提拉头直径、硅胶拉伸疲劳、diverter 可操作性、居中稳定性和动态注水表现 |
| S-03 | Curved / gooseneck-like spout | 弯曲出水口，出水方向非水平向前；含 freestanding tub filler 弧形/异型管非瀑布出水子场景 | Varies | 3M 贴挂钩 + 附赠的5孔总长124mm，宽20mm的扎带 + 扁挂带 | Freestanding non-waterfall 2 kg load-bearing validated / broader S-03 test pending | 2026-06-17 用户补充：freestanding tub filler 弧形管、异型管、非瀑布出水已实测可用，2 kg 承重；扎带需扎在距离出水嘴末端 60 mm 处，默认扎倒数第二孔；主固定力来自硅胶扎带拉力和摩擦力，3M 胶仅辅助防滑；仍需验证动态注水、溅水/绕流、扎带长期变形和挂钩位移 |
| S-04 | Short-projection spout close to wall | 喷嘴出水口距离墙面较近，tile clearance 偏小 | Varies | 可使用 S-01/S-02 方案；40-60 mm 允许偏心安装 | GO if center-to-wall >=40 mm; >=60 mm is centered/aesthetic | 出水嘴中心到墙面 >=60 mm 可居中安装；40-60 mm 可偏心安装，功能可用但不完美/不美观；仍需验证动态注水、用户手部安装空间和视觉接受度 |
| S-05 | Wide-body decorative spout | 装饰型宽体喷嘴（常见于 modern / designer 浴室）| Varies | 可能使用贴挂钩，但不保证挂带居中 | High-risk conditional / likely exclude unless tested | 宽体表面会影响贴钩、挂带路径和居中；不应默认支持 |
| S-06 | Slip-fit spout with wobble / lower confidence | 套装固定（无螺纹），本体已有轻微松动 | Varies | 挂带无法消除 spout base wobble | Likely not-supported if wobble is visible | 即便挂住，spout 本体晃动仍会放大滤体摆动；应作为排除项测试 |
| S-07 | Threaded spout with varied outlet geometry | 螺纹固定（更稳固），但出水口方向或截面不统一 | Varies | 根据外形套用 S-01/S-02/S-03 方案 | Design-covered by subtype / test pending | threaded base 更稳，但仍取决于是否有提拉头、出水口截面和外形 |
| S-08 | Low-clearance / off-center install scenario | 出水嘴中心到墙面距离约 40-60 mm 的低间隙场景 | Varies | 允许滤体相对出水嘴偏移最多约 20 mm | GO with aesthetic compromise if center-to-wall >=40 mm | 60 mm 是居中美观线，不是功能限制；40-60 mm 可偏心使用，只是不完美/不美观；<40 mm 属理论极端，用户观察为实际浴缸嘴基本没有少于 40 mm |

---

## 2026-06-17 安装场景与 KES GO/NO-GO 矩阵

当前把美国浴缸出水嘴安装场景拆成 **8 类**。其中 S-07 是连接/底座稳定性维度，会和 S-01/S-02/S-03 的外形维度交叉；RV / mobile-home center-set 是 S-02 的子场景，不单独计算占比。

占比口径：下表为 **KES strategy proxy estimate**，用于 V1 适配范围和测试优先级，不是公开权威统计。S-03/S-04/S-07 与具体 OEM SKU、房龄、翻新程度会互相重叠，所以不能把所有比例机械相加为 100%。

先按客户会说出来的安装位置分层，再映射到工程 S 类：

| 客户口语 / 安装位置 | 工程映射 | 典型空间 | 估算占比 | KES status | 判定 |
|---|---|---|---|---|---|
| Wall-mounted tub spout / tub-shower combo spout | S-02 为主，叠加 S-04/S-07/S-08 | 美国主流家庭浴缸+淋浴一体 | ~55-65% 目标安装场景 | GO / GO（偏心） | 带提拉分水器时 GO；出水嘴中心到墙面 >=60 mm 可居中安装，40-60 mm 可偏心安装但不完美/不美观；本体晃动时 NO-GO |
| Wall-mounted tub spout / tub-only non-diverter | S-01，部分 S-07 | 纯浴缸、酒店、公寓、部分 RV | ~10-15% | GO | 末端折弯位置周长 <=18 cm 时 GO；>22 cm 或无贴钩/扎带路径时 NO-GO |
| RV / mobile-home tub shower center-set faucet | S-02 子场景 | 房车、mobile home、轻量化塑料或金属 center-set faucet | S-02 内部子集，不单独累加 | GO | 已有 2 组样本实测可用；仍按提拉头直径、墙距、动态注水复核 |
| Deck-mounted widespread / Roman tub faucet | 多数落入 S-03 或 S-05，少量可按 S-01/S-07 判断 | 独立浴缸、主卧浴室、翻新浴室 | ~8-12% | GO（条件）/ NO-GO | 圆弧或常规窄 spout 可用 3M 贴挂钩 + 附赠的5孔总长124mm，宽20mm的扎带进入条件 GO；宽体/瀑布式默认 NO-GO |
| Freestanding tub filler | S-03（弧形/异型管/非瀑布）或 S-05（瀑布/宽体） | 独立浴缸、现代高端浴室 | ~3-5% | GO（非瀑布）/ NO-GO（瀑布/宽体） | 弧形管、异型管、非瀑布出水可用；使用附赠的5孔总长124mm，宽20mm的扎带 + 3M 贴挂钩，扎带扎在距离出水嘴末端 60 mm 处；已测 2 kg 承重。瀑布口/宽体片状出水仍 NO-GO |
| Wide waterfall / decorative tub faucet | S-05 | 现代装饰型、宽体瀑布口 | ~5-10% | NO-GO（默认） | 水流是片状或宽面，挂带路径和滤体居中不可控；不应写入 V1 support |
| Aged loose slip-fit / low-clearance exception | S-06/S-08 | 老旧安装、维修质量不稳定、墙距不足 | ~5-10% | S-06 NO-GO；S-08 GO（偏心） | 可见晃动直接 NO-GO；低墙距本身不是限制条件，>=40 mm 可偏心使用，40-60 mm 只是美观折中 |

场景划分：
- **主流家庭 tub+shower combo**：以 S-02 为核心，可能叠加 S-04 短出水或 S-07 threaded base。
- **纯浴缸 / 无提拉分水器**：以 S-01 为核心，依赖 3M 贴挂钩模拟挂位。
- **RV / mobile-home center-set**：归入 S-02 pull-up diverter 子场景，已有 2 组正向实测样本。
- **现代翻新 / 设计款浴室**：主要落在 S-03 curved / pull-down / freestanding non-waterfall，或 S-05 wide-body decorative / waterfall。
- **老旧或维修风险场景**：主要落在 S-06 wobble slip-fit；S-08 low-clearance 现在按偏心美观场景处理，不再按墙距不足直接排除。

| 场景ID | 龙头 / 出水嘴场景 | 典型空间 | 估算占比 | KES status | GO / NO-GO 判定条件 | 当前证据 |
|---|---|---|---|---|---|---|
| S-02 | Straight spout with pull-up diverter knob，包括 RV / mobile-home center-set / valve-diverter 变体 | 主流 tub+shower combo、家庭浴室、RV / mobile-home | ~35-45% | GO | 中央圆孔可套过提拉头；21 mm 扁硅胶挂带可让滤体中心线对准出水口；>=60 mm 可居中安装，40-60 mm 可偏心安装；spout 本体无明显松动 | 已有 2 组 RV / mobile-home center-set / valve-diverter 样本正向通过；仍需补不同提拉头直径和动态注水记录 |
| S-01 | Straight non-diverter, stable underside / lip | 纯浴缸、无 shower 切换结构、部分酒店/公寓/RV 场景 | ~10-15% | GO | 末端折弯位置周长 <=18 cm；常规 15-17 cm；附赠的5孔总长124mm，宽20mm的扎带 + 3M 贴挂钩可模拟 diverter 挂位；124mm 硅胶扎带可拉伸到 22 cm | 用户补充 S-01 已实测可用；仍需补每个样本的实测周长、贴钩照片和重复注水稳定性 |
| S-07 | Threaded / IPS stable base with varied outlet geometry | 主流 OEM 替换件、较稳固的旧房/翻新浴室 | ~15-20% | GO（按子类型） | threaded base 本身是正向因素；若外形落入 S-01 或 S-02，按对应 GO 条件执行；若落入 S-03，则按 S-03 条件执行 | 当前是结构判断，未形成独立全量实测；不应单独写成 universal fit |
| S-04 | Short-projection / close-to-wall spout | 老建筑、城市公寓、墙面瓷砖较厚或 spout 较短的浴室 | ~10-15% | GO / GO（偏心） | 出水嘴中心到墙面距离 >=60 mm 时居中 GO；40-60 mm 时偏心 GO，功能可用但不完美/不美观；还需确认用户手部安装空间、动态注水和视觉接受度 | 60 mm 是居中美观线；偏心最多约 20 mm，因此 40 mm 是当前实际可用下限；用户观察为浴缸嘴基本没有少于 40 mm |
| S-03 | Curved / gooseneck-like / pull-down diverter / freestanding non-waterfall spout | 现代翻新浴室、弧面出水嘴、非标准水流方向、独立浴缸 | ~10-15% | GO（条件）/ NO-GO | 弧面可通过 3M 贴挂钩 + 附赠的5孔总长124mm，宽20mm的扎带固定，且水流能居中进入滤体时为 GO（条件）；freestanding 弧形管/异型管/非瀑布出水已实测可用，扎带需扎在距离出水嘴末端 60 mm 处；若曲面导致贴钩滑移、滤体偏心、水流打到滤体侧壁或为瀑布片状出水，则 NO-GO | freestanding 非瀑布出水已有 2 kg 承重正向记录；其他 S-03 仍缺动态注水记录 |
| S-05 | Wide-body decorative / oversized designer spout | 高端或装饰型 modern 浴室 | ~5-10% | NO-GO（默认） | 宽体外形会让贴钩位置、挂带路径和滤体居中不可控；除非单独实测通过，否则 V1 不承诺适配 | 当前无正向实测；应作为排除或个案确认场景 |
| S-06 | Slip-fit spout with visible wobble / loose setscrew | 老旧 CC / slip-fit 安装、租房维修质量不稳定场景 | ~5-10% | NO-GO | KES 挂带无法消除 spout base wobble；水流冲击会放大滤体摆动和偏心，容易触发漏水/绕流/脱落投诉 | 结构性排除判断；即使外形可挂，也不应承诺支持 |
| S-08 | Low-clearance / off-center install scenario | 出水嘴中心到墙面约 40-60 mm 的低墙距场景 | ~3-5% | GO（偏心） | 40-60 mm 不是限制条件，偏心最多约 20 mm 后仍可用，只是不完全居中/不完美美观；<40 mm 作为理论极端记录，不作为当前主动限制 | 旧版 60 mm 是居中美观线而非硬边界；用户观察为实际浴缸嘴基本没有少于 40 mm |

规则摘要：
- **直接 GO**：S-01 末端折弯位置周长 <=18 cm；S-02 pull-up diverter，包括已测 RV / mobile-home center-set / valve-diverter 样本；S-07 中可明确归入 S-01/S-02 的稳定 threaded 场景。
- **GO（条件）**：S-03 弧面/异形但贴钩 + 扎带可稳定固定且水流居中；freestanding tub filler 弧形管/异型管/非瀑布出水，且扎带位于距离出水嘴末端 60 mm 处；S-04/S-08 中出水嘴中心到墙面距离 40-60 mm 的偏心安装。
- **直接 NO-GO**：spout 本体可见晃动；S-05 wide-body decorative 未单独实测；S-01 末端折弯位置周长 >22 cm 或没有稳定贴钩/扎带路径。出水嘴中心到墙面 <40 mm 目前按理论极端记录，不作为常规浴缸嘴限制条件。

---

## Failure mode by type

Based on the installation risk matrix and compatibility engineering breakpoints. This table maps which spout types are structurally likely to trigger which failure modes. All entries are **pre-test hypotheses**, not confirmed observations.

| # | Spout type | Bypass flow risk | Top overflow risk | Seam / housing leak risk | Retention failure risk | Notes |
|---|---|---|---|---|---|---|
| S-01 | Straight non-diverter, stable | Low | Medium | Low | Low | Best candidate; still needs overflow discipline at high flow |
| S-02 | Straight with diverter knob | Low–medium | Medium | Low | Medium | Diverter knob may create misalignment and partial bypass |
| S-03 | Curved / gooseneck | Medium-high | Medium | Medium | Medium | Freestanding non-waterfall sub-scenario has 2 kg load-bearing positive evidence; water path, splash, bypass and repeat-fill behavior still need dynamic testing |
| S-04 | Short-projection / close to wall | Medium | Low–medium | Medium | Medium | >=60 mm gives centered/aesthetic install; 40-60 mm is usable with up to ~20 mm offset, but needs splash/bypass and visual-acceptance testing |
| S-05 | Wide-body decorative | Medium | Medium | High | High | Clamp may not seat properly; seam stress if over-tightened |
| S-06 | Slip-fit with wobble | High | Medium | Medium | Very high | Wobble propagates to entire filter assembly during fill |
| S-07 | Threaded, varied outlet | Low–medium | Medium | Low | Low | Best retention of threaded types; outlet variation is primary variable |
| S-08 | Low-clearance / off-center install | Medium | Medium | Medium | Medium | 60 mm is not a hard support boundary; 40-60 mm can be used off-center, while <40 mm is a theoretical edge case not expected in normal bathtub spouts |

---

## 2026-04-17 公开 SKU 目录补充（pre-test 推断，非物理验证）

下表把 S-01 ~ S-08 与三大美国主流 OEM（Delta / Moen / Kohler）的实际 SKU 类别 + 美国家庭安装比例做对照——**用于 WS2 物理采样优先级排序**，不替代物理测试。

### 主流 OEM 双 connection 体系

行业标准（Delta / Moen / Kohler 通用）：
- **CC / Slip-Fit**：1/2" 铜管 + 5/32" hex 螺丝固定。底部有 setscrew 孔 → 可识别。
- **IPS / Threaded NPT**：1/2" male 螺纹，无 setscrew，底部无孔 → 可识别。

外形看几乎相同，**安装机制完全不同**——KES retention 设计必须同时考虑两种 base。

### 美国家庭基准比例（公开行业资讯）

- **~60% 美国家庭是 tub+shower combo 装置**——意味着多数 KES 目标用户的 spout 是带 diverter 的 tub spout（不是纯 tub-only）
- **T-diverter（pull-up knob）是最常见的 diverter 形态**——意味着 **S-02（带 diverter knob 的直型喷嘴）是物理采样的最高优先级**

### S-01 ~ S-08 × OEM SKU 对照

| Taxonomy ID | OEM 对应类型 | 代表 SKU | 美国安装比例（推断）| WS2 采样优先级 |
|---|---|---|---|---|
| **S-01** Straight non-diverter, stable | Delta / Moen / Kohler 单浴缸（无 shower）型 | 较少独立列产品（多在 deck-mount 系列）| ~10–15% | 🥈 中（基础对照样本）|
| **S-02** Straight + diverter knob | **T-diverter pull-up**：Moen 3801 / 3931, Delta U1075-PK, Kohler GP85556-CP | ~35–45% | 🥇 **最高** — 必采 |
| **S-03** Curved / gooseneck | Pull-down diverter (Delta RP17453, RP5836)、modern designer 系列 | ~10–15% | 🥇 高 — Sprite 评论显示这是 retention failure 高发型 |
| **S-04** Short-projection / 距墙近 | 老建筑常见、城市公寓常见 | ~10–15% | 🥈 中（高 fail risk，但小众）|
| **S-05** Wide-body decorative | Kohler Forte / Artifacts、Delta Cassidy 等高端线 | ~5–10% | 🥉 低（高端用户少 + KES 价位错位） |
| **S-06** Slip-fit + wobble | 老 setscrew 已松动的 CC connection | ~5–10%（年代相关）| 🥉 低（即便 KES 兼容也是 tenant complaint trap） |
| **S-07** Threaded + outlet 形状不一 | IPS NPT + 各种 outlet | ~15–20% | 🥇 高（Threaded 更稳，是 KES 主推目标） |
| **S-08** Low-clearance / 间隙极小 | 极老/特殊定制 | ~3–5% | 40-60 mm 可偏心使用；>=60 mm 居中更美观；<40 mm 为理论极端 |

> 比例为 KES strategy 推断，基于"60% US 家庭是 combo + T-diverter 最常见"+ Delta/Moen/Kohler 三家主流市场份额（合计 >70% 主流 plumbing supply）。**真实数字必须从 NAHB / US Census housing characteristics 数据交叉核实**。

### 后续实测/记录最小覆盖集

按上表，KES V1 最小化实测/记录覆盖集（目标覆盖 ~80% 美国 tub spout 安装场景）：

```
必补记录（V1 fit scope 决定）：
  S-02   Moen 3801 (slip-fit)         ← T-diverter 主流
  S-02   Moen 3931 (slip-fit, 5.5")   ← T-diverter 短款
  S-02   Delta U1075-PK (slip-fit)    ← T-diverter Delta 主线
  S-07   Kohler GP85556-CP (slip-fit) ← Kohler T-diverter
  S-03   Delta RP17453 (slip-fit)     ← Pull-down diverter (curved)
  S-03   Delta RP5836                  ← Pull-down diverter
  S-01   Moen 单浴缸非 diverter        ← 基础对照
  S-04   Generic 短 projection (老建筑) ← 高 fail risk 验证

可选：
  S-05   Kohler Forte K-10281-4       ← 高端 wide-body
  S-06   Old slip-fit (used)          ← wobble 验证
```

这里不是样品采购清单；如果已有样品、图片、人工安装记录或测试视频，应优先把对应参数和结果补入本页。

### KES V1 fit scope 推断（按当前设计方案）

基于上面的安装场景矩阵，**KES V1 推荐 fit scope 起手包**（后续由更多实物和动态注水记录覆写）：

- **GO**：S-01（末端折弯位置周长 <=18 cm）、S-02（pull-up diverter；含已测 RV / mobile-home center-set / valve-diverter 样本）、S-03 中 freestanding tub filler 弧形管/异型管/非瀑布出水（扎带距离出水嘴末端 60 mm，2 kg 承重已测）、S-07 中可明确归入 S-01/S-02 的稳定 threaded 场景。
- **GO（条件）**：S-03 其他弧面/异形场景（3M 贴挂钩 + 附赠的5孔总长124mm，宽20mm的扎带能稳定固定且水流居中）、S-04/S-08 中出水嘴中心到墙面距离 40-60 mm 的偏心安装场景。
- **NO-GO**：S-06 visible wobble；S-05 wide-body decorative 未单独实测；S-01 末端折弯位置周长 >22 cm 或无稳定贴钩/扎带路径。出水嘴中心到墙面 <40 mm 仅作为理论极端记录。

这意味着 KES V1 的 marketing 应该写：

> "Designed for standard tub spouts with pull-up diverters, stable non-diverter spouts when the terminal bend circumference is 18 cm or less, and curved or special-shaped freestanding tub fillers with non-waterfall outlets when secured about 60 mm from the outlet end using the included 3M hook and silicone tie. Close-to-wall tub spouts can be used off-center when the outlet center is about 40-60 mm from the wall, though the appearance may be less centered. Not designed for loose/wobbly slip-fit spouts or waterfall/wide-body decorative outlets unless fit-confirmed."

不写 "fits most tubs"——那是 Sprite/Crystal Quest 翻车的原因。

## 竞品安装方式分布（2026-04-18 LLM 分类，2026-06-03 修正）

> 来源：`kes-ops-platform` report 04-18 dimension_matrix，LLM 基于 title + bullet point 标注。可能有误分；详见 `raw/llm_clustering_result.json`。2026-06-03 修正：Filterbaby 已拆到 shower-filter 项目，不再计入 bathtub active competitor set。

| installation_type | ASIN 数 | 月销合计（US）| 均价（US）| 代表品牌 |
|---|---|---|---|---|
| `velcro_strap` | 1 | 1K+ | $16 | JYFJYF（最低价 entry）|
| `faucet_mount` | 1 | 500+ | **$89** | Canopy |
| `overflow_integrated` | 3 | 2K+ | $21 | SHLLKTTRY / Yolycen |
| `ball_style` | 1 | 500+ | $65 | Crystal Quest |
| `other` | 6 | 4K+ | $41 | Santevia / Beati Faucet / Tubo |

**对 KES V1 fit scope 的含义：**

1. **faucet_mount 当前 active bathtub 样本只剩 Canopy。** Canopy 的 $89 仍证明 premium tub-spout-cover 路线存在，但不能再用 Filterbaby 的 shower inline 数据来抬高 bathtub faucet_mount 均价。

2. **overflow_integrated（嵌入溢水口）= 最低价**（均价 $21），主要是中国白牌 SHLLKTTRY / Yolycen——这是 Cluster 1 白牌的主要形态，KES 应避开（价格信号错误）。

3. **velcro_strap（魔术贴固定）**是入门价位（$16）的独特形态——安装最简单，但固定稳定性可能是隐患（对应 S-06 retention failure 风险）。

4. **ball_style（悬挂球）= $65 小众高价**，Crystal Quest 独占，对应 KES taxonomy 中的离散附件形态——不与 KES V1 spout-mount 路线直接竞争。

**与 active 10 ASIN 公开资料和实物记录的关联：**
- Canopy 对应 premium tub-spout 公开竞品线索；Filterbaby 是 showerhead filter，已迁出到 shower-filter 项目，不作为 tub-spout fit benchmark
- overflow_integrated（SHLLKTTRY）安装在溢水口而非出水口——与 KES S-01~S-07 的 spout-mount 路线是完全不同的安装点，不存在直接兼容冲突

## Next steps to complete this page

在进行 Workstream 2（公开竞品资料补全）和 Workstream 3（验证测试准备）期间，按以下顺序完成本页：

- **Step 1 — 建立 spout taxonomy 与已有实物记录：** 如已有 spout 或竞品记录，优先覆盖 S-01、S-02、S-03 作为最高优先级（最常见 + 最有分歧）；不把采购列为本轮任务
- **Step 2 — 拍摄与记录：** 对每类 spout 拍照，记录外径、出水口截面、底面几何、diverter 位置、距墙间距等关键参数
- **Step 3 — 适配测试：** 仅在已有实物或人工记录时进行 attachment fit test；记录是否需要 workaround
- **Step 4 — 动态注水测试：** 在真实 fill 条件下测试 retention stability、overflow behavior、bypass evidence；参考 validation-testing-protocol
- **Step 5 — 更新 KES support status 列：** 将每行的 "TBD" 替换为 "supported" / "conditional (with constraint)" / "not supported (exclude from V1 scope)"
- **Step 6 — 标记 V1 scope boundary：** 识别出哪些 spout type 将被明确纳入 KES V1 产品支持范围，哪些将在产品页上明确注明"不在支持范围内"
- **Step 7 — 同步更新 decision-register：** 关闭 D-02（supported spout types decision）

---

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-compatibility-engineering-breakpoints]]
- [[bathtub-filter-installation-risk-matrix-v2]]
- [[bathtub-filter-test-gating-checklist-for-kes]]
- [[bathtub-filter-kes-next-step-execution-plan-v1]]
- [[bathtub-filter-decision-register]]
- [[bathtub-filter-kes-rd-and-validation-roadmap]]
- [[bathtub-filter-normal-flow-vs-reduced-flow-evidence-table]]
- [[bathtub-filter-kes-flat-strap-spout-fit-design-2026-06-03]]
