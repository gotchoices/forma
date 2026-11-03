"""Neutrino circle around K4's electron triangle, with junctions set by geometry.

What it does
  In ma-domain's K4 the three electron sheets form a triangle on the spokes
  m1, m2, m3; each spoke is shared by two electron sheets.  Here the neutrino
  circle runs around that triangle: each SEGMENT is one electron sheet and each
  JUNCTION is the spoke two neighboring sheets share.

  1. Bookkeeping: for each of K4's fitted discrete assignments, the tube/ring
     role of every spoke in the electron sheets (tube–tube, ring–ring, or
     mixed) and the hub's role in each quark sheet.
  2. Test: junction reflections come from a rule fixed in advance (no free
     per-junction numbers), r = (w_A − w_B)/(w_A + w_B), with w for each of
     the two sheets meeting at a corner taken as:
        other  the size of the sheet's non-shared dimension
        tube   the size of the sheet's tube
        ring   the size of the sheet's ring
     Fitted: two segment lengths, plus m1 (K4's free size, 4505 fm to 2.2e15
     fm) and m3 (0.91–1.05 fm).  Flips off and on.  Flavor at a point
     (junction entry), via junction_fit.

Inputs: command-line options.  Outputs: bookkeeping tables, fit table, best fits.
"""
import argparse

import numpy as np
from scipy.optimize import minimize

import junction_fit as jf

SHEET_ORDER = [("m1", "m4"), ("m2", "m4"), ("m3", "m4"), ("m1", "m2"), ("m1", "m3"), ("m2", "m3")]
# K4's fitted discrete assignments (ma-domain outputs/cand_QY-ED-share3*.txt):
# tube/ring code per sheet in SHEET_ORDER (T = first dim is the tube), and the
# particle hosted on each sheet.
ASSIGNMENTS = [
    ("TRRTTR", ["u/d", "b/t", "s/c", "e", "mu", "tau"]),
    ("TRRTTT", ["u/d", "s/c", "b/t", "e", "mu", "tau"]),
    ("RTRRTT", ["s/c", "u/d", "b/t", "e", "tau", "mu"]),
    ("TRRTTT", ["u/d", "s/c", "b/t", "mu", "e", "tau"]),
    ("TRRTTR", ["u/d", "b/t", "s/c", "mu", "e", "tau"]),
]
M2, M3_RANGE, M1_RANGE = 0.007344, (0.9097, 1.053), (4505.0, 2.201e15)


class Args:
    phases = False
    kmax = 4.0
    n_grid = 1200
    n_per_seg = 120
    flavor = "point"
    ratio_weight = 0.3
    s23 = 0.5
    junction = "free"


def roles(code, hosts):
    """Return (electron sheets {lepton: (tube, ring)}, quark sheets {quark: (tube, ring)})."""
    elec, quark = {}, {}
    for (d1, d2), c, h in zip(SHEET_ORDER, code, hosts):
        tr = (d1, d2) if c == "T" else (d2, d1)
        (elec if h in ("e", "mu", "tau") else quark)[h] = tr
    return elec, quark


def bookkeeping():
    print("== Role bookkeeping across K4 assignments")
    for code, hosts in ASSIGNMENTS:
        elec, quark = roles(code, hosts)
        spoke_roles = {}
        for lep, (t, r) in elec.items():
            spoke_roles.setdefault(t, []).append(f"T({lep})")
            spoke_roles.setdefault(r, []).append(f"R({lep})")
        kinds = {d: ("tube–tube" if all(x.startswith("T") for x in v) else
                     "ring–ring" if all(x.startswith("R") for x in v) else "mixed")
                 for d, v in spoke_roles.items()}
        hub = {q: ("tube" if t == "m4" else "ring") for q, (t, r) in quark.items()}
        print(f"  {code} {hosts}:")
        print("    electron spokes: " + "; ".join(f"{d} {kinds[d]} ({', '.join(spoke_roles[d])})"
                                              for d in sorted(spoke_roles)))
        print("    hub role in quark sheets: " + ", ".join(f"{q}: {v}" for q, v in hub.items()))


def circle(elec):
    """Cyclic order of the three electron sheets and the spoke at each junction."""
    sheets = {lep: set(tr) for lep, tr in elec.items()}
    order = ["e"]
    while len(order) < 3:
        last = order[-1]
        nxt = [l for l in sheets if l not in order and sheets[l] & sheets[last]][0]
        order.append(nxt)
    shared = [(sheets[order[i - 1]] & sheets[order[i]]).pop() for i in range(3)]
    return order, shared          # junction i sits between order[i-1] and order[i]


def run(code, hosts, rule, flips, restarts, seed):
    elec, _ = roles(code, hosts)
    order, shared = circle(elec)
    a = Args()
    a.flips = flips

    def sizes(p):
        return {"m1": np.exp(p[2]), "m2": M2, "m3": p[3]}

    def width(lep, junction_dim, sz):
        t, r = elec[lep]
        if rule == "tube":
            return sz[t]
        if rule == "ring":
            return sz[r]
        other = r if t == junction_dim else t           # the sheet's non-shared dimension
        return sz[other]

    def x_of(p):
        sz = sizes(p)
        rs = []
        for i in range(3):
            A, B, s = order[i - 1], order[i], shared[i]
            wa, wb = width(A, s, sz), width(B, s, sz)
            rs.append((wa - wb) / (wa + wb))
        return np.concatenate([[p[0], p[1]], np.arctanh(np.clip(rs, -0.999999, 0.999999))])

    def loss(p):
        if not (np.log(M1_RANGE[0]) <= p[2] <= np.log(M1_RANGE[1])
                and M3_RANGE[0] <= p[3] <= M3_RANGE[1]):
            return 1e3
        return jf.evaluate(x_of(p), a)[0]

    rng = np.random.default_rng(seed)
    best = None
    for _ in range(restarts):
        p0 = [rng.uniform(0.2, 2.5), rng.uniform(0.2, 2.5),
              rng.uniform(*np.log(M1_RANGE)), rng.uniform(*M3_RANGE)]
        res = minimize(loss, p0, method="Nelder-Mead", options=dict(maxiter=300))
        if best is None or res.fun < best.fun:
            best = res
    return best, order, shared, x_of(best.x), a


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--rules", nargs="+", default=["other", "tube", "ring"])
    p.add_argument("--restarts", type=int, default=4)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--show", type=int, default=3)
    a = p.parse_args()
    bookkeeping()
    print("\n== Fits (point flavor)")
    rows = []
    for code, hosts in ASSIGNMENTS:
        for rule in a.rules:
            for flips in (False, True):
                best, order, shared, x, args = run(code, hosts, rule, flips, a.restarts, a.seed)
                rows.append((best.fun, code, hosts, rule, flips, order, shared, best.x, x, args))
                print(f"  {code} e-sheet={hosts[3:]} rule {rule:5s} flips {'on ' if flips else 'off'}: "
                      f"loss {best.fun:.2e}  (circle {'-'.join(order)}, junctions {shared}, "
                      f"m1 ≈ {np.exp(best.x[2]):.3g} fm)", flush=True)
    rows.sort(key=lambda r: r[0])
    for loss, code, hosts, rule, flips, order, shared, p_, x, args in rows[:a.show]:
        jf.report(x, args, f"{code}, rule {rule}, flips {'on' if flips else 'off'}, circle "
                           f"{'-'.join(order)}, junction spokes {shared}, m1 = {np.exp(p_[2]):.3g} fm, "
                           f"m3 = {p_[3]:.3f} fm")


if __name__ == "__main__":
    main()
