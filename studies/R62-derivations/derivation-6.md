# Derivation 6 — Lorentz force on the standing-wave state

Show that a standing-wave eigenstate of the photon-on-2-torus
(the 4D-projected particle defined by Tracks 3–5), placed in a
weak external electromagnetic field, has a centroid that obeys
the standard relativistic Lorentz-force equation

<!-- m d²x^μ/dτ² = Q F^μ_ν^(ext) ẋ^ν -->
$$
m\,\frac{d^{2}x^{\mu}}{d\tau^{2}}
\;=\; Q\,F^{\mu}{}_{\nu}^{\text{(ext)}}\,\dot{x}^{\nu},
$$

with **the same** m derived in Track 4 (m² c² = h^ab P_a P_b)
and **the same** Q derived in Track 5 (Q = e n_t).  No new
parameters are introduced.

This is the operational closure of the single-sheet
"electron from light" arc.  Earlier tracks established mass
and charge as separate properties of the eigenstate.  This
derivation shows that the **same algebra** that produced m
and Q also produces the coupling between them — i.e., that
m and Q are not just labels but the inertial coefficient and
charge coefficient of an actual 4D charged particle.

---

## Inputs

In addition to the inputs of derivations 1–5:

1. **F4** (Track 2): U(1)×U(1) gauge structure on M⁴ × T²,
   metric ansatz G_AB = [g_μν + g_ab A^a_μ A^b_ν, g_ab A^b_μ;
   g_ab A^a_ν, g_ab], inverse blocks G^μν = g^μν,
   G^μa = −A^aμ, G^ab = h^ab + A^a_μ A^bμ, conserved
   compact momenta P_a = g_ab w^b.
2. **F7** (Track 3): photon-on-2-torus mass formula
   m²c² = h^ab P_a P_b.
3. **F11–F13** (Track 4): the (ε, s) parametrization of the
   internal metric.
4. **F14** (Track 5): under the tube-couples convention
   B_μ ≡ A^5_μ ≡ 0, Q = e × n_t with
   e = h / (L_t e_0).
5. **The 6D massless Klein–Gordon equation**
   G^AB ∂_A ∂_B Ψ = 0 (treated as the field-theoretic
   version of the Planck–Einstein photon used in F1 and F7;
   the only quantum input beyond those already in use).
6. **An external electromagnetic 4-potential A_μ^ext(x)**, with
   field strength F_μν^ext ≡ ∂_μ A_ν^ext − ∂_ν A_μ^ext.
   "External" means: produced by sources outside the
   particle of interest (e.g. a laboratory capacitor /
   solenoid); it depends only on x^μ, not on x^4 or x^5.
7. **The weak-field assumption**: A_μ^ext is small compared
   to the natural internal scales (specifically, |q A_μ^ext| ≪
   |compact momentum quanta|) and varies slowly in spacetime
   (length scales ≫ L_t, L_r).
8. **The eikonal / WKB limit** as the standard tool for
   extracting classical centroid trajectories from a wave
   equation.

Conventions: signature (−, +, +, +, +, +); index ranges as in
F4; ε_0 absorbed into the definition of A_μ^ext throughout
(SI / Gaussian units are recoverable by restoring the
appropriate factor at the end).

---

## Section A — Switching on the external field as a metric perturbation

### A.1 — In KK, the EM field *is* the metric

> *Purpose: clarify that there is no separate "external EM
> field" sitting on top of the geometry — the EM field is one
> of the off-diagonal metric components, by F4.*

In standard 4D physics, an external EM field is an
independent object: a 4-potential A_μ^ext that lives on the
spacetime manifold and couples to charged particles through a
minimal-coupling prescription D_μ = ∂_μ − i (Q/ℏ) A_μ^ext.
The electromagnetic field is a separate object from the
spacetime metric.

In Kaluza–Klein, this is not the case.  The EM field is
*part of the metric* — it appears as the off-diagonal block
G_μa.  From F4 A.3 we have G_μa = g_ab A^b_μ; the gauge
potentials A^a_μ are read off from the off-diagonal entries.

Therefore "switching on an external EM field" means switching
on a particular component of the 6D metric.  Specifically,
under Track 5's tube-couples convention (where A^5_μ = 0
permanently), switching on an external field means

<!-- A^4_μ(x) = 0   →   A^4_μ(x) = A_μ^ext(x) -->
$$
A^{4}{}_{\mu}(x) \;=\; 0
\quad\longrightarrow\quad
A^{4}{}_{\mu}(x) \;=\; A_{\mu}^{\text{ext}}(x),
$$

with A_μ^ext small (weak-field assumption) and slowly varying
in x^μ.

A_μ^ext is the same object that 4D physicists call "the
electromagnetic 4-potential," up to the units factor e_0
that mediates between F4's geometric A^4_μ and the SI /
Gaussian A_μ^ext.  Concretely, A_μ^ext = A^4_μ × e_0, so
that the "physical" charge Q = ℏ k_4 / e_0 = e n_t (per F14)
couples to A_μ^ext in the dimensionful form.  For most of
this derivation we will keep e_0 implicit (working in units
where e_0 = 1) and restore it only when comparing to F14.

### A.2 — Background geometry

> *Purpose: state the metric we are perturbing around.*

We work on M⁴ × T² with M⁴ flat (η_μν background) and the
internal 2-torus carrying the F11 metric

<!-- g_44 = ε², g_55 = 1/ε² + s², g_45 = ε s, det g = 1 -->
$$
g_{ab} \;=\;
\begin{pmatrix} \varepsilon^{2} & \varepsilon\,s \\
\varepsilon\,s & \tfrac{1}{\varepsilon^{2}} + s^{2}
\end{pmatrix},
\qquad
h^{ab} \;=\;
\begin{pmatrix} \tfrac{1}{\varepsilon^{2}} + s^{2}
                & -\varepsilon\,s \\
