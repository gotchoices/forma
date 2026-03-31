# Deriving G from the GRID Lattice

Starting from axioms A1, A2, and A5 of the
[foundations](foundations.md), this document derives Newton's
gravitational constant G and the Einstein field equations,
following the thermodynamic argument of Jacobson (1995).

All work is in natural units (c = ℏ = k_B = 1).

---

## Axioms used

Three of the six GRID axioms enter this derivation:

**A1. Four-dimensional causal lattice.**
Space is a regular array of cells in four dimensions, grain
size L = 1.  Disturbances propagate at c = 1.

**A2. Lorentzian signature (1,3).**
One dimension is timelike (causal ordering, forward only).
Three are spatial.  Metric: η_μν = diag(−1, +1, +1, +1).

**A5. Information resolution ζ = 1/4.**
Each cell contributes ζ bits to the collective information.
A causal horizon of area A carries entropy S = ζA.

**Not used:** A3 (phase), A4 (gauge invariance), A6 (coupling α).
Gravity does not depend on electromagnetism.  The two
derivations (Maxwell and G) are independent.

## What we do NOT assume

We do not assume Einstein's field equations, the Einstein
tensor, the Schwarzschild solution, black holes, or any
gravitational dynamics.  We do not assume the value of G.
These will all emerge.

## Additional inputs beyond the axioms

This derivation uses two results from outside the GRID axioms.
They are flagged here rather than smuggled in:

**The Unruh effect.** An observer accelerating at rate a through
the vacuum perceives thermal radiation at temperature:

<!-- T = a / (2π) -->
$$
T = \frac{a}{2\pi}
$$

This is a theorem of quantum field theory on flat spacetime
(the Bisognano-Wichmann theorem).  It should follow from the
quantized lattice in the continuum limit — our lattice
produces Maxwell (classical EM), and lattice gauge theories
are known to reproduce QFT when quantized.  But we have not
explicitly derived it here from A1–A6.  We take it as
established physics.

**The Raychaudhuri equation.** The expansion θ of a bundle
(congruence) of light rays satisfies:

<!-- dθ/dλ = −(1/2)θ² − σ² − R_ab k^a k^b -->
$$
\frac{d\theta}{d\lambda} = -\frac{1}{2}\theta^2
  - \sigma^2 - R_{ab}\,k^a k^b
$$

where λ is the affine parameter along the rays, σ is the
shear of the congruence, R_ab is the Ricci tensor, and k^a
is the tangent vector to the rays.  This is **not** a field
equation — it is a kinematic identity that holds in any
Lorentzian geometry (A2), before imposing any dynamics.  It
is purely about how the cross-sectional area of a light
beam changes as it propagates through curved spacetime.

---

## The derivation

### Step 1: Local Rindler horizons

From A1 and A2, our lattice has causal structure — light cones,
past, future, and the notion of an accelerating observer.

Any observer accelerating at rate a through the lattice vacuum
sees a **Rindler horizon**: a surface behind them that they can
never receive signals from (analogous to the cosmological
horizon, but local and observer-dependent).

