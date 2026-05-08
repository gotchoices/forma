# Bloch's Theorem and Band Structure — A Ground-Up Introduction

A self-contained introduction to Bloch's theorem and band structure: how a
linear update rule on a periodic lattice gives rise to plane-wave
eigenstates labelled by a wavevector **k**, and how the resulting
*dispersion relation* ω(**k**) and *band structure* organise everything
the lattice can do.

**Audience.** Anyone with college-level linear algebra and a working
familiarity with complex exponentials. No prior solid-state physics
is needed; the standard solid-state vocabulary (Brillouin zone,
crystal momentum, effective mass) is built up here from scratch.

**Why this primer exists.** Several projects in this repo —
[grid-duality](../projects/grid-duality/) most prominently — analyse
discrete update rules on periodic lattices, and the natural language
for that analysis is the Bloch / band-structure language of solid-state
physics. The aim of this primer is to make that language feel inevitable
rather than imported. Bloch's theorem is *not* an electromagnetic or
quantum-mechanical result; it is a representation-theoretic fact about
periodic lattices, and it applies to any linear translation-invariant
update on such a lattice.

---

## Concepts introduced in this primer

| § | Concept |
|---|---------|
| 1 | The setting: a periodic lattice with a translation-invariant linear update |
| 2 | Discrete translation symmetry |
| 3 | Eigenstates of translations are plane waves |
| 4 | Bloch's theorem |
| 5 | Worked example: a 1D ring |
| 6 | The Brillouin zone |
| 7 | More than one site per unit cell — the Bloch matrix |
| 8 | Bands and band structure |
| 9 | Group velocity and the speed of waves |
| 10 | Effective mass at a band extremum |
| 11 | What breaks without translation invariance |
| 12 | Application to lattice update rules |

---

## 1. The setting

Consider a regular array of sites — a *lattice*. Examples include a
1D ring of N sites, a 2D hexagonal grid, a 3D cubic or diamond
lattice. At each site there is some local state: one complex number,
a small vector of complex numbers, the registers on a node's
incident edges. The full state of the system is the collection of
all per-site states.

A *linear update rule* takes the current state to the next state by
some matrix multiplication: the update operator U acts on the full
state vector ψ to give Uψ. Linearity means ψ → Uψ respects
superposition: if ψ_1 and ψ_2 are two valid states, so is
α ψ_1 + β ψ_2, and U(α ψ_1 + β ψ_2) = α U ψ_1 + β U ψ_2.

For Bloch's theorem to apply, the update rule must satisfy two
conditions:

1. **Linearity.** U is a linear operator. Every site's next state
   is a linear combination of the current states (its own and its
   neighbours').
2. **Discrete translation invariance.** Shifting the entire state
   by one lattice vector and then applying U is the same as
   applying U first and then shifting. In plain language: the rule
   at every site is the *same* rule.

Both conditions are properties of U itself; nothing yet has been
said about energies, wavefunctions, or quantum mechanics.

---

## 2. Discrete translation symmetry

Suppose the lattice has lattice vectors **a**_1, **a**_2, ... — the
vectors that take a unit cell to its neighbours. (For a 1D ring of
spacing 1, there is just **a** = (1). For a 2D square lattice,
**a**_1 = (1, 0) and **a**_2 = (0, 1). For 2D hex, the two primitive
vectors point at 60° to each other.) A *lattice translation* T_R is
the operation "shift everything by **R**", where **R** = n_1 **a**_1
+ n_2 **a**_2 + ... is any integer combination of the lattice
vectors.

The set of all lattice translations forms a group (composition is
just adding the **R**'s; the inverse of T_R is T_{−R}). Translation
invariance of U means

<!-- T_R · U = U · T_R   for all R -->
$$
T_{\mathbf{R}} \cdot U \;=\; U \cdot T_{\mathbf{R}} \qquad \text{for every lattice vector } \mathbf{R}.
$$

When two operators commute, they share a common basis of
eigenvectors. So *if we can find the eigenvectors of the
translations T_R, we have a basis in which U is automatically
block-diagonal*. That is the route Bloch's theorem takes.

---

## 3. Eigenstates of translations are plane waves

What does it mean to be an eigenvector of a translation? Concretely,
on a 1D lattice, T (shift by one site) acts on a state ψ_j (the
amplitude at site j) by sending it to ψ_{j−1}. (After a unit
shift, the amplitude that was at site j−1 is now at site j.) An
eigenvector of T with eigenvalue λ satisfies

<!-- ψ_{j-1} = λ ψ_j  for all j -->
$$
\psi_{j-1} \;=\; \lambda\, \psi_j \qquad \text{for every } j.
$$

Iterating this n times gives ψ_{j−n} = λ^n ψ_j, so the amplitude at
site j is a geometric progression in j. Writing λ = e^{−ik} (any
non-zero λ on the unit circle can be written this way; we will see
shortly why |λ| = 1 is forced), the solution is

<!-- ψ_j = ψ_0 · exp(i k j) -->
$$
\psi_j \;=\; \psi_0 \, e^{\,i\, k\, j}.
$$

This is a *plane wave*: a uniform-amplitude oscillation along the
lattice with **wavevector k**. The wavevector k labels the
eigenvector; different k's give different eigenvectors, and
together they form a complete basis for any state on the lattice
(this is the discrete Fourier transform).

The same argument generalises to higher dimensions: the eigenvectors
of all the lattice translations T_R are the plane waves

<!-- ψ(r) = exp(i k · r) -->
$$
\psi(\mathbf{r}) \;=\; e^{\,i\,\mathbf{k} \cdot \mathbf{r}},
$$

with eigenvalue e^{−i**k**·**R**} under T_R.

**Why |λ| = 1.** On a finite ring of N sites, T^N is the identity
(shifting all the way around brings every site back to itself). So
λ^N = 1, which forces λ to be an N-th root of unity — i.e., a
complex number on the unit circle. The N allowed values of k are
k_m = 2π m/N for m = 0, 1, ..., N−1. On an infinite lattice the
analogous statement is that |λ| = 1 is the only choice that keeps
the plane wave bounded as j → ±∞.

---

## 4. Bloch's theorem

The discussion so far makes Bloch's theorem almost a tautology.
Recall:

- U commutes with every lattice translation T_R (translation
  invariance, §1).
- The simultaneous eigenvectors of all T_R are plane waves
  e^{i**k**·**r**} (§3).
- Commuting operators share an eigenbasis.

Therefore the eigenvectors of U can be chosen to be plane waves
labelled by **k**. With one site per unit cell that is the whole
story. With more than one site per unit cell, the plane wave gets
multiplied by a small **k**-dependent vector u(**k**) that lives on
one unit cell (one entry per site in the cell). The general
statement is:

> **Bloch's theorem.** Every eigenvector of a linear,
> translation-invariant update on a periodic lattice can be chosen
> to have the form
>
> ψ_α(**r**) = u_α(**k**) · e^{i**k**·**r**},
>
> where α labels the sites within one unit cell and u_α(**k**) is a
> per-cell vector that depends on **k** but is the *same* in every
> unit cell.

The small vector u_α(**k**) is sometimes called the *Bloch vector*
or *cell-periodic part* of the wavefunction. The full state has
**k**-dependent oscillation between cells (the e^{i**k**·**r**}
factor) and a fixed pattern within each cell (the u_α factor).

The label **k** is called the **crystal momentum** or
**Bloch wavevector**. Like ordinary momentum, it is conserved by
translation-invariant evolution; unlike ordinary momentum, it lives
in a finite domain (see §6 below) rather than the whole real line.

---

## 5. Worked example: a 1D ring

Consider a 1D ring of N sites, with one complex amplitude ψ_j at
each site. Define the update rule by

<!-- ψ_j(t+1) = ψ_{j-1}(t) -->
$$
\psi_j(t+1) \;=\; \psi_{j-1}(t).
$$

This is the simplest possible translation-invariant linear update:
"shift everything one site to the right." It is what a
non-dispersive wave does on a 1D lattice.

A plane wave ψ_j = e^{ikj} evolves under one update step into
e^{ik(j−1)} = e^{−ik} · e^{ikj}, so it is an eigenvector of U with
eigenvalue e^{−ik}. Writing the eigenvalue as e^{−iω(k)} (a useful
convention because eigenvalues will tile the unit circle), we read
off

<!-- ω(k) = k -->
$$
\omega(k) \;=\; k.
$$

This is the **dispersion relation** of the update: the function
that gives the eigenvalue's phase ω as a function of the wavevector
k. The shape of ω(k) is what controls how waves propagate, as the
next two sections develop.

The ring's periodicity quantises k. Going all the way around the
ring (N sites) must return the wave to itself, so e^{ikN} = 1, which
forces

<!-- k_m = 2π m / N,  m ∈ {0, 1, ..., N-1} -->
$$
k_m \;=\; \frac{2\pi m}{N}, \qquad m \in \{0, 1, \ldots, N-1\}.
$$

There are exactly N plane-wave eigenstates, one for each m. Together
they form a complete orthonormal basis for any state on the ring.
This is just the discrete Fourier transform: any state ψ_j can be
written as a sum Σ_m c_m e^{ik_m j}, and the update rule acts
diagonally — each c_m simply picks up a phase factor e^{−iω(k_m)}.

That diagonalisation is the punchline: a translation-invariant
update is *block-diagonal* in the **k**-basis, with each k-block
acting independently. Once you switch to the **k**-basis,
complicated lattice dynamics reduce to per-mode phase rotations.

---

## 6. The Brillouin zone

Plane waves with wavevector k and wavevector k + 2π give the same
state on a 1D unit-spaced lattice, because e^{i(k+2π)j} = e^{ikj}
for integer j. So the wavevector is only defined modulo 2π. The
*fundamental domain* of k — the smallest range that lists every
distinct plane wave exactly once — is conventionally taken as
k ∈ [−π, π) (or equivalently [0, 2π)).

This fundamental domain is called the **first Brillouin zone**.

In higher dimensions the same construction applies. The set of
**k** vectors modulo "translations in **k**-space" forms a finite
region — the first Brillouin zone — whose shape depends on the
lattice. For a 2D square lattice it is a square; for 2D hex it is a
regular hexagon; for 3D diamond it is a truncated octahedron. The
specific shapes show up in solid-state textbooks; the conceptual
content is just *fundamental domain of crystal momentum*.

The Brillouin zone matters because:

- Every distinct Bloch state is labelled by exactly one **k** in the
  first Brillouin zone.
- The dispersion relation ω(**k**) is naturally a function on the
  Brillouin zone (so it can be plotted on a finite domain, even
  for an infinite lattice).
- Special points in the Brillouin zone (centre, corners, edge
  midpoints) often coincide with band extrema and become the
  natural anchor points of the lattice's dynamics.

---

## 7. More than one site per unit cell — the Bloch matrix

If a unit cell contains more than one site, the plane-wave argument
of §3 is modified slightly. Within each cell, the update can mix
amplitudes among the cell's sites; between cells, translation
invariance still holds. Bloch's theorem then says every eigenstate
factors as

<!-- ψ_α(r) = u_α(k) · exp(i k · r) -->
$$
\psi_\alpha(\mathbf{r}) \;=\; u_\alpha(\mathbf{k}) \, e^{\,i\, \mathbf{k} \cdot \mathbf{r}},
$$

where α = 1, 2, ..., M ranges over the M sites in one unit cell,
and u_α(**k**) is a complex number for each α (an M-component
vector overall).

Plugging this ansatz into the update rule converts it into an
**M × M matrix equation** at each **k**:

<!-- H(k) u(k) = e^{-iω(k)} u(k) -->
$$
H(\mathbf{k}) \, u(\mathbf{k}) \;=\; e^{-i\,\omega(\mathbf{k})} \, u(\mathbf{k}).
$$

The matrix H(**k**) is variously called the **Bloch matrix** or
**Bloch Hamiltonian**. It is the **k**-by-**k** representation of the
update operator, with the "between-cell" oscillation already
factored out.

Because H(**k**) is M × M, it has M eigenvalues at each **k**, and
therefore M dispersion branches — *bands* — labelled
ω_1(**k**), ω_2(**k**), ..., ω_M(**k**). The collection of all M
bands across the Brillouin zone is the **band structure** of the
lattice.

**Examples.**

- *1D ring with one site per cell.* M = 1; the Bloch matrix is
  1 × 1; one band.
- *2D hexagonal lattice with two sublattices A and B.* The hex
  lattice's natural unit cell contains one A-site and one B-site;
  M = 2; the Bloch matrix is 2 × 2; two bands.
- *3D diamond with two-atom basis.* M = 2 (in the simplest
  formulation); the Bloch matrix is 2 × 2; two bands. (A larger
  unit cell that includes more sublattices gives an
  appropriately larger Bloch matrix; the band count grows with
  the cell size, but the physics is unchanged.)

Diagonalising the M × M Bloch matrix at each **k** is mechanical
linear algebra. The non-trivial work is in writing down the
matrix; once it is in hand, the bands ω_n(**k**) are just its
eigenvalues.

---

## 8. Bands and band structure

A **band** is a single dispersion branch ω_n(**k**) — one
eigenvalue of the Bloch matrix as a function of **k**, plotted
across the Brillouin zone.

Bands have a few generic features worth naming:

- **Continuity.** ω_n(**k**) is continuous in **k** (assuming the
  Bloch matrix is continuous in **k**, which it always is for
  finite-range update rules).
- **Periodicity.** ω_n(**k**) has the periodicity of the reciprocal
  lattice — it agrees on opposite faces of the Brillouin zone.
- **Extrema.** ω_n(**k**) typically has interior extrema (maxima
  and minima) within the Brillouin zone, at high-symmetry points.
  These extrema are the anchor points for several physically
  important constructions, especially effective mass (§10).
- **Gaps.** Two bands ω_n(**k**) and ω_{n+1}(**k**) may be
  separated by an energy gap throughout the Brillouin zone, or
  they may touch at isolated points. Whether they touch is a
  topological property of the Bloch matrix.

The band structure encodes everything the lattice does dynamically,
in the sense that any state's evolution is a sum of independent
per-mode rotations and the rotation rate of each mode is exactly
ω_n(**k**) for that mode's band and **k**.

---

## 9. Group velocity and the speed of waves

A *wavepacket* — a localised superposition of plane waves with
wavevectors near some central **k**_0 — propagates with a velocity
called the **group velocity**:

<!-- v_g = ∇_k ω(k) -->
$$
\mathbf{v}_g \;=\; \nabla_\mathbf{k}\, \omega(\mathbf{k}).
$$

In 1D this is just dω/dk. The group velocity is the *physical*
propagation speed of the wavepacket's energy and information. It
need not equal the *phase velocity* ω/k (the speed at which a
single plane wave's crests move), and on a dispersive medium it
often does not.

A few consequences:

- **Linear dispersion.** If ω(k) = c·k (linear in k), then v_g = c
  for every **k** — the medium is non-dispersive, and all
  wavepackets propagate at the same speed c. This is what light
  in vacuum and waves on a coord-2 chain (the simplest 1D ring)
  both do.
- **Curved dispersion.** If ω(k) is non-linear, v_g varies with
  **k**, and different parts of a wavepacket move at different
  speeds — the wavepacket spreads (disperses) over time. This is
  the generic situation on a higher-coordination lattice.
- **v_g = 0 at band extrema.** At a maximum or minimum of ω(**k**),
  the gradient ∇_**k**ω vanishes. A wavepacket centred at such an
  extremum does not move. This is the key fact for the next
  section.

---

## 10. Effective mass at a band extremum

Near an extremum **k**_0 (a point where v_g = 0), expand ω(**k**) to
second order:

<!-- ω(k) ≈ ω(k_0) + (1/2) (k − k_0)_i (∂²ω/∂k_i ∂k_j)|_{k_0} (k − k_0)_j -->
$$
\omega(\mathbf{k}) \;\approx\; \omega(\mathbf{k}_0) + \tfrac{1}{2}\,
(k - k_0)_i \, \frac{\partial^2 \omega}{\partial k_i\, \partial k_j}\bigg|_{\mathbf{k}_0}
(k - k_0)_j.
$$

This is *exactly* the dispersion relation of a non-relativistic free
particle of mass m_eff, where the effective mass is set by the band
curvature:

<!-- m_eff (with ℏ = 1, isotropic case) = 1 / (d²ω/dk²)|_{k = k_0} -->
$$
m_{\text{eff}} \;=\; \frac{\hbar^2}{(d^2\omega/dk^2)\big|_{\mathbf{k}_0}}
\qquad \text{(isotropic case).}
$$

Anisotropic extrema have a *tensor* effective mass set by the full
matrix of second derivatives, and the wavepacket's response to a
small perturbation in different directions is governed by that
tensor.

The interpretation is that **a wavepacket parked at a band
extremum behaves like a free particle of mass m_eff**. It is
spatially localised (since its envelope does not propagate, it can
be made stationary), and a perturbation that changes its central
**k** slightly accelerates it the way a force accelerates a
non-relativistic massive particle. This is the **effective-mass
theorem**, the cornerstone of solid-state band theory's connection
to particle-like behaviour on a lattice.

The crucial structural point is that **band curvature exists only
when there is a band extremum to evaluate it at**, and band
extrema appear only on lattices whose Bloch matrix is non-trivial
— that is, lattices with M ≥ 2 sites per unit cell, or
equivalently, coordination number ≥ 3 in the simplest 1D
embedding. A coord-2 1D chain has linear dispersion ω = k, no
extremum, and therefore no effective-mass eigenstates.

---

## 11. What breaks without translation invariance

Bloch's theorem requires the linear update to commute with every
lattice translation. If translation invariance fails — because the
lattice has a boundary, or some sites have a different rule, or
the rule depends on position — the entire construction unravels:

- **Plane waves are no longer eigenstates.** A plane wave hitting a
  boundary scatters into a different state, so e^{i**k**·**r**}
  is not preserved by the update.
- **Crystal momentum is no longer conserved.** Different plane
  waves mix under the update, so a wavepacket initialised at
  wavevector **k** evolves into a superposition of many
  wavevectors.
- **The natural eigenbasis is sin/cos standing waves.** On a
  finite open chain (no periodic identification), the eigenstates
  of a near-translation-invariant rule with hard walls are sines
  and cosines satisfying the boundary conditions. These can still
  be enumerated and the update can still be diagonalised, but the
  resulting basis lacks the conserved **k**-label that makes the
  Bloch picture so useful.
- **Group velocity is not directly defined.** Without a clean
  ω(**k**) curve there is no derivative to take. A wavepacket's
  effective propagation speed can still be measured, but it is no
  longer a simple function of **k**.

This is why projects that want to apply the standard wave / band /
mass language must first establish that the substrate is periodic.
Without periodicity, the language doesn't apply — not because of
any deep physical principle, but because Bloch's theorem doesn't
apply.

---

## 12. Application to lattice update rules

The preceding sections developed Bloch's theorem and band structure
without committing to any specific physical setting. Whenever a
project has:

1. a periodic lattice (any dimension, any unit cell),
2. a linear update rule (matrix multiplication on the state vector),
3. translation invariance (the rule is the same at every cell),

— the Bloch / band-structure machinery applies *as a theorem*. The
resulting bands ω_n(**k**), group velocities v_g = ∇_**k** ω, and
effective masses m_eff at extrema are all features of the
lattice's *update rule*, not of any externally postulated physics.

The grid-duality project's [Scattering update](../projects/grid-duality/06-3d-extension-and-lattice-closures.md)
satisfies all three conditions: the per-vertex S-matrix
S = (2/N)·J − I and the per-edge swap of the exhale phase are
both linear, are applied identically at every site of given
coordination, and live on a lattice that becomes periodic once the
substrate has wrapped (chapter 7 §2). Bloch decomposition therefore
produces a band structure for the Scattering update on each closed
substrate (ring, plaquette, 2-torus, 3-torus). Light, mass, and
charge in that project are interpretations of features of these
band structures and the topology of the substrates that host them.

The key takeaway for any reader following such a project is that
Bloch's theorem and its band structure are *generic* mathematical
machinery for periodic linear systems — not a physics import. The
theorem is what permits the language; the *interpretation* of the
bands as light, the band curvature as mass, and the integer
windings as charge is a separate set of physical claims that each
project carries on its own.

---

## Further reading

- [metric.md](metric.md) — the metric tensor primer, prerequisite for
  the continuum-side companions to this primer.
- [kaluza-klein.md](kaluza-klein.md) — Kaluza-Klein theory, which
  takes the integer-quantised modes on a compact extra dimension
  and identifies them with charge. The lattice analogue of KK's
  compact-direction momentum quantisation is the integer
  wavevector quantisation k = 2π m / N developed here.
- [maxwell-primer.md](maxwell-primer.md) — Maxwell's equations,
  whose dispersion relation ω = c|**k**| is the simplest possible
  band structure (linear, dispersionless, single band).

For deeper solid-state references outside this repo, the standard
introduction is Ashcroft & Mermin, *Solid State Physics*, chapters
8 ("Electron Levels in a Periodic Potential") and 9 ("Electrons in
a Weak Periodic Potential"); a more modern and topology-aware
treatment is Bernevig & Hughes, *Topological Insulators and
Topological Superconductors*, chapters 1–3.