-\varepsilon\,s & \varepsilon^{2}
\end{pmatrix},
\qquad
\det g \;=\; 1.
$$

Track 5's tube-couples convention is in force throughout: the
*background* values of both gauge potentials are zero,

<!-- A^4_μ = 0, A^5_μ = 0 (background) -->
$$
A^{4}{}_{\mu}{}^{(0)} \;=\; 0,
\qquad
A^{5}{}_{\mu} \;\equiv\; 0
\;\;\text{(permanently)},
$$

and we now switch on a perturbation A^4_μ = A_μ^ext(x).
The ring gauge potential A^5_μ stays zero by Track 5's
convention (it never gets turned on; that is what makes it the
"dark" direction).

### A.3 — The perturbed inverse metric

> *Purpose: write G^AB after switching on A_μ^ext, keeping
> only what is needed to first order.*

Substituting A^4_μ = A_μ^ext into the F4 B.3 inverse-metric
formulas:

<!-- G^μν = η^μν, G^μ4 = -A^μ ext, G^μ5 = 0, G^44 = h^44 + A·A ext, G^45 = h^45, G^55 = h^55 -->
$$
G^{\mu\nu} \;=\; \eta^{\mu\nu},
\qquad
G^{\mu 4} \;=\; -A^{\mu}{}_{\text{ext}},
\qquad
G^{\mu 5} \;=\; 0,
$$

$$
G^{44} \;=\; h^{44} \;+\; A^{\mu}{}_{\text{ext}}\,A_{\mu}^{\text{ext}},
\qquad
G^{45} \;=\; h^{45},
\qquad
G^{55} \;=\; h^{55},
$$

with A^μ_ext ≡ η^μν A_ν^ext.  The only metric components
modified by switching on A_μ^ext are G^μ4 (linear in A^ext)
and G^44 (quadratic in A^ext).  All other components stay at
their background values.

### A.4 — Cylinder condition still holds

> *Purpose: confirm Killing-momentum conservation survives the
> perturbation.*

By assumption, A_μ^ext depends only on x^μ.  All metric
components remain independent of x^4 and x^5.  Therefore
the Killing vectors ξ_4^A = δ^A_4 and ξ_5^A = δ^A_5 from F4
D.2 are still Killing vectors of the perturbed metric, and the
two compact momenta P_4 and P_5 are still conserved along any
geodesic (or wave-equation characteristic).

This is the algebraic guarantee that turning on A_μ^ext does
not change the eigenvalue labels (n_t, n_r) of a standing-
wave state.  A particle that was a (n_t, n_r) eigenstate
before A_μ^ext is switched on remains a (n_t, n_r)
eigenstate after — the perturbation does not mix compact
modes.  This is exactly the content one needs to identify
"the same particle" in the presence and absence of the
external field, and it is the reason the centroid trajectory
will turn out to depend on the *fixed* labels (n_t, n_r) and
not on a time-dependent superposition of them.

---

## Section B — The 6D wave equation and separation of variables

### B.1 — The 6D massless Klein–Gordon equation

> *Purpose: introduce the field-theoretic version of the
> photon, in the form needed for the calculation.*

A photon, as a quantum object, is characterized by its wave
equation.  The simplest covariant scalar wave equation in 6D
is the massless Klein–Gordon equation

<!-- ∂_A (√|G| G^AB ∂_B Ψ) = 0 -->
$$
\frac{1}{\sqrt{|G|}}\,\partial_{A}\!\left(\sqrt{|G|}\,G^{AB}\,\partial_{B}\Psi\right) \;=\; 0.
$$

This equation reduces in geometrical optics to the 6D null
geodesic equation already used in F7, with Ψ playing the role
of a wavefunction whose phase is the eikonal action S.  We
adopt it here as the field-equation form of the same "photon"
used in derivations 1, 3 — no new physical assumption beyond
"the photon obeys a wave equation."

(The vector character of the photon — its polarization — is
not used in this derivation, which concerns only the centroid
motion of an eigenstate.  A spin-1 derivation would reproduce
the Lorentz force at the leading semiclassical order with an
identical prefactor, plus a separate spin-magnetic-moment term
that belongs to the magnetic-moment track.)

### B.2 — Det |G| to leading order

> *Purpose: simplify the wave equation by computing the metric
> determinant.*

To linear order in A_μ^ext, the determinant of the perturbed
6D metric equals the determinant of the background 6D metric.
Reason: det |G| is invariant under the linear shift of the
off-diagonal block g_μa by a small term that the diagonal
blocks dominate; algebraically,

<!-- det G = det g_μν × det g_ab × (1 + O(A^ext²)) -->
$$
\det G \;=\; (\det g_{\mu\nu}) \times (\det g_{ab})
            \times \left(1 + \mathcal{O}(A_{\text{ext}}^{2})\right)
       \;=\; \det g_{\mu\nu} \times 1
            + \mathcal{O}(A_{\text{ext}}^{2}),
$$

using det g = 1 from F11.  Furthermore, since A_μ^ext is
slowly varying in x^μ (by assumption), the spacetime
gradient ∂_μ √|G| is itself either zero (background) or of
order A_ext × ∂A_ext, which is second order in the small
parameter.

To linear order in A_μ^ext, then,

<!-- (1/√|G|) ∂_A(√|G| G^AB ∂_B Ψ) = ∂_A (G^AB ∂_B Ψ) + O(A^ext²) -->
$$
\frac{1}{\sqrt{|G|}}\,\partial_{A}\!\left(\sqrt{|G|}\,G^{AB}\,\partial_{B}\Psi\right)
\;=\; \partial_{A}\!\left(G^{AB}\,\partial_{B}\Psi\right)
   \;+\; \mathcal{O}(A_{\text{ext}}^{2}).
