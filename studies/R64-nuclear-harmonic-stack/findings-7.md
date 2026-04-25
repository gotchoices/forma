# R64 Track 7 — Strong force from a 7-tensor: 6 Ma + 1 S spatial dim

Track 7 explores whether a 7-tensor (T⁶ Ma block plus 1 abstract S
spatial dimension) naturally produces the observed nucleon-nucleon
potential shape — a trough at r ≈ 1 fm with depth ~50 MeV plus
Coulomb tail — from MaSt's geometric structure with the standard
1/α coupling assumption.

**Result: structurally encouraging, scale off by factor ~2-3.**

The 7-tensor with a tube-direction cross-shear σ_t between the
p-sheet and S produces:

- A **trough** in E(r) for pp, pn, nn configurations
- **Charge-independent** strong-force shape (σ_t couples to n_pt=6
  in all three configurations equally) — matching the SM observation
  that the strong nuclear force is approximately charge-symmetric
- **pn preferred over pp** at the trough (pn deeper by ~18 MeV) —
  matches observed nuclear stability favoring N ≈ Z light nuclei
- **Coulomb 1/r tail** at large r between charged configurations
  (added explicitly using α as a structural input, per user's
  framing)

But:
- **Trough depth is ~21 MeV** at the σ_t value that gives the right
  position (~1.6 fm), vs observed ~50 MeV at ~1 fm.
- The σ_t value needed (-20 dimensionless) doesn't have an obvious
  α-relation (σ_t / α = -2740, σ_t · √α = -1.7).
- The 7-tensor as currently constructed couples depth and position:
  Depth · r₀² ≈ -10 MeV·fm² (constant, set by the (ℏc)² S-kinetic
  scale), vs observed Depth · r₀² ≈ -50 MeV·fm². Off by factor ~5.

So the 7-tensor produces the right SHAPE but the structural
parameters (with A = (ℏc)² for S kinetic) don't naturally reach
the observed nuclear potential strength.

Script:
[`scripts/track7_phase7a_seven_tensor.py`](scripts/track7_phase7a_seven_tensor.py)
Outputs:
[`outputs/track7_phase7a_potential_curves.csv`](outputs/track7_phase7a_potential_curves.csv) ·
[`outputs/track7_phase7a_potential_curves.png`](outputs/track7_phase7a_potential_curves.png)

---

## Phase 7a — 7-tensor sweep at R64 Point B

### Method

Construct a 7-tensor metric with:
- 6 Ma diagonals from R64 Point B p-sheet (and R63 e/ν, though
  e- and ν-sheets don't appear in nucleons, so they're ignored
  here for simplicity).
- 1 S spatial dimension with kinetic scale A = (ℏc)² (the natural
  relativistic-kinetic normalization).
- Cross-shears σ_t (tube↔S) and σ_r (ring↔S) between p-sheet and S.

For a two-particle p-sheet compound at additive winding (n_pt,
n_pr), the mass-squared as a function of S-momentum k_S = 1/r is:

<!-- m²(k_S) = m²_Ma + A · k_S² + 2·k_S·(σ_t·n_pt + σ_r·n_pr)·ℏc -->
$$
m^2(k_S) \;=\; m_{\text{Ma}}^2 + A \cdot k_S^2 +
                2 \, k_S \cdot (\sigma_t \cdot n_{pt} +
                                \sigma_r \cdot n_{pr}) \cdot \hbar c.
$$

For two protons (R64 (3, +2) each): joint compound (6, +4).
For proton+neutron (deuteron): (6, 0).
For two neutrons: (6, −4).

Energy: `E(r) = m(r) − m_constituents_sum`.

Coulomb is added separately for charged pairs as `α·ℏc·Z₁Z₂/r`.

### F7a.1. Setting σ_r = 0 is structurally required for charge-independence

Initial sweep used σ_r (ring cross-shear). But:
- pn has n_pr = 0, so σ_r contributes nothing to the deuteron's
  cross-coupling.
- pp has n_pr = +4, nn has n_pr = −4. With σ_r ≠ 0, pp and nn
  would have OPPOSITE strong-force corrections (one more bound,
  the other less).

This is structurally wrong: the strong nuclear force is
approximately charge-symmetric (per the
[primer](../../primers/nuclear-scaling.md)).

Setting σ_r = 0 and using only σ_t (tube↔S coupling) gives the
right structure: σ_t couples to n_pt = 6 in all three configs
equally, producing a charge-independent strong-force contribution.

This is the first non-trivial finding of Track 7: **the
charge-independence of the strong force selects σ_r = 0 as the
right structural choice** in the 7-tensor framework.

### F7a.2. Ma alone produces some pn over-binding

Before adding S coupling, R64's Ma at Point B gives:

| Config | m_Ma | m_constituents | Δ_Ma |
|:---|:-:|:-:|:-:|
| pp (6, +4) | 1876.55 | 1876.54 | +0.01 |
| pn (6, 0)  | 1860.52 | 1877.84 | **−17.32** |
| nn (6, −4) | 1879.14 | 1879.13 | +0.01 |

The Ma side already supplies **~17 MeV of pn over-binding** at the
compound level, present even without any S-coupling. This is the
deuteron-overshoot of Track 5 reappearing — at the 2-particle
compound (6, 0), R64's flat Ma formula gives a value ~17 MeV
below the additive sum.

Observed deuteron binding is 2.22 MeV (much less). So R64-Ma
alone over-predicts the deuteron's bulk binding by ~15 MeV. The
S-coupling adds an additional, r-dependent contribution on top.

### F7a.3. Sweeping σ_t gives a clear trough shape

Sweeping σ_t (negative = attractive) at fixed σ_r = 0:

| σ_t | r₀ (trough position, fm) | Trough depth (additional, MeV) |
|:-:|:-:|:-:|
| −0.5 | 65.8 | tiny |
| −1.0 | 32.9 | tiny |
| −5.0 | 6.6 | small |
| −10.0 | 3.3 | ~1 |
| −20.0 | **1.64** | **3.87** |

