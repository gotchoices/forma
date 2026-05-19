#!/usr/bin/env python3
"""
cand_solver.py — general topology-candidate solver for the ma-domain project.

Reads a candidate spec (JSON) describing a set of compact dimensions and the
2D sheets (dim-pairs) built on them, then fits the dimension sizes and the
per-sheet shear sigma_eff so the hosted particle masses match observation.
Replaces the hard-coded per-candidate driver candidate_fits.py and the
single-topology script quark_search_wye.py.

For each candidate it reports:
  * R1 compliance — at most one sheet per dim-pair (see candidates.md R1)
  * degrees of freedom — free parameters minus mass constraints
  * whether a compliant fit exists, and the best fit error
  * how many discrete (particle->sheet, tube/ring) assignments fit
  * for the continuous parameters: which are PINNED to a value and which
    are FREE over a range (the solution manifold)

Physics model (uniform across all sheets):
  A sheet is a dim-pair Ma(i, j). One dim is the tube (L_T), the other the
  ring (L_R) — a per-sheet binary choice. A closure mode T(m_t, m_r) has mass
        m = COEFF * sqrt( (m_t / L_T)^2 + (delta / L_R)^2 ),
        delta = m_r - sigma_eff * m_t,   COEFF = 2*pi*hbar*c.
  m_t = 1 throughout.
  - A quark sheet hosts one generation: lighter quark at T(1, 2), heavier at
    T(1, 1)  -> 2 mass constraints.
  - An electron / neutrino sheet hosts one particle at T(1, 2) -> 1 constraint.

Usage:
    python cand_solver.py <spec.json> [options]
    python cand_solver.py --all [<spec-dir>] [options]

Options:
    --seeds N        random restarts per discrete combo, mapping phase (default 60)
    --scan-seeds N   random restarts per discrete combo, scan phase (default 3)
    --threshold PCT  max |Delta%| for a fit to count as compliant (default 1.0)
    --out PATH       output report path (default outputs/cand_<name>.txt)

Spec format (JSON):
    {
      "name": "QY-ED",
      "note": "free-text description",
      "dims": ["m1", "m2", "m3", "m4", "m5"],
      "sheets": [
        {"pair": ["m1", "m5"], "sector": "quark"},
        ...
      ]
    }
  sector is one of: "quark" (hosts a generation, 2 quarks), "electron" (one
  charged lepton), "neutrino" (one mass eigenstate). Each sector present must
  have exactly 3 sheets (3 generations / 3 leptons / 3 nu mass eigenstates).
"""

from __future__ import annotations

import argparse
import json
import sys
from itertools import permutations, product
from math import pi, sqrt, log10
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares


HBARC_MEV_FM = 197.3269804
COEFF = 2 * pi * HBARC_MEV_FM  # ~= 1239.84 MeV*fm

# Observed masses (MeV).
QUARK = {"u": 2.16, "d": 4.67, "s": 93.0, "c": 1270.0, "b": 4180.0, "t": 173000.0}
LEPTON = {"e": 0.511, "mu": 105.66, "tau": 1776.86}
NEUTRINO = {"nu1": 3.0e-8, "nu2": 3.3e-8, "nu3": 6.0e-8}  # R49 / model-F Family A

# Quark generations as (lighter, heavier) — lighter goes to T(1,2), heavier T(1,1).
QUARK_GENS = [("u", "d"), ("s", "c"), ("b", "t")]

# Per-sector item lists. A quark sheet hosts a generation tuple; an electron /
# neutrino sheet hosts a single particle name.
SECTOR_ITEMS = {
    "quark": QUARK_GENS,
    "electron": list(LEPTON.keys()),
    "neutrino": list(NEUTRINO.keys()),
}

# log10(L/fm) search/seed bounds and sigma_eff bounds.
LOG_L_LO, LOG_L_HI = -5.0, 16.0
SIGMA_LO, SIGMA_HI = 0.0, 3.0


# ---------------------------------------------------------------------------
# Spec loading and validation
# ---------------------------------------------------------------------------

