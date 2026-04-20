"""
R60 Track 18 — Phase 1: Conjugate-pair structure on ν-sheet.

Test whether the ν-sheet's low-ε geometry naturally produces
near-degenerate pairs of (n_t, n_r) and (−n_t, n_r) modes.
If every observable state is such a superposition, the net
tube-winding vanishes and the tube-charge contribution does
too — giving electrical neutrality as a structural consequence
rather than a definitional choice.

Closed form.  For a sheet mode (n_t, n_r) on (ε, s):

    μ²(n_t, n_r)   =  (n_t/ε)² + (n_r − n_t s)²
    μ²(−n_t, n_r)  =  (n_t/ε)² + (n_r + n_t s)²

Their split:

    Δμ²  =  μ²(+) − μ²(−)  =  (n_r − n_t s)² − (n_r + n_t s)²
         =  −4 n_r n_t s

So the conjugate pair is split by an amount proportional to
n_r · n_t · s.  At small s (like s_ν = 0.022), the split is
small; conjugate partners are near-degenerate.  Small ε_ν
amplifies the EFFECT by pushing the (n_t/ε)² term up relative
to the split, so the RELATIVE split (fraction of total μ)
decreases.

Sandboxed.
"""

import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np

from track1_solver import (
    mu_sheet, PI,
)


def conjugate_split_fraction(n_t, n_r, eps, s):
    """Return |μ(+) − μ(−)| / ((μ(+) + μ(−)) / 2) — the relative
    split between a mode and its tube-conjugate."""
    if n_t == 0 or n_r == 0:
        return 0.0  # trivially degenerate
    mu_plus = mu_sheet(n_t, n_r, eps, s)
    mu_minus = mu_sheet(-n_t, n_r, eps, s)
    avg = 0.5 * (mu_plus + mu_minus)
    return abs(mu_plus - mu_minus) / avg if avg > 0 else 0.0


def enumerate_modes(eps, s, N_max=5):
    """Return sorted list of (μ, n_t, n_r) with |n_t|, |n_r| ≤ N_max
    and (n_t, n_r) ≠ (0, 0)."""
    modes = []
    for n_t in range(-N_max, N_max + 1):
        for n_r in range(-N_max, N_max + 1):
            if n_t == 0 and n_r == 0:
                continue
            mu = mu_sheet(n_t, n_r, eps, s)
            modes.append((mu, n_t, n_r))
    modes.sort()
    return modes


