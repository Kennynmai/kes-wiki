# Log — KES Company Wiki

Use one heading per meaningful action.

Example:
## [2026-04-06] ingest | Japan market entry report
- source: raw/markets/japan/report.pdf
- updated: wiki/markets/japan.md; wiki/projects/japan-market-entry.md
- status: pending-owner-review
- notes: short summary of what changed

## [2026-04-17] cleanup | bathtub-filter cluster — MT 噪音重写 + superseded stub + 归档
- source: 本次 pass 无新来源；基于 cluster 现有内容
- updated: wiki/products/bathtub-filter/bathtub-filter-normal-flow-vs-reduced-flow-evidence-table.md（转为 superseded stub 指向 media-efficacy）；wiki/products/bathtub-filter/bathtub-filter-cluster-cleanup-note-2026-04-14.md（frontmatter 标记 archived）；wiki/products/bathtub-filter/bathtub-filter-brand-operating-matrix-v2.md（MT 噪音整页重写）；wiki/products/bathtub-filter/bathtub-filter-pricing-refill-flow-fit-table-v2.md（targeted 清理标题 + 归档链接指向）；wiki/products/bathtub-filter/bathtub-filter-kes-product-architecture-hypotheses.md（下半"原始假设记录"6 条重写）；wiki/products/bathtub-filter/bathtub-filter-product-forms.md（整页重写）；log.md；dashboards/recent-updates.md
- status: done
- notes: |
  确立 cluster 内"中文正文 + brand / 专业术语保留英文"的 style 标准。处理两类问题：
  (1) **MT 噪音重写**：brand-operating-matrix-v2 / kes-product-architecture-hypotheses / product-forms 三页有明显机翻残留（"表格明" × N、"（review）" 插入中文句中、"纯商品沐浴球克隆" / "飞行员" / "长江语言" 等破句）。pricing-refill-flow-fit-table-v2 只做标题 + sources 的 targeted 清理。原样保留每页的 structure、table、argument——只修语言。
  (2) **superseded / archive**：normal-flow-vs-reduced-flow-evidence-table（~25 inbound links）转为 stub 留在原路径，frontmatter 标 archived + superseded_by，body 只剩索引段——保持链接不破；cluster-cleanup-note-2026-04-14 标 archived（一次性维护日志）。structure-audit-and-link-maintenance-2026-04-13 此前已 archived，本轮 skip。
  遗留：cluster 内应该还有更多"中文正文 + 英文术语"的 style 偏差，但本轮只修列 A 清单里 explicit MT 的 4 页 + 2 页结构处理。更深度的风格统一留给后续按需 trigger。

## [2026-04-17] ingest | bathtub filter — Onlyzone 供应商材料证据（NSF 42 + EU food-contact + 抑菌 + 铅去除 + CaSO₃ reference）
- source: raw/products/bathtub-filter/2026-04-17-onlyzone-supplier-material-evidence-pass.md
- updated: wiki/source-summaries/bathtub-filter-onlyzone-supplier-material-evidence-2026-04-17.md (new); wiki/products/bathtub-filter/bathtub-filter-media-efficacy-at-bath-conditions.md; wiki/products/bathtub-filter/bathtub-filter-evidence-bibliography.md (新增 Section E × 5 条); wiki/products/bathtub-filter/bathtub-filter-claim-register.md (新增 6 条 conditional wording); wiki/products/bathtub-filter/bathtub-filter-certification-and-testing-pathways.md (新增 Section 1b supplier-level 现状); wiki/playbooks/bathtub-filter-validation-testing-protocol.md (Module 1 新增 ✅ 供应商侧行 + ⏳ 3-4mm 粒径复测); log.md; dashboards/recent-updates.md; ops/ingestion-registry.md; index.md
- status: done
- notes: |
  Strategist 提交 7 份 Zibo Onlyzone（宗立）供应商文件 + 3 份产品手册 (KDF-55 / CaSO₃ 球 / 长效碱性球)。Onlyzone 是 Version A 的单一媒体供应商。**最关键的单一发现**：文件 #5（CaSO₃ 余氯报告 ZONET20251113001，2025-12-26 完成）就是 Version A 寿命模型的 reference baseline。本次写入已对 η=0.9 × 3.25 = 2.925× 缩放规则做 4 档逐点验证：≥99% (1,190 × 2.925 = 3,481 L ✅) / ≥95% (6,042 × 2.925 = 17,673 L ✅) / ≥90% (6,880 × 2.925 = 20,124 L ✅) / ≥50% (8,707 × 2.925 = 25,467 L ✅) 全部命中 Version A 文档。η=0.9 从"未验证的假设"升级为"数学一致，物理假设仍未第三方复测"。材料级认证归档：KDF55 拿到 (a) NSF/ANSI 42 组织级 listing C0843384-01 (2025-04-10)、(b) EU food-contact TÜV SÜD 721682290C (2023-07-13) 22 重金属全过 + 感官 0/4、(c) ASTM E 2149-2020 抑菌 >99.99% (广州微生物研究所 WJ20221264, 2022-04-20, CNAS L0823)、(d) 静态浸泡 24h 铅去除 92.6% (浙江弗里斯 FSDA M250616-30, 2025-06-23)。claim-register 新增 6 条 conditional wording：全部以"material-level only / finished product is not itself certified"作为必须的限定语；铅去除标记为"高 misread 风险，建议 V1 不用于 marketing"。长效碱性球手册 (ZONE-PH-A03) 会提升 pH 与 TDS → 与 Version A "不以 TDS 为目标"定位冲突，记录为 Version A 不采用，未来若作为 mineral-enhancement SKU 必须独立声明。遗留 open gaps：3-4mm 生产粒径复测（供应商 reference 用 0.5–1mm，粒径差异对动力学的影响未单独处理）、第三方独立实验室复测（供应商内部实验室非 CNAS/ilac/NSF 独立）、finished-product 级别 NSF/WQA 认证（仍未启动）。

