"""
6-dim shared-MaSt structural test for work/ma-share-6.md.

Tests whether a 6-dim compact topology (3 sheet-unique + 3 sheet-pair-shared
dims) can reproduce the observed 12-fermion mass spectrum under bare 2D-planar
mode quantization on each sheet's three coordinate planes.

Topology:
    e-sheet uses: (U_e, S_ep, S_eν)
    p-sheet uses: (U_p, S_ep, S_pν)
    ν-sheet uses: (U_ν, S_eν, S_pν)

Each pair of sheets shares one compact dimension. The hypothesis: cross-sheet
mass clustering (tau ≈ proton ≈ charm ≈ bottom at ~1 GeV; muon ≈ strange at
~100 MeV) is a structural consequence of dim sharing, not numerical accident.

The test does NOT include shear resonances (σ=0 throughout) — it is a bare
sanity check on the dim-sharing hierarchy. Within-sheet 3-generation
splitting (the R53 shear-resonance regime) is a separate problem (see
work/3-torus.md §5).

Usage:
    python scripts/ma_share_6.py [--max-winding N] [--variant VARIANT_NAME]

Outputs to outputs/:
    ma_share_6_<variant>.csv    — per-fermion match results
    ma_share_6_summary.txt      — variant comparison and verdict
"""

from __future__ import annotations

import argparse
from math import pi, sqrt
from pathlib import Path

import numpy as np


HBARC_MEV_FM = 197.3269804  # ℏc in MeV·fm


# Observed fundamental fermions: (mass_MeV, host sheet under model-F)
OBSERVED = {
    # ν-sheet
    "nu1":  (3.0e-8, "v"),
    "nu2":  (3.3e-8, "v"),
    "nu3":  (6.0e-8, "v"),
    # e-sheet (charged leptons)
    "e":    (0.511,   "e"),
    "mu":   (105.66,  "e"),
    "tau":  (1776.86, "e"),
    # p-sheet (quarks — current-quark masses)
    "u":    (2.16,    "p"),
    "d":    (4.67,    "p"),
    "s":    (93.0,    "p"),
    "c":    (1270.0,  "p"),
    "b":    (4180.0,  "p"),
    "t":    (1.73e5,  "p"),
}


# 6-dim topology: each sheet uses 3 of 6 dims, each pair shares 1
SHEETS = {
    "e": ("U_e", "S_ep", "S_ev"),
    "p": ("U_p", "S_ep", "S_pv"),
    "v": ("U_v", "S_ev", "S_pv"),
}


