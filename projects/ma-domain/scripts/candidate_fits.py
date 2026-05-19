"""
Per-candidate fit summary for the three current topology candidates in
work/candidates.md.

All dim labels are size-ordered: m1 is the smallest compact circumference
(hosting the heaviest mass scales), m_N is the largest. Pair notation:
Ma(i, j) for a single pair, Ma((i,j), ...) for a topology.

Dim-size hierarchy after the natural-scale e-refactor:
    m1 ≈ 0.007 fm    (b/t ring)
    m2 ≈ 0.7 fm      (electron-sector new dim)
    m3 ≈ 0.91 fm     (s/c ring)
    m4 ≈ 181 fm      (u/d ring)
    m5 ≈ 5740 fm     (quark wye hub)
    m6, m7, m8       (ν-region, ~cm scale; fit-determined)

All three candidates share the same quark wye:
    Ma((1, 5), (3, 5), (4, 5))   hub at m5 (largest of the quark-region dims)

Candidates B and C share the same electron delta:
    Ma((2, 4), (2, 5), (4, 5))
(natural scale placement: uses the lepton-scale m2 with the two largest
quark-region dims m4, m5, hosting τ, e, μ on the three pairs without
R53 fine-tuning)

Candidate C adds a neutrino delta on fresh dims (decoupled from the e-sector):
    Ma((6, 7), (6, 8), (7, 8))

Candidate A uses an electron path Ma((1, 3), (1, 2), (2, 5)) which is not
fit here (mixed-shape, requires separate analysis); and a single neutrino
pair Ma(6, 7) which is not viable under strict closure modes.

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
# Quark sector: wye/star with hub at m5, rings at m1, m3, m4
# Size-ordered: m1 (smallest) hosts the heaviest pair (t, b)
# (m2 is reserved for the electron-sector new dim)
# ===============================================================

def quark_wye_fit() -> dict:
    """
    Fit the 6 quarks on the wye topology Ma((1,5), (3,5), (4,5)).
    m5 is the common hub (plays tube in every pair, ~5740 fm).
    m1, m3, m4 are the rings; heaviest pair on smallest ring.

    Each pair hosts one generation: lighter quark at T(1, 2), heavier
    at T(1, 1) (per metric-charge §4 closure rule).
    """
    # Size-ordered: heaviest generation on smallest ring m1
    # (m2 is intentionally skipped — reserved for the electron-sector dim)
    gen_to_spoke = [
        ("b/t", 1),   # m1 (smallest, ~0.007 fm) hosts (t, b)
        ("s/c", 3),   # m3 (~0.91 fm) hosts (c, s)
        ("u/d", 4),   # m4 (~181 fm) hosts (d, u)
    ]
    hub_dim = 5

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
                    for s in (1, 3, 4)) * 10
    L_hub = max(L_hub_min, 5000.0)
    Ls = {hub_dim: L_hub}
    for s in (1, 3, 4):
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
# Electron sector: delta Ma((2, 4), (2, 5), (4, 5))  (candidates B and C)
# Hypothesis: 1 lepton per pair (no clover doublet on charged leptons)
# Mode: T(1, 2) per pair
# Natural-scale placement: uses m4 (181 fm, near electron Compton λ ~ 386 fm)
# and m5 (5740 fm, the quark hub), plus a new lepton-scale dim m2 (~0.7 fm)
# which sets the τ Compton wavelength.
# ===============================================================

def electron_delta_fit(L_fixed: dict, n_seeds: int = 20) -> dict:
    """
    Fit (e, μ, τ) on the delta Ma((2, 4), (2, 5), (4, 5)).
    L_fixed: dict of inherited L values, e.g. {4: 181, 5: 5740}
    Unknowns: L_2 (lepton-scale dim), σ for each pair, plus tube/ring per pair.

    Each pair hosts ONE charged lepton at T(1, 2).
    Try all 6 (lepton → pair) assignments and all 2^3 tube/ring choices.
    """
    pairs = [(2, 4), (2, 5), (4, 5)]
    leptons = list(LEPTON.keys())

    def mass(L_T: float, L_R: float, sigma_eff: float) -> float:
        delta = 2 - sigma_eff
        return COEFF * sqrt((1 / L_T) ** 2 + (delta / L_R) ** 2)

    def predict(x: np.ndarray, lepton_to_pair: list, tube_is_first: list) -> dict:
        """x = [log10 L_2, σ for each of 3 pairs]"""
        L_2 = 10 ** x[0]
        sigmas = {pairs[i]: x[1 + i] for i in range(3)}
        Ls = {2: L_2, 4: L_fixed[4], 5: L_fixed[5]}
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
                        "L_2": 10 ** res.x[0],
                        "sigma_eff": {pairs[i]: res.x[1 + i] for i in range(3)},
                        "predictions": pred,
                    }
    return best


# ===============================================================
# Electron sector — wye variant (wye-ladder topology)
# Ma((1, 6), (3, 6), (6, 7))  — hub at m6, spokes m1 (shared with quark
# wye), m3 (shared with quark wye), and m7 (new e-region dim).
# Hypothesis: 1 lepton per pair at T(1, 2); the same small dims m1 and
# m3 that play ring for the heaviest quarks (b/t, c/s) also play ring
# for the heaviest leptons (τ, μ).  m2 is unused in wye-ladder
# (was the lepton-scale dim in Candidate C; reserved/skipped here).
# ===============================================================

def electron_wye_fit(L_fixed: dict, n_seeds: int = 30) -> dict:
    """
    Fit (e, μ, τ) on the wye Ma((1, 6), (3, 6), (6, 7))  [wye-ladder].
    L_fixed: dict of inherited L values, e.g. {1: 0.007, 3: 0.91}
    Unknowns: L_6 (e-wye hub), L_7 (e-region dim), σ for each pair,
    plus tube/ring assignment per pair.

    Each pair hosts ONE charged lepton at T(1, 2).
    Try all 6 (lepton → pair) assignments and all 2^3 tube/ring choices.
    5 free continuous params vs 3 lepton masses → underdetermined.
    """
    pairs = [(1, 6), (3, 6), (6, 7)]
    leptons = list(LEPTON.keys())

    def mass(L_T: float, L_R: float, sigma_eff: float) -> float:
        delta = 2 - sigma_eff
        return COEFF * sqrt((1 / L_T) ** 2 + (delta / L_R) ** 2)

    def predict(x: np.ndarray, lepton_to_pair: list, tube_is_first: list) -> dict:
        """x = [log10 L_6, log10 L_7, σ for each of 3 pairs]"""
        L_6 = 10 ** x[0]
        L_7 = 10 ** x[1]
        sigmas = {pairs[i]: x[2 + i] for i in range(3)}
        Ls = {1: L_fixed[1], 3: L_fixed[3], 6: L_6, 7: L_7}
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
        try:
            pred = predict(x, lepton_to_pair, tube_is_first)
            return [log10(pred[lep] / LEPTON[lep]) if pred[lep] > 0 else 1e6
                    for lep in leptons]
        except (ValueError, ZeroDivisionError):
            return [1e6] * 3

    best = None
    for lepton_perm in permutations(leptons):
        lepton_to_pair = list(lepton_perm)
        for tube_combo in [(a, b, c) for a in (True, False)
                                       for b in (True, False)
                                       for c in (True, False)]:
            for seed in range(n_seeds):
                rng = np.random.default_rng(seed)
                x0 = [
                    rng.uniform(-3, 6),    # log10 L_6 (e-wye hub)
                    rng.uniform(-3, 6),    # log10 L_7 (e-region dim)
                    rng.uniform(0.5, 2.5),
                    rng.uniform(0.5, 2.5),
                    rng.uniform(0.5, 2.5),
                ]
                try:
                    res = least_squares(
                        residuals, x0,
                        args=(lepton_to_pair, list(tube_combo)),
                        bounds=([-5, -5, 0, 0, 0], [10, 10, 3, 3, 3]),
                        method="trf", max_nfev=2000,
                    )
                    pred = predict(res.x, lepton_to_pair, list(tube_combo))
                    max_err = max(abs(100 * (pred[lep] - LEPTON[lep]) / LEPTON[lep])
                                  for lep in leptons)
                    if best is None or max_err < best["max_err"]:
                        best = {
                            "max_err": max_err,
                            "lepton_to_pair_arrangement": list(zip(pairs, lepton_to_pair)),
                            "tube_is_first": list(tube_combo),
                            "L_6": 10 ** res.x[0],
                            "L_7": 10 ** res.x[1],
                            "sigma_eff": {pairs[i]: res.x[2 + i] for i in range(3)},
                            "predictions": pred,
                        }
                except Exception:
                    continue
    return best


# ===============================================================
# Neutrino sector
# ===============================================================

def neutrino_pair_fit_check(L_inherited: float = None) -> dict:
    """
    Candidates A and B: ν is a single pair on fresh dims (e.g. Ma(6, 7)).

    Under strict closure modes (T(1, 1) and T(1, 2) only), a single pair
    has at most 2 modes — can't host 3 ν mass eigenstates.

    Even ignoring that, the mass floor m ≥ 2π·ℏc/min(L_T, L_R) requires
    min(L_T, L_R) ≥ 4e10 fm ≈ 4 cm for m ≈ 30 meV.

    After the natural-scale e-refactor, the ν pair does NOT inherit L_5
    from the electron fit (L_5 ≈ 0.7 fm is way too small for ν).  Both ν
    dims are fresh free parameters.
    """
    min_L_required = COEFF / NEUTRINO["nu1"]  # ≈ 4 × 10¹⁰ fm
    return {
        "L_inherited": L_inherited,
        "min_L_required_for_nu1": min_L_required,
        "modes_per_pair": 2,
        "n_observed_nu_masses": 3,
        "modes_sufficient": False,
        "verdict": ("NOT VIABLE under strict closure: a single pair has at "
                   "most 2 modes at m_t=1, but 3 ν mass eigenstates are "
                   "observed.  Both ν dims are fresh; meV scale requires "
                   f"min(L_T, L_R) ≥ {min_L_required:.2g} fm. The B-candidate "
                   "rescue uses sign-flipped m_t modes — see candidates.md §4."),
    }


def neutrino_delta_fit() -> dict:
    """
    Candidate C: ν delta Ma((6, 7), (6, 8), (7, 8)) — on fresh dims,
    decoupled from the e-sector (the previous m5-shared design breaks
    after the natural-scale e-refactor).

    All three dim sizes L_6, L_7, L_8 are free parameters.  Fit
    (ν₁, ν₂, ν₃) under 1-mass-per-pair hypothesis at T(1, 2).
    """
    pairs = [(6, 7), (6, 8), (7, 8)]
    nu_list = ["nu1", "nu2", "nu3"]

    def mass(L_T: float, L_R: float, sigma_eff: float) -> float:
        delta = 2 - sigma_eff
        return COEFF * sqrt((1 / L_T) ** 2 + (delta / L_R) ** 2)

    def predict(x, nu_to_pair, tube_is_first):
        """x = [log10 L_6, log10 L_7, log10 L_8, σ for each of 3 pairs]"""
        L_6 = 10 ** x[0]
        L_7 = 10 ** x[1]
        L_8 = 10 ** x[2]
        sigmas = {pairs[i]: x[3 + i] for i in range(3)}
        Ls = {6: L_6, 7: L_7, 8: L_8}
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
                    rng.uniform(5, 15),
                    rng.uniform(1, 2), rng.uniform(1, 2), rng.uniform(1, 2),
                ]
                try:
                    res = least_squares(
                        residuals, x0,
                        args=(nu_to_pair, list(tube_combo)),
                        bounds=([-5, -5, -5, 0, 0, 0], [15, 15, 15, 3, 3, 3]),
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
                        "L_8": 10 ** res.x[2],
                        "sigma_eff": {pairs[i]: res.x[3 + i] for i in range(3)},
                        "predictions": pred,
                    }
    return best


# ===============================================================
# Per-candidate driver
# ===============================================================

def candidate_A():
    """Wye + 4-dim electron path + ν pair (on fresh dim m6/m7)."""
    quark = quark_wye_fit()
    return {
        "name": "Candidate A (wye + path)",
        "quark_topology": "Ma((1,5), (3,5), (4,5)) — wye, hub at m5",
        "electron_topology": "Ma((1,3), (1,2), (2,5)) — 4-dim path (m3—m1—m2—m5)",
        "neutrino_topology": "Ma(6, 7) — single pair (fresh dims)",
        "n_dims": 7,
        "quark": quark,
        "electron_note": ("4-dim path topology (m3—m1—m2—m5), not a clean shape. "
                          "e-sector fit not implemented here (mixed-shape topology "
                          "requires a separate analysis). Shares L_1, L_3, L_5 with "
                          "quarks via the pairs (1,3), (1,2)*, (2,5)*."),
        "neutrino": neutrino_pair_fit_check(),
    }


def candidate_B():
    """Wye + e delta + ν pair (on fresh dims, decoupled from e-sector)."""
    quark = quark_wye_fit()
    L_e_inherit = {4: quark["Ls"][4], 5: quark["Ls"][5]}
    electron = electron_delta_fit(L_e_inherit)
    nu_check = neutrino_pair_fit_check()
    return {
        "name": "Candidate B (wye + delta + ν pair, 7 dims)",
        "quark_topology": "Ma((1,5), (3,5), (4,5)) — wye, hub at m5",
        "electron_topology": "Ma((2,4), (2,5), (4,5)) — delta on m2, m4, m5",
        "neutrino_topology": "Ma(6, 7) — single pair (fresh dims, decoupled from e-sector)",
        "n_dims": 7,
        "quark": quark,
        "electron": electron,
        "neutrino": nu_check,
    }


def candidate_C():
    """Wye + e delta + ν delta (ν delta on fresh dims, decoupled)."""
    quark = quark_wye_fit()
    L_e_inherit = {4: quark["Ls"][4], 5: quark["Ls"][5]}
    electron = electron_delta_fit(L_e_inherit)
    neutrino = neutrino_delta_fit()
    return {
        "name": "Candidate C (wye + delta + delta, 8 dims)",
        "quark_topology": "Ma((1,5), (3,5), (4,5)) — wye, hub at m5",
        "electron_topology": "Ma((2,4), (2,5), (4,5)) — delta on m2, m4, m5",
        "neutrino_topology": "Ma((6,7), (6,8), (7,8)) — delta on m6, m7, m8 (fresh dims)",
        "n_dims": 8,
        "quark": quark,
        "electron": electron,
        "neutrino": neutrino,
    }


def candidate_W():
    """Wye-ladder: quark wye + electron wye (sharing rings m1, m3) + 1D ν on m8.

    The electron wye uses m1 (b/t quark ring) and m3 (c/s quark ring)
    as its own ring dims, plus a new hub m6 and a new e-region dim m7.
    The ν sector is a 1D shaped substrate on m8 (per neutrino-1D.md);
    not fit here.
    """
    quark = quark_wye_fit()
    L_e_inherit = {1: quark["Ls"][1], 3: quark["Ls"][3]}
    electron = electron_wye_fit(L_e_inherit)
    return {
        "name": "Wye-ladder (wye + wye + 1D ν, 7 dims)",
        "quark_topology": "Ma((1,5), (3,5), (4,5)) — wye, hub at m5",
        "electron_topology": "Ma((1,6), (3,6), (6,7)) — wye, hub at m6 (rings m1, m3 SHARED with quark wye)",
        "neutrino_topology": "1D shaped substrate on m8 (see neutrino-1D.md); not fit here",
        "n_dims": 7,  # m1, m3, m4, m5, m6, m7, m8 — m2 is unused
        "quark": quark,
        "electron": electron,
        "neutrino_note": ("1D substrate; band-structure fit requires a separate "
                          "neutrino_1d_fit.py per neutrino-1D.md. Not implemented "
                          "in this script."),
    }


def main():
    out_dir = Path(__file__).resolve().parents[1] / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "candidate_fits.txt"

    candidates = [candidate_A(), candidate_B(), candidate_C(), candidate_W()]
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
            if "L_2" in e:
                lines.append(f"  L_2 (new e-sector dim) = {e['L_2']:.4g} fm")
            if "L_6" in e:
                lines.append(f"  L_6 (e-wye hub) = {e['L_6']:.4g} fm,  "
                             f"L_7 (e-region dim) = {e['L_7']:.4g} fm")
            lines.append(f"  σ_eff per pair:")
            for pair, s in e['sigma_eff'].items():
                lines.append(f"    Ma{pair}: σ_eff = {s:.4f}")
            lines.append("")
        elif "electron_note" in c:
            lines.append(f"  ELECTRON FIT: {c['electron_note']}")
            lines.append("")
        # Neutrino
        if "neutrino" not in c and "neutrino_note" in c:
            lines.append(f"  NEUTRINO: {c['neutrino_note']}")
            lines.append("")
            lines.append("-" * 90)
            lines.append("")
            continue
        nu = c["neutrino"]
        if "max_err" in nu:
            lines.append(f"  NEUTRINO FIT: max |Δ%| = {nu['max_err']:.3f}%")
            for n in NEUTRINO:
                err = 100 * (nu['predictions'][n] - NEUTRINO[n]) / NEUTRINO[n]
                lines.append(f"    {n:4s} pred = {nu['predictions'][n]:>10.4g}  "
                             f"obs = {NEUTRINO[n]:>10.4g}  Δ% = {err:+.2f}%")
            if "L_6" in nu:
                lines.append(f"  L_6 = {nu['L_6']:.4g} fm,  L_7 = {nu['L_7']:.4g} fm,  L_8 = {nu['L_8']:.4g} fm")
        else:
            lines.append(f"  NEUTRINO check: {nu['verdict']}")
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
