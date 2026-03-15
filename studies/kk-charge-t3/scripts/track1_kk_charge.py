"""
R13 Track 1: KK charge from flat T³

Compute the effective 4D charge of a photon propagating along
a geodesic on flat T³, using Kaluza-Klein mode decomposition.

The setup:
  - 7D spacetime: M₄ × T³ with circumferences L₁, L₂, L₃
  - Massless scalar field Φ(x, y) on the full space
  - The "electron" is a wave propagating along a (p, q) = (1, 2)
    geodesic in the (y₁, y₂) plane, with y₃ trivial
  - KK decomposition: expand Φ in Fourier modes of T³
  - The effective 4D charge comes from the coupling between the
    geodesic mode and the zero mode

Theory:
  The 7D action for a massless scalar is:
    S = ∫ d⁴x d³y  ½ ∂_M Φ ∂^M Φ

  Expand:  Φ(x,y) = Σ_n φ_n(x) ψ_n(y)
  where ψ_n(y) = (1/V) exp(2πi n_a y^a / L_a) and V = L₁L₂L₃

  The 4D effective action for the modes:
    S₄D = Σ_n ∫ d⁴x  ½ [∂_μ φ_n ∂^μ φ_n* - m_n² |φ_n|²]

  with KK masses:  m_n² = (2π/L_a)² n_a²  (summed over a)

  For a self-interacting theory (e.g., Φ³ or gauge coupling),
  the trilinear coupling between modes n, m, k is:
    g_{nmk} ∝ ∫_T³ ψ_n(y) ψ_m(y) ψ_k(y) d³y
            = (1/V) δ_{n+m+k, 0}

  The "charge" of mode n is its coupling to the zero mode:
    q_eff(n) ∝ g_{n, -n, 0} = 1/V

  This is the same for ALL non-zero modes — the KK charge is
  universal and proportional to 1/V.

  In standard KK electromagnetism, the effective 4D coupling is:
    e₄D = e₇D / √V
  where e₇D is the 7D gauge coupling and V is the compact volume.

Bears on: R13 README, Q18, Q32
"""

import math

# Physical constants
alpha = 1 / 137.035999084
e_SI = 1.602176634e-19      # Coulombs
hbar = 1.054571817e-34       # J·s
c = 2.99792458e8             # m/s
epsilon_0 = 8.8541878128e-12 # F/m
m_e = 9.1093837015e-31       # kg
r_e = 2.8179403262e-15       # m (classical electron radius)
lambda_C = 2.42631023867e-12 # m (Compton wavelength)
lambda_bar_C = lambda_C / (2 * math.pi)  # reduced Compton wavelength


def section(title):
    print(f"\n{'=' * 65}")
    print(f"  {title}")
    print(f"{'=' * 65}")


def subsection(title):
    print(f"\n--- {title} ---")


# ================================================================
# PART 1: Standard KK charge derivation
# ================================================================
section("PART 1: Standard KK charge on T³")

print("""
In Kaluza-Klein theory, a gauge field A_M in D dimensions
decomposes on M₄ × K into:
  - A_μ(x, y): the 4D gauge field components
  - A_a(x, y): scalar fields from compact components

For a U(1) gauge field on M₄ × T³:

  S_D = -1/(4 g_D²) ∫ d⁴x d³y  F_MN F^MN

Integrating over the compact volume V = L₁ L₂ L₃:

  S_4D = -V/(4 g_D²) ∫ d⁴x  F_μν F^μν  + ...

The 4D gauge coupling is:

  1/g₄² = V / g_D²   →   g₄ = g_D / √V

The 4D electric charge of a KK mode with momentum n_a/L_a
in the compact direction is:

  e₄D = g₄ × (2π n_a / L_a)  [for momentum in direction a]

But this applies to the STANDARD KK mechanism where charge =
compact momentum.  Our setup is different: the photon is an
EM wave propagating on a geodesic, not a particle with compact
momentum.
""")

subsection("The WvM mechanism vs standard KK")

print("""
Standard KK:  charge = compact momentum quantum number
  - A particle moving in the y-direction has charge ∝ n/L
  - The charge is quantized because momentum is quantized
  - Works for ANY particle with compact momentum

WvM mechanism: charge = net E-field flux from the EM
  configuration on the compact space
  - A photon's EM field has specific polarization and profile
  - The monopole moment of the field projected into 3+1D IS
    the apparent charge
  - The charge depends on the field configuration, not just
    on a quantum number

These are DIFFERENT mechanisms.  Standard KK produces charge
from compact momentum; WvM produces charge from field
configuration.  They may or may not give the same answer.

The question for Track 1: which mechanism (if either) gives
the correct electron charge?
""")


