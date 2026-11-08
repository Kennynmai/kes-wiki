# Log — KES Company Wiki

Use one heading per meaningful action.

Example:
## [2026-04-06] ingest | Japan market entry report
- source: raw/markets/japan/report.pdf
- updated: wiki/markets/japan.md; wiki/projects/japan-market-entry.md
- status: pending-owner-review
- notes: short summary of what changed

## [2026-10-09] ingest | CaSO₃ × chloramine contradiction event (supplier ZONET20230707001 + KES first-party bench test)
- source: raw/products/bathtub-filter/2026-10-09-caso3-chloramine-contradiction-pass.md; supplier report ZONET20230707001 (淄博宗立, completed 2023-07-13); KES first-party chloramine bench test (130g CaSO₃ / 4 ppm / 24 L/min / 60s / 38°C)
- updated: raw/products/bathtub-filter/2026-10-09-caso3-chloramine-contradiction-pass.md (new); wiki/source-summaries/bathtub-filter-caso3-chloramine-contradiction-event-2026-10-09.md (new); wiki/products/bathtub-filter/bathtub-filter-chloramine-media-research.md (new Section 3.5; Section 6 CaSO₃ row re-labelled ❌→⚠️; Gap 2 reframed); wiki/products/bathtub-filter/bathtub-filter-evidence-bibliography.md (new E6/E7); wiki/products/bathtub-filter/bathtub-filter-claim-register.md (banned-zone rationale updated, ban retained); wiki/products/bathtub-filter/bathtub-filter-disinfectant-types-and-media-guide.md (media matrix row re-labelled; trichloramine naming risk added); wiki/products/bathtub-filter/bathtub-filter-media-efficacy-at-bath-conditions.md (Section 8 gap 3 and Section 9 open-limits wording qualified); wiki/products/bathtub-filter/bathtub-filter-assumption-register.md (A-14 reviewed and held); wiki/playbooks/bathtub-filter-validation-testing-protocol.md (new Module 7 spec); ops/ingestion-registry.md; ops/verification-queue.md; index.md; log.md
- status: pending-owner-review
- notes: |
  Recorded a contradiction event rather than a gap fill. A supplier report and a KES bench test both report near-total calcium-sulfite chloramine removal, against a Tier-1-anchored wiki position of "no removal expected".

  **The conclusion was not reversed and no claim was unlocked.** The Tier-1 anchor (Yiin, Walker & Margerum 1987) is unretracted. What changed is the *basis* recorded underneath it: the chloramine research page had rested partly on an argument-from-silence ("no data exists, therefore ineffective"), and two uncontrolled observations now run against that. The CaSO₃ matrix cell was re-labelled ❌ → ⚠️ "untested, unresolved" and Gap 2 was reframed from "no data" to "no controlled data". The claim-register banned-zone entry stays banned; only the recorded rationale changed, from "chemistry mismatch" to "chemistry mismatch contested, no controlled evidence either way". Version A's life model, product scope, and assumption A-14 (chloramine geos deferred) are all unchanged.

  Both new data points were assessed as incapable of supporting any claim: neither reports pH (the variable Yiin identifies as controlling the reaction rate), neither has a media-free decay control, neither uses a chloramine-specific method, neither states a detection limit, and both consumed under 1% of media capacity (0.61% and 0.13%, computed from brochure bulk density and 1 mol SO₃ per mol NH₂Cl stoichiometry). The supplier report additionally shows a ~26% influent decay across the run with no paired blank, and labels its challenge water "三氯铵" at 0.728–1.0 mg/L — roughly three orders of magnitude above reported NCl₃ levels in potable water, so the species label requires written supplier clarification before the four 100% results can be used at all.

  New work item opened: playbook Module 7 specifies a decisive CaSO₃ × chloramine test built on **chloride mass balance** — because both prior tests measure the substrate they are trying to remove using a method that substrate can independently degrade, IC chloride measures the reaction *product* and is immune to the spike-decay confound. Full protocol: 4 arms, pH controlled at 7.0/7.8/8.5, throughput series to breakthrough, n≥3, production-spec 3–4 mm media.

  Follow-up same day: KES confirmed the supplier's Chinese legal name 淄博宗立新材料科技有限公司 and the English "Zibo Onlyzone Water Treatment Technology Co., Ltd." are **the same entity** — a translation variance, not two companies. The open entity-reconciliation item was closed, and the canonical pairing was registered in `governance/entity-canonicalization.md` so the question does not get re-raised.
## [2026-09-06] maintain | bathtub filter — 决策链刷新、provenance 补全、视觉稿对齐、占位登记
- source: 2026-09-06 缺口盘点（决策链停在 4 月、6 个 raw 包无 source summary、视觉稿与新文案漂移、审查页 M4/M5/K3/K4 未落地、326 个占位无清单）
- updated: 决策链 5 页加「2026-09-06 状态更新」（go-no-go memo、最终执行摘要、R&D roadmap Phase 映射、test-gating Gate 映射、assumption register 重评 + A-17～A-19）; wiki/source-summaries/ 新增 6 页（06-17 策略文档、宗立氯胺测试、06-18 源文件夹、宗立阻垢卫生报告、专利申请、V1 BOM xlsx）; ops/ingestion-registry.md 补 9 行; homepage-and-about-page-layout Hero 改 场景→收益→机制→证明、PET / 130 / 110 口径、去「赌」「便宜填料」; hero-film storyboard 镜 1 改场景开场、镜 2 并入 reframe; decision register D-13～D-15; validation protocol Module 3 新增动态挂重; 新页 bathtub-filter-site-placeholder-register-2026-09-06.md（326 项按页面 / 负责方）; gap doc 顶部「当前状态速览」; hub / index / log / dashboards
- status: done（桌面侧）/ pending-user（专利 7 份原件、BOM xlsx 未入 raw）
- notes: |
  决策链五页正文保留为历史判断，只在 H1 下加状态块，把 conditional GO 的含义从"要不要继续研究"改为"V1 已定义，product GO 只差 Gate 1 与三项工程复核"。source summary 补记时核查发现专利与 BOM 两个 primary source 的 raw 目录只有 README，原件未入库，已在 summary、hub 已知缺口、registry 三处标出。占位登记显示 326 项中 114 项未标负责方，运营 65、法务 41、工程 29 为前三；法务项阻塞包装开印与 DTC 上线，列为第一优先。

## [2026-09-06] write | bathtub filter — 三条人群故事完整版
- source: bathtub-filter-kes-marketing-layers-and-story-format-2026-09-06.md §三 模板
- updated: 同页新增 §三A（三条完整版 + CN 对齐 + Hero / 社媒 / 邮件 / 包装内卡切片 + 逐段护栏 + 永不说清单 + 共同七节拍结构 + 上线检查表）; log.md
- status: draft（Illustrative scenario，待 UGC 替换）
- notes: |
  S-A 城市敏感肌（"The water smells like water"）、S-B 幼儿家庭（"Sunday night is bath night"，内嵌 "nobody can honestly tell you that" 承重句）、S-C 硬水城市（"The scale is still my problem. The chlorine isn't."，内嵌 "does not soften"）。三条共用七节拍：日常 → 注意到 → 旧答案 → 诚实边界 → 自测 → 看见 → 现在的 routine；每条必有一句承重 disclaim，读数只描述不给百分比，收束句宾语只能是水 / 气味 / 流程。

## [2026-09-06] synthesize | bathtub filter — 营销版本分层与故事版规则
- source: 2026-09-06 策略讨论（理性版 / clean material 版 / 故事版）；审查页 M2；评论标签购买动机占比
- updated: wiki/products/bathtub-filter/bathtub-filter-kes-marketing-layers-and-story-format-2026-09-06.md (new); bathtub-filter-kes-clean-formula-emotional-positioning.md §十一; bathtub-filter-kes-website-copy-v1.md（Hero 场景句槽位）; bathtub-filter.md; index.md; dashboards/recent-updates.md; log.md
- status: done（框架）/ pending-ab-test（主次由上市后 A/B 定）
- notes: |
  决策：不新增第三个定位版本。理性版 = 证据层（register / T2 / T3），clean material = 品牌故事层（情感定位页），故事版 = 用户故事格式层，只做 Hero 轮换、社媒前 3 秒、邮件开头与包装内卡片，不新开页面。页面固定顺序 场景 → 转折 → 证明。故事版六条规则（同一套 claim、只讲 routine 不讲结果、婴幼儿只作场景、硬水以诊断为转折、真人前不叫证言、不新开页面）与三条人群脚本模板（城市敏感肌 / 幼儿家庭 / 硬水城市）附逐句护栏。创始人故事、恐惧型、成就型、"We clean the water that cleans you" 式口号明确不做。验证用 H 层 $3,200 A/B：证据 / 品牌故事 / 用户故事三种 Hero 开场，退货率为主指标。

## [2026-09-05] fix | bathtub filter V1 — 全链路审查修复批次（28 页）
- source: wiki/products/bathtub-filter/bathtub-filter-v1-full-chain-critical-review-2026-09-05.md §6 修复清单
- updated: 25lpm bench spec（基准配置改 BOM、新增 §2.5 装填 / 溢流 / 起泡复核）; media-efficacy §9.5（旧配置标注）; T2（≥99% 降 🟡、35 L/min 降 🟡）; website-copy-v1（Hero 改 收益→机制→证明、tagline / 对照语气、key facts 拆流量、更换句改试纸触发、Maker note 团队署名）; Amazon listing spec（B4 去 35、B5 去 96/121）; P1 / P2（床厚→仓有效高 14 mm、#8/#9 升 🟢、125 mm、试纸量程要求、refill 决策挂链）; T3（新增 §〇 试纸可执行触发）; post-purchase / IFU / packaging §三 #2 同步; care guide §一 改在位滴干 + 每周深晾（🟡 待 Module 4）; claim register（Positioning 行去 harm-reduction、Fit 行去 35、新增 2026-09-05 增补段）; FAQ / 结构总览 / 挂带页 / 技术笔记 同步; 卖点页 §5 浴盐卖点降 🟡; GTM（订阅按寿命分档、per-bath 与 TCO 重算）; 订阅页默认周期; decision register 新增 D-09～D-12; validation protocol Module 3 / 4 新增 5 项; 挂带设计页 / 支持龙头矩阵 / 安装指南 124→125 mm; hub / gap doc / 审查页 §8 处理记录; log.md; dashboards/recent-updates.md
- status: done（桌面侧）/ pending-engineering（D-10 KDF 仓装填、V1 溢流复测、在位滴干霉变观察、D-11 试纸量程、D-09 refill 形态、D-12 LTV 重跑）
- notes: |
  按审查页 §6 清单执行。原则：凡数字口径与 BOM 或寿命模型冲突的，改到 BOM / T3；凡对外数字来源于旧配置或内部模型的，降 🟡 并从 Amazon 与盒面撤出；凡需要物理验证才能定的（KDF 仓装填、溢流包络、在位滴干霉变、试纸量程），写成测试项与决策项而不是直接改结论。对外承重定位句由 "harm-reduction module" 改为 "free-chlorine reduction module"，中文「减害」改「除游离氯」；历史页（concept brief、PRD、架构假设、批判分析）保留原句不改。订阅从 90 天改为按水型分档（9 / 12 个月），TCO 由 $161 修正为约 $99（2 ppm），同时 refill 收入预期缩到原估算 1/3，需 finance 重跑 LTV。

## [2026-09-05] review | bathtub filter V1 — 配置 / 参数 / 包装 / 营销 / 文案 全链路批判审查
- source: wiki/products/bathtub-filter/（BOM、专利、efficacy §9/9.5、25lpm spec、卖点页、GTM、website copy、claim register）+ site/（P1/P2/P5/T2/T3/CH1/CH2/P4/SVC 订阅/维护）
- updated: wiki/products/bathtub-filter/bathtub-filter-v1-full-chain-critical-review-2026-09-05.md (new); bathtub-filter.md; bathtub-filter-research-coverage-gaps.md; index.md; dashboards/recent-updates.md; log.md
- status: pending-owner-review
- notes: |
  交叉审查发现 5 项 P0：① Gate 1 台架 spec 仍以裁定前配置（KDF 110 / CaSO₃ 130 / PP / 3,481 L / 143 baths）为基准；② 按 BOM 几何核算 KDF55 130 g 在 Ø117×14 mm 环形仓内只能装 36–44%（摊平床厚 5–6 mm，P1/P2 写 15 mm），透明仓会显得半空；③ 35 L/min 无溢流包络来自 204 g KDF + 45 g 炭配置，非 V1；④ 试纸粗档分辨率下 90/80% 触发在 1–2 ppm 进水时不可见，只有 50% 点可见，T3 与 skip-if-still-good 不可执行；⑤ GTM 90 天订阅 = 寿命模型消耗量约 3 倍，per-bath 与 TCO 数字不自洽。另有 P1：BOM 裁定只做了寿命重算未做性能重算、T2 ≥99% 与其它表面状态不一、承重定位句 harm-reduction 自带健康框架、首屏透明主张未回应四大购买动机、维护指令与"挂上就能用"冲突、refill 整仓/介质未拍板、Maker note 占位。已写成修复清单（§6），不改动被审查页面。

