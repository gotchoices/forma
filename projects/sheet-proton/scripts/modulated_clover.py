"""
modulated_clover.py — solver for the modulated-clover baryon construction.

Implements the computational steps of
    projects/sheet-proton/work/modulated-clover.md

Two work-file steps, selected by --step (default 3):

  --step 1 : the six-piece cross-section curvature budget (work file §2, §6.1).
  --step 3 : the modulation + track solver (work file §4, §6.3).
  --step 4 : mass — the Laplace-Beltrami spectrum of the surface (work file §7).

The cross-section is the harmonic tube-function (same family as
ma-domain/work/tube-function.md):

    z(t) = R e^{i t} [ 1 + a1 cos(N t) + a2 cos(2N t)
                          + i ( b1 sin(N t) + b2 sin(2N t) ) ]

At N = 3 with a1, a2 > 0 it has three MAJOR and three MINOR lobes.  Cut at the
six valley midpoints t = pi/6 + k pi/3 into six equal (pi/3-wide) pieces.

STEP 1 evaluates a cross-section's six piece turnings and scans how large the
major-piece turning T_major can get.  Result: the smooth family caps near
Q_maj ~ 0.63; the idealised T_major = 4pi/3 is the cusp limit and (per work
file §4) is not needed — the operative charge is the modulated track integral.

STEP 3 builds the swept surface

    z(t;θ) = e^{iθ/2} e^{it} [ 1 + a1(θ)cos3t + a2 cos6t
                                  + i ( b1(θ)sin3t + b2 sin6t ) ]

with twist θ/2 and modulation profiles a1(θ), b1(θ) carried by half-integer
harmonics cos/sin((2k+1)θ/2) — each antiperiodic, so the surface closes (work
file §3.3).  The sin (odd-in-θ) harmonics break the proton<->neutron symmetry.  The proton and neutron tracks t(θ)=t0+θ/2 each close
in one ring revolution (§4.1).  STEP 3 tunes the modulation coefficients so the
proton track's experienced charge Q = (1/2pi) INT ∂_tχ dt is +1 and the
neutron track's is 0.

Inputs : command-line (see --help).
Outputs: outputs/modulated_clover_crosssection.txt   (--step 1)
         outputs/modulated_clover_tracks.txt          (--step 3)
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


def star_margin(N, a1, a2, b1, b2, K=4000):
    """min_t of d(arg z)/dt for a frozen cross-section.  > 0  =>  the curve is
    simple (star-shaped).  Used as the Step-3 simplicity penalty."""
    t = np.linspace(0.0, 2 * pi, K, endpoint=False)
    z, zp, _ = curve(t, 1.0, N, a1, a2, b1, b2)
    if np.min(np.abs(z)) < 1e-9:
        return -10.0
    return float(np.min(np.imag(zp / z)))


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

def run_step1(args):
    """STEP 1 report — six-piece curvature budget and the T_major-vs-a1 scan."""
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


# ======================================================================
# STEP 3 — the modulation + track solver  (work file §4, §6.3)
# ======================================================================
#
# Swept surface:
#     z(t;θ) = e^{iθ/2} e^{it} w(t;θ)
#     w(t;θ) = 1 + a1(θ) cos3t + a2 cos6t + i( b1(θ) sin3t + b2 sin6t )
# The modulation profiles a1(θ), b1(θ) are half-integer harmonic series
# Σ [c_k cos((2k+1)θ/2) + s_k sin((2k+1)θ/2)]; every term is antiperiodic,
# a1(θ+2π) = -a1(θ), the closure condition (§3.3).  cos terms are even in θ,
# sin terms odd — the sin terms break the proton<->neutron symmetry.
#
# A track is t(θ) = t0 + θ/2, θ in [0,2π]: it closes in one ring revolution
# (§4.1), traversing three of the six pieces.
#     proton track : t0 = -pi/6   (major-minor-major)
#     neutron track: t0 = +pi/6   (minor-major-minor)
#
# Experienced charge (§4.3):  Q = (1/2π) INT_track ∂_tχ dt,  χ = arg ∂_t z.
# Along the track dt = (1/2)dθ, so Q = (1/4π) INT_0^{2π} ∂_tχ(t0+θ/2;θ) dθ.
# The solver tunes the modulation coefficients so Q_proton -> +1, Q_neutron -> 0.


def modulation(theta, cos_c, sin_c):
    """Modulation profile  Σ_k [ cos_c[k] cos((2k+1)θ/2) + sin_c[k] sin((2k+1)θ/2) ].

    Every term is antiperiodic over 2π (the closure condition, §3.3).  The cos
    terms are even in θ, the sin terms odd; the sin terms break the
    proton<->neutron reflection symmetry (see run_step3)."""
    th = np.asarray(theta, dtype=float)
    out = np.zeros_like(th)
    for k, c in enumerate(cos_c):
        out = out + c * np.cos((2 * k + 1) * th / 2.0)
    for k, c in enumerate(sin_c):
        out = out + c * np.sin((2 * k + 1) * th / 2.0)
    return out


def w_derivs_N3(t, a1, b1, a2, b2):
    """w, w_t, w_tt for the N=3 harmonic bracket (a1, b1 may vary with t)."""
    c3, s3 = np.cos(3 * t), np.sin(3 * t)
    c6, s6 = np.cos(6 * t), np.sin(6 * t)
    w = 1.0 + a1 * c3 + a2 * c6 + 1j * (b1 * s3 + b2 * s6)
    wt = (-3 * a1 * s3 - 6 * a2 * s6) + 1j * (3 * b1 * c3 + 6 * b2 * c6)
    wtt = (-9 * a1 * c3 - 36 * a2 * c6) + 1j * (-9 * b1 * s3 - 36 * b2 * s6)
    return w, wt, wtt


def dchi_dt(t, theta, Ac, As, Bc, Bs, a2, b2):
    """∂_tχ — the tube-direction turning rate of the profile (§4.3)."""
    a1 = modulation(theta, Ac, As)
    b1 = modulation(theta, Bc, Bs)
    w, wt, wtt = w_derivs_N3(t, a1, b1, a2, b2)
    g = 1j * w + wt                       # ∂_t z = e^{iα} e^{it} g
    gt = 1j * wt + wtt
    return 1.0 + np.imag(gt / g)


def chi_total(t, theta, Ac, As, Bc, Bs, a2, b2):
    """Full tangent angle χ = α + t + arg(g),  α = θ/2."""
    a1 = modulation(theta, Ac, As)
    b1 = modulation(theta, Bc, Bs)
    w, wt, _ = w_derivs_N3(t, a1, b1, a2, b2)
    g = 1j * w + wt
    return theta / 2.0 + t + np.angle(g)


def track_charge(t0, Ac, As, Bc, Bs, a2, b2, Nth=3000):
    """Experienced tube-charge of the track t(θ)=t0+θ/2, θ:0->2π.

    Returns (Q_tube, n_total): Q_tube = (1/2π) INT ∂_tχ dt is the charge;
    n_total = (1/2π) ∮ dχ is the winding of the tangent field around the
    closed track (should be an integer; tube + ring = n_total, §4.3)."""
    theta = np.linspace(0.0, 2 * pi, Nth + 1)
    t = t0 + theta / 2.0
    dcdt = dchi_dt(t, theta, Ac, As, Bc, Bs, a2, b2)
    Q_tube = 0.5 * np.trapezoid(dcdt, theta) / (2 * pi)   # dt = (1/2) dθ
    chi = np.unwrap(chi_total(t, theta, Ac, As, Bc, Bs, a2, b2))
    n_total = (chi[-1] - chi[0]) / (2 * pi)
    return Q_tube, n_total


def refine_to_target(N, Bc, Bs, a2, b2, t0_p, t0_n, x0, levels=4, npts=5):
    """Zoom-grid over (As0, As1, Ac0, Ac1) for the SIMPLE-surface point closest
    to (Q_proton, Q_neutron) = (1, 0).  The a1 sin-harmonics (As0, As1) break
    the proton<->neutron symmetry and set the charge DIFFERENCE; the a1
    cos-harmonics (Ac0, Ac1) are θ-even and set the charge SUM.  Both are
    needed for exact (1, 0).  x0 = [As0, As1, Ac0, Ac1].  Returns the best
    simple point as a dict, or None if none is simple."""
    center = np.array(x0, dtype=float)
    radius = np.array([0.35, 0.35, 0.35, 0.35])
    best = None
    for _ in range(levels):
        gr = [np.linspace(center[k] - radius[k], center[k] + radius[k], npts)
              for k in range(4)]
        for s0 in gr[0]:
            for s1 in gr[1]:
                for c0 in gr[2]:
                    for c1 in gr[3]:
                        As, Ac = np.array([s0, s1]), np.array([c0, c1])
                        mm = 1e9
                        for th in np.linspace(0.0, 2*pi, 15, endpoint=False):
                            mm = min(mm, star_margin(
                                N, float(modulation(th, Ac, As)), a2,
                                float(modulation(th, Bc, Bs)), b2, K=2000))
                            if mm <= 0.0:
                                break
                        if mm <= 0.0:
                            continue                # reject self-intersecting
                        Qp, _ = track_charge(t0_p, Ac, As, Bc, Bs, a2, b2)
                        Qn, _ = track_charge(t0_n, Ac, As, Bc, Bs, a2, b2)
                        err = (Qp - 1.0) ** 2 + Qn ** 2
                        if best is None or err < best["err"]:
                            best = dict(err=err, As0=s0, As1=s1, Ac0=c0,
                                        Ac1=c1, Qp=Qp, Qn=Qn, margin=mm)
        if best is None:
            return None
        center = np.array([best["As0"], best["As1"],
                           best["Ac0"], best["Ac1"]])
        radius = radius * 0.4
    return best


def run_step3(args):
    """STEP 3: sweep the symmetry-breaking modulation and map the proton/
    neutron charge separation against cross-section simplicity.

    A cos-only modulation is θ-even: the (t,θ)->(-t,-θ) reflection maps the
    proton track onto the neutron track, so Q_proton == Q_neutron (both 1/2).
    The sin (odd-in-θ) harmonics break that and open up the separation
    D = Q_proton - Q_neutron.  Success needs D = 1 (proton +1, neutron 0) WITH
    a simple cross-section at every ring angle.  This sweep maps D and the
    cross-section simplicity margin over the two leading a1 sin-harmonics, to
    see whether the two requirements can be met together."""
    N, a2, b2 = args.N, args.a2, args.b2
    t0_p, t0_n = -pi / 6.0, +pi / 6.0
    # Fixed backbone; the sweep varies only the two a1 sin-harmonics (the
    # symmetry breakers).  a1 cos = [args.a1, 0]; b1 = cos args.b1, sin 0.
    Ac = np.array([args.a1, 0.0])
    Bc = np.array([args.b1])
    Bs = np.array([0.0])

    def evaluate(As):
        """Q_proton, Q_neutron, min star-margin, kappa_max for a1 sin = As."""
        Qp, _ = track_charge(t0_p, Ac, As, Bc, Bs, a2, b2)
        Qn, _ = track_charge(t0_n, Ac, As, Bc, Bs, a2, b2)
        mm, kmx = 1e9, 0.0
        for th in np.linspace(0.0, 2 * pi, 19, endpoint=False):
            a1th = float(modulation(th, Ac, As))
            b1th = float(modulation(th, Bc, Bs))
            mm = min(mm, star_margin(N, a1th, a2, b1th, b2))
            _, km = kappa_extremes(N, a1th, a2, b1th, b2)
            kmx = max(kmx, km)
        return Qp, Qn, mm, kmx

    grid0 = np.round(np.linspace(0.0, 2.0, 7), 3)       # As0
    grid1 = np.round(np.linspace(-1.5, 1.5, 7), 3)      # As1

    Qp0, Qn0, mm0, _ = evaluate(np.array([0.0, 0.0]))

    D_grid, mm_grid, simple_grid = [], [], []
    dmax_simple = -1e9
    best = None
    for s0 in grid0:
        Drow, mmrow, srow = [], [], []
        for s1 in grid1:
            Qp, Qn, mm, kmx = evaluate(np.array([s0, s1]))
            D = Qp - Qn
            simple = bool(mm > 0.0)
            Drow.append(D)
            mmrow.append(mm)
            srow.append(simple)
            if simple and np.isfinite(D):
                if D > dmax_simple:
                    dmax_simple = D
                if best is None or abs(D - 1.0) < abs(best[2] - 1.0):
                    best = (s0, s1, D, mm, kmx, Qp, Qn)
        D_grid.append(Drow)
        mm_grid.append(mmrow)
        simple_grid.append(srow)

    L = []
    L.append("=" * 78)
    L.append("modulated-clover — STEP 3: symmetry-breaking sweep")
    L.append("surface z(t;θ)=e^{iθ/2}e^{it}[1+a1(θ)cos3t+a2cos6t+i(b1(θ)sin3t+b2sin6t)]")
    L.append("a1(θ)=Σ[c_k cos((2k+1)θ/2)+s_k sin((2k+1)θ/2)] ; tracks close in 1 ring rev")
    L.append("D = Q_proton - Q_neutron ;  success needs D=1 with a simple surface")
    L.append("=" * 78)
    L.append("")
    L.append(f"fixed:  a1 cos-harmonics {Ac.tolist()},  b1 cos {args.b1},  "
             f"a2={a2}, b2={b2}")
    L.append("swept:  a1 sin-harmonics As0 (rows) x As1 (cols)")
    L.append("")
    L.append(f"baseline As=(0,0):  Q_p={Qp0:+.4f}  Q_n={Qn0:+.4f}  "
             f"D={Qp0 - Qn0:+.4f}  margin={mm0:+.3f}")
    L.append("  (cos-only is θ-even -> reflection symmetry -> Q_p=Q_n, D=0)")
    L.append("")
    L.append("--- D = Q_p - Q_n   (suffix s = simple surface, X = self-intersecting) ---")
    L.append("  As0\\As1 " + " ".join(f"{s1:>8.2f}" for s1 in grid1))
    for i, s0 in enumerate(grid0):
        cells = []
        for j in range(len(grid1)):
            tag = "s" if simple_grid[i][j] else "X"
            cells.append(f"{D_grid[i][j]:>7.3f}{tag}")
        L.append(f"  {s0:>7.2f} " + " ".join(cells))
    L.append("")
    L.append("--- min star-margin over the ring  (< 0 = self-intersecting) ---")
    L.append("  As0\\As1 " + " ".join(f"{s1:>8.2f}" for s1 in grid1))
    for i, s0 in enumerate(grid0):
        cells = [f"{mm_grid[i][j]:>8.2f}" for j in range(len(grid1))]
        L.append(f"  {s0:>7.2f} " + " ".join(cells))
    L.append("")
    L.append(f"largest D reached with a SIMPLE surface : {dmax_simple:+.4f}")
    if best is not None:
        s0, s1, D, mm, kmx, Qp, Qn = best
        L.append(f"simple point nearest D=1 : As=({s0:+.2f},{s1:+.2f})  "
                 f"D={D:+.4f}  Q_p={Qp:+.4f}  Q_n={Qn:+.4f}  margin={mm:+.3f}")
    L.append("")
    # ---- zoom-refine to exact (Q_p, Q_n) = (1, 0) ----
    L.append("--- refinement: zoom-search for exact (Q_p, Q_n) = (1, 0) ---")
    L.append("  knobs: a1 sin-harmonics (set the charge difference) +")
    L.append("         a1 cos-harmonics (set the charge sum)")
    ref = None
    sa, rerr = False, 1e9
    if best is None:
        L.append("  no simple point in the sweep — refinement skipped.")
    else:
        ref = refine_to_target(N, Bc, Bs, a2, b2, t0_p, t0_n,
                               x0=[best[0], best[1], args.a1, 0.0])
    if ref is not None:
        As = np.array([ref["As0"], ref["As1"]])
        Acr = np.array([ref["Ac0"], ref["Ac1"]])
        rerr = max(abs(ref["Qp"] - 1.0), abs(ref["Qn"]))
        sa, kmx = True, 0.0
        for th in np.linspace(0.0, 2 * pi, 25, endpoint=False):
            a1th = float(modulation(th, Acr, As))
            b1th = float(modulation(th, Bc, Bs))
            tt = total_turning(1.0, N, a1th, a2, b1th, b2) / (2 * pi)
            if not (is_simple(N, a1th, a2, b1th, b2)
                    and abs(tt - 1.0) < 1e-3):
                sa = False
            _, km = kappa_extremes(N, a1th, a2, b1th, b2)
            kmx = max(kmx, km)
        L.append(f"  a1 cos-harmonics Ac = [{ref['Ac0']:+.5f}, {ref['Ac1']:+.5f}]")
        L.append(f"  a1 sin-harmonics As = [{ref['As0']:+.5f}, {ref['As1']:+.5f}]")
        L.append(f"  Q_proton  = {ref['Qp']:+.6f}   (target +1)")
        L.append(f"  Q_neutron = {ref['Qn']:+.6f}   (target  0)")
        L.append(f"  max |residual| = {rerr:.2e}")
        L.append(f"  surface: simple at every θ = {sa}   "
                 f"min margin = {ref['margin']:+.3f}   kappa_max = {kmx:.1f}")
    L.append("")
    ok = (ref is not None and sa and rerr < 5e-3)
    if ok:
        L.append("RESULT: SUCCESS — the modulated-clover construction closes the")
        L.append("proton track at Q = +1 and the neutron at Q = 0 on a simple,")
        L.append("self-consistent half-twisted surface.  The CHARGE construction")
        L.append("works.  (Mass — the wave spectrum on this surface — is a")
        L.append("separate calculation, not yet built.)")
    elif dmax_simple >= 0.95:
        L.append("RESULT: D = 1 is reachable on a simple surface, but the")
        L.append("refinement did not land exact (1, 0) — pinning the charge SUM")
        L.append("as well as the difference needs more modulation knobs.")
    else:
        L.append("RESULT: within this sweep D = 1 needs a self-intersecting")
        L.append("surface — the geometry likely needs rethinking (§5).")

    text = "\n".join(L)
    print(text)
    out_dir = Path(__file__).resolve().parents[1] / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "modulated_clover_tracks.txt"
    out_path.write_text(text + "\n")
    print(f"\nWrote: {out_path}")


# ======================================================================
# STEP 4 — mass: the Laplace-Beltrami spectrum of the surface (work file §7)
# ======================================================================


def build_surface_mesh(Ac, As, Bc, Bs, a2, b2, rho, Rmajor, Nt, Nth):
    """Triangle mesh of the embedded modulated-clover surface (work file §7.1).

    Nt must be even: the half-twist θ-wrap (t,θ+2π)~(t+π,θ) identifies the
    θ-seam with a shift of π = Nt/2 tube-grid steps.  Returns (verts[V,3] float,
    tris[F,3] int), V = Nt*Nth, grid point (i,j) at vertex i*Nth + j."""
    assert Nt % 2 == 0, "Nt must be even for the half-twist wrap"
    t = np.linspace(0.0, 2 * pi, Nt, endpoint=False)
    th = np.linspace(0.0, 2 * pi, Nth, endpoint=False)
    T, TH = np.meshgrid(t, th, indexing="ij")
    a1 = modulation(TH, Ac, As)
    b1 = modulation(TH, Bc, Bs)
    w = (1.0 + a1 * np.cos(3 * T) + a2 * np.cos(6 * T)
         + 1j * (b1 * np.sin(3 * T) + b2 * np.sin(6 * T)))
    zeta = rho * np.exp(1j * TH / 2.0) * np.exp(1j * T) * w
    Px, Py = zeta.real, zeta.imag
    X = (Rmajor + Px) * np.cos(TH)
    Y = (Rmajor + Px) * np.sin(TH)
    verts = np.stack([X.ravel(), Y.ravel(), Py.ravel()], axis=1)

    half = Nt // 2
    tris = []
    for i in range(Nt):
        for j in range(Nth):
            sh = half if j + 1 == Nth else 0          # half-twist at the seam
            v00 = (i % Nt) * Nth + j
            v10 = ((i + 1) % Nt) * Nth + j
            v01 = ((i + sh) % Nt) * Nth + (j + 1) % Nth
            v11 = ((i + 1 + sh) % Nt) * Nth + (j + 1) % Nth
            tris.append((v00, v10, v11))
            tris.append((v00, v11, v01))
    return verts, np.array(tris, dtype=np.int64)


def cotan_laplacian(verts, tris):
    """Cotangent-weighted discrete Laplace-Beltrami L and lumped mass M for a
    triangle mesh.  L psi = mu^2 M psi discretises -Δ_g psi = mu^2 psi
    (work file §7.3).  L is symmetric positive-semidefinite, M diagonal."""
    from scipy.sparse import coo_matrix, diags
    V = len(verts)
    p = verts[tris]                                   # [F, 3, 3]
    rows, cols, vals = [], [], []
    mass = np.zeros(V)
    for c in range(3):
        b, d = (c + 1) % 3, (c + 2) % 3
        u = p[:, b] - p[:, c]
        v = p[:, d] - p[:, c]
        area2 = np.linalg.norm(np.cross(u, v), axis=1)   # = 2 * triangle area
        cot = np.sum(u * v, axis=1) / np.maximum(area2, 1e-30)
        w = 0.5 * cot                                 # weight for edge (b,d)
        ib, idd = tris[:, b], tris[:, d]
        rows += [ib, idd, ib, idd]
        cols += [idd, ib, ib, idd]
        vals += [-w, -w, w, w]
        if c == 0:
            per_vert = area2 / 6.0                    # triangle area / 3
            for k in range(3):
                np.add.at(mass, tris[:, k], per_vert)
    L = coo_matrix((np.concatenate(vals),
                    (np.concatenate(rows), np.concatenate(cols))),
                   shape=(V, V)).tocsr()
    L = 0.5 * (L + L.T)                               # symmetrise (float)
    return L, diags(mass)


def run_step4(args):
    """STEP 4: mass — Laplace-Beltrami spectrum, with the cos-only vs solved
    comparison that identifies the proton/neutron doublet and its split.

    A θ-even (cos-only, As=0) modulation has the (t,θ)->(-t,-θ) reflection
    symmetry; under it the eigenmodes are reflection-singlets or
    reflection-swapped DOUBLETS (degenerate).  The proton/neutron modes are
    such a doublet — the reflection swaps the proton and neutron tracks.
    Turning the sin-harmonics on (As -> As_solved) splits every doublet; the
    nucleon doublet's split is m_neutron - m_proton.  This routine sweeps
    As = lambda * As_solved and reports the spectrum vs lambda, so the
    doublets and their splitting are visible."""
    from scipy.sparse.linalg import eigsh
    N, a2, b2 = args.N, args.a2, args.b2
    t0_p, t0_n = -pi / 6.0, +pi / 6.0
    Bc, Bs = np.array([args.b1]), np.array([0.0])

    # Modulation that closes the charges (Step 3 / §4.5).
    ref = refine_to_target(N, Bc, Bs, a2, b2, t0_p, t0_n,
                           x0=[0.0, 0.5, args.a1, 0.0])
    Ac = np.array([ref["Ac0"], ref["Ac1"]])
    As_sol = np.array([ref["As0"], ref["As1"]])

    lambdas = [0.0, 0.25, 0.5, 0.75, 1.0]
    K = 12
    spectra, margins = [], []
    for lam in lambdas:
        As = lam * As_sol
        verts, tris = build_surface_mesh(Ac, As, Bc, Bs, a2, b2, args.rho,
                                         args.rmajor, args.nt, args.ntheta)
        L, M = cotan_laplacian(verts, tris)
        ev = eigsh(L, k=K, M=M, sigma=-1e-5, which="LM",
                   return_eigenvectors=False)
        spectra.append(np.sort(np.real(ev)))
        margins.append(min(
            star_margin(N, float(modulation(th, Ac, As)), a2,
                        float(modulation(th, Bc, Bs)), b2, K=3000)
            for th in np.linspace(0.0, 2 * pi, 19, endpoint=False)))

    cos0 = spectra[0]
    # doublets in the cos-only spectrum: consecutive near-equal mu^2 (n >= 1)
    doublets, n = [], 1
    while n < K - 1:
        avg = 0.5 * (cos0[n] + cos0[n + 1])
        if avg > 1e-6 and abs(cos0[n + 1] - cos0[n]) < 0.02 * avg:
            doublets.append(n)
            n += 2
        else:
            n += 1

    R = []
    R.append("=" * 78)
    R.append("modulated-clover — STEP 4: mass spectrum and the nucleon doublet")
    R.append("-Δ_g ψ = μ² ψ ; cotangent Laplacian on the §7 embedded surface")
    R.append("As = lambda * As_solved :  lambda=0 cos-only (θ-even, symmetric);")
    R.append("lambda=1 the charge-closing modulation.  Doublets split as λ grows.")
    R.append("=" * 78)
    R.append("")
    R.append(f"  Ac = [{ref['Ac0']:+.4f}, {ref['Ac1']:+.4f}]   "
             f"As_solved = [{ref['As0']:+.4f}, {ref['As1']:+.4f}]")
    R.append(f"  scales rho={args.rho} R_major={args.rmajor}   "
             f"mesh {args.nt}x{args.ntheta}")
    R.append("")
    R.append("--- mu^2  vs  lambda ---")
    R.append(f"  {'mode':>5}  " + "  ".join(f"λ={l:>4.2f}" for l in lambdas))
    for m in range(K):
        R.append(f"  {m:>5}  " + "  ".join(f"{spectra[i][m]:>8.5f}"
                                           for i in range(len(lambdas))))
    R.append(f"  {'simple':>5}  " + "  ".join(
        ("   yes " if mm > 0 else "   NO  ") for mm in margins))
    R.append("")
    R.append("--- cos-only (λ=0) degeneracy check ---")
    if doublets:
        R.append("  near-degenerate pairs at λ=0 (within 2%): "
                 + ", ".join(f"modes {nd},{nd+1}" for nd in doublets))
    else:
        R.append("  no near-degenerate pairs among the lowest modes.")
    R.append("")
    R.append("Reading (Step-4 finding). The cos-only (λ=0) spectrum has no clean")
    R.append("degenerate doublets — a θ-even modulation has only a Z2 reflection")
    R.append("symmetry, which sorts the eigenmodes into even/odd SINGLETS and")
    R.append("does NOT force degeneracy.  So m_n - m_p is not 'a degenerate")
    R.append("nucleon doublet that the sin-harmonics split' — that §7.5 draft")
    R.append("premise is wrong (now corrected in the work file).  The deeper")
    R.append("issue: the proton and neutron are two tracks, the SAME knot, on")
    R.append("ONE surface; how one Laplace-Beltrami spectrum assigns them two")
    R.append("distinct masses needs a mode<->track identification that is not")
    R.append("yet resolved (§7.5).  The spectrum above is real data; its")
    R.append("proton/neutron reading is not yet pinned.")

    text = "\n".join(R)
    print(text)
    out_dir = Path(__file__).resolve().parents[1] / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "modulated_clover_mass.txt"
    out_path.write_text(text + "\n")
    print(f"\nWrote: {out_path}")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--step", choices=["1", "3", "4"], default="3",
                    help="1 = cross-section budget; 3 = modulation/track "
                         "solver; 4 = mass (Laplace-Beltrami spectrum)")
    ap.add_argument("--N", type=int, default=3, help="lobe-pair count (default 3)")
    ap.add_argument("--a1", type=float, default=0.62,
                    help="step 1: eval a1;  step 3: initial a1-modulation amplitude")
    ap.add_argument("--b1", type=float, default=-0.015,
                    help="step 1: eval b1;  step 3: initial b1-modulation amplitude")
    ap.add_argument("--a2", type=float, default=0.340,
                    help="constant 6-fold backbone a2")
    ap.add_argument("--b2", type=float, default=0.030,
                    help="constant 6-fold backbone b2")
    ap.add_argument("--target", type=float, default=4 * pi / 3,
                    help="step 1 target T_major (default 4pi/3)")
    ap.add_argument("--K", type=int, default=4000,
                    help="step 1 integration resolution per piece")
    ap.add_argument("--rho", type=float, default=1.0,
                    help="step 4: cross-section scale")
    ap.add_argument("--rmajor", type=float, default=3.0,
                    help="step 4: ring (major) radius")
    ap.add_argument("--nt", type=int, default=120,
                    help="step 4: tube-direction mesh resolution (must be even)")
    ap.add_argument("--ntheta", type=int, default=120,
                    help="step 4: ring-direction mesh resolution")
    args = ap.parse_args()

    if args.step == "1":
        run_step1(args)
    elif args.step == "3":
        run_step3(args)
    else:
        run_step4(args)


if __name__ == "__main__":
    main()
