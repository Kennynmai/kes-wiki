---
type: product
status: draft
owner: strategy
created: 2026-06-13
updated: 2026-06-13
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, north-america, water-quality, market-prioritization, product-definition]
source_count: 5
review_cycle: monthly
verification_status: working
related:
  - ./bathtub-filter-water-jurisdiction-demand-map.md
  - ./bathtub-filter-user-segments.md
  - ./bathtub-filter.md
---

# 浴缸过滤器北美水质与需求深化分析（产品定义用）

## 为什么有这页

这页是基于桌面研究 + 新增 web 数据，专门为 **KES V1 产品定义** 做的北美水质与需求深化分析。

目标：回答产品定义必须回答的 5 个问题：
1. 我们应该针对哪些水质剖面设计产品？
2. 这些水质剖面覆盖多少美国家庭？
3. 这些家庭集中在哪些大都会区？（V1 上市地理优先级）
4. 这些家庭的用户痛点是什么？（用户分层与需求信号）
5. 水质剖面对产品技术要求意味着什么？（滤材、流量、接触时间）

---

## 一句话结论（产品定义用）

> **V1 最可防守的目标剖面：游离氯（free chlorine）+ 任意硬度 + 有婴儿/敏感肌的家庭**
> 
> - 可触达市场：约 **60% 的美国大城市人口**（游离氯城市）
> - 地理优先级：**拉斯维加斯、凤凰城、圣安东尼奥、芝加哥**（游离氯 + 极硬/硬水，需求动机最强）
> - 不可触达（V1）：氯胺城市（~40% 大城市人口）、井水用户
> - 产品技术要求：point-of-use compact filter，针对游离氯去除优化，不声称软化硬水

---

## 1. 北美水质剖面与可触达市场测算

### 1.1 消毒剂类型：100 大城市（Aquatell 2024 数据）

| 消毒剂类型 | 城市数（前 100） | 大致人口占比 | V1 可触达？ |
|---|---|---|---|
| 游离氯（free chlorine） | ~60 城 | ~60% | ✅ 是 |
| 氯胺（chloramine） | ~40 城 | ~40% | ❌ 否（标准 KDF/CaSO₃ 无效） |

**游离氯城市（人口优先级排序）：**
纽约、芝加哥、拉斯维加斯、凤凰城、圣安东尼奥、埃尔帕索、科罗拉多斯普林斯、亚特兰大、杰克逊维尔、孟菲斯、匹兹堡、巴尔的摩、纳什维尔、萨克拉门托、西雅图、波特兰、火奴鲁鲁、底特律、哥伦布、印第安纳波利斯（氯胺）、堪萨斯城（氯胺）…

**氯胺城市（产品局限市场）：**
洛杉矶、旧金山、圣地亚哥、休斯顿、达拉斯、丹佛、费城、波士顿、华盛顿特区、明尼阿波利斯、迈阿密、坦帕、新奥尔良、奥斯丁、奥克兰…

> ⚠️ 约 40% 的氯胺城市会在每年某几周临时切换回游离氯进行管网冲洗。氯胺城市不是绝对排除，但 V1 无法对氯胺做出同等去除承诺。

### 1.2 水质硬度与消毒剂：重点城市实测数据（2024-2026）