## [2026-09-05] maintain | bathtub filter — Filterbaby 剥离资料口径统一（shower-filter 目录不存在）
- source: 跨 kes-wiki / kenny-wiki 排查（含 git 历史）
- updated: wiki/products/bathtub-filter/bathtub-filter.md; bathtub-filter-research-coverage-gaps.md; bathtub-filter-2026-06-18-source-import-index.md; bathtub-filter-kes-next-step-execution-plan-v1.md; bathtub-filter-11-asin-public-competitor-evidence-2026-06-02.md; bathtub-filter-amazon-review-image-installation-packaging-leads-2026-06-02.md; bathtub-filter-competitor-claim-review-accuracy-scorecard-2026-06-02.md; bathtub-filter-competitor-customer-installation-target-matrix-2026-06-02.md; 另修 4 处 related 相对路径错误（pfas → site/catalytic-carbon、curtains、validation-protocol、labeling-analysis）
- status: done（用户确认口径）
- notes: |
  8 个页面此前写 Filterbaby `B0FNVDJRSQ` 资料"已迁到 wiki/products/shower-filter/ 与 raw/products/shower-filter/"。经查两个 repo 及其 git 历史都没有该目录；99 条评论原文、客户图、scorecard 子集与 competitor brief 未保留在任何 repo，源头是 ops-platform `dev_competitor_review` 库。统一改为"已从 bathtub 语料剔除、资料未保留在 repo、可按需从 ops-platform 重新导出"，品牌研究落点指向 kenny-wiki brand-studies 与本 repo market-research 的 shower-filter 定位/专利页。

## [2026-09-05] maintain | bathtub filter cluster — 结构 lint、hub / gap doc 刷新到 V1 定义阶段
- source: wiki/products/bathtub-filter/（117 + 53 页全量扫描）
- updated: wiki/products/bathtub-filter/bathtub-filter.md; wiki/products/bathtub-filter/bathtub-filter-research-coverage-gaps.md; index.md; 5 页补 frontmatter（ascorbate-chloramine-kinetics、kes-bathtub-filter-PRD-v1、critical-analysis-v1、deep-competitive-analysis-v2、review-corpus-wiki-update-note 归档）；competitive-intelligence-filterbaby-bath-haus 规范化 frontmatter；3 页去 UTF-8 BOM；3 处断链修复；删除 acf-supplier-research.md 重复副本与 inbox 中 3 份已入库文档；dashboards/recent-updates.md；log.md
- status: done
- notes: |
  hub 页此前停在 2026-06-24 口径（"研究已完成，可停止扩写"），而 2026-06-18 → 07-02 已入库自有专利申请 19/281,644（patent pending）、V1 27 项 BOM 裁定（KDF55 130g / CaSO₃ 110g、PET 滤棉、寿命模型重算 ~21,550 L @2ppm）、53 页 site/ 内容体系、产品线决策（氯胺版 / 井水版 GO、不做软化、PFAS 禁写）。hub 现以「V1 真理源」表把这些页面标为 single source of truth，并把"可以继续 benchmark sample buying"与"样品采购不作为本轮任务"的自相矛盾统一为后者。gap doc 新增本批次表，D 层 BOM 部件表关闭（COGS 仍 🟡），G 层加入自有专利，剩余卡点收敛为三项：Gate 1 第三方 DPD、COGS / margin、spout 实物泄漏 / 溢流记录。index.md 补入约 95 页（含整个 site/ 目录）。结构性缺口：6 个页面引用的 `wiki/products/shower-filter/` 在本 repo 与 git 历史中都不存在，Filterbaby 剥离资料需从外部仓库同步或改口径。

## [2026-05-30] synthesize | KES SKU certification mapping table and evidence pack checklist
- source: KES certifications register; KES certification claim-control matrix; KES official online verification; KES model-pattern inventory; KES DOE / CEC access notes
- updated: wiki/company/kes-sku-certification-mapping-table.md (new); wiki/company/kes-certification-evidence-pack-checklist.md (new); wiki/company/kes-certification-claim-control-matrix.md; wiki/company/kes-certifications-and-compliance-register.md; index.md; dashboards/recent-updates.md; ops/ingestion-registry.md; log.md
- status: done
- notes: |
  Added two execution assets. The SKU mapping table gives the team a fillable structure for `SKU -> printed model -> normalized public pattern / filing model -> certificate or filing id -> evidence path -> allowed wording`, with statuses such as `source-table-only`, `needs-model-normalization`, and `ready-to-claim`. The evidence-pack checklist defines what must be archived for IAPMO, WaterSense, DOE, CEC, CE, UKCA, and ISO, plus evidence strength tiers and a claim release gate. These pages convert the investigation into a practical control process, but remain draft until internal SKU exports and archived evidence packages are attached.

## [2026-05-30] deepen | KES DOE / CEC public database access
- source: raw/company/certifications/2026-05-30-kes-doe-cec-public-database-access-notes.md
- updated: raw/company/certifications/2026-05-30-kes-doe-cec-public-database-access-notes.md (new); wiki/source-summaries/kes-doe-cec-public-database-access-2026-05-30.md (new); wiki/company/kes-certifications-and-compliance-register.md; wiki/source-summaries/kes-official-online-certification-verification-2026-05-30.md; dashboards/recent-updates.md; ops/ingestion-registry.md; log.md
- status: done
- notes: |
  Added a focused DOE / CEC access note. DOE CCMS faucet and showerhead certification-data endpoints still returned HTTP 403, so no KES-specific DOE rows were captured. CEC Advanced Search is publicly accessible and exposes the relevant path `Plumbing Products -> Plumbing Fittings / Plumbing Fixtures`; Quick Search redirects to login in command-line access. A simulated `Plumbing Fittings + Approved` form search timed out before returning results, so CEC remains internal-evidence-only pending browser screenshots, export, or model-level MAEDbS rows.

## [2026-05-30] deepen | KES public certification model-pattern inventory
- source: raw/company/certifications/2026-05-30-kes-public-model-pattern-inventory-notes.md
- updated: raw/company/certifications/2026-05-30-kes-public-model-pattern-inventory-notes.md (new); wiki/source-summaries/kes-public-certification-model-pattern-inventory-2026-05-30.md (new); wiki/company/kes-certification-claim-control-matrix.md; wiki/company/kes-certifications-and-compliance-register.md; wiki/source-summaries/kes-official-online-certification-verification-2026-05-30.md; dashboards/recent-updates.md; ops/ingestion-registry.md; log.md
- status: done
- notes: |
  Added a model-pattern inventory layer for public KES certification records. The key operational correction is that exact string matching produces false gaps: all 18 WaterSense rows fail exact cUPC matching, but all 18 align with broader cUPC wildcard patterns after treating `***` / `**` as pattern slots. The 12 WaterSense faucet rows also align with NSF 372 and NSF 61 faucet rows after wildcard and `Q` marker normalization; the 6 WaterSense shower rows align with cUPC only in the public data observed. This gives the next SKU-level matcher clear normalization rules while keeping external claims gated behind SKU mapping and owner review.

## [2026-05-30] synthesize | KES certification claim-control matrix
- source: KES official online certification verification pass; KES certification / compliance register; internal source-table readout
- updated: wiki/company/kes-certification-claim-control-matrix.md (new); wiki/company/kes-certifications-and-compliance-register.md; index.md; dashboards/recent-updates.md; ops/ingestion-registry.md; log.md
- status: done
- notes: |
  Added a working claim-control surface for KES certifications. Because no SKU-level mapping export is available in the local wiki, the page is deliberately set at public listing / model-pattern level. It defines safer wording and blocked wording for cUPC, NSF 61, NSF 372, WaterSense, DOE, CEC, CE/UKCA, and ISO 9001; maps product families to current public evidence; lists the exact 12 WaterSense faucet and 6 WaterSense showerhead public model patterns; and defines the minimum SKU-level fields needed next.

## [2026-05-30] deepen | KES official online certification verification
- source: IAPMO PLD / myPLC public records; IAPMO WaterSense public listings; EPA WaterSense API; DOE / CEC official public database access attempts; public CE/UKCA/ISO issuer search
- updated: raw/company/certifications/2026-05-30-kes-official-online-certification-verification.md (new); wiki/source-summaries/kes-official-online-certification-verification-2026-05-30.md (new); wiki/company/kes-certifications-and-compliance-register.md; dashboards/recent-updates.md; ops/ingestion-registry.md; log.md
- status: done
- notes: |
  Confirmed public-current issuer evidence for the IAPMO-backed KES records: cUPC file 10664, NSF/ANSI/CAN 372 file 10666, NSF/ANSI/CAN 61 file N-10665, WaterSense lavatory faucet file 16508, and WaterSense showerhead file 16509 are all active under KES HOME (U.S.) LIMITED. Captured current dates and model-pattern counts where available: cUPC 124 patterns, NSF 372 80 patterns, NSF 61 80 patterns, WaterSense 12 faucet + 6 showerhead patterns. EPA WaterSense API independently returns the same 18 KES brand model patterns. DOE/CEC were not publicly retrieved in this pass; CE/UKCA/ISO did not surface KES-specific issuer verification records, so those remain internal-evidence-only pending exports/certificate numbers.

## [2026-05-30] ingest | KES certification / compliance register
- source: user-provided 2026-05-30 DingTalk Notable source-table readout; targeted public reference scan
- updated: raw/company/certifications/2026-05-30-kes-certification-source-table-readout.md (new); wiki/source-summaries/kes-certification-source-table-readout-2026-05-30.md (new); wiki/source-summaries/kes-certification-public-reference-scan-2026-05-30.md (new); wiki/company/kes-certifications-and-compliance-register.md (new); index.md; dashboards/recent-updates.md; ops/ingestion-registry.md; log.md
- status: done
- notes: |
  Captured the current KES certification / compliance source-table readout and built a company-level register for cUPC, NSF/ANSI/CAN 61, NSF/ANSI/CAN 372, DOE, CEC, CE, UKCA, WaterSense lavatory faucets, WaterSense showerheads, and ISO 9001. The register separates current internal SKU coverage from external verification routes and claim boundaries. Key caution flags: static certificate PDFs are not current-listing proof; DOE/CEC are legal filings rather than third-party product certificates; NSF 61 and 372 do not support contaminant-removal claims; WaterSense is water-efficiency/performance labeling; ISO 9001 is company-level QMS; CE/UKCA need the underlying regulatory basis, declarations, certificate numbers, and test reports before marketing can safely use broad conformity language.

## [2026-04-23] maintain | 补入两份中文模板用于产品开发洞察与测试记录转内容
- source: wiki/syntheses/kes-offsite-brand-marketing-and-site-acquisition-framework.md
- updated: templates/product-development-insight-capture.md (new); templates/test-log-to-content.md (new); wiki/syntheses/kes-offsite-brand-marketing-and-site-acquisition-framework.md; dashboards/recent-updates.md; log.md
- status: done
- notes: |
  为了让新增的第 9 个主题 `把产品开发洞察变成品牌资产` 可以直接进入执行，而不是停留在框架层，本轮新增两份中文模板。第一份 `产品开发洞察采集模板` 用于从项目讨论、打样失败、实验测试、供应链限制、结构取舍里，提炼出值得对外表达的原创判断，并明确哪些能讲、哪些不能讲。第二份 `测试记录转内容模板` 用于把原始测试记录转成可发布资产，强制保留测试目的、条件、过程、结果、用户版解释和证据边界，避免团队把内部测试写成夸大宣传。这两份模板也已回链到 `KES 站外品牌营销与官网引流｜AI 内容扩展框架` 对应主题，后续可以直接拿来填。

## [2026-04-23] maintain | 补入产品开发过程洞察作为品牌资产主题
- source: wiki/syntheses/kes-offsite-brand-marketing-and-site-acquisition-framework.md
- updated: wiki/syntheses/kes-offsite-brand-marketing-and-site-acquisition-framework.md; dashboards/recent-updates.md; log.md
- status: done
- notes: |
  在原本 8 个子主题的 `站外品牌营销 + 官网引流` 框架里，补入第 9 个主题 `Product Development Insights As Brand Asset`。目的不是再加一个抽象栏目，而是明确 KES 在产品开发过程中自然产生的大量原创判断、失败教训、测试设计、实验结果、材料取舍、结构权衡，本身就是最稀缺的一手内容来源。如果不做结构化转化，这些材料只会停留在内部聊天、测试记录和表格里；如果做对了，它们可以变成 `engineering note`、`test note`、`how we decided`、`evidence / validation hub` 一类既能支持站外 expert-style 分发、也能承接官网信任建立的资产。同步把页内所有 “8 个子主题” 更新成 “9 个子主题”，并把该主题纳入推荐顺序与 90 天输出清单。

