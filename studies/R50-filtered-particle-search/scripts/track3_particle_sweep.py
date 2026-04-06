"""
R50 Track 3: Full joint mode sweep — particle spectrum at σ_ep ≈ −0.13

At the preferred cross-shear from Track 2 (σ_ep = −0.13), scans the
full 6D mode space up to ~2 GeV and matches against the tier 1–4
particle targets from the R50 README.

KEY PHYSICS:
The topological spin rule (J = number_of_odd_tube_windings × ½)
constrains which (Q, J) combinations are possible:
  - J = 0 → only even Q (all tubes even → Q even)
  - J = 3/2 → only even Q (all three tubes odd → Q even)
  - J = ½, 1 → any Q
This means charged pseudoscalar mesons (π±, K±) and odd-charge
J = 3/2 baryons (Ω⁻, Δ±) cannot be eigenmodes in the current model.

DELIVERABLES (from R50 README Track 3):
  - For each known target: nearest mode, mass residual, charge/spin match
  - Lifetime-residual correlation (R27's r = −0.84 result)
  - Mode overcounting: how many predicted modes have no known particle?
"""

import sys
import os
import math
from itertools import product as iproduct
from collections import defaultdict

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np

from lib.ma_model_d import (
    MaD, M_E_MEV, M_P_MEV, DM2_21,
    _TWO_PI_HC, _build_circumferences, _build_metric,
    solve_shear_for_alpha,
)

# ── Constants ─────────────────────────────────────────────────────

M_NEUTRON = 939.565
EPS_E, EPS_NU, EPS_P = 0.65, 5.0, 0.55
S_NU_DEFAULT = 0.022
SIGMA_EP = -0.13
E_MAX = 2000.0  # MeV

# ── Target particles ──────────────────────────────────────────────
# (name, mass_MeV, charge, spin, lifetime_s, tier)

TARGETS = [
    ('e⁻',       0.511,     -1, 0.5,  float('inf'), 1),
    ('p',        938.272,    +1, 0.5,  float('inf'), 1),
    ('ν₁',       2.92e-5,    0, 0.5,  float('inf'), 1),
    ('n',        939.565,     0, 0.5,  879.4,        2),
    ('μ⁻',      105.658,    -1, 0.5,  2.197e-6,     2),
    ('π±',      139.570,    +1, 0.0,  2.603e-8,     2),
    ('π⁰',     134.977,     0, 0.0,  8.43e-17,     2),
    ('K±',      493.677,    +1, 0.0,  1.238e-8,     2),
    ('K⁰',      497.611,     0, 0.0,  8.954e-11,    2),
    ('η',       547.862,     0, 0.0,  5.02e-19,     2),
    ('η′',      957.78,      0, 0.0,  3.32e-21,     2),
    ('φ',      1019.461,     0, 1.0,  1.55e-22,     3),
    ('Λ',      1115.683,     0, 0.5,  2.632e-10,    2),
    ('Σ⁺',    1189.37,     +1, 0.5,  8.018e-11,    3),
    ('Ξ⁰',    1314.86,      0, 0.5,  2.90e-10,     3),
    ('Ω⁻',    1672.45,     -1, 1.5,  8.21e-11,     3),
    ('Δ⁰',     1232.0,      0, 1.5,  5.63e-24,     3),
    ('ρ⁰',      775.26,     0, 1.0,  4.51e-24,     3),
    ('τ⁻',    1776.86,     -1, 0.5,  2.903e-13,    3),
]

# ── Model builder (from Track 2) ─────────────────────────────────