## [2026-04-17] ingest | bathtub filter — Version A 系统级去氯直测（5 mg/L 压力条件，测试日期 2026-03-20）
- source: raw/products/bathtub-filter/2026-04-17-kes-internal-chlorine-removal-bench-test.md (new)
- updated: wiki/playbooks/bathtub-filter-validation-testing-protocol.md (Module 1 新增 ✅ 行); wiki/products/bathtub-filter/bathtub-filter-technology-notes.md (EBCT 表下新增系统级直测段); wiki/products/bathtub-filter/bathtub-filter-media-efficacy-at-bath-conditions.md (新增 Section 9.5); log.md; dashboards/recent-updates.md
- status: done
- notes: |
  Strategist 提交了 Version A 首次系统级端到端去氯直测（测试实际进行日 2026-03-20，2026-04-17 交付 wiki）。被测架构与 Version A 一致（35 孔 PP 棉盘 15 mm + KDF55 110 g + CaSO₃ 130 g）；原水自由氯 5 mg/L（约 Section 9 寿命模型 2 ppm 基线的 2.5×，属压力条件）。四个压力 / 流速点（纸面照片 + 3 段 20260320.mp4 视频存档）：0.2 MPa / 16.5 L/min → 0.5 mg/L (~90%)；0.3 MPa / 21 L/min → 0.7 mg/L (~86%)；0.4 MPa / 27 L/min → 0.8 mg/L (~84%)；~0.5 MPa / 30 L/min → 1.5 mg/L (~70%)。测量方法：**氯试纸比色法**（非 DPD；中间读数 0.7 / 0.8 mg/L 为内插）。对照 Section 9 模型：方向一致（流速↑ → 去除↓）但绝对值偏低；27→30 L/min 斜率陡增（14pp vs. 模型 4pp）可能是两种成因叠加——EBCT 触及 breakthrough 和 / 或压力升到 ~0.5 MPa 引起床压实 / channeling（0.5 MPa 与 2024-11-07 overflow envelope 起步压力重合）。限制：单次测量无复测、试纸比色刻度粗、水温 / pH / TDS 未标、新旧滤芯累计通水量未标。**不能直接替换 Section 9 模型或用于 label claim**，但在 US 典型龙头流速 18–25 L/min 段仍保留 84–86% 去除，与 Section 9 寿命模型方向性闭环。Open items：需第三方 DPD 法在 2 ppm 基线 + 5 ppm 压力双条件复测，并在 27–30 L/min 段 **分别控制压力与流速以解耦两种成因**。

## [2026-04-17] ingest | bathtub filter — KES first-party internal product materials
- source: raw/products/bathtub-filter/2026-04-17-kes-internal-product-materials-pass.md
- updated: wiki/source-summaries/bathtub-filter-kes-internal-product-materials-2026-04-17.md (new); wiki/products/bathtub-filter/bathtub-filter-technology-notes.md; wiki/products/bathtub-filter/bathtub-filter-media-efficacy-at-bath-conditions.md; wiki/products/bathtub-filter/bathtub-filter-kes-product-architecture-hypotheses.md; wiki/products/bathtub-filter/bathtub-filter-kes-concept-brief-v1.md; wiki/products/bathtub-filter/bathtub-filter-claim-register.md; wiki/playbooks/bathtub-filter-validation-testing-protocol.md; ops/ingestion-registry.md; dashboards/recent-updates.md; index.md
- status: done
- notes: |
  Strategist delivered 5 internal KES documents + 1 product photo representing the actual Version A bathtub-filter product (urban municipal tap water, 38–42°C). Materials cover: (1) Version A sales/explanation doc Feb-2026 with positioning language, media stack (PP → CaSO₃ 130g → KDF55 110g → optional cavity), flow/EBCT/KDF-coefficient table (15/20/25/30 L/min → 43/32/26/21% KDF contribution), life model (130g CaSO₃ η=0.9 at 2ppm: ≥99% ≈ 3,481L / ≥50% mandatory-replace ≈ 25,467L ≈ ~1 year; at 1ppm ~2× lifespan), replacement triggers (90% soft / 80% strong / 50% mandatory), system-total formula 1−(1−KDF)(1−CaSO₃), 30-sec retail video script (whiteness → bubbles → chlorine strip → TDS pen for objection kill), verbatim FAQ positions; (2) 2024-02 market survey with 5-ASIN teardown (B008A4AG2U/B0742KFY9R/B08Y8GSVJS/B0C5D7NLC7/B0012045EO) and cost breakdown (urban MP $36.84, rural variant $77); (3) acid-washed coconut-shell carbon selection + 20240730–20240807 commissioning test (2-min pre-rinse resolves powder shed); (4) 2024-11-07 flow/overflow test (204g KDF + 45g carbon at 0.5 MPa / 38-40 L/min: zero filter disc = overflow; 1 mesh + 2 fiber discs = no overflow at 35 L/min; 3rd disc causes overflow — US typical spout 18-25 L/min is comfortably inside envelope); (5) 2025-10-22 diversion module test (no effect on KDF layer; essential on CaSO₃ layer to prevent center-crater erosion). Classification: internal-doc, high officiality impact (supersedes architecture-hypothesis framing; calibrates concept brief, technology notes, claim register, validation protocol). Limits noted: US-free-chlorine municipal only; chloramine and well-water scopes explicitly excluded; KDF coefficients and η=0.9 scaling lack external verification; Version A label implies Version B/C exist or are planned. Held at source-summary level pending strategist direction on 5 proposed downstream page updates.