## [2026-04-23] maintain | KES 站外品牌营销与官网引流框架扩展为 8 个子主题
- source: wiki/source-summaries/kes-independent-site-content-ai-visibility-note-2026-04-23.md; wiki/syntheses/kes-geo-experiment-backlog.md; Google / OpenAI / Bing 现有官方 guidance
- updated: wiki/syntheses/kes-offsite-brand-marketing-and-site-acquisition-framework.md (new); ops/ingestion-registry.md; dashboards/recent-updates.md; log.md
- status: done
- notes: |
  将上一轮偏 operator note 的 AI 可见度判断，扩成一页更接近内容经营框架的 synthesis，目标明确聚焦 `站外品牌营销 + 官网引流`，而不是继续停留在 GEO 原理讨论。新页把最值得延展的方向压成 8 个子主题：`comparison content strategy`、`fit / non-fit strategy`、`review mining to content ops`、`external proof architecture`、`AI visibility measurement`、`question-to-page mapping`、`merchant data and structured data readiness`、`post-purchase content as acquisition asset`。每个子主题都补了四层：为什么重要、该回答什么问题、最适合的外部 surface、最适合承接的官网页型，以及对应的可交付物和 success signals。页尾再补一条 KES 推荐顺序和 90 天首批输出，方便从概念直接过渡到执行。

## [2026-04-23] ingest | KES / 独立站 / 出海内容 AI 可见度操作评注收入与 backlog 回写
- source: 用户提供文字；raw/strategy/geo/2026-04-23/internal-notes/kes-independent-site-content-ai-visibility-operator-note.md
- updated: wiki/source-summaries/kes-independent-site-content-ai-visibility-note-2026-04-23.md (new); wiki/syntheses/kes-geo-experiment-backlog.md; ops/ingestion-registry.md; dashboards/recent-updates.md; log.md
- status: done
- notes: |
  将一段面向 `KES / 独立站 / 出海内容` 场景的用户判断收入 wiki，处理原则不是把它升级为平台机制，而是保留为 `operator note`。这段材料最有价值的不是原文案例强度，而是四个执行转向：`关键词 -> 真实问题`、`页面存在 -> 可被引用的答案资产`、`官网自述 -> external signal stack`、`SEO/traffic/CVR -> AI visibility scoreboard`。因此本轮新增 raw capture 与 source-summary，并把可执行部分写回 `KES GEO Experiment Backlog`：新增 `High-Value Question Map`、`Best-Answer Page Template`、`External Signal Stack`、`AI Visibility Scoreboard` 四个实验，同时在 backlog 前部补一段 write-back framing，明确这更像 KES 的 operating layer translation，而不是新理论。

## [2026-04-19] maintain | Amazon / Rufus GEO playbook pass with scorecard, fix mapping, and page archetypes
- source: 现有 Amazon / GEO / OpenAI shopping 研究页；无新增 raw 本地源文件
- updated: wiki/playbooks/amazon-rufus-geo-audit-and-corroboration-playbook.md (new); wiki/syntheses/amazon-rufus-cosmo-e-geo-kes-response.md; wiki/syntheses/kes-ai-era-amazon-content-strategy-judgment.md; wiki/syntheses/kes-geo-experiment-backlog.md; index.md; dashboards/recent-updates.md; log.md
- status: done
- notes: |
  在上一轮把三项重点补成原则性操作后，再做一次缺口审视，发现仍缺三类真正会影响执行质量的东西：`打分法`、`symptom -> action surface` 映射、以及 `什么时候该建 FAQ / comparison / fit guide` 的页面选择规则。因此本轮新增独立 playbook，把 Amazon / Rufus GEO 从 synthesis 提炼成执行手册：一是固定 monthly query deck 的最低覆盖和 Rufus 评分卡（6 个维度，12 分制，并映射到 `Level 0-4` 成熟度）；二是把常见观测症状翻译成 first-fix surface，避免团队把所有问题都默认回写到 title；三是加入 off-Amazon corroboration 的 page archetype chooser 与最小结构，明确 FAQ、comparison、fit/non-fit、maintenance、selection guide 各自适用的触发条件。同步把相关 synthesis 和 experiment backlog 链回这页，并更新 index / recent-updates，方便后续直接按 playbook 执行。

## [2026-04-19] maintain | GEO / Rufus operationalization pass for audit, testing, and off-Amazon corroboration
- source: 现有 Amazon / GEO / OpenAI shopping synthesis pages；无新增 raw 本地源文件
- updated: wiki/syntheses/amazon-rufus-cosmo-e-geo-kes-response.md; wiki/syntheses/kes-geo-experiment-backlog.md; log.md
- status: done
- notes: |
  将此前偏判断层的 Amazon / GEO 研究，补成更可执行的 operating layer，重点补强三件事。第一，新增 `monthly Rufus query audit` 的固定流程：把 query family、记录字段、最小评分、月度 deliverable 固化，避免团队把 Rufus 观察做成零散截图。第二，明确 `如何利用 Rufus 做 GEO 与测试 GEO 水平`：把 Rufus 定义为 query-mining、answer-gap detection、maturity test 三合一工具，并给出从 `Level 0` 到 `Level 4` 的简化成熟度标尺，帮助区分问题卡在 retrieval、description、comparison、trust 还是 external corroboration。第三，把 `off-Amazon FAQ / comparison pages` 从抽象建议推进到页面类型、写法纪律与效果衡量：优先做 high-objection FAQ、adjacent-alternative comparison、fit/non-fit、maintenance 页面，并把效果从“看流量”改成 `AI citation / answer completeness / cross-surface consistency / assisted click / support deflection` 五类指标。对应 experiment backlog 也新增 monthly Rufus 审计实验，并细化 external corroboration 页的 change 与 metric。

## [2026-04-19] deepen | Amazon / Rufus 研究线补入更强一手材料，并形成 KES 判断页
- source: Amazon Science / Amazon publications / OpenReview 一手页面；无新增本地 raw 下载
- updated: wiki/source-summaries/amazon-paper-yu-et-al-2023-folkscope.md (new); wiki/source-summaries/amazon-paper-agrawal-sembium-2025-rtsm.md (new); wiki/source-summaries/amazon-paper-guo-et-al-2025-negation-product-search.md (new); wiki/source-summaries/amazon-paper-jagatap-et-al-2025-cold-start-product-search.md (new); wiki/source-summaries/shoppingcomp-openreview-2025-2026.md (new); wiki/syntheses/amazon-rufus-geo-agentic-commerce-core-reading.md (new); wiki/syntheses/kes-ai-era-amazon-content-strategy-judgment.md (new); wiki/syntheses/amazon-rufus-cosmo-e-geo-kes-response.md; log.md
- status: done
- notes: |
  在已有 `Rufus / COSMO / E-GEO / ACES` 基础上，补了五个更能纠偏 seller 圈叙事的一手来源：`FolkScope` 解释 Amazon intention knowledge 研究线并非从 Rufus 开始；`RTSM` 强化 recall / semantic matching 基础设施仍是核心层；`negation query rewriting` 说明复杂自然语言约束与排除条件已进入 product-search 研究前线；`cold-start product search` 说明新品 / 新类目首先卡在 query-to-category mapping，而不是先卡在 GEO；`ShoppingComp` 则把注意力从“AI 写购物报告”转向“AI 是否真能可靠选品和做安全判断”。基于这些材料，新增一页“8 篇核心材料”作为团队阅读入口，并新增一页“KES 版 AI 时代 Amazon 内容策略判断”，把 KES 的结论明确压成：这不是 `SEO -> GEO` 的单次替代，而是 `recall -> intent -> evidence -> rerank -> agent-choice` 五层叠加；内容策略的核心不是更像 AI 文案，而是把商品与品牌建设成更容易被召回、被理解、被引用、被比较、也更不容易在 agentic 时代被误判的证据系统。现有 Amazon / Rufus synthesis 也已同步回写这些新增判断。

## [2026-04-19] ingest | Amazon Rufus / GEO 微信卖家解读文章收入与研究底稿回写
- source: 用户提供的微信文章正文；raw/platforms/amazon/rufus-cosmo/2026-04-19/external-pages/wechat-kris-rufus-geo-listing-guide.md
- updated: wiki/source-summaries/wechat-kris-rufus-geo-listing-guide-2026-04-19.md (new); wiki/syntheses/amazon-rufus-cosmo-e-geo-kes-response.md; raw/platforms/amazon/rufus-cosmo/2026-04-19/raw-capture-log.md; log.md
- status: done
- notes: |
  将一篇以 `Kuzi & Malmasi 2024` 和 `E-GEO 2025` 为论据、面向 Amazon seller 的微信解读文收入 KES。处理原则不是把它当平台事实，而是把它归类为 `seller-side interpretation / discourse layer`：一方面，这篇文章确实把 KES 已有研究中的几个高价值方向压缩成了可操作模板，例如把 PDP 从“关键词页”改写成“答案页”、在 exploration/comparison/final consideration 三阶段分别配置 buying guide / comparison table / FAQ、减少 hype 和 keyword stuffing、提高结构化与事实密度；另一方面，它也明显把方向性论文写得过于确定，包括把 `Kuzi & Malmasi` 近似写成“Rufus 官方完整逻辑披露”、把 `E-GEO` 外部 benchmark 的 uplift/penalty 数值改写成 Amazon listing 实战结论、以及把若干 heuristic 提炼成近似稳定规则。为此，本次新增 source-summary 明确区分“文章做对了什么”和“哪些说法不能写成事实”；同时把现有 synthesis 补了一段 seller-market translation 说明，允许 KES 借鉴其 operational packaging，但不接受其 certainty level。

## [2026-04-19] maintain | bathtub filter — California Prop 65 独立调查与应对页
- source: 官方公开法规与指引页（OEHHA / Proposition 65 Warnings / California AG），无新增 raw 本地源文件
- updated: wiki/products/bathtub-filter/bathtub-filter-california-prop65-investigation-and-response.md (new); wiki/products/bathtub-filter/bathtub-filter-us-state-federal-compliance-sidelines.md; wiki/products/bathtub-filter/bathtub-filter.md; dashboards/recent-updates.md; log.md
- status: done
- notes: |
  将原本挂在“美国州级 / 联邦合规副线”里的 Prop 65 段落拆成独立工作面，目标不是重复法规百科，而是把 KES 当前最需要的 `调查路径 + 决策口径 + 执行动作` 单独固化。基于官方页面确认三条时间/执行事实：`2025-01-01` 起新版 short-form warning 规则已生效；旧短版 warning 对 `2028-01-01` 及之后制造并贴标的产品不再适用；OEHHA 当前化学品清单日期为 `2025-12-08`。新页把 bathtub filter 的 Prop 65 问题重构为三个执行门槛：`risk BOM`、warning-ready packaging / PDP、California sell / no-sell 决策。后续补充进一步澄清了两层边界：(1) 法律上并非“某品类天然必须 warning”，而是存在 listed chemical exposure 且无法证明低于 safe harbor 时必须；(2) 行业实务里，`lead/brass`、`DEHP/PVC/soft parts`、加州互联网销售、`BPS` 热敏纸、供应链证据不足等场景通常已接近“effectively must warn”。工作结论收敛为：在缺少整机级成分与暴露评估前，KES 不应默认按“无需 warning”推进；更稳妥的默认应对要么是 `Warning-ready`，要么是 `California-holdout`。此页为运营/上市决策支持，不构成法律意见，后续若进入实际加州销售，应再接外部法务或检测机构复核。

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

