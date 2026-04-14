"""
R58 Track 1: Systematic binary compound phonon survey

For every binary compound A-B from a pool of common elements,
estimate the TO optical phonon frequency and score against
the 12 neutrino target frequencies (4 families × 3 eigenstates).

Method:
  1. Group compounds by bond type (III-V, II-VI, IV-IV, I-VII, etc.)
  2. For each group, calibrate the spring constant k from a known
     compound's measured phonon frequency
  3. Estimate f_TO = (1/2π)√(k/μ) for every compound in the group
  4. For compounds not in any calibrated group, use a cross-group
     average k (less accurate but still informative)
  5. Score against all 12 target frequencies
"""

import math
from collections import defaultdict

# ════════════════════════════════════════════════════════════════
#  Neutrino target frequencies (THz)
# ════════════════════════════════════════════════════════════════

FAMILIES = {
    'A': [7.06, 7.37, 14.07],
    'B': [1.23, 2.44, 12.11],
    'C': [0.82, 2.25, 12.28],
    'D': [7.16, 7.45, 14.00],
}

ALL_TARGETS = []
for fam, freqs in FAMILIES.items():
    for i, f in enumerate(freqs):
        ALL_TARGETS.append((f, fam, f'ν_{i+1}'))

# ════════════════════════════════════════════════════════════════
#  Element data: symbol, mass (amu), common valence group
# ════════════════════════════════════════════════════════════════

ELEMENTS = {
    # Group I
    'Li': (6.94, 'I'), 'Na': (22.99, 'I'), 'K': (39.10, 'I'),
    'Rb': (85.47, 'I'), 'Cs': (132.91, 'I'),
    'Cu': (63.55, 'I/II'), 'Ag': (107.87, 'I'),
    'Au': (196.97, 'I'),
    # Group II
    'Be': (9.01, 'II'), 'Mg': (24.31, 'II'), 'Ca': (40.08, 'II'),
    'Sr': (87.62, 'II'), 'Ba': (137.33, 'II'),
    'Zn': (65.38, 'II'), 'Cd': (112.41, 'II'),
    # Group III
    'B': (10.81, 'III'), 'Al': (26.98, 'III'), 'Ga': (69.72, 'III'),
    'In': (114.82, 'III'), 'Tl': (204.38, 'III'),
    # Group IV
    'C': (12.01, 'IV'), 'Si': (28.09, 'IV'), 'Ge': (72.63, 'IV'),
    'Sn': (118.71, 'IV'), 'Pb': (207.2, 'IV'),
    # Group V
    'N': (14.01, 'V'), 'P': (30.97, 'V'), 'As': (74.92, 'V'),
    'Sb': (121.76, 'V'), 'Bi': (208.98, 'V'),
    # Group VI
    'O': (16.00, 'VI'), 'S': (32.07, 'VI'), 'Se': (78.96, 'VI'),
    'Te': (127.60, 'VI'),
    # Group VII (halogens)
    'F': (19.00, 'VII'), 'Cl': (35.45, 'VII'), 'Br': (79.90, 'VII'),
    'I': (126.90, 'VII'),
    # Transition metals (selected)
    'Ti': (47.87, 'TM'), 'V': (50.94, 'TM'), 'Cr': (52.00, 'TM'),
    'Mn': (54.94, 'TM'), 'Fe': (55.85, 'TM'), 'Co': (58.93, 'TM'),
    'Ni': (58.69, 'TM'), 'Zr': (91.22, 'TM'), 'Nb': (92.91, 'TM'),
    'Mo': (95.95, 'TM'), 'Pd': (106.42, 'TM'), 'W': (183.84, 'TM'),
    'Pt': (195.08, 'TM'), 'La': (138.91, 'TM'), 'Y': (88.91, 'TM'),
    # Hydrogen isotopes
    'H': (1.008, 'I'), 'D': (2.014, 'I'),
}

# ════════════════════════════════════════════════════════════════
#  Calibration: known phonon frequencies
# ════════════════════════════════════════════════════════════════

