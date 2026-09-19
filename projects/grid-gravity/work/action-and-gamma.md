# The lattice action, the source, and the light-bending parameter γ

**Status:** Derivation + exact-spectrum and time-domain checks. **Step 3 of the
mechanism 3 validation plan ([STATUS.md](STATUS.md)): passed at first order,
with one added posit and two flags carried forward.**

- The source of the carrier is *derived*, not posited: it is proportional to
  energy, has one sign, and makes every mass attract.
- Full light bending (γ = 1) is obtained when the carrier loads **nodes and
  extended edges equally** — which is the *impedance-matched* (reflectionless)
  loading — and the compact circulation sees only one of the two.
- Flags: a purely standing wave is a *breathing* source (§6); and the
  second-order parameter β depends on a nonlinear completion not yet chosen (§7).

Script: [`../scripts/gamma_test.py`](../scripts/gamma_test.py).

Grades: **[rigorous]**, **[simulated]**, **[argument]**, **[posit]**, **[open]**.

---

## 1. Two ways to slow a wave [rigorous]

A wave on a transmission line travels at 1/√(L·C): it can be slowed by adding
shunt capacitance C *or* series inductance L. The two are not equivalent. Their
ratio sets the wave impedance √(L/C), and a wave reflects wherever the
impedance changes. In field language C ↔ ε and L ↔ μ; the speed is c₀/√(εμ)
and the impedance is √(μ/ε).

Step 1's node storage register is the shunt-capacitance kind: it raises ε. It
slows every direction alike, because a node is shared by all its edges.
Series loading lives *on an edge*, so it can be applied to some directions and
not others. Its lattice form: split each edge into two half-links with a
two-port series junction between them, and give the junction a storage
register of weight Z. With Z = 0 the junction is transparent.

**The dual sign rule.** Exact spectra show:

| storage | share returns same sign | share returns inverted |
|---|---|---|
| at a **node** (shunt) | slows: raises ε | opens a gap — a photon mass |
| on an **edge** (series) | opens a gap — a photon mass | slows that axis: raises μ |

So each location has exactly one lossless, gapless way to store, and they are
mirror images.

**The spectrum.** On an (x, c) lattice — x extended, c compact — with node
storage Y everywhere and edge storage Z on the x-edges only, at low frequency

<!-- ω² = c₀² ( k_x²/μ_x + k_c² ) / ε,   ε = 1 + Y/8,  μ_x = 1 + Z/4 -->
$$
\omega^2 \;=\; \frac{c_0^2}{\varepsilon}\Bigl(\frac{k_x^2}{\mu_x} + k_c^2\Bigr),
\qquad \varepsilon = 1+\tfrac{Y}{8},\quad \mu_x = 1+\tfrac{Z}{4}
$$

(c₀² = 1/8 per tick² on the half-link lattice). Checked against exact
eigenvalues to five figures for six loadings, including the inertia coefficient
of a massive mode, which follows the *extended* speed c₀²/(εμ_x).

## 2. The light-bending parameter [rigorous]

Two observables matter. The **rest-clock rate** is the rest frequency of a
massive mode, ω₀ = c₀k_c/√ε: it sees only ε. The **coordinate speed of light**
along space is c_x = c₀/√(εμ_x): it sees both. In the standard weak-field
parametrization, with Newtonian potential Φ, the clock rate is (1 + Φ/c²) and
the light speed c(1 + (1+γ)Φ/c²), where γ = 1 is general relativity and the
observed value (to about 10⁻⁵). Therefore

<!-- γ = δln c_x / δln ω₀ − 1 = δμ_x / δε -->
$$
\gamma \;=\; \frac{\delta\ln c_x}{\delta\ln\omega_0} - 1 \;=\; \frac{\delta\mu_x}{\delta\varepsilon} .
$$

