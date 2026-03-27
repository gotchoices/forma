#!/usr/bin/env python3
"""
R15 Track 5: Self-consistent σ from Coulomb self-energy.

Compute U_total(σ) = U_kinetic(σ) + U_Coulomb(σ) for a Gaussian
wavepacket of angular width σ on the (1,2) geodesic, and check
whether the Coulomb self-interaction can determine σ.

Key question: is U_Coulomb(σ) large enough compared to U_kinetic(σ)
to create a nontrivial balance?
"""

import sys
import os
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import h, hbar, c, eps0, e, alpha as alpha_em, m_e, lambda_C


def compute_track5(R, a, N_sigma=40):
    r = a / R
    L_path = 4 * np.pi * np.sqrt((a / 2)**2 + R**2)

    print(f"\n{'='*65}")
    print(f"R15 Track 5: Self-Consistent σ from Coulomb Self-Energy")
    print(f"  r = {r:.2f}   R = {R:.4e} m   a = {a:.4e} m")
    print(f"  L_path = {L_path:.4e} m   λ_C = {lambda_C:.4e} m")
    print(f"{'='*65}")

    # ════════════════════════════════════════════════════════
    # SECTION 1: Energy scales (analytical)
    # ════════════════════════════════════════════════════════
    print(f"\nSECTION 1  Energy Scales")
    print("-" * 55)

    E_mc2 = m_e * c**2
    E_alpha = alpha_em * E_mc2
    E_mode = h * c / L_path  # energy of one mode spacing

    print(f"  m_e c²          = {E_mc2:.4e} J")
    print(f"  α × m_e c²      = {E_alpha:.4e} J")
    print(f"  Mode spacing ℏω₁ = {E_mode:.4e} J")
    print(f"  ℏω₁ / m_e c²    = {E_mode / E_mc2:.4f}")
    print(f"  Ratio α / 1     = {alpha_em:.6f}")
    print(f"\n  KEY: Coulomb self-energy ~ α × m_e c²")
    print(f"       Kinetic from localization ~ m_e c²")
    print(f"       Ratio: {alpha_em:.4f}  (Coulomb is {1/alpha_em:.0f}× weaker)")

    # ════════════════════════════════════════════════════════
    # SECTION 2: Monopole charge Q(σ)
    # ════════════════════════════════════════════════════════
    print(f"\nSECTION 2  Monopole Charge Q(σ)")
    print("-" * 55)

    # From R15 F5: Q(σ) ∝ σ√π × exp(-25σ²/16)
    # (Gaussian FT at k = 5/2)
    # The charge peaks at σ_peak = √(16/50) = √(8/25) = 2√2/5 ≈ 0.566 rad
    sigma_peak = np.sqrt(8.0 / 25.0)
    print(f"  Q(σ) ∝ σ × exp(-25σ²/16)")
    print(f"  Q peaks at σ = {sigma_peak:.4f} rad")

    sigma_arr = np.linspace(0.2, 5.0, N_sigma)
    Q_shape = sigma_arr * np.exp(-25 * sigma_arr**2 / 16.0)
    Q_shape /= np.max(Q_shape)  # normalize to peak = 1

    # ════════════════════════════════════════════════════════
    # SECTION 3: Kinetic energy of localization U_K(σ)
    # ════════════════════════════════════════════════════════
    print(f"\nSECTION 3  Kinetic Energy of Localization")
    print("-" * 55)

    # The wavepacket is a Gaussian in φ centered at φ₀ with
    # carrier frequency 5/2 (from the (1,2) winding).
    # In the momentum representation, the Fourier amplitudes are:
    #   c_k ∝ exp(-(k - 5/2)² σ²/4)
    # where k = n/2 is the half-integer mode number.
    #
    # The energy of mode k (massless particle on the path):
    #   E_k = |k| × hc/L_path = |k| × E_mode
    #
    # The average energy:
    #   <E> = Σ |c_k|² × E_k / Σ |c_k|²
    #
    # The excess kinetic energy:
    #   U_K = <E> - E_base  where E_base = (5/2) × E_mode ≈ m_e c²

    E_base = 2.5 * E_mode

    U_kin_arr = []
    for sigma in sigma_arr:
        n_max = max(int(20 / sigma), 30)
        ks = np.arange(-n_max, n_max + 1) / 2.0  # half-integer modes

        weights = np.exp(-(ks - 2.5)**2 * sigma**2 / 2.0)
        weights /= np.sum(weights)

        E_avg = np.sum(weights * np.abs(ks) * E_mode)
        U_K = E_avg - E_base
        U_kin_arr.append(U_K)

    U_kin_arr = np.array(U_kin_arr)

    print(f"  E_base = (5/2) × E_mode = {E_base:.4e} J")
    print(f"  E_base / m_e c² = {E_base / E_mc2:.6f}")
    print(f"\n  U_K at σ = 0.5:  {U_kin_arr[np.argmin(np.abs(sigma_arr-0.5))]:.4e} J "
          f"({U_kin_arr[np.argmin(np.abs(sigma_arr-0.5))]/E_mc2:.4f} m_e c²)")
    print(f"  U_K at σ = 1.0:  {U_kin_arr[np.argmin(np.abs(sigma_arr-1.0))]:.4e} J "
          f"({U_kin_arr[np.argmin(np.abs(sigma_arr-1.0))]/E_mc2:.4f} m_e c²)")
    print(f"  U_K at σ = 1.1:  {U_kin_arr[np.argmin(np.abs(sigma_arr-1.1))]:.4e} J "
          f"({U_kin_arr[np.argmin(np.abs(sigma_arr-1.1))]/E_mc2:.4f} m_e c²)")
    print(f"  U_K at σ = 2.0:  {U_kin_arr[np.argmin(np.abs(sigma_arr-2.0))]:.4e} J "
          f"({U_kin_arr[np.argmin(np.abs(sigma_arr-2.0))]/E_mc2:.4f} m_e c²)")

    # ════════════════════════════════════════════════════════
    # SECTION 4: Coulomb self-energy U_C(σ)
    # ════════════════════════════════════════════════════════
    print(f"\nSECTION 4  Coulomb Self-Energy (Monopole)")
    print("-" * 55)

    # The monopole Coulomb self-energy is:
    #   U_mono = Q²(σ) / (4πε₀ × R_eff)
    # where Q(σ) = Q_max × σ√π × exp(-25σ²/16) / Q_max_norm
    #
    # From R7: for charge e on a (1,2) torus at Compton scale,
    #   U_C = α × m_e c²
    # So Q = e gives U_C = α × m_e c².
    #
    # For a wavepacket, Q(σ) = e × [Q_shape(σ) / Q_shape(σ_target)]
    # where σ_target = 1.109 is the value that gives Q = e.

    # Normalize so Q(σ_target) = e
    sigma_target = 1.109
    Q_target_shape = sigma_target * np.exp(-25 * sigma_target**2 / 16.0)

    Q_arr = e * (sigma_arr * np.exp(-25 * sigma_arr**2 / 16.0)) / Q_target_shape

    # Effective Coulomb radius (from R7)
    R_eff = R  # approximate
    U_coul_mono = Q_arr**2 / (4 * np.pi * eps0 * R_eff)

    print(f"  Normalizing: Q(σ = {sigma_target}) = e = {e:.4e} C")
    print(f"  R_eff = R = {R:.4e} m")
    print(f"  U_C(σ = {sigma_target}) = {U_coul_mono[np.argmin(np.abs(sigma_arr-sigma_target))]:.4e} J")
    print(f"  α × m_e c² = {E_alpha:.4e} J")

    show_sigmas = [0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.1, 1.5, 2.0, 3.0, 4.0, 5.0]
    print(f"\n  {'σ':>6s}  {'Q/e':>8s}  {'U_K/m_ec²':>11s}  "
          f"{'U_C/m_ec²':>11s}  {'U_C/U_K':>9s}")

    for target_s in show_sigmas:
        i = np.argmin(np.abs(sigma_arr - target_s))
        sigma = sigma_arr[i]
        ratio = U_coul_mono[i] / U_kin_arr[i] if U_kin_arr[i] > 0 else float('inf')
        note = "  ← α=1/137" if abs(sigma - sigma_target) < 0.1 else ""
        print(f"  {sigma:6.3f}  {Q_arr[i]/e:8.4f}  "
              f"{U_kin_arr[i]/E_mc2:11.6f}  "
              f"{U_coul_mono[i]/E_mc2:11.4e}  "
              f"{ratio:9.4f}{note}")

    # ════════════════════════════════════════════════════════
    # SECTION 5: Total energy and equilibrium
    # ════════════════════════════════════════════════════════
    print(f"\nSECTION 5  Balance and Equilibrium")
    print("-" * 55)

    U_total = U_kin_arr + U_coul_mono

    # Check for minimum
    idx_min = np.argmin(U_total)
    sigma_min = sigma_arr[idx_min]

    # Check sign of dU/dσ at various points
    dU = np.gradient(U_total, sigma_arr)

    print(f"  U_total = U_kinetic + U_Coulomb_monopole")
    print(f"\n  dU/dσ at σ = 0.5: {dU[np.argmin(np.abs(sigma_arr-0.5))]:.4e}")
    print(f"  dU/dσ at σ = 1.0: {dU[np.argmin(np.abs(sigma_arr-1.0))]:.4e}")
    print(f"  dU/dσ at σ = 2.0: {dU[np.argmin(np.abs(sigma_arr-2.0))]:.4e}")

    if idx_min == 0:
        print(f"\n  RESULT: U_total monotonically decreasing → σ → ∞")
    elif idx_min == len(sigma_arr) - 1:
        print(f"\n  RESULT: U_total monotonically increasing → σ → 0")
    else:
        print(f"\n  RESULT: U_total minimum at σ = {sigma_min:.3f}")
        alpha_pred = np.exp(-4 * sigma_min**2)
        print(f"  α = exp(-4σ²) = {alpha_pred:.4e} (1/α = {1/alpha_pred:.1f})")

    # ════════════════════════════════════════════════════════
    # SECTION 6: Why the soliton mechanism fails
    # ════════════════════════════════════════════════════════
    print(f"\nSECTION 6  Analysis")
    print("-" * 55)

    i11 = np.argmin(np.abs(sigma_arr - 1.1))
    i05 = np.argmin(np.abs(sigma_arr - 0.5))
    print(f"""
  At σ = 1.1 (the value that gives α ≈ 1/137):
    U_K = {U_kin_arr[i11]/E_mc2:.4e} × m_e c²
    U_C = {U_coul_mono[i11]/E_mc2:.4e} × m_e c²
    Both are small (~10⁻² m_e c²).

  At σ = 0.5 (more localized):
    U_K = {U_kin_arr[i05]/E_mc2:.4f} × m_e c²  (large)
    U_C = {U_coul_mono[i05]/E_mc2:.4e} × m_e c²  (near peak)

  CRITICAL: Both U_K and U_C DECREASE as σ INCREASES.
  - U_K decreases because wider packet = less localization cost
  - U_C decreases because wider packet = less charge = less energy

  The system minimizes energy by going to σ → ∞.
  There is nothing that INCREASES with σ to create a restoring
  force toward finite σ.

  Furthermore, the Coulomb self-energy of ANY charge
  distribution is POSITIVE (∫ ε₀E²/2 dV ≥ 0).  It always
  ADDS to the total energy, favoring σ → ∞ where Q → 0.

  The soliton mechanism fails for TWO independent reasons:
  1. Both energy contributions decrease with σ → no equilibrium
  2. The self-energy is always positive → always repulsive
""")

    return sigma_arr, U_kin_arr, U_coul_mono


