"""
modulated_clover.py — solver for the modulated-clover baryon construction.

Implements the computational steps of
    projects/sheet-proton/work/modulated-clover.md

Two work-file steps, selected by --step (default 3):

  --step 1 : the six-piece cross-section curvature budget (work file §2, §6.1).
  --step 3 : the modulation + track solver (work file §4, §6.3).
  --step 4 : mass — the Laplace-Beltrami spectrum of the surface (work file §7).
  --step 5 : mass-fit sweep — low spectrum vs the aspect ratio.
  --step 6 : global parameter sweep — differential evolution over all 9 params.

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


def track_charge_segments(t0, Ac, As, Bc, Bs, a2, b2, Nth=3000, n_seg=3):
    """Per-segment decomposition of the tube charge.

    Splits θ ∈ [0, 2π] into n_seg equal sub-intervals and returns
    [Q_1, Q_2, ..., Q_n] with Σ Q_i = Q_tube.  For n_seg = 3 on the
    Z₂ × Z₃-symmetric clover, each segment corresponds to one arc-piece
    along the (1/2, 1) track:
      proton t₀ = -π/6  →  segments cover  lobe / saddle / lobe   (uud)
      neutron t₀ = +π/6 →  segments cover  saddle / lobe / saddle (udd)
    so the per-segment charges should resolve into the per-quark fractional
    charges +2/3, -1/3 expected under hypothesis G1."""
    # Use a finer grid that's a multiple of n_seg.
    Nth_local = (Nth // n_seg) * n_seg
    theta = np.linspace(0.0, 2 * pi, Nth_local + 1)
    t = t0 + theta / 2.0
    dcdt = dchi_dt(t, theta, Ac, As, Bc, Bs, a2, b2)
    seg_size = Nth_local // n_seg
    Qs = []
    for k in range(n_seg):
        i0 = k * seg_size
        i1 = (k + 1) * seg_size
        # Slice [i0:i1+1] so adjacent segments share the boundary point;
        # the trapezoid rule then sums cleanly.
        Q_k = 0.5 * np.trapezoid(dcdt[i0:i1 + 1], theta[i0:i1 + 1]) / (2 * pi)
        Qs.append(float(Q_k))
    return Qs


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


def triangulation(Nt, Nth):
    """Triangle connectivity for the Nt x Nth half-twisted-torus grid.  Nt must
    be even: the half-twist θ-wrap (t,θ+2π)~(t+π,θ) shifts the θ-seam by
    π = Nt/2 tube steps.  Connectivity is modulation-independent — build once,
    reuse.  Grid point (i,j) is vertex i*Nth + j."""
    assert Nt % 2 == 0, "Nt must be even for the half-twist wrap"
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
    return np.array(tris, dtype=np.int64)


def surface_vertices(Ac, As, Bc, Bs, a2, b2, rho, Rmajor, Nt, Nth):
    """3D vertex positions of the modulated-clover surface (work file §7.1),
    flattened so grid point (i,j) is row i*Nth + j."""
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
    return np.stack([X.ravel(), Y.ravel(), Py.ravel()], axis=1)


def build_surface_mesh(Ac, As, Bc, Bs, a2, b2, rho, Rmajor, Nt, Nth):
    """Triangle mesh (verts[V,3], tris[F,3]) of the modulated-clover surface."""
    return (surface_vertices(Ac, As, Bc, Bs, a2, b2, rho, Rmajor, Nt, Nth),
            triangulation(Nt, Nth))


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


def run_step5(args):
    """STEP 5: mass-fit sweep.  Vary the charge-neutral free parameter — the
    aspect ratio (ring radius R_major) — and report the low Laplace-Beltrami
    spectrum as scale-free mass ratios μ_n/μ_1, looking for a configuration
    whose two lowest modes could be the proton/neutron (ratio ≈ 1.0014).

    R_major does not affect charge (the experienced curvature is a
    cross-section quantity), so the whole sweep stays charge-correct without
    re-solving Step 3.  The other free parameters (the charge-modulation
    family, b1/a2/b2) do affect charge and are left fixed here — opening them
    is the natural Step-5 extension."""
    from scipy.sparse.linalg import eigsh
    N, a2, b2 = args.N, args.a2, args.b2
    t0_p, t0_n = -pi / 6.0, +pi / 6.0
    Bc, Bs = np.array([args.b1]), np.array([0.0])

    ref = refine_to_target(N, Bc, Bs, a2, b2, t0_p, t0_n,
                           x0=[0.0, 0.5, args.a1, 0.0])
    Ac = np.array([ref["Ac0"], ref["Ac1"]])
    As = np.array([ref["As0"], ref["As1"]])

    Rvals = np.geomspace(2.0, 24.0, args.r_steps)
    K = 10
    rows = []
    for Rm in Rvals:
        verts, tris = build_surface_mesh(Ac, As, Bc, Bs, a2, b2,
                                         args.rho, Rm, args.nt, args.ntheta)
        L, M = cotan_laplacian(verts, tris)
        ev = np.sort(np.real(eigsh(L, k=K, M=M, sigma=-1e-5, which="LM",
                                   return_eigenvectors=False)))
        rows.append((Rm, np.sqrt(np.clip(ev, 0.0, None))))

    R = []
    R.append("=" * 78)
    R.append("modulated-clover — STEP 5: mass-fit sweep over the aspect ratio")
    R.append("low Laplace-Beltrami spectrum vs R_major (a charge-neutral knob);")
    R.append("μ_n/μ_1 are scale-free mass ratios.  Nucleon target μ_2/μ_1 ≈ 1.0014.")
    R.append("=" * 78)
    R.append("")
    R.append(f"  charge modulation: Ac=[{ref['Ac0']:+.4f}, {ref['Ac1']:+.4f}]  "
             f"As=[{ref['As0']:+.4f}, {ref['As1']:+.4f}]")
    R.append(f"  (Q_proton={ref['Qp']:+.4f}, Q_neutron={ref['Qn']:+.4f})   "
             f"rho={args.rho}, mesh {args.nt}x{args.ntheta}")
    R.append("")
    R.append("--- mass ratios μ_n/μ_1  and the lowest-pair fractional split ---")
    R.append(f"  {'R_major':>8}  {'mu2/mu1':>9}  {'mu3/mu1':>9}  {'mu4/mu1':>9}"
             f"  {'mu5/mu1':>9}  {'split(2,1)':>11}")
    best = None
    for (Rm, mu) in rows:
        m1 = mu[1]
        ratios = [mu[n] / m1 for n in range(2, 6)]
        split = (mu[2] - mu[1]) / (0.5 * (mu[1] + mu[2]))
        R.append(f"  {Rm:>8.3f}  " + "  ".join(f"{r:>9.5f}" for r in ratios)
                 + f"  {split:>11.5f}")
        if best is None or split < best[1]:
            best = (Rm, split)
    R.append("")
    R.append(f"smallest lowest-pair split in the sweep: {best[1]:.5f} "
             f"at R_major = {best[0]:.3f}")
    R.append("observed proton/neutron:  (m_n - m_p)/m_N ≈ 0.00140")
    R.append("")
    if best[1] < 0.003:
        R.append("The two lowest modes CAN be brought near-degenerate by the")
        R.append("aspect-ratio knob — a 0.0014-level split is reachable by")
        R.append("dialling R_major near the crossing.  CAVEAT: this is an")
        R.append("accidental mode crossing, not by itself a structural")
        R.append("proton/neutron doublet; the two modes' character and charges")
        R.append("must be checked before identifying them as the nucleon.")
    else:
        R.append(f"The lowest-pair split stays well above 0.0014 across the")
        R.append(f"sweep (minimum {best[1]:.4f}).  The aspect ratio alone does")
        R.append("not bring two low modes near-degenerate; the charge-modulation")
        R.append("family and b1/a2/b2 would need to be opened (Step-5 extension).")

    text = "\n".join(R)
    print(text)
    out_dir = Path(__file__).resolve().parents[1] / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "modulated_clover_massfit.txt"
    out_path.write_text(text + "\n")
    print(f"\nWrote: {out_path}")


def run_step6(args):
    """STEP 6: global parameter sweep.  Differential evolution over all nine
    parameters (a1/b1 modulation harmonics, a2, b2, R_major) for the
    charge-correct, simple surface whose low Laplace-Beltrami spectrum has the
    smallest pair-split — i.e. the best shot at a near-degenerate nucleon pair
    (target split ≈ 0.0014).  Charge is enforced by a heavy penalty;
    self-intersecting surfaces are rejected.  The DE runs on a coarse mesh; the
    winner is re-evaluated on the fine mesh."""
    from scipy.optimize import differential_evolution
    from scipy.sparse.linalg import eigsh
    N = args.N
    t0_p, t0_n = -pi / 6.0, +pi / 6.0
    msh = args.sweep_mesh + (args.sweep_mesh % 2)      # force even
    tris_c = triangulation(msh, msh)
    W_CHG, REJECT = 1.0e4, 5.0

    # x = [Ac0, Ac1, As0, As1, Bc0, Bs0, a2, b2, R_major]
    bounds = [(-1.0, 1.0), (-1.0, 1.0), (-1.5, 1.5), (-1.5, 1.5),
              (-0.40, 0.40), (-0.40, 0.40), (0.05, 0.60), (-0.20, 0.20),
              (2.0, 16.0)]
    x0 = np.array([0.1916, -0.5068, 0.2016, 0.6736,
                   args.b1, 0.0, args.a2, args.b2, 6.0])

    def unpack(x):
        return (np.array([x[0], x[1]]), np.array([x[2], x[3]]),
                np.array([x[4]]), np.array([x[5]]),
                float(x[6]), float(x[7]), float(x[8]))

    def min_pair_split(Ac, As, Bc, Bs, a2, b2, Rm, Nt, Nth, tris):
        """Smallest fractional split among the low eigenmode pairs (1,2)..(4,5).
        Returns (split, pair_index, mu) or (None, None, None) on failure."""
        verts = surface_vertices(Ac, As, Bc, Bs, a2, b2, args.rho, Rm, Nt, Nth)
        Lm, Mm = cotan_laplacian(verts, tris)
        try:
            ev = np.sort(np.real(eigsh(Lm, k=6, M=Mm, sigma=-1e-5,
                                       which="LM", return_eigenvectors=False)))
        except Exception:
            return None, None, None
        mu = np.sqrt(np.clip(ev, 0.0, None))
        if mu[1] < 1e-6:
            return None, None, None
        sp = [(mu[n + 1] - mu[n]) / (0.5 * (mu[n] + mu[n + 1]))
              for n in range(1, 5)]
        k = int(np.argmin(sp))
        return sp[k], k + 1, mu

    neval = [0]

    def objective(x):
        neval[0] += 1
        Ac, As, Bc, Bs, a2, b2, Rm = unpack(x)
        for th in np.linspace(0.0, 2 * pi, 15, endpoint=False):
            if star_margin(N, float(modulation(th, Ac, As)), a2,
                           float(modulation(th, Bc, Bs)), b2, K=1200) <= 0.02:
                return REJECT                          # self-intersecting
        Qp, _ = track_charge(t0_p, Ac, As, Bc, Bs, a2, b2, Nth=1200)
        Qn, _ = track_charge(t0_n, Ac, As, Bc, Bs, a2, b2, Nth=1200)
        cerr = (Qp - 1.0) ** 2 + Qn ** 2
        sp, _, _ = min_pair_split(Ac, As, Bc, Bs, a2, b2, Rm, msh, msh, tris_c)
        if sp is None:
            return REJECT
        return sp + W_CHG * cerr

    print(f"STEP 6: differential evolution — 9 params, coarse mesh {msh}x{msh}, "
          f"maxiter={args.de_iters} ...", flush=True)
    res = differential_evolution(objective, bounds, x0=x0, seed=1,
                                 maxiter=args.de_iters, popsize=12,
                                 tol=1e-9, polish=True)
    # ---- fine-mesh local polish of the DE winner ----
    # The DE minimised a coarse-mesh proxy; polish on the fine mesh so the
    # reported split is trustworthy and not a coarse-mesh artifact.
    from scipy.optimize import minimize
    tris_f = triangulation(args.nt, args.ntheta)

    def fine_objective(x):
        Ac, As, Bc, Bs, a2, b2, Rm = unpack(x)
        for th in np.linspace(0.0, 2 * pi, 15, endpoint=False):
            if star_margin(N, float(modulation(th, Ac, As)), a2,
                           float(modulation(th, Bc, Bs)), b2, K=1500) <= 0.02:
                return REJECT
        Qp, _ = track_charge(t0_p, Ac, As, Bc, Bs, a2, b2)
        Qn, _ = track_charge(t0_n, Ac, As, Bc, Bs, a2, b2)
        sp, _, _ = min_pair_split(Ac, As, Bc, Bs, a2, b2, Rm,
                                  args.nt, args.ntheta, tris_f)
        if sp is None:
            return REJECT
        return sp + W_CHG * ((Qp - 1.0) ** 2 + Qn ** 2)

    print("STEP 6: fine-mesh local polish of the DE winner ...", flush=True)
    pol = minimize(fine_objective, res.x, method="Nelder-Mead",
                   options={"maxiter": args.polish_iters,
                            "xatol": 1e-5, "fatol": 1e-9})
    x = pol.x if fine_objective(pol.x) <= fine_objective(res.x) else res.x

    Ac, As, Bc, Bs, a2, b2, Rm = unpack(x)
    Qp, _ = track_charge(t0_p, Ac, As, Bc, Bs, a2, b2)
    Qn, _ = track_charge(t0_n, Ac, As, Bc, Bs, a2, b2)
    cerr = max(abs(Qp - 1.0), abs(Qn))
    csp, _, _ = min_pair_split(Ac, As, Bc, Bs, a2, b2, Rm, msh, msh, tris_c)
    fsp, fpair, fmu = min_pair_split(Ac, As, Bc, Bs, a2, b2, Rm,
                                     args.nt, args.ntheta, tris_f)

    R = []
    R.append("=" * 78)
    R.append("modulated-clover — STEP 6: global parameter sweep")
    R.append("differential evolution over all 9 parameters; objective = smallest")
    R.append("low-mode-pair split; charge penalised; self-intersecting rejected.")
    R.append("Question: can a charge-correct simple surface put two low modes")
    R.append("within the proton/neutron ratio (split ≈ 0.0014)?")
    R.append("=" * 78)
    R.append("")
    R.append(f"function evaluations: {neval[0]}    "
             f"coarse mesh {msh}x{msh}, fine {args.nt}x{args.ntheta}")
    R.append("")
    R.append("--- best point found ---")
    R.append(f"  a1 cos Ac = [{x[0]:+.5f}, {x[1]:+.5f}]")
    R.append(f"  a1 sin As = [{x[2]:+.5f}, {x[3]:+.5f}]")
    R.append(f"  b1 cos Bc = [{x[4]:+.5f}]   b1 sin Bs = [{x[5]:+.5f}]")
    R.append(f"  a2 = {x[6]:.5f}   b2 = {x[7]:+.5f}   R_major = {x[8]:.4f}")
    R.append(f"  charge:  Q_proton = {Qp:+.5f}   Q_neutron = {Qn:+.5f}"
             f"   (max error {cerr:.2e})")
    R.append("")
    if fsp is not None:
        R.append(f"  smallest low-pair split (fine mesh): {fsp:.5f}"
                 f"   (modes {fpair},{fpair+1})")
        R.append("  fine-mesh low spectrum  mu_n/mu_1 (n=2..5): "
                 + ", ".join(f"{fmu[n] / fmu[1]:.5f}" for n in range(2, 6)))
    if csp is not None:
        R.append(f"  coarse-mesh smallest split (for comparison): {csp:.5f}")
    R.append("")
    R.append("observed proton/neutron:  (m_n - m_p)/m_N  ~  0.00140")
    R.append("")
    use = fsp if fsp is not None else csp
    if use is None:
        R.append("RESULT: the search returned no usable surface — inspect.")
    else:
        R.append(f"RESULT: smallest low-pair split found = {use:.5f}  "
                 f"(~{use / 0.00140:.1f}x the observed 0.00140).")
        if use <= 0.0016:
            R.append("At the proton/neutron level — a charge-correct, simple")
            R.append("surface CAN host a near-degenerate nucleon pair; dial the")
            R.append("split onto 0.00140.  (This is a consistency fit, 9 params")
            R.append("to one ratio — not a parameter-free prediction.)")
        elif use < 0.010:
            R.append("Within a small factor of the target.  Treat as an UPPER")
            R.append("bound, not a proven floor — if differential evolution had")
            R.append("not plateaued, a deeper run can lower it.  Whether it")
            R.append("crosses 0.00140 is not yet settled.")
        else:
            R.append("Far above the target — the parameter freedom looks")
            R.append("exhausted; a different mass mechanism would be needed.")
            R.append("(The charge construction, steps 1-3, is independent.)")
        if cerr >= 1e-3:
            R.append(f"NOTE: charge error {cerr:.1e} is loose — re-polish charge.")

    text = "\n".join(R)
    print(text)
    out_dir = Path(__file__).resolve().parents[1] / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "modulated_clover_globalsweep.txt"
    out_path.write_text(text + "\n")
    print(f"\nWrote: {out_path}")


# ======================================================================
# STEP 7 — path-length mass:  mass = 2(pi)hbar c / L_track
# ======================================================================
#
# A baryon is a standing wave on its closed (1/2,1) track; the fundamental
# has wavelength = the track's arc length L, so mass = 2(pi)hbar c / L.
# Proton and neutron are the two tracks (the same objects the charge
# construction uses), so  m_n / m_p = L_proton / L_neutron.  Charge and mass
# then both come from the track — one consistent picture.


def modulation_deriv(theta, cos_c, sin_c):
    """d/dθ of modulation(theta, cos_c, sin_c)."""
    th = np.asarray(theta, dtype=float)
    out = np.zeros_like(th)
    for k, c in enumerate(cos_c):
        m = (2 * k + 1) / 2.0
        out = out - c * m * np.sin(m * th)
    for k, c in enumerate(sin_c):
        m = (2 * k + 1) / 2.0
        out = out + c * m * np.cos(m * th)
    return out


def track_length(t0, Ac, As, Bc, Bs, a2, b2, rho, Rmajor, Nth=4000):
    """Arc length of the (1/2,1) track t(θ)=t0+θ/2 on the modulated-clover
    surface, from the induced metric (work file §7.2).  Along the track
    dt = (1/2)dθ, so ds^2 = (g_tt/4 + g_tθ + g_θθ) dθ^2."""
    theta = np.linspace(0.0, 2 * pi, Nth + 1)
    t = t0 + theta / 2.0
    a1 = modulation(theta, Ac, As)
    b1 = modulation(theta, Bc, Bs)
    a1p = modulation_deriv(theta, Ac, As)
    b1p = modulation_deriv(theta, Bc, Bs)
    c3, s3 = np.cos(3 * t), np.sin(3 * t)
    c6, s6 = np.cos(6 * t), np.sin(6 * t)
    w = 1.0 + a1 * c3 + a2 * c6 + 1j * (b1 * s3 + b2 * s6)
    wt = (-3.0 * a1 * s3 - 6.0 * a2 * s6) + 1j * (3.0 * b1 * c3 + 6.0 * b2 * c6)
    wth = a1p * c3 + 1j * (b1p * s3)                  # ∂_θ w  (a2, b2 constant)
    phase = rho * np.exp(1j * (theta / 2.0 + t))
    zeta = phase * w
    zeta_t = phase * (1j * w + wt)
    zeta_th = phase * (0.5j * w + wth)                # twist  α' = 1/2
    g_tt = np.abs(zeta_t) ** 2
    g_tth = np.real(np.conj(zeta_t) * zeta_th)
    g_thth = np.abs(zeta_th) ** 2 + (Rmajor + zeta.real) ** 2
    ds = np.sqrt(np.maximum(g_tt / 4.0 + g_tth + g_thth, 0.0))
    return float(np.trapezoid(ds, theta))


def run_step7(args):
    """STEP 7: the path-length mass mechanism.  Mass = 2πℏc / L_track, so
    m_n/m_p = L_proton/L_neutron.  Reports the proton and neutron track
    lengths for the Step-3 charge-correct surface, then sweeps the full
    charge-correct parameter space for L_proton/L_neutron equal to the
    observed m_n/m_p — charge and mass both read off the tracks.

    With --symmetric, the modulation is restricted to the Z₂ × Z₃-
    symmetric subspace: only the k=1 half-integer harmonics
    cos(3θ/2), sin(3θ/2) are allowed for a1(θ) and b1(θ) (the k=0
    cos(θ/2), sin(θ/2) terms — which break 3-fold ring symmetry —
    are zeroed out).  The search becomes 7-parameter instead of 9.
    """
    from scipy.optimize import differential_evolution
    N = args.N
    t0_p, t0_n = -pi / 6.0, +pi / 6.0
    TARGET = 939.56542 / 938.27209           # observed m_n/m_p = L_p/L_n
    W_CHG, REJECT = 1.0e4, 9.0
    SYM = getattr(args, "symmetric", False)

    if SYM:
        # Symmetric subspace: only k=1 half-integer harmonics
        # (cos(3θ/2), sin(3θ/2)) are allowed in a1 and b1.
        # Parameter vector: [Ac1, As1, Bc1, Bs1, a2, b2, Rm].
        def unpack(x):
            return (np.array([0.0, x[0]]),       # Ac: zero k=0, free k=1
                    np.array([0.0, x[1]]),       # As: zero k=0, free k=1
                    np.array([0.0, x[2]]),       # Bc: zero k=0, free k=1
                    np.array([0.0, x[3]]),       # Bs: zero k=0, free k=1
                    float(x[4]), float(x[5]), float(x[6]))
        bounds = [(-1.0, 1.0), (-1.5, 1.5), (-0.40, 0.40), (-0.40, 0.40),
                  (0.05, 0.60), (-0.20, 0.20), (2.0, 300.0)]
        # Seed: project the unconstrained Step-7 solution into the
        # symmetric subspace (keep k=1 coefficients, zero k=0).
        x0 = np.array([-0.489, 0.656, 0.0, 0.0, 0.330, 0.032, 60.0])
        label = "STEP 7 (symmetric)"
        outname = "modulated_clover_pathmass_sym.txt"
    else:
        def unpack(x):
            return (np.array([x[0], x[1]]), np.array([x[2], x[3]]),
                    np.array([x[4]]), np.array([x[5]]),
                    float(x[6]), float(x[7]), float(x[8]))
        bounds = [(-1.0, 1.0), (-1.0, 1.0), (-1.5, 1.5), (-1.5, 1.5),
                  (-0.40, 0.40), (-0.40, 0.40), (0.05, 0.60), (-0.20, 0.20),
                  (2.0, 300.0)]
        label = "STEP 7"
        outname = "modulated_clover_pathmass.txt"

    def lengths(Ac, As, Bc, Bs, a2, b2, Rm):
        return (track_length(t0_p, Ac, As, Bc, Bs, a2, b2, args.rho, Rm),
                track_length(t0_n, Ac, As, Bc, Bs, a2, b2, args.rho, Rm))

    R = []
    R.append("=" * 78)
    R.append(f"modulated-clover — {label}: path-length mass mechanism")
    R.append("mass = 2πℏc / L  (standing wave; wavelength = closed-track length).")
    R.append("proton and neutron are the two (1/2,1) tracks: m_n/m_p = L_p/L_n.")
    if SYM:
        R.append("symmetric: modulation restricted to Z₂×Z₃-compatible k=1")
        R.append("half-integer harmonics cos(3θ/2), sin(3θ/2) only.")
    R.append("=" * 78)
    R.append("")
    R.append(f"observed  m_n/m_p = {TARGET:.7f}   (target for L_proton/L_neutron)")
    R.append("")

    if not SYM:
        # baseline: the Step-3 charge-correct modulation
        ref = refine_to_target(N, np.array([args.b1]), np.array([0.0]),
                               args.a2, args.b2, t0_p, t0_n,
                               x0=[0.0, 0.5, args.a1, 0.0])
        Acb = np.array([ref["Ac0"], ref["Ac1"]])
        Asb = np.array([ref["As0"], ref["As1"]])
        R.append("--- baseline: the Step-3 charge-correct surface, vs R_major ---")
        R.append(f"  {'R_major':>9}  {'L_proton':>12}  {'L_neutron':>12}  {'L_p/L_n':>11}")
        for Rm in [3.0, 6.0, 12.0, 24.0]:
            Lp, Ln = lengths(Acb, Asb, np.array([args.b1]), np.array([0.0]),
                             args.a2, args.b2, Rm)
            R.append(f"  {Rm:>9.3f}  {Lp:>12.5f}  {Ln:>12.5f}  {Lp / Ln:>11.7f}")
        R.append("  (L_p > L_n  =>  proton path longer  =>  m_p < m_n, the right sign)")
        R.append("")
        # Use refined values as seed
        x0 = np.array([ref["Ac0"], ref["Ac1"], ref["As0"], ref["As1"],
                       args.b1, 0.0, args.a2, args.b2, 60.0])

    neval = [0]

    def objective(x):
        neval[0] += 1
        Ac, As, Bc, Bs, a2, b2, Rm = unpack(x)
        for th in np.linspace(0.0, 2 * pi, 15, endpoint=False):
            if star_margin(N, float(modulation(th, Ac, As)), a2,
                           float(modulation(th, Bc, Bs)), b2, K=1500) <= 0.02:
                return REJECT
        Qp, _ = track_charge(t0_p, Ac, As, Bc, Bs, a2, b2, Nth=1500)
        Qn, _ = track_charge(t0_n, Ac, As, Bc, Bs, a2, b2, Nth=1500)
        cerr = (Qp - 1.0) ** 2 + Qn ** 2
        Lp, Ln = lengths(Ac, As, Bc, Bs, a2, b2, Rm)
        return abs(Lp / Ln - TARGET) + W_CHG * cerr

    print(f"{label}: differential evolution for L_p/L_n = {TARGET:.7f} ...",
          flush=True)
    res = differential_evolution(objective, bounds, x0=x0, seed=1,
                                 maxiter=args.de_iters, popsize=12,
                                 tol=1e-14, polish=True)
    x = res.x
    Ac, As, Bc, Bs, a2, b2, Rm = unpack(x)
    Qp, _ = track_charge(t0_p, Ac, As, Bc, Bs, a2, b2)
    Qn, _ = track_charge(t0_n, Ac, As, Bc, Bs, a2, b2)
    cerr = max(abs(Qp - 1.0), abs(Qn))
    Lp, Ln = lengths(Ac, As, Bc, Bs, a2, b2, Rm)
    ratio = Lp / Ln

    R.append(f"--- best charge-correct surface for L_p/L_n = m_n/m_p "
             f"({neval[0]} evals) ---")
    if SYM:
        R.append(f"  Ac = [{Ac[0]:+.5f}, {Ac[1]:+.5f}]   As = [{As[0]:+.5f}, {As[1]:+.5f}]")
        R.append(f"  Bc = [{Bc[0]:+.5f}, {Bc[1]:+.5f}]   Bs = [{Bs[0]:+.5f}, {Bs[1]:+.5f}]")
        R.append(f"  a2 = {a2:.5f}   b2 = {b2:+.5f}   R_major = {Rm:.4f}")
    else:
        R.append(f"  Ac = [{x[0]:+.5f}, {x[1]:+.5f}]   As = [{x[2]:+.5f}, {x[3]:+.5f}]")
        R.append(f"  Bc = [{x[4]:+.5f}]   Bs = [{x[5]:+.5f}]   a2 = {x[6]:.5f}   "
                 f"b2 = {x[7]:+.5f}   R_major = {x[8]:.4f}")
    R.append(f"  charge:  Q_proton = {Qp:+.6f}   Q_neutron = {Qn:+.6f}   "
             f"(error {cerr:.1e})")
    R.append(f"  L_proton = {Lp:.6f}   L_neutron = {Ln:.6f}")
    R.append(f"  L_p/L_n = {ratio:.7f}   target {TARGET:.7f}   "
             f"residual {ratio - TARGET:+.2e}")
    R.append("")
    if cerr < 1e-3 and abs(ratio - TARGET) < 1e-5:
        R.append("RESULT: charge-correct surface DOES reproduce the observed")
        R.append("proton/neutron mass ratio as the ratio of track lengths.")
        if SYM:
            R.append("AND it sits in the Z₂×Z₃-symmetric subspace: 3-fold ring")
            R.append("symmetry holds exactly. The (proton, neutron) pair can be")
            R.append("treated as one Z₂ × Z₃ orbit of one fundamental track.")
    elif cerr < 1e-3:
        R.append(f"RESULT: closest charge-correct L_p/L_n = {ratio:.6f} vs target")
        R.append(f"{TARGET:.6f}  (off by {abs(ratio - TARGET):.1e}). The track-")
        R.append("length ratio could not be tuned onto the nucleon mass ratio")
        if SYM:
            R.append("within the symmetric subspace — may require k=4 harmonics.")
        else:
            R.append("with the available parameter range.")
    else:
        R.append(f"RESULT: search did not hold charge in the symmetric subspace.")
        if SYM:
            R.append(f"Best charge error {cerr:.2e} > 1e-3. The k=1 harmonic")
            R.append("alone is insufficient; add k=4 (cos(9θ/2), sin(9θ/2)).")

    text = "\n".join(R)
    print(text)
    out_dir = Path(__file__).resolve().parents[1] / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / outname
    out_path.write_text(text + "\n")
    print(f"\nWrote: {out_path}")


def run_step8(args):
    """STEP 8: per-segment quark-charge decomposition.

    The per-arc charge integral on one closed (1/2, 1) track decomposes
    in series into three sub-segments (θ ∈ [0, 2π/3], [2π/3, 4π/3],
    [4π/3, 2π]).  On the Z₂×Z₃-symmetric clover these line up with
    the three arc pieces the track crosses — lobe/saddle/lobe for the
    proton t₀ = -π/6 and saddle/lobe/saddle for the neutron t₀ = +π/6.
    Each segment is identified with one *quark*; the expected
    per-segment charges are (+2/3, -1/3, +2/3) for uud and
    (-1/3, +2/3, -1/3) for udd under G1.

    The Z₂×Z₃-symmetric Step-7 modulation is reproduced from work/derived-
    clover.md §Finding and used directly (no DE re-fit).
    """
    N, a2, b2 = args.N, args.a2, args.b2
    # Symmetric Step-7 solution (work/derived-clover.md §Finding).
    Ac = np.array([0.0, -0.48765])
    As = np.array([0.0, +0.65694])
    Bc = np.array([0.0, -0.00038])
    Bs = np.array([0.0, +0.00032])
    a2_sym, b2_sym = 0.32994, 0.03201

    t0_p, t0_n = -pi / 6.0, +pi / 6.0
    Qp_tot, _ = track_charge(t0_p, Ac, As, Bc, Bs, a2_sym, b2_sym, Nth=6000)
    Qn_tot, _ = track_charge(t0_n, Ac, As, Bc, Bs, a2_sym, b2_sym, Nth=6000)
    Qp_seg = track_charge_segments(t0_p, Ac, As, Bc, Bs, a2_sym, b2_sym,
                                    Nth=6000, n_seg=3)
    Qn_seg = track_charge_segments(t0_n, Ac, As, Bc, Bs, a2_sym, b2_sym,
                                    Nth=6000, n_seg=3)

    # Comparison runs: unmodulated (a1 = b1 = 0, Z_6 backbone only) and
    # cos-only modulation (which preserves a proton-neutron reflection
    # symmetry but breaks Z_6 → Z_3).  These help isolate where the
    # lobe/saddle distinction lives in the integrand.
    zero = np.array([0.0, 0.0])
    Qp_seg_unmod = track_charge_segments(t0_p, zero, zero, zero, zero,
                                          a2_sym, b2_sym, Nth=6000, n_seg=3)
    Qn_seg_unmod = track_charge_segments(t0_n, zero, zero, zero, zero,
                                          a2_sym, b2_sym, Nth=6000, n_seg=3)
    Qp_seg_cos = track_charge_segments(t0_p, Ac, zero, zero, zero,
                                        a2_sym, b2_sym, Nth=6000, n_seg=3)
    Qn_seg_cos = track_charge_segments(t0_n, Ac, zero, zero, zero,
                                        a2_sym, b2_sym, Nth=6000, n_seg=3)
    # Per-segment at 6 segments (one per arc on the full closed track)
    Qp_seg6 = track_charge_segments(t0_p, Ac, As, Bc, Bs, a2_sym, b2_sym,
                                     Nth=6000, n_seg=6)
    Qn_seg6 = track_charge_segments(t0_n, Ac, As, Bc, Bs, a2_sym, b2_sym,
                                     Nth=6000, n_seg=6)
    Qp_seg6_unmod = track_charge_segments(t0_p, zero, zero, zero, zero,
                                           a2_sym, b2_sym, Nth=6000, n_seg=6)
    Qn_seg6_unmod = track_charge_segments(t0_n, zero, zero, zero, zero,
                                           a2_sym, b2_sym, Nth=6000, n_seg=6)

    R = []
    R.append("=" * 78)
    R.append("modulated-clover — STEP 8: per-segment quark-charge decomposition")
    R.append("=" * 78)
    R.append("")
    R.append("Each closed (1/2, 1) track is split into 3 equal-θ segments.")
    R.append("Under G1, each segment is a quark; expected charges are")
    R.append("  proton (uud, lobe/saddle/lobe):   (+2/3, -1/3, +2/3) = (+0.6667, -0.3333, +0.6667)")
    R.append("  neutron (udd, saddle/lobe/saddle): (-1/3, +2/3, -1/3) = (-0.3333, +0.6667, -0.3333)")
    R.append("")
    R.append(f"Z₂ × Z₃-symmetric Step-7 modulation:")
    R.append(f"  Ac = [{Ac[0]:+.5f}, {Ac[1]:+.5f}]  As = [{As[0]:+.5f}, {As[1]:+.5f}]")
    R.append(f"  Bc = [{Bc[0]:+.5f}, {Bc[1]:+.5f}]  Bs = [{Bs[0]:+.5f}, {Bs[1]:+.5f}]")
    R.append(f"  a2 = {a2_sym:.5f}   b2 = {b2_sym:+.5f}")
    R.append("")
    R.append(f"PROTON (t₀ = -π/6):")
    R.append(f"  total Q_tube              = {Qp_tot:+.6f}  (target +1.0)")
    R.append(f"  3 equal-θ segments,  full mod  = ({Qp_seg[0]:+.5f}, {Qp_seg[1]:+.5f}, {Qp_seg[2]:+.5f})")
    R.append(f"  3 equal-θ segments,  unmod     = ({Qp_seg_unmod[0]:+.5f}, {Qp_seg_unmod[1]:+.5f}, {Qp_seg_unmod[2]:+.5f})")
    R.append(f"  3 equal-θ segments,  cos-only  = ({Qp_seg_cos[0]:+.5f}, {Qp_seg_cos[1]:+.5f}, {Qp_seg_cos[2]:+.5f})")
    R.append(f"  6 equal-θ segments,  full mod  = ({Qp_seg6[0]:+.5f}, {Qp_seg6[1]:+.5f}, {Qp_seg6[2]:+.5f},")
    R.append(f"                                    {Qp_seg6[3]:+.5f}, {Qp_seg6[4]:+.5f}, {Qp_seg6[5]:+.5f})")
    R.append(f"  6 equal-θ segments,  unmod     = ({Qp_seg6_unmod[0]:+.5f}, {Qp_seg6_unmod[1]:+.5f}, {Qp_seg6_unmod[2]:+.5f},")
    R.append(f"                                    {Qp_seg6_unmod[3]:+.5f}, {Qp_seg6_unmod[4]:+.5f}, {Qp_seg6_unmod[5]:+.5f})")
    R.append(f"  expected (uud)    = (+0.666667, -0.333333, +0.666667)")
    R.append("")
    R.append(f"NEUTRON (t₀ = +π/6):")
    R.append(f"  total Q_tube              = {Qn_tot:+.6f}  (target  0.0)")
    R.append(f"  3 equal-θ segments,  full mod  = ({Qn_seg[0]:+.5f}, {Qn_seg[1]:+.5f}, {Qn_seg[2]:+.5f})")
    R.append(f"  3 equal-θ segments,  unmod     = ({Qn_seg_unmod[0]:+.5f}, {Qn_seg_unmod[1]:+.5f}, {Qn_seg_unmod[2]:+.5f})")
    R.append(f"  3 equal-θ segments,  cos-only  = ({Qn_seg_cos[0]:+.5f}, {Qn_seg_cos[1]:+.5f}, {Qn_seg_cos[2]:+.5f})")
    R.append(f"  6 equal-θ segments,  full mod  = ({Qn_seg6[0]:+.5f}, {Qn_seg6[1]:+.5f}, {Qn_seg6[2]:+.5f},")
    R.append(f"                                    {Qn_seg6[3]:+.5f}, {Qn_seg6[4]:+.5f}, {Qn_seg6[5]:+.5f})")
    R.append(f"  6 equal-θ segments,  unmod     = ({Qn_seg6_unmod[0]:+.5f}, {Qn_seg6_unmod[1]:+.5f}, {Qn_seg6_unmod[2]:+.5f},")
    R.append(f"                                    {Qn_seg6_unmod[3]:+.5f}, {Qn_seg6_unmod[4]:+.5f}, {Qn_seg6_unmod[5]:+.5f})")
    R.append(f"  expected (udd)    = (-0.333333, +0.666667, -0.333333)")
    R.append("")
    # Verdict
    exp_p = np.array([2.0 / 3.0, -1.0 / 3.0, 2.0 / 3.0])
    exp_n = np.array([-1.0 / 3.0, 2.0 / 3.0, -1.0 / 3.0])
    err_p = np.max(np.abs(np.array(Qp_seg) - exp_p))
    err_n = np.max(np.abs(np.array(Qn_seg) - exp_n))
    R.append(f"max |Q_seg - expected|:  proton {err_p:.4f}   neutron {err_n:.4f}")
    R.append("")
    if err_p < 0.05 and err_n < 0.05:
        R.append("RESULT: per-segment charges match the uud / udd pattern.")
        R.append("The 3-quarks-in-series decomposition holds under the symmetric")
        R.append("Step-7 modulation — quark substructure is geometric and color is")
        R.append("the Z₃ phase-track index.")
    elif err_p < 0.20 and err_n < 0.20:
        R.append("RESULT: per-segment charges are CLOSE to the uud / udd pattern")
        R.append("but show modulation-distortion in the per-segment values.")
        R.append("The series structure is right; the exact per-quark fractions")
        R.append("may require refinement (e.g. variable segment boundaries,")
        R.append("or attribution by arc-content rather than equal-θ).")
    else:
        R.append("RESULT: per-segment charges do NOT match the uud / udd pattern.")
        R.append("Either the segment decomposition is wrong, or the per-arc-curvature")
        R.append("identification of quarks needs a different mathematical embodiment.")

    text = "\n".join(R)
    print(text)
    out_dir = Path(__file__).resolve().parents[1] / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "modulated_clover_per_segment.txt"
    out_path.write_text(text + "\n")
    print(f"\nWrote: {out_path}")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--step", choices=["1", "3", "4", "5", "6", "7", "8"], default="3",
                    help="1 = cross-section budget; 3 = modulation/track "
                         "solver; 4 = mass spectrum; 5 = mass-fit sweep; "
                         "6 = global parameter sweep; 7 = path-length mass; "
                         "8 = per-segment quark charge")
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
                    help="step 4/5: ring-direction mesh resolution")
    ap.add_argument("--r-steps", type=int, default=9,
                    help="step 5: number of R_major values in the sweep")
    ap.add_argument("--de-iters", type=int, default=60,
                    help="step 6: differential-evolution maxiter")
    ap.add_argument("--sweep-mesh", type=int, default=48,
                    help="step 6: coarse mesh resolution for the DE search")
    ap.add_argument("--symmetric", action="store_true",
                    help="step 7: restrict modulation to Z₂×Z₃-symmetric "
                         "subspace (k=1 half-integer harmonics only).")
    ap.add_argument("--polish-iters", type=int, default=250,
                    help="step 6: fine-mesh Nelder-Mead polish iterations")
    args = ap.parse_args()

    if args.step == "1":
        run_step1(args)
    elif args.step == "3":
        run_step3(args)
    elif args.step == "4":
        run_step4(args)
    elif args.step == "5":
        run_step5(args)
    elif args.step == "6":
        run_step6(args)
    elif args.step == "7":
        run_step7(args)
    else:
        run_step8(args)


if __name__ == "__main__":
    main()
