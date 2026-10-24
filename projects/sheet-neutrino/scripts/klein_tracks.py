"""Closed tracks on a modulated Klein-bottle tube, and the masses they imply.

What it does
  Builds a Klein-bottle tube in 3D (an immersion: it may pass through itself)
  whose cross-section changes shape around the ring, finds the closed tracks a
  wave can ride, and converts track lengths to masses with sheet-proton's
  path-length rule, mass = 2πħc / L_track (one wavelength per closed track).
  The aim is to test whether ν₁, ν₂ (two two-lap tracks) and ν₃ (a one-lap
  track) can reproduce the measured ratio Δm²₃₁/Δm²₂₁ ≈ 33.6.

Geometry
  Surface point X(t, θ) = ((R + u) cos θ, (R + u) sin θ, v), where (u, v) is
  the cross-section c(t; θ) rotated by θ/2.  Klein closure, X(t, θ+2π) =
  X(−t, θ), then requires c(t; θ+2π) = −c(−t; θ).  Two kinds of shape terms
  satisfy this:
    odd   Σ (A_k, B_k) sin(k t)              unchanged every lap
    morph Σ (C_k, D_k) cos(k t) · cos(θ/2)   flips sign every lap
  The morph terms are what let lobes change into each other around the ring.

Tracks
  A track rides a fixed cross-section parameter t₀.  After one lap it arrives
  at −t₀, so t₀ = 0 and t₀ = π (the mirror points) close in one lap; every
  other t₀ pairs with −t₀ into a single two-lap track.  Tracks a wave rides are
  taken to be the stationary ones (local extrema of length over t₀).

Inputs: command-line options (see --help).
Outputs: printed track table and fit; optional figure in ../outputs/.
"""
import argparse
from pathlib import Path

import numpy as np
from scipy.optimize import minimize


def unpack(p, n_odd, n_morph):
    """Parameter vector → (R, odd dict {k: (A, B)}, morph dict {k: (C, D)})."""
    R = p[0]
    odd = {k + 1: (p[1 + 2 * k], p[2 + 2 * k]) for k in range(n_odd)}
    base = 1 + 2 * n_odd
    morph = {k: (p[base + 2 * k], p[base + 1 + 2 * k]) for k in range(n_morph)}
    return R, odd, morph


def cross_section(t, th, odd, morph):
    """Cross-section point c(t; θ), before the θ/2 rotation."""
    cx = sum(A * np.sin(k * t) for k, (A, B) in odd.items())
    cy = sum(B * np.sin(k * t) for k, (A, B) in odd.items())
    g = np.cos(th / 2)
    cx = cx + g * sum(C * np.cos(k * t) for k, (C, D) in morph.items())
    cy = cy + g * sum(D * np.cos(k * t) for k, (C, D) in morph.items())
    return cx, cy


def surface(t, th, R, odd, morph):
    cx, cy = cross_section(t, th, odd, morph)
    ph = th / 2
    u = cx * np.cos(ph) - cy * np.sin(ph)
    v = cx * np.sin(ph) + cy * np.cos(ph)
    return np.stack([(R + u) * np.cos(th), (R + u) * np.sin(th), v])


def track_length(t0, laps, R, odd, morph, n_per_lap):
    th = np.linspace(0.0, 2 * np.pi * laps, n_per_lap * laps + 1)
    P = surface(np.full_like(th, t0), th, R, odd, morph)
    return float(np.sum(np.linalg.norm(np.diff(P, axis=1), axis=0)))


def tracks(R, odd, morph, n_t0, n_per_lap):
    """Stationary tracks: one-lap at t₀ = 0, π; two-lap at extrema of L(t₀) on (0, π)."""
    one = [(0.0, track_length(0.0, 1, R, odd, morph, n_per_lap)),
           (np.pi, track_length(np.pi, 1, R, odd, morph, n_per_lap))]
    t0 = np.linspace(0, np.pi, n_t0 + 2)[1:-1]
    L = np.array([track_length(t, 2, R, odd, morph, n_per_lap) for t in t0])
    two = []
    for i in range(1, len(L) - 1):
        if (L[i] - L[i - 1]) * (L[i + 1] - L[i]) < 0:
            kind = "max" if L[i] > L[i - 1] else "min"
            two.append((t0[i], L[i], kind))
    return one, two, (t0, L)


