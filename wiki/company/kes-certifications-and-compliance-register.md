---
type: synthesis
status: draft
owner: operations
created: 2026-05-30
updated: 2026-05-30
visibility: team
confidence: medium
officiality: draft
domain: operations
domains: [kes, certification, compliance, products, quality-system]
source_count: 5
review_cycle: monthly
verification_status: unverified
related:
  - ./kes-certification-claim-control-matrix.md
  - ./kes-sku-certification-mapping-table.md
  - ./kes-certification-evidence-pack-checklist.md
  - ../source-summaries/kes-doe-cec-public-database-access-2026-05-30.md
  - ../source-summaries/kes-public-certification-model-pattern-inventory-2026-05-30.md
  - ../source-summaries/kes-certification-source-table-readout-2026-05-30.md
  - ../source-summaries/kes-certification-public-reference-scan-2026-05-30.md
  - ../source-summaries/kes-official-online-certification-verification-2026-05-30.md
aliases:
  - KES certificates
  - KES certifications
  - KES compliance
  - KES 证书
  - KES 认证
  - KES 合规备案
name_zh: KES 证书认证与合规登记册
name_en: KES Certifications and Compliance Register
---

# KES 证书认证与合规登记册

## Purpose
这页是 KES 现有 certification / compliance 的公司级索引。

它不替代源表、证书 PDF、官方 listing、DOE CCMS、CEC MAEDbS、WaterSense Product Search 或 ISO 证书原件。它的作用是把每个认证的业务含义、覆盖范围、外部核验路径和资料缺口放在同一张可维护地图里。

SKU / 页面话术使用规则见 [KES Certification Claim-Control Matrix](./kes-certification-claim-control-matrix.md)。SKU 级填表见 [KES SKU Certification Mapping Table](./kes-sku-certification-mapping-table.md)，证据归档见 [KES Certification Evidence Pack Checklist](./kes-certification-evidence-pack-checklist.md)。

## Current Source-Table Snapshot
依据 2026-05-30 直接读取 DingTalk Notable 源表的结果：

| Certification | Evidence type | Institution / standard | Status | SKU coverage |
|---|---|---|---|---:|
| cUPC Certificate | 产品证书 | IAPMO / ASME A112.18.1, CSA B125.1 | 有效 | 335 |
| NSF/ANSI/CAN 61 Certificate – Health Effects | 产品证书 | IAPMO / NSF/ANSI/CAN 61 | 有效 | 202 |
| NSF/ANSI/CAN 372 Certificate – Lead Free | 产品证书 | IAPMO / NSF/ANSI/CAN 372 | 有效 | 202 |
| DOE Compliance Certification | 法定合规备案 | U.S. DOE / 10 CFR Part 429, 430 | 有效 | 493 |
| CEC Compliance | 法定合规备案 | California Energy Commission / California Title 20 | 有效 | 828 |
| CE Certificate of Conformity | 符合性认证 | Global Testing Services / EN 817, EN 1112 | 有效 | 705 |
| UKCA Certificate of Conformity | 符合性认证 | Global Testing Services / BS EN 817, BS EN 1112 | 有效 | 1,142 |
| EPA WaterSense Certification – Lavatory Faucets | 产品证书 | IAPMO / EPA WaterSense Specification | 有效 | 31* |
| EPA WaterSense Certification – Showerheads | 产品证书 | IAPMO / EPA WaterSense Specification | 有效 | 31* |
| ISO 9001:2015 Quality Management System Certification | 管理体系认证 | XQC / ISO 9001:2015 | 有效 | 公司级 |

`*` 源 SKU 表里的 `watersense` 字段没有区分 lavatory faucets 与 showerheads，所以此处先按 WaterSense 总 SKU 数列出。

## Official Online Evidence Found
2026-05-30 深查公开官方/发证机构在线记录后，当前能直接证明 KES 在册的最强证据集中在 IAPMO 与 EPA WaterSense。

