---
type: product
status: draft
owner: strategy
created: 2026-04-17
updated: 2026-04-18
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
| **S-08** Low-clearance / 间隙极小 | 极老/特殊定制 | ~3–5% | ⛔ V1 不支持（结构不可能）|

> 比例为 KES strategy 推断，基于"60% US 家庭是 combo + T-diverter 最常见"+ Delta/Moen/Kohler 三家主流市场份额（合计 >70% 主流 plumbing supply）。**真实数字必须从 NAHB / US Census housing characteristics 数据交叉核实**。

### WS2 物理采样最小集

按上表，KES V1 最小化采样集（覆盖 ~80% 美国 tub spout 安装）：

```
必采（V1 fit scope 决定）：
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

总采样数：8–10 件，预算 ~$300–600（plumbing supply / Home Depot）

### KES V1 fit scope 推断（pre-test）

基于 §2.6 公开比例 + 失败模式 §3，**KES V1 推荐 fit scope 起手包**（待 WS2 测试覆写）：

- ✅ **支持**：S-01, S-02 (slip-fit + IPS), S-07 — 覆盖 ~60–70% 美国家庭
- ⚠️ **conditional**：S-03（取决于曲率），S-04（取决于具体间距）
- ❌ **不支持**：S-05, S-06, S-08 — 必须在产品页 + 包装明示

这意味着 KES V1 的 marketing 应该写：

> "Tested compatible with most standard tub-spout faucets including Moen, Delta, and Kohler T-diverter and threaded models. Not designed for wide-body decorative spouts, severely worn slip-fit fittings, or spouts with less than [X] inches wall clearance."

不写 "fits most tubs"——那是 Sprite/Crystal Quest 翻车的原因。

## 竞品安装方式分布（2026-04-18 LLM 分类，n=13 ASIN）

> 来源：`kes-ops-platform` report 04-18 dimension_matrix，LLM 基于 title + bullet point 标注。可能有误分；详见 `raw/llm_clustering_result.json`。

| installation_type | ASIN 数 | 月销合计（US）| 均价（US）| 代表品牌 |
|---|---|---|---|---|
| `velcro_strap` | 1 | 1K+ | $16 | JYFJYF（最低价 entry）|
| `faucet_mount` | 2 | 1K+ | **$101** | Canopy / Filterbaby |
| `overflow_integrated` | 3 | 2K+ | $21 | SHLLKTTRY / Yolycen |
| `ball_style` | 1 | 500+ | $65 | Crystal Quest |
| `other` | 6 | 4K+ | $41 | Santevia / Beati Faucet / Tubo |

**对 KES V1 fit scope 的含义：**

1. **faucet_mount 是最高价安装方式**（均价 $101），Canopy + Filterbaby 都是 faucet_mount——这是 premium 路线的标配安装形态，与 KES 的 $59–$79 定位一致。

2. **overflow_integrated（嵌入溢水口）= 最低价**（均价 $21），主要是中国白牌 SHLLKTTRY / Yolycen——这是 Cluster 1 白牌的主要形态，KES 应避开（价格信号错误）。

3. **velcro_strap（魔术贴固定）**是入门价位（$16）的独特形态——安装最简单，但固定稳定性可能是隐患（对应 S-06 retention failure 风险）。

4. **ball_style（悬挂球）= $65 小众高价**，Crystal Quest 独占，对应 KES taxonomy 中的离散附件形态——不与 KES V1 spout-mount 路线直接竞争。

**与 WS2 物理采样的关联：**
- faucet_mount（Canopy / Filterbaby）对应 S-01 / S-02 spout-mount 形态——是 KES V1 最直接的参照竞品，WS2 必须采购这两款做 benchmark
- overflow_integrated（SHLLKTTRY）安装在溢水口而非出水口——与 KES S-01~S-07 的 spout-mount 路线是完全不同的安装点，不存在直接兼容冲突

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
