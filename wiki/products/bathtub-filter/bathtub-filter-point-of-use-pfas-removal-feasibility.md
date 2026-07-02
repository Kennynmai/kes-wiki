---
type: product
status: draft
owner: product
created: 2026-07-01
updated: 2026-07-01
visibility: team
confidence: medium-high
officiality: draft
domain: product
domains: [bathtub-filter, pfas, catalytic-carbon, gac, activated-carbon, point-of-use, ebct, nsf, epa, ion-exchange, evidence]
source_count: 10
review_cycle: monthly
verification_status: deep-research-verified
related:
  - ./bathtub-filter-kes-media-catalytic-carbon.md
  - ./bathtub-filter-point-of-use-hardness-softening-feasibility.md
  - ./bathtub-filter-claim-register.md
  - ./bathtub-filter-water-source-types-guide.md
  - ./bathtub-filter-certification-and-testing-pathways.md
  - ./bathtub-filter-evidence-bibliography.md
---

# 浴缸过滤器就地除 PFAS 可行性（尤其催化活性炭路线）

## 为什么有这页

现有 wiki 一直把 PFAS 归到「broad-stack、未验证不得写」的禁区（见 [claim register](./bathtub-filter-claim-register.md) Banned 区、[产品架构假设](./bathtub-filter-kes-product-architecture-hypotheses.md) H1），但缺一个更工程化的回答：

> **催化活性炭（catalytic activated carbon）到底能不能在浴缸端 point-of-use 有效除 PFAS？「催化」这个卖点对除 PFAS 有没有贡献？**

本页把这个问题按「机理 → 长短链 → 接触时间 → 认证 → EPA 立场」拆开回答，作为 KES 站内 **PFAS ↔ 催化炭** 的边界口径源。结论供 SKU 决策与 copy 审查直接引用。

**方法说明**：本页结论来自 2026-07-01 一次深度研究（fan-out 检索 + 对抗式验证，见 §7 Validation log），主证据为 EPA 2024 BAT 官方文件、NSF 官方文档、多篇同行评审文献。

---

## 一句话结论

**「催化」对除 PFAS 没有任何贡献——活性炭除 PFAS 靠的是纯物理/化学吸附，催化炭与普通 GAC 在这件事上无本质差异；而且吸附对长链 PFAS 尚可、对短链几乎无效，浴缸端「高流速 + 低炭量 = 短 EBCT」恰恰是活性炭除 PFAS 最差的工况。**

推论：**「催化炭除 PFAS」是误导性 claim，不得写**；即便想打通用「PFAS reduction」，在浴缸形态也拿不出可信的成品去除率，且认证水平（~20 ppt）本身达不到 EPA 强制线（4 ppt）。**PFAS 应视为 RO / 专项 IX 的独立路线，不是浴缸滤芯路线。**

---

## 1. 「催化」不除 PFAS：机理正交（高置信度）

催化活性炭的「催化活性位」是为**一氯胺（NH₂Cl）/ H₂S 的催化分解**工程出来的（见 [催化炭滤材页](./site/bathtub-filter-kes-media-catalytic-carbon.md) §一）。它对 PFAS **不发生催化**——PFAS 的 C–F 键是自然界最强化学键之一，活性炭根本催化分解不了它。

- EPA 2024 BAT 官方文件（815R24011）在描述 GAC 除 PFAS 的机理时，**全文 `catalyt*` 出现 0 次**；机理被定性为**吸附 → 饱和穿透（breakthrough）**，归因于疏水作用与静电作用。
- 同行评审建模（Murray 2021）用孔表面扩散模型**纯以吸附动力学**刻画 GAC 除 PFAS，无催化项。
- NSF 官方只承认三类除 PFAS 技术：**GAC、离子交换（AER）、反渗透（RO）**——**未把「催化」活性炭列为独立或更优的 PFAS 去除机制**。

> **口径结论**：催化位点针对氯胺/H₂S，与 PFAS 去除**正交**。用「催化」给「除 PFAS」背书 = 张冠李戴。催化炭除 PFAS 的能力 = 同等物理参数普通 GAC 的能力，一分不多。

---

## 2. 长链尚可、短链几乎无效：链长效率梯度陡峭（高置信度）

