"""
Range test for projects/grid-gravity mechanism 2 (detour/refractive).

Question
--------
Does a localized constraint on the hex lattice, propagated by the ACTUAL
lattice operator, spread as a scale-free 1/r (log r in 2D) isotropic field —
and is that spread INDEPENDENT of the size of the seed loop (so the compact
loop and small/large spatial hexagon loops are equivalent as sources)?

This is the direct test of the loop-unification idea (work/detour-refractive.md,
work/loops-and-range.md): the "loops at all scales" through n0 are the
lattice's own Green's function, and the operator's confirmed masslessness
(linear dispersion) should give a power-law, scale-free response.

Method: the static response of the massless lattice operator is the graph
Laplacian Green's function. Build the triangular ("hex") lattice Laplacian
L, solve L u = s with s a localized SCALAR source (a point, or a ring/"loop"
of a given radius), Dirichlet boundary u=0, and measure:
  - falloff: u vs log r over a WIDE range (power-law/scale-free = straight
    line; Yukawa would curve down) + a screening-length fit;
  - scale-freeness: is the log-slope constant across radial sub-decades;
  - isotropy: genuine 6-fold anisotropy after removing the radial trend;
  - loop-size independence: are the far-field slopes equal for point, small
    loop, and large loop seeds.

No free parameters: the operator is the lattice Laplacian; the answer is
predicted (log r, isotropic, scale-free) and either holds or does not.

Inputs: --radius (default 140), --seeds (loop radii, default "0 6 20").
Output: printed report; a PNG.
"""

import argparse
import os
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import spsolve

SQRT3_2 = np.sqrt(3.0) / 2.0
NBR = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1)]


def build(radius):
    idx, pts = {}, []
    n = int(radius) + 2
    for i in range(-n, n + 1):
        for j in range(-n, n + 1):
            x, y = i + 0.5 * j, SQRT3_2 * j
            if np.hypot(x, y) <= radius:
                idx[(i, j)] = len(pts)
                pts.append((x, y, i, j))
    pts = np.array(pts)
    xy = pts[:, :2]
    rr = np.hypot(xy[:, 0], xy[:, 1])
    N = len(pts)
    rows, cols, vals = [], [], []
    for (i, j), a in idx.items():
        deg = 0
        for di, dj in NBR:
            b = idx.get((i + di, j + dj))
            if b is not None:
                rows.append(a); cols.append(b); vals.append(-1.0)
                deg += 1
        rows.append(a); cols.append(a); vals.append(float(deg))
    L = sp.csr_matrix((vals, (rows, cols)), shape=(N, N))
    boundary = rr > (radius - 1.5)
    return xy, rr, L, boundary, idx


def solve(L, boundary, source):
    """Solve L u = source with Dirichlet u=0 on the boundary."""
    N = L.shape[0]
    free = ~boundary
    Lff = L[free][:, free]
    u = np.zeros(N)
    u[free] = spsolve(Lff.tocsc(), source[free])
    return u


def ring_source(xy, rr, r_seed, width=1.2):
    if r_seed <= 0:
        i0 = int(np.argmin(rr))
        s = np.zeros(len(rr)); s[i0] = 1.0
        return s
    m = np.abs(rr - r_seed) < width
    s = np.zeros(len(rr))
    if m.any():
        s[m] = 1.0 / np.count_nonzero(m)
    return s


def r2(y, yh):
    ss = np.sum((y - yh) ** 2); st = np.sum((y - y.mean()) ** 2)
    return 1 - ss / st if st > 0 else np.nan


