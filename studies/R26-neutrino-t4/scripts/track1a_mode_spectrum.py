#!/usr/bin/env python3
"""
R26 Track 1a: Neutrino material sheet mode spectrum.

Computes the full mode spectrum on the neutrino material sheet (Ma_ν) for both Assignment A
and Assignment B.  Verifies the mass-squared ratio Δm²₃₁/Δm²₂₁ = 33.6,
catalogs all modes below 1 eV, and compares Σm with the cosmological bound.

ENERGY FORMULA
==============
On the neutrino material sheet with circumferences L₃, L₄ and shear s = s₃₄:

  E(n₃, n₄) = ℏc √((n₃/L₃)² + ((n₄ − n₃·s)/L₄)²)

Define r = L₃/L₄ (aspect ratio), E₀ = ℏc/L₄ (energy scale).  Then:

  E(n₃, n₄) = E₀ √((n₃/r)² + (n₄ − n₃·s)²)

The mass-squared of mode (n₃, n₄) is proportional to:

  μ²(n₃, n₄) = (n₃/r)² + (n₄ − n₃·s)²

All mass-squared differences and ratios can be computed from μ².
The overall scale E₀ is fixed by the absolute neutrino mass.

ASSIGNMENTS
===========
A: Neutrino triplet = (1,1), (−1,1), (1,2).  Ratio = (3−2s)/(4s).
B: Neutrino triplet = (p₁,2), (p₂,2), (p₃,2), all pᵢ odd.
   Best candidate from README: (1,2), (3,2), (17,2).
"""

import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import h, c

eV_to_J = 1.602176634e-19
hc_eVm = h * c / eV_to_J  # ℏc in eV·m (using h, so E = hc/λ convention)

# Experimental neutrino parameters (PDG 2024, normal ordering)
DM2_21 = 7.53e-5    # eV²  (solar)
DM2_32 = 2.455e-3   # eV²  (atmospheric)
DM2_31 = DM2_32 + DM2_21  # ≈ 2.530e-3 eV²
TARGET_RATIO = DM2_31 / DM2_21
COSMO_BOUND = 0.120  # eV, DESI+CMB Σm bound


def mu_sq(n3, n4, s, r):
    """Dimensionless mass-squared: (n₃/r)² + (n₄ − n₃·s)²."""
    return (n3 / r)**2 + (n4 - n3 * s)**2


def dm2_ratio_A(s):
    """Analytical mass-squared ratio for Assignment A: (3−2s)/(4s)."""
    return (3 - 2 * s) / (4 * s)


def solve_s_for_ratio_A(target):
    """Solve (3−2s)/(4s) = target for s."""
    # 3 - 2s = 4s·target → 3 = s(4·target + 2) → s = 3/(4·target + 2)
    return 3.0 / (4.0 * target + 2.0)


def compute_E0_from_m1(m1_eV, n3_1, n4_1, s, r):
    """Compute E₀ = ℏc/L₄ such that mode (n3_1, n4_1) has mass m₁."""
    ms = mu_sq(n3_1, n4_1, s, r)
    if ms <= 0:
        return None
    return m1_eV / math.sqrt(ms)


def mode_mass(n3, n4, s, r, E0):
    """Absolute mass of mode (n₃, n₄) in eV."""
    ms = mu_sq(n3, n4, s, r)
    if ms <= 0:
        return 0.0
    return E0 * math.sqrt(ms)


def spin_label(n3, n4):
    """WvM spin assignment: L = ℏ/|n₄|, fermion if |n₃| odd."""
    if n4 == 0:
        return "—"
    spin_val = 1.0 / abs(n4)
    fermion = (n3 % 2 != 0)
    if spin_val == 0.5:
        return "½" + (" F" if fermion else " B")
    elif spin_val == 1.0:
        return "1" + (" F" if fermion else " B")
    else:
        return f"1/{abs(n4)}" + (" F" if fermion else " B")


def catalog_modes(s, r, E0, max_eV=1.0, n_range=300):
    """
    Enumerate all modes (n₃, n₄) with mass < max_eV.

    Returns list of (mass_eV, n3, n4, spin_str) sorted by mass.
    Excludes (0,0).
    """
    modes = []
    for n3 in range(-n_range, n_range + 1):
        for n4 in range(-n_range, n_range + 1):
            if n3 == 0 and n4 == 0:
                continue
            m = mode_mass(n3, n4, s, r, E0)
            if m < max_eV:
                modes.append((m, n3, n4, spin_label(n3, n4)))
    modes.sort(key=lambda x: x[0])
    return modes


