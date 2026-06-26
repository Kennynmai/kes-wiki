---
type: product
status: draft
owner: strategy
created: 2026-04-17
updated: 2026-06-15
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, kes, claims, compliance, marketing, version-a, clean-formula, diagnosis-kit]
source_count: 4
review_cycle: monthly
verification_status: spot-checked
related:
  - ./bathtub-filter-claim-risk-audit-v2.md
  - ./bathtub-filter-evidence-matrix.md
  - ./bathtub-filter-compliance-framework-and-evidence-boundaries.md
  - ./bathtub-filter-kes-positioning-and-problem-layer-decision-2026-06-15.md
  - ./bathtub-filter-kes-clean-formula-emotional-positioning.md
  - ./bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md
  - ./bathtub-filter-chloramine-media-research.md
  - ../../source-summaries/bathtub-filter-kes-internal-product-materials-2026-04-17.md
  - ../../source-summaries/bathtub-filter-onlyzone-supplier-material-evidence-2026-04-17.md
---

# 浴缸过滤器宣称台账

## Status note

**2026-04-17 更新：Version A 内部产品讲解文档到位后，Allowed / Conditional 区的 example wording 已从占位符填入 Version A 实际语言。**

禁区仍保持不变（非谈判性）。Version B / C（氯胺城市 / 软水器下游 / well water / 仪式浸浴）的 claim wording 仍 pending。Workstream 2 的竞品样品差异化审核，仍可在 Version A 的 wording 上做二次优化（确保不被竞品语言占领），但不再阻塞首次使用。

**2026-06-15 操作化更新**：把本轮战略产出（clean-formula 定位、水质自测套件/模块化获客引擎、氯胺 V1.5 证据）产生的 claim 决策归并进本表——见文末 **「2026-06-15 操作化增补」** 段（透明/clean-formula、自测套件、模块目录、氯胺 V1.5、诚实劝退、**表面→claim 映射**）。两处对既有表的修改：① Banned 区氯胺行从「V1 一律禁」改为「**V1 禁 / V1.5 conditional**」；② Conditional 区 fast-flow 行接上 [25L/min 测试 spec](./bathtub-filter-25lpm-dechlorination-bench-test-spec.md) 的通过门槛。

---

## Claim categories

基于 claim-risk-audit-v2 和 evidence-matrix（宣称阶梯）识别出的 7 个主要宣称类别：

1. **Chlorine reduction** — 游离氯去除，当前最可防守的技术宣称核心
2. **Sensory / comfort benefit** — "浴水更柔和 / 更舒适"等感官层面表达，不带医疗结果含义
3. **Skin-comfort framing** — 针对敏感肌肤的非结果型 framing，需要与 eczema claim 严格区隔
4. **Baby / infant segment** — 针对婴儿洗澡场景的 framing，商业价值高但 trust burden 也最高
5. **Fit / compatibility** — 适配范围宣称，包括支持的 spout types 和明确的不支持说明
6. **Performance / testing** — 关于测试条件、测试结果和认证的宣称，需要清晰区分 certified vs tested vs media-credibility
7. **Environmental / sustainability** — 如有可替换滤芯等，可能涉及的环保/可持续相关表达
8. **Transparency / clean-formula** *(2026-06-15 新增)* — 「看得见真料 / 读得懂配方」透明叙事，及主动 disclaim 疗效的承重句
9. **Self-diagnosis / test-kit** *(2026-06-15 新增)* — 「测你家的水」自测套件、读卡处方、精度与诚实边界
10. **Modular media catalog** *(2026-06-15 新增)* — 各滤材模块（阻垢/井水 KDF85/强化物理层/氯胺配置）各自有界的 cross-sell 宣称

---

## Allowed claim zone (structure)

这些宣称类别在满足对应证据要求后可以使用。**"Example wording" 列当前为占位符，等待 Workstream 2 竞品研究后填入。**

