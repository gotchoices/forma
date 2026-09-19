"""
Node storage + edge storage on the canonical GRID scatter: anisotropic slowing,
impedance matching, and the light-bending parameter gamma (validation step 3).

What it does
------------
Step 1 (carrier_dispersion.py) loaded each NODE with a storage register; that
slows every direction alike and gives gamma = 0 (half the observed light
bending).  This script adds the dual element: a storage register mounted in
SERIES at the middle of an edge.  Each edge is two half-links (one tick each)
with a two-port series junction between them; with zero weight the junction is
transparent and the lattice is the step-1 lattice at half the tick rate.

  node storage  weight Y, share returns with the SAME sign   -> raises eps
  edge storage  weight Z, share returns INVERTED             -> raises mu on
                                                                 that axis only
(the opposite return sign in either place opens a gap: a photon mass.)

On an (x, c) lattice (x extended, c compact) with edge storage on x-edges only:
    omega^2 = c0^2 ( k_x^2 / mu_x + k_c^2 ) / eps ,
    eps = 1 + Y/8 ,  mu_x = 1 + Z/4 ,  c0^2 = 1/8  (per tick^2).
Light speed along x ~ 1/sqrt(eps mu_x); rest frequency ~ 1/sqrt(eps).  Hence
    gamma = d(ln c_x)/d(ln w0) - 1 = d(mu_x)/d(eps),
and gamma = 1  <=>  eps and mu_x are loaded equally  <=>  the wave impedance
sqrt(mu_x/eps) is unchanged (no reflection from a gradient).

Modes
-----
  --mode spectrum  exact Bloch spectrum: c_x^2, w0^2/k_c^2, inertia alpha for a
                   list of (K_eps, K_mu) loadings; compares with the formula and
                   reports gamma for small equal/unequal loadings.
  --mode reflect   time domain: a photon packet meets an ABRUPT step in the
                   loading.  Compares node-only, edge-only and matched loading.
  --mode drop      time domain: uniform gradient of a MATCHED loading K(x).
                   Rest packet acceleration and photon delay versus the ray
                   equations of the exact local spectrum; the measured
                   light-to-clock ratio gives gamma.

Inputs: see --help.   Outputs: printed tables.
"""
import argparse
import numpy as np

D = 2                      # axes: 0 = x (extended), 1 = c (compact)
NREG = 5 * D + 1           # [a+x a-x a+c a-c | s_node | b+x b-x s_x | b+c b-c s_c]
C0SQ = 1.0 / 8.0


def ia(a, s): return 2 * a + (0 if s > 0 else 1)
IST = 2 * D
def ib(a, s): return 2 * D + 1 + 3 * a + (0 if s > 0 else 1)
def ims(a): return 2 * D + 1 + 3 * a + 2


def bloch(k, Y, Z):
    """One-tick operator at wavevector k; node storage Y, edge storage Z[a]."""
    T = np.zeros((NREG, NREG), complex)
    sy, Nn = np.sqrt(Y), 2 * D
    V = np.zeros(NREG)
    for a in range(D):
        V[ia(a, 1)] = V[ia(a, -1)] = 2 / (Nn + Y)
    V[IST] = 2 * sy / (Nn + Y)
    for a in range(D):
        r = V.copy(); r[ia(a, -1)] -= 1; T[ib(a, 1)] += r                        # out +a
        r = V.copy(); r[ia(a, 1)] -= 1; T[ib(a, -1)] += np.exp(1j * k[a]) * r    # out -a
    r = sy * V; r[IST] -= 1; T[IST] += r                                         # node store: same sign
    for a in range(D):
        sz = np.sqrt(Z[a])
        I = np.zeros(NREG)
        I[ib(a, 1)], I[ib(a, -1)], I[ims(a)] = 2 / (2 + Z[a]), -2 / (2 + Z[a]), 2 * sz / (2 + Z[a])
        r = -I.copy(); r[ib(a, 1)] += 1; T[ia(a, -1)] += r
        r = I.copy(); r[ib(a, -1)] += 1; T[ia(a, 1)] += np.exp(-1j * k[a]) * r
        r = -sz * I; r[ims(a)] += 1; T[ims(a)] -= r                              # edge store: inverted
    return T


def freq_and_vec(k, Y, Z):
    lam, vec = np.linalg.eig(bloch(np.asarray(k, float), Y, Z))
    w = -np.angle(lam)
    j = int(np.argmin(np.where(w > 1e-7, w, np.inf)))
    return float(w[j]), vec[:, j]


def freq(k, Y, Z): return freq_and_vec(k, Y, Z)[0]


def load(Ke, Km): return 8.0 * (Ke - 1.0), [4.0 * (Km - 1.0), 0.0]


