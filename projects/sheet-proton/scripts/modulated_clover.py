"""
modulated_clover.py — solver for the modulated-clover baryon construction.

Implements the computational steps of
    projects/sheet-proton/work/modulated-clover.md

STEP 1 (this version): the six-piece cross-section curvature budget (work file
§2 and §6 step 1).  The cross-section is the harmonic tube-function (the same
family as ma-domain/work/tube-function.md):

    z(t) = R e^{i t} [ 1 + a1 cos(N t) + a2 cos(2N t)
                          + i ( b1 sin(N t) + b2 sin(2N t) ) ]

At N = 3 with a1, a2 > 0 it has three MAJOR and three MINOR lobes.  Cut at the
six valley midpoints t = pi/6 + k pi/3 into six equal (pi/3-wide) pieces, each
one lobe plus two valley halves.  The net turning of a piece is T = INT kappa ds
over it.  The construction wants

    T_major = +4 pi/3   (Q = +2/3, the u-like piece)
    T_minor = -2 pi/3   (Q = -1/3, the d-like piece)

forced together by Gauss-Bonnet (3 T_major + 3 T_minor = total turning = 2 pi).

What this script does:
  1. Evaluates a given (a1, b1, a2, b2) point: reports the six piece turnings,
     the total turning, and shape diagnostics.
  2. Scans T_major versus a1 (polar slice b1=b2=0, over an a2 sweep) to locate
     where T_major caps and to report the maximum-contrast simple cross-section.
     T_major = 4pi/3 is not reachable by the smooth family; per work-file
     §4.3-4.4 the operative charge is the modulated track integral, so the
     achievable contrast — not an exact 4pi/3 — is what Step 3 consumes.

Inputs : command-line (see --help); the evaluation-point defaults are the
         user's tube-lab values.
Outputs: outputs/modulated_clover_crosssection.txt
"""

from __future__ import annotations

import argparse
import numpy as np
from math import pi
from pathlib import Path


# ----------------------------------------------------------------------
# Harmonic cross-section curve (shared form with ma-domain/harmonic_tube.py)
# ----------------------------------------------------------------------

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
    kappa = np.imag(np.conj(zp) * zpp) / speed**3
    return kappa, speed


# ----------------------------------------------------------------------
# Piece turnings
# ----------------------------------------------------------------------

def piece_turning(R, N, a1, a2, b1, b2, t0, t1, K=4000):
    """Net turning INT kappa ds over the t-interval [t0, t1]."""
    t = np.linspace(t0, t1, K)
    kappa, speed = kappa_and_speed(t, R, N, a1, a2, b1, b2)
    return np.trapezoid(kappa * speed, t)


def six_piece_turnings(R, N, a1, a2, b1, b2, K=4000):
    """Net turning of each of the six pi/3-wide pieces.

    For N = 3 the lobes sit at t = k pi/3 (k = 0..5); piece k is centred there,
    spanning [k pi/3 - pi/6, k pi/3 + pi/6].  Even k = major lobe, odd k = minor
    lobe (when a1 > 0).  Returns a length-6 list.
    """
    half = pi / N / 2.0           # = pi/6 for N = 3
    step = pi / N                 # = pi/3 for N = 3
    out = []
    for k in range(2 * N):
        c = k * step
        out.append(piece_turning(R, N, a1, a2, b1, b2, c - half, c + half, K))
    return out


def total_turning(R, N, a1, a2, b1, b2, K=24000):
    """Full INT kappa ds over the closed curve — should be 2 pi."""
    t = np.linspace(0.0, 2 * pi, K, endpoint=False)
    dt = 2 * pi / K
    kappa, speed = kappa_and_speed(t, R, N, a1, a2, b1, b2)
    return np.sum(kappa * speed * dt)


def T_major(N, a1, a2, b1, b2, K=4000):
    """Net turning of the major piece centred on t = 0."""
    half = pi / N / 2.0
    return piece_turning(1.0, N, a1, a2, b1, b2, -half, half, K)


# ----------------------------------------------------------------------
# Shape diagnostics
# ----------------------------------------------------------------------

