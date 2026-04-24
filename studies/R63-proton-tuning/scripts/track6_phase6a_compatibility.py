"""
R63 Track 6 Phase 6A: Per-sheet Q132 compatibility of the observed inventory.

Classifies each baseline-inventory 6-tuple on each sheet independently
under Q132 (promotion-chain principle).  Ratio-independent: only the
winding integers enter.

Per-sheet classification cells:
  null            (0, 0)           -- no contribution from this sheet
  ring-only       (0, n_r != 0)    -- valid neutral particle
  tube-only       (+/-1, 0)        -- valid neutral particle (tube self-mass)
  charged         (+/-1, n_r != 0) -- valid charged particle

Multi-event cases (|n_t| >= 2) require a binding mechanism:
  e-sheet:   no known mechanism -> Q132-FORBIDDEN if |n_et| >= 2
  nu-sheet:  R60 T18 (real-field conjugate pairing) zeros charge;
             whether it allows |n_nut| >= 2 as a paired bound state is
             an OPEN STRUCTURAL QUESTION.  Flag but do not dismiss.
  p-sheet:   Z3 confinement binds three n_pt = +/-1 events into a color
             singlet.  Allowed: |n_pt| in {3, 6, 9, ...} (n_pt ~= 0 mod 3).
             Forbidden: |n_pt| in {2, 4, 5, 7, 8, ...}.

Inventory source: R60 Track 19 Phase 1b Z3-filtered inventory
(studies/R60-metric-11/findings-19.md, F110).
"""

import csv
from pathlib import Path


# R60 Track 19 Phase 1b Z3-compatible inventory (model-F baseline).
# electron, proton, nu_1 are inputs (not searched).  Other 16 are
# the Z3-filtered best matches for each observed particle.
INVENTORY = [
    # name,        (n_et, n_er, n_nut, n_nur, n_pt, n_pr)
    ("electron",   ( 1,  2,  0,  0,  0,  0)),
    ("proton",     ( 0,  0,  0,  0,  3,  6)),
    ("nu_1",       ( 0,  0,  1,  1,  0,  0)),
    ("muon",       ( 1,  1, -2, -6,  0,  0)),
    ("tau",        (-5, -1, -2, -6, -6,  5)),
    ("neutron",    (-3, -6,  1, -6, -3, -6)),
    ("Lambda",     (-3,  2,  1, -6, -3, -3)),
    ("eta_prime",  ( 0, -6, -1, -6,  0, -6)),
    ("Sigma_-",    ( 4,  0, -2, -6,  3,  5)),
    ("Sigma_+",    ( 2, -3, -2, -6,  3,  6)),
    ("Xi_-",       (-2,  4,  0, -6, -3,  6)),
    ("phi",        (-3, -6,  1, -6, -3,  6)),
    ("Xi_0",       (-3,  2,  1, -6, -3,  6)),
    ("rho",        (-3, -6,  1, -6, -3,  3)),
    ("K0",         ( 0, -1, -1, -6,  0, -4)),
    ("K_pm",       ( 1,  3, -2, -6,  0, -4)),
    ("eta",        ( 0, -4, -1, -6,  0, -3)),
    ("pi0",        ( 0,  0, -1, -6,  0, -1)),
    ("pi_pm",      ( 1,  2, -2, -6,  0, -1)),
]


def classify_sheet(n_t, n_r, sheet):
    """
    Classify a single-sheet winding pair under per-sheet Q132.
    Returns (status, detail) where status is one of:
      'null'          -- (0, 0) no contribution
      'ring-only'     -- valid neutral, ring-trapped
      'tube-only'     -- valid neutral, tube self-mass
      'charged'       -- valid charged
      'z3-baryon'     -- p-sheet multi-event bound by Z3 (n_pt in {+/-3, +/-6,..})
      'nu-paired?'    -- nu-sheet |n_nut| >= 2 pending R60 T18 structural check
      'forbidden'     -- Q132-incompatible (no known binding mechanism)
    """
    at = abs(n_t)
    if at == 0 and n_r == 0:
        return ("null", "no activity")
    if at == 0:
        return ("ring-only", f"neutral, n_r={n_r}")
    if at == 1 and n_r == 0:
        return ("tube-only", f"neutral self-mass, n_t={n_t}")
    if at == 1:
        return ("charged", f"Q={-n_t}, n_r={n_r}")

    # |n_t| >= 2: needs a binding mechanism
    if sheet == "p":
        if at % 3 == 0:
            k = at // 3
            return ("z3-baryon", f"{k}-baryon (|n_pt|={at}); Z3 binds 3 events per baryon")
        else:
            return ("forbidden", f"|n_pt|={at} not 0 mod 3: not Z3-bindable")
    if sheet == "nu":
        # Open structural question: does R60 T18 real-field pairing allow
        # |n_nut| >= 2 as paired bound state?  Even |n_nut| is at least
        # conjugate-symmetric; odd |n_nut| >= 3 looks harder.
        if at % 2 == 0:
            return ("nu-paired?",
                    f"|n_nut|={at} even; pending R60 T18 pairing interpretation")
        else:
            return ("forbidden",
                    f"|n_nut|={at} odd; no known binding mechanism")
    # e-sheet: no known binding mechanism
    return ("forbidden", f"|n_et|={at}, no known binding mechanism on e-sheet")


def verdict(e_status, nu_status, p_status):
    """Overall Q132 compatibility verdict for a particle."""
    statuses = [e_status, nu_status, p_status]
    if "forbidden" in statuses:
        return "incompatible"
    if "nu-paired?" in statuses:
        return "conditional (nu pairing)"
    if "z3-baryon" in statuses:
        return "baryon (Z3-composite)"
    return "compatible"


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    rows = []
    counts = {"compatible": 0,
              "baryon (Z3-composite)": 0,
              "conditional (nu pairing)": 0,
              "incompatible": 0}

    print(f"{'particle':<12} {'e-sheet':<20} {'nu-sheet':<22} {'p-sheet':<22} verdict")
    print("-" * 110)

    for name, tup in INVENTORY:
        n_et, n_er, n_nut, n_nur, n_pt, n_pr = tup
        e_s = classify_sheet(n_et, n_er, "e")
        nu_s = classify_sheet(n_nut, n_nur, "nu")
        p_s = classify_sheet(n_pt, n_pr, "p")
        v = verdict(e_s[0], nu_s[0], p_s[0])
        counts[v] += 1
        print(f"{name:<12} {e_s[0]:<20} {nu_s[0]:<22} {p_s[0]:<22} {v}")
        rows.append({
            "particle": name,
            "n_et": n_et, "n_er": n_er,
            "n_nut": n_nut, "n_nur": n_nur,
            "n_pt": n_pt, "n_pr": n_pr,
            "e_sheet_status": e_s[0], "e_sheet_detail": e_s[1],
            "nu_sheet_status": nu_s[0], "nu_sheet_detail": nu_s[1],
            "p_sheet_status": p_s[0], "p_sheet_detail": p_s[1],
            "verdict": v,
        })

    print("-" * 110)
    print(f"Total: {len(rows)}")
    for v, c in counts.items():
        print(f"  {v}: {c}")

    csv_path = out_dir / "track6_compatibility_matrix.csv"
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    print(f"\nCSV written: {csv_path}")

    return rows, counts


if __name__ == "__main__":
    main()
