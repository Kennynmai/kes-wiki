---
type: product
status: draft
owner: strategy
created: 2026-07-01
updated: 2026-07-01
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, consumer-education, water-quality, glossary, disinfectant, hardness, tds]
source_count: 4
review_cycle: monthly
verification_status: spot-checked
related:
  - ../bathtub-filter-disinfectant-types-and-media-guide.md
  - ../bathtub-filter-utility-service-map-by-metro.md
  - ../bathtub-filter-na-water-profile-and-target-market-analysis.md
  - ../bathtub-filter-customer-water-quality-test-methods-2026-06-03.md
  - ../bathtub-filter-claim-register.md
---

# E4 · 洗澡水术语表（一页速查）

## 这一页帮你搞懂什么

第一次研究"我家水该不该装过滤器"的时候，你会撞上一堆看不懂的词：free chlorine、chloramine、ppm、gpg、TDS、DBPs……它们听起来都像"氯"，其实指的是完全不同的东西，处理方式也不一样。

这一页把这些词一次讲清，每个配一句人话解释 + 一个简单例子。**这是本科普簇（Spoke E）的术语真理源**——其它页遇到这些词，都会链回这里，不重复解释。

> 口径提醒：这一页只帮你**认识水里有什么、术语什么意思**，不替你的水下健康结论，也不是买产品的理由。中立赋能，不吓唬人。

---

## 一、消毒剂类术语（市政自来水才有）

> 下面这几个词只跟**市政自来水**有关。井水通常没有氯，见 [E2 井水基础](./bathtub-filter-kes-edu-well-water-basics.md)。

### Free chlorine（游离氯）

- **人话**：水厂用液氯 / 漂白水 / 次氯酸钙加进水里，到你龙头这一端形成的那种"氯"。就是让水有"泳池味"的最常见来源。
- **化学形态**：HOCl + OCl⁻（[消毒剂指南 §1a](../bathtub-filter-disinfectant-types-and-media-guide.md)）。水厂加的三种形式（液氯 Cl₂ / 次氯酸钠 NaOCl / 次氯酸钙 Ca(OCl)₂）到龙头端**是同一种游离氯**，对过滤器来说没区别。
- **例子**：纽约、芝加哥、拉斯维加斯、凤凰城、亚特兰大等约 60% 的美国大城市用游离氯（[城市速查表 §2.1](../bathtub-filter-utility-service-map-by-metro.md)）。
- **能不能过滤**：游离氯是**最容易被普通滤材去除**的一种（活性炭 / KDF / 亚硫酸钙 / 维生素 C 都有效，[消毒剂指南 §2](../bathtub-filter-disinfectant-types-and-media-guide.md)）。

### Chloramine / Monochloramine（氯胺 / 一氯胺）

- **人话**：另一种消毒方式，水厂把氨（NH₃）和氯合在一起，形成更稳定、在管网里衰减更慢的消毒剂。到你龙头端主要是**一氯胺（NH₂Cl）**。
- **为什么水厂用它**：氯胺产生的消毒副产物（见下）更少、余量维持得更久（[消毒剂指南 §1b](../bathtub-filter-disinfectant-types-and-media-guide.md)）。
- **例子**：洛杉矶、旧金山、休斯顿、丹佛、费城、华盛顿特区等约 35–40% 的美国市政系统用氯胺（[消毒剂指南 §1b](../bathtub-filter-disinfectant-types-and-media-guide.md)、[城市速查表 §2.2](../bathtub-filter-utility-service-map-by-metro.md)）。
- **能不能过滤**：**比游离氯难得多**。普通活性炭要 3–4 倍接触时间，KDF 和亚硫酸钙基本无效（KDF-55 实测仅 18.2%、KDF-85 仅 1.4%，[消毒剂指南 §2](../bathtub-filter-disinfectant-types-and-media-guide.md)）。要靠催化活性炭或维生素 C，且需要足够接触时间。
- 详见 [E1 你的城市用游离氯还是氯胺](./bathtub-filter-kes-edu-chlorine-vs-chloramine-geography.md)。

### Total chlorine（总氯）

- **人话**：游离氯 + 结合氯（氯胺）加在一起的总量。
- **关键换算**：**总氯 − 游离氯 = 结合氯（约等于氯胺）**（[自测套件 §二](../bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md)）。
- **例子**：如果试纸测出总氯远大于游离氯，说明你家水里很可能有氯胺。但**这个减法会放大误差，只能作为线索（flag），不能当结论**——消毒剂类型还是以查 CCR / 水务图谱为准。

### Combined chlorine（结合氯）

- **人话**：氯跟氨或有机物结合后的那部分氯，在市政水里主要就是氯胺。数值上 = 总氯 − 游离氯。

### DBPs — Disinfection By-Products（消毒副产物）

