# DTC 品牌/产品研究分析框架 v2.2

> **创建日期**: 2026-06-14 | **最后修订**: 2026-06-14 | **状态**: actionable | **版本**: v2.2
> **目的**: 系统性分析和收集 DTC 品牌和产品资料，结合 KES 情况，输出可借鉴的方法、思路和具体打法
> **参考案例**: FilterBaby（浴缸过滤器品类）—— 见 `wiki/brand-studies/filterbaby-dtc-case-study.md`
> **v2.2 变更**: 工具配置全面补充 → last30days 完整配置（xAI cookie/FROM_BROWSER + ScrapeCreators API）、Arctic Shift 状态更新（API ❌ 仅 Web UI）、SellerSprite/Helium 10 数据获取 SOP（KES 已订阅）、Codex 浏览器操作 SEMrush 方法（3 种方案）
>
> **🔗 工具配置详细步骤**: 见补充文档 `wiki/topics/dtc-brand-research-tools-setup-guide.md`（v2.2 新增）

---

## 一、框架概述

### 1.1 为什么需要这个框架

DTC 品牌研究不是「看看竞品在做什么」，而是**系统性解构**：
- 他们如何被发现（SEO / GEO / 社交媒体 / 付费广告）
- 他们如何建立信任（E-E-A-T 信号 / 认证体系 / 社交证明）
- 他们如何转化用户（定价 / 促销 / 着陆页 / 结账体验 / 售后）
- 他们如何积累资产（内容 / 社区 / 品牌 / 数据 / IP）
- 他们如何持续增长（复购 / 推荐 / 产品迭代 / 护城河）
- **他们做对了什么（可复制）+ 他们忽略了什么（KEE 的机会）**

### 1.2 框架的三个输出

| 输出 | 说明 | 格式 | 频率 |
|------|------|------|------|
| **品牌/产品深度报告** | 16 层全维度解构 | `wiki/brand-studies/` | 按需（每次 3-5 工作日）|
| **可复用打法库** | 跨案例提炼的可执行技巧卡片 | `wiki/protocols/dt-tactics/` | 每完成 3 个案例更新一次 |
| **竞品监控面板** | 关键指标持续跟踪 | `dashboards/competitor-watch.md` | 每周更新 |

### 1.3 适用场景与不适用场景

**适用** ✅:
- 研究直接/间接竞品（如 KES 研究 bathroom hardware DTC 品牌）
- 寻找品类机会（如 FilterBaby 的 bathtub filter 品类）
- 学习增长打法（如某品牌如何通过 Reddit 社区驱动增长）
- 对标产品定位（如「Metal First」vs 竞品的差异化策略）
- 投资/收购标的评估（品牌资产深度摸底）

**不适用** ❌:
- 快速扫描（用下面的「5 分钟快速扫描」代替完整 16 层）
- 纯粹价格监控（用「竞品价格追踪表」代替）
- 供应商/工厂研究（用「供应链专项研究」模板）

### 1.4 研究深度分级

| 级别 | 名称 | 时间投入 | 覆盖层数 | 适用场景 |
|------|------|----------|----------|----------|
| **L1** | 快速扫描 | 1-2 小时 | Layer 0-4 | 初步筛选、快速对标 |
| **L2** | 标准研究 | 3-5 天 | Layer 0-9 | 竞品深度分析 |
| **L3** | 完整研究 | 1-2 周 | Layer 0-16 + 财务估算 | 战略决策、投资评估 |
| **L4** | 持续监控 | 每周 1 小时 | 关键指标更新 | 竞品动态跟踪 |

---

## 二、研究分析核心方法论（16 层深度）

### 2.1 分析维度总览

```
                    ┌─────────────────────────────────┐
    【发现层】      │ Layer 0: 发现路径                │  用户怎么找到他们？
                    ├─────────────────────────────────┤
    【品牌层】      │ Layer 1: 品牌定位                │  他们说自己是干嘛的？
                    ├─────────────────────────────────┤
    【产品层】      │ Layer 2: 产品矩阵                │  他们卖什么？怎么组合？
                    │ Layer 3: 定价策略                │  他们怎么赚钱？
                    ├─────────────────────────────────┤
    【信任层】      │ Layer 4: 信任体系 E-E-A-T        │  用户为什么信他们？
                    ├─────────────────────────────────┤
    【内容层】      │ Layer 5: 内容策略                │  他们生产什么内容？
                    │ Layer 6: 社区运营                │  他们在哪里和用户对话？
                    ├─────────────────────────────────┤
    【增长层】      │ Layer 7: 流量结构                │  他们的流量从哪来？
                    │ Layer 8: 转化漏斗                │  从看到到购买的路径？
                    │ Layer 9: 复购 / 留存            │  怎么让用户回来？
                    ├─────────────────────────────────┤
    【竞争层】 ✨    │ Layer 10: 竞争格局               │  他们在和谁竞争？
    【广告层】 ✨    │ Layer 11: 广告创意分析           │  他们怎么花钱获客？
    【供应层】 ✨    │ Layer 12: 供应链与制造           │  产品从哪来？成本多少？
    【技术层】 ✨    │ Layer 13: 技术栈                │  用什么工具建站/运营？
    【团队层】 ✨    │ Layer 14: 团队与资本             │  谁在做？钱从哪来？
    【壁垒层】 ✨    │ Layer 15: 护城河分析             │  他们的优势能持续吗？
    【用户层】 ✨    │ Layer 16: 用户画像与真实反馈     │  用户到底怎么说？
                    └─────────────────────────────────┘
    
    ✨ = v2.0 新增层
```

---

### 2.2 Layer 0：发现路径分析

**目标**: 理解用户在不认识品牌的情况下，如何第一次接触到它。

| 分析项 | 数据来源 | 采集方法 | KES 可借鉴 |
|--------|----------|----------|------------|
| **SEO 可见性** | Google 品类词前 3 页排名 | SEMrush/Ahrefs + 手动搜索 | 关键词策略、内容缺口 |
| **GEO 可见性** | ChatGPT/Perplexity/Google SGE 是否推荐 | 手动提示词查询（见下文） | AI 搜索优化方向 |
| **社交媒体发现** | 各平台搜索品类词/品牌词 | 平台内置搜索 + 手动 | 视觉内容策略 |
| **社区自然提及** | Reddit/Quora/知乎/Discord | RedditSearch.io / GummySearch | 社区营销机会 |
| **PR/媒体报道** | Google News / 行业垂直媒体 | Google News Alerts | PR 策略 |
| **Amazon 存在** | 品类 BSR / 评论数 / 广告位 | Jungle Scout / Keepa | 电商品牌信任度 |
| **视频平台** | YouTube/TikTok/B站 品类搜索排序 | 手动搜索 + Tubebuddy | 视频内容策略 |
| **播客提及** | Apple Podcasts / Spotify 搜索 | ListenNotes API | 创始人内容策略 |

**GEO 可见性测试提示词模板**:

```
1. "What's the best [category] for [use case]?"
2. "I'm looking for a [category]. What options should I consider?"
3. "Compare [Brand A] vs [Brand B] for [category]"
4. "Is [Brand Name] worth it? What do reviews say?"
5. "What [category] do [target audience] recommend?"
```

**输出模板** ⬇️ 保持不变，额外增加：

```markdown
### 发现路径量化评分
| 发现渠道 | 品牌是否存在 | 排名/位置 | 可复制难度(1-5) | KES 应投入 |
|----------|:----------:|-----------|:---------------:|:----------:|
| Google 有机 | ✅ | 第2位 | 4 | 是 |
| Google 付费 | ✅ | 第1位 | 2 | 测试 |
| ChatGPT | ✅ | 被推荐 | 3 | 是 |
| Reddit 自然 | ✅ | 12条提及 | 5 | 强烈建议 |
| Pinterest | ✅ | 120+ Pins | 2 | 已是强项 |
```

---

### 2.3 Layer 1：品牌定位分析

**目标**: 解构品牌的「一句话定位」和支撑证据。

| 分析项 | 分析问题 | 数据来源 | 量化指标 |
|--------|----------|----------|----------|
| **核心定位** | 用一句话怎么介绍自己？ | Hero Banner / About / Meta Description | 定位清晰度 1-5 |
| **价值主张** | 解决什么痛点？痛点是否真实？ | 首页 + 产品页标题 | 痛点匹配度 1-5 |
| **差异化声明** | 和竞品有什么不同？差异是否可验证？ | "Why Us" / 竞品对比页 | 差异化可验证性 1-5 |
| **目标人群** | 为谁服务？是否有清晰 Persona？ | 文案语气 / 模特 / 使用场景 | Persona 清晰度 1-5 |
| **品牌调性** | 专业/亲民/奢华/幽默/极简？ | 视觉风格 / 文案 / 字体 | — |
| **使命/价值观** | 相信什么？是否和用户价值一致？ | About / Manifesto / ESG 页面 | 真实感 1-5 |
| **品牌故事** | 创始人故事？创立原因？ | About / Founder Page / 媒体报道 | 故事感染力 1-5 |
| **视觉识别** | Logo / 配色 / 字体 / 摄影风格是否一致？ | 全站截图对比 | 一致性评分 1-5 |
| **品牌声量** | 品牌词月搜索量？品牌提及趋势？ | Google Trends / SEMrush / Brand24 | 声量趋势 ↗️→↘️ |

**定位语句拆解 — 解剖公式**:

```
「定位 = 为 [谁] 提供的 [什么]，因为 [差异化理由]」

FilterBaby:
  → 为 [租房者] 提供的 [浴缸过滤器]，因为 [无需工具 + 不损坏浴缸]

Allbirds:
  → 为 [关注舒适和可持续的都市人] 提供的 [鞋]，因为 [天然材料 + 极简设计]

KES 可尝试:
  → 为 [租房者和 DIY 房主] 提供的 [浴室五金]，因为 [全金属构造 + 免打孔安装]
```

---

### 2.4 Layer 2：产品矩阵分析

**目标**: 理解产品组合、SKU 策略、交叉销售逻辑。

