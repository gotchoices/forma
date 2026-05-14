"""
Compare the corrugated-torus mass spectrum against the PDG light-hadron table.

Workflow:
  1. Compute the lowest-N eigenvalues of the Hill operator at given (ε, χ),
     using the Bloch-restricted Fourier solver from laplacian_spectrum.py.
  2. Calibrate the mass scale by demanding that one designated (n, m) mode
     matches the observed proton mass (938.27 MeV). This pins R_major in
     physical units (fm).
  3. Convert every eigenvalue to a physical mass (MeV).
  4. Match against a hard-coded PDG table of light hadrons (p, n, π, K, η, ρ,
     ω, φ, Δ, N* up to ~1500 MeV).
  5. Apply the user's interpretation filters:
       (F1) flag predicted modes at integer multiples of m_p as candidate
            multi-nucleon configurations, not new particles
       (F2) note neutral predicted modes with no observed match (candidate
            "dark" / decoupled)
       (F3) for SM composite recipes (q + q̄ for mesons, qqq for baryons),
            sum the (n, m) labels of the constituents and check whether the
            sum lands on an eigenmode
  6. Report matches, gaps, and over-predictions.

This script does NOT use clover-mass.md's perturbative formula. It just
discretises the Hill operator and reads the spectrum directly — the
analytical predictions are comparison targets, not inputs.

Usage:
    python scripts/spectrum_vs_pdg.py [--epsilon E] [--chi CHI]
                                      [--proton-label "n,m"]
                                      [--n-max N] [--m-max M]
                                      [--match-tol MEV]

Outputs:
    outputs/pdg_match_eps<E>_chi<C>.csv
    outputs/pdg_match_eps<E>_chi<C>.txt  (human-readable report)
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


# ----- Charge inference from (n, m) -----
def k_theta_label(n: int, m: int) -> float:
    """k_θ = n − m/3 (the boundary-identification wavenumber)."""
    return n - m / 3.0


def fractional_charge(n: int, m: int) -> float:
    """Charge from third-integer-momentum reading (clover-quarks §11.5/§11.7).

    The wave-mode (n, m) has k_θ = n − m/3. The "fractional charge" reading:
      m mod 3 = 0  →  integer charge offset (= n mod ??)
      m mod 3 = 1  →  charge offset of −1/3 (or +2/3 if we read +2π/3 winding as +q)
      m mod 3 = 2  →  charge offset of −2/3 (or +1/3)

    This is an UNSETTLED conversion in the framework. We adopt the convention
    that the third-integer offset = charge mod 1, and read out the integer part
    from n.  This means for (n, m), Q = (n − m/3) interpreted as a rational —
    the integer plus fractional contributions both come into the charge.

    NOTE: this is a best-guess convention; the framework does not pin a unique
    charge-from-(n,m) reading. The matches below should be read accordingly.
    """
    return n - m / 3.0  # Q identified with k_θ — provisional


# ----- Spectrum generation -----
def generate_spectrum(eps: float, chi: float, n_max: int, m_max: int,
                       N_grid: int = 1024) -> list:
    """Compute eigenvalues for (n, m) with |n| ≤ n_max, |m| ≤ m_max.

    Returns a list of (n, m, mu_squared) tuples sorted by mu_squared.
    """
    seen_k_v = {}  # k_v → eigenvalue list (avoid recomputing per sector)
    results = []
    for m in range(-m_max, m_max + 1):
        for n in range(-n_max, n_max + 1):
            if (n, m) == (0, 0):
                continue
            # Bloch sector is determined by k_v = q/3 where q = 3n − 2m
            # (per clover-mass.md §3); but the Hill solver takes k_v as input
            # and the sector is set by p ≡ q (mod 3). Each (n, m) maps to
            # a specific (k_v, p) where p = m.
            k_v = n - 2 * m / 3.0
            p = m
            # Cache the eigenvalue list at each (k_v, sector) pair
            cache_key = (round(k_v * 9) / 9, m % 3)
            if cache_key not in seen_k_v:
                seen_k_v[cache_key] = hill_eigenvalues(k_v, eps, chi, N_grid, n_eigs=10)
            eigs = seen_k_v[cache_key]
            # The lowest eigenvalue in this (k_v, sector) corresponds to the
            # plane wave at smallest |p| in the sector. Pick the eigenvalue
            # closest to the predicted zeroth-order value.
            predicted_mu2 = k_v ** 2 + (p / eps) ** 2
            idx = int(np.argmin(np.abs(eigs - predicted_mu2)))
            results.append((n, m, float(eigs[idx])))
    results.sort(key=lambda x: x[2])
    return results


# ----- Calibrate physical mass scale from proton -----
def calibrate_scale(spectrum: list, proton_n: int, proton_m: int) -> tuple:
    """Find the proton candidate's μ² and return (R_major_fm, m_per_mu)."""
    for n, m, mu2 in spectrum:
        if (n, m) == (proton_n, proton_m):
            mu_p = np.sqrt(mu2)
            # m_p (in MeV) = μ_p * (ℏc / R_major). ℏc = 197.327 MeV·fm.
            # m_p_observed = 938.272 MeV ⇒ R_major = μ_p * 197.327 / 938.272
            R_fm = mu_p * 197.327 / 938.272
            m_per_mu = 938.272 / mu_p  # MeV per dimensionless μ
            return R_fm, m_per_mu, mu_p
    raise ValueError(f"Proton label ({proton_n}, {proton_m}) not in spectrum")


