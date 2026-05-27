"""
track_localization.py — does the 2D wave equation reduce to a 1D wave
on the characteristic curves of the modulated-clover surface?

Question (work/derived-clover.md gap 2): the Step-7 path-length mass
formula m = 2π ℏ c / L treats each closed (1/2,1) track as if it carried
a 1D standing wave.  The Step-4 attempt to read the proton/neutron
mass from a 2D Laplace–Beltrami (LB) eigenvalue failed.  This script
asks the *structural* question that bridges them:

  In the semi-classical (high-eigenvalue) regime, is there a sequence of
  LB eigenmodes whose support concentrates on the union of the closed
  characteristic curves t(θ) = t₀ + θ/2  ?

A positive answer would say: the 2D theory itself produces 1D-on-track
wave packets in the WKB limit, and the path-length formula is the
high-frequency consequence of the 2D wave equation, not a separate
ansatz.

A negative answer would say: there is no track-localised eigenmode
band — the modes are essentially delocalised on the full 2D sheet
no matter how high we go.  In that case Reading α (single quantum
in 3-mode superposition, mass = E) is structurally blocked and
Reading β (multi-quantum, fermionic spinor upgrade, mass = N E)
becomes the live alternative.

Method:
  1. Build the Z₂×Z₃-symmetric modulated-clover mesh using the
     parameters found by modulated_clover.py --step 7 --symmetric.
  2. Compute K LB eigenmodes via scipy.sparse.linalg.eigsh, sweeping
     from low to mid-range eigenvalues.
  3. Build the characteristic-curve set: 6 t₀ values in [0, 2π) that
     are the (Z₂ × Z₃)-orbit of the proton seed t₀ = -π/6, each
     traced as t(θ) = t₀ + θ/2 for θ ∈ [0, 2π).
  4. For each eigenmode ψ_i, compute the *enrichment* metric
        E_i = ⟨w⟩_{|ψ_i|²} / ⟨w⟩_uniform,
     where w(v) = exp(-d(v)²/(2σ²)) is a Gaussian tube around the
     curve set in parameter (t, θ) space and ⟨·⟩ uses the lumped
     mass matrix.  E_i = 1 means uniform; E_i > 1 means concentrated
     near the tracks.
  5. Plot E_i vs eigenvalue index and vs eigenvalue.  If the
     envelope of E_i grows with index, that is evidence for
     semiclassical track-localisation.  Also write a CSV with the
     full eigenvalue/enrichment list.

Outputs:
  outputs/track_localization.csv
  outputs/track_localization.png
  outputs/track_localization.txt   (summary)

Usage:
  python scripts/track_localization.py [--K 80] [--nt 96] [--ntheta 96]
                                        [--sigma 0.10]
"""
from __future__ import annotations

import argparse
import sys
from math import pi
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from modulated_clover import build_surface_mesh, cotan_laplacian


# Z₂ × Z₃-symmetric Step-7 solution (work/modulated-clover.md §11, §12).
# Identified by modulated_clover.py --step 7 --symmetric.
SYM_PARAMS = dict(
    Ac=np.array([0.0, -0.48765]),
    As=np.array([0.0, +0.65694]),
    Bc=np.array([0.0, -0.00038]),
    Bs=np.array([0.0, +0.00032]),
    a2=0.32994,
    b2=0.03201,
    rho=1.0,
    Rmajor=36.17,                       # path-length-mass solution
)

# (Z₂ × Z₃)-orbit of the proton seed t₀ = -π/6.  Six closed (1/2,1) tracks
# in the symmetric subspace; under the half-twist t₀ ~ t₀ + π they
# collapse to three distinct closed curves in 3D.
T0_ORBIT = np.array([-pi / 6.0, +pi / 6.0,
                     +pi / 2.0, -pi / 2.0,
                     +5.0 * pi / 6.0, -5.0 * pi / 6.0])


