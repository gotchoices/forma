# KK Charge Comparison — Findings

Study R1. Each section builds on the previous one; every formula
is derived step by step and verified numerically in
[`scripts/verify.py`](scripts/verify.py).

**Prerequisites:** [`primers/kaluza-klein.md`](../../primers/kaluza-klein.md),
[`primers/matrix-primer.md`](../../primers/matrix-primer.md),
[`primers/maxwell-primer.md`](../../primers/maxwell-primer.md).

---

## F1. Starting point: 6D spacetime

We have six coordinates:

    (x⁰, x¹, x², x³, w¹, w²)
     ─────────┬──────────  ──┬──
     4D spacetime (μ,ν)    compact (a,b)

The first four are ordinary spacetime (t, x, y, z). The last two
are compact — periodic with circumferences L₁ and L₂:

    w¹ ~ w¹ + L₁
    w² ~ w² + L₂

This makes the material space a flat torus (S¹ × S¹). "Flat"
means zero intrinsic curvature: straight lines are genuinely
straight. The "donut" shape is just how we visualize it in 3D.


## F2. Extracting 4D: what falls out

The 6D metric is a 6×6 symmetric matrix g_AB. Just as we split
the 5D metric in the KK primer (§7), we split the 6×6 into
blocks based on what they connect:

    ds² = g_μν dx^μ dx^ν      ← spacetime × spacetime
        + γ_ab dw^a dw^b      ← compact × compact
        + 2 g_μa dx^μ dw^a    ← spacetime × compact

where μ,ν ∈ {0,1,2,3} and a,b ∈ {1,2}.

### Block 1: spacetime × spacetime → gravity

g_μν is a 4×4 matrix — the ordinary spacetime metric. This is
general relativity. We already know this block.

### Block 2: material × material → shape of the material sheet

γ_ab is a 2×2 matrix describing the geometry of the compact
space:

    γ = | γ₁₁  γ₁₂ |
        | γ₁₂  γ₂₂ |

For a rectangular torus (perpendicular axes), γ₁₂ = 0:

    γ = | R₁²   0  |
        |  0   R₂² |

where R_a = L_a/(2π) is the compact radius in each direction.
This block gives us scalar fields — the sizes (and possible
angle) of the material dimensions. These are the "moduli" of the material sheet.

### Block 3: spacetime × compact → gauge fields

g_μa is where the new physics lives. There are two compact
dimensions, so there are two sets of cross terms:

    g_μ1  →  A¹_μ   (a 4-vector, one for each spacetime direction)
    g_μ2  →  A²_μ   (a second 4-vector)

In the 5D case, we had one cross term g_μ5 = A_μ, and it turned
out to be the electromagnetic four-potential. Now we have two.

### Counting components

| Block | Size | Components | Physics |
|-------|------|------------|---------|
| g_μν | 4×4 symmetric | 10 | Gravity |
| A¹_μ | 4-vector | 4 | First gauge field |
| A²_μ | 4-vector | 4 | Second gauge field |
| γ₁₁ | scalar | 1 | Size of w¹ |
| γ₂₂ | scalar | 1 | Size of w² |
| γ₁₂ | scalar | 1 | Angle between w¹ and w² |
| **Total** | | **21** | |

Check: a 6×6 symmetric matrix has 6×7/2 = 21 independent
components. ✓

### What this IS

The 6D metric decomposes into:

- **4D gravity** (familiar — general relativity)
- **Two Maxwell-like gauge fields** (each satisfies Maxwell's
  equations, independently)
- **Three scalar fields** (the shape of the material sheet)

The gauge group is **U(1) × U(1)** — two independent
electromagnetic-like symmetries, one for each material dimension.

In the 5D case, one material dimension gave one U(1) = one
electromagnetism. Adding a second material dimension gives a
second, independent copy.


## F3. The KK metric ansatz for the material sheet

The standard way to write the 6D metric (generalizing the 5D
ansatz from the primer, §8) is:

    ds² = g_μν dx^μ dx^ν
        + γ₁₁ (dw¹ + A¹_μ dx^μ)²
        + γ₂₂ (dw² + A²_μ dx^μ)²

(Setting γ₁₂ = 0 for a rectangular torus.)

Expanding the squared terms:

    (dw^a + A^a_μ dx^μ)² = (dw^a)²
                          + 2 A^a_μ dx^μ dw^a
                          + A^a_μ A^a_ν dx^μ dx^ν

The first term is the compact metric (block 2). The second is the
cross terms (block 3). The third is a small correction to the
spacetime metric from gauge field energy.

