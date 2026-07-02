---
type: product
status: draft
owner: strategy
created: 2026-07-01
updated: 2026-07-02
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, product-architecture, industrial-design, flow-diversion, anti-channeling]
source_count: 5
review_cycle: monthly
verification_status: spot-checked
related:
  - ./bathtub-filter-kes-structure-overview.md
  - ./bathtub-filter-kes-media-calcium-sulfite.md
  - ./bathtub-filter-kes-media-kdf55-copper-zinc.md
  - ./bathtub-filter-kes-media-pp-cotton.md
  - ./bathtub-filter-kes-structure-ip-and-patent-governance.md
  - ./bathtub-filter-kes-marketing-site-content-map.md
  - ../bathtub-filter-technology-notes.md
---

# KES 浴缸过滤器 · 导流模块 / 防沟槽（Flow-Diversion Module）★最核心差异点

## 这一页是什么

这是「产品本体」内容簇的核心差异子页（D2）。它解释 KES 结构里**最能拉开与竞品差距的一个决策**：内腔的**导流模块**，以及为什么 KES 选「分层不混」而不是市面常见的 mixed-bead 黑箱。

这是结构 / 工程叙事，不是疗效叙事。去氯效能口径由滤材页与实测负责，本页只讲「水怎么在滤仓里走」。

> **承重护栏**：导流模块是让 CaSO₃ 层正常工作的**运行必要条件**，讲的是水路均匀性，不代表任何健康结果。这不是净水器，不降 TDS。

---

## 一、机理：为什么 CaSO₃ 层必须有导流

内部测试结论（2025-10-22，见 [技术说明](../bathtub-filter-technology-notes.md)）：

- **KDF 层**：有无导流**无可见差异**——KDF 颗粒大、床密、抗冲刷。
- **CaSO₃ 层**：**无导流时，水流集中冲击床面中心，形成中心冲蚀 crater（沟槽 / channeling）**；一旦形成沟槽，水会走「阻力最小的中心通道」绕过大部分料，接触时间骤降、去氯效能塌陷。
- **加导流模块后**：水流被均匀铺开到整个床面，避免中心冲蚀。

因此结论是：

> **导流模块是 CaSO₃ 层的 operational requirement（运行必要条件），不是可选装饰件。**

浴缸注水是高流速场景（15–30 L/min），水流冲击强，这让 CaSO₃ 层的沟槽风险比低流速场景更突出——导流不是「锦上添花」，是让主力去游离氯层能真正被水流过的前提。

### 一A、生产实现：两仓各有防沟流结构（2026-07-02 按 V1 BOM 表对齐）

上面是**工程测试结论**（谁怕沟流）；[V1 BOM 表](../bathtub-filter-v1-free-chlorine-removal-dimensions-materials.md) 给出的是**生产实现**（防沟流结构长在哪）——两者要分开读，别混：

| 仓 | 防沟流实现（BOM 实物） | 角色 |
|---|---|---|
| **KDF55 仓**（水流先到） | 滤芯上盖中心 **Ø50mm 轻微鼓起导流锥**（部件 10）+ 中心支撑柱（部件 12） | **全系统的进水布水口**：在水进入滤料链的第一站就把冲击铺开——保护的是**整条下游水路**（含 CaSO₃ 层），不是因为 KDF 自己怕沟流（测试显示 KDF 有无导流无可见差异） |
| **CaSO₃ 仓** | 上/下盖把滤料**平均分成 6 个分区**（部件 17/20）+ 3 筋条 6 等份内骨架（部件 19） | CaSO₃ 层自己的防沟流：分区物理隔断，水想「走中心捷径」也只能走到 1/6 区，冲蚀不会塌掉整床 |

一句话：**「导流」在产品里不是一个零件，是一套两级结构**——KDF 仓入口的导流锥管「进水铺开」，CaSO₃ 仓的 6 分区管「主力层不塌」。对外讲导流时按这个口径，不要说成「只有 CaSO₃ 仓有导流件」。

---

## 二、分层不混 vs mixed-bead（解释技术选择，非贬竞品）

KES 明确不走 category default 的混合介质床（mixed-bead / bath-ball）路线，改用严格分层 + 导流。这是解释一个**技术设计选择**，不是贬低任何竞品、不点名 ASIN。

| 维度 | 分层不混 + 导流（KES） | mixed-bead 黑箱（品类常见） |
|---|---|---|
| 水路 | 导流铺开 → 强制水流均匀经过每层料 | 混合床易 channeling，水走捷径 |
| 介质互扰 | 各料分腔，不互相干扰 | 不同料混在一起可能互扰 |
| 更换 | 可分段更换（过滤棉（PET）/ KDF55 仓 / CaSO₃ 仓各自替换） | 整体更换，无法分段 |
| 失效诊断 | 透明可见 + 分层 → 失效原因可定位 | 黑箱，失效原因难诊断 |

客户可见英文（对照 claim-register「Head-to-head with mixed-media competitors」Conditional 行的措辞）：

