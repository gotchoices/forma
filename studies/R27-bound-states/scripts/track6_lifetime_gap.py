#!/usr/bin/env python3
"""
R27 Track 6: Lifetime-gap correlation — the central test of the
off-resonance hypothesis.

Uses the Track 5 catalog and performs:
  1. Full-sample correlation (all 15 unstable particles)
  2. Robustness: exclude reference particles (n, μ) to check if
     the trend survives without pinning anchors
  3. Subgroup analysis: mesons vs baryons vs leptons
  4. Rank-order (Spearman) correlation for non-parametric test
  5. Bootstrap confidence interval on correlation
  6. Outlier identification
  7. Physical interpretation
"""

import sys
import os
import math
import numpy as np
from scipy import stats

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.t6_solver import self_consistent_metric
from lib.t6 import mode_energy, mode_charge, mode_spin, M_P_MEV, M_E_MEV

R_E, R_NU, R_P = 6.6, 5.0, 8.906
SIGMA_EP = -0.09064


# ── Catalog from Track 5 (hardcoded to avoid recomputation) ───────
# (sym, name, mass_MeV, charge, spin_halves, lifetime_s,
#  mode_n, mode_E_MeV)
# Entries with mode_n = None had no match.

CATALOG = [
    ("e⁻",  "electron",        0.511,  -1, 1, float('inf'),
     (1,2,0,0,0,0),           0.511),
    ("p",   "proton",        938.272,  +1, 1, float('inf'),
     (0,0,0,0,1,2),         938.272),
    ("n",   "neutron",       939.565,   0, 1, 878.4,
     (0,-2,1,0,0,2),        939.565),
    ("μ⁻",  "muon",          105.658,  -1, 1, 2.197e-6,
     (-1,5,0,0,-2,0),       105.658),
    ("τ⁻",  "tau",          1776.86,   -1, 1, 2.903e-13,
     (-1,8,0,0,-2,-4),     1876.375),
    ("π⁺",  "pion+",         139.570,  +1, 0, 2.603e-8,
     (2,-8,1,0,3,0),        158.480),
    ("π⁰",  "pion0",         134.977,   0, 0, 8.52e-17,
     (-3,8,0,0,-3,0),       158.484),
    ("K⁺",  "kaon+",         493.677,  +1, 0, 1.238e-8,
     (-4,-8,1,0,-3,-1),     488.008),
    ("K⁰",  "kaon0",         497.611,   0, 0, None,
     (-3,-8,0,0,-3,1),      503.710),
    ("η",   "eta",           547.862,   0, 0, 5.02e-19,
     (-5,-8,0,0,-5,1),      551.172),
    ("η′",  "eta prime",     957.78,    0, 0, 3.32e-21,
     (-3,-8,0,0,-3,2),      961.070),
    ("ρ⁰",  "rho",           775.26,    0, 2, 4.5e-24,
     (-7,8,0,0,-7,1),       613.426),
    ("ω",   "omega meson",   782.66,    0, 2, 7.75e-23,
     (-1,8,0,0,-1,-2),      938.104),
    ("φ",   "phi",          1019.461,   0, 2, 1.55e-22,
     (-7,-8,0,0,-7,2),     1027.982),
    ("Λ",   "lambda",       1115.683,   0, 1, 2.632e-10,
     (-8,8,1,0,-8,2),      1050.875),
    ("Σ⁺",  "sigma+",       1189.37,   +1, 1, 8.018e-11,
     (7,-8,0,0,8,-2),      1050.877),
    ("Ξ⁰",  "xi zero",      1314.86,    0, 1, 2.90e-10,
     (-2,8,1,0,-2,-3),     1407.566),
    ("Δ⁺⁺", "delta",        1232.0,    +2, 3, 5.63e-24,
     (-1,-8,1,0,1,3),      1407.407),
    ("Ω⁻",  "omega baryon", 1672.45,   -1, 3, 8.21e-11,
     None,                   None),
]


def get_unstable_pairs(exclude_syms=None):
    """Extract (sym, name, mass, |gap|, frac_gap, lifetime) for unstable particles."""
    if exclude_syms is None:
        exclude_syms = set()
    pairs = []
    for entry in CATALOG:
        sym, name, mass, charge, spin, lt, mode_n, mode_E = entry
        if lt is None or lt == float('inf'):
            continue
        if mode_n is None or mode_E is None:
            continue
        if sym in exclude_syms:
            continue
        gap = abs(mass - mode_E)
        fgap = gap / mass
        pairs.append((sym, name, mass, gap, fgap, lt))
    return pairs