def main():
    print("=" * 65)
    print("R15 Track 5: Self-Consistent σ from Coulomb Self-Energy")
    print("=" * 65)

    r_val = 0.50
    R = lambda_C / (2 * np.pi * np.sqrt(4 + r_val**2))
    a = r_val * R
    compute_track5(R, a)

    print(f"\n{'='*65}")
    print("SUMMARY")
    print("=" * 65)
    print("""
  NEGATIVE RESULT for candidate 1 (soliton / self-interaction).

  The Coulomb self-energy of the charge distribution is:
  - Always POSITIVE (repulsive) — ∫ε₀E²/2 dV ≥ 0
  - Of order α × m_e c² — a factor 1/137 too small to
    compete with the kinetic energy of localization

  Both points independently kill the soliton mechanism:
  - Point 1: the self-interaction is repulsive, so it
    SPREADS the wavepacket (favors σ → ∞), the opposite
    of what's needed for a soliton.
  - Point 2: even if it were attractive, it's too weak
    to balance the kinetic spreading (which is ~ m_e c²).

  The ground state (minimum energy) is σ → ∞: the fully
  delocalized plane wave with zero charge.

  WHAT DETERMINES σ REMAINS OPEN.  The surviving candidates
  from F8 are:
  - #2: Mode structure of the compact space
  - #3: Quantum uncertainty (possibly equivalent to #2)
  - #4: Topology of the (1,2) knot
  - #5: Breaking torus symmetry (non-torus embedding)
  - #6: Dipole radiation pattern (subcase of #5)
""")


if __name__ == '__main__':
    main()
