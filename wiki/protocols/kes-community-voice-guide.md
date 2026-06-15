---
type: protocol
status: draft
created: 2026-06-07
updated: 2026-06-07
domain: marketing-infrastructure
domains: [brand-voice, community-marketing, kes, copywriting]
confidence: high
verification_status: designed
sources:
  - /Users/moltbot/dev/kes-wiki/wiki/products/bathtub-filter/bathtub-filter-community-language-compression-patterns.md
  - /Users/moltbot/dev/kes-wiki/wiki/products/bathtub-filter/bathtub-filter-visual-merchandising-and-creative-strategy.md
  - /Users/moltbot/dev/kes-wiki/wiki/products/bathtub-filter/bathtub-filter-brand-operating-matrix-v2.md
related:
  - wiki/protocols/ai-draft-pipeline-design.md
  - wiki/protocols/reddit-post-discovery-system-design.md
  - wiki/principles/community-marketing-meta-principle.md
  - wiki/syntheses/kes-community-marketing-implementation-2026.md
---

# KES 社区声音指南

> 在 Reddit / Quora / Discord / 垂直论坛中，KES 应该怎么说话？
> 本指南定义社区回复的语气、风格、禁忌和可复用句式，来自 kes-wiki 品牌资料 + 社区营销方法论提炼。

---

## 设计原则

### 为什么需要「声音指南」而不是「品牌手册」

| 品牌手册（官网/广告） | 社区声音（Reddit/Quora） |
|----------------------|---------------------------|
| 精心打磨的 headline | 对话式的自然回答 |
| 预设的 slogan 和 tagline | 根据对方问题现组装的回答 |
| 「我们是最好的」叙事 | 「我遇到过类似问题」叙事 |
| 品牌主导 → 用户从属 | 用户主导 → 品牌响应 |
| 可以重复 | 每一句话必须独一无二 |

**核心矛盾：** 品牌手册告诉你怎么「说」，但社区里人们问的是「你能帮我吗」。声音指南告诉你怎么「回答」。

---

## 第一部分：KES 社区身份的「人格」

### 人格定义

| 维度 | 是什么 | 不是什么 |
|------|--------|----------|
| **角色** | 帮过朋友装修的同行 | 卖货的销售员 |
| **语气** | 技术自信但谦虚 | 傲慢、绝对化 |
| **知识** | 做过测试，知道数据 | 凭感觉、在猜测 |
| **边界** | 知道什么场景不适用 | 什么都行、包治百病 |
| **情绪** | 真诚关心对方的问题 | 急着完成 KPI |

### 一句话自画像

> 「我是 KES 的产品工程师。我做过测试、拆过产品、知道什么材质耐用、什么会坏。你有问题就问，我知道的告诉你；不知道的我不瞎说。」

### 检验标准（同帮助优先原则）

> **删掉所有关于 KES 的部分，这条回复还有价值吗？**

---

## 第二部分：6 个社区可用的「情感骨架」

> 来自 kes-wiki `bathtub-filter-community-language-compression-patterns.md`，
> 经改写适配为社区回复场景。

### 骨架 1：「我也有过这个困惑」（共鸣锚）

**适用场景：** 对方描述一个常见但令人沮丧的问题。

**句式骨架：**
```
"I had a similar issue with [问题]，and the thing that eventually
mattered was [关键洞察] —  not [常见的错误解法]."
```

**KES 示例（卫浴五金）：**
```
"I had a similar issue with a leaky faucet in my own bathroom.
The thing that eventually mattered was the cartridge material —
ceramic disc vs plastic internals makes a 10x difference in
cycle life. Not so much the brand name."
```

**❌ 不要写成：** "KES 的产品用全金属阀芯，一定不会漏" — 销售员语气。

---

### 骨架 2：「关键差别在这里」（知识锚）

**适用场景：** 对方在比较产品 / 选购 / 困惑时。

**句式骨架：**
```
"The key difference between [A] and [B] is actually [技术洞察] —
[A] will [具体效果]，while [B] will [另一种效果]。
For your use case ([引用对方说的使用场景])，[建议]."
```

**KES 示例（窗帘系统 Egypt）：**
```
"The key difference between PU-coated and PVC-coated roller blind
fabric is actually the UV tolerance. PVC starts degrading and flaking
at around 60°C sustained heat — which is very common in Egypt summers.
PU-coated fabric's UV-resistance rating is about 3x higher.
For your use case (direct sun on the window), I'd go with PU."
```

**❌ 不要写成：** "KES 用的是最好的 PU 涂层" — 没有解释为什么。

---

### 骨架 3：「不是我一个人说」（证据锚）

**适用场景：** 对方需要可信的数据支撑。

