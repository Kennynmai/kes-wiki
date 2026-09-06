---
type: product
status: draft
owner: strategy
created: 2026-07-01
updated: 2026-09-05
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, v1, product-definition, not-for-list, scope, free-chlorine, primary-source]
source_count: 6
review_cycle: monthly
verification_status: spot-checked
related:
  - ../bathtub-filter-kes-v1-selling-points-and-pack-contents.md
  - ./bathtub-filter-kes-pack-contents-spec.md
  - ./bathtub-filter-kes-care-and-maintenance-guide.md
  - ../bathtub-filter-claim-register.md
  - ../bathtub-filter-kes-media-stack-options-by-water-type.md
  - ./bathtub-filter-kes-page-replacement-and-lifespan.md
  - ./bathtub-filter-kes-page-water-test-diagnosis.md
  - ./bathtub-filter-kes-scenario-free-chlorine.md
  - ./bathtub-filter-kes-structure-flow-diversion-module.md
---

# P1 · KES V1 产品定义与「不适用」清单

## 这一页是什么

这一页是 KES 浴缸过滤器 **V1（城市市政自来水 / 游离氯版）** 的对内 + 对外**真理源**：V1 到底是什么、为什么做了现在这些技术选择、以及它**明确不做什么**。

它把仓库里最重要的一手件——[**《浴缸过滤器\_城市市政自来水版202602讲解》原件**](../../../../raw/products/bathtub-filter/2026-06-18-desktop-source-folder-import/source-files/浴缸过滤器_城市市政自来水版202602讲解.md)（供应商/内部产品讲解，Version A 稳健合规版）——正式化为 wiki 页。凡本页正文引用「讲解件」处，均指该 raw 原件（双向溯源）。

> **口径纪律**：护栏一律以 [claim-register](../bathtub-filter-claim-register.md) 为准。本页只做「定义 + 边界」，不新造去氯数字 / 寿命曲线（那些在 [T3 更换与寿命页](./bathtub-filter-kes-page-replacement-and-lifespan.md)）。每条 claim 标 🟢（可直接用）/ 🟡（待补 / 待溯源）/ 🔴（禁区）。

---

## 一、一句话定位（承重定位句）

> **这不是净水器，不以降低 TDS 为目标。**
> 这是「浴缸注水场景的末端除游离氯模块」，解决泡澡体验的核心问题。（2026-09-05 改：原「净化 / 减害」自带健康框架）

🟢 对外可用措辞（照 register Positioning 行原文保留英文）：

> "This is not a water purifier. It does not target TDS reduction. It is an end-stage free-chlorine reduction module for the bath-fill scenario."

来源：讲解件 §0「一句话定位」。register 要求这句**出现在每个客户可见表面**（页面 / 包装 / 说明书 / 客服话术），用来先手挡掉「它能降 TDS 吗」的异议。

---

## 二、V1 是什么：目标分层

据讲解件 §0，V1 的价值分四层，卖点顺序也照此排（先体感、再信任、再长期）：

| 层级 | 内容 | 等级 | 备注 |
|---|---|---|---|
| **主目标：快速去游离氯** | 新滤芯 best-experience 段整机总游离氯去除可达 99%+ → 氯味不刺鼻、刺激感更低 | 🟢 定位 / 🟡 数字 | 数字须带「fresh-filter / best-experience」+ 流量限定词；**必须写 free chlorine**，见 register Chlorine-reduction 行 |
| **辅目标：拦截杂质（可视化）** | 过滤棉（PET）拦铁锈 / 沉积物 / 黑点，滤棉变色让用户看到过滤在工作 | 🟢 | 「白→黄 / 挂杂质」是信任证据 |
| **安心层：KDF55 末端把关 + 抑膜** | KDF55 做末端风险把关 + 抑制滤芯**内部**生物膜（抑味 / 抑黏 / 更稳定） | 🟢 结构 / 🟡 具体百分比 | 不宣传杀菌率；抑膜是**柱内**属性，不得说「杀死浴缸水里的细菌」 |
| **功能扩展：浴盐溶解 / 阻垢** | 底部装载仓：浴盐均匀溶解，或阻垢抑垢 | 🟢 溶解 / 🔴 软化 | **阻垢不去除溶解盐，TDS 可能上升；不软化** |

