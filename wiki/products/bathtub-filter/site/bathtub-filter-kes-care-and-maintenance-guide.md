---
type: product
status: draft
owner: product
created: 2026-07-01
updated: 2026-07-02
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, v1, care, maintenance, mold, drying, cleaning, replacement, troubleshooting, return-reduction]
source_count: 5
review_cycle: monthly
verification_status: spot-checked
related:
  - ./bathtub-filter-kes-v1-definition-and-not-for-list.md
  - ./bathtub-filter-kes-pack-contents-spec.md
  - ./bathtub-filter-kes-page-replacement-and-lifespan.md
  - ../bathtub-filter-complaint-taxonomy-and-risk-by-route.md
  - ../bathtub-filter-marketplace-negative-review-signals.md
  - ../bathtub-filter-review-patterns-and-return-risk.md
  - ../bathtub-filter-claim-register.md
  - ./bathtub-filter-kes-page-water-test-diagnosis.md
---

# P3 · KES V1 使用与维护指南（防霉 / 寿命 / 清洁 / 排查）

## 这一页是什么

这是把**竞品负面评论洞察**（说明书必须写清排水 / 晾干 / 清洁 / 更换 / 防霉）+ **投诉分类**（3 周变黑 / 漏水 / 溢流 / 看不到效果）转成 KES 自有说明书内容的页。目的很直接：**降退货**。

依据：[marketplace-negative-review-signals](../bathtub-filter-marketplace-negative-review-signals.md)（竞品洞察：更该强化 replacement / drying / storage clarity）、[complaint-taxonomy](../bathtub-filter-complaint-taxonomy-and-risk-by-route.md)（发霉 13.6%、绕流/溢流 19.0%、整体无效 46.5% 是 1-2 星高杀伤）、[review-patterns-and-return-risk](../bathtub-filter-review-patterns-and-return-risk.md)。更换 / 寿命口径**沿用 [T3 更换与寿命页](./bathtub-filter-kes-page-replacement-and-lifespan.md)，本页不新造去氯 / 寿命数字**。护栏照 [claim-register](../bathtub-filter-claim-register.md)。

---

## 一、每次泡澡后：排水 + 晾干（防霉第一防线）

> **为什么这条最重要**：湿 + 温 + 有机负荷 = 霉菌天堂，是竞品（尤其软挂 / 织物型）最高频差评来源之一（complaint-taxonomy 投诉 #4 mold/odor 60–90 天；逐条标签发霉 / 卫生 13.6%）。KES 靠**排水晾干闭环**把霉菌窗口关掉。

1. **每次注水结束后取下滤仓**，把仓内残水**倒尽 / 排空**。
2. **晾干**：置于通风处自然晾干，不要密封收进潮湿角落。
3. **不要长期泡在浴缸水里**（V1 是注水路径产品，不是泡在缸里的 floating filter）。

🟢 对外可用（照 register 包装/说明书表面口径，用 baths/gallons 不用月；防霉走操作闭环）：

> "After each fill, remove the cartridge, drain it, and let it air-dry. Do not store it wet."

---

## 二、定期清洁

> （2026-07-02 按 [V1 BOM 表](../bathtub-filter-v1-free-chlorine-removal-dimensions-materials.md) 裁定更正：滤棉材质 PP→聚酯纤维（PET）；寿命换算参照随模型重算改为约 9–10 个月）

| 部件 | 怎么清 | 频率 |
|---|---|---|
| 白色外壳（防溢仓 / 装载仓）| 清水冲洗，自然晾干；有水垢感可用温水 | 每周 / 目视需要时 🟡 建议频率待确认 |
| 过滤棉（PET） | **不清洗、直接换**（属消耗件，见 §四）| 变色 / 挂杂质即换 |
| KDF55 / CaSO₃ 透明滤仓 | 外部冲洗即可；**不拆内部滤料** | 目视需要时 |
| 硅胶挂带 / 3M 挂钩 | 清水擦净、晾干，保持粘 / 摩擦力 | 目视需要时 |

> 🟡 具体清洁剂 / 禁用清洁剂清单原件未给，待补，不杜撰。

### 二A、回洗自清洁 / 再生（**升级款可选** · 基础款不适用）

> **适用范围**：仅**带回洗口的升级款**（专利 App# 19/281,644 Fig.1 元件 107 / claim 16）。**基础款不带回洗**——基础款的维护方式就是本页 §二 清洁 + §四 换滤料，不要尝试对基础款做回洗。

回洗 = 把自来水**反向**通过滤床，冲出截留的细粉 / 沉积，恢复水流与部分性能。它是「换滤料」之外的第二种维护手段，**不是替代更换**——去氯衰减到 T3 更换触发点时仍需换芯。

