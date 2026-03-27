#!/usr/bin/env python3
"""
R34 Track 3: Backing into the shear from 1/α₀ = 80.

The α formula  α = r²μ sin²(2πs) / (4π(2−s)²)  has two
free parameters: r (aspect ratio) and s (shear).  Currently,
s is solved from α = 1/137, making the formula a tautology.

This track asks: what if the BASE coupling is 1/80 (from
the weighted gauge partition, R32 F23)?  Solving s from
α₀ = 1/80 instead of 1/137 gives a different shear.

Is that shear geometrically natural?  Is it related to
1/r, 1/2π, a modular invariant, or some other clean number?

Also tests Approach B: replacing the denominator 4π(2−s)²
with 24 (the gauge channel count), and Approach C:
decomposing α into base × modulation.
"""

import sys
import os
import math
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.t6 import (
    alpha_kk, solve_shear_for_alpha, mu_12,
    M_P_MEV, M_E_MEV, hbar_c_MeV_fm, ALPHA,
)

R_E = 6.6
R_P = 8.906


print("=" * 70)
print("R34 Track 3: Backing into the shear")
print("=" * 70)


# ── Section 1: Current shears (s from α = 1/137) ─────────────────────
print(f"\n{'='*70}")
print("SECTION 1: Current shears (solved from α = 1/137.036)")
print("=" * 70)

s_e = solve_shear_for_alpha(R_E, ALPHA)
s_p = solve_shear_for_alpha(R_P, ALPHA)

print(f"\n  Electron sheet (r = {R_E}):")
print(f"    s = {s_e:.8f}")
print(f"    α(r, s) = {alpha_kk(R_E, s_e):.8e} = 1/{1/alpha_kk(R_E, s_e):.3f}")
print(f"    2πs = {2*math.pi*s_e:.8f}")
print(f"    sin(2πs) = {math.sin(2*math.pi*s_e):.8f}")
print(f"    sin²(2πs) = {math.sin(2*math.pi*s_e)**2:.8e}")

print(f"\n  Proton sheet (r = {R_P}):")
print(f"    s = {s_p:.8f}")
print(f"    α(r, s) = {alpha_kk(R_P, s_p):.8e} = 1/{1/alpha_kk(R_P, s_p):.3f}")
print(f"    2πs = {2*math.pi*s_p:.8f}")
print(f"    sin(2πs) = {math.sin(2*math.pi*s_p):.8f}")
print(f"    sin²(2πs) = {math.sin(2*math.pi*s_p)**2:.8e}")


# ── Section 2: Shears from α₀ = 1/80 ────────────────────────────────
print(f"\n\n{'='*70}")
print("SECTION 2: Shears solved from α₀ = 1/80")
print("=" * 70)

ALPHA_80 = 1.0 / 80.0
ALPHA_805 = 1.0 / 80.5

for alpha_target, label in [(ALPHA_80, "1/80"), (ALPHA_805, "1/80.5")]:
    print(f"\n  Target: α₀ = {label}")

    s_e_80 = solve_shear_for_alpha(R_E, alpha_target)
    s_p_80 = solve_shear_for_alpha(R_P, alpha_target)

    if s_e_80 is not None:
        print(f"\n  Electron sheet (r = {R_E}):")
        print(f"    s = {s_e_80:.8f}")
        print(f"    2πs = {2*math.pi*s_e_80:.8f}")
        print(f"    sin(2πs) = {math.sin(2*math.pi*s_e_80):.8f}")
        print(f"    sin²(2πs) = {math.sin(2*math.pi*s_e_80)**2:.8e}")
        print(f"    α check = 1/{1/alpha_kk(R_E, s_e_80):.3f}")
        print(f"    Ratio s₈₀/s₁₃₇ = {s_e_80/s_e:.6f}")
    else:
        print(f"    Electron: no solution found")

    if s_p_80 is not None:
        print(f"\n  Proton sheet (r = {R_P}):")
        print(f"    s = {s_p_80:.8f}")
        print(f"    2πs = {2*math.pi*s_p_80:.8f}")
        print(f"    sin(2πs) = {math.sin(2*math.pi*s_p_80):.8f}")
        print(f"    sin²(2πs) = {math.sin(2*math.pi*s_p_80)**2:.8e}")
        print(f"    α check = 1/{1/alpha_kk(R_P, s_p_80):.3f}")
        print(f"    Ratio s₈₀/s₁₃₇ = {s_p_80/s_p:.6f}")
    else:
        print(f"    Proton: no solution found")


# ── Section 3: Check for geometric significance ──────────────────────
print(f"\n\n{'='*70}")
print("SECTION 3: Geometric significance of shears")
print("=" * 70)

