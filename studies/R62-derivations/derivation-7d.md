# Derivation 7d — Spin from per-sheet Dirac–Kähler construction

**Program 1, Track 7 (continuation after 7a, 7b, 7c).**  Derive
the spin content of MaSt's matter modes from the compact
topology of each Ma sheet, using the Dirac–Kähler construction
on flat 2-tori.  The result is a cleaner and stronger version
of 7c:

> **Each Ma sheet is a flat 2-torus.  It admits a Dirac–Kähler
> field as its privileged fermion content.  Kaluza–Klein
> reducing this field produces a tower of 4D Dirac spinors
> labeled by winding numbers (n_t, n_r).  Every mode is
> spin-½ in 4D, independent of (n_t, n_r).  Compound particles
> spanning multiple sheets have total spin given by SU(2)
> angular-momentum composition of per-sheet spin-½ contributions.**

This gives the Standard-Model particle taxonomy structurally:

- 1 active sheet → spin ½ (leptons)
- 2 active sheets → spin 0 or 1 (mesons)
- 3 active sheets → spin ½ or 3/2 (baryons)

Exactly matching observation, and matching R60 Track 20's
independently-derived empirical winner (unit-per-sheet AM
rule).

7d is the MINIMAL spin derivation that:

- Gives every matter mode spin ½ regardless of winding (a
  Dirac-field property, not a mode-specific property)
- Sidesteps the classical KK fermion problem (globally-defined
  bulk spinors often give anomalies, wrong generations, or
  non-chiral doubling)
- Requires only **per-sheet** spin structures on flat T²
  (well-established mathematically), not a global 6D Dirac
  spinor (7c's approach, which has GRID-compatibility issues)
- Reduces to 7b's ratio rule in a specific limit (single-sheet,
  (n, 2n) modes) while correctly handling all other cases

---

## The KK fermion problem — historical context

Standard Kaluza–Klein reduction, from its origins, has been
notably good at producing gauge bosons and notably difficult
at producing matter fermions:

- **Kaluza 1921 / Klein 1926** — 5D gravity reduces to 4D
  gravity + Maxwell + a scalar.  The photon's spin-1 emerges
  automatically from the 4D vector index of the 5D metric.  A
  mathematical success.

- **Adding fermions (Witten 1981 and onward)** — generic
  compactifications fail to produce the observed fermion
  content.  Common pathologies:
  - *Chirality doubling*: KK reduction of a bulk Dirac
    spinor on many manifolds gives non-chiral 4D fermions
    (both left- and right-handed modes at every KK level),
    contradicting the observed chiral structure of weak
    interactions.
  - *Generation counting*: getting exactly three observed
    generations requires specific geometric conditions
    (index theorems tied to Euler number, Ricci curvature,
    holonomy groups).  Not all compact manifolds qualify.
  - *Non-propagating spinor components*: on some manifolds
    the KK zero-mode of a bulk Dirac is not a propagating
    4D field at all — it's frozen by the compactification
    geometry.

- **Consequence**: half a century of KK-inspired theories
  (including supergravity, heterotic string, and M-theory
  compactifications) have struggled to produce matter
  spectra matching the Standard Model from fundamental
  geometry alone.  The spin of fermions, their counts, and
  their charges are typically imposed by hand through
  geometric choices (Calabi–Yau manifold, G₂ holonomy,
  orbifold resolutions).

**The per-sheet Dirac–Kähler approach** avoids these global
problems by working sheet-by-sheet.  Each 2-torus is flat,
admits four clean spin structures, and the Dirac–Kähler
correspondence on flat T² is mathematically rigorous and
completely standard.  Three independent sheets produce three
independent fermion families, sidestepping the need to derive
generation counts from a single global spinor on T⁶.

This is not just a technical convenience — it is an
architectural choice that respects MaSt's postulate that each
Ma sheet is an independent 2-torus hosting its own matter
content.

---

## Attribution

The per-sheet construction used here rests on standard
results:

- **Ivanenko & Landau 1928** — first formulation of the
  Dirac–Kähler correspondence (spinors as differential
  forms).

- **Kähler 1962** — modern formulation of the Dirac–Kähler
  equation.

