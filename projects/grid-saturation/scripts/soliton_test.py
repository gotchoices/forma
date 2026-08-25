"""
Clean focusing+saturating soliton test -- "particle as a contained wave" (Q-ball).

WHY: every dynamical containment test in forma (grid-saturation 1D cylinder,
R24 2D torus, sheet-proton 2D clover) disperses. The obstruction named repeatedly
is a MISSING FOCUSING (attractive) nonlinearity. Stable localized waves in real
physics need the standard recipe: FOCUSING at low amplitude (pull together) +
SATURATING at high amplitude (stop collapse) -- cubic-quintic / Q-ball. forma has
tried the saturating half alone (defocusing) and pure nonlinearities that disperse,
but never the combination. This decouples the question from the scatter lattice and
asks it cleanly: does focusing+saturating bind a STABLE, MOBILE, localized particle?

MODEL: complex relativistic scalar (nonlinear Klein-Gordon) in 1D -- faithful to
GRID (2nd-order/relativistic, a mass gap like KK, and a conserved U(1) charge Q =
the winding/charge). Leapfrog time integration.

    phi_tt = phi_xx - ( m^2  - 2 g |phi|^2  + 3 q |phi|^4 ) phi
                        \___/   \________/    \________/
                        mass    FOCUSING      SATURATING
                                (g>0 attr.)   (q>0 stabilizes)

A Q-ball is phi = f(x) e^{-i w t}, f localized, stable, boostable (mobile), with
conserved charge Q = Integral Im(phi* phi_t) dx. Vacuum at phi=0 needs m^2>0;
Q-balls exist when U(sigma)/sigma = m^2 - g sigma + q sigma^2 dips below m^2 at
sigma>0, i.e. g^2/(4q) < m^2.

TESTS (via --g, --q, --kx):
  linear (g=q=0)          : baseline -- should DISPERSE.
  focusing only (g>0,q=0) : binds but may COLLAPSE/blow up (no stabilizer).
  focus+saturate (g,q>0)  : the recipe -- does a STABLE localized lump persist?
  boost (--kx != 0)       : does the lump TRANSLATE as a coherent packet (MOBILE)?

Reports width(t), centroid/speed, and conservation of charge Q and energy E.
"""
import argparse
import os
import numpy as np


