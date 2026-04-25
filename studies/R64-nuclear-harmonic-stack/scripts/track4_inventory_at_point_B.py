"""
R64 Track 4 Phase 4a — Hadron inventory audit at the chain-fit point.

Track 3 Phase 3d/3e identified Point B = (ε_p=0.2052, s_p=+0.0250,
K_p=63.629) as a candidate working point that fits the body of the
nuclear chain within 1–2%, in contrast to Point A (the deuteron-
anchored magic point) which under-predicts heavy nuclei by 7×.

Track 4 tests whether Point B preserves the 13-particle hadron
inventory under R64's flavor-aware composition rule, with an open
question about how to identify primitives for s, c, b, t.

Approach:
  1. For mesons (q-q̄ pairs): test simplest u/d compositions for π;
     for K, η, etc., search for a strange-primitive that fits.
  2. For baryons: re-derive uud, udd, uds compositions etc.
  3. Light hadrons (proton, neutron) are anchors; we expect those
     to match by construction.
  4. Strange-bearing hadrons depend on identifying a strange-quark
     primitive at Point B.

Phase 4a is a SCAN: for each strange-bearing hadron, find the
best-matching strange primitive (n_t_s, n_r_s) and report.  Whether
a single (n_t_s, n_r_s) works for ALL strange particles is the gate.

Outputs:
  outputs/track4_phase4a_inventory.csv
  outputs/track4_phase4a_strange_search.csv
"""

import math
import csv
from pathlib import Path

import numpy as np


# ─── Point B parameters ────────────────────────────────────────────────

EPS_P = 0.2052
S_P   = 0.0250
K_P   = 63.629    # MeV/μ-unit (anchored to proton at (3, +2))


# ─── Mass formula ──────────────────────────────────────────────────────

def mu2(n_t, n_r):
    return (n_t / EPS_P)**2 + (n_r - S_P * n_t)**2


def mass(n_t, n_r):
    return K_P * math.sqrt(mu2(n_t, n_r))


# ─── Sanity check on quarks and nucleons ──────────────────────────────

def sanity_check():
    print("  Sanity check at Point B:")
    print(f"    m_u = m(1, +2) = {mass(1, 2):.3f} MeV")
    print(f"    m_d = m(1, -2) = {mass(1, -2):.3f} MeV")
    print(f"    m_p = m(3, +2) = {mass(3, 2):.3f} MeV  (anchored)")
    print(f"    m_n = m(3, -2) = {mass(3, -2):.3f} MeV  (target 939.57)")
    print()


# ─── Strange-quark search at Point B ──────────────────────────────────

def search_strange_primitive():
    """For each strangeness-bearing baryon, find the best-fit
    strange primitive (n_t_s, n_r_s) consistent with Z₃ confinement
    in the resulting baryon, and report the implied m_s.

    Z₃ requires baryon n_pt ≡ 0 (mod 3).  For a baryon
    (q1, q2, q3) on the p-sheet with each q_i = (1, ±2) for u/d
    and q_s = (n_t_s, n_r_s) for strange, the baryon n_pt
    = 2 + n_t_s for one strange (Λ, Σ, K), or 1 + 2·n_t_s for
    two strange (Ξ), or 3·n_t_s for three strange (Ω).

    For Λ/Σ/K (1 strange):  n_t_s ≡ 1 (mod 3).
    For Ξ (2 strange):       n_t_s ≡ 1 (mod 3).
    For Ω (3 strange):       n_t_s ≡ 0 (mod 3) only — different class.

    In QCD/SM, the strange quark is the SAME particle in all four;
    we expect a single (n_t_s, n_r_s) to fit.  But Z₃ allows
    n_t_s ∈ {±1, ±2, ±4, ±5, ...} for one and two strange,
    and n_t_s ∈ {0, ±3, ±6, ...} for three strange.  These
    intersect only at... nowhere unless n_t_s exists in both sets.
    They don't.  So strict Z₃ confinement at the BARYON level
    (which is what matters for stable baryons) requires n_t_s
    such that the baryon's total n_pt ≡ 0 mod 3.  Since the
    constraint depends on how many strange are in the baryon,
    a SINGLE n_t_s value cannot satisfy Z₃ for all strange
    baryons under strict additive composition.

    This is a structural concern for R64.  Phase 4a documents it
    and reports the best per-particle fits anyway.
    """
    targets = [
        ("Ω⁻ (sss)",      1672.45,  3,    'sss',
         lambda nts, nrs: (3 * nts, 3 * nrs)),
        ("Ξ⁻ (dss)",      1321.71,  2,    'dss',
         lambda nts, nrs: (1 + 2 * nts, -2 + 2 * nrs)),
        ("Ξ⁰ (uss)",      1314.86,  2,    'uss',
         lambda nts, nrs: (1 + 2 * nts, +2 + 2 * nrs)),
        ("Λ (uds)",       1115.683, 1,    'uds',
         lambda nts, nrs: (2 + nts, 0 + nrs)),
        ("Σ⁺ (uus)",      1189.37,  1,    'uus',
         lambda nts, nrs: (2 + nts, +4 + nrs)),
        ("Σ⁻ (dds)",      1197.449, 1,    'dds',
         lambda nts, nrs: (2 + nts, -4 + nrs)),
        ("Σ⁰ (uds)",      1192.642, 1,    'uds',
         lambda nts, nrs: (2 + nts, 0 + nrs)),
        ("K⁺ (us̄)",       493.677,  1,    'us̄',
         lambda nts, nrs: (1 + (-nts), +2 + (-nrs))),
        ("K⁰ (ds̄)",       497.611,  1,    'ds̄',
         lambda nts, nrs: (1 + (-nts), -2 + (-nrs))),
    ]
    return targets


