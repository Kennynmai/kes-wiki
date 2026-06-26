---
type: product
status: draft
owner: strategy
created: 2026-04-19
updated: 2026-04-20
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, media-stack, product-architecture, free-chlorine, chloramine, well-water]
source_count: 9
review_cycle: monthly
verification_status: spot-checked
related:
  - ./bathtub-filter-kes-concept-brief-v1.md
  - ./bathtub-filter-product-definition-language.md
  - ./bathtub-filter-technology-notes.md
  - ./bathtub-filter-chloramine-media-research.md
  - ./bathtub-filter-well-water-research.md
  - ./bathtub-filter-claim-register.md
---

# 浴缸过滤器按水源类型的滤材方案

## 为什么有这页
在 KES 当前产品定义下，bathtub filter 不是“全能净水器”，而是：

> **浴缸注水场景的末端减害 / bath-water comfort 模块**

因此，不同水源类型不应被塞进一个万能 media stack，而应拆成不同 SKU 路线。

本页把当前最可讨论的三套方案整理成统一格式：

1. **游离氯城市**
2. **氯胺城市**
3. **私人井水**

---

## 先讲总原则

### KES 当前统一产品定义

三套方案都必须遵守同一条定义边界：

- 不是全功能净水器
- 不以降 TDS 为目标
- 不承诺 broad-contaminant removal
- 不做 eczema / baby-safe / clinical outcome 语言
- 以 **bath-fill 场景的真实水感改善与已知问题负荷降低** 为核心

新增边界（2026-04-20）：

- **不把阻垢剂 / 阻垢条当作“软化水”滤材**
- **不把 antiscale rate 翻译成 hardness reduction**
- 若未来试验阻垢陶瓷，只能作为 `anti-scale adjunct`，不能侵占主力去游离氯媒体的逻辑空间

### 为什么必须拆成三套

因为这三类水的主问题完全不同：

- **游离氯城市**：主要是 free chlorine
- **氯胺城市**：主要是一氯胺，媒体和接触时间要求都不同
- **井水**：通常没有加氯，核心变成铁、硫化氢、沉积物、气味

把这三类问题强行压进一个 compact cartridge，最后大概率只会得到：

- proof 不够
- claim 边界失控
- 用户买错 SKU

---

## 方案 A — 游离氯城市：Version A 主线

### 适用水源

- US urban municipal tap water
- 龙头端主问题是 **free chlorine**
- 不以氯胺为主

### 推荐媒体栈

**PP cotton → KDF55 → CaSO3**

按当前 Version A 的已确认架构，核心配比可继续沿用：

- **PP cotton**
- **KDF55 110 g**
- **CaSO3 130 g**
- **导流模块**

### 各层职责

| 层 | 角色 | 备注 |
|---|---|---|
| PP cotton | 截留颗粒 / 稳定水路 | 不是主 KPI |
| KDF55 | 末端安心层 / 生物膜抑制层 / 寿命稳定层 | 不再当主力去游离氯层 |
| CaSO3 | **主力去游离氯 KPI** | 当前 Version A 的主 KPI 所在层 |

### 这套为什么成立

- 与当前 KES 已确认定义最一致
- 已有内部 EBCT、life model、system-total dechlorination 数据
- claim architecture 已经最清晰

### 可守住的主叙事

- `free chlorine reduction`
- `bath-water comfort`
- `less pool-smell bath fill`

### 不应承诺

- chloramine removal
- hard-water softening
- well-water treatment

### KES 判断

这是 **当前最成熟、最应该先做的主 SKU**。

---

## 方案 B — 氯胺城市：inline 媒体 + 浴缸浸泡配件双段路线

### 适用水源

- 龙头端主问题是 **monochloramine（NH2Cl）**
- 面向 chloramine-city 用户

### 推荐结构

这条路线不建议只靠 inline cartridge。
在当前证据下，更可守住的是 **双段方案**：

1. **inline bath-spout filter**
2. **浴缸内浸泡配件**（维生素 C / 抗坏血酸钠）