This is exactly two copies of the 5D ansatz, side by side. Each
material dimension contributes its own gauge field, its own scalar,
and its own cross terms. If you understand the 5D case, you
understand this — it's the same structure, doubled.


## F4. Momentum quantization on the material sheet

Each material dimension is periodic. The same argument as in the
5D case (KK primer §9) applies independently to each:

A wavefunction must be single-valued. Going around w^a and
returning to the same point must give the same ψ:

    ψ(w^a + L_a) = ψ(w^a)

This requires:

    p_a = n_a ℏ / R_a       (n_a = 0, ±1, ±2, ...)

where R_a = L_a/(2π). Two independent quantized momenta — one
for each compact direction.

Each is a conserved quantity (Noether's theorem: translation
symmetry in w^a → conservation of p_a). A particle's momentum in
each compact direction is fixed, quantized, and conserved.


## F5. The charge identification — with gravity

This is where the 5D and 6D cases diverge from each other in an
important way, and where both diverge from WvM.

### Review: 5D charge (from the primer)

In 5D gravitational KK, the identification g_μ5 ∝ A_μ means the
compact momentum p_w maps to electric charge. But there is a
subtlety the primer glossed over: a **coupling constant**.

The off-diagonal metric component g_μ5 and the electromagnetic
potential A_μ don't have the same units. Matching the 5D Einstein
action to the 4D Einstein + Maxwell action (so that the Maxwell
term has the correct normalization) fixes a coupling constant κ:

    g_μ5 = κ A_μ       where  κ = √(4πε₀G) / c

### The charge formula

A particle with compact momentum p_w = nℏ/R follows a 5D
geodesic. When projected to 4D, the geodesic equation produces
an acceleration proportional to κ × p_w × (field strength).
Comparing with the Lorentz force a ∝ q × (field strength):

    q = κ × p_w = √(4πε₀G)/c × nℏ/R

    q_KK = n × ℏ√(4πε₀G) / (cR)            ... (KK charge, SI)

Equivalently, using the Planck charge q_P = √(4πε₀ℏc):

    q_KK = n × q_P × l_P / R               ... (KK charge, Planck units)

where l_P = √(ℏG/c³) is the Planck length.

### What compact radius gives q = e?

Setting q_KK = e with n = 1:

    e = q_P × l_P / R

    R_KK = q_P × l_P / e = l_P / √α

Since e = √α × q_P (the definition of the fine-structure
constant α = e²/(4πε₀ℏc) = (e/q_P)²):

    R_KK = l_P / √α

Numerically (see verify.py):

    l_P  = 1.616 × 10⁻³⁵ m
    √α   = 0.08542
    R_KK = 1.891 × 10⁻³⁴ m   ← about 12 Planck lengths

This is the **Planck scale** — twenty orders of magnitude
smaller than a proton.


## F6. The 6D charge: two independent charges

Extending F5 to the 6D case with two material dimensions, each
has its own gauge field and its own charge:

    q₁ = κ × p₁       from momentum in w¹
    q₂ = κ × p₂       from momentum in w²

For a rectangular material sheet where both dimensions couple to gravity
symmetrically, κ₁ = κ₂ = κ, and:

    q₁ = n₁ × ℏ√(4πε₀G) / (cR₁)
    q₂ = n₂ × ℏ√(4πε₀G) / (cR₂)

### For the (1,2) geodesic

The electron in the WvM/material-sheet picture follows a (1,2) torus knot:
it winds n₁ = 2 times around w¹ per n₂ = 1 time around w².

This gives TWO charges:

    q₁ = 2 ℏ√(4πε₀G) / (cR₁)
    q₂ = 1 × ℏ√(4πε₀G) / (cR₂)

These are charges under two different gauge symmetries — U(1)₁
and U(1)₂. The electron has only one electric charge, so we must
ask: how do two charges become one?

Three possibilities:

1. **Only one couples to our electromagnetism.** Perhaps one U(1)
   is electromagnetism and the other is something else (hidden,
   broken, or confined). Then the observed charge is just q₁ or q₂.

2. **Diagonal combination.** The physical electromagnetic U(1)
   could be a specific linear combination of the two, like
   q_EM = (q₁ + q₂)/√2 or q_EM = q₁ cos θ + q₂ sin θ for some
   mixing angle θ.

3. **The charges are not independent.** The geodesic constraint
   (fixed path on a material sheet) might force a relationship between R₁ and
   R₂ that makes q₁ and q₂ proportional.