def print_modes(modes, label, max_show=40):
    """Print a mode catalog with counts by spin type."""
    print(f"\n  {'n₃':>4s}  {'n₄':>4s}  {'mass (meV)':>12s}  {'spin':>6s}")
    print(f"  {'—'*4}  {'—'*4}  {'—'*12}  {'—'*6}")
    for i, (m, n3, n4, sp) in enumerate(modes):
        if i < max_show:
            print(f"  {n3:4d}  {n4:4d}  {m*1e3:12.4f}  {sp:>6s}")
    if len(modes) > max_show:
        print(f"  ... ({len(modes) - max_show} more modes below 1 eV) ...")

    # Count by spin type
    spin_half_f = sum(1 for m, n3, n4, sp in modes if "½ F" in sp)
    spin_1_f = sum(1 for m, n3, n4, sp in modes if "1 F" in sp)
    spin_half_b = sum(1 for m, n3, n4, sp in modes if "½ B" in sp)
    spin_1_b = sum(1 for m, n3, n4, sp in modes if "1 B" in sp)
    other = len(modes) - spin_half_f - spin_1_f - spin_half_b - spin_1_b

    print(f"\n  Total modes below 1 eV: {len(modes)}")
    print(f"    spin-½ fermions: {spin_half_f}")
    print(f"    spin-1 fermions: {spin_1_f}")
    print(f"    spin-½ bosons:   {spin_half_b}")
    print(f"    spin-1 bosons:   {spin_1_b}")
    if other > 0:
        print(f"    other:           {other}")


