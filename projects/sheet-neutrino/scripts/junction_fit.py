"""Inverse design of the lepton-domain circle's junctions (host G).

What it does
  Treats the neutrino circle as three segments (lengths L1, L2, L3) joined by
  three junctions, and asks what the junctions must do for the circle to
  reproduce the measured neutrino data.  Each junction is a general lossless,
  reciprocal two-way scatterer:
      S = [[r·e^{iα},  t], [t, −r·e^{−iα}]],   t = √(1 − r²)
  with reflection strength r ∈ (−1, 1) and an optional reflection phase α.
  (α = 0 is the real-valued family a GRID node or impedance step produces;
  with --junction neck each junction is instead a narrow section: a step from
  segment width to neck width (ratio ρ), a short neck, and a step back;
  impedance steps between ribbons of widths w_a, w_b give r = (w_a−w_b)/(w_a+w_b).)
  With the Klein flips on, the circle closes with one net sign change.

  For given parameters it finds the three lowest modes (mass ∝ wavenumber k),
  the splitting ratio Δm²31/Δm²21, and a mixing matrix under two flavor
  definitions:
    segment   flavor α = the combination of the three modes most concentrated
              on segment α (maximally localized);
    point     flavor α = what a coupling at junction α creates: the
              projection of a point source there onto the three modes,
              made orthonormal by the symmetric (Löwdin) procedure.
  The target is the measured mass ratio plus the five mixing entries that do
  not depend on the unknown CP phase: |U_e1|², |U_e2|², |U_e3|², |U_μ3|²,
  |U_τ3|².  An optimizer with random restarts searches the parameters.

Inputs: command-line options (see --help).  Outputs: printed best fits.
"""
import argparse
import itertools

import numpy as np
from scipy.optimize import minimize

# Measured mixing angles (normal ordering, approximate global-fit values).
S12, S13 = 0.307, 0.0220                 # sin²θ12, sin²θ13
TARGET_RATIO = 33.6


def target_entries(s23):
    """δ_CP-independent |U|² entries: e-row (3) and ν3 column μ, τ (2)."""
    c13 = 1 - S13
    return np.array([(1 - S12) * c13, S12 * c13, S13, s23 * c13, (1 - s23) * c13])


def transfer(k, L, r, alpha):
    """Transfer matrices for propagation over L then junction (r, α); arrays over k."""
    t = np.sqrt(1 - r ** 2)
    rr, rp = r * np.exp(1j * alpha), -r * np.exp(-1j * alpha)
    J = np.array([[(t * t - rr * rp) / t, rp / t], [-rr / t, 1 / t]], complex)
    P = np.zeros((len(k), 2, 2), complex)
    P[:, 0, 0] = np.exp(1j * k * L)
    P[:, 1, 1] = np.exp(-1j * k * L)
    return J[None] @ P


def monodromy(k, Ls, rs, alphas):
    M = np.broadcast_to(np.eye(2, dtype=complex), (len(k), 2, 2)).copy()
    for L, r, a in zip(Ls, rs, alphas):
        M = transfer(k, L, r, a) @ M
    return M


def find_modes(Ls, rs, alphas, sigma, kmax, n_grid, n_modes=3):
    """Lowest n_modes wavenumbers with M(k)·v = σ·v."""
    k = np.linspace(1e-4, kmax, n_grid)
    M = monodromy(k, Ls, rs, alphas)
    # For unitary-like M with det = 1, condition ⇔ tr(M) = 2σ (real part).
    f = np.real(M[:, 0, 0] + M[:, 1, 1]) - 2 * sigma
    roots = []
    for i in range(n_grid - 1):
        if f[i] == 0 or f[i] * f[i + 1] < 0:
            roots.append(_refine(k[i], k[i + 1], Ls, rs, alphas, sigma))
        elif i > 0 and abs(f[i]) < abs(f[i - 1]) and abs(f[i]) < abs(f[i + 1]) \
                and abs(f[i]) < 1e-3:                         # touching: degenerate pair
            kk = _refine_min(k[i - 1], k[i + 1], Ls, rs, alphas, sigma)
            roots += [kk, kk]
        if len(roots) >= n_modes:
            break
    return np.array(sorted(roots)[:n_modes])


def _trace_f(k, Ls, rs, alphas, sigma):
    M = monodromy(np.array([k]), Ls, rs, alphas)[0]
    return np.real(M[0, 0] + M[1, 1]) - 2 * sigma


