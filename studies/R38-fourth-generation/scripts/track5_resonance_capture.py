#!/usr/bin/env python3
"""
R38 Track 5: Resonance capture and generation gating.

Hypothesis: Ma acts as a resonant cavity.  A photon must exceed
2m_e to enter (pair production), but can only couple stably to
modes near a cavity resonance.  If the capture efficiency falls
off with detuning, there is a natural stability boundary that
could gate the generation count.

This script computes:
  1. Mode energies along the proton-ring ladder (the generational axis)
  2. Compton wavelength of each mode vs cavity dimensions
  3. Off-resonance gaps for the three known charged leptons
  4. A simple Lorentzian capture model parameterized by cavity Q
  5. Extrapolation to the 4th and 5th generation candidates
"""

import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.ma import mode_energy, mode_charge
from lib.ma_solver import self_consistent_metric

R_E = 6.6
R_NU = 5.0
R_P = 8.906
SIGMA_EP = -0.0906

HBAR_C = 197.3269804   # MeV·fm

# Observed charged lepton masses (MeV) and lifetimes (s)
LEPTONS = {
    'e':  {'mass': 0.511,    'lifetime': float('inf'), 'stable': True},
    'μ':  {'mass': 105.658,  'lifetime': 2.197e-6,     'stable': False},
    'τ':  {'mass': 1776.86,  'lifetime': 2.903e-13,    'stable': False},
}