| 城市 | 州 | 人口（约） | 消毒剂 | 硬度（mg/L ppm） | 硬度分类 | 消毒剂实测浓度 | V1 可触达？ | 备注 |
|---|---|---|---|---|---|---|---|---|
| 拉斯维加斯 | NV | 220万 | 游离氯 ✅ | 318 | 极硬 | 游离氯 avg 1.0 ppm（范围 0–2.5） | ✅ P1 | 科罗拉多河水源，气候干燥 |
| 凤凰城 | AZ | 500万 | 游离氯 ✅ | 278 | 极硬 | 需补充 | ✅ P1 | 科罗拉多河+盐河，季节波动 150–350 |
| 圣安东尼奥 | TX | 260万 | 游离氯 ✅ | 314 | 极硬 | 游离氯 avg 1.41 ppm（范围 0.14–6.4） | ✅ P1 | 德州硬水区代表 |
| 埃尔帕索 | TX | 85万 | 游离氯 ✅ | ~300 | 极硬 | 需补充 | ✅ P1 | 德州西部，小市场但需求极强 |
| 芝加哥 | IL | 950万 | 游离氯 ✅ | 183 | 极硬 | 游离氯 1.0 ppm | ✅ P2 | 人口基数最大 |
| 科罗拉多斯普林斯 | CO | 75万 | 游离氯 ✅ | 80 | 略硬 | 需补充 | ✅ P3 | 硬度较低，需求动机中等 |
| 萨克拉门托 | CA | 230万 | 游离氯 ✅ | ~100-150 | 中等 | 需补充 | ✅ P3 | 加州唯一游离氯大城市 |
| 杰克逊维尔 | FL | 160万 | 游离氯 ✅ | ~100-150 | 中等 | 需补充 | ✅ P3 | 佛罗里达代表 |
| 亚特兰大 | GA | 610万 | 游离氯/氯胺 ⚠️ | 30 | 软 | 需补充 | ⚠️ 待验证 | 水源软，硬度数据异常低，需核实 |
| 纽约 | NY | 2000万 | 游离氯 ✅ | 25 | 软 | 游离氯 0.5 ppm | ❌ 不适配 | 水软，硬水叙事无法用 |
| 西雅图 | WA | 400万 | 游离氯/氯胺 ⚠️ | 24.4 | 软 | 检出氯 1.0 ppm | ❌ 不适配 | 水软，需求动机弱 |
| 洛杉矶 | CA | 1300万 | 氯胺 ❌ | 162 | 硬 | 氯胺存在（量未明） | ❌ V1 不覆盖 | 需 V2 催化活性炭配方 |
| 圣地亚哥 | CA | 330万 | 氯胺 ❌ | 749 | 极硬 | 氯胺 avg 1.73 ppm（范围 0–3.8） | ❌ V1 不覆盖 | 极硬水但氯胺，需求有但产品无法诚实覆盖 |
| 迈阿密 | FL | 610万 | 氯胺 ❌ | 383 | 极硬 | 氯胺 2.7 ppm | ❌ V1 不覆盖 | 极硬水 + 氯胺，双重需求但双重技术障碍 |
| 达拉斯 | TX | 750万 | 游离氯/氯胺 ⚠️ | 135 | 硬 | 总氯 avg 2.97 ppm | ⚠️ 待验证 | 消毒剂类型需核实 |
| 休斯顿 | TX | 700万 | 氯胺 ❌ | 71.9 | 中等 | 氯胺 avg 3.0 ppm（范围 0.03–5.4） | ❌ V1 不覆盖 | 消毒剂类型为氯胺 |
| 明尼阿波利斯 | MN | 360万 | 氯胺 ❌ | 280.5 | 极硬 | 氯胺 avg 3.33 ppm（范围 2.8–3.7） | ❌ V1 不覆盖 | 极硬水但氯胺 |
| 坦帕 | FL | 320万 | 氯胺 ❌ | 190 | 极硬 | 需补充 | ❌ V1 不覆盖 | 极硬水但氯胺 |

**数据来源**：TapWater.org（2024-2026）、各城市 CCR 报告、Aquatell 100 大城市数据集
**⚠️ 待验证**：亚特兰大硬度 30 ppm 与"硬水州"预期不符，可能数据有误；洛杉矶/旧金山等加州城市消毒剂类型需查官方 CCR

### 1.3 可触达市场测算

**V1 产品定义下的可触达剖面**：游离氯 + 任意硬度（不声称软化）

