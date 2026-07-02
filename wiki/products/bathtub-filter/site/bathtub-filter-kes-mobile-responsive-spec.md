---
type: product
status: draft
owner: strategy
created: 2026-07-02
updated: 2026-07-02
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, mobile, responsive, selector, generator, hub, pdp, ux, performance, a11y, channel-spec, ch3]
review_cycle: monthly
related:
  - ./bathtub-filter-kes-water-match-selector-spec.md
  - ./bathtub-filter-kes-proof-and-testimonials.md
  - ../bathtub-filter-kes-website-copy-v1.md
  - ../bathtub-filter-kes-acquisition-engine-mvp-spec.md
  - ../bathtub-filter-claim-register.md
  - ./bathtub-filter-kes-privacy-terms-and-consent.md
  - ./bathtub-filter-kes-marketing-site-content-map.md
---

# CH3 · 移动端 / 响应式规格（选购器 · Hub · PDP · 生成器）

## 这一页是什么

**冷流量主力 = 移动端**（社媒/搜索到站默认场景），但全站 spec 至今按桌面叙事写。本页给四个关键表面——**选购器（SVC10）、Hub、PDP、分享图生成器（SVC8 §4.7.3）**——补移动规格：断点、交互目标、折叠规则、性能与无障碍基线。

**分工边界**：各表面**说什么**（文案/分岔/护栏）归各自 spec 页（[选购器 spec](./bathtub-filter-kes-water-match-selector-spec.md) / [website-copy](../bathtub-filter-kes-website-copy-v1.md) / [proof 页 §4.7.3](./bathtub-filter-kes-proof-and-testimonials.md)），本页只管**在小屏上怎么呈现**——凡与内容 spec 冲突处，以内容 spec 口径为准、本页版式让位。

---

## 一、断点与移动优先原则

| 断点 | 目标设备 | 规则 |
|---|---|---|
| **360px（基线）** | 主流 Android / 小屏 iPhone | **设计从这里开始**：所有表面先画 360 再放大；360 上放不下的内容 = 该砍或该折叠，不是该缩字 |
| 768px | 平板 / 大屏手机横屏 | 单栏 → 双栏过渡点；表格开始允许回表格形态 |
| 1024px+ | 桌面 | 桌面版式（既有 spec 默认叙事） |

**移动优先三原则**：

1. **单手可达**：主 CTA 与高频交互放**拇指区**（屏幕下半）；顶部只放信息不放必点按钮。
2. **触控目标 ≥44×44px**（含点选色块、单选项、CTA；间距 ≥8px 防误触）。
3. **承重句不折叠**（§四）：合规承重内容的可见性是 claim 义务，不是版式偏好——折叠策略永远只折解释，不折结论。

---

## 二、选购器移动规格（本页重点）

> 内容/分岔树/护栏全部沿 [选购器 spec](./bathtub-filter-kes-water-match-selector-spec.md)，此处只定移动呈现。

### 2.1 交互框架

| 项 | 规格 |
|---|---|
| **每屏一问** | Q1/Q2/Q3/ZIP 各占一整屏（视口内完成，不滚动作答）；选项即大按钮，点选即前进，无「下一步」二跳 |
| 点选目标 | 选项按钮全宽或半宽色块，**高度 ≥44px**；试纸读色类输入用**色块点选**（复用生成器的零打字设计，SVC8 §4.7.3） |
| 单手可达 | 选项列表纵向排布、重心在屏幕下 2/3；「返回上一问」放左下角固定位 |
| **进度指示** | 顶部轻量进度条或步点（如 `1/3`）；🔴 不用百分比游戏化（这是诊断不是测验）；劝退分岔到达时进度指示**照常走完**——劝退也是一个「完成」，不是中断 |
| ZIP 输入 | 数字键盘唤起（`inputmode="numeric"`）；5 位自动提交；错误态就地提示不弹窗 |
| 无注册墙 | 沿选购器 spec §四：所有结果（含劝退）不注册可看；邮箱字段只在劝退/等待分岔出现，且**单字段 + 一句给什么**，不做多字段表单 |

### 2.2 劝退分岔的小屏折叠策略（关键）

劝退文案（氯胺 / RO / 全屋炭工作中 / 井水红旗）在小屏的呈现规则：

- **结论行永不折叠**：`"V1 isn't for your water yet."` / `"You don't need us."` 级别的结论句必须在结果首屏完整可见——**劝退的诚实价值就在第一眼**，折叠结论 = 变相软化劝退。
- **解释可折叠**：为什么氯胺不适用 / 炭床穿透机理等教育内容收进 `Read why ▾` 折叠区或链接到 E 页（E11/E1），展开不跳页。
- **邮箱字段跟随结论同屏**（不折叠、不下滚才见）：劝退→候补的转化动作必须零滚动可达。
- 🔴 折叠区内**不得藏合规承重句**（如阻垢选项处的 "It does not soften your water." 必须与选项本体同屏同视野，见 §四）。
- 🔴 劝退页无加购 CTA（选购器 spec §五 #3）——移动版也不得以 sticky bar 形式出现购买入口。