**句式骨架：**
```
"This is something we actually tested — [测试方法]，
using [测试条件]。The [指标] came out at [数字]。
Happy to share the full report if you want the details."
```

**KES 示例：**
```
"This is something we actually tested — salt spray corrosion
test per ASTM B117, using our brass valve vs a standard plastic
cartridge at 400 hours. The brass showed 0.2mm of surface
corrosion vs 1.8mm for the plastic. Happy to share the
test photos if you want to see."
```

**❌ 不要写成：** "我们的产品经过严格测试，质量很好" — 没有具体数据。

---

### 骨架 4：「但我不推荐你用…」（诚实锚）

**适用场景：** 对方的问题有多个解法，诚实标注哪种场景不适用。

**句式骨架：**
```
"One thing I should mention though — [方法 A] works well if [条件 1]，
but won't help much if [条件 2]。If [对方的情况匹配条件 2]，
you're probably better off [方法 B]."
```

**KES 示例：**
```
"One thing I should mention though — a brass valve faucet works
great if you're going for pure durability, but if your priority
is a really soft/smooth handle feel, ceramic disc might actually
feel better day to day. Different trade-off."
```

**❌ 不要写成：** 不标注局限 — 标注局限让社区觉得你不是在推销。

---

### 骨架 5：「实际成本是这样的」（价值锚）

**适用场景：** 对方在犹豫是否值得更换/升级。

**句式骨架：**
```
"If you use it [频率]，it [会持续多久] before you need to replace [耗材]。
Per-use cost works out to about [数字]。Compare that to [替代方案成本]，
and it's [结论]."
```

**KES 示例：**
```
"A decent metal-cartridge faucet will last 8-10 years in normal
use. If you pay $100 vs $60 for a plastic one, you're spending
about $10/year for the metal one vs replacing the plastic one
every 3 years ($20/year). Even strictly by the numbers, the
metal one comes out ahead."
```

---

### 骨架 6：「我是做这个的，说两句」（身份锚）

**适用场景：** 需要建立可信度时，在回答的开头自然提及。

**句式骨架：**
```
"I work in [product category] (disclosure: [品牌关联])，
so I see a lot of [同类产品]。Here's what I've learned..."
```

**KES 示例：**
```
"I work in bathroom hardware (disclosure: I'm at KES)，
and I've probably tested more faucet valves than I can count.
Here's what I've consistently seen..."
```

**❌ 不要写成：** 隐藏身份直到结尾才说 — FTC 要求透明披露。

---

## 第三部分：必须避开的 12 个词（社区版 blacklist）

> 来自 kes-wiki 的 12 词黑名单，用 `[general version]` 标记通用词，
> 用 `[KES-community]` 标记社区场景特别禁忌。

| 词 / 短语 | 为什么不能用 | 社区安全替代 |
|-----------|-------------|-------------|
| `best [anything]` | 触发社区反驳 + FTC substantiation | `designed to [function]` / `built specifically for [use case]` |
| `guaranteed` | 触发社区嘲笑 + 法律风险 | `in the tests we ran, [具体结果]` |
| `everyone should` | 社区讨厌被告诉做什么 | `one option is` / `here's what worked for me` |
| `you need to` | 同上 | `you might want to check` / `I'd suggest looking at` |
| `trust me` | 最差的信任建立方式 | 不替代 — 用数据说话 |
| `we're the only one who` | 几乎总是可被事实反驳 | `one thing we chose to do differently is [具体差异]` |
| `Amazon review says` | 社区不认可 review 作为权威来源 | 引用第三方测试数据 |
| `our competitors` | 不要说教竞品 | `other brands in this price range` / `similar products I've tested` |
| `revolutionary` | 社区 bs 探测器第一关 | `one approach that has worked well` |
| `game-changer` | 同上 | `has made a noticeable difference in our testing` |
| `safe for babies` | CPSIA 触发 + 社区认为你在打感情牌 | `designed with families in mind` / 不提及 baby |
| `scientifically proven` | FTC + 社区要求看论文 | `here's the test methodology we used: [描述]` |

**通用规则：** 社区里不要说「我们比别人好」，要说「我们在这个具体场景看到了这个具体结果」。让社区自己得出结论。

---

## 第四部分：回复结构的「好 vs 坏」对照

### 关于安装问题

| ❌ 坏 | ✅ 好 |
|------|------|
| "Our faucet is very easy to install, 10 minutes." | "Installation depends on your rough-in size. If it's standard 4-inch centerset, you should be able to swap it out in about 20 minutes with a basic wrench. The one thing that trips people up is the mounting nuts — make sure they're fully seated before tightening." |
| 问题：空洞声称，没有实质信息 | 具体、有细节、标注陷阱 |

### 关于耐久性