def analyse(xy, rr, u, radius, r_seed):
    lo = max(3.0, 1.5 * r_seed, 0.06 * radius)
    hi = 0.62 * radius
    m = (rr > lo) & (rr < hi) & (u > 0)
    rq, uq = rr[m], u[m]
    # radial profile
    nb = 34
    edges = np.linspace(lo, hi, nb + 1)
    w = np.digitize(rq, edges)
    rb, ub = [], []
    for k in range(1, nb + 1):
        mm = w == k
        if mm.sum() >= 4:
            rb.append(rq[mm].mean()); ub.append(uq[mm].mean())
    rb, ub = np.array(rb), np.array(ub)
    lr = np.log(rb)
    coef = np.polyfit(lr, ub, 1)
    r2_log = r2(ub, np.polyval(coef, lr))
    # Yukawa screening fit: ln u = b - r/xi
    cs = np.polyfit(rb, np.log(ub), 1)
    xi = -1 / cs[0] if cs[0] < 0 else np.inf
    # scale-freeness: slope over inner half vs outer half
    h = len(rb) // 2
    s_in = np.polyfit(lr[:h], ub[:h], 1)[0]
    s_out = np.polyfit(lr[h:], ub[h:], 1)[0]
    scalefree = abs(s_in - s_out) / abs(0.5 * (s_in + s_out))
    # isotropy: 6-fold after removing radial trend
    trend = np.polyval(coef, np.log(rq))
    res = uq - trend
    th = np.arctan2(xy[m, 1], xy[m, 0])
    a6 = 2 * np.mean(res * np.cos(6 * th)); b6 = 2 * np.mean(res * np.sin(6 * th))
    aniso = np.hypot(a6, b6) / uq.mean()
    return dict(slope=coef[0], r2_log=r2_log, xi=xi, scalefree=scalefree,
                aniso=aniso, rb=rb, ub=ub)


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--radius", type=float, default=140.0)
    p.add_argument("--seeds", type=str, default="0 6 20")
    p.add_argument("--out", type=str,
                   default=os.path.join(os.path.dirname(__file__), "..", "outputs"))
    args = p.parse_args()

    xy, rr, L, boundary, idx = build(args.radius)
    print(f"triangular lattice: {len(rr)} nodes, radius {args.radius}")
    seeds = [float(s) for s in args.seeds.split()]

    results = {}
    print("\n seed_loop_r   slope(logfit)   R^2_log    screen_xi   scale-free   6fold-aniso")
    for rs in seeds:
        u = solve(L, boundary, ring_source(xy, rr, rs))
        res = analyse(xy, rr, u, args.radius, rs)
        results[rs] = res
        print(f"   {rs:6.1f}      {res['slope']:9.4f}    {res['r2_log']:.5f}   "
              f"{res['xi']:8.0f}    {res['scalefree']*100:6.2f}%    {res['aniso']*100:7.3f}%")

    slopes = [results[s]['slope'] for s in seeds]
    spread = (max(slopes) - min(slopes)) / abs(np.mean(slopes))
    print(f"\n far-field slope spread across seed loop sizes: {spread*100:.2f}%")
    print(" -> " + ("LOOP-SIZE-INDEPENDENT (compact loop == spatial loops as sources)"
                    if spread < 0.03 else "loop-size-dependent — inspect"))
    print(" falloff: " + ("scale-free log r  (massless -> 1/r in 3D)"
                          if all(results[s]['r2_log'] > 0.995 and results[s]['scalefree'] < 0.08
                                 for s in seeds) else "not clean power-law — inspect"))
    print(" isotropy: " + ("isotropic (<0.5% 6-fold)"
                          if all(results[s]['aniso'] < 0.005 for s in seeds)
                          else "check 6-fold"))

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        outdir = os.path.abspath(args.out); os.makedirs(outdir, exist_ok=True)
        fig, ax = plt.subplots(figsize=(6.4, 4.6))
        for rs in seeds:
            r = results[rs]
            ax.plot(np.log(r['rb']), r['ub'] / r['ub'][0], 'o-', ms=3,
                    label=f"seed loop r={rs:.0f}")
        ax.set_xlabel("ln r"); ax.set_ylabel("field (normalized)")
        ax.set_title("Loop-size independence: same scale-free log r far-field")
        ax.legend()
        fig.tight_layout()
        png = os.path.join(outdir, "hex_greens.png")
        fig.savefig(png, dpi=110); print(f"\nsaved {png}")
    except Exception as e:
        print(f"(plot skipped: {e})")


if __name__ == "__main__":
    main()
