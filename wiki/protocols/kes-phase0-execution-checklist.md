---
type: protocol
status: active
created: 2026-06-07
domain: marketing-operations
tags:
  - community-marketing
  - phase0
  - execution
related:
  - wiki/syntheses/kes-community-marketing-master-plan-2026.md
  - wiki/syntheses/kes-community-marketing-implementation-2026.md
  - wiki/protocols/platform-registration-requirements-matrix.md
---

# KES 社区营销 Phase 0 执行清单

> **目标：** Week 0-1 完成基础设施搭建，为账号热身（Phase 1）做好准备。
> **使用方式：** 逐项勾选完成。每个子项标注了「需要 Kenny 操作」还是「AI 已准备」。

---

## 前置准备：需要 Kenny 确认/提供的素材

在开始注册之前，先确认以下素材：

| # | 素材 | 用途 | 状态 |
|---|------|------|:--:|
| 1 | Kenny 专业半身照 | Quora 头像（也可用于 Facebook/Houzz） | ⚠️ 需要 → 用手机在自然光下拍一张即可 |
| 2 | KES Logo（方形版本，≥ 400×400px） | 全平台头像（Reddit 品牌号 / Facebook Page / Discord） | ⚠️ 需确认是否有合适版本 |
| 3 | @keshome.com Google Workspace 2FA 确认 | 所有账号 TOTP 绑定 | ⚠️ 需确认已在 Google Admin 启用 |
| 4 | Google Admin 权限确认 | Kenny 需为超级管理员（确保可重置任何员工邮箱密码） | ⚠️ 需确认 |

---

## 第一部分：账号注册（Reddit × 2 + Quora × 1）

### 1.1 Reddit 主号（工程师身份）

| 步骤 | 操作 | 详情 |
|------|------|------|
| 1 | 打开注册页 | https://www.reddit.com/register/ |
| 2 | 邮箱 | `kenny@keshome.com` |
| 3 | 用户名 | 从以下选项中选择（见下方） |
| 4 | 密码 | 强密码（建议 16 位+，保存到 Google Workspace 密码管理器） |
| 5 | 注册后立即 → User Settings → 开启 2FA | 绑定 Google Workspace TOTP |
| 6 | 填写个人简介 | 见下方「预起草文案」 |
| 7 | 注册后至少 30 分钟不要发任何内容 | 避免被标记为新号 spam |

#### Reddit 主号用户名选项（Kenny 选择）

| 选项 | 用户名 | 风格 | 推荐 |
|------|--------|------|:--:|
| A | `u/KennyMak_KES` | 真名 + 品牌，透明直接 | ⭐ 推荐 |
| B | `u/KES_Kenny` | 品牌前 + 名，简洁 | |
| C | `u/BathroomHardware_Kenny` | 领域 + 名，SEO 友好但较长 | |

#### Reddit 主号个人简介（预起草）

```
KES 产品工程师 · 8 年卫浴五金 QC · 专注金属阀芯寿命测试
有问题关于花洒、水龙头、浴室五金的随时问
```

**设计说明：**
- 「产品工程师」而非「创始人」→ Reddit 对工程师身份接受度远高
- 「8 年 QC」→ 建立技术可信度（不是来卖货的）
- 「有问题随时问」→ 帮助优先的社区友好信号
- 不含链接 → 新号发链接易被判定 spam

---

### 1.2 Reddit 品牌号（备用 / 未来 subreddit 管理）

| 步骤 | 操作 | 详情 |
|------|------|------|
| 1 | 浏览器开隐身窗口（新网络环境） | **不同账号用不同网络环境，避免关联封禁** |
| 2 | 打开注册页 | https://www.reddit.com/register/ |
| 3 | 邮箱 | `admin@keshome.com` 或 `info@keshome.com`（需先在 Google Admin 创建） |
| 4 | 用户名 | 从以下选项中选择 |
| 5 | 密码 | 不同密码（不要与主号相同） |
| 6 | 2FA | 绑定 Google Workspace TOTP |
| 7 | 个人简介留空 | 品牌号先不填，等需要运营 r/KES 时再补充 |

