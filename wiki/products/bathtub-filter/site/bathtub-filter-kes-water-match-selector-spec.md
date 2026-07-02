---
type: product
status: draft
owner: strategy
created: 2026-07-01
updated: 2026-07-01
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, selector, diagnosis, conversion, zip-lookup, referral, acquisition]
source_count: 8
review_cycle: monthly
verification_status: spot-checked
related:
  - ../bathtub-filter-kes-acquisition-engine-mvp-spec.md
  - ../bathtub-filter-utility-service-map-by-metro.md
  - ./bathtub-filter-kes-page-water-test-diagnosis.md
  - ./bathtub-filter-kes-edu-special-water-sources.md
  - ./bathtub-filter-kes-edu-water-softener-households.md
  - ./bathtub-filter-kes-scenario-free-chlorine.md
  - ./bathtub-filter-kes-scenario-chloramine.md
  - ./bathtub-filter-kes-scenario-well-water.md
  - ./bathtub-filter-kes-scenario-hard-water-scale.md
  - ./bathtub-filter-kes-scenario-sediment.md
  - ../bathtub-filter-claim-register.md
  - ./bathtub-filter-kes-marketing-site-content-map.md
---

# 选购器（Water-Match Selector）· 产品 spec

> 把「帮顾客选对版本」的交互工具本身当产品写成完整规格：交互流 + 数据 + 技术实现 + 护栏。
> **底稿关系**：[获客引擎 MVP spec](../bathtub-filter-kes-acquisition-engine-mvp-spec.md) 已把 ZIP 查表、数据模型、技术栈、构建顺序 spec 过——本页是它的**工具产品化超集**：MVP spec 定义「怎么 build 第一版」，本页定义「这个工具的完整交互分岔与升级路径」。凡 MVP spec 已定的，本页**引用不重复**。

---

## 一、这是什么

**选购器 = Hub「Find your water」区块的完整产品 spec。** 用户回答 1–3 个问题（水源 → 全屋系统 → ZIP 或症状），工具返回「你家的水属于哪一类 + KES 适不适合你 + 适合的话买哪套」。

它有**三重身份**，缺一不可：

| 身份 | 干什么 | 成功指标 |
|---|---|---|
| **① Conversion 工具** | 把已到站访客路由到对的场景页/SKU，一键加购 | 结果页→加购转化（MVP spec §6：>15%） |
| **② 诚实劝退门** | 氯胺 / RO / 全屋炭正常工作 / 高铁井水——**主动说「别买」**，把劝退变成邮箱资产 | 劝退分岔邮箱捕获率；零错卖差评 |
| **③ Referral 落地页** | `kes.com/t/{code}` 落地 = 同一个选购器 + 码上下文，朋友走同一诊断流 | referral 归因转化（MVP spec §6） |

> 设计原则沿 MVP spec §1.5：**极低摩擦、看结果不需注册、邮箱只在劝退/等待的价值时刻才要**；诊断只说「水的类型 / 产品适配」，禁健康恐吓。

---

## 二、交互流（完整分岔树，2026-07-01 定稿）

### 2.1 决策树总览

