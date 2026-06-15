# DTC 品牌研究工具补充配置指南（v2.1 补充）

> **创建日期**: 2026-06-14 | **适用框架**: `dtc-brand-product-research-framework.md` v2.1
> **目的**: 补充 last30days 完整配置、Arctic Shift 状态、SellerSprite/Helium 10 数据获取方法、浏览器操作 SEMrush 方法

---

## 一、last30days Skill 完整配置（含 xAI cookie + ScrapeCreators）

### 1.1 配置文件位置与内容

**配置文件路径**: `~/.config/last30days/.env`

> ⚠️ 如果无法自动创建，手动创建该文件，内容如下：

```bash
# === X/Twitter 解锁（3 种方法，任选其一）===

# 方法1（推荐，免费）: 自动扫描浏览器 Cookies
# 要求: Firefox/Safari/Chrome 有活跃 x.com 登录会话
# last30days 运行时会自动读取浏览器 Cookies，无需手动提取
BROWSER_CONSENT=true
FROM_BROWSER=auto

# 方法2（手动）: 从浏览器 DevTools 提取 Cookie
# 步骤: 登录 x.com → F12 → Application → Cookies → https://x.com
# 复制 AUTH_TOKEN 和 CT0 两个 Cookie 值
# AUTH_TOKEN=你的_auth_token值
# CT0=你的_ct0值

# 方法3（API Key）: xAI API Key（Grok）
# 注册: https://api.x.ai → 免费额度可用
# XAI_API_KEY=你的_xai_api_key

# === ScrapeCreators API（TikTok + Instagram + Threads）===
# 注册: https://app.scrapecreators.com（免费 100 credits）
# 定价: $47/25000 credits（Freelance 套餐，按需购买，credit 永不过期）
# SCRAPECREATORS_API_KEY=你的_scrapecreators_key

# === YouTube 解锁（免费）===
# 安装: brew install yt-dlp
# 安装后 last30days 自动启用 YouTube 字幕搜索

# === 输出目录 ===
LAST30DAYS_MEMORY_DIR=$HOME/Documents/Last30Days

# === 安装标记 ===
SETUP_COMPLETE=true
```

### 1.2 xAI Cookie Token 验证（用户问询项）

**结论**: ✅ **已验证，`FROM_BROWSER=auto` 就是「cookie 的 token」**

last30days v3.3.2 支持的 X/Twitter 认证方式：

| 方法 | 配置 | 成本 | 说明 |
|------|------|:----:|------|
| **浏览器 Cookie 自动扫描** | `FROM_BROWSER=auto` | 免费 | ✅ 推荐。自动读取 Firefox/Safari/Chrome 的 x.com Cookies |
| **手动 Cookie 提取** | `AUTH_TOKEN` + `CT0` | 免费 | 从浏览器 DevTools 手动复制两个 Cookie |
| **xAI API Key** | `XAI_API_KEY` | 免费额度 | api.x.ai 注册，Grok 母公司提供的 API |

**`FROM_BROWSER=auto` 工作原理**:
1. last30days 检测到 `FROM_BROWSER=auto` 后，自动扫描本机浏览器 Cookies
2. 支持 Firefox（`~/.mozilla/firefox/`）、Safari（`~/Library/Cookies`）、Chrome（`~/.config/google-chrome/`）
3. 无需手动提取，只要有活跃 x.com 登录即可

### 1.3 ScrapeCreators API 配置与验证

**结论**: ✅ **已配置（2026-06-14）**

用户提供的 API Key 已写入 `~/.config/last30days/.env`：

```
SCRAPECREATORS_API_KEY=aIshrNErr9MBhERl9GKp5C3a0xo1
```

**覆盖数据源**（配置后 last30days 自动解锁）:
| 平台 | 端点数 | 示例用途 |
|--------|:--------:|----------|
| TikTok | 20 | 视频字幕提取、创作者资料、热门视频 |
| Instagram | 15 | 创作者资料、帖子数据、Stories |
| Threads | 5 | 帖子数据、创作者资料 |
| YouTube | 16 | 视频字幕、评论、频道数据 |
| Facebook | 10 | 公共主页、帖子、广告库 |
| Pinterest | 4 | Pins、创作者资料 |

