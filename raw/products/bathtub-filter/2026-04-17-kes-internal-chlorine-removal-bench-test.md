# Bathtub Filter — KES Internal Chlorine Removal Bench Test (测试日期 2026-03-20，交付 2026-04-17)

## Purpose
First **direct system-level** free-chlorine removal measurement for KES bathtub filter Version A. Complements the earlier 2026-04-17 internal materials pass, which contained the EBCT / KDF coefficient table and the scaled CaSO₃ life model but **no direct "X ppm in → Y ppm out at Z L/min"** measurement.

## Classification
- Source type: internal-doc / first-party bench test
- Test setting: KES internal bench (not third-party / certified lab)
- Data type: point measurements, no replicates stated
- Extraction mode: verbatim preservation
- **Test conducted**: 2026-03-20 (from video filenames `20260320.mp4`)
- **Delivered to wiki**: 2026-04-17

## Product under test
- Top disc: 35-hole white non-woven fiber disc, 15 mm thickness
- KDF55: 110 g
- Calcium sulfite (CaSO₃): 130 g

This matches the confirmed Version A media stack documented in `wiki/source-summaries/bathtub-filter-kes-internal-product-materials-2026-04-17.md`.

## Test conditions
- **Influent free chlorine**: **5 mg/L** (elevated — higher than US typical 1–2 ppm and higher than NSF/ANSI 177's 2 ppm challenge level; consistent with worst-case municipal or a stress test)
- **Measurement method**: **chlorine test strips** (colorimetric read — confirmed from photo of 5 strips laid out: raw + 4 effluent samples)
- **Pressure**: 0.2 / 0.3 / 0.4 MPa at the first three flow points; 30 L/min point's pressure not annotated on paper (implied ≳0.5 MPa based on 2024-11-07 overflow-test precedent)
- **Water temperature**: not specified on paper (Version A baseline is 38–42°C)
- **Cumulative throughput / filter age at test**: not stated

## Raw results (from photo annotations, paper-verbatim)

| # | 进水压力 | 流速 | Influent | Effluent | Removal | Video filename (2026-03-20) |
|---|---|---|---|---|---|---|
| 1 | 0.2 MPa | 16.5 L/min | 5 mg/L | 0.5 mg/L | ~90% | `16L每分钟流速：余氯5→0.5mg每升——20260320.mp4` |
| 2 | 0.3 MPa | 21 L/min | 5 mg/L | 0.7 mg/L | ~86% | `21L每分钟流速：余氯5→0.7mg每升——20260320.mp4` (有一份 `_20260320.mp4` 重复) |
| 3 | 0.4 MPa | 27 L/min | 5 mg/L | 0.8 mg/L | ~84% | 无独立视频，仅含在 strip 照片中 |
| 4 | (~0.5 MPa) | 30 L/min | 5 mg/L | 1.5 mg/L | ~70% | `31L每分钟流速：余氯5→1.5mg每升——20260320.mp4`（文件名用 "31L" 的四舍五入）|

注：测试人在纸面用 "16.5 L/min" 的精确值标注第一点，但视频文件名用 "16L"；第四点纸面写 "30 L/min"，视频文件名写 "31L"——两处均为四舍五入，实际数据取纸面精确值。

## Strategist's own conclusion (verbatim translation)
> Under raw-water free-chlorine 5 mg/L, the combination of 35-hole white filter cotton (15mm) + KDF55 110g + calcium sulfite 130g achieves good chlorine removal.
>
> 1. 16 L/min: 5 → 0.5 mg/L, ~90% removal
> 2. 21 L/min: 5 → 0.7 mg/L, ~86% removal
> 3. 27 L/min: 5 → 0.8 mg/L, ~84% removal
> 4. 30 L/min: 5 → 1.5 mg/L, ~70% removal

## Physical evidence preserved
- **Photo**: 5 chlorine test strips on white paper with handwritten arrows showing pressure + flow annotations between strips (supplied 2026-04-17)
- **Videos** (3): 16 / 21 / 31 L/min runs filmed 2026-03-20 (27 L/min point appears only in strip photo, no dedicated video)

## Why this matters
- First direct measurement that validates the chain-model prediction (system = 1 − (1 − KDF) × (1 − CaSO₃)) at the system level, not just per-media.
- At 5 mg/L influent (≈2.5× the 2 ppm condition used in the `media-efficacy-at-bath-conditions` life model), the Version A stack still clears 70–90% across the full 16.5–30 L/min US-spout envelope. This is an elevated-stress data point, not the nominal life-model condition.
- Removal trends monotonically with flow rate, consistent with EBCT logic: higher flow → shorter contact time → lower removal. The inflection between 27 L/min (84%) and 30 L/min (70%) is steeper than the earlier stages — possibly indicating breakthrough onset at the upper end of the US-spout envelope **or** pressure-driven channeling at ~0.5 MPa, and warrants replication.

## Known limits
- Single-shot measurements; no replicates, no uncertainty bands
- **Method resolved**: chlorine test strip (colorimetric, coarse discretization — typically 0.5 / 1.0 / 1.5 mg/L graduations, meaning 0.7 / 0.8 mg/L are interpolated reads)
- Influent chemistry (free vs. combined chlorine, pH, temperature, TDS) not disclosed in the delivered summary
- Fresh-filter state (cumulative throughput before the test) not stated — cannot be placed on the life-model curve without that anchor
- Pressure-to-flow conversion (0.2/0.3/0.4/~0.5 MPa → 16.5/21/27/30 L/min) is consistent with the 2024-11-07 overflow-test envelope but means **pressure is the independent variable, not flow** — the "27 → 30 L/min steep drop" may partly reflect pressure (and thus channeling / bed compression) effects, not pure contact-time
- Not independently replicated; belongs to the "internal-experience" tier of evidence (same tier as the KDF coefficient table)

## Cross-refs
- Validation log entry: `wiki/playbooks/bathtub-filter-validation-testing-protocol.md` Module 1
- Analytical integration: `wiki/products/bathtub-filter/bathtub-filter-media-efficacy-at-bath-conditions.md` Section 9.5
- EBCT + chain formula: `wiki/products/bathtub-filter/bathtub-filter-technology-notes.md`
- Prior KES internal materials: `wiki/source-summaries/bathtub-filter-kes-internal-product-materials-2026-04-17.md`
- Overflow envelope (同 0.5 MPa 起步): `wiki/products/bathtub-filter/bathtub-filter-technology-notes.md`（2024-11-07 测试）