# ------------------------------------------------------------------ spectrum
def run_spectrum(args):
    k, kc = 0.01, 0.02
    print(f"{'K_eps':>6}{'K_mu':>6}{'c_x^2':>10}{'formula':>10}{'w0^2/kc^2':>11}{'formula':>10}{'alpha':>10}")
    for Ke, Km in [(1, 1), (1.25, 1), (1, 1.25), (1.25, 1.25), (1.5, 1.5), (1.1, 1.3)]:
        Y, Z = load(Ke, Km)
        cx = (freq([k, 0], Y, Z) / k) ** 2
        w0 = freq([0, kc], Y, Z) ** 2 / kc ** 2
        al = (freq([k, kc], Y, Z) ** 2 - freq([0, kc], Y, Z) ** 2) / k ** 2
        print(f"{Ke:6.2f}{Km:6.2f}{cx:10.5f}{C0SQ / (Ke * Km):10.5f}{w0:11.5f}{C0SQ / Ke:10.5f}{al:10.5f}")
    print("\ngamma = dln(c_x)/dln(w0) - 1 for a small loading step (exact spectrum):")
    e = 1e-3
    for name, dKe, dKm in [("node only", e, 0), ("edge only", 0, e), ("matched (equal)", e, e),
                           ("edge = 3 x node (check: gamma = dmu/deps)", e, 3 * e)]:
        Y0, Z0 = load(1.2, 1.2); Y1, Z1 = load(1.2 + dKe, 1.2 + dKm)
        dlc = np.log(freq([k, 0], Y1, Z1) / freq([k, 0], Y0, Z0))
        dlw = np.log(freq([0, kc], Y1, Z1) / freq([0, kc], Y0, Z0))
        g = dlc / dlw - 1 if abs(dlw) > 1e-12 else float("inf")
        print(f"  {name:<44} gamma = {g:8.4f}")


# --------------------------------------------------------------- time domain
def packet(nx, x0, k0, sigma, kc, Y0, Z0):
    ks = 2 * np.pi * np.fft.fftfreq(nx)
    dk = (ks - k0 + np.pi) % (2 * np.pi) - np.pi
    G = np.exp(-(dk * sigma) ** 2)
    spec = np.zeros((NREG, nx), complex)
    for i in np.where(G > 1e-10)[0]:
        v = freq_and_vec([ks[i], kc], Y0, Z0)[1]
        v = v * np.exp(-1j * np.angle(v[:4].sum() + 1e-30)) / np.linalg.norm(v)
        spec[:, i] = G[i] * v * np.exp(-1j * ks[i] * x0)
    r = np.fft.ifft(spec, axis=1) * nx
    return r / np.sqrt((np.abs(r) ** 2).sum())


def step(r, Y, sy, Zx, szx, ph):
    V = 2 * (r[0] + r[1] + r[2] + r[3] + sy * r[IST]) / (4 + Y)
    opx, omx, opc, omc = V - r[1], V - r[0], V - r[3], V - r[2]
    sn = sy * V - r[IST]
    bp, bm, sx = r[ib(0, 1)], r[ib(0, -1)], r[ims(0)]
    I = 2 * (bp - bm + szx * sx) / (2 + Zx)
    mmx, mpx, sxn = bp - I, bm + I, -(sx - szx * I)
    mpc, mmc = r[ib(1, 1)].copy(), r[ib(1, -1)].copy()          # compact edges: transparent
    new = np.empty_like(r)
    new[ib(0, 1)], new[ib(0, -1)] = opx, np.roll(omx, -1)
    new[ib(1, 1)], new[ib(1, -1)] = opc, omc * ph
    new[ia(0, 1)], new[ia(0, -1)] = np.roll(mpx, 1), mmx
    new[ia(1, 1)], new[ia(1, -1)] = mpc * np.conj(ph), mmc
    new[IST], new[ims(0)], new[ims(1)] = sn, sxn, 0.0
    return new


def centroid(r, x):
    e = (np.abs(r) ** 2)
    pos = np.vstack([np.tile(x, (5, 1)), np.tile(x + 0.5, (6, 1))])   # mid registers sit at j + 1/2
    return float((pos * e).sum() / e.sum())


def run_reflect(args):
    nx = args.nx; x = np.arange(nx); xs0, xr0 = nx // 5, nx // 2
    print(f"abrupt step in the loading at x={xr0}; photon k0={args.kphot} "
          f"(wavelength {2 * np.pi / args.kphot:.1f} nodes)\n")
    print(f"{'loading beyond the step':<34}{'speed ratio':>12}{'R measured':>13}{'R impedance':>13}")
    for name, Ke, Km in [("node only   (eps=1.5, mu=1)", 1.5, 1.0), ("edge only   (eps=1, mu=1.5)", 1.0, 1.5),
                         ("matched     (eps=mu=1.2247)", 1.5 ** 0.5, 1.5 ** 0.5)]:
        Yb, Zb = load(Ke, Km)
        Y = np.where(x < xr0, 0.0, Yb); Zx = np.where(x + 0.5 < xr0, 0.0, Zb[0])
        r = packet(nx, xs0, args.kphot, args.sigma, 0.0, 0.0, [0.0, 0.0])
        v = (freq([args.kphot + 1e-5, 0], 0, [0, 0]) - freq([args.kphot - 1e-5, 0], 0, [0, 0])) / 2e-5
        for _ in range(int((xr0 - xs0) / v * 1.7)):
            r = step(r, Y, np.sqrt(Y), Zx, np.sqrt(Zx), 1.0)
        e = (np.abs(r) ** 2).sum(0)
        R = e[: int(xr0 - 2 * args.sigma)].sum() / e.sum()
        z = np.sqrt(Km / Ke)                                   # wave impedance ratio
        print(f"{name:<34}{1 / np.sqrt(Ke * Km):12.4f}{R:13.3e}{((z - 1) / (z + 1)) ** 2:13.3e}")


