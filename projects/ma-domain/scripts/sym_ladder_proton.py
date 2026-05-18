"""
Proton-delta fit analysis for the sym-ladder topology Ma((1,2), (1,3), (2,3)).

Tests three increasingly elaborate mode-selection schemes against the 6
observed quark masses:

  Test A — SIMPLE 2D modes per pair. Each pair hosts one generation
           with lighter quark at T(1, 2) and heavier at T(1, 1).
           Per-pair tube/ring choice is free.
           48 configs (6 gen-perms × 2³ tube/ring combos).
           6 unknowns (L_1, L_2, L_3, σ_12, σ_13, σ_23) vs 6 masses.

  Test B — COMPOUND 3D modes for heavy quarks. u, d on Ma(2,3) simple
           modes; s, c, b, t on compound 3D modes (1, n_2, n_3) for
           (n_2, n_3) ∈ {1, 2}². Compound mass uses chained-shear form:
              δ_2 = n_2 - σ_12
              δ_3 = n_3 - σ_13 - σ_23 · n_2
           m_compound² = (2πℏc)² · [(1/L_1)² + (δ_2/L_2)² + (δ_3/L_3)²]
           48 configs (24 heavy-quark perms × 2 Ma(2,3) tube/ring).
           6 unknowns vs 6 masses (just-determined).

  Test C — ORPHAN modes on the upper legs.  Using the σ values from the
           best Test B fit, predict the masses of simple T(1, 1) and
           T(1, 2) modes that would exist on Ma(1,2) and Ma(1,3) ALONE
           (i.e., as 2D-planar modes on those pairs, without the m1
           winding of the compound mode).  Compare to observed
           particle masses to see if anything matches.

Closure rule (metric-charge ch. 4): valid modes are T(1, n) with n ≥ 1.
For compound modes, closure is read per-pair-projection (T(1, n_2) on
Ma(1, 2) is closure-valid for n_2 ≥ 1, etc).

Outputs to outputs/sym_ladder_proton.txt
"""

from __future__ import annotations

from math import pi, sqrt, log10
from itertools import permutations, product
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares


HBARC_MEV_FM = 197.3269804
COEFF = 2 * pi * HBARC_MEV_FM  # ≈ 1239.84 MeV·fm

QUARK = {
    "u": 2.16, "d": 4.67,
    "s": 93.0, "c": 1270.0,
    "b": 4180.0, "t": 173000.0,
}

# (lighter, heavier) per generation
GENS = [("u", "d"), ("s", "c"), ("b", "t")]
HEAVY = ["s", "c", "b", "t"]

# Selected reference particle masses for Test C comparison (MeV).
REFERENCE_PARTICLES = [
    ("e", 0.511),
    ("μ", 105.66),
    ("π⁰", 134.98),
    ("π±", 139.57),
    ("K", 493.7),
    ("η", 547.86),
    ("ρ", 775.26),
    ("ω", 782.65),
    ("φ", 1019.46),
    ("τ", 1776.86),
    ("D", 1869.7),
    ("J/ψ", 3096.9),
    ("Υ", 9460.3),
    ("W", 80377.0),
    ("Z", 91188.0),
    ("H", 125100.0),
]


def mass_pair_2d(L_tube: float, L_ring: float,
                 m_r: int, sigma_eff: float) -> float:
    """Standard 2D pair mass at mode T(1, m_r)."""
    delta = m_r - sigma_eff
    return COEFF * sqrt((1 / L_tube)**2 + (delta / L_ring)**2)


def mass_compound_3d(L_1: float, L_2: float, L_3: float,
                     n_2: int, n_3: int,
                     sigma_12: float, sigma_13: float,
                     sigma_23: float) -> float:
    """Compound 3D mode (m_t=1 on m1, n_2 on m2, n_3 on m3).

    Chained-shear form: σ_23 enters δ_3 through n_2.
        δ_2 = n_2 - σ_12
        δ_3 = n_3 - σ_13 - σ_23·n_2
    """
    delta_2 = n_2 - sigma_12
    delta_3 = n_3 - sigma_13 - sigma_23 * n_2
    return COEFF * sqrt(
        (1.0 / L_1) ** 2
        + (delta_2 / L_2) ** 2
        + (delta_3 / L_3) ** 2
    )


