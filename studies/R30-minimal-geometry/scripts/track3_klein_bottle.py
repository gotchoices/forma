#!/usr/bin/env python3
"""
R30 Track 3: Klein bottle and non-orientable identifications.

On a torus T², opposite edges are identified with the same orientation:
    (x, 0) ~ (x, L₂)   and   (0, y) ~ (L₁, y)

On a Klein bottle K², one pair is reversed:
    (x, 0) ~ (x, L₂)   and   (0, y) ~ (L₁, L₂ − y)

This reversal has profound consequences for:
    1. The mode spectrum (Laplacian eigenvalues)
    2. Geodesic closure (how curves wrap)
    3. The charge mechanism (Gauss flux on a non-orientable surface)
    4. Spin (phase accumulation along curves)

We compute all four and compare to T².

Also addresses the user's questions:
    - Does the aspect ratio need to be fixed, or can reality be a curve?
    - Is the geometry flexible / elastic?
"""

import sys, os, math
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.ma import (
    alpha_ma, hbar_c_MeV_fm, M_E_MEV, M_P_MEV, ALPHA,
)

TWO_PI_HC = 2 * math.pi * hbar_c_MeV_fm


print("=" * 72)
print("R30 TRACK 3: KLEIN BOTTLE AND NON-ORIENTABLE IDENTIFICATIONS")
print("=" * 72)


# ══════════════════════════════════════════════════════════════════════
#  Section 1: Mode spectrum comparison
# ══════════════════════════════════════════════════════════════════════

print("\n\n── Section 1: Mode spectrum — T² vs Klein bottle ──\n")

print("  T² eigenvalues (flat metric, no shear):")
print("    E²(n₁, n₂) = (2π/L₁)² n₁² + (2π/L₂)² n₂²")
print("    for (n₁, n₂) ∈ Z²")
print()
print("  Klein bottle eigenvalues:")
print("    Family A (m = 0, y-independent):")
print("      E²(n, 0) = (2πn/L₁)²")
print("      n ∈ Z, same as T² with n₂ = 0")
print()
print("    Family B (m ≥ 1, y-dependent):")
print("      E²(n, m) = (πn/L₁)² + (2πm/L₂)²")
print("      n ∈ Z, m = 1, 2, 3, ...")
print("      NOTE: tube quantization is π/L₁, not 2π/L₁ — half-steps!")
print()
print("  The reversal doubles the effective tube period for y-dependent")
print("  modes.  A mode that winds once in x sees the y-direction")
print("  reflected, so it must wind TWICE to return to the same state.")
print("  This halves the tube momentum quantization.")


# Compute and compare spectra

r_test = 8.906  # use proton aspect ratio for comparison
L_ring = 1.0    # arbitrary units; energy ratios are what matter
L_tube = r_test * L_ring

def t2_eigenvalues(n1, n2, L1, L2):
    """T² energy² in units of (2π/L₂)²."""
    return (n1 * L2 / L1)**2 + n2**2

def kb_eigenvalue_A(n, L1, L2):
    """Klein bottle family A: y-independent."""
    return (n * L2 / L1)**2

def kb_eigenvalue_B(n, m, L1, L2):
    """Klein bottle family B: y-dependent, half-quantized tube."""
    return (n * L2 / (2 * L1))**2 + m**2

print(f"\n  Comparison at r = {r_test} (L_tube/L_ring):\n")
print(f"  {'Mode':>12s} {'T² E²':>10s} {'KB E²':>10s} {'Match?':>8s}")
print(f"  {'─'*44}")

# Collect T² modes
t2_modes = []
for n1 in range(-5, 6):
    for n2 in range(-5, 6):
        if n1 == 0 and n2 == 0:
            continue
        E2 = t2_eigenvalues(n1, n2, L_tube, L_ring)
        t2_modes.append((E2, n1, n2))
t2_modes.sort()

