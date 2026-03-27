"""
R14 Track 0: Feasibility check for universal geometry hypothesis.

Three questions:
  1. Can multiple geodesics on T² be topologically linked?
  2. Does T³ enable linking? Connection to 3 color charges?
  3. Does the proton mass fit as three photon harmonics on the
     electron's T² geometry?

Bears on: R14 README, Q26 (multi-photon hadrons)
"""

import math

# Physical constants
alpha = 1 / 137.035999084
m_e_MeV = 0.51099895       # electron mass in MeV
m_p_MeV = 938.27208816     # proton mass in MeV
m_n_MeV = 939.56542052     # neutron mass in MeV
m_u_MeV = 2.16             # up quark mass (current, MS-bar)
m_d_MeV = 4.67             # down quark mass (current, MS-bar)
r_e = 2.8179403262e-15     # classical electron radius (m)
lambda_C = 2.42631023867e-12  # Compton wavelength (m)
hbar_c_MeV_fm = 197.3269804   # ℏc in MeV·fm


def section(title):
    print(f"\n{'=' * 65}")
    print(f"  {title}")
    print(f"{'=' * 65}")


def subsection(title):
    print(f"\n--- {title} ---")


# ================================================================
# PART 1: Geodesic topology on T²
# ================================================================
section("PART 1: Can geodesics on T² be topologically linked?")

print("""
On a flat T² = R²/Λ, closed geodesics are straight lines with
rational slope.  A geodesic with winding numbers (p, q) wraps
p times around the minor circle and q times around the major.

Key topological fact: on a 2D surface, closed curves CANNOT LINK.
Linking is a 3D concept — one curve must pass through the interior
of another, requiring a third dimension.

However, curves on T² CAN:
  - Intersect (cross each other at points)
  - Be homotopically distinct (different winding classes)
  - Be non-separable in certain senses (homological linking)

The intersection number of two curves with winding numbers
(p₁, q₁) and (p₂, q₂) on T² is:

    I = |p₁ q₂ - p₂ q₁|
""")

subsection("Intersection numbers for candidate geodesic pairs")

geodesics = [
    ("electron (1,2)", 1, 2),
    ("electron' (1,2) shifted", 1, 2),
    ("(1,3) geodesic", 1, 3),
    ("(2,3) geodesic", 2, 3),
    ("(1,1) geodesic", 1, 1),
    ("(3,5) geodesic", 3, 5),
]

print(f"{'Curve A':>25s}  {'Curve B':>25s}  {'I = |p1q2-p2q1|':>16s}")
print("-" * 70)
for i in range(len(geodesics)):
    for j in range(i + 1, len(geodesics)):
        na, p1, q1 = geodesics[i]
        nb, p2, q2 = geodesics[j]
        I = abs(p1 * q2 - p2 * q1)
        print(f"{na:>25s}  {nb:>25s}  {I:>16d}")

print("""
Key result: Two geodesics in the SAME winding class (p,q)
have intersection number 0 — they can be deformed to be
parallel (non-intersecting).  Three electrons on T² don't
cross each other.

Geodesics in DIFFERENT winding classes DO intersect.  A (1,2)
and a (1,3) cross once.  A (1,2) and a (2,3) cross once.
""")

subsection("Can 'linking' on T² arise from homology?")

print("""
Although curves on T² can't link in the 3D sense, there is a
notion of HOMOLOGICAL LINKING on T²:

Two curves α, β on T² have a homological linking number equal
to their algebraic intersection number.  This is a topological
invariant: if I(α, β) ≠ 0, neither curve can be continuously
deformed to avoid the other.

For 1D curves on a 2D surface, this is as close to "linking"
as you can get.  The curves must cross, and the crossing is
topologically enforced.

Physical meaning: if two photons on T² have different winding
classes, their paths MUST cross.  At each crossing, the EM
fields interact.  This forced interaction could bind the
photons even without 3D linking.

BUT: three photons all in the (1,2) class have I = 0 pairwise.
They don't cross — they're parallel.  So for a three-quark
proton built from (1,2) geodesics, there is NO forced
topological interaction on T².
""")

subsection("Assessment: T² linking")

print("""
VERDICT: T² does NOT support topological linking of geodesics.
- Same-class geodesics (all (1,2)) don't intersect: I = 0
- Different-class geodesics intersect but don't link (2D)
- No mechanism for confinement from topology on T²

This is a NEGATIVE result for the R14 hypothesis as
originally framed (Borromean links of photons on T²).
""")