| Certification family | Official online evidence | Entity / brand shown | Product / model evidence visible | Evidence strength | Caveat |
|---|---|---|---|---|---|
| cUPC | IAPMO PLD current record, file `10664`; public certificate URL `http://myplc.iapmo.org/certificate#/18134` | `KES HOME (U.S.) LIMITED` | Plumbing Fixture Fittings; ASME A112.18.1-2024 / CSA B125.1-24; 124 public model patterns in certificate-preview data; product families include lavatory / bathroom sink faucets, kitchen / pull-out kitchen faucets, pot fillers, beverage / drinking-water faucets, showerheads, shower valves, shower faucet sets, tub spouts, bathtub faucets | Strong public-current issuer evidence | Public model-pattern count is not internal SKU count; SKU mapping still required |
| NSF/ANSI/CAN 372 | IAPMO PLD current record, file `10666`; public certificate URL `http://myplc.iapmo.org/certificate#/18135` | `KES HOME (U.S.) LIMITED` | Lead Free Plumbing Products; references SDWA section 1417(d), California Health & Safety Code section 116875, and NSF/ANSI/CAN 372-2024; 80 public model patterns | Strong public-current issuer evidence | Lead-free / lead-content only; not lead-removal performance |
| NSF/ANSI/CAN 61 | IAPMO PLD current record, file `N-10665`; public certificate URL `http://myplc.iapmo.org/certificate#/18651` | `KES HOME (U.S.) LIMITED` | Drinking Water System Components - Health Effects; NSF/ANSI/CAN 61-2023; 80 public model patterns | Strong public-current issuer evidence | Health-effects material/contact certification only; not contaminant-reduction performance |
| WaterSense lavatory faucets | IAPMO WaterSense file `16508` and EPA WaterSense API | IAPMO lists `KES HOME (U.S.) LIMITED`; EPA lists brand `KES` | 12 bathroom sink faucet model patterns, all 1.2 gpm; IAPMO listing says current as of 2026-05-30 | Strong public-current issuer / EPA evidence | Internal source-table WaterSense count remains a combined SKU count and must be split by category |
| WaterSense showerheads | IAPMO WaterSense file `16509` and EPA WaterSense API | IAPMO lists `KES HOME (U.S.) LIMITED`; EPA lists brand `KES` | 6 showerhead / handheld shower / shower faucet set model patterns, all 1.8 gpm; IAPMO listing says current as of 2026-05-30 | Strong public-current issuer / EPA evidence | Internal source-table WaterSense count remains a combined SKU count and must be split by category |
| DOE | DOE CCMS is the expected public surface, but KES-specific rows were not retrieved in this pass | Not verified publicly in this pass | No KES-specific public rows captured | Internal source-table evidence only | DOE public endpoint returned HTTP 403 in command-line access; needs browser search export / screenshot or CCMS confirmation |
| CEC | CEC MAEDbS is the expected public surface, but KES-specific rows were not retrieved in this pass | Not verified publicly in this pass | No KES-specific public rows captured | Internal source-table evidence only | CEC search redirected to login surface / timed out from command-line access; needs MAEDbS export / screenshot |
| CE / UKCA | Public search did not find KES-specific Global Testing Services verification records | Not verified publicly in this pass | No public KES-specific issuer record captured | Internal certificate evidence only | Needs certificate numbers, test reports, declarations, and GTS verification channel |
| ISO 9001:2015 | Public search did not find KES-specific XQC / ISO 9001 verification records | Not verified publicly in this pass | No public KES-specific issuer record captured | Internal certificate evidence only | Needs certificate number, legal entity, site scope, accreditation chain, and verification URL |

