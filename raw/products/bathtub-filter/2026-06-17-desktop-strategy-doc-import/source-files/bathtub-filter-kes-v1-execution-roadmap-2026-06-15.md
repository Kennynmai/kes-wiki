---
type: product
status: draft
owner: strategy
created: 2026-06-15
updated: 2026-06-15
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, execution-roadmap, gating, launch-plan, v1, control-tower]
source_count: 9
related:
  - ./bathtub-filter-kes-positioning-and-problem-layer-decision-2026-06-15.md
  - ./bathtub-filter-25lpm-dechlorination-bench-test-spec.md
  - ./bathtub-filter-kes-v1-pricing-channel-launch-geo-subscription.md
  - ./bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md
  - ./bathtub-filter-kes-next-step-execution-plan-v1.md
  - ./bathtub-filter-kes-go-no-go-memo-v1.md
  - ./bathtub-filter-validation-testing-protocol.md
  - ./bathtub-filter-chloramine-media-research.md
review_cycle: monthly
verification_status: working
---

# KES Bathtub Filter V1 · 执行路线图（控制塔，2026-06-15）

> 把本轮 8 份战略 doc 收敛成**一条可排期的路径**：哪些 gate、谁 gate 谁、V1→V1.5 怎么排、哪些卡点必须人/外部做。
> 这是「控制塔」页——遇到「下一步做什么」先看这页。

## 0. 决策状态（已推进，更新旧 memo）

| | 2026-04 旧 memo | 2026-06-15 现状 |
|---|---|---|
| 阶段 | conditional GO **for diligence**，非 product GO | **concept 已锁 + 定位/GTM 已定**；进入**上市前 gate 通关**阶段 |
| concept | 待 Workstream 1 收窄 | ✅ 锁定：**游离氯版 · clean-formula「看得见·测得到」· faucet_mount × multi-stage 空白格** |
| A-01（normal-flow 去氯） | weak / 未验证、route-breaking | 🟡 内部 2026-03-20 已测 ~84–86%@27L/min（5ppm 比色，单次）→ **待第三方 DPD 确认** |
| 定位/GTM/获客 | 未做 | ✅ 本轮全部落定 |

> **本页更新/超越**：[next-step-execution-plan-v1](./bathtub-filter-kes-next-step-execution-plan-v1.md) 的 5 workstream 尽调框架（其 WS1 概念收窄、WS4 claim 边界已完成）；[go-no-go-memo-v1](./bathtub-filter-kes-go-no-go-memo-v1.md) 的「必须完成的验证」清单大部分已由本轮 desk 工作 + 内部测试推进，剩下的是**第三方确认 + 认证 + 供应链**（见 §4 gate）。其 §kill-criteria 仍有效，原样继承（§6）。

---

## 1. 关键路径（一句话）

> **一切卡在 Gate 1：25L/min 第三方 DPD 去氯测试。** 它同时确认「测得到」首要价值、25L/min 可行性、和挂篮形态的床体积——过了才谈认证/供应/上市，没过整个 clean-formula 定位的「测得到」半边就是空头。

```
Gate 1 第三方去氯测试 ──→ Gate 2 龙头兼容矩阵 ──→ Gate 3 认证路径 + BOM/COGS
   (go/no-go 总开关)          (launch blocker)         (证明可核查 + 定价)
        │                                                      │
        └──────────────→ V1 上市筹备（文案/创意/claim register/获客 MVP）←┘
                                        │
                                   V1 LAUNCH（游离氯版，P1 三城 DTC）
                                        │
                          V1.5 氯胺配置  ─→  模块目录扩张（井水/阻垢/强化物理层）
```

---

## 2. 三道 Gate（详述）

### Gate 1 — 25L/min 第三方 DPD 去氯测试 ★总开关
- **测什么**：[25L/min 去氯特征 spec](./bathtub-filter-25lpm-dechlorination-bench-test-spec.md)——去氯率 × 流量 × 压降 × 床体积，真实 1–2ppm、第三方 DPD、≥3 重复、寿命坐标。
- **谁做**：实验室/第三方（非比色自测）。
- **通过标准**：25L/min、2ppm、新芯 ≥85% 且 25→27 斜率平缓（spec §4）。
- **解锁**：①「测得到」首屏数字；② 25L/min 形态是否成立 / 床要多大；③ A-01 从 weak→实测；④ claim register「指定流量去氯 X%」的外部证据。
- **不过怎么办**：CONDITIONAL→加大床或降流量标注；FAIL→首屏改「合理流量+高实测去氯」，25 仅作峰值。

### Gate 2 — 龙头兼容矩阵 ★launch blocker
- **测什么**：[validation protocol](./bathtub-filter-validation-testing-protocol.md) Module 2——diverter/non-diverter/swan-neck/slip-fit 真实龙头矩阵 + leak taxonomy（bypass/overflow/seam/retention 分开报）+ TPU strap 耐久。
- **谁做**：产品/工程 + 真实样机。
- **通过标准**：明确 supported / unsupported spout 清单（bounded-fit，非 universal-fit）；重复装卸无 retention/seam 失败。
- **解锁**：兼容性承诺文案、客服规则、退货风险控制。

### Gate 3 — 认证路径 + BOM/COGS
- **认证**：去氯成品走 **WQA Gold Seal / NSF 42 游离氯**（不是 177，177 不测成品认证且不含氯胺）；口径如实（KDF55 继承 NSF/ANSI 42 材料端，成品不冒认）。
- **BOM/COGS**：unit BOM <$15、refill <$5 才能保 wholesale 30% EBIT（定价页反推）。
- **谁做**：法务/合规（认证）+ 供应链/财务（BOM）。
- **解锁**：可核查 USP 的「认证可查」支柱、最终定价、wholesale 谈判。

