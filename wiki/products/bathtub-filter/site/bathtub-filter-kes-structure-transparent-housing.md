---
type: product
status: draft
owner: strategy
created: 2026-07-01
updated: 2026-07-14
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, product-architecture, industrial-design, transparent-housing, clean-formula]
source_count: 4
review_cycle: monthly
verification_status: spot-checked
related:
  - ./bathtub-filter-kes-structure-overview.md
  - ../bathtub-filter-kes-website-copy-v1.md
  - ./bathtub-filter-kes-media-calcium-sulfite.md
  - ./bathtub-filter-kes-media-kdf55-copper-zinc.md
  - ./bathtub-filter-kes-media-pp-cotton.md
  - ./bathtub-filter-kes-marketing-site-content-map.md
  - ../bathtub-filter-kes-v1-selling-points-and-pack-contents.md
---

# KES 浴缸过滤器 · 透明滤仓（Transparent Housing）

## 这一页是什么

这是「产品本体」内容簇的透明滤仓子页（D3）。它讲 clean-honest 定位的**物理实现**：透明硬壳滤仓让用户看到真实的料名、料量、顺序，并且可替换。

> **承重护栏（本页最关键的一句）**：**可见 ≠ 更有效**。透明是**信任（trust）钩子**，让用户能核对「盒子里真有这些料、这个量、这个顺序」；产品的去氯**效能（efficacy）另由去氯实测支撑**，不是「因为看得见所以更管用」。这防的是内容地图里点名的「假设 4 陷阱」——不得让「可见」暗示「更有效 / 更能治」。

---

## 一、clean-honest 的物理实现

对照 [宣称台账](../bathtub-filter-claim-register.md) 的 Transparency / clean-formula 行与 [网站文案 v1](../bathtub-filter-kes-website-copy-v1.md) 的 clean-formula 叙事：

- 透明硬壳包裹滤材，组合成滤仓；当前选中 Formula 的料名、料量、顺序都应可核对。Free-Chlorine 基线为 PET / KDF55 130g / CaSO₃ 110g；其它版本切换到各自真实 BOM，不能继续显示游离氯层序。
- 客户可见英文：`See the media. The amount. The order. Clean is what you can see.` / `Copper-zinc you can see. Calcium sulfite you can see. No third thing you can't name.`
- 这是「clean」的诚实定义：clean 讲的是**透明与料级诚实**，不是 efficacy，不是「去有害物 = 治皮肤 / 健康」（见 claim-register Banned 区）。

---

## 二、可替换

- 透明硬壳滤仓是**独立、可替换**结构：过滤棉（PET）、KDF55 仓、CaSO₃ 仓可分段更换（呼应 [D2 分层不混](./bathtub-filter-kes-structure-flow-diversion-module.md)）。
- 结构支持经批准的可配置组合，但用户不能自行改变顺序；S1/S2/S3 使用固定 Formula，SVC13 只生成白名单 `formula_id`。
- 更换触发与寿命口径不在本页定义——见唯一真理源 [T3 更换/寿命页](./bathtub-filter-kes-page-replacement-and-lifespan.md)（按 baths/gallons，不用月）。

---

## 三、材质

| 项 | 内容 | 状态 |
|---|---|---|
| 滤仓外壳 | 透明硬壳（可视化、可替换） | 🟢结构 |
| 具体材质牌号 | Eastman Tritan TX1001；Ø120×35 mm，目标壁厚 1.5 mm | 🟢 BOM 已定；成品批次/迁移与耐久验证仍按质量计划管理 |
| 内部网夹 | KDF55 层 60-mesh 304 不锈钢网夹；CaSO₃ 层 40-mesh 304 网夹 | 🟢（[技术说明](../bathtub-filter-technology-notes.md)） |

---

## claim / 证据状态表

| claim | 状态 | 出处 | 护栏 |
|---|---|---|---|
| 透明硬壳滤仓，料名/料量/顺序可见 | 🟢 | [V1 卖点页](../bathtub-filter-kes-v1-selling-points-and-pack-contents.md)、claim-register | **可见≠更有效**；透明是 trust 钩子 |
| 滤仓可替换 / 可分段更换 | 🟢 | [V1 卖点页](../bathtub-filter-kes-v1-selling-points-and-pack-contents.md) | 更换/寿命口径回 [T3](./bathtub-filter-kes-page-replacement-and-lifespan.md)，本页不改写 |
| `Clean is what you can see`（clean-formula） | 🟢 | [网站文案 v1](../bathtub-filter-kes-website-copy-v1.md) | clean 讲透明与料级诚实，🔴 不得暗示治皮肤/健康 |
| Tritan TX1001 透明滤仓 | 🟢 BOM | [V1 BOM 表](../bathtub-filter-v1-free-chlorine-removal-dimensions-materials.md) | 只作材质/结构事实；成品认证不得由牌号外推 |

## 四、Hub / PDP 展示与链接

- 整体近照可点击进入本页；材料 hotspot 分别进入 M1–M7。
- 版本 tab 改变时，材料名、量、层序、试纸/附件和 `Used in` 必须同步更新。
- 默认图不允许始终显示 Free-Chlorine 层序后再用文字声称适配氯胺/井水。
- 主 CTA 读取 `selected_formula` 返回对应 PDP；没有选择时进入 Water Match。
- `See the media. The amount. The order.` 可用；`because you can see it, it works better` 不可用。

---

## 承重护栏（必带）

> **可见 ≠ 更有效。** 透明滤仓是让你**核对**「料、量、顺序」的信任工具，不是效能证明。去氯效能由实测支撑（数字待 Gate 1 DPD）。这不是净水器、不降 TDS；`We won't tell you it 'treats' anything.`

---

## 相关页链接

- [D1 · 结构总览](./bathtub-filter-kes-structure-overview.md)
- [Hub · 网站文案 v1（clean-formula）](../bathtub-filter-kes-website-copy-v1.md)
- [M1 · 亚硫酸钙 CaSO₃](./bathtub-filter-kes-media-calcium-sulfite.md)
- [M2 · 铜锌合金 KDF55](./bathtub-filter-kes-media-kdf55-copper-zinc.md)
- [M7 · 过滤棉（PET）](./bathtub-filter-kes-media-pp-cotton.md)
- [T3 · 更换 / 寿命](./bathtub-filter-kes-page-replacement-and-lifespan.md)
- [内容地图（父）](./bathtub-filter-kes-marketing-site-content-map.md)

## Sources

- [KES V1 卖点与套装内容（透明滤仓、可替换）](../bathtub-filter-kes-v1-selling-points-and-pack-contents.md)
- [网站文案 v1（clean-formula 叙事）](../bathtub-filter-kes-website-copy-v1.md)
- [技术说明（网夹规格）](../bathtub-filter-technology-notes.md)
- [宣称台账（Transparency / clean-formula 护栏）](../bathtub-filter-claim-register.md)

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-kes-structure-overview]]
- [[bathtub-filter-kes-website-copy-v1]]
- [[bathtub-filter-kes-media-calcium-sulfite]]
- [[bathtub-filter-kes-media-kdf55-copper-zinc]]
- [[bathtub-filter-kes-media-pp-cotton]]
- [[bathtub-filter-kes-marketing-site-content-map]]
