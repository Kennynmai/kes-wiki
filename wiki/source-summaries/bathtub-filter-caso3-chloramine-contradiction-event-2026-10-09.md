---
type: source-summary
status: draft
owner: strategy
created: 2026-10-09
updated: 2026-10-09
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, chloramine, monochloramine, supplier-evidence, onlyzone, calcium-sulfite, caso3, contradiction-event, first-party-testing, control-design]
source_type: vendor-material
extraction_mode: structured
review_cycle: monthly
verification_status: spot-checked
source_count: 2
aliases:
  - 亚硫酸钙氯胺测试
  - CaSO3 chloramine test
  - 宗立氯胺报告
  - Onlyzone chloramine report
  - 一氯胺 三氯铵 测试
name_zh: 来源摘要｜亚硫酸钙 × 氯胺 矛盾事件（2026-10-09）
name_en: Source Summary — Calcium Sulfite × Chloramine Contradiction Event (2026-10-09)
related:
  - ./bathtub-filter-onlyzone-supplier-material-evidence-2026-04-17.md
  - ./bathtub-filter-kes-internal-product-materials-2026-04-17.md
  - ../products/bathtub-filter/bathtub-filter-chloramine-media-research.md
  - ../products/bathtub-filter/bathtub-filter-disinfectant-types-and-media-guide.md
  - ../products/bathtub-filter/bathtub-filter-media-efficacy-at-bath-conditions.md
  - ../products/bathtub-filter/bathtub-filter-claim-register.md
  - ../products/bathtub-filter/bathtub-filter-evidence-bibliography.md
  - ../products/bathtub-filter/bathtub-filter-assumption-register.md
  - ../playbooks/bathtub-filter-validation-testing-protocol.md
  - ../../raw/products/bathtub-filter/2026-10-09-caso3-chloramine-contradiction-pass.md
---

# 来源摘要｜亚硫酸钙 × 氯胺 矛盾事件（2026-10-09）

## Why this source matters

> **与前次 ingest 的关系。** 供应商报告本体已于 **2026-06-17** 从另一台工作站 ingest 过：raw 归档 `raw/products/bathtub-filter/2026-06-17-zongli-calcium-sulfite-chloramine-test/`、归档页 [[bathtub-filter-supplier-report-zongli-calcium-sulfite-chloramine-2023-07]]、来源摘要 `./bathtub-filter-zongli-calcium-sulfite-chloramine-test-2023-07.md`。那次评估的结论是「值得验证的供应商信号」，并起草了待供应商澄清清单（含三氯铵命名问题）。**本页的新增量**：① KES 一方 bench test 这个第二数据点；② 对供应商报告的定量批判（进水衰减混淆、容量利用率 0.61%、EBCT 测算、去除率反算）；③ 把两个数据点合起来裁定为矛盾事件；④ playbook Module 7 受控测试规格。

两份新材料同时指向一个与 wiki 现有结论**相反**的方向，因此这是一次 **contradiction event**，不是 gap fill：

1. **供应商报告** `ZONET20230707001`（淄博宗立内部实验室，2023-07-13 完成）：50 g 2–3 mm 亚硫酸钙球沐浴过滤器，对**一氯胺**报告 93.26%–100% 去除，对**三氯铵**报告 100% 去除。
2. **KES 一方 bench test**（2026-10-09）：4 ppm 氯胺水经 130 g 亚硫酸钙，流速 24 L/min，60 s，38 °C，测得**接近 0**。

现有 wiki 立场（[[bathtub-filter-chloramine-media-research]] Section 3）是 CaSO₃ 对一氯胺 `❌ No removal expected`，且 [[bathtub-filter-claim-register]] 把 chloramine claim 列入**禁区**。

**这份摘要的立场是：现有结论可能仍然正确，但它的论证基础已经站不住。** 详见「这次真正改变了什么」。

---

## Extracted facts / observations

### 1）供应商报告 ZONET20230707001 — 提取原样

- **出具方**：淄博宗立新材料科技有限公司，盖章为「检验专用章」（**供应商内部实验室**）
- **样品编号**：`ZONET20230707001`；接收 2023-07-07，完成 2023-07-13
- **样品名称**：沐浴过滤器；**样品描述**：内置滤料为 50 g 宗立（2–3 mm）亚硫酸钙球
- **检测项目**：加标测试（氯胺）；**方法**：出水流速分别为 5 L/min、3 L/min，滤芯接入通水设备