## Working Interpretation
- KES 的证书体系分成四类：plumbing product listing、drinking-water material / lead-free certification、water-efficiency compliance / labeling、company QMS certification。
- SKU 覆盖数不等于可宣传范围。每个 SKU 的页面、包装、说明书、A+、销售话术都应引用具体适用的 certificate / listing / filing，而不是泛称“KES certified”。
- 证书 PDF 不是最终真相。IAPMO、DOE、CEC、WaterSense 这类体系都应以官方 public directory / database 的当前状态为核验锚点。
- CE / UKCA 需要额外审慎。它们不是普通“质量证书”，而是与适用法规、技术文件、Declaration of Conformity / Declaration of Performance、指定/协调标准相绑定的 conformity regime。
- Public model-pattern matching cannot rely on exact strings only. The 18 WaterSense rows do not exactly equal cUPC strings, but all 18 align with broader cUPC wildcard patterns; the 12 WaterSense faucet rows also align with NSF 61 / 372 faucet patterns after wildcard and `Q` marker normalization. See [KES Certification Claim-Control Matrix](./kes-certification-claim-control-matrix.md).

## Per-Certification Notes

### 1. cUPC Certificate
**Current KES status:** 有效；335 SKU。

**What it means:** cUPC 是 IAPMO R&T 产品 listing / mark 体系的一部分，通常用于证明 plumbing product 对适用 plumbing standards / codes 的符合性。当前源表对应标准为 `ASME A112.18.1` / `CSA B125.1`，即 plumbing supply fittings 标准族。

**Current public evidence:** IAPMO PLD 当前列出 `KES HOME (U.S.) LIMITED` file `10664` 为 `Active`，产品为 `Plumbing Fixture Fittings`，标准为 `ASME A112.18.1-2024/CSA B125.1-24`。IAPMO public certificate-preview data 显示 effective date `2024-12-31`、revised date `2026-03-19`、expiration date `2029-12-31`，并显示 124 个 public model patterns。

**Relevant product scope:** 水龙头、淋浴件、供水 fittings 等 plumbing supply fittings。公开 listing 的 model families 包括 bath / bathroom sink faucets、widespread bathroom sink faucets、kitchen / pull-out kitchen faucets、pot fillers、drinking-water / beverage faucets、fixed / handheld showerheads、shower valves、shower faucet sets、tub spouts、bathtub faucets 等。ASME A112.18.1/CSA B125.1 覆盖 kitchen / lavatory supply fittings、bath and shower supply fittings、showerheads、hand-held showers、body sprays、supply stops 等类别。

**Verification route:** IAPMO R&T Product Listing Directory，按公司名、file number 或 model 查当前 listing。内部资料包还应保存 certificate PDF、file number、issue / revised date、void date、covered model list、mark usage permission。

**Do not overstate:** cUPC 不是饮用水 health effects 证书，也不是 WaterSense / flow-efficiency label；如果页面同时讲 cUPC、NSF 61、WaterSense，需要写清各自覆盖对象。

**Open collection items:** 335 SKU 明细、每个 SKU 对应 public model pattern、certificate PDF、mark artwork 使用规则、listing renewal owner。

### 2. NSF/ANSI/CAN 61 Certificate – Health Effects
**Current KES status:** 有效；202 SKU。

**What it means:** NSF/ANSI/CAN 61 是 drinking water contact 的 health effects 标准，用于评价与饮用水接触的材料、组件、产品和系统。NSF 将 mechanical plumbing devices 纳入该标准范围。

**Current public evidence:** IAPMO PLD 当前列出 `KES HOME (U.S.) LIMITED` file `N-10665` 为 `Active`，产品为 `Drinking Water System Components - Health Effects`，标准为 `NSF/ANSI/CAN 61-2023`。IAPMO public certificate-preview data 显示 effective date `2024-11-30`、revised date `2026-03-19`、expiration date `2029-11-30`，并显示 80 个 public model patterns。公开历史 PDF file `N-10665` 标准为 `NSF/ANSI/CAN 61-2022`、revised date `2024-05-13`、void after `November 2024`，只能作为历史材料。