def _refine(a, b, Ls, rs, alphas, sigma):
    fa = _trace_f(a, Ls, rs, alphas, sigma)
    for _ in range(50):
        m = 0.5 * (a + b)
        fm = _trace_f(m, Ls, rs, alphas, sigma)
        if fa * fm <= 0:
            b = m
        else:
            a, fa = m, fm
    return 0.5 * (a + b)


def _refine_min(a, b, Ls, rs, alphas, sigma):
    ks = np.linspace(a, b, 200)
    return ks[np.argmin([abs(_trace_f(x, Ls, rs, alphas, sigma)) for x in ks])]


def mode_profiles(kvals, Ls, rs, alphas, sigma, n_per_seg):
    """Sample each mode ψ(x) on every segment; also ψ at each junction."""
    profiles, junction_vals = [], []
    dx = np.concatenate([np.full(n_per_seg, L / n_per_seg) for L in Ls])   # length per sample
    for k in kvals:
        M = monodromy(np.array([k]), Ls, rs, alphas)[0]
        w, v = np.linalg.eig(M)
        vec = v[:, np.argmin(abs(w - sigma))]
        segs, jv = [], []
        a = vec.copy()
        for L, r, al in zip(Ls, rs, alphas):
            x = np.linspace(0, L, n_per_seg, endpoint=False)
            psi = a[0] * np.exp(1j * k * x) + a[1] * np.exp(-1j * k * x)
            segs.append(psi)
            jv.append(psi[0])                                # value just after junction
            a = transfer(np.array([k]), L, r, al)[0] @ a
        prof = np.concatenate(segs)
        norm = np.sqrt(np.sum(dx * abs(prof) ** 2))                     # ∫|ψ|² dx = 1
        profiles.append(prof / norm)
        junction_vals.append(np.array(jv) / norm)
    return np.array(profiles).T * np.sqrt(dx)[:, None], np.array(junction_vals).T
    # profiles are returned weighted by √dx, so plain sums over points are integrals


def segment_flavors(prof, n_per_seg):
    """Unitary V (modes × flavors) maximizing concentration on each segment."""
    A = []
    for s in range(3):
        sl = slice(s * n_per_seg, (s + 1) * n_per_seg)
        A.append(prof[sl].conj().T @ prof[sl])
    best = None
    for seed in range(6):
        p0 = np.random.default_rng(seed).normal(0, 1, 9)
        res = minimize(lambda p: -_loc(p, A), p0, method="BFGS")
        if best is None or res.fun < best.fun:
            best = res
    V = _unitary(best.x)
    return (abs(V) ** 2).T, [np.real(V[:, a].conj() @ A[a] @ V[:, a]) for a in range(3)]


def _unitary(p):
    H = np.zeros((3, 3), complex)
    iu = np.triu_indices(3, 1)
    H[iu] = p[:3] + 1j * p[3:6]
    H = H - H.conj().T + 1j * np.diag(p[6:9])
    w, v = np.linalg.eigh(-1j * H)
    return v @ np.diag(np.exp(1j * w)) @ v.conj().T


def _loc(p, A):
    V = _unitary(p)
    return sum(np.real(V[:, a].conj() @ A[a] @ V[:, a]) for a in range(3))


def point_flavors(jv):
    """Flavor α ∝ point coupling at junction α, Löwdin-orthonormalized."""
    F = jv.conj()                                     # rows: flavors, cols: modes
    G = F @ F.conj().T
    w, v = np.linalg.eigh(G)
    if w.min() < 1e-12:
        return None
    Ginv = v @ np.diag(w ** -0.5) @ v.conj().T
    return abs(Ginv @ F) ** 2


def mixing_loss(U2, s23):
    """Squared error on the δ-independent entries, best over flavor↔junction assignment."""
    tgt = target_entries(s23)
    best = np.inf
    for p in itertools.permutations(range(3)):
        e, mu, tau = U2[p[0]], U2[p[1]], U2[p[2]]
        got = np.array([e[0], e[1], e[2], mu[2], tau[2]])
        best = min(best, np.sum((got - tgt) ** 2))
    return best


