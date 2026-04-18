---
type: product
status: draft
owner: strategy
created: 2026-04-17
updated: 2026-04-17
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, ip, freedom-to-operate, filterbaby, patent, claim-analysis, legal-prep]
source_count: 4
review_cycle: as-needed
verification_status: working
related:
  - ./bathtub-filter-ip-depth-and-brand-marker-map.md
  - ./bathtub-filter-patent-table.md
  - ./bathtub-filter-sns-creator-and-visual-taxonomy.md
  - ./bathtub-filter-claim-risk-audit-v2.md
  - ./bathtub-filter-research-coverage-gaps.md
---

# Bathtub Filter — FilterBaby `US12534389B2` FTO 预分析（KES 定位对照）

## 为什么有这页

Gap doc G 层的 2026-04-17 法律状态扫描发现：经典 spout-mount + KDF/CaSO₃ 架构（Sprite Chlorgon, US6145670A 等）已 expired/lapsed，KES freedom-to-operate。**唯一活跃的 blocking 风险是 FilterBaby 的 `US12534389B2`**（到期 2044-03-21）。

但 IP-depth-and-brand-marker-map 只到"识别威胁"层，没把 patent claim 拆开对照 KES 候选定位。这页做：

1. 把 FilterBaby patent 的 claim limitations 拆成 element list
2. 把 KES 候选定位（V1 baby/eczema、V1 skincare-DTC、V2 mineral spa 等）逐一对照
3. 给出**哪些 KES positioning 路径是 patent-clear，哪些必须避开或申请 design-around**
4. 输出一份给外部 patent counsel 的 FTO opinion brief

> ⚠️ **本页不是 legal opinion。** 是 KES 内部的 pre-counsel triage，目的是减少外部 attorney 工时（让他们直接做 claim chart，不用花时间理解我们的产品）。**真正的 FTO 决定必须由有 patent bar 资质的 attorney 出具。**

## 1. Patent 基础信息

| 字段 | 值 |
|---|---|
| Patent number | **US12534389B2** |
| Title | Faucet water filter assembly for water filtration and skin treatment |
| Assignee | FilterBaby LLC + Saxton Brothers LLC |
| Inventors | Xin Ma, Aaron Saxton, Matthew Saxton |
| Priority date | **2023-03-28** |
| Filing date | 2023-09-14 |
| Issue date | 2026-01-27（最近 issued）|
| Expiration | **2044-03-21** |
| Status | **Active**（issued + maintenance fees current） |

> 来源：Google Patents (`patents.google.com/patent/US12534389B2`)。完整 claim 文本未在公开 page 上展开，本页基于 Abstract + Detailed Description + 公开技术描述综合。**外部 counsel 必须基于完整 claim 文本（USPTO PAIR 下载）做正式 chart。**

## 2. Claim limitation 重建（基于公开 description）

按公开技术描述，Claim 1（独立 claim）的核心 limitations 推断包括：

| Element ID | Limitation 描述 | 必要性 |
|---|---|---|
| L-01 | **Faucet** water filter assembly | 必要——claim 限定 faucet 而非 tub-spout |
| L-02 | **Horizontal orientation** of the filter | 必要——区别于传统垂直 inline filter |
| L-03 | Filter element **viewable through a front cover** | 必要——前 cover 透明/开窗 |
| L-04 | Filter housing 适配 standard faucet | 必要 |
| L-05 | **Optional skin treatment element adapter** | 可选 dependent claim |
| L-06 | Adapter receives a **water-dissolvable, skin treatment element** (disc) | 可选 dependent |
| L-07 | Filtered water passes through skin treatment element **before being dispensed** | 可选 dependent |
| L-08 | UV sterilization element（独立或 dependent claim） | dependent claim |
| L-09 | Smart controller monitoring filter status + treatment element consumption | dependent claim |
| L-10 | Geographic/contaminant-customized filter selection | dependent claim |

