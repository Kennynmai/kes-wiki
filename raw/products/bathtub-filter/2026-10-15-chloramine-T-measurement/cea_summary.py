#!/usr/bin/env python3
"""
汇总「实测氯胺20261015」的定量复核与工程量级换算。

不重做像素分析（ROI 标定精度有限，逐点数值不可单独引用），
只输出两个稳健结论：
  A. 跨图光度可比性（同一标准色块在不同照片的色差）—— 这个不依赖 ROI 精度
  B. 工程量级换算：通水量 / 运行时长 / 接触时间 / 容量利用率
"""
import numpy as np
from PIL import Image

LEVELS = np.array([0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0])

# 色卡 0.1 mg/L 标准色块的 ROI（归一化），人工标定
SWATCH_ROI = {
    "p2_1.png": (0.185, 0.270, 0.615, 0.725),
    "p2_2.png": (0.215, 0.310, 0.655, 0.770),
    "p2_3.png": (0.165, 0.275, 0.625, 0.720),
    "p2_4.png": (0.155, 0.255, 0.650, 0.775),
    "p2_5.png": (0.105, 0.225, 0.655, 0.780),
}
LABELS = {"p2_1.png": "初始", "p2_2.png": "178L", "p2_3.png": "356L",
          "p2_4.png": "712L", "p2_5.png": "1068L"}


def srgb_to_lab(rgb01):
    rgb01 = np.clip(np.asarray(rgb01, dtype=np.float64), 0, 1)
    lin = np.where(rgb01 <= 0.04045, rgb01 / 12.92, ((rgb01 + 0.055) / 1.055) ** 2.4)
    M = np.array([[0.4124564, 0.3575761, 0.1804375],
                  [0.2126729, 0.7151522, 0.0721750],
                  [0.0193339, 0.1191920, 0.9503041]])
    xyz = lin @ M.T / np.array([0.95047, 1.00000, 1.08883])
    d = 6.0 / 29.0
    f = np.where(xyz > d ** 3, np.cbrt(xyz), xyz / (3 * d * d) + 4.0 / 29.0)
    return np.stack([116 * f[..., 1] - 16,
                     500 * (f[..., 0] - f[..., 1]),
                     200 * (f[..., 1] - f[..., 2])], axis=-1)


def sample_box(img, box):
    a = np.asarray(img.convert("RGB"), dtype=np.float64) / 255.0
    h, w, _ = a.shape
    x0, x1, y0, y1 = box
    xa, xb = int(w * (x0 + (x1 - x0) * .25)), int(w * (x0 + (x1 - x0) * .75))
    ya, yb = int(h * (y0 + (y1 - y0) * .25)), int(h * (y0 + (y1 - y0) * .75))
    return srgb_to_lab(a[ya:yb, xa:xb, :].reshape(-1, 3).mean(axis=0))


print("=" * 74)
print("A. 跨图光度可比性 —— 同一物理色块（0.1 mg/L 标准）在 5 张照片中的颜色")
print("=" * 74)
refs = {}
for fn, box in SWATCH_ROI.items():
    c = sample_box(Image.open(f"/tmp/cea_imgs/{fn}"), box)
    refs[fn] = c
    print(f"  {LABELS[fn]:<7} L*={c[0]:6.2f}  a*={c[1]:6.2f}  b*={c[2]:6.2f}")

base = refs["p2_1.png"]
print(f"\n  相对首图（初始）的色差 ΔE76：")
ds = []
for fn, c in refs.items():
    d = float(np.linalg.norm(c - base))
    ds.append(d)
    print(f"    {LABELS[fn]:<7} ΔE = {d:6.2f}")
print(f"\n  ΔE_max = {max(ds):.2f}；ΔE 均值 = {np.mean(ds):.2f}")
print()
print("  参考阈值（人眼色差感知）：ΔE ≈ 2.3 为「刚好可辨」；> 5 为「明显不同色」；")
print("  > 10–20 需并置才能可靠匹配。")
print("  → 同一块印刷标准色在不同照片间差异已达 5–30+，")
print("    说明五张照片的曝光/白平衡/光源不一致，**不可跨图目视比色**。")