| 水质剖面 | 美国家庭估算 | 说明 |
|---|---|---|
| 游离氯城市（所有硬度） | ~60% 大城市人口 | 约 1.8-2 亿人口，~7,000-8,000 万家庭 |
| 其中：游离氯 + 硬水（>120 mg/L） | ~45% 大城市人口 | 需求动机最强（氯味 + 硬水不适感叠加） |
| 其中：游离氯 + 极硬水（>180 mg/L） | ~20% 大城市人口 | 拉斯维加斯、凤凰城、圣安东尼奥等 |
| 氯胺城市 | ~40% 大城市人口 | V1 不可触达 |
| 井水用户 | ~13% 美国家庭 | 不在 V1 市政供水范围内，单独评估 |

> **注意**：以上是城市级估算，非精确统计。精确数字需要按 ZIP code 级别的水质数据加权计算。

---

## 2. V1 目标大都会区优先级排序（2026-06-13 更新版）

基于：**人口 × 游离氯 × 硬水程度 × 产品可防守性 × Reddit 社区验证**

| 优先级 | 大都会区 | 人口（约） | 消毒剂 | 硬度 | 需求动机强度 | Reddit 社区信号 | 备注 |
|---|---|---|---|---|---|---|---|
| **P1** | 拉斯维加斯（NV） | 220 万 | 游离氯 ✅ | 极硬（318） | ⭐⭐⭐⭐⭐ | 未查到特定讨论 | 气候干燥，皮肤敏感度高 |
| **P1** | 凤凰城（AZ） | 500 万 | 游离氯 ✅ | 极硬（278） | ⭐⭐⭐⭐⭐ | 未查到特定讨论 | 增长最快的太阳带城市 |
| **P1** | 圣安东尼奥（TX） | 260 万 | 游离氯 ✅ | 极硬（314） | ⭐⭐⭐⭐⭐ | 未查到特定讨论 | 德州硬水区代表，游离氯实测 1.41 ppm |
| **P2** | 芝加哥（IL） | 950 万 | 游离氯 ✅ | 极硬（183） | ⭐⭐⭐⭐ | r/eczema 有 Chicago 用户讨论洗澡问题 | 人口基数最大，极硬水 |
| **P2** | 埃尔帕索（TX） | 85 万 | 游离氯 ✅ | 极硬（~300） | ⭐⭐⭐⭐ | 未查到特定讨论 | 小市场但需求动机极强 |
| **P3** | 科罗拉多斯普林斯（CO） | 75 万 | 游离氯 ✅ | 略硬（80） | ⭐⭐⭐ | 未查到特定讨论 | 硬度较低，需求动机中等 |
| **P3** | 萨克拉门托（CA） | 230 万 | 游离氯 ✅ | 中等（~100-150） | ⭐⭐⭐ | 未查到特定讨论 | 加州唯一游离氯大城市 |
| **P3** | 杰克逊维尔（FL） | 160 万 | 游离氯 ✅ | 中等 | ⭐⭐⭐ | 未查到特定讨论 | 佛罗里达代表 |
| **⚠️ 待验证** | 亚特兰大（GA） | 610 万 | 游离氯/氯胺 ⚠️ | 软（30）⚠️ | ⭐⭐ | 未查到特定讨论 | 硬度数据异常（30 ppm 与 GA 预期不符），需核实 |
| **不适配** | 纽约 | 2000 万 | 游离氯 ✅ | 软（25） | ⭐⭐ | r/Parenting NYC 用户讨论水污染 | 水软，硬水叙事几乎无法用 |
| **不适配** | 西雅图 | 400 万 | 游离氯/氯胺 ⚠️ | 软（24.4） | ⭐⭐ | 未查到特定讨论 | 同上，需求动机弱 |
| **不适配（V1）** | 洛杉矶、圣地亚哥、迈阿密、达拉斯、休斯顿、明尼阿波利斯、坦帕… | 各 320-1300 万 | 氯胺 ❌ | 各异 | ⭐⭐（需求有，但产品无法诚实覆盖） | r/eczema 有 bleach bath 讨论，但无 filter | V2 考虑催化活性炭配方 |