```
Q1 「你家水从哪来？」 Where does your water come from?
│
├─ A. 市政自来水 City / municipal tap water
│   │
│   └─ Q2 「装了全屋系统吗？」 Do you have a whole-house water system?
│       │
│       ├─ 没有 No ──────────────────────────────→ [ZIP 流]
│       │
│       ├─ 软水器 Water softener
│       │   └─ ✅ 提示「软水器不除氯」(链 E8) ──→ [ZIP 流]
│       │
│       ├─ 前置过滤 Sediment pre-filter
│       │   └─ ✅ 提示「前置管颗粒，氯还在」──→ [ZIP 流]
│       │
│       ├─ 全屋活性炭 Whole-house carbon
│       │   └─ ⚠️ 「先测再说」分岔 (链 E11 §六)
│       │       ├─ 试纸测不出氯 → 🔴 诚实劝退「别买」（可留邮箱要提醒）
│       │       └─ 试纸测出氯   → 炭床可能穿透提示 ──→ [ZIP 流]
│       │
│       └─ 整屋 RO Whole-house reverse osmosis
│           └─ 🔴 诚实劝退（RO 已去氯，链 E11 §一）
│
├─ B. 私人井水 Private well
│   │
│   └─ Q3 症状粗筛（多选）：铁锈色染渍 / 臭鸡蛋味 / 看得见沉积
│       ├─ 低中度 nuisance ─→ S3 井水场景页（⚠️ 井水版 GO 后才开此路由，见 2.5）
│       └─ 高铁 >2–3 ppm / 砷 / 细菌担忧 ─→ 🔴 劝退 + 建议专业检测（链 E2）
│
└─ C. 不确定 Not sure
    └─ 「怎么知道我家水」教育出口（链 E7 CCR / E5 试纸），不强推 ZIP

[ZIP 流] 输入 5 位 ZIP → 查表返回 {消毒剂类型, 硬度档, confidence}
│
├─ 游离氯 free_chlorine ─→ S1 推荐（推荐 SKU + 一键加购）
│   └─ 硬度 hard / very_hard → 附阻垢选项
│       （「It does not soften your water.」必随行）
│
├─ 氯胺 chloramine ─→ 🔴 诚实劝退 + 留邮箱（V1.5 候补，见 2.4）
│
└─ 未覆盖 / unknown ─→ 诚实 fallback：「查你的 CCR」(链 E7) + 试纸 (链 E5)
                        + 留邮箱（「覆盖到你的城市时告诉你」）

[referral 入口] kes.com/t/{code} 落地 = 同一选购器 + 码上下文
                 朋友首单减免在「适配分岔」（S1 推荐 / 加购）处挂出，
                 劝退分岔不挂折扣（不为奖励错卖）
```

### 2.2 每分岔的界面文案（EN）与路由

**Q1 — 水源**

> **"Where does your water come from?"**
> - `City / municipal tap water` → Q2
> - `Private well` → Q3 症状粗筛
> - `Not sure` → 教育出口

不确定出口文案：

> "No problem — here's how to find out in 2 minutes: check your city's annual water quality report (CCR), or test your tap with a strip."
> → 链 [E7 怎么读 CCR](./bathtub-filter-kes-edu-how-to-read-your-ccr.md) / [E5 怎么测洗澡水](./bathtub-filter-kes-edu-how-to-test-your-water.md)。搞清后可回来重走。**不收邮箱、不强推 ZIP**（用户还不知道自己是谁，问了也是噪音）。
>
> **软出口（2026-07-01 增补）**：同屏可展示 **B0 测试套装**（"Test first — we'll credit it back."，`[$9.99]` 购整机全额抵，见 [Bundle 页 §一A](./bathtub-filter-kes-bundles-and-multipacks.md)）。定位=**给想动手的人一条付费自助路**，不是强卖：教育链接在前、B0 在后，🔴 不做弹窗/拦截式推销。

**Q2 — 全屋系统（仅市政线）**