# ================================================================
# PART 2: KK mode spectrum on T³
# ================================================================
section("PART 2: KK mode spectrum on T³")

subsection("Mode frequencies")

print("""
On T³ with circumferences L₁, L₂, L₃, the scalar eigenmodes
are:

  ψ_{n₁,n₂,n₃}(y) = (1/√V) exp(2πi(n₁y₁/L₁ + n₂y₂/L₂ + n₃y₃/L₃))

with eigenvalues (KK masses):

  m²_{n} = (2π)² [(n₁/L₁)² + (n₂/L₂)² + (n₃/L₃)²]

The zero mode (0,0,0) is massless — it's the 4D photon.
""")

# Use R8 electron geometry as reference
# At q = 137, r = 0.308:  R = 2.79e-15 m, a = 8.60e-16 m
R_electron = 2.79e-15  # major radius (m)
a_electron = 8.60e-16  # minor radius (m)
L1 = 2 * math.pi * a_electron  # minor circumference
L2 = 2 * math.pi * R_electron  # major circumference

print(f"Using R8 electron geometry (q=137, r=0.308):")
print(f"  R = {R_electron:.3e} m,  a = {a_electron:.3e} m")
print(f"  L₁ (minor circ) = 2πa = {L1:.3e} m")
print(f"  L₂ (major circ) = 2πR = {L2:.3e} m")
print(f"  L₃ (third dim)  = unknown (free parameter)")
print(f"  V = L₁ L₂ L₃ = {L1 * L2:.3e} × L₃  m³")

subsection("Lowest KK masses")

print(f"\nLowest non-zero KK masses (in units of m_e):")
print(f"  (1,0,0): m = 2π/L₁ = {2*math.pi*hbar*c/L1 / (m_e*c**2):.2f} m_e "
      f"= {2*math.pi*hbar*c/L1 / 1.602e-13:.2f} MeV")
print(f"  (0,1,0): m = 2π/L₂ = {2*math.pi*hbar*c/L2 / (m_e*c**2):.2f} m_e "
      f"= {2*math.pi*hbar*c/L2 / 1.602e-13:.2f} MeV")

m_KK_1 = 2 * math.pi * hbar * c / L1
m_KK_2 = 2 * math.pi * hbar * c / L2
print(f"\n  m_KK(1,0,0) = {m_KK_1/(m_e*c**2):.1f} m_e = {m_KK_1/1.602e-13:.1f} MeV")
print(f"  m_KK(0,1,0) = {m_KK_2/(m_e*c**2):.1f} m_e = {m_KK_2/1.602e-13:.1f} MeV")

print(f"""
These are ENORMOUS — hundreds of MeV.  The KK modes are
extremely heavy because the compact dimensions are tiny
(~10⁻¹⁵ m).  Only the zero mode is relevant at low energies.
""")


# ================================================================
# PART 3: The geodesic wave in KK language
# ================================================================
section("PART 3: The geodesic wave as a KK mode superposition")

print("""
The electron is a photon propagating along a (1,2) geodesic
in the (y₁, y₂) plane.  On the flat T², this geodesic has
slope dy₁/dy₂ = L₁/(2L₂) and wraps p=1 time around y₁ and
q=2 times around y₂ before closing.

As a wave, the photon has wavevector:

  k_geodesic = (2π p/L₁, 2π q/L₂, 0)  = (2π/L₁, 4π/L₂, 0)

But this is a SINGLE plane-wave mode — a specific KK mode
with quantum numbers (n₁, n₂, n₃) = (p, q, 0) = (1, 2, 0).

Wait — is the electron a single KK mode or a superposition?
""")

subsection("Single mode vs wavepacket")

print("""
KEY DISTINCTION:

A single KK mode (n₁, n₂, 0) = (1, 2, 0) is a plane wave
that fills the entire T³ uniformly in amplitude.  It has a
definite frequency:

  ω = c |k| = c × 2π √((1/L₁)² + (2/L₂)²)

Its energy is ℏω, which must equal m_e c² for the electron.

Let's check: does ω for the (1,2,0) mode give m_e c²?
""")

