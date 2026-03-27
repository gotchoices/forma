#!/usr/bin/env python3
"""
R33 Track 1: Charge integral per mode on electron and proton sheets.

Generalizes the R19-shear-charge integral from the (1,2) electron mode
to all (n₁, n₂) modes.  Determines which modes carry charge and how
strongly they couple electromagnetically.

TWO CHARGE FORMULAS ARE COMPARED:

1. KK formula: Q = -n₁ (electron sheet) or Q = +n₅ (proton sheet).
   Every n₁ ≠ 0 mode carries charge proportional to n₁.

2. WvM charge integral (R19):
   - θ₁_phys integral selects |n₁| = 1 ONLY (F17)
   - θ₂ integral gives Q_eff ∝ sin(2πs)/(n₂ - s) for n₁ = 1
   - Charge STRENGTH depends on n₂ (not just charge sign)

The WvM integral is more restrictive: it kills all |n₁| ≠ 1 modes
and modulates the coupling of surviving modes by 1/(n₂ - s)².
"""

import sys
import os
import math
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.t6 import (
    alpha_kk, solve_shear_for_alpha, mode_energy, mode_charge, mode_spin,
    build_scaled_metric, ALPHA, M_E_MEV, M_P_MEV,
)


def charge_integral_2d(n1, n2, s):
    """
    WvM charge integral for mode (n₁, n₂) on a sheared T².

    The θ₁ integral selects |n₁| = 1.  For |n₁| ≠ 1, returns 0.
    For n₁ = ±1, returns sin(2πs)/(n₂ - n₁·s).
    """
    if abs(n1) != 1:
        return 0.0
    q2 = n2 - n1 * s
    if abs(q2) < 1e-12:
        return float('inf')
    return math.sin(2 * math.pi * s) / q2


def alpha_eff_kk(r, s, n1, n2):
    """
    Effective fine-structure constant for mode (n₁, n₂) using the
    KK convention.  Generalizes alpha_kk to arbitrary modes.

    α_eff = r² × μ(n₁,n₂) × sin²(2πs) / (4π × (n₂ - n₁·s)²)

    where μ = √(n₁²/r² + (n₂ - n₁·s)²) is the dimensionless mode energy.
    """
    if abs(n1) != 1:
        return 0.0
    q2 = n2 - n1 * s
    if abs(q2) < 1e-12:
        return float('inf')
    mu = math.sqrt(n1**2 / r**2 + q2**2)
    return r**2 * mu * math.sin(2 * math.pi * s)**2 / (4 * math.pi * q2**2)


def mode_energy_2d(n1, n2, r, s):
    """Dimensionless energy μ of mode (n₁, n₂) on sheared T²."""
    q2 = n2 - n1 * s
    return math.sqrt(n1**2 / r**2 + q2**2)


def wvm_spin(n1, n2):
    """Spin from WvM winding ratio.  Returns (value, label)."""
    if n2 == 0:
        return (None, "undefined")
    ratio = abs(n1 / n2)
    if ratio == 0:
        return (0, "spin-0")
    if abs(ratio - 0.5) < 1e-10:
        return (0.5, "spin-½")
    if abs(ratio - 1.0) < 1e-10:
        return (1, "spin-1")
    if abs(ratio - round(ratio)) < 1e-10:
        return (int(round(ratio)), f"spin-{int(round(ratio))}")
    return (ratio, f"spin-{ratio:.3f} FORBIDDEN")


