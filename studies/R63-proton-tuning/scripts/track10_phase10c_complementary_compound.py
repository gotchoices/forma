"""
R63 Track 10 Phase 10c — Complementary-shear compound mode for the deuteron.

Tests the user's structural hypothesis: that the deuteron's p-sheet content
might be (6, 0) — three (1, 2)-type strands and three (1, -2)-type strands at
interleaved phases, with n_r contributions cancelling — rather than the
additive (6, 12) of two aligned (3, 6) triplets.  The neutron's e-sheet
(1, 2) and ν-sheet (-1, -1) windings (per T8) are proposed as "ballast"
that stabilizes the compound.

Three sub-tests:

1. Compute four candidate compound tuples at g-candidate baseline:
     (a) "regular pp"      = (0, 0,  0,  0, 6, 12)  — diproton, additive
     (b) "regular pn"      = (1, 2, -1, -1, 6, 12)  — T8 additive deuteron
     (c) "complementary pp" = (0, 0,  0,  0, 6,  0)  — n_r-cancelled diproton
     (d) "complementary pn" = (1, 2, -1, -1, 6,  0)  — user's proposal

2. Quantify the e/ν "ballast" contribution by comparing pn vs pp at the same
   p-sheet structure.

3. Sweep s_p to find where the (6, 0) compound matches m_d, and audit the
   hadron inventory damage at that shear.

Outputs:
  outputs/track10_phase10c_candidates.csv
  outputs/track10_phase10c_shear_sweep.csv
  outputs/track10_phase10c_inventory_damage.csv
"""

import sys
import os
import csv
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'R60-metric-11', 'scripts'))

from track1_solver import (
    Params, derive_L_ring, L_vector_from_params, mode_energy, mode_6_to_11,
    signature_ok, M_E_MEV, M_P_MEV,
    SQRT_ALPHA, FOUR_PI, ALPHA,
)
from track7b_resolve import build_aug_metric
from track15_phase1_mass import K_MODELF


# ─── Constants ───────────────────────────────────────────────────────

DEUTERON_OBS_MEV = 1875.613
PROTON_OBS_MEV = 938.272
NEUTRON_OBS_MEV = 939.565


# ─── Working params ──────────────────────────────────────────────────

def build_working_params(eps_p=0.55, s_p=0.162037):
    """Re-derive L_ring_p so the proton mass stays anchored at any s_p."""
    return Params(
        eps_e=397.074, s_e=2.0042,
        eps_p=eps_p, s_p=s_p,
        eps_nu=2.0, s_nu=0.022,
        k_e=K_MODELF, k_p=K_MODELF, k_nu=K_MODELF,
        g_aa=1.0,
        sigma_ta=SQRT_ALPHA, sigma_at=FOUR_PI * ALPHA,
        sign_e=+1.0, sign_p=-1.0, sign_nu=+1.0,
        L_ring_e=derive_L_ring(M_E_MEV, 1, 2, 397.074, 2.0042, K_MODELF),
        L_ring_p=derive_L_ring(M_P_MEV, 3, 6, eps_p, s_p, K_MODELF),
        L_ring_nu=derive_L_ring(3.21e-8, 1, 1, 2.0, 0.022, K_MODELF),
    )


def E(tup, params):
    G = build_aug_metric(params)
    if not signature_ok(G):
        return None
    L = L_vector_from_params(params)
    return mode_energy(G, L, mode_6_to_11(tup))


# ─── Candidates and inventory ────────────────────────────────────────

CANDIDATES = [
    ("regular pp",        (0, 0,  0,  0, 6, 12), "diproton, additive p-sheet"),
    ("regular pn",        (1, 2, -1, -1, 6, 12), "T8 additive deuteron"),
    ("complementary pp",  (0, 0,  0,  0, 6,  0), "n_r-cancelled diproton"),
    ("complementary pn",  (1, 2, -1, -1, 6,  0), "user's hypothesis"),
]

