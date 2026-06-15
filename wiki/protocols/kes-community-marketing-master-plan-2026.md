---
type: synthesis
status: draft
created: 2026-06-07
updated: 2026-06-07
domain: marketing-operations
domains: [community-marketing, kes, execution-plan, methodology]
confidence: high
verification_status: designed
related:
  - wiki/principles/community-marketing-meta-principle.md
  - wiki/syntheses/community-marketing-cross-platform-2026.md
  - wiki/syntheses/kes-community-marketing-implementation-2026.md
  - wiki/protocols/reddit-post-discovery-system-design.md
  - wiki/protocols/ai-draft-pipeline-design.md
  - wiki/protocols/kes-community-voice-guide.md
  - wiki/protocols/kes-negative-response-handbook.md
---

# KES 社区营销方法论体系与落地细化执行计划

> 本文档是 KES 社区营销的「总作战图」。
> 先理解方法论体系（为什么），再按执行计划推进（怎么做）。

---

## 第一部分：方法论体系总图

### 体系架构（三层）

```
元原则层（Why — 不变的底层逻辑）
│
├── 帮助优先：删掉品牌提及，回复还有价值吗？
├── 信任是货币：账号 karma/声誉 = 唯一可积累资产
├── 复合周期 3-12 个月：不是流量购买，是资产积累
├── 内容即资产：一次智力投入，长期复合回报
└── 衡量用信任信号：被引用次数 > 最后点击
    │
    ▼
平台方法论层（What — 每个平台怎么做）
│
├── Reddit：三手册（热身/参与/危机）× 四阶段阶梯
├── Quora：B2B 线索引擎 ×逐答案凭据×SEO 资产
├── Discord：七步社区建设框架 × 角色权限设计
├── Slack：五阶段专业社区 × 10:1 贡献比例
└── 垂直论坛：四大支柱 × 评估过滤器 × 长尾效应
    │
    ▼
KES 执行层（How — KES 具体怎么做）
    │
    ├── 产品知识库（问题→答案→证据）
    ├── 账号资产体系（@keshome.com + 2FA + 离职收回）
    ├── 帖子发现系统（Arctic Shift + last30days 双轨）
    ├── AI 起草流水线（抓取→匹配→起草→审核）
    ├── KES 社区声音指南（6 情感骨架 + 12 词 blacklist）
    └── 负面回应处理手册（11 场景 + L0-L4 升级路径）
```

---

### 各层之间的引用关系

| 执行层文件 | 依赖的方法论 | 输出的资产 |
|--------------|--------------|----------|
| 产品知识库 | 元原则「帮助优先」 | 所有回复的实质内容来源 |
| 帖子发现系统 | 各平台方法论 + Arctic Shift 能力边界 | 每日待回复清单 |
| AI 起草流水线 | KES 声音指南 + 产品知识库 | 回复草稿（需人工审核）|
| KES 社区声音指南 | 元原则 + kes-wiki 品牌资料 | 所有社区回复的语气规范 |
| 负面回应处理手册 | 各平台版规 + FTC 合规要求 | 危机处理 SOP |
| 账号资产体系 | FTC 披露要求 + 各平台 ToS | 可收回、合规的账号矩阵 |

---

## 第二部分：落地细化执行计划

### 总体时间线

```
Week 0-1   → 基础设施搭建（知识库骨架 + 账号注册 + 工具配置）
Week 2-4   → 账号热身（只评论，不提 KES）
Week 5-8   → 有价值评论（建立声誉，谨慎提产品）
Week 9-12  → 发帖测试（每周 1-2 帖，测量反应）
Week 13+   → 全面覆盖 + 迭代优化
```

---

### Phase 0：基础设施搭建（Week 0-1）

#### 交付物清单

| # | 交付物 | 负责人 | 完成标准 | 依赖 |
|---|----------|--------|----------|------|
| 1 | KES 产品知识库骨架 | Kenny + 产品经理 | 目录结构创建完成，`pain-points.md` 各填 3 条以上 | kes-wiki 品牌资料 |
| 2 | 账号注册（Reddit × 2, Quora × 1） | Kenny | 用 @keshome.com 注册完成，2FA 绑定 Google Workspace | Google Admin 权限 |
| 3 | Arctic Shift 监控脚本配置 | Kenny（或技术同事） | 能跑通一次，输出 pending-reviews.md | 无代码，见 protocol |
| 4 | 负面回应处理手册阅读 | Kenny + 未来社区经理 | 所有人读完 `kes-negative-response-handbook.md` | 无 |
| 5 | KES 社区声音指南签署 | Kenny + 未来社区经理 | 所有人确认理解声音指南 | 无 |

