"""
R63 Track 10 Phase 10a — Geometric slot-fit on the p-sheet (1, 2) eigenmode.

Hypothesis A: at the g-candidate baseline (ε_p = 0.55, s_p = 0.162), the
(1, 2) primitive eigenmode on the p-sheet has a localization profile that
permits k = 6 strands at 60° offsets in θ₂ — corresponding to the
3 colors × 2 spins Pauli capacity = the deuteron.

What this script computes:
  1. Sturm-Liouville eigenvalue problem for the (n_t, n_r) = (1, 2) mode
     on a curved torus with aspect ratio ε and shear s, modifying R21
     Track 1's solver to admit shear via q_eff = n_r − s · n_t.
  2. The lowest eigenvalue λ₀ and corresponding eigenfunction f(θ₁).
  3. Density profile |f(θ₁)|² and its angular FWHM.
  4. Geometric "fit" criterion: can N copies of this mode at uniform
     θ₂ offsets (= 2π/N spacing) coexist on the p-sheet without
     spatial overlap?  Compare to N = 2 (electron 1s capacity), N = 3
     (proton Z₃), N = 6 (deuteron Pauli saturation).

The torus surface area at tube angle θ₁ is proportional to (1 + ε cos θ₁);
at the outer equator (θ₁ = 0) the ring circumference is 2π·a·(1 + ε)/ε,
at the inner equator (θ₁ = π) it is 2π·a·(1 − ε)/ε.  The "fit" question
is whether a strand's effective spread in θ₂ (set by the mode profile)
allows N parallel copies at uniform offsets without overlap, evaluated
at the most-constrained (smallest-circumference) θ₁ position.

Reference for Sturm-Liouville form (with shear):
  d/dθ₁ [(1 + ε cos θ₁) df/dθ₁]
    + [λ (1 + ε cos θ₁) − ε² q²/(1 + ε cos θ₁)] f = 0
where q = q_eff = n_r − s · n_t.

Outputs (../outputs/):
  - track10_phase10a_density_profile.png
  - track10_phase10a_fit_summary.csv
"""

import sys, os
import math
import csv
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg


# ─── Sturm-Liouville eigenvalue problem ───────────────────────────────

def build_eigensystem(eps, q_eff, N=512):
    """Build the (S, W) generalized eigenvalue problem.

    For modes ψ = f(θ₁) · e^(i q_eff θ₂) on a torus with aspect ratio
    ε = a/R and effective ring winding q_eff = n_r − s · n_t,
    the eigenvalue equation is

        −[p f']' + (ε² q² / p) f = λ p f

    with p(θ₁) = 1 + ε cos(θ₁).  Discretize on N points with periodic
    boundary conditions (θ₁ ∈ [0, 2π)).  Returns (S, W) such that the
    generalized eigenvalues solve  S · f = λ · W · f.
    """
    h = 2 * math.pi / N
    theta = np.array([2 * math.pi * j / N for j in range(N)])
    p = 1 + eps * np.cos(theta)

    p_plus  = (p + np.roll(p, -1)) / 2  # midpoint to next
    p_minus = (p + np.roll(p, +1)) / 2  # midpoint to prev

    # Diagonal of S: (p_minus + p_plus)/h² + ε²q²/p
    main_diag = (p_minus + p_plus) / h**2 + (eps**2 * q_eff**2) / p
    upper_diag = -p_plus / h**2
    lower_diag = -p_minus / h**2

    S = np.zeros((N, N))
    for j in range(N):
        S[j, j] = main_diag[j]
        S[j, (j + 1) % N] = upper_diag[j]
        S[j, (j - 1) % N] = lower_diag[j]

    W = np.diag(p)
    return S, W, theta


def solve_mode(eps, q_eff, n_t, N=512):
    """Return (λ, f, θ) for the n_t-th excited mode at given ring winding.

    Eigenvalues come ordered.  For q_eff ≠ 0 on a curved torus, modes
    with the same ring winding come in a tower indexed by n_t (the
    "tube-direction" quantum number).  For each n_t > 0 there are two
    parity-split modes (cos-like / sin-like).  We pick the lower of
    the two, which is the cos-like (even) mode that peaks at the
    outer equator.

    Index map (lowest first):
      0 → n_t = 0 ground state
      1 → n_t = 1 (cos-like, even parity, lower)
      2 → n_t = 1 (sin-like, odd parity, slightly higher)
      3 → n_t = 2 (cos-like)
      4 → n_t = 2 (sin-like)
      ...
    """
    S, W, theta = build_eigensystem(eps, q_eff, N)
    eigvals, eigvecs = linalg.eigh(S, W)
    if n_t == 0:
        idx = 0
    else:
        idx = 1 + 2 * (n_t - 1)  # cos-like for given n_t
    lam = eigvals[idx]
    f   = eigvecs[:, idx]
    return lam, f, theta, eigvals[:8]