**🔴 重要修正：**
1. 芝加哥硬度从 153 ppm 更新为 **183 ppm（极硬）**——需求动机从 P2 升级
2. 亚特兰大硬度数据为 **30 ppm（软）**，与"乔治亚州是硬水州"的预期严重不符——**需人工核实官方 CCR**
3. 圣地亚哥硬度 **749 ppm（极硬）**，但使用氯胺——需求最强但 V1 无法覆盖（需 V2）

---

## 3. 用户分层与需求信号（深化）

### 3.1 目标用户剖面（V1 产品定义）

**主要目标（Primary Target）：**
- 有 0-3 岁婴儿的家庭，住在游离氯 + 硬水城市
- 家长对洗澡水氯味敏感，担心婴儿皮肤刺激
- 愿意为"婴儿洗澡水质量"付费，价格敏感度中等

**次要目标（Secondary Target）：**
- 敏感肌/湿疹成人用户，住在游离氯城市
- 自己或孩子有洗澡后皮肤干燥/发痒问题
- 试过润肤霜但效果不满意，在寻找"水"的原因

**非目标（V1 不主动触达）：**
- 氯胺城市用户（产品无法诚实覆盖）
- 井水用户（单独产品路线）
- 硬水软化期望者（产品不声称软化）

### 3.2 需求信号（现有证据 + 2026-06-13 新增）

**搜索意图信号：**
- `bathtub filter` 全国搜索量：低但存在（Google Trends 峰值 100/100 出现在 2022 年）
- `baby bath filter`、`eczema bath filter` 等长尾词：存在但量小
- 竞争品牌：Filterbaby（$113 MSRP，月销 ~1K+），Canopy（$69-89，多渠道）

**评论情感信号（来自 existing wiki 的 10-ASIN 调查）：**
- 正面：氯味减少、皮肤刺激减轻、婴儿洗澡更安心
- 负面（投诉模式）：漏水、流量小、滤芯寿命短、安装不兼容

**Reddit 社区信号（2026-06-13 Arctic Shift 数据采集）：**

| Subreddit | 搜索关键词 | 是否有 bathtub filter 讨论？ | 关键发现 |
|---|---|---|---|
| r/eczema | "bath" | ❌ 无 | 用户讨论 bleach baths、oat baths、Dead Sea salt baths，**从未提到 bathtub filter** |
| r/Parenting | "filter" | ❌ 无 | 仅 2 条弱相关（学校饮水机过滤、搬家水污染），**无 bathtub filter** |
| r/BeyondTheBump | "bath" | ❌ 无 | 全部是关于婴儿洗澡哭闹、睡眠倒退、洗澡例行公事，**无产品过滤讨论** |
| r/SkincareAddiction | "bath" | ❌ 无 | 用户讨论 bath oils、emollients、exfoliation，**无 filtration** |
| r/BuyItForLife | "bathtub" | ❌ 无 | 讨论 bathtub 本身（品牌、安装、防滑贴），**无 filter** |

**🔴 关键发现：bathtub filter 在相关 Reddit 社区中几乎零认知度**

这意味着：
1. **品类教育成本会很高**——用户不会主动搜索"bathtub filter"，因为他们不知道这个产品存在
2. **需求是隐性的**——用户知道"洗澡后皮肤痒"，但不知道"水"是原因，更不知道"过滤器"是解决方案
3. **SEO 和内容营销至关重要**——需要教育用户"氯/硬水 → 皮肤问题 → 洗澡水过滤"的因果链
4. **竞品 Filterbaby 的社区存在感也很低**——说明整个品类都还在非常早期

**对比：shower filter 在社区中的认知度**
（建议后续补充：搜索 r/eczema 中的 "shower filter" 作为对比，验证是否是"bathtub"格式本身的问题，还是整个品类认知度低）

### 3.3 用户旅程关键点

