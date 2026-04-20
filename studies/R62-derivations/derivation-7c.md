# Derivation 7c — Spin from 6D Dirac Kaluza–Klein reduction

**Program 1, Track 7 (alternative to 7a and 7b).**  Derive
the spin of each Kaluza–Klein mode of a 6D Dirac spinor
field on M⁴ × T² by standard dimensional reduction.  The
result is that every compact mode, regardless of its
winding numbers (n_t, n_r), reduces to a 4D Dirac spinor —
a spin-½ field — with effective 4D mass given by the
familiar Kaluza–Klein formula

$$
m^2 c^2 \;=\; h^{ab} P_a P_b
$$

(matching F7 and F11 of derivations 3 and 4) and electric
charge given by the tube momentum

$$
Q \;=\; e\,n_t
$$

(matching F14 of derivation 5).  Mass and charge continue
to be set by (n_t, n_r); **spin is not set by (n_t, n_r) —
it is set by the 6D field type**.  Matter modes are spin-½
because the 6D matter field is a Dirac spinor.  Photons,
W/Z bosons, and gravitons are spin-1 or spin-2 because
they are 6D 1-forms or the 6D metric, respectively.  Under
this mechanism MaSt carries no parity rule, no ratio rule,
and no winding-dependent spin selection whatsoever:
every matter mode on every sheet is uniformly spin-½.

---

## A note on competing approaches

Three derivations of spin on T² are in play:

- **7a (metric route).** Asked whether the *metric* of a
  sheared flat 2-torus alone produces spin-½ through
  Killing-vector eigenstates or Levi-Civita holonomy.
  Answer: no — the Killing algebra is abelian u(1)⊕u(1)
  and the Levi-Civita connection is identically zero, so
  neither mechanism can generate a (−1) phase on a 2π
  loop.  Spin-½ fields do live on T² once a spin structure
  is chosen as external input (T² admits four), but the
  metric does not pick one.

- **7b (CP-field-polarization route).** Counts the number
  of rotations of a circularly-polarized electric-field
  vector per ring circuit and obtains the Williamson–van
  der Mark ratio rule s = n_t/n_r.  Under this rule,
  (1,2) → spin ½ and (2,4), (3,6), … all share the same
  spin.  Mode (1,3) has s = ⅓ and is therefore not a
  spin-½ candidate.  The rule treats the photon as a
  classical circulating entity and is a single-particle
  picture.

- **7c (this file — 6D Dirac KK reduction).** Treats the
  matter field as a 6D Dirac spinor and reduces it on T²
  by the standard Kaluza–Klein procedure.  Each compact
  mode inherits 4D spin-½ from the 6D Clifford algebra
  independently of its winding; the winding sets only
  mass and charge.  Mode (1,2) and mode (1,3) are both
  spin-½, because *any* Dirac KK mode is spin-½.  This
  mechanism is fully consistent with the mass and charge
  derivations of F7 and F14.

7b and 7c disagree only on mode (1,3) and on any other
mode where n_t / n_r is not ½.  7b forbids such modes
from being spin-½; 7c permits them.  The project keeps
both alternatives open until an independent discriminator
— experimental, or from a fuller wave-equation treatment,
or from the T⁶ cross-sheet structure — selects between
them.

**GRID-compatibility note** (see §F.4 for the full
discussion).  7a and 7b use only bosonic field content
on T² (scalar/1-form for 7a; CP-polarized photon for 7b)
that is directly realized by GRID's phase field and its
exterior derivatives.  **7c, as written here, posits a 6D
Dirac spinor — a Grassmann field — which is not part of
GRID's axiomatic content (`grid/foundations.md` A1–A6
are purely bosonic).**  The Dirac–Kähler correspondence
on flat T² provides a natural bridge that would realize
7c's spinor as a specific projection of GRID's p-form
phase data, but that bridge is not constructed in this
derivation.  7c should therefore be read as a
mathematically rigorous 6D alternative whose
reconciliation with GRID is an open task — not (yet) as
a derivation *from* GRID.

---

## Attribution

The 6D Dirac KK reduction used here is standard material
in higher-dimensional field theory.  The essential moves
— spinor representation of SO(1, d−1) for d = 6, KK
Fourier decomposition on an internal torus, choice of
spin structure — are covered in:

> T. Kaluza, *Zum Unitätsproblem der Physik*,
> Sitzungsber. Preuss. Akad. Wiss. (1921) 966–972.
> O. Klein, *Quantentheorie und fünfdimensionale
> Relativitätstheorie*, Z. Phys. **37** (1926) 895–906.

> E. Witten, *Search for a realistic Kaluza–Klein theory*,
> Nucl. Phys. **B186** (1981) 412–428, §2–§3 — first
> systematic treatment of KK fermions and the
> chirality / spin-structure issue.

> M. J. Duff, B. E. W. Nilsson, C. N. Pope, *Kaluza–Klein
> supergravity*, Phys. Rep. **130** (1986) 1–142, §2 —
> general framework and toroidal-reduction formulae.

