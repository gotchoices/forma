# Derivation 11 — Magnetic moment at tree level

**Program 1, Track 11 (promoted from pool item g).**  Derive
the tree-level magnetic moment of a MaSt standing-wave
eigenstate from the geometric machinery of Tracks 1–10 plus
the per-sheet Dirac–Kähler spin derivation D7d.  Target values:

- **Electron (single-sheet):**  g_e = 2 exactly.
  μ_e = e ℏ / (2 m_e) = 1 Bohr magneton.
- **Proton (three-quark Z₃ composite under the (3, 6)
  interpretation):**  g_p = 6 exactly at tree level.
  μ_p = 3 μ_N (nuclear magnetons).

**Scope statement.**  Observed values are g_e ≈ 2.00232
(electron anomaly 0.23%) and g_p ≈ 5.586 (proton anomaly
≈ 7% below tree).  These anomalies are radiative /
strong-interaction corrections and are **explicitly out of
scope** — handled by standard QED (electron) and QCD-analog
corrections (proton) that MaSt inherits as-is.  Track 11
produces the tree-level numbers only.

---

## Attribution

Two established lines of work combine here:

- **Dirac 1928** — the original derivation that g = 2 is a
  structural constant of the Dirac representation of SL(2, C).
- **Kaluza–Klein magnetic moment literature** — that a 4D
  spinor obtained by KK reduction from a higher-dimensional
  manifold inherits g = 2 at tree level, with no free
  parameters.  Covered in Witten 1981, *Search for a realistic
  Kaluza-Klein theory*, and Duff–Nilsson–Pope 1986,
  *Kaluza-Klein supergravity*.
- **Beg–Lee–Pais 1964** — the SU(6) quark-model calculation
  that the proton's magnetic moment at tree level is exactly
  3 μ_N when the three constituent quarks have flavor-dependent
  charges (Q_u = +2/3, Q_d = −1/3) and common constituent mass
  m_q = m_p/3.  Covered in Close 1979, *An Introduction to
  Quarks and Partons*.

The novel content in Track 11 is applying these established
machinery to MaSt's specific architecture:

1. **Single-sheet Dirac spinor from D7d per-sheet Dirac–Kähler**
   (rather than a 5D or 11D bulk Dirac).
2. **Three-quark proton from R60 Track 16's Z₃ confinement
   derivation** (rather than postulated SU(3) color triplets).
3. **Cross-shear invariance check** confirming MaSt's internal
   shears (σ_ra from R60 Track 7) do not shift g at tree level.

The numerical predictions (g_e = 2, g_p = 6) are identical to
the Standard Model tree-level expectations.  The novelty is in
the derivational path through MaSt's per-sheet + Z₃
architecture.

---

## Inputs

1. **D7d (F25–F28)** — per-sheet Dirac–Kähler on each flat
   2-torus gives a 4D Dirac spinor tower of spin ½ per
   winding (n_t, n_r).  Used in §B for the electron.
2. **D6 (F17–F19)** — minimal coupling D_μ = ∂_μ − i(Q/ℏ)A_μ^ext
   falls out of the 6D separation of variables under an
   external weak EM perturbation in the spacetime block.  Shear
   is mass-only at centroid level (F19).  Used in §B and §E.
3. **D10 (F30–F33)** — full 6D architecture giving the three
   sheets and the universal charge formula Q = e(−n_1 + n_5).
   Used in §C for the proton constituents.
4. **R60 Track 16** — Z₃ confinement on the p-sheet, deriving
   the (3, 6) proton as three (1, 2) quark constituents at
   120° phase offsets.  Used in §C.
5. **R60 Track 15** — composite α rule (α_sum_composite =
   n_et − n_pt/gcd + n_νt); used in §C for charge consistency.
6. **R60 Track 7** — σ_ra structural cancellation derivation;
   used in §E for the cross-shear invariance check.

No new quantum inputs beyond those already established in
Tracks 1–10 and R60 work.

---

## Section A — Setup

### A.1 — The 4D Dirac equation with external field

From D6 F18, the 6D wave equation for a matter field on
M⁴ × T⁶ separates cleanly under a weak external EM
perturbation A_μ^ext(x) in the spacetime block.  The compact
mode wavefunction factors out; the 4D envelope ψ obeys

