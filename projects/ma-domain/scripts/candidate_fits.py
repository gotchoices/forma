"""
Per-candidate fit summary for the three current topology candidates in
work/candidates.md.

All dim labels are size-ordered: m1 is the smallest compact circumference
(hosting the heaviest mass scales), m_N is the largest. Pair notation:
Ma(i, j) for a single pair, Ma((i,j), ...) for a topology.

All three candidates share the same quark wye:
    Ma((1, 4), (2, 4), (3, 4))   hub at m4 (largest, common tube)

Candidates B and C share the same electron delta:
    Ma((1, 2), (1, 5), (2, 5))

Candidate C adds a neutrino delta:
    Ma((5, 6), (5, 7), (6, 7))

Candidate A uses an electron path Ma((1, 2), (1, 5), (4, 5)) which is not
fit here (mixed-shape, requires separate analysis); and a single neutrino
pair Ma(5, 6) which is not viable under strict closure modes.

For each candidate, this script computes:

  - The quark sector fit (identical math; m4 hub + m1, m2, m3 rings).
  - The electron sector under the lepton-per-pair hypothesis (1 charged
    lepton mode T(1, 2) per pair; no clover doublet on electrons).
  - The neutrino sector under each candidate's ν topology.

Mode-selection convention: per metric-charge ch. 4, valid closure modes
are T(1, n) for n ≥ 1 (m_t divides m_r, both nonzero).  Lowest two
m_t = 1 modes are T(1, 1) and T(1, 2).

Outputs to outputs/candidate_fits.txt.
"""

from __future__ import annotations

from math import pi, sqrt, log10
from itertools import permutations
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares


HBARC_MEV_FM = 197.3269804
COEFF = 2 * pi * HBARC_MEV_FM  # ≈ 1239.84

# Observed fermion masses (MeV)
QUARK = {
    "u": 2.16, "d": 4.67,
    "s": 93.0, "c": 1270.0,
    "b": 4180.0, "t": 173000.0,
}
LEPTON = {"e": 0.511, "mu": 105.66, "tau": 1776.86}
NEUTRINO = {  # R49 / model-F Family A values
    "nu1": 3.0e-8, "nu2": 3.3e-8, "nu3": 6.0e-8,
}


# ===============================================================
# Quark sector: wye/star with hub at m4, rings at m1, m2, m3
# Size-ordered: m1 (smallest) hosts the heaviest pair (t, b)
# ===============================================================

def quark_wye_fit() -> dict:
    """
    Fit the 6 quarks on the wye topology Ma((1,4), (2,4), (3,4)).
    m4 is the common hub (plays tube in every pair, ~5740 fm).
    m1, m2, m3 are the rings; heaviest pair on smallest ring.

    Each pair hosts one generation: lighter quark at T(1, 2), heavier
    at T(1, 1) (per metric-charge §4 closure rule).
    """
    # Size-ordered: heaviest generation on smallest ring m1
    gen_to_spoke = [
        ("b/t", 1),   # m1 (smallest, ~0.007 fm) hosts (t, b)
        ("s/c", 2),   # m2 (~0.91 fm) hosts (c, s)
        ("u/d", 3),   # m3 (~181 fm) hosts (d, u)
    ]
    hub_dim = 4

    rings = {}
    sigmas = {}
    for gen_label, spoke in gen_to_spoke:
        q_light, q_heavy = gen_label.split("/")
        r = QUARK[q_heavy] / QUARK[q_light]
        sigma_eff = (2 * r + 1) / (r + 1)
        f = 2 - sigma_eff
        L_R = COEFF * f / QUARK[q_light]
        rings[spoke] = L_R
        sigmas[(spoke, hub_dim)] = sigma_eff

    # Hub L: large enough for pure-ring regime in tightest pair
    L_hub_min = max(rings[s] / (2 - sigmas[(s, hub_dim)])
                    for s in (1, 2, 3)) * 10
    L_hub = max(L_hub_min, 5000.0)
    Ls = {hub_dim: L_hub}
    for s in (1, 2, 3):
        Ls[s] = rings[s]

    predictions = {}
    for gen_label, spoke in gen_to_spoke:
        q_light, q_heavy = gen_label.split("/")
        sigma_eff = sigmas[(spoke, hub_dim)]
        L_T = Ls[hub_dim]
        L_R = Ls[spoke]
        # Mode T(1, 2) — lighter
        delta_light = 2 - sigma_eff
        m_light = COEFF * sqrt((1 / L_T) ** 2 + (delta_light / L_R) ** 2)
        # Mode T(1, 1) — heavier
        delta_heavy = 1 - sigma_eff
        m_heavy = COEFF * sqrt((1 / L_T) ** 2 + (delta_heavy / L_R) ** 2)
        predictions[q_light] = m_light
        predictions[q_heavy] = m_heavy

    max_err = max(abs(100 * (predictions[q] - QUARK[q]) / QUARK[q])
                  for q in QUARK)
    return {
        "Ls": Ls, "sigmas": sigmas, "predictions": predictions,
        "max_err": max_err,
    }


