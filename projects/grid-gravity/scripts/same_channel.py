"""
Same-channel branch of grid-gravity mechanism 3 (validation steps 5c', 5d):
ONE real field on the lattice; gravity is its own zero-frequency part.

The rule, derived from the action
---------------------------------
State per node: deflection q and momentum P.  Node inertia and space-link
compliance both follow the linear-delay rule, the compact links are unloaded:
    M(q)  = (1 + q/2)^2            node inertia
    C(qb) = (1 + qb/2)^2           compliance of a space link, qb = mean of its ends
    H = sum P^2 / (2 M(q))  +  sum_x-links e^2 / (2 C(qb))  +  sum_c-links e^2 / 2
with e the link extension (difference of q across the link).  Hamilton's
equations give the rate v = P/M, the tension T = e/C, and the force
    dP/dt = (net tension) + (1/2) M'(q) v^2 + (1/4) sum_adjacent C'(qb) T^2 .
The last two terms are not added by hand: they are what the q-dependence of M and
C forces.  They are always positive, so an oscillating wave pushes its own
zero-frequency part upward in proportion to its energy -- rectification.  What is
carried through a change of M or C is P and e (the canonical variables), not the
stored energies.  There is NO free coupling constant.

What it does
------------
Two lumps (circulating compact modes) of different amplitude are released at
rest on an (x, c) lattice.  Each rectifies its own deflection; each should fall
toward the other on the ray law.  Reports energy conservation, the size of the
rectified deflection against the waves' own amplitude, the second-harmonic
content of the compact mode, the third law, and the momentum balance.

Inputs: see --help.   Outputs: printed tables; outputs/same_channel.png (--plot).
"""
import argparse
import os
import numpy as np


def force_energy(q, P):
    h = 1 + q / 2
    M = h * h
    v = P / M
    ex = np.roll(q, -1, 0) - q
    hb = 1 + (q + np.roll(q, -1, 0)) / 4
    Cx = hb * hb
    Tx = ex / Cx
    ec = np.roll(q, -1, 1) - q
    back = 0.25 * hb * Tx * Tx                                  # (1/4) C' T^2, per adjacent link
    F = (Tx - np.roll(Tx, 1, 0)) + (ec - np.roll(ec, 1, 1)) + 0.5 * h * v * v + back + np.roll(back, 1, 0)
    H = (P * v / 2).sum() + (ex * Tx / 2).sum() + (ec * ec / 2).sum()
    return F, M, H


def evolve(q, P, dt):
    F, _, _ = force_energy(q, P)
    P = P + 0.5 * dt * F
    q = q + dt * P / (1 + q / 2) ** 2
    F, _, _ = force_energy(q, P)
    P = P + 0.5 * dt * F
    return q, P


def lump(x, c, x0, A, sigma, kc, w0):
    """A lump in the compact n=1 mode, at rest in x, CIRCULATING around the ring:
    cos(kc c - w t), each x-wavenumber given its own frequency (so its source is steady)."""
    env = np.exp(-(x - x0) ** 2 / (2 * sigma ** 2))
    kx = 2 * np.pi * np.fft.fftfreq(x.size)
    wk = np.sqrt(w0 ** 2 + (2 * np.sin(kx / 2)) ** 2)
    wenv = np.fft.ifft(wk * np.fft.fft(env)).real
    return A * env[:, None] * np.cos(kc * c)[None, :], A * wenv[:, None] * np.sin(kc * c)[None, :]


