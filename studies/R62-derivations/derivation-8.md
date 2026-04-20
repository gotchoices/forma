# Derivation 8 — Cross-shears between two 2-tori

**Program 1, Track 8.**  Extend the Kaluza–Klein
machinery of derivations 2–6 from a single 2-torus
(4 + 2 = 6D) to two 2-tori with mutual cross-shear
couplings (4 + 4 = 8D).  The deliverables are:

1. A generalized 4D rest-mass formula
   $$
   m^2 c^2 \;=\; h^{ab}\,p_a\,p_b,
   \qquad a, b \in \{4, 5, 6, 7\},
   $$
   in which the inverse internal metric h^{ab} is now a
   4×4 matrix spanning both tori.
2. An explicit account of how *cross-shears* — the
   four off-block entries of the 4×4 internal metric
   that couple sheet A to sheet B — mediate
   **mass-eigenstate mixing** between single-sheet
   states, using the standard Schur-complement
   structure of block matrix inversion.
3. A generalized Lorentz force with four Kaluza–Klein
   U(1) gauge potentials (two per sheet) and a check
   that Tracks 2–6 are recovered in the zero-cross-
   shear limit.

No new physical postulate is introduced.  The entire
derivation is metric algebra on top of the 6D KK setup
of derivations 2–6.  Single-torus lemmas F3, F4, F7,
F11, F14, F17 are cited at the points where they are
being generalized.

---

## Inputs

1. **F3 / F4** (derivation-2): the KK reduction
   procedure and the U(1)×U(1) gauge structure that
   emerges from a 6D metric with two compact Killing
   vectors.

2. **F7 / F11** (derivations 3 and 4): the single-
   torus mass formula m² c² = h^{ab} p_a p_b with
   a, b ∈ {4, 5} and h^{ab} the 2×2 inverse internal
   metric.

3. **F14** (derivation 5): the tube-couples
   convention — the tube Killing momentum sets the
   4D electric charge (per sheet), while the ring
   momentum is conserved but electromagnetically dark.

4. **F17** (derivation 6): the generalized 4D Lorentz
   force acting on the standing-wave eigenstate,
   mediated by the KK gauge potentials descended from
   the off-diagonal metric components g_{μa}.

5. **R54 numerical compound-mode findings.**  The R54
   study observed compound eigenstates of a three-sheet
   T⁶ with numerically fitted cross-shears.  Track 8
   derives the analytical mechanism underlying those
   findings in the two-sheet case.

No quantum input beyond F7 (Planck-Einstein relation
already in place) is introduced.  The derivation is
GRID-native throughout: it uses only the bosonic
metric, compact momenta, and gauge potentials, all of
which are directly realized by GRID's phase field and
its link connections.

---

## Section A — 8D setup and the 4×4 internal metric

### A.1 — Coordinates

> *Purpose: fix conventions for the 8-dimensional
> manifold M⁴ × T_A × T_B and name the two tori.*

Let coordinates on the full 8-dimensional manifold be

$$
x^A \;=\; (x^\mu,\, y^a),
\qquad \mu \in \{0, 1, 2, 3\},
\qquad a \in \{4, 5, 6, 7\}.
$$

The non-compact directions x^μ span 4D Minkowski space
M⁴ with metric η_{μν} = diag(−, +, +, +).  The compact
directions y^a are grouped as:

- **Sheet A** (torus T_A):  y^4 = tube direction (length
  L_4 = 2π R_4), y^5 = ring direction (length
  L_5 = 2π R_5).
- **Sheet B** (torus T_B):  y^6 = tube direction (length
  L_6 = 2π R_6), y^7 = ring direction (length
  L_7 = 2π R_7).

Each y^a is identified periodically, y^a ≡ y^a + L_a.
The full internal manifold is T_A × T_B, a 4-dimensional
compact flat space.

### A.2 — The 4×4 internal metric

> *Purpose: write the full internal block of the 8D
> metric and identify its independent components.*

The 8D metric, in block form (as in derivation-2 F4 for
a single torus), reads

$$
G_{AB}(x^\mu, y^a) \;=\;
\begin{pmatrix}
\eta_{\mu\nu} + h_{ab}\,A^a_\mu A^b_\nu & h_{ab}\,A^b_\mu \\[4pt]
h_{ab}\,A^b_\nu & h_{ab}
\end{pmatrix}. \tag{A.2.1}
$$

Here

- η_{μν} is 4D Minkowski,
- h_{ab} is the **internal 4×4 symmetric metric** with
  a, b ∈ {4, 5, 6, 7},
- A^a_μ(x) are the four KK gauge potentials, one per
  compact direction, descended from the off-block
  components G_{μa}.