### 2.3 结果页（适配分岔）

- 推荐卡：SKU + 一键加购在首屏拇指区；精度句（"one ZIP can span more than one water system…"）紧贴结果**不折叠**（选购器 spec §五 #1）。
- 硬度追加的阻垢选项：选项与 "It does not soften your water." **同一卡片内**渲染，不允许版式拆散。

---

## 三、生成器移动规格（SVC8 §4.7.3 的移动实现）

> 生成器**本来就是移动场景产品**（扫卡上 QR 进入），移动是主形态不是适配。

| 项 | 规格 |
|---|---|
| **canvas 出图分辨率** | 固定输出 **1080×1920（story）+ 1080×1080（feed）** 两档（proof 页 §4.7.3 已定），与设备屏幕分辨率解耦——canvas 按输出尺寸离屏渲染，预览缩放显示；devicePixelRatio 只影响预览清晰度不影响出图 |
| **原生分享** | 首选 **`navigator.share()`**（Web Share API Level 2，带 `files` 传图）：一键唤起系统分享面板，直达 IG/iMessage/微信等。特性检测降级链：`navigator.share(files)` → `navigator.share(url)` + 提示保存图片 → 显示图片 + 保存指引 |
| **iOS Safari 保存图片路径** | iOS Safari **不支持 `<a download>` 直接下载图片到相册**。路径说明（需内置到 UI 文案）：① 优先 `navigator.share(files)`（iOS 15+ 支持，分享面板内有「保存图像」）；② 降级：把 canvas 以 `<img>` 呈现 + 指引 **长按图片 →「存储图像」**；🔴 不做「点击下载」按钮假动作（iOS 上会开新标签或存到「文件」，用户找不到 = 分享流程死在最后一步） |
| 输入交互 | BEFORE/AFTER 色块点选按钮 ≥44px；零打字（proof 页已定）；城市选填走 ZIP 前 3 位 |
| 文本战报出口 | 「Copy as text」用 Clipboard API + 成功态 toast；emoji 色块网格在系统字体下逐机型走查 `[____ 待工程]` |
| 合规继承 | 品牌模板零自由文本 / 白名单词库 / 零 PII（proof 页 §4.7.3）——移动 UI 不得为「个性化」加自由输入框 |

---

## 四、Hub / PDP 移动规格

### 4.1 首屏承重句不被折叠（承重规则）

- **"This is not a water purifier. It does not target TDS reduction."** 必须在 Hub 与 PDP 的**移动首屏可见**（register Positioning 行：must appear on every customer-facing surface——「表面」在移动端指首屏，不是「页面某处」）。
- 版式实现：承重句作为 Hero sub-copy 或首屏定位条，**不进折叠区、不进轮播第 2 帧、不被 cookie banner/promo bar 挤出视口**（360×640 最小视口下验收）。
- 同理不折叠清单：PDP 的 "free chlorine" 限定 + "fresh-filter / 15 L/min" 限定词随其所修饰的 claim 同屏；What We Won't Say 区块的第一行承重句（"We won't tell you it 'treats' anything."）到达该区块时完整可见，不做 `…more` 截断。

### 4.2 锚点导航

- PDP 长页配**锚点条**（sticky，收缩为图标 + 短标签）：`What's inside / How it works / Testing / Replacement / FAQ / Fit`——对应 website-copy PDP 区块。
- 锚点跳转保留浏览器回退语义（hash 路由），从选购器/广告深链进入可直达锚点（如 `#fit`）。
- Hub 的 Match-Your-Water 区块（选购器入口）在移动首屏给**次级 CTA 直达**（website-copy 区块 6 是转化主路径）。

### 4.3 表格 → 卡片化规则

全站 spec 里的宽表（P4 兼容矩阵 S-01~S-08、P5 水型速查、T3 触发曲线表等）在 <768px 一律按此规则转卡片：

1. **一行 = 一卡**：行主键（如龙头类型）作卡标题，列变为卡内「标签: 值」纵排。
2. **判定列前置**：✅/⚠️/❌ 判定放卡标题行右侧，扫一眼可分拣。
3. **边界列不省略**：「不支持条件」列在卡片内**必须保留全文**——兼容边界是 claim 的一部分（register Fit 行），🔴 不得因卡片化砍掉「不支持」信息。
4. 超过 6 卡的矩阵加前置筛选（如「我的龙头有提拉头 y/n」）优先路由，替代整表滚动。

---

## 五、性能预算与无障碍基线