CALIBRATORS = {
    # III-V compounds
    'III-V': {
        'GaAs': ('Ga', 'As', 8.0),
        'GaP':  ('Ga', 'P', 11.0),
        'InAs': ('In', 'As', 6.5),
        'InP':  ('In', 'P', 9.1),
        'InSb': ('In', 'Sb', 5.5),
        'AlAs': ('Al', 'As', 10.8),
        'GaSb': ('Ga', 'Sb', 6.8),
        'AlSb': ('Al', 'Sb', 9.8),
        'BN':   ('B', 'N', 31.4),
        'AlN':  ('Al', 'N', 21.3),
        'GaN':  ('Ga', 'N', 16.3),
    },
    # II-VI compounds
    'II-VI': {
        'ZnSe': ('Zn', 'Se', 6.2),
        'ZnS':  ('Zn', 'S', 9.7),
        'ZnTe': ('Zn', 'Te', 5.3),
        'CdTe': ('Cd', 'Te', 4.2),
        'CdS':  ('Cd', 'S', 7.0),
        'CdSe': ('Cd', 'Se', 5.4),
        'ZnO':  ('Zn', 'O', 12.0),
    },
    # IV-IV compounds
    'IV-IV': {
        'SiC':  ('Si', 'C', 23.9),
    },
    # I-VII (alkali halides)
    'I-VII': {
        'NaCl': ('Na', 'Cl', 4.9),
        'KBr':  ('K', 'Br', 3.4),
        'LiF':  ('Li', 'F', 9.2),
        'NaF':  ('Na', 'F', 7.7),
        'KCl':  ('K', 'Cl', 4.3),
        'CsI':  ('Cs', 'I', 1.8),
    },
    # II-IV (lead chalcogenides etc)
    'IV-VI': {
        'PbTe': ('Pb', 'Te', 1.0),
        'PbSe': ('Pb', 'Se', 1.3),
        'PbS':  ('Pb', 'S', 2.0),
        'SnTe': ('Sn', 'Te', 1.5),
    },
}


def reduced_mass(sym1, sym2):
    m1 = ELEMENTS[sym1][0]
    m2 = ELEMENTS[sym2][0]
    return m1 * m2 / (m1 + m2)


def derive_k(sym1, sym2, f_measured):
    """Derive spring constant k from measured frequency."""
    mu = reduced_mass(sym1, sym2)
    mu_kg = mu * 1.6605e-27
    omega = 2 * math.pi * f_measured * 1e12
    k = omega**2 * mu_kg
    return k


def estimate_freq(k, sym1, sym2):
    """Estimate TO phonon frequency from spring constant and masses."""
    mu = reduced_mass(sym1, sym2)
    mu_kg = mu * 1.6605e-27
    omega = math.sqrt(k / mu_kg)
    return omega / (2 * math.pi * 1e12)


def score_against_targets(f):
    """Find best matching target frequency."""
    best = None
    for target_f, fam, label in ALL_TARGETS:
        d = abs(f - target_f)
        pct = d / target_f * 100
        if best is None or d < best[0]:
            best = (d, pct, target_f, fam, label)
    return best