**Relevant product scope:** 主要落在 drinking-water-contact 的 faucets / pot fillers / beverage faucets / relevant mechanical plumbing devices。当前 public model families 与 NSF 372 file `10666` 对齐，覆盖 bath / bathroom sink faucets、widespread bathroom sink faucets、kitchen / pull-out kitchen faucets、pot fillers、drinking-water / beverage faucets。

**Verification route:** IAPMO Product Listing Directory 为当前状态锚点；也可保存公开/内部 certificate PDF。NSF 61 不必须由 NSF International 本身签发，IAPMO 等认证机构也可按 NSF/ANSI/CAN 标准做 listing。

**Do not overstate:** NSF 61 不是“过滤污染物”或“去除铅”的性能声明。它关注与饮用水接触材料/产品的 health effects，不等于 NSF 53 lead reduction、PFAS reduction 或 filtration performance。

**Open collection items:** 202 SKU 明细、SKU-to-model-pattern 映射、是否含 `Q` optional lower lead requirement 标记、与 NSF 372 的 SKU 对齐关系、current PLD export / screenshot archive。

### 3. NSF/ANSI/CAN 372 Certificate – Lead Free
**Current KES status:** 有效；202 SKU。

**What it means:** NSF/ANSI/CAN 372 是 drinking-water-system components 的 lead content / lead-free 认证路径。它用于证明产品满足 lead content 要求。

**Current public evidence:** IAPMO PLD 当前列出 `KES HOME (U.S.) LIMITED` file `10666` 为 `Active`，产品为 `Lead Free Plumbing Products`，标准/法规文本包括 `Section 1417(d) of the Safe Drinking Water Act`、`Section 116875 of the California Health & Safety Code`、`NSF/ANSI/CAN 372-2024`。IAPMO public certificate-preview data 显示 effective date `2024-12-31`、revised date `2026-03-18`、expiration date `2029-12-31`，并显示 80 个 public model patterns。

**Relevant product scope:** 与饮用水接触的 faucets / components / mechanical plumbing devices，通常与 NSF 61 形成配套，但两个证书的 claim scope 不同。当前 public model families 覆盖 bath / bathroom sink faucets、widespread bathroom sink faucets、kitchen / pull-out kitchen faucets、pot fillers、drinking-water / beverage faucets。

**Verification route:** IAPMO Product Listing Directory 或相应认证机构 listing；内部资料包应保存 certificate PDF 和 model list。

**Do not overstate:** NSF 372 是 lead content / lead-free，不是 lead removal。它不能支持“reduces lead in water”这类过滤性能 claim。

**Open collection items:** 202 SKU 明细、SKU-to-model-pattern 映射、与 NSF 61 的 SKU 对齐关系、页面/包装可用的 lead-free wording、current PLD export / screenshot archive。

### 4. DOE Compliance Certification
**Current KES status:** 有效；493 SKU。源表 2026-05-30 直读显示 DOE 全部已获证；本地 `dim_sku_certification` 2026-05-25 同步仍有 24 个等待下证，已被源表状态 supersede。

**What it means:** DOE compliance 是法定合规备案，不是第三方产品证书。对 faucets 和 showerheads，DOE 依据 10 CFR Part 429 / 430 管 certification report、sampling、certified ratings、record retention 和 enforcement。

**Relevant product scope:** faucets、showerheads，以及相应 basic model / model family。10 CFR 429.28 要求 faucet certification report 包含最大用水量和水压等 public product-specific information；10 CFR 429.29 对 showerheads 要求最大用水量、水压和 flow-restricting insert 机械保持相关声明。

**Verification route:** DOE CCMS certification database / report templates；内部应保存 CCMS submission confirmation、basic model mapping、SKU-to-basic-model mapping、flow test basis。本次公开查证中 DOE public certification-data endpoint 对命令行访问返回 HTTP 403，未能抓取 KES-specific rows。