- **人话**：氯 / 氯胺跟水里的有机物反应生成的副产物，最常被提到的是**三卤甲烷（THMs）**和**卤乙酸（HAAs）**。
- **为什么被提**：EPA 对这些物质有法规限制；水厂改用氯胺的原因之一就是减少 DBPs（[消毒剂指南 §1b](../bathtub-filter-disinfectant-types-and-media-guide.md)）。
- **例子**：热带高有机物负荷 + 氯化的地区 DBP 通常更高（如波多黎各，[水源类型指南 §6](../bathtub-filter-water-source-types-guide.md)）。
- **能不能过滤**：活性炭对部分 DBP 有效，但不同 DBP 差异大——这不是 KES V1 的核心声称，别当成主要卖点。

### Chlorine dioxide（二氧化氯，ClO₂）

- **人话**：一种**独立的**消毒分子，**不是"氯"**（不会变成游离氯），少数水厂用作预处理。约 1,200 万美国人有接触（[消毒剂指南 §1c](../bathtub-filter-disinfectant-types-and-media-guide.md)）。普通消费者一般不用管这个词。

---

## 二、硬度类术语

> 详细的地理和"硬水意味着什么"，见 [E3 美国硬水地图 + 硬度单位](./bathtub-filter-kes-edu-hard-water-map-and-units.md)。

### Hardness（硬度）

- **人话**：水里溶解的**钙（Ca²⁺）和镁（Mg²⁺）**的量。多了就是"硬水"，会结水垢、洗完有干涩感。
- **注意**：硬度**跟氯是两码事**。硬水城市可能用游离氯也可能用氯胺——两个维度分开看。

### ppm / mg/L（毫克每升）

- **人话**：硬度最常用的单位之一。1 ppm ≈ 1 mg/L（在水质语境下当作相等）。硬度通常写成 "mg/L as CaCO₃"（以碳酸钙计）。
- **例子**：拉斯维加斯约 318 ppm、圣安东尼奥约 314 ppm、芝加哥约 183 ppm、纽约约 25 ppm（[北美水质分析 §1.2](../bathtub-filter-na-water-profile-and-target-market-analysis.md)）。

### gpg（grains per gallon，格令每加仑）

- **人话**：美国另一个常见硬度单位，很多软水机和硬水试纸用它。
- **换算**：源文件里出现过成对写法，如拉斯维加斯 "~290 ppm / 16 gpg"、凤凰城 "~285 ppm / 16 gpg"、印第安纳波利斯 "20 gpg"（[城市速查表 §2.1/§2.2](../bathtub-filter-utility-service-map-by-metro.md)）。
- 🟡 **精确换算系数（1 gpg ≈ 17.1 mg/L）在源文件中未单独给出**——若要在对外页面印换算公式，需另找权威来源核实后再用。

### 硬度分档（软 / 中等 / 硬 / 极硬）

- **人话**：把硬度分成几档，方便消费者对号入座。源文件对具体城市做了分档，例如：纽约 25 ppm = 软、科罗拉多斯普林斯 80 ppm = 略硬、萨克拉门托约 100–150 ppm = 中等、洛杉矶 162 ppm = 硬、拉斯维加斯 318 ppm = 极硬（[北美水质分析 §1.2](../bathtub-filter-na-water-profile-and-target-market-analysis.md)）。
- 🟡 **各档位的精确 ppm 边界（软 / 中 / 硬 / 极硬各是多少到多少）源文件未给出统一阈值表**——只有逐城市的分档标注可引用。

### Scale（水垢）

- **人话**：硬水里的钙镁在龙头、缸壁、玻璃门上结出的白色沉积。
- **注意（护栏）**："阻垢"（不让它结垢 / 挂垢）和"软化"（把钙镁从水里拿走）是两回事。compact 浴缸滤芯做的是前者，**不软化你的水**（[硬水场景页](./bathtub-filter-kes-scenario-hard-water-scale.md)）。

### Softening（软化）

- **人话**：真正把水里的钙镁**拿走**、让硬度数字下降。需要离子交换软水机，**不是**小型浴缸过滤器能做到的（[硬水场景页](./bathtub-filter-kes-scenario-hard-water-scale.md)）。
- 家里已装全屋软水机？软水机去了水垢，但**氯 / 氯胺仍 100% 保留在浴水里**（[水源类型指南 §1](../bathtub-filter-water-source-types-guide.md)）。

---

## 三、测试工具类术语

> 怎么测、每个工具测什么、置信度多高，详见 [E5 怎么测我家洗澡水](./bathtub-filter-kes-edu-how-to-test-your-water.md)。

### TDS（Total Dissolved Solids，溶解性总固体）

- **人话**：水里**所有溶解固体**的总量（矿物质、盐等），单位 ppm。
- 🔴 **最重要的一件事：TDS 笔测不出氯，也不等于硬度。** TDS 高不代表"有害"，TDS 不变也不代表过滤器没用。
- **不能干什么**：**不能用 TDS 笔验证去氯效果**。去氯要用**游离氯试纸**（[自测套件 §五](../bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md)、[客户测试方法页](../bathtub-filter-customer-water-quality-test-methods-2026-06-03.md)）。这是差评高发点——很多用户用 TDS 笔测"数字没变"就以为产品无效，其实 TDS 本来就不是去氯该看的指标。