$$
\Bigl[i\,\gamma^\mu\,\bigl(\partial_\mu - i\tfrac{Q}{\hbar}\,A_\mu^{\text{ext}}\bigr)
\;-\;m\Bigr]\,\psi(x) \;=\; 0
$$

where:

- Q = e(−n_et + n_pt) is the charge from F14/F15 (R60: charge
  is the effective per-strand value under the composite α rule)
- m is the KK mass from F7/F11
- γ^μ are the 4D Dirac matrices in standard Clifford basis

This is the standard Dirac equation in an external EM field,
with the KK origin of m and Q made explicit.  The equation
is the starting point for the magnetic-moment calculation.

### A.2 — The Pauli reduction (non-relativistic limit)

Write the 4-component Dirac spinor in large-/small-component
form:

$$
\psi \;=\; e^{-imt/\hbar}\begin{pmatrix}\varphi\\\chi\end{pmatrix}
$$

with 2-component Pauli spinors φ (upper) and χ (lower), and
factor out the rest-mass phase.  In the non-relativistic limit
(E_kinetic ≪ mc²), the lower component satisfies

$$
\chi \;\approx\; \frac{1}{2mc}\,\vec{\sigma} \cdot \vec{\pi}\,\varphi
$$

where $\vec{\pi} = \vec{p} - Q \vec{A}^{\text{ext}}/c$ is the
kinetic momentum.  Substituting into the equation for φ gives
the Pauli equation:

$$
\Bigl[\frac{(\vec{\sigma}\cdot\vec{\pi})^2}{2m}
\;+\;Q A_0^{\text{ext}}\Bigr]\,\varphi \;=\; E_{\text{NR}}\,\varphi
$$

Using the identity (valid for any Pauli-matrix operator):

$$
(\vec{\sigma}\cdot\vec{\pi})^2 \;=\; \vec{\pi}^{\,2}
\;-\;\frac{Q\hbar}{c}\,\vec{\sigma}\cdot\vec{B}^{\text{ext}}
$$

the Pauli Hamiltonian becomes

$$
\boxed{\;\;H \;=\; \frac{\vec{\pi}^{\,2}}{2m} \;+\; Q A_0^{\text{ext}}
\;-\;\frac{Q\hbar}{2mc}\,\vec{\sigma}\cdot\vec{B}^{\text{ext}}\;\;}
$$

The last term is the **magnetic moment interaction**.  Writing
it in the standard form $-\vec{\mu}\cdot\vec{B}$ with
$\vec{\mu} = g\,(Q/2mc)\,\vec{S}$ and $\vec{S} = \hbar\vec{\sigma}/2$:

$$
-\vec{\mu}\cdot\vec{B} \;=\; -g \cdot \frac{Q}{2mc} \cdot \frac{\hbar}{2}\,
\vec{\sigma}\cdot\vec{B}
$$

Comparing with $-\frac{Q\hbar}{2mc}\,\vec{\sigma}\cdot\vec{B}$,
we read off

$$
\boxed{\;\;g \;=\; 2\;\;}
$$

This is **Dirac's result** (1928).  It is structural — the
factor of 2 comes from the Dirac representation's specific
form of γ^μ, not from any free parameter in the theory.

The derivation above is the standard textbook Dirac-equation
Pauli reduction (Dirac 1928; reproduced in any QFT text such as
Peskin & Schroeder §3.3 or Bjorken & Drell §1.4).  We reproduce
it here for completeness; the MaSt-specific content is in what
we put INTO the Dirac equation (the per-sheet spinor structure
from D7d, the mass and charge from F11/F14), not in what we
extract from the Pauli reduction itself.

---

## Section B — Electron case

### B.1 — Single-sheet (1, 2) Dirac spinor

Under D7d's per-sheet Dirac–Kähler construction, the electron
is a KK mode of the Dirac–Kähler field on the e-sheet (flat
T² with ε_e = 397.074, s_e = 2.004200).  Specifically:

- **Winding:** (n_et, n_er) = (1, 2)
- **Mass:** m_e from F11 with L_ring_e calibrated (0.511 MeV)
- **Charge:** Q = e · n_et = +e... actually −e by the sign
  convention σ_e = −1 (so Q = −e · n_et = −e for n_et = +1)
- **4D spin:** ½ (Dirac spinor from per-sheet Dirac–Kähler)

