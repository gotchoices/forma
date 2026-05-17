"""
3-torus mode spectrum and R19-style EM-coupling integral test.

Implements the two tests of work/3-torus.md:

  Test A — Spectrum classification.  Enumerate the bare Laplacian
    eigenmodes of a 3-torus with circumferences (L1, L2, L3), classify
    each by # of nonzero windings (1D-line, 2D-planar, 3D-mixed), and
    report the layout of the low-energy spectrum.

  Test B — Per-cycle EM-coupling integrals.  For each plane-wave mode
    ψ_n = exp(i 2π (n1 u1/L1 + n2 u2/L2 + n3 u3/L3)), compute three
    candidate R19-extensions analytically:

      Candidate I  (per-direction 1-cycle):
          Q_i = (1/L_i) ∮ ∂_i ψ du_i
        Evaluates exactly to (2π i n_i / L_i^2) * <ψ>, where <ψ> = 1 for
        the zero-winding directions only; for plane waves on a closed
        torus the relevant per-cycle-line integral picks up n_i directly.
        SIMPLIFIED EVALUATION: |Q_i|^2 ∝ n_i^2.

      Candidate II  (per-plane 2-cycle flux of orthogonal derivative):
          Φ_{ij} = ∫∫ ∂_k ψ du_i du_j  (k ∉ {i,j})
        Nonzero only when n_i = n_j = 0 and n_k ≠ 0 — selects 1D-line
        modes along the perpendicular direction.  SIMPLIFIED:
        |Φ_{ij}|^2 ∝ n_k^2 * δ_{n_i,0} * δ_{n_j,0}.

      Candidate III  (per-plane circulation / curl-like):
          C_{ij} = ∮ ∂(L_i × L_j cell) [(∂_i ψ) du_j − (∂_j ψ) du_i]
        Evaluates by Stokes to ∫∫ (∂_i ∂_j ψ − ∂_j ∂_i ψ) dA times the
        plane wave's phase; for plane waves the integrand reduces to a
        bilinear  ∝ n_i n_j.  SIMPLIFIED: |C_{ij}|^2 ∝ (n_i n_j)^2.

    Candidates I, II, III have qualitatively distinct properties; only
    III implements the "winding-in-at-least-two-dims" selection rule.

Outputs to outputs/:
    torus3d_spectrum_L{L1}_{L2}_{L3}.csv  — sorted mode list with
        class and coupling-magnitude columns
    torus3d_coupling_report.txt           — analytical formulas + the
        per-class result on representative modes
    torus3d_summary.csv                   — across-ratios summary

Usage:
    python scripts/torus3d_modes.py [--L1 1] [--L2 580] [--L3 78000]
                                     [--n-max 4] [--n-report 30]
                                     [--ratios "label:l1:l2:l3,..."]
"""

from __future__ import annotations

import argparse
import itertools
from pathlib import Path
from typing import Iterable

import numpy as np


def classify_mode(n: tuple) -> str:
    """Class by # nonzero entries in (n1, n2, n3)."""
    k = sum(1 for ni in n if ni != 0)
    if k == 0:
        return "zero"
    if k == 1:
        return "1D-line"
    if k == 2:
        return "2D-planar"
    return "3D-mixed"


def plane_label(n: tuple) -> str:
    """For 2D-planar modes, return which plane (12, 13, 23)."""
    cls = classify_mode(n)
    if cls != "2D-planar":
        return ""
    nonzero = tuple(i + 1 for i, ni in enumerate(n) if ni != 0)
    return f"({nonzero[0]}{nonzero[1]})"


def coupling_I(n: tuple, L: tuple) -> tuple:
    """Candidate I — per-direction 1-cycle integrals.

    |Q_i|^2 ∝ n_i^2 / L_i^2 (each direction's winding gives a
    non-trivial line integral around that cycle).  Returns
    (|Q_1|^2, |Q_2|^2, |Q_3|^2) in units where the (2π)^2 factor is
    absorbed.
    """
    return tuple((n[i] / L[i]) ** 2 for i in range(3))