def correlation_analysis(pairs, label=""):
    """Compute Pearson and Spearman correlations for (log|gap|, log τ)."""
    if len(pairs) < 3:
        print(f"  Too few data points ({len(pairs)}) for {label}")
        return None, None

    log_gaps = np.array([math.log10(max(p[3], 1e-4)) for p in pairs])
    log_lts = np.array([math.log10(p[5]) for p in pairs])

    r_pearson, p_pearson = stats.pearsonr(log_gaps, log_lts)
    r_spearman, p_spearman = stats.spearmanr(log_gaps, log_lts)

    slope, intercept = np.polyfit(log_gaps, log_lts, 1)

    print(f"  {label}")
    print(f"  N = {len(pairs)}")
    print(f"  Pearson  r = {r_pearson:+.4f},  p = {p_pearson:.4f}")
    print(f"  Spearman ρ = {r_spearman:+.4f},  p = {p_spearman:.4f}")
    print(f"  Best-fit: log(τ) = {slope:+.3f} × log|gap| + ({intercept:+.3f})")
    print(f"  → τ ∝ |gap|^({slope:+.2f})")
    print()

    return r_pearson, r_spearman


def bootstrap_ci(pairs, n_boot=10000, ci=0.95):
    """Bootstrap confidence interval on Pearson r."""
    log_gaps = np.array([math.log10(max(p[3], 1e-4)) for p in pairs])
    log_lts = np.array([math.log10(p[5]) for p in pairs])
    n = len(log_gaps)

    rng = np.random.default_rng(42)
    rs = []
    for _ in range(n_boot):
        idx = rng.integers(0, n, size=n)
        g = log_gaps[idx]
        l = log_lts[idx]
        if np.std(g) > 0 and np.std(l) > 0:
            rs.append(np.corrcoef(g, l)[0, 1])

    rs = np.array(rs)
    lo = np.percentile(rs, (1 - ci) / 2 * 100)
    hi = np.percentile(rs, (1 + ci) / 2 * 100)
    return lo, hi, np.median(rs)


def section(n, title):
    print(f"\n{'='*70}")
    print(f"  SECTION {n}: {title}")
    print(f"{'='*70}\n")