The electron is a 4D Dirac spinor with mass m_e and charge −e.
All subsequent 4D physics (Dirac equation, Pauli reduction,
magnetic moment) treats it as a standard Dirac particle.

### B.2 — Substitute into §A.2 result

Plug Q = −e and m = m_e into the Pauli Hamiltonian:

$$
H_{\text{e}} \;=\; \frac{\vec{\pi}^{\,2}}{2 m_e} \;-\; e A_0^{\text{ext}}
\;+\;\frac{e\hbar}{2 m_e c}\,\vec{\sigma}\cdot\vec{B}^{\text{ext}}
$$

The magnetic moment operator is:

$$
\vec{\mu}_e \;=\; -g_e \cdot \frac{e}{2 m_e c} \cdot \vec{S}
\;=\; -g_e \cdot \frac{e\hbar}{4 m_e c}\,\vec{\sigma}
$$

with $g_e = 2$ from §A.2.  For a spin-up state
$\vec{S} = \frac{\hbar}{2}\hat{z}$:

$$
\mu_e \;=\; -g_e \cdot \frac{e\hbar}{4 m_e c} \;=\; -\frac{e\hbar}{2 m_e c}
\;=\; -\mu_B
$$

(one Bohr magneton, negative because the electron carries
negative charge).  **g_e = 2 derived at tree level.**

### B.3 — MaSt-specific confirmations

Two checks unique to MaSt's architecture:

1. **Winding independence.**  D7d's lemma F25 established that
   all KK modes are spin ½ regardless of winding (n_et, n_er).
   The Dirac equation with the F11 mass and F14 charge is
   therefore structurally the same for any (n_et, n_er) on the
   e-sheet; g = 2 follows for any single-sheet mode.  In
   particular, higher e-sheet modes (if excited, e.g., the
   muon under R53 resonance) would also have g = 2 at tree
   level — modifications come only from QED radiative
   corrections that depend on m/α ratios, not on the KK
   structure.

2. **Cross-shear independence.**  D6 F19 established that
   cross-shears enter the spectrum (mass formula) but not the
   centroid coupling to A_μ^ext.  Consequently, shear-induced
   corrections do not appear in the Pauli Hamiltonian's
   magnetic-moment term.  g_e = 2 is invariant under σ_ra
   (R60 Track 7) and cross-sheet σ perturbations at tree level.
   This check is formalized in §E.

### B.4 — Summary

The electron's tree-level magnetic moment **g_e = 2,
μ_e = 1 μ_B** follows directly from:

- The Dirac spinor structure given by D7d's per-sheet
  Dirac–Kähler
- The mass m_e from F11
- The charge Q = −e from F14/F15
- The standard Pauli reduction of §A.2

No MaSt-specific structure beyond the single-sheet Dirac
field is needed.  The 0.23% anomaly (g_e − 2 ≈ 0.00232) is
Schwinger 1948's QED radiative correction, inherited as-is.

---

## Section C — Proton case

### C.1 — Three-quark Z₃ composite structure

Under the (3, 6) interpretation (R60 Track 15 + Track 16), the
proton is a three-quark bound state on the p-sheet:

- **Constituents:** three (1, 2) quark modes on the p-sheet
- **Binding mechanism:** Z₃ phase alignment at 120° offsets
  (R60 Track 16 derivation from 2ω density cancellation)
- **Per-quark mass:** m_q = m_p / 3 ≈ 312.76 MeV (Track 15
  Option A calibration)
- **Per-quark spin:** ½ (D7d; each (1, 2) mode on the p-sheet
  is a Dirac spinor independent of winding)
- **Per-quark charge:** requires flavor assignment (see C.2)

The proton's total spin ½ emerges from SU(2) AM composition
of three spin-½ constituents (R60 Track 20 empirical
confirmation; D7d §E theoretical structure).  The specific
octet spin-½ realization (rather than decuplet spin-3/2)
requires a fully symmetric spin-flavor wavefunction under
SU(6), which is standard SU(6) quark-model content.

### C.2 — Quark charge assignments

The constituent quarks carry the fractional charges observed
in the Standard Model:

- u quark: Q_u = +(2/3)e
- d quark: Q_d = −(1/3)e