# ===============================================================
# Electron sector: delta Ma((1, 2), (1, 5), (2, 5))  (candidates B and C)
# Hypothesis: 1 lepton per pair (no clover doublet on charged leptons)
# Mode: T(1, 2) per pair
# ===============================================================

def electron_delta_fit(L_fixed: dict, n_seeds: int = 20) -> dict:
    """
    Fit (e, μ, τ) on the delta Ma((1, 2), (1, 5), (2, 5)).
    L_fixed: dict of inherited L values, e.g. {1: 0.007, 2: 0.91}
    Unknowns: L_5, σ for each pair, plus tube/ring assignment per pair.

    Each pair hosts ONE charged lepton at T(1, 2).
    Try all 6 (lepton → pair) assignments and all 2^3 tube/ring choices.
    """
    pairs = [(1, 2), (1, 5), (2, 5)]
    leptons = list(LEPTON.keys())

    def mass(L_T: float, L_R: float, sigma_eff: float) -> float:
        delta = 2 - sigma_eff
        return COEFF * sqrt((1 / L_T) ** 2 + (delta / L_R) ** 2)

    def predict(x: np.ndarray, lepton_to_pair: list, tube_is_first: list) -> dict:
        """x = [log10 L_5, σ for each of 3 pairs]"""
        L_5 = 10 ** x[0]
        sigmas = {pairs[i]: x[1 + i] for i in range(3)}
        Ls = {1: L_fixed[1], 2: L_fixed[2], 5: L_5}
        out = {}
        for i, lepton in enumerate(lepton_to_pair):
            d1, d2 = pairs[i]
            if tube_is_first[i]:
                L_T, L_R = Ls[d1], Ls[d2]
            else:
                L_T, L_R = Ls[d2], Ls[d1]
            out[lepton] = mass(L_T, L_R, sigmas[pairs[i]])
        return out

    def residuals(x, lepton_to_pair, tube_is_first):
        pred = predict(x, lepton_to_pair, tube_is_first)
        return [log10(pred[lep] / LEPTON[lep]) if pred[lep] > 0 else 1e6
                for lep in leptons]

    best = None
    for lepton_perm in permutations(leptons):
        lepton_to_pair = list(lepton_perm)
        for tube_combo in [(a, b, c) for a in (True, False)
                                       for b in (True, False)
                                       for c in (True, False)]:
            for seed in range(n_seeds):
                rng = np.random.default_rng(seed)
                x0 = [
                    rng.uniform(-3, 6),
                    rng.uniform(1, 2), rng.uniform(1, 2),
                    rng.uniform(1, 2),
                ]
                try:
                    res = least_squares(
                        residuals, x0,
                        args=(lepton_to_pair, list(tube_combo)),
                        bounds=([-5, 0, 0, 0], [10, 3, 3, 3]),
                        method="trf", max_nfev=1000,
                    )
                except Exception:
                    continue
                pred = predict(res.x, lepton_to_pair, list(tube_combo))
                max_err = max(abs(100 * (pred[lep] - LEPTON[lep]) / LEPTON[lep])
                              for lep in leptons)
                if best is None or max_err < best["max_err"]:
                    best = {
                        "max_err": max_err,
                        "lepton_to_pair_arrangement": list(zip(pairs, lepton_to_pair)),
                        "tube_is_first": list(tube_combo),
                        "L_5": 10 ** res.x[0],
                        "sigma_eff": {pairs[i]: res.x[1 + i] for i in range(3)},
                        "predictions": pred,
                    }
    return best