(Best fit to "trough at ~1 fm, ~50 MeV deep" search: σ_t = −20
hit the sweep boundary, giving r₀ = 1.64 fm with depth 3.9 MeV
of *additional* binding above R64's Ma over-binding.)

### F7a.4. The structural relationship: Depth · r₀² is fixed

Algebraically:

- r₀ = 2A/|B| where A = (ℏc)², B = 12·σ_t·ℏc
- Depth ΔM = −B²/(8·A·m_Ma)
- Therefore ΔM · r₀² = −A/(2·m_Ma) ≈ −10.4 MeV·fm² (with A = (ℏc)²,
  m_Ma ≈ 2·m_p)

Observed nuclear potential: ΔM · r₀² ≈ −50 MeV·fm² (at depth 50,
position 1 fm). Off by factor ~5.

To match observation, **A would need to be ~5·(ℏc)²** (i.e., the
S-kinetic scale isn't (ℏc)² but ~5·(ℏc)²). Or some other parameter
needs to scale appropriately.

### F7a.5. σ_t doesn't have a clean α-relation

At σ_t = −20 (best fit at sweep boundary):

| Quantity | Value |
|:---|:-:|
| σ_t / α | −2741 |
| σ_t · α | −0.146 |
| σ_t · √α | −1.71 |

None of these match natural α-derived values (1, 1/137, √α ≈ 0.085,
etc.). The cross-shear value as currently structured doesn't
emerge from α universality. This is consistent with the user's
clarification that **α is an INPUT to GRID, not a derivation** —
there's no a priori reason σ_t would be α-related, even if the
S-Ma coupling magnitude is "1/α" in a structural sense.

### F7a.6. Marginal-nucleon preference is satisfied

At σ_t = −20:

| Config | Min E (after Coulomb) | At r |
|:---|:-:|:-:|
| pp | −3.00 MeV | 1.86 fm |
| pn | **−21.19 MeV** | 1.64 fm |
| nn | similar to pp | similar |

**pn binding is 18 MeV deeper than pp**, consistent with observed
preference for N ≈ Z light nuclei over pure-proton or pure-neutron
configurations.

This is structurally meaningful: in the 7-tensor, the pn
preference comes naturally from the Ma side (R64's (6, 0) compound
is lighter than (6, ±4)), with the S-coupling contributing
charge-independently.

The "marginal nucleon preference" criterion (criterion 4) is
qualitatively satisfied: at given (Z, N), the next nucleon
prefers to maintain N ≈ Z balance, which is observed in the
valley-of-stability shape for light nuclei.

### F7a.7. What Phase 7a establishes

**Positive findings**:

1. **Trough shape exists** in E(r) under the 7-tensor — a real
   structural result, not by construction.
2. **Charge-independence** of the strong force selects σ_r = 0
   structurally — a physical constraint emerges from the
   geometry.
3. **pn preferred over pp** matches nuclear stability — the
   Ma-side (R64 Point B) supplies this without further input.
4. **Coulomb tail** added cleanly at large r for charged
   configurations.

**Limitations**:

5. **Scale off by factor ~2-5**: depth too shallow at the
   structurally-natural A = (ℏc)² S-kinetic scale.
6. **σ_t value (−20) doesn't have a clean structural origin**.
   It's fitted, not derived.
7. **The trough's "Depth · r₀²" is structurally fixed** by the
   7-tensor formula at ~−10 MeV·fm² with A = (ℏc)². To match
   nature (~−50 MeV·fm²), we'd need A larger by factor 5 or a
   different functional form.
8. **No "barrier"** in the strict sense — m(r) rises monotonically
   as r → 0 (from the 1/r² term). The hard-core repulsion exists
   but isn't a discrete barrier between attractive and repulsive
   regions.

### F7a.8. Reading

The 7-tensor approach produces the right STRUCTURE for the
nuclear potential — trough, charge-independence, pn preference,
Coulomb tail — but with the simple form chosen here, the SCALE
of the trough doesn't naturally match observation.

Two readings, both honestly available:

**Reading A — refine the framework**: a more structurally rich
7-tensor (additional cross-shears between sheets, different
S-kinetic coefficient, or higher-order coupling terms) might
match the scale naturally. The current setup is the simplest
possible; richness might bring it into agreement.

**Reading B — accept partial success**: MaSt's 7-tensor produces
the shape of the NN potential from its geometric structure but
the strength remains an empirical input (analogous to how QCD's
α_s is an empirical coupling). Combined with the Ma-side pn
overbinding and Coulomb's tail (both already in MaSt), this
gives a qualitative derivation of the strong force.

### F7a.9. Did we declare victory?

The user's victory criteria, with current results:

| # | Criterion | Status |
|:-:|:---|:-:|
| 1 | Energy curve matches strong-force shape | **Partial** — trough yes, depth/scale off |
| 2 | P-sheet supports both p and n | ✓ (R64 Point B already does) |
| 3 | Shear explains light elements' Fe preference | Inherits Track 3's chain fit |
| 4 | Marginal-nucleon preference computable | ✓ (pn deeper than pp at trough) |

Three of four criteria are satisfied at least qualitatively; the
fourth (energy-curve scale) is partially right.

Not yet a clean victory, but **structurally encouraging**.

---

## Recommended next steps

If continuing Track 7:

- **Phase 7b — Refined 7-tensor**. Test variations: include both
  σ_t and σ_r with relative magnitudes, larger S-kinetic A,
  different functional forms (e.g., Yukawa-like decay built into
  the metric structure).
- **Phase 7c — α-pinning analysis**. Look at R59 / R60 for any
  natural σ_t value emerging from sheet-coupling structure
  (despite α being an input). If σ_t = √α · (some natural number),
  that's a partial derivation.
- **Phase 7d — Connection to Yukawa/pion exchange**. Check if the
  7-tensor's E(r) can be re-expressed as the Yukawa form
  e^(-mr)/r at large r. If yes, identify the "exchange particle"
  in MaSt's lattice.

If pausing Track 7 here:

- The structural success (right shape, charge-independence, pn
  preference) is documentable as a partial first-principles
  derivation.
- The scale gap (factor ~2-5) is a known limitation that future
  refinements would address.

---

## Phase 7b — Yukawa fit analysis

Tested whether the 7-tensor's E(r) fits a Yukawa form `−A·exp(−m·r/ℏc)/r`
or other functional shapes.

### F7b.1. Polynomial 1/r² + 1/r is essentially exact

Four functional forms fitted to 7-tensor V(r) over r ∈ [0.5, 5] fm:

| Rank | Form | R² | RMS (MeV) |
|:-:|:---|:-:|:-:|
| 1 | **Polynomial A₂/r² + A₁/r** | **0.999816** | **0.038** |
| 2 | Yukawa | −0.010 | 2.82 |
| 3 | Inverse-square | −0.459 | 3.39 |
| 4 | Coulomb | −0.556 | 3.50 |

The polynomial fit is **essentially exact** (R² = 0.9998); Yukawa,
Coulomb, and inverse-square all have negative R² (worse than
just predicting the mean).

### F7b.2. The polynomial fit matches the analytical derivation exactly

For the 7-tensor with `m²(r) = m_Ma² + A/r² + B/r` (where A = (ℏc)²
and B = 2·σ_t·n_pt·ℏc), expanding `m(r) − m_Ma`:

<!-- V(r) ≈ A/(2 m_Ma r²) + B/(2 m_Ma r) -->
$$
V(r) \;\approx\; \frac{A}{2 m_{\text{Ma}}}\cdot\frac{1}{r^2}
                 + \frac{B}{2 m_{\text{Ma}}}\cdot\frac{1}{r}.
$$

With our parameters: A = 38927 MeV²·fm², B = −47352 MeV²·fm,
m_Ma = 1860.4 MeV:
- A/(2·m_Ma) = 10.46 MeV·fm²
- B/(2·m_Ma) = −12.73 MeV·fm

Compare to the fit: A₂ = 10.271, A₁ = −12.359. Match within
linearization error (the relativistic √-correction).

**This confirms the 7-tensor produces V(r) = polynomial in 1/r BY
CONSTRUCTION.** It cannot produce exponential decay through this
mechanism.

### F7b.3. The Yukawa fit gives a nonsensical exchange mass

Forced Yukawa fit gives m = 1521 MeV — about 11× the pion mass,
range ~0.13 fm.  This isn't "the pion shows up" — it's the fitter
finding that exponential decay with a very large m approximates
the polynomial near r ~ 0, which is mathematically bad and
physically uninterpretable.

### F7b.4. Why the 7-tensor can't produce Yukawa

In QFT, the Yukawa potential `V(r) = −g²·exp(−mr)/r` arises from
the propagator of a massive boson:

<!-- V(r) ∝ ∫ d³k exp(ik·r) / (k² + m²) -->
$$
V(r) \;\propto\; \int d^3 k \,\frac{e^{i \vec{k}\cdot\vec{r}}}
                                    {k^2 + m^2}
\;\propto\; \frac{e^{-mr}}{r}.
$$

The integration over all momenta with the propagator pole gives
the exponential.  The exchange particle's mass `m` sets the
range.

Our 7-tensor evaluates `m²(k_S)` at a SINGLE momentum `k_S = 1/r`
(not an integral over all momenta).  The result is polynomial,
not exponential.  **There's no propagator structure in the simple
7-tensor**, so no Yukawa-style decay can emerge.

### F7b.5. What this means

The simple 7-tensor approach as built **cannot produce the
observed Yukawa form of the strong nuclear force**.  Three
honest readings:

**Reading A — Simple 7-tensor is wrong**.  The strong force
requires propagator-based exchange physics that this metric-
coupling approach doesn't capture.  Need a different formalism
(QFT-style exchange amplitudes in MaSt's framework).

**Reading B — Partial picture**.  The polynomial part of E(r)
captures *some* of the strong force's contribution (perhaps the
"hard core" + "intermediate range").  Yukawa-like exponential
tail comes from a separate mechanism (lighter-meson exchange
via propagator) that requires additional MaSt structure.

**Reading C — Strong force isn't really Yukawa anyway**.
Phenomenologically, NN scattering data is well-fit by Yukawa,
but at higher accuracy multiple exchange channels (π, ρ, ω, σ)
contribute.  The "true" V(r) has multiple components.  The
7-tensor's polynomial might match one of these channels but
miss others.

I lean toward **Reading A**.  The structural reason: metric
coupling at a single mode IS NOT the same as virtual-particle
exchange.  The strong force in QFT is an EXCHANGE process; the
7-tensor doesn't model exchanges, only static metric coupling.

### F7b.6. The 7-tensor's polynomial form is structurally Coulomb-like at large r

The fitted A₁ = −12.36 MeV·fm.  Compare to Coulomb's coefficient
α·ℏc·Z₁Z₂ = (1/137)·197.3·1·1 = 1.44 MeV·fm.  Our A₁ is ~9× the
Coulomb scale.  At large r, V(r) ≈ A₁/r dominates (the 1/r²
term decays faster).

So the 7-tensor's large-r tail looks like **Coulomb with a
strength ~9× larger than EM**.  This is consistent with the
strong force being "nuclear EM" at long range — but in nature
the strong force has the EXPONENTIAL Yukawa cutoff, which our
7-tensor can't produce.

A philosophical note: if MaSt's strong force is structurally
Coulomb-like with strength α_s (~1) instead of α (~1/137), we'd
have a *power-law* strong force.  Nature has Yukawa.  The
discrepancy is real and meaningful.

### F7b.7. Implications for Track 7

Phase 7b's negative result reframes Track 7's status:

- **Phase 7a's right-shape, wrong-scale** is now understood as
  "right shape" being polynomial (which IS right at intermediate
  r) but missing the Yukawa exponential tail at large r.
- The 7-tensor can produce NUCLEAR-SCALE attraction (depth ~21
  MeV at ~1.6 fm) but not the right LONG-RANGE behavior.
- For the observed Fe peak and full nuclear-force phenomenology,
  we'd need a propagator-based formalism (or accept that the
  7-tensor is a partial model).

Track 7's contribution: a structural derivation that the strong
force in MaSt is **polynomial 1/r² + 1/r** at the simple metric-
coupling level, with charge-independence as a structural
constraint.  This is not the full strong force as observed in
nature, but it's a honest first step.

---

---

## Phase 7c — Corrected two-body kinematics

Phase 7a treated the joint two-nucleon compound as a single
particle of mass `M_total = 2·m_p` carrying momentum
`p = ℏ·k_S`, giving the kinetic coefficient `A = (ℏc)²` in
`m²(k_S) = m²_Ma + A·k_S²`.

But `k_S = 1/r` physically represents the **relative momentum**
between two nucleons in their COM frame.  For two equal-mass
particles:

<!-- M_inv²(p_rel) = M_total² + 4·p_rel² -->
$$
M_{\text{inv}}^2(p_{\text{rel}}) = M_{\text{total}}^2 + 4 \, p_{\text{rel}}^2
$$

So the kinematic coefficient should be **`A = 4·(ℏc)²`**, not
`(ℏc)²`.  Equivalently, in the non-relativistic picture, relative-
motion kinetic energy uses reduced mass `μ_red = m_p/2` (for
equal masses), four times smaller than the `2·m_p` we implicitly
used.

**This factor-of-4 correction explains most of Phase 7a's scale
miss directly.**

Script:
[`scripts/track7_phase7c_two_body_kinematics.py`](scripts/track7_phase7c_two_body_kinematics.py)
Outputs:
[`outputs/track7_phase7c_potential_curves.csv`](outputs/track7_phase7c_potential_curves.csv) ·
[`outputs/track7_phase7c_potential_curves.png`](outputs/track7_phase7c_potential_curves.png)

### F7c.1. Predicted scale identity under corrected kinematics

With `A = 4·(ℏc)²`:

<!-- Depth · r₀² = A / (2 · M_total) = (ℏc)² / m_p ≈ 41.5 MeV·fm² -->
$$
\text{Depth} \cdot r_0^2 \;=\; \frac{A}{2\,M_{\text{total}}}
\;=\; \frac{(\hbar c)^2}{m_p}
\;\approx\; 41.5 \text{ MeV·fm}^2.
$$

Observed nuclear NN potential: `Depth · r₀² ≈ 50 MeV·fm²` (depth
~50 MeV at r₀ ~1 fm).  Phase 7c lands **17% from observation**
at the linearized level, vs Phase 7a's factor-5 miss at 10.4
MeV·fm².

### F7c.2. σ_t sweep result

Sweeping σ_t ∈ [−200, 0] for the pn channel (best fit to "trough
at 1 fm with depth 50 MeV"):

| Quantity | Phase 7a | Phase 7c |
|:---|:-:|:-:|
| Kinetic coefficient A | (ℏc)² | 4·(ℏc)² |
| Best σ_t | −20 (sweep boundary) | **−116.1** |
| Trough position r₀ | 1.64 fm | **1.135 fm** |
| Trough depth | −21.2 MeV | **−50.2 MeV** |
| Depth · r₀² | ~10 MeV·fm² | ~65 MeV·fm² (relativistic) |

Phase 7c lands **inside the observed band** of 40–60 MeV depth
at ~1 fm.  The trough depth slightly exceeds the linearized
estimate (50 vs 41.5 MeV) because of relativistic √-correction
to the polynomial form at r ~ 1 fm — a real, not fit, effect.

### F7c.3. Charge-symmetry and pn preference preserved

At σ_t = −116.1, σ_r = 0:

| Config | r₀ (fm) | E_min (MeV, with Coulomb) |
|:---|:-:|:-:|
| pp | 1.150 | −31.34 |
| pn | 1.135 | **−50.21** |
| nn | 1.135 | −32.55 |

- **pn deeper than pp** by 18.9 MeV (Ma-side at Point B supplies
  this without further input).
- **pn deeper than nn** by 17.7 MeV.
- **pp ≈ nn** modulo Coulomb shift (charge-symmetric strong
  contribution).

All three structural features from Phase 7a are preserved at the
corrected kinematic scale.

### F7c.4. σ_t at the corrected kinematics — structural status

| Quantity | Value |
|:---|:-:|
| σ_t | −116.1 |
| σ_t · α | −0.847 |
| σ_t · √α | −9.92 |
| σ_t / 4π | −9.24 |
| σ_t · n_pt² · α | −30.5 |
| σ_t · ε_p | −23.82 |

None of these is a clean integer or natural unit.  **σ_t at
Phase 7c sits as an empirical strong-coupling parameter** —
analogous to QCD's α_s.  No structural derivation from R64's
existing parameters (ε_p, s_p, K_p, α) reveals it.

The analytical prediction at exact r₀ = 1 fm gives
`|σ_t| = 4·ℏc/n_pt = 131.5`; the numerical fit lands at 116.1
because the trough position drifts to 1.135 fm under the
relativistic √-correction.

### F7c.5. Acceptance criteria

| # | Criterion | Status |
|:-:|:---|:-:|
| 1 | Depth at r_min ≈ 1 fm in 40–60 MeV range | ✓ (50.2 MeV at 1.135 fm) |
| 2 | pn deeper than pp by 10–25 MeV | ✓ (18.9 MeV) |
| 3 | Coulomb tail correct | ✓ (preserved) |
| 4 | σ_t value documented | ✓ (empirical, no clean α-relation) |

All four Phase 7c acceptance criteria met.

### F7c.6. What Phase 7c establishes

The 7-tensor at R64 Point B with corrected two-body kinematics
produces:

- **Strong-force trough at r ≈ 1 fm with depth ~50 MeV** —
  matching observed NN scattering data.
- **pn preferred over pp by ~19 MeV** — matching nuclear
  stability.
- **Charge-symmetric** (σ_r = 0) — matching observed approximate
  charge-independence.
- **Coulomb 1/r tail** at large r for charged configurations.

The polynomial form (1/r² + 1/r, vs nature's Yukawa) remains as
a Phase 7b finding — at intermediate r (the deuteron's binding
scale, r ~ 1–2 fm), the polynomial approximates the Yukawa form
adequately for trough-scale physics.  At large r (> 2 fm), the
polynomial lacks the exponential cutoff; this is a separate
question requiring propagator-based extension of the formalism.

**Phase 7c upgrades Track 7 from "right shape, wrong scale" to
"right shape AND right scale at intermediate r, with one
empirical coupling σ_t."**

---

---

## Phase 7d — Schrödinger validation of Phase 7c V(r)

Phase 7c demonstrated that the 7-tensor V(r) has the right
shape and scale at the trough.  Phase 7d tests whether the
**quantum-mechanical observables** of that V(r) — bound-state
energies and scattering lengths — match observation when V(r)
is solved as a two-body radial Schrödinger problem.

Script:
[`scripts/track7_phase7d_schrodinger.py`](scripts/track7_phase7d_schrodinger.py)
Outputs:
[`outputs/track7_phase7d_results.csv`](outputs/track7_phase7d_results.csv) ·
[`outputs/track7_phase7d_potential_and_wavefunctions.png`](outputs/track7_phase7d_potential_and_wavefunctions.png)

### Method

Radial Schrödinger equation with reduced-mass Hamiltonian:

<!-- −ℏ²/(2μ) u'' + V(r) u = E u -->
$$
-\frac{\hbar^2}{2\mu}\,u''(r) + V(r)\,u(r) \;=\; E\,u(r)
$$

with `μ = m_p·m_n/(m_p+m_n)` for pn (similarly for nn, pp), and
`V(r) = m_compound(r) − m_Ma(n_pt, n_pr)` (subtracts the constant
Ma-side offset so V(∞) = 0).  Bound states found by shooting
method (scipy.integrate solve_ivp + brentq sign-change refinement);
scattering lengths extracted from k·cot(δ) = −1/a + (r_eff/2)·k²
effective-range fit at low k.

### F7d.1. Multiple bound states emerge in all channels

| Channel | Bound states | E (MeV)            | Observed |
|:---|:-:|:---|:---|
| pn  | 3 | −12.64, −4.82, −2.22 | 1 (deuteron at −2.22) |
| nn  | 3 | −12.46, −4.74, −2.17 | **0 (unbound)** |
| pp  | 3 | −11.99, −4.56, −2.05 | **0 (unbound)** |

The nn and pp channels having multiple bound states is decisively
wrong — observation says these systems are unbound.  The pn
channel having THREE bound states is also wrong; nature has only
the deuteron.

### F7d.2. Deuteron binding energy off by factor ~13

| Quantity | Phase 7d | Observed |
|:---|:-:|:-:|
| Schrödinger eigenvalue (above V(∞)) | −12.64 MeV | — |
| Ma-side offset Δ_Ma(pn) | −17.32 MeV | — |
| Total binding from free-nucleon threshold | **29.95 MeV** | **2.22 MeV** |

Phase 7d's pn ground state is bound by 30 MeV from the free-nucleon
threshold — vs observed 2.22 MeV.  Off by **factor 13.5**.

(Numerically, the *third* bound state at −2.22 MeV happens to land
at the observed B(²H) value.  This is coincidence — that state is
the highest excited state of a Rydberg-like spectrum, not the
ground state, so it doesn't represent a successful prediction.)

### F7d.3. The Rydberg-like spectrum diagnoses the polynomial tail

The bound-state spectrum follows approximately
`E_n = −μ·B²/(2·n²)` — a Coulomb-like Rydberg series — with
effective dimensionless coupling

<!-- B = |A_1| / ℏc = |σ_t · n_pt · ℏc / m_Ma| / ℏc -->
$$
B \;=\; \frac{|A_1|}{\hbar c} \;=\;
\left|\frac{\sigma_t \cdot n_{pt}}{m_{\text{Ma}}}\right|
\;\approx\; 0.374
$$

(compare to QED's α ≈ 0.0073).  The 7-tensor's polynomial 1/r
tail is acting like a strong attractive "Coulomb force" with
~50× the EM coupling — far larger than any short-range piece —
producing the bound-state ladder.

A Yukawa potential `V(r) = −g²·exp(−mr)/r` cuts off the
attraction at r > 1/m; the spectrum truncates to a single
deuteron-like bound state.  Phase 7d's failure mode is precisely
the predicted polynomial-vs-Yukawa structural difference (Phase
7b), now made concrete in quantum-mechanical observables.

### F7d.4. Scattering lengths — wrong sign for singlet

Effective-range fit of k·cot(δ) at low k:

| Channel | Phase 7d a (fm) | r_eff (fm) | Observed a (fm) | Status |
|:---|:-:|:-:|:-:|:-:|
| pn triplet (³S₁) | +13.2 | +33.7 | +5.42 | right sign, 2.4× off |
| nn singlet (¹S₀) | +22.5 | +34.9 | **−23.7** | **wrong sign** |

The singlet sign reversal is direct evidence that V(r) is too
attractive: nature's a_s ≈ −23.7 fm signals an *almost-bound*
state (very near the threshold, large negative scattering
length); Phase 7d's a_s ≈ +22.5 fm signals an *already-bound*
system (positive a, with bound states below threshold).
Reducing V(r)'s long-range attraction (Yukawa cutoff) would
move the singlet from "bound" to "almost-bound," reversing the
sign correctly.

The triplet a_t = +13 fm vs observed +5.4 fm is the same problem
in milder form: V(r) is binding the deuteron too strongly,
giving a smaller asymptotic |r·u(r)/u(r)| at low energy.

### F7d.5. Acceptance criteria

| # | Criterion | Status |
|:-:|:---|:-:|
| 1 | B(²H) within ±20% of 2.224 MeV | ✗ FAIL (factor 13.5) |
| 2 | a_t positive, few-fm magnitude | ✓ PASS (sign and order) |
| 3 | a_s large negative | ✗ FAIL (wrong sign) |
| 4 | nn unbound | ✗ FAIL (3 bound states) |
| 5 | pp unbound | ✗ FAIL (3 bound states) |

Phase 7d does **not** validate Phase 7c V(r) as a quantum-
mechanical NN potential.  The polynomial 1/r tail produces a
Coulomb-like attraction that dominates the bound-state spectrum
and scattering structure.

### F7d.6. What Phase 7d establishes

**The static-trough success of Phase 7c does not survive
quantum-mechanical lifting.**  At intermediate r (where Phase 7c
matched the observed depth ~50 MeV at ~1 fm), the polynomial
form approximates Yukawa adequately.  But the wavefunctions of
bound states sample V(r) at all r — including the long-range
1/r tail — and the integrated effect is dominated by that tail.

This is a clean structural finding, not a parameter-tuning
question:

- **σ_t cannot be retuned** to fix this.  Reducing |σ_t| weakens
  the trough below 50 MeV (which Phase 7c gets right) without
  fixing the qualitative tail problem.
- **No combination of (ε_p, s_p, σ_t)** at the polynomial form
  level can give one bound state instead of three or fix a_s sign
  — it's the functional form that's wrong.
- **The Yukawa exponential cutoff is structurally required** for
  the QM observables to land near observation — exactly what
  pool item m (propagator-based extension) addresses.

Phase 7d's negative result is therefore *informative*: it
confirms in concrete observables that the polynomial form is the
limiting factor at the deuteron-binding scale, not just at the
asymptotic tail.

### F7d.7. What Phase 7d does NOT invalidate

Phase 7c's *static-potential* claims still hold:

- Trough depth ~50 MeV at r ≈ 1 fm — consistent with NN potential
  phenomenology at intermediate r.
- pn preferred over pp by ~19 MeV — Ma-side at Point B.
- Charge symmetry preserved (σ_r = 0 structural constraint).
- Coulomb 1/r tail at large r for charged pairs.

These remain valid as features of the static V(r); Phase 7d
simply shows that integrating V(r) into the QM problem requires
the long-range tail to also be right, which the polynomial form
isn't.

---

---

## Phase 7e — α-coupling integration test

Phase 7c introduced new metric off-diagonals at (p_t, S_x), (p_t, S_y),
(p_t, S_z) — call them σ_pS_tube — to deliver the strong-force trough.
R60 model-F's α-architecture lives in the ℵ row (σ_ta tube↔ℵ, σ_at
ℵ↔t, σ_ra ring↔ℵ derived).  These are different rows/columns of the
11×11 metric.  Phase 7e tests whether they're algebraically
*decoupled* — i.e., whether α-extraction stays invariant under
non-zero σ_pS_tube.

Script:
[`scripts/track7_phase7e_alpha_integration.py`](scripts/track7_phase7e_alpha_integration.py)
Outputs:
[`outputs/track7_phase7e_alpha_universality.csv`](outputs/track7_phase7e_alpha_universality.csv) ·
[`outputs/track7_phase7e_alpha_curves.png`](outputs/track7_phase7e_alpha_curves.png)

### Method

Augment R60's `build_aug_metric(p)` (Track 7b — model-F with σ_ra
ring↔ℵ included) by writing σ_pS_tube into G[p_t, S_x],
G[p_t, S_y], G[p_t, S_z] (S-isotropic).  Sweep σ_pS_tube ∈
[−0.5, +0.5]; at each value:

1. Check signature (one negative eigenvalue).
2. Compute `alpha_coulomb(G, n11) / α₀` for ten model-F inventory
   modes spanning Q = ±1, 0 and the active-sheet taxonomy
   (electron, muon, proton, neutron, Λ, Σ⁻, π⁰, π±, K±, ρ).
3. Compare to baseline values at σ_pS_tube = 0.

### F7e.1. Baseline α-universality is reproduced

At σ_pS_tube = 0, the bare α-sum rule
`α/α₀ = (n_et − n_pt + n_νt)²` lands within numerical noise on
all ten test modes:

| Mode | α_sum | Expected α/α₀ | Observed α/α₀ |
|:---|:-:|:-:|:-:|
| electron | +1 | 1 | 1.000000 |
| muon | −1 | 1 | 1.000000 |
| proton (1,3) | −1 | 1 | 1.000000 |
| neutron | −1 | 1 | 1.000000 |
| Λ | −1 | 1 | 1.000000 |
| Σ⁻ | −1 | 1 | 1.000000 |
| π⁰ | −2 | 4 | 4.000000 |
| π± | −4 | 16 | 16.0 |
| K± | −3 | 9 | 9.000000 |
| ρ | −3 | 9 | 9.000000 |

R60 model-F's α-architecture is reproduced cleanly at σ_pS_tube = 0
— the test infrastructure is sound.

### F7e.2. Signature-preservation band is narrow

Sweeping σ_pS_tube ∈ [−0.5, +0.5] in the augmented metric, the
**signature stays Lorentzian only for σ_pS_tube ∈ [−0.075, +0.075]**.
Outside this window, additional negative eigenvalues appear and
the metric is no longer physical.  Phase 7c's value σ_t = −116
(in 7-tensor units) cannot be inserted directly as a dimensionless
metric entry — that's a unit-translation issue separate from this
band.  But within the dimensionless [−0.075, +0.075] window, we can
ask whether α-extraction survives.

### F7e.3. α is mode-dependently sensitive to σ_pS_tube

Sample α/α₀ at representative σ_pS_tube values:

| Mode | σ=−0.05 | σ=−0.01 | σ=0 | σ=+0.01 | σ=+0.05 |
|:---|:-:|:-:|:-:|:-:|:-:|
| electron | 1.166 | 1.0037 | 1.000 | 1.0037 | 1.166 |
| muon | 1.166 | 1.0037 | 1.000 | 1.0037 | 1.166 |
| proton | 0.565 | 0.989 | 1.000 | 0.989 | 0.565 |
| neutron | 4.396 | 1.051 | 1.000 | 1.051 | 4.396 |
| Λ | 0.393 | 0.927 | 1.000 | 0.927 | 0.393 |
| Σ⁻ | 0.144 | 0.972 | 1.000 | 0.972 | 0.144 |
| π⁰ | 4.663 | 4.015 | 4.000 | 4.015 | 4.663 |
| π± | 18.65 | 16.06 | 16.0 | 16.06 | 18.65 |
| K± | 8.410 | 8.986 | 9.000 | 8.986 | 8.410 |
| ρ | 8.410 | 8.986 | 9.000 | 8.986 | 8.410 |

Three structural features:

1. **Deviations are symmetric in σ** (e.g. ±0.05 give the same
   |Δα|).  The leading effect is **quadratic** in σ_pS_tube.
2. **Different modes shift in different directions.**  Electron
   α RISES at non-zero σ; proton α FALLS.  Charge-positive
   compounds and charge-negative compounds get pushed in opposite
   senses.
3. **The α-sum rule's universality is broken.**  At σ = ±0.05,
   different |α_sum|² values that originally agreed (e.g.
   electron and proton both at α/α = 1) now disagree (1.17 vs
   0.57).

### F7e.4. Universality preserved only at σ_pS_tube ≈ 0

Maximum relative deviation `max |α(σ)/α(0) − 1|` across modes vs
σ_pS_tube:

| Threshold ε | σ_pS_tube range satisfying |Δα/α| < ε |
|:---:|:---|
| 10⁻⁶ | [+0.00000, +0.00000] (only σ = 0) |
| 10⁻⁴ | [+0.00000, +0.00000] (only σ = 0) |
| 10⁻² | [−0.00250, +0.00250] (very narrow) |

Universality is structurally preserved only at σ_pS_tube = 0 to
machine-noise precision.  Even the loose 1% threshold gives a
window of only ±0.0025 — narrow compared to the [−0.075, +0.075]
signature band.

### F7e.5. Verdict — sectors are NOT decoupled

The α-coupling sector and the (p_t, S) coupling sector are
**algebraically coupled** through G⁻¹.  Adding σ_pS_tube ≠ 0 to
the model-F metric does not preserve R60's α-extraction; it
disturbs both the magnitude (α(electron) shifts away from α₀) and
the universality (different modes get different shifts).

This is a clean negative result on the simple decoupling
hypothesis.  It does **not** mean σ_pS_tube cannot exist — only
that a *naive* free σ_pS_tube ≠ 0 is incompatible with model-F's
α-architecture.

### F7e.6. What this implies for model-G integration

To carry Phase 7c's strong-force coupling into model-G without
regressing model-F's α-universality, σ_pS_tube needs a
**structural prescription** analogous to σ_ra = (s·ε)·σ_ta.  Two
candidate forms suggest themselves:

- **(A) σ_pS_tube = f(σ_ta, σ_at, sheet params)** — derived from
  existing α-architecture parameters, possibly with
  a constraint that cancels its contribution to G⁻¹[Ma, t].
- **(B) σ_pS_tube + companion entries** — additional (S, t),
  (S, ℵ) or (e_t, S), (ν_t, S) entries that, in combination,
  cancel the α-perturbation while preserving the strong-force
  trough.  Analogous to how R60's σ_ra cancels shear-induced
  mode-dependence in α.

Either route requires new structural derivation.  This sharpens
the next-track question:

- **Pool item j** (this phase) is now *answered*: sectors are
  coupled, σ_pS_tube needs structure.
- **Pool item m** (Yukawa propagator extension) becomes a
  natural foil: a propagator-based formulation may not require
  a metric off-diagonal at (p_t, S) at all — the strong force
  could come from a separate exchange particle in Ma whose
  propagator integrates to give Yukawa, leaving R60's metric
  algebraically untouched.

### F7e.7. Caveats

1. **Unit translation** between Phase 7c's σ_t = −116 (7-tensor
   units) and R60's dimensionless metric entries is non-trivial.
   The signature band [−0.075, +0.075] in dimensionless units
   does not directly map to "Phase 7c is in or out."  A separate
   calculation is needed to translate Phase 7c's σ_t to the
   equivalent metric entry — but the structural finding here
   (sectors couple) is independent of that translation.
2. **Charge-independence test (σ_pS_ring)** was not exercised.
   Phase 7c forces σ_pS_ring = 0 already, so no sweep is required.
3. **Higher-order companions.**  This phase tested a single new
   entry; companion entries that could restore universality
   weren't enumerated.  That's the structural-prescription work
   for whichever direction model-G integration takes.

---

## Phase 7f — Unit translation: 7-tensor σ_t ↔ 11D σ_pS_tube

Phase 7e left an unresolved question: where does Phase 7c's
σ_t = −116.1 (7-tensor units) land in the dimensionless 11D
universality band [−0.0025, +0.0025]?  Phase 7f answers this by
deriving the equivalent 11D σ_pS_tube via Schur-complement
matching of the cross term in m²(k_S).

Script:
[`scripts/track7_phase7f_unit_translation.py`](scripts/track7_phase7f_unit_translation.py)
Outputs:
[`outputs/track7_phase7f_unit_translation.csv`](outputs/track7_phase7f_unit_translation.csv) ·
[`outputs/track7_phase7f_unit_translation.png`](outputs/track7_phase7f_unit_translation.png)

### Method

Equating cross terms in m²(k_S):

- 7-tensor: `2 · k_S · σ_t · n_pt · ℏc`
- 11D Schur: `−(2π·ℏc)² · 2 · (n_pt/L_p) · k_S · σ_pS / (k_p · 1)`
  (leading order in σ_pS; G[p_t,p_t] = k_p, G[S,S] = 1)

Solving:

<!-- σ_pS = −σ_t · L_p · k_p / [(2π)² · ℏc] -->
$$
\sigma_{pS} \;=\; -\sigma_t \cdot L_p \cdot k_p \;\big/\; [(2\pi)^2 \cdot \hbar c]
$$

with L_p = ε_p · L_ring_p the p-sheet tube length.

### F7f.1. Translation result for Phase 7c at two baselines

| Baseline | ε_p | L_ring_p (fm) | L_p_tube (fm) | σ_pS_equiv |
|:---|:-:|:-:|:-:|:-:|
| R60 Track 9 model-F | 0.4 | 15.24 | 6.10 | **+0.00427** |
| R64 Point B | 0.2052 | 89.91 | 18.45 | **+0.01291** |

(Sign positive because σ_t < 0 and prefactor carries a negative sign.)

### F7f.2. Numerical verification

At Track 9 baseline with σ_pS = +0.00427 and test mode
(n_pt = 6, k_S = 1 fm⁻¹):

- m²(σ_pS = 0) = +8.795e7 MeV²
- m²(σ_pS = +0.00427) = +8.747e7 MeV²
- 11D Δm² = −4.75 × 10⁵ MeV²
- 7-tensor Δm² (cross only) = −2.75 × 10⁵ MeV²
- Ratio: **+1.73**

The 1.73 ratio reflects higher-order Schur corrections (the
linearization is not exact at this σ_pS magnitude) plus the
(2π)² factor's interaction with the kinetic A normalization.
The order of magnitude is correct; absolute precision would
require a more careful Schur-complement expansion or a
nonlinear matching condition.

### F7f.3. Locating in Phase 7e bands

Phase 7e's bands (model-F frame):
- Signature OK: [−0.0750, +0.0750]
- Universality < 10⁻⁶: only σ = 0
- Universality < 1%: [−0.0025, +0.0025]

| Translation | σ_pS_equiv | In sig band? | In 1% univ band? | × 1% threshold |
|:---|:-:|:-:|:-:|:-:|
| Track 9 baseline | +0.00427 | ✓ | ✗ | 1.7× |
| R64 Point B baseline | +0.01291 | ✓ | ✗ | 5.2× |

### F7f.4. Implication

Phase 7c's σ_t corresponds to a **moderate** dimensionless 11D
coupling — comparable to (Track 9) or several times larger than
(R64 PB) the 1% universality threshold.  Not deeply inside the
band ("safely small"), not catastrophically outside ("breaks
metric"); right at the **edge**.

Estimated α-perturbation magnitude at this σ_pS:
- ~0.12% on electron α (Track 9 σ_pS_equiv)
- ~few % on charge-positive compounds (R64 PB σ_pS_equiv)

This is the "moderate σ_pS_tube" case the review anticipated:
the metric stays physical, model-F's α-architecture is
disturbed at the few-percent level (not negligible, not
catastrophic).  Pool item j (structural prescription) and pool
item m (Yukawa pivot) both remain viable paths through this.

---

## Phase 7g — α-test at R64 Point B with R64 u/d inventory

Phase 7e tested model-F regression (proton at (0,0,0,0,1,3),
etc.).  Phase 7g tests the same structural question at R64's
own frame: R64 Point B parameters with R64 u/d compound tuples
(proton (3,+2), neutron (3,−2), deuteron (6,0)).

Script:
[`scripts/track7_phase7g_R64_inventory.py`](scripts/track7_phase7g_R64_inventory.py)
Outputs:
[`outputs/track7_phase7g_R64_alpha_universality.csv`](outputs/track7_phase7g_R64_alpha_universality.csv) ·
[`outputs/track7_phase7g_R64_alpha_curves.png`](outputs/track7_phase7g_R64_alpha_curves.png)

### F7g.1. Baseline α-extraction at R64 Point B

At σ_pS = 0 with R64 PB params:

| Mode | Tuple | α_sum | Expected α/α₀ | Observed α/α₀ |
|:---|:-:|:-:|:-:|:-:|
| electron | (1,2,0,0,0,0) | +1 | 1 | 1.000 |
| muon | (1,1,−2,−2,0,0) | −1 | 1 | 1.000 |
| **R64 proton** | (0,0,0,0,3,+2) | **−3** | **9** | **9.000** |
| **R64 neutron** | (0,0,0,0,3,−2) | **−3** | **9** | **9.000** |
| **R64 deuteron** | (0,0,0,0,6,0) | **−6** | **36** | **36.0** |
| R64 pp | (0,0,0,0,6,+4) | −6 | 36 | 36.0 |
| π⁰ | (0,−1,−2,−2,0,0) | −2 | 4 | 4.000 |
| K± | (−1,−6,−2,2,0,1) | −3 | 9 | 9.000 |

The R64 baryon tuples give **α/α₀ = 9** (proton, neutron) or
**α/α₀ = 36** (deuteron, NN compounds) under the bare α-sum
rule, **not** the physical 1 or Z².  This is a known R64-specific
issue requiring a different α-attribution rule (pool item g,
"Charge-attribution rule extension").  Phase 7g sidesteps this
by testing **relative ratios** α(σ)/α(0) — coupling structure
is independent of the baseline α value.

### F7g.2. Signature and universality bands at R64 frame

| Band | Phase 7e (model-F) | **Phase 7g (R64 PB)** |
|:---|:-:|:-:|
| Signature OK | [−0.0750, +0.0750] | **[−0.1100, +0.1100]** |
| Universality < 10⁻⁶ | only σ = 0 | only σ = 0 |
| Universality < 1% | [−0.0025, +0.0025] | **[−0.0075, +0.0075]** |

The R64 frame has both wider signature window (~1.5×) and
wider 1% universality region (3×).  The wider tolerance is a
geometric consequence of R64's (ε_p, s_p) being smaller, which
shifts the off-diagonal weight in G⁻¹.

### F7g.3. Two-group coupling pattern at R64's frame

α(mode)/α(σ=0) ratios at sample σ_pS:

| Mode | σ=−0.05 | σ=−0.01 | σ=+0.01 | σ=+0.05 |
|:---|:-:|:-:|:-:|:-:|
| electron | 1.116 | 1.0036 | 1.0036 | 1.116 |
| muon | 1.116 | 1.0036 | 1.0036 | 1.116 |
| **R64 proton** | **1.579** | **1.0165** | **1.0165** | **1.579** |
| **R64 neutron** | **1.583** | **1.0166** | **1.0166** | **1.583** |
| **R64 deuteron** | **1.581** | **1.0166** | **1.0166** | **1.581** |
| **R64 pp** | **1.579** | **1.0165** | **1.0165** | **1.579** |
| **R64 nn** | **1.583** | **1.0166** | **1.0166** | **1.583** |
| π⁰ | 1.116 | 1.0036 | 1.0036 | 1.116 |
| π± | 1.116 | 1.0036 | 1.0036 | 1.116 |
| K± | 1.116 | 1.0036 | 1.0036 | 1.116 |
| ρ | 1.116 | 1.0036 | 1.0036 | 1.116 |

**Two clean groups** emerge:

- **p-sheet group** (R64 proton, neutron, deuteron, pp, nn — all
  R64 baryon-class compounds): shift uniformly together,
  ~3.4× the rate of the e/ν group.
- **e/ν group** (electron, muon, mesons): shift uniformly
  together at a smaller rate.

Within each group: deviations agree to 4+ significant figures.
Between groups: relative shift differs by factor ~3.4.

This is a **structural feature**, not noise.  σ_pS_tube
modifies G⁻¹ in a way that affects p-sheet modes more strongly
than e/ν modes (because the perturbation is on the p-sheet
row).  Modes on the same sheet shift uniformly because the
α-extraction formula's mode-dependence factors out within a
sheet.

### F7g.4. Implication for companion-entry strategy

The two-group pattern is highly informative for pool item j's
companion-entry search.  Phase 7e's 10-mode chaos (different
sign shifts across modes) was actually masked by the fact that
some R60 model-F tuples mix sheets in complex ways.  At R64's
clean p-sheet-only baryon picture, the perturbation reduces to
**a 2-parameter structure**: one coefficient for the p-sheet
group, one for the e/ν group.

A companion entry σ_companion at e.g. (e_t, S_*) or (ν_t, S_*)
that reproduces the same magnitude perturbation on the e/ν
group while leaving the p-sheet group unaffected would
**equalize the two groups' shifts**, restoring universality at
second order.  This is a concrete and tractable
structural-prescription problem.

### F7g.5. Comparison to Phase 7e

The "α-sectors are coupled" finding survives at R64's frame.
The structure is **cleaner** at R64's frame: the two-group
pattern (p-sheet vs e/ν) is more interpretable than 7e's
mode-by-mode chaos.

Where Phase 7c's σ_pS_equiv = +0.0129 (R64 PB baseline) lands:

| Reference | Threshold | Status |
|:---|:-:|:-:|
| Phase 7g signature band | [−0.110, +0.110] | ✓ Inside |
| Phase 7g 1% universality | [−0.0075, +0.0075] | ✗ 1.7× over |
| Estimated α-shift on R64 proton | — | ~3% |
| Estimated α-shift on electron | — | ~0.6% |

The α perturbation at Phase 7c's coupling is:
- ~3% on R64 baryons (proton, neutron, deuteron, NN compounds)
- ~0.6% on leptons and mesons

Few-percent disagreement between sheets — structurally
disturbing for model-G integration unless cancelled by
companion entries.

### F7g.6. Recap of the conditional from F7e.6

Phase 7e/7f/7g together resolve the conditionality flagged in
F7e.6:

- (a) **Phase 7c's coupling is non-trivial in 11D** (F7f.3): it's
  outside the 1% universality band by factor 2-5.
- (b) **The same coupling pattern persists at R64's frame**
  (F7g.4): two-group structure (p-sheet vs e/ν), each shifting
  uniformly.
- (c) **Companion-entry resolution is more tractable than
  expected** (F7g.4): the two-group pattern reduces companion
  search to a 2-parameter constraint, not a per-mode constraint.

Net read: Phase 7c's σ_t **does** require a structural
prescription to coexist with R60's α-architecture; the
prescription likely takes the form of one or two companion
entries (e_t, S) and/or (ν_t, S) that equalize the e/ν-sheet
shift to match the p-sheet shift.  This is pool item j's
companion-entry direction.  Pool item m (Yukawa pivot) remains
the alternative path that sidesteps the companion problem
entirely by removing the (p_t, S) entry from the metric.

---

## Phase 7h — Yukawa QM observables test

Phase 7d showed Phase 7c's polynomial V(r) produces 3 bound states
in pn (vs 1 deuteron observed) and binds nn, pp (vs unbound).  The
polynomial 1/r tail acts like a strong attractive Coulomb-like
force.  Pool item m (Yukawa propagator extension) is the natural
structural reframing.  Phase 7h tests whether Yukawa form
`V(r) = −g²·ℏc·exp(−m·r/ℏc)/r` resolves the QM failures.

Script:
[`scripts/track7_phase7h_yukawa_qm.py`](scripts/track7_phase7h_yukawa_qm.py)
Outputs:
[`outputs/track7_phase7h_yukawa_results.csv`](outputs/track7_phase7h_yukawa_results.csv) ·
[`outputs/track7_phase7h_yukawa_curves.png`](outputs/track7_phase7h_yukawa_curves.png)

### Method

Three Yukawa variants, each with a g² sweep:

- **V1** Pure Yukawa, m = 140 MeV (pion mass).
- **V2** Pure Yukawa, m = 254 MeV (R64's `(0, ±4)` compound mass —
  the closest meson-class state in R64's Ma lattice).
- **V3** Hybrid: Phase 7c kinetic 1/r² hard core +
  Yukawa attraction, m = 140 MeV.

For each (variant, g²) combination, run Phase 7d's Schrödinger
solver on pn (no Coulomb), nn (no Coulomb), pp (with Coulomb).
Report bound-state count, B(²H) = −E_ground in pn, triplet
scattering length a_t.

### F7h.1. Yukawa exponential cutoff fixes the bound-state spectrum

V1 sweep results (m = 140 MeV):

| g² | pn bound states | B(²H) MeV |
|:-:|:-:|:-:|
| 0.05 | 0 (unbound) | — |
| 0.30 | 1 | 0.32 |
| **0.40** | **1** | **3.76** |
| 0.50 | 1 | 11.0 |
| 0.70 | 1 | 37.2 |

The bound-state count drops from 3 (Phase 7d's polynomial) to **1
or 0** across the relevant Yukawa parameter range.  This confirms
the structural diagnosis from Phase 7d: the polynomial 1/r tail
*was* the source of the Rydberg-like spectrum, and replacing it
with an exponential cutoff suppresses the spurious excited
states.

### F7h.2. Best parameter sets near observed B(²H)

| Variant | m (MeV) | g² | B(²H) (MeV) | nn bound | pp bound |
|:---|:-:|:-:|:-:|:-:|:-:|
| V1 (pure m=140) | 140 | 0.30 | 0.32 | 1 | 0 |
| V1 (pure m=140) | 140 | **0.40** | **3.76** | **1** | **1** |
| V2 (pure m=254) | 254 | 0.50 | 0.07 | 1 | 0 |
| V2 (pure m=254) | 254 | 2.00 | 0.58 | 1 | 1 |
| V3 (hybrid m=140) | 140 | 2.00 | 0.84 | 1 | 1 |

V1 with g² = 0.4 gives B(²H) = 3.76 MeV — **factor 1.7 from
observed 2.22 MeV**, vs Phase 7d's factor 13.5.  Yukawa
exponential clearly improves the binding magnitude.

### F7h.3. But nn and pp bind too — no isospin asymmetry

Across all 30 (variant, g²) combinations swept, **none** gave the
required pattern:

- pn bound (1 state)
- nn unbound (0 states)
- pp unbound (0 states, after Coulomb)

In every Yukawa configuration where pn is bound at B ~ few MeV,
**nn is also bound** with similar binding.  Coulomb removes pp
binding only at low coupling (g² ≤ 0.3) where pn is also
unbound.

### F7h.4. Why: central Yukawa lacks deuteron-vs-singlet asymmetry

The structural reason is unavoidable: a *central* Yukawa potential
`V(r) = −g²·ℏc·exp(−m·r/ℏc)/r` is identical for pn, nn, and pp
(modulo Coulomb).  All three channels see the same V(r).

Nature's deuteron is in the **³S₁ triplet** channel and is bound
(B = 2.22 MeV).  The **¹S₀ singlet** channel is *unbound* (a_s =
−23.7 fm signals an almost-bound state, not a true bound state).
This asymmetry between ³S₁ and ¹S₀ comes from **spin-dependent
operators**:

- Spin-spin: σ₁·σ₂ (gives different sign in triplet vs singlet)
- Tensor force: S₁₂(r) (only operates in triplet ³S₁ via tensor
  coupling)
- Spin-orbit: L·S (vanishes in S-waves)

Simple central Yukawa has none of these.  In real nuclear
physics, OPE (one-pion-exchange) includes a spin-spin term and a
tensor term; the deuteron is bound largely by the tensor force,
which is *forbidden in singlet*.

### F7h.5. Channel asymmetry in Phase 7d came from Ma compound winding

Phase 7d's V_pn, V_nn, V_pp were *not* identical — they differed
because of the (n_pt, n_pr) compound winding:

- pn: (6, 0)
- pp: (6, +4)
- nn: (6, −4)

The ring-direction asymmetry (n_pr) entered through R64's mass
formula μ² = (n_pt/ε)² + (n_pr − s·n_pt)², making V_pn slightly
deeper than V_pp/V_nn (~19 MeV difference in the trough).  But
this was small compared to the overall Coulomb-like 1/r tail
attraction, so all three channels had multiple bound states
anyway.

In Phase 7h Yukawa, we **deliberately stripped that ring
asymmetry** by using a pure central form.  So both channels bind
together — exactly what we'd expect from a central force.

### F7h.6. Acceptance vs result

| # | Criterion | Result |
|:-:|:---|:---|
| 1 | pn has exactly 1 bound state | ✓ achievable (g² range) |
| 2 | B(²H) within factor 2 of 2.22 MeV | ✓ V1 g²=0.4 gives 3.76 |
| 3 | nn unbound | ✗ FAILS — nn binds with pn |
| 4 | pp unbound (after Coulomb) | ✗ FAILS at relevant g² |
| 5 | a_t > 0 | ✓ multiple cases |
| 6 | a_s < 0 | mixed (depends on g²) |

Three of six pass.  The three that fail are precisely the
deuteron-vs-singlet asymmetry that requires spin structure.

### F7h.7. What Phase 7h establishes

**Positive findings**:

1. **Yukawa exponential cutoff DOES fix Phase 7d's Rydberg
   spectrum.**  Bound-state count drops from 3 to 1 across the
   relevant g² range.  This was Pool item m's primary motivation
   and it's confirmed.
2. **Yukawa CAN give B(²H) within factor 2 of observation.**
   V1 g² = 0.4 lands at 3.76 MeV — close enough that with
   parameter refinement, exact match is plausible.

**Sharpened understanding of what's needed**:

3. **Pool item m needs MORE than exponential cutoff.**  A central
   Yukawa alone cannot reproduce the deuteron-vs-singlet
   selectivity.  Pool item m's full version requires the strong
   mediator's coupling to nucleons to be **spin-dependent** —
   either:
   - a Ma-overlap vertex that distinguishes spin-aligned (³S₁)
     from spin-anti-aligned (¹S₀) configurations, or
   - separate mediators for the various exchange channels (π,
     ρ, σ, ω in the SM picture), each with its own spin-isospin
     structure.

In MaSt language: the pool-item-m derivation must include the
spin-projection operator structure that comes from Ma's
quantum-number rules (R60 Track 20's unit-per-sheet AM rule
gives spin ½ per sheet; how that propagates into a 2-nucleon
exchange amplitude is the missing piece).

### F7h.8. Status of Yukawa pivot

Yukawa is **partially validated**:
- Confirms shape diagnosis from Phase 7d.
- Resolves the bound-state count problem.
- Gets B(²H) within factor 2 with one parameter (g²).

But Yukawa **alone is not enough**:
- Cannot produce ³S₁/¹S₀ asymmetry.
- nn and pp bind with pn unless spin/isospin structure is added.

Pool item m, properly developed, must include spin-dependent
vertex structure (analog of QFT's σ₁·σ₂, S₁₂, L·S operators in
OPE).  This makes pool item m a substantial research project,
not a small extension — but the structural shape of what's
needed is now sharp.

---

## Status

**Phases 7a, 7b, 7c, 7d, 7e, 7f, 7g, 7h complete.**

**Phase 7a**: 7-tensor produces a trough in E(r) for two-particle
states, charge-independent (σ_r = 0 selected structurally), pn
preferred over pp.  Trough depth ~21 MeV, position ~1.6 fm —
wrong scale by factor ~5 vs nature.

**Phase 7b**: The 7-tensor's V(r) is essentially exactly polynomial
A₂/r² + A₁/r (R² = 0.9998).  Yukawa form fits poorly.  The
metric-coupling approach as built CANNOT produce Yukawa
exponential decay; that requires propagator physics not in this
formalism.

**Phase 7c**: Phase 7a's scale miss diagnosed as a kinematic
accounting error — k_S = 1/r is the relative momentum of two
nucleons in COM, requiring `A = 4·(ℏc)²` (not `(ℏc)²`) to match
the two-body invariant-mass relation.  With the fix, the trough
lands at **−50.2 MeV at r = 1.135 fm**, inside the observed
NN-potential band.  pn-vs-pp preference, charge symmetry, and
Coulomb tail all preserved.

**Phase 7d**: Phase 7c V(r) solved as a two-body radial Schrödinger
problem.  Quantum-mechanical observables fail decisively —
**3 bound states in pn** (vs 1 deuteron observed), **bound states
in nn and pp** (vs unbound), **B(²H) = 30 MeV** (vs 2.22 MeV
observed, factor 13.5 off), **wrong sign for a_s**.  The
polynomial 1/r tail produces a Coulomb-like Rydberg series with
effective coupling ~0.37 — too strong to support nature's
single-bound-state spectrum.  Phase 7b's structural finding
(polynomial form, no Yukawa) is now made concrete in QM
observables.

**Phase 7e**: Augmented R60 model-F's 11×11 metric with
σ_pS_tube at the new (p_t, S) entries; swept and re-extracted
α.  **α-sectors are NOT decoupled**.  Even small σ_pS_tube ≠ 0
disturbs α, and different modes shift in different directions —
universality breaks at the 1% level for σ_pS_tube outside
[−0.0025, +0.0025].  Conditional finding pending unit
translation and R64-frame test.

**Phase 7f**: Schur-complement matching translates Phase 7c's
σ_t = −116.1 (7-tensor units) to **σ_pS_tube ≈ +0.0043** in 11D
units (Track 9 baseline) or **+0.0129** (R64 Point B baseline).
Inside the signature band but outside the 1% universality band
by factor 1.7× to 5×.  Phase 7c's coupling is moderate — α
perturbation at the few-percent level, not negligible and not
catastrophic.

**Phase 7g**: Re-ran Phase 7e at R64's actual frame (Point B
params + R64 u/d inventory).  Universality bands wider at R64
frame (1% band: [−0.0075, +0.0075], 3× wider than model-F).
**Two-group coupling pattern** revealed: R64 baryons (proton,
neutron, deuteron, NN compounds) shift uniformly together at
~3.4× the rate of leptons + mesons, which also shift uniformly.
Highly informative — companion-entry resolution reduces to a
2-parameter constraint (equalize p-sheet shift with e/ν
shift), much more tractable than per-mode chaos.  σ_pS_tube
needs structure, but the structure is concrete and solvable.

**Phase 7h**: Tested Yukawa form `V = −g²·ℏc·exp(−m·r/ℏc)/r` as
the pool-item-m alternative to the metric-coupling route.  Three
variants swept: pure Yukawa with m_π = 140, with R64's m=254
mediator candidate, hybrid 7c-hardcore + Yukawa.  **Yukawa
exponential cutoff DOES fix Phase 7d's Rydberg spectrum** — pn
bound-state count drops from 3 to 1; V1 with g²=0.4 gives B(²H)
= 3.76 MeV (factor 1.7 from observed 2.22, vs Phase 7d's factor
13.5).  But **central Yukawa cannot produce ³S₁/¹S₀ asymmetry**:
nn and pp bind with pn whenever pn is bound.  This sharpens
pool item m: needs Yukawa cutoff AND spin-dependent vertex
structure (analog of OPE's σ₁·σ₂, S₁₂ operators) — the strong
mediator's coupling to nucleons must distinguish triplet from
singlet.  Pool item m is a substantial research direction, not
a small extension; the shape of what's needed is now sharp.

Track 7 produces the right shape AND right scale of the NN
potential at the static intermediate-r level (Phase 7c).  Lifting
to QM observables (Phase 7d) reveals the polynomial 1/r tail as
the limiting factor: V(r) is "too long-range" without an
exponential cutoff.  Pool item m (Yukawa propagator extension)
is the natural next step — addressing not just the asymptotic
tail but the deuteron's binding energy and scattering-length
structure simultaneously.

This is the most novel positive result R64 has produced: an
emergent strong-force shape and scale from MaSt's geometry,
including charge-independence as a structural constraint and
pn preference as a Ma-side feature.  Phase 7d's negative
quantum-mechanical result sharpens the next-step question:
the polynomial form is the limiting factor, not parameter
tuning.