The cylinder condition (extended from derivation-2) is

$$
\partial_a G_{BC} \;=\; 0 \qquad \text{for all } a \in \{4, 5, 6, 7\},
$$

i.e. the 8D metric is independent of all four compact
coordinates.  This grants four abelian Killing vectors
(Section B).

### A.3 — Parameter counting

> *Purpose: count the independent degrees of freedom of
> the 4×4 internal metric and identify which are new
> relative to Track 2.*

A 4×4 symmetric matrix has 10 independent entries.
Decompose h_{ab} in 2×2 blocks:

$$
h_{ab} \;=\;
\begin{pmatrix}
H_A & C \\[2pt]
C^\top & H_B
\end{pmatrix},
\qquad
H_A, H_B, C \in \mathbb{R}^{2\times 2}, \tag{A.3.1}
$$

with

- **H_A** = 2×2 symmetric metric of sheet A, with
  entries (h_{44}, h_{45}, h_{55}).  Three parameters;
  these are the single-torus entries of Track 2 (the
  (ε_A, s_A) of F11 applied to sheet A).
- **H_B** = 2×2 symmetric metric of sheet B, entries
  (h_{66}, h_{67}, h_{77}).  Three parameters;
  analogous (ε_B, s_B) for sheet B.
- **C** = 2×2 cross-shear block with entries
  (h_{46}, h_{47}, h_{56}, h_{57}).  Four parameters.
  These are **new relative to Track 2** — they do not
  exist in a single-torus calculation.  They are the
  **inter-sheet cross-shears**.

Totals: 3 + 3 + 4 = 10.  ✓

**Parametrization.**  For computational convenience, we
sometimes normalize H_A and H_B to unit determinants and
absorb the overall scales into radii; the cross-shear
block C then carries only the mixing information.  This
is the analog of the (ε, s) parametrization of F11
extended to two sheets.

