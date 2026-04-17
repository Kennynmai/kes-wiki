---
type: source-summary
status: draft
owner: strategy
created: 2026-04-17
updated: 2026-04-17
visibility: team
confidence: high
officiality: draft
domain: product
domains: [bathtub-filter, kes-internal, product-architecture, engineering-tests, sales-training, competitor-teardown]
source_type: internal-doc
extraction_mode: structured
review_cycle: one-shot
verification_status: unverified-by-agent
related:
  - ../products/bathtub-filter/bathtub-filter.md
  - ../products/bathtub-filter/bathtub-filter-kes-concept-brief-v1.md
  - ../products/bathtub-filter/bathtub-filter-kes-product-architecture-hypotheses.md
  - ../products/bathtub-filter/bathtub-filter-technology-notes.md
  - ../products/bathtub-filter/bathtub-filter-normal-flow-vs-reduced-flow-evidence-table.md
  - ../products/bathtub-filter/bathtub-filter-media-efficacy-at-bath-conditions.md
  - ../products/bathtub-filter/bathtub-filter-claim-register.md
  - ../products/bathtub-filter/bathtub-filter-compatibility-engineering-breakpoints.md
  - ../playbooks/bathtub-filter-validation-testing-protocol.md
  - ../../raw/products/bathtub-filter/2026-04-17-kes-internal-product-materials-pass.md
---

# 来源摘要｜KES Bathtub Filter 内部产品材料（2026-04-17）

## Obsidian links
- [[bathtub-filter]]
- [[bathtub-filter-kes-concept-brief-v1]]
- [[bathtub-filter-kes-product-architecture-hypotheses]]
- [[bathtub-filter-technology-notes]]
- [[bathtub-filter-normal-flow-vs-reduced-flow-evidence-table]]
- [[bathtub-filter-media-efficacy-at-bath-conditions]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-compatibility-engineering-breakpoints]]
- [[bathtub-filter-validation-testing-protocol]]

## Source
- 原始抓取：[2026-04-17-kes-internal-product-materials-pass.md](../../raw/products/bathtub-filter/2026-04-17-kes-internal-product-materials-pass.md)
- 五份底层文档 + 一张产品爆炸图，均由 product strategist 2026-04-17 提供
- 属于 **KES first-party material**，与此前本 cluster 已收的 external research (marketplace / academic / patent / institutional) 类别不同

## 这份来源是什么
这是 KES 自己已完成的 **bathtub-filter 产品开发档案**的一次集中交付，包含：

1. **Version A 产品讲解 / 销售培训文档**（2026-02，城市市政自来水版，口径"稳妥合规"，浴缸水温 38–42°C）
2. **2024-02 原始市场调查**（2025-09 更新成本）：5 个对标 ASIN 的 teardown + 复盘 mixed-media 品类失效模式
3. **活性炭测试日志**：coconut-shell vs 其他 carbon 的选型 + acid-wash 后的 commissioning 验证（2024-07–2024-08）
4. **流速/溢水/过滤棉分层测试**（2024-11-07）：确定 top stack 的 overflow envelope
5. **导流模块 vs 无 的测试**（2025-10-22）：确认 CaSO₃ 层需要导流以避免中心冲蚀
6. **产品爆炸图**：strap handle → 水箱外壳 → 顶部 cotton/fiber 盘 → KDF55 腔体（金色介质）→ CaSO₃ 腔体（白色颗粒）→ 底部 mesh retention 盘

## 这份来源意味着什么
**这不是"候选架构"，而是已落地的 Version A 产品规格**。它对 bathtub-filter cluster 内多个 pages 的 officiality 有升级作用：

- "architecture hypotheses" 层应从 hypothesis 改为 confirmed design
- "concept brief v1" 应从 concept candidate 语言改为 confirmed Version A
- technology-notes / media-efficacy / normal-flow-vs-reduced-flow 三个 evidence 页面，此前只含 external literature + marketplace signals，现在可以加入 **KES 自己的实测数据**
- claim-register 的 "allowed / conditional" 列可以首次从推测改为基于内部寿命模型 + 测试