| 累计水量 | 流速 | 项目 | 过滤前 mg/L | 过滤后 mg/L | 去除率 % |
|---|---|---|---|---|---|
| 300 L | 5 L/min | 一氯胺 | 0.46 | 0.0184 | 96 |
| | | 三氯铵 | 1 | 0 | 100 |
| 500 L | | 一氯胺 | 0.341 | 0.023 | 93.26 |
| | | 三氯铵 | 0.728 | 0 | 100 |
| 300 L | 3 L/min | 一氯胺 | 0.43 | 0 | 100 |
| | | 三氯铵 | 1 | 0 | 100 |
| 500 L | | 一氯胺 | 0.341 | 0 | 100 |
| | | 三氯铵 | 0.728 | 0 | 100 |

**报告未披露**：分析方法、检出限/定量限、**pH**、水温、TDS、氯物种确认、复测次数、**对照组**、突破曲线。

### 2）KES 一方 bench test — 提取原样

| 参数 | 数值 |
|---|---|
| 介质 | 亚硫酸钙 130 g（与 Version A 装填量一致）|
| 流速 | 24 L/min |
| 接触时间 | 60 s |
| 水温 | 38 °C |
| 进水 | 4 ppm 氯胺 |
| 读数方式 | 总氯比色卡（0.1–10 mg/L）|
| 结果 | 氯胺**接近 0** |

> **照片序列警告**：第二张照片标注「原水」，但显示的比第一张（标注「4 ppm 绿氨水」）**更清澈**。两个标签不可能描述同一份水。照片顺序存在歧义，不应作为 before/after 证据使用；只有报告的数值参数可用。

### 3）本轮计算出的定量交叉核对

**容量利用率**（CaSO₃ 中 SO₃ 质量分数 66.6%；1 mol SO₃ 还原 1 mol NH₂Cl，即 1.19 g SO₃ / g NH₂Cl；堆积密度取说明书 0.9–1.1 g/cm³）：

| 来源 | 理论 NH₂Cl 容量 | 累计负荷 | **容量利用率** |
|---|---|---|---|
| ZONET20230707001 | 50 g → ~28 g NH₂Cl | 500 L × 0.341 mg/L = 170.5 mg | **0.61%** |
| KES bench test | 130 g → ~73 g NH₂Cl | 24 L × 4 mg/L = 96 mg | **0.13%** |

**两份测试都没有触及容量。** 它们都是「大试剂过量下的存在性证明」，是效能类证据中最弱的一种形式，也是两者都不能被放大成寿命模型的原因。

**接触时间 EBCT**：

| 工况 | 床体积 | 流速 | **EBCT** |
|---|---|---|---|
| 供应商报告 | 50 cm³ | 5 L/min | **≈0.60 s** |
| 供应商报告 | 50 cm³ | 3 L/min | **≈1.00 s** |
| KES bench test | 130 cm³ | 24 L/min | **≈0.33 s** |

**关键观察**：KES 那次是在供应商最慢点的**约三分之一接触时间**下、**量产装填量**、**量产浴缸流速与水温**条件下读到的接近 0。如果供应商数据成立，KES 那次才是更难解释的那一个。这是对该假设**有利**的最强单点论据，不应被丢弃。

**供应商报告中的衰减混淆**：进水本身不恒定——一氯胺 0.46 → 0.341（−25.9%），三氯铵 1.0 → 0.728（−27.2%），在 60–167 分钟内两个物种同步衰减约 26–27%。**没有报告任何配对时间点的纯进水空白**。自衰减的加标氯胺溶液会产生完全相同的模式，也会产生「0」的出水读数。报告没有任何内容能区分「介质去除」与「加标衰减」。这是 ZONET20230707001 最大的缺陷。

**去除率列不携带独立信息**：0.46 → 0.0184 恰好等于 96.00%，0.341 → 0.023 恰好等于 93.26%。另注意精度异常——`0.0184`（4 位有效数字）夹在 2–3 位有效数字的进水值和其他 2–3 位的出水值之间，与「出水值是为凑目标百分比而反算」的形态一致。

---

## Caveats / ambiguity

### 1）化学上的三方不可判定

Tier-1 锚点 Yiin / Walker / Margerum (1987) 报告 NH₂Cl + 亚硫酸根的反应为 general-acid-assisted 且**强烈依赖 pH**：pH 8.5 时亚硫酸氢钠「无效」，pH 4.0 时很快。**两份新数据都没有报告 pH。** 报告无法区分三种情形：

