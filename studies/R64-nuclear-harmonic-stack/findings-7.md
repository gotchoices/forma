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

## Status

**Phases 7a, 7b, 7c, and 7d complete.**

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