## 提取出的关键信息

### 1）核心定位语（必须在所有 customer-facing surface 重复）
> "这不是净水器；它不以降 TDS 为目标。它是**浴缸注水场景的末端减害模块**。"

- **主目标**：快速去氯（新滤芯 · 最佳体验段 ≥99% 总去氯）
- **辅助目标**：沉积物可视化（让用户看到滤芯在工作 = 信任锚）
- **安心层**：KDF55 做末端风险兜底 + 滤芯内部生物膜抑制
- **功能扩展**：浴盐溶解（240 mL 腔体）、矿物增强（可能令 TDS 升高，需声明）

### 2）确认的产品架构（Version A）
媒体层（沿水流方向顶 → 底）：
```
Strap handle (TPU 可调节)
  ↓
外壳 inlet（顶部溢流槽 + 宽入口设计）
  ↓
可选 loading cavity（240 mL：浴盐 / 矿物包 / 维C）
  ↓
KDF55 层：110 g，5–10 目，15 mm 高腔体，60-mesh 304 不锈钢顶底保持网
  ↓
CaSO₃ 层：130 g，3–4 mm 颗粒，15 mm 高腔体，40-mesh 304 不锈钢顶底保持网
  ↓
PP 过滤棉盘（顶部 2 张非织造 + 底部 mesh 盘）
  ↓
Outlet
```

### 3）反品类默认（mixed-media bath ball）的设计决策
category default 的 mixed bead bed 有四个结构性问题：**channeling / 介质互相干扰 / 无法分段更换 / 无法诊断失效模式**。KES 选择严格 PP / KDF / CaSO₃ 分层 + inner 导流模块 + 顶部溢流槽，强制水流**穿过**每一层而不是沿阻力最小路径绕开。

导流模块测试结论（Doc 5）：
- 在 KDF 层：导流 vs 无，无明显差异（KDF 颗粒大、床密，抗冲刷）
- 在 CaSO₃ 层：**无导流时中心形成 crater 被冲蚀**；加导流后水流均匀铺开
- 结论：导流模块是 CaSO₃ 层的 operational requirement，不是 nice-to-have

### 4）流速 / EBCT / KDF 贡献系数（内部实测）
| 注水流速 | 单层 EBCT | KDF 去氯贡献（经验系数） |
|---|---|---|
| 15 L/min | 0.95 s | 43% |
| 20 L/min | 0.71 s | 32% |
| 25 L/min | 0.57 s | 26% |
| 30 L/min | 0.48 s | 21% |

**关键结论**：bath-fill 场景的 EBCT 对 KDF 来说太短，无法让 KDF 做主力去氯。**CaSO₃ 是主力去氯 KPI；KDF 是安心层 + 寿命稳定层**。链式公式：系统总去氯 = 1 − (1 − KDF) × (1 − CaSO₃)。

### 5）Version A 寿命模型（130 g CaSO₃，η = 0.9，38–42°C）
**以"累计通水量 / 泡澡次数 / 周期"为寿命单位，不用"月数"**（这是对 B008A4AG2U / B0012045EO 口径的直接反击，因为后者的"12 个月寿命"是基于淋浴场景，不适用浴缸注水）。

泡澡基准：70 gal 满缸，2/3 = 47 gal ≈ 178 L/次，3 次/周。

**2 ppm 自由氯（US 典型偏高段）条件下**：
| 去氯阶段 | 累计水量 | 泡澡次数 | 周数 |
|---|---|---|---|
| 系统 ≥99% | ~3,481 L | 19.6 | 6.5 |
| 系统 ≥95% | ~17,672 L | 99.3 | 33.1 |
| 系统 ≥90% | ~20,124 L | 113.1 | 37.7 |
| 系统 ≥50%（强制换） | ~25,467 L | 143.1 | 47.7 (~1 年) |

**1 ppm 自由氯（US 典型常见段）条件下**：寿命约 ×2 → ≥99% ≈ 6,962 L，强制换 ≈ 50,934 L ≈ ~2 年。