The 6D dimensional arithmetic (8-component Dirac spinor
decomposing as 2 × 4D Dirac under SO(1,3) × SO(2)) is
standard Clifford-algebra accounting.  What is novel here
is not the reduction itself but the **role it plays in
MaSt**: it provides the cleanest available explanation for
the uniformity of spin-½ across every matter sheet (e, ν,
p), while leaving mass and charge to the torus winding
numbers already derived in F7–F14.

---

## Inputs

1. **F7** (derivation-3): a photon on a 2-torus with
   winding numbers (n_t, n_r) has 4D rest mass
   m²c² = h^{ab} P_a P_b.  This derivation will show
   that the *same* mass formula emerges from a 6D Dirac
   spinor with the same compactification — i.e., the
   mass content of F7 is indifferent to whether the 6D
   field is scalar, vector, or spinor.

2. **F11** (derivation-4): the canonical-case mass
   reduction m² c² = (n_t ℏ/R_t)² + (n_r ℏ/R_r)² with
   no shear.  Used as the diagonal limit against which
   the KK–Dirac result will be checked.

3. **F14** (derivation-5): electric charge Q = e n_t
   under the tube-couples convention.  This derivation
   will show that the Dirac KK mode inherits exactly the
   same charge coupling through the same minimal-coupling
   prescription as F14, because minimal coupling is
   uniform across 6D field types.

4. **6D Clifford algebra and Lorentz representation
   theory.**  Specifically: in 6D, the minimal spinor
   representation has 8 complex components, and under
   SO(1,3) × SO(2) ⊂ SO(1,5) it decomposes as
   (4-component 4D Dirac) ⊗ (2-dimensional internal SO(2)
   representation).  After fixing an internal chirality
   projector, each compact KK mode is exactly one 4D
   Dirac spinor.

5. **Standard Kaluza–Klein Fourier decomposition** of a
   field on M⁴ × T² with a chosen spin structure
   (ε_t, ε_r) ∈ {0, 1}².  For fermions, the antiperiodic
   structures are permitted; for matching MaSt's
   observed integer charges, we will take (ε_t, ε_r) =
   (0, 0) throughout, which is the periodic (Ramond–
   Ramond) structure on both cycles.

No new quantum input is introduced.  The only physical
ingredient beyond derivations 1–6 is the assumption that
the 6D field carrying matter modes is a Dirac spinor
rather than a scalar or 1-form.  This is the one new
postulate of 7c, and its only consequence for the prior
derivations is that F7's mass formula and F14's charge
formula continue to hold unchanged, while spin acquires
a definite value (½) that is independent of (n_t, n_r).

---

## Section A — 6D Clifford algebra and spinor representation

### A.1 — Setup

> *Purpose: fix conventions for the 6D Clifford algebra and
> identify how 6D Dirac spinors decompose under the
> 4D Lorentz × internal SO(2) subgroup.*

The 6D spacetime manifold is M⁴ × T² with coordinates
x^A = (x^μ, y^4, y^5), μ ∈ {0, 1, 2, 3}, a ∈ {4, 5}.  The
metric is as in derivation 2 (signature (−, +, +, +, +, +)
in the canonical case):

$$
G_{AB} \;=\; \begin{pmatrix} \eta_{\mu\nu} & 0 \\ 0 & h_{ab} \end{pmatrix},
$$

with h_{ab} the (generally sheared) 2×2 internal metric
from derivations 2–4.  In the canonical (diagonal, no
shear) case, h_{ab} = diag(R_t², R_r²).

Introduce the 6D gamma matrices Γ^A satisfying

$$
\{\Gamma^A, \Gamma^B\} \;=\; 2\, G^{AB}\, \mathbf{1}.
$$

Choose the block decomposition

$$
\Gamma^\mu \;=\; \gamma^\mu \otimes \sigma_3,
\qquad
\Gamma^4 \;=\; \mathbf{1} \otimes i\sigma_1,
\qquad
\Gamma^5 \;=\; \mathbf{1} \otimes i\sigma_2,
$$

where γ^μ are 4×4 4D Dirac gamma matrices and σ_{1,2,3}
are Pauli matrices.  One verifies:

- {Γ^μ, Γ^ν} = 2η^{μν}, from {γ^μ, γ^ν} = 2η^{μν} and
  (σ_3)² = 1.
- {Γ^4, Γ^5} = 0, from {iσ_1, iσ_2} = 0.
- {Γ^μ, Γ^a} = 0, from {σ_3, σ_{1,2}} = 0.
- (Γ^4)² = (iσ_1)² = -1 → G^{44} sign, consistent with
  spacelike compact metric in this mostly-plus signature.

So the 6D Dirac spinor is 4 × 2 = 8-component, split into
two 4-component blocks labeled by the eigenvalue of the
internal chirality operator

$$
\Gamma^{45} \;\equiv\; i\, \Gamma^4 \Gamma^5
\;=\; \mathbf{1} \otimes \sigma_3.
$$

Γ^{45} commutes with all Γ^μ (both σ_3 factors agree) and
anticommutes with Γ^4, Γ^5.  Its eigenvalues are ±1; the
±1 eigenspaces each carry a 4-component 4D Dirac structure.

