#!/usr/bin/env python3
"""
R42 — Dark matter from ghost modes

Tracks 1–5 in one script:
  1. Mode census + charge symmetry proof
  2. Mass ratio under equal occupation
  3. Mass ratio under thermal distributions
  4. Dark spectrum characterization
  5. Window Q factor sensitivity

Usage:
    cd studies && python3 R42-dark-matter/scripts/dark_matter_census.py
"""

import sys, os, time, math
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../..')
from lib.ma_model import Ma, _mode_charge, _mode_spin

REF = dict(r_e=6.6, r_nu=5.0, r_p=8.906, sigma_ep=-0.0906)
E_MAX = 2000.0   # MeV
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


def logspace(start, stop, n):
    """Simple logspace without numpy."""
    log_start = math.log10(start)
    log_stop = math.log10(stop)
    step = (log_stop - log_start) / (n - 1)
    return [10 ** (log_start + i * step) for i in range(n)]


def main():
    model = Ma(**REF, dynamic=False)

    # ══════════════════════════════════════════════════════════════
    #  TRACK 1: Mode census + charge symmetry
    # ══════════════════════════════════════════════════════════════
    section("TRACK 1: MODE CENSUS AND CHARGE SYMMETRY")

    t0 = time.perf_counter()
    modes = model.scan_modes(n_max=N_MAX, E_max_MeV=E_MAX)
    t_scan = time.perf_counter() - t0
    print(f"Total modes scanned: {len(modes):,d}  ({t_scan:.1f}s)")

    families = defaultdict(list)
    for m in modes:
        families[essential_key(m.n)].append(m)
    print(f"Families (n₄ collapsed): {len(families):,d}")

    visible_modes = []
    dark_modes = []
    for m in modes:
        name, _ = match_particle(m.E_MeV, m.charge, m.spin_halves)
        if name:
            visible_modes.append(m)
        else:
            dark_modes.append(m)

    print(f"\nVisible modes (match known particle): {len(visible_modes):,d}")
    print(f"Dark modes (no match):                {len(dark_modes):,d}")

    # --- Charge symmetry ---
    print(f"\n--- Charge symmetry of dark modes ---")
    charge_counts = defaultdict(int)
    charge_mass = defaultdict(float)
    for m in dark_modes:
        charge_counts[m.charge] += 1
        charge_mass[m.charge] += m.E_MeV

    charges = sorted(charge_counts.keys())
    print(f"{'Charge':>8}  {'Count':>10}  {'Total mass (MeV)':>18}")
    print(f"{'─'*8}  {'─'*10}  {'─'*18}")
    for q in charges:
        print(f"{q:8d}  {charge_counts[q]:10,d}  {charge_mass[q]:18,.1f}")

    net_charge = sum(q * charge_counts[q] for q in charges)
    print(f"\nNet charge (Σ Q×count): {net_charge}")

    for q in charges:
        if q > 0 and -q in charge_counts:
            sym = '✓ SYMMETRIC' if charge_counts[q] == charge_counts[-q] else '✗ ASYMMETRIC'
            print(f"  Q={q:+d}: {charge_counts[q]:,d} modes, "
                  f"Q={-q:+d}: {charge_counts[-q]:,d} modes  {sym}")

    # Check mass symmetry for charge partners
    print(f"\n--- Mass symmetry for charge-conjugate pairs ---")
    mode_dict = {}
    for m in dark_modes:
        mode_dict[m.n] = m

    n_checked = 0
    n_partner_found = 0
    n_mass_match = 0
    for m in dark_modes:
        if m.charge <= 0:
            continue
        n = m.n
        conjugate = (-n[0], n[1], n[2], n[3], -n[4], n[5])
        n_checked += 1
        if conjugate in mode_dict:
            n_partner_found += 1
            partner = mode_dict[conjugate]
            if abs(m.E_MeV - partner.E_MeV) / max(m.E_MeV, 1e-30) < 1e-10:
                n_mass_match += 1

    print(f"Positive-charge dark modes checked: {n_checked:,d}")
    print(f"  Partner (−Q, same mass) found:    {n_partner_found:,d}")
    print(f"  Mass matches to <10⁻¹⁰:          {n_mass_match:,d}")
    if n_checked > 0:
        print(f"  Partner rate: {n_partner_found/n_checked*100:.1f}%")
        print(f"  Mass match rate: {n_mass_match/n_checked*100:.1f}%")

    # ══════════════════════════════════════════════════════════════
    #  TRACK 2: Mass ratio under equal occupation
    # ══════════════════════════════════════════════════════════════
    section("TRACK 2: MASS RATIO — EQUAL OCCUPATION")

    sum_m_vis = sum(m.E_MeV for m in visible_modes)
    sum_m_dark = sum(m.E_MeV for m in dark_modes)

    print(f"Total visible mass (1 per mode):  {sum_m_vis:,.1f} MeV  ({len(visible_modes):,d} modes)")
    print(f"Total dark mass (1 per mode):     {sum_m_dark:,.1f} MeV  ({len(dark_modes):,d} modes)")
    print(f"Dark / Visible ratio:             {sum_m_dark/sum_m_vis:.2f}")
    print(f"Observed DM/visible:              5.4")

    avg_vis = sum_m_vis / max(len(visible_modes), 1)
    avg_dark = sum_m_dark / max(len(dark_modes), 1)
    print(f"\nAverage visible mode mass:  {avg_vis:.1f} MeV")
    print(f"Average dark mode mass:    {avg_dark:.1f} MeV")
    print(f"Ratio (avg_dark/avg_vis):  {avg_dark/avg_vis:.3f}")

    # By family (collapse n₄ degeneracy)
    vis_families = defaultdict(list)
    dark_families = defaultdict(list)
    for m in visible_modes:
        vis_families[essential_key(m.n)].append(m)
    for m in dark_modes:
        dark_families[essential_key(m.n)].append(m)

    sum_mf_vis = sum(members[0].E_MeV for members in vis_families.values())
    sum_mf_dark = sum(members[0].E_MeV for members in dark_families.values())

    print(f"\n--- By family (n₄ collapsed) ---")
    print(f"Visible families: {len(vis_families):,d}  total mass: {sum_mf_vis:,.1f} MeV")
    print(f"Dark families:    {len(dark_families):,d}  total mass: {sum_mf_dark:,.1f} MeV")
    print(f"Dark / Visible (families): {sum_mf_dark/sum_mf_vis:.2f}")

    # ══════════════════════════════════════════════════════════════
    #  TRACK 3: Mass ratio under thermal distributions
    # ══════════════════════════════════════════════════════════════
    section("TRACK 3: MASS RATIO — THERMAL DISTRIBUTIONS")

    vis_masses = [members[0].E_MeV for members in vis_families.values()]
    dark_masses = [members[0].E_MeV for members in dark_families.values()]

    temperatures_MeV = logspace(0.1, 10000, 200)

    print(f"{'T (MeV)':>10}  {'Boltzmann DM/vis':>16}")
    print(f"{'─'*10}  {'─'*16}")

    ratios_boltz = []
    best_boltz_T = None
    best_boltz_diff = 1e10
    best_boltz_r = 0

    show_temps = {0.1, 0.5, 1.0, 5.0, 10, 50, 100, 200, 500, 1000, 2000, 5000, 10000}

    for T in temperatures_MeV:
        w_vis = sum(m * math.exp(-m / T) for m in vis_masses)
        w_dark = sum(m * math.exp(-m / T) for m in dark_masses)

        r_boltz = w_dark / max(w_vis, 1e-300)
        ratios_boltz.append((T, r_boltz))

        if abs(r_boltz - 5.4) < best_boltz_diff:
            best_boltz_diff = abs(r_boltz - 5.4)
            best_boltz_T = T
            best_boltz_r = r_boltz

        for st in list(show_temps):
            if abs(T - st) / st < 0.05:
                print(f"{T:10.1f}  {r_boltz:16.4f}")
                show_temps.discard(st)

    print(f"\nBest Boltzmann match to 5.4: T = {best_boltz_T:.1f} MeV  "
          f"(ratio = {best_boltz_r:.4f})")

    # Find crossings
    crossings = []
    for i in range(len(ratios_boltz) - 1):
        T1, r1 = ratios_boltz[i]
        T2, r2 = ratios_boltz[i + 1]
        if (r1 - 5.4) * (r2 - 5.4) < 0:
            T_cross = T1 + (5.4 - r1) / (r2 - r1) * (T2 - T1)
            crossings.append(T_cross)

    if crossings:
        print(f"Boltzmann ratio crosses 5.4 at T = {', '.join(f'{T:.1f}' for T in crossings)} MeV")
    else:
        all_r = [r for _, r in ratios_boltz]
        print(f"Boltzmann ratio never crosses 5.4")
        print(f"  Range: {min(all_r):.4f} (T→0) to {max(all_r):.4f} (T→∞)")

    # ══════════════════════════════════════════════════════════════
    #  TRACK 4: Dark spectrum characterization
    # ══════════════════════════════════════════════════════════════
    section("TRACK 4: DARK SPECTRUM CHARACTERIZATION")

    dark_list = sorted(dark_families.items(), key=lambda x: x[1][0].E_MeV)

    if dark_list:
        lightest = dark_list[0]
        heaviest = dark_list[-1]
        print(f"Lightest dark family: E = {lightest[1][0].E_MeV:.4f} MeV  "
              f"Q = {lightest[1][0].charge}  spin = {lightest[1][0].spin_halves}  "
              f"key = {lightest[0]}")
        print(f"Heaviest dark family: E = {heaviest[1][0].E_MeV:.3f} MeV  "
              f"Q = {heaviest[1][0].charge}  spin = {heaviest[1][0].spin_halves}  "
              f"key = {heaviest[0]}")

    # Mass histogram (100 MeV bins)
    bins = list(range(0, int(E_MAX) + 100, 100))
    dark_E = [members[0].E_MeV for members in dark_families.values()]
    vis_E = [members[0].E_MeV for members in vis_families.values()]

    def histogram(values, bins):
        counts = [0] * (len(bins) - 1)
        for v in values:
            for i in range(len(bins) - 1):
                if bins[i] <= v < bins[i + 1]:
                    counts[i] += 1
                    break
        return counts

    dark_hist = histogram(dark_E, bins)
    vis_hist = histogram(vis_E, bins)

    print(f"\n--- Mass spectrum (families per 100 MeV bin) ---")
    print(f"{'Bin (MeV)':>15}  {'Dark':>8}  {'Visible':>8}  {'D/V':>8}")
    print(f"{'─'*15}  {'─'*8}  {'─'*8}  {'─'*8}")
    for i in range(len(dark_hist)):
        if dark_hist[i] + vis_hist[i] > 0:
            ratio_str = f"{dark_hist[i]/max(vis_hist[i],1):.1f}" if vis_hist[i] > 0 else "∞"
            print(f"{bins[i]:6d}–{bins[i+1]:6d}  {dark_hist[i]:8d}  "
                  f"{vis_hist[i]:8d}  {ratio_str:>8}")

    # Fermion/boson split
    dark_fermions = sum(1 for k, ms in dark_families.items() if ms[0].spin_halves % 2 == 1)
    dark_bosons = sum(1 for k, ms in dark_families.items() if ms[0].spin_halves % 2 == 0)
    print(f"\nDark mode statistics:")
    print(f"  Fermions (odd spin-½ count): {dark_fermions:,d} families")
    print(f"  Bosons (even spin-½ count):  {dark_bosons:,d} families")

    # Charge distribution
    dark_q_dist = defaultdict(int)
    for k, ms in dark_families.items():
        dark_q_dist[ms[0].charge] += 1
    print(f"\nDark mode charge distribution (by family):")
    for q in sorted(dark_q_dist.keys()):
        print(f"  Q = {q:+d}: {dark_q_dist[q]:,d} families")

    # Max tube winding distribution
    dark_mt_dist = defaultdict(int)
    for k, ms in dark_families.items():
        mt = max_tube(ms[0].n)
        dark_mt_dist[mt] += 1
    print(f"\nDark mode max-tube-winding distribution:")
    for mt in sorted(dark_mt_dist.keys()):
        print(f"  max|n_tube| = {mt}: {dark_mt_dist[mt]:,d} families")

    # Lowest 20 dark modes
    print(f"\n--- 20 lightest dark families ---")
    print(f"{'(n₁,n₂,n₃,n₅,n₆)':>22}  {'E (MeV)':>10}  {'Q':>4}  {'Sp':>3}  {'mt':>3}")
    print(f"{'─'*22}  {'─'*10}  {'─'*4}  {'─'*3}  {'─'*3}")
    for key, members in dark_list[:20]:
        rep = members[0]
        print(f"{str(key):>22}  {rep.E_MeV:10.4f}  {rep.charge:4d}  "
              f"{rep.spin_halves:3d}  {max_tube(rep.n):3d}")

    # ══════════════════════════════════════════════════════════════
    #  TRACK 5: Window Q factor sensitivity
    # ══════════════════════════════════════════════════════════════
    section("TRACK 5: WINDOW Q FACTOR SENSITIVITY")

    fund_e = model.energy((1, 2, 0, 0, 0, 0))
    fund_p = model.energy((0, 0, 0, 0, 1, 2))
    fund_nu = model.energy((0, 0, 1, 2, 0, 0))

    print(f"Fundamental frequencies (MeV):")
    print(f"  Ma_e (1,2): {fund_e:.4f}")
    print(f"  Ma_p (1,2): {fund_p:.3f}")
    print(f"  Ma_ν (1,2): {fund_nu:.6f}")

    def window_factor(mode_E, fund_E, Q):
        if fund_E < 1e-10 or mode_E < 1e-10:
            return 0.0
        x = mode_E / fund_E
        return 1.0 / (1.0 + Q**2 * (x - 1.0/x)**2)

    def best_harmonic_W(mode_E, fund_E, Q):
        if fund_E < 1e-10:
            return 0.0
        k_est = max(1, round(mode_E / fund_E))
        best = 0.0
        for k in range(max(1, k_est - 2), k_est + 3):
            W = window_factor(mode_E, k * fund_E, Q)
            if W > best:
                best = W
        return best

    def multi_window_factor(n, mode_E, Q, model):
        decomp = model.energy_decomp(n)
        fracs = decomp.fractions

        W_e = best_harmonic_W(mode_E, fund_e, Q) if fracs.get('e', 0) > 0.01 else 0
        W_p = best_harmonic_W(mode_E, fund_p, Q) if fracs.get('p', 0) > 0.01 else 0
        W_nu = best_harmonic_W(mode_E, fund_nu, Q) if fracs.get('nu', 0) > 0.01 else 0

        return max(W_e, W_p, W_nu)

    Q_values = (list(range(1, 20)) +
                list(range(20, 50, 2)) +
                list(range(50, 200, 5)) +
                list(range(200, 1001, 50)))

    print(f"\n--- Q sweep (multi-sheet harmonic windows, W_thresh=0.5) ---")
    print(f"{'Q':>6}  {'N_vis_fam':>9}  {'N_dark_fam':>10}  {'Σm_vis':>12}  "
          f"{'Σm_dark':>12}  {'DM/vis':>8}")
    print(f"{'─'*6}  {'─'*9}  {'─'*10}  {'─'*12}  {'─'*12}  {'─'*8}")

    show_Q = {1, 2, 3, 5, 10, 15, 20, 30, 50, 75, 100, 130, 137, 140, 150, 200, 300, 500, 1000}

    results = []
    for Q in Q_values:
        n_vis = 0
        n_dark = 0
        sm_vis = 0.0
        sm_dark = 0.0

        for key, members in families.items():
            rep = members[0]
            W = multi_window_factor(rep.n, rep.E_MeV, Q, model)

            if W >= 0.5:
                n_vis += 1
                sm_vis += rep.E_MeV
            else:
                n_dark += 1
                sm_dark += rep.E_MeV

        ratio = sm_dark / max(sm_vis, 1e-300)
        results.append((Q, n_vis, n_dark, sm_vis, sm_dark, ratio))

        if Q in show_Q:
            print(f"{Q:6d}  {n_vis:9d}  {n_dark:10d}  {sm_vis:12,.1f}  "
                  f"{sm_dark:12,.1f}  {ratio:8.2f}")

    # Key Q values
    n_known_families = len(vis_families)
    print(f"\n--- Key Q values ---")
    print(f"Known visible families (particle matching): {n_known_families:,d}")

    best_Q_count = None
    best_diff_count = 1e10
    best_Q_ratio = None
    best_diff_ratio = 1e10

    for Q, nv, nd, sv, sd, r in results:
        if abs(nv - n_known_families) < best_diff_count:
            best_diff_count = abs(nv - n_known_families)
            best_Q_count = (Q, nv, r)
        if abs(r - 5.4) < best_diff_ratio:
            best_diff_ratio = abs(r - 5.4)
            best_Q_ratio = (Q, nv, r)

    Q137 = [(Q, nv, nd, sv, sd, r) for Q, nv, nd, sv, sd, r in results if Q == 137]

    if best_Q_count:
        print(f"Q for N_vis ≈ {n_known_families}: Q = {best_Q_count[0]}  "
              f"(N_vis = {best_Q_count[1]}, DM/vis = {best_Q_count[2]:.2f})")
    if best_Q_ratio:
        print(f"Q for DM/vis ≈ 5.4:  Q = {best_Q_ratio[0]}  "
              f"(N_vis = {best_Q_ratio[1]}, DM/vis = {best_Q_ratio[2]:.2f})")
    if Q137:
        _, nv, nd, sv, sd, r = Q137[0]
        print(f"Q = 137:             N_vis = {nv}, DM/vis = {r:.2f}")

    # ══════════════════════════════════════════════════════════════
    #  SUMMARY
    # ══════════════════════════════════════════════════════════════
    section("SUMMARY")

    print("Track 1 — Charge symmetry:")
    print(f"  Net charge of dark modes: {net_charge}")
    if n_checked > 0:
        print(f"  Charge-conjugate partners: "
              f"{n_partner_found}/{n_checked} ({n_partner_found/n_checked*100:.0f}%)")
        print(f"  Mass-matched to <10⁻¹⁰:   "
              f"{n_mass_match}/{n_checked} ({n_mass_match/n_checked*100:.0f}%)")

    print(f"\nTrack 2 — Equal occupation:")
    print(f"  Dark/visible by mode:   {sum_m_dark/sum_m_vis:.2f}")
    print(f"  Dark/visible by family: {sum_mf_dark/sum_mf_vis:.2f}")

    if crossings:
        print(f"\nTrack 3 — Boltzmann:")
        for T in crossings:
            print(f"  Crosses 5.4 at T = {T:.1f} MeV")
    else:
        all_r = [r for _, r in ratios_boltz]
        print(f"\nTrack 3 — Boltzmann:")
        print(f"  Never crosses 5.4.  Range: {min(all_r):.4f} – {max(all_r):.4f}")

    print(f"\nTrack 4 — Dark spectrum:")
    print(f"  {len(dark_families):,d} dark families, "
          f"{dark_fermions:,d} fermion / {dark_bosons:,d} boson")
    if dark_list:
        print(f"  Lightest: {dark_list[0][1][0].E_MeV:.4f} MeV  "
              f"Heaviest: {dark_list[-1][1][0].E_MeV:.1f} MeV")

    print(f"\nTrack 5 — Q factor:")
    if best_Q_count:
        print(f"  Q for correct particle count: {best_Q_count[0]}  "
              f"(N_vis={best_Q_count[1]}, DM/vis={best_Q_count[2]:.2f})")
    if best_Q_ratio:
        print(f"  Q for correct DM ratio:       {best_Q_ratio[0]}  "
              f"(N_vis={best_Q_ratio[1]}, DM/vis={best_Q_ratio[2]:.2f})")
    if Q137:
        print(f"  Q = 1/α = 137:                "
              f"N_vis={Q137[0][1]}, DM/vis={Q137[0][5]:.2f}")


if __name__ == '__main__':
    main()
