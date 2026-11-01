"""Test the lepton-domain circle with junction widths taken from ma-domain's K4 fit.

What it does
  In ma-domain's K4 candidate (QY-ED-share3) the charged leptons live on the
  sheets e = (m1, m2), μ = (m1, m3), τ = (m2, m3), with fitted dimension sizes
  m2 ≈ 0.007344 fm, m3 ≈ 1 fm (0.91–1.05), m1 free over [4505, 2.2e15] fm
  (K4's one leftover degree of freedom).  Each neutrino segment shares one
  dimension of its lepton's sheet; its ribbon width is taken proportional to
  that dimension's size, so junction reflections are r = (w_a−w_b)/(w_a+w_b).

  For every choice of shared dimensions (2×2×2), both cyclic orders of the
  segments, and flips on/off, only the two segment-length ratios are fitted
  (plus log m1 when m1 is used).  Against four independent data numbers this is
  a genuine test, not an under-determined fit.

Inputs: command-line options.  Outputs: printed table of best losses and,
for the best combinations, the fitted solution.
"""
import argparse
import itertools

import numpy as np
from scipy.optimize import minimize

import junction_fit as jf

SIZES = {"m2": 0.007344, "m3": 1.0}
M1_RANGE = (4505.0, 2.201e15)
CHOICES = {"e": ("m1", "m2"), "mu": ("m1", "m3"), "tau": ("m2", "m3")}


class Args:
    phases = False
    kmax = 4.0
    n_grid = 1500
    n_per_seg = 150
    flavor = "point"
    ratio_weight = 0.3
    s23 = 0.5
    junction = "free"


def run(order, dims, flips, restarts, seed):
    a = Args()
    a.flips = flips
    uses_m1 = "m1" in dims

    def widths(lm1):
        size = dict(SIZES, m1=np.exp(lm1))
        return np.array([size[d] for d in dims])

    def loss(p):
        L1, L2 = p[0], p[1]
        lm1 = p[2] if uses_m1 else 0.0
        if uses_m1 and not (np.log(M1_RANGE[0]) <= lm1 <= np.log(M1_RANGE[1])):
            return 1e3
        w = widths(lm1)
        r = np.array([(w[i - 1] - w[i]) / (w[i - 1] + w[i]) for i in range(3)])
        x = np.concatenate([[L1, L2], np.arctanh(np.clip(r, -0.999999, 0.999999))])
        return jf.evaluate(x, a)[0]

    rng = np.random.default_rng(seed)
    best = None
    for _ in range(restarts):
        p0 = [rng.uniform(0.2, 2.5), rng.uniform(0.2, 2.5)]
        if uses_m1:
            p0.append(rng.uniform(np.log(M1_RANGE[0]), np.log(M1_RANGE[1])))
        res = minimize(loss, p0, method="Nelder-Mead", options=dict(maxiter=600))
        if best is None or res.fun < best.fun:
            best = res
    return best, uses_m1, a


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--restarts", type=int, default=8)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--show", type=int, default=3, help="best combinations to report in full")
    args = p.parse_args()

    rows = []
    for order in (("e", "mu", "tau"), ("e", "tau", "mu")):
        for pick in itertools.product(*(CHOICES[l] for l in order)):
            for flips in (False, True):
                best, uses_m1, a = run(order, pick, flips, args.restarts, args.seed)
                rows.append((best.fun, order, pick, flips, best.x, uses_m1, a))
                print(f"  order {'-'.join(order):10s} dims {'-'.join(pick):10s} "
                      f"flips {'on ' if flips else 'off'}  best loss {best.fun:.2e}"
                      + (f"  m1 ≈ {np.exp(best.x[2]):.3g} fm" if uses_m1 else ""), flush=True)
    rows.sort(key=lambda r: r[0])
    for loss, order, pick, flips, x, uses_m1, a in rows[:args.show]:
        size = dict(SIZES, m1=np.exp(x[2]) if uses_m1 else 1.0)
        w = np.array([size[d] for d in pick])
        r = np.array([(w[i - 1] - w[i]) / (w[i - 1] + w[i]) for i in range(3)])
        xx = np.concatenate([[x[0], x[1]], np.arctanh(np.clip(r, -0.999999, 0.999999))])
        jf.report(xx, a, f"order {'-'.join(order)}, dims {'-'.join(pick)}, flips "
                         f"{'on' if flips else 'off'}" + (f", m1 = {size['m1']:.3g} fm" if uses_m1 else ""))


if __name__ == "__main__":
    main()