活性炭吸附 PFAS 的效率随碳链长度单调变化。一项列柱研究的 10% 穿透床体积（bed volumes，越大越好）：

| PFAS | 碳链 | 10% 穿透床体积 | 去除能力 |
|---|---|---:|---|
| PFBA | C4 | ~6,000 | ❌ 差，近乎立即穿透 |
| PFPeA | C5 | ~11,000 | ❌ 差 |
| PFHxA | C6 | ~16,000 | ⚠️ 中 |
| PFHpA | C7 | ~20,000 | ⚠️ 中偏好 |
| PFOA | C8 | ~23,000 | ✅ 好 |
| PFOS | C8（磺酸）| 更高 | ✅ 好 |

机理：每增加一个 `-CF₂-` 单元，log 分配系数约升 0.50–0.60。短链疏水性弱、**增加投加量也压不住**（某批次实验 PFBA 仅从 18%→24%），容量耗尽时甚至出现「色谱位移」——**出水浓度反超进水**。

- EPA 口径：对长链 **PFOA/PFOS 最大去除率 >99%**（最佳设计条件下），但明确承认**短链 PFBS/PFBA 吸附不佳**。
- Pannu 2024：长链 PFOA/PFOS/PFHxS 去除良好，短链 **PFPeA/PFBA「立即穿透」不被去除**。

⚠️ **数据护栏**：网络流传的「PFOS 89% / PFOA 73% / PFBS 55% / PFBA 30%」这组百分比来自单篇球磨胶体活性炭的 **1 小时批次实验、1.0 mg/L 极高浓度（AFFF 源区条件）、误差棒很大**，**不能当作饮用水/点式场景的固定去除率**；只能引用其**定性趋势**（长链远优于短链），该趋势被多篇文献稳固佐证。而监管与污染趋势正持续往**短链**走——对活性炭越来越不利。

---

## 3. EBCT / 流速是决定性变量 → 点式浴缸场景最不利（高置信度）

空床接触时间（EBCT）与流速直接决定去除率与穿透时点：

- **EBCT 越短、流速越高 → 去除越差、穿透越早**（Murray 2021；Belkouteb 2020 全尺度水厂：流速从 39 降到 29 L/s，总 PFAS 去除率提升 6.5–14%）。
- 短链 PFAS 因**质量传递区（MTZ）更长**，需要**更长** EBCT 才能压住。
- GAC 吸附容量有限、随运行时间衰减：某全尺度滤床新床 92–100%，运行到 357 天（~29,300 床体积）时最低掉到 **7%**。

**对浴缸/淋浴滤芯的直接含义**：point-of-use 形态 = **高流速（bath-fill 甚至 25 L/min）+ 低炭量 = 极短 EBCT**，正好落在「去除差、穿透早」那一端。对照 [催化炭页](./site/bathtub-filter-kes-media-catalytic-carbon.md) §二：compact 滤芯连**除氯胺**都常达不到 4–5 分钟 EBCT 门槛，而 PFAS（尤其短链）需要的接触时间只多不少。

⚠️ **诚实边界**：**没有任何被证实的来源直接测过「淋浴/浴缸滤芯」这类具体产品**在其额定流速下的 PFAS 去除率。上述「点式无效」是从 EBCT/流速/MTZ 通用规律**强推**，不是直接实测（见 §7 开放问题）。但方向明确，不宜赌反面。

---

## 4. 认证现状：能证明「减量」，证明不了「达标」（高置信度）

| 事实 | 内容 | 对 KES 的含义 |
|---|---|---|
| **旧 P473 已废除** | 2017 年 NSF 把 P473 测试方法并入 **NSF/ANSI 53（活性炭/离子交换）** 与 **58（反渗透）**，P473 产品与引用被移除 | 供应商若还拿「P473 认证」说事 = 过期信息，须要求换算到 53/58 |
| **2022 年更新** | 新建「Total PFAS」减量声明，组合 PFAS 限值从 **70 ppt 降到 20 ppt** | 认证挑战/验证水平约 20 ng/L |
| **认证 ≠ 达标** | EPA / PA DEP 官方明说：现行认证标准**尚不能证明**滤芯能把 PFAS 降到 EPA 饮用水标准水平 | 见下 |
| **EPA 强制线** | 2024-04 最终 MCL：**PFOA、PFOS 各 4.0 ppt** | 认证的 ~20 ppt 与 4 ppt 差 5 倍 |