# Collect KB modes
kb_modes = []
# Family A
for n in range(-10, 11):
    if n == 0:
        continue
    E2 = kb_eigenvalue_A(n, L_tube, L_ring)
    kb_modes.append((E2, n, 0, 'A'))
# Family B
for n in range(-10, 11):
    for m in range(1, 6):
        E2 = kb_eigenvalue_B(n, m, L_tube, L_ring)
        kb_modes.append((E2, n, m, 'B'))
kb_modes.sort()

print(f"\n  First 15 T² modes:")
for E2, n1, n2 in t2_modes[:15]:
    print(f"    ({n1:+d},{n2:+d})  E² = {E2:8.4f}")

print(f"\n  First 15 Klein bottle modes:")
for E2, n, m, fam in kb_modes[:15]:
    label = f"({n:+d},{m:+d})" if fam == 'B' else f"({n:+d}, 0)"
    print(f"    {label:>8s} [{fam}]  E² = {E2:8.4f}")


# ══════════════════════════════════════════════════════════════════════
#  Section 2: Where is the electron (1,2) mode on a Klein bottle?
# ══════════════════════════════════════════════════════════════════════

print("\n\n── Section 2: The (1,2) mode — torus vs Klein bottle ──\n")

print("  On T²:")
E2_t2 = t2_eigenvalues(1, 2, L_tube, L_ring)
print(f"    (1,2) mode:  E² = (1/r)² + 2² = {E2_t2:.6f}")
print(f"    This is the electron (or proton) — the fundamental charged mode.")
print()

print("  On Klein bottle:")
print("    The (1,2) mode does NOT map directly.")
print()
print("    Family A (m=0): only tube modes, no ring winding.")
print("    Family B (m=2): E² = (n/(2r))² + 2² = (n/{:.3f})² + 4".format(2*r_test))
print()

E2_kb_n1 = kb_eigenvalue_B(1, 2, L_tube, L_ring)
E2_kb_n2 = kb_eigenvalue_B(2, 2, L_tube, L_ring)
print(f"    KB (n=1, m=2): E² = {E2_kb_n1:.6f}")
print(f"    KB (n=2, m=2): E² = {E2_kb_n2:.6f}")
print(f"    T² (1,2):      E² = {E2_t2:.6f}")
print()

# The T² (1,2) has tube momentum 2π×1/L₁ = 2π/L₁
# The KB family B has tube momentum π×n/L₁
# To match the same tube momentum: π×n/L₁ = 2π×1/L₁ → n = 2
print("  To match the T² tube momentum (2π/L₁):")
print("    KB needs n = 2 (since πn/L₁ = 2π/L₁ → n = 2)")
print(f"    KB (n=2, m=2): E² = {E2_kb_n2:.6f}")
print(f"    T² (1,2):      E² = {E2_t2:.6f}")
print(f"    These are IDENTICAL — same energy.")
print()
print("  But the KB mode (n=2, m=2) has n₁ = 2 (even).")
print("  On T², Q = −n₁ means charge comes from tube winding parity.")
print("  On KB, n = 2 is even → charge = 0 under the T² convention!")
print()
print("  The KB ALSO has a NEW mode at (n=1, m=2):")
print(f"    E² = {E2_kb_n1:.6f} vs electron E² = {E2_t2:.6f}")
print(f"    This has n = 1 (odd → could carry charge)")
print(f"    But its energy is DIFFERENT from the electron.")
print(f"    E_KB / E_T² = {math.sqrt(E2_kb_n1/E2_t2):.6f}")


# ══════════════════════════════════════════════════════════════════════
#  Section 3: Geodesics on the Klein bottle
# ══════════════════════════════════════════════════════════════════════

print("\n\n── Section 3: Geodesics on the Klein bottle ──\n")