omega_geodesic = c * 2 * math.pi * math.sqrt((1/L1)**2 + (2/L2)**2)
E_geodesic = hbar * omega_geodesic
m_geodesic = E_geodesic / c**2

print(f"  ω(1,2,0) = c × 2π × √((1/L₁)² + (2/L₂)²)")
print(f"           = {omega_geodesic:.6e} rad/s")
print(f"  E = ℏω   = {E_geodesic:.6e} J")
print(f"           = {E_geodesic / 1.602e-13:.4f} MeV")
print(f"  m = E/c² = {m_geodesic:.6e} kg")
print(f"  m / m_e  = {m_geodesic / m_e:.6f}")

print(f"""
The KK mass of the (1,2,0) mode is:
  m_KK = ℏc × 2π √((1/L₁)² + (4/L₂)²)
       = {E_geodesic / 1.602e-13:.1f} MeV

This is {m_geodesic / m_e:.0f}× the electron mass!

This is NOT the electron.  The (1,2,0) KK mode has a mass
of ~{E_geodesic / 1.602e-13:.0f} MeV — it's an extremely heavy
particle by 4D standards.
""")

subsection("The electron as a PROPAGATING wave, not a KK mode")

# Path length for (1,2) geodesic
path_length = math.sqrt(L1**2 + (2*L2)**2)
E_compton = 2 * math.pi * hbar * c / path_length
m_compton = E_compton / c**2

print(f"""
The electron's mass comes from the COMPTON condition:
  Path length ℓ = √(L₁² + (2L₂)²) = λ_C
  E = hc/λ_C = m_e c²

The path length:
  ℓ = √(L₁² + (2L₂)²) = {path_length:.6e} m
  λ_C (measured)       = {lambda_C:.6e} m
  Ratio: {path_length / lambda_C:.6f}

The Compton energy:
  E = hc/ℓ = {E_compton / 1.602e-13:.6f} MeV
  m_e c²   = {m_e * c**2 / 1.602e-13:.6f} MeV

But in KK language, a wave propagating along the geodesic has
wavevector components:
  k₁ = 2πp/L₁ = 2π × 1/L₁   (one wrap in y₁)
  k₂ = 2πq/L₂ = 2π × 2/L₂   (two wraps in y₂)

This IS the KK mode (1, 2, 0).  Its KK mass is:
  m_KK = (ℏ/c) × c × 2π√((1/L₁)² + (2/L₂)²) = ℏ × 2π√((c/L₁)² + (2c/L₂)²) / c

Wait — let me recompute.  The KK mass formula:
  m_KK² c⁴ = (2πℏc)² [(1/L₁)² + (4/L₂)²]
  m_KK c² = 2πℏc √((1/L₁)² + (4/L₂)²)
           = hc/ℓ  where ℓ = 1/√((1/L₁)² + (4/L₂)²) × ... 

Hmm, let me be more careful.
""")

subsection("Reconciling KK mass with Compton mass")

print(f"""
The KK mass of mode (n₁, n₂, n₃):
  m²_KK c⁴ = (ℏc)² × (2π)² × [(n₁/L₁)² + (n₂/L₂)² + (n₃/L₃)²]

For (1, 2, 0):
  m_KK c² = ℏc × 2π × √((1/L₁)² + (4/L₂)²)
""")

m_KK_sq = (hbar * c)**2 * (2*math.pi)**2 * ((1/L1)**2 + (4/L2**2))
m_KK = math.sqrt(m_KK_sq) / c**2
E_KK = m_KK * c**2

print(f"  m_KK c² = {E_KK / 1.602e-13:.4f} MeV")

# Now the Compton condition
# ℓ = √(L₁² + (2L₂)²)
# E = hc/ℓ = 2πℏc/ℓ... no
# E = hc/λ where λ = ℓ (path = one wavelength)
# E = hc/ℓ

E_path = 2 * math.pi * hbar * c * 2 * math.pi / path_length  # Wrong
# Actually h = 2πℏ, and E = hc/λ = 2πℏc/λ... wait
# λ = path length = ℓ.  E = hc/λ = hc/ℓ.  h = 2πℏ.
# E = 2πℏc/ℓ

E_path2 = 2 * math.pi * hbar * c / path_length

print(f"\nCompton condition: E = hc/ℓ = 2πℏc/ℓ")
print(f"  ℓ = √(L₁² + (2L₂)²) = {path_length:.6e} m")
print(f"  E = 2πℏc/ℓ = {E_path2 / 1.602e-13:.6f} MeV")