# ================================================================
# PART 2: Does T³ enable linking?
# ================================================================
section("PART 2: Does T³ = S¹ × S¹ × S¹ enable linking?")

print("""
Linking requires at least 3 spatial dimensions.  On T³ (three
compact dimensions), closed curves CAN form genuine links:

- T³ has fundamental group π₁(T³) = Z³ (three integer winding
  numbers per curve)
- Two closed curves in T³ can be topologically linked if they
  wind around different pairs of dimensions
- The linking number in T³ generalizes the 2D intersection
  number to 3D

A curve on T³ has winding numbers (n₁, n₂, n₃) around the
three circles.  Two curves α, β in T³ have a linking number
computed from their winding vectors and relative positions.

Crucially: two curves that wind around DIFFERENT pairs of
dimensions can be linked.  For example:
  - Curve A winds around dimensions 1 and 2: (1, 2, 0)
  - Curve B winds around dimensions 2 and 3: (0, 1, 1)
  These can form a nontrivial link in T³.
""")

subsection("Linking on T³ and three colors")

print("""
Three compact dimensions naturally accommodate three types of
linking:
  - Linking in the (1,2) plane
  - Linking in the (2,3) plane
  - Linking in the (1,3) plane

Three curves, each winding primarily in a different plane, form
a three-component link.  Each component is topologically
distinct — it cannot be deformed into either of the others.

This is suggestive of THREE COLOR CHARGES:
  - Three compact dimensions → three distinct link types
  - Three quarks → three curves, each in a different plane
  - Color neutrality → the three-component link is
    topologically trivial as a whole (Borromean property:
    remove one curve and the other two unlink)

The connection to QCD's SU(3) color symmetry:
  - SU(3) has 3 fundamental representations
  - T³ has 3 pairs of dimensions for linking
  - The correspondence is: color index ↔ which pair of
    compact dimensions the curve winds around
""")

subsection("Borromean links on T³")

print("""
A Borromean link has the property that:
  - Three curves are mutually linked (can't separate all three)
  - Any two are UNlinked (remove one and the other two separate)

This is exactly quark confinement:
  - Can't extract one quark (one curve) from the proton
  - But mesons (quark-antiquark = two curves) CAN exist as
    separate entities (the two are linked pairwise)

On T³, a Borromean-like configuration is:
  Curve A: (1, 0, 0) — winds around dim 1
  Curve B: (0, 1, 0) — winds around dim 2
  Curve C: (0, 0, 1) — winds around dim 3

Any pair has linking number 0 in T³ (they wind around
different circles and don't interact).  But all three together
cannot be simultaneously separated to non-interacting
positions — they share the compact space.

Whether this gives genuine Borromean topology depends on the
specific path configurations, not just the winding numbers.
A rigorous analysis requires computing the Milnor invariants
of the three-component link in T³.
""")

subsection("Assessment: T³ linking")

print("""
VERDICT: T³ DOES support topological linking.
- Genuine 3D links between closed curves are possible
- Three compact dimensions ↔ three color charges (suggestive)
- Borromean-like configurations may exist (needs rigorous check)
- This motivates considering T³ instead of T² as the compact
  space

IMPORTANT IMPLICATION: If T³ is needed for multi-photon
linking, then the electron also lives on T³ (not T²).  The
electron would use only 2 of the 3 dimensions for its (1,2)
winding, with the third dimension playing no role for a
single-photon state but becoming essential for multi-photon
states (hadrons).
""")


# ================================================================
# PART 3: Proton mass arithmetic
# ================================================================
section("PART 3: Proton mass from three photons on shared geometry")

subsection("Basic mass ratios")

ratio_pe = m_p_MeV / m_e_MeV
ratio_ne = m_n_MeV / m_e_MeV
print(f"m_p / m_e = {ratio_pe:.4f}")
print(f"m_n / m_e = {ratio_ne:.4f}")
print(f"(m_n - m_p) / m_e = {(m_n_MeV - m_p_MeV) / m_e_MeV:.4f}")

subsection("Three equal photons")

E_per_photon = m_p_MeV / 3
n_per_photon = E_per_photon / m_e_MeV
print(f"\nIf proton = 3 equal-energy photons:")
print(f"  Energy per photon: {E_per_photon:.4f} MeV")
print(f"  Harmonic number:   {n_per_photon:.4f}")
print(f"  Nearest integer:   {round(n_per_photon)}")
print(f"  3 × {round(n_per_photon)} × m_e = {3 * round(n_per_photon) * m_e_MeV:.4f} MeV")
print(f"  Proton mass:       {m_p_MeV:.4f} MeV")
print(f"  Discrepancy:       {abs(3 * round(n_per_photon) * m_e_MeV - m_p_MeV):.4f} MeV "
      f"({abs(3 * round(n_per_photon) * m_e_MeV - m_p_MeV) / m_p_MeV * 100:.3f}%)")

