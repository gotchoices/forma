"""
Drop test and reflection test for grid-gravity mechanism 3 (validation step 2).

What it does
------------
Time-domain simulation of wave packets on the canonical GRID scatter over an
(x, c) lattice (x extended, c compact), where every node carries a storage
register of weight Y(x) (work/uniform-q-theorem.md).  The compact direction is
handled exactly by its Bloch phase, so the run is one-dimensional in x with
complex registers [+x, -x, +c, -c, store].

  --mode drop     Y(x) = Y0 + g (x - x0): a gentle uniform gradient of the
                  storage weight, i.e. of the local rate.  Packets are released
                  and their energy centroid is tracked.  Tested:
                    * packets at rest with different compact mode n (different
                      mass) -- do they all fall at the same acceleration?
                    * a moving massive packet and a photon -- do they follow
                      the ray (Hamilton) equations of the local dispersion?
                  Predictions:  low-frequency   a = g / (4+Y)^2   (= -c dc/dx)
                                exact lattice   a = g / (4+Y)^2 / cos^2(W0/2)
                  with W0 the packet's rest frequency.  The 1/cos^2 factor is
                  the lattice-scale departure from universality.
  --mode reflect  a photon packet crosses a ramp Y: Ya -> Yb of length Lr.
                  The reflected energy fraction is measured versus Lr and
                  compared with the step value ((n2-n1)/(n2+n1))^2,
                  n = sqrt(1+Y/4).

Inputs: see --help (all parameters have defaults).
Outputs: a printed table; outputs/drop_test.png (drop mode, with --plot).
"""
import argparse
import os
import numpy as np

N = 4  # links per node on the (x, c) lattice


def local_freq(kx, kc, Y):
    """Exact one-tick frequency of the loaded canonical scatter."""
    return np.arccos((2 * np.cos(kx) + 2 * np.cos(kc) + Y) / (N + Y))


def eigvec(kx, kc, Y):
    """Positive-frequency physical eigenvector of the one-tick operator at (kx, kc)."""
    n = N + 1
    sy = np.sqrt(Y)
    u = np.array([1, 1, 1, 1, sy]) / np.sqrt(N + Y)
    X = np.zeros((n, n))
    X[0, 1] = X[1, 0] = X[2, 3] = X[3, 2] = X[4, 4] = 1.0
    S = 2 * np.outer(u, u) - X
    P = np.diag([np.exp(-1j * kx), np.exp(1j * kx), np.exp(-1j * kc), np.exp(1j * kc), 1.0])
    lam, vec = np.linalg.eig(P @ S)
    j = int(np.argmin(np.abs(lam - np.exp(-1j * local_freq(kx, kc, Y)))))
    v = vec[:, j]
    ref = v[:4].sum() + sy * v[4]                       # fix the phase smoothly in k
    return v * np.exp(-1j * np.angle(ref)) / np.linalg.norm(v)


def make_packet(nx, x0, k0, sigma, kc, Y0):
    ks = 2 * np.pi * np.fft.fftfreq(nx)
    dk = (ks - k0 + np.pi) % (2 * np.pi) - np.pi
    G = np.exp(-(dk * sigma) ** 2)
    spec = np.zeros((N + 1, nx), complex)
    for i in np.where(G > 1e-10)[0]:
        spec[:, i] = G[i] * eigvec(ks[i], kc, Y0) * np.exp(-1j * ks[i] * x0)
    r = np.fft.ifft(spec, axis=1) * nx
    return r / np.sqrt((np.abs(r) ** 2).sum())


def step(r, Y, sy, ph):
    V = 2 * (r[0] + r[1] + r[2] + r[3] + sy * r[4]) / (N + Y)
    o0, o1, o2, o3 = V - r[1], V - r[0], V - r[3], V - r[2]   # out[d] = V - in[-d]
    a = sy * V - r[4]
    r[0] = np.roll(o0, 1)
    r[1] = np.roll(o1, -1)
    r[2] = o2 * np.conj(ph)
    r[3] = o3 * ph
    r[4] = a
    return r


def centroid(r, x):
    e = (np.abs(r) ** 2).sum(0)
    return float((x * e).sum() / e.sum()), e


