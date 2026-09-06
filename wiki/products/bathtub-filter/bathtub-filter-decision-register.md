---
type: product
status: draft
owner: strategy
created: 2026-04-17
updated: 2026-09-06
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, decisions, tracker]
source_count: 4
review_cycle: weekly
verification_status: working
related:
  - ./bathtub-filter-kes-next-step-execution-plan-v1.md
  - ./bathtub-filter-kes-go-no-go-memo-v1.md
  - ./bathtub-filter-test-gating-checklist-for-kes.md
---

# 浴缸过滤器决策与工作流台账

## 这页的用途

这页是整个 bathtub filter KES diligence 过程中的**决策与工作流追踪器**。

它不替代 go/no-go memo 或 execution plan，而是作为一个持续更新的工作状态视图：
- 哪些决策仍然 open，谁负责，下一步是什么
- 每条 workstream 当前在哪里
- 已完成的决策（防止重复讨论）
- 决策历史存档

**更新频率：** weekly（至少在 workstream 有进展时同步更新）

---

## Open Decisions

这些决策目前尚未有明确答案，需要验证数据或明确的判断调用才能关闭。

| # | Decision | Owner | Input required | Due | Status |
|---|---|---|---|---|---|
| D-01 | Confirm or re-rank lead concept: Hybrid premium-but-disciplined route vs Narrow chlorine-focused route — current ranking is provisional pending Workstream 2 and 3 results | strategy | Public competitor evidence (WS2) + normal-flow test results if existing samples/records are available (WS3) | After WS2+WS3 evidence review | not-started |
| D-02 | Define exact supported tub-spout types — which spout configurations are in scope for V1, which are explicitly out | strategy | 2026-06-17 已在 [[bathtub-filter-supported-spout-matrix]] 补入 8 类安装场景 + KES GO/GO（条件）/NO-GO 矩阵；S-01 non-diverter terminal-bend circumference <=18 cm 为正向边界；两组 RV / mobile-home center-set / valve-diverter faucet 为 S-02-adjacent 正向证据；freestanding tub filler 弧形/异型管非瀑布出水已补 2 kg 承重正向证据。仍需动态注水、漏水/溢流和更多 spout 类型实测记录。 | Before fit/testing scope finalized | in-progress |
| D-03 | Set pass/fail thresholds for normal-flow chlorine reduction test — what performance level is required for the route to remain viable | strategy | Validation protocol design (WS3) | Before testing begins | not-started |
| D-04 | Resolve renter-friendly vs engineering robustness priority — if they cannot be simultaneously achieved, which takes precedence in V1 concept | strategy | Sample testing + engineering assessment (WS3) | After WS3 results | not-started |
| D-05 | Determine acceptable refill cadence and cost ceiling — what refill interval and price point will the target segment accept without triggering maintenance fatigue or lived-economics collapse | strategy | Consumer research or benchmark review; refill economics sanity check (WS3) | After WS3 | not-started |
| D-06 | Decide whether chlorine/comfort story converts without eczema-forward language — is the disciplined claim set commercially sufficient | strategy | Content testing or competitive signal review (WS2+WS4) | After WS2+WS4 | not-started |
| D-07 | Select primary geo / water-profile for V1 launch targeting — confirm free-chlorine North America as primary, or refine sub-geo further | strategy | Water jurisdiction demand map review + WS2 competitive observation | Before concept finalization | not-started |
| D-08 | Final continue / pause / archive decision after early validation | strategy | All WS1–WS4 outputs; gate checklist passage | After WS5 | not-started |
| D-09 | **Refill 形态**：补芯是整个 Tritan 透明滤仓，还是散装介质自行装填（专利腔体可重复开启、BOM 上下盖 33° 卡扣）——决定 refill COGS / 价格 / 包装体积 / 可持续措辞 / "看得见的料"是否延伸为"自己装的料" | product | BOM + COGS；建议倾向散装介质 + 可重开仓，Tritan 仓作耐用件 | Before refill SKU pricing | open（2026-09-05 登记） |
| D-10 | **KDF55 仓装填与壳体**：按 BOM 几何 130 g KDF55 只占床容积 36–44%（摊平 5–6 mm），透明仓会显得半空且床层易位移。选项：改 KDF 仓有效高度 / 加透明填充隔板 / 增加 KDF 用量 / 可视化主张只落 CaSO₃ 仓。同时确认 2026-07-02 克数互换是否为装配驱动（130 g CaSO₃ 装不进 123 cm³ 仓） | engineering | 实机装填高度实测（25lpm spec §2.5） | Before Gate 1 | open（2026-09-05 登记） |
| D-11 | **试纸规格**：随盒游离氯试纸须能读出更换触发。市售 0/0.5/1/2 ppm 粗档在 1–2 ppm 进水下只能看到 ~50% 失效点。选项：低量程细分试纸（0/0.1/0.25/0.5/1）/ DPD 滴剂 / 接受"首次显色即换"单触发 | product + ops | 试纸供应商量程规格；T3 §〇 | Before P2 定稿 | open（2026-09-05 登记） |
| D-13 | **性能锚点流量**：T2 以 15 L/min 为性能主口径，低于美国典型 18–25 L/min。Gate 1 出三点曲线（15 / 20 / 25）后，对外是否直接发布曲线而非单点 | product + marketing | Gate 1 结果 | After Gate 1 | open（2026-09-06 登记） |
| D-14 | **产品线展开节奏**：氯胺版 / 井水版已 GO 且 site/ 有 S2 / S3 / M3–M6 页，但 V1 未过 Gate 1；是否冻结这两条线的内容维护与 SKU 定义直到 V1 Gate 1 通过。氯胺版的抗坏血酸浸泡步骤用户负担未评估 | strategy | Gate 1；K1 维护负担验证 | Before V1.5 spec | open（2026-09-06 登记） |
| D-15 | **分享试纸卡 ×3 与 Before/After 对比卡进 BOM**：P5 包装层序 L3 已依赖两者，P2 仍为提案；不批则刀模要改 | product + supply chain | 成本核算；referral 机制是否上线 | Before packaging die | open（2026-09-06 登记） |
| D-12 | **订阅周期**：原 90 天与寿命模型（2 ppm ≈ 40 周）矛盾；改为按 ZIP 水型分档（9 / 12 个月）+ 耗材包 90 天档。需 finance 按 1.3 次/年重跑 LTV | ops + finance | T3 寿命口径；GTM §4.2 | Before subscription launch | open（2026-09-05 登记） |