> `Unlike mixed-bead products, KES uses strict layered media (polyester (PET) fiber → KDF55 → CaSO3) with an internal flow-diversion module. This prevents channeling, prevents media cross-reaction, and lets you replace each layer separately.`
>
> （2026-07-02 按 [V1 BOM 表](../bathtub-filter-v1-free-chlorine-removal-dimensions-materials.md) 裁定更正：滤棉材质 PP→聚酯纤维 PET）

护栏：这是解释技术选择而非贬损，**安全的前提是不点名竞品 ASIN、不夸大对方缺陷**。

---

## 三、claim / 证据状态表

| claim | 状态 | 出处 | 护栏 |
|---|---|---|---|
| CaSO₃ 层无导流→中心冲蚀 crater；加导流→水流均匀铺开 | 🟢 | 2025-10-22 内部测试（[技术说明](../bathtub-filter-technology-notes.md)） | 讲水路机理，不作疗效背书 |
| 导流模块是 CaSO₃ 层 operational requirement（非可选） | 🟢 | 同上 + [V1 卖点页](../bathtub-filter-kes-v1-selling-points-and-pack-contents.md) | 运行必要条件，不译成健康结果 |
| 分层不混防 channeling / 防介质互扰 / 可分段更换 / 可诊断 | 🟢 | [产品架构假设页](../bathtub-filter-kes-product-architecture-hypotheses.md)（反 mixed-media 决策） | 解释技术选择，非贬竞品；不点名 ASIN |
| `Patent pending`（U.S. App. 19/281,644，申请日 2025-07-26；含径向导流腔/防溅裙 + 蜗壳导流槽/涡流叶片） | 🟢 可用 | [专利参考页](../bathtub-filter-kes-patent-19-281644-modular-terminal-water-treatment.md)、[IP 治理页](./bathtub-filter-kes-structure-ip-and-patent-governance.md) | 现可对外写 "Patent pending (U.S. App. 19/281,644)"。🔴 仍禁 patented / granted / 专利技术 / 专利去氯 |
| CaSO₃+KDF 组合本身 | — | [专利表](../bathtub-filter-patent-table.md)（基础专利 2015 已过期） | **不是 KES 专有**；可讲料，不得包装成 KES 专利 |

> **导流结构的专利事实（权威）**：专利申请把导流实现为 **进水模块的径向导流腔 + 防溅裙**，与**处理模块输入端的蜗壳导流槽 + 壳内壁螺旋肋/涡流叶片**——均匀布水、延长接触时间、单向连续水路（无并联分流）。这就是本页「防沟槽」的真实结构（见 [专利参考页 §二](../bathtub-filter-kes-patent-19-281644-modular-terminal-water-treatment.md)）。
>
> ⚠️ **专利措辞铁律（本页最敏感处）**：KES 有 **1 项 pending 发明专利（App# 19/281,644，未授权）**。对外可写 **`Patent pending`（有申请号背书）**。**🔴 绝对禁止**：`patented` / `granted` / `专利技术` / `获得专利` / `专利保护` / `专利去氯技术`（它是 pending 非授权）。CaSO₃+KDF 去氯是行业公有（2015 基础专利已过期），不得包装成 KES 专利。

---

## 承重护栏（必带）

> 导流模块解决的是「水均匀流过 CaSO₃ 层」这个工程问题，让主力去游离氯层能被真正流过。它**不改变**产品定位：这不是净水器、不降 TDS、不治皮肤。去氯效能以实测为准（数字待 Gate 1 DPD）。

---

## 相关页链接

- [D1 · 结构总览](./bathtub-filter-kes-structure-overview.md)
- [M1 · 亚硫酸钙 CaSO₃（为何需导流）](./bathtub-filter-kes-media-calcium-sulfite.md)
- [M2 · 铜锌合金 KDF55](./bathtub-filter-kes-media-kdf55-copper-zinc.md)
- [M7 · 过滤棉（PET）](./bathtub-filter-kes-media-pp-cotton.md)
- [IP 与专利治理（内部真理源）](./bathtub-filter-kes-structure-ip-and-patent-governance.md)
- [内容地图（父）](./bathtub-filter-kes-marketing-site-content-map.md)

## Sources

- [技术说明（导流模块必要性 2025-10-22 测试结论）](../bathtub-filter-technology-notes.md)
- [KES V1 卖点与套装内容（内置导流结构、非混合黑箱）](../bathtub-filter-kes-v1-selling-points-and-pack-contents.md)
- [产品架构假设与确认记录（反 mixed-media 决策）](../bathtub-filter-kes-product-architecture-hypotheses.md)
- [专利表（CaSO₃/KDF 基础专利 2015 过期）](../bathtub-filter-patent-table.md)
- [宣称台账（护栏总表）](../bathtub-filter-claim-register.md)

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-kes-structure-overview]]
- [[bathtub-filter-kes-media-calcium-sulfite]]
- [[bathtub-filter-kes-media-kdf55-copper-zinc]]
- [[bathtub-filter-kes-media-pp-cotton]]
- [[bathtub-filter-kes-structure-ip-and-patent-governance]]
- [[bathtub-filter-kes-marketing-site-content-map]]
- [[bathtub-filter-technology-notes]]