# ===================================================================
# Test A: Simple 2D modes per pair
# ===================================================================

def test_a_simple_2d(n_seeds: int = 30):
    pairs = [(1, 2), (1, 3), (2, 3)]
    results = []

    for gen_perm in permutations(GENS):
        for tube_combo in product([0, 1], repeat=3):
            def predict(params):
                L_1, L_2, L_3, s12, s13, s23 = params
                Ls = {1: L_1, 2: L_2, 3: L_3}
                sigmas = [s12, s13, s23]
                out = {}
                for k, (d_a, d_b) in enumerate(pairs):
                    if tube_combo[k] == 0:
                        L_T, L_R = Ls[d_a], Ls[d_b]
                    else:
                        L_T, L_R = Ls[d_b], Ls[d_a]
                    q_light, q_heavy = gen_perm[k]
                    out[q_light] = mass_pair_2d(L_T, L_R, 2, sigmas[k])
                    out[q_heavy] = mass_pair_2d(L_T, L_R, 1, sigmas[k])
                return out

            def residuals(params):
                try:
                    pred = predict(params)
                    return [log10(pred[q] / QUARK[q]) if pred[q] > 0 else 1e6
                            for q in QUARK]
                except (ValueError, ZeroDivisionError):
                    return [1e6] * 6

            best = None
            for seed in range(n_seeds):
                rng = np.random.default_rng(seed)
                x0 = [
                    10 ** rng.uniform(-3, 5),
                    10 ** rng.uniform(-3, 5),
                    10 ** rng.uniform(-3, 5),
                    rng.uniform(0.5, 2.5),
                    rng.uniform(0.5, 2.5),
                    rng.uniform(0.5, 2.5),
                ]
                try:
                    res = least_squares(
                        residuals, x0,
                        bounds=([1e-5, 1e-5, 1e-5, -5, -5, -5],
                                [1e9, 1e9, 1e9, 5, 5, 5]),
                        method="trf", max_nfev=2000,
                    )
                    pred = predict(res.x)
                    max_err = max(abs(100 * (pred[q] - QUARK[q]) / QUARK[q])
                                  for q in QUARK)
                    if best is None or max_err < best["max_err"]:
                        best = {
                            "max_err": max_err,
                            "params": res.x.tolist(),
                            "pred": pred,
                            "gen_perm": [list(g) for g in gen_perm],
                            "tube_combo": list(tube_combo),
                        }
                except Exception:
                    continue
            if best:
                results.append(best)
    results.sort(key=lambda r: r["max_err"])
    return results


# ===================================================================
# Test B: Compound 3D modes for heavy quarks
# ===================================================================

def test_b_compound(n_seeds: int = 30):
    compound_keys = list(product([1, 2], repeat=2))
    results = []

    for hq_perm in permutations(HEAVY):
        for ud_tube in [0, 1]:
            def predict(params):
                L_1, L_2, L_3, s12, s13, s23 = params
                pred = {}
                # u, d on Ma(2,3) simple modes
                if ud_tube == 0:
                    L_T_ud, L_R_ud = L_2, L_3
                else:
                    L_T_ud, L_R_ud = L_3, L_2
                pred["u"] = mass_pair_2d(L_T_ud, L_R_ud, 2, s23)
                pred["d"] = mass_pair_2d(L_T_ud, L_R_ud, 1, s23)
                # s, c, b, t on compound modes
                for i, (n_2, n_3) in enumerate(compound_keys):
                    q = hq_perm[i]
                    pred[q] = mass_compound_3d(
                        L_1, L_2, L_3, n_2, n_3, s12, s13, s23
                    )
                return pred

            def residuals(params):
                try:
                    pred = predict(params)
                    return [log10(pred[q] / QUARK[q]) if pred[q] > 0 else 1e6
                            for q in QUARK]
                except (ValueError, ZeroDivisionError):
                    return [1e6] * 6

            best = None
            for seed in range(n_seeds):
                rng = np.random.default_rng(seed)
                x0 = [
                    10 ** rng.uniform(-3, 6),
                    10 ** rng.uniform(-3, 6),
                    10 ** rng.uniform(-3, 6),
                    rng.uniform(0, 3),
                    rng.uniform(0, 3),
                    rng.uniform(-2, 2),
                ]
                try:
                    res = least_squares(
                        residuals, x0,
                        bounds=([1e-5, 1e-5, 1e-5, -5, -5, -5],
                                [1e9, 1e9, 1e9, 5, 5, 5]),
                        method="trf", max_nfev=3000,
                    )
                    pred = predict(res.x)
                    max_err = max(abs(100 * (pred[q] - QUARK[q]) / QUARK[q])
                                  for q in QUARK)
                    if best is None or max_err < best["max_err"]:
                        best = {
                            "max_err": max_err,
                            "params": res.x.tolist(),
                            "pred": pred,
                            "hq_perm": list(hq_perm),
                            "ud_tube": ud_tube,
                            "compound_keys": [list(k) for k in compound_keys],
                        }
                except Exception:
                    continue
            if best:
                results.append(best)
    results.sort(key=lambda r: r["max_err"])
    return results


