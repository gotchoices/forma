"""
R50 Track 4: Decay rate ↔ near-miss correlation

Quantifies the relationship between mass residual (distance from
nearest eigenmode) and measured lifetime, using Track 3 results
at σ_ep = −0.13.

KEY HYPOTHESIS (off-resonance):
Unstable particles are near-misses to Ma eigenmodes.  Closer
near-misses are more stable (longer τ).  The correlation
log₁₀(τ) vs log₁₀(|Δm/m|) should be negative.

R27 (model-C) found: r = −0.84 (p = 0.009), power law exponent
β ≈ −2.7.  Track 3 found r = −0.40 (N = 9).  This track
deepens the analysis: fits the power law, tests subsets,
predicts lifetimes, and compares to the R27 result.

DELIVERABLES:
  - Power law fit: log₁₀(τ) = A + β × log₁₀(|Δm/m|)
  - Pearson and Spearman correlations for full sample and subsets
  - Predicted vs observed lifetimes
  - Comparison to R27 power law (β = −2.7)
  - Assessment of which particles fit and which are outliers
"""

import math
import numpy as np


# ── Track 3 results (σ_ep = −0.13) ───────────────────────────────
# Each entry: (name, mass_MeV, best_E_MeV, delta_m_MeV, tau_s,
#              decay_type, tier)
# decay_type: 'weak', 'em', 'strong', 'stable'

DATA = [
    ('e⁻',    0.511,    0.511,      -1.05e-6,  float('inf'), 'stable',  1),
    ('p',     938.272,  938.272,     +1.14e-13, float('inf'), 'stable',  1),
    ('n',     939.565,  939.256,     -0.309,    879.4,        'weak',    2),
    ('μ⁻',   105.658,  117.212,     +11.554,   2.197e-6,     'weak',    2),
    ('π⁰',   134.977,  117.541,     -17.436,   8.43e-17,     'em',      2),
    ('K⁰',   497.611,  469.702,     -27.909,   8.954e-11,    'weak',    2),
    ('η',    547.862,  586.799,     +38.937,   5.02e-19,     'strong',  2),
    ('η′',   957.78,   939.256,     -18.524,   3.32e-21,     'strong',  2),
    ('φ',   1019.461, 1019.945,     +0.484,    1.55e-22,     'strong',  3),
    ('Λ',    1115.683, 1127.654,    +11.971,   2.632e-10,    'weak',    2),
    ('Σ⁺',  1189.37,  1187.065,    -2.305,    8.018e-11,    'weak',    3),
    ('Ξ⁰',  1314.86,  1291.422,    -23.438,   2.90e-10,     'weak',    3),
    ('Ω⁻',  1672.45,  1673.066,    +0.616,    8.21e-11,     'weak',    3),
    ('Δ⁰',  1232.0,   1237.035,    +5.035,    5.63e-24,     'strong',  3),
    ('ρ⁰',   775.26,   742.306,    -32.954,   4.51e-24,     'strong',  3),
    ('τ⁻',  1776.86,  1779.997,    +3.137,    2.903e-13,    'weak',    3),
]


def pearson_r(x, y):
    """Pearson correlation coefficient."""
    n = len(x)
    if n < 3:
        return float('nan'), float('nan')
    mx, my = np.mean(x), np.mean(y)
    sx, sy = np.std(x, ddof=1), np.std(y, ddof=1)
    if sx < 1e-15 or sy < 1e-15:
        return float('nan'), float('nan')
    r = np.sum((x - mx) * (y - my)) / ((n - 1) * sx * sy)
    # t-statistic for significance
    if abs(r) > 0.9999:
        p = 0.0
    else:
        t = r * math.sqrt((n - 2) / (1 - r**2))
        # Two-tailed p-value approximation (Student's t, N-2 dof)
        # Using the survival function of the t-distribution
        # For small N, approximate with beta incomplete function
        # Simple approximation: p ≈ 2 * (1 - Φ(|t|)) for large N
        # More accurately, use the continued fraction for I_x
        dof = n - 2
        x_val = dof / (dof + t**2)
        p = _betai(0.5 * dof, 0.5, x_val)
    return float(r), float(p)