subsection("Two up + one down quark energies")

print(f"\nUsing current quark masses (MS-bar, 2 GeV):")
print(f"  m_u = {m_u_MeV:.2f} MeV  →  n_u = m_u/m_e = {m_u_MeV / m_e_MeV:.2f}")
print(f"  m_d = {m_d_MeV:.2f} MeV  →  n_d = m_d/m_e = {m_d_MeV / m_e_MeV:.2f}")
print(f"  Sum: 2m_u + m_d = {2 * m_u_MeV + m_d_MeV:.2f} MeV")
print(f"  Proton mass:      {m_p_MeV:.2f} MeV")
print(f"  Deficit:          {m_p_MeV - (2 * m_u_MeV + m_d_MeV):.2f} MeV ({(m_p_MeV - (2 * m_u_MeV + m_d_MeV)) / m_p_MeV * 100:.1f}%)")

print(f"""
NOTE: Current quark masses (2+2+5 ≈ 9 MeV) account for only
~1% of the proton mass.  The other ~99% comes from QCD binding
energy (gluon field energy + kinetic energy of quarks).

In the WvM framework, there are no gluons.  The proton's mass
must come from the photon energies directly.  Two scenarios:

  A. Three photons each carry ~313 MeV (equal split)
     → harmonic n ≈ 613 on the electron's T²
     → total 3 × 613 × m_e ≈ 939.2 MeV (0.1% from m_p)

  B. Three photons carry unequal energies matching quark
     masses... but then 99% of the mass is missing.

Scenario A is far more natural in this framework: the proton
mass IS the three photons' total energy, not a small fraction
of it.  "Current quark masses" (which are QCD-renormalized
quantities) would have no meaning here — each photon carries
~1/3 of the proton's total energy.
""")

subsection("Harmonic structure on the electron's geometry")

print("Allowed harmonics on the electron's T²:")
print(f"{'n':>6s}  {'Mass (MeV)':>12s}  {'Particle?':>20s}")
print("-" * 44)

matches = [
    (1,    m_e_MeV,    "electron"),
    (207,  207 * m_e_MeV, "muon?"),
    (3477, 3477 * m_e_MeV, "tau?"),
]

m_mu_MeV = 105.6583755
m_tau_MeV = 1776.86

for n in [1, 2, 3, 4, 5, 10, 100, 206, 207, 208, 612, 613, 614,
          1836, 1837, 1838, 3477, 3478]:
    mass = n * m_e_MeV
    label = ""
    if n == 1:
        label = "electron"
    elif abs(mass - m_mu_MeV) / m_mu_MeV < 0.01:
        label = f"muon? (actual {m_mu_MeV:.2f})"
    elif abs(mass - m_tau_MeV) / m_tau_MeV < 0.01:
        label = f"tau? (actual {m_tau_MeV:.2f})"
    elif abs(mass - m_p_MeV / 3) / (m_p_MeV / 3) < 0.01:
        label = f"proton/3? (actual {m_p_MeV/3:.2f})"
    elif abs(mass - m_p_MeV) / m_p_MeV < 0.01:
        label = f"proton? (actual {m_p_MeV:.2f})"
    print(f"{n:>6d}  {mass:>12.4f}  {label:>20s}")

subsection("Lepton mass ratios vs integer harmonics")

print(f"\nm_μ / m_e = {m_mu_MeV / m_e_MeV:.6f}  (nearest int: {round(m_mu_MeV / m_e_MeV)})")
print(f"m_τ / m_e = {m_tau_MeV / m_e_MeV:.6f}  (nearest int: {round(m_tau_MeV / m_e_MeV)})")
print(f"m_p / m_e = {m_p_MeV / m_e_MeV:.6f}  (nearest int: {round(m_p_MeV / m_e_MeV)})")