> **"Do you have a whole-house water system?"**
> - `No / just the regular pipes` → 直接 ZIP 流
> - `Water softener` → 过渡提示后进 ZIP 流：
>   "Good news: your softener handles hardness — but softeners don't remove chlorine. It passes straight through. Let's check what disinfectant your city uses."（链 [E8](./bathtub-filter-kes-edu-water-softener-households.md)）
> - `Sediment pre-filter` → 过渡提示后进 ZIP 流：
>   "Your pre-filter catches particles — but chlorine is dissolved, so it passes right through. Let's check your city's water."
> - `Whole-house carbon filter` → ⚠️「先测再说」分岔：
>   "Whole-house carbon removes chlorine — when it's working. Carbon beds wear out silently. **Test your tap with a chlorine strip first.**"
>   - `My strip shows no chlorine` → 🔴 劝退："Your carbon system is doing its job — **you don't need us.** If you'd like, leave your email and we'll remind you to re-test in a few months."（口径照 [E11 §6.3](./bathtub-filter-kes-edu-special-water-sources.md)：不说「全屋炭不可靠所以你需要我们」）
>   - `My strip shows chlorine` → "That usually means your carbon bed has broken through. The right fix is replacing the bed — a point-of-fill filter can cover the gap at the tub while you do." → ZIP 流
>   - `I don't have a strip` → 链 E5（怎么买/怎么测），留在流程外，不猜
> - `Whole-house reverse osmosis (RO)` → 🔴 劝退："RO already removes chlorine along with most dissolved solids. **KES likely has no value for you** — we'd rather tell you now than after you buy."（链 [E11 §一](./bathtub-filter-kes-edu-special-water-sources.md)）

**ZIP 流 — 结果分岔**

> **"Enter your ZIP — we'll look up your city's water."**

- `free_chlorine` 命中 → S1 推荐卡：
  > "Your city uses **free chlorine** — that's exactly what KES V1 is built for."
  > + 推荐 SKU + Add to cart（结果页规格沿 MVP spec §3.2，不重复）
  > 硬度 `hard/very_hard` 追加阻垢选项：
  > "Your area also has hard water. You can add the anti-scale option — it helps protect your tub and fixtures from scale buildup. **It does not soften your water.**"
  > 路由：[S1 游离氯](./bathtub-filter-kes-scenario-free-chlorine.md)（+硬水档链 [S4](./bathtub-filter-kes-scenario-hard-water-scale.md)）
- `chloramine` 命中 → 🔴 诚实劝退 + 候补：
  > "Your city uses **chloramine** — the current KES isn't built for your water yet. We won't sell you something that won't work. A chloramine version is in development — leave your email and we'll tell you when it ships."
  > 路由：[S2 氯胺](./bathtub-filter-kes-scenario-chloramine.md)（教育）。**注意**：氯胺产品线已 GO 但未 ship——文案只说 in development / when it ships，**不提前认领任何氯胺去除 claim**（register S2 行：未闭环不上首屏）。
- 未覆盖 / `unknown` → 诚实 fallback：
  > "We haven't mapped your city yet — and we won't guess. Two ways to find out yourself: check your city's water report (CCR), or test with a strip. Want us to email you when we cover your area?"
  > 链 [E7](./bathtub-filter-kes-edu-how-to-read-your-ccr.md) + [E5](./bathtub-filter-kes-edu-how-to-test-your-water.md)；邮箱 reason=`out_of_coverage`。**软出口**：同屏可展示 [B0 测试套装](./bathtub-filter-kes-bundles-and-multipacks.md)（"我们没数据、你可以自己测——买整机时全额抵回"），教育在前、B0 在后，🔴 不拦截式推销。埋点 `b0_offered` / `b0_purchased`。

**Q3 — 井水症状粗筛**

> **"Which of these do you see at home?"**（多选）
> - `Rust-colored stains on tub or fixtures`（铁）
> - `Rotten-egg smell`（H₂S）
> - `Visible particles / cloudy water`（沉积）
> - `None of these, just want better bath water`

- 低中度（症状勾选但无红旗）→ [S3 井水](./bathtub-filter-kes-scenario-well-water.md)：nuisance 舒适线推荐（KDF85 井水配置）。
- 红旗追问（任一命中即劝退）："Have you ever measured iron above 2–3 ppm, or do you have arsenic / bacteria concerns?"
  > "That's beyond what a compact point-of-fill filter can do. You need a professional water test and a dedicated system — here's what to look for."（链 [E2 井水必读](./bathtub-filter-kes-edu-well-water-basics.md)；邮箱可选，reason=`well_out_of_scope`）
- 症状全无 + 只想更好洗澡水 → 提示先做一次专业/邮寄检测再配（井水无 ZIP 权威源，见 §五）。

