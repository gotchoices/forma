# Derivation 9 — Klein quantization at non-Planck scales

**Program 1, Track 9.**  A reader familiar with
traditional Kaluza–Klein (KK) theory will notice an
apparent tension with Tracks 1–8: traditional KK
produces states at the Planck mass (~10¹⁹ GeV), while
MaSt's derivations give electrons (~10⁻³ GeV), muons,
nucleons, and so on.  The compact radius R used in
Tracks 1–8 is evidently not at the Planck scale.  This
derivation does two things:

1. **Document the scale-invariance of the KK mass
   formula.**  Show explicitly that none of Tracks 1–8
   uses the value of R or its ratio to ℓ_Planck.  Klein
   quantization is a *local* condition — it depends
   only on the compact topology, the metric, and the
   standing-wave boundary condition, and works for
   **any** positive R.  The mass formula F7 / F11 /
   F25 scales as m ∝ 1/R for fixed winding numbers
   and fixed internal-metric shape.

2. **Document the hierarchy question as an inherited
   open issue, not a derivation bug.**  The fact that
   R ~ 10²² ℓ_Planck in MaSt's phenomenological fits
   is not explained by Tracks 1–8 nor by this
   derivation.  It is an empirical input, analogous to
   the choice of the compactification manifold in
   string theory: the derivation machinery works on any
   scale, and the scale is fixed by the physics being
   modeled.

The outcome is not a new theorem.  It is a clean
statement of what the KK-on-torus derivations do and
do not claim about the compact scale, together with a
UV consistency check showing that treating the compact
tori as a low-energy effective theory (with GRID
providing the Planck-scale UV completion) is
internally consistent.

---

## Inputs

1. **F7** (derivation 3) — the single-torus mass
   formula m² c² = h^{ab} p_a p_b with a, b ∈ {4, 5}.

2. **F11** (derivation 4) — MaSt's parametrization
   h_{ab} = R² [[ε², εs], [εs, 1]] giving
   μ² = (n_t/ε)² + (n_r − s n_t)² with mass
   normalization m_c = ℏ/(Rc).

3. **F25** (derivation 8) — the two-torus mass formula
   m² c² = h^{ab} p_a p_b on the 4×4 internal metric.

4. **Planck-Einstein quantization**, p_a = n_a ℏ / R_a
   with n_a ∈ ℤ, as established in derivations 2–3.

5. **GRID's natural scale** (grid/foundations.md):  the
   underlying GRID lattice has spacing ~ ℓ_Planck, and
   all physics below Planck energy is treated as an
   effective field theory on this lattice.  MaSt's
   compact tori are emergent structures at a scale that
   GRID does not pin down.

No new quantum input is introduced in this track.
Everything here follows from restating and analyzing
what is already in Tracks 1–8.

---

## Section A — Klein quantization and the role of R

### A.1 — The standing-wave condition on a compact circle

> *Purpose: make the role of R in the mass formula
> completely explicit.*

On a compact direction y with period L = 2π R, a
single-valued wave function ψ(y) must satisfy

$$
\psi(y + L) \;=\; \psi(y). \tag{A.1.1}
$$

For a plane-wave ansatz ψ(y) = e^{i k y}, this forces
k L = 2π n with n ∈ ℤ, hence

$$
k \;=\; \frac{n}{R},
\qquad
p \;=\; \hbar k \;=\; \frac{n\,\hbar}{R},
\qquad
n \in \mathbb{Z}. \tag{A.1.2}
$$

The compact momentum p is **inversely proportional to
R**.  This is the only place in the Tracks 1–8
derivations where R enters:  once p = n ℏ/R is
substituted into the mass formula, R appears in the
overall scale of m, but nowhere in its shape
(relative sizes of modes, mode mixing, Lorentz
structure, etc.).

### A.2 — The single-torus mass formula scales as 1/R²

The single-torus mass formula F7 reads

$$
m^2 c^2 \;=\; h^{ab}\,p_a\,p_b,
\qquad a, b \in \{4, 5\}. \tag{A.2.1}
$$

