"""
R63 Track 6 Phase 6a: Q132 v2 per-sheet classification and compound-
charge check for the baseline inventory.

For each particle tuple, classify its winding pair on each sheet under
Q132 v2 (gcd-decomposition + phase-lock rule), compute the predicted
compound charge by summing per-sheet contributions, and compare to
observed charge.

Q132 v2 per-sheet classification:
  null          (0, 0)         no contribution
  ring-only     (0, p_r≠0)     neutral, ring-trapped photon
  tube-only     (p_t≠0, 0)     neutral, tube self-mass
  bright        (|p_t|=1,      one clean tube-2π closure with ring
                 p_r≠0)        at integer phase → charge fires
  dark-massive  (|p_t|>1,      ring off-phase at first tube closure
                 gcd=1)        → ω-sum cancels → Q = 0, mass only

Compound charge arithmetic (v2):
  Q_e (bright only)   = -p_t   (e-sheet convention, primitive charge)
  Q_ν                 =  0     (R60 T18 always)
  Q_p (bright only)   = +p_t   (p-sheet convention; Z₃ binding means
                                 three strands give one composite
                                 primitive-charge, not 3× strand-charge)
  Q_total = Q_e + Q_ν + Q_p

For each particle: pass if |Q_total| matches |Q_observed|.
Otherwise the tuple is a v2 re-derivation candidate (Phase 6b).

Inventory source: R60 Track 19 Phase 1b Z₃-filtered search.
"""

import csv
import math
from pathlib import Path


# ─── Inventory ────────────────────────────────────────────────────

# (name, tuple, |Q_observed|)
INVENTORY = [
    # Inputs (tuples chosen by calibration, not search)
    ("electron",   ( 1,  2,  0,  0,  0,  0), 1),
    ("proton",     ( 0,  0,  0,  0,  3,  6), 1),
    ("nu_1",       ( 0,  0,  1,  1,  0,  0), 0),
    # R60 T19 search results
    ("muon",       ( 1,  1, -2, -6,  0,  0), 1),
    ("tau",        (-5, -1, -2, -6, -6,  5), 1),
    ("neutron",    (-3, -6,  1, -6, -3, -6), 0),
    ("Lambda",     (-3,  2,  1, -6, -3, -3), 0),
    ("eta_prime",  ( 0, -6, -1, -6,  0, -6), 0),
    ("Sigma_-",    ( 4,  0, -2, -6,  3,  5), 1),
    ("Sigma_+",    ( 2, -3, -2, -6,  3,  6), 1),
    ("Xi_-",       (-2,  4,  0, -6, -3,  6), 1),
    ("phi",        (-3, -6,  1, -6, -3,  6), 0),
    ("Xi_0",       (-3,  2,  1, -6, -3,  6), 0),
    ("rho",        (-3, -6,  1, -6, -3,  3), 0),
    ("K0",         ( 0, -1, -1, -6,  0, -4), 0),
    ("K_pm",       ( 1,  3, -2, -6,  0, -4), 1),
    ("eta",        ( 0, -4, -1, -6,  0, -3), 0),
    ("pi0",        ( 0,  0, -1, -6,  0, -1), 0),
    ("pi_pm",      ( 1,  2, -2, -6,  0, -1), 1),
]


# ─── v2 classifier ────────────────────────────────────────────────