def ratio_from_lengths(L1, La, Lb):
    """Δm²₃₁/Δm²₂₁ with masses ∝ 1/L; ν₃ on the one-lap track L1."""
    m = sorted([1 / La, 1 / Lb])
    m3 = 1 / L1
    return (m3**2 - m[0]**2) / (m[1]**2 - m[0]**2)


def best_assignment(one, two, kind="any"):
    """Pick ν₃ = shorter one-lap track, ν₁/ν₂ = the pair of two-lap tracks
    closest (in log ratio) to the target; returns (ratio, L1, La, Lb).
    kind = "max" restricts ν₁/ν₂ to length-maximum tracks."""
    L1 = min(L for _, L in one)
    if kind != "any":
        two = [x for x in two if x[2] == kind]
    best = None
    for i in range(len(two)):
        for j in range(i + 1, len(two)):
            r = ratio_from_lengths(L1, two[i][1], two[j][1])
            if best is None or abs(np.log(r / TARGET)) < abs(np.log(best[0] / TARGET)):
                best = (r, L1, two[i][1], two[j][1])
    return best


def thickness(odd, morph):
    """Smallest/largest spread of the cross-section over one lap (1 = round, 0 = flat)."""
    t = np.linspace(0, 2 * np.pi, 200)
    worst = 1.0
    for th in np.linspace(0, 2 * np.pi, 9):
        cx, cy = cross_section(t, th, odd, morph)
        sv = np.linalg.svd(np.stack([cx - cx.mean(), cy - cy.mean()]), compute_uv=False)
        worst = min(worst, sv[1] / max(sv[0], 1e-12))
    return worst


def objective(p, a):
    R, odd, morph = unpack(p, a.n_odd, a.n_morph)
    t = np.linspace(0, 2 * np.pi, 200)
    extent = max(np.max(np.hypot(*cross_section(t, th, odd, morph)))
                 for th in np.linspace(0, 2 * np.pi, 9))
    if R < a.min_r_ratio * extent or extent < 1e-3:
        return 1e3
    if thickness(odd, morph) < a.min_thickness:
        return 1e3
    one, two, _ = tracks(R, odd, morph, a.n_t0_fit, a.n_per_lap_fit)
    best = best_assignment(one, two, a.track_kind)
    if best is None:
        return 1e2
    return np.log(best[0] / TARGET) ** 2


def report(p, a, label):
    R, odd, morph = unpack(p, a.n_odd, a.n_morph)
    one, two, curve = tracks(R, odd, morph, a.n_t0, a.n_per_lap)
    print(f"\n== {label}")
    print(f"  R={R:.3f}  odd={ {k: (round(A, 3), round(B, 3)) for k, (A, B) in odd.items()} }")
    print(f"  morph={ {k: (round(C, 3), round(D, 3)) for k, (C, D) in morph.items()} }")
    L1min = min(L for _, L in one)
    print("  one-lap tracks (mirror points; wave returns unchanged each lap):")
    for t0, L in one:
        print(f"    t₀={t0:.3f}  L={L:.4f}  L/L₁={L / L1min:.4f}")
    print("  two-lap tracks (wave returns inverted each lap):")
    for t0, L, kind in two:
        print(f"    t₀=±{t0:.3f} ({kind})  L={L:.4f}  L/L₁={L / L1min:.4f}")
    print(f"  cross-section thickness (min/max spread) = {thickness(odd, morph):.3f}")
    best = best_assignment(one, two, a.track_kind)
    if best:
        r, L1, La, Lb = best
        m = sorted([1 / La, 1 / Lb]) + [1 / L1]
        unit2 = a.dm21 / (m[1]**2 - m[0]**2)
        mev = [1e3 * x * np.sqrt(unit2) for x in m]
        print(f"  assignment ν₁,ν₂ = two-lap pair, ν₃ = shorter one-lap: ratio={r:.3f}")
        print(f"  masses (calibrated to Δm²₂₁) = ({mev[0]:.1f}, {mev[1]:.1f}, {mev[2]:.1f}) meV, "
              f"Σm={sum(mev):.0f} meV, m₃/m₁={mev[2] / mev[0]:.3f}, "
              f"two-lap length split={abs(La - Lb) / min(La, Lb) * 100:.2f}%")
        others = [x for x in [1 / L for _, L in one] + [1 / L for _, L, _ in two]
                  if not any(np.isclose(x, y) for y in m)]
        if others:
            extra = sorted(1e3 * x * np.sqrt(unit2) for x in others)
            print(f"  other stationary tracks (must be sterile): "
                  f"{', '.join(f'{x:.1f}' for x in extra)} meV")
    return R, odd, morph, curve