$$

The wave equation simplifies to ∂_A (G^AB ∂_B Ψ) = 0 to the
order at which we are working.  Higher-order terms can be kept
if desired but are not needed for the leading-order Lorentz-
force result.

### B.3 — Separation of variables

> *Purpose: factor out the compact-mode dependence using the
> Killing structure.*

Because the perturbed metric is independent of x^4 and x^5
(A.4), the wave equation admits separable solutions of the
form

<!-- Ψ(x^μ, x^4, x^5) = ψ(x^μ) Φ_(n_t, n_r)(x^4, x^5) -->
$$
\Psi(x^{\mu}, x^{4}, x^{5})
\;=\; \psi(x^{\mu})\,\Phi_{(n_{t}, n_{r})}(x^{4}, x^{5}),
$$

with Φ a compact-mode eigenfunction of the two compact-
direction translation generators −i ∂_4 and −i ∂_5.  By the
single-valuedness boundary conditions on T² (standing-wave
quantization, F4 D.4 / F11 B.2),

<!-- Φ = (1/√(L_t L_r)) exp(i k_4 x^4 + i k_5 x^5),  k_a = 2π n_a / L_a -->
$$
\Phi_{(n_{t}, n_{r})}(x^{4}, x^{5})
\;=\; \frac{1}{\sqrt{L_{t}\,L_{r}}}
      \,\exp\!\left[i\!\left(k_{4}\,x^{4} + k_{5}\,x^{5}\right)\right],
\qquad
k_{a} \;=\; \frac{2\pi\,n_{a}}{L_{a}}, \quad n_{a} \in \mathbb{Z}.
$$

(With our 4 ↔ tube, 5 ↔ ring convention: k_4 = 2π n_t/L_t,
k_5 = 2π n_r/L_r.  Φ is L²-normalized over one fundamental
cell of T².)

The conserved Killing momenta in the dimensionful units of
F11 / F14 are

<!-- P_a = ℏ k_a -->
$$
P_{a} \;=\; \hbar\,k_{a},
\qquad
P_{4} \;=\; \frac{n_{t}\,h}{L_{t}},
\qquad
P_{5} \;=\; \frac{n_{r}\,h}{L_{r}},
$$

matching F4 D.4 exactly.  We will use k_a (inverse-length
units) inside the wave-equation manipulation and convert to
P_a (momentum units, ℏ restored) when comparing to F11 / F14.

### B.4 — Substituting into the wave equation

> *Purpose: do the algebra and obtain the 4D equation for ψ.*

Apply ∂_A (G^AB ∂_B Ψ) = 0 with the separated Ψ.  Group by
which indices are compact vs. spacetime.  Each term:

(i) Pure-spacetime (A, B both spacetime).
G^μν ∂_μ ∂_ν Ψ = η^μν ∂_μ ∂_ν Ψ = (□ψ) Φ.

(ii) Spacetime-derivative of mixed off-diagonal (A spacetime,
B compact).  G^μa ∂_a Ψ = G^μ4 (i k_4 ψ Φ) + G^μ5 (i k_5 ψ Φ)
= −A^μ_ext (i k_4 ψ Φ) + 0.  Then
∂_μ (G^μa ∂_a Ψ) = i k_4 ∂_μ (−A^μ_ext ψ) Φ
= −i k_4 [(∂_μ A^μ_ext) ψ + A^μ_ext (∂_μ ψ)] Φ.

(iii) Compact-derivative of mixed off-diagonal (A compact, B
spacetime).  G^aμ ∂_μ Ψ = G^4μ (∂_μ ψ) Φ = −A^μ_ext (∂_μ ψ) Φ.
Then ∂_a (G^aμ ∂_μ Ψ) = (i k_a) G^aμ (∂_μ ψ) Φ
= (i k_4)(−A^μ_ext)(∂_μ ψ) Φ = −i k_4 A^μ_ext (∂_μ ψ) Φ.

(iv) Pure-compact (A, B both compact).
G^ab ∂_a ∂_b Ψ = (i k_a)(i k_b) G^ab ψ Φ = −G^ab k_a k_b ψ Φ.
With G^ab = h^ab + A^a_μ A^bμ (F4 B.3):
G^ab k_a k_b = h^ab k_a k_b + (A^4_μ A^4μ) k_4 k_4
            = h^ab k_a k_b + A^μ_ext A_μ^ext × k_4².

Summing (i) + (ii) + (iii) + (iv) and dividing through by Φ:

<!-- □ψ - 2 i k_4 A^μ_ext ∂_μ ψ - i k_4 (∂_μ A^μ_ext) ψ - h^ab k_a k_b ψ - k_4² A_ext² ψ = 0 -->
$$
\Box\,\psi
\;-\; 2\,i\,k_{4}\,A^{\mu}_{\text{ext}}\,\partial_{\mu}\psi
\;-\; i\,k_{4}\,(\partial_{\mu}A^{\mu}_{\text{ext}})\,\psi
\;-\; h^{ab}\,k_{a}\,k_{b}\,\psi
\;-\; k_{4}^{2}\,A^{\mu}_{\text{ext}}\,A_{\mu}^{\text{ext}}\,\psi
\;=\; 0.
$$

This is the **effective 4D wave equation** for the eigenstate
ψ of compact label (n_t, n_r), in the presence of the
external field A_μ^ext.

---

## Section C — Identifying the effective mass and charge

### C.1 — The minimal-coupling structure

> *Purpose: rewrite the B.4 result in the form of a Klein–
> Gordon equation with gauge-covariant derivatives.*

