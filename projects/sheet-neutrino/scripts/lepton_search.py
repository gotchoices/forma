"""Back-to-basics search: a flat compact torus hosting all six leptons by spectrum.

What it does
  Searches flat N-dimensional compact geometries (sizes plus shears between
  chosen pairs of dimensions, the "sheets") for one whose LIGHTEST states are
  the observed leptons, with no particle assigned to any mode by hand:
    - the three lightest charged states have the e, μ, τ masses;
    - the three lightest neutral states reproduce the neutrino squared-mass
      splittings (Δm²21, Δm²31), lightest mass left free, all below the
      direct limit.
  Quarks are not included.

Physics rules (the irreducible assumptions)
  1. A mode is a vector of whole-number circulations n (one per dimension).
     Sheet s = (T_s, R_s) with shear σ_s shifts the momentum along R_s by
     −σ_s·n_T (ma-domain's per-sheet formula, generalized):
         k_d = (n_d − Σ_{s: R_s = d} σ_s n_{T_s}) / L_d,   m = C·|k|,  C = 2πħc.
  2. Modes exist only as single-axis modes (one nonzero circulation) or on a
     sheet (nonzero circulations on exactly that sheet's two dimensions).
     Pairs that are not sheets host no two-dimensional modes (ma-domain).
  3. Charge (metric-charge closure): a sheet mode is charged when both
     circulations are nonzero and n_T divides n_R ("asym", as written), or
     when either divides the other ("sym", tube/ring treated alike).
     Single-axis modes and sheet modes failing closure are neutral.
  4. Harmonics are not new particles: only primitive vectors (gcd = 1) count,
     and n and −n are one particle/antiparticle pair.
  5. Identification rule (--rule):
       strict  the three lightest charged states are e, μ, τ and the three
               lightest neutral states are the neutrinos;
       loose   the electron is the lightest charged state and the neutrinos
               are the three lightest neutral states (both forced by
               stability), but μ and τ need only match SOME charged mode;
               extra charged states are allowed and listed (ma-domain's
               working assumption: unobserved higher modes decay away).

Search
  For each topology (which pairs are sheets, and each sheet's orientation)
  a differential-evolution search over log sizes and shears minimizes the
  mismatch.  Reports, per topology, the best fit and the resulting spectrum.

Inputs: command-line options (see --help).  Outputs: printed ranking.
"""
import argparse
import itertools
from math import gcd

import numpy as np
from scipy.optimize import differential_evolution

C_MEV_FM = 2 * np.pi * 197.3269804            # 2πħc in MeV·fm
LEPTONS = np.array([0.51099895, 105.6583755, 1776.86])     # MeV
DM21, DM31 = 7.53e-5, 2.51e-3                 # eV²
MNU_MAX = 0.45                                 # eV, direct limit (KATRIN)


def primitive(v):
    g = 0
    for x in v:
        g = gcd(g, abs(int(x)))
    return g == 1


def canonical(v):
    for x in v:
        if x != 0:
            return x > 0
    return False


def mode_table(N, sheets, K, closure):
    """Allowed primitive canonical modes: (vectors, charged flags)."""
    vecs, charged = [], []
    for d in range(N):                                   # single-axis
        v = [0] * N
        v[d] = 1
        vecs.append(v); charged.append(False)
    for (T, R) in sheets:                                # sheet modes
        for a, b in itertools.product(range(-K, K + 1), repeat=2):
            if a == 0 or b == 0:
                continue
            v = [0] * N
            v[T], v[R] = a, b
            if not (primitive(v) and canonical(v)):
                continue
            if closure == "asym":
                ch = b % a == 0
            else:
                ch = (b % a == 0) or (a % b == 0)
            vecs.append(v); charged.append(ch)
    return np.array(vecs, float), np.array(charged)


def masses(params, N, sheets, vecs):
    L = 10.0 ** params[:N]
    sig = params[N:]
    shift = np.zeros_like(vecs)
    for s, (T, R) in enumerate(sheets):
        shift[:, R] += sig[s] * vecs[:, T]
    k = (vecs - shift) / L
    return C_MEV_FM * np.sqrt((k ** 2).sum(axis=1))      # MeV


def match_leptons(mc, rule):
    """Charged masses chosen as (e, μ, τ) under the identification rule."""
    if rule == "strict":
        return mc[:3]
    rest = mc[1:]
    mu = rest[np.argmin(abs(np.log(rest / LEPTONS[1])))]
    tau = rest[np.argmin(abs(np.log(rest / LEPTONS[2])))]
    return np.array([mc[0], mu, tau])


