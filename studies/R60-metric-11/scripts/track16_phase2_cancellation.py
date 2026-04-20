"""
R60 Track 16 — Phase 2: N-copy cancellation of the 2ω density.

Given Phase 1's finding that a single (1, 2) mode has charge
density ρ_Q(t) = 1/2 + (1/2)·cos(2ωt + χ) for some phase χ,
sum N identical copies at uniform phase offsets and ask: for
which N does the 2ω part vanish?

Closed-form answer.  The N copies at time offsets kT/N (k=0..N−1)
have 2ω phases differing by 4πk/N.  Their sum is

    S_2ω(N)  =  Σ_{k=0..N−1} exp(i · 4πk/N)

which is a geometric series: N when 4π/N is a multiple of 2π
(i.e. when N divides 2, i.e. N ∈ {1, 2}); 0 otherwise.

So N = 1 and N = 2 fail; N = 3 is the minimum cancelling N.

This matches 3-phase electrical power mathematics: 2-phase at
180° reinforces the 2ω pulsation rather than cancelling it;
2-phase at 90° is secretly 4-phase.  True minimum is N = 3.

Phase 2 proves this symbolically (sympy closed form) and verifies
it numerically on the model-F p-sheet (1, 2) mode frequency.

Sandboxed.
"""

import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np
import sympy as sp

from track1_solver import (
    mode_6_to_11, derive_L_ring, L_vector_from_params, mode_energy,
    PI, M_P_MEV,
)
from track7b_resolve import build_aug_metric
from track15_phase1_mass import K_MODELF, modelF_baseline


TWO_PI = 2 * PI