**Public-database access note:** 2026-05-30 复查 DOE faucet / showerhead certification-data endpoints 仍返回 HTTP `403`，没有取得 KES-specific CCMS rows。DOE 对外证明仍需要浏览器截图、CCMS export 或内部 submission confirmation。

**Do not overstate:** DOE compliance 支持合法销售和 water-use representation，不是产品质量 badge，也不替代 FTC marking / website disclosure、CEC MAEDbS 或 WaterSense。

**Open collection items:** CCMS public search export / screenshot、493 SKU 与 basic model 映射、提交日期、submitter、flow-rate value、test pressure、是否有 pending / withdrawn / discontinued basic model。

### 5. CEC Compliance
**Current KES status:** 有效；828 SKU。

**What it means:** CEC Compliance 是 California Title 20 下的法定备案 / listing。CEC 要求 regulated appliances 满足能效/水效标准，并把性能 certified to CEC；公开 surface 是 MAEDbS。

**Relevant product scope:** California Title 20 里的 Plumbing Fittings，包括 showerhead、lavatory faucet、public lavatory faucet、kitchen faucet、replacement aerator、tub spout diverter 等。

**Verification route:** CEC MAEDbS public database。每个销售到 California 的相关 model 应能在 Approved MAEDbS 中按 manufacturer / brand / model 查到。本次公开查证中 CEC Quick / Advanced Search 从命令行访问被 login surface / timeout 阻断，未能抓取 KES-specific rows。

**Public-database access note:** 2026-05-30 复查确认 CEC Advanced Search 可公开加载，并且 `Plumbing Products` 下有 `Plumbing Fittings` 与 `Plumbing Fixtures` 两个相关 appliance type；Quick Search 在命令行访问中跳转登录。模拟选择 `Plumbing Products -> Plumbing Fittings -> Approved` 后服务端查询超时，仍未取得 KES-specific MAEDbS rows。下一轮应使用浏览器或 CEC 导出功能分别查 `KES`、`KES HOME` 和已知内部 model numbers。

**Do not overstate:** CEC 是 California sale / offering-for-sale compliance，不是全国性质量证书。CEC listing 也不自动说明 WaterSense、NSF 61 或 cUPC。

**Open collection items:** MAEDbS export / screenshots、828 SKU 明细、manufacturer name normalization、flow rate、approved / archived status、California page claim wording checklist。

### 6. CE Certificate of Conformity
**Current KES status:** 有效；705 SKU。

**What it means:** 源表显示由 Global Testing Services 针对 `EN 817`、`EN 1112` 出具 Certificate of Conformity。`EN 817` 通常对应 mechanical mixing valves / sanitary tapware，`EN 1112` 对应 shower outlets / showerheads 类产品性能标准。

**Evidence boundary:** 需要把 GTS certificate、test report、EU Declaration of Conformity / Declaration of Performance、适用法规/指令、产品技术文件分开归档。EU 官方 guidance 明确：CE marking 只适用于被特定 EU harmonised rules 覆盖且要求 CE marking 的产品；如果没有适用 EU 要求，不能使用 CE marking。

**Verification route:** 内部证书原件 + GTS verification channel + applicable EU legislation / harmonised standard check。若只是 EN 817 / EN 1112 conformity certificate，应在内部命名上避免直接扩写成 broad EU CE permission。本次公开查证没有找到 KES-specific GTS verification page / certificate PDF / issuer database result。

**Do not overstate:** 不要把 `EN 817 / EN 1112 tested` 写成“所有欧盟合规已完成”；也不要把 third-party lab certificate 等同于 manufacturer Declaration of Conformity。

**Open collection items:** 705 SKU 明细、GTS certificate numbers、test report numbers、issue date / expiry date、standards edition、applicable EU legal basis、DoC / DoP 文件、欧代 / responsible person 信息。

### 7. UKCA Certificate of Conformity
**Current KES status:** 有效；1,142 SKU。