We'll return to this in F9 after comparing to WvM.


## F7. The WvM charge formula — no gravity

WvM derives charge from a completely different mechanism. No
material dimensions, no momentum quantization, no gravitational
constant G.

### The derivation (from WvM paper §3)

1. Confine a photon of wavelength λ to a spherical cavity of
   diameter λ.

2. The photon's energy is U = hc/λ. Uniformly distributed in the
   cavity volume V = πλ³/6, the energy density is:

       u = U/V = 6hc / (πλ⁴)

3. The energy density of an electromagnetic field is u = ε₀E².
   So the average E-field magnitude inside is:

       ⟨E⟩ = √(u/ε₀) = √(6hc / (πε₀λ⁴))

4. At the mean energy transport radius r = λ/(4π), compare this
   to the Coulomb field of a point charge E = q/(4πε₀r²):

       q/(4πε₀r²) = ⟨E⟩

5. Solve for q:

       q = 4πε₀r² × ⟨E⟩
         = 4πε₀ × (λ/(4π))² × √(6hc/(πε₀λ⁴))
         = (ε₀λ²/(4π)) × √(6hc/(πε₀λ⁴))
         = (1/(4π)) × √(ε₀²λ⁴ × 6hc/(πε₀λ⁴))
         = (1/(4π)) × √(6ε₀hc/π)
         = (1/(4π)) × √(6 × 2πε₀ℏc/π)
         = (1/(4π)) × √(12ε₀ℏc)
         = √(12ε₀ℏc) / (4π)
         = √(12ε₀ℏc/(16π²))
         = √(3ε₀ℏc/(4π²))

   Or equivalently:

       q_WvM = (1/(2π)) × √(3ε₀ℏc)         ... (WvM charge)

### The key feature

**The charge is independent of λ.** The λ cancels — any photon
wavelength (any mass) gives the same charge. This is why WvM
claim charge is topological: it depends on the field geometry
(the confinement topology), not on the photon's energy.

### Numerical value

    q_WvM = (1/(2π)) × √(3 × 8.854 × 10⁻¹² × 1.055 × 10⁻³⁴ × 2.998 × 10⁸)
          = (1/(2π)) × √(2.814 × 10⁻³⁷ × 2.998 × 10⁸)
          = (1/(2π)) × √(8.437 × 10⁻²⁹)     ... (see verify.py)

    q_WvM ≈ 1.461 × 10⁻¹⁹ C
    e     = 1.602 × 10⁻¹⁹ C
    q_WvM / e ≈ 0.912

The ~9% deficit comes from WvM's uniform-field-in-a-sphere
approximation. **This was resolved in S2 (S2-toroid-geometry):**
replacing the sphere with a degenerate torus of aspect ratio
a/R = 1/√(πα) ≈ 6.60 gives q = e exactly. The photon orbits at
R = λ_C/(4π) but its field extends outward to ~0.6λ, filling a
nearly spherical volume (the "rotation horizon"). The ratio
a/R = 1/√(πα) is an exact algebraic result, not a numerical fit.

So the WvM charge mechanism already produces q = e with the
correct geometry. The question is not "can WvM get the right
charge?" — it can. The question is whether a/R = 1/√(πα) can be
derived from first principles rather than demanded.


## F8. Structural comparison

### Both charges in terms of the Planck charge

The Planck charge q_P = √(4πε₀ℏc) is the natural unit of charge
in any theory built from ℏ, c, and ε₀:

    q_P = √(4πε₀ℏc) = 1.876 × 10⁻¹⁸ C

Both formulas produce charges as fractions of q_P:

    e     = √α × q_P                           = 0.0854 × q_P
    q_WvM = √(3/(16π³)) × q_P                  = 0.0778 × q_P
    q_KK  = (l_P / R) × q_P                    = (depends on R)

### What determines the prefactor?

| Formula | Prefactor of q_P | What sets it |
|---------|------------------|--------------|
| e (observed) | √α = 0.0854 | Nature |
| q_WvM (sphere) | √(3/(16π³)) = 0.0778 | Uniform sphere approximation |
| q_WvM (a/R = 1/√(πα)) | √α = 0.0854 | Degenerate torus with correct aspect ratio (S2) |
| q_KK | l_P / R | Compact radius R (set by gravity + periodicity) |

The un-corrected WvM prefactor (0.0778) is close to √α but not
equal. S2 showed that the exact geometry a/R = 1/√(πα) produces
exactly √α — i.e., q = e.