print("  On T²: a geodesic with slope n₂/n₁ closes after |n₁| tube")
print("  circuits and |n₂| ring circuits.  The (1,2) geodesic closes")
print("  after 1 tube circuit, wrapping the ring twice.")
print()
print("  On Klein bottle: the y-direction is REFLECTED at each tube")
print("  circuit.  A geodesic starting at (x₀, y₀) with velocity")
print("  (v_x, v_y) reaches (x₀ + L₁, y₀ + v_y L₁/v_x) after one")
print("  tube circuit, then gets mapped to:")
print()
print("    y → L₂ − y   and   v_y → −v_y  (velocity reversal)")
print()
print("  So the geodesic BOUNCES in the ring direction every tube")
print("  circuit.  It only closes after an EVEN number of tube circuits.")
print()

# Trace a (1,2)-like geodesic on KB
print("  Tracing (1,2) geodesic on Klein bottle:")
print("    Start: y₀ = 0, v_y/v_x = 2L₂/L₁")
print()

y = 0.0
vy_sign = +1
for circuit in range(1, 5):
    dy = vy_sign * 2.0  # in units of L₂
    y_new = y + dy
    y_new_mod = y_new % 1.0  # mod L₂
    # Klein bottle reflection
    y_reflected = 1.0 - y_new_mod
    vy_sign *= -1

    closed = abs(y_reflected) < 0.001 or abs(y_reflected - 1.0) < 0.001
    print(f"    Circuit {circuit}: y goes {y:.3f} → {y_new_mod:.3f}"
          f" → reflected to {y_reflected:.3f}"
          f"  {'← CLOSED' if closed and circuit > 1 else ''}")
    y = y_reflected

print()
print("  The (1,2) geodesic on KB closes after 2 tube circuits,")
print("  not 1.  It traces a path that wraps the tube TWICE and")
print("  the ring FOUR times (2 forward, 2 backward).")
print()
print("  On T²: (1,2) → 1 circuit, winding number n₁ = 1")
print("  On KB: (1,2) → 2 circuits, effective n₁ = 2 (even!)")
print()
print("  This means the fundamental charged geodesic on KB")
print("  has even tube winding.  Even winding → zero charge")
print("  and spin 0 under the T² parity rules.")


# ══════════════════════════════════════════════════════════════════════
#  Section 4: Charge on a non-orientable surface
# ══════════════════════════════════════════════════════════════════════

print("\n\n── Section 4: Charge on a non-orientable surface ──\n")

print("  The T² charge mechanism (R19) relies on:")
print("    1. Gauss's law: ∮ E·dA = Q_enclosed")
print("    2. The surface integral requires a consistent ORIENTATION")
print("    3. The sheared geodesic wraps n₁ times around the tube,")
print("       picking up a phase 2πn₁s from the shear")
print("    4. Quantized charge = integer × e")
print()
print("  On a Klein bottle:")
print("    - The surface is NON-ORIENTABLE: there is no consistent")
print("      choice of 'inside' vs 'outside'")
print("    - Gauss's law requires ∮ E·dA with a consistently oriented")
print("      normal vector, but on a Klein bottle the normal vector")
print("      flips sign after one tube circuit")
print("    - The 'enclosed charge' changes sign depending on which")
print("      side of the surface you call 'inside'")
print("    - Therefore: CHARGE IS ILL-DEFINED on a Klein bottle")
print()
print("  From the Kaluza-Klein perspective:")
print("    - The gauge field A_μ ∝ g_μθ (off-diagonal metric)")
print("    - On KB, θ → −θ after one circuit")
print("    - So A_μ → −A_μ (gauge field changes sign!)")
print("    - A gauge field that changes sign around a loop is a")
print("      Z₂ gauge field, not U(1)")
print("    - Z₂ gauge fields produce ±1 charges, not integer charges")
print("    - But they don't give the continuous U(1) symmetry needed")
print("      for electromagnetism")
print()
print("  CONCLUSION: The Klein bottle structurally CANNOT support")
print("  the U(1) gauge field that produces electric charge.")
print("  Non-orientability is incompatible with the Ma charge")
print("  mechanism.")


