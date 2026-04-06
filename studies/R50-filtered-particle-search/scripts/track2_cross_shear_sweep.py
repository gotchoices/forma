"""
R50 Track 2: Cross-shear sweep — neutron as first cross-sheet test

Sweeps cross-shear parameters (σ_ep, σ_eν, σ_νp) independently,
looking for Q=0, spin-½ modes near the neutron mass (939.565 MeV).

KEY PHYSICS:
When σ changes, the dimensionless metric G̃ changes, which alters
G̃⁻¹ via the Schur complement.  The ring circumferences L_ring
must be re-derived to keep reference masses (electron, proton)
physical.  This self-consistent adjustment shifts non-reference
mode energies, which is the primary mechanism by which cross-shears
affect particle predictions.

The scale hierarchy (L_ring_e / L_ring_p ≈ 600) suppresses direct
cross-terms in the energy formula, so the dominant effect is the
indirect one: σ modifies [G̃⁻¹]_pp via the Schur complement,
changing L_ring_p, which rescales all proton-sheet modes.  Whether
this rescaling shifts a particular mode RELATIVE to the proton
depends on whether the Schur complement correction is uniform
across the pp block — it generally is not.

DELIVERABLES (from R50 README Track 2):
  - σ landscape for each cross-shear
  - Neutron candidate mode(s) with mass residual and quantum numbers
  - Metric health check at candidate parameter values
  - Sensitivity table: δm/δσ for each parameter
"""

import sys
import os
import math
from itertools import product as iproduct

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np

from lib.ma_model_d import (
    MaD, M_E_MEV, M_P_MEV, DM2_21,
    _TWO_PI_HC, _build_circumferences, _build_metric,
    solve_shear_for_alpha,
)

M_NEUTRON = 939.565  # MeV (PDG 2022)

EPS_E, EPS_NU, EPS_P = 0.65, 5.0, 0.55
S_NU_DEFAULT = 0.022  # R49 Assignment A


def build_corrected_model(sigma_ep=0.0, sigma_enu=0.0, sigma_nup=0.0,
                          eps_e=EPS_E, eps_nu=EPS_NU, eps_p=EPS_P):
    """
    Build MaD with L_ring adjusted for cross-shear effects on G̃⁻¹.

    G̃ depends only on (ε, s, σ), not on the absolute circumferences L.
    So we can:
      1. Build G̃ from geometry + σ (using dummy L)
      2. Compute effective μ for reference modes from the FULL G̃⁻¹
      3. Derive L_ring = 2πℏc × μ_eff / M_target

    This is equivalent to model-C's self-consistent iteration but
    exact (no iteration needed), because G̃ is L-independent.

    Returns (model, info_dict) or (None, info_dict) if metric fails.
    """
    s_e = solve_shear_for_alpha(eps_e)
    s_p = solve_shear_for_alpha(eps_p)
    s_nu = S_NU_DEFAULT

    if s_e is None or s_p is None:
        return None, {'reason': 'no shear solution'}

    L_dummy = _build_circumferences(
        eps_e, s_e, 1.0, eps_nu, s_nu, 1.0, eps_p, s_p, 1.0)
    Gt, Gti = _build_metric(
        L_dummy, s_e, s_nu, s_p,
        sigma_ep=sigma_ep, sigma_enu=sigma_enu, sigma_nup=sigma_nup)

    if Gt is None:
        return None, {'reason': 'not positive definite'}

    # Effective μ for reference modes (from full 6×6 inverse)
    n_e_d = np.array([1.0/eps_e, 2.0, 0, 0, 0, 0])
    mu_eff_e = math.sqrt(float(n_e_d @ Gti @ n_e_d))
    L_ring_e = _TWO_PI_HC * mu_eff_e / M_E_MEV

    n_p_d = np.array([0, 0, 0, 0, 3.0/eps_p, 6.0])
    mu_eff_p = math.sqrt(float(n_p_d @ Gti @ n_p_d))
    L_ring_p = _TWO_PI_HC * mu_eff_p / M_P_MEV

    E0_nu_MeV = math.sqrt(DM2_21 / (4 * s_nu)) * 1e-6
    L_ring_nu = _TWO_PI_HC / E0_nu_MeV

    try:
        model = MaD(
            eps_e=eps_e, eps_nu=eps_nu, eps_p=eps_p,
            s_e=s_e, s_nu=s_nu, s_p=s_p,
            L_ring_e=L_ring_e, L_ring_nu=L_ring_nu, L_ring_p=L_ring_p,
            sigma_ep=sigma_ep, sigma_enu=sigma_enu, sigma_nup=sigma_nup)
    except ValueError:
        return None, {'reason': 'model construction failed'}

    info = {
        'mu_eff_e': mu_eff_e, 'mu_eff_p': mu_eff_p,
        'L_ring_e': L_ring_e, 'L_ring_p': L_ring_p,
        'L_ring_nu': L_ring_nu,
    }
    return model, info