Define the 4D gauge-covariant derivative

<!-- D_μ ψ = (∂_μ - i k_4 A_μ^ext) ψ -->
$$
D_{\mu}\,\psi \;\equiv\;
\left(\partial_{\mu} \;-\; i\,k_{4}\,A_{\mu}^{\text{ext}}\right)\!\psi.
$$

Compute D^μ D_μ ψ:

$$
D^{\mu}D_{\mu}\,\psi
\;=\; \partial^{\mu}(\partial_{\mu} - i k_{4} A_{\mu}^{\text{ext}})\,\psi
   \;-\; i k_{4} A^{\mu}_{\text{ext}} (\partial_{\mu} - i k_{4} A_{\mu}^{\text{ext}})\,\psi
$$

$$
\;=\; \Box\psi
   \;-\; i k_{4} (\partial^{\mu} A_{\mu}^{\text{ext}})\,\psi
   \;-\; i k_{4} A_{\mu}^{\text{ext}}\,\partial^{\mu}\psi
   \;-\; i k_{4} A^{\mu}_{\text{ext}}\,\partial_{\mu}\psi
   \;-\; k_{4}^{2}\,A^{\mu}_{\text{ext}} A_{\mu}^{\text{ext}}\,\psi
$$

$$
\;=\; \Box\psi
   \;-\; 2\,i\,k_{4}\,A^{\mu}_{\text{ext}}\,\partial_{\mu}\psi
   \;-\; i\,k_{4}\,(\partial_{\mu} A^{\mu}_{\text{ext}})\,\psi
   \;-\; k_{4}^{2}\,A^{\mu}_{\text{ext}} A_{\mu}^{\text{ext}}\,\psi.
$$

Comparing this to the wave equation in B.4 (last line), the
two expressions match exactly — every coefficient and every
sign.  So B.4 can be rewritten as

<!-- D^μ D_μ ψ = h^ab k_a k_b ψ -->
$$
\boxed{\;
D^{\mu}D_{\mu}\,\psi \;=\; h^{ab}\,k_{a}\,k_{b}\,\psi
\;}
$$

This is the **4D Klein–Gordon equation with minimal coupling
to A_μ^ext**, with effective mass-squared eigenvalue
h^ab k_a k_b on the right-hand side and effective charge-to-
ℏ ratio k_4 in the gauge-covariant derivative.

The minimal-coupling structure D_μ = ∂_μ − i k_4 A_μ^ext is
**not postulated** — it falls out of the algebra of separating
variables on the 6D wave equation.  This is one of the
classic results of Kaluza–Klein, here repeated for the 2-torus
generalization with the extra observation that only k_4 (not
k_5) couples to the external field, by Track 5's tube-couples
convention.

### C.2 — Identifying the effective mass

> *Purpose: read off m² from the C.1 box and compare to F7.*

The 4D KG equation in C.1 has D²ψ = h^ab k_a k_b ψ.  To
identify m², compare with the standard free 4D KG equation in
our mostly-plus signature.

A free 4D plane wave ψ = exp(i p_μ x^μ / ℏ) for a massive
particle with timelike 4-momentum p^μ p_μ = −m²c² (mostly
plus convention) satisfies

<!-- □ ψ = (i p_μ/ℏ)(i p^μ/ℏ) ψ = -(p_μ p^μ/ℏ²) ψ = +(m²c²/ℏ²) ψ -->
$$
\Box\,\psi \;=\; -\,\frac{p_{\mu}\,p^{\mu}}{\hbar^{2}}\,\psi
        \;=\; +\,\frac{m^{2}\,c^{2}}{\hbar^{2}}\,\psi.
$$

So the standard free 4D KG equation in mostly-plus is

<!-- □ ψ - (m²c²/ℏ²) ψ = 0  →  □ ψ = +(m²c²/ℏ²) ψ -->
$$
\Box\,\psi \;=\; \frac{m^{2}\,c^{2}}{\hbar^{2}}\,\psi.
$$

The minimally-coupled version replaces ∂_μ by D_μ:
D²ψ = (m²c²/ℏ²) ψ.  Comparing with C.1's box,

<!-- D² ψ = h^ab k_a k_b ψ  vs.  D² ψ = (m²c²/ℏ²) ψ -->
$$
\frac{m^{2}\,c^{2}}{\hbar^{2}} \;=\; h^{ab}\,k_{a}\,k_{b},
\qquad\text{i.e.,}\qquad
m^{2}\,c^{2} \;=\; \hbar^{2}\,h^{ab}\,k_{a}\,k_{b}
\;=\; h^{ab}\,P_{a}\,P_{b},
$$

using P_a = ℏ k_a (B.3).  This is **exactly F7** — the same
photon-on-2-torus mass formula derived in Track 3 from the
6D null condition.

The sign is right because the compact directions are
*spacelike* in our (−, +, +, +, +, +) signature: a compact
wavefunction Φ ∝ exp(i k_a x^a) with real k_a contributes a
positive G^ab k_a k_b to the action of the 6D box, which
appears on the spacetime side as a positive effective
mass-squared.  This is the standard KK mechanism: spacelike
compact momentum → real, positive 4D rest mass.

So the effective 4D rest-mass-squared in the presence of the
external field A_μ^ext is identical to the rest-mass-squared
of the same eigenstate in the absence of A_μ^ext.  Switching
on the external field does **not** shift the mass (at linear
order); the external field only couples to the gauge-
covariant derivative, not to the mass eigenvalue.

This is the desired result: the m that appears as the
inertial coefficient in the 4D Klein–Gordon equation
(C.1 → eikonal limit, Section E) is the **same** m derived
in F11 from the photon-on-2-torus geometry.