## [2026-04-17] ingest | bathtub filter — full investigation deepening P1–P5（市场量化 + 竞品情报 + 氯胺证据 + 浴缸媒体效能 + 综合分析更新）
- source: 4 并行 web research agents（AmzChart / ShelfTrush / Amazon 产品页 / WaterFilterGuru / Aquasana & Leaf Home & AWWA 消费者调查 / NSF International / PubMed / 品牌 DTC 网站 / 行业技术文档）
- updated:
  - **新页面（4）：** bathtub-filter-market-size-and-demand-data.md; bathtub-filter-competitor-commercial-intelligence.md; bathtub-filter-media-efficacy-at-bath-conditions.md; bathtub-filter-chloramine-media-research.md（由 P4 agent 自动创建）
  - **更新页面：** technology-notes.md（实测流速数据 + 滤芯寿命比较）; evidence-bibliography.md（新增 A2 节，4 篇 Tier 1 氯胺化学文献）; index.md; obsidian-map.md
- status: done
- notes: |
  P1 市场量化关键发现：美国淋浴/浴缸过滤器市场约 $3.6 亿（2024），年增 7.2%；87% 美国人担心未过滤自来水；24% 将氯/氯胺列为首要关切（较 2020 年增 71%）；NSF 认证产品可支持 17% 溢价（NSF 2023 消费者调查）；TIME 2025 年度最佳发明两个奖项均为浴缸过滤器；**没有任何行业报告将浴缸过滤器单独追踪——品类定义白空间清晰**。

  P2 竞品情报关键发现：8 个品牌完整情报（ASIN / BSR / 评论数 / 定价 / 订阅结构）；Filterbaby 是品类商业表现最强的品牌（BSR T&HI #7,145 / 龙头过滤 #7，DTC 1,235 条评论 @4.8 星，10 个月内约 123 条/月）；Santevia 独立测试最佳（8.17/10，正常流速 100% 去除）但营销极弱；Tubo 营销最强但正常流速去除率 0%，且检测到铜渗出 405%；**品类内没有任何产品持有浴缸应用场景的 NSF 独立认证——这是 KES 最重要的产品白空间之一**；订阅模式正成为高端品牌（Canopy / Filterbaby）的标志；价格天花板已从 $20–30 移动至 $65–140。

  P4 氯胺证据关键发现（Tier 1 实验数据）：KDF-55 氯胺去除率仅 18.2%（Pure Water Gazette 测试）；KDF-85 仅 1.4%；亚硫酸钙在 pH > 7.5 下对氯胺基本无效（Yiin 1987，Tier 1）；催化活性炭有效但需 EBCT ≥4–5 分钟（Kochany 2008，Tier 1）；维生素 C 在短接触时间下无效（Basu 2011，Tier 1），但浴缸 4–8 分钟接触时间可实现完全去除（SFPUC 实测）；**NSF 177 明确要求产品在使用氯胺水时附带免责声明；NSF 42 是唯一可声称氯胺去除的认证路径**。

  P5 浴缸媒体效能关键发现：**最重要的逆直觉结论——浴缸注水低流速（0.3–0.8 GPM）对氯去除有利而非不利**；多数产品在正常流速（1–4 GPM）下去除率 0–50%，但在慢速（接近浴缸注水）下达到 85–100%（waterfilterguru 实测）；滤芯寿命：浴缸注水比淋浴消耗快 2–4 倍，以月数标注的淋浴滤芯寿命不适用于浴缸场景；KDF 在 37–40°C 下性能优于冷水；亚硫酸钙在热水下更稳定（溶出率更低）；**浴缸注水过滤在学术上是完全未被研究的应用场景——没有任何针对浴缸水龙头的行业技术标准**。