| loading | γ (exact spectrum) |
|---|---|
| node storage only (step 1's rule) | 0.0000 — half the observed bending |
| edge storage only | undefined: clocks are unaffected, so bodies at rest do not fall (light is still delayed) |
| **node and extended-edge storage, equal** | **1.0000** |

**γ = 1 ⇔ δμ_x = δε ⇔ the wave impedance √(μ_x/ε) is unchanged.** The full
light bending is obtained exactly when the carrier loads the lattice *without
disturbing its impedance match*. GRID's scatter is, by construction, the
matched-impedance scatter ([grid-duality](../../grid-duality/)); the statement
here is that the carrier preserves that property. Call the common factor K:
ε = μ_x = K.

A plainer way to see the factor of two: a hop through space passes through one
node *and* one edge, and is delayed by both; a clock — a wave circulating in
the compact dimension — sits at the node and is delayed by one. If every
lattice member stores in proportion to the same carrier value, light is slowed
twice as much (in the logarithm) as clocks. That is γ = 1.

## 3. Checks in the time domain [simulated]

**Reflection at an abrupt step** (same 18% speed change in each case; photon
wavelength 20.9 nodes):

| loading beyond the step | reflected fraction |
|---|---|
| node only | 1.07 × 10⁻² |
| edge only | 1.07 × 10⁻² |
| matched | 3.0 × 10⁻⁴ — and 7.2 × 10⁻⁵ at twice the wavelength |

Even an *abrupt* matched step is nearly transparent; the residue scales as
(lattice spacing / wavelength)², because the two storages sit half a link
apart. A matched carrier does not scatter the waves it slows.

**A matched gradient**, K(x) = 1.2 + 2×10⁻⁵·(x − x₀):

| quantity | simulation | ray equations (exact spectrum) |
|---|---|---|
| photon delay after 4897 ticks | −17.031 nodes | −17.030 |
| rest packet acceleration | 7.110 × 10⁻⁷ | 7.241 × 10⁻⁷ × 0.982 = 7.11 × 10⁻⁷ |
| γ from the local slopes | 0.9997 | 1 |

The factor 0.982 is the packet's momentum spread acting through the speed
dependence of the acceleration, which for this loading is a ∝ (1 − 3v²/c²) —
the general-relativistic factor for radial motion in coordinates of this kind.
(Step 2's node-only rule gave (1 − 2v²/c²); in general it is 1 − (2+γ)v²/c².)

To first order the test-particle Hamiltonian, ω² = c₀²(k_x²/K² + k_c²/K), is
identical to that of the weak-field Schwarzschild metric in isotropic
coordinates. Everything a test body or light ray does at first order follows.

## 4. The action, and what sources the carrier [rigorous]

Let the carrier χ set the loading, K = K(χ), and write one Lagrangian density
for the wave ψ and the carrier (continuum limit; c₀ = 1):

<!-- L = ½K ψ̇² − ½(∂ₓψ)²/K − ½(∂_cψ)²  +  (κ/2)[ χ̇² − (∇χ)² ]  (carrier term to lowest order) -->
$$
\mathcal{L} \;=\; \tfrac12 K\,\dot\psi^2 - \tfrac{1}{2K}(\partial_x\psi)^2 - \tfrac12(\partial_c\psi)^2
\;+\; \tfrac{\kappa}{2}\bigl[\dot\chi^2 - (\nabla\chi)^2\bigr] ,
$$

κ being the carrier's stiffness. Varying χ gives the carrier's equation, and
its source is whatever in the wave's Lagrangian depends on χ:

<!-- κ(χ̈ − ∇²χ) = (K′/2)[ ψ̇² + (∂ₓψ)²/K² ] -->
$$
\kappa\,(\ddot\chi - \nabla^2\chi) \;=\; \frac{K'}{2}\Bigl[\dot\psi^2 + \frac{(\partial_x\psi)^2}{K^2}\Bigr] .
$$

Nothing here was chosen. **The rate depends on the carrier, so the wave pushes
back on the carrier** — that is action and reaction — and the push is a sum of
squares:

- **Proportional to energy.** For a mode at rest the time-averaged source is
  (K′/K)·u/2, with u the energy density. *This replaces posit P3 of the
  mechanism note with a derived result.*
- **One sign, and always attractive.** The carrier's response has the sign of
  K′, and the change in loading is K′ times that response — proportional to
  K′², positive whatever the convention. The loading always *rises* near
  energy; everything always falls toward everything.
- **Light gravitates twice as much as matter, per unit energy.** For a wave
  travelling along x the two terms are equal and the source is (K′/K)·u; for a
  body moving at speed v it is (K′/K)·(u/2)(1 + v²/c²). General relativity says
  the same (the active gravitational mass of radiation is twice its energy).
  The passive factor of two (light bending) and the active one come from the
  same place, as an action guarantees.
- **Energy and momentum are conserved** and Newton's third law holds between
  two masses, carrier momentum included — Noether's theorem, since the action
  has no explicit dependence on position or time.
- **Newton's constant** is fixed by the carrier's stiffness: with K′ = K = 1 at
  χ = 0, a mass M holds χ = M/(8πκr), the potential is Φ = −χ/2, and
  G = 1/(16πκ). As with ζ in [grid/gravity.md](../../../grid/gravity.md), this
  is a calibration, not a prediction.
- **A falling body pays for its fall** with rest energy: ω₀ ∝ 1/√K is lower in
  the well.

## 5. What had to be added [posit]

Two additions to the ledger of
[sync-carrier-mechanism.md](sync-carrier-mechanism.md) §2:

- **P6 — every member stores.** Extended edges carry a (series) storage
  register as nodes carry a (shunt) one, and the carrier loads both equally.
  The equality is not a free parameter: it is the unique reflectionless
  loading, and it is what "every lattice member stores in proportion to the
  carrier" would mean.
- **P7 — the compact circulation is loaded once.** A clock's compact loop
  closes through a node and is not loaded by the storage on space edges. In the
  (x, c) testbed the compact dimension is drawn as a ring of ordinary edges, so
  this is a genuine posit there. The reading that makes it natural: the carrier
  is a field over *space*; it loads the members that make up space; the compact
  dimension is not made of space edges. (If the compact loop instead lived
  inside an edge and saw only the edge storage, the result would be the same by
  symmetry. If compact edges are loaded like space edges, γ returns to 0.)

**A consequence for the candidate in the mechanism note's §8.** A stretch of
the compact circumference R_ℵ, acting alone, slows clocks but not light: no
light bending at all. It cannot be the carrier's whole effect. And the sourcing
it was introduced to explain (radiation pressure ∝ energy) is now supplied by
the action without it.

## 6. Flag: a purely standing wave is a breathing source [open]

For a mode at rest the source is (K′/2)ψ̇² — the *kinetic* half of the energy.
In a standing wave, energy passes back and forth between kinetic and gradient
form twice per cycle, so the source oscillates between zero and twice its mean
at frequency 2ω₀. A massless carrier would radiate from such a source:
P = G M²(2ω₀)²/(2c), which for a proton-mass standing wave empties it in about
2 million years. That is excluded.

What removes it, in order of plausibility:

1. **The particle is not a pure standing wave.** A wave that *travels* around
   one compact cycle has a constant ψ̇². [metric-charge](../../metric-charge/)'s
   charged particle "stands in the ring and travels in the tube": its source is
   static. Only the neutral, purely standing idealization of
   [metric-mass](../../metric-mass/) breathes.
2. **Whole quanta.** The radiated carrier quantum would carry 2Mc², more than
   the particle has. A one-quantum state cannot emit it; the classical
   breathing is a feature of treating one quantum as a classical amplitude.
3. A different loading pattern in which compact propagation is loaded too
   (source = total energy, constant) — but that needs extended edges loaded
   three times as much as nodes to keep γ = 1, and gives up the impedance match.

A classical lattice simulation with a real standing wave and a dynamical carrier
*will* show this radiation (relevant to step 5).

## 7. Flag: the second-order parameter β is not yet determined [open]

γ is a first-order quantity. The next one, β (measured by Mercury's perihelion
advance; general relativity and observation give β = 1 to about 10⁻⁴), depends
on how the carrier's own dynamics are loaded — a nonlinear question. Three
candidate completions, with the carrier's shift symmetry fixing K = e^χ:

| carrier dynamics | static solution | β |
|---|---|---|
| carrier Lagrangian = K × (the light-type Lagrangian): (κ/2)[K²χ̇² − (∇χ)²] | χ harmonic, K = e^(2GM/r) | **1** |
| carrier Lagrangian = the light-type one: (κ/2)[Kχ̇² − (∇χ)²/K] | 1/√K harmonic | ½ — excluded |
| carrier as a linear wave in the medium K (not from an action) | 1/K harmonic | 0 — excluded, and not conservative |

All three give the carrier exactly light's speed everywhere (so gravitational
and light signals are delayed alike by a mass). Only the first survives, and it
is a known model: it is the polarizable-vacuum Lagrangian the README already
names as mechanism 2's target, with the exponential metric (β = γ = 1). So a
viable completion exists; what is open is whether a lattice rule *produces* it.
That belongs with the nonlinear work of step 5.

## 8. Verdict against the plan

The plan's pass condition was "source ∝ energy with one sign; a stated, natural
spatial partner that gives γ = 1", and its fail condition "γ = 1 requires an
unnatural or tuned partner."

- Source: **derived** — stronger than asked.
- Partner: edge storage, loaded equally with node storage. **Not tuned** — the
  equality is the impedance-matching condition and the unique reflectionless
  choice — but it rests on **P7**, a new posit about where the compact loop
  closes.
- New liabilities, both with a known way out: §6 and §7.

## Grades summary

- **[rigorous]** Dual sign rule; the two-storage spectrum; γ = δμ_x/δε; the
  source from the action, its sign, the factor of two for light; G = 1/(16πκ);
  the three β outcomes.
- **[simulated]** Spectrum to five figures; γ = 0, 1 from exact eigenvalues;
  matched step reflecting 36× less than an unmatched one, vanishing as
  (spacing/wavelength)²; matched-gradient photon delay (ratio 1.0001) and
  rest-packet acceleration with the (1 − 3v²/c²) factor.
- **[posit]** P6, P7.
- **[open]** The breathing source for pure standing waves; β and the nonlinear
  completion; whether one carrier loads every sheet's compact loop alike.