def build_corrected_model(sigma_ep=0.0, sigma_enu=0.0, sigma_nup=0.0):
    """Build MaD with L_ring adjusted for cross-shear effects on G̃⁻¹."""
    s_e = solve_shear_for_alpha(EPS_E)
    s_p = solve_shear_for_alpha(EPS_P)
    s_nu = S_NU_DEFAULT

    if s_e is None or s_p is None:
        return None, {}

    L_dummy = _build_circumferences(
        EPS_E, s_e, 1.0, EPS_NU, s_nu, 1.0, EPS_P, s_p, 1.0)
    Gt, Gti = _build_metric(
        L_dummy, s_e, s_nu, s_p,
        sigma_ep=sigma_ep, sigma_enu=sigma_enu, sigma_nup=sigma_nup)
    if Gt is None:
        return None, {}

    n_e_d = np.array([1.0 / EPS_E, 2.0, 0, 0, 0, 0])
    mu_eff_e = math.sqrt(float(n_e_d @ Gti @ n_e_d))
    L_ring_e = _TWO_PI_HC * mu_eff_e / M_E_MEV

    n_p_d = np.array([0, 0, 0, 0, 3.0 / EPS_P, 6.0])
    mu_eff_p = math.sqrt(float(n_p_d @ Gti @ n_p_d))
    L_ring_p = _TWO_PI_HC * mu_eff_p / M_P_MEV

    E0_nu_MeV = math.sqrt(DM2_21 / (4 * s_nu)) * 1e-6
    L_ring_nu = _TWO_PI_HC / E0_nu_MeV

    try:
        model = MaD(
            eps_e=EPS_E, eps_nu=EPS_NU, eps_p=EPS_P,
            s_e=s_e, s_nu=s_nu, s_p=s_p,
            L_ring_e=L_ring_e, L_ring_nu=L_ring_nu, L_ring_p=L_ring_p,
            sigma_ep=sigma_ep, sigma_enu=sigma_enu, sigma_nup=sigma_nup)
    except ValueError:
        return None, {}

    return model, {
        'L_ring_e': L_ring_e, 'L_ring_p': L_ring_p, 'L_ring_nu': L_ring_nu,
    }


# ── Helpers ───────────────────────────────────────────────────────

def generate_candidates(n_ranges, charge_target=None, spin_target=None):
    """Generate 6-tuples, optionally filtered by charge and/or spin."""
    ranges = [range(lo, hi + 1) for lo, hi in n_ranges]
    out = []
    for n in iproduct(*ranges):
        if all(ni == 0 for ni in n):
            continue
        if charge_target is not None and MaD.charge_composite(n) != charge_target:
            continue
        if spin_target is not None and MaD.spin_total(n) != spin_target:
            continue
        out.append(n)
    return out


def batch_energies(candidates_arr, L, Gti):
    """Vectorized energy computation for many modes."""
    n_over_L = candidates_arr / L
    E2 = _TWO_PI_HC**2 * np.sum((n_over_L @ Gti) * n_over_L, axis=1)
    return np.sqrt(np.maximum(E2, 0))


def is_qs_possible(Q, spin):
    """
    Check if (Q, spin) is topologically realizable.

    The number of odd per-strand tube windings k determines spin J = k/2.
    Charge Q = −n₁ + n₅/gcd.  Both n₁ and n₅/gcd are tube windings
    (on charged sheets), so:
      k = 0: both even → Q even
      k = 1: one odd tube, can be on ν (no charge) → any Q
      k = 2: two odd tubes, one can be on ν → any Q
      k = 3: all three odd, n₁ and n₅/gcd both odd → Q even
    """
    k = int(2 * spin)
    if k == 0 or k == 3:
        return Q % 2 == 0
    return True