- **Becher & Joos 1982** — *The Dirac–Kähler equation and
  fermions on the lattice*, Z. Phys. **C 15**, 343–365.  The
  foundational treatment relevant to lattice realizations.

- **Kogut & Susskind 1975** — *Hamiltonian formulation of
  Wilson's lattice gauge theories*, Phys. Rev. D **11**,
  395–408.  Staggered fermions on a cubic lattice, the
  natural discretization of the Dirac–Kähler construction.

- **Witten 1981** — *Search for a realistic Kaluza–Klein
  theory*, Nucl. Phys. B **186**, 412–428.  The fermion
  problem in KK compactifications, and the constraints that
  must be imposed.

- **Rabin 1982** — *Homology theory of lattice fermion
  doubling*, Nucl. Phys. B **201**, 315–332.  The topological
  origin of the species-doubling problem and its resolution
  via Dirac–Kähler reduction.

The novel content in 7d is not the per-sheet Dirac–Kähler
construction itself but its **application to MaSt**: the
observation that the three Ma sheets of MaSt are exactly
three independent flat 2-tori, and the per-sheet spin-½
fermion content follows automatically, with compound modes
composing by SU(2) across sheets.

---

## Inputs

1. **MaSt's sheet structure.**  Each of the three Ma
   dimensions is a 2-torus with compact directions (tube,
   ring).  Sheets are geometrically independent (the Ma
   metric has no off-block entries between sheets at
   leading order).

2. **Flat geometry per sheet.**  After the natural-form
   parameter choice, each sheet has a flat (possibly sheared)
   2-torus metric.  Flatness is what admits the clean
   Dirac–Kähler correspondence.

3. **Kaluza–Klein compactification.**  Fields on M⁴ × T²
   decompose into towers labeled by compact momenta (n_t,
   n_r); the effective 4D Lagrangian is obtained by
   integrating out compact coordinates.

4. **F7 / F11 mass formula** (derivations 3 and 4) —
   m²c² = h^{ab} P_a P_b.

5. **F14 charge formula** (derivation 5) — Q = e n_t under
   the tube-couples convention.

6. **Standard flat-torus spinor representation theory** —
   Cl(2) (the 2D Clifford algebra) has a 2-complex-component
   irreducible representation; a flat T² admits four
   inequivalent ℤ₂ spin structures; the Dirac–Kähler field
   is a complete set of differential forms on T², of which
   the Dirac spinor is a specific projection.