| ❌ 坏 | ✅ 好 |
|------|------|
| "KES faucets are very durable, we use the best materials." | "The thing that determines faucet durability isn't the brand — it's two things: (1) whether the internal cartridge is brass/ceramic vs plastic, and (2) the surface finish process. PVD is about 3x more scratch-resistant than electroplating. If you can find both at your budget, you're in good shape." |
| 问题：品牌吹嘘 | 教他怎么看，不是只推自己 |

### 关于价格

| ❌ 坏 | ✅ 好 |
|------|------|
| "We're more affordable than Grohe, check our Amazon page." | "A full-metal cartridge faucet usually runs $80-150. Below $50, you're very likely getting plastic internals (which isn't necessarily bad, just won't last as long). If you give me your budget range and rough-in type, I can point you to a few options — KES and non-KES." |
| 问题：直接的销售 CTA | 给选择空间，包含诚实提醒 |

### 关于竞品比较

| ❌ 坏 | ✅ 好 |
|------|------|
| "Moen uses plastic valves, KES uses metal. KES is better." | "Moen and KES take different approaches to valve design. Moen's Cartridge uses a plastic body with ceramic internals — which gives a very smooth handle feel. KES uses full brass — which gives better thermal cycling tolerance. It depends on whether smooth feel or long-term durability matters more to you." |
| 问题：片面贬低竞品 | 客观对比，让用户自己选 |

---

## 第五部分：平台适配

### Reddit

| 维度 | 规则 |
|------|------|
| **语气** | 对话式、略随意，可以自嘲 |
| **长度** | 150-300 词（太短 = 没内容，太长 = 不读了） |
| **格式** | 分段，用列表，不加任何格式花哨 |
| **身份** | KES 产品工程师 / KES 创始人（已在个人简介披露） |
| **CTA** | 无直接 CTA。如果对方有兴趣，他会问 |
| **回复时机** | 帖子发后 2-6 小时（太早 = bot，太晚 = 没人看了） |
| **要不要 DM** | 绝对不要。所有沟通在公开帖中进行 |
| **特别禁忌** | 不要用 `edit:` 标记修改，Reddit 用户会找 edit history 质疑你 |

### Quora

| 维度 | 规则 |
|------|------|
| **语气** | 专业但友好，结构化回答 |
| **长度** | 300-800 词（Quora 用户期待详细答案） |
| **格式** | 标题 + 小节 + 列表 + 总结 |
| **身份** | 「KES 创始人 · 10 年卫浴五金经验」（逐答案凭据） |
| **CTA** | 可加软 CTA：「了解更多 → KES 官网」 |
| **图片** | 可以加产品对比图 / 安装示意图（Quora 支持） |
| **特别禁忌** | 不要在 Quora 回答中插入 Amazon 链接 |

### Discord

| 维度 | 规则 |
|------|------|
| **语气** | 非常随意，朋友聊天方式 |
| **长度** | 50-150 词，碎片化 |
| **格式** | 纯文本，emoji 可接受 |
| **身份** | 个人真实身份 + KES 角色标签 |
| **CTA** | 无 |
| **特别禁忌** | 不要 unsolicited @everyone 或 DM |

### Facebook（Egypt 本地社区）

| 维度 | 规则 |
|------|------|
| **语言** | 阿拉伯语优先，粗糙英语可接受 |
| **语气** | 地面、邻里、朋友的朋友 |
| **长度** | 100-250 词 |
| **身份** | 「KES Egypt 项目负责 · 正在解决高温卷帘织物老化问题」 |
| **CTA** | 可提供 WhatsApp 号（Egypt 市场习惯） |
| **特别禁忌** | 不要用正式阿拉伯语（Fushā），用埃及口语（Masri） |

---

## 第六部分：常见场景回应速查

### 场景 1：对方问「有没有推荐的 XX 牌子」

```
回答策略：先教他怎么看，再给具体型号。

模板：
"I'd actually suggest looking for [X criteria] rather than
a specific brand — here's why: [解释]。For what you described,
a few models that meet that bar: [1-2 个，含 KES 和竞品]。"
```

### 场景 2：对方描述一个你产品能解决的问题

```
回答策略：先解决他的问题，产品提及自然出现在最后。

模板：
"This is a common issue with [某类产品/材质]。
The root cause is usually [原因]。Two things you can try:
1. [通用建议]
2. [通用建议]
One more thing — we've seen this exact failure mode in our lab,
so we [KE 做了什么事来解决]。But even if you don't go that
route, fixing [X] should help."
```

### 场景 3：有人在你的产品相关帖里说了负面看法

```
回答策略：承认 + 感谢 + 解释（如果合理）+ 不争辩。

模板：
"Fair point, and thanks for bringing it up.
You're right that [承认有效的部分]。
What we found in our testing was [解释角度] — but I completely
get why that might not match everyone's experience.
If you've run into this, I'd genuinely want to know more
about your specific setup so we can look into it."
```