def gcd_primitive(n_t, n_r):
    """Return (k, p_t, p_r) with original = k × primitive, gcd(p_t, p_r) = 1."""
    if n_t == 0 and n_r == 0:
        return (0, 0, 0)
    k = math.gcd(abs(n_t), abs(n_r))
    return (k, n_t // k, n_r // k)


def classify_sheet_v2(n_t, n_r):
    """Return (category, k, p_t, p_r)."""
    if n_t == 0 and n_r == 0:
        return ("null", 0, 0, 0)
    k, p_t, p_r = gcd_primitive(n_t, n_r)
    if p_t == 0:
        return ("ring-only", k, 0, p_r)
    if p_r == 0:
        return ("tube-only", k, p_t, 0)
    if abs(p_t) == 1:
        return ("bright", k, p_t, p_r)
    return ("dark-massive", k, p_t, p_r)


def sheet_charge_v2(sheet, category, p_t):
    """Charge contribution from one sheet under v2.

    Sign conventions:
      e-sheet:  bright contributes -p_t (electron (1,2) → -1)
      p-sheet:  bright contributes +p_t (proton (3,6) primitive (1,2) → +1)
      ν-sheet:  always 0 (R60 T18 real-field conjugate pairing)
    All non-bright categories contribute 0.
    """
    if category != "bright":
        return 0
    if sheet == "e":
        return -p_t
    if sheet == "p":
        return +p_t
    if sheet == "nu":
        return 0  # T18
    raise ValueError(f"unknown sheet {sheet}")


def analyze_particle(name, tup, absQ_obs):
    n_et, n_er, n_νt, n_νr, n_pt, n_pr = tup
    cls_e  = classify_sheet_v2(n_et, n_er)
    cls_nu = classify_sheet_v2(n_νt, n_νr)
    cls_p  = classify_sheet_v2(n_pt, n_pr)

    Q_e  = sheet_charge_v2("e",  cls_e[0],  cls_e[2])
    Q_nu = sheet_charge_v2("nu", cls_nu[0], cls_nu[2])
    Q_p  = sheet_charge_v2("p",  cls_p[0],  cls_p[2])
    Q_total = Q_e + Q_nu + Q_p
    absQ_pred = abs(Q_total)

    verdict = "pass" if absQ_pred == absQ_obs else "re-derive"

    return {
        "name": name,
        "tuple": tup,
        "absQ_observed": absQ_obs,
        "e_sheet": cls_e,
        "nu_sheet": cls_nu,
        "p_sheet": cls_p,
        "Q_e": Q_e, "Q_nu": Q_nu, "Q_p": Q_p,
        "Q_predicted": Q_total,
        "absQ_predicted": absQ_pred,
        "verdict": verdict,
    }


# ─── Main ─────────────────────────────────────────────────────────

def category_short(cat, k, p_t, p_r):
    if cat == "null":         return "null"
    if cat == "ring-only":    return f"ring({k}×{p_r:+d})"
    if cat == "tube-only":    return f"tube({k}×{p_t:+d})"
    if cat == "bright":       return f"BRIGHT({k}×{p_t:+d},{p_r:+d})"
    if cat == "dark-massive": return f"dark({p_t:+d},{p_r:+d})"
    return cat


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    results = []
    for name, tup, absQ_obs in INVENTORY:
        r = analyze_particle(name, tup, absQ_obs)
        results.append(r)

    # Print table
    print("=" * 118)
    print("R63 Track 6 Phase 6a — Q132 v2 compatibility check")
    print("=" * 118)
    print()
    print(f"  {'particle':<10}  {'e-sheet':<22}  {'nu-sheet':<22}  {'p-sheet':<20}  "
          f"{'Q_e':>3}  {'Q_ν':>3}  {'Q_p':>3}  {'Q':>3}  {'|Q_obs|':>7}  {'verdict':<10}")
    print("  " + "─" * 130)

    n_pass = n_fail = 0
    for r in results:
        e_s = category_short(*r["e_sheet"])
        nu_s = category_short(*r["nu_sheet"])
        p_s = category_short(*r["p_sheet"])
        print(f"  {r['name']:<10}  {e_s:<22}  {nu_s:<22}  {p_s:<20}  "
              f"{r['Q_e']:>+3d}  {r['Q_nu']:>+3d}  {r['Q_p']:>+3d}  "
              f"{r['Q_predicted']:>+3d}  {r['absQ_observed']:>7d}  {r['verdict']:<10}")
        if r["verdict"] == "pass":
            n_pass += 1
        else:
            n_fail += 1
    print("  " + "─" * 130)
    print(f"  Pass: {n_pass} / {len(results)}    Re-derive: {n_fail} / {len(results)}")
    print()

    # Flag re-derivation targets
    failing = [r for r in results if r["verdict"] == "re-derive"]
    if failing:
        print("  Re-derivation candidates for Phase 6b:")
        for r in failing:
            tup_str = ",".join(str(x) for x in r["tuple"])
            print(f"    {r['name']:<10}  tuple=({tup_str})  "
                  f"|Q_obs|={r['absQ_observed']}  predicted Q={r['Q_predicted']:+d}")
        print()

    # CSV
    csv_path = out_dir / "track6_phase6a_v2.csv"
    fieldnames = [
        "particle", "n_et", "n_er", "n_nut", "n_nur", "n_pt", "n_pr",
        "e_category", "e_k", "e_p_t", "e_p_r",
        "nu_category", "nu_k", "nu_p_t", "nu_p_r",
        "p_category", "p_k", "p_p_t", "p_p_r",
        "Q_e", "Q_nu", "Q_p", "Q_predicted",
        "absQ_observed", "verdict",
    ]
    with open(csv_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in results:
            n_et, n_er, n_nut, n_nur, n_pt, n_pr = r["tuple"]
            w.writerow({
                "particle": r["name"],
                "n_et": n_et, "n_er": n_er,
                "n_nut": n_nut, "n_nur": n_nur,
                "n_pt": n_pt, "n_pr": n_pr,
                "e_category": r["e_sheet"][0],
                "e_k": r["e_sheet"][1],
                "e_p_t": r["e_sheet"][2],
                "e_p_r": r["e_sheet"][3],
                "nu_category": r["nu_sheet"][0],
                "nu_k": r["nu_sheet"][1],
                "nu_p_t": r["nu_sheet"][2],
                "nu_p_r": r["nu_sheet"][3],
                "p_category": r["p_sheet"][0],
                "p_k": r["p_sheet"][1],
                "p_p_t": r["p_sheet"][2],
                "p_p_r": r["p_sheet"][3],
                "Q_e": r["Q_e"],
                "Q_nu": r["Q_nu"],
                "Q_p": r["Q_p"],
                "Q_predicted": r["Q_predicted"],
                "absQ_observed": r["absQ_observed"],
                "verdict": r["verdict"],
            })
    print(f"  CSV: {csv_path}")
    return results


if __name__ == "__main__":
    main()
