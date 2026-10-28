---
type: source-summary
status: draft
owner: strategy
created: 2026-10-09
updated: 2026-10-28
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

> **与前次 ingest 的关系。** 供应商报告本体已于 **2026-06-17** 从另一台工作站 ingest 过：raw 归档 `raw/products/bathtub-filter/2026-06-17-zongli-calcium-sulfite-chloramine-test/`、归档页 [[bathtub-filter-supplier-report-zongli-calcium-sulfite-chloramine-2023-07]]、来源摘要 `./bathtub-filter-zongli-calcium-sulfite-chloramine-test-2023-07.md`。那次评估的结论是「值得验证的供应商信号」，并起草了待供应商澄清清单（含三氯铵命名问题）。**本页的新增量（2026-10-28 注：第 ① 项已退出氯胺证据）**：① KES 一方 bench test 这个第二数据点；② 对供应商报告的定量批判（进水衰减混淆、容量利用率 0.61%、EBCT 测算、去除率反算）；③ 把两个数据点合起来裁定为矛盾事件；④ playbook Module 7 受控测试规格。

两份新材料同时指向一个与 wiki 现有结论**相反**的方向，因此这是一次 **contradiction event**，不是 gap fill：

> ⚠️ **2026-10-28 追记（先行提示）**：第 2 项（KES 一方 bench test）的加标物种**不可确认**，**已退出氯胺证据**。下面的「两份」应读作「一份」。详见文末 2026-10-28 追记。

1. **供应商报告** `ZONET20230707001`（淄博宗立内部实验室，2023-07-13 完成）：50 g 2–3 mm 亚硫酸钙球沐浴过滤器，对**一氯胺**报告 93.26%–100% 去除，对**三氯铵**报告 100% 去除。
2. **KES 一方 bench test**（2026-10-09）：4 ppm 氯胺水经 130 g 亚硫酸钙，流速 24 L/min，60 s，38 °C，测得**接近 0**。

现有 wiki 立场（[[bathtub-filter-chloramine-media-research]] Section 3）是 CaSO₃ 对一氯胺 `❌ No removal expected`，且 [[bathtub-filter-claim-register]] 把 chloramine claim 列入**禁区**。

**这份摘要的立场是：现有结论可能仍然正确，但它的论证基础已经站不住。** 详见「这次真正改变了什么」。

> ⚠️ **2026-10-28 状态更新 —— 本页的一半证据已退场。**
> 工单「2026-10-09 KES bench test 试剂身份」回查完成：第 2 项（KES 一方 bench test）的**加标液物种身份不可确认**，推定为游离氯路径，**已退出氯胺证据**。因此上面「两份新材料同时指向相反方向」的表述现在**只剩第 1 项（供应商报告）成立**；KES 自有的氯胺数据点为 **0**。本页的裁定（⚠️ 未验证 / 禁区 / A-14）**不变**，但支撑基础变窄。详见文末「2026-10-28 追记」与 [raw pass](../../raw/products/bathtub-filter/2026-10-28-caso3-2026-10-09-reagent-identity-check.md)。

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
| **加标试剂身份** | **未记录 —— 2026-10-28 回查后确认「不可确认」，该数据点已退出氯胺证据**（见下文 2026-10-28 追记）|
| **实测日期** | **≤2026-09-24**（同一批照片于 2026-09-24 已在群内发出，md5 逐张相同）；2026-10-09 是**汇报日** |

> **照片序列说明（2026-10-28 已更正）**：原注记称「第二张标注『原水』却比标注『4 ppm 绿氨水』的第一张更清澈，两个标签不可能描述同一份水」——**该判断是误判，已撤回**。原水是未加标的自来水（本来就该无色），4 ppm 加标液为粉红，出水为无色，**三张照片与所述协议逐张对应，不存在矛盾**。保留的真实限制：第 2、3 张均为无色，**目视无法分辨哪张是原水、哪张是出水**，因此照片仍不能单独证明 before/after（但原因是「分不出来」，不是「标注自相矛盾」）。详见 raw pass 的 2026-10-28 更正记录。

### 3）本轮计算出的定量交叉核对

**容量利用率**（CaSO₃ 中 SO₃ 质量分数 66.6%；1 mol SO₃ 还原 1 mol NH₂Cl，即 1.19 g SO₃ / g NH₂Cl；堆积密度取说明书 0.9–1.1 g/cm³）：