def ray(x0, k0, kc, Yfun, T, dt=1.0):
    """Hamilton's equations for the exact local dispersion (RK4, numeric derivatives)."""
    H = lambda x, k: local_freq(k, kc, Yfun(x))
    hx, hk = 1e-3, 1e-5
    f = lambda s: np.array([(H(s[0], s[1] + hk) - H(s[0], s[1] - hk)) / (2 * hk),
                            -(H(s[0] + hx, s[1]) - H(s[0] - hx, s[1])) / (2 * hx)])
    s = np.array([x0, k0], float)
    xs = [x0]
    for _ in range(int(T / dt)):
        k1 = f(s); k2 = f(s + dt / 2 * k1); k3 = f(s + dt / 2 * k2); k4 = f(s + dt * k3)
        s = s + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        xs.append(s[0])
    return np.array(xs)


def run_drop(args):
    nx, x0 = args.nx, args.nx // 2
    x = np.arange(nx)
    Y = np.clip(args.Y0 + args.grad * (x - x0), 0, None)
    sy = np.sqrt(Y)
    Yfun = lambda xx: args.Y0 + args.grad * (xx - x0)
    a_ir = args.grad / (N + args.Y0) ** 2
    print(f"drop test: Y(x) = {args.Y0} + {args.grad:g}(x-x0), nx={nx}, steps={args.steps}, "
          f"packet sigma={args.sigma}")
    print(f"low-frequency prediction a = g/(4+Y)^2 = {a_ir:.4e} nodes/tick^2 (toward larger Y)\n")
    print(f"{'packet':<26}{'W0':>8}{'a_sim':>12}{'a_exact':>12}{'sim/exact':>10}{'sim/IR':>9}")
    curves = []
    cases = [(f"rest, n={n}", n, 0.0) for n in args.modes]
    for label, n, k0 in cases:
        kc = 2 * np.pi * n / args.nc
        ph = np.exp(1j * kc)
        r = make_packet(nx, x0, k0, args.sigma, kc, args.Y0)
        ts, xs = [], []
        for t in range(args.steps + 1):
            if t % args.every == 0:
                ts.append(t); xs.append(centroid(r, x)[0])
            r = step(r, Y, sy, ph)
        ts, xs = np.array(ts, float), np.array(xs)
        a_sim = 2 * np.polyfit(ts, xs - x0, 2)[0]
        W0 = local_freq(0.0, kc, args.Y0)
        a_ex = a_ir / np.cos(W0 / 2) ** 2
        print(f"{label:<26}{W0:8.4f}{a_sim:12.4e}{a_ex:12.4e}{a_sim / a_ex:10.4f}{a_sim / a_ir:9.4f}")
        curves.append((label, ts, xs - x0))

    # Moving packets: deflection = (run with gradient) - (control run without), so the
    # packet's own mean velocity and spreading cancel.  Run length is capped so the
    # packet stays clear of the periodic wrap.
    print(f"\n{'moving packet':<26}{'v0':>8}{'ticks':>7}{'defl_sim':>12}{'defl_ray':>12}{'sim/ray':>10}")
    Yflat = np.full(nx, args.Y0); syflat = np.sqrt(Yflat)
    for label, n, k0 in [("massive n=1, k0=%.2f" % args.kmove, 1, args.kmove),
                         ("photon, k0=%.2f" % args.kphot, 0, args.kphot)]:
        kc = 2 * np.pi * n / args.nc
        ph = np.exp(1j * kc)
        v0 = (local_freq(k0 + 1e-5, kc, args.Y0) - local_freq(k0 - 1e-5, kc, args.Y0)) / 2e-5
        T = int(min(args.steps, 0.35 * nx / v0))
        rg = make_packet(nx, x0, k0, args.sigma, kc, args.Y0); rf = rg.copy()
        dx = []
        for t in range(T + 1):
            dx.append(centroid(rg, x)[0] - centroid(rf, x)[0])
            rg = step(rg, Y, sy, ph); rf = step(rf, Yflat, syflat, ph)
        dx = np.array(dx)
        d_ray = ray(x0, k0, kc, Yfun, T)[-1] - ray(x0, k0, kc, lambda xx: args.Y0, T)[-1]
        print(f"{label:<26}{v0:8.4f}{T:7d}{dx[-1]:12.3f}{d_ray:12.3f}{dx[-1] / d_ray:10.4f}")
        curves.append((label + " (minus control)", np.arange(T + 1.0), dx))

    if args.plot:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(7, 4.4))
        for label, ts, dx in curves:
            ax.plot(ts, dx, label=label)
        tt = np.linspace(0, args.steps, 50)
        ax.plot(tt, 0.5 * a_ir * tt ** 2, "k:", label="(1/2) a t^2, low-frequency a")
        ax.set_xlabel("tick"); ax.set_ylabel("displacement toward larger Y (nodes)")
        ax.set_title("drop test: packets in a uniform gradient of the storage weight")
        ax.legend(fontsize=7)
        fig.tight_layout()
        os.makedirs(os.path.abspath(args.out), exist_ok=True)
        png = os.path.join(os.path.abspath(args.out), "drop_test.png")
        fig.savefig(png, dpi=110); print(f"\nsaved {png}")


