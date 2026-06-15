---
type: protocol
status: draft
created: 2026-06-07
updated: 2026-06-07
domain: marketing-infrastructure
domains: [ai-draft-pipeline, community-marketing, kes]
confidence: high
verification_status: designed
related:
  - wiki/protocols/reddit-post-discovery-system-design.md
  - wiki/syntheses/kes-community-marketing-implementation-2026.md
  - wiki/principles/community-marketing-meta-principle.md
---

# KES 社区回复 AI 起草流水线设计

> 从「待回复帖子清单」到「可发送的回复草稿」，描述完整的信息流、知识库调用逻辑、人工审核节点。
> 本文档不含代码，只描述流程设计、输入输出规范、质量控制门禁。

---

## 流水线总览

```
输入：pending-replies.md（待回复帖子清单）
  │
  ↓
Step 1：帖子内容抓取
  └── 输入：帖子 URL
  └── 输出：结构化帖子内容（标题 + 正文 + 热门评论）
  │
  ↓
Step 2：知识库匹配
  └── 输入：帖子内容（语义）
  └── 输出：匹配的知识库条目（问题画像 → 答案 → 证据）
  │
  ↓
Step 3：AI 起草回复
  └── 输入：帖子内容 + 匹配知识库条目 + 回复结构模板
  └── 输出：回复草稿（Markdown）+ 置信度评分
  │
  ↓
Step 4：人工审核
  └── 输入：回复草稿
  └── 输出：修改后的最终回复 / 决定不回复
  │
  ↓
输出：最终回复文本（供复制到 Reddit/Quora/Discord）
```

---

## Step 1：帖子内容抓取

### 目的

将 Reddit/Quora/Discord 的帖子 URL 转化为**结构化文本**，供后续步骤使用。

### 输入

```
帖子 URL（来自 pending-replies.md）
例如：https://www.reddit.com/r/HomeImprovement/comments/abc123/...
```

### 输出格式（概念设计）

```yaml
# 文件：assistant-drafts/{post_id}.yaml（概念格式）

post:
  platform: reddit
  subreddit: HomeImprovement
  url: https://www.reddit.com/r/HomeImprovement/comments/abc123/...
  title: "推荐一个耐用不打滑的 bathroom faucet？"
  author: u/xxx
  created: 2026-06-07T03:51:00Z
  score: 15
  num_comments: 8

content:
  body: |
    我正在翻新主卧浴室，想换掉原来那个塑料阀芯的 faucet。
    用了三年就漏水，想问一下有没有推荐的全金属阀芯的牌子？
    预算大概 $100-150，DIY 安装。
  top_comments: |
    [u/aaa, 8pts] "Moen 的 Align 系列不错，但阀芯还是有点塑料"
    [u/bbb, 5pts] "全金属的很少，Grohe 有但很贵"
    [u/ccc, 3pts] "DIY 安装注意水管接口尺寸"

intent: active_recommendation   # 主动求推荐 / 描述问题 / 比较讨论
priority: high
matched_keywords: [faucet, valve, leak, DIY]
```

### 抓取方式（概念描述，不含代码）

| 平台 | 抓取方法 | 注意事项 |
|------|----------|----------|
| **Reddit** | 通过 Arctic Shift 的 `/api/posts/search` 用帖子 ID 获取全文；或直接访问 `https://www.reddit.com/{permalink}.json` | 无需登录，公开可访问 |
| **Quora** | 通过 `web_fetch` 或 ScrapeCreators API 获取回答页面 | Quora 有反爬，建议用 ScrapeCreators |
| **Discord** | 无法直接抓取历史消息；只能监控实时消息 | 不在本流水线范围内 |
| **Slack** | 同 Discord | 不在本流水线范围内 |

### 质量控制

```
抓取后检查清单：
  ✅ 帖子正文是否完整？（没有被截断）
  ✅ 热门评论是否包含（前 5 条，按得分排序）？
  ✅ 意图判断是否正确？（见 Step 2）
  ❌ 如果帖子已被删除 → 写入 ignored-posts.json，跳过
```

---

## Step 2：知识库匹配

### 目的

找到**知识库中最相关的条目**，作为 AI 起草的信息来源。

### 匹配逻辑（概念设计）

```
输入：帖子内容（标题 + 正文 + 热门评论）
  │
  ├── 方法 A：关键词匹配（快速，适合 80% 场景）
  │   └── 提取帖子关键词 → 匹配 knowledge-base/ 目录下的文件名和标签
  │
  ├── 方法 B：语义匹配（精确，适合复杂场景）
  │   └── 将帖子内容向量化 → 与知识库条目向量比对 → 取 top 3
  │
  └── 输出：匹配的知识库条目（1-3 条）
       格式：
       - knowledge-base/products/bathroom-hardware/pain-points.md
       - knowledge-base/products/bathroom-hardware/test-data/plastic-vs-metal-valve.md
       - knowledge-base/products/bathroom-hardware/competitor-comparisons.md
```

