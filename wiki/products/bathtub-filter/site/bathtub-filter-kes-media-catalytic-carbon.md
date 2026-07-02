---
type: product
status: draft
owner: strategy
created: 2026-06-30
updated: 2026-06-30
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, chloramine, catalytic-carbon, media, filtration-media, clean-formula, version-a]
source_count: 5
review_cycle: monthly
verification_status: spot-checked
related:
  - ./bathtub-filter-kes-marketing-site-content-map.md
  - ../bathtub-filter-claim-register.md
  - ../bathtub-filter-point-of-use-pfas-removal-feasibility.md
  - ../bathtub-filter-kes-media-stack-options-by-water-type.md
  - ../bathtub-filter-chloramine-media-research.md
  - ./bathtub-filter-kes-media-sodium-ascorbate-soak.md
  - ./bathtub-filter-kes-scenario-chloramine.md
  - ../bathtub-filter-evidence-bibliography.md
---

# KES 滤材页 · 催化活性炭（Catalytic Activated Carbon）

> **这一页是「催化活性炭」这一滤材在 KES 站内的唯一口径源（single source of truth）。**
> 任何场景页 / PDP / Hub 提到催化炭的定位、机理、claim、护栏，都引用本页，不得各自改写。催化炭是**氯胺红线区**——本页所有氯胺相关 claim 默认 🟡 Conditional，仅限 V1.5 双段配置，**未闭环前不上 Hub 首屏、不作对外承诺**。

---

## 一、是什么料 / 机理

催化活性炭（catalytic activated carbon）是经特殊蒸汽活化、在表面工程出更多「催化活性位」的活性炭。它与普通 GAC 的区别不在吸附，而在对**一氯胺（NH₂Cl）**的**催化分解**能力：

- Step 1：NH₂Cl + H₂O + C\* → NH₃ + H⁺ + Cl⁻ + CO\*（活性位生成碳-氧中间体）
- Step 2：NH₂Cl + CO\* → N₂ + 2H⁺ + 2Cl⁻ + H₂O + C\*（中间体进一步分解氯胺）

副产物是氨、氯离子、氮气，**不生成含氯有机物**。

**关键机理事实（有 Tier 1 支持）**：氯胺比游离氯「更难、更慢」。游离氯几乎瞬时去除（<1 秒）；一氯胺的去除靠「表面活性位的慢催化分解」，慢 2–3 个数量级。所需接触时间（EBCT）：

| 炭种 | 除一氯胺所需 EBCT | 备注 |
|---|---|---|
| 普通 GAC | ≥10 分钟 | 常在 10 分钟柱测内击穿 |
| 催化炭（煤基） | 4–7 分钟 | 表面活性位改善 |
| 催化炭（椰壳基，如 Jacobi CX-MCA） | ~3–5 分钟 | 氯胺表现最好 |

温度有利于浴缸：Kochany & Lipczynska-Kochany (2008, Tier 1) 实测 20°C 比 5°C 快得多；浴缸水温 ~38–42°C 推断更有利（**但无 40°C 直接台架数据**，见缺口）。

---

## 二、在 KES 的定位

**催化活性炭 = 氯胺版（V1.5）inline 主力：必要，但非充分。**

- 在氯胺配置里，催化炭是**唯一可信的固相 inline 除氯胺路线**（不靠 KDF、不靠亚硫酸钙——那两者对氯胺无效，见 [claim register](../bathtub-filter-claim-register.md) Banned 区 V1 氯胺行 + [氯胺证据页](../bathtub-filter-chloramine-media-research.md) §1、§3）。
- **但它「必要非充分」**：normal bath-fill flow（更别说 25 L/min）下，compact 滤芯的 EBCT 往往达不到 4–5 分钟门槛 → 催化炭单靠 inline **不能保证全除氯胺**，必须配 [抗坏血酸钠浸泡件（M4）](./bathtub-filter-kes-media-sodium-ascorbate-soak.md) 用浴缸停留段完成反应。
- **游离氯版 V1 不含催化炭**（V1 = 过滤棉（PET）+ KDF55 + CaSO₃）。催化炭是 V1.5 / 氯胺线专属，**不得写成 V1 卖点**（register Banned「Carbon claims for V1」行）。

> 定位一句话：**「催化炭把氯胺先降一部分，浴缸浸泡段完成剩下」——它开局，浸泡件收尾。** 不许写成「一颗炭芯搞定氯胺」。

---

## 三、claim 与证据状态表

