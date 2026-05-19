"""
harmonic_tube.py — verify the harmonic-basis tube cross-section family.

The cross-section is the parametric (complex) harmonic curve

    z(t) = R · e^{i t} · w(t)
    w(t) = 1 + a1·cos(N t) + a2·cos(2N t) + i·( b1·sin(N t) + b2·sin(2N t) )

This generalizes the old polar form r(phi) = R[1 + a1 cos(N phi) + a2 cos(2N phi)]:
setting b1 = b2 = 0 makes w real, z = r(t)·e^{it}, and t coincides with the
geometric polar angle phi.  Non-zero b's let the inner/outer harmonic partners
differ, which (among other things) makes a TRUE ellipse reachable at N = 2.

What this script checks / produces:
  1. Ellipse exactness — N=2, a2=b2=0, b1=-a1 should be an exact ellipse.
  2. A_lobe = (1/2pi)∮ over the positive-curvature region — the quark-charge
     integral.  Reports the A_lobe = 4pi/3 (Q_lobe = +2/3) locus in the
     polar slice (b1=0) and with b1 unlocked, to see whether the new knob
     makes the 240/120 quark shape easier to reach.
  3. Convexity / off-axis-extrema diagnostics along the way.

Inputs : command-line (see --help); all have sensible defaults.
Outputs: outputs/harmonic_tube.txt
"""

from __future__ import annotations

import argparse
import numpy as np
from math import pi
from pathlib import Path


def curve(t, R, N, a1, a2, b1, b2):
    """Return z, z', z'' (complex arrays) for the harmonic cross-section."""
    cN, sN = np.cos(N * t), np.sin(N * t)
    c2N, s2N = np.cos(2 * N * t), np.sin(2 * N * t)

    w = 1.0 + a1 * cN + a2 * c2N + 1j * (b1 * sN + b2 * s2N)
    wp = (-a1 * N * sN - 2 * a2 * N * s2N
          + 1j * (b1 * N * cN + 2 * b2 * N * c2N))
    wpp = (-a1 * N**2 * cN - 4 * a2 * N**2 * c2N
           + 1j * (-b1 * N**2 * sN - 4 * b2 * N**2 * s2N))

    e = np.exp(1j * t)
    z = R * e * w
    zp = R * e * (1j * w + wp)
    zpp = R * e * (-w + 2j * wp + wpp)
    return z, zp, zpp


def kappa_and_speed(t, R, N, a1, a2, b1, b2):
    """Signed curvature kappa(t) and arc speed |z'(t)|."""
    z, zp, zpp = curve(t, R, N, a1, a2, b1, b2)
    speed = np.abs(zp)
    # kappa = Im(conj(z') z'') / |z'|^3
    kappa = np.imag(np.conj(zp) * zpp) / speed**3
    return kappa, speed


def a_lobe(R, N, a1, a2, b1, b2, K=20000):
    """Integral of kappa ds over the positive-curvature region of ONE
       fundamental domain t in [-pi/N, pi/N].  Returns (A_lobe, A_saddle)."""
    t = np.linspace(-pi / N, pi / N, K, endpoint=False)
    dt = (2 * pi / N) / K
    kappa, speed = kappa_and_speed(t, R, N, a1, a2, b1, b2)
    ds = speed * dt
    pos = kappa > 0
    A_lobe = np.sum(kappa[pos] * ds[pos])
    A_saddle = np.sum(kappa[~pos] * ds[~pos])
    return A_lobe, A_saddle


def total_turning(R, N, a1, a2, b1, b2, K=40000):
    """Full ∮ kappa ds over the closed curve — should be 2pi."""
    t = np.linspace(0, 2 * pi, K, endpoint=False)
    dt = 2 * pi / K
    kappa, speed = kappa_and_speed(t, R, N, a1, a2, b1, b2)
    return np.sum(kappa * speed * dt)


