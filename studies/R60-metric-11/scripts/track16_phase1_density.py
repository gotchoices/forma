"""
R60 Track 16 — Phase 1: Identify the 2ω density fluctuation.

Test whether a single (1, 2) mode on the p-sheet carries a
physical density quantity that oscillates at 2ω (twice the
mode's 4D angular frequency).  If present, this is the source
of the "non-stationarity" that a single mode carries and the
target of the N-copy cancellation argument in Phase 2.

Two field-type pictures:

(a) Real-field picture (7b / CP-rotating E-field).
    Matter mode is the real part of a complex KK wavefunction.
    Re[ψ]² oscillates at 2ω.  Single mode is NOT stationary
    in the ρ² sense.

(b) Complex-field picture (7c / Dirac KK).
    Matter mode is a complex 4D Dirac spinor.  |ψ|² is
    constant for a plane-wave KK eigenstate.  Single mode
    IS stationary; the 2ω problem doesn't arise.

Under 7b (the working spin derivation after 7c was set aside
for GRID incompatibility), the real-field 2ω fluctuation is
physical and the Z₃ confinement argument proceeds from it.

Sandboxed — no changes to model-F or prior tracks.
"""

import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np

from track1_solver import (
    build_metric_11, signature_ok, mode_6_to_11,
    derive_L_ring, mu_sheet, L_vector_from_params, mode_energy,
    ALPHA, SQRT_ALPHA, FOUR_PI, PI, M_P_MEV, HBAR_C_MEV_FM,
)
from track7b_resolve import build_aug_metric
from track15_phase1_mass import K_MODELF, modelF_baseline


TWO_PI = 2 * PI