**Referral 入口**

- `kes.com/t/{code}` 落地 = **同一个选购器**，顶部加一行码上下文："{Friend's name} used this to figure out their water — check yours."
- 朋友首单减免**只在适配分岔**（S1 推荐卡 / 加购处）挂出："Your friend's link gives you $X off your starter."
- **劝退分岔不出现折扣**——氯胺/RO/全屋炭工作中的朋友照样被诚实劝退；referral 不改变诊断结论（防「为奖励错卖」）。
- 归因 cookie / 奖励兑付沿 MVP spec §3.3，不重复。

### 2.3 分岔 × 路由 × 出口速查表

| 分岔终点 | 路由 | 出口类型 | 邮箱 reason |
|---|---|---|---|
| 市政+游离氯 | S1（+S4 阻垢选项） | ✅ 加购 | — |
| 市政+氯胺 | S2 教育页 | 🔴 劝退+候补 | `chloramine_wait` |
| ZIP 未覆盖 | E7/E5 | 🟡 fallback | `out_of_coverage` |
| 整屋 RO | E11 | 🔴 劝退 | 可选 `ro_no_value`（不推销） |
| 全屋炭·测不出氯 | E11 §六 | 🔴 劝退 | 可选 `carbon_retest_reminder` |
| 全屋炭·测出氯 | ZIP 流→S1 | ✅（带换炭床提示） | — |
| 井水低中度 | S3 | ✅（井水版 GO 后） | GO 前 `well_waitlist` |
| 井水红旗 | E2 | 🔴 劝退+专业检测 | 可选 `well_out_of_scope` |
| 不确定 | E7/E5 | 🟡 教育 | 不收 |

### 2.4 氯胺分岔状态说明

氯胺产品线（催化炭 + 抗坏血酸钠浸泡件，V1.5）**已 GO 但未 ship**。选购器口径：

- 只说 "in development / we'll tell you when it ships"，**不认领**任何氯胺去除数字或时间承诺。
- ship 后此分岔从「劝退+候补」翻转为「S2 推荐」——**翻转是配置开关**（见 §四），不需要改树。
- waitlist 邮箱池 = V1.5 首发名单 + metro 扩张信号（MVP spec §3.1「劝退池=资产」）。

### 2.5 井水分岔状态说明

井水线（S3，KDF85 配置）在内容地图为 🟡 Conditional。选购器口径：

- **井水版 GO 前**：Q3 低中度分岔落到「教育 + waitlist」（链 E2/S3 页教育部分，邮箱 reason=`well_waitlist`），不出加购。
- **GO 后**：翻转为 S3 推荐 + 加购。同样是配置开关。

---

## 三、数据 spec

### 3.1 查表结构（沿 MVP spec §4，补 confidence）

```
zip_water_lookup:
  zip_prefix (PK)      # 3 位 ZIP 前缀为主；跨水系 metro 可下探 5 位
  disinfectant_type    # free_chlorine | chloramine | unknown
  hardness_band        # soft | moderate | hard | very_hard
  metro                # 展示用城市名（"Las Vegas, NV"）
  confidence           # high | medium | low   ← 本页新增
  serviceable          # bool（由 type 推导，冗余存储便于前端）
```

**confidence 字段定义与前端行为：**

| confidence | 含义 | 前端行为 |
|---|---|---|
| `high` | 该 metro 单一水务、CCR 核实过、近 12 个月内复核 | 正常出结果 + 标准精度句 |
| `medium` | 多水务 metro / 数据 >12 个月 / 过渡观察名单（如 LA 2027–2029 氯胺过渡，见 [水务图谱 §4 watch list](../bathtub-filter-utility-service-map-by-metro.md)） | 出结果 + 强化精度句："your area has more than one water utility — confirm with your CCR or the included strip" |
| `low` / 无记录 | 未核实 / 未覆盖 | **不出推荐**，走未覆盖 fallback（宁可 fallback 不猜错） |