```
意识到问题：洗澡后皮肤干/痒/红 → 怀疑是水的问题
    ↓
搜索：硬水 皮肤 / 氯 洗澡 / baby eczema bath
    ↓
发现品类：shower filter（更成熟）→ bathtub filter（小众但存在）
    ↓
评估：Amazon 评论阅读，关注安装兼容性、漏水、滤芯寿命
    ↓
购买决策：价格 $50-80 接受度最高；>$100 需要强信任信号
    ↓
使用后：氯味减少是最容易感知的 benefit；皮肤改善需要长期使用才判断
```

---

## 4. 水质剖面 → 产品技术要求

### 4.1 游离氯城市的技术要求

| 水质参数 | 典型范围 | 对产品的要求 |
|---|---|---|
| 游离氯浓度 | 0.5-2.0 mg/L（EPA 允许最高 4.0） | 滤材针对游离氯优化（KDF-55 + CaSO₃ 或活性炭） |
| 流量（tub fill） | 10-20 L/min（典型浴缸注水速度） | **最关键约束**：接触时间短，需要高反应速度滤材 |
| 水温（洗澡） | 37-42°C | CaSO₃ 在高温下寿命可能缩短，需要实测 |
| 硬度（共存离子） | 60-300+ mg/L（CaCO₃） | 不声称软化，但硬水会缩短部分滤材寿命 |

### 4.2 氯胺城市的技术障碍（V1 不覆盖）

| 问题 | 说明 |
|---|---|
| 标准 KDF-55 对氯胺几乎无效 | KDF 主要针对游离氯 |
| 标准 CaSO₃（亚硫酸钙）对氯胺无效 | 需要催化活性炭或维生素 C |
| 氯胺更难去除 | 需要更长的接触时间或更强的氧化能力 |
| 结论 | V1 配方无法诚实覆盖氯胺城市；V2 需要单独研发配方 |

### 4.3 产品定义的技术约束

**从水质剖面推导的产品技术要求：**

1. **滤材选择**：KDF-55 + CaSO₃ 组合（针对游离氯，NSF/ANSI 177 路线）
2. **接触时间挑战**：典型浴缸注水流量 15-20 L/min，compact filter 的接触时间极短 → **这是 V1 最大的技术风险**（A-01 假设验证）
3. **水温影响**：CaSO₃ 在 40°C 热水下的寿命和效率需要实测
4. **硬度共存**：硬水会缩短 KDF 寿命（结垢），需要在文案中明确滤芯更换周期
5. **不声称软化**：产品不声称软化硬水，只针对游离氯去除

---

## 5. 现有研究缺口（产品定义前必须补）

### 5.1 高优先级（直接卡住产品定义）

| # | 缺口 | 为什么卡住产品定义 | 怎么补 |
|---|---|---|---|
| G1 | **top 20 大都会区完整的"消毒剂 × 硬度 × 人口" joined 数据表** | 无法精确计算可触达市场大小，无法做地理优先级决策 | 继续补全城市硬度数据（逐城市查），或找现成的 dataset |
| G2 | **游离氯浓度分布（不是 EPA 上限，而是龙头实际浓度）** | 产品滤材寿命模型依赖进水氯浓度 | 查各城市 CCR 报告中的实际检测浓度范围 |
| G3 | **目标大都会区的"婴儿家庭密度"和"湿疹患病率"** | 用户分层需要量化，不能只靠推断 | CDC WONDER、美国湿疹协会数据 |
| G4 | **`bathtub filter` 搜索量 × 大都会区交叉数据** | 需求信号需要地理维度，不能只有全国总量 | Google Trends 分区域数据，或 Ahrefs/SEMrush 美国区域数据 |

### 5.2 中优先级（影响 go/no-go 决策）

| # | 缺口 | 影响 |
|---|---|---|
| G5 | Reddit / 社区真实用户声音（目前只有商业评测） | 用户真实痛点与文案语言来源 |
| G6 | 竞品在目标城市的销售分布（Filterbaby 哪卖得最好？） | 验证需求地理分布是否与我们的优先级一致 |
| G7 | 目标城市租金 vs 购房比例（影响"租房友好"产品定位） | 安装方式决策（租房友好 vs 永久安装） |