**操作步骤（全程 ≤30 秒）**：

1. **1/4 转拧下**处理滤仓（免工具）；
2. 打开排水端；
3. 自来水**反向**通到滤仓末端，**约 10 L/min 反冲 15 秒**；
4. 关排水，把滤仓**1/4 转拧回**原位，确认到位无渗漏。

**它能恢复什么（专利实施例口径，🟡 全部待第三方复测，不作对外承诺）**：

| 指标 | 专利实施例（内部） | 状态 |
|---|---|---|
| 压降 ΔP（跑 3200L≈80 缸后回洗） | 9.4 → 4.8 kPa（恢复 ~49%，水流明显变顺） | 🟡 待第三方 |
| 去氯率 | 86% → >92% | 🟡 待第三方；对外数字归 [T2/Gate 1](./bathtub-filter-kes-page-how-we-test-and-certify.md) |
| 耐久 | 20 循环 / 累计 64,000L：壳无裂、O 圈老化 ≤5% | 🟡 待第三方 |

**护栏**：🔴 对外不得写「回洗后恢复 X%」类具体数字（内部实施例非第三方）；🟢 可讲的结构事实 = 「升级款支持 ≤30 秒免工具回洗自清洁」。回洗后仍按 [T3 更换触发](./bathtub-filter-kes-page-replacement-and-lifespan.md) 判断换芯——回洗恢复的是水流与部分性能，**不重置滤料寿命**。

---

## 三、防霉要点（把 §一 做成习惯）

- 🟢 **排水 → 晾干 → 干存**三步是防霉核心，不是可选项。
- 🟢 KDF55 层帮助**抑制滤芯内部生物膜与异味 / 发黏**（讲解件 §3.13）——但这是**柱内**属性，🔴 不得说「杀死浴缸水里的细菌 / 给浴缸水消毒」。
- 🟢 若已出现异味 / 发黏 / 变色加速：优先按更换触发换过滤棉（PET）/ 滤仓（见 §四），不要继续用。

---

## 四、何时更换（口径沿用 T3，不在本页新造数字）

> 完整更换触发曲线 + baths/gallons 寿命口径见 **[T3 更换与寿命页](./bathtub-filter-kes-page-replacement-and-lifespan.md)**。本页只做操作提醒。

### 过滤棉（PET，高频耗材）
- 🟢 **变色（白→黄）/ 明显挂杂质即换**。随盒 20 块（见 [P2 套装清单](./bathtub-filter-kes-pack-contents-spec.md)）。

### KDF55 / CaSO₃ 滤仓（按去氯衰减曲线）
- 🟢 判断标准 = **系统总游离氯去除率**沿曲线衰减（~90% 软触发备芯 / ~80% 强触发建议换 / **<50% 强制换**）。
- 🟢 **用游离氯试纸自验证**：过滤前后对比，读数掉到你不满意就换；**不要用 TDS 笔当裁判**。
- 🟡 「约 9–10 个月」只是 2 ppm / 3 baths·week 情形的换算参照，**不作独立时间承诺**——你家自来水氯浓度直接影响寿命（口径见 T3）。

🟢 承重限定句必带（照 register 原文）：

> "Your local tap chlorine affects lifespan — verify with the included free-chlorine test strip."

---

## 五、常见问题排查树（据 complaint-taxonomy 反写）

把竞品最高杀伤投诉逐条转成「症状 → 原因 → 处理」，直接放说明书 / FAQ / 客服脚本，降退货。

### 症状 A：滤棉 / 滤仓「3 周就变黑 / 变脏」
- **原因**：这是**正常现象**——过滤棉（PET）在拦截铁锈 / 沉积物 / 黑点，变色 = 过滤在工作（讲解件 §3.12「白→黄 / 挂杂质」是信任证据）。也可能是所在地水杂质偏多。
- **处理**：属可视化正常损耗，**直接换过滤棉**（随盒 20 块）。若变色异常快，可能水质杂质高，正常增加更换频率。
- 🟢 文案口径：把「变黑」讲成**证据**而非缺陷。

### 症状 B：漏水 / 顶部溢出（top-spill）
- **原因**：多为**流量超过滤材处理能力**，或挂带 / 接水仓未装到位、出水嘴几何不匹配（complaint-taxonomy R3 overflow / 逐条标签绕流·溢流 19.0%）。
- **处理**：① 适度调小水龙头（V1 防溢目标 ≤30 L/min，讲解件 §3.11）；② 检查主挂带 / 接水仓是否装正、贴合；③ 异形 / 无提拉头出水嘴用 3M 挂钩 + 短硅胶带辅助固定（见 [P2](./bathtub-filter-kes-pack-contents-spec.md)）。
- 🟡 具体「推荐最大流速」上包装前须以实测 flow-overflow 数据坐实（不杜撰精确阈值）。

