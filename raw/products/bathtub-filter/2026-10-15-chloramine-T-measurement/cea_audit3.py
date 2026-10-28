#!/usr/bin/env python3
"""
审计 v3：正确处理倾斜色块。

v2 失败的根因（已通过切图肉眼确认）：
  - 印刷色块是**倾斜的平行四边形**，不是矩形 → 固定 x 带会随 y 漂移出块外
  - 采样 y 带跨到色块下方的数字标签（黑字 → 拉低 L*）→ 阶梯非单调
  - p2_2 色卡位于手的阴影中；p2_3 是强侧光

修正：
  - 自动按列检测色块，色块中心 x 取该列的「饱和粉」像素纵向中位数位置
  - 采样只用色块**上半部**（避开标签与阴影）
  - 每图做单调性检验；单调性不通过的图直接判为「该图不可用」而非硬算
"""
import glob
import numpy as np
from PIL import Image

LEVELS = np.array([0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0])
FILES = ["p2_1.png", "p2_2.png", "p2_3.png", "p2_4.png", "p2_5.png"]
LBL = ["初始", "178L", "356L", "712L", "1068L"]


def srgb_to_lab(rgb):
    rgb = np.clip(np.asarray(rgb, float), 0, 1)
    lin = np.where(rgb <= .04045, rgb / 12.92, ((rgb + .055) / 1.055) ** 2.4)
    M = np.array([[.4124564, .3575761, .1804375],
                  [.2126729, .7151522, .0721750],
                  [.0193339, .1191920, .9503041]])
    xyz = lin @ M.T / np.array([.95047, 1., 1.08883])
    d = 6 / 29
    f = np.where(xyz > d ** 3, np.cbrt(xyz), xyz / (3 * d * d) + 4 / 29)
    return np.stack([116 * f[..., 1] - 16, 500 * (f[..., 0] - f[..., 1]),
                     200 * (f[..., 1] - f[..., 2])], -1)


def find_swatches(path, verbose=False):
    """返回 (colors_lab[N,3], xs[N], n)，按 x 排序。"""
    img = Image.open(path).convert("RGB")
    a = np.asarray(img, float) / 255
    h, w, _ = a.shape
    y0 = int(h * .40)
    sub = a[y0:]
    R, G, B = sub[:, :, 0], sub[:, :, 1], sub[:, :, 2]
    mx, mn = sub.max(2), sub.min(2)
    sat = np.where(mx > 1e-6, (mx - mn) / np.maximum(mx, 1e-6), 0)
    mask = (sat > .06) & (R > G + .02) & (G >= B - .05)

    cs = mask.sum(0)
    thr = max(.03 * cs.max(), 4)
    cols = np.where(cs > thr)[0]
    if len(cols) < 7:
        return None, None, 0
    # 分组
    groups, cur = [], [cols[0]]
    for c in cols[1:]:
        if c - cur[-1] <= 5:
            cur.append(c)
        else:
            groups.append(cur); cur = [c]
    groups.append(cur)
    groups = [g for g in groups if len(g) >= 6]
    if len(groups) < 7:
        return None, None, 0
    groups = sorted(sorted(groups, key=len, reverse=True)[:7], key=lambda g: g[0])

    out, xs = [], []
    for g in groups:
        cx0, cx1 = g[0], g[-1]
        band = mask[:, cx0:cx1 + 1]
        rr = np.where(band.any(1))[0]
        if len(rr) < 4:
            return None, None, 0
        # 色块顶部（最小 y）起，取上部 35% 高度 —— 避开底部数字标签
        r0 = rr[0]
        hgt = max(int((rr[-1] - r0) * .35), 3)
        ya, yb = r0 + 1, r0 + hgt
        xa = cx0 + int((cx1 - cx0) * .30)
        xb = cx0 + int((cx1 - cx0) * .70)
        if yb > sub.shape[0] or xb <= xa:
            continue
        px = sub[ya:yb, xa:xb, :].reshape(-1, 3)
        out.append(srgb_to_lab(px.mean(0)))
        xs.append((cx0 + cx1) // 2)
    return np.array(out), np.array(xs), len(out)


print("=" * 86)
print("v3 修正：按倾斜色块自动检测 + 采样仅取色块上部")
print("=" * 86)
print(f"{'照片':<8}{'检出块数':<10}{'L* 阶梯':<44}单调")
print("-" * 86)
valid = {}
for fn, lab in zip(FILES, LBL):
    cols, xs, n = find_swatches(f"/tmp/cea_imgs/{fn}")
    if cols is None:
        print(f"{lab:<8}{0:<10}{'检测失败':<44}")
        continue
    L = cols[:, 0]
    mono = bool(np.all(np.diff(L) < 0))   # 越深 L* 越低
    steps = np.diff(L)
    print(f"{lab:<8}{n:<10}{' '.join(f'{v:5.1f}' for v in L):<44}{mono}")
    if mono:
        valid[lab] = (cols, xs)
        print(f"{'':<8}{'':<10}级差 = {' '.join(f'{v:4.1f}' for v in steps)}"
              f"{'  ← 1→2mg/L 段级差过小' if steps[4] > -1.5 else ''}")

print()
print(f"单调可用的照片：{list(valid.keys()) if valid else '无'}")
print()

if not valid:
    print("→ 所有照片的色卡阶梯均非单调或检测失败：")
    print("  **「跨图 ΔE 3–30」这一条不能作为定量论据使用。**")
    print("  原因链：手机自动白平衡 + 强侧光 + 阴影 + 色块倾斜 + 标签干扰，")
    print("  使任何基于单张照片的像素级比色都无法达到可信精度。")
else:
    print("基于单调照片做光照不变量插值：")
    print(f"  {'照片':<8}{'插值 mg/L'}")
    for lab in valid:
        cols, xs = valid[lab]
        print(f"  {lab:<8}L* 阶梯可用")