| 分析项 | 说明 | 输出 |
|--------|------|------|
| **核心产品** | 主打 SKU（占收入 >30% 的） | 产品清单 + 价格 + 评价 |
| **产品线结构** | 按功能/价格/场景分级 | 产品矩阵图 |
| **配件/耗材** | 高毛利长尾配件 | 清单 + 定价 + 毛利估算 |
| **捆绑销售** | 提高 AOV 的组合策略 | 捆绑方案 + 折扣力度 |
| **限时/限量产品** | 稀缺性策略 | 发布频率 + 售罄速度 |
| **变体策略** | 颜色/尺寸/材质变体数量 | 变体矩阵 |
| **产品命名** | 命名规则是否清晰？ | 命名逻辑分析 |
| **包装/开箱体验** | 拆包第一印象 | 照片 + 评分 |
| **产品生命周期** | 新品发布频率？旧款下架节奏？ | 时间线 |
| **退货/品控** | 负面评价集中在哪些产品？ | 差评分析 |

**新增分析维度**:

```markdown
### 产品 SKU 效率分析
| 指标 | 估算 |
|------|------|
| 总 SKU 数 | XXX |
| 前 5 SKU 收入占比（估算） | XX% |
| 平均每个 SKU 评价数 | XX |
| 评价 <10 的 SKU 占比 | XX% —> 可能表现差 |
| 缺货 / 下架 SKU 数 | XX —> 产品管理问题信号 |
```

---

### 2.5 Layer 3：定价策略分析

**目标**: 理解定价逻辑、利润结构和促销节奏。

| 分析维度 | 问题 | 采集方法 |
|----------|------|----------|
| **价格段位** | 高端/中端/低端？和竞品差距？ | 竞品全网比价 |
| **价格锚点** | 最高价SKU用于锚定？主推SKU价格？ | 产品页排序分析 |
| **价格尾数** | .99 / .95 / .00？什么心理策略？ | 全 SKU 价格尾数统计 |
| **促销节奏** | 多久打折？折扣力度？ | Keepa (Amazon) + 官网邮件观察 |
| **订阅折扣** | 订阅省多少？ | 结算页测试 |
| **运费策略** | 免运费门槛？国际运费？ | 加购测试 |
| **退款保证** | 退货窗口？是否有"试用期"？ | 政策页面 |
| **价格历史** | 过去 12 个月价格波动？ | Keepa / CamelCamelCamel / Wayback Machine |
| **隐藏成本** | 安装费？配件必须买？ | 用户评论挖掘 |
| **价格心理学** | "原价 $199 → 现价 $89" 是否为假锚定？ | 历史价格验证 |

**价格历史追踪方法**:

```
Amazon 产品:
  1. 复制 ASIN
  2. Keepa.com → 查看 12 个月价格曲线
  3. 记录: 最低价、最高价、促销频率、Prime Day/黑五价格

官网:
  1. Wayback Machine (archive.org)
  2. 输入产品页 URL
  3. 对比不同时间点的标价变化
```

---

### 2.6 Layer 4：信任体系分析（E-E-A-T 强化版）

**这是最重要的层**。DTC 品牌的生死取决于信任——尤其对于 YMYL（Your Money Your Life）品类如浴室五金、水质过滤器。

| E-E-A-T 维度 | 分析项 | 数据来源 | 评分 |
|---------------|--------|----------|:----:|
| **Experience** | 真实使用场景展示 | 用户 UGC、安装视频、Before/After | /5 |
| | 产品拆解/对比视频 | YouTube 搜索 "brand + review" | /5 |
| | 用户生成内容的数量和质量 | 各平台 #品牌标签 内容 | /5 |
| **Expertise** | 技术知识展示深度 | 技术指南、白皮书、参数完整度 | /5 |
| | 认证/测试报告可查证性 | 认证编号是否可在线验证 | /5 |
| | 团队技术背景 | About 页面、LinkedIn | /5 |
| **Authoritativeness** | 第三方媒体/机构引用 | Google News、行业媒体、评测网站 | /5 |
| | 行业认证标志 | cUPC/NSF/WaterSense 等可查证标志 | /5 |
| | KOL/专家推荐 | YouTube/Instagram/Blog 合作 | /5 |
| | Wikipedia 词条 | 如有 | /5 |
| **Trustworthiness** | 评价真实性（好评 + 差评） | Amazon + Trustpilot + 官网 | /5 |
| | 联系信息完整度 | 地址、电话、邮箱、真人照片 | /5 |
| | 政策透明度 | 退货、保修、隐私政策清晰度 | /5 |
| | 材料/成分完整披露 | 材质清单、产地信息 | /5 |
| | 第三方安全认证 | TrustedSite / Norton / McAfee | /5 |

**E-E-A-T 综合评分卡**:

```markdown
## 信任体系评分

| 维度 | 评分(1-5) | 权重 | 加权分 |
|------|:--------:|:----:|:------:|
| Experience | 3 | 25% | 0.75 |
| Expertise | 4 | 25% | 1.00 |
| Authoritativeness | 3 | 25% | 0.75 |
| Trustworthiness | 4 | 25% | 1.00 |
| **总分** | | | **3.50 / 5** |

对比: KES 当前得分 XX / 5 —> 差距在 [具体维度]
```

**差评分析（新增）**:

```markdown
### 差评根本原因分类
| 问题类别 | 差评占比 | 典型反馈 | KES 是否也有 |
|----------|:------:|----------|:-----------:|
| 漏水/安装问题 | 35% | "Leaked after 2 weeks" | ⚠️ KES 也需关注 |
| 材质不符预期 | 20% | "Thought it was metal, it's plastic" | KES 优势 |
| 客服响应慢 | 15% | "No response to my email" | 需加强 |
| 发货延迟 | 10% | "Took 3 weeks to arrive" | 物流监控 |
| 其他 | 20% | — | — |
```

---

### 2.7 Layer 5：内容策略分析

**目标**: 理解内容生产、分发、效果的全貌。

| 分析项 | 说明 | 采集方法 |
|--------|------|----------|
| **内容类型矩阵** | Blog / YouTube / Podcast / Social / Email / Tools | 全站内容审计 |
| **内容主题分布** | 教育% / 娱乐% / 产品% / UGC% / 品牌% | 抽样分类 |
| **内容质量深度** | 字数 / 原创数据 / 引用 / 多媒体元素 | 抽样评分 |
| **SEO 内容策略** | 针对哪些关键词？集群策略？ | SEMrush 内容差距分析 |
| **内容发布频率** | 各类内容的更新节奏 | 历史发布记录统计 |
| **爆款内容分析** | 哪些内容表现最好？为什么？ | BuzzSumo + 手动 |
| **内容再利用** | Blog → Video → Social 的复用链条 | 追踪同一主题的多格式 |
| **UGC 内容策略** | 用户内容如何被品牌使用？ | 品牌社交账号分析 |
| **内容-产品对齐** | 每篇内容是否指向相关产品？ | 内链策略分析 |
| **邮件内容序列** | 注册后收到什么？购买后收到什么？ | 注册观察 |

**内容审计增强模板**:

```markdown
### 内容效果排名（Top 10）
| 排名 | 标题/类型 | 形式 | 估计流量 | 分享数 | 转化暗示 | KES 可做吗？ |
|:----:|-----------|------|:------:|:-----:|:--------:|:----------:|
| 1 | "Installing X in 60s" | Video | 120K | 2.1K | 🔗 产品页 | ✅ |
| 2 | "X vs Y Comparison" | Blog | 45K | 890 | 🔗 ✅ | ✅ |
| ... | ... | ... | ... | ... | ... | ... |

### 内容日历模式
- 周一: Blog 发布（教育向）
- 周三: YouTube（产品向）
- 周五: Email Newsletter（促销 + 使用技巧）
- 每日: Pinterest 2-3 Pins
- 周末: UGC 转发
```

---

### 2.8 Layer 6：社区运营分析

**目标**: 理解社区策略、互动质量和品牌人设。

| 平台 | 分析重点 | 采集方法 |
|------|----------|----------|
| **Reddit** | 品牌账号活跃度 / 自然提及数 / 讨论情绪 | RedditSearch.io / GummySearch / 手动搜索 |
| **Quora** | 问答覆盖系统性 / 回答质量 | site:quora.com "brand" |
| **Facebook Group** | 是否有官方社群 / 成员数 / 活跃度 | 加入观察 |
| **Discord / Slack** | 核心粉丝社群深度 | 邀请链接搜索 |
| **TikTok** | #标签视频数 / 观看量 / 内容类型 | 手动搜索 |
| **Instagram** | 粉丝增长率 / 互动率 / Stories 使用 | SocialBlade |
| **YouTube 评论区** | 官方是否回复 / 回复质量 | 手动抽样 |
| **Amazon Q&A + 评价** | 品牌回复率 / 回复质量 | 差评回复分析 |
| **Trustpilot / SiteJabber** | 是否有独立评价页面 / 评分 | 直接浏览 |
| **客服体验** | 响应速度 / 解决质量 / 渠道多样性 | 神秘顾客测试 |

**社群健康度量化指标**:

```markdown
### 社区健康度评分
| 指标 | 数据 | 健康/不健康 |
|------|------|:-----------:|
| Reddit 自然提及（月均） | 12 条 | 🟢 |
| 品牌 vs 用户发帖比 | 1:20 | 🟢 |
| 差评回复率 | 60% | 🟡 |
| 差评回复质量（非模板） | 高 | 🟢 |
| 用户自发推荐率 | 30% | 🟢 |
| 社区 toxic 内容占比 | <5% | 🟢 |
```

---

### 2.9 Layer 7：流量结构分析

**目标**: 理解流量来源分布和增长趋势。

| 分析项 | 工具 | 采集内容 |
|--------|------|----------|
| **流量来源分布** | SimilarWeb / SEMrush | 搜索/直接/社交/付费/引荐/展示 占比 |
| **有机关键词排名** | SEMrush / Ahrefs | Top 50 关键词/月搜索量/排名位置 |
| **品牌词 vs 品类词** | SEMrush | 品牌词占比越高 = 品牌力越强 |
| **付费广告关键词** | SpyFu / SEMrush | PPC 关键词/预算估算/落地页 |
| **社交媒体流量贡献** | SimilarWeb | 每个社交平台的流量占比 |
| **引荐域名质量** | Ahrefs / Majestic | Top 引荐来源/DR/是否高权威 |
| **流量趋势** | SimilarWeb / SEMrush | 6-12 个月流量曲线 |
| **季节性模式** | Google Trends | 品类 + 品牌搜索量季节波动 |
| **移动 vs 桌面** | SimilarWeb | 移动端占比 — 反映用户场景 |
| **跳出率 / 停留时间** | SimilarWeb | 内容质量和匹配度指标 |
| **Display Ads 存在** | SimilarWeb / 手动浏览 | 是否投展示广告/在哪些网站 |