### 推荐媒体栈

**PP cotton → catalytic activated carbon → small KDF55 safety layer**

配合：

**drop-in bath accessory: sodium ascorbate / vitamin C soak puck, tablet, or mesh pod**

### 各层职责

| 组件 | 角色 | 备注 |
|---|---|---|
| PP cotton | 基础颗粒控制 / 稳定水路 | 非主 KPI |
| Catalytic activated carbon | **主力 inline chloramine reduction** | 必要但未必充分 |
| KDF55 小层 | free chlorine residual / media-stability / familiar credibility anchor | 不承担 chloramine 主 KPI |
| Sodium ascorbate / vitamin C 浸泡配件 | **在浴缸停留阶段完成 chloramine neutralization** | 利用 4–8 分钟接触时间 |

### 为什么要做成双段

当前证据下，单靠 compact inline cartridge 处理氯胺的问题在于：

- 催化活性炭是最可信的固态路线
- 但 normal bath-fill flow 下，**EBCT 往往还是不够宽裕**
- 浴缸 format 的真正结构优势，是水会在缸里停留几分钟

所以最稳的 KES 方案不是“假装 inline 一步搞定”，而是：

> **inline 先降一部分 + 浴缸内浸泡配件完成反应**

### 为什么优先推荐抗坏血酸钠

用户已接受“可额外放入浴缸浸泡配件”的前提下，**抗坏血酸钠**比抗坏血酸更适合作为默认候选：

- 反应路径相同
- 更接近中性，不会像纯 vitamin C 那样更容易拉低局部 pH
- 更符合 bath comfort 叙事

### 可守住的主叙事

- `for chloramine-city bathers`
- `inline reduction + in-tub completion`
- `reduces combined chlorine during fill and soak`

### 不应承诺

- “单靠滤芯即可 fully remove chloramine”
- “compact cartridge handles chloramine everywhere”
- “NSF 177 supports chloramine claim”

### KES 判断

这条是 **Version B 的最可信方向**。
如果 KES 要进 chloramine 市场，优先做这条，不建议做 KDF/CaSO3 的硬外推版本。

---

## 方案 C — 私人井水：低到中等铁 / 硫化氢 comfort 路线

### 适用水源

- private well households
- 主要 bath pain points 是：
  - 铁锈色 / staining
  - metallic smell
  - hydrogen sulfide（臭鸡蛋味）
  - 部分颗粒物

### 推荐媒体栈

**coarse PP sediment layer → KDF85 → catalytic activated carbon → outlet mesh**

必要时可保留一层细 PP 做后端拦截，但主栈应围绕上面三层。

### 各层职责

| 层 | 角色 | 备注 |
|---|---|---|
| Coarse PP / sediment layer | 先截留颗粒 / 锈渣 | 减少主媒体过快堵塞 |
| KDF85 | **主力针对低到中等铁、H2S、部分锰的 well-water 媒体** | well-water 主 KPI 所在层 |
| Catalytic activated carbon | 气味 polish / organics polish / well-water sensory finish | 不是 chlorine-city 逻辑，而是 odor/polish 逻辑 |

### 为什么不是 KDF55 + CaSO3

因为井水通常：

- **没有 free chlorine**
- 也没有 chloramine 作为主问题

所以 municipal SKU 的核心媒体在这里会错位：

- **CaSO3**：失去主要任务
- **KDF55**：不再是最 relevant 的主媒体

井水 bath-comfort 路线应该换成 **KDF85 主导**。

### 明确边界

这条路线只能诚实覆盖：

- **低到中等铁 / 硫化氢 / 气味问题**

不能把它包装成：

- bacteria treatment
- arsenic / nitrate / uranium solution
- high-iron whole-house replacement
- hardness softener

### 建议适用门槛

如果 KES 做这条 SKU，建议在定位上明确：

- 仅面向 **low-to-moderate iron / sulfur odor**
- **高铁（约 >2–3 ppm）** 不建议用 compact bath filter 解决

