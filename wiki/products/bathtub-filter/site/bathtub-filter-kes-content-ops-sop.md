---
type: product
status: draft
owner: strategy
created: 2026-07-02
updated: 2026-07-02
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, content-ops, sop, governance, claims, evidence, workflow, onboarding]
source_count: 4
review_cycle: monthly
verification_status: spot-checked
related:
  - ./bathtub-filter-kes-marketing-site-content-map.md
  - ../bathtub-filter-claim-register.md
  - ../bathtub-filter-evidence-bibliography.md
  - ../bathtub-filter-media-efficacy-at-bath-conditions.md
---

# KES 浴缸过滤器 · 内容运维 SOP（Content-Ops Standard Operating Procedure）

> 本页把 [内容地图（MAP）](./bathtub-filter-kes-marketing-site-content-map.md) §一（治理原则）和 §四（导航/单一真理源）里的**原则**落成可执行**流程**，目标是让新同事不依赖口头传承就能独立接手加页、清 claim、改数字、跑月度巡检。
>
> **上下位关系**：MAP 是"施工蓝图 + 页面清单 + claim 区归属"；本 SOP 是"施工队作业手册"。MAP 说*建什么*，本页说*怎么建、怎么验、怎么维护*。两页冲突时以 MAP 的 claim 区归属和 §四单一真理源规则为准。

---

## 0. 谁读这页

- **新写手/新编辑**：从 §1 加页流程开始。
- **claim 审批人（产品/法务）**：看 §2 审批链。
- **证据 owner（产品/研究）**：看 §3 🟡→🟢 销项流程。
- **改配比/改数字的人（产品/工程）**：看 §4 数字改动传播 checklist——**任何改真理源数字前必读**。
- **月度巡检 owner**：看 §5。

---

## 1. 新页怎么加

### 1.1 建页六步

1. **定归属**：先去 MAP §二"页面索引"和 §三"页面清单"确认这页属于哪一簇（T/M/S/D/E/P/SVC）、归哪个 claim 区、真理源指向谁。**MAP 里没有的页不要凭空建**——先在 MAP 加一行再建页，保持索引是唯一目录。
2. **拷模板**：用 §1.2 frontmatter 模板 + §1.3 正文骨架起页。
3. **填五段**（场景/滤材页按 §1.3 结构）。
4. **挂 claim 标签**：每条对外 claim 就地标 🟢/🟡/🔴（见 §1.4）。
5. **过必带项 checklist**（§1.5）——**缺一项不许 ship**。
6. **进索引 + 建反链**：回 MAP 页面索引补硬链接；被引用的真理源页（M/T 页）底部补"用到我的页"反链。

### 1.2 Frontmatter 字段表

所有 site/ 内容页统一用下表字段（照 [MAP](./bathtub-filter-kes-marketing-site-content-map.md) 与既有滤材页对齐）：

| 字段 | 含义 | 取值约定 |
|---|---|---|
| `type` | 文档大类 | 内容页固定 `product` |
| `status` | 生命周期 | `draft` / `active`；未定稿一律 `draft` |
| `owner` | 责任簇 | `strategy` / `product` / `research`（谁维护这页口径） |
| `created` / `updated` | 建/改日期 | ISO `YYYY-MM-DD`；**任何实质改动必 bump `updated`**（见 §4） |
| `visibility` | 可见范围 | `team`（内部）/ `public`（可对外表面） |
| `confidence` | 内容置信 | `high` / `medium` / `low` |
| `officiality` | 官方度 | `draft`（草稿）/ `placeholder`（占位待业务补）/ `official`（已签发） |
| `domain` / `domains` | 主域 + 标签 | `domains` 带 `bathtub-filter, kes` + 本页主题词 |
| `source_count` | 引用来源数 | 整数，便于审计 |
| `review_cycle` | 巡检周期 | 内容页固定 `monthly`（喂 §5 月度巡检） |
| `verification_status` | 核验状态 | `spot-checked` / `verified` / `unverified` |
| `related` | 相邻页硬链接 | 相对路径；真理源页必列 |

### 1.3 正文结构

**场景页（S）/ 滤材页（M）固定五段**（照 MAP §三）：

```
① problem 框定（这页解决用户哪个 problem，不越界到别的水源路线）
② 用哪套 media 配置（真理源=对应 M 页；场景页只引用不改写口径）
③ 有界 claim（每条带 🟢🟡🔴 + 限定词，如 "free chlorine / fresh-filter / 15 L/min"）
④ 承重护栏 / disclaim（本页必带句，如 "This is not a water purifier."）
⑤ 诚实劝退（能力外明说不适合 + 留邮箱/引导）
```

**其它页型**：T/E/P 页按 MAP §三对应块的"内容/护栏"列展开；SVC 占位页保 `officiality: placeholder` 骨架，事实留 `[____]` 待业务补。

### 1.4 claim 标签口径

- 🟢 **坐实** — 有第三方/内部证据闭环，可上首屏、可对外承诺。
- 🟡 **待验证** — 有方向证据未闭环。**可写进 spec 页但必标黄、不上 Hub 首屏、不作对外承诺**。
- 🔴 **禁** — 见 [claim-register](../bathtub-filter-claim-register.md) Banned 区（eczema/baby-safe/软化/氯胺秒解/TDS 笔/toxin-panic/patented 等）。