def lobe_radii(N, a1, a2, b1, b2):
    """Radii at the major lobe (t=0), minor lobe (t=pi/N), valley (t=pi/2N)."""
    pts = curve(np.array([0.0, pi / N, pi / (2 * N)]),
                1.0, N, a1, a2, b1, b2)[0]
    return abs(pts[0]), abs(pts[1]), abs(pts[2])


def is_simple(N, a1, a2, b1, b2, K=8000):
    """True iff the cross-section is a simple closed curve.

    Tests, in order: the curve avoids the origin; arg z is strictly monotonic
    (no angular backtracking); and z winds the origin exactly once.  For the
    r > 0 harmonic family these together imply a simple, star-shaped Jordan
    curve.  (A departure of the total tangent turning from 2 pi is the other
    self-intersection signature; callers also check total_turning / 2pi == 1.)
    """
    t = np.linspace(0.0, 2 * pi, K + 1)          # include the endpoint
    z, zp, _ = curve(t, 1.0, N, a1, a2, b1, b2)
    if np.min(np.abs(z)) < 1e-6:
        return False                              # passes through the origin
    if np.min(np.imag(zp / z)) <= 0.0:
        return False                              # arg z not monotonic
    ang = np.unwrap(np.angle(z))
    return abs((ang[-1] - ang[0]) / (2 * pi) - 1.0) < 1e-3


def kappa_extremes(N, a1, a2, b1, b2, K=8000):
    t = np.linspace(0.0, 2 * pi, K, endpoint=False)
    kappa, _ = kappa_and_speed(t, 1.0, N, a1, a2, b1, b2)
    return float(kappa.min()), float(kappa.max())


# ----------------------------------------------------------------------
# Scan T_major vs a1 — locate the achievable maximum contrast
# ----------------------------------------------------------------------

def scan_a1(N, a2, b1, b2, a1_values, K):
    """For each a1 return (a1, T_major, T_minor, total/2pi, kappa_max, simple)."""
    half, step = pi / N / 2.0, pi / N
    rows = []
    for a1 in a1_values:
        tmaj = piece_turning(1.0, N, a1, a2, b1, b2, -half, half, K)
        tmin = piece_turning(1.0, N, a1, a2, b1, b2,
                             step - half, step + half, K)
        tt = total_turning(1.0, N, a1, a2, b1, b2) / (2 * pi)
        _, kmax = kappa_extremes(N, a1, a2, b1, b2)
        simple = is_simple(N, a1, a2, b1, b2) and abs(tt - 1.0) < 1e-3
        rows.append((float(a1), tmaj, tmin, tt, kmax, simple))
    return rows


