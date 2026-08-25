"""
Discrete sine-Gordon on the GRID (x, c) lattice -- breather + dimensionality test.

Tests two things at once (see work/focusing-from-phase.md, work/responsive-medium.md):

1) REDUCTION: the breather on a GENUINE DISCRETE lattice. The coupling term is the
   discrete Laplacian the impedance scatter produces in the continuum limit (the
   kinetic term GRID supplies); the on-site cosine is the compact-phase (ILN-line)
   potential. EOM (leapfrog):
       phi_tt = K (Lap_x phi + Lap_c phi) - m^2 sin(phi)
   x = extended (open ends), c = compact (periodic). Discreteness adds a
   Peierls-Nabarro barrier -> does the breather survive, and stay MOBILE?

2) DIMENSIONALITY (Derrick): a real-scalar breather is stable only in 1 EXTENDED
   dimension.
     --scn cuniform : breather localized in x, UNIFORM in c  -> effectively 1+1D
                      -> expect STABLE & MOBILE (compact c is not a 2nd extended dim)
     --scn clocal   : lump localized in x AND c              -> genuinely 2+1D
                      -> expect DISPERSE/decay (Derrick instability)

Diagnostics: x-width of the energy density, centroid/speed (mobility), energy drift,
and c-uniformity (to see clocal spreading in c).
"""
import argparse
import os
import numpy as np


def lap_open_x(f):
    l = np.zeros_like(f)
    l[1:-1, :] = f[2:, :] + f[:-2, :] - 2 * f[1:-1, :]
    return l


def lap_periodic_c(f):
    return np.roll(f, 1, 1) + np.roll(f, -1, 1) - 2 * f


def run(args):
    nx, nc = args.nx, args.nc
    xi = np.arange(nx) - nx // 2
    w = args.omega
    k = np.sqrt(max(1e-6, 1 - w ** 2))
    scale = args.m * k                                   # inverse breather width
    bx = 4 * np.arctan((k / w) / np.cosh(scale * xi))    # 1D breather profile in x

    phi = np.tile(bx[:, None], (1, nc)).astype(float)
    if args.scn == "clocal":                             # also localize in c (=> 2D lump)
        cc = np.arange(nc) - nc // 2
        cenv = np.exp(-(cc / max(2.0, nc / 6)) ** 2)[None, :]
        phi = phi * cenv
    phi_t = np.zeros_like(phi)
    if args.kx != 0.0:
        phi_t = -args.kx * np.gradient(phi, axis=0)      # x-momentum (mobility)
    phi_prev = phi - args.dt * phi_t

    damp = np.ones(nx); mm = 30
    ramp = np.linspace(0, 0.05, mm)
    damp[:mm] = 1 - ramp[::-1]; damp[-mm:] = 1 - ramp
    damp = damp[:, None]

    xw, cent, en, cunif = [], [], [], []
    for t in range(args.steps):
        lap = args.K * (lap_open_x(phi) + lap_periodic_c(phi))
        phi_next = 2 * phi - phi_prev + args.dt ** 2 * (lap - args.m ** 2 * np.sin(phi))
        phi_next *= damp
        pt = (phi_next - phi_prev) / (2 * args.dt)
        gx = lap_open_x(phi)  # cheap proxy grad^2 not needed; use energy below
        # energy density
        px = np.zeros_like(phi); px[1:-1] = (phi[2:] - phi[:-2]) / 2
        pc = (np.roll(phi, -1, 1) - np.roll(phi, 1, 1)) / 2
        dens = 0.5 * pt ** 2 + 0.5 * args.K * (px ** 2 + pc ** 2) + args.m ** 2 * (1 - np.cos(phi))
        prof = dens.sum(axis=1)                          # energy vs x (summed over c)
        tot = prof.sum() + 1e-30
        cx = (xi * prof).sum() / tot
        wx = np.sqrt(((xi - cx) ** 2 * prof).sum() / tot)
        xw.append(float(wx)); cent.append(float(cx)); en.append(float(dens.sum()))
        # c-uniformity: fraction of energy in c-varying part
        cprof = dens.sum(axis=0)
        cunif.append(float(1 - cprof.min() / (cprof.max() + 1e-30)))
        phi_prev, phi = phi, phi_next
    return dict(xw=np.array(xw), cent=np.array(cent), en=np.array(en),
                cunif=np.array(cunif), phi=phi)


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--scn", choices=["cuniform", "clocal"], default="cuniform")
    p.add_argument("--nx", type=int, default=400)
    p.add_argument("--nc", type=int, default=16)
    p.add_argument("--steps", type=int, default=5000)
    p.add_argument("--dt", type=float, default=0.05)
    p.add_argument("--K", type=float, default=1.0, help="edge coupling (from the scatter)")
    p.add_argument("--m", type=float, default=0.2, help="mass (compact-phase gap)")
    p.add_argument("--omega", type=float, default=0.6)
    p.add_argument("--kx", type=float, default=0.0, help="x-boost (mobility)")
    p.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "outputs"))
    p.add_argument("--tag", default="")
    args = p.parse_args()

    r = run(args)
    xw, ct, en, cu = r["xw"], r["cent"], r["en"], r["cunif"]
    a, b = int(0.15 * len(xw)), int(0.9 * len(xw))
    print(f"scn={args.scn}  nc={args.nc}  m={args.m}  omega={args.omega}  kx={args.kx}")
    print(f"  x-width: {xw[a]:.2f} -> {xw[b]:.2f}  (x{xw[b]/max(xw[a],1e-9):.2f})")
    speed = (ct[b] - ct[a]) / ((b - a) * args.dt)
    print(f"  centroid: {ct[a]:+.2f} -> {ct[b]:+.2f}   speed {speed:+.4f}")
    print(f"  c-nonuniformity: {cu[a]:.2f} -> {cu[b]:.2f}  (0=uniform in c)")
    print(f"  energy drift: {(en[a:b].max()-en[a:b].min())/(abs(en[a:b].mean())+1e-30)*100:.1f}%")
    grew = xw[b] / max(xw[a], 1e-9)
    verdict = "DISPERSES" if grew > 1.8 else "STABLE localized (breather!)"
    mob = "MOBILE" if abs(speed) > 0.05 else "at rest"
    print(f"  -> {verdict};  {mob}")

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        outdir = os.path.abspath(args.out); os.makedirs(outdir, exist_ok=True)
        fig, ax = plt.subplots(1, 2, figsize=(12, 4.4))
        ax[0].imshow(r["phi"].T, aspect="auto", origin="lower", cmap="twilight")
        ax[0].set_xlabel("x"); ax[0].set_ylabel("c"); ax[0].set_title(f"final phi ({args.scn})")
        ax[1].plot(xw, label="x-width"); ax[1].plot(cu, label="c-nonuniformity")
        ax[1].set_xlabel("t"); ax[1].legend(); ax[1].set_title("width & c-spread vs t")
        fig.tight_layout()
        tag = args.tag or f"{args.scn}_nc{args.nc}_k{args.kx}"
        png = os.path.join(outdir, f"dsg2d_{tag}.png")
        fig.savefig(png, dpi=110); print(f"  saved {png}")
    except Exception as e:
        print(f"  (plot skipped: {e})")


if __name__ == "__main__":
    main()
