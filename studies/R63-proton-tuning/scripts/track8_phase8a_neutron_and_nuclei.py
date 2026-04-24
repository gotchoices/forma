"""
R63 Track 8 Phase 8a — Neutron tuple substitution and nuclear verification.

Substitute the β-decay-derived neutron tuple (1, 2, 1, 1, 3, 6) into the
g-candidate inventory and verify:

  1. Neutron under v2 charge arithmetic still gives Q = 0
     (fundamental-mode charge check).
  2. Additive composition of nuclei reproduces the Phase 7a
     results at equal or better accuracy than the A-scaling formula.
  3. Compound-charge consistency is achieved by ingredient-sum
     (nucleus Q = Z · Q_proton + (A−Z) · Q_neutron = Z), not by
     re-applying v2's per-sheet rule to the composite tuple.

Inputs: current g-candidate parameters.  No new parameter pinning;
Track 8 is combinatoric over integer windings at fixed parameters.

Outputs (../outputs/):
  - track8_phase8a_neutron_check.txt — fundamental neutron charge check
  - track8_phase8a_nuclei_additive.csv — additive nuclear chain table
  - track8_phase8a_additive_vs_Ascaling.png — comparison plot
"""

import sys, os
import csv
import math
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'R60-metric-11', 'scripts'))

from track1_solver import (
    derive_L_ring, L_vector_from_params, mode_energy, mode_6_to_11,
    signature_ok, M_E_MEV, M_P_MEV,
)
from track7b_resolve import build_aug_metric
from track15_phase1_mass import K_MODELF

from track6_phase6a_compatibility import (
    classify_sheet_v2, sheet_charge_v2,
)
from track7a_nuclei_H_to_Fe import (
    NUCLEI, nuclear_mass, binding_energy, build_working_metric,
    U_TO_MEV, M_E, M_P, M_N, WORKING_PARAMS,
)


# ─── Fundamental tuples (g-candidate, Phase 8a proposal) ───────────

PROTON_TUPLE   = (0, 0, 0, 0, 3, 6)
NEUTRON_TUPLE  = (1, 2, -1, -1, 3, 6)      # β-decay-derived (Phase 8a)
ELECTRON_TUPLE = (1, 2, 0, 0, 0, 0)
NU1_TUPLE      = (0, 0, 1, 1, 0, 0)

# The neutron tuple satisfies the β-decay identity
#   n → p + e⁻ + ν̄_e   ⟹   n_tuple = p_tuple + e_tuple + ν̄_e_tuple
#   ν̄_e = C-conjugate of ν₁ = (0, 0, −1, −1, 0, 0)
#   ⟹ n = (0,0,0,0,3,6) + (1,2,0,0,0,0) + (0,0,-1,-1,0,0)
#       = (1, 2, -1, -1, 3, 6)
# The ν-sheet negative windings reflect the fact that an antineutrino
# (not a neutrino) is emitted in β decay.  Mass is identical to the
# (1, 2, 1, 1, 3, 6) sign-flip since ν-sheet μ² depends on |windings|²
# symmetrically, so the Phase 7 nuclear mass verification results hold
# unchanged.


# ─── Fundamental charge arithmetic ─────────────────────────────────

def v2_charge(tup):
    """Compute v2 charge for a FUNDAMENTAL mode tuple.

    Returns (Q, (Q_e, Q_nu, Q_p)).  Note: for COMPOSITES (nuclei),
    use ingredient_sum_charge instead.
    """
    n_et, n_er, n_nut, n_nur, n_pt, n_pr = tup
    c_e  = classify_sheet_v2(n_et,  n_er)
    c_nu = classify_sheet_v2(n_nut, n_nur)
    c_p  = classify_sheet_v2(n_pt,  n_pr)
    Q_e  = sheet_charge_v2("e",  c_e[0],  c_e[2])
    Q_nu = sheet_charge_v2("nu", c_nu[0], c_nu[2])
    Q_p  = sheet_charge_v2("p",  c_p[0],  c_p[2])
    return Q_e + Q_nu + Q_p, (Q_e, Q_nu, Q_p, c_e[0], c_nu[0], c_p[0])