# Baseline dim values (in fm), chosen to span the observed mass scales.
# Each dim's natural 2π/L mass scale (in MeV) noted in comments.
# Convention: smaller L → larger mass.
BASELINE_VARIANTS = {
    "v1_log_spaced": {
        # Log-spaced from top scale (~0.001 fm) to neutrino scale (~10^9 fm),
        # roughly 2 orders of magnitude between each dim.
        # S_ep is set near 1 fm to match the ~GeV cluster.
        "U_p":  0.005,    # 2π/L = 250 GeV (top)
        "S_pv": 0.1,      # 2π/L = 12.4 GeV
        "S_ep": 1.0,      # 2π/L = 1.24 GeV  ← bridging dim, tau/proton scale
        "U_e":  100.0,    # 2π/L = 12.4 MeV  (light quarks / electron)
        "S_ev": 1.0e4,    # 2π/L = 124 keV
        "U_v":  3.3e9,    # 2π/L = 0.38 μeV  (ν natural scale)
    },
    "v2_tuned_GeV": {
        # Tune S_ep to match tau (1.78 GeV) at the (1, 1) mode on e-sheet.
        # 2π × ℏc / S_ep = tau → S_ep = 2π·197.327/1776 ≈ 0.7 fm
        "U_p":  0.001,    # ~ 1.2 TeV
        "S_pv": 0.07,     # ~ 17.7 GeV
        "S_ep": 0.7,      # ~ 1.77 GeV  ← matches tau
        "U_e":  200.0,    # ~ 6.2 MeV
        "S_ev": 1.0e4,    # ~ 124 keV
        "U_v":  6.7e9,    # ~ 0.18 μeV
    },
    "v3_tuned_proton": {
        # Tune S_ep to match proton (938 MeV).
        # S_ep = 2π·197.327/938 = 1.32 fm
        "U_p":  0.002,    # ~ 620 GeV
        "S_pv": 0.06,     # ~ 20.7 GeV
        "S_ep": 1.32,     # ~ 938 MeV  ← matches proton
        "U_e":  500.0,    # ~ 2.5 MeV
        "S_ev": 5.0e4,    # ~ 25 keV
        "U_v":  4.1e10,   # ~ 0.030 μeV
    },
    "v4_modelF_inspired": {
        # Use model-F's L_ring_e = 54.83 and L_ring_p = 47.29 as the shared S_ep.
        # Other dims chosen so 2π/min(pair) hits observed clusters.
        "U_p":  0.01,     # ~ 124 GeV
        "S_pv": 0.2,      # ~ 6.2 GeV
        "S_ep": 50.0,     # ~ 24.8 MeV  (between L_ring_e and L_ring_p of model-F)
        "U_e":  20000.0,  # ~ 62 keV
        "S_ev": 1.0e5,    # ~ 12.4 keV
        "U_v":  1.0e10,   # ~ 0.12 μeV
    },
}


def mode_mass_2d(L_a: float, L_b: float, n_a: int, n_b: int) -> float:
    """Bare 2D mode mass on (L_a, L_b)-plane with windings (n_a, n_b).

    mass [MeV] = ℏc × 2π × √((n_a/L_a)² + (n_b/L_b)²),  with L in fm.
    """
    if n_a == 0 and n_b == 0:
        return float("inf")
    k_sq = (2 * pi * n_a / L_a) ** 2 + (2 * pi * n_b / L_b) ** 2
    return HBARC_MEV_FM * sqrt(k_sq)


def enumerate_sheet_modes(sheet: str, L_dict: dict, max_n: int):
    """Enumerate all 2D-planar modes on a sheet's three coordinate planes,
    excluding 1D-line modes (where one winding is zero) — per the dim-sharing
    hypothesis from work/3-torus.md, only 2D-planar modes are physical.

    Returns a list of dicts with keys: n_a, n_b, plane, mass.
    """
    dim_names = SHEETS[sheet]
    modes = []
    for i in range(3):
        for j in range(i + 1, 3):
            name_a = dim_names[i]
            name_b = dim_names[j]
            L_a = L_dict[name_a]
            L_b = L_dict[name_b]
            # Order so smaller is L_a ("tube" by MaSt convention)
            if L_a > L_b:
                L_a, L_b = L_b, L_a
                name_a, name_b = name_b, name_a
            for n_a in range(1, max_n + 1):
                for n_b in range(1, max_n + 1):
                    m = mode_mass_2d(L_a, L_b, n_a, n_b)
                    modes.append({
                        "sheet": sheet,
                        "plane": f"{name_a}–{name_b}",
                        "L_a": L_a,
                        "L_b": L_b,
                        "n_a": n_a,
                        "n_b": n_b,
                        "mass": m,
                    })
                    # Include sign-flipped n_a as well (give it the same mass
                    # under bare wave eq; sign matters only when shears or
                    # topological identifications appear).
    return modes


def find_best_match(target_mass: float, modes: list):
    """Closest mode by log-distance in mass. Returns (best_mode, log_err)."""
    best = None
    best_log = float("inf")
    for m in modes:
        if m["mass"] <= 0:
            continue
        log_err = np.log10(m["mass"] / target_mass)
        if abs(log_err) < abs(best_log):
            best_log = log_err
            best = m
    return best, best_log