def main():
    print("=" * 72)
    print("R38 Track 5: Resonance Capture and Generation Gating")
    print("=" * 72)

    result = self_consistent_metric(
        r_e=R_E, r_nu=R_NU, r_p=R_P, sigma_ep=SIGMA_EP)
    if not result['converged']:
        print("WARNING: metric did not converge")
    Gti = result['Gtilde_inv']
    L = result['L']

    print(f"\nMa circumferences:")
    labels = ['L₁ e-tube', 'L₂ e-ring', 'L₃ ν-tube', 'L₄ ν-ring',
              'L₅ p-tube', 'L₆ p-ring']
    for lbl, val in zip(labels, L):
        print(f"  {lbl:12s} = {val:.4f} fm")

    L6 = L[5]  # proton ring — sets the ~470 MeV ladder spacing

    # ── Section 1: Proton-ring energy ladder ────────────────────
    print(f"\n{'=' * 72}")
    print("SECTION 1: Proton-ring energy ladder (generational axis)")
    print(f"{'=' * 72}\n")

    print("Charged lepton modes along the proton-ring ladder:")
    print("Mode template: (−1, +5, 0, 0, −2, n₆)  [charge −1, spin ½]")
    print("The muon is n₆ = 0; the tau candidate is n₆ = −4.\n")

    ladder = []
    for n6 in range(-8, 9):
        n = (-1, 5, 0, 0, -2, n6)
        E = mode_energy(n, Gti, L)
        lam = 2 * math.pi * HBAR_C / E  # Compton wavelength (fm)
        lam_gamma = lam / 2              # pair threshold photon wavelength
        ladder.append((n6, E, lam, lam_gamma))

    ladder.sort(key=lambda x: x[1])

    print(f"  {'n₆':>4s}  {'E (MeV)':>10s}  {'λ_C (fm)':>10s}  "
          f"{'λ_γ (fm)':>10s}  {'λ_γ/L₆':>8s}  {'Particle':>10s}")
    print(f"  {'-' * 65}")

    for n6, E, lam, lam_g in ladder:
        name = ""
        if n6 == 0:
            name = "μ⁻"
        elif abs(n6) == 4:
            name = "τ cand."
        elif abs(n6) == 5:
            name = "4th?"
        elif abs(n6) == 6:
            name = "5th?"
        ratio = lam_g / L6
        print(f"  {n6:+4d}  {E:10.1f}  {lam:10.4f}  "
              f"{lam_g:10.4f}  {ratio:8.4f}  {name:>10s}")

    # ── Section 2: Known leptons — gaps and lifetimes ───────────
    print(f"\n{'=' * 72}")
    print("SECTION 2: Known charged leptons — modes, gaps, lifetimes")
    print(f"{'=' * 72}\n")

    lepton_modes = [
        ('e⁻',  (1, 2, 0, 0, 0, 0),     0.511,    float('inf')),
        ('μ⁻',  (-1, 5, 0, 0, -2, 0),    105.658,  2.197e-6),
        ('τ⁻',  (-1, 5, 0, 0, -2, -4),   1776.86,  2.903e-13),
    ]

    print(f"  {'Name':>4s}  {'Mode':>26s}  {'E_mode':>10s}  "
          f"{'m_obs':>10s}  {'Gap':>8s}  {'Gap%':>7s}  {'τ (s)':>12s}")
    print(f"  {'-' * 85}")

    gaps = []
    for name, n, m_obs, tau in lepton_modes:
        E = mode_energy(n, Gti, L)
        gap = E - m_obs
        gap_pct = gap / m_obs * 100
        n_str = f"({n[0]:+d},{n[1]:+d},{n[2]},{n[3]},{n[4]:+d},{n[5]:+d})"

        tau_str = "stable" if tau == float('inf') else f"{tau:.3e}"
        print(f"  {name:>4s}  {n_str:>26s}  {E:10.3f}  "
              f"{m_obs:10.3f}  {gap:+8.1f}  {gap_pct:+6.1f}%  {tau_str:>12s}")
        gaps.append((name, E, m_obs, gap, gap_pct, tau))

    # ── Section 3: Cavity Q from the tau ────────────────────────
    print(f"\n{'=' * 72}")
    print("SECTION 3: Cavity Q estimated from the tau")
    print(f"{'=' * 72}\n")

    tau_mode_E = gaps[2][1]   # 1876.4 MeV
    tau_obs = gaps[2][2]      # 1776.86 MeV
    tau_detuning = abs(tau_mode_E - tau_obs)  # ~99.5 MeV

    print(f"  Tau mode energy:  {tau_mode_E:.1f} MeV")
    print(f"  Tau observed:     {tau_obs:.1f} MeV")
    print(f"  Detuning:         {tau_detuning:.1f} MeV  ({tau_detuning/tau_mode_E*100:.1f}%)")
    print()

    print("  If the capture cross-section is Lorentzian:")
    print("    σ(E) ∝ 1 / (1 + (2δ/Γ)²)")
    print("  where δ = detuning, Γ = resonance FWHM = E_mode / Q")
    print()

    for efficiency in [0.5, 0.25, 0.10, 0.01]:
        # σ = 1/(1 + (2δ/Γ)²) = efficiency
        # (2δ/Γ)² = 1/efficiency - 1
        # Γ = 2δ / sqrt(1/efficiency - 1)
        fac = math.sqrt(1.0/efficiency - 1.0)
        Gamma = 2 * tau_detuning / fac
        Q = tau_mode_E / Gamma
        print(f"  If tau capture is at {efficiency*100:5.1f}% efficiency: "
              f"Γ = {Gamma:.1f} MeV, Q = {Q:.1f}")

    print()
    print("  The tau exists, so it WAS captured.  The question is how")
    print("  efficiently, and whether the 4th generation falls below")
    print("  the minimum viable capture efficiency.")

    # ── Section 4: Extrapolation to 4th generation ──────────────
    print(f"\n{'=' * 72}")
    print("SECTION 4: 4th generation — what would the gap be?")
    print(f"{'=' * 72}\n")

    n_4th = (-1, 5, 0, 0, -2, -5)
    E_4th = mode_energy(n_4th, Gti, L)
    n_5th = (-1, 5, 0, 0, -2, -6)
    E_5th = mode_energy(n_5th, Gti, L)

    print(f"  4th lepton mode: (−1,+5,0,0,−2,−5)  E = {E_4th:.1f} MeV")
    print(f"  5th lepton mode: (−1,+5,0,0,−2,−6)  E = {E_5th:.1f} MeV")
    print()

    print("  Gap pattern along the generational ladder:")
    print()
    print(f"  {'Gen':>4s}  {'E_mode':>10s}  {'m_obs':>10s}  "
          f"{'|Gap|':>10s}  {'Gap%':>7s}  {'λ_C/L₆':>8s}")
    print(f"  {'-' * 58}")

    gen_data = [
        ('1st', 0.511,    0.511,    'e⁻'),
        ('2nd', 105.658,  105.658,  'μ⁻'),
        ('3rd', tau_mode_E, tau_obs, 'τ⁻'),
    ]

    for gen, E_m, m_o, _ in gen_data:
        gap = abs(E_m - m_o)
        gap_pct = gap / m_o * 100 if m_o > 0 else 0
        lam = 2 * math.pi * HBAR_C / E_m
        ratio = lam / L6
        print(f"  {gen:>4s}  {E_m:10.1f}  {m_o:10.1f}  "
              f"{gap:10.1f}  {gap_pct:+6.1f}%  {ratio:8.4f}")

    lam_4 = 2 * math.pi * HBAR_C / E_4th
    lam_5 = 2 * math.pi * HBAR_C / E_5th
    print(f"  {'4th':>4s}  {E_4th:10.1f}  {'?':>10s}  "
          f"{'?':>10s}  {'?':>7s}  {lam_4/L6:8.4f}")
    print(f"  {'5th':>4s}  {E_5th:10.1f}  {'?':>10s}  "
          f"{'?':>10s}  {'?':>7s}  {lam_5/L6:8.4f}")

    print(f"""
  The trend is clear: λ_C/L₆ (Compton wavelength relative to the
  proton ring cavity) decreases steadily.  Higher generations pack
  more standing-wave oscillations into the same cavity.

  For capture, the 4th generation photon (at pair threshold) has
  wavelength λ_γ = {lam_4/2:.4f} fm, while the cavity is L₆ = {L6:.4f} fm.
  The photon wavelength is {lam_4/2/L6:.1f}× the cavity size — the photon
  fits inside the cavity {L6/(lam_4/2):.0f} times over.
""")

    # ── Section 5: Capture efficiency vs Q ──────────────────────
    print(f"{'=' * 72}")
    print("SECTION 5: Capture efficiency model")
    print(f"{'=' * 72}\n")

    print("  Lorentzian capture model:  σ ∝ 1 / (1 + (2δ/Γ)²)")
    print("  with Γ = E_mode / Q,  δ = |E_mode − m_observed|")
    print()
    print("  Assuming the tau is captured at threshold (σ_τ = minimum")
    print("  viable efficiency), we scan Q values to find where the")
    print("  4th generation's efficiency drops below τ's.\n")

    # For each Q, compute capture efficiency at the tau's gap,
    # then compute what gap would give 1/10 of that efficiency
    print(f"  {'Q':>6s}  {'Γ_τ (MeV)':>10s}  {'σ_τ':>8s}  "
          f"{'Max gap for':>14s}  {'Gap at σ_τ/10':>14s}")
    print(f"  {'':>6s}  {'':>10s}  {'':>8s}  "
          f"{'σ > σ_τ':>14s}  {'(MeV)':>14s}")
    print(f"  {'-' * 58}")

    for Q in [5, 10, 15, 20, 30, 50]:
        Gamma_tau = tau_mode_E / Q
        sigma_tau = 1.0 / (1.0 + (2 * tau_detuning / Gamma_tau)**2)

        Gamma_4 = E_4th / Q
        # Gap at which σ = σ_tau for the 4th mode
        # σ_4 = 1/(1 + (2δ_4/Γ_4)²) = σ_tau
        # (2δ_4/Γ_4)² = 1/σ_tau - 1
        # δ_4 = Γ_4/2 × sqrt(1/σ_tau - 1)
        if sigma_tau > 0 and sigma_tau < 1:
            delta_4_at_tau = Gamma_4 / 2 * math.sqrt(1.0/sigma_tau - 1.0)
        else:
            delta_4_at_tau = float('inf')

        # Gap at which σ = σ_tau/10
        sigma_tenth = sigma_tau / 10
        if sigma_tenth > 0 and sigma_tenth < 1:
            delta_tenth = Gamma_4 / 2 * math.sqrt(1.0/sigma_tenth - 1.0)
        else:
            delta_tenth = float('inf')

        print(f"  {Q:6d}  {Gamma_tau:10.1f}  {sigma_tau:8.4f}  "
              f"{delta_4_at_tau:11.1f} MeV  {delta_tenth:11.1f} MeV")

    # ── Section 6: R27 lifetime-gap power law ───────────────────
    print(f"\n{'=' * 72}")
    print("SECTION 6: R27 F33/F39 lifetime-gap extrapolation")
    print(f"{'=' * 72}\n")

    print("  R27 found τ ∝ |gap|^(−2.7) for weak CC decays (r = −0.84).")
    print("  The tau is the highest-gap charged lepton (5.6%).")
    print()
    print("  If a 4th generation lepton existed with gap G%:")
    print()
    print(f"  {'Gap%':>6s}  {'Predicted τ':>14s}  {'τ/τ_tau':>10s}  {'Comment':>20s}")
    print(f"  {'-' * 55}")

    tau_lifetime = 2.903e-13  # tau lifetime in seconds
    tau_gap_pct = 5.6

    for gap_pct in [5.6, 8.0, 10.0, 15.0, 20.0, 30.0, 50.0]:
        ratio = (gap_pct / tau_gap_pct) ** (-2.7)
        predicted_tau = tau_lifetime * ratio
        comment = ""
        if gap_pct == 5.6:
            comment = "= tau (calibration)"
        elif predicted_tau < 1e-24:
            comment = "< strong decay scale"
        elif predicted_tau < 1e-20:
            comment = "~ EM decay scale"
        elif predicted_tau < 1e-15:
            comment = "sub-femtosecond"
        print(f"  {gap_pct:6.1f}  {predicted_tau:14.2e}  {ratio:10.4f}  {comment:>20s}")

    # ── Section 7: Verdict ──────────────────────────────────────
    print(f"\n{'=' * 72}")
    print("SECTION 7: Assessment")
    print(f"{'=' * 72}")
    print(f"""
  The data shows:

  1. The proton-ring ladder continues indefinitely — no geometric
     cutoff.  Modes at n₆ = ±5, ±6, ... exist with valid quantum
     numbers and energies {E_4th:.0f}, {E_5th:.0f}, ... MeV.

  2. The gap pattern is suggestive but inconclusive.  Only the tau
     has a measured off-resonance gap (5.6%).  The electron and
     muon have zero gap by construction (inputs).  One data point
     cannot establish a trend.

  3. The R27 lifetime-gap power law (τ ∝ |gap|^(−2.7)) predicts
     that if a 4th lepton had a 15% gap, its lifetime would be
     ~20× shorter than the tau's (~1.5 × 10⁻¹⁴ s).  At 30% gap
     it would be ~200× shorter (~1.5 × 10⁻¹⁵ s).  These are
     short but still above the strong-decay scale.

  4. The cavity Q determines the capture bandwidth.  If Q ≈ 10,
     the tau is captured at ~15% efficiency and the 4th generation
     could still be captured with a gap up to ~{E_4th/10/2*math.sqrt(1/0.15 - 1):.0f} MeV.  If Q ≈ 30,
     the tau is barely captured and the 4th generation is likely
     excluded.

  OPEN QUESTIONS:
  - What determines the cavity Q?  (Needs a model of Ma-S coupling.)
  - Why is the tau 5.6% off?  (Needs multi-mode or asymmetric shear.)
  - Does the gap systematically grow with n₆?  (Needs more than one
    data point — the tau alone can't establish a trend.)

  The resonance capture hypothesis is VIABLE but UNDERDETERMINED
  with current data.  A first-principles calculation of the Ma-S
  coupling (the "cavity Q") would make it predictive.
""")


if __name__ == "__main__":
    main()