The KK prefactor depends on the compact radius R, which involves
the gravitational constant G (through l_P = √(ℏG/c³)). Setting
q_KK = e forces R = l_P/√α.

### The crucial difference

**WvM's charge formula contains no G.** It is purely
electromagnetic: ε₀, ℏ, c, and geometry. And with the correct
geometry (a/R = 1/√(πα), from S2), it gives q = e exactly.

**KK's charge formula requires G.** The gravitational constant
enters through the coupling κ that converts compact momentum to
charge. Without G, there is no way to determine the unit of
charge from the compact geometry alone.

This means:

1. **WvM is not standard gravitational KK.** The charge
   mechanisms are fundamentally different — one is electromagnetic
   (field topology), the other is gravitational (compact momentum).

2. **The size scales are different.** KK gives R ~ 10⁻³⁴ m
   (Planck). WvM gives structures at ~ 10⁻¹³ m (Compton). These
   differ by a factor of ~ 10²¹.

3. **The charge question is already resolved.** S2 showed that
   q = e for a/R = 1/√(πα). The open question is not "which
   formula gives the right charge" but "can a/R = 1/√(πα) be
   derived from first principles?"


## F9. What the compact topology DOES provide

Although the charge mechanisms differ, the material sheet topology is
still valuable. It provides three things that WvM needs but
cannot explain on its own:

### 1. Confinement without a force

WvM's biggest open problem: what confines the photon? On a material sheet, no
confinement is needed. The photon follows a geodesic (straightest
possible path) on a material space. The path is closed because the
space is compact, not because a force bends it.

### 2. Spin from topology

The (1,2) geodesic on a material sheet winds twice before returning. This
gives spin ½ by the same argument WvM uses (double traversal →
ωs = 2ω → L = ℏ/2). The topology of the path determines the
spin, and the material sheet provides the two wrapping directions needed for
non-trivial topology.

### 3. Mass from wavelength quantization

On a material sheet, the photon must fit an integer number of wavelengths
around the closed geodesic. The path length for a (1,2) geodesic
on a rectangular material sheet is:

    L_path = √((n₁L₁)² + (n₂L₂)²) = √(4L₁² + L₂²)

Setting L_path = λ_C (one Compton wavelength) gives the photon
energy E = hc/λ_C = m_e c². The mass is determined by the
compact geometry.

### Charge: from field profile, not compact momentum

The material sheet topology does not determine the charge through the KK
momentum mechanism (which requires gravity and produces Planck-
scale structures). Instead, the charge comes from the photon's
electromagnetic field profile on the geodesic — the WvM mechanism.

S2 showed this works: with a/R = 1/√(πα), the WvM mechanism
gives q = e exactly. S3 showed that only the (1,2) knot produces
nonzero charge (all other knots cancel by symmetry). Together,
these establish that the charge is determined by the combination
of topology (which knot) and geometry (the field extent a/R).


## F10. The material sheet parameter space

The (1,2) geodesic constraint gives one equation:

    √(4L₁² + L₂²) = λ_C                    ... (path length)

This leaves one free parameter. Parameterize by the ratio
r = L₂/L₁:

    L₁ = λ_C / √(4 + r²)
    L₂ = r × L₁
    R₁ = L₁/(2π)
    R₂ = L₂/(2π)

For each ratio r, verify.py computes the KK gravitational charges
q₁ and q₂, the WvM charge, and the Compton-scale geometry.

### Key observations (from verify.py)

1. **KK charges are tiny for any r.** Because R₁ and R₂ are of
   order λ_C/(2π) ~ 10⁻¹³ m, and the KK charge goes as l_P/R,
   the KK charges are:

       q₁/e ~ l_P/R₁ ~ 10⁻³⁵/10⁻¹³ = 10⁻²²

   Twenty-two orders of magnitude too small. The KK gravitational
   charge mechanism does not work at the Compton scale.

2. **WvM charge depends on field extent, not material sheet dimensions.**
   The un-corrected WvM formula gives q ≈ 0.91e regardless of
   the material sheet geometry. But S2 showed that the corrected charge
   (using the actual field extent a/R = 1/√(πα) instead of a
   uniform sphere) gives q = e exactly. The field extent "a" is
   not one of the material sheet parameters (L₁, L₂) — it describes how far
   the photon's field reaches into the non-material dimensions.

3. **The free parameter r determines the shape.** Different r
   values give different L₁/L₂ ratios — different aspect ratios
   of the material space. This free parameter might be constrained
   by the magnetic moment, g-factor, or a self-consistency
   condition.