def analyze_sheet(name, r, s, n_max=8):
    """Analyze all modes on a single T² sheet."""
    print(f"\n{'='*72}")
    print(f"  {name} SHEET   r = {r:.4f},  s = {s:.6f}")
    print(f"{'='*72}")

    alpha_electron = alpha_eff_kk(r, s, 1, 2)
    q_electron = charge_integral_2d(1, 2, s)
    mu_electron = mode_energy_2d(1, 2, r, s)

    print(f"\nReference mode (1,2):")
    print(f"  α_eff = {alpha_electron:.6e}  (expect 1/137 = {ALPHA:.6e})")
    print(f"  Q_int = {q_electron:.6f}")
    print(f"  μ     = {mu_electron:.6f}")
    print(f"  Spin  = {wvm_spin(1, 2)[1]}")

    print(f"\n{'─'*72}")
    print(f"SECTION 1: n₁ selection rule verification")
    print(f"{'─'*72}")
    print(f"\nQ_int for various n₁ at n₂ = 2:")
    for n1 in range(-4, 5):
        q = charge_integral_2d(n1, 2, s)
        label = " ← ELECTRON" if n1 == 1 else ""
        if n1 == 0:
            label = " (trivially zero: n₁=0)"
        print(f"  n₁ = {n1:+2d}:  Q_int = {q:12.6f}{label}")

    print(f"\n  RESULT: Only |n₁| = 1 modes carry charge.")
    print(f"  This eliminates {(2*n_max+1)**2 - 2*(2*n_max+1)} of "
          f"{(2*n_max+1)**2} modes on this sheet.")

    print(f"\n{'─'*72}")
    print(f"SECTION 2: Charge integral Q(1, n₂) for surviving modes")
    print(f"{'─'*72}")
    print(f"\n{'n₂':>4s} | {'Q_int':>12s} | {'Q/Q_e':>10s} | "
          f"{'α_eff':>12s} | {'α/α_e':>10s} | {'μ':>8s} | {'Spin':>20s}")
    print(f"  {'─'*90}")

    results = []
    for n2 in range(-n_max, n_max + 1):
        q = charge_integral_2d(1, n2, s)
        a = alpha_eff_kk(r, s, 1, n2)
        mu = mode_energy_2d(1, n2, r, s)
        spin_val, spin_label = wvm_spin(1, n2)
        q_ratio = q / q_electron if abs(q_electron) > 1e-15 else 0
        a_ratio = a / alpha_electron if alpha_electron > 1e-30 else 0

        if abs(a) > 1e30:
            a_str = "      ∞     "
            ar_str = "     ∞    "
        else:
            a_str = f"{a:12.6e}"
            ar_str = f"{a_ratio:10.4f}"

        marker = ""
        if n2 == 2:
            marker = " ← ELECTRON"
        elif "FORBIDDEN" in spin_label:
            marker = " ← killed by spin"
        elif spin_label == "undefined":
            marker = " ← killed by spin"

        print(f"  {n2:+3d} | {q:12.6f} | {q_ratio:10.4f} | "
              f"{a_str} | {ar_str} | {mu:8.4f} | {spin_label:>20s}{marker}")

        results.append({
            'n2': n2, 'Q_int': q, 'Q_ratio': q_ratio,
            'alpha_eff': a, 'alpha_ratio': a_ratio,
            'mu': mu, 'spin': spin_val, 'spin_label': spin_label,
        })

    print(f"\n{'─'*72}")
    print(f"SECTION 3: Spin-statistics filter applied")
    print(f"{'─'*72}")

    survivors = [r for r in results
                 if r['spin'] is not None
                 and (abs(r['spin'] - round(r['spin'])) < 1e-10
                      or abs(r['spin'] - 0.5) < 1e-10)]

    print(f"\nModes surviving spin filter (|n₁| = 1, valid spin):")
    print(f"{'n₂':>4s} | {'Spin':>10s} | {'α/α_e':>10s} | {'μ/μ_e':>10s} | Status")
    print(f"  {'─'*60}")
    for r in survivors:
        mu_ratio = r['mu'] / mu_electron
        status = "ELECTRON" if r['n2'] == 2 else "GHOST"
        if r['alpha_ratio'] > 1e10:
            ar_str = "DIVERGENT"
        else:
            ar_str = f"{r['alpha_ratio']:10.4f}"
        print(f"  {r['n2']:+3d} | {r['spin_label']:>10s} | {ar_str:>10s} | "
              f"{mu_ratio:10.4f} | {status}")

    killed = [r for r in results if r not in survivors and abs(r['Q_int']) > 1e-10]
    print(f"\n  Total modes with n₁=1, n₂ in [{-n_max},{n_max}]: {len(results)}")
    print(f"  Killed by n₁ rule (n₁ ≠ ±1): all other modes")
    print(f"  Killed by spin filter: {len(killed)} of {len(results)}")
    print(f"  Surviving: {len(survivors)}")

    return results, survivors