# ===============================================================
# Neutrino sector
# ===============================================================

def neutrino_pair_fit_check(L_fixed: dict) -> dict:
    """
    Candidates A and B: ν is a single pair Ma(5, 6). L_5 inherited from
    e-sector fit.

    Under strict closure modes (T(1, 1) and T(1, 2) only), a single pair
    has at most 2 modes — can't host 3 ν mass eigenstates.

    Even ignoring that, the mass floor m ≥ 2π·ℏc/min(L_T, L_R) requires
    min(L_T, L_R) ≥ 4e10 fm ≈ 4 cm for m ≈ 30 meV.
    """
    L_5 = L_fixed.get(5, None)
    min_L_required = COEFF / NEUTRINO["nu1"]  # ≈ 4 × 10¹⁰ fm
    verdict = {
        "L_5_inherited": L_5,
        "min_L_required_for_nu1": min_L_required,
        "L_5_sufficient": L_5 is not None and L_5 >= min_L_required,
        "modes_per_pair": 2,
        "n_observed_nu_masses": 3,
        "modes_sufficient": False,
        "verdict": ("NOT VIABLE: a single pair Ma(5, 6) has at most 2 closure "
                   "modes at m_t=1, but 3 ν mass eigenstates are observed; "
                   "AND the inherited L_5 from e-sector is far below the "
                   f"{min_L_required:.2g} fm floor required for meV-scale modes."),
    }
    return verdict


def neutrino_delta_fit(L_fixed: dict) -> dict:
    """
    Candidate C: ν delta Ma((5, 6), (5, 7), (6, 7)) — analogous to e delta.
    L_5 inherited from e-fit. L_6, L_7 free.

    Fit (ν₁, ν₂, ν₃) under 1-lepton-per-pair hypothesis (no doublet).
    """
    L_5 = L_fixed[5]
    pairs = [(5, 6), (5, 7), (6, 7)]
    nu_list = ["nu1", "nu2", "nu3"]

    def mass(L_T: float, L_R: float, sigma_eff: float) -> float:
        delta = 2 - sigma_eff
        return COEFF * sqrt((1 / L_T) ** 2 + (delta / L_R) ** 2)

    def predict(x, nu_to_pair, tube_is_first):
        """x = [log10 L_6, log10 L_7, σ for each of 3 pairs]"""
        L_6 = 10 ** x[0]
        L_7 = 10 ** x[1]
        sigmas = {pairs[i]: x[2 + i] for i in range(3)}
        Ls = {5: L_5, 6: L_6, 7: L_7}
        out = {}
        for i, nu in enumerate(nu_to_pair):
            d1, d2 = pairs[i]
            if tube_is_first[i]:
                L_T, L_R = Ls[d1], Ls[d2]
            else:
                L_T, L_R = Ls[d2], Ls[d1]
            out[nu] = mass(L_T, L_R, sigmas[pairs[i]])
        return out

    def residuals(x, nu_to_pair, tube_is_first):
        pred = predict(x, nu_to_pair, tube_is_first)
        return [log10(pred[n] / NEUTRINO[n]) if pred[n] > 0 else 1e6
                for n in nu_list]

    best = None
    for nu_perm in permutations(nu_list):
        nu_to_pair = list(nu_perm)
        for tube_combo in [(a, b, c) for a in (True, False)
                                       for b in (True, False)
                                       for c in (True, False)]:
            for seed in range(15):
                rng = np.random.default_rng(seed)
                x0 = [
                    rng.uniform(5, 15),
                    rng.uniform(5, 15),
                    rng.uniform(1, 2), rng.uniform(1, 2), rng.uniform(1, 2),
                ]
                try:
                    res = least_squares(
                        residuals, x0,
                        args=(nu_to_pair, list(tube_combo)),
                        bounds=([-5, -5, 0, 0, 0], [15, 15, 3, 3, 3]),
                        method="trf", max_nfev=1500,
                    )
                except Exception:
                    continue
                pred = predict(res.x, nu_to_pair, list(tube_combo))
                max_err = max(abs(100 * (pred[n] - NEUTRINO[n]) / NEUTRINO[n])
                              for n in nu_list)
                if best is None or max_err < best["max_err"]:
                    best = {
                        "max_err": max_err,
                        "nu_arrangement": list(zip(pairs, nu_to_pair)),
                        "tube_is_first": list(tube_combo),
                        "L_6": 10 ** res.x[0],
                        "L_7": 10 ** res.x[1],
                        "sigma_eff": {pairs[i]: res.x[2 + i] for i in range(3)},
                        "predictions": pred,
                    }
    return best


