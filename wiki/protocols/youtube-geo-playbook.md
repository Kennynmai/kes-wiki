# KES YouTube GEO Playbook

> 浴室五金 DTC 品牌 YouTube 频道 GEO 优化操作手册
> 版本：v1.0 | 2026-06-09 | 关联：[YouTube+Pinterest 执行方案](youtube-pinterest-execution-plan.md) | [GEO 六大概念实操指南](../syntheses/kes-geo-howto-six-concepts-2026-06.md)

---

## 目录

1. [核心理念：AI 如何「看」你的视频](#1-核心理念ai-如何看你的视频)
2. [发布前检查清单（每条视频）](#2-发布前检查清单每条视频)
3. [描述区结构化索引模板](#3-描述区结构化索引模板)
4. [字幕质量控制](#4-字幕质量控制)
5. [VideoObject Schema 部署](#5-videoobject-schema-部署)
6. [视频内容 → 博客转写管线](#6-视频内容--博客转写管线)
7. [频道级 GEO 信号](#7-频道级-geo-信号)
8. [监控与迭代](#8-监控与迭代)

---

## 1. 核心理念：AI 如何「看」你的视频

### AI 不「看」画面

当 ChatGPT、Perplexity、Google AI Overviews 回答用户问题时，它们**完全不看你的视频画面**。它们只看：

```
┌─────────────────────────────────────────────┐
│                                             │
│  视频文件  ──→  ❌ AI 不解析画面            │
│                                             │
│  音频      ──→  字幕/转录文本              │
│  描述区    ──→  手写描述（AI 读全部）       │
│  标题      ──→  关键词信号                  │
│  Tags      ──→  弱信号                      │
│  Schema    ──→  结构化元数据               │
│                                             │
│         ↳ 这五层文本 = AI 对视频的全部认知   │
└─────────────────────────────────────────────┘
```

### 三层 GEO 覆盖模型

| 层 | 内容 | 谁在用 | 优先级 |
|---|------|--------|--------|
| **层 1：转录/字幕** | 视频中说的每一句话 | Google 索引 + AI 引用 | 🔴 必须 |
| **层 2：描述区结构化索引** | 章节时间戳 + 问题清单 + 规格数据 | YouTube 搜索 + AI 引用 | 🔴 必须 |
| **层 3：VideoObject Schema** | 机器可读的元数据（时长、缩略图、上传日期） | Google Rich Results | 🟡 推荐 |

---

## 2. 发布前检查清单（每条视频）

### 必须项（P0 — 缺一不可）

```
□ 标题含主关键词 + 副关键词，格式：「[核心主题] | [应用场景]」
□ 字幕已上传（非仅依赖 auto-generated）
□ 字幕已手动校正专业术语
□ 描述区包含 YouTube Chapters（至少 3 个，第一行 0:00）
□ 描述区包含「涵盖问题」清单（3-8 个 Q）
□ 描述区包含产品关键规格数据（材质、认证、标准编号）
□ 描述区包含最多 10 个 Hashtag（优先：品类 + 材质 + 场景）
□ 视频页面（keshome.com 嵌入页）已部署 VideoObject Schema
```

### 推荐项（P1 — 尽量做）

```
□ 描述区包含「安装手册/产品页」链接
□ 描述区包含「相关视频」链接
□ 标签栏填满（不是只在描述区写 #tags，要在 Tags 字段填写）
□ 自定义缩略图含文字标注
□ 播放列表归类
```

---

## 3. 描述区结构化索引模板

### 完整模板（直接复制使用）

```markdown
【视频章节】
0:00 - [阶段一标题]
X:XX - [阶段二标题]
...
XX:XX - [总结/CTA]

【本视频涵盖的问题】
Q: [问题一]？
Q: [问题二]？
...

【提及的关键规格】
- 材质/标准：[具体数值 + 标准编号]
- 尺寸/承重：[数据]
- 认证：[证书名称 + 机构]

【相关资源】
- 产品页：https://keshome.com/product/xxx
- 安装手册：https://keshome.com/installation/xxx
- 相关视频：[链接]

【关于 KES】
成立于 1997 年，服务 1500 万+ 客户。所有产品通过 IAPMO cUPC 认证，在自有测试实验室完成承重及耐久性测试。了解更多：https://keshome.com

#KESbathroom #bathroomhardware #[材质] #[品类] #[场景]
```

### 章节标题命名规则

| ✅ 好的标题 | ❌ 差的标题 | 为什么 |
|-----------|-----------|--------|
| 钻孔定位技巧（附测量方法） | 第二步 | AI 知道这个章节在讲什么 |
| 304 vs 201 不锈钢：磁铁测试对比 | 材质对比 | 含具体关键词 |
| M6 vs M8 膨胀螺丝选择指南 | 选螺丝 | 含具体规格 |
| 密封防水：硅胶 vs 生料带 | 防水步骤 | 含对比关键词 |

### 问题清单写作规则

- 每个 Q 必须是一个**自然语言查询**——用户会如何搜索这个问题
- 视频中必须**实际回答了**这个问题
- 3-8 个 Q，不宜过多

**示例：304 不锈钢置物架安装视频**

```markdown
【本视频涵盖的问题】
Q: 浴室砖墙怎么装不锈钢置物架？
Q: 钻孔深度和螺丝长度应该怎么计算？
Q: 如何判断买到的到底是不是真304不锈钢？
Q: 装好后怎么测试承重是否安全？
Q: 浴室潮湿环境需要做哪些防水处理？
```

---

## 4. 字幕质量控制

### 为什么手动校正字幕是 GEO 的基础

Google 和 AI 搜索对视频的**主要理解来源 = 字幕文本**。如果字幕把专业术语识别错了：
- 「ceramic disc cartridge」（陶瓷阀芯）→「ceramic disk cartridge」（错误）
- 「SUS304 stainless steel」→ 「sauce 304 stainless steel」（完全错）
- 「IAPMO cUPC certified」→ 「IAP more see you PC certificate」（废了）

**AI 就永远不会因你的专业内容而引用你的视频。**

### 字幕操作流程

```
Step 1: YouTube Studio → 字幕 → 选择视频
Step 2: 下载 auto-generated 字幕文件 (.srt)
Step 3: 用文本编辑器打开，逐行检查术语
Step 4: 上传校正后的 .srt 文件替换自动字幕
Step 5: 发布
```

### KES 专业术语标准表（字幕校正参考）

| 中文 | 标准英文 | 常见自动识别错误 |
|------|---------|----------------|
| 304不锈钢 | SUS304 stainless steel | sauce 304 / 304 stainless still |
| 陶瓷阀芯 | ceramic disc cartridge | ceramic disk cartridge / ceramic disc cartage |
| cUPC 认证 | cUPC certified | see you PC / see UPC |
| IAPMO | IAPMO | IAP more / I app more |
| 膨胀螺丝 | expansion anchor / wall plug | expansion anker |
| 石膏板锚栓 | toggle bolt / snap toggle | toggle boat / snap toggle |
| 生料带 | PTFE tape / plumber's tape | PTF tape / plumber step |
| 密封垫圈 | gasket / sealing washer | gas kit |

> 💡 **建议**：将上表贴在剪辑电脑旁边。每次校对字幕时逐项搜索替换。

### 多语言策略

如果目标是美国市场：
- 主字幕：**英文字幕**（AI 主要索引）
- 副字幕：中文字幕（辅助，中国 AI 生态如 DeepSeek/豆包可能索引）

---

## 5. VideoObject Schema 部署

### 这是什么？

VideoObject Schema 是一种结构化数据标记，告诉 Google 这个网页嵌入了视频、视频的时长是多少、缩略图在哪里、什么时候上传的。

### 在 keshome.com 上的部署

**场景**：为每个产品/教程页创建嵌入视频的 blog post，视频来自 YouTube embed。

**代码**（放在 WordPress 页面/文章的 `<head>` 中）：

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "KES 304不锈钢置物架完整安装教程",
  "description": "砖墙/石膏板墙体评估、钻孔、膨胀螺丝选择、防水密封、承重测试的完整安装演示",
  "thumbnailUrl": "https://i.ytimg.com/vi/VIDEO_ID/maxresdefault.jpg",
  "uploadDate": "2026-06-09T08:00:00+08:00",
  "duration": "PT19M30S",
  "contentUrl": "https://www.youtube.com/watch?v=VIDEO_ID",
  "embedUrl": "https://www.youtube.com/embed/VIDEO_ID",
  "interactionStatistic": {
    "@type": "InteractionCounter",
    "interactionType": { "@type": "WatchAction" },
    "userInteractionCount": "1234"
  }
}
</script>
```

**WooCommerce 实现**：
- 方式 A：Rank Math SEO → 编辑页面 → Schema → Video → 填写信息
- 方式 B：在主题 `functions.php` 中动态输出（开发量小）

---

## 6. 视频内容 → 博客转写管线

### 为什么要做

一条视频 = 多个可被 AI 引用的资产：

```
一条 15 分钟视频
    ├── YouTube 视频本身（层 1：字幕 + 层 2：描述区）
    ├── keshome.com Blog 文章（完整转录 + FAQ Schema + VideoObject Schema）
    ├── Reddit 帖子摘要（简版 + YouTube 链接）
    ├── 社交媒体片段（TikTok/Reels 简版）
    └── Pinterest Idea Pin（安装步骤图）
```

**AI 从多个来源交叉引用同一内容 → 引用该信息的概率倍增。**

### 管线流程

```
Step 1: 视频发布（YouTube）— 使用以上完整模板
Step 2: 下载校正后字幕文件 (.srt)
Step 3: 转换为 Markdown 格式博客文章
        - 自动：srt → text → ChatGPT 整理章节 → Markdown
        - 手动：30 分钟润色 + 加图片
Step 4: 发布到 keshome.com/blog/transcripts/[video-slug]/
        - 嵌入 YouTube 视频
        - 部署 VideoObject Schema
        - 部署 FAQPage Schema（基于视频中回答的问题）
Step 5: 发布 Reddit 摘要帖（r/HomeImprovement / r/DIY 等）
Step 6: 社媒切片（60s Shorts / TikTok）
```

### 博客文章模板

```markdown
# [视频标题]

> 视频教程：[YouTube 链接] | 时长：[XX:XX]

## 视频概览

[2-3 句话总结]

## 内容导航

| 时间戳 | 章节 |
|--------|------|
| 0:00 | ... |
| ... | ... |

## 完整教程

### 第 1 步：[章节标题]

[转录文字，整理为可读段落]

### 第 2 步：[章节标题]

...

## 关键数据总结

| 项目 | 数据 |
|------|------|
| ... | ... |

## 常见问题

[FAQ 区块 — 会自动转为 FAQPage Schema]
```

---

## 7. 频道级 GEO 信号

### 频道首页优化

| 元素 | 优化内容 |
|------|---------|
| 频道名称 | `KES Bathroom`（简洁 + 品类词） |
| 频道描述 | 含品牌信息 + 产品品类 + 认证 + 成立年份 |
| 频道横幅 | 含品牌 Logo + 关键认证 Logo（cUPC / NSF） |
| 播放列表 | 按品类/视频类型分类（安装教程、材质科普、产品展示、行业洞察） |
| 频道链接 | 加 keshome.com + 各社媒平台 |

### 频道描述模板

```
KES Bathroom — Founded in 1997, serving 15M+ customers worldwide.

We make bathroom hardware backed by real engineering:
🔬 In-house testing lab | ✅ IAPMO cUPC certified | 🔩 SUS304 stainless steel

What we cover:
• Installation guides for bathroom shelves, towel bars, shower systems
• Material science: 304 vs 201 stainless, finishes, corrosion resistance
• Product reviews and load testing

New videos every Wednesday & Saturday.
Learn more: https://keshome.com

#bathroomhardware #304stainless #bathroomrenovation #DIYbathroom
```

### 频道级信号汇总

| 信号 | 对 AI/Google 的价值 |
|------|-------------------|
| 频道描述含品牌 + 认证 + 统计 | 被 Google Knowledge Graph 作为实体信号抓取 |
| 播放列表按品类分类 | AI 理解频道内容结构 |
| 频道链接指向官网 | 强化域名权威 |
| 一致的发布频率 | Google 信任因子 |

---

## 8. 监控与迭代

### 月度 GEO 自检

每月第 1 个工作日检查：

```
□ Top 10 视频的字幕是否有未校正的专业术语错误？
□ Top 10 视频的描述区是否使用了完整的结构化索引模板？
□ 过去一个月，有没有视频被嵌入到 keshome.com blog 页？
□ 在 ChatGPT/Perplexity 搜索 5 个核心关键词，KES 视频是否出现在引用中？
□ YouTube Analytics → 流量来源中「外部网站」的占比是否增长？
□ 视频描述区中的产品链接是否仍然有效？
```

### AI 引用追踪查询（每月执行）

在 ChatGPT/Perplexity 中搜索以下查询，记录 KES 视频是否被引用：

1. `how to install bathroom shelf on tile wall`
2. `304 vs 201 stainless steel bathroom hardware`
3. `bathroom shelf weight capacity test`
4. `how to seal bathroom hardware waterproof`
5. `expansion anchor size guide bathroom`

---

> **关联文档**：[YouTube+Pinterest 执行方案](youtube-pinterest-execution-plan.md) · [KES 社区内容运营指南](kes-community-voice-guide.md) · [GEO 六大概念实操指南](../syntheses/kes-geo-howto-six-concepts-2026-06.md) · [KES GEO 落地执行方案](../syntheses/kes-geo-implementation-plan-2026-06.md)