**Independent claim 的核心 = L-01 + L-02 + L-03 + L-04**（faucet + horizontal + viewable + 安装在 faucet 上）。L-05~L-07 是 dependent，把 skincare-disc 路线锁定在更窄范围。

## 3. KES 候选定位 × claim element 对照

### 3.1 路径 A：KES V1 = bath tub-spout filter（当前 default）

| Element | KES V1 vs. patent | 含义 |
|---|---|---|
| L-01 (faucet) | **KES 不在 faucet，在 tub-spout（浴缸喷嘴）** | ✅ **claim 文字字面不读 KES**——faucet 与 tub-spout 在 plumbing 行业是不同 fixture |
| L-02 (horizontal) | KES 形态 TBD，但典型 over-spout clamp 是 **垂直 hanging** | ✅ 不读 |
| L-03 (viewable through front cover) | KES 设计 TBD | 不影响——前两个不读已足够 |
| L-05~L-07 (skincare disc adapter) | KES 不含 dissolvable skincare 元素 | ✅ 不读 |
| L-08 (UV) | KES 无 UV | ✅ 不读 |
| L-09 (smart controller) | KES 无 smart 监控 | ✅ 不读 |

**verdict（pre-counsel）：✅ likely clear**

**关键风险：** "faucet" 在 patent claim construction 中可能被解读为**包括 tub-spout** （都是水嘴），因为：
- 行业内 "faucet" 有时泛指任何 spout fixture
- Patent 的 detailed description 可能包含支持 "faucet includes bath spout" 的语言
- doctrine of equivalents 可能扩展到 "substantially same function in substantially same way"

**External counsel 必读：** detailed description 是否在任何位置明示 "faucet" 不限于 sink faucet？是否提到 bath spout 或 tub spout？

### 3.2 路径 B：KES skincare-DTC 定位（成人面部护理路线）

如果 KES 把 V1 / V2 定位为**面部洗护 skincare filter**——直接撞 FilterBaby 主市场。

| Element | KES skincare 路线 vs. patent | 含义 |
|---|---|---|
| L-01 (faucet) | KES 接 sink/basin faucet | ❌ **完全 reads** |
| L-02 (horizontal) | 取决于产品形态 | 若 horizontal → ❌ reads；若 vertical inline → ✅ |
| L-03 (viewable front cover) | 取决于设计 | 可控 |
| L-05~L-07 (skincare disc) | KES 若用 dissolvable additive → ❌ reads | dependent claim 触发 |

**verdict：🔴 high risk** — 若 KES 想做 horizontal 的 sink-faucet skincare filter，**几乎必撞**

**Design-around 候选：**
- 改 vertical orientation（避 L-02）
- 不用 dissolvable additive（避 L-05~L-07）
- 走 in-line under-sink filter（不在 faucet 本体）

### 3.3 路径 C：KES showerhead filter（V2/B-line 候选）

KES 若做 shower filter（不是 bath spout），与 patent claim 是否冲突：

| Element | KES showerhead vs. patent | 含义 |
|---|---|---|
| L-01 (faucet) | shower head 不是 faucet——industry 区分清晰 | ✅ likely 不读 |
| 其他 | 不适用 | ✅ |

**verdict：✅ likely clear**

但 showerhead category 已极拥挤（Aquasana / Jolie / AquaBliss / Canopy Shower 等），是另一个商业问题，不是 IP 问题。

### 3.4 路径 D：KES whole-house / inline plumbing filter

完全不在 faucet/spout 形态——

**verdict：✅ clear from US12534389B2**

但 KES 作为 startup 没有进入 whole-house 的渠道力（Home Depot 主导），不是现实路径。

## 4. KES 战略选择树

```
KES 想做什么？
├── (A) bath tub-spout filter (当前默认)  →  ✅ likely clear，但需 counsel 确认 "faucet" 的 claim construction
│
├── (B) skincare sink-faucet filter         →  🔴 高风险，几乎必撞 FilterBaby
│       └── 必须 design around：vertical orientation + 不用 dissolvable additive + 不在 front 显示 filter
│
├── (C) shower head filter                  →  ✅ clear from this patent，但商业拥挤
│
└── (D) whole-house / inline                →  ✅ clear，但 channel 不可行
```