## [2026-07-04] deepen | 淋浴螺纹标准调查（G1/2 vs NPT/NPSM）与美站文案口径
- source: Amazon bullet 回写试点（PSAN204-BK-RE）文案质疑 → 三轮外部查证（Delta/High Sierra/Trausch NPSM 尺寸表/Kingston Brass/Terry Love）+ 内部工程履历与产品负责人确认
- updated: wiki/products/kes-product-knowledge-base/products/bathroom-hardware/thread-standards-us-market.md
- status: verified
- notes: 最终结论=墙端 1/2" NPT 锥牙（螺纹密封）、花洒端 1/2"-14 直牙+垫圈密封（G1/2 与 NPSM 同 14 TPI、外径差 0.38mm 可直配）；"G 转 NPT 需转接头"的警告只适用锥牙场景不适用花洒端；文案规则（本地化标记打头/工程标记括号/禁跨标准改标/两端分开写）已固化进 ops 平台两个内容生成器 prompt；遗留待办=产品规格中台补录墙端 NPT。
## [2026-10-09] capture | WF US / WF CA promo task dispatch and activation check cancellation (张艳娟 request)
- source: raw/company/2026-10-09-wayfair-us-ca-promo-task-cancellation-request.md (internal request, dialogue channel)
- updated: raw/company/2026-10-09-wayfair-us-ca-promo-task-cancellation-request.md (new); wiki/protocols/wayfair-us-ca-promo-task-scope-change-2026-10-09.md (new); dashboards/recent-decisions.md; dashboards/recent-updates.md; ops/verification-queue.md; index.md; log.md
- status: pending-owner-review
- notes: |
  Two operational scope changes requested by 张艳娟: (1) cancel dispatch and notification of the 【新任务分配——促销开始前 24h】 task for Wayfair US and Wayfair CA; (2) stop checking coupon / Deal correct activation after a Wayfair promotion starts.

  Recorded as a decision page rather than silently dropped, because it removes an existing supervision step and future Wayfair promo SOP work will contradict it if it is not written down. Other platforms (Amazon / Home Depot / Walmart / DTC) are explicitly unchanged.

  Two points are unverified and queued: that `WF` means Wayfair (inferred from `dashboards/company-overview.md` and the WF / HD platform pairing in the North America research page — no wiki record of the task type itself exists), and whether "cancel dispatch and notification" also retires the task itself and whether any spot-check remains. Risks recorded: promo mis-configuration and wrong price will no longer be caught proactively, and promo start timing now relies entirely on operator scheduling. A data-side exception signal (price / conversion / order anomaly) is noted as the suggested compensating control, not as an approved decision.

## [2026-10-09] maintain | WF US / WF CA promo push cancellation — scope corrected after requester clarification
- source: raw/company/2026-10-09-wayfair-us-ca-promo-task-cancellation-request.md (clarification by 张艳娟, same day)
- updated: raw/company/2026-10-09-wayfair-us-ca-promo-task-cancellation-request.md; wiki/protocols/wayfair-us-ca-promo-task-scope-change-2026-10-09.md (title, Decision, Alternatives, Risks, Implementation implications, verification_status unverified → spot-checked); dashboards/recent-decisions.md; dashboards/recent-updates.md; ops/ingestion-registry.md; ops/verification-queue.md; index.md; log.md
- status: pending-owner-review
- notes: |
  Same-day clarification by 张艳娟 corrected the recorded scope of the 2026-10-09 Wayfair change. Three corrections: (1) `WF` is confirmed to mean Wayfair, no longer an inference; (2) what is cancelled is the **DingTalk push** for 【新任务分配——促销开始前 24h】, not the task or the operator action itself; (3) the coupon / Deal activation check after promo start is **retained** as an optional manual spot-check, not removed.

  This materially lowers the risk profile of the change versus the first capture, which had read as a removal of promo activation supervision. The page was rewritten rather than patched in place at the decision level, because the alternatives and risk sections had been written against the wrong scope: the remaining exposure is that promo start timing now has no system reminder (operator scheduling only) and that a spot-check with no agreed frequency or owner is effectively unobservable and may decay to zero.
## [2026-10-15] capture | 氯胺T 实测报告（实测氯胺20261015.pdf）收入与评估
- source: raw/products/bathtub-filter/2026-10-15-chloramine-T-measurement/（原始 PDF + 9 张提取图 + 2 个分析脚本）
- updated: raw/products/bathtub-filter/2026-10-15-chloramine-T-measurement/pass.md (new); wiki/source-summaries/bathtub-filter-chloramine-T-measurement-2026-10-15.md (new); wiki/products/bathtub-filter/bathtub-filter-chloramine-media-research.md (§3.5 第三数据点、§7 Gap 6 补注、§8 新增不可支撑项); wiki/products/bathtub-filter/bathtub-filter-disinfectant-types-and-media-guide.md (§1b-bis 新增「氯胺 T ≠ 一氯胺」物种辨析); wiki/source-summaries/bathtub-filter-caso3-chloramine-contradiction-event-2026-10-09.md (2026-10-15 追记节); wiki/playbooks/bathtub-filter-validation-testing-protocol.md (Module 7 加标试剂身份前置项 + 照片比色禁跨图); ops/ingestion-registry.md; ops/verification-queue.md
- status: unverified
- notes: |
  用户任务：收入该 PDF 并评估过滤氯胺的有效程度。

  **结论：这份报告无法评估氯胺去除，且挑战物身份很可能就错了。** 三条定性：
  1. 读数**不降反升** —— 初始 0.5~1 ppm，356L / 712L / 1068L 均为 1 ppm。零净去除证据。
  2. **试剂是「氯胺 T」不是「一氯胺」。** 氯胺 T（CAS 127-65-1，N-氯对甲苯磺酰胺钠）是**固体缓释消毒剂**，在水中缓慢水解生成**次氯酸 HOCl**；一氯胺（CAS 10599-90-3，NH₂Cl）才是市政水真实结合氯。西语维基明确警告「no debe ser confundida con monocloramina」。据此推断：本次实际测的是**游离氯去除**，而亚硫酸钙对游离氯 KES 已自测 84–90%（2026-03-20，5 ppm，16.5–30 L/min）——「无下降」反而与自有数据冲突，指向旁通/取样/读数错误。
  3. **照片比色数据跨图不可用。** 我对 9 张内嵌图做了 CIE-Lab 分析：同一块印刷标准色块（0.1 mg/L 格）跨 5 张照片 ΔE 达 3–30（人眼可辨阈值 ΔE≈2.3，明显不同色 >5）。五张照片分别在室内灯/室外阴影/直射日光下拍摄，曝光与白平衡严重不一致 —— 所谓「上升趋势」很可能只是光照差异。此项不依赖 ROI 标定，稳健。

  **工程量级**：19 L/min，1,068 L 全程仅 56 分钟。EBCT ≈ 0.37–0.46 s（假设 CaSO₃ 130 g），约为催化炭固相除氯胺门槛（EBCT ≥ 4–5 min）的 **1/600–1/800** —— 即便介质有活性，此工况也天然倾向「无净去除」，属证明力弱的设计选择。容量利用率 2.9–3.5%，仍是「存在性证明」而非寿命数据。

  **口径矛盾**：报告称配制 2 ppm，自来水总氯 0.1 ppm，但首个读数即 0.5–1 ppm，差 2–4 倍。无论怎么解释，五点若全为出水则缺配对进水，若「初始」为进水则与标称矛盾 —— **算不出有意义的去除率**。

  **这次真正变了什么**：产品结论零变化（CaSO₃ 氯胺格维持 ⚠️ Untested、claim 禁区维持、A-14 不变）。变化的是方法学层面新增一条要求 —— **加标试剂的物种身份必须在投加前书面确认 CAS**。并引出一个**高优先级回查项**：2026-10-09 那次 KES bench test 记录为「4 ppm 氯胺」未写明物种，若同为氯胺 T，则那份「矛盾事件」的判定可能根本不是矛盾，而是两次同向的自由氯观测 —— 氯胺方向上至今为零数据。确认前「两个方向相反的观测」应视为待验证。

  **自我标注**：逐点 Lab 反推浓度（0.50/2.00/1.94/1.00/0.50 mg/L）与报告标注不一致，但 ROI 为目视标定、像素精度有限，**该组数值不可单独引用**；页面已标注。稳健的只有跨图同色块色差与色卡区间分辨率不足两条结构性事实。

## [2026-10-15] maintain | 氯胺T 摘要自查降级 — 撤回「最稳健」标注
- source: 对 2026-10-15 本人 ingest 产物的复核（同事转述原结论要求评价）
- updated: wiki/source-summaries/bathtub-filter-chloramine-T-measurement-2026-10-15.md (§3.1 加自查修正记录 + 降级标题); raw/products/bathtub-filter/2026-10-15-chloramine-T-measurement/pass.md (§3.1 同上 + 方法学教训); wiki/products/bathtub-filter/bathtub-filter-chloramine-media-research.md (§3.5 加 correction 框); ops/verification-queue.md; raw 目录追加 cea_audit.py / cea_audit3.py / card_712L.png
- status: working
- notes: |
  同事转述了我 19:00 那轮结论并要求评价。复核中发现**我自己标注为「最稳健」的那一条是错的**，现予撤回。

  **错误内容**：我曾称「同一标准色块跨 5 图 ΔE 达 3–30，此条不依赖 ROI，最稳健」。这个「不依赖 ROI」的判断是错的 —— 它只是看起来不依赖。

  **四个系统性缺陷**（全部由复核发现）：
  1. p2_2 色卡 ROI **落在手的阴影里** → ΔE=30 主要反映阴影几何，不是白平衡。
  2. 印刷色块是**倾斜的平行四边形**（卡片有透视），而我的采样框是固定矩形 → 固定 x 带随 y 漂移出块外。
  3. 采样 y 带**跨到色块下方的数字标签**，黑字拉低 L* → 造出「阶梯非单调」假象。
  4. **重做两版修正均失败**。v2：全部 5 图非单调，连肉眼最清晰的 712L 也失败。v3：掩膜本身有效（63,245 px）但**分组只得 4 组而非 7 组** —— 透视倾斜使相邻色块在列投影上连成一片。**这不是可修的 bug，是照片比色的根本困难。**

  **仍然成立的是什么**：在肉眼最清晰的 712L 图上，「跨图同一色块 L* 差 3–30」对「同图内相邻色块 L* 差 0.13–5.88」—— **跨图扰动比相邻色阶差大一个量级，误差远大于信号**。这条量级关系才是依据；**具体 ΔE 数值不再引用**。定性结论（五张照片不同光源 + 明显透视 → 不可跨图比色）不需要数字也成立。

  **纪律教训（比原结论更重要）**：用手机照片做定量比色，需同时满足「固定光源 + 固定色温 + 正对拍摄消透视 + 同帧含标准卡」，本测试一条都不满足。**照片比色只能作现场预读，不能作证据** —— 这与 2026-03-20 内部比色被判定「不可作第三方可核查证据」是同一条纪律，这次连预读都不可靠。

  **三条主结论未变**：① 读数不降反升（此条引自报告自身标注，不依赖我的像素分析）；② 氯胺 T ≠ 一氯胺，对氯胺零信息量（化学事实，三个独立来源）；③ EBCT ≈ 0.4 s 属证明力弱工况。**产品结论依旧零变化**：CaSO₃ 氯胺格维持 ⚠️ 未验证、禁区维持、A-14 不变。

  **自省**：我在第一轮把一条「看起来不依赖 ROI」的结论主动标成「稳健」，这比不做标注更危险 —— 它把一个未验证的定量结果包装成了可靠论据。**标注「稳健」本身需要比结论更强的证据。**