### 可守住的主叙事

- `for low-to-moderate well-water odor and rust discomfort`
- `targets iron / sulfur-related bath nuisance`
- `bath fixture staining and odor relief framing`

### KES 判断

这是 **Version C / well-water line**，但它不应被当成 Version A 的延伸，而应视为另一条功能逻辑不同的 SKU。

---

## 三套方案对比表

| 方案 | 目标水源 | 主媒体 | 关键辅助组件 | 主 KPI | 不解决什么 |
|---|---|---|---|---|---|
| A | 游离氯城市 | **CaSO3** | KDF55 + PP | free chlorine reduction | chloramine / hard-water softening / well-water issues |
| B | 氯胺城市 | **catalytic activated carbon** | 抗坏血酸钠/维生素 C 浸泡配件 + 小层 KDF55 | chloramine reduction during fill + soak | 不能假装单靠小滤芯全做完 |
| C | 私人井水 | **KDF85** | sediment layer + catalytic carbon | low-moderate iron / H2S / odor relief | bacteria / arsenic / nitrate / hard-water softening / high-iron treatment |

---

## 对 KES 的直接建议

### SKU 排序

如果按当前成熟度和产品定义一致性排序：

1. **方案 A — free chlorine municipal**
2. **方案 B — chloramine city dual-stage**
3. **方案 C — well-water nuisance route**

### 不建议的做法

- 不要把三条路线混成一个“universal bath filter”
- 不要为了 marketplace 关键词把 KDF55 / CaSO3 / KDF85 / catalytic carbon / vitamin C 全塞进一个小球
- 不要在 chlorine / chloramine / well-water 三类市场共用同一套文案

### 最稳的产品架构语言

最稳的说法不是：

> “我们有一个滤芯适合所有家庭”

而是：

> **KES 有同一产品定义下的三条水源适配路线：游离氯版、氯胺版、井水版。**

这样更接近真实工程，也更接近真实 claim discipline。

---

## 产品会速览表

下面这张表是给 KES 内部产品会直接使用的压缩版。

| SKU 路线 | 内部建议名 | 目标用户 | 主媒体栈 | 主 claim 方向 | 禁止 claim | 推荐验证测试 |
|---|---|---|---|---|---|---|
| A | **KES Bath Filter Free-Chlorine** | free-chlorine municipal bathers；希望减少 pool smell / chlorine discomfort 的家庭 | `PP cotton → KDF55 → CaSO3` | `free chlorine reduction` / `bath-water comfort` / `less pool-smell bath fill` | chloramine removal / hard-water softening / broad contaminant removal / well-water treatment | DPD free chlorine in/out；15/20/25/30 L/min curve；寿命曲线；overflow / leak / fit test |
| B | **KES Bath Filter Chloramine + Soak Kit** | chloramine-city bathers；已知自己所在城市使用 chloramine、且愿意接受额外 bath accessory 的用户 | `PP cotton → catalytic carbon → small KDF55` + `sodium ascorbate soak accessory` | `reduces combined chlorine during fill and soak` / `chloramine-city bath-water comfort` | single-cartridge full chloramine removal / NSF 177 chloramine implication / universal chloramine claim without soak step | total chlorine / monochloramine in/out；with-vs-without soak accessory；不同 fill time 验证；温水 38–42°C 条件测试；用户操作可理解性测试 |
| C | **KES Bath Filter Well-Water Nuisance** | private well households with low-to-moderate iron / sulfur smell / rust nuisance | `coarse PP sediment → KDF85 → catalytic carbon` | `targets iron / sulfur-related bath nuisance` / `odor and rust discomfort relief framing` | bacteria treatment / arsenic / nitrate / uranium / high-iron replacement for whole-house / hard-water softening | iron / H2S / manganese challenge test；sediment loading / clogging test；pressure-drop life test；staining / odor panel validation |

---

## 每套 SKU 的会议口径

### SKU A — KES Bath Filter Free-Chlorine

