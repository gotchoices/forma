"""
Exact Bloch spectrum of the GRID scatter with a node storage register
("stub") -- the uniform-q test for grid-gravity mechanism 3.

Question
--------
Mechanism 3 (work/sync-carrier-mechanism.md) needs a local, lossless rule by
which a carrier value q slows propagation.  For that slowing to be TIME
DILATION rather than an optical medium, a *uniform* q must rescale the whole
low-frequency spectrum together: the photon speed c, the rest frequency
omega_0 of a compact (massive) mode, and that mode's inertia (the k_x^2
coefficient) must all scale consistently, omega^2 = c_q^2 (k_x^2 + k_c^2).

The candidate rule is the simplest lossless one: give every node one extra
storage register of weight Y that takes a share of the node's total each tick
and returns it one tick later.  The node scatter stays a reflection about a
unit vector u = (1,...,1,sqrt(Y))/sqrt(N+Y), so it is exactly orthogonal
(lossless) for every Y >= 0.

Two labelings of the link registers are tested, because the repo uses both:

  tlm   out[d] = V - in[-d]   registers are edge END-registers; the edge swaps
                              its two ends (grid-duality's canonical scatter;
                              the transmission-line-matrix convention).
                              Physical band at omega ~ 0.
  repo  out[d] = V - in[d]    registers labeled by direction of travel
                              (grid-matter's sim code).  Physical band at
                              omega ~ pi; physical frequency Omega = pi - omega.

where V = 2 (sum_links in + sqrt(Y) a_stub) / (N + Y) is the node value.

Inputs
------
--dims   number of lattice axes d (2 = x,c ; 3 = x,y,c).  N = 2d links.
--Y      list of storage weights to scan.
--stub-sign  +1 or -1: sign with which the stored share returns.
--nc     compact circumference in nodes (k_c = 2 pi n / nc).
--k      small wavenumber used for the low-frequency fits.

Outputs
-------
Printed table per convention and Y:
  c2_axis   photon speed^2 along x            (k_c = 0)
  c2_diag   photon speed^2 along the diagonal (isotropy check; d>=3 uses x,y)
  w0^2/kc^2 rest frequency^2 of the compact mode over k_c^2
  alpha     inertia coefficient: Omega^2 ~ w0^2 + alpha k_x^2
  pred      the isotropic prediction (1/d) / (1 + Y/N)
A rule passes the uniform-q test when all four agree with each other AND show
a slowing (they then also match pred).
Optionally (--plot) saves outputs/carrier_dispersion.png: Omega(k)/Omega_0(k)
versus k, showing where the rescaling stops being uniform.
"""
import argparse
import os
import numpy as np


def bloch_matrix(kvec, Y, convention, stub_sign):
    """One-tick operator M = P S on the 2d (+1 stub) registers at wavevector kvec."""
    d = len(kvec)
    N = 2 * d
    has_stub = Y > 0
    n = N + (1 if has_stub else 0)
    u = np.ones(n)
    if has_stub:
        u[-1] = np.sqrt(Y)
    u = u / np.sqrt(N + Y)
    refl = 2.0 * np.outer(u, u)
    if convention == "repo":
        S = refl - np.eye(n)
    else:                                   # tlm: subtract the OPPOSITE-direction input
        X = np.zeros((n, n))
        for a in range(d):
            X[2 * a, 2 * a + 1] = 1.0       # registers ordered (+a, -a)
            X[2 * a + 1, 2 * a] = 1.0
        if has_stub:
            X[-1, -1] = 1.0
        S = refl - X
    phases = []
    for a in range(d):
        phases += [np.exp(-1j * kvec[a]), np.exp(+1j * kvec[a])]
    if has_stub:
        phases.append(complex(stub_sign))
    return np.diag(phases) @ S, S


def physical_freq(kvec, Y, convention, stub_sign):
    """Lowest positive physical frequency Omega at kvec (band at 0 for tlm, at pi for repo)."""
    M, _ = bloch_matrix(kvec, Y, convention, stub_sign)
    w = -np.angle(np.linalg.eigvals(M))                 # eigenvalue = exp(-i w)
    Om = np.abs(w) if convention == "tlm" else np.pi - np.abs(w)
    Om = Om[Om > 1e-9]
    return float(np.min(Om)) if Om.size else 0.0


