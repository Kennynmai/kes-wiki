---
type: product
status: draft
owner: compliance
created: 2026-07-21
updated: 2026-07-21
visibility: team
confidence: high
officiality: draft
domain: product
domains: [drinking-faucet, z506, compliance, nsf61, nsf372, cupc, p0, kes]
source_count: 6
review_cycle: weekly
verification_status: verified-internal
related:
  - ./drinking-faucet.md
  - ./drinking-faucet-z506-baseline-and-margin-audit.md
  - ../bathtub-filter/
---

# P0 合规敞口：Z506 在售 SKU 的饮用水认证记录缺失

**发现于 2026-07-21，是调查 air-gap 议题时的顺带发现，但优先级高于该议题本身。**
**本文档描述的是数据层面的发现，不等同于结论说产品未认证 —— 见「这份文档不主张什么」。**

## 一句话

实际在美国发货的 Z506 变体，在 `dim_sku_certification` 里**没有任何饮用水接触认证记录**；
而另一个配置的记录**自相矛盾到无法作为持证证据使用**。

## 发现 1：在售变体只有 cec 和 doe

实际发货的 `Z506LF-BK` / `-BS` / `-BZ` / `-PS`：

| cert_type | 有记录？ |
|---|---|
| `cec` | ✅ |
| `doe` | ✅ |
| **`nsf61`** | ❌ **无任何行** |
| **`nsf372`** | ❌ **无任何行** |
| **`cupc`** | ❌ **无任何行** |

`cec`（加州能效）和 `doe`（联邦能效）覆盖的是**流量/能效**，
不覆盖**材料浸出**和**无铅**。

## 发现 2：另一配置的记录自相矛盾

`Z506F18-*`（BK / BS / BZ / ORB / PS）**有** `nsf61` / `nsf372` / `cupc` 行，但每一行：

- `is_applicable = False`
- `is_filed = False`
- `admission_status = 未合规`
- `filing_no` = 空
- `expiry_date` = 空
- **却又** `status = '已获证'`

**`status='已获证'` 与其余五个字段直接冲突。** 这组记录不能作为真实持证的证据 ——
它既可能是"实际有证但数据没录"，也可能是"实际无证但状态字段被误填"。
**在人工核实纸质证书之前，两种可能都不能排除。**

## 发现 3：AB1953 在枚举里根本不存在

`dim_sku_certification.cert_type` 的现有枚举：

```
ce, cec, cupc, doe, domestic_water_efficiency_filing,
nsf372, nsf61, ukca, watersense
```

**没有 `ab1953`。** 平台合规 cheat sheet（`ui/docs/ops_category_config.md:221`）
把 `ab1953` 列为 `drinking_faucet` 的 **P0** 要求，但数据模型里无处可存。

实务上 AB1953 已被 NSF/ANSI 372 实质覆盖（联邦 SDWA "lead free" 同口径），
所以这**可能**不是真实敞口，而是**建模缺口** —— 但需要合规确认后再决定是补枚举还是补文档说明。

## 为什么这是 P0

美国市场对饮用水龙头的强制要求（外部已验证）：

| 要求 | 覆盖什么 |
|---|---|
| **NSF/ANSI/CAN 61** | 所有过水材料向饮用水的浸出 |
| **NSF/ANSI 372** | 过水表面加权平均铅含量 ≤0.25%，满足联邦 SDWA "lead free" |
| **cUPC / IAPMO R&T listing** | 压力、密封、结构耐久、流量；美加通用 |
| **CA AB1953 / Prop 65** | 州级铅限值与警示义务 |

**北美所有示范管道规范都要求龙头经认可的第三方机构列名认证，这不是可选项。**

KES 自己的研发规格书（`data/product_design_params_dingtalk/full_md/厨房/厨房龙头/净水龙头配置文档.md`）
本身就列明了 cUPC 盾牌标 + ASME A112.18.1/CSA B125.1 + NSF/ANSI/CAN 61 (Q≤1) + NSF/ANSI 372。
**但同一份文档里写着一句悬而未决的话：「家浚：产品是否已经有认证？如果没有的话，只需要打流量标和 KES 标」** ——
说明写规格书时认证状态本身就没有定论。

## 这份文档不主张什么

**不主张 Z506 未经认证。** 数据缺失 ≠ 产品无证。可能的解释包括：

1. 已认证但 `dim_sku_certification` 未录入（**最可能**）
2. 认证挂在工厂或另一料号下，未映射到销售 SKU
3. 确实未认证

**在核实之前不要对外做任何合规声明，也不要据此下架或停售。**

## 建议动作

| # | 动作 | 负责 | 产出 |
|---|---|---|---|
| 1 | 向工厂 / 供应商索取 Z506 的 NSF61、NSF372、cUPC 证书原件与列名编号 | 采购 / SCM | 证书 PDF + listing number |
| 2 | 用列名编号在 IAPMO R&T、NSF、WQA 的公开数据库反查有效性与到期日 | 合规 | 核验截图 |
| 3 | 核实证书覆盖的料号是 `Z506LF-*` 还是 `Z506F18-*`，两者是否同一物料 | 研发 | 料号对应关系 |
| 4 | 按核实结果回填 `dim_sku_certification`，并修正 `Z506F18-*` 的矛盾字段 | 平台 | 数据订正 |
| 5 | 与合规确认 `ab1953` 是补枚举还是文档说明 NSF372 已覆盖 | 合规 | 决议 |
| 6 | 若第 1 步取不到证书 → 升级为停售评估 | 管理层 | 决策 |
| 7 | 检查同 Z5 组其他 SPU（Z504 / Z507）是否有同样问题 | 平台 | 排查报告 |

**第 1 步取不到证书是唯一的真实红线。** 其余都是数据治理问题。

## 可复用资产

`../bathtub-filter/` 目录下已有完整的北美水接触认证方法论，**不要重跑**：

- `bathtub-filter-certification-and-testing-pathways.md`
- `bathtub-filter-certification-cost-and-timeline-estimates.md`
- `bathtub-filter-certification-authority-tiers-and-workflow.md`
- `bathtub-filter-cross-jurisdiction-standards-map.md`
- `bathtub-filter-california-prop65-investigation-and-response.md`

⚠️ 认证费用：IAPMO R&T、NSF、WQA **均不公开报价单**，需直接询价。
网上流传的 "$100k–$200k" 是净水**系统**性能认证（NSF 42/53/58）的数字，
**不适用于龙头，不要拿去做预算。**
