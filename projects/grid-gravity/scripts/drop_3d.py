"""
3D drop test: a massive wave packet released at rest in the 1/r deflection of a
point source -- does it fall with acceleration ~ 1/r^2 ?

Why
---
Step 4 (switch_on.py) showed a source builds a 1/r deflection in 3D.  Steps 2-3
showed bodies accelerate along the gradient of the deflection (in one extended
dimension).  This run puts the two together directly: three extended dimensions,
a 1/r field, a body released at several distances.

What it does
------------
Canonical scatter on a cubic lattice (x, y, z) with a compact direction c carried
exactly by its Bloch phase (complex registers), and a node store of weight Y at
every node (work/uniform-q-theorem.md):
    registers  [+x -x +y -y +z -z +c -c store],   N = 8 links
    spectrum   cos w = (2 sum_a cos k_a + Y) / (8 + Y)
The deflection of a fixed point source is imposed,  q = A / sqrt(r^2 + soft^2),
with the linear-delay rule  1 + q/2  per member:   Y = 8 ((1 + q/2)^2 - 1).
(Node stores only: that is enough to test the falloff.  The link stores of step 3
change the light-bending coefficient, not the power law.)

A packet in the compact n=1 mode (a massive body) is built from exact
eigenvectors, released at rest at distance r0 from the source, and its energy
centroid tracked.  Compared with: Hamilton's ray equations for the exact local
spectrum, integrated in 3D; and the weak-field form  a = (c0^2/2) A / r^2.

Inputs:  --radii (list of r0), --A, --box, --steps, --sigma, --nc, --diag (also
         run one body-diagonal release), --plot
Outputs: printed table; fitted power law; outputs/drop_3d.png with --plot.
"""
import argparse
import os
import numpy as np

N = 8
OPP = [1, 0, 3, 2, 5, 4, 7, 6]


def local_freq(k, kc, Y):
    return np.arccos((2 * (np.cos(k[0]) + np.cos(k[1]) + np.cos(k[2]) + np.cos(kc)) + Y) / (N + Y))


def eigvec(k, kc, Y):
    sy = np.sqrt(Y)
    u = np.array([1.0] * 8 + [sy]) / np.sqrt(N + Y)
    X = np.zeros((9, 9))
    for a in range(4):
        X[2 * a, 2 * a + 1] = X[2 * a + 1, 2 * a] = 1.0
    X[8, 8] = 1.0
    S = 2 * np.outer(u, u) - X
    ph = [np.exp(-1j * k[0]), np.exp(1j * k[0]), np.exp(-1j * k[1]), np.exp(1j * k[1]),
          np.exp(-1j * k[2]), np.exp(1j * k[2]), np.exp(-1j * kc), np.exp(1j * kc), 1.0]
    lam, vec = np.linalg.eig(np.diag(ph) @ S)
    j = int(np.argmin(np.abs(lam - np.exp(-1j * local_freq(k, kc, Y)))))
    v = vec[:, j]
    return v * np.exp(-1j * np.angle(v[:8].sum() + sy * v[8])) / np.linalg.norm(v)


