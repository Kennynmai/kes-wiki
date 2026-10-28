#!/usr/bin/env python3
"""
审计我上一轮的分析：修正 ROI 标定错误 + 改用光照不变量。

上一轮的两个问题：
  (a) p2_2 的色卡 ROI 落在手的阴影里 → ΔE=30 可能是阴影几何，不是"白平衡"
  (b) p2_3 的色块框整体左偏，最后一格已在卡外空白 → ΔE=10.02 是测到了白卡纸

修正方法：
  1. 手工重标 ROI（逐张核对）
  2. 用「单色卡内的相对位置」代替「绝对 Lab」——把样品 L* 插值到
     它自己那张色卡的 L* 阶梯上，得到无量纲读数。该量对
     曝光/白平衡/阴影都免疫（只要色卡本身单调且未被阴影完全吞掉）
  3. 单调性作为每张图的有效性检验
"""
import numpy as np
from PIL import Image

LEVELS = np.array([0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0])

# 手工重标：7 个色块中心 x（归一化），色块 y 带，样品 y 带，样品 x 带
# 依据 roi_*.png 逐张目视核对；宽度取相邻间距的 55%
S = [
    # fn,        label,   色块7中心x起点,            色块y带,        样品y带,         样品x带
    ("p2_1.png", "初始", [0.196,0.290,0.405,0.510,0.605,0.700,0.795], (0.625,0.715), (0.420,0.575), (0.462,0.532)),
    ("p2_2.png", "178L", [0.230,0.320,0.402,0.480,0.562,0.645,0.730], (0.660,0.752), (0.435,0.592), (0.418,0.488)),
    ("p2_3.png", "356L", [0.190,0.300,0.410,0.518,0.628,0.735,0.842], (0.628,0.712), (0.398,0.552), (0.372,0.462)),
    ("p2_4.png", "712L", [0.172,0.272,0.377,0.482,0.590,0.696,0.800], (0.655,0.768), (0.392,0.602), (0.448,0.522)),
    ("p2_5.png","1068L", [0.128,0.248,0.368,0.488,0.608,0.723,0.838], (0.660,0.772), (0.402,0.598), (0.428,0.535)),
]


def srgb_to_lab(rgb01):
    rgb01 = np.clip(np.asarray(rgb01, dtype=np.float64), 0, 1)
    lin = np.where(rgb01 <= 0.04045, rgb01 / 12.92, ((rgb01 + 0.055) / 1.055) ** 2.4)
    M = np.array([[0.4124564,0.3575761,0.1804375],
                  [0.2126729,0.7151522,0.0721750],
                  [0.0193339,0.1191920,0.9503041]])
    xyz = lin @ M.T / np.array([0.95047,1.0,1.08883])
    d = 6.0/29.0
    f = np.where(xyz > d**3, np.cbrt(xyz), xyz/(3*d*d) + 4.0/29.0)
    return np.stack([116*f[...,1]-16, 500*(f[...,0]-f[...,1]), 200*(f[...,1]-f[...,2])], -1)


def sample(img, box):
    a = np.asarray(img.convert("RGB"), dtype=np.float64)/255.0
    h, w, _ = a.shape
    x0,x1,y0,y1 = box
    xa,xb = int(w*(x0+(x1-x0)*.22)), int(w*(x0+(x1-x0)*.78))
    ya,yb = int(h*(y0+(y1-y0)*.22)), int(h*(y0+(y1-y0)*.78))
    return srgb_to_lab(a[ya:yb, xa:xb, :].reshape(-1,3).mean(0))


print("="*88)
print("修正后：色卡单调性检验（有效性前提）")
print("="*88)
rows=[]
for fn,lab,xs,cy,vy,vx in S:
    img = Image.open(f"/tmp/cea_imgs/{fn}")
    L=[]
    for i,x in enumerate(xs):
        gap = (xs[1]-xs[0]) if i==0 else (xs[i]-xs[i-1])
        L.append(sample(img,(x,x+gap*0.55,cy[0],cy[1]))[0])
    L=np.array(L)
    mono = bool(np.all(np.diff(L)>0))
    # 单调性下的相邻级差（判断该图色卡可用性）
    steps = np.diff(L)
    rows.append((lab,fn,L,mono,steps))
    print(f"  {lab:<7} L* = {' '.join(f'{v:5.1f}' for v in L)}")
    print(f"  {'':<7} 单调={mono}  相邻级差 = {' '.join(f'{v:4.1f}' for v in steps)}"
          f"  {'← 0.1/0.2 区间几乎不可分' if steps[0]<3 else ''}")

print()
print("="*88)
print("光照不变量读数：样品在「自己那张色卡」L* 阶梯上的位置")
print("="*88)
print("  做法：把样品 L* 线性插值到本图色卡 L*(log10 ppm) 曲线上 → 输出 mg/L")
print("  该值对曝光/白平衡/阴影免疫（色卡与样品同框同光照）")
print()
print(f"  {'标点':<8}{'样品 L*':<12}{'插值浓度 mg/L':<18}{'该图 L* 跨度':<14}可信度")
print("  "+"-"*70)
est=[]
for (lab,fn,L,mono,steps),(_,_,xs,cy,vy,vx) in zip(rows,S):
    img = Image.open(f"/tmp/cea_imgs/{fn}")
    v = sample(img,(vx[0],vx[1],vy[0],vy[1]))[0]
    lg = np.log10(LEVELS)
    e = float(10**np.interp(v, L, lg))
    span = float(L[-1]-L[0])
    est.append((lab,e))
    conf = "高" if (mono and span>25 and steps[0]>2.5) else ("中" if mono else "低")
    print(f"  {lab:<8}{v:<12.2f}{e:<18.2f}{span:<14.1f}{conf}")

print()
c0=est[0][1]
print(f"  以「初始」为基准的相对变化：")
for lab,e in est:
    print(f"    {lab:<8}{(e-c0)/c0*100:+6.1f}%")

print()
print("="*88)
print("结论（修正版）")
print("="*88)
vals=[e for _,e in est]
print(f"  光照不变量读数区间：{min(vals):.2f} – {max(vals):.2f} mg/L")
print(f"  全程相对波动幅度：{(max(vals)-min(vals))/c0*100:.0f}%（相对初始）")
print(f"  是否存在单调下降趋势：{'是' if vals[-1]<vals[0]-0.3 else '否 — 读数持平或上升'}")
print()
print("  关键：本方法对光照免疫，因此上述波动不能用曝光差异解释。")
print("  若读数确实持平/上升，则「无净去除」这一条比上一轮更强，")
print("  而「上升是光照造成」的说法被本方法排除。")
