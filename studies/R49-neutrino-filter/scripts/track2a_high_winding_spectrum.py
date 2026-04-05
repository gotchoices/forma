"""
R49 Track 2a: High-winding neutrino modes and the electron mass

Questions:
  1. Do neutrino sheet modes reach the electron mass?
  2. How does mass grow with winding number?
  3. At what winding does a neutrino mode match the electron?
  4. What is the mode density at that scale?

Mass formula: m(n₃, n₄) = E₀ × √((n₃/ε)² + (n₄ − n₃·s)²)

For Assignment A at ε = 5, s = 0.022, E₀ ≈ 22.6 meV.
Electron mass = 511 keV = 5.11 × 10⁸ meV.
"""

import math
import numpy as np

M_E_MEV = 0.51099895       # electron mass in MeV
M_E_MEVV = M_E_MEV * 1e9  # in meV (1 MeV = 10⁹ meV)

DM2_21 = 7.53e-5  # eV²


def mu_sq(n3, n4, s, eps):
    return (n3 / eps)**2 + (n4 - n3 * s)**2


def get_E0(eps, s):
    """E₀ from Assignment A: ν₁=(1,1), ν₂=(-1,1)."""
    dm = mu_sq(-1, 1, s, eps) - mu_sq(1, 1, s, eps)
    if dm <= 0:
        return None
    return math.sqrt(DM2_21 / dm) * 1000  # meV


def print_section(title):
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}\n")