With the F11 parametrization h_{ab} = R² Γ_{ab}
(where Γ_{ab} is the *shape* matrix with det Γ = ε²
and one off-diagonal entry εs), the inverse satisfies
h^{ab} = Γ^{ab} / R².  Substituting p_a = n_a ℏ / R
(for simplicity taking both compact directions of
equal circumference R; the F11 formula handles the
anisotropic case via ε):

$$
m^2 c^2 \;=\; \frac{\hbar^2}{R^4}\,\Gamma^{ab}\,n_a\,n_b. \tag{A.2.2}
$$

Divide both sides by (ℏ/(Rc))² c² = ℏ² c² / (R² c²) =
ℏ²/R² to introduce the **Compton mass scale**

$$
m_c \;\equiv\; \frac{\hbar}{R\,c}, \tag{A.2.3}
$$

giving

$$
\frac{m^2}{m_c^2} \;=\; \Gamma^{ab}\,n_a\,n_b
\;\equiv\; \mu^2(n_4, n_5), \tag{A.2.4}
$$

the **dimensionless mass formula** μ² whose shape
depends only on the integers n_a and on the
dimensionless parameters (ε, s) of F11.  **The scale R
has been completely factored out** — it enters only
through the prefactor m_c.

This is the precise statement of scale-invariance:
for fixed shape (ε, s) and fixed winding pattern
(n_4, n_5), changing R rescales all masses uniformly
without changing their ratios.  The physical content
of the KK-on-torus derivation — which particles exist,
their mass ratios, their charges, their mixing
structure — is entirely **R-independent**.

### A.3 — The multi-torus formula is also 1/R²

For two 2-tori (Track 8, F25), the same algebra
generalizes.  If we scale both sheets uniformly
(R_A = R_B = R) and hold the shape matrices H_A /R²,
H_B /R², C /R² fixed, then

$$
m^2 c^2 \;=\; \frac{\hbar^2}{R^4}\,(\text{shape}^{ab})\,n_a\,n_b, \tag{A.3.1}
$$

giving the same m ∝ 1/R scaling.  When the two sheets
have different radii, there are *two* scales (m_c^A
and m_c^B), and the mass spectrum depends on their
ratio plus the dimensionless cross-shear; but again,
the *overall* scale is a free parameter, and only
*ratios* are fixed by the dimensionless structure.

### A.4 — Summary: R is a free parameter

Every derivation in Tracks 1–8 uses:

1. **Compact topology** (periodicity along y^a).  This
   is a *statement about identification*, not about
   size.
2. **Metric shape** (the ratio matrix h_{ab} / R²).
   This is a dimensionless quantity.
3. **Standing-wave quantization** p = n ℏ / R.  This
   is the same condition for any R.
4. **4D Minkowski structure** (the non-compact part of
   the 8D metric).  This is independent of R.

None of these inputs requires R to take any specific
value.  R is a free parameter set by whatever physics
produces the compact tori in the first place.  The
mass formula works for any R > 0.

---

## Section B — Why traditional KK uses Planck-scale R

> *Purpose: explain the historical association between
> KK and the Planck scale, and show why MaSt does not
> inherit this association.*

### B.1 — Kaluza–Klein's original setting

Kaluza (1921) and Klein (1926) formulated their
unification in the context of *pure gravity plus
electromagnetism*.  The action was the 5D Einstein–
Hilbert action

$$
S_{\text{KK}} \;=\; \frac{c^3}{16\pi G_5}\int d^5x\,\sqrt{-G}\,R_{(5)}, \tag{B.1.1}
$$

where G_5 is the 5D Newton constant and R_{(5)} the 5D
Ricci scalar.  After compactification on a circle of
radius R, the 4D effective theory is 4D gravity + 4D
electromagnetism + a scalar (the radion).  The 4D
Newton constant is related to G_5 by G_N = G_5 / (2π R).

The only dimensional input in (B.1.1) is G_5 itself.
For the 4D theory to reproduce the observed
gravitational strength, G_5 = 2π R G_N must come out
right.  Klein's argument (and subsequent standard KK)
takes R to be **set by G_N**, giving R of order the
Planck length ℓ_Planck ≈ 10⁻³⁵ m.  Consequently, the
KK mass tower begins at m_1 = ℏ / (R c) ≈ M_Planck ≈
10¹⁹ GeV — far above any observed matter scale.

