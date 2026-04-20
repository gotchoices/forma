"""
R60 Track 20 — Phases A + B: Enumerate spin rules, audit inventories.

Test 12 candidate spin-composition rules against two inventories:
 - Original Track 10 model-E / model-F tuples (R50-parity-selected)
 - Track 19 Z₃-compliant tuples (Z₃ + parity-selected)

For each particle with known observed spin, check rule compliance.
Report per-rule pass counts across the inventory.

Sandboxed.
"""

import sys, os
import math
from fractions import Fraction

sys.path.insert(0, os.path.dirname(__file__))

from track10_hadron_inventory import MODEL_E_INVENTORY


# Observed spins for each inventory particle
OBSERVED_SPIN = {
    "electron":  Fraction(1, 2),
    "muon":      Fraction(1, 2),
    "tau":       Fraction(1, 2),
    "proton":    Fraction(1, 2),
    "neutron":   Fraction(1, 2),
    "Λ":         Fraction(1, 2),
    "Σ⁻":        Fraction(1, 2),
    "Σ⁺":        Fraction(1, 2),
    "Ξ⁻":        Fraction(1, 2),
    "Ξ⁰":        Fraction(1, 2),
    "η′":        Fraction(0),
    "φ":         Fraction(1),
    "ρ":         Fraction(1),
    "K⁰":        Fraction(0),
    "K±":        Fraction(0),
    "η":         Fraction(0),
    "π⁰":        Fraction(0),
    "π±":        Fraction(0),
}


def sheet_ratio(n_t, n_r):
    """Per-sheet ratio as Fraction; None if both zero."""
    if n_t == 0 and n_r == 0:
        return None
    if n_r == 0:
        return None  # undefined; treat as None for rule logic
    return Fraction(n_t, n_r)


def active_sheets(n6):
    """Return list of (sheet_name, n_t, n_r, ratio) for nonzero sheets."""
    n_et, n_er, n_nut, n_nur, n_pt, n_pr = n6
    out = []
    if n_et or n_er:
        out.append(("e", n_et, n_er, sheet_ratio(n_et, n_er)))
    if n_nut or n_nur:
        out.append(("ν", n_nut, n_nur, sheet_ratio(n_nut, n_nur)))
    if n_pt or n_pr:
        out.append(("p", n_pt, n_pr, sheet_ratio(n_pt, n_pr)))
    return out


# ─── Rule implementations (return predicted spin, or None if undefined) ───

def rule_1_strict_per_sheet(n6, target):
    """Every active sheet has n_r = 2·n_t.  Pass iff every ratio is 1/2
    (or -1/2), OR single sheet with that ratio."""
    sheets = active_sheets(n6)
    if not sheets:
        return False
    for (_, _, _, r) in sheets:
        if r is None or abs(r) != Fraction(1, 2):
            return False
    return target == Fraction(1, 2)


def rule_2_sum_all(n6, target):
    """Σ of per-sheet ratios = target."""
    sheets = active_sheets(n6)
    total = Fraction(0)
    for (_, _, _, r) in sheets:
        if r is None:
            return False  # undefined ratio kills sum
        total += r
    return abs(total) == abs(target)


def rule_3_e_plus_p(n6, target):
    """(ratio_e) + (ratio_p), ignore ν ('paired off')."""
    sheets = active_sheets(n6)
    total = Fraction(0)
    for (s, _, _, r) in sheets:
        if s == "ν":
            continue
        if r is None:
            # if e or p has undefined ratio, rule fails
            return False
        total += r
    return abs(total) == abs(target)


def rule_4_parity(n6, target):
    """Current search rule: odd count of odd tube windings = spin ½."""
    n_et, _, n_nut, _, n_pt, _ = n6
    odd_count = (n_et % 2 != 0) + (n_nut % 2 != 0) + (n_pt % 2 != 0)
    is_odd = (odd_count % 2 == 1)
    return (target == Fraction(1, 2) and is_odd) or (target != Fraction(1, 2) and not is_odd)


def rule_5_vector_magnitude(n6, target):
    """spin = sqrt(s_e² + s_p² + s_ν²), with ratios as Cartesian components."""
    sheets = active_sheets(n6)
    mag_sq = Fraction(0)
    for (_, _, _, r) in sheets:
        if r is None:
            return False
        mag_sq += r * r
    # target² should equal mag_sq
    return target * target == mag_sq


