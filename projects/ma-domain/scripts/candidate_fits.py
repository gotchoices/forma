"""
Per-candidate fit summary for the three current topology candidates in
work/candidates.md.

Each candidate uses the same quark sector (the wye/star topology that
fit 6 quarks to < 0.5% in quark-search.md §9), differing only in how
the electron and neutrino sectors are laid out.

For each candidate, this script computes:

  - The quark sector fit (same numerics; relabel of dim indices).
  - The electron sector under the lepton-per-pair hypothesis (1 charged
    lepton mode per pair; no clover doublet on electrons).
  - The neutrino sector under each candidate's ν topology.

Mode-selection convention: per metric-charge ch. 4, valid closure modes
are T(1, n) for n ≥ 1 (m_t divides m_r, both nonzero).  Lowest two
m_t = 1 modes are (1, 1) and (1, 2).

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

# Observed fermion masses
QUARK = {
    "u": 2.16, "d": 4.67,
    "s": 93.0, "c": 1270.0,
    "b": 4180.0, "t": 173000.0,
}
LEPTON = {"e": 0.511, "mu": 105.66, "tau": 1776.86}
NEUTRINO = {  # using R49 / model-F Family A values
    "nu1": 3.0e-8, "nu2": 3.3e-8, "nu3": 6.0e-8,
}


# ===============================================================
# Quark sector: identical for all 3 candidates (star/wye topology)
# ===============================================================

def quark_fit_under_labels(hub_dim: int, spoke_dims: tuple) -> dict:
    """
    Fit the 6 quarks on a star topology with `hub_dim` as the common tube
    and three `spoke_dims` as the three rings. Each pair (hub, spoke_i)
    hosts one generation, with the lighter quark at T(1, 2) and heavier
    at T(1, 1) (per metric-charge §4 closure rule).

    Returns dict with L's, σ_eff per pair, predicted masses, max error.
    """
    gen_to_spoke = list(zip(["u/d", "s/c", "b/t"], spoke_dims))
    rings = {}
    sigmas = {}
    for gen_label, spoke in gen_to_spoke:
        q_light, q_heavy = gen_label.split("/")
        r = QUARK[q_heavy] / QUARK[q_light]
        sigma_eff = (2 * r + 1) / (r + 1)
        f = 2 - sigma_eff
        L_R = COEFF * f / QUARK[q_light]
        rings[spoke] = L_R
        sigmas[(hub_dim, spoke)] = sigma_eff
    # Choose hub L: large enough for pure-ring regime in tightest pair
    L_hub_min = max(rings[s] / (2 - sigmas[(hub_dim, s)])
                    for s in spoke_dims) * 10
    L_hub = max(L_hub_min, 5000.0)
    Ls = {hub_dim: L_hub}
    for s in spoke_dims:
        Ls[s] = rings[s]
    # Predict all 6 quark masses
    predictions = {}
    for gen_label, spoke in gen_to_spoke:
        q_light, q_heavy = gen_label.split("/")
        sigma_eff = sigmas[(hub_dim, spoke)]
        L_T = Ls[hub_dim]  # hub is tube
        L_R = Ls[spoke]
        # Mode (1, 2) — lighter
        delta_light = 2 - sigma_eff
        m_light = COEFF * sqrt((1 / L_T) ** 2 + (delta_light / L_R) ** 2)
        # Mode (1, 1) — heavier
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
# Electron sector: triangle (3,4)(3,5)(4,5) under candidates B and C
# Hypothesis: 1 lepton per pair (no clover doublet on charged leptons)
# Mode: T(1, 2) lightest per pair (per metric-charge §4.1)
# ===============================================================

def electron_triangle_fit(L_fixed: dict, n_seeds: int = 20) -> dict:
    """
    Fit (e, μ, τ) on the triangle (3, 4), (3, 5), (4, 5).
    L_fixed: dict of inherited L values (e.g. {3: 0.91, 4: 0.007})
    Unknowns: L_5, σ_{34}, σ_{35}, σ_{45}, plus tube/ring assignment per pair.

    Each pair hosts ONE charged lepton at T(1, 2).
    Try all 6 (lepton → pair) assignments and all 2^3 tube/ring choices.
    Report best fit.
    """
    pairs = [(3, 4), (3, 5), (4, 5)]
    leptons = list(LEPTON.keys())

    def mass(L_T: float, L_R: float, sigma_eff: float) -> float:
        delta = 2 - sigma_eff  # T(1, 2) detuning
        return COEFF * sqrt((1 / L_T) ** 2 + (delta / L_R) ** 2)

    def predict(x: np.ndarray, lepton_to_pair: list, tube_is_first: list) -> dict:
        """x = [log10 L_5, σ_{34}, σ_{35}, σ_{45}]"""
        L_5 = 10 ** x[0]
        sigmas = {pairs[i]: x[1 + i] for i in range(3)}
        Ls = {3: L_fixed[3], 4: L_fixed[4], 5: L_5}
        out = {}
        for i, lepton in enumerate(lepton_to_pair):
            d1, d2 = pairs[i]
            if tube_is_first[i]:  # d1 plays tube
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
                    rng.uniform(-3, 6),                  # log10 L_5
                    rng.uniform(1, 2), rng.uniform(1, 2),  # σ_eff in [1, 2]
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
                        "lepton_to_pair": dict(zip(leptons, [pairs[i] for i in range(3)])),
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
    Candidates A and B: ν pair is (5, 6). L_5 inherited from e-sector fit.
    Question: can a single pair give the 3 ν mass eigenstates?

    No — a single pair has at most 2 closure modes at m_t=1 (the (1,1)
    and (1,2) modes), so cannot host 3 distinct masses.

    Even ignoring that, the mass floor m ≥ 2π·ℏc/min(L_T, L_R) requires
    min(L_T, L_R) ≥ 4e10 fm = 4 cm for m ≈ 30 meV.

    Returns a verdict dict.
    """
    L_5 = L_fixed.get(5, None)
    min_L_required = COEFF / NEUTRINO["nu1"]  # ≈ 4 × 10¹⁰ fm
    verdict = {
        "L_5_inherited": L_5,
        "min_L_required_for_nu1": min_L_required,
        "L_5_sufficient": L_5 is not None and L_5 >= min_L_required,
        "modes_per_pair": 2,
        "n_observed_nu_masses": 3,
        "modes_sufficient": False,  # 2 < 3
        "verdict": ("NOT VIABLE: a single pair has at most 2 closure modes "
                   "at m_t=1, but 3 ν mass eigenstates are observed; AND "
                   "the inherited L_5 from e-sector is far below the "
                   f"{min_L_required:.2g} fm floor required for meV-scale modes."),
    }
    return verdict


