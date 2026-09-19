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

SCATTER CONVENTION (--scatter) — matters only for d >= 3 axes
-------------------------------------------------------------
Two update rules in this repo look alike and differ beyond two axes:

  canonical (default; grid-duality/models/scattering.md)
      registers are edge END-registers: out[d] = V - in[-d], then each edge
      swaps its two ends.  Dispersion, any d:   cos(Omega) = (sum_a cos k_a)/d
      Propagating band sits at Omega ~ 0, so the drive maps as Omega = omega.
      ISOTROPIC in any number of axes; one propagating branch.

  legacy
      registers labelled by DIRECTION OF TRAVEL: out[d] = V - in[d].  Exact
      dispersion, any d:      sum_a  1/(cos k_a - cos Omega) = 0
      Propagating band sits at omega ~ pi, so Omega = pi - omega.
      This reduces to the mean-of-cosines form ONLY for d = 2.  For d = 3 it is
      a quadratic in cos(Omega): ANISOTROPIC (c^2 = 2/3 on-axis, 1/2 and 1/6 on
      a face diagonal) and BIREFRINGENT off-axis.  Retained for reproducing the
      superseded three-axis runs; not recommended beyond two axes.

The two agree exactly for d = 2 (related by Omega <-> pi - omega), so every
two-axis result in this project is convention-independent.

The de Broglie wavelength is both (a) predicted analytically from the exact
dispersion above and (b) MEASURED from the field by FFT along x, in a separate
barrier-free calibration pass with a CW drive (--measure, on by default). The
measured value is convention-independent and is the check on the analytic one.

Impedance scatter S = (2/N)J - R, with R = identity (legacy) or the
end-swap permutation (canonical); x,y open with sponge edges; c periodic.
Output: accumulated |field|^2 along the detector line vs y (the pattern), a field
snapshot, analytic + measured in-plane lambda, fringe spacing, and (optionally)
single-lump clicks sampled from |field|^2 (whole-quantum, per grid-quantization).