### 场景 4：有人质疑「你是来推销的」

```
回答策略：直接承认 + 保持帮助姿态。

模板：
"I am (disclosure's in my profile). But I answered
here because I know this specific issue pretty well —
I've tested [X] versions of this thing and have seen
the same failure mode you're describing.
If the advice helps, great. If not, no worries."
```

---

## 第七部分：声音一致性自检清单

在发送每条回复前，逐项检查：

```
□ 删掉 KES 提及后，回复还有价值吗？
  → 如果否，重写。这是最重要的测试。

□ 有没有一个字来自 blacklist？
  → 如果有，替换为安全替代。

□ 语气是否像社区成员（不是销售员）？
  → 如果回复读起来像「我们可以、我们提供、联系我们」— 重写。

□ 有没有引用可验证的数据？
  → 如果没有，是否真的需要？（不是所有回复都需要数据）
  → 如果有，是否能在 knowledge-base/ 中找到对应 test-data？

□ 是否标注了局限？
  → 如果没有，加一句。社区信任来自诚实。

□ 是否透明披露了 KES 身份？
  → Reddit：个人简介已披露 ✓ / 回复中加了一句话 ✓
  → Quora：逐答案凭据已设置 ✓

□ FTC 合规
  → 身份披露 ✓
  → 数据声称有支撑 ✓
  → 无比较级 superlative ✓
  → 无 medical claim ✓
```

---

## 第八部分：新员工入职培训（声音部分）

### 培训流程（4 周）

```
Week 1：读本指南 + 阅读知识库
  - 读完 KES 社区声音指南
  - 读完 pertinent knowledge-base/ 条目
  - 读完 KES V1 视觉定位坐标
  - 每周考核：判断 10 条回复的合规性（好/坏）

Week 2：观察无声周
  - 不要发布任何评论
  - 每天阅读 target subreddit 新帖（30 分钟）
  - 找 5 条你认为值得回复的帖子
  - 在草稿本里写回复但不发 → 给经理审

Week 3：协助草拟（不发）
  - 用 AI 草稿 + 人工修改方式写回复
  - 所有草稿提交给经理审核
  - 学习回复结构（见第五部分）

Week 4：第一条回复（监督下发）
  - 在经理监督下发第一条回复
  - 发后 1 小时内不刷新（不要数 upvote）
  - 发后 24 小时进行回顾分析
```

### 新人的常见错误及预防

| 常见错误 | 为什么危险 | 预防 |
|----------|------------|------|
| 写完就直接发 | 没有自检 | 每周前 20 条回复必须完成声音自检清单 |
| 用「我们」太多 | 听起来像公司声明，不像个人 | 每段至少一次用「I」开头 |
| 夸得多但没数据 | 社区能识别空洞声称 | 如果要用「最好」类词，先检查是否有 test-data/ |
| 太急着提产品 | 信任还没建立 | 先给 2-3 条不提及 KES 的纯帮助回复 |
| 每一条都回复 | 看起来像 bot | 每天最多 5 条 |

---

## 第九部分：迭代机制

### 声音指南的更新触发条件

```
如果 月回复得分均值 < 2 for 连续 2 周：
  → 审查声音指南是否过时（社区语气可能变了）
  → 对比高分回复和低分回复的语气差异
  → 更新骨架 / blacklist

如果 单条回复得分 > 50（爆款）：
  → 将回复存入 knowledge-base/successful-replies.md
  → 分析：用了哪个骨架？哪个句式？为什么有效？
  → 提炼为新的可复用模板

如果 从社区收到「this reads like AI」类评论：
  → 立即停止 AI 起草，人工写 2 周
  → 审查 AI prompt → 调整 → 恢复
```

### 声音审计（每季度一次）

```
季度结束：
  ├── 随机抽取 30 条回复
  ├── 按声音自检清单打分（0-5）
  ├── 回顾所有负面回应
  └── 更新本指南
```

---

## 来源

- 6 个情感骨架：改编自 `kes-wiki/wiki/products/bathtub-filter/bathtub-filter-community-language-compression-patterns.md`（6 emotion arcs + 12-word blacklist）
- 3 个视觉世界：改编自 `kes-wiki/wiki/products/bathtub-filter/bathtub-filter-visual-merchandising-and-creative-strategy.md`（baby-safe / premium bath ritual / technical-clean-water credibility）
- 帮助优先原则：来自 `wiki/principles/community-marketing-meta-principle.md`
- 回复结构模板：来自 `wiki/syntheses/community-marketing-cross-platform-2026.md` + 各平台 topic 页