1. **测试在酸性 pH 下进行** → 化学真实，与 Yiin 1987 完全一致，但对 pH 7.5–8.5 的市政水**零信息量**。
2. **测试在中性–碱性 pH 下进行且效应真实** → 这将真实地与 Yiin 1987 在 CaSO₃ 层面冲突（可能源于多孔球体表面催化或微量金属催化），但未获证明。
3. **效应是假象** —— 加标衰减、游离氯干扰、或低于检出限的填报。

### 2）物种命名问题（引用前必须向供应商澄清）

**三氯铵（NCl₃）在 0.728–1.0 mg/L 不是现实的自来水物种。** NCl₃ 是氯化副产物，在配水系统中通常以 ng/L–µg/L 计。约 1 mg/L 的挑战浓度比文献报道的饮用水水平高约三个数量级，且 NCl₃ 本身不稳定、浓态具冲击敏感性。

两种可能：（a）供应商实际指的是**二氯铵**（NCl₂H）而标注错误；（b）挑战液不具任何代表性。

这一点很关键——[[bathtub-filter-disinfectant-types-and-media-guide]] 已经基于「pH>8 时罕见」把二氯胺/三氯胺**排除在产品模型之外**。如果标注有误，那么报告中最亮眼的那组数字（100%×4）对应的物种，是 KES 根本没有建模过的。

### 3）KES bench test 的方法学缺陷

**总氯比色卡不是氯胺特异性方法。** 无法归因于氯胺：从未测过游离氯。如果 4 ppm 挑战液中同时存在游离氯，亚硫酸钙会优先消耗游离氯，比色卡照样读近零。

因此「接近 0」的准确含义是 **≤0.1–0.2 mg/L**，即去除 **>95–97.5%**，不是 100%，也不是测得的零。

其余缺口：无纯进水对照（38 °C 下氯胺本身会衰减）、无惰性介质对照（未控制床层压降/流阻）、无 pH、单点单次、无氯离子质量平衡。

### 4）溯源与实体注意事项

- **实体名——已于 2026-10-09 澄清**：印章为「淄博宗立**新材料**科技有限公司」，wiki 规范名为「淄博宗立 / Zibo Onlyzone **Water Treatment** Technology Co., Ltd」。**KES 于 2026-10-09 确认二者为同一法人主体**，是中英文名称的两种写法，不存在 certificate-holder 歧义，无需再做法人核对。规范对照见 `governance/entity-canonicalization.md`。
- **报告时效**：`ZONET20230707001` 比去氯基准报告 `ZONET20251113001` 早约 2.3 年，比当前早约 3.3 年，很可能描述的是**上一代**介质。
- **SKU 不匹配**：50 g / **2–3 mm** 属于 `ZONE-CL-A01 Gen-4` 尺寸段；KES Version A 用 `ZONE-CL-A02 Gen-3` **3–4 mm** / 130 g。不同代、不同粒径段、不同装填量。
- **流速工况不匹配**：供应商是淋浴/手持工况（3–5 L/min）；KES Version A 是浴缸注水（15–30 L/min，典型 18–25 L/min）。供应商较慢、接触更长的工况比 KES 设计点**更有利**。
- **分析人可追溯性**：`ZONET20230707001` 无机器可读的检测/批准人姓名；`ZONET20251113001` 有（马艳华 / 陈加森）。本报告溯源性更弱。

---

## 这次真正改变了什么

### 变了：现有 wiki 立场被过度陈述了——这是本次最重要的发现

[[bathtub-filter-chloramine-media-research]] 的 Gap #2 已经写明了自己的论证基础：

> "No peer-reviewed study measuring CaSO₃ + NH₂Cl reaction rate. **The expected ineffectiveness is inferred.**"

这是**把「没有找到数据」当成「已测得无效」**。该页正文自己承认在「任何同行评审或行业来源」中都找不到 CaSO₃ + NH₂Cl 的定量数据，然后把这份沉默当成了反面证据的证据。

现在出现了**两个独立的、反向的观测**——其中一个是在量产装填量、量产浴缸流速、量产浴缸水温下得到的。那个 ❌ 单元格所声明的基础已经站不住，**即使它的结论仍然为真**。

**建议的重新标注（不是反转）**：该单元格从「❌ No removal expected」改为「⚠️ Untested — 两个无对照观测，均为正面，但均不足以支撑」。禁区条目**保留**；但禁区记录的理由从「chemistry mismatch」改为「chemistry mismatch 存在争议且未解决；两个方向都没有受控证据」。

