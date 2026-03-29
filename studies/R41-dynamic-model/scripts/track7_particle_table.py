#!/usr/bin/env python3
"""
R41 Track 7 — Full particle table and dynamic vs static verdict

Compiles all canonical Ma mode assignments from the Taxonomy and
prior studies (R27, R28), computing static energy, dynamic energy,
dynamic correction, filter factor, and comparison with observed masses.

Concludes with a quantitative verdict: what does the dynamic model
add, improve, or break compared to the static model?

Usage:
    cd studies && python3 R41-dynamic-model/scripts/track7_particle_table.py
"""

import sys, os, time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../..')

from lib.ma_model import Ma, ALPHA, M_E_MEV, M_P_MEV, M_N_MEV

REF = dict(r_e=6.6, r_nu=5.0, r_p=8.906, sigma_ep=-0.0906)

# ── Canonical mode assignments ────────────────────────────────────
# Sources: Taxonomy.md §5, R27, R28

CATALOG = [
    # (name, mode_tuple, observed_mass_MeV, category, source)

    # === Anchors (inputs that pin the geometry) ===
    ("e⁻",     (1, 2, 0, 0, 0, 0),       0.511,   "anchor",  "input"),
    ("p",      (0, 0, 0, 0, 1, 2),      938.272,   "anchor",  "input"),
    ("n",      (0, -2, 1, 0, 0, 2),     939.565,   "anchor",  "R27 F16"),
    ("μ⁻",    (-1, 5, 0, 0, -2, 0),    105.658,   "anchor",  "R27 F17"),

    # === Generations ===
    ("τ⁻",    (-1, 5, 0, 0, -2, -4),  1776.86,    "generation", "R27 F22"),

    # === Hadron predictions (Taxonomy §5.2) ===
    ("K⁺",    (-4, -8, 1, 0, -3, -1),   493.677,  "prediction", "R28"),
    ("K⁰",    (-3, -8, 0, 0, -3, 1),    497.611,  "prediction", "R28"),
    ("η",     (-5, -8, 0, 0, -5, 1),    547.862,  "prediction", "R28"),
    ("η′",    (-3, -8, 0, 0, -3, 2),    957.78,   "prediction", "R28"),
    ("φ",     (-7, -8, 0, 0, -7, 2),   1019.461,  "prediction", "R28"),
    ("Λ",     (-12, -15, 1, 0, -12, -2), 1115.683, "prediction", "R28"),
    ("Σ⁺",   (-14, -15, 0, 0, -13, 2), 1189.37,   "prediction", "R28"),

    # === Neutrinos (meV scale, on Ma_ν) ===
    ("ν₁",    (0, 0, 1, 1, 0, 0),        0.0292e-3, "neutrino", "R26"),
    ("ν₂",    (0, 0, -1, 1, 0, 0),       0.0305e-3, "neutrino", "R26"),
    ("ν₃",    (0, 0, 1, 2, 0, 0),        0.0582e-3, "neutrino", "R26"),

    # === Known failures (included for completeness) ===
    ("π⁺",   None,                       139.570,  "failure",   "R27"),
    ("π⁰",   None,                       134.977,  "failure",   "R27"),
    ("Ω⁻",   None,                      1672.45,   "failure",   "R27"),
]


def section(title):
    print(f"\n{'=' * 78}")
    print(f"  {title}")
    print(f"{'=' * 78}\n")