| # | Claim（英文为客户可见 wording） | 状态 | 证据 / 依据 | 备注护栏 |
|---|---|---|---|---|
| C1 | 「Catalytic carbon is the most credible inline media for reducing combined chlorine (chloramine).」 | 🟡 Conditional | Kochany 2008（Tier 1，催化炭分解一氯胺为 N₂）+ EBCT 表（Tier 2） | 仅 V1.5；必带「inline reduction，not full removal」限定 |
| C2 | 「Inline catalytic carbon reduces part of the chloramine load during fill; the in-tub soak completes it.」 | 🟡 Conditional | 双段机理（[氯胺证据页 §2 / §8](../bathtub-filter-chloramine-media-research.md)） | 必须同时出现 M4 浸泡件；单写 inline 即违规 |
| C3 | 具体去氯胺**百分比 / 击穿点**（如「≥X% @ 某流量」） | 🔴 未验证 / 不得写 | **无 KES 成品氯胺台架数据** | 🟡 待验证：须补**氯胺专属台架**（总氯口径），见缺口。无数前不得给任何百分比 |
| C4 | 「Fast / instant / 秒解 chloramine」 | 🔴 Banned | register Banned §C「氯胺快速/秒解」 | 机理为慢催化分解，**按 4–8 分钟规划**；「fast」不可出现 |
| C5 | 「NSF/ANSI 177 supports our chloramine performance」 | 🔴 Banned | NSF 177 只测游离氯，challenge water 要求氯胺 <0.1 mg/L（[证据页 §5](../bathtub-filter-chloramine-media-research.md)） | 严禁把 177 挪用为氯胺背书 |
| C6 | 「Catalytic carbon removes PFAS / 催化炭除 PFAS」 | 🔴 Banned | 「催化」对 PFAS **零贡献**，机理正交（催化位点针对氯胺/H₂S，除 PFAS 纯靠吸附，催化炭 ≈ 普通 GAC）；且短链几乎无效、浴缸短 EBCT 最不利。详见 [PFAS 除去可行性页](../bathtub-filter-point-of-use-pfas-removal-feasibility.md) | 机理误导 claim，直接判不合规；PFAS 属独立 RO/IX 路线，非浴缸炭路线 |

> 供应商信号提示：宗立 50g 亚硫酸钙球有一份 3–5 L/min 高去除一氯胺的**供应商内部报告**（[证据页 §3 补记](../bathtub-filter-chloramine-media-research.md)），但它是**亚硫酸钙**、非催化炭，且缺方法/检出限/pH/重复次数，**不能作为催化炭 claim 背书**，只能作 KES 自测跟进项。

---

## 四、必带承重护栏（每次引用催化炭都要随行）

1. **「单芯不全除氯胺」必须明说**——催化炭 inline 必要非充分，全除靠 M4 浸泡件在浴缸停留段完成。
2. **禁 fast / instant / 秒解**（register Banned §C）；氯胺按 **4–8 分钟接触时间**讲。
3. **禁「NSF 177 支持氯胺」**；NSF 177 只测游离氯。若日后做认证，正确标准是 NSF/ANSI 42 chloramine reduction（另行申请）。
4. **验证用总氯（total chlorine）试纸**，不是游离氯试纸；并提示抗坏血酸对 DPD/比色法的**还原干扰**测量时机（见 [M4](./bathtub-filter-kes-media-sodium-ascorbate-soak.md) 与 [证据页 §9.5](../bathtub-filter-chloramine-media-research.md)）。
5. 具体百分比 / 流量数字**未坐实前不写**（🟡 待氯胺专属台架）。

---

## 五、用到我的场景（反链）

- [S2 · 氯胺城市场景](./bathtub-filter-kes-scenario-chloramine.md) —— 催化炭是该配置的 inline 主力。
- [S3 · 井水](./bathtub-filter-kes-scenario-well-water.md) —— 井水线（粗 PP → KDF85 → 催化炭）用催化炭，但角色是 **气味 / organics polish**，非氯胺、非游离氯逻辑；见 [media-stack 方案 C](../bathtub-filter-kes-media-stack-options-by-water-type.md)。

---

## Sources

- [Claim register（Banned/Conditional + 表面→claim 映射）](../bathtub-filter-claim-register.md)
- [氯胺去除证据（Kochany 2008 / EBCT / 双段结论）](../bathtub-filter-chloramine-media-research.md)
- [按水源类型的滤材方案（方案 B 氯胺双段）](../bathtub-filter-kes-media-stack-options-by-water-type.md)
- [内容地图（§三 C M3 行）](./bathtub-filter-kes-marketing-site-content-map.md)
- [证据参考书目（条目 22 Kochany）](../bathtub-filter-evidence-bibliography.md)

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-point-of-use-pfas-removal-feasibility]]
- [[bathtub-filter-chloramine-media-research]]
- [[bathtub-filter-kes-media-stack-options-by-water-type]]
- [[bathtub-filter-kes-media-sodium-ascorbate-soak]]
- [[bathtub-filter-kes-scenario-chloramine]]
- [[bathtub-filter-kes-scenario-well-water]]
- [[bathtub-filter-kes-marketing-site-content-map]]
