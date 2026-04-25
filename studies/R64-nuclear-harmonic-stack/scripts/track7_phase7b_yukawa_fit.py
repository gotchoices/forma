"""
R64 Track 7 Phase 7b — Yukawa fit analysis of the 7-tensor potential.

The 7-tensor's E(r) was computed in Phase 7a.  The standard SM nuclear
potential is approximately Yukawa-form V(r) ∝ -g²·exp(-mr)/r, where m
is the exchange particle's mass (~140 MeV for the pion, giving range
~1.4 fm).

This phase fits the 7-tensor's E(r) to several functional forms:
  - Yukawa: V_Y(r) = -A·exp(-m·r/ℏc)/r
  - Coulomb-like: V_C(r) = -A/r
  - Inverse-square: V_2(r) = -A/r²
  - Polynomial (the actual 7-tensor expansion): V_P(r) = A/r² + B/r

The goal: identify which form best describes the 7-tensor's E(r),
and if Yukawa fits, what mass m emerges.  If m ≈ 140 MeV (pion
mass), MaSt has implicitly produced pion-exchange physics.

Outputs:
  outputs/track7_phase7b_yukawa_fit.csv
  outputs/track7_phase7b_yukawa_fit.png
"""

import math
import csv
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# ─── Constants and Phase 7a setup ──────────────────────────────────────

EPS_P = 0.2052
S_P = 0.0250
K_P = 63.629
M_P = 938.272
M_N = 939.565
ALPHA = 1.0 / 137.035999084
HBAR_C = 197.3269804


def mu2_Ma(n_pt, n_pr):
    return (n_pt / EPS_P)**2 + (n_pr - S_P * n_pt)**2


def m_Ma(n_pt, n_pr):
    return K_P * math.sqrt(mu2_Ma(n_pt, n_pr))


def m_seven_tensor(r, n_pt, n_pr, sigma_t, sigma_r=0,
                   A=HBAR_C**2):
    if r < 1e-6:
        return float('inf')
    k_S = 1.0 / r
    m_ma = m_Ma(n_pt, n_pr)
    m2 = (m_ma**2
          + A * k_S**2
          + 2 * k_S * (sigma_t * n_pt + sigma_r * n_pr) * HBAR_C)
    return math.sqrt(max(m2, 0))


# ─── Generate E(r) curve ─────────────────────────────────────────────

# Use pn (deuteron) configuration at σ_t = -20 (Phase 7a's best fit)
N_PT, N_PR = 6, 0    # pn additive winding (deuteron)
SIGMA_T = -20.0
M_CONST_SUM = M_P + M_N

# Range of r: 0.5 to 5 fm (nuclear scale)
r_arr = np.linspace(0.5, 5.0, 200)
m_arr = np.array([m_seven_tensor(r, N_PT, N_PR, SIGMA_T) for r in r_arr])

# m(infinity) — asymptote at large r
m_far = m_seven_tensor(100.0, N_PT, N_PR, SIGMA_T)

# E(r) relative to asymptote (the "interaction potential")
V_ref = m_arr - m_far


# ─── Fit forms ───────────────────────────────────────────────────────

def yukawa_form(r, A, m):
    """Yukawa: V(r) = -A · exp(-m·r/ℏc) / r."""
    return -A * np.exp(-m * r / HBAR_C) / r


def coulomb_form(r, A):
    """V(r) = -A/r."""
    return -A / r


def inv_square_form(r, A):
    """V(r) = -A/r²."""
    return -A / r**2


def poly_form(r, A2, A1):
    """V(r) = A2/r² + A1/r (the 7-tensor's natural expansion)."""
    return A2 / r**2 + A1 / r


def fit_form(form, r, V, p0):
    try:
        popt, pcov = curve_fit(form, r, V, p0=p0, maxfev=20000)
        residuals = V - form(r, *popt)
        ss_res = np.sum(residuals**2)
        ss_tot = np.sum((V - np.mean(V))**2)
        r_squared = 1 - ss_res / ss_tot
        rms = np.sqrt(np.mean(residuals**2))
        return popt, r_squared, rms
    except Exception as e:
        return None, None, None


# ─── Main ─────────────────────────────────────────────────────────────

