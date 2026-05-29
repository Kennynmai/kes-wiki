---
source_type: vendor-material
source_vendor: Zibo Onlyzone Water Treatment Technology Co., Ltd.
source_file: /Users/kennymak/Downloads/阻垢条_宗立.pdf
created: 2026-04-20
domain: bathtub-filter
status: extracted
---

# Onlyzone 阻垢条材料快审（2026-04-20）

## Source
- 文件：`/Users/kennymak/Downloads/阻垢条_宗立.pdf`
- 文件形式：1 页扫描型 PDF
- 供应商页眉品牌：`ZONE / 宗立科技`

## 分类
- `source_type`: vendor-material
- `material_type`: antiscale-media
- `extraction_mode`: narrow-then-manual

## 先看结论
- 这份材料展示的是 **阻垢条 / antiscale strip**，不是离子交换树脂，也不是去氯滤材。
- 它宣称的是 **阻垢率**，不是 **硬度去除率**，因此不能把它当成“软化水”证据。
- 现有页面中的“真正软化只能靠离子交换或膜法”的判断，与这份材料 **不冲突**。

## 从扫描件人工读取到的关键信息

### 1. 产品介绍
- 文案：`本产品适用各类净水滤芯，产品添加量仅需25g，过水寿命8吨，阻垢率可达85%，可有效提高水效。`

### 2. 产品参数
- 产品名称：阻垢条
- 产品型号：`ZONE-ZG-A01`
- 产品规格：直径 `1.2–1.5 mm`
- 堆积密度：`0.7 g/cm³`
- 产品材质：`陶瓷`

### 3. 性能测试 4.1
- 测试项目：通水测试阻垢率
- 测试样品：阻垢滤芯
- 测试水源：自来水
- 自来水硬度：`350 ppm`
- 阻垢颗粒添加量：`20 g`
- 测试流速：`1.6 L/min`

表 1：

| 通水量 | 阻垢率 |
|---|---:|
| 1000 L | 100% |
| 2000 L | 98% |
| 3000 L | 97% |
| 4000 L | 94% |
| 5000 L | 93% |
| 10000 L | 91% |
| 20000 L | 88% |

### 4. 性能测试 4.2
- 测试项目：通水测试阻垢率
- 测试样品：阻垢花洒
- 测试水源：自来水
- 自来水硬度：`350 ppm`
- 阻垢颗粒添加量：`25 g`
- 测试流速：`8 L/min`

表 2：

| 通水量 | 阻垢率 |
|---|---:|
| 1000 L | 93% |
| 2000 L | 90% |
| 3000 L | 87% |
| 4000 L | 85% |
| 5000 L | 81% |
| 6000 L | 79% |
| 7000 L | 76% |
| 8000 L | 74% |

### 5. 涉水安全
- 文案：`根据《生活饮用水输配水设备及防护材料卫生安全评价规范》(2001)，符合涉水安全标准。`
- 扫描件中放大框展示的项目主要是外观、浑浊度、臭和味、肉眼可见物等。

### 6. 应用
- 文案：`本产品适用各类净水滤芯`
- 配图含多种滤芯/花洒/龙头类载体

## 初步判断

### A. 它证明了什么
- 它证明供应商在卖一种 **陶瓷类阻垢介质**。
- 它证明供应商内部有一套 **“阻垢率” 随通水量衰减** 的测试口径。
- 它说明该介质可被包装成 `filter additive` 或 `shower/bath hardware adjunct media`。

### B. 它没有证明什么
- 没有证明 **Ca²⁺ / Mg²⁺ 被移除**
- 没有证明 **出水硬度下降**
- 没有证明 **soap performance / lather / skin-feel** 发生软水意义上的变化
- 没有证明 **浴缸整缸水** 在 bath-fill 条件下得到用户可感知收益

### C. 对 bathtub filter 研究的直接意义
- 它更接近 **scale-control adjunct media**，不是 **softening media**。
- 如果 KES 想做的是 `hard-water comfort` 或 `true softening`，这份材料不能作为成立依据。
- 如果 KES 只想探索 `scale-storytelling`，这份材料可作为供应商信号，但仍需要 finished-product 测试来回答：
  - scale 控制发生在什么位置
  - 对 tub spout / housing / tub wall 是否有可测收益
  - 是否会占用主力去氯媒体体积

## 建议写回方向
- 写入 `wiki/source-summaries/`：作为 vendor-material 摘要
- 写入 `bathtub-filter-point-of-use-hardness-softening-feasibility.md`：明确 `阻垢 ≠ 软化`
- 写入 `bathtub-filter-kes-media-stack-options-by-water-type.md`：不把阻垢条当成 Version A/B/C 的核心滤材