## F11. Addressing the propositions

### P1. Are WvM and KK charge algebraically equivalent?

**No.** They are structurally different:

    q_KK  = n × q_P × l_P / R      (involves G through l_P)
    q_WvM = √(3/(16π³)) × q_P      (involves ε₀, ℏ, c — no G)

The KK charge depends on the compact radius R and the
gravitational constant G. The WvM charge depends on the cavity
field geometry and electromagnetic constants. They happen to be
numerically close (both are ~0.08 × q_P) because both involve
simple powers of π, but they are different formulas reflecting
different physics.

### P2. Does material sheet momentum give q ≈ e?

**Not at the Compton scale.** For material dimensions of order
λ_C, the gravitational KK charges are ~10⁻²² × e. Only at
R ~ l_P/√α ≈ 10⁻³⁴ m would the KK mechanism give charges of
order e.

### P3. Single effective charge from two U(1)s?

**Not relevant for the gravitational mechanism** (charges are too
small). For the WvM mechanism, the charge is already single
(it comes from the total E-field profile, not from compact
momenta). The two U(1) gauge symmetries of the material sheet might play a role
in a deeper theory, but they don't determine the electron's
charge.

### P4. Unification of α

The relationship a/R = 1/√(πα) from S2 equates a geometric
ratio to the fine-structure constant. In the KK framework,
α = (l_P/R_KK)². These are different relationships between
different quantities at vastly different scales:

- S2: a/R involves the field extent and orbital radius (~10⁻¹³ m)
- KK: R_KK is the material dimension radius (~10⁻³⁴ m)

They don't unify. However, both express α as a geometric ratio,
which suggests α might have a geometric origin. The S2 result is
more directly useful: if a/R = 1/√(πα) can be derived from a
physical principle (boundary matching, energy minimization, or
self-consistent confinement), that would amount to deriving α
from geometry — a major result independent of KK.


## F12. Conclusions

### The main finding

**The KK gravitational charge mechanism does not apply at the
WvM scale.** KK derives charge from gravitational coupling to
compact momentum, giving charges of order 10⁻²² × e at the
Compton scale. The WvM charge mechanism — electromagnetic field
topology — is a different kind of physics that operates at a
different scale and does not involve G.

### What was already known (from S1–S3)

This study should have started from the established results:

| Property | Status | Source |
|----------|--------|--------|
| Spin ½ | Exact (topological) | WvM; confirmed S3 |
| q = e | Exact (algebraic) | S2: a/R = 1/√(πα) |
| Mass | From path length = λ_C | WvM |
| g ≈ 2.002 | Near-exact | WvM (depends on charge) |
| Only (1,2) has charge | Demonstrated | S3 (symmetry cancellation) |
| Confinement | Geodesic on material space | Material dimension hypothesis |

The charge question was resolved by S2. The 9% deficit is an
artifact of WvM's uniform-sphere approximation; the correct
geometry (degenerate torus with a/R = 1/√(πα)) gives q = e.

### What this study adds

1. **6D metric decomposition (F1–F3).** Two material dimensions
   give gravity + two gauge fields + three scalars. The gauge
   group is U(1) × U(1). This is useful structural knowledge.

2. **KK charge is ruled out at Compton scale (F5–F6).** The
   gravitational coupling produces charges ~10⁻²² × e for
   compact radii of order λ_C. This definitively separates the
   WvM and KK charge mechanisms.

3. **The compact topology is still useful (F9).** Even without
   the KK charge mechanism, material dimensions provide
   confinement (geodesic, no force), spin (double winding), and
   mass quantization (wavelength fitting).

### What remains open

The central open question is not about charge (S2 solved that)
but about **deriving the geometry from first principles:**

1. **Can a/R = 1/√(πα) be derived independently?** S2 obtained
   this by demanding q = e. An independent derivation (boundary
   matching, energy minimization, self-consistent confinement)
   would amount to deriving α from geometry.

2. **What determines the material dimensions L₁, L₂?** The path
   length constraint (√(4L₁² + L₂²) = λ_C) leaves one free
   parameter. What fixes it?

3. **What is "a" in the material-dimension picture?** S2's "a" is
   the field extent — how far the photon's field reaches into
   non-material space. In a material-dimension framework, this
   should emerge from the field equations, not be put in by hand.

4. **Do all constraints (q, m, spin, g) determine a unique
   geometry?** This is the goal of the next study.

---

*Numerical verification of all formulas: [`scripts/verify.py`](scripts/verify.py)*
