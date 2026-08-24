"""
(x, c) cylinder saturation sim for projects/grid-saturation.

A minimal GRID testbed: 1D space x (the axis) x 1D compact c (the
circumference, periodic), on a square lattice with the equal-impedance
scatter S = (2/N)J - I, N = 4. Directed edge amplitudes in[d], d in
{+x,-x,+c,-c}; per tick: scatter at each node, then propagate to neighbours
(x open with sponge ends; c periodic).

  photon  = a c-UNIFORM (n=0) wave propagating in x.
  mass    = a c-WINDING (n>=1) mode.

Milestones this script targets:
  M1 (--sat none): confirm a photon propagates in x and two photons PASS
     THROUGH each other, energy staying in n=0 (the KK-decoupling baseline,
     never tested dynamically in forma).
  M2 (--sat clip|spillover): drive two photons HEAD-ON into saturation and
     watch whether energy transfers n=0 -> n>=1 (photon -> compact mode) --
     energy entering the compact dimension (the pair-production signal).

Open-by-design knobs (per the project brief -- stay agnostic):
  --bound     saturation magnitude (base-2 => 1.0; 8-bit => e.g. 127).
  --quantize  optional discrete levels across [-bound,bound] (0 = continuous).
  --sat       none | clip (lossy) | spillover (overflow on a saturated edge
              is redistributed to edges with headroom; energy is TRACKED,
              not assumed -- a first model, to be validated).

Scenarios: --scn single | headon | winding.

Outputs: printed diagnostics (energy conservation; E(n0) vs E(n>=1)) and a
PNG (space-time streak of the c-averaged field + energy-partition time
series).
"""
import argparse
import os
import numpy as np

N = 4  # +x, -x, +c, -c


def sponge_mask(nx, m):
    """Damping ramp near both x-ends to absorb outgoing waves (1 in interior)."""
    s = np.ones(nx)
    if m > 0:
        ramp = np.linspace(0.0, 0.12, m)
        s[:m] = 1.0 - ramp[::-1]
        s[-m:] = 1.0 - ramp
    return s


def propagate(out):
    """out[d] leaving in direction d -> in_new[d] at the forward neighbour.
    x open (zero-fill); c periodic (roll)."""
    inn = np.zeros_like(out)
    inn[0, 1:, :] = out[0, :-1, :]      # +x
    inn[1, :-1, :] = out[1, 1:, :]      # -x
    inn[2] = np.roll(out[2], +1, axis=1)  # +c
    inn[3] = np.roll(out[3], -1, axis=1)  # -c
    return inn


