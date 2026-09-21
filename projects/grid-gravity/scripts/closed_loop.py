"""
Closed loop for grid-gravity mechanism 3 (validation step 5c, separate-channel
branch): two lumps source the deflection; the deflection loads the lattice; the
lumps respond.

What it does
------------
(x, c) lattice with node and space-link stores (gamma_test.py), now with the
store weights set DYNAMICALLY by a deflection field q(x, t):

    delay factor per member:   1 + q/2          (requirement R9)
    loading:                   K = (1 + q/2)^2 ;  node store Y = 8(K-1),
                                                  link store Z = 4(K-1)
    deflection:                q_tt = c^2 q_xx + g * |deflection rate|^2

The source is the node-rate energy of the waves present (the rest-mass form of
the source derived in work/action-and-gamma.md; valid for slow lumps).  The
packets are circulating compact modes, so the source is steady (no breathing).
The deflection's own propagation is a plain wave equation at the unloaded light
speed -- step 4 already showed the scatter carries it at light speed; to first
order in q the difference is negligible.

Two lumps of different mass are released at rest.  Nothing tells them to move.
Measured: each lump's trajectory; compared with Hamilton's ray equations applied
to the deflection the lumps actually produced (averaged over each lump):
    dk/dt = - d(w0)/dx = w0 * (q_x / 2) / (1 + q/2),     w0 = c0 k_c / (1 + q/2)
    dx/dt = c_x^2 k / w,      c_x^2 = c0^2 / K^2,  w^2 = c_x^2 k^2 + w0^2
(the second line matters: in 1D the uniform part of q grows steadily, which
slows every coordinate velocity a little without any force).  Also: the ratio
of the two accelerations (Newton's third law predicts the inverse mass ratio)
and the total wave momentum.

The two lumps are told apart by which side of the midpoint their energy lies
on, so they must stay well separated: a light, narrow packet spreads until its
tails cross the midpoint and the measured centroids are contaminated.  The
defaults (heavy mode, wide packet, large separation) avoid that.

One extended dimension only: the static deflection of a lump is then linear in
|x| (a constant pull) and its uniform part grows steadily -- properties of 1D,
not of the mechanism.  The run is kept short enough that q stays small.

Inputs: see --help.   Outputs: printed table; outputs/closed_loop.png (--plot).
"""
import argparse
import os
import numpy as np
from gamma_test import packet, step, C0SQ, IST


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--nx", type=int, default=8192)
    p.add_argument("--nc", type=int, default=32, help="compact circumference (sets the lump's rest frequency)")
    p.add_argument("--steps", type=int, default=7000)
    p.add_argument("--sep", type=int, default=1200, help="initial separation of the lumps (nodes)")
    p.add_argument("--m1", type=float, default=1.0, help="mass (norm) of the left lump")
    p.add_argument("--m2", type=float, default=3.0, help="mass (norm) of the right lump")
    p.add_argument("--sigma", type=float, default=100.0, help="packet width; wide + heavy keeps spreading small")
    p.add_argument("--g", type=float, default=2.0e-5, help="coupling of wave energy to the deflection")
    p.add_argument("--plot", action="store_true")
    p.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "outputs"))
    args = p.parse_args()

    nx, c0 = args.nx, args.nx // 2
    x = np.arange(nx, dtype=float)
    kc = 2 * np.pi / args.nc
    ph = np.exp(1j * kc)
    x1, x2 = c0 - args.sep // 2, c0 + args.sep // 2
    r = (np.sqrt(args.m1) * packet(nx, x1, 0.0, args.sigma, kc, 0.0, [0.0, 0.0]) +
         np.sqrt(args.m2) * packet(nx, x2, 0.0, args.sigma, kc, 0.0, [0.0, 0.0]))
    pos = np.vstack([np.tile(x, (5, 1)), np.tile(x + 0.5, (6, 1))])
    left = pos < c0

    q = np.zeros(nx); qdot = np.zeros(nx)
    spread = 1 - 3 * (np.sqrt(C0SQ) / (2 * args.sigma) / (np.sqrt(C0SQ) * kc)) ** 2   # momentum-spread factor
    T = args.steps
    rec = {k: [] for k in ("t", "x1", "x2", "f1", "f2", "c1", "c2", "w1", "w2", "norm", "qmax", "J1", "J2")}

    for t in range(T + 1):
        K = (1 + q / 2) ** 2
        Y = 8 * (K - 1)
        qm = 0.5 * (q + np.roll(q, -1))
        Zx = 4 * ((1 + qm / 2) ** 2 - 1)
        sy, sz = np.sqrt(Y), np.sqrt(Zx)
        V = 2 * (r[0] + r[1] + r[2] + r[3] + sy * r[IST]) / (4 + Y)
        S = np.abs(V) ** 2
        if t % 10 == 0:
            e = np.abs(r) ** 2
            eL, eR = np.where(left, e, 0), np.where(left, 0, e)
            en = e.sum(0)
            qx = (np.roll(q, -1) - np.roll(q, 1)) / 2
            w0 = np.sqrt(C0SQ) * kc / (1 + q / 2)
            frc = w0 * (qx / 2) / (1 + q / 2)                     # dk/dt
            cx2 = C0SQ / K ** 2
            mL, mR = np.where(x < c0, en, 0), np.where(x < c0, 0, en)
            rec["t"].append(t)
            rec["x1"].append((pos * eL).sum() / eL.sum()); rec["x2"].append((pos * eR).sum() / eR.sum())
            for i, mm in (("1", mL), ("2", mR)):
                rec["f" + i].append((frc * mm).sum() / mm.sum())
                rec["c" + i].append((cx2 * mm).sum() / mm.sum())
                rec["w" + i].append((w0 * mm).sum() / mm.sum())
            rec["norm"].append(e.sum()); rec["qmax"].append(q.max())
            rec["J1"].append(args.g * S[x < c0].sum()); rec["J2"].append(args.g * S[x >= c0].sum())
        # deflection: leapfrog wave equation, sourced by the node-rate energy
        qdot += C0SQ * (np.roll(q, -1) - 2 * q + np.roll(q, 1)) + args.g * S
        q += qdot
        r = step(r, Y, sy, Zx, sz, ph)

    for k in rec:
        rec[k] = np.array(rec[k], float)
    t = rec["t"]; dt = t[1] - t[0]
    pred = {}
    kray = {}
    for i in ("1", "2"):
        k = np.cumsum(rec["f" + i]) * dt
        v = rec["c" + i] * k / np.sqrt(rec["c" + i] * k ** 2 + rec["w" + i] ** 2) * spread
        pred[i] = np.cumsum(v) * dt
        kray[i] = k
    d1, d2 = rec["x1"] - rec["x1"][0], rec["x2"] - rec["x2"][0]
    late = t > (args.sep / np.sqrt(C0SQ)) * 1.3          # after each lump's field has reached the other
    a1 = 2 * np.polyfit(t[late], d1[late], 2)[0]; a2 = 2 * np.polyfit(t[late], d2[late], 2)[0]
    v1 = np.gradient(d1, dt); v2 = np.gradient(d2, dt)

    print(f"two lumps, masses {args.m1:g} and {args.m2:g}, released at rest {args.sep} nodes apart; "
          f"{T} ticks; coupling g = {args.g:g}")
    print(f"deflection stays small: max q = {rec['qmax'][-1]:.3f}   wave norm drift = "
          f"{rec['norm'][-1] / rec['norm'][0] - 1:+.1e}")
    print(f"source strengths  J1 = {rec['J1'].mean():.3e}   J2 = {rec['J2'].mean():.3e}   "
          f"J2/J1 = {rec['J2'].mean() / rec['J1'].mean():.3f}  (mass ratio {args.m2 / args.m1:.3f})\n")
    print(f"{'lump':<22}{'moved (sim)':>13}{'moved (ray law)':>17}{'sim/ray':>9}{'accel (late)':>15}")
    print(f"{'1 (mass %g), left' % args.m1:<22}{d1[-1]:13.2f}{pred['1'][-1]:17.2f}{d1[-1] / pred['1'][-1]:9.3f}{a1:15.3e}")
    print(f"{'2 (mass %g), right' % args.m2:<22}{d2[-1]:13.2f}{pred['2'][-1]:17.2f}{d2[-1] / pred['2'][-1]:9.3f}{a2:15.3e}")
    print(f"\nthey move TOWARD each other: lump 1 {'+' if d1[-1] > 0 else '-'}x, lump 2 {'+' if d2[-1] > 0 else '-'}x")
    print(f"acceleration ratio |a1/a2| = {abs(a1 / a2):.3f}    (third law predicts m2/m1 = {args.m2 / args.m1:.3f})")
    P1 = args.m1 * kray["1"][-1] / rec["w1"][-1]; P2 = args.m2 * kray["2"][-1] / rec["w2"][-1]
    print(f"wave momentum at end (mass x k / w):  lump 1 {P1:+.4e}   lump 2 {P2:+.4e}   "
          f"sum/size = {(P1 + P2) / abs(P1):+.3f}")

    if args.plot:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
        ax[0].plot(t, d1, label=f"lump 1 (mass {args.m1:g}), sim"); ax[0].plot(t, pred["1"], "k:", label="ray law")
        ax[0].plot(t, d2, label=f"lump 2 (mass {args.m2:g}), sim"); ax[0].plot(t, pred["2"], "k:")
        ax[0].set_xlabel("tick"); ax[0].set_ylabel("displacement (nodes)"); ax[0].legend(fontsize=8)
        ax[0].set_title("two lumps fall toward each other")
        ax[1].plot(x, q); ax[1].axvline(x1, color="C0", lw=0.7); ax[1].axvline(x2, color="C1", lw=0.7)
        ax[1].set_xlabel("x (nodes)"); ax[1].set_ylabel("deflection q at the end")
        ax[1].set_title("the deflection the lumps made")
        fig.tight_layout()
        os.makedirs(os.path.abspath(args.out), exist_ok=True)
        png = os.path.join(os.path.abspath(args.out), "closed_loop.png")
        fig.savefig(png, dpi=110); print(f"\nsaved {png}")


if __name__ == "__main__":
    main()
