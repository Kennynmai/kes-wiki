---
type: product
status: draft
owner: strategy
created: 2026-04-14
updated: 2026-04-14
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, roadmap, rd, validation]
source_count: 9
review_cycle: monthly
verification_status: working
related:
  - ./bathtub-filter-kes-go-no-go-memo-v1.md
  - ./bathtub-filter-kes-next-step-execution-plan-v1.md
  - ./bathtub-filter-test-gating-checklist-for-kes.md
  - ./bathtub-filter-certification-authority-tiers-and-workflow.md
  - ./bathtub-filter-route-clusters-and-kes-opportunity-spaces.md
  - ../playbooks/bathtub-filter-validation-testing-protocol.md
---
# Bathtub Filter KES R&D 与验证 roadmap

## 这页的目的
这页不是再讨论“这个品类有没有意思”，而是把现有 research package 直接转换成 **KES 接下来 4–8 周该怎么动** 的 roadmap。

核心目标只有一个：

> **尽快判断 KES 是否存在一个值得继续推进的 survivable bathtub filter route。**

如果答案是否定的，就应尽早 kill，而不是继续堆文案、堆研究、堆想象。

## 总原则
### 不是先做什么
- 不是先做包装
- 不是先做 listing 文案
- 不是先追求大而全 claims
- 不是先冲 formal certification

### 而是先做什么
1. 定义 route
2. 采购样品
3. 建测试基准
4. 做 fit / flow / leak / hygiene 验证
5. 锁最窄、最可证实的 claim
6. 再决定是否值得 prototype / certification / launch planning

---

## Roadmap 总览
### Phase 0 — scope freeze（第 1 周）
**目标：停止继续发散，冻结当前评估范围。**

#### 必须确认
- Lead route：**premium-but-disciplined inline route** 是否仍为第一优先
- Backup route：**hygiene-upgraded hanging route** 是否保留为第二优先
- 明确 out-of-scope：
  - aggressive eczema / baby outcome route
  - broad-contaminant fantasy route
  - commodity bath-ball clone route

#### 输出物
- 1 页 route priority note
- 1 页 out-of-scope note
- 1 份 sample acquisition shortlist

#### Kill criteria
如果团队连“先测哪条路线”都定不下来，就不应继续进入开发阶段。

---

### Phase 1 — benchmark sample acquisition（第 1–2 周）
**目标：把判断从“页面感觉”转成“样品现实”。**

#### 建议采购结构
至少覆盖 4 类：
1. **premium spout-attach benchmark**
   - 代表 design-first inline route
2. **legacy-media / chlorine-focused benchmark**
   - 代表 Sprite-like technical lineage
3. **hanging / soft-hanging benchmark**
   - 代表 Santevia-like route
4. **bath-ball / immersion benchmark**
   - 代表 Crystal Quest-like route

#### 采购时必须记录
- SKU 名称
- 当前页面 claims
- 页面 authority language（certified / tested / media / clinical）
- 价格、refill 节奏、适配说明

#### 输出物
- sample tracker
- buy list + budget
- competitor-claim snapshot

#### Kill criteria
如果连能代表主流路线的 benchmark 都买不到或信息残缺严重，说明这类目标准化程度太低，后续开发要进一步降预期。

---

### Phase 2 — engineering baseline definition（第 2 周）
**目标：先定义真实浴缸工况，再谈性能。**

#### 必做 1：spout geometry matrix
建立 tub-spout taxonomy，至少区分：
- diverter vs non-diverter
- 外径 / 长度 / 出水角度差异
- 是否存在典型不适配结构

#### 必做 2：bath-fill realism benchmark
先定义：
- realistic normal-flow band
- reduced-flow band
- acceptable fill-time upper bound
- 参考 bathtub volume 区间

#### 必做 3：test fixture / measurement method
准备：
- chlorine 测试方法
- fill-time 记录方法
- leak / splash / overflow 记录表
- photo / video capture routine

#### 输出物
- spout matrix
- bath-fill benchmark sheet
- test SOP v1

#### Kill criteria
如果连 realistic flow benchmark 都定不出来，后续所有“性能”都可能变成伪结论。

---

### Phase 3 — teardown + water-path proof（第 2–3 周）
**目标：先搞清样品到底怎么工作，而不是先相信它写了什么。**

#### 要做什么
- 拆样品
- 看 media stack
- 看 water path
- 看 cartridge lock / seal / bypass 风险
- 看 drying / hygiene 设计

#### 特别关注
- 水是否真的被迫穿过主要 media
- 有没有明显 bypass 机会
- 有没有为了看起来复杂而堆的“stage theater”
- hanging route 是否本质上只是 bath-treatment accessory，而非严肃过滤装置

#### 输出物
- teardown notes
- water-path sketches
- route comparison note

#### Kill criteria
如果样品拆解后发现主流产品大都严重依赖模糊路径和 marketing theater，那 KES 应更保守定义产品 ambition。

---

### Phase 4 — core validation testing（第 3–5 周）
**目标：验证“能不能用”，不是验证“故事好不好听”。**

#### Module A — normal-flow chlorine reduction
测：
- realistic normal flow
- reduced flow
- chlorine reduction %
- fill time impact

#### Module B — fit / installation test
测：
- supported spouts
- unsupported spouts
- 安装时间
- 稳定性
- 是否需要 workaround

