"""
Switch-on of a constant source on the canonical GRID scatter in 3D
(validation step 4 for grid-gravity mechanism 3).

Question
--------
A static 1/r potential is a property of the lattice Laplacian; that is not in
doubt.  What is in doubt is whether the scatter's own DYNAMICS reach it: switch
a steady source on at t = 0 and ask whether the field behind the outgoing front
settles to the static 1/r, isotropically, with the front moving at the lattice
light speed c = 1/sqrt(3) -- or rings, drifts, or grows.

Which quantity is "the potential"
---------------------------------
The scatter is a first-order form of the wave equation.  A node's value
V = (2/N) sum(registers) behaves as a VELOCITY (like the voltage of an LC
network), and the link amplitudes carry the GRADIENT (the link currents).  The
carrier's potential q -- the quantity the local rate must follow -- is the
running sum of V:   q(node, t) = sum_{t' <= t} V(node, t').
For a steady monopole injection s into each of a node's N = 6 registers, the
network equations give      3 q_tt = lap(q) + 6 s      so the prediction is
    behind the front:  q(r) = 6 s / (4 pi r),   V = 0,   link flux ~ 1/r^2
    front:             r = t / sqrt(3).

What it does
------------
Cubic lattice n^3, 6 registers per node labeled by direction of travel,
canonical scatter out[d] = V - in[-d].  Source at the centre, switched on
smoothly over --ramp ticks.  Runs for fewer than n/2 ticks, so by strict
causality (one node per tick) the periodic boundary cannot influence anything.
Records q(t) at probe nodes along an axis, a face diagonal and a body diagonal,
and the final radial profile.

With --off T the source is switched off again at tick T: the potential should
then LEAVE as a wave (an outgoing "off" front), returning q to zero -- the
lossless form of "remove the load and the region relaxes".

Inputs:  --n (lattice size), --ramp, --probe-r (probe radius), --off, --plot
Outputs: printed tables; outputs/switch_on.png (or switch_on_off.png) with --plot.
"""
import argparse
import os
import numpy as np

