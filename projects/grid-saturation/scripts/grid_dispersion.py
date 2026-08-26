"""
GRID matter-wave dispersion + the de Broglie relation on the (x,c) cylinder.

Work item #1 (see ../README.md, work/foundation-de-broglie-harmony.md). The
impedance scatter S=(2/N)J-I followed by propagation is a LINEAR operator; for a
plane wave exp(i(kx*x + kc*c - w*t)) one full tick acts as
    inn_new = P(kx,kc) @ S @ inn ,   P = diag(e^{i kx}, e^{-i kx}, e^{i kc}, e^{-i kc})
so the EXACT GRID dispersion is w(kx,kc) = -arg(eigenvalues of M=P@S) (per tick).
This is not a fit -- it is the dynamics diagonalized. (A short time-domain run
confirms the operator reproduces the actual cylinder update.)

Tests:
  * PHOTON  (kc=0, c-uniform n=0): is w(kx) ~ c*kx (massless), giving the lattice
    light-speed c?
  * MASSIVE (kc=2*pi*n/nc, winding n>=1): is w^2 = c^2 kx^2 + w0^2 (RELATIVISTIC),
    with w0 the compact/Compton gap (the mass)? A discrete lattice breaks Lorentz
    invariance, so this is a real test, not automatic.
  * de BROGLIE: v_phase * v_group == c^2 (the phase-harmony signature), and
    lambda = 2*pi/kx = h/p. Report where lattice corrections break it.
"""
import argparse
import os
import numpy as np

N = 4
J = np.ones((N, N)); Ieye = np.eye(N)
S = (2.0 / N) * J - Ieye                      # equal-impedance scatter (orthogonal)


def Mmat(kx, kc):
    P = np.diag([np.exp(1j * kx), np.exp(-1j * kx),
                 np.exp(1j * kc), np.exp(-1j * kc)])
    return P @ S


def omega_branches(kx, kc):
    lam = np.linalg.eigvals(Mmat(kx, kc))     # |lam|=1 (M unitary)
    return np.sort(-np.angle(lam))            # w in (-pi,pi], 4 branches


# The propagating modes sit at the BAND EDGE w~pi (the scatter's non-DC eigenvalue
# is -1 => sign flip each tick, a "staggered" background). The PHYSICAL matter-wave
# frequency is the distance from that edge:  Omega = pi - |w|. The physical low band
# is the smallest resolved Omega>0 (the flat w=+-pi Nyquist branch has Omega~0).
def physical_branch(kxs, kc):
    def cands(kx):
        O = np.pi - np.abs(omega_branches(kx, kc))
        return O[O > 1e-5]                    # drop the exactly-flat Omega~0 branch
    O = np.empty(len(kxs))
    i0 = len(kxs) // 3                        # start mid-range, where bands are resolved
    O[i0] = cands(kxs[i0]).min()              # physical = lowest resolved band
    p = O[i0]
    for i in range(i0 + 1, len(kxs)):
        c = cands(kxs[i]); O[i] = c[np.argmin(np.abs(c - p))]; p = O[i]
    p = O[i0]
    for i in range(i0 - 1, -1, -1):
        c = cands(kxs[i]); O[i] = c[np.argmin(np.abs(c - p))]; p = O[i]
    return O