def measure_fwhm(theta, density):
    """Full-width at half-maximum of a density profile on [0, 2π).

    Returns (theta_peak, fwhm_radians).
    """
    peak_idx = int(np.argmax(density))
    peak_val = density[peak_idx]
    half_val = peak_val / 2

    # Walk left and right from peak until we drop below half_val
    n = len(theta)

    def walk(direction):
        for k in range(1, n):
            j = (peak_idx + direction * k) % n
            if density[j] < half_val:
                # linear interp between (peak_idx + (k-1)*direction)
                # and j
                j_prev = (peak_idx + direction * (k - 1)) % n
                d1 = density[j_prev]
                d2 = density[j]
                frac = (d1 - half_val) / (d1 - d2) if d1 != d2 else 0.5
                idx_at_half = j_prev + direction * frac
                return idx_at_half * (2 * math.pi / n)
        return None

    theta_left  = walk(-1)
    theta_right = walk(+1)
    if theta_left is None or theta_right is None:
        return theta[peak_idx], 2 * math.pi  # never drops below half

    fwhm = (theta_right - theta_left) % (2 * math.pi)
    if fwhm > math.pi:
        fwhm = 2 * math.pi - fwhm
    return theta[peak_idx], fwhm


# ─── Geometric fit ────────────────────────────────────────────────────

def fit_test(eps, fwhm_theta1, N_target=6):
    """Can N parallel copies of a (1,2) mode at uniform θ₂ offsets fit?

    The (1, 2) eigenmode density is uniform in θ₂ but localized in θ₁.
    Two copies at θ₂ offset Δ are parallel geodesics; they never
    intersect in the geometric sense.  But their density "ribbons"
    extend across the surface; the relevant question is whether the
    ribbons overlap in θ₂ at the most-constrained θ₁ position
    (typically the inner equator at θ₁ = π for ε < 1, where the ring
    is narrowest).

    The ribbon's projected θ₂ extent is determined by the geodesic
    slope — for a (1, 2) mode the geodesic advances Δθ₂ = 2 · Δθ₁ /
    n_t = 2 · Δθ₁ per unit poloidal advance, so a tube-direction
    ribbon of width fwhm_theta1 occupies a θ₂ band of width
    2 · fwhm_theta1 in the unrolled sheet.

    Slot constraint: N copies at 2π/N offset fit if 2π/N ≥ ribbon
    θ₂ width, i.e., N ≤ 2π / (2 · fwhm_theta1) = π / fwhm_theta1.
    """
    ribbon_theta2_width = 2 * fwhm_theta1   # for (n_t, n_r) = (1, 2)
    N_max = math.pi / fwhm_theta1
    return N_max, ribbon_theta2_width


# ─── Main ─────────────────────────────────────────────────────────────

# g-candidate p-sheet baseline
EPS_P = 0.55
S_P   = 0.162037

# Mode of interest: (n_t, n_r) = (1, 2), the proton's primitive quark
N_T = 1
N_R = 2

