# Q101. Are ghost modes excited states of the electron?

**Question:** The (1,3), (1,4), (1,5), ... modes on Ma_e have the
same charge (−1) and spin (½) as the electron.  Rather than being
separate unobserved particles (the "ghost problem"), could they be
**excited internal states** of the electron — analogous to the
excited energy levels of a hydrogen atom?

**Short answer:** Yes, this interpretation is physically well-motivated
and resolves a significant fraction of the ghost problem.  The (1,n)
ladder forms a discrete, monotonically increasing energy spectrum
above the (1,2) ground state, with decreasing coupling strength and
increasing instability — exactly the pattern of quantum excited states.
The torus cavity's equilibrium shape provides the mechanism: it
"tunes" to the fundamental (1,2) mode and penalizes higher harmonics,
just as a resonant cavity rings at its fundamental.


## The energy ladder

The single-sheet energy for mode (1, n₂) on Ma_e scales as
μ = √(1/r² + (n₂ − s)²), where r is the aspect ratio and s ≈ 0.01
is the within-plane shear.  Since s is small, the energy grows
approximately as n₂:

| Mode | Mass (m_e units) | Energy (MeV) | Δ from (1,2) |
|------|----------------:|-------------:|-------------:|
| (1,1) | 0.502 | 0.257 | −0.254 |
| **(1,2)** | **1.000** | **0.511** | **ground state** |
| (1,3) | 1.500 | 0.766 | +0.255 |
| (1,4) | 2.000 | 1.022 | +0.511 |
| (1,5) | ~2.50 | ~1.28 | +0.77 |
| (1,8) | 4.006 | 2.05 | +1.54 |
| (1,n) | ~n/2 | ~n × 0.256 | ~(n−2) × 0.256 |

Source: R33 F2 (coupling and mass table for n₁ = 1 modes).

Each step up the ladder costs roughly 0.256 MeV (half the electron
mass).  The spectrum is discrete, monotonic, and bounded below — the
defining characteristics of quantum energy levels.

The (1,1) mode sits *below* the electron and is a separate case: under
the WvM spin assignment it has spin 1 (boson), making it a different
species from the spin-½ ladder.  Under the tube-winding convention it
is also spin ½ — its status is discussed separately (R33 F4, R46).


## Why the ground state is preferred

### Cavity self-tuning (R40 F10)

When the torus cross-section reaches equilibrium under the (1,2)
mode's radiation pressure, higher ring harmonics (higher n₂) are
penalized:

| Mode | Energy shift on (1,2)-optimized cavity |
|------|---------------------------------------:|
| (1,2) | 0% (stable — it shaped the cavity) |
| (1,4) | +11.8% |
| (1,5) | +17.6% |
| (1,6) | higher still |

Source: R40 F10 (bandpass on n₂ from the (1,2) equilibrium shape).

This is standard resonant-cavity physics.  A cavity adapts to its
fundamental mode; that adaptation creates an energy barrier for
higher harmonics.  An electron in the (1,2) state has shaped its
Ma_e cavity into a configuration that resists transitions to (1,3)
or higher — just as a tuned circuit resists oscillation at
off-resonance frequencies.

### Coupling suppression (R33 F5)

The electromagnetic coupling of mode (1, n₂) to external space
scales as ~1/n₂².  Higher excited states couple more weakly to the
outside world, making them harder to excite and easier to lose.
In atomic physics, the same pattern holds: higher-n states have
weaker transition matrix elements and shorter lifetimes (for
spontaneous emission).

| Mode | EM coupling / electron | Suppression |
|------|----------------------:|------------:|
| (1,2) | 1.00× | reference |
| (1,3) | 0.66× | 1.5× weaker |
| (1,4) | 0.50× | 2× weaker |
| (1,8) | 0.25× | 4× weaker |
| (1,n) | ~1/n₂² | ~n₂²/4 × weaker |

Source: R33 F2, F5 (charge coupling integral for n₁ = 1 modes).


## The analogy to atomic energy levels

| Feature | Atomic physics | Ma excited states |
|---------|---------------|-------------------|
| Ground state | Hydrogen n = 1 | Electron as (1,2) on Ma_e |
| Excited states | n = 2, 3, 4, ... | (1,3), (1,4), (1,5), ... |
| Energy ordering | Monotonically increasing | Monotonically increasing |
| Stability | Ground state stable; excited states decay | (1,2) stable; higher modes unstable |
| Decay mechanism | Photon emission | Mode transition, radiating excess energy |
| Coupling strength | Decreases with n | Decreases as ~1/n₂² |
| Discrete spectrum | Bohr/Schrödinger levels | Torus winding-number quantization |
| Energy scale | ~eV (Coulomb potential) | ~MeV (compact geometry) |

The critical difference is the energy scale.  Atomic energy levels
arise from the Coulomb potential in the spatial dimensions S
(~eV scale).  The Ma excited states arise from the compact geometry
itself (~MeV scale).  These are excitations of the electron's
*internal structure*, not of its position in an atom.

Ordinary atomic spectral lines are well-explained by the Coulomb
potential and are not affected by this internal ladder.  The Ma
excitations would be observable only at MeV energies — the domain
of pair production and high-energy electron scattering.


## What this resolves

### The ghost problem shrinks

R38 F1 found 14,012 charge −1, spin ½ energy levels below 10 GeV,
of which 66 lie between the electron and muon masses.  Under the
standard interpretation, each is a "ghost particle" — an unobserved
species that the model must explain away.