### 知识库条目调用规范

每份知识库条目有三种使用方式：

| 使用方式 | 说明 | 示例 |
|----------|------|------|
| **直接引用** | 将知识库内容原样作为回复的一部分 | 引用测试数据：「我们做了 xxx 小时盐雾测试，结果见下图」 |
| **改写后引用** | 将知识库内容改写为对话语气 | 将 `test-data/plastic-vs-metal-valve.md` 改写为「塑料阀芯在 xxx 情况下容易断裂…」 |
| **作为背景知识** | 不直接引用，但影响回复角度 | 读了 `competitor-comparisons.md` 后，知道要避开 Moen 的哪个弱点 |

### 匹配失败处理

```
if 没有匹配的知识库条目：
  → 标记为「需要人工撰写」
  → 同时将帖子问题记录到 knowledge-base/community-questions/ 目录
  → 触发知识库更新流程（见下方）
```

#### 知识库更新触发流程

```
帖子问题未覆盖 → 记录到 community-questions/{platform}-{topic}-qs.md
  ↓
  每周五下午（定时）
  ↓
  审查未覆盖问题清单
  ↓
  决定：
  ├── 如果是共性问题 → 写入 pain-points.md，补充 test-data/
  ├── 如果是竞品新问题 → 更新 competitor-comparisons.md
  └── 如果是一次性问题 → 仅记录在 community-questions/，不写入知识库
```

---

## Step 3：AI 起草回复

### 目的

用**帖子内容 + 匹配知识库条目**生成符合社区语气的回复草稿。

### 输入包设计（概念格式）

```yaml
# AI 输入包（传给 GPT-4o / Claude 的 prompt）

system_prompt: |
  你是 KES 的产品工程师（r/KennyMak_KES）。
  你的任务是在 Reddit 上帮助遇到卫浴五金问题的人。
  
  核心原则：
  1. 先帮人，后提产品（帮助优先）
  2. 用他们的语言，不是产品说明书语言
  3. 给出可验证的答案（有测试数据、对比图）
  4. 标注局限（诚实说什么情况下你的建议不适用）
  5. 产品提及必须是自然延伸（删掉产品部分，回复还有价值吗？）

platform: reddit
subreddit: HomeImprovement
tone: helpful, technical, humble   # 不是销售员

post:
  title: "推荐一个耐用不打滑的 bathroom faucet？"
  body: "我正在翻新主卧浴室..."
  top_comments: "..."

knowledge_base:
  - source: knowledge-base/products/bathroom-hardware/pain-points.md
    relevant_section: "塑料阀芯在低温下容易开裂"
    content: "..."
  - source: knowledge-base/products/bathroom-hardware/test-data/plastic-vs-metal-valve.md
    relevant_section: "盐雾测试 500 小时对比"
    content: "..."
  - source: knowledge-base/products/bathroom-hardware/competitor-comparisons.md
    relevant_section: "Grohe vs Moen vs KES 阀芯对比"
    content: "..."

response_structure:
  - step: 承认具体处境（1-2 句）
    instruction: 显示你读懂了他的帖子，不要套话
  - step: 给出实质建议（3-5 句）
    instruction: 直接有用的信息，引用 test-data/ 的具体数字
  - step: 标注局限（1 句）
    instruction: 诚实说什么情况下你的建议不适用
  - step: 自然提产品（0-1 句，可选）
    instruction: 仅当产品确实解决了他问的问题时才写

output_format: markdown
max_length: 300 words
```

### AI 输出格式

