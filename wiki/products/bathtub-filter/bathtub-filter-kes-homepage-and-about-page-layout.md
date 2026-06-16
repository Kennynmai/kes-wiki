---
type: product
status: draft
owner: strategy
created: 2026-06-15
updated: 2026-06-15
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, landing-page, homepage, about-page, copy, layout, dtc]
source_count: 3
related:
  - ./bathtub-filter-kes-clean-formula-emotional-positioning.md
  - ./bathtub-filter-kes-media-eeat-and-clean-formula-narrative.md
  - ./bathtub-filter-kes-transparent-box-hero-shot-script.md
review_cycle: monthly
verification_status: working
---

# KES Bathtub Filter · 独立站首屏 + About 页落地版式

> 把 [Clean-Formula 感性定位](./bathtub-filter-kes-clean-formula-emotional-positioning.md) 落成可交付前端的**版式 + 文案 slot**。
> 漏斗逻辑：**感性让人停下 → reframe 让人认出自己 → villain 让人不安 → 透明盒解围 → 证据让人相信 → disclaim 让人信任 → CTA**。
> 全程红线：反派是**不透明**不是化学物质；**可见 ≠ 有效**（不暗示改善皮肤）；不 toxin-panic；认证口径如实。

---

## 一、首页（Homepage · 滚动分区）

> **排版与移动端原则（designer 不能破坏漏斗）**：每屏只讲一件事；冷访客的第一屏是**钩子（reframe 问题）**不是品牌口号；透明盒视觉在每个关键区块复现（它是感性+理性的共用证据）；移动端 9 块顺序不变、图文垂直堆叠。

### 区块 1 — Hero（首屏，above the fold）　✅必须达成：3 秒内让冷访客认出「这说的是我」
**版式**：左文右图（移动端图上文下）。右侧**透明滤盒英雄镜头**为绝对主角（见 [镜头脚本](./bathtub-filter-kes-transparent-box-hero-shot-script.md)）。
**文案**：
- Eyebrow（小字）：`看得见的滤料。读得懂的配方。`（EN：`Filter media you can see. A formula you can read.`）
- H1（钩子）：`你读食品的配料表，你读护肤的成分表。你的洗澡水呢？`
  （EN：`You read your food labels. You read your skincare. What about your bath water?`）
- Sub：`透明滤盒——料、量、层序，全看得见。干净，是你看得见的事实。`
  （EN：`A clear cartridge — the media, the amount, the order, all visible. Clean is what you can see.`）
- CTA 主：`找到你家的水`（EN：`Find your water`）→ 区块 6　｜　CTA 次：`看看盒子里有什么`（EN：`See what's inside`）→ 区块 4
**注**：首屏不放未实测数字；25L/min 去氯率待 [台架 spec](./bathtub-filter-25lpm-dechlorination-bench-test-spec.md) 坐实后才进 Hero。

### 区块 2 — The Reframe（识别瞬间）　✅必须达成：把「读标签」这个已认同的自己，迁移到洗澡水
**版式**：全宽，大字、留白，像一句被读出来的话（逐行入场动效，慢节奏）。
**文案**：
> `你本来就是个会读标签的人。`
> `食品翻背面，护肤查成分——读不懂、藏起来的，你放回货架。`
> `可有一样你天天用，从没翻过来看：你的洗澡水。`
（EN：`You've always read the label. / The back of the food. The actives in the serum — if you can't read it, you put it back. / But there's one thing you use every day and never turn around: your bath water.`）

### 区块 3 — The Villain（黑箱）
**版式**：左右对照——左「不透明竞品滤芯（黑箱）」，右「KES 透明盒」。
**文案**：
- 左标签：`别人的滤芯：一把你看不见的杂豆，几行你查不到的承诺。`
- 右标签：`KES：翻过来，看进去。`
- 一句：`它们赌你不会去看。我们把盒子做成透明的。`
**红线**：对照图**不得**出现「脏水/毒水」恐吓画面；villain 是「看不见」，不是「有毒」。

### 区块 4 — See Inside（透明盒揭示 · 成分美学）
**版式**：滤料 macro 特写横滑 / 逐层拆解图，标签式排版（真名真量）。
**文案**：
- `这是 KDF 铜锌合金。这是亚硫酸钙。没有第三种你叫不出名字的东西。`
- 逐层注释：`① PP 棉先拦颗粒 → ② KDF 铜锌合金 → ③ 亚硫酸钙去游离氯`（水流向标注）
- `没有躲在不透明塑料背后的便宜填料。`
**注**：metal-first 在此是**料级/工程叙事**（看得见的好料），**非去重金属健康声称**。