def score(params, N, sheets, vecs, charged, detail=False, rule="strict"):
    m = masses(params, N, sheets, vecs)
    mc = np.sort(m[charged])
    mn = np.sort(m[~charged]) * 1e6                       # neutral in eV
    if len(mc) < 3 or len(mn) < 3:
        return 1e3
    picked = match_leptons(mc, rule)
    r_lep = np.log(picked / LEPTONS)
    d21 = mn[1] ** 2 - mn[0] ** 2
    d31 = mn[2] ** 2 - mn[0] ** 2
    if d21 <= 0:
        return 1e3
    r_nu = [np.log(d21 / DM21), np.log(d31 / DM31)]
    pen = max(0.0, np.log(mn[2] / MNU_MAX))
    loss = float(np.sum(r_lep ** 2) + np.sum(np.square(r_nu)) + pen ** 2)
    if detail:
        return loss, mc, mn, picked
    return loss


def topologies(N, max_sheets):
    pairs = list(itertools.combinations(range(N), 2))
    for choice in itertools.product((None, 0, 1), repeat=len(pairs)):
        sheets = [(p[0], p[1]) if c == 0 else (p[1], p[0])
                  for p, c in zip(pairs, choice) if c is not None]
        if 1 <= len(sheets) <= max_sheets:
            yield sheets


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--dims", type=int, default=3, help="number of compact dimensions N")
    p.add_argument("--max-sheets", type=int, default=3)
    p.add_argument("--closure", choices=["asym", "sym", "both"], default="both")
    p.add_argument("--K", type=int, default=4, help="max |circulation| enumerated")
    p.add_argument("--logL", type=float, nargs=2, default=[-5.0, 16.0], help="log10 size bounds (fm)")
    p.add_argument("--sigma", type=float, nargs=2, default=[-3.0, 3.0], help="shear bounds")
    p.add_argument("--maxiter", type=int, default=300)
    p.add_argument("--popsize", type=int, default=25)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--top", type=int, default=5)
    p.add_argument("--rule", choices=["strict", "loose"], default="strict",
                   help="identification rule (see module docstring)")
    a = p.parse_args()

    closures = ["asym", "sym"] if a.closure == "both" else [a.closure]
    results = []
    topos = list(topologies(a.dims, a.max_sheets))
    print(f"N={a.dims}, rule={a.rule}: {len(topos)} topologies × {len(closures)} closure rules", flush=True)
    for cl in closures:
        for i, sheets in enumerate(topos):
            vecs, charged = mode_table(a.dims, sheets, a.K, cl)
            bounds = [tuple(a.logL)] * a.dims + [tuple(a.sigma)] * len(sheets)
            res = differential_evolution(score, bounds, args=(a.dims, sheets, vecs, charged,
                                                              False, a.rule),
                                         maxiter=a.maxiter, popsize=a.popsize, seed=a.seed,
                                         tol=1e-10, polish=True)
            results.append((res.fun, cl, sheets, res.x))
            print(f"  [{cl}] topology {i + 1}/{len(topos)} sheets {sheets}: loss {res.fun:.3e}",
                  flush=True)
    results.sort(key=lambda r: r[0])
    print("\n#### best topologies")
    for loss, cl, sheets, x in results[:a.top]:
        vecs, charged = mode_table(a.dims, sheets, a.K, cl)
        _, mc, mn, picked = score(x, a.dims, sheets, vecs, charged, detail=True, rule=a.rule)
        print(f"\n== closure {cl}, sheets (tube→ring) {sheets}: loss {loss:.3e}")
        print("  sizes L (fm): " + ", ".join(f"{10 ** v:.4g}" for v in x[:a.dims]))
        print("  shears σ: " + ", ".join(f"{v:+.4f}" for v in x[a.dims:]))
        print("  matched e, μ, τ (MeV): " + ", ".join(f"{v:.6g}" for v in picked))
        extra = [v for v in mc if v < 1.05 * LEPTONS[2] and not np.any(np.isclose(v, picked))]
        print(f"  extra charged states below the τ: {len(extra)}"
              + (" (" + ", ".join(f"{v:.4g}" for v in extra[:12]) + (" …" if len(extra) > 12 else "") + " MeV)"
                 if extra else ""))
        print("  lightest neutral (meV): " + ", ".join(f"{v * 1e3:.4g}" for v in mn[:6]))
        d21, d31 = mn[1] ** 2 - mn[0] ** 2, mn[2] ** 2 - mn[0] ** 2
        print(f"  Δm²21 = {d21:.3e} eV², Δm²31 = {d31:.3e} eV², ratio {d31 / d21:.2f}")


if __name__ == "__main__":
    main()