```markdown
<!-- 文件：assistant-drafts/{post_id}-draft.md -->

# 回复草稿：{post_title}

## 元信息

- **帖子 URL：** https://...
- **平台：** Reddit / r/HomeImprovement
- **意图：** 主动求推荐
- **匹配知识库：** pain-points.md, plastic-vs-metal-valve.md
- **置信度：** 高 / 中 / 低
- **建议发送时机：** 等 2 小时再发（刚发帖就回复容易被当 bot）

---

## 草稿正文

（以下是 AI 生成的回复草稿，Markdown 格式，可直接复制粘贴到 Reddit）

---

Thanks for the detailed post! Renovating a master bath is 
The plastic cartridge issue you mentioned is real. I've seen a lot of faucets where the cartridge cracks after 2-3 winters (thermal cycling). 

If you want all-metal, the key thing to check is whether the cartridge is brass or ceramic-disc (metal internals). Grohe and some of the higher-end Moen lines use ceramic discs, but they're usually $200+.

One thing you can do is look for NSF/ANSI 61 certication (low lead) + a written cycle-life test result (should be 500K+ cycles). Most brands that publish this data tend to be more transparent about their materials.

Happy to share more specific model recs if you share your rough-in size (4" centerset vs 8" widespread).

---

## AI 自检

- [ ] 删掉 KES 提及后，这条回复还有价值吗？ → 是 / 否
- [ ] 是否有可验证的数据支撑？ → 是（见 plastic-vs-metal-valve.md）/ 否
- [ ] 是否标注了局限？ → 是 / 否
- [ ] 语气是否像社区成员？ → 是 / 否

## 人工审核提示

- 如果置信度 = 低 → 建议完全重写
- 如果 `删掉 KES 提及后还有价值吗？` = 否 → AI 违反了帮助优先原则，必须修改
- 如果语气不像社区成员 → 修改第一人称，加入个人经验（"I had a similar issue with..."）
```

### 质量控制门禁

```
AI 草稿生成后，自动检查：

门禁 1：帮助优先检验
  → 运行：删掉所有 KES 提及，剩余内容 ≥ 50 字？
  → 如果不通过 → 标记「违反了帮助优先」，需要人工重写

门禁 2：数据可验证检验
  → 运行：回复中是否有「根据我们的测试...」类表述？
  → 如果有 → 检查 knowledge-base/ 中是否有对应 test-data/
  → 如果没有 → 标记「声称无数据支撑」，需要补充或删除声称

门禁 3：语气检验
  → 运行：是否包含「我们是最好的」「买我们的产品」类表述？
  → 如果有 → 标记「语气像销售员」，需要修改

如果任意门禁不通过 → 自动重新生成草稿（最多 2 次）
如果 3 次都不通过 → 标记为「需要人工撰写」
```

---

## Step 4：人工审核

### 目的

确保每条发出去的回复都符合 KES 社区营销标准。

### 审核界面设计（概念）

```markdown
<!-- 文件：assistant-drafts/{post_id}-review.md -->

# 人工审核：{post_title}

## 审核清单

### 必检项（任一项不通过 = 必须修改）

- [ ] **帮助优先**：删掉 KES 提及后，回复还有价值 → 是 / 否
- [ ] **数据准确**：引用的测试数据是否与 knowledge-base/ 一致 → 是 / 否
- [ ] **语气社区化**：是否像真实社区成员发的回复 → 是 / 否
- [ ] **标注局限**：是否说了「这个方法不适用于 xxx 情况」→ 是 / 否
- [ ] **FTC 合规**：是否披露了 KES 关联 → 是（个人简介已披露 ✓）/ 否（需在回复中加一句）

### 选检项

- [ ] 是否有趣或有用到值得保存到 knowledge-base/ → 是（保存到 xxx）/ 否
- [ ] 是否可能引发争议（竞品粉丝反驳）？ → 是（准备回应）/ 否

### 修改记录

| 修改位置 | 原文 | 修改后 | 原因 |
|---------|------|--------|------|
| 第 2 段 | "KES 的阀芯是全金属的" | "全金属阀芯在 thermal cycling 下更耐用（我们测试了 xxx 小时）" | 加入了可验证数据 |
| 结尾 | "可以看看 KES 的 XXX 系列" | "如果你想要具体型号推荐，我可以发几个（包括 KES 和非 KES 的）" | 降低了推销感 |

---

## 审核决策

- [ ] **通过** → 复制到 Reddit 发送 → 记录到 replied-posts.json
- [ ] **修改后通过** → 修改 → 重新审核
- [ ] **不回复** → 记录到 ignored-posts.json（原因：_______）
- [ ] **需要更多信息** → 暂时跳过，24 小时后再看（可能楼主补充了信息）
```

### 审核时间标准

| 优先级 | 审核时限 | 原因 |
|--------|----------|------|
| 高（主动求推荐） | 2 小时内 | 黄金窗口，越早回复越容易被看到 |
| 中（描述问题） | 6 小时内 | 仍然在活跃讨论期内 |
| 低（比较讨论） | 24 小时内 | 通常是旧帖复活，时间压力小 |

---

## 完整流水线时序图

```
t=0min      Arctic Shift 发现新帖
             ↓
t=5min      帖子内容抓取完成
             ↓
t=10min     知识库匹配完成
             ↓
t=15min     AI 起草草稿完成
             ↓
t=20min     自动质量门禁检查
             ↓
t=25min     【人工审核】开始
             ↓
t=35min     审核完成，修改后通过
             ↓
t=40min     在 Reddit 发送
             ↓
t=45min     记录到 replied-posts.json
             ↓
t=50min     如果回复得分 > 10 → 保存到 knowledge-base/（作为成功案例）
```