def coupling_II(n: tuple, L: tuple) -> tuple:
    """Candidate II — per-plane 2-cycle flux of orthogonal derivative.

    For each plane (i, j), the flux through the L_i × L_j cell of the
    perpendicular derivative ∂_k ψ vanishes unless n_i = n_j = 0.  In
    that case the integral gives 2π i n_k / L_k times L_i L_j, so
    |Φ_{ij}|^2 ∝ (n_k / L_k)^2 * (L_i L_j)^2 when n_i = n_j = 0,
    else 0.

    Returns ordered as (Φ_12², Φ_13², Φ_23²).
    """
    pairs = ((0, 1, 2), (0, 2, 1), (1, 2, 0))  # (i, j, k)
    out = []
    for (i, j, k) in pairs:
        if n[i] == 0 and n[j] == 0 and n[k] != 0:
            val = (n[k] / L[k]) ** 2 * (L[i] * L[j]) ** 2
        else:
            val = 0.0
        out.append(val)
    return tuple(out)


def coupling_III(n: tuple, L: tuple) -> tuple:
    """Candidate III — per-plane circulation/curl-like (bilinear).

    For plane waves the boundary integral along (∂_i ψ) du_j contributes
    a phase-orbit term proportional to (n_i / L_i) * (n_j / L_j); summing
    the two cycle pieces with the curl sign gives net amplitude
    ∝ n_i * n_j.  Nonzero iff both n_i and n_j are nonzero.

    Returns ordered as (|C_12|², |C_13|², |C_23|²).
    """
    pairs = ((0, 1), (0, 2), (1, 2))
    return tuple(((n[i] / L[i]) * (n[j] / L[j])) ** 2 for (i, j) in pairs)


def enumerate_modes(n_max: int) -> Iterable[tuple]:
    """All (n1, n2, n3) with |n_i| ≤ n_max, excluding (0, 0, 0)."""
    for n1 in range(-n_max, n_max + 1):
        for n2 in range(-n_max, n_max + 1):
            for n3 in range(-n_max, n_max + 1):
                if (n1, n2, n3) == (0, 0, 0):
                    continue
                yield (n1, n2, n3)


def omega2(n: tuple, L: tuple) -> float:
    """Bare 3-torus Laplacian eigenvalue ω² = (2π)² Σ (n_i / L_i)²."""
    return (2 * np.pi) ** 2 * sum((n[i] / L[i]) ** 2 for i in range(3))


def build_spectrum(L: tuple, n_max: int):
    """Return a list of (omega2, n, class, plane, couplings_I,II,III)
    sorted by omega2 ascending.
    """
    rows = []
    for n in enumerate_modes(n_max):
        w2 = omega2(n, L)
        cls = classify_mode(n)
        rows.append({
            "omega2": w2,
            "omega": float(np.sqrt(w2)),
            "n": n,
            "class": cls,
            "plane": plane_label(n),
            "Q_I_sq": coupling_I(n, L),       # (Q1², Q2², Q3²)
            "Phi_II_sq": coupling_II(n, L),   # (Φ12², Φ13², Φ23²)
            "C_III_sq": coupling_III(n, L),   # (C12², C13², C23²)
        })
    rows.sort(key=lambda r: r["omega2"])
    return rows