**Positivity.**  For the internal metric to be
Riemannian (positive-definite), a necessary and
sufficient condition is that both H_A and the Schur
complement S ≡ H_B − C^⊤ H_A⁻¹ C be positive-definite
(Sylvester's criterion applied to the block form).
This places an upper bound on the cross-shear block C:
if the inter-sheet couplings are too strong, the
internal metric degenerates.  Below we will work in the
regime where h is positive-definite throughout.

---

## Section B — Killing vectors and compact momenta

### B.1 — Four abelian Killing vectors

> *Purpose: identify the conserved charges associated
> with translations along each compact direction.*

Under the cylinder condition of §A.2, each of the four
vector fields

$$
\xi_a \;=\; \frac{\partial}{\partial y^a},
\qquad a \in \{4, 5, 6, 7\}, \tag{B.1.1}
$$

is a Killing vector of G_{AB}.  This is the direct
extension of F3 / F4 from two to four compact directions.
Their Lie brackets vanish,

$$
[\xi_a, \xi_b] \;=\; 0 \qquad \text{for all } a, b,
$$

so the Killing algebra is the 4-dimensional abelian
algebra u(1)_4 ⊕ u(1)_5 ⊕ u(1)_6 ⊕ u(1)_7.

### B.2 — Conserved compact momenta

For any geodesic or wave-equation eigenstate on the 8D
manifold, each Killing vector produces a conserved
charge (Noether):

$$
p_a \;=\; G_{AB}\,\xi_a^B\, \frac{dx^A}{d\tau}
\;=\; G_{aA}\,\frac{dx^A}{d\tau}, \tag{B.2.1}
$$

the canonical momentum conjugate to y^a.  On the compact
directions, the quantization condition is the standard
Fourier one,

$$
p_a \;=\; \frac{n_a\,\hbar}{R_a},
\qquad n_a \in \mathbb{Z}, \tag{B.2.2}
$$

one integer winding number per compact direction.  The
four winding numbers (n_4, n_5, n_6, n_7) label the
standing-wave eigenstates.

**Notation.**  We write n = (n_A, n_B) with n_A ≡ (n_4,
n_5) the sheet-A winding pair and n_B ≡ (n_6, n_7) the
sheet-B pair.  Similarly p = (p_A, p_B) with p_A =
(p_4, p_5), p_B = (p_6, p_7).  An individual mode is
identified by its full winding 4-tuple (n_4, n_5, n_6,
n_7).

### B.3 — Classification of modes

A mode is called:

- **Pure sheet-A** if n_B = (0, 0).  Only sheet-A
  windings are non-zero; the mode lives entirely on
  torus T_A.
- **Pure sheet-B** if n_A = (0, 0).  Symmetric: lives
  entirely on T_B.
- **Compound** if both n_A ≠ (0, 0) and n_B ≠ (0, 0).
  Winds non-trivially on both tori.

We will show in §E that compound modes are generically
the mass eigenstates when cross-shears C ≠ 0; when
C = 0, single-sheet modes are the mass eigenstates.

---

## Section C — 8D null condition and 4D mass formula

### C.1 — The null-trajectory condition

> *Purpose: derive the 4D mass-shell condition from the
> 8D null condition for a photon.*

Following derivation 3 (Track 3), let the fundamental 8D
object be a photon — a null trajectory.  The 8D null
condition reads

$$
G_{AB}\,k^A\,k^B \;=\; 0, \tag{C.1.1}
$$

where k^A = dx^A/dτ is the 8D wave vector.  In block
form (A.2.1), with A^a_μ = 0 for a free-particle check
of the mass formula (gauge potentials are decoupled
here; they re-enter in the Lorentz force of §F),

$$
\eta_{\mu\nu}\,k^\mu\,k^\nu
\;+\; h_{ab}\,k^a\,k^b \;=\; 0. \tag{C.1.2}
$$

Identify the 4D wave vector k^μ with the physical
4-momentum of the 4D observer:

$$
k^\mu \;=\; \frac{p^\mu}{\hbar},
\qquad
p^\mu p_\mu \;=\; -\,m^2 c^2.
$$

The compact-direction wave vector is the quantized
momentum from (B.2.2):

$$
k^a \;=\; G^{aB}\,k_B \;=\; h^{ab}\,\frac{n_b}{R_b}.
$$

Substituting into (C.1.2) and rearranging gives:

$$
-\,\frac{m^2 c^2}{\hbar^2}
\;+\; h_{ab}\,h^{ac}\,h^{bd}\,\frac{n_c n_d}{R_c R_d}
\;=\; 0.
$$

Using h_{ab} h^{ac} = δ_a^{\ c} (h^{ab} is the inverse
of h_{ab}), this simplifies to

$$
\frac{m^2 c^2}{\hbar^2}
\;=\; h^{ab}\,\frac{n_a n_b}{R_a R_b}
\;=\; \frac{1}{\hbar^2}\,h^{ab}\,p_a\,p_b.
$$

Hence:

$$
\boxed{\;m^2 c^2 \;=\; h^{ab}\,p_a\,p_b,
\qquad a, b \in \{4, 5, 6, 7\}\;} \tag{C.1.3}
$$

with h^{ab} the **4×4 inverse of the full 4×4 internal
metric** (A.3.1).  This is the generalized mass formula
— the direct extension of F7 / F11 from two compact
dimensions to four.

**Structural fact.**  The mass formula has exactly the
same form as F7; only the rank of the internal metric
has changed.  Every single-torus result that depended
only on the algebraic structure of h^{ab} (not on its
dimension) extends to two tori without modification.
This is the principal simplification that makes Track 8
a short derivation.

### C.2 — Consistency with F7 / F11

In the limit where h_{ab} is block-diagonal (C = 0),

$$
h_{ab} \;=\;
\begin{pmatrix} H_A & 0 \\ 0 & H_B \end{pmatrix},
\qquad
h^{ab} \;=\;
\begin{pmatrix} H_A^{-1} & 0 \\ 0 & H_B^{-1} \end{pmatrix},
$$

so that (C.1.3) separates:

$$
m^2 c^2 \;=\; (H_A^{-1})^{ij}\,p_i\,p_j \;+\; (H_B^{-1})^{kl}\,p_k\,p_l,
$$

with i, j ∈ {4, 5} and k, l ∈ {6, 7}.  Each term is
exactly F7 / F11 for one sheet.  The two sheets
contribute additively to the mass-squared.  This is the
Track-2 recovery referenced in §A and revisited in §G.

---

## Section D — Block-inverse structure and the Schur complement

### D.1 — Block inverse of the 4×4 internal metric

> *Purpose: write h^{ab} explicitly in terms of H_A,
> H_B, and the cross-shear block C, so that the
> mass formula (C.1.3) can be analyzed sector by sector.*

Let h be as in (A.3.1).  The standard 2×2 block-inverse
formula gives

$$
h^{-1} \;=\;
\begin{pmatrix}
H_A^{-1} + H_A^{-1} C\,S^{-1}\,C^\top H_A^{-1}
& -\,H_A^{-1} C\,S^{-1} \\[4pt]
-\,S^{-1}\,C^\top H_A^{-1}
& S^{-1}
\end{pmatrix}, \tag{D.1.1}
$$

where

$$
S \;\equiv\; H_B \;-\; C^\top\,H_A^{-1}\,C \tag{D.1.2}
$$

is the **Schur complement** of the H_A block.  S is 2×2
symmetric and positive-definite whenever h is
positive-definite (§A.3).

An equivalent form, obtained by interchanging the roles
of A and B, is

$$
h^{-1} \;=\;
\begin{pmatrix}
\tilde S^{-1}
& -\,\tilde S^{-1} C\,H_B^{-1} \\[4pt]
-\,H_B^{-1} C^\top \tilde S^{-1}
& H_B^{-1} + H_B^{-1} C^\top \tilde S^{-1} C\,H_B^{-1}
\end{pmatrix}, \tag{D.1.3}
$$

with 𝑆̃ = H_A − C H_B^{-1} C^⊤ the Schur complement of
the H_B block.  (D.1.1) and (D.1.3) are algebraically
equivalent; use whichever one isolates the sector of
interest.

### D.2 — Mass formula in block form

Substituting (D.1.1) into (C.1.3) gives, in block form,

$$
m^2 c^2 \;=\; p_A^\top (h^{-1})_{AA}\, p_A
\;+\; 2\, p_A^\top (h^{-1})_{AB}\, p_B
\;+\; p_B^\top (h^{-1})_{BB}\, p_B, \tag{D.2.1}
$$

where p_A = (p_4, p_5)^⊤ and p_B = (p_6, p_7)^⊤ and the
blocks of h^{-1} come from (D.1.1).  Explicitly:

$$
m^2 c^2
\;=\; p_A^\top H_A^{-1} p_A
\;+\; p_B^\top S^{-1} p_B
\;+\; (p_A^\top H_A^{-1} C - p_B^\top)\,S^{-1}\,(C^\top H_A^{-1} p_A - p_B),
$$

which, after simplification, reduces more transparently to

$$
\boxed{\;
m^2 c^2 \;=\; p_A^\top H_A^{-1} p_A
\;+\; q^\top S^{-1} q,
\qquad
q \;\equiv\; p_B \;-\; C^\top H_A^{-1} p_A
\;}
\tag{D.2.2}
$$

(the identity is an algebraic rearrangement of D.2.1
using the explicit block inverse; it can be verified
directly.)  **This is the cleanest form of the mass
formula** because it manifestly separates the two
sheets:

- The first term is the pure sheet-A mass contribution,
  identical to F7 / F11 for sheet A alone.
- The second term is a sheet-B contribution with
  **shifted** momenta q — where the shift q − p_B =
  −C^⊤ H_A^{-1} p_A is generated entirely by the cross-
  shear block C acting on the sheet-A momenta.

When C = 0, q = p_B and S = H_B, and (D.2.2) becomes
the sum of two independent single-sheet contributions.
The cross-shear block C thus appears as a **kinematic
shift** of the sheet-B momenta by an amount proportional
to the sheet-A momenta.  This is the structural signal
of inter-sheet mixing.

---

## Section E — Compound modes and mass-eigenstate mixing

### E.1 — Mass eigenstates are diagonal in the 4-winding basis

> *Purpose: identify mass eigenstates and show how
> cross-shears couple them.*

Each standing-wave eigenstate of the 8D KK reduction is
labelled by its 4-tuple of winding numbers n = (n_4,
n_5, n_6, n_7) ∈ ℤ^4 (F5 extended to four compact
directions).  In this winding basis, the mass-squared
operator is the **quadratic form**

$$
M^2(n) \;\equiv\; m^2(n) c^2
\;=\; \hbar^2 \,h^{ab}\,\frac{n_a n_b}{R_a R_b}, \tag{E.1.1}
$$

with h^{ab} the 4×4 inverse metric from (D.1.1).
Eigenstates of M^2 are simply points of the integer
lattice ℤ^4 — each (n_4, n_5, n_6, n_7) is already a
sharp mass eigenstate.

**There is no diagonalization to do over wave functions.**
The quantum numbers (n_4, n_5, n_6, n_7) are good
quantum numbers because each n_a is the eigenvalue of a
commuting Killing-vector charge (§B.1).  What the
cross-shears do affect is the **mass spectrum** — i.e.,
how the scalar mass M(n) depends on the four integers.

### E.2 — The "compound mode" phenomenon

> *Purpose: explain what R54 meant by a compound mode
> and identify its analytical origin.*

Call a mode **pure sheet-A** if n_B = 0, **pure sheet-B**
if n_A = 0, and **compound** if both n_A ≠ 0 and n_B ≠
0.

**Observation.**  When C = 0, the mass of a compound
mode equals the sum of the masses-squared of its
pure-sheet projections:

$$
M^2(n_A, n_B) \;=\; M_A^2(n_A) + M_B^2(n_B)
\qquad (\text{at } C = 0). \tag{E.2.1}
$$

When C ≠ 0, (D.2.2) shows that the sheet-B contribution
is computed with shifted momenta q, not p_B.  The effective
sheet-B mass that a compound mode carries is therefore

$$
M_{B,\text{eff}}^2(n_A, n_B)
\;=\; \hbar^2 \, q^\top S^{-1} q\,/\,R_B^2,
\qquad q \;=\; p_B - C^\top H_A^{-1} p_A, \tag{E.2.2}
$$

which depends on **both** n_A and n_B.  The pure-sheet
decomposition (E.2.1) no longer holds.

This is what "compound mode" means in practice: a mode
whose mass cannot be written as a sum of sheet
contributions with sheet-labeled momenta.  It is a
genuine eigenstate of the full 4-winding mass operator,
not a product of sheet eigenstates.

### E.3 — Kinematic mass–charge mixing

> *Purpose: document the consequence for charge
> assignments.*

Under the tube-couples convention of F14 extended to
two sheets:

- Sheet-A electric charge:  Q_A = e_A × n_4  (the sheet-
  A tube winding).
- Sheet-B electric charge:  Q_B = e_B × n_6  (the sheet-
  B tube winding).

A compound mode with (n_4, n_5, n_6, n_7) = (1, 0, 1, 0)
carries **both** Q_A and Q_B.  Under the MaSt universal
charge convention (F15 extension), these are combined
into a single observable electric charge with
sheet-dependent signs (σ_e, σ_ν, σ_p for the three
sheets; for Track 8's two-sheet case the signs are
whatever the project ultimately adopts).

Mass and charge are therefore **kinematically
decoupled at the quantum-number level**: the four
winding numbers (n_4, n_5, n_6, n_7) are the common
eigenvalues, and both mass (via h^{ab}) and charge (via
the tube-couples convention) are functions of them.
The cross-shear block C enters only the mass formula —
it does not modify the charge assignments.

**This is a key structural feature.**  The cross-shears
that modify the mass spectrum do not modify which
U(1)'s the particles couple to, nor the quantization
of their charges.  Charge is a Killing-vector eigenvalue
(§B.1, derivation 5); its integer quantization is
independent of the internal metric.  Cross-shears
shift masses without shifting charges.

---

## Section F — Generalized Lorentz force with four U(1) gauge fields

### F.1 — Four KK gauge potentials

> *Purpose: extend F17 from two to four U(1) gauge
> potentials.*

The off-block components A^a_μ(x) of the 8D metric
(A.2.1) are four independent 4D gauge potentials:

- **A^4_μ(x)** — sheet-A tube gauge potential
- **A^5_μ(x)** — sheet-A ring gauge potential
- **A^6_μ(x)** — sheet-B tube gauge potential
- **A^7_μ(x)** — sheet-B ring gauge potential

Each is associated with one of the abelian Killing
vectors of §B.  Under the tube-couples convention of
F14, A^4_μ and A^6_μ are identified with the sheet-A and
sheet-B electromagnetic potentials; A^5_μ and A^7_μ are
conserved but electromagnetically dark (they couple to
the ring momenta p_5 and p_7, which F14 identified as
dark charges).

### F.2 — Generalized Lorentz force

Repeating the reasoning of derivation 6 (Track 6) with
four Killing-vector charges instead of two, the 4D
Lorentz force on a standing-wave eigenstate of winding
(n_4, n_5, n_6, n_7) is

$$
\frac{dp^\mu}{d\tau}
\;=\; \sum_{a = 4}^{7} \, n_a\,F^a{}^\mu{}_\nu\,\frac{dx^\nu}{d\tau}, \tag{F.2.1}
$$

where F^a_{μν} = ∂_μ A^a_ν − ∂_ν A^a_μ is the 4D field
strength of the a-th KK U(1).  Each winding contributes
a Lorentz term weighted by the corresponding winding
number.

Under the tube-couples convention, only a = 4 and a = 6
produce external electromagnetic forces; a = 5 and a = 7
couple to dark gauge potentials that do not participate
in 4D electromagnetic interactions.  In the electron +
proton case (one sheet per particle family), the
electric Lorentz force acts as

$$
\frac{dp^\mu}{d\tau}
\;=\; e_A n_4 F^{\text{EM}}{}^\mu{}_\nu\,\frac{dx^\nu}{d\tau}
\quad (\text{sheet A})
\qquad \text{or} \qquad
e_B n_6 F^{\text{EM}}{}^\mu{}_\nu\,\frac{dx^\nu}{d\tau}
\quad (\text{sheet B}),
$$

which is F17 extended to two sheets with independent
electric sectors.

**No new physics.**  The Lorentz force derivation of
Track 6 is per-Killing-vector.  Adding more Killing
vectors simply produces more force terms.  Cross-shears
C do not appear in (F.2.1) — they enter only the mass
(via h^{ab}) and therefore only the *inertial* side of
the equation of motion, not the coupling side.

---

## Section G — Zero-cross-shear limit recovers Track 2

### G.1 — Setting C = 0

When the cross-shear block C = 0, the 4×4 internal
metric (A.3.1) becomes block-diagonal:

$$
h_{ab}\bigg|_{C = 0}
\;=\;
\begin{pmatrix} H_A & 0 \\ 0 & H_B \end{pmatrix}, \qquad
h^{ab}\bigg|_{C = 0}
\;=\;
\begin{pmatrix} H_A^{-1} & 0 \\ 0 & H_B^{-1} \end{pmatrix}.
$$

The Schur complement (D.1.2) simplifies to S = H_B and
the shifted momentum q = p_B.  The mass formula (D.2.2)
becomes

$$
m^2 c^2 \big|_{C = 0}
\;=\; p_A^\top H_A^{-1} p_A + p_B^\top H_B^{-1} p_B. \tag{G.1.1}
$$

This is exactly the sum of two independent Track-2 /
F11 mass contributions — one per sheet.  Pure sheet-A
modes have p_B = 0 and carry F7 mass with H_A; pure
sheet-B modes have p_A = 0 and carry F7 mass with H_B.
Compound modes become pure superpositions (E.2.1 holds
with equality).

### G.2 — Gauge and Lorentz structure also decouples

At C = 0, the four Killing charges separate into two
decoupled U(1)×U(1) pairs: {n_4, n_5} (sheet A) and
{n_6, n_7} (sheet B).  The Lorentz-force equation
(F.2.1) reduces to two independent Track-6 equations,
one per sheet.  No cross-sheet coupling exists: a
particle living on sheet A cannot feel sheet-B gauge
fields, and vice versa.

### G.3 — Summary of the limit

| Quantity | 4×4 metric (general) | 2×2 metric (Track 2) |
|---|---|---|
| Rank of internal metric | 4 | 2 |
| Killing vectors | 4 (u(1)^4) | 2 (u(1)^2) |
| Winding labels | (n_4, n_5, n_6, n_7) | (n_t, n_r) |
| Mass formula | h^{ab} p_a p_b, 4-sum | h^{ab} p_a p_b, 2-sum |
| Compound modes exist? | Yes (generic, C ≠ 0) | N/A (single sheet) |
| Decouples at C = 0? | To two copies of Track 2 | — |

**Lineage clean.**  Track 8 contains Track 2 strictly,
reduces to Track 2 on setting C = 0, and introduces
exactly one new structural element relative to Track 2:
the cross-shear block C that couples sheet A to sheet B.

---

## Section H — Worked example: rank-1 cross-shear, isotropic sheets

### H.1 — A minimal non-trivial case

For clarity we take the two tori to have equal radii
R_A = R_B = R (so that the expressions below are
algebraically clean; the generic R_A ≠ R_B case has
the same structure with R-ratios carried through).
Take diagonal intra-sheet metrics and a rank-1 cross-
shear:

$$
H_A \;=\; R^2\,I_2,
\qquad
H_B \;=\; R^2\,I_2,
\qquad
C \;=\; R^2\,\sigma\,\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix},
$$

