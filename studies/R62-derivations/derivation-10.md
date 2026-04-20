# Derivation 10 — Full 6D MaSt with three 2-tori and all cross-shears

**Program 1, Track 10.**  Extend the Kaluza–Klein
machinery from two 2-tori (Track 8) to **three 2-tori
with all inter-sheet cross-shears** — the geometry
MaSt's model-E actually uses.  The compact manifold is
T_e × T_ν × T_p (electron sheet × neutrino sheet ×
proton sheet), total internal dimension 6, so the full
spacetime is M⁴ × T⁶, 4 + 6 = 10 dimensions.

The deliverables are:

1. The 4D rest-mass formula on the 6×6 internal
   metric:
   $$
   m^2 c^2 \;=\; h^{ab}\,p_a\,p_b,
   \qquad a, b \in \{1, 2, 3, 4, 5, 6\},
   $$
   in MaSt's standard compact-index convention (§A).
2. An **iterated-Schur-complement** form of h^{-1}
   that peels off sheets one at a time, producing a
   three-level hierarchical mass formula in which
   each sheet contributes with progressively shifted
   compact momenta (§E).
3. The **universal charge formula** Q = e(−n_1 + n_5),
   recovered as the sum of three independent
   tube-couples conventions with MaSt's empirical
   sign assignment (σ_e, σ_ν, σ_p) = (−1, 0, +1)
   (§F).
4. A **six-term generalized Lorentz force** acting on
   the standing-wave eigenstate, with three physical
   EM directions (the sheet tubes) and three dark
   (the sheet rings) (§G).
5. A **mode catalog** identifying the lowest winding
   configurations and their MaSt model-E particle
   interpretations (§H).
6. Explicit **consistency limits** that recover Track 8
   (C_νp = 0 plus drop sheet ν or p), Track 2 (any
   two sheets silent), and Track 9 (scale-invariance
   of the dimensionless mass formula) (§I).

No new physical postulate is introduced.  The entire
derivation is metric algebra on top of Tracks 1–9.
GRID-compatibility is preserved throughout: all inputs
are bosonic (metric, Killing vectors, standing-wave
quantization), all of which are native GRID content
under `grid/foundations.md` A1–A6.

---

## Inputs

1. **F7 / F11** (derivations 3, 4) — single-torus
   mass formula m² c² = h^{ab} p_a p_b.

2. **F14 / F15** (derivation 5) — tube-couples charge
   convention and MaSt's universal charge formula
   with empirical signs (σ_e, σ_ν, σ_p) = (−1, 0, +1).

3. **F17** (derivation 6) — generalized 4D Lorentz
   force on the standing-wave eigenstate, with one
   term per KK Killing vector.

4. **F25 / F26 / F27** (derivation 8) — the two-sheet
   extension: mass formula on 4×4 internal metric,
   compound modes from Schur-complement structure,
   kinematic mass–charge decoupling.

5. **F29** (derivation 9) — the KK-on-torus
   derivations depend on R only through an overall
   scale m_c = ℏ/(Rc); the dimensionless mass formula
   is scale-invariant.

6. **MaSt's compact-index convention.**  The six
   compact coordinates are labelled (y^1, y^2, y^3,
   y^4, y^5, y^6) = (tube_e, ring_e, tube_ν, ring_ν,
   tube_p, ring_p).  This is the convention used in
   F15 and in model-E.  Tracks 2 and 8 used index
   offsets {4, 5} and {4, 5, 6, 7} respectively to
   stay visually distinct from the 4D spacetime
   indices; Track 10 adopts MaSt's 1–6 labelling to
   match existing project conventions for the full
   three-sheet case.

No new quantum input beyond F7 is introduced.

---

## Section A — 10D setup

### A.1 — Coordinates and metric

> *Purpose: fix the 10-dimensional manifold and name
> the three tori.*

Let coordinates on the full 10-dimensional manifold be

$$
x^A \;=\; (x^\mu,\, y^a),
\qquad \mu \in \{0, 1, 2, 3\},
\qquad a \in \{1, 2, 3, 4, 5, 6\}.
$$

- **x^μ**: non-compact 4D Minkowski coordinates with
  metric η_{μν} = diag(−, +, +, +).
- **y^1, y^2**: electron sheet, T_e.  y^1 = tube,
  y^2 = ring.  Periods L_1 = 2π R_1, L_2 = 2π R_2.
- **y^3, y^4**: neutrino sheet, T_ν.  y^3 = tube,
  y^4 = ring.  Periods L_3, L_4.
- **y^5, y^6**: proton sheet, T_p.  y^5 = tube,
  y^6 = ring.  Periods L_5, L_6.

The full compact manifold is T_e × T_ν × T_p, six-
dimensional flat compact.

The 10D metric has the standard KK block form (as in
F4 extended to three tori):