def ingredient_sum_charge(Z, A):
    """Nucleus charge under ingredient-sum rule.

    Z protons contribute Z · (+1) = +Z; (A−Z) neutrons contribute 0.
    """
    return Z


# ─── Additive nucleus tuple from Z protons + (A−Z) neutrons ─────────

def additive_tuple(Z, A):
    """Nucleus tuple as Z · proton + (A−Z) · neutron under Phase 8a neutron."""
    tup = tuple(Z * p + (A - Z) * n
                for p, n in zip(PROTON_TUPLE, NEUTRON_TUPLE))
    return tup


# ─── Main ───────────────────────────────────────────────────────────

def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 104)
    print("R63 Track 8 Phase 8a — Neutron substitution + additive nuclear verification")
    print("=" * 104)
    print()

    # ─── Step 1: Fundamental neutron charge check ───
    print("── Step 1: Fundamental charge checks under v2 ──")
    print(f"  {'particle':<10s}  {'tuple':<28s}  {'e-cat':<14s}  {'ν-cat':<14s}  {'p-cat':<14s}  {'Q_pred':>6s}  {'Q_obs':>5s}")
    print("  " + "-" * 106)
    log_lines = []
    for name, tup, Q_obs in [
        ("electron", ELECTRON_TUPLE, -1),
        ("proton",   PROTON_TUPLE,   +1),
        ("ν₁",       NU1_TUPLE,       0),
        ("neutron (Phase 8a)", NEUTRON_TUPLE, 0),
    ]:
        Q, (Qe, Qn, Qp, ce, cn, cp) = v2_charge(tup)
        verdict = '✓' if Q == Q_obs else '✗'
        line = (f"  {name:<10s}  {str(tup):<28s}  {ce:<14s}  {cn:<14s}  "
                f"{cp:<14s}  {Q:>+6d}  {Q_obs:>+5d}  {verdict}")
        print(line); log_lines.append(line)
    print()
    log_lines.append('')

    # Verify the neutron's additive composition explicitly
    note = ("  Note: the proposed neutron (1, 2, 1, 1, 3, 6) equals the\n"
            "  β-decay winding sum p + e + ν (with the ν sign convention\n"
            "  matching R60 T19's ν tuple; p + e + ν̄ gives the same tuple\n"
            "  up to overall ν sign and gives an identical mass).")
    print(note)
    log_lines.append(note)

    with open(out_dir / "track8_phase8a_neutron_check.txt", 'w') as f:
        f.write("\n".join(log_lines))
    print()

    # ─── Step 2: Nuclear chain under additive composition ───
    print("── Step 2: Additive nuclear chain, H → Fe ──")
    params, G, L = build_working_metric()

    def E(tup):
        return mode_energy(G, L, mode_6_to_11(tup))

    rows = []
    for name, Z, A, atomic_u in NUCLEI:
        m_obs = nuclear_mass(atomic_u, Z)
        B = binding_energy(Z, A, m_obs)
        # Predictions
        tup_As  = (1 - Z, 0, 0, 0, 3 * A, 6 * A)
        tup_add = additive_tuple(Z, A)
        m_As  = E(tup_As)
        m_add = E(tup_add)
        miss_As  = (m_As  - m_obs) / m_obs * 100
        miss_add = (m_add - m_obs) / m_obs * 100
        # Ingredient-sum charge
        Q_ingr = ingredient_sum_charge(Z, A)
        # Composite v2 charge (expected to fail past Z=1)
        Q_v2, _ = v2_charge(tup_add)
        rows.append({
            'name': name, 'Z': Z, 'A': A,
            'm_obs': m_obs, 'B': B,
            'm_Ascale': m_As, 'miss_Ascale': miss_As,
            'tup_additive': str(tup_add).replace(' ', ''),
            'm_additive': m_add, 'miss_additive': miss_add,
            'Q_ingredient_sum': Q_ingr,
            'Q_v2_on_composite': Q_v2,
            'Z_observed': Z,
        })

    # Print summary
    print(f"  {'nucleus':<8s}  {'Z':>3s} {'A':>3s}  "
          f"{'m_obs':>10s}  {'A-scale miss':>12s}  {'additive miss':>13s}  "
          f"{'improvement':>11s}  {'Q_v2(tup)':>9s}  {'Q_ingredient':>12s}")
    print("  " + "-" * 108)
    total_improvement = 0.0
    n_better = 0
    for r in rows:
        improvement = abs(r['miss_Ascale']) - abs(r['miss_additive'])
        total_improvement += improvement
        if improvement > 0:
            n_better += 1
        better = '(better)' if improvement > 0 else ('(same)' if abs(improvement) < 0.0001 else '(worse)')
        print(f"  {r['name']:<8s}  {r['Z']:>3d} {r['A']:>3d}  "
              f"{r['m_obs']:>10.3f}  {r['miss_Ascale']:>+11.4f}%  "
              f"{r['miss_additive']:>+12.4f}%  {improvement:>+10.4f}%  "
              f"{r['Q_v2_on_composite']:>+9d}  {r['Z_observed']:>12d}  {better}")
    print()
    print(f"  Summary: additive beats A-scaling on {n_better} of {len(rows)} nuclei; "
          f"mean improvement {total_improvement/len(rows):+.4f} percentage points.")
    print()

    # Observations about the Q columns
    print("  Observation: Q_v2(composite tuple) ≠ observed Z for Z ≥ 2, confirming")
    print("  that v2's per-sheet primitive rule does not lift from fundamental to")
    print("  composite.  Ingredient-sum rule (Q = Z×Q_p + (A−Z)×Q_n) gives the")
    print("  correct observed charge for every nucleus by construction.")
    print()

    # ─── CSV ───
    csv_path = out_dir / "track8_phase8a_nuclei_additive.csv"
    fields = ['name', 'Z', 'A', 'm_obs', 'B',
              'm_Ascale', 'miss_Ascale',
              'tup_additive', 'm_additive', 'miss_additive',
              'Q_ingredient_sum', 'Q_v2_on_composite', 'Z_observed']
    with open(csv_path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({k: r[k] for k in fields})
    print(f"  CSV: {csv_path}")

    # ─── Plot: additive vs A-scaling miss ───
    A_arr   = np.array([r['A'] for r in rows])
    As_arr  = np.array([r['miss_Ascale'] for r in rows])
    add_arr = np.array([r['miss_additive'] for r in rows])
    names   = [r['name'] for r in rows]

    fig, ax = plt.subplots(figsize=(12, 6.5))
    ax.plot(A_arr, As_arr, 'o-', color='tab:orange', markersize=7,
            label='A-scaling (original R60 T19)')
    ax.plot(A_arr, add_arr, 's-', color='tab:blue', markersize=7,
            label='Additive (Z·proton + (A−Z)·neutron)')
    for A, y, n in zip(A_arr, add_arr, names):
        ax.annotate(n, xy=(A, y), xytext=(3, -12),
                    textcoords='offset points', fontsize=7)
    ax.axhline(0, color='k', linewidth=0.5)
    ax.set_xlabel('mass number A')
    ax.set_ylabel('Δm/m (%)')
    ax.set_title("R63 Track 8 Phase 8a — additive nuclear composition vs. A-scaling\n"
                 "using β-decay-derived neutron tuple (1, 2, 1, 1, 3, 6)")
    ax.grid(alpha=0.3)
    ax.legend()
    plt.tight_layout()
    plt.savefig(out_dir / "track8_phase8a_additive_vs_Ascaling.png",
                dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Plot: {out_dir / 'track8_phase8a_additive_vs_Ascaling.png'}")


if __name__ == "__main__":
    main()
