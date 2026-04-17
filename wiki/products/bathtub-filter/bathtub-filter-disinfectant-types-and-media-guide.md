---
type: product
status: draft
owner: product
created: 2026-04-17
updated: 2026-04-17
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, disinfectant, chlorine, chloramine, filtration-media, technology, claims]
source_count: 14
review_cycle: monthly
verification_status: spot-checked
related:
  - ./bathtub-filter-technology-notes.md
  - ./bathtub-filter-water-jurisdiction-demand-map.md
  - ./bathtub-filter-certification-and-testing-pathways.md
  - ./bathtub-filter-claim-register.md
  - ./bathtub-filter-evidence-matrix.md
---

# Bathtub Filter 消毒剂种类与滤材指南

## ⚠️ 本页仅覆盖市政供水的消毒剂种类
> 私人井水用户（约 2,300 万美国家庭）通常**没有氯胺或游离氯**。他们的主要问题是铁、氢硫化物（硫磺臭味）、硬度——与市政用水用户完全不同。详见：[[bathtub-filter-well-water-research]]

---

## 为什么有这页
"氯"不是单一的化学物质。用户水龙头里的"氯"可能是三种完全不同的化学形态之一，每种形态的去除方式截然不同。市面上大量 bathtub / shower filter 产品的 claim 混淆了这一点——声称"removes chlorine"却未说明是哪种。

这页整理：
- 水处理中实际使用的消毒剂类型及其在龙头水中的形态
- 每种形态对应哪些滤材有效、哪些无效
- 对 KES 产品设计与宣称的直接含义

---

## 1. 消毒剂类型：从水厂到龙头

### 1a. 加氯处理剂（水厂端）
美国市政水厂使用三种主要投氯形式，但这三种在水中形成**完全相同的龙头端化学形态**：

| 水厂投加形式 | 化学式 | 龙头端形态 |
|------|------|------|
| 液氯（氯气） | Cl₂ | 游离氯（HOCl + OCl⁻）|
| 次氯酸钠（漂白水） | NaOCl | 游离氯（HOCl + OCl⁻）|
| 次氯酸钙 | Ca(OCl)₂ | 游离氯（HOCl + OCl⁻）|

> **对产品的含义：** 使用上述任何一种投加形式的城市，龙头处的消毒剂形态是相同的。滤材选择上没有区别。

**游离氯的 pH 依赖性（影响去除难度）：**
- pH < 7.5：HOCl 占主导（活性更强，更易氧化滤材）
- pH > 7.5：OCl⁻ 占主导（反应活性较弱）
- 美国自来水 pH 通常为 7.0–8.5，HOCl 通常占游离氯的 30–70%

### 1b. 氯胺（Chloramine）
约 35–40% 的美国市政系统（超过 20% 的美国人口）使用氯胺作为配水管网的持续消毒剂。

**形成机制：**
NH₃ + HOCl → NH₂Cl（一氯胺）+ H₂O — 反应在投加后约 1 分钟内 90% 完成

龙头端主要形态：**一氯胺（Monochloramine, NH₂Cl）**

> 二氯胺（NHCl₂）和三氯胺（NCl₃）在 pH > 8 且 Cl:N 比例正常的系统中极少出现，不构成龙头端的主要问题。产品层面假设氯胺 = 一氯胺即可。

**为什么水厂要用氯胺？**
- 减少消毒副产物（三卤甲烷 THMs、卤乙酸 HAAs）——这些物质受 EPA 法规限制
- 氯胺更稳定，在配水管网中衰减更慢，可维持更长距离的余氯
- 代价：更难被终端过滤器去除

### 1c. 二氧化氯（Chlorine Dioxide, ClO₂）
- 约 300–400 家美国水厂有 ClO₂ 设备，约 5% 的大型水厂使用
- 约 1,200 万美国人有 ClO₂ 接触
- **ClO₂ 不是"氯"**：它是一个独立的气态分子（ClO₂），不会水解为 HOCl 或 OCl⁻
- 在水中，50–70% 的 ClO₂ 转化为亚氯酸盐（ClO₂⁻）；龙头端可能同时含有 ClO₂ 和 ClO₂⁻
- MRDL：ClO₂ 0.8 mg/L；MCL：ClO₂⁻ 1.0 mg/L
- 通常用于**预处理**（去除铁/锰/异味），之后仍以游离氯或氯胺维持管网余氯
- **滤材的好消息：** 普通活性炭对 ClO₂ 和 ClO₂⁻ 的去除效果良好（Johns Hopkins 研究：2 分钟 EBCT 可有效去除所有 ClO₂、ClO₂⁻ 和游离氯残留）

### 1d. 非氯消毒（臭氧 / UV）
- 臭氧（O₃）和 UV 在配水系统中无法维持残余消毒剂，必须配合二次消毒
- **臭氧 + 氯胺**是常见组合（洛杉矶等城市）：龙头端只含氯胺，对产品来说与纯氯胺系统无区别
- **UV + 游离氯**：龙头端只含游离氯，处理同标准游离氯城市