def rule_6_linf_max(n6, target):
    """spin = max(|s_e|, |s_p|, |s_ν|)."""
    sheets = active_sheets(n6)
    max_abs = Fraction(0)
    for (_, _, _, r) in sheets:
        if r is None:
            return False
        if abs(r) > max_abs:
            max_abs = abs(r)
    return max_abs == abs(target)


def rule_7_unit_per_sheet(n6, target):
    """Each nonzero sheet contributes spin ½ (regardless of ratio); total
    spin is in the angular-momentum-addition set.  For k sheets, allowed
    spins are {0, 1, 2, ...} if k even, {1/2, 3/2, ...} if k odd."""
    sheets = active_sheets(n6)
    k = len(sheets)
    # Angular momentum addition of k spin-½'s: allowed spins are
    # {0, 1, ..., k/2} (stepping by 1) for even k, {1/2, 3/2, ..., k/2} for odd k
    if k == 0:
        return target == Fraction(0)
    if k % 2 == 0:
        # Even: integer spins 0 to k/2
        allowed = [Fraction(i) for i in range(k // 2 + 1)]
    else:
        # Odd: half-integer spins 1/2 to k/2
        allowed = [Fraction(2 * i + 1, 2) for i in range(k // 2 + 1)]
    return target in allowed or -target in allowed


def rule_8_total_winding(n6, target):
    """(Σ n_t) / (Σ n_r) = target spin."""
    n_et, n_er, n_nut, n_nur, n_pt, n_pr = n6
    total_nt = n_et + n_nut + n_pt
    total_nr = n_er + n_nur + n_pr
    if total_nr == 0:
        return False
    return Fraction(total_nt, total_nr) == target or Fraction(total_nt, total_nr) == -target


def rule_9_gcd_reduced(n6, target):
    """Per-sheet ratio (n_t/gcd)/(n_r/gcd) — under gcd reduction.  But
    gcd reduction doesn't change the ratio, so this is same as rule 2.
    Keep as separate entry for explicit documentation; same math as 2."""
    return rule_2_sum_all(n6, target)


def rule_10_integer_nulls_out(n6, target):
    """Integer ratios contribute 0; only fractional (|ratio| < 1 or
    non-integer) ratios sum."""
    sheets = active_sheets(n6)
    total = Fraction(0)
    for (_, _, _, r) in sheets:
        if r is None:
            continue  # skip undefined
        if r.denominator == 1:
            # integer
            continue
        total += r
    return abs(total) == abs(target)


def rule_11_fractional_sum(n6, target):
    """Σ (ratio mod 1), where mod 1 = fractional part in [0, 1).
    target matched if fractional_part(total) == target (mod 1)."""
    sheets = active_sheets(n6)
    total = Fraction(0)
    for (_, _, _, r) in sheets:
        if r is None:
            continue
        # r - floor(r) via Fraction arithmetic
        frac = r - Fraction(int(r) if r >= 0 else int(r) - (0 if r == int(r) else 1))
        total += frac
    # Normalize to [0, 1)
    total_int = int(total) if total >= 0 else int(total) - (0 if total == int(total) else 1)
    total_frac = total - Fraction(total_int)
    return total_frac == target or total_frac == Fraction(1) - abs(target)


def rule_12_tensor_product(n6, target):
    """Tensor-product composition: spin is in set of allowed values
    from angular-momentum addition of per-sheet half-integer-ified
    spins |s_a ⊗ s_b ⊗ s_c|.  Per-sheet 'spin' is the absolute ratio
    rounded to nearest half-integer (implementation: abs(ratio))."""
    sheets = active_sheets(n6)
    if not sheets:
        return target == Fraction(0)
    # Take per-sheet spin = |ratio|, treat as half-integer
    spins = []
    for (_, _, _, r) in sheets:
        if r is None:
            return False
        spins.append(abs(r))
    # Compose: start with first, add each next
    allowed = {spins[0]}
    for s in spins[1:]:
        new_allowed = set()
        for curr in allowed:
            lo = abs(curr - s)
            hi = curr + s
            # Step by 1 from lo to hi
            total = lo
            while total <= hi:
                new_allowed.add(total)
                total += 1
        allowed = new_allowed
    return abs(target) in allowed


RULES = [
    ("1. strict 7b per-sheet", rule_1_strict_per_sheet),
    ("2. sum-all ratios",      rule_2_sum_all),
    ("3. e+p additive (ν paired)", rule_3_e_plus_p),
    ("4. parity rule (current)", rule_4_parity),
    ("5. vector magnitude",    rule_5_vector_magnitude),
    ("6. L-∞ max",             rule_6_linf_max),
    ("7. unit-per-sheet AM add", rule_7_unit_per_sheet),
    ("8. total-winding ratio", rule_8_total_winding),
    ("9. gcd-reduced per-sheet", rule_9_gcd_reduced),
    ("10. integer-nulls-out",  rule_10_integer_nulls_out),
    ("11. fractional-sum mod 1", rule_11_fractional_sum),
    ("12. tensor-product",     rule_12_tensor_product),
]


def main():
    print("=" * 98)
    print("R60 Track 20 — Phases A+B: enumerate + audit spin rules")
    print("=" * 98)
    print()
    print(f"  {len(RULES)} candidate rules.  {len(MODEL_E_INVENTORY)} inventory particles.")
    print("  Apply each rule; mark pass/fail; tabulate per-rule pass counts.")
    print()

    # ── Per-particle per-rule grid ──
    print("─" * 98)
    print("  Per-particle per-rule audit (inventory = original model-E tuples):")
    print("─" * 98)
    print()

    # Header
    rule_nums = [lbl.split(".")[0] for lbl, _ in RULES]
    print(f"  {'particle':<10s}  {'tuple':<28s}  {'spin':>4s}  ", end="")
    for n in rule_nums:
        print(f"{n:>3s}", end="")
    print()
    print("  " + "-" * 98)

    rule_passes = [0] * len(RULES)
    for label, target_mass, Q, tup, _ in MODEL_E_INVENTORY:
        spin = OBSERVED_SPIN.get(label, None)
        if spin is None:
            continue
        tuple_str = str(tup).replace(" ", "")
        print(f"  {label:<10s}  {tuple_str:<28s}  {str(spin):>4s}  ", end="")
        for i, (rule_lbl, rule_fn) in enumerate(RULES):
            try:
                passes = rule_fn(tup, spin)
            except Exception:
                passes = False
            mark = " ✓ " if passes else " . "
            if passes:
                rule_passes[i] += 1
            print(f"{mark:>3s}", end="")
        print()
    print()

    # ── Summary ──
    print("─" * 98)
    print("  Per-rule pass counts (of 18 particles):")
    print("─" * 98)
    print()
    print(f"  {'Rule':<35s}  {'Passes':>8s}  {'Fraction':>10s}")
    print("  " + "-" * 60)
    total = len(OBSERVED_SPIN)
    ranking = sorted(enumerate(RULES), key=lambda x: -rule_passes[x[0]])
    for i, (rule_lbl, _) in ranking:
        count = rule_passes[i]
        frac = count / total
        bar = "█" * int(frac * 20)
        print(f"  {rule_lbl:<35s}  {count:>3d}/{total:>2d}  {frac:>9.0%}  {bar}")
    print()

    # ── Split: unit-charged and neutral analyzed separately ──
    print("─" * 98)
    print("  Split by particle class — unit-charged (likely spin ½):")
    print("─" * 98)
    print()
    unit_count = sum(1 for lbl in OBSERVED_SPIN if OBSERVED_SPIN[lbl] == Fraction(1, 2))
    neutral_zero = sum(1 for lbl in OBSERVED_SPIN if OBSERVED_SPIN[lbl] == Fraction(0))
    neutral_one = sum(1 for lbl in OBSERVED_SPIN if OBSERVED_SPIN[lbl] == Fraction(1))

    unit_particles = [(l, t, Q, tup) for l, t, Q, tup, _ in MODEL_E_INVENTORY
                      if OBSERVED_SPIN.get(l) == Fraction(1, 2)]
    print(f"  Unit-charged spin-½ particles: {len(unit_particles)}")
    print()

    # Per-rule pass on unit-charged spin-½
    rule_unit_passes = [0] * len(RULES)
    for label, target_mass, Q, tup in unit_particles:
        for i, (_, rule_fn) in enumerate(RULES):
            try:
                if rule_fn(tup, Fraction(1, 2)):
                    rule_unit_passes[i] += 1
            except Exception:
                pass

    print(f"  {'Rule':<35s}  {'Spin-½ passes':>15s}")
    print("  " + "-" * 55)
    ranking_unit = sorted(enumerate(RULES), key=lambda x: -rule_unit_passes[x[0]])
    for i, (rule_lbl, _) in ranking_unit:
        count = rule_unit_passes[i]
        print(f"  {rule_lbl:<35s}  {count:>3d}/{len(unit_particles):>2d}")
    print()

    # Per-rule pass on neutral spin-0
    neutral_0 = [(l, t, Q, tup) for l, t, Q, tup, _ in MODEL_E_INVENTORY
                 if OBSERVED_SPIN.get(l) == Fraction(0)]
    rule_n0_passes = [0] * len(RULES)
    for label, target_mass, Q, tup in neutral_0:
        for i, (_, rule_fn) in enumerate(RULES):
            try:
                if rule_fn(tup, Fraction(0)):
                    rule_n0_passes[i] += 1
            except Exception:
                pass
    print(f"  Neutral spin-0 particles: {len(neutral_0)}")
    print()
    print(f"  {'Rule':<35s}  {'Spin-0 passes':>15s}")
    print("  " + "-" * 55)
    ranking_n0 = sorted(enumerate(RULES), key=lambda x: -rule_n0_passes[x[0]])
    for i, (rule_lbl, _) in ranking_n0:
        count = rule_n0_passes[i]
        print(f"  {rule_lbl:<35s}  {count:>3d}/{len(neutral_0):>2d}")
    print()

    # Per-rule pass on neutral spin-1
    neutral_1 = [(l, t, Q, tup) for l, t, Q, tup, _ in MODEL_E_INVENTORY
                 if OBSERVED_SPIN.get(l) == Fraction(1)]
    rule_n1_passes = [0] * len(RULES)
    for label, target_mass, Q, tup in neutral_1:
        for i, (_, rule_fn) in enumerate(RULES):
            try:
                if rule_fn(tup, Fraction(1)):
                    rule_n1_passes[i] += 1
            except Exception:
                pass
    print(f"  Neutral spin-1 particles: {len(neutral_1)}")
    print()
    print(f"  {'Rule':<35s}  {'Spin-1 passes':>15s}")
    print("  " + "-" * 55)
    ranking_n1 = sorted(enumerate(RULES), key=lambda x: -rule_n1_passes[x[0]])
    for i, (rule_lbl, _) in ranking_n1:
        count = rule_n1_passes[i]
        print(f"  {rule_lbl:<35s}  {count:>3d}/{len(neutral_1):>2d}")
    print()

    # ── Consistency check — false-positive-free rules ──
    print("─" * 98)
    print("  Consistency check — rules that don't give FALSE POSITIVES:")
    print("─" * 98)
    print()
    print("  A rule is 'consistent' if it doesn't predict spin ½ for a spin-0")
    print("  particle (or vice versa).  A rule can FAIL (miss a spin ½) but")
    print("  still be consistent; it can't PASS a spin-0 as spin ½ and remain so.")
    print()
    # Check: for each rule, check if any spin-½ particle 'passes' rule(spin=0)
    # or any spin-0 particle 'passes' rule(spin=½)
    print(f"  {'Rule':<35s}  {'false_½_to_0':>12s}  {'false_0_to_½':>13s}")
    print("  " + "-" * 70)
    for i, (rule_lbl, rule_fn) in enumerate(RULES):
        false_pos_half_to_zero = 0
        false_pos_zero_to_half = 0
        for label, target_mass, Q, tup, _ in MODEL_E_INVENTORY:
            spin = OBSERVED_SPIN.get(label)
            if spin is None:
                continue
            try:
                if spin == Fraction(1, 2) and rule_fn(tup, Fraction(0)):
                    false_pos_half_to_zero += 1
                if spin == Fraction(0) and rule_fn(tup, Fraction(1, 2)):
                    false_pos_zero_to_half += 1
            except Exception:
                pass
        print(f"  {rule_lbl:<35s}  {false_pos_half_to_zero:>12d}  {false_pos_zero_to_half:>13d}")
    print()

    print("Phases A + B complete.")


if __name__ == "__main__":
    main()