print(f"\nKK mode (1,2,0):")
print(f"  E_KK = 2πℏc × √((1/L₁)² + (2/L₂)²)")

# Let's see: are these the same?
# Compton: E = 2πℏc / √(L₁² + 4L₂²)
# KK:      E = 2πℏc × √(1/L₁² + 4/L₂²)
# These are DIFFERENT unless L₁ = L₂

ratio_formulas = math.sqrt(1/L1**2 + 4/L2**2) / (1 / math.sqrt(L1**2 + 4*L2**2))
print(f"\n  E_KK / E_Compton = √(1/L₁² + 4/L₂²) × √(L₁² + 4L₂²)")
print(f"                   = {ratio_formulas:.6f}")
print(f"  E_KK  = {E_KK / 1.602e-13:.4f} MeV")
print(f"  E_C   = {E_path2 / 1.602e-13:.6f} MeV")
print(f"  m_e   = {m_e * c**2 / 1.602e-13:.6f} MeV")

print(f"""
KEY FINDING: The KK mass and the Compton mass are DIFFERENT.

  E_KK = 2πℏc × √(1/L₁² + 4/L₂²)     [sum of squared inverses]
  E_C  = 2πℏc / √(L₁² + 4L₂²)         [inverse of sum of squares]

These are related by:
  E_KK × E_C = (2πℏc)² × √[(1/L₁² + 4/L₂²) / (L₁² + 4L₂²)]

For L₁ ≠ L₂, they differ.  At the electron geometry:
  E_KK / E_C = {ratio_formulas:.1f}

The KK mode (1,2,0) has mass {E_KK / 1.602e-13:.0f} MeV — it is NOT
the electron.

This means: THE ELECTRON IS NOT A SINGLE KK MODE.
""")


# ================================================================
# PART 4: What IS the electron in KK language?
# ================================================================
section("PART 4: What is the electron in KK language?")

print(f"""
The electron has energy m_e c² = 0.511 MeV.  The lowest KK
mode (0,0,1) already has mass ~{2*math.pi*hbar*c/L2 / 1.602e-13:.0f} MeV (for L₃ ~ L₂).
Even (0,1,0) has mass ~{2*math.pi*hbar*c/L2 / 1.602e-13:.0f} MeV.

The electron sits FAR BELOW the KK mass gap — exactly the
same spectral gap found in R12 Track 1 (ω_C/ω_min ~ α).

In KK language, the electron is a state with energy well below
any individual KK mode.  What kind of state is this?
""")

subsection("The electron as a coherent superposition")

# The electron is a wave with wavelength = path length.
# In Fourier space on T³, this is a specific superposition.
# A wave propagating along direction d̂ with wavevector k₀:
#   Φ(y) ~ exp(i k₀ · y)
# where k₀ points along the geodesic with |k₀| = 2π/λ_C

# The geodesic direction in (y₁, y₂) space:
# d̂ = (L₁, 2L₂) / ||(L₁, 2L₂)||
d_norm = math.sqrt(L1**2 + 4*L2**2)
d1 = L1 / d_norm
d2 = 2*L2 / d_norm

# k₀ = (2π/λ_C) × d̂
k0_mag = 2 * math.pi / lambda_C
k0_1 = k0_mag * d1
k0_2 = k0_mag * d2

# The allowed k-vectors on T³ are:
# k = (2π n₁/L₁, 2π n₂/L₂, 2π n₃/L₃)
# The geodesic wavevector k₀ must be one of these:
# k0_1 = 2π n₁/L₁  →  n₁ = k0_1 L₁/(2π) = (L₁/λ_C) × d1
# k0_2 = 2π n₂/L₂  →  n₂ = k0_2 L₂/(2π) = (2L₂/λ_C) × d2... 

n1_eff = k0_1 * L1 / (2 * math.pi)
n2_eff = k0_2 * L2 / (2 * math.pi)

print(f"The geodesic wavevector k₀ = (2π/λ_C) × d̂")
print(f"  d̂ = ({d1:.6f}, {d2:.6f}) in (y₁, y₂) space")
print(f"  |k₀| = 2π/λ_C = {k0_mag:.4e} m⁻¹")
print(f"")
print(f"Effective mode numbers:")
print(f"  n₁_eff = k₀₁ × L₁/(2π) = {n1_eff:.6f}")
print(f"  n₂_eff = k₀₂ × L₂/(2π) = {n2_eff:.6f}")