def make_packet(n, sigma, kc, Y0):
    ks = 2 * np.pi * np.fft.fftfreq(n)
    g1 = np.exp(-(ks * sigma) ** 2)
    idx = np.where(g1 > 1e-7)[0]
    spec = np.zeros((9, n, n, n), complex)
    shift = np.exp(-1j * ks * (n // 2))
    for i in idx:
        for j in idx:
            for l in idx:
                w = g1[i] * g1[j] * g1[l]
                if w < 1e-9:
                    continue
                spec[:, i, j, l] = w * shift[i] * shift[j] * shift[l] * eigvec((ks[i], ks[j], ks[l]), kc, Y0)
    r = np.fft.ifftn(spec, axes=(1, 2, 3))
    return r / np.sqrt((np.abs(r) ** 2).sum())


def step(r, Y, sy, ph):
    V = 2 * (r[:8].sum(0) + sy * r[8]) / (N + Y)
    new = np.empty_like(r)
    for d, (ax, sh) in enumerate([(0, 1), (0, -1), (1, 1), (1, -1), (2, 1), (2, -1)]):
        new[d] = np.roll(V - r[OPP[d]], sh, axis=ax)
    new[6] = (V - r[7]) * np.conj(ph)
    new[7] = (V - r[6]) * ph
    new[8] = sy * V - r[8]
    return new


def ray(x0, kc, Yfun, T):
    H = lambda x, k: local_freq(k, kc, Yfun(x))
    hx, hk = 1e-2, 1e-5
    E = np.eye(3)

    def f(s):
        x, k = s[:3], s[3:]
        dx = np.array([(H(x, k + hk * E[i]) - H(x, k - hk * E[i])) / (2 * hk) for i in range(3)])
        dk = -np.array([(H(x + hx * E[i], k) - H(x - hx * E[i], k)) / (2 * hx) for i in range(3)])
        return np.concatenate([dx, dk])
    s = np.concatenate([np.asarray(x0, float), np.zeros(3)])
    out = [s[:3].copy()]
    for _ in range(T):
        k1 = f(s); k2 = f(s + .5 * k1); k3 = f(s + .5 * k2); k4 = f(s + k3)
        s = s + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        out.append(s[:3].copy())
    return np.array(out)


def control(args):
    """Zero-field run: the packet's own field-independent centroid drift (a small
    construction artifact, ~3e-3 nodes), subtracted from every case."""
    n, c0 = args.box, args.box // 2
    kc = 2 * np.pi / args.nc
    g = np.arange(n) - c0
    X, Yc, Z = np.meshgrid(g, g, g, indexing="ij")
    Y = np.zeros((n, n, n)); r = make_packet(n, args.sigma, kc, 0.0); ph = np.exp(1j * kc)
    cen = []
    for t in range(args.steps + 1):
        e = (np.abs(r) ** 2).sum(0); tot = e.sum()
        cen.append([(X * e).sum() / tot, (Yc * e).sum() / tot, (Z * e).sum() / tot])
        r = step(r, Y, Y, ph)
    cen = np.array(cen)
    return cen - cen[0]


def run_case(args, src, ctrl):
    """Packet at the box centre; point source at position `src` (relative to the packet)."""
    n, c0 = args.box, args.box // 2
    kc = 2 * np.pi / args.nc
    g = np.arange(n) - c0
    X, Yc, Z = np.meshgrid(g, g, g, indexing="ij")
    Yfun = lambda x: 8 * ((1 + 0.5 * args.A / np.sqrt(((np.asarray(x) - src) ** 2).sum() + args.soft ** 2)) ** 2 - 1)
    R2 = (X - src[0]) ** 2 + (Yc - src[1]) ** 2 + (Z - src[2]) ** 2
    Y = 8 * ((1 + 0.5 * args.A / np.sqrt(R2 + args.soft ** 2)) ** 2 - 1)
    sy = np.sqrt(Y)
    r = make_packet(n, args.sigma, kc, float(Yfun(np.zeros(3))))
    ph = np.exp(1j * kc)
    cen = []
    for t in range(args.steps + 1):
        e = (np.abs(r) ** 2).sum(0)
        tot = e.sum()
        cen.append([(X * e).sum() / tot, (Yc * e).sum() / tot, (Z * e).sum() / tot])
        r = step(r, Y, sy, ph)
    cen = np.array(cen) - cen[0] - ctrl
    rhat = -src / np.linalg.norm(src)                         # unit vector source -> packet
    rad = -(cen @ rhat)                                       # displacement TOWARD the source
    xr = ray(np.zeros(3), kc, Yfun, args.steps)
    rad_ray = -(xr @ rhat)
    tt = np.arange(args.steps + 1.0)
    m = tt <= args.fit
    a_sim = 2 * np.polyfit(tt[m], rad[m], 2)[0]
    a_ray = 2 * np.polyfit(tt[m], rad_ray[m], 2)[0]
    side = np.abs(cen - np.outer(cen @ rhat, rhat)).max()
    return rad[-1], rad_ray[-1], a_sim, a_ray, side


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--radii", type=float, nargs="+", default=[24, 32, 40, 48, 64])
    p.add_argument("--A", type=float, default=0.3, help="deflection strength: q = A / r")
    p.add_argument("--soft", type=float, default=2.0)
    p.add_argument("--box", type=int, default=80)
    p.add_argument("--steps", type=int, default=160)
    p.add_argument("--fit", type=int, default=80, help="ticks used to fit the initial acceleration")
    p.add_argument("--sigma", type=float, default=7.0)
    p.add_argument("--nc", type=int, default=8)
    p.add_argument("--diag", action="store_true", help="also release on a body diagonal at the middle radius")
    p.add_argument("--plot", action="store_true")
    p.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "outputs"))
    args = p.parse_args()

    c0sq = 1.0 / 4.0
    kc = 2 * np.pi / args.nc
    spread = 1 - 2 * (1 / (2 * args.sigma) / kc) ** 2          # momentum-spread factor (node-only loading)
    print(f"3D drop: q = {args.A}/r, packet sigma={args.sigma}, compact n=1 with nc={args.nc}, "
          f"box {args.box}^3, {args.steps} ticks (fit over first {args.fit})")
    print(f"weak-field law: a = (c0^2/2) A / r^2 = {c0sq / 2 * args.A:.4f} / r^2;  "
          f"momentum-spread factor {spread:.4f}\n")
    print(f"{'r0':>6}{'direction':>12}{'fell (sim)':>12}{'fell (ray)':>12}{'sim/ray':>9}"
          f"{'a_sim':>12}{'a_sim/a_ray':>13}{'a_sim*r0^2':>12}{'sideways':>10}")
    ctrl = control(args)
    cases = [(r0, np.array([-r0, 0.0, 0.0]), "axis") for r0 in args.radii]
    if args.diag:
        rm = args.radii[len(args.radii) // 2]
        cases.append((rm, -rm / np.sqrt(3) * np.ones(3), "diagonal"))
    rows = []
    for r0, src, name in cases:
        d_sim, d_ray, a_sim, a_ray, side = run_case(args, src, ctrl)
        rows.append((r0, name, a_sim, a_ray))
        print(f"{r0:6.0f}{name:>12}{d_sim:12.4f}{d_ray * spread:12.4f}{d_sim / (d_ray * spread):9.4f}"
              f"{a_sim:12.4e}{a_sim / (a_ray * spread):13.4f}{a_sim * r0 * r0:12.5f}{side:10.1e}")
    ax_rows = [x for x in rows if x[1] == "axis"]
    rr = np.array([x[0] for x in ax_rows]); aa = np.array([x[2] for x in ax_rows])
    slope = np.polyfit(np.log(rr), np.log(aa), 1)[0]
    print(f"\npower law of the measured acceleration:  a ~ r^{slope:.3f}   (inverse square = -2)")
    w0 = local_freq((0, 0, 0), kc, 0.0)
    print(f"a*r^2 expected at large r: (c0^2/2) A x spread = {c0sq / 2 * args.A * spread:.5f} in the low-frequency "
          f"limit;\n  x 1/cos^2(w0/2) = {1 / np.cos(w0 / 2) ** 2:.4f} for this packet's rest frequency "
          f"(w0 = {w0:.3f}) -> {c0sq / 2 * args.A * spread / np.cos(w0 / 2) ** 2:.5f}")

    if args.plot:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(6, 4.2))
        ax.loglog(rr, aa, "o", label="simulation (on axis)")
        ax.loglog(rr, [x[3] * spread for x in ax_rows], "k-", lw=0.8, label="ray equations, exact spectrum")
        ax.loglog(rr, c0sq / 2 * args.A * spread / rr ** 2, "r:", label="(c0^2/2) A / r^2")
        for x in rows:
            if x[1] == "diagonal":
                ax.loglog([x[0]], [x[2]], "s", mfc="none", label="simulation (body diagonal)")
        ax.set_xlabel("distance from the source r (nodes)"); ax.set_ylabel("acceleration toward the source")
        ax.set_title(f"3D drop: fitted slope {slope:.3f}"); ax.legend(fontsize=8)
        fig.tight_layout()
        os.makedirs(os.path.abspath(args.out), exist_ok=True)
        png = os.path.join(os.path.abspath(args.out), "drop_3d.png")
        fig.savefig(png, dpi=110); print(f"\nsaved {png}")


if __name__ == "__main__":
    main()