Near any point in spacetime, for a sufficiently short time
interval, the geometry looks flat (this is the equivalence
principle — a consequence of A2's smooth Lorentzian structure).
So every point has a family of local Rindler horizons, one for
each possible acceleration direction.

These horizons are real causal boundaries.  Information on one
side cannot reach the other.

### Step 2: The entropy of a horizon patch

From A5, any causal horizon carries entropy proportional to its
area:

<!-- δS = ζ δA -->
$$
\delta S = \zeta\,\delta A
$$

where δA is the area of a small patch of the horizon.

This is the key physical content of A5: the lattice has a finite
information density, and a causal boundary of area A stores ζA
bits.  The entropy is not a property of what's behind the
horizon — it is a property of the boundary itself, counting the
number of lattice configurations consistent with the macroscopic
state.

### Step 3: Heat flow and the Clausius relation

The **Clausius relation** from thermodynamics states:

<!-- δQ = T δS -->
$$
\delta Q = T\,\delta S
$$

Heat flow (energy crossing the horizon) equals temperature times
entropy change.  This is not a gravitational assumption — it is
basic thermodynamics, applicable to any system with a
temperature and an entropy.

From the Unruh effect, the horizon has temperature T = κ/(2π),
where κ is the surface gravity (the acceleration of the
observer who sees this horizon).

### Step 4: Energy flux through the horizon

Consider a small pencil of light rays (null generators) that
form the horizon.  Let k^a be the tangent vector to these rays
and λ the affine parameter along them.

Near the horizon, the boost Killing vector (the vector field
associated with the accelerating observer's motion) is
ξ^a ≈ κλ k^a, where κ is the surface gravity and λ measures
distance along the generators from the horizon.

The energy flux through the horizon, as seen by the accelerating
observer, is:

<!-- δQ = ∫ T_ab ξ^a dΣ^b = ∫ T_ab k^a k^b κλ dλ dA -->
$$
\delta Q = \int T_{ab}\,\xi^a\,d\Sigma^b
         = \int T_{ab}\,k^a k^b\;\kappa\lambda\;d\lambda\,dA
$$

where T_ab is the stress-energy tensor (the energy and momentum
content of whatever matter is present) and dA is the
cross-sectional area element.

This is the "load" — the matter-energy pushing on the horizon.

### Step 5: Area change from the Raychaudhuri equation

The cross-sectional area of the light-ray bundle changes as it
propagates.  The Raychaudhuri equation (a kinematic identity,
not a field equation) governs this:

<!-- dθ/dλ = −(1/2)θ² − σ² − R_ab k^a k^b -->

For a horizon patch that starts with zero expansion (θ = 0 at
the horizon — the rays are instantaneously parallel), the
leading-order area change is:

<!-- δA = ∫ θ dA dλ, with dθ/dλ ≈ −R_ab k^a k^b -->

Integrating once: θ(λ) ≈ −R_ab k^a k^b × λ.

So the area change is:

<!-- δA = −∫ R_ab k^a k^b λ dλ dA -->
$$
\delta A = -\int R_{ab}\,k^a k^b\;\lambda\;d\lambda\,dA
$$

This is the "response" — how much the horizon area changes due
to the curvature of spacetime.

### Step 6: Combining via Clausius

Now apply δQ = T δS = T ζ δA:

$$
\int T_{ab}\,k^a k^b\;\kappa\lambda\;d\lambda\,dA
\;=\; \frac{\kappa}{2\pi}\;\zeta\;\Bigl(
  -\int R_{ab}\,k^a k^b\;\lambda\;d\lambda\,dA
\Bigr)
$$

The surface gravity κ, the affine parameter integral, and the
area element all cancel (they appear identically on both sides):

<!-- T_ab k^a k^b = −(ζ / 2π) R_ab k^a k^b -->
$$
T_{ab}\,k^a k^b = -\frac{\zeta}{2\pi}\;R_{ab}\,k^a k^b
$$

This must hold for **every** null vector k^a (because we can
construct a local Rindler horizon in any null direction at any
point).  Two tensors that agree on all null vectors must be
equal up to a term proportional to the metric g_ab (since
g_ab k^a k^b = 0 for null k, any multiple of g_ab is
invisible to the null contraction):

<!-- T_ab = −(ζ / 2π) R_ab + f g_ab -->
$$
T_{ab} = -\frac{\zeta}{2\pi}\;R_{ab} + f\,g_{ab}
$$

where f is an undetermined scalar function.

### Step 7: Fixing f from conservation

The stress-energy tensor is conserved (energy-momentum is
neither created nor destroyed):

<!-- ∇^a T_ab = 0 -->
$$
\nabla^a T_{ab} = 0
$$

The contracted Bianchi identity (a geometric theorem, not a
field equation) states:

<!-- ∇^a (R_ab − (1/2) R g_ab) = 0 -->
$$
\nabla^a \bigl(R_{ab} - \tfrac{1}{2}R\,g_{ab}\bigr) = 0
$$

where R = g^{ab}R_{ab} is the Ricci scalar (the trace of the
Ricci tensor — a single number measuring the overall curvature
at a point).

Applying ∇^a to our equation and using both conservation laws:

<!-- 0 = −(ζ/2π) ∇^a R_ab + ∇_b f -->
<!-- 0 = −(ζ/2π)(1/2) ∇_b R + ∇_b f -->

This gives: f = (ζ/(4π)) R + Λ, where Λ is a constant of
integration (the **cosmological constant** — it appears here
for free, not put in by hand).

### Step 8: The Einstein field equations

Substituting f back:

<!-- T_ab = −(ζ/2π) R_ab + (ζ/4π) R g_ab + Λ g_ab -->

Rearranging:

<!-- (ζ/2π)(R_ab − (1/2) R g_ab) + Λ g_ab = −T_ab -->

or:

<!-- R_ab − (1/2) R g_ab + (2πΛ/ζ) g_ab = −(2π/ζ) T_ab -->

Defining the **Einstein tensor** G_ab = R_ab − (1/2) R g_ab:

<!-- G_ab + (2πΛ/ζ) g_ab = (2π/ζ) T_ab -->
$$
\boxed{\;G_{ab} + \Lambda'\,g_{ab} = \frac{2\pi}{\zeta}\;T_{ab}\;}
$$

where Λ' = 2πΛ/ζ absorbs the constants into the cosmological
term.

### Step 9: Reading off G

The standard form of the Einstein equation is:

<!-- G_ab + Λ g_ab = 8πG T_ab -->
$$
G_{ab} + \Lambda\,g_{ab} = 8\pi G\;T_{ab}
$$

Comparing coefficients of T_ab:

<!-- 8πG = 2π/ζ -->
$$
8\pi G = \frac{2\pi}{\zeta}
$$

Therefore:

<!-- G = 1/(4ζ) -->
$$
\boxed{\;G = \frac{1}{4\zeta}\;}
$$

For ζ = 1/4:

$$
G = \frac{1}{4 \times \frac{1}{4}} = 1 \qquad\text{(natural units)}
$$

**Newton's gravitational constant is the inverse of four times
the lattice resolution.**  The stiffer the lattice (more
information per cell, larger ζ), the smaller G and the harder
it is to curve spacetime.

---

## The spacetime stiffness

From G = 1/(4ζ), the spacetime stiffness is:

<!-- c⁴/(8πG) = c⁴ζ/(2π) = ζ/(2π) in natural units -->
$$
\frac{c^4}{8\pi G} = \frac{\zeta}{2\pi}
  = \frac{1}{8\pi} \qquad\text{(natural units, ζ = 1/4)}
$$

In SI units this is approximately 4.8 × 10⁴² newtons — the
"maximum force" scale of general relativity.  The lattice
resolution directly determines how resistant spacetime is to
deformation.

---

## SI restoration

In natural units, G = 1/(4ζ) = 1.  To express this in SI:

The natural unit system sets c = ℏ = k_B = 1 and the grain
size L = 1.  In SI, the grain size is the Planck length
L_P = √(ℏG/c³) ≈ 1.616 × 10⁻³⁵ m.  The Planck length is
defined in terms of G, so the SI value of G cannot be
"predicted" from ζ alone — it also requires knowing the grain
size in meters.

What the derivation establishes is the **relationship**:

<!-- G = ℏc³ / (4ζ k_B × (k_B T_P²)...) -->

Actually, the clean statement in SI is: the Bekenstein-Hawking
entropy in SI units is:

<!-- S = k_B c³ A / (4ℏG) -->
$$
S = \frac{k_B\,c^3}{4\,\hbar\,G}\;A
$$

Our axiom says S = ζ × (number of Planck cells in A) = ζ A/L_P².
Equating:

<!-- ζ / L_P² = k_B c³ / (4ℏG) -->

Since L_P² = ℏG/c³:

<!-- ζ c³ / (ℏG) = k_B c³ / (4ℏG) -->
<!-- ζ = k_B / 4 -->

With k_B = 1 (natural units), ζ = 1/4.  ✓

The SI value G = 6.674 × 10⁻¹¹ m³ kg⁻¹ s⁻² is consistent with
ζ = 1/4 (it must be — the Bekenstein-Hawking formula was
derived assuming GR).  The content of our derivation is not a
new numerical prediction for G, but the demonstration that G
**emerges from entropy** rather than being an independent
fundamental constant.

---

## Summary: what was derived

| Result | Expression | From |
|--------|-----------|------|
| Einstein field equations | G_ab + Λg_ab = (2π/ζ)T_ab | Clausius + Unruh + Raychaudhuri + A5 |
| Newton's constant | G = 1/(4ζ) | Coefficient matching |
| Cosmological constant | Λ appears as integration constant | Conservation law |
| Spacetime stiffness | c⁴/(8πG) = ζ/(2π) | Rearrangement |

---

## What was used — and what was not

| Input | Where it entered | Status |
|-------|------------------|--------|
| A1 (4D lattice) | Spacetime arena, causal structure | Axiom |
| A2 (signature 1,3) | Rindler horizons, null rays, Raychaudhuri | Axiom |
| A5 (ζ = 1/4) | Entropy bound δS = ζ δA | Axiom |
| Unruh effect | Temperature T = κ/(2π) | Established physics (QFT theorem) |
| Raychaudhuri equation | δA from R_ab | Kinematic identity (not a field equation) |
| Clausius relation | δQ = TδS | Basic thermodynamics |
| Contracted Bianchi identity | Fixes f, gives Λ | Geometric identity |
| Energy conservation | ∇^a T_ab = 0 | Physical requirement |

**Not used:** A3 (phase), A4 (gauge invariance), A6 (α).
Gravity is completely independent of electromagnetism in this
derivation.

---

## Honesty check

**Is this circular?**  The Bekenstein-Hawking entropy S = A/(4G)
was originally derived *assuming* GR.  We use the entropy-area
relation (A5) to *derive* GR.  Is that circular?

No — because we are not using the Bekenstein-Hawking formula.
We are postulating a lattice with information density ζ (A5).
The Jacobson argument then shows that any spacetime with this
entropy structure must obey the Einstein equations.  The
Bekenstein-Hawking formula is a *consequence* of this, not an
input.  The logical chain is:

```
Lattice with ζ bits per cell (A5)
    → entropy scales with area (follows from A5)
    → Clausius + Unruh + Raychaudhuri
    → Einstein equations emerge
    → Bekenstein-Hawking formula follows from Einstein + QFT
    → confirms S = ζA (self-consistent)
```

The postulate is the lattice.  GR and Bekenstein-Hawking are
outputs.

**Is the Unruh effect smuggled GR?**  No.  The Unruh effect
is derived in flat spacetime (special relativity + QFT).  It
does not assume Einstein's equations or curved spacetime.  We
use it only on the local Rindler horizon, which is a flat-
spacetime construction (the equivalence principle guarantees
any small patch looks flat).

**Is the Raychaudhuri equation smuggled GR?**  No.  It is a
kinematic identity about null congruences in any Lorentzian
geometry.  It uses the Ricci tensor R_ab, which is defined
purely from the metric (second derivatives of g_ab).  No
field equation is assumed.  The Einstein equation is what
*comes out* — the Raychaudhuri equation is just the geometric
machinery that connects area change to curvature.

**What IS assumed that goes beyond A1–A6?**  The Unruh effect.
It requires quantized fields on the lattice, not just classical
fields.  Our Maxwell derivation is classical.  The implicit
assumption is that the lattice, when quantized, produces
standard QFT — which is the well-established claim of lattice
gauge theory, but we have not derived it explicitly within GRID.