### 为什么「先讲去氯」（讲解件 §1）

城市用户真实痛点排序决定了卖点顺序：

1. **氯味刺鼻**（热水更明显，浴室空间小放大）
2. **泡澡后干燥紧绷**（38–42℃ 热水 + 长时间浸泡放大刺激）
3. **偶发杂质黑点 / 铁锈 / 沉积物**（肉眼可见，影响信任）

→ 卖点顺序：**先去氯（体感最大）→ 再杂质可视化（信任最强）→ 再安心层（长期价值）**。

---

## 三、为什么用「快反应去氯」（核心技术选择）

浴缸注水 = **热水 + 大水量 + 大流量**，属于「短接触时间系统」。据讲解件 §4，单层 EBCT 极短：

| 注水流量 | 单层 EBCT |
|---|---:|
| 15 L/min | 约 0.95 s |
| 20 L/min | 约 0.71 s |
| 25 L/min | 约 0.57 s |
| 30 L/min | 约 0.48 s |

🟢 因此技术分工是硬约束：

- **去氯主力必须是快反应介质 CaSO₃（亚硫酸钙，化学中和）** —— 唯一能在亚秒级接触时间里扛住大流量去氯的角色。
- **KDF55 更适合做「把关 / 抑膜」的长期价值层**，去氯只是加分项，不作主力去游离氯层。

> 内部一句话（讲解件 §4）：**短 EBCT 系统必须靠 CaSO₃ 做去氯主力；KDF 做把关 / 抑膜长期价值。**

### 为什么不走「混装滤料」（讲解件 §3.0）

竞品常见「多种滤材装同一腔体」，在浴缸大流量下三个不可控：**沟流（channeling）水走捷径**、**快 / 慢反应介质互相抢工负荷失衡**、**无法定位失效层只能整体更换**。KES 的解法是**分层分工 + 结构整流（顶部分流槽 + KDF 层中央实心柱）+ 可视化验证**（结构真理源见 [[bathtub-filter-kes-structure-flow-diversion-module]]、[[bathtub-filter-kes-structure-transparent-housing]]）。

🟢 对外可用（照 register head-to-head 行，讲设计选择、不点名竞品）：

> "Strict layered media (polyester (PET) fiber → KDF55 → CaSO3) with an internal flow-diversion module — water passes each layer in order instead of channeling around it."

---

## 四、V1 固定配置（当前边界）

> （2026-07-02 按 [V1 BOM 表](../bathtub-filter-v1-free-chlorine-removal-dimensions-materials.md) 裁定更正：KDF55/CaSO₃ 克数互换、滤棉 PET、浴盐仓 250 mL）

🟢 V1 = **过滤棉（PET）→ KDF55 130g → CaSO₃ 110g → 浴盐 / 阻垢装载仓**，分层不混（讲解件 §3.1；[卖点页](../bathtub-filter-kes-v1-selling-points-and-pack-contents.md)）。

| 层（从上到下） | 料量 | 角色 | 等级 |
|---|---|---|---|
| 防溢接水仓（白壳，含主挂带） | — | 承接龙头出水、引导入滤仓；目标 ≤30 L/min 不溢出（讲解件 §3.11）| 🟢 |
| 过滤棉（PET 聚酯纤维） | 20 块随盒 | 物理拦截、可视化变色 | 🟢 |
| KDF55 环形滤床（透明壳）| **130g**，5–10 目，仓有效高 14 mm（BOM）；🟡 **实际装填高度待工程确认**（按几何核算约 5–6 mm），上下 60 目 304 网夹持 | 末端把关 + 抑膜 + 寿命稳定 | 🟢 |
| CaSO₃ 亚硫酸钙球（透明壳）| **110g**，3–4mm 球，仓有效高 14 mm（BOM，约 11–14 mm 装填），上下 40 目 304 网夹持 | **主力去游离氯 KPI** | 🟢 |
| 多功能装载仓（白壳）| 方案A 浴盐 250ml / 方案B 阻垢剂 | 浴盐溶解 / 阻垢 | 🟢 溶解 / 🔴 软化 |

> V1 **不含活性炭**。「no pre-rinse / no carbon dust / 酸洗椰壳炭」属其它含碳版本资料，不纳入 V1（🔴 register banned：wrong-version claim）。