### B.2 — Why MaSt does not inherit this

MaSt is *not* pure gravity.  It is a *bosonic phase
theory on the GRID lattice* (grid/foundations.md).
The KK-on-torus construction of Tracks 1–8 treats the
compact tori as a given geometric structure — they are
not dynamical solutions of 8D Einstein equations, and
G_5 plays no role in the derivations.

Concretely, nothing in Tracks 1–8:

- uses Einstein's 5D or 8D field equations,
- uses Newton's constant G_N or G_5,
- uses the relation between the compact radius and 4D
  gravity.

What is used is:

- the 8D metric (as a *given* background),
- Killing vectors and standing-wave quantization,
- the null-trajectory condition (massless KG operator)
  on the fixed background.

This is a **background-field treatment**.  The compact
scale R is whatever sets the ground-state scale of the
tori as given, **not** whatever would make them
solutions of 8D gravity.  No connection to ℓ_Planck is
forced.

### B.3 — Historical parallels

This decoupling of "the KK mass formula" from "the
Planck scale" is not new.  It is the standard move in
several post-Kaluza literatures:

- **String-theoretic compactifications** (1980s
  onward):  the string scale M_s can be ≪ M_Planck if
  the compactification volume is large; the KK mass
  formula works identically, just at a lower scale.
- **Large extra dimensions** (Arkani-Hamed, Dimopoulos,
  Dvali 1998):  extra dimensions as large as mm-scale,
  with KK modes at meV masses.  The KK mass formula is
  the same as Klein's; only R changes.
- **Warped extra dimensions** (Randall–Sundrum 1999):
  a warp factor redshifts the effective KK scale well
  below M_Planck.
- **Lattice / condensed-matter compactifications**:
  any effective theory on a small torus in a larger
  manifold — the KK formula is the mode quantization
  on that torus, with no intrinsic Planck dependence.

MaSt's treatment sits in this tradition:  the KK mass
formula is used as a geometric mode-quantization tool
with a free scale parameter.

---

## Section C — UV consistency: KK modes versus the Planck cutoff

> *Purpose: verify that treating Tracks 1–8 as an
> effective field theory below a Planck-scale UV cutoff
> is internally consistent.*

### C.1 — The EFT hierarchy

Let R be the compact radius and ℓ_Planck the GRID
lattice spacing.  Define the **hierarchy ratio**

$$
\mathcal{N} \;\equiv\; \frac{R}{\ell_{\text{Planck}}}. \tag{C.1.1}
$$

The KK mode of winding n has mass m_n ≈ n ℏ/(Rc) = n
m_c, where m_c = ℏ/(Rc) is the Compton mass scale of
(A.2.3).  The UV validity of the KK treatment requires
m_n ≪ M_Planck, i.e.

$$
n\,m_c \;\ll\; M_{\text{Planck}}
\;=\; \frac{\hbar}{\ell_{\text{Planck}} c}
\;=\; m_c \cdot \mathcal{N}. \tag{C.1.2}
$$

This gives the validity window

$$
n \;\ll\; \mathcal{N}. \tag{C.1.3}
$$