### C.3 — Identifying the effective charge

> *Purpose: read off Q from the gauge-covariant derivative
> coefficient in C.1 and compare to F14.*

The minimal-coupling form D_μ = ∂_μ − i k_4 A_μ^ext has the
canonical structure D_μ = ∂_μ − i (Q/ℏ) A_μ^ext when

<!-- Q / ℏ = k_4 -->
$$
\frac{Q}{\hbar} \;=\; k_{4},
\qquad\text{i.e.,}\qquad
Q \;=\; \hbar\,k_{4} \;=\; P_{4}.
$$

So the **charge that the external field sees is the conserved
Killing momentum P_4** — exactly what F14 identified as the
electric charge of the eigenstate, before any units factor is
applied.

In F14's units, with the standing-wave quantization
P_4 = n_t h/L_t and the unit-fixing factor e_0,

<!-- Q = e × n_t with e = h/(L_t e_0) -->
$$
Q \;=\; \frac{P_{4}}{e_{0}} \;=\; e \times n_{t},
\qquad
e \;=\; \frac{h}{L_{t}\,e_{0}}.
$$

So Q in dimensionful units is **exactly the F14 charge**.

The two operational tests of "what is the charge of this
particle?" — (i) "what is the conserved Killing momentum in
the tube direction?" (Track 5) and (ii) "what is the
coefficient of A_μ^ext in the gauge-covariant derivative of
the effective 4D wave equation?" (this derivation, C.3) —
return the **same number**.  This is the non-trivial
consistency check that earlier tracks could not perform, since
they treated charge purely as a conserved Killing momentum
without coupling it to an external field.

### C.4 — Summary box

For a (n_t, n_r) standing-wave eigenstate in a weak external
EM field, the effective 4D wave equation is

<!-- (D² - m²c²/ℏ²) ψ = 0 with D = ∂ - i Q A_ext / ℏ, m² = h^ab P_a P_b / c², Q = P_4 -->
$$
\boxed{\;
\left(D^{\mu}D_{\mu} \;-\; \frac{m^{2}\,c^{2}}{\hbar^{2}}\right)\!\psi \;=\; 0,
\qquad
D_{\mu} \;=\; \partial_{\mu} \;-\; \frac{i\,Q}{\hbar}\,A_{\mu}^{\text{ext}},
\;}
$$

with **m and Q derived from the same 6D photon eigenstate**:

<!-- m² c² = h^ab P_a P_b (F7),  Q = P_4 (F14, before units factor) -->
$$
m^{2}\,c^{2} \;=\; h^{ab}\,P_{a}\,P_{b} \;\;[F7], \qquad
Q \;=\; P_{4} \;\;[F14, \text{up to } e_{0}].
$$

No new parameters appear.  The same algebra that produced
F7 (m) and F14 (Q) also produces, by separating variables in
the 6D wave equation, the standard 4D Klein–Gordon equation
with minimal coupling to the external field.

---

## Section D — Eikonal limit and the Lorentz force

### D.1 — Setup

> *Purpose: take the centroid limit of the 4D KG equation in
> C.4 and recover the classical Lorentz force.*

The result of Section C is a quantum wave equation.  The
classical Lorentz force is recovered by taking the eikonal
(WKB / geometrical-optics) limit, in which ψ is a slowly-
varying envelope on top of a rapidly-oscillating phase:

<!-- ψ(x) = a(x) exp(i S(x) / ℏ) -->
$$
\psi(x) \;=\; a(x)\,\exp\!\left(\frac{i\,S(x)}{\hbar}\right),
$$

with S the eikonal action and a a slowly-varying amplitude.
"Slowly varying" means the relative scale on which a varies
is much larger than ℏ/|∂_μ S|, the de Broglie wavelength.

### D.2 — Substituting and keeping leading order in ℏ

Compute D_μ ψ:

<!-- D_μ ψ = (i/ℏ)(∂_μ S - Q A_μ^ext) ψ + (∂_μ a / a) ψ -->
$$
D_{\mu}\,\psi \;=\;
\left[\frac{i}{\hbar}\!\left(\partial_{\mu}S - Q\,A_{\mu}^{\text{ext}}\right)
   \;+\; \frac{\partial_{\mu}a}{a}\right]\!\psi.
$$

Define the **kinetic momentum**

<!-- π_μ ≡ ∂_μ S - Q A_μ^ext -->
$$
\pi_{\mu} \;\equiv\; \partial_{\mu}S \;-\; Q\,A_{\mu}^{\text{ext}}.
$$

In the eikonal limit (envelope variations subleading in ℏ),

<!-- D_μ ψ ≈ (i/ℏ) π_μ ψ -->
$$
D_{\mu}\,\psi \;\approx\; \frac{i}{\hbar}\,\pi_{\mu}\,\psi
\;+\; \mathcal{O}(\hbar^{0}\text{-envelope}).
$$

Then to leading order

<!-- D² ψ ≈ -(π^μ π_μ / ℏ²) ψ -->
$$
D^{\mu}D_{\mu}\,\psi \;\approx\; -\,\frac{\pi^{\mu}\pi_{\mu}}{\hbar^{2}}\,\psi.
$$

Substituting into the C.4 box:

<!-- -π^μ π_μ / ℏ² = m²c²/ℏ² → π^μ π_μ = -m²c² -->
$$
\pi^{\mu}\,\pi_{\mu} \;=\; -\,m^{2}\,c^{2}.
$$

This is the **relativistic Hamilton–Jacobi equation** for a
particle of mass m and charge Q in the external field
A_μ^ext.  The kinetic momentum π_μ has timelike norm equal to
−m²c², exactly as for a 4D massive particle in standard
classical electrodynamics.

### D.3 — Characteristics: the 4D worldline

