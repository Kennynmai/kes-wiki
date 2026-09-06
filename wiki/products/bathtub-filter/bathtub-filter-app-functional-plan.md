---
type: product
status: draft
owner: product
created: 2026-09-06
updated: 2026-09-06
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, app, pwa, subscription, test-strip, colorimetry, acquisition, chloramine, data]
aliases: [App 规划, 小程序, PWA, app functional plan, 试纸相机]
name_zh: 浴缸过滤器 App 功能规划
name_en: Bathtub Filter App Functional Plan
source_count: 5
review_cycle: monthly
verification_status: working
related:
  - ./bathtub-filter-sensing-strategy.md
  - ./bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md
  - ./bathtub-filter-kes-v1-pricing-channel-launch-geo-subscription.md
  - ./bathtub-filter-chloramine-media-research.md
  - ./bathtub-filter-claim-register.md
  - ./bathtub-filter-decision-register.md
---

# KES Bathtub Filter · App 功能规划

> **一句话**：App 的工作不是给用户看仪表盘，是**采集带标签数据 + 把补货时点算对**。
> **核心纪律**：**App 是可选增强，不是产品依赖**——所有关键价值在零 App 使用下必须成立。

> 📐 本页的功能边界由 [感知策略](./bathtub-filter-sensing-strategy.md) 决定。**先读那页再读本页**——不了解"为什么不能做实时水质"，会把这个 App 做成错的那个。

---

## 一、五条设计原则（每条都从约束推导，不是偏好）

| # | 原则 | 推导自 |
|---|---|---|
| 1 | **零 App 也成立** | 2562 条评论仅 29 条用过工具（[客户测试方法](./bathtub-filter-customer-water-quality-test-methods-2026-06-03.md)）→ 品类不测量，不能把核心价值押在使用率上 |
| 2 | **不做实时水质** | 出水判别带 0.1 mg/L，低于消费级分辨率（[感知策略 §2](./bathtub-filter-sensing-strategy.md)） |
| 3 | **不黑箱** | 品牌内核是「透明 / 自己测 / 看得见」；黑箱倒计时正是我们批对手的东西（[获客引擎 §五](./bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md)） |
| 4 | **不配网** | 浴室 2.4G WiFi 配网是智能家居退货率高发项；$69 配件不值这个支持成本 |
| 5 | **App 是 claim surface** | 屏幕上的每句话与包装同级，受 [claim-register](./bathtub-filter-claim-register.md) 管辖 |

---

## 二、架构判断：Web PWA 优先，原生只为 BLE 存在

> **建议：MVP 不做原生 App。**

| 维度 | Web PWA | 原生 App |
|---|---|---|
| 下载摩擦 | **无** —— 与诊断漏斗同域同链路 | 高，购前必死 |
| 相机读试纸 | ✅ `getUserMedia` 可行 | ✅ |
| 与 Shopify DTC 集成 | **原生同栈**（主战场在 DTC，见[渠道页](./bathtub-filter-kes-v1-pricing-channel-launch-geo-subscription.md)） | 需另接 |
| BLE | ❌ Web Bluetooth iOS Safari 不支持 | ✅ **唯一理由** |
| 推送 | ⚠️ iOS PWA 受限 → **改用邮件/短信** | ✅ |

**结论：Web PWA 覆盖 95% 功能与 100% 客户；原生 App 只为样本盘 BLE 存在（≤1000 人）。**
→ 样本盘可用**极简原生壳**（仅 BLE 同步 + WebView），不重复实现业务逻辑。

**推送策略**：不依赖 App 推送，一律走**邮件 + 短信**——本来订阅提醒就在这条链路上，且不受 PWA 限制。

---

## 三、功能分层

### L0 · 零 App 基线（必须先成立）

| 功能 | 载体 |
|---|---|
| 按 ZIP 分档的订阅发货（2 ppm 城市 9 个月 / 1 ppm 12 个月） | 后端 + 邮件 |
| 试纸 + 纸质读卡（读数→模块映射） | 包装内 |
| 换芯提醒 | 邮件 / 短信 |