### 游离氯试纸（free chlorine test strip）

- **人话**：一张色块试纸，蘸一下水、对色卡，读出游离氯大致浓度。
- **用途**：**验证去氯的正确工具**——装过滤器前后各测一次，看游离氯有没有降下来。
- **置信**：🟡 粗筛指路，给档位、不给实验室级精确数字。

### 总氯试纸（total chlorine test strip）

- **人话**：测总氯的试纸，常和游离氯试纸做成双垫。
- **用途**：**氯胺城市的验证工具**——游离氯试纸测不出氯胺，氯胺要看总氯（[自测套件 §五](../bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md)）。

### CCR（Consumer Confidence Report，消费者信心报告）

- **人话**：你所在的水务公司每年发布的**水质年报**，里面写了用什么消毒剂、硬度、检出的污染物等（[机构指南 §1](../bathtub-filter-institutional-guidance.md)）。
- **用途**：查"我家用游离氯还是氯胺"的**权威来源**。怎么找、怎么读，见 [E7 怎么读你的 CCR](./bathtub-filter-kes-edu-how-to-read-your-ccr.md)。

### NSF/ANSI 42 与 177（认证标准，了解即可）

- **人话**：过滤产品常引用的两个测试标准。42 大致对应减氯 / 味道类，177 对应淋浴过滤器。
- **护栏**：177 的测试水里氯胺 <0.1 mg/L，**标准本身明确不评估氯胺性能**——所以"通过 NSF 177"不能拿来支持"去氯胺"（[消毒剂指南 §5](../bathtub-filter-disinfectant-types-and-media-guide.md)）。认证口径别自己发挥，以官方定义为准。

---

## 诚实边界 / 护栏

- 这一页**只解释术语**，不替你的水下"好 / 坏 / 有毒"的判断。看到某个词不必恐慌——先搞清它指什么、能不能测、能不能过滤。
- 🔴 **TDS 笔不能验证去氯**；🔴 **NSF 177 不支持氯胺声称**；🔴 硬水滤材"阻垢"不等于"软化"。这三条是本簇反复强调的红线。
- 试纸是**粗筛指路**，不是实验室检测——给档位、不给精确数字。
- 标 🟡 的两处（gpg 精确换算系数、硬度分档精确阈值表）源文件未给出，若要对外印公式 / 阈值表需另行核实。

---

## 下一步

- 想知道你家城市用游离氯还是氯胺 → [E1 你的城市用游离氯还是氯胺？](./bathtub-filter-kes-edu-chlorine-vs-chloramine-geography.md)
- 想搞懂硬水地图和单位换算 → [E3 美国硬水地图 + 硬度单位](./bathtub-filter-kes-edu-hard-water-map-and-units.md)
- 想动手测自己家的水 → [E5 怎么测我家洗澡水 + 工具置信度](./bathtub-filter-kes-edu-how-to-test-your-water.md)
- 想读懂自家水质年报 → [E7 怎么读你的 CCR](./bathtub-filter-kes-edu-how-to-read-your-ccr.md)
- 已经知道自己是哪种水，想看该买哪个 → [T1 水质自测 / 选型页](./bathtub-filter-kes-page-water-test-diagnosis.md)

## Sources

- [消毒剂种类与滤材指南（游离氯 / 氯胺 / 总氯 / DBP / ClO₂ / NSF 口径）](../bathtub-filter-disinfectant-types-and-media-guide.md)
- [美国主要城市消毒剂与硬度速查表（ppm / gpg 成对写法）](../bathtub-filter-utility-service-map-by-metro.md)
- [北美水质与目标市场分析（逐城市硬度 ppm + 分档）](../bathtub-filter-na-water-profile-and-target-market-analysis.md)
- [客户如何判断水质是否改善（TDS 误解）](../bathtub-filter-customer-water-quality-test-methods-2026-06-03.md)
- [机构指南（CCR / EPA 背景）](../bathtub-filter-institutional-guidance.md)
- [水质自测套件 / 获客引擎（总氯 − 游离氯 flag、验证试纸）](../bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md)

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-kes-marketing-site-content-map]]
- [[bathtub-filter-disinfectant-types-and-media-guide]]
- [[bathtub-filter-utility-service-map-by-metro]]
- [[bathtub-filter-na-water-profile-and-target-market-analysis]]
- [[bathtub-filter-customer-water-quality-test-methods-2026-06-03]]
- [[bathtub-filter-institutional-guidance]]
- [[bathtub-filter-kes-edu-chlorine-vs-chloramine-geography]]
- [[bathtub-filter-kes-edu-hard-water-map-and-units]]
- [[bathtub-filter-kes-edu-how-to-test-your-water]]
- [[bathtub-filter-kes-edu-how-to-read-your-ccr]]
- [[bathtub-filter-kes-page-water-test-diagnosis]]
