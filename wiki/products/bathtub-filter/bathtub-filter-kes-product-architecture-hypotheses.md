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
domains: [bathtub-filter, kes, product-architecture, hypotheses, confirmed-design]
source_count: 11
review_cycle: monthly
verification_status: spot-checked
related:
  - ./bathtub-filter-brand-operating-matrix-v2.md
  - ./bathtub-filter-installation-risk-matrix-v2.md
  - ./bathtub-filter-claim-risk-audit-v2.md
  - ./bathtub-filter-technology-notes.md
  - ./bathtub-filter-media-efficacy-at-bath-conditions.md
  - ../../source-summaries/bathtub-filter-kes-internal-product-materials-2026-04-17.md
---
# Bathtub Filter — KES 产品架构假设 → 确认 log

## 📌 Status update 2026-04-17：Version A 已从假设升级为确认设计

以下 6 个原始假设在 [KES 内部产品材料 2026-04-17](../../source-summaries/bathtub-filter-kes-internal-product-materials-2026-04-17.md) 到位后，已可以逐条映射到 **Version A 已确认架构**（urban municipal tap water，38–42°C）。

| # | 原假设（2026-04-12）| Version A 状态 | 落地证据 |
|---|---|---|---|
| 1 | 不要从最大宣称沐浴球起步 | ✅ **已确认并执行** | Version A 定位语："不是净水器，不以降 TDS 为目标，是末端减害模块"。不声称 heavy metals / VOCs / PFAS 等 broad stack |
| 2 | 以氯为重点的狭义路径优于广泛皮肤结果路径 | ✅ **已确认并执行** | 主 KPI 绑定"系统总去氯率"（新滤芯 ≥99%）；FAQ 明确拒绝 eczema / baby-safe 类语言 |
| 3 | 浴缸喷嘴兼容性是核心产品问题 | ✅ **已确认；方案不同**于早期猜想 | Version A 选择 **TPU 可调 strap** + 宽入口设计（而非 adapter 矩阵）；overflow envelope 已实测在 35 L/min 内 |
| 4 | 优质视觉需要更强性能证明 | ✅ **已确认并执行** | Version A 设计 **可视化 filter disc**（让用户看到滤芯在工作）+ chlorine test strip 赠品（让用户自验证）——同时满足视觉可信 + 实测可信 |
| 5 | 软悬挂/仪式路线有维护摩擦风险 | ⏸ **作为 Version A 非路径**；候选 B/C 留作未来评估 | Version A 选择硬壳 + 可替换腔体；软悬挂路线（如 Santevia 式布袋）的霉变风险（Doc 2 竞品 teardown: B0742KFY9R 16 赞差评）已验证为真 |
| 6 | 获胜组合 = 优质设计 + 狭义承诺 + 现实流程 | ✅ **已确认为 Version A 执行范本** | 三者同时到位：可视化 filter + "≥99% 最佳段"的有界承诺 + no-overflow envelope（18–25 L/min US 常见龙头下有余量） |

### Version A 的 **新增已确认设计事实**（超出原 6 条假设的范围）

这些是 2026-04-12 假设清单**未预见但已被确认**的设计决策：

- **反 mixed-media 决策**：category default 的混合介质床（bath ball）因 channeling / 介质互干扰 / 无法分段更换 / 无法诊断失效，被 KES 明确拒绝。Version A 采用严格 PP / KDF / CaSO₃ 分层 + 导流模块
- **媒体职责重分配**：KDF 从"去氯主力"降级为 **安心层 + 生物膜抑制 + 寿命稳定层**；CaSO₃ 上升为 **主力去氯 KPI**。原因是浴缸 EBCT 0.48–0.95 s 对 KDF 太短（详见 [[bathtub-filter-technology-notes]] EBCT 表）
- **寿命口径反品类默认**：用"累计水量 / 泡澡次数 / 周期"而非"月数"（见 [[bathtub-filter-media-efficacy-at-bath-conditions]] Section 9）
- **认证口径**：KDF55 继承 NSF/ANSI 42 material-side；CaSO₃ 无第三方认证但内部参照 NSF/ANSI 177 protocol 测试；**成品本身不声称 NSF 认证**
- **碳选型已决定**：acid-washed coconut-shell 8–10 目，出厂已通过 pre-rinse 验证 → 可宣称 "no pre-rinse required"（反击 B008A4AG2U 类产品的碳粉差评）

### 仍未落定的架构问题（待 Version B / C 或后续评估）

以下问题 Version A 暂不解决，但在未来版本或次级路线中仍 open：