---

## 五、明确「不适用 / 不支持」清单（本页核心）

这张表是 V1 对内对外统一的**能力边界**。凡越界的表达一律回到本表 + [claim-register](../bathtub-filter-claim-register.md) banned 区。

| 不支持项 | 为什么不支持 | 归属 / 去向 | 等级 |
|---|---|---|---|
| **氯胺（chloramine）去除** | V1 媒体（KDF55+CaSO₃）对氯胺基本无效；化学机理不匹配 | 属 **V1.5 / Version B**：催化炭芯 + 抗坏血酸钠浸泡双段（见 [[bathtub-filter-kes-media-stack-options-by-water-type]] 方案B、[[bathtub-filter-kes-scenario-chloramine]]）| 🔴 V1 禁 / 🟡 V1.5 conditional |
| **软化硬水 / 降 TDS / PPM / 硬度** | 去氯是化学中和不是 RO；阻垢方案甚至可能让 TDS 上升。**产品决策（2026-07-01）：本产品不做软化，硬水只提供阻垢剂选项** | 阻垢只能作 anti-scale adjunct，**必带「不软化」承重句**；真软化属**全屋软水器品类（非 KES 这类浴缸滤芯）**——不夸大、不留"软化版"钩子（见 [[bathtub-filter-kes-scenario-hard-water-scale]]）| 🔴 |
| **PFAS（全氟 / 多氟「永久化学品」）去除** | 催化炭对 PFAS 机理正交、贡献 ≈ 普通 GAC，短链几乎无效，浴缸短 EBCT 最不利；市场「炭除 PFAS」是误导 | 属 **RO / 离子交换独立路线**，非浴缸炭路线；诚实说明「我们不除 PFAS」（见 [[bathtub-filter-kes-edu-pfas-and-bath-filters]]、[[bathtub-filter-point-of-use-pfas-removal-feasibility]]）| 🔴 |
| **井水处理（铁 / H₂S / 硝酸盐 / 砷 / 铀 / 高铁全屋替代）** | 井水通常无游离氯，主问题是铁 / 硫 / 沉积，媒体错位 | 属 **Version C / well-water**：KDF85 主导（见 [[bathtub-filter-kes-scenario-well-water]]）| 🔴（V1 范围外）|
| **除重金属作健康保护** | KDF 除铅仅为料级 24h 静态浸泡测试参考；不适用 bath-fill 条件 | 仅作规格表脚注，**不进营销文案**（register KDF lead-reduction 行）| 🔴 健康化 / 🟡 料级仅参考 |
| **杀菌 / 除菌率宣称** | KDF 抑菌是**柱内 24h 动态**属性；浴缸 EBCT 仅 0.48–0.95s，短 5–6 个数量级 | 只能说「抑制滤芯**内部**生物膜 / 减少异味发黏」| 🔴 浴水杀菌 / 🟢 柱内抑膜 |
| **婴儿安全 / baby-safe** | 无「去除有害物 → 婴儿安全」的证据基础 | 情感 framing 可（「许多家庭把浴缸过滤器用于对氯敏感的洗澡routine」），**「safe for babies / newborns」🔴 禁** | 🔴 safe-claim / 🟡 framing |
| **eczema / 湿疹改善、任何皮肤病 / 健康疗效** | 成品对湿疹疗效在真实条件下无可信证据 | 只能停在感官 / comfort（「feels different」OK，「improves your skin」NOT OK）| 🔴 |
| **「purifies / 净化」/ 广谱污染物去除 / 临床 / 医生推荐** | 缺实质性证明；FTC / FDA 硬边界 | 一律禁 | 🔴 |
| **universal fit / 适配所有浴缸** | 实测有兼容边界；swan-neck / 短出水 / 异形出水嘴需 workaround | 每条兼容 claim 必带「不支持」边界（见 [[bathtub-filter-supported-spout-matrix]]）| 🔴 |
| **「patented / 专利技术 / 获得专利」** | KES 仅 1 项模块化滤仓结构**申请中**，未授权 | 对外只能 "Patent pending"，**且须受理文件确认后**（见 [[bathtub-filter-kes-structure-ip-and-patent-governance]]）| 🔴 patented / 🟡 pending |

### 适用范围声明（scope）

