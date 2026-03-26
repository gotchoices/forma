# Q85: Energy accumulation in compact modes — toward threshold theory on T²

**Status:** Open — hypothesis catalog  
**Source:** User insight (R36/R33 discussion)  
**Related:** [Q28](Q28-photon-absorption.md) (photon absorption),
[Q31](Q31-discrete-torus-digital-counter.md) (digital counter),
[Q77](Q77-alpha-as-impedance.md) (impedance mismatch),
R33 (ghost selection), R35 (threshold coupling),
[`papers/storage-in-t6.md`](../papers/storage-in-t6.md) (Reiter's threshold theory)

---

## 1. The core question

Reiter's threshold model (`papers/storage-in-t6.md` §3)
proposes that energy absorption is continuous: a mode
accumulates energy gradually until a threshold triggers a
discrete event.  If this is correct and T⁶ is the geometry
of matter, how does sub-threshold energy distribute itself
within a particle's compact dimensions?

This question sits at the intersection of:

- **Pair production**: at exactly 2× the particle's rest
  energy, the particle splits into particle + antiparticle.
  This is the universal ceiling.
- **Threshold theory**: between 1× and 2× rest energy,
  energy accumulates continuously — invisible to quantum
  measurements but physically real.
- **Information storage**: the pattern of accumulated energy
  across modes could encode information (the premise of the
  storage-in-t6 paper).

The ideal answer would explain WHERE the energy goes
(which degrees of freedom hold it), HOW it distributes
(uniformly? geometrically? thermally?), and WHY pair
production occurs at exactly 2×.


## 2. Constraints on any mechanism

Whatever mechanism holds sub-threshold energy must satisfy:

1. **Charge preservation.** Adding energy to an electron
   must not change its charge (−1).  In T⁶, charge depends
   on n₁ (tube winding).  Any excitation must keep n₁ = 1.

2. **Pair production at 2m.** The total internal capacity
   must equal exactly m (the rest mass) of additional
   energy, so that fundamental + capacity = 2m.

3. **No lighter charged particles.** The electron is the
   lightest charged particle.  No sub-electron charged
   mode can exist as a stable state.

4. **Invisible to standard measurement.** Sub-threshold
   energy must not produce detectable signatures in
   standard quantum experiments (Reiter's premise).

5. **Spin preservation.** The electron is spin-½.  Energy
   accumulation must not change the spin statistics.


## 3. The mode spectrum (what the torus gives us)

On the electron T², the energy of mode (1, n₂) is:

    E(1, n₂) / m_e = √[ (1/r² + n₂²) / (1/r² + 4) ]

where r = L₁/L₂ (aspect ratio, currently free).

### Upward ladder: (1, n₂) for n₂ > 2

These are charge-preserving excitations with HIGHER energy
than the electron.  The energy gaps are roughly constant
at ~½ m_e for moderate r:

| Mode | r = 1 | r = 5 | r → ∞ |
|------|-------|-------|--------|
| (1,2) electron | 1.000 | 1.000 | 1.000 |
| (1,3) | 1.414 | 1.496 | 1.500 |
| (1,4) | 1.844 | 1.993 | 2.000 |

For moderate-to-large r, only 1–2 modes fit in [m_e, 2m_e).

### Downward ladder: (1, n₂) for n₂ < 2

These have LOWER energy than the electron — same charge,
lighter mass:

| Mode | r = 1 | r = 5 | Spin |
|------|-------|-------|------|
| (1,0) | 0.447 | 0.100 | undefined |
| (1,1) | 0.632 | 0.507 | 1 (boson) |

These are sub-electron charged ghosts — a major tension
(R33 Track 3).  Their non-observation demands either a
suppression mechanism or a fundamental reason they don't
exist.  The spin-statistics argument helps: (1,1) has
spin 1 (n₁/n₂ = 1), not ½, so it's a different species.
But it should still be observable if it exists.

### Proportional harmonics: (k, 2k)

E(k, 2k) = k × m_e exactly (shear cancels).  These have
charge −k.  The first proportional harmonic (2, 4) sits
at exactly the pair-production threshold with charge −2.

### Key limitation

Standard torus modes have INCREASING energy with harmonic
number.  This gives a coarse ladder with roughly uniform
gaps — not the finely graduated spectrum that threshold
theory seems to require.


## 4. Hypothesis catalog

### A. Discrete mode transitions (standard QM on T²)

Energy goes into the charge-preserving ladder (1, n₂).
Transitions are discrete jumps.  Between levels, energy
can only go to R³ kinetic energy (the particle moves
faster).  No sub-threshold storage.

- **Supports:** known physics, pair production at 2m
- **Problems:** only 1–2 levels in [m_e, 2m_e); no
  sub-threshold storage; no gradual filling; contradicts
  threshold theory premise
- **Prediction:** excited electrons at specific masses
  determined by r; detection would pin r (§7)


### B. Continuous amplitude within a mode (Reiter)

The (1, 2) traveling wave can hold energy between 0 and
E(1,3) − m_e without triggering a transition.  Energy
fills the mode continuously.  At the threshold, a discrete
event fires.

- **Supports:** Reiter's experiments; storage-in-t6 paper;
  explains why sub-threshold energy is invisible
- **Problems:** traveling waves on a torus have uniform
  |ψ|² — unclear what "increased amplitude" means for a
  mode with fixed winding numbers; the current T⁶ model
  is linear, so mode energy = rest mass (fixed)
- **What's needed:** a nonlinear extension of the T⁶ wave
  equation where mode amplitude is a dynamical variable,
  not fixed by the boundary conditions alone


### C. Geometric (binary) energy partition

The energy capacity between m_e and 2m_e subdivides
geometrically:

    Capacity: ½ m_e + ¼ m_e + ⅛ m_e + ... = m_e

The sum equals m_e exactly → total = 2m_e = pair
production.  This is the ONLY geometric ratio where the
series sums to exactly 2× the first term.

Each "level" is a bit: total information = N bits from
N levels.  The energy of level k is m_e / 2^k.  This
creates a binary register encoding a number between
m_e and 2m_e.

- **Supports:** pair production ceiling emerges naturally;
  connects to Q31 (digital counter); binary subdivision is
  maximally information-efficient
- **Problems:** no known torus mechanism produces this
  spectrum; mode energies on T² INCREASE (not decrease)
  with harmonic number; would require a fundamentally
  different kind of excitation
- **What's needed:** nonlinear mode coupling where
  exciting a mode modifies the geometry, making subsequent
  excitations cost less energy (backreaction / self-
  consistent deformation)


### D. Multipole coupling suppression

The coupling between an external photon and successive
internal modes decreases geometrically.  Higher multipole
transitions (E1, E2, E3, ...) are suppressed by powers
of (system size / wavelength)²:

    Coupling to mode k: ~ α^k

The MODE energies still increase, but the TRANSITION
PROBABILITY decreases geometrically.  The effective energy
deposited into mode k scales as E_k × α^k, giving a
rapidly converging series.

- **Supports:** standard physics (multipole expansion);
  naturally produces geometric suppression; the ratio α
  appears from the compact/spatial interface
- **Problems:** this is about coupling, not about energy
  levels; it doesn't change where the energy SITS, only
  how easily it gets there; doesn't explain sub-threshold
  continuous filling
- **Connection:** if transitions to higher modes are
  suppressed by α^k, then in practice most energy stays
  in the fundamental and the first excitation — the
  system ACTS like it has a geometric hierarchy even if
  the mode energies don't follow one


### E. Thermal occupation (Boltzmann weighting)

If the particle's internal modes are in thermal
equilibrium at effective temperature T, the occupation
probability of the n-th excitation is:

    P(n) ∝ exp(−E_n / kT)

For a harmonic oscillator with ℏω/kT = ln 2, this gives
P(n) = 1/2^(n+1) — exactly the geometric series from
Hypothesis C.  The energy distribution is 1/2, 1/4, 1/8,
... of the total, not because the LEVELS have those
energies, but because the OCCUPATION PROBABILITY follows
that pattern.

- **Supports:** well-understood statistical mechanics;
  produces the desired geometric distribution; connects
  to condensed matter (phonon occupation)
- **Problems:** requires the particle to have an effective
  temperature, which has no current meaning in the T⁶
  model; thermal equilibrium implies fluctuations, which
  might destroy stored information
- **What's needed:** a definition of "internal temperature"
  for a compact-dimension mode; possibly related to the
  particle's interaction with the vacuum or with other
  particles


### F. Phase advance as energy storage

The (1, 2) traveling wave circulates the torus at speed c.
In one natural period T = h/(m_e c²), it completes one
full trace of the (1, 2) path: 1× tube, 2× ring.

If energy accumulates (Reiter), the frequency increases:
ω = E/ℏ.  The wave circulates FASTER on the same cavity.
The topology hasn't changed — still (1, 2) per spatial
cycle — but MORE cycles happen per unit time.  The excess
phase (beyond the natural 2π per period) IS the stored
energy.  Energy is encoded as phase advance rate.

**The spin-phase catastrophe at 2m.**  Spin-½ means the
wave function picks up a minus sign after one ring cycle
(tube phase advances by π, not 2π).  Two ring cycles (4π
total) are needed to return to +1.  This is the defining
property of a fermion.

At E = 2m_e the frequency doubles.  In one natural period
the wave now completes TWO spatial cycles.  The tube phase
advances by 2π (not π).  The wave function returns to +1
after one period — no sign flip.  Dynamically, the wave
behaves like a **boson**, even though the topology is still
fermionic (winding ratio 1/2).

This is a fundamental contradiction:
- Topologically: fermion (winding ratio 1/2)
- Dynamically: boson (phase returns to +1 per period)

The system cannot sustain this mismatch.  Resolution:
**split into two fermions**, each at E = m_e, restoring
the one-to-one correspondence between phase evolution and
topological spin.  This makes pair production a
**topological phase-matching failure**, not just a
kinematic threshold.

**Between m_e and 2m_e.**  At E = 1.5 m_e, the frequency
is 1.5ω₀.  After one natural period, the wave has
completed 1.5 spatial cycles.  The tube phase has advanced
by 1.5π.  The wave function carries a phase factor
e^{i·1.5π} — neither +1 (boson) nor −1 (fermion).  It is
in a fractional phase state.

This fractional phase is the sub-threshold energy storage
channel.  Each increment of energy advances the phase
further.  The total phase capacity is one full extra cycle
(from 2π to 4π), corresponding to energy from m_e to 2m_e.
The phase is a continuous, analog variable — matching
Reiter's continuous-filling picture.

**Phase as information.**  For a single isolated particle,
absolute phase is unobservable (U(1) gauge invariance).
But RELATIVE phase — between two particles, or between a
particle and a coherent background — is physical and
measurable (interference).  Sub-threshold phase advance
could encode information readable only by a system that
shares a phase reference.  This connects to:
- Q31 (digital counter): phase subdivisions as bits
- Storage-in-t6 paper: cross-sheet phase as the storage
  channel (electron phase relative to neutrino-sheet mode)
- Entanglement (Q82): shared phase reference between
  particles on the same T⁶

- **Supports:** energy and phase are conjugate variables
  (ΔE·Δt ≥ ℏ/2); phase advance is a natural consequence
  of energy accumulation; the 2m ceiling emerges from the
  spin-phase catastrophe; provides a continuous (analog)
  storage channel; pair production gets a geometric
  explanation
- **Problems:** the current T⁶ model uses fixed-frequency
  modes — no mechanism for continuous frequency change on
  a fixed torus; requires Reiter premise or backreaction
  (Hypothesis G); the "fractional spin" state between m
  and 2m has no standard QM interpretation
- **What's needed:** compute the phase evolution of a (1,2)
  mode with energy E ≠ m_e on a fixed torus; determine
  whether a "loaded" mode with excess phase is a valid
  solution of the wave equation or requires nonlinear
  extension


### G. Nonlinear anharmonicity (backreaction)

The T⁶ model uses a linear wave equation on a fixed
background.  If the wave energy backreacts on the torus
geometry (Einstein's equations: energy curves spacetime),
the mode spectrum becomes energy-dependent.  A mode with
more energy sits on a slightly different torus than a mode
with less energy.

In an anharmonic oscillator, the energy levels are NOT
equally spaced.  Depending on the sign of the anharmonicity:
- **Positive (stiffening):** gaps increase → harder to
  excite successive levels
- **Negative (softening):** gaps decrease → easier to
  excite successive levels

If the T² geometry softens under energy loading, the
harmonic ladder could have DECREASING gaps — each
additional excitation costs less.  In the extreme case,
this could produce the geometric series of Hypothesis C.

- **Supports:** general relativity requires backreaction;
  any real physical system has anharmonicity; softening
  is plausible if energy loading expands the torus
  slightly (larger cavity → lower frequencies)
- **Problems:** not computed; the backreaction might be
  tiny (of order α or smaller); could go either direction
  (stiffening or softening)
- **What's needed:** solve Einstein's equations for a T²
  with finite mode energy and compute the corrected mode
  spectrum.  This would be a new study beyond R33.


### H. Wavepacket breathing

If the electron is not a pure (1, 2) eigenstate but a
narrow wavepacket on T² (as in the original WvM picture),
it has a spatial extent σ.  Adding energy could change σ
(the packet broadens or narrows) without changing the
winding numbers.

A broader packet has more overlap with higher modes.  A
narrower packet has less uncertainty in position but more
in momentum.  The "breathing" of σ is a continuous degree
of freedom that could hold analog energy.

- **Supports:** connects to the original WvM localization
  picture; wavepacket width is a continuous parameter;
  R15 explored σ as the parameter controlling α
- **Problems:** in KK theory, the electron is a
  delocalized mode (no wavepacket); the relationship
  between σ and energy is not monotonic
- **Connection:** if α = f(σ) (R15), then changing σ
  changes α — which changes the particle's coupling to
  everything.  A particle "loaded" with energy might have
  a slightly different α than an unloaded one.


## 5. Pair production as capacity saturation

Several hypotheses converge on the same structural result:
**the total internal capacity of a particle equals its
rest mass, so the maximum total energy is 2m.**

- Hypothesis C derives this from the geometric series:
  Σ m/2^k = m
- Hypothesis F derives it from the spin-phase catastrophe:
  at 2× frequency, dynamical phase evolution completes an
  extra full cycle per period, breaking the topological
  spin identity
- Standard QM derives it from pair creation kinematics:
  need ≥ 2m for particle + antiparticle
- The proportional harmonic (2, 4) has energy exactly 2m_e
  with charge −2 — a structural coincidence (§3)

If these are the same phenomenon viewed from different
angles, pair production is not just a kinematic threshold
but a CAPACITY limit: the compact mode is "full" and must
create a new mode to hold more energy.  Hypothesis F gives
the most specific geometric mechanism: the phase advance
laps the topological periodicity, destroying the fermion
identity.


## 6. The spin-statistics filter

The WvM derivation of spin-½ is specific to the (1, 2)
winding: one tube orbit per two ring orbits gives angular
momentum ℏ × (n₁/n₂) = ℏ/2.  Applying the same logic
to every mode:

| Mode | Spin = n₁/n₂ | Valid? |
|------|---------------|--------|
| (1, 0) | undefined | No |
| (1, 1) | 1 | Yes — spin-1 boson |
| **(1, 2)** | **1/2** | **Yes — spin-½ fermion** |
| (1, 3) | 1/3 | No — fractional |
| (1, 4) | 1/4 | No — fractional |
| (1, n₂) for n₂ > 2 | 1/n₂ | No — fractional |

The spin-statistics theorem demands integer or half-integer
spin.  This eliminates almost every mode:

- **Upward ladder killed:** (1,3), (1,4), (1,5)... all
  have fractional spin → FORBIDDEN.
- **Downward ladder killed:** (1,0) is undefined; (1,−1)
  is spin −1 (same magnitude as spin 1, valid boson).
- **Only survivors with n₁ = 1:** the electron (1,2) at
  spin ½, and the boson (1,1) at spin 1.

The electron is the UNIQUE spin-½ charged mode on its
sheet.  No lighter spin-½ particle with charge −1 exists.

The only spin-½ modes on the entire electron sheet are
the proportional harmonics (k, 2k), which have charge −k
and energy k × m_e.  These change charge — they're pair-
production channels, not excitations.

**Critical caveat:** R27/R28 used a simplified spin rule
(spin ½ per active sheet, regardless of n₂).  If that is
correct, the filter doesn't work and ghosts return.
Whether spin = n₁/n₂ (WvM geometric) or spin = ½ per
sheet (KK field-theoretic) is one of the deepest
unresolved questions in the model.  R33 could resolve
this: if Track 1 (charge integral) also selects n₂ = 2,
it and the spin filter tell the same story.

**Implication for energy storage:** if the spin filter
holds, the electron has NO discrete internal excitation
ladder.  All sub-threshold energy storage must be
continuous — the phase-advance mechanism (Hypothesis F)
becomes the ONLY channel.

**Non-orientable alternatives ruled out.** R30 Track 3
investigated the Klein bottle (T² with twisted edge
identification).  It kills charge (Gauss's law breaks;
gauge becomes Z₂, not U(1)) and kills spin-½ (no odd
tube windings on closed geodesics).  Findings F15–F17
confirm T² is the unique compact orientable 2D surface
with the required winding structure.


## 7. Continuous energy and R³ momentum

If Reiter's continuous filling is correct and the electron
accumulates sub-threshold energy, the standard picture
says the only place for extra energy is R³ kinetic energy
(momentum).  But what does this actually mean?

**What changes physically:**
- The electron moves through space.  Its de Broglie
  wavelength shortens (λ = h/p).
- Its T⁶ mode (1, 2) is unchanged — same charge, same
  rest mass, same spin.
- The total energy is E = √(m²c⁴ + p²c²).
- The wave function gains an R³ plane wave factor: e^{ikx}

**Where is the energy stored?**
- In the SPATIAL wavelength of the particle.  A moving
  electron is a shorter-wavelength wave in R³ while its
  T⁶ pattern is unchanged.
- The energy is "stored" in the momentum degree of freedom
  — which is continuous, not quantized (in free space).
- On the torus, nothing has changed.  The energy is
  entirely in R³.

**The tension with threshold theory:**
Reiter proposes that energy enters the MODE, not just R³.
A mode that accumulates sub-threshold energy has more
internal energy than m_e but hasn't yet transitioned.
Standard QM says this is impossible — the mode energy is
fixed by the geometry.  But:

- **Hypothesis F (phase advance):** extra energy shows up
  as faster phase evolution of the (1, 2) mode itself.
  The T⁶ pattern is still (1, 2), but ω > ω₀.  This is
  energy stored IN the compact mode, not in R³ momentum.
  The distinction: a phase-loaded electron at rest
  (p = 0) has E > m_e but zero R³ momentum.

- **Hypothesis G (backreaction):** extra energy slightly
  deforms the torus (L₁, L₂ shift), changing the mode
  frequency.  The energy is stored in the geometry.

- **Standard QM:** extra energy can only be R³ kinetic
  energy.  An electron with E > m_e is always moving.
  An electron at rest always has E = m_e exactly.

Distinguishing these experimentally: can an electron at
rest have more energy than m_e?  Standard QM says no.
Threshold theory says yes (the excess is invisible to
standard detectors).  This is the core disagreement.


## 8. Neutrino sheet status and the dense ladder

The neutrino sheet aspect ratio r_ν is NOT pinned.

- R26 F63: r_ν is free with a one-sided lower bound
  r_ν ≥ ~3.2 from cosmological Σm_ν ≤ 120 meV.
- The Δm² ratio (33.6) is r-independent — it doesn't
  constrain r_ν at all.
- R27: r_ν is invisible at MeV scale (no hadronic
  sensitivity).
- Default r_ν = 5.0 in code is conventional, not physical.

### Why the neutrino sheet is the natural storage medium

On the neutrino T², the energy of mode (n₃, n₄) is

    E(n₃, n₄) = E₀ √(n₃²/r_ν² + n₄²)

For large r_ν, modes with different n₃ but the same n₄
are closely spaced — spacing ∝ 1/r_ν.  The number of
modes in the window [m_ν, 2m_ν] is:

| r_ν | Approx. modes in [m_ν, 2m_ν] |
|------|-------------------------------|
| 5    | ~20                           |
| 50   | ~200                          |
| 500  | ~2,000                        |
| 5000 | ~20,000                       |

(Estimate: for fixed n₄ = 2 or 3, n₃ ranges up to
~3.5 r_ν; additional modes from n₄ = 1 with large n₃.)

The electron sheet (r_e ≈ 6.6) has at most 1–2 modes in
[m_e, 2m_e].  The neutrino sheet with even moderate r_ν
has a DENSE mode spectrum — arbitrarily dense if r_ν is
large.  This is exactly the fine-grained ladder that
threshold theory and information storage require.

**The spin filter caveat (§6) applies to free particles.**
Sub-threshold excitations within an existing neutrino are
NOT creating new free particles — they are internal
perturbations of the (1, 2) mode.  The spin-statistics
theorem constrains asymptotic scattering states, not the
internal configuration of a single particle.  If Reiter's
continuous filling is correct, these dense modes are
available as internal degrees of freedom regardless of
their free-particle spin assignment.

**Contrast with electron sheet:** the electron sheet has
few modes and large gaps.  If the spin filter holds, it
has NO discrete internal excitations at all.  The only
storage mechanism is phase advance (Hypothesis F).  The
neutrino sheet, by contrast, has a rich internal structure
— potentially thousands of closely spaced levels between
m_ν and 2m_ν.  This is consistent with the storage-in-t6
paper's claim that the neutrino sheet is the primary
information storage medium.

### Where the energy really goes (threshold theory)

Standard QM says: all energy beyond the rest mass goes
into R³ momentum.  A faster particle has shorter de
Broglie wavelength (λ = h/p).  The T⁶ mode is unchanged.
The energy is stored in the spatial wavelength, not the
compact dimensions.

Threshold theory rejects this for sub-threshold
increments.  It proposes energy enters the MODE ITSELF.
On the neutrino sheet this makes more sense than on the
electron sheet, because:

1. Dense modes exist within [m_ν, 2m_ν] — energy has
   somewhere to go internally
2. Mode transitions can be very small (δE ∝ 1/r_ν) — no
   need for large discrete jumps
3. The transitions change n₃ (tube winding on the long
   axis) while keeping n₄ = 2 — the ring structure that
   determines spin is preserved
4. From outside (R³), the neutrino's mass changes by a
   tiny amount — undetectable at current precision

What changes physically when energy enters: the neutrino
shifts from mode (1, 2) to a nearby mode (k, 2) with
k slightly different.  The rest mass shifts by ~m_ν/r_ν
per step.  Externally, the neutrino moves slightly slower
or faster (momentum adjusts to conserve total energy).
The information is encoded in WHICH mode (k, 2) the
neutrino occupies — this is a discrete register with
~r_ν bits of capacity.

**The counting ladder on the neutrino sheet:**

If we label accessible modes by their n₃ value (fixing
n₄ = 2), the modes are:

    n₃ = 1 (fundamental), 2, 3, 4, ... up to ~3.5 r_ν

Each is a distinct "address."  The neutrino can be in any
one of them.  The number of addresses scales with r_ν.
With r_ν ~ 1000, we get ~3500 discrete states.  At
12 bits per 4096 states, this is ~12 bits per neutrino.

The energy spacing is NOT uniform — it varies as modes
at different n₃ have energies that go roughly as n₃/r_ν
(for large r_ν, approximately linear in n₃).  But the
elastic torus idea (§8a below) could make the spacing
energy-dependent.


### 8a. The elastic torus — r as a dynamical variable

**Hypothesis I: Elastic deformation under energy loading.**

The aspect ratio r is currently treated as a fixed
geometric constant.  But if the torus has finite stiffness
(as any physical object must), energy stored in a mode
exerts radiation pressure on the walls.  The torus
deforms: r becomes a function of the stored energy.

    r(E) = r₀ + κ(E − m₀)

where κ is the "elastic compliance" of the torus and m₀
is the rest energy at unloaded r₀.

This creates a feedback loop:

1. Start at r₀.  Mode energy = m₀ = E(1, 2, r₀).
2. Add energy δE.  Torus stretches to r₁ = r₀ + κδE.
3. On the new torus, modes are more closely spaced
   (spacing ∝ 1/r₁).
4. The NEXT energy increment δE₂ required to reach the
   next mode is SMALLER: δE₂ < δE₁.
5. That smaller increment stretches the torus less,
   but the torus is already larger, so modes are already
   denser.

If the compliance κ and the mode density 1/r conspire
correctly, the increments follow a geometric series:

    δE_k = δE₁ / 2^(k-1)

    Total capacity = Σ δE_k = 2 δE₁ = m₀

This recovers Hypothesis C (binary partition) from
PHYSICS rather than numerology.  The geometric ratio
emerges from the nonlinear coupling between energy and
geometry.

**Why this works better on the neutrino sheet:**

- Electron sheet: r_e ≈ 6.6.  Few modes in [m_e, 2m_e].
  Even with elastic deformation, the mode density is too
  low to create a fine ladder.  The torus would need to
  stretch from r = 6.6 to r >> 100 to get dense modes —
  a 15× deformation, implying zero stiffness.

- Neutrino sheet: r_ν ≥ 3.2, possibly much larger.  If
  r_ν ~ 100–1000, the mode ladder is already dense at
  zero deformation.  A small elastic stretch (δr/r ~ 1%)
  shifts which modes are accessible, creating a smooth,
  energy-dependent ladder.  The torus doesn't need to
  deform dramatically — it just needs to breathe.

**Running the ratio curve:**

As energy increases from m_ν to 2m_ν, the aspect ratio
traces a curve r(E).  If we plot r vs. E, the trajectory
encodes the full energy-storage capacity:

    r(m_ν) = r₀           (unloaded)
    r(2m_ν) = r₀ + κm_ν   (fully loaded, pair threshold)

Along this curve, the mode density, level spacing, and
effective "bit depth" all change.  The curve IS the
counting ladder — each point on it corresponds to a
different internal state.

**Is this computable?**

Yes, in multiple ways:

1. **Radiation pressure on a T² cavity:** a standing wave
   (n₃, n₄) on a rectangular T² with side lengths L₃, L₄
   exerts pressure P₃ = −∂E/∂L₃ and P₄ = −∂E/∂L₄.
   If the torus has elastic modulus K (energy per unit
   strain), the equilibrium deformation is:

       δL₃/L₃ = P₃ / K

   This is a 1D minimization for each energy level.

2. **Self-consistent mode spectrum:** for a given total
   energy E_total, find r(E_total) such that the mode
   occupying the torus has energy E_total on a torus with
   aspect ratio r(E_total).  This is a fixed-point problem.

3. **The stiffness K is the unknown.**  In the current T⁶
   model, there is no moduli potential — the torus shape
   is a flat direction.  K = 0 means infinite compliance:
   any energy addition causes unbounded stretching.  This
   is unphysical and suggests a moduli potential MUST exist
   (see R31: "deriving α requires a dynamics/moduli
   potential not yet in the model").

   If K exists but is very small (soft moduli), the
   elastic response is large and the ladder is dense.
   If K is very large (stiff moduli), the torus barely
   moves and the ladder is the standard fixed-torus one.

4. **Parameterize and bracket:** treat K as a free
   parameter.  For each K, compute the full r(E) curve,
   the mode density, the level spacing, and the total
   number of "bits" in [m_ν, 2m_ν].  Map K → bit count.
   The storage-in-t6 paper requires ~10–20 bits per
   neutrino; this constrains K.

**Connection to the moduli problem:**

String theory has the same issue — moduli (shape
parameters of compact dimensions) are massless scalars
with no potential.  Flux compactification and other
mechanisms stabilize them.  The T⁶ model needs an
analogous stabilization.  The elastic torus hypothesis
proposes that stabilization is SOFT — the moduli have a
potential, but it's shallow enough that mode energy can
shift the equilibrium appreciably.  This turns a bug
(free parameter r) into a feature (dynamical storage).


## 9. Pinning the aspect ratio r

The charge-preserving ladder makes a testable prediction:
heavier versions of the electron (charge −1, higher mass)
should exist at specific energies determined by r.

From two measured masses m_e and m*(1, n₂):

    r² = [ n₂² − 4(m*/m_e)² ] / [ (m*/m_e)² − 1 ]

Detecting the (1, 3) excitation — a charge −1 particle at
0.66–0.77 MeV (depending on r) — would:
- Pin r_e with zero remaining freedom
- Make all higher modes parameter-free predictions
- Be a smoking-gun test of the T⁶ model

No such particle has been identified.  The muon (charge −1,
mass 207 m_e) would require n₂ ~ 414 — not a "next level."


## 10. What to compute next

The hypotheses above suggest specific computations:

1. **R33 Track 1 (charge integral):** does the R19 formula
   suppress modes with n₂ ≠ 2?  If so, the downward ladder
   is killed and the electron is protected.  HIGHEST
   PRIORITY — resolves the ghost tension.

2. **R33 Track 6 (spin-statistics derivation):** derive
   spin for general (n₁, n₂) from the WvM confined-photon
   picture.  Is spin = n₁/n₂, or is it ½ per active sheet?
   Compute the angular momentum of the EM field for modes
   (1,1), (1,2), (1,3) on a sheared T² and determine the
   effective spin quantum number.  If spin = n₁/n₂, most
   ghost modes are eliminated by spin-statistics alone.

3. **Neutrino ladder density (new computation):** count the
   exact number of modes in [m_ν, 2m_ν] as a function of
   r_ν.  For each mode, record (n₃, n₄), energy, and
   WvM spin.  Plot mode density vs r_ν.  Determine the
   minimum r_ν needed for N bits of storage capacity.

4. **Elastic torus radiation pressure (Hypothesis I):**
   compute the radiation pressure exerted by a (1, 2)
   standing wave on a T² with given aspect ratio r.
   For a parameterized stiffness K, solve for the
   equilibrium deformation r(E) as energy increases from
   m₀ to 2m₀.  Does the level spacing decrease
   geometrically?  What K gives the binary series?
   Apply to the neutrino sheet.

5. **Phase evolution on fixed T² (Hypothesis F test):**
   can the (1, 2) mode carry energy E > m_e on a fixed
   torus?  Solve the wave equation with a source term or
   initial amplitude > 1 quantum.  Does the solution
   remain in the (1, 2) sector or leak into other modes?

6. **Anharmonic correction (Hypothesis G):** solve for
   the T² mode spectrum including first-order backreaction
   from the mode's own energy.  Does the spectrum soften
   (gaps decrease) or stiffen (gaps increase)?  Related to
   Hypothesis I but without the elastic degree of freedom —
   tests whether backreaction alone modifies the ladder.


## 11. Connection to threshold theory and storage

Two sheets, two storage mechanisms:

**Neutrino sheet (primary storage medium):**
- Dense discrete ladder: ~r_ν modes in [m_ν, 2m_ν]
- r_ν is free and possibly large → thousands of levels
- Elastic deformation (Hypothesis I) could make the
  spacing energy-dependent, producing a natural binary
  partition (Hypothesis C)
- Information encoded in which mode (k, 2) is occupied
- Capacity: ~log₂(3.5 r_ν) bits per neutrino
- This is the storage-in-t6 paper's channel

**Electron sheet (limited storage):**
- Sparse ladder: 1–2 modes in [m_e, 2m_e] at most
- Spin filter (§6) likely kills all discrete excitations
- Phase advance (Hypothesis F) is the only remaining
  channel — continuous, analog, single variable
- Capacity: 1 continuous analog variable (phase angle)
- Pair production at 2m_e = phase-matching catastrophe

The neutrino sheet is the NATURAL home for threshold
theory's counting ladder because:
1. r_ν is unconstrained (can be large → dense ladder)
2. Neutrinos are electrically neutral (no EM radiation
   losses during mode transitions)
3. Neutrino masses are tiny (meV) → the [m_ν, 2m_ν]
   window is in the sub-eV regime, matching biological
   energy scales
4. The spin filter is less restrictive for internal
   excitations than for free particles (§8)
5. The elastic torus (§8a) naturally produces decreasing
   energy steps, matching the binary-partition ideal

The electron sheet's role is different: it provides the
CHARGE CARRIER.  The electron interacts electromagnetically
(through R³), while the neutrino sheet stores the pattern.
A cross-sheet coupling (σ_eν) links them: the electron
"reads" the neutrino sheet's state.  This two-layer
architecture — one sheet for interaction, one for storage
— is the structural prediction of the T⁶ model for
biological information processing.


## 12. Superposition encoding and the frequency chord

### A single mode is a pure tone

Each eigenmode (n₃, n₄) on the neutrino T² has one
temporal frequency: ω = E(n₃, n₄)/ℏ.  But it has TWO
spatial frequency components — one per torus axis:

- Along L₃ (tube): k₃ = 2π n₃/L₃
- Along L₄ (ring): k₄ = 2π n₄/L₄

The ratio n₃/n₄ is the mode's spatial fingerprint.
Mode (1, 2) oscillates once along the tube per two ring
circuits.  Mode (3, 2) oscillates three times per two
ring circuits.  Same ring structure, different tube
pattern, slightly different energy.

### A superposition is a chord

A neutrino need not occupy a single eigenmode.  It can
be in a superposition:

    ψ = c₁|1,2⟩ + c₂|2,2⟩ + c₃|3,2⟩ + ...

Each coefficient c_k = |c_k| × e^{iφ_k} has an amplitude
and a phase.  The set {c_k} defines a waveform on the
torus — a 2D interference pattern — that changes in time
because each component oscillates at a different frequency.

This is exactly a chord:
- Each mode is a note (pure frequency)
- The amplitudes {|c_k|} set the loudness of each note
- The phases {φ_k} set the timing
- Different chords = different stored information

The beat frequencies between adjacent modes are:

    f_beat(k, k+1) = |ω(k+1, 2) − ω(k, 2)| / 2π
                   ≈ m_ν c² × (2k+1) / (8π ℏ r_ν²)

For large r_ν these are very small — the chord evolves
slowly.  The superposition doesn't rapidly dephase; it's
a slowly rotating pattern on the torus.


## 13. Storage capacity estimates

### Total modes available

All modes (n₃, n₄) with energy in [m_ν, 2m_ν] satisfy
4 ≤ n₃²/r_ν² + n₄² ≤ 16 (for large r_ν).  The lattice
point count in this annulus scales as:

    N_total ≈ 12π r_ν ≈ 38 r_ν

(12π = area of the annulus in scaled coordinates.)
This is ~10× more than the (k, 2)-only estimate because
modes with n₄ = 1 and n₄ = 3 also fall in the window.

### Framework A: Single-mode (which note is playing)

The simplest encoding: the neutrino occupies exactly one
mode.  The stored value is the mode index.

    Capacity = log₂(N_total) bits

| r_ν   | N modes in [m_ν, 2m_ν] | Capacity       |
|--------|------------------------|----------------|
| 10     | ~380                   | 8.6 bits       |
| 100    | ~3,800                 | 11.9 bits      |
| 1,000  | ~38,000                | 15.2 bits      |
| 10,000 | ~380,000               | 18.5 bits      |
| 10⁶    | ~3.8 × 10⁷            | 25.2 bits      |

Requirements: the mode must be stable (no spontaneous
decay).  No coherence needed — this is classical storage.
Very robust, but only ~2 bytes per neutrino even at large
r_ν.

### Framework B: Superposition with finite precision (Reiter)

Under threshold theory, the full superposition state is
physically real and persistent.  The state is a point in
a (2N − 2)-dimensional real space (N complex amplitudes
minus normalization and global phase).  If each real
parameter is set to p bits of precision:

    Capacity = (2N − 2) × p bits

| r_ν   | N modes | p = 8 bits   | p = 16 bits  | p = 32 bits  |
|--------|---------|--------------|--------------|--------------|
| 100    | 3,800   | 60 kbits     | 120 kbits    | 240 kbits    |
|        |         | **7.5 KB**   | **15 KB**    | **30 KB**    |
| 1,000  | 38,000  | 600 kbits    | 1.2 Mbits    | 2.4 Mbits    |
|        |         | **75 KB**    | **150 KB**   | **300 KB**   |
| 10,000 | 380,000 | 6 Mbits      | 12 Mbits     | 24 Mbits     |
|        |         | **750 KB**   | **1.5 MB**   | **3 MB**     |
| 10⁶    | 3.8×10⁷ | 600 Mbits    | 1.2 Gbits    | 2.4 Gbits    |
|        |         | **75 MB**    | **150 MB**   | **300 MB**   |

The precision p is set by whatever physical mechanism
reads and writes the state.  If the Reiter channel
operates at the natural energy resolution of the mode
spacing (δE ~ m_ν/r_ν), then p is limited by the
signal-to-noise of the read/write process, not by
quantum uncertainty.

### Framework C: Standard quantum (Holevo bound)

Under standard QM, the maximum classical information
extractable from an N-dimensional quantum state by
a single measurement is:

    Capacity_readable = log₂(N) bits

This is the Holevo bound.  A superposition of 38,000
modes still yields at most ~15 bits of readable output
per measurement.  The state space is huge, but quantum
measurement collapses it.

**The gap:** Framework B gives 75 KB where Framework C
gives 15 bits.  The entire premise of threshold theory
is that Framework B is physically correct — that the
superposition state carries persistent, readable
information through a channel that standard QM doesn't
recognize.  If Framework C is correct, the neutrino sheet
is a 2-byte register at best.

### One cell = one coherent domain

The neutrino T² ring circumference is L₄ ≈ 42 μm (R26).
A typical animal cell is 10–100 μm in diameter.  The
Compton wavelength of the lightest neutrino (λ_C = 2πL₄
≈ 42 μm) matches the cell scale.

Every atom in a cell has the same T⁶ geometry (same L₃,
L₄, r_ν).  Because all atoms sit within one Compton
wavelength of each other in R³, their neutrino-sheet
wavefunctions overlap completely.  They cannot be resolved
as separate locations on the neutrino T².  They all
contribute to a SINGLE collective neutrino-sheet state.

**One cell = one neutrino storage domain.**

This is not an arbitrary assumption — it follows directly
from the neutrino T² scale (R26) and the definition of
spatial resolution on the compact dimensions.

### Collective occupation: many atoms, one state

A cell contains ~10¹⁴ atoms.  Each atom contributes one
"quantum" to the neutrino-sheet occupation.  These 10¹⁴
quanta are distributed across the ~N available modes.  The
PATTERN of distribution is the stored information.

With M = 10¹⁴ quanta in N = 38,000 modes (r_ν = 1000):

Average occupation per mode: M/N ≈ 2.6 × 10⁹

The number of distinguishable distributions (information
capacity) depends on the precision with which occupancies
can be distinguished.  The large number of atoms provides
natural statistical precision — the occupation of each
mode can be specified to ~√M/N ≈ 51,000 distinguishable
levels (Poisson statistics), giving:

    Bits per mode ≈ log₂(√(M/N)) ≈ log₂(51,000) ≈ 15.6
    Total capacity ≈ N × 15.6 ≈ 38,000 × 15.6
                   ≈ 593,000 bits ≈ **74 KB per cell**

This is remarkably close to the Framework B estimate
(75 KB at p = 8) — the large atom count provides about
8 bits of natural precision per mode through statistics.

### Capacity estimates per cell

| r_ν   | Modes N | Bits/mode | Total        |
|--------|---------|-----------|--------------|
| 100    | 3,800   | 15.6      | 7.4 KB       |
| 1,000  | 38,000  | 15.6      | **74 KB**    |
| 10,000 | 380,000 | 15.6      | **740 KB**   |
| 10⁶    | 3.8×10⁷ | 15.6      | **74 MB**    |

(Bits per mode is nearly constant because it depends on
M/N, and M ≈ 10¹⁴ is large for all reasonable N.)

### Scaling to organisms

Each cell is one domain.  The human body has ~37 trillion
cells (3.7 × 10¹³).  Each organ, tissue type, or
developmental lineage might maintain a coherent sub-
population.

| System             | Cells   | Capacity (r_ν=1000) |
|--------------------|---------|---------------------|
| One cell           | 1       | 74 KB               |
| One neuron         | 1       | 74 KB               |
| Brain (86 billion) | 8.6×10¹⁰| **6.4 PB**         |
| Whole body         | 3.7×10¹³| **2.7 EB**         |

For comparison:
- Human genome: ~750 MB
- Estimated synaptic weights in the brain: ~1–10 PB
- Entire internet (2025): ~120 ZB

**74 KB per cell** is biologically meaningful — comparable
to the information content of a small program or a
detailed configuration file.  A brain at 6.4 PB is in
the same range as the synaptic-weight estimate — two
entirely different models converging on the same order
of magnitude.

### Why one-cell-one-domain is a strong gateway

All 10¹⁴ atoms in a cell are "antennas" broadcasting and
receiving on the same neutrino-sheet state.  This gives:

1. **Massive signal amplification:** 10¹⁴ coherent
   contributors make the collective state extremely robust.
   Losing or gaining a few atoms doesn't change the pattern.

2. **Natural cell boundary:** when a cell divides, the two
   daughter cells separate beyond one Compton wavelength.
   Their neutrino states DECOUPLE — each gets an
   independent 74 KB register.  Cell division is a natural
   "fork" operation in the storage model.

3. **Intra-cell communication:** every atom in the cell
   "sees" the same neutrino-sheet pattern.  A chemical
   reaction at one end of the cell shifts mode occupancy;
   every other atom instantly reflects the change (at the
   speed of light on the compact dimensions).  This is
   instantaneous intra-cell signaling that doesn't require
   molecular diffusion.

4. **Inter-cell communication:** two adjacent cells share
   a boundary where their Compton-wavelength domains
   overlap.  Atoms near the boundary couple to BOTH cells'
   states.  This is the gateway for cell-to-cell
   communication — a physical overlap region, not a
   chemical signal.

5. **Thermal protection:** neutrino modes are electrically
   neutral.  Thermal photons at 300K (kT = 26 meV ≈ m_ν)
   couple to the neutrino sheet only through the
   vanishingly small cross-shear σ_eν.  The storage medium
   is naturally insulated from thermal noise.

### What sets the precision?

The precision p (bits per amplitude) determines whether
storage is byte-scale or megabyte-scale.  Physical
constraints:

1. **Energy resolution:** distinguishing two amplitudes
   requires detecting energy differences ~m_ν × δc².
   If δc = 2^{−p}, then δE ~ m_ν/2^p.  At p = 8,
   δE ~ m_ν/256 ~ 0.1 μeV — detectable by any system
   sensitive to sub-eV energy (e.g., molecular vibrations).

2. **Thermal noise:** at temperature T, thermal energy
   kT = 26 meV at 300K.  This is ~equal to m_ν at
   r_ν = 5.  For thermal noise not to scramble the state,
   the mode spacing must be larger than kT, OR the storage
   must be in a protected subspace where thermal noise
   doesn't couple.  Neutrino modes on T² couple weakly to
   thermal photons (no EM charge), which provides natural
   thermal protection.

3. **Decoherence time:** for adjacent modes separated by
   δE, the coherence time is τ = ℏ/δE.  At r_ν = 1000,
   the minimum mode spacing is ~m_ν/r_ν² ~ 30 neV, giving
   τ ~ 22 ps.  This is fast.  Long-lived superpositions
   require either (a) very large r_ν so that only widely
   spaced modes are used, or (b) Reiter's premise that the
   state is sub-quantum and doesn't decohere by standard
   mechanisms.

### Summary of capacity regimes

| Regime          | Per-particle    | Per-cell (10⁶ domains) |
|-----------------|-----------------|------------------------|
| Classical QM    | 2 bytes         | 2 MB                   |
| Threshold (p=8) | 75 KB           | 75 GB                  |
| Threshold (p=16)| 150 KB          | 150 GB                 |
| Threshold (p=32)| 300 KB          | 300 GB                 |

The threshold theory regime gives biologically meaningful
storage capacity.  The classical QM regime gives a
trivially small register.  The difference is entirely
about whether Reiter's sub-quantum channel exists.
