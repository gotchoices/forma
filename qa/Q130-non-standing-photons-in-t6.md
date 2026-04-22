# Q130: Does a non-standing-photon bath in T⁶ influence the embedding — through the Compton window, and with what effective equation of state?

**Status:** Open — framing document.  Two distinct
mechanisms by which free (non-bound, non-standing) EM
excitations of Ma could influence the non-compact spatial
embedding: (a) resonant leakage into S selected by Compton-
scale matching to bound modes, (b) non-trivial effective
equation of state in the 3D projection.  Neither derived
yet; both concrete and computable on model-F's metric.

**Related:**
  [Q94](Q94-compton-window-and-dark-modes.md) (Compton window and dark modes),
  [Q123](Q123-higgs-mechanism-in-mast.md) (Higgs mechanism — §5.1 Hessian ground state),
  [Q127](Q127-orders-of-compactification.md) (orders of compactification),
  [Q128](Q128-detecting-compact-universe.md) (α as leakage rate, cosmological signatures),
  [Q129](Q129-discrete-mass-atlas-with-s-separation.md) (discrete mass atlas),
  [R42](../studies/R42-dark-matter/) (dark matter from ghost modes),
  [R59](../studies/R59-clifford-torus/), [R60](../studies/R60-metric-11/) (σ_ta coupling, 9D metric solver).

---

## 1. The setup

MaSt particles are **standing-wave** excitations of Ma —
definite winding, fixed energy, stable identity.  The
complement: **non-standing** excitations are free EM quanta
propagating through Ma without forming a bound mode.  These
are natural objects on the T⁶ geometry (any compact
manifold admits both standing and travelling excitations),
and cosmological contexts (thermal bath, primordial
radiation, GRID-level fluctuations) would generically
populate them.

**Question:** does a bath of non-standing Ma photons
influence the non-compact spatial embedding S in ways
distinct from what bound modes contribute?  Two mechanisms
and one regime question are worth separating.

## 2. Mechanism A — direct σ_ta coupling (baseline)

Any excitation of Ma couples to S via the same
`σ_ta ~ √α` chain that R59/R60 use to establish α
universality.  A non-standing photon bath therefore leaks
energy into S at α-scaled rate **regardless of
wavelength**.  This channel is not Compton-window-specific
and not privileged over bound-mode leakage.

Not itself novel; baseline behaviour.

## 3. Mechanism B — Compton-window resonant enhancement

At wavelengths matching the Compton scale `λ_C = h/(mc)`
of any bound Ma mode, a non-standing photon can resonantly
pump that mode.  Three consequences:

- **Bound particles as transducers.**  Non-standing photon
  energy → resonant excitation of a bound mode → the
  bound mode's normal S-coupling radiates it out.  This
  is **[R42](../studies/R42-dark-matter/)'s ghost-mode
  mechanism run in reverse**: R42 uses the Compton window
  to select what's dark; here the same window selects what
  couples through.
- **Selection by the particle spectrum.**  A uniform
  thermal bath in T⁶ would be filtered by Ma's bound-mode
  Compton scales: wavelengths near electron-Compton,
  proton-Compton, neutrino-Compton leak preferentially;
  off-resonance photons pass through largely unaffected.
- **Frequency structure in the leakage spectrum.**  If B
  is the dominant channel, the α-leakage signal of
  [Q128](Q128-detecting-compact-universe.md) acquires
  spectral features at characteristic Compton scales —
  quite distinct from the uniform per-cycle rate Q128
  currently assumes.

Mechanism B is a conjugate of R42 that no current Q file
or study names explicitly.  This is the novelty of Q130.

## 4. Mechanism C — effective equation of state in the 3D projection

An isotropic radiation bath in 6+3 dimensions has `w = +1/3`
uniformly.  A bath confined to the **compact six** and
projected into the **non-compact three** has a different
effective `w` — the 3D pressure depends on how photon
momentum partitions between Ma and S components.