**流量健康度诊断**:

```markdown
### 流量来源健康度

| 指标 | 当前值 | 健康基准 | 诊断 |
|------|:-----:|:--------:|------|
| 品牌词 / 品类词比 | 0.6 | >0.5 | 🟢 品牌力尚可 |
| 有机搜索占比 | 42% | >40% | 🟢 健康 |
| 直接访问占比 | 28% | >25% | 🟢 品牌认知度好 |
| 付费搜索占比 | 8% | <20% | 🟢 不过度依赖 |
| 社交媒体占比 | 18% | >10% | 🟢 社区活跃 |
| 移动端占比 | 65% | >50% | 🟢 符合行业趋势 |
| 跳出率 | 45% | <50% | 🟢 着陆页匹配度好 |
```

---

### 2.10 Layer 8：转化漏斗分析

**目标**: 完整走一遍用户路径，找到所有转化优化点。

| 漏斗阶段 | 分析项 | 工具 | 关键问题 |
|----------|--------|------|----------|
| **广告 → 着陆** | 广告文案和着陆页是否匹配？ | 手动点击测试 | 信息一致性 |
| **着陆页第一屏** | Hero 区域是否有清晰的 CTA？ | 5 秒测试 | 是否能快速理解？ |
| **浏览 → 加购** | 产品页说服力如何？ | 手动评分 | 信任信号是否足够？ |
| **加购 → 结账** | 是否有 upsell/cross-sell？ | 手动测试 | 是否过度推送？ |
| **结账流程** | 步骤数/必填字段/支付方式 | 手动测试 | 结账摩擦点多吗？ |
| **放弃购物车** | 是否有挽回机制？ | 加购后不买看邮件 | 挽回策略是否及时？ |
| **支付成功** | 确认页有什么？ | 购买测试 | 是否有下一步引导？ |
| **售后邮件** | 购买后邮件序列 | 真实购买或注册 | 序列完整度/时机 |
| **包裹/开箱** | 包装质量/开箱体验/附赠品 | 购买测试 | 是否有惊喜感？ |

**转化优化检查清单**:

```markdown
### 转化优化清单 — 每项 1 分
□ 首页 Hero 区域 3 秒内理解价值主张
□ 产品页有高清产品图 + 细节图 + 尺寸图
□ 产品页有视频（安装/使用/对比）
□ 产品页有信任标志（认证/保修/退款）
□ 产品页有社会证明（评价/UGC/媒体标志）
□ 加购按钮显眼 + 移动端固定
□ 结账 ≤ 3 步
□ 支持访客结账（不强制注册）
□ 支付选项 ≥ 3 种（卡/PayPal/BNPL）
□ 有购物车挽回（邮件/弹窗）
□ 售后邮件序列 ≥ 3 封
□ 免运费门槛在产品页可见

总分: __ / 12
```

**购买测试 SOP**:

```
神秘顾客测试步骤:
1. 用新邮箱注册账号
2. 浏览 → 加购 → 结账（但不付款，或实际购买）
3. 记录每一步的体验:
   - 收集所有触发弹窗（截图）
   - 记录所有邮件（时间戳 + 标题 + 内容摘要）
   - 记录所有短信（如提供手机号）
   - 记录售后包裹内容（如有实际购买）
4. 完成测试后取消订单或退货
```

---

### 2.11 Layer 9：复购/留存分析

**目标**: 理解用户 LTV 最大化的策略。

| 分析项 | 说明 | 数据来源 |
|--------|------|----------|
| **订阅 / 自动补货** | 耗材订阅折扣？默认开启？ | 产品页 + 结账页 |
| **忠诚度 / 积分计划** | 积分获取方式？兑换价值？ | 注册后探索 |
| **推荐计划 Referral** | 推荐奖励（双方）？分享便捷度？ | 用户面板 |
| **VIP / 会员体系** | 付费会员？权益是什么？ | 注册后探索 |
| **产品迭代节奏** | 新版本 V2/V3 发布时间 | 产品发布历史 |
| **跨品类销售** | 是否推荐互补品类？ | 购买后推荐 |
| **季节性回购** | 是否有节日限定款？ | 产品发布日历 |
| **流失预警** | 多久不买会触发挽留？ | 邮件观察 |

**复购策略评分**:

```markdown
### 复购机制完整度
| 机制 | 是否存在 | 质量 |
|------|:------:|:----:|
| 订阅省钱 | ✅ | ⭐⭐⭐⭐ |
| 忠诚度积分 | ❌ | — |
| Referral | ✅ | ⭐⭐⭐ |
| VIP 会员 | ❌ | — |
| 耗材提醒邮件 | ✅ | ⭐⭐⭐⭐⭐ |
| 产品升级 V2 | ❌ | — |
| 跨品类推荐 | ✅ | ⭐⭐ |
```

---

### 2.12 ✨ Layer 10：竞争格局分析（新增）

**目标**: 画出完整竞争版图，不止是直接竞品。

| 分析维度 | 问题 | 方法 |
|----------|------|------|
| **直接竞品** | 谁在卖几乎一样的东西？ | 产品对比表 |
| **间接竞品** | 谁在解决同一个问题但方式不同？ | 替代方案分析 |
| **品类替代品** | 有没有完全不同的解决方案？ | 从用户视角发散思考 |
| **新进入者** | 最近 12 个月出现的新品牌？ | Google Trends + 行业新闻 |
| **平台玩家** | Amazon Basics/Walmart 自有品牌？ | 平台搜索 |
| **各品牌市场份额估算** | 谁的 Amazon BSR 最高？评论最多？ | Jungle Scout / 手动统计 |
| **价格-质量定位图** | 每个品牌在价格/质量矩阵的哪个位置？ | 2x2 矩阵图 |
| **差异化对比** | 每个竞品的核心差异点是什么？ | 差异总结表 |

**竞争格局画布模板**:

```markdown
### 竞争格局 2x2 矩阵（价格 vs 质量感知）

          高价格
            |
    Moen    |    Kohler
    Delta   |
  ——————————+—————————— 质量感知
            |
  Amazon    |    KES ← 目标位置
  Basics    |
            |
          低价格
```

---

### 2.13 ✨ Layer 11：广告创意分析（新增）

**目标**: 理解他们的付费获客策略和创意方向。

| 分析维度 | 数据来源 | 采集内容 |
|----------|----------|----------|
| **Meta (Facebook/Instagram) Ads** | Meta Ad Library | 活跃广告数、创意类型（图/视频/轮播）、文案角度 |
| **TikTok Ads** | TikTok Creative Center / Ad Library | 热门广告、Spark Ads vs 普通广告 |
| **Google Ads** | 手动搜索 + SpyFu/SEMrush | 搜索广告文案、购物广告、展示广告 |
| **Pinterest Ads** | Pinterest 搜索 | 推广 Pin 的内容类型 |
| **广告投放频率** | 长期观察 | 是否全年投放还是季节性？ |
| **广告创意主题** | 广告库分析 | 痛点/功能/社交证明/UGC/促销 → 占比 |
| **Landing Page 专用页** | 点击广告查看 | 是否有专用着陆页？和官网首页有何不同？ |
| **Retargeting 策略** | 浏览后观察 | 是否在浏览后再看到广告？ |
| **Influencer/KOL 内容** | 品牌标签 + #ad #sponsored | KOL 类型/粉丝量/内容形式/互动率 |
| **Affiliate 计划** | 官网页脚 / ShareASale / Impact | 是否公开招募？佣金比例？ |

**广告创意审计表**:

```markdown
### Meta Ad Library 分析
| 广告 ID | 平台 | 创意类型 | 角度 | 投放时长 | 推测效果 |
|---------|------|----------|------|:------:|:------:|
| #12345 | IG | 视频 30s | 痛点 — "房东不让改管道" | 6个月+ | ⭐⭐⭐⭐⭐ |
| #12346 | FB | 轮播图 | 功能对比 — "vs 传统过滤器" | 3个月 | ⭐⭐⭐⭐ |
| #12347 | IG | UGC 转发 | 社交证明 — 用户安装视频 | 2个月 | ⭐⭐⭐ |

### 广告创意方向占比
- 痛点教育: 40%
- 功能对比: 25%
- UGC/社交证明: 20%
- 促销/折扣: 15%
```

---

### 2.14 ✨ Layer 12：供应链与制造分析（新增）

**目标**: 理解产品成本结构和供应链策略（KES 最了解的部分）。

| 分析维度 | 问题 | 数据来源 |
|----------|------|----------|
| **制造模式** | 自有工厂 vs OEM/ODM？在中国还是海外？ | 产品标签/包装/官网关于 |
| **产地披露** | 是否公开制造国家？ | 产品页/包装 |
| **材料来源** | 原材料哪里来？是否有认证？ | 产品描述/认证文档 |
| **成本结构估算** | 基于同类产品估算 BOM + 制造成本 | KES 自身制造经验 |
| **物流模式** | 从哪发货？仓储分布？配送时效？ | 购买测试 + 运费政策 |
| **库存管理** | 是否有缺货？SKU 管理效率？ | 长期观察 |
| **供应商关系** | DTC 品牌背后是否有共同代工厂？ | 行业人脉 + 进口数据 |
| **质量认证** | 通过了哪些认证？（KES 对比优势） | 产品页 + 认证查询 |
| **包装策略** | 包装是否可持续？是否有开箱体验设计？ | 购买测试 + 开箱视频 |

**KES 专属分析 — 成本对比估算**:

```markdown
### 同类产品成本估算
| 产品 | 零售价 | 估算 BOM | 估算制造成本 | 估算毛利 | KES 类似产品成本 |
|------|:-----:|:------:|:----------:|:------:|:--------------:|
| 竞品龙头 A | $89 | $22 | $28 | 68% | KES: $19 |
| 竞品龙头 B | $59 | $12 | $17 | 71% | KES: $11 |
```

