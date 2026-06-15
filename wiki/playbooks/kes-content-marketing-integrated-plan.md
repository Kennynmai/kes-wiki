# KES 内容营销整合实施计划
## YouTube + Pinterest 双引擎 × KES 工作流集成

> 基于 2026-06-02 三项深度调查综合输出  
> 调查范围：YouTube 算法/竞争/转换 | Pinterest 算法/电商/API | KES 工作流/资产/能力缺口

---

## 目录

1. [核心战略修正](#1-核心战略修正)
2. [双引擎模型精化](#2-双引擎模型精化)
3. [平台级内容规格](#3-平台级内容规格)
4. [KES 集成架构](#4-kes-集成架构)
5. [分阶段执行路线图](#5-分阶段执行路线图)
6. [内容日历框架](#6-内容日历框架)
7. [归因与度量体系](#7-归因与度量体系)
8. [风险与缓解](#8-风险与缓解)
9. [P0 立即行动清单](#9-p0-立即行动清单)

---

## 1. 核心战略修正

### 1.1 原计划 vs 调查结论

| 维度 | 原假设 | 调查修正 | 影响 |
|------|--------|----------|------|
| **YouTube 竞争态势** | 竞争激烈，需要差异化 | **蓝海**：零个 DTC 浴室五金品牌做 YouTube | 策略从"差异化"转为"先占位" |
| **Pinterest 流量来源** | Saves + Repins 驱动分发 | **90%+ 来自 Fresh Pins**（全新创作），Saves 几乎不驱动分发 | Pin 策略从"复用"转为"多版本创作" |
| **内容复用比** | 80% 复用 / 20% 新拍 | 平台算法要求实质不同 → **50/30/20**（50% 平台原生 / 30% 适配 / 20% 直接复用） | 产能预期下调，首批内容量减半 |
| **Pinterest 启动速度** | 立即自动化发 Pin | Trial Access 的 Pin **对公众不可见**；Standard Access 审批 1-4 周 | Phase 1 前必须人工发 Pin 过渡 |
| **YouTube Shorts 性质** | Evergreen 搜索引擎 | **非 Evergreen**：recency-biased 推荐流，时效衰减快 | Shorts 定位从"资产"调整为"流量入口" |
| **AI 生成素材** | 可补充素材缺口 | Pinterest 2025 上线 AI 检测 → 自动标记 + 用户可过滤 | **必须用真实产品照片**，AI 素材仅限内部 mockup |
| **Topic Authority** | 未提及 | YouTube 2025-2026 算法新超级力量：30 条同领域视频 > 泛化频道单条优化 | YouTube 策略必须聚焦单一细分领域 |

### 1.2 战略定位修正

```
修正前：YouTube + Pinterest = 两个 evergreen 搜索引擎，大量复用素材铺量

修正后：YouTube = Trust Engine（信任建立，6-12月见效）
        Pinterest = Discovery Engine（灵感触达，数周见效）
        Shorts/Reels = Distribution Amplifier（流量入口，即时曝光）
        
        KES = Content Operations Backbone（内容运营中枢）
```

---

## 2. 双引擎模型精化

### 2.1 三平台差异化定位

| 维度 | YouTube Long-form | Pinterest | YouTube Shorts / Reels |
|------|-------------------|-----------|------------------------|
| **核心功能** | 建立信任与权威 | 触发灵感与发现 | 扩大触达与引流 |
| **用户意图** | "我要学会/了解/比较" | "我要找灵感/方案" | "刷到什么是什么" |
| **内容形态** | 8-15 分钟教程/评测 | 静态竖版图（89% 病毒 Pin） | 15-60 秒竖版视频 |
| **分发机制** | 搜索 + 推荐（搜索为主） | 搜索 + 推荐（搜索为主） | 算法推荐流 |
| **内容寿命** | 数月–数年（长尾搜索） | 16 周中位数，峰值 1-2 年 | 数天–数周（时效衰减） |
| **见效时间** | 3-6 个月（topic authority 积累） | 数周（Fresh Pin 即时分发） | 数天（如命中算法） |
| **生产门槛** | 高（拍摄、剪辑、SEO） | 低（静态图 + 文案） | 中（剪辑节奏要求高） |
| **转化路径** | 搜索 → 视频 → 描述链接 → PDP | 浏览 → Pin → 外链 → PDP | 刷到 → Shorts → 长视频/频道 → PDP |
| **归因方式** | UTM + YouTube Analytics | Pinterest Tag + Conversions API | 辅助转化（assist，非 last-click） |
| **KES 对应** | 长文内容生产流程 | 批量素材生产流程 | 轻量剪辑流程 |

### 2.2 用户旅程映射

```
                ┌─────────────────────────────────────────────────────┐
                │                   CUSTOMER JOURNEY                    │
                └─────────────────────────────────────────────────────┘

   AWARENESS          CONSIDERATION          DECISION            RETENTION
   ─────────          ─────────────          ────────            ─────────
   
   Pinterest          YouTube                Google               YouTube
   "small bathroom    "grab bar              "buy grab bar"       "how to clean
    ideas"            installation"                               grab bar"
        │                  │                     │                    │
        ▼                  ▼                     ▼                    ▼
   Pin → Save         Video → Channel       Product Page         Post-purchase
   (灵感触动)          Sub → Website          → Purchase            tutorial
        │                  │                     │                    │
        ▼                  ▼                     ▼                    ▼
   ┌────────┐         ┌────────┐            ┌────────┐           ┌────────┐
   │ 70%    │         │ 55%    │            │ 30%    │           │ 15%    │
   │ 首次   │         │ 首次   │            │ 直接   │           │ 回访   │
   │ 触达   │         │ 触达   │            │ 搜索   │           │ 复购   │
   └────────┘         └────────┘            └────────┘           └────────┘
        │                  │                     │                    │
        └──────────────────┴─────────────────────┴────────────────────┘
                                   │
                           KES Content Pipeline
                           (统一生产 → 多渠道分发 → 归因回写)
```

### 2.3 6 内容支柱的平台分配

| 支柱 | YouTube Long-form | Pinterest | Shorts/Reels | 优先级 |
|------|:---:|:---:|:---:|:---:|
| **A. 安装 How-to** | ★★★ 主力（8-15min） | ★★ 步骤图解 Pin | ★★ 15-30s 快剪 | P0 |
| **B. 选购对比** | ★★★ 主力（8-12min） | ★★ 对比图 Pin | ★ 结果速览 | P0 |
| **C. 灵感造型** | ★ 合集视频 | ★★★ 主力（Before/After） | ★★ 变装风格 Shorts | P1 |
| **D. 产品 FABE** | ★★ 深度讲解 | ★★★ 主力（Product Pin + Catalog） | ★ 单卖点快剪 | P0 |
| **E. 社证/UGC** | ★★ 客户案例 | ★★ 实拍分享 | ★★★ 主力（真实感） | P1 |
| **F. 品牌信任** | ★★★ 主力（实验室/工艺） | ★★ 品牌理念 Pin | ★ 幕后 Shorts | P2 |

---

## 3. 平台级内容规格

### 3.1 YouTube Long-form 规格

#### 内容类型与时长

| 内容类型 | 最优时长 | 结构模板 |
|----------|----------|----------|
| 安装教程 | 8-15 分钟 | Hook(0-15s) → 工具清单 → 步骤 1-N → 常见错误 → CTA |
| 产品横评 | 8-12 分钟 | Hook → 评测标准 → 逐个产品 → 对比表 → 推荐 → CTA |
| 灵感合集 | 3-8 分钟 | Before/After → 设计原则 → 产品推荐 → CTA |
| 品牌故事 | 5-10 分钟 | 问题 → 解决方案 → 工艺展示 → 客户见证 → CTA |

#### 制作规格

| 元素 | 规格 |
|------|------|
| 分辨率 | 1080p 最低，建议 4K |
| 缩略图 | 1280×720px, <2MB, 3-4 字, 粗体无衬线, 人脸占比 ≥25% |
| 标题 | <60 字符, 关键词前置, 用数字不用中文数字 |
| 描述 | 150-250 字, 前 200 字符含 hook + 关键词, Timestamps 章节 |
| 字幕 | 必须（85% Shorts 无声观看，YouTube 自动字幕用于搜索索引） |
| 标签 | 3-5 个相关 Hashtag |

#### SEO 策略（50 长尾词矩阵）

**竞争分析结论**：高搜索量核心词（"grab bar installation"、"how to install towel bar"）被 This Old House / Lowe's / Home Depot / wikiHow 垄断（DA 80+）。新频道必须走**长尾词策略**。

**关键词分层**：

```
Tier 1: 核心词（DA 80+ 垄断，新频道不碰）
├── "how to install grab bar"
├── "bathroom grab bar"
└── "towel bar installation"

Tier 2: 长尾机会词（中等搜索量，低竞争）★ 主攻
├── "install grab bar without drilling tile"
├── "grab bar stud vs drywall anchor"
├── "ADA grab bar placement height"
├── "best grab bars for elderly 2026"
├── "grab bar weight capacity 500 lbs"
├── "modern grab bar that doesn't look medical"
├── "towel bar height standard bathroom"
├── "rental friendly bathroom grab bar"
├── "shower shelf no drilling"
└── "bathroom safety makeover aging in place"

Tier 3: 蓝海词（几乎零竞争）★ 先占
├── "grab bar brand comparison test"
├── "matte black grab bar review"
├── "UK vs US grab bar standards"
├── "tile drilling grab bar tips"
├── "bathroom hardware metal vs plastic durability"
└── "accessible bathroom complete guide"
```

### 3.2 Pinterest 规格

#### Pin 格式与使用场景

| 格式 | 占比 | 规格 | 使用场景 |
|------|:---:|------|----------|
| **标准图片 Pin** | 60-70% | 2:3 竖版 (1000×1500px) | 产品展示、生活方式、教育信息图 |
| **轮播 Pin** | 20-30% | 2:3 竖版 × 2-5 张 | 产品多角度、Before/After 步骤、颜色选项 |
| **视频 Pin** | 10-15% | 竖版 <15 秒 | 安装演示、产品特写、Before/After 动效 |

#### 每产品 Pin 裂变策略

```
1 次拍摄 → 1 个产品 → 3-5 个 Fresh Pins（不同关键词定位）

示例：Matte Black Grab Bar

Pin 1: "Modern Matte Black Grab Bar — ADA Compliant Bathroom Safety"
       → 关键词: matte black grab bar, modern bathroom hardware
       → 视觉: 产品在当代风格浴室中，强调设计感

Pin 2: "Bathroom Safety for Seniors — Easy-Install Grab Bar Guide"
       → 关键词: bathroom safety seniors, aging in place bathroom
       → 视觉: 适老化浴室场景，突出易安装

Pin 3: "Small Bathroom Ideas — Space-Saving Grab Bar + Towel Bar Combo"
       → 关键词: small bathroom ideas, bathroom storage solutions
       → 视觉: 小浴室整体方案，展示空间利用率

Pin 4: "Before & After: Rental-Friendly Bathroom Upgrade (No Drilling!)"
       → 关键词: rental bathroom upgrade, no drill bathroom hardware
       → 视觉: Before/After 对比，强调免打孔

Pin 5: "Spring Bathroom Refresh — Top 5 Hardware Upgrades Under $50"
       → 关键词: bathroom refresh ideas, affordable bathroom upgrade
       → 视觉: 春季色调，多产品组合展示
```

#### 发布节奏

| 阶段 | 频率 | 说明 |
|------|------|------|
| Phase 0 (人工发) | 3-5 Fresh Pins/周 | 新账号建立期，保守起步 |
| Phase 1 (走量) | 5-10 Fresh Pins/天 | 电商量级，建立搜索覆盖 |
| Phase 2+ (自动化) | 5-10 Fresh Pins/天 + Tailwind SmartPin | API 自动发 + SmartPin 每周为每个 URL 生成新 Pin |

**发布窗口**：8AM–4PM 工作日，Pin 间隔 2-3 小时

#### 必备设置

1. **Rich Pins**（Product Rich Pins）：自动同步价格、库存
2. **Pinterest Catalogs**：上传全量产品目录 → 自动生成 shoppable Pins
3. **Pinterest Tag**（客户端）+ **Conversions API**（服务端）：双轨追踪
4. **Alt Text**：每 Pin 必加（+123% 外链点击）

### 3.3 Shorts / Reels 规格

| 元素 | 规格 |
|------|------|
| 格式 | 9:16 竖版 |
| 帧率 | 60fps（+23% retention） |
| 时长 | 15-60 秒（22 秒 sweet spot） |
| 字幕 | 必须（85% 无声观看） |
| CTA 位置 | 21-25 秒（+267% CTR） |
| 链接 | 描述区优惠码（+356% CTR） |

#### Shorts → Long-form 漏斗

```
Shorts (15-30s)           Long-form (8-15min)         Website
─────────────────         ───────────────────         ────────
"3 grab bar mistakes"     "Complete grab bar          PDP with
 → 只说 2 个              installation guide"         UTM link
 → CTA: "Full guide       → 完整教程
   on channel"            → 描述区产品链接
                          → 优惠码
```

---

## 4. KES 集成架构

### 4.1 端到端内容管线 × KES 工作流

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    KES Content Marketing Pipeline                        │
└─────────────────────────────────────────────────────────────────────────┘

  KES Stage          Content Stage         Tool/System              Output
  ─────────          ─────────────         ────────────             ──────
                                          
  Capture            Research              web_content_fetcher.py   原始灵感
  ───────            ────────              → inbox/                 竞品内容
                                          
  Classify           Content Planning      ingestion-registry.md    Brief 入库
  ────────           ────────────────      → 新建 content-brief     关键词分配
                                           模板                     
  Narrow             Opportunity Scoring   LLM 产品研究 Protocol    优先级矩阵
  ──────             ───────────────────   → 7-axis 评分模型        选题决策
                                          
  Extract            Brief Generation      营销研究 Doc              Content Brief
  ───────            ────────────────      → 17+ 字段 Schema         脚本/文案
                                           StoryBrand Framework     
                                          
  Deepen             Content Production    拍摄/剪辑/设计            成品素材
  ──────             ──────────────────    → raw/marketing/          
                                          
  Update             Publishing            Content Calendar          已发布内容
  ──────             ──────────            → Pinterest / YouTube     + 归因数据
                                           → 人工发 (Phase 0-1)     
                                           → API 自动 (Phase 2+)    
                                          
  Verify             Quality Review        5-Dimension Rubric        审批通过
  ──────             ──────────────        Verification Policy       → gate ✅
                                           (grab bar 安全声明强制    → 或退回修改
                                            事实核查)                
                                          
  Lint               Performance Audit     Marketing Dashboard       优化决策
  ────               ─────────────────     → 赢家加码 / 输家裁撤     → 更新原则
                                           → 月度回顾 → 更新        
                                             principles-layer       
```

### 4.2 复用现有 KES 能力

| 现有 KES 资产 | 路径 | 内容营销用途 | 适配方式 |
|-------------|------|-------------|----------|
| **营销研究总 Doc** | `wiki/questions/电商页面图片生成与内容规划研究.md` | Brief Schema, 5 叙事策略, 说服模型, 5 维评估表 | 直接使用，将 "Amazon PDP" 替换为 "YouTube/Pinterest Content" |
| **StoryBrand 框架** | `wiki/source-summaries/building-a-storybrand.md` | YouTube 视频叙事结构 + Pin 文案英雄旅程 | 直接套用 Hero → Problem → Guide → Plan → CTA |
| **STEPPS 病毒框架** | `wiki/source-summaries/contagious-why-things-catch-on.md` | Shorts 传播设计, Pin 标题 A/B 测试 | 6 原则逐条检查每件内容 |
| **Cialdini 7 原则** | 营销研究 Doc 内嵌 | Landing Page CTA, Pin 描述说服链 | 与 Fogg B=MAP 配合 |
| **电商运营 KPI 框架** | `wiki/protocols/cross-border-ecommerce-operations-performance-framework.md` | 营销 KPI 分层（活动→触达→流量→转化→效率） | 4 层架构直接适配，替换指标 |
| **LLM 产品研究 Protocol** | `wiki/protocols/llm-product-market-research-for-kes-categories.md` | 内容机会研究（替代产品机会研究） | 7 输出 → 7 内容输出, 7-axis → 7-axis 内容评分 |
| **Ingestion Registry** | `ops/ingestion-registry.md` | 内容生产追踪（10 阶段生命周期） | 新增阶段："scheduled" / "published" / "analyzed" |
| **Dashboard 约定** | `governance/dashboard-conventions.md` | 新建 Content Calendar + Marketing Dashboard | 遵循一行一实体、一 Dashboard 一领域 |
| **品牌 VI** | `raw/kes/brand-vi/` | 品牌视觉一致性 + 本地化适配 | UK/US 市场差异化（GBP 标价、UK 拼写、ADA → UK Building Regs） |
| **营销书库** | `raw/books/marketing/` + `wiki/source-summaries/` | 内容策略持续参考 | 按需查询 |

### 4.3 需新建的 KES 能力（8 项）

| # | 新建能力 | 类型 | 依赖 | 优先级 | KES 路径 |
|---|---------|------|------|:---:|------|
| 1 | **Content Calendar Dashboard** | Dashboard | Dashboard 约定 | P0 | `dashboards/content-calendar.md` |
| 2 | **Content Brief 模板** | Template | 营销研究 Doc (17 字段) | P0 | `templates/content-brief.md` |
| 3 | **YouTube 视频脚本模板** | Template | StoryBrand + 营销研究 Doc | P0 | `templates/youtube-script.md` |
| 4 | **Pinterest Pin 设计 Brief 模板** | Template | 营销研究 Doc (Amazon 9 图策略) | P0 | `templates/pin-brief.md` |
| 5 | **Content Production Protocol** | Protocol | AGENTS.md 8 阶段 + LLM 产品研究 Protocol | P1 | `wiki/protocols/content-production-workflow.md` |
| 6 | **Marketing KPI Dashboard** | Dashboard | Dashboard 约定 + 电商运营 KPI 框架 | P1 | `dashboards/marketing-kpi.md` |
| 7 | **SEO/关键词追踪系统** | Dashboard | 50 词矩阵 (Tier 1/2/3) | P1 | `dashboards/keyword-tracker.md` |
| 8 | **内容素材库 (Content DAM)** | 目录结构 | `raw/marketing/` | P2 | `raw/marketing/assets/` |

---

## 5. 分阶段执行路线图

### Phase 0: 基建 + 首批内容（Week 1-4）

```
目标：系统就绪，首批 30-50 条内容产出，全部人工发布
状态：MVP — 零 API 依赖
```

| 周 | KES 建设 | YouTube | Pinterest | 产出量 |
|:---:|---------|---------|-----------|:---:|
| **W1** | 新建 Content Calendar Dashboard + Content Brief 模板 + YouTube/Pinterest 模板 | 确定第一批 10 个 Tier 2 长尾词 | **立即提交 Pinterest Standard Access 申请**；设置 Rich Pins + Catalog | 0（基建周） |
| **W2** | 关键词矩阵录入；首发 Brief 生成（5 条 YouTube + 10 个 Pin 设计） | 拍摄 1 条安装教程 + 1 条产品评测 | 从现有产品图库生成 3 Fresh Pins/产品 × 5 产品 | 2 视频 + 15 Pins |
| **W3** | Brief → 成品流水线试跑（人工 gate） | 剪辑 + 发布 W2 拍摄内容 | 继续 Fresh Pins（5/天） | 2 视频 + 25 Pins |
| **W4** | Phase 0 回顾；修正模板和流程 | 拍摄 1 条品牌信任视频（实验室/工艺） | 制作 2 个 Idea Pin（步骤图解教程） | 1 视频 + 25 Pins + 2 Idea Pins |

**Phase 0 产出合计**：5 条 YouTube Long-form + 65 Pins + 2 Idea Pins

**里程碑**：
- [ ] Pinterest Standard Access 申请已提交
- [ ] Content Calendar 上线运行
- [ ] 3 个 Brief 模板完成初版
- [ ] 首批 YouTube 视频发布

### Phase 1: 双引擎启动（Week 5-12）

```
目标：YouTube 搜索覆盖建立，Pinterest 走量启动
依赖：Pinterest Standard Access 到手（否则人工发布继续）
```

| 周 | YouTube | Pinterest | Shorts 副产品 | KPI 追踪 |
|:---:|---------|-----------|:---:|---------|
| **W5-6** | 2 条安装教程 + 1 条选购对比 | 10 Fresh Pins/天（或 API 自动发布） | 每条 Long-form → 3-5 Shorts | 建立基线 |
| **W7-8** | 2 条安装教程 + 1 条灵感合集 | 同上 + 启动 Shopping Ads ($1,000/月测试) | Shorts 节奏稳定 | 首次月度回顾 |
| **W9-10** | 2 条选购对比 + 1 条品牌信任 | 同上 + A/B 测试 Pin 设计（颜色/文案/CTA） | Shorts 跑量 | 按 pillar 分析 |
| **W11-12** | 核心词首次尝试（1 条 Tier 1） | 基于 Pinterest Analytics 淘汰低效 Pin 设计 | Shorts 跑量 | Phase 1 终期回顾 |

**Phase 1 产出合计**：12 条 YouTube Long-form + 400-500 Pins + 60-80 Shorts

**关键决策点（Week 12）**：
- 哪些 Tier 2 关键词已进入 YouTube 首页？
- 哪些 Pin 设计 CTR > 1%？
- 是否有内容 pillar 明显 outperforming？
- Shopping Ads ROAS 是否 > 3x？

### Phase 2: 稳定生产 + 自动化（Week 13-26）

```
目标：内容管线半自动化，数据驱动优化，副产物渠道扩展
```

| 模块 | 动作 |
|------|------|
| **YouTube** | 维持 1-2 条/周；测试 1 条 Tier 1 核心词；启动社区 Tab（达到 500 订阅后） |
| **Pinterest** | API 自动发布全面上线；Tailwind SmartPin 启用；Shopping Ads 按 ROAS 加码 |
| **Shorts/Reels** | 内容复用流水线成熟；TikTok + IG Reels 同步分发（零额外成本） |
| **KES** | Content Production Protocol 正式化；Marketing KPI Dashboard 上线；首次 Content DAM 建设 |
| **归因** | 非 UTM 归因三保险实施（专属 URL + 优惠码 + Post-Purchase Survey） |
| **本地化** | UK 版 Pin 描述（British English 拼写 + GBP 标价 + UK Building Regulations 引用） |

**Phase 2 产出合计**：20-25 条 YouTube + 600-900 Pins + 150-200 Shorts

**关键决策点（Week 26）**：
- 是否达到 YouTube 1,000 订阅？
- YouTube Shopping 功能是否已启用？
- 是否启动 EU 本地化（DE/FR）？

### Phase 3: 数据驱动规模化（Week 27+）

```
目标：按 UTM→订单数据加码赢家，启动 EU 本地化
前置条件：UTM 归因链路成熟 + 至少 6 个月流量数据
```

| 动作 | 条件 |
|------|------|
| **赢家加码**：UTM→订单转化率 Top 20% 的内容 → 投入付费推广 | 累计 >50 笔可归因订单 |
| **输家裁撤**：连续 3 个月 CTR < 行业基准 50% 的内容 → 归档或重做 | 月度 Performance Audit |
| **EU 本地化**：DE 市场优先（YouTube + Pinterest DE 版） | UK 市场验证成功 |
| **YouTube 广告**：长视频作为广告素材（YouTube Ads 引流到 PDP） | 自然流量 ROAS 基线建立 |
| **KES 原则更新**：Content Compounding 原则入库 | Phase 1-2 经验沉淀 |

---

## 6. 内容日历框架

### 6.1 KES Content Calendar Dashboard 结构

```markdown
# Content Calendar

> type: dashboard | status: active | domain: content-marketing

| ID | Status | Platform | Pillar | Title/Keyword | Brief | Due | Published | Views | CTR | Conv | Notes |
|----|--------|----------|--------|---------------|-------|-----|-----------|-------|-----|------|-------|
| YT-001 | published | youtube | A-install | install-grab-bar-without-drilling | brief-001 | 2026-06-15 | 2026-06-16 | 1,240 | 8.2% | 2 | - |
| YT-002 | in-prod | youtube | B-compare | best-grab-bars-2026-comparison | brief-002 | 2026-06-22 | - | - | - | - | filming W2 |
| PT-001 | scheduled | pinterest | D-fabe | matte-black-grab-bar-ada | brief-003 | 2026-06-14 | 2026-06-14 | 890 | 1.1% | 0 | Pin variant A |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

## Stats
- Total live: 12 | Scheduled: 8 | In production: 5 | In brief: 10
- MTD YouTube views: 15,400 | Pinterest impressions: 45,200
- MTD attributed orders: 14 | Revenue: $1,260
```

### 6.2 月度批量生产节奏

```
Week 1: Brief Week
  Mon: 关键词研究 + 选题确认
  Tue-Wed: Brief 生成（KES Content Brief 模板）
  Thu: Brief Review Gate（人工审核）
  Fri: 素材清单确认

Week 2: Production Week
  Mon-Tue: 拍摄（1 天集中拍摄，产出 1 月素材）
  Wed-Fri: 剪辑 / Pin 设计

Week 3: Publishing Week
  Mon: YouTube 发布 #1
  Wed: YouTube 发布 #2
  Daily: Pinterest Fresh Pins 发布（5-10/天）
  Daily: Shorts 发布（1-2/天，复用 Long-form）

Week 4: Review Week
  Mon-Tue: 指标收集（YouTube Analytics + Pinterest Analytics）
  Wed: Content Performance Report
  Thu: 月度回顾 → 更新 Content Calendar + KPI Dashboard
  Fri: 下月选题调整
```

### 6.3 季节性内容日历

| 月份 | 主题 | 内容焦点 | Pinterest 高峰 |
|------|------|----------|:---:|
| **1 月** | 新年改造 | 浴室翻新灵感 + 预算规划 | ★★★ Q1 高峰 |
| **2 月** | 适老化改造 | 老人浴室安全方案（配合 Valentine's 家庭关怀角度） | ★★★ |
| **3 月** | 春季刷新 | 春季浴室升级 Top 10 | ★★★ |
| **4 月** | 免打孔方案 | 租房友好 + 春季大扫除 | ★★ |
| **5 月** | 母亲节/父亲节 | 父母浴室安全礼物指南 | ★★ |
| **6 月** | 夏季防霉 | 浴室通风 + 不锈钢材质重要性 | ★ |
| **7 月** | 暑假 DIY | 自己动手安装教程合集 | ★ |
| **8 月** | 返校季 | 学生公寓浴室收纳方案 | ★ |
| **9 月** | 秋季翻新 | 浴室翻新前必看 | ★★ |
| **10 月** | 万圣节/秋冬准备 | 浴室保暖 + 防滑安全 | ★★ |
| **11 月** | Black Friday | 礼物指南 + 折扣预告 | ★★ |
| **12 月** | 年终总结 | 年度最佳产品 + 新年预告 | ★ |

---

## 7. 归因与度量体系

### 7.1 KPI 五层架构（适配自电商运营框架）

| 层级 | 指标 | 数据源 | 目标（Month 3） | 目标（Month 6） |
|:---:|------|--------|:---:|:---:|
| **L1: 活动** | 内容发布量 | Content Calendar | 20-30/月 | 40-60/月 |
| **L2: 触达** | YouTube 观看 + Pinterest 展示 | YouTube Analytics, Pinterest Analytics | 50K/月 | 200K/月 |
| **L3: 流量** | 网站点击（UTM + 专属 URL） | Google Analytics + Pinterest Tag | 2,000/月 | 10,000/月 |
| **L4: 转化** | UTM 归因订单（三重验证） | Shopify + Google Analytics + Post-Purchase Survey | 20/月 | 100/月 |
| **L5: 效率** | 单次点击成本 (CPC), ROAS (if paid) | 各平台 Analytics | CPC <$0.50 | CPC <$0.30 |

### 7.2 非 UTM 归因三保险

```
原计划依赖：UTM → 订单（单一归因路径）
修正方案：三重验证减少 20-40% dark traffic 信号丢失

保险 1: 专属落地页 URL
  youtube.kessafety.com/grab-bar-install
  pin.kessafety.com/modern-bathroom
  → 独立于 UTM，不受参数剥离影响

保险 2: 渠道专属优惠码
  YOUTUBE10, PINTEREST15, SHORTS5
  → 直接反映渠道转化，不受隐私限制

保险 3: Post-Purchase Survey
  "How did you first hear about us?"
  → 捕获跨设备/跨会话转化
  → 样本推估全量（行业基准：Survey 样本 × 15-25 = 实际归因）
```

### 7.3 Pinterest 归因配置

| 配置项 | 推荐值 | 原因 |
|--------|:---:|------|
| 归因窗口 | **30 天点击 + 30 天浏览** | 浴室五金是高客单价长决策品类 |
| 追踪方式 | **Pinterest Tag + Conversions API 双轨** | +28% 归因转化，-14% CPA |
| Enhanced Match | **开启** | 跨设备匹配，提升归因准确度 |

---

## 8. 风险与缓解

| # | 风险 | 可能性 | 影响 | 缓解措施 | 负责人 |
|:---:|------|:---:|:---:|------|:---:|
| R1 | Pinterest Standard Access 审批被拒或超 4 周 | M | H | Day 1 提交 + 视频 Demo（含 OAuth 完整流程）；被拒后立即重提 | Tech |
| R2 | YouTube 频道 0-1K 订阅超 6 个月 | M | M | Shorts 加速订阅（驱动 40% 新增）；每视频末强制 CTA 订阅；合作互推 | Content |
| R3 | UTM 归因数据不足以支撑 Phase 3 决策 | H | M | 三保险方案（专属 URL + 优惠码 + Survey）Phase 2 上线 | Data |
| R4 | 内容生产瓶颈（人力不足） | H | H | 月度集中拍摄 → 批量产出；Tailwind SmartPin 自动化；AI 辅助初稿 | Ops |
| R5 | Grab bar 安全声明合规风险 | L | H | KES Verification Policy 强制执行；安装声明需引用 ADA/UK Building Regs 原文；LLM 生成内容人工事实核查 | Legal |
| R6 | Pinterest AI 检测误标真实照片 | L | L | 保留原始 RAW 文件 + 拍摄元数据；被误标后利用 Appeals 流程申诉 | Content |
| R7 | 竞品跟随进入 YouTube/Pinterest | M | L | First-mover 优势（6-12 月窗口）；通过 Topic Authority 积累建立护城河 | Strategy |

---

## 9. P0 立即行动清单

### Day 1（今天）

- [ ] **提交 Pinterest Standard Access 申请**（含完整 OAuth 流程视频 Demo）
- [ ] 在 KES 中新建 `dashboards/content-calendar.md`（遵循 Dashboard 约定）
- [ ] 在 KES 中新建 `templates/content-brief.md`（适配自营销研究 Doc 17 字段 Schema）

### Week 1

- [ ] **完成 50 词双平台关键词矩阵**（Tier 1/2/3 分层）
- [ ] 设置 Pinterest Business Account + Rich Pins + Catalogs
- [ ] 创建 YouTube 频道（品牌名一致，完善 About 页 + 链接）
- [ ] 新建 `templates/youtube-script.md` + `templates/pin-brief.md`

### Week 2

- [ ] **首批 Brief 生成**（5 条 YouTube + 10 个 Pin 设计）
- [ ] 设计非 UTM 归因三保险的技术方案
- [ ] Pinterest Tag + Conversions API 部署

### Phase 0 结束前（Week 4）

- [ ] Phase 0 回顾 → 决定是否按原计划进入 Phase 1
- [ ] Content Calendar 已运行 4 周 → 评估产能节奏
- [ ] Pinterest Standard Access 状态确认 → 决定 Phase 1 发布方式（人工 vs API）

---

## 附录

### A. KES 待建模板清单

| 模板 | 路径 | 参考来源 |
|------|------|----------|
| Content Brief | `templates/content-brief.md` | 营销研究 Doc 17 字段 |
| YouTube 视频脚本 | `templates/youtube-script.md` | StoryBrand + Hook-Story-Offer |
| Pinterest Pin Brief | `templates/pin-brief.md` | Amazon 9 图策略适配 |
| Content Production Protocol | `wiki/protocols/content-production-workflow.md` | AGENTS.md + LLM 产品研究 Protocol |

### B. KES 待建 Dashboard 清单

| Dashboard | 路径 | 参考来源 |
|-----------|------|----------|
| Content Calendar | `dashboards/content-calendar.md` | Dashboard 约定 |
| Marketing KPI | `dashboards/marketing-kpi.md` | 电商运营 KPI 框架 + Dashboard 约定 |
| Keyword Tracker | `dashboards/keyword-tracker.md` | 50 词矩阵 Tier 1/2/3 |

### C. 调查数据来源

- **YouTube**: Backlinko (1.3M 视频研究), YouTube Creator Academy, Todd Beaupre (YouTube Growth Director), ATTN Agency ($15M+ 广告支出分析), FeedSpot (60 家装频道), 40+ 文章/案例
- **Pinterest**: Pinterest Business Blog, Tailwind, GenSumo Research (2026), Metricool, Zernio (API v5 文档), Pinterest Community Forums, 10+ 电商案例
- **KES**: 完整工作区探索（247 行 index.md, 179K 字符 log.md, 2000 行营销研究 Doc, 8 本营销书库, 5 个 Dashboard, 5 个 Python 脚本, 43 行 ingestion registry）