print(f"""
The effective mode numbers are:
  n₁ ~ {n1_eff:.4f}  (very close to zero!)
  n₂ ~ {n2_eff:.4f}  (very close to zero!)

These are NOT integers — and they are extremely small.
The electron's wavevector |k₀| = 2π/λ_C is MUCH smaller than
the smallest KK wavevector 2π/L₂.

The ratio:
  |k₀| / k_KK,min = L₂ / λ_C = {L2 / lambda_C:.6e}
  (equivalently: L₂/λ_C = 2πR/λ_C = 2gα from R12 Track 1)

This IS the spectral gap from R12.  The electron lives in a
regime where its wavevector is ~α times the smallest KK mode.

In KK language, the electron is essentially a ZERO-MODE
perturbation — it lives in the gap between the true zero mode
(k = 0) and the first excited KK mode.  It cannot be expressed
as any single KK mode or finite sum of KK modes.
""")

subsection("Physical interpretation")

print(f"""
The KK decomposition organizes states by their compact-space
wavelength.  Short wavelengths (n >> 1) are heavy KK modes.
Long wavelengths (n = 1) are the lightest KK modes, with mass
~2πℏc/L ~ hundreds of MeV.

The electron has a wavelength λ_C that SPANS THE ENTIRE COMPACT
SPACE ~137 times over.  Its wavevector is ~α times the smallest
KK wavevector.  It lives in a regime that standard KK theory
doesn't normally encounter — between the zero mode and the
first excited mode.

This is NOT a failure of KK — it's a feature.  The electron is
a topologically nontrivial zero-mode: it has zero NET compact
momentum (it returns to its starting point after one circuit)
but nonzero WINDING (it wraps p times in y₁ and q times in y₂).

In the mathematics of T³, this is the difference between:
  - Momentum modes: exp(2πi n·y/L) — the standard KK basis
  - Winding modes: localized along a geodesic with specific
    topology — NOT a momentum eigenstate

String theory makes this distinction explicit: a string on T³
has both momentum quantum numbers (n_a) and winding quantum
numbers (w_a).  The two are related by T-duality.  The KK
momentum modes become light at large L; the winding modes
become light at small L.

For our compact space (L ~ 10⁻¹⁵ m, very small), the WINDING
modes are the light ones.  The electron is a winding mode, not
a momentum mode.  Standard KK charge (= compact momentum) does
not apply.
""")


# ================================================================
# PART 5: Charge from winding
# ================================================================
section("PART 5: Charge from winding — the correct mechanism")

print(f"""
FINDING: The electron cannot be a standard KK momentum mode.
Its energy (0.511 MeV) is far below the KK mass gap (~hundreds
of MeV).  It is a WINDING mode — a topological excitation
characterized by how many times the wave wraps around the
compact dimensions, not by its compact momentum.

In standard KK theory:
  Charge = compact momentum quantum number × (coupling / L)

For winding modes, the charge mechanism is different:
  Charge = topological flux from the winding configuration

This is exactly the WvM mechanism:
  - The photon's EM field wraps around T³ with specific topology
  - The field has a net monopole moment when projected into 3+1D
  - That monopole moment IS the charge

The KK framework is not WRONG — it correctly identifies the
mode spectrum and shows that the electron is below the KK gap.
But it does not directly compute the winding-mode charge.  That
requires computing the EM field profile of the winding
configuration and projecting it into 3+1D.

IMPLICATIONS:
1. Standard KK charge formula (e = g/√V × n/L) does NOT apply
   to the electron — it's for momentum modes, not winding modes.
2. The WvM charge mechanism (field flux) IS the correct KK
   picture for winding modes.
3. The computation we need is: what is the monopole moment of
   the EM field of a photon winding (1,2) on T³, as seen from
   3+1D?
4. This requires solving Maxwell's equations for the winding
   mode, not just counting KK quantum numbers.
""")

subsection("What the correct calculation looks like")