> *Purpose: extract the centroid trajectory from the
> Hamilton–Jacobi equation.*

The characteristics of the Hamilton–Jacobi equation D.2 are
defined by

<!-- m dx^μ/dτ = π^μ -->
$$
m\,\frac{dx^{\mu}}{d\tau} \;=\; \pi^{\mu}
\;=\; \partial^{\mu}S \;-\; Q\,A^{\mu}_{\text{ext}},
$$

with τ the proper time on the centroid worldline.  This is
the standard relation between canonical momentum (∂^μ S) and
kinetic momentum (π^μ = m ẋ^μ) in a charged-particle
Lagrangian — derivable from L = −mc √(−ẋ²) + Q ẋ^μ A_μ.

Differentiating along the worldline:

<!-- m d²x^μ/dτ² = dπ^μ/dτ = ẋ^ν ∂_ν π^μ -->
$$
m\,\frac{d^{2}x^{\mu}}{d\tau^{2}}
\;=\; \frac{d\pi^{\mu}}{d\tau}
\;=\; \dot{x}^{\nu}\,\partial_{\nu}\pi^{\mu}.
$$

Using ∂_ν π^μ = ∂_ν ∂^μ S − Q ∂_ν A^μ_ext, and after the
algebraic manipulation spelled out in D.4 below — which uses
the constraint π^μ π_μ = −m²c² (from D.2) to convert the
symmetric ∂_ν ∂^μ S piece into a charge-dependent term that
combines with Q ∂_ν A^μ to give the antisymmetric field
strength — one obtains

<!-- m d²x^μ/dτ² = -Q ẋ^ν (∂_ν A^μ_ext - ∂^μ A_ν_ext) = Q F^μ_ν^ext ẋ^ν -->
$$
\boxed{\;
m\,\frac{d^{2}x^{\mu}}{d\tau^{2}}
\;=\; Q\,F^{\mu}{}_{\nu}^{\text{ext}}\,\dot{x}^{\nu},
\;}
$$

with F_μν^ext = ∂_μ A_ν^ext − ∂_ν A_μ^ext the external EM
field strength.  This is the **relativistic Lorentz-force
equation**.

The *m* on the left is the inertial mass of C.2 (= F7
mass).  The *Q* on the right is the charge of C.3 (= F14
charge).  Both are the same numbers derived in earlier tracks
from the underlying compact momenta P_a; nothing new has been
introduced.

### D.4 — Step-by-step Lagrangian derivation of the Lorentz term

> *Purpose: spell out the algebra hidden in "the standard
> manipulation" of D.3, for completeness.*

Starting from D.3's intermediate step

<!-- m d²x^μ/dτ² = ẋ^ν ∂_ν (∂^μ S - Q A^μ_ext) -->
$$
m\,\frac{d^{2}x^{\mu}}{d\tau^{2}}
\;=\; \dot{x}^{\nu}\,\partial_{\nu}\partial^{\mu}S
   \;-\; Q\,\dot{x}^{\nu}\,\partial_{\nu}A^{\mu}_{\text{ext}}.
$$

The first term: differentiate the Hamilton–Jacobi equation D.2
with respect to x^ρ:

<!-- ∂_ρ (π^μ π_μ) = -∂_ρ m²c² = 0 (m constant) -->
$$
2\,\pi^{\mu}\,\partial_{\rho}\pi_{\mu} \;=\; 0,
$$

i.e., π^μ ∂_ρ π_μ = 0.  Substituting π_μ = ∂_μ S − Q A_μ^ext:

$$
\pi^{\mu}\!\left(\partial_{\rho}\partial_{\mu}S
        \;-\; Q\,\partial_{\rho}A_{\mu}^{\text{ext}}\right) \;=\; 0.
$$

Mixed partial derivatives commute: ∂_ρ ∂_μ S = ∂_μ ∂_ρ S.
Multiply through by 1/m and use π^μ = m ẋ^μ from D.3:

$$
\dot{x}^{\mu}\,\partial_{\mu}\partial_{\rho}S
\;-\; Q\,\dot{x}^{\mu}\,\partial_{\rho}A_{\mu}^{\text{ext}} \;=\; 0,
$$

which gives

<!-- ẋ^μ ∂_μ ∂_ρ S = Q ẋ^μ ∂_ρ A_μ^ext -->
$$
\dot{x}^{\mu}\,\partial_{\mu}\partial_{\rho}S
\;=\; Q\,\dot{x}^{\mu}\,\partial_{\rho}A_{\mu}^{\text{ext}}.
$$

Substitute this into the right-hand side of D.3 with the
relabeling ν ↔ ρ (and with index μ on the LHS coming from
∂^μ on S, raised by η^μν):

$$
m\,\frac{d^{2}x^{\mu}}{d\tau^{2}}
\;=\; \eta^{\mu\rho}\,\dot{x}^{\nu}\,\partial_{\nu}\partial_{\rho}S
   \;-\; Q\,\dot{x}^{\nu}\,\partial_{\nu}A^{\mu}_{\text{ext}}
$$

$$
\;=\; \eta^{\mu\rho}\,Q\,\dot{x}^{\nu}\,\partial_{\rho}A_{\nu}^{\text{ext}}
   \;-\; Q\,\dot{x}^{\nu}\,\partial_{\nu}A^{\mu}_{\text{ext}}
$$

$$
\;=\; Q\,\dot{x}^{\nu}\!\left(\partial^{\mu}A_{\nu}^{\text{ext}}
                          \;-\; \partial_{\nu}A^{\mu}_{\text{ext}}\right)
\;=\; Q\,F^{\mu}{}_{\nu}^{\text{ext}}\,\dot{x}^{\nu}.
$$