| 来源 | 理论 NH₂Cl 容量 | 累计负荷 | **容量利用率** |
|---|---|---|---|
| ZONET20230707001 | 50 g → ~28 g NH₂Cl | 500 L × 0.341 mg/L = 170.5 mg | **0.61%** |
| KES bench test | 130 g → ~73 g NH₂Cl | 24 L × 4 mg/L = 96 mg | **0.13%** |

**两份测试都没有触及容量。**（2026-10-28：KES 一方那份已退出氯胺证据；这一条对**剩余**的供应商报告依然成立）它们都是「大试剂过量下的存在性证明」，是效能类证据中最弱的一种形式，也是两者都不能被放大成寿命模型的原因。

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

Tier-1 锚点 Yiin / Walker / Margerum (1987) 报告 NH₂Cl + 亚硫酸根的反应为 general-acid-assisted 且**强烈依赖 pH**：pH 8.5 时亚硫酸氢钠「无效」，pH 4.0 时很快。**两份新数据都没有报告 pH**（2026-10-28：KES 一方那份已退出氯胺证据；供应商那份的这一缺陷依然成立）。报告无法区分三种情形：

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

## 2026-10-15 追记：第三个数据点，且挑战物身份错误

> 增量来源：[来源摘要｜氯胺T 实测报告评估（2026-10-15）](./bathtub-filter-chloramine-T-measurement-2026-10-15.md)｜[raw pass](../../raw/products/bathtub-filter/2026-10-15-chloramine-T-measurement/pass.md)

2026-10-15 又做了一次 KES 一方 bench test，报告**无氯胺去除**（读数不降：0.5–1 ppm 起，356 L / 712 L / 1068 L 均为 1 ppm；19 L/min，29 °C，总氯比色卡）。

**但这个数据点不能算作「第三次观测」，因为挑战物身份错了。** 试剂是**氯胺 T**（CAS 127-65-1，N-氯对甲苯磺酰胺钠，**固体缓释消毒剂**，水中水解生成 HOCl），**不是一氯胺**（CAS 10599-90-3，NH₂Cl）。它测的是**游离氯去除**——而那件事 KES 已在 2026-03-20 测得 84–90%，本次「无下降」反而与自有数据冲突（指向旁通/取样/读数错误）。

### 因此，本页第 2 项数据点的物种身份需要回查

上文 §2 记录的 2026-10-09 KES bench test，挑战液口径写的是「4 ppm 氯胺」，**未写明物种**。

> ⚠️ **待办（2026-10-15 新开）**：向该次测试的操作者书面确认所用试剂是**一氯胺标准液**，还是**氯胺 T**。若是后者，则该次「接近 0」的结果同样是游离氯去除，而非氯胺去除 —— 那么本页的「矛盾事件」就**根本不是矛盾事件**，而是**两次同向的自由氯观测**，且氯胺方向上至今零数据。

这一条不改变本页的任何裁定（Section 6 立场、禁区、A-14 全部不变），但它可能**抽掉矛盾事件本身的事实基础**。在试剂身份确认前，「两个方向相反的观测」这个表述应视为**待验证**。

### 状态小结（2026-10-15）

| 项 | 状态 |
|---|---|
| 本页裁定（CaSO₃ 保持 ⚠️ 未验证、禁区、A-14） | **全部不变** |
| 「两个方向相反的观测」 | **待验证** — 10-09 的试剂身份未确认 |
| 可解释的受控 CaSO₃ × 氯胺数据点 | **仍为 0 个** |
| 新增方法学要求 | 加标试剂身份须书面确认；照片比色数据不得跨图比较（见 [[bathtub-filter-validation-testing-protocol]] Module 7）|

> **状态更新：本节列出的待办已于 2026-10-28 结案** —— 试剂身份回查结论为「不可确认」，该数据点退出氯胺证据。见下节「2026-10-28 追记」。

---

## 2026-10-28 追记：试剂身份回查完成 —— 本页的一半证据退场

> 增量来源：[raw pass｜2026-10-09 KES bench test 加标试剂身份回查](../../raw/products/bathtub-filter/2026-10-28-caso3-2026-10-09-reagent-identity-check.md)｜[照片归档](../../raw/products/bathtub-filter/2026-10-09-caso3-chloramine-bench-test-photos/README.md)
>
> 工单来源：`ops/verification-queue.md` 中 2026-10-15 开出的**高优先级**条目「（跨页）2026-10-09 KES bench test 试剂身份」。

### 答案不是「是氯胺 T」或「是一氯胺」，而是「不可确认」

