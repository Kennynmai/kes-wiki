---
type: product-knowledge
product: bathroom-hardware
section: thread-standards
status: active
created: 2026-07-04
updated: 2026-07-04
domain: product-engineering
domains: [thread-standards, us-market, listing-copy, shower-arm, shower-head]
confidence: high
verification_status: verified
---

# 淋浴螺纹标准与美国市场口径（G1/2 / NPT / NPSM / IPS）

> 起因：2026-07-04 Amazon 美站 bullet 回写试点（PSAN204-BK-RE 淋浴臂）文案写
> "G1/2 thread" 被质疑非美标。经三轮查证形成本篇最终结论——
> **哪些连接是什么螺纹、G1/2 在美国到底能不能直接用、文案该怎么写**。

---

## 一、最终结论（TL;DR）

1. **淋浴系统里存在两类完全不同的螺纹连接，不能混为一谈**：
   - **墙端（arm ↔ 墙内弯头）= 1/2" NPT 锥牙**，靠螺纹本身+生料带密封；
   - **花洒端（arm ↔ 花洒旋帽）= 1/2"-14 直牙 + 橡胶垫圈密封**，螺纹只负责夹紧，不负责密封。
2. **G1/2 出水端配美标花洒没有问题**：G1/2 与美标花洒旋帽（NPSM/NPS/IPS 系）
   同为 14 牙/英寸、外径仅差 0.38mm，可正常旋合；密封由垫圈完成，
   55°/60° 牙型差异不影响。Delta 官方自述淋浴臂即"1/2" IPS 直牙+垫圈密封"。
3. **G1/2 直配 NPT（锥牙场景）不行**——牙型 55° 圆顶 vs 60° 平顶、锥直不同，
   靠螺纹密封会漏，需转接头。网上大量"G 转 NPT 需要 adapter"的警告都是说这类场景，
   **不适用于垫圈密封的花洒端**。
4. **文案口径**：术语按目标市场买家习惯表述（美站 "1/2-inch" 打头、工程标记括号），
   两端分开写清；**严禁把 G1/2 改标成 NPSM/NPT**（跨标准改标=虚假规格）。

## 二、螺纹标准速查表

