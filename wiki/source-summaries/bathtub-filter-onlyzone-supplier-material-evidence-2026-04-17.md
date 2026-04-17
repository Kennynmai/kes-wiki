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
domains: [bathtub-filter, supplier-evidence, onlyzone, kdf55, calcium-sulfite, material-level-certification, nsf42, eu-food-contact]
source_type: vendor-material
extraction_mode: structured
review_cycle: one-shot
verification_status: spot-checked
related:
  - ../products/bathtub-filter/bathtub-filter.md
  - ../products/bathtub-filter/bathtub-filter-media-efficacy-at-bath-conditions.md
  - ../products/bathtub-filter/bathtub-filter-technology-notes.md
  - ../products/bathtub-filter/bathtub-filter-evidence-bibliography.md
  - ../products/bathtub-filter/bathtub-filter-claim-register.md
  - ../products/bathtub-filter/bathtub-filter-certification-and-testing-pathways.md
  - ../playbooks/bathtub-filter-validation-testing-protocol.md
  - ./bathtub-filter-kes-internal-product-materials-2026-04-17.md
  - ../../raw/products/bathtub-filter/2026-04-17-onlyzone-supplier-material-evidence-pass.md
---

# 来源摘要｜Onlyzone（宗立）媒体供应商材料证据（2026-04-17）

## Obsidian links
- [[bathtub-filter]]
- [[bathtub-filter-media-efficacy-at-bath-conditions]]
- [[bathtub-filter-technology-notes]]
- [[bathtub-filter-evidence-bibliography]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-certification-and-testing-pathways]]
- [[bathtub-filter-validation-testing-protocol]]
- [[bathtub-filter-kes-internal-product-materials-2026-04-17]]

## Source
- 原始抓取：[2026-04-17-onlyzone-supplier-material-evidence-pass.md](../../raw/products/bathtub-filter/2026-04-17-onlyzone-supplier-material-evidence-pass.md)
- 7 份 PDF + 2 份产品手册（KDF-55 + CaSO₃ 球 + 长效碱性球），均由 product strategist 2026-04-17 提供
- 供应商：**淄博宗立 / Zibo Onlyzone Water Treatment Technology Co., Ltd**（山东淄博）

## 这份来源是什么
Onlyzone 是 KES Version A 的**单一媒体供应商**（KDF55 + CaSO₃）。这份材料是 Onlyzone 提供的 7 份证明文件 + 3 份产品手册，用来支撑 supplier-level claim（材料级证据），区别于 finished-KES-product 级别的证据（仍欠缺）。

**最关键的单一发现**：文件 #5（宗立 CaSO₃ 余氯去除报告 ZONET20251113001，2025-12-26 完成）**就是 Version A 寿命模型的 reference report**——即 KES Doc 1 里多次引用但未附原始数据的"宁立 40g / 0.5–1mm / 8 L/min / 2 ppm"底数。本 pass 已将该表格完整记录，并对 η=0.9 × 3.25 = 2.925× 的缩放规则做了 **4 档逐点验证，全部命中 Version A 公布数据**。

## 提取出的关键信息

### 1）η=0.9 缩放数学已通过逐点验证（4/4 命中）

| 阈值 | 供应商 last ≥ 点 | 供应商 first < 点 | 线性插值（L）| × 2.925 | Version A 文档值 | 是否吻合 |
|---|---|---|---|---|---|---|
| ≥99% | 1020 L @ 99.2% | 1870 L @ 98.2% | 1,190 | **3,481 L** | 3,481 L | ✅ |
| ≥95% | 5780 L @ 95.5% | 6460 L @ 94.2% | 6,042 | **17,673 L** | 17,672 L | ✅ |
| ≥90% | 6460 L @ 94.2% | 7650 L @ 82.3% | 6,880 | **20,124 L** | 20,124 L | ✅ |
| ≥50% | 8670 L @ 52.9% | (未观测，外推) | 8,707 | **25,467 L** | 25,467 L | ✅ |

**插值规则**（Version A 内定）：使用"**最后一个 ≥ 阈值的点 → 第一个明确 < 阈值的点**"线性插值；忽略非单调反弹（报告中 4760 L 跌到 92.6% 后 5780 L 反弹到 95.5%，规则取 5780 L 作为"最后一个 ≥95%"）；≥50% 在数据末端做线性外推。