These u/d flavor charges are **imported inputs** at this
stage — MaSt's derivation of the u/d flavor split within the
(1, 2)-quark / (3, 6)-proton Z₃ architecture is an open
pool item.  For the purposes of this derivation, the charge
assignments are treated as inputs consistent with the
composite α rule (R60 Track 15):

- Proton = uud.  Total charge: Q_p = 2(+2/3) + (−1/3) = +1·e ✓
- Consistency with composite α rule: for the proton tuple
  (0, 0, 0, 0, 3, 6), α_sum_comp = n_et − n_pt/gcd + n_νt
  = 0 − 3/3 + 0 = −1, giving α_Coulomb = α.  This matches
  observed Q = 1 under the composite interpretation.

### C.3 — Per-quark Dirac magnetic moment

Each quark constituent is a 4D Dirac spinor with Q = Q_q and
m = m_q.  By the §A.2 Pauli reduction (applied per-quark), the
per-quark magnetic moment operator is

$$
\vec{\mu}_q \;=\; g \cdot \frac{Q_q}{2 m_q c} \cdot \vec{S}_q
\quad\text{with}\quad g = 2
$$

Evaluating the scalar magnetic moment (projection on the
positive-z direction with spin up):

$$
\mu_q \;=\; \frac{Q_q\hbar}{2 m_q c}
\;=\; Q_q \cdot \mu_{N,q}
\quad\text{where}\quad
\mu_{N,q} \equiv \frac{\hbar}{2 m_q c}
$$

In nuclear-magneton units ($\mu_N = e\hbar/(2 m_p c)$) with
$m_q = m_p / 3$:

$$
\mu_{N,q} \;=\; \frac{3 \hbar}{2 m_p c} \;=\; 3 \mu_N / e
$$

So per-quark moments in nuclear magnetons:

- $\mu_u = +(2/3) e \cdot 3 \mu_N / e = +2 \mu_N$
- $\mu_d = -(1/3) e \cdot 3 \mu_N / e = -\mu_N$

### C.4 — SU(6) spin-flavor composition (Beg–Lee–Pais 1964)

The proton is a totally symmetric spin-flavor wavefunction
under SU(6).  Writing the proton's J=½, m_J=+½ state with
the three quarks in the uud configuration:

$$
|p\uparrow\rangle \;=\; \frac{1}{\sqrt{18}}\Bigl[
2|u\uparrow u\uparrow d\downarrow\rangle
\;-\;|u\uparrow u\downarrow d\uparrow\rangle
\;-\;|u\downarrow u\uparrow d\uparrow\rangle
\;+\;\text{(permutations)}
\Bigr]
$$

(explicit form from Close 1979 §4.3; all 18 terms fully
symmetric.)  Computing the total magnetic moment in the
z-direction by summing each quark's contribution, weighted by
its spin state:

$$
\mu_p \;=\; \langle p\uparrow | \hat{\mu}_z | p\uparrow\rangle
$$

This is the Beg–Lee–Pais 1964 calculation.  The result reduces
to the single-line formula:

$$
\mu_p \;=\; \frac{4\,\mu_u \;-\;\mu_d}{3}
$$

Substituting the §C.3 values:

$$
\mu_p \;=\; \frac{4(+2 \mu_N) - (-\mu_N)}{3}
\;=\; \frac{8 \mu_N + \mu_N}{3}
\;=\; \frac{9 \mu_N}{3}
\;=\; 3 \mu_N
$$

In g-factor units ($\mu_p = g_p Q_p \hbar / (4 m_p c) =
g_p \mu_N / 2$):

$$
\boxed{\;\;g_p \;=\; \frac{2 \mu_p}{\mu_N} \;=\; 6 \;\;}
$$

**g_p = 6 at tree level, μ_p = 3 μ_N.**

### C.5 — Why the Beg–Lee–Pais formula is the right tree-level expression

The formula $\mu_p = (4\mu_u - \mu_d)/3$ follows directly from
summing per-quark magnetic moments weighted by the spin
probabilities that the fully symmetric SU(6) wavefunction
assigns.  Specifically:

- In the proton's spin-up state, the "up" quark is spin-up with
  probability 5/6 and spin-down with probability 1/6, giving an
  effective z-component of magnetic moment (5/6 − 1/6)·μ_u
  = (2/3)·μ_u per u quark.  There are two u quarks, so
  (4/3)·μ_u total.