def run_fall(args):
    nx, nc, dt = args.nx, args.nc, args.dt
    x = np.arange(nx, dtype=float); c = np.arange(nc, dtype=float)
    kc = 2 * np.pi / nc; w0 = 2 * np.sin(kc / 2); c0 = nx // 2
    x1, x2 = c0 - args.sep // 2, c0 + args.sep // 2
    A1, A2 = args.A, args.A * np.sqrt(args.ratio)
    q1, P1 = lump(x, c, x1, A1, args.sigma, kc, w0)
    q2, P2 = lump(x, c, x2, A2, args.sigma, kc, w0)
    q, P = q1 + q2, P1 + P2
    e1 = np.exp(-1j * kc * c)[None, :] * (2 / nc); e2 = np.exp(-2j * kc * c)[None, :] * (2 / nc)
    left = x < c0
    spread = 1 - 3 / (2 * args.sigma ** 2 * w0 ** 2)
    rec = {k: [] for k in ("t", "x1", "x2", "f1", "f2", "c1", "c2", "w1", "w2", "H", "qb", "h2", "m1", "m2")}
    nsteps = int(args.T / dt)
    for n in range(nsteps + 1):
        if n % 20 == 0:
            _, _, H = force_energy(q, P)
            a = (q * e1).sum(1); b = (P * e1).sum(1)
            rho = np.abs(b) ** 2 + w0 ** 2 * np.abs(a) ** 2       # energy density of the n=1 (lump) sector
            qb = q.mean(1)                                        # zero sector: the deflection
            qx = (np.roll(qb, -1) - np.roll(qb, 1)) / 2
            hh = 1 + qb / 2
            frc = w0 * (qx / 2) / hh ** 2                         # dk/dt = -d(w0/h)/dx
            rec["t"].append(n * dt); rec["H"].append(H); rec["qb"].append(qb.max())
            rec["h2"].append(np.abs((q * e2).sum(1)).max())
            for i, m in (("1", np.where(left, rho, 0)), ("2", np.where(left, 0, rho))):
                tot = m.sum()
                rec["x" + i].append((x * m).sum() / tot); rec["m" + i].append(tot)
                rec["f" + i].append((frc * m).sum() / tot)
                rec["c" + i].append((m / hh ** 4).sum() / tot)
                rec["w" + i].append((m * w0 / hh).sum() / tot)
        q, P = evolve(q, P, dt)
    for k in rec:
        rec[k] = np.array(rec[k], float)
    t = rec["t"]; d = t[1] - t[0]
    pred, kr = {}, {}
    for i in ("1", "2"):
        k = np.cumsum(rec["f" + i]) * d
        v = rec["c" + i] * k / np.sqrt(rec["c" + i] * k ** 2 + rec["w" + i] ** 2) * spread
        pred[i] = np.cumsum(v) * d; kr[i] = k
    d1, d2 = rec["x1"] - rec["x1"][0], rec["x2"] - rec["x2"][0]
    late = t > args.sep * 1.3
    a1 = 2 * np.polyfit(t[late], d1[late], 2)[0]; a2 = 2 * np.polyfit(t[late], d2[late], 2)[0]
    mr = rec["m2"][0] / rec["m1"][0]
    print(f"one field, no coupling constant.  two circulating lumps, amplitudes {A1:.2e} and {A2:.2e} "
          f"(energy ratio {mr:.3f}), {args.sep} nodes apart, T = {args.T:g}")
    print(f"energy conservation: drift of H = {rec['H'][-1] / rec['H'][0] - 1:+.2e}")
    print(f"rectified deflection reached q = {rec['qb'][-1]:.4f}  (the waves' own amplitude is {A2:.1e})")
    print(f"second harmonic of the compact mode: amplitude {rec['h2'].max():.2e}  "
          f"= {rec['h2'].max() / A2:.2e} of the fundamental\n")
    print(f"{'lump':<24}{'moved (sim)':>13}{'moved (ray law)':>17}{'sim/ray':>9}{'accel (late)':>14}")
    print(f"{'1 (lighter), left':<24}{d1[-1]:13.3f}{pred['1'][-1]:17.3f}{d1[-1] / pred['1'][-1]:9.3f}{a1:14.3e}")
    print(f"{'2 (heavier), right':<24}{d2[-1]:13.3f}{pred['2'][-1]:17.3f}{d2[-1] / pred['2'][-1]:9.3f}{a2:14.3e}")
    print(f"\nacceleration ratio |a1/a2| = {abs(a1 / a2):.3f}   (third law predicts the energy ratio {mr:.3f})")
    Pm1 = rec["m1"][-1] * kr["1"][-1] / rec["w1"][-1]; Pm2 = rec["m2"][-1] * kr["2"][-1] / rec["w2"][-1]
    print(f"wave momenta at end: {Pm1:+.4e}  {Pm2:+.4e}   sum/size = {(Pm1 + Pm2) / abs(Pm1):+.3f}")
    if args.plot:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
        ax[0].plot(t, d1, label="lighter lump, sim"); ax[0].plot(t, pred["1"], "k:", label="ray law")
        ax[0].plot(t, d2, label="heavier lump, sim"); ax[0].plot(t, pred["2"], "k:")
        ax[0].set_xlabel("time"); ax[0].set_ylabel("displacement (nodes)"); ax[0].legend(fontsize=8)
        ax[0].set_title("one field: two lumps fall into the deflection they rectify")
        ax[1].plot(x, q.mean(1)); ax[1].axvline(x1, color="C0", lw=0.7); ax[1].axvline(x2, color="C1", lw=0.7)
        ax[1].set_xlabel("x"); ax[1].set_ylabel("zero-frequency part of the field")
        ax[1].set_title("the rectified deflection")
        fig.tight_layout()
        os.makedirs(os.path.abspath(args.out), exist_ok=True)
        png = os.path.join(os.path.abspath(args.out), "same_channel.png")
        fig.savefig(png, dpi=110); print(f"\nsaved {png}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--nx", type=int, default=8192)
    p.add_argument("--nc", type=int, default=16)
    p.add_argument("--dt", type=float, default=0.5)
    p.add_argument("--T", type=float, default=3000.0)
    p.add_argument("--sep", type=int, default=1200)
    p.add_argument("--sigma", type=float, default=80.0)
    p.add_argument("--A", type=float, default=2.0e-3, help="amplitude of the lighter lump")
    p.add_argument("--ratio", type=float, default=3.0, help="energy ratio heavier / lighter")
    p.add_argument("--plot", action="store_true")
    p.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "outputs"))
    args = p.parse_args()
    run_fall(args)


if __name__ == "__main__":
    main()