The KK tower is a reliable EFT description for winding
numbers up to ~𝒩 modes; above that, UV physics
(whatever GRID's Planck-scale dynamics is) takes over
and the KK picture must be re-examined.

### C.2 — MaSt's empirical hierarchy

The electron mass is m_e ≈ 0.511 MeV/c².  If the
electron is the (1, n_r) compact mode of a single
torus, then m_c ~ m_e / (some O(1) factor depending on
winding pattern and shape).  Taking the ground-state
estimate m_c ~ m_e gives the compact radius

$$
R_e \;\sim\; \frac{\hbar}{m_e\,c} \;=\; \lambda_{\text{Compton},e}
\;\approx\; 3.86\times10^{-13}\,\text{m}. \tag{C.2.1}
$$

The hierarchy ratio is

$$
\mathcal{N}_e \;=\; \frac{R_e}{\ell_{\text{Planck}}}
\;\approx\; \frac{3.86\times 10^{-13}\,\text{m}}
               {1.62\times 10^{-35}\,\text{m}}
\;\approx\; 2.4\times 10^{22}. \tag{C.2.2}
$$

This means the KK tower has approximately 10²² usable
modes (winding numbers from 1 up to ~10²²) before the
Planck cutoff kicks in.

For the proton sheet (m_p ~ 10³ m_e), R_p ~ R_e /
1000, so 𝒩_p ~ 10¹⁹ — still a huge number.

For the neutrino sheet (m_ν ~ 10⁻⁶ m_e by rough
phenomenology), R_ν ~ 10⁶ R_e, so 𝒩_ν ~ 10²⁸.

**All three hierarchies are vastly larger than any
realistic winding number that enters the MaSt
phenomenology.**  The R50 filter studies, R54 model-E,
and subsequent work use winding numbers of order ~1
to ~10; these are well inside the EFT validity window
𝒩 ~ 10²²⁻²⁸ for every sheet.

### C.3 — What the UV cutoff means physically

At winding n ~ 𝒩, the KK mass reaches M_Planck.  At
this point:

- The KK wavelength λ_n = 2π R / n approaches ℓ_Planck,
  so the mode no longer resolves distances larger than
  the GRID lattice spacing — the continuum picture of
  a smooth torus breaks down.
- GRID's lattice phase dynamics (the fundamental
  content of grid/foundations.md A1–A6) becomes the
  relevant physics; the KK-on-torus is an emergent
  low-energy description and ceases to apply.

This is exactly what one expects of any EFT: it works
up to a cutoff, and the cutoff is set by the underlying
theory.  For MaSt on GRID, the cutoff is M_Planck and
the validity window is enormous.

**Conclusion:**  The KK-on-torus derivations of Tracks
1–8 are internally consistent as an EFT for all
phenomenologically relevant winding numbers.  The
Planck-scale UV completion (GRID) decouples cleanly
from the MaSt mode structure, as a good EFT
decoupling should.

---

## Section D — The compact scale as an inherited empirical input

### D.1 — What MaSt pins down

The tracks 1–8 derivation pins down, *for a given
compact scale R*:

- **Mass ratios** among the KK modes (F11, F25
  dimensionless μ² formula).
- **Charge assignments** (F14, tube-couples convention).
- **Mass-eigenstate mixing from cross-shears** (F26).
- **Lorentz force structure** (F17).

All of these depend only on the **dimensionless** ε,
s, and cross-shear parameters — not on R itself.

### D.2 — What MaSt does not pin down

The derivation does *not* pin down:

- **The compact scale R.**  This is inherited from the
  empirical fit to the electron mass (and via
  model-E, the nucleon masses and neutrino
  mass-squared differences).
- **The shape parameters (ε, s).**  These are fitted
  phenomenologically — most notably through the
  MaSt fine-structure constant identification α =
  s (F19 precursor in R45/R47) and the R50/R54
  filter results.
- **The cross-shear structure.**  Fitted in R54.
- **Whether the tori are stable ground states.**  This
  would require a full dynamical 8D action; Tracks 1–8
  treat the tori as static background geometry.

Each of these is a separate open problem, inherited
from MaSt's empirical-input posture and not addressed
in Program 1.

### D.3 — Analogy: lattice QCD

A useful analogy is lattice QCD.  The lattice spacing a
is a free parameter (chosen by the numerical
implementation); the mass ratios of the hadron spectrum
and the scaling with a are derived from the theory,
but *the value of a itself* is fixed by matching to
one physical quantity (e.g., the pion mass).  Nobody
considers this a failure of lattice QCD: a is an input
that matches the theory to reality, not a prediction.

MaSt's compact scale R plays the same role.  The
tracks 1–8 derivations give mass ratios; a single
match (e.g., to the electron mass) fixes R; all other
predictions follow.

---

## Section E — The hierarchy question

### E.1 — The question

Why is the compact radius R ~ 10²² ℓ_Planck and not
~ℓ_Planck?  Equivalently: why is the electron
mass ~10⁻²² M_Planck?