# ══════════════════════════════════════════════════════════════════════
#  Section 5: Spin on a Klein bottle
# ══════════════════════════════════════════════════════════════════════

print("\n\n── Section 5: Spin on a Klein bottle ──\n")

print("  On T², spin-½ comes from odd tube windings.")
print("  The E-field picks up a phase of π per tube traversal,")
print("  requiring two traversals (2π) for return → spin ½.")
print()
print("  On KB, the fundamental closed geodesic wraps the tube")
print("  TWICE (Section 3), giving 2π phase from geometry alone.")
print("  This is already a full 2π rotation — spin 0 or 1, not ½.")
print()
print("  For spin ½, we need a closed curve that wraps the tube")
print("  an ODD number of times.  On KB, no such curve exists:")
print("  the y-reflection forces all closed geodesics to have")
print("  EVEN tube winding.")
print()
print("  CONCLUSION: The Klein bottle cannot produce spin-½")
print("  particles.  All closed modes have even tube winding,")
print("  giving only integer spin.")


# ══════════════════════════════════════════════════════════════════════
#  Section 6: What about the Möbius strip?
# ══════════════════════════════════════════════════════════════════════

print("\n\n── Section 6: Other non-orientable spaces ──\n")

print("  Möbius strip: non-orientable with a BOUNDARY.")
print("    Not compact → cannot support periodic modes.")
print("    Boundary conditions would break translational symmetry.")
print("    Ruled out for particle physics.")
print()
print("  RP² (real projective plane): non-orientable, compact.")
print("    Identification: (x, y) ~ (L₁ − x, L₂ − y)")
print("    Both directions reflected simultaneously.")
print("    All closed geodesics have even total winding → same")
print("    problem as Klein bottle for charge and spin.")
print()
print("  General principle: non-orientability is INCOMPATIBLE")
print("  with the charge/spin mechanisms in this model.")
print("  The mechanisms require:")
print("    - Consistent orientation for Gauss's law (charge)")
print("    - Odd tube winding for spin ½")
print("  Both are structurally impossible on non-orientable surfaces.")


# ══════════════════════════════════════════════════════════════════════
#  Section 7: The r-freedom and elastic geometry
# ══════════════════════════════════════════════════════════════════════

print("\n\n── Section 7: Does r need to be fixed? Elastic geometry ──\n")

print("  Track 4 showed: r is free because charge is topological.")
print("  The charge mechanism needs shear to EXIST but doesn't care")
print("  about its magnitude.  The α formula adjusts s(r) to keep")
print("  α = 1/137 at every r > 0.26.")
print()
print("  This raises the user's question: CAN the geometry be elastic?")
print()

print("  Three interpretations of 'flexible r':")
print()
print("  (A) STATIC FLEXIBILITY: r is a constant of nature, but we")
print("      don't know which value nature chose.  Physics works the")
print("      same at every r.  This is what the model currently says.")
print()
print("  (B) DYNAMIC FLEXIBILITY: r can change over time or vary")
print("      in space.  The torus literally stretches and contracts.")
print("      This would be a 'breathing mode' of the compact geometry")
print("      — a scalar field in 4D (called a 'modulus' or 'radion').")
print("      Such fields are a standard prediction of KK theories.")
print("      If r can change dynamically:")
print("        - Charge stays quantized (topological, r-independent)")
print("        - Mass changes (ring circumference changes)")
print("        - The breathing mode itself carries energy")
print("        - Stabilizing r requires a potential energy function")
print("          with a minimum — otherwise r rolls to 0 or ∞")
print()
print("  (C) CURVE SOLUTION: reality is not a single r but a")
print("      CURVE through (r, s) space satisfying α(r,s) = 1/137.")
print("      The geometry is a 1-parameter family parameterized")
print("      by position along the curve.  This is a more radical")
print("      idea: the compact geometry itself might vary along")
print("      the extended spatial dimensions (R³), with r(x) being")
print("      a field.  This is called 'moduli space' in string theory.")