### 适合怎么讲

- KES 当前主线 SKU
- 最接近已验证状态
- 适合先 launch、先 build trust

### 会议里应盯住的决策点

- Version A 是否保持当前配比不变
- 是否先做 third-party free-chlorine test 替代内部 bench evidence
- 是否把 chlorine strip 作为固定 pack-in

### 进入下一阶段前至少要过的测试

- **DPD 法 free chlorine reduction**
- **bath-fill flow envelope**
- **寿命与 replacement trigger**
- **supported spout compatibility**

---

### SKU B — KES Bath Filter Chloramine + Soak Kit

### 适合怎么讲

- 不是 Version A 文案外推
- 是单独的 chloramine-market SKU
- 真正差异点不只是滤材，而是 **两段式使用逻辑**

### 会议里应盯住的决策点

- 是否接受“滤芯 + 浸泡配件”双组件体验
- 默认使用 **抗坏血酸钠** 还是抗坏血酸
- soak accessory 的形态是 puck、tablet 还是 mesh pod
- 是否允许用户不放浸泡配件；如果允许，文案如何处理

### 进入下一阶段前至少要过的测试

- **monochloramine / total chlorine reduction with soak step**
- **inline-only vs. inline+soak 对比**
- **不同注水时长 / 浴缸体积下的完成度**
- **用户是否理解“需要把配件放进浴缸”**

---

### SKU C — KES Bath Filter Well-Water Nuisance

### 适合怎么讲

- 不是净化井水的全屋替代品
- 是 low-to-moderate nuisance problem 的 bath-comfort SKU
- 重点是 smell、stain、rust discomfort，不是 health-grade remediation

### 会议里应盯住的决策点

- KDF85 供应与粒径是否稳定
- 井水 SKU 是否需要更粗的前置沉积层
- 高铁 / 高硫用户如何在前端就被排除，避免买错
- 零售 / 农村渠道 vs. DTC 的渠道差异

### 进入下一阶段前至少要过的测试

- **iron / sulfur odor / manganese challenge testing**
- **pressure-drop and clogging under sediment load**
- **低到中等铁阈值界定**
- **明确“超过某阈值不推荐”的 fail boundary**

---

## 会议建议的决策顺序

如果 KES 要开产品会，建议按下面顺序做决定：

1. **先确认是否接受三 SKU 框架**
   - 不要再讨论“一个滤芯通吃三种水”
2. **先锁定 SKU A 继续推进**
   - 它是最成熟、最接近现有证据与定义边界的
3. **再决定 SKU B 是否值得立项**
   - 关键不是 chemistry，而是用户是否接受 soak accessory
4. **最后决定 SKU C 是否进入独立路线**
   - 它更像新市场 / 新渠道 / 新 claim boundary，不应混进 Version A 节奏

---

## 需要补的管理动作

为了让这三套方案真正可推进，下一轮 wiki 最值得补的是三个配套页：

1. **SKU-level claim register**
   - 把 A/B/C 的 allowed / conditional / banned wording 分开
2. **SKU-level validation checklist**
   - 把每条路线必须过的 bench / user / compatibility test 单独列出
3. **SKU-level front-end qualification logic**
   - 让用户先判断自己是 free chlorine、chloramine 还是 well-water，避免买错

---

## Sources

- [Bathtub Filter KES Concept Brief — V1](./bathtub-filter-kes-concept-brief-v1.md)
- [Bathtub Filter 产品定义语言](./bathtub-filter-product-definition-language.md)
- [Bathtub Filter 技术说明](./bathtub-filter-technology-notes.md)
- [Chloramine media research](./bathtub-filter-chloramine-media-research.md)
- [Private well water research](./bathtub-filter-well-water-research.md)
- [Claim register](./bathtub-filter-claim-register.md)
- [Disinfectant types and media guide](./bathtub-filter-disinfectant-types-and-media-guide.md)
- [KES 产品架构假设 → 确认 log](./bathtub-filter-kes-product-architecture-hypotheses.md)