### 没变：Version A 的范围、模型与宣称今天全部不变

- [[bathtub-filter-media-efficacy-at-bath-conditions]] Section 9 仍然是**游离氯**模型。两个无对照的氯胺存在性证明不能延展它。
- [[bathtub-filter-claim-register]] 的 chloramine 条目**留在禁区**。本次没有产生任何能越过任何 claim 门槛的新证据。
- 假设 **A-14**（V1 推迟氯胺地区）不受影响——它从来不是化学假设，而是 claim 可辩护性假设，该假设依然完全成立。

### 一个新的高价值实验被解锁了

**氯离子质量平衡**。如果氯胺被真实还原为氨，每 1 mol NH₂Cl 被破坏就释放 1 mol Cl⁻。离子色谱测氯离子是成熟、廉价、且**对物种不敏感**的方法，完全免疫于加标衰减这个混淆因素——因为它测的是反应的**产物**，不是底物。

测：进水 Cl⁻、无介质空白在配对时间/温度下的 Cl⁻、出水 Cl⁻。如果出水氯离子的增量恰好等于比色卡所隐含的去除量，则结论成立；如果不是，那个颜色下降就是衰减或干扰。

**这一个对照，比任何进一步的比色法都更能定案。** 在本次 pass 之前它不在 R&D 清单上，因为没有人有理由相信 CaSO₃ 值得测。

最小协议见 raw pass 文件的「The decisive control」章节（4 个臂：介质 / 无介质衰减空白 / 惰性介质水力空白 / 生产规格 3–4 mm；pH 7.0/7.8/8.5；20/38/42 °C；做**到突破的连续序列**而非单点；n≥3；先书面澄清一氯胺/二氯铵/三氯铵）。

---

## Affected pages

| 页面 | 本次处理 |
|---|---|
| `wiki/products/bathtub-filter/bathtub-filter-chloramine-media-research.md` | 新增 Section 3.5 矛盾事件；Gap #2 由「无数据」改为「无受控数据」；Summary 表 CaSO₃ 行重新标注；Sources 增补 |
| `wiki/products/bathtub-filter/bathtub-filter-evidence-bibliography.md` | 新增 E6（ZONET20230707001）、E7（KES bench test） |
| `wiki/products/bathtub-filter/bathtub-filter-claim-register.md` | 禁区 chloramine 行理由更新；新增 status note |
| `wiki/products/bathtub-filter/bathtub-filter-disinfectant-types-and-media-guide.md` | 介质矩阵 CaSO₃ 氯胺列重新标注；标注 trichloramine 命名风险 |
| `wiki/products/bathtub-filter/bathtub-filter-media-efficacy-at-bath-conditions.md` | Section 9 open 限制中「CaSO₃ 对氯胺基本无效」加限定；Section 8 gap #3 加限定 |
| `wiki/products/bathtub-filter/bathtub-filter-assumption-register.md` | A-14 证据强度补注 |
| `wiki/playbooks/bathtub-filter-validation-testing-protocol.md` | 新增受控 CaSO₃ 氯胺测试条目 |
| `ops/ingestion-registry.md` | 新增 ingestion 行 |
| `ops/verification-queue.md` | 新增矛盾事件条目（high stakes）|
| `index.md` / `log.md` | 索引与日志 |

---

## Sources

- 原始提取：[2026-10-09-caso3-chloramine-contradiction-pass.md](../../raw/products/bathtub-filter/2026-10-09-caso3-chloramine-contradiction-pass.md)
- 供应商报告 `ZONET20230707001`，淄博宗立新材料科技有限公司，2023-07-13 完成 — 本地文件 `/Users/moltbot/Downloads/宗立测试-一氯胺及三氯铵 50g亚硫酸钙球.docx`
- [Onlyzone 供应商材料证据 2026-04-17](./bathtub-filter-onlyzone-supplier-material-evidence-2026-04-17.md) — 供应商实验室身份、CaSO₃ 堆积密度 0.9–1.1 g/cm³、SKU 映射、`ZONET20251113001`
- Yiin BS, Walker DM, Margerum DW. "Nonmetal redox kinetics: general-acid-assisted reactions of chloramine with sulfite and hydrogen sulfite." *Inorganic Chemistry.* 1987;26(21):3435–3441 — DOI 10.1021/ic00268a006
- [[bathtub-filter-chloramine-media-research]]
- [[bathtub-filter-disinfectant-types-and-media-guide]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-media-efficacy-at-bath-conditions]]