def write_spectrum_csv(rows, out_path: Path, n_report: int) -> None:
    with open(out_path, "w") as f:
        f.write("rank,omega,omega2,class,plane,n1,n2,n3,"
                "Q1sq,Q2sq,Q3sq,Phi12sq,Phi13sq,Phi23sq,"
                "C12sq,C13sq,C23sq,Q_I_total,Phi_II_total,C_III_total\n")
        for rank, r in enumerate(rows[:n_report]):
            n1, n2, n3 = r["n"]
            q1, q2, q3 = r["Q_I_sq"]
            p12, p13, p23 = r["Phi_II_sq"]
            c12, c13, c23 = r["C_III_sq"]
            qt = q1 + q2 + q3
            pt = p12 + p13 + p23
            ct = c12 + c13 + c23
            f.write(f"{rank},{r['omega']:.6g},{r['omega2']:.6g},{r['class']},"
                    f"{r['plane']},{n1},{n2},{n3},"
                    f"{q1:.4g},{q2:.4g},{q3:.4g},"
                    f"{p12:.4g},{p13:.4g},{p23:.4g},"
                    f"{c12:.4g},{c13:.4g},{c23:.4g},"
                    f"{qt:.4g},{pt:.4g},{ct:.4g}\n")


def class_count_in_lowest_N(rows, n_report: int) -> dict:
    """Count modes by class in the lowest n_report modes."""
    counts = {"1D-line": 0, "2D-planar": 0, "3D-mixed": 0}
    for r in rows[:n_report]:
        counts[r["class"]] = counts.get(r["class"], 0) + 1
    return counts


def first_of_class(rows, cls: str):
    """Find the lowest-energy mode of a given class.  Returns None if
    not found in `rows`."""
    for r in rows:
        if r["class"] == cls:
            return r
    return None


def write_coupling_report(L_ratios: list, n_max: int, out_path: Path) -> None:
    """Write the coupling-candidate verdict, evaluated on representative
    modes across the requested L-ratios."""
    lines = []
    lines.append("=" * 78)
    lines.append("R19-extension test: EM-coupling integral candidates on the 3-torus")
    lines.append("=" * 78)
    lines.append("")
    lines.append("Three candidate per-mode 'charge magnitudes' on (n1,n2,n3) plane waves:")
    lines.append("")
    lines.append("  Cand I  — per-direction 1-cycle integrals:")
    lines.append("           |Q_i|^2 ∝ (n_i/L_i)^2  — picks up each direction's winding")
    lines.append("           1D-line modes have ONE nonzero Q_i, others zero")
    lines.append("           => 1D modes are NOT dark under this rule")
    lines.append("")
    lines.append("  Cand II — per-plane 2-cycle flux of perpendicular derivative:")
    lines.append("           |Φ_{ij}|^2 ∝ (n_k/L_k)^2 * (L_i L_j)^2 * δ(n_i=0) * δ(n_j=0)")
    lines.append("           Nonzero ONLY for 1D-line modes (along the perp direction)")
    lines.append("           => 2D and 3D modes are dark; only 1D 'shines' — opposite of what we want")
    lines.append("")
    lines.append("  Cand III— per-plane circulation/curl-like (bilinear in n_i, n_j):")
    lines.append("           |C_{ij}|^2 ∝ (n_i n_j / (L_i L_j))^2")
    lines.append("           Nonzero IFF both n_i AND n_j are nonzero")
    lines.append("           => 1D modes are dark; 2D-planar and 3D-mixed are charged")
    lines.append("           => THIS implements the hypothesis's selection rule")
    lines.append("")
    lines.append("-" * 78)
    lines.append("Per-mode evaluations (totals summed over all i,j,k):")
    lines.append("-" * 78)
    lines.append("")

    # Representative modes — one per class — at each L-ratio
    rep_modes = [
        ("1D along L3", (0, 0, 1)),
        ("1D along L2", (0, 1, 0)),
        ("1D along L1", (1, 0, 0)),
        ("2D in (23)-plane", (0, 1, 1)),
        ("2D in (13)-plane", (1, 0, 1)),
        ("2D in (12)-plane", (1, 1, 0)),
        ("3D fully-mixed", (1, 1, 1)),
    ]

    for label, L in L_ratios:
        lines.append(f"** L1, L2, L3 = {L[0]:g}, {L[1]:g}, {L[2]:g}  ({label}) **")
        lines.append("")
        lines.append(f"  {'Mode':<24} {'class':<11} {'ω':>13} "
                     f"{'ΣQ_I':>12} {'ΣΦ_II':>12} {'ΣC_III':>12}")
        for tag, n in rep_modes:
            w = float(np.sqrt(omega2(n, L)))
            cls = classify_mode(n)
            qt = sum(coupling_I(n, L))
            pt = sum(coupling_II(n, L))
            ct = sum(coupling_III(n, L))
            lines.append(f"  {tag + ' ' + str(n):<24} {cls:<11} "
                         f"{w:>13.4g} {qt:>12.4g} {pt:>12.4g} {ct:>12.4g}")
        lines.append("")

    lines.append("-" * 78)
    lines.append("Selection rule verdict (read down each column):")
    lines.append("")
    lines.append("  Cand I  (per-direction 1-cycle):")
    lines.append("    1D modes carry charge.  Picture is killed: predicted ghost flood.")
    lines.append("")
    lines.append("  Cand II (per-plane perpendicular flux):")
    lines.append("    Only 1D modes carry charge; 2D and 3D are dark.")
    lines.append("    Inverted picture; if this is the physical rule, the 2D-planar")
    lines.append("    'three generations' would all be dark — equally bad.")
    lines.append("")
    lines.append("  Cand III (per-plane curl/circulation, bilinear in n_i n_j):")
    lines.append("    1D-line modes have ΣC_III = 0.  2D and 3D modes are nonzero.")
    lines.append("    This is the rule the hypothesis needs.  If this is the correct")
    lines.append("    extension of R19 to 3D, then 1D modes ARE dark (no EM coupling")
    lines.append("    to S) and the 2D-planar 'three generations' picture works.")
    lines.append("")
    lines.append("WHICH candidate is the physical one is NOT decided here.  It requires")
    lines.append("re-running R19's 2D derivation on the 3-torus, identifying which")
    lines.append("topological integral measures asymptotic monopole charge.  This is")
    lines.append("a finite analytical extension of R19, not implemented here.")
    lines.append("")
    lines.append("=" * 78)

    with open(out_path, "w") as f:
        f.write("\n".join(lines))