### A.2 — Decomposition under SO(1,3) × SO(2)

The 6D Lorentz group SO(1, 5) acts on 8-component spinors.
The subgroup SO(1, 3) × SO(2) — where SO(1, 3) acts on x^μ
and SO(2) acts on (y^4, y^5) — is manifest in the block
decomposition above:

- **SO(1, 3)** is generated by Σ^{μν} = (i/4)[Γ^μ, Γ^ν]
  = (i/4)[γ^μ, γ^ν] ⊗ 1 = σ^{μν} ⊗ 1.  This is the
  standard 4D Dirac spinor representation acting on the
  first factor.
- **SO(2)** is generated by Σ^{45} = (i/4)[Γ^4, Γ^5] =
  (1/2) Γ^{45} = (1/2) 1 ⊗ σ_3.  Its eigenvalues on the
  two 4D Dirac blocks are ±1/2.

So an 8-component 6D Dirac spinor Ψ decomposes under
SO(1, 3) × SO(2) as two 4D Dirac spinors, labeled by
internal SO(2) charge ±1/2:

$$
\Psi \;=\; \Psi_+ \oplus \Psi_-,
\qquad
\Gamma^{45}\,\Psi_\pm \;=\; \pm\,\Psi_\pm.
$$

Each Ψ_± is a 4-component 4D Dirac spinor — it
transforms under SO(1, 3) in the standard Dirac
representation.  **This is the key structural fact for
what follows**: every 4D sector of a 6D Dirac spinor is
already, and automatically, a 4D spin-½ field.

---

## Section B — 6D Dirac equation and separation of variables

### B.1 — The 6D Dirac equation

> *Purpose: write the 6D equation of motion and separate
> compact from non-compact coordinates.*

The 6D massless Dirac equation is

$$
i\,\Gamma^A\,\partial_A\,\Psi(x^\mu, y^a) \;=\; 0.
$$

(A 6D mass m_0 can be included without changing any
conclusion; we set m_0 = 0 for minimal structure.  A
nonzero m_0 would contribute a 6D Lorentz-invariant
floor to every KK mass and can be recovered by
restoring it in Section C.)

Split the operator:

$$
i\,\Gamma^\mu\,\partial_\mu\,\Psi
\;+\;
i\,\Gamma^a\,\partial_a\,\Psi
\;=\; 0.
$$

### B.2 — Spin structure and Fourier decomposition

> *Purpose: enumerate the allowed compact-direction
> wavefunctions.*

A spinor field on T² requires a choice of **spin
structure** — a rule for how Ψ transforms when a compact
coordinate y^a is translated by its period L_a = 2πR_a.
T² has four inequivalent ℤ₂ spin structures labeled by
(ε_t, ε_r) ∈ {0, 1}²:

$$
\Psi(y^4 + 2\pi R_t,\, y^5) \;=\; (-1)^{\varepsilon_t}\,\Psi(y^4, y^5),
$$
$$
\Psi(y^4,\, y^5 + 2\pi R_r) \;=\; (-1)^{\varepsilon_r}\,\Psi(y^4, y^5).
$$

For matching MaSt's observed integer charges (F14) and
the F7 mass formula with integer winding labels, we take

$$
(\varepsilon_t, \varepsilon_r) \;=\; (0,\, 0)
$$

throughout — the **periodic (Ramond–Ramond) spin
structure**.  Other choices shift the allowed momenta by
half-units and would correspond to half-integer winding
labels; they are available as additional sectors if the
physical interpretation requires them.

With (0, 0), the compact Fourier expansion is

$$
\Psi(x^\mu, y^a) \;=\; \sum_{n_t, n_r \in \mathbb{Z}}
\psi_{n_t, n_r}(x^\mu)\;
\exp\!\left(i\,\frac{n_t\, y^4}{R_t} + i\,\frac{n_r\, y^5}{R_r}\right),
$$

where each ψ_{n_t, n_r}(x^μ) is an 8-component 4D field.
(In the canonical diagonal case; the non-diagonal
sheared metric generalizes this by replacing the
exponents with the Killing-form combination
exp(i P_a y^a) with P_a the appropriate gauge-covariant
compact momentum.  The derivation proceeds identically.)

### B.3 — Reduced equation for each KK mode

> *Purpose: obtain a 4D equation satisfied by each
> ψ_{n_t, n_r}.*

Substituting into the 6D Dirac equation, each Fourier
mode satisfies

$$
\left[\,i\,\Gamma^\mu\,\partial_\mu
\;-\;\frac{n_t}{R_t}\,\Gamma^4
\;-\;\frac{n_r}{R_r}\,\Gamma^5\,\right]\psi_{n_t, n_r}(x)
\;=\; 0. \tag{B.3.1}
$$

(The compact derivatives i ∂_4 of exp(i n_t y^4/R_t)
produce −(n_t/R_t), and similarly for ∂_5; the factor
of i from the Dirac equation cancels the one from the
derivative, giving the form shown.  Units: P_a ≡ ℏ n_a /
R_a has units of momentum, and the substitution
ℏ = 1 has been made for notational economy; restoring ℏ
replaces (n_a/R_a) with (n_a ℏ/R_a) and gives P_a
explicitly.)

