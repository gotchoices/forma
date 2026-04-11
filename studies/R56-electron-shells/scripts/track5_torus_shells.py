"""
R56 Track 5: Torus standing waves and orientation packing

Part A: Derive shell radii from the standing-wave condition of
        a Compton-scale torus orbiting a nucleus.

Part B: Count how many distinct non-overlapping torus orientations
        fit at each shell radius → angular capacity.

Part C: Combine: total = 2 (tube winding) × orientations per shell.
        Compare to 2, 8, 18, 32.
"""

import numpy as np
import math

ALPHA = 1.0 / 137.036
HC = 197.3269804  # MeV·fm (= ℏc)
A0 = 52917.7  # Bohr radius in fm
M_E = 0.511  # MeV

# Electron torus dimensions (model-E)
L_TUBE = 4717.0  # fm (tube circumference)
L_RING = 11.9    # fm (ring circumference)
R_TUBE = L_TUBE / (2 * math.pi)  # 751 fm (tube radius = effective size)
R_RING = L_RING / (2 * math.pi)  # 1.9 fm (ring radius)
LAMBDA_C = 2 * math.pi * HC / M_E  # Compton wavelength = 2426 fm
LAMBDA_BAR = HC / M_E  # reduced Compton = 386 fm


def main():
    print("=" * 70)
    print("R56 Track 5: Torus standing waves and orientation packing")
    print("=" * 70)
    print()

    # ════════════════════════════════════════════════════════════
    # PART A: Shell radii from standing-wave condition
    # ════════════════════════════════════════════════════════════

    print("PART A: Shell radii from torus standing-wave condition")
    print("=" * 70)
    print()

    print("Physical picture: the electron torus orbits the nucleus.")
    print("Its center traces a circle of circumference 2πr around")
    print("the nucleus.  For a stable orbit, this circumference must")
    print("accommodate an integer number of de Broglie wavelengths:")
    print()
    print("  2π r = n λ_dB")
    print()
    print("This is the Bohr quantization condition.  But in MaSt,")
    print("the electron is not a point with an abstract wavelength —")
    print("it is a PHYSICAL TORUS of circumference L_tube ≈ λ_Compton.")
    print("The de Broglie wavelength at orbit radius r in a Coulomb")
    print("potential is:")
    print()
    print("  λ_dB = 2πℏ / p = 2πℏ / (m_e v)")
    print()
    print("where v is the orbital velocity.  For a Coulomb orbit:")
    print("  v/c = Z α / n  (from Bohr model)")
    print("  λ_dB = 2πℏc / (m_e c × Zα/n) = n × λ_C / (Zα)")
    print()
    print("The standing-wave condition 2πr = nλ_dB gives:")
    print("  r = n² × ℏ/(m_e c × Zα) = n² × a₀/Z")
    print()
    print("This IS the Bohr radius formula.  It follows from requiring")
    print("integer wavelengths around the orbit — the same physics,")
    print("just expressed as a physical torus fitting around the nucleus.")
    print()

    Z = 1  # hydrogen
    print(f"  Hydrogen (Z={Z}) shell radii:")
    print(f"  {'n':>4s}  {'r (pm)':>10s}  {'r/a₀':>8s}  {'2πr (fm)':>12s}  "
          f"{'nλ_dB (fm)':>12s}  {'tori fit':>10s}")
    print(f"  {'─'*4}  {'─'*10}  {'─'*8}  {'─'*12}  {'─'*12}  {'─'*10}")

    for n in range(1, 6):
        r = n**2 * A0 / Z  # Bohr radius for shell n
        circumference = 2 * math.pi * r
        lambda_dB = n * LAMBDA_C / (Z * ALPHA)
        n_lambda = circumference / lambda_dB  # should be n
        # How many torus tube-circumferences fit around the orbit?
        tori_fit = circumference / L_TUBE

        print(f"  {n:>4d}  {r/100:>10.2f}  {r/A0:>8.1f}  "
              f"{circumference:>12.0f}  {n*lambda_dB:>12.0f}  "
              f"{tori_fit:>10.1f}")

    print()
    print("  The 'tori fit' column: how many electron torus diameters")
    print("  fit around each orbit.  At n=1: ~70 tori around the orbit.")
    print("  The electron is much smaller than its orbit — it's a small")
    print("  torus on a large circle, not a torus filling the orbit.")
    print()

    # ════════════════════════════════════════════════════════════
    # PART B: Torus orientations at each shell
    # ════════════════════════════════════════════════════════════

    print("PART B: Torus orientation counting")
    print("=" * 70)
    print()

    print("A torus at radius r around a nucleus has an axis of symmetry.")
    print("This axis can point in different directions:")
    print("  - Radial (pointing at nucleus)")
    print("  - Tangential (along orbit)")
    print("  - Any angle in between")
    print()
    print("The question: how many DISTINCT, non-overlapping orientations")
    print("fit at each radius?")
    print()

    print("Approach 1: Angular momentum quantization as orientation count")
    print()
    print("In QM, at principal quantum number n:")
    print("  l = 0, 1, ..., n-1  (angular momentum quantum number)")
    print("  m = -l, ..., +l     (magnetic quantum number)")
    print("  Total states per n: Σ(2l+1) for l=0..n-1 = n²")
    print()
    print("MaSt interpretation: each (l, m) is a distinct ORIENTATION")
    print("of the electron torus at radius r_n:")
    print("  l = tilt angle of torus axis from the radial direction")
    print("  m = azimuthal orientation of the tilted torus")
    print()
    print("  l=0 (s): axis radial — torus face-on to nucleus (1 orientation)")
    print("  l=1 (p): axis ~45° — 3 orientations (x, y, z tilts)")
    print("  l=2 (d): axis ~60° — 5 orientations")
    print("  l=3 (f): axis ~70° — 7 orientations")
    print()

    print("Can we derive n² from torus packing geometry?")
    print()

    # At each shell radius, what solid angle does one torus subtend?
    print("Approach 2: Solid angle subtended by one torus")
    print()
    for n in range(1, 6):
        r = n**2 * A0  # shell radius (hydrogen)

        # The torus has effective diameter 2 × R_TUBE ≈ 1500 fm
        # At distance r from nucleus, it subtends solid angle:
        # Ω ≈ π R_TUBE² / r²  (small-angle approx)
        omega_torus = math.pi * R_TUBE**2 / r**2

        # Total solid angle of sphere: 4π
        # Maximum non-overlapping tori: 4π / Ω
        max_tori = 4 * math.pi / omega_torus

        # The actual QM count is n²
        qm_count = n**2

        print(f"  n={n}: r = {r/100:.0f} pm, "
              f"Ω_torus = {omega_torus:.2e} sr, "
              f"max packing = {max_tori:.0f}, "
              f"QM count = {qm_count}, "
              f"ratio = {max_tori/qm_count:.0f}")

    print()
    print("  The solid-angle packing gives MANY more tori than n².")
    print("  This means orientational packing is NOT the limiting factor")
    print("  — the torus is too small compared to the orbit to constrain")
    print("  how many orientations fit.")
    print()

    # ════════════════════════════════════════════════════════════
    # PART C: Standing-wave angular modes
    # ════════════════════════════════════════════════════════════

    print("PART C: Angular modes from standing waves on a sphere")
    print("=" * 70)
    print()

    print("The solid-angle packing (Part B) fails because the torus is")
    print("much smaller than the orbit.  But there's another approach:")
    print()
    print("The electron torus at radius r is a WAVE, not a solid object.")
    print("Its angular distribution around the nucleus is a standing wave")
    print("on a sphere of radius r.  The number of independent angular")
    print("standing waves on a sphere is:")
    print()
    print("  Spherical harmonics Y_l^m: for each l, there are (2l+1) modes")
    print("  At shell n, l ranges from 0 to n-1")
    print("  Total angular modes: Σ(2l+1) = n²")
    print()
    print("This is the standard QM result.  The MaSt question is:")
    print("WHY does l range from 0 to n-1?")
    print()
    print("The Bohr orbit at shell n has n de Broglie wavelengths")
    print("around the circumference.  A standing wave with angular")
    print("momentum l has l nodal lines on the sphere.  The constraint")
    print("l < n means: the number of angular nodes cannot exceed the")
    print("number of radial wavelengths.")
    print()
    print("MaSt interpretation: the electron torus wrapping n times")
    print("around the nucleus (n radial wavelengths) can simultaneously")
    print("oscillate with up to n-1 angular nodes.  More angular nodes")
    print("than radial wavelengths would create a standing wave that")
    print("doesn't close on itself — the angular pattern wouldn't match")
    print("up after one orbit.")
    print()
    print("This is the same closure condition that quantizes modes on")
    print("the Ma torus: the winding numbers must be integers for the")
    print("wave to return to its starting point.  On Ma, this gives")
    print("the particle spectrum.  In S (around the nucleus), it gives")
    print("the shell structure.")
    print()

    # ════════════════════════════════════════════════════════════
    # SUMMARY
    # ════════════════════════════════════════════════════════════

    print("=" * 70)
    print("SUMMARY: Shell structure from MaSt perspective")
    print("=" * 70)
    print()
    print("  Shell capacity = 2 × n²")
    print()
    print("  The '2': two tube winding orientations (±1) on the Ma")
    print("  torus.  DERIVED from topology (MaSt contribution).")
    print()
    print("  The 'n²': number of angular standing-wave patterns on a")
    print("  sphere at the Bohr radius.  This follows from:")
    print("    - n radial wavelengths around the orbit (Bohr condition)")
    print("    - l < n angular nodes (closure condition)")
    print("    - (2l+1) azimuthal modes per l")
    print("    - Sum = n²")
    print()
    print("  The Bohr condition (n wavelengths around the orbit) is the")
    print("  SAME physics as Ma mode quantization (n windings close on")
    print("  the torus).  The closure condition (l < n) is the SAME")
    print("  constraint: the pattern must return to its starting point.")
    print()

    print("  SHELL TABLE:")
    print(f"  {'n':>4s}  {'r/a₀':>6s}  {'l values':>12s}  "
          f"{'n²':>4s}  {'×2':>4s}  {'total':>6s}  {'element':>8s}")
    print(f"  {'─'*4}  {'─'*6}  {'─'*12}  {'─'*4}  {'─'*4}  {'─'*6}  {'─'*8}")

    elements = {2: 'He', 10: 'Ne', 28: 'Ni', 60: 'Nd'}
    noble = {2: 'He', 10: 'Ne', 18: 'Ar', 36: 'Kr'}

    cumulative = 0
    for n in range(1, 5):
        l_vals = ', '.join(str(l) for l in range(n))
        cap = n**2
        total = 2 * cap
        cumulative += total
        elem = noble.get(cumulative, '')
        print(f"  {n:>4d}  {n**2:>6d}  {l_vals:>12s}  "
              f"{cap:>4d}  {total:>4d}  {cumulative:>6d}  {elem:>8s}")

    print()
    print("  Note: chemical shell closing (noble gases) occurs at")
    print("  2, 10, 18, 36 — not 2, 10, 28, 60 — because shells")
    print("  fill in energy order (Madelung rule), not n order.")
    print("  The geometric capacity of shell n is 2n², but higher-n")
    print("  s-orbitals are lower energy than lower-n d-orbitals.")
    print()

    print("  WHAT MAST ADDS:")
    print("  1. The '2' is DERIVED from tube winding topology (not postulated)")
    print("  2. The Bohr condition IS Ma quantization applied to S")
    print("     (integer windings → standing waves → closure)")
    print("  3. The torus is a PHYSICAL OBJECT fitting around the nucleus,")
    print("     not an abstract probability cloud")
    print("  4. The same closure condition that gives particle masses on")
    print("     Ma gives shell structure in S — one mechanism, two domains")
    print()
    print("  WHAT MAST DOES NOT ADD (yet):")
    print("  1. The n² angular count follows from spherical harmonics on S")
    print("     — MaSt doesn't derive it from a different starting point")
    print("  2. The Madelung filling order (why 4s before 3d) is not")
    print("     explained by torus geometry")
    print("  3. The Pauli exclusion is reinterpreted (topology of tube")
    print("     winding) but the antisymmetry of the wave function is")
    print("     not yet derived from Ma structure")
    print()

    print("Track 5 complete.")


if __name__ == '__main__':
    main()