def run_reflect(args):
    nx = args.nx
    x = np.arange(nx)
    xs0, xr0 = nx // 5, nx // 2
    n1, n2 = np.sqrt(1 + args.Ya / N), np.sqrt(1 + args.Yb / N)
    R_step = ((n2 - n1) / (n2 + n1)) ** 2
    lam = 2 * np.pi / args.kphot
    print(f"reflection test: photon k0={args.kphot} (wavelength {lam:.1f} nodes), "
          f"Y: {args.Ya} -> {args.Yb}, step prediction R = {R_step:.5f}\n")
    print(f"{'ramp length':>12}{'Lr/wavelength':>15}{'R measured':>13}{'R / R_step':>12}{'energy drift':>14}")
    for Lr in args.ramps:
        if Lr == 0:
            Y = np.where(x < xr0, args.Ya, args.Yb).astype(float)
        else:
            Y = args.Ya + (args.Yb - args.Ya) * np.clip((x - (xr0 - Lr / 2)) / Lr, 0, 1)
        sy = np.sqrt(Y)
        r = make_packet(nx, xs0, args.kphot, args.sigma, 0.0, args.Ya)
        e0 = (np.abs(r) ** 2).sum()
        c1 = (local_freq(args.kphot + 1e-5, 0, args.Ya) - local_freq(args.kphot - 1e-5, 0, args.Ya)) / 2e-5
        steps = int((xr0 - xs0) / c1 * 1.75)
        for _ in range(steps):
            r = step(r, Y, sy, 1.0)
        e = (np.abs(r) ** 2).sum(0)
        R = e[: int(xr0 - Lr / 2 - 2 * args.sigma)].sum() / e.sum()
        print(f"{Lr:12d}{Lr / lam:15.2f}{R:13.3e}{R / R_step:12.4f}{e.sum() / e0 - 1:14.1e}")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--mode", choices=["drop", "reflect"], default="drop")
    p.add_argument("--nx", type=int, default=4096)
    p.add_argument("--nc", type=int, default=32, help="compact circumference (nodes)")
    p.add_argument("--steps", type=int, default=4000)
    p.add_argument("--every", type=int, default=20)
    p.add_argument("--sigma", type=float, default=60.0, help="packet width parameter (nodes)")
    p.add_argument("--Y0", type=float, default=1.0)
    p.add_argument("--grad", type=float, default=1e-4, help="dY/dx")
    p.add_argument("--modes", type=int, nargs="+", default=[1, 2, 3], help="compact mode numbers dropped from rest")
    p.add_argument("--kmove", type=float, default=0.10)
    p.add_argument("--kphot", type=float, default=0.30)
    p.add_argument("--Ya", type=float, default=0.0)
    p.add_argument("--Yb", type=float, default=2.0)
    p.add_argument("--ramps", type=int, nargs="+", default=[0, 8, 32, 128, 512])
    p.add_argument("--plot", action="store_true")
    p.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "outputs"))
    args = p.parse_args()
    run_drop(args) if args.mode == "drop" else run_reflect(args)


if __name__ == "__main__":
    main()
