#!/usr/bin/env python3
"""
定量核实「实测氯胺20261015」比色卡读数（手动标定 ROI 版本）。

每张照片同时含 (a) 标准比色卡 7 色块 (b) 试管内液体。
在 CIE-Lab 空间把液体颜色与【同图】色卡做最近邻匹配 → 客观读数。

为什么必须定量而不是目视：
  0.1~1 ppm 是色卡上最拥挤的一段（0.1/0.2/0.5/1 四级挤在一起），
  目视在这个区间的分辨率远达不到要求；
  且五张照片光照差异极大（室内灯 / 室外阴影 / 直射日光），
  跨图目视对比必然引入系统误差。

ROI 依据：/tmp/cea_grid/*.png 的坐标网格图目视标定（960x1280 原图）。
"""
import numpy as np
from PIL import Image

LEVELS = np.array([0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0])

# 手动标定 ROI（归一化 x0,x1,y0,y1，基于 960x1280 网格图目视）
# 每个样本: (文件名, 标签, 报告值, 色卡7色块x区间, 色块y区间, 试管液体y区间, 试管x区间)
SAMPLES = [
    ("p2_1.png", "初始",  "0.5~1",
     [0.185, 0.290, 0.405, 0.510, 0.605, 0.700, 0.795], (0.615, 0.725), (0.415, 0.585), (0.450, 0.545)),
    ("p2_2.png", "178L",  "0.5-1",
     [0.215, 0.310, 0.395, 0.475, 0.560, 0.650, 0.740], (0.655, 0.770), (0.430, 0.600), (0.400, 0.500)),
    ("p2_3.png", "356L",  "1",
     [0.165, 0.275, 0.385, 0.490, 0.600, 0.710, 0.815], (0.625, 0.720), (0.395, 0.560), (0.370, 0.480)),
    ("p2_4.png", "712L",  "1",
     [0.155, 0.255, 0.360, 0.465, 0.575, 0.680, 0.780], (0.650, 0.775), (0.390, 0.610), (0.435, 0.535)),
    ("p2_5.png", "1068L", "1",
     [0.105, 0.225, 0.345, 0.465, 0.585, 0.700, 0.815], (0.655, 0.780), (0.400, 0.605), (0.420, 0.545)),
]


def srgb_to_lab(rgb01):
    """自实现 sRGB → CIE Lab (D65)。"""
    rgb01 = np.clip(np.asarray(rgb01, dtype=np.float64), 0, 1)
    lin = np.where(rgb01 <= 0.04045, rgb01 / 12.92, ((rgb01 + 0.055) / 1.055) ** 2.4)
    M = np.array([
        [0.4124564, 0.3575761, 0.1804375],
        [0.2126729, 0.7151522, 0.0721750],
        [0.0193339, 0.1191920, 0.9503041],
    ])
    xyz = lin @ M.T
    wp = np.array([0.95047, 1.00000, 1.08883])
    t = xyz / wp
    d = 6.0 / 29.0
    f = np.where(t > d ** 3, np.cbrt(t), t / (3 * d * d) + 4.0 / 29.0)
    L = 116 * f[..., 1] - 16
    a = 500 * (f[..., 0] - f[..., 1])
    b = 200 * (f[..., 1] - f[..., 2])
    return np.stack([L, a, b], axis=-1)


def sample(img, box):
    a = np.asarray(img.convert("RGB"), dtype=np.float64) / 255.0
    h, w, _ = a.shape
    x0, x1, y0, y1 = box
    # 取中部区域，避开印刷边框与高光
    xa, xb = int(w * (x0 + (x1 - x0) * 0.25)), int(w * (x0 + (x1 - x0) * 0.75))
    ya, yb = int(h * (y0 + (y1 - y0) * 0.25)), int(h * (y0 + (y1 - y0) * 0.75))
    patch = a[ya:yb, xa:xb, :].reshape(-1, 3)
    return srgb_to_lab(patch.mean(axis=0))