#### 知识库骨架细化（Phase 0 核心交付）

**卫浴五金产品线**：

```
wiki/products/kes-product-knowledge-base/products/bathroom-hardware/
├── meta-principle.md         ← 从 kes-wiki 提炼，50-100 字
├── pain-points.md            ← 至少 5 条，格式：「用户原话」+「KES 答案」+「证据来源」
├── competitor-comparisons.md ← GROHE / Moen / Delta 各 1 条对比维度
└── test-data/
    ├── salt-spray-corrosion.md      ← 如果没有数据，标注「2026-Q3 补测」
    ├── cycle-life-faucet.md
    └── plastic-vs-metal-valve.md
```

**窗帘系统（Egypt）产品线**：

```
wiki/products/kes-product-knowledge-base/products/curtain-roller-blind-egypt/
├── meta-principle.md         ← 「耐高温织物 + 加厚铝管 + 链条寿命」
├── pain-points-egypt.md      ← 至少 5 条埃及用户痛点
├── competitor-gap.md        ← 埃及本地常见产品的具体短板
└── test-data/
    ├── fabric-UV-resistance.md
    ├── aluminum-profile-thickness.md
    └── chain-durability.md
```

> ⚠️ **Phase 0 阻塞条件**：如果 `test-data/` 下有任何文件标注「无数据」，必须先安排实验室测试，或明确标注「2026-Q3 补测」并在社区回复中诚实说明。

---

### Phase 1：账号热身（Week 2-4）

#### 每周时间分配

| 活动 | 每周时间 | 具体做法 | 测量标准 |
|------|----------|----------|----------|
| Reddit 无品牌评论 | 3-4h | 在 r/HomeImprovement / r/DIY 评论，**完全不提 KES** | 每周 +15-25 karma |
| Quora 回答（非 KES 话题） | 1-2h | 回答 1-2 个与卫浴无关的问题（建立资料权重） | 答案被采纳 1+ |
| 监听工具熟悉 | 1h | 每天看 Arctic Shift 推送的帖子，只观察不回复 | 能识别 3 个意图信号 |
| 知识库维护 | 1h | 把本周观察到的用户原话补充进 `pain-points.md` | 每周 +3-5 条 |

#### 热身阶段禁止事项

| 禁止 | 原因 |
|------|------|
| 提 KES 或任何产品 | 热身阶段核心是建立「这个人懂行」的声誉 |
| 在 24h 内发 2+ 条评论到同一个 subreddit | 看起来像机器人 |
| 用 AI 直接生成评论发出去 | 语气不对，容易被识破 |
| 回复任何包含「推荐一个品牌」的帖子 | 太早了，等热身完成 |

---

### Phase 2：有价值评论（Week 5-8）

#### 评论结构（必须遵循）

```
第一步（承认）：「我也遇到过类似情况，当时是 xxx 原因。」
              ↓
第二步（实质建议）：给出具体可操作的建议（50-100 字）
              ↓
第三步（标注局限）：「这个方案在你的情况是 xxx，如果是 yyy 可能不适用。」
              ↓
第四步（谨慎提产品 — 仅当匹配时）：「我最近在测试一个金属阀芯的方案，
                    如果你感兴趣我可以私信你测试数据。」
```

#### 每周时间分配

| 活动 | 每周时间 | 数量目标 | 测量标准 |
|------|----------|----------|----------|
| Reddit 有价值评论 | 4-5h | 8-12 条 | upvote 率 > 30% |
| Quora 回答（KES 相关话题） | 2-3h | 2-3 条 | 逐答案凭据设置正确 |
| AI 起草练习（不发出） | 1h | 3-5 条草稿 | 声音指南自检通过 |
| 知识库迭代 | 1h | 更新 2-3 条 | `pain-points.md` 增长到 15+ 条 |

#### 进入 Phase 3 的判断标准

| 条件 | 最低要求 |
|------|----------|
| Reddit 账号 karma | ≥ 100 |
| 有价值评论平均 upvote | ≥ 2 |
| 无人质疑营销意图 | 连续 20 条评论无「这是广告」回应 |
| Kenny 判断 | 「我觉得可以开始发帖了」|

---

### Phase 3：发帖测试（Week 9-12）

#### 发帖频率（保守起步）