> **验收标准：拔掉整个 App，产品与订阅仍完整可用。**

---

### L1 · 诊断漏斗（Web，购前，**不属于 App**）

架构上的关键切分：**诊断是购前 Web 漏斗，不是 App 功能。** 要求下载才能诊断 = 转化死亡。

- 路径 A：只输 ZIP → 30 秒结果卡（消毒剂类型 + 基线硬度 + 推荐配方）
- 路径 B：ZIP + 试纸 + 观察指引 → 完整组合处方
- 输出「你家的水」报告卡（带 referral 码，可分享）

详见 [获客引擎 §三/§七](./bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md)。**本页不重复设计，只声明归属。**

---

### L2 · ★ 试纸相机读数（核心，数据采集主入口）

> 这是整个 App 存在的第一理由。**零硬件成本，覆盖全量客户，修的是寿命模型主误差项。**

#### 2.1 三个使用时机

| 时机 | 测什么 | 目的 | 优先级 |
|---|---|---|---|
| **① 开箱设置** | **进水**游离氯（+总氯） | ★ **校准该户寿命模型**；反哺 CCR 校正 | **P0** |
| ② 装芯前后验证 | 进/出水对比 | 信任峰值 → referral 触发点 | P1 |
| ③ 每季复测 | 进水 | 捕捉季节性投氯变化 | P2 |

> ⚠️ **①（进水）比②（前后对比）优先级更高**，与直觉相反：②是营销价值，①是模型价值。资源冲突时先保①。

#### 2.2 交互流程

```
拍照（试纸 + 画面内印刷参比色卡同框）
   ↓ 自动：试纸定位 → 色垫分割 → 以参比色卡做白平衡/光源校正
读数（游离氯 / 总氯）
   ↓ 必须同屏显示：量程 + 置信 + 「这是粗筛，不是实验室」
存档 → 更新该户模型 → 回写 ZIP 图谱
```

#### 2.3 硬性 UI 要求（合规）

- **必须显示置信档与量程**，禁止显示超出方法分辨率的小数位
- 读数措辞用**「你家水的类型/档位」**，禁止「你水里有 X 危害」（继承 [获客引擎 §八](./bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md) 反 toxin-panic 红线）
- **氯胺版**：必须提示测量时机——[抗坏血酸会干扰比色使中和被高估](./bathtub-filter-chloramine-media-research.md)
- 光照不足 / 无参比卡入框 → **拒绝给读数**，不给低质量结果

#### 2.4 依赖

- 🔴 **参比色卡必须进包装 BOM** → 挂 gap doc **D-15（卡片进 BOM）**
- 🔴 **试纸量程选型** → 挂 **D-11**；进水场景需覆盖 0.5–4 ppm，与出水验证场景量程要求不同

---

### L3 · 滤芯寿命与换芯（订阅时点，**必须可解释**）

#### 3.1 展示原则：把公式摊开，不给黑箱百分比

```
❌ 「滤芯剩余 37%」
✅ 「你家进水 2.4 ppm（你 3 月测的）
     × 估算已用 14,200 L（约 79 次泡澡）
     = 约还剩 2 个月
     不信？测一张试纸复核 →」
```

**理由**：[「诚实复购触发：氯试纸告诉你该换了，不是黑箱倒计时」](./bathtub-filter-kes-v1-pricing-channel-launch-geo-subscription.md)已是定价页承诺。黑箱百分比直接违背该承诺。

#### 3.2 用户控制权（品牌一致性关键）

| 动作 | 必须支持 |
|---|---|
| Skip 本期发货 | ✅ 一键，不设挽留漏斗 |
| 提前 / 延后 | ✅ |
| **试纸复核作为 override** | ✅ **用户实测结果压过模型预测** |
| 改用量假设（人数/频次/缸容量） | ✅ |

