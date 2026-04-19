# Derivation 5 — Charge identification

Show that the conserved Killing momentum P_4 of F4 (the one in
the **tube** direction, by Track 4's convention) is the
**electric charge** Q of the projected 4D particle, when one
additional convention is adopted: among the two gauge potentials
that the 2-torus generates (F4 A.3), only the **tube**
gauge potential is physical; the **ring** gauge potential
vanishes.  Show that with standing-wave quantization, Q is
automatically integer-quantized.  Sketch the extension to
MaSt's three-sheet T⁶ setup that recovers the empirical
universal charge formula Q = −n₁ + n₅.

This is the **charge counterpart** of Track 4 (mass).  Together
they give the full mass-and-charge picture of the
"electron-from-light" hypothesis on a single sheet.  Magnetic
moment, spin, and the multi-sheet bookkeeping are subsequent
work.

---

## Inputs

1. **F4** (U(1)×U(1) gauge structure on a 2-torus): two gauge
   potentials A_μ ≡ A⁴_μ and B_μ ≡ A⁵_μ from the off-diagonal
   metric entries G_μa = g_ab A^b_μ; two conserved Killing
   momenta P_4 and P_5.
2. **F5** (two-charge Lorentz force): the projected 4D
   geodesic includes a Lorentz-force term with two distinct
   charges Q_A and Q_B coupling to two distinct field
   strengths F^A_μν and F^B_μν.
3. **F11** (Track 4 convention): index 4 is "tube" (smaller
   compact period L_t), index 5 is "ring" (larger compact
   period L_r = ε L_t), with the parametrization
   g_44 = ε², g_55 = 1/ε² + s², g_45 = ε s, det g = 1.
4. **Standing-wave quantization** (F4 D.4): P_a = n_a h / L_a
   with n_a ∈ ℤ.

One additional convention will be introduced and motivated in
Section B:

5. **Tube-couples convention**: the ring gauge potential
   vanishes, B_μ ≡ A⁵_μ = 0.  Equivalently: the only physical
   gauge potential the 2-torus generates is the one associated
   with the tube isometry ∂/∂x⁴.

---

## Section A — The two-charge starting point (recap)

### A.1 — Two gauge potentials, two conserved momenta

> *Purpose: restate the F4–F5 picture in the form needed for
> this derivation.*

From F4 A.2–A.3, the 6D KK metric on M⁴ × T² has off-diagonal
spacetime↔compact entries

<!-- G_μa = g_ab A^b_μ  with  A^4_μ = A_μ,  A^5_μ = B_μ -->
$$
G_{\mu a} \;=\; g_{ab}\,A^{b}{}_{\mu},
\qquad
A^{4}{}_{\mu} \;\equiv\; A_{\mu},
\qquad
A^{5}{}_{\mu} \;\equiv\; B_{\mu},
$$

so the two compact directions each generate their own U(1)
gauge potential.  From F4 D.2, the cylinder condition makes
∂/∂x⁴ and ∂/∂x⁵ Killing vectors of G_AB, yielding two
conserved momenta on any geodesic:

<!-- P_a = g_ab w^b,  w^b ≡ A^b_ν ẋ^ν + ẋ^b -->
$$
P_{a} \;=\; g_{ab}\,w^{b},
\qquad
w^{b} \;\equiv\; A^{b}{}_{\nu}\,\dot{x}^{\nu} \;+\; \dot{x}^{b}.
$$

So far, completely symmetric between a = 4 and a = 5.

### A.2 — The Lorentz force

> *Purpose: recall the form in which F5 cast the two charges
> as physical objects.*

From F5 (derivation-2 E.4), the projected 4D geodesic of a
massive particle on the 2-torus has the form

<!-- d²x^μ/dτ² + (4D Christoffel) = -(Q_A F^Aμ_ν + Q_B F^Bμ_ν) ẋ^ν / m + corrections -->
$$
m\,\frac{d^{2}x^{\mu}}{d\tau^{2}}
\;+\; (\text{4D Christoffel terms})
\;=\; -\!\left(Q_{A}\,F^{A\,\mu}{}_{\nu} \;+\; Q_{B}\,F^{B\,\mu}{}_{\nu}\right)\!\dot{x}^{\nu}
\;+\; \text{(corrections)},
$$

with charges identified as Q_A ∝ P_4 and Q_B ∝ P_5 (F4 D.3),
and field strengths F^A_μν = ∂_μ A_ν − ∂_ν A_μ (similarly
F^B for B_μ).

Two charges, two forces.  Both quantized via F4 D.4.  This is
the starting point.

---

## Section B — The tube-couples convention

### B.1 — Statement

> *Purpose: state the one new ingredient of this derivation.*

We adopt the convention

<!-- B_μ ≡ A^5_μ ≡ 0 -->
$$
\boxed{\;B_{\mu} \;\equiv\; A^{5}{}_{\mu} \;\equiv\; 0\;}
$$

The ring direction (index 5) does not generate a physical
gauge potential.  Only the tube direction (index 4) does:
A_μ ≡ A⁴_μ remains a free spacetime vector field.

This is *not* a derived consequence of F4–F11.  It is a
**convention** (or equivalently an empirical input): the
choice of how many of the two U(1) gauge potentials are
realized as observable forces in 4D.

### B.2 — Geometric meaning: which compact direction the
spacetime sector "talks to"

> *Purpose: explain what the convention is geometrically saying.*

The Track 4 basis on the 2-torus is fixed by the mass
formula: index 4 is tube (smaller compact period L_t), index 5
is ring (larger compact period L_r = ε L_t).  In this fixed
basis, B.1 says that the off-diagonal G_μ5 entries — which would
encode a second physical gauge field tied to the ring isometry
— are absent.

Geometrically, the only way the spacetime sector knows about
the compact dimensions is through the tube: variations of the
4D metric across spacetime are coupled to motion along the tube
direction (via A_μ = A⁴_μ), but **not** to motion along the
ring direction.  Particles can move freely along the ring
without being deflected by any 4D field.

Note that even with B_μ = 0, the spacetime↔compact metric
entry G_μ5 is generally nonzero:

<!-- G_μ5 = g_45 A^4_μ + g_55 A^5_μ = g_45 A_μ  (B_μ = 0 case) -->
$$
G_{\mu 5}
\;=\; g_{45}\,A^{4}{}_{\mu} \;+\; g_{55}\,A^{5}{}_{\mu}
\;=\; g_{45}\,A_{\mu}
\quad\;\;\text{(when }B_{\mu} = 0\text{)}.
$$

Whenever the **internal shear** g_45 = ε s is nonzero, motion
along the ring is still mixed with spacetime via the *same*
A_μ that couples to the tube.  This is a kinematic consequence
of the shear and was already discussed in F6: pure-Q_B
eigenstates have nonzero w⁴ and vice versa.  The convention
B_μ = 0 only zeros the *independent* second gauge field; it
does not zero the shear-induced cross-coupling.

### B.3 — Empirical motivation

> *Purpose: justify why this is the right convention.*

Three converging reasons:

(i) **Only one EM force is observed.**  Experimentally, all
4D charged particles couple to a single electromagnetic gauge
field (the photon's A_μ).  There is no observed second long-
range vector force tied to a "ring charge."  If both U(1)s
were realized, we would expect a second photon coupled to
ring-direction quantum numbers — a Maxwellian "U(1)_B" with
its own Coulomb law.  No such force has ever been detected.

(ii) **Basis choice.**  The 2-torus has a continuous basis-
choice freedom (rotations and rescalings on the compact 2D
plane).  In a generic basis, both A⁴_μ and A⁵_μ might be
nonzero.  An SO(2) rotation on the (4, 5) basis can always
diagonalize the spacetime↔compact coupling so that all of the
gauge content lives in one direction (call it 4) and none in
the orthogonal direction (call it 5).  This rotation, however,
also mixes the internal metric g_ab; in particular, the Track 4
basis (where g_44 = ε², g_55 = 1/ε² + s², g_45 = εs takes the
canonical MaSt form) is *not* the same as the basis where
A⁵_μ = 0 unless we make it so by hand.  The convention B.1
should therefore be read as: **the basis fixed by the mass
formula and the basis that diagonalizes the spacetime coupling
are taken to be the same basis.**  This is the operational
content of "tube carries mass *and* charge in MaSt."

(iii) **Asymmetric content.**  The ring direction in Track 4
has the specific role of carrying the "n_r − s n_t" combination
in the mass formula.  Its physical signature is mass
contribution.  The tube has the role of carrying the n_t/ε
contribution to mass.  The convention B.1 assigns the
*additional* role of carrying charge to the tube only.  Mass
and charge thus emerge from different aspects of the same two
compact directions: mass from both, charge from only the tube.

### B.4 — Consequence: U(1)×U(1) collapses to U(1)

> *Purpose: trace through the algebraic consequences of B.1.*

With B_μ = 0:

- The field strength of the second gauge field vanishes:
  F^B_μν = ∂_μ B_ν − ∂_ν B_μ = 0.
- The Lorentz force in A.2 reduces from two terms to one:

<!-- m d²x^μ/dτ² + ... = -Q_A F^A μ_ν ẋ^ν + corrections -->
$$
m\,\frac{d^{2}x^{\mu}}{d\tau^{2}}
\;+\; (\text{4D Christoffel})
\;=\; -\,Q_{A}\,F^{A\,\mu}{}_{\nu}\,\dot{x}^{\nu}
\;+\; \text{(corrections)}.
$$

There is now a single physical 4D gauge field, F^A_μν, and a
single physical 4D charge, Q_A.  This is the electromagnetic
U(1).

---

## Section C — Charge from the surviving U(1)

### C.1 — The single physical gauge potential

> *Purpose: name the surviving object as "the electromagnetic
> potential."*

After the convention B.1, the off-diagonal spacetime↔compact
entries reduce to

<!-- G_μ4 = g_44 A_μ  (tube),   G_μ5 = g_45 A_μ  (ring, shear-induced) -->
$$
G_{\mu 4} \;=\; g_{44}\,A_{\mu}
\;=\; \varepsilon^{2}\,A_{\mu},
\qquad
G_{\mu 5} \;=\; g_{45}\,A_{\mu}
\;=\; \varepsilon\,s\,A_{\mu},
$$

where the second equalities use the Track 4 parametrization
(F11).  Both nonzero, both proportional to the *same* A_μ.

Define the **electromagnetic potential** as

<!-- A_μ^EM ≡ A_μ  (up to a normalization constant set by the charge unit) -->
$$
A_{\mu}^{\text{EM}} \;\equiv\; A_{\mu}
\quad (\text{up to an overall normalization, fixed in C.4}).
$$

The corresponding field strength F_μν^EM = ∂_μ A_ν − ∂_ν A_μ is
the unique physical 4D gauge field on the 2-torus after the
convention B.1 is imposed.

### C.2 — The Killing momentum P_4 with B_μ = 0

> *Purpose: write out the conserved Killing momentum on which
> the surviving Lorentz force depends.*

From A.1 with B_μ = A⁵_μ = 0, the gauge-covariant compact
velocities become

<!-- w^4 = A_μ ẋ^μ + ẋ^4,  w^5 = ẋ^5 -->
$$
w^{4} \;=\; A_{\mu}\,\dot{x}^{\mu} \;+\; \dot{x}^{4},
\qquad
w^{5} \;=\; \dot{x}^{5}.
$$

The conserved Killing momentum in the tube direction is

<!-- P_4 = g_44 w^4 + g_45 w^5 = ε² (A_μ ẋ^μ + ẋ^4) + ε s ẋ^5 -->
$$
P_{4}
\;=\; g_{44}\,w^{4} \;+\; g_{45}\,w^{5}
\;=\; \varepsilon^{2}\!\left(A_{\mu}\,\dot{x}^{\mu} + \dot{x}^{4}\right)
\;+\; \varepsilon\,s\,\dot{x}^{5}.
$$

In the ring direction:

<!-- P_5 = g_45 w^4 + g_55 w^5 = ε s (A_μ ẋ^μ + ẋ^4) + (1/ε² + s²) ẋ^5 -->
$$
P_{5}
\;=\; g_{45}\,w^{4} \;+\; g_{55}\,w^{5}
\;=\; \varepsilon\,s\!\left(A_{\mu}\,\dot{x}^{\mu} + \dot{x}^{4}\right)
\;+\; \left(\tfrac{1}{\varepsilon^{2}} + s^{2}\right)\!\dot{x}^{5}.
$$

Both are conserved.  P_4 couples to A_μ explicitly (the ẋ^μ
term is multiplied by A_μ); P_5 couples only via the
shear-induced cross-term (proportional to εs × A_μ ẋ^μ),
which vanishes when s = 0.

### C.3 — Identifying Q with P_4

> *Purpose: connect P_4 to "the charge that the Lorentz force
> sees."*

The Lorentz-force term in B.4 was

$$
\text{Lorentz force per unit mass}
\;=\; -\,(Q_A / m)\,F_{\mu\nu}\,\dot{x}^{\nu}.
$$

By F5's identification (F4 D.3), Q_A is proportional to the
conserved Killing momentum P_4:

<!-- Q_A = P_4 / (charge units factor) -->
$$
Q_{A} \;=\; \frac{P_{4}}{e_{0}},
$$

where e_0 is a units factor that converts momentum to charge.
Both Q_A and P_4 are conserved along the geodesic; both are
quantized integer multiples of h/L_t (by F4 D.4).

Define the physical electric charge as

<!-- Q ≡ Q_A = P_4 / e_0 -->
$$
\boxed{\;Q \;\equiv\; Q_{A} \;=\; \frac{P_{4}}{e_{0}}\;}
$$

### C.4 — Standing-wave quantization gives Q = e × n_t

> *Purpose: show that Q is automatically integer-quantized in
> units of an elementary charge e.*

By F4 D.4 (standing-wave quantization), the conserved compact
momenta are integer multiples of the inverse compact period:

<!-- P_a = n_a h / L_a -->
$$
P_{a} \;=\; \frac{n_{a}\,h}{L_{a}}.
$$

For the tube direction (a = 4, L_4 = L_t per F11):

<!-- P_4 = n_t h / L_t -->
$$
P_{4} \;=\; \frac{n_{t}\,h}{L_{t}}.
$$

Substituting into C.3:

<!-- Q = (h / (L_t e_0)) × n_t  =  e × n_t,  with  e ≡ h/(L_t e_0) -->
$$
Q \;=\; \left(\frac{h}{L_{t}\,e_{0}}\right) n_{t}
\;\equiv\; e \times n_{t},
\qquad
e \;\equiv\; \frac{h}{L_{t}\,e_{0}}.
$$

So **the electric charge of the projected particle is automatically
quantized in integer units of an elementary charge e**, with e
fixed by the tube period L_t and the units factor e_0.

### C.5 — The elementary charge unit

> *Purpose: discuss what e is and what determines it.*

The numerical value of e depends on two ingredients:

- The **tube period L_t**, set by the geometry of the sheet
  (related to the Compton wavelength of the lightest mode on
  that sheet — see Track 4 D.1).
- The **units factor e_0**, set by the choice of conventions
  for the gauge potential A_μ and the periodicity of x⁴.  In
  conventional KK with x⁴ ∈ [0, L_t), one finds (primer §10)
  e_0 = L_t / √(8π G), giving e = h √(8π G) / L_t² for the
  natural Newton-constant normalization.

The resulting elementary charge e is what GRID ultimately ties
to the fine-structure constant α (see R44, R49 for the GRID
side).  Within Program 1, we treat e as a *given* — a
geometric quantity set by L_t and the GRID-derived unit
conventions.  The result of *this* derivation is **charge
quantization** (Q = integer × e) and the **identification of Q
with P_4** — independent of what specific value e takes.

---

## Section D — The "dark" P_5

### D.1 — P_5 is still conserved

> *Purpose: clarify that the convention B.1 doesn't break a
> conservation law.*

The Killing-vector argument of F4 D.2 only requires that the
metric be independent of x⁵ (the cylinder condition).  Whether
the gauge potential A⁵_μ is zero or nonzero is irrelevant to
the existence of the Killing vector ∂/∂x⁵ — that vector is
generated by translations along x⁵, and the metric's
x⁵-independence guarantees its Killing property.

Therefore **P_5 remains a conserved quantity** even when
B_μ = 0:

<!-- P_5 = g_45 w^4 + g_55 w^5  is still conserved -->
$$
\frac{dP_{5}}{d\tau} \;=\; 0
\quad\text{regardless of whether } B_{\mu} = 0 \text{ or not.}
$$

### D.2 — But P_5 has no Lorentz-force partner

> *Purpose: spell out what changes when B_μ = 0.*

The Lorentz force in F5 was Q_A F^A + Q_B F^B.  With B_μ = 0,
the second field strength vanishes (B.4), and so the Q_B F^B
term disappears.  The conserved P_5 — which would have been
identified as Q_B in F4 D.3 — now has no electromagnetic
field to push it around.

Operationally: a particle with nonzero P_5 carries a conserved
quantity, but that quantity does not couple to any 4D long-
range force.  No Coulomb-like potential, no second photon, no
observable signature in 4D EM experiments.

### D.3 — P_5 contributes to mass (via F11)

> *Purpose: state what P_5 *does* show up in.*

Even though P_5 is electromagnetically invisible, it still
appears in the mass formula F7:

<!-- m²c² = h^ab P_a P_b  involves both P_4 and P_5 -->
$$
m^{2}\,c^{2}
\;=\; h^{ab}\,P_{a}\,P_{b}
\;=\; h^{44}\,P_{4}^{\,2}
\;+\; 2\,h^{45}\,P_{4}\,P_{5}
\;+\; h^{55}\,P_{5}^{\,2}.
$$

With the F11 parametrization, P_5 = n_r h/L_r enters the
"ring" contribution (n_r − s n_t)² to MaSt's mass formula.
A particle with n_r ≠ 0 and n_t = 0 has nonzero mass but zero
electric charge — it is a "neutral massive ring excitation."

### D.4 — Interpretation: a hidden quantum number

> *Purpose: spell out the physical interpretation.*

P_5 is a *hidden conservation law*: a strictly conserved
quantity with no electromagnetic signature.  It contributes to
inertial mass and to the discrete particle spectrum, but
particles with the same total mass and total electric charge
but different P_5 are degenerate as far as 4D EM physics is
concerned.

This is qualitatively similar to flavor in the Standard Model
(electron, muon, tau all have charge −e but differ in lepton-
flavor quantum numbers), or to the strong/weak isospin
distinctions that are invisible to electromagnetism.  In MaSt
language, the n_r quantum numbers across sheets are the seeds
of generation structure, where the mass formula's
"(n_r − s n_t)²" term is the generation-splitting mechanism
identified empirically in R49 / R53.

---

## Section E — Recovery of MaSt's universal charge formula

### E.1 — Generalization to T⁶ = T² × T² × T²

> *Purpose: extend the single-sheet result to MaSt's three-
> sheet setup.*

MaSt has three 2-tori (electron, neutrino, proton sheets),
giving a six-dimensional internal manifold T⁶ = T² × T² × T²
(no cross-shears between sheets at this level — those are
treated in a separate derivation).  Each sheet has its own
Track 4 internal metric:

| Sheet | Tube index | Ring index | Aspect ratio | Shear |
|-------|------------|------------|--------------|-------|
| Electron (e) | 1 | 2 | ε_e | s_e |
| Neutrino (ν) | 3 | 4 | ε_ν | s_ν |
| Proton (p) | 5 | 6 | ε_p | s_p |

(MaSt's index labels: tubes are odd indices 1, 3, 5; rings are
even indices 2, 4, 6.  This is just relabeling of "4 ↔ tube,
5 ↔ ring" three times in parallel.)

### E.2 — Six conserved Killing momenta

> *Purpose: extend F4 D.2 to T⁶.*

The cylinder condition gives one Killing vector per compact
direction, hence **six** conserved Killing momenta:

<!-- {P_1, P_2, P_3, P_4, P_5, P_6} -->
$$
\{P_{1},\, P_{2},\, P_{3},\, P_{4},\, P_{5},\, P_{6}\}
\quad
\text{(all conserved on any geodesic)}.
$$

By the Track 5 convention (B.1) applied to each sheet, only
the *tube* momenta couple to gauge fields:

- P_1 (electron tube) — couples to a gauge field A^1_μ.
- P_3 (neutrino tube) — couples to a gauge field A^3_μ.
- P_5 (proton tube) — couples to a gauge field A^5_μ.
- P_2, P_4, P_6 (rings) — conserved but dark (D.1–D.4).

So the U(1)⁶ that the cylinder condition might naively suggest
collapses to U(1)³ by the per-sheet convention.

### E.3 — Per-sheet Ma–S coupling sign assignments

> *Purpose: state the empirical inputs that further reduce
> U(1)³ → U(1)¹.*

MaSt's empirical input: the three tube gauge fields are not
independent.  They are all proportional to a *single* physical
electromagnetic potential A_μ:

<!-- A^a_μ = σ_a × A_μ,  with σ_e = -1, σ_ν = 0, σ_p = +1 (in normalized units) -->
$$
A^{1}{}_{\mu} \;=\; \sigma_{e}\,A_{\mu},
\qquad
A^{3}{}_{\mu} \;=\; \sigma_{\nu}\,A_{\mu},
\qquad
A^{5}{}_{\mu} \;=\; \sigma_{p}\,A_{\mu},
$$

with **per-sheet Ma–S coupling signs**

<!-- σ_e = -1,  σ_ν = 0,  σ_p = +1   (in units where |σ| = 1 sets the elementary charge) -->
$$
\sigma_{e} \;=\; -1, \qquad
\sigma_{\nu} \;=\; 0, \qquad
\sigma_{p} \;=\; +1.
$$

Three remarks:

(i) **The neutrino sheet is electrically neutral (σ_ν = 0).**
    No matter how excited the neutrino-sheet tube winding n_3
    is, the corresponding gauge potential A^3_μ vanishes
    identically.  Neutrino-sheet excitations carry no charge
    by construction.

(ii) **The electron and proton sheets carry opposite charges
    (σ_e = −σ_p) of equal magnitude.**  This is the geometric
    encoding of "the proton's charge is exactly +e and the
    electron's is exactly −e."  In MaSt, the equality of
    magnitudes is *imposed* via |σ_e| = |σ_p|; the equality is
    what makes hydrogen electrically neutral.

(iii) **These sign assignments are inputs to MaSt, not derived
    here.**  Why σ_e = −σ_p exactly (rather than, say,
    σ_e = −0.99 σ_p) is a question outside the scope of this
    derivation — MaSt currently postulates the exact equality
    based on the empirical observation that hydrogen is
    neutral to one part in 10²¹ (and similar tests).

### E.4 — Single physical EM gauge potential

> *Purpose: see how the three tube gauge fields collapse to
> one physical A_μ.*

Substituting E.3 into the gauge-covariant velocities:

<!-- w^1 = σ_e A_μ ẋ^μ + ẋ^1,  w^3 = σ_ν A_μ ẋ^μ + ẋ^3 = ẋ^3,  w^5 = σ_p A_μ ẋ^μ + ẋ^5 -->
$$
w^{1} = \sigma_{e}\,A_{\mu}\dot{x}^{\mu} + \dot{x}^{1},
\quad
w^{3} = \dot{x}^{3},
\quad
w^{5} = \sigma_{p}\,A_{\mu}\dot{x}^{\mu} + \dot{x}^{5}.
$$

Only A_μ appears as a 4D field — there is just one
electromagnetic potential to which the various sheets couple
with strengths σ_e, 0, σ_p.

### E.5 — The universal charge formula Q = −n_1 + n_5

> *Purpose: assemble the per-sheet contributions into the
> single physical charge.*

The Lorentz force on a multi-sheet particle (one with nonzero
windings on multiple sheets) couples to A_μ with a coefficient
that is the sum of the per-sheet contributions.  Specifically,
a particle with conserved tube momenta (P_1, P_3, P_5) and
sheet couplings (σ_e, σ_ν, σ_p) experiences a Lorentz force

<!-- Lorentz coefficient = (σ_e P_1 + σ_ν P_3 + σ_p P_5)/m -->
$$
\text{4D charge that A_μ sees}
\;=\; \sigma_{e}\,Q_{1} \;+\; \sigma_{\nu}\,Q_{3} \;+\; \sigma_{p}\,Q_{5}
$$

where Q_1, Q_3, Q_5 are the per-sheet charges from C.3 applied
to each sheet's tube.  Substituting E.3 (σ_e = −1, σ_ν = 0,
σ_p = +1) and C.4 (Q_a = e × n_a for the tube on each sheet,
with e the common elementary charge — see C.5 for what fixes
this):

<!-- Q = -e n_1 + 0 + e n_5 = e × (-n_1 + n_5) -->
$$
\boxed{\;
Q \;=\; e\!\left(-n_{1} + n_{5}\right)
\;}
$$

In the natural units where e = 1 (the elementary charge sets
the scale), this is **MaSt's universal charge formula**

<!-- Q = -n_1 + n_5 -->
$$
Q \;=\; -n_{1} + n_{5}.
$$

The neutrino-sheet tube quantum n_3 does not appear because
σ_ν = 0.  All four "ring" quantum numbers (n_2, n_4, n_6) do
not appear because of the per-sheet tube-couples convention
(Section B applied to each sheet).  Charge is a property of
the **tube windings** of the **electron and proton sheets**
only.

---

## Section F — What this establishes

### F.1 — Charge is the tube-direction Killing momentum

> *Purpose: state the central claim of this derivation.*

Electric charge Q is **identified** with the conserved Killing
momentum P_tube of the tube compact direction (the smaller of
the two on each 2-torus), not derived from any spinor or
group-representation argument.  Charge quantization (Q is an
integer multiple of an elementary charge e) is automatic from
the standing-wave boundary condition on the tube — single-
valuedness of the wavefunction across one tube circumference.

The sign of Q for a single excitation is the sign of n_tube
(matter vs. antimatter).  The magnitude is |n_tube|.

### F.2 — Universality and matter/antimatter symmetry

> *Purpose: connect to MaSt's empirical observation.*

The universal formula Q = −n_1 + n_5 reproduces:

- **Lepton vs. baryon distinction**: leptons are pure electron-
  sheet excitations (n_1 ≠ 0, n_5 = 0); baryons are pure
  proton-sheet excitations (n_1 = 0, n_5 ≠ 0).  Mixed
  excitations are compound modes (treated separately).
- **Particle/antiparticle symmetry**: (n_1, n_3, n_5) →
  (−n_1, −n_3, −n_5) flips Q → −Q, with all three ring
  quanta (n_2, n_4, n_6) likewise flipped.  This is just the
  natural ℤ₂ symmetry of the integer lattice underlying MaSt.
- **Hydrogen neutrality**: the simplest atomic compound
  (one electron + one proton) has total Q = (−1) + (+1) = 0
  exactly, with no per-sheet adjustment.
- **Neutrino neutrality**: a pure neutrino excitation has
  n_1 = n_5 = 0, hence Q = 0 regardless of n_3.

### F.3 — Charge quantization is geometric, not quantum-
mechanical

> *Purpose: emphasize the structural origin.*

In the Standard Model, charge quantization is an unexplained
empirical fact (or, in some GUT extensions, a consequence of
group-theoretic embedding).  Here it follows directly from
the topology of the compact dimension: a wavefunction must be
single-valued around any closed loop, so the momentum along
that loop is restricted to integer multiples of h/L.  No
additional quantum-mechanical structure is needed beyond the
Planck–Einstein relation that's already in F1 and F7.

### F.4 — What is *not* derived here

This derivation pins down:

- Charge quantization (Q = e × n_t).
- Identification of Q with P_tube.
- The role of the per-sheet Ma–S coupling signs in giving
  Q = −n_1 + n_5.

It does **not** determine:

- The numerical value of e (or equivalently, of α).  This is
  set by L_t and the GRID-derived units factor e_0.  GRID
  derives α; this derivation just identifies which geometric
  quantity is "the elementary charge."
- The sign assignment σ_e = −σ_p exactly.  This is taken as
  an empirical input from MaSt; deriving it from a deeper
  symmetry (matter/antimatter, charge conjugation) is open.
- Why the neutrino sheet has σ_ν = 0 specifically.  This is
  the empirical input "neutrinos are electrically neutral."
  Whether σ_ν = 0 follows from a geometric feature of the
  neutrino sheet (e.g., the fact that R49 finds ε_ν = 5.0
  and a special shear value 0.022) is open.
- The full multi-sheet charge formula in the presence of
  inter-sheet cross-shears (which would add new off-diagonal
  terms across sheets).  The current derivation handles three
  independent 2-tori; the cross-sheared case is treated
  separately.

---

## Lemma (Track 5 result)

We have shown:

> **(F14) Charge from the tube Killing momentum.**  Under the
> tube-couples convention B_μ ≡ A⁵_μ ≡ 0, the conserved Killing
> momentum P_4 in the tube direction (on a single 2-torus) is
> proportional to the electric charge Q seen by the surviving
> 4D Lorentz force.  Standing-wave quantization makes Q an
> integer multiple of an elementary charge e set by the tube
> period:
>
> $$
> Q \;=\; e \times n_{t},
> \qquad
> e \;=\; \frac{h}{L_{t}\,e_{0}},
> \qquad
> n_{t} \;\in\; \mathbb{Z}.
> $$
>
> **(F15) Universal charge formula on T⁶.**  Extending the
> tube-couples convention to all three MaSt sheets and applying
> the per-sheet Ma–S sign assignments σ_e = −1, σ_ν = 0,
> σ_p = +1 reduces the U(1)⁶ that T⁶'s cylinder condition
> would naively imply to a single physical electromagnetic
> U(1).  The conserved electric charge of any 4D-projected
> particle is
>
> $$
> Q \;=\; e\!\left(-n_{1} + n_{5}\right),
> $$
>
> matching MaSt's empirically-found universal formula across
> leptons, baryons, and atomic compounds.
>
> **(F16) Dark conservation laws.**  The convention B_μ = 0
> does **not** break the Killing-momentum conservation of P_5
> (or, in the multi-sheet case, of P_2, P_4, P_6).  These ring
> momenta remain conserved but couple to no 4D field.  They
> contribute to mass (via F7) and to the discrete particle
> spectrum (the "(n_r − s n_t)" term of F11), and so they
> participate in determining which particles exist and what
> their mass and quantum numbers are — but they are
> electromagnetically invisible.  This is the geometric
> origin of "non-electromagnetic quantum numbers" in MaSt:
> generation labels, lepton-family structure, baryon number,
> and similar conserved-but-dark quantities.

F14–F16 complete the **mass-and-charge** picture of the
electron-from-light hypothesis on a single sheet, with the
multi-sheet generalization mechanically following the same
pattern.  What remains for the full electron is spin and the
magnetic moment (gated by spin).