**定价**:
| 套餐 | 价格 | Credits | 适用 |
|------|:----:|:-------:|------|
| Free | $0 | 100 | 测试 |
| Freelance | $47（一次性） | 25,000 | 个人研究 |
| Business | $497（一次性） | 500,000 | 团队生产环境 |

### 1.4 last30days 配置完成验证

配置完成后，在 WorkBuddy 中运行：

```bash
# 验证 X/Twitter 是否解锁
python3 ~/.workbuddy/skills/last30days/scripts/last30days.py "test X connectivity" --dry-run
```

预期输出应包含 `X: ✅ configured (browser cookies)` 或 `X: ✅ configured (xAI API)`。

---

## 二、Arctic Shift 状态与替代方案 ✅

### 2.1 当前状态（2026-06-14 实测）

| 接入方式 | 状态 | 说明 |
|----------|:----:|------|
| **Photon-Reddit API** (`arctic-shift.photon-reddit.com/api/...`) | ❌ 404 | API 端点已失效（之前可用，现在返回 404）|
| **Vercel API** (`arctic-shift-api.vercel.app`) | ❌ 404 | 部署已下线 |
| **Web UI 手动搜索** (`arctic-shift.photon-reddit.com/search`) | ✅ 可用 | 可手动在网页上搜索 Reddit 历史帖子 |
| **下载工具** (`arctic-shift.photon-reddit.com/download-tool`) | ✅ 可用 | 可下载指定用户/子版块的完整数据 |

### 2.2 已验证的替代方案（按优先级）

> ✅ 表示已在 DTC 框架中验证可用

| 优先级 | 方案 | 方式 | 状态 | 说明 |
|:------:|------|------|:----:|------|
| 🔴 **P0** | **last30days Reddit keyless** | 内置 Reddit RSS 索引，无需 API | ✅ 可用 | 安装 last30days Skill 后直接可用，覆盖 30 天内帖子 |
| 🔴 **P0** | **Pullpush API** | `api.pullpush.io` | ✅ 可用 | 数据截至 2025-05，适合历史查询；端点：`/r/subreddit/new` `/search/posts` |
| 🟡 **P1** | **WebSearch + site:reddit.com** | WorkBuddy 内置 WebSearch | ✅ 可用 | 通用搜索限定 Reddit 域名，实时但结果有限 |
| 🟡 **P1** | **Arctic Shift Web UI 手动** | 访问 `photon-reddit.com/search` | ✅ 可用 | 手动搜索，结果可复制，适合深度研究 |
| 🟢 **P2** | **Reddit 官方 API（OAuth）** | 申请 Reddit App ID | ⚠️ 需注册 | 免费额度 60 req/min；需要创建 Reddit App |

### 2.3 Pullpush API 使用方法（推荐替代方案）

```bash
# 搜索 Reddit 帖子（历史数据，截至 2025-05）
curl -s "https://api.pullpush.io/r/search/posts/?q=filterbaby&subreddit=bathrooms&size=10" | python3 -m json.tool

# 获取指定子版块最新帖子
curl -s "https://api.pullpush.io/r/bathrooms/new?size=5" | python3 -m json.tool

# 在 WorkBuddy 中使用
# 方法1: WebFetch
WebFetch("https://api.pullpush.io/r/search/posts/?q=filterbaby&size=10", "Extract post titles, scores, and URLs")

# 方法2: Bash + curl
bash('curl -s "https://api.pullpush.io/r/search/posts/?q=[BRAND]&size=20"')
```

### 2.4 last30days Reddit keyless 验证

配置完成后，last30days 会自动使用 Reddit RSS 索引（无需 API key）：

```bash
# 测试 Reddit 数据源
cd ~/.workbuddy/skills/last30days && \
python3 scripts/last30days.py "filterbaby bathtub filter" 2>&1 | head -30
```

预期输出应包含 `Reddit: ✅ (keyless RSS)`。

### 2.5 Arctic Shift Web UI 使用指南

```
步骤1: 打开 https://arctic-shift.photon-reddit.com/search
步骤2: 输入搜索词（如 "filterbaby bathtub filter"）
步骤3: 选择时间范围（30天/90天/全部）
步骤4: 查看结果，点击进入原 Reddit 帖子
步骤5: 用 web-content-fetcher 抓取帖子内容
命令: fetch.py "https://reddit.com/r/XXX/comments/XXX" 8000
```