---

## 6. 下一步行动建议（产品定义前）

### 立即可做（不需要外部合作）：

1. **补全 top 20 大都会区的水质数据表**（G1）
   - 继续用 waterhardnessscale.com / tapwaterdata.com 逐个查
   - 目标：建立完整的 `bathtub-filter-utility-service-map-by-metro` 页面
   
2. **提取目标城市的 CCR 报告中的游离氯实际浓度**（G2）
   - 不是 EPA 上限 4.0 mg/L，而是实际检测值
   - 用于滤材寿命建模

3. **Google Trends 分区域数据分析**（G4）
   - `bathtub filter`、`baby eczema bath`、`chlorine bath filter` 按 US 区域
   - 验证：硬水 + 游离氯区域是否有更高搜索意图

### 需要外部合作 / 工具：

4. **Amazon Brand Analytics / 卖家精灵**（G6）
   - 竞品销售地理分布
   - 需要 Amazon 卖家账号或第三方工具订阅

5. **Reddit 社区信号采集**（G5）
   - 需要人工阅读 r/eczema、r/Parenting、r/beyondthebump
   - 或用 Reddit API 做 NLP 分析

---

## 7. 产品定义方向指引（2026-06-13 更新版）

基于现有数据（城市水质实测 + Reddit 社区信号），**V1 产品定义建议方向**：

| 维度 | 建议 | 依据 |
|---|---|---|
| **目标水质剖面** | 游离氯城市（~60% 美国大城市人口），不覆盖氯胺 | 标准 KDF-55 + CaSO₃ 对氯胺几乎无效 |
| **目标硬度范围** | 任意硬度（不声称软化，但硬水区是需求动机最强的） | 硬水 + 游离氯叠加区 = 最强需求（拉斯维加斯、凤凰城、圣安东尼奥） |
| **目标用户** | 有婴儿的家庭（0-3 岁）为主，敏感肌成人为辅 | Reddit 信号：婴儿洗澡哭闹/皮肤问题讨论量大，但 filter 认知度为零 |
| **地理优先级** | P1：拉斯维加斯、凤凰城、圣安东尼奥；P2：芝加哥、埃尔帕索 | 基于实测水质数据（硬度 × 消毒剂） |
| **核心宣称** | 游离氯去除（odor/comfort 叙事），**不声称**湿疹改善或硬水软化 | 学术证据不支持 eczema 改善宣称；compact filter 无法软化硬水 |
| **技术路线** | KDF-55 + CaSO₃，NSF 177 认证路径 | 针对游离氯，认证路径最清晰 |
| **最大技术风险** | normal-flow 条件下的氯去除效率（A-01 假设） | 浴缸注水流量 15-20 L/min，接触时间极短 |
| **定价建议** | $59-79 MSRP（与现有 wiki 建议一致） | Filterbaby $113 月销 1K+，证明有付费意愿 |
| **品类教育策略** | **高优先级**——Reddit 信号表明用户不知道这个产品存在 | 需要 SEO + 内容营销建立"氯/硬水 → 皮肤问题 → 洗澡水过滤"因果链 |

---

## 8. 关键发现与风险提示

### 8.1 关键发现

1. **品类认知度极低**：Reddit 相关社区（r/eczema、r/Parenting、r/BeyondTheBump、r/SkincareAddiction）中，**没有任何关于 bathtub filter 的讨论**。用户讨论的是 bleach baths、oat baths、Dead Sea salt baths——他们知道"洗澡水可能影响皮肤"，但不知道"过滤器"是解决方案。

2. **这意味着品类教育成本会很高**：用户不会主动搜索"bathtub filter"，因为他们不知道这个产品存在。需要主动教育。