def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 110)
    print("R64 Track 7 Phase 7b — Yukawa fit analysis of 7-tensor E(r)")
    print("=" * 110)
    print()
    print(f"  Reference curve: pn at (n_pt, n_pr) = (6, 0), σ_t = {SIGMA_T}")
    print(f"  r range: {r_arr.min()} to {r_arr.max()} fm, {len(r_arr)} points")
    print(f"  m(∞) = {m_far:.3f} MeV (asymptote)")
    print(f"  m(constituents) = {M_CONST_SUM:.3f} MeV (m_p + m_n)")
    print(f"  E(∞) = m(∞) − m_constituent_sum = {m_far - M_CONST_SUM:.3f} MeV")
    print(f"  V(r) = m(r) − m(∞) (the interaction potential, asymptote subtracted)")
    print()
    print(f"  V(0.5 fm) = {V_ref[0]:.2f} MeV")
    print(f"  V(1.0 fm) = {V_ref[np.argmin(np.abs(r_arr - 1.0))]:.2f} MeV")
    print(f"  V(2.0 fm) = {V_ref[np.argmin(np.abs(r_arr - 2.0))]:.2f} MeV")
    print(f"  V(5.0 fm) = {V_ref[-1]:.2f} MeV")
    print()

    # ─── Fit each form ─────────────────────────────────────────────
    print("Fitting V(r) to four functional forms:")
    print("-" * 100)
    fits = {}

    # 1. Yukawa
    popt, r2, rms = fit_form(yukawa_form, r_arr, V_ref,
                              p0=[100, 140])
    if popt is not None:
        A_y, m_y = popt
        fits['yukawa'] = (popt, r2, rms)
        range_y = HBAR_C / m_y if m_y > 0 else float('inf')
        print(f"  Yukawa V_Y(r) = -A·exp(-m·r/ℏc)/r:")
        print(f"    A = {A_y:.3f} MeV·fm, m = {m_y:.3f} MeV")
        print(f"    Yukawa range = ℏc/m = {range_y:.3f} fm")
        print(f"    R² = {r2:.6f}, RMS residual = {rms:.4f} MeV")

    # 2. Coulomb
    popt, r2, rms = fit_form(coulomb_form, r_arr, V_ref, p0=[20])
    if popt is not None:
        A_c = popt[0]
        fits['coulomb'] = (popt, r2, rms)
        print(f"  Coulomb V_C(r) = -A/r:")
        print(f"    A = {A_c:.3f} MeV·fm")
        print(f"    R² = {r2:.6f}, RMS residual = {rms:.4f} MeV")

    # 3. Inverse-square
    popt, r2, rms = fit_form(inv_square_form, r_arr, V_ref, p0=[20])
    if popt is not None:
        A_2 = popt[0]
        fits['inv_square'] = (popt, r2, rms)
        print(f"  Inverse-square V₂(r) = -A/r²:")
        print(f"    A = {A_2:.3f} MeV·fm²")
        print(f"    R² = {r2:.6f}, RMS residual = {rms:.4f} MeV")

    # 4. Polynomial (7-tensor's structural form)
    popt, r2, rms = fit_form(poly_form, r_arr, V_ref, p0=[20, -20])
    if popt is not None:
        A2_p, A1_p = popt
        fits['poly'] = (popt, r2, rms)
        print(f"  Polynomial V_P(r) = A₂/r² + A₁/r:")
        print(f"    A₂ = {A2_p:.3f} MeV·fm², A₁ = {A1_p:.3f} MeV·fm")
        print(f"    R² = {r2:.6f}, RMS residual = {rms:.4f} MeV")

    print()

    # ─── Best fit comparison ─────────────────────────────────────────
    print("Comparison: which form fits best?")
    print("-" * 100)
    sorted_fits = sorted(fits.items(), key=lambda x: -x[1][1])
    print(f"  {'rank':>4s}  {'form':<20s}  {'R²':>10s}  {'RMS (MeV)':>12s}  {'parameters':<40s}")
    for i, (name, (popt, r2, rms)) in enumerate(sorted_fits):
        print(f"  {i+1:>4d}  {name:<20s}  {r2:>10.6f}  {rms:>12.4f}  {str([f'{p:.3f}' for p in popt]):<40s}")
    print()

    # ─── Yukawa-specific analysis ────────────────────────────────
    if 'yukawa' in fits:
        popt, r2, rms = fits['yukawa']
        A_y, m_y = popt
        print("Yukawa-specific analysis:")
        print("-" * 100)
        print(f"  Fitted exchange-particle mass: m = {m_y:.3f} MeV")
        print(f"  Pion mass (m_π): 139.57 MeV (charged), 134.98 MeV (neutral)")
        print(f"  Match to pion: m_fitted/m_π_charged = {m_y/139.57:.4f}")
        print()
        if m_y < 30:
            print(f"  → m ≈ 0 (Coulomb-like, NO Yukawa cutoff)")
            print(f"    The 7-tensor doesn't produce Yukawa exponential decay.")
        elif m_y < 100:
            print(f"  → m < 100 MeV: longer range than pion exchange.")
            print(f"    Might be intermediate-mass exchange or different mediator.")
        elif 100 < m_y < 200:
            print(f"  → m near pion mass!  Range ~{HBAR_C/m_y:.2f} fm.")
            print(f"    Suggestive of pion-exchange-like structure.")
        elif 200 < m_y < 1000:
            print(f"  → m heavier than pion (m ≈ {m_y:.0f}). Range ~{HBAR_C/m_y:.2f} fm.")
            print(f"    Possible vector-meson (ρ, ω) range?")
        else:
            print(f"  → m very heavy. Functional form is essentially")
            print(f"    a pole near zero, not a proper exchange.")
        print()

    # ─── Save data ─────────────────────────────────────────────────
    csv_path = out_dir / "track7_phase7b_yukawa_fit.csv"
    with open(csv_path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['r_fm', 'V_7tensor_MeV',
                     'V_yukawa_MeV', 'V_coulomb_MeV',
                     'V_inv_sq_MeV', 'V_poly_MeV'])
        for i, r in enumerate(r_arr):
            row = [r, V_ref[i]]
            for name, form, default_p in [
                ('yukawa', yukawa_form, [0, 140]),
                ('coulomb', coulomb_form, [0]),
                ('inv_square', inv_square_form, [0]),
                ('poly', poly_form, [0, 0])]:
                if name in fits:
                    row.append(form(r, *fits[name][0]))
                else:
                    row.append(0)
            w.writerow(row)

    # ─── Plot ──────────────────────────────────────────────────────
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Linear plot
    ax = axes[0]
    ax.plot(r_arr, V_ref, 'k-', linewidth=2, label='7-tensor V(r)')
    if 'yukawa' in fits:
        ax.plot(r_arr, yukawa_form(r_arr, *fits['yukawa'][0]),
                'b--', label=f"Yukawa: m={fits['yukawa'][0][1]:.0f} MeV")
    if 'coulomb' in fits:
        ax.plot(r_arr, coulomb_form(r_arr, *fits['coulomb'][0]),
                'g--', label='Coulomb: -A/r')
    if 'poly' in fits:
        ax.plot(r_arr, poly_form(r_arr, *fits['poly'][0]),
                'r:', linewidth=2, label='Poly: A₂/r² + A₁/r')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.set_xlabel('r (fm)')
    ax.set_ylabel('V(r) (MeV)')
    ax.set_title('7-tensor V(r) vs functional fits (linear)')
    ax.set_xlim(0.4, 5.5)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=9)

    # Log-log plot (for tail behavior)
    ax = axes[1]
    V_abs = np.abs(V_ref)
    ax.plot(r_arr, V_abs, 'k-', linewidth=2, label='|V_7tensor|')
    if 'yukawa' in fits:
        V_y = np.abs(yukawa_form(r_arr, *fits['yukawa'][0]))
        ax.plot(r_arr, V_y, 'b--', label=f'|Yukawa|')
    if 'coulomb' in fits:
        V_c = np.abs(coulomb_form(r_arr, *fits['coulomb'][0]))
        ax.plot(r_arr, V_c, 'g--', label='|Coulomb|')
    if 'poly' in fits:
        V_p = np.abs(poly_form(r_arr, *fits['poly'][0]))
        ax.plot(r_arr, V_p, 'r:', linewidth=2, label='|Poly|')
    ax.set_xlabel('r (fm)')
    ax.set_ylabel('|V(r)| (MeV)')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_title('Tail behavior: log-log')
    ax.grid(alpha=0.3, which='both')
    ax.legend(fontsize=9)

    plt.tight_layout()
    plt.savefig(out_dir / "track7_phase7b_yukawa_fit.png",
                dpi=150, bbox_inches='tight')
    plt.close()

    # ─── Verdict ──────────────────────────────────────────────────
    print("=" * 110)
    print("VERDICT — Phase 7b")
    print("=" * 110)
    print()

    best_form, (best_popt, best_r2, best_rms) = sorted_fits[0]
    print(f"  Best fit: {best_form} (R² = {best_r2:.6f})")

    # Compare specifically Yukawa vs Polynomial
    if 'yukawa' in fits and 'poly' in fits:
        y_r2 = fits['yukawa'][1]
        p_r2 = fits['poly'][1]
        if p_r2 > y_r2:
            print(f"  Polynomial fits better than Yukawa: R²(poly) = {p_r2:.6f} "
                  f"vs R²(Yukawa) = {y_r2:.6f}")
            print(f"  → 7-tensor is structurally polynomial (1/r² + 1/r), NOT Yukawa.")
            print(f"    The strong-force decay in this 7-tensor is power-law, not exponential.")
        else:
            print(f"  Yukawa fits better than polynomial: R²(Yukawa) = {y_r2:.6f} "
                  f"vs R²(poly) = {p_r2:.6f}")

    print()
    print(f"  CSV: {csv_path}")
    print(f"  Plot: {out_dir / 'track7_phase7b_yukawa_fit.png'}")


if __name__ == "__main__":
    main()