### 5.1 性能预算 `[____ 待工程]`

| 指标 | 目标 | 说明 |
|---|---|---|
| LCP | `[____ 待工程]`（建议向 ≤2.5s @ 4G 中端机对齐） | 冷流量落地页（Hub/选购器）优先；Hero 实拍图出尺寸裁切 + 懒加载首屏外资产 |
| CLS | `[____ 待工程]`（建议向 ≤0.1 对齐） | 图片/嵌入区块预留尺寸；承重句区块不得因异步加载位移出首屏（CLS 在这里是合规问题不只是体验问题） |
| INP / 交互延迟 | `[____ 待工程]` | 选购器为纯客户端状态机 + 静态 JSON（MVP spec §5），本身极轻；生成器 canvas 渲染放 rAF/离屏，不阻塞点选 |
| 预算归属 | 每表面单列（Hub / 选购器 / PDP / 生成器），广告落地以选购器为最严档 | 工程定稿后回填本表 |

### 5.2 触控 / 字号无障碍基线

- 触控目标 ≥44×44px（§一）；正文字号移动端 ≥16px（同时防 iOS 聚焦自动缩放），辅助文字 ≥13px；色块点选控件**必须带文字/数值双编码**（色阶按钮标注 ppm 区间——色弱用户可用，也符合 T1「读数非猜色」口径）。
- 对比度、焦点态、屏读语义、表单标签等完整 a11y 基线**引 [SVC12 隐私/ToS/同意/无障碍页](./bathtub-filter-kes-privacy-terms-and-consent.md) a11y 节**（该页同批在建，前向链接；WCAG 基线以该页为唯一口径，本页不重复定标准）。
- 生成器输出图含色块信息 → 分享图 alt 文案模板进白名单词库 `[____ 待市场+法务]`。

---

## 六、验收清单（移动专项）

- [ ] 360×640 视口：Hub / PDP 首屏可见 "not a water purifier" 承重句（无 banner 遮挡态与有 banner 态各验一次）。
- [ ] 选购器每问单屏完成、选项 ≥44px、进度指示在场；劝退分岔结论句 + 邮箱字段零滚动可见，解释折叠可展开。
- [ ] 阻垢选项与 "It does not soften your water." 同卡同屏；劝退页无任何购买入口（含 sticky bar）。
- [ ] 生成器：iOS Safari 真机走通「出图 → navigator.share 保存/分享」与降级「长按保存」两条路径；1080×1920 与 1080×1080 两档出图像素正确。
- [ ] 宽表卡片化后「不支持」边界信息零丢失（对照 P4 矩阵逐行核）。
- [ ] 承重句区块在慢网模拟下无加载位移（CLS 专项）。
- [ ] a11y 基线逐条对 SVC12 a11y 节走查（该页定稿后）。

### `[____]` 待补清单

| 项 | 负责 |
|---|---|
| LCP / CLS / INP 数值定稿 `[____]` | 工程 |
| 生成器 emoji 网格逐机型渲染走查 `[____]` | 工程 |
| 分享图 alt 模板入白名单词库 `[____]` | 市场 + 法务 |
| SVC12 a11y 节定稿后回链核对 `[____]` | 产品 |
| 选购器 768px+ 桌面版式（本页只定移动，桌面沿选购器 spec） `[____]` | 设计 |

---

## Sources / 内部依据

- [选购器（Water-Match Selector）spec（分岔树/护栏/技术实现）](./bathtub-filter-kes-water-match-selector-spec.md)
- [proof 页 §4.7.3（生成器：双格式出图/零自由文本/零 PII）](./bathtub-filter-kes-proof-and-testimonials.md)
- [website-copy-v1（Hub/PDP 区块与承重句）](../bathtub-filter-kes-website-copy-v1.md)
- [获客引擎 MVP spec（静态 JSON/无后端/埋点）](../bathtub-filter-kes-acquisition-engine-mvp-spec.md)
- [claim-register（Positioning 行「every customer-facing surface」/ Fit 边界随行）](../bathtub-filter-claim-register.md)
- [SVC12 隐私/ToS/同意/无障碍（a11y 基线唯一口径，同批在建）](./bathtub-filter-kes-privacy-terms-and-consent.md)

## Obsidian links

- [[bathtub-filter-kes-marketing-site-content-map]]
- [[bathtub-filter-kes-water-match-selector-spec]]
- [[bathtub-filter-kes-proof-and-testimonials]]
- [[bathtub-filter-kes-website-copy-v1]]
- [[bathtub-filter-kes-acquisition-engine-mvp-spec]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-kes-privacy-terms-and-consent]]
- [[bathtub-filter-kes-install-and-compatibility-guide]]
- [[bathtub-filter-kes-page-water-test-diagnosis]]
- [[bathtub-filter]]