---

## Workstream Status

来自执行计划（execution plan v1）的 5 条工作流，当前状态如下。

| Workstream | Description | Owner | Status | Next action |
|---|---|---|---|---|
| WS1 — Concept narrowing | 从现有 concept candidates 中锁定 1 lead + 1 backup，输出每条路线的 concept summary 和被淘汰路线的 rejection note | strategy | not-started | Confirm lead concept ranking (D-01); freeze route scope before WS2 begins |
| WS2 — Competitor public evidence integration | 整理原始 11 ASIN 中的 bathtub active 10 ASIN 官方/PDP 公开资料、价格/销量信号、claim、安装与结构线索；Filterbaby 已迁出 shower-filter；不做样品采购清单或预算估算 | strategy | in-progress | Use [[bathtub-filter-11-asin-public-competitor-evidence-2026-06-02]] as the evidence matrix |
| WS3 — Validation test setup | 建立并运行验证测试：normal-flow chlorine reduction, reduced-flow comparison, fit matrix across spout types, leak/overflow/stability, refill/maintenance burden | TBD | in-progress | 2026-06-17 已有 S-01 周长边界正向记录、2 组 S-02-adjacent 正向适配样本、freestanding tub filler 非瀑布出水 2 kg 承重记录，以及 8 类安装场景 GO/NO-GO 矩阵；仍需设计 test sheet template、定义 pass/fail thresholds (D-03)、补更多 spout 类型和动态注水记录 |
| WS4 — Claim & language guardrails | 完成 allowed / conditional / banned claim list，防止团队在这个品类滑向高风险语言；输出 claim register | strategy | in-progress | Complete [[bathtub-filter-claim-register]] stub; fill in example wording after WS2 competitor research |
| WS5 — Decision checkpoint | 在公开竞品资料复盘与验证测试准备后，做一次明确的 continue / pause / archive 决策；如无实物或人工测试记录，E 层安装/兼容性仍保持未关闭 | strategy | not-started | Depends on WS1–WS4 outputs; schedule decision review after WS2 evidence and any WS3 records |

---

## Completed Decisions

_这个区域目前为空。随着决策被关闭，将逐条移入此处。_

| # | Decision | Resolution | Date | Notes |
|---|---|---|---|---|
| **D-16** | **参比色卡是否进包装 BOM**（手机比色读试纸的物理前提：无同框参比，无法在未知光源下校正色彩） | ✅ **进 BOM** | 2026-09-06 | 用户裁定。解锁 [[bathtub-filter-app-functional-plan]] L2 全部功能。**工艺约束见下方 §参比色卡规格要求**——不是普通印刷卡，误做会让读数不可用。**应与 D-15 合并出一张卡 / 一套刀模** |

### 参比色卡规格要求（D-16 配套，供应链执行口径）

> ⚠️ **这不是一张普通印刷卡。** 下列每条都直接决定手机比色读数能否用；做错任一条，卡片仍会被印出来，但读数不可用且不会报错。