with σ ∈ [0, 1) the dimensionless **cross-shear
magnitude**.  The metric couples only the sheet-A tube
(y^4) to the sheet-B tube (y^6); the two rings remain
uncoupled.

The 4×4 internal metric is

$$
h_{ab}
\;=\;
R^2
\begin{pmatrix}
1 & 0 & \sigma & 0 \\
0 & 1 & 0 & 0 \\
\sigma & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}.
$$

The Schur complement of the H_A block is

$$
S \;=\; H_B - C^\top H_A^{-1} C
\;=\;
R^2\,I_2 - R^2 \sigma^2
\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}
\;=\;
R^2
\begin{pmatrix}
1 - \sigma^2 & 0 \\
0 & 1
\end{pmatrix}.
$$

Positive-definiteness requires σ < 1 (as expected).

### H.2 — Mass formula for this example

Using (D.2.2) with p_A = (p_4, p_5)^⊤ and p_B = (p_6, p_7)^⊤,
compute q = p_B − C^⊤ H_A^{−1} p_A = (p_6 − σ p_4, p_7)^⊤,
so

$$
m^2 c^2
\;=\; \frac{p_4^2 + p_5^2}{R^2}
\;+\; \frac{(p_6 - \sigma\, p_4)^2}{R^2 (1 - \sigma^2)}
\;+\; \frac{p_7^2}{R^2}. \tag{H.2.1}
$$