## [2026-04-17] ingest | bathtub filter — special water source types investigation
- source: targeted web research (EPA, USGS, CDC, PMC literature, WQA, NRDC, ARCSA, Hawaii DOH, USVI water quality studies)
- updated: wiki/products/bathtub-filter/bathtub-filter-water-source-types-guide.md (new); wiki/products/bathtub-filter/bathtub-filter-water-jurisdiction-demand-map.md; index.md; obsidian-map.md
- status: done
- notes: investigated 6 additional water source types beyond municipal chlorine/chloramine and private well water. Key findings: (1) MOST ACTIONABLE — whole-house softener households (14–22M US households): softener removes only hardness, chlorine/chloramine 100% preserved → bath filter highly relevant, best underserved segment; marketing hook: "your softener doesn't remove chlorine"; (2) rainwater harvesting (~20–100K mainland + 60K Hawaii Big Island): no chlorine, real risks are microbial/heavy metals/PAHs → standard bath filter irrelevant, do not market; (3) cistern/hauled water (150–500K incl. USVI): USVI study found E. coli 80%, Naegleria fowleri 30% of cisterns; no chlorine; standard bath filter irrelevant and potentially misleading/dangerous; (4) small disinfected community systems (~1.5–2M households): free chlorine, standard product works; 93% of EPA enforcement priority systems are small systems; (5) whole-house RO (~200–500K): near-zero chlorine, near-zero TDS, already ultra-pure → bath filter adds no value; (6) Puerto Rico (~1.1M housing units): free chlorine + elevated DBPs (THMs from tropical climate+chlorination) + lead risk → secondary market with stronger purchase motivation than most mainland cities. Exclusion zone clearly defined: rainwater/cistern/hauled/no-disinfection households must be excluded from product claims to avoid false safety implications.

## [2026-04-17] ingest | bathtub filter — private well water investigation
- source: targeted web research (EPA, CDC, USGS, PMC studies, Penn State Extension, Santé product data, NJ DEP)
- updated: wiki/products/bathtub-filter/bathtub-filter-well-water-research.md (new); wiki/products/bathtub-filter/bathtub-filter-water-jurisdiction-demand-map.md; wiki/products/bathtub-filter/bathtub-filter-disinfectant-types-and-media-guide.md; index.md; obsidian-map.md
- status: done
- notes: comprehensive new page on US private well water. Key findings: (1) scale — ~23M US households (~15% of population) on private wells; geographically concentrated in Northeast, Great Lakes, Southeast; skews rural/moderate-income/older vs. urban premium DTC demographic; (2) contaminants — 23% of wells exceed at least one health benchmark (USGS); 50% exceed at least one combined benchmark; top aesthetic/bath concerns are iron (32–57% of regional wells exceed 0.3 ppm SMCL), hydrogen sulfide (~20% of wells seasonally), hardness (groundwater typically harder than surface), pH (26% out of range, 83.8% too acidic); (3) well water has NO chlorine/chloramine — KDF-55 and calcium sulfite (the standard bath filter media) provide little value for well water users; (4) KDF-85 is the correct media for well water iron/H2S; effective below ~3 ppm iron; cartridges clog rapidly above 3 ppm; (5) compact bath filter viable for moderate iron (<3 ppm) and H2S odor complaints; cannot address hardness, bacteria (bacteriostatic only), arsenic, nitrate; (6) regulatory context: private wells excluded from EPA Safe Drinking Water Act entirely; homeowner solely responsible; only 22% of states require testing at property sale; most contamination is self-announcing (sensory) for aesthetic issues but invisible for health-level arsenic/nitrate/radon; (7) radon is underexploited claim space in Northeast — 65% of wells exceed proposed standard, 89% of waterborne radon cancer deaths are from inhalation during bathing/showering. Cross-reference notes added to water-jurisdiction-demand-map and disinfectant-types-and-media-guide marking their municipal-water-only scope.

## [2026-04-17] ingest | bathtub filter — disinfectant chemistry investigation
- source: targeted web research (NCBI, EPA, CDC, Aquatell, DC Water, Missouri DNR, TCEQ, industry technical sources)
- updated: wiki/products/bathtub-filter/bathtub-filter-disinfectant-types-and-media-guide.md (new); wiki/products/bathtub-filter/bathtub-filter-technology-notes.md; wiki/products/bathtub-filter/bathtub-filter-water-jurisdiction-demand-map.md; index.md; obsidian-map.md
- status: done
- notes: created new page documenting three distinct chlorine forms at tap (free chlorine HOCl/OCl⁻, monochloramine NH₂Cl, chlorine dioxide ClO₂) and their removal by each filter media type. Key operational findings: (1) calcium sulfite and KDF-55/85 are effective for free chlorine but have negligible effect on monochloramine (KDF-55 18.2%, KDF-85 1.4% in test data); (2) vitamin C works on both free chlorine and monochloramine but requires 4+ minutes contact time for chloramine — bath fill provides this, shower does not; (3) catalytic activated carbon is the best solid-media option for chloramine; (4) ~25–40% of chloramine utilities do annual seasonal free-chlorine switches (typically spring, 2–8 weeks); (5) NSF/ANSI 177 explicitly excludes chloramine from its test scope, requiring product disclaimer; (6) ClO₂ (affects ~12M Americans) is effectively removed by standard activated carbon. Misrepresentation risk matrix added covering 6 common false claims in the market. Cross-references added to technology-notes and water-jurisdiction pages.