def write_summary_csv(L_ratios: list, n_max: int, n_report: int,
                       out_path: Path) -> None:
    """Across-ratios summary: for each (L1, L2, L3) ratio, build the
    spectrum and report counts of each class in the lowest n_report
    modes plus the lowest-of-each-class energies and their ratios.
    """
    with open(out_path, "w") as f:
        f.write("label,L1,L2,L3,n_lowest,n_max,"
                "count_1D,count_2D,count_3D,"
                "omega_1D_low,omega_2D_low,omega_3D_low,"
                "ratio_2D_to_1D,ratio_3D_to_1D\n")
        for label, L in L_ratios:
            rows = build_spectrum(L, n_max)
            counts = class_count_in_lowest_N(rows, n_report)
            r1 = first_of_class(rows, "1D-line")
            r2 = first_of_class(rows, "2D-planar")
            r3 = first_of_class(rows, "3D-mixed")
            w1 = r1["omega"] if r1 else float("nan")
            w2 = r2["omega"] if r2 else float("nan")
            w3 = r3["omega"] if r3 else float("nan")
            f.write(f"{label},{L[0]:g},{L[1]:g},{L[2]:g},"
                    f"{n_report},{n_max},"
                    f"{counts.get('1D-line', 0)},"
                    f"{counts.get('2D-planar', 0)},"
                    f"{counts.get('3D-mixed', 0)},"
                    f"{w1:.6g},{w2:.6g},{w3:.6g},"
                    f"{(w2/w1 if (w1 and not np.isnan(w1) and not np.isnan(w2)) else float('nan')):.6g},"
                    f"{(w3/w1 if (w1 and not np.isnan(w1) and not np.isnan(w3)) else float('nan')):.6g}\n")


