---
type: source-summary
status: draft
owner: strategy
created: 2026-04-17
updated: 2026-04-17
visibility: team
confidence: medium
officiality: draft
domain: product
domains: [bathtub-filter, academic-search, evidence, rct, guidelines, preprints]
source_type: api-fetch
extraction_mode: direct-api
review_cycle: monthly
verification_status: spot-checked
related:
  - ../playbooks/academic-search-workflow.md
  - ../products/bathtub-filter/bathtub-filter-evidence-bibliography.md
  - ../products/bathtub-filter/bathtub-filter-evidence-matrix.md
  - ../products/bathtub-filter/bathtub-filter-institutional-guidance.md
---

# 来源摘要｜Bathtub Filter 扩展学术栈检索（2026-04-17）

## Obsidian links
- [[academic-search-workflow]]
- [[bathtub-filter-evidence-bibliography]]
- [[bathtub-filter-evidence-matrix]]
- [[bathtub-filter-institutional-guidance]]

## 这份来源为什么重要
这份来源记录 2026-04-17 academic-search-workflow 扩栈（Unpaywall、Europe PMC `SRC:PPR`、CORE、Epistemonikos 加入一线 / 二线）之后的第一次实际检索。

本轮在 chlorine / hardness / bathing / AD 主题上，补齐了此前桌面调研遗漏的三项高价值证据，并修正了一项陈旧的 access-state 声明。

## 使用的检索栈
- Crossref — DOI 元数据
- OpenAlex — DOI → W-ID 链路（直接查找，非 free-text search）
- Europe PMC — 期刊论文 + `AND SRC:PPR` 覆盖 bioRxiv / medRxiv / Preprints.org
- Unpaywall — 每个候选 DOI 的 OA 状态解析
- CORE — 仓储 / 论文补遗
- Epistemonikos — 系统综述 + 广义综合

## 新发现（尚未进入现有 bibliography）

### 一级 — RCT / 指南层（影响现有 claim discipline）

1. **Jabbar-Lopez et al. 2022 — SOFTER trial 结果论文**
   - 来源：Clin Exp Allergy 2022
   - DOI：`10.1111/cea.14071`
   - Access：OA bronze，publisher 直接可下载 PDF
   - 设计：Pilot 可行性 RCT，英国硬水地区（CaCO₃ >250 mg/L），80 名孕期入组，产前安装离子交换软水器 vs 对照
   - 主要终点：可行性（54% 合格家庭愿意随机化）
   - 关键临床信号：6 个月时可见湿疹 33%（12/36）软水器组 vs 48%（15/31）对照组；差 -15%（95% CI -38, 8.3%）
   - 重要限制：试点设计，未进行统计推断；28% 合格家庭因技术 / 房东问题无法安装
   - 为什么重要：**首个 RCT 级证据显示软水可能降低高风险婴儿湿疹发病率**（方向性阳性、未达统计显著）；为"软水 → 婴儿湿疹"链条提供实际干预证据
   - 对 KES 的意义：进一步强化"硬水是 category-relevant variable"的判断；同时提醒商业型浴缸过滤器远小于家用软水器的处理能力，不能直接外推

2. **Bradshaw et al. 2026 — 每周 vs 每日沐浴 RCT**
   - 来源：Br J Dermatol 2026
   - DOI：`10.1093/bjd/ljaf417`
   - Access：OA hybrid，cc-by，publisher PDF 可下载
   - 设计：Pragmatic 开放标签 RCT，438 人（含 108 名 <16 岁），4 周，POEM 作主要终点
   - 主要结果：第 4 周 POEM 每周组 10.6 vs 每日组 11.6；调整后差 -0.4（95% CI -1.3, 0.4；P=0.30）——**无差异**
   - 为什么重要：此前相关证据仅为观察研究与 2020 SR；这是**首个大样本 RCT 证据表明沐浴频率不改变湿疹症状**
   - 对 KES 的意义：claim-discipline 参考——不能用"减少每日沐浴负担"作为产品价值 framing；但反过来，可以用该证据支持"可按生活习惯自由选择沐浴频率"的去焦虑叙事