def timedomain_check(kx, kc, nx=None, steps=4000):
    """Confirm the operator: run the actual scatter+propagate on a periodic-x
    lattice for a single plane-wave mode; recover w by time-FFT."""
    if nx is None:
        nx = int(round(2 * np.pi / kx)) if kx > 0 else 64
        nx = max(nx, 8)
    x = np.arange(nx)
    inn = np.zeros((N, nx), dtype=complex)
    # seed the M-eigenvector for this (kx,kc) so a single frequency is excited
    lam, vec = np.linalg.eig(Mmat(kx, kc))
    v = vec[:, np.argmax(-np.angle(lam) > 1e-9)]        # a nonzero-w branch
    for d in range(N):
        inn[d] = v[d] * np.exp(1j * kx * x)
    probe = []
    for t in range(steps):
        T = inn.sum(0)
        out = (2.0 / N) * T[None, :] - inn
        # propagate: x by roll (periodic), c-phase by the kc plane-wave factor
        inn = np.empty_like(out)
        inn[0] = np.roll(out[0], 1); inn[1] = np.roll(out[1], -1)
        inn[2] = out[2] * np.exp(1j * kc); inn[3] = out[3] * np.exp(-1j * kc)
        probe.append(inn[0, 0])
    sp = np.abs(np.fft.fft(np.array(probe)))          # complex signal
    freqs = 2 * np.pi * np.fft.fftfreq(steps)
    w = abs(freqs[np.argmax(sp)])                     # dominant |w|
    return np.pi - w                                  # physical Omega = pi - w


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--nc", type=int, default=24, help="compact ring size (sets masses)")
    p.add_argument("--nmodes", type=int, default=3, help="how many winding masses to test")
    p.add_argument("--kmax", type=float, default=np.pi, help="max kx to scan")
    p.add_argument("--nk", type=int, default=400)
    p.add_argument("--relfit-kfrac", type=float, default=0.3,
                   help="fit the relativistic law over kx < kfrac*pi (continuum window)")
    p.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "outputs"))
    args = p.parse_args()

    kxs = np.linspace(1e-4, args.kmax, args.nk)
    print("(physical frequency Omega = pi - w, measured from the band edge)\n")

    # PHOTON branch (kc=0)
    wph = physical_branch(kxs, 0.0)                  # Omega(kx)
    win0 = (kxs > 0.03 * np.pi) & (kxs < 0.2 * np.pi)  # resolved, still linear
    c_light = float(np.polyfit(kxs[win0], wph[win0], 1)[0])  # slope dOmega/dk
    print(f"=== PHOTON (n=0, c-uniform) ===")
    print(f"  lattice light-speed c = Omega/kx at small k : {c_light:.4f} nodes/tick")
    kfit = kxs < 0.2 * np.pi
    lin_dev = np.abs(wph - c_light * kxs) / (c_light * kxs + 1e-9)
    print(f"  masslessness: |Omega - c*kx|/Omega over kx<0.2pi : max {lin_dev[kfit].max()*100:.2f}%")

    # time-domain confirmation at one photon k (proves the operator = the dynamics)
    ktest = kxs[args.nk // 8]
    Opred = physical_branch(kxs[:args.nk // 8 + 1], 0.0)[-1]
    Omeas = timedomain_check(ktest, 0.0)
    print(f"  operator check @ kx={ktest:.3f}: eig Omega={Opred:.4f}, "
          f"time-FFT Omega={Omeas:.4f} (diff {abs(Opred-Omeas):.4f})")

    # MASSIVE branches (kc = 2 pi n / nc)
    print(f"\n=== MASSIVE (winding n, kc=2pi n/{args.nc}) ===")
    results = {}
    for n in range(1, args.nmodes + 1):
        kc = 2 * np.pi * n / args.nc
        wm = physical_branch(kxs, kc)                 # Omega(kx)
        w0 = wm[0]                                    # rest frequency = mass gap
        # relativistic fit w^2 = c^2 kx^2 + w0^2 over the continuum window
        win = kxs < args.relfit_kfrac * np.pi
        A = np.vstack([kxs[win] ** 2, np.ones(win.sum())]).T
        coef, *_ = np.linalg.lstsq(A, wm[win] ** 2, rcond=None)
        c2_fit, w02_fit = coef
        pred = np.sqrt(np.clip(c2_fit * kxs ** 2 + w02_fit, 0, None))
        dev = np.abs(wm - pred) / (wm + 1e-9)
        # de Broglie phase harmony: v_phase * v_group == c^2, checked at a resolved kx
        vg = np.gradient(wm, kxs)
        vp = wm / kxs
        idb = int(np.argmin(np.abs(kxs - 0.12 * np.pi)))   # moderate, well-resolved
        vpg = vp[idb] * vg[idb]
        print(f"  n={n}: mass w0={w0:.4f}  |  rel-fit c={np.sqrt(max(c2_fit,0)):.4f}, "
              f"w0_fit={np.sqrt(max(w02_fit,0)):.4f}")
        print(f"        relativistic ok to <2% out to kx/pi = "
              f"{(kxs[dev < 0.02].max()/np.pi if np.any(dev<0.02) else 0):.2f}; "
              f"max dev in window {dev[win].max()*100:.2f}%")
        print(f"        de Broglie  v_phase*v_group/c^2 @ kx=0.12pi = "
              f"{vpg/max(c_light**2,1e-9):.3f}  (1.000 = exact phase harmony)")
        results[n] = (kxs, wm, pred)

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        outdir = os.path.abspath(args.out); os.makedirs(outdir, exist_ok=True)
        fig, ax = plt.subplots(1, 2, figsize=(12, 4.6))
        ax[0].plot(kxs / np.pi, wph, 'k', label="photon (massless)")
        for n, (kk, wm, pred) in results.items():
            ax[0].plot(kk / np.pi, wm, label=f"n={n} (mass {wm[0]:.2f})")
            ax[0].plot(kk / np.pi, pred, '--', lw=0.8, color='gray')
        ax[0].set_xlabel("kx / pi"); ax[0].set_ylabel("omega"); ax[0].legend(fontsize=8)
        ax[0].set_title("GRID dispersion (solid) vs relativistic fit (dashed)")
        for n, (kk, wm, pred) in results.items():
            ax[1].plot(kk / np.pi, np.abs(wm - pred) / (wm + 1e-9) * 100, label=f"n={n}")
        ax[1].axhline(2, color='r', ls=':', lw=0.8); ax[1].set_ylim(0, 15)
        ax[1].set_xlabel("kx / pi"); ax[1].set_ylabel("deviation from relativistic (%)")
        ax[1].set_title("Lorentz-breaking vs kx"); ax[1].legend(fontsize=8)
        fig.tight_layout()
        png = os.path.join(outdir, "grid_dispersion.png")
        fig.savefig(png, dpi=110); print(f"\n  saved {png}")
    except Exception as e:
        print(f"  (plot skipped: {e})")


if __name__ == "__main__":
    main()