# ══════════════════════════════════════════════════════════════════
def main():
    print("=" * 72)
    print("R50 Track 3: Full joint mode sweep — particle spectrum")
    print("=" * 72)

    # ── Phase 0: Build model ──────────────────────────────────────
    print(f"\nPhase 0: Model at σ_ep = {SIGMA_EP}")
    model, info = build_corrected_model(sigma_ep=SIGMA_EP)
    E_e = model.energy((1, 2, 0, 0, 0, 0))
    E_p = model.energy((0, 0, 0, 0, 3, 6))
    E0_p = _TWO_PI_HC / info['L_ring_p']
    E0_e = _TWO_PI_HC / info['L_ring_e']

    print(f"  E(electron) = {E_e:.6f} MeV  (target {M_E_MEV:.6f})")
    print(f"  E(proton)   = {E_p:.3f} MeV  (target {M_P_MEV:.3f})")
    print(f"  E₀_p (proton ring unit) = {E0_p:.2f} MeV")
    print(f"  E₀_e (electron ring unit) = {E0_e:.4f} MeV")
    print(f"  Mass desert: {E0_e:.2f} – {E0_p:.0f} MeV (no modes here)")

    N_RANGES = [
        (-3, 3),     # n₁  electron tube
        (-6, 6),     # n₂  electron ring
        (-3, 3),     # n₃  neutrino tube
        (-3, 3),     # n₄  neutrino ring
        (-6, 6),     # n₅  proton tube
        (-16, 16),   # n₆  proton ring
    ]
    total_space = 1
    for lo, hi in N_RANGES:
        total_space *= (hi - lo + 1)
    print(f"  Search space: {total_space:,} 6-tuples")

    # ── Phase 1: Topological constraints ──────────────────────────
    print(f"\n{'=' * 72}")
    print("Phase 1: Topological charge-spin constraints")
    print(f"{'=' * 72}")
    print("""
  Additive spin rule: J = (# odd per-strand tubes) × ½
  Charge:             Q = −n₁ + n₅/gcd(|n₅|,|n₆|)

  Both n₁ and n₅/gcd are tube windings on charged sheets.
  When ALL tubes are even (J = 0) or ALL are odd (J = 3/2),
  both charged-sheet tubes share the same parity → Q is even.

   J    | Allowed Q parity | Impossible examples
  ------|------------------|------------------------------
   0    | even only        | π± (Q=±1, J=0), K± (Q=±1, J=0)
   ½    | any              | —
   1    | any              | —
   3/2  | even only        | Ω⁻ (Q=−1, J=3/2), Δ± (Q=±1, J=3/2)
""")
    impossible_targets = []
    for name, mass, Q, spin, tau, tier in TARGETS:
        if not is_qs_possible(Q, spin):
            impossible_targets.append(name)
            print(f"  ✗ {name}: Q = {Q:+d}, J = {spin} — topologically impossible")

    # ── Phase 2: Generate candidates ──────────────────────────────
    print(f"\n{'=' * 72}")
    print("Phase 2: Generating candidates per (Q, J)")
    print(f"{'=' * 72}")

    qs_needed = set()
    relaxed_charges = set()
    for name, mass, Q, spin, tau, tier in TARGETS:
        if is_qs_possible(Q, spin):
            qs_needed.add((Q, spin))
        else:
            relaxed_charges.add(Q)

    cand_data = {}  # key → (modes_list, energies_array)

    for Q, J in sorted(qs_needed):
        cands = generate_candidates(N_RANGES, charge_target=Q, spin_target=J)
        prop = [n for n in cands if model.propagates(n)]
        if not prop:
            print(f"  (Q={Q:+d}, J={J}): {len(cands)} raw, 0 propagating")
            continue
        arr = np.array(prop, dtype=float)
        E = batch_energies(arr, model.L, model.metric_inv)
        mask = E <= E_MAX
        cand_data[(Q, J)] = (
            [prop[i] for i in range(len(prop)) if mask[i]],
            E[mask],
        )
        print(f"  (Q={Q:+d}, J={J:.1f}): {len(cands):>6d} raw → "
              f"{len(prop):>5d} prop → {int(mask.sum()):>5d} ≤ {E_MAX:.0f} MeV")

    for Q in sorted(relaxed_charges):
        cands = generate_candidates(N_RANGES, charge_target=Q)
        prop = [n for n in cands if model.propagates(n)]
        if not prop:
            continue
        arr = np.array(prop, dtype=float)
        E = batch_energies(arr, model.L, model.metric_inv)
        mask = E <= E_MAX
        cand_data[('relax', Q)] = (
            [prop[i] for i in range(len(prop)) if mask[i]],
            E[mask],
        )
        print(f"  Relaxed Q={Q:+d} (any J): {len(prop):>5d} prop → "
              f"{int(mask.sum()):>5d} ≤ {E_MAX:.0f} MeV")

    # ── Phase 3: Match targets ────────────────────────────────────
    print(f"\n{'=' * 72}")
    print(f"Phase 3: Target matching at σ_ep = {SIGMA_EP}")
    print(f"{'=' * 72}")

    results = []

    for name, mass, Q, spin, tau, tier in TARGETS:
        key = (Q, spin)
        relaxed = False

        if key in cand_data:
            modes, Es = cand_data[key]
        elif ('relax', Q) in cand_data:
            modes, Es = cand_data[('relax', Q)]
            relaxed = True
        else:
            results.append(dict(
                name=name, mass=mass, Q=Q, spin=spin, tau=tau, tier=tier,
                best_n=None, best_E=None, best_dm=None,
                relaxed=relaxed, best_J=None, sheets=None,
            ))
            continue

        if len(modes) == 0:
            results.append(dict(
                name=name, mass=mass, Q=Q, spin=spin, tau=tau, tier=tier,
                best_n=None, best_E=None, best_dm=None,
                relaxed=relaxed, best_J=None, sheets=None,
            ))
            continue

        diffs = np.abs(Es - mass)
        top5 = np.argsort(diffs)[:5]

        bi = top5[0]
        bn = modes[bi]
        bE = float(Es[bi])
        bdm = bE - mass
        bJ = MaD.spin_total(bn)
        bsh = model.active_sheets(bn)

        results.append(dict(
            name=name, mass=mass, Q=Q, spin=spin, tau=tau, tier=tier,
            best_n=bn, best_E=bE, best_dm=bdm,
            relaxed=relaxed, best_J=bJ, sheets=bsh,
        ))

        tag = ""
        if relaxed:
            tag = f"  [Q-only match; J={bJ} vs target {spin}]"

        print(f"\n  {name} (tier {tier}, m = {mass:.3f} MeV, "
              f"Q = {Q:+d}, J = {spin}){tag}")

        hdr = (f"  {'#':>2s}  {'Mode':>30s}  {'E (MeV)':>10s}  "
               f"{'Δm (MeV)':>10s}  {'|Δm|/m':>8s}  {'J':>4s}  {'Sheets':>10s}")
        print(hdr)
        print(f"  {'─' * 2}  {'─' * 30}  {'─' * 10}  {'─' * 10}  "
              f"{'─' * 8}  {'─' * 4}  {'─' * 10}")

        for rank, idx in enumerate(top5, 1):
            n = modes[idx]
            E = float(Es[idx])
            dm = E - mass
            J = MaD.spin_total(n)
            sh = model.active_sheets(n)
            mark = " ←" if rank == 1 else ""
            print(f"  {rank:2d}  {str(n):>30s}  {E:10.3f}  {dm:+10.3f}  "
                  f"{abs(dm) / mass * 100:7.3f}%  {J:4.1f}  {sh:>10s}{mark}")

    # ── Phase 4: Master table ─────────────────────────────────────
    print(f"\n{'=' * 72}")
    print("Phase 4: Master summary table")
    print(f"{'=' * 72}\n")

    print(f"  {'Particle':>8s}  {'T':>1s}  {'m (MeV)':>10s}  {'Q':>3s}  "
          f"{'J':>4s}  {'Best mode':>30s}  {'Δm (MeV)':>10s}  "
          f"{'|Δm|/m':>8s}  {'J_mode':>6s}  {'Note':>10s}")
    print(f"  {'─' * 8}  {'─'}  {'─' * 10}  {'─' * 3}  {'─' * 4}  "
          f"{'─' * 30}  {'─' * 10}  {'─' * 8}  {'─' * 6}  {'─' * 10}")

    for r in results:
        if r['best_n'] is None:
            print(f"  {r['name']:>8s}  {r['tier']:1d}  {r['mass']:10.3f}  "
                  f"{r['Q']:+3d}  {r['spin']:4.1f}  {'— none —':>30s}  "
                  f"{'':>10s}  {'':>8s}  {'':>6s}  {'no match':>10s}")
            continue

        frac = abs(r['best_dm']) / r['mass']
        if r['relaxed']:
            note = "J imposs."
        elif frac < 0.001:
            note = "reference"
        elif frac < 0.02:
            note = "good"
        elif frac < 0.10:
            note = "fair"
        else:
            note = "poor"

        Jstr = f"{r['best_J']:.1f}"
        if r['best_J'] != r['spin']:
            Jstr += "!"

        print(f"  {r['name']:>8s}  {r['tier']:1d}  {r['mass']:10.3f}  "
              f"{r['Q']:+3d}  {r['spin']:4.1f}  {str(r['best_n']):>30s}  "
              f"{r['best_dm']:+10.3f}  {frac * 100:7.3f}%  "
              f"{Jstr:>6s}  {note:>10s}")

    # ── Phase 5: Off-resonance correlation ────────────────────────
    print(f"\n{'=' * 72}")
    print("Phase 5: Off-resonance correlation (log τ vs log |Δm/m|)")
    print(f"{'=' * 72}")

    for r in results:
        if r['best_n'] is not None and r['tau'] == float('inf'):
            dm = abs(r['best_dm']) if r['best_dm'] else 0
            print(f"  {r['name']:>6s}: stable,  |Δm| = {dm:.2e} MeV  "
                  f"({'exact' if dm < 0.001 else 'offset'})")

    corr = [r for r in results
            if r['best_n'] is not None
            and r['tau'] != float('inf')
            and r['best_dm'] is not None
            and abs(r['best_dm']) > 1e-10
            and not r['relaxed']]

    if len(corr) >= 3:
        log_tau = np.array([math.log10(r['tau']) for r in corr])
        log_dm = np.array([math.log10(abs(r['best_dm']) / r['mass']) for r in corr])
        r_corr = float(np.corrcoef(log_tau, log_dm)[0, 1])

        print(f"\n  Unstable particles (exact Q+J match only):\n")
        print(f"  {'Particle':>8s}  {'τ (s)':>12s}  {'|Δm| MeV':>10s}  "
              f"{'|Δm|/m':>10s}  {'log₁₀ τ':>8s}  {'log₁₀|Δm/m|':>12s}")
        print(f"  {'─' * 8}  {'─' * 12}  {'─' * 10}  {'─' * 10}  "
              f"{'─' * 8}  {'─' * 12}")

        for r in sorted(corr, key=lambda x: -x['tau']):
            dm = abs(r['best_dm'])
            frac = dm / r['mass']
            print(f"  {r['name']:>8s}  {r['tau']:12.2e}  {dm:10.4f}  "
                  f"{frac:10.6f}  {math.log10(r['tau']):8.2f}  "
                  f"{math.log10(frac):12.4f}")

        print(f"\n  Pearson r = {r_corr:+.3f}  (N = {len(corr)})")
        if r_corr < -0.3:
            print(f"  → Negative correlation: consistent with "
                  f"off-resonance hypothesis (R27: r = −0.84)")
        elif r_corr > 0.3:
            print(f"  → Positive correlation: INCONSISTENT with hypothesis")
        else:
            print(f"  → Weak correlation: inconclusive at N = {len(corr)}")
    else:
        print(f"\n  Only {len(corr)} valid points — insufficient for correlation")

    # ── Phase 6: Mode census ──────────────────────────────────────
    print(f"\n{'=' * 72}")
    print("Phase 6: Mode census (all propagating modes ≤ 2 GeV)")
    print(f"{'=' * 72}")

    print("\n  Enumerating modes in chunks by (n₅, n₆)...")

    count_prop = 0
    qs_census = defaultdict(int)
    dark_count = 0
    e_bins = defaultdict(int)
    dark_examples = []

    n5_range = range(N_RANGES[4][0], N_RANGES[4][1] + 1)
    n6_range = range(N_RANGES[5][0], N_RANGES[5][1] + 1)

    for n5 in n5_range:
        for n6 in n6_range:
            chunk = []
            for n1 in range(N_RANGES[0][0], N_RANGES[0][1] + 1):
                for n2 in range(N_RANGES[1][0], N_RANGES[1][1] + 1):
                    for n3 in range(N_RANGES[2][0], N_RANGES[2][1] + 1):
                        for n4 in range(N_RANGES[3][0], N_RANGES[3][1] + 1):
                            n = (n1, n2, n3, n4, n5, n6)
                            if all(ni == 0 for ni in n):
                                continue
                            chunk.append(n)
            if not chunk:
                continue

            arr = np.array(chunk, dtype=float)
            E = batch_energies(arr, model.L, model.metric_inv)

            for i in range(len(chunk)):
                if E[i] > E_MAX:
                    continue
                n = chunk[i]
                if not model.propagates(n):
                    continue
                count_prop += 1
                Q = MaD.charge_composite(n)
                J = MaD.spin_total(n)
                qs_census[(Q, J)] += 1
                ebin = int(E[i] / 200) * 200
                e_bins[ebin] += 1
                if n[0] == 0 and n[4] == 0:
                    dark_count += 1
                    if len(dark_examples) < 10:
                        dark_examples.append((n, float(E[i])))

    print(f"\n  Total propagating modes ≤ {E_MAX:.0f} MeV: {count_prop}")
    print(f"  Fully dark (n₁ = n₅ = 0):              {dark_count}")

    print(f"\n  By (Q, J):")
    for (Q, J) in sorted(qs_census.keys()):
        print(f"    (Q={Q:+d}, J={J:.1f}): {qs_census[(Q, J)]:5d}")

    print(f"\n  By energy bin:")
    for ebin in sorted(e_bins.keys()):
        bar = '█' * min(e_bins[ebin] // 20, 50)
        print(f"    {ebin:5d}–{ebin + 200:5d} MeV: {e_bins[ebin]:5d}  {bar}")

    if dark_examples:
        print(f"\n  Dark-mode examples (n₁ = n₅ = 0 → Q = 0, EM invisible):")
        for n, E in sorted(dark_examples, key=lambda x: x[1])[:5]:
            J = MaD.spin_total(n)
            sh = model.active_sheets(n)
            print(f"    {str(n):>30s}  E = {E:10.3f} MeV  J = {J:.1f}  {sh}")

    # ── Phase 7: Summary ──────────────────────────────────────────
    print(f"\n{'=' * 72}")
    print("Summary")
    print(f"{'=' * 72}")

    n_ref = sum(1 for r in results
                if r['best_n'] is not None and r['tau'] == float('inf')
                and abs(r.get('best_dm', 999)) < 0.001)
    n_good = sum(1 for r in results
                 if r['best_n'] is not None and not r['relaxed']
                 and r['tau'] != float('inf')
                 and abs(r['best_dm']) / r['mass'] < 0.02)
    n_fair = sum(1 for r in results
                 if r['best_n'] is not None and not r['relaxed']
                 and r['tau'] != float('inf')
                 and 0.02 <= abs(r['best_dm']) / r['mass'] < 0.10)
    n_poor = sum(1 for r in results
                 if r['best_n'] is not None and not r['relaxed']
                 and r['tau'] != float('inf')
                 and abs(r['best_dm']) / r['mass'] >= 0.10)
    n_impossible = sum(1 for r in results if r['relaxed'])

    print(f"\n  {len(TARGETS)} target particles:")
    print(f"    Reference (exact by construction): {n_ref}")
    print(f"    Good match (|Δm/m| < 2%):          {n_good}")
    print(f"    Fair match (2–10%):                 {n_fair}")
    print(f"    Poor match (> 10%):                 {n_poor}")
    print(f"    J topologically impossible:         {n_impossible}")
    print(f"\n  Mode census:")
    print(f"    Total propagating ≤ 2 GeV:    {count_prop}")
    print(f"    Fully dark (EM invisible):    {dark_count}")
    print(f"    Overcounting ratio:           "
          f"{count_prop}:{len(TARGETS)} = {count_prop / len(TARGETS):.0f}:1")

    print(f"\n  Key structural findings:")
    print(f"    1. Charged J=0 (π±, K±) and odd-Q J=3/2 (Ω⁻, Δ±)")
    print(f"       are topologically forbidden by additive spin rule.")
    print(f"       Resolution: allow QM spin addition (antiparallel alignment).")
    print(f"    2. Mass desert from ~{E0_e:.1f} MeV to ~{E0_p:.0f} MeV — the")
    print(f"       muon ({TARGETS[4][1]:.1f} MeV) sits below the first")
    print(f"       proton-ring harmonic with no nearby eigenmode.")
    print(f"    3. Mode overcounting: {count_prop} propagating modes for")
    print(f"       {len(TARGETS)} targets. Most are degenerate clusters")
    print(f"       (same proton winding, varying e/ν labels).")

    print(f"\n{'=' * 72}")
    print("Track 3 complete.")
    print(f"{'=' * 72}")


if __name__ == '__main__':
    main()