> **模型给建议，试纸给裁定，用户有最终决定权。** 这是「透明品牌的订阅不靠 lock-in」的产品化表达。

#### 3.3 输入项

ZIP → CCR 预测 ‖ 进水试纸实测（优先） ‖ 自报家庭人数/频次/缸容量 ‖ 购买与换芯历史 ‖ *（样本盘）实测流量*

---

### L4 · 样本盘同步（仅 ≤1000 台，原生壳）

- BLE **被动同步**：开 App 时拉取，不常驻、不后台、不配网
- 样本盘专属视图：**「实测用量 vs 估算用量」** —— 对这批用户本身就是有趣的反馈
- ΔP 异常 → 触发**人工介入**（客服联系），**不直接对用户报警**
  - 理由：沟流判读尚未验证（[台架 Q2](./bathtub-filter-25lpm-dechlorination-bench-test-spec.md) 未结），误报会制造"产品有问题"的印象

---

### L5 · 氯胺剂量计算器（V1.5，**不是传感器**）

> 氯胺失效模式是"这缸水剂量够不够"，不是滤芯寿命（[感知策略 §4](./bathtub-filter-sensing-strategy.md)）。

```
输入：ZIP 总氯（或试纸实测） + 浴缸容量
输出：放几片抗坏血酸钠 + 泡几分钟（规划值 4–8 min）
可选：计时器 + 到时提示测总氯验证
```

**红线**：
- ❌ 计时器 UI **不得暗示秒解**；[「快速/秒解」是明确禁区](./bathtub-filter-chloramine-media-research.md)
- ❌ 不得引用 AWWARF Portland「亚分钟」——该数据有三条保留，不作承诺
- ✅ 措辞只能是「在注水+浸泡阶段中和氯胺」

---

## 四、不做什么（与做什么同等重要）

| ❌ 不做 | 原因 |
|---|---|
| 实时水质仪表盘 | 判别带 0.1 mg/L，测不了（[感知策略 §2](./bathtub-filter-sensing-strategy.md)） |
| **任何 TDS 显示** | 化学上方向相反，会自证产品无效（[感知策略 §1](./bathtub-filter-sensing-strategy.md)） |
| 皮肤 / 健康功效追踪 | [claim-register](./bathtub-filter-claim-register.md) 禁区 |
| 软化 / 硬度改善展示 | 产品不做软化，只做阻垢 |
| WiFi 配网 | 原则 4 |
| 强制注册才能用滤芯 | 与透明定位直接冲突；且[专利](./bathtub-filter-kes-patent-19-281644-modular-terminal-water-treatment.md)平台是开放模块化 |
| 黑箱倒计时 | 定价页明确承诺不做 |
| toxin-panic 推送 | 获客引擎红线 |
| 社区 / 商城 / 会员体系 | MVP 阶段纯粹分散精力 |

---

## 五、数据模型（这才是资产）

每户累积：

| 字段 | 来源 | 用途 |
|---|---|---|
| ZIP → CCR 预测水质 | [水务图谱](./bathtub-filter-utility-service-map-by-metro.md) | 基线特征 |
| **进水试纸实测（时序）** | L2 相机 | ★ 修正基线 + **反哺 CCR 校正** |
| 自报用量（人数/频次/缸容量） | L3 表单 | 剂量估算 |
| 购买 / 换芯 / skip 历史 | 电商后端 | 真实消耗节奏 |
| 出水验证读数 | L2 时机② | **穿透真值标签** |
| 流量 / ΔP 时序 | L4 样本盘 | 剂量真值 + 结构失效 |
| skip / 早换 / 晚换 + 原因 | L3 | churn 与满意度信号 |

> 这正是 [感知策略 §6.3](./bathtub-filter-sensing-strategy.md) 所需的带标签三元组来源。

---

## 六、分期

