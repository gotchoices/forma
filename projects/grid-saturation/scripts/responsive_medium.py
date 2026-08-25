"""
Responsive-medium (x, c) cylinder -- KNOB A: load-dependent propagation delay.

Direction/intent is recorded in work/responsive-medium.md -- READ IT FIRST. Short
version: the substrate reacts to what it carries (the Wheeler loop at the edge
level -- "traffic tells the edge how to curve; the curved edge tells traffic how
to move"). Two knobs map onto the two halves of the weak-field metric:
    Knob A  speed / propagation delay  <->  g_00 (time): a loaded edge runs slow
            = higher optical index. LOCAL. Gives Newtonian gravity + the self-dug,
            CO-MOVING well that should CONTAIN a particle (the mobile soliton the
            flat-band winding could not be). *** This script tests Knob A. ***
    Knob B  physical contraction       <->  g_ij (space): edges shorten, neighbours
            take up the slack, so it PROPAGATES as elastic strain (static Green's
            fn ~ 1/r) -- the long-range/gravity carrier. NOT in this script yet.

Knob A is implemented as an intensity-dependent PHASE (index) accrued per node per
tick: out_d *= exp(i * gA * rho), rho = local edge-energy density. This is exactly
"the edge's propagation delay rises with load," is the standard self-focusing
(Kerr / nonlinear-Schrodinger) operator, and being a pure phase it is EXACTLY
energy-conserving. Sign of gA selects focusing vs defocusing (swept, not assumed).

The make-or-break test (the thing the flat band failed): launch a moving x-packet
and ask -- does Knob A make it STOP DISPERSING (self-bind) while STILL MOVING
(mobile soliton)?  Refute if it disperses regardless, only binds when pinned, or
collapses with no stable window.

KNOB B (dynamical geometry / elastic strain) is now included. A SEPARATE real
field s(x,c) -- the strain (edge stretch/pinch) -- evolves as
    s += D*lap(s) + gB*rho - lamB*s
i.e. it is SOURCED by local load rho, SPREADS elastically via the Laplacian (so a
local deformation propagates to neighbours -- the non-local behaviour a mere phase
lacks), and RELAXES at rate lamB (lamB->0 = long-range/static, the gravity limit;
lamB>0 = screened/local). It back-reacts on the wave as an index well,
out *= exp(i*Bsign*s). The point vs Knob A: s is SLOW, ACCUMULATING and NON-LOCAL
(a photorefractive/thermal-soliton medium), so it can dig a persistent well that
the instantaneous local index (Knob A, which failed) could not. lap uses open x /
periodic c. See work/responsive-medium.md.

Scenarios (--scn):
  packet : a moving n=0 (c-uniform) complex wavepacket, source-launched.  [mobility]
  blob   : a stationary n=0 lump (all edges equal), in the interior -- disperses
           when linear; does Knob B dig a well and self-trap it?  [containment]
  wind   : a c-winding IC (to later combine with mechanism III).

Outputs: width(t) and centroid(t) of the packet -> does width grow (disperse) or
hold (bind), and does the centroid translate (mobile)? Plus a streak PNG.
"""
import argparse
import os
import numpy as np

N = 4  # +x, -x, +c, -c


def sponge_mask(nx, m):
    s = np.ones(nx)
    if m > 0:
        ramp = np.linspace(0.0, 0.12, m)
        s[:m] = 1.0 - ramp[::-1]
        s[-m:] = 1.0 - ramp
    return s


def propagate(out):
    inn = np.zeros_like(out)
    inn[0, 1:, :] = out[0, :-1, :]        # +x
    inn[1, :-1, :] = out[1, 1:, :]        # -x
    inn[2] = np.roll(out[2], +1, axis=1)  # +c
    inn[3] = np.roll(out[3], -1, axis=1)  # -c
    return inn


def lap2(f):
    """Discrete Laplacian: open x (zero-gradient ends), periodic c."""
    lx = np.zeros_like(f)
    lx[1:-1] = f[2:] + f[:-2] - 2 * f[1:-1]
    lc = np.roll(f, 1, 1) + np.roll(f, -1, 1) - 2 * f
    return lx + lc