| # | 要求 | 为什么 |
|---|---|---|
| 1 | **必须哑光（matte）**，禁止覆亮膜 / UV 上光 | 亮面产生镜面高光，直接毁掉色度读数 |
| 2 | **含中性灰 + 白色块** | 未知光源下做白平衡 / 光源校正的锚点 |
| 3 | **含该配方 DPD 色阶**（游离氯版 / 总氯版分开） | 机读的比对基准；同时保留肉眼可读的降级路径 |
| 4 | **色彩批次一致性须进 QC** | 印刷批间漂移会让模型标定跟着漂 |
| 5 | ★ **卡面印批次 / 版本码**（小字或 QR） | 后端据此套用对应标定档；**没有它，一旦换印刷批次，历史读数无法追溯校正** |
| 6 | **防潮**（哑光覆膜或合成纸） | 浴室环境；受潮变色即失效 |
| 7 | 尺寸须能与试纸**同框入镜** | 手机单张拍摄同时含试纸与参比 |

**待办**：① 该卡尚未进 [[bathtub-filter-v1-free-chlorine-removal-dimensions-materials]] 部件表（该表源自 2026-07-01 最终版 xlsx，需供应链在下一版 BOM 增列）；② 与 D-15 的分享试纸卡 ×3 / Before-After 卡**合并刀模**核算；③ 色卡打样后须**与目标机型实拍验证**，不能只看印刷稿。

---

## Decision Log

_这个区域用来记录决策历史——每次重大判断调用、每次路线重排序、或每次 go/no-go memo 更新，都应在这里留下一条记录。_

_Format:_ `YYYY-MM-DD | Decision ID or topic | What was decided | Why | Who`

| Date | Topic | Decision | Rationale | Owner |
|---|---|---|---|---|
| 2026-04-14 | Route framing | Conditional GO for continued diligence — not product GO | Research package sufficient for continued concept exploration, but insufficient for launch conviction | strategy |
| 2026-04-14 | Route elimination | Eliminated: aggressive eczema/baby DTC, commodity broad-claim bath-ball as lead routes | Claim/compliance risk too high; no differentiation advantage | strategy |
| 2026-04-14 | Concept priority | Lead: Hybrid premium-but-disciplined tub-spout route. Backup: Narrow chlorine-focused technically disciplined route. Conditional reserve: soft-hanging ritual | Based on route comparison across commercial appeal, defensibility, and technical feasibility | strategy |
| 2026-04-14 | Market scope | V1 primary target: North America, free-chlorine-dominant regions | Chloramine and hard-water markets are harder to defend with current claim set | strategy |
| 2026-06-17 | D-02 supported spout scope | Added first V1 installation scenario GO/NO-GO matrix with 8 spout scenarios; S-01 <=18 cm and S-02 pull-up diverter are current GO cores; S-06 wobble and untested S-05 wide-body are NO-GO; S-08 low-clearance was later corrected to GO with off-center install for 40-60 mm wall distance | Combines KES flat-strap design, S-01 circumference evidence, RV/mobile-home S-02 evidence, and existing spout taxonomy estimates | strategy |
| 2026-06-17 | Wall-distance boundary correction | Changed outlet center-to-wall distance from a <60 mm NO-GO rule to a usability/aesthetics rule: >=60 mm centered/aesthetic, 40-60 mm off-center usable, <40 mm theoretical edge case | User clarified the water outlet need not be perfectly centered; KES can tolerate about 20 mm offset and typical bathtub spouts are not under 40 mm from wall | strategy |
| 2026-09-06 | D-16 参比色卡进 BOM | 参比色卡进包装 BOM；规格按「哑光 + 中性灰/白块 + DPD 色阶 + 批次码 + 防潮 + 可同框」执行 | 手机比色读试纸是[[bathtub-filter-sensing-strategy]]中唯一零硬件成本、覆盖全量客户、且修复寿命模型主误差项（进水浓度）的手段；无同框参比则未知光源下无法校正，该功能不成立 | user / strategy |
| 2026-06-17 | Freestanding tub filler fit evidence | Updated freestanding tub filler from default NO-GO to GO for curved / special-shaped / non-waterfall outlets when the tie is installed 60 mm from the outlet end; waterfall / wide-body outlets remain NO-GO | User-provided photo and 2 kg load-bearing test using included 5-hole 125 mm x 20 mm tie + 3M hook | strategy |

---

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-kes-next-step-execution-plan-v1]]
- [[bathtub-filter-kes-go-no-go-memo-v1]]
- [[bathtub-filter-kes-concept-brief-v1]]
- [[bathtub-filter-kes-route-elimination-memo-v1]]
- [[bathtub-filter-test-gating-checklist-for-kes]]
- [[bathtub-filter-claim-register]]
- [[bathtub-filter-assumption-register]]
- [[bathtub-filter-supported-spout-matrix]]
