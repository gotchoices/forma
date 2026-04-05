"""
R49 Track 1a: Can many modes mimic three-flavor oscillations?

Takes the full mode spectrum from Track 1 at representative
(ε, s) points and simulates the oscillation signal when all
modes between ν₁ and ν₃ participate.  Tests whether a standard
3-flavor fit can absorb the extra modes, or whether detectable
residuals remain.

Oscillation probability (N mass eigenstates):
  P(ν_e → ν_μ) = |Σᵢ U*_eᵢ U_μᵢ exp(−i m²ᵢ L / 2E)|²

For simplicity, we use a toy mixing model where the coupling
of mode i to the "electron-like" and "muon-like" flavors is
set by a weight wᵢ (normalized to Σwᵢ² = 1), with a mixing
angle θ between the two flavors.
"""

import math
import numpy as np

PI = math.pi
DM2_21 = 7.53e-5   # eV²
DM2_31 = 2.530e-3  # eV²
TARGET_RATIO = DM2_31 / DM2_21


def mu_sq(n3, n4, s, eps):
    return (n3 / eps)**2 + (n4 - n3 * s)**2


def build_spectrum(eps, s, n3_max=10, n4_max=6):
    modes = []
    for n3 in range(-n3_max, n3_max + 1):
        for n4 in range(0, n4_max + 1):
            if n3 == 0 and n4 == 0:
                continue
            ms = mu_sq(n3, n4, s, eps)
            if ms > 0:
                modes.append((n3, n4, ms))
    modes.sort(key=lambda m: m[2])
    return modes


def get_masses_eV(modes, i_nu1, i_nu2, i_nu3):
    """Fix E₀ from Δm²₂₁, return all mode masses in eV."""
    dm21 = modes[i_nu2][2] - modes[i_nu1][2]
    if dm21 <= 0:
        return None, None
    E0_sq = DM2_21 / dm21
    E0 = math.sqrt(E0_sq)
    masses = [E0 * math.sqrt(m[2]) for m in modes]
    return masses, E0


def oscillation_probability(L_over_E, m_sq, weights_e, weights_mu):
    """
    P(ν_e → ν_μ) at given L/E (in km/GeV).

    L/E in natural units: phase = Δm² L / (4E) = 1.267 Δm² L/E
    where Δm² in eV², L in km, E in GeV.
    """
    N = len(m_sq)
    prob = np.zeros_like(L_over_E)

    for i in range(N):
        for j in range(N):
            dm2 = m_sq[i] - m_sq[j]
            phase = 1.267 * dm2 * L_over_E
            prob += (weights_e[i] * weights_mu[i] *
                     weights_e[j] * weights_mu[j] *
                     np.cos(phase))
    return prob


def three_flavor_probability(L_over_E, m1_sq, m2_sq, m3_sq,
                              theta12, theta13, theta23):
    """Standard 3-flavor P(ν_e → ν_μ) (no CP phase)."""
    s12, c12 = math.sin(theta12), math.cos(theta12)
    s13, c13 = math.sin(theta13), math.cos(theta13)
    s23, c23 = math.sin(theta23), math.cos(theta23)

    U = np.array([
        [c12*c13,             s12*c13,             s13],
        [-s12*c23 - c12*s23*s13, c12*c23 - s12*s23*s13, s23*c13],
        [s12*s23 - c12*c23*s13, -c12*s23 - s12*c23*s13, c23*c13],
    ])

    m_sq = [m1_sq, m2_sq, m3_sq]
    prob = np.zeros_like(L_over_E)
    for i in range(3):
        for j in range(3):
            dm2 = m_sq[i] - m_sq[j]
            phase = 1.267 * dm2 * L_over_E
            prob += U[0,i]*U[1,i] * U[0,j]*U[1,j] * np.cos(phase)
    return prob