| Claim category | Allowed | Example wording (Version A) | Evidence requirement | Notes |
|---|---|---|---|---|
| Positioning (category-level) | Yes — **leading** with this | "This is not a water purifier. It does not target TDS reduction. It is an end-stage harm-reduction module for the bath-fill scenario." | Verbatim from Doc 1 positioning statement; no efficacy claim embedded | Must appear on every customer-facing surface (page, pack, manual, rep script) to pre-empt "does it drop TDS?" objection |
| Chlorine reduction | Yes — with precision | "Fresh-filter, best-experience segment: **≥99% system-total chlorine reduction** at 15 L/min bath-fill flow." / "System-total chlorine reduction follows a posted curve over the filter life (99% → 95% → 90% → 80% → <50% replacement trigger)." | Internal life model at 130 g CaSO₃ + η=0.9 scaling (see [[bathtub-filter-media-efficacy-at-bath-conditions]] Section 9); **"free chlorine" must be specified — NOT "total chlorine" or "chloramine"**; flow rate and "fresh-filter / best-experience segment" qualifiers are non-optional | KPI is system-total (KDF × CaSO₃ chain), not single-media; must not re-use this wording for chloramine markets |
| Verification-by-user | Yes — with physical tool | "Verify with the included chlorine test strip: compare before- and after-filter water. Do not use a TDS pen — this product does not target TDS." | Test strip included in pack; FAQ explicitly steers user away from TDS pen as verification tool | This is a trust-building anchor unique to Version A vs. competitors who avoid user verification |
| Replacement-trigger language | Yes — with posted schedule | "Replace when system-total chlorine reduction drops to ~90% (soft trigger) / ~80% (strong trigger) / ~50% (mandatory)." / "At 2 ppm tap chlorine, 3 baths/week: soft trigger ≈ 113 baths; mandatory ≈ 143 baths (~1 year). At 1 ppm tap: approximately 2× lifespan." | Internal life model (see [[bathtub-filter-media-efficacy-at-bath-conditions]] Section 9) | Use gallons / baths / weeks — **do not convert to months** (per Doc 1 口径决策); add "your local tap chlorine affects lifespan — verify with test strip" |
| Sensory / comfort benefit | Yes — with non-medical framing | "Bath-water without the pool smell." / "Gentler-feeling bath-fill." / "A cleaner bath starting experience." | Stays in sensory/comfort language; no therapeutic outcome implied | Verbatim guardrail from Doc 1 sales script: "feels different" OK; "improves your skin" NOT OK |
| Media transparency | Yes — with specific framing | "Layered media: PP cotton → KDF55 (110 g) → CaSO3 (130 g). Each layer replaceable separately." / "KDF55 as end-stage safety layer and biofilm-inhibition layer. CaSO3 as primary free-chlorine reduction KPI." | Doc 1 media stack spec | Explicitly reframes KDF as safety-layer, not "free-chlorine reduction main media" — reduces "KDF = cure-all" misread |
| Fit / compatibility | Yes — with explicit scope | "Designed for standard US tub spouts 18–25 L/min; adjustable TPU strap fits most spout diameters; no-overflow envelope up to 35 L/min." | Internal flow-overflow test Doc 4; supported-spout matrix needs external sample sweep before launch (see [[bathtub-filter-supported-spout-matrix]]) | Every compatibility claim must ship with a "not supported" boundary (e.g., "swan-neck spouts without a pull-diverter may need aftermarket strap") |
| Performance / testing | Yes — with test/certified distinction | "KDF55 media is backed by supplier NSF/ANSI 42 material-level listing. CaSO3 has NSF/ANSI 177-protocol free-chlorine reference testing, but CaSO3 itself is not NSF-certified and the finished product is not NSF-certified. Verify with the included free-chlorine test strip." | Doc 1 standards-口径; supplier cert docs on hand | See compliance-framework-and-evidence-boundaries for the 5 common misreads to avoid; this wording is **deliberately conservative** — it does not claim NSF certification of CaSO3 or the finished product |
| Environmental / sustainability | Conditional — only if substantiated | TBD — pending replaceable-cartridge final design + supply-chain sourcing verification | Requires specific data on cartridge lifespan, material composition, and disposal or recycling pathway | Do not use vague "eco" language without specific backing |

---

## Conditional claim zone (structure)

这些宣称在特定条件或免责说明下可以考虑使用，但需要更高审慎度，且必须在使用前通过内部 evidence review。**"Example wording" 列待 WS2 填入。**

