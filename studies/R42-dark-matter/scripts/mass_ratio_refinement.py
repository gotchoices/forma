#!/usr/bin/env python3
"""
R42 Track 6 — Refined mass ratio under physically motivated filters

The Track 2 equal-occupation ratio (12.4) counts ALL modes equally,
including high-charge (|Q| > 5) and high-tube-winding modes that
the R33 selection rule and dynamic low-pass filter already suppress.

This track applies successive physical filters and computes the
dark/visible ratio at each stage, establishing upper and lower bounds.

Usage:
    cd studies && ../.venv/bin/python3 R42-dark-matter/scripts/mass_ratio_refinement.py
"""

import sys, os, time, math
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../..')
from lib.ma_model import Ma, _mode_charge, _mode_spin

REF = dict(r_e=6.6, r_nu=5.0, r_p=8.906, sigma_ep=-0.0906)
E_MAX = 2000.0
N_MAX = 5

KNOWN_PARTICLES = [
    ("e⁻",     0.511,   -1,  1),
    ("e⁺",     0.511,   +1,  1),
    ("μ⁻",   105.658,   -1,  1),
    ("μ⁺",   105.658,   +1,  1),
    ("τ⁻",  1776.86,    -1,  1),
    ("τ⁺",  1776.86,    +1,  1),
    ("p",    938.272,    +1,  1),
    ("p̄",    938.272,    -1,  1),
    ("n",    939.565,     0,  1),
    ("π⁺",   139.570,   +1,  0),
    ("π⁻",   139.570,   -1,  0),
    ("π⁰",   134.977,    0,  0),
    ("K⁺",   493.677,   +1,  0),
    ("K⁻",   493.677,   -1,  0),
    ("K⁰",   497.611,    0,  0),
    ("η",    547.862,    0,  0),
    ("ρ",    775.26,     0,  2),
    ("ω",    782.66,     0,  2),
    ("η′",   957.78,     0,  0),
    ("φ",   1019.461,    0,  2),
    ("Λ",   1115.683,    0,  1),
    ("Σ⁺",  1189.37,    +1,  1),
    ("Σ⁰",  1192.642,    0,  1),
    ("Σ⁻",  1197.449,   -1,  1),
    ("Δ",   1232.0,      0,  3),
    ("Ξ⁰",  1314.86,     0,  1),
    ("Ξ⁻",  1321.71,    -1,  1),
    ("Ω⁻",  1672.45,    -1,  3),
]

MATCH_THRESHOLD = 0.10


def match_particle(E, charge, spin_halves):
    for name, mass, q, s in KNOWN_PARTICLES:
        if q == charge and s == spin_halves:
            if abs(E - mass) / mass < MATCH_THRESHOLD:
                return name, mass
    return None, None


def max_tube(n):
    return max(abs(n[0]), abs(n[2]), abs(n[4]))


def essential_key(n):
    return (n[0], n[1], n[2], n[4], n[5])


def section(title):
    print(f"\n{'=' * 72}")
    print(f"  {title}")
    print(f"{'=' * 72}\n")