# ===============================================================
# Per-candidate driver
# ===============================================================

def candidate_A():
    """Wye + 4-dim electron path + ν pair."""
    quark = quark_wye_fit()
    return {
        "name": "Candidate A (wye + path)",
        "quark_topology": "Ma((1,4), (2,4), (3,4)) — wye, hub at m4",
        "electron_topology": "Ma((1,2), (1,5), (4,5)) — 4-dim path",
        "neutrino_topology": "Ma(5, 6) — single pair",
        "n_dims": 6,
        "quark": quark,
        "electron_note": ("4-dim path topology (m2—m1—m5—m4), not a clean shape. "
                          "e-sector fit not implemented here (mixed-shape topology "
                          "requires a separate analysis). Shares L_1, L_2, L_4 with "
                          "quarks via the pairs (1,2), (1,5)*, (4,5)*."),
        "neutrino": neutrino_pair_fit_check({}),
    }


def candidate_B():
    """Wye + e delta + ν pair."""
    quark = quark_wye_fit()
    L_e_inherit = {1: quark["Ls"][1], 2: quark["Ls"][2]}
    electron = electron_delta_fit(L_e_inherit)
    nu_check = neutrino_pair_fit_check({5: electron["L_5"]})
    return {
        "name": "Candidate B (wye + delta, 6 dims)",
        "quark_topology": "Ma((1,4), (2,4), (3,4)) — wye, hub at m4",
        "electron_topology": "Ma((1,2), (1,5), (2,5)) — delta on m1, m2, m5",
        "neutrino_topology": "Ma(5, 6) — single pair",
        "n_dims": 6,
        "quark": quark,
        "electron": electron,
        "neutrino": nu_check,
    }


def candidate_C():
    """Wye + e delta + ν delta."""
    quark = quark_wye_fit()
    L_e_inherit = {1: quark["Ls"][1], 2: quark["Ls"][2]}
    electron = electron_delta_fit(L_e_inherit)
    L_nu_inherit = {5: electron["L_5"]}
    neutrino = neutrino_delta_fit(L_nu_inherit)
    return {
        "name": "Candidate C (wye + delta + delta, 7 dims)",
        "quark_topology": "Ma((1,4), (2,4), (3,4)) — wye, hub at m4",
        "electron_topology": "Ma((1,2), (1,5), (2,5)) — delta on m1, m2, m5",
        "neutrino_topology": "Ma((5,6), (5,7), (6,7)) — delta on m5, m6, m7",
        "n_dims": 7,
        "quark": quark,
        "electron": electron,
        "neutrino": neutrino,
    }