print()
print("  What the model tells us:")
print()

# The α constraint defines a curve in (r, s) space
print("  The α = 1/137 constraint defines a CURVE in (r, s) space:\n")
print(f"    {'r':>8s} {'s':>10s} {'r²s²':>10s}")
print(f"    {'─'*30}")

from lib.ma import solve_shear_for_alpha

extended_solve = None
try:
    from scipy.optimize import brentq

    def extended_solve(r):
        s_scan = np.concatenate([
            np.linspace(1e-8, 1e-4, 500),
            np.linspace(1e-4, 0.01, 500),
            np.linspace(0.01, 0.49, 2000),
        ])
        a_scan = [alpha_ma(r, s) for s in s_scan]
        for i in range(len(s_scan) - 1):
            if (a_scan[i] - ALPHA) * (a_scan[i + 1] - ALPHA) < 0:
                return brentq(lambda s: alpha_ma(r, s) - ALPHA,
                              s_scan[i], s_scan[i + 1])
        return None
except ImportError:
    extended_solve = solve_shear_for_alpha

curve_points = []
for r in [0.26, 0.3, 0.5, 1.0, 2.0, 5.0, 6.6, 8.906, 20, 100, 1000]:
    s = extended_solve(r)
    if s is not None:
        curve_points.append((r, s))
        print(f"    {r:8.3f} {s:10.6f} {r**2 * s**2:10.6f}")

print()
print("  This curve has a striking property: r²s² ≈ 0.00465")
print("  (converging to a constant).  The PRODUCT rs determines")
print("  the physics; r and s individually do not.")
print()
print("  A particle IS this curve — not a point on it.  The electron")
print("  is any (r, s) pair satisfying α(r, s) = 1/137 and")
print("  E₁₂ = 0.511 MeV.  All such pairs give the same charge,")
print("  spin, mass, and α.  The geometry is a one-parameter")
print("  family of solutions, all physically equivalent.")
print()
print("  Whether r is 'fixed at a value we don't know' or")
print("  'fluctuating because it doesn't matter' is a question")
print("  about dynamics, not kinematics.  The model as currently")
print("  formulated is kinematic — it computes spectra, not")
print("  time evolution.  Both interpretations are consistent.")


# ══════════════════════════════════════════════════════════════════════
#  Section 8: Can the geometry be bent or run within?
# ══════════════════════════════════════════════════════════════════════

print("\n\n── Section 8: Elastic geometry — bending and running ──\n")

print("  The T² is currently treated as FLAT (constant metric).")
print("  What if it has curvature — a local deformation?")
print()
print("  Three types of deformation:")
print()
print("  1. BENDING (extrinsic curvature):")
print("     The torus is embedded in a higher-dimensional space and")
print("     curves through it.  A physical donut has this — the outer")
print("     rim is curved differently from the inner rim.  This breaks")
print("     the translational symmetry of the flat torus and changes")
print("     the mode spectrum.  On a bent torus:")
print("       - Modes concentrate on regions of less curvature")
print("       - Energy levels shift and split")
print("       - The uniform winding picture breaks down")
print("     Our model uses an ABSTRACT flat torus (no embedding).")
print("     Adding curvature is possible but adds parameters.")
print()
print("  2. INTRINSIC CURVATURE (Ricci curvature):")
print("     The torus itself has a non-flat metric, like a surface")
print("     of varying density.  The Gauss-Bonnet theorem constrains")
print("     this: ∫ K dA = 2πχ, and for a torus χ = 0, so the TOTAL")
print("     curvature must vanish.  The torus can be locally curved")
print("     (hills and valleys) but the average curvature is zero.")
print("     This is equivalent to Track 2's 'non-uniform metric' on")
print("     T¹, extended to 2D.  It could produce Mathieu-like")
print("     band structure.")
print()
print("  3. MODULI VARIATION (the shape changes in space/time):")
print("     r varies as a function of position in R³: r(x,y,z).")
print("     The compact geometry literally 'runs' — it's different")
print("     at different locations.  This is the 'moduli space'")
print("     picture.  Since charge is r-independent (Track 4),")
print("     charge is constant everywhere.  But mass (from the ring")
print("     circumference) would vary — a spatially varying electron")
print("     mass!  This is constrained by observation: the electron")
print("     mass is the same everywhere we've measured it.")
print()
print("  All three deformations are physically possible in principle.")
print("  The FLAT torus is the simplest (fewest parameters) and")
print("  matches all current observations.  Adding curvature or")
print("  moduli variation would need to be motivated by a specific")
print("  observational discrepancy.")
print()