---

## 2. 滤材效能矩阵

| 滤材 | 游离氯 | 一氯胺 | 二氧化氯（ClO₂）| 备注 |
|------|------|------|------|------|
| **标准活性炭（GAC）** | ✅ 优秀 | ⚠️ 差至中等 | ✅ 有效 | 对氯胺的去除需要 3–4× 更长接触时间；热水下吸附容量下降 40–60% |
| **催化活性炭** | ✅ 优秀 | ✅ 较好至优秀 | ✅ 有效 | 专为化学降解一氯胺改性；最好的氯胺去除媒体；仍需充足接触时间 |
| **亚硫酸钙（Calcium Sulfite）** | ✅ 优秀（热水稳定）| ❌ 无效 | ❓ 可能有效（无数据）| 氧化还原机制专门针对游离氯；不能断裂 N–Cl 键 |
| **KDF-55（铜锌合金）** | ✅ 优秀 | ❌ 无效（实测 18.2%）| ❓ 部分有效（无数据）| 同上；实测氯胺去除率极低 |
| **KDF-85** | ✅ 优秀 | ❌ 无效（实测 1.4%）| ❓ 部分有效 | 比 KDF-55 对氯胺更差 |
| **维生素 C（抗坏血酸）** | ✅ 极速（瞬时）| ✅ 有效（需 4+ 分钟接触）| ✅ 有效 | 与一氯胺反应半衰期约 4 分钟；1,000 mg 可中和一整缸浴水中的氯胺（SFPUC 建议量）|
| **维生素 C（抗坏血酸钠）** | ✅ 极速 | ✅ 有效（同上）| ✅ 有效 | pH 中性，不酸化浴水；对 pH 敏感用户更友好 |
| **催化炭 + 维生素 C 组合** | ✅ 优秀 | ✅ 最强防守 | ✅ 优秀 | 最宽谱的组合方案 |

### 关键量化数据
- 维生素 C 与一氯胺反应半衰期：**~4 分钟**（浴缸注水过程通常 5–10 分钟，接触时间充足）
- 淋浴过滤器接触时间：**< 1 秒**（无法满足维生素 C 与氯胺的反应时间要求）
- **浴缸过滤器的结构性优势**：注水过程提供数分钟接触时间，维生素 C 和催化炭去除氯胺在浴缸场景是可行的，在淋浴场景基本不可行

---

## 3. 季节性切换：氯胺城市的游离氯窗口

约 **25–40% 的氯胺城市**每年临时切换回游离氯处理数周（EPA 2016 年调查数据）。

**为什么要切换：**
氯胺在管网末端衰减后会释放游离氨；亚硝化细菌（*Nitrosomonas* 等）以此为能量来源，造成管网内消毒剂余量下降，即"硝化反应（nitrification）"。游离氯的更强氧化活性可以杀灭生物膜中的这些细菌，配合消防栓冲洗，恢复管网卫生。

**切换规律：**
- 时间：通常在**春季**（夏季高温前）
- 持续：通常 **2–8 周**
- 通知：部分城市官方公告（如 DC Water 每年公布），多数城市仅在官网发布，不主动通知用户

**已知切换的城市示例：** DC Water（每年 3–5 月）、格林斯博罗 NC、德克萨斯部分城市

**对产品的含义：**
- 氯胺城市用户在切换期间接触的是游离氯，可能突然闻到"泳池味"
- 同时覆盖游离氯 + 氯胺的产品（维生素 C 或催化炭）在切换前后都有效，不出现断档
- 仅针对游离氯的产品，在切换回氯胺后性能下降，但用户难以察觉

---

## 4. 宣称含义（按龙头端消毒剂类型）

### 游离氯城市（拉斯维加斯、凤凰城、芝加哥、纽约等）
- 任何常规滤材（活性炭、KDF、亚硫酸钙、维生素 C）均可有效工作
- **可防守的宣称：** "减少游离氯"
- NSF/ANSI 177 认证在测试条件上与实际使用场景相符（测试用游离氯）

### 氯胺城市（洛杉矶、休斯顿、丹佛、DC 等）
- 有效滤材：**催化活性炭**（需要充足接触时间）+ **维生素 C**（浴缸注水场景有足够接触时间）
- 无效滤材：标准 GAC（接触时间不够）、KDF、亚硫酸钙
- **可防守的宣称：** "减少一氯胺（化合氯）"——需要明确说明是氯胺，不能仅写"removes chlorine"
- **不可支撑的宣称：** 使用标准 GAC 或 KDF 的产品声称"removes chloramine"

### 不确定或季节性切换城市
- 最优产品配方：维生素 C + 催化活性炭组合
- **最宽谱的可防守宣称：** "减少游离氯和氯胺——无论您所在地区使用哪种消毒方式均有效"
- 切换叙事话术：约 30–40% 的氯胺城市每年临时切换至游离氯，双效配方全程覆盖