No other axioms are required.  7d does NOT require a global
6D Dirac spinor on T⁶ (7c's assumption); it needs only
per-sheet Dirac structure.

---

## Section A — Setup

### A.1 — Per-sheet 2-torus structure

MaSt's three Ma sheets are labeled e, p, ν.  Each sheet's
two compact directions are (tube, ring) with circumferences
(L_t, L_r).  The sheet metric is flat (possibly sheared):

$$
g^{(sheet)}_{ij} \;=\; k_{sheet} \begin{pmatrix} 1 & s\varepsilon \\ s\varepsilon & 1 + (s\varepsilon)^2 \end{pmatrix}
$$

where ε = L_t/L_r, s is the shear, k is the diagonal scale
(1/(8π) at R59 natural form).  For the Dirac–Kähler
construction, flatness is sufficient — the shear twists the
coordinates but does not introduce curvature.

Each sheet is topologically T² with first Betti number
b₁ = 2, second Betti number b₂ = 1, and Euler characteristic
χ = 0.

### A.2 — Spin structures on T²

A spin structure on T² is a choice of how a spinor field
transforms under the two generators of π₁(T²) ≅ ℤ².  Each
generator can multiply the spinor by +1 (periodic / Ramond)
or −1 (antiperiodic / Neveu–Schwarz):

$$
\psi(y^t + 2\pi R_t, y^r) = (-1)^{\varepsilon_t} \psi(y^t, y^r), \qquad
\psi(y^t, y^r + 2\pi R_r) = (-1)^{\varepsilon_r} \psi(y^t, y^r)
$$

The four choices (ε_t, ε_r) ∈ {0, 1}² give the four spin
structures on T² (labeled RR, RNS, NSR, NSNS in string
theory).  For matching MaSt's observed integer compact
momenta (F7/F14), we take the **RR (periodic) structure**
(ε_t, ε_r) = (0, 0) throughout.  Other sectors are available
as additional towers if the physics requires them (e.g., for
doubling cancellations).

### A.3 — The Dirac–Kähler field

On a flat manifold of dimension d, the Dirac–Kähler field is
an inhomogeneous differential form

$$
\Phi \;=\; \phi_0 + \phi_1 + \phi_2 + \cdots + \phi_d
$$

where φ_k is a k-form.  The Dirac–Kähler equation is

$$
(d - \delta + m)\Phi \;=\; 0
$$

where d is the exterior derivative and δ its adjoint.  This
equation is **equivalent on flat spacetime to the Dirac
equation**, with the Dirac spinor obtained as a specific
projection of Φ.

**Key fact (Becher–Joos 1982).**  On a flat d-dimensional
manifold, a Dirac–Kähler field Φ is equivalent to 2^{⌊d/2⌋}
copies of a Dirac spinor.  For d = 2, this is 2 copies; for
d = 4, it is 4 copies ("species doubling" in lattice gauge
theory).  The 2^{⌊d/2⌋} factor is removed in specific
projections — the Dirac–Kähler "single-species" projection
gives exactly one Dirac spinor.

On T² (d = 2), the Dirac–Kähler field has 2² = 4 real
components organized as:

- 1 scalar (0-form): φ_0
- 2 vector components (1-form): φ_1 = φ_t dy^t + φ_r dy^r
- 1 pseudoscalar (2-form): φ_2 = φ_{tr} dy^t ∧ dy^r

Total: 4 real components, equivalent after projection to 1
complex 2-component Dirac spinor on T².

---

## Section B — S¹ case: the photon (brief)

To establish the compactification-determines-spin principle
with a simple example, consider a single compact dimension
S¹.  This case is solved by standard Kaluza–Klein theory and
we include it only as context.

### B.1 — 1-form on M⁴ × S¹

A U(1) gauge field A_M on M⁴ × S¹ has 5 components
(M = 0, 1, 2, 3, 5).  Under KK reduction:

- A_μ (μ = 0, 1, 2, 3) → 4D 1-form (spin 1 gauge field)
- A_5 → 4D scalar (KK photon, absorbed into Higgs-like sector or decoupled)

The spin-1 nature of A_μ comes from its 4D vector index
structure, preserved through reduction.  Winding mode
(n ∈ ℤ) in S¹ direction gives mass:

$$
m^2 c^2 = (n\hbar / R)^2
$$

but does **not** change the spin.  Every KK mode of the
1-form is a 4D spin-1 field.

This is entirely conventional; we note it here because the
same pattern — compact topology privileges a field type,
field type determines 4D spin — appears in the T² case
below.

---

## Section C — T² case: per-sheet spin-½ fermion (main result)

### C.1 — Dirac–Kähler field on M⁴ × T²

Put a Dirac–Kähler field Φ on the total space M⁴ × T².
Components decompose by rank and by M⁴ vs T² indices.  The
relevant KK decomposition for the 2D Dirac content:

$$
\Phi(x, y) \;=\; \sum_{n_t, n_r \in \mathbb{Z}} \Phi_{n_t, n_r}(x) \cdot e^{i(n_t y^t / R_t + n_r y^r / R_r)}
$$

where each Φ_{n_t, n_r}(x) is a 4D field containing the
projection onto the Dirac sector of the 2D Dirac–Kähler
multiplet.  With the RR spin structure (A.2), all integer
(n_t, n_r) are permitted.

### C.2 — The Dirac–Kähler equation reduces to the Dirac equation

The Dirac–Kähler equation (d − δ + m)Φ = 0 decomposes
mode-by-mode into

$$
(i\gamma^\mu \partial_\mu - m_{n_t, n_r}) \psi_{n_t, n_r}(x) \;=\; 0
$$

where ψ_{n_t, n_r}(x) is the 4D Dirac spinor projected from
the (n_t, n_r) sector of Φ, γ^μ are 4D Dirac γ matrices, and
the 4D mass is

$$
m^2_{n_t, n_r} \;=\; (n_t \hbar / R_t)^2 + (n_r \hbar / R_r - n_t s \hbar / R_r)^2 + m_0^2
$$

with shear s and any bulk mass m₀.  This matches F7/F11
exactly (the shear correction is the standard Kaluza–Klein
reduction of a sheared torus).  It's the Klein–Gordon
equation, obtained by squaring the 4D Dirac equation.

**Each KK mode is a 4D Dirac spinor — a spin-½ field.**  The
spin is independent of (n_t, n_r); it is inherited from the
Dirac–Kähler structure's internal representation content,
which is the flat-T² spin bundle.

### C.3 — Why the Dirac–Kähler projection is well-defined on flat T²

The Dirac–Kähler equivalence has a subtlety: on curved
manifolds, the projection from the Dirac–Kähler multiplet to
a single Dirac spinor depends on additional structure (metric,
spin connection).  **On a flat manifold, this projection is
canonical**: there is a global parallel-transport-preserved
orthonormal frame, and the projection is a fixed linear map
defined by the Clifford algebra Cl(2).

Since each MaSt sheet is flat (possibly sheared), the
Dirac–Kähler construction gives a unique Dirac spinor per
KK mode.  No additional structure is needed.  This is why
7d works cleanly on flat T² where 7c's global bulk Dirac
spinor on T⁶ (with possible curvature in the combined
product) was harder to handle.

### C.4 — Charge from the same KK structure

Including U(1) gauge coupling in the Dirac–Kähler
construction gives, for each KK mode, the minimally coupled
Dirac equation with electric charge

$$
Q \;=\; e \cdot n_t
$$

under the tube-couples convention of derivation 5.  This is
F14, unchanged.  The charge coupling is independent of the
spin content — it's set by the tube winding, while spin is
set by the Dirac–Kähler representation.

### C.5 — Summary of the single-sheet result

A Dirac–Kähler field on M⁴ × T² (per MaSt sheet) reduces to:

- A tower of 4D Dirac spinors labeled by winding (n_t, n_r)
- Each tower member is **spin-½ in 4D**
- Mass is set by F7/F11
- Charge is set by F14
- Spin is **independent of (n_t, n_r)** — it's the uniform
  label of the underlying field type

This is the per-sheet content of 7d.  Every KK mode of a
Ma sheet, regardless of its compact momentum, is a spin-½
4D Dirac spinor.

---

## Section D — Multiple sheets: three independent fermion families

MaSt has three Ma sheets (e, p, ν), each topologically T²
and geometrically independent.  The total matter-sector field
content is the direct sum (not the product) of three
independent Dirac–Kähler fields:

$$
\Phi_{\text{matter}} \;=\; \Phi_e \oplus \Phi_p \oplus \Phi_\nu
$$

Each Φ_{sheet} carries its own KK tower; the three are
independent at the free-field level (cross-sheet couplings
enter through the ℵ channel and the α couplings established
in R59/R60).

**Consequence.**  Three independent spin-½ Dirac towers,
one per sheet — exactly the three-family matter structure of
the Standard Model, realized as three geometrically-separated
sheets rather than through a single bulk manifold with
specific curvature or topology.

This sidesteps Witten's generation-counting problem (the KK
problem of deriving three generations from a single
manifold): in MaSt, the three generations emerge as three
distinct sheets, each a T², each supporting its own
independent Dirac–Kähler tower.