class Spec:
    """A parsed, validated candidate spec."""

    def __init__(self, raw: dict, source: str):
        self.source = source
        self.name = raw.get("name") or Path(source).stem
        self.note = raw.get("note", "")
        self.dims = list(raw["dims"])
        self.sheets = []
        for sh in raw["sheets"]:
            pair = tuple(sh["pair"])
            sector = sh["sector"]
            if len(pair) != 2:
                raise ValueError(f"sheet pair must have 2 dims: {sh}")
            for d in pair:
                if d not in self.dims:
                    raise ValueError(f"sheet uses undeclared dim '{d}': {sh}")
            if sector not in SECTOR_ITEMS:
                raise ValueError(
                    f"unknown sector '{sector}' (expected one of "
                    f"{sorted(SECTOR_ITEMS)})")
            self.sheets.append({"pair": pair, "sector": sector})
        # Each present sector must have exactly 3 sheets.
        for sector in self.sectors():
            n = sum(1 for s in self.sheets if s["sector"] == sector)
            if n != 3:
                raise ValueError(
                    f"sector '{sector}' has {n} sheets; the one-particle-per-"
                    f"sheet model needs exactly 3 (3 generations / 3 leptons / "
                    f"3 nu). Multi-mode-per-pair configs (NS, NC) are not "
                    f"supported by this solver.")

    def sectors(self) -> list:
        seen = []
        for s in self.sheets:
            if s["sector"] not in seen:
                seen.append(s["sector"])
        return seen


def load_spec(path: str) -> Spec:
    with open(path) as fh:
        raw = json.load(fh)
    return Spec(raw, path)


# ---------------------------------------------------------------------------
# R1 — one sheet per dim-pair
# ---------------------------------------------------------------------------

def check_r1(spec: Spec) -> dict:
    """Return {compliant: bool, collisions: [(pair, [sheet indices])]}."""
    by_pair = {}
    for idx, sh in enumerate(spec.sheets):
        key = frozenset(sh["pair"])
        by_pair.setdefault(key, []).append(idx)
    collisions = [(sorted(k), v) for k, v in by_pair.items() if len(v) > 1]
    return {"compliant": not collisions, "collisions": collisions}


# ---------------------------------------------------------------------------
# Degrees of freedom
# ---------------------------------------------------------------------------

def dof_analysis(spec: Spec) -> dict:
    n_dims = len(spec.dims)
    n_sheets = len(spec.sheets)
    n_params = n_dims + n_sheets  # one L per dim, one sigma_eff per sheet
    n_constraints = sum(2 if s["sector"] == "quark" else 1 for s in spec.sheets)
    return {
        "n_params": n_params, "n_dims": n_dims, "n_sheets": n_sheets,
        "n_constraints": n_constraints, "dof": n_params - n_constraints,
    }


# ---------------------------------------------------------------------------
# Fit machinery
# ---------------------------------------------------------------------------

def _obs_mass(sector: str, item) -> list:
    """Observed (particle, mass, m_r) tuples a sheet contributes."""
    if sector == "quark":
        light, heavy = item
        return [(light, QUARK[light], 2), (heavy, QUARK[heavy], 1)]
    if sector == "electron":
        return [(item, LEPTON[item], 2)]
    return [(item, NEUTRINO[item], 2)]


def make_residuals(spec: Spec, assignment: list, tube_first: tuple):
    """Build the residual function for one discrete combo.

    x = [log10 L for each dim] + [sigma_eff for each sheet].
    Residual per hosted particle = log10(predicted / observed).
    """
    dims = spec.dims
    n_dims = len(dims)
    sheets = spec.sheets

    def predict(x) -> dict:
        Ls = {d: 10.0 ** x[i] for i, d in enumerate(dims)}
        out = {}
        for s_idx, sh in enumerate(sheets):
            d1, d2 = sh["pair"]
            if tube_first[s_idx]:
                L_T, L_R = Ls[d1], Ls[d2]
            else:
                L_T, L_R = Ls[d2], Ls[d1]
            sigma = x[n_dims + s_idx]
            for name, _obs, m_r in _obs_mass(sh["sector"], assignment[s_idx]):
                delta = m_r - sigma  # m_t = 1
                out[name] = COEFF * sqrt((1.0 / L_T) ** 2 + (delta / L_R) ** 2)
        return out

    targets = []
    for s_idx, sh in enumerate(sheets):
        for name, obs, _m_r in _obs_mass(sh["sector"], assignment[s_idx]):
            targets.append((name, obs))

    def residuals(x):
        pred = predict(x)
        r = []
        for name, obs in targets:
            p = pred[name]
            r.append(log10(p / obs) if p > 0 else 1e6)
        return r

    return residuals, predict, targets