Under the excited-state interpretation, the single-sheet (1,n≥3)
modes are not separate particles.  They are internal excitations of
the electron that exist only transiently when sufficient energy is
supplied.  The "ghost" count drops by the number of pure electron-sheet
ladder modes — a significant fraction of the low-energy population.

Cross-sheet ghosts (modes with nonzero windings on multiple sheets)
remain a separate problem and are not addressed by this reframing.

### Particle identity is clarified

A common objection to the Ma spectrum is: "if (1,5) is a valid mode,
why don't we see a 1.28 MeV electron-like particle?"  The answer:
for the same reason we don't call the hydrogen n = 3 state a "new
particle."  It's the same electron, temporarily at a higher energy
level.  It has the same charge, the same spin, and it decays back
to the ground state.

### The off-resonance hypothesis is reinforced

The off-resonance hypothesis (R27 F33) says unstable particles sit
between eigenmodes and the gap predicts the lifetime.  The excited
states of the electron ARE the eigenmodes that nearby particles sit
between.  The (1,3) mode at 0.766 MeV is a real eigenmode — but
because the cavity is shaped for (1,2), the (1,3) state cannot
persist.  It decays to (1,2) by emitting ~0.255 MeV of radiation.

The expected lifetime of an excited state scales with the energy
gap and coupling strength: large gap (easy to radiate) + weak
coupling (slow to absorb) = short-lived.  This is consistent with
no (1,3) particle ever being observed as a stable species.


## Observable consequences

If the (1,n) ladder represents real internal excitations, several
predictions follow:

1. **MeV-scale electron resonances.**  High-energy electron
   scattering should show resonances at discrete energies
   corresponding to (1,3) at ~0.77 MeV, (1,4) at ~1.02 MeV, etc.
   These would appear as brief enhancements in cross-sections,
   not as stable particles.

2. **The (1,4) mode coincides with pair threshold.**  The (1,4)
   energy of ~2 m_e = 1.022 MeV is exactly the electron-positron
   pair production threshold.  Whether this is a coincidence or
   a connection deserves investigation: could pair production
   involve a transient (1,4) excitation?

3. **Emission spectrum from de-excitation.**  An electron dropping
   from (1,3) back to (1,2) would emit a ~0.255 MeV photon.
   This is in the hard X-ray / soft gamma range — potentially
   observable in high-energy physics experiments.

4. **Transition selection rules.**  Not all (1,n) → (1,m)
   transitions may be allowed.  The coupling integral and
   cavity geometry may impose selection rules analogous to
   Δl = ±1 in atomic physics.  This is computable from the
   Ma model.


## Open questions

1. **Which spin convention governs stability?**  Under the WvM
   spin = n₁/n₂ rule (R33 F3), the (1,n≥3) modes have fractional
   spin and are simply forbidden — they don't exist as states at
   all.  Under the tube-winding-parity rule (Taxonomy §4.2,
   `ma_model.py`), they are valid spin-½ states.  The
   excited-state interpretation requires the tube-winding
   convention.  Resolving the spin rule (R33 deferred Track 6)
   would settle this.

2. **Lifetime estimates.**  The decay rate (1,3) → (1,2) + γ
   should be computable from the coupling integrals in R33 and
   the radiation physics in R40/R41.  If the predicted lifetime
   is ~10⁻²⁰ s or shorter, these states would be unresolvable
   in current experiments — consistent with non-observation.
   If longer, they should be detectable.

3. **Cross-sheet excited states.**  The muon mode (−1,5,0,0,−2,0)
   could also have excited states: (−1,5,0,0,−2,±1),
   (−1,5,0,0,−2,±2), etc.  Whether the excited-state
   interpretation extends to cross-sheet modes is unexplored.

4. **Experimental signatures.**  Have electron resonances at
   0.77 MeV or 1.02 MeV been looked for in existing scattering
   data?  A literature search would determine whether this
   prediction is already constrained.


## Relationship to the ghost problem

This reframing does not fully solve the ghost problem — it
addresses the single-sheet (1,n) ladder on each charged sheet.
The broader ghost problem includes:

- **The (1,1) mode:** spin-1 boson at 0.26 MeV (R33 F4).
  Not part of the excited-state ladder (different spin class
  under WvM, or the lowest state under tube-winding).
- **Cross-sheet ghosts:** modes spanning Ma_e × Ma_p with valid
  charge and spin but no observed particle (R33 F7).
- **Ghost count at high energy:** 14,012 levels below 10 GeV
  (R38 F1), mostly cross-sheet modes.

The excited-state interpretation removes the single-sheet
(1, n≥3) modes from the ghost census.  For the remainder,
the Compton window hypothesis (Q94), cavity Q arguments
(R38 F8–F10), and dynamic filter factors (R41 F36) remain
the active lines of investigation.


## Studies

- R33 F1–F5: charge integral, coupling hierarchy, spin filter
  for (1,n) modes on Ma_e
- R33 F4: the (1,1) boson ghost (separate problem)
- R33 Track 6 (deferred): spin derivation — would resolve which
  spin convention is correct
- R38 F1: charged lepton census (14,012 levels below 10 GeV)
- R38 F8–F10: cavity Q ≈ 30, generation gating
- R40 F10: bandpass on n₂ from (1,2) equilibrium shape
- R40 F12–F15: per-mode shape optimization and barrier arguments
- R41 F35–F36: dynamic filter factors by tube harmonic
- R27 F33: off-resonance hypothesis (lifetime-gap correlation)
- Q86: three generations and the ghost problem
- Q94: Compton window and dark modes
- R46: electron filter (current study, where this question arose)
