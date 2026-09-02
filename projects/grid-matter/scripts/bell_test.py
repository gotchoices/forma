"""
Toy Bell/CHSH test of the fiber-self-consistency measurement model.

Question (see work/measurement-and-bell.md): can the compact-fiber hidden variable
reproduce the *exact* quantum correlation E(a,b)=cos(a-b) (CHSH = 2*sqrt(2)) with
NO signaling -- and is a *local* shared fiber phase enough, or must the fiber be
genuinely non-local (global)?

Two entangled particles share a fiber phase lam (fixed at pair creation). Each is
measured at a freely chosen setting (a, b). Three models:

  local     : outcomes are LOCAL functions A(a,lam), B(b,lam). This is the naive
              "shared fiber phase" -- a local hidden variable. Bell says it CANNOT
              exceed CHSH=2, and cannot trace the cosine.
  nonlocal  : the fiber is a GLOBAL condition -- the outcome correlation depends on
              BOTH settings (a-b) as the fiber self-consistency requires. Built to
              be no-signaling (each marginal stays 50/50). Tests whether a non-local
              fiber CAN reach QM with no signaling. (Rule put in by hand -- this
              tests the STRUCTURE, it does not derive cos from fiber dynamics.)
  qm        : the reference, E=cos(a-b).

Reports the CHSH value for each, the correlation curve E vs (a-b), and a
no-signaling check (marginals independent of the far setting).
"""
import argparse
import os
import numpy as np


def outcomes(model, a, b, lam, rng):
    if model == "local":
        # local hidden variable: each side sees only its own setting + shared lam
        A = np.sign(np.cos(lam - a))
        B = np.sign(np.cos(lam - b))
        return A, B
    if model == "nonlocal":
        # fiber is a global condition: A is a fair coin from the fiber; B is
        # correlated to A with P(B=A)=cos^2((a-b)/2) -- QM's rule, no-signaling.
        A = np.where(np.cos(lam) >= 0, 1.0, -1.0)
        p_same = np.cos((a - b) / 2.0) ** 2
        same = rng.random(len(lam)) < p_same
        B = np.where(same, A, -A)
        return A, B
    raise ValueError(model)


def corr(model, a, b, N, rng):
    lam = rng.uniform(-np.pi, np.pi, N)
    if model == "qm":
        E = np.cos(a - b)
        return E, 0.0, 0.0
    A, B = outcomes(model, a, b, lam, rng)
    return float(np.mean(A * B)), float(np.mean(A)), float(np.mean(B))


def chsh(model, N, rng):
    a, ap, b, bp = 0.0, np.pi / 2, np.pi / 4, 3 * np.pi / 4
    e1 = corr(model, a, b, N, rng)[0]
    e2 = corr(model, a, bp, N, rng)[0]
    e3 = corr(model, ap, b, N, rng)[0]
    e4 = corr(model, ap, bp, N, rng)[0]
    return abs(e1 - e2 + e3 + e4)


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--N", type=int, default=400000)
    p.add_argument("--seed", type=int, default=3)
    p.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "outputs"))
    args = p.parse_args()
    rng = np.random.default_rng(args.seed)

    print("CHSH (classical bound 2, quantum/Tsirelson bound 2.828):")
    for m in ("local", "nonlocal", "qm"):
        print(f"  {m:>9}: CHSH = {chsh(m, args.N, rng):.3f}")

    # no-signaling: does side-A's marginal depend on side-B's setting?
    print("\nno-signaling check (mean of A for two different far settings b):")
    for m in ("local", "nonlocal"):
        _, mA1, _ = corr(m, 0.0, 0.0, args.N, rng)
        _, mA2, _ = corr(m, 0.0, np.pi / 2, args.N, rng)
        print(f"  {m:>9}: <A>|b=0 = {mA1:+.3f}, <A>|b=90 = {mA2:+.3f}  "
              f"-> {'no signaling' if abs(mA1 - mA2) < 0.01 else 'SIGNALS!'}")

    # correlation curve E vs (a-b)
    dth = np.linspace(0, np.pi, 25)
    curves = {}
    for m in ("local", "nonlocal", "qm"):
        curves[m] = np.array([corr(m, 0.0, -d, args.N // 4, rng)[0] for d in dth])
    print("\nE(a-b): local is a straight-line 'triangle'; nonlocal & qm are cosines.")

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        outdir = os.path.abspath(args.out); os.makedirs(outdir, exist_ok=True)
        fig, ax = plt.subplots(figsize=(6.4, 4.6))
        for m, style in (("local", "b.-"), ("nonlocal", "r.-"), ("qm", "k--")):
            ax.plot(dth * 180 / np.pi, curves[m], style, label=m, lw=1.2, ms=4)
        ax.set_xlabel("angle a-b (deg)"); ax.set_ylabel("E(a,b)")
        ax.set_title("Bell correlation: local fiber (Bell-bound) vs non-local fiber = QM")
        ax.legend(); ax.grid(alpha=0.3)
        fig.tight_layout()
        png = os.path.join(outdir, "bell_test.png")
        fig.savefig(png, dpi=110); print(f"\n  saved {png}")
    except Exception as e:
        print(f"  (plot skipped: {e})")


if __name__ == "__main__":
    main()