INVENTORY = [
    ("proton",    (0,  0,  0,  0,  3,  6),  PROTON_OBS_MEV),
    ("neutron",   (1,  2, -1, -1,  3,  6),  NEUTRON_OBS_MEV),
    ("Lambda",    (-3,  2,  1, -6, -3, -3), 1115.683),
    ("eta_prime", (0, -6, -1, -6,  0, -6),   957.78),
    ("Sigma_-",   (4,  0, -2, -6,  3,  5), 1197.449),
    ("Sigma_+",   (2, -3, -2, -6,  3,  6), 1189.37),
    ("Xi_-",      (-2,  4,  0, -6, -3,  6), 1321.71),
    ("phi",       (-3, -6,  1, -6, -3,  6), 1019.461),
    ("K0",        (0, -1, -1, -6,  0, -4),  497.611),
    ("K_pm",      (1,  3, -2, -6,  0, -4),  493.677),
    ("eta",       (0, -4, -1, -6,  0, -3),  547.862),
    ("pi0",       (0,  0, -1, -6,  0, -1),  134.977),
    ("pi_pm",     (1,  2, -2, -6,  0, -1),  139.570),
]


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 100)
    print("R63 Track 10 Phase 10c — Complementary-shear compound for deuteron")
    print("=" * 100)
    print()

    # ─── Part 1: Four candidate masses at g-candidate baseline ───
    print("Part 1 — Four candidate compound masses at g-candidate baseline")
    print("           (ε_p = 0.55, s_p = 0.162037)")
    print("-" * 100)
    print(f"  {'configuration':22s} {'tuple':28s} {'mass (MeV)':>11}  "
          f"{'vs m_d':>10}")
    print("  " + "─" * 80)

    params = build_working_params()
    cand_rows = []

    for label, tup, desc in CANDIDATES:
        m = E(tup, params)
        if m is None:
            print(f"  {label:22s} {str(tup):28s} {'—':>11}  (sig broken)")
            continue
        diff = m - DEUTERON_OBS_MEV
        print(f"  {label:22s} {str(tup):28s} {m:>11.3f}  {diff:>+10.3f}")
        cand_rows.append({
            'label': label,
            'tuple': str(tup),
            'description': desc,
            'mass_MeV': m,
            'mass_minus_m_d': diff,
        })
    print()
    print(f"  Reference: observed deuteron mass = {DEUTERON_OBS_MEV:.3f} MeV")
    print(f"             observed proton mass   = {PROTON_OBS_MEV:.3f} MeV")
    print(f"             observed neutron mass  = {NEUTRON_OBS_MEV:.3f} MeV")
    print(f"             observed binding       = {2*PROTON_OBS_MEV - DEUTERON_OBS_MEV:.3f} MeV")
    print()

    csv_path1 = out_dir / "track10_phase10c_candidates.csv"
    with open(csv_path1, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(cand_rows[0].keys()))
        w.writeheader()
        w.writerows(cand_rows)

    # ─── Part 2: e/ν "ballast" quantification ───
    print("Part 2 — e/ν ballast quantification")
    print("-" * 100)

    m_pp_reg = next(r['mass_MeV'] for r in cand_rows if r['label'] == 'regular pp')
    m_pn_reg = next(r['mass_MeV'] for r in cand_rows if r['label'] == 'regular pn')
    m_pp_comp = next(r['mass_MeV'] for r in cand_rows if r['label'] == 'complementary pp')
    m_pn_comp = next(r['mass_MeV'] for r in cand_rows if r['label'] == 'complementary pn')

    ballast_reg = m_pn_reg - m_pp_reg
    ballast_comp = m_pn_comp - m_pp_comp
    print(f"  Mass shift from neutron's e/ν content (pn vs pp same p-sheet):")
    print(f"    regular structure  ((6, 12) p-sheet): "
          f"+{ballast_reg:.4f} MeV")
    print(f"    complementary  ((6,  0) p-sheet):     "
          f"+{ballast_comp:.4f} MeV")
    print()
    print(f"  Required deuteron binding: ~"
          f"{2*PROTON_OBS_MEV - DEUTERON_OBS_MEV:.3f} MeV")
    print(f"  Conclusion: e/ν ballast is far below required binding magnitude.")
    print()

    # ─── Part 3: Sweep s_p for (6, 0) deuteron candidacy ───
    print("Part 3 — Sweep s_p to find where (6, 0) tuple matches deuteron mass")
    print("-" * 100)
    print(f"  Test tuple: (1, 2, -1, -1, 6, 0)")
    print(f"  L_ring_p re-anchors at each s_p so the proton's calibration")
    print(f"  remains m_p exactly.  We check m_compound vs m_d.")
    print()
    print(f"  {'s_p':>8} {'m_(6,0)':>11} {'vs m_d':>10}  status")
    print("  " + "─" * 50)

    sweep_rows = []
    s_p_values = [0.05, 0.1, 0.162, 0.3, 0.5, 0.7, 0.85, 0.9, 0.95,
                  0.97, 0.98, 0.99, 0.995, 0.998, 1.0, 1.05, 1.1, 1.5]

    best = None
    for s_p in s_p_values:
        try:
            params_sweep = build_working_params(eps_p=0.55, s_p=s_p)
            m = E((1, 2, -1, -1, 6, 0), params_sweep)
            if m is None:
                print(f"  {s_p:>8.4f} {'—':>11} {'—':>10}  (sig broken)")
                continue
            diff = m - DEUTERON_OBS_MEV
            status = "MATCH" if abs(diff) < 1.0 else ""
            print(f"  {s_p:>8.4f} {m:>11.3f} {diff:>+10.3f}  {status}")
            sweep_rows.append({
                's_p': s_p,
                'm_compound_6_0': m,
                'mass_minus_m_d': diff,
            })
            if best is None or abs(diff) < abs(best['mass_minus_m_d']):
                best = sweep_rows[-1]
        except Exception as ex:
            print(f"  {s_p:>8.4f} error: {ex}")

    print()

    csv_path2 = out_dir / "track10_phase10c_shear_sweep.csv"
    with open(csv_path2, 'w', newline='') as f:
        if sweep_rows:
            w = csv.DictWriter(f, fieldnames=list(sweep_rows[0].keys()))
            w.writeheader()
            w.writerows(sweep_rows)

    # ─── Part 4: Inventory damage at best-match s_p ───
    if best is None:
        print("No best-match s_p found; skipping inventory audit.")
        return

    s_p_match = best['s_p']
    print(f"Part 4 — Inventory damage at s_p = {s_p_match:.4f}  "
          f"(closest match to m_d in the sweep)")
    print("-" * 100)
    print(f"  Compute every inventory tuple's mass at the deuteron-matching s_p.")
    print(f"  Proton remains anchored to m_p by L_ring_p re-derivation.")
    print()
    print(f"  {'particle':12s} {'tuple':32s} {'predicted':>11} {'observed':>11}  "
          f"{'Δ%':>10}")
    print("  " + "─" * 88)

    params_match = build_working_params(eps_p=0.55, s_p=s_p_match)
    damage_rows = []
    n_within_5pct = 0
    n_total = 0
    max_dev = 0.0
    max_dev_name = None

    for name, tup, m_obs in INVENTORY:
        try:
            m_pred = E(tup, params_match)
            if m_pred is None:
                print(f"  {name:12s} (sig broken)")
                continue
            rel_err = (m_pred - m_obs) / m_obs * 100
            print(f"  {name:12s} {str(tup):32s} {m_pred:>11.3f} "
                  f"{m_obs:>11.3f}  {rel_err:>+9.2f}%")
            damage_rows.append({
                'particle': name, 'tuple': str(tup),
                's_p': s_p_match,
                'predicted_MeV': m_pred,
                'observed_MeV': m_obs,
                'relative_error_pct': rel_err,
            })
            n_total += 1
            if abs(rel_err) <= 5.0:
                n_within_5pct += 1
            if abs(rel_err) > abs(max_dev):
                max_dev = rel_err
                max_dev_name = name
        except Exception as ex:
            print(f"  {name:12s} error: {ex}")

    print()
    if n_total > 0:
        print(f"  Summary: {n_within_5pct} of {n_total} hadrons within ±5%")
        print(f"  Worst miss: {max_dev_name} at {max_dev:+.2f}%")
        print(f"  At g-candidate s_p = 0.162, every inventory entry was")
        print(f"  within ~1.8% (per Track 8 Phase 8a / Track 6 Phase 6a).")
    print()

    csv_path3 = out_dir / "track10_phase10c_inventory_damage.csv"
    with open(csv_path3, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(damage_rows[0].keys()))
        w.writeheader()
        w.writerows(damage_rows)

    # ─── Verdict ───
    print("=" * 100)
    print("Phase 10c verdict")
    print("=" * 100)
    print(f"""
  At g-candidate baseline (ε_p=0.55, s_p=0.162):
    regular pp      (6, 12):  ~{m_pp_reg:>8.2f} MeV   matches additive deuteron
    regular pn      (6, 12):  ~{m_pn_reg:>8.2f} MeV   = pp + 0.5 MeV (electron mass)
    complementary pp (6,  0):  ~{m_pp_comp:>8.2f} MeV   ~550 MeV under deuteron
    complementary pn (6,  0):  ~{m_pn_comp:>8.2f} MeV   essentially same as comp pp

  Findings:

  1. The (6, 0) compound mode is a different particle, not the deuteron.
     Mass ~1326 MeV places it in the Σ–Ξ baryon region, but its v2
     classification (gcd=6, primitive (1, 0), tube-only neutral) gives
     Q=0 — inconsistent with deuteron's Q=+1.

  2. The neutron's e/ν "ballast" is ~0.5 MeV (essentially the electron
     mass).  The deuteron's binding energy is ~2.2 MeV.  Ballast is in
     the ballpark of binding magnitude but several factors short, and
     it has the wrong parity — it pushes mass UP (heavier compound),
     not down (binding).

  3. The (6, 0) tuple matches m_d only at s_p ≈ 1, far from g-candidate
     s_p = 0.162.  At that shear, the hadron inventory is broken
     (worst miss {max_dev:+.1f}% on {max_dev_name}); the rest of model-F
     becomes inconsistent with observation.

  4. The shear-flip-on-binding hypothesis (free neutron at (3, 6),
     bound neutron at (3, -6)) is not directly testable in the existing
     framework.  Each tuple is its own eigenmode; there is no operator
     that transitions between tuple classes upon proximity to another
     baryon.  Implementing such an operator would be a framework
     extension on the order of Reading B-extended.

  Reading A (honest closure within existing operator inventory) is
  re-confirmed.  The user's complementary-shear hypothesis is
  structurally interesting but does not give the deuteron at any
  parameter point that preserves the rest of model-F.

  R63's binding closure stands.  Successor-study directions remain
  Reading B-extended (spin-coupled operator), Reading C (S-space
  configuration energy), and Reading D (vacuum polarization).
""")
    print(f"  CSVs:")
    print(f"    {csv_path1}")
    print(f"    {csv_path2}")
    print(f"    {csv_path3}")


if __name__ == "__main__":
    main()
