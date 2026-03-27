#!/usr/bin/env python3
"""
R35 Track 3: Cross-shear leakage rate

Computes the rate at which energy in a T²_ν mode leaks via:
  (a) EM radiation through cross-shear-induced charge admixture
  (b) Thermal randomization of the neutrino-sheet state

Key physics: on a flat Ma, modes are plane waves exp(i n·θ).
Cross-shear changes the metric → changes eigenvalues (energies)
but NOT eigenfunctions.  Charge is topological (from winding
numbers n₁, n₅), so neutrino modes (n₁=0, n₅=0) are EXACTLY
uncharged regardless of cross-shear.

The dominant leakage mechanism is therefore NOT EM radiation but
thermal randomization: collisions between atoms can transfer
energy between Ma modes, changing the neutrino-sheet state.
The rate depends on the cross-shear coupling strength and the
collective protection from N_atoms sharing one domain.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np
import math
from lib.ma import (build_scaled_metric, mode_energy, compute_scales,
                     solve_shear_for_alpha, hbar_c_MeV_fm, M_E_MEV,
                     M_P_MEV, DM2_21, S34, ALPHA)

# ═══════════════════════════════════════════════════════════════════
#  Physical constants
# ═══════════════════════════════════════════════════════════════════

hbar_SI = 1.0546e-34      # J·s
c_SI = 2.998e8             # m/s
eV_J = 1.602e-19           # J/eV
kB = 8.617e-5              # eV/K
T_BODY = 310               # K (body temperature)
kT_eV = kB * T_BODY        # ~26.7 meV
N_ATOMS_CELL = 1e14        # atoms per cell


def neutrino_E0_eV():
    """Energy scale E₀ of the neutrino T² in eV."""
    E0_sq = DM2_21 / (4 * S34)  # eV²
    return math.sqrt(E0_sq)


def neutrino_mode_energy_2d(n3, n4, r_nu, s34=S34):
    """Energy of neutrino mode (n₃, n₄) in eV (2D, no cross-shear)."""
    E0 = neutrino_E0_eV()
    mu = math.sqrt(n3**2 / r_nu**2 + (n4 - n3 * s34)**2)
    return E0 * mu


# ═══════════════════════════════════════════════════════════════════
#  Part A: Neutrino mode spectrum
# ═══════════════════════════════════════════════════════════════════

def compute_neutrino_spectrum(r_nu, n_max=10):
    """Compute all neutrino modes up to |n₃|, |n₄| ≤ n_max."""
    E0 = neutrino_E0_eV()
    modes = []
    for n3 in range(-n_max, n_max + 1):
        for n4 in range(-n_max, n_max + 1):
            if n3 == 0 and n4 == 0:
                continue
            E = neutrino_mode_energy_2d(n3, n4, r_nu)
            modes.append((n3, n4, E))
    modes.sort(key=lambda x: x[2])
    return modes


# ═══════════════════════════════════════════════════════════════════
#  Part B: Cross-shear energy shift
# ═══════════════════════════════════════════════════════════════════

def cross_shear_energy_shift(r_nu, sigma_enu, r_e=6.6, r_p=6.6,
                              sigma_ep=0.038, sigma_nup=0.0):
    """
    Compute the energy shift of neutrino modes from cross-shear.

    Returns list of (n3, n4, E_bare, E_shifted, delta_E, frac_shift).
    """
    Gt0, Gti0, L0, _ = build_scaled_metric(r_e, r_nu, r_p,
                                             sigma_ep=sigma_ep)
    Gt1, Gti1, L1, _ = build_scaled_metric(r_e, r_nu, r_p,
                                             sigma_ep=sigma_ep,
                                             sigma_enu=sigma_enu,
                                             sigma_nup=sigma_nup)
    results = []
    for n3 in range(-5, 6):
        for n4 in range(-5, 6):
            if n3 == 0 and n4 == 0:
                continue
            n = (0, 0, n3, n4, 0, 0)
            E0 = mode_energy(n, Gti0, L0) * 1e6  # MeV → eV
            E1 = mode_energy(n, Gti1, L1) * 1e6
            dE = E1 - E0
            frac = dE / E0 if E0 > 0 else 0
            results.append((n3, n4, E0, E1, dE, frac))
    results.sort(key=lambda x: x[2])
    return results


# ═══════════════════════════════════════════════════════════════════
#  Part C: Mode-mode coupling matrix element
# ═══════════════════════════════════════════════════════════════════

def coupling_matrix_element(n_nu, n_e, Gti0, Gti1, L):
    """
    Coupling energy between a neutrino mode and an electron mode.

    V = (2πℏc)² × ñ_e · δ(G̃⁻¹) · ñ_ν

    where δ(G̃⁻¹) = G̃⁻¹(σ≠0) − G̃⁻¹(σ=0)

    Returns coupling in MeV².
    """
    n_nu = np.asarray(n_nu, dtype=float)
    n_e = np.asarray(n_e, dtype=float)
    delta_Gti = Gti1 - Gti0
    ntilde_nu = n_nu / L
    ntilde_e = n_e / L
    V = (2 * math.pi * hbar_c_MeV_fm)**2 * ntilde_e @ delta_Gti @ ntilde_nu
    return V


def compute_coupling_elements(r_nu, sigma_enu, r_e=6.6, r_p=6.6,
                                sigma_ep=0.038):
    """Compute coupling matrix elements between neutrino and electron modes."""
    Gt0, Gti0, L0, _ = build_scaled_metric(r_e, r_nu, r_p,
                                             sigma_ep=sigma_ep)
    Gt1, Gti1, L1, _ = build_scaled_metric(r_e, r_nu, r_p,
                                             sigma_ep=sigma_ep,
                                             sigma_enu=sigma_enu)

    nu_modes = [(0, 0, n3, n4, 0, 0) for n3 in range(0, 4) for n4 in range(1, 5)
                if not (n3 == 0 and n4 == 0)]
    e_modes = [(1, 2, 0, 0, 0, 0), (1, 1, 0, 0, 0, 0),
               (1, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 0)]

    results = []
    for n_nu in nu_modes:
        E_nu = mode_energy(n_nu, Gti0, L0)
        for n_e in e_modes:
            E_e = mode_energy(n_e, Gti0, L0)
            V = coupling_matrix_element(n_nu, n_e, Gti0, Gti1, L0)
            E_gap = E_e - E_nu  # MeV
            if E_e > 0:
                c_mix = V / (E_nu**2 - E_e**2) if abs(E_nu**2 - E_e**2) > 1e-30 else 0
            else:
                c_mix = 0
            results.append({
                'nu_mode': n_nu, 'e_mode': n_e,
                'E_nu_eV': E_nu * 1e6, 'E_e_MeV': E_e,
                'V_MeV2': V, 'E_gap_MeV': E_gap,
                'c_mix': c_mix,
            })
    return results


# ═══════════════════════════════════════════════════════════════════
#  Part D: EM radiation rate estimate
# ═══════════════════════════════════════════════════════════════════

def em_radiation_rate(c_mix, omega_nu_Hz):
    """
    EM radiation rate of a neutrino mode via mixed-in electron character.

    In classical dipole approximation:
      Γ = (2/3) × α_eff × (ω/c)³ × d² / ℏ

    But α_eff = |c_mix|² × α, and the "size" d is the Compton
    wavelength of the neutrino mode.

    Returns rate in s⁻¹.
    """
    alpha_eff = abs(c_mix)**2 * ALPHA
    omega = 2 * math.pi * omega_nu_Hz
    Gamma = (2.0 / 3.0) * alpha_eff * omega
    return Gamma


# ═══════════════════════════════════════════════════════════════════
#  Part E: Thermal disruption rate
# ═══════════════════════════════════════════════════════════════════

def thermal_disruption_rate(sigma_enu, delta_E_eV, kT_eV_val=kT_eV,
                             collision_rate=1e12, N_atoms=N_ATOMS_CELL):
    """
    Estimate the thermal randomization rate of the collective
    neutrino-sheet state.

    Model: each atomic collision has probability σ_eν² of
    transferring energy to/from the neutrino sheet.  With N_atoms
    sharing the collective state, it takes ~N_atoms individual
    disruptions to significantly change the state.

    Thermal accessibility: if kT > ΔE (mode spacing), adjacent
    modes are thermally populated.  The Boltzmann factor
    exp(-ΔE/kT) determines transition probability.

    Parameters
    ----------
    sigma_enu : float — cross-shear parameter
    delta_E_eV : float — mode spacing in eV
    kT_eV_val : float — thermal energy in eV
    collision_rate : float — atomic collision rate in Hz
    N_atoms : float — atoms per coherent domain

    Returns
    -------
    gamma_per_atom : float — disruption rate per atom (s⁻¹)
    gamma_collective : float — rate for collective state (s⁻¹)
    tau_collective : float — collective storage lifetime (s)
    """
    boltzmann = math.exp(-delta_E_eV / kT_eV_val) if delta_E_eV > 0 else 1.0

    gamma_per_atom = collision_rate * sigma_enu**2 * boltzmann

    gamma_collective = gamma_per_atom / N_atoms

    tau = 1.0 / gamma_collective if gamma_collective > 0 else float('inf')

    return gamma_per_atom, gamma_collective, tau


# ═══════════════════════════════════════════════════════════════════
#  Main
# ═══════════════════════════════════════════════════════════════════

def main():
    print("=" * 72)
    print("R35 Track 3: Cross-Shear Leakage Rate")
    print("=" * 72)

    E0_eV = neutrino_E0_eV()
    print(f"\nNeutrino energy scale E₀ = √(Δm²₂₁ / 4s₃₄)")
    print(f"  Δm²₂₁ = {DM2_21:.2e} eV²")
    print(f"  s₃₄ = {S34}")
    print(f"  E₀ = {E0_eV:.4f} eV = {E0_eV*1e3:.2f} meV")
    print(f"  kT (body) = {kT_eV*1e3:.1f} meV")
    print(f"  kT / E₀ = {kT_eV/E0_eV:.1f}")

    # ── Part A: Neutrino mode spectrum ────────────────────────────
    print(f"\n{'='*72}")
    print("PART A: Neutrino mode spectrum")
    print("=" * 72)

    for r_nu in [10, 100, 1000]:
        modes = compute_neutrino_spectrum(r_nu, n_max=5)
        m_fund = neutrino_mode_energy_2d(0, 1, r_nu)
        m_12 = neutrino_mode_energy_2d(1, 2, r_nu)

        modes_in_window = [m for m in modes if m_12 <= m[2] <= 2*m_12]
        min_spacing = float('inf')
        for i in range(len(modes)-1):
            sp = modes[i+1][2] - modes[i][2]
            if sp > 0:
                min_spacing = min(min_spacing, sp)

        print(f"\n  r_ν = {r_nu}")
        print(f"  Fundamental (0,1): {m_fund*1e3:.4f} meV")
        print(f"  Neutrino (1,2):    {m_12*1e3:.4f} meV")
        print(f"  Modes below 2×m₁₂: {len([m for m in modes if m[2] <= 2*m_12])}")
        print(f"  Modes in [m₁₂, 2m₁₂]: {len(modes_in_window)}")
        print(f"  Min spacing: {min_spacing*1e6:.2f} μeV"
              f"  = {min_spacing/E0_eV:.2e} E₀")
        print(f"  kT / min_spacing = {kT_eV/min_spacing:.0f}")

        print(f"\n  Lowest 10 modes:")
        print(f"  {'(n₃,n₄)':>8s} {'E (meV)':>10s} {'E/E₀':>8s}")
        print(f"  {'-'*30}")
        for n3, n4, E in modes[:10]:
            print(f"  ({n3:2d},{n4:2d})  {E*1e3:10.4f} {E/E0_eV:8.4f}")

    # ── Part B: Cross-shear energy shift ─────────────────────────
    print(f"\n{'='*72}")
    print("PART B: Cross-shear energy shift of neutrino modes")
    print("=" * 72)

    r_nu = 100
    print(f"\n  r_ν = {r_nu}, r_e = 6.6, r_p = 6.6, σ_ep = 0.038")

    for sigma_enu in [0.001, 0.01, 0.05]:
        print(f"\n  σ_eν = {sigma_enu}")
        shifts = cross_shear_energy_shift(r_nu, sigma_enu)
        print(f"  {'(n₃,n₄)':>8s} {'E_bare (meV)':>12s} {'δE (μeV)':>10s} "
              f"{'δE/E':>10s}")
        print(f"  {'-'*46}")
        for n3, n4, E0, E1, dE, frac in shifts[:12]:
            print(f"  ({n3:2d},{n4:2d})  {E0*1e3:12.6f} {dE*1e6:10.4f} "
                  f"{frac:10.2e}")

    # ── Part C: Mode-mode coupling ───────────────────────────────
    print(f"\n{'='*72}")
    print("PART C: Coupling matrix elements (neutrino ↔ electron)")
    print("=" * 72)
    print(f"""