#### Module C — leak / splash / overflow / repeated-use stability
测：
- 连续使用下的稳定性
- seal 是否衰减
- mounting 是否松脱
- 是否容易产生溅水与溢流风险

#### Module D — refill / maintenance / hygiene burden
测：
- 替换频率是否可接受
- 是否必须频繁晾干、拆洗、存放
- 用户维护动作是否过于麻烦

#### 输出物
- validation report v1
- fail-mode log
- route scorecard

#### Kill criteria
以下任一成立，都应高度警惕：
- 只有在 slow flow 下才有像样表现
- 主 route 对 fit 过度挑剔
- leak / splash / overflow 问题难消
- hygiene burden 高到不像可规模化消费品

---

### Phase 5 — claim architecture lock（第 5–6 周）
**目标：在产品现实基础上，锁定可以说什么。**

#### 必须建立
1. **claim-evidence register**
   - 每条 claim 对应哪类证据
2. **authority map**
   - certified / tested / media / internal / testimonial 各自是什么
3. **copy red-lines**
   - 客服 / Amazon / 包装 / FAQ 禁词
4. **SKU authority boundary**
   - bathtub SKU 不能借 shower SKU 的 authority 乱写

#### 优先锁定的 claim zone
- chlorine-conscious
- odor reduction
- gentler bath-water feel
- stated fit boundary
- stated refill boundary

#### 默认不碰的 claim zone
- eczema improvement
- baby-safe implication
- broad contaminant package
- hard-water softening promise
- clinical outcome

#### 输出物
- allowed claims
- conditional claims
- banned claims
- red-line glossary

#### Kill criteria
如果没有可守住的 claim architecture，这条 route 即使工程上能做，也不一定适合商业化。

---

### Phase 6 — certification path decision（第 6–7 周）
**目标：决定是只做 testing，还是值得投入 formal certification。**

#### 决策问题
- 当前 route 是 bathtub-only，还是未来有 shower sibling SKU？
- 当前最强 claim 是否已经足够窄、足够稳定？
- 是否值得走：
  - third-party testing only
  - materials / component compliance
  - formal certification exploration（如 `NSF/ANSI 177` / WQA / IAPMO 邻近路径）

#### 当前建议倾向
- **bathtub 先走 realistic-flow third-party testing + narrow claims**
- 如果未来发展 shower sibling SKU，再认真评估 `NSF/ANSI 177` / WQA / IAPMO 路径

#### 输出物
- certification decision memo
- authority strategy note
- estimated certification cost/time note

#### Kill criteria
如果 route 只有靠“借认证气氛”才显得可信，而不是靠真实 evidence，就不应进入认证投入阶段。

---

### Phase 7 — prototype go / no-go checkpoint（第 7–8 周）
**目标：明确要不要进入 prototype / supplier conversation。**

#### Go 条件
至少同时满足：
- realistic flow 下仍有 meaningful performance
- fit scope 足够清楚
- leak / splash 风险可控
- hygiene / refill burden 可接受
- claim architecture 清晰
- authority strategy 清晰

#### No-Go / Pause 条件
任一较重问题未解决：
- normal-flow 表现塌陷
- fit 成功率太低
- 维护负担过高
- 只能靠高风险 claims 才能卖
- certification / testing 路径讲不清楚

#### 输出物
- prototype brief
或
- pause / archive memo

---

## 建议组织方式
### 建议 owner
- Strategy：总 roadmap owner
- Product / sourcing：样品采购
- Engineering：fit / leak / flow / teardown
- QA / compliance：claim-evidence register + authority map

### 建议每周节奏
- 周初：决定测试包 / 采购 / 本周验证目标
- 周中：实测 / 记录 / 拆解
- 周末：出 route scorecard + 下周 go / no-go

---

## 当前最推荐的优先顺序
### Lead route
**premium-but-disciplined inline route**

原因：
- 最接近 KES 能力带
- 最容易做成可信的 bathroom hardware object
- 最适合走窄 claim + 工程验证路线

### Backup route
**hygiene-upgraded hanging route**

原因：
- 更适合 wellness / ritual 表达
- fit 风险可能低于某些 inline route
- 但必须先过 hygiene / maintenance / proof-visibility 这一关

---

## 给 Kenny / KES 的一句话执行建议
> **接下来 4–8 周不要再把重心放在“找更多资料”，而要把重心放在“买样、拆样、测样、定边界”。**

## Obsidian links
- [[bathtub-filter]]
- [[bathtub-filter-kes-next-step-execution-plan-v1]]
- [[bathtub-filter-test-gating-checklist-for-kes]]
- [[bathtub-filter-certification-authority-tiers-and-workflow]]
- [[bathtub-filter-route-clusters-and-kes-opportunity-spaces]]
- [[bathtub-filter-validation-testing-protocol]]
- [[bathtub-filter-kes-go-no-go-memo-v1]]

## Sources
- [[bathtub-filter-kes-next-step-execution-plan-v1]]
- [[bathtub-filter-test-gating-checklist-for-kes]]
- [[bathtub-filter-certification-authority-tiers-and-workflow]]
- [[bathtub-filter-route-clusters-and-kes-opportunity-spaces]]
- [[bathtub-filter-validation-testing-protocol]]
- [[bathtub-filter-kes-go-no-go-memo-v1]]