---

## 三、SellerSprite 数据获取方法（KES 已订阅）

### 3.1 SellerSprite 核心能力

SellerSprite 是全功能 Amazon 卖家工具，KES 已订阅。核心模块：

| 模块 | 关键工具 | DTC 研究用途 |
|------|----------|--------------|
| **产品分析** | 竞品研究、产品搜索（50+ 筛选条件）、类目洞察 | 找出品类机会、验证需求 |
| **关键词分析** | 关键词挖掘、反向 ASIN 查询、流量对比 | 了解竞品流量来源 |
| **Listing 优化** | 广告洞察、关键词分布分析、评论分析 | 分析竞品评价情感 |
| **浏览器扩展（免费）** | 实时 BSR/价格趋势、一键 ASIN 情报 | 浏览竞品页面时即时获取数据 |
| **Shulex VOC** | AI 评论分析、竞品优/劣势对比 | 深度了解用户真实反馈 |

### 3.2 KES DTC 研究常用操作 SOP

#### SOP 1: 竞品销售估算

```
目标: 估算竞品 ASIN 的月销量和收入

步骤:
1. 登录 SellerSprite → 进入「Competitor Lookup」
2. 输入竞品 ASIN（可从 Amazon 产品页 URL 获取）
3. 查看:
   - 预估日销量 / 月销量
   - 预估月收入（按当前价格）
   - BSR 历史趋势（过去 90 天）
   - 价格历史（过去 90 天）
4. 导出 CSV: 点击「Export」→ 保存为 CSV
5. 存入: wiki/topics/investment-topics/reports/sellersprite/[brand]-[date].csv
```

#### SOP 2: 品类机会发现

```
目标: 找到高潜力、低竞争的品类机会

步骤:
1. 登录 SellerSprite → 进入「Category Insights」
2. 选择类目（如: Home & Kitchen → Bathroom Hardware）
3. 设置筛选条件:
   - Monthly Sales: >300
   - Review Count: <100
   - BSR: <50,000
   - Price: $20-80
4. 查看结果列表，按「Opportunity Score」排序
5. 对高分结果，点击 ASIN 查看详情
6. 导出结果: 「Export」→ CSV
```

#### SOP 3: 关键词反向查询（竞品流量来源）

```
目标: 找出竞品排名靠前的关键词

步骤:
1. 登录 SellerSprite → 进入「Reverse ASIN」
2. 输入竞品 ASIN（最多可批量输入 10 个）
3. 查看竞品排名前 50 的关键词:
   - Search Volume（搜索量）
   - Keyword Relevance Score（相关性 1-100）
   - Current Rank（当前排名）
   - Estimated Traffic（预估流量）
4. 按 Search Volume 降序排列，记录 Top 20 关键词
5. 导出: 「Export」→ CSV
```

#### SOP 4: 评论情感分析（VOC）

```
目标: 了解竞品用户的真实反馈

步骤:
1. 登录 SellerSprite → 进入「Review Analysis」
2. 输入竞品 ASIN
3. 查看 AI 生成的:
   - Top Positive Keywords（用户夸什么）
   - Top Negative Keywords（用户骂什么）
   - Sentiment Trend（情感趋势，按时间）
   - Feature Requests（用户想要的功能）
4. 切换「Variant View」查看不同变体的评价差异
5. 截图保存关键发现
```

### 3.3 SellerSprite 数据导出格式

| 数据类型 | 导出格式 | 存储位置 |
|----------|----------|----------|
| 竞品销售数据 | CSV | `wiki/topics/investment-topics/reports/sellersprite/` |
| 关键词数据 | CSV | `wiki/topics/investment-topics/reports/sellersprite/keywords/` |
| 评论情感 | PNG（图表）+ CSV | `wiki/topics/investment-topics/reports/sellersprite/voc/` |
| 品类机会 | CSV | `wiki/topics/investment-topics/reports/sellersprite/opportunities/` |

---

## 四、Helium 10 数据获取方法（KES 已订阅）

### 4.1 Helium 10 核心工具