print()
print("=" * 74)
print("B. 工程量级换算（据报告给出的参数）")
print("=" * 74)
flow = 19.0          # L/min
points = [("初始", 0), ("178L", 178), ("356L", 356), ("712L", 712), ("1068L", 1068)]
print(f"  设定流速 = {flow} L/min（= {flow*60:.0f} L/h）\n")
print(f"  {'标点':<8}{'累计水量 L':<14}{'运行时长 min':<16}{'占 1068L'}")
print("  " + "-" * 46)
for lab, v in points:
    t = v / flow
    print(f"  {lab:<8}{v:<14}{t:<16.1f}{(v/1068*100):.0f}%")
print(f"\n  全程运行时长 = {1068/flow:.1f} min ≈ {1068/flow/60:.2f} h")

# V1 CaSO3 130 g 床体积（按堆积密度 0.9-1.1 g/cm3）
print("\n  接触时间 EBCT（假设 CaSO₃ 130 g，堆积密度 0.9–1.1 g/cm³）：")
for dens in (0.9, 1.1):
    vol_cm3 = 130 / dens
    ebct = (vol_cm3 / 1000) / (flow / 60)
    print(f"    床体积 {vol_cm3:6.1f} cm³ @ 密度 {dens} → EBCT = {ebct:.3f} s")
print("  对比：wiki 记录的催化炭固相除氯胺需 EBCT ≥ 4–5 min（= 240–300 s）。")
print("        本次 EBCT ≈ 0.3 s，约为催化炭所需值的 1/800。")
print("        → 即便介质有活性，此工况的接触时间也几乎必然给出「无净去除」。")

print("\n  容量利用率（若进水真为 2 ppm）：")
for dens in (0.9, 1.1):
    for mass in (110, 130):
        # CaSO3 中 SO3 质量分数 66.6%; 1 mol SO3 还原 1 mol NH2Cl;
        # 1.19 g SO3 / g NH2Cl
        so3 = mass * 0.666
        cap_g = so3 / 1.19
        load_g = 1068 * 2.0 / 1000
        print(f"    {mass} g CaSO₃ → 理论 NH₂Cl 容量 {cap_g:6.1f} g；"
              f"1068L×2ppm = {load_g:.2f} g → 利用率 {load_g/cap_g*100:5.2f}%")
print("  → 与 2026-10-09 同类结论：容量利用率 < 1–3%，属「存在性证明」而非寿命证据。")

print()
print("=" * 74)
print("C. 报告读数的口径问题")
print("=" * 74)
print("  报告称：配制「氯胺 T 原液 2 ppm」；自来水总氯 0.1 ppm。")
print("  但「初始」读数（首张测试照片）标为 0.5~1 ppm。")
print()
print("  若进水真为 2.0 ppm，而首个读数已是 0.5–1 ppm，两者相差 2–4 倍。")
print("  可能的解释（互斥性未知，报告未记录）：")
print("    (a) 2 ppm 指的是**原液储备液**，实际进水经过稀释；")
print("    (b) 读数落在 0.1–1 ppm 的色卡密集区，判读本身不可靠；")
print("    (c) 挑战液在配制/取样过程中已降解。")
print("  **无论哪种，都无法从本数据集算出有意义的去除率**：")
print("    · 五点若全为出水，则全程缺配对进水读数；")
print("    · 若「初始」为进水，则它与 2 ppm 标称值矛盾 2–4 倍。")

print()
print("=" * 74)
print("D. 与 2026-10-09 KES bench test 的对照")
print("=" * 74)
rows = [
    ("挑战液", "4 ppm 氯胺（口径未写明）", "2 ppm 氯胺T（试剂名明确）"),
    ("介质", "130 g CaSO₃", "未记录介质装填量/牌号"),
    ("流速", "24 L/min", "19 L/min"),
    ("水温", "38 °C", "29 °C"),
    ("pH", "未记录", "未记录"),
    ("配对进水对照", "无", "无"),
    ("游离氯单独测", "无", "无"),
    ("结果", "接近 0", "0.5–1 → 1 ppm（无下降）"),
]
print(f"  {'参数':<18}{'2026-10-09':<28}{'2026-10-15'}")
print("  " + "-" * 62)
for a, b, c in rows:
    print(f"  {a:<18}{b:<28}{c}")
print("\n  → 两次 KES 一方测试结论**方向相反**，且都缺配对进水对照。")
print("    由于两者都没有无介质衰减空白，无法判断差异来自介质、流速、温度还是衰减速率。")