OPP = [1, 0, 3, 2, 5, 4]                       # registers: +x -x +y -y +z -z
SHIFT = [(0, 1), (0, -1), (1, 1), (1, -1), (2, 1), (2, -1)]


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--n", type=int, default=161)
    p.add_argument("--ramp", type=int, default=12, help="ticks over which the source is switched on")
    p.add_argument("--probe-r", type=int, default=18, help="axis distance of the time-series probes")
    p.add_argument("--off", type=int, default=0,
                   help="if > 0, switch the source off again (smoothly) starting at this tick")
    p.add_argument("--plot", action="store_true")
    p.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "outputs"))
    args = p.parse_args()

    n, c0 = args.n, args.n // 2
    T = n // 2 - 2
    r = np.zeros((6, n, n, n), np.float32)
    q = np.zeros((n, n, n), np.float64)
    a = args.probe_r
    b = int(round(a / np.sqrt(2)))
    d = int(round(a / np.sqrt(3)))
    probes = {"axis": (c0 + a, c0, c0), "face diagonal": (c0 + b, c0 + b, c0),
              "body diagonal": (c0 + d, c0 + d, c0 + d)}
    series = {k: [] for k in probes}

    for t in range(T):
        s = 0.5 * (1 - np.cos(np.pi * min(t, args.ramp) / args.ramp))
        if args.off and t >= args.off:
            s *= 0.5 * (1 + np.cos(np.pi * min(t - args.off, args.ramp) / args.ramp))
        r[:, c0, c0, c0] += s
        V = r.sum(0) * (2.0 / 6.0)
        q += V
        new = np.empty_like(r)
        for dd in range(6):
            ax, sh = SHIFT[dd]
            new[dd] = np.roll(V - r[OPP[dd]], sh, axis=ax)
        r = new
        for k, idx in probes.items():
            series[k].append(q[idx])

    if args.off:
        print(f"n={n}  ticks={T}  source on at t=0, off at t={args.off} (ramps of {args.ramp} ticks)\n")
        print(f"{'direction':<16}{'peak q*r':>10}{'q*r at end':>12}{'residue / peak':>16}")
        for k, idx in probes.items():
            dist = np.sqrt(sum((np.array(idx) - c0) ** 2))
            y = np.array(series[k]) * dist
            print(f"{k:<16}{y.max():10.4f}{y[-1]:12.2e}{abs(y[-1]) / y.max():16.2e}")
        print(f"  (static value while on: 6/(4 pi) = {6 / (4 * np.pi):.4f}; off-front expected at the probes near "
              f"t = {args.off + args.ramp / 2 + a * np.sqrt(3):.0f})")
        if args.plot:
            import matplotlib
            matplotlib.use("Agg")
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots(figsize=(6.4, 4))
            for k, idx in probes.items():
                dist = np.sqrt(sum((np.array(idx) - c0) ** 2))
                ax.plot(np.array(series[k]) * dist, label=f"{k} (r={dist:.1f})")
            ax.axhline(6 / (4 * np.pi), color="k", ls=":")
            ax.set_xlabel("tick"); ax.set_ylabel("q * r"); ax.legend(fontsize=8)
            ax.set_title("source on, then off: the potential arrives, holds, and leaves")
            fig.tight_layout()
            os.makedirs(os.path.abspath(args.out), exist_ok=True)
            png = os.path.join(os.path.abspath(args.out), "switch_on_off.png")
            fig.savefig(png, dpi=110); print(f"\nsaved {png}")
        return

    # ---- final radial profile
    pred = 6.0 / (4 * np.pi)
    r_front = (T - args.ramp / 2) / np.sqrt(3)
    print(f"n={n}  ticks={T}  predicted front radius = {r_front:.1f}  predicted q*r = 6/(4 pi) = {pred:.4f}\n")
    print(f"{'r':>6}{'axis q*r':>12}{'face q*r':>12}{'body q*r':>12}{'spread':>10}")
    rows = []
    for rr in (3, 5, 8, 12, 16, 20, 25, 30, 35):
        if rr > 0.8 * r_front:
            continue
        i, j, k = rr, int(round(rr / np.sqrt(2))), int(round(rr / np.sqrt(3)))
        va = q[c0 + i, c0, c0] * i
        vf = q[c0 + j, c0 + j, c0] * (j * np.sqrt(2))
        vb = q[c0 + k, c0 + k, c0 + k] * (k * np.sqrt(3))
        rows.append((rr, va, vf, vb))
        print(f"{rr:6d}{va:12.4f}{vf:12.4f}{vb:12.4f}{(max(va, vf, vb) - min(va, vf, vb)) / pred:10.2%}")
    far = [x for x in rows if x[0] >= 8]
    mean = np.mean([v for row in far for v in row[1:]])
    print(f"\nmean q*r for r >= 8: {mean:.4f}   (prediction {pred:.4f}, ratio {mean / pred:.4f})")

    # ---- does the potential stay put once the front has passed?
    print(f"\nprobe time series at distance ~{a} (front expected at t = {a * np.sqrt(3) + args.ramp / 2:.0f}):")
    print(f"{'direction':<16}{'arrival (half height)':>22}{'implied speed':>15}{'q at end / pred':>17}{'drift, last 25%':>17}")
    for k, idx in probes.items():
        y = np.array(series[k])
        dist = np.sqrt(sum((np.array(idx) - c0) ** 2))
        final = y[-1]
        t_half = int(np.argmax(y >= 0.5 * final))
        tail = y[int(0.75 * T):]
        print(f"{k:<16}{t_half:22d}{dist / (t_half - args.ramp / 2):15.4f}"
              f"{final / (pred / dist):17.4f}{(tail.max() - tail.min()) / final:17.2%}")
    print(f"  (lattice light speed 1/sqrt(3) = {1 / np.sqrt(3):.4f})")

    # ---- V itself behind the front, and the link flux
    V = r.sum(0) * (2.0 / 6.0)
    x = np.arange(n) - c0
    R = np.sqrt(x[:, None, None] ** 2 + x[None, :, None] ** 2 + x[None, None, :] ** 2)
    inner = (R > 2) & (R < 0.5 * r_front)
    shell = (R > 0.8 * r_front) & (R < 1.2 * r_front)
    print(f"\nnode value V:  max|V| well behind the front = {np.abs(V[inner]).max():.2e}   "
          f"max|V| in the front shell = {np.abs(V[shell]).max():.2e}")
    print("radial link flux (+x register minus -x register) on the axis, times r^2:")
    for rr in (5, 10, 20, 30):
        if rr < 0.7 * r_front:
            flux = r[0, c0 + rr, c0, c0] - r[1, c0 + rr, c0, c0]
            print(f"   r={rr:3d}:  flux*r^2 = {flux * rr * rr:.4f}   (prediction 6/(4 pi) = {pred:.4f})")

    if args.plot:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
        for k, idx in probes.items():
            dist = np.sqrt(sum((np.array(idx) - c0) ** 2))
            ax[0].plot(np.array(series[k]) * dist, label=f"{k} (r={dist:.1f})")
        ax[0].axhline(pred, color="k", ls=":", label="6/(4 pi)")
        ax[0].set_xlabel("tick"); ax[0].set_ylabel("q * r"); ax[0].legend(fontsize=8)
        ax[0].set_title("the potential arrives, then stays")
        rr = np.arange(2, int(r_front * 1.3))
        ax[1].loglog(rr, [q[c0 + i, c0, c0] for i in rr], "o", ms=3, label="axis")
        ax[1].loglog(rr, pred / rr, "k:", label="6/(4 pi r)")
        ax[1].axvline(r_front, color="r", lw=0.8, label="front")
        ax[1].set_xlabel("r (nodes)"); ax[1].set_ylabel("q"); ax[1].legend(fontsize=8)
        ax[1].set_title("final radial profile")
        fig.tight_layout()
        os.makedirs(os.path.abspath(args.out), exist_ok=True)
        png = os.path.join(os.path.abspath(args.out), "switch_on.png")
        fig.savefig(png, dpi=110); print(f"\nsaved {png}")


if __name__ == "__main__":
    main()