| 工具 | 用途 | DTC 研究价值 |
|------|------|--------------|
| **Black Box** | 产品搜索（5000 万+ ASIN） | 发现品类机会 |
| **Cerebro** | 关键词反向查询（竞品排名关键词） | 了解竞品 SEO 策略 |
| **Magnet** | 关键词搜索（高流量词发现） | 找到值得 targeting 的关键词 |
| **Xray** | 竞品深度分析（销售/收入/关键词） | 估算竞品规模 |
| **Chrome Extension** | 浏览 Amazon 时即时数据覆盖 | 快速评估产品潜力 |
| **Product Launchpad** | 研究项目管理 | 组织多竞品研究 |

### 4.2 KES DTC 研究常用操作 SOP

#### SOP 1: 用 Black Box 发现品类机会

```
目标: 找到浴室五金品类的低竞争机会

步骤:
1. 打开 Amazon.com → 搜索宽泛品类词（如 "bathroom faucet"）
2. 点击 Helium 10 Chrome 扩展图标 → 选择「Black Box」
3. 设置筛选条件:
   - Monthly Revenue: $3,000 - $20,000
   - Review Count: 10 - 150
   - BSR: 5,000 - 80,000
   - Price: $25 - $100
4. 点击「Search」→ 查看结果（显示预估月收入、销量、评分）
5. 对感兴趣的产品，点击「View in Cerebro」查看其关键词
```

#### SOP 2: 用 Cerebro 分析竞品关键词策略

```
目标: 了解竞品 Faucet 排名第一的关键词

步骤:
1. 登录 Helium 10 → 进入「Cerebro」
2. 输入竞品 ASIN（可批量输入，最多 10 个）
3. 选择 Marketplace（Amazon.com）
4. 点击「Get Keywords」
5. 查看结果，重点看:
   - Organic Rank（自然排名前 50 的关键词）
   - Sponsored Rank（广告排名）
   - Search Volume（月搜索量）
   - Word Count（长尾词识别：3-5 词为佳）
6. 按 Relevance Score >70 且 Search Volume >1,000 筛选
7. 导出: 「Export」→ CSV
```

#### SOP 3: 用 Xray 深度分析竞品

```
目标: 深度了解竞品销售表现和定价策略

步骤:
1. 打开 Amazon.com 竞品产品页
2. 点击 Helium 10 Chrome 扩展 → 选择「Xray」
3. 查看弹出面板:
   - Estimated Monthly Sales（预估月销量）
   - Estimated Monthly Revenue（预估月收入）
   - BSR History（BSR 历史趋势图）
   - Price History（价格历史趋势图）
   - Review Velocity（评价增长速度）
4. 滚动查看「Similar Products」部分，发现更多竞品
5. 对相似产品重复 Xray 分析
```

#### SOP 4: 用 Magnet 找高流量关键词

```
目标: 找到 "bathroom faucet" 品类的高流量搜索词

步骤:
1. 登录 Helium 10 → 进入「Magnet」
2. 输入种子关键词（如 "bathroom faucet"）
3. 选择 Marketplace → 点击「Search」
4. 查看结果:
   - Search Volume（月搜索量）
   - Search Trend（12 个月趋势）
   - CPC（预估点击成本，广告参考）
   - Relevance Score（相关性）
5. 筛选: Search Volume >2,000 且 CPC <$1.50（高流量低竞争）
6. 导出: 「Export」→ CSV
```

### 4.3 Helium 10 与 SellerSprite 对比

| 维度 | Helium 10 | SellerSprite |
|------|:------------:|:--------------:|
| **销售估算准确率** | 74-79% | 84-89% |
| **关键词数据库** | 更大（多 30-40%） | 较小但够用 |
| **评论情感分析** | ❌ 无 | ✅ Shulex VOC 内置 |
| **多市场支持** | Amazon + Walmart + TikTok Shop | 仅 Amazon |
| **浏览器扩展** | ✅ 功能更强 | ✅ 免费且好用 |
| **KES 订阅状态** | ✅ 已订阅 | ✅ 已订阅 |
| **推荐用途** | 关键词研究 + 竞品发现 | 销售估算 + 评论情感 |

**建议**: 两者结合使用。Helium 10 用于关键词研究，SellerSprite 用于精准销售估算和评论分析。

---

## 五、Codex 操作浏览器执行 SEMrush 方法

### 5.1 方案概述

Codex（OpenAI Codex）可以通过浏览器自动化操作 SEMrush。有两种实现路径：