def lattice_scan(n_t_max=6, n_r_max=15):
    """Enumerate primitives (n_t, n_r) with masses computed at Point B."""
    primitives = []
    for n_t in range(-n_t_max, n_t_max + 1):
        if n_t == 0:
            continue
        for n_r in range(-n_r_max, n_r_max + 1):
            primitives.append((n_t, n_r, mass(n_t, n_r)))
    return primitives


# ─── Main ──────────────────────────────────────────────────────────────

def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 110)
    print("R64 Track 4 Phase 4a — Hadron inventory audit at chain-fit Point B")
    print("=" * 110)
    print()
    print(f"  Point B: ε_p = {EPS_P}, s_p = {S_P}, K_p = {K_P:.3f} MeV/μ")
    print()
    sanity_check()

    # ─── Lattice scan ──────────────────────────────────────────────
    print("Lattice scan: primitive masses at Point B (n_t in [-3, 3], n_r in [-10, 10])")
    print("-" * 110)
    print(f"  {'(n_t, n_r)':>12s}  {'mass (MeV)':>11s}")
    for n_t in [1, 2, 3]:
        for n_r in range(-6, 7):
            m = mass(n_t, n_r)
            if 200 < m < 800:
                print(f"  ({n_t:>3d},{n_r:>3d})  {m:>11.3f}")
    print()

    # ─── Strange-quark per-particle search ────────────────────────
    print("Per-particle strange-quark fit: best (n_t_s, n_r_s) for each "
          "strange-bearing hadron")
    print("-" * 110)
    targets = search_strange_primitive()
    print(f"  {'particle':>12s} {'observed':>10s}  "
          f"{'best (nts, nrs)':>18s}  {'predicted':>11s}  "
          f"{'err':>9s}  {'baryon Z₃?':>11s}")

    rows = []
    best_strange_fits = {}
    for name, m_obs, nstrange, content, tuple_fn in targets:
        # Search for best (n_t_s, n_r_s)
        best_err = float('inf')
        best_fit = None
        for n_t_s in range(-5, 6):
            for n_r_s in range(-12, 13):
                if n_t_s == 0 and n_r_s == 0:
                    continue
                total = tuple_fn(n_t_s, n_r_s)
                if total[0] == 0 and abs(total[1]) > 0:
                    continue  # skip n_t = 0 (no Z₃ check)
                m_pred = mass(*total)
                err = abs(m_pred - m_obs) / m_obs
                if err < best_err:
                    best_err = err
                    best_fit = (n_t_s, n_r_s, m_pred, total)

        nts, nrs, m_pred, tup = best_fit
        err_signed = (m_pred - m_obs) / m_obs
        z3 = "✓" if (tup[0] % 3 == 0) else "✗"
        print(f"  {name:>12s} {m_obs:>10.2f}  "
              f"({nts:>3d}, {nrs:>3d})  {m_pred:>11.3f}  "
              f"{err_signed:>+9.2%}  {z3:>11s}")
        rows.append({
            'particle': name, 'content': content,
            'm_observed': m_obs,
            'best_n_t_s': nts, 'best_n_r_s': nrs,
            'baryon_tuple': str(tup),
            'baryon_n_pt': tup[0], 'baryon_n_pr': tup[1],
            'm_predicted': m_pred,
            'rel_err': err_signed,
            'z3_compatible': (tup[0] % 3 == 0),
        })
        best_strange_fits[name] = (nts, nrs, err_signed)

    # ─── Coherence test: do all strange particles agree on (n_t_s, n_r_s)? ─
    print()
    print("Coherence: do strange particles agree on a single (n_t_s, n_r_s)?")
    print("-" * 110)
    fits = list(best_strange_fits.values())
    nts_set = set(f[0] for f in fits)
    nrs_set = set(f[1] for f in fits)
    print(f"  Distinct n_t_s values found: {sorted(nts_set)}")
    print(f"  Distinct n_r_s values found: {sorted(nrs_set)}")
    if len(nts_set) == 1 and len(nrs_set) == 1:
        print(f"  ✓ ALL particles agree on (n_t_s, n_r_s) = "
              f"({fits[0][0]}, {fits[0][1]})")
    else:
        print(f"  ✗ Strange-particle predictions inconsistent — no single")
        print(f"    (n_t_s, n_r_s) fits all strange-bearing hadrons.")

    # Try forcing single (n_t_s, n_r_s) and see global error
    print()
    print("Global fit: forcing single (n_t_s, n_r_s) for all strange hadrons")
    print("-" * 110)
    best_global_err = float('inf')
    best_global_fit = None
    for n_t_s in range(-5, 6):
        for n_r_s in range(-12, 13):
            if n_t_s == 0 and n_r_s == 0:
                continue
            sum_sq = 0
            valid = True
            for name, m_obs, nstrange, content, tuple_fn in targets:
                total = tuple_fn(n_t_s, n_r_s)
                if total[0] == 0 and abs(total[1]) > 0:
                    valid = False
                    break
                m_pred = mass(*total)
                err = (m_pred - m_obs) / m_obs
                sum_sq += err * err
            if not valid:
                continue
            rms = math.sqrt(sum_sq / len(targets))
            if rms < best_global_err:
                best_global_err = rms
                best_global_fit = (n_t_s, n_r_s)

    if best_global_fit:
        nts_g, nrs_g = best_global_fit
        print(f"  Best global (n_t_s, n_r_s) = ({nts_g}, {nrs_g})")
        print(f"  RMS error = {best_global_err:.2%}")
        print()
        print(f"  {'particle':>12s} {'observed':>10s}  "
              f"{'predicted':>11s}  {'err':>9s}")
        for name, m_obs, nstrange, content, tuple_fn in targets:
            total = tuple_fn(nts_g, nrs_g)
            m_pred = mass(*total)
            err = (m_pred - m_obs) / m_obs
            flag = "" if abs(err) < 0.05 else (
                "  >5% off" if abs(err) < 0.20 else "  ✗ shattered")
            print(f"  {name:>12s} {m_obs:>10.2f}  "
                  f"{m_pred:>11.3f}  {err:>+9.2%}{flag}")
    print()

    # ─── Save CSV ─────────────────────────────────────────────────
    csv_path = out_dir / "track4_phase4a_strange_search.csv"
    with open(csv_path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    # ─── Verdict ──────────────────────────────────────────────────
    print("=" * 110)
    print("VERDICT — Phase 4a")
    print("=" * 110)
    print()
    if len(nts_set) == 1 and len(nrs_set) == 1:
        print(f"  ✓ Strange quark identifies as single primitive at Point B.")
        print(f"  Inventory survival depends on Σ, Ξ, K mass errors.")
    else:
        print(f"  Strange quark does NOT identify as a single primitive at Point B.")
        print(f"  Different strange-bearing particles prefer different (n_t_s, n_r_s).")
        if best_global_fit:
            print(f"  Best compromise: ({best_global_fit[0]}, {best_global_fit[1]})")
            print(f"  RMS error: {best_global_err:.2%}")
            if best_global_err < 0.05:
                print(f"  → Survives 5% inventory gate ✓")
            elif best_global_err < 0.10:
                print(f"  → Marginal: 5-10% RMS error")
            else:
                print(f"  → Inventory gate failure (>10%): R64's strange "
                      f"sector doesn't fit cleanly at Point B")
    print()
    print(f"  CSV: {csv_path}")


if __name__ == "__main__":
    main()