## [2026-04-17] ingest | bathtub filter — patent / technology / academic research deepening
- source: targeted web research (PubMed, USGS, EPA, Aquatell, Google Patents, NSF, Wiley)
- updated: wiki/products/bathtub-filter/bathtub-filter-evidence-bibliography.md; wiki/products/bathtub-filter/bathtub-filter-evidence-matrix.md; wiki/products/bathtub-filter/bathtub-filter-water-jurisdiction-demand-map.md; wiki/products/bathtub-filter/bathtub-filter-technology-notes.md; wiki/products/bathtub-filter/bathtub-filter-certification-and-testing-pathways.md; wiki/products/bathtub-filter/bathtub-filter-patent-table.md; wiki/syntheses/bathtub-filter-patent-and-technical-landscape.md
- status: done
- notes: five substantive additions: (1) academic — 3 new studies added to bibliography (Danby 2018 TEWL+hard water n=80; Tanaka 2015 soft water TEWL reduction; Uchiyama 2021 mineral water vs tap TEWL); Seki 2003 updated with actual numbers (0.5 mg/L chlorine threshold in AD skin, which overlaps with normal US tap water 0.5–2.0 mg/L); Source #8 balneotherapy article confirmed and populated from secondary access; new TEWL evidence summary section added to evidence-matrix. (2) NSF/ANSI 177 scope — confirmed standard covers shower only (not bathtub spout), test conditions now documented (2.0 mg/L FAC, 50% min reduction, 40°C, ≥1.0 GPM, 80 psi); correct certification path for bath filter = NSF/ANSI 42 + 61 or WQA Gold Seal, not 177. (3) North America water geography — USGS hardness map data, state-level hardness rankings, EPA chlorine concentration range (0.5–2.0 mg/L typical), 100-city chloramine vs free-chlorine classification, best target markets identified (Las Vegas, Phoenix, Tucson, San Antonio, El Paso, Colorado Springs). (4) Patent IP landscape update — Canopy: possible design patent pending, no utility patents confirmed; Kinder/Tubo: no patents found; D1,034,899 bath ball filter design patent (2024) noted; DTC newcomers confirmed as non-patent-protected. (5) Evidence matrix: Section 1 updated with Seki 2003 numbers + US tap water concentration context; new Section 10 added with TEWL evidence table and product claim implications.

## [2026-04-17] maintain | bathtub filter consolidation — claim-evidence-ladder merge + structure-audit retirement
- source: internal pruning review
- updated: wiki/products/bathtub-filter/bathtub-filter-evidence-matrix.md; wiki/products/bathtub-filter/bathtub-filter-claim-evidence-ladder.md (archived); wiki/products/bathtub-filter/bathtub-filter-structure-audit-and-link-maintenance-2026-04-13.md (archived); index.md; 8 additional reference files updated
- status: done
- notes: merged claim-evidence-ladder 5-level framework into evidence-matrix as Section 9 (宣称强度阶梯); ladder file archived with superseded_by pointer; structure-audit-and-link-maintenance-2026-04-13 retired as one-time log; all internal references updated across buying-criteria, obsidian-map, claim-risk-audit-v2, claim-register, review-and-compliance-landscape, institutional-guidance, and index.

## [2026-04-17] maintain | bathtub filter content depth — Type A gap-fill
- source: internal content audit
- updated: wiki/products/bathtub-filter/bathtub-filter-normal-flow-vs-reduced-flow-evidence-table.md; wiki/products/bathtub-filter/bathtub-filter-product-forms.md; wiki/products/bathtub-filter/bathtub-filter-buying-criteria.md; wiki/products/bathtub-filter/bathtub-filter-visual-merchandising-and-creative-strategy.md
- status: working
- notes: strengthened 4 thin pages using existing cluster content. (1) normal-flow evidence table: added realistic fill GPM baseline definition (1.0–2.0 GPM benchmark from compatibility-engineering-breakpoints); (2) product-forms: added complaint-pattern-by-form table from complaint-taxonomy + KES route-to-form correspondence table; (3) buying-criteria: added "当前证据指向" evidence page pointers under each of the 7 criteria, converting the checklist into a connected evidence map; (4) visual-merchandising: added brand × visual world × claim positioning full matrix from brand-operating-matrix-v2 + inline commentary on performance signal quality per brand.

## [2026-04-17] maintain | bathtub filter cross-link + coverage-status refresh
- source: internal gap analysis
- updated: wiki/products/bathtub-filter/bathtub-filter-obsidian-map.md; wiki/products/bathtub-filter/bathtub-filter.md; wiki/products/bathtub-filter/bathtub-filter-research-coverage-gaps.md; wiki/products/bathtub-filter/bathtub-filter-cluster-cleanup-note-2026-04-14.md; wiki/products/bathtub-filter/bathtub-filter-kes-route-screening-memo-v2.md; wiki/products/bathtub-filter/bathtub-filter-kes-route-elimination-memo-v1.md
- status: working
- notes: added 4 new execution-tracking pages to obsidian-map and hub page; added patent-and-technical-landscape to synthesis list in obsidian-map; updated research-coverage-gaps with coverage status table (all 8 layers now ✓); added scope/分工 notes to route-screening-v2 and route-elimination-v1 (matching earlier claim-page treatment); updated cluster-cleanup-note with 2026-04-17 additions summary.

