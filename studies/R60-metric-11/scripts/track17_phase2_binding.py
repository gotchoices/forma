"""
R60 Track 17 — Phase 2: Binding energy threshold map.

Phase 1 established that Z₃ binding activates when the (1, 2)
mode is localized on the sheet (R_loc = m_mode × L_ring / ℏc > 1)
and that the same ratio gives the Z₃-to-Coulomb energy comparison.

Phase 2 produces a map of R_loc across the (ε, s) plane,
identifies the threshold contour R_loc = 1, and places the three
sheets on it.

For each (ε, s), the (1, 2) mode on a sheet with diagonal scale
k has:

    μ(1, 2, ε, s)  =  √((1/ε)² + (2 − s)²)
    E_mode         =  2π ℏc · μ / (L_ring · √k)
    R_loc          =  E_mode · L_ring / ℏc
                   =  2π · μ / √k

So R_loc is ∝ μ, independent of the L_ring calibration — it
depends only on the dimensionless mode number μ and the diagonal
scale k.  With k_modelF = 1.1803/(8π) = 4.696 × 10⁻²,

    R_loc(ε, s)  =  2π · μ(1, 2, ε, s) / √k_modelF
                =  28.96 · μ(1, 2, ε, s)

Threshold R_loc = 1 corresponds to μ ≈ 0.0345.  Sheets with
μ(1, 2) > 0.0345 have confinement; sheets below are exempt.

Sandboxed.
"""

import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np

from track1_solver import (
    mu_sheet, PI, HBAR_C_MEV_FM,
)


K_MODELF = 4.696442e-02
R_LOC_SCALE = 2 * PI / math.sqrt(K_MODELF)  # ≈ 28.96


def R_loc_from_geom(eps, s, target_ratio_nt=1, target_ratio_nr=2):
    """R_loc for the (n_t, n_r) mode on this sheet, with L_ring
    calibrated to make the mode hit the target mass.

    R_loc is independent of the target mass — depends only on μ
    and k."""
    mu = mu_sheet(target_ratio_nt, target_ratio_nr, eps, s)
    return R_LOC_SCALE * mu


