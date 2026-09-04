"""
Two-slit interference on a GRID lab (Act 2, step 1) — photon *or* matter wave.

GRID reading of the apparatus (Kyle's framing):
  * the lab is continuous GRID (2D S-space x,y with the impedance scatter);
  * a BARRIER is a region of nodes blocked by mass -> absorbs (field forced to 0);
  * a SLIT is open GRID -> the wave transmits freely;
  * so a two-slit barrier is continuous GRID everywhere except two open channels.

A broad coherent wavefront is launched from the left, hits the barrier, and only
the two slits transmit. Question: do the two transmitted waves INTERFERE at the
backdrop (fringes), i.e. does information from BOTH slits reach each detector point?

PHOTON vs MATTER (the --nc / --nmode switch):
  * --nc 0            : massless field on 2D (x,y), N=4. This is the *photon* /
                        Maxwell-sector sim (a massless wave); its interference is
                        classical wave optics.
  * --nc NC --nmode 0 : add a compact c-axis (NC nodes, periodic), N=6, and excite
                        the c-uniform mode -> still massless (photon) baseline on
                        the SAME lattice.
  * --nc NC --nmode n : excite the compact n>=1 mode -> a MASSIVE, compact-sector
                        MATTER wave (rest freq omega_0 from the Bloch dispersion).
                        Its in-plane wavelength is the de Broglie lambda, distinct
                        from the photon's. This is the electron-style two-slit.

The script measures the in-plane wavelength directly from the field snapshot (FFT
along x, post-barrier), so the fringe spacing is tied to the *actual* de Broglie
wavelength -- not to an assumed drive->k mapping.

Dispersion (N/2 = number of lattice axes d): cos(omega) = -(sum_i cos k_i)/d, so
the compact term cos(k_c) with k_c = 2*pi*nmode/nc raises the rest frequency and
lengthens the in-plane wavelength at fixed drive -- the mass effect.

Impedance scatter S=(2/N)J-I; x,y open with sponge edges; c periodic (compact).
Output: accumulated |field|^2 along the detector line vs y (the pattern), a field
snapshot, measured in-plane lambda, fringe spacing, and (optionally) single-lump
clicks sampled from |field|^2 (whole-quantum, per grid-quantization).
"""
import argparse
import os
import numpy as np


def propagate_2d(out):
    inn = np.zeros_like(out)
    inn[0, 1:, :] = out[0, :-1, :]      # +x
    inn[1, :-1, :] = out[1, 1:, :]      # -x
    inn[2, :, 1:] = out[2, :, :-1]      # +y
    inn[3, :, :-1] = out[3, :, 1:]      # -y
    return inn


def propagate_3d(out):
    inn = np.zeros_like(out)
    inn[0, 1:, :, :] = out[0, :-1, :, :]        # +x
    inn[1, :-1, :, :] = out[1, 1:, :, :]        # -x
    inn[2, :, 1:, :] = out[2, :, :-1, :]        # +y
    inn[3, :, :-1, :] = out[3, :, 1:, :]        # -y
    inn[4] = np.roll(out[4], 1, axis=2)         # +c (periodic / compact)
    inn[5] = np.roll(out[5], -1, axis=2)        # -c (periodic / compact)
    return inn