def max_err_pct(pred: dict, targets: list) -> float:
    return max(abs(100.0 * (pred[n] - obs) / obs) for n, obs in targets)


def fit_combo(spec: Spec, assignment: list, tube_first: tuple,
              n_seeds: int, rng_offset: int = 0):
    """Fit one discrete combo from n_seeds random restarts.

    Returns a list of {x, max_err, pred} for every restart that converged,
    sorted by max_err ascending.
    """
    residuals, predict, targets = make_residuals(spec, assignment, tube_first)
    n_dims = len(spec.dims)
    n_sheets = len(spec.sheets)
    lo = [LOG_L_LO] * n_dims + [SIGMA_LO] * n_sheets
    hi = [LOG_L_HI] * n_dims + [SIGMA_HI] * n_sheets
    sols = []
    for s in range(n_seeds):
        rng = np.random.default_rng(s + rng_offset)
        x0 = list(rng.uniform(-4, 14, n_dims)) + list(rng.uniform(0.3, 2.7, n_sheets))
        try:
            res = least_squares(residuals, x0, bounds=(lo, hi),
                                method="trf", max_nfev=800)
        except Exception:
            continue
        pred = predict(res.x)
        sols.append({"x": res.x, "max_err": max_err_pct(pred, targets),
                     "pred": pred})
    sols.sort(key=lambda d: d["max_err"])
    return sols


def enumerate_combos(spec: Spec):
    """Yield (assignment, tube_first) over all discrete choices."""
    sectors = spec.sectors()
    sector_sheet_idx = {sec: [i for i, s in enumerate(spec.sheets)
                              if s["sector"] == sec] for sec in sectors}
    per_sector_perms = [list(permutations(SECTOR_ITEMS[sec])) for sec in sectors]
    n_sheets = len(spec.sheets)
    for perm_combo in product(*per_sector_perms):
        assignment = [None] * n_sheets
        for sec, perm in zip(sectors, perm_combo):
            for sheet_idx, item in zip(sector_sheet_idx[sec], perm):
                assignment[sheet_idx] = item
        for tube_first in product((True, False), repeat=n_sheets):
            yield assignment, tube_first


# ---------------------------------------------------------------------------
# Manifold characterization — pinned vs ranged parameters
# ---------------------------------------------------------------------------

def characterize_params(spec: Spec, solutions: list) -> list:
    """Given good-fit solutions for ONE discrete combo, decide for each
    parameter whether it is pinned or free over a range.

    Returns a list of {label, kind, ...} entries.
    """
    n_dims = len(spec.dims)
    xs = np.array([s["x"] for s in solutions])
    out = []
    for i, dim in enumerate(spec.dims):
        col = xs[:, i]  # log10 L
        lo, hi = col.min(), col.max()
        if hi - lo < 0.03:  # ~7% in linear scale
            out.append({"label": f"L[{dim}]", "kind": "pinned",
                        "value": 10.0 ** float(np.median(col)), "unit": "fm"})
        else:
            open_above = hi > LOG_L_HI - 0.5
            out.append({"label": f"L[{dim}]", "kind": "ranged",
                        "lo": 10.0 ** lo, "hi": 10.0 ** hi,
                        "open_above": open_above, "unit": "fm"})
    for j, sh in enumerate(spec.sheets):
        col = xs[:, n_dims + j]
        lo, hi = col.min(), col.max()
        tag = f"sigma_eff[Ma{tuple(sh['pair'])}]"
        if hi - lo < 0.03:
            out.append({"label": tag, "kind": "pinned",
                        "value": float(np.median(col)), "unit": ""})
        else:
            out.append({"label": tag, "kind": "ranged",
                        "lo": float(lo), "hi": float(hi),
                        "open_above": False, "unit": ""})
    return out


# ---------------------------------------------------------------------------
# Solve one candidate
# ---------------------------------------------------------------------------