**What it means:** 源表显示由 Global Testing Services 针对 `BS EN 817`、`BS EN 1112` 出具 UKCA Certificate of Conformity。UKCA 属于 Great Britain 产品合规标识体系，通常需对应 UK legislation、UK Declaration of Conformity 和 designated standards。

**Relevant product scope:** 取决于证书覆盖的 tapware / shower outlet / showerhead model list。SKU 覆盖数显著高于 CE，说明该项可能覆盖更宽的 UK sales assortment，应优先拆出 SKU-family mapping。

**Verification route:** 内部 GTS certificate / report + UK Declaration of Conformity + applicable UK legislation / designated standards。GOV.UK guidance 要求 UKCA/CE 产品持有充分技术资料，并在 DoC 中列出适用法规和标准。本次公开查证没有找到 KES-specific GTS verification page / certificate PDF / issuer database result。

**Do not overstate:** UKCA 不等于 cUPC / NSF / WaterSense，也不自动适用于 EU market。GB、Northern Ireland、EU 的 marking route 需要分开管理。

**Open collection items:** 1,142 SKU 明细、GTS certificate numbers、BS EN standard editions、UK DoC、UK responsible person / importer details、GB vs NI selling rules。

### 8. EPA WaterSense Certification – Lavatory Faucets
**Current KES status:** 有效；31 total WaterSense SKU count shared with showerheads in source table.

**What it means:** WaterSense lavatory faucet certification is an EPA label program for water-efficient, performing bathroom sink faucets and faucet accessories. EPA states WaterSense labeled bathroom sink faucets / accessories use a maximum 1.5 gpm and complete an independent certification process.

**Current public evidence:** IAPMO WaterSense file `16508` lists `KES HOME (U.S.) LIMITED` as issued-to entity and states the listing is current as of `05/30/2026`. It lists 12 KES bathroom sink faucet model patterns, each certified on `2024-07-18` at max rated flow `1.2 gpm`: `L3156ALFF12-**`, `L3156BLFF12-**`, `L4117LFF12-**`, `L4317ALFF12-**`, `L4317LFF12-**`, `L4350LFF12-**`, `L4150LFF12-**`, `L4355LFF12-**`, `L4327ALFF12-**`, `L4327BLFF12-**`, `L3209LFF12-**`, `L3210LFF12-**`. EPA WaterSense API returns the same 12 brand `KES` faucet rows.

**Relevant product scope:** private lavatory faucets and faucet accessories / aerators that meet WaterSense specification. Because the KES source field does not distinguish lavatory faucets from showerheads, current internal count cannot yet be split by SKU category.

**Verification route:** EPA WaterSense product search and/or IAPMO WaterSense certification listing. Internal evidence should preserve WaterSense certificate / model list and the product category.

**Do not overstate:** WaterSense is water-efficiency + performance labeling. It does not certify drinking-water health effects, lead content, cUPC plumbing-code compliance, or company quality management.

**Open collection items:** Split the 31 SKU count into lavatory faucet vs showerhead, map each SKU to the 12 public model patterns, collect WaterSense label usage rules, and packaging/page claim copy.

### 9. EPA WaterSense Certification – Showerheads
**Current KES status:** 有效；31 total WaterSense SKU count shared with lavatory faucets in source table.

**What it means:** WaterSense showerhead certification indicates water efficiency and performance criteria. EPA states WaterSense showerheads use no more than 2.0 gpm and independently certified performance includes spray force, spray coverage, and pressure compensation.

**Current public evidence:** IAPMO WaterSense file `16509` lists `KES HOME (U.S.) LIMITED` as issued-to entity and states the listing is current as of `05/30/2026`. It lists 6 KES model patterns, each certified on `2024-07-18` at max rated flow `1.8 gpm`: `XB6305F18-**`, `XB6230F18-**`, `XB6223F18-**`, `XB6202F18-**`, `P300F18-**`, `J215F18-**`. EPA WaterSense API returns the same 6 brand `KES` showerhead rows.

**Relevant product scope:** showerheads / handheld showers / relevant shower outlet models in the WaterSense listing.