---

## Section E — Compound spin from SU(2) angular-momentum composition

### E.1 — Multi-sheet particles

A compound particle is a mode with nonzero winding on more
than one sheet.  Its total Hilbert-space state is the tensor
product of per-sheet states:

$$
|\psi_{\text{compound}}\rangle \;=\; |\psi_e\rangle \otimes |\psi_p\rangle \otimes |\psi_\nu\rangle
$$

Each per-sheet factor carries spin ½ (from Section C).  The
composite's total spin is determined by **standard SU(2)
angular-momentum addition** across active sheets.

### E.2 — Allowed spins by active-sheet count

For N active sheets (each contributing spin ½), the allowed
total spins are:

- **N = 0**: no matter content → spin 0 (not a matter particle).
- **N = 1**: spin ½ (a single lepton or quark ladder).
- **N = 2**: ½ ⊗ ½ = 0 ⊕ 1.  Spin 0 or spin 1 (singlet or triplet).
- **N = 3**: ½ ⊗ ½ ⊗ ½ = (0 ⊕ 1) ⊗ ½ = ½ ⊕ ½ ⊕ 3/2.
  Two spin-½ states and one spin-3/2 state.
- **N = 4+**: requires at least two of the same sheet, not
  supported in MaSt's three-sheet architecture.