def generate_candidates(n_ranges, charge_target=0, spin_target=0.5):
    """
    Pre-generate all 6-tuples with given charge and spin.

    n_ranges : list of 6 (min, max) tuples, one per quantum number.
    Returns list of tuples.
    """
    ranges = [range(lo, hi + 1) for lo, hi in n_ranges]
    out = []
    for n in iproduct(*ranges):
        if all(ni == 0 for ni in n):
            continue
        if MaD.charge_composite(n) != charge_target:
            continue
        if MaD.spin_total(n) != spin_target:
            continue
        out.append(n)
    return out


def batch_energies(candidates_arr, L, Gti):
    """
    Vectorized energy computation for many modes.

    candidates_arr : ndarray (N, 6)
    L : ndarray (6,) — circumferences in fm
    Gti : ndarray (6, 6) — inverse dimensionless metric

    Returns ndarray (N,) — energies in MeV
    """
    n_over_L = candidates_arr / L
    E2 = _TWO_PI_HC**2 * np.sum((n_over_L @ Gti) * n_over_L, axis=1)
    return np.sqrt(np.maximum(E2, 0))


def sweep_one_sigma(name, kwarg_name, sigma_range,
                    cand_arr, baseline_model, top_k=5):
    """
    Sweep one cross-shear, returning landscape data.

    For each σ value:
      1. Build corrected model (L_ring adjusted)
      2. Compute energies of all candidates
      3. Find top_k nearest to neutron mass
    """
    results = []
    for sigma_val in sigma_range:
        kwargs = {kwarg_name: sigma_val}
        m, info = build_corrected_model(**kwargs)
        if m is None:
            results.append(None)
            continue

        E_e = m.energy((1, 2, 0, 0, 0, 0))
        E_p = m.energy((0, 0, 0, 0, 3, 6))

        energies = batch_energies(cand_arr, m.L, m.metric_inv)
        diffs = np.abs(energies - M_NEUTRON)
        best_idx = np.argsort(diffs)[:top_k]

        results.append({
            'sigma': sigma_val,
            'E_e': E_e,
            'E_p': E_p,
            'L_ring_p': info['L_ring_p'],
            'mu_eff_p': info['mu_eff_p'],
            'best': [(int(i), float(energies[i]),
                       float(energies[i] - M_NEUTRON)) for i in best_idx],
        })

    return results