**Verification route:** EPA WaterSense product search and/or IAPMO WaterSense certification listing.

**Do not overstate:** WaterSense showerhead does not equal NSF/ANSI 177 shower filtration performance, cUPC plumbing listing, NSF 61 drinking-water health effects, or DOE/CEC legal filing.

**Open collection items:** Split the 31 SKU count by category, map each SKU to the 6 public model patterns, collect pressure-compensation evidence, label artwork permissions, and SKU-to-listing mapping.

### 10. ISO 9001:2015 Quality Management System Certification
**Current KES status:** 有效；company-level, no SKU granularity.

**What it means:** ISO 9001:2015 is a quality management system standard. ISO describes it as a globally recognized standard that helps organizations improve performance, meet customer expectations, and demonstrate commitment to quality. It is the certifiable standard in the ISO 9000 family, but certification is not mandatory.

**Relevant scope:** Company / factory / legal entity / operational scope stated on the XQC certificate. It does not certify any individual SKU, material, plumbing performance, lead-free status, water efficiency, or market access filing.

**Verification route:** XQC certificate number and verification portal / accreditation chain. Internal evidence should preserve certificate PDF, audit scope, sites, issue date, expiry date, surveillance schedule, and accreditation mark。本次公开查证没有找到 KES-specific XQC / ISO 9001 public verification record。

**Do not overstate:** ISO 9001 can support supplier / process credibility, but it must not be used as a product-safety or product-compliance claim.

**Open collection items:** Certificate PDF, certificate number, legal entity, site scope, audited processes, issue / expiry date, surveillance audit dates, accreditation body, public verification link.

## Cross-Cutting Evidence Checklist
For each certification family, collect:

| Field | Why it matters |
|---|---|
| Certificate / filing number | Enables exact lookup and customer support response |
| Issuer / authority | Separates third-party certifier, regulator, lab, and standard owner |
| Legal entity | Prevents KES HOME, KES faucet brand, factory, importer, and applicant confusion |
| Model list | Prevents SKU over-claiming |
| SKU mapping | Makes listing pages, packaging, and marketplace compliance auditable |
| Issue / revised / void / expiry dates | Tracks renewal risk |
| Standard edition | Prevents outdated-standard drift |
| Current public listing URL or screenshot | Public directory is usually stronger than a static PDF |
| Claim wording allowed | Prevents marketing from turning narrow evidence into broad claim |
| Owner | Assigns renewal and correction responsibility |

## Priority Follow-Ups
1. Archive IAPMO PLD exports/screenshots for files `10664`, `10666`, `N-10665`, `16508`, and `16509`.
2. Export DOE CCMS and CEC MAEDbS records for all KES basic models / SKUs.
3. Split WaterSense 31 SKUs into lavatory faucet vs showerhead and map them to the 18 public model patterns.
4. Collect CE / UKCA certificate PDFs and verify whether they include only EN 817 / EN 1112 testing or a full regulatory conformity basis.
5. Collect ISO 9001 XQC certificate details, scope, sites, and expiry / surveillance dates.
6. Build a SKU-level claim-control table: `SKU -> certification family -> certificate/listing id -> allowed page wording`.
7. Confirm IAPMO wildcard / `Q` marker semantics with issuer evidence or owner review before using normalized inheritance in external-facing claims.
8. Fill [KES SKU Certification Mapping Table](./kes-sku-certification-mapping-table.md) from the next internal SKU export.
9. Use [KES Certification Claim-Control Matrix](./kes-certification-claim-control-matrix.md) as the working control surface until SKU-level mapping is available.