Equation (B.3.1) is the **central equation of 7c.**  It is
a 4D first-order equation of Dirac type, with the compact
momenta (n_t/R_t, n_r/R_r) appearing as mass-like
couplings through the off-block gamma matrices Γ^4, Γ^5.

---

## Section C — Each KK mode is a 4D Dirac spinor of spin ½

### C.1 — The 4D mass and the spin-½ structure

> *Purpose: show that (B.3.1) is equivalent to a standard
> 4D Dirac equation with a well-defined mass, and that
> each mode carries 4D spin ½.*

Square the operator in (B.3.1).  Using
(Γ^μ)² = η^{μμ}, (Γ^4)² = (Γ^5)² = −1 in mostly-plus
signature (G^{aa} > 0, so Γ^a squared with a factor of i
gives −1), and the anticommutators:

$$
\{\Gamma^\mu, \Gamma^4\} = \{\Gamma^\mu, \Gamma^5\} = 0,
\qquad
\{\Gamma^4, \Gamma^5\} = 0,
$$

one obtains (on squaring B.3.1):

$$
\left[\,-\partial^\mu \partial_\mu
\;+\;\frac{n_t^2}{R_t^2}
\;+\;\frac{n_r^2}{R_r^2}\,\right]\psi_{n_t, n_r}(x)
\;=\; 0. \tag{C.1.1}
$$

This is the 4D Klein–Gordon equation for a field of mass

$$
\boxed{\;
m^2 c^2 \;=\; \left(\frac{n_t\,\hbar}{R_t}\right)^2
\;+\; \left(\frac{n_r\,\hbar}{R_r}\right)^2 \;=\; h^{ab}\,P_a\,P_b
\;} \tag{C.1.2}
$$

which is **exactly F7 / F11** — the mass formula already
derived from the photon-on-torus picture for a scalar or
vector field on the same compact geometry.  The KK mass is
indifferent to whether the 6D field is a scalar
(Klein–Gordon), a 1-form (Proca), or a spinor (Dirac):
the compact eigenvalues give the same 4D mass in every
case.

The **spinor character** of each mode is inherited
automatically.  Equation (B.3.1) can be recast as

$$
(i\,\Gamma^\mu \partial_\mu - M_{n_t, n_r})\,\psi_{n_t, n_r}
\;=\; 0,
\qquad
M_{n_t, n_r} \;\equiv\;
\frac{n_t}{R_t}\,\Gamma^4 + \frac{n_r}{R_r}\,\Gamma^5,
$$

and M_{n_t, n_r} is Hermitian and anticommutes with Γ^μ
for all μ (since Γ^4, Γ^5 anticommute with all Γ^μ).
Conjugating ψ by the SO(1, 3) × SO(2) block basis of §A
diagonalizes M into ±m I_{4} on the internal ±1
eigenspaces of Γ^{45}, leaving two independent 4D Dirac
equations

$$
(i\,\gamma^\mu \partial_\mu - m)\,\psi_\pm(x)
\;=\; 0,
\qquad m = \sqrt{h^{ab} P_a P_b},
$$

one for each sign of the internal SO(2) charge.  **Each
ψ_± is a 4D Dirac spinor.**  It therefore transforms in
the (½, 0) ⊕ (0, ½) representation of SO⁺(1, 3) and
carries 4D spin ½.

### C.2 — The spin value is independent of (n_t, n_r)

The 4D spin of ψ_± is determined entirely by its
transformation under SO(1, 3), which is inherited from
the 6D Lorentz transformation properties of Ψ — the
compact indices (n_t, n_r) play no role in the SO(1, 3)
representation.  Explicitly:

- Under a 4D Lorentz transformation Λ ∈ SO⁺(1, 3),
  ψ_{n_t, n_r}(x) → S(Λ) ψ_{n_t, n_r}(Λ^{−1} x), where
  S(Λ) is the standard 4D Dirac representation matrix
  (generated by σ^{μν} = (i/4)[γ^μ, γ^ν]).
- The compact labels (n_t, n_r) are Lorentz scalars
  (they are eigenvalues of translations along compact
  directions, which commute with 4D Lorentz).

Therefore every KK mode — (1, 2), (1, 3), (2, 4),
(3, 6), (0, 0), or any other — is a 4D spin-½ field.

**This is the content of the "always ½ or nothing" rule:**
for a 6D Dirac spinor on T², the KK reduction delivers a
tower of 4D spin-½ fields labeled by (n_t, n_r), with
mass set by F7 and all modes uniformly spin-½.

### C.3 — Why this is not the parity rule or the ratio rule

7c does *not* predict "odd n_t → spin ½, even n_t → spin
0 or 1".  Every mode in the tower is spin-½; even the
(0, 0) mode — a massless 4D spin-½ particle — is
spin-½ under this mechanism (it is either allowed or
forbidden by additional physics such as the Chapline–
Manton mechanism, but if present it is spin-½).

7c does *not* predict "spin = n_t/n_r" either.  The
ratio n_t/n_r is a perfectly good label within the
spectrum — it distinguishes (1, 2) from (1, 3) by their
different masses — but it does not set the spin, which
is uniformly ½.