---

### 2.15 ✨ Layer 13：技术栈分析（新增）

**目标**: 识别他们用了什么技术工具，评估技术成熟度。

| 技术类别 | 分析工具 | 识别方法 |
|----------|----------|----------|
| **建站平台** | BuiltWith / Wappalyzer | Shopify / WooCommerce / Magento / BigCommerce？ |
| **主题/模板** | 页面源码 + Wappalyzer | 用的什么主题？自定义程度？ |
| **支付网关** | 结账页 | Stripe / PayPal / Shopify Payments / BNPL？ |
| **邮件营销** | 邮件 Header 分析 | Klaviyo / Mailchimp / Omnisend？ |
| **评价系统** | 产品页 | Yotpo / Judge.me / Loox / Stamped？ |
| **客服工具** | 右下角聊天窗口 | Zendesk / Gorgias / Tidio / Intercom？ |
| **分析工具** | 页面源码 | GA4 / Hotjar / Mixpanel / Triple Whale？ |
| **A/B Testing** | 页面源码 | Google Optimize / VWO / Optimizely？ |
| **Subscription 管理** | 结账页 + 用户面板 | Recharge / Bold / OrderGroove？ |
| **Loyalty 系统** | 用户面板 | Smile.io / Yotpo Loyalty / LoyaltyLion？ |
| **CDN/托管** | BuiltWith | Shopify 自带 / Cloudflare / Fastly？ |
| **页面速度** | PageSpeed Insights / GTmetrix | 性能评分 + 优化建议 |

**技术栈输出模板**:

```markdown
### 技术栈一览
| 类别 | 工具 | 费用估算（月） | KES 能用吗？ |
|------|------|:----------:|:----------:|
| 建站 | Shopify Plus | $2,000 | KES 用 WooCommerce ✅ |
| 邮件 | Klaviyo | $500-1,500 | 可考虑 |
| 评价 | Yotpo | $300-1,000 | 可用免费替代 |
| 客服 | Gorgias | $300 | 可考虑 |
| 分析 | Triple Whale | $300 | ROI 待评估 |
```

---

### 2.16 ✨ Layer 14：团队与资本分析（新增）

**目标**: 了解团队背景和资金实力，判断品牌成长空间。

| 分析维度 | 数据来源 | 关键问题 |
|----------|----------|----------|
| **创始人背景** | About 页面 / LinkedIn / 采访 | 是否有行业经验？连续创业者？ |
| **团队规模** | LinkedIn 员工数 / Glassdoor | 大团队 vs 小而美？ |
| **关键招聘** | LinkedIn Jobs / 官网 Careers | 在招什么人？反映什么战略？ |
| **融资历史** | Crunchbase / PitchBook / TechCrunch | 拿了多少钱？哪一轮？ |
| **投资方** | 同上 | 战略投资 vs 纯财务？ |
| **收购/合并** | 行业新闻 | 是否被收购？是否收购了其他品牌？ |
| **品牌矩阵** | 官网页脚 / 关于 | 母公司旗下有多少品牌？ |
| **营收估算** | SimilarWeb + Amazon + 行业推估 | 年营收范围（$1M-$10M-$50M-$100M+） |

**营收估算模型**:

```markdown
### 年营收估算（电商部分）
1. SimilarWeb 月访问: XXX K
2. 假设转化率: 2-3%（DTC 行业平均）
3. 月订单 = 月访问 × 转化率
4. AOV 估算: $XX（从产品价格推断）
5. 月营收（DTC）= 月订单 × AOV
6. Amazon 营收: 评论数 × 品类评论/销量比
7. 年营收 = (DTC 月营收 + Amazon 月营收) × 12

⚠️ 此为估值，误差范围 ±40%
```

---

### 2.17 ✨ Layer 15：护城河分析（新增）

**目标**: 判断品牌的竞争优势是否可持续。

| 护城河类型 | 是否有 | 强度 | 说明 |
|------------|:------:|:----:|------|
| **品牌护城河** | | | 品牌词搜索量是否持续增长？ |
| **网络效应** | | | 用户越多产品越好？（社区/数据） |
| **规模经济** | | | 量大是否显著降本？ |
| **转换成本** | | | 用户换品牌成本多高？（生态系统锁定） |
| **技术/专利壁垒** | | | 是否有专利/专有技术？ |
| **监管许可** | | | 是否有准入门槛？（医疗器械/食品） |
| **独家渠道** | | | 是否有独家分销/合作？ |
| **数据资产** | | | 是否有不可复制的用户数据？ |
| **团队/文化** | | | 团队是否是护城河？ |

**护城河评分卡**:

```markdown
### 护城河强度

| 护城河类型 | FilterBaby | KES |
|------------|:---------:|:---:|
| 品牌 | ⭐⭐ | ⭐⭐ |
| 网络效应 | ⭐ | ⭐ |
| 规模经济 | ⭐⭐ | ⭐⭐⭐ |
| 转换成本 | ⭐⭐⭐ (耗材锁定) | ⭐ |
| 技术专利 | ⭐ | ⭐ |
| **总分** | **9/25** | **8/25** |

结论: FilterBaby 的护城河来自耗材锁定，KES 的护城河来自制造规模
```

---

### 2.18 ✨ Layer 16：用户画像与真实反馈（新增）

**目标**: 真正理解用户是谁、他们怎么说。

| 数据来源 | 采集内容 | 方法 |
|----------|----------|------|
| **Amazon 评价** | 用户画像推断（语气/场景/关注点） | 抽样 100+ 评价分类 |
| **Reddit 讨论** | 自然对话中的用户语言和痛点 | 搜索品牌名 → 提取用户原话 |
| **Trustpilot** | 独立平台的评价偏向 | 浏览分析 |
| **社交媒体评论** | 品牌帖子下的用户评论 | 抽样分析 |
| **YouTube 评论** | 视频下的真实反馈 | 抽样分析 |
| **客服对话公开** | 如有公开 FAQ/论坛 | 分析高频问题 |
| **用户生成内容 UGC** | #标签 内容分析 | 分类 UGC 类型和情绪 |

**用户画像推断模板**:

```markdown
### 推断用户画像
| Persona | 特征 | 占比估计 | 需求优先级 |
|---------|------|:------:|----------|
| "租房达人 Alex" | 25-35岁/城市/租公寓/关注健康 | 45% | 安装简单 > 价格 > 效果 |
| "宝妈 Megan" | 30-40岁/郊区/有小孩/安全第一 | 35% | 安全 > 效果 > 品牌 |
| "DIY 爱好者 John" | 25-45岁/房主/懂技术/性价比 | 20% | 性价比 > 技术 > 效果 |

### 用户原话摘录
- "I was skeptical but it actually works"（需要社交证明）
- "Landlord won't let me change pipes"（租房痛点）
- "A bit pricey but worth it for peace of mind"（价格敏感但接受）
```

---

## 三、数据收集方法（完整数据源 SOP）

### 3.0 已装 Skill / 工具实测状态（2026-06-14）

> ⚠️ 以下为实际测试结果，非理论列表。每个工具标注了「能否在 WorkBuddy 内直接调用」。

#### A. 已装 Skill — 实测结果

| Skill | 版本 | 状态 | 调用方式 | 覆盖层 | 备注 |
|-------|------|:----:|----------|--------|------|
| **web-content-fetcher** | — | ✅ 可用 | `fetch.py "<url>" [chars] [--stealth]` | L0-L16 全层 | Scrapling fast 模式为主，自动降级 stealth；Jina Reader 备用 |
| **last30days** | v3.3.2 | ✅ 已配置 | `python3 last30days.py "<query>"` | L0, L6, L11, L16 | Reddit keyless ✅；X/Twitter ✅（`FROM_BROWSER=auto` cookie 扫描）；YouTube ✅（yt-dlp 已安装）；TikTok/IG ✅（`SCRAPECREATORS_API_KEY` 已配置） |
| **openclaw-assets-migrator** | v1.0 | N/A | 不涉及研究功能 | — | 迁移工具，不用于品牌研究 |

#### B. WorkBuddy 内置工具 — 可用性

| 工具 | 状态 | 覆盖层 | 用法 |
|------|:----:|--------|------|
| **WebSearch** | ✅ | L0, L1, L4, L7, L10, L11, L14 | 关键词搜索、新闻搜索、趋势搜索 |
| **WebFetch** | ✅ | 全层 | 抓取 URL 内容转 Markdown；200 req/day（Jina） |
| **Bash + curl** | ⚠️ | 部分 | 受沙箱限制，部分域名被拦截 |
| **Grep / Glob** | ✅ | 内部 | 在本地 wiki 中搜索已有研究资料 |

#### C. 外部免费 API — 实测结果

| 工具/API | 状态 | 测试结果 | 替代方案 |
|----------|:----:|----------|----------|
| **Reddit .json API** | ❌ 沙箱 403 | `reddit.com/*.json` 从沙箱被 Block | 用 last30days keyless 或 WebSearch `site:reddit.com` |
| **Arctic Shift API (Vercel)** | ❌ 404 | 部署已下线 | 用 photon-reddit.com Web UI 手动搜索 |
| **Arctic Shift (photon-reddit)** | ⚠️ 仅 Web UI | `arctic-shift.photon-reddit.com/search` 可手动访问 | 无法程序化调用 |
| **Pullpush API** | ✅ 可用（历史数据） | `api.pullpush.io` 可用，数据截至 2025-05 | Reddit 历史查询 ✅ 已验证 || **BuiltWith** | ❌ Captcha | JS 渲染 + 验证码，headless 无法绕过 | 手动浏览器访问，或用 Wappalyzer 扩展 |
| **SimilarWeb** | ❌ 反爬 | 无法通过 WebFetch 获取数据 | 手动浏览器访问免费版（5 次/月） |
| **Google Trends** | ✅ WebFetch | 可通过 WebFetch 抓取趋势页面 | 配合 WebSearch 查询 |
| **Meta Ad Library** | ✅ WebFetch | 可通过 WebFetch 抓取广告信息 | 需要手动浏览查看创意图片 |
| **Keepa/CamelCamelCamel** | ✅ WebFetch | 可抓取 Amazon 价格历史 | |
| **PageSpeed Insights** | ✅ WebFetch | `pagespeed.web.dev` 可抓取 | |
| **Google Patents** | ✅ WebFetch | 专利搜索可抓取 | |

