"""
Relaxation 1 sweep on the (1,2)(1,3)(2,3) topology.

Goal: revisit the negative result from work/quark-search.md §1-§7 with TWO
relaxations:
  (1) Allow m_t=2 as the second-lowest closure mode per pair (rather than
      always (m_t=1, m_r=round(σ_eff)±1)).
  (2) Allow per-pair tube/ring assignment (per the updated architecture.md
      §3.1) — each pair independently picks which dim is tube and which
      is ring.

For each of (6 gen→pair perms) × (2³ mode-B choices) × (2³ tube/ring
choices) = 384 configurations, attempt a least-squares fit of (L_1, L_2,
L_3, σ_eff_{12}, σ_eff_{13}, σ_eff_{23}) to the 6 observed quark masses.
Report all configurations that fit to < 5% across all 6 quarks.

Outputs to outputs/quark_search_relaxation_1.txt
"""

from __future__ import annotations

from math import pi, sqrt, log
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

GENERATIONS = [("u", "d"), ("s", "c"), ("b", "t")]
PAIRS = [("(1,2)", (1, 2)), ("(1,3)", (1, 3)), ("(2,3)", (2, 3))]


def mode_mass(L_T: float, L_R: float, m_t: int, delta: float) -> float:
    """2D mode mass: m = 2π·ℏc·√((m_t/L_T)² + (δ/L_R)²)."""
    return COEFF * sqrt((m_t / L_T) ** 2 + (delta / L_R) ** 2)


def pair_modes(L_T: float, L_R: float, sigma_eff: float, mode_b: str):
    """Return (mode_A_mass, mode_B_mass) for a pair with given tube/ring
    sizes, σ_eff, and Mode-B choice ('mr-shift' or 'mt-2')."""
    # Mode A: m_t=1, m_r=round(σ_eff)
    mr_A = round(sigma_eff)
    delta_A = mr_A - sigma_eff
    m_A = mode_mass(L_T, L_R, 1, delta_A)
    # Mode B
    if mode_b == "mr-shift":
        # The m_r one step further (more detuned)
        if delta_A >= 0:
            mr_B = mr_A + 1
        else:
            mr_B = mr_A - 1
        delta_B = mr_B - sigma_eff
        m_B = mode_mass(L_T, L_R, 1, delta_B)
    else:  # "mt-2"
        mt_B = 2
        mr_B = round(2 * sigma_eff)
        delta_B = mr_B - 2 * sigma_eff
        m_B = mode_mass(L_T, L_R, mt_B, delta_B)
    return m_A, m_B


def predicted_masses(L: list, sigma_eff: list, gen_to_pair_idx: list,
                      mode_b_per_pair: list, tube_choice_per_pair: list) -> dict:
    """Predict the 6 quark masses given a parameter set and discrete choices.

    L: list [L_1, L_2, L_3] in fm
    sigma_eff: list [s_12, s_13, s_23]
    gen_to_pair_idx: list, the i-th gen (u/d, s/c, b/t) is on PAIRS[gen_to_pair_idx[i]]
    mode_b_per_pair: list of 'mr-shift' or 'mt-2' for each of 3 pairs
    tube_choice_per_pair: list of 'smaller' or 'larger' for each pair
    """
    results = {}
    for i, (q_light, q_heavy) in enumerate(GENERATIONS):
        pair_idx = gen_to_pair_idx[i]
        dim_i, dim_j = PAIRS[pair_idx][1]
        L_dim_i = L[dim_i - 1]
        L_dim_j = L[dim_j - 1]
        if tube_choice_per_pair[pair_idx] == "smaller":
            L_T = min(L_dim_i, L_dim_j)
            L_R = max(L_dim_i, L_dim_j)
        else:
            L_T = max(L_dim_i, L_dim_j)
            L_R = min(L_dim_i, L_dim_j)
        m_A, m_B = pair_modes(L_T, L_R, sigma_eff[pair_idx],
                               mode_b_per_pair[pair_idx])
        m_lighter = min(m_A, m_B)
        m_heavier = max(m_A, m_B)
        results[q_light] = m_lighter
        results[q_heavy] = m_heavier
    return results


def residuals(x, gen_to_pair_idx, mode_b_per_pair, tube_choice_per_pair):
    """Residuals in log mass."""
    L = [10 ** x[0], 10 ** x[1], 10 ** x[2]]  # L in fm via log10
    sigma_eff = [x[3], x[4], x[5]]
    pred = predicted_masses(L, sigma_eff, gen_to_pair_idx, mode_b_per_pair,
                             tube_choice_per_pair)
    out = []
    for q, m_obs in QUARK.items():
        if pred.get(q, 0) <= 0:
            out.append(1e6)
        else:
            out.append(log(pred[q] / m_obs))
    return out


