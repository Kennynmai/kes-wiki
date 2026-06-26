---
type: product
status: draft
owner: strategy
created: 2026-04-14
updated: 2026-06-17
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, execution-plan]
source_count: 7
review_cycle: monthly
verification_status: working
related:
  - ./bathtub-filter-final-executive-summary-2026-04-14.md
  - ./bathtub-filter-kes-concept-brief-v1.md
  - ./bathtub-filter-test-gating-checklist-for-kes.md
  - ./bathtub-filter-kes-route-elimination-memo-v1.md
  - ./bathtub-filter-11-asin-public-competitor-evidence-2026-06-02.md
  - ../../playbooks/bathtub-filter-validation-testing-protocol.md
---

# 浴缸过滤器下一步执行计划 — V1

## 这页的目的
这页把当前 research package 转成实际可执行的 next-step plan。

它回答的不是“这个品类有没有意思”，而是：

> **如果 KES 还要继续，这件事下一步到底怎么做？**

## 当前总原则
当前建议不是 launch，而是：
- 结束继续扩写型 desk research
- 进入 concept narrowing + 公开竞品资料补全 + validation testing 准备
- 在测试后再做一次明确的 continue / pause / archive decision

## 目标
先回答一个更窄的问题：

> **KES 是否存在一个可存活（survivable）的 bathtub filter concept path？**

如果没有，就应把这题保留为 research archive，而不是继续投入产品开发叙事。

## Workstream 1 — concept narrowing（概念收窄）
### 目标
只保留：
- 1 个 lead concept（主概念）
- 1 个 backup concept（备选概念）

### 当前建议
> **注意：** 以下是基于当前 research package 的推荐起点，**不是已锁定的产品决策**。Workstream 2 现在只做 bathtub active 10 ASIN 公开竞品资料补全，不做样品采购；Filterbaby `B0FNVDJRSQ` 已从 bathtub 评论语料删除并拆到 shower-filter 项目。Workstream 3 已有 S-01 non-diverter 周长边界正向记录、2 组 RV / mobile-home center-set / valve-diverter faucet 正向适配样本，以及 freestanding tub filler 非瀑布出水 2 kg 承重记录，但仍不足以关闭安装/兼容性证据缺口；如后续测试结果不支持当前排序，应重回 concept-brief 修订优先级。

- Lead：[[bathtub-filter-kes-concept-brief-v1|Hybrid premium-but-disciplined tub-spout route]]
- Backup：[[bathtub-filter-kes-concept-brief-v1|Narrow chlorine-focused technically disciplined route]]
- Conditional reserve only：soft-hanging ritual route

### 输出物
- 每条 surviving route 各 1 页简要 concept summary
- 每条被放弃路线各 1 份 rejection note（可短）

## Workstream 2 — competitor public evidence integration（竞品公开资料补全）
### 目标
把 bathtub active 10 ASIN 官方页面、Amazon PDP 快照、公开价格/销量信号、公开 claim、可见结构/安装线索整理成可复用的竞品证据层。

### 2026-06-02 口径修正
- 不做样品采购任务，不生成采购优先级或采购预算。
- 公开网页只能补“页面可见信息”：定位、价格、销量信号、claim、安装描述、公开图片/说明书线索。
- 实物拆解结论不能由网页补齐；必须来自已有样品、开箱照片、人工拆解记录或测试记录。
- 真实退货率、退款原因、客服工单、Brand Registry / DTC 后台数据不作为公开补资料任务。

### 2026-06-03 口径修正
- Filterbaby `B0FNVDJRSQ` 是 shower filter / showerhead inline 产品，已拆到 [[../shower-filter/shower-filter]]。
- Bathtub-filter active competitor set 改为 10 ASIN；Filterbaby 不再进入 bathtub 的价格均值、安装对象矩阵、claim 准确率排名或 tub-spout fit 判断。

### 覆盖对象
- Canopy `B0GFQ1JRSK`：premium baby tub-spout / DTC claim benchmark。
- Crystal Quest `B008A4AG2U`：classic bath-ball / technical legacy benchmark。
- Santevia `B0742KFY9R`：soft-hanging / cotton bath ritual benchmark。
- 低价白牌 `B0CXT5KL5Z`、`B0D3X39378`、`B0FL24SLM5`、`B0FT7R9ZQ9`、`B0G5NZBW6W`、`B0GKT5CHYL`：PDP-only claim / price / fit-risk benchmark。
- Tubo `B0DTQ8H23D`：premium-ish baby/tub positioning benchmark；公开资料不足时只标 PDP 线索。

