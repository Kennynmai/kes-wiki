---
type: product
status: draft
owner: strategy
created: 2026-04-17
updated: 2026-04-17
visibility: team
confidence: low
officiality: draft
domain: product
domains: [bathtub-filter, kes, compatibility, installation, fit]
source_count: 2
review_cycle: monthly
verification_status: unverified
related:
  - ./bathtub-filter-compatibility-engineering-breakpoints.md
  - ./bathtub-filter-installation-risk-matrix-v2.md
  - ./bathtub-filter-test-gating-checklist-for-kes.md
---

# Bathtub Filter — Supported Tub-Spout Matrix (Stub)

## Why this page exists

这是 **Gate 2 必须完成的 artifact**，在样品采购（Workstream 2）开始前必须填充完整。

当前状态：**stub（框架页）**。spout type taxonomy 和 KES support status 列均未经实物测试确认。

**不得在完成以下工作前将此页用于产品决策：**
1. 获得各类 spout 的实物样本
2. 实际测试每类 spout 的 attachment、retention stability、overflow risk
3. 将 support status 从 "TBD" 更新为 "supported / conditional / not-supported"

---

## Spout type taxonomy

这套分类基于 compatibility-engineering-breakpoints 页面识别出的 minimum tub-spout taxonomy。8 个类别是工程断点分析建议的最低区分粒度——实际物理采购和测试时可能需要细化。

| # | Spout type | Description | Diverter? | Attachment method | KES support status | Notes |
|---|---|---|---|---|---|---|
| S-01 | Straight non-diverter, stable underside / lip | 最常见的圆柱型直出口喷嘴，底面或边缘有稳定支撑面 | No | Over-spout clamp / underside hanging | TBD | Likely most compatible candidate; should be tested first |
| S-02 | Straight spout with diverter knob | 顶部有换向拨杆（用于切换到 showerhead）的直型喷嘴 | Yes | Over-spout clamp (knob may interfere with some attachments) | TBD | Diverter knob may block or destabilize certain adapter designs |
| S-03 | Curved / gooseneck-like spout | 弯曲出水口，出水方向非水平向前 | Varies | Adapter geometry must accommodate curve | TBD | Geometry mismatch likely higher; needs specific adapter design |
| S-04 | Short-projection spout close to wall | 喷嘴出水口距离墙面很近，tile clearance 很小 | Varies | Limited adapter / hanger room | TBD | High clearance constraint; likely difficult without custom geometry |
| S-05 | Wide-body decorative spout | 装饰型宽体喷嘴（常见于 modern / designer 浴室）| Varies | Clamp may not close around wide body | TBD | Wide profile may prevent standard over-spout clamping |
| S-06 | Slip-fit spout with wobble / lower confidence | 套装固定（无螺纹），本体已有轻微松动 | Varies | Attachment stability compromised by base wobble | TBD | High retention failure risk; even if adapter fits, spout wobble propagates |
| S-07 | Threaded spout with varied outlet geometry | 螺纹固定（更稳固），但出水口方向或截面不统一 | Varies | Threaded body provides better retention, but outlet geometry varies | TBD | Body retention stronger; compatibility depends on outlet cross-section |
| S-08 | Low-clearance spout with minimal wall gap | 喷嘴与墙面之间没有足够间隙，安装件无法正确就位 | Varies | Extremely limited adapter mounting space | TBD | May be physically incompatible with any over-spout approach |

---

## Failure mode by type

Based on the installation risk matrix and compatibility engineering breakpoints. This table maps which spout types are structurally likely to trigger which failure modes. All entries are **pre-test hypotheses**, not confirmed observations.

| # | Spout type | Bypass flow risk | Top overflow risk | Seam / housing leak risk | Retention failure risk | Notes |
|---|---|---|---|---|---|---|
| S-01 | Straight non-diverter, stable | Low | Medium | Low | Low | Best candidate; still needs overflow discipline at high flow |
| S-02 | Straight with diverter knob | Low–medium | Medium | Low | Medium | Diverter knob may create misalignment and partial bypass |
| S-03 | Curved / gooseneck | High | Medium | Medium | Medium | Water path geometry mismatch likely increases bypass risk |
| S-04 | Short-projection / close to wall | Medium | Low–medium | Medium | High | Tight clearance forces non-ideal attachment angles |
| S-05 | Wide-body decorative | Medium | Medium | High | High | Clamp may not seat properly; seam stress if over-tightened |
| S-06 | Slip-fit with wobble | High | Medium | Medium | Very high | Wobble propagates to entire filter assembly during fill |
| S-07 | Threaded, varied outlet | Low–medium | Medium | Low | Low | Best retention of threaded types; outlet variation is primary variable |
| S-08 | Low-clearance / minimal wall gap | High | Medium | High | High | Physical constraint likely makes this category incompatible |

---

## Next steps to complete this page

在进行 Workstream 2（样品采购）和 Workstream 3（验证测试）期间，按以下顺序完成本页：

- **Step 1 — 获取实物样本：** 每个 spout type 至少采购 1–2 件实物，优先覆盖 S-01、S-02、S-03 作为最高优先级（最常见 + 最有分歧）
- **Step 2 — 拍摄与记录：** 对每类 spout 拍照，记录外径、出水口截面、底面几何、diverter 位置、距墙间距等关键参数
- **Step 3 — 适配测试：** 使用候选竞品 benchmark 样品（来自 WS2）对每类 spout 进行 attachment fit test；记录是否需要 workaround
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