## Sources
- [Source Summary — KES Certification / Compliance Source-Table Readout (2026-05-30)](../source-summaries/kes-certification-source-table-readout-2026-05-30.md)
- [Source Summary — KES Certification Public Reference Scan (2026-05-30)](../source-summaries/kes-certification-public-reference-scan-2026-05-30.md)
- [Source Summary — KES Official Online Certification Verification (2026-05-30)](../source-summaries/kes-official-online-certification-verification-2026-05-30.md)
- [Source Summary — KES Public Certification Model-Pattern Inventory (2026-05-30)](../source-summaries/kes-public-certification-model-pattern-inventory-2026-05-30.md)
- [Source Summary — KES DOE / CEC Public Database Access (2026-05-30)](../source-summaries/kes-doe-cec-public-database-access-2026-05-30.md)
- [KES Certification Claim-Control Matrix](./kes-certification-claim-control-matrix.md)
- [KES SKU Certification Mapping Table](./kes-sku-certification-mapping-table.md)
- [KES Certification Evidence Pack Checklist](./kes-certification-evidence-pack-checklist.md)
- IAPMO R&T Product Listing Directory: <https://pld.iapmo.org/>
- IAPMO PLD API endpoint observed from public app: <https://pld-api.iapmo.org/api/search/myplc>
- IAPMO WaterSense file 16508: <https://mirobase.iapmo.org/pld/listing_watersense.aspx?file=16508>
- IAPMO WaterSense file 16509: <https://mirobase.iapmo.org/pld/listing_watersense.aspx?file=16509>
- IAPMO R&T Water Systems Certification: <https://iapmort.org/certification-services/water-systems-certification>
- IAPMO R&T WaterSense certification: <https://iapmort.org/certification-services/us-epa-watersense-certification/>
- ASME A112.18.1/CSA B125.1: <https://www.asme.org/codes-standards/find-codes-standards/plumbing-supply-fittings-%28with-10-18-errata%29>
- NSF/ANSI/CAN 61: <https://www.nsf.org/water-systems/nsf-ansi-can-61-testing-and-certification>
- NSF faucets and plumbing products: <https://www.nsf.org/consumer-resources/articles/faucets-plumbing-products>
- NSF/ANSI/CAN 372 associated product standards scope: <https://www.nsf.org/knowledge-library/associated-product-standards-scope>
- DOE faucets: <https://www.energy.gov/cmei/buildings/faucets>
- DOE showerheads: <https://www.energy.gov/cmei/buildings/showerheads>
- 10 CFR 429.28 faucets: <https://ecfr.io/Title-10/Section-429.28>
- 10 CFR 429.29 showerheads: <https://ecfr.io/Title-10/Section-429.29>
- 10 CFR 430.32 water conservation standards: <https://ecfr.io/Title-10/Section-430.32>
- FTC 16 CFR 305.24 plumbing product marking: <https://www.law.cornell.edu/cfr/text/16/305.24>
- FTC 16 CFR 305.27 websites and catalogs: <https://ecfr.io/Title-16/Section-305.27>
- CEC appliance certification assistance: <https://www.energy.ca.gov/rules-and-regulations/appliance-efficiency-regulations-title-20/appliance-regulations-certification>
- CEC Public Search Help PDF: <https://cacertappliances.energy.ca.gov/Help/PublicSearchHelp.pdf>
- California Title 20 section 1606: <https://www.law.cornell.edu/regulations/california/20-CCR-1606>
- California Title 20 section 1608: <https://www.law.cornell.edu/regulations/california/20-CCR-1608>
- EPA WaterSense bathroom faucets: <https://www.epa.gov/watersense/bathroom-faucets>
- EPA WaterSense showerheads: <https://www.epa.gov/watersense/showerheads>
- EPA WaterSense Product Search: <https://lookforwatersense.epa.gov/>
- EPA WaterSense API base: <https://api.epa.gov/watersense>
- EU CE marking guidance: <https://europa.eu/youreurope/business/product-requirements/labels-markings/ce-marking/index_en.htm>
- GOV.UK UKCA / CE market guidance: <https://www.gov.uk/guidance/using-the-ukca-marking>
- ISO 9001:2015: <https://www.iso.org/standard/62085.html>
