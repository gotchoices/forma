"""
R60 Track 19 — Phase 1c: 7b ratio-rule audit.

Derivation 7b proposes:  spin = n_t / n_r  (single-sheet)

For a spin-½ particle on a single sheet, this requires
n_r = 2·n_t on that sheet.

For compound modes spanning multiple sheets, the extension is
not settled.  This audit tests three candidate extensions
against the Track 19 inventory (and the model-E/F Track 10
inventory for comparison):

 (A) STRICT per-sheet: every active sheet must have n_r = 2·n_t
 (B) SUM rule: total n_t/total n_r = 1/2
 (C) PARITY rule (current implementation): odd count of odd
     tube windings is 1 or 3 (i.e., odd total)

Reports compliance per tuple under each rule.

Sandboxed.
"""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from track10_hadron_inventory import MODEL_E_INVENTORY


def sheet_ratio(n_t, n_r):
    """Per-sheet ratio n_t/n_r, or None if n_r = 0."""
    if n_r == 0:
        return None  # degenerate
    return n_t / n_r


def active_sheet_ratios(n6):
    """For each sheet with nonzero content, return (sheet, n_t, n_r, ratio)."""
    n_et, n_er, n_nut, n_nur, n_pt, n_pr = n6
    sheets = []
    if n_et != 0 or n_er != 0:
        sheets.append(("e", n_et, n_er, sheet_ratio(n_et, n_er)))
    if n_nut != 0 or n_nur != 0:
        sheets.append(("ν", n_nut, n_nur, sheet_ratio(n_nut, n_nur)))
    if n_pt != 0 or n_pr != 0:
        sheets.append(("p", n_pt, n_pr, sheet_ratio(n_pt, n_pr)))
    return sheets


def strict_per_sheet_compliant(n6, target_spin="1/2"):
    """(A) STRICT: every active sheet has n_r = 2·n_t (spin 1/2)."""
    sheets = active_sheet_ratios(n6)
    if not sheets:
        return False  # no content = no spin
    for sheet, n_t, n_r, ratio in sheets:
        if ratio is None:
            return False  # n_r = 0: undefined ratio; reject under strict rule
        if ratio != 0.5:
            return False
    return True


def sum_rule_compliant(n6, target_spin="1/2"):
    """(B) SUM: total n_t / total n_r = 1/2."""
    n_et, n_er, n_nut, n_nur, n_pt, n_pr = n6
    total_nt = n_et + n_nut + n_pt
    total_nr = n_er + n_nur + n_pr
    if total_nr == 0:
        return False
    return abs(total_nt / total_nr - 0.5) < 1e-9


def parity_rule_compliant(n6):
    """(C) PARITY: odd count of odd tube windings = 1 or 3 (i.e., odd)."""
    n_et, _, n_nut, _, n_pt, _ = n6
    odd_count = (n_et % 2 != 0) + (n_nut % 2 != 0) + (n_pt % 2 != 0)
    return odd_count % 2 == 1


