"""
R64 Track 16 — Pool item v opening phase: quick scan of magnetic anomaly proxies.

Question: does σ_pS_tube + H2 activation (and/or other sheet activations)
shift the metric quantities that determine magnetic-moment coupling, in
ways and magnitudes consistent with observed g-2 anomalies?

Method (proxy-level, no full derivation yet):
  1. Identify the metric quantity that determines magnetic coupling for
     each particle.  Analogous to α-Coulomb's `G⁻¹[X_TUBE, t]`, the
     magnetic coupling for sheet X is `G⁻¹[X_TUBE, S_x]` — the
     direct projection of the particle's tube sector onto the spatial
     direction.
  2. Compute baseline (no σ_xS activation) values.
  3. Sweep σ_pS_tube and σ_eS_tube at moderate values (well inside
     signature band, NOT at edge).
  4. For each particle (electron, muon, proton, neutron, single u, d):
     compute the relevant G⁻¹ shift; convert to dimensionless ratio
     against α-baseline; compare to observed a_e, a_p.
  5. Report whether shifts are in the right ballpark.

If the proxies show shifts of order a_e (10⁻³) for electron and order
a_p (1) for proton at moderate σ_pS_tube, the architecture is plausible
and warrants a full derivation.  If shifts are tiny or wrong-direction,
σ_pS_tube isn't the source of g-2 anomalies and we look elsewhere.
"""

import math
import csv
from pathlib import Path

import sys
import numpy as np

R60_SCRIPTS = Path(__file__).resolve().parent.parent.parent / "R60-metric-11" / "scripts"
sys.path.insert(0, str(R60_SCRIPTS))

from track1_solver import (    # noqa: E402
    signature_ok, ALPHA, SQRT_ALPHA, FOUR_PI, MA_SLICE,
    I_E_TUBE, I_E_RING, I_P_TUBE, I_P_RING, I_NU_TUBE, I_NU_RING,
    I_ALEPH, I_SX, I_SY, I_SZ, I_T,
)
from track7b_resolve import build_aug_metric    # noqa: E402
from track10_hadron_inventory import track9_params    # noqa: E402


# H2 coefficients per sheet (derived in Phase 11d analog)
H2_P = -1.818920
H2_E = +1.818920    # opposite sign because sign_e = +1


# Reference observables
A_E_OBS = 1.159652e-3   # electron anomalous moment
A_P_OBS = 1.7928        # proton anomalous moment (huge)
A_MU_OBS = 1.165921e-3  # muon anomalous moment
ANOMALY_TARGET_QED = ALPHA / (2 * math.pi)   # one-loop QED prediction


def build_with_pS(p, sigma_p, sigma_e):
    """Activate σ_pS_tube + p-H2 AND σ_eS_tube + e-H2."""
    G = build_aug_metric(p).copy()
    sigma_aS = H2_P * sigma_p + H2_E * sigma_e
    for s_idx in (I_SX, I_SY, I_SZ):
        G[I_P_TUBE, s_idx] += sigma_p
        G[s_idx, I_P_TUBE] += sigma_p
        G[I_E_TUBE, s_idx] += sigma_e
        G[s_idx, I_E_TUBE] += sigma_e
        G[I_ALEPH, s_idx] += sigma_aS
        G[s_idx, I_ALEPH] += sigma_aS
    return G


def magnetic_proxy(G, idx_tube):
    """
    Magnetic-coupling proxy for a particle whose tube sector lives at
    `idx_tube`: G⁻¹[idx_tube, I_SX] (the Schur projection onto S spatial).
    Analogous to G⁻¹[idx_tube, I_T] for Coulomb.

    Sign and magnitude depend on metric details; this returns the raw
    inverse-metric entry.
    """
    G_inv = np.linalg.inv(G)
    return float(G_inv[idx_tube, I_SX])