| Claim category | Condition required | Example wording (Version A) | Evidence requirement | Notes |
|---|---|---|---|---|
| Skin-comfort framing (sensitive skin) | Must not imply eczema improvement or clinical outcome; must stay in "may be gentler for" or "designed with sensitive-skin users in mind" territory | "Designed with sensitive-skin bathers in mind." / "May be gentler for users who find highly-chlorinated tap water drying." (Never: "improves eczema" / "heals your skin" / "clinical results for sensitive skin") | EPA literature + Seki 2003 + Danby 2018 support that chlorine ≥ 0.5 mg/L affects compromised skin; this supports the problem framing, **not** finished-product efficacy | The distinction between "for sensitive-skin users" vs "improves sensitive skin" is non-negotiable. Doc 1 FAQ verbatim: do not market as eczema product |
| Baby / infant framing | Only if product has clear scope definition, no medical safety implication, and no "baby-safe" equivalents without substantiation | "Filters the bath-water before it reaches your tub." / "Many families use a bath filter for chlorine-sensitive bathtime routines." (Never: "safe for babies" / "safe for newborns" / "pediatrician-approved") | Doc 2 review evidence: infant / small-child segment is the single largest positive review cluster across 5 ASINs — segment relevance is real, safety-claim burden is not met | Premium pricing will increase scrutiny on any baby-adjacent claim; do not write "baby-safe" without explicit evidence base |
| Head-to-head with mixed-media competitors | With technical explanation, non-disparaging | "Unlike mixed-bead products, Version A uses strict layered media (PP cotton → KDF55 → CaSO3) with an internal flow-diversion module. This prevents channeling, prevents media cross-reaction, and lets you replace each layer separately." | Doc 5 diversion-module test + Doc 4 flow-overflow test + Doc 2 competitor complaint teardown | Safe framing because it explains a technical design choice, not disparages a competitor; do not name specific competitor ASINs in marketing copy |
| Fast-flow chlorine performance（含 25 L/min 卖点） | Only if independently replicated for the specific KES product at the stated flow rate **per [25L/min 测试 spec](./bathtub-filter-25lpm-dechlorination-bench-test-spec.md) Gate 1** | 公开文案的去氯数字**必须用第三方 DPD 实测值**回填，不得用内部模型的 ≥92%@25 L/min（那是 5 ppm 系统总氯比色单测） | spec §4 通过门槛：25 L/min、真实 2 ppm、新芯 **≥85%** 且 25→27 斜率平缓。**未达门槛前 25 L/min 不上首屏**（[执行路线图](./bathtub-filter-kes-v1-execution-roadmap-2026-06-15.md) Gate 1） | 这是 clean-formula「测得到」首要价值的硬证据来源——口径必须如实，否则就成了我们批 FilterBaby 的放大 |
| Reduced water irritation | Only with careful framing — comfort framing acceptable, skin-barrier claim is not | "Less chlorine in your bath water means less chlorine contacting your skin — that's the comfort difference many bathers notice." (Never: "restores skin barrier" / "prevents eczema flares") | Chlorine / bathing / skin-barrier evidence supports cautious problem framing; does not support product-level skin outcome promise | Use 3rd-level claim evidence ladder language (education framing), not 5th-level (clinical result language) — see [[bathtub-filter-evidence-matrix]] Section 9 |
| Supplier material credibility (NSF/ANSI 42) | Only as a media/material-level statement, never as a finished-product certification | "KDF55 has supplier-side NSF/ANSI 42 support via Zibo Onlyzone, Cert# C0843384-01. The finished KES product is not itself NSF-certified." | [[bathtub-filter-evidence-bibliography]] E1 (NSF cert C0843384-01, 2025-04-10) | Must always include the "finished product is not itself NSF-certified" disclaimer — otherwise the claim reads as a product cert |
| Supplier material safety (EU food-contact) | Only as a media-level statement about extractable heavy metals | "KDF55 media tested compliant with EU food-contact standards (CM/RES 2013/9 + Regulation 1935/2004 Ch. III) — 22 heavy metals below maximum limits, sensory rating 0 / 4 for taste and odor." | [[bathtub-filter-evidence-bibliography]] E2 (TÜV SÜD 721682290C, 2023-07-13) | Supports material-safety credibility; do not transfer this to finished-product food-contact claim without separate testing |
| KDF bacteriostatic property (biofilm inhibition) | Only as an internal-column property, never as a bath-water kill claim | "KDF media supports biofilm inhibition inside the filter column. In a 24-hour dynamic-contact test (ASTM E 2149-2020) against *S. aureus*, reduction exceeded 99.99%." | [[bathtub-filter-evidence-bibliography]] E3 (Guangzhou Institute of Microbiology WJ20221264, 2022-04-20; CNAS L0823) | **Must NOT claim** "kills bacteria in your bath water" — the test is 24h static; bath EBCT is 0.48–0.95 s (5-6 orders of magnitude shorter). Positioning must stay column-internal |
| KDF lead-reduction capability | Only as a material-level static-test reference; never as a "product removes X% lead" claim | "KDF55 media documented 92.6% lead reduction in a 24-hour static soak test (FSDA M250616-30, 2025-06-23)." | [[bathtub-filter-evidence-bibliography]] E4 (Zhejiang Fries FSDA M250616-30) | **High misread risk** — customers may assume this applies to bath-fill conditions. Recommend avoiding this claim in marketing copy entirely for V1; keep it as a specification-sheet line only |
| Life-model / free-chlorine reduction claim traceability | Only with full caveat chain | "Version A life model (system-total free-chlorine reduction ≥99% → ≥50% over ~25,467 L at 2 ppm free chlorine) scales from a supplier reference report (40g / 0.5-1mm CaSO3 / 8 L/min / 2 ppm; ZONET20251113001, 2025-12-26) by a factor of 3.25× (mass ratio) × 0.9 (efficiency)." | [[bathtub-filter-evidence-bibliography]] E5 + [[bathtub-filter-media-efficacy-at-bath-conditions]] Section 9 | Supplier internal lab; particle-size delta (0.5–1 mm reference → 3–4 mm production) not separately resolved. For external marketing copy, prefer the user-facing language "verify with included free-chlorine test strip" rather than quoting the numeric curve directly |