#### D. 待安装免费工具

| 工具 | 安装命令 | 作用 | 优先级 |
|------|----------|------|:------:|
| **yt-dlp** | ✅ 已安装（`~/.local/bin/yt-dlp`）| YouTube 视频字幕提取 → 启用 last30days YouTube 源 | 🔴 P0 已完成 |
| **Wappalyzer CLI** | ⚠️ 未安装 | 技术栈检测（替代 BuiltWith 自动化）| 🟡 P1 |

---

### 3.1 免费工具 — 完整清单（v2.1 实测标注版）

| 工具 | 用途 | 适用层 | 调用方式 | 限制 |
|------|------|--------|----------|------|
| **WebSearch（内置）** | 关键词/新闻/趋势搜索 | L0, L1, L7, L10 | 直接调用 | — |
| **WebFetch（内置）** | URL 内容转 Markdown | 全层 | 直接调用 | 200 req/day |
| **web-content-fetcher** | 网页正文提取（含反爬） | 全层 | `fetch.py "<url>" [chars] [--stealth]` | fast→stealth 自动降级 |
| **last30days** | Reddit/HN/GitHub 社媒研究 | L0, L6, L11, L16 | `last30days.py "<query>"` | 见 3.0 限制 |
| **SimilarWeb** | 流量估算、来源分析 | L7, L8 | 手动浏览器（5 次/月免费） | 免费版功能有限 |
| **Google Trends** | 品牌/品类搜索趋势 | L0, L1, L7 | WebFetch 或 WebSearch | 无绝对数值 |
| **Wayback Machine** | 历史页面快照 | L1, L3, L5 | WebFetch | 存档不连续 |
| **Google Alerts** | 品牌提及实时监控 | L0, L6 | 在 Google Alerts 网站设置 | 延迟 1-2 天 |
| **Meta Ad Library** | FB/IG 活跃广告 | L11 | WebFetch 或手动浏览 | 不显示效果数据 |
| **TikTok Creative Center** | TikTok 热门广告 | L11 | WebFetch | 有限的国家覆盖 |
| **Wappalyzer 扩展** | 网站技术栈检测 | L13 | 浏览器扩展或 CLI | 不显示后台工具 |
| **PageSpeed Insights** | 网站性能评分 | L13 | WebFetch | Google 数据 |
| **Arctic Shift Web UI** | Reddit 历史搜索 | L0, L6, L16 | 手动浏览 photon-reddit.com | 无 API |
| **Keepa（免费版）** | Amazon 价格历史 | L3 | WebFetch | 功能有限 |
| **CamelCamelCamel** | Amazon 价格追踪 | L3 | WebFetch | 仅 Amazon |
| **SocialBlade** | YouTube/IG/Twitter 数据 | L5, L6 | WebFetch | 仅公开数据 |
| **Google Patents** | 专利搜索 | L15 | WebFetch | 需专业解读 |
| **Crunchbase（免费）** | 融资/团队基本数据 | L14 | WebFetch | 不完整 |
| **Google News** | 媒体提及 | L0, L4 | WebSearch topic:news | 英文为主 |
| **ImportYeti** | 进口数据/供应商 | L12 | WebFetch | 免费部分数据 |
| **ChatGPT/Perplexity** | GEO 可见性测试 | L0 | 手动提示词 | 需系统性提示词 |
| **Pullpush API** | Reddit 历史数据（截至 2025-05） | L6, L16 | `api.pullpush.io` | 数据非最新 |

### 3.2 付费工具 — 2026 采购建议（按 KES 需求排序）

> 💡 采购原则：每个工具先用免费版/试用验证价值 → 按月订阅而非年付 → 用够了再升级

#### 采购优先级矩阵

| 优先级 | 工具 | 月费（年付折算） | 核心价值 | 为什么值得 | KES ROI 预估 |
|:------:|------|:---------------:|----------|-----------|:----------:|
| 🔴 **P0** | **SEMrush Pro** | $117/月 | SEO + PPC + AI 可见性全数据 | DTC 品牌研究唯一必需品：关键词/流量/广告/竞品/AI 引用，一个工具覆盖 L0/L7/L10/L11 | ⭐⭐⭐⭐⭐ |
| 🔴 **P0** | **Keepa Premium** | €19/月 | Amazon 完整价格+BSR+销量历史 | KES 核心渠道 Amazon 的数据基础设施，价格追踪/库存监控/销量估算 | ⭐⭐⭐⭐⭐ |
| 🟡 **P1** | **Jungle Scout Starter** | $29/月 | Amazon 选品/BSR/关键词/供应商 | 精准销售估算（84-89% 准确率）+ 供应商数据库，KES 多市场适用 | ⭐⭐⭐⭐ |
| 🟡 **P1** | **SpyFu** | $39/月 | 竞品 PPC 关键词+广告历史 | 低成本 PPC 情报，如已买 SEMrush 可跳过 | ⭐⭐⭐ |
| 🟢 **P2** | **Ahrefs Lite** | $108/月 | 反向链接+内容差距分析 | 反向链接数据最权威，但 SEMrush 已覆盖 80% 功能；仅在专注 Link Building 时购买 | ⭐⭐⭐ |
| 🟢 **P2** | **Brand24** | $79/月 | 社交媒体监听/品牌提及 | 自动化品牌提及追踪，但 WebSearch + Google Alerts 免费替代 60% | ⭐⭐ |
| 🔵 **P3** | **BuzzSumo** | $199/月 | 内容效果分析 | 价格偏高，可用 SEMrush 内容模块部分替代 | ⭐⭐ |
| 🔵 **P3** | **Triple Whale** | $300/月 | DTC 数据归因 | 仅在 DTC 营收 >$100K/月 时有意义 | ⭐ |

#### 关键对比：SEMrush vs Ahrefs（2026）

| 维度 | SEMrush Pro ($117/月) | Ahrefs Lite ($108/月) |
|------|:--------------------:|:--------------------:|
| **DTC 适用性** | ✅ **完胜** — 含 PPC 广告情报 | ❌ 不含 PPC |
| **AI 品牌可见性** | ✅ 追踪 5 个 AI 平台 | ⚠️ Brand Radar 准确率差（低报 35-40x） |
| **PPC 竞品情报** | ✅ 完整 | ❌ 无 |
| **内容营销工具** | ✅ Topic Research + Writing Assistant | ❌ 无写作工作流 |
| **反向链接新鲜度** | ⚠️ 每周更新 | ✅ 15-30 分钟更新 |
| **YouTube SEO** | ⚠️ 数据较薄 | ✅ 有用 |
| **免费试用** | ✅ 14 天 | ❌ 无 |

**结论**: KES 应选 SEMrush Pro。Ahrefs 仅在专注 Link Building 时补充购买。

#### 关键对比：Jungle Scout vs Helium 10（2026）

| 维度 | Jungle Scout Starter ($29/月) | Helium 10 Platinum ($99/月) |
|------|:---------------------------:|:--------------------------:|
| **销售估算准确率** | ✅ 84-89% | ⚠️ 74-79% |
| **供应商数据库** | ✅ 含海关数据 | ❌ 无 |
| **关键词深度** | ⚠️ 够用 | ✅ 多 30-40% 关键词 |
| **多市场** | ❌ 仅 Amazon | ✅ Amazon + Walmart + TikTok Shop |
| **免费版** | ❌ | ✅ 2 次 Cerebro 搜索/天 |
| **KES 适配** | ✅ 性价比最高 | KES 暂不需要 Walmart/TikTok Shop |

**结论**: KES 先用 Jungle Scout Starter。Helium 10 免费版可用于零成本关键词研究。

#### 建议采购组合（年度成本）

| 方案 | 工具组合 | 月费 | 年费 | 适合 |
|------|----------|:----:|:----:|------|
| **轻量启动** | SEMrush Pro + Keepa | $136 | $1,632 | 初期深度研究阶段 |
| **标准配置** | SEMrush Pro + Keepa + Jungle Scout | $165 | $1,980 | 持续竞品研究 + Amazon 运营 |
| **完整配置** | SEMrush Pro + Keepa + Jungle Scout + Ahrefs | $273 | $3,276 | 需要深度 Link Building |
| **最小可行** | SEMrush Pro 单月试用 + Keepa | $136 | — | 先用一个月验证价值 |

### 3.3 无需工具的采集方法

| 方法 | 适用层 | 耗时 | 输出质量 |
|------|--------|:----:|:--------:|
| **神秘顾客购买测试** | L8, L12, L16 | 中 | ⭐⭐⭐⭐⭐ |
| **注册邮件列表观察** | L5, L8, L9 | 低 | ⭐⭐⭐⭐ |
| **假装客户咨询客服** | L6, L16 | 低 | ⭐⭐⭐⭐ |
| **加入官方社群观察** | L6, L16 | 低（持续）| ⭐⭐⭐⭐ |
| **参与行业展会/论坛** | L12, L14 | 高 | ⭐⭐⭐⭐⭐ |
| **逆向工程/产品拆解** | L2, L12 | 高 | ⭐⭐⭐⭐⭐ |
| **用户访谈（竞品用户）** | L16 | 高 | ⭐⭐⭐⭐⭐ |

### 3.4 AI 辅助研究工作流 — WorkBuddy 内完整 SOP

> 🤖 以下 SOP 假设你在 WorkBuddy 中操作，标注了每步用的工具和具体命令。

#### L1 快速扫描 — 1 小时 AI 工作流