| 周期 | Reddit 发帖 | Quora 回答 | Facebook（Egypt）|
|------|--------------|-------------|-----------------|
| Week 9 | 1 帖（经验分享类） | 2 回答 | 0（只观察）|
| Week 10 | 1 帖 + 观察反应 | 2 回答 | 0 |
| Week 11 | 2 帖（如果 Week 9-10 反应好） | 3 回答 | 1 个分享（安装案例）|
| Week 12 | 复盘 → 决定是否加速 | 复盘 | 复盘 |

#### 发帖内容原型（必须经过 Kenny 审核）

| 原型 | 适用平台 | 示例主题 | KES 提及位置 |
|------|------------|----------|----------------|
| 经验分享 | Reddit | 「我测试了 5 款阀芯，这是我的数据」 | 结尾一句：「我在做金属阀芯，有类似发现」|
| 犀利观点 | Reddit / Quora | 「为什么大多数花洒在 2 年内坏了？」 | 不提及（纯教育）|
| 求助式 | Reddit | 「我在设计 XX，你们觉得最烦的是什么？」 | 自我介绍里已有 |
| 数据分享 | Quora | 「我们测了 XXX，结果是…」 | 逐答案凭据 |
| 安装案例 | Facebook（Egypt）| before/after 照片 | 自然露出品牌 |

#### 发帖后监测清单

```
发帖后 2h：
  □ 有没有人回应？
  □ 有没有人质疑营销意图？

发帖后 24h：
  □ upvote/downvote 比例？
  □ 如果有负面回应 → 按负面回应手册处理
  □ 如果无人回应 → 分析：标题不行？版块不对？

发帖后 72h：
  □ 最终 score？
  □ 有没有有机提及（别人主动引用你的帖）？
  □ 记录到 `successful-replies.md` 或 `failed-replies.md`
```

---

### Phase 4：全面覆盖 + 迭代（Week 13+）

#### 扩大覆盖的三个维度

| 维度 | 做法 | 前提条件 |
|------|------|----------|
| **更多 subreddit** | 从 r/HomeImprovement 扩展到 r/Plumbing, r/BathroomRemodel | Phase 3 无负面事件 |
| **更多平台** | Reddit → Quora →（可选）Discord / Houzz | Quora 逐答案凭据设置完成 |
| **更多账号** | Kenny 账号 → 员工账号（产品经理/工程师） | 员工培训完成，声音指南理解一致 |

#### 员工账号培训流程（4 周）

```
Week 1：观察期
  - 只读负面回应手册 + 声音指南
  - 每天看 Kenny 的回复 2-3 条，写一句话评价
  - 不发送任何内容

Week 2：草拟期
  - 用 AI 起草流水线生成草稿
  - Kenny 修改，讲解修改原因
  - 不发送，只练习

Week 3：监督下发期
  - 员工发帖/回评，Kenny 预先审核每一句
  - 每天最多 2 条
  - 结束后复盘

Week 4：独立下发（谨慎）
  - Kenny 随机抽查 30%
  - 员工可独立发送，但重大决定（L2+ 负面）必须转 Kenny
  - 持续 4 周无事故 → 转正
```

---

## 第三部分：工具与责任人矩阵

### 工具链总览

| 环节 | 工具 | 用途 | 费用 |
|------|------|------|------|
| 帖子发现 | Arctic Shift API（免费） | 每日抓取相关新帖 | $0 |
| 帖子发现（宏观） | last30days skill | 每周分析趋势和痛点语言 | 免费额度 100 credits |
| 知识库 | KES wiki（本地 Markdown） | 存储所有产品知识 | $0 |
| AI 起草 | WorkBuddy（GPT-4o） | 根据知识和帖子生成草稿 | 已付费 |
| 账号管理 | Google Workspace（@keshome.com） | 统一注册 + 2FA | 已付费 |
| 定时运行 | 待定（cron / WorkBuddy 自动化） | 每日 3 次运行帖子发现 | $0 或低 |
| 数据分析 | 手动（每周复盘） | 测量框架指标 | $0 |

### 责任人矩阵（RACI）

| 活动 | Kenny | 未来社区经理 | 产品经理 | 工程师 |
|------|-------|----------|----------|--------|
| 战略决策 | **A** | C | I | I |
| 账号注册与安全 | **R** | A | C | C |
| 知识库内容提供 | **A** | C | **R** | **R** |
| 帖子发现系统维护 | **A** | R | C | C |
| Reddit 评论/发帖 | **R** | R（未来） | C | C |
| Quora 回答 | **R** | R（未来） | **R** | C |
| 负面回应处理（L0-L1） | A | **R** | C | C |
| 负面回应处理（L2-L4） | **R** | C | I | I |
| 每周复盘 | **R** | R（未来） | C | C |