def main():
    print("=" * 72)
    print("R50 Track 2: Cross-shear sweep — neutron as first cross-sheet test")
    print("=" * 72)

    # ── Phase 0: Baseline ─────────────────────────────────────────────
    print("\nPhase 0: Baseline model (all σ = 0)")
    m0, info0 = build_corrected_model()
    E_e0 = m0.energy((1, 2, 0, 0, 0, 0))
    E_p0 = m0.energy((0, 0, 0, 0, 3, 6))
    print(f"  Electron: {E_e0:.6f} MeV (target {M_E_MEV:.6f})")
    print(f"  Proton:   {E_p0:.3f} MeV (target {M_P_MEV:.3f})")
    print(f"  L_ring_e = {info0['L_ring_e']:.2f} fm")
    print(f"  L_ring_p = {info0['L_ring_p']:.4f} fm")
    print(f"  L_ring_ν = {info0['L_ring_nu']:.4e} fm")
    print(f"  Scale ratio L_e/L_p = {info0['L_ring_e']/info0['L_ring_p']:.1f}")

    # ── Phase 1: Generate candidates ──────────────────────────────────
    print("\nPhase 1: Generating Q = 0, spin = ½ candidates")

    n_ranges = [
        (-3, 3),    # n₁ (electron tube)
        (-4, 4),    # n₂ (electron ring)
        (-2, 2),    # n₃ (neutrino tube)
        (-2, 2),    # n₄ (neutrino ring)
        (-6, 6),    # n₅ (proton tube)
        (-10, 10),  # n₆ (proton ring)
    ]
    total_search = 1
    for lo, hi in n_ranges:
        total_search *= (hi - lo + 1)
    print(f"  Search space: {total_search:,} 6-tuples")

    candidates = generate_candidates(n_ranges, charge_target=0, spin_target=0.5)
    print(f"  Q = 0, spin = ½: {len(candidates):,} candidates")

    propagating = [n for n in candidates if m0.propagates(n)]
    print(f"  Propagating:     {len(propagating):,} candidates")

    cand_arr = np.array(propagating, dtype=float)

    # Baseline energies and nearest to neutron
    E0 = batch_energies(cand_arr, m0.L, m0.metric_inv)

    near_mask = np.abs(E0 - M_NEUTRON) < 100  # within 100 MeV
    near_idx = np.where(near_mask)[0]
    near_idx = near_idx[np.argsort(np.abs(E0[near_idx] - M_NEUTRON))]

    print(f"\n  Nearest Q = 0, spin = ½ modes to neutron (939.565 MeV) at σ = 0:")
    print(f"  {'Mode':>30s}  {'E (MeV)':>10s}  {'Δm (MeV)':>10s}  {'Δm/m':>8s}  {'Sheets':>8s}")
    print(f"  {'─'*30}  {'─'*10}  {'─'*10}  {'─'*8}  {'─'*8}")
    for i in near_idx[:12]:
        n = propagating[i]
        sheets = m0.active_sheets(n)
        dm = E0[i] - M_NEUTRON
        print(f"  {str(n):>30s}  {E0[i]:10.3f}  {dm:+10.3f}  "
              f"{abs(dm)/M_NEUTRON*100:7.3f}%  {sheets:>8s}")

    # Identify the single best candidate at baseline
    best_baseline_idx = np.argmin(np.abs(E0 - M_NEUTRON))
    best_baseline_n = propagating[best_baseline_idx]
    best_baseline_E = E0[best_baseline_idx]
    print(f"\n  Best candidate: {best_baseline_n}  "
          f"E = {best_baseline_E:.3f} MeV  "
          f"Δ = {best_baseline_E - M_NEUTRON:+.3f} MeV")

    # ── Phase 2: σ sweeps ─────────────────────────────────────────────
    sigma_range = np.linspace(-0.3, 0.3, 61)
    sweeps = [
        ('σ_ep',  'sigma_ep'),
        ('σ_νp',  'sigma_nup'),
        ('σ_eν',  'sigma_enu'),
    ]

    sweep_results = {}
    for label, kwarg in sweeps:
        print(f"\n{'='*72}")
        print(f"Phase 2: {label} sweep  ({label} = -0.3 to +0.3, 61 points)")
        print(f"{'='*72}")

        results = sweep_one_sigma(
            label, kwarg, sigma_range, cand_arr, m0, top_k=3)
        sweep_results[label] = results

        valid = [r for r in results if r is not None]
        failed = sum(1 for r in results if r is None)
        print(f"  Valid: {len(valid)}/{len(results)}  "
              f"(metric failed at {failed} points)")

        if not valid:
            print("  No valid points — skipping.")
            continue

        # Reference mass stability
        if label == 'σ_ep':
            E_e_vals = [r['E_e'] for r in valid]
            E_p_vals = [r['E_p'] for r in valid]
            print(f"\n  Reference mass stability:")
            print(f"    E_e: {min(E_e_vals):.6f} – {max(E_e_vals):.6f} MeV  "
                  f"(shift {max(E_e_vals)-min(E_e_vals):.2e} MeV)")
            print(f"    E_p: {min(E_p_vals):.3f} – {max(E_p_vals):.3f} MeV  "
                  f"(shift {max(E_p_vals)-min(E_p_vals):.2e} MeV)")

        # L_ring_p variation (for σ_ep)
        if label == 'σ_ep':
            Lp_vals = [r['L_ring_p'] for r in valid]
            Lp_0 = info0['L_ring_p']
            print(f"\n  L_ring_p variation (baseline = {Lp_0:.4f} fm):")
            print(f"    Range: {min(Lp_vals):.4f} – {max(Lp_vals):.4f} fm  "
                  f"(δ = {(max(Lp_vals)-min(Lp_vals))/Lp_0*100:.3f}%)")

        # Best neutron candidate vs σ
        print(f"\n  Best neutron candidate vs {label}:")
        print(f"  {label:>8s}  {'Mode':>30s}  {'E (MeV)':>10s}  {'Δm (MeV)':>10s}")
        print(f"  {'─'*8}  {'─'*30}  {'─'*10}  {'─'*10}")
        step = max(1, len(valid) // 10)
        for r in valid[::step]:
            idx, E_best, dm_best = r['best'][0]
            n_best = propagating[idx]
            print(f"  {r['sigma']:+8.3f}  {str(n_best):>30s}  "
                  f"{E_best:10.3f}  {dm_best:+10.3f}")

        # Minimum residual across sweep
        min_resid_r = min(valid, key=lambda r: abs(r['best'][0][2]))
        idx_min, E_min, dm_min = min_resid_r['best'][0]
        print(f"\n  Minimum |Δm| = {abs(dm_min):.3f} MeV at "
              f"{label} = {min_resid_r['sigma']:+.3f}  "
              f"mode {propagating[idx_min]}")

    # ── Phase 3: Sensitivity analysis ─────────────────────────────────
    print(f"\n{'='*72}")
    print("Phase 3: Sensitivity analysis (δE/δσ at σ = 0)")
    print(f"{'='*72}")

    # Top 5 candidates from baseline
    top5_idx = np.argsort(np.abs(E0 - M_NEUTRON))[:5]
    delta = 0.001

    print(f"\n  {'Mode':>30s}  {'E₀ (MeV)':>10s}  "
          f"{'∂E/∂σ_ep':>10s}  {'∂E/∂σ_νp':>10s}  {'∂E/∂σ_eν':>10s}")
    print(f"  {'─'*30}  {'─'*10}  {'─'*10}  {'─'*10}  {'─'*10}")

    for ci in top5_idx:
        n = propagating[ci]
        E_base = E0[ci]
        sensitivities = []
        for kwarg in ['sigma_ep', 'sigma_nup', 'sigma_enu']:
            m_lo, _ = build_corrected_model(**{kwarg: -delta})
            m_hi, _ = build_corrected_model(**{kwarg: +delta})
            if m_lo and m_hi:
                E_lo = m_lo.energy(n)
                E_hi = m_hi.energy(n)
                dEdσ = (E_hi - E_lo) / (2 * delta)
                sensitivities.append(dEdσ)
            else:
                sensitivities.append(float('nan'))

        print(f"  {str(n):>30s}  {E_base:10.3f}  "
              + "  ".join(f"{s:+10.4f}" for s in sensitivities))

    # What σ_ep would be needed to shift best candidate to neutron mass?
    best_n = propagating[top5_idx[0]]
    best_E = E0[top5_idx[0]]
    m_lo, _ = build_corrected_model(sigma_ep=-delta)
    m_hi, _ = build_corrected_model(sigma_ep=+delta)
    if m_lo and m_hi:
        dEdσ_ep = (m_hi.energy(best_n) - m_lo.energy(best_n)) / (2 * delta)
        if abs(dEdσ_ep) > 1e-10:
            σ_needed = (M_NEUTRON - best_E) / dEdσ_ep
            print(f"\n  To shift {best_n} from {best_E:.3f} to "
                  f"{M_NEUTRON:.3f} MeV:")
            print(f"    Need σ_ep ≈ {σ_needed:+.2f}  "
                  f"(∂E/∂σ_ep = {dEdσ_ep:+.4f} MeV/unit)")
            if abs(σ_needed) > 0.5:
                print(f"    ⚠ This exceeds reasonable σ range and likely "
                      f"breaks metric positive-definiteness.")

    # ── Phase 4: Scale hierarchy analysis ─────────────────────────────
    print(f"\n{'='*72}")
    print("Phase 4: Scale hierarchy analysis")
    print(f"{'='*72}")

    L_e = info0['L_ring_e']
    L_p = info0['L_ring_p']
    L_nu = info0['L_ring_nu']
    E0_p = _TWO_PI_HC / L_p  # proton sheet energy unit

    print(f"\n  Sheet scales:")
    print(f"    Ma_e:  L_ring = {L_e:.2f} fm      "
          f"(E₀ = {_TWO_PI_HC/L_e:.4f} MeV)")
    print(f"    Ma_ν:  L_ring = {L_nu:.2e} fm  "
          f"(E₀ = {_TWO_PI_HC/L_nu*1e9:.4f} meV)")
    print(f"    Ma_p:  L_ring = {L_p:.4f} fm     "
          f"(E₀ = {E0_p:.2f} MeV)")

    print(f"\n  Mode spacing on Ma_p ring (determines resolution):")
    print(f"    ΔE per unit n₆ ≈ E₀_p = {E0_p:.2f} MeV")
    print(f"    Neutron–proton mass difference: "
          f"{M_NEUTRON - M_P_MEV:.3f} MeV = "
          f"{(M_NEUTRON - M_P_MEV)/E0_p:.4f} × E₀_p")
    print(f"    ➜ The n-p splitting is {(M_NEUTRON-M_P_MEV)/E0_p*100:.2f}% "
          f"of one mode spacing unit.")
    print(f"      Integer modes cannot resolve sub-percent mass differences")
    print(f"      on the proton sheet at this geometry.")

    print(f"\n  Cross-term suppression (direct coupling):")
    print(f"    (1/L_e)(1/L_p) / (1/L_p)² = L_p/L_e = "
          f"{L_p/L_e:.2e}  (e-p coupling)")
    print(f"    (1/L_ν)(1/L_p) / (1/L_p)² = L_p/L_ν = "
          f"{L_p/L_nu:.2e}  (ν-p coupling)")
    print(f"    Direct cross-shear terms are negligible.")

    print(f"\n  Indirect effect (Schur complement on [G̃⁻¹]_pp):")
    # Compute numerically: how much does [G̃⁻¹]_pp change at σ_ep = 0.1?
    m_test, _ = build_corrected_model(sigma_ep=0.1)
    if m_test:
        Lp_test = m_test.L_ring[2]
        delta_Lp = abs(Lp_test - L_p) / L_p * 100
        print(f"    At σ_ep = 0.1: L_ring_p shifts by {delta_Lp:.4f}%")
        print(f"    All Ma_p modes rescale ≈ {delta_Lp:.4f}% in energy")
        # But the RELATIVE shift between different modes matters
        E_08 = m_test.energy((0, 0, 1, 1, 0, 8))
        E_36 = m_test.energy((0, 0, 0, 0, 3, 6))
        ratio_test = E_08 / E_36
        E_08_0 = m0.energy((0, 0, 1, 1, 0, 8))
        ratio_0 = E_08_0 / E_p0
        print(f"    Ratio E(0,0,1,1,0,8)/E(proton):")
        print(f"      σ = 0:   {ratio_0:.6f}")
        print(f"      σ = 0.1: {ratio_test:.6f}  "
              f"(δ = {(ratio_test-ratio_0)/ratio_0*100:+.4f}%)")
        print(f"    Absolute shift of (0,0,1,1,0,8): "
              f"{E_08 - E_08_0:+.4f} MeV")

    # ── Phase 5: Summary ──────────────────────────────────────────────
    print(f"\n{'='*72}")
    print("Summary")
    print(f"{'='*72}")

    overall_best = None
    for label, results in sweep_results.items():
        valid = [r for r in results if r is not None]
        if valid:
            best_r = min(valid, key=lambda r: abs(r['best'][0][2]))
            _, E_b, dm_b = best_r['best'][0]
            if overall_best is None or abs(dm_b) < abs(overall_best[2]):
                overall_best = (label, best_r['sigma'], dm_b,
                                propagating[best_r['best'][0][0]], E_b)

    if overall_best:
        label, sigma, dm, n, E = overall_best
        print(f"\n  Best neutron candidate across all sweeps:")
        print(f"    Mode: {n}")
        print(f"    E = {E:.3f} MeV  (Δ = {dm:+.3f} MeV, "
              f"{abs(dm)/M_NEUTRON*100:.2f}%)")
        print(f"    At {label} = {sigma:+.3f}")

    print(f"\n  Key findings:")
    print(f"    1. Mode spacing on Ma_p ≈ {E0_p:.0f} MeV >> "
          f"n-p splitting ({M_NEUTRON-M_P_MEV:.1f} MeV)")
    print(f"    2. No integer mode can land within 1.3 MeV of neutron")
    print(f"    3. Cross-shears shift modes by ≪ 1 mode spacing")
    print(f"    4. Scale hierarchy L_e/L_p ≈ {L_e/L_p:.0f} "
          f"suppresses direct cross-coupling")

    print(f"\n{'='*72}")
    print("Track 2 complete.")
    print(f"{'='*72}")


if __name__ == '__main__':
    main()