```
Phase 1: 官网深度抓取（15 分钟）
──────────────────────────────────
1. web-content-fetcher → 抓取首页
   fetch.py "https://[brand].com" 15000

2. web-content-fetcher → 抓取 About 页
   fetch.py "https://[brand].com/pages/about" 10000

3. web-content-fetcher → 抓取产品列表页
   fetch.py "https://[brand].com/collections/all" 15000

4. WebSearch → 搜索 "[brand] review" 了解舆论
   query: "[brand] review reddit"

Phase 2: 社区与社媒（15 分钟）
──────────────────────────────────
5. last30days → Reddit/HN 讨论研究
   last30days.py "[brand] [category]"

6. WebSearch → 搜索 Reddit 讨论
   query: "site:reddit.com [brand]"

7. WebFetch → Meta Ad Library 查广告
   fetch "https://facebook.com/ads/library/?active_status=all&ad_type=all&country=US&q=[brand]"

Phase 3: 搜索可见性与竞品（15 分钟）
──────────────────────────────────
8. WebSearch → 品类词搜索
   query: "best [category] 2026"

9. WebSearch → 竞品对比搜索
   query: "[brand] vs [competitor]"

10. WebFetch → Google Trends
    fetch "https://trends.google.com/trends/explore?q=[brand]&geo=US"

Phase 4: Amazon 数据（15 分钟）
──────────────────────────────────
11. web-content-fetcher → Amazon 产品页
    fetch.py "https://amazon.com/s?k=[brand]" 10000

12. WebFetch → Keepa 价格历史
    fetch "https://keepa.com/#!product/[ASIN]"

13. WebSearch → "[brand] Amazon rating review"
    query: "[brand] faucet Amazon review"
```

#### L2 标准研究 — 3 天 AI 工作流

```
Day 1: 数据采集
────────────────
- 运行 L1 快速扫描全部步骤
- web-content-fetcher 抓取每个产品页（Top 10 SKU）
- WebFetch 抓取 Trustpilot 页面
- last30days 深度搜索（品牌名 + 品类词 + 竞品名）
- WebFetch 抓取 SocialBlade 数据
- WebFetch 抓取 Crunchbase 数据
- 手动浏览 BuiltWith（浏览器）
- 手动浏览 SimilarWeb（浏览器）

Day 2: 深度分析
────────────────
- web-content-fetcher 抓取竞品官网（3-5 个）
- WebFetch 抓取 Meta Ad Library 全部广告
- WebSearch 搜索专利信息
- 抓取 Amazon Q&A + 差评分析
- WebSearch 搜索融资/团队信息
- 整理 E-E-A-T 评分卡
- 构建产品矩阵图

Day 3: 综合输出
────────────────
- 填写案例研究模板
- 计算财务估算
- 完成 SWOT 分析
- 提炼 KES 可借鉴点
- 撰写行动建议
- 更新 wiki/brand-studies/
```

#### 30 分钟竞品快速数据采集（更新版）

```markdown
## 30 分钟竞品快速数据采集 — WorkBuddy 版

### 前 10 分钟: 建站技术 + 流量
□ web-content-fetcher → 抓取官网首页
  fetch.py "https://[brand].com" 10000
□ 手动开浏览器 → BuiltWith 看 tech stack（沙箱限制）
□ 手动开浏览器 → SimilarWeb 截图月流量 + 来源分布
□ WebFetch → PageSpeed Insights
  fetch "https://pagespeed.web.dev/analysis?url=[brand].com"

### 中间 10 分钟: 搜索可见性 + 社区
□ WebSearch "best [category] 2026" → 标注品牌在搜索结果位置
□ WebSearch "[brand] review" → 谁在写评测？
□ WebSearch "[brand] vs" → 竞品对比页是谁的？
□ ChatGPT "推荐好的 [品类]" → 是否出现？怎么描述？
□ last30days → "[brand] [category]"
□ WebSearch "site:reddit.com [brand]" → Reddit 讨论前 5 条

### 最后 10 分钟: 广告 + Amazon
□ WebFetch → Meta Ad Library 搜索品牌名
□ WebFetch → TikTok Creative Center 搜索品牌名
□ WebSearch → "[brand] Amazon" → 看 BSR + 评论数 + 评分
□ WebFetch → Keepa 查 Amazon 价格历史（如有 ASIN）
```

---

## 四、案例研究模板（v2.0 增强版）

```markdown
# [品牌名] DTC 案例研究

> **研究日期**: YYYY-MM-DD | **品类**: XXX | **研究深度**: L2/L3 | **验证状态**: unverified
> **数据来源**: 官网、Amazon、Reddit、SEMrush、Meta Ad Library、神秘顾客测试

---

## 一、品牌概览

| 项目 | 内容 |
|------|------|
| 品牌名 | |
| URL | |
| 成立时间 | |
| 总部位置 | |
| 创始人 | |
| 融资情况 | |
| 核心品类 | |
| SKU 数量 | |
| 价格段位 | $XX - $XX |
| 年营收估算 | $X - $XX M |
| 主要渠道 | DTC 官网 % / Amazon % / 零售 % |

## 二、16 层深度分析

### Layer 0: 发现路径
[按 2.2 模板]

### Layer 1: 品牌定位
[按 2.3 模板]

### Layer 2: 产品矩阵
[按 2.4 模板]

### Layer 3: 定价策略
[按 2.5 模板]

### Layer 4: 信任体系 + E-E-A-T 评分
[按 2.6 模板 + 评分卡]

### Layer 5: 内容策略
[按 2.7 模板]

### Layer 6: 社区运营
[按 2.8 模板]

### Layer 7: 流量结构
[按 2.9 模板]

### Layer 8: 转化漏斗 + 购买测试
[按 2.10 模板]

### Layer 9: 复购/留存
[按 2.11 模板]

### Layer 10: 竞争格局 ✨
[按 2.12 模板]

### Layer 11: 广告创意分析 ✨
[按 2.13 模板]

### Layer 12: 供应链与制造 ✨
[按 2.14 模板]

### Layer 13: 技术栈 ✨
[按 2.15 模板]

### Layer 14: 团队与资本 ✨
[按 2.16 模板]

### Layer 15: 护城河分析 ✨
[按 2.17 模板]

### Layer 16: 用户画像与真实反馈 ✨
[按 2.18 模板]

## 三、财务估算

### 营收估算（详见 5.1）
| 渠道 | 月访问 | 转化率 | AOV | 月营收（估）|
|------|:-----:|:-----:|:---:|:--------:|
| DTC 官网 | | 2% | | |
| Amazon | — | — | — | |
| **年营收合计** | | | | **$XX M** |

### 单位经济学估算（详见 5.2）
| 指标 | 估算 |
|------|------|
| 产品毛利率 | XX% |
| 平均 CAC | $XX |
| 平均 LTV | $XX |
| LTV/CAC | XX |

## 四、SWOT 分析

| 优势 Strengths | 劣势 Weaknesses |
|----------------|-----------------|
| | |

| 机会 Opportunities | 威胁 Threats |
|-------------------|--------------|
| | |

## 五、KES 可借鉴点

### 可直接复制的打法（成本 < $500）
1. 
2. 

### 需要适配的打法（成本 < $5,000）
1. 
2. 

### 需要投资的打法（成本 > $5,000）
1. 

### 必须避免的坑
1. 
2. 

## 六、具体行动建议

| # | 行动 | 优先级 | 预估成本 | 预期影响 | 时间线 |
|---|------|--------|----------|----------|--------|
| 1 | | P0 | | | 1 周 |
| 2 | | P1 | | | 1 月 |
| 3 | | P2 | | | 1 季 |

## 七、附件清单

□ 官网首页 + 产品页截图
□ Amazon 产品页截图
□ Meta Ad Library 广告截图
□ E-E-A-T 信号截图合集
□ 购买测试照片（如有）
□ SEMrush 关键词导出
□ SimilarWeb 流量数据截图
□ 竞品对比表 Excel

## 八、研究日志

| 日期 | 做了什么 | 发现 |
|------|----------|------|
| | | |

---
```

---

## 五、财务估算模型 ✨（新增）

### 5.1 营收估算模型

```
步骤:
1. SimilarWeb → 月访问量 (A)
2. 转化率假设:
   - DTC 新品牌: 1-1.5%
   - DTC 成熟品牌: 2-3%
   - Amazon: 10-15%（Amazon 流量转化高）
3. AOV 假设: 从产品价格推断（主推 SKU 价格 × 0.7-1.0）
4. Amazon 营收: Jungle Scout 月销估计 或 评论数 × 品类评论/销量比
5. 多渠道合计

公式:
  月营收(DTC) = 月访问 × 转化率 × AOV
  年营收 = [月营收(DTC) + 月营收(Amazon)] × 12

品类评论/销量参考比:
  - 家居五金: 1 评论 ≈ 50-80 销售
  - 过滤器/耗材: 1 评论 ≈ 30-50 销售
  - 日用消费品: 1 评论 ≈ 100-200 销售
```

### 5.2 CAC:LTV 估算模型

```
CAC 估算:
  - DTC 行业平均 CAC: $30-60（家居品类偏高）
  - 如果品牌大量投 Meta Ads + Google Ads:
    CAC ≈ (月广告支出 / 月新增客户数)
    经验: 月广告支出 ≈ 月营收 × 20-40%（成长期品牌）

LTV 估算:
  LTV = AOV × 复购次数
  - 一次性产品（浴室五金）: AOV × 1.0-1.2（部分跨品类回购）
  - 耗材产品（过滤器）: AOV × 3-8（订阅驱动）

健康度:
  LTV/CAC > 3 ✅
  LTV/CAC 2-3 🟡
  LTV/CAC < 2 ❌
```

### 5.3 盈利能力快速判断

| 指标 | 健康范围 | 警告信号 |
|------|----------|----------|
| 毛利率 | >60% | <40% — 不可持续 |
| 营销费用率 | 20-35% | >50% — 烧钱获客 |
| CAC | <$50 | >$100 — 品类太贵 |
| AOV | >$60 | <$30 — 履约难赚钱 |
| 复购率 | >20% | <10% — 没有留存 |

---

## 六、用户旅程地图 ✨（新增）

### 6.1 KES 用户旅程 vs 竞品用户旅程对照

```
阶段        竞品触点                    → KES 优化机会
─────────────────────────────────────────────────────
意识        品类词搜索/Reddit/PR        → SEO + GEO + 社区铺设
            社交媒体广告                → 信息流广告测试
            KOL 推荐                   → 微型 KOL 合作

考虑        官网首页 → 产品页            → 3 秒价值命题优化
            竞品对比博客                 → "Metal vs Plastic" 对比内容
            评价/UGC 内容               → 社交证明策略

决策        加购弹出折扣                 → 首单折扣策略
            信任标志（认证/保修）        → "5-Year Warranty" 醒目展示
            客服即时响应                 → 客服测速 + 优化

购买        2 步结账                    → 结账流程简化
            多种支付方式                → 增加 BNPL？

体验        开箱惊喜                    → 包装升级
            安装视频/指南               → "Install in 10 Min" 卡片

售后        感谢 + 安装提示邮件          → 邮件序列模板
            差评回复                    → 技术型回复模板
            复购提醒/推荐               → 跨品类推荐策略
```