def main():
    print("=" * 76)
    print("R26 Track 1a: Neutrino Material Sheet Mode Spectrum")
    print("=" * 76)

    # ================================================================
    # SECTION 1: Assignment A — modes (1,1), (−1,1), (1,2)
    # ================================================================
    print("\n" + "=" * 76)
    print("SECTION 1: Assignment A — modes (1,1), (−1,1), (1,2)")
    print("=" * 76)

    print("\n--- 1.1: Analytical ratio ---")
    print("\n  The mass-squared ratio for Assignment A is:")
    print("    Δm²₃₁/Δm²₂₁ = (3 − 2s) / (4s)")
    print("\n  Derivation:")
    print("    μ²(1,1)  = 1/r² + (1−s)²")
    print("    μ²(−1,1) = 1/r² + (1+s)²")
    print("    μ²(1,2)  = 1/r² + (2−s)²")
    print("    Δμ²₂₁ = μ²(−1,1) − μ²(1,1) = (1+s)² − (1−s)² = 4s")
    print("    Δμ²₃₁ = μ²(1,2)  − μ²(1,1) = (2−s)² − (1−s)² = 3 − 2s")
    print("    Ratio = (3 − 2s) / (4s)")
    print("\n  The aspect ratio r cancels completely — the ratio depends only on s.")

    s_A = solve_s_for_ratio_A(TARGET_RATIO)
    ratio_A = dm2_ratio_A(s_A)
    print(f"\n  Experimental target: {TARGET_RATIO:.4f}")
    print(f"  Required shear: s₃₄ = {s_A:.6f}")
    print(f"  Computed ratio:  {ratio_A:.4f}")
    print(f"  Match: {abs(ratio_A - TARGET_RATIO):.2e} (exact by construction)")

    print("\n--- 1.2: Numerical verification ---")
    # Verify with explicit μ² computation at several r values
    print("\n  Verify ratio is r-independent:")
    for r in [0.5, 1.0, 2.0, 5.0, 10.0]:
        m1sq = mu_sq(1, 1, s_A, r)
        m2sq = mu_sq(-1, 1, s_A, r)
        m3sq = mu_sq(1, 2, s_A, r)
        ratio_num = (m3sq - m1sq) / (m2sq - m1sq)
        print(f"    r = {r:5.1f}:  ratio = {ratio_num:.6f}")

    print("\n--- 1.3: Spin classification ---")
    modes_A = [(1, 1), (-1, 1), (1, 2)]
    print(f"\n  {'Mode':>10s}  {'|n₄|':>4s}  {'L':>6s}  {'|n₃| odd?':>10s}  {'Type':>12s}")
    for n3, n4 in modes_A:
        sl = spin_label(n3, n4)
        L_val = f"ℏ/{abs(n4)}" if abs(n4) > 0 else "—"
        odd = "yes" if n3 % 2 != 0 else "no"
        print(f"  ({n3:+d},{n4:d})     {abs(n4):4d}  {L_val:>6s}  {odd:>10s}  {sl:>12s}")
    print("\n  ⚠ Two of three modes are spin-1 fermions — not spin-½.")

    print("\n--- 1.4: Mode catalog (Assignment A) ---")
    # Need to pick r to compute absolute masses.  r doesn't affect the
    # ratio but does affect which other modes are light.
    # Explore r = 1, 2, 5.

    for r_val in [1.0, 3.0]:
        print(f"\n  --- r = {r_val} ---")

        # Fix m₁ by requiring Σm to be near minimum (m₁ → 0 limit)
        # In that limit: m₁² ≈ 0, m₂² = Δm²₂₁, m₃² = Δm²₃₁
        # Use m₁ = 1 meV as a representative small value
        m1_eV = 0.001  # 1 meV
        E0 = compute_E0_from_m1(m1_eV, 1, 1, s_A, r_val)

        m1 = mode_mass(1, 1, s_A, r_val, E0)
        m2 = mode_mass(-1, 1, s_A, r_val, E0)
        m3 = mode_mass(1, 2, s_A, r_val, E0)
        sum_m = m1 + m2 + m3

        print(f"  E₀ = {E0*1e3:.4f} meV  (ℏc/L₄)")
        print(f"  m₁ = m(1,1)  = {m1*1e3:.4f} meV")
        print(f"  m₂ = m(−1,1) = {m2*1e3:.4f} meV")
        print(f"  m₃ = m(1,2)  = {m3*1e3:.4f} meV")
        print(f"  Σm = {sum_m*1e3:.2f} meV")

        # Verify ratio numerically
        ratio_check = (m3**2 - m1**2) / (m2**2 - m1**2)
        print(f"  Δm²₃₁/Δm²₂₁ = {ratio_check:.4f}")

        # Check against experimental Δm² values
        # We can also fix E₀ by matching Δm²₂₁ exactly
        # Δm²₂₁ = E₀² × 4s → E₀ = √(Δm²₂₁ / (4s))
        E0_from_dm2 = math.sqrt(DM2_21 / (4 * s_A))
        m1_phys = mode_mass(1, 1, s_A, r_val, E0_from_dm2)
        m2_phys = mode_mass(-1, 1, s_A, r_val, E0_from_dm2)
        m3_phys = mode_mass(1, 2, s_A, r_val, E0_from_dm2)
        sum_phys = m1_phys + m2_phys + m3_phys

        print(f"\n  Physical scale (E₀ from Δm²₂₁):")
        print(f"  E₀ = {E0_from_dm2*1e3:.4f} meV")
        print(f"  m₁ = {m1_phys*1e3:.4f} meV")
        print(f"  m₂ = {m2_phys*1e3:.4f} meV")
        print(f"  m₃ = {m3_phys*1e3:.4f} meV")
        print(f"  Σm = {sum_phys*1e3:.2f} meV")
        if sum_phys < COSMO_BOUND:
            print(f"  ✓ Below cosmological bound ({COSMO_BOUND*1e3:.0f} meV)")
        else:
            print(f"  ✗ EXCEEDS cosmological bound ({COSMO_BOUND*1e3:.0f} meV)")

        # Full catalog
        print(f"\n  All modes below 1 eV (r={r_val}, physical E₀):")
        modes = catalog_modes(s_A, r_val, E0_from_dm2, max_eV=1.0, n_range=300)
        print_modes(modes, f"Assignment A, r={r_val}")

    # ================================================================
    # SECTION 2: Assignment B — modes (1,2), (3,2), (17,2)
    # ================================================================
    print("\n\n" + "=" * 76)
    print("SECTION 2: Assignment B — modes (1,2), (3,2), (17,2), all spin-½")
    print("=" * 76)

    print("\n--- 2.1: Mass-squared ratio ---")
    print("\n  μ²(p,2) = (p/r)² + (2 − p·s)²")
    print("  For triplet (p₁,2), (p₂,2), (p₃,2):")
    print("    Δμ²₂₁ = (p₂²−p₁²)/r² + (2−p₂s)² − (2−p₁s)²")
    print("    Δμ²₃₁ = (p₃²−p₁²)/r² + (2−p₃s)² − (2−p₁s)²")
    print("  The ratio depends on both s and r (does NOT simplify).")

    s_B = -0.09
    r_B = 1.0
    p1, p2, p3 = 1, 3, 17

    m1sq = mu_sq(p1, 2, s_B, r_B)
    m2sq = mu_sq(p2, 2, s_B, r_B)
    m3sq = mu_sq(p3, 2, s_B, r_B)
    ratio_B = (m3sq - m1sq) / (m2sq - m1sq)

    print(f"\n  At s = {s_B}, r = {r_B}:")
    print(f"    μ²(1,2)  = {m1sq:.6f}")
    print(f"    μ²(3,2)  = {m2sq:.6f}")
    print(f"    μ²(17,2) = {m3sq:.6f}")
    print(f"    Ratio = {ratio_B:.4f}  (target: {TARGET_RATIO:.4f})")
    print(f"    Deviation: {ratio_B - TARGET_RATIO:+.4f}")

    # Scan (s, r) to find exact match
    print("\n--- 2.2: Finding (s, r) for exact ratio ---")
    best_s, best_r, best_dev = None, None, 1e10
    for r_try in [x * 0.01 for x in range(10, 500)]:
        for s_try in [x * 0.001 for x in range(-300, 300)]:
            m1s = mu_sq(p1, 2, s_try, r_try)
            m2s = mu_sq(p2, 2, s_try, r_try)
            m3s = mu_sq(p3, 2, s_try, r_try)
            if m2s - m1s < 1e-15:
                continue
            rat = (m3s - m1s) / (m2s - m1s)
            dev = abs(rat - TARGET_RATIO)
            if dev < best_dev:
                best_dev = dev
                best_s = s_try
                best_r = r_try

    print(f"  Best match: s = {best_s:.4f}, r = {best_r:.4f}")
    m1sq = mu_sq(p1, 2, best_s, best_r)
    m2sq = mu_sq(p2, 2, best_s, best_r)
    m3sq = mu_sq(p3, 2, best_s, best_r)
    ratio_best = (m3sq - m1sq) / (m2sq - m1sq)
    print(f"  Ratio = {ratio_best:.4f}  (deviation: {ratio_best - TARGET_RATIO:+.4f})")

    # Refine with finer grid around best
    best_s2, best_r2, best_dev2 = best_s, best_r, best_dev
    for r_try in [best_r + x * 0.001 for x in range(-50, 51)]:
        if r_try <= 0:
            continue
        for s_try in [best_s + x * 0.0001 for x in range(-50, 51)]:
            m1s = mu_sq(p1, 2, s_try, r_try)
            m2s = mu_sq(p2, 2, s_try, r_try)
            m3s = mu_sq(p3, 2, s_try, r_try)
            if m2s - m1s < 1e-15:
                continue
            rat = (m3s - m1s) / (m2s - m1s)
            dev = abs(rat - TARGET_RATIO)
            if dev < best_dev2:
                best_dev2 = dev
                best_s2 = s_try
                best_r2 = r_try

    print(f"  Refined:  s = {best_s2:.5f}, r = {best_r2:.5f}")
    m1sq = mu_sq(p1, 2, best_s2, best_r2)
    m2sq = mu_sq(p2, 2, best_s2, best_r2)
    m3sq = mu_sq(p3, 2, best_s2, best_r2)
    ratio_refined = (m3sq - m1sq) / (m2sq - m1sq)
    print(f"  Ratio = {ratio_refined:.6f}  (deviation: {ratio_refined - TARGET_RATIO:+.6f})")

    print("\n--- 2.3: Spin classification ---")
    modes_B = [(p1, 2), (p2, 2), (p3, 2)]
    print(f"\n  {'Mode':>10s}  {'|n₄|':>4s}  {'L':>6s}  {'|n₃| odd?':>10s}  {'Type':>12s}")
    for n3, n4 in modes_B:
        sl = spin_label(n3, n4)
        L_val = f"ℏ/{abs(n4)}"
        odd = "yes" if n3 % 2 != 0 else "no"
        print(f"  ({n3:+d},{n4:d})     {abs(n4):4d}  {L_val:>6s}  {odd:>10s}  {sl:>12s}")
    print("\n  ✓ All three modes are spin-½ fermions.")

    print("\n--- 2.4: Mode catalog (Assignment B) ---")
    s_use = best_s2
    r_use = best_r2

    E0_B = math.sqrt(DM2_21 / (mu_sq(p2, 2, s_use, r_use) - mu_sq(p1, 2, s_use, r_use)))
    m1_B = mode_mass(p1, 2, s_use, r_use, E0_B)
    m2_B = mode_mass(p2, 2, s_use, r_use, E0_B)
    m3_B = mode_mass(p3, 2, s_use, r_use, E0_B)
    sum_B = m1_B + m2_B + m3_B

    print(f"\n  Using s = {s_use:.5f}, r = {r_use:.5f}")
    print(f"  E₀ = {E0_B*1e3:.4f} meV")
    print(f"  m₁ = m(1,2)  = {m1_B*1e3:.4f} meV")
    print(f"  m₂ = m(3,2)  = {m2_B*1e3:.4f} meV")
    print(f"  m₃ = m(17,2) = {m3_B*1e3:.4f} meV")
    print(f"  Σm = {sum_B*1e3:.2f} meV")
    if sum_B < COSMO_BOUND:
        print(f"  ✓ Below cosmological bound ({COSMO_BOUND*1e3:.0f} meV)")
    else:
        print(f"  ✗ EXCEEDS cosmological bound ({COSMO_BOUND*1e3:.0f} meV)")

    # Intermediate spin-½ fermion modes between ν₂ and ν₃
    print(f"\n  Intermediate spin-½ fermion modes between m₂ and m₃:")
    n_range = max(abs(p3) + 5, 30)
    all_modes = catalog_modes(s_use, r_use, E0_B, max_eV=1.0, n_range=n_range)
    intermediate = [(m, n3, n4, sp) for m, n3, n4, sp in all_modes
                    if m2_B < m < m3_B and "½ F" in sp]
    if intermediate:
        print(f"  Found {len(intermediate)} intermediate spin-½ fermion modes:")
        for m, n3, n4, sp in intermediate:
            print(f"    ({n3:+d},{n4:d})  m = {m*1e3:.4f} meV")
        print(f"\n  ⚠ These are sterile neutrinos — they violate N_eff if thermalized.")
    else:
        print("  None found.")

    # Full catalog
    print(f"\n  All modes below 1 eV:")
    print_modes(all_modes, "Assignment B")

    # ================================================================
    # SECTION 3: Comparison and summary
    # ================================================================
    print("\n\n" + "=" * 76)
    print("SECTION 3: Summary")
    print("=" * 76)

    print("\n  Assignment A: (1,1), (−1,1), (1,2)")
    print(f"    Shear: s = {s_A:.6f}")
    print(f"    Ratio: (3−2s)/(4s) = {dm2_ratio_A(s_A):.4f} — exact, r-independent")
    print(f"    Spin:  TWO spin-1 fermions + ONE spin-½ fermion")
    print(f"    ⚠ Spin problem: neutrinos must be spin-½")

    print(f"\n  Assignment B: (1,2), (3,2), (17,2)")
    print(f"    Shear: s = {best_s2:.5f}, r = {best_r2:.5f}")
    print(f"    Ratio: {ratio_refined:.4f}")
    print(f"    Spin:  ALL spin-½ fermions ✓")
    n_sterile = len(intermediate)
    print(f"    ⚠ Sterile neutrinos: {n_sterile} intermediate spin-½ modes")

    # Physical scales
    print("\n  Physical scales (from Δm²₂₁):")
    E0_A = math.sqrt(DM2_21 / (4 * s_A))
    L4_A = hc_eVm / E0_A
    print(f"    Assignment A: E₀ = {E0_A*1e3:.2f} meV, L₄ = {L4_A*1e6:.2f} μm")
    L4_B = hc_eVm / E0_B
    print(f"    Assignment B: E₀ = {E0_B*1e3:.2f} meV, L₄ = {L4_B*1e6:.2f} μm")

    print("\n  Cosmological comparison (Σm < 120 meV):")
    for r_val in [1.0, 3.0]:
        E0_phys = math.sqrt(DM2_21 / (4 * s_A))
        m1p = mode_mass(1, 1, s_A, r_val, E0_phys)
        m2p = mode_mass(-1, 1, s_A, r_val, E0_phys)
        m3p = mode_mass(1, 2, s_A, r_val, E0_phys)
        sp = m1p + m2p + m3p
        status = "✓" if sp < COSMO_BOUND else "✗"
        print(f"    A (r={r_val}): Σm = {sp*1e3:.1f} meV  {status}")

    print(f"    B (r={best_r2:.3f}): Σm = {sum_B*1e3:.1f} meV  "
          f"{'✓' if sum_B < COSMO_BOUND else '✗'}")

    print("\n  CONCLUSION:")
    print("  Both assignments reproduce the mass-squared ratio.")
    print("  Assignment A has the spin problem (two spin-1 neutrinos).")
    print("  Assignment B has the sterile neutrino problem.")
    print("  Tracks 1b–1f address these tensions.")


if __name__ == "__main__":
    main()