---

## Banned claim zone

**这个区域现在就可以执行。** 禁区来自 go/no-go memo、execution plan、和 claim-risk-audit，在 WS2 完成之前不会改变。

以下类别的宣称语言对 KES 是**不可妥协的禁区（non-negotiable forbidden zones）**：

| Banned claim type | Why banned | Risk level |
|---|---|---|
| Eczema improvement / eczema benefit | "改善湿疹" / "缓解湿疹症状" / "减少湿疹发作" — finished-product efficacy for eczema has no credible evidence base in this category at realistic conditions | Very high — trust collapse + regulatory exposure |
| Broad contaminant stack without proof | Claiming removal of heavy metals, VOCs, PFAS, pesticides, bacteria, viruses, or "hundreds of contaminants" without specific, independent test data per contaminant | Very high — false advertising risk |
| Universal-fit / "fits all tubs" | Any claim that implies compatibility with all or virtually all tub types without a tested and bounded spout matrix | High — support burden, return volume, review collapse |
| Baby-safety implication without substantiation | "Safe for babies" / "safe for newborns" / "mom-approved for infant bathing" style claims that imply safety from harmful substances without specific evidence | Very high — regulatory and liability exposure |
| Clinical language without clinical-grade backing | "Clinically proven" / "clinically tested to improve skin" / "doctor-recommended for eczema-prone skin" without the specific clinical evidence base these phrases imply | Very high — FTC / consumer protection risk |
| Hard-water softening claims | Implying that a compact bath filter meaningfully softens hard water — current evidence does not support compact bath filters achieving clinically or practically meaningful water softening | High — evidence does not support this for compact filter form factors |
| Chloramine removal claims **for V1 (free-chlorine media)** | V1 媒体（KDF55+CaSO₃）对氯胺基本无效，宣称氯胺去除不可防守。**注：V1.5 氯胺配置（催化炭+抗坏血酸钠浸泡）有界 claim 已移入 Conditional——见「2026-06-15 操作化增补」§B。** | High — chemistry mismatch；V1 仍为禁区 |
| Carbon / no-pre-rinse / no-carbon-dust claims for V1 | V1 当前滤材为 PP棉 + KDF55 110g + CaSO3 130g，不含活性炭；"no pre-rinse required"、"no carbon dust"、"acid-washed coconut-shell carbon" 属于其他含碳版本资料，不纳入 V1 卖点 | Medium-high — wrong-version claim / material mismatch |
| Implied medical treatment or disease prevention | Any language that positions the product as treating, preventing, or managing a health condition (including skin conditions, respiratory sensitivity, etc.) | Very high — drug/device regulatory threshold risk |

---

## 2026-06-15 操作化增补

> 本段把本轮战略产出的 claim 决策归并入表，覆盖既有 Version A 表未涵盖的新类别与新表面。优先级规则不变：**先查 Banned，再查 Conditional，最后 Allowed 也要核证据。**