$$
G_{AB}(x^\mu, y^a)
\;=\;
\begin{pmatrix}
\eta_{\mu\nu} + h_{ab}\,A^a_\mu A^b_\nu & h_{ab}\,A^b_\mu \\[2pt]
h_{ab}\,A^b_\nu & h_{ab}
\end{pmatrix}, \tag{A.1.1}
$$

with six KK gauge potentials A^a_μ(x), one per
compact direction, and h_{ab} the **6×6 symmetric
internal metric**.

**Cylinder condition.**  The 10D metric is
independent of all six y^a:

$$
\partial_a G_{BC} \;=\; 0
\qquad \text{for all } a \in \{1, \ldots, 6\},
$$

granting six abelian Killing vectors (§C).

### A.2 — Scale conventions

Per F29, the compact radii R_a enter the derivation
only through quantized momenta p_a = n_a ℏ/R_a.  We
will factor out the overall mass scale at the end by
introducing Compton masses m_{c,a} = ℏ/(R_a c).  The
dimensionless shape matrix is Γ_{ab} = h_{ab}/R_a R_b
(or an obvious generalization when R_a vary per
direction); all physical conclusions depend only on
Γ^{ab} and the integers n_a.

---

## Section B — The 6×6 internal metric

### B.1 — Block decomposition

> *Purpose: organize the 21 independent entries of
> h_{ab} into intra-sheet and inter-sheet blocks.*

Decompose h_{ab} into nine 2×2 blocks, one per
(sheet, sheet) pair:

$$
h_{ab}
\;=\;
\begin{pmatrix}
H_e & C_{e\nu} & C_{ep} \\[2pt]
C_{e\nu}^\top & H_\nu & C_{\nu p} \\[2pt]
C_{ep}^\top & C_{\nu p}^\top & H_p
\end{pmatrix}, \tag{B.1.1}
$$

with

- **Intra-sheet metrics** H_e, H_ν, H_p ∈ ℝ^{2×2},
  each symmetric — three entries per sheet (the
  (ε, s) of F11 for each sheet):
  (h_{11}, h_{22}, h_{12}) for sheet e, analogous
  for ν and p.  **9 parameters** total.
- **Inter-sheet cross-shears** C_{eν}, C_{ep}, C_{νp}
  ∈ ℝ^{2×2}, general (not necessarily symmetric).  Each
  is a 2×2 block; three pairs of sheets gives three
  blocks, each with 4 entries.  **12 parameters**
  total.

Total: 9 + 12 = 21 independent entries = 6·7/2, as
expected for a 6×6 symmetric matrix.  ✓

The 12 cross-shear entries are the **new** degrees of
freedom beyond Track 8 (which had only one cross-
shear block C of 4 entries).  They encode all possible
inter-sheet couplings pairwise among the three sheets.

### B.2 — Positivity

h must be positive-definite for the internal geometry
to be Riemannian.  By Sylvester's criterion applied
hierarchically, this requires:

1. H_e positive-definite (sheet-e standalone check).
2. S_{ep} ≡ H_p − C_{ep}^⊤ H_e^{-1} C_{ep} positive-
   definite (sheet-e–dressed proton check).
3. The full 4×4 Schur complement of H_e in h
   (computed below in §E) positive-definite.

We work in the regime where all three conditions hold.
This places upper bounds on the cross-shear
magnitudes relative to the intra-sheet metrics — a
generalization of the σ < 1 condition of Track 8
§H.

### B.3 — Parameter taxonomy

For the three-sheet case, it is useful to catalog the
21 parameters as:

| Category | Count | Symbol(s) |
|---|---|---|
| Electron-sheet intra-metric | 3 | H_e: (ε_e, s_e) + overall R_e |
| Neutrino-sheet intra-metric | 3 | H_ν: (ε_ν, s_ν) + R_ν |
| Proton-sheet intra-metric | 3 | H_p: (ε_p, s_p) + R_p |
| e–ν cross-shear block | 4 | C_{eν} (four entries) |
| e–p cross-shear block | 4 | C_{ep} |
| ν–p cross-shear block | 4 | C_{νp} |
| **Total** | **21** | |

In model-E's phenomenological fits (R50, R54),
many of these entries are either zero by convention
or small and constrained by particle-mass data.
Track 10 derives the **kinematic consequence** of
having all 21 available; which subset is actually
realized is a phenomenological question that
model-E addresses numerically.

---

## Section C — Six Killing vectors and compact momenta

### C.1 — Six abelian Killing vectors

> *Purpose: identify the six conserved compact
> charges.*

Under the cylinder condition (§A.1), each of the six
vector fields

$$
\xi_a \;=\; \frac{\partial}{\partial y^a},
\qquad a \in \{1, 2, 3, 4, 5, 6\}, \tag{C.1.1}
$$