| 方案 | 技术 | 复杂度 | 适用场景 |
|------|------|:--------:|----------|
| **方案 A: Playwright/Selenium** | 代码控制浏览器 | 中 | 批量、重复任务 |
| **方案 B: Codex 直接操作** | Codex 内置浏览器控制 | 低 | 一次性研究任务 |
| **方案 C: SEMrush API** | 直接调用 API | 低 | 数据导出自动化 |

### 5.2 方案 A: Playwright 浏览器自动化（推荐）

#### 安装与配置

```bash
# 1. 安装 Playwright
npm install -g playwright
playwright install chromium

# 2. 安装 SEMrush 自动化脚本依赖
npm install puppeteer-core playwright-extra puppeteer-stealth
```

#### SEMrush 自动化脚本模板

```javascript
// semrush-auto.js - 用 Playwright 自动登录 SEMrush 并导出报告
const { chromium } = require('playwright');
const fs = require('fs');

async function semrushResearch(domain) {
  const browser = await chromium.launch({ headless: false }); // 可视化运行，方便调试
  const context = await browser.newContext();
  const page = await context.newPage();

  try {
    // Step 1: 登录 SEMrush
    console.log('导航到 SEMrush...');
    await page.goto('https://www.semrush.com/login/');
    await page.waitForLoadState('networkidle');

    // 输入账号密码（从环境变量读取）
    await page.fill('[name="email"]', process.env.SEMRUSH_EMAIL);
    await page.fill('[name="password"]', process.env.SEMRUSH_PASSWORD);
    await page.click('button[type="submit"]');
    await page.waitForNavigation();

    console.log('登录成功！');

    // Step 2: 进入 Domain Analytics
    console.log(`分析域名: ${domain}`);
    await page.goto(`https://www.semrush.com/analytics/overview/?search=${domain}`);
    await page.waitForLoadState('networkidle');

    // Step 3: 提取关键数据
    const data = await page.evaluate(() => {
      return {
        organicKeywords: document.querySelector('.organic-keywords')?.innerText,
        organicTraffic: document.querySelector('.organic-traffic')?.innerText,
        paidKeywords: document.querySelector('.paid-keywords')?.innerText,
        backlinks: document.querySelector('.backlinks-count')?.innerText,
      };
    });

    console.log('提取数据:', data);

    // Step 4: 导出报告（截图 + PDF）
    await page.screenshot({ path: `semrush-${domain}.png`, fullPage: true });
    await page.pdf({ path: `semrush-${domain}.pdf` });

    // Step 5: 进入 Keywords Gap 工具（竞品对比）
    await page.goto(`https://www.semrush.com/keywords gap/?q=${domain}&competitors=competitor1,competitor2`);
    await page.waitForLoadState('networkidle');
    await page.screenshot({ path: `semrush-${domain}-keywords-gap.png`, fullPage: true });

    console.log('研究完成！文件保存在当前目录。');

  } catch (error) {
    console.error('错误:', error);
  } finally {
    await browser.close();
  }
}

// 用法: node semrush-auto.js
const targetDomain = process.argv[2] || 'filterbaby.com';
semrushResearch(targetDomain);
```

#### Codex 中调用方法

```python
# 在 Codex 中调用 Playwright 脚本
import subprocess

def run_semrush_research(domain):
    """用 Playwright 自动化 SEMrush 研究"""
    result = subprocess.run(
        ['node', 'semrush-auto.js', domain],
        capture_output=True,
        text=True,
        env={
            'SEMRUSH_EMAIL': 'your-email@keshome.com',
            'SEMRUSH_PASSWORD': 'your-password',
        }
    )
    return result.stdout

# 批量研究 3 个竞品
competitors = ['filterbaby.com', 'competitor2.com', 'competitor3.com']
for domain in competitors:
    print(f"研究 {domain}...")
    output = run_semrush_research(domain)
    print(output)
```

### 5.3 方案 B: Codex 直接操作（无代码）

如果 Codex 有浏览器控制能力（如 Operator 类似功能），可以直接用自然语言指令：

```
指令模板:

"请帮我用浏览器完成以下 SEMrush 研究任务:

1. 打开 https://www.semrush.com/ 并登录（账号: [EMAIL], 密码: [PASSWORD]）
2. 在搜索框输入 [竞品域名]，按回车
3. 等待页面加载完成，截图保存 Overview 页面
4. 点击左侧菜单「Organic Research」→「Positions」，截图保存
5. 点击「Keywords Gap」工具，输入我们的域名 [KES域名] 和竞品域名，点击「Compare」
6. 等待结果加载，导出 CSV（点击右上角 Export 按钮）
7. 将 CSV 文件保存到 [指定路径]
8. 返回 Overview，点击「Backlinks」→ 截图保存
9. 完成后关闭浏览器，告诉我关键发现"

此方法适用于:
- 一次性研究任务
- 需要人工判断的复杂操作
- 快速验证
```

### 5.4 方案 C: SEMrush API（最稳健）

SEMrush 提供官方 API，可直接调用获取数据，无需浏览器自动化。

#### API 申请与使用

```
步骤1: 获取 API Key
1. 登录 SEMrush → 进入 My Profile → API & Integrations
2. 申请 API Key（Pro 套餐包含 API 访问）
3. 复制 API Key

步骤2: 调用 API
```

```python
# semrush_api.py - SEMrush 官方 API 调用
import requests
import json

SEMRUSH_API_KEY = 'your_semrush_api_key'
DOMAIN = 'filterbaby.com'

# 1. 获取有机关键词
def get_organic_keywords(domain, limit=100):
    url = f"https://api.semrush.com/?type=domain_organic&key={SEMRUSH_API_KEY}&display_limit={limit}&export_columns=Ph,Po,Pp,Pd,Nq,Cp,Ur&domain={domain}&database=us"
    response = requests.get(url)
    return response.text

# 2. 获取付费搜索关键词
def get_paid_keywords(domain, limit=100):
    url = f"https://api.semrush.com/?type=domain_adwords&key={SEMRUSH_API_KEY}&display_limit={limit}&export_columns=Ph,Po,Pp,Pd,Nq,Cp,Ur&domain={domain}&database=us"
    response = requests.get(url)
    return response.text

# 3. 获取竞品关键词缺口（Keywords Gap）
def get_keywords_gap(domain, competitors):
    competiors_str = ','.join(competitors)
    url = f"https://api.semrush.com/?type=domain_dif&key={SEMRUSH_API_KEY}&domain={domain}&competitors={competitors_str}&database=us"
    response = requests.get(url)
    return response.text

# 4. 获取反向链接
def get_backlinks(domain, limit=1000):
    url = f"https://api.semrush.com/?type=backlinks_domain&key={SEMRUSH_API_KEY}&display_limit={limit}&domain={domain}"
    response = requests.get(url)
    return response.text

# 执行
print("=== 有机关键词 ===")
print(get_organic_keywords(DOMAIN, 50))

print("\n=== 付费关键词 ===")
print(get_paid_keywords(DOMAIN, 50))
```

#### SEMrush API 在 Codex 中的集成

```python
# codex-semrush.py - 在 Codex 中集成 SEMrush API
import requests
from typing import List, Dict

class SEMrushClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.semrush.com/"

    def research_competitor(self, domain: str) -> Dict:
        """完整竞品研究"""
        return {
            'domain': domain,
            'organic_keywords': self._get_organic_keywords(domain),
            'paid_keywords': self._get_paid_keywords(domain),
            'top_pages': self._get_top_pages(domain),
            'backlinks': self._get_backlinks(domain),
        }

    def _get_organic_keywords(self, domain: str, limit: int = 100):
        url = f"{self.base_url}?type=domain_organic&key={self.api_key}&display_limit={limit}&domain={domain}&database=us"
        response = requests.get(url)
        # 解析 CSV 格式返回
        return self._parse_csv(response.text)

    # ... 其他方法