def main():
    # ── Section 1: Full sample ────────────────────────────────────────
    section(1, "Full-sample correlation (all unstable)")

    all_pairs = get_unstable_pairs()
    r_all, rho_all = correlation_analysis(all_pairs, "All 15 unstable particles")

    # ── Section 2: Exclude reference particles ────────────────────────
    section(2, "Robustness — exclude pinning particles (n, μ)")

    no_ref = get_unstable_pairs(exclude_syms={"n", "μ⁻"})
    r_noref, rho_noref = correlation_analysis(no_ref, "13 particles (no n, μ)")

    # ── Section 3: Exclude reference + stable-ish ─────────────────────
    section(3, "Robustness — exclude all near-exact matches")

    no_exact = get_unstable_pairs(exclude_syms={"n", "μ⁻", "e⁻", "p"})
    # Also filter out particles with |gap| < 0.1 MeV
    no_exact = [p for p in no_exact if p[3] > 0.1]
    r_noexact, rho_noexact = correlation_analysis(
        no_exact, "Genuinely off-resonance particles only")

    # ── Section 4: Subgroup analysis ──────────────────────────────────
    section(4, "Subgroup analysis")

    leptons = get_unstable_pairs()
    leptons = [p for p in leptons if p[0] in {"μ⁻", "τ⁻"}]
    print(f"  Leptons (N={len(leptons)}): too few for correlation\n")
    for p in leptons:
        print(f"    {p[0]:>4s}  |gap| = {p[3]:8.3f} MeV  τ = {p[5]:.2e} s")
    print()

    mesons_ps = [p for p in get_unstable_pairs()
                 if p[0] in {"π⁺", "π⁰", "K⁺", "η", "η′"}]
    correlation_analysis(mesons_ps, "Pseudoscalar mesons")

    mesons_v = [p for p in get_unstable_pairs()
                if p[0] in {"ρ⁰", "ω", "φ"}]
    correlation_analysis(mesons_v, "Vector mesons")

    baryons = [p for p in get_unstable_pairs()
               if p[0] in {"n", "Λ", "Σ⁺", "Ξ⁰", "Δ⁺⁺"}]
    correlation_analysis(baryons, "Baryons")

    # ── Section 5: Bootstrap CI ───────────────────────────────────────
    section(5, "Bootstrap 95% CI on Pearson r")

    lo_all, hi_all, med_all = bootstrap_ci(all_pairs)
    print(f"  Full sample:      r = {med_all:+.3f}  [{lo_all:+.3f}, {hi_all:+.3f}]")

    lo_nr, hi_nr, med_nr = bootstrap_ci(no_ref)
    print(f"  Excl. n, μ:       r = {med_nr:+.3f}  [{lo_nr:+.3f}, {hi_nr:+.3f}]")

    if len(no_exact) >= 3:
        lo_ne, hi_ne, med_ne = bootstrap_ci(no_exact)
        print(f"  Off-resonance only: r = {med_ne:+.3f}  [{lo_ne:+.3f}, {hi_ne:+.3f}]")

    # ── Section 6: Outlier identification ─────────────────────────────
    section(6, "Outlier identification")

    all_pairs_sorted = sorted(all_pairs, key=lambda p: p[3])
    log_gaps = np.array([math.log10(max(p[3], 1e-4)) for p in all_pairs_sorted])
    log_lts = np.array([math.log10(p[5]) for p in all_pairs_sorted])

    slope, intercept = np.polyfit(log_gaps, log_lts, 1)
    predicted = slope * log_gaps + intercept
    residuals = log_lts - predicted

    print(f"  Best-fit: log(τ) = {slope:+.3f} × log|gap| + ({intercept:+.3f})")
    print(f"  Residual σ = {np.std(residuals):.2f} decades\n")

    print(f"  {'Sym':>6s}  {'|Gap|':>10s}  {'log(τ)':>8s}  {'Predicted':>10s}  "
          f"{'Residual':>10s}  {'σ':>5s}")
    print(f"  {'-'*60}")

    sigma = np.std(residuals)
    for i, p in enumerate(all_pairs_sorted):
        n_sigma = residuals[i] / sigma if sigma > 0 else 0
        flag = " ← OUTLIER" if abs(n_sigma) > 1.5 else ""
        print(f"  {p[0]:>6s}  {p[3]:10.3f}  {log_lts[i]:+8.1f}  "
              f"{predicted[i]:+10.1f}  {residuals[i]:+10.2f}  "
              f"{n_sigma:+5.1f}{flag}")

    # ── Section 7: Decay-class analysis ───────────────────────────────
    section(7, "Decay mechanism classes")

    print("  Grouping particles by dominant decay mechanism:\n")

    classes = {
        'Weak (charged current)': [
            ("n",  878.4,     0.000),
            ("μ⁻", 2.197e-6,  0.000),
            ("π⁺", 2.603e-8, 18.910),
            ("K⁺", 1.238e-8,  5.669),
            ("τ⁻", 2.903e-13, 99.515),
            ("Λ",  2.632e-10, 64.808),
            ("Σ⁺", 8.018e-11, 138.493),
            ("Ξ⁰", 2.90e-10, 92.706),
        ],
        'Electromagnetic': [
            ("π⁰", 8.52e-17, 23.507),
            ("η",  5.02e-19,  3.310),
            ("η′", 3.32e-21,  3.290),
        ],
        'Strong': [
            ("ρ⁰", 4.5e-24,  161.834),
            ("ω",  7.75e-23, 155.444),
            ("φ",  1.55e-22,   8.521),
            ("Δ⁺⁺", 5.63e-24, 175.407),
        ],
    }

    for cls_name, particles in classes.items():
        print(f"  {cls_name}:")
        log_g = []
        log_t = []
        for sym, lt, gap in particles:
            lg = math.log10(max(gap, 1e-4))
            ll = math.log10(lt)
            log_g.append(lg)
            log_t.append(ll)
            print(f"    {sym:>4s}  |gap| = {gap:8.3f} MeV  τ = {lt:.2e} s  "
                  f"log₁₀τ = {ll:+6.1f}")
        if len(log_g) >= 3:
            r, p = stats.pearsonr(log_g, log_t)
            print(f"    → Within-class Pearson r = {r:+.3f} (p = {p:.3f})")
        print()

    # ── Section 8: Summary ────────────────────────────────────────────
    section(8, "Summary")

    print(f"  Full-sample Pearson r  = {r_all:+.4f}")
    print(f"  Full-sample Spearman ρ = {rho_all:+.4f}")
    print(f"  Excl. n,μ   Pearson r  = {r_noref:+.4f}" if r_noref else "")
    print(f"  Excl. n,μ   Spearman ρ = {rho_noref:+.4f}" if rho_noref else "")
    print()
    print(f"  Bootstrap 95% CI (full): [{lo_all:+.3f}, {hi_all:+.3f}]")
    print()

    if r_all < -0.3 and r_noref is not None and r_noref < -0.3:
        print("  CONCLUSION: The negative correlation is ROBUST.")
        print("  It survives exclusion of reference particles.")
        print("  The off-resonance hypothesis passes this test.")
    elif r_all < -0.3:
        print("  CONCLUSION: Negative correlation present but may be")
        print("  driven partly by the reference particles.")
    else:
        print("  CONCLUSION: Correlation is weak or absent.")


if __name__ == '__main__':
    main()
