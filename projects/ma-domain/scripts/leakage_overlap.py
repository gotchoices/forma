#!/usr/bin/env python3
"""
leakage_overlap.py - family-wide lepton-universality scan of QY-ED candidates.

Applies the geometric leakage-overlap result of leakage-rate.md (sec.3-4) to
every member of the QY-ED candidate family at once.

For a charged-lepton decay l -> l', the two lepton sheets share one dimension;
the leakage overlap is (leakage-rate.md sec.4.2)

    O ~ 1 / sqrt(L_a * L_b)        a, b = the two NON-shared dimensions

(the shared dimension's length cancels in the junction integral). Lepton
universality requires the three leptonic-decay overlaps - mu->e, tau->e,
tau->mu - to be EQUAL: only then do the leptonic widths follow the pure
Sargent m^5 law. This script computes the three overlaps for each candidate
from its lepton-sheet topology and fitted dimension sizes, and reports their
spread; a spread far from 1 means lepton universality is violated.

STRUCTURAL POINT. The electron delta puts the three leptons on the three edges
of a triangle whose nodes are three dimensions. The three overlaps are then
1/sqrt of the three node-omitted pairwise products, which are equal ONLY if all
three node dimensions are equal - impossible, since the lepton mass hierarchy
needs them unequal. The scan confirms this numerically across the family.

INPUTS  : the CANDIDATES table below - each member's lepton-sheet topology and
          representative dimension sizes (cand-QY-ED.md; a size is the geometric
          mean of the solver's sampled range). The structural verdict does not
          depend on the representative choice; the numbers are illustrative.
OUTPUTS : per-candidate overlap table + universality verdict, printed and
          written to outputs/leakage_overlap.txt.
"""

import argparse
import math
import os

# Candidate specs: lepton -> sheet (dimension pair); dimension -> representative
# size in fm (geometric mean of the solver's sampled range, cand-QY-ED.md).
CANDIDATES = {
    "QY-ED-share1": {
        "leptons": {"e": ("m2", "m6"), "mu": ("m2", "m4"), "tau": ("m4", "m6")},
        "dims": {"m2": 8.20e6, "m4": 0.977, "m6": 2.97e5},
        "note": "electron delta on 1 quark spoke (m4) + 2 fresh dims (m2, m6)",
    },
    "QY-ED-share2": {
        "leptons": {"e": ("m2", "m3"), "tau": ("m2", "m4"), "mu": ("m3", "m4")},
        "dims": {"m2": 1.03e7, "m3": 578.0, "m4": 0.0073},
        "note": "electron delta on 2 quark spokes (m3, m4) + 1 fresh dim (m2); "
                "m3 at its floor (range unbounded above)",
    },
    "QY-ED-share3 (K4)": {
        "leptons": {"e": ("m1", "m2"), "mu": ("m1", "m3"), "tau": ("m2", "m3")},
        "dims": {"m1": 2.25e9, "m2": 0.977, "m3": 0.0073},
        "note": "electron delta on the 3 quark spokes (Solution A)",
    },
}

# the three observed charged-lepton leptonic decays (heavier -> lighter)
DECAYS = [("mu", "e"), ("tau", "e"), ("tau", "mu")]


def overlap(cand, heavy, light):
    """Geometric leakage overlap O ~ 1/sqrt(L_a L_b) for decay heavy -> light."""
    sa, sb = set(cand["leptons"][heavy]), set(cand["leptons"][light])
    shared = sa & sb
    if len(shared) != 1:
        raise ValueError("decay %s->%s: sheets share %d dims (expected 1)"
                          % (heavy, light, len(shared)))
    non_shared = sorted((sa | sb) - shared)
    La, Lb = (cand["dims"][d] for d in non_shared)
    return 1.0 / math.sqrt(La * Lb), sorted(shared)[0], non_shared


def scan(name, cand):
    """Return (report lines, overlap spread) for one candidate."""
    lines = [name + "  -  " + cand["note"], "  " + "-" * 68]
    results = {}
    for heavy, light in DECAYS:
        O, shared, ns = overlap(cand, heavy, light)
        results[(heavy, light)] = O
        lines.append("  %-9s  shared = %-3s  non-shared = (%s, %s)   O ~ %.3e"
                     % ("%s->%s" % (heavy, light), shared, ns[0], ns[1], O))
    base = results[("mu", "e")]
    spread = max(results.values()) / min(results.values())
    lines.append("")
    lines.append("  universality ratios O/O[mu->e]  (all must be ~ 1):")
    for (h, l), O in results.items():
        lines.append("    O[%s->%s] / O[mu->e]  =  %.3e" % (h, l, O / base))
    lines.append("")
    lines.append("  overlap spread (max/min) = %.2e" % spread)
    lines.append("  -> universality %s"
                 % ("SATISFIED" if spread < 3.0
                    else "VIOLATED by ~%.0e (the three overlaps must be equal)"
                         % spread))
    return lines, spread


def main():
    p = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--candidates", nargs="+", default=sorted(CANDIDATES),
                   help="which candidates to scan (default: all)")
    default_out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               "..", "outputs", "leakage_overlap.txt")
    p.add_argument("--outfile", default=default_out)
    args = p.parse_args()

    out = ["=" * 72,
           "leakage_overlap.py  -  lepton-universality scan, QY-ED family",
           "=" * 72, "",
           "O ~ 1/sqrt(L_a L_b),  a,b = the non-shared dims (leakage-rate.md 4.2).",
           "Universality requires the three leptonic-decay overlaps to be equal.",
           ""]
    verdicts = {}
    for name in args.candidates:
        lines, spread = scan(name, CANDIDATES[name])
        out += lines + [""]
        verdicts[name] = spread
    out += ["=" * 72, "SUMMARY"]
    for name, spread in verdicts.items():
        out.append("  %-22s  overlap spread %.2e   %s"
                    % (name, spread,
                       "universality OK" if spread < 3.0
                       else "universality VIOLATED"))
    out += ["",
            "Every QY-ED member uses the electron-delta topology: three leptons",
            "on the three edges of a triangle. The three decay overlaps are equal",
            "only if the three triangle-node dimensions are equal - which the",
            "lepton mass hierarchy forbids. The violation is structural to the",
            "electron delta, not specific to one member.",
            "=" * 72]

    report = "\n".join(out)
    print(report)
    outpath = os.path.abspath(args.outfile)
    os.makedirs(os.path.dirname(outpath), exist_ok=True)
    with open(outpath, "w") as fh:
        fh.write(report + "\n")
    print("\nwritten: %s" % outpath)


if __name__ == "__main__":
    main()