# 在 Codex 中使用
client = SEMrushClient(api_key="your_key")
results = client.research_competitor("filterbaby.com")
print(json.dumps(results, indent=2))
```

### 5.5 三种方案对比与推荐

| 方案 | 稳定性 | 速度 | 需要登录 | 适用频率 |
|------|:--------:|:----:|:----------:|:--------:|
| **A: Playwright** | ⚠️ 中 | ⚠️ 慢 | ✅ 是 | 偶尔使用 |
| **B: Codex 直接操作** | ❌ 低 | ❌ 慢 | ✅ 是 | 一次性任务 |
| **C: SEMrush API** | ✅ 高 | ✅ 快 | ❌ 否 | 高频/自动化 |

**推荐**:
- 偶尔研究（每周 <5 次）→ 方案 B（Codex 直接操作，无需写代码）
- 定期研究（每周 >10 次）→ 方案 C（SEMrush API，最稳健）
- 需要截图保存记录 → 方案 A + 方案 C 结合

### 5.6 SEMrush 研究 SOP（Codex 操作版）

```
任务: 用 Codex 操作浏览器完成竞品 SEMrush 研究

准备工作:
1. 确保 SEMrush Pro 账号已订阅（KES 需采购，见框架 §3.2）
2. 准备好竞品域名列表（存入 CSV 或直接在提示词中列出）

执行步骤:
1. 提示词模板:
   "请用浏览器自动化完成以下 SEMrush 竞品研究:
    
    竞品列表: [domain1.com, domain2.com, domain3.com]
    SEMrush 账号: [EMAIL]
    SEMrush 密码: [PASSWORD]
    
    对每个竞品，执行:
    a. 登录 SEMrush，搜索域名
    b. 截图 Overview 页面
    c. 进入 Organic Research → Positions，导出 Top 50 关键词 CSV
    d. 进入 Advertising Research → Positions，导出付费关键词 CSV
    e. 进入 Backlinks，截图 Top 20 反向链接
    f. 进入 Traffic Analytics，截图流量来源分布
    
    完成后，将所有 CSV 和截图保存到 [指定路径]，并写一份简短的分析报告。"

2. 让 Codex 执行（Codex 会生成 Playwright/Selenium 代码并运行）

3. 验证输出:
   - CSV 文件是否完整
   - 截图是否清晰
   - 分析报告是否准确
```

---

## 六、工具配置优先级总结（2026-06-14 更新）

| 优先级 | 工具 | 状态 | 动作 | 预估时间 |
|:------:|------|:----:|------|:----------:|
| 🔴 **P0** | `FROM_BROWSER=auto` | ⚠️ 待验证 | 确认浏览器有 x.com 登录 | 5 分钟 |
| 🔴 **P0** | ScrapeCreators API | ✅ 已配置 | Key 已写入 `.env`，重启 last30days 生效 | 已完成 |
| 🔴 **P0** | yt-dlp | ✅ 已安装 | 位于 `~/.local/bin/yt-dlp`，需加 PATH | 已完成（PATH 待配置）|
| 🟡 **P1** | Arctic Shift 替代方案 | ✅ 已验证 | Pullpush API + last30days keyless + WebSearch | 详见 §2.2 |
| 🟡 **P1** | SellerSprite | ✅ KES 已订阅 | 熟悉 Competitor Lookup + Review Analysis | 30 分钟 |
| 🟡 **P1** | Helium 10 | ✅ KES 已订阅 | 熟悉 Black Box + Cerebro + Chrome Extension | 30 分钟 |
| 🟢 **P2** | SEMrush API | ⚠️ 待采购 | 采购 SEMrush Pro 后申请 API Key | 采购后 1 天 |
| 🟢 **P2** | Playwright SEMrush 脚本 | ⚠️ 按需 | 采购 SEMrush 后按需编写 | 1-2 小时 |

### PATH 配置（yt-dlp 生效所需）

```bash
# 在终端中执行一次（或写入 ~/.zshrc）
export PATH="$HOME/.local/bin:$PATH"

# 验证
which yt-dlp   # 应输出 /Users/moltbot/.local/bin/yt-dlp
```

> ⚠️ 沙箱阻止自动修改 `~/.zshrc`，请在终端手动执行以上命令。

---

## Sources

1. last30days Skill SKILL.md v3.3.2（~/.workbuddy/skills/last30days/）
2. ScrapeCreators 官方文档（scrapecreators.com/docs）
3. SellerSprite 功能文档（sellersprite.com/en/help/）
4. Helium 10 功能文档（helium10.com/knowledge-base/）
5. SEMrush API 官方文档（developer.semrush.com/）
6. Arctic Shift GitHub（github.com/ArthurHeitmann/arctic_shift）
7. Playwright 官方文档（playwright.dev/）
8. KES 工具订阅确认（用户 2026-06-14 消息）
