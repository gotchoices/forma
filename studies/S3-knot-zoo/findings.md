# Findings: Knot Zoo Study

Running log of experiments, results, and their implications.
Entries are chronological. Each entry references the script that
produced it and the propositions from `theory.md` that it bears on.

---

## F1. Torus Knot Survey

**Script:** `scripts/01_knot_survey.py`
**Bears on:** P1 (spin classification), P2 (charge), P3 (mass ratios)

Enumerated all coprime (p,q) torus knots with p,q ≤ 7 and computed
spin, fermion/boson classification, and mass ratios.

### Fermion/boson classification — clean result

Odd p (tube windings) → fermion (π-twist per traversal, needs 2
circuits to restore the E-field → half-integer spin).

Even p → boson (2π-twist, restores in 1 circuit → integer spin).

This is a purely topological result and is robust.

### Spin values — only q = 1 and q = 2 give known spins

The angular momentum about the torus axis (in the a << R limit) is:

    L_z = ℏ/q

This gives:
- **q = 1** → spin 1 (bosons if p even, fermions if p odd)
- **q = 2** → spin ½ (the electron — WvM's (1,2) knot)
- **q = 3** → spin 1/3 (non-physical for elementary particles)
- **q ≥ 3** → non-standard spins

Only q = 1 and q = 2 produce spins that match known particles.
This constrains the zoo — but the spin formula L_z = ℏ/q has only
been verified in the a ≪ R limit and may need revision for general
geometry.

| q | Spin | Statistics | Relevant knots |
|---|------|-----------|---------------|
| 1 | 1 | p odd → fermion, p even → boson | (1,1), (2,1), (3,1), ... |
| 2 | ½ | all fermion (p must be odd for coprime) | (1,2), (3,2), (5,2), ... |

Note: q = 1, p = 1 is the (1,1) knot — the simplest closed curve
on a torus, going once around each way. It is a fermion with spin 1,
which is unusual (fermions normally have half-integer spin). This
suggests the spin formula may need refinement, or (1,1) is exotic.

### Mass ratios — fixed torus doesn't work

On a single torus (fixed R, a), all knots with p > 1 or q > 2 have
longer path lengths than the (1,2) electron, meaning lower photon
energy and lower mass. All computed m/m_e ratios are < 1. This
cannot explain the muon (206.8× m_e) or tau (3477× m_e).

**Key realization:** In WvM, R = λ/(4π) is set by the particle's
own Compton wavelength. A heavier particle has a smaller Compton
wavelength and a smaller torus:

    R_{particle} = λ_{particle} / (4π) = h / (4π m c)

So R_μ = R_e/206.8 and R_τ = R_e/3477. Different particles live
on different-sized tori, not on the same one.

### Important distinction: orbit vs field extent

The a/R = 1/√(πα) ≈ 6.60 from study 2 describes the **field extent**
(how far the E-field reaches from the orbit), not the physical tube
of the torus. The photon orbits on a thin torus (a_orbit << R) and
the spin ½ comes from this tight orbit. The field extends much
further (to the rotation horizon), and this extended field determines
the charge.

For the spin calculation, the relevant parameter is the orbit, not
the field extent. So spin = ℏ/q holds even though a_field/R ≈ 6.6.

### Correction history: surface, volume, and radial structure

This understanding was corrected twice. The full analysis is in
`reference/WvM-summary.md` §4.

**v1 (initial):** Treated the photon path as living on one torus
surface (2D material space, a material sheet = S¹ × S¹).

**v2 (over-correction):** Noted that WvM Fig. 2 shows "a family of
nested toroidal surfaces" and energy flow filling a 3D volume.
Suggested the material space might need 3 dimensions (φ, θ, r).

**v3 (current):** After full re-read of the paper:

- WvM's primary model (Fig. 1b) IS a single path — a twisted strip
  closed into a double loop on the torus surface. This is the
  visualization that produces E-inward and B-vertical.
- WvM then note (§2) that "we are firmly in the diffractive limit,
  where it makes little sense to talk about a specific photon
  'path'." The nested surfaces in Fig. 2 are **streamlines of
  energy flow** — the Poynting vector pattern of a single photon
  whose field extends across the toroidal volume as a wave.
- The nested surfaces are not separate photons or separate orbits.
  Individual streamlines stay at constant tube radius r. Nothing
  propagates radially. r is a **transverse mode coordinate** (like
  the radial intensity profile of a waveguide mode).
- The material space (if one exists) is **2D** (φ, θ). The radial
  field profile is the transverse mode structure, not a third
  material dimension.
- Our scripts (`02_knot_charge.py`) modeled a single path on one
  surface — this matches WvM's primary visualization (Fig. 1b)
  and captures the correct topology and winding.

This does not invalidate the charge computation (F3) or the
algebraic relationships (F4).

### Open questions from F1

1. **Why only q = 1, 2?** Is there a physical selection rule that
   eliminates q ≥ 3, or could exotic particles with non-standard
   spin exist?

2. **What determines the mass?** If different particles have different
   torus sizes, what selects the torus size (and hence the mass)?
   The WvM model does not answer this — mass is an input.
   **However:** if the torus is reframed as a fixed material extra
   dimension (see F2 below), mass could come from photon energy
   rather than torus size. This is a hypothesis, not a demonstrated
   result — see F2 for discussion and caveats.

3. **Do higher-p knots on q = 2 correspond to heavier fermions?**
   (3,2) and (5,2) are spin-½ fermions. On a fixed torus they are
   lighter (longer path), but higher harmonics (n > 1) of the same
   knot could be heavier. Alternatively, different particle types
   might live in different material dimensions.

4. **Charge for different knots.** Does the charge derivation
   (q = e via a/R = 1/√(πα)) change for different (p,q)? Or is
   it universal? The field topology may differ for higher-p knots.
   Fractional charges (1/3, 2/3 for quarks) are a key test.

5. **Photon as trivial case.** The free photon is not a knot — it
   is the unconfined building block. A photon traversing ordinary
   (non-material) space is massless and has spin 1 without any
   toroidal topology. Modeling it as a knot of itself is circular.

---

## F3. Charge Variation Across Knots — Null Result

**Script:** `scripts/02_knot_charge.py`
**Bears on:** P2 (charge), F1 open question 4

### Method

Parameterized (p,q) torus knots on a thin torus (a ≪ R) and propagated
a circularly polarized E-field along each path using the Frenet frame.
Computed three independent charge measures:

- **M_sph** = ⟨E · r̂⟩ — spherical monopole moment
- **M_cyl** = ⟨E · ρ̂⟩ — cylindrical radial component
- **M_tube** = ⟨E · r̂_tube⟩ — outward from tube center (WvM mechanism)

All measures normalized to the (1,2) baseline (electron).

### Result

**In the Frenet frame model, only (1,2) produces charge. All other
knots produce exactly zero.**

| Knot  | Spin | Q_sph | Q_cyl | Q_tube |
|-------|------|-------|-------|--------|
| (1,2) | ½    | 1.000 | 1.000 | 1.000  |
| (3,2) | ½    | 0.000 | 0.000 | 0.000  |
| (5,2) | ½    | 0.000 | 0.000 | 0.000  |
| (7,2) | ½    | 0.000 | 0.000 | 0.000  |
| (9,2) | ½    | 0.000 | 0.000 | 0.000  |

Tested across a/R = 0.001, 0.01, 0.1, 0.3, 0.5 — result is
identical in every case. This is not a numerical artifact.

### Why this happens — symmetry cancellation

For a (p,2) knot, the path winds p times around the tube per 2
circuits of the major axis. The E-field, transverse to the path,
rotates with tube angle θ = p·t.

For p = 1, the E-field orientation correlates with the azimuthal
position in just the right way to produce a net outward monopole
component — this is the WvM electron.

For p > 1, the E-field completes multiple oscillations around the
tube cross-section per trip around the major axis. Outward and inward
contributions cancel exactly, leaving zero monopole moment. This is
the same reason ∫cos(nθ)dθ = 0 for n ≥ 1 over a full period.

Within this model, the cancellation depends only on the winding
numbers, not on the torus geometry (a/R). No tuning of the torus
shape can produce fractional charge from higher-winding knots.

**Caveat:** This computation assumes Frenet frame transport for the
polarization vector. A different transport rule (e.g., parallel
transport on the torus surface, or a Berry phase correction) might
give different results. This has not been tested.

### Implications

1. **In this model, fractional charges do not emerge from different
   torus knots.** The 1/3 and 2/3 charges of quarks cannot be
   explained by assigning quarks to (3,2) or (5,2) knots on the
   same torus — at least not with Frenet frame polarization transport.

2. **Within this model, the (1,2) knot is unique** — the only torus
   knot that produces a net monopole E-field. If this result
   survives under more general transport rules, it would explain
   why there is exactly one fundamental charged lepton topology.

3. **If this result holds generally, quarks need a different
   mechanism.** Possible directions:
   - **Multi-photon states:** Three confined photons with correlated
     phases could each contribute 1/3 of the charge, yielding
     fractional apparent charge. This naturally connects to three
     color charges.
   - **Different material dimensions:** Quarks might live in a
     different extra dimension with different topology, where the
     charge integral produces 1/3 or 2/3 instead of 1.
   - **Non-toroidal topology:** Quarks might not be torus knots at
     all. Other compact manifolds (lens spaces, Seifert fibrations)
     could yield different charge quantizations.

4. **Neutrino interpretation.** The (3,2), (5,2), ... knots have
   spin ½ and zero charge — precisely the neutrino's quantum numbers.
   This is suggestive but not conclusive, since the mass mechanism
   is unresolved.

---

## F4. Charge from Geometry: Same Knot, Different Torus

**Script:** `scripts/03_charge_geometry.py`
**Bears on:** P2 (charge), F3 (null result for winding-based charge)

### Setup

F3 showed that varying the knot winding produces zero charge for
everything except (1,2). But from the S2-toroid-geometry study (F6), the
charge is a continuous function of the torus aspect ratio:

    q = e / ((a/R) · √(πα))

This means different a/R values produce different charges. Inverting:

    a/R = 1 / (q_frac · √(πα))

### Required a/R for each charge quantum

| Particle    | Charge | a/R           | Numerical | Multiple of electron |
|-------------|--------|---------------|-----------|---------------------|
| Electron    | e      | 1/√(πα)       | 6.60      | 1.0×                |
| Up quark    | 2e/3   | (3/2)/√(πα)   | 9.91      | 1.5×                |
| Down quark  | e/3    | 3/√(πα)       | 19.81     | 3.0×                |
| Neutrino    | 0      | ∞             | —         | —                   |

The ratios are clean: a/R scales as 1/q_frac, giving 1 : 3/2 : 3
for electron : up : down.

**Note:** This is algebra — inverting the WvM charge formula for
each target charge. It shows what geometry *would be required* if
the WvM mechanism applies to quarks. It does not demonstrate that
quarks are (1,2) knots or that material dimensions with these aspect
ratios exist.

### Model A: shared material dimension

If all particles live on one material dimension (tube radius a fixed,
R varies with particle mass via R = ℏ/(2mc)):

    m_u/m_e = (a/R_u)/(a/R_e) = 3/2 → m_u = 0.77 MeV

Experimental m_u ≈ 2.2 MeV — off by a factor of ~3. Absolute masses
do not match.

However, the *ratio* within the quark sector:

    m_d/m_u = (a/R_d)/(a/R_u) = (3)/(3/2) = 2.000
    Experimental m_d/m_u = 2.162

Agreement to 7.5%. The model predicts a clean 2:1 mass ratio for
first-generation quarks.

### Model B: two material dimensions (leptons vs quarks)

Separate the electron and quarks into different material dimensions.
The quark dimension has its own tube radius a_q. Only the quark mass
ratio is predicted:

    m_d/m_u = 2.000  vs  experimental 2.162  (7.5% off)

### Cross-generation test (Model A only)

Model A links mass and charge through geometry: with fixed a, the
orbital radius R determines both the charge (via a/R) and the mass
(via R = ℏ/(2mc)). This predicts that the mass ratio between
charge-partners should always be 2:

| Generation | m_{-1/3} / m_{+2/3} | Predicted |
|------------|---------------------|-----------|
| 1st        | m_d/m_u = 2.16      | 2.000     |
| 2nd        | m_s/m_c = 0.074     | 2.000     |
| 3rd        | m_b/m_t = 0.024     | 2.000     |

This fails for generations 2 and 3. But the test is likely
**asking the wrong question.** If the material dimension picture
(F2) is correct, mass comes from photon energy (independent of
geometry), and charge comes from a/R (fixed per dimension). In
that case:

- Charge and mass are decoupled
- Generations are energy levels (harmonics), not different geometries
- The cross-generation test is irrelevant — it tests Model A,
  which conflates two independent quantities

The 1st-generation m_d/m_u ≈ 2 agreement is likely coincidental.

### What this finding means

1. **The WvM charge formula admits fractional charges** via different
   torus aspect ratios. The required a/R values are algebraically
   clean multiples of 1/√(πα). This is a mathematical property of
   the formula, not a physical demonstration.

2. **Hypothesis: same topology, different geometry.** Electron, up
   quark, and down quark *could* all be (1,2) knots on material
   dimensions with different aspect ratios. This is consistent with
   the algebra but untested as physics.

3. **Hypothesis: three material dimensions.** The three distinct a/R
   values (6.60, 9.91, 19.81) are consistent with three material
   dimensions — one for each charge quantum. This is speculative.

4. **Neutrino remains unresolved.** q = 0 requires a/R → ∞, which
   is unphysical. Whether the neutrino fits this framework at all
   is unclear.

---

## F2. Compact Dimension Reframing (Hypothesis)

**No script** — conceptual analysis, not a computed result
**Bears on:** P3 (mass ratios), theory.md §4

**Status: This entire section is a hypothesis.** It has not been
tested computationally or derived from first principles. It is
included because it reframes the confinement problem and suggests
a testable mass spectrum, but none of its predictions have been
verified.

### The confinement problem dissolves (if this interpretation holds)

WvM's biggest weakness is the unknown confinement mechanism: what
forces a photon into a toroidal orbit? This problem disappears under
a different interpretation:

**Interpretation A (WvM original):** The photon orbits in our 3D space.
Something confines it. No known force can do this.

**Interpretation B (material dimension):** The torus IS an extra
dimension of spacetime — material, fixed in size, orthogonal to (x,y,z).
The photon follows a geodesic (straight line) in this space. No force
is needed: a straight line on a material space is already closed.

This resembles the Kaluza-Klein idea (1919–1926): charge emerges from
momentum in a compactified dimension. Whether WvM's charge derivation
is literally a KK mechanism has not been verified — the mathematical
correspondence needs to be checked explicitly.

### Mass from photon energy, not torus size

Under interpretation B, the torus dimensions (R, a) are properties of
spacetime — fixed, shared by all particles. The photon's energy is a
separate parameter that determines the particle mass:

    m = E/c² = h/(λc)

In this picture, the knot topology (p,q) would determine quantum
numbers (spin, charge), and the photon energy would determine mass.
These would be independent — but this decoupling is assumed, not
derived.

Quantization: the photon wavelength must fit the closed path
(constructive interference). On a path of length L, allowed
wavelengths are λ = L/n, giving:

    m_n = nh/(Lc)    for n = 1, 2, 3, ...

The fundamental (n=1) is the lightest particle for that knot type.
Higher harmonics (n > 1) are heavier particles with the same quantum
numbers.

### Two sub-models

**Shared dimension:** All particles live on one fixed torus. Different
knots give different quantum numbers. Harmonics give the mass spectrum.
Testable prediction: lepton mass ratios should be integers
(m_μ/m_e ≈ 207, m_τ/m_e ≈ 3477). If not exact integers, the model
needs refinement.

**Per-particle dimensions:** Electron and quarks each have their own
material dimension (a small number: perhaps 1 for leptons, 1 for
quarks). This is cleaner if mass ratios don't fit integer harmonics,
and it's still economical — 2 or 3 extra dimensions vs string theory's
6–7.

### Implications for this study

This reframing is significant enough to warrant its own study. The
S3-knot-zoo study can continue with topological classification (spin,
charge, fermion/boson) without committing to either mass model. The
mass spectrum question — harmonics on a fixed torus vs separate
dimensions — should be explored in a dedicated "material dimension"
study.

### Why this would matter (if correct)

If the material dimension picture works:
- No confinement problem (geodesic on material space)
- Mass from photon energy (not a free parameter per particle)
- Spin from topology (demonstrated for (1,2) in WvM)
- Charge from field geometry (demonstrated algebraically in study 2)
- Small number of extra dimensions (1–3, not 6–7)

These are attractive properties, but none have been derived from a
material-dimension formulation. The hypothesis needs to be tested
against Kaluza-Klein theory explicitly before drawing conclusions.

---

## Conclusion

The knot zoo study asked: **what torus knots model known particles?**

### What was demonstrated

- **P1 (spin):** Odd p → fermion, even p → boson (topological,
  robust). Only q = 1, 2 give known spin values — but the spin
  formula L_z = ℏ/q is only verified in the a ≪ R limit.
- **P2 (charge):** In the Frenet frame model, varying the knot
  winding does NOT produce different charges — only (1,2) gives
  nonzero charge (F3). This is a clear computational result, though
  it assumes a specific polarization transport rule.
- **P3 (mass):** On a fixed torus, different knots give lighter
  particles (longer paths), not heavier. Mass ratios of known
  particles cannot be reproduced by different knots on one torus (F1).

### What was shown algebraically (but not physically demonstrated)

- The WvM charge formula maps specific a/R values to specific
  charge fractions: 6.60 → e, 9.91 → 2e/3, 19.81 → e/3 (F4).
  These are clean algebraic relationships.

### What was hypothesized (untested)

- The material dimension reframing (F2): the torus as an extra
  dimension of spacetime, mass from photon energy, generations as
  harmonics. Attractive but unverified.
- Three material dimensions for three charge quanta (F4). Consistent
  with the algebra but speculative.
- Neutrino as a (3,2) knot (F3). Quantum numbers match but this
  is suggestive, not conclusive.

### What remains open

The study raises questions that go beyond torus knot classification:

- What is the nature of the material dimension(s)? Is the space
  toroidal in the geometric sense, or only topologically so?
- How does the photon's E/B field manifest in xyz from flat
  motion in material space?
- Is the material space 2D (surface path) or 3D (volume)?
- Can orthogonality between xyz and material dimensions be
  formalized with a transform?
- What determines the number and sizes of material dimensions?

These are foundational questions about the framework itself, not
about knot classification. They warrant a dedicated study.