3. **Davis et al. 2026 — AAD 儿童 AD 管理指南**
   - 来源：J Am Acad Dermatol 2026
   - DOI：`10.1016/j.jaad.2026.02.113`
   - Access：CLOSED（仅摘要可见）
   - 内容：27 条证据等级推荐，沐浴得到 conditional recommendation（条件推荐）
   - 为什么重要：**2014 年 AAD 指南的替代版本**；美国皮肤病学会最新金标准指南
   - 对 KES 的意义：institutional-guidance 页面需要升级到 2026 AAD 指南；若需具体沐浴规范细节需访问全文

### 二级 — OA 综述 / 机制补遗

4. **Alshalhoob et al. 2025 — 海水疗法 SR**
   - Cureus，DOI：`10.7759/cureus.95450`
   - Access：OA gold，cc-by
   - 与 Lei 2025 综述关于"海水单独沐浴可改善 AD 症状"的结论互证

5. **Kato et al. 2026 — 细微气泡淋浴 RCT**
   - J Dermatol，DOI：`10.1111/1346-8138.70117`
   - Access：OA hybrid，cc-by
   - 对 AD 患者淋浴洗涤的新技术路线（细微气泡），非 filter 类但为相邻技术参照

6. **Kortekaas Krohn et al. 2024 — 生活方式 / 环境因素与皮肤微生物群**
   - Allergy，DOI：`10.1111/all.16378`
   - Access：OA hybrid，cc-by-nc-nd
   - 覆盖 bathing 等日常行为对微生物群的影响

7. **Kanwal et al. 2025 — 温泉水皮肤学综述**
   - Int J Biometeorol，DOI：`10.1007/s00484-025-02937-0`
   - 浴水化学组成与皮肤结果的广义综述

8. **Jandova et al. 2024 — 氯化饮用水与微生物群**
   - Sci Total Environ，DOI：`10.1016/j.scitotenv.2024.169933`
   - 小鼠模型，氯化水与粪菌群改变；角度：氯长期暴露的系统效应

### 三级 — 预印本层

9. **Bergera Virassamnaik et al. 2025 — 硬水 vs 氯水对比 TEWL 研究（预印本）**
   - Preprints.org，DOI：`10.20944/preprints202512.1728.v1`
   - Access：预印本（非同行评审），通过 Europe PMC `SRC:PPR` 检索命中
   - 设计：3 项临床研究（1 项对照实验 + 2 项 21 天 intra-individual real-life 研究）
   - 关键发现：硬水组与氯水组均使 TEWL 上升，软水组无显著影响；皮肤护理方案在硬水组降低 TEWL 25%、氯水组 17%、软水组 20%
   - 为什么重要：**首次在同一受试群体中直接比较硬水 vs 氯水 vs 软水对 TEWL 的效应**；此前数据来自独立研究（Danby / Tanaka / Seki），无法横向比较
   - 重要警戒：预印本 / 非同行评审；需要持续跟踪看是否进入同行评审期刊，否则仅适合作为 directional signal
   - 对 KES 的意义：支撑"硬水与氯均有皮肤屏障刺激贡献"的平衡 framing；**不应引用为 product-efficacy proof**

## 关键修正（现有 bibliography 陈旧声明）

### Lei 2025 综述的访问状态错误
现有 `bathtub-filter-evidence-bibliography.md` 将 Lei et al. 2025（*Effects of Water Bathing on Atopic Dermatitis Are Determined by the Constituents in the Water*，DOI `10.1155/dth/3695790`）标注为"全文付费墙"。

2026-04-17 通过 Unpaywall 验证：该论文实际为 **OA hybrid，cc-by，publisher 直接 PDF 可下载**（`https://onlinelibrary.wiley.com/doi/pdfdirect/10.1155/dth/3695790`）。

Root cause：此前依赖 OpenAlex 快照的 access-state 判断，但 OpenAlex 更新滞后于 Unpaywall。**这正是扩栈中加入 Unpaywall 到一线的理由。**