With p_a = n_a ℏ / R (uniform radius):

$$
\frac{m^2 c^2}{\hbar^2}
\;=\; \frac{n_4^2 + n_5^2}{R^4}
\;+\; \frac{(n_6 - \sigma\,n_4)^2}{R^4 (1 - \sigma^2)}
\;+\; \frac{n_7^2}{R^4}. \tag{H.2.2}
$$

### H.3 — What this shows

- **At σ = 0:** (H.2.2) is the sum of two independent
  single-torus mass formulas.  Pure sheet-A modes: only
  the first term (plus n_7 = 0).  Pure sheet-B modes:
  only the second (which at σ = 0 reduces to n_6²/R⁴)
  plus the third term.
- **At σ ≠ 0:** a mode with n_4 ≠ 0 has an effective
  sheet-B tube winding n_6 → n_6 − σ n_4.  A "pure
  sheet-A" mode at σ = 0 (with n_B = 0) acquires an
  **effective** sheet-B tube excitation of magnitude
  σ n_4 at σ ≠ 0.  Its mass is shifted, but its charge
  quantum numbers (n_4, n_5, n_6, n_7) are unchanged.
- **Mass-degenerate compound modes.** The pair (n_4,
  n_5, n_6, n_7) = (1, 0, σ, 0) would be mass-
  degenerate with the pure sheet-A (1, 0, 0, 0) at
  σ = 0.  At σ ≠ 0, the mass split depends on the
  specific σ and integer combinations.  This is the
  analytical origin of R54's observed spectrum
  degeneracies and splittings.