# What about a wave RUNNING along the curve?
print("  The user asks: can a wave 'run within' the geometry?")
print()
print("  Yes — that's exactly what a particle IS in this model.")
print("  The electron is a standing wave running along the (1,2)")
print("  geodesic of the T².  It runs 'within' the compact")
print("  geometry.  The wave wraps around the torus, and the")
print("  pattern of wrapping determines the particle's properties.")
print()
print("  The standing wave occupies the ENTIRE torus simultaneously")
print("  — it's not localized at one point.  It's a resonance of")
print("  the whole geometry, like a bell ringing.  Different modes")
print("  (different wrapping patterns) give different particles.")
print()
print("  Adding propagation in R³ (the wave moves through space)")
print("  gives a MASSIVE particle moving through 3D — the usual")
print("  physics of a particle with mass.  The mass comes from")
print("  the compact wrapping; the motion comes from R³.")


# ══════════════════════════════════════════════════════════════════════
#  Summary
# ══════════════════════════════════════════════════════════════════════

print("\n\n── Summary ──\n")

print("  1. KLEIN BOTTLE KILLS CHARGE AND SPIN.")
print("     Non-orientability prevents:")
print("     (a) Consistent Gauss flux → no U(1) charge")
print("     (b) Odd tube winding → no spin-½")
print("     The KK gauge field becomes Z₂ (sign-flip), not U(1).")
print("     Non-orientable material spaces are ruled out.")
print()
print("  2. THE TORUS (T²) IS THE MINIMUM ORIENTABLE COMPACT SURFACE.")
print("     Compact + orientable + 2D → T² is the unique choice.")
print("     (The sphere S² has no cycles for winding numbers.)")
print("     This makes T² structurally inevitable, not arbitrary.")
print()
print("  3. r DOES NOT NEED TO BE FIXED.")
print("     The α = 1/137 constraint defines a curve in (r, s) space.")
print("     All points on the curve give identical physics (charge,")
print("     spin, mass, α).  The geometry is a one-parameter family.")
print("     Whether r is a specific constant or a fluctuating modulus")
print("     is a dynamical question the model doesn't yet address.")
print()
print("  4. THE GEOMETRY CAN BE ELASTIC in principle:")
print("     - Bending: extrinsic curvature in embedding space")
print("     - Curvature: intrinsic hills/valleys (Gauss-Bonnet = 0)")
print("     - Moduli variation: r(x) varies in space")
print("     All are possible but unconstrained by current data.")
print("     The flat torus is the simplest model consistent with")
print("     observation.")
print()
print("  5. REALITY AS A CURVE:")
print("     The particle is not a point on the torus — it's the")
print("     entire resonant pattern.  The geometry provides the")
print("     stage; the standing wave is the actor.  Different")
print("     wrapping patterns = different particles.")
print("     The 'curve solution' is the (r, s) family of equivalent")
print("     geometries: the physics lives on the curve α = 1/137,")
print("     not at a specific point on it.")