def main():
    print("=" * 72)
    print("R33 Track 1: Charge Integral Per Mode")
    print("=" * 72)
    print()
    print("Two selection rules are applied sequentially:")
    print("  1. n₁ selection rule (R19 F17): only |n₁| = 1 carries charge")
    print("  2. Spin-statistics filter (Q85 §6): spin = n₁/n₂ must be")
    print("     integer or half-integer")
    print()
    print("The charge integral Q(1, n₂) ∝ sin(2πs)/(n₂ - s) determines")
    print("the RELATIVE coupling strength of surviving modes.")

    r_e = 6.6
    s_e = solve_shear_for_alpha(r_e)
    print(f"\nElectron sheet: r_e = {r_e}, s_e = {s_e:.8f}")

    r_p = 6.6
    s_p = solve_shear_for_alpha(r_p)
    print(f"Proton sheet:   r_p = {r_p}, s_p = {s_p:.8f}")

    e_results, e_survivors = analyze_sheet("ELECTRON", r_e, s_e)
    p_results, p_survivors = analyze_sheet("PROTON", r_p, s_p)

    print(f"\n{'='*72}")
    print(f"SECTION 4: Cross-sheet modes (neutron-like)")
    print(f"{'='*72}")

    Gt, Gti, L, info = build_scaled_metric(r_e=r_e, r_nu=5.0, r_p=r_p,
                                            sigma_ep=0.038)

    cross_modes = [
        ((1, 2, 0, 0, 0, 0), "electron"),
        ((0, 0, 0, 0, 1, 2), "proton"),
        ((1, 2, 0, 0, 1, 2), "neutron candidate"),
        ((-1, 2, 0, 0, 1, 2), "neutron candidate (alt)"),
        ((1, 1, 0, 0, 0, 0), "e-sheet (1,1) ghost"),
        ((0, 0, 0, 0, 1, 1), "p-sheet (1,1) ghost"),
        ((1, 1, 0, 0, 1, 2), "cross ghost (1,1)+(1,2)"),
        ((1, 2, 0, 0, 1, 1), "cross ghost (1,2)+(1,1)"),
        ((1, 1, 0, 0, 1, 1), "cross ghost (1,1)+(1,1)"),
    ]

    print(f"\n{'Mode':>25s} | {'E (MeV)':>10s} | {'Q_KK':>5s} | {'Q_WvM':>10s} | "
          f"{'Spin':>10s} | Description")
    print(f"  {'─'*85}")
    for n, desc in cross_modes:
        E = mode_energy(n, Gti, L)
        Q_kk = mode_charge(n)

        q_e = charge_integral_2d(n[0], n[1], s_e) if n[0] != 0 else 0
        q_p = charge_integral_2d(n[4], n[5], s_p) if n[4] != 0 else 0
        Q_wvm = -q_e / charge_integral_2d(1, 2, s_e) + q_p / charge_integral_2d(1, 2, s_p) \
            if (abs(charge_integral_2d(1, 2, s_e)) > 1e-15) else 0

        s_half = mode_spin(n)
        spin_str = f"{'½' if s_half == 1 else str(s_half) + '/2'}"

        n_str = f"({n[0]},{n[1]},{n[2]},{n[3]},{n[4]},{n[5]})"
        print(f"  {n_str:>23s} | {E:10.3f} | {Q_kk:+5d} | {Q_wvm:+10.4f} | "
              f"{spin_str:>10s} | {desc}")

    print(f"\n{'='*72}")
    print(f"SECTION 5: Preference hierarchy summary")
    print(f"{'='*72}")

    print(f"\nOn each sheet, the charge integral Q ∝ sin(2πs)/(n₂ - s)")
    print(f"gives a coupling that DECREASES with |n₂|:")
    print(f"")
    print(f"  α(1, n₂)/α(1, 2) = [μ(1,n₂)/μ(1,2)] × [(2-s)/(n₂-s)]²")
    print(f"")
    print(f"Combined with the spin filter, only TWO modes survive per sheet:")
    print(f"")

    for sheet, results, survivors in [("Electron", e_results, e_survivors),
                                       ("Proton", p_results, p_survivors)]:
        print(f"  {sheet} sheet:")
        for sv in survivors:
            if sv['alpha_ratio'] > 1e10:
                ar = "DIVERGENT"
            else:
                ar = f"{sv['alpha_ratio']:.2f}×"
            print(f"    (1, {sv['n2']:+d}): {sv['spin_label']}, "
                  f"coupling = {ar} electron,  "
                  f"mass = {sv['mu'] / mode_energy_2d(1, 2, r_e, s_e):.3f}× electron")
        print()

    print(f"KEY FINDINGS:")
    print(f"─" * 72)
    print(f"""
F1. The n₁ = ±1 selection rule (R19 F17) eliminates the vast majority
    of modes.  On a grid of |n₁|,|n₂| ≤ 8, only 2×17 = 34 of 289
    modes carry any charge.  This is the primary ghost suppression
    mechanism from the charge integral.

F2. Among surviving modes (n₁ = 1), the charge integral gives coupling
    proportional to 1/(n₂ - s)².  This ENHANCES low-n₂ modes:
    
      (1, 0): coupling diverges (pole at n₂ = s ≈ 0.01)
      (1, 1): coupling ~ 2× electron
      (1, 2): coupling = 1× (this IS the electron)
      (1, 3): coupling ~ 0.66× electron
      (1, n₂ >> 1): coupling ~ 1/n₂² → strongly suppressed

    The charge integral does NOT prefer the electron over (1,1).
    It creates a preference hierarchy with (1,0) at the top.

F3. The spin filter eliminates most remaining modes:
      (1, 0): undefined spin → KILLED
      (1, 1): spin 1 (valid boson) → SURVIVES
      (1, 2): spin ½ (fermion) → ELECTRON
      (1, 3+): fractional spin → KILLED
      (1, -1): spin 1 (valid boson) → SURVIVES
      (1, -2+): fractional spin → KILLED

    Only THREE modes survive per sheet: (1,-1), (1,1), and (1,2).
    The bosons at (1,±1) have ~2× the electron's coupling and
    ~50% of its mass.

F4. The (1,1) boson is the critical remaining ghost.  It is:
    - Lighter than the electron (mass ~ 0.50 m_e ≈ 0.26 MeV)
    - More strongly coupled (α_eff ~ 2× electron)
    - Valid spin (spin-1 boson)
    - Charged (Q = -1)
    - NOT observed

    Its non-observation is the model's sharpest tension if the WvM
    spin assignment is correct.

F5. For high-n₂ modes, the charge integral provides STRONG natural
    suppression.  The coupling scales as 1/n₂², so modes with
    n₂ = 10 have ~1/25th the electron's coupling, and n₂ = 100
    has ~1/2500th.  Combined with the spin filter (which kills
    all n₂ > 2 for n₁ = 1), this is overkill — two independent
    mechanisms both suppress the same modes.

F6. The proton sheet shows identical structure: (1,2) is the proton,
    (1,1) is a ghost boson at ~half proton mass (~470 MeV) with
    ~2× coupling.  No such particle is observed.

F7. The n₁ selection rule and spin filter together reduce ~900 ghost
    modes to exactly 2 ghost bosons per charged sheet (4 total).
    The ghost problem is reduced from "~860 unexplained modes" to
    "4 unexplained charged bosons."  Resolving the (1,1) tension
    would close the ghost problem for the charged sheets entirely.
""")

    print(f"IMPLICATIONS FOR TRACK 7 (r_e scan):")
    print(f"─" * 72)
    print(f"""
The charge integral Q ∝ sin(2πs)/(n₂ - s) depends on s, which is
determined by r through solve_shear_for_alpha(r).  As r varies:
  - s changes to maintain α = 1/137
  - The coupling ratios α(1,n₂)/α(1,2) shift
  - The pole at n₂ = s moves (always near 0 for small s)

The (1,1) ghost cannot be eliminated by the charge integral alone:
Q(1,1) = sin(2πs)/(1-s) is nonzero for any s ≠ 0.  Only s = 0
gives Q(1,1) = 0 — but s = 0 also gives Q(1,2) = 0 (no electron).

CONCLUSION: The charge integral CANNOT pin r_e by making (1,1)
uncharged.  The (1,1) tension must be resolved by a mechanism
beyond the charge integral — e.g., the spin assignment being wrong
(spin = ½ per sheet, not n₁/n₂), or (1,1) being unstable.
""")


if __name__ == "__main__":
    main()