This worked example is the minimal non-trivial case
that exhibits all the structural features: kinematic
momentum shift, Schur-complement-controlled mass
splitting, and the decoupling of charge from mass-
eigenstate mixing.  The general case follows the same
pattern with the 4 cross-shear parameters instead of
just σ.

---

## Section I — Contact with R54 and the path to T⁶

### I.1 — Analytical versus numerical compound modes

The R54 study fitted compound eigenstates on a three-
sheet T⁶ (electron + neutrino + proton sheets) with
numerically chosen cross-shears and observed that

- compound eigenstates are generic whenever any cross-
  shear is non-zero,
- their masses depend on the cross-shear values in a
  way that R54 characterized numerically but did not
  write out in closed form,
- the mode inventory (which compound modes exist at
  what mass) depends on the full cross-shear
  configuration.

Track 8 provides the analytical counterpart for the
two-sheet case.  The mass formula (D.2.2) with the
Schur-complement structure (D.1.2) is the closed form
underlying R54's numerical findings.  For the two-sheet
case:

- Compound modes have mass given by (D.2.2) with q =
  p_B − C^⊤ H_A^{−1} p_A.
- Degeneracies at C = 0 are lifted by the Schur-
  complement deviation S − H_B = −C^⊤ H_A^{−1} C.