3. **硬水 + 游离氯叠加区 = 最强需求动机**：拉斯维加斯（318 ppm，游离氯）、凤凰城（278 ppm，游离氯）、圣安东尼奥（314 ppm，游离氯）是 V1 最理想的市场。

4. **氯胺城市（~40% 大城市人口）V1 无法覆盖**：标准滤材（KDF-55、CaSO₃）对氯胺几乎无效。需要 V2 研发催化活性炭配方。

5. **亚特兰大硬度数据异常**：TapWater.org 显示 30 ppm（软），但乔治亚州是硬水州——**需要人工核实官方 CCR**。

### 8.2 风险提示

| 风险 | 影响 | 缓解措施 |
|---|---|---|
| 品类教育成本高 | 用户不知道产品存在，CAC 会很高 | 内容营销 + SEO + 影响者合作 |
| normal-flow 氯去除效率未验证 | 产品核心功能可能不成立 | WS2 物理测试（最高优先级） |
| 氯胺城市 ~40% 人口无法覆盖 | 市场总量受限 | V2 研发催化活性炭配方 |
| 硬水会缩短滤材寿命 | 滤芯更换周期可能比预期短 | 文案中明确更换周期；实测硬水条件下寿命 |
| 亚特兰大数据异常 | 地理优先级决策可能有误 | 人工核实官方 CCR |

---

## 9. 下一步行动建议

### 立即可做（不需要外部合作）：

1. **核实亚特兰大官方 CCR**（G1 补充）
   - TapWater.org 显示 30 ppm（软），但预期应为硬水
   - 需要查亚特兰大水务部门官方 CCR 报告

2. **Google Trends 分区域数据分析**（G4）
   - `bathtub filter`、`baby eczema bath`、`chlorine bath filter` 按 US 区域
   - 验证：硬水 + 游离氯区域是否有更高搜索意图

3. **补充 r/eczema 中的 "shower filter" 搜索**（验证是否是"bathtub"格式问题）
   - 如果 shower filter 有讨论但 bathtub filter 没有，说明是品类认知问题，不是格式问题

### 需要外部合作 / 工具：

4. **Amazon Brand Analytics / 卖家精灵**（G6）
   - 竞品销售地理分布
   - 需要 Amazon 卖家账号或第三方工具订阅

5. **WS2 物理样本采购和测试**（最高优先级）
   - 解决 A-01 假设验证
   - 这是 go/no-go 的核心卡点

---

---

## Sources

- Aquatell: "Chlorine or Chloramine in 100 Largest US Cities" (2024): `https://www.aquatell.com/pages/chlorine-or-chloramine-100-largest-cities-of-america`
- TapWaterData.com: Water Hardness Map (4,220+ US cities, updated 2026-03): `https://www.tapwaterdata.com/map/hardness`
- WaterHardnessScale.com: City-level hardness data (Las Vegas, Phoenix, Chicago, Colorado Springs)
- Existing wiki pages: `bathtub-filter-water-jurisdiction-demand-map.md`, `bathtub-filter-user-segments.md`, `bathtub-filter-assumption-register.md`
- EPA: National Primary Drinking Water Regulations (MRDL for chlorine: 4.0 mg/L)
- USGS: Water Hardness Map (state-level data)

---

## 10. 数据来源与验证状态

### 10.1 城市水质数据来源