> **口径结论**：「通过 NSF/ANSI 53 认证」**只证明减量、不等于达到 EPA 安全标准**。任何把「NSF 认证」暗示成「达 EPA PFAS 标准」的表述都不成立。

---

## 5. EPA 立场与更优对照：GAC 是 BAT 之一，但不是短链最优（高置信度）

- EPA 把 **GAC 列为 PFAS 去除的最佳可行技术（BAT）之一**，与 **PFAS 选择性离子交换（IX）**、**反渗透/纳滤（RO/NF）** 并列；措辞为「潜在 BAT……成熟技术，已在众多设施全尺度处理 PFAS」，对 PFOA/PFOS 最大去除率 >99%。
- **但 GAC 不是短链 PFAS 的最优技术**：头对头中试（Water Research 2022，441 天平行柱）显示**阴离子交换树脂（AER）全面优于 GAC**，床寿命更长，**对短链优势尤其大**（Murray 2021：相同 5 分钟 EBCT 下，AER 处理床体积 PFOS 是 GAC 的 8 倍、PFOA 6 倍；短链 PFPeA 优势达 46:1）。

**含义**：即使 KES 未来真要做 PFAS，正确技术栈也是 **RO 或 PFAS 选择性 IX**，而不是（催化）活性炭——更不是浴缸端的一小撮炭。这与 [就地软水可行性](./bathtub-filter-point-of-use-hardness-softening-feasibility.md) 的结论同构：**真去除 = 独立设备路线，不是 compact bath filter 顺手加一层。**

---

## 6. 对 KES 的产品判断与 claim boundary

严格按 **problem → product → claim** 三层拆开。

### 6a. 三层判断

- **Problem（真实）**：PFAS 在部分水源真实存在且有监管/健康共识（如关岛军事基地污染区，见 [水源类型指南](./bathtub-filter-water-source-types-guide.md)）。这是真问题。
- **Product（形态不匹配）**：浴缸端高流速/低炭量形态，对 PFAS（尤其短链）去除**先天不利**；催化炭的「催化」对此**零加成**。
- **Claim（不成立）**：无成品测试、无达标能力、形态不利——三重不支持。

### 6b. claim boundary

**不应说（直接判不合规）：**

- ❌ 「catalytic carbon removes PFAS」/「催化炭除 PFAS」——机理误导，暗示「催化」在除 PFAS
- ❌ 「removes PFAS / forever chemicals」（无成品逐化合物测试）
- ❌ 「NSF certified for PFAS」暗示达 EPA 标准（认证只到 ~20 ppt，非 4 ppt）
- ❌ 把「除氯/氯胺」能力外推为「除 PFAS」

**即便日后有数据，最多也只能说（且需硬证据）：**

- ⚠️ 「partial reduction of long-chain PFAS (e.g. PFOA/PFOS) under specified flow」——须 **NSF/ANSI 53 成品认证 + 额定流速下第三方去除率**，且必带「reduction, not removal / 不达 EPA MCL」限定
- ⚠️ 短链 PFAS 一律不承诺

### 6c. 与现有 SKU 路线对齐

沿用 [就地软水可行性](./bathtub-filter-point-of-use-hardness-softening-feasibility.md) §6 的路线分法：

- **Route A（bath filter）**：游离氯/氯胺/气味/comfort —— **PFAS 不在其内**
- **PFAS 若要做**：只能是独立的 **RO / 专项 IX SKU**，与浴缸滤芯分开命名、分开背书

---

## 7. Validation log（2026-07-01 深度研究）

> 本页遵循「先测后写」约定：结论先经一次 fan-out 深度研究 + 对抗式验证（3 票制，2/3 反驳才否决），再落文档。

**已坐实（3-0 通过）：**