**fallback 行为定义（写死）**：查不到、confidence=low、或 ZIP 格式错 → 一律走「未覆盖」分岔；**任何情况下不默认返回 free_chlorine**。

### 3.2 数据升级路径（三档，每档写维护成本与切换触发）

| 档 | 数据源与做法 | 覆盖 | 维护成本 | 切换到下一档的触发 |
|---|---|---|---|---|
| **① 静态表（MVP，现在）** | [水务图谱](../bathtub-filter-utility-service-map-by-metro.md) 人工整理 P1（拉斯维加斯/凤凰城/圣安东尼奥）+ P2（芝加哥/埃尔帕索）→ 静态 JSON；**人工季度维护**（对照 CCR 年报 + watch list 复核） | ~5 metro | 低：每季度约 0.5–1 人日；LA 类过渡城市需盯 watch list | `out_of_coverage` 邮箱量显示**需求 ZIP 数超过人工可维护量**（粗门槛：待覆盖 metro >15 个或月均未覆盖查询 >30%） |
| **② EPA SDWIS / CCR 半自动抓取** | 用 EPA SDWIS 公开数据 + 各水务 CCR 半自动抓取消毒剂类型与硬度基线，人工抽检后灌表；仍产出**同一张静态 JSON**（前端不变） | 全美主要 PWS | 中：一次性抓取管道开发（→工程，见 §六 待补）+ 每半年跑批 + 抽检；错误风险从「没覆盖」变「可能错」，**confidence 字段在此档开始真正干活** | 用户自报试纸读数量足够形成校准信号（粗门槛：月均自报 >500 条且与查表冲突率可统计） |
| **③ 用户自报试纸读数校准（远期）** | 已购客试纸读数（游离氯/总氯/硬度档）回流，聚合后校准查表、发现过渡中的水务 | 动态自修正 | 高：需防污染机制——**只收已购客读数、按 ZIP 聚合去极值、与 SDWIS 交叉验证、不让单点读数改表**；另有读数录入 UX 成本 | —（终态） |

> 三档共享同一 schema：升级只换「表怎么生成」，不换「前端怎么查」。这是 MVP spec §5「静态 JSON 查表」决定的红利，保持住。

### 3.3 stack_mapping / email_capture

沿 MVP spec §4 不重复；`email_capture.reason` 枚举扩展为本页 §2.3 表列出的全部值（原有 `out_of_coverage | chloramine_wait` + 新增 `ro_no_value | carbon_retest_reminder | well_waitlist | well_out_of_scope`）。

---

## 四、技术实现

- **MVP 形态**：纯前端表单 + 静态 JSON 查表，**无后端**（沿 MVP spec §5）。分岔树是纯客户端状态机；Q1/Q2/Q3 是静态选项，唯一「查询」是 ZIP → JSON。
- **挂载**：WooCommerce（主）/ Shopify（等价）挂法引 MVP spec §5 + §3.3，不重复。
- **分岔开关**：氯胺（§2.4）与井水（§2.5）的「劝退↔推荐」翻转做成 JSON 配置 flag（`chloramine_live: false`, `well_line_live: false`），ship 时改配置不改代码。
- **结果页**：模板化、可分享、带码（沿 MVP spec §3.2）；referral 落地的码上下文从 URL path（`/t/{code}`）读取，透传给 referral app 归因。
- **无注册墙**：所有结果（包括劝退结论）**不需注册即可看**；邮箱字段只在 §2.3 标注的分岔出现。

**埋点事件表**（GA4，命名与 MVP spec §6 对齐；MVP 的 `zip_diagnose`/`diagnose_result` 由下表 `zip_hit`/`zip_miss` 细化取代，其余沿用）：