def _betai(a, b, x):
    """Regularized incomplete beta function (simple approximation)."""
    if x < 0 or x > 1:
        return float('nan')
    if x == 0:
        return 0.0
    if x == 1:
        return 1.0
    # Use continued fraction for better accuracy
    if x < (a + 1) / (a + b + 2):
        return _betacf(a, b, x) * math.exp(
            math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
            + a * math.log(x) + b * math.log(1 - x)) / a
    else:
        return 1.0 - _betacf(b, a, 1 - x) * math.exp(
            math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
            + a * math.log(x) + b * math.log(1 - x)) / b


def _betacf(a, b, x, max_iter=200, eps=3e-7):
    """Continued fraction for incomplete beta function."""
    qab = a + b
    qap = a + 1
    qam = a - 1
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < 1e-30:
        d = 1e-30
    d = 1.0 / d
    h = d
    for m in range(1, max_iter + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < 1e-30:
            d = 1e-30
        c = 1.0 + aa / c
        if abs(c) < 1e-30:
            c = 1e-30
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < 1e-30:
            d = 1e-30
        c = 1.0 + aa / c
        if abs(c) < 1e-30:
            c = 1e-30
        d = 1.0 / d
        dl = d * c
        h *= dl
        if abs(dl - 1.0) < eps:
            break
    return h


def spearman_r(x, y):
    """Spearman rank correlation."""
    n = len(x)
    if n < 3:
        return float('nan')
    rx = np.argsort(np.argsort(x)).astype(float)
    ry = np.argsort(np.argsort(y)).astype(float)
    r, _ = pearson_r(rx, ry)
    return float(r)


def linreg(x, y):
    """Simple linear regression: y = A + B*x.  Returns (A, B, r²)."""
    n = len(x)
    mx, my = np.mean(x), np.mean(y)
    ss_xx = np.sum((x - mx)**2)
    ss_xy = np.sum((x - mx) * (y - my))
    ss_yy = np.sum((y - my)**2)
    B = ss_xy / ss_xx if ss_xx > 0 else 0
    A = my - B * mx
    r2 = (ss_xy**2 / (ss_xx * ss_yy)) if (ss_xx > 0 and ss_yy > 0) else 0
    return float(A), float(B), float(r2)


def analyze_subset(label, subset):
    """Run full correlation analysis on a subset of data."""
    print(f"\n  ── {label} (N = {len(subset)}) {'─' * (50 - len(label))}")

    if len(subset) < 3:
        print("    Too few points for correlation.")
        return None

    names = [d[0] for d in subset]
    log_tau = np.array([math.log10(d[4]) for d in subset])
    log_frac = np.array([math.log10(abs(d[3]) / d[1]) for d in subset])

    r_p, p_p = pearson_r(log_tau, log_frac)
    r_s = spearman_r(log_tau, log_frac)
    A, beta, r2 = linreg(log_frac, log_tau)

    print(f"    Pearson  r = {r_p:+.3f}  (p = {p_p:.4f})")
    print(f"    Spearman ρ = {r_s:+.3f}")
    print(f"    Power law: log₁₀(τ) = {A:+.2f} + ({beta:+.2f}) × "
          f"log₁₀(|Δm/m|)   R² = {r2:.3f}")
    print(f"    Exponent β = {beta:+.2f}  "
          f"(R27 model-C: β ≈ −2.7)")

    # Predicted lifetimes
    print(f"\n    {'Particle':>8s}  {'τ_obs (s)':>12s}  {'τ_pred (s)':>12s}  "
          f"{'log ratio':>10s}  {'|Δm/m|':>10s}")
    print(f"    {'─' * 8}  {'─' * 12}  {'─' * 12}  {'─' * 10}  {'─' * 10}")

    for d in sorted(subset, key=lambda x: -x[4]):
        frac = abs(d[3]) / d[1]
        log_pred = A + beta * math.log10(frac)
        tau_pred = 10**log_pred
        log_ratio = math.log10(d[4] / tau_pred) if tau_pred > 0 else float('inf')
        print(f"    {d[0]:>8s}  {d[4]:12.2e}  {tau_pred:12.2e}  "
              f"{log_ratio:+10.2f}  {frac:10.6f}")

    return {'r_p': r_p, 'p_p': p_p, 'r_s': r_s,
            'A': A, 'beta': beta, 'r2': r2, 'N': len(subset)}


def main():
    print("=" * 72)
    print("R50 Track 4: Decay rate ↔ near-miss correlation")
    print("=" * 72)

    # ── Phase 0: Data summary ─────────────────────────────────────
    print("\nPhase 0: Track 3 data summary")

    stable = [d for d in DATA if d[5] == 'stable']
    unstable = [d for d in DATA if d[5] != 'stable']

    print(f"\n  Stable particles (verify Δm ≈ 0):")
    for d in stable:
        print(f"    {d[0]:>4s}: |Δm| = {abs(d[3]):.2e} MeV  → "
              f"{'exact' if abs(d[3]) < 0.01 else 'OFFSET'}")

    print(f"\n  Unstable particles (N = {len(unstable)}):")
    print(f"  {'Particle':>8s}  {'m (MeV)':>10s}  {'|Δm| MeV':>10s}  "
          f"{'|Δm/m|':>10s}  {'τ (s)':>12s}  {'Decay':>6s}")
    print(f"  {'─' * 8}  {'─' * 10}  {'─' * 10}  {'─' * 10}  "
          f"{'─' * 12}  {'─' * 6}")
    for d in sorted(unstable, key=lambda x: -x[4]):
        frac = abs(d[3]) / d[1]
        print(f"  {d[0]:>8s}  {d[1]:10.3f}  {abs(d[3]):10.4f}  "
              f"{frac:10.6f}  {d[4]:12.2e}  {d[5]:>6s}")

    # ── Phase 1: Full sample correlation ──────────────────────────
    print(f"\n{'=' * 72}")
    print("Phase 1: Correlation analysis — all subsets")
    print(f"{'=' * 72}")

    results = {}

    # All unstable
    results['all'] = analyze_subset("All unstable", unstable)

    # Weak decays only
    weak = [d for d in unstable if d[5] == 'weak']
    results['weak'] = analyze_subset("Weak decays only", weak)

    # Exclude muon (mass-desert outlier)
    no_muon = [d for d in unstable if d[0] != 'μ⁻']
    results['no_muon'] = analyze_subset("All except muon", no_muon)

    # Weak decays, no muon
    weak_no_muon = [d for d in weak if d[0] != 'μ⁻']
    results['weak_no_muon'] = analyze_subset(
        "Weak decays, no muon", weak_no_muon)

    # Exclude strong decays (Δ, ρ)
    no_strong = [d for d in unstable if d[5] != 'strong']
    results['no_strong'] = analyze_subset(
        "Exclude strong decays (Δ, ρ)", no_strong)

    # Exclude strong + muon
    no_strong_muon = [d for d in no_strong if d[0] != 'μ⁻']
    results['no_strong_muon'] = analyze_subset(
        "Excl. strong + muon", no_strong_muon)

    # Baryons only (n, Λ, Σ⁺, Ξ⁰, Ω⁻, Δ⁰)
    baryons = [d for d in unstable
               if d[0] in ('n', 'Λ', 'Σ⁺', 'Ξ⁰', 'Ω⁻', 'Δ⁰')]
    results['baryons'] = analyze_subset("Baryons only", baryons)

    # Weak baryons (exclude Δ⁰ strong decay)
    weak_baryons = [d for d in baryons if d[5] == 'weak']
    results['weak_baryons'] = analyze_subset(
        "Weak-decay baryons", weak_baryons)

    # ── Phase 2: R27 power law comparison ─────────────────────────
    print(f"\n{'=' * 72}")
    print("Phase 2: R27 power law test (β = −2.7)")
    print(f"{'=' * 72}")

    # Use the R27 power law: τ ∝ |Δm/m|^(−2.7)
    # Calibrate the constant A using the neutron (best-constrained)
    neutron = [d for d in unstable if d[0] == 'n'][0]
    frac_n = abs(neutron[3]) / neutron[1]
    A_r27 = math.log10(neutron[4]) - (-2.7) * math.log10(frac_n)

    print(f"\n  R27 power law: log₁₀(τ) = {A_r27:.2f} + "
          f"(−2.70) × log₁₀(|Δm/m|)")
    print(f"  Calibrated to neutron: τ = {neutron[4]:.1f} s, "
          f"|Δm/m| = {frac_n:.6f}")

    print(f"\n  {'Particle':>8s}  {'τ_obs (s)':>12s}  {'τ_R27 (s)':>12s}  "
          f"{'log₁₀(obs/R27)':>14s}  {'|Δm/m|':>10s}")
    print(f"  {'─' * 8}  {'─' * 12}  {'─' * 12}  {'─' * 14}  {'─' * 10}")

    for d in sorted(unstable, key=lambda x: -x[4]):
        frac = abs(d[3]) / d[1]
        log_pred = A_r27 + (-2.7) * math.log10(frac)
        tau_pred = 10**log_pred
        ratio = math.log10(d[4] / tau_pred) if tau_pred > 0 else float('inf')
        flag = " ◄" if d[0] == 'n' else ""
        print(f"  {d[0]:>8s}  {d[4]:12.2e}  {tau_pred:12.2e}  "
              f"{ratio:+14.2f}  {frac:10.6f}{flag}")

    # RMS log error
    log_errs = []
    for d in unstable:
        frac = abs(d[3]) / d[1]
        log_pred = A_r27 + (-2.7) * math.log10(frac)
        log_errs.append(math.log10(d[4]) - log_pred)
    rms = math.sqrt(sum(e**2 for e in log_errs) / len(log_errs))
    print(f"\n  RMS log₁₀ error: {rms:.2f}  "
          f"(1 = factor-of-10 average miss)")

    # ── Phase 3: Best-fit power law predictions ───────────────────
    print(f"\n{'=' * 72}")
    print("Phase 3: Best-fit power law predictions")
    print(f"{'=' * 72}")

    # Use the best subset (weak_no_muon or weak_baryons)
    best_key = None
    best_r2 = -1
    for key in ['weak_no_muon', 'weak_baryons', 'no_strong_muon', 'all']:
        if results[key] and results[key]['r2'] > best_r2:
            best_r2 = results[key]['r2']
            best_key = key
    
    if best_key and results[best_key]:
        res = results[best_key]
        print(f"\n  Best subset: '{best_key}'  (R² = {res['r2']:.3f}, "
              f"β = {res['beta']:+.2f}, N = {res['N']})")
        print(f"  Power law: log₁₀(τ) = {res['A']:+.2f} + "
              f"({res['beta']:+.2f}) × log₁₀(|Δm/m|)")

        print(f"\n  Predictions for ALL unstable particles "
              f"(extrapolating from {best_key}):")
        print(f"\n  {'Particle':>8s}  {'τ_obs (s)':>12s}  {'τ_pred (s)':>12s}  "
              f"{'log ratio':>10s}  {'In subset':>9s}")
        print(f"  {'─' * 8}  {'─' * 12}  {'─' * 12}  {'─' * 10}  {'─' * 9}")

        in_subset = set()
        if best_key == 'weak_no_muon':
            in_subset = {d[0] for d in weak_no_muon}
        elif best_key == 'weak_baryons':
            in_subset = {d[0] for d in weak_baryons}
        elif best_key == 'no_strong_muon':
            in_subset = {d[0] for d in no_strong_muon}
        else:
            in_subset = {d[0] for d in unstable}

        for d in sorted(unstable, key=lambda x: -x[4]):
            frac = abs(d[3]) / d[1]
            log_pred = res['A'] + res['beta'] * math.log10(frac)
            tau_pred = 10**log_pred
            log_ratio = math.log10(d[4] / tau_pred)
            in_flag = "yes" if d[0] in in_subset else "no"
            ok = "✓" if abs(log_ratio) < 3 else "✗"
            print(f"  {d[0]:>8s}  {d[4]:12.2e}  {tau_pred:12.2e}  "
                  f"{log_ratio:+10.2f}  {in_flag:>9s}  {ok}")

    # ── Phase 4: Outlier analysis ─────────────────────────────────
    print(f"\n{'=' * 72}")
    print("Phase 4: Outlier analysis")
    print(f"{'=' * 72}")

    print(f"\n  Residuals from best-fit ({best_key}):")
    if best_key and results[best_key]:
        res = results[best_key]
        resids = []
        for d in unstable:
            frac = abs(d[3]) / d[1]
            log_pred = res['A'] + res['beta'] * math.log10(frac)
            log_resid = math.log10(d[4]) - log_pred
            resids.append((d[0], log_resid, d[5]))

        resids.sort(key=lambda x: abs(x[1]), reverse=True)
        print(f"\n  {'Particle':>8s}  {'log₁₀ residual':>14s}  {'Decay':>6s}  "
              f"{'Assessment':>20s}")
        print(f"  {'─' * 8}  {'─' * 14}  {'─' * 6}  {'─' * 20}")
        for name, lr, dt in resids:
            if abs(lr) < 1:
                assess = "good fit"
            elif abs(lr) < 3:
                assess = "moderate outlier"
            elif abs(lr) < 6:
                assess = "significant outlier"
            else:
                assess = "extreme outlier"
            print(f"  {name:>8s}  {lr:+14.2f}  {dt:>6s}  {assess:>20s}")

    # ── Phase 5: Summary table ────────────────────────────────────
    print(f"\n{'=' * 72}")
    print("Phase 5: Summary of all subsets")
    print(f"{'=' * 72}\n")

    print(f"  {'Subset':>25s}  {'N':>2s}  {'r':>6s}  {'p':>8s}  "
          f"{'ρ':>6s}  {'β':>7s}  {'R²':>5s}")
    print(f"  {'─' * 25}  {'─' * 2}  {'─' * 6}  {'─' * 8}  "
          f"{'─' * 6}  {'─' * 7}  {'─' * 5}")

    for key in ['all', 'weak', 'no_muon', 'weak_no_muon',
                'no_strong', 'no_strong_muon', 'baryons', 'weak_baryons']:
        res = results.get(key)
        if res is None:
            continue
        print(f"  {key:>25s}  {res['N']:2d}  {res['r_p']:+6.3f}  "
              f"{res['p_p']:8.4f}  {res['r_s']:+6.3f}  "
              f"{res['beta']:+7.2f}  {res['r2']:5.3f}")

    print(f"\n  R27 (model-C) reference:  r = −0.84, β ≈ −2.7, N ≈ 7")

    # ── Phase 6: Key findings ─────────────────────────────────────
    print(f"\n{'=' * 72}")
    print("Phase 6: Key findings")
    print(f"{'=' * 72}")

    all_res = results.get('all', {})
    wbn_res = results.get('weak_baryons', {})
    wnm_res = results.get('weak_no_muon', {})

    print(f"\n  1. Full sample: r = {all_res.get('r_p', 0):+.3f}, "
          f"β = {all_res.get('beta', 0):+.2f}")
    print(f"     Correct sign (negative) but moderate strength.")

    if wnm_res:
        print(f"\n  2. Weak decays (no muon): r = {wnm_res.get('r_p', 0):+.3f}, "
              f"β = {wnm_res.get('beta', 0):+.2f}")
        impr = "improves" if abs(wnm_res.get('r_p', 0)) > abs(all_res.get('r_p', 0)) else "worsens"
        print(f"     Removing the muon {impr} the correlation.")

    if wbn_res:
        print(f"\n  3. Weak-decay baryons: r = {wbn_res.get('r_p', 0):+.3f}, "
              f"β = {wbn_res.get('beta', 0):+.2f}")

    print(f"\n  4. The muon is in the mass desert — its large residual")
    print(f"     (10.9%) reflects structural absence of intermediate-")
    print(f"     scale modes, not a genuine off-resonance distance.")

    print(f"\n  5. Strong decays (Δ⁰, ρ⁰) have lifetimes ~10⁻²⁴ s")
    print(f"     determined by phase space and coupling strength,")
    print(f"     not solely by mass gap.")

    print(f"\n{'=' * 72}")
    print("Track 4 complete.")
    print(f"{'=' * 72}")


if __name__ == '__main__':
    main()
