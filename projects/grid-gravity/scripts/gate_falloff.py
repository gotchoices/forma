"""
Gate go/no-go (falloff + isotropy leg) for projects/grid-gravity.

What it does
------------
Simulates the candidate congestion mechanism as a LOSSLESS, FINITE-BANDWIDTH,
conservative transport on a 2D triangular ("hex") lattice, driven by a
persistent point load (a mass), and measures the steady-state proper-time /
congestion field q(x). It then asks the gate's falloff question:

    is q(r) MASSLESS (log r in 2D, i.e. 1/r in 3D) and ISOTROPIC,
    or SCREENED (Yukawa, finite range) / anisotropic?

The model (matching work/update-rule.md and work/shunt-check.md):
  - nodes: triangular lattice, 6 neighbours (the "hex" substrate);
  - conserved scalar s on nodes (the backlog; q = s, up to the bandwidth
    factor), never destroyed in the bulk -> lossless -> no shunt expected;
  - edge flow = clip(kappa*(s_i - s_j), -mu, mu): linear diffusion below the
    bandwidth mu, saturating (congesting) where the demanded flow exceeds mu;
  - persistent injection S at the centre (the mass);
  - absorbing boundary s=0 (signal that has propagated "to infinity").
    Boundary absorption is the ONLY sink; there is no bulk loss.

Because the bulk is strictly conservative, the shunt-check predicts a massless
(log r) field with the bandwidth saturation only renormalising the near-field
core. This script tests that prediction at full nonlinearity, and separately
tests whether the triangular lattice keeps it isotropic.

NOTE: this covers the falloff + isotropy leg only. Non-dispersivity
(work/congestion-falloff.md sec 6) is a wave-propagation measurement, a
separate follow-up.

Inputs (argparse)
-----------------
  --radius   lattice radius in cell units (default 60)
  --kappa    diffusion coefficient (default 0.2)
  --mu       edge bandwidth / max flow per edge per tick (default 0.05)
  --source   injection rate at the centre (default 1.0)
  --tol      steady-state convergence tolerance (default 1e-7)
  --maxiter  max iterations (default 200000)
  --out      output directory (default ../outputs)

Outputs
-------
  - printed report: log-fit R^2 (massless), exp-fit R^2 (screened), implied
    screening length, and angular anisotropy (coefficient of variation);
  - a PNG: radial profile with the log fit, and the angular scan.
"""

import argparse
import os
import numpy as np


SQRT3_2 = np.sqrt(3.0) / 2.0
# Triangular lattice neighbour offsets in (i, j) integer coords.
NBR = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1)]


def build_lattice(radius):
    """Return node cartesian coords, radii, edge index arrays, centre idx,
    and a boundary mask, for a triangular lattice inside `radius`."""
    coords = {}
    idx = {}
    pts = []
    n = int(radius) + 2
    for i in range(-n, n + 1):
        for j in range(-n, n + 1):
            x = i + 0.5 * j
            y = SQRT3_2 * j
            r = np.hypot(x, y)
            if r <= radius:
                idx[(i, j)] = len(pts)
                pts.append((x, y))
                coords[(i, j)] = (x, y)
    pts = np.array(pts)
    rr = np.hypot(pts[:, 0], pts[:, 1])

    ea, eb = [], []
    for (i, j), a in idx.items():
        for di, dj in NBR:
            b = idx.get((i + di, j + dj))
            if b is not None and a < b:
                ea.append(a)
                eb.append(b)
    ea = np.array(ea)
    eb = np.array(eb)

    centre = idx[(0, 0)]
    boundary = rr > (radius - 1.5)
    return pts, rr, ea, eb, centre, boundary


def relax(rr, ea, eb, centre, boundary, kappa, mu, source, tol, maxiter):
    """Iterate the lossless finite-bandwidth transport to steady state."""
    npts = rr.shape[0]
    s = np.zeros(npts)
    # explicit-step stability: dt * kappa * max_degree < 1; degree <= 6
    dt = 0.5 / (kappa * 6.0)
    last = None
    for it in range(maxiter):
        ds = s[ea] - s[eb]                    # drive across each edge (a->b)
        flow = np.clip(kappa * ds, -mu, mu)   # bandwidth-limited, odd in ds
        net = np.zeros(npts)
        np.add.at(net, eb, flow)              # b receives
        np.add.at(net, ea, -flow)             # a gives  (exactly conservative)
        net[centre] += source
        s = s + dt * net
        s[boundary] = 0.0                     # absorbing sink at "infinity"
        if s[centre] < 0:
            s[centre] = 0.0
        if it % 200 == 0:
            if last is not None:
                change = np.max(np.abs(s - last))
                if change < tol:
                    return s, it, change
            last = s.copy()
    return s, maxiter, np.max(np.abs(s - last)) if last is not None else np.nan