- The mixing magnitude is controlled by ‖C‖ (in the
  operator norm) relative to √‖H_A‖·‖H_B‖.

### I.2 — The path to the full T⁶

The three-sheet T⁶ case (electron + neutrino + proton,
as in MaSt's model-E) is a direct generalization of
Track 8.  The internal metric becomes 6×6 with:

- 3 × 3 = 9 intra-sheet entries (3 per sheet),
- 6 × 2 = 12 inter-sheet cross-shear entries (one 2×2
  block per sheet pair, three pairs: e-ν, e-p, ν-p),

for a total of 21 independent entries in the 6×6
symmetric matrix (matching 6·7/2 = 21).  The mass
formula has the same structure as (C.1.3) with the
sum now running over a, b ∈ {1, 2, 3, 4, 5, 6}
(MaSt's standard six-compact-index convention).

The block-inverse structure (D.1) generalizes via
iterated Schur complements: one can peel off sheets
one at a time.  The generalized Lorentz force (F.2.1)
gets six terms, one per Killing vector; under the F15
universal convention, three of them (the tube directions
of each sheet) contribute to the observable Q = e(−n_1 +
n_5), with n_3 (neutrino tube) dark by the σ_ν = 0
assignment.

The three-sheet extension is *bookkeeping* on top of
Track 8: the algebra is identical, just with larger
matrices.  The new content of that extension is the
identification of which MaSt particles correspond to
which winding configurations in the enlarged mode
catalog — i.e., the phenomenology, not the kinematics.

### I.3 — Implications for the open spin question

The spin question (Track 7) was posed on a single 2-
torus.  On a single T², the Killing algebra is u(1) ⊕
u(1) — abelian — and cannot close to a non-abelian
so(3) needed for spin-½ by the Horoto–Scholtz
mechanism.  **On the enlarged T^{2n} (with n ≥ 2
sheets and cross-shears), the Killing algebra remains
abelian as derived in §B.1.**  Cross-shears do not
introduce non-abelian structure by themselves — they
only modify the metric, not the Killing bracket.

This is a non-trivial observation: extending to T⁴
(Track 8) or to the full T⁶ does not, by itself,
resolve the spin-½ Killing-vector obstruction of
derivation 7a.  The spin question will require a
*separate* structural addition (curvature, non-trivial
topology, or a Dirac–Kähler lift to spinor fields) on
top of the cross-shear structure derived here.  Track
8 thus clarifies the spin obstruction: the metric
algebra of cross-shears alone is not enough.

---

## Lemma (Track 8 result)

We have shown:

> **(F25) Generalized mass formula on T⁴ (two 2-tori).**
> For a photon-like null trajectory on M⁴ × T_A × T_B
> with cylinder-condition 8D metric
> G_{AB}, the 4D rest mass of a standing-wave eigenstate
> with winding numbers (n_4, n_5, n_6, n_7) is
>
> $$
> m^2 c^2 \;=\; h^{ab}\,p_a\,p_b
> \;=\; \hbar^2\,h^{ab}\,\frac{n_a n_b}{R_a R_b},
> \qquad a, b \in \{4, 5, 6, 7\},
> $$
>
> with h^{ab} the 4×4 inverse of the internal metric.
> This extends F7 / F11 from a single sheared 2-torus
> to two 2-tori coupled by a 2×2 cross-shear block C.
>
> **(F26) Compound modes from cross-shear.**  When the
> cross-shear block C = 0, mass eigenstates decompose
> into pure sheet-A and pure sheet-B modes with
> additive masses-squared.  When C ≠ 0, the mass
> formula acquires a Schur-complement structure
> (D.2.2) that couples sheet-A and sheet-B momenta:
>
> $$
> m^2 c^2 \;=\; p_A^\top H_A^{-1} p_A + q^\top S^{-1} q,
> \qquad q = p_B - C^\top H_A^{-1} p_A,
> \qquad S = H_B - C^\top H_A^{-1} C.
> $$
>
> Compound modes — modes with both n_A ≠ 0 and n_B ≠ 0 —
> are the generic mass eigenstates of the C ≠ 0 case.
> This is the analytical mechanism underlying R54's
> numerical compound-mode findings.
>
> **(F27) Kinematic mass–charge decoupling.**
> Electric charges under the tube-couples convention
> (F14 per sheet) depend only on the tube winding
> integers (n_4 for sheet A, n_6 for sheet B) and are
> unaffected by the cross-shear block C.  Cross-shears
> shift masses without shifting charges.  The Killing-
> vector eigenvalues (n_4, n_5, n_6, n_7) are the common
> quantum numbers; mass is a C-dependent functional of
> them (F25), charge is C-independent (F14 extended).
>
> **(F28) Recovery of Track 2.**  Setting C = 0 in F25
> and F26 reduces the mass formula to the sum of two
> independent Track-2 (F7/F11) contributions, one per
> sheet.  The four U(1) gauge potentials A^a_μ
> (a = 4, 5, 6, 7) decouple into two non-interacting
> U(1) × U(1) pairs.  The magnetic-moment corollary (a
> spin-dependent extension) and the three-sheet T⁶
> extension can both be built on top of this track:
> the magnetic moment by applying F25–F27 to the
> single-sheet limit (recovering Track 6's Lorentz
> force with a spin-carrying state), and the T⁶
> extension by iterating the block-inverse structure of
> D.1 one more time.

F25–F28 establish the two-sheet KK reduction as a direct
extension of Tracks 2–6 with a single new structural
ingredient (the cross-shear block C).  The extension is
algebraic and introduces no new physical postulate.
GRID-compatibility is preserved: the entire derivation
uses only the bosonic metric and its Killing structure.
The full T⁶ case (three sheets, 12 cross-shears) is
bookkeeping on top of Track 8 and is the natural next
consolidation step.  The analytical substrate needed
for any future cross-sheet spin-½ mechanism is in place;
whether such a mechanism actually arises from non-
abelian closure of cross-sheared Killing generators
(as hypothesized in F23 of derivation-7a) remains an
open question — but one that can now be framed
precisely against the T⁴ structure derived here.
