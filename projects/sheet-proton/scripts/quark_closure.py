"""
Path-closure and charge-closure analysis for quark combinations on the
corrugated clover torus.

For an arbitrary multiset of quarks (and antiquarks), compute:

  1. The total path arc Δφ_path on the cross-section profile
  2. The smallest (n_t, n_r) path-winding pair that closes the path on the
     surface, given the τ = 1/3 twist:
        Δφ_path = 2π · n_t + (2π/3) · n_r
  3. The total electric charge Q = Σ q_i
  4. Whether the combination is **charge-closed** (Q ∈ ℤ → observable
     baryon/meson candidate) or **fractional** (confined fragment)
  5. If fractional: the smallest integer k such that placing k linear
     copies of the combination end-to-end yields integer total charge

Quark properties (clover-quarks.md §0.6, §11.7):

  Quark   Arc (radians)   Charge (per radian-integral)
  u       4π/3 (one lobe, 240°)        +2/3
  d       2π/3 (one saddle, 120°)      −1/3
  ū       4π/3 (one lobe, reversed)    −2/3
  d̄       2π/3 (one saddle, reversed)  +1/3

  (s, c, b, t are identified in Phase 3; not yet supported here.)

Per AGENTS.md:
  - Combinations are parameterized via the --combo CLI flag
  - All outputs go to outputs/ as CSV (filename encodes the inputs)
  - The script reuses no other infrastructure; closed-form arithmetic only.

Usage:

    python scripts/quark_closure.py --combo uud
    python scripts/quark_closure.py --combo uud,udd,uuu,ddd,u,ud,uū
    python scripts/quark_closure.py --combo "uud,udd" --csv-out

Single-combo mode prints a human-readable report. Multi-combo mode prints a
table summary. With --csv-out, results also save to outputs/.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd
from pathlib import Path


# ---- Quark inventory ----

# (arc_in_units_of_2pi/3, charge_as_Fraction)
# arc unit choice: 2π/3 (= saddle arc length). One lobe = 2 units, one saddle = 1 unit.
QUARKS = {
    "u":  {"arc_units": 2, "charge": Fraction(2, 3), "kind": "lobe"},
    "d":  {"arc_units": 1, "charge": Fraction(-1, 3), "kind": "saddle"},
    "U":  {"arc_units": 2, "charge": Fraction(-2, 3), "kind": "lobe", "anti": True},   # ū
    "D":  {"arc_units": 1, "charge": Fraction(1, 3), "kind": "saddle", "anti": True},  # d̄
}

# User-friendly aliases. Unicode antiquark labels map to capitalized ASCII for parsing.
ALIASES = {
    "ū":  "U",
    "d̄":  "D",
    "ub": "U",  # "u-bar" alternate spelling
    "db": "D",
}


def parse_combo(combo: str) -> list:
    """Parse a string like 'uud' or 'u,u,d' or 'uūd' into a list of quark keys."""
    s = combo.strip()
    # Apply unicode/two-letter aliases first
    for alias, key in ALIASES.items():
        s = s.replace(alias, key)
    # Strip separators
    for sep in [",", " ", "+"]:
        s = s.replace(sep, "")
    if not s:
        raise ValueError(f"Empty quark combination: '{combo}'")
    result = []
    for ch in s:
        if ch not in QUARKS:
            raise ValueError(f"Unknown quark label '{ch}' in '{combo}'. "
                             f"Known: {list(QUARKS.keys())}")
        result.append(ch)
    return result


# ---- Path-closure on the corrugated torus ----

def path_closure(arc_units_total: int) -> tuple:
    """Find the smallest non-negative integer (n_t, n_r) satisfying

        arc_units_total = 3 · n_t + n_r

    (which is Δφ_path = 2π · n_t + (2π/3) · n_r divided by 2π/3).
    Prefer the solution with smallest n_t such that n_t ≥ 1; if none, fall back
    to n_t = 0.

    Returns (n_t, n_r). For arc_units_total > 0 the solution is always integer-valued
    because each quark contributes an integer number of saddle-units.
    """
    if arc_units_total <= 0:
        return (0, 0)
    # Solutions: n_r = arc_units_total - 3 · n_t, with n_r ≥ 0
    # → n_t ranges from 0 to arc_units_total // 3
    # Prefer the largest n_t (smallest n_r ≥ 0). If we want the "n_t ≥ 1" minimal-pair,
    # we pick the largest n_t such that n_r ≥ 0.
    n_t_max = arc_units_total // 3
    if n_t_max >= 1:
        n_t = n_t_max
        n_r = arc_units_total - 3 * n_t
    else:
        n_t = 0
        n_r = arc_units_total
    return (n_t, n_r)


# ---- Charge-closure (integerality) ----

def charge_closure_multiplicity(charge: Fraction) -> int:
    """Smallest positive integer k such that k · charge is an integer.

    For a Fraction p/q in lowest terms, the answer is |q|. If the input is
    already integer, returns 1.
    """
    return charge.denominator  # Fraction is always in lowest terms


# ---- Aggregate a quark multiset ----

def analyse(combo_str: str) -> dict:
    """Return a dictionary of derived properties for a quark combination."""
    quarks = parse_combo(combo_str)
    arc_units = sum(QUARKS[q]["arc_units"] for q in quarks)
    charge = sum((QUARKS[q]["charge"] for q in quarks), Fraction(0))
    n_t, n_r = path_closure(arc_units)
    k_close = charge_closure_multiplicity(charge)
    is_integer_charge = (charge.denominator == 1)
    # Composition counts for reporting
    counts = {label: quarks.count(label) for label in sorted(set(quarks))}
    return {
        "combo": combo_str,
        "parsed": quarks,
        "counts": counts,
        "arc_units": arc_units,                       # in saddle-arc units (each = 2π/3 = 120°)
        "arc_degrees": arc_units * 120,               # equivalent in degrees
        "path_closure": (n_t, n_r),
        "total_charge": charge,
        "is_integer_charge": is_integer_charge,
        "copies_to_charge_close": k_close,
        "closed_charge_after_k": k_close * charge,
    }


def format_quark_string(parsed: list) -> str:
    """Pretty-print a list of quark keys back into a label like 'uud' (with bars)."""
    out = ""
    for q in parsed:
        if q == "U":
            out += "ū"
        elif q == "D":
            out += "d̄"
        else:
            out += q
    return out


def report_single(result: dict) -> str:
    lines = []
    lines.append(f"Combo: {format_quark_string(result['parsed'])}  (parsed as {result['counts']})")
    lines.append(f"  Total profile arc:    {result['arc_units']} × (2π/3) = "
                 f"{result['arc_degrees']}° of profile arc")
    n_t, n_r = result["path_closure"]
    lines.append(f"  Path closes at:       (n_t, n_r) = ({n_t}, {n_r})  "
                 f"— {n_t} tube turn{'s' if n_t != 1 else ''}, "
                 f"{n_r} ring revolution{'s' if n_r != 1 else ''}")
    q = result["total_charge"]
    if q.denominator == 1:
        lines.append(f"  Total charge:         Q = {q}  (integer → charge-closed; "
                     f"observable particle candidate)")
        lines.append(f"  Copies to close:      k = 1 (already closed)")
    else:
        lines.append(f"  Total charge:         Q = {q} = {float(q):+.4f}  "
                     f"(fractional → confined fragment)")
        k = result["copies_to_charge_close"]
        kq = result["closed_charge_after_k"]
        lines.append(f"  Copies to close:      k = {k}  (k × Q = {kq}, integer)")
    return "\n".join(lines)


def report_table(results: list) -> str:
    """Tabular summary across multiple combinations."""
    header = (
        f"{'combo':>10}  {'arc° ':>6}  {'(n_t, n_r)':>10}  "
        f"{'Q':>8}  {'integer?':>9}  {'k copies':>9}  {'k·Q':>6}"
    )
    sep = "-" * len(header)
    rows = [header, sep]
    for r in results:
        q = r["total_charge"]
        qstr = str(q) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"
        kqstr = str(r['closed_charge_after_k'])
        nt, nr = r["path_closure"]
        rows.append(
            f"{format_quark_string(r['parsed']):>10}  "
            f"{r['arc_degrees']:>6d}  "
            f"({nt:>2d}, {nr:>2d})  "
            f"{qstr:>8}  "
            f"{'yes' if r['is_integer_charge'] else 'no':>9}  "
            f"{r['copies_to_charge_close']:>9d}  "
            f"{kqstr:>6}"
        )
    return "\n".join(rows)


# ---- CLI ----

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--combo",
        type=str,
        default="uud",
        help="Quark combination(s). Single: 'uud'. Multiple (comma-separated): "
        "'uud,udd,uuu,ddd,u,ud,uū'. Letters u,d for quarks; ū (or U or 'ub') "
        "and d̄ (or D or 'db') for antiquarks. Default: 'uud'.",
    )
    parser.add_argument(
        "--csv-out",
        action="store_true",
        help="Write a CSV summary to outputs/quark_closure_<combos>.csv",
    )
    parser.add_argument(
        "--outputs-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "outputs",
    )
    args = parser.parse_args()

    combos = [c.strip() for c in args.combo.split(",") if c.strip()]

    results = [analyse(c) for c in combos]

    if len(results) == 1:
        print(report_single(results[0]))
    else:
        print(report_table(results))

    if args.csv_out:
        args.outputs_dir.mkdir(parents=True, exist_ok=True)
        safe = "_".join(format_quark_string(r["parsed"]).replace("ū", "ub").replace("d̄", "db")
                        for r in results)
        csv_path = args.outputs_dir / f"quark_closure_{safe}.csv"
        with open(csv_path, "w") as f:
            f.write("combo,arc_degrees,n_t,n_r,charge,charge_decimal,"
                    "is_integer_charge,copies_to_close,charge_after_k_copies\n")
            for r in results:
                q = r["total_charge"]
                f.write(
                    f"{format_quark_string(r['parsed'])},"
                    f"{r['arc_degrees']},"
                    f"{r['path_closure'][0]},{r['path_closure'][1]},"
                    f"{q.numerator}/{q.denominator},{float(q):.6f},"
                    f"{int(r['is_integer_charge'])},"
                    f"{r['copies_to_charge_close']},"
                    f"{r['closed_charge_after_k']}\n"
                )
        print(f"\nSaved: {csv_path}")


if __name__ == "__main__":
    main()