### E.3 — Map to the particle taxonomy

| Active sheets | Allowed spin | Observed particle class |
|:-:|:-:|:---|
| 1 | ½ | **Leptons** (electron, muon, tau, neutrinos) |
| 2 | 0 or 1 | **Mesons** (pseudoscalar → 0; vector → 1) |
| 3 | ½ or 3/2 | **Baryons** (octet → ½; decuplet → 3/2) |

This is exactly the Standard Model particle taxonomy.  The
mapping is **structural**: the number of active sheets is a
topological label of the compound mode, and it determines the
spin class via SU(2) composition.

### E.4 — Which specific spin within the allowed set?

The SU(2) composition gives a SET of allowed spins.  Which
specific spin in the set is realized depends on additional
structure:

- For 2-sheet compounds, spin 0 (singlet) vs spin 1 (triplet)
  depends on the symmetry of the two-spinor combination.
  Pseudoscalar mesons (π, K, η) are singlets; vector mesons
  (ρ, φ, K*) are triplets.

- For 3-sheet compounds, spin ½ vs spin 3/2 depends on the
  permutation symmetry of the three-spinor combination.
  Octet baryons (p, n, Λ, Σ, Ξ) are spin ½; decuplet baryons
  (Δ, Σ*, Ξ*, Ω) are spin 3/2.

These fine distinctions are controlled by the internal
structure of the mode — how the tube and ring windings on
different sheets couple, what α-channel back-reactions
exist, and so on.  7d establishes the allowed spin sets;
the specific assignment within those sets requires additional
derivation (identified as pool item; not blocking).

---

## Section F — Empirical correlation

### F.1 — R60 Track 20 independently derived this rule

R60 Track 20 performed an unbiased search over 12 candidate
compound-spin rules, using model-F's observed particle
inventory as a test set.  The rule that emerged as the
winner was:

> **Unit-per-sheet angular-momentum addition**: each active
> sheet contributes spin ½; total spin is in the SU(2)
> composition of per-sheet ½'s.

This is **exactly** the rule derived structurally in
Sections C–E of 7d.  Track 20 also identified:

- **14 of 16 non-input inventory particles match within 2%**
  under this rule (best of all 12 tested rules)
- **No pathological misses** (unlike the parity rule, which
  admits particles at >100% off)
- **The Standard Model taxonomy falls out**: 1-sheet →
  lepton, 2-sheet → meson, 3-sheet → baryon, exactly
  matching observation

The only persistent failure mode is the pion desert
(π⁰ at ~10%, π± at ~13%), which is independent of spin
structure — an open issue since model-E.

This empirical correlation is strong support for 7d's
derivation path.

### F.2 — The muon as a 1-sheet lepton

Track 20's search found the muon at tuple (1, 1, 0, 0, 0, 0)
— a single-sheet mode on the e-sheet alone.  This matches
the Standard Model understanding of the muon as a heavier
generation of the electron, not as a compound state.

Under 7b (the ratio rule), this assignment fails: (1, 1) has
ratio 1, not 1/2.  Under 7d, (1, 1) on the e-sheet is a
Dirac KK mode, spin ½ regardless of ratio.  **7d is
consistent with the muon's observed 1-sheet structure; 7b
is not.**

This is a concrete discriminator between 7b and 7d, and 7d
wins.

### F.3 — Nuclear scaling respects the structure