**KES 推荐路径：** **路径 A**（当前 default）保持，但**明确把 KES 与 FilterBaby 在 SNS / 产品页 / claim 措辞上做语言切割**：

- ✅ KES = "bath" / "tub" / "tub-spout" / "bathtub filter"
- ❌ 不要在任何 KES 营销中用 "faucet filter" 描述自己——这种语言重叠会助攻 FilterBaby 在未来 claim construction 论辩里把 "faucet" 解读得宽
- ❌ 不要 ship KES 与 FilterBaby 视觉相似的 horizontal-orientation product
- ❌ 不要做 dissolvable skincare additive（L-06 触发）

## 5. 给外部 counsel 的 FTO brief 模板

下次咨询 patent attorney 时直接发以下 5 项：

```
1. Subject: Pre-launch FTO assessment for KES bath-spout-mount water filter,
   target market US, against FilterBaby LLC US12534389B2 (issued 2026-01-27,
   expires 2044-03-21).

2. KES product description: [attach KES Concept Brief V1 + product architecture
   hypothesis page]. Key facts:
   - Mount: tub spout (not sink faucet)
   - Orientation: TBD — please advise whether horizontal vs vertical
     materially affects FTO position
   - No skincare additive disc
   - No UV
   - No smart controller
   - Media: KDF + calcium sulfite (per Onlyzone supplier file, attached separately)

3. Specific questions:
   (a) Does the term "faucet" in claim 1 of US12534389B2, as construed in
       light of the specification, encompass a tub-spout (bath fill spout)?
       Please cite specific portions of the specification that support
       narrow vs. broad construction.
   (b) Does any independent claim read on a tub-spout-mount, vertical-orientation
       filter without a viewable-through-front-cover element?
   (c) If KES adopts horizontal orientation, does that materially shift FTO
       position? (We are open to vertical if it materially reduces risk.)
   (d) Are there any FilterBaby continuations / divisionals / pending apps
       we should be aware of? (Please pull family from USPTO PAIR.)
   (e) What design-around options would you recommend if any claim is
       likely to read?

4. Materials provided: KES product brief, Onlyzone supplier file, this page
   (bathtub-filter-filterbaby-patent-fto-analysis.md), KES IP-depth map.

5. Deliverable requested: written FTO opinion letter, claim chart for claim 1
   (and any independent claim that may read), and design-around
   recommendations if applicable. Timeline: pre-DV sample finalization
   (estimated [DATE]).
```

## 6. 还卡在哪里（必须人工/外部完成）

- [ ] **正式 FTO opinion** by patent counsel（必做，pre-DV sample 之前）
- [ ] USPTO PAIR 下载 US12534389B2 完整 file wrapper（看 prosecution history → 可能 narrow construction）
- [ ] 调查 FilterBaby continuations / divisionals / pending apps（PAIR + Patent Center 查家族）
- [ ] 监测 FilterBaby 是否对竞品发律师函或起诉（公开诉讼记录）
- [ ] 若 KES 决策 design-around：与 industrial design 团队对接，确认 horizontal vs vertical / front-viewable 的设计可行性

## 7. 复查节奏

- **每季度** 检查 USPTO Patent Center 是否有 FilterBaby 新 issued patents
- **每年** 复查 US12534389B2 maintenance fee 状态（如未付 → 失效，KES 风险消失）
- **每事件** 一旦 KES marketing language 漂向 "faucet" / "skincare" 词义，立即重审本页

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-ip-depth-and-brand-marker-map]]
- [[bathtub-filter-patent-table]]
- [[bathtub-filter-sns-creator-and-visual-taxonomy]]
- [[bathtub-filter-claim-risk-audit-v2]]
- [[bathtub-filter-kes-concept-brief-v1]]
- [[bathtub-filter-kes-product-architecture-hypotheses]]
- [[bathtub-filter-research-coverage-gaps]]