This is a form of the standard **hierarchy problem**:
the observed mass scales are far below the Planck
scale without an obvious mechanism.  In the Standard
Model, this takes the form "why is the Higgs mass so
much smaller than M_Planck?"; in KK theories, "why is
the compact radius so much larger than ℓ_Planck?"

### E.2 — What MaSt does and does not claim

MaSt does *not* claim to solve the hierarchy problem.
The claim of Tracks 1–8 is limited: *given* the
compact structure (at whatever scale), the mass,
charge, and mass-eigenstate structure follow from the
photon-on-torus kinematics.

The hierarchy R ≫ ℓ_Planck is treated as an inherited
constraint, identical in status to the choice of
compactification manifold in string theory or the
input lattice spacing in lattice QCD.

### E.3 — Known candidate mechanisms

If the hierarchy is eventually to be addressed, the
literature provides several candidate mechanisms —
none of which are adopted by Tracks 1–9 as derivations,
but which are listed here as possible future directions:

- **Large extra dimensions.** (Arkani-Hamed,
  Dimopoulos, Dvali 1998):  if gravity propagates in
  more compact dimensions than the SM gauge forces, R
  can be as large as ~mm and the 4D Planck mass still
  emerges at 10¹⁹ GeV.  MaSt's compact tori are much
  smaller than this, so this specific mechanism does
  not apply directly.
- **Warped compactification.** (Randall–Sundrum
  1999):  a non-trivial warp factor along a fifth
  dimension redshifts the effective scale on a brane.
  MaSt's compact T² has no warp factor in Tracks 1–8,
  but a warp could be added.
- **Dynamical stabilization.**  If the compact tori
  are solutions of an 8D dynamical action with a
  self-consistent modulus potential, the equilibrium
  R may be far from ℓ_Planck.  This requires positing
  the 8D action (which Tracks 1–8 do not).
- **GRID emergent compactification.**  If GRID's
  Planck-lattice dynamics produces the compact tori as
  composite structures (topological defects, flux
  tubes, or coherent phase patterns), their
  characteristic scale may be much larger than ℓ_Planck
  by the usual confinement-scale-vs-lattice-scale
  gap.  This is speculative and requires explicit
  GRID dynamics, which is beyond the scope of Tracks
  1–9.

**Stance.**  Tracks 1–9 treat R as inherited.
Addressing the hierarchy is outside Program 1 and
belongs to a later program (or to GRID's dynamical
sector when it is developed).

---

## Section F — Relation to GRID

### F.1 — GRID is a Planck-scale lattice

From grid/foundations.md A1–A6, GRID is a 4D causal
lattice with spacing ~ ℓ_Planck, carrying a U(1)
phase field on cells and bosonic 1-form gauge fields
on links.  All GRID physics lives natively at the
Planck scale.

### F.2 — MaSt's compact tori are emergent at a
### sub-Planck (but far-sub-Planck) scale

MaSt's tori are not fundamental objects in GRID's
axioms.  They are *emergent* structures — coherent
solutions of GRID dynamics at scales R ≫ ℓ_Planck.
Their existence (and specific size) is a claim about
GRID's dynamical phase diagram, not about its
kinematics.

The fact that MaSt's mass formulas work for any R is
a feature here:  GRID may eventually predict R
dynamically (at some specific value), and the KK-on-
torus machinery will then feed that value through
Tracks 1–8 to get the observed particle spectrum.  If
GRID predicts R ~ ℓ_Planck, the KK tower is Planck-
scale and phenomenology fails.  If GRID predicts
R ~ λ_Compton_e, MaSt's phenomenology works as
fitted.

### F.3 — The decoupling is consistent

Wilsonian EFT teaches that low-energy physics
decouples from high-energy physics up to
renormalization-group running of parameters.  MaSt
and GRID respect this:

- GRID provides the UV completion.
- MaSt provides the low-energy EFT on the emergent
  compact geometry.
- The hierarchy 𝒩 ≈ 10²² (C.2.2) is an **output** of
  the GRID dynamics (once that dynamics is specified)
  or an **input** to MaSt (fitted from particle
  masses).
- There is no inconsistency.  There is a gap:  GRID's
  dynamics that produces the compact structures at
  scale R has not yet been specified.