- The "down" quark is spin-up with probability 1/3 and spin-
  down with probability 2/3, giving (1/3 − 2/3)·μ_d = −(1/3)·μ_d
  per d quark.  There is one d quark, so −(1/3)·μ_d total.
- Sum: (4/3)·μ_u − (1/3)·μ_d = (4 μ_u − μ_d)/3.

This spin-flavor structure is NOT derived here; it is imported
from standard SU(6) quark-model physics (Close 1979, Gell-Mann
1964 eightfold way).  MaSt's structural contribution is the
three-quark Z₃ binding (R60 Track 16); the SU(6) spin-flavor
is applied to that binding structure without modification.

### C.6 — Summary

The proton's tree-level magnetic moment **g_p = 6, μ_p = 3 μ_N**
follows from:

- The three-quark Z₃ composite structure derived in R60 Track 16
- Per-quark Dirac magnetic moment from §A.2 (standard tree-level
  Dirac result)
- SU(6) spin-flavor wavefunction (imported from Beg–Lee–Pais
  1964; MaSt's derivation of u/d flavor split is an open
  pool item)
- Constituent quark mass m_q = m_p/3 (Track 15 Option A
  calibration)

The ~7% anomaly (g_p ≈ 5.586 observed vs g_p = 6 tree-level)
is a strong-interaction correction outside Program 1's scope.

---

## Section D — Anomaly scope

Both g_e and g_p have observed values below the tree-level
predictions of §B and §C:

| Particle | Tree (this derivation) | Observed | Anomaly |
|----------|-----------------------:|---------:|--------:|
| electron | g_e = 2.0000000 | g_e = 2.00232 | +0.23% |
| proton | g_p = 6.0000000 | g_p = 5.586 | −6.9% |

### D.1 — Electron anomaly (QED radiative correction)

The electron anomaly g_e − 2 = α/(π) + higher-order terms is
Schwinger 1948's one-loop QED result, extended to ~10⁻¹² by
multi-loop calculations (Kinoshita et al.).  This calculation
uses only:

- 4D Dirac equation (same as our tree-level input)
- The charge e, mass m_e, and spin ½ as inputs
- Loop integrals in 4D Minkowski spacetime

The result is indifferent to the geometric origin of the
fields.  **MaSt inherits the QED anomaly as-is**; no MaSt-
specific modification to the Schwinger calculation is needed
at the α/(2π) order or beyond.

*Potential MaSt-specific correction.*  If the electron
sheet's KK tower has modes at masses significantly below the
electroweak scale, those modes might contribute additional
loop pieces to g − 2 beyond the standard QED value.  Whether
they do depends on:

- The spectrum of excited e-sheet modes (R53 generation
  resonance picture)
- Whether those modes carry unit charge and appropriate mass
  for loop weighting
- Phenomenological filters (R50 spin-statistics filter, R46
  waveguide cutoff)

This would be a phenomenological test — does MaSt predict
g − 2 consistent with the measured value? — and belongs to an
R-study (R44-adjacent), not to Program 1.

### D.2 — Proton anomaly (strong-interaction correction)

The proton anomaly g_p − 6 ≈ −0.414 (or μ_p − 3 ≈ −0.21 μ_N)
is much larger than the electron anomaly.  In the Standard
Model it is a consequence of:

- QCD corrections to the naive constituent-quark picture
  (the constituent quarks are not free; they are surrounded by
  sea quarks and gluons that modify the effective moments)
- SU(3) breaking effects between u and d constituent masses
- Relativistic corrections (v/c ~ 0.4 for quarks inside the
  proton)

In MaSt the analogous corrections would come from:

- Higher-order Z₃ dynamics beyond the pure 120° phase binding
  derived in R60 Track 16 (e.g., quark-quark interactions
  mediated by p-sheet ring excitations)
- Cross-sheet σ interactions (pool item h; zero in model-F
  baseline but conceivably active)
- Mass-mixing corrections from shear terms at higher order

The calculation of MaSt-specific proton corrections to g_p
would be a substantial research program paralleling lattice
QCD calculations of the proton moment.  It is explicitly
outside Program 1's scope; a future R-study could take this
up.

### D.3 — Summary on anomaly scope

**Track 11 derives tree-level g_e = 2 and g_p = 6 only.**
Observed anomalies are not addressed here.  For the electron,
the anomaly is fully covered by standard QED (Schwinger 1948
and higher-order calculations) and inherited into MaSt
unchanged.  For the proton, the anomaly would require a
higher-order Z₃ / strong-interaction calculation that is
beyond Program 1's scope.

