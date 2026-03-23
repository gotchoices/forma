#!/usr/bin/env python3
"""
R26 Track 1d: Spin formula at finite a/R.

The WvM spin formula L_z = ℏ/q was derived in the thin-torus limit
(a << R).  This track re-derives it at finite aspect ratio ε = a/R
to determine whether curvature corrections modify the spin of
different (p,q) modes.

DERIVATION
==========
A photon of energy E = hc/ℓ circulates on a (p,q) torus knot on a
torus with major radius R and minor radius a (ε = a/R).

Position in cylindrical coordinates:
    ρ(t) = R + a cos(pt) = R(1 + ε cos(pt))
    φ(t) = qt
    z(t) = a sin(pt) = Rε sin(pt)

Path tangent speed:
    |v(t)|² = p²a² + q²ρ(t)² = R²[p²ε² + q²(1+ε cos(pt))²]

Path length:
    ℓ = R × I(ε)  where  I(ε) = ∫₀²π √(p²ε² + q²(1+ε cos(pt))²) dt

Instantaneous angular momentum about z:
    L_z(t) = ρ(t) × p_φ = (E/c) × qρ²(t) / |v(t)|

Time-averaged (weighting by dτ = ds/c):
    ⟨L_z⟩ = (hq/ℓ²) × ∫₀²π ρ²(t) dt = hqπ(2R² + a²) / ℓ²

Spin correction factor:
    S(ε) = ⟨L_z⟩ / (ℏ/q) = 2π²q²(2 + ε²) / I²(ε)

S(0) = 1 by construction.  If S(ε) ≠ 1, the spin deviates from ℏ/q.

NOTE: This is the ORBITAL angular momentum of a point-particle photon
on the geodesic.  The photon's INTRINSIC spin (helicity) contributes a
z-component that averages to zero for integer p:

    ⟨s_z⟩ = (ℏ/ℓ) ∫₀²π pa cos(pt) dt = 0
"""

import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import hbar

import numpy as np
from scipy.integrate import quad


def path_length_integrand(t, p, q, eps):
    """Integrand for I(ε) = ∫₀²π √(p²ε² + q²(1+ε cos(pt))²) dt."""
    rho_norm = 1 + eps * math.cos(p * t)
    return math.sqrt(p**2 * eps**2 + q**2 * rho_norm**2)


def compute_I(p, q, eps, npts=10000):
    """Compute I(ε) = ∫₀²π √(p²ε² + q²(1+ε cos(pt))²) dt."""
    result, _ = quad(path_length_integrand, 0, 2 * math.pi,
                     args=(p, q, eps), limit=200)
    return result


def spin_correction(p, q, eps):
    """
    Compute S(ε) = ⟨L_z⟩ / (ℏ/q).

    S(ε) = 2π²q²(2 + ε²) / I²(ε)
    """
    I = compute_I(p, q, eps)
    return 2 * math.pi**2 * q**2 * (2 + eps**2) / I**2


def Lz_over_hbar(p, q, eps):
    """Compute ⟨L_z⟩/ℏ at finite ε."""
    S = spin_correction(p, q, eps)
    return S / q  # S(ε)/q = ⟨L_z⟩/ℏ