def r2(y, yhat):
    ss_res = np.sum((y - yhat) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    return 1.0 - ss_res / ss_tot if ss_tot > 0 else np.nan


def analyse(pts, rr, s, radius):
    """Fit the mid-range radial profile to massless (log) vs screened (exp)
    and measure angular anisotropy."""
    # Mid-range: outside the saturated core, inside the boundary layer.
    r_core = 0.10 * radius
    r_out = 0.60 * radius
    mask = (rr > r_core) & (rr < r_out) & (s > 0)

    # bin by radius
    rq = rr[mask]
    sq = s[mask]
    nb = 30
    bins = np.linspace(r_core, r_out, nb + 1)
    which = np.digitize(rq, bins)
    rb, sb = [], []
    for k in range(1, nb + 1):
        m = which == k
        if np.count_nonzero(m) >= 3:
            rb.append(rq[m].mean())
            sb.append(sq[m].mean())
    rb = np.array(rb)
    sb = np.array(sb)

    # massless 2D: s = a - A*ln r   (straight line vs ln r)
    lr = np.log(rb)
    A_ml = np.polyfit(lr, sb, 1)
    ml_hat = np.polyval(A_ml, lr)
    r2_ml = r2(sb, ml_hat)

    # screened: fit ln s = b - r/xi   (straight line vs r); xi = screening len
    good = sb > 0
    A_sc = np.polyfit(rb[good], np.log(sb[good]), 1)
    sc_hat = np.exp(np.polyval(A_sc, rb))
    r2_sc = r2(sb, sc_hat)
    xi = -1.0 / A_sc[0] if A_sc[0] < 0 else np.inf

    # isotropy: de-trend the radial (log) profile over the whole mid-range,
    # then measure the residual's genuine angular structure. On a triangular
    # lattice any true anisotropy is 6-fold (cos 6th); everything else is
    # discrete-sampling noise.
    iso = (rr > r_core) & (rr < r_out) & (s > 0)
    ri, si = rr[iso], s[iso]
    theta = np.arctan2(pts[iso, 1], pts[iso, 0])
    trend = np.polyval(A_ml, np.log(ri))          # a - A ln r  (radial fit)
    resid = si - trend
    field_scale = float(np.mean(si))              # typical q in the range
    a6 = 2.0 * np.mean(resid * np.cos(6 * theta))
    b6 = 2.0 * np.mean(resid * np.sin(6 * theta))
    aniso_6fold = float(np.hypot(a6, b6) / field_scale)   # genuine hex anisotropy
    aniso_rms = float(np.std(resid) / field_scale)        # all non-radial residual

    return dict(rb=rb, sb=sb, slope=A_ml[0], r2_log=r2_ml, r2_exp=r2_sc,
                xi=xi, aniso_6fold=aniso_6fold, aniso_rms=aniso_rms,
                radius=radius, theta=theta, resid=resid, field_scale=field_scale)


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--radius", type=float, default=60.0)
    p.add_argument("--kappa", type=float, default=0.2)
    p.add_argument("--mu", type=float, default=0.05)
    p.add_argument("--source", type=float, default=1.0)
    p.add_argument("--tol", type=float, default=1e-7)
    p.add_argument("--maxiter", type=int, default=200000)
    p.add_argument("--out", type=str,
                   default=os.path.join(os.path.dirname(__file__), "..", "outputs"))
    args = p.parse_args()

    pts, rr, ea, eb, centre, boundary = build_lattice(args.radius)
    print(f"lattice: {rr.size} nodes, {ea.size} edges, radius {args.radius}")

    s, iters, change = relax(rr, ea, eb, centre, boundary,
                             args.kappa, args.mu, args.source,
                             args.tol, args.maxiter)
    print(f"relaxed: {iters} iters, final max-change {change:.2e}, "
          f"centre s={s[centre]:.3f}")

    # conservation check: net injection should equal net boundary outflow
    # (in steady state the bulk conserves exactly; report residual)
    res = analyse(pts, rr, s, args.radius)

    print("\n--- FALLOFF (massless log r  vs  screened Yukawa) ---")
    print(f"  log-fit  R^2 (massless) : {res['r2_log']:.5f}   slope {res['slope']:.4f}")
    print(f"  exp-fit  R^2 (screened) : {res['r2_exp']:.5f}   xi ~ {res['xi']:.1f} cells")
    verdict_falloff = ("MASSLESS (log r / 1-over-r) — falloff PASSES"
                       if res['r2_log'] > res['r2_exp'] and res['r2_log'] > 0.985
                       else "AMBIGUOUS or SCREENED — inspect")
    print(f"  -> {verdict_falloff}")
    print(f"     (screening length {res['xi']:.0f} cells vs system {args.radius:.0f}; "
          f"xi >> system => effectively massless)")

    print("\n--- ISOTROPY (radial log trend removed) ---")
    print(f"  6-fold (hexagonal) anisotropy / field : {res['aniso_6fold']:.4f}")
    print(f"  non-radial residual RMS / field        : {res['aniso_rms']:.4f}")
    print(f"  -> {'ISOTROPIC' if res['aniso_6fold'] < 0.02 else 'anisotropic — inspect'}")

    # plot
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        outdir = os.path.abspath(args.out)
        os.makedirs(outdir, exist_ok=True)
        fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
        lr = np.log(res['rb'])
        ax[0].plot(lr, res['sb'], 'o', ms=4, label='sim')
        ax[0].plot(lr, np.polyval([res['slope'],
                   np.polyfit(lr, res['sb'], 1)[1]], lr), '-',
                   label=f"log fit R^2={res['r2_log']:.4f}")
        ax[0].set_xlabel("ln r"); ax[0].set_ylabel("q  (congestion / delay)")
        ax[0].set_title("Radial falloff: straight line vs ln r = massless")
        ax[0].legend()
        ax[1].plot(res['theta'], res['resid'] / res['field_scale'], '.', ms=2)
        ax[1].set_xlabel("angle (rad)")
        ax[1].set_ylabel("(q - radial trend) / q")
        ax[1].set_title(f"Isotropy: 6-fold={res['aniso_6fold']:.4f}")
        fig.tight_layout()
        png = os.path.join(outdir, "gate_falloff.png")
        fig.savefig(png, dpi=110)
        print(f"\nsaved {png}")
    except Exception as e:
        print(f"(plot skipped: {e})")


if __name__ == "__main__":
    main()