frac_mu = m_mu_MeV / m_e_MeV
frac_tau = m_tau_MeV / m_e_MeV
print(f"\nMuon: {frac_mu:.4f} = {round(frac_mu)} + {frac_mu - round(frac_mu):.4f}")
print(f"  Fractional part: {(frac_mu - round(frac_mu)) / round(frac_mu) * 100:.2f}%")
print(f"Tau:  {frac_tau:.4f} = {round(frac_tau)} + {frac_tau - round(frac_tau):.4f}")
print(f"  Fractional part: {(frac_tau - round(frac_tau)) / round(frac_tau) * 100:.2f}%")

print("""
The muon and tau mass ratios are NOT integers:
  m_μ/m_e ≈ 206.77 (0.11% from 207)
  m_τ/m_e ≈ 3477.2 (0.006% from 3477)

The muon is close to n=207 but not exact.  The tau is very
close to n=3477.  If the mass spectrum comes from harmonics,
the non-integer ratios might indicate:
  - Binding energy corrections
  - Slightly different geometry for each generation
  - The harmonic model is approximate
  - These are not harmonics at all
""")

subsection("Proton mass: the 3 × 612 coincidence")

n_proton = round(m_p_MeV / m_e_MeV)
residual = m_p_MeV / m_e_MeV - n_proton
print(f"m_p / m_e = {m_p_MeV / m_e_MeV:.6f}")
print(f"Nearest integer: {n_proton}")
print(f"Residual: {residual:.6f} ({residual / n_proton * 100:.4f}%)")
print(f"\n{n_proton} = 3 × {n_proton // 3} + {n_proton % 3}")
print(f"  → 3 × {n_proton // 3} × m_e = {3 * (n_proton // 3) * m_e_MeV:.4f} MeV")
print(f"  → vs m_p = {m_p_MeV:.4f} MeV")

print(f"\nActual ratio: {m_p_MeV / m_e_MeV:.6f}")
print(f"3 × 612 = {3 * 612}")
print(f"3 × 613 = {3 * 613}")
actual = m_p_MeV / m_e_MeV
print(f"Closer to 3×612 ({abs(actual - 1836):.4f}) or 3×613 ({abs(actual - 1839):.4f})? "
      f"→ 3×{'612' if abs(actual - 1836) < abs(actual - 1839) else '613'}")

# Check: is 1836 = 3 × 612 or does it factor differently?
print(f"\nFactorization of {n_proton}:")
n = n_proton
factors = []
for p in range(2, n + 1):
    while n % p == 0:
        factors.append(p)
        n //= p
    if n == 1:
        break
print(f"  {n_proton} = {' × '.join(str(f) for f in factors)}")

# Neutron
n_neutron = round(m_n_MeV / m_e_MeV)
print(f"\nm_n / m_e = {m_n_MeV / m_e_MeV:.4f}, nearest int = {n_neutron}")
print(f"  {n_neutron} = 3 × {n_neutron // 3} + {n_neutron % 3}")
print(f"  m_n - m_p = {m_n_MeV - m_p_MeV:.4f} MeV = {(m_n_MeV - m_p_MeV) / m_e_MeV:.4f} m_e")


# ================================================================
# SUMMARY
# ================================================================
section("SUMMARY")

print("""
1. TOPOLOGY ON T²: NEGATIVE
   Geodesics on T² cannot be topologically linked.  Same-class
   geodesics (all (1,2)) have intersection number 0 — they're
   parallel.  No mechanism for confinement on T².

2. TOPOLOGY ON T³: PROMISING
   T³ supports genuine 3D linking of closed curves.  Three
   compact dimensions naturally map to three color charges
   (linking in three planes).  Borromean-like configurations
   may be possible.  The electron would use 2 of 3 dimensions;
   hadrons use all 3.

3. PROTON MASS ARITHMETIC: SUGGESTIVE
   m_p / m_e = 1836.15.  If proton = 3 equal-energy photons,
   each at harmonic n = 612, then 3 × 612 = 1836 — within
   0.008% of m_p/m_e.  This is striking but may be coincidental.
   The non-integer residual (0.15 m_e ≈ 0.08 MeV) is much
   smaller than the n-p mass difference (2.53 m_e ≈ 1.29 MeV).

IMPLICATIONS:
   - R14 should be reframed around T³ (not T²)
   - The electron model needs re-examination on T³: a (1,2)
     geodesic on a 2D subspace of T³, with the third dimension
     flat (no winding)
   - Three compact dimensions = three extra spatial dimensions,
     for a total of 3+3+1 = 7 spacetime dimensions (or 6+1)
   - This connects to Q13 (three compact dimensions) and the
     S3 observation that three distinct a/R values produce the
     three charge quanta (e, 2e/3, e/3)
""")