Nuclear modes (deuteron, ⁴He, ¹²C, ⁵⁶Fe) use scaling
n_pt = 3A, n_pr = 6A on the p-sheet — all multiples of 3,
all consistent with the Z₃ selection rule (R60 Track 16).
These are 1-sheet modes on the p-sheet alone, so under 7d
they're spin ½.  Nuclei have varying spins: d is spin 1,
⁴He is spin 0, ¹²C is spin 0, ⁵⁶Fe is spin 0.

For nuclei (which are compound bound states of multiple
nucleons), spin is determined by the nuclear shell structure,
not by the single-mode KK-reduction of 7d.  7d gives the
spin of the fundamental nucleon; nuclear spin is a
many-body problem layered on top.

---

## Section G — Relation to 7a, 7b, 7c; note on GRID

### G.1 — 7a (metric-only)

7a asked whether the METRIC of a sheared 2-torus alone
produces spin ½.  Answer: no — the Levi-Civita connection is
zero (flat torus), Killing algebra is abelian, and no (-1)
phase arises from metric structure.

**7d is fully consistent with 7a's negative result.**  7d
does NOT claim spin ½ comes from the metric — it comes from
the FIELD TYPE (Dirac–Kähler), which is an additional
structure chosen beyond the metric.  7a's result tells us
what we cannot do; 7d tells us what we must do instead.

### G.2 — 7b (CP-polarization ratio rule)

7b counted rotations of a circularly-polarized classical
electric field around a torus and obtained spin = n_t/n_r.
This is a useful SINGLE-MODE heuristic: for (1, 2), spin =
½; for (n, 2n), spin = ½.

**7d's relation to 7b.**  7d says every KK mode is spin ½,
regardless of ratio.  But 7b's ratio condition n_r = 2 n_t
picks out a specific subset of modes that are "clean" in
another sense: they are the modes where the CP polarization
closes cleanly on the torus without external imposition.

The two are not contradictory:
- 7d gives the SPIN (topological, ½ for any KK mode).
- 7b identifies a PRIVILEGED MODE CLASS (n, 2n) with
  special kinematic properties relevant to mass or
  magnetic-moment computations.