**含义**：η=0.9 的 **数学追溯性已建立**。之前标注为"未验证的缩放假设"——现在降级为"**数学一致但物理假设未第三方验证**"：
- ✅ 缩放规则、供应商源数据、Version A 寿命表 三者 numerically closed
- ⏳ η=0.9 **作为物理效率假设** 仍未经第三方 finished-product 复测
- ⏳ **粒径差异未被显式处理**：供应商测试用 0.5–1 mm CaSO₃；Version A 生产使用 **3–4 mm**。更大粒径 = 更少比表面 = 动力学更慢。η=0.9 是否已隐式吸收此差异是未知的

### 2）材料级认证与测试清单

| # | 文件 | 发证方 | 日期 | 范围 | 能支撑什么 claim | 不能支撑什么 |
|---|---|---|---|---|---|---|
| 1 | NSF Certificate C0843384-01 | NSF International | 2025-04-10 | **组织级** 列入 NSF/ANSI 42 | "我们的 KDF55 来自 NSF/ANSI 42 listed 供应商" | **不能**说 KES finished product 通过 NSF 认证 |
| 2 | EU food-contact 721682290C | TÜV SÜD Shanghai | 2023-07-13 | KDF55 bronze-zinc alloy，22 重金属 + 感官 | "KDF55 介质通过 EU food-contact（CM/RES 2013/9 + Reg 1935/2004 Ch.III）" | 不能声称 KES 成品 food-contact certified |
| 3 | KDF 抑菌报告 WJ20221264 | 广州微生物研究所（CNAS L0823 / ilac MRA） | 2022-04-20 | KDF 合金 ASTM E 2149-2020，24h 动态接触，金黄色葡萄球菌 ATCC 6538 | "KDF 媒体在 24h 动态接触下对 *S. aureus* 减少 >99.99%"；可**支撑** Version A "KDF 作为生物膜抑制层" 定位 | **不能**说 "KES 过滤器会杀死洗澡水中的细菌"（浴缸 EBCT 比此测试短 5-6 个数量级）|
| 4 | KDF Pb 去除 FM250616-30 | 浙江弗里斯 FSDA | 2025-06-23 | 100g 材料 + 100g 铅溶液，**静态浸泡 24h**，64.7→4.8 μg/L | "KDF55 材料在 24h 静态浸泡下展示 92.6% 铅去除" | **不能**说 "产品去除 92.6% 铅"（静态浸泡 vs 流通动力学差异巨大；Version A EBCT 0.48–0.95 s） |
| 5 | CaSO₃ 余氯参考报告 ZONET20251113001 | 淄博宗立内部实验室 | 2025-12-26 | 40g 0.5–1mm，8 L/min，2.0±0.2 mg/L 自由氯 | 是 Version A 寿命模型的 **reference baseline** | 内部实验室非第三方；粒径与生产规格不同 |
| 6 | CaSO₃ 产品手册 | Onlyzone | 未注明 | 三代 SKU + 产品参数 | 介质规格可追溯到 ZONE-CL-A02 Gen-3 3–4mm | 手册非检测报告 |
| 7 | KDF-55 产品手册 | Onlyzone | 未注明 | SKU + 参数 + 手册内 200g@7 L/min 70–80% 氯去除测试 | 支撑 "KDF 在此流速下去氯率约 70–80%" 量级 | 手册非检测报告 |
| 8 | 长效碱性球手册 | Onlyzone | 未注明 | pH 提升 + 寿命 10,000 L+ | 可作为 optional loading-cavity 备选 | **与 Version A "不以 TDS 为目标" 定位冲突**——碱性球会提升 pH 和 TDS |

### 3）KDF 手册自测数据（200g / 7 L/min / 0.15 mg/L 自由氯）
| L | In | Out | 去除率 |
|---|---|---|---|
| 10 | 0.15 | 0.04 | 73.33% |
| 30 | 0.15 | 0.042 | 72.00% |
| 50 | 0.15 | 0.045 | 70.00% |
| 130 | 0.15 | 0.029 | 80.67% |

