"""
Sine-Gordon breather test -- is GRID's compact phase (ILN-line) FOCUSING?

DERIVATION (see work/focusing-from-phase.md): GRID's bounded quantity is a COMPACT
PHASE (the ILN-line), not a clipped linear amplitude. A compact phase's natural
on-site potential is periodic; the minimal one is the cosine:

    U(phi) = m^2 (1 - cos phi) = m^2 ( phi^2/2 - phi^4/24 + phi^6/720 - ... )
                                          mass    ATTRACTIVE   SATURATING
                                                  (quartic<0)  (sextic>0)

So periodicity ALONE gives focusing+saturating -- the exact soliton recipe. This is
the sine-Gordon equation, phi_tt - phi_xx + m^2 sin phi = 0, whose continuum theory
has exact BREATHERS: localized, oscillating, Lorentz-boostable (mobile) lumps -- a
contained-wave particle, derived from GRID's compact-phase structure (not borrowed).

This checks it numerically:
  --model sg   : full sine-Gordon (sin phi)     -> expect a STABLE, MOBILE breather
  --model lin  : linearized (sin phi -> phi)    -> control, expect DISPERSION
  --kx K       : boost the breather (mobility)

Real scalar field, leapfrog. Breather IC (exact, at its turning point):
  phi(x,0) = 4 atan[ (sqrt(1-w^2)/w) / cosh(sqrt(1-w^2) x) ],  phi_t(x,0)=0.
"""
import argparse
import os
import numpy as np


def run(args):
    dx, dt = args.dx, args.dt
    nx = args.nx
    x = (np.arange(nx) - nx // 2) * dx
    w = args.omega
    k = np.sqrt(max(1e-6, 1 - w ** 2))
    phi = 4 * np.arctan((k / w) / np.cosh(k * x))       # breather turning point
    phi_t = np.zeros_like(phi)
    if args.kx != 0.0:
        phi_t = -args.kx * np.gradient(phi, dx)          # give it momentum
    phi_prev = phi - dt * phi_t

    damp = np.ones(nx); mm = 60
    ramp = np.linspace(0, 0.05, mm)
    damp[:mm] = 1 - ramp[::-1]; damp[-mm:] = 1 - ramp

    widths, cents, energies, peaks = [], [], [], []
    for t in range(args.steps):
        lap = (np.roll(phi, -1) + np.roll(phi, 1) - 2 * phi) / dx ** 2
        force = np.sin(phi) if args.model == "sg" else phi
        phi_next = 2 * phi - phi_prev + dt ** 2 * (lap - args.m ** 2 * force)
        phi_next *= damp
        pt = (phi_next - phi_prev) / (2 * dt)
        px = np.gradient(phi, dx)
        U = (1 - np.cos(phi)) if args.model == "sg" else 0.5 * phi ** 2
        dens = 0.5 * pt ** 2 + 0.5 * px ** 2 + args.m ** 2 * U     # energy density
        rho = dens                                                # localize by energy
        tot = rho.sum() + 1e-30
        cx = (x * rho).sum() / tot
        wx = np.sqrt(((x - cx) ** 2 * rho).sum() / tot)
        widths.append(float(wx)); cents.append(float(cx))
        energies.append(float(dens.sum() * dx)); peaks.append(float(np.abs(phi).max()))
        phi_prev, phi = phi, phi_next

    return dict(width=np.array(widths), cent=np.array(cents),
                energy=np.array(energies), peak=np.array(peaks), x=x, phi=phi)


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--model", choices=["sg", "lin"], default="sg")
    p.add_argument("--nx", type=int, default=1600)
    p.add_argument("--dx", type=float, default=0.1)
    p.add_argument("--dt", type=float, default=0.05)
    p.add_argument("--steps", type=int, default=6000)
    p.add_argument("--m", type=float, default=1.0)
    p.add_argument("--omega", type=float, default=0.6, help="breather internal freq (<1)")
    p.add_argument("--kx", type=float, default=0.0, help="boost/momentum (mobility)")
    p.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "outputs"))
    p.add_argument("--tag", default="")
    args = p.parse_args()

    r = run(args)
    wd, ct, en, pk = r["width"], r["cent"], r["energy"], r["peak"]
    a, b = int(0.15 * len(wd)), int(0.9 * len(wd))
    print(f"model={args.model}  omega={args.omega}  kx={args.kx}")
    print(f"  width:  {wd[a]:.2f} -> {wd[b]:.2f}  (x{wd[b]/max(wd[a],1e-9):.2f})")
    print(f"  peak|phi|: {pk[a]:.2f} -> {pk[b]:.2f}  (oscillates for a breather)")
    speed = (ct[b] - ct[a]) / ((b - a) * args.dt)
    print(f"  centroid: {ct[a]:+.2f} -> {ct[b]:+.2f}   speed {speed:+.4f}")
    print(f"  energy drift: {(en[a:b].max()-en[a:b].min())/(abs(en[a:b].mean())+1e-30)*100:.1f}%")
    grew = wd[b] / max(wd[a], 1e-9)
    verdict = "DISPERSES" if grew > 1.8 else "STABLE localized (breather!)"
    mob = "MOBILE" if abs(speed) > 0.05 else "at rest"
    print(f"  -> {verdict};  {mob}")

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        outdir = os.path.abspath(args.out); os.makedirs(outdir, exist_ok=True)
        fig, ax = plt.subplots(1, 2, figsize=(12, 4.4))
        ax[0].plot(r["x"], r["phi"]); ax[0].set_xlabel("x"); ax[0].set_ylabel("phi (final)")
        ax[0].set_title(f"final field ({args.model})")
        ax[1].plot(wd, label="width"); ax[1].plot(pk, label="peak|phi|")
        ax[1].set_xlabel("t"); ax[1].set_title("width & amplitude vs t"); ax[1].legend()
        fig.tight_layout()
        tag = args.tag or f"{args.model}_k{args.kx}"
        png = os.path.join(outdir, f"sinegordon_{tag}.png")
        fig.savefig(png, dpi=110); print(f"  saved {png}")
    except Exception as e:
        print(f"  (plot skipped: {e})")


if __name__ == "__main__":
    main()