| 期 | 范围 | 载体 | 依赖 |
|---|---|---|---|
| **MVP**（V1 同期） | L0 + L1 + **L2 时机①（进水）** + L3 可解释寿命 | **Web PWA** | 参比色卡进 BOM（D-15）、试纸量程（D-11） |
| **P1**（V1+3 月） | L2 时机②③ + referral 触发接入 + 报告卡 | Web PWA | MVP 完成率数据 |
| **P2**（V1.5） | L5 氯胺剂量计算器 | Web PWA | 氯胺台架 + 抗坏血酸干扰处理 |
| **P3**（样本盘） | L4 BLE 同步 | 原生壳 | 样本盘硬件 + FCC |

> **MVP 不含任何硬件、不含原生 App、不含 BLE。** 可与 V1 上市并行推进，不占硬件排期。

---

## 七、指标

| 指标 | 目标 | 说明 |
|---|---|---|
| **开箱进水读数完成率** | **≥30%** | ★ 主指标。<15% 则[感知策略 §3](./bathtub-filter-sensing-strategy.md) 全量覆盖假设不成立 |
| 覆盖 ZIP / metro 数 | 首发三城各 ≥100 户 | 决定 CCR 校正能否成立 |
| 模型误差 vs ZIP 基线 | 显著优于 | ★ 一年期总判据 |
| 订阅 skip 率 | 下降 | 时点算准的直接体现 |
| 换芯逾期率 | 下降 | 另一方向的误差 |
| 验证读数 → referral 转化 | 建立基线 | 信任峰值假设是否成立 |

---

## 八、待决策

| # | 决策 | 影响 | 建议挂靠 |
|---|---|---|---|
| 1 | 参比色卡进包装 BOM | L2 全部功能的前提 | **D-15** |
| 2 | 试纸量程（进水 0.5–4 ppm vs 出水低量程，是否两种） | L2 准确度 + COGS | **D-11** |
| 3 | 手机比色自研 vs 外采 SDK | 排期与成本 | 新增 |
| 4 | 样本盘独立 SKU（$99–129）vs 免费投放 | 数据获取成本 | 新增 |
| 5 | 原生壳是否值得为 ≤1000 人做 | 可否推迟到 P3 后 | 新增 |

---

## 九、风险

| # | 风险 | 缓解 |
|---|---|---|
| 1 | **读数完成率过低** | 把入口埋在开箱卡 QR + 首封邮件；20 秒内完成；**不要求注册** |
| 2 | 手机比色在真实光照下不准 | 参比色卡强制同框；光照不足拒绝出数；**上线前需自建验证集** |
| 3 | 皂液基质污染出水读数 | 出水验证仅作定性（时机②），**不进模型** |
| 4 | 抗坏血酸干扰氯胺读数 | L5 强制时机提示；并入氯胺台架验证 |
| 5 | App 变成 claim 泄漏面 | 所有文案走 claim-register 同一审校流程 |

---

## Sources / 内部依据

- [感知策略](./bathtub-filter-sensing-strategy.md) —— 功能边界的全部推导依据
- [水质自测套件 + 模块化获客引擎](./bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md) —— 诊断路径 A/B、验证试纸、referral 触发、红线
- [V1 定价/渠道/订阅](./bathtub-filter-kes-v1-pricing-channel-launch-geo-subscription.md) —— 9/12 月档期、诚实复购触发承诺、DTC 主战场
- [氯胺介质研究](./bathtub-filter-chloramine-media-research.md) —— 4–8 min 规划值、抗坏血酸干扰、claim 禁区
- [客户水质检测方法分析](./bathtub-filter-customer-water-quality-test-methods-2026-06-03.md) —— 品类不测量的行为基线

## Obsidian links

- [[bathtub-filter-sensing-strategy]]
- [[bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine]]
- [[bathtub-filter-kes-v1-pricing-channel-launch-geo-subscription]]
- [[bathtub-filter-chloramine-media-research]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-decision-register]]