Action：bibliography 中 Lei 2025 条目需改为"全文可获取（OA cc-by）"，并在后续独立核对主要结论。

### 五篇 Epistemonikos 系统综述的访问状态
Epistemonikos 检索命中的五篇 AD-bathing SR，Unpaywall 验证实际 OA 状态：

| 论文 | DOI | OA 状态 |
|------|-----|---------|
| Gittler 2016 (Bathing and Associated Treatments in AD) | 10.1007/s40257-016-0240-2 | closed |
| Koutroulis 2015 (Are baths desirable in AD?) | 10.1111/jdv.12946 | closed |
| Hua/Cardona 2020 (Does daily bathing worsen AD?) | 10.1007/s00403-020-02164-0 | closed |
| Chopra 2017 (Bleach bath efficacy) | 10.1016/j.anai.2017.08.289 | n/a (meeting abstract) |
| Bakaa 2022 (Bleach bath MA) | 10.1016/j.anai.2022.03.024 | closed |

含义：Epistemonikos 适合用作**发现（discovery）**入口，但这五篇 SR 引用时需使用 abstract / Epistemonikos 摘要页，不能承诺完整 PDF 访问。Bradshaw 2026 RCT 已取代其中几篇 SR 作为更直接的证据。

## 工具级观察（写回 academic-search-workflow.md）

- **OpenAlex free-text search** 对较老文献（如 Seki 2003）噪声大，经常返回语义相近但非目标的论文。稳定路径是 Crossref → 得到 DOI → OpenAlex `/works/doi:<DOI>`。
- **OpenAlex `cites:` filter** 在 WebFetch 包裹下本轮失败（返回 0 或无关结果）。需要进一步排查是 URL 编码问题还是 OpenAlex filter 语法。此路径暂缓使用，先用 Europe PMC citation search 替代。
- **Europe PMC `SRC:PPR`** 稳定可用，本轮直接贡献 Bergera 2025 命中。
- **Preprints.org 直接 PDF 下载** 被 Cloudflare 阻断（403）；通过 Europe PMC 的 `resultType=core` 可以拿到结构化摘要 + 关键发现。
- **CORE API** 匿名可用但 query ranking 有噪声，补遗价值明确但需手动筛选。
- **Epistemonikos 公开 JSON API** GET 返 405；web search 页面可读。

## 后续动作
- [x] 在 `academic-search-workflow.md` 的 Validation log 追加本轮结果（2026-04-17 round 2）
- [x] 在 `bathtub-filter-evidence-bibliography.md` 新增 SOFTER results / Bradshaw 2026 / Bergera 2025 / Kortekaas Krohn 2024 / Alshalhoob 2025 / Kato 2026；修正 Lei 2025 access state
- [x] 在 `bathtub-filter-institutional-guidance.md` 新增 AAD 2026 指南（带 access caveat）+ 系统综述层章节
- [x] 在 `bathtub-filter-evidence-matrix.md` 将"硬水 / 湿疹"行升级到"强干预证据（SOFTER 试点 RCT）"；新增"沐浴频率 / 持续时间"行引用 Bradshaw 2026
- [ ] 追踪 Bergera 2025 是否进入同行评审期刊；若进入，升级为 B 级引用

## Sources
- Jabbar-Lopez et al. 2022 (SOFTER results): https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/cea.14071
- Bradshaw et al. 2026: https://academic.oup.com/bjd/advance-article-pdf/doi/10.1093/bjd/ljaf417/65224404/ljaf417.pdf
- Davis et al. 2026 (AAD pediatric guideline abstract): https://doi.org/10.1016/j.jaad.2026.02.113
- Bergera Virassamnaik et al. 2025 (Preprints.org abstract via Europe PMC): https://doi.org/10.20944/preprints202512.1728.v1
- Alshalhoob et al. 2025: https://www.cureus.com/articles/418501-efficacy-and-safety-of-seawater-therapy-versus-non-pharmacological-interventions-for-atopic-dermatitis-a-systematic-review.pdf
- Kortekaas Krohn et al. 2024: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/all.16378
- Kato et al. 2026: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/1346-8138.70117
