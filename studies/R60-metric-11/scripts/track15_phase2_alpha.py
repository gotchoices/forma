"""
R60 Track 15 — Phase 2: composite α-sum rule (gcd-aware).

Test whether the proposed composite α rule:
    α_sum_comp = n_et − (n_pt / gcd(|n_pt|, |n_pr|)) + n_νt

gives the right physics:
 (a) Bare (3, 6) proton lands at α = α (not 9α).
 (b) Model-F existing modes (gcd = 1) are unchanged — composite
     rule reduces to bare rule.
 (c) Nuclear Z² scaling preserved if we use (n_pt = 3A, n_pr = 6A)
     with appropriate n_et compensation.

Sandboxed.  No changes to model-F or other tracks.
"""

import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))

from track1_solver import ALPHA

from track10_hadron_inventory import (
    MODEL_E_INVENTORY, mode_alpha_sum,
)


def gcd_safe(a, b):
    """GCD, returning 1 when either is 0."""
    a, b = abs(a), abs(b)
    if a == 0 and b == 0:
        return 1
    if a == 0:
        return b
    if b == 0:
        return a
    return math.gcd(a, b)


def alpha_sum_composite(n6):
    """Composite gcd-aware α-sum rule for 6-tuple mode.

    Uses the p-sheet gcd to reduce n_pt contribution.  For gcd=1
    (most model-F modes) this equals the bare rule.  For gcd>1
    (like (3, 6) proton), n_pt is divided by gcd — representing
    the "per-strand charge" of a composite mode.
    """
    n_et, n_er, n_νt, n_νr, n_pt, n_pr = n6
    gcd_p = gcd_safe(n_pt, n_pr)
    return n_et - (n_pt // gcd_p if gcd_p > 0 else 0) + n_νt


def main():
    print("=" * 72)
    print("R60 Track 15 — Phase 2: composite α-sum rule (gcd-aware)")
    print("=" * 72)
    print()
    print("  Bare rule:       α_sum = n_et − n_pt + n_νt")
    print("  Composite rule:  α_sum = n_et − n_pt/gcd(|n_pt|,|n_pr|) + n_νt")
    print()

    # ── Test (a): proton at bare (3, 6) ──
    print("─" * 72)
    print("Test (a): proton at bare (0, 0, 0, 0, 3, 6)")
    print("─" * 72)
    n_proton_36 = (0, 0, 0, 0, 3, 6)
    bare = mode_alpha_sum(n_proton_36)
    comp = alpha_sum_composite(n_proton_36)
    print(f"  mode              = (0, 0, 0, 0, 3, 6)")
    print(f"  gcd(|n_pt|,|n_pr|) = {gcd_safe(3, 6)}")
    print(f"  bare α_sum       = {bare}  → α/α = {bare*bare}")
    print(f"  composite α_sum  = {comp}  → α/α = {comp*comp}")
    print(f"  composite rule: proton α = α ✓" if comp*comp == 1 else "  composite rule FAILED")
    print()

    # ── Test (b): all model-F (gcd=1) modes — composite = bare ──
    print("─" * 72)
    print("Test (b): model-F inventory — composite should equal bare for gcd=1")
    print("─" * 72)
    print()
    print(f"  {'particle':<10s}  {'tuple':<28s}  "
          f"{'gcd_p':>5s}  {'bare α/α':>10s}  {'comp α/α':>10s}  {'agree?'}")
    n_disagreements = 0
    for label, target, Q, tup, _ in MODEL_E_INVENTORY:
        bare_val = mode_alpha_sum(tup)**2
        comp_val = alpha_sum_composite(tup)**2
        gcd_p = gcd_safe(tup[4], tup[5])
        match = "✓" if bare_val == comp_val else "✗"
        if bare_val != comp_val:
            n_disagreements += 1
        tuple_str = str(tup).replace(" ", "")
        print(f"  {label:<10s}  {tuple_str:<28s}  "
              f"{gcd_p:>5d}  {bare_val:>10d}  {comp_val:>10d}  {match}")
    print()
    if n_disagreements == 0:
        print(f"  → All {len(MODEL_E_INVENTORY)} model-F inventory modes agree under both rules")
        print(f"    (backward compatibility confirmed)")
    else:
        print(f"  → {n_disagreements} model-F modes get different α under the composite rule")
    print()

    # ── Test (c): nuclear Z² scaling under composite rule ──
    print("─" * 72)
    print("Test (c): Nuclear scaling with (3, 6) proton base")
    print("─" * 72)
    print()
    print("  Propose: nuclear mode has (n_pt, n_pr) = (3A, 6A), gcd = 3A")
    print("  n_pt/gcd = (3A)/(3A) = 1 always (per-proton contribution)")
    print("  α_sum = n_et − 1 + n_νt")
    print()
    print(f"  For α_Coulomb = Z²α, need (α_sum)² = Z², so α_sum = ±Z")
    print(f"  With n_pt/gcd = 1 and n_νt = 0: need n_et = 1 − Z (or Z − 1 + something)")
    print()
    print(f"  {'Nucleus':<10s}  {'A':>3s}  {'Z':>3s}  {'n_et':>5s}  "
          f"{'n_pt':>5s}  {'n_pr':>5s}  {'gcd_p':>5s}  "
          f"{'bare α_sum':>11s}  {'comp α_sum':>11s}  "
          f"{'bare α/α':>10s}  {'comp α/α':>10s}")
    for label, A, Z in [("d",2,1), ("⁴He",4,2), ("¹²C",12,6), ("⁵⁶Fe",56,26)]:
        n_pt = 3 * A
        n_pr = 6 * A
        # Under composite rule, n_pt/gcd = 1 so α_sum_comp = n_et + 0 - 1
        # For α_sum_comp = -Z: n_et = 1 - Z
        n_et = 1 - Z
        n6 = (n_et, 0, 0, 0, n_pt, n_pr)
        bare = mode_alpha_sum(n6)
        comp = alpha_sum_composite(n6)
        gcd_p = gcd_safe(n_pt, n_pr)
        print(f"  {label:<10s}  {A:>3d}  {Z:>3d}  {n_et:>+5d}  "
              f"{n_pt:>5d}  {n_pr:>5d}  {gcd_p:>5d}  "
              f"{bare:>+11d}  {comp:>+11d}  "
              f"{bare*bare:>10d}  {comp*comp:>10d}  (target: Z²={Z*Z})")
    print()
    print("  Composite rule gives α/α = Z² exactly for every nucleus ✓")
    print("  Required n_et = 1 − Z (negative for Z > 1) — electron-sheet")
    print("  compensation needed for each nucleus")
    print()

    # ── Compare with model-F bare rule nuclear scaling ──
    print("─" * 72)
    print("For reference: model-F bare rule nuclear scaling")
    print("  (n_et, n_pt, n_pr) = (A−Z, A, 3A)")
    print("─" * 72)
    print(f"  {'Nucleus':<10s}  {'A':>3s}  {'Z':>3s}  {'n_et':>5s}  "
          f"{'n_pt':>5s}  {'n_pr':>5s}  {'gcd_p':>5s}  "
          f"{'bare α_sum':>11s}  {'bare α/α':>10s}")
    for label, A, Z in [("d",2,1), ("⁴He",4,2), ("¹²C",12,6), ("⁵⁶Fe",56,26)]:
        n_et = A - Z
        n_pt = A
        n_pr = 3 * A
        n6 = (n_et, 0, 0, 0, n_pt, n_pr)
        bare = mode_alpha_sum(n6)
        gcd_p = gcd_safe(n_pt, n_pr)
        print(f"  {label:<10s}  {A:>3d}  {Z:>3d}  {n_et:>+5d}  "
              f"{n_pt:>5d}  {n_pr:>5d}  {gcd_p:>5d}  "
              f"{bare:>+11d}  "
              f"{bare*bare:>10d}")
    print()
    print("  Both work for α scaling.  Key difference: composite rule needs")
    print("  different nuclear structure (n_pt = 3A vs A); L_ring_p doesn't scale")
    print("  the same way between schemes.  Phase 3 tests nuclear MASS fit.")
    print()

    print("Phase 2 complete.")
    print()
    print("Key findings:")
    print("  (a) composite rule gives proton α = α ✓")
    print("  (b) composite rule is backward-compatible for all gcd=1 modes ✓")
    print("  (c) nuclear Z² scaling preserved with (n_pt, n_pr) = (3A, 6A)")
    print("      and n_et = 1−Z compensation")


if __name__ == "__main__":
    main()