def main():
    print("=" * 96)
    print("R60 Track 19 — Phase 1c: 7b ratio-rule audit")
    print("=" * 96)
    print()
    print("  Three candidate rules for SPIN-½ compliance:")
    print("    (A) STRICT per-sheet: every active sheet has n_r = 2·n_t")
    print("    (B) SUM rule:         total n_t / total n_r = 1/2")
    print("    (C) PARITY rule:      odd count of odd tube windings = 1 or 3")
    print()
    print("  Rule (C) is what the Track 10 and Track 19 searches actually use.")
    print("  Rule (A) is the strict reading of 7b.  Rule (B) is a natural")
    print("  'total-winding' extension of 7b to compound modes.")
    print()

    # ── Audit the existing model-E inventory (used by model-F Track 12) ──
    print("─" * 96)
    print("  Model-E / model-F inventory audit (current tuples):")
    print("─" * 96)
    print()
    print(f"  {'particle':<10s}  {'tuple':<28s}  {'Q':>3s}  "
          f"{'sheets':<18s}  {'A strict':>9s}  {'B sum':>7s}  {'C parity':>9s}")
    print("  " + "-" * 96)

    counts = {"A": 0, "B": 0, "C": 0}
    unit_charge = 0
    for label, target, Q, tup, me_delta in MODEL_E_INVENTORY:
        if abs(Q) != 1:
            continue  # only check spin-½ for unit-charged particles
        unit_charge += 1

        a = strict_per_sheet_compliant(tup)
        b = sum_rule_compliant(tup)
        c = parity_rule_compliant(tup)

        if a: counts["A"] += 1
        if b: counts["B"] += 1
        if c: counts["C"] += 1

        sheets = [s[0] for s in active_sheet_ratios(tup)]
        sheets_str = "+".join(sheets) if sheets else "—"

        tup_str = str(tup).replace(" ", "")
        a_mark = "✓" if a else "✗"
        b_mark = "✓" if b else "✗"
        c_mark = "✓" if c else "✗"
        print(f"  {label:<10s}  {tup_str:<28s}  {Q:>+3d}  "
              f"{sheets_str:<18s}  {a_mark:>9s}  {b_mark:>7s}  {c_mark:>9s}")
    print()
    print(f"  {'Total unit-charge particles:':<50s}  {unit_charge}")
    print(f"  {'  obey rule (A) STRICT per-sheet:':<50s}  {counts['A']} / {unit_charge}")
    print(f"  {'  obey rule (B) SUM n_t/n_r = 1/2:':<50s}  {counts['B']} / {unit_charge}")
    print(f"  {'  obey rule (C) PARITY (current search):':<50s}  {counts['C']} / {unit_charge}")
    print()

    # ── Details: per-sheet ratios for each particle ──
    print("─" * 96)
    print("  Per-sheet ratio details (for unit-charged particles):")
    print("─" * 96)
    print()
    for label, target, Q, tup, me_delta in MODEL_E_INVENTORY:
        if abs(Q) != 1:
            continue
        sheets = active_sheet_ratios(tup)
        sheets_info = []
        for (s, n_t, n_r, r) in sheets:
            if r is None:
                sheets_info.append(f"{s}:({n_t},{n_r}→r undefined)")
            else:
                sheets_info.append(f"{s}:({n_t},{n_r}→s={r:.3f})")
        print(f"  {label:<10s}  {', '.join(sheets_info)}")
    print()

    # ── Verdict and implications ──
    print("─" * 96)
    print("  Verdict:")
    print("─" * 96)
    print()
    print("  (A) STRICT per-sheet: the rule fails for almost every compound")
    print("      particle in the inventory.  Few if any unit-charged hadrons")
    print("      satisfy n_r = 2·n_t on EVERY active sheet.")
    print("      → Strict 7b per-sheet reading is NOT met by our inventory.")
    print()
    print("  (B) SUM rule: most compound tuples fail.  This is because the")
    print("      sum-of-windings doesn't need to give 1/2 to have the right")
    print("      total angular momentum under a composition rule.")
    print("      → Sum rule is also NOT met by our inventory.")
    print()
    print("  (C) PARITY rule: this is what the search currently enforces for")
    print("      unit-charged particles.  Every matched inventory tuple passes")
    print("      by construction.")
    print()
    print("  Interpretation: the inventory uses the parity rule (R50-era) for")
    print("  spin assignment, NOT 7b's strict ratio rule.  This is a real")
    print("  inconsistency between our claimed 'adopting 7b as the spin")
    print("  derivation' and our inventory search implementation.")
    print()
    print("  Three ways forward:")
    print()
    print("  (1) ACCEPT that 7b applies only to single-sheet modes; compound")
    print("      modes use a SEPARATE spin-composition rule (to be derived).")
    print("      Current parity rule is an empirical stand-in.")
    print()
    print("  (2) EXTEND 7b to compound modes with a natural composition rule")
    print("      (e.g., tensor-product of per-sheet spins), then re-audit.")
    print("      May reveal that the inventory already works under a more")
    print("      sophisticated interpretation.")
    print()
    print("  (3) REDO the inventory search with the STRICT (A) rule and see")
    print("      if any compound-mode particles can be matched under a more")
    print("      restrictive tuple space.  Likely reveals many particles")
    print("      cannot be reached — would be informative as to where 7b's")
    print("      reach ends.")
    print()
    print("  Most honest framing: derivation 7b is a SINGLE-MODE spin rule.")
    print("  For the compound-mode inventory, we are implicitly using a")
    print("  different (parity-based) rule whose derivation is open.  This")
    print("  is an acknowledged gap in the current model documentation and")
    print("  should be stated openly.")


if __name__ == "__main__":
    main()