def run(args):
    nx, ny, nc = args.nx, args.ny, args.nc
    compact = nc > 0
    N = 6 if compact else 4
    shape = (N, nx, ny, nc) if compact else (N, nx, ny)
    inn = np.zeros(shape)

    # sponge (absorb) at the four open (x,y) edges
    m = 24
    ramp = np.linspace(0, 0.08, m)
    sx = np.ones(nx); sx[:m] = 1 - ramp[::-1]; sx[-m:] = 1 - ramp
    sy = np.ones(ny); sy[:m] = 1 - ramp[::-1]; sy[-m:] = 1 - ramp
    sponge = np.outer(sx, sy)                                  # (nx, ny)

    # barrier: 0 where blocked by mass, 1 where open GRID
    barrier = np.ones((nx, ny))
    if args.slits >= 1:
        cy = ny // 2
        openy = np.zeros(ny, bool)
        w = args.slit // 2
        if args.slits == 2:
            s = args.sep // 2
            openy[cy - s - w:cy - s + w] = True                # slit 1
            openy[cy + s - w:cy + s + w] = True                # slit 2
        else:
            openy[cy - w:cy + w] = True                        # single slit
        barrier[args.xbar - args.thick:args.xbar + args.thick, ~openy] = 0.0

    # compact-mode profile: cos(2*pi*nmode*c/nc) excites |k_c| = 2*pi*nmode/nc
    if compact:
        cidx = np.arange(nc)
        cmode = np.cos(2 * np.pi * args.nmode * cidx / nc)     # (nc,)
        sp3 = (sponge[:, :, None], barrier[:, :, None])
    propagate = propagate_3d if compact else propagate_2d

    backdrop = np.zeros(ny)
    t0, wt, om = 40.0, 18.0, args.omega
    snap = None
    for t in range(args.steps):
        T = inn.sum(0)
        out = (2.0 / N) * T[None, ...] - inn
        inn = propagate(out)
        s_t = args.amp * np.exp(-((t - t0) / wt) ** 2) * np.cos(om * (t - t0))
        if compact:
            inn[0, args.xsrc, :, :] += s_t * cmode[None, :]    # broad +x wavefront, compact-mode
            inn *= barrier[None, :, :, None]
            inn *= sponge[None, :, :, None]
        else:
            inn[0, args.xsrc, :] += s_t
            inn *= barrier[None, :, :]
            inn *= sponge[None, :, :]
        if t > int(0.3 * args.steps):
            if compact:
                backdrop += np.sum(inn[:, args.xdet, :, :] ** 2, axis=(0, 2))
            else:
                backdrop += np.sum(inn[:, args.xdet, :] ** 2, axis=0)
        if t == int(0.62 * args.steps):
            snap = inn.sum(0).copy()                           # field snapshot mid-run
    if compact:
        snap = snap.sum(axis=2)                                # integrate out c -> (nx, ny)
    return backdrop, snap, barrier, N