# ----------------------------------------------------------------------
# Report
# ----------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--N", type=int, default=3, help="lobe-pair count (default 3)")
    ap.add_argument("--a1", type=float, default=0.62, help="eval point a1")
    ap.add_argument("--b1", type=float, default=-0.015, help="eval point b1")
    ap.add_argument("--a2", type=float, default=0.340, help="eval point a2")
    ap.add_argument("--b2", type=float, default=0.030, help="eval point b2")
    ap.add_argument("--target", type=float, default=4 * pi / 3,
                    help="target T_major (default 4pi/3 = Q +2/3)")
    ap.add_argument("--K", type=int, default=4000,
                    help="integration resolution per piece")
    args = ap.parse_args()

    N, K, tgt = args.N, args.K, args.target
    tgt_minor = (2 * pi - 3 * tgt) / 3.0   # Gauss-Bonnet partner

    L = []
    L.append("=" * 78)
    L.append("modulated-clover — STEP 1: six-piece cross-section curvature budget")
    L.append("z(t) = R e^{it} [ 1 + a1 cos(Nt) + a2 cos(2Nt)"
             "  + i ( b1 sin(Nt) + b2 sin(2Nt) ) ]")
    L.append(f"target  T_major = {tgt:+.5f}  (= 4pi/3, Q = +2/3)")
    L.append(f"        T_minor = {tgt_minor:+.5f}  (= -2pi/3, Q = -1/3,"
             " forced by Gauss-Bonnet)")
    L.append("=" * 78)
    L.append("")

    # ---- 1. Evaluate the given point -----------------------------------
    a1, b1, a2, b2 = args.a1, args.b1, args.a2, args.b2
    L.append(f"--- 1. Evaluation point  a1={a1}  b1={b1}  a2={a2}  b2={b2} ---")
    pieces = six_piece_turnings(1.0, N, a1, a2, b1, b2, K)
    tot = total_turning(1.0, N, a1, a2, b1, b2)
    rmaj, rmin, rval = lobe_radii(N, a1, a2, b1, b2)
    simple = is_simple(N, a1, a2, b1, b2) and abs(tot / (2 * pi) - 1.0) < 1e-3
    kmin, kmax = kappa_extremes(N, a1, a2, b1, b2)
    L.append("  piece turnings (k = 0 major, 1 minor, 2 major, ...):")
    for k, T in enumerate(pieces):
        kind = "major" if k % 2 == 0 else "minor"
        L.append(f"    piece {k} ({kind}):  T = {T:+.5f}   ( {T/(2*pi):+.4f} x 2pi )")
    L.append(f"  total turning / 2pi      = {tot/(2*pi):.6f}   (should be 1)")
    L.append(f"  T_major (piece 0)        = {pieces[0]:+.5f}"
             f"   [target {tgt:+.5f}]")
    L.append(f"  T_minor (piece 1)        = {pieces[1]:+.5f}"
             f"   [target {tgt_minor:+.5f}]")
    L.append(f"  radii  major/minor/valley = {rmaj:.4f} / {rmin:.4f} / {rval:.4f}")
    L.append(f"  kappa min / max          = {kmin:.3f} / {kmax:.3f}")
    L.append(f"  simple closed curve      = {simple}")
    L.append("")

    # ---- 2. Scan T_major vs a1 — where does it cap? --------------------
    L.append("--- 2. Scan T_major vs a1 (polar slice b1=b2=0) ---")
    L.append(f"  target T_major = {tgt:.5f}.  Watch where T_major maxes out,")
    L.append("  and whether the curve is still simple there (simple? = True).")
    a1_grid = np.round(np.linspace(0.2, 1.5, 14), 3)
    best = None
    for a2s in [0.20, 0.34, 0.50]:
        L.append("")
        L.append(f"  a2 = {a2s}:")
        L.append(f"    {'a1':>6}  {'T_major':>9}  {'T_minor':>9}  {'tot/2pi':>8}"
                 f"  {'kappa_max':>10}  {'simple?':>8}")
        for (a1s, tmaj, tmin, tt, kmax, simple) in scan_a1(N, a2s, 0.0, 0.0,
                                                           a1_grid, K):
            mark = "  <-- >= target" if tmaj >= tgt else ""
            L.append(f"    {a1s:6.3f}  {tmaj:9.4f}  {tmin:9.4f}  {tt:8.5f}"
                     f"  {kmax:10.2f}  {str(simple):>8}{mark}")
            if simple and (best is None or tmaj > best[1]):
                best = (a1s, tmaj, tmin, a2s, kmax)
    L.append("")
    if best is not None:
        a1b, tmb, tnb, a2b, kmb = best
        L.append("  Best SIMPLE cross-section on this grid:")
        L.append(f"    a1 = {a1b}, a2 = {a2b}, b1 = b2 = 0")
        L.append(f"    T_major = {tmb:+.4f}   Q_major = {tmb/(2*pi):+.4f}"
                 f"   (target +0.6667)")
        L.append(f"    T_minor = {tnb:+.4f}   Q_minor = {tnb/(2*pi):+.4f}"
                 f"   (target -0.3333)")
        L.append(f"    kappa_max = {kmb:.2f}")
        gap = tgt - tmb
        L.append(f"    shortfall to 4pi/3: {gap:+.4f}"
                 f"   ({'reached' if gap <= 0 else 'NOT reached'})")
    L.append("")
    L.append("Reading: the largest T_major with simple? = True is the maximum")
    L.append("major/minor contrast the smooth family supports.  Per the work")
    L.append("file §4.3-4.4 the charge is the MODULATED track integral, not the")
    L.append("static piece split, so this contrast (not T_major = 4pi/3) is what")
    L.append("feeds the Step-3 modulation/track solver.")

    text = "\n".join(L)
    print(text)

    out_dir = Path(__file__).resolve().parents[1] / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "modulated_clover_crosssection.txt"
    out_path.write_text(text + "\n")
    print(f"\nWrote: {out_path}")


if __name__ == "__main__":
    main()