def run(args):
    nx, dt = args.nx, args.dt
    x = (np.arange(nx) - nx // 2).astype(float)
    m2 = args.m ** 2

    # initial localized lump with the Q-ball rotating phase e^{-i w t}
    env = args.amp * np.exp(-(x / args.width) ** 2)
    phi = env.astype(complex)
    phi_t = -1j * args.omega * phi
    if args.kx != 0.0:                          # boost -> mobility test
        boost = np.exp(1j * args.kx * x)
        phi = phi * boost
        phi_t = phi_t * boost
    phi_prev = phi - dt * phi_t                 # leapfrog seed

    # absorbing ramp near the ends (so radiation leaves, doesn't reflect)
    damp = np.ones(nx)
    m = 40
    ramp = np.linspace(0, 0.06, m)
    damp[:m] = 1 - ramp[::-1]; damp[-m:] = 1 - ramp

    def dU_dsigma(sig):
        return m2 - 2 * args.g * sig + 3 * args.q * sig ** 2

    widths, cents, norms, charges, energies, peak = [], [], [], [], [], []
    for t in range(args.steps):
        lap = np.roll(phi, -1) + np.roll(phi, 1) - 2 * phi        # dx=1
        sig = np.abs(phi) ** 2
        phi_next = 2 * phi - phi_prev + dt ** 2 * (lap - dU_dsigma(sig) * phi)
        phi_next *= damp
        # diagnostics on current phi
        pt = (phi_next - phi_prev) / (2 * dt)
        px = (np.roll(phi, -1) - np.roll(phi, 1)) / 2
        U = m2 * sig - args.g * sig ** 2 + args.q * sig ** 3
        dens = np.abs(pt) ** 2 + np.abs(px) ** 2 + U             # energy density
        rho = np.abs(phi) ** 2                                    # |phi|^2 profile
        tot = rho.sum() + 1e-30
        cx = (x * rho).sum() / tot
        wx = np.sqrt(((x - cx) ** 2 * rho).sum() / tot)
        widths.append(float(wx)); cents.append(float(cx)); norms.append(float(tot))
        charges.append(float(np.sum(np.imag(np.conj(phi) * pt))))
        energies.append(float(dens.sum())); peak.append(float(rho.max()))
        phi_prev, phi = phi, phi_next

    return {k: np.array(v) for k, v in dict(
        width=widths, cent=cents, norm=norms, charge=charges,
        energy=energies, peak=peak).items()} | {"phi": phi, "x": x}


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--nx", type=int, default=1024)
    p.add_argument("--steps", type=int, default=4000)
    p.add_argument("--dt", type=float, default=0.4)
    p.add_argument("--m", type=float, default=1.0, help="mass (vacuum curvature)")
    p.add_argument("--g", type=float, default=0.0, help="FOCUSING strength (attractive)")
    p.add_argument("--q", type=float, default=0.0, help="SATURATING strength (stabilizer)")
    p.add_argument("--amp", type=float, default=1.3)
    p.add_argument("--width", type=float, default=5.0)
    p.add_argument("--omega", type=float, default=0.6, help="Q-ball rotation freq")
    p.add_argument("--kx", type=float, default=0.0, help="boost / momentum (mobility test)")
    p.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "outputs"))
    p.add_argument("--tag", default="")
    args = p.parse_args()

    r = run(args)
    w, c, n, Q, E, pk = r["width"], r["cent"], r["norm"], r["charge"], r["energy"], r["peak"]
    print(f"g(focus)={args.g}  q(sat)={args.q}  kx={args.kx}  amp={args.amp} width0={args.width}")
    # settle window: skip initial transient, compare early vs late (interior)
    a, b = int(0.25 * len(w)), int(0.95 * len(w))
    print(f"  width:  {w[a]:.2f} -> {w[b]:.2f}   (x{w[b]/max(w[a],1e-9):.2f})   init {args.width}")
    print(f"  peak |phi|^2: {pk[a]:.3f} -> {pk[b]:.3f}   norm(|phi|^2): x{n[b]/max(n[a],1e-9):.2f}")
    speed = (c[b] - c[a]) / (b - a) / args.dt
    print(f"  centroid: {c[a]:+.1f} -> {c[b]:+.1f}   speed {speed:+.4f}")
    print(f"  charge Q: {Q[a]:.3f} -> {Q[b]:.3f}   energy drift (interior): "
          f"{(E[a:b].max()-E[a:b].min())/(abs(E[a:b].mean())+1e-30)*100:.1f}%")
    grew = w[b] / max(w[a], 1e-9)
    if pk[b] > 5 * pk[a] or not np.isfinite(pk[b]):
        verdict = "COLLAPSE/blow-up"
    elif grew > 1.8:
        verdict = "DISPERSES"
    else:
        verdict = "STABLE localized (contained!)"
    mob = "MOBILE" if abs(speed) > 0.05 else "at rest"
    print(f"  -> {verdict};  {mob}")

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        outdir = os.path.abspath(args.out); os.makedirs(outdir, exist_ok=True)
        fig, ax = plt.subplots(1, 2, figsize=(12, 4.4))
        ax[0].plot(r["x"], np.abs(r["phi"]) ** 2)
        ax[0].set_xlabel("x"); ax[0].set_ylabel("|phi|^2 (final)")
        ax[0].set_title(f"final profile (g={args.g}, q={args.q})")
        ax[1].plot(w, label="width"); ax[1].plot(pk, label="peak |phi|^2")
        ax[1].plot(n / n[0], label="norm/norm0")
        ax[1].set_xlabel("t (steps)"); ax[1].set_title("width / peak / norm vs t")
        ax[1].legend(fontsize=8)
        fig.tight_layout()
        tag = args.tag or f"g{args.g}_q{args.q}_k{args.kx}"
        png = os.path.join(outdir, f"soliton_{tag}.png")
        fig.savefig(png, dpi=110); print(f"  saved {png}")
    except Exception as e:
        print(f"  (plot skipped: {e})")


if __name__ == "__main__":
    main()