def grid_params(Nt: int, Nth: int):
    """Return per-vertex (t, θ) parameter values for the surface_vertices
    layout (vertex index i*Nth + j, with i along t, j along θ)."""
    t = np.linspace(0.0, 2 * pi, Nt, endpoint=False)
    th = np.linspace(0.0, 2 * pi, Nth, endpoint=False)
    T, TH = np.meshgrid(t, th, indexing="ij")
    return T.ravel(), TH.ravel()


def track_distance(t_v: np.ndarray, th_v: np.ndarray) -> np.ndarray:
    """Minimum parameter-space distance from each vertex to the union
    of characteristic curves t(θ) = t₀ + θ/2 (t₀ ∈ T0_ORBIT), modulo 2π."""
    d = np.full_like(t_v, np.inf)
    for t0 in T0_ORBIT:
        delta = (t_v - t0 - th_v / 2.0) % (2 * pi)
        delta = np.minimum(delta, 2 * pi - delta)
        d = np.minimum(d, delta)
    return d


def enrichment(eigvecs: np.ndarray, mass_diag: np.ndarray,
               weight: np.ndarray) -> np.ndarray:
    """For each eigenvector column ψ_i, compute
        E_i = (Σ_v m_v w_v ψ_v²) / (Σ_v m_v ψ_v²)  /  (Σ_v m_v w_v / Σ_v m_v)
    The first ratio is ⟨w⟩ under the |ψ|² measure; the second is ⟨w⟩
    under the uniform area measure.  E_i = 1 for a uniformly-spread
    mode, E_i > 1 for a track-localised mode."""
    psi2 = eigvecs ** 2                              # [V, K]
    num = (mass_diag[:, None] * weight[:, None] * psi2).sum(axis=0)
    den = (mass_diag[:, None] * psi2).sum(axis=0)
    mode_avg_w = num / np.maximum(den, 1e-30)
    uniform_avg_w = (mass_diag * weight).sum() / mass_diag.sum()
    return mode_avg_w / uniform_avg_w