candidates = [
    ("1/(2π)",       1/(2*math.pi)),
    ("1/(4π)",       1/(4*math.pi)),
    ("1/r_e",        1/R_E),
    ("1/r_p",        1/R_P),
    ("1/(2πr_e)",    1/(2*math.pi*R_E)),
    ("1/(2πr_p)",    1/(2*math.pi*R_P)),
    ("α (1/137)",    ALPHA),
    ("√α",           math.sqrt(ALPHA)),
    ("1/12",         1/12),
    ("1/24",         1/24),
    ("1/48",         1/48),
    ("1/10",         0.1),
    ("1/20",         0.05),
    ("1/100",        0.01),
    ("1/√(4π)",      1/math.sqrt(4*math.pi)),
    ("2πα",          2*math.pi*ALPHA),
    ("α/π",          ALPHA/math.pi),
    ("1/r_e²",       1/R_E**2),
    ("1/r_p²",       1/R_P**2),
    ("1/(r_e+r_p)",  1/(R_E + R_P)),
]

s_e_80 = solve_shear_for_alpha(R_E, ALPHA_80)
s_p_80 = solve_shear_for_alpha(R_P, ALPHA_80)

for s_val, s_name, r_val in [
    (s_e,    "s_e(137)",    R_E),
    (s_p,    "s_p(137)",    R_P),
    (s_e_80, "s_e(80)",     R_E),
    (s_p_80, "s_p(80)",     R_P),
]:
    if s_val is None:
        continue
    print(f"\n  {s_name} = {s_val:.8f}")
    print(f"  {'Candidate':<16s} {'Value':>12s} {'Ratio':>10s} {'Match?':>8s}")
    print(f"  {'─'*16} {'─'*12} {'─'*10} {'─'*8}")
    for cname, cval in candidates:
        if cval > 0 and cval < 0.5:
            ratio = s_val / cval
            match = "YES" if 0.95 < ratio < 1.05 else ""
            print(f"  {cname:<16s} {cval:12.8f} {ratio:10.4f} {match:>8s}")


# ── Section 4: Approach B — replace 4π(2−s)² with 24 ─────────────────
print(f"\n\n{'='*70}")
print("SECTION 4: Approach B — denominator = 24 instead of 4π(2−s)²")
print("=" * 70)

print(f"\n  Standard formula: α = r²μ sin²(2πs) / (4π(2−s)²)")
print(f"  Modified formula: α = r²μ sin²(2πs) / 24")
print(f"  (24 = number of gauge field components = 4 non-compact × 6 compact)")

def alpha_mod24(r, s):
    mu = math.sqrt(1 / r**2 + (2 - s)**2)
    return r**2 * mu * math.sin(2 * math.pi * s)**2 / 24.0

print(f"\n  What α does the 24-denominator give for the STANDARD shears (from 137)?")
print(f"    Electron: α_24(r_e, s_e) = {alpha_mod24(R_E, s_e):.6e} = 1/{1/alpha_mod24(R_E, s_e):.2f}")
print(f"    Proton:   α_24(r_p, s_p) = {alpha_mod24(R_P, s_p):.6e} = 1/{1/alpha_mod24(R_P, s_p):.2f}")

denom_standard_e = 4 * math.pi * (2 - s_e)**2
denom_standard_p = 4 * math.pi * (2 - s_p)**2
print(f"\n  Standard denominator values:")
print(f"    Electron: 4π(2−s)² = {denom_standard_e:.4f}")
print(f"    Proton:   4π(2−s)² = {denom_standard_p:.4f}")
print(f"    Ratio to 24: {denom_standard_e/24:.4f} (e), {denom_standard_p/24:.4f} (p)")

# Solve s for α = 1/137 with denominator = 24
print(f"\n  Solving s from α = 1/137 with denominator = 24:")
from scipy.optimize import brentq

for r, rname in [(R_E, "electron"), (R_P, "proton")]:
    def resid(s):
        return alpha_mod24(r, s) - ALPHA
    s_scan = np.linspace(0.001, 0.49, 3000)
    a_scan = [alpha_mod24(r, s) for s in s_scan]
    found = False
    for i in range(len(s_scan) - 1):
        if (a_scan[i] - ALPHA) * (a_scan[i+1] - ALPHA) < 0:
            s_sol = brentq(resid, s_scan[i], s_scan[i+1])
            print(f"    {rname}: s = {s_sol:.8f}, 2πs = {2*math.pi*s_sol:.6f}")
            found = True
            break
    if not found:
        print(f"    {rname}: no solution (max α_24 = {max(a_scan):.6f} = 1/{1/max(a_scan):.1f})")

