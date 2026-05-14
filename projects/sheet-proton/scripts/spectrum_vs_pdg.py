"""
Compare the corrugated-torus mass spectrum against the PDG light-hadron table.

Two modes:

  (default) Single-point mode — compute the spectrum at one (ε, χ), calibrate
            from a designated proton (m_t, m_r), match every predicted mode to its
            best PDG candidate within tolerance, and report matches/misses.

  --sweep   Parameter-grid mode — compute a "PDG fitness score" at each (ε, χ)
            on a grid, to check whether matches concentrate at a specific
            parameter point (real signal) or scatter (statistical coincidence
            from the dense spectrum). Outputs a CSV grid and a heatmap PNG.

Workflow (single-point):
  1. Compute the lowest-N eigenvalues of the Hill operator at given (ε, χ),
     using the Bloch-restricted Fourier solver from laplacian_spectrum.py.
  2. Calibrate the mass scale by demanding that one designated (m_t, m_r) mode
     matches the observed proton mass (938.27 MeV). This pins R_major in fm.
  3. Convert every eigenvalue to a physical mass (MeV).
  4. Match against a hard-coded PDG table of light hadrons (p, n, π, K, η, ρ,
     ω, φ, Δ, N* up to ~1500 MeV).
  5. Apply interpretation filters: flag harmonics that could be multi-nucleon;
     note unmatched modes (candidate "dark"); report missing observations.

This script does NOT use clover-mass.md's perturbative formula. It just
discretises the Hill operator and reads the spectrum directly — the
analytical predictions are comparison targets, not inputs.

Usage:
    python scripts/spectrum_vs_pdg.py [--epsilon E] [--chi CHI]
                                      [--proton-label "n,m"]
                                      [--mt-max MT] [--mr-max MR]
                                      [--match-tol MEV]

    python scripts/spectrum_vs_pdg.py --sweep
                                      [--sweep-eps "e1,e2,..."]
                                      [--sweep-chi "c1,c2,..."]
                                      [--proton-label "n,m"]

Outputs:
    Single-point: outputs/pdg_match_eps<E>_chi<C>.csv
    Sweep:        outputs/pdg_sweep_proton<n>,<m>.csv
                  outputs/pdg_sweep_proton<n>,<m>.png
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from laplacian_spectrum import hill_eigenvalues


# ----- PDG light-hadron table (mass in MeV, charge, common name) -----
# Stopping around 1.5 GeV; covers the cleanly-identified light particles.
PDG_LIGHT_HADRONS = [
    # (name, mass_MeV, charge, comment)
    ("p",         938.272,  +1, "proton (uud)"),
    ("n",         939.565,   0, "neutron (udd)"),
    ("π⁰",        134.977,   0, "pion (uū-dd̄)/√2"),
    ("π±",        139.570,  +1, "pion (ud̄ or dū)"),
    ("K±",        493.677,  +1, "kaon (us̄ or sū)"),
    ("K⁰",        497.611,   0, "kaon (ds̄)"),
    ("η",         547.862,   0, "eta (uū+dd̄−2ss̄)/√6"),
    ("ρ",         775.26 ,  +1, "rho-meson (vector, ~π content)"),
    ("ω",         782.65 ,   0, "omega-meson (vector, uū+dd̄)"),
    ("η'",        957.78 ,   0, "eta-prime"),
    ("φ",        1019.46 ,   0, "phi-meson (ss̄)"),
    ("Λ",        1115.683,   0, "lambda baryon (uds)"),
    ("Σ⁺",       1189.37 ,  +1, "sigma baryon (uus)"),
    ("Σ⁰",       1192.642,   0, "sigma baryon (uds)"),
    ("Σ⁻",       1197.449,  -1, "sigma baryon (dds)"),
    ("Δ⁺⁺",      1232.0  ,  +2, "delta resonance (uuu)"),
    ("Δ⁺",       1232.0  ,  +1, "delta resonance (uud, J=3/2)"),
    ("Δ⁰",       1232.0  ,   0, "delta resonance (udd, J=3/2)"),
    ("Δ⁻",       1232.0  ,  -1, "delta resonance (ddd)"),
    ("Ξ⁰",       1314.86 ,   0, "xi baryon (uss)"),
    ("Ξ⁻",       1321.71 ,  -1, "xi baryon (dss)"),
    ("N(1440)",  1440.0  ,  +1, "Roper resonance (uud excited)"),
    ("K*",        891.66 ,  +1, "K* vector meson (us̄)"),
    ("a₀(980)",   980.0  ,  +1, "scalar meson (ud̄)"),
    ("f₀(980)",   990.0  ,   0, "scalar meson (uū+dd̄)"),
]


# ----- Charge inference from (m_t, m_r) -----
def k_theta_label(m_t: int, m_r: int) -> float:
    """k_θ = m_r − m_t/3 (the boundary-identification wavenumber).

    Tube-first wave-mode labels per clover-quarks §0.3.
    """
    return m_r - m_t / 3.0


def fractional_charge(m_t: int, m_r: int) -> float:
    """Charge from third-integer-momentum reading (clover-quarks §11.5/§11.7).

    The wave-mode (m_t, m_r) has k_θ = m_r − m_t/3. The "fractional charge" reading:
      m_t mod 3 = 0  →  integer charge offset
      m_t mod 3 = 1  →  charge offset of −1/3 (or +2/3 if we read +2π/3 winding as +q)
      m_t mod 3 = 2  →  charge offset of −2/3 (or +1/3)

    This is an UNSETTLED conversion in the framework. We adopt the convention
    that the third-integer offset = charge mod 1, and read out the integer part
    from m_r. This means for (m_t, m_r), Q = (m_r − m_t/3) interpreted as a rational —
    the integer plus fractional contributions both come into the charge.

    NOTE: this is a best-guess convention; the framework does not pin a unique
    charge-from-(m_t, m_r) reading. The matches below should be read accordingly.
    """
    return m_r - m_t / 3.0  # Q identified with k_θ — provisional


# ----- Spectrum generation -----
def generate_spectrum(eps: float, chi: float, mt_max: int, mr_max: int,
                       N_grid: int = 1024) -> list:
    """Compute eigenvalues for wave-modes (m_t, m_r) with |m_t| ≤ mt_max,
    |m_r| ≤ mr_max. Tube-first convention per clover-quarks §0.3.

    Returns a list of (m_t, m_r, mu_squared) tuples sorted by mu_squared.
    """
    seen_k_v = {}  # k_v → eigenvalue list (avoid recomputing per sector)
    results = []
    for m_t in range(-mt_max, mt_max + 1):
        for m_r in range(-mr_max, mr_max + 1):
            if (m_t, m_r) == (0, 0):
                continue
            # Bloch sector is determined by k_v = q/3 where q = 3 m_r − 2 m_t
            # (per clover-mass.md §3); the Hill solver takes k_v as input
            # and the sector is set by p ≡ q (mod 3). Each (m_t, m_r) maps to
            # a specific (k_v, p) where p = m_t.
            k_v = m_r - 2 * m_t / 3.0
            p = m_t
            # Cache the eigenvalue list at each (k_v, sector) pair
            cache_key = (round(k_v * 9) / 9, m_t % 3)
            if cache_key not in seen_k_v:
                seen_k_v[cache_key] = hill_eigenvalues(k_v, eps, chi, N_grid, n_eigs=10)
            eigs = seen_k_v[cache_key]
            # The lowest eigenvalue in this (k_v, sector) corresponds to the
            # plane wave at smallest |p| in the sector. Pick the eigenvalue
            # closest to the predicted zeroth-order value.
            predicted_mu2 = k_v ** 2 + (p / eps) ** 2
            idx = int(np.argmin(np.abs(eigs - predicted_mu2)))
            results.append((m_t, m_r, float(eigs[idx])))
    results.sort(key=lambda x: x[2])
    return results


# ----- Calibrate physical mass scale from proton -----
def calibrate_scale(spectrum: list, proton_mt: int, proton_mr: int) -> tuple:
    """Find the proton candidate's μ² and return (R_major_fm, m_per_mu, mu_p).

    proton_mt, proton_mr: the tube and ring Bloch labels of the proton mode
    (tube-first convention).
    """
    for mt, mr, mu2 in spectrum:
        if (mt, mr) == (proton_mt, proton_mr):
            mu_p = np.sqrt(mu2)
            # m_p (in MeV) = μ_p * (ℏc / R_major). ℏc = 197.327 MeV·fm.
            # m_p_observed = 938.272 MeV ⇒ R_major = μ_p * 197.327 / 938.272
            R_fm = mu_p * 197.327 / 938.272
            m_per_mu = 938.272 / mu_p  # MeV per dimensionless μ
            return R_fm, m_per_mu, mu_p
    raise ValueError(f"Proton label (m_t, m_r) = ({proton_mt}, {proton_mr}) "
                     f"not in spectrum")


# ----- Matching predicted to observed -----
def match_spectrum_to_pdg(spectrum: list, m_per_mu: float, tol_mev: float):
    """For each predicted mode (m_t, m_r), find the closest PDG hadron
    within tol_mev. Returns (matches, unmatched_predictions, missing_observations).
    """
    predicted = [(mt, mr, np.sqrt(mu2) * m_per_mu, mu2) for mt, mr, mu2 in spectrum]
    matches = []
    unmatched = []
    for mt, mr, mass_mev, mu2 in predicted:
        # Find closest PDG entry
        best = None
        best_d = float("inf")
        for name, obs_mev, charge, comment in PDG_LIGHT_HADRONS:
            d = abs(mass_mev - obs_mev)
            if d < best_d:
                best_d = d
                best = (name, obs_mev, charge, comment)
        if best is not None and best_d < tol_mev:
            matches.append(((mt, mr), mass_mev, best, best_d))
        else:
            unmatched.append(((mt, mr), mass_mev, mu2))
    # Find PDG hadrons with no near match
    matched_obs_names = {m_best[0] for _, _, m_best, _ in matches}
    missing = [
        (name, obs_mev, charge, comment)
        for name, obs_mev, charge, comment in PDG_LIGHT_HADRONS
        if name not in matched_obs_names and obs_mev <= max(p[2] for p in predicted)
    ]
    return matches, unmatched, missing


# ----- Multi-particle filter -----
def is_likely_multinucleon(mass_mev: float, m_p: float = 938.272,
                            tol_mev: float = 30.0) -> int:
    """Return integer N if mass ≈ N · m_p within tol, else 0."""
    if mass_mev <= 0: return 0
    n_approx = round(mass_mev / m_p)
    if n_approx >= 2 and abs(mass_mev - n_approx * m_p) < tol_mev:
        return n_approx
    return 0


# NOTE: a future extension can add SM-composite recipes that sum constituent
# (m_t, m_r) labels (q̄ → (−m_t, −m_r)) and look up the resulting label in the
# spectrum. That requires first committing to clover quark-flavor identifications
# (u, d, and especially s/c/b/t), which is the open question in quark-flavor.md
# Mapping Clover.


# ----- Fitness scoring at a single (ε, χ) -----
def fitness_at_point(eps: float, chi: float, proton_mt: int, proton_mr: int,
                      mt_max: int, mr_max: int, tolerances_mev: list,
                      N_grid: int) -> dict:
    """Compute several PDG-fit metrics at one (ε, χ) point.

    Returns a dict with keys:
      R_fm, mu_p, n_matches_at_each_tol (dict tol→int), mean_abs_delta_at_each_tol,
      total_abs_delta_at_each_tol, max_predicted_mass_MeV.
    """
    spectrum = generate_spectrum(eps, chi, mt_max, mr_max, N_grid=N_grid)
    try:
        R_fm, m_per_mu, mu_p = calibrate_scale(spectrum, proton_mt, proton_mr)
    except ValueError:
        return None
    # Build predicted-mass list
    predicted_masses = []
    for n, m, mu2 in spectrum:
        mass = np.sqrt(max(mu2, 0)) * m_per_mu
        predicted_masses.append((n, m, mass))
    # For each PDG hadron, find closest predicted mode's |Δ|
    pdg_deltas = []
    for name, obs_mev, charge, _comment in PDG_LIGHT_HADRONS:
        if obs_mev > max(p[2] for p in predicted_masses):
            continue
        d_best = min(abs(mass - obs_mev) for _, _, mass in predicted_masses)
        pdg_deltas.append((name, obs_mev, d_best))
    # Compute per-tolerance metrics
    n_matches = {}
    mean_delta = {}
    total_delta = {}
    for tol in tolerances_mev:
        within = [d for _, _, d in pdg_deltas if d < tol]
        n_matches[tol] = len(within)
        if within:
            mean_delta[tol] = sum(within) / len(within)
            total_delta[tol] = sum(within)
        else:
            mean_delta[tol] = float("nan")
            total_delta[tol] = 0.0
    return {
        "R_fm": R_fm,
        "mu_p": mu_p,
        "n_matches": n_matches,
        "mean_delta": mean_delta,
        "total_delta": total_delta,
        "max_predicted_mass_MeV": max(p[2] for p in predicted_masses),
        "pdg_deltas": pdg_deltas,
    }


def run_sweep(args) -> None:
    """Sweep (ε, χ) over a grid and report fitness."""
    import matplotlib.pyplot as plt
    proton_mt, proton_mr = (int(x) for x in args.proton_label.split(","))
    eps_list = [float(x) for x in args.sweep_eps.split(",")]
    chi_list = [float(x) for x in args.sweep_chi.split(",")]
    tolerances = [10.0, 30.0, 80.0]

    print(f"# Clover spectrum × PDG fitness sweep")
    print(f"# Proton label (m_t, m_r) = ({proton_mt}, {proton_mr})  [tube-first per clover-quarks §0.3]")
    print(f"# ε grid: {eps_list}")
    print(f"# χ grid: {chi_list}")
    print(f"# Tolerances tested: {tolerances} MeV")
    print()

    n_eps, n_chi = len(eps_list), len(chi_list)
    n_matches_grid = {tol: np.zeros((n_chi, n_eps)) for tol in tolerances}
    mean_delta_grid = {tol: np.full((n_chi, n_eps), np.nan) for tol in tolerances}
    R_grid = np.zeros((n_chi, n_eps))

    rows = []
    for j, chi in enumerate(chi_list):
        for i, eps in enumerate(eps_list):
            print(f"  evaluating ε={eps:.3f}, χ={chi:.2f} ...", end="", flush=True)
            f = fitness_at_point(eps, chi, proton_mt, proton_mr,
                                  args.mt_max, args.mr_max, tolerances,
                                  N_grid=args.n_grid)
            if f is None:
                print(" SKIP (proton label not in spectrum)")
                continue
            R_grid[j, i] = f["R_fm"]
            for tol in tolerances:
                n_matches_grid[tol][j, i] = f["n_matches"][tol]
                mean_delta_grid[tol][j, i] = f["mean_delta"][tol]
            print(f" R={f['R_fm']:.3f} fm  "
                  f"matches@10={f['n_matches'][10]:2d}  "
                  f"@30={f['n_matches'][30]:2d}  "
                  f"@80={f['n_matches'][80]:2d}  "
                  f"meanΔ@30={f['mean_delta'][30]:.1f} MeV")
            rows.append((eps, chi, f))

    # Save CSV (filename uses tube-first label: mt,mr)
    args.outputs_dir.mkdir(parents=True, exist_ok=True)
    csv_path = args.outputs_dir / f"pdg_sweep_proton{proton_mt},{proton_mr}.csv"
    with open(csv_path, "w") as fout:
        cols = ["epsilon", "chi", "R_fm", "mu_p"]
        for tol in tolerances:
            cols += [f"n_matches_tol{int(tol)}", f"mean_delta_tol{int(tol)}",
                     f"total_delta_tol{int(tol)}"]
        fout.write(",".join(cols) + "\n")
        for eps, chi, f in rows:
            row = [f"{eps:.4f}", f"{chi:.4f}", f"{f['R_fm']:.4f}", f"{f['mu_p']:.4f}"]
            for tol in tolerances:
                row += [str(f["n_matches"][tol]),
                        f"{f['mean_delta'][tol]:.4f}",
                        f"{f['total_delta'][tol]:.4f}"]
            fout.write(",".join(row) + "\n")
    print(f"\nSaved: {csv_path}")

    # Heatmap PNG: 3 columns (one per tolerance), two rows (matches and mean Δ)
    fig, axes = plt.subplots(2, 3, figsize=(15, 8))
    for col, tol in enumerate(tolerances):
        ax = axes[0, col]
        im = ax.imshow(n_matches_grid[tol], origin="lower", aspect="auto",
                       extent=[min(eps_list), max(eps_list),
                               min(chi_list), max(chi_list)],
                       cmap="viridis")
        ax.set_title(f"# PDG matches within ±{int(tol)} MeV")
        ax.set_xlabel("ε")
        ax.set_ylabel("χ")
        # Annotate cells
        for j, chi in enumerate(chi_list):
            for i, eps in enumerate(eps_list):
                v = int(n_matches_grid[tol][j, i])
                ax.text(eps, chi, str(v), ha="center", va="center",
                        color="white" if v < n_matches_grid[tol].max() / 2 else "black",
                        fontsize=9)
        plt.colorbar(im, ax=ax)

        ax = axes[1, col]
        # Mean delta (lower is better); cap nan to a sentinel for plotting
        plot_md = np.where(np.isnan(mean_delta_grid[tol]), tol, mean_delta_grid[tol])
        im = ax.imshow(plot_md, origin="lower", aspect="auto",
                       extent=[min(eps_list), max(eps_list),
                               min(chi_list), max(chi_list)],
                       cmap="viridis_r")
        ax.set_title(f"mean |Δ| of matched (MeV), tol ±{int(tol)}")
        ax.set_xlabel("ε")
        ax.set_ylabel("χ")
        for j, chi in enumerate(chi_list):
            for i, eps in enumerate(eps_list):
                v = mean_delta_grid[tol][j, i]
                lbl = f"{v:.1f}" if not np.isnan(v) else "—"
                ax.text(eps, chi, lbl, ha="center", va="center",
                        color="white", fontsize=8)
        plt.colorbar(im, ax=ax)

    fig.suptitle(f"PDG fit vs (ε, χ); proton at (m_t, m_r) = ({proton_mt}, {proton_mr})")
    fig.tight_layout()
    png_path = args.outputs_dir / f"pdg_sweep_proton{proton_mt},{proton_mr}.png"
    fig.savefig(png_path, dpi=120, bbox_inches="tight")
    print(f"Saved: {png_path}")

    # Headline summary: best grid point per tolerance
    print()
    print(f"## Best grid points per tolerance")
    for tol in tolerances:
        # Best = most matches, then smallest mean Δ as tiebreaker
        best_j, best_i = np.unravel_index(np.argmax(n_matches_grid[tol]),
                                           n_matches_grid[tol].shape)
        best_eps = eps_list[best_i]
        best_chi = chi_list[best_j]
        n = int(n_matches_grid[tol][best_j, best_i])
        md = mean_delta_grid[tol][best_j, best_i]
        R = R_grid[best_j, best_i]
        print(f"  tol ±{int(tol)} MeV: best at ε={best_eps:.3f}, χ={best_chi:.2f} "
              f"→ {n} matches, mean |Δ|={md:.2f} MeV, R={R:.3f} fm")


# ----- Main -----
def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--epsilon", type=float, default=0.2,
                        help="Aspect ratio (default 0.2 — robust cluster value)")
    parser.add_argument("--chi", type=float, default=1.0,
                        help="Corrugation ratio (default 1.0)")
    parser.add_argument("--proton-label", type=str, default="2,1",
                        help="(m_t, m_r) tube-first wave-mode label assigned to "
                        "the proton, per clover-quarks §0.3. Default '2,1' = (m_t=2, m_r=1), "
                        "which corresponds to the old (n=1, m=2) under the pre-restart convention.")
    parser.add_argument("--mt-max", type=int, default=3,
                        help="|m_t| range (tube). Default 3.")
    parser.add_argument("--mr-max", type=int, default=3,
                        help="|m_r| range (ring). Default 3.")
    parser.add_argument("--match-tol", type=float, default=80.0,
                        help="Mass-match tolerance in MeV. Default 80.")
    parser.add_argument("--n-grid", type=int, default=1024)
    parser.add_argument("--sweep", action="store_true",
                        help="Run a parameter sweep over (ε, χ) instead of "
                        "a single-point report.")
    parser.add_argument("--sweep-eps", type=str,
                        default="0.10,0.15,0.20,0.25,0.30,0.40,0.50,0.70,1.00",
                        help="Comma-separated ε values to sweep.")
    parser.add_argument("--sweep-chi", type=str,
                        default="0.50,1.00,1.50,2.00",
                        help="Comma-separated χ values to sweep.")
    parser.add_argument("--outputs-dir", type=Path,
                        default=Path(__file__).resolve().parents[1] / "outputs")
    args = parser.parse_args()

    if args.sweep:
        run_sweep(args)
        return

    proton_mt, proton_mr = (int(x) for x in args.proton_label.split(","))

    print(f"# Clover-torus spectrum vs PDG light hadrons")
    print(f"# (ε, χ) = ({args.epsilon}, {args.chi})")
    print(f"# Proton label (m_t, m_r) = ({proton_mt}, {proton_mr})  [tube-first per clover-quarks §0.3]")
    print(f"# (m_t, m_r) range: |m_t| ≤ {args.mt_max}, |m_r| ≤ {args.mr_max}")
    print()

    # Generate spectrum
    spectrum = generate_spectrum(args.epsilon, args.chi, args.mt_max, args.mr_max,
                                  N_grid=args.n_grid)

    # Calibrate scale
    try:
        R_fm, m_per_mu, mu_p = calibrate_scale(spectrum, proton_mt, proton_mr)
    except ValueError as e:
        print(f"ERROR: {e}")
        sys.exit(1)

    print(f"Calibration: μ_p = {mu_p:.4f}, R_major = {R_fm:.4f} fm,"
          f"  m/μ = {m_per_mu:.2f} MeV per dimensionless mass unit")
    print(f"(observed R_p_charge = 0.84 fm — for comparison)")
    print()

    # Predicted spectrum in physical units
    print(f"## Predicted spectrum (lowest 25 modes)")
    print(f"{'(m_t, m_r)':>12}  {'k_θ':>8}  {'μ²':>10}  {'mass (MeV)':>12}  {'Q?':>6}  {'multi?':>8}")
    print("-" * 72)
    for mt, mr, mu2 in spectrum[:25]:
        mass = np.sqrt(max(mu2, 0)) * m_per_mu
        kth = k_theta_label(mt, mr)
        mn = is_likely_multinucleon(mass)
        multi_str = f"≈{mn}·p" if mn else ""
        Q = fractional_charge(mt, mr)
        print(f"({mt:+d}, {mr:+d})  {kth:+8.4f}  {mu2:10.5f}  {mass:12.2f}  "
              f"{Q:+6.3f}  {multi_str:>8}")

    # Match to PDG
    print()
    print(f"## Matches against PDG (tolerance {args.match_tol} MeV)")
    matches, unmatched, missing = match_spectrum_to_pdg(spectrum, m_per_mu, args.match_tol)
    print(f"{'(m_t, m_r)':>12}  {'Predicted (MeV)':>16}  {'Best PDG match':>20}  "
          f"{'Δ (MeV)':>10}")
    print("-" * 72)
    for (mt, mr), mass_mev, (name, obs_mev, charge, comment), d in matches:
        print(f"({mt:+d}, {mr:+d})  {mass_mev:16.2f}  {name + ' (' + str(obs_mev) + ')':>20}  "
              f"{d:+10.2f}")

    print()
    print(f"## Unmatched predicted modes (no PDG hadron within {args.match_tol} MeV):")
    print(f"{'(m_t, m_r)':>12}  {'Predicted (MeV)':>16}  {'Q (best guess)':>14}  "
          f"{'multinucleon?':>14}")
    print("-" * 72)
    for (mt, mr), mass_mev, mu2 in unmatched[:15]:
        mn = is_likely_multinucleon(mass_mev)
        multi_str = f"yes (≈{mn}·p)" if mn else "no"
        Q = fractional_charge(mt, mr)
        print(f"({mt:+d}, {mr:+d})  {mass_mev:16.2f}  {Q:14.3f}  {multi_str:>14}")

    print()
    print(f"## PDG hadrons with no nearby predicted mode (under mass ceiling):")
    print(f"{'Name':>10}  {'Observed (MeV)':>16}  {'Charge':>8}  Comment")
    print("-" * 72)
    for name, obs_mev, charge, comment in missing:
        print(f"{name:>10}  {obs_mev:16.2f}  {charge:+8d}  {comment}")

    # Save CSV
    args.outputs_dir.mkdir(parents=True, exist_ok=True)
    csv_path = args.outputs_dir / f"pdg_match_eps{args.epsilon:.2f}_chi{args.chi:.2f}.csv"
    with open(csv_path, "w") as f:
        f.write("m_t,m_r,k_theta,mu_squared,predicted_mass_MeV,charge_guess,multinucleon_N\n")
        for mt, mr, mu2 in spectrum:
            mass = np.sqrt(max(mu2, 0)) * m_per_mu
            kth = k_theta_label(mt, mr)
            mn = is_likely_multinucleon(mass)
            Q = fractional_charge(mt, mr)
            f.write(f"{mt},{mr},{kth:.6f},{mu2:.8f},{mass:.4f},{Q:.6f},{mn}\n")
    print()
    print(f"Saved: {csv_path}")


if __name__ == "__main__":
    main()