| 标准 | 全称/体系 | 牙距 (1/2") | 牙型角 | 公牙外径 (1/2") | 锥/直 | 密封方式 | 主用地 |
|---|---|---|---|---|---|---|---|
| **NPT** | National Pipe Taper | 14 TPI | 60° 平顶 | 0.840" (21.3mm) | 锥 | 螺纹+生料带 | 美国（墙内管路） |
| **NPSM / NPS** | National Pipe Straight Mechanical | 14 TPI | 60° | 0.84" (27/32")，母口 ID 25/32" | 直 | 垫圈/机械座 | 美国（花洒旋帽等活接） |
| **IPS** | Iron Pipe Straight（贸易叫法，≈NPS 系） | 14 TPI | 60° | ≈0.84" | 直 | 垫圈 | 美国（Delta 等自述淋浴臂螺纹） |
| **G1/2 (BSPP)** | ISO 228 平行管螺纹 | 14 TPI | 55° 圆顶 | 20.955mm (0.825") | 直 | 垫圈/O 圈 | 欧亚（花洒/软管全球标准） |
| BSPT | 英制锥管螺纹 | 14 TPI | 55° | — | 锥 | 螺纹 | 欧亚墙内管路 |

关键数字：**G1/2 与 NPSM 1/2 同牙距（14 TPI）、外径只差 0.38mm**（0.825" vs 0.84"）
→ G1/2 公牙旋入美标花洒母帽能咬合（略松），垫圈压紧后密封无虞。

### NPS 家族辨析（术语必读）

**NPS = National Pipe Straight，是美标直牙管螺纹的"家族统称"**，不是单一规格。
全家族与 NPT 共享公称尺寸/牙距/60° 牙型（1/2" 一律 14 TPI、OD 0.840"），
区别只在直牙 + 各成员配合用途：

| 成员 | 用途 | 密封 | 卫浴相关性 |
|---|---|---|---|
| **NPSM**（Mechanical） | 自由配合机械活接——**花洒旋帽即此** | 垫圈/密封座 | ★ 核心 |
| NPSC（Coupling） | 管接箍内牙，配 NPT 公牙 | 密封胶 | 少见 |
| NPSL（Locknut） | 锁紧螺母 | 不密封 | 台面龙头锁母 |
| NPSH（Hose） | 软管接头 | 垫圈 | 基本不涉 |
| NPSF/NPSI（Dryseal, B1.20.3） | 燃油/气动干密封 | 螺纹 | 不涉 |

- 厂商写 "1/2-14 NPS"（如 High Sierra 花洒母口）= 口语化省略，严格即 **NPSM**。
  卫浴场景 NPS ≈ NPSM 可互换理解。
- ⚠️ **术语陷阱**：NPS 另有完全无关的第二义 = **Nominal Pipe Size（公称管径）**
  （"NPS 1/2 pipe" 说的是管径编号非螺纹）。读供应商资料靠上下文分辨。

## 三、按连接点的判定

| 连接点 | 美国标准 | G1/2 件能否直配 | 说明 |
|---|---|---|---|
| 淋浴臂 → 墙内弯头 (drop-ear) | 1/2" NPT 锥牙母口 | ❌ 不能 | G1/2 平行公牙进 NPT 锥母，螺纹密封失效；必须本身就是 NPT 公牙或加转接头 |
| 花洒旋帽 → 淋浴臂出水端 | 1/2"-14 NPSM/IPS 直牙 + 垫圈 | ✅ 能 | 同牙距近同径可旋合；垫圈密封；Delta/Moen/High Sierra 等美系花洒旋帽均为此类 |
| 手持花洒软管两端 | 全球统一 G1/2 | ✅ 本来就是 | 淋浴软管是少数全球单一标准的连接 |
| 恒温/暗装阀体进出水 | NPT（美规阀） | ❌ 视产品 | 走墙内管路逻辑 |

## 四、PSAN204-BK-RE 案例（本次调查的实证载体）

- 产品：KES 替换淋浴臂（哑光黑，amz_us，B0C2T8SDBT）。
- **物理规格（已确认）**：墙端 = 1/2" NPT（产品负责人 2026-07-04 确认）；
  出水端 = G1/2（工程履历：曾改 NPT 因"标准 NPT 生产难以把控、加工偏差大、
  配合度出问题"而**改回 G1/2**；策展属性 connector_type = G1/2 Thread）。
- 结论：这是"墙端美标锥牙 + 出水端全球直牙"的**合理组合**——墙端满足美国管路，
  出水端 G1/2 与美标花洒旋帽垫圈连接兼容。
- 文案终版（v4，Amazon accepted）：
  - 墙端："Standard 1/2-inch NPT wall-end thread screws onto US supply pipes—installs
    in minutes with thread seal tape."
  - 花洒端："Shower Head Connection: 1/2-inch-14 straight outlet thread (G1/2) fits
    standard US shower head swivel nuts, which seal on a rubber washer—no tapered
    thread needed at the head joint."

### 迭代教训（四版演进）
| 版本 | 问题 |
|---|---|
| v1 "Standard G1/2 threaded connection fits most shower heads" | G1/2 打头美国买家不识；"any/most"无证据 |
| v2 "1/2-inch (G1/2)" | 表述改善但兼容声明仍未验证 |
| v3 撤掉兼容声明+提示可能需转接头 | 过度保守（当时 G↔NPSM 未查清，误用了 G↔NPT 的警告） |
| v4 两端分开+完整证据链 | ✅ 终版 |

## 五、文案与数据治理规则（已固化）

1. **表述本地化、事实不动**：美站规格用买家惯用标记打头（1/2-inch），
   工程标记（G1/2）放括号；**禁止跨标准改标**（G1/2 ≠ NPT ≠ NPSM）。
2. **兼容性声明分场景**：垫圈密封直牙连接可写 "fits standard US shower heads"；
   锥牙螺纹密封场景严禁写通配兼容；避免 "any/all"，用 "most standard"。
3. **两端螺纹分开写**：淋浴臂/龙头类产品必须分端标注，单写一个 G1/2 会让买家
   误以为墙端也是 G1/2。
4. 以上规则已写入 ops 平台两个内容生成器（文本改写桥 + A+ gap-fill 桥）的
   system prompt（2026-07-04）。
5. **待办**：产品规格中台只录了出水端 connector_type=G1/2，
   **墙端 1/2" NPT 未入库**——需在 /admin/product-spec 补录（wall_end_thread），
   否则后续 LLM 内容批次仍只见 G1/2 单一信息。

## 六、证据来源

- Delta 官方产品页（淋浴臂 1/2" IPS 直牙+垫圈密封）：
  https://www.deltafaucet.com/bathroom/product/RP46870.html
- High Sierra（美系花洒母口 "1/2 inch-14 NPS Female Threads"）：
  https://www.highsierrashowerheads.com/shop/retrofits-standard-shower-heads-with-1-2-inch-14-nps-female-threads-chrome-swivel/
- Trausch Dynamics 螺纹识别手册（NPSM 尺寸表：1/2-14，公牙 OD 27/32"；BSPP 1/2-14）：
  https://www.hydraulicstore.com/images/pdf/NPSM%20THREAD.pdf
- Kingston Brass：NPT vs NPS 淋浴连接：
  https://www.kingstonbrass.com/blogs/blog/npt-vs-nps-shower-connections
- Terry Love 水暖论坛（G↔NPT 直配会漏、需转接头——仅适用锥牙场景）：
  https://terrylove.com/forums/index.php?threads/g-1-2-thread.63418/
- KES 内部：product_context_section 工程履历（出水端 NPT→G1/2 改回记录）、
  attribute_value（connector_type=G1/2）、产品负责人确认（墙端 NPT，2026-07-04）。