def main():
    print("=" * 76)
    print("R26 Track 1d: Spin Formula at Finite a/R")
    print("=" * 76)

    # ================================================================
    # SECTION 1: Verify thin-torus limit
    # ================================================================
    print("\n" + "=" * 76)
    print("SECTION 1: Verify S(ε→0) = 1 for all modes")
    print("=" * 76)

    modes = [(1, 2), (1, 1), (3, 2), (5, 2), (7, 2), (2, 1), (3, 1)]
    eps_small = 0.001

    print(f"\n  ε = {eps_small} (thin-torus limit):")
    print(f"  {'(p,q)':>6s}  {'S(ε)':>10s}  {'L_z/ℏ':>10s}  {'ℏ/q':>10s}")
    for p, q in modes:
        S = spin_correction(p, q, eps_small)
        Lz = Lz_over_hbar(p, q, eps_small)
        target = 1.0 / q
        print(f"  ({p},{q})   {S:10.6f}  {Lz:10.6f}  {target:10.6f}")

    # ================================================================
    # SECTION 2: Spin correction vs ε for key modes
    # ================================================================
    print("\n" + "=" * 76)
    print("SECTION 2: S(ε) for key modes across ε = 0 to 10")
    print("=" * 76)

    eps_vals = [0.001, 0.01, 0.1, 0.5, 1.0, 2.0, 3.0, 5.0, 6.6, 8.0, 10.0]

    print(f"\n  {'ε':>6s}", end="")
    for p, q in modes:
        print(f"  S({p},{q}){' '*(5-len(str(p))-len(str(q)))}", end="")
    print()
    print(f"  {'—'*6}", end="")
    for _ in modes:
        print(f"  {'—'*8}", end="")
    print()

    for eps in eps_vals:
        print(f"  {eps:6.3f}", end="")
        for p, q in modes:
            S = spin_correction(p, q, eps)
            print(f"  {S:8.4f}", end="")
        print()

    # ================================================================
    # SECTION 3: L_z/ℏ vs ε — actual spin values
    # ================================================================
    print("\n" + "=" * 76)
    print("SECTION 3: L_z/ℏ (actual spin) vs ε")
    print("=" * 76)

    print(f"\n  {'ε':>6s}", end="")
    for p, q in modes:
        print(f"  Lz({p},{q}){' '*(4-len(str(p))-len(str(q)))}", end="")
    print()
    print(f"  {'—'*6}", end="")
    for _ in modes:
        print(f"  {'—'*8}", end="")
    print()

    for eps in eps_vals:
        print(f"  {eps:6.3f}", end="")
        for p, q in modes:
            Lz = Lz_over_hbar(p, q, eps)
            print(f"  {Lz:8.4f}", end="")
        print()

    print("\n  Reference spin values:")
    print("    spin-½ = 0.5000")
    print("    spin-1 = 1.0000")
    print("    spin-3/2 = 1.5000")

    # ================================================================
    # SECTION 4: Critical question — does (1,1) approach spin-½?
    # ================================================================
    print("\n" + "=" * 76)
    print("SECTION 4: Can (1,1) become spin-½?")
    print("=" * 76)

    print("\n  Assignment A uses (1,1) modes which have L_z = ℏ at ε=0.")
    print("  If L_z → ℏ/2 at some finite ε, Assignment A would be viable.")

    print(f"\n  L_z/ℏ for (1,1) vs ε:")
    eps_fine = np.linspace(0.001, 20.0, 200)
    for eps in eps_fine:
        Lz = Lz_over_hbar(1, 1, eps)
        if abs(Lz - 0.5) < 0.01:
            print(f"    ε = {eps:.3f}: L_z/ℏ = {Lz:.4f}  ← NEAR SPIN-½!")
            break
    else:
        Lz_at_20 = Lz_over_hbar(1, 1, 20.0)
        print(f"    (1,1) never reaches spin-½ for ε ∈ [0, 20].")
        print(f"    At ε = 20: L_z/ℏ = {Lz_at_20:.4f}")

    # Check monotonicity
    Lz_prev = Lz_over_hbar(1, 1, 0.001)
    monotone = True
    for eps in eps_fine[1:]:
        Lz = Lz_over_hbar(1, 1, eps)
        if Lz > Lz_prev + 1e-10:
            monotone = False
        Lz_prev = Lz

    if monotone:
        print("    L_z/ℏ for (1,1) is monotonically DECREASING with ε.")
        print("    It moves AWAY from spin-1 but TOWARD spin-½?")
    else:
        print("    L_z/ℏ for (1,1) is non-monotonic.")

    # Detailed scan
    print(f"\n  Detailed L_z/ℏ for (1,1):")
    for eps in [0.001, 0.5, 1, 2, 3, 5, 7, 10, 15, 20, 30, 50, 100]:
        Lz = Lz_over_hbar(1, 1, eps)
        print(f"    ε = {eps:7.1f}: L_z/ℏ = {Lz:.6f}")

    # ================================================================
    # SECTION 5: Does (p,2) spin remain ½?
    # ================================================================
    print("\n" + "=" * 76)
    print("SECTION 5: Spin stability of (p,2) modes")
    print("=" * 76)

    print("\n  For the neutrino model, (p,2) modes should maintain spin-½.")
    print("  Check L_z/ℏ for several (p,2) modes across ε:")

    p_vals = [1, 3, 5, 7, 11, 17]
    print(f"\n  {'ε':>6s}", end="")
    for p in p_vals:
        print(f"  ({p:d},2){' '*(6-len(str(p)))}", end="")
    print()
    print(f"  {'—'*6}", end="")
    for _ in p_vals:
        print(f"  {'—'*8}", end="")
    print()

    for eps in [0.001, 0.5, 1.0, 1.93, 3.0, 5.0, 6.6, 9.17, 10.0]:
        print(f"  {eps:6.3f}", end="")
        for p in p_vals:
            Lz = Lz_over_hbar(p, 2, eps)
            print(f"  {Lz:8.4f}", end="")
        print()

    print("\n  Target: all values should be 0.5000 for spin-½.")

    # Check: does higher p give different spin at fixed ε?
    print(f"\n  Spread of L_z/ℏ across p at key ε values:")
    for eps in [1.93, 6.6, 9.17]:
        Lz_vals = [Lz_over_hbar(p, 2, eps) for p in p_vals]
        spread = max(Lz_vals) - min(Lz_vals)
        print(f"    ε = {eps:.2f}: range = [{min(Lz_vals):.6f}, {max(Lz_vals):.6f}], "
              f"spread = {spread:.6f}")

    # ================================================================
    # SECTION 6: Physical interpretation
    # ================================================================
    print("\n" + "=" * 76)
    print("SECTION 6: Physical interpretation")
    print("=" * 76)

    print("""
  The spin correction S(ε) = ⟨L_z⟩/(ℏ/q) modifies the angular
  momentum at finite torus aspect ratio.  Key observations:

  1. S(ε) is the same function of ε for ALL modes with the same
     (p,q) fundamental winding, regardless of harmonic number d.

  2. At ε = 0 (thin torus): S = 1 for all modes (exact).

  3. At finite ε, S(ε) depends on BOTH p and q — the tube winding
     DOES affect the spin through the path geometry, contrary to
     the thin-torus formula.

  4. For q = 2 modes: if S(ε) remains close to 1 for all p at
     the physically relevant ε, then all (p,2) modes are still
     spin-½ and the Track 1a/1b analysis stands.

  5. For (1,1) modes (Assignment A): if S(ε) drops significantly
     below 1 as ε increases, L_z may approach ℏ/2 at some ε,
     potentially resolving Assignment A's spin problem.

  CAVEAT: This calculation treats the photon as a point particle on
  a geodesic.  The full quantum calculation requires computing the
  angular momentum of the electromagnetic field on the embedded
  torus, which may include additional contributions from the field
  structure (polarization, evanescent tails).  The point-particle
  result is an upper bound on the magnitude of finite-ε corrections.
""")

    # ================================================================
    # SECTION 7: Summary
    # ================================================================
    print("=" * 76)
    print("SECTION 7: Summary")
    print("=" * 76)

    # Compute key numbers for summary
    S_12_66 = spin_correction(1, 2, 6.6)
    S_11_66 = spin_correction(1, 1, 6.6)
    S_32_66 = spin_correction(3, 2, 6.6)
    Lz_11_66 = Lz_over_hbar(1, 1, 6.6)
    Lz_12_66 = Lz_over_hbar(1, 2, 6.6)
    Lz_32_66 = Lz_over_hbar(3, 2, 6.6)

    S_11_193 = spin_correction(1, 1, 1.93)
    Lz_11_193 = Lz_over_hbar(1, 1, 1.93)
    Lz_12_193 = Lz_over_hbar(1, 2, 1.93)

    print(f"""
  At the electron's ε = 6.6:
    (1,2): S = {S_12_66:.4f}, L_z/ℏ = {Lz_12_66:.4f}  (target: 0.5000)
    (1,1): S = {S_11_66:.4f}, L_z/ℏ = {Lz_11_66:.4f}  (target: 1.0000)
    (3,2): S = {S_32_66:.4f}, L_z/ℏ = {Lz_32_66:.4f}  (target: 0.5000)

  At Assignment B's ε = 1.93:
    (1,2): L_z/ℏ = {Lz_12_193:.4f}
    (1,1): L_z/ℏ = {Lz_11_193:.4f}
""")


if __name__ == "__main__":
    main()