## [2026-04-17] maintain | bathtub filter content audit + structural gap-fill
- source: internal content audit
- updated: wiki/products/bathtub-filter/bathtub-filter-kes-concept-brief-v1.md; wiki/products/bathtub-filter/bathtub-filter-kes-next-step-execution-plan-v1.md; wiki/products/bathtub-filter/bathtub-filter-assumption-register.md (new); wiki/products/bathtub-filter/bathtub-filter-decision-register.md (new); wiki/products/bathtub-filter/bathtub-filter-supported-spout-matrix.md (new); wiki/products/bathtub-filter/bathtub-filter-claim-register.md (new); index.md
- status: working
- notes: conducted content-level audit of decision chain, evidence pages, and syntheses. Key findings: decision chain had concept-brief → execution-plan status mismatch (concept brief treated as locked, execution plan framed as conditional — now aligned); water-profile targeting was absent from concept brief (now declared as North America / free-chlorine-dominant, explicitly excludes chloramine-heavy and pure hard-water markets); created 4 missing canonical pages: assumption register (16 assumptions), decision register (8 open decisions × 5 workstreams), supported-spout-matrix stub (gate 2 artifact), and claim register (banned zone complete; allowed/conditional pending competitor research).

## [2026-04-13] ingest | bathtub filter marketplace review pass
- source: raw/products/bathtub-filter/2026-04-13-market-review-pass.md
- updated: wiki/products/bathtub-filter/bathtub-filter.md; wiki/products/bathtub-filter/bathtub-filter-review-patterns-and-return-risk.md; wiki/source-summaries/bathtub-filter-marketplace-review-and-editorial-review-pass-2026-04-13.md
- status: pending-owner-review
- notes: captured public HTML pages into raw/products/bathtub-filter/2026-04-13-market-review-pass/ and distilled early conversion / disappointment patterns.

## [2026-04-13] ingest | bathtub filter normal-flow vs reduced-flow evidence
- source: raw/products/bathtub-filter/2026-04-13-normal-flow-vs-reduced-flow-evidence-notes.md
- updated: wiki/products/bathtub-filter/bathtub-filter-normal-flow-vs-reduced-flow-evidence-table.md; wiki/products/bathtub-filter/bathtub-filter.md; wiki/syntheses/bathtub-filter-review-and-compliance-landscape.md
- status: pending-owner-review
- notes: isolated flow-rate sensitivity as a category-gating issue and added a dedicated working evidence table.

## [2026-04-13] maintain | bathtub filter obsidian link pass
- source: wiki/products/bathtub-filter/bathtub-filter-obsidian-map.md
- updated: wiki/products/bathtub-filter/bathtub-filter.md; wiki/products/bathtub-filter/bathtub-filter-review-patterns-and-return-risk.md; wiki/products/bathtub-filter/bathtub-filter-normal-flow-vs-reduced-flow-evidence-table.md; wiki/syntheses/bathtub-filter-review-and-compliance-landscape.md
- status: working
- notes: added `[[wikilinks]]` and a dedicated Obsidian navigation hub for the bathtub-filter page cluster.

## [2026-04-13] maintain | bathtub filter structure audit + marketplace negative-review scouting
- source: wiki/products/bathtub-filter/bathtub-filter-structure-audit-and-link-maintenance-2026-04-13.md
- updated: wiki/products/bathtub-filter/bathtub-filter-marketplace-negative-review-signals.md; wiki/products/bathtub-filter/bathtub-filter.md; wiki/products/bathtub-filter/bathtub-filter-obsidian-map.md; wiki/products/bathtub-filter/bathtub-filter-brand-operating-matrix.md; wiki/products/bathtub-filter/bathtub-filter-brand-operating-matrix-v2.md; wiki/products/bathtub-filter/bathtub-filter-channel-positioning-table.md; wiki/products/bathtub-filter/bathtub-filter-channel-positioning-table-v2.md
- status: working
- notes: added early marketplace-native complaint signals from public snippets and started explicit version links for selected v1/v2 pages.

## [2026-04-13] maintain | bathtub filter source-summary link pass + complaint clustering deepening
- source: wiki/source-summaries/bathtub-filter-marketplace-review-and-editorial-review-pass-2026-04-13.md
- updated: wiki/source-summaries/bathtub-filter-marketplace-review-and-editorial-review-pass-2026-04-13.md; wiki/source-summaries/bathtub-filter-market-scan-2026-04-11.md; wiki/source-summaries/bathtub-filter-academic-and-institutional-evidence-2026-04-11.md; wiki/source-summaries/bathtub-filter-api-backed-academic-and-patent-fetch-2026-04-12.md; wiki/source-summaries/bathtub-filter-swimming-eczema-explanation-layer-2026-04-12.md; wiki/source-summaries/bathtub-filter-web-content-fetch-attempts-2026-04-11.md; wiki/products/bathtub-filter/bathtub-filter-marketplace-negative-review-signals.md
- status: working
- notes: added `[[wikilinks]]` to key source-summary pages and expanded complaint clusters to include overflow, slower-fill frustration, value disappointment, and curved-faucet compatibility tension.