def run_variant(name: str, L_dict: dict, max_n: int):
    """Run the test for one L-variant; return per-fermion results."""
    results = []
    # Pre-compute modes per sheet
    sheet_modes = {s: enumerate_sheet_modes(s, L_dict, max_n) for s in SHEETS}
    for fname, (target, sheet) in OBSERVED.items():
        modes = sheet_modes[sheet]
        best, log_err = find_best_match(target, modes)
        results.append({
            "fermion": fname,
            "sheet": sheet,
            "target_MeV": target,
            "best_mass_MeV": best["mass"],
            "log_err": log_err,
            "plane": best["plane"],
            "n_a": best["n_a"],
            "n_b": best["n_b"],
            "L_a": best["L_a"],
            "L_b": best["L_b"],
        })
    return results


def write_results_csv(results: list, out_path: Path) -> None:
    with open(out_path, "w") as f:
        f.write("fermion,sheet,target_MeV,best_mass_MeV,log_err,"
                "plane,n_a,n_b,L_a_fm,L_b_fm\n")
        for r in results:
            f.write(f"{r['fermion']},{r['sheet']},"
                    f"{r['target_MeV']:.6g},{r['best_mass_MeV']:.6g},"
                    f"{r['log_err']:+.4f},{r['plane']},"
                    f"{r['n_a']},{r['n_b']},{r['L_a']:.6g},{r['L_b']:.6g}\n")


def fmt_log_err(log_err: float) -> str:
    """Pretty-print log-error with bracket: ✓ <0.5; ~ <1.0; ✗ ≥1.0."""
    if abs(log_err) < 0.5:
        tag = "✓"
    elif abs(log_err) < 1.0:
        tag = "~"
    else:
        tag = "✗"
    return f"{log_err:+.2f} {tag}"


def print_variant(name: str, L_dict: dict, results: list) -> None:
    print(f"\n{'='*80}")
    print(f"Variant: {name}")
    print(f"{'='*80}")
    print("Dim sizes (fm):")
    for k, v in L_dict.items():
        natural_scale = HBARC_MEV_FM * 2 * pi / v
        unit = "MeV"
        if natural_scale > 1e3:
            natural_scale /= 1e3; unit = "GeV"
        if natural_scale < 1e-3:
            natural_scale *= 1e3; unit = "keV"
        if natural_scale < 1e-3:
            natural_scale *= 1e3; unit = "eV"
        print(f"  {k:6s} = {v:>12.4g} fm    (2π/L = {natural_scale:>8.3g} {unit})")
    print()
    print(f"  {'fermion':<6s} {'sheet':<5s} {'target [MeV]':>13s} {'best [MeV]':>13s} "
          f"{'log_err':>14s} {'plane':<14s} {'(n_a,n_b)':<10s}")
    print(f"  {'-'*100}")
    for r in results:
        print(f"  {r['fermion']:<6s} {r['sheet']:<5s} {r['target_MeV']:>13.3g} "
              f"{r['best_mass_MeV']:>13.3g} {fmt_log_err(r['log_err']):>14s} "
              f"{r['plane']:<14s} ({r['n_a']},{r['n_b']})")
    log_errs = [abs(r['log_err']) for r in results]
    print(f"\n  Total |log_err| = {sum(log_errs):.2f}")
    print(f"  Max  |log_err|  = {max(log_errs):.2f}")
    print(f"  Within factor 3 (|log_err| < 0.5): {sum(1 for e in log_errs if e < 0.5)}/{len(log_errs)}")
    print(f"  Within factor 10 (|log_err| < 1.0): {sum(1 for e in log_errs if e < 1.0)}/{len(log_errs)}")