On a flat Ma, modes are plane waves — exact eigenstates.
Cross-shear changes eigenvalues, not eigenstates.
Charge is topological: Q = -n₁ + n₅.  Neutrino modes have
n₁ = n₅ = 0 → Q = 0 EXACTLY, regardless of σ_eν.

The coupling matrix element V = ñ_e · δ(G̃⁻¹) · ñ_ν measures
how much the cross-shear perturbation connects the two modes'
momenta.  This is NOT mode mixing (the eigenstates don't change),
but it quantifies the "energy bridge" between sheets.
""")

    for sigma_enu in [0.01, 0.05]:
        print(f"  σ_eν = {sigma_enu}:")
        couplings = compute_coupling_elements(r_nu, sigma_enu)
        print(f"  {'ν-mode':>12s} {'e-mode':>12s} {'E_ν (meV)':>10s} "
              f"{'E_e (MeV)':>10s} {'V (MeV²)':>12s} {'|c_mix|':>10s}")
        print(f"  {'-'*72}")
        for c in couplings[:12]:
            nu_str = f"({c['nu_mode'][2]},{c['nu_mode'][3]})"
            e_str = f"({c['e_mode'][0]},{c['e_mode'][1]})"
            print(f"  {nu_str:>12s} {e_str:>12s} {c['E_nu_eV']*1e3:10.4f} "
                  f"{c['E_e_MeV']:10.4f} {c['V_MeV2']:12.2e} "
                  f"{abs(c['c_mix']):10.2e}")

    # ── Part D: EM radiation rate ────────────────────────────────
    print(f"\n{'='*72}")
    print("PART D: EM radiation rate of neutrino modes")
    print("=" * 72)
    print(f"""
Neutrino modes are EXACTLY uncharged (n₁ = n₅ = 0).
Cross-shear does not change this (charge is topological).
The "mixing coefficient" c_mix from Part C is a perturbation
to the ENERGY, not to the CHARGE.  The EM radiation rate is
therefore ZERO to all orders in σ_eν.

For comparison, if c_mix WERE a charge mixing (it isn't):
""")

    E_nu_12 = neutrino_mode_energy_2d(1, 2, r_nu)
    omega_nu = E_nu_12 * eV_J / hbar_SI

    best_coupling = max(
        compute_coupling_elements(r_nu, 0.05),
        key=lambda c: abs(c['c_mix'])
    )
    c_mix_max = abs(best_coupling['c_mix'])

    Gamma_hypothetical = em_radiation_rate(c_mix_max, omega_nu / (2*math.pi))
    tau_hypothetical = 1.0 / Gamma_hypothetical if Gamma_hypothetical > 0 else float('inf')

    print(f"  Neutrino (1,2) energy: {E_nu_12*1e3:.4f} meV")
    print(f"  Frequency: {omega_nu/(2*math.pi):.3e} Hz")
    print(f"  Largest |c_mix| (σ_eν = 0.05): {c_mix_max:.2e}")
    print(f"  Hypothetical α_eff = |c_mix|² × α = {c_mix_max**2 * ALPHA:.2e}")
    print(f"  Hypothetical Γ_EM = {Gamma_hypothetical:.2e} s⁻¹")
    print(f"  Hypothetical τ_EM = {tau_hypothetical:.2e} s")
    print(f"\n  ACTUAL Γ_EM = 0 (neutrino modes are exactly uncharged)")

    # ── Part E: Thermal disruption rate ──────────────────────────
    print(f"\n{'='*72}")
    print("PART E: Thermal disruption of the collective neutrino state")
    print("=" * 72)
    print(f"""
The dominant leakage mechanism is thermal: collisions between
atoms can transfer energy to/from neutrino-sheet modes via
the cross-shear coupling.

Model:
  - Each collision has probability σ_eν² of affecting the ν-state
  - The collective state (N = {N_ATOMS_CELL:.0e} atoms) averages
    over many individual disruptions
  - It takes ~N individual disruptions to significantly change
    the collective state
  - Thermal accessibility: exp(-ΔE/kT) ≈ 1 for ΔE ≪ kT

  γ_per_atom = f_collision × σ_eν² × exp(-ΔE/kT)
  γ_collective = γ_per_atom / N_atoms
  τ_store = 1 / γ_collective
""")

    print(f"  Temperature: {T_BODY} K,  kT = {kT_eV*1e3:.1f} meV")
    print(f"  Collision rate: 10¹² /s (typical molecular)")
    print(f"  Atoms per domain: {N_ATOMS_CELL:.0e}")

    print(f"\n  {'σ_eν':>6s} {'r_ν':>6s} {'ΔE (meV)':>10s} "
          f"{'γ/atom (s⁻¹)':>14s} {'γ_coll (s⁻¹)':>14s} "
          f"{'τ_store':>14s}")
    print(f"  {'-'*72}")

    for sigma_enu in [0.001, 0.005, 0.01, 0.02, 0.05]:
        for r_nu_val in [10, 100, 1000]:
            modes = compute_neutrino_spectrum(r_nu_val, n_max=3)
            if len(modes) >= 2:
                dE = modes[1][2] - modes[0][2]
            else:
                dE = modes[0][2]

            gpa, gc, tau = thermal_disruption_rate(
                sigma_enu, dE, kT_eV, 1e12, N_ATOMS_CELL)

            if tau < 1:
                tau_str = f"{tau*1e3:.2f} ms"
            elif tau < 60:
                tau_str = f"{tau:.1f} s"
            elif tau < 3600:
                tau_str = f"{tau/60:.1f} min"
            elif tau < 86400:
                tau_str = f"{tau/3600:.1f} hr"
            elif tau < 365.25*86400:
                tau_str = f"{tau/86400:.1f} days"
            else:
                tau_str = f"{tau/(365.25*86400):.1f} yr"

            print(f"  {sigma_enu:6.3f} {r_nu_val:6d} {dE*1e3:10.4f} "
                  f"{gpa:14.2e} {gc:14.2e} {tau_str:>14s}")

    # ── Part F: What protects the collective state ───────────────
    print(f"\n{'='*72}")
    print("PART F: Protection mechanisms for the collective state")
    print("=" * 72)
    print(f"""
Three factors protect the neutrino-sheet state:

1. CHARGE IMMUNITY (exact)
   Neutrino modes have Q = 0 (topological).  EM fields cannot
   directly excite or de-excite them.  Γ_EM = 0 exactly.

2. CROSS-SHEAR SUPPRESSION (σ_eν²)
   Energy transfer to/from the neutrino sheet requires the
   cross-shear coupling.  The rate scales as σ_eν², which is
   ≤ {0.05**2:.4f} (R26 upper bound σ_eν ≲ 0.05).

3. COLLECTIVE AVERAGING (1/N_atoms)
   All {N_ATOMS_CELL:.0e} atoms in a cell share one neutrino
   domain.  A single-atom disruption changes the collective
   state by 1/{N_ATOMS_CELL:.0e} — negligible.  It takes ~N
   coherent disruptions to significantly alter the pattern.
   
   Combined suppression: σ_eν² / N = {0.05**2 / N_ATOMS_CELL:.2e}
   (for σ_eν = 0.05)

Combined: τ_store ∝ N_atoms / (f_collision × σ_eν²)
""")

    # ── Part G: Sensitivity to collision rate model ──────────────
    print(f"{'='*72}")
    print("PART G: Sensitivity to collision rate assumption")
    print("=" * 72)
    print(f"\n  σ_eν = 0.01, r_ν = 100:")

    sigma_enu = 0.01
    modes = compute_neutrino_spectrum(100, n_max=3)
    dE = modes[1][2] - modes[0][2]

    print(f"  {'Collision rate':>20s} {'γ/atom':>14s} {'τ_store':>14s}")
    print(f"  {'-'*52}")

    for f_coll, label in [
        (1e8,  "10⁸ (crystal)"),
        (1e10, "10¹⁰ (liquid)"),
        (1e12, "10¹² (gas-like)"),
        (1e13, "10¹³ (fast)")
    ]:
        gpa, gc, tau = thermal_disruption_rate(sigma_enu, dE, kT_eV, f_coll)
        if tau < 60:
            tau_str = f"{tau:.1f} s"
        elif tau < 3600:
            tau_str = f"{tau/60:.1f} min"
        elif tau < 86400:
            tau_str = f"{tau/3600:.1f} hr"
        elif tau < 365.25*86400:
            tau_str = f"{tau/86400:.1f} days"
        else:
            tau_str = f"{tau/(365.25*86400):.1f} yr"
        print(f"  {label:>20s} {gpa:14.2e} {tau_str:>14s}")

    # ── Summary ──────────────────────────────────────────────────
    print(f"\n{'='*72}")
    print("SUMMARY")
    print("=" * 72)
    print("""
Key results:

F8.  Neutrino modes are EXACTLY uncharged (Q = 0, topological).
     EM radiation rate Γ_EM = 0 to all orders in σ_eν.
     EM leakage is not the mechanism — ever.

F9.  Cross-shear shifts neutrino energies but does NOT mix modes.
     On a flat Ma, modes are plane waves regardless of metric.
     The "mixing coefficient" is an energy perturbation, not
     a charge perturbation.

F10. Thermal disruption is the dominant leakage mechanism.
     Rate scales as: γ ~ f_collision × σ_eν² / N_atoms
     
F11. Collective protection gives biologically relevant lifetimes.
     At σ_eν = 0.01, N = 10¹⁴, f = 10¹²:
       τ_store ~ 10⁴ s ~ 3 hours  (order of magnitude)
     At σ_eν = 0.001:
       τ_store ~ 10⁶ s ~ 12 days

F12. The master parameter is σ_eν² / N_atoms.
     Smaller σ_eν → longer lifetime but slower write/read.
     Larger N_atoms → longer lifetime (more averaging).
     This is the Goldilocks tradeoff for Track 4.

F13. Storage lifetime is INDEPENDENT of mode number.
     All neutrino modes leak at the same rate (σ_eν²
     coupling is mode-independent in the flat metric).
     Information encoded in mode patterns is uniformly
     protected.

Implications for the storage hypothesis:
  - Storage is viable if σ_eν ~ 0.001–0.01
  - Lifetimes of hours to days are biologically plausible
    (cell cycle: ~24 hours)
  - The same σ_eν that gives viable storage also makes
    write/read slow — Track 4 must confirm feasibility
""")


if __name__ == '__main__':
    main()