**The content of 7c is that spin is not a torus quantum
number at all.**  Mass and charge are torus quantum
numbers (F7, F14).  Spin is a field-type label.

---

## Section D — Charge coupling is unchanged

### D.1 — Minimal coupling of the 6D Dirac field

> *Purpose: show that the charge formula F14 carries over
> to the Dirac KK spectrum without modification.*

Include the KK gauge potentials A_μ(x) (descended from
g_{μ4}) and B_μ(x) (from g_{μ5}), as in derivation 2.
The 6D covariant derivative acting on Ψ is

$$
D_A \;=\; \partial_A - i\,A_A^{\text{KK}},
$$

where A_A^{KK} is the Kaluza-derived gauge potential
with A_μ^{KK} = A_μ (tube direction) and
A_μ^{KK} = B_μ (ring direction) under the decomposition
of derivation 2.  Substituting into the 6D Dirac
equation and repeating the Fourier decomposition with
(ε_t, ε_r) = (0, 0), mode ψ_{n_t, n_r} obeys

$$
\left[\,i\,\Gamma^\mu\,(\partial_\mu - i\,n_t\,A_\mu - i\,n_r\,B_\mu)
\;-\;\frac{n_t}{R_t}\,\Gamma^4
\;-\;\frac{n_r}{R_r}\,\Gamma^5\,\right]\psi_{n_t, n_r}
\;=\; 0,
$$

which is the **4D Dirac equation coupled minimally to
two U(1) gauge fields with charges (n_t, n_r)**.

### D.2 — Tube-couples convention (F14)

Under the tube-couples convention of derivation 5 (only
the tube U(1) has an external electromagnetic
interpretation; the ring U(1) is dark), the ring gauge
field B_μ does not appear in the observed low-energy
theory, and the electric charge of ψ_{n_t, n_r} is

$$
\boxed{\;Q \;=\; e\, n_t\;}
$$

(the tube Killing momentum).  This is **exactly F14** —
the Dirac KK mode inherits the same charge as any other
6D field (scalar or vector) with the same compact
momentum.  Minimal coupling does not depend on the
spin structure.

The sign assignments σ_e = −1, σ_ν = 0, σ_p = +1 of F15
extend to the three-sheet T⁶ case by the same
construction and give Q = e(−n_1 + n_5) as in
derivation 5 with the universal convention.

---

## Section E — The full 4D spin spectrum requires multiple 6D fields

### E.1 — Which 4D spins arise from which 6D fields

> *Purpose: map out how the full 4D particle spectrum is
> distributed across 6D field types.*

The 6D Dirac KK reduction of §§A–D produces *only*
spin-½ modes.  The 4D photon (spin 1), gravitons
(spin 2), and scalar Higgs-like fields (spin 0) are
*not* modes of the 6D Dirac spinor.  They come from
*other* 6D fields on the same M⁴ × T² compactification:

| 6D field | 4D content after KK reduction |
|---|---|
| Scalar Φ(x, y) | tower of spin-0 fields, masses from F7 |
| 1-form A_M(x, y) | (0,0) mode massless spin-1 (the physical photon); (n_t, n_r) ≠ (0,0) modes massive spin-1 vectors; compact components A_a give scalars (the U(1) KK gauge fields of F14) |
| Spinor Ψ(x, y) | tower of spin-½ Dirac fields, masses from F7 (this derivation) |
| Metric g_{MN}(x, y) | (0,0) mode 4D graviton (spin 2); compact components give the KK U(1)s and scalars |

The spin-1 result for 1-forms is already derived in
derivation 7a §B–§C (lemma F20 of 7a).  The spin-2
result for the metric is the standard KK graviton.
The spin-0 result for scalars is the Klein–Gordon
content of F7/F11.

### E.2 — MaSt's ontological expansion under 7c

Derivations 1–6 treated the fundamental degree of
freedom on T² as a "photon-on-torus" — a null
trajectory or CP electromagnetic wave.  Under 7c, MaSt
requires a richer field content on M⁴ × T²:

- A **6D Dirac spinor** whose KK modes are the matter
  particles — electron, neutrino, proton — all spin-½.
- A **6D 1-form** whose KK modes are the gauge bosons —
  the photon (massless, uncharged, (0,0)) and any
  massive gauge bosons (from non-trivial winding modes).
- Possibly a **6D metric** for gravity (if MaSt is to
  incorporate it) and **6D scalars** for Higgs-like
  physics.

This is the **field-content expansion cost** of 7c.
MaSt no longer has only "light on a torus"; it has
"light + spinors on a torus" at minimum.  The reward is
that spin-½ for every matter mode falls out
automatically, without parity rules, ratio rules, or
winding-dependent selection.

### E.3 — Relationship to derivations 1–6

Derivations 1 and 2 set up the kinematics of a photon
(null trajectory) on the compactified geometry — these
are statements about the 6D metric and the geodesic
equation in 6D.  They apply identically to a 6D Dirac
spinor, since the geodesic / mass-shell structure is
determined by G_{AB} and is independent of the field's
Lorentz representation.