is a Killing vector of G_{AB}.  They all commute:

$$
[\xi_a, \xi_b] \;=\; 0 \qquad \text{for all } a, b.
$$

The Killing algebra is the 6-dimensional abelian
algebra

$$
\mathfrak{g} \;=\; \mathfrak{u}(1)^6
\;=\;
\mathfrak{u}(1)_{\text{tube}_e} \oplus
\mathfrak{u}(1)_{\text{ring}_e} \oplus
\mathfrak{u}(1)_{\text{tube}_\nu} \oplus
\mathfrak{u}(1)_{\text{ring}_\nu} \oplus
\mathfrak{u}(1)_{\text{tube}_p} \oplus
\mathfrak{u}(1)_{\text{ring}_p}.
$$

Cross-shears do **not** introduce non-abelian
structure (see Track 8 §I.3 for the same observation
in T⁴).  The Killing algebra remains abelian for any
3-sheet cross-shear configuration.  This is a
structural fact of compact flat tori, independent of
the metric off-diagonal content.

### C.2 — Quantized compact momenta

Each Killing vector produces a conserved Noether
charge — the canonical momentum conjugate to y^a:

$$
p_a \;=\; G_{aB}\,\frac{dx^B}{d\tau}
\;=\; n_a\,\hbar / R_a,
\qquad n_a \in \mathbb{Z}. \tag{C.2.1}
$$

The six winding integers (n_1, n_2, n_3, n_4, n_5,
n_6) label the standing-wave eigenstates.  They are
independent good quantum numbers because the six
Killing vectors commute.

**Notation.**  We group the six momenta as a
3-block vector of 2-vectors:

$$
p \;=\; (p_e,\, p_\nu,\, p_p)
\qquad \text{with}
\qquad
p_e = (p_1, p_2)^\top,\;\;
p_\nu = (p_3, p_4)^\top,\;\;
p_p = (p_5, p_6)^\top.
$$

Similarly n = (n_e, n_ν, n_p) with n_e = (n_1, n_2)^⊤
etc.

### C.3 — Classification of modes

A mode with winding n = (n_e, n_ν, n_p) is:

- **Pure sheet-e** if n_ν = n_p = 0.
- **Pure sheet-ν** if n_e = n_p = 0.
- **Pure sheet-p** if n_e = n_ν = 0.
- **Compound** if two or more of (n_e, n_ν, n_p) are
  non-zero.

Compound modes come in three pairwise flavors
(eν-compound, ep-compound, νp-compound) and one
three-way flavor (all three sheets active).  Track 10
produces the mass of each type as a function of the
21 metric parameters.

---

## Section D — 12D null condition and the mass formula

### D.1 — The mass formula

From the 10D null condition G^{AB} k_A k_B = 0 applied
to a standing-wave eigenstate with k^a = h^{ab} p_b /
ℏ, the same steps as §C of derivation 8 (which used
the 8D null condition) give

$$
\boxed{\;m^2 c^2 \;=\; h^{ab}\,p_a\,p_b,
\qquad a, b \in \{1, 2, 3, 4, 5, 6\}\;}  \tag{D.1.1}
$$

with h^{ab} the 6×6 inverse of the internal metric
(B.1.1).  Structurally identical to F7 / F25; only the
rank of the internal metric has changed.

