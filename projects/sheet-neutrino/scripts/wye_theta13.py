"""Can the charged-wye neutrino circle reach θ13 ≈ 8.5° without new freedom?

What it does
  Neutrino circle (junction_fit model, flips off) with three segments, one per
  charged lepton.  Each segment shares either its lepton's TUBE dimension
  (width = C/m_lepton: 2426, 11.73, 0.698 fm) or the wye's shared tiny RING
  (width r, the wye's own unconstrained size, r ≤ 0.7 fm).  For every
  tube/ring choice (8) and segment order (2), fits the two segment lengths
  (plus log r when any segment uses the ring), under both flavor definitions
  (point coupling at the junction, or concentration on the segment).
  Reports the loss and the resulting |U_e3|² (θ13 measure; measured 0.022).

Inputs: command-line options.  Outputs: printed table, best cases in full.
"""
import argparse
import itertools

import numpy as np
from scipy.optimize import minimize

import junction_fit as jf

TUBE = {"e": 2426.0, "mu": 11.73, "tau": 0.6977}
R_RANGE = (1e-4, 0.7)


class Args:
    phases = False
    flips = False
    kmax = 4.0
    n_grid = 1200
    n_per_seg = 120
    ratio_weight = 0.3
    s23 = 0.5
    junction = "free"


def run(order, use_ring, flavor, restarts, seed):
    a = Args()
    a.flavor = flavor
    needs_r = any(use_ring)

    def widths(lr):
        return np.array([np.exp(lr) if u else TUBE[l] for l, u in zip(order, use_ring)])

    def x_of(p):
        w = widths(p[2] if needs_r else 0.0)
        r = np.array([(w[i - 1] - w[i]) / (w[i - 1] + w[i]) for i in range(3)])
        return np.concatenate([[p[0], p[1]], np.arctanh(np.clip(r, -0.999999, 0.999999))])

    def loss(p):
        if needs_r and not (np.log(R_RANGE[0]) <= p[2] <= np.log(R_RANGE[1])):
            return 1e3
        return jf.evaluate(x_of(p), a)[0]

    rng = np.random.default_rng(seed)
    best = None
    for _ in range(restarts):
        p0 = list(rng.uniform(0.2, 2.5, 2))
        if needs_r:
            p0.append(rng.uniform(*np.log(R_RANGE)))
        res = minimize(loss, p0, method="Nelder-Mead", options=dict(maxiter=400))
        if best is None or res.fun < best.fun:
            best = res
    info = jf.evaluate(x_of(best.x), a, full=True)[1]
    ue3 = None
    if info is not None:
        U2 = info["U2"]
        ue3 = min(U2[:, 2])          # the flavor row with least ν3 is the ν_e candidate
    r_fm = np.exp(best.x[2]) if needs_r else None
    return best.fun, ue3, r_fm, x_of(best.x), a


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--restarts", type=int, default=6)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--flavors", nargs="+", default=["point", "segment"])
    p.add_argument("--show", type=int, default=3)
    a = p.parse_args()
    rows = []
    for flavor in a.flavors:
        for order in (("e", "mu", "tau"), ("e", "tau", "mu")):
            for use_ring in itertools.product((False, True), repeat=3):
                loss, ue3, r_fm, x, args = run(order, use_ring, flavor, a.restarts, a.seed)
                tag = "".join("R" if u else "T" for u in use_ring)
                rows.append((loss, flavor, order, tag, ue3, r_fm, x, args))
                print(f"  {flavor:7s} order {'-'.join(order):10s} share {tag}: loss {loss:.2e}"
                      + (f", |U_e3|² {ue3:.3f}" if ue3 is not None else "")
                      + (f", ring r = {r_fm:.3g} fm" if r_fm is not None else ""), flush=True)
    rows.sort(key=lambda r: r[0])
    for loss, flavor, order, tag, ue3, r_fm, x, args in rows[:a.show]:
        jf.report(x, args, f"{flavor}, order {'-'.join(order)}, share {tag}"
                           + (f", r = {r_fm:.3g} fm" if r_fm is not None else ""))


if __name__ == "__main__":
    main()