def saturate(out, mode, bound, levels):
    """Apply the edge bound to outgoing amplitudes. Returns (out, lost_energy)."""
    if mode == "none" and not levels:
        return out, 0.0
    e0 = float(np.sum(out ** 2))
    if mode == "clip":
        out = np.clip(out, -bound, bound)
    elif mode == "spillover":
        clipped = np.clip(out, -bound, bound)
        net = np.sum(out - clipped, axis=0)              # [Nx,Nc] net overflow
        # signed headroom available in the direction of `net`, per edge
        sgn = np.sign(net)[None, :, :]
        room = np.clip((bound * sgn - clipped) * sgn, 0.0, None)  # >=0 magnitude
        room_tot = np.sum(room, axis=0) + 1e-12
        add = (room / room_tot[None]) * (np.abs(net)[None]) * sgn
        out = np.clip(clipped + add, -bound, bound)
    if levels and levels > 1:
        step = bound / (levels // 2)
        out = np.round(out / step) * step
    return out, e0 - float(np.sum(out ** 2))


def mode_energy(inn):
    """Split node-field energy into n=0 (c-uniform, 'photon') and n>=1
    (c-varying, 'mass'). U = sum_d in[d]."""
    U = np.sum(inn, axis=0)                     # [Nx,Nc]
    dc = U.mean(axis=1, keepdims=True)          # c-average per x
    e_n0 = float(np.sum(dc ** 2) * U.shape[1])  # DC energy
    e_ge1 = float(np.sum((U - dc) ** 2))        # AC energy
    return e_n0, e_ge1, U


def source(t, t0, w, omega, amp):
    return amp * np.exp(-((t - t0) / w) ** 2) * np.cos(omega * (t - t0))


def run(args):
    nx, nc = args.nx, args.nc
    inn = np.zeros((N, nx, nc))
    spg = sponge_mask(nx, args.sponge)[:, None]
    xL, xR = args.sponge + 30, nx - args.sponge - 30
    w, om, amp = args.width, args.omega, args.amp

    E_edge, E_n0, E_ge1, Ex, Ec, streak, lost = [], [], [], [], [], [], 0.0
    for t in range(args.steps):
        T = inn.sum(axis=0)
        out = (2.0 / N) * T[None, :, :] - inn         # scatter, all dirs
        out, dl = saturate(out, args.sat, args.bound, args.quantize)
        lost += dl
        inn = propagate(out)
        # inject sources (uniform in c => n=0 photons), after propagation
        s = source(t, args.t0, w, om, amp)
        # optional c-symmetry-breaking seed (needed for a c-structured particle)
        cprof = 1.0 + args.cseed * np.cos(2 * np.pi * np.arange(nc) / nc)
        if args.scn in ("single", "headon"):
            inn[0, xL, :] += s * cprof                 # +x photon from left
        if args.scn == "headon":
            inn[1, xR, :] += s * cprof                 # -x photon from right
        if args.scn == "winding":                      # n=1 test excitation
            prof = np.cos(2 * np.pi * np.arange(nc) / nc)
            inn[0, xL, :] += s * prof
        inn *= spg                                     # absorb at x-ends

        e0, e1, U = mode_energy(inn)
        E_edge.append(float(np.sum(inn ** 2)))         # CONSERVED edge energy
        E_n0.append(e0); E_ge1.append(e1)
        Ex.append(float(np.sum(inn[0] ** 2 + inn[1] ** 2)))   # x-directed (photon)
        Ec.append(float(np.sum(inn[2] ** 2 + inn[3] ** 2)))   # c-directed (compact circulation)
        streak.append(U.mean(axis=1).copy())           # c-averaged field vs x

    return dict(E_edge=np.array(E_edge), E_n0=np.array(E_n0),
                E_ge1=np.array(E_ge1), Ex=np.array(Ex), Ec=np.array(Ec),
                streak=np.array(streak), lost=lost)


def prop_speed(streak, t_lo, t_hi):
    """Estimate x-speed of the pulse from the argmax of |c-averaged field|."""
    xs = np.array([np.argmax(np.abs(streak[t])) for t in range(t_lo, t_hi)])
    ts = np.arange(t_lo, t_hi)
    good = (xs > 2) & (xs < streak.shape[1] - 2)
    if good.sum() < 5:
        return float("nan")
    return float(np.polyfit(ts[good], xs[good], 1)[0])


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--nx", type=int, default=600)
    p.add_argument("--nc", type=int, default=24)
    p.add_argument("--steps", type=int, default=900)
    p.add_argument("--sat", choices=["none", "clip", "spillover"], default="none")
    p.add_argument("--bound", type=float, default=1.0)
    p.add_argument("--quantize", type=int, default=0)
    p.add_argument("--scn", choices=["single", "headon", "winding"], default="single")
    p.add_argument("--amp", type=float, default=0.2)
    p.add_argument("--width", type=float, default=18.0)
    p.add_argument("--omega", type=float, default=0.5)
    p.add_argument("--t0", type=float, default=70.0)
    p.add_argument("--sponge", type=int, default=40)
    p.add_argument("--cseed", type=float, default=0.0,
                   help="c-symmetry-breaking seed on the injected photons (0 = perfectly c-uniform)")
    p.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "outputs"))
    p.add_argument("--tag", default="")
    args = p.parse_args()

    r = run(args)
    Ee, e0, e1 = r["E_edge"], r["E_n0"], r["E_ge1"]
    peak = Ee.max() + 1e-30
    lo, hi = int(0.20 * len(Ee)), int(0.55 * len(Ee))   # pulse in interior
    seg = Ee[lo:hi]
    speed = prop_speed(r["streak"], lo, hi)
    print(f"scenario={args.scn}  sat={args.sat}  bound={args.bound}  "
          f"quantize={args.quantize}  amp={args.amp}")
    print(f"  peak edge energy (conserved qty) : {peak:.4g}")
    print(f"  energy lost to bound              : {r['lost']:.4g}")
    print(f"  interior conservation drift       : {(seg.max()-seg.min())/(seg.mean()+1e-30)*100:.3f}%")
    print(f"  propagation speed (nodes/tick)    : {speed:.3f}")
    mfrac = e1 / (e0 + e1 + 1e-30)          # fraction of field energy in n>=1
    print(f"  max compact fraction E(n>=1)/(n0+n>=1): {mfrac.max()*100:.4f}%")
    print(f"  final compact fraction                : {mfrac[-1]*100:.4f}%")
    # PRIMARY compact signal = c-STRUCTURE E(n>=1); Ec (c-edge energy) is
    # confounded by the isotropic scatter (~50% even for a photon) -- reported
    # but not used for the verdict.
    base = mfrac[:lo].max()
    grew = mfrac.max() - base
    print(f"  compact STRUCTURE frac E(n>=1): base {base*100:.4f}%  max {mfrac.max()*100:.4f}%  (grew +{grew*100:.4f}%)")
    print(f"  [Ec/(Ex+Ec) c-edge energy    : {(r['Ec']/(r['Ex']+r['Ec']+1e-30)).max()*100:.1f}% — confounded by isotropic scatter]")
    verdict = ("no c-STRUCTURE formed (energy stays photon-like)"
               if grew < 0.005 else
               f"c-STRUCTURE GREW by {grew*100:.3f}% -> energy trapped into a compact mode")
    print(f"  -> {verdict}")
    Et = Ee

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        outdir = os.path.abspath(args.out); os.makedirs(outdir, exist_ok=True)
        fig, ax = plt.subplots(1, 2, figsize=(12, 4.4))
        st = r["streak"]
        vmax = np.abs(st).max() + 1e-30
        ax[0].imshow(st, aspect="auto", origin="lower", cmap="RdBu_r",
                     vmin=-vmax, vmax=vmax, extent=[0, args.nx, 0, args.steps])
        ax[0].set_xlabel("x"); ax[0].set_ylabel("t")
        ax[0].set_title("c-averaged field (photon) — streak = propagation")
        ax[1].plot(e0 / peak, label="E(n=0) photon")
        ax[1].plot(e1 / peak, label="E(n>=1) compact")
        ax[1].plot(Et / peak, label="E total", lw=0.8, color="k")
        ax[1].set_xlabel("t"); ax[1].set_ylabel("energy / peak")
        ax[1].set_title("photon vs compact-mode energy"); ax[1].legend()
        fig.tight_layout()
        tag = args.tag or f"{args.scn}_{args.sat}"
        png = os.path.join(outdir, f"cylinder_{tag}.png")
        fig.savefig(png, dpi=110); print(f"  saved {png}")
    except Exception as e:
        print(f"  (plot skipped: {e})")


if __name__ == "__main__":
    main()
