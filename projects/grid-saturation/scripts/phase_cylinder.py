"""
Phase (U(1)) cylinder: the topological-winding test for grid-saturation.

Same (x, c) cylinder and equal-impedance scatter S = (2/N)J - I, N = 4, but each
directed edge now carries a COMPLEX amplitude, so the field has a genuine PHASE
and a WINDING NUMBER around the compact ring c. This is the minimal U(1) / ILN-line
needed to test candidate mechanism III (a particle = a topological phase winding).

What it tests against the gate (work/binding-evaluation.md):
  G1  photon (winding 0, c-uniform) still propagates at the lattice c.
  G2  two coherent sources still interfere (phase is real).
  G3  a unit c-winding localized in x: does it PERSIST and stay LOCALIZED?
      - topology should protect the c-WINDING NUMBER (can't unwind while |psi|!=0)
      - but x-LOCALIZATION needs a binding nonlinearity; we test:
          --sat clip   : the GRID-native value-bound (caps |edge|; DEFOCUSING)
          --focus g    : self-phase-modulation psi->psi*exp(i g|psi|^2)
                         (FOCUSING; discrete-NLS soliton maker -- positive control)

Scenarios (--scn):
  photon    : winding-0 wavepacket on +x, uniform in c  (G1)
  wind      : winding-1 excitation, localized in x, zero net x-momentum (G3)
  twobeam   : two coherent +x/-x winding-0 beams (G2 interference smoke test)

Diagnostics: energy conservation (sum|edge|^2), n=0 vs n>=1 split, propagation
speed, winding number w(x) around c, and interior persistence/localization of the
compact-structure energy (the same trap metric as cylinder.py).
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
    """x open (zero-fill); c periodic (roll). Works on complex arrays."""
    inn = np.zeros_like(out)
    inn[0, 1:, :] = out[0, :-1, :]        # +x
    inn[1, :-1, :] = out[1, 1:, :]        # -x
    inn[2] = np.roll(out[2], +1, axis=1)  # +c
    inn[3] = np.roll(out[3], -1, axis=1)  # -c
    return inn


def nonlinear(out, sat, bound, focus):
    """Apply optional nonlinearity to complex outgoing edges. Returns (out, lost)."""
    lost = 0.0
    if sat == "clip":                     # value-bound: cap magnitude, keep phase
        e0 = float(np.sum(np.abs(out) ** 2))
        mag = np.abs(out)
        scale = np.minimum(1.0, bound / (mag + 1e-30))
        out = out * scale
        lost = e0 - float(np.sum(np.abs(out) ** 2))
    if focus > 0.0:                       # self-phase modulation (focusing, |psi| kept)
        rho = np.abs(out) ** 2
        out = out * np.exp(1j * focus * rho)
    return out, lost


def mode_energy(inn):
    """n=0 (c-uniform) vs n>=1 (c-varying) energy, and the x-profile of n>=1."""
    U = np.sum(inn, axis=0)                       # [Nx,Nc] complex
    dc = U.mean(axis=1, keepdims=True)            # c-average per x
    e_n0 = float(np.sum(np.abs(dc) ** 2) * U.shape[1])
    ac_x = np.sum(np.abs(U - dc) ** 2, axis=1)    # [Nx]
    return e_n0, float(np.sum(ac_x)), U, ac_x


def winding_x(U):
    """Winding number of the phase around c, per x: (1/2pi) sum_c wrap(dtheta)."""
    th = np.angle(U)                              # [Nx,Nc]
    d = np.diff(np.concatenate([th, th[:, :1]], axis=1), axis=1)  # wrap around ring
    d = (d + np.pi) % (2 * np.pi) - np.pi
    return np.sum(d, axis=1) / (2 * np.pi)        # [Nx], ~integer where |U| sizable


def run(args):
    nx, nc = args.nx, args.nc
    inn = np.zeros((N, nx, nc), dtype=complex)
    spg = sponge_mask(nx, args.sponge)[:, None]
    xc = nx // 2
    x = np.arange(nx)
    env = np.exp(-((x - xc) / args.width) ** 2)[:, None]     # x-localized envelope
    phase = np.exp(1j * 2 * np.pi * np.arange(nc) / nc)[None, :]  # winding-1 in c

    if args.scn == "wind":
        kick = np.exp(1j * args.kx * (x - xc))[:, None]   # optional x-momentum
        for d in range(N):                        # all edges equal => zero net x-momentum
            inn[d] = args.amp * env * phase * kick
    elif args.scn == "photon":
        xL = args.sponge + 30
        packet = np.exp(-((x - xL) / args.width) ** 2)[:, None]
        inn[0] = args.amp * packet * np.ones((1, nc))         # winding 0, +x moving
    elif args.scn == "twobeam":
        xL, xR = args.sponge + 30, nx - args.sponge - 30
        pL = np.exp(-((x - xL) / args.width) ** 2)[:, None]
        pR = np.exp(-((x - xR) / args.width) ** 2)[:, None]
        inn[0] = args.amp * pL * np.ones((1, nc))
        inn[1] = args.amp * pR * np.ones((1, nc))

    marg = args.sponge + 50
    interior = np.zeros(nx, dtype=bool)
    interior[marg:nx - marg] = True

    E_edge, E_n0, E_ge1, E_ge1_int, streak, lost = [], [], [], [], [], 0.0
    wind_center = []
    ac_x_last = np.zeros(nx)
    for t in range(args.steps):
        T = inn.sum(axis=0)
        out = (2.0 / N) * T[None, :, :] - inn
        out, dl = nonlinear(out, args.sat, args.bound, args.focus)
        lost += dl
        inn = propagate(out)
        inn *= spg
        e0, e1, U, ac_x = mode_energy(inn)
        E_edge.append(float(np.sum(np.abs(inn) ** 2)))
        E_n0.append(e0); E_ge1.append(e1)
        E_ge1_int.append(float(ac_x[interior].sum()))
        streak.append(np.abs(U).mean(axis=1).copy())
        w = winding_x(U)
        wind_center.append(float(w[xc]))
        ac_x_last = ac_x

    return dict(E_edge=np.array(E_edge), E_n0=np.array(E_n0),
                E_ge1=np.array(E_ge1), E_ge1_int=np.array(E_ge1_int),
                streak=np.array(streak), wind_center=np.array(wind_center),
                ac_x_last=ac_x_last, interior=interior, lost=lost, U_last=U)


def prop_speed(streak, t_lo, t_hi):
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
    p.add_argument("--steps", type=int, default=1500)
    p.add_argument("--scn", choices=["photon", "wind", "twobeam"], default="wind")
    p.add_argument("--sat", choices=["none", "clip"], default="none")
    p.add_argument("--bound", type=float, default=1.0)
    p.add_argument("--focus", type=float, default=0.0)
    p.add_argument("--amp", type=float, default=0.5)
    p.add_argument("--width", type=float, default=18.0)
    p.add_argument("--kx", type=float, default=0.0, help="x-momentum kick on the wind IC (mobility test)")
    p.add_argument("--sponge", type=int, default=40)
    p.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "outputs"))
    p.add_argument("--tag", default="")
    args = p.parse_args()

    r = run(args)
    Ee = r["E_edge"]
    peak = Ee.max() + 1e-30
    lo, hi = int(0.10 * len(Ee)), int(0.55 * len(Ee))
    speed = prop_speed(r["streak"], lo, hi)
    print(f"scenario={args.scn}  sat={args.sat}  focus={args.focus}  amp={args.amp}")
    print(f"  peak edge energy (conserved qty) : {peak:.4g}")
    print(f"  energy lost to bound             : {r['lost']:.4g}")
    seg = Ee[lo:hi]
    print(f"  conservation drift (interior win): {(seg.max()-seg.min())/(seg.mean()+1e-30)*100:.3f}%")
    print(f"  propagation speed (nodes/tick)   : {speed:.3f}")

    # G3 winding protection: winding number at the domain center over time
    wc = r["wind_center"]
    print(f"  [winding] w(center): start {wc[0]:+.2f}  end {wc[-1]:+.2f}  "
          f"min {wc.min():+.2f}  max {wc.max():+.2f}  "
          f"-> {'PROTECTED (stays ~1)' if abs(wc[-1]-round(wc[0])) < 0.3 and abs(round(wc[0]))>=1 else 'unwound / lost'}")

    # G3 localization/persistence of the compact structure
    e1i = r["E_ge1_int"]; n = len(e1i)
    base_i = e1i[:int(0.10 * n)].mean() + 1e-30
    final_i = e1i[int(0.90 * n):].mean()
    ac = r["ac_x_last"]
    if ac.sum() > 1e-12:
        xpk = int(np.argmax(ac))
        width_now = float(np.sqrt(np.sum(((np.arange(len(ac)) - xpk) ** 2) * ac) / ac.sum()))
    else:
        xpk, width_now = -1, float("nan")
    print(f"  [localize] interior E(n>=1): base {base_i:.4g}  final {final_i:.4g}  "
          f"(retained {final_i/base_i*100:.1f}% of initial)")
    print(f"  [localize] final peak x~{xpk} (center {args.nx//2}), rms width {width_now:.0f} "
          f"(init width {args.width:.0f}) -> {'LOCALIZED' if width_now < 3*args.width else 'DISPERSED'}")

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        outdir = os.path.abspath(args.out); os.makedirs(outdir, exist_ok=True)
        fig, ax = plt.subplots(1, 2, figsize=(12, 4.4))
        st = r["streak"]
        vmax = np.abs(st).max() + 1e-30
        ax[0].imshow(st, aspect="auto", origin="lower", cmap="magma",
                     vmin=0, vmax=vmax, extent=[0, args.nx, 0, args.steps])
        ax[0].set_xlabel("x"); ax[0].set_ylabel("t"); ax[0].set_title("|field| (c-avg) vs x,t")
        ax[1].plot(r["E_n0"] / peak, label="E(n=0) photon")
        ax[1].plot(r["E_ge1"] / peak, label="E(n>=1) compact")
        ax[1].plot(r["E_ge1_int"] / peak, label="E(n>=1) interior", lw=1.4)
        ax[1].plot(r["wind_center"] / max(1, abs(r["wind_center"][0])), "--", label="winding(center)/w0")
        ax[1].set_xlabel("t"); ax[1].set_title("energy split + winding"); ax[1].legend(fontsize=8)
        fig.tight_layout()
        tag = args.tag or f"{args.scn}_{args.sat}_f{args.focus}"
        png = os.path.join(outdir, f"phase_{tag}.png")
        fig.savefig(png, dpi=110); print(f"  saved {png}")
    except Exception as e:
        print(f"  (plot skipped: {e})")


if __name__ == "__main__":
    main()
