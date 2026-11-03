"""Look-elsewhere check for the wye + neutrino circle ring-sharing near-fit.

What it does
  Repeats wye_theta13.py's search (8 tube/ring sharing choices × 2 segment
  orders, point flavors; fitted: two segment lengths and the ring size r)
  with the three charged-lepton tube sizes replaced by random hierarchical
  sizes spanning the same total range (log-uniform), the ring bounded above by
  the smallest tube as in the real case (r ≤ 0.7 fm ≈ τ tube).  Prints the best
  loss per trial, for comparison with the real-mass result.

Inputs: command-line options (--trials, --seed, --real for the baseline).
Outputs: printed best loss per trial (and its configuration).
"""
import argparse
import itertools

import numpy as np

import wye_theta13 as wt

REAL = {"e": 2426.0, "mu": 11.73, "tau": 0.6977}


def best_over_combos(tubes, restarts, seed):
    wt.TUBE = dict(tubes)
    wt.R_RANGE = (1e-4 * min(tubes.values()) / 0.6977, min(tubes.values()))
    wt.Args.n_grid = 1000
    best = (np.inf, None)
    for order in (("e", "mu", "tau"), ("e", "tau", "mu")):
        for use_ring in itertools.product((False, True), repeat=3):
            if all(use_ring):
                continue                                  # all on one ring: no junctions
            loss, ue3, r_fm, _, _ = wt.run(order, use_ring, "point", restarts, seed)
            if loss < best[0]:
                best = (loss, (order, "".join("R" if u else "T" for u in use_ring), r_fm, ue3))
    return best


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--trials", type=int, default=3)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--restarts", type=int, default=3)
    p.add_argument("--real", action="store_true", help="run the real-mass baseline instead")
    a = p.parse_args()
    if a.real:
        loss, cfg = best_over_combos(REAL, a.restarts, a.seed)
        print(f"real tube sizes: best loss {loss:.2e}  {cfg}", flush=True)
        return
    rng = np.random.default_rng(a.seed)
    span = np.log(max(REAL.values()) / min(REAL.values()))
    for t in range(a.trials):
        lw = np.sort(rng.uniform(0, span, 2))
        sizes = np.exp(np.array([0.0, lw[0], lw[1]])) * min(REAL.values())
        sizes = rng.permutation(sizes)
        tubes = dict(zip(("e", "mu", "tau"), sizes))
        loss, cfg = best_over_combos(tubes, a.restarts, a.seed)
        print(f"trial {t + 1}: tubes {np.round(sizes, 3)} fm  best loss {loss:.2e}  {cfg}", flush=True)


if __name__ == "__main__":
    main()