> R=Responsible（执行者）, A=Accountable（最终责任人）, C=Consulted（被咨询）, I=Informed（被通知）

---

## 第四部分：决策检查点

### 每个 Phase 结束时的 Go/No-Go 决策

| 检查点 | Go 标准 | No-Go 动作 |
|----------|----------|------------|
| Phase 0 → 1 | 知识库骨架完成，`pain-points.md` 各 ≥ 5 条 | 补完知识库再开始 |
| Phase 1 → 2 | karma ≥ 50，无「广告」质疑 | 延长热身 2 周 |
| Phase 2 → 3 | 连续 20 条评论无负面，upvote 率 > 30% | 继续只评论，不急于发帖 |
| Phase 3 → 4 | 发帖无 Shadowban，无 L2+ 负面事件 | 降频，回到每周 1 帖 |
| Phase 4 扩员工 | 员工通过 4 周培训，Kenny 抽查满意率 > 80% | 不扩，先优化 Kenny 的流程 |

---

## 第五部分：风险登记册

| 风险 | 概率 | 影响 | 缓解措施 | 负责人 |
|------|------|------|----------|--------|
| Shadowban | 中 | 高 | 四阶段热身 + 避免 pattern | Kenny |
| 负面回应升级（L3） | 中 | 中 | 负面回应手册 + 不辩论 | Kenny |
| 员工账号违规 | 低 | 高 | 4 周培训 + 抽查审核 | Kenny |
| 知识库数据不足 | 高 | 中 | 标注缺失 + 诚实回复「我们还没测过」| 产品经理 |
| 竞品组织性攻击 | 低 | 高 | 记录 + Kenny 官方声明 | Kenny |
| 平台规则变更 | 中 | 中 | 每季度审查各平台 ToS | Kenny |

---

## 第六部分：第一个 90 天甘特图

```
活动                      | W1 | W2 | W3 | W4 | W5 | W6 | W7 | W8 | W9 | W10 | W11 | W12 |
---------------------------|----|----|----|----|----|----|----|----|----|-----|-----|-----|
知识库骨架                  |████|    |    |    |    |    |    |    |    |     |     |     |
账号注册 + 2FA             |████|    |    |    |    |    |    |    |    |     |     |     |
Arctic Shift 配置          |████|    |    |    |    |    |    |    |    |     |     |     |
热身：无品牌评论            |    |████|████|████|    |    |    |    |    |     |     |     |
监听 + 知识库积累           |    |████|████|████|    |    |    |    |    |     |     |     |
有价值评论（不提品牌）       |    |    |    |    |████|████|████|████|    |     |     |     |
发帖测试（每周 1-2）       |    |    |    |    |    |    |    |    |████|████ |████ |████ |
测量 + 复盘                |    |    |    |    |    |    |    | ████|    |     |     | ████|
决定是否扩大               |    |    |    |    |    |    |    |    |    |     |     | ████|
```

> ██ = 该活动在该周进行。W = Week。

---

## 附录：文档依赖关系图

```
KES 社区营销总作战图
│
├── 必须先读（入场前）
│   ├── 元原则（community-marketing-meta-principle.md）← 理解为什么
│   ├── 跨平台方法论（community-marketing-cross-platform-2026.md）← 理解每个平台
│   └── KES 落地方案（kes-community-marketing-implementation-2026.md）← 理解 KES 具体计划
│
├── 必须携带执行（每周参考）
│   ├── KES 声音指南（kes-community-voice-guide.md）← 每次发帖前对照
│   ├── 负面回应手册（kes-negative-response-handbook.md）← 遇到负面时查阅
│   └── AI 起草流水线设计（ai-draft-pipeline-design.md）← 使用 AI 辅助时参考
│
└── 基础设施（后台运行）
    ├── 帖子发现系统设计（reddit-post-discovery-system-design.md）← 技术实现参考
    ├── 产品知识库（wiki/products/kes-product-knowledge-base/）← 所有回复的实质内容来源
    └── 账号资产体系（在落地方案中）← 注册和 2FA 设置参考
```

---

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| v1.0 | 2026-06-07 | 初版：方法论体系总图 + 90 天执行计划 + RACI 矩阵 + 风险登记册 + 甘特图 |