### F.4 — What remains open

Two related gaps, to be addressed outside Program 1:

1. **GRID dynamics producing the compact tori.**  What
   solution of GRID's phase dynamics corresponds to a
   2-torus (or T⁶) at the Compton scale?  This is a
   statement about GRID's emergent geometry that the
   project has not derived.  Candidate mechanisms
   (topological defects, coherent flux configurations,
   non-trivial ground states of the U(1) phase field)
   are listed in papers/matter-from-light.md but not
   yet executed.

2. **Setting the specific scale R.**  Even if GRID
   produces compact tori, the specific scale at which
   they form is a further question, addressable only
   once (1) is in place.

Both of these are GRID-layer problems, not KK-layer
problems.  Tracks 1–9 are complete and internally
consistent as MaSt-layer derivations; the scale
question is *below* the MaSt layer, in GRID dynamics
not yet specified.

---

## Lemma (Track 9 result)

We have established:

> **(F29) Scale-invariance of the KK-on-torus
> derivations.**  Every derivation in Tracks 1–8 of
> Program 1 uses the compact radius R only through:
> (a) the standing-wave quantization p_a = n_a ℏ / R_a,
> (b) the overall mass scale m_c = ℏ / (R c).  The
> **dimensionless** mass formula μ² = (m/m_c)² = Γ^{ab}
> n_a n_b (single torus; analogous expressions for two
> or three tori) depends only on the *shape* of the
> internal metric (the dimensionless parameters ε, s,
> and cross-shear ratios) and on the integer winding
> numbers.  Consequently:
>
> 1. All mass ratios, charge assignments, mass-
>    eigenstate structure, and Lorentz-force structure
>    derived in Tracks 1–8 are **independent of R**.
>    The Tracks 1–8 derivations work for any positive R.
>
> 2. The value R ~ 10²² ℓ_Planck used phenomenologically
>    by MaSt is an **inherited empirical input**, not a
>    derived quantity.  It is fixed by matching one
>    mass (e.g., the electron's) to observation; all
>    other mass ratios then follow from the
>    dimensionless formula.
>
> 3. The apparent conflict with traditional
>    Kaluza–Klein "Planck-mass states" is removed:
>    that conclusion rests on *pure-gravity* KK (where
>    R is set by Newton's constant), while MaSt's
>    KK-on-torus is a *background-field* treatment
>    using only the metric, Killing vectors, and
>    standing-wave quantization — none of which
>    prescribes a scale.
>
> 4. The UV validity window is n ≪ 𝒩 where 𝒩 = R /
>    ℓ_Planck ~ 10²² for the electron sheet.  All
>    phenomenologically relevant winding numbers (~1
>    to ~10) are comfortably inside this window.  The
>    MaSt KK-on-torus treatment is a consistent EFT
>    up to the Planck cutoff at which GRID lattice
>    dynamics takes over.
>
> 5. The hierarchy question — why R ≫ ℓ_Planck — is
>    **not addressed** by Tracks 1–9.  It is
>    documented as an inherited open problem, to be
>    resolved by GRID dynamics (the mechanism that
>    produces the compact tori) or by a separate
>    stabilization argument, neither of which is
>    part of Program 1.

**What this caps.**  With F29, Program 1's
KK-on-torus structure is closed in the following
sense:  every element that can be derived from the
photon-on-torus setup *without* fixing the compact
scale has been derived (Tracks 1–6 for a single torus;
Track 8 for two tori; the three-sheet T⁶ extension
is bookkeeping on top of Track 8).  What remains is
external:  (i) the spin question (documented with
three alternatives in derivations 7a, 7b, 7c); (ii)
the GRID dynamics that produces the compact tori at
the observed scale R (documented here as inherited).
These are genuine open problems, appropriately
flagged, and do not block the use of Tracks 1–8 as
the kinematic backbone of MaSt at whatever scale
GRID (or empirical fitting) eventually pins down.

GRID-compatibility:  the entire analysis of Track 9
uses only the bosonic metric and standing-wave
structure of Tracks 1–8 — no Grassmann fields, no
spin structure — and is GRID-native throughout.