def solve(spec: Spec, scan_seeds: int, map_seeds: int, threshold: float) -> dict:
    r1 = check_r1(spec)
    dof = dof_analysis(spec)

    # Scan phase — every discrete combo, few seeds, keep the best per combo.
    scan = []
    for assignment, tube_first in enumerate_combos(spec):
        sols = fit_combo(spec, assignment, tube_first, scan_seeds)
        if sols:
            scan.append({"assignment": assignment, "tube_first": tube_first,
                         "best_err": sols[0]["max_err"]})
    scan.sort(key=lambda d: d["best_err"])

    compliant = [c for c in scan if c["best_err"] <= threshold]

    result = {
        "spec": spec, "r1": r1, "dof": dof,
        "n_combos_scanned": len(scan),
        "n_combos_compliant": len(compliant),
        "best_err": scan[0]["best_err"] if scan else None,
        "compliant": bool(compliant),
        "combos": compliant[:12],   # report a capped list
        "manifold": None,
    }
    if not compliant:
        return result

    # Mapping phase — re-fit the best discrete combo with many seeds to
    # trace the continuous solution manifold.
    best = compliant[0]
    sols = fit_combo(spec, best["assignment"], best["tube_first"],
                     map_seeds, rng_offset=1000)
    good = [s for s in sols if s["max_err"] <= threshold]
    if good:
        result["manifold"] = {
            "assignment": best["assignment"],
            "tube_first": best["tube_first"],
            "n_solutions": len(good),
            "params": characterize_params(spec, good),
            "best_pred": good[0]["pred"],
            "best_err": good[0]["max_err"],
        }
    return result


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def _fmt_item(item) -> str:
    return f"{item[0]}/{item[1]}" if isinstance(item, tuple) else str(item)