def try_config(gen_to_pair_idx, mode_b_per_pair, tube_choice_per_pair,
                n_seeds: int = 6) -> dict:
    """Try multiple random seeds to find best fit for this config."""
    best = None
    for seed in range(n_seeds):
        rng = np.random.default_rng(seed)
        x0 = [
            rng.uniform(-5, 5),    # log10 L_1
            rng.uniform(-5, 5),    # log10 L_2
            rng.uniform(-5, 5),    # log10 L_3
            rng.uniform(0, 1),     # σ_eff_12
            rng.uniform(0, 1),     # σ_eff_13
            rng.uniform(0, 1),     # σ_eff_23
        ]
        try:
            res = least_squares(
                residuals, x0,
                args=(gen_to_pair_idx, mode_b_per_pair, tube_choice_per_pair),
                bounds=([-10, -10, -10, 0, 0, 0], [10, 10, 10, 1, 1, 1]),
                method="trf", max_nfev=2000,
            )
        except Exception:
            continue
        L = [10 ** res.x[i] for i in range(3)]
        sigma_eff = list(res.x[3:6])
        pred = predicted_masses(L, sigma_eff, gen_to_pair_idx,
                                 mode_b_per_pair, tube_choice_per_pair)
        max_err = max(abs(100 * (pred[q] - QUARK[q]) / QUARK[q])
                      for q in QUARK) if all(pred.get(q, 0) > 0 for q in QUARK) else 1e6
        if best is None or max_err < best["max_err"]:
            best = {
                "max_err": max_err,
                "L": L,
                "sigma_eff": sigma_eff,
                "predictions": pred,
            }
    return best


def main() -> None:
    out_dir = Path(__file__).resolve().parents[1] / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "quark_search_relaxation_1.txt"

    results = []
    n_configs = 0
    for gen_perm in permutations(range(3)):
        gen_to_pair_idx = list(gen_perm)
        for mb_combo in product(["mr-shift", "mt-2"], repeat=3):
            mode_b_per_pair = list(mb_combo)
            for tube_combo in product(["smaller", "larger"], repeat=3):
                tube_choice_per_pair = list(tube_combo)
                n_configs += 1
                fit = try_config(gen_to_pair_idx, mode_b_per_pair,
                                  tube_choice_per_pair)
                if fit is not None and fit["max_err"] < 200:
                    results.append({
                        "gen_to_pair_idx": gen_to_pair_idx,
                        "mode_b_per_pair": mode_b_per_pair,
                        "tube_choice_per_pair": tube_choice_per_pair,
                        **fit,
                    })

    results.sort(key=lambda r: r["max_err"])

    lines = []
    lines.append("Relaxation 1 sweep on (1,2)(1,3)(2,3) topology")
    lines.append("=" * 90)
    lines.append("")
    lines.append(f"Configurations tested: {n_configs}")
    lines.append(f"Configurations with max |Δ%| < 200%: {len(results)}")
    lines.append(f"Configurations with max |Δ%| < 50%:  "
                 f"{sum(1 for r in results if r['max_err'] < 50)}")
    lines.append(f"Configurations with max |Δ%| < 10%:  "
                 f"{sum(1 for r in results if r['max_err'] < 10)}")
    lines.append(f"Configurations with max |Δ%| <  5%:  "
                 f"{sum(1 for r in results if r['max_err'] < 5)}")
    lines.append(f"Configurations with max |Δ%| <  1%:  "
                 f"{sum(1 for r in results if r['max_err'] < 1)}")
    lines.append("")
    lines.append("Top 10 best fits:")
    lines.append("")
    for i, r in enumerate(results[:10]):
        gp = r["gen_to_pair_idx"]
        gen_assigns = [f"{GENERATIONS[g][0]}/{GENERATIONS[g][1]}→{PAIRS[gp[g]][0]}" for g in range(3)]
        lines.append(f"  #{i+1}: max |Δ%| = {r['max_err']:.3f}%")
        lines.append(f"    assignment: {', '.join(gen_assigns)}")
        lines.append(f"    mode-B: P12={r['mode_b_per_pair'][0]} P13={r['mode_b_per_pair'][1]} P23={r['mode_b_per_pair'][2]}")
        lines.append(f"    tube/ring: P12={r['tube_choice_per_pair'][0]} P13={r['tube_choice_per_pair'][1]} P23={r['tube_choice_per_pair'][2]}")
        lines.append(f"    L_1={r['L'][0]:.3g}fm L_2={r['L'][1]:.3g}fm L_3={r['L'][2]:.3g}fm")
        lines.append(f"    σ_eff: P12={r['sigma_eff'][0]:.3f} P13={r['sigma_eff'][1]:.3f} P23={r['sigma_eff'][2]:.3f}")
        lines.append(f"    predicted:  " + "  ".join(f"{q}={r['predictions'][q]:.3g}" for q in QUARK))
        lines.append(f"    observed:   " + "  ".join(f"{q}={QUARK[q]:.3g}" for q in QUARK))
        lines.append("")

    text = "\n".join(lines)
    print(text)
    with open(out_path, "w") as f:
        f.write(text + "\n")
    print(f"\nWrote: {out_path}")


if __name__ == "__main__":
    main()