# Targets to compare
TARGETS = [
    ('electron 1s', 2, "1 group at 180° offset"),
    ('proton Z₃',   3, "3 groups at 120° offsets"),
    ('deuteron PS', 6, "6 groups at 60° offsets"),
]


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 100)
    print("R63 Track 10 Phase 10a — Geometric slot-fit, (1, 2) eigenmode on p-sheet")
    print("=" * 100)
    print()

    q_eff = N_R - S_P * N_T
    print(f"  Mode: (n_t, n_r) = ({N_T}, {N_R})")
    print(f"  p-sheet ε_p = {EPS_P}, s_p = {S_P}")
    print(f"  Effective ring winding q_eff = n_r − s·n_t = {q_eff:.6f}")
    print()

    # Solve the SL eigensystem for the n_t = 1 mode (cos-like)
    lam0, f0, theta, eigvals_low = solve_mode(EPS_P, q_eff, n_t=N_T, N=512)

    print(f"  Lowest 8 eigenvalues: {[f'{lv:.4f}' for lv in eigvals_low]}")
    flat_lam = N_T**2 + EPS_P**2 * q_eff**2
    print(f"  Selected (n_t={N_T}) eigenvalue: λ = {lam0:.6f}")
    print(f"    (compare flat-torus value: λ_flat = n_t² + ε²q² "
          f"= {flat_lam:.6f})")
    print()

    # |f|² density profile (selected mode)
    density = np.abs(f0)**2
    density /= np.trapezoid(density, theta) / (2 * math.pi)  # normalize ⟨|f|²⟩=1

    theta_peak, fwhm = measure_fwhm(theta, density)
    print(f"  Density profile of ground mode:")
    print(f"    peak θ₁ = {math.degrees(theta_peak):.2f}°")
    print(f"    FWHM Δθ₁ = {math.degrees(fwhm):.2f}°")
    print()

    # Geometric fit test
    N_max, ribbon_w = fit_test(EPS_P, fwhm)
    print(f"  Geometric fit:")
    print(f"    Ribbon θ₂ width (for n_r=2 slope): {math.degrees(ribbon_w):.2f}°")
    print(f"    Max copies that fit at uniform offsets: N_max = {N_max:.2f}")
    print()

    print(f"  Capacity check:")
    print(f"    {'Target':<14s}  {'N':>3s}  {'offset':>8s}  {'fits?':>8s}")
    for name, N, descr in TARGETS:
        fits = N <= N_max
        offset_deg = 360.0 / N
        marker = "✓ yes" if fits else "✗ NO"
        print(f"    {name:<14s}  {N:>3d}  {offset_deg:>7.1f}°  {marker:>8s}")
    print()

    # Plot the density profile
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    ax = axes[0]
    ax.plot(np.degrees(theta), density, color='tab:orange', linewidth=1.6)
    ax.axhline(np.max(density)/2, color='gray', linestyle=':', alpha=0.5,
               label='half-max')
    ax.set_xlabel('θ₁ (degrees)')
    ax.set_ylabel('|f(θ₁)|² (normalized)')
    ax.set_title(f'(1, 2) eigenmode density on p-sheet\n(ε={EPS_P}, s={S_P})')
    ax.set_xlim(0, 360)
    ax.grid(alpha=0.3)
    ax.legend()

    # Sketch slot positions for N = 2, 3, 6 in θ₂
    ax = axes[1]
    for ii, (name, N, descr) in enumerate(TARGETS):
        y = ii
        positions = [k * 360.0 / N for k in range(N)]
        for pos in positions:
            ax.plot([pos - math.degrees(ribbon_w)/2, pos + math.degrees(ribbon_w)/2],
                    [y, y], color='tab:blue', linewidth=8, alpha=0.6)
            ax.plot([pos], [y], 'o', color='tab:red', markersize=6)
        ax.text(-5, y, f'{name}\n(N={N})', ha='right', va='center', fontsize=9)
    ax.set_xlim(-30, 390)
    ax.set_ylim(-0.5, len(TARGETS) - 0.5)
    ax.set_xlabel('θ₂ (degrees)')
    ax.set_yticks([])
    ax.set_title(f'Slot offsets vs ribbon θ₂ width ({math.degrees(ribbon_w):.1f}°)\n'
                 f'overlap if ribbons collide')
    ax.grid(alpha=0.3, axis='x')

    plt.tight_layout()
    fig.savefig(out_dir / "track10_phase10a_density_profile.png",
                dpi=150, bbox_inches='tight')
    plt.close()

    # CSV
    csv_path = out_dir / "track10_phase10a_fit_summary.csv"
    with open(csv_path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['quantity', 'value'])
        w.writerow(['eps_p', EPS_P])
        w.writerow(['s_p', S_P])
        w.writerow(['n_t', N_T])
        w.writerow(['n_r', N_R])
        w.writerow(['q_eff', q_eff])
        w.writerow(['lambda_0', lam0])
        w.writerow(['theta1_peak_deg', math.degrees(theta_peak)])
        w.writerow(['fwhm_theta1_deg', math.degrees(fwhm)])
        w.writerow(['ribbon_theta2_width_deg', math.degrees(ribbon_w)])
        w.writerow(['N_max', N_max])
        for name, N, _ in TARGETS:
            w.writerow([f'fits_{name.replace(" ","_")}', N <= N_max])

    print(f"  Plot: {out_dir / 'track10_phase10a_density_profile.png'}")
    print(f"  CSV:  {csv_path}")


if __name__ == "__main__":
    main()
