"""
2D free-space soliton test -- can a lump stay coherent in more than one extended
dimension? (The "travels in x but disperses in y,z" question.)

Complex nonlinear Klein-Gordon on a 2D (x,y) grid, cubic-quintic potential
(focusing + saturating), leapfrog:
    phi_tt = lap(phi) - ( m^2 - 2 g |phi|^2 + 3 q |phi|^4 ) phi

Three cases (--mode):
  linear   (g=q=0, real)      : baseline -- a 2D lump DISPERSES.
  oscillon (g,q>0, real)      : a real focusing lump. Derrick forbids a *static*
                                2D scalar soliton, but a *breathing* one (an
                                OSCILLON) can be long-lived -- this is exactly the
                                "small oscillations in the side lobes contain the
                                lump" idea. Does it hold, and for how long?
  qball    (g,q>0, complex)   : a charge-carrying lump (phi ~ e^{-i w t}). The
                                conserved U(1) charge evades Derrick -> should be
                                STABLE in 2D. (The charge = the aleph-winding.)

Diagnostics: rms radius, peak |phi|^2, norm, charge -- over time. Tells hold vs
disperse vs collapse, and stable vs slowly-radiating.
"""
import argparse
import os
import numpy as np


def run(args):
    n, dx, dt = args.n, args.dx, args.dt
    ax = (np.arange(n) - n // 2) * dx
    X, Y = np.meshgrid(ax, ax, indexing="ij")
    R = np.sqrt(X ** 2 + Y ** 2)
    m2 = args.m ** 2

    env = args.amp * np.exp(-(R / args.width) ** 2)
    phi = env.astype(complex)
    phi_t = np.zeros_like(phi)
    if args.mode == "qball":
        phi_t = -1j * args.omega * phi                 # rotating -> carries charge
    phi_prev = phi - dt * phi_t

    damp = np.ones((n, n)); mm = 24
    ramp = np.linspace(0, 0.05, mm)
    d1 = np.ones(n); d1[:mm] = 1 - ramp[::-1]; d1[-mm:] = 1 - ramp
    damp = np.outer(d1, d1)

    g = 0.0 if args.mode == "linear" else args.g
    q = 0.0 if args.mode == "linear" else args.q

    def lap(f):
        return (np.roll(f, 1, 0) + np.roll(f, -1, 0) +
                np.roll(f, 1, 1) + np.roll(f, -1, 1) - 4 * f) / dx ** 2

    rad, peak, norm, charge = [], [], [], []
    for t in range(args.steps):
        sig = np.abs(phi) ** 2
        phi_next = 2 * phi - phi_prev + dt ** 2 * (lap(phi) - (m2 - 2 * g * sig + 3 * q * sig ** 2) * phi)
        phi_next *= damp
        pt = (phi_next - phi_prev) / (2 * dt)
        rho = np.abs(phi) ** 2
        tot = rho.sum() + 1e-30
        rad.append(float(np.sqrt((R ** 2 * rho).sum() / tot)))
        peak.append(float(rho.max())); norm.append(float(tot))
        charge.append(float(np.sum(np.imag(np.conj(phi) * pt))))
        phi_prev, phi = phi, phi_next
    return dict(rad=np.array(rad), peak=np.array(peak), norm=np.array(norm),
                charge=np.array(charge), phi=phi, R=R)


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--mode", choices=["linear", "oscillon", "qball"], default="oscillon")
    p.add_argument("--n", type=int, default=200)
    p.add_argument("--dx", type=float, default=0.5)
    p.add_argument("--dt", type=float, default=0.2)
    p.add_argument("--steps", type=int, default=3000)
    p.add_argument("--m", type=float, default=1.0)
    p.add_argument("--g", type=float, default=1.0)
    p.add_argument("--q", type=float, default=0.3)
    p.add_argument("--amp", type=float, default=1.3)
    p.add_argument("--width", type=float, default=3.0)
    p.add_argument("--omega", type=float, default=0.6)
    p.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "outputs"))
    p.add_argument("--tag", default="")
    args = p.parse_args()

    r = run(args)
    rd, pk, nm, Q = r["rad"], r["peak"], r["norm"], r["charge"]
    a, b = 3, int(0.95 * len(rd))                     # start near t=0 to catch dispersal
    print(f"mode={args.mode}  g={args.g if args.mode!='linear' else 0}  q={args.q if args.mode!='linear' else 0}")
    print(f"  rms radius: {rd[a]:.2f} -> {rd[b]:.2f}   (x{rd[b]/max(rd[a],1e-9):.2f})   init width {args.width}")
    print(f"  peak |phi|^2: {pk[a]:.3f} -> {pk[b]:.3f}   norm: x{nm[b]/max(nm[a],1e-9):.2f}")
    print(f"  charge Q: {Q[a]:.3f} -> {Q[b]:.3f}")
    grow = rd[b] / max(rd[a], 1e-9)
    if not np.isfinite(pk[b]) or pk[b] > 8 * pk[a]:
        verdict = "COLLAPSE/blow-up"
    elif grow > 1.8:
        verdict = "DISPERSES (no free-space containment)"
    elif grow > 1.15:
        verdict = "slowly spreading / radiating (quasi-stable)"
    else:
        verdict = "HOLDS COHERENT in 2D free space"
    print(f"  -> {verdict}")

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        outdir = os.path.abspath(args.out); os.makedirs(outdir, exist_ok=True)
        fig, ax = plt.subplots(1, 2, figsize=(11, 4.4))
        im = ax[0].imshow(np.abs(r["phi"]) ** 2, cmap="magma")
        ax[0].set_title(f"|phi|^2 final ({args.mode})"); plt.colorbar(im, ax=ax[0])
        ax[1].plot(rd, label="rms radius"); ax[1].plot(pk, label="peak |phi|^2")
        ax[1].set_xlabel("t"); ax[1].legend(); ax[1].set_title("radius & peak vs t")
        fig.tight_layout()
        tag = args.tag or args.mode
        png = os.path.join(outdir, f"soliton2d_{tag}.png")
        fig.savefig(png, dpi=110); print(f"  saved {png}")
    except Exception as e:
        print(f"  (plot skipped: {e})")


if __name__ == "__main__":
    main()