| 事件 | 触发 | 关键参数 |
|---|---|---|
| `source_selected` | Q1 作答 | `source: municipal\|well\|unsure`；`referral_code`（如有） |
| `whole_house_selected` | Q2 作答 | `system: none\|softener\|prefilter\|carbon\|ro` |
| `zip_hit` | ZIP 查表命中 | `type, hardness, confidence, metro` |
| `zip_miss` | 查表未命中 / low confidence | `zip_prefix` |
| `disqualified_chloramine` | 氯胺劝退页展示 | `metro` |
| `disqualified_other` | RO / 全屋炭无氯 / 井水红旗劝退 | `reason: ro\|carbon_working\|well_flags` |
| `email_captured` | 任一分岔收到邮箱 | `reason`（§3.3 枚举） |
| `add_to_cart` | 结果页加购 | `sku[], source_tag: referral\|paid\|organic` |

> KPI 沿 MVP spec §6（诊断完成率 / 结果页→加购 / k-factor / referral CAC），本页新增关注：**各劝退分岔的邮箱捕获率**与**Q2 全屋炭分岔的「先测再说」跳出率**（衡量诚实门有没有把人吓跑 vs 建立信任）。

---

## 五、诚实护栏表

| # | 护栏 | 落在哪 |
|---|---|---|
| 1 | **精度句必带**（每个 ZIP 结果页脚注，EN 原文）："Based on your city's water utility data — one ZIP can span more than one water system. **Your included strip is the ground truth for your home.**" | ZIP 流全部命中分岔；confidence=medium 时强化版（§3.1） |
| 2 | 🔴 **禁 toxin-panic / 健康恐吓**：结果只说水的类型与产品适配，不说「你的水有毒/伤害皮肤/宝宝」（register Banned） | 全树所有文案，含劝退页与 referral 上下文条 |
| 3 | **每个劝退分岔 = 获客，🔴 无强卖**：氯胺→候补；RO/全屋炭工作中→「你不需要我们」+ 可选提醒邮箱；井水红旗→专业检测指引。劝退页**不出现任何加购 CTA** | §2.3 全部 🔴 行 |
| 4 | **阻垢≠软化**：阻垢选项出现处「It does not soften your water.」必随行；🔴 不做「软化版留邮箱」承诺（E11 §五：不暗示会有软化产品） | ZIP 流硬水档 |
| 5 | **氯胺不提前认领**：已 GO 未 ship，只说 in development；ship 前不写任何氯胺去除表述 | §2.4 |
| 6 | **类型判定以 ZIP/CCR 为准，试纸只作交叉验证**（T1 口径）；全屋炭分岔的试纸是「有没有氯」的存在性判断，不冒充浓度实验室 | Q2 炭分岔、精度句 |
| 7 | **看结果不需注册**；邮箱只在劝退/等待价值时刻，且说清楚给什么（候补通知/复测提醒/覆盖通知） | §2.3 邮箱列 |
| 8 | 🔴 禁 TDS 笔 / 铅试纸引导；井水不认领杀菌/除砷/硝酸盐（register Banned；E2/S3 口径） | Q3 分岔 |
| 9 | **referral 不改变诊断结论**：折扣只挂适配分岔，劝退照劝退 | §2.2 referral 入口 |

---

## 六、验收标准（照 MVP spec §9 扩展新分岔）

MVP spec §9 全部条目继续有效（P1 三城 ZIP 正确返回 / 氯胺劝退收邮箱 / referral 兑付 / GA4 事件 / 合规清单），新增：