---

## Section E — Cross-shear invariance check

### E.1 — Hypothesis

D6 F19 established that cross-shears g_45 (within a sheet) and
cross-sheet σ entries affect the mass spectrum but not the
centroid coupling to A_μ^ext.  The hypothesis for the magnetic
moment calculation: cross-shear terms should also not shift
g_e or g_p at tree level.  This section verifies the
hypothesis explicitly for the magnetic moment case.

### E.2 — Cross-shear terms to check

Three families of shear entries in MaSt's 11D metric need
checking:

1. **In-sheet shear g_45 = εs** (every sheet has this; R60 uses
   s_e = 2.004, s_p = 0.162, s_ν = 0.022).  Known from F19 to
   affect mass only.
2. **σ_ra = (sε)·σ_ta per sheet** (R60 Track 7 structural
   cancellation).  This is the ring-to-aleph coupling that
   cancels shear-induced α mode-dependence.
3. **Cross-sheet σ entries** (zero in model-F baseline but
   allowed in principle; pool item h).  Couplings between
   e-sheet, p-sheet, ν-sheet tube/ring indices.

### E.3 — Mechanism of the invariance

The Pauli Hamiltonian derived in §A.2 depends on:

- The mass m (from F7/F11, which IS mass-spectrum-dependent
  and affected by shears)
- The charge Q (from F14, which is the tube Killing momentum
  n_t; the ring contributions do not affect Q)
- The external field A_μ^ext acting on the 4D spacetime
  centroid

Cross-shears affect m (via the mass formula).  They do NOT
affect Q (which is determined by n_t alone).  They do NOT
affect the Pauli reduction (which is a 4D operation on the
Dirac equation).

**Crucially, the magnetic moment g-factor is determined by
the STRUCTURE of the Dirac representation, not by Q or m.**
The tree-level factor g = 2 falls out of the (σ·π)² identity,
which uses only the Pauli matrix algebra and not any
mass-dependent or shear-dependent quantity.

Therefore:

- Shear corrections shift m and hence μ = gQℏ/(4m) in the
  mass denominator.  This corresponds to a shift in the
  absolute magnetic moment, NOT in the g-factor.
- The g-factor itself is unchanged at tree level under any
  metric perturbation that preserves the Dirac representation.

### E.4 — Specific check for σ_ra

σ_ra is a ring-to-aleph metric entry derived in R60 Track 7.
It enters the 11D metric's inverse-determinant calculation for
α_Coulomb (via the tube↔ℵ↔t chain), NOT the minimal coupling
D_μ = ∂_μ − i(Q/ℏ)A_μ^ext to the external spacetime-sector
EM field.  The external A_μ^ext is a perturbation to the
spacetime block g_μν, not to the ℵ or Ma blocks.

**Result:** σ_ra does not shift g_e or g_p at tree level.

### E.5 — Specific check for cross-sheet σ entries

Cross-sheet σ entries (zero in model-F baseline) would mix
Ma windings between sheets, modifying the compound mass
spectrum.  They do not change the per-sheet Dirac-spinor
structure and do not modify the minimal coupling to the
external A_μ^ext.

**Result:** cross-sheet σ does not shift g_e or g_p at tree
level.

### E.6 — Summary

**Cross-shear invariance confirmed.**  MaSt's internal shears
(σ_ra, in-sheet shears g_45, cross-sheet σ) all shift the
mass spectrum but not the g-factor.  Tree-level magnetic
moments are:

- g_e = 2 on any e-sheet (ε, s) combination
- g_p = 6 for any Z₃-compatible three-quark proton structure,
  independent of p-sheet (ε, s) choice (Track 15 Option A or
  alternative magic-shear baselines)

This confirms the physical robustness of the tree-level
prediction.

---

## Lemma (Track 11 result)

We have shown:

> **(F34) Electron tree-level magnetic moment.**  Under
> per-sheet Dirac–Kähler (D7d) with minimal coupling to an
> external EM field (D6 F18), the electron (single-sheet (1, 2)
> mode on the e-sheet) has a magnetic moment given by the
> Pauli-reduction of the 4D Dirac equation with
> g_e = 2 exactly at tree level.  Specifically,
> μ_e = e ℏ / (2 m_e c) = 1 Bohr magneton.  The result is
> structural — g = 2 falls out of the Dirac representation's
> (σ·π)² identity with no free parameters.