def main():
    model = Ma(**REF, dynamic=False)

    t0 = time.perf_counter()
    modes = model.scan_modes(n_max=N_MAX, E_max_MeV=E_MAX)
    t_scan = time.perf_counter() - t0
    print(f"Scanned {len(modes):,d} modes in {t_scan:.1f}s")

    # Build families
    families = defaultdict(list)
    for m in modes:
        families[essential_key(m.n)].append(m)

    # Classify each family
    family_data = []
    for key, members in families.items():
        rep = members[0]
        name, _ = match_particle(rep.E_MeV, rep.charge, rep.spin_halves)
        mt = max_tube(rep.n)
        family_data.append({
            'key': key,
            'E': rep.E_MeV,
            'Q': rep.charge,
            'spin': rep.spin_halves,
            'mt': mt,
            'visible': name is not None,
            'n': rep.n,
            'name': name,
        })

    vis_base = [f for f in family_data if f['visible']]
    dark_base = [f for f in family_data if not f['visible']]
    print(f"Families: {len(family_data):,d} total, "
          f"{len(vis_base):,d} visible, {len(dark_base):,d} dark\n")

    # ══════════════════════════════════════════════════════════════
    section("FILTER ANALYSIS: DARK/VISIBLE RATIO UNDER SUCCESSIVE CUTS")

    def ratio_report(label, dark, vis):
        sm_d = sum(f['E'] for f in dark)
        sm_v = sum(f['E'] for f in vis)
        r = sm_d / max(sm_v, 1e-300)
        avg_d = sm_d / max(len(dark), 1)
        avg_v = sm_v / max(len(vis), 1)
        print(f"  {label}")
        print(f"    Dark: {len(dark):,d} families, Σm = {sm_d:,.0f} MeV, <m> = {avg_d:.1f} MeV")
        print(f"    Vis:  {len(vis):,d} families, Σm = {sm_v:,.0f} MeV, <m> = {avg_v:.1f} MeV")
        print(f"    DM/vis = {r:.2f}   (target: 5.4)")
        print()
        return r

    print("--- A. No filter (all families) ---")
    r_all = ratio_report("All modes", dark_base, vis_base)

    # Filter 1: |Q| ≤ 1 (R33 says |n₁| > 1 modes don't produce charge)
    # But note: |Q| > 1 modes DO exist with |n₁| = 1 (because Q = -n₁ + n₅)
    # The R33 rule kills modes with |n₁| > 1, not |Q| > 1
    # However, modes with large |Q| require large |n₅|, which means
    # large proton-sheet tube winding — also suppressed.
    print("--- B. Charge filter: |Q| ≤ 2 ---")
    dark_q2 = [f for f in dark_base if abs(f['Q']) <= 2]
    vis_q2 = [f for f in vis_base if abs(f['Q']) <= 2]
    r_q2 = ratio_report("|Q| ≤ 2", dark_q2, vis_q2)

    print("--- C. Charge filter: |Q| ≤ 1 ---")
    dark_q1 = [f for f in dark_base if abs(f['Q']) <= 1]
    vis_q1 = [f for f in vis_base if abs(f['Q']) <= 1]
    r_q1 = ratio_report("|Q| ≤ 1", dark_q1, vis_q1)

    # Filter 2: max tube winding
    for mt_max in [5, 4, 3, 2, 1]:
        label = f"max|n_tube| ≤ {mt_max}"
        dark_mt = [f for f in dark_base if f['mt'] <= mt_max]
        vis_mt = [f for f in vis_base if f['mt'] <= mt_max]
        print(f"--- D{mt_max}. Tube filter: {label} ---")
        ratio_report(label, dark_mt, vis_mt)

    # Combined filters
    print("--- E. Combined: |Q| ≤ 1 AND max|n_tube| ≤ 2 ---")
    dark_comb = [f for f in dark_base if abs(f['Q']) <= 1 and f['mt'] <= 2]
    vis_comb = [f for f in vis_base if abs(f['Q']) <= 1 and f['mt'] <= 2]
    r_comb = ratio_report("|Q| ≤ 1, mt ≤ 2", dark_comb, vis_comb)

    print("--- F. Combined: |Q| ≤ 1 AND max|n_tube| ≤ 1 ---")
    dark_tight = [f for f in dark_base if abs(f['Q']) <= 1 and f['mt'] <= 1]
    vis_tight = [f for f in vis_base if abs(f['Q']) <= 1 and f['mt'] <= 1]
    r_tight = ratio_report("|Q| ≤ 1, mt ≤ 1", dark_tight, vis_tight)

    print("--- G. Neutral only: Q = 0 ---")
    dark_neutral = [f for f in dark_base if f['Q'] == 0]
    vis_neutral = [f for f in vis_base if f['Q'] == 0]
    r_neutral = ratio_report("Q = 0 only", dark_neutral, vis_neutral)

    print("--- H. Neutral AND max|n_tube| ≤ 1 ---")
    dark_n_tight = [f for f in dark_base if f['Q'] == 0 and f['mt'] <= 1]
    vis_n_tight = [f for f in vis_base if f['Q'] == 0 and f['mt'] <= 1]
    r_n_tight = ratio_report("Q = 0, mt ≤ 1", dark_n_tight, vis_n_tight)

    # ══════════════════════════════════════════════════════════════
    section("MASS-WEIGHTED RATIO WITH PROTON DOMINANCE")

    # In the real universe, visible matter is ~99% protons/neutrons
    # by mass. Let's compute the ratio using only stable baryonic
    # matter as the visible baseline.
    proton_mass = 938.272
    neutron_mass = 939.565

    # Visible mass = protons + neutrons (the rest is negligible in
    # cosmic abundance). Each baryon species has ~equal number density.
    # Use total visible family mass as before for comparison, but also
    # compute with just p + n.
    vis_baryon_mass = proton_mass + neutron_mass  # per baryon pair

    print("If visible matter = protons + neutrons only (2 species):\n")
    for label, dark_set in [
        ("All dark families", dark_base),
        ("|Q| ≤ 1", dark_q1),
        ("|Q| ≤ 1, mt ≤ 2", dark_comb),
        ("|Q| ≤ 1, mt ≤ 1", dark_tight),
        ("Q = 0", dark_neutral),
        ("Q = 0, mt ≤ 1", dark_n_tight),
    ]:
        n_dark = len(dark_set)
        avg_dark = sum(f['E'] for f in dark_set) / max(n_dark, 1)
        # If each dark species has same number density as one baryon species:
        # DM/vis = N_dark_species × <m_dark> / (2 × m_baryon_avg)
        r = n_dark * avg_dark / vis_baryon_mass
        print(f"  {label:30s}  N_dark={n_dark:>8,d}  <m>={avg_dark:>8.1f} MeV  "
              f"DM/vis={r:>10.1f}")

    print("\n  These ratios assume equal number density per species.")
    print("  Real ratio depends on freeze-out / production mechanism.")

    # ══════════════════════════════════════════════════════════════
    section("WHAT NUMBER DENSITY RATIO IS NEEDED?")

    # DM/vis = 5.4 = (N_species × n_per_species × <m_dark>) /
    #                 (2 × n_baryon × m_baryon)
    # If n_per_species = f × n_baryon, then:
    # f = 5.4 × 2 × m_baryon / (N_species × <m_dark>)

    print("Required number density per dark species (as fraction of baryon density)")
    print("to give DM/vis = 5.4:\n")
    print(f"{'Filter':>30s}  {'N_dark':>8}  {'<m> MeV':>8}  {'f = n_dark/n_baryon':>20}")
    print(f"{'─'*30}  {'─'*8}  {'─'*8}  {'─'*20}")

    m_baryon = (proton_mass + neutron_mass) / 2
    for label, dark_set in [
        ("All dark families", dark_base),
        ("|Q| ≤ 1", dark_q1),
        ("|Q| ≤ 1, mt ≤ 2", dark_comb),
        ("|Q| ≤ 1, mt ≤ 1", dark_tight),
        ("Q = 0", dark_neutral),
        ("Q = 0, mt ≤ 1", dark_n_tight),
    ]:
        n_dark = len(dark_set)
        if n_dark == 0:
            continue
        avg_dark = sum(f['E'] for f in dark_set) / n_dark
        # 5.4 = f × N × <m_dark> / (2 × m_baryon)
        f = 5.4 * 2 * m_baryon / (n_dark * avg_dark)
        print(f"  {label:>30s}  {n_dark:8,d}  {avg_dark:8.1f}  {f:20.6f}")

    # ══════════════════════════════════════════════════════════════
    section("SENSITIVITY TO n_max (SCAN RANGE)")

    # Our n_max=5 scan includes modes up to |n_i| = 5. Higher n_max
    # would find more modes. How does the ratio scale?
    # The number of families grows roughly as n_max^k where k depends
    # on dimensionality. Let's estimate by comparing n_max=3 vs n_max=5.

    print("Running n_max=3 scan for comparison...")
    t0 = time.perf_counter()
    modes3 = model.scan_modes(n_max=3, E_max_MeV=E_MAX)
    t3 = time.perf_counter() - t0
    print(f"n_max=3: {len(modes3):,d} modes in {t3:.1f}s")

    fam3 = defaultdict(list)
    for m in modes3:
        fam3[essential_key(m.n)].append(m)

    vis3 = []
    dark3 = []
    for key, members in fam3.items():
        rep = members[0]
        name, _ = match_particle(rep.E_MeV, rep.charge, rep.spin_halves)
        if name:
            vis3.append(rep)
        else:
            dark3.append(rep)

    sm_v3 = sum(m.E_MeV for m in vis3)
    sm_d3 = sum(m.E_MeV for m in dark3)
    r3 = sm_d3 / max(sm_v3, 1e-300)

    print(f"n_max=3: {len(vis3):,d} vis, {len(dark3):,d} dark, ratio = {r3:.2f}")
    print(f"n_max=5: {len(vis_base):,d} vis, {len(dark_base):,d} dark, ratio = {r_all:.2f}")
    print(f"\nRatio is {'stable' if abs(r3 - r_all) / r_all < 0.3 else 'sensitive'} "
          f"to n_max ({r3:.2f} vs {r_all:.2f})")

    # ══════════════════════════════════════════════════════════════
    section("DETAIL: LIGHTEST DARK MODES IN THE CRITICAL FILTERS")

    for label, dark_set in [
        ("|Q| ≤ 1, mt ≤ 1 (tightest physical filter)", dark_tight),
        ("Q = 0, mt ≤ 1 (strictly neutral)", dark_n_tight),
    ]:
        print(f"\n--- {label} ---")
        dark_sorted = sorted(dark_set, key=lambda f: f['E'])
        print(f"{'(n₁,n₂,n₃,n₅,n₆)':>22}  {'E (MeV)':>10}  {'Q':>4}  {'Sp':>3}  {'mt':>3}")
        print(f"{'─'*22}  {'─'*10}  {'─'*4}  {'─'*3}  {'─'*3}")
        for f in dark_sorted[:25]:
            print(f"{str(f['key']):>22}  {f['E']:10.4f}  {f['Q']:4d}  "
                  f"{f['spin']:3d}  {f['mt']:3d}")

    # ══════════════════════════════════════════════════════════════
    section("SUMMARY TABLE")

    print(f"{'Filter':>35s}  {'N_dark':>7}  {'N_vis':>6}  {'DM/vis':>7}  {'vs 5.4':>8}")
    print(f"{'─'*35}  {'─'*7}  {'─'*6}  {'─'*7}  {'─'*8}")

    summary_data = [
        ("No filter (all families)", dark_base, vis_base),
        ("|Q| ≤ 2", dark_q2, vis_q2),
        ("|Q| ≤ 1", dark_q1, vis_q1),
        ("max|n_tube| ≤ 2", 
         [f for f in dark_base if f['mt'] <= 2],
         [f for f in vis_base if f['mt'] <= 2]),
        ("max|n_tube| ≤ 1",
         [f for f in dark_base if f['mt'] <= 1],
         [f for f in vis_base if f['mt'] <= 1]),
        ("|Q| ≤ 1 AND mt ≤ 2", dark_comb, vis_comb),
        ("|Q| ≤ 1 AND mt ≤ 1", dark_tight, vis_tight),
        ("Q = 0 only", dark_neutral, vis_neutral),
        ("Q = 0 AND mt ≤ 1", dark_n_tight, vis_n_tight),
    ]

    for label, ds, vs in summary_data:
        sm_d = sum(f['E'] for f in ds)
        sm_v = sum(f['E'] for f in vs)
        r = sm_d / max(sm_v, 1e-300)
        factor = r / 5.4
        print(f"  {label:>35s}  {len(ds):7,d}  {len(vs):6,d}  {r:7.2f}  {factor:7.2f}×")

    print(f"\n  Observed astrophysical DM/baryon: 5.36 ± 0.05 (Planck 2018)")
    print(f"  Our range: {min(r for _, ds, vs in summary_data if (r := sum(f['E'] for f in ds) / max(sum(f['E'] for f in vs), 1e-300)) > 0):.2f} "
          f"to {max(r for _, ds, vs in summary_data if (r := sum(f['E'] for f in ds) / max(sum(f['E'] for f in vs), 1e-300)) > 0):.2f}")
    print(f"  5.4 is within this range: "
          f"{'YES' if any(abs(sum(f['E'] for f in ds)/max(sum(f['E'] for f in vs),1e-300) - 5.4) < 2 for _, ds, vs in summary_data) else 'NO'}")


if __name__ == '__main__':
    main()