**Replacement 触发锚**：
- soft trigger：系统总去氯跌到 90%（体验仍好）
- strong trigger：跌到 80%（进入快速衰减）
- mandatory：跌到 50%（视为失效）

### 6）流速 / 溢水 envelope（内部实测，Doc 4）
测试条件：204 g KDF（10–40 目）+ 45 g acid-washed carbon（8–10 目），0.5 MPa，瞬时 38–40 L/min，目标 178 L。

| 顶部 stack | 35 L/min 是否溢水 |
|---|---|
| 无过滤棉盘 | 溢水，且多次冲击后床压实 → 间歇性溢水 |
| 1 mesh + 1 非织造棉盘 | 不溢水 |
| 1 mesh + 2 非织造棉盘 | 不溢水 |
| 1 mesh + 3 非织造棉盘 | 开始溢水（流阻过大） |

美国典型浴缸龙头出水量 18–25 L/min，**2-盘配置在 no-overflow envelope 内有充足余量**。第三盘作为 optional upsell 给偏好慢注水的用户。

### 7）活性碳选型（Doc 3）
- 最终选择：**acid-washed coconut-shell carbon**，8–10 目
- 理由：coconut shell 在 ash（2–4% → acid-wash 后 ~0.5%）/ hardness（≥95%）/ iodine（1,000–1,200 mg/g）三项上均属最高档
- commissioning：2 分钟 pre-rinse 冲洗残粉；0.3 MPa / 29 L/min 穿 200 L 水后无粉末溢出；干燥一天后复测仍无粉末
- **合规动作**：对标 review 中出现的 "carbon powder all over the tub"（B008A4AG2U 10 人点赞的一条差评）→ KES 产品出厂已通过 pre-rinse 验证，可以在 onboarding 中写 "no pre-rinse required"

### 8）Standards 表述口径
- KDF55：从供应商继承 NSF/ANSI 42 的 material-side 资料
- CaSO₃：无第三方 NSF 认证；内部以 NSF/ANSI 177 protocol 做测试参考
- **产品本身不声称 NSF 认证**；提供 chlorine test strips + DPD reagent 让用户自己验证
- 明确区分 material-grade 认证（供应商层）vs finished-product 认证（KES 目前没有）

### 9）FAQ / 销售 anchors
verbatim positions（Version A doc）：
- Q：能降 TDS/PPM 吗？→ A：**不能**。本产品不是 RO 净水器，不以降 TDS 为目标。
- Q：怎么验证去氯效果？→ A：用氯试纸 / DPD 试剂做前后对比，不要用 TDS 笔替代。
- Q：KDF55 到底干什么？→ A：安心层 + 末端风险兜底 + 抑制滤芯内生物膜。**不宣传杀菌**。
- Q：寿命多久？→ A：按累计通水量 / 泡澡次数 / 周期来表达（不用月数）。

### 10）30-秒 retail floor 演示脚本
白度 → 气泡 → **氯试纸** → TDS 笔镇压"TDS 会掉吗"的误解。氯试纸是最强闭环，TDS 笔是**反误解**道具。

### 11）竞品 teardown 要点（从 Doc 2）
5 个对标 ASIN 的核心失效模式（可直接作为 KES 的差异化证据）：

| ASIN | 价格 | 核心正向 | 核心差评（投票数最高） |
|---|---|---|---|
| B008A4AG2U Crystal Quest | $64.95 | 给小孩买、去氯、皮肤/头发改善 | 碳粉从滤芯冲出来（10 赞）、chrome 涂层剥落（29 赞）、strap 断裂（42 赞）、氯试纸显示无变化（111 赞）、无第三方测试（363 赞）、盖子拧不开（44 赞） |
| B0742KFY9R Santevia-type | $22.99 | 给小孩买 | loofah 袋里发霉（16 赞）、TDS 升高被 seller 解释（需要 narrative defense） |
| B08Y8GSVJS | $17.80 | KDF55 含量更高 | 溢水（38 条差评占主导） |
| B0C5D7NLC7 | $36.97 | 双滤芯、KDF55 | 溢水（评论量少） |
| B0012045EO | $39.95 | KDF55 classic、去氯 | 安装问题（67 条）、溢水（63 条）、无效（36 条 + 一条 422 赞的氯试纸验证） |

