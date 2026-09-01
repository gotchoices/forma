"""
Two-slit interference on a 2D GRID lab (Act 2, step 1).

GRID reading of the apparatus (Kyle's framing):
  * the lab is continuous GRID (2D S-space x,y with the impedance scatter);
  * a BARRIER is a region of nodes blocked by mass -> absorbs (field forced to 0);
  * a SLIT is open GRID -> photons transmit freely;
  * so a two-slit barrier is continuous GRID everywhere except two open channels.

A broad coherent wavefront is launched from the left, hits the barrier, and only
the two slits transmit. Question: do the two transmitted waves INTERFERE at the
backdrop (fringes), i.e. does information from BOTH slits reach each detector point?

  --slits 2 : two slits  -> expect interference fringes
  --slits 1 : one slit   -> control, single-slit diffraction (broad, no fringes)
  --slits 0 : no barrier -> control, uniform illumination

Impedance scatter S=(2/N)J-I, N=4 (edges +x,-x,+y,-y); x,y open with sponge edges.
Output: accumulated |field|^2 along the detector line vs y (the pattern), + a field
snapshot showing the wave passing through the slits.
"""
import argparse
import os
import numpy as np

N = 4


def propagate(out):
    inn = np.zeros_like(out)
    inn[0, 1:, :] = out[0, :-1, :]      # +x
    inn[1, :-1, :] = out[1, 1:, :]      # -x
    inn[2, :, 1:] = out[2, :, :-1]      # +y
    inn[3, :, :-1] = out[3, :, 1:]      # -y
    return inn


def run(args):
    nx, ny = args.nx, args.ny
    inn = np.zeros((N, nx, ny))

    # sponge (absorb) at all four edges
    m = 24
    ramp = np.linspace(0, 0.08, m)
    sx = np.ones(nx); sx[:m] = 1 - ramp[::-1]; sx[-m:] = 1 - ramp
    sy = np.ones(ny); sy[:m] = 1 - ramp[::-1]; sy[-m:] = 1 - ramp
    sponge = np.outer(sx, sy)

    # barrier: 0 where blocked by mass, 1 where open GRID
    barrier = np.ones((nx, ny))
    if args.slits >= 1:
        cy = ny // 2
        openy = np.zeros(ny, bool)
        w = args.slit // 2
        if args.slits == 2:
            s = args.sep // 2
            openy[cy - s - w:cy - s + w] = True      # slit 1
            openy[cy + s - w:cy + s + w] = True      # slit 2
        else:
            openy[cy - w:cy + w] = True              # single slit
        barrier[args.xbar - args.thick:args.xbar + args.thick, ~openy] = 0.0

    backdrop = np.zeros(ny)
    t0, wt, om = 40.0, 18.0, args.omega
    snap = None
    for t in range(args.steps):
        T = inn.sum(0)
        out = (2.0 / N) * T[None, :, :] - inn
        inn = propagate(out)
        s_t = args.amp * np.exp(-((t - t0) / wt) ** 2) * np.cos(om * (t - t0))
        inn[0, args.xsrc, :] += s_t                    # broad +x wavefront (illuminates both slits)
        inn *= barrier[None, :, :]                     # mass absorbs blocked nodes
        inn *= sponge[None, :, :]
        if t > int(0.3 * args.steps):
            backdrop += np.sum(inn[:, args.xdet, :] ** 2, axis=0)  # |field|^2 at detector
        if t == int(0.62 * args.steps):
            snap = np.sum(inn, axis=0).copy()          # field snapshot mid-run
    return backdrop, snap, barrier


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--nx", type=int, default=320)
    p.add_argument("--ny", type=int, default=320)
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
    p.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "outputs"))
    p.add_argument("--tag", default="")
    args = p.parse_args()

    bd, snap, barrier = run(args)
    y = np.arange(args.ny)
    interior = (y > 30) & (y < args.ny - 30)
    b = bd.copy(); b[~interior] = 0
    # count fringe maxima (interference signature)
    from numpy import diff, sign
    bb = b / (b.max() + 1e-30)
    peaks = np.where((bb[1:-1] > bb[:-2]) & (bb[1:-1] > bb[2:]) & (bb[1:-1] > 0.15))[0]
    print(f"slits={args.slits}  sep={args.sep}  slit={args.slit}")
    print(f"  detector pattern: {len(peaks)} maxima above 0.15 "
          f"-> {'INTERFERENCE FRINGES' if len(peaks) >= 3 else 'single lobe (no fringes)'}")
    if len(peaks) >= 2:
        sp = np.diff(peaks)
        print(f"  fringe spacing ~ {np.mean(sp):.1f} nodes (uniform => interference)")

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        outdir = os.path.abspath(args.out); os.makedirs(outdir, exist_ok=True)
        fig, ax = plt.subplots(1, 2, figsize=(12, 4.6))
        fld = snap.copy()
        fld[barrier == 0] = np.nan                     # show barrier as blank
        vmax = np.nanmax(np.abs(fld)) + 1e-30
        ax[0].imshow(fld.T, origin="lower", cmap="RdBu_r", vmin=-vmax, vmax=vmax, aspect="auto")
        ax[0].axvline(args.xdet, color="k", ls=":", lw=0.8)
        ax[0].set_title(f"field snapshot, {args.slits} slit(s) (barrier blank)")
        ax[0].set_xlabel("x"); ax[0].set_ylabel("y")
        ax[1].plot(bd, y)
        ax[1].set_xlabel("accumulated |field|^2"); ax[1].set_ylabel("y (detector)")
        ax[1].set_title("backdrop pattern")
        fig.tight_layout()
        tag = args.tag or f"{args.slits}slit"
        png = os.path.join(outdir, f"dualslit_{tag}.png")
        fig.savefig(png, dpi=110); print(f"  saved {png}")
    except Exception as e:
        print(f"  (plot skipped: {e})")


if __name__ == "__main__":
    main()