def main():
    print("=" * 84)
    print("R60 Track 17 — Phase 2: binding threshold map R_loc(ε, s)")
    print("=" * 84)
    print()
    print("  R_loc = m_mode · L_ring / ℏc = 2π · μ(1, 2, ε, s) / √k_modelF")
    print(f"  R_loc scale constant:  2π / √k_modelF = {R_LOC_SCALE:.4f}")
    print(f"  Confinement threshold: R_loc > 1  ⟺  μ > {1.0/R_LOC_SCALE:.4f}")
    print()

    # ── The three sheets ──
    sheets = [
        ("electron", 397.074, 2.004200),
        ("proton",   0.55,    0.162037),
        ("neutrino", 2.0,     0.022),
    ]

    print("─" * 84)
    print("  Three sheets:")
    print("─" * 84)
    for label, eps, s in sheets:
        R = R_loc_from_geom(eps, s)
        status = "CONFINED (Z₃ active)" if R > 10 else (
                 "MARGINAL" if R > 1 else
                 "EXEMPT (no Z₃)")
        print(f"    {label:<10s}  (ε={eps:>10.4f}, s={s:>9.4f})  "
              f"R_loc = {R:>10.4f}  → {status}")
    print()

    # ── Full (ε, s) map ──
    print("─" * 84)
    print("  R_loc(ε, s) map with threshold labels:")
    print("─" * 84)
    print()
    print("  Symbols:  ·  R_loc < 0.1 (strongly exempt)")
    print("            .  R_loc < 1   (exempt)")
    print("            :  R_loc < 10  (marginal)")
    print("            +  R_loc < 100 (moderate binding)")
    print("            #  R_loc ≥ 100 (strong binding)")
    print()

    eps_values = [0.1, 0.3, 0.55, 1.0, 2.0, 5.0, 20.0, 100.0, 397.0, 1000.0]
    s_values = []
    for s in np.arange(0.0, 3.01, 0.1):
        s_values.append(round(s, 2))

    def symbol(R):
        if R < 0.1: return "·"
        elif R < 1: return "."
        elif R < 10: return ":"
        elif R < 100: return "+"
        else: return "#"

    # Print header
    print(f"  {'s':>6s}", end="")
    for eps in eps_values:
        print(f"  {eps:>7.2f}", end="")
    print()
    for s in s_values:
        print(f"  {s:>6.2f}", end="")
        for eps in eps_values:
            R = R_loc_from_geom(eps, s)
            sym = symbol(R)
            print(f"  {sym:>5s}{R:>2.0f}" if R < 100 else f"  {sym:>5s}{min(R, 999):>2.0f}", end="")
        print()
    print()

    # ── Critical ray s = 2 (magic shear for (1, 2)) ──
    print("─" * 84)
    print("  The critical ray s = 2 (magic shear for the (1, 2) mode):")
    print("─" * 84)
    print()
    print("  At s = 2 exactly, μ(1, 2, ε, 2) = 1/ε.  R_loc = 2π / (ε √k_modelF).")
    print("  Confinement fails when 1/ε < 1/R_LOC_SCALE, i.e., when ε > R_LOC_SCALE ≈ 29.")
    print()
    print(f"  {'ε at s = 2':>12s}  {'μ(1, 2)':>10s}  {'R_loc':>10s}  {'confinement?'}")
    print("  " + "-" * 70)
    for eps in [0.1, 0.3, 0.55, 1.0, 2.0, 5.0, 20.0, 28.96, 50.0, 100.0, 397.0, 1000.0]:
        mu = mu_sheet(1, 2, eps, 2.0)
        R = R_LOC_SCALE * mu
        status = "confined" if R > 1 else "EXEMPT"
        print(f"  {eps:>12.4f}  {mu:>10.6f}  {R:>10.4f}  {status}")
    print()
    print("  Observation: at exact magic shear s = 2, confinement survives")
    print("  for any ε ≲ 29.  Beyond ε ≈ 29 the mode becomes delocalized.")
    print()
    print("  The e-sheet sits at ε = 397 — well beyond the threshold.")
    print("  The electron's extreme ε is what places it in the exempt region.")
    print()

    # ── Position of each sheet on a finer scan ──
    print("─" * 84)
    print("  Fine scan near each sheet's position:")
    print("─" * 84)
    print()

    for label, eps0, s0 in sheets:
        print(f"  {label} neighborhood (ε₀={eps0}, s₀={s0}):")
        # Vary ε and s by factor of 2 around the sheet's position
        # unless we're near s = 2 (take narrower s range)
        ds_range = 0.05 if abs(s0 - 2.0) < 0.1 else 0.2
        eps_range = [eps0 * 0.5, eps0, eps0 * 2]
        s_range = [s0 - ds_range, s0, s0 + ds_range]

        print(f"    {'':>8s}", end="")
        for eps in eps_range:
            print(f"  {'ε='+f'{eps:>8.4f}':>14s}", end="")
        print()
        for s in s_range:
            print(f"    s={s:>6.4f}", end="")
            for eps in eps_range:
                R = R_loc_from_geom(eps, s)
                print(f"  R={R:>10.4f}", end="")
            print()
        print()

    # ── Summary: which regions of (ε, s) give confinement ──
    print("─" * 84)
    print("  Phase diagram summary:")
    print("─" * 84)
    print()
    print("  CONFINED region (R_loc > 1):  any (ε, s) with μ(1, 2) > 0.0345.")
    print("  Equivalently: (1/ε)² + (2−s)² > 0.00119.")
    print()
    print("  This is the COMPLEMENT of a small elliptical region near the")
    print("  point (ε → ∞, s = 2) — the magic-shear limit at large ε.")
    print()
    print("  EXEMPT region (R_loc < 1): small ellipse around (ε → ∞, s = 2).")
    print("  Parametrically: need both")
    print("      ε > 29       AND      |s − 2| < 0.0345")
    print("  (approximate product form; exact boundary is elliptical).")
    print()
    print("  The e-sheet at (ε = 397, s = 2.004) is WELL INSIDE the exempt")
    print("  ellipse: 1/ε = 0.0025, |s − 2| = 0.004.  Both are below 0.035.")
    print()
    print("  The p-sheet at (ε = 0.55, s = 0.162) is VERY FAR OUTSIDE:")
    print("  1/ε = 1.82 (well above threshold), |s − 2| = 1.84.")
    print()
    print("  The ν-sheet at (ε = 2, s = 0.022) is ALSO FAR OUTSIDE:")
    print("  1/ε = 0.5, |s − 2| = 1.98.")
    print()
    print("  The e-sheet is the ONLY sheet in the exempt region.  This is")
    print("  a STRUCTURAL feature of model-F's geometry, not an accident.")
    print()

    # ── Self-consistency observation ──
    print("─" * 84)
    print("  Self-consistency observation:")
    print("─" * 84)
    print()
    print("  The e-sheet's parameters (ε = 397, s = 2.004) were chosen in")
    print("  R53 to place (1, 2) at the generation resonance — a specific")
    print("  dynamical stability condition.  R60 Track 9 confirmed that")
    print("  this extreme geometry is required for model-E's mass spectrum.")
    print()
    print("  Track 17 now reveals a SECOND reason this geometry is correct:")
    print("  it places (1, 2) in the Z₃-exempt region of (ε, s) space, so")
    print("  the electron propagates as a single free mode without being")
    print("  confined into a (3, 6) composite.")
    print()
    print("  The two requirements — generation resonance and Z₃ exemption —")
    print("  are independently derived but land on the SAME (ε, s) neighborhood.")
    print("  This suggests the e-sheet's 'extreme' geometry is a self-")
    print("  consistency point where multiple physical conditions coincide:")
    print()
    print("    1. Mass scale: (1, 2) at 0.511 MeV (R53 Solution D)")
    print("    2. Generation resonance: (1, 2) ghost-suppressed (R53)")
    print("    3. Z₃ exemption: (1, 2) observable as free single mode (Track 17)")
    print()
    print("  This is a strong coherence argument for the e-sheet geometry.")
    print()

    print("Phase 2 complete.")
    print()
    print("Key findings:")
    print("  (1) R_loc = 2π μ / √k_modelF is the unified confinement threshold.")
    print("  (2) The exempt region (R_loc < 1) is a small elliptical neighborhood")
    print("      of (ε → ∞, s = 2) in the (ε, s) plane.")
    print("  (3) Only the e-sheet sits in the exempt region; p and ν are far outside.")
    print("  (4) The e-sheet's extreme geometry — independently required by R53")
    print("      generation resonance and model-E mass calibration — ALSO places")
    print("      it at the Z₃-exempt point.  This is a self-consistency win, not")
    print("      a coincidence.")
    print("  (5) ν-sheet is NOT in the exempt region.  Track 18 must address")
    print("      whether ν modes form Z₃ composites (composite picture) or")
    print("      whether some other mechanism prevents ν confinement (e.g.,")
    print("      ν neutrality killing the Coulomb repulsion that three ν-quarks")
    print("      would otherwise face).")


if __name__ == "__main__":
    main()