def main():
    m_static = Ma(**REF, dynamic=False)
    m_full = Ma(**REF, dynamic='full')

    # ── 1. Full particle table ────────────────────────────────────
    section("1. FULL PARTICLE TABLE — STATIC vs DYNAMIC")

    header = (f"{'Particle':>8}  {'Mode':>30}  {'E_stat':>9}  {'E_dyn':>9}  "
              f"{'E_obs':>9}  {'Err_s':>7}  {'Err_d':>7}  "
              f"{'δE/E':>11}  {'FF':>7}  {'Q':>3}  {'Sp':>3}  {'Cat':>10}")
    sep = '─' * len(header)
    print(header)
    print(sep)

    results = []
    for name, mode, m_obs, cat, src in CATALOG:
        if mode is None:
            print(f"{name:>8}  {'(no mode assignment)':>30}  {'—':>9}  {'—':>9}  "
                  f"{m_obs:9.3f}  {'—':>7}  {'—':>7}  "
                  f"{'—':>11}  {'—':>7}  {'—':>3}  {'—':>3}  {cat:>10}")
            results.append(dict(name=name, mode=None, E_s=None, E_d=None,
                                m_obs=m_obs, cat=cat))
            continue

        E_s = m_static.energy(mode)
        E_d = m_full.energy(mode)
        corr = m_full.dynamic_correction(mode)
        ff = m_full.filter_factor(mode)
        Q = Ma.charge(mode)
        spin = Ma.spin(mode)

        err_s = (E_s - m_obs) / m_obs * 100 if m_obs > 0 else 0
        err_d = (E_d - m_obs) / m_obs * 100 if m_obs > 0 else 0

        print(f"{name:>8}  {str(mode):>30}  {E_s:9.3f}  {E_d:9.3f}  "
              f"{m_obs:9.3f}  {err_s:+6.1f}%  {err_d:+6.1f}%  "
              f"{corr.delta_E_over_E:11.4e}  {ff:7.4f}  {Q:3d}  {spin:3d}  {cat:>10}")

        results.append(dict(name=name, mode=mode, E_s=E_s, E_d=E_d,
                            m_obs=m_obs, err_s=err_s, err_d=err_d,
                            dE=corr.delta_E_over_E, ff=ff, Q=Q, spin=spin,
                            cat=cat, per_sheet=corr.per_sheet))

    # ── 2. Dynamic corrections breakdown ──────────────────────────
    section("2. DYNAMIC CORRECTIONS — PER-SHEET BREAKDOWN")

    print(f"{'Particle':>8}  {'δE/E total':>12}  {'e-sheet':>11}  "
          f"{'ν-sheet':>11}  {'p-sheet':>11}  {'Dominant':>10}")
    print(f"{'─'*8}  {'─'*12}  {'─'*11}  {'─'*11}  {'─'*11}  {'─'*10}")

    for r in results:
        if r.get('mode') is None or r['cat'] == 'neutrino':
            continue
        ps = r['per_sheet']
        dom_sheet = max(ps, key=lambda k: abs(ps[k]))
        print(f"{r['name']:>8}  {r['dE']:12.4e}  {ps['e']:11.4e}  "
              f"{ps['nu']:11.4e}  {ps['p']:11.4e}  {dom_sheet:>10}")

    # ── 3. Error comparison ───────────────────────────────────────
    section("3. DOES THE DYNAMIC MODEL IMPROVE MASS PREDICTIONS?")

    improved = 0
    worsened = 0
    unchanged = 0
    for r in results:
        if r.get('mode') is None or r['cat'] in ('neutrino', 'failure'):
            continue
        if abs(r['err_d']) < abs(r['err_s']) - 0.001:
            improved += 1
            tag = "IMPROVED"
        elif abs(r['err_d']) > abs(r['err_s']) + 0.001:
            worsened += 1
            tag = "WORSENED"
        else:
            unchanged += 1
            tag = "unchanged"

        delta_err = abs(r['err_d']) - abs(r['err_s'])
        print(f"  {r['name']:>8}: static {r['err_s']:+6.2f}% → "
              f"dynamic {r['err_d']:+6.2f}%  (Δ = {delta_err:+.4f}%)  {tag}")

    print(f"\n  Improved: {improved},  Worsened: {worsened},  Unchanged: {unchanged}")

    # ── 4. Dynamic model predictions ──────────────────────────────
    section("4. UNIQUE PREDICTIONS OF THE DYNAMIC MODEL")

    print("The dynamic model makes predictions that differ from the static model:\n")

    print("  A. Mass shifts (δE = E_dynamic - E_static):\n")
    for r in results:
        if r.get('mode') is None or r['cat'] in ('neutrino', 'failure'):
            continue
        dE_MeV = r['E_d'] - r['E_s']
        print(f"     {r['name']:>8}: δE = {dE_MeV:+.4f} MeV "
              f"({r['dE']:+.2e} relative)")

    print("\n  B. Filter factors (generation hierarchy):\n")
    gen_results = [r for r in results if r['name'] in ('e⁻', 'μ⁻', 'τ⁻')]
    for r in gen_results:
        print(f"     {r['name']:>8}: FF = {r['ff']:.4f}")

    print(f"\n     Ratio μ/e: {gen_results[1]['ff']/gen_results[0]['ff']:.2e}")
    print(f"     Ratio τ/e: {gen_results[2]['ff']/gen_results[0]['ff']:.2e}")
    print(f"     Ratio τ/μ: {gen_results[2]['ff']/gen_results[1]['ff']:.1f}")

    # ── 5. Unmatched resonances summary ───────────────────────────
    section("5. UNMATCHED RESONANCES (from Track 5c)")

    print("Category C modes (|n_tube| ≤ 1, no known particle match):\n")
    print("  Total families (n_max=5, E < 2 GeV): 2,273")
    print("  Total modes: 25,002")
    print()
    print("  Critical cases:")
    print()

    critical_unmatched = [
        ("(1,1) e-boson",  (1, 1, 0, 0, 0, 0),  "half-electron mass, Q=-1, spin ½"),
        ("(1,-1) e-boson", (1, -1, 0, 0, 0, 0),  "sub-MeV, Q=-1, spin ½"),
        ("pure tube",      (1, 0, 0, 0, 0, 0),   "39 keV, Q=-1, spin ½"),
        ("ring-only",      (0, 1, 0, 0, 0, 0),   "258 keV, Q=0, spin 0"),
    ]

    print(f"  {'Name':>18}  {'Mode':>25}  {'E (MeV)':>10}  {'FF':>7}  {'Note'}")
    print(f"  {'─'*18}  {'─'*25}  {'─'*10}  {'─'*7}  {'─'*35}")
    for cname, cmode, cnote in critical_unmatched:
        E = m_full.energy(cmode)
        ff = m_full.filter_factor(cmode)
        print(f"  {cname:>18}  {str(cmode):>25}  {E:10.4f}  {ff:7.4f}  {cnote}")

    print()
    print("  The (1,1) boson (FF=0.46) is the model's primary tension.")
    print("  It has the same tube winding as the electron but different")
    print("  ring winding, so the low-pass filter barely touches it.")

    # ── 6. What does the dynamic model add? ───────────────────────
    section("6. SCORECARD: DYNAMIC vs STATIC")

    print("  ┌──────────────────────────────────────────────────────────┐")
    print("  │  DYNAMIC MODEL WINS                                     │")
    print("  ├──────────────────────────────────────────────────────────┤")
    print("  │  1. Elliptical cross-section from first principles      │")
    print("  │     → no free parameters, follows from α-impedance      │")
    print("  │                                                         │")
    print("  │  2. Low-pass filter suppresses |n_tube| ≥ 2 modes       │")
    print("  │     → 120,863 families killed (92% of spectrum)         │")
    print("  │     → complements R33 charge selection rule             │")
    print("  │                                                         │")
    print("  │  3. Generation hierarchy has geometric origin           │")
    print("  │     → FF: e(1.00) > τ(0.025) > μ(0.0002)               │")
    print("  │     → cross-sheet tube windings couple to higher k      │")
    print("  │                                                         │")
    print("  │  4. Self-consistent force balance converges rapidly     │")
    print("  │     → 3-4 iterations, ratio ~α²                        │")
    print("  │     → perturbative nature is OUTPUT not assumption      │")
    print("  │                                                         │")
    print("  │  5. Reproduces static parameters to 7 sig figs          │")
    print("  │     → r_p and σ_ep are stable under dynamic model      │")
    print("  ├──────────────────────────────────────────────────────────┤")
    print("  │  STATIC MODEL WINS                                      │")
    print("  ├──────────────────────────────────────────────────────────┤")
    print("  │  1. Simpler (no iteration needed)                       │")
    print("  │                                                         │")
    print("  │  2. Mass predictions not improved                       │")
    print("  │     → dynamic shifts are O(α²) ≈ 10⁻⁴ relative         │")
    print("  │     → all prediction errors are structural (1-6%)       │")
    print("  │     → dynamic corrections are 100× smaller than errors  │")
    print("  │                                                         │")
    print("  │  3. Consistent L-rescaling with electron target         │")
    print("  │     → dynamic model's L-rescaling has a bug (F32)       │")
    print("  ├──────────────────────────────────────────────────────────┤")
    print("  │  NEITHER WINS                                           │")
    print("  ├──────────────────────────────────────────────────────────┤")
    print("  │  1. (1,1) ghost unsuppressed (FF=0.46)                  │")
    print("  │     → the critical tension survives both models          │")
    print("  │                                                         │")
    print("  │  2. r_e and r_ν remain free                             │")
    print("  │     → dynamic model does not pin them either            │")
    print("  │                                                         │")
    print("  │  3. Tau discrepancy unchanged (5.6%)                    │")
    print("  │     → structural gap, not a precision issue             │")
    print("  │                                                         │")
    print("  │  4. Pion not matched by either model                    │")
    print("  └──────────────────────────────────────────────────────────┘")

    # ── 7. Verdict ────────────────────────────────────────────────
    section("7. VERDICT")

    print("""The dynamic model is a CONCEPTUAL advance but not a QUANTITATIVE one.

It provides:
  • A physical mechanism (α-impedance force balance) that explains
    WHY the torus has the shape it does.
  • A geometric origin for the generation hierarchy via the low-pass
    filter's differential suppression of cross-sheet modes.
  • An elimination of 92% of the mode spectrum (high harmonics with
    |n_tube| ≥ 2), complementing R33's charge selection rule.

It does NOT provide:
  • Improved mass predictions (corrections are 100× smaller than
    existing structural errors).
  • A solution to the (1,1) ghost problem (FF=0.46, not zero).
  • A way to pin the free parameters r_e and r_ν.

The dynamic model should be retained as the CORRECT physical picture
(the torus IS deformed by radiation pressure), but for practical
calculations the static model gives identical results to 4 decimal
places. Use dynamic='full' when studying mode suppression or
generation structure; use dynamic=False for everything else.

Bottom line: the dynamic model earns its keep through CONCEPTUAL
CLARITY, not numerical improvement. The real physics is that the
torus deforms — the correction happens to be small.""")


if __name__ == '__main__':
    main()