# Solve s for α = 1/80 with denominator = 24
print(f"\n  Solving s from α = 1/80 with denominator = 24:")
for r, rname in [(R_E, "electron"), (R_P, "proton")]:
    def resid80(s):
        return alpha_mod24(r, s) - ALPHA_80
    s_scan = np.linspace(0.001, 0.49, 3000)
    a_scan = [alpha_mod24(r, s) for s in s_scan]
    found = False
    for i in range(len(s_scan) - 1):
        if (a_scan[i] - ALPHA_80) * (a_scan[i+1] - ALPHA_80) < 0:
            s_sol = brentq(resid80, s_scan[i], s_scan[i+1])
            print(f"    {rname}: s = {s_sol:.8f}, 2πs = {2*math.pi*s_sol:.6f}")
            found = True
            break
    if not found:
        print(f"    {rname}: no solution (max α_24 = {max(a_scan):.6f} = 1/{1/max(a_scan):.1f})")


# ── Section 5: The α formula as a function of s only ─────────────────
print(f"\n\n{'='*70}")
print("SECTION 5: α(s) landscape for fixed r = r_e and r = r_p")
print("=" * 70)

print(f"\n  Scanning α(r, s) over s ∈ (0, 0.5):")
print(f"\n  {'s':>10s} {'α(r_e,s)':>14s} {'1/α(r_e)':>10s} {'α(r_p,s)':>14s} {'1/α(r_p)':>10s}")
print(f"  {'─'*10} {'─'*14} {'─'*10} {'─'*14} {'─'*10}")

for s in np.linspace(0.001, 0.15, 30):
    ae = alpha_kk(R_E, s)
    ap = alpha_kk(R_P, s)
    print(f"  {s:10.5f} {ae:14.8f} {1/ae:10.2f} {ap:14.8f} {1/ap:10.2f}")

# Find the maximum of α(r, s) over s
s_scan_fine = np.linspace(0.001, 0.49, 10000)
ae_scan = [alpha_kk(R_E, s) for s in s_scan_fine]
ap_scan = [alpha_kk(R_P, s) for s in s_scan_fine]

i_max_e = np.argmax(ae_scan)
i_max_p = np.argmax(ap_scan)

print(f"\n  Maximum α for electron sheet:")
print(f"    s_max = {s_scan_fine[i_max_e]:.6f}, α_max = {ae_scan[i_max_e]:.6f} = 1/{1/ae_scan[i_max_e]:.2f}")
print(f"\n  Maximum α for proton sheet:")
print(f"    s_max = {s_scan_fine[i_max_p]:.6f}, α_max = {ap_scan[i_max_p]:.6f} = 1/{1/ap_scan[i_max_p]:.2f}")


# ── Section 6: Approach C — decomposition α = α_base × mod ───────────
print(f"\n\n{'='*70}")
print("SECTION 6: Approach C — decompose α into base × modulation")
print("=" * 70)

print(f"\n  If 1/α_base = 80.5, then:")
print(f"    modulation at E=0:  80.5/137 = {80.5/137:.6f}")
print(f"    modulation at E→∞: 80.5/24 = {80.5/24:.6f}")
print(f"")
print(f"  The shear factor sin²(2πs) varies between 0 and 1.")
print(f"  At s = s_e(137): sin²(2πs) = {math.sin(2*math.pi*s_e)**2:.6e}")
print(f"  At s = s_e(80):  sin²(2πs) = {math.sin(2*math.pi*s_e_80)**2:.6e}")

ratio_sin2 = math.sin(2*math.pi*s_e_80)**2 / math.sin(2*math.pi*s_e)**2
print(f"\n  Ratio of sin²(2πs) values: {ratio_sin2:.4f}")
print(f"  Ratio of α values: {ALPHA_80/ALPHA:.4f} = 137/80 = {137/80:.4f}")

# The formula decomposition:
# α = [r²μ / (4π(2−s)²)] × sin²(2πs)
# The first factor depends weakly on s (through μ and (2−s)²)
# The second factor is the "modulation"

print(f"\n  Decomposition: α = prefactor(r,s) × sin²(2πs)")
for s_val, label in [(s_e, "s_e(137)"), (s_e_80, "s_e(80)"), (s_p, "s_p(137)"), (s_p_80, "s_p(80)")]:
    if s_val is None:
        continue
    r_val = R_E if "e" in label else R_P
    mu = math.sqrt(1/r_val**2 + (2-s_val)**2)
    prefactor = r_val**2 * mu / (4 * math.pi * (2-s_val)**2)
    sin2 = math.sin(2*math.pi*s_val)**2
    alpha_check = prefactor * sin2
    print(f"    {label}:")
    print(f"      prefactor = {prefactor:.6f}")
    print(f"      sin²(2πs) = {sin2:.6e}")
    print(f"      α = {alpha_check:.6e} = 1/{1/alpha_check:.2f}")
    print(f"      1/prefactor = {1/prefactor:.4f}")


# ── Section 7: What s gives α = 1/N for various N? ───────────────────
print(f"\n\n{'='*70}")
print("SECTION 7: Shear for various target 1/α values")
print("=" * 70)