Derivations 3 and 4 derive the mass formula F7/F11 from
the 6D null condition on the 1-form / Klein–Gordon
sector.  Section C.1 above re-derives the same F7
formula from the 6D Dirac sector.  The two derivations
are consistent and compatible: mass is a property of
the compact eigenvalues, not of the field type.

Derivation 5 derives the charge formula F14 from the
Killing-vector identification of the tube U(1).  Section
D above extends F14 unchanged to the 6D Dirac sector.

Derivation 6 shows that the standing-wave eigenstate
centroid follows the Lorentz force equation in the
eikonal limit.  The argument uses the Klein–Gordon
equation as a representative; the analogous argument for
a Dirac KK mode uses the squared Dirac operator, which
reduces to Klein–Gordon in the eikonal limit and gives
the same result.  So F17 (Lorentz force) extends to the
Dirac sector with no modification.

Under 7c, derivations 1–6 are therefore **unchanged in
content** but reinterpreted: the 4D particle they
describe is a Dirac KK mode rather than a scalar or
vector KK mode.  Its mass is F7, its charge is F14, and
— the new content of 7c — its spin is ½ by Lorentz
covariance of the 6D Clifford algebra.

---

## Section F — Concordance and tensions

### F.1 — What 7c explains cleanly

- **Universal spin-½ across the three matter sheets.**
  e, ν, p are all observed spin-½.  Under 7c, they are
  all KK modes of the same 6D Dirac spinor (with
  different sheet radii and shears setting their
  different masses).  The uniformity of spin-½ across
  sheets is automatic and needs no additional rule.

- **Spin of (1, 2) electron.**  Mode (1, 2) of the 6D
  Dirac spinor is spin-½.  Compatible with observation.

- **Spin of (1, 3) proton (if adopted).**  Mode (1, 3)
  of the 6D Dirac spinor is spin-½.  Compatible with
  observation.  7c places no obstruction on (1, 3) as a
  spin-½ proton, in contrast to 7b where (1, 3) has
  s = ⅓ and must be rejected.

- **Spin of harmonic modes.**  Modes (2, 4), (3, 6), …
  are all spin-½ KK modes of the same 6D spinor.  They
  differ only in mass and possibly in charge structure,
  not in spin.

- **Photon as the (0, 0) mode of a separate field.**
  The 4D photon is not a Dirac KK mode; it is the
  zero mode of the 6D 1-form A_M.  Its spin (1) comes
  from the vector index, not from the compact momentum.
  Derivation 7a §C has this result.

### F.2 — What 7c does not distinguish

7c is *silent* on whether (1, 2), (1, 3), (3, 6), or
some other mode is the correct proton.  All of them are
spin-½ under the Dirac KK mechanism; only their masses
and charges differ.  The proton-mode question must be
resolved on mass and charge grounds, not on spin
grounds.

In particular, 7c does not offer any mechanism by which
some modes are spin-½ and others are spin-1 based on
their winding numbers.  If the project requires such a
distinction — e.g., to forbid certain modes from
appearing in the matter sector — it must come from
additional structure (mode filtering by cross-sheet
shears, charge quantization, or explicit projection),
not from the spin derivation itself.

### F.3 — Tension with the "matter from light" thesis

The single sharpest tension of 7c is conceptual rather
than technical: it expands MaSt's ontology from "one
field (light) on T²" to "multiple fields (including a
Dirac spinor) on T²".  The "matter from light" thesis
of Program 1 is preserved for the kinematic content of
mass, charge, and Lorentz force — all of these emerge
from the torus compactification of a 6D field whose 4D
null trajectory matches what we call "light".  But the
spin-½ character of matter requires the 6D field to be
a spinor, which is not manifestly "light".

This tension is resolvable in at least two ways, neither
worked out in this derivation:

- **Dirac–Kähler reformulation.**  On a flat torus, a
  Dirac spinor can be written as an antisymmetric
  tensor (a sum of p-forms), and the Dirac equation as
  a tensorial equation on differential forms.  Under
  this reformulation, the 6D Dirac spinor is
  equivalent to a set of 6D p-forms (i.e., "light"
  in various polarizations).  The Kähler–Dirac
  equivalence is a classical result (Ivanenko–
  Landau, 1928; Kähler, 1962) and applies cleanly to
  a flat T².  If adopted, MaSt's 6D Dirac sector
  becomes a "higher-rank photon-on-torus", restoring
  the "matter from light" interpretation.

- **Supersymmetric completion.**  A 6D field theory
  with supersymmetry contains both bosonic (1-form,
  metric) and fermionic (Dirac) fields in related
  multiplets.  The "fundamental field" is the
  supermultiplet, and the individual field
  components are different projections of it.  This
  is speculative for MaSt but is the standard path
  in the KK-supergravity literature.

The choice between these (or a third option) is outside
the scope of 7c.  The derivation makes its structural
case independent of that choice: *if* a 6D Dirac
spinor is part of MaSt's field content, its KK modes
are uniformly spin-½, with mass and charge as already
derived in F7 and F14.