Under 7d, 7b's "ratio rule" is demoted from a spin rule to
a mode-structure rule.  This is consistent with R60 Track 20's
finding that strict 7b per-sheet fails across the inventory
while unit-per-sheet AM (which is 7d's result) succeeds.

### G.3 — 7c (6D bulk Dirac spinor)

7c proposed a single global 6D Dirac spinor on M⁴ × T⁶
(equivalently, on M⁴ × (T²)³ with the three sheets
considered as a single compactification).  KK reducing gives
4D Dirac fermions of spin ½.

**7d's relation to 7c.**  7d is the **per-sheet restriction
of 7c**.  Instead of a single 6D bulk Dirac spinor, 7d
uses three independent 2D Dirac–Kähler fields, one per
sheet.

Advantages of 7d over 7c:

1. **Mathematical simplicity.**  Per-sheet Dirac–Kähler on
   flat T² is completely standard (Becher–Joos 1982,
   Kogut–Susskind staggered fermions).  No 6D Clifford
   algebra gymnastics needed.

2. **Three generations automatic.**  Three sheets directly
   give three fermion families, no need to derive this
   from a single-manifold index theorem.

3. **No global-spinor anomalies.**  The species-doubling
   and chirality problems of bulk spinors on curved
   compactifications don't arise because each sheet is
   treated independently.

4. **Better compatibility with GRID-style lattice
   substrates** (see G.4).

Disadvantages:

1. **Explicit axiomatization of per-sheet spin structure
   needed.**  Saying "each sheet admits a Dirac–Kähler
   field" is an assumption; deriving it from a deeper
   principle (why Dirac rather than scalar, why each sheet
   independently) is an open derivation target.

2. **No direct derivation of cross-sheet couplings.**  The
   α-channel couplings of R59/R60 are external to 7d; they
   attach to the per-sheet spinors via minimal coupling to
   U(1) gauge fields, not derived from a unifying bulk
   structure.

On balance, 7d is the cleaner construction and the one that
matches R60 Track 20's empirical pattern.  7c remains as a
"more ambitious bulk version" with theoretical attraction
but architectural cost.

### G.4 — GRID observation (passing note)

An interesting architectural parallel appears when looking
at GRID's photon sector.  GRID places a U(1) phase field on
its sub-Planck scale dimension (aleph ≈ S¹, one compact
direction).  Standard KK reduction of a 1-form on M⁴ × S¹
gives the photon — a 4D spin-1 field — via the same
compactification-determines-field-type principle that gives
matter spin-½ on M⁴ × T² per sheet.

This is:

- **Not part of 7d's derivation.**  7d derives spin ½ for
  matter; it does not depend on GRID for its argument.
- **A concordance observation.**  The same principle
  (compact topology → privileged field type → 4D spin)
  applies to both the photon (1 compact dim → spin 1) and
  to matter (2 compact dims per sheet → spin ½).

A rigorous GRID-level derivation of the photon — including
the lattice-level construction of Maxwell from GRID's U(1)
phase axioms — is a separate derivation target.  Likely
to be framed as a future R62 derivation.

---

## Lemma (Track 7d result)

We have shown:

> **(F25) Per-sheet spin content.**  Each flat 2-torus sheet
> in MaSt admits a Dirac–Kähler field as privileged matter
> content.  Its Kaluza–Klein reduction to M⁴ is a tower of
> 4D Dirac spinors labeled by winding (n_t, n_r), each
> spin-½, with mass given by F7/F11 and charge by F14.  The
> spin is independent of winding numbers — it is the
> topological label of the Dirac–Kähler sector.
>
> **(F26) Three-sheet fermion family structure.**  MaSt's
> three Ma sheets provide three independent Dirac–Kähler
> fields.  Each delivers an independent spin-½ KK tower.
> The three-family structure of matter observed in the
> Standard Model emerges from the three-sheet architecture,
> not from a single-manifold index theorem.
>
> **(F27) Compound spin by SU(2) composition.**  Compound
> particles on multiple active sheets have total spin given
> by SU(2) angular-momentum addition across per-sheet
> spin-½ contributions.  The allowed-spin set for N active
> sheets is:
> - N = 1: ½
> - N = 2: 0 or 1
> - N = 3: ½ or 3/2
>
> **(F28) Standard Model taxonomy.**  The active-sheet
> count maps directly onto the Standard Model particle
> classification:
> - 1 sheet ↔ lepton (spin ½)
> - 2 sheets ↔ meson (spin 0 or 1)
> - 3 sheets ↔ baryon (spin ½ or 3/2)
> This classification is structural, not postulated — it
> follows from the tensor-product decomposition of per-sheet
> fermion content.

F25 establishes the per-sheet spin content from standard
Dirac–Kähler on flat T².  F26 extends to the three-sheet
MaSt architecture.  F27 gives the compound-spin rule by
SU(2) composition.  F28 matches the observed Standard Model
taxonomy.

The rule is:

- Mass-formula-preserving (matches F7/F11).
- Charge-formula-preserving (matches F14).
- Compatible with the negative result of 7a (spin not from
  metric).
- Consistent with 7b as a mode-structure rule within its
  single-sheet domain of validity.
- Per-sheet restriction of 7c, avoiding 7c's global-bulk
  challenges.
- Empirically supported by R60 Track 20, where unit-per-sheet
  AM emerged as the best-fit compound-spin rule without
  prior knowledge of the derivation.

Open items:

- Axiomatize per-sheet Dirac–Kähler from deeper principles
  (why Dirac, why each sheet independently) — pool item
  derivation target.
- Rigorously derive which specific spin within the
  SU(2)-allowed set is realized for each compound (spin 0
  vs spin 1 for mesons; spin ½ vs spin 3/2 for baryons) —
  requires internal-structure analysis of tuple couplings.
- Bridge to GRID-style lattice substrates via the
  Kogut–Susskind / Dirac–Kähler equivalence — open
  derivation target (see G.4).

F25–F28 give MaSt a coherent derivation-backed spin story
for the first time, replacing the heuristic parity rule and
the single-sheet-only 7b ratio rule with a full
per-sheet-plus-composition framework.