def find_shared_match_evidence(L_dict: dict, max_n: int) -> str:
    """Construct evidence string for the user's specific claim: tau (e-sheet)
    and proton (p-sheet) both prefer modes on the S_ep shared plane.
    """
    lines = []
    # Get the tau best match
    tau_target = OBSERVED["tau"][0]
    e_modes = enumerate_sheet_modes("e", L_dict, max_n)
    tau_best, _ = find_best_match(tau_target, e_modes)
    # Get the proton-mass-region match on p-sheet (proton itself is composite under model-F,
    # so we check whether SOME mode near 1 GeV uses the S_ep dim)
    p_modes = enumerate_sheet_modes("p", L_dict, max_n)
    # Find the lightest p-sheet mode that uses S_ep
    s_ep_modes = [m for m in p_modes if "S_ep" in m["plane"]]
    if s_ep_modes:
        lightest_p_on_Sep = min(s_ep_modes, key=lambda m: m["mass"])
    else:
        lightest_p_on_Sep = None
    lines.append("Per-sheet S_ep usage (the bridging-dim hypothesis):")
    lines.append(f"  tau best match (e-sheet):  plane = {tau_best['plane']:<14s}  "
                 f"mass = {tau_best['mass']:.4g} MeV  (target {tau_target} MeV)")
    if lightest_p_on_Sep is not None:
        lines.append(f"  lightest p-sheet S_ep mode: plane = {lightest_p_on_Sep['plane']:<14s}  "
                     f"mass = {lightest_p_on_Sep['mass']:.4g} MeV  (proton ≈ 938 MeV)")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-winding", type=int, default=5,
                        help="Maximum |winding| in each direction (default 5).")
    parser.add_argument("--variant", type=str, default="all",
                        help="Name of variant to run; 'all' runs all variants. "
                             f"Available: {list(BASELINE_VARIANTS.keys())}")
    parser.add_argument("--outputs-dir", type=Path,
                        default=Path(__file__).resolve().parents[1] / "outputs")
    args = parser.parse_args()

    args.outputs_dir.mkdir(parents=True, exist_ok=True)

    variants = list(BASELINE_VARIANTS.items()) if args.variant == "all" \
        else [(args.variant, BASELINE_VARIANTS[args.variant])]

    summary_lines = []
    summary_lines.append("=" * 80)
    summary_lines.append("ma-share-6 numerical test summary")
    summary_lines.append("=" * 80)
    summary_lines.append("")
    summary_lines.append(f"Topology: 6 dims; sheets share 1 dim per pair")
    summary_lines.append(f"Max winding tested: ±{args.max_winding}")
    summary_lines.append(f"Number of variants: {len(variants)}")
    summary_lines.append("")

    best_variant = None
    best_total = float("inf")
    for name, L_dict in variants:
        results = run_variant(name, L_dict, args.max_winding)
        print_variant(name, L_dict, results)

        csv_path = args.outputs_dir / f"ma_share_6_{name}.csv"
        write_results_csv(results, csv_path)
        print(f"  → wrote {csv_path.name}")

        total = sum(abs(r["log_err"]) for r in results)
        within_3 = sum(1 for r in results if abs(r["log_err"]) < 0.5)
        within_10 = sum(1 for r in results if abs(r["log_err"]) < 1.0)

        summary_lines.append(f"--- Variant: {name} ---")
        for k, v in L_dict.items():
            summary_lines.append(f"  {k:6s} = {v:>12.4g} fm")
        summary_lines.append(f"  Total |log_err| = {total:.2f}  "
                             f"(within ×3: {within_3}/{len(results)}; "
                             f"within ×10: {within_10}/{len(results)})")
        summary_lines.append("")
        evidence = find_shared_match_evidence(L_dict, args.max_winding)
        for line in evidence.split("\n"):
            summary_lines.append("  " + line)
        summary_lines.append("")

        if total < best_total:
            best_total = total
            best_variant = name

    summary_lines.append("=" * 80)
    summary_lines.append(f"Best variant by total |log_err|: {best_variant} "
                         f"(total = {best_total:.2f})")
    summary_lines.append("=" * 80)

    summary_path = args.outputs_dir / "ma_share_6_summary.txt"
    with open(summary_path, "w") as f:
        f.write("\n".join(summary_lines))
    print(f"\n\nWrote: {summary_path.name}")


if __name__ == "__main__":
    main()