def fit_3flavor(L_over_E, signal, m_sq_all, i1, i2, i3):
    """Brute-force best-fit 3-flavor model to the multi-mode signal.

    Fixes masses to the three "neutrino" modes, scans mixing angles.
    Returns best-fit parameters and residual RMS.
    """
    m1s = m_sq_all[i1]
    m2s = m_sq_all[i2]
    m3s = m_sq_all[i3]

    best_rms = 1e10
    best_params = None

    for t12 in np.linspace(0.1, 0.9, 17):
        for t13 in np.linspace(0.01, 0.3, 13):
            for t23 in np.linspace(0.3, 1.2, 17):
                pred = three_flavor_probability(
                    L_over_E, m1s, m2s, m3s, t12, t13, t23)
                rms = math.sqrt(np.mean((signal - pred)**2))
                if rms < best_rms:
                    best_rms = rms
                    best_params = (t12, t13, t23)

    return best_params, best_rms


def print_section(title):
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}\n")


def run_scenario(name, eps, s, nu_modes, weight_scheme, n3_max=10):
    """Run one multi-mode oscillation scenario.

    nu_modes: list of (n3, n4) for the three "neutrino" modes
    weight_scheme: 'uniform', 'dominant3', 'exp_decay'
    """
    print(f"\n  --- {name} ---")
    print(f"  ε = {eps}, s = {s}")
    print(f"  Neutrino triplet: {nu_modes}")
    print(f"  Weight scheme: {weight_scheme}")

    modes = build_spectrum(eps, s, n3_max=n3_max)

    nu_indices = []
    for n3t, n4t in nu_modes:
        for idx, (n3, n4, ms) in enumerate(modes):
            if n3 == n3t and n4 == n4t:
                nu_indices.append(idx)
                break

    if len(nu_indices) != 3:
        print(f"  ERROR: could not find all 3 modes")
        return

    i1, i2, i3 = nu_indices
    masses, E0 = get_masses_eV(modes, i1, i2, i3)
    if masses is None:
        print(f"  ERROR: degenerate modes")
        return

    m1, m2, m3 = masses[i1], masses[i2], masses[i3]
    print(f"  m₁ = {m1*1000:.2f}, m₂ = {m2*1000:.2f},"
          f" m₃ = {m3*1000:.2f} meV")

    window = [i for i, m in enumerate(modes)
              if modes[i1][2] <= m[2] <= modes[i3][2]]
    n_window = len(window)
    print(f"  Modes in [ν₁, ν₃] window: {n_window}")

    m_sq_all = [(masses[i])**2 for i in range(len(modes))]

    if weight_scheme == 'dominant3':
        weights = np.zeros(len(modes))
        weights[i1] = 0.55
        weights[i2] = 0.30
        weights[i3] = 0.15
        norm = math.sqrt(sum(w**2 for w in weights))
        weights /= norm
    elif weight_scheme == 'uniform':
        weights = np.zeros(len(modes))
        for i in window:
            weights[i] = 1.0
        norm = math.sqrt(sum(w**2 for w in weights))
        if norm > 0:
            weights /= norm
    elif weight_scheme == 'exp_decay':
        weights = np.zeros(len(modes))
        for i in window:
            rank = abs(i - i1) + abs(i - i2) + abs(i - i3)
            dist = min(abs(i - i1), abs(i - i2), abs(i - i3))
            weights[i] = math.exp(-dist / 3.0)
        norm = math.sqrt(sum(w**2 for w in weights))
        if norm > 0:
            weights /= norm

    theta_mix = 0.59  # ~34°, near θ₂₃
    weights_e = weights * math.cos(theta_mix)
    weights_mu = weights * math.sin(theta_mix)

    L_over_E = np.linspace(0.1, 5000, 20000)  # km/GeV

    signal = oscillation_probability(L_over_E, m_sq_all,
                                      weights_e, weights_mu)

    three_only_sq = [m_sq_all[i1], m_sq_all[i2], m_sq_all[i3]]
    w3 = np.zeros(3)
    w3[0], w3[1], w3[2] = 0.55, 0.30, 0.15
    w3 /= math.sqrt(sum(w3**2))
    w3_e = w3 * math.cos(theta_mix)
    w3_mu = w3 * math.sin(theta_mix)
    signal_3only = oscillation_probability(L_over_E, three_only_sq,
                                            w3_e, w3_mu)

    residual = signal - signal_3only
    rms = math.sqrt(np.mean(residual**2))
    max_dev = np.max(np.abs(residual))
    mean_signal = np.mean(np.abs(signal))

    print(f"\n  Multi-mode vs 3-mode comparison:")
    print(f"    RMS residual:     {rms:.6f}")
    print(f"    Max deviation:    {max_dev:.6f}")
    print(f"    Mean |signal|:    {mean_signal:.6f}")
    print(f"    Relative RMS:     {rms/mean_signal*100:.2f}%")
    print(f"    Relative max dev: {max_dev/mean_signal*100:.2f}%")

    best_params, best_rms = fit_3flavor(
        L_over_E, signal, m_sq_all, i1, i2, i3)
    print(f"\n  Best 3-flavor fit to multi-mode signal:")
    print(f"    θ₁₂ = {best_params[0]:.3f},"
          f" θ₁₃ = {best_params[1]:.3f},"
          f" θ₂₃ = {best_params[2]:.3f}")
    print(f"    Fit RMS: {best_rms:.6f}")
    print(f"    Fit quality: {best_rms/mean_signal*100:.2f}% of signal")

    detectable = best_rms / mean_signal > 0.01
    print(f"\n  Would extra modes be detectable (>1% residual)?"
          f"  {'YES' if detectable else 'NO'}")

    return {
        'n_window': n_window,
        'rms': rms,
        'max_dev': max_dev,
        'rel_rms': rms / mean_signal,
        'fit_rms': best_rms,
        'fit_rel': best_rms / mean_signal,
        'detectable': detectable,
    }