- [ ] Q1 三选项均可达终点，无死胡同；「不确定」出口不收邮箱、不强推 ZIP。
- [ ] Q2 五个全屋系统选项各自路由正确：软水器/前置带过渡提示进 ZIP 流；全屋炭出现「先测再说」三分岔；RO 落劝退页且**无加购 CTA**。
- [ ] 全屋炭「测不出氯」分岔文案不含任何「再加一层更安心」式推销（对照 E11 §七护栏表）。
- [ ] ZIP 命中 confidence=medium 时展示强化精度句；low/未命中一律走 fallback，**任何路径不默认返回 free_chlorine**。
- [ ] 硬水档阻垢选项处「It does not soften your water.」逐字出现。
- [ ] 氯胺/井水分岔由配置 flag 控制翻转，改 flag 不需改树代码。
- [ ] 井水红旗（>2–3 ppm 铁/砷/菌）任一命中即劝退到 E2，不出推荐。
- [ ] `kes.com/t/{code}` 落地展示码上下文；折扣只在适配分岔出现；劝退分岔无折扣。
- [ ] §四 埋点事件全部可在 GA4 验证，`add_to_cart` 带 source 标签。
- [ ] §五 护栏表逐条走查通过（含每个劝退页无 toxin-panic、无强卖）。

**待补 `[____]`：**

- `[____]` P1/P2 之外 metro 的查表数据（下一批城市名单与 CCR 核实）→ **产品**（接水务图谱维护，§3.2 档①）
- `[____]` 井水症状粗筛的问题文案定稿（症状选项措辞、红旗追问阈值表述）→ **产品**
- `[____]` EPA SDWIS / CCR 半自动抓取方案（数据管道、抽检流程、confidence 赋值规则）→ **工程**（§3.2 档② 前置）
- `[____]` 氯胺/井水配置 flag 的翻转时点（跟随各自产品线 ship/GO 决议）→ **产品**
- `[____]` referral 落地码上下文条的最终文案与朋友折扣金额（接 MVP spec §11 奖励金额待定项）→ **产品+finance**

---

## Sources / 内部依据

- [获客引擎 MVP spec](../bathtub-filter-kes-acquisition-engine-mvp-spec.md)（底稿：ZIP 查表 §3.1、结果页 §3.2、referral §3.3、数据模型 §4、技术栈 §5、埋点 §6、验收 §9）
- [按 metro 水务图谱](../bathtub-filter-utility-service-map-by-metro.md)（ZIP→消毒剂/硬度数据源 + LA watch list）
- [T1 水质自测/诊断页](./bathtub-filter-kes-page-water-test-diagnosis.md)（ZIP=类型权威、试纸=粗筛交叉验证的诊断口径）
- [E11 特殊水源 §六](./bathtub-filter-kes-edu-special-water-sources.md)（全屋系统三分岔：软水器/前置/全屋炭 + RO 劝退口径）
- [E8 软水器家庭](./bathtub-filter-kes-edu-water-softener-households.md)（「软水器不除氯」口径）
- [S1](./bathtub-filter-kes-scenario-free-chlorine.md) / [S2](./bathtub-filter-kes-scenario-chloramine.md) / [S3](./bathtub-filter-kes-scenario-well-water.md) / [S4](./bathtub-filter-kes-scenario-hard-water-scale.md) / [S5](./bathtub-filter-kes-scenario-sediment.md)（路由目标场景页）
- [Claim register](../bathtub-filter-claim-register.md)（Self-diagnosis 精度行、诊断报告卡行、Banned：toxin-panic/TDS 笔/铅试纸/软化承诺）

## Obsidian links

- [[bathtub-filter-kes-acquisition-engine-mvp-spec]]
- [[bathtub-filter-utility-service-map-by-metro]]
- [[bathtub-filter-kes-page-water-test-diagnosis]]
- [[bathtub-filter-kes-edu-special-water-sources]]
- [[bathtub-filter-kes-edu-water-softener-households]]
- [[bathtub-filter-kes-edu-how-to-read-your-ccr]]
- [[bathtub-filter-kes-edu-how-to-test-your-water]]
- [[bathtub-filter-kes-edu-well-water-basics]]
- [[bathtub-filter-kes-scenario-free-chlorine]]
- [[bathtub-filter-kes-scenario-chloramine]]
- [[bathtub-filter-kes-scenario-well-water]]
- [[bathtub-filter-kes-scenario-hard-water-scale]]
- [[bathtub-filter-kes-scenario-sediment]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-kes-marketing-site-content-map]]
- [[bathtub-filter]]