2026-10-28 按工单做了三件事：① 找回 2026-10-09 的**原始钉钉会话**；② 把三张一手照片**首次归档进 raw**；③ 检索 2026-08→10 全部 IM 中关于挑战液配制、试剂、标液的记录。

**结论：没有任何记录能确认那次挑战液是什么物种。**

| 证据 | 内容 | 来源 |
|---|---|---|
| 操作者自述（10-12 14:15） | 「我们自己测试氯胺是可以过滤的（**用其他方法配比出来的，没有实验室氯胺标液准，也有可能我们配出来的是错误**）」| 单聊 Kenny Mai ↔ 麦家浚 |
| KES 内部唯一有记录的「氯胺」试剂 | 「氯胺（**用氯胺T去配2ppm**）」——10-14 测试方案 | 同上 |
| 操作者自述（10-14 11:17） | 「**这个氯胺是无法确认是一氯胺还是什么**」，并把对外口径收缩为 free chlorine only | 同上 |
| 物证 | 三张照片中**无试剂瓶 / 无 CAS / 无配比**；试管手写只有容量标记 | 照片归档 |
| 10-15 测试 | 试剂写明为**氯胺 T** | 同上 |

### 裁定

> **2026-10-09 的 KES 台架是一次「未确认物种的加标氯测试」。按 KES 内部唯一有记录的氯胺试剂（氯胺 T）与操作者自述，其去除去向推定为游离氯，而非氯胺。该数据点不得再作为氯胺证据引用。**

**不说「已证明是氯胺 T」** —— 记录不支持这个强度。

### 这一裁定改了什么

| 之前 | 之后 |
|---|---|
| 「两个方向相反的观测」 | **该表述撤回**：只剩供应商报告一条 |
| KES 一方 bench test =「最难解释的那一点」「支持假设的最强单点论据」 | **撤回**：它描述的若是游离氯去除，本就该近零——KES 2026-03-20 已自测 84–90%，**不构成任何稀罕性** |
| KES 氯胺数据点 = 2 条观测 | **= 0 条**（唯一物种写明的是供应商报告，但其自带衰减混淆、无 pH、去除率反算） |
| 「照片序列内部矛盾」 | **撤回**（是误判；照片与协议逐张对应）——见上文 §2 的更正 |
| 「KES 一方 bench test（2026-10-09）」 | **实测 ≤2026-09-24**，10-09 是汇报日（同一批照片 md5 逐张相同）|

### 没有改什么

**本页裁定全部不变**：CaSO₃ × 氯胺格维持 **⚠️ 未验证**；claim **禁区维持**；假设 **A-14** 不变；Version A 寿命模型不变；Tier-1 化学（Yiin 1987）未被推翻。

**为什么 ⚠️ 仍然成立（而不是退回 ❌）**：Gap 2 原文承认「The expected ineffectiveness is **inferred**」——把「没找到数据」当反面证据，这一步确实无效。而供应商 `ZONET20230707001` 仍是一条**物种写明**（一氯胺 / `三氯铵`）的正向观测，尽管它无 pH、无对照、无方法、无检出限、进水自衰减 −26%、去除率列为反算。**一条不足以支撑宣称，但足以说明「不是已知无效」。**

### 顺带回答了组织一直在问的第三方检测问题

10-12 11:57 麦家浚给出实验室报价与口径：**广州微生物研究所按国标 `GB/T 5750.11-2023` 执行，「只能给出总氯胺，没有细分到一氯胺、二氯胺、三氯化氮」**；游离氯 800 元/点位、氯胺 1000 元/点位（另有全程加标 9000 / 10000 元、点加标 4000 / 5000 元两档）。

**含义**：**国标路线给的是「总氯胺」，不物种拆分** —— 即便花钱做国标氯胺测试，**依然无法证明测的是一氯胺**。Module 7 所需的 **DPD 自由/化合区分 + 离子色谱测 Cl⁻ 是国标之外的加项**，询价时必须单独写明，否则会拿到一份「总氯胺」数字而误当作物种确认。已写入 [[bathtub-filter-validation-testing-protocol]] Module 7。

### owner 答复（2026-10-28，当日）

**① 接受裁定。** 10-09 台架**正式退出氯胺证据**；本裁定（CaSO₃ 氯胺格 ⚠️ 未验证、claim 禁区、A-14 不变）生效。**KES 自有的物种确认氯胺数据点 = 0**，作为后续一切氯胺讨论的事实前提。