**总耗时：约 50 分钟（含人工审核 10 分钟）**

---

## 知识库反馈循环

### 成功案例保存

```
if 回复得分 > 10 (upvote)：
  → 保存到 knowledge-base/community-questions/{platform}-{topic}-successful-replies.md
  → 格式：
      ## 帖子：{title}
      - URL: https://...
      - 得分: 15
      - 回复摘要: "..."
      - 为什么成功: （人工标注）
      - 可复用的表述: （人工提取）

if 回复得分 < -5 (downvote)：
  → 保存到 knowledge-base/community-questions/{platform}-{topic}-failed-replies.md
  → 格式同上
  → 触发复盘：为什么失败？（语气？数据？ timing？）
```

### 知识库更新触发

```
每周五 15:00（定时）
  ↓
  审查本周的：
  ├── successful-replies.md（提炼可复用表述）
  ├── failed-replies.md（提炼避坑规则）
  └── community-questions/（未覆盖问题）
  ↓
  更新 knowledge-base/ 对应文件
```

---

## 多平台适配

### 回复模板差异

| 平台 | 语气 | 长度 | 格式 |
|------|------|------|------|
| **Reddit** | 对话式，略随意 | 150-300 词 | Markdown，无格式 |
| **Quora** | 专业，结构化 | 300-800 词 | 富文本，可加图片 |
| **Discord** | 非常随意，碎片化 | 50-150 词 | 纯文本，emoji 可接受 |
| **Slack** | 专业但友好 | 100-200 词 | Markdown |
| **Facebook** | 友好，本地化（Egypt 用阿拉伯语或阿拉伯语+英语） | 100-250 词 | 富文本 |

### 知识库调用差异

```
Reddit：调用 pain-points.md + test-data/（技术细节）
Quora：  调用 pain-points.md + competitor-comparisons.md（全面比较）
Discord：调用 pain-points.md（快速回答，不引用数据）
Slack：  调用 pain-points.md + installer-talk.md（专业角度）
Facebook：调用 pain-points-egypt.md（本地化痛点）
```

---

## 指标与迭代

### 流水线效率指标

| 指标 | 定义 | 目标 |
|------|------|------|
| 草稿通过率 | 人工审核「通过」的草稿数 / AI 生成草稿总数 | > 70% |
| 平均审核时间 | 人工审核耗时（分钟） | < 10 分钟 |
| 回复得分均值 | 发出回复的 upvote 均值 | > 3 |
| 知识库覆盖率 | 有匹配知识库条目的帖子数 / 总待回复帖子数 | > 80% |

### 迭代触发条件

```
if 草稿通过率 < 50% for 1 周：
  → 检查 AI prompt 是否过时
  → 更新 response_structure（可能社区语气变了）

if 平均审核时间 > 15 分钟：
  → 检查 AI 草稿质量（是否太多需要修改的地方？）
  → 考虑增加自动修改环节（AI 自检后自动修改）

if 知识库覆盖率 < 60%：
  → 触发知识库更新（见 Step 2 知识库更新触发流程）
  → 可能产品线发生了变化，但知识库没跟上
```

---

## 工具选择（概念建议）

| 环节 | 推荐工具 | 原因 |
|------|----------|------|
| 帖子内容抓取 | Arctic Shift API（Reddit）+ ScrapeCreators（Quora） | 免费/低成本，覆盖主流平台 |
| 知识库匹配 | GPT-4o embeddings + 简单向量数据库（如 Chroma） | 语义匹配准确 |
| AI 起草 | GPT-4o（成本优先）或 Claude 3.5 Sonnet（质量优先） | 前者便宜，后者语气更自然 |
| 人工审核界面 | 简单的 Web 页面（本地运行）或 Markdown 文件 + VS Code | 不需要复杂系统，Markdown 够用 |
| 状态管理 | JSON 文件（seen-posts.json / replied-posts.json） | 简单，git 跟踪 |

---

## 后续演进方向

| 阶段 | 能力 | 说明 |
|------|------|------|
| v1（当前设计） | 人工驱动，AI 辅助起草 | 人工审核每一条 |
| v2 | AI 自动修改 | AI 草稿不通过门禁后，自动修改（最多 2 次） |
| v3 | 多平台自动适配 | 同一帖子，自动生成 Reddit/Quora/Discord 三个版本 |
| v4 | 效果预测 | 根据历史数据，预测这条回复的得分（用机器学习） |
```