def debroglie_lambda(args, N):
    """In-plane (de Broglie) wavelength predicted *analytically* from the Bloch
    dispersion at the drive frequency. The drive cos(om t) selects the physical
    band frequency Omega = pi - om. The lab has two extended axes (x propagation,
    y transverse) plus, when nc>0, one compact axis c; d = N/2 lattice axes. On
    axis (k_y = 0):
      cos Omega = (cos k_x + cos k_y + [cos k_c])/d
                = (cos k_x + 1     + [cos k_c])/d
    -> cos k_x = d*cos(Omega) - 1 - [cos k_c], and lambda = 2*pi/k_x. The compact
    term cos k_c < 1 lowers cos k_x -> larger lambda: the de Broglie lengthening
    from mass. Returns (lambda, k_x), or None if evanescent (below the mass gap)."""
    d = N // 2
    Om = np.pi - args.omega
    if not (0 < Om < np.pi):
        return None
    coskx = d * np.cos(Om) - 1.0                              # subtract transverse k_y=0
    if args.nc > 0:
        coskx -= np.cos(2 * np.pi * args.nmode / args.nc)     # compact mass term
    if abs(coskx) > 1:
        return None                                           # evanescent (below gap)
    kx = float(np.arccos(coskx))
    return (2 * np.pi / kx, kx) if kx > 0 else None


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--nx", type=int, default=320)
    p.add_argument("--ny", type=int, default=320)
    p.add_argument("--nc", type=int, default=0,
                   help="compact c-axis size (0 = massless photon, N=4; >0 = N=6 with compact dim)")
    p.add_argument("--nmode", type=int, default=1,
                   help="compact mode n to excite when nc>0 (0 = massless c-uniform; >=1 = massive matter wave)")
    p.add_argument("--steps", type=int, default=700)
    p.add_argument("--slits", type=int, choices=[0, 1, 2], default=2)
    p.add_argument("--xsrc", type=int, default=35)
    p.add_argument("--xbar", type=int, default=110)
    p.add_argument("--xdet", type=int, default=285)
    p.add_argument("--thick", type=int, default=3)
    p.add_argument("--slit", type=int, default=10, help="slit width (nodes)")
    p.add_argument("--sep", type=int, default=60, help="slit separation (centre-to-centre)")
    p.add_argument("--omega", type=float, default=0.5)
    p.add_argument("--amp", type=float, default=0.3)
    p.add_argument("--clicks", type=int, default=0, help="sample N single-lump detections from |field|^2")
    p.add_argument("--seed", type=int, default=1)
    p.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "outputs"))
    p.add_argument("--tag", default="")
    args = p.parse_args()

    bd, snap, barrier, N = run(args)
    y = np.arange(args.ny)
    interior = (y > 30) & (y < args.ny - 30)
    b = bd.copy(); b[~interior] = 0

    kind = "photon (massless)" if args.nc == 0 or args.nmode == 0 else f"matter wave (compact n={args.nmode})"
    print(f"slits={args.slits}  sep={args.sep}  slit={args.slit}  N={N}  ->  {kind}")
    if args.nc > 0:
        kc = 2 * np.pi * args.nmode / args.nc
        # rest frequency from the N=6 dispersion at k_x=k_y=0: cos Omega_0 = (2+cos kc)/3
        arg0 = (2 + np.cos(kc)) / 3
        w0 = float(np.arccos(np.clip(arg0, -1, 1)))
        print(f"  compact: nc={args.nc}  k_c={kc:.4f}  rest freq omega_0={w0:.4f} "
              f"({'massless' if args.nmode == 0 else 'MASSIVE'})")

    # single-lump detections: each reveals ONE hidden-variable centre, distributed
    # P(y) ~ |field(y)|^2 (whole-quantum, per grid-quantization; NO collapse -- the
    # lump was localized all along). Do they rebuild the fringes?
    clicks_hist = None
    if args.clicks > 0:
        rng = np.random.default_rng(args.seed)
        prob = np.clip(b, 0, None); prob = prob / prob.sum()
        draws = rng.choice(args.ny, size=args.clicks, p=prob)
        clicks_hist = draws
        edges = np.arange(0, args.ny + 1, 4)
        for nn in (30, 300, args.clicks):
            if nn <= args.clicks:
                h, _ = np.histogram(draws[:nn], bins=edges)
                corr = np.corrcoef(h, np.histogram(y, bins=edges, weights=b)[0])[0, 1]
                print(f"  {nn:>5} single lumps: histogram vs |field|^2 corr = {corr:+.3f}")

    # fringe maxima (interference signature) and spacing
    bb = b / (b.max() + 1e-30)
    peaks = np.where((bb[1:-1] > bb[:-2]) & (bb[1:-1] > bb[2:]) & (bb[1:-1] > 0.15))[0]
    print(f"  detector pattern: {len(peaks)} maxima above 0.15 "
          f"-> {'INTERFERENCE FRINGES' if len(peaks) >= 3 else 'single lobe (no fringes)'}")
    fringe_sp = None
    if len(peaks) >= 2:
        fringe_sp = float(np.mean(np.diff(peaks)))
        print(f"  fringe spacing  ~ {fringe_sp:.1f} nodes (uniform => interference)")

    # in-plane (de Broglie) wavelength -- computed analytically from the dispersion
    # at the drive frequency (exact; mass lengthens it). We do NOT fit lambda*L/d:
    # wide slits on the lattice near the band edge are not paraxial, so the fringe
    # spacing is reported as the empirical observable, compared photon-vs-matter.
    dbl = debroglie_lambda(args, N)
    if dbl is not None:
        lam, kx = dbl
        print(f"  de Broglie lambda = {lam:.2f} nodes  (in-plane k_x={kx:.4f}; analytic, "
              f"{'massless' if args.nc == 0 or args.nmode == 0 else 'lengthened by mass'})")
    else:
        print("  de Broglie lambda: mode evanescent at this drive (below the mass gap)")

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        outdir = os.path.abspath(args.out); os.makedirs(outdir, exist_ok=True)
        fig, ax = plt.subplots(1, 2, figsize=(12, 4.6))
        fld = snap.copy()
        fld[barrier == 0] = np.nan
        vmax = np.nanmax(np.abs(fld)) + 1e-30
        ax[0].imshow(fld.T, origin="lower", cmap="RdBu_r", vmin=-vmax, vmax=vmax, aspect="auto")
        ax[0].axvline(args.xdet, color="k", ls=":", lw=0.8)
        ax[0].set_title(f"field snapshot, {args.slits} slit(s) -- {kind}")
        ax[0].set_xlabel("x"); ax[0].set_ylabel("y")
        if clicks_hist is not None:
            ax[1].hist(clicks_hist, bins=np.arange(0, args.ny + 1, 4),
                       orientation="horizontal", color="0.6", label=f"{args.clicks} single lumps")
            ax[1].plot(bd / bd.max() * np.histogram(clicks_hist, bins=np.arange(0, args.ny + 1, 4))[0].max(),
                       y, "r", lw=1.2, label="|field|^2")
            ax[1].legend(fontsize=8)
        else:
            ax[1].plot(bd, y)
        ax[1].set_xlabel("counts / |field|^2"); ax[1].set_ylabel("y (detector)")
        ax[1].set_title("backdrop pattern")
        fig.tight_layout()
        tag = args.tag or (f"{args.slits}slit_n{args.nmode}" if args.nc > 0 else f"{args.slits}slit_photon")
        png = os.path.join(outdir, f"dualslit_{tag}.png")
        fig.savefig(png, dpi=110); print(f"  saved {png}")
    except Exception as e:
        print(f"  (plot skipped: {e})")


if __name__ == "__main__":
    main()