**KES 优势窗口**（从竞品差评反推）：
- overflow 解决（Doc 4 的 2-盘 no-overflow envelope）
- universal spout 适配（strap handle + 灵活 TPU 设计）
- carbon 不冲粉（Doc 3 的 acid-wash + pre-rinse 验证）
- 第三方可验证（送 chlorine test strips）
- 寿命口径老实（"累计通水量"而不是"12 个月"）

## 这份来源的局限
- **口径范围**：明确只覆盖 US urban municipal tap water + 浴缸注水（不覆盖 well water / softened water / rainwater / cistern / rural USVI 场景 — 这些路径参见 [bathtub-filter-water-jurisdiction-demand-map](../products/bathtub-filter/bathtub-filter-water-jurisdiction-demand-map.md) 和 [bathtub-filter-well-water-research](../products/bathtub-filter/bathtub-filter-well-water-research.md)）
- **氯形式假设**：寿命模型默认自由氯 1–2 ppm。**氯胺场景未覆盖**（CaSO₃ 对氯胺基本无效 — 参见 [bathtub-filter-chloramine-media-research](../products/bathtub-filter/bathtub-filter-chloramine-media-research.md)）。需要在 US 地理对应上做 free-chlorine city 圈定，或增加 Version C 专门处理氯胺城市
- **KDF 贡献系数来源**：标注为"内部经验值"，无附带实验条件原始记录；建议由 validation protocol 在外部复测
- **寿命模型基础数据**：来自"宁立"（Lining? Ningli?）实验报告（40 g CaSO₃ / 0.5–1 mm / 8 L/min / 2 ppm 自由氯），按质量比 3.25 × η 0.9 缩放；原始报告 PDF 列在 Doc 1 的附录链接中，需要核对
- **没有第三方 finished-product 认证**；已在产品讲解中明确声明"不做此类 claim"
- **Version A 存在即暗示 Version B / C 存在或规划中**：Doc 1 多次写"稳妥合规（Version A）"；需要确认是否有更激进的 claim 口径版本，以及它们的边界条件

## 建议下一步（hold pending 用户决策）
五条具体的 downstream 写入建议，每条可独立执行，相互不阻塞：

1. **[技术记录层]** 把内部 EBCT / KDF 贡献系数 / 寿命模型三张表写入 [bathtub-filter-technology-notes](../products/bathtub-filter/bathtub-filter-technology-notes.md) 和 [bathtub-filter-media-efficacy-at-bath-conditions](../products/bathtub-filter/bathtub-filter-media-efficacy-at-bath-conditions.md)
2. **[架构确认层]** 升级 [bathtub-filter-kes-product-architecture-hypotheses](../products/bathtub-filter/bathtub-filter-kes-product-architecture-hypotheses.md) 从 hypothesis 到 confirmed design，或 rename
3. **[Concept brief 层]** 更新 [bathtub-filter-kes-concept-brief-v1](../products/bathtub-filter/bathtub-filter-kes-concept-brief-v1.md)：从 concept candidate 改为 Version A confirmed，明确 Version A / 待规划 Version B 的边界
4. **[Claim register 层]** 从 Doc 1 的定位语 + FAQ + 寿命模型，填充 [bathtub-filter-claim-register](../products/bathtub-filter/bathtub-filter-claim-register.md) 的 allowed / conditional / banned
5. **[Validation log 层]** 在 [bathtub-filter-validation-testing-protocol](../playbooks/bathtub-filter-validation-testing-protocol.md) 登记：已完成的内部测试（overflow、carbon commissioning、diversion）、仍缺的外部复测（EBCT-分辨率的 free-chlorine 去除率、DPD 方法的前后对比、泡澡水温下的 CaSO₃ 寿命实测）

全部 5 项都执行约需 5–9 页更新；如果先只执行 1 + 5（最小化风险、最大化 evidence 价值），约需 3 页更新。