def main():
    print("R49 Track 2a: High-Winding Neutrino Modes")
    print("=" * 70)

    eps = 5.0
    s = 0.022
    E0 = get_E0(eps, s)

    print(f"\n  Assignment A: ε = {eps}, s = {s}")
    print(f"  E₀ = {E0:.2f} meV")
    print(f"  Electron mass = {M_E_MEVV:.0f} meV")
    print(f"  Ratio m_e / E₀ = {M_E_MEVV / E0:.0f}")

    mu_electron = M_E_MEVV / E0
    print(f"  Need μ ≈ {mu_electron:.0f} to match electron mass")

    # ── 1. Mass vs winding number ────────────────────────────────

    print_section("1. MASS vs WINDING NUMBER (diagonal modes n₃=n₄=N)")

    print(f"  Diagonal modes (N,N): μ ≈ N×√((1/ε)² + (1-s)²)"
          f" ≈ N×{math.sqrt(1/eps**2 + (1-s)**2):.4f}")
    print()
    print(f"  {'N':>8} {'μ':>10} {'mass':>12} {'mass unit':>10}")
    print(f"  {'-'*8} {'-'*10} {'-'*12} {'-'*10}")

    for N in [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000,
              2000, 5000, 10000, 20000, 23000, 25000]:
        ms = mu_sq(N, N, s, eps)
        mu = math.sqrt(ms)
        mass = E0 * mu  # meV
        if mass < 1000:
            print(f"  {N:8d} {mu:10.1f} {mass:12.2f} {'meV':>10}")
        elif mass < 1e6:
            print(f"  {N:8d} {mu:10.1f} {mass/1000:12.4f} {'eV':>10}")
        elif mass < 1e9:
            print(f"  {N:8d} {mu:10.1f} {mass/1e6:12.4f} {'keV':>10}")
        else:
            print(f"  {N:8d} {mu:10.1f} {mass/1e9:12.4f} {'MeV':>10}")

    # ── 2. Where does μ cross the electron mass? ─────────────────

    print_section("2. ELECTRON MASS CROSSING")

    N_cross = mu_electron / math.sqrt(1/eps**2 + (1-s)**2)
    print(f"  Diagonal crossing: N ≈ {N_cross:.0f}")
    print(f"  That's winding number ~{N_cross:.0f} around both")
    print(f"  the tube and the ring.")

    N_ring_only = mu_electron  # n₃=0: μ = n₄
    print(f"\n  Ring-only crossing (n₃=0, n₄=N): N ≈ {N_ring_only:.0f}")

    N_tube_only = mu_electron * eps  # n₄=0: μ = n₃/ε
    print(f"  Tube-only crossing (n₃=N, n₄=0): N ≈ {N_tube_only:.0f}")

    # ── 3. Mode density at the electron mass scale ───────────────

    print_section("3. MODE DENSITY AT ELECTRON MASS SCALE")

    target_mu = mu_electron
    window = 0.01  # 1% window
    mu_lo = target_mu * (1 - window)
    mu_hi = target_mu * (1 + window)

    count = 0
    n_max = int(N_cross * 1.5)
    # Too many to enumerate naively. Estimate analytically.

    # On a torus with ε=5, s≈0, modes with μ ≈ μ_target lie on
    # an ellipse: (n₃/(ε·μ_target))² + (n₄/μ_target)² ≈ 1
    # Circumference of this ellipse ≈ π(ε·μ + μ)/2 × correction
    # Mode density ≈ circumference of the ellipse ÷ 1 (integer spacing)

    a_axis = eps * target_mu  # semi-axis in n₃ direction
    b_axis = target_mu        # semi-axis in n₄ direction

    # Ramanujan approximation for ellipse circumference
    h = ((a_axis - b_axis) / (a_axis + b_axis))**2
    circ = math.pi * (a_axis + b_axis) * (1 + 3*h/(10 + math.sqrt(4 - 3*h)))

    print(f"  At μ ≈ {target_mu:.0f}:")
    print(f"  Modes lie on an ellipse with semi-axes:")
    print(f"    n₃ axis: ε × μ = {a_axis:.0f}")
    print(f"    n₄ axis: μ = {b_axis:.0f}")
    print(f"  Ellipse circumference ≈ {circ:.0f}")
    print(f"  ⇒ ~{circ:.0f} integer lattice points on the ellipse")
    print(f"  In a ±1% mass window: ~{circ * 2 * window:.0f} modes")

    # ── 4. Energy accumulation scenario ──────────────────────────

    print_section("4. ENERGY ACCUMULATION: NEUTRINO → ELECTRON")

    print("  Could a neutrino accumulate energy in high-winding")
    print("  modes and eventually excite a linked electron mode?\n")

    print(f"  Energy of ν₁ = (1,1): {E0 * math.sqrt(mu_sq(1,1,s,eps)):.2f} meV")
    print(f"  Energy of electron:   {M_E_MEVV:.0f} meV")
    print(f"  Ratio: {M_E_MEVV / (E0 * math.sqrt(mu_sq(1,1,s,eps))):.0f}×")
    print()

    print("  Number of ν₁-energy quanta needed: "
          f"{M_E_MEVV / (E0 * math.sqrt(mu_sq(1,1,s,eps))):.0f}")
    print()

    print("  Energy ladder from ν₁ to electron mass:")
    print(f"  {'Step':>6} {'Mode':>12} {'mass (meV)':>12}"
          f" {'cumulative':>12}")
    print(f"  {'-'*6} {'-'*12} {'-'*12} {'-'*12}")

    cumulative = 0
    for N in [1, 2, 5, 10, 50, 100, 500, 1000, 5000,
              10000, int(N_cross)]:
        ms = mu_sq(N, N, s, eps)
        mass = E0 * math.sqrt(ms)
        cumulative = mass  # single mode, not cumulative addition
        if mass < 1e6:
            print(f"  {N:6d} ({N:4d},{N:4d}) {mass:12.1f} {'meV':>8}")
        else:
            print(f"  {N:6d} ({N:4d},{N:4d}) {mass/1e6:12.4f} {'keV':>8}")

    # ── 5. Cross-sheet resonance ─────────────────────────────────

    print_section("5. CROSS-SHEET RESONANCE")

    print("  The electron on Ma_e is mode (1,2) at ε_e ≈ 0.5.")
    print("  Its Compton wavelength λ̄_C = ℏ/(m_e c) ≈ 386 fm.")
    print()
    print("  A neutrino mode at the same mass has a very different")
    print("  spatial structure:\n")

    E0_eV = E0 / 1000  # eV
    hbar_c_eV_m = 1.054571817e-34 * 299792458 / 1.602176634e-19

    for N in [int(N_cross) - 100, int(N_cross), int(N_cross) + 100]:
        ms = mu_sq(N, N, s, eps)
        mass_eV = E0_eV * math.sqrt(ms)
        L4 = hbar_c_eV_m / E0_eV
        wavelength_ring = L4 / N if N > 0 else float('inf')
        print(f"  Mode ({N},{N}): mass = {mass_eV:.1f} eV")
        print(f"    Ring wavelength: L₄/N = {L4*1e6:.1f} μm / {N}"
              f" = {wavelength_ring*1e9:.2f} nm")
        print(f"    Tube wavelength: L₃/N = {eps*L4*1e6:.1f} μm / {N}"
              f" = {eps*wavelength_ring*1e9:.2f} nm")
        print()

    lambda_C_e = hbar_c_eV_m / (M_E_MEV * 1e6) * 1e15  # fm
    print(f"  Electron Compton wavelength: {lambda_C_e:.1f} fm")
    print(f"  Neutrino mode wavelength at m_e: ~nm scale")
    print(f"  Scale mismatch: ~{1e-9/1e-15:.0f}×")
    print()
    print("  The spatial scales are vastly different.")
    print("  Cross-sheet resonance requires matching ENERGY,")
    print("  not wavelength — and the energy CAN match at")
    print(f"  winding N ≈ {N_cross:.0f}.")

    # ── 6. Summary ───────────────────────────────────────────────

    print_section("6. SUMMARY")

    print(f"  1. Neutrino modes DO reach the electron mass, at")
    print(f"     winding N ≈ {N_cross:.0f} (both tube and ring).")
    print(f"")
    print(f"  2. Mass grows linearly with winding number:")
    print(f"     m ≈ E₀ × N for diagonal modes (N,N).")
    print(f"")
    print(f"  3. Mode density at the electron scale is enormous:")
    print(f"     ~{circ:.0f} modes in a thin shell around m_e,")
    print(f"     ~{circ*2*window:.0f} modes in a ±1% window.")
    print(f"")
    print(f"  4. A single mode at (N,N) ≈ ({int(N_cross)},{int(N_cross)})")
    print(f"     has mass = m_e.  No accumulation of multiple")
    print(f"     low-energy modes is needed — a single high-winding")
    print(f"     mode carries the full electron energy.")
    print(f"")
    print(f"  5. The spatial wavelengths on Ma_ν at this winding")
    print(f"     are ~nm scale — vastly larger than the electron's")
    print(f"     Compton wavelength (~fm).  Cross-sheet coupling")
    print(f"     requires energy matching, not spatial matching.")


if __name__ == '__main__':
    main()