### 输出物
- [[bathtub-filter-11-asin-public-competitor-evidence-2026-06-02]]（legacy 文件名；bathtub active 10 ASIN 公开竞品资料补充）
- public claim / installation / structure signal matrix（公开 claim、安装、结构线索矩阵）
- evidence boundary list（哪些信息不能由网页替代）
- unresolved teardown/test fields（需要已有实物或人工记录才能补的字段）

## Workstream 3 — validation test setup（验证测试搭建）
### 目标
把 validation protocol 变成真实可运行的内部测试。

### 必做模块
- normal-flow chlorine reduction（正常流速下的氯 reduction 表现）
- reduced-flow comparison（降流对比）
- fit matrix across tub-spout types（不同浴缸出水口类型的适配矩阵）
- leak / overflow / repeated-use stability（漏水 / 溢流 / 重复使用稳定性）
- refill / maintenance burden（耗材更换与维护负担）

### 输出物
- test sheet template（测试记录模板）
- pass/fail thresholds（通过 / 失败阈值）
- equipment / reagent list（设备与试剂清单，如需要）

## Workstream 4 — claim and language guardrails（宣称与语言边界）
### 目标
防止 KES 在这个品类里滑向最危险的市场表达。

### Non-negotiables（不可妥协项）
- no eczema-improvement promise（不做“改善湿疹”承诺）
- no broad contaminant fantasy stack without proof（无证据不做泛化污染物去除大礼包）
- no vague universal-fit promise（不做模糊的 universal fit 承诺）
- no baby-safety implication beyond substantiated boundary（不做超出证据边界的婴儿安全暗示）

### 输出物
- allowed claims（允许宣称）
- conditional claims（条件宣称）
- banned claims（禁用宣称）

## Workstream 5 — decision checkpoint（决策关口）
### 目标
在公开竞品资料复盘与验证测试准备之后，强制做一次明确决策。当前已有 S-01 non-diverter 周长边界正向记录、2 组 RV / mobile-home center-set / valve-diverter faucet 正向适配样本，以及 freestanding tub filler 非瀑布出水 2 kg 承重记录，但 E 层安装/兼容性仍不能关闭，直到更多 spout 类型、动态注水、漏水/溢流和重复使用稳定性记录补齐。

### 决策选项
- continue concept development（继续概念开发）
- pause pending better proof（暂停，等待更强证据）
- archive as non-priority adjacency（作为非优先邻近品类归档）

### 触发条件
在通过 [[bathtub-filter-test-gating-checklist-for-kes]] 前，不应进入真正的 product GO 逻辑。

## 建议执行顺序
1. freeze route scope（冻结路线范围）
2. integrate active bathtub 10-ASIN public competitor evidence（整理 bathtub active 10 ASIN 公开竞品资料）
3. set up validation protocol（搭建验证协议）
4. run flow / fit / leak tests if real samples or existing records are available（如已有实物或记录，再执行流速 / 适配 / 漏水测试）
5. compare complaint risk vs observed behavior（把评论风险与真实表现对照）
6. update concept brief and go/no-go memo（更新概念简报与 go/no-go 结论）
7. make explicit continue / pause / archive decision（做明确继续 / 暂停 / 归档决策）

## 当前管理判断
这题已经成熟到可以进入 **structured diligence（结构化尽调）**。

但它仍然**没有成熟到可直接支持 launch conviction（直接支持上市信心）**。

## Obsidian links
- [[bathtub-filter]]
- [[bathtub-filter-final-executive-summary-2026-04-14]]
- [[bathtub-filter-kes-concept-brief-v1]]
- [[bathtub-filter-test-gating-checklist-for-kes]]
- [[bathtub-filter-kes-rd-and-validation-roadmap]]
- [[bathtub-filter-kes-route-elimination-memo-v1]]
- [[bathtub-filter-validation-testing-protocol]]
- [[bathtub-filter-kes-go-no-go-memo-v1]]
- [[bathtub-filter-11-asin-public-competitor-evidence-2026-06-02]]

## Sources
- [[bathtub-filter-final-executive-summary-2026-04-14]]
- [[bathtub-filter-kes-concept-brief-v1]]
- [[bathtub-filter-test-gating-checklist-for-kes]]
- [[bathtub-filter-kes-route-elimination-memo-v1]]
- [[bathtub-filter-validation-testing-protocol]]
- [[bathtub-filter-11-asin-public-competitor-evidence-2026-06-02]]