### A. 新增 Allowed（满足证据要求即可用）

| Claim category | Allowed | Example wording | Evidence requirement | Notes |
|---|---|---|---|---|
| **Transparency / clean-formula** | Yes — **leading** | "See the media. The amount. The order. Clean is what you can see." / 「看得见的滤料，读得懂的配方。」 / "Copper-zinc you can see. Calcium sulfite you can see. No third thing you can't name." | 透明滤盒为真实可见结构；料名/料量与实物一致 | 这是首要价值的载体；**「可见」不得暗示「更有效」**——可见是 trust 钩子，efficacy 另由去氯实测支撑（防假设4陷阱） |
| **Clean-formula 承重 disclaim 句** | Yes — **必须保留** | "We won't tell you it 'treats' anything." / 「我们不替你下结论它能治好什么。」 | 无（这是 disclaim，本身降低风险） | **承重合规句**：主动 disclaim 疗效，守 A-10。出现在宣言/About/产品片；**编辑/法务不得为「更顺」删除**（见 [感性定位 §5.4](./bathtub-filter-kes-clean-formula-emotional-positioning.md)） |
| **Metal-first 料级叙事** | Yes — 料级/工程，非健康 | "Premium copper-zinc alloy media — not the cheap filler hiding behind opaque plastic." | KDF55 料级事实 | **仅料级/质感**；**不得**translate 成「去重金属保护皮肤」健康声称（无经皮证据） |
| **Self-diagnosis / 「测你家的水」** | Yes — with precision boundary | "Find out what's in your water — so you pick the right media. A quick guide, not a lab test." / 「先测你家的水，帮你选对组合。」 | ZIP→CCR（类型，权威）+ 多垫试纸（浓度/硬度，粗筛） | 精度如实「粗筛指路 ≠ 检测危害」；类型判定以 ZIP 为准，试纸总氯−游离氯只作 flag（见 [获客引擎 §二](./bathtub-filter-kes-water-diagnosis-kit-and-modular-acquisition-engine.md)） |
| **Honest disqualification（诚实劝退）** | Yes — **必须做** | "Your city uses chloramine — V1 isn't for your water yet. Leave your email and we'll tell you when the chloramine version ships." / 高铁/软化/杀菌等能力外明说不适合 | 水务图谱 + 模块边界 | 不卖错 = clean-formula 信任资产；把能力外坦白做成承诺 |

### B. 新增 Conditional（条件满足 + evidence review 后用）

| Claim category | Condition required | Example wording | Evidence requirement | Notes |
|---|---|---|---|---|
| **Chloramine reduction — V1.5 配置 only** | 仅限催化炭芯 + 抗坏血酸钠浸泡件配置；**禁「fast / instant / 秒解」**；按 4–8 分钟规划；须氯胺专属台架 | "Reduces combined chlorine (chloramine) during fill and soak — give it a few minutes." / 「注水+浸泡阶段中和氯胺。」 | Catalytic carbon = Kochany 2008 (Tier 1) + EBCT 数据；ascorbate bath = SFPUC + AWWA C655；接触时间 4–8 min（[氯胺证据页](./bathtub-filter-chloramine-media-research.md)） | **禁**：单芯全除氯胺 / NSF 177 支持氯胺 / 「快速」。验证须用**总氯试纸**，并提示抗坏血酸对比色法干扰的测量时机 |
| **阻垢 adjunct（anti-scale）** | 仅设备防垢，非软化非护肤 | "Helps protect your tub and fixtures from scale buildup. **It does not soften your water.**" | 阻垢机理（sequestration）；非硬度去除 | **承重 disclaim**「不软化」必须随行；不得侵占去游离氯主媒体逻辑（媒体方案页边界） |
| **井水 KDF85 模块** | 仅低中度铁/H₂S/味；高铁(>2–3ppm)劝退 | "Targets iron / sulfur-related bath odor and rust nuisance (low-to-moderate)." | KDF85 机理；nuisance 级 | **禁**：杀菌/除砷/硝酸盐/铀/高铁全屋替代/软化 |
| **强化物理层（PP）** | 颗粒/沉积，非主过滤 KPI | "Extra sediment layer for particulate-heavy water." | 物理拦截 | 不得当主去污 KPI 讲 |
| **诊断报告卡 / referral 卡个性化结论** | 继承全部红线 | "Your water: free-chlorine, very hard. Recommended: free-chlorine reduction core + anti-scale." | ZIP+试纸诊断 | 报告卡是对外表面，**同样禁 toxin-panic / 健康声称 / 软化承诺** |