def neck_elements(x):
    """Neck junctions: params [L1, L2, log ρ1..3, neck-length logits 1..3].
    Elements: seg1, neck1, seg2, neck2, seg3, neck3.  ρ = segment width / neck width.
    Returns (Ls, rs, rho, neck_frac); lengths normalized to total 2π."""
    rho = np.exp(np.abs(x[2:5]))
    nf = 0.15 / (1 + np.exp(-x[5:8]))                  # each neck ≤ 15% of a unit segment
    raw = np.array([x[0], nf[0], x[1], nf[1], 1.0, nf[2]])
    Ls = raw * 2 * np.pi / raw.sum()
    rin = (rho - 1) / (rho + 1)
    rs = np.array([rin[0], -rin[0], rin[1], -rin[1], rin[2], -rin[2]])
    return Ls, rs, rho, Ls[1::2] / (2 * np.pi)


def neck_reflection(k, L, r):
    """|R| of one neck (step in, length L, step out) at wavenumber k."""
    T = transfer(np.array([k]), L, -r, 0.0)[0] @ transfer(np.array([k]), 0.0, r, 0.0)[0]
    return abs(T[1, 0] / T[1, 1])


def evaluate(x, a, full=False):
    neck = a.junction == "neck"
    if neck:
        if min(x[0], x[1]) <= 0.05:
            return 1e3, None
        Ls, rs, rho, nfrac = neck_elements(x)
        alphas = np.zeros(6)
        seg_idx = [0, 2, 4]
    elif a.junction == "widths":
        # direct width steps only: widths (1, e^x2, e^x3); r = (w_prev − w_next)/(w_prev + w_next)
        Ls = np.array([x[0], x[1], 1.0]) * 2 * np.pi / (x[0] + x[1] + 1.0)
        w = np.array([1.0, np.exp(x[2]), np.exp(x[3])])
        rs = np.array([(w[i - 1] - w[i]) / (w[i - 1] + w[i]) for i in range(3)])
        alphas = np.zeros(3)
        seg_idx = [0, 1, 2]
    else:
        Ls = np.array([x[0], x[1], 1.0]) * 2 * np.pi / (x[0] + x[1] + 1.0)
        rs = np.tanh(x[2:5])
        alphas = x[5:8] if a.phases else np.zeros(3)
        seg_idx = [0, 1, 2]
    sigma = -1.0 if a.flips else 1.0
    if not neck and min(x[0], x[1]) <= 0.05:
        return 1e3, None
    k = find_modes(Ls, rs, alphas, sigma, a.kmax, a.n_grid)
    if len(k) < 3 or k[1] - k[0] < 1e-9:
        return 1e3, None
    ratio = (k[2] ** 2 - k[0] ** 2) / (k[1] ** 2 - k[0] ** 2)
    prof, jv = mode_profiles(k, Ls, rs, alphas, sigma, a.n_per_seg)
    if a.flavor == "point":
        U2 = point_flavors(jv[seg_idx])               # coupling at each segment's entry
        loc = None
    else:
        keep = np.concatenate([np.arange(i * a.n_per_seg, (i + 1) * a.n_per_seg) for i in seg_idx])
        U2, loc = segment_flavors(prof[keep], a.n_per_seg)
    if U2 is None:
        return 1e3, None
    loss = a.ratio_weight * np.log(ratio / TARGET_RATIO) ** 2 + mixing_loss(U2, a.s23)
    info = dict(Ls=Ls, rs=rs, alphas=alphas, k=k, ratio=ratio, U2=U2, loc=loc) if full else None
    if full and neck:
        info.update(rho=rho, nfrac=nfrac,
                    R=[neck_reflection(k[0], Ls[2 * j + 1], rs[2 * j]) for j in range(3)])
    return loss, info