targets = [24, 40, 60, 80, 80.5, 100, 120, 128, 137, 137.036]

print(f"\n  {'1/α target':>12s} {'s_e':>12s} {'s_p':>12s} {'2πs_e':>10s} {'2πs_p':>10s} {'s_e/s_e137':>12s}")
print(f"  {'─'*12} {'─'*12} {'─'*12} {'─'*10} {'─'*10} {'─'*12}")

for inv_a in targets:
    a_target = 1.0 / inv_a
    se = solve_shear_for_alpha(R_E, a_target)
    sp = solve_shear_for_alpha(R_P, a_target)

    if se is not None and sp is not None:
        print(f"  {inv_a:12.1f} {se:12.8f} {sp:12.8f} {2*math.pi*se:10.6f} {2*math.pi*sp:10.6f} {se/s_e:12.6f}")
    elif se is not None:
        print(f"  {inv_a:12.1f} {se:12.8f} {'none':>12s} {2*math.pi*se:10.6f} {'—':>10s} {se/s_e:12.6f}")
    else:
        print(f"  {inv_a:12.1f} {'none':>12s} {'none':>12s}")


# ── Section 8: Relationship between s values ─────────────────────────
print(f"\n\n{'='*70}")
print("SECTION 8: Relationships between shear values")
print("=" * 70)

if s_e_80 is not None:
    print(f"\n  s_e(137) = {s_e:.8f}")
    print(f"  s_e(80)  = {s_e_80:.8f}")
    print(f"  s_e(80)/s_e(137) = {s_e_80/s_e:.6f}")
    print(f"  s_e(80) − s_e(137) = {s_e_80 - s_e:.8f}")
    print(f"  √(80/137) = {math.sqrt(80/137):.6f}")
    print(f"  √(s_e(80)/s_e(137)) = {math.sqrt(s_e_80/s_e):.6f}")
    print(f"  80/137 = {80/137:.6f}")
    print(f"  (s_e(80)/s_e(137))² = {(s_e_80/s_e)**2:.6f}")

    # Since α ∝ sin²(2πs) approximately:
    # α₈₀/α₁₃₇ = sin²(2πs₈₀)/sin²(2πs₁₃₇) ≈ (s₈₀/s₁₃₇)²
    # for small s (sin(x) ≈ x)
    print(f"\n  Small-s approximation: α ∝ s²")
    print(f"  Predicted ratio: (s₈₀/s₁₃₇)² = {(s_e_80/s_e)**2:.6f}")
    print(f"  Actual ratio:    α₈₀/α₁₃₇   = {ALPHA_80/ALPHA:.6f} = 137/80 = {137/80:.6f}")

    # Check if s² is truly proportional to α
    print(f"\n  More precisely: sin²(2πs₈₀)/sin²(2πs₁₃₇)")
    sin_ratio = math.sin(2*math.pi*s_e_80)**2 / math.sin(2*math.pi*s_e)**2
    print(f"    = {sin_ratio:.6f}")
    print(f"  But α₈₀/α₁₃₇ = {ALPHA_80/ALPHA:.6f}")
    print(f"  Discrepancy: {sin_ratio/(ALPHA_80/ALPHA):.6f}")
    print(f"  (Not exactly proportional because prefactor also depends on s)")


# ── SUMMARY ──────────────────────────────────────────────────────────
print(f"\n\n{'='*70}")
print("SUMMARY")
print(f"{'='*70}")

print(f"""
Approach A: Solving s from α₀ = 1/80 instead of 1/137
  Electron: s changes from {s_e:.6f} to {s_e_80:.6f} (ratio {s_e_80/s_e:.4f})
  Proton:   s changes from {s_p:.6f} to {s_p_80:.6f} (ratio {s_p_80/s_p:.4f})

  Neither s value matches any obvious geometric constant
  (1/2π, 1/r, modular invariant, etc.) — both are small,
  arbitrary-looking numbers.

  The shear is approximately proportional to √α for small s
  (because α ∝ sin²(2πs) ≈ (2πs)² for small s).

Approach B: Denominator = 24
  Standard denominator: 4π(2−s)² ≈ {denom_standard_e:.2f} (electron)
  This is already ≈ 50.  24 is about half.
  Effect: using 24 approximately doubles α.

Approach C: Decomposition
  The prefactor r²μ/(4π(2−s)²) is ~{R_E**2*math.sqrt(1/R_E**2+4)/(4*math.pi*4):.1f} for the
  electron sheet.  The shear sin²(2πs) is the small factor
  that makes α small.  Changing the target α just rescales
  the shear — there is no qualitative change in the formula.

Key finding: The shear is a CONTINUOUS free parameter with
no preferred value from the formula alone.  Both 1/137 and
1/80 correspond to small shears with no obvious geometric
significance.  The formula cannot select between them.
""")