# ===================================================================
# Test C: Orphan 2D modes on Ma(1,2), Ma(1,3) using best Test B fit
# ===================================================================

def test_c_orphan_modes(best_b_params):
    L_1, L_2, L_3, s12, s13, s23 = best_b_params
    orphans = []
    for pair_name, dims, sigma in [
        ("Ma(1,2)", (L_1, L_2), s12),
        ("Ma(1,3)", (L_1, L_3), s13),
    ]:
        L_a, L_b = dims
        for tube_label, (L_T, L_R) in [
            ("smaller-as-tube", (L_a, L_b)),
            ("larger-as-tube", (L_b, L_a)),
        ]:
            m_T11 = mass_pair_2d(L_T, L_R, 1, sigma)
            m_T12 = mass_pair_2d(L_T, L_R, 2, sigma)
            orphans.append({
                "pair": pair_name,
                "tube_label": tube_label,
                "L_T_fm": L_T,
                "L_R_fm": L_R,
                "T(1,1)_MeV": m_T11,
                "T(1,2)_MeV": m_T12,
            })
    return orphans


def find_nearest_particle(mass_MeV, max_log_diff: float = 0.5):
    """Find the reference particle nearest to mass_MeV (by log10 distance).
    Return (name, mass, log10_ratio) for the nearest if within max_log_diff.
    """
    best = None
    for name, ref_mass in REFERENCE_PARTICLES:
        if ref_mass <= 0 or mass_MeV <= 0:
            continue
        log_diff = abs(log10(mass_MeV / ref_mass))
        if log_diff < max_log_diff and (best is None or log_diff < best[2]):
            best = (name, ref_mass, log_diff)
    return best


# ===================================================================
# Main
# ===================================================================