def magnetic_anomaly_ratio(G, G_baseline, idx_tube):
    """
    Anomaly proxy = (magnetic_coupling(G) - magnetic_coupling(baseline))
                    / (sqrt(α) reference scale)
    The √α scale is suggestive (it's σ_ta's natural scale); other
    normalizations possible.
    """
    delta = magnetic_proxy(G, idx_tube) - magnetic_proxy(G_baseline, idx_tube)
    return delta / SQRT_ALPHA


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 100)
    print("R64 Track 16 — Pool item v opening phase: magnetic anomaly proxy scan")
    print("=" * 100)
    print()
    print("  Reference observables:")
    print(f"    a_e (electron) = {A_E_OBS:.4e}    (~α/(2π) = {ANOMALY_TARGET_QED:.4e})")
    print(f"    a_μ (muon)     = {A_MU_OBS:.4e}")
    print(f"    a_p (proton)   = {A_P_OBS:+.4f}")
    print()
    print("  α/(2π) = QED one-loop magnetic anomaly target")
    print()

    # Use Point A (the calibration point we trust most)
    p = track9_params().copy_with(eps_p=0.07309, s_p=0.19387)

    # Baseline (no σ_pS activation)
    G_baseline = build_with_pS(p, 0.0, 0.0)
    print("=" * 100)
    print("Step 1: Baseline G⁻¹[X_TUBE, S_x] entries (no activation)")
    print("=" * 100)
    print()
    print(f"  {'particle':<12s}  {'G⁻¹[X_TUBE, S_x]':>20s}  {'value/√α':>12s}")
    for label, idx in [('electron', I_E_TUBE),
                       ('muon (e-sheet)', I_E_TUBE),
                       ('ν (ν-sheet tube)', I_NU_TUBE),
                       ('proton', I_P_TUBE),
                       ('neutron', I_P_TUBE)]:
        val = magnetic_proxy(G_baseline, idx)
        print(f"  {label:<12s}  {val:>+20.6e}  {val/SQRT_ALPHA:>+12.6f}")
    print()

    # ── Step 2: sweep σ_pS_tube (proton-sheet activation) ───────────
    print("=" * 100)
    print("Step 2: Sweep σ_pS_tube (proton activation), watch proton's magnetic proxy")
    print("=" * 100)
    print()
    sigma_p_vals = [0.001, 0.005, 0.01, 0.025, 0.05, 0.075, 0.10, 0.115, 0.124, 0.12505]
    print(f"  {'σ_pS_tube':>10s}  {'sig OK':>7s}  {'G⁻¹[p_t, S_x]':>14s}  "
          f"{'shift / √α':>12s}  {'compare to a_p={:+.4f}':>22s}".format(A_P_OBS))
    print("  " + "─" * 80)
    rows_p = []
    for s in sigma_p_vals:
        G = build_with_pS(p, -s, 0.0)   # negative for attractive
        ok = signature_ok(G)
        if not ok:
            print(f"  {s:>10.5f}  {'NO':>7s}")
            continue
        proxy = magnetic_proxy(G, I_P_TUBE)
        ratio = magnetic_anomaly_ratio(G, G_baseline, I_P_TUBE)
        match = abs(ratio / A_P_OBS) if A_P_OBS != 0 else float('nan')
        print(f"  {s:>10.5f}  {'YES':>7s}  {proxy:>+14.4e}  {ratio:>+12.6f}  "
              f"({match:.3f}× a_p)")
        rows_p.append({
            "sigma_pS_tube": s,
            "G_inv_pt_Sx": proxy,
            "ratio_over_sqrt_alpha": ratio,
        })
    print()

    # ── Step 3: sweep σ_eS_tube (electron-sheet activation) ─────────
    print("=" * 100)
    print("Step 3: Sweep σ_eS_tube (electron activation), watch electron's magnetic proxy")
    print("=" * 100)
    print()
    # e-sheet edge was at 0.000150, so use much smaller values
    sigma_e_vals = [1e-7, 1e-6, 1e-5, 1e-4, 1.4e-4, 1.5e-4]
    print(f"  {'σ_eS_tube':>12s}  {'sig OK':>7s}  {'G⁻¹[e_t, S_x]':>14s}  "
          f"{'shift / √α':>12s}  {'compare to a_e={:.3e}':>22s}".format(A_E_OBS))
    print("  " + "─" * 90)
    for s in sigma_e_vals:
        G = build_with_pS(p, 0.0, -s)   # negative for attractive
        ok = signature_ok(G)
        if not ok:
            print(f"  {s:>12.6f}  {'NO':>7s}")
            continue
        proxy = magnetic_proxy(G, I_E_TUBE)
        ratio = magnetic_anomaly_ratio(G, G_baseline, I_E_TUBE)
        match = abs(ratio / A_E_OBS) if A_E_OBS != 0 else float('nan')
        print(f"  {s:>12.6e}  {'YES':>7s}  {proxy:>+14.4e}  {ratio:>+12.4e}  "
              f"({match:.3f}× a_e)")
    print()

    # ── Step 4: cross-effects (does σ_pS_tube affect electron's proxy?) ─
    print("=" * 100)
    print("Step 4: Cross-effect — does σ_pS_tube activation affect the *electron's* magnetic proxy?")
    print("=" * 100)
    print()
    print("  This tests whether p-sheet activation propagates via aleph to e-sheet.")
    print()
    print(f"  {'σ_pS_tube':>10s}  {'σ_eS_tube':>10s}  "
          f"{'G⁻¹[e_t, S_x]':>14s}  {'shift / √α':>12s}")
    print("  " + "─" * 60)
    for s_p in [0.0, 0.01, 0.05, 0.10]:
        G = build_with_pS(p, -s_p, 0.0)
        if signature_ok(G):
            proxy = magnetic_proxy(G, I_E_TUBE)
            ratio = (proxy - magnetic_proxy(G_baseline, I_E_TUBE)) / SQRT_ALPHA
            print(f"  {s_p:>+10.5f}  {0.0:>+10.5f}  {proxy:>+14.4e}  "
                  f"{ratio:>+12.6f}")
    print()

    # ── Step 5: cross-effects — σ_eS_tube on proton's proxy ─────────
    print("=" * 100)
    print("Step 5: Cross-effect — does σ_eS_tube activation affect the *proton's* magnetic proxy?")
    print("=" * 100)
    print()
    for s_e in [0.0, 1e-5, 5e-5, 1e-4]:
        G = build_with_pS(p, 0.0, -s_e)
        if signature_ok(G):
            proxy = magnetic_proxy(G, I_P_TUBE)
            ratio = (proxy - magnetic_proxy(G_baseline, I_P_TUBE)) / SQRT_ALPHA
            print(f"  {0.0:>+10.5f}  {s_e:>+10.7f}  {proxy:>+14.4e}  "
                  f"{ratio:>+12.6f}")
    print()

    # ── Verdict ─────────────────────────────────────────────────────
    print("=" * 100)
    print("VERDICT — pool item v opening scan")
    print("=" * 100)
    print()
    print("  Question: do metric activations shift quantities at the right magnitudes")
    print("            for observed g-2 anomalies?")
    print()
    print("  Key observation: the proxy ratios in Steps 2 and 3 should be dimensionless")
    print("  shifts; if they reach order 1 for the proton (matching a_p ≈ 1.79) and")
    print("  order 10⁻³ for the electron (matching a_e ≈ 0.00116), the architecture")
    print("  is plausible and a full derivation is warranted.")
    print()
    print("  If proxies are far smaller (order 10⁻⁹ for proton at moderate σ), then the")
    print("  metric mechanism doesn't produce QED-scale anomalies and we look elsewhere.")
    print()


if __name__ == "__main__":
    main()