This is the standard Kaluza-Klein / braneworld
pressure-decomposition effect: bulk fields give rise to
4D effective equations of state that differ from their
bulk values.  Applied to MaSt's specific three-sheet
architecture with cross-couplings, the 3D-projected `w`
could land anywhere in `[−1, +1/3]` depending on the
polarization and cross-shear structure.

**If `w → −1` in the projection**, a T⁶ photon bath could
mimic a cosmological constant — a MaSt-native mechanism
for dark energy distinct from vacuum-energy-of-modes
(which inherits the cosmological constant problem).  This
is speculative but checkable.

## 5. What this predicts (if derivations work out)

Under Mechanism B alone:
- Q128's predicted leakage signal has spectral structure
  peaked at bound-particle Compton scales.
- Cosmic photon bath with these specific frequencies is
  predicted to drain more efficiently than off-resonance
  radiation.
- Could contribute to CMB spectral distortions at
  frequencies tied to particle masses — potentially
  observable by future CMB missions (PIXIE-class).

Under Mechanism C alone:
- The non-compact 3D effective `w` for a T⁶ photon bath
  is a specific computable number.
- If `w < −1/3`, the bath contributes accelerating
  pressure; if `w ≈ −1`, it looks like Λ.
- Either way it is a quantitative prediction of model-F,
  not a free parameter.

Under B and C together:
- The dark-energy-like contribution is **density-selected**
  by the Compton window, not uniform across all modes.
- Gives a natural regulator for the cosmological constant
  problem: most of the naive vacuum energy in T⁶ doesn't
  contribute because only Compton-resonant wavelengths
  couple effectively.

## 6. Concrete derivation targets

1. **Compton-resonance rate computation.**  Starting from
   model-F's σ_ta coupling, compute the rate at which a
   non-standing photon at wavelength λ pumps a bound mode
   of Compton scale λ_C.  Identify the Lorentzian width
   and peak amplitude.  Compare the resulting spectral
   profile to a uniform-rate α-leakage for the same total
   energy flow.
2. **3D-projected equation of state.**  On model-F's 9D
   solved metric, decompose the stress-energy of an
   isotropic photon bath into Ma-direction and S-direction
   components.  Read off the 3D pressure and compute
   `w_eff = p_S / ρ_total`.  Depends only on metric
   structure — no free parameters.
3. **Cosmological-constant problem check.**  If C alone
   gives `w ≈ −1`, what bath density does model-F predict?
   Compare to observed ρ_Λ ≈ 10⁻¹²²  in Planck units.  If
   the prediction is off by the usual 60–120 orders, the
   mechanism fails.  If the Compton-window selection
   (B) regulates the density to observed value, the
   mechanism succeeds.

All three targets are pure geometry computations using
R60's existing solver — no new framework required.

## 7. Relation to existing threads

- **Q128** has α-leakage; Q130 adds Compton-window
  structure to that leakage, and adds the 3D equation-of-
  state angle Q128 does not cover.
- **R42** uses the Compton window to identify dark
  modes; Q130 uses the same window as a selection
  mechanism for *which* non-standing excitations couple
  strongly — opposite face of the same coin.
- **Q123 §5.1** proposes Higgs as lightest 9D Hessian
  eigenmode; Q130's equation-of-state question is a
  nearby calculation on the same metric, targeting the
  bulk rather than a specific eigenmode.
- **Q129** asks what Ma + S looks like as a unified mass
  scale for bound modes; Q130 asks the complementary
  question for non-bound excitations.

## 8. Status

Framing only.  Two mechanisms (B and C) and one derivation
chain (§6).  The required infrastructure already exists.
Worth promoting to a study (candidate R63, joint with the
discrete mass atlas of Q129, or R64 as a standalone
cosmology-facing derivation) only after the three
calculations in §6 return non-trivial results.  If all
three fail, Q130 closes cleanly as a negative result on a
tempting-but-wrong mechanism.