def main():
    print("=" * 78)
    print("R58 Track 1: Binary compound phonon survey")
    print("=" * 78)
    print()

    # ── Derive k for each bond-type family ─────────────────────
    family_k = {}
    for family_name, compounds in CALIBRATORS.items():
        ks = []
        for name, (s1, s2, f) in compounds.items():
            k = derive_k(s1, s2, f)
            ks.append(k)
        k_avg = sum(ks) / len(ks)
        k_min = min(ks)
        k_max = max(ks)
        family_k[family_name] = (k_avg, k_min, k_max)
        print(f"  {family_name}: k_avg = {k_avg:.1f} N/m "
              f"(range {k_min:.1f}–{k_max:.1f})")

    print()

    # ── Generate all binary compounds and estimate frequencies ──
    all_results = []

    # Within each calibrated family: use that family's k
    group_pairs = {
        'III-V': ('III', 'V'),
        'II-VI': ('II', 'VI'),
        'I-VII': ('I', 'VII'),
        'IV-VI': ('IV', 'VI'),
    }

    for family_name, (g1, g2) in group_pairs.items():
        k_avg, k_min, k_max = family_k[family_name]
        for sym1, (m1, grp1) in ELEMENTS.items():
            if g1 not in grp1:
                continue
            for sym2, (m2, grp2) in ELEMENTS.items():
                if g2 not in grp2:
                    continue
                if sym1 == sym2:
                    continue
                f = estimate_freq(k_avg, sym1, sym2)
                f_lo = estimate_freq(k_max, sym1, sym2)
                f_hi = estimate_freq(k_min, sym1, sym2)
                mu = reduced_mass(sym1, sym2)
                name = f"{sym1}{sym2}"
                score = score_against_targets(f)
                all_results.append((score[1], name, sym1, sym2,
                                   mu, f, f_lo, f_hi, family_name,
                                   score))

    # Also try metal-deuterides using PdD as calibrator
    k_PdD = derive_k('Pd', 'D', 8.3)
    for sym, (m, grp) in ELEMENTS.items():
        if grp == 'TM' or sym in ('Pd', 'Ni', 'Pt', 'Cu', 'Ag',
                                    'Au', 'Fe', 'Ti', 'Zr', 'W',
                                    'La', 'Nb', 'Mo', 'Y', 'V',
                                    'Cr', 'Mn', 'Co'):
            for iso, iso_sym in [('H', 'H'), ('D', 'D')]:
                f = estimate_freq(k_PdD, sym, iso_sym)
                mu = reduced_mass(sym, iso_sym)
                name = f"{sym}{iso}"
                score = score_against_targets(f)
                all_results.append((score[1], name, sym, iso_sym,
                                   mu, f, f, f, 'M-H/D',
                                   score))

    # Sort by match quality
    all_results.sort()

    # ── Report: best matches per target ────────────────────────
    print("=" * 78)
    print("TOP MATCHES PER TARGET FREQUENCY")
    print("=" * 78)
    print()

    for target_f, fam, label in sorted(ALL_TARGETS):
        matches = []
        for pct, name, s1, s2, mu, f, f_lo, f_hi, bond, score in all_results:
            if score[3] == fam and score[4] == label:
                matches.append((abs(f - target_f) / target_f * 100,
                               name, f, mu, bond))
        matches.sort()

        print(f"  Family {fam} {label} = {target_f:.2f} THz:")
        print(f"  {'Material':>10s}  {'f_est':>7s}  {'Δ%':>6s}  "
              f"{'μ(amu)':>7s}  {'bond type':>10s}")
        print(f"  {'─'*10}  {'─'*7}  {'─'*6}  {'─'*7}  {'─'*10}")
        for pct, name, f, mu, bond in matches[:8]:
            marker = ' ◄' if pct < 3 else ''
            print(f"  {name:>10s}  {f:>7.2f}  {pct:>5.1f}%  "
                  f"{mu:>7.1f}  {bond:>10s}{marker}")
        print()

    # ── Report: overall top 30 across all targets ──────────────
    print("=" * 78)
    print("OVERALL TOP 30 MATCHES (all targets, all families)")
    print("=" * 78)
    print()
    print(f"  {'Material':>10s}  {'f_est':>7s}  {'target':>7s}  "
          f"{'Δ%':>6s}  {'family':>8s}  {'μ':>6s}  {'bond':>8s}")
    print(f"  {'─'*10}  {'─'*7}  {'─'*7}  {'─'*6}  "
          f"{'─'*8}  {'─'*6}  {'─'*8}")

    seen = set()
    count = 0
    for pct, name, s1, s2, mu, f, f_lo, f_hi, bond, score in all_results:
        key = (name, score[3], score[4])
        if key in seen:
            continue
        seen.add(key)
        print(f"  {name:>10s}  {f:>7.2f}  {score[2]:>7.2f}  "
              f"{pct:>5.1f}%  {score[3]+' '+score[4]:>8s}  "
              f"{mu:>6.1f}  {bond:>8s}")
        count += 1
        if count >= 30:
            break

    print()

    # ── Materials matching MULTIPLE targets ─────────────────────
    print("=" * 78)
    print("MATERIALS MATCHING MULTIPLE TARGETS (within 10%)")
    print("=" * 78)
    print()

    mat_targets = defaultdict(list)
    for pct, name, s1, s2, mu, f, f_lo, f_hi, bond, score in all_results:
        if pct < 10:
            mat_targets[name].append((f, score[2], score[3], score[4], pct))

    multi = {k: v for k, v in mat_targets.items() if len(v) >= 2}
    for name, targets in sorted(multi.items(), key=lambda x: -len(x[1])):
        print(f"  {name}: matches {len(targets)} targets")
        for f, tf, fam, label, pct in targets:
            print(f"    f={f:.2f} → {fam} {label}={tf:.2f} THz ({pct:.1f}%)")
    if not multi:
        print("  (none found — each material matches at most one target)")

    print()
    print("Track 1 complete.")


if __name__ == '__main__':
    main()