### 1.5 必带项 checklist（缺一不 ship）

- [ ] **claim 表对齐**：本页每条对外 claim 能在 [claim-register](../bathtub-filter-claim-register.md) 找到对应行（Allowed/Conditional），且 §D 表面→claim 映射对得上。
- [ ] **承重护栏随行**：定位承重句 + 该 claim 区强制 disclaim（如软化行必带 "It does not soften your water."）。
- [ ] **MAP 反链**：本页已进 MAP 页面索引；引用的真理源页已回链本页。
- [ ] **进索引**：MAP §二对应簇列表里有本页硬链接。
- [ ] **单一真理源**：去氯数字引 T2、寿命引 T3、每种 media claim 引对应 M 页——**本页不自造口径**。
- [ ] **禁词自查**：跑 §5.2 禁词扫描零命中。

---

## 2. claim 审批链

任何对外 claim 上线前走这条链，**先查 Banned，再查 Conditional，最后 Allowed 也要核证据**（[claim-register](../bathtub-filter-claim-register.md) "How to use"）：

| 环节 | 谁 | 做什么 |
|---|---|---|
| **起草** | 写手/编辑 | 写出 claim + 限定词，标初判 🟢🟡🔴 |
| **对区** | 写手 | 对照 claim-register：命中 Banned→🔴 删；命中 Conditional→🟡 走证据；落 Allowed→仍核证据要求列 |
| **产品签** | 产品 owner | 核证据是否满足对应行 evidence requirement；🟡 是否已闭环可转 🟢 |
| **法务签（触发条件）** | 法务 | 命中下列**任一触发词/类**必须法务过： |
| **上线门** | 发布人 | 全部签完 + §1.5 checklist 全绿才 ship |

### 法务触发条件（命中任一即必过法务）

- **健康词**：eczema/湿疹、baby-safe、"更健康的皮肤/头发"、任何健康疗效暗示。
- **认证词**：NSF/ANSI「成品认证」措辞（料级 listing ≠ 成品认证，易读成成品认证的句子）、"certified for safety and performance" 类。
- **专利词**：升级 "Patent pending" 为 "patented/granted/专利技术/获专利/专利保护"（pending 非授权，🔴 禁）；据专利说明书宽 claim（软化/除重金属/UV）扩营销（🔴 禁）。
- **价格声称**：虚划线/scarcity/best-value/省 X%（让利逻辑须诚实、可核）。

---

## 3. 🟡 → 🟢 销项流程

每个 🟡 要转绿，**必须三项齐备**，缺一不翻绿：

1. **(a) 缺什么证据** — 明确写出闭环需要的那份数据/测试/文件。
2. **(b) 谁验证** — 指名 owner（产品/研究/工程/法务）。
3. **(c) 证据落到哪** — 收进 [evidence-bibliography](../bathtub-filter-evidence-bibliography.md) 拿到编号（现有条目按 ### 序号，如 #25 Peskin & Winterbourn），原始件归档到 `raw/products/bathtub-filter/`。

三项齐 → 把页内标签从 🟡 改 🟢 → 同步 claim-register 对应行 → bump 两页 `updated`。

### 两个实例

| 🟡 claim | (a) 缺什么证据 | (b) 谁验证 | (c) 证据落到哪 | 现状 |
|---|---|---|---|---|
| **25 L/min 去氯性能数字** | Gate 1 第三方 DPD 报告（25 L/min 最大通过流量下的实测去氯率） | 产品（Gate 1 台架） | 报告收 evidence-bibliography 新编号 + raw 归档；口径只在 [T2](./bathtub-filter-kes-page-how-we-test-and-certify.md) 落一次 | 🟡 待 Gate 1 DPD；性能口径仍回 15 L/min |
| **O 圈线径 / 挂带密封配合** | 生产规格实测（线径公差 + no-overflow 复核） | 工程 | 工程 spec 收 raw 归档，回填 [D4 挂带适配](./bathtub-filter-kes-structure-flat-strap-fit.md) | 🟡 待工程实测 |

---

## 4. 数字改动传播 checklist（防 claim 漂移的强制机制）

> **背景**：单一真理源规则（MAP §四）只在"真理源改动被逐页核销"时才成立。一处真理源数字改了、下游没跟，就是 claim 漂移。**任何改真理源数字的动作强制走本节六步。**

### 六步

1. **改真理源数字**：只在真理源页改（如 BOM 配比、T2 去氯数字、T3 寿命表）。
2. **grep 全站引用**：拿旧数字全仓搜，列出所有下游命中。
   `grep -rn "旧数字" wiki/products/bathtub-filter/`
3. **逐页核销**：每个命中要么改成新值，要么显式标注为"旧值对照/历史记录"（如页首裁定注）。
4. **bump `updated`**：每个动过的页 `updated` 改当天日期。
5. **复核 grep 零残留**：再 grep 一次旧数字，确认只剩"显式旧值对照"处，正文零残留。
6. **同步 claim-register**：若数字支撑某条 claim，回 claim-register 对应行同步。