---

## 七、验证与质量控制 SOP ✨（新增）

### 7.1 研究质量检查清单

完成一个品牌研究后，必须通过以下质量检查：

```markdown
## 研究质量自检

### 完整性检查
□ 所有 16 层信息均已收集（至少标记"未找到/不适用"）
□ 所有数据来源已标注
□ 所有估算已注明"估算"和误差范围
□ 截图/数据导出已保存

### 准确性检查
□ 关键数据至少有 2 个来源交叉验证
□ 流量数据标注 SimilarWeb 估算
□ 营收数据标注估算方法和误差范围
□ 价格信息已通过购买测试或 Keepa 验证

### 偏见检查
□ 没有仅看好评忽略差评
□ 差评分析覆盖率 >50%（至少分析 20 条差评）
□ 没有过度美化竞品
□ KES 可借鉴点有「可行性验证」标注

### 时效性检查
□ 核心数据来源日期不超过 3 个月
□ 价格数据是最新的（标注采集日期）
□ 广告数据是当前的（Meta Ad Library 实时）
```

### 7.2 数据交叉验证方法

| 数据类型 | 验证方法 |
|----------|----------|
| **流量** | SimilarWeb + SEMrush 趋势对比（不一致是正常的，看趋势） |
| **关键词** | SEMrush + Ahrefs + 手动 Google 搜索验证 |
| **定价** | 官网 + Amazon + Keepa 历史 + 手动购买 |
| **评价** | Amazon + Trustpilot + Reddit（三个来源看模式） |
| **营收** | SimilarWeb 推估 + Jungle Scout + 行业人脉验证 |
| **广告** | Meta Ad Library + 手动搜索品牌名前后的广告 |

---

## 八、竞品持续监控体系 ✨（新增）

### 8.1 监控指标面板

```markdown
# 竞品监控面板 — 每周更新

## 流量指标
| 品牌 | 月访问 | 周变化 | 移动% | 跳出率 |
|------|:-----:|:-----:|:----:|:-----:|
| FilterBaby | 450K | +2% | 65% | 45% |
| Waterdrop | 1.2M | +5% | 70% | 42% |
| [KES] | XXX | ±X% | XX% | XX% |

## Amazon 指标
| 品牌 | BSR | 评论数 | 评分 | 库存状态 |
|------|:---:|:-----:|:---:|:-------:|
| FilterBaby | #3 | 1,650 | 4.3 | ✅ |
| [KES 产品] | #XX | XXX | X.X | ✅/⚠️ |

## 内容指标
| 品牌 | 本周新内容 | 类型 | 表现 |
|------|-----------|------|------|
| FilterBaby | "New PFAS Study" | Blog | — |
| [KEE] | — | — | — |

## 定价变动
| 品牌 | 产品 | 原价 | 现价 | 变动原因 |
|------|------|:---:|:---:|----------|
| — | — | — | — | — |
```

### 8.2 监控工具组合

| 监控对象 | 工具 | 频率 | 自动化 |
|----------|------|:----:|:------:|
| 网站流量 | SimilarWeb | 每周 | 手动 |
| Amazon BSR/价格 | Keepa | 实时 | ✅ 自动 |
| 新内容发布 | Feedly / RSS | 每日 | ✅ 自动 |
| 广告变动 | Meta Ad Library | 每两周 | 手动 |
| 品牌提及 | Google Alerts | 实时 | ✅ 自动 |
| 社交媒体增长 | SocialBlade | 每周 | 手动 |
| 招聘变�� | LinkedIn Alerts | 实时 | ✅ 自动 |
| 融资/新闻 | Google Alerts | 实时 | ✅ 自动 |

### 8.3 监控触发报告

当以下事件发生时，触发「竞品警报」：

- 🚨 竞品月流量单月增长/下降 >20%
- 🚨 竞品 Amazon BSR 大幅跃升（突然进入 Top 10）
- 🚨 竞品发布重大新品/新品类
- 🚨 竞品获得大额融资或被收购
- 🚨 竞品大幅降价（>20%）
- 🚨 竞品负面舆论爆发（Reddit/Trustpilot 集中差评）
- 🚨 新进入者出现（新的品类词搜索结果）

---

## 九、研究效率与协作 ✨（新增）

### 9.1 研究效率技巧

| 技巧 | 节省时间 | 说明 |
|------|:------:|------|
| **Chrome 竞品书签夹** | 30% | 把竞品官网/Amazon/社交 集中一个书签夹，一键打开 |
| **看板工具（Notion/Airtable）** | 40% | 用数据库替代 Markdown 表格，可筛选/排序/对比 |
| **截图工具（CleanShot X）** | 50% | 快速标注+按品牌分类保存 |
| **模板化邮件注册** | 30% | 用固定 Gmail 别名 brand+filterbaby@gmail.com 追踪 |
| **批量 Wayback Machine** | 50% | 同时查多个品牌的历史页面 |
| **Google Sheets 竞品对比** | 40% | 把 5+ 竞品放在一个 Sheet 里横向对比 |

### 9.2 研究分工建议

如果是团队操作：

| 角色 | 负责层 | 输出 |
|------|--------|------|
| **市场研究员** | L0, L1, L7, L10 | 发现/定位/流量/竞争 |
| **产品经理** | L2, L3, L12, L15 | 产品/定价/供应链/护城河 |
| **内容/社区** | L4, L5, L6, L16 | 信任/内容/社区/用户 |
| **增长黑客** | L8, L9, L11, L13 | 转化/复购/广告/技术 |

---

## 十、KES 品类研究优先级

### 10.1 建议优先研究的品牌（按紧迫度）

| 优先级 | 品类 | 品牌 | 为什么 | 建议深度 |
|:------:|------|------|--------|:--------:|
| **P0** | 浴室五金 DTC | Moen 线上直销 | 行业标杆，转化策略参考 | L3 |
| **P0** | 租房五金 | Command (3M) | 定位最接近「租房友好」 | L2 |
| **P0** | DTC 家居 | Brooklinen | 内容营销黄金标准 | L3 |
| **P1** | 浴室五金 | Delta DTC | 直接竞品，定价参考 | L2 |
| **P1** | 过滤器 DTC | Waterdrop | 快速增长，耗材模式 | L2 |
| **P1** | 家居电商 | Build.com 自有品牌 | 品类宽度策略 | L2 |
| **P2** | DTC 家居 | Parachute | 品牌建设案例 | L1 |
| **P2** | 五金 | FaucetDirect | 垂直电商模式 | L1 |
| **P2** | 新兴 DTC | 寻找 2024-2025 新成立的浴室五金 DTC | 新打法观察 | L1 |

### 10.2 研究节奏建议

| 阶段 | 时间 | 目标 |
|------|------|------|
| **Sprint 0** | 第 1 周 | 完成 3 个 P0 品牌快速扫描（L1）→ 确定深度研究方向 |
| **Sprint 1** | 第 2-3 周 | 完成 1 个 P0 品牌 L3 完整研究 |
| **Sprint 2** | 第 4-5 周 | 完成 2 个 P1 品牌 L2 标准研究 |
| **Sprint 3+** | 持续 | 每个月新增 1-2 个品牌研究 + 周度监控 |

---

## 十一、从案例到行动：KES 适配矩阵

研究完品牌后，用这个矩阵评估 KES 是否可以借鉴：

| 维度 | 问题 | 评分（1-5） |
|------|------|:----------:|
| **品类适配性** | KES 品类和该品牌品类相似度？ | |
| **资源可行性** | KES 是否有能力复制这个打法？ | |
| **预期 Impact** | 复制后可能带来多少增收/增利？ | |
| **执行难度** | 需要多少时间和人力？ | |
| **风险可控性** | 复制失败或竞品反击的风险？ | |
| **时间窗口** | 现在是做这件事的时机吗？（1=太早/太晚，5=完美时机） | |
| **差异化程度** | 复制后 KES 的版本有多大差异？（1=完全一样，5=高度差异化） | |

**评分标准**:
- ≥ 28 → 立即执行（P0）
- 21-27 → 列入本季路线图（P1）
- 14-20 → 列入下季路线图（P2）
- < 14 → 暂不执行或降级为观察

---

## 十二、输出物管理

```
wiki/
  brand-studies/
    bathroom-hardware/
      moen-dtc-analysis.md
      delta-dtc-analysis.md
      faucetdirect-analysis.md
      brooklinen-dtc-analysis.md
    filters/
      filterbaby-dtc-case-study.md    ← 已完成 ✅
      waterdrop-dtc-analysis.md
    home-dtc/
      parachute-dtc-analysis.md
    
  protocols/
    dtc-tactics/
      dtc-eat-implementation-roadmap.md
      dtc-content-marketing-playbook.md
      dtc-community-engagement-sop.md
      dtc-conversion-optimization-checklist.md
      dtc-email-sequence-templates.md
      dtc-tactics-playbook.md           ← 从案例中提炼的执行打法

  dashboards/
    competitor-watch.md

  templates/
    dtc-brand-study-template.md        ← 本文挡第四部分的模板
    dtc-quick-scan-template.md         ← L1 快速扫描模板
```

---

## 十三、关联页面

| 页面 | 说明 |
|------|------|
| `wiki/brand-studies/filterbaby-dtc-case-study.md` | FilterBaby 完整案例（v1.0，待更新到 v2.0） |
| `wiki/syntheses/kes-dtc-eat-implementation-roadmap-2026-06.md` | KES DTC E-E-A-T 建设路径 |
| `wiki/syntheses/product-kb-vs-community-kb-comparison.md` | 产品 KB vs 社区 KB 对比 |
| `wiki/products/kes-product-knowledge-base/KNOWLEDGE-BASE-BUILD-GUIDE.md` | 知识库构建方法 |
| `wiki/topics/pinterest-playbook-for-kes.md` | Pinterest 渠道打法 |
| `wiki/topics/reddit-marketing.md` | Reddit 营销方法论 |
| `wiki/syntheses/kes-geo-implementation-plan-2026-06.md` | GEO 实施计划 |
| `wiki/syntheses/kes-content-marketing-integrated-plan.md` | 内容营销整合计划 |
| `~/.workbuddy/skills/web-content-fetcher/SKILL.md` | web-content-fetcher 技能配置 |
| `~/.workbuddy/skills/last30days/SKILL.md` | last30days 技能配置 |