def main():
    print("R49 Track 1a: Can Many Modes Mimic Three-Flavor Oscillations?")
    print("=" * 70)

    print_section("SCENARIO A: Family A (ε=5, s=0.022, 26 modes)")

    results_A = {}
    for scheme in ['dominant3', 'exp_decay', 'uniform']:
        r = run_scenario(
            f"Family A / {scheme}",
            eps=5.0, s=0.022,
            nu_modes=[(1,1), (-1,1), (1,2)],
            weight_scheme=scheme)
        if r:
            results_A[scheme] = r

    print_section("SCENARIO B: Family B (ε=0.1, s=0.01, ~120 modes)")

    results_B = {}
    for scheme in ['dominant3', 'exp_decay', 'uniform']:
        r = run_scenario(
            f"Family B / {scheme}",
            eps=0.1, s=0.01,
            nu_modes=[(1,2), (2,2), (10,1)],
            weight_scheme=scheme)
        if r:
            results_B[scheme] = r

    print_section("SCENARIO C: Family C (ε=0.2, s=0.3, ~75 modes)")

    results_C = {}
    for scheme in ['dominant3', 'exp_decay', 'uniform']:
        r = run_scenario(
            f"Family C / {scheme}",
            eps=0.2, s=0.3,
            nu_modes=[(0,2), (-1,2), (6,1)],
            weight_scheme=scheme)
        if r:
            results_C[scheme] = r

    print_section("SUMMARY")

    print(f"  {'Scenario':<30} {'N_modes':>7} {'Fit residual':>12}"
          f" {'Detectable?':>12}")
    print(f"  {'-'*30} {'-'*7} {'-'*12} {'-'*12}")

    for label, results in [('Family A (26 modes)', results_A),
                            ('Family B (~120 modes)', results_B),
                            ('Family C (~75 modes)', results_C)]:
        for scheme, r in results.items():
            tag = f"{label} / {scheme}"
            det = "YES" if r['detectable'] else "NO"
            print(f"  {tag:<30} {r['n_window']:>7}"
                  f" {r['fit_rel']*100:>11.2f}% {det:>12}")

    print()
    any_detectable = any(
        r['detectable']
        for results in [results_A, results_B, results_C]
        for r in results.values())

    if any_detectable:
        print("  CONCLUSION: Extra modes ARE detectable in at least")
        print("  some coupling scenarios.  A clean 3-flavor fit is")
        print("  not guaranteed when many modes participate.")
    else:
        print("  CONCLUSION: A 3-flavor fit absorbs the extra modes")
        print("  in all tested scenarios.  Many modes CAN mimic")
        print("  three-flavor oscillations.")


if __name__ == '__main__':
    main()