Here in the second-to-last line we used ∂^μ ≡ η^μρ ∂_ρ.  The
combination ∂^μ A_ν − ∂_ν A^μ is exactly F^μ_ν, the mixed
form of the field strength.  This recovers the boxed Lorentz
force of D.3.

### D.5 — The internal kinetic-momentum / shear contribution

> *Purpose: examine whether the shear g_45 introduces an
> additional term beyond the standard Lorentz force.*

Section D so far treated the standing-wave eigenstate with
both n_t and n_r general, so the wave equation in C.1 has
both k_4 and k_5 contributing to the right-hand-side mass
formula h^ab k_a k_b.  But only k_4 enters the gauge-covariant
derivative D_μ (not k_5), because of the tube-couples
convention A^5_μ = 0.

This means: a particle with both n_t ≠ 0 *and* n_r ≠ 0 has

- mass affected by both quanta (via h^ab P_a P_b);
- charge affected only by n_t (Q = e n_t);
- centroid trajectory determined by (m, Q) via D.3, with **no
  separate dependence on n_r** beyond its contribution to m.

So the n_r quantum is "dark" with respect to the centroid
trajectory — it modifies inertial mass, but it does not couple
to the external field.  This is the kinematic content of F16
made operational: dark conservation laws contribute to
inertia but not to acceleration.

The shear g_45 enters only through h^ab in the mass formula
(the off-diagonal h^45 = −εs is what creates the (n_r − s n_t)
combination of F11).  It does not appear in the gauge-
covariant derivative — that one is purely k_4 = (2π/L_t) n_t
on the tube.  So the shear is a *mass-spectrum* effect, not a
*Lorentz-force* effect.  The Lorentz-force coefficient (Q/m)
of an eigenstate is the F14 charge divided by the F11 mass —
both fully determined by the geometry (ε, s, L_t, L_r) and
the integer labels (n_t, n_r), with no additional shear-
mediated cross-couplings between the two.

This is a non-trivial observation, in the sense that one might
have feared that "shear mixes mass and charge" (per F9) would
also imply "shear modifies the Lorentz-force coupling."  It
does not — at least not at the level of the centroid motion in
the eikonal limit.  Mass-charge mixing is a *spectrum*
phenomenon (which integer pairs (n_t, n_r) give which
masses); Lorentz-force coupling is a *post-spectrum*
phenomenon (given the values of m and Q for the eigenstate
selected, the centroid moves as a standard charged particle).

---

## Section E — What this establishes

### E.1 — Mass, charge, and the EM coupling are the same geometric object

> *Purpose: state the central result.*

The 4D rest mass m of a (n_t, n_r) eigenstate is its compact-
direction quadratic form (F7).  The 4D electric charge Q is
its conserved tube-direction Killing momentum (F14).  Both
quantities are extracted from the same compact momenta P_a,
just contracted into different invariants:

| Quantity | How extracted from P_a |
|----------|------------------------|
| Mass m | √(h^ab P_a P_b) / c |
| Charge Q | P_4 / e_0 |
| Lorentz coupling Q/m × A_μ^ext | The same P_4 from charge, divided by the same h^ab P_a P_b that gives mass |

The Lorentz force m ẍ = Q F · ẋ uses both quantities together,
in their derived form, with no additional parameters.  Mass,
charge, and the EM coupling are not three separate
postulates — they are three projections of one underlying
compact-momentum vector.

This is the operational closure of the single-sheet "electron
from light" picture: every classical electrodynamic property
of the projected particle is now derived from the same 6D null
trajectory.

### E.2 — The minimal-coupling prescription is derived

> *Purpose: emphasize that "D_μ = ∂_μ − iQ A_μ/ℏ" is not a
> postulate.*

In standard 4D electrodynamics, minimal coupling is a
postulate — the prescription that A_μ enters the Schrödinger
or Klein–Gordon equation through the substitution
∂_μ → ∂_μ − i(Q/ℏ) A_μ.  Justification is typically by gauge
invariance, but the form of the substitution itself is taken
as given.

Here, minimal coupling falls out of the algebra of separating
variables on the 6D wave equation (Section B.4 → C.1).  The
appearance of A_μ^ext in the gauge-covariant derivative is a
*consequence* of the geometry: the off-diagonal metric
component G^μ4 contributes to the 4D effective wave equation
with exactly the coefficients required to look like minimal
coupling.

This is a notable technical result, independent of MaSt: 6D
KK on M⁴ × T² *derives* minimal coupling for any 4D charged
field.  Klein noted this for the original 5D case; Section
B.4 extends it to the 2-torus generalization with one of the
two U(1)s suppressed by Track 5's tube-couples convention.

### E.3 — Inertial mass and rest mass are the same

> *Purpose: confirm that the m on the left side of the Lorentz
> force is really the inertial mass.*

The m that appears on the left side of the Lorentz force in
D.3 is the coefficient of d²x^μ/dτ² — by definition the
inertial mass.  The m identified in C.2 is the rest-mass
parameter of the effective Klein–Gordon equation — the F7
mass.  These are the **same number** because they are both
read off from the same equation (C.4 → D.2 → D.3) without
any rescaling.

This generalizes F10 (inertia and rest mass equal for the
free 6D photon) to the case with an external EM field present.
Switching on A_μ^ext modifies the centroid motion but does
not change the inertial coefficient — exactly as in standard
4D electrodynamics.

### E.4 — Multi-mode wavepackets

> *Purpose: address the realistic case where ψ is a
> superposition of compact eigenstates.*

The derivation took ψ as a single (n_t, n_r) eigenstate.  A
realistic localized wavepacket would be a superposition,