### 二氧化氯城市（少数，约 1,200 万人）
- 标准活性炭可有效去除 ClO₂ 和 ClO₂⁻
- 目前无消费品认证体系覆盖 ClO₂ 去除
- 不应做出 ClO₂ 去除宣称，除非有独立测试报告支撑

---

## 5. 常见误导性声明及风险评估

| 常见市场用语 | 实际风险 |
|------|------|
| "removes chlorine" | 如果用户在氯胺城市，这个表述形同虚设；未披露不覆盖氯胺是严重的 framing 问题 |
| "KDF removes chloramine" | KDF-55 实测去除率 18.2%、KDF-85 仅 1.4%——此宣称无据 |
| "tested to NSF/ANSI 177" for a bath spout filter | 177 范围仅限淋浴产品；对浴缸水龙头产品属于超范围引用 |
| "tested to NSF/ANSI 177" for chloramine removal | 177 测试水中氯胺 <0.1 mg/L，标准明确不评估氯胺性能，并要求产品附带此免责声明 |
| calcium sulfite + "removes chloramine" | 亚硫酸钙不与一氯胺反应，此宣称无化学机制支撑 |
| vitamin C in shower filter + "removes chloramine" | 维生素 C 与一氯胺的反应半衰期 ~4 分钟，淋浴接触时间 < 1 秒，去除率无法保证 |

---

## 6. 对 KES 产品设计的直接启示

### 游离氯城市目标 → 标准配方可行
亚硫酸钙（热水稳定）+ KDF 或标准活性炭即可。
可以申请针对 NSF/ANSI 42 的认证（不是 177）。

### 氯胺城市目标 → 配方必须升级
标配的媒体组合（KDF + 亚硫酸钙）**不够**。
需要：催化活性炭 + 维生素 C，且浴缸注水的接触时间是天然优势。

### 全市场覆盖（"无论您在哪"）→ 需要组合配方
维生素 C（抗坏血酸钠）+ 催化活性炭的组合，是当前技术上最宽谱、最可防守的路线。
这也是唯一可以诚实地说"同时覆盖游离氯和氯胺"的单产品配方。

### 最需要避免的产品设计陷阱
- 媒体选择只对游离氯有效，但宣称却覆盖氯胺城市用户
- 在氯胺城市销售时未披露产品局限
- 依赖 NSF/ANSI 177 来支持氯胺去除宣称（177 明确不测试氯胺）

---

## Sources
- [NCBI NBK234591 — Chemistry of Disinfectants in Water](https://www.ncbi.nlm.nih.gov/books/NBK234591/)
- [NCBI NBK596893 — ATSDR Toxicological Profile for Chlorine Dioxide](https://www.ncbi.nlm.nih.gov/books/NBK596893/)
- [EPA — Chloramines in Drinking Water](https://www.epa.gov/dwreginfo/chloramines-drinking-water)
- [CDC — About Water Disinfection with Chlorine and Chloramine](https://www.cdc.gov/drinking-water/about/about-water-disinfection-with-chlorine-and-chloramine.html)
- [Aquatell — Chlorine or Chloramine: 100 Largest US Cities](https://www.aquatell.com/pages/chlorine-or-chloramine-100-largest-cities-of-america)
- [DC Water — 2026 Annual Chlorine Switch](https://www.dcwater.com/resources/waterquality/chlorine-switch)
- [Missouri DNR PUB2646 — Nitrification and Temporary Free Chlorine Conversion](https://dnr.mo.gov/document-search/nitrification-temporary-conversion-chloramine-free-chlorine-pub2646/pub2646)
- [TCEQ — Chlorine Dioxide and Chlorite in Drinking Water](https://www.tceq.texas.gov/drinkingwater/chemicals/dbp/chlorinedioxide-and-chlorite.html)
- [TCEQ — Temporary Free Chlorine Conversion](https://www.tceq.texas.gov/drinkingwater/disinfection/temporary-free-chlorine-conversion)
- [Pureline — Carbon Filtration for ClO₂, Chlorite, and Chlorine](https://www.pureline.com/carbon-filtration-to-remove-chlorine-chlorine-dioxide-and-chlorite/)
- [Clean Faucet — Best Shower Filter for Chloramine (NSF 177 disclaimer note)](https://cleanfaucet.com/this-is-the-best-shower-filter-for-chloramine-2026/)
- [Pure Water Products — Removing Chloramines](https://www.purewaterproducts.com/articles/removing-chloramines)
- [Inspired Living — Vitamin C Removes Chloramines (SFPUC 1,000mg recommendation)](https://inspiredliving.com/chloramine-filters/vitamin-c-removes-chloramines.htm)
- [AquaBliss — Calcium Sulfite and Water Filters](https://aquabliss.com/blogs/healthy-water/calcium-sulfite-and-water-filters)