### 区块 5 — Test It Yourself（证据 · 理性接缝）
**版式**：氯试纸自测 demo（动图/短视频）+ 第三方测试徽标位（待出报告）。
**文案**：
- `别信我们，自己测。`（EN：`Don't take our word for it. Test it yourself.`）
- `每盒附赠氯试纸。`＋`第三方实验室在标注流量下实测去氯率。`（report 出来前此行用占位、不写具体数字）
**注**：这是「测得到」理性半边的入口；把 [EEAT 证据模块](./bathtub-filter-kes-media-eeat-and-clean-formula-narrative.md) 在 PDP 展开。

### 区块 6 — Match Your Water（支撑层 + 防呆）
**版式**：交互选择器（前端水质 qualification），三选一卡片。
**文案**：
- 标题：`你家的水，不该用别人家的滤芯。`
- 卡片：`游离氯城市` / `氯胺城市` / `私人井水` → 各自推荐**预配方**（不卖散料，物理防呆见产品定义）
- 不确定引导：`不知道你家是哪种？输入 ZIP 查一下。`
**注**：这是把「自由组合」做成**被引导的选择**——解决组错顺序/买错的风险。

### 区块 7 — What We Won't Say（disclaim 即信任）
**版式**：安静的诚实带，深色或留白，单列。
**文案**：
> `我们不会替你下结论，说它能"治"好什么。`
> `它不软化硬水。它不是医疗器械。它不去除重金属当健康卖点。`
> `它做一件事，并把这件事测给你看：减少游离氯。`
**红线承重句**：第一行**不可删**（主动 disclaim 疗效，守 A-10）。

### 区块 8 — Real Proof（社会证明 + 认证 · 理性）
**版式**：真实评价（含评分分布、不删负评）+ 认证标志（如实口径）。
**文案**：`真实评价，好的坏的都在。` ＋ `KDF55 继承 NSF/ANSI 42 材料端。`（**不冒认成品 NSF**）

### 区块 9 — Final CTA
**文案**：`看得见的滤料。读得懂的配方。` ＋ 主 CTA `找到你家的水` / 次 `读读我们为什么这么做`（→ About）

---

## 二、About 页（品牌宣言之家 · 长文案承载）

### 结构
1. **宣言全文**（[§5.1 中文长版 / §5.2 英文 ship 版](./bathtub-filter-kes-clean-formula-emotional-positioning.md)）——About 页主体，大字、慢节奏排版。
2. **我们为什么把盒子做透明**：接 KES brand「Metal First. No plastic shortcuts.」——透明是 metal-first 诚实的延伸；自有实验室、29 年制造，让「看得见 + 测得到」有底气（接 [brand EEAT roadmap](../../playbooks/kes-dtc-eat-implementation-roadmap-2026-06.md)）。
3. **我们不说什么**（边界即品牌）：把 §七红线表的「禁说清单」正面写出来——`不治湿疹 / 不软化 / 不去重金属当健康卖点 / 不 toxin-panic`。**主动列禁区是最高级 trust 信号**，直接对照对手的越界。
4. **Maker 署名**：测试工程师/资质署名（接 EEAT「Who Made This」），强化一手经验。

### About 页语气
- 第一人称、直白、克制（语气支柱见定位页 §八）。
- **不**讲增长故事/融资/宏大愿景；只讲「我们为什么让你看见」。

---

## 三、合规 / 红线检查（上线前逐条过）
- [ ] 全站无 "chemical-free / toxin-free / non-toxic" 伪科学绝对化
- [ ] 无「改善/治疗皮肤/湿疹」或 baby-safe 医疗式安心
- [ ] 无「去除重金属」健康卖点（metal-first 仅料级叙事）
- [ ] villain 视觉为「不透明」非「脏水/毒水」
- [ ] 「可见」与「实测有效」在文案中分开，不互相暗示
- [ ] 去氯率/认证数字未坐实前用占位，不写具体值
- [ ] disclaim 承重句（区块 7 行 1）在线

---

## 下一步
- ⏳ 待 [25L/min 台架 spec](./bathtub-filter-25lpm-dechlorination-bench-test-spec.md) 出报告 → 回填区块 1/5 去氯率数字
- ⏳ 区块 6 水源选择器 + ZIP 查询的产品/工程实现
- ⏳ 配套视觉：[透明盒英雄镜头脚本](./bathtub-filter-kes-transparent-box-hero-shot-script.md)

## Sources / 内部依据
- [Clean-Formula 感性定位（深化）](./bathtub-filter-kes-clean-formula-emotional-positioning.md)
- [媒体/EEAT + clean-formula 叙事](./bathtub-filter-kes-media-eeat-and-clean-formula-narrative.md)
- [KES DTC E-E-A-T 实施路线图](../../playbooks/kes-dtc-eat-implementation-roadmap-2026-06.md)

## Obsidian links
- [[bathtub-filter-kes-clean-formula-emotional-positioning]]
- [[bathtub-filter-kes-media-eeat-and-clean-formula-narrative]]
- [[bathtub-filter-kes-transparent-box-hero-shot-script]]
- [[bathtub-filter-25lpm-dechlorination-bench-test-spec]]