**② 包装与电商页面确认无「除氯胺 / chloramine removal / 秒去」字样在流通。** 配合本轮 wiki 内巡检（`site/` 页面与 claim 台账口径为**禁**）—— **对外文案无改动需求**，本次裁定反而**加强**了这条禁令的依据。

**仍开放的两项事实性问题**（不是裁定的一部分，需补事实而非补判断）：

| # | 事项 | 归属 |
|---|---|---|
| ③ | 2026-09-24「可以讲，直接亚硫酸钙即可，无需要 ACF」这个架构结论是否重审 —— 其唯一支撑即被降级的照片，**证据基础已空** | 产品侧（本次未改任何架构页）|
| ④ | 2026-10-12「亚硫酸钙量只有 20g 左右（拆样板所见）」与台架 130 g、V1 BOM 110 g 是否同一对象（取数口径问题，**本次不据此改动任何计算**）| 产品侧 |
| ⑤ | Module 7 排期与询价口径（规格已更新，含「物种拆分是加项」提示与 2026-10 报价锚点）| strategy |

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

### 2026-10-28 试剂身份回查的受影响页面

| 页面 | 本次处理 |
|---|---|
| `raw/products/bathtub-filter/2026-10-28-caso3-2026-10-09-reagent-identity-check.md` | **新建** —— 证据链、裁定、影响面、留给 owner 的问题 |
| `raw/products/bathtub-filter/2026-10-09-caso3-chloramine-bench-test-photos/` | **新建** —— 三张一手照片首次入 raw + 溯源 README（md5 显示与 09-24 群内同发图逐张相同）|
| `raw/products/bathtub-filter/2026-10-09-caso3-chloramine-contradiction-pass.md` | 加「更正记录（2026-10-28）」：数据点退出氯胺证据、照片误判撤回、实测日期口径修正 |
| `wiki/products/bathtub-filter/bathtub-filter-chloramine-media-research.md` | §3.5 标题与正文（「两个观测」→「一条」+ 撤回最强论据）、§6 汇总表 CaSO₃ 行、§7 Gap 2 / Gap 6、§8、Sources |
| `wiki/products/bathtub-filter/bathtub-filter-evidence-bibliography.md` | E7 重新定性（氯胺证据 → 物种不可确认的自由氯路径推定）；E6 补注 |
| `wiki/products/bathtub-filter/bathtub-filter-claim-register.md` | status note 加 2026-10-28 追记；禁区行理由同步收紧 |
| `wiki/playbooks/bathtub-filter-validation-testing-protocol.md` | Module 7：前提修正（只剩一份数据）、新增「国标只给总氯胺」的加项提示与成本锚点、新增「标称浓度必须由物种特异性方法读出」现场纪律 |
| `ops/verification-queue.md` | 高优先级工单结案 + 遗留条目重写 |
| `ops/ingestion-registry.md` | 新增本次回查行；10-15 行 next_action 更新 |
| `index.md` / `log.md` / `dashboards/recent-updates.md` | 索引、日志、看板 |

---

## Sources

- 原始提取：[2026-10-09-caso3-chloramine-contradiction-pass.md](../../raw/products/bathtub-filter/2026-10-09-caso3-chloramine-contradiction-pass.md)
- **2026-10-28 试剂身份回查**：[2026-10-28-caso3-2026-10-09-reagent-identity-check.md](../../raw/products/bathtub-filter/2026-10-28-caso3-2026-10-09-reagent-identity-check.md)｜[照片归档与溯源](../../raw/products/bathtub-filter/2026-10-09-caso3-chloramine-bench-test-photos/README.md)
- 供应商报告 `ZONET20230707001`，淄博宗立新材料科技有限公司，2023-07-13 完成 — 本地文件 `/Users/moltbot/Downloads/宗立测试-一氯胺及三氯铵 50g亚硫酸钙球.docx`
- [Onlyzone 供应商材料证据 2026-04-17](./bathtub-filter-onlyzone-supplier-material-evidence-2026-04-17.md) — 供应商实验室身份、CaSO₃ 堆积密度 0.9–1.1 g/cm³、SKU 映射、`ZONET20251113001`
- Yiin BS, Walker DM, Margerum DW. "Nonmetal redox kinetics: general-acid-assisted reactions of chloramine with sulfite and hydrogen sulfite." *Inorganic Chemistry.* 1987;26(21):3435–3441 — DOI 10.1021/ic00268a006
- [[bathtub-filter-chloramine-media-research]]
- [[bathtub-filter-disinfectant-types-and-media-guide]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-media-efficacy-at-bath-conditions]]