#### Reddit 品牌号用户名选项

| 选项 | 用户名 | 风格 |
|------|--------|------|
| A | `u/KES_Official` | 官方标识 |
| B | `u/KESHome` | 品牌名简写 |
| C | `u/KES_plumbing` | 领域标识 |

#### ⚠️ Reddit 注册注意事项
- 主号和品牌号**不要在同一 IP / 同一浏览器 / 同一设备上注册**
- 建议：主号在公司电脑注册，品牌号用手机 4G 网络注册
- 注册后 30 分钟内不要发帖/评论
- 新号 7 天内不要加 subreddit 太多（每天 ≤ 3 个）

---

### 1.3 Quora 账号（创始人身份）

| 步骤 | 操作 | 详情 |
|------|------|------|
| 1 | 打开注册页 | https://www.quora.com/ （点击 Sign Up → Sign up with email） |
| 2 | 邮箱 | `kenny@keshome.com` |
| 3 | 姓名 | `Kenny M.`（First Name + 姓氏首字母） |
| 4 | 密码 | 强密码 |
| 5 | 上传头像 | Kenny 半身照 |
| 6 | 填写 Headline（头条） | 见下方预起草 |
| 7 | 填写个人简介 | 见下方预起草 |
| 8 | 设置 Credentials（凭据） | 见下方预起草 |

#### Quora Headline（预起草，选一个）

| 选项 | Headline | 风格 |
|------|----------|------|
| A | `Founder at KES · 10 years in bathroom hardware · Metal-first design advocate` | 创始人 + 专业 + 哲学 |
| B | `KES Founder & Product Engineer · Faucet valve testing · Bathroom hardware` | 创始人 + 技术 + 品类 |
| C | `Building better bathroom hardware at KES · Metal valves, no plastic shortcuts` | 行动 + 品牌 + 价值观 |

#### Quora 个人简介（预起草）

```
I run KES, a bathroom hardware brand focused on metal-first design — 
no plastic shortcuts where it matters. 

Before KES, I spent 8 years in QC for faucet and shower manufacturing, 
which taught me: most failures happen in the parts you can't see. 

I answer questions about choosing bathroom hardware, what to look for 
in materials and finishes, and how to avoid common product failures. 
Ask me anything.

Not financial or health advice. My answers reflect my own engineering 
experience and may include context about KES products where relevant.
```

#### Quora Credentials（逐答案凭据，预起草 2 套）

**凭据 A（技术类问题——阀芯、材料、测试）：**
```
CES Product Engineer · Valve life testing & materials QC
```

**凭据 B（品牌比较 / 选购类问题——best faucet, worth it?）：**
```
Founder, KES · 10 years in bathroom hardware manufacturing
```

#### ⚠️ Quora 注意事项
- Quora 有「真名政策」，`Kenny M.` 比单独的 `Kenny` 安全
- 注册后先关注「Bathroom Hardware」「Faucets」「Home Improvement」等话题
- 前 2 周只浏览 + upvote，不回答问题
- 回答第一条问题时应选择非 KES 相关话题（展示独立知识）

---

## 第二部分：2FA 与资产安全（关键）

### 统一 2FA 设置

| 平台 | 2FA 方式 | 绑定目标 | 操作 |
|------|----------|----------|------|
| Reddit 主号 | TOTP | Google Workspace Authenticator | User Settings → Safety & Privacy → Two-factor authentication |
| Reddit 品牌号 | TOTP | Google Workspace Authenticator | 同上 |
| Quora | 邮箱验证（Quora 不提供 TOTP 2FA） | `kenny@keshome.com` | Settings → Security |

### 密码管理

- 所有密码存入 Google Workspace 密码管理器（或 1Password/Bitwarden）
- 不要重复使用密码
- 记录到 `KES-账号注册信息表`（见附录，仅 Kenny + 关键人可见）

### 资产收回演练

