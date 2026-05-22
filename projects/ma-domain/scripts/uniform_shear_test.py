#!/usr/bin/env python3
"""
uniform_shear_test.py — does a QY-ED candidate still fit if the shear is uniform?

The general solver (cand_solver.py) fits one free sigma_eff per sheet. That
per-sheet freedom is what gives K4 its DOF-1 solution family. This script asks
the counterfactual: if the shear is *not* free per sheet — if it is a single
value shared across the topology — can the candidate still reproduce the 9
fermion masses, or does the topology become genuinely unsolvable?

It re-fits each spec under three shear constraints:

  free  — one sigma_eff per sheet (the unconstrained baseline; = cand_solver).
          K4: 4 L + 6 sigma_eff = 10 params vs 9 masses.
  bare  — one global *bare* shear sigma; each sheet's sigma_eff = sigma + c*tau,
          where (c, tau) is the posited per-sector cross-section construction
          (quark clover c*tau = 2/3; electron ellipse c*tau = 2). The twist
          still differs by sector — only the bare shear is uniform.
          K4: 4 L + 1 sigma = 5 params vs 9 masses.
  seff  — one global sigma_eff shared verbatim by every sheet (strictest).
          K4: 4 L + 1 sigma_eff = 5 params vs 9 masses.

For each (spec, mode) it sweeps every discrete (particle->sheet, tube/ring)
combo, fits the continuous parameters from several random restarts, refines the
best combo, and reports the smallest achievable max|Delta%|. A fit "clears" if
that error is within the compliance threshold (default 1%).

Inputs : spec JSONs in cand_specs/ (default: the three QY-ED* specs).
Outputs: a comparison report to outputs/uniform_shear_test.txt (and stdout).

Usage:
    python uniform_shear_test.py [--specs A.json B.json ...]
                                 [--scan-seeds N] [--refine-seeds N]
                                 [--threshold PCT]

This is a constrained-fit companion to cand_solver.py; it imports that module's
fit machinery (build_fit, enumerate_combos, sector construction) unchanged.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares

import cand_solver as cs


# Generous shear bounds — wide enough that a "no fit" verdict cannot be blamed
# on the bound. The single shear parameter g is searched over this range.
G_LO, G_HI = -4.0, 8.0


def sheet_offsets(spec: cs.Spec, mode: str) -> np.ndarray:
    """Per-sheet offset added to the single shear param to get sigma_eff.

    bare: offset = c*tau for that sheet's sector (sigma_eff = sigma + c*tau).
    seff: offset = 0      (sigma_eff shared verbatim).
    """
    off = []
    for sh in spec.sheets:
        if mode == "seff":
            off.append(0.0)
        else:  # bare
            con = cs.SECTOR_CONSTRUCTION.get(sh["sector"])
            if con is None:
                raise ValueError(f"no construction for sector {sh['sector']}")
            off.append(con["monodromy_c"] * con["tau"])
    return np.array(off, dtype=float)


def fit_uniform(spec, assignment, tube_first, offsets, n_seeds, seed0=0):
    """Fit one discrete combo with a single shear parameter.

    Parameter vector x_r = [log10 L per dim] + [g]; full per-sheet
    sigma_eff = g + offsets. Returns the best {max_err, full_x, pred} or None.
    """
    residual, jac, predict, targets, n_params = cs.build_fit(
        spec, assignment, tube_first)
    n_dims = len(spec.dims)

    def expand(xr):
        full = np.empty(n_params)
        full[:n_dims] = xr[:n_dims]
        full[n_dims:] = xr[n_dims] + offsets
        return full

    def res_r(xr):
        return residual(expand(xr))

    def jac_r(xr):
        J = jac(expand(xr))
        # dr/dg = sum_s dr/dsigma_eff[s], since each sigma_eff[s] = g + const.
        return np.hstack([J[:, :n_dims],
                          J[:, n_dims:].sum(axis=1, keepdims=True)])

    lo = [cs.LOG_L_LO] * n_dims + [G_LO]
    hi = [cs.LOG_L_HI] * n_dims + [G_HI]
    best = None
    for s in range(n_seeds):
        rng = np.random.default_rng(seed0 + s)
        x0 = np.concatenate([rng.uniform(-4, 14, n_dims),
                             [rng.uniform(G_LO + 0.5, G_HI - 0.5)]])
        try:
            r = least_squares(res_r, x0, jac=jac_r, bounds=(lo, hi),
                              method="trf", max_nfev=400)
        except Exception:
            continue
        full = expand(r.x)
        pred = predict(full)
        merr = max(abs(100.0 * (pred[n] - o) / o) for n, o in targets)
        if best is None or merr < best["max_err"]:
            best = {"xr": r.x, "full": full, "max_err": merr, "pred": pred,
                    "g": float(r.x[n_dims])}
    return best


def run_mode(spec, mode, scan_seeds, refine_seeds):
    """Sweep all discrete combos for one (spec, mode); refine the best."""
    combos = list(cs.enumerate_combos(spec))
    n_dims = len(spec.dims)

    best = None
    if mode == "free":
        # Unconstrained per-sheet sigma_eff — reuse cand_solver's fit_combo.
        for asg, tf in combos:
            sols = cs.fit_combo(spec, asg, tf, scan_seeds)
            if sols and (best is None or sols[0]["max_err"] < best["max_err"]):
                best = {"assignment": asg, "tube_first": tf,
                        "max_err": sols[0]["max_err"], "pred": sols[0]["pred"],
                        "g": None}
        if best is not None:
            sols = cs.fit_combo(spec, best["assignment"], best["tube_first"],
                                refine_seeds, rng_offset=9000)
            if sols and sols[0]["max_err"] < best["max_err"]:
                best.update(max_err=sols[0]["max_err"], pred=sols[0]["pred"])
        return best

    offsets = sheet_offsets(spec, mode)
    for asg, tf in combos:
        b = fit_uniform(spec, asg, tf, offsets, scan_seeds)
        if b and (best is None or b["max_err"] < best["max_err"]):
            best = {"assignment": asg, "tube_first": tf, **b}
    if best is not None:
        b = fit_uniform(spec, best["assignment"], best["tube_first"],
                        offsets, refine_seeds, seed0=9000)
        if b and b["max_err"] < best["max_err"]:
            best.update(max_err=b["max_err"], pred=b["pred"], g=b["g"],
                        full=b["full"])
    return best


def main(argv=None):
    here = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--specs", nargs="+", default=None,
                    help="spec JSONs (default: the three QY-ED* specs)")
    ap.add_argument("--scan-seeds", type=int, default=4,
                    help="random restarts per discrete combo (default 4)")
    ap.add_argument("--refine-seeds", type=int, default=60,
                    help="restarts to refine the best combo (default 60)")
    ap.add_argument("--threshold", type=float, default=1.0,
                    help="max |Delta%%| for a fit to count as clearing (default 1.0)")
    args = ap.parse_args(argv)

    if args.specs:
        spec_paths = [Path(p) for p in args.specs]
    else:
        sd = here / "cand_specs"
        spec_paths = sorted(p for p in sd.glob("QY-ED*.json"))
    if not spec_paths:
        print("no specs found", file=sys.stderr)
        return 1

    modes = ["free", "bare", "seff"]
    mode_desc = {
        "free": "per-sheet sigma_eff (unconstrained baseline)",
        "bare": "one global bare shear; sigma_eff = sigma + c*tau per sector",
        "seff": "one global sigma_eff shared verbatim by every sheet",
    }
    obs_all = {**cs.QUARK, **cs.LEPTON, **cs.NEUTRINO}

    out = []
    out.append("=" * 78)
    out.append("UNIFORM-SHEAR TEST — can QY-ED fit with the shear not free per sheet?")
    out.append("=" * 78)
    out.append("")
    for m in modes:
        out.append(f"  {m:5s} : {mode_desc[m]}")
    out.append(f"  compliance threshold: max|Delta%| <= {args.threshold:g}%")
    out.append("")

    summary = []
    for sp in spec_paths:
        spec = cs.load_spec(str(sp))
        d = cs.dof_analysis(spec)
        print(f"solving {spec.name} ...", file=sys.stderr, flush=True)
        out.append("-" * 78)
        out.append(f"CANDIDATE: {spec.name}   "
                   f"({d['n_dims']} dims, {d['n_sheets']} sheets, "
                   f"{d['n_constraints']} masses)")
        out.append("-" * 78)
        for m in modes:
            print(f"  mode {m} ...", file=sys.stderr, flush=True)
            best = run_mode(spec, m, args.scan_seeds, args.refine_seeds)
            if best is None:
                out.append(f"  {m:5s}: no fit converged")
                continue
            if m == "free":
                nparam = d["n_dims"] + d["n_sheets"]
            else:
                nparam = d["n_dims"] + 1
            bal = nparam - d["n_constraints"]
            balstr = (f"DOF {bal:+d}" if bal != 0 else "just-determined")
            clears = best["max_err"] <= args.threshold
            verdict = "CLEARS" if clears else "FAILS "
            gstr = "" if best["g"] is None else f"  shear g = {best['g']:.4f}"
            out.append(f"  {m:5s}: {nparam:2d} params vs {d['n_constraints']} "
                       f"masses ({balstr:>14s})   "
                       f"best max|Delta%| = {best['max_err']:.4g}%  "
                       f"-> {verdict}{gstr}")
            summary.append((spec.name, m, nparam, bal, best["max_err"], clears))
            # Per-mass breakdown for the constrained modes (shows what breaks).
            if m != "free":
                worst = sorted(best["pred"].items(),
                               key=lambda kv: -abs((kv[1] - obs_all[kv[0]])
                                                   / obs_all[kv[0]]))
                line = "        per-mass Delta%: " + "  ".join(
                    f"{n}={100.0*(p-obs_all[n])/obs_all[n]:+.2g}"
                    for n, p in worst)
                out.append(line)
        out.append("")

    out.append("=" * 78)
    out.append("SUMMARY")
    out.append("=" * 78)
    out.append(f"{'candidate':18s} {'mode':6s} {'params':>7s} {'DOF':>5s} "
               f"{'best max|D%|':>13s}  verdict")
    for name, m, npar, bal, err, clears in summary:
        out.append(f"{name:18s} {m:6s} {npar:7d} {bal:+5d} {err:13.4g}  "
                   f"{'CLEARS' if clears else 'FAILS'}")
    out.append("")

    report = "\n".join(out)
    print(report)
    out_dir = here.parent / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "uniform_shear_test.txt").write_text(report + "\n")
    print(f"  -> {out_dir / 'uniform_shear_test.txt'}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