### C. 新增 Banned

| Banned claim type | Why banned | Risk |
|---|---|---|
| 诊断结果导向 **toxin-panic / 健康恐吓** | 「你的水有毒/伤害你宝宝」——读数只说水的类型/产品适配，不说危害健康 | Very high |
| **TDS 笔 / 铅试纸**作为验证或卖点 | TDS 非氯非硬度（伪精确）；铅试纸低浓度不可靠且非我们声称 | High（clean-washing 反噬 + 误导） |
| 氯胺「**快速/秒解**」 | AWWARF/SFPUC 证据为 4–8 分钟（充分混合的亚分钟为单次现场、有比色干扰、未重复，不可作承诺） | High |
| 「clean / 干净」暗示去有害物=**治皮肤/健康** | clean 讲透明与料级诚实，非 efficacy | High |

### D. 表面 → 适用 claim 映射（按客户表面查护栏）

| 客户表面 | 主用 claim 区 | 必带护栏/承重句 |
|---|---|---|
| 首页 Hero / 首屏 | Transparency + Chlorine reduction（数字待 Gate 1） | 25 L/min 数字未坐实不上；「可见≠有效」分开讲 |
| About / 品牌片 | Clean-formula 宣言 | **「我们不替你下结论它能治什么」承重句必在** |
| PDP 产品页 | Chlorine reduction（精度）+ Media transparency + Fit + Performance/testing | 「free chlorine」「fresh-filter/best-experience」「15 L/min」限定词不可删；成品不冒认 NSF |
| 诊断报告卡 / 试纸读卡 | Self-diagnosis + 模块处方 | 精度如实；阻垢「不软化」；toxin-panic 禁 |
| Referral 卡 | 个性化诊断结论 | 同报告卡红线；不刷屏不绑夸大 |
| 包装/说明书 | Replacement-trigger + Verification-by-user + 氯胺浸泡时机 | 用 baths/gallons 不用 months；总氯试纸 + 抗坏血酸干扰时机提示 |
| 广告 | Sensory/comfort + Transparency | 禁 eczema/baby-safe/scarcity；禁 best-value/cheapest |

---

## How to use this register

**For marketing and product copywriting:**

1. **Check the banned zone first.** If a draft claim matches any banned category, remove or rewrite before review — these are not negotiable regardless of market pressure.
2. **Check the conditional zone second.** If a claim falls in the conditional zone, verify the stated condition is met and documented before use.
3. **For allowed claims, confirm evidence requirement is satisfied.** "Allowed" means structurally safe — it does not mean "usable without checking." The evidence requirement column must be ticked off per claim.
4. **Version A example wording is now usable but still pending WS2 competitive-language optimization.** First-pass wording is drawn from Doc 1 (Version A product explanation 2026-02); WS2 competitor sample review should sharpen differentiation without changing meaning.
5. **The chlorine-reduction wording is bounded by "fresh-filter, best-experience segment" and "at 15 L/min."** Do not drop these qualifiers — the system-total reduction curve degrades with filter age, and degrades with flow rate.
6. **Version A scope is US urban municipal (free-chlorine) tap water only.** Any marketing surface that could be read globally or read as chloramine-city-compatible must be rewritten. See [[bathtub-filter-kes-concept-brief-v1]] for scope declaration.

**For internal research and strategy:**

- This register is a living document. Update it when: new test results are available, competitor samples reveal new language patterns, or a legal/compliance review changes the risk assessment on any category.
- The banned zone should be treated as unchangeable until there is a specific, documented rationale for reconsideration (e.g., new clinical evidence base, regulatory guidance change).

---

## Obsidian links

- [[bathtub-filter]]
- [[bathtub-filter-claim-risk-audit-v2]]
- [[bathtub-filter-compliance-framework-and-evidence-boundaries]]
- [[bathtub-filter-kes-next-step-execution-plan-v1]]
- [[bathtub-filter-kes-go-no-go-memo-v1]]
- [[bathtub-filter-evidence-matrix]]
- [[bathtub-filter-decision-register]]
- [[bathtub-filter-assumption-register]]
- [[bathtub-filter-supported-spout-matrix]]