**This is the direct extension** of the single-torus
formula (a, b range over {4, 5}), the two-torus
formula (over {4, 5, 6, 7}), and now the three-torus
formula (over {1, ..., 6} in MaSt's convention).  All
three live inside the same algebraic family m² c² =
h^{ab} p_a p_b.

### D.2 — Dimensionless form

Following F29, factor out the compact scales.  With
h_{ab} = R_a R_b Γ_{ab} (using a diagonal radius
prescription R_a for each direction; other conventions
differ only by reparametrization of Γ) and p_a =
n_a ℏ/R_a,

$$
m^2 c^2
\;=\; \frac{\hbar^2}{R_0^2}\,\Gamma^{ab}\,n_a\,n_b \cdot
\frac{R_0^2}{R_a R_b}. \tag{D.2.1}
$$

Introducing an overall reference scale R_0 (e.g.
R_0 = R_1 = R_e,tube) and the Compton mass m_{c,0} =
ℏ/(R_0 c), (D.2.1) becomes the dimensionless

$$
\left(\frac{m}{m_{c,0}}\right)^2 \;=\;
\tilde\Gamma^{ab}\,n_a\,n_b, \tag{D.2.2}
$$

with Γ̃ the dimensionless shape tensor.  All physical
mass ratios depend only on Γ̃ and the integer
windings — **not** on any compact scale.  This is F29
extended from one torus to three.  The compact scales
determine the overall mass scale but not the spectrum.

---

## Section E — Iterated Schur complement

### E.1 — Strategy

> *Purpose: write h^{-1} in a hierarchical form that
> exposes how each sheet contributes, and how cross-
> shears dress each sheet's effective metric.*

We apply Track 8's 2-block Schur-complement formula
**iteratively**.  First view h as a 2-block matrix
[e | (νp)]:

$$
h \;=\; \begin{pmatrix} H_e & \mathbf{C}_{e,\cdot} \\
                        \mathbf{C}_{e,\cdot}^\top & \mathbf{M}_{\nu p} \end{pmatrix}, \tag{E.1.1}
$$

with

$$
\mathbf{C}_{e,\cdot} \;\equiv\; (C_{e\nu},\; C_{ep})
\;\in\; \mathbb{R}^{2\times 4},
\qquad
\mathbf{M}_{\nu p} \;\equiv\;
\begin{pmatrix} H_\nu & C_{\nu p} \\ C_{\nu p}^\top & H_p \end{pmatrix}
\;\in\; \mathbb{R}^{4\times 4}.
$$

By Track 8's D.2.2 applied at this level,

$$
m^2 c^2
\;=\; p_e^\top H_e^{-1} p_e
\;+\; q_{\nu p}^\top (S_1)^{-1} q_{\nu p}, \tag{E.1.2}
$$

with

- **Shifted (ν, p) momentum**
  $q_{\nu p} \;=\; (p_\nu, p_p) - \mathbf{C}_{e,\cdot}^\top H_e^{-1} p_e \;\in\; \mathbb{R}^4$,
  shifted by an *amount set entirely by the electron
  sheet's compact momentum and cross-shears*.
- **Electron-dressed 4×4 Schur complement**
  $S_1 \;\equiv\; \mathbf{M}_{\nu p} - \mathbf{C}_{e,\cdot}^\top H_e^{-1} \mathbf{C}_{e,\cdot}$.

Expand S_1 in its own 2-block form:

$$
S_1
\;=\;
\begin{pmatrix}
H_\nu' & C_{\nu p}' \\
{C_{\nu p}'}^\top & H_p'
\end{pmatrix}, \tag{E.1.3}
$$

where the **electron-dressed** intra-sheet metrics
and cross-shear are

$$
H_\nu' \;\equiv\; H_\nu - C_{e\nu}^\top H_e^{-1} C_{e\nu},
$$
$$
H_p'\;\equiv\; H_p - C_{ep}^\top H_e^{-1} C_{ep},
$$
$$
C_{\nu p}' \;\equiv\; C_{\nu p} - C_{e\nu}^\top H_e^{-1} C_{ep}.
$$

Each dressed quantity is the original minus an
electron-sheet-mediated correction.

### E.2 — Second Schur step

Now apply Track 8's D.2.2 *again* to S_1, peeling off
the electron-dressed neutrino block:

$$
q_{\nu p}^\top (S_1)^{-1} q_{\nu p}
\;=\; q_\nu^\top (H_\nu')^{-1} q_\nu
\;+\; q_p'^\top (S_2)^{-1} q_p', \tag{E.2.1}
$$

with

- **Twice-shifted proton momentum**
  $q_p' \;=\; q_p - (C_{\nu p}')^\top (H_\nu')^{-1} q_\nu$,
  where q_p, q_ν are the two halves of q_{νp} from
  E.1.
- **Doubly-dressed proton Schur complement**
  $S_2 \;\equiv\; H_p' - (C_{\nu p}')^\top (H_\nu')^{-1} C_{\nu p}'$.

### E.3 — Three-level hierarchical mass formula

Combining (E.1.2) and (E.2.1),

$$
\boxed{\;
m^2 c^2
\;=\; p_e^\top H_e^{-1} p_e
\;+\; q_\nu^\top (H_\nu')^{-1} q_\nu
\;+\; q_p'^\top S_2^{-1} q_p'
\;} \tag{E.3.1}
$$

with the three momentum-shift definitions

$$
q_\nu \;=\; p_\nu - C_{e\nu}^\top H_e^{-1} p_e, \tag{E.3.2}
$$

$$
q_p \;=\; p_p - C_{ep}^\top H_e^{-1} p_e, \tag{E.3.3}
$$

$$
q_p' \;=\; q_p - (C_{\nu p}')^\top (H_\nu')^{-1} q_\nu. \tag{E.3.4}
$$

**Interpretation of (E.3.1).**

- Sheet e contributes its own F7 mass term,
  unmodified.
- Sheet ν contributes with shifted momentum q_ν — the
  shift is entirely from the electron sheet's e–ν
  cross-shear.
- Sheet p contributes with **doubly** shifted momentum
  q_p' — first shifted by the e–p cross-shear, then
  further by the electron-dressed ν–p cross-shear.

This hierarchy makes it completely explicit how cross-
shears mediate inter-sheet couplings.  Every sheet
after the first is "dressed" by the cross-shears to
all earlier sheets in the peel order.  The peel order
is arbitrary (e → ν → p here; swapping gives an
equivalent formula with different dressed quantities);
the final m² is peel-order-invariant.

### E.4 — Recovery of Track 8

Set C_{ep} = 0 and C_{νp} = 0, i.e. drop sheet p's
couplings to both e and ν.  Then H_p' = H_p, C_{νp}' =
C_{νp} − C_{eν}^⊤ H_e^{-1} · 0 = 0, and S_2 =
H_p − 0 = H_p.  Also q_p = p_p and q_p' = p_p − 0
(since C_{νp}' = 0), so q_p' = p_p.

(E.3.1) becomes

$$
m^2 c^2 \bigg|_{\text{drop sheet-p coupling}}
\;=\; p_e^\top H_e^{-1} p_e
\;+\; q_\nu^\top (H_\nu')^{-1} q_\nu
\;+\; p_p^\top H_p^{-1} p_p,
$$

which is the (e, ν) Track-8 two-sheet formula with an
**additive** decoupled sheet-p contribution — as
expected.  If we also drop C_{eν}, we get three
decoupled single-sheet contributions (Track 2 for
each).

### E.5 — Recovery of Track 2

Set all cross-shears to zero: C_{eν} = C_{ep} = C_{νp}
= 0.  Then H_ν' = H_ν, H_p' = H_p, S_2 = H_p, and all
shifts vanish (q_ν = p_ν, q_p = p_p, q_p' = p_p).
(E.3.1) becomes

$$
m^2 c^2 \bigg|_{\text{all cross-shears zero}}
\;=\; p_e^\top H_e^{-1} p_e + p_\nu^\top H_\nu^{-1} p_\nu + p_p^\top H_p^{-1} p_p,
$$

a sum of three independent F7 terms — three decoupled
copies of Track 2, one per sheet.  ✓

---

## Section F — Charge: the universal formula

### F.1 — Three tube-couples conventions

Per F14 (derivation 5), the tube momentum of a single
sheet is identified with the 4D electric charge via
the tube-couples convention.  Applying this to each of
the three sheets independently gives three
sheet-specific electric charges:

$$
Q_e \;=\; e\,\sigma_e\,n_1, \qquad
Q_\nu \;=\; e\,\sigma_\nu\,n_3, \qquad
Q_p \;=\; e\,\sigma_p\,n_5, \tag{F.1.1}
$$

where n_1, n_3, n_5 are the three tube windings and
σ_e, σ_ν, σ_p are the per-sheet sign conventions.

### F.2 — Empirical sign assignments

MaSt's model-E uses the assignment

$$
(\sigma_e,\,\sigma_\nu,\,\sigma_p) \;=\; (-1,\, 0,\, +1). \tag{F.2.1}
$$

The σ_ν = 0 assignment makes the neutrino sheet
electromagnetically dark — its tube winding n_3 is
conserved (a good Killing charge) but does not
couple to the observable EM gauge potential.  This
is the geometric origin of the neutrino's zero
electric charge in MaSt.  The σ_e = −1, σ_p = +1
assignment sets the relative sign of the electron
and proton elementary charges.

The sign vector (σ_e, σ_ν, σ_p) is an **empirical
input** to MaSt — it is not derived from the 10D
geometry.  It arises from the three sheets' identity
assignments, which is phenomenology.

### F.3 — Universal charge formula

Summing (F.1.1) and substituting (F.2.1),

$$
\boxed{\;
Q \;=\; Q_e + Q_\nu + Q_p
\;=\; e\,(-n_1 + n_5)\;} \tag{F.3.1}
$$

— MaSt's universal charge formula (F15).  The ring
windings n_2, n_4, n_6 are conserved but do not
appear in the electric charge; the neutrino tube
winding n_3 is conserved but silent by σ_ν = 0.
Charge is linear in the two physical tube windings
n_1 and n_5 with coefficients ∓e.

**Particle charges in this framework.**

| Mode (n_1, n_2, n_3, n_4, n_5, n_6) | Q |
|---|---|
| (1, 0, 0, 0, 0, 0)   | −e (electron-like) |
| (0, 0, 0, 0, 1, 0)   | +e (proton-like) |
| (0, 0, 1, 0, 0, 0)   | 0 (neutrino-like) |
| (0, 0, 1, 1, 0, 0)   | 0 (ν compound with its own ring) |
| (1, 0, 0, 0, 1, 0)   | 0 (eigencompound e+p; neutron-like?) |
| (1, 0, 1, 0, 0, 0)   | −e (e+ν compound) |
| (0, 0, 1, 0, 1, 0)   | +e (ν+p compound) |
| (−1, 0, 0, 0, 1, 0)  | +2e (unphysical? or exotic) |

The (1, 0, 0, 0, 1, 0) neutral compound is
structurally a candidate for a neutron-like bound
state — electron + proton with opposite charges
cancelling.  Whether this is the actual identity of
the neutron in MaSt's model-E, or whether the neutron
is a different compound (e.g. involving neutrino
winding), is a phenomenological question addressed by
the R53/R54 studies, not by Track 10.

### F.4 — Kinematic decoupling of mass and charge

**Charge depends only on tube windings n_1, n_5**
(F.3.1).  **Mass depends on all 21 metric parameters
and all 6 winding numbers** (E.3.1).

Cross-shears (12 of the 21 parameters) enter mass but
**not** charge.  This is F27 of Track 8 generalized to
three sheets: cross-shears shift masses via the
Schur-complement dressing, but charge is a pure
Killing-eigenvalue sum and is invariant under any
metric change.

**Consequence.**  Two modes with identical charge
(same n_1, n_5) can have different masses if their
other windings (n_2, n_3, n_4, n_6) or the cross-
shear configuration differ.  Conversely, modes with
very different n_1, n_5 can have similar masses if
the metric is chosen to balance them (mass
degeneracies from metric tuning, as R54 explores).

---

## Section G — Generalized Lorentz force

### G.1 — Six KK U(1) gauge potentials

The off-block 10D metric components yield six KK
gauge potentials A^a_μ(x), a = 1..6.  Under the
tube-couples convention with (F.2.1), only three
combinations are observed externally as
electromagnetism:

$$
A^{\text{EM}}_\mu \;\equiv\; \sigma_e A^1_\mu + \sigma_\nu A^3_\mu + \sigma_p A^5_\mu
\;=\; -A^1_\mu + A^5_\mu. \tag{G.1.1}
$$

The other five combinations (two more independent
linear combinations of the tube A's, plus all three
ring A's) are either dark (sheet-ν tube A^3_μ) or
not directly coupled to observable matter (the three
ring A's, by F14 ring-dark convention).

### G.2 — Lorentz force on the eigenstate

Repeating the derivation 6 logic with six Killing
charges:

$$
\frac{d p^\mu}{d\tau}
\;=\; \sum_{a=1}^{6} n_a\,F^a{}^\mu{}_\nu\,\frac{dx^\nu}{d\tau}, \tag{G.2.1}
$$

with F^a_{μν} = ∂_μ A^a_ν − ∂_ν A^a_μ the 4D field
strength of the a-th KK U(1).  Each winding contributes
an independent Lorentz term.

**Under the tube-couples convention**, terms a = 1
and a = 5 are the two physical electric-charge-
carrying ones; term a = 3 is dark (σ_ν = 0); terms
a = 2, 4, 6 are dark (rings).  For a particle with
winding pattern (n_1, 0, 0, 0, n_5, 0):

$$
\frac{d p^\mu}{d\tau}
\;=\; (-n_1 + n_5)\,e\,F^{\text{EM}}{}^\mu{}_\nu\,\frac{dx^\nu}{d\tau}
\;=\; Q\,F^{\text{EM}}{}^\mu{}_\nu\,\frac{dx^\nu}{d\tau},
$$

— the standard 4D Lorentz force with charge Q =
e(−n_1 + n_5) per F15.  For compound modes with
non-tube windings active, those components are
carried along as conserved but kinematically dark
charges (§F.4).

### G.3 — No cross-shear dependence

Cross-shears do **not** appear in (G.2.1) — they enter
only the *inertial* side of the equation of motion
(through the mass in the left-hand-side, via F25 /
E.3.1).  The coupling side has six terms weighted by
Killing eigenvalues, which are cross-shear independent.
This is the direct generalization of the same
observation in derivation 8 §F.

---

## Section H — Mode catalog

### H.1 — The lowest-winding modes

Table the pure single-sheet modes with winding
magnitudes ≤ 1 per direction:

| Mode | Sheet | (n₁,n₂,n₃,n₄,n₅,n₆) | Q | Identity sketch |
|---|---|---|---|---|
| e₁ | e | (1, 0, 0, 0, 0, 0) | −e | ground electron tube |
| e₂ | e | (0, 1, 0, 0, 0, 0) | 0 | e ring (dark) |
| e₃ | e | (1, 1, 0, 0, 0, 0) | −e | e tube + ring |
| e₄ | e | (1, 2, 0, 0, 0, 0) | −e | e (1,2) — model-E electron |
| ν₁ | ν | (0, 0, 1, 0, 0, 0) | 0 | ν tube (dark) |
| ν₂ | ν | (0, 0, 1, 1, 0, 0) | 0 | ν (1,1) |
| p₁ | p | (0, 0, 0, 0, 1, 0) | +e | p tube ground |
| p₂ | p | (0, 0, 0, 0, 1, 2) | +e | p (1,2) |
| p₃ | p | (0, 0, 0, 0, 1, 3) | +e | p (1,3) |

Per MaSt's phenomenological fits, the physical
electron is a sheet-e mode with some (n_1, n_2)
winding (not necessarily (1, 0) — model-E uses
(1, 2)); the proton is a sheet-p (1, n_p6) mode
(model-E leaves this open between (1, 2), (1, 3), and
(3, 6)); the neutrino is a sheet-ν mode with some
small winding.  The *kinematic* structure derived
here is the same for any choice of these; only the
mass values differ (via the metric parameters).

### H.2 — Compound modes

Compound modes with non-zero winding on two or more
sheets are the generic mass eigenstates when cross-
shears are non-zero (§E, F26 generalized to three
sheets).  Two examples are structurally interesting:

- **(1, 0, 0, 0, 1, 0):** charge Q = −e + e = 0.  A
  neutral compound of an electron sheet tube and a
  proton sheet tube.  Structurally a **neutron-like
  candidate**; whether this is the physical neutron's
  identity in MaSt or whether neutron involves
  neutrino-sheet winding too is a question for R53/
  R54 phenomenology.
- **(1, n_2, 1, n_4, 0, 0):** Q = −e.  An e–ν compound
  with electron charge.  Could be a candidate for
  heavier charged leptons (muon, tau) if the
  higher-winding/cross-shear mass corrections shift
  the mass upward by the right factors.  Again,
  phenomenological matching is the R-studies'
  territory, not Track 10's.

The key Track-10 statement is: these compound modes
**exist as sharp mass eigenstates** of the full T⁶
mass formula (E.3.1), with compound masses
controlled by the cross-shear configuration through
the iterated Schur complement.  The mode catalog
available to model-E is the integer lattice ℤ⁶,
filtered in the studies by R50-style high-pass
arguments to exclude UV ghosts.

### H.3 — Relation to model-E

Model-E (studies/R53, R54) fits a three-sheet T⁶
with specific cross-shear values and identifies
particles as specific compound modes with parity /
filter constraints.  Track 10 provides the
**analytical substrate** for those fits:

- The mass formula (D.1.1 / E.3.1) is the analytical
  ground truth that model-E's numerical mass-squared
  operator realizes.
- The cross-shear parameter count (12 inter-sheet
  entries) is the number of independent fit
  parameters model-E has available to match the
  inter-sheet mass splittings.
- The iterated Schur structure (E.3.1) lets one
  analyze perturbatively which sheet pairs dominate
  which compound-mode masses.

A full quantitative comparison — i.e., computing the
R54 spectrum from (E.3.1) with R54's fitted cross-
shears — is not part of Track 10 (it requires the
full 6×6 matrix inversion at fitted numerical values,
which is numerical phenomenology).  Track 10's
contribution is the closed-form expression that
underlies those numerics.

---

## Section I — Consistency checks

### I.1 — Track 8 recovery (two sheets)

Drop sheet p entirely by setting H_p = 0 and C_{ep}
= C_{νp} = 0 (interpreted as the limit where sheet p
is decoupled / absent).  The 6×6 metric reduces to a
4×4 metric on sheets (e, ν), (E.3.1) reduces to

$$
m^2 c^2 \;=\; p_e^\top H_e^{-1} p_e + q_\nu^\top (H_\nu')^{-1} q_\nu, \tag{I.1.1}
$$

which is Track 8's F25 / D.2.2 applied to sheets e
and ν.  ✓

Analogously for (e, p) or (ν, p) pairings by
decoupling the remaining sheet.

### I.2 — Track 2 recovery (one sheet)

Drop two sheets (say ν and p) entirely.  (E.3.1)
reduces to

$$
m^2 c^2 \;=\; p_e^\top H_e^{-1} p_e,
$$

the single-torus F7 / F11 mass formula for sheet e.
✓

### I.3 — Track 9 recovery (scale-invariance)

The dimensionless form (D.2.2) factors every R out of
the mass spectrum.  For the three-sheet case, there
are three Compton scales (m_{c,e}, m_{c,ν}, m_{c,p})
and the dimensionless spectrum depends on the 18
dimensionless *shape* parameters (ε, s per sheet = 6;
12 cross-shears, all dimensionless as ratios of
√(H_i)×√(H_j)).  Scale-invariance holds at the three-
sheet level with three independent scale factors.  ✓

### I.4 — GRID-compatibility

All inputs used are bosonic: the metric h_{ab}, the
Killing vectors ξ_a = ∂/∂y^a, the standing-wave
quantization, and the null-trajectory (massless
Klein-Gordon) condition.  These are directly realized
by GRID's axioms (bosonic U(1) phase field and its
exterior derivatives; grid/foundations.md A1–A6).  No
spinor structure is invoked — Track 10 is orthogonal
to the Track 7 spin trilemma and applies identically
under 7a, 7b, or 7c.  ✓

---

## Lemmas (Track 10 results)

We have established:

> **(F30) Mass formula on T⁶ (three 2-tori).**  For a
> photon-like null trajectory on M⁴ × T_e × T_ν × T_p
> with cylinder-condition 10D metric G_{AB}, the 4D
> rest mass of a standing-wave eigenstate with winding
> numbers (n_1, n_2, n_3, n_4, n_5, n_6) is
>
> $$
> m^2 c^2 \;=\; h^{ab}\,p_a\,p_b,
> \qquad a, b \in \{1, 2, 3, 4, 5, 6\},
> $$
>
> with h^{ab} the 6×6 inverse of the 21-parameter
> internal metric.  This extends F7 / F11 (one torus)
> and F25 (two tori) to the full MaSt three-sheet
> geometry.
>
> **(F31) Iterated Schur-complement structure.**  The
> mass formula can be written hierarchically,
>
> $$
> m^2 c^2
> \;=\; p_e^\top H_e^{-1} p_e
> \;+\; q_\nu^\top (H_\nu')^{-1} q_\nu
> \;+\; q_p'^\top S_2^{-1} q_p',
> $$
>
> with sheet-ν's momentum shifted by e (q_ν = p_ν −
> C_{eν}^⊤ H_e^{-1} p_e), sheet-p's momentum shifted
> by both e and the e-dressed ν (q_p' = p_p − C_{ep}^⊤
> H_e^{-1} p_e − (C_{νp}')^⊤ (H_ν')^{-1} q_ν), and
> sheet-p's effective metric doubly dressed by the
> iterated Schur complements.  This makes the inter-
> sheet coupling mechanism completely explicit: every
> sheet after the first has its effective metric
> dressed by the cross-shears to all earlier sheets.
>
> **(F32) Universal charge formula recovered from three
> tube-couples conventions.**  Applying F14's tube-
> couples convention to each of the three sheets
> independently, with MaSt's empirical sign vector
> (σ_e, σ_ν, σ_p) = (−1, 0, +1), yields the observable
> 4D electric charge
>
> $$
> Q \;=\; e\,(-n_1 + n_5).
> $$
>
> This is F15 of MaSt, now derived from the three-
> sheet kinematics rather than postulated.  The sign
> vector itself remains an empirical input.  The six-
> term generalized Lorentz force has three physical
> EM-coupled components (tubes) and three dark
> (rings + neutrino tube) under (σ_e, σ_ν, σ_p) =
> (−1, 0, +1).
>
> **(F33) Consistency with prior tracks.**  Track 2
> (single torus), Track 8 (two tori), and Track 9
> (scale-invariance) are all strict sub-cases of Track
> 10, recovered respectively by setting two sheets
> silent (F33 → Track 2), setting one sheet silent
> (F33 → Track 8), and extracting the dimensionless
> form (F33 → Track 9 on all three sheets).  No new
> physical postulate is introduced in Track 10 beyond
> Tracks 1–9; the derivation is pure metric algebra
> at one more block-iteration level.  GRID-native
> throughout.

**What this caps.**  F30–F33 close the *three-sheet
kinematic* arc of Program 1.  Mass (F30), charge
(F32), and Lorentz force (G.2.1) are all derived for
MaSt's actual T⁶ geometry, with an explicit closed-
form inverse-metric structure (F31) and consistency
with all prior tracks (F33).

Together with Tracks 1–9, Track 10 establishes that
the complete mass, charge, and interaction kinematics
of MaSt's three-sheet model follow from a single
structural input — the 6×6 internal metric on T⁶ —
plus MaSt's empirical sign-vector (σ_e, σ_ν, σ_p).
The phenomenological fits (specific metric values,
particle-to-winding assignments, filter constraints)
live in the R-studies; the analytical framework they
sit on is Track 10.

What remains open at the close of Program 1:

1. **Spin.**  The Track 7 trilemma (derivations 7a/
   7b/7c) is unresolved; a discriminator between 7b
   (WvM ratio rule) and 7c (6D Dirac KK) is needed.
   This does not affect the Track 10 mass/charge
   kinematics.
2. **GRID dynamics for the compact geometry.**  The
   mechanism by which GRID's Planck-scale lattice
   phase dynamics produces the three emergent compact
   tori at the Compton scale is undetermined (see
   derivation 9, F29 part 5).  Track 10 assumes the
   geometry as given.
3. **Specific R-studies phenomenology.**  Quantitative
   fits to the particle spectrum (R50 filters, R54
   cross-shear values, R53 geometric ratios) live in
   those studies and instantiate (F30) numerically.
   Track 10's closed form is the analytical skeleton
   they fit to.

Program 1's kinematic backbone is now complete.  The
remaining open problems are flagged, bounded, and
have identified pathways forward.