> **(F35) Proton tree-level magnetic moment.**  Under the
> (3, 6) interpretation (R60 Track 15) with Z₃ confinement
> (R60 Track 16), the proton is a three-quark composite.
> Per-quark magnetic moments from F34 combine via the Beg–Lee–
> Pais 1964 SU(6) spin-flavor wavefunction to give
> μ_p = 3 μ_N exactly at tree level, equivalently g_p = 6.
> The result assumes u/d flavor charges (+2/3, −1/3) as
> imported inputs (MaSt's own u/d flavor derivation is an open
> pool item); constituent mass m_q = m_p/3 is from Track 15.

> **(F36) Cross-shear invariance of tree-level g.**  MaSt's
> internal shears — in-sheet g_45, ring-to-ℵ σ_ra (R60 Track
> 7), and cross-sheet σ entries — shift the mass spectrum but
> not the g-factor.  Tree-level g_e = 2 and g_p = 6 hold on
> any (ε, s) combination that yields a valid signature and
> correct masses.  Shear effects appear in the absolute
> magnitude (via m in μ = gQℏ/(4m)) but not in the
> dimensionless g.

F34–F36 establish the tree-level magnetic moments from Program
1's kinematic machinery plus the Z₃ and composite-α structure
developed in R60.  The observed anomalies (g_e − 2 ≈ 0.23%,
g_p − 6 ≈ −6.9%) are radiative/strong-interaction corrections
handled by standard QED (electron; inherited as-is) or a
future R-study paralleling lattice-QCD-style constituent
corrections (proton; outside Program 1).

This closes Program 1's kinematic arc: mass (F7/F11), charge
(F14/F15), Lorentz force (F17), spin (F25 via D7d), compound
modes (F25/F30), and magnetic moment (F34/F35) are all derived
from the photon-on-torus machinery introduced in Tracks 1–2
and extended through D7d and R60.  **Program 1's closeout
(pool z) can now proceed.**

---

## Open items

- **u/d flavor derivation.**  §C.2 imports Q_u = +2/3 and
  Q_d = −1/3 from the Standard Model.  MaSt does not yet
  derive the u/d flavor split within the (1, 2) quark / (3, 6)
  proton Z₃ architecture.  Open pool item, outside Program 1.
- **Higher-order Z₃ corrections to g_p.**  The ~7% proton
  anomaly (g_p = 5.586 observed vs 6 tree-level) is not
  derived here.  Future R-study could compute the MaSt
  equivalent of QCD corrections (Z₃ dynamics beyond the pure
  120° binding, quark-quark interactions mediated by p-sheet
  ring excitations).
- **MaSt-specific contributions to g_e − 2.**  If the e-sheet
  KK tower has significant modes below electroweak scales,
  loop contributions to g_e − 2 could shift the Schwinger
  prediction.  Phenomenological R-study, R44-adjacent.
- **Compound particles with spin ≠ ½.**  For 2-sheet mesons
  (spin 0 or 1) and 3-sheet baryons other than the proton
  (spin ½ octet or spin 3/2 decuplet), analogous magnetic-
  moment calculations would follow the same pattern
  (per-sheet Dirac spinor + SU(6) combinatorics).  Not part of
  Program 1's closeout but a natural extension.

---

## Program 1 closeout

With F34–F36 established, Program 1's kinematic arc is
complete:

- **D1–D6:** mass, charge, Lorentz force on a single sheet
- **D7 (resolved by D7d):** spin from per-sheet Dirac–Kähler
- **D8–D10:** compound modes on T⁴ and T⁶
- **D11 (this):** magnetic moment at tree level

The electron's four quantum numbers (mass, charge, spin,
magnetic moment) are now all derived from the photon-on-torus
starting point with no free parameters beyond the compact
scale.  The proton's corresponding numbers are derived under
the (3, 6) Z₃-confinement interpretation from R60.

Program 1 closeout (pool z) can now synthesize Tracks 1–11
into a unified narrative / primer.  The remaining open items
(u/d flavor, higher-order corrections, MaSt-specific
radiative contributions) belong to later programs.