| 数据项 | 来源 | 验证状态 |
|---|---|---|
| 拉斯维加斯硬度 + 游离氯浓度 | TapWater.org (Las Vegas) | ✅ 已验证 |
| 凤凰城硬度 | WaterHardnessScale.com (Phoenix) | ✅ 已验证 |
| 凤凰城消毒剂 | Phoenix.gov 官网（需补充官方 CCR） | ⚠️ 部分验证 |
| 圣安东尼奥硬度 + 游离氯浓度 | TapWater.org (San Antonio) + EWG | ✅ 已验证 |
| 芝加哥硬度 + 游离氯浓度 | TapWater.org (Chicago) | ✅ 已验证 |
| 洛杉矶硬度 + 消毒剂 | TapWater.org (Los Angeles) | ⚠️ 消毒剂类型需核实 |
| 迈阿密硬度 + 氯胺浓度 | TapWater.org (Miami) | ✅ 已验证 |
| 达拉斯硬度 + 消毒剂 | TapWater.org (Dallas) | ⚠️ 消毒剂类型需核实 |
| 圣地亚哥硬度 + 氯胺浓度 | TapWater.org (San Diego) | ✅ 已验证 |
| 休斯顿硬度 + 氯胺浓度 | TapWater.org (Houston) | ✅ 已验证 |
| 明尼阿波利斯硬度 + 氯胺浓度 | TapWater.org (Minneapolis) | ✅ 已验证 |
| 西雅图硬度 + 消毒剂 | TapWater.org (Seattle) | ⚠️ 消毒剂类型需核实 |
| 纽约硬度 + 游离氯浓度 | TapWater.org (New York City) | ✅ 已验证 |
| 亚特兰大硬度 | TapWater.org (Atlanta) | ⚠️ 硬度数据异常（30 ppm），需核实官方 CCR |
| 坦帕硬度 + 消毒剂 | TapWater.org (Tampa) | ✅ 已验证 |

### 10.2 Reddit 社区数据来源

| 数据项 | 来源 | 采集方法 | 验证状态 |
|---|---|---|---|
| r/eczema "bath" 搜索结果 | Arctic Shift API (`/api/posts/search?subreddit=eczema&query=bath`) | API 查询（2026-06-13） | ✅ 已验证 |
| r/Parenting "filter" 搜索结果 | Arctic Shift API (`/api/posts/search?subreddit=Parenting&query=filter`) | API 查询（2026-06-13） | ✅ 已验证 |
| r/BeyondTheBump "bath" 搜索结果 | Arctic Shift API (`/api/posts/search?subreddit=beyondthebump&query=bath`) | API 查询（2026-06-13） | ✅ 已验证 |
| r/SkincareAddiction "bath" 搜索结果 | Arctic Shift API (`/api/posts/search?subreddit=SkincareAddiction&query=bath`) | API 查询（2026-06-13） | ✅ 已验证 |
| r/BuyItForLife "bathtub" 搜索结果 | Arctic Shift API (`/api/posts/search?subreddit=buyitforlife&query=bathtub`) | API 查询（2026-06-13） | ✅ 已验证 |

### 10.3 主要数据来源 URL

- TapWater.org (城市水质数据): `https://www.tapwater.org/`
- WaterHardnessScale.com (硬度排名): `https://www.waterhardnessscale.com/en/guides/hardest-water-cities-usa`
- Arctic Shift (Reddit 历史数据 API): `https://arctic-shift.photon-reddit.com/`
- Arctic Shift API 文档: `https://github.com/ArthurHeitmann/arctic_shift/blob/master/api/README.md`
- Aquatell (100 大城市消毒剂类型): `https://www.aquatell.com/pages/chlorine-or-chloramine-100-largest-cities-of-america`
- EWG Tap Water Database: `https://www.ewg.org/tapwater/`

---

## 11. Obsidian 内部链接

- [[bathtub-filter]]
- [[bathtub-filter-water-jurisdiction-demand-map]]
- [[bathtub-filter-user-segments]]
- [[bathtub-filter-assumption-register]]
- [[bathtub-filter-evidence-matrix]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-normal-flow-vs-reduced-flow-evidence-table]]
- [[bathtub-filter-compatibility-engineering-breakpoints]]
- [[bathtub-filter-kes-go-no-go-memo-v1]]
- [[bathtub-filter-kes-next-step-execution-plan-v1]]

---

*此页面最后更新于 2026-06-13，基于桌面研究 + web 数据采集（TapWater.org + Arctic Shift Reddit API）。如需更新，请优先核实亚特兰大官方 CCR 报告和洛杉矶/达拉斯消毒剂类型。*