def plot(R, odd, morph, curve, path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1, 2, figsize=(10, 4.2))
    t = np.linspace(0, 2 * np.pi, 400)
    for th in np.linspace(0, 2 * np.pi, 5):
        cx, cy = cross_section(t, th, odd, morph)
        ax[0].plot(cx, cy, label=f"θ = {th / np.pi:.1f}π")
    ax[0].set_aspect("equal")
    ax[0].set_title("Cross-section c(t; θ) in its rotating frame\n(curves coincide unless morph terms are present)")
    ax[0].legend(fontsize=7)
    t0, L = curve
    ax[1].plot(t0, L)
    ax[1].set_xlabel("track position t₀")
    ax[1].set_ylabel("two-lap track length")
    ax[1].set_title("Two-lap track length vs. t₀\n(extrema = stationary tracks)")
    fig.tight_layout()
    path.parent.mkdir(exist_ok=True)
    fig.savefig(path, dpi=120)
    print(f"  figure: {path}")


TARGET = 33.6


def main():
    global TARGET
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--target", type=float, default=33.6, help="Δm²₃₁/Δm²₂₁ target")
    p.add_argument("--dm21", type=float, default=7.53e-5, help="solar Δm²₂₁ in eV²")
    p.add_argument("--n-odd", type=int, default=3, help="number of odd harmonics k = 1..n")
    p.add_argument("--n-morph", type=int, default=2, help="number of morph harmonics k = 0..n-1")
    p.add_argument("--start", type=float, nargs="+",
                   default=[3.0, 1.0, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                   help="initial parameters: R, (A_k, B_k)…, (C_k, D_k)…")
    p.add_argument("--fit", action="store_true", help="search shapes for the target ratio")
    p.add_argument("--restarts", type=int, default=12, help="random restarts for --fit")
    p.add_argument("--seed", type=int, default=1, help="random seed for --fit")
    p.add_argument("--min-r-ratio", type=float, default=1.5,
                   help="require R ≥ this × largest cross-section radius")
    p.add_argument("--min-thickness", type=float, default=0.0,
                   help="reject cross-sections flatter than this (min/max spread)")
    p.add_argument("--track-kind", choices=["any", "max", "min"], default="any",
                   help="which stationary two-lap tracks may host ν₁, ν₂")
    p.add_argument("--n-t0", type=int, default=361, help="t₀ samples for reporting")
    p.add_argument("--n-per-lap", type=int, default=4000, help="θ samples per lap for reporting")
    p.add_argument("--n-t0-fit", type=int, default=121, help="t₀ samples during fit")
    p.add_argument("--n-per-lap-fit", type=int, default=600, help="θ samples per lap during fit")
    p.add_argument("--plot", type=Path, default=None, help="write a figure to this path")
    a = p.parse_args()
    TARGET = a.target

    p0 = np.array(a.start[:1 + 2 * a.n_odd + 2 * a.n_morph], dtype=float)
    R, odd, morph, curve = report(p0, a, "starting shape")

    if a.fit:
        rng = np.random.default_rng(a.seed)
        best = (objective(p0, a), p0)
        for i in range(a.restarts):
            start = best[1] if i == 0 else best[1] + rng.normal(0, 0.15, size=p0.size)
            res = minimize(objective, start, args=(a,), method="Nelder-Mead",
                           options=dict(maxiter=1500, xatol=1e-4, fatol=1e-8))
            if res.fun < best[0]:
                best = (res.fun, res.x)
        R, odd, morph, curve = report(best[1], a, f"best fit (objective {best[0]:.2e})")
    if a.plot:
        plot(R, odd, morph, curve, a.plot)


if __name__ == "__main__":
    main()