def solve_a1_for_alobe(N, a2, b1, b2, target=4 * pi / 3,
                       lo=0.01, hi=2.5):
    """Bisection: find a1 so A_lobe(a1) = target, at fixed (N, a2, b1, b2).
       Returns a1 or None if no sign change on [lo, hi]."""
    def f(a1):
        return a_lobe(1.0, N, a1, a2, b1, b2)[0] - target

    flo, fhi = f(lo), f(hi)
    if flo * fhi > 0:
        return None
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        fm = f(mid)
        if flo * fm <= 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return 0.5 * (lo + hi)


def min_curvature(R, N, a1, a2, b1, b2, K=8000):
    """Minimum signed curvature — negative means concave regions exist."""
    t = np.linspace(0, 2 * pi, K, endpoint=False)
    kappa, _ = kappa_and_speed(t, R, N, a1, a2, b1, b2)
    return kappa.min(), kappa.max()


def is_simple(R, N, a1, a2, b1, b2, K=4000):
    """Crude self-intersection / r>0 check: |z| stays positive and the
       turning tangent winds exactly once."""
    t = np.linspace(0, 2 * pi, K, endpoint=False)
    z, zp, _ = curve(t, R, N, a1, a2, b1, b2)
    if np.min(np.abs(z)) < 1e-6:
        return False
    # winding of the tangent should be +1
    ang = np.unwrap(np.angle(zp))
    winding = (ang[-1] - ang[0] + np.angle(zp[0]) - np.angle(zp[-1])) / (2 * pi)
    return abs(winding - 1.0) < 0.1