def run(args):
    nx, nc = args.nx, args.nc
    inn = np.zeros((N, nx, nc), dtype=complex)
    spg = sponge_mask(nx, args.sponge)[:, None]
    xL = args.sponge + 30
    x = np.arange(nx)
    marg = args.sponge + 50

    # blob (stationary n=0 lump) IC
    if args.scn == "blob":
        env = np.exp(-((x - nx // 2) / args.width) ** 2)[:, None]
        for d in range(N):
            inn[d] = args.amp * env * np.ones((1, nc))

    strain = np.zeros((nx, nc))                              # KNOB B geometry field
    centroid, width, ienergy, streak, smax = [], [], [], [], []
    for t in range(args.steps):
        T = inn.sum(axis=0)
        out = (2.0 / N) * T[None, :, :] - inn
        rho = np.sum(np.abs(out) ** 2, axis=0)              # [Nx,Nc] local load
        if args.gA != 0.0:
            # KNOB A: instantaneous local index (pure phase, exactly conserving).
            out = out * np.exp(1j * args.gA * rho)[None, :, :]
        if args.gB != 0.0:
            # KNOB B: strain field -- sourced by load, spreads elastically, relaxes.
            strain += args.Dstrain * lap2(strain) + args.gB * rho - args.lamB * strain
            if args.Bmode == "phase":
                out = out * np.exp(1j * args.Bsign * strain)[None, :, :]  # index (phase vel)
                inn = propagate(out)
            else:  # "delay": high strain physically SLOWS TRANSIT (group velocity)
                h = np.clip(args.Bsign * strain, 0.0, 0.9)[None, :, :]     # held fraction
                inn = (1.0 - h) * propagate(out) + h * out                 # blend moved/stayed
        else:
            inn = propagate(out)
        # source: launch a right-moving c-uniform complex wavepacket, then off
        if args.scn == "packet":
            src = args.amp * np.exp(-((t - args.t0) / args.width) ** 2) \
                * np.exp(-1j * args.omega * (t - args.t0))
            inn[0, xL, :] += src
        elif args.scn == "wind" and t == 0:
            env = np.exp(-((x - nx // 2) / args.width) ** 2)[:, None]
            phase = np.exp(1j * 2 * np.pi * np.arange(nc) / nc)[None, :]
            for d in range(N):
                inn[d] = args.amp * env * phase
        inn *= spg

        U = np.sum(inn, axis=0)
        prof = np.abs(U).mean(axis=1)                        # c-averaged |field| vs x
        pin = prof.copy(); pin[:marg] = 0; pin[nx - marg:] = 0
        tot = pin.sum() + 1e-30
        cx = float((x * pin).sum() / tot)
        wx = float(np.sqrt(((x - cx) ** 2 * pin).sum() / tot))
        centroid.append(cx); width.append(wx); ienergy.append(float(tot))
        streak.append(prof.copy())
        smax.append(float(np.abs(strain).max()))

    return dict(centroid=np.array(centroid), width=np.array(width),
                ienergy=np.array(ienergy), streak=np.array(streak),
                smax=np.array(smax), strain_prof=strain.mean(axis=1))


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--nx", type=int, default=700)
    p.add_argument("--nc", type=int, default=24)
    p.add_argument("--steps", type=int, default=1200)
    p.add_argument("--scn", choices=["packet", "blob", "wind"], default="packet")
    p.add_argument("--gA", type=float, default=0.0, help="Knob A strength (signed); 0 = linear")
    p.add_argument("--gB", type=float, default=0.0, help="Knob B strain-source strength; 0 = off")
    p.add_argument("--Dstrain", type=float, default=0.15, help="Knob B elastic spread (<0.25 stable)")
    p.add_argument("--lamB", type=float, default=0.02, help="Knob B strain relaxation (0 = long-range/gravity)")
    p.add_argument("--Bsign", type=float, default=1.0, help="Knob B back-reaction sign (+1/-1)")
    p.add_argument("--Bmode", choices=["phase", "delay"], default="delay",
                   help="Knob B back-reaction: 'delay' = strain slows transit (geometric); 'phase' = index")
    p.add_argument("--amp", type=float, default=0.5)
    p.add_argument("--width", type=float, default=16.0, help="source/IC width")
    p.add_argument("--omega", type=float, default=0.5, help="carrier frequency (packet)")
    p.add_argument("--t0", type=float, default=60.0)
    p.add_argument("--sponge", type=int, default=40)
    p.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "outputs"))
    p.add_argument("--tag", default="")
    args = p.parse_args()

    r = run(args)
    cen, wid, ie = r["centroid"], r["width"], r["ienergy"]
    print(f"scenario={args.scn}  gA={args.gA}  amp={args.amp}  omega={args.omega}")

    # track the packet only while it is a real signal in the interior
    live = ie > 0.05 * ie.max()
    ts = np.where(live)[0]
    if len(ts) < 20:
        print("  (no sustained interior packet)"); return
    # measure across the clean stretch: centroid moving through the interior
    a, b = ts[len(ts) // 5], ts[-len(ts) // 6]           # skip launch and sponge-exit
    speed = (cen[b] - cen[a]) / (b - a)
    print(f"  centroid: x{cen[a]:.0f} (t{a}) -> x{cen[b]:.0f} (t{b})   speed {speed:+.3f} nodes/tick")
    print(f"  width:    {wid[a]:.1f} -> {wid[b]:.1f} nodes  "
          f"(x{wid[b]/max(wid[a],1e-9):.2f})  init source width {args.width:.0f}")
    verdict = ("DISPERSES" if wid[b] > 1.6 * wid[a] else
               ("collapses/blows up" if wid[b] < 0.4 * wid[a] and ie[b] > 3*ie[a] else
                "HOLDS (self-bound)"))
    mob = "MOBILE" if abs(speed) > 0.15 else "immobile"
    print(f"  -> {args.scn} {verdict};  {mob}")

    if args.gB != 0.0:
        sp = np.abs(r["strain_prof"])
        speak = sp.max() + 1e-30; sx = int(np.argmax(sp))
        half = np.where(sp > 0.5 * speak)[0]
        ext = (half.max() - half.min()) if len(half) > 1 else 0
        # tail: how far strain reaches above 10% of peak (the "gravity" reach)
        tail = np.where(sp > 0.1 * speak)[0]
        reach = (tail.max() - tail.min()) if len(tail) > 1 else 0
        print(f"  [knob B] strain well: peak|s|={speak:.3f} at x{sx}, fwhm~{ext} nodes, "
              f"10%-reach~{reach} nodes; max|s| over run={r['smax'].max():.3f}")

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        outdir = os.path.abspath(args.out); os.makedirs(outdir, exist_ok=True)
        fig, ax = plt.subplots(1, 2, figsize=(12, 4.4))
        st = r["streak"]; vmax = np.abs(st).max() + 1e-30
        ax[0].imshow(st, aspect="auto", origin="lower", cmap="magma", vmin=0, vmax=vmax,
                     extent=[0, args.nx, 0, args.steps])
        ax[0].set_xlabel("x"); ax[0].set_ylabel("t")
        ax[0].set_title(f"|field| (c-avg)  gA={args.gA}  (slope=speed, spread=dispersion)")
        ax[1].plot(wid, label="packet width")
        ax[1].plot(cen / cen.max() * wid.max(), "--", label="centroid (scaled)")
        ax[1].set_xlabel("t"); ax[1].set_title("width & centroid vs t"); ax[1].legend()
        fig.tight_layout()
        tag = args.tag or f"{args.scn}_gA{args.gA}"
        png = os.path.join(outdir, f"respmed_{tag}.png")
        fig.savefig(png, dpi=110); print(f"  saved {png}")
    except Exception as e:
        print(f"  (plot skipped: {e})")


if __name__ == "__main__":
    main()