def report(x, a, label):
    loss, info = evaluate(x, a, full=True)
    if info is None:
        print(f"\n== {label}: no valid modes"); return
    Ls = info["Ls"] / (2 * np.pi)
    print(f"\n== {label}  (loss {loss:.2e})")
    if a.junction == "neck":
        print(f"  segment lengths (fractions of circle): {', '.join(f'{x:.3f}' for x in Ls[0::2])}")
        print(f"  neck narrowness ρ = segment width / neck width: {', '.join(f'{x:.1f}' for x in info['rho'])}")
        print(f"  neck lengths (fractions of circle): {', '.join(f'{x:.4f}' for x in info['nfrac'])}")
        print(f"  neck reflection |R| at ν1's wavenumber: {', '.join(f'{x:.3f}' for x in info['R'])}")
        k = info["k"]
        print(f"  modes k = {', '.join(f'{x:.4f}' for x in k)};  ratio = {info['ratio']:.2f};  k3/k1 = {k[2] / k[0]:.3f}")
        print("  |U|² (rows: flavor at segment 1, 2, 3; columns ν1 ν2 ν3):")
        for i in range(3):
            extra = f"  (localization {info['loc'][i]:.2f})" if info["loc"] is not None else ""
            print("    " + "  ".join(f"{v:.3f}" for v in info["U2"][i]) + extra)
        return
    print(f"  segment lengths (fractions of circle): {', '.join(f'{x:.3f}' for x in Ls)}")
    print(f"  junction reflections r: {', '.join(f'{x:+.3f}' for x in info['rs'])}"
          + (f";  phases α: {', '.join(f'{x:+.2f}' for x in info['alphas'])}" if a.phases else ""))
    rs = info["rs"]
    wr = [(1 - r) / (1 + r) for r in rs]                # width ratio implied by each r
    print(f"  implied width ratios w_next/w_prev at each junction: {', '.join(f'{x:.3f}' for x in wr)}"
          f"  (product {np.prod(wr):.3f}; widths alone require 1)")
    k = info["k"]
    print(f"  modes k = {', '.join(f'{x:.4f}' for x in k)};  ratio = {info['ratio']:.2f};  k3/k1 = {k[2] / k[0]:.3f}")
    print("  |U|² (rows: flavor at junction/segment 1, 2, 3; columns ν1 ν2 ν3):")
    for i in range(3):
        extra = f"  (localization {info['loc'][i]:.2f})" if info["loc"] is not None else ""
        print("    " + "  ".join(f"{v:.3f}" for v in info["U2"][i]) + extra)
    t = target_entries(a.s23)
    print(f"  target: e-row {t[0]:.3f} {t[1]:.3f} {t[2]:.3f};  |U_μ3|² {t[3]:.3f}, |U_τ3|² {t[4]:.3f}")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--flavor", choices=["segment", "point"], default="point")
    p.add_argument("--junction", choices=["free", "neck", "widths"], default="free",
                   help="free: arbitrary reflection r; neck: narrow section (width ratio ρ, length)")
    p.add_argument("--flips", action="store_true", help="Klein flips on (antiperiodic closure)")
    p.add_argument("--phases", action="store_true", help="allow junction reflection phases α")
    p.add_argument("--s23", type=float, default=0.50, help="sin²θ23 (≈0.45–0.57 allowed)")
    p.add_argument("--restarts", type=int, default=60)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--top", type=int, default=2)
    p.add_argument("--maxiter", type=int, default=600, help="optimizer iterations per restart")
    p.add_argument("--ratio-weight", type=float, default=0.3)
    p.add_argument("--kmax", type=float, default=4.0)
    p.add_argument("--n-grid", type=int, default=1500)
    p.add_argument("--n-per-seg", type=int, default=200)
    a = p.parse_args()

    rng = np.random.default_rng(a.seed)
    n_par = 8 if (a.phases or a.junction == "neck") else 5
    results = []
    for i in range(a.restarts):
        if a.junction == "neck":
            x0 = np.concatenate([rng.uniform(0.3, 2.0, 2), rng.uniform(0, 5, 3), rng.normal(0, 1.5, 3)])
        elif a.junction == "widths":
            x0 = np.concatenate([rng.uniform(0.3, 2.0, 2), rng.uniform(-7, 7, 2)])
        else:
            x0 = np.concatenate([rng.uniform(0.3, 2.0, 2), rng.normal(0, 1.2, 3),
                                 rng.uniform(-np.pi, np.pi, 3) if a.phases else []])[:n_par]
        res = minimize(lambda x: evaluate(x, a)[0], x0, method="Nelder-Mead",
                       options=dict(maxiter=a.maxiter, xatol=1e-5, fatol=1e-9))
        results.append((res.fun, res.x))
        if (i + 1) % 5 == 0:
            print(f"  restart {i + 1}/{a.restarts}: best loss so far {min(r[0] for r in results):.2e}",
                  flush=True)
    results.sort(key=lambda r: r[0])
    print(f"\n#### junction={a.junction}, flavor={a.flavor}, flips={'on' if a.flips else 'off'}, "
          f"phases={'on' if a.phases else 'off'}, sin²θ23={a.s23}")
    for j, (loss, x) in enumerate(results[:a.top]):
        report(x, a, f"fit {j + 1}")


if __name__ == "__main__":
    main()