**对照 Version A EBCT 表**（内部经验系数 43/32/26/21% for 15/20/25/30 L/min）：
- 手册 7 L/min 下去氯 70–81%，流速更慢（EBCT 更长）
- Version A 15–30 L/min 去氯贡献系数 21–43%，流速更快（EBCT 更短）
- **两组数据方向一致**（流速越低 KDF 贡献越高），但手册数据集中在慢速/低氯/大质量条件，不能直接外推到浴缸注水场景

### 4）CaSO₃ 手册自测数据（20g Gen-3 1.5–2mm / 8 L/min / 0.39 mg/L 自由氯）
| L | In | Out | 去除率 |
|---|---|---|---|
| 2690 | 0.39 | <0.01 | >96.87% |
| 4320 | 0.39 | 0.02 | 94.67% |
| 5760 | 0.38 | 0.01 | 96.07% |
| 8640 | 0.38 | 0.05 | 83.33% |
| 11520 | 0.38 | 0.06 | 82.76% |
| 15120 | 0.38 | 0.06 | 80% |

**差异点**：与参考报告（40g / 0.5–1mm / 2 mg/L）相比，手册使用 **更小质量（20g）+ 更大粒径（1.5–2mm）+ 更低氯（0.39 vs 2 mg/L）**。低氯低质量组合下寿命仍到 15,000 L 以上 80%——与"CaSO₃ 在低氯条件下寿命非线性延长"一致。

### 5）长效碱性球的 scope 决策（与 Version A 冲突点）
供应商的 PH-A03 碱性球是 loading-cavity 的可选 mineral pack。但它：
- **提升 pH** 至 9–10（初始 6.43）
- **TDS 明显变化**（从 32 下降到 19 —— 这是 ion-exchange 迁移而非"不影响 TDS"）
- Version A Doc 1 verbatim 位置语是 "不以降 TDS 为目标"；若增加这个 upgrade，**不是"不影响 TDS"**，而是"将 TDS 从 32 减到 19"——方向巧合地"好像 KES 不做的事"，但本质上会让用户以为产品"会改水质"

**建议**：
- V1 Version A **不含** 长效碱性球（维持纯末端减害定位）
- 若未来出 Version A+ "mineral enhancement" SKU，**必须显式声明**"本 SKU 会改变 pH 与 TDS；与标准 Version A 的末端减害定位分开"
- 不要把它隐性塞进 loading-cavity 说 "optional mineral pack"——容易让用户读错整个产品定位

## 这份来源的局限
- **Supplier-level only**：所有证据停在介质级，不等于 finished-KES-product 级。供应商测试条件（静态 / 特定流速 / 特定粒径）与浴缸注水场景差距显著
- **NSF/ANSI 42 是组织列名**，不是具体 KES 产品列名；KES 想要成品 NSF cert 仍需独立申请（见 [bathtub-filter-certification-cost-and-timeline-estimates](../products/bathtub-filter/bathtub-filter-certification-cost-and-timeline-estimates.md)）
- **CaSO₃ 参考报告由供应商内部实验室出具**，非独立第三方；如果 KES 要对外发布寿命曲线，需要补第三方复测
- **粒径差异**（0.5–1 mm 参考 vs 3–4 mm 生产）是 η=0.9 里未被单独处理的变量；应补一轮以 3–4 mm 生产规格为样品的内部或第三方测试
- **Pb 和抑菌测试都是 24h 静态**，完全不对应浴缸 EBCT 0.48–0.95 s；此类报告**只能支撑"材料具备 X 能力"**，**不能支撑"产品在使用场景下实现 X"**

## 建议下一步（已在 wiki 执行）
1. ✅ media-efficacy Section 9：把 η=0.9 从 "未验证的缩放假设" 升级到 "数学已验证，物理假设未第三方复测"，并新增粒径差异 open gap
2. ✅ evidence-bibliography：新增 5 条 supplier-level 证据条目
3. ✅ claim-register：Pb / 抑菌 / food-contact / NSF 42 四条 conditional wording 写入，带显式"material-level only" caveat
4. ✅ certification-and-testing-pathways：NSF/ANSI 42 supplier listing 记录为支持层，但明确不等同于 finished-product cert
5. ✅ validation-testing-protocol Module 1："third-party CaSO₃ dechlor reference" 从 ⏳ 改为 ✅ **supplier-side only**，并新增 "3–4 mm 生产规格复测" 作为新 ⏳