def main():
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--K", type=int, default=80,
                    help="number of LB eigenmodes to compute (default 80)")
    ap.add_argument("--nt", type=int, default=96,
                    help="tube-direction mesh resolution (default 96, must be even)")
    ap.add_argument("--ntheta", type=int, default=96,
                    help="ring-direction mesh resolution (default 96)")
    ap.add_argument("--sigma", type=float, default=0.10,
                    help="Gaussian tube half-width in (t, θ) space (radians, default 0.10)")
    args = ap.parse_args()

    # ---- mesh + LB operator ----
    print(f"Building mesh ({args.nt} x {args.ntheta} = "
          f"{args.nt * args.ntheta} vertices) ...", flush=True)
    verts, tris = build_surface_mesh(
        SYM_PARAMS["Ac"], SYM_PARAMS["As"],
        SYM_PARAMS["Bc"], SYM_PARAMS["Bs"],
        SYM_PARAMS["a2"], SYM_PARAMS["b2"],
        SYM_PARAMS["rho"], SYM_PARAMS["Rmajor"],
        args.nt, args.ntheta)
    L, M = cotan_laplacian(verts, tris)
    mass_diag = np.asarray(M.diagonal()).ravel()
    area_total = float(mass_diag.sum())

    # ---- eigenmodes ----
    from scipy.sparse.linalg import eigsh
    print(f"Solving for {args.K} LB eigenmodes ...", flush=True)
    eigvals, eigvecs = eigsh(L, k=args.K, M=M, sigma=-1e-5, which="LM")
    order = np.argsort(np.real(eigvals))
    eigvals = np.real(eigvals[order])
    eigvecs = np.real(eigvecs[:, order])

    # ---- characteristic-curve weight ----
    t_v, th_v = grid_params(args.nt, args.ntheta)
    d = track_distance(t_v, th_v)
    sigma = args.sigma
    weight = np.exp(-0.5 * (d / sigma) ** 2)

    # Sanity: weight should be O(σ × n_tracks) fraction of total area
    tube_fraction = (mass_diag * weight).sum() / mass_diag.sum()
    print(f"  tube area fraction = {tube_fraction:.4f} "
          f"(σ = {sigma:.3f} rad)", flush=True)

    # ---- enrichment per mode ----
    print("Computing enrichment metric per mode ...", flush=True)
    E = enrichment(eigvecs, mass_diag, weight)

    # ---- best-localizable superposition: localisation vs energy ----
    # For φ = Σ c_i ψ_i (M-orthonormal ψ_i), the enrichment
    #   E(φ) = (Σ_ij c_i c_j W_ij) / (Σ_i c_i²) / ⟨w⟩_uniform
    # where W_ij = Σ_v m_v w_v ψ_iv ψ_jv.  Reading α posits the proton
    # is a *superposition* of low LB modes; the diagnostic is therefore
    # how localized we can make a normalised state while keeping its
    # energy ⟨H⟩ = Σ c_i² λ_i bounded.  The trade-off curve comes from
    # the generalized eigenproblem  W c = ξ (Λ + (1/μ) I) c  parameterised
    # by Lagrange multiplier μ ≥ 0; equivalently the largest eigenvalue
    # of (W - μ Λ) at each μ.
    print("Building W matrix and computing localisation-vs-energy trade-off ...",
          flush=True)
    mw = mass_diag * weight                                   # [V]
    psi_w = eigvecs * mw[:, None]                             # [V, K]
    W = eigvecs.T @ psi_w                                     # [K, K], symmetric
    W = 0.5 * (W + W.T)
    uniform_avg_w = mw.sum() / mass_diag.sum()

    # 1. Unconstrained best.
    w_eigvals, w_eigvecs = np.linalg.eigh(W)
    E_sub_max = w_eigvals[-1] / uniform_avg_w
    c_best = w_eigvecs[:, -1]
    energy_best = float(np.sum(c_best**2 * eigvals))

    # 2. Truncation sweep: best superposition within the first n_trunc modes.
    Lambda = np.diag(eigvals)
    trunc_levels = sorted(set([5, 10, 20, 40, 80, 160, args.K]))
    trunc_levels = [k for k in trunc_levels if 2 <= k <= args.K]
    trunc_results = []
    for k in trunc_levels:
        Wk = W[:k, :k]
        eigv_k, eigvec_k = np.linalg.eigh(Wk)
        c_k = eigvec_k[:, -1]
        e_k = eigv_k[-1] / uniform_avg_w
        en_k = float(np.sum(c_k**2 * eigvals[:k]))
        trunc_results.append((k, e_k, en_k))

    # ---- output ----
    out_dir = Path(__file__).resolve().parents[1] / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)

    csv_path = out_dir / "track_localization.csv"
    with csv_path.open("w") as f:
        f.write("index,eigenvalue,sqrt_eigenvalue,enrichment\n")
        for i, (lam, e) in enumerate(zip(eigvals, E)):
            sl = float(np.sqrt(max(lam, 0.0)))
            f.write(f"{i},{lam:.8e},{sl:.8e},{e:.6f}\n")
    print(f"Wrote: {csv_path}", flush=True)

    # ---- plot ----
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    sqrt_eig = np.sqrt(np.maximum(eigvals, 0.0))
    axes[0].plot(np.arange(len(E)), E, "o-", markersize=3)
    axes[0].axhline(1.0, ls="--", color="gray", lw=0.8,
                    label="uniform mode baseline")
    axes[0].set_xlabel("eigenmode index (sorted by eigenvalue)")
    axes[0].set_ylabel("track enrichment E = ⟨w⟩_ψ / ⟨w⟩_uniform")
    axes[0].set_title("Localisation vs mode index")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(sqrt_eig, E, "o-", markersize=3)
    axes[1].axhline(1.0, ls="--", color="gray", lw=0.8)
    axes[1].set_xlabel("√eigenvalue (wave-number scale)")
    axes[1].set_ylabel("track enrichment E")
    axes[1].set_title("Localisation vs wave-number")
    axes[1].grid(True, alpha=0.3)

    fig.suptitle(f"Modulated-clover LB modes: track localisation "
                 f"(K={args.K}, σ={sigma:.3f} rad, "
                 f"tube fraction={tube_fraction:.3f})")
    fig.tight_layout()
    png_path = out_dir / "track_localization.png"
    fig.savefig(png_path, dpi=120)
    print(f"Wrote: {png_path}", flush=True)

    # ---- mode visualizations in (t, θ) parameter space ----
    # Pick a few representative modes: lowest few, mid-range, and the
    # most-enriched.  Plot |ψ|² on the (t, θ) grid with characteristic
    # curves overlaid.  This is the eyeball test for localisation.
    top_e_idx = int(np.argmax(E))
    sample_indices = sorted(set([1, 2, 5, 10, args.K // 4,
                                  args.K // 2, top_e_idx, args.K - 1]))
    sample_indices = [i for i in sample_indices if 0 <= i < args.K]
    ncols = 4
    nrows = (len(sample_indices) + ncols - 1) // ncols
    figv, axv = plt.subplots(nrows, ncols, figsize=(4.0 * ncols, 3.2 * nrows))
    axv = np.atleast_2d(axv).ravel()
    T_mesh = t_v.reshape(args.nt, args.ntheta)
    TH_mesh = th_v.reshape(args.nt, args.ntheta)
    for k, idx in enumerate(sample_indices):
        psi2 = (eigvecs[:, idx] ** 2).reshape(args.nt, args.ntheta)
        ax = axv[k]
        im = ax.pcolormesh(TH_mesh, T_mesh, psi2, shading="auto", cmap="viridis")
        # overlay the 6 characteristic curves
        th_line = np.linspace(0, 2 * pi, 200)
        for t0 in T0_ORBIT:
            tline = (t0 + th_line / 2.0) % (2 * pi)
            # break the line where it wraps to avoid spurious segments
            jumps = np.where(np.abs(np.diff(tline)) > pi)[0]
            segs = np.split(np.arange(len(tline)), jumps + 1)
            for s in segs:
                ax.plot(th_line[s], tline[s], color="white", lw=0.7, alpha=0.7)
        ax.set_title(f"idx={idx}  λ={eigvals[idx]:.3e}  E={E[idx]:.3f}",
                     fontsize=9)
        ax.set_xlabel("θ")
        ax.set_ylabel("t")
        ax.set_xlim(0, 2 * pi)
        ax.set_ylim(0, 2 * pi)
    for k in range(len(sample_indices), len(axv)):
        axv[k].axis("off")
    figv.suptitle("|ψ_i|² in (t, θ) parameter space (white lines = characteristic tracks)")
    figv.tight_layout()
    modes_png = out_dir / "track_localization_modes.png"
    figv.savefig(modes_png, dpi=110)
    print(f"Wrote: {modes_png}", flush=True)

    # ---- summary ----
    R = []
    R.append("=" * 78)
    R.append("track_localization.py — LB-mode track localisation on the")
    R.append("Z₂ × Z₃-symmetric modulated-clover (work/derived-clover.md gap 2).")
    R.append("=" * 78)
    R.append("")
    R.append(f"mesh:        {args.nt} x {args.ntheta} = {args.nt*args.ntheta} vertices")
    R.append(f"R_major:     {SYM_PARAMS['Rmajor']:.4f}")
    R.append(f"K modes:     {args.K}")
    R.append(f"σ (rad):     {sigma:.4f}")
    R.append(f"tube area:   {tube_fraction:.4f}  (fraction of total surface area)")
    R.append(f"total area:  {area_total:.4f}")
    R.append("")
    # Calibration: a perfectly-track-confined mode (|ψ|² = w) has known E_max.
    # E_max = (∫ m·w² dA / ∫ m·w dA) / (∫ m·w dA / ∫ m dA)
    #       = (Σ m_v w_v²) (Σ m_v) / (Σ m_v w_v)²
    e_max_perfect = ((mass_diag * weight**2).sum() * mass_diag.sum()
                     / (mass_diag * weight).sum()**2)
    R.append(f"calibration:  a perfectly-tube-confined |ψ|² = w would give")
    R.append(f"              E_perfect = {e_max_perfect:.4f}")
    R.append(f"              (E = 1.0 means uniform; E = E_perfect means")
    R.append(f"               every bit of probability sits in the tube)")
    R.append("")
    R.append(f"observed enrichment range:  min = {E.min():.4f}   max = {E.max():.4f}")
    R.append(f"observed enrichment mean:   {E.mean():.4f}   median = {np.median(E):.4f}")
    R.append(f"observed localisation depth (individual modes):")
    R.append(f"  (E_max - 1) / (E_perfect - 1) = "
             f"{(E.max() - 1) / (e_max_perfect - 1):.4f}")
    R.append("")
    R.append(f"best-localized superposition within the K-mode subspace:")
    R.append(f"  max E over normalised c in span(ψ_1, ..., ψ_K)  =  {E_sub_max:.4f}")
    R.append(f"  subspace localisation depth = "
             f"{(E_sub_max - 1) / (e_max_perfect - 1):.4f}")
    R.append(f"  energy of best superposition ⟨H⟩ = Σ cᵢ² λᵢ = {energy_best:.4e}")
    R.append("")
    R.append(f"localisation-vs-energy trade-off (truncation sweep):")
    R.append(f"  Truncate to first n_trunc modes; report max E achievable")
    R.append(f"  inside that subspace and ⟨H⟩ of the localising state.")
    R.append(f"  Path-length wavenumber 2π/L_track ≈ 0.028  (so the proton")
    R.append(f"  energy is λ_p ≈ 7.8e-4 — orders of magnitude below.)")
    R.append("")
    R.append(f"  {'n_trunc':>8}  {'max E':>8}  {'depth':>8}  {'⟨H⟩':>12}  {'√⟨H⟩':>8}")
    for k, e_k, en_k in trunc_results:
        depth_k = (e_k - 1) / (e_max_perfect - 1)
        sqrt_e = float(np.sqrt(max(en_k, 0.0)))
        R.append(f"  {k:>8d}  {e_k:>8.4f}  {depth_k:>8.4f}  "
                 f"{en_k:>12.4e}  {sqrt_e:>8.4f}")
    R.append("")
    # Localisation envelope vs mode index: linear regression of E vs index
    # for the upper half, to look for a growth trend.
    half = len(E) // 2
    if half > 4:
        idx = np.arange(half, len(E))
        slope, intercept = np.polyfit(idx, E[half:], 1)
        R.append(f"upper-half trend (linear fit of E vs index, last {len(E)-half} modes):")
        R.append(f"  E ≈ {slope:+.5f} · index + {intercept:.4f}")
        R.append(f"  slope > 0 ⇒ enrichment growing with mode index (localising)")
        R.append(f"  slope ≤ 0 ⇒ enrichment flat or decaying (no localisation)")
    R.append("")
    top = np.argsort(E)[::-1][:10]
    R.append("top-10 most-enriched modes (mode index, eigenvalue, E):")
    for i in top:
        R.append(f"  idx={i:>4d}   λ={eigvals[i]:>10.4e}   E={E[i]:.4f}")
    R.append("")
    R.append("INTERPRETATION GUIDE:")
    R.append(f"  Individual-mode panel:")
    R.append(f"    - E ≈ 1 throughout:   no single eigenmode track-localises.")
    R.append(f"    - E grows with index: semiclassical localisation at high k.")
    R.append(f"  Truncation-sweep panel:")
    R.append(f"    - The localising state's energy ⟨H⟩ vs proton wavenumber")
    R.append(f"      (2π/L_track ≈ 0.028 in script units) sets whether the")
    R.append(f"      proton can be a track-localised superposition.")
    R.append(f"    - depth < 0.01 at proton energy ⇒ Reading α is structurally")
    R.append(f"      blocked on this substrate; Reading β is the live alternative.")
    R.append(f"  See work/lb-mode-localization.md for the full discussion.")

    text = "\n".join(R)
    print()
    print(text)
    out_path = out_dir / "track_localization.txt"
    out_path.write_text(text + "\n")
    print(f"\nWrote: {out_path}")


if __name__ == "__main__":
    main()