## [2026-04-13] maintain | bathtub filter complaint taxonomy by route + synthesis backlink strengthening
- source: raw/products/bathtub-filter/2026-04-13-complaint-taxonomy-by-route-notes.md
- updated: wiki/products/bathtub-filter/bathtub-filter-complaint-taxonomy-and-risk-by-route.md; wiki/products/bathtub-filter/bathtub-filter.md; wiki/products/bathtub-filter/bathtub-filter-obsidian-map.md; wiki/syntheses/bathtub-filter-brand-and-content-landscape.md; wiki/syntheses/bathtub-filter-competitor-and-demand-scan.md; wiki/syntheses/bathtub-filter-patent-and-technical-landscape.md; wiki/syntheses/bathtub-filter-research-map.md
- status: working
- notes: converted complaint clusters into a route-based screening lens and strengthened Obsidian graph connectivity across the main synthesis pages.

## [2026-04-13] maintain | bathtub filter route elimination memo + weak-page backlink strengthening
- source: wiki/products/bathtub-filter/bathtub-filter-kes-route-elimination-memo-v1.md
- updated: wiki/products/bathtub-filter/bathtub-filter-kes-route-elimination-memo-v1.md; wiki/products/bathtub-filter/bathtub-filter.md; wiki/products/bathtub-filter/bathtub-filter-obsidian-map.md; wiki/products/bathtub-filter/bathtub-filter-kes-route-screening-memo-v2.md; wiki/products/bathtub-filter/bathtub-filter-buying-criteria.md; wiki/products/bathtub-filter/bathtub-filter-category-boundary.md; wiki/products/bathtub-filter/bathtub-filter-institutional-guidance.md; wiki/products/bathtub-filter/bathtub-filter-technology-notes.md; wiki/playbooks/bathtub-filter-validation-testing-protocol.md; wiki/syntheses/bathtub-filter-operations-channel-and-visual-landscape.md; wiki/syntheses/bathtub-filter-sns-creator-and-visual-taxonomy.md; wiki/products/bathtub-filter/bathtub-filter-structure-audit-and-link-maintenance-2026-04-13.md; wiki/source-summaries/bathtub-filter-web-content-fetch-attempts-2026-04-11.md
- status: working
- notes: added a stricter KES route-elimination layer and improved Obsidian reachability for previously low-backlink bathtub-filter pages.

## [2026-04-13] maintain | bathtub filter test-gating checklist + final weak-page link pass
- source: wiki/products/bathtub-filter/bathtub-filter-test-gating-checklist-for-kes.md
- updated: wiki/products/bathtub-filter/bathtub-filter-test-gating-checklist-for-kes.md; wiki/products/bathtub-filter/bathtub-filter.md; wiki/products/bathtub-filter/bathtub-filter-obsidian-map.md; wiki/playbooks/bathtub-filter-validation-testing-protocol.md; wiki/products/bathtub-filter/bathtub-filter-brand-page-claim-compliance-audit.md; wiki/products/bathtub-filter/bathtub-filter-brand-page-pack-audit-v2.md; wiki/products/bathtub-filter/bathtub-filter-product-definition-language.md; wiki/products/bathtub-filter/bathtub-filter-research-program-a-to-f.md; wiki/source-summaries/bathtub-filter-swimming-eczema-explanation-layer-2026-04-12.md
- status: working
- notes: converted research into a practical KES screening gate and further reduced weak-link pockets in the bathtub-filter Obsidian graph.

## [2026-04-14] maintain | bathtub filter concept brief + concept-graph tightening
- source: wiki/products/bathtub-filter/bathtub-filter-kes-concept-brief-v1.md
- updated: wiki/products/bathtub-filter/bathtub-filter-kes-concept-brief-v1.md; wiki/products/bathtub-filter/bathtub-filter.md; wiki/products/bathtub-filter/bathtub-filter-obsidian-map.md; wiki/products/bathtub-filter/bathtub-filter-kes-route-elimination-memo-v1.md; wiki/products/bathtub-filter/bathtub-filter-test-gating-checklist-for-kes.md; wiki/products/bathtub-filter/bathtub-filter-buying-criteria.md; wiki/products/bathtub-filter/bathtub-filter-technology-notes.md; wiki/products/bathtub-filter/bathtub-filter-product-definition-language.md; wiki/products/bathtub-filter/bathtub-filter-kes-product-architecture-hypotheses.md
- status: working
- notes: translated surviving routes into concept candidates and tightened the decision chain from elimination → test gating → concept definition.

## [2026-04-14] maintain | bathtub filter execution-plan package + cleanup note
- source: wiki/products/bathtub-filter/bathtub-filter-kes-next-step-execution-plan-v1.md
- updated: wiki/products/bathtub-filter/bathtub-filter-kes-next-step-execution-plan-v1.md; wiki/products/bathtub-filter/bathtub-filter.md; wiki/products/bathtub-filter/bathtub-filter-obsidian-map.md; wiki/products/bathtub-filter/bathtub-filter-kes-concept-brief-v1.md; wiki/products/bathtub-filter/bathtub-filter-kes-route-elimination-memo-v1.md; wiki/products/bathtub-filter/bathtub-filter-test-gating-checklist-for-kes.md; wiki/products/bathtub-filter/bathtub-filter-cluster-cleanup-note-2026-04-14.md
- status: working
- notes: converted the concept package into an execution sequence and recorded current cluster cleanup status for ongoing maintenance.