def run_drop(args):
    nx, x0 = args.nx, args.nx // 2
    x = np.arange(nx)
    Kfun = lambda xx: args.K0 + args.grad * (xx - x0)
    Yx = 8 * (Kfun(x) - 1); Zx = 4 * (Kfun(x + 0.5) - 1)
    Y0, Z0 = load(args.K0, args.K0)
    H = lambda xx, kx, kc: freq([kx, kc], *load(Kfun(xx), Kfun(xx)))
    print(f"matched loading K(x) = {args.K0} + {args.grad:g}(x-x0): eps = mu_x = K, compact edges unloaded\n")

    kc = 2 * np.pi / args.nc
    r = packet(nx, x0, 0.0, args.sigma, kc, Y0, Z0)
    ts, xs = [], []
    for t in range(args.steps + 1):
        if t % 20 == 0:
            ts.append(t); xs.append(centroid(r, x))
        r = step(r, Yx, np.sqrt(Yx), Zx, np.sqrt(Zx), np.exp(1j * kc))
    a_sim = 2 * np.polyfit(np.array(ts, float), np.array(xs) - x0, 2)[0]
    hk, hx = 1e-4, 0.5
    Hkk = (H(x0, hk, kc) - 2 * H(x0, 0, kc) + H(x0, -hk, kc)) / hk ** 2
    Hx = (H(x0 + hx, 0, kc) - H(x0 - hx, 0, kc)) / (2 * hx)
    a_ray = -Hkk * Hx
    a_cont = C0SQ * args.grad / (2 * args.K0 ** 3)
    print(f"rest packet (n=1):  a_sim = {a_sim:.4e}   a_ray(exact spectrum) = {a_ray:.4e}   "
          f"ratio = {a_sim / a_ray:.4f}   [continuum c0^2 K'/(2K^3) = {a_cont:.4e}]")

    # photon: delay relative to a flat control, against the ray equations
    k0 = args.kphot
    v0 = (H(x0, k0 + 1e-5, 0.0) - H(x0, k0 - 1e-5, 0.0)) / 2e-5
    T = int(min(args.steps, 0.35 * nx / v0))
    rg = packet(nx, x0, k0, args.sigma, 0.0, Y0, Z0); rf = rg.copy()
    Yf = np.full(nx, Y0); Zf = np.full(nx, Z0[0])
    for _ in range(T):
        rg = step(rg, Yx, np.sqrt(Yx), Zx, np.sqrt(Zx), 1.0)
        rf = step(rf, Yf, np.sqrt(Yf), Zf, np.sqrt(Zf), 1.0)
    d_sim = centroid(rg, x) - centroid(rf, x)
    s = np.array([x0, k0], float)
    f = lambda s: np.array([(H(s[0], s[1] + 1e-5, 0) - H(s[0], s[1] - 1e-5, 0)) / 2e-5,
                            -(H(s[0] + hx, s[1], 0) - H(s[0] - hx, s[1], 0)) / (2 * hx)])
    for _ in range(T):
        k1 = f(s); k2 = f(s + .5 * k1); k3 = f(s + .5 * k2); k4 = f(s + k3)
        s = s + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    d_ray = s[0] - x0 - v0 * T
    print(f"photon delay after {T} ticks:  sim = {d_sim:.3f}   ray = {d_ray:.3f}   ratio = {d_sim / d_ray:.4f}")

    dlc = (np.log(H(x0 + hx, 1e-2, 0)) - np.log(H(x0 - hx, 1e-2, 0))) / (2 * hx)
    dlw = (np.log(H(x0 + hx, 0, kc)) - np.log(H(x0 - hx, 0, kc))) / (2 * hx)
    print(f"local slopes:  dln(c_x)/dx = {dlc:.4e}   dln(w0)/dx = {dlw:.4e}   ->  gamma = {dlc / dlw - 1:.4f}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--mode", choices=["spectrum", "reflect", "drop"], default="spectrum")
    p.add_argument("--nx", type=int, default=4096)
    p.add_argument("--nc", type=int, default=64, help="compact circumference (nodes)")
    p.add_argument("--steps", type=int, default=6000)
    p.add_argument("--sigma", type=float, default=60.0)
    p.add_argument("--K0", type=float, default=1.2)
    p.add_argument("--grad", type=float, default=2e-5, help="dK/dx for the matched loading")
    p.add_argument("--kphot", type=float, default=0.30)
    args = p.parse_args()
    {"spectrum": run_spectrum, "reflect": run_reflect, "drop": run_drop}[args.mode](args)


if __name__ == "__main__":
    main()