def format_report(result: dict) -> str:
    spec = result["spec"]
    L = []
    L.append("=" * 78)
    L.append(f"CANDIDATE: {spec.name}")
    if spec.note:
        L.append(f"  {spec.note}")
    L.append("=" * 78)
    L.append("")
    L.append(f"Topology: {len(spec.dims)} dims, {len(spec.sheets)} sheets")
    for sh in spec.sheets:
        L.append(f"  Ma{tuple(sh['pair'])}  [{sh['sector']}]")
    L.append("")

    # R1
    r1 = result["r1"]
    if r1["compliant"]:
        L.append("R1 (one sheet per dim-pair): SATISFIED")
    else:
        L.append("R1 (one sheet per dim-pair): VIOLATED")
        for pair, idxs in r1["collisions"]:
            secs = ", ".join(spec.sheets[i]["sector"] for i in idxs)
            L.append(f"  pair Ma{tuple(pair)} carries {len(idxs)} sheets: {secs}")
    L.append("")

    # DOF
    d = result["dof"]
    L.append("Degrees of freedom:")
    L.append(f"  free params  = {d['n_params']}  "
             f"({d['n_dims']} dim sizes + {d['n_sheets']} sigma_eff)")
    L.append(f"  constraints  = {d['n_constraints']}  (one per hosted mass)")
    L.append(f"  DOF          = {d['dof']}  "
             + ("(just-determined)" if d["dof"] == 0
                else f"(underdetermined — {d['dof']}-parameter solution family)"
                if d["dof"] > 0 else "(over-determined)"))
    L.append("")

    # Fit
    if not result["compliant"]:
        be = result["best_err"]
        L.append("FIT: NO compliant solution found.")
        if be is not None:
            L.append(f"  best max |Delta%| over all discrete combos = {be:.3f}%")
        L.append("")
        L.append("=" * 78)
        return "\n".join(L)

    L.append(f"FIT: compliant solution found "
             f"(best max |Delta%| = {result['best_err']:.4f}%).")
    L.append(f"  discrete (assignment + tube/ring) combos scanned : "
             f"{result['n_combos_scanned']}")
    L.append(f"  discrete combos that reach a compliant fit       : "
             f"{result['n_combos_compliant']}")
    if result["n_combos_compliant"] > 1:
        L.append("  -> multiple discrete solutions exist (see list below).")
    L.append("")

    # Discrete combo list
    L.append("Compliant discrete combos (best first):")
    for c in result["combos"]:
        asg = ", ".join(f"Ma{tuple(spec.sheets[i]['pair'])}:"
                        f"{_fmt_item(c['assignment'][i])}"
                        for i in range(len(spec.sheets)))
        tr = "".join("T" if t else "R" for t in c["tube_first"])
        L.append(f"  err={c['best_err']:.4f}%  tube/ring={tr}  {asg}")
    if result["n_combos_compliant"] > len(result["combos"]):
        L.append(f"  ... and {result['n_combos_compliant'] - len(result['combos'])}"
                 f" more")
    L.append("")

    # Manifold
    m = result["manifold"]
    if m:
        L.append("Best discrete solution — assignment:")
        for i, sh in enumerate(spec.sheets):
            tf = m["tube_first"][i]
            d1, d2 = sh["pair"]
            tube, ring = (d1, d2) if tf else (d2, d1)
            L.append(f"  Ma{tuple(sh['pair'])} [{sh['sector']}]  "
                     f"hosts {_fmt_item(m['assignment'][i])}  "
                     f"(tube={tube}, ring={ring})")
        L.append("")
        L.append(f"Continuous-parameter manifold "
                 f"({m['n_solutions']} sampled solutions):")
        for p in m["params"]:
            if p["kind"] == "pinned":
                if p["unit"]:
                    L.append(f"  {p['label']:28s} PINNED  ~= "
                             f"{p['value']:.4g} {p['unit']}")
                else:
                    L.append(f"  {p['label']:28s} PINNED  ~= {p['value']:.4f}")
            else:
                if p.get("open_above"):
                    L.append(f"  {p['label']:28s} RANGED  >= "
                             f"{p['lo']:.4g} {p['unit']} (unbounded above)")
                else:
                    L.append(f"  {p['label']:28s} RANGED  "
                             f"[{p['lo']:.4g}, {p['hi']:.4g}] {p['unit']}")
        n_ranged = sum(1 for p in m["params"] if p["kind"] == "ranged")
        L.append("")
        L.append(f"  {n_ranged} parameter(s) free over a range; "
                 f"{len(m['params']) - n_ranged} pinned. "
                 f"(Expected free directions = DOF = {d['dof']}.)")
        L.append("")

        # Predicted masses
        L.append("Predicted vs observed masses (best solution, "
                 f"max |Delta%| = {m['best_err']:.4f}%):")
        obs_all = {**QUARK, **LEPTON, **NEUTRINO}
        for name, pred in m["best_pred"].items():
            obs = obs_all[name]
            err = 100.0 * (pred - obs) / obs
            L.append(f"  {name:5s} pred = {pred:>11.5g}  "
                     f"obs = {obs:>11.5g}  Delta% = {err:+.3f}%")
        L.append("")

    L.append("=" * 78)
    return "\n".join(L)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv=None):
    ap = argparse.ArgumentParser(description="General ma-domain candidate solver.")
    ap.add_argument("spec", nargs="?", help="path to a candidate spec JSON")
    ap.add_argument("--all", nargs="?", const="cand_specs", metavar="DIR",
                    help="solve every *.json spec in DIR (default cand_specs/)")
    ap.add_argument("--seeds", type=int, default=60,
                    help="restarts per discrete combo, mapping phase (default 60)")
    ap.add_argument("--scan-seeds", type=int, default=3,
                    help="restarts per discrete combo, scan phase (default 3)")
    ap.add_argument("--threshold", type=float, default=1.0,
                    help="max |Delta%%| for a compliant fit (default 1.0)")
    ap.add_argument("--out", default=None,
                    help="output report path (default outputs/cand_<name>.txt)")
    args = ap.parse_args(argv)

    here = Path(__file__).resolve().parent
    out_dir = here.parent / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.all is not None:
        spec_dir = (here / args.all) if not Path(args.all).is_absolute() \
            else Path(args.all)
        spec_paths = sorted(spec_dir.glob("*.json"))
        if not spec_paths:
            print(f"no specs found in {spec_dir}", file=sys.stderr)
            return 1
    elif args.spec:
        spec_paths = [Path(args.spec)]
    else:
        ap.print_help()
        return 1

    for spec_path in spec_paths:
        spec = load_spec(str(spec_path))
        print(f"solving {spec.name} ...", file=sys.stderr)
        result = solve(spec, args.scan_seeds, args.seeds, args.threshold)
        report = format_report(result)
        print(report)
        out_path = Path(args.out) if (args.out and len(spec_paths) == 1) \
            else out_dir / f"cand_{spec.name}.txt"
        out_path.write_text(report + "\n")
        print(f"  -> {out_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