<!-- Ψ = Σ c_{n_t, n_r} ψ_{n_t, n_r}(x^μ) Φ_{n_t, n_r}(x^4, x^5) -->
$$
\Psi \;=\; \sum_{n_{t}, n_{r}} c_{n_{t}, n_{r}}\,
        \psi_{n_{t}, n_{r}}(x^{\mu})\,
        \Phi_{n_{t}, n_{r}}(x^{4}, x^{5}).
$$

Because the perturbed metric is independent of x^4, x^5 (A.4)
and because the compact-mode functions are orthogonal,
different (n_t, n_r) sectors do not mix under the wave
equation — each ψ_{n_t, n_r} obeys its own 4D KG equation
(C.4) with its own (m, Q).

Operationally this means a multi-mode wavepacket spreads
because different (n_t, n_r) sectors have different masses
(group velocities at the same energy), and each sector
independently obeys its own Lorentz force.  The overall
centroid is a weighted average that does *not* obey the
single-particle Lorentz force unless one sector dominates
(or all sectors with significant amplitude have the same
m, Q — degeneracy).

This is just the standard quantum-mechanical statement that
"a superposition of mass eigenstates does not have a well-
defined trajectory."  For a particle to behave as a classical
charged particle of definite (m, Q), it must occupy a single
(n_t, n_r) eigenstate — which is the natural state under
the standard "asymptotic in / asymptotic out" particle
identification.

### E.5 — What is *not* derived here

This derivation pins down:

- The 4D effective wave equation for a (n_t, n_r) standing-
  wave eigenstate in an external EM field (C.4).
- The minimal-coupling structure of that equation (C.1).
- The Lorentz-force equation for the centroid, with m and Q
  identical to those of F7 and F14 (D.3).
- The fact that the shear g_45 enters only the mass formula,
  not the gauge-covariant derivative (D.5).
- The identification of inertial mass with rest mass in the
  presence of an external field (E.3).

It does **not** determine:

- Spin — the wave equation used (scalar Klein–Gordon) is
  spin-0; the vector or spinor cases would add a polarization
  index and a separate magnetic-moment term.  Spin is
  separate, treated in subsequent work.
- Higher-order wavepacket effects (Berry curvature in the
  envelope, anomalous velocity terms, etc.).  These are
  subleading in the eikonal expansion and could plausibly
  contribute to anomalous-moment corrections at higher
  order.
- Self-field effects.  A_μ^ext is an *external* field,
  produced by sources other than the eigenstate itself.  The
  back-reaction of the eigenstate's own field on its motion
  (radiation reaction, self-energy) is not addressed.
- Non-perturbative external fields.  The derivation assumed
  |q A_μ^ext| ≪ |compact momentum quanta|; a strong-field
  treatment (Schwinger limit, etc.) would require keeping
  higher-order terms in A^ext.
- Curved 4D spacetime.  The background was flat M⁴; a
  generalization to curved 4D (gravity coupled to an EM
  field, with a charged test particle) would require the
  full 6D Christoffel structure of derivation-2 with both g_μν
  and A^4_μ varying.

---

## Lemma (Track 6 result)

We have shown:

> **(F17) Lorentz force on the standing-wave state.**  Under
> Track 5's tube-couples convention with an external EM field
> A_μ^ext switched on as a metric perturbation A^4_μ = A_μ^ext,
> a (n_t, n_r) standing-wave eigenstate of the 6D massless
> Klein–Gordon equation has a 4D effective wave equation of
> Klein–Gordon form
>
> $$
> \left(D^{\mu}D_{\mu} \;-\; \frac{m^{2}\,c^{2}}{\hbar^{2}}\right)\!\psi \;=\; 0,
> \qquad
> D_{\mu} \;=\; \partial_{\mu} - \frac{i\,Q}{\hbar}\,A_{\mu}^{\text{ext}},
> $$
>
> with effective rest mass m given by F7 (m²c² = h^ab P_a P_b)
> and effective charge Q given by F14 (Q = P_4 / e_0 = e n_t).
> The eikonal limit of this equation yields the relativistic
> Lorentz-force equation
>
> $$
> m\,\frac{d^{2}x^{\mu}}{d\tau^{2}}
> \;=\; Q\,F^{\mu}{}_{\nu}^{\text{ext}}\,\dot{x}^{\nu}
> $$
>
> for the centroid worldline, with **the same** m and Q
> derived in earlier tracks.
>
> **(F18) Minimal coupling is geometric.**  The minimal-coupling
> prescription D_μ = ∂_μ − i(Q/ℏ) A_μ^ext is *derived*, not
> postulated, in this 6D KK setting.  The off-diagonal metric
> component G^μ4 = −A^μ_ext, when separated from the compact-
> mode wavefunction, produces the gauge-covariant derivative
> with exactly the coefficients required by minimal coupling.
> This is the 2-torus generalization of Klein's original
> observation in 5D.
>
> **(F19) Shear is mass-only at the centroid level.**  The
> internal shear g_45 — which mediates mass-charge mixing in
> the spectrum (F9) and parametrizes the (n_r − s n_t)
> combination in MaSt's mass formula (F11) — does *not* enter
> the gauge-covariant derivative.  It modifies which integer
> pairs (n_t, n_r) give which masses, but it does not
> contribute to the Q/m coupling that determines centroid
> response to an external field.  Mass-charge mixing is a
> spectrum phenomenon; the Lorentz-force coefficient is
> shear-independent given the eigenvalues.

F17 closes the single-sheet "electron from light" arc.  Mass,
charge, and the Lorentz force coupling of any 2-torus
standing-wave eigenstate are now all derived from the same
underlying compact momenta P_a, with no remaining
postulates other than the 6D massless wave equation and the
tube-couples convention.  What remains for the full electron
is spin (and, gated by spin, the magnetic moment).