### 案例：2026-07-02 BOM 裁定

BOM 表把滤料克数互换（KDF55 110g/CaSO₃ 130g → **KDF55 130g / CaSO₃ 110g**）。传播执行：

- 真理源 = [V1 BOM 表](../bathtub-filter-v1-free-chlorine-removal-dimensions-materials.md)。
- 下游核销：[efficacy §9](../bathtub-filter-media-efficacy-at-bath-conditions.md) 寿命模型缩放 3.25×→2.75×（总系数 2.925→2.475）、@2ppm/@1ppm 全表重算、推导行、L240 附注全部落实；同批把**误记 TPU 挂带**改为**硅胶（silicone）挂带**（concept-brief / PRD / claim-register Fit 行）。
- grep 复核：efficacy 正文旧值（3,481/17,672/…/2.925）零残留，仅页首裁定注保留"旧→新"对照记录。

### 真理源 → 下游映射表

| 真理源 | 数字/口径 | 下游页（改真理源必核这些） |
|---|---|---|
| **[V1 BOM 表](../bathtub-filter-v1-free-chlorine-removal-dimensions-materials.md)** | 配比/克数/挂带材质/尺寸 | efficacy §9/§9.5、[S1 游离氯场景](./bathtub-filter-kes-scenario-free-chlorine.md)、concept-brief、PRD、claim-register Fit 行、结构页 D1/D4 |
| **[T2 我们怎么测/认证](./bathtub-filter-kes-page-how-we-test-and-certify.md)** | 去氯数字 / 认证口径 / 15↔25 L/min | Hub、S1–S5 场景页、PDP、[E10 流速×去氯](./bathtub-filter-kes-edu-flow-rate-and-lifespan.md)、efficacy 引用处 |
| **[T3 更换/寿命](./bathtub-filter-kes-page-replacement-and-lifespan.md)** | 寿命表 / 更换触发 / 容量 | efficacy §9、[SVC4 补芯订阅](./bathtub-filter-kes-refill-subscription.md)、[P3 维护指南](./bathtub-filter-kes-care-and-maintenance-guide.md)、[SVC2 买后验证](./bathtub-filter-kes-post-purchase-verification.md) |
| **[E4 术语表](./bathtub-filter-kes-edu-water-glossary.md)** | 游离氯/总氯/氯胺/ppm/硬度/TDS 定义 | 全部 E 页、S1–S5 场景页、[SVC1 买前 FAQ](./bathtub-filter-kes-faq-is-kes-right-for-you.md)、[T1 自测页](./bathtub-filter-kes-page-water-test-diagnosis.md) |

---

## 5. 月度巡检（review_cycle: monthly 落地）

每月固定跑三项扫描（命令在仓库根目录跑）：

### 5.1 链接扫描（找坏链）

抽出所有相对 markdown 链接目标，检查文件是否存在：

```
grep -rEho '\]\(\.{1,2}/[^)]+\.md' wiki/products/bathtub-filter/ | sed 's/](//'
```

对每个目标 `ls` 验证存在；[[obsidian]] 反链同理核对目标页真在。目标：0 broken。

### 5.2 禁词扫描（找 claim 漂移/违禁措辞）

```
grep -rniE 'eczema|湿疹|baby-safe|patented|专利技术|获专利|softens? your water|软化你的水|TDS 笔|toxin' wiki/products/bathtub-filter/
```

命中逐条判：正文违禁 → 改/删并回 claim-register；仅出现在"禁用清单/护栏说明"上下文 → 放行。

### 5.3 占位 owner 巡检（占位页别烂尾）

```
grep -rln 'officiality: placeholder' wiki/products/bathtub-filter/
grep -rn '\[____\]' wiki/products/bathtub-filter/
```

对每个 placeholder 页 / `[____]` 空位，核对 owner（法务/财务/运营/市场）是否有进展；无进展的记月度待办。

> 巡检产出：一张"坏链数 / 禁词命中 / 未补占位数"三行小结，附本月已清项，写回本页 §6 或提 issue。

---

## 6. 变更 / 巡检日志

| 日期 | 动作 | owner |
|---|---|---|
| 2026-07-02 | SOP 页建立（draft）；随 2026-07-02 BOM 裁定 + TPU→硅胶 + ascorbate 误署更正批次 | strategy |

---

## Sources / 内部依据

- [内容地图（MAP · 治理原则 §一 / 单一真理源 §四）](./bathtub-filter-kes-marketing-site-content-map.md)
- [Claim register（Banned/Conditional/Allowed + 表面→claim 映射）](../bathtub-filter-claim-register.md)
- [Evidence bibliography（证据编号库）](../bathtub-filter-evidence-bibliography.md)
- [滤材效能页（§9 寿命模型 · 数字传播案例）](../bathtub-filter-media-efficacy-at-bath-conditions.md)

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-kes-marketing-site-content-map]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-evidence-bibliography]]
- [[bathtub-filter-media-efficacy-at-bath-conditions]]