NOTE on the snapshot: for a compact mode n >= 1 the field is proportional to
cos(2*pi*n*c/nc) along the compact axis, which SUMS TO ZERO over c.  The snapshot
is therefore PROJECTED onto the compact mode, not summed over it; summing returns
only floating-point noise for n >= 1.
"""
import argparse
import os
import numpy as np

# register order: 0:+x 1:-x 2:+y 3:-y 4:+c 5:-c ; REV swaps each +/- pair
REV = np.array([1, 0, 3, 2, 5, 4])


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


# ----------------------------------------------------------------- dispersion

def physical_omega(drive, scatter):
    """Physical band frequency Omega implied by a cos(drive*t) source."""
    return drive if scatter == "canonical" else np.pi - drive


def omega_of_k(ks, scatter):
    """Exact Omega for wavevector ks (list of per-axis k). None if no
    propagating root. Canonical: cos Omega = mean(cos k_a).  Legacy: the
    propagating root of sum_a 1/(cos k_a - cos Omega) = 0."""
    A = np.cos(np.asarray(ks, float))
    d = len(A)
    if scatter == "canonical":
        u = A.mean()
        return float(np.arccos(np.clip(u, -1, 1)))
    # legacy: roots of sum_a prod_{b!=a} (u - A_b) = 0
    s = np.poly1d([0.0])
    for a in range(d):
        q = np.poly1d([1.0])
        for b in range(d):
            if b != a:
                q = q * np.poly1d([1.0, -A[b]])
        s = s + q
    roots = [r.real for r in np.roots(s) if abs(r.imag) < 1e-9 and abs(r.real) <= 1.0]
    if not roots:
        return None
    # Drop u = +-1: those are Omega = 0 or pi, the flat non-propagating bands.
    # They appear as spurious degenerate roots whenever two axes share a k
    # (e.g. k = (0, 0, k_c), the rest-frequency case).
    prop = [r for r in roots if abs(abs(r) - 1.0) > 1e-9]
    if not prop:
        return float(np.arccos(np.clip(max(roots), -1, 1)))
    # legacy is multi-branch off-axis (birefringent); report the lowest-Omega
    # (largest cos Omega) branch, which is the one continuous with the band edge.
    return float(np.arccos(np.clip(max(prop), -1, 1)))


def kx_of_omega(Om, other_cos, scatter):
    """In-plane k_x at band frequency Om, given cos k of every OTHER axis.
    Returns (lambda, k_x) or None if evanescent / non-propagating."""
    if not (0 < Om < np.pi):
        return None
    C = np.cos(Om)
    d = len(other_cos) + 1
    if scatter == "canonical":
        coskx = d * C - float(np.sum(other_cos))
    else:
        den = 0.0
        for A in other_cos:
            if abs(A - C) < 1e-14:
                return None
            den += 1.0 / (A - C)
        if abs(den) < 1e-14:
            return None
        coskx = C - 1.0 / den
    if abs(coskx) > 1:
        return None                                    # evanescent (below gap)
    kx = float(np.arccos(coskx))
    return (2 * np.pi / kx, kx) if kx > 1e-12 else None


def rest_frequency(args):
    """Mass gap: Omega at k_x = k_y = 0 with the compact mode excited."""
    if args.nc <= 0 or args.nmode == 0:
        return 0.0
    kc = 2 * np.pi * args.nmode / args.nc
    return omega_of_k([0.0, 0.0, kc], args.scatter)


def debroglie_lambda(args, N):
    """Analytic in-plane (de Broglie) wavelength at the drive, on axis (k_y = 0)."""
    Om = physical_omega(args.omega, args.scatter)
    other = [1.0]                                       # cos k_y, k_y = 0
    if args.nc > 0:
        other.append(float(np.cos(2 * np.pi * args.nmode / args.nc)))
    return kx_of_omega(Om, other, args.scatter)


# ------------------------------------------------------------------ evolution

def run(args, slits=None, ny=None, steps=None, cw=False):
    """Evolve the lab. cw=True gives a ramped continuous drive and snapshots the
    final (steady-state) field; otherwise a Gaussian burst, snapshotted mid-run."""
    nx = args.nx
    ny = args.ny if ny is None else ny
    nc = args.nc
    slits = args.slits if slits is None else slits
    steps = args.steps if steps is None else steps
    compact = nc > 0
    N = 6 if compact else 4
    shape = (N, nx, ny, nc) if compact else (N, nx, ny)
    inn = np.zeros(shape)
    rev = REV[:N]

    # sponge (absorb) at the four open (x,y) edges
    m = 24
    ramp = np.linspace(0, 0.08, m)
    sx = np.ones(nx); sx[:m] = 1 - ramp[::-1]; sx[-m:] = 1 - ramp
    sy = np.ones(ny); sy[:m] = 1 - ramp[::-1]; sy[-m:] = 1 - ramp
    sponge = np.outer(sx, sy)                                  # (nx, ny)

    # barrier: 0 where blocked by mass, 1 where open GRID
    barrier = np.ones((nx, ny))
    if slits >= 1:
        cy = ny // 2
        openy = np.zeros(ny, bool)
        w = args.slit // 2
        if slits == 2:
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
    propagate = propagate_3d if compact else propagate_2d

    backdrop = np.zeros(ny)
    t0, wt, om = 40.0, 18.0, args.omega
    snap_at = steps - 1 if cw else int(0.62 * steps)
    snap = None
    for t in range(steps):
        T = inn.sum(0)
        out = (2.0 / N) * T[None, ...] - (inn[rev] if args.scatter == "canonical" else inn)
        inn = propagate(out)
        if cw:
            s_t = args.amp * min(1.0, t / 150.0) * np.cos(om * t)
        else:
            s_t = args.amp * np.exp(-((t - t0) / wt) ** 2) * np.cos(om * (t - t0))
        if compact:
            inn[0, args.xsrc, :, :] += s_t * cmode[None, :]    # broad +x wavefront, compact-mode
            inn *= barrier[None, :, :, None]
            inn *= sponge[None, :, :, None]
        else:
            inn[0, args.xsrc, :] += s_t
            inn *= barrier[None, :, :]
            inn *= sponge[None, :, :]
        if t > int(0.3 * steps):
            if compact:
                backdrop += np.sum(inn[:, args.xdet, :, :] ** 2, axis=(0, 2))
            else:
                backdrop += np.sum(inn[:, args.xdet, :] ** 2, axis=0)
        if t == snap_at:
            snap = inn.sum(0).copy()                           # field snapshot
    if compact:
        # PROJECT onto the compact mode. Summing over c annihilates n >= 1 exactly
        # (sum_c cos(2*pi*n*c/nc) = 0), leaving only float noise.
        norm = nc if args.nmode == 0 else nc / 2.0
        snap = (snap * cmode[None, None, :]).sum(axis=2) / norm
    return backdrop, snap, barrier, N


# ---------------------------------------------------------------- measurement

def fft_wavelength(fld, x0, x1, ycen, yhalf):
    """Dominant along-x wavelength of fld[(x0:x1), (ycen+-yhalf)], in nodes.
    Hann window + parabolic peak interpolation. Returns (lambda, half-bin
    resolution in lambda) or None."""
    x1 = min(x1, fld.shape[0]); y0 = max(0, ycen - yhalf); y1 = min(fld.shape[1], ycen + yhalf)
    if x1 - x0 < 32:
        return None
    strip = fld[x0:x1, y0:y1].mean(axis=1).astype(float)
    strip = strip - strip.mean()
    n = len(strip)
    if not np.isfinite(strip).all() or np.max(np.abs(strip)) < 1e-12:
        return None
    F = np.abs(np.fft.rfft(strip * np.hanning(n)))
    if len(F) < 4:
        return None
    i = int(np.argmax(F[1:])) + 1
    dlt = 0.0
    if 0 < i < len(F) - 1:
        den = F[i - 1] - 2 * F[i] + F[i + 1]
        if abs(den) > 1e-30:
            dlt = float(np.clip(0.5 * (F[i - 1] - F[i + 1]) / den, -0.5, 0.5))
    j = i + dlt
    if j <= 0:
        return None
    lam = n / j
    return lam, lam * lam / (2.0 * n)          # half-bin resolution in lambda


def measure_debroglie(args):
    """Barrier-free CW calibration pass -> measured in-plane lambda."""
    ny = max(64, 4 * args.slit)
    steps = args.calsteps
    _, snap, _, _ = run(args, slits=0, ny=ny, steps=steps, cw=True)
    x0 = args.xsrc + 110
    x1 = args.nx - 40
    return fft_wavelength(snap, x0, x1, ny // 2, 10)


# ------------------------------------------------------------------------ main

def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--nx", type=int, default=320)
    p.add_argument("--ny", type=int, default=320)
    p.add_argument("--nc", type=int, default=0,
                   help="compact c-axis size (0 = massless photon, N=4; >0 = N=6 with compact dim)")
    p.add_argument("--nmode", type=int, default=1,
                   help="compact mode n to excite when nc>0 (0 = massless c-uniform; >=1 = massive matter wave)")
    p.add_argument("--scatter", choices=["canonical", "legacy"], default="canonical",
                   help="scatter convention; differs only for d>=3 axes (see module docstring)")
    p.add_argument("--steps", type=int, default=700)
    p.add_argument("--calsteps", type=int, default=600,
                   help="steps for the barrier-free CW pass that MEASURES lambda")
    p.add_argument("--measure", dest="measure", action="store_true", default=True,
                   help="measure lambda by FFT in a barrier-free CW pass (default on)")
    p.add_argument("--no-measure", dest="measure", action="store_false")
    p.add_argument("--slits", type=int, choices=[0, 1, 2], default=2)
    p.add_argument("--xsrc", type=int, default=35)
    p.add_argument("--xbar", type=int, default=110)
    p.add_argument("--xdet", type=int, default=285)
    p.add_argument("--thick", type=int, default=3)
    p.add_argument("--slit", type=int, default=10, help="slit width (nodes)")
    p.add_argument("--sep", type=int, default=60, help="slit separation (centre-to-centre)")
    p.add_argument("--omega", type=float, default=0.4416,
                   help="literal drive frequency in cos(omega*t); physical Omega = omega "
                        "(canonical) or pi-omega (legacy)")
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
    Om = physical_omega(args.omega, args.scatter)
    print(f"slits={args.slits}  sep={args.sep}  slit={args.slit}  N={N}  "
          f"scatter={args.scatter}  ->  {kind}")
    print(f"  drive omega={args.omega:.4f}  ->  physical Omega={Om:.4f}  "
          f"(d={N // 2} axes; {'isotropic' if args.scatter == 'canonical' else 'ANISOTROPIC for d>=3'})")
    if args.nc > 0:
        kc = 2 * np.pi * args.nmode / args.nc
        w0 = rest_frequency(args)
        margin = (Om / w0 - 1) * 100 if w0 else float("inf")
        print(f"  compact: nc={args.nc}  k_c={kc:.4f}  rest freq omega_0={w0:.4f} "
              f"({'massless' if args.nmode == 0 else 'MASSIVE'}"
              + (f", drive {margin:.0f}% above gap)" if args.nmode else ")"))

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

    # fringe maxima and spacing. NOTE: >=3 maxima is NOT by itself proof of
    # two-slit interference -- single-slit diffraction also ripples. The
    # discriminator is the 1-slit vs 2-slit comparison, not this count.
    bb = b / (b.max() + 1e-30)
    peaks = np.where((bb[1:-1] > bb[:-2]) & (bb[1:-1] > bb[2:]) & (bb[1:-1] > 0.15))[0]
    print(f"  detector pattern: {len(peaks)} maxima above 0.15 "
          f"-> {'structured (compare 1-slit control)' if len(peaks) >= 3 else 'single lobe'}")
    if len(peaks) >= 2:
        print(f"  fringe spacing  ~ {float(np.mean(np.diff(peaks))):.1f} nodes")

    # in-plane (de Broglie) wavelength: analytic from the exact dispersion, and
    # measured by FFT. We do NOT fit lambda*L/d: wide slits on a lattice are not
    # paraxial, so absolute fringe spacing is reported as the empirical observable.
    dbl = debroglie_lambda(args, N)
    if dbl is not None:
        lam, kx = dbl
        print(f"  de Broglie lambda = {lam:.2f} nodes  (in-plane k_x={kx:.4f}; analytic, "
              f"{'massless' if args.nc == 0 or args.nmode == 0 else 'lengthened by mass'})")
    else:
        print("  de Broglie lambda: mode evanescent at this drive (below the mass gap)")
    if args.measure:
        mz = measure_debroglie(args)
        if mz is None:
            print("  measured lambda: no clean spectral peak")
        else:
            mlam, mres = mz
            agree = f", analytic off by {100 * (lam - mlam) / mlam:+.1f}%" if dbl else ""
            print(f"  measured lambda   = {mlam:.2f} +- {mres:.2f} nodes  "
                  f"(FFT, barrier-free CW pass{agree})")

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
        ax[0].set_title(f"field snapshot, {args.slits} slit(s) -- {kind}"
                        + (f"\n(projected onto compact mode n={args.nmode})" if args.nc > 0 else ""))
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