def main():
    print("=" * 86)
    print("一、逐点读数（CIE-Lab 匹配同图色卡；ΔE 为与匹配色块的距离）")
    print("=" * 86)
    print(f"{'标点':<8}{'报告值':<9}{'客观估计':<14}{'匹配色块':<10}{'ΔE':<7}{'次近ΔE':<9}判读")
    print("-" * 86)

    recs = []
    for fn, lab, rep, xs, cy, vy, vx in SAMPLES:
        img = Image.open(f"/tmp/cea_imgs/{fn}")
        cols = np.array([sample(img, (x, x + 0.085, cy[0], cy[1])) for x in xs])
        vial = sample(img, (vx[0], vx[1], vy[0], vy[1]))

        L = cols[:, 0]
        mono = bool(np.all(np.diff(L) > -1.0))
        dE = np.linalg.norm(cols - vial[None, :], axis=1)
        k = int(np.argmin(dE))
        if k == 0:
            est = float(LEVELS[0])
        else:
            x0, x1 = L[k - 1], L[k]
            y0v, y1v = np.log10(LEVELS[k - 1]), np.log10(LEVELS[k])
            if abs(x1 - x0) < 1e-6:
                est = float(LEVELS[k])
            else:
                t = float(np.clip((vial[0] - x0) / (x1 - x0), 0, 1))
                est = float(10 ** (y0v + t * (y1v - y0v)))
        ds = np.sort(dE)
        sep = float(ds[1] - ds[0])
        verdict = "可分辨" if (sep > 3.0 and mono) else ("⚠色阶拥挤" if sep <= 3.0 else "⚠色卡非单调")
        print(f"{lab:<8}{rep:<9}{f'≈{est:.2f} mg/L':<14}{LEVELS[k]:<10.1f}{dE[k]:<7.2f}{ds[1]:<9.2f}{verdict}")
        recs.append((lab, rep, est, float(LEVELS[k]), float(dE[k]), sep, mono, cols[0], cols))

    print()
    print("=" * 86)
    print("二、跨图可比性：同一标准色块(0.1 mg/L)在五张照片中的 Lab 色差")
    print("=" * 86)
    ref = recs[0][7]
    print(f"  {recs[0][0]:<7} 基准  L*={ref[0]:.2f}  a*={ref[1]:.2f}  b*={ref[2]:.2f}")
    spread = 0.0
    for r in recs[1:]:
        c = r[7]
        d = float(np.linalg.norm(c - ref))
        spread = max(spread, d)
        print(f"  {r[0]:<7} ΔE vs 首图 = {d:5.2f}   L*={c[0]:.2f}  {'← 光照/白平衡显著不一致' if d > 6 else ''}")
    print(f"\n  最大跨图同色块色差 ΔE_max = {spread:.2f}")

    # 单图内色卡整体亮度差异（更稳健的曝光指标）
    print("\n  各图色卡整体亮度（7 色块 L* 均值）—— 反映曝光差异：")
    for r in recs:
        print(f"    {r[0]:<7} L*_mean = {r[8][:, 0].mean():6.2f}")

    print()
    print("=" * 86)
    print("三、按报告值直接算去除率")
    print("=" * 86)
    rep_vals = {"初始": 0.75, "178L": 0.75, "356L": 1.0, "712L": 1.0, "1068L": 1.0}
    c0 = rep_vals["初始"]
    print(f"  {'标点':<8}{'累计水量':<12}{'报告读数 mg/L':<16}{'相对初始'}")
    print("  " + "-" * 48)
    for lab, *_ in recs:
        v = rep_vals[lab]
        wl = "0 L" if lab == "初始" else lab
        print(f"  {lab:<8}{wl:<12}{v:<16.2f}{(v - c0) / c0 * 100:+.1f}%")
    print("\n  → 读数随累计水量【上升】而非下降；无任何净去除证据。")


if __name__ == "__main__":
    main()