def main():
    print("=" * 72)
    print("R60 Track 16 — Phase 2: N-copy cancellation of the 2ω density")
    print("=" * 72)
    print()

    # ── Closed-form sum (sympy) ──
    print("─" * 72)
    print("  Closed-form analysis (sympy):")
    print("─" * 72)
    print()

    N, k, t, omega = sp.symbols("N k t omega", positive=True, integer=False)
    # single-mode charge density: ρ(t) = 1/2 + 1/2 cos(2 ω t)
    # copy-k density with time offset k·T/N = 2πk/(Nω):
    #   ρ_k(t) = 1/2 + 1/2 cos(2ω(t − 2πk/(Nω)))
    #         = 1/2 + 1/2 cos(2ωt − 4πk/N)
    # Sum S(t) = Σ_{k=0..N-1} ρ_k(t)
    # DC part: N/2
    # 2ω part: (1/2) Σ cos(2ωt − 4πk/N) = (1/2) Re[exp(i·2ωt) · Σ exp(-i·4πk/N)]
    # The geometric sum Σ_{k=0..N-1} exp(-i·4πk/N):
    #   = (1 − exp(-i·4π)) / (1 − exp(-i·4π/N))
    #   = 0   if 4π/N ∉ {0, 2π, 4π, ...}, i.e., N does not divide 2
    #   = N   if N ∈ {1, 2}

    print("  Claim: Σ_{k=0..N-1} exp(i·4πk/N) = N if N ∈ {1, 2}, else 0.")
    print()
    print(f"  {'N':>3s}    {'geometric sum':>20s}   {'|2ω amplitude|':>16s}")
    for Nv in range(1, 9):
        # geometric sum
        S = sum(sp.exp(sp.I * 4 * sp.pi * kk / Nv) for kk in range(Nv))
        S_simp = sp.simplify(S)
        abs_S = complex(sp.N(sp.Abs(S_simp)))
        # 2ω amplitude is |sum| / 2 divided by N (normalize per copy)
        amp = abs_S / 2.0
        print(f"  {Nv:>3d}    {str(S_simp):>20s}   {amp:>16.6f}")
    print()
    print("  → N = 1: amplitude 0.5 (full).  N = 2: amplitude 1.0 (reinforced!).")
    print("  → N = 3: amplitude 0 — minimum cancelling N.  N ≥ 3: amplitude 0.")
    print()
    print("  The N = 2 case is the critical subtlety: two identical modes")
    print("  at 180° time offset do NOT cancel, they DOUBLE the fluctuation.")
    print("  Hence pairs of (1, 2) quarks (diquarks) are not stable composites")
    print("  — a real-analog of QCD's 'no free diquarks'.")
    print()

    # ── Numerical verification at the (1, 2) frequency ──
    print("─" * 72)
    print("  Numerical verification on model-F p-sheet (1, 2) mode:")
    print("─" * 72)
    L_ring_p = derive_L_ring(M_P_MEV, 3, 6, 0.55, 0.162037, K_MODELF)
    p = modelF_baseline(L_ring_p=L_ring_p)
    G = build_aug_metric(p)
    L = L_vector_from_params(p)
    n12 = mode_6_to_11((0, 0, 0, 0, 1, 2))
    omega12 = mode_energy(G, L, n12)  # ω in MeV
    T12 = TWO_PI / omega12

    N_samples = 1024
    ts = np.linspace(0, T12, N_samples, endpoint=False)

    def rho_single(phase_offset):
        """ρ(t) = cos²(ωt − phase_offset·ω) for real field."""
        return np.cos(-omega12 * ts - phase_offset * omega12) ** 2

    def dft_2omega_amp(signal):
        fft = np.fft.rfft(signal)
        fft_amp = np.abs(fft) / N_samples * 2
        fft_amp[0] /= 2
        freqs = np.fft.rfftfreq(N_samples, ts[1] - ts[0])
        k2 = int(np.argmin(np.abs(freqs - 2 * omega12 / TWO_PI)))
        return fft_amp[k2]

    print()
    print(f"  {'N':>3s}   {'phase offsets':<38s}  "
          f"{'|2ω amp|':>12s}   {'cancel?':>8s}")
    for Nv in range(1, 9):
        offsets = [T12 * k / Nv for k in range(Nv)]
        total = np.zeros_like(ts)
        for off in offsets:
            total += rho_single(off)
        amp_2w = dft_2omega_amp(total)
        offsets_str = "[" + ", ".join(f"{o*omega12/TWO_PI:.3f}" for o in offsets) + "]"
        offsets_str = offsets_str[:38]  # truncate
        status = "YES" if abs(amp_2w) < 1e-6 else "NO"
        print(f"  {Nv:>3d}   {offsets_str:<38s}  {amp_2w:>12.6f}   {status:>8s}")
    print()

    # ── Key sanity checks ──
    print("─" * 72)
    print("  Subtleties and sanity checks:")
    print("─" * 72)
    print()

    # Check N=2 with 90° offset (Tesla's 2-phase)
    print("  Check: 2 copies at 90° offset (Tesla's 2-phase, not 180°)")
    offsets_90 = [0.0, T12 / 4]  # 90° time offset, or 180° at 2ω
    total_90 = rho_single(offsets_90[0]) + rho_single(offsets_90[1])
    amp_90 = dft_2omega_amp(total_90)
    print(f"    |2ω amp| = {amp_90:.6f}")
    print(f"  → 2-phase-90° cancels (it's secretly 4-phase at 2ω).")
    print(f"    This is why Tesla's early 2-phase worked for motors;")
    print(f"    the N = 2 failure case refers to the natural/anti-phase")
    print(f"    offset N·T/N = T (i.e., no offset), not the 90°/half-N offset.")
    print()

    # What about N = 3 at non-uniform offsets?
    print("  Check: 3 copies at irregular offsets (e.g., 0°, 50°, 200°)")
    offsets_irreg = [0.0, T12 * 50 / 360, T12 * 200 / 360]
    total_irreg = sum(rho_single(o) for o in offsets_irreg)
    amp_irreg = dft_2omega_amp(total_irreg)
    print(f"    |2ω amp| = {amp_irreg:.6f}")
    print(f"  → Irregular 3-copy offsets do NOT cancel cleanly.")
    print(f"    The cancellation requires uniform 2π/N spacing; Phase 3")
    print(f"    investigates why 120° is dynamically selected.")
    print()

    print("Phase 2 complete.")
    print()
    print("Key findings:")
    print("  (1) The 2ω density cancellation requires N copies at uniform")
    print("      phase offsets 2πk/N, with N not dividing 2.")
    print("  (2) Minimum cancelling N = 3.  N = 1 has full 2ω fluctuation;")
    print("      N = 2 DOUBLES it (not intuitive — 180° is constructive!).")
    print("  (3) The result matches the 3-phase power mathematics:")
    print("      3 phases at 120° are the minimum for constant")
    print("      instantaneous power.")
    print("  (4) Implication for MaSt: a single (1, 2) or pair of (1, 2)")
    print("      modes cannot form a stable composite; the minimum stable")
    print("      composite is 3 copies at 120° offsets — i.e., (3, 6) =")
    print("      three (1, 2) quarks bound at Z₃-symmetric phases.")


if __name__ == "__main__":
    main()