---

## 十四、16 层→工具→命令速查表 ✨（v2.1 新增）

> 一张表查到每层该用什么工具、怎么调用。

| Layer | 分析维度 | 首选工具（WorkBuddy 内） | 备选工具（手动/付费） | 关键命令 |
|:-----:|----------|--------------------------|----------------------|----------|
| **L0** | 发现路径 | WebSearch + last30days + web-content-fetcher | SEMrush（付费） | `last30days.py "[brand] [category]"` ; WebSearch `"[category] review 2026"` |
| **L1** | 品牌定位 | web-content-fetcher + WebFetch | Google Trends（手动） | `fetch.py "https://[brand].com" 15000` ; WebFetch About 页 |
| **L2** | 产品矩阵 | web-content-fetcher + WebFetch Amazon | Jungle Scout（付费） | `fetch.py "https://[brand].com/collections/all" 15000` |
| **L3** | 定价策略 | WebFetch Keepa/CamelCamelCamel + web-content-fetcher | Keepa Premium（付费） | WebFetch `keepa.com/#!product/[ASIN]` |
| **L4** | 信任体系 E-E-A-T | WebSearch + web-content-fetcher | 手动验证认证编号 | WebSearch `"[brand] cUPC certification"` |
| **L5** | 内容策略 | WebFetch + WebSearch + web-content-fetcher | BuzzSumo（付费） | `fetch.py "https://[brand].com/blogs" 15000` |
| **L6** | 社区运营 | last30days + WebSearch + WebFetch | Brand24（付费） | `last30days.py "[brand]"` ; WebSearch `"site:reddit.com [brand]"` |
| **L7** | 流量结构 | WebSearch + WebFetch SimilarWeb | SEMrush（付费）+ SimilarWeb（手动） | 手动浏览 SimilarWeb ; WebSearch `"[brand] traffic similarweb"` |
| **L8** | 转化漏斗 | web-content-fetcher（模拟走一遍流程）| 神秘顾客测试 | `fetch.py "https://[brand].com/products/[sku]" 10000` |
| **L9** | 复购/留存 | web-content-fetcher + WebFetch | 邮件注册观察 | WebFetch 产品页订阅/会员部分 |
| **L10** | 竞争格局 | WebSearch + WebFetch | SEMrush（付费） | WebSearch `"best [category] 2026"` ; WebSearch `"[brand] vs [competitor]"` |
| **L11** | 广告创意 | WebFetch Meta Ad Library + TikTok Creative Center | SpyFu（付费）| WebFetch `facebook.com/ads/library/?q=[brand]` |
| **L12** | 供应链制造 | WebSearch + WebFetch ImportYeti | ImportYeti + 行业人脉 | WebSearch `"[brand] supplier manufacturer China"` |
| **L13** | 技术栈 | Wappalyzer（手动浏览器扩展） | BuiltWith（手动）| 手动浏览器访问 `builtwith.com/[brand].com` |
| **L14** | 团队资本 | WebSearch + WebFetch Crunchbase | Crunchbase Pro | WebSearch `"[brand] funding crunchbase"` ; WebFetch Crunchbase |
| **L15** | 护城河 | WebSearch + WebFetch Google Patents | SEMrush Brand Monitoring | WebSearch `"[brand] patent"` ; WebFetch `patents.google.com` |
| **L16** | 用户画像 | last30days + WebFetch Amazon 评价 + WebSearch Reddit | Jungle Scout（付费）| `last30days.py "[brand] [category] user review"` |

---

## 十五、last30days Skill 深度配置指南 ✨（v2.1 新增）

> last30days 是最核心的社媒研究 Skill。以下说明如何解锁其全部数据源。

### 当前可用数据源

| 数据源 | 状态 | 覆盖范围 | 配置要求 |
|--------|:----:|----------|----------|
| **Reddit** | ✅ | Keyless RSS 索引，30 天内帖子 | 无需配置 |
| **Hacker News** | ✅ | 30 天内帖子 | 无需配置 |
| **GitHub** | ✅ | Issues/PR 搜索 | 无需配置 |
| **Polymarket** | ✅ | 预测市场 | 无需配置 |

### 可解锁数据源

| 数据源 | 状态 | 解锁方法 | 价值 |
|--------|:----:|----------|------|
| **X/Twitter** | ❌ | 方法 1: 在 Firefox/Safari 登录 x.com → cookie 自动检测<br>方法 2: 设置 `XAI_API_KEY`（api.x.ai，免费额度）| 🔴 实时舆论信号 |
| **YouTube** | ❌ | `brew install yt-dlp` | 🔴 视频字幕 → 深度分析 |
| **TikTok** | ❌ | `SCRAPECREATORS_API_KEY`（scrapecreators.com 免费额度）| 🟡 短视频趋势 |
| **Instagram** | ❌ | `SCRAPECREATORS_API_KEY` | 🟡 视觉内容分析 |
| **Bluesky** | ❌ | `BSKY_HANDLE` + `BSKY_APP_PASSWORD` | 🟢 次要 |

### 建议解锁优先级

1. **🔴 P0 — yt-dlp**：`brew install yt-dlp`（免费，1 分钟完成）→ 启用 YouTube 字幕研究
2. **🔴 P0 — XAI_API_KEY**：注册 x.ai API（免费额度足够研究用）→ 启用 X/Twitter 实时数据
3. **🟡 P1 — SCRAPECREATORS_API_KEY**：注册 scrapecreators.com（免费额度）→ 启用 TikTok + Instagram
4. **🟢 P2 — Bluesky**：如有 Bluesky 账号可配置

---

## 十六、web-content-fetcher Skill 高级用法 ✨（v2.1 新增）

### 核心能力

| 模式 | 命令 | 速度 | 适用场景 |
|------|------|:----:|----------|
| **fast（默认）** | `fetch.py "<url>"` | 1-3s | 静态 HTML 网站（大多数品牌官网） |
| **stealth** | `fetch.py "<url>" --stealth` | 5-15s | JS 渲染/反爬网站（微信公众号、知乎） |
| **自动降级** | `fetch.py "<url>"` | — | fast 内容过少时自动切 stealth |

### DTC 研究专用路由表

| 目标网站 | 推荐模式 | 示例命令 |
|----------|:--------:|----------|
| Shopify 店铺首页 | fast | `fetch.py "https://filterbaby.com" 15000` |
| Shopify 产品页 | fast | `fetch.py "https://filterbaby.com/products/skincare-filter" 10000` |
| Amazon 产品页 | fast | `fetch.py "https://amazon.com/dp/B0XXXXX" 10000` |
| Trustpilot 评价 | fast | `fetch.py "https://trustpilot.com/review/[brand]" 10000` |
| Reddit 帖子 | fast | `fetch.py "https://reddit.com/r/XXX/comments/XXX" 8000` |
| 微信公众号 | stealth | `fetch.py "https://mp.weixin.qq.com/s/xxx" --stealth` |
| 知乎专栏 | stealth | `fetch.py "https://zhuanlan.zhihu.com/p/xxx" --stealth` |

### 输出限制建议

| 用途 | 推荐 max_chars | 说明 |
|------|:--------------:|------|
| 快速概览 | 5,000 | 看首页/About |
| 产品页详情 | 10,000 | 含描述+评价+FAQ |
| 博客全文 | 15,000 | 长文内容提取 |
| 完整页面 | 30,000 | 默认值，含所有内容 |

---

## Sources

1. FilterBaby 品牌研究（2026-06，手动审计）
2. KES DTC E-E-A-T 实施路线图（2026-06）
3. Product KB vs Community KB 对比分析（2026-06-07）
4. Google Search Quality Rater Guidelines — E-E-A-T 框架
5. SimilarWeb / SEMrush / Ahrefs 竞品分析方法论文档
6. Meta Ad Library 使用指南
7. Google Trends 数据解读方法
8. DTC 行业 CAC/LTV 基准研究（各行业报告汇集）
9. SEMrush vs Ahrefs 2026 对比分析（Truescho, 2026-04）
10. Jungle Scout vs Helium 10 2026 对比分析（Bagengine, 2026）
11. Reddit Data API 2026 免费替代方案（Web Data Labs, 2026-04）
12. Arctic Shift Reddit 归档项目（GitHub, 2026）
13. web-content-fetcher Skill 实测（WorkBuddy, 2026-06-14）
14. last30days Skill v3.3.2 实测（WorkBuddy, 2026-06-14）

---

## Change Log

| 版本 | 日期 | 变更 |
|------|------|------|
| v1.0 | 2026-06-14 | 初始版本，10 层分析框架 |
| v2.0 | 2026-06-14 | 扩展至 16 层 → 新增 L10-L16、财务估算模型、用户旅程地图、验证 SOP、持续监控体系、研究效率技巧 |
| v2.1 | 2026-06-14 | 工具体系全面升级 → 已装 Skill 实测状态（web-content-fetcher ✅ / last30days ⚠️ / Reddit API ❌ / Arctic Shift ❌ / BuiltWith ❌）、免费工具可用性逐项验证、付费工具 2026 采购建议（SEMrush Pro $117/月 P0 + Keepa €19/月 P0 + Jungle Scout $29/月 P1）、AI 辅助研究工作流 SOP、16 层→工具→命令速查表、last30days 深度配置指南、web-content-fetcher 高级用法 |
| v2.2 | 2026-06-14 | 工具配置全面补充 → last30days 完整配置（FROM_BROWSER=auto cookie 扫描 ✅ + ScrapeCreators API 接入指南）、Arctic Shift 状态更新（API ❌ 仅 Web UI ✅）、SellerSprite/Helium 10 数据获取 SOP（KES 已订阅）、Codex 浏览器操作 SEMrush 方法（3 种方案）、补充文档 `dtc-brand-research-tools-setup-guide.md` |