def main():
    out_dir = Path(__file__).resolve().parents[1] / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "sym_ladder_proton.txt"

    lines = []
    lines.append("=" * 90)
    lines.append("Proton delta Ma((1,2), (1,3), (2,3)) — quark fit attempts")
    lines.append("=" * 90)
    lines.append("")

    # Test A
    lines.append("=" * 90)
    lines.append("TEST A — simple 2D modes per pair (one generation per leg)")
    lines.append("=" * 90)
    lines.append("")
    a_results = test_a_simple_2d()
    lines.append(f"Configurations tested: {len(a_results)}")
    if a_results:
        lines.append(f"Best max |Δ%|: {a_results[0]['max_err']:.3f}%")
    lines.append("")
    lines.append("Top 3 configurations:")
    lines.append("")
    for i, r in enumerate(a_results[:3], 1):
        L_1, L_2, L_3, s12, s13, s23 = r['params']
        pair_labels = ['Ma(1,2)', 'Ma(1,3)', 'Ma(2,3)']
        gen_map = ", ".join(
            f"{p}={g[0]}/{g[1]}" for p, g in zip(pair_labels, r['gen_perm'])
        )
        tube_map = ", ".join(
            f"{p}.tube=m{[(1,2),(1,3),(2,3)][k][r['tube_combo'][k]]}"
            for k, p in enumerate(pair_labels)
        )
        lines.append(f"#{i}  max |Δ%| = {r['max_err']:.3f}%")
        lines.append(f"    gen→pair: {gen_map}")
        lines.append(f"    tube/ring: {tube_map}")
        lines.append(f"    L_1 = {L_1:.4g} fm, L_2 = {L_2:.4g} fm, L_3 = {L_3:.4g} fm")
        lines.append(f"    σ_12 = {s12:+.4f}, σ_13 = {s13:+.4f}, σ_23 = {s23:+.4f}")
        for q in QUARK:
            err = 100 * (r['pred'][q] - QUARK[q]) / QUARK[q]
            lines.append(f"      {q}: pred={r['pred'][q]:>11.4g}  obs={QUARK[q]:>10.4g}  Δ%={err:+8.2f}")
        lines.append("")

    # Test B
    lines.append("=" * 90)
    lines.append("TEST B — compound 3D modes for s,c,b,t (u,d on Ma(2,3) simple)")
    lines.append("=" * 90)
    lines.append("")
    b_results = test_b_compound()
    lines.append(f"Configurations tested: {len(b_results)}")
    if b_results:
        lines.append(f"Best max |Δ%|: {b_results[0]['max_err']:.3f}%")
    lines.append("")
    lines.append("Top 5 configurations:")
    lines.append("")
    for i, r in enumerate(b_results[:5], 1):
        L_1, L_2, L_3, s12, s13, s23 = r['params']
        assign = ", ".join(
            f"(n_2={k[0]},n_3={k[1]})→{q}"
            for k, q in zip(r['compound_keys'], r['hq_perm'])
        )
        lines.append(f"#{i}  max |Δ%| = {r['max_err']:.3f}%")
        lines.append(f"    compound assignment: {assign}")
        lines.append(f"    Ma(2,3) tube = m{2 if r['ud_tube']==0 else 3}")
        lines.append(f"    L_1 = {L_1:.4g} fm, L_2 = {L_2:.4g} fm, L_3 = {L_3:.4g} fm")
        lines.append(f"    σ_12 = {s12:+.4f}, σ_13 = {s13:+.4f}, σ_23 = {s23:+.4f}")
        for q in QUARK:
            err = 100 * (r['pred'][q] - QUARK[q]) / QUARK[q]
            lines.append(f"      {q}: pred={r['pred'][q]:>11.4g}  obs={QUARK[q]:>10.4g}  Δ%={err:+8.2f}")
        lines.append("")

    # Test C
    lines.append("=" * 90)
    lines.append("TEST C — orphan 2D modes on Ma(1,2), Ma(1,3) using best Test B fit")
    lines.append("=" * 90)
    lines.append("")
    if b_results and b_results[0]["max_err"] < 5.0:
        c_results = test_c_orphan_modes(b_results[0]["params"])
        lines.append("Simple T(1,1) and T(1,2) modes on each upper-leg pair,")
        lines.append("using the σ values from the best Test B fit.  Closest reference")
        lines.append("particle (within 0.5 in log10 mass) is annotated.")
        lines.append("")
        for r in c_results:
            lines.append(f"  {r['pair']} ({r['tube_label']}):")
            lines.append(f"    L_T = {r['L_T_fm']:.4g} fm,  L_R = {r['L_R_fm']:.4g} fm")
            for mode_name, mass in [
                ("T(1,1)", r['T(1,1)_MeV']),
                ("T(1,2)", r['T(1,2)_MeV']),
            ]:
                nearest = find_nearest_particle(mass)
                annotation = (
                    f"  nearest: {nearest[0]} ({nearest[1]:.4g} MeV, log10 diff {nearest[2]:+.2f})"
                    if nearest else "  (no nearby reference particle)"
                )
                lines.append(f"    {mode_name}: {mass:>11.4g} MeV{annotation}")
            lines.append("")
    else:
        lines.append("Test B did not close to better than 5%; skipping orphan-mode analysis.")
        lines.append("")

    text = "\n".join(lines)
    print(text)
    with open(out_path, "w") as f:
        f.write(text + "\n")
    print(f"\nWrote: {out_path}")


if __name__ == "__main__":
    main()