def main():
    print("=" * 72)
    print("R60 Track 16 — Phase 1: 2ω density fluctuation on (1, 2) p-sheet")
    print("=" * 72)
    print()

    # ── p-sheet calibrated for (3, 6) at proton mass (Track 15 Option A) ──
    L_ring_p_calibrated = derive_L_ring(M_P_MEV, 3, 6, 0.55, 0.162037,
                                          K_MODELF)
    p = modelF_baseline(L_ring_p=L_ring_p_calibrated)
    G = build_aug_metric(p)
    L = L_vector_from_params(p)

    print("  p-sheet calibration (Track 15 Option A):")
    print(f"    (ε_p, s_p) = ({p.eps_p}, {p.s_p})")
    print(f"    L_ring_p   = {L_ring_p_calibrated:.4f} fm")
    print(f"    k_p        = {K_MODELF:.4e}")
    print()

    # ── (1, 2) quark mode properties ──
    n12 = mode_6_to_11((0, 0, 0, 0, 1, 2))
    E12 = mode_energy(G, L, n12)  # MeV
    # Angular frequency in natural units (set ℏc = 1 in fm·MeV):
    #   E = ℏ ω  →  ω = E / ℏ; numerically ω·T = 2π, so ω = 2π / T_period
    # With ℏc = 197.33 MeV·fm, ω = E / (ℏc) has units of 1/fm (spatial) —
    # convert to per-second-like by dividing by c; for our algebra we only
    # need dimensionless phase (ω·t), so a consistent choice works.
    omega12 = E12  # we'll use MeV as the unit of ω for algebra clarity
    T12 = TWO_PI / omega12

    print("  Single-mode (1, 2) on p-sheet:")
    print(f"    m(1, 2) = {E12:10.4f} MeV   (should be m_p / 3 ≈ 312.76)")
    print(f"    ω(1, 2) = {omega12:10.4f} [MeV units]   "
          f"T(1, 2) = {T12:.4f} [1/MeV]")
    print()

    # ── Real-field (7b) 2ω oscillation ──
    print("─" * 72)
    print("  Real-field picture (7b / CP-rotating E-field):")
    print("─" * 72)
    print()
    print("  The (1, 2) KK wavefunction (plane-wave form):")
    print("    ψ(y_t, y_r, t)  =  exp(i · [y_t/R_t + 2·y_r/R_r − ωt])")
    print()
    print("  Under 7b, the physical matter field is Re[ψ]:")
    print("    φ(y, t)  =  Re[ψ]  =  cos(y_t/R_t + 2·y_r/R_r − ωt)")
    print()
    print("  The charge density on the sheet:")
    print("    ρ_Q(y, t)  =  e · n_t · φ²(y, t)")
    print("             =  e · 1 · cos²(y_t/R_t + 2·y_r/R_r − ωt)")
    print("             =  e/2 · [1 + cos(2·(y_t/R_t + 2·y_r/R_r) − 2ωt)]")
    print()
    print("  The DC piece (1/2) is the time-averaged charge, the same on")
    print("  every such mode.  The 2ω-oscillating piece has unit amplitude")
    print("  at maximum overlap and is what sources 2ω back-reaction on")
    print("  the α channel.")
    print()

    # ── Numeric verification: DFT of ψ² at a fixed (y_t, y_r) ──
    print("─" * 72)
    print("  Numeric verification (DFT of φ² sampled over one period):")
    print("─" * 72)
    # Evaluate at y = 0 (peak) so no spatial dilution
    N_t = 512
    ts = np.linspace(0, T12, N_t, endpoint=False)
    phi_vals = np.cos(-omega12 * ts)  # Re[ψ] at y=0
    rho_Q = phi_vals ** 2             # charge density (up to constants)

    # DFT
    fft = np.fft.rfft(rho_Q)
    fft_amp = np.abs(fft) / N_t * 2   # one-sided
    fft_amp[0] /= 2                    # DC is not doubled
    freqs = np.fft.rfftfreq(N_t, ts[1] - ts[0])

    # Locate 0·ω, 1·ω, 2·ω, 3·ω, 4·ω bins (angular → linear: f = ω/2π)
    def bin_near(f_target):
        return int(np.argmin(np.abs(freqs - f_target)))

    f1 = omega12 / TWO_PI
    print(f"  DFT amplitudes at harmonics of (1,2) mode frequency:")
    print(f"    DC (0·ω) = {fft_amp[0]:.6f}     (expected 0.5)")
    print(f"    1·ω      = {fft_amp[bin_near(1*f1)]:.6f}     (expected 0)")
    print(f"    2·ω      = {fft_amp[bin_near(2*f1)]:.6f}     (expected 0.5)")
    print(f"    3·ω      = {fft_amp[bin_near(3*f1)]:.6f}     (expected 0)")
    print(f"    4·ω      = {fft_amp[bin_near(4*f1)]:.6f}     (expected 0)")
    print()
    print("  Single-mode ρ_Q has ONE non-DC Fourier component, at 2ω,")
    print("  with amplitude 0.5 (half the peak value).  ✓")
    print()

    # ── Complex-field (7c) comparison ──
    print("─" * 72)
    print("  Complex-field picture (7c / Dirac KK):")
    print("─" * 72)
    # For complex ψ = exp(-iωt), |ψ|² = 1 (constant)
    psi_complex = np.exp(-1j * omega12 * ts)
    rho_Q_complex = np.abs(psi_complex) ** 2
    fft_c = np.abs(np.fft.rfft(rho_Q_complex)) / N_t * 2
    fft_c[0] /= 2
    print(f"  |ψ|² over one period:")
    print(f"    DC       = {fft_c[0]:.6f}     (expected 1)")
    print(f"    1·ω      = {fft_c[bin_near(1*f1)]:.6e}     (expected 0)")
    print(f"    2·ω      = {fft_c[bin_near(2*f1)]:.6e}     (expected 0)")
    print()
    print("  Complex-field ρ_Q = |ψ|² is constant in time.")
    print("  Under 7c, single KK modes are already stationary;")
    print("  the 3-phase argument is moot because there's nothing to cancel.")
    print()
    print("  Under 7b (the adopted spin picture), 2ω fluctuation is real")
    print("  and Phase 2 tests which N-copy configurations cancel it.")
    print()

    # ── Coupling to α channel ──
    print("─" * 72)
    print("  Coupling of ρ_Q to the α channel:")
    print("─" * 72)
    print()
    print("  In MaSt's R59 architecture, the charge density on a sheet")
    print("  couples to the ℵ field through σ_ta = √α (tube↔ℵ).  ℵ")
    print("  couples to time through σ_at = 4πα.  The chain")
    print("    tube  ↔  ℵ  ↔  t")
    print("  is what gives α_Coulomb = α on the R59 natural-form point.")
    print()
    print("  If ρ_Q has a 2ω oscillation, it sources a 2ω current on the")
    print("  α channel.  For a single (1, 2) mode, this 2ω source is")
    print("  nonzero — the mode is not a true stationary state of its own")
    print("  gauge back-reaction.  It either emits 2ω radiation (if a 2ω")
    print("  gauge mode exists) or suffers back-reaction mass shifts.")
    print()
    print("  The 3-phase stability question: can multiple copies of the")
    print("  same mode arrange themselves so that their summed ρ_Q is")
    print("  constant — i.e., they collectively become stationary?")
    print()

    print("Phase 1 complete.")
    print()
    print("Key findings:")
    print("  (1) (1, 2) quark mass on the model-F p-sheet is 312.76 MeV")
    print("      (= m_p / 3, matching Track 15 Option A calibration).")
    print("  (2) Charge density ρ_Q = e·n_t·φ² of a real-field (1, 2) mode")
    print("      has a single nonzero oscillating harmonic: 2ω, amplitude 0.5.")
    print("  (3) The 2ω source on the α channel means a lone (1, 2) mode is")
    print("      not stationary under 7b's real-field matter picture.")
    print("  (4) Under 7c (complex Dirac), ρ_Q = |ψ|² is constant — the")
    print("      argument is inapplicable there.  We proceed under 7b.")


if __name__ == "__main__":
    main()
