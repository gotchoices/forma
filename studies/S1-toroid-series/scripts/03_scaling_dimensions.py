#!/usr/bin/env python3
"""
03_scaling_dimensions.py — Dimensional scaling analysis.

Tests Proposition P3 (finite number of terms / Planck floor cutoff) and
P4 (dimensional correspondence with string/M-theory).

For a hierarchy of nested tori scaled by ratio r, this script:
  1. Computes how many layers are needed to reach the Planck length,
     starting from the Compton wavelength.
  2. Reports whether that layer count matches known dimensional constraints
     (6 extra in 10D string theory, 7 extra in 11D M-theory).
  3. Inverts the question: what scaling ratio gives exactly 6 or 7 layers
     to the Planck floor?
  4. Checks whether those "dimensionally-motivated" ratios produce a good
     series sum.

Reference: theory.md §4 (P3, P4), §3.2
"""

import math, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib import constants as C
from lib.wvm import S_TARGET
from lib.series import geometric_sum, infinite_sum


def layers_to_planck(r):
    """How many times must we multiply λ_C by r before we drop below l_P?"""
    if r <= 0 or r >= 1:
        return None
    return math.ceil(math.log(C.l_P / C.lambda_C) / math.log(r))


def r_for_n_layers(n):
    """What ratio r gives exactly n multiplications from λ_C to l_P?"""
    return (C.l_P / C.lambda_C) ** (1 / n)


CANDIDATES = [
    ("α",       C.alpha),
    ("√α",      math.sqrt(C.alpha)),
    ("4πα",     4 * math.pi * C.alpha),
    ("1/11",    1/11),
    ("1/ϕ",     1/C.phi),
    ("1/ϕ²",    1/C.phi**2),
    ("1/ϕ³",    1/C.phi**3),
    ("1/ϕ⁴",    1/C.phi**4),
    ("1/π",     1/math.pi),
    ("1/e_nat", 1/math.e),
]


def main():
    print("=" * 72)
    print("Scaling & Dimensional Analysis — Propositions P3 & P4")
    print("=" * 72)
    print()
    print(f"  λ_C  = {C.lambda_C:.6e} m  (electron Compton wavelength)")
    print(f"  l_P  = {C.l_P:.6e} m  (Planck length)")
    print(f"  Ratio λ_C / l_P = {C.lambda_C / C.l_P:.3e}")
    print(f"  log₁₀(λ_C / l_P) = {math.log10(C.lambda_C / C.l_P):.2f}")
    print()

    # ── Part 1: Named ratios — how many layers to Planck? ─────────────────────
    print("─" * 72)
    print("Layers from λ_C to l_P for named scaling ratios:")
    print("─" * 72)
    print(f"  {'Name':<10s} {'r':>10s}  {'Layers':>6s}  {'Final layer':>12s}  "
          f"{'× l_P':>8s}  {'S(∞)':>10s}  {'Charge err':>10s}")
    print()

    for name, r in CANDIDATES:
        n = layers_to_planck(r)
        if n is None or n > 500:
            continue
        final = C.lambda_C * r ** n
        ratio_planck = final / C.l_P
        s_inf = infinite_sum(r)
        charge_err = abs(s_inf - S_TARGET) / S_TARGET * 100
        print(f"  {name:<10s} {r:>10.6f}  {n:>6d}  {final:>12.3e}  "
              f"{ratio_planck:>8.1f}  {s_inf:>10.6f}  {charge_err:>9.4f}%")

    print()

    # ── Part 2: Layer-by-layer detail for the best candidates ─────────────────
    best = [("α", C.alpha), ("4πα", 4*math.pi*C.alpha), ("1/11", 1/11)]

    for name, r in best:
        n = layers_to_planck(r)
        print("─" * 72)
        print(f"Layer-by-layer: {name}  (r = {r:.8f})")
        print("─" * 72)
        print(f"  {'Layer':>5s}  {'Size (m)':>12s}  {'× l_P':>14s}  "
              f"{'Cum. series':>12s}  {'Charge err':>10s}")
        for k in range(n + 1):
            size = C.lambda_C * r ** k
            ratio_p = size / C.l_P
            s_k = geometric_sum(r, k)
            c_err = abs(s_k - S_TARGET) / S_TARGET * 100
            marker = " ← Planck floor" if size < C.l_P else ""
            print(f"  {k:>5d}  {size:>12.3e}  {ratio_p:>14.1f}  "
                  f"{s_k:>12.8f}  {c_err:>9.4f}%{marker}")
        print()

    # ── Part 3: Invert — what r gives exactly N layers? ───────────────────────
    print("─" * 72)
    print("Inversion: What ratio r gives exactly N layers from λ_C to l_P?")
    print("─" * 72)
    print(f"  {'N layers':>8s}  {'Total dims':>10s}  {'r':>12s}  "
          f"{'S(∞)':>10s}  {'Charge err':>10s}  {'Note':>20s}")
    print()

    dim_notes = {
        6:  "10D string (6 extra)",
        7:  "11D M-theory (7 extra)",
        8:  "F-theory (8 extra)",
        10: "10 extra spatial",
        11: "Gemini claim",
    }

    for n in range(1, 16):
        r = r_for_n_layers(n)
        s_inf = infinite_sum(r)
        c_err = abs(s_inf - S_TARGET) / S_TARGET * 100
        note = dim_notes.get(n, "")
        print(f"  {n:>8d}  {n+3:>10d}  {r:>12.8f}  "
              f"{s_inf:>10.6f}  {c_err:>9.4f}%  {note:>20s}")

    print()
    print("=" * 72)
    print("KEY FINDING")
    print("=" * 72)
    print()
    print("The charge target (S ≈ 1.0985) and the Planck floor are")
    print("two independent constraints.  For a given r, both must be")
    print("satisfied simultaneously:")
    print("  • The series must sum to S_TARGET.")
    print("  • The smallest sub-torus must be ≥ l_P.")
    print()
    print("For small r (~0.09), the series converges in 3–4 terms,")
    print("so the Planck floor is reached long after the series has")
    print("effectively converged.  The number of 'active' terms is")
    print("therefore set by the series convergence, NOT by the Planck")
    print("cutoff — unless the scaling ratio is much larger (r > 0.3).")
    print()


if __name__ == "__main__":
    main()