### F.4 — Compatibility with GRID

GRID (MaSt's substrate layer, documented in
`grid/foundations.md`) postulates a single U(1) phase
θ(x) ∈ [0, 2π) on each lattice cell (axiom A3), local
U(1) gauge invariance (axiom A4) which produces the
gauge field A_μ on links as a bosonic 1-form, an
information-resolution parameter ζ = 1/4 (axiom A5)
which fixes Newton's constant, and the fine-structure
constant α (axiom A6).  **GRID's field content is
entirely bosonic**: a scalar phase, its differences,
and p-form excitations built from them.  The axioms
introduce no Grassmann (anticommuting) degrees of
freedom and no Clifford-algebra generators.  The
public-facing `papers/matter-from-light.md` reflects
this by deriving spin-½ from bosonic-photon winding
topology (essentially the 7b mechanism) rather than
from a spinor field.

As a matter of literal axiomatic content, therefore,
**7c's 6D Dirac spinor is not present in GRID.**  This
is a structural tension that 7a and 7b do not have,
since both of them use only bosonic field content
(scalar/1-form on T² for 7a, CP-polarized photon on T²
for 7b) that is directly realized by GRID's phase
field and its exterior derivatives.

The tension is not unresolvable.  The **Dirac–Kähler
correspondence** (Ivanenko–Landau 1928; Kähler 1962;
Becher–Joos 1982; underlying the staggered-fermion
construction of Kogut–Susskind 1975 in lattice gauge
theory) states that on a flat manifold — and T² is
flat — a Dirac spinor is exactly equivalent to a
specific projection of a "Kähler field" Φ = φ₀ + φ₁ +
⋯ + φ_d assembled from p-forms of all ranks.  For
d = 6, the 2³ = 8 Dirac components emerge from the
2⁶ = 64 real (32 complex) Kähler-form components as
one of four "flavor copies" selected by a discrete
projection.

This is directly relevant here because GRID's lattice
already supports exactly the p-form content needed:

