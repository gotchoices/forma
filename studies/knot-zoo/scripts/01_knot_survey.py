#!/usr/bin/env python3
"""
01_knot_survey.py — Enumerate (p,q) torus knots and compute predicted
quantum numbers in the WvM framework.

For each coprime pair (p,q) with p = tube windings, q = major-axis loops:

  - Spin: derived from the angular momentum formula L = R·(h/λ) and
    the number of major-axis loops q.  WvM (p=1,q=2) gives L = ℏ/2.
    General case: L = ℏ·p/(2q)  (to be verified).

  - Charge: generalized WvM derivation using path-dependent photon
    energy and the same confinement volume.

  - Mass ratio: relative to the (1,2) electron, assuming the torus
    geometry (R, a) is fixed and mass scales with path length.

Bears on theory.md P1–P4, findings F1.
"""

import math
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib import constants as C


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def path_length(p, q, R, a):
    """Length of a (p,q) torus knot on a torus with major radius R, tube radius a."""
    return math.sqrt((2 * math.pi * q * R) ** 2 + (2 * math.pi * p * a) ** 2)


def wvm_spin(p, q):
    """
    Spin quantum number for a (p,q) torus knot in the WvM framework.

    WvM electron (1,2): photon path length = λ, angular momentum L = R·(h/λ).
    The photon makes q loops around the major axis, each at radius R.
    Total orbital angular momentum = R × p_photon = R × (h/λ) / c × c = R·h/λ.
    But the path closes after q major loops, so the angular momentum
    measured per revolution of the coordinate φ is L/q.

    Actually: L = R × (hν/c) where hν = hc/λ is the photon energy.
    For WvM (q=2): L = R·h/λ = (λ/4π)·(h/λ) = h/(4π) = ℏ/2.

    For general (p,q): the path winds q times around the axis.
    The effective circumference for the angular momentum is q × 2πR.
    The photon momentum is h/λ where λ = path_length.

    The angular momentum about the symmetry axis is:
      L_z = R × (h/λ) × cos(pitch_angle) × sign

    where the pitch angle is the angle the path makes with the
    equatorial plane: tan(pitch) = pa/(qR).

    For WvM with a << R: pitch ≈ 0, L_z ≈ R·h/λ ≈ R·h/(2π·q·R) = ℏ/q.
    But WvM gets ℏ/2 for q=2, so L_z = ℏ/q... wait that's the same thing.

    Let's verify: for (1,2), L_z = ℏ/2. For (1,3), L_z = ℏ/3.
    For (1,1), L_z = ℏ. For (2,1), L_z = ℏ (with path length adjustment).

    Hmm — this gives non-standard spin values for some knots. Let's
    compute and tabulate, then interpret.

    Returns L_z in units of ℏ (approximate, for a << R limit).
    """
    return 1.0 / q


def is_fermion(p):
    """
    In WvM topology: odd p gives a π-twist (needs 2 traversals to
    restore E-field orientation → fermion). Even p gives 2π-twist
    (restores in 1 traversal → boson).
    """
    return p % 2 == 1