完成注册后，做一次「收回测试」：
1. 在 Google Admin 重置 `kenny@keshome.com` 密码
2. 在 Reddit 点击「Forgot password」
3. 确认重置邮件到达 `kenny@keshome.com`
4. 确认可以重新登录
5. 将密码改回 → 确认

> 这个测试证明：离职员工即使改了 Reddit 密码，你也可以通过邮箱收回。

---

## 第三部分：产品知识库（AI 已创建骨架，Kenny 审核 + 补充）

### 已创建的文件结构

```
wiki/products/kes-product-knowledge-base/
├── products/
│   ├── bathroom-hardware/
│   │   ├── meta-principle.md          ✅ 已起草
│   │   ├── pain-points.md             ✅ 已起草（5 条痛点）
│   │   ├── competitor-comparisons.md  ✅ 已起草（3 个对比维度）
│   │   ├── test-data/
│   │   │   └── _README.md             ✅ 模板 + 补测计划
│   │   └── installation/
│   │       ├── DIY-guides.md          ✅ 已起草
│   │       └── plumber-talk.md        ✅ 已起草
│   └── curtain-roller-blind-egypt/
│       ├── meta-principle.md          ✅ 已起草
│       ├── pain-points-egypt.md       ✅ 已起草（5 条痛点）
│       ├── competitor-gap.md          ✅ 已起草
│       ├── test-data/
│       │   └── _README.md             ✅ 模板 + 补测计划
│       └── installer-talk.md          ✅ 已起草
├── community-questions/
│   ├── reddit-bathroom-hardware-qs.md ✅ 空模板
│   ├── reddit-egypt-curtain-qs.md     ✅ 空模板
│   └── quora-bathroom-hardware-qs.md  ✅ 空模板
└── assets/
    └── README.md                      ✅ 资产清单
```

### Kenny 审核清单

| 文件 | 审核要点 | 状态 |
|------|----------|:--:|
| `bathroom-hardware/meta-principle.md` | 品牌主张是否准确？「金属优先，无塑料捷径」是否过度承诺？ | ⚠️ 需审核 |
| `bathroom-hardware/pain-points.md` | 5 条痛点是否真实？用户原话模拟是否贴近实际？ | ⚠️ 需审核 |
| `bathroom-hardware/competitor-comparisons.md` | GROHE/Moen/Delta 的数据是否准确？ | ⚠️ 需审核 |
| `curtain-roller-blind-egypt/meta-principle.md` | 埃及策略是否准确？当前阶段描述是否正确？ | ⚠️ 需审核 |
| `curtain-roller-blind-egypt/pain-points-egypt.md` | 5 条痛点是否覆盖埃及市场真实情况？ | ⚠️ 需审核 |
| `curtain-roller-blind-egypt/competitor-gap.md` | 本地竞品描述是否准确？价格区间是否正确？ | ⚠️ 需审核 |
| 所有文件 | 是否触碰了禁用语（如「最好」「第一」「临床验证」）？ | ⚠️ 需审核 |

---

## 第四部分：其他 Phase 0 交付物

### 4.1 Arctic Shift 监控脚本

> ⚠️ 需要 Kenny 或技术同事操作。协议文档已有详细设计（见 `reddit-post-discovery-system-design.md`）。

**操作步骤（简版）：**
1. 确认 Arctic Shift API 端点可访问
2. 创建搜索配置（已定义 3 组关键词）：
   - 卫浴五金：`faucet OR shower head OR bathroom hardware OR valve`
   - 埃及窗帘：`roller blind OR curtain OR window shade egypt`
   - 水管工：`plumbing DIY OR leak fix OR water pressure`
3. 跑一次 → 输出 → 检查结果质量
4. 配置自动化（cron / WorkBuddy automation）每日 3 次运行

> 当前可不做代码实现，先确认 API 可用性。

### 4.2 文档阅读确认

**Kenny + 未来社区经理需阅读并理解：**