🟢 V1 范围 = **US urban municipal（free-chlorine）tap water only**。任何可能被读成全球通用或氯胺城市兼容的表面都要改写（register How-to-use §6）。

---

## 六、滤料标准边界（不踩雷的价值感）

据讲解件 §2，KDF55 与 CaSO₃ 来自具 NSF 相关标准体系语境的材料体系，但**必须严格区分料级 vs 整机**：

- 🟢 **KDF55**：有供应商 material-level **NSF/ANSI 42** 支撑（不是 KES 成品认证）。
- 🟢 **CaSO₃**：按 **NSF/ANSI 177** protocol 做游离氯**测试参考**；**CaSO₃ 本身无 NSF 认证，KES 成品也不声称 NSF 认证**。
- 🔴 **滤料标准 / 材料验证 ≠ 整机 NSF 认证**（整机需另送检）。不得把料级说成成品认证。

🟢 对外可用措辞（照 register Performance/testing 行原文保留英文，故意保守）：

> "KDF55 media is backed by supplier NSF/ANSI 42 material-level listing. CaSO3 has NSF/ANSI 177-protocol free-chlorine reference testing, but CaSO3 itself is not NSF-certified and the finished product is not NSF-certified. Verify with the included free-chlorine test strip."

---

## 七、护栏摘要（本页承重红线）

1. **free chlorine 限定** —— 去氯 claim 一律写 free chlorine，不写 total chlorine / chloramine（🔴）。
2. **成品未 NSF 认证免责** —— 料级支撑 ≠ 整机认证，永远随行「finished product is not NSF-certified」。
3. **不软化** —— 阻垢 ≠ 软化，TDS 可能上升，「不软化」是承重 disclaim。
4. **氯胺仅 V1.5** —— V1 一律禁氯胺去除；催化炭 + 抗坏血酸钠双段属 V1.5 conditional。
5. **不认领 eczema / 健康 / 婴儿安全** —— 停在感官 / comfort framing。
6. **去氯数字须带限定** —— 「fresh-filter / best-experience」+ 流量，且数字口径不在本页新造（见 T3）。

> 完整台账见 [claim-register](../bathtub-filter-claim-register.md)（Allowed / Conditional / Banned 三区 + 表面→claim 映射）。

---

## Sources

- **一手 primary source**：[`浴缸过滤器_城市市政自来水版202602讲解.md`](../../../../raw/products/bathtub-filter/2026-06-18-desktop-source-folder-import/source-files/浴缸过滤器_城市市政自来水版202602讲解.md)（Version A 稳健合规产品讲解件，§0 定位 / §1 痛点 / §2 标准 / §3 结构 / §4 EBCT / §7 FAQ / §8 话术）
- [卖点与套装内容页](../bathtub-filter-kes-v1-selling-points-and-pack-contents.md)
- [claim-register](../bathtub-filter-claim-register.md)（护栏真理源）
- [按水源类型的滤材方案页](../bathtub-filter-kes-media-stack-options-by-water-type.md)（V1/V1.5/井水三 SKU 边界）
- [T3 更换与寿命页](./bathtub-filter-kes-page-replacement-and-lifespan.md)（去氯 / 寿命数字口径）
- [结构 / IP 治理页](./bathtub-filter-kes-structure-ip-and-patent-governance.md)（patent-pending 措辞）

## Obsidian links

- [[bathtub-filter-kes-v1-selling-points-and-pack-contents]]
- [[bathtub-filter-kes-marketing-site-content-map]]
- [[bathtub-filter-kes-pack-contents-spec]]
- [[bathtub-filter-kes-care-and-maintenance-guide]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-kes-media-stack-options-by-water-type]]
- [[bathtub-filter-kes-page-replacement-and-lifespan]]
- [[bathtub-filter-kes-page-water-test-diagnosis]]
- [[bathtub-filter-kes-scenario-free-chlorine]]
- [[bathtub-filter-kes-scenario-chloramine]]
- [[bathtub-filter-kes-scenario-well-water]]
- [[bathtub-filter-kes-structure-flow-diversion-module]]
- [[bathtub-filter-kes-structure-transparent-housing]]
- [[bathtub-filter-kes-structure-ip-and-patent-governance]]
- [[bathtub-filter-supported-spout-matrix]]