## [2026-10-28] maintain | 氯胺 T 物种辨析节表述口径复核 —— 一处引语撤回、一处数值收紧、配比补引
- source: ops/verification-queue.md `VQ-0011`（disinfectant-types-and-media-guide §1b-bis 表述口径确认；原引用：第 17 行工单）
- updated: wiki/products/bathtub-filter/bathtub-filter-disinfectant-types-and-media-guide.md (§1b-bis 表 + 规则 + 复核记录 + Sources); wiki/products/bathtub-filter/bathtub-filter-chloramine-media-research.md (第三数据点表 + 引语 + Tier 2 新增来源 #26–#33); wiki/source-summaries/bathtub-filter-chloramine-T-measurement-2026-10-15.md (§2 表 + 更正记录 + pH 表述 + Sources); raw/products/bathtub-filter/2026-10-15-chloramine-T-measurement/pass.md (§2 表 + 2026-10-28 更正记录 + 来源分级); wiki/playbooks/bathtub-filter-validation-testing-protocol.md (Module 7 加标试剂身份行 + 来源补录); ops/verification-queue.md
- status: working
- notes: |
  工单性质：§1b-bis 是 2026-10-15 新增的领域知识条目，此前只记录了「CAS / 水解 / pH 8–10 三项来自公开来源」，**没有逐项核过来源**。本轮逐项核，结论是「**物种身份结论成立，但三条支撑表述里有两条不能用**」。

  **一、撤回一条无法归属的引语（最严重）**
  原文引用西班牙语维基：*「como antiséptico — no debe ser confundida con monocloramina」*，并当作「西语维基直接警告」写入 4 个页面（media guide、chloramine-media-research、source-summary、raw pass.md）。2026-10-28 复核：es.wikipedia MediaWiki `insource` 全文检索 0 命中，**全网精确短语检索同样 0 命中** —— 该句在 es.wikipedia 上不存在，来源无法归属。已删除，替换为该条目实际表述：*«La Cloramina-T se denomina cloramina, pero es realmente una sal (CH₃C₆H₄SO₂NClNa) derivada de una cloramina.»*（氯胺 T 虽名为氯胺，实为氯胺衍生盐）。**这条引语承载的结论方向没错，但它证明不了任何事 —— 一句查不到的引语比没有引语更糟。**

  **二、pH「8–10」收紧为「pH 通常约 8.5」**
  en.wikipedia 原文是 "slightly basic (pH typically 8.5)"；「8–10」来自科普中国（二级来源），**本次未能核到原文**。两处（media guide 表、media research 表、source-summary 表、raw pass.md 表、playbook Module 7、source-summary 缺口表第 4 行）统一改为 pH ≈ 8.5，并注明 8–10 属未核原文的二级来源。

  **三、CAS 与分子式补一手登记**
  PubChem PUG REST 核到：CID 3641960 = Chloramine-T（CAS 127-65-1，C₇H₇ClNNaO₂S，MW 227.64，三水合物 7080-50-4）；CID 25423 = Monochloramine（CAS 10599-90-3，ClH₂N，MW 51.47）。「水中水解生成次氯酸」改引 de.wikipedia（"In wässriger Lösung entsteht Hypochlorit durch Hydrolyse"）+ BenchChem 厂商协议，删去一句并非英文维基现行表述的伪引文（"In water, it breaks down to the disinfectant hypochlorite."）。

  **四、配比核完发现是对的 —— 但当时没有引用**
  「Cl₂:NH₃-N = 4.5:1~5:1 现场配比」我一开始判定方向反了（准备改写），**复核后确认它是正确的**：In-Situ / ChemScan 给出最优 Cl₂:NH₃-N = 4.5:1、水厂常规 3:1–5:1、> 5:1 才向二氯胺/三氯胺偏移；Snoeyink & Jenkins（经 Curry & Associates 2015/2023 引用）给出化学计量 5.06 mg Cl₂ : 1 mg NH₃-N；Halogen Systems 给出配比 4.5:1–5:1 与 pH 窗口（6.5–8.5 一氯胺占优，< 7 偏向二氯胺/三氯胺）。**教训：几乎要"修"掉一个正确的操作指引，只因为它当时没有引用。** 现已补引用，并加一条硬要求：配好后必须用 DPD 法分别测游离氯与一氯胺确认物种，配比、pH、读数写入测试记录。

  **五、撤回一个夸大措辞**
  raw pass.md 原写「由 3 个独立来源交叉确认」——实际是 1 个英文维基 + 1 个中文科普二级来源 + 2 个镜像/AI 百科（11467、grokipedia）。**物种身份结论不变**（氯胺 T ≠ 一氯胺，且现在有 PubChem 一手登记支撑），但"交叉确认"的措辞撤回。这是 2026-10-15 19:20 那次自查之后**第二类**同类错误：把"引用了若干网页"说成"独立交叉验证"。

  **产品结论零变化**：CaSO₃ 氯胺格维持 ⚠️ Untested、claim 禁区维持、A-14～A-19 不变。**2026-10-09 bench test 试剂身份回查工单不在本条范围内**（那是队列里更新的另一条，单独处理）。

  **剩余**：§1b-bis 的**最终表述口径仍待产品负责人 sign-off**（本轮只能做到"事实层核到一手来源 + 措辞收紧"，agent 不能替代 owner 确认）→ 保留在 ops/verification-queue.md。

## [2026-10-28] maintain | 照片比色数值降级的全库生效核查 —— 降级当时并没有全库生效
- source: ops/verification-queue.md `VQ-0010`（2026-10-15 pass.md 自查降级复核；原引用：第 16 行工单）
- updated: wiki/products/bathtub-filter/bathtub-filter-chloramine-media-research.md (§3.5 正文段落); wiki/source-summaries/bathtub-filter-chloramine-T-measurement-2026-10-15.md (§3.1 / §3.2 / TL;DR 第 3 条 / §5 缺口表第 9 行); wiki/playbooks/bathtub-filter-validation-testing-protocol.md (Module 7 附带发现); raw/products/bathtub-filter/2026-10-15-chloramine-T-measurement/pass.md (§3.1 表头 / §3.2 / 自查修正记录第 1 条 / §5 缺口表第 9 行); ops/ingestion-registry.md (bf-2026-10-15-chloramine-T 行 officiality_impact); ops/verification-queue.md
- status: working
- notes: |
  工单问的是：2026-10-15 19:20 那次自查把像素级 Lab 比对降级、宣布「具体 ΔE 数值不应引用」之后，**这个撤回到底在全库生效了吗？**

  **结论：没有生效。** 降级声明只写在 raw pass.md 与 source-summary §3.1 内部，**4 处仍在把已撤回的具体数值当证据用**：
  1. `bathtub-filter-chloramine-media-research.md` §3.5 正文（"differs across the five photographs by ΔE 3–30"）—— 而它自己下一段的更正框写着"The specific ΔE numbers should not be cited"，**同一页内自相矛盾**；
  2. `source-summaries/...-2026-10-15.md` TL;DR 第 3 条（「跨图 ΔE 达 30」）；
  3. 同页 §5 方法学缺口表第 9 行（「ΔE 达 30」）；
  4. `playbooks/bathtub-filter-validation-testing-protocol.md` Module 7 附带发现（「跨图 ΔE 达 3–30」）；
  5. 另加 `ops/ingestion-registry.md` 该行 officiality_impact 也写着「ΔE 达 3–30」—— **登记表是最容易被下游当成事实引用的地方**。

  **处理**：逐处改为只保留两条结构性事实 —— ① 跨图差异量级远大于同图相邻色阶差（约一个量级）；② 色卡 0.1–1 ppm 区间分辨率不足。raw 归档里的数值表**保留但加「已撤回数值·仅供审计，不得引用」抬头**，并保留撤回原因记录（审计需要看到撤回过程，但不让数字继续流通）。§3.2 的逐点 Lab 反推值同样标注撤回。

  **顺手补一条来源**：人眼辨色阈值原文写「ΔE ≈ 2.3 刚好可辨；> 5 明显不同色；> 10–20 须并置」——其中 **2.3 = JND 是有出处的**（CIE76 ΔE\*ab ≈ 2.3，Wikipedia《Color difference》§CIE76），但 **"> 5 明显不同 / > 10–20 须并置"是无出处的经验阶梯**，已删除。现在只保留 2.3 这一个有源阈值，并明确标注它**与本次测量无关**（本次跨图差异的数值已撤回）。

  **这次真正的问题不是数值错，而是「撤回」被当成了局部声明。** 撤回一个数字和撤回一个数字的**全部引用**是两件事：只在自己那页写一句「不应引用」，等于把风险外包给读者的自觉。**方法学纪律追加一条：撤回动作必须包含一次全库引用扫描（grep 级别），并把被撤回的值在登记表中一并替换。**

  **产品结论零变化**（本工单只涉及方法学表述，不触及任何化学结论）。

## [2026-10-28] maintain | 2026-10-09 bench test 试剂身份回查结案 —— 一份数据点退出氯胺证据，两处旧结论纠错
- source: ops/verification-queue.md `VQ-0012`（高优先级：「（跨页）2026-10-09 KES bench test 试剂身份」；原引用：第 18 行工单）
- updated: raw/products/bathtub-filter/2026-10-28-caso3-2026-10-09-reagent-identity-check.md (new); raw/products/bathtub-filter/2026-10-09-caso3-chloramine-bench-test-photos/ (new — 3 张一手照片 + 溯源 README); raw/products/bathtub-filter/2026-10-09-caso3-chloramine-contradiction-pass.md (2026-10-28 更正记录); wiki/source-summaries/bathtub-filter-caso3-chloramine-contradiction-event-2026-10-09.md (顶部状态框 + §2 表补物种/日期行 + 照片说明更正 + 2026-10-28 追记 + Affected pages); wiki/products/bathtub-filter/bathtub-filter-chloramine-media-research.md (§3 状态框 / §3.5 标题与正文 / 2026-10-28 立场表 / §6 汇总表 / §7 Gap 2 与 Gap 6 / §8 / Sources); wiki/products/bathtub-filter/bathtub-filter-evidence-bibliography.md (E7 重新定性 + E6 补注); wiki/products/bathtub-filter/bathtub-filter-claim-register.md (2026-10-28 status note + 禁区行理由第三次收紧); wiki/playbooks/bathtub-filter-validation-testing-protocol.md (Module 7 前提修正 + 三条新硬门槛 + 报价锚点 + 优先级上调); ops/verification-queue.md; ops/ingestion-registry.md; index.md; dashboards/recent-updates.md
- status: pending-owner-review
- notes: |
  工单问的是一件很具体的事：2026-10-09 那次 KES 台架记的是「4 ppm 氯胺」，**没写物种**。如果它用的是氯胺 T，那 2026-10-09 判定的「矛盾事件」就不成立，氯胺方向上至今零数据。

  **答案不是「是氯胺 T」，也不是「是一氯胺」，而是第三种：不可确认。**

  取证三步：① 找回 2026-10-09 的**原始钉钉会话**（11 条消息 + 3 张图）；② 把三张一手照片**首次归档进 raw**（此前只记了「verbal + photographic」，图根本没入库）；③ 检索 2026-08→10 全部 IM 中关于挑战液配制 / 试剂 / 标液的记录。

  **决定性证据是执行人自己的话。** 麦家浚 2026-10-12 14:15：「我们自己测试氯胺是可以过滤的（**用其他方法配比出来的，没有实验室氯胺标液准，也有可能我们配出来的是错误**）」；2026-10-14 10:54：KES 的「氯胺」试剂就是「**用氯胺T去配2ppm**」；2026-10-14 11:17：「**这个氯胺是无法确认是一氯胺还是什么**」——并把对外口径收缩成 free chlorine only。

  **裁定**：该台架是一次「未确认物种的加标氯测试」，按 KES 内部唯一有记录的氯胺试剂与执行人自述，**去除去向推定为游离氯**；**不得再作为氯胺证据引用**。措辞上刻意**不写**「已证明是氯胺 T」——记录不支持这个强度。

  **连带三件事**
  1. 「两个方向相反的观测」**撤回**；「KES 最难解释的那一点 / 支持假设的最强单点论据」**撤回** —— 若挑战物是游离氯，近零本就是 KES 自有数据（2026-03-20，5 ppm，16.5–30 L/min，**84–90%**）所预期的，**不构成稀罕性**。KES 物种确认氯胺数据点 = **0**。
  2. **「照片序列内部矛盾」是误判，撤回。** 旧推理错在把「原水」和「4 ppm 加标液」当成必须同源的一份水 —— 原水是没加标的自来水（本来就该无色，执行人自己也说「我们这边的自来水是 0.几，基本上不显色」）。**三张照片与所述协议逐张对应。** 保留的真实限制更窄也更准：第 2、3 张都是无色、**目视分不出哪张是原水哪张是出水**，所以照片仍不能单独证明 before/after —— 但原因是「分不出来」，不是「标注自相矛盾」。
  3. **实测日期口径修正**：三张图与 2026-09-24 群内同发图 **md5 逐张相同**，当日结论是「亚硫酸钙对氯胺效果非常明显」「**可以讲，直接亚硫酸钙即可，无需要 ACF**」。故实测发生在 **≤2026-09-24**，**10-09 是汇报日不是测试日**。

  **顺手回答了组织一直在问的第三方检测问题**：实验室按国标 `GB/T 5750.11-2023` 执行，**只给总氯胺、不拆一氯胺/二氯铵/NCl₃** → **花钱做国标氯胺测试依然无法证明测的是一氯胺**，Module 7 需要的 DPD 自由/化合区分 + IC 测 Cl⁻ 是**国标之外的加项**，询价必须写明。报价锚点（2026-10）：游离氯 800 元/点位、氯胺 1000 元/点位；全程加标 9000/10000 元、点加标 4000/5000 元。

  **产品结论零变化**：CaSO₃ 氯胺格维持 ⚠️ Untested、claim 禁区维持、A-14 不变、Version A 寿命模型不变、Tier-1 化学（Yiin 1987）未被推翻。**变化的是证据基数的清点与两处此前写错的表述。**

  **⚠️ 为什么 ⚠️ 不退回 ❌**：Gap 2 原文承认「The expected ineffectiveness is **inferred**」—— 把「没找到数据」当反面证据，这一步确实无效；而供应商 2023 那份报告仍是一条**物种写明**的正向观测（尽管无 pH、无对照、无方法、无检出限、去除率反算）。**一条不足以支撑宣称，但足以说明「不是已知无效」。** 变的是支持假设的证据**条数**，不是它**是否存在**。

  **方法学纪律再收紧一条**：原先写「投加前必须书面确认试剂 CAS」，现在升级为**准入门槛** —— 物种未经物种特异性方法确认的加标测试，**数据点直接作废**，不是「事后补个记录」。KES 三次自测（≤09-24 / 10-15 / 至今无）无一次确认过物种。另外新增一条现场纪律：**标称浓度必须由方法读出**——两次挑战液的标称值都比色卡读数高 2–4 倍（4 vs 1–2 区；2 vs 0.5–1 ppm），而稀释误差、配液后衰减、色卡读低三者均未排除。

  **留给 owner（agent 不代答）**：① 是否接受「10-09 数据点正式退出氯胺证据」；② 09-24「直接亚硫酸钙即可、无需 ACF」这个架构结论（唯一支撑就是被降级的照片）是否重审；③ 10-12 所提「亚硫酸钙量只有 20g 左右」与台架 130 g / V1 BOM 110 g 是否同一对象；④ 运营确认包装与电商页无「除氯胺 / chloramine removal / 秒去」字样在流通（wiki 内 `site/` 与 claim 台账本轮已巡检，口径为禁、无冲突）；⑤ strategy 按 Module 7 新口径排期与询价。

  **合规巡检结果**：wiki 内对外页面与 claim 台账当前口径均为**禁止氯胺宣称**，本次裁定反而**加强**了这条禁令的依据，**无需改动任何对外文案**。

  **owner 答复（2026-10-28，当日）**：**① 接受** —— 裁定生效，10-09 台架正式退出氯胺证据，「KES 物种确认氯胺数据点 = 0」成为后续一切氯胺讨论的事实前提。**② 确认** —— 包装与电商页面**无「除氯胺 / chloramine removal / 秒去」字样在流通**。**仍开放三项**：09-24「直接亚硫酸钙即可、无需 ACF」架构结论是否重审（产品判断，证据基础已空，本次未改架构页）；10-12「亚硫酸钙只有 20g 左右」的取数口径（不据此改任何计算）；Module 7 排期与询价（规格已更新，排期决定待 strategy）。

## [2026-10-28] maintain | Verification queue 增加永久事项 ID
- source: Kenny 要求执行队列 ID 列与行号引用修复；ops/verification-queue.md；本日志三处历史行号引用
- updated: ops/verification-queue.md; log.md
- status: completed
- notes: |
  为现有 15 条审核事项按迁移时顺序一次性分配 VQ-0001～VQ-0015；后续新增从 VQ-0016 起分配。ID 代表审核事项，同页不同事项分别编号；编辑、排序、结案和归档均保留 ID，不重新编号、不复用，合并并发改动时检查唯一性。
  历史日志原第 16 / 17 / 18 行引用分别补为 VQ-0010 / VQ-0011 / VQ-0012，并保留原行号及事项描述供审计。原 15 条记录的页面、审核原因、级别与责任人均保留；本次不改变业务审核结论或状态。

## [2026-11-08] maintain | 新增 Bathroom Caddy 研究簇（市场速判 + metal-first 混合结构）
- source: Kenny 门店实拍 2 张（Crate&Barrel Caddies 价签与凹槽近景）+ 公开检索；Kenny 追问"加入金属材质解决差评、提高价值感、契合 metal first"
- updated: raw/products/bathroom-caddy/2026-11-08-crateandbarrel-caddy-store-observation.md; wiki/products/bathroom-caddy/bathroom-caddy-marble-market-scan-2026-11-08.md; wiki/products/bathroom-caddy/bathroom-caddy-metal-first-hybrid-design-2026-11-08.md; index.md; log.md
- status: completed
- notes: |
  按 capture → extract → update 落地三份：原始价签逐字与竞品／PVD／FBA 数据；市场速判（研究 ✓ / 立项 ✗）；metal-first 混合结构设计简报（升级为有条件的概念 GO，仍非产品 GO）。
  设计结论：金属承担结构、定位、排水、饰面与跌落保护，石材退为 3–4mm 可拆换薄嵌片；不采用"整石 + 金属装饰条"。对齐品牌资料 Metal-First Definition（不等于全金属；非金属材料须有意选择、透明说明、按用途测试），并接上"水龙头→柜拉手→门把手同色同店"这一既有定位，把 caddy 作为第 4 个同色触点。
  已记录 FTO 先例：DDBESSIC/CNCEST 201 不锈钢电镀 + 可拆大理石板浴缸托盘、Ruhe 304 PVD 大理石嵌片地漏、C&B 凹槽 + 材质分层；不宣称首创，检索范围收窄到卡扣／磁吸定位、微排水坡、同色 PVD 套系。
  方法学纪律沿用本库既有撤回记录：ΔE 只认分光光度计对实物签样与批次留样，不用照片跨图比色，不引用具体 ΔE 数值。
  全部重量、成本、退货率改善均标为方向性估算；未做样品实测、搜索量验证、FTO 检索与毛利模型。页面 officiality 均为 draft，未写入高信任正式面。

## [2026-11-08] correct | Caddy 差评机理二次核验，撤回过度承诺并补新失效模式
- source: Kenny 追问「引入金属能否解决多孔渗色／酸蚀／硬水水垢／皂垢／发霉 + 太重／砸台面／运输崩边」；8 组公开检索（BSSA、Natural Stone 资料、PVD care 指南、soap scum 化学、霉菌资料、pH 表）
- updated: raw/products/bathroom-caddy/2026-11-08-material-failure-mechanisms-research.md (new); wiki/products/bathroom-caddy/bathroom-caddy-metal-first-hybrid-design-2026-11-08.md; log.md
- status: completed
- notes: |
  撤回上一版「A 六项均改善」「C 六项全部消除」。按机理重判：仅金属面渗色与方解石酸蚀为真消除；硬水水垢与皂垢由水质与蒸发决定、与基材无关，金属完全不解决；发霉靠装配纪律且混合结构界面更多、设计不当会反噬；太重／砸台面／崩边靠减重与结构细节。
  关键新发现：哑黑 PVD 上白色 CaCO3 对比度最高、最显水垢，而 PVD 又最怕酸性除垢剂（变色／点蚀／分层）⇒ 存在「过度清洁 → 涂层损坏 → 保修争议」的反向组合陷阱，上一版未覆盖。
  风险转移：304/316 对盐酸任何浓度／温度均不推荐（BSSA），≥5% 含氯漂白剂室温可致腐；方解石酸蚀机理消失，但改怕氯离子与强酸。
  口径纠正：牙膏通常 pH 7–9、pH 平衡洗手液 5–6、真皂 9–10，并非主要酸蚀源；真凶是 pH 1–3 除垢剂与 pH 1–2 洁厕灵。牙膏对石材主要是研磨划伤与残留白膜。
  结论修订：真正杠杆是「不积水 + 可拆洗 + 快干」，金属的作用是让这套结构做得薄、精确、耐久、可同色。与软水主线仅为内容／叙事协同（共同变量 Ca2+/Mg2+），非技术协同，不改变「不独立立项」结论。
  简报同步更新：第 2 节方案表、第 4 节全表重写 + 4.1/4.2/4.3、第 5 节门禁新增清洁剂误用声明／水垢可见度／缝隙滞水／薄壁抗凹、第 8 阶段 2 测试项、第 9 Claim 禁区（禁写防垢／不结水垢／免擦洗）、第 10 边界、Sources。
  所有化学机理与 pH 均标注为公开资料二次核验，非 KES 台架实测；冷凝、凹陷率、哑黑水垢差评权重列为待验证假设。未做 git 提交、未同步 kenny-wiki。

## [2026-11-08] research | 双层石纹陶瓷层板置物架：两平台销售实况与需求缺口
- source: Kenny 纠正产品对象（非边几，是浴室／厨房双层置物架）并说明 KES 已有类似陶瓷层板产品、这次只改形态；要求深入调查 Amazon / Wayfair 销售与未满足需求。4 路并行检索（Amazon listing、Wayfair 与跨渠道、VOC 差评引文、多源综合）+ 3 组补充核验
- updated: raw/products/bathroom-caddy/2026-11-08-two-tier-ceramic-shelf-market-evidence.md (new); wiki/products/bathroom-caddy/two-tier-ceramic-shelf-market-opportunity-2026-11-08.md (new); index.md; log.md
- status: completed
- notes: |
  核心结论：不是蓝海，是「已被验证但功能创新停滞」的赛道。Amazon 上 Dobbyby 已把「石纹可拆陶瓷托盘 + 不锈钢框」做成 $44.99–47.69 / 4.6★ / 1,514 评 / BSR #19 Bathroom Trays / 200–300+ 月购，另有 Sweese 895 评、Kanwone 401 评 ⇒ >$40 陶瓷带有真实量；真天然石款评论量反而低。Wayfair 同形态 SKU 成体系（Orren Ellis / 17 Stories / Ivy Bronx / Rebrilliant）但评论 0–54 条、标价 $100–176 靠 −39%～−70% 折扣，真正有口碑的是 $26.99 / 54 评的玻璃壁挂架。
  需求缺口的本质：解法都在但都在别的品类——可调层高（Kitstorack 水槽下架 5 档）、镂空排水（转角架）、72h 盐雾（玻璃壁挂架）、免工具快装与防崩垫片（Dobbyby 自己），没人搬进石纹装饰架。按证据强度排序：① 层高固定／净层高不标注（中强）② 潮湿环境框体与螺丝锈蚀、金色发绿（强）③ 陶瓷到货破损且只换整件（强）④ 晃动与螺丝过短（强）⑤ 积水与垫圈藏污（中）⑥ 同色套系（中偏弱，直接买家引文未见）⑦ 餐桌食品接触（弱，不下重注）。
  形态建议：错层可调双层台面架，下层净高 ≥24cm、主图标净层高；6mm 陶瓷层板做可换嵌片、304 全周包边、可拆弹性垫、1–2° 排水坡；框体一体焊接、层板可拆；304/316 + PVD 四色，首发拉丝不锈钢／枪灰而非哑黑；层板单独补发 SKU + 分格泡棉。变体顺序：浴室台面 → 厨房 → 壁挂 → 餐桌（不做首发，食品接触证据弱）。
  口径纪律：两平台均不公开销量，所有月销／BSR／搜索量标为第三方估算或缓存快照且互相矛盾（同一 Dobbyby ASIN 出现 50+/200+/300+），投产前须 Helium 10 / Keepa / Brand Analytics 复核；Reddit 一手帖被反爬拦截标为未见；Wayfair damage allowance 本轮第三方口径 2%–5%（另有 4%–10% 说），与上一轮口头「4–8%」不一致，官方 MSA 未见，已在两份文档标注须索取官方文本。
  修正同日上一轮误判：产品不是落地边几／家具，「供应链零复用、两平台均不切入」结论撤回；但「已有陶瓷层板能力」在全库检索无对应产品文档，仅作为 Kenny 口述前提，不推断工艺／尺寸／成本。材质标注只能用 marble-pattern / porcelain / stone look，不写 marble 或 sintered stone（小件无该搜索心智）。
  边界：未做样品实测、搜索量验证、FTO 检索、供应商报价与毛利模型；页面 officiality 均为 draft，未写入高信任正式面。未做 git 提交、未同步 kenny-wiki。

## [2026-11-08] research | 餐桌甜点／糕点摆架细分销量与第三次对象校准
- source: Kenny 第三次校准——原始照片「应该是餐桌实物／甜点糕点的置物架」，要求重新研究该细分品类销量。重看旋转图与局部放大确认：矩形平板无围边、上下平行错位、细黑 U 形框、周围为玻璃碗与高脚杯等餐具陈列。3 路并行专项检索（Amazon 销量、Wayfair 与跨渠道、VOC 差评）+ 2 组补充核验 + 图片复判
- updated: raw/products/bathroom-caddy/2026-11-08-tiered-dessert-stand-market-evidence.md (new); wiki/products/bathroom-caddy/tiered-dessert-stand-segment-2026-11-08.md (new); wiki/products/bathroom-caddy/two-tier-ceramic-shelf-market-opportunity-2026-11-08.md（修正 6 处）; index.md; log.md
- status: completed
- notes: |
  核心结论：销量成立、缺口真实、且 KES 的 U 形框形态天然避开该品类第一大痛点（中柱晃动／头重脚轻，≥8 独立来源）；但价格带更低、季节性强、需新建食品接触合规、与同色套系几乎无连带 ⇒ 「更好的形态差异化，更差的 KES 生意」。定位为共用陶瓷层板的第二场景变体，有限试水，不首发、不作主线。
  销量实况：Amazon Cake Stands／Cupcake Stands 类目 Top10 均月销约 2,800、均价 $19.58 [三 ASINSIGHT，自相矛盾]；头部 Sumerflos $25.99/2,762 评/800+ 月、MALACASA $32.99/446 评/1K+ 月、PinCute 1K+ 月、Vecxoty #1 Cupcake Stands/700+ 月。Top3 点击份额仅 14.8%、转化 7.7%，极度分散；$20–35 占 69%，>$40 降一个数量级，>$60 长尾；真大理石款评数 12–512 无一破千。Wayfair 真石 SKU 评论 0–22（最高 AllModern 59），标价 $57–142 靠 −39%～−74% 折扣；2,883 评爆款是 Birch Lane 木+中柱，形态无关。
  精确形态空白：Amazon US 与 11 个零售渠道均未查到「两层矩形石纹薄板 + 细黑 U 框」在售 SKU，非 Amazon 仅 Daraz.pk 一款 0 评；渠道主流是同心圆盘 + 中央立柱。空白位不可反推为需求证据。
  上一轮结论修正：「餐桌食品接触证据弱」升级为**明确硬门槛**——Wayfair 多个真石 SKU 页面直标 Food Safe: No + Prop 65；FDA CPG 7117.06/07 铅镉溶出（扁平器皿 Pb≤3.0/Cd≤0.5 mg/L，4% 乙酸 22±2℃/24h），石纹釉上彩／贴花属高风险且一份报告不可跨花面套用；全品类未查到任何品牌公开第三方检测报告（这同时是空位）。已在旧文档 §1 校准、§3 表格第 7 项、§4 变体 4、§7 证据强度、related 与 Sources 共 6 处修正，两份文档并存不互相覆盖。
  VOC 组合空位：「可拆洗 + 不积水不藏污 + 可平放收纳 + 食品接触安全可证明」全市场无人做全，MALACASA 最多两项（且为厂商宣称）。中柱晃动／到货破损／缺件补件三类为强证据。同色套系诉求**无任何直接买家引文**，属产品假设，已写入 Claim 禁区。
  季节性证据冲突：Accio 系 Google Trends 转述称 11 月峰值 100 vs 6 月 31、C&B/Pottery Barn 节日文案与批发双峰（婚礼季 1–3 月、节日季 9–10 月下单）一致；但 Flapen UK 站称「无显著峰值 1.5×」且主词 cake stand 年搜 −17.8%、afternoon tea stands −57.9%、转化率仅 1.0–1.2%。Keepa 实测曲线与渠道官方上架日历未见。今天 2026-11-08，2026 Q4 窗口已关闭，下一可执行窗口为 2027 春季婚礼季或 2027 Q4。
  口径纪律：所有月销／BSR／评数为缓存快照或第三方估算，ASINSIGHT 同一 ASIN 出现 8K/7K 两版本、Sumerflos 评数三版本、Godinger 233/244/5223 三种口径，已列「数据矛盾与未查到清单」随结论保留；投产前须 Helium 10 / Keepa / Brand Analytics 复核。Reddit 一手帖被反爬拦截；2026 年 AI 联盟评测站含虚构评分已全部排除。
  边界：未做样品实测、搜索量验证、FTO、供应商报价与毛利模型、KES 现有陶瓷层板工艺成本核对、Wayfair 官方 MSA、FDA CPG 官方原文直链。未做 git 提交、未同步 kenny-wiki。

## [2026-11-08] research | 食品接触面材料决策：陶瓷水转印与广西白大理石
- source: Kenny 追问「陶瓷如果转水转印上大理石花纹，作为食品的器皿属于高风险？大理石（广西白）安全吗？」。2 路并行专项检索（水转印工艺与法规、广西白矿物与食品接触）+ 4 组补充核验（含现行标准版本核实）
- updated: raw/products/bathroom-caddy/2026-11-08-food-contact-ceramic-decal-and-guangxi-white-evidence.md (new); wiki/products/bathroom-caddy/food-contact-materials-decision-2026-11-08.md (new); wiki/products/bathroom-caddy/tiered-dessert-stand-segment-2026-11-08.md（related 与 Claim 禁区）; index.md; log.md
- status: completed
- notes: |
  核心结论：两种「水转印」都不能用在承放食物的正面，但机理不同。(A) 陶瓷水转印花纸＝釉上彩（700–850℃ 烤花、铅硼硅低熔熔剂 + 镉系颜料 CdS/CdS·Se、彩料裸露在釉面），是铅镉溶出风险最高一类；花纸供应商自己写「DO NOT decorate on surfaces that come in contact with food or drink unless decal is In-glaze」。(B) 水披覆 hydrographics＝PVA 膜 + 溶剂油墨 + 活化剂 + PU/UV 面漆，风险是有机涂层迁移且 GB 4806.4 只管 Pb/Cd 不覆盖有机迁移物，须另按 GB 4806.10-2016／21 CFR 175.300 做全组分正面清单与迁移评估，食品接触面几乎缺合规路径。平板满版石纹业界主流其实是数码喷墨 + 1200–1280℃ 一次烧成，不是水转印；花纸有收缩/接缝/气泡/封面油残留，水披覆为 3D 曲面工艺。
  风险排序：通体坯/喷墨 ≥1200℃ ≲ 釉下彩 < 釉中彩 ≥1100℃ << 釉上彩/低温花纸 < 有机水披覆。满版放大所有失效；EU 84/500/EEC Art 2(5) 明文复测须「同形状、尺寸、装饰和釉料」≥3 件 ⇒ 一份报告不可跨花面/釉料/颜料批次/烤花曲线套用。
  **重要纠错（不得写入规格书）**：多个检测机构营销页声称「GB 4806.4-2023 于 2024-09-06 实施、Pb 降至 0.5 mg/L、Cd 0.1、新增 6 元素」，为不实信息。CFSA 标准平台标 GB 4806.4-2016「现行」；2023 年 NHC 第 6 号公告 17 项食品接触材料标准 = 塑料/金属/橡胶/复合材料/油墨 5 项 + 12 项 GB 31604 方法标准，不含陶瓷；上海市监局 2024 版目录只列 2016 版；瑞昌 2025、太原 2026、重庆 2026 抽查细则与厦门市 2026-11-04 通报仍以 2016 版判定；且这些页面 Pb 出现 0.5/1.0/0.8 三种矛盾数值。真正更新的是检测方法 GB 31604.49-2023（多元素迁移测定），限值标准未变。规格书须写「GB 4806.4-2016（现行）」并要求实验室报告明示依据版本。
  广西白：放射性不是风险点（贺州牛塘口「贺州白」官方矿区实测 IRa=0.02/Iγ=0.02，GB 6566-2010 A 类，大理石为变质碳酸盐岩不富集 U/Th/K；但属地质报告非成品批次 CMA 证书）。方解石 90–99%、白云石 1–10%，灰纹为泥质/铁质/残留缝合线，官方明确记载黄铁矿与铁质细脉；厂商「CaCO₃>99%、不含硫化物」与官方冲突不可采信。真正问题在：吸水率 0.147–0.22% 吸油渗色（Food & Wine 实测 5 天留下 dark oil circle）、不满足 FDA Food Code 2022 §4-101.11「nonabsorbent」、CaCO₃ 遇酸蚀失光、密封剂只减缓渗色不能防酸蚀且需重涂、禁洗碗机/微波/含氯/碱性清洁剂；以及 CFSA 明文天然石材无专门产品类国标、按 GB 4806.1 企业自评，EU/FDA 亦无专门规定（法国 DGCCRF 1991-08-29 Art.4 最贴近）⇒「不是测了就能过，是没人能告诉你测什么算过」。矿口批次不均质，一份报告不覆盖全部产品，灰纹/暗色条带/铁质线须单独取样。
  行业惯例佐证：Wayfair 真石甜点架标 Food Safe: No + Prop 65，Target/TOV 写「Not food-safe on its own…paired with a plate or liner」，GlobeDecor 写 decorative purpose only + paper doilies ⇒ 真石架本质是装饰件 + 垫盘，不是标注保守。
  三条行动：①先问现有陶瓷层板供应商要「石纹工艺与烧成温度 / 第三方铅镉溶出报告 / 报告对应花面釉料批次」三样，大概率已是喷墨高温烧成，可能根本不用上水转印（全库无 KES 现有陶瓷层板产品文档，仅按 Kenny 口述作能力前提）；②水转印只用于金属框外表面、陶瓷板侧边/底面等非食品接触面，不延伸到上表面口沿、不因滴落叠放构成间接接触，贴合 Metal-First；③食品面只用通体/釉下/釉中/喷墨 ≥1200℃，按目标市场分别出报告（美 FDA CPG 7117.07 Pb 3.0 µg/mL、7117.06 Cd 0.5 mg/L；中 GB 4806.4-2016 扁平 Pb≤0.8/Cd≤0.07 mg/dm²；欧 84/500/EEC；加州 Prop 65 和解口径），有有机涂层加测 GB 4806.10，报告按「器型×花面×釉料批次×烤花曲线×生产批次」绑定。
  公开案例：RASFF 2022.0086 中国陶瓷碟铅 2.3 mg/dm² 从消费者召回、2023.8592 镉 1.15 mg/dm²（限值 0.07）；SAMR 2024 国抽 1 批次铅迁移量不合格；FDA Import Alert 99-45 红名单承接已停用 52-08。诚实边界：通报原文只写迁移超标，工艺归因（釉上彩）来自中国市场监管抽查解读，不是通报原文。
  Claim 禁区补充：FDA 官方不认证单个产品，未取证前不写 food safe / lead free / FDA approved；装饰件定位须给永久性「非食品接触／须配垫盘」说明；不得写「食品级大理石」（不存在该法定身份）、防渗色/不吸油/耐酸/可洗碗机等绝对承诺。
  边界：未做样品实测与第三方检测、KES 现有层板工艺成本核对、广西白成品板材食品接触迁移报告或 A 类成品证书、方铅矿/闪锌矿/含砷矿物在广西白中的检测证据、ISO 6486-2 具体限值（ISO 官网付费）、GB 4806.4-2016 中文全文 PDF 直抓。未做 git 提交、未同步 kenny-wiki。

## [2026-11-08] research | 装饰陶瓷作 riser / cupcake stand 的产品责任：Food Safe: No 无效
- source: Kenny 追问「用 (A) 水转印花纸做的陶瓷盆作为 riser cupcake stand，是否有产品责任风险？即使标明 food safe no？」。3 路并行专项检索（美国产品责任法 / 监管与平台 / 合规替代路径与成本）+ 主 agent 亲自 WebFetch 与 PDF 直抓核实 3 份决定性原始文件
- updated: raw/products/bathroom-caddy/2026-11-08-decorative-ceramic-product-liability-evidence.md (new); wiki/products/bathroom-caddy/decorative-ceramic-riser-product-liability-2026-11-08.md (new); food-contact-materials-decision-2026-11-08.md（related）; tiered-dessert-stand-segment-2026-11-08.md（related）; index.md; log.md
- status: completed
- notes: |
  核心结论：**有实质产品责任风险，且 `Food Safe: No` 不但挡不住，还构成独立的合规缺陷**。四道关卡全部失守：① FDA 21 CFR 109.16(b) 法定推定；② Restatement (Third) §18 严格责任；③ UCC 2-313/2-316 + FTC net impression 表征矛盾；④ Prop 65 H&S Code §25249.13 明示不免除普通法与法定义务。
  **本轮亲自核实的三份决定性文件**（标【核】）：① eCFR 21 CFR §109.16 全文——"appears to be suitable for food use **will be considered to be for food use unless**"，豁免仅 (b)(1) 显著贴标（字高≥3.2mm + 三句法定措辞逐字使用）+ 底部**永久模压/烧制**同一语句，或 (b)(2) 在潜在食品接触面钻孔；三句为 "Not for Food Use. May Poison Food" / "Not for Food Use. Glaze contains lead. Food Use May Result in Lead Poisoning" / "Not for Food Use—Food Consumed from this Vessel May be Harmful"；(c)(1) 明确 "Decorative" / "For Decorative Purposes Only" 仅为**须置于法定语句之后的可选附加语**。② Cal. H&S Code §25249.13 原文："Nothing in this chapter shall alter or diminish any legal obligation otherwise required in common law or by statute or regulation, and nothing in this chapter shall create or enlarge any defense"；罚则 "in addition to"。③ Johnson v. Casa Collective 和解协议 PDF（12 页，pypdf 提取全文核对）：Kohl's Ceramic Tray「ceramic trays with surface designs containing lead」，被告标 "Decorative Trinket Tray" + "For Decorative Purposes Only"、明言 "not designed or intended for use with food or beverages"、§1.5 不承认违法，**仍付 $1,000 民事罚款 + $11,000 律师费**，承诺装饰铅≤90 ppm + NIOSH 9100 表面≤1.0 µg 或依法警示，并管线上同页/结账前警示与 §25600.2 第三方卖家通知。准确表述：私人执法和解、非「法院判免责无效」，但证明该抗辩未阻断执法。
  条文编号纠错（不得再引错）：Restatement (Third) §16 = Increased harm due to product defect（非可预见误用）；**§18 = Disclaimers, Limitations, Waivers... as Defenses... for Harm to Persons**（非警示缺陷），原文 "do not bar or reduce otherwise valid products liability claims... for harm to persons"；警示缺陷在 §2(c)、警示不能替代安全设计在 §2 cmt l、营销期待在 §2 cmt f、可预见误用在 §2 cmt p/§15 cmt b/§17 cmt c。§18 标题本身即答案。
  免责声明唯一残存效力：在 failure to warn 与比较过失（§17(a)(b)）上作为「已尽提示」的事实证据部分减责，不能全免；铅溶出非显而易见危险，open and obvious 不成立。但 `Food Safe: No` 既不具体、不显著、又被营销抵消，连这层都很弱。
  三条法定出口全不成立：自创措辞 → 未触发豁免且可能构成误导性标注；(b)(1) 法定措辞 → 要在本体印 "May Poison Food" 并烧在底部，与 cupcake stand 营销自毁；(b)(2) 钻孔 → 承放面漏水藏污、放不住纸杯蛋糕，未查到任何在售 riser 采用。加垫盘/衬纸/烘焙纸**不是第四条路**（TOV / Wayfair "paired with a plate or liner" 是行业惯例非合规做法）；109.16 看器物整体「appears suitable」，Amazon FCM 范围按 foreseeable use，GPSR (EU) 2023/988 **Recital 22**（不是 Article）要求安全首先靠设计、警示只缓解剩余风险。「riser 只是底座」也不成立——盆倒扣仍可被翻过来用。
  风险分级：Prop 65 私人执法**高**（2019–2026 多份陶瓷外饰铅 60-day notice，Casa / Sino 同款标签仍和解，§25249.7(b)(1) ≤$2,500/日/项）；平台与保险**高**（listing 可停用、Prop 65 Warning Type 是强制申报字段、BSA §9 ≥$1M、**2026-11-02 起大陆卖家新保单只能经 AIA**、已知含铅+用途错报踩 known loss / intentional act / application misrepresentation）；人身伤害严格责任**中**（有血铅事件或超标数据升高）；进口**中高**（Import Alert 99-45 DWPE、adulteration §402(a)(2)(C)(i)，非 misbranding）；召回 CPSC 估算平均直接成本 $540,000，责任险不赔召回费用。中国卖家送达难（Hague 第 10 条中国已提反对、电邮送达无效）、中美无判决互认条约 ⇒ 原告现实路径是压 Amazon / 保险 / 卖家账户资金。
  推荐路径不变且更明确：**F 平层板 + 数码喷墨/釉中彩 ≥1200℃ 无铅体系 + 金属全周框**；D（仅换无铅花纸）备选但须全系统无铅 + 逐批成品检测，供应商「无铅」自述不可豁免检测；A/B/C 明确不能走。按目标市场分别出报告（US CPG 545.450 / CN GB 4806.4-**2016** / EU 84/500/EEC + 2005/31/EC DoC），绑定「器型×花面×釉料批次×烤花曲线×生产批次」+ Golden Sample；工艺/配方变更须书面通知保险人（中国保险行业协会条款第 21 条，否则不赔）。第三方实验室报价四组互相冲突，仅作量级不进财务模型。
  与前稿关系：食品接触面材料决策「釉上彩禁用」由材料风险升级为**法定推定 + 责任不可豁免**；甜点架细分「食品接触是硬门槛」补上法律形态；浴室/厨房台面主路径不受影响（不承放裸食、不进入食品接触语境），进一步支持「餐桌只作有限试水」。
  口径纪律：全部条文档案标【核】/【原】/【三】/【未】；Casa / Sino 均不承认违法，不得表述为法院判决；Oberdorf v. Amazon 已被全席复议撤销、不得援引；Amazon FCM 官方页系欧洲站/Haul 页，US 站专门页未查到；Wayfair $1M/$2M 保额仅第三方转述。本报告**不是法律意见**，须美国产品责任 + FDA/Prop 65 律师书面确认。
  边界：未做样品实测与第三方检测、未拿到 KES 现有陶瓷层板工艺与报告、未由美国律师出具意见、未做 FTO、未核 Amazon 增强安全类目完整清单与 AIA 保费、未查到本品类人身伤害集体诉讼判决/和解金额或以 not intended for food 成功免责的公开判例。未做 git 提交、未同步 kenny-wiki。

## [2026-11-08] research | riser 定性 + KES 现有浴室陶瓷层架风险评估（首次查库取证）
- source: Kenny 三问——① riser 属不属于 food container？② 用陶瓷做 riser 呢？③ 深入评估我们目前的浴室陶瓷层架产品是否有风险？前两问定性检索，第三问**首次直查 OPS 生产库**（只读）
- updated: raw/products/bathroom-caddy/2026-11-08-kes-ceramic-shelf-existing-product-risk-evidence.md (new); wiki/products/bathroom-caddy/kes-ceramic-shelf-existing-product-risk-2026-11-08.md (new); index.md; log.md
- status: completed
- notes: |
  Q1 定性：**riser 不是任何法域的法定产品类别**。美国 FDA 用 "food contact substance/article" 与 CPG 545.450 的形状分类（flatware/small hollowware/large hollowware/cups-mugs/pitchers）；21 CFR 109.16 用 "appears to be suitable for food use"；EU 用 1935/2004 Art.1(2) 与 84/500/EEC Art.1(2) 的 "intended to come into contact"。故判准是「预期用途 + 可预见用途 + 形态」而非名称。三类 riser：结构型（柱状/框架，通常不落入）、托盘型（有围边平面，高度落入）、中间态（看语境）。**KES 现有产品正好是「有围边」的**（五点自述 "raised edges act as a barrier"），靠 bathroom-trays 类目与化妆品用途词挡住。
  Q2 陶瓷 riser：材料本身不带来义务，形态/语境/材料体系才是变量。两个反向事实——陶瓷比金属**更容易被认成餐具**（陶瓷＝餐具的默认联想），但**只有陶瓷能做到 ≥1200℃ 无铅、可洗碗机、真食品级**（金属要涂层，涂层另受 21 CFR 175.300）。结论：陶瓷 riser 优于金属 riser，但要先选边：做结构/陈列件（形态去容器化 + 非食品类目）或做真食品接触件（无铅釉 + 釉中彩/喷墨 ≥1200℃ + 逐批检测），**中间地带最危险**。
  Q3 首次数据库取证结论：KES 有 5 个陶瓷层架 SKU（HS 6911 章 + material=ceramic），4 个在售——BSC901B-CH/B0DT9PFTS3、BSC900B-CH/B0DT9QVSB7、BSC901B-PG/B0DT9NLSNP、BSC900B-PG/B0DT9RN9CQ，另 BSC223S4-2 无 listing。商品为「双层陶瓷托盘 + 抛光铝手柄 + 手工大理石纹」浴室转角/台面收纳架。US 近 12 个月 2,132 件 / 收入 $84,223 / 毛利仅 $5,631（**毛利率 6.7%**），全站点约 2,420 件 / $10 万；BSC901B-CH 铺 23 个渠道（14 Amazon 站 + HD + Wayfair + Walmart + 4 个 WooCommerce）。
  **做得对的 5 点（别动）**：item_type_keyword=bathroom-trays、tray_type=Bathroom Tray（不是 food/serving tray）；specific_uses=Decorative Items、recommended_uses 全是 Skincare/Makeup/Perfume；pattern=Marble（纹路）而非 material=Marble；care=Wipe With Damp Cloth（未承诺洗碗机）；**不触发 21 CFR 109.16**。
  **5 个真实风险（按优先级）**：R1 **HS 归类错章**【P0】——5 个 SKU 全报 6911102900「其他瓷厨房器具」，CIQ 691110290101「**食品接触陶瓷产品**」、监管条件 A、检验检疫 **R 进口食品卫生监督检验**；正确应 6911900000「其他家用或盥洗用瓷器」，监管与检验检疫均「无」，申报示例即「卫浴套件；陶瓷制；卫生间用」。等于报关层面自认食品接触件，却与 listing 的 required_product_compliance_certificate=Not Applicable、specific_uses=Decorative Items 互相打架 → 一旦查验首先被问铅镉报告在哪。R2 **零测试零认证零 Prop 65**【P0/P1】——product_test_record 在 shelf 三子类 205 条记录中陶瓷/铅/镉/釉类 **0 条**；dim_sku_certification 全表只有 water_efficiency 64/cec 26/doe 12（只有水效能效，无材料安全类），BSC 四 SKU 零记录；**全库无任何 prop65/california 字段**，US listing 66 属性无 safety_warning/supplier_declared_chemical_compliance。R3 **Prop 65 零申报**【P1】，参照 Casa 案 $12,000 和解 ≈ 该线 US 全年毛利 2.1 倍。R4 **文案矛盾**【P2，最便宜】——B0DT9RN9CQ description 写 "Polished brass handles" 而 material=Aluminum、五点写 "polished aluminum"，三处打架；"crack-resistant" 绝对化；"Heat Resistant" 作为 special_feature 暗示可承热物；maximum_weight_recommendation=13.00 无单位；4 个标题把 Handcrafted 拼成 "Hancrafted"；number_of_shelves 一个填 1 一个填 2 却都叫 2-Tier。R5 **形态 + Heat Resistant 构成 109.16 边缘暴露**（观察项，冗余薄）。
  行动清单：P0 本周（近乎零成本）①向工厂要工艺三样：大理石纹是水转印/釉上彩/釉中彩/釉下彩/喷墨、烤花温度曲线、釉料彩料是否无铅及 TDS；②交报关行按 6911900000 复核归类并走正式变更留痕。P1 本月：补铅镉溶出（最不利样品，成品 6 件浸出 ASTM C738/AOAC 973.32）、做 Prop 65 exposure assessment、把测试与认证入系统。P2 季度：修文案、定「主图/A+ 禁食物场景、禁 food/serving/dessert 词」硬约束、评估 Heat Resistant 是否保留。
  新增材料线索：KES 同时有**天然大理石**产品线（BPH284S1/BPH285S1/BPS202S39 系列的「天然大理石底座」），前几轮以为「陶瓷替代大理石」从零开始，实际两线都在跑；但大理石多孔，浴室里洗手液/洁面乳/酸性护肤品滴落的渗色与酸蚀可能比食品场景更常发生，且同样零密封/耐污测试记录，建议另立一项不并入本页。铝件阳极氧化/抛光层在潮湿浴室的耐久性同样无测试支撑。
  边界：**未操作任何平台后台**（Amazon SC / Wayfair Partner Home / HD），数据取自 OPS 已落库快照；工艺完全未知，釉上彩判断均为「若…则…」条件推论；未抓图片视频、未查供应商验厂、未核 BSC223S4-2 无 listing 原因；HS 结论为待报关行确认的建议、非报关意见；毛利为 PnL 口径含分摊；不是法律意见。未做 git 提交、未同步 kenny-wiki。

## [2026-11-08] ops | R1–R4 派单到 OPS（KM 指定执行人/关注人）
- source: Kenny 指示——R1/R2/R3 派给梁育苗、watch 黄金玮；R4 派给 listing owner、watch 设开发负责人
- updated: wiki/products/bathroom-caddy/kes-ceramic-shelf-existing-product-risk-2026-11-08.md（新增 §8 派单记录 + 两处 R4 更正）; log.md
- status: completed
- notes: |
  5 条 OPS 待办已建、逐条回读：ee0677（R1 HS 归类，梁育苗/黄金玮，P0，11-10 18:00）、270bad（R2 工艺取证，同上，P0，11-11 18:00）、2bdff6（R3 铅镉送检+Prop 65+落库，同上，P1，11-27 18:00）、d54095（R4a amz_us 文案，梁雨欣/麦家浚，P2，11-13 18:00）、bfe2c0（R4b amz_us 文案，黄倩敏/麦家浚，P2，11-13 18:00）。
  R4 拆两条的依据：`entity_responsibility` entity_type=listing role=owner 按站点查，amz_us 归 BSC900B-CH/PG = 梁雨欣、BSC901B-CH/PG = 黄倩敏；关注人取 product_variant `developer_owner` = 麦家浚。本次只覆盖 amz_us，EU/UK（李翠莹）与 Wayfair/HD/Walmart（张艳娟）对应文案未审未派。
  **R4 原有两处表述在本轮逐字段复核后更正**：① `maximum_weight_recommendation` 单位并不缺失，两款均为 `13.00 pounds`；② "Hancrafted" 拼写错误只出现在 B0DT9RN9CQ 与 B0DT9PFTS3 两款，不是四款都有。两项已从派单正文剔除，改以「无测试支撑的承重/耐裂声明」与「number_of_shelves 与 2-Tier 矛盾」入单。
  纪律：建单前按主题词严格去重（1107 条派出记录 / 203 条在途，主题词零命中；仅 3 条在正文提到本批 SKU 的无关单，已登记不阻止）；正文按平台五段式；执行人与关注人均经目录查人核 ID；关注人走批量接口写入（单条创建会静默丢弃）。未操作任何平台后台、未私信同事、未建钉钉原生待办。