| 文档 | 路径 | 状态 |
|------|------|:--:|
| 负面回应处理手册 | `wiki/protocols/kes-negative-response-handbook.md` | ⚠️ 需阅读 |
| KES 社区声音指南 | `wiki/protocols/kes-community-voice-guide.md` | ⚠️ 需阅读 |
| 平台注册需求矩阵 | `wiki/protocols/platform-registration-requirements-matrix.md` | ⚠️ 需阅读 |
| AI 起草流水线设计 | `wiki/protocols/ai-draft-pipeline-design.md` | ⚠️ 可选（使用 AI 辅助时再读） |

---

## 第五部分：Phase 0 Go / No-Go 检查

Phase 0 完成标准（全部 ✅ 才能进入 Phase 1）：

| # | 条件 | 标准 |
|---|------|------|
| 1 | Reddit 主号已注册 | 用 @keshome.com 注册 + 2FA 绑定 Google Workspace |
| 2 | Reddit 品牌号已注册 | 用 @keshome.com 注册 + 独立 IP 注册 |
| 3 | Quora 账号已注册 | 用 @keshome.com 注册 + 头像 + 头条 + Credentials 设置 |
| 4 | 邮箱收回测试通过 | 能通过 @keshome.com 重置 Reddit 密码 |
| 5 | 知识库骨架审核通过 | Kenny 审核 + 修改所有 pain-points（每产品线 ≥ 5 条） |
| 6 | Arctic Shift API 可访问 | 能成功请求一次 |
| 7 | 负面回应手册已阅读 | Kenny 确认已读 |
| 8 | 声音指南已阅读 | Kenny 确认已读 |

---

## 附录 A：KES 账号注册信息表（模板）

> ⚠️ **机密信息——仅 Kenny + 授权人员可见。** 不要提交到 Git。

```markdown
| 平台 | 用户名 | 注册邮箱 | 注册日期 | 2FA 方式 | 密码位置 | 备注 |
|------|--------|----------|----------|----------|----------|------|
| Reddit 主号 | u/xxx | kenny@keshome.com | YYYY-MM-DD | Google WS TOTP | 密码管理器 | 工程师身份 |
| Reddit 品牌号 | u/xxx | admin@keshome.com | YYYY-MM-DD | Google WS TOTP | 密码管理器 | 备用+品牌号 |
| Quora | Kenny M. | kenny@keshome.com | YYYY-MM-DD | 邮箱验证 | 密码管理器 | 创始人身份 |
```

**建议存储位置：** Google Workspace 加密文档 或 1Password Shared Vault。

---

## 附录 B：预起草文案汇总（复制即用）

### Reddit 主号简介
```
KES 产品工程师 · 8 年卫浴五金 QC · 专注金属阀芯寿命测试
有问题关于花洒、水龙头、浴室五金的随时问
```

### Quora Headline
```
Founder at KES · 10 years in bathroom hardware · Metal-first design advocate
```

### Quora 个人简介
```
I run KES, a bathroom hardware brand focused on metal-first design — 
no plastic shortcuts where it matters. 

Before KES, I spent 8 years in QC for faucet and shower manufacturing, 
which taught me: most failures happen in the parts you can't see. 

I answer questions about choosing bathroom hardware, what to look for 
in materials and finishes, and how to avoid common product failures. 
Ask me anything.

Not financial or health advice. My answers reflect my own engineering 
experience and may include context about KES products where relevant.
```

### Quora Credentials A（技术问题）
```
CES Product Engineer · Valve life testing & materials QC
```

### Quora Credentials B（品牌比较）
```
Founder, KES · 10 years in bathroom hardware manufacturing
```

---

## 下一步

Phase 0 完成后 → Phase 1：账号热身（Week 2-4）
- Reddit：无品牌评论积累 karma（目标 100+）
- Quora：回答非 KES 话题建立资料权重
- 监听工具：每天看 Arctic Shift 推送，只观察
- 知识库：持续补充用户原话到 pain-points

---

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| v1.0 | 2026-06-07 | Phase 0 执行清单初版：账号注册步骤、预起草文案、知识库审核清单、Go/No-Go 标准 |