def fits(d, Y, convention, stub_sign, nc, k):
    e = lambda i, val: np.array([val if j == i else 0.0 for j in range(d)])
    kc = 2 * np.pi / nc
    c_ax = (physical_freq(e(0, k), Y, convention, stub_sign) / k) ** 2
    kd = e(0, k) + e(1 if d >= 3 else d - 1, k)         # x+y if available, else x+c
    c_dg = physical_freq(kd, Y, convention, stub_sign) ** 2 / (2 * k * k)
    comp = e(d - 1, kc)
    w0sq = physical_freq(comp, Y, convention, stub_sign) ** 2
    w1sq = physical_freq(comp + e(0, k), Y, convention, stub_sign) ** 2
    alpha = (w1sq - w0sq) / (k * k)
    return c_ax, c_dg, w0sq / kc ** 2, alpha


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--dims", type=int, default=2)
    p.add_argument("--Y", type=float, nargs="+", default=[0.0, 0.5, 1.0, 2.0, 4.0])
    p.add_argument("--stub-sign", type=int, choices=[1, -1], default=1)
    p.add_argument("--nc", type=int, default=400)
    p.add_argument("--k", type=float, default=0.01)
    p.add_argument("--plot", action="store_true")
    p.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "outputs"))
    args = p.parse_args()

    d, N = args.dims, 2 * args.dims
    for conv in ("tlm", "repo"):
        _, S = bloch_matrix(np.zeros(d), max(args.Y), conv, args.stub_sign)
        err = np.abs(S.T @ S - np.eye(S.shape[0])).max()
        print(f"\n=== convention: {conv}   d={d}  N={N}  stub-sign={args.stub_sign:+d}"
              f"   (scatter orthogonality error {err:.1e}) ===")
        print(f"{'Y':>5} {'c2_axis':>9} {'c2_diag':>9} {'w0^2/kc^2':>10} {'alpha':>9} {'pred':>9}  verdict")
        for Y in args.Y:
            ca, cd, w0, al = fits(d, Y, conv, args.stub_sign, args.nc, args.k)
            pred = (1.0 / d) / (1.0 + Y / N)
            uniform = max(abs(ca - cd), abs(ca - w0), abs(ca - al)) < 2e-3 * max(ca, 1e-9)
            if not uniform:
                verdict = "GAPPED (photon acquires a mass)" if ca > 1.0 else "not uniform"
            elif Y > 0 and abs(ca - 1.0 / d) < 1e-3 / d:
                verdict = "uniform, but no slowing"
            elif abs(ca - pred) < 2e-3 * pred:
                verdict = "UNIFORM rescale = prediction"
            else:
                verdict = "uniform, off prediction"
            print(f"{Y:5.2f} {ca:9.5f} {cd:9.5f} {w0:10.5f} {al:9.5f} {pred:9.5f}  {verdict}")

    if args.plot:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        ks = np.linspace(0.02, 1.2, 60)
        fig, ax = plt.subplots(figsize=(6.4, 4.2))
        for Y in [y for y in args.Y if y > 0]:
            r = [physical_freq(np.array([kk] + [0.0] * (d - 1)), Y, "tlm", args.stub_sign) /
                 physical_freq(np.array([kk] + [0.0] * (d - 1)), 0.0, "tlm", args.stub_sign) for kk in ks]
            ax.plot(ks, np.array(r) * np.sqrt(1 + Y / N), label=f"Y={Y:g}")
        ax.axhline(1.0, color="k", lw=0.6)
        ax.set_xlabel("k_x (rad / node)")
        ax.set_ylabel("Omega(k;Y) / Omega(k;0)  x  sqrt(1+Y/N)")
        ax.set_title("uniformity of the rescaling (tlm, photon along x): 1 = exact")
        ax.legend(fontsize=8)
        fig.tight_layout()
        os.makedirs(os.path.abspath(args.out), exist_ok=True)
        png = os.path.join(os.path.abspath(args.out), "carrier_dispersion.png")
        fig.savefig(png, dpi=110)
        print(f"\nsaved {png}")


if __name__ == "__main__":
    main()