1. 「催化」对除 PFAS 无贡献，催化炭 ≈ 普通 GAC（机理正交）—— EPA BAT 文件 catalyt* 0 次 + Murray 2021 + NSF 三分类
2. 长链 >> 短链效率梯度（穿透床体积 PFBA ~6,000 → PFOA ~23,000）
3. EBCT/流速主导，短链需更长 EBCT → 点式高流速场景不利
4. NSF 53/58 取代 P473；组合限值 70→20 ppt；认证 ≠ 达 EPA 4 ppt
5. EPA 列 GAC 为 BAT 之一；AER 全面优于 GAC，短链优势尤大

**Caveats（写 copy 时必守）：**

- §2 那组「89/73/55/30%」是**高浓度批次实验**、误差大，**只引趋势不引数值**
- 无来源直测「淋浴/浴缸滤芯」产品 → §3 点式无效为**强推论非实测**
- 认证逐化合物限值（是否含短链、各限值）细节存不确定，须查标准全文而非二手概述
- 多数吸附数据来自市政/地下水基质，NOM/TOC 竞争会缩短穿透；点式自来水基质可能不同
- 时间敏感：EPA MCL 2024-04 生效、NSF 2022 版为当前活跃版——法规/认证会演进，引用需复核日期

**开放问题（未闭环，勿当已知）：**

1. 真实点式产品（淋浴/浴缸/水龙头/水壶滤芯）在额定短 EBCT 下的**实测 PFAS 去除率**为何？现有证据全是市政 GAC 柱/中试。
2. 市售标称「catalytic activated carbon」滤芯是否有**任何独立测试**显示其除 PFAS 优于同参数普通 GAC？（机理判无差异，但缺直接商业品类对比。）
3. NSF/ANSI 53 对 PFAS 减量的**完整测试条件**（挑战浓度、流速/EBCT、pH、竞争物、逐化合物限值与是否含短链）——须查标准全文。
4. 把水从典型自来水 PFAS 水平（常个位数~数十 ppt）降到 4 ppt MCL 这一**实际低浓度区间**，点式 GAC 能维持多久、多久换芯？EPA >99% 是最佳设计值，点式穿透寿命未量化。

---

## Sources

- [EPA (2024) — Final PFAS BAT / Small Systems Compliance Technologies, 815R24011](https://www.epa.gov/system/files/documents/2024-04/2024-final-pfas-bat-ssct_final-508.pdf)
- [NSF — Forever Chemicals & the Advancement of Filtration Standards (P473 → 53/58, Total PFAS 20 ppt)](https://www.nsf.org/knowledge-library/forever-chemicals-advancement-filtration-standards)
- [Murray et al. (2021) — GAC vs anion exchange for PFAS, EBCT / MTZ modeling](https://www.sciencedirect.com/science/article/abs/pii/S2214714421004293)
- [Belkouteb et al. (2020) — Full-scale GAC PFAS removal vs flow / bed volumes, Water Research](https://www.sciencedirect.com/science/article/pii/S0043135420304504)
- [Water Research (2022) — 441-day pilot: anion exchange resin outperforms GAC for PFAS](https://www.sciencedirect.com/science/article/abs/pii/S0043135422011435)
- [Pannu et al. (2024) — EBCT scaling / long- vs short-chain PFAS breakthrough, WER](https://onlinelibrary.wiley.com/doi/full/10.1002/wer.11035)
- [Environmental Sciences Europe (2023) — GAC (adsorption) vs AER (ion exchange) mechanisms](https://link.springer.com/article/10.1186/s12302-023-00716-5)
- [PMC — column study, chain-length breakthrough bed volumes (PFBA→PFOA)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11706541/)
- [PA DEP (restating EPA) — POU devices certified for PFAS reduction ≠ meeting EPA drinking-water levels](https://files.dep.state.pa.us/Water/DrinkingWater/Perfluorinated%20Chemicals/Point_of_Use_Devices_Certified_for_Reduction_of_PFAS_final.pdf)
- [Catalytic carbon media page (KES single source of truth)](./site/bathtub-filter-kes-media-catalytic-carbon.md)

## Obsidian links

- [[bathtub-filter-kes-media-catalytic-carbon]]
- [[bathtub-filter-point-of-use-hardness-softening-feasibility]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-water-source-types-guide]]
- [[bathtub-filter-certification-and-testing-pathways]]
- [[bathtub-filter-kes-product-architecture-hypotheses]]