def main():
    R = C.lambda_C / (4 * math.pi)
    a = R / math.sqrt(math.pi * C.alpha)

    print("=" * 78)
    print("Torus Knot Survey — WvM Framework")
    print("=" * 78)
    print()
    print(f"  Torus geometry: R = λ/(4π) = {R:.4e} m")
    print(f"                  a = R/√(πα) = {a:.4e} m")
    print(f"                  a/R = 1/√(πα) = {a/R:.4f}")
    print()

    electron_lambda = C.lambda_C
    electron_mass = C.m_e

    print("─" * 78)
    print(f"  {'(p,q)':>6s}  {'Coprime':>7s}  {'Ferm/Bos':>8s}  "
          f"{'L_z/ℏ':>8s}  {'L(m)':>12s}  {'λ_ratio':>8s}  "
          f"{'m/m_e':>10s}  {'Spin?':>8s}")
    print("─" * 78)

    results = []
    for q in range(1, 8):
        for p in range(1, 8):
            if gcd(p, q) != 1:
                continue

            L = path_length(p, q, R, a)
            lam_ratio = L / electron_lambda
            mass_ratio = lam_ratio  # m ∝ E = hc/λ_path, but λ_path = L
            # Actually: if the SAME photon wavelength λ is used but the
            # path is different, then mass = hc/(c²·λ) is the same.
            # But if the path length IS the wavelength (λ = L), then
            # different knots have different wavelengths and hence masses.

            # In WvM: λ = path_length (the photon fits exactly once).
            # So for (p,q) on the SAME torus, λ_{p,q} = L_{p,q},
            # and mass_{p,q} = h/(L_{p,q} · c).
            # mass_ratio = m_{p,q}/m_e = λ_e / L_{p,q} = 1/lam_ratio.
            # Wait — higher path length means LOWER frequency, LOWER mass.
            mass_ratio_inv = 1.0 / lam_ratio  # m/m_e if same torus

            Lz = wvm_spin(p, q)
            fb = "fermion" if is_fermion(p) else "boson"

            # Interpret spin
            spin_str = f"{Lz:.4f}"
            if abs(Lz - 0.5) < 0.001:
                spin_str = "1/2"
            elif abs(Lz - 1.0) < 0.001:
                spin_str = "1"
            elif abs(Lz - 1.0/3) < 0.001:
                spin_str = "1/3"
            elif abs(Lz - 0.25) < 0.001:
                spin_str = "1/4"
            elif abs(Lz - 1.0/5) < 0.001:
                spin_str = "1/5"
            elif abs(Lz - 1.0/6) < 0.001:
                spin_str = "1/6"
            elif abs(Lz - 1.0/7) < 0.001:
                spin_str = "1/7"

            print(f"  ({p},{q}){' ':>{4-len(str(p))-len(str(q))}s}  "
                  f"{'yes':>7s}  {fb:>8s}  {spin_str:>8s}  "
                  f"{L:>12.4e}  {lam_ratio:>8.4f}  "
                  f"{mass_ratio_inv:>10.4f}  "
                  f"{'←e' if (p,q) == (1,2) else ''}")

            results.append((p, q, fb, Lz, L, lam_ratio, mass_ratio_inv))

    print("─" * 78)
    print()

    print("=" * 78)
    print("Analysis: Spin Values")
    print("=" * 78)
    print()
    print("The WvM spin formula L_z = ℏ/q (in the a << R limit) gives:")
    print()

    spin_groups = {}
    for p, q, fb, Lz, L, lr, mr in results:
        key = f"{Lz:.4f}"
        if key not in spin_groups:
            spin_groups[key] = []
        spin_groups[key].append((p, q, fb))

    for spin_val in sorted(spin_groups.keys(), key=float, reverse=True):
        knots = spin_groups[spin_val]
        frac = float(spin_val)
        label = ""
        for d in range(1, 8):
            n = round(frac * d)
            if abs(n/d - frac) < 0.001 and gcd(n, d) == 1:
                label = f"{n}/{d}" if d > 1 else str(n)
                break
        fb_types = set(k[2] for k in knots)
        knot_strs = [f"({k[0]},{k[1]})" for k in knots]
        print(f"  L_z = {label:>4s} ℏ  ({', '.join(fb_types):>8s}):  "
              f"{', '.join(knot_strs)}")

    print()
    print("NOTE: L_z = ℏ/q is a TENTATIVE formula derived from the a << R")
    print("limit. The actual spin depends on the full path geometry and")
    print("the polarization transport around the knot. Values like 1/3")
    print("or 1/5 are non-physical for elementary particles and suggest")
    print("either the formula needs refinement or these knots are not")
    print("realized in nature.")
    print()

    print("=" * 78)
    print("Analysis: Mass Ratios (same torus, different knots)")
    print("=" * 78)
    print()
    print("If all knots live on the same torus (R, a), the photon wavelength")
    print("equals the path length, so mass ∝ 1/L. Ratios relative to (1,2):")
    print()

    e_L = None
    for p, q, fb, Lz, L, lr, mr in results:
        if (p, q) == (1, 2):
            e_L = L
            break

    print(f"  {'(p,q)':>6s}  {'Path/λ_e':>10s}  {'m/m_e':>10s}  "
          f"{'Type':>8s}  {'Known particle?':>20s}")
    print("  " + "─" * 64)

    known = {
        (1, 2): "electron (by construction)",
        (1, 1): "?",
    }

    for p, q, fb, Lz, L, lr, mr in sorted(results, key=lambda r: -r[6]):
        particle = known.get((p, q), "")
        if mr > 100 and fb == "fermion":
            if abs(mr - 206.8) / 206.8 < 0.5:
                particle = "muon range?"
            elif abs(mr - 3477) / 3477 < 0.5:
                particle = "tau range?"
        print(f"  ({p},{q}){' ':>{4-len(str(p))-len(str(q))}s}  "
              f"{lr:>10.4f}  {mr:>10.4f}  {fb:>8s}  {particle}")

    print()
    print("NOTE: The mass ratios above assume fixed torus geometry. If")
    print("different particles have different torus sizes, the mass ratios")
    print("would be different. The assumption that all particles share one")
    print("torus is strong and may not hold.")
    print()

    print("=" * 78)
    print("Analysis: Fermion/Boson Classification")
    print("=" * 78)
    print()
    print("Odd p (tube windings) → fermion (π-twist, needs 2 traversals)")
    print("Even p → boson (2π-twist, restores in 1 traversal)")
    print()

    fermions = [(p, q) for p, q, fb, *_ in results if fb == "fermion"]
    bosons = [(p, q) for p, q, fb, *_ in results if fb == "boson"]
    print(f"  Fermions (p odd):  {', '.join(f'({p},{q})' for p,q in fermions)}")
    print(f"  Bosons (p even):   {', '.join(f'({p},{q})' for p,q in bosons)}")
    print()


if __name__ == "__main__":
    main()