# ----- Matching predicted to observed -----
def match_spectrum_to_pdg(spectrum: list, m_per_mu: float, tol_mev: float):
    """For each predicted mode, find the closest PDG hadron within tol_mev.

    Returns (matches, unmatched_predictions, missing_observations).
    """
    predicted = [(n, m, np.sqrt(mu2) * m_per_mu, mu2) for n, m, mu2 in spectrum]
    matches = []
    unmatched = []
    for n, m, mass_mev, mu2 in predicted:
        # Find closest PDG entry
        best = None
        best_d = float("inf")
        for name, obs_mev, charge, comment in PDG_LIGHT_HADRONS:
            d = abs(mass_mev - obs_mev)
            if d < best_d:
                best_d = d
                best = (name, obs_mev, charge, comment)
        if best is not None and best_d < tol_mev:
            matches.append(((n, m), mass_mev, best, best_d))
        else:
            unmatched.append(((n, m), mass_mev, mu2))
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
# (n, m) labels (q̄ → (−n, −m)) and look up the resulting label in the spectrum.
# That requires first committing to clover quark-flavor identifications (u, d,
# and especially s/c/b/t), which is the open question in quark-flavor.md
# Mapping Clover.


# ----- Main -----
def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--epsilon", type=float, default=0.2,
                        help="Aspect ratio (default 0.2 — robust cluster value)")
    parser.add_argument("--chi", type=float, default=1.0,
                        help="Corrugation ratio (default 1.0)")
    parser.add_argument("--proton-label", type=str, default="1,2",
                        help="(n, m) label assigned to the proton. Default '1,2'.")
    parser.add_argument("--n-max", type=int, default=3, help="|n| range. Default 3.")
    parser.add_argument("--m-max", type=int, default=3, help="|m| range. Default 3.")
    parser.add_argument("--match-tol", type=float, default=80.0,
                        help="Mass-match tolerance in MeV. Default 80.")
    parser.add_argument("--n-grid", type=int, default=1024)
    parser.add_argument("--outputs-dir", type=Path,
                        default=Path(__file__).resolve().parents[1] / "outputs")
    args = parser.parse_args()

    proton_n, proton_m = (int(x) for x in args.proton_label.split(","))

    print(f"# Clover-torus spectrum vs PDG light hadrons")
    print(f"# (ε, χ) = ({args.epsilon}, {args.chi})")
    print(f"# Proton label: (n, m) = ({proton_n}, {proton_m})")
    print(f"# (n, m) range: |n| ≤ {args.n_max}, |m| ≤ {args.m_max}")
    print()

    # Generate spectrum
    spectrum = generate_spectrum(args.epsilon, args.chi, args.n_max, args.m_max,
                                  N_grid=args.n_grid)

    # Calibrate scale
    try:
        R_fm, m_per_mu, mu_p = calibrate_scale(spectrum, proton_n, proton_m)
    except ValueError as e:
        print(f"ERROR: {e}")
        sys.exit(1)

    print(f"Calibration: μ_p = {mu_p:.4f}, R_major = {R_fm:.4f} fm,"
          f"  m/μ = {m_per_mu:.2f} MeV per dimensionless mass unit")
    print(f"(observed R_p_charge = 0.84 fm — for comparison)")
    print()

    # Predicted spectrum in physical units
    print(f"## Predicted spectrum (lowest 25 modes)")
    print(f"{'(n, m)':>10}  {'k_θ':>8}  {'μ²':>10}  {'mass (MeV)':>12}  {'Q?':>6}  {'multi?':>8}")
    print("-" * 70)
    for n, m, mu2 in spectrum[:25]:
        mass = np.sqrt(max(mu2, 0)) * m_per_mu
        kth = k_theta_label(n, m)
        mn = is_likely_multinucleon(mass)
        multi_str = f"≈{mn}·p" if mn else ""
        Q = fractional_charge(n, m)
        print(f"({n:+d}, {m:+d})  {kth:+8.4f}  {mu2:10.5f}  {mass:12.2f}  "
              f"{Q:+6.3f}  {multi_str:>8}")

    # Match to PDG
    print()
    print(f"## Matches against PDG (tolerance {args.match_tol} MeV)")
    matches, unmatched, missing = match_spectrum_to_pdg(spectrum, m_per_mu, args.match_tol)
    print(f"{'(n, m)':>10}  {'Predicted (MeV)':>16}  {'Best PDG match':>20}  "
          f"{'Δ (MeV)':>10}")
    print("-" * 70)
    for (n, m), mass_mev, (name, obs_mev, charge, comment), d in matches:
        print(f"({n:+d}, {m:+d})  {mass_mev:16.2f}  {name + ' (' + str(obs_mev) + ')':>20}  "
              f"{d:+10.2f}")

    print()
    print(f"## Unmatched predicted modes (no PDG hadron within {args.match_tol} MeV):")
    print(f"{'(n, m)':>10}  {'Predicted (MeV)':>16}  {'Q (best guess)':>14}  "
          f"{'multinucleon?':>14}")
    print("-" * 70)
    for (n, m), mass_mev, mu2 in unmatched[:15]:
        mn = is_likely_multinucleon(mass_mev)
        multi_str = f"yes (≈{mn}·p)" if mn else "no"
        Q = fractional_charge(n, m)
        print(f"({n:+d}, {m:+d})  {mass_mev:16.2f}  {Q:14.3f}  {multi_str:>14}")

    print()
    print(f"## PDG hadrons with no nearby predicted mode (under mass ceiling):")
    print(f"{'Name':>10}  {'Observed (MeV)':>16}  {'Charge':>8}  Comment")
    print("-" * 70)
    for name, obs_mev, charge, comment in missing:
        print(f"{name:>10}  {obs_mev:16.2f}  {charge:+8d}  {comment}")

    # Save CSV
    args.outputs_dir.mkdir(parents=True, exist_ok=True)
    csv_path = args.outputs_dir / f"pdg_match_eps{args.epsilon:.2f}_chi{args.chi:.2f}.csv"
    with open(csv_path, "w") as f:
        f.write("n,m,k_theta,mu_squared,predicted_mass_MeV,charge_guess,multinucleon_N\n")
        for n, m, mu2 in spectrum:
            mass = np.sqrt(max(mu2, 0)) * m_per_mu
            kth = k_theta_label(n, m)
            mn = is_likely_multinucleon(mass)
            Q = fractional_charge(n, m)
            f.write(f"{n},{m},{kth:.6f},{mu2:.8f},{mass:.4f},{Q:.6f},{mn}\n")
    print()
    print(f"Saved: {csv_path}")


if __name__ == "__main__":
    main()