def main():
    out_dir = Path(__file__).resolve().parents[1] / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "candidate_fits.txt"

    candidates = [candidate_A(), candidate_B(), candidate_C()]
    lines = []
    lines.append("=" * 90)
    lines.append("ma-domain candidate fits")
    lines.append("(dim labels m1..m_N size-ordered; m1 smallest, m_N largest)")
    lines.append("=" * 90)
    lines.append("")
    for c in candidates:
        lines.append(f"### {c['name']}  ({c['n_dims']} dims)")
        lines.append(f"  Quark    topology: {c['quark_topology']}")
        lines.append(f"  Electron topology: {c['electron_topology']}")
        lines.append(f"  Neutrino topology: {c['neutrino_topology']}")
        lines.append("")
        # Quark fit
        q = c["quark"]
        lines.append(f"  QUARK FIT: max |Δ%| = {q['max_err']:.3f}%  ({len(QUARK)} quarks)")
        for q_name in QUARK:
            err = 100 * (q['predictions'][q_name] - QUARK[q_name]) / QUARK[q_name]
            lines.append(f"    {q_name:3s} pred = {q['predictions'][q_name]:>10.4g}  "
                         f"obs = {QUARK[q_name]:>10.4g}  Δ% = {err:+.2f}%")
        # Print L's in size order (m1 smallest)
        L_items = sorted(q['Ls'].items())
        lines.append(f"  Quark L's (size-ordered):")
        for k, v in L_items:
            lines.append(f"    L_{k} = {v:.4g} fm")
        lines.append("")
        # Electron
        if "electron" in c and c.get("electron"):
            e = c["electron"]
            lines.append(f"  ELECTRON FIT (1 mode per pair, T(1,2)): "
                         f"max |Δ%| = {e['max_err']:.3f}%")
            for lep in LEPTON:
                err = 100 * (e['predictions'][lep] - LEPTON[lep]) / LEPTON[lep]
                lines.append(f"    {lep:4s} pred = {e['predictions'][lep]:>10.4g}  "
                             f"obs = {LEPTON[lep]:>10.4g}  Δ% = {err:+.2f}%")
            lines.append(f"  Electron lepton→pair: {e['lepton_to_pair_arrangement']}")
            lines.append(f"  L_5 = {e['L_5']:.4g} fm")
            lines.append("")
        elif "electron_note" in c:
            lines.append(f"  ELECTRON FIT: {c['electron_note']}")
            lines.append("")
        # Neutrino
        nu = c["neutrino"]
        if "max_err" in nu:
            lines.append(f"  NEUTRINO FIT: max |Δ%| = {nu['max_err']:.3f}%")
            for n in NEUTRINO:
                err = 100 * (nu['predictions'][n] - NEUTRINO[n]) / NEUTRINO[n]
                lines.append(f"    {n:4s} pred = {nu['predictions'][n]:>10.4g}  "
                             f"obs = {NEUTRINO[n]:>10.4g}  Δ% = {err:+.2f}%")
            if "L_6" in nu:
                lines.append(f"  L_6 = {nu['L_6']:.4g} fm,  L_7 = {nu['L_7']:.4g} fm")
        else:
            lines.append(f"  NEUTRINO check: {nu['verdict']}")
            lines.append(f"    L_5 inherited from e-fit: "
                         f"{nu.get('L_5_inherited', 'n/a')} fm")
            lines.append(f"    L floor required for m_ν₁ = 30 meV: "
                         f"{nu['min_L_required_for_nu1']:.2g} fm")
        lines.append("")
        lines.append("-" * 90)
        lines.append("")

    text = "\n".join(lines)
    print(text)
    with open(out_path, "w") as f:
        f.write(text + "\n")
    print(f"Wrote: {out_path}")


if __name__ == "__main__":
    main()