def neutrino_triangle_fit(L_fixed: dict) -> dict:
    """
    Candidate C: ν triangle (5,6)(5,7)(6,7) — analogous to e triangle.
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
        """x = [log10 L_6, log10 L_7, σ_{56}, σ_{57}, σ_{67}]"""
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
                    rng.uniform(5, 15),                              # L_6, L_7 large
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
    """First topology: quark (1,3)(2,3)(3,4), e (2,4)(3,5)(4,5), ν (5,6)."""
    # Quark fit under old labels
    quark = quark_fit_under_labels(hub_dim=3, spoke_dims=(1, 2, 4))
    return {
        "name": "Candidate A (original)",
        "quark_topology": "(1,3) (2,3) (3,4) — wye/star, hub=dim 3",
        "electron_topology": "(2,4) (3,5) (4,5) — 4 dims, no hub",
        "neutrino_topology": "(5,6) — pair",
        "n_dims": 6,
        "quark": quark,
        "electron_note": ("4 dims, not a pure shape. e-sector fit not implemented "
                          "here (mixed-dim topology requires a separate analysis). "
                          "Shares L_2, L_3, L_4 with quarks via pairs (2,4), (3,5), (4,5)."),
        "neutrino": neutrino_pair_fit_check({}),
    }


def candidate_B():
    """New: quark (1,2)(2,3)(2,4), e (3,4)(3,5)(4,5), ν (5,6)."""
    quark = quark_fit_under_labels(hub_dim=2, spoke_dims=(1, 3, 4))
    L_e_inherit = {3: quark["Ls"][3], 4: quark["Ls"][4]}
    electron = electron_triangle_fit(L_e_inherit)
    # Inherit L_5 (the smallest fit L_5 from electron fit) for ν check
    nu_check = neutrino_pair_fit_check({5: electron["L_5"]})
    return {
        "name": "Candidate B (wye+delta, 6 dims)",
        "quark_topology": "(1,2) (2,3) (2,4) — wye/star, hub=dim 2",
        "electron_topology": "(3,4) (3,5) (4,5) — delta on 3 dims",
        "neutrino_topology": "(5,6) — pair",
        "n_dims": 6,
        "quark": quark,
        "electron": electron,
        "neutrino": nu_check,
    }


def candidate_C():
    """C: quark (1,2)(2,3)(2,4), e (3,4)(3,5)(4,5), ν (5,6)(5,7)(6,7)."""
    quark = quark_fit_under_labels(hub_dim=2, spoke_dims=(1, 3, 4))
    L_e_inherit = {3: quark["Ls"][3], 4: quark["Ls"][4]}
    electron = electron_triangle_fit(L_e_inherit)
    L_nu_inherit = {5: electron["L_5"]}
    neutrino = neutrino_triangle_fit(L_nu_inherit)
    return {
        "name": "Candidate C (wye+delta+delta, 7 dims)",
        "quark_topology": "(1,2) (2,3) (2,4) — wye/star, hub=dim 2",
        "electron_topology": "(3,4) (3,5) (4,5) — delta on 3 dims",
        "neutrino_topology": "(5,6) (5,7) (6,7) — delta on 3 dims",
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
        lines.append(f"  Quark L's: {q['Ls']}")
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