---

## 3. 五条工作流（现状 → 下一步 → 归属 → 所在 doc）

| 工作流 | 现状 | 下一步 | 归属 | doc |
|---|---|---|---|---|
| **① 产品/测试** | Version A 确认；内部单测正向 | 跑 Gate 1（第三方 DPD）+ Gate 2（兼容矩阵） | 产品/实验室 | [测试 spec](./bathtub-filter-25lpm-dechlorination-bench-test-spec.md) / [validation protocol](./bathtub-filter-validation-testing-protocol.md) |
| **② 合规/Claim** | claim 决策散落本轮各 doc | **归并进操作级 claim register**（allowed/conditional/banned）+ Gate 3 认证 | 法务/合规 | [claim register](./bathtub-filter-claim-register.md)（待更新） |
| **③ 品牌/创意** | 定位/宣言/版式/镜头脚本已定 | 写**完整网站文案** + 拍透明盒英雄镜头 | 品牌/创意 | [定位决策](./bathtub-filter-kes-positioning-and-problem-layer-decision-2026-06-15.md) / [感性定位](./bathtub-filter-kes-clean-formula-emotional-positioning.md) / [版式](./bathtub-filter-kes-homepage-and-about-page-layout.md) / [镜头脚本](./bathtub-filter-kes-transparent-box-hero-shot-script.md) |
| **④ GTM/渠道/定价** | $59–79、DTC 首发、P1 三城、90 天订阅已定 | 等 Gate 1 数字回填首屏；建 DTC + Amazon listing | 增长/GTM | [定价/渠道/地理/订阅](./bathtub-filter-kes-v1-pricing-channel-launch-geo-subscription.md) |
| **⑤ 获客引擎** | 自测套件+读卡+转介绍机制+落地已设计 | 上 **MVP**（referral app+静态链接+换芯抵扣）；ZIP 查询器接水务图谱 | 增长/产品 | [获客引擎](./bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md) |

---

## 4. 分期

| 期 | 范围 | 前置 gate |
|---|---|---|
| **V1** | 游离氯版核心 SKU，P1 三城 DTC 首发 + Amazon 引流，clean-formula 定位，获客引擎 MVP | Gate 1 + 2 + 3 |
| **V1.5** | 氯胺配置（催化炭芯 + 抗坏血酸钠浸泡件），触达圣地亚哥/迈阿密等极硬+氯胺市场 | 氯胺专属台架（[§9 混合自变量](./bathtub-filter-chloramine-media-research.md)）+ 总氯试纸 + 浸泡 UX |
| **V2 / 扩张** | 模块目录补全（井水 KDF85 / 阻垢 adjunct / 强化物理层），喂交叉销售引擎；Target/Babylist 零售 | V1 跑通 + 各模块边界验证 |

---

## 5. 必须人/外部做的卡点（desk 做不了，须排期给人）

- [ ] **Gate 1 第三方 DPD 测试**（实验室）— 总开关
- [ ] **Gate 2 兼容矩阵 + 漏水耐久**（样机）
- [ ] **认证申请**（WQA/NSF 42）— 成本/时间见 cert 估算页
- [ ] **BOM/COGS 反推**（供应链/财务）
- [ ] **CAC payback 模型**（品类认知低→CAC 偏高，教育成本入模）
- [ ] **订阅 churn**（上市 60 天后真实数据）
- [ ] **氯胺台架 + 总氯试纸定制**（V1.5）

---

## 6. Kill criteria（继承 go-no-go，仍有效）

任一成立则把 GO 下调：
- 产品只在 reduced flow 下才有像样去氯（Gate 1 FAIL）
- 兼容性成功高度依赖隐藏 geometry / 用户 workaround（Gate 2 FAIL）
- renter-friendly 与 leak/overflow discipline 无法兼得
- refill/hygiene/setup 负担叠加使 lived economics 崩
- BOM 无法压到保 wholesale margin 的水平（Gate 3 FAIL）

---

## 7. 下一步（本路线图之后最该动的三件）
1. **排 Gate 1 第三方测试**（总开关，越早越好）
2. **claim register 操作化**（工作流②，通往文案/广告/包装/法务）
3. **获客引擎 MVP**（工作流⑤，2–4 周可上，先验证转介绍率）

## Sources / 内部依据
- 本轮 8 份 doc（定位决策 / 感性定位 / 媒体EEAT / 版式 / 镜头脚本 / 定价渠道地理订阅 / 获客引擎 / 25L/min spec）
- [next-step-execution-plan-v1](./bathtub-filter-kes-next-step-execution-plan-v1.md)（被本页更新）
- [go-no-go-memo-v1](./bathtub-filter-kes-go-no-go-memo-v1.md)（kill-criteria 继承）
- [validation testing protocol](./bathtub-filter-validation-testing-protocol.md)（Gate 2）
- [氯胺证据页 §9](./bathtub-filter-chloramine-media-research.md)（V1.5 gate）

## Obsidian links
- [[bathtub-filter-kes-positioning-and-problem-layer-decision-2026-06-15]]
- [[bathtub-filter-25lpm-dechlorination-bench-test-spec]]
- [[bathtub-filter-kes-v1-pricing-channel-launch-geo-subscription]]
- [[bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine]]
- [[bathtub-filter-kes-next-step-execution-plan-v1]]
- [[bathtub-filter-kes-go-no-go-memo-v1]]
- [[bathtub-filter-chloramine-media-research]]