def parse_ratios(spec: str) -> list:
    """Parse 'label1:l1a:l1b:l1c,label2:l2a:l2b:l2c,...'."""
    out = []
    for chunk in spec.split(","):
        chunk = chunk.strip()
        if not chunk:
            continue
        parts = chunk.split(":")
        if len(parts) != 4:
            raise ValueError(f"--ratios entry malformed: {chunk!r}")
        label = parts[0]
        L = tuple(float(x) for x in parts[1:])
        out.append((label, L))
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--L1", type=float, default=1.0)
    parser.add_argument("--L2", type=float, default=580.0)
    parser.add_argument("--L3", type=float, default=78000.0)
    parser.add_argument("--n-max", type=int, default=4,
                        help="Mode enumeration: |n_i| ≤ n-max in each direction. "
                        "Default 4 (so 9^3 - 1 = 728 modes).")
    parser.add_argument("--n-report", type=int, default=30,
                        help="Report the lowest n-report modes by energy.")
    parser.add_argument(
        "--ratios",
        type=str,
        default=(
            "natural-quark:1:580:78000,"
            "uniform:1:1:1,"
            "mild:1:10:100,"
            "moderate:1:20:400,"
            "gen-2-only:1:580:5800"
        ),
        help="Comma-separated 'label:l1:l2:l3' triples; the across-ratios "
        "summary is computed at each and saved to outputs/torus3d_summary.csv.",
    )
    parser.add_argument("--outputs-dir", type=Path,
                        default=Path(__file__).resolve().parents[1] / "outputs")
    args = parser.parse_args()

    L = (args.L1, args.L2, args.L3)
    args.outputs_dir.mkdir(parents=True, exist_ok=True)

    print(f"3-torus mode test")
    print(f"  default L = ({L[0]:g}, {L[1]:g}, {L[2]:g}), n_max = {args.n_max}")
    print(f"  enumerating {(2*args.n_max+1)**3 - 1} modes")
    print()

    # Test A: spectrum at the default L
    rows = build_spectrum(L, args.n_max)
    spec_path = (args.outputs_dir /
                 f"torus3d_spectrum_L{L[0]:g}_{L[1]:g}_{L[2]:g}.csv")
    write_spectrum_csv(rows, spec_path, args.n_report)
    print(f"  wrote: {spec_path.name}  (top {args.n_report} modes)")

    counts = class_count_in_lowest_N(rows, args.n_report)
    r1 = first_of_class(rows, "1D-line")
    r2 = first_of_class(rows, "2D-planar")
    r3 = first_of_class(rows, "3D-mixed")
    print()
    print("  Test A — lowest-{n_report} class counts and class-leaders:".format(
        n_report=args.n_report))
    def _fmt_class_line(label: str, count: int, r) -> str:
        if r is None:
            return f"    {label}:{count:>4}  (none in n_max range)"
        return (f"    {label}:{count:>4}  lowest = "
                f"{str(r['n']):<14}  at ω = {r['omega']:.4g}")

    print(_fmt_class_line("1D-line  ", counts.get("1D-line", 0), r1))
    print(_fmt_class_line("2D-planar", counts.get("2D-planar", 0), r2))
    print(_fmt_class_line("3D-mixed ", counts.get("3D-mixed", 0), r3))
    if r1 and r2:
        print(f"    → ratio (lowest 2D) / (lowest 1D) = {r2['omega']/r1['omega']:.4g}")
    if r1 and r3:
        print(f"    → ratio (lowest 3D) / (lowest 1D) = {r3['omega']/r1['omega']:.4g}")
    print()

    # Test B: coupling-integral verdict across ratios
    ratios = parse_ratios(args.ratios)
    report_path = args.outputs_dir / "torus3d_coupling_report.txt"
    write_coupling_report(ratios, args.n_max, report_path)
    print(f"  wrote: {report_path.name}  (Test B verdict)")

    # Across-ratios summary
    summary_path = args.outputs_dir / "torus3d_summary.csv"
    write_summary_csv(ratios, args.n_max, args.n_report, summary_path)
    print(f"  wrote: {summary_path.name}  (across-ratios class counts)")


if __name__ == "__main__":
    main()