## [2026-04-15] maintain | bathtub filter marketplace-native review mining deepening
- source: raw/products/bathtub-filter/2026-04-15-marketplace-review-mining-pass.md
- updated: raw/products/bathtub-filter/2026-04-15-marketplace-review-mining-pass.md; wiki/products/bathtub-filter/bathtub-filter-review-patterns-and-return-risk.md; wiki/products/bathtub-filter/bathtub-filter-marketplace-negative-review-signals.md
- status: working
- notes: extended review mining with Amazon snippet/Q&A and Reddit-visible signals; sharpened slip/overflow/slow-fill/value-collapse patterns and converted them into clearer KES product/messaging implications.

## [2026-04-15] maintain | bathtub filter channel + unit-economics deepening
- source: raw/products/bathtub-filter/2026-04-15-channel-and-unit-economics-pass.md
- updated: raw/products/bathtub-filter/2026-04-15-channel-and-unit-economics-pass.md; wiki/products/bathtub-filter/bathtub-filter-channel-positioning-table-v2.md; wiki/products/bathtub-filter/bathtub-filter-pricing-refill-flow-fit-table-v2.md
- status: working
- notes: clarified channel identities (marketplace commodity vs premium DTC vs utility-lineage vs review bridge) and reframed pricing/replacement logic around lived unit economics rather than list price alone.

## [2026-04-15] maintain | bathtub filter compatibility engineering + water-jurisdiction deepening
- source: raw/products/bathtub-filter/2026-04-15-compatibility-engineering-and-water-jurisdiction-pass.md
- updated: raw/products/bathtub-filter/2026-04-15-compatibility-engineering-and-water-jurisdiction-pass.md; wiki/products/bathtub-filter/bathtub-filter-compatibility-engineering-breakpoints.md; wiki/products/bathtub-filter/bathtub-filter-water-jurisdiction-demand-map.md; wiki/products/bathtub-filter/bathtub-filter-installation-risk-matrix-v2.md; wiki/products/bathtub-filter/bathtub-filter.md
- status: working
- notes: upgraded installation/compatibility from generic risk language into engineering breakpoints, and clarified how chlorine, chloramine, and hard-water realities affect category demand versus claim defensibility.

## [2026-04-15] maintain | bathtub filter E/F write-back into go-no-go and gating
- source: wiki/products/bathtub-filter/bathtub-filter-kes-go-no-go-memo-v1.md
- updated: wiki/products/bathtub-filter/bathtub-filter-kes-go-no-go-memo-v1.md; wiki/products/bathtub-filter/bathtub-filter-test-gating-checklist-for-kes.md
- status: working
- notes: wrote compatibility-engineering and water-jurisdiction insights back into the decision memo and test gates, adding leak-taxonomy, spout-taxonomy, and geo/water-profile-fit requirements.

## [2026-04-16] maintain | wiki structure audit and index/dashboard refresh
- source: internal audit
- updated: index.md; dashboards/active-projects.md; dashboards/recent-updates.md; wiki/products/bathtub-filter/bathtub-filter-brand-operating-matrix.md; wiki/products/bathtub-filter/bathtub-filter-channel-positioning-table.md; wiki/products/bathtub-filter/bathtub-filter-claim-risk-audit.md; wiki/products/bathtub-filter/bathtub-filter-installation-risk-matrix.md; wiki/products/bathtub-filter/bathtub-filter-kes-route-screening-memo-v1.md; wiki/products/bathtub-filter/bathtub-filter-pricing-refill-flow-fit-table.md
- status: working
- notes: audited all 78 pages; expanded index.md from 8 to full coverage (all canonical pages, full bathtub-filter cluster, all source-summaries); archived 6 superseded v1 pages (brand-operating-matrix, channel-positioning-table, claim-risk-audit, installation-risk-matrix, kes-route-screening-memo-v1, pricing-refill-flow-fit-table) with superseded_by pointers; populated active-projects dashboard with Japan Market Entry and Bathtub Filter KES Evaluation; brought recent-updates dashboard current through 2026-04-16.

## [2026-04-15] maintain | bathtub filter IP depth + visual strategy deepening
- source: raw/products/bathtub-filter/2026-04-15-ip-depth-and-visual-strategy-pass.md
- updated: raw/products/bathtub-filter/2026-04-15-ip-depth-and-visual-strategy-pass.md; wiki/products/bathtub-filter/bathtub-filter-ip-depth-and-brand-marker-map.md; wiki/products/bathtub-filter/bathtub-filter-visual-merchandising-and-creative-strategy.md; wiki/products/bathtub-filter/bathtub-filter.md
- status: working
- notes: clarified which brands appear more technically anchored versus marketing-led, and mapped the recurring visual worlds that seem to drive bathtub-filter conversion.