- 0-forms: the phase θ itself.
- 1-forms: the link connections A_μ (already A4).
- 2-forms: field strengths F_{μν} (already used in
  GRID's Maxwell derivation).
- Higher p-forms: exterior products of the above.

**In principle, the 6D Dirac spinor of 7c is a
particular projection of GRID's existing bosonic
p-form content — no new axiom required.**  The
correspondence is exact on a flat torus; it is the
standard mechanism behind lattice fermions in the
staggered/Kähler formulation and has been rigorously
studied for fifty years.

What has *not* been done in this project:

1. Identify which p-form content of GRID's lattice
   maps to the 6D Kähler field Φ on M⁴ × T².
2. Specify the flavor/chirality projection that
   extracts a single 6D Dirac spinor from the 4-copy
   Kähler multiplet.
3. Verify that this projection is consistent with
   the periodic spin structure (ε_t, ε_r) = (0, 0)
   used in §B.2.
4. Check that the resulting Dirac KK modes carry
   the masses (F7/C.1.2) and charges (F14/D.2)
   derived in §C–§D — not merely by the abstract
   Clifford-algebra argument of this derivation,
   but by explicit lattice-level p-form arithmetic.

Until these four steps are carried out, **7c should
be regarded as a mathematical alternative to 7b that
has not yet been reconciled with GRID's substrate
axioms**.  The reconciliation path (Dirac–Kähler)
exists and is physically natural; the explicit
construction is an open project-level task.

**Comparative compatibility summary:**

| Derivation | Field content | GRID-compatible today? |
|---|---|---|
| 7a | Scalar / 1-form on T² | Yes — directly |
| 7b | Bosonic CP-polarized photon on T² with 1:2-type winding | Yes — directly; matches `papers/matter-from-light.md` §4.2 |
| 7c | 6D Dirac spinor on T² | Not directly; requires Dirac–Kähler bridge (open) |

One reading of this table is that 7b has an
architectural advantage as long as GRID remains the
intended substrate: it plugs in without additional
structure.  Another reading is that the
Dirac–Kähler bridge is worth building anyway, because
if 7c turns out to be the right spin mechanism (via
the discriminators of §G), the bridge is needed
regardless.  The derivation here does not take a
position on which reading is correct; it documents
the gap so that future work on Program 1 can address
it deliberately.

---

## Section G — Discriminator between 7b and 7c

### G.1 — The crux: mode (1, 3)

7b and 7c agree on (1, 2), (2, 4), (3, 6), and every
mode with n_t/n_r = ½.  They disagree on:

- **Mode (1, 3).**  7b: s = ⅓, not a spin-½ particle.
  7c: s = ½, a valid spin-½ candidate for the proton.
- **Mode (2, 1).**  7b: s = 2.  7c: s = ½.
- **Any mode with n_t/n_r ∉ {½, integer, 0}.**  7b:
  non-standard rational spin.  7c: spin-½.

The cleanest experimental or structural discriminator
would be an identification of the proton mode:

- If the proton is (1, 3) and has observed spin ½,
  then 7c is consistent and 7b must be revised.
- If the proton is (1, 2) or (3, 6), both 7b and 7c
  are consistent, and the discrimination must come from
  elsewhere.

### G.2 — Possible future discriminators

- **A cross-sheet T⁶ calculation** that determines the
  neutron mass from cross-sheared modes, fitted under
  both assumptions (ratio rule vs Dirac KK), with the
  better-fitting hypothesis selected by χ².
- **The magnetic moment derivation** (the next open
  derivation in Program 1).  Both 7b and 7c admit a
  magnetic moment, but the moment-to-spin ratio (the
  g-factor) may differ between the two mechanisms,
  providing a quantitative discriminator against the
  observed electron and proton g-factors.
- **A full 6D wave-equation calculation** (Maxwell on
  T² for 7b's photon field; Dirac on T² for 7c's
  spinor field) that checks which one produces a
  self-consistent standing-wave spectrum matching
  MaSt's empirical assignments.

None of these are done in derivation 7.  They are the
natural continuations once the choice between 7b and 7c
is brought to closure.

---

## Lemma (Track 7c result)

We have shown:

> **(F20) Spin from 6D Dirac KK reduction.**  A 6D Dirac
> spinor Ψ on M⁴ × T², reduced by standard
> Kaluza–Klein Fourier decomposition with the periodic
> (0, 0) spin structure, yields a tower of 4D Dirac
> spinors ψ_{n_t, n_r}(x) labeled by winding numbers
> (n_t, n_r) ∈ ℤ × ℤ.  Each ψ_{n_t, n_r} is a
> 4-component 4D field transforming in the Dirac
> representation (½, 0) ⊕ (0, ½) of SO⁺(1, 3).  The
> spin of every KK mode is therefore ½, independent of
> (n_t, n_r).
>
> **(F21) Mass formula for Dirac KK modes.**  Each KK
> mode ψ_{n_t, n_r} satisfies the 4D Dirac equation
> (iγ^μ ∂_μ − m) ψ_{n_t, n_r} = 0 with effective mass
> m² c² = h^{ab} P_a P_b.  This matches F7 / F11
> (derivations 3 and 4) derived from the scalar /
> 1-form sector, confirming that the Kaluza–Klein
> mass formula is independent of 6D field type.
>
> **(F22) Charge formula for Dirac KK modes.**  With
> minimal coupling to the KK gauge potentials descended
> from the off-diagonal metric components, under the
> tube-couples convention of derivation 5, each KK
> mode ψ_{n_t, n_r} has 4D electric charge Q = e n_t.
> This matches F14 and extends to the three-sheet T⁶
> case via Q = e(−n_1 + n_5) with the universal sign
> assignments of F15.
>
> **(F23) Spin as field-type label.**  Under 7c, spin
> is not a torus quantum number: it is an SO(1, 3)
> representation label carried by the 6D field rather
> than by its compact mode.  The full 4D particle
> spectrum therefore requires multiple 6D fields on
> the same M⁴ × T² compactification — a 6D Dirac
> spinor (matter, all spin ½), a 6D 1-form (gauge
> bosons, spin 1 or 0), and as needed a 6D metric
> (graviton, spin 2) and 6D scalars (Higgs-like,
> spin 0).  The torus winding (n_t, n_r) sets mass
> (F21) and charge (F22) for every field type; the
> field type sets spin.
>
> **(F24) GRID-compatibility caveat.**  GRID's axioms
> (foundations.md A1–A6) introduce only bosonic field
> content: a U(1) phase per cell, its link
> connections A_μ, and the p-form excitations built
> from them.  The 6D Dirac spinor posited by F20 is
> not a GRID primitive and requires one of the
> following to be realized:  (a) addition of a
> fermionic axiom to GRID (breaks minimality), or
> (b) a Dirac–Kähler projection from GRID's
> bosonic p-forms to an equivalent spinor — exact on
> a flat torus by the Ivanenko–Landau/Kähler/Becher–
> Joos correspondence and standard in lattice gauge
> theory (staggered / Kogut–Susskind fermions), but
> not explicitly constructed in the MaSt/GRID
> context.  7a and 7b are natively GRID-compatible;
> 7c carries a reconciliation debt that must be
> settled before it can be regarded as a GRID
> derivation rather than a phenomenological 6D
> alternative.

F20–F23 establish the "always spin-½ or nothing" rule
rigorously for the 6D Dirac field on M⁴ × T².  The rule
is mass-formula-preserving and charge-formula-preserving
relative to derivations 3–5, and it is independent of
the winding-dependent rules proposed in 7a (metric) and
7b (CP rotation).  The cost is an expansion of MaSt's
6D field content beyond "light on a torus" to include a
6D Dirac spinor (or, equivalently under the Dirac–Kähler
correspondence, a set of 6D differential forms).  The
reward is a clean and uniform explanation of the
spin-½ character of all matter modes, with mass and
charge continuing to be set by (n_t, n_r).  F24 flags
the GRID-compatibility gap and identifies the
Dirac–Kähler bridge as the natural reconciliation path.
The choice between 7b and 7c is left open for
project-wide resolution; the discriminators laid out
in §G — together with the construction of the
Dirac–Kähler bridge — are the natural places to look
for it.