def main():
    print("=" * 82)
    print("R60 Track 18 — Phase 1: conjugate-pair structure vs ε_ν")
    print("=" * 82)
    print()
    print("  Closed form: |μ²(+) − μ²(−)| = 4 |n_r n_t s|")
    print("  At s_ν = 0.022 (oscillation-constrained), the split is")
    print("  0.088 · n_r · n_t per unit (n_r n_t).")
    print()

    # ── Scan ε_ν at fixed s_ν = 0.022 ──
    s_NU = 0.022
    eps_values = [0.01, 0.05, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 50.0]

    print("─" * 82)
    print("  Mean relative conjugate-pair split, scanning ε_ν at s_ν = 0.022:")
    print("─" * 82)
    print()
    print("  For each ε_ν, enumerate the 10 lightest (n_t, n_r) modes with")
    print("  n_t > 0 and compute the relative split |μ(+n_t) − μ(−n_t)| / μ̄.")
    print("  A small mean split means the conjugate pairs are near-degenerate")
    print("  and charge cancellation via pair-superposition is supported.")
    print()
    print(f"  {'ε_ν':>8s}  {'mean rel split':>16s}  {'max rel split':>16s}  "
          f"{'lightest mode Δ':>16s}")
    print("  " + "-" * 78)

    for eps in eps_values:
        modes = enumerate_modes(eps, s_NU, N_max=5)
        # Keep only modes with n_t > 0 (half the spectrum; each is one of the pair)
        mode_pos = [(mu, n_t, n_r) for (mu, n_t, n_r) in modes if n_t > 0]
        # Top 10 lightest
        mode_pos = mode_pos[:10]
        if not mode_pos:
            continue
        rel_splits = [conjugate_split_fraction(n_t, n_r, eps, s_NU)
                      for (_, n_t, n_r) in mode_pos]
        mean_rel = np.mean(rel_splits)
        max_rel = max(rel_splits)
        light_mu, light_nt, light_nr = mode_pos[0]
        light_split = conjugate_split_fraction(light_nt, light_nr, eps, s_NU)
        print(f"  {eps:>8.3f}  {mean_rel:>16.6e}  {max_rel:>16.6e}  "
              f"{light_split:>16.6e}")
    print()

    # ── Detailed table for current model-F ν-sheet ──
    print("─" * 82)
    print("  Detailed pair structure at current model-F ν-sheet (ε_ν = 2):")
    print("─" * 82)
    print()
    print(f"  {'n_t':>4s}  {'n_r':>4s}  {'μ(+n_t)':>12s}  {'μ(−n_t)':>12s}  "
          f"{'Δμ':>12s}  {'Δμ/μ̄':>12s}")
    print("  " + "-" * 78)
    eps_modelF = 2.0
    modes = enumerate_modes(eps_modelF, s_NU, N_max=3)
    mode_pos = [(mu, n_t, n_r) for (mu, n_t, n_r) in modes if n_t > 0]
    for mu, n_t, n_r in mode_pos[:10]:
        mu_plus = mu_sheet(n_t, n_r, eps_modelF, s_NU)
        mu_minus = mu_sheet(-n_t, n_r, eps_modelF, s_NU)
        avg = 0.5 * (mu_plus + mu_minus)
        dmu = abs(mu_plus - mu_minus)
        rel = dmu / avg if avg > 0 else 0.0
        print(f"  {n_t:>+4d}  {n_r:>+4d}  {mu_plus:>12.6f}  {mu_minus:>12.6f}  "
              f"{dmu:>12.6e}  {rel:>12.6e}")
    print()

    # ── Same table for small ε_ν ──
    print("─" * 82)
    print("  Detailed pair structure at small ε_ν = 0.1:")
    print("─" * 82)
    print()
    print(f"  {'n_t':>4s}  {'n_r':>4s}  {'μ(+n_t)':>12s}  {'μ(−n_t)':>12s}  "
          f"{'Δμ':>12s}  {'Δμ/μ̄':>12s}")
    print("  " + "-" * 78)
    eps_small = 0.1
    modes = enumerate_modes(eps_small, s_NU, N_max=3)
    mode_pos = [(mu, n_t, n_r) for (mu, n_t, n_r) in modes if n_t > 0]
    for mu, n_t, n_r in mode_pos[:10]:
        mu_plus = mu_sheet(n_t, n_r, eps_small, s_NU)
        mu_minus = mu_sheet(-n_t, n_r, eps_small, s_NU)
        avg = 0.5 * (mu_plus + mu_minus)
        dmu = abs(mu_plus - mu_minus)
        rel = dmu / avg if avg > 0 else 0.0
        print(f"  {n_t:>+4d}  {n_r:>+4d}  {mu_plus:>12.6f}  {mu_minus:>12.6f}  "
              f"{dmu:>12.6e}  {rel:>12.6e}")
    print()

    # ── Interpretation ──
    print("─" * 82)
    print("  Physical reading:")
    print("─" * 82)
    print()
    print("  The absolute split Δμ² = 4 |n_r n_t| · s is independent of ε.")
    print("  So conjugate pairs are ABSOLUTELY split by the same amount on")
    print("  every ν-sheet geometry at fixed s_ν.")
    print()
    print("  The RELATIVE split Δμ/μ̄ depends on ε through μ̄.  Small ε")
    print("  makes μ̄ large (via the (n_t/ε)² term), so the relative split")
    print("  SHRINKS:")
    print()
    print("    At ε_ν = 2   (model-F current):  relative split ~ 1–5% for")
    print("                                     low (n_t, n_r) pairs")
    print("    At ε_ν = 0.1 (hypothetical):     relative split ~ 0.01–0.05%")
    print("    At ε_ν = 0.01:                   relative split ~ 10⁻⁶")
    print()
    print("  If 'pair superposition via near-degeneracy' is the mechanism")
    print("  by which ν-sheet modes appear charge-neutral, then SMALL ε_ν")
    print("  makes this mechanism increasingly effective.  The ν-sheet's")
    print("  natural preference for small ε may be driven by this requirement:")
    print()
    print("    Just as the e-sheet's geometry optimizes for spin-½ free")
    print("    propagation via extreme ε AND magic shear (Track 17), the")
    print("    ν-sheet's geometry may optimize for charge-zero appearance")
    print("    via small ε, by making conjugate-pair near-degeneracy")
    print("    dominate over any single tube-winding mode.")
    print()
    print("  CAVEAT.  The absolute split is the same on any (ε, s_ν) pair.")
    print("  Small ε makes the relative split small, but doesn't make the")
    print("  pair PERFECTLY degenerate.  A mechanism that FORCES the")
    print("  observable ν state to be the pair-superposition (rather than")
    print("  the individual + or − tube-winding components) is still")
    print("  required.  Candidates:")
    print("    - Lorentz invariance forces (n_t, n_r) and (−n_t, n_r) to")
    print("      appear as complex conjugates of the same real excitation")
    print("    - CPT symmetry forces charge conjugation partners to coexist")
    print("    - The ν-sheet's macroscopic L_ring means any localized")
    print("      tube-winding has mass ≈ ring-scale · quantum anyway")
    print()
    print("  Phase 4 examines which mechanism is preferred.")
    print()

    # ── Final summary ──
    print("─" * 82)
    print("  Comparison: e, p, ν sheet conjugate-pair structure:")
    print("─" * 82)
    print()
    print(f"  {'Sheet':<10s}  {'ε':>8s}  {'s':>8s}  {'rel split (1,1)':>16s}  "
          f"{'rel split (1,2)':>16s}")
    print("  " + "-" * 70)
    sheets_full = [
        ("electron", 397.074, 2.004200),
        ("proton",   0.55,    0.162037),
        ("neutrino", 2.0,     s_NU),
        ("ν small ε", 0.1,    s_NU),
    ]
    for label, eps, s in sheets_full:
        split_11 = conjugate_split_fraction(1, 1, eps, s)
        split_12 = conjugate_split_fraction(1, 2, eps, s)
        print(f"  {label:<10s}  {eps:>8.3f}  {s:>8.4f}  "
              f"{split_11:>16.6e}  {split_12:>16.6e}")
    print()
    print("  Observations:")
    print("    • e-sheet has LARGE relative split (s ≈ 2 is huge) — conjugate")
    print("      pairs clearly distinct.  Single-mode + and − are observably")
    print("      different.  Electron and positron are distinct charges.")
    print("    • p-sheet has moderate-large split — pairs are distinguishable.")
    print("      Proton and antiproton are distinct.")
    print("    • ν-sheet (model-F) has SMALL split — pairs nearly degenerate.")
    print("    • ν-sheet at small ε — pairs effectively degenerate.")
    print()

    print("Phase 1 complete.")
    print()
    print("Key findings:")
    print("  (1) Conjugate-pair absolute split Δμ² = 4|n_r n_t| s is the")
    print("      SAME for any ε_ν at fixed s_ν. It's a constant of the")
    print("      sheet shear alone.")
    print("  (2) Relative split Δμ/μ̄ shrinks at small ε_ν because μ̄ grows.")
    print("      At ε_ν = 0.1, relative split is ~0.01% for light modes.")
    print("  (3) The ν-sheet at s_ν = 0.022 has conjugate pairs that are")
    print("      1–5% split at model-F's current ε_ν = 2 — already close")
    print("      to degeneracy, but not at the 'both always present' limit.")
    print("  (4) A physical mechanism (CPT, Lorentz invariance, ν-sheet")
    print("      macroscopic topology) is still needed to force the")
    print("      observable state to be the pair-superposition rather than")
    print("      the individual ± components.  Phase 4 investigates.")


if __name__ == "__main__":
    main()