### 症状 C：装不稳 / 从出水嘴滑落
- **原因**：出水嘴几何不匹配——curved / swan-neck / 短出水 / 会晃的出水嘴，clamp 难稳定（complaint-taxonomy R3 spout retention 极高风险）。
- **处理**：① 用扁硅胶主挂带贴合固定（宽约 21mm）；② 异形 / 无提拉头出水嘴改用 3M 挂钩 + 短硅胶带（5孔 / 124mm / 20mm）；③ 主固定力来自硅胶带拉力 + 摩擦力。
- 🔴 **不要**承诺 universal fit；对不支持的出水嘴类型要提前明示（见 [[bathtub-filter-supported-spout-matrix]]）。**不建议**用胶带 / 发圈 workaround（那是退货前兆）。

### 症状 D：闻不到 / 感觉不到差别（「看不到效果」）
- **原因**：这是最高杀伤投诉（整体无效 46.5%）。可能是滤芯已到寿命末段、水本身氯浓度低、或用户没做对比。
- **处理**：① **用游离氯试纸做过滤前后对比**（客观读数，别只靠鼻子）；② 若读数确实下降 = 产品在工作，只是你家水氯本就不高；③ 若前后读数都低且滤芯用久了 → 按曲线更换（见 §四 / T3）。
- 🔴 客服 / 文案**不得**用「purifies / 降 TDS」找补；🔴 不得用 TDS 笔证明效果（TDS 非氯）。🟢 只讲 free-chlorine 验证。

### 症状 E：有霉味 / 发黏
- **原因**：湿存放未晾干，或滤芯 / 过滤棉超期。
- **处理**：① 回到 §一 排水晾干闭环；② 更换过滤棉（PET）/ 滤仓；③ 保持干存。

---

## 六、护栏（本页承重红线）

- 🟢 更换 / 寿命 / 去氯**数字口径不在本页新造**，一律引 [T3](./bathtub-filter-kes-page-replacement-and-lifespan.md)；用 baths / gallons，不换算成月。
- 🟢 验证只用**游离氯试纸**（前后对比）；🔴 TDS 笔 / 铅试纸不作验证或卖点。
- 🔴 抑膜 / 抑菌是**柱内**属性，不得说「给浴缸水消毒 / 杀菌」。
- 🔴 不认领 eczema / 健康 / 婴儿安全；排查话术停在感官 / comfort + 客观读数。
- 🔴 兼容表达必带「不支持」边界，不承诺 universal fit。

> 完整护栏见 [claim-register](../bathtub-filter-claim-register.md) §表面→claim 映射「包装/说明书」行。

---

## Sources

- [marketplace-negative-review-signals](../bathtub-filter-marketplace-negative-review-signals.md)（竞品洞察：replacement / drying / storage clarity 必写）
- [complaint-taxonomy-and-risk-by-route](../bathtub-filter-complaint-taxonomy-and-risk-by-route.md)（发霉 / 溢流 / 整体无效 / retention 投诉排序）
- [review-patterns-and-return-risk](../bathtub-filter-review-patterns-and-return-risk.md)（退货风险模式）
- [T3 更换与寿命页](./bathtub-filter-kes-page-replacement-and-lifespan.md)（更换 / 寿命 / 去氯口径真理源）
- [claim-register](../bathtub-filter-claim-register.md)（护栏）
- 一手结构 / 抑膜 / 防溢背景：[`浴缸过滤器_城市市政自来水版202602讲解.md`](../../../../raw/products/bathtub-filter/2026-06-18-desktop-source-folder-import/source-files/浴缸过滤器_城市市政自来水版202602讲解.md)（§3.11 防溢 / §3.12 滤棉 / §3.13 KDF 抑膜 / §7 FAQ）

## Obsidian links

- [[bathtub-filter-kes-v1-definition-and-not-for-list]]
- [[bathtub-filter-kes-marketing-site-content-map]]
- [[bathtub-filter-kes-pack-contents-spec]]
- [[bathtub-filter-kes-page-replacement-and-lifespan]]
- [[bathtub-filter-complaint-taxonomy-and-risk-by-route]]
- [[bathtub-filter-marketplace-negative-review-signals]]
- [[bathtub-filter-review-patterns-and-return-risk]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-kes-page-water-test-diagnosis]]
- [[bathtub-filter-supported-spout-matrix]]
- [[bathtub-filter-kes-patent-19-281644-modular-terminal-water-treatment]]