- 氯胺城市的媒体配方（Version A 明确不覆盖；约 35–40% 美国市政系统使用氯胺）
- 硬水 / 软水器下游用户的次级价值主张（CaSO₃ 不软水）
- Well-water 场景的替代媒体栈（需要 KDF-85 + 催化炭，不适用 Version A）
- 软悬挂/仪式版本（如果 KES 决定进入 beauty / ritual segment）
- 第三方 finished-product 认证路径（WQA Gold Seal 或 NSF/ANSI 42 成品申请的成本/时间评估见 [[bathtub-filter-certification-cost-and-timeline-estimates]]）

---

## 原始假设记录（2026-04-12，保留作 trail）

## Obsidian links
- [[bathtub-filter]]
- [[bathtub-filter-brand-operating-matrix-v2]]
- [[bathtub-filter-installation-risk-matrix-v2]]
- [[bathtub-filter-claim-risk-audit-v2]]
- [[bathtub-filter-kes-concept-brief-v1]]
- [[bathtub-filter-kes-route-elimination-memo-v1]]

## 为什么有这页
本页把研究转化为 KES 角度的产品架构假设。

这些**不是推荐方案**——它们是关于"哪种 bathtub filter 概念更有可能成立"的结构化押注，便于后续用证据去验证或推翻。

## 假设 1 — 不要从"最大 claim 的 bath-ball"路线起步
### 原因
- bath-ball 形态的入场者普遍讲宽 claim（heavy metals / VOCs / PFAS / 皮肤结果）
- 评测 / 性能证据上可见 flow 真实性与 proof 之间的张力
- 宣称合规风险快速累积

### KES 解读
commodity bath-ball clone 路线入场门槛低，但**建立信任的门槛高**——这对 KES 不是好权衡。

## 假设 2 — 以氯为核心的窄路径，比宽皮肤结果路径更成立
### 原因
- 以氯为锚的语言目前是最稳的防御区
- Sprite 式的窄滤材叙事比 Tubo / Kinder 式的宽结果宣称看起来更可信

### KES 解读
如果 KES 进入这个品类，应优先选择：
- chlorine / 气味 / bath comfort 这种窄 framing

**而不是**：
- eczema / baby-safe / 皮肤结果这种宽 framing

## 假设 3 — 龙头兼容性（compatibility）是核心产品问题，不是次级配件问题
### 原因
- install / slip / fit / flow 这些 trade-off 在评测里反复出现，权重远高于一般预期
- 市场普遍使用的"universal fit"叙述被明显高估

### KES 解读
真正可行的产品可能需要**明确的兼容性规则 + adapter 逻辑 + 清晰的 spout 适配边界**——而不是模糊的"通用兼容"。

## 假设 4 — premium 视觉可以支撑溢价，前提是 performance 没有显著更弱
### 原因
- Canopy 证明 premium bathtub filter 定位是可行的
- 但评测同时显示：**越 premium 的视觉，评测对 performance 的审查越严**

### KES 解读
KES 可以借用 premium 视觉语言，但需要比"纯美学"更强的**实用证明闭环（proof loop）**来承接溢价。

## 假设 5 — soft-hanging / 仪式路线能减轻硬件压迫感，但会加重维护摩擦
### 原因
- Santevia 式悬挂过滤器更容易 frame 成"健康 / 皮肤舒适"
- 但**晾干 + 更短的换芯节奏 + 霉变风险**会抬高维护摩擦

### KES 解读
如果 KES 想避开硬塑料硬件的视觉冲突，这条路线有吸引力；但必须按**用户对仪式化维护的耐受度**来评估——这是决定路线死活的关键变量。

## 假设 6 — 最可信的"获胜组合"可能是混合体：premium 设计 + 窄技术承诺 + 现实 flow 规则
### 原因
当前证据指向"最强组合"大致是：
- 不激进的 claim 栈
- 更贴合浴室感知的 fit / 美学
- 现实的 install 故事
- 清晰的 maintenance 逻辑
- 无 medical / outcome claim

### KES 解读
这条路径比两端的任一极端都更有希望：
- 纯 commodity bath-ball clone（宽 claim，低信任）
- 纯 eczema / baby-outcome DTC 产品（高合规风险）

## 对 KES 的 open design questions
- 龙头 vs. 淋浴场景的适配如何 split？
- 窄 chlorine comfort 叙事 vs. 更宽的过滤叙事，如何定 framing？
- 以"每次泡澡"水量为口径的 cartridge 经济学是否成立？
- family / baby 邻接是否可做到**不越过 safety claim 边界**？
- premium 软视觉识别 × 技术信任识别 × 两者混合识别，哪一种最优？