def ellipse_check(R, a1, K=4000):
    """N=2, a2=b2=0, b1=-a1: confirm z(t) is an exact ellipse.
       Returns max |(x/A)^2 + (y/B)^2 - 1|."""
    N = 2
    t = np.linspace(0, 2 * pi, K, endpoint=False)
    z, _, _ = curve(t, R, N, a1, 0.0, -a1, 0.0)
    x, y = z.real, z.imag
    A = R * (1 + a1)   # semi-axis along x
    B = R * (1 - a1)   # semi-axis along y
    resid = np.abs((x / A)**2 + (y / B)**2 - 1.0)
    foci_sep = 2 * np.sqrt(abs(A**2 - B**2))
    return resid.max(), A, B, foci_sep


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--N", type=int, default=3,
                    help="lobe count for the A_lobe sweep (default 3)")
    ap.add_argument("--target", type=float, default=4 * pi / 3,
                    help="target A_lobe (default 4pi/3 = quark +2/3 charge)")
    ap.add_argument("--K", type=int, default=20000,
                    help="integration resolution per fundamental domain")
    args = ap.parse_args()

    out_dir = Path(__file__).resolve().parents[1] / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "harmonic_tube.txt"

    L = []
    L.append("=" * 78)
    L.append("Harmonic-basis tube cross-section — verification")
    L.append("z(t) = R e^{it} [ 1 + a1 cos(Nt) + a2 cos(2Nt)")
    L.append("                      + i ( b1 sin(Nt) + b2 sin(2Nt) ) ]")
    L.append("polar slice: b1 = b2 = 0  (then t = phi, recovers old r(phi))")
    L.append("=" * 78)
    L.append("")

    # ---- 1. Ellipse exactness ------------------------------------------
    L.append("--- 1. Ellipse exactness  (N=2, a2=b2=0, b1 = -a1) ---")
    L.append(f"  {'a1':>6}  {'semi-A':>9}  {'semi-B':>9}  "
             f"{'foci sep':>9}  {'max |ellipse residual|':>24}")
    for a1 in [0.1, 0.2, 0.3, 0.5, 0.7]:
        resid, A, B, fsep = ellipse_check(1.0, a1)
        L.append(f"  {a1:6.2f}  {A:9.5f}  {B:9.5f}  {fsep:9.5f}  "
                 f"{resid:24.2e}")
    L.append("")
    L.append("  Residual ~1e-15 confirms z(t) is an EXACT ellipse there.")
    L.append("  (semi-A = R(1+a1), semi-B = R(1-a1), foci sep = 4R*sqrt(a1).)")
    L.append("  The polar family can only approximate this shape.")
    L.append("")

    # ---- 2. Total turning sanity ---------------------------------------
    L.append("--- 2. Gauss-Bonnet check: total turning should be 2pi ---")
    for (N, a1, a2, b1, b2) in [(3, 0.5, 0.0, 0.0, 0.0),
                                (3, 0.5, 0.1, 0.3, 0.0),
                                (2, 0.3, 0.0, -0.3, 0.0)]:
        tot = total_turning(1.0, N, a1, a2, b1, b2)
        L.append(f"  N={N} a1={a1} a2={a2} b1={b1} b2={b2}:  "
                 f"total turning / 2pi = {tot / (2 * pi):.6f}")
    L.append("")

    # ---- 3. A_lobe = 4pi/3 locus, polar slice vs b1 unlocked -----------
    N = args.N
    tgt = args.target
    L.append(f"--- 3. A_lobe = {tgt:.5f} (= 4pi/3) locus at N={N} ---")
    L.append("    Q_lobe = A_lobe/2pi = 2/3, Q_saddle = 1/3 — the quark charges.")
    L.append("")
    L.append("  3a. POLAR SLICE (b1 = b2 = 0) — the old tube-function:")
    L.append(f"    {'a2':>7}  {'a1 solving 4pi/3':>18}  {'kappa_min':>11}  "
             f"{'simple?':>8}")
    for a2 in [-0.10, -0.05, 0.0, 0.05, 0.10]:
        a1 = solve_a1_for_alobe(N, a2, 0.0, 0.0, tgt)
        if a1 is None:
            L.append(f"    {a2:7.2f}  {'(no solution)':>18}")
            continue
        kmin, _ = min_curvature(1.0, N, a1, a2, 0.0, 0.0)
        simple = is_simple(1.0, N, a1, a2, 0.0, 0.0)
        L.append(f"    {a2:7.2f}  {a1:18.4f}  {kmin:11.3f}  {str(simple):>8}")
    L.append("")
    L.append("  3b. b1 UNLOCKED (a2 = b2 = 0) — does the new knob help?")
    L.append(f"    {'b1':>7}  {'a1 solving 4pi/3':>18}  {'r_peak/r_mean':>14}  "
             f"{'kappa_min':>11}  {'simple?':>8}")
    for b1 in [-0.30, -0.20, -0.10, 0.0, 0.10, 0.20, 0.30]:
        a1 = solve_a1_for_alobe(N, 0.0, b1, 0.0, tgt)
        if a1 is None:
            L.append(f"    {b1:7.2f}  {'(no solution)':>18}")
            continue
        kmin, _ = min_curvature(1.0, N, a1, 0.0, b1, 0.0)
        simple = is_simple(1.0, N, a1, 0.0, b1, 0.0)
        # peak radius (lobe axis t=0) relative to mean
        zpk, _, _ = curve(np.array([0.0]), 1.0, N, a1, 0.0, b1, 0.0)
        rpk = abs(zpk[0])
        L.append(f"    {b1:7.2f}  {a1:18.4f}  {rpk:14.4f}  "
                 f"{kmin:11.3f}  {str(simple):>8}")
    L.append("")
    L.append("  Reading 3b: if a1 needed to hit 4pi/3 DROPS as b1 moves one")
    L.append("  way, that direction 'fattens' the lobe — less radial swing")
    L.append("  buys the same lobe charge.  kappa_min shows how deep the")
    L.append("  valley has gone concave at that point.")
    L.append("")

    text = "\n".join(L)
    print(text)
    out_path.write_text(text + "\n")
    print(f"\nWrote: {out_path}")


if __name__ == "__main__":
    main()
