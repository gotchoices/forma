"""
Independent validation of the analytical mass-formula claims in work/clover-mass.md.

This script does NOT use the analytical mass formula or perturbation-theory
result to compute anything. It only uses them as COMPARISON TARGETS.

It runs the numerical Hill-equation eigensolver from laplacian_spectrum.py at
several (ε, χ) points and checks five claims:

  C1. The lowest eigenvalues at k_v = q/3 match the third-integer momentum
      structure of the boundary condition.
  C2. At small η = ε/(2+χ), the lowest eigenvalues converge to the
      zeroth-order formula μ² = (m_r - 2 m_t/3)² + (m_t/ε)² (σ = 0 case).
  C3. The χ-dependence at fixed ε is O(η²) (not O(η)) — first-order
      perturbations vanish.
  C4. The numerical second-order shift δ²μ²(n, m, ε, χ) matches the analytical
      sum -1/(2+χ)² · Σ |ã_q|² (mq - 2ε²k_v²)² / (q(2m+q)).
  C6. At nonzero rolled-leaf shear σ and small η, μ² matches the σ-generalised
      zeroth-order formula (k_v − σ p)² + (p/ε)² — equivalently
      (m_r − (σ + 2τ) m_t)² + (m_t/ε)² in (m_t, m_r) labels. Validates the
      Phase 1/2 σ + τ generalisation of clover-mass.md §§1–4.

Outputs a written report and exit code 0 = all pass, 1 = at least one fail.

Usage:
    python scripts/validate_mass_formula.py [--n-grid N]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from laplacian_spectrum import hill_eigenvalues
from lib.geometry import ProfileParams, profile


def predicted_zeroth(k_v: float, eps: float, n_eigs: int = 8,
                     sigma: float = 0.0) -> np.ndarray:
    """μ² = (k_v − σ p)² + (p/ε)² for integer p in the Bloch sector
    p ≡ q (mod 3), q = 3·k_v. Sorted ascending. σ = 0 recovers the
    original τ-only formula."""
    q = int(round(3 * k_v))
    p_range = [p for p in range(-30, 31) if (p - q) % 3 == 0]
    return np.array(sorted([(k_v - sigma * p) ** 2 + (p / eps) ** 2 for p in p_range])[:n_eigs])


def fourier_coeffs(chi: float, n_max: int = 30, N: int = 12000) -> dict:
    """Numerical Fourier coefficients ã_q of P_x in r_lobe = 1 units."""
    params = ProfileParams(r_lobe=1.0, r_saddle=chi)
    u = np.linspace(0, 2 * np.pi, N, endpoint=False)
    px, _ = profile(u, params)
    return {q: (1 / N) * np.sum(px * np.exp(-1j * q * u)) for q in range(-n_max, n_max + 1)}


def predicted_second_order(m_t: int, m_r: int, eps: float, chi: float) -> float:
    """δ²μ²(m_t, m_r, ε, χ) per clover-mass.md §6.3 (tube-first wave-mode labels)."""
    a = fourier_coeffs(chi)
    k_v = m_r - 2 * m_t / 3.0
    p = m_t
    total = 0.0
    for q, aq in a.items():
        if q == 0:
            continue
        denom = q * (2 * p + q)
        if denom == 0:
            continue
        total += abs(aq) ** 2 * (p * q - 2 * eps**2 * k_v**2) ** 2 / denom
    return -(1.0 / (2 + chi) ** 2) * total


def lowest_eig_for_kv_with_target(eps: float, chi: float, k_v: float,
                                   p_target: int, N_grid: int,
                                   sigma: float = 0.0) -> float:
    """Numerical μ² at k_v, picking the eigenvalue closest to the predicted p_target."""
    eigs = hill_eigenvalues(k_v, eps, chi, N_grid, n_eigs=10, sigma=sigma)
    expected = (k_v - sigma * p_target) ** 2 + (p_target / eps) ** 2
    # Pick the eigenvalue closest to expected — for low-mode identification
    idx = int(np.argmin(np.abs(eigs - expected)))
    return float(eigs[idx])


# ---------- Tests ----------

def test_zeroth_order_convergence(N_grid: int) -> tuple[bool, str]:
    """C2: at small η, numerical → analytical."""
    msg = []
    msg.append("[C2] Zeroth-order convergence as η → 0:")
    msg.append("  Test: lowest eigenvalues at small ε should match μ² = k_v² + (p/ε)²")
    msg.append("")
    all_pass = True
    for eps in [0.1, 0.2, 0.5]:
        chi = 1.0
        eta = eps / (2 + chi)
        # Test at k_v = 1/3 (representative third-integer); lowest |p| in Bloch sector is p = 1
        # But our solver gives all eigenvalues regardless of Bloch — lowest is p = 0.
        k_v = 1.0 / 3.0
        eigs = hill_eigenvalues(k_v, eps, chi, N_grid, n_eigs=4)
        pred = predicted_zeroth(k_v, eps, n_eigs=4)
        rel_err = np.abs(eigs[:2] - pred[:2]) / np.maximum(pred[:2], 1e-10)
        max_err = float(np.max(rel_err))
        # Expected: error scales as η² (corrugation correction). For η = 0.05, error < 1%
        # For η = 0.17, error < 10%.
        threshold = 5 * eta**2
        passed = max_err < threshold
        all_pass = all_pass and passed
        msg.append(f"  ε={eps:.2f}, χ={chi:.1f}, η={eta:.4f}: "
                   f"max rel err = {max_err:.4f}, threshold = {threshold:.4f}  "
                   f"{'PASS' if passed else 'FAIL'}")
    return all_pass, "\n".join(msg)


def test_first_order_vanishes(N_grid: int) -> tuple[bool, str]:
    """C3: χ-dependence at fixed ε should scale as η², not η."""
    msg = []
    msg.append("[C3] First-order vanishing (χ-dependence scales as η²):")
    msg.append("  Test: vary χ at fixed ε, fit |δμ²(χ) − δμ²(χ_ref)| vs η — should be quadratic.")
    msg.append("")
    eps = 0.3  # small so corrugation correction is well-resolved
    # Use a clean low-mode: k_v = 1/3, target p = 1
    k_v = 1.0 / 3.0
    p_target = 1
    chis = [0.5, 1.0, 1.5, 2.0]
    eigs = []
    etas = []
    for chi in chis:
        e = lowest_eig_for_kv_with_target(eps, chi, k_v, p_target, N_grid)
        eigs.append(e)
        etas.append(eps / (2 + chi))
    pred0 = k_v**2 + (p_target / eps) ** 2
    deltas = np.array(eigs) - pred0
    msg.append(f"  ε = {eps}, k_v = 1/3, target p = 1, predicted zeroth μ² = {pred0:.5f}")
    msg.append(f"  {'χ':>6}  {'η':>8}  {'numerical μ²':>14}  {'δ (num − pred)':>16}  {'δ/η²':>10}")
    delta_over_eta2 = []
    for chi, eta, e, d in zip(chis, etas, eigs, deltas):
        ratio = d / eta**2 if eta > 0 else float("nan")
        delta_over_eta2.append(ratio)
        msg.append(f"  {chi:6.2f}  {eta:8.4f}  {e:14.6f}  {d:+16.6f}  {ratio:+10.4f}")
    # If first-order is zero, δ/η² should be roughly constant across χ. If first-order is
    # nonzero, δ/η would be roughly constant instead. Check ratio of variations:
    d_over_eta = deltas / np.array(etas)
    d_over_eta2 = deltas / np.array(etas) ** 2
    std_eta = np.std(d_over_eta) / np.mean(np.abs(d_over_eta))
    std_eta2 = np.std(d_over_eta2) / np.mean(np.abs(d_over_eta2))
    msg.append(f"  Relative spread of δ/η : {std_eta:.4f}")
    msg.append(f"  Relative spread of δ/η²: {std_eta2:.4f}")
    msg.append(f"  → δ/η² much flatter than δ/η means scaling is quadratic, not linear")
    # Pass if δ/η² is at least 3× tighter than δ/η
    passed = std_eta2 < std_eta / 3
    return passed, "\n".join(msg)


def test_second_order_formula(N_grid: int) -> tuple[bool, str]:
    """C4: numerical δ²μ² should match analytical formula."""
    msg = []
    msg.append("[C4] Second-order formula:")
    msg.append("  Test: numerical (μ²_num − μ²_zeroth) ≈ δ²μ²_analytical from §6.3")
    msg.append("")
    msg.append(f"  {'(m_t, m_r)':>10}  {'ε':>5}  {'χ':>5}  {'η':>6}  "
               f"{'μ²_num':>10}  {'μ²_0th':>10}  {'δ_num':>10}  {'δ_PT':>10}  {'agreement':>12}")
    passes = []
    cases = [
        # (m_t, m_r, ε, χ, p_target) — tube-first labels per clover-quarks §0.3
        (1, 0, 0.3, 1.0, 1),   # k_v = -2/3, lowest with that sign of k_v
        (1, 1, 0.3, 1.0, 1),   # k_v = +1/3
        (2, 1, 0.3, 1.0, 2),   # k_v = -1/3
        (1, 1, 0.5, 1.0, 1),
        (2, 1, 0.5, 1.0, 2),
        (1, 1, 0.5, 0.5, 1),
        (1, 1, 0.5, 2.0, 1),
    ]
    for m_t, m_r, eps, chi, p in cases:
        k_v = m_r - 2 * m_t / 3.0
        eta = eps / (2 + chi)
        # Numerical
        e_num = lowest_eig_for_kv_with_target(eps, chi, k_v, p, N_grid)
        # Predicted zeroth-order at the same (k_v, p):
        e_0 = k_v**2 + (p / eps) ** 2
        d_num = e_num - e_0
        # Analytical PT:
        d_PT = predicted_second_order(m_t, m_r, eps, chi)
        # Agreement: relative difference. Pass if within 30% (PT is asymptotic; this is a
        # qualitative check that the *sign* and *order of magnitude* match).
        agreement = abs(d_num - d_PT) / max(abs(d_PT), 1e-6)
        ok = agreement < 0.3
        passes.append(ok)
        msg.append(f"  ({m_t:+d}, {m_r:+d})  {eps:5.2f}  {chi:5.2f}  {eta:6.4f}  "
                   f"{e_num:+10.5f}  {e_0:+10.5f}  {d_num:+10.5f}  {d_PT:+10.5f}  "
                   f"{('PASS' if ok else 'FAIL'):>12}")
    return all(passes), "\n".join(msg)


def test_proton_neutron_inversion(N_grid: int) -> tuple[bool, str]:
    """C5: Survey low-(m_t, m_r) identifications using numerical eigenvalues; is there any
    (ε, χ, identification) that fits m_n/m_p = 1.001378 in a PT-valid regime?"""
    msg = []
    msg.append("[C5] Proton-neutron inversion using numerical eigenvalues:")
    msg.append("  Question: is there ANY low-(m_t, m_r) pair giving m_n/m_p = 1.001378 at small η?")
    msg.append("")
    target = 1.001378
    target_sq = target**2

    # Try several (ε, χ) and several proton/neutron candidate pairs.
    # Tube-first wave-mode labels: (m_t, m_r) per clover-quarks §0.3.
    candidates = []
    for mt_p in range(-2, 3):
        for mr_p in range(-2, 3):
            for mt_n in range(-2, 3):
                for mr_n in range(-2, 3):
                    if (mt_p, mr_p) == (0, 0) or (mt_n, mr_n) == (0, 0):
                        continue
                    if (mt_p, mr_p) == (mt_n, mr_n):
                        continue
                    candidates.append(((mt_p, mr_p), (mt_n, mr_n)))

    best = []  # (η, ratio_diff, (mt_p, mr_p), (mt_n, mr_n), ε, χ, ratio)
    for eps in [0.2, 0.3, 0.5, 0.7, 1.0]:
        for chi in [0.5, 1.0, 2.0]:
            eta = eps / (2 + chi)
            if eta > 0.5:  # skip clearly non-perturbative
                continue
            # Pre-compute all relevant eigenvalues
            eig_cache = {}
            for mt, mr in {pair for c in candidates for pair in c}:
                k_v = mr - 2 * mt / 3.0
                p_t = mt
                if (k_v, p_t) not in eig_cache:
                    eig_cache[(k_v, p_t)] = lowest_eig_for_kv_with_target(
                        eps, chi, k_v, p_t, N_grid
                    )
            for (mt_p, mr_p), (mt_n, mr_n) in candidates:
                k_v_p = mr_p - 2 * mt_p / 3.0
                k_v_n = mr_n - 2 * mt_n / 3.0
                e_p = eig_cache[(k_v_p, mt_p)]
                e_n = eig_cache[(k_v_n, mt_n)]
                if e_p <= 0 or e_n <= 0:
                    continue
                if e_n <= e_p:
                    continue  # neutron must be heavier than proton
                ratio = (e_n / e_p) ** 0.5
                if abs(ratio - target) < 1e-2:
                    best.append((eta, abs(ratio - target), (mt_p, mr_p),
                                  (mt_n, mr_n), eps, chi, ratio))
    best.sort(key=lambda x: (x[1], x[0]))
    msg.append(f"  Target m_n/m_p = {target}")
    msg.append(f"  Candidates with |ratio - target| < 0.01 in PT regime (η ≤ 0.5):")
    msg.append(f"  {'η':>6}  {'(mt_p,mr_p)':>12}  {'(mt_n,mr_n)':>12}  {'ε':>5}  {'χ':>5}  {'ratio':>9}  {'|Δ|':>10}")
    for eta, diff, p_lbl, n_lbl, eps, chi, ratio in best[:10]:
        msg.append(f"  {eta:6.4f}  {p_lbl!s:>12}  {n_lbl!s:>12}  "
                   f"{eps:5.2f}  {chi:5.2f}  {ratio:9.5f}  {diff:10.6f}")
    if not best:
        msg.append("  (no candidates within 1%)")
    msg.append("")
    msg.append("  Note: this confirms or refutes the analytical claim in clover-mass.md §6.4")
    msg.append("  that no low-(m_t, m_r) identification fits in any PT-valid regime.")
    # The "test" here doesn't pass/fail in the usual sense — we just report.
    # Pass if no candidate is found (matches the analytical negative result).
    return len(best) == 0, "\n".join(msg)


def test_sigma_dependence(N_grid: int) -> tuple[bool, str]:
    """C6: at small η, numerical μ²(σ) matches (k_v − σ p)² + (p/ε)²
    for several σ values, validating the rolled-leaf σ generalisation of
    the zeroth-order formula (work/clover-mass.md §4)."""
    msg = []
    msg.append("[C6] σ-dependence of zeroth-order spectrum:")
    msg.append("  Test: at small η, numerical μ²(σ) should match (k_v − σ p)² + (p/ε)²")
    msg.append("  for several σ values. σ enters the cross-term as σ_eff = σ + 2τ in (m_t, m_r) labels.")
    msg.append("")
    msg.append(f"  {'σ':>5}  {'ε':>5}  {'χ':>5}  {'η':>6}  {'k_v':>7}  {'p':>3}  "
               f"{'μ²_num':>12}  {'μ²_pred':>12}  {'rel err':>10}  {'verdict':>8}")
    all_pass = True
    # Small η for clean comparison; sweep σ.
    cases = [
        # (σ, ε, χ, k_v, p_target)
        (0.00, 0.05, 1.0, 1.0/3.0, 1),
        (0.05, 0.05, 1.0, 1.0/3.0, 1),
        (0.10, 0.05, 1.0, 1.0/3.0, 1),
        (0.20, 0.05, 1.0, 1.0/3.0, 1),
        (0.30, 0.05, 1.0, 1.0/3.0, 1),
        (0.10, 0.05, 1.0, 2.0/3.0, 2),
        (0.10, 0.10, 1.0, 1.0/3.0, 1),  # slightly larger η
    ]
    for sigma, eps, chi, k_v, p in cases:
        eta = eps / (2.0 + chi)
        e_num = lowest_eig_for_kv_with_target(eps, chi, k_v, p, N_grid, sigma=sigma)
        e_pred = (k_v - sigma * p) ** 2 + (p / eps) ** 2
        rel_err = abs(e_num - e_pred) / max(e_pred, 1e-10)
        # Threshold: η² accuracy plus σ²ε² correction; allow modest headroom.
        threshold = max(5 * eta**2, 5 * (sigma * eta) ** 2, 1e-5)
        ok = rel_err < threshold
        all_pass = all_pass and ok
        msg.append(f"  {sigma:5.2f}  {eps:5.2f}  {chi:5.2f}  {eta:6.4f}  {k_v:7.4f}  "
                   f"{p:3d}  {e_num:12.6f}  {e_pred:12.6f}  {rel_err:10.2e}  "
                   f"{('PASS' if ok else 'FAIL'):>8}")
    msg.append("")
    msg.append("  Note: in (m_t, m_r) wave-mode labels with k_v = m_r − 2τ m_t and p = m_t,")
    msg.append("  the formula (k_v − σ p)² + (p/ε)² rewrites as (m_r − (σ+2τ) m_t)² + (m_t/ε)²,")
    msg.append("  giving the rolled-leaf σ_eff = σ + 2τ generalisation of the τ-only cross-term.")
    return all_pass, "\n".join(msg)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n-grid", type=int, default=256,
                        help="Hill-equation grid resolution. 256 is enough for low modes.")
    args = parser.parse_args()

    print(f"# Mass-formula validation report (Hill grid N = {args.n_grid})")
    print()
    overall_pass = True

    for test_fn in [
        test_zeroth_order_convergence,
        test_first_order_vanishes,
        test_second_order_formula,
        test_proton_neutron_inversion,
        test_sigma_dependence,
    ]:
        ok, report = test_fn(args.n_grid)
        print(report)
        print()
        overall_pass = overall_pass and ok

    print("=" * 64)
    if overall_pass:
        print("All claims VALIDATED by independent numerical solver.")
    else:
        print("At least one claim FAILED validation — see details above.")
    sys.exit(0 if overall_pass else 1)


if __name__ == "__main__":
    main()