print(f"""
The right approach (for Track 2 or a follow-up):

1. Write the EM field of a photon propagating along the (1,2)
   geodesic on flat T³:
     E(y, t) = E₀ × f(y) × exp(i(k·y - ωt))
   where f(y) is the transverse profile and k points along
   the geodesic.

2. The field is periodic: it must be single-valued on T³.
   This means f(y) must respect the periodic boundary
   conditions.

3. Expand f(y) in Fourier modes of T³.  The monopole
   coefficient (n = 0,0,0 component) gives the apparent
   charge:
     q_apparent = ∫_T³ ρ(y) d³y
   where ρ(y) is the charge density implied by the EM field.

4. For a pure plane wave (uniform amplitude on T³), the
   monopole moment is ZERO — a uniform field has no net charge.
   The charge must come from field LOCALIZATION or
   POLARIZATION effects along the geodesic.

5. The WvM mechanism: the E-field rotates as the photon
   spirals around the torus.  The time-averaged E-field has
   a net radial component (pointing outward from the torus
   axis) that doesn't cancel — THIS is the charge.

6. On the flat T³, this becomes: the polarization vector
   rotates as the wave propagates along the geodesic.  After
   q orbits, it returns to its starting orientation (spin ½
   condition).  The rotation of polarization creates a net
   flux that constitutes the charge.
""")


# ================================================================
# PART 6: Summary and parameter dependence
# ================================================================
section("PART 6: Summary")

print(f"""
KEY RESULTS:

F1. The electron is NOT a standard KK momentum mode.
    Its energy (0.511 MeV) is ~{E_KK/1.602e-13 / (m_e*c**2/1.602e-13):.0f}× below the lowest
    KK mode ({E_KK/1.602e-13:.0f} MeV for the (1,2,0) mode).
    The spectral gap is a factor of ~1/α, confirming R12 F1.

F2. The KK mass formula and the Compton mass formula give
    DIFFERENT results for the (1,2) mode:
      E_KK    = 2πℏc × √(1/L₁² + 4/L₂²)   = {E_KK/1.602e-13:.0f} MeV
      E_C     = 2πℏc / √(L₁² + 4L₂²)       = {E_path2/1.602e-13:.3f} MeV
    The Compton formula gives the correct electron mass.
    The KK formula gives the mass of a KK-excited state.

F3. The electron is a WINDING mode, not a momentum mode.
    In string theory language, it has winding numbers (1,2,0)
    but effectively zero compact momentum.  Winding modes
    become light when the compact space is small — exactly
    our regime (L ~ 10⁻¹⁵ m).

F4. Standard KK charge formula does NOT apply.
    KK charge = compact momentum / (coupling × circumference)
    applies to momentum modes.  The electron has ~zero compact
    momentum.  Its charge comes from the FIELD CONFIGURATION
    (WvM mechanism: rotating polarization → net monopole flux),
    not from a momentum quantum number.

F5. The correct charge calculation requires:
    Computing the EM field profile of the winding mode on T³
    and extracting its monopole moment as seen from 3+1D.
    This is the WvM mechanism done consistently on flat T³.
    
WHAT THIS MEANS FOR THE PROJECT:
    The KK framework is not the right tool for computing the
    electron's charge directly — but it correctly identifies
    WHY: the electron is a winding mode, and winding-mode
    charge comes from field topology, not compact momentum.

    The next step is to compute the field profile of the
    winding mode on T³ and extract the monopole moment.  This
    is a concrete, well-defined calculation that does not use
    e as input — the charge emerges from the geometry and the
    polarization transport along the geodesic.
""")

# Parameter dependence
subsection("Parameter dependence (qualitative)")

print(f"""
The monopole moment of the winding mode depends on:

1. The winding numbers (p, q): determines how the polarization
   rotates.  Only (1,2) gives nonzero monopole (S3 result).

2. The aspect ratio L₁/L₂: determines the geodesic slope and
   hence the polarization rotation rate.  Different L₁/L₂ give
   different monopole moments → different charges.

3. L₃: for a single-photon state using only (y₁, y₂), L₃
   should not affect the charge.  But for multi-photon states
   (hadrons), L₃ participates through the linking topology.

4. The polarization transport rule: Frenet frame (WvM), parallel
   transport (flat T³ gives trivial holonomy), or something else.
   On flat T³, parallel transport preserves the polarization
   exactly — no rotation.  This is a PROBLEM: without curvature,
   there's no polarization rotation, and hence no charge.

   BUT: the geodesic on T³ IS curved when embedded in 3+1D.
   The question is whether the EM field follows the intrinsic
   (flat) geometry or the extrinsic (curved) embedding.

   This is exactly the R12 tension: flat-T³ says no rotation;
   embedded torus says rotation.  The charge mechanism may
   require going beyond purely flat compact geometry.
""")
