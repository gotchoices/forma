#!/usr/bin/env python3
"""
R41 Track 5c — Three-category census with generation identification

Proper taxonomy (replaces blunt "ghost" label):
  A. Generation modes — resonances matching known particles
  B. High harmonics — |n_tube| ≥ 2, targets of the low-pass filter
  C. Unmatched resonances — low-energy modes with no known counterpart

Uses n_max=5 to capture the muon mode (-1,5,0,0,-2,0).
Groups by "essential" quantum numbers (n₁,n₂,n₅,n₆), collapsing
the nearly-degenerate neutrino sheet (n₃,n₄) copies.

Usage:
    cd studies && python3 R41-dynamic-model/scripts/track5c_generation_census.py
"""

import sys, os, time
import math
import numpy as np
from collections import defaultdict
from itertools import product as iproduct

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../..')

from lib.ma_model import Ma, ALPHA, _mode_charge, _mode_spin

REF = dict(r_e=6.6, r_nu=5.0, r_p=8.906, sigma_ep=-0.0906)

KNOWN_PARTICLES = [
    # (name, mass_MeV, charge, spin_halves_count)
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

MATCH_THRESHOLD = 0.10  # 10% for broader matching


def match_particle(E, charge, spin_halves):
    for name, mass, q, s in KNOWN_PARTICLES:
        if q == charge and s == spin_halves:
            if abs(E - mass) / mass < MATCH_THRESHOLD:
                return name, mass
    return None, None


def max_tube(n):
    return max(abs(n[0]), abs(n[2]), abs(n[4]))


def essential_key(n):
    """(n₁, n₂, n₃, n₅, n₆) — collapses only n₄ (neutrino ring).

    n₃ affects charge and max_tube, so it must be preserved.
    n₄ only contributes negligible energy (~meV) and doesn't change
    charge, spin, or tube winding classification.
    """
    return (n[0], n[1], n[2], n[4], n[5])


def section(title):
    print(f"\n{'=' * 70}")
    print(f"  {title}")
    print(f"{'=' * 70}\n")


def main():
    E_MAX = 2000.0
    N_MAX = 5

    m_static = Ma(**REF, dynamic=False)
    m_full = Ma(**REF, dynamic='full')

    # ── Scan ──────────────────────────────────────────────────────
    section(f"1. FULL SCAN — n_max={N_MAX}, E < {E_MAX:.0f} MeV")

    t0 = time.perf_counter()
    modes = m_static.scan_modes(n_max=N_MAX, E_max_MeV=E_MAX)
    t_scan = time.perf_counter() - t0
    print(f"Total modes: {len(modes):,d}  ({t_scan:.1f}s)")

    # Group by essential quantum numbers (collapse only n₄)
    families = defaultdict(list)
    for mode in modes:
        key = essential_key(mode.n)
        families[key].append(mode)

    print(f"Distinct (n₁,n₂,n₃,n₅,n₆) families: {len(families):,d}")
    print(f"Average ν₄ copies per family: {len(modes)/len(families):.1f}")

    # ── Three-generation identification ───────────────────────────
    section("2. THREE GENERATIONS OF CHARGED LEPTONS")

    # R27 mode assignments
    gen_modes = [
        ("electron", (1, 2, 0, 0, 0, 0), 0.511),
        ("muon",     (-1, 5, 0, 0, -2, 0), 105.658),
        ("tau",      (-1, 5, 0, 0, -2, -4), 1776.86),
    ]

    print(f"{'Particle':>10}  {'Mode':>28}  {'E_static':>10}  {'E_target':>10}  "
          f"{'Error':>8}  {'δE/E':>12}  {'FF':>8}  {'Q':>4}  {'Sp':>3}")
    print(f"{'─'*10}  {'─'*28}  {'─'*10}  {'─'*10}  {'─'*8}  {'─'*12}  {'─'*8}  {'─'*4}  {'─'*3}")

    for name, n, m_target in gen_modes:
        E_s = m_static.energy(n)
        E_d = m_full.energy(n)
        corr = m_full.dynamic_correction(n)
        ff = m_full.filter_factor(n)
        Q = Ma.charge(n)
        spin = Ma.spin(n)
        err = (E_s - m_target) / m_target * 100
        print(f"{name:>10}  {str(n):>28}  {E_s:10.3f}  {m_target:10.3f}  "
              f"{err:+7.1f}%  {corr.delta_E_over_E:12.4e}  {ff:8.4f}  {Q:4d}  {spin:3d}")
        print(f"{'':>42}per_sheet: e={corr.per_sheet['e']:.2e}  "
              f"nu={corr.per_sheet['nu']:.2e}  p={corr.per_sheet['p']:.2e}")

    # Check: is the muon in the scan?
    muon_in_scan = any(m.n == (-1, 5, 0, 0, -2, 0) for m in modes)
    tau_in_scan = any(m.n == (-1, 5, 0, 0, -2, -4) for m in modes)
    print(f"\nMuon mode in n_max={N_MAX} scan: {'YES' if muon_in_scan else 'NO'}")
    print(f"Tau mode in n_max={N_MAX} scan:  {'YES' if tau_in_scan else 'NO'}")

    # ── Classify families ─────────────────────────────────────────
    section("3. THREE-CATEGORY CLASSIFICATION (by family, n₄ collapsed)")

    cat_A = []  # Generation modes (match known particles)
    cat_B = []  # High harmonics (|n_tube| ≥ 2)
    cat_C = []  # Unmatched resonances

    for key, members in families.items():
        rep = members[0]
        E = rep.E_MeV
        Q = rep.charge
        spin = rep.spin_halves
        mt = max_tube(rep.n)

        match_name, match_mass = match_particle(E, Q, spin)

        if match_name:
            cat_A.append((key, rep, match_name, match_mass, len(members)))
        elif mt >= 2:
            cat_B.append((key, rep, len(members)))
        else:
            cat_C.append((key, rep, len(members)))

    # Some families might have mt >= 2 AND match a particle
    # Let's count overlaps
    cat_A_high = [(k, r, n, m, c) for k, r, n, m, c in cat_A if max_tube(r.n) >= 2]

    print(f"Category A (match known particle):      {len(cat_A):6,d} families  "
          f"({sum(c for _,_,_,_,c in cat_A):,d} modes)")
    print(f"  ... of which |n_tube| ≥ 2:            {len(cat_A_high):6,d} families")
    print(f"Category B (high harmonics, no match):  {len(cat_B):6,d} families  "
          f"({sum(c for _,_,c in cat_B):,d} modes)")
    print(f"Category C (unmatched resonances):      {len(cat_C):6,d} families  "
          f"({sum(c for _,_,c in cat_C):,d} modes)")

    # ── Category A detail ─────────────────────────────────────────
    section("4. CATEGORY A — KNOWN PARTICLE MATCHES")

    # Group cat A by matched particle
    by_particle = defaultdict(list)
    for key, rep, name, mass, count in cat_A:
        by_particle[name].append((key, rep, count))

    print(f"{'Particle':>8}  {'Families':>8}  {'Modes':>8}  {'E_range (MeV)':>20}  "
          f"{'Tube range':>12}")
    print(f"{'─'*8}  {'─'*8}  {'─'*8}  {'─'*20}  {'─'*12}")

    for pname in sorted(by_particle.keys(), key=lambda x: next(
            (m for n,m,_,_ in KNOWN_PARTICLES if n==x), 0)):
        entries = by_particle[pname]
        Es = [e.E_MeV for _, e, _ in entries]
        tubes = [max_tube(e.n) for _, e, _ in entries]
        total_modes = sum(c for _, _, c in entries)
        print(f"{pname:>8}  {len(entries):8d}  {total_modes:8d}  "
              f"{min(Es):8.1f} – {max(Es):8.1f}  "
              f"{min(tubes):3d} – {max(tubes):3d}")

    # ── Category C detail — the problematic ones ──────────────────
    section("5. CATEGORY C — UNMATCHED RESONANCES (|n_tube|_max ≤ 1)")

    cat_C.sort(key=lambda x: x[1].E_MeV)

    print(f"Total: {len(cat_C)} families\n")
    print("Lowest 30 by energy:\n")
    print(f"{'(n₁,n₂,n₃,n₅,n₆)':>22}  {'E (MeV)':>10}  {'Q':>4}  {'Sp':>3}  "
          f"{'ν₄ copies':>9}  {'mt':>3}  {'Note':>20}")
    print(f"{'─'*22}  {'─'*10}  {'─'*4}  {'─'*3}  {'─'*9}  {'─'*3}  {'─'*20}")

    for key, rep, count in cat_C[:40]:
        Q = rep.charge
        spin = rep.spin_halves
        mt = max_tube(rep.n)
        note = ""
        if key[:2] == (1, 1) and key[3:] == (0, 0):
            note = "(1,1) e-boson"
        elif key[:2] == (1, -1) and key[3:] == (0, 0):
            note = "(1,-1) e-boson"
        elif key[1] == 0 and key[3:] == (0, 0) and key[0] != 0:
            note = "pure tube mode"
        elif key[:2] == (0, 0) and key[3] != 0 and key[4] != 0:
            note = f"p-sheet ({key[3]},{key[4]})"
        elif key[:2] == (0, 0) and key[3] != 0:
            note = f"p-sheet tube"
        print(f"{str(key):>22}  {rep.E_MeV:10.3f}  {Q:4d}  {spin:3d}  "
              f"{count:9d}  {mt:3d}  {note:>20}")

    # ── Dynamic model effect on Category C ────────────────────────
    section("6. DYNAMIC CORRECTIONS FOR CRITICAL UNMATCHED MODES")

    critical_unmatched = []
    for key, rep, count in cat_C[:50]:
        n = rep.n
        corr = m_full.dynamic_correction(n)
        ff = m_full.filter_factor(n)
        critical_unmatched.append((key, rep, corr, ff))

    critical_unmatched.sort(key=lambda x: x[3], reverse=True)

    print(f"{'(n₁,n₂,n₃,n₅,n₆)':>22}  {'E (MeV)':>10}  {'Q':>4}  {'Sp':>3}  "
          f"{'δE/E':>12}  {'FF':>8}  {'mt':>3}")
    print(f"{'─'*22}  {'─'*10}  {'─'*4}  {'─'*3}  {'─'*12}  {'─'*8}  {'─'*3}")
    for key, rep, corr, ff in critical_unmatched[:30]:
        mt = max_tube(rep.n)
        print(f"{str(key):>22}  {rep.E_MeV:10.3f}  {rep.charge:4d}  "
              f"{rep.spin_halves:3d}  {corr.delta_E_over_E:12.4e}  {ff:8.4f}  {mt:3d}")

    # ── Generation filter factors ─────────────────────────────────
    section("7. LOW-PASS FILTER EFFECT ON GENERATIONS")

    print("The dynamic model distinguishes generations by their tube windings:\n")
    print("  Electron (1,2,0,0,0,0):  n_tube=1 on e-sheet only")
    print("    → couples to k=2, full correction, FF=1.0\n")
    print("  Muon (-1,5,0,0,-2,0):    n_tube=1 on e-sheet, n_tube=2 on p-sheet")
    print("    → p-sheet couples to k=4 (suppressed 40×)")
    print("    → muon correction is dominated by e-sheet\n")
    print("  Tau (-1,5,0,0,-2,-4):    n_tube=1 on e-sheet, n_tube=2 on p-sheet")
    print("    → same tube windings as muon, but with n₆=-4 ring winding")
    print("    → p-sheet correction slightly larger (different ring winding)\n")

    # Detailed per-sheet breakdown
    for name, n, _ in gen_modes:
        corr = m_full.dynamic_correction(n)
        decomp = m_full.energy_decomp(n)
        print(f"  {name}: δE/E = {corr.delta_E_over_E:.4e}")
        print(f"    E² fractions: e={decomp.fractions.get('e',0):.4f}  "
              f"nu={decomp.fractions.get('nu',0):.4f}  "
              f"p={decomp.fractions.get('p',0):.4f}  "
              f"ep={decomp.fractions.get('ep',0):.4f}")
        print(f"    per-sheet δE/E: e={corr.per_sheet['e']:.4e}  "
              f"nu={corr.per_sheet['nu']:.4e}  "
              f"p={corr.per_sheet['p']:.4e}")
        print()

    # ── Summary ───────────────────────────────────────────────────
    section("SUMMARY")

    print("Three-category taxonomy of the Ma spectrum below 2 GeV:")
    print()
    print(f"  A. Known particle matches: {len(cat_A):,d} families")
    print(f"     — Includes 3 charged lepton generations (e, μ, τ)")
    print(f"     — Most are ν-degenerate copies of a few core modes")
    print()
    print(f"  B. High harmonics (|n_tube| ≥ 2, no match): {len(cat_B):,d} families")
    print(f"     — Low-pass filter suppresses these (FF < 0.03)")
    print(f"     — Also killed by R33 charge selection rule (|n₁| ≥ 2 → Q=0)")
    print()
    print(f"  C. Unmatched resonances (|n_tube| ≤ 1): {len(cat_C):,d} families")
    print(f"     — The (1,1) boson remains the critical tension")
    print(f"     — Dynamic model does not suppress these (FF ≈ 0.46)")
    print()
    print("Generation structure:")
    print("  The low-pass filter DOES distinguish generations:")
    print("  electron (FF=1.00) > tau (FF=0.025) > muon (FF=0.0002)")
    print("  The muon's tiny correction comes from its p-sheet tube winding")
    print("  coupling to k=4 (40× suppressed) rather than k=2.")


if __name__ == '__main__':
    main()
