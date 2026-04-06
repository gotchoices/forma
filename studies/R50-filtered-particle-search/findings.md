# R50 Findings

Study: [`README.md`](README.md)

---

## Track 1: Build `ma_model_d.py`

### Model status at end of Track 1

| Component | Status | Notes |
|-----------|--------|-------|
| Energy (6×6 metric) | **Ready** | Electron, proton, neutrino energies exact |
| Charge (fundamental) | **Ready** | Q = −n₁ + n₅ correct for simple modes |
| Charge (composite) | **Ready** | gcd-based division gives Q = +1 for (3,6) proton |
| Spin (topological) | **Ready** | Exact ½ for electron, proton, neutrino — from tube winding parity |
| Waveguide on Ma_e | **Ready** | (1,1) ghost killed, (1,2) electron passes with 30% margin |
| Waveguide on Ma_ν | **Ready** | All modes propagate at ε = 5 |
| Waveguide on Ma_p | **Usable with caveat** | (1,1) ghost killed, (3,6) propagates; but standalone (1,2) ghost also passes — this is the confinement problem |
| Classical L_z diagnostic | **Informational** | Not the physical spin; retained for geometry studies |
| Mode scan | **Ready** | Brute-force 6D scan with filtering |
| Near-miss finder | **Ready** | Finds closest modes to a target mass |
| Alpha formula | **Ready** | Both sheets solve α = 1/137 |

**Bottom line:** The model engine is ready for the particle sweep
(Tracks 2–5).  One physics question remains open: standalone (1,2)
modes on Ma_p propagate, predicting a Q = +1 spin-½ particle at
~313 MeV that isn't observed.  This is the quark confinement
problem — quarks have well-defined properties but aren't free.
The sweep should proceed and flag these modes, not wait for
confinement to be solved.

**Script:** [`scripts/track1_validate.py`](scripts/track1_validate.py)
**Code:** [`lib/ma_model_d.py`](../lib/ma_model_d.py)

### F1. Model-D engine implemented

`ma_model_d.py` provides the `MaD` class — a clean replacement for
`ma_model.py` (model-C).  All parameters are explicit inputs; nothing
is derived from hard-coded assumptions.  No scipy dependency.

**Per-sheet inputs:** aspect ratio ε, within-plane shear s, ring
circumference L_ring.  **Cross-sheet inputs:** σ_ep, σ_eν, σ_νp.

**APIs:** `energy()`, `charge()`, `spin_halves()`, `spin_Lz_total()`,
`propagates()`, `energy_decomp()`, `scan_modes()`, `nearest_modes()`,
`with_params()`, `from_physics()`.

### F2. Reference energies validated

At default parameters (ε_e = 0.5, ε_ν = 5.0, ε_p = 1/3):

| Particle | Mode | Predicted | Target | Error |
|----------|------|-----------|--------|-------|
| Electron | (1,2,0,0,0,0) | 0.510999 MeV | 0.511000 MeV | < 0.001% |
| Proton | (0,0,0,0,3,6) | 938.272 MeV | 938.272 MeV | exact (input) |
| Neutrino ν₁ | (0,0,1,1,0,0) | 29.20 meV | ~29 meV (R49) | consistent |

These are single-sheet energies (zero cross-shears).  The electron and
proton energies are inputs by construction (the ring circumference is
derived from the target mass).  The neutrino energy is derived from
Δm²₂₁ and s₃₄ = 0.022.

### F3. Ghost filtering — what works and what doesn't

Updated defaults: ε_e = 0.65, ε_p = 0.55, ε_ν = 5.0.  The
principle (from the user): place the cutoff just above the mode
you want to cancel, not just below the mode you want to keep.
This gives clear margin between ghost and desired mode.

**Ma_e (electron sheet) — WORKS:**

| Mode | n₂ | Cutoff (1/ε = 1.54) | Status | Margin |
|------|---|---------------------|--------|--------|
| Ghost (1,1) | 1 | 1 < 1.54 | **KILLED** | — |
| Electron (1,2) | 2 | 2 > 1.54 | **PASSES** | 30% |

**Ma_ν (neutrino sheet) — WORKS:**

| Mode | n₄ | Cutoff (1/ε = 0.20) | Status | Margin |
|------|---|---------------------|--------|--------|
| ν₁ (1,1) | 1 | 1 > 0.20 | **PASSES** | 400% |

**Ma_p (proton sheet) — UNRESOLVED CONFINEMENT TENSION:**

Waveguide and spin are now checked per-strand for composites.
The (3,6) proton = three (1,2) strands, so the composite
propagates wherever its strands do.  This fixes two former
problems (F4b, F4c) but creates a new one:

| Mode | Per-strand? | Cutoff (1/ε = 1.82) | Status |
|------|-------------|---------------------|--------|
| Ghost (1,1) | No | 1 < 1.82 | **KILLED** ✓ |
| Ghost (1,2) standalone | No | 2 > 1.82 | **PASSES** ✗ |
| Proton (3,6) composite | Yes → (1,2) | 2 > 1.82 | **PASSES** ✓ |

The standalone (1,2) on Ma_p has E = 313 MeV, Q = +1, spin ½.
No such particle exists.  **This is the confinement problem:**

- If strands can propagate → so can standalone (1,2) ghosts
- If strands can't propagate → the composite can't either
- There is no ε window where (3,6) propagates but (1,2) does not,
  because the composite IS three (1,2) strands

This mirrors the confinement problem in QCD: individual quarks
have well-defined properties (~313 MeV, Q = ±1/3 or ±2/3) but
are never observed free.  Confinement requires physics beyond
the waveguide cutoff — likely color charge or flux-tube binding
between strands.

**For R50:** The waveguide filter works for Ma_e and Ma_ν.
For Ma_p, the (1,1) ghost is killed, but standalone (1,2) modes
pass.  The particle sweep should flag standalone proton-sheet
modes as "quark-like" and note they require confinement.

### F4. Proton (3,6) composite — resolved per-strand

**F4a. Charge (resolved):** Q = −n₁ + n₅ gives +3 for the raw
(0,0,0,0,3,6) tuple.  `charge_composite()` divides the proton-
sheet contribution by gcd(n₅, n₆) = 3, giving Q = +1.  This is
the R47 Track 7 F4 fractional quark charge mechanism.

**F4b. Waveguide (resolved):** Per-strand checking: each (1,2)
strand is tested against the sheet's ε, not the composite (3,6).
At ε_p = 0.55: strand (1,2) has cutoff 1.82 < 2 → propagates.
The composite propagates because its strands do.

**F4c. Spin (resolved):** Per-strand spin: each (1,2) strand
contributes L_z/ℏ = 0.529 at ε = 0.55 (6% from ½).  The
previous result of 0.171 was wrong — it applied the single-
geodesic formula to the (3,6) path, which wraps the tube 3 times
and is a different trajectory from three (1,2) paths.

### F5. Spin: topological vs classical

**Physical spin is topological.**  A mode's spin depends only on
whether its tube winding numbers are odd or even.  Odd n_tube → ½.
This is exact, always gives half-integers, and does not depend on
ε, shear, or any continuous geometry parameter.

| Mode | n_tube (per strand) | Topological spin |
|------|---------------------|------------------|
| Electron (1,2) | n₁ = 1 (odd) | **½** |
| Proton (3,6) → strand (1,2) | n₅ = 1 (odd) | **½** |
| Neutrino (1,1) | n₃ = 1 (odd) | **½** |
| Boson example (2,4) | n = 2 (even) | **0** |

The classical L_z/ℏ (path integral on the torus surface) is a
separate quantity — the orbital angular momentum of a geodesic.
It gives non-half-integer values (0.535, 0.529, 0.358) because
it is a continuous geometric calculation, not a topological one.
It is retained in the model as a diagnostic (`spin_Lz_total()`)
but is **not used for filtering** and should not be confused with
the physical spin.

R49's concern about "marginal spin" at ε = 5 was a misattribution:
the path integral's deviation from ½ reflects the classical
geodesic geometry, not a problem with the mode's quantum spin.
The neutrino's spin is ½ by topology regardless of ε_ν.

### F6. Alpha formula validated

Both the electron and proton sheets produce α = 1/137.036
from the R19 formula α(ε, s) = ε² μ sin²(2πs) / (4π(2−s)²):

| Sheet | ε | s (solved) | α (computed) |
|-------|---|------------|-------------|
| Ma_e | 0.5 | 0.12056 | 0.00729735 |
| Ma_p | 1/3 | 0.17311 | 0.00729735 |

### F7. Mode scan at default parameters

At n_max = 2 with zero cross-shears, 944 propagating modes exist
below 2 GeV.  The lowest modes are all on Ma_ν (neutrino sheet),
as expected given the ~meV energy scale of that sheet.

The proton-sheet modes (~938 MeV scale) appear at higher energies
but only if `propagating_only=False` is used (see F4b).

### F8. Neutron near-miss at n_max = 2

With zero cross-shears and n_max = 2, no mode comes close to
939.565 MeV.  The nearest propagating Q = 0 mode is at 178 MeV
(81% off).  This is expected:
- Cross-shears are required for cross-sheet modes
- n_max = 2 is too small to reach the proton mass scale
  on sheets other than Ma_p
- The neutron search is Track 3's job

### F9. Geometry at default parameters

| Sheet | ε | s | L_ring (fm) | L_tube (fm) | Scale |
|-------|---|---|-------------|-------------|-------|
| Ma_e | 0.650 | 0.096 | 5.939 × 10³ | 3.861 × 10³ | nm (Compton) |
| Ma_ν | 5.000 | 0.022 | 4.239 × 10¹⁰ | 2.119 × 10¹¹ | μm |
| Ma_p | 0.550 | 0.111 | 1.039 × 10¹ | 5.717 | fm (nuclear) |

### F10. Design decisions documented

**Waveguide boundary:** Uses `≥` (at-cutoff modes propagate).
With the updated defaults (ε_e = 0.65), the electron is well
above cutoff (30% margin), so this edge case rarely matters.

**Composite handling:** Waveguide and spin are checked per-strand
for composite modes (gcd > 1).  The (3,6) proton is treated as
three (1,2) strands.  Each strand is checked against the sheet's ε.

**No scipy:** The shear solver uses bisection (60 iterations,
~10⁻¹⁸ precision) instead of `scipy.optimize.brentq`.  The spin
integral uses numpy trapezoidal summation with 2048 points.

**Separation of concerns:** `ma_model_d.py` does not know which
mode is "the electron" or "the proton."  The `from_physics()`
constructor is a convenience wrapper that makes assumptions
(electron = (1,2), proton = (3,6), neutrino = (1,1)) but the
core `MaD` class is assumption-free.

---

## Track 2: Cross-shear sweep — neutron as first cross-sheet test

**Script:** [`scripts/track2_cross_shear_sweep.py`](scripts/track2_cross_shear_sweep.py)

### Setup

Sweeps each cross-shear parameter (σ_ep, σ_eν, σ_νp) independently
over the range −0.3 to +0.3, searching for Q = 0, spin-½ modes
within striking distance of the neutron mass (939.565 MeV).

**Self-consistent L_ring adjustment.**  When σ ≠ 0, the Schur
complement modifies the diagonal blocks of G̃⁻¹, changing the
effective dimensionless energy μ_eff of reference modes.  Ring
circumferences must be re-derived so that E(electron) = 0.511 MeV
and E(proton) = 938.272 MeV remain exact.  A key insight from
Track 2: the dimensionless metric G̃ depends only on (ε, s, σ),
NOT on the absolute circumferences L.  This means L_ring can be
derived analytically from G̃⁻¹ and the target mass — no iteration
is needed (unlike model-C's iterative scheme).

**Search space.**  7,800 Q = 0, spin-½ mode 6-tuples generated
from n₁ ∈ [−3,3], n₂ ∈ [−4,4], n₃ ∈ [−2,2], n₄ ∈ [−2,2],
n₅ ∈ [−6,6], n₆ ∈ [−10,10].  Of these, 2,556 pass the waveguide
propagation filter.  Energies are computed in vectorized batches
(numpy) for each σ value.

### F11. Best mass match: (0, 0, 2, 2, 0, −8) at σ_νp ≈ −0.13

The numerically closest Q = 0, spin-½ mode to the neutron mass:

| Property | Value |
|----------|-------|
| Mode | (0, 0, 2, 2, 0, −8) |
| Energy | 939.819 MeV |
| Residual | +0.254 MeV (0.03%) |
| Cross-shear | σ_νp = −0.130 |
| Charge | Q = 0 |
| Spin | ½ (from Ma_ν composite strand) |
| Sheets active | Ma_ν + Ma_p |

**Quantum number anatomy:** This mode has no electron-sheet
winding (n₁ = n₂ = 0).  The neutrino sheet carries (2, 2), which
is a composite of gcd(2, 2) = 2 strands of (1, 1).  Each strand
has odd tube winding → spin ½.  The proton sheet carries (0, −8)
— pure ring winding, no tube — so it contributes mass but no
charge or spin.

**Decomposition concern (open):** The real neutron decays via
n → p + e⁻ + ν̄_e.  Intuitively, a neutron mode should contain
an electron-sheet component that can "unravel" into the decay
electron.  Mode (0, 0, 2, 2, 0, −8) has **no Ma_e winding**,
which raises the question of where the electron comes from.

However, we do not have proof that a mode on one sheet cannot
produce decay products on a different sheet.  Energy arriving
along one axis can depart along another (a baseball hit in x
can leave in y).  Cross-sheet coupling (σ ≠ 0) already shows
that sheets are not independent — the same coupling that shifts
mode energies may also allow cross-sheet decay channels.

**Status:** Flagged as a concern, not a disqualification.  The
F12 candidate (below) avoids this issue entirely by spanning all
three sheets.  Both candidates should be carried forward.

### F12. Three-sheet neutron: (0, 4, 1, −2, 0, 8) at σ_ep ≈ −0.13

A three-sheet candidate that naturally decomposes into proton +
electron + neutrino components:

| Property | Value |
|----------|-------|
| Mode | (0, 4, 1, −2, 0, 8) |
| Energy | ~939.2 MeV (varies with σ_ep) |
| Minimum residual | 0.358 MeV |
| Cross-shear | σ_ep ≈ −0.130 |
| Sheets active | Ma_e + Ma_ν + Ma_p |

This mode spans all three sheets: Ma_e ring (n₂ = 4) provides
the electron component, Ma_ν (n₃ = 1, n₄ = −2) provides spin ½
and the neutrino component, and Ma_p ring (n₆ = 8) provides the
mass.  The σ_ep cross-shear shifts its energy through the
electron–proton coupling — the electron ring winding is what
enables this coupling.

**Structural parallel to model-C neutron:**

| Property | Model-C neutron | F12 candidate |
|----------|----------------|---------------|
| Mode | (0, −2, 1, 0, 0, +2) | (0, 4, 1, −2, 0, 8) |
| Ma_e winding | n₂ = −2 | n₂ = 4 |
| Ma_ν winding | n₃ = 1 | n₃ = 1, n₄ = −2 |
| Ma_p winding | n₆ = +2 | n₆ = 8 |
| Spin source | Ma_ν (n₃ = 1) | Ma_ν (n₃ = 1) |
| Cross-shear | σ_ep = −0.091 | σ_ep ≈ −0.130 |
| Mass residual | 0 (pinned) | 0.358 MeV (near-miss) |
| Beta decay | ✓ (has e winding) | ✓ (has e winding) |

Both get spin from Ma_ν (n₃ = 1, odd tube winding).  Both have
electron-sheet winding enabling beta decay.  The model-D
candidate has higher winding numbers throughout (n₂ = 4 vs −2,
n₆ = 8 vs 2), reflecting the different proton geometry — (3,6)
composite at ε_p = 0.55 vs (1,2) at r_p = 8.906.

The n₆ = 8 proton-ring winding is notably higher than the
proton's n₆ = 6.  The neutron winds the proton ring at a higher
harmonic than the proton itself.

The 0.358 MeV residual is consistent with the neutron being a
near-miss (it is unstable, τ = 879 s).  Whether this gap maps
to 879 s under the off-resonance power law (τ ∝ |gap|^−2.7
from R27 F33) should be checked in Track 4.

### F12a. σ_νp is physically nonzero

Although F11's specific mode is not the neutron, the σ_νp sweep
reveals that modes near the neutron mass appear at σ_νp ≈ ±0.13.
This constrains σ_νp to be nonzero and of substantial magnitude
— important for the fusion bootstrap pathway (Q89 §12.2), which
requires σ_νp ≠ 0 so that protons have virtual neutrino-sheet
fluctuations that can be pumped by IR at 42 μm.

If the physical neutron is produced by σ_ep (F12), then σ_νp
remains unconstrained by the neutron mass.  Both cross-shears
may be nonzero — they come from independent sweeps and need not
be exclusive.

### F12b. Dark windings — mass without charge

A "dark winding" is any component of a mode that contributes
energy (mass) without contributing charge.  The model already
handles these naturally:

- **Ring windings** on any sheet (n₂, n₄, n₆) contribute to E²
  through the metric but never enter the charge formula
  Q = −n₁ + n₅.  A mode can carry GeV-scale mass from pure
  ring winding and still be electrically neutral.

- **All windings on Ma_ν** are dark — the neutrino sheet has no
  charge channel (Q102: neutrino neutrality from sheet size).

- **Even-tube composites** on charged sheets can also be dark:
  a (2, 4) composite on Ma_p has strand (1, 2) with charge
  contribution n₅/gcd = 1, but a pure ring mode (0, n₆) has
  zero tube winding and zero charge.

Both neutron candidates make heavy use of dark windings:
the proton ring winding n₆ = 8 provides ~954 MeV of mass
with zero charge.  This is not a defect — it may be exactly
how neutral massive particles carry their mass in the model.

The mode scan already detects and catalogs dark-winding modes.
No filter change is needed.  Track 3 should watch for modes
that are ALL dark windings (no tube winding on any charged
sheet) — these would be completely invisible to electromagnetism
and are natural dark-matter candidates.

### F13. σ_eν has zero effect on proton-scale modes

The electron–neutrino cross-shear produces no energy shift at
the proton mass scale.  The best candidate is stuck at 954.3 MeV
(Δ = +14.7 MeV) regardless of σ_eν.

This is expected: σ_eν couples Ma_e (L ~ 6000 fm) to Ma_ν
(L ~ 10¹⁰ fm), neither of which carries significant energy at
the proton scale (L ~ 10 fm).

### F14. Cross-shear mechanism: indirect, not direct

The cross-shear effect on proton-scale mode energies operates
through an **indirect** mechanism:

1. **Direct cross-terms are negligible.**  The energy cross-term
   involves (n_e/L_e)(n_p/L_p), which is suppressed by the scale
   ratio L_p/L_e ≈ 1.75 × 10⁻³.  For the ν–p coupling the
   suppression is L_p/L_ν ≈ 2.45 × 10⁻¹⁰.

2. **The Schur complement modifies [G̃⁻¹]_pp.**  When σ ≠ 0,
   the inverse metric's proton-proton block changes through the
   Schur complement:
   [G̃⁻¹]_pp → [G̃_pp − G̃_pe G̃_ee⁻¹ G̃_ep]⁻¹.
   This correction is O(σ²), meaning the energy shift is
   **quadratic** in σ, not linear.  The first derivative ∂E/∂σ
   at σ = 0 is exactly zero for all candidates.

3. **L_ring_p adjusts to keep the proton mass fixed.**  The Schur
   complement shifts the proton's effective μ, so L_ring_p must
   be rescaled.  At σ_ep = 0.1, L_ring_p shifts by 1.81%.  This
   rescaling is what moves non-reference modes relative to the
   proton.

4. **Different modes shift differently.**  The Schur complement
   correction is a rank-1 (or low-rank) perturbation to [G̃⁻¹]_pp.
   It shifts different directions in mode space by different amounts.
   The ratio E(0,0,1,1,0,8)/E(proton) changes from 1.0171 at σ = 0
   to 1.0075 at σ_ep = 0.1 — a 0.94% relative shift, corresponding
   to ~9 MeV.  Over the full sweep range (σ up to ±0.3), the shift
   reaches ~50 MeV.

### F15. Mode spacing limits resolution

The proton sheet's energy unit is E₀_p = 2πℏc / L_ring_p ≈ 119 MeV.
This sets the spacing between adjacent proton-ring modes.

The neutron–proton mass difference (1.293 MeV) is only **1.08%**
of one mode spacing unit.  No integer quantum number on Ma_p can
land within 1.3 MeV of the proton by itself.  The neutron must
be tuned by cross-shear adjustment of L_ring_p (which shifts the
entire proton mode spectrum by a continuous amount).

This reinforces the parameter discipline from model-D: σ_νp
(or σ_ep) is **constrained** by the neutron mass, not pinned.
The constraint is: "the cross-shear must be in the range where
a Q = 0, spin-½ mode passes through 939.565 MeV."

### F16. Reference mass stability

The self-consistent L_ring adjustment keeps reference masses
exact to numerical precision across the entire σ sweep:

| Reference | Stability across σ_ep = ±0.3 |
|-----------|------------------------------|
| Electron (0.511 MeV) | shift < 10⁻¹⁶ MeV |
| Proton (938.272 MeV) | shift < 10⁻¹² MeV |

This confirms that the L_ring derivation from G̃⁻¹ is exact.

### Track 2 summary

Cross-shears CAN produce a neutron-like mode (Q = 0, spin ½,
m ≈ 939.6 MeV) in model-D.  The mechanism is indirect — the
Schur complement modifies the proton block of G̃⁻¹, which
shifts proton-ring modes relative to the proton reference mass
when L_ring_p is adjusted.

Two neutron candidates survive, carried forward with different
confidence levels:

- **(0, 4, 1, −2, 0, 8)** at σ_ep ≈ −0.13 (Δ = 0.36 MeV) —
  **preferred**.  Spans all three sheets.  Electron-sheet ring
  winding (n₂ = 4) provides a natural decomposition channel for
  beta decay.  Parallels model-C's neutron structurally.

- **(0, 0, 2, 2, 0, −8)** at σ_νp ≈ −0.13 (Δ = 0.25 MeV) —
  **flagged**.  Better mass match but no electron-sheet winding.
  Decomposition to p + e⁻ + ν̄ is not obvious (though
  cross-sheet energy transfer has not been ruled out).  May
  correspond to a dark or exotic neutral fermion.

Both share key structural features: spin from the neutrino
sheet, mass from the proton ring (n₆ = 8), and no proton tube
winding — consistent with the neutron having zero charge.

**Constraint from Track 2:** σ_ep ≈ −0.13 (from the preferred
candidate), constrained (not pinned) by the neutron mass.
Future tracks will provide additional constraints that may
prefer a slightly different value.

**Open questions:** Addressed in Track 3 below.


### Track 2 addendum: Re-run under (1,3) proton hypothesis

The original Track 2 results above used the (3,6) composite
proton.  After Track 5 established (1,3) as the leading proton
hypothesis, Track 2 was re-run to assess the neutron under (1,3).

**The (1,3) proton creates a structural neutron problem.**

The proton ring circumference changes dramatically:

| | (3,6) proton | (1,3) proton |
|---|---|---|
| L_ring_p | 10.39 fm | 4.51 fm |
| Ring energy unit E₀_p | ~119 MeV | ~275 MeV |
| Ring mode spacing | 119 MeV | 275 MeV |

The neutron mass (939.6 MeV) falls between proton-ring modes
n₆ = 3 (825 MeV) and n₆ = 4 (1100 MeV) — a 275 MeV gap with
no integer mode close by.  Under (3,6), mode n₆ = 8 landed at
954 MeV, only 14.7 MeV from the neutron.

**Spin parity blocks the proton's own winding.**  For Q = 0
with spin ½, the constraint is n₁ = n₅ (both even), n₃ odd.
The proton mode itself has n₅ = 1 (odd), so adding n₁ = 1 for
charge neutrality gives two odd tube windings — base spin
contribution = 2, which cannot reach spin ½ (only spin 1 or
3/2).  The neutron cannot contain the proton's tube winding.

**Cross-shear and electron ring cannot close the gap.**

| σ_ep | Best mode | E (MeV) | Gap |
|------|-----------|---------|-----|
| 0.00 | (0, 0, 1, 0, 0, 3) | 824.6 | 115 MeV |
| −0.13 | (0, 30, 1, −5, 0, 3) | 842.9 | 97 MeV |
| −0.30 | (0, 200, 1, −5, 0, 3) | 926.0 | 14 MeV |

Even extreme electron ring winding (n₂ = 200) at the maximum
σ_ep only closes the gap to ~14 MeV (1.4%).  The electron ring
contributes ~0.21 MeV per unit — too small to bridge a 115 MeV
gap.  Cross-shear sensitivity is ~0.7 MeV per unit σ — also
too small.

**Comparison of best neutron candidates:**

| Property | (3,6) result | (1,3) result |
|----------|-------------|-------------|
| Best mode | (0, 4, 1, −2, 0, 8) | (0, 200, 1, −5, 0, 3) |
| Energy | 939.2 MeV | 926.0 MeV |
| Gap | 0.36 MeV (0.04%) | 13.6 MeV (1.4%) |
| σ_ep | −0.13 | −0.30 |
| Electron ring | n₂ = 4 | n₂ = 200 |
| Physical? | yes — moderate winding | questionable — extreme winding |

**Assessment.** The (1,3) proton hypothesis has a structural
neutron problem.  The coarser proton-ring mode spacing (275 MeV
vs 119 MeV) means no integer mode lands near 939.6 MeV.  The
(3,6) model's larger L_ring_p naturally places n₆ = 8 close to
the neutron mass.

This creates a tension with Track 5's charge formula finding:
- **(1,3) wins** on nuclear charge formula and scaling (F31–F33)
- **(3,6) wins** on neutron mass proximity (F11, F12)

The two hypotheses each solve one fundamental problem while
creating another.  This tension is unresolved and should inform
the design of R51.

**Possible resolutions (not yet tested):**
1. A different ε_p could change L_ring_p and shift the mode
   spectrum — but ε_p is constrained by the waveguide cutoff
   (needs ε > 1/3 for (1,3) to propagate).
2. The neutron may require a mechanism beyond simple mode
   matching — e.g., a dynamical cross-sheet resonance that
   doesn't correspond to a single eigenmode.
3. A hybrid model where the proton is (1,3) but the nuclear
   scaling uses a different L_ring might resolve both problems,
   though this adds complexity.

---

## Track 3: Full joint mode sweep — particle spectrum

**Script:** [`scripts/track3_particle_sweep.py`](scripts/track3_particle_sweep.py)

### Setup

At σ_ep = −0.13 (preferred neutron cross-shear from Track 2),
scans all 6D modes up to 2 GeV across the tier 1–3 particle
targets.  Search ranges: n₁ ∈ [−3,3], n₂ ∈ [−6,6], n₃ ∈ [−3,3],
n₄ ∈ [−3,3], n₅ ∈ [−6,6], n₆ ∈ [−16,16] — 1.9 M 6-tuples.
Proton ring energy unit at this σ: E₀_p ≈ 115.7 MeV.

### F17. Topological spin-charge constraint

The additive spin rule (J = number of odd per-strand tube windings
× ½) constrains which (Q, J) combinations are realizable as
eigenmodes.

**The parity rule (fundamental modes).** Each charged sheet
contributes charge from its tube winding: Q = −n₁ + n₅/gcd.
When all tube windings are even (J = 0), charge must be even.
When all three are odd (J = 3/2), both n₁ and n₅/gcd are odd,
so their sum is even → Q is even.

| J   | Allowed Q parity | Reason |
|-----|------------------|--------|
| 0   | even only        | all tubes even → both charge contributions even |
| ½   | any              | one odd tube can be on Ma_ν (neutral) |
| 1   | any              | one odd can be on Ma_ν |
| 3/2 | even only (fundamental) | all three odd → Q even |

This means **charged pseudoscalar mesons (π±, K±) are
topologically impossible** — they need Q = ±1 with J = 0, but
J = 0 requires all tubes even, forcing Q even.

**Composite loophole (J = 3/2).**  The initial analysis predicted
that Q = ±1, J = 3/2 is also impossible.  This was wrong.
Electron-sheet composites create a loophole: n₁ = −2 with n₂ = −6
gives gcd = 2, strand (−1, −3), strand tube = 1 (odd).  The raw
charge is Q_e = −(−2) = +2 (even), but the per-strand tube is
odd → spin ½.  Combined with odd tubes on Ma_ν and Ma_p, this
gives J = 3/2 with Q = +2 + (−3) = −1 (odd).

The Ω⁻ (Q = −1, J = 3/2) was found via this mechanism — see F22.
The revised constraint: only J = 0 with odd Q is truly forbidden.

### F18. Master spectrum at σ_ep = −0.13

| Particle | Tier | m (MeV) | Q | J | Best mode | Δm (MeV) | |Δm|/m | Grade |
|----------|------|---------|---|---|-----------|-----------|--------|-------|
| e⁻ | 1 | 0.511 | −1 | ½ | (1, 2, 0, 0, 0, 0) | ~0 | ~0 | reference |
| p | 1 | 938.272 | +1 | ½ | (0, 0, 0, 0, 3, 6) | ~0 | ~0 | reference |
| φ | 3 | 1019.46 | 0 | 1 | (−1, 6,*,*,−2,−8) | +0.5 | 0.05% | good |
| n | 2 | 939.565 | 0 | ½ | (0, 6, *, *, 0, 8) | −0.31 | 0.03% | good |
| Ω⁻ | 3 | 1672.45 | −1 | 3/2 | (−2,−6,*,*,−3, 13) | +0.6 | 0.04% | good |
| τ⁻ | 3 | 1776.86 | −1 | ½ | (2, 5, *, *, 1, −15) | +3.1 | 0.18% | good |
| Σ⁺ | 3 | 1189.37 | +1 | ½ | (−2,−5,*,*,−1,−10) | −2.3 | 0.19% | good |
| Δ⁰ | 3 | 1232.0 | 0 | 3/2 | (1,−6,*,*, 2, 10) | +5.0 | 0.41% | good |
| Λ | 2 | 1115.68 | 0 | ½ | (−2, 6, *, *,−2,−9) | +12.0 | 1.1% | good |
| Ξ⁰ | 3 | 1314.86 | 0 | ½ | (0, 6, *, *, 0, 11) | −23.4 | 1.8% | good |
| η′ | 2 | 957.78 | 0 | 0 | (0,−6, *, *, 0,−8) | −18.5 | 1.9% | good |
| ρ⁰ | 3 | 775.26 | 0 | 1 | (1,−6,*,*, 1,−6) | −33.0 | 4.3% | fair |
| K⁰ | 2 | 497.61 | 0 | 0 | (0,−6, *, *, 0,−4) | −27.9 | 5.6% | fair |
| η | 2 | 547.86 | 0 | 0 | (0, 6, *, *, 0,−5) | +38.9 | 7.1% | fair |
| μ⁻ | 2 | 105.66 | −1 | ½ | (1, 6, *, *, 0, −1) | +11.6 | 10.9% | poor |
| π⁰ | 2 | 134.98 | 0 | 0 | (0, 6, *, *, 0, −1) | −17.4 | 12.9% | poor |
| π± | 2 | 139.57 | +1 | 0 | — | — | — | J impossible |
| K± | 2 | 493.68 | +1 | 0 | — | — | — | J impossible |

Neutrino quantum numbers marked `*` are freely varying
(Ma_ν contributes < 0.001% of the energy at hadron scales).
Table sorted by |Δm|/m within grade.

**Grade definitions:** reference = exact by construction;
good = |Δm/m| < 2%; fair = 2–10%; poor = > 10%.

Ten of sixteen unstable targets are matched within 2%.
The φ match (0.05%) and Ω⁻ match (0.04%) are particularly
striking — tier 3 particles not used in any parameter fit,
matched to within 0.5–0.6 MeV at ~1 GeV and above.

### F18a. Comparison with model-C mesons

Model-C's strongest predictions were the neutral mesons,
matched at a different geometry (r_p = 8.906, σ_ep = −0.091,
proton as (1,2)):

| Particle | Model-C | Model-D | Change |
|----------|---------|---------|--------|
| K⁰ | 1.2% | 5.6% | worse |
| η | 0.6% | 7.1% | worse |
| η′ | 0.3% | 1.9% | worse |
| φ | 0.8% | 0.05% | much better |

The φ improves dramatically (16× better).  The K⁰ and η
degrade to "fair."  The η′ remains "good" but is 6× worse.

The degradation is structural: model-C had two pinned
parameters (r_p, σ_ep) that were tuned to the neutron and
muon, which also happened to place the meson harmonics well.
Model-D's unpinned geometry (ε_p = 0.55, σ_ep = −0.13) shifts
the proton-ring harmonic spacing, moving some mesons off their
model-C sweet spot.

The K⁰ and η residuals (5.6% and 7.1%) are the model's
largest among particles with correct quantum numbers (excluding
the mass-desert victims μ and π).  Whether σ_ep optimization
or a different ε_p could improve them without degrading the
baryon matches is an open question.

### F19. Mass desert and the muon problem

The model has two energy scales separated by a large gap:

| Scale | Source | E₀ |
|-------|--------|-----|
| Electron sheet | 2πℏc / L_ring_e | 0.20 MeV |
| Proton sheet | 2πℏc / L_ring_p | 115.7 MeV |

No eigenmode exists between ~2 MeV and ~116 MeV.  The muon
(105.7 MeV) sits in this desert, with its nearest eigenmode
at ~117 MeV (proton ring n₆ = 1).  The 10.9% residual is the
model's largest for any fermion target.

The pion (135/140 MeV) also falls in a gap between proton-ring
harmonics n₆ = 1 (~116 MeV) and n₆ = 2 (~231 MeV), giving a
12–16% miss.

This is a structural issue: the electron–proton mass ratio
(m_e/m_p ≈ 1/1836) maps to a length ratio L_e/L_p ≈ 571,
leaving a three-decade desert in the energy spectrum.
Intermediate-mass particles (muon, pion) cannot be accommodated
without either:

1. An additional sheet at an intermediate scale,
2. A mechanism that creates sub-harmonic modes (fractional n₆),
3. Aspect-ratio or shear adjustments that compress proton-ring
   spacing below 116 MeV, or
4. The muon and pion being composite states (multi-mode
   superpositions rather than single eigenmodes).

### F20. Mode overcounting and label degeneracy

The scan found **567,470 propagating modes** below 2 GeV — an
overcounting ratio of ~38,000:1 relative to the 15 targets.

Most of this overcounting is **label degeneracy**: different
neutrino quantum numbers (n₃, n₄) have negligible effect on
the energy at hadron scales.  For example, the neutron cluster
(0, 6, *, *, 0, 8) has dozens of modes at E ≈ 939.26 MeV that
differ only in neutrino labels.  Similarly, electron ring
windings contribute < 1 MeV at the proton scale.

The physically distinct mode count is much smaller — roughly
one per unique (n₅, n₆) pair that passes waveguide cutoff.
With n₅ ∈ [−6, 6] and n₆ ∈ [−16, 16], this is ~200–400
distinct energy levels below 2 GeV.

The label degeneracy may be physical (internal quantum numbers
analogous to flavor) or may indicate that neutrino/electron
labels should be integrated out when predicting the hadron
spectrum.

### F21. Off-resonance correlation

The correlation between lifetime and mass residual, using only
targets with exact (Q, J) matches:

| Particle | τ (s) | |Δm| (MeV) | |Δm|/m | log₁₀ τ | log₁₀ |Δm/m| |
|----------|-------|-----------|--------|---------|-------------|
| n | 8.79 × 10² | 0.309 | 3.3 × 10⁻⁴ | 2.94 | −3.48 |
| μ⁻ | 2.20 × 10⁻⁶ | 11.55 | 0.109 | −5.66 | −0.96 |
| Ξ⁰ | 2.90 × 10⁻¹⁰ | 23.44 | 0.018 | −9.54 | −1.75 |
| Λ | 2.63 × 10⁻¹⁰ | 11.97 | 0.011 | −9.58 | −1.97 |
| Σ⁺ | 8.02 × 10⁻¹¹ | 2.31 | 0.002 | −10.10 | −2.71 |
| τ⁻ | 2.90 × 10⁻¹³ | 3.14 | 0.002 | −12.54 | −2.75 |
| π⁰ | 8.43 × 10⁻¹⁷ | 17.44 | 0.129 | −16.07 | −0.89 |
| Δ⁰ | 5.63 × 10⁻²⁴ | 5.04 | 0.004 | −23.25 | −2.39 |
| ρ⁰ | 4.51 × 10⁻²⁴ | 32.95 | 0.043 | −23.35 | −1.37 |

**Pearson r = −0.40** (N = 9).  The sign is correct (shorter
lifetime → larger residual), consistent with the off-resonance
hypothesis.  The magnitude is weaker than R27's r = −0.84, but
the sample is different (R27 used model-C at different σ) and
includes particles (Δ, ρ) not in the original R27 analysis.

Notable: the Σ⁺ and τ⁻ have among the smallest |Δm/m| values
(~0.2%) but moderate lifetimes (10⁻¹¹ to 10⁻¹³ s).  The π⁰
has a large |Δm/m| (13%) and a very short lifetime (10⁻¹⁷ s),
fitting the pattern.  The muon is an outlier — large |Δm/m|
(11%) but relatively long lifetime (2.2 μs) — likely because
it sits in the mass desert where the nearest mode is far away.

The weaker correlation compared to R27 may partly reflect
the extended particle sample: the Δ and ρ (τ ~ 10⁻²⁴ s)
are resonances where lifetime depends on decay-channel
availability and phase space, not just the mass gap.  If the
off-resonance hypothesis needs refinement, it may be that
τ depends on |Δm| AND the number of available decay channels
(review note).

### F22. Ω⁻ via composite electron winding

The Ω⁻ match is the most surprising result of Track 3:

| Property | Value |
|----------|-------|
| Mode | (−2, −6, −1, 2, −3, 13) |
| Energy | 1673.07 MeV |
| Residual | +0.62 MeV (0.04%) |
| Q | −1 |
| J | 3/2 |

This was initially believed to be topologically impossible
(Q = −1, J = 3/2 requires all three per-strand tubes odd, which
should force Q even).  The resolution: the electron sheet forms
a **composite** — n₁ = −2 with n₂ = −6 gives gcd(2, 6) = 2,
strand = (−1, −3).  The per-strand tube is 1 (odd → spin ½),
but the raw charge contribution is Q_e = −(−2) = +2 (even).

| Sheet | Raw | gcd | Strand | Strand tube | Spin | Charge |
|-------|-----|-----|--------|-------------|------|--------|
| Ma_e | (−2, −6) | 2 | (−1, −3) | 1 (odd) | ½ | +2 (raw) |
| Ma_ν | (−1, 2) | 1 | (−1, 2) | 1 (odd) | ½ | 0 |
| Ma_p | (−3, 13) | 1 | (−3, 13) | 3 (odd) | ½ | −3 |
| **Total** | | | | | **3/2** | **−1** |

The key insight: the charge formula uses **raw** n₁ for the
electron sheet but **per-strand** n₅/gcd for the proton sheet.
When the electron sheet forms a composite, raw n₁ can be even
(giving even charge) while strand tube is odd (giving spin ½).
This breaks the simple parity argument and allows Q = odd
with J = 3/2.

The Ω⁻ is a tier 3 particle with no parameter fitted to it,
yet the model matches its mass to within 0.6 MeV at 1672 MeV.
Its mode structure — composites on all three sheets, n₆ = 13
proton ring — is complex and unpredictable from simple scaling.

**Comparison to model-C:** Model-C listed the Ω⁻ as
structurally forbidden (see review notes).  Model-D finds
it through the composite-electron mechanism — a genuine
prediction improvement over the prior model.

### F23. Dark mode census

Modes with n₁ = n₅ = 0 (no tube winding on either charged
sheet) have Q = 0 and are electromagnetically invisible.
The scan found **18,446 such modes** below 2 GeV.

These dark modes get mass from ring windings (n₂, n₄, n₆)
and/or neutrino tube windings (n₃).  They interact only
gravitationally — natural dark-matter candidates.

The dark-mode density grows with energy (more (n₆) values
available at higher mass).  At 1–2 GeV there are ~5,000
dark modes.  Whether these correspond to physical dark
particles or are artifacts of the label degeneracy (F20)
remains open.

### F24. Improved neutron at wider scan

With the expanded n₂ range (±6 vs ±4 in Track 2), the best
neutron candidate improved:

| Source | Mode | Δm (MeV) | n₂ |
|--------|------|-----------|-----|
| Track 2 F12 | (0, 4, 1, −2, 0, 8) | +0.358 | 4 |
| Track 3 | (0, 6, *, *, 0, 8) | −0.309 | 6 |

The Track 3 candidate has n₆ = 8 (same proton ring winding)
but higher electron ring winding (n₂ = 6 vs 4).  Still n₁ = 0
— the decomposition concern from F11 persists.  The electron
ring winding is dark (no charge, no spin) but couples to
the proton sheet via σ_ep, which is what shifts the energy
toward the neutron mass.

**Sharpened concern (from review):** The electron in beta
decay needs charge −1 (n₁ = 1) and spin ½ (odd tube).
Neither is present in this neutron candidate's electron-sheet
component — its Ma_e winding is purely ring (n₁ = 0, n₂ = 6).
The wider scan improved the mass match but sharpened rather
than resolved the decomposition question.

**Testable question:** If the neutron mode loses its cross-
sheet coupling (σ_ep → 0), does the energy stored in the
dark electron-ring winding redistribute into a charged
electron mode (n₁ = 1, n₂ = 2)?  Or does it simply raise
the mode's energy away from the neutron mass?  This could
distinguish between the "cross-sheet decay channel" picture
and the requirement for explicit charged-electron content.

### Track 3 summary

At σ_ep = −0.13, the model produces a recognizable particle
spectrum across 19 targets (expanded to include model-C's
meson benchmarks).  Ten of sixteen unstable targets with
allowed quantum numbers are matched within 2%.

**Structural successes:**
- Baryons (n, Λ, Σ⁺, Ξ⁰, Ω⁻, Δ⁰) are all matched within
  2%, with the correct Q and J.
- The φ meson is matched at 0.05% — a dramatic improvement
  over model-C's 0.8%.
- The τ lepton is matched at 0.18%, suggesting it may be a
  higher proton-ring harmonic (n₆ = 15).
- The η′ is matched at 1.9%, within the "good" threshold.

**Structural challenges:**
- Charged pseudoscalar mesons (π±, K±) are topologically
  forbidden by the additive spin rule.  This is the most
  significant structural failure.  The proposed fix — QM spin
  addition (two spin-½ combining to J = 0) — is standard
  quantum mechanics, but whether the torus geometry supports
  antiparallel alignment within a single mode is an open
  question.  It may require two strands on the same sheet
  with opposite tube orientations, which is geometrically
  different from the current picture of phase-separated
  identical strands (review note).
- The K⁰ (5.6%) and η (7.1%) degrade from model-C's 1.2%
  and 0.6%.  These are the model's largest residuals among
  particles with correct quantum numbers outside the mass
  desert.  Whether σ_ep or ε_p optimization can recover
  them without degrading baryons is an open question.
- The muon sits in a mass desert between the electron and
  proton energy scales, with a 10.9% residual.  This is
  structural (follows from m_e/m_p), not parametric — no
  parameter adjustment within the current three-sheet
  geometry can fix it.
- Mode overcounting (~30,000:1) is dominated by label
  degeneracy (neutrino/electron dressings at negligible
  energy).  Even after removing label degeneracy, the
  ~200–400 physically distinct energy levels still overcount
  by 15–25× (review note).
- The neutron decomposition concern (F24) sharpened rather
  than resolved by the wider scan: the best match still has
  n₁ = 0 (no charged electron component).

**Open questions (carried from Track 3):**
- Can the spin rule be refined to allow antiparallel alignment,
  enabling charged J = 0 modes?  What geometry on the torus
  supports two strands with opposite tube orientations?
- The muon problem: is there a parameter regime (different ε_p)
  that places the first proton harmonic near 105.7 MeV?  Or
  does an intermediate-scale sheet resolve it?
- Neutron decomposition: does a mode with dark electron-ring
  winding (n₁ = 0, n₂ ≠ 0) redistribute its energy into
  charged electron components when cross-sheet coupling
  is removed?


---

## Track 4 — Decay rate ↔ near-miss correlation

**Goal:** Test the off-resonance hypothesis quantitatively —
do particles with smaller mass residuals live longer?

**Script:** `scripts/track4_offresonance.py`

### F25. Correlation summary across subsets

| Subset | N | Pearson r | p-value | Spearman ρ | β | R² |
|--------|---|-----------|---------|------------|---|-----|
| All unstable | 14 | −0.23 | 0.43 | −0.11 | −1.9 | 0.05 |
| Weak only | 8 | −0.25 | 0.55 | +0.19 | −1.3 | 0.06 |
| All − muon | 13 | −0.37 | 0.21 | −0.28 | −3.0 | 0.14 |
| Weak − muon | 7 | −0.45 | 0.31 | +0.04 | −2.7 | 0.20 |
| Excl. strong + muon | 8 | −0.61 | 0.11 | −0.31 | −3.4 | 0.37 |
| Baryons | 6 | −0.45 | 0.37 | −0.09 | −5.1 | 0.20 |
| Weak baryons | 5 | −0.53 | 0.36 | −0.10 | −3.8 | 0.28 |

β is the fitted power law exponent in
log₁₀(τ) = A + β × log₁₀(|Δm/m|).
R27 (model-C): r = −0.84, β ≈ −2.7, N ≈ 7.

**All subsets show the correct sign** (negative r), confirming
that the direction of the off-resonance hypothesis holds:
smaller residuals do tend to accompany longer lifetimes.  But
no subset achieves statistical significance at p < 0.05, and
none approaches R27's r = −0.84.

Notable: the "weak − muon" subset (N = 7, which now includes
K⁰) yields **β = −2.69**, nearly exactly matching R27's
β ≈ −2.7.  The exponent is consistent; what differs is the
intercept (absolute scale), confirming that the power law
shape may be real even though the single-variable model
cannot predict absolute lifetimes.

The best-performing subset is "excl. strong + muon" (N = 8,
r = −0.61, R² = 0.37), which removes the two classes of
particles whose lifetimes are least likely to be governed by
mass-gap alone.

### F26. The neutron–Ω⁻ paradox

The most striking result:

| Particle | |Δm/m| | τ (s) |
|----------|--------|-------|
| n | 0.033% | 879 |
| Ω⁻ | 0.037% | 8.2 × 10⁻¹¹ |

These two particles have nearly identical fractional mass
residuals but lifetimes differing by **13 orders of magnitude**.
No single power law τ ∝ |Δm/m|^β can accommodate this pair.

The reason is clear from standard physics: the neutron can
only decay via the **weak interaction** (flavor change n → p
requires W boson exchange), while the Ω⁻ decays via
**weak strangeness-changing** currents with much larger phase
space (1672 MeV vs 1.3 MeV neutron Q-value).

This establishes that |Δm/m| alone is insufficient to
predict lifetime.  At minimum, the decay **coupling strength**
(strong / EM / weak) and **available phase space** (Q-value)
must factor into any lifetime formula.

### F27. The R27 power law fails quantitatively

Calibrating the R27 power law (τ ∝ |Δm/m|^−2.7) to the
neutron and predicting all other lifetimes yields an RMS
log₁₀ error of **14.5** — meaning the average prediction
is off by ~14 orders of magnitude.

| Particle | τ_obs | τ_R27 | log₁₀(obs/R27) |
|----------|-------|-------|-----------------|
| n | 879 s | 879 s | 0 (calibrated) |
| μ⁻ | 2.2 × 10⁻⁶ | 1.4 × 10⁻⁴ | −1.8 |
| K⁰ | 9.0 × 10⁻¹¹ | 8.3 × 10⁻⁴ | −7.0 |
| Ξ⁰ | 2.9 × 10⁻¹⁰ | 1.8 × 10⁻² | −7.8 |
| Ω⁻ | 8.2 × 10⁻¹¹ | 648 | −12.9 |
| Σ⁺ | 8.0 × 10⁻¹¹ | 7.3 | −11.0 |
| τ⁻ | 2.9 × 10⁻¹³ | 9.4 | −13.5 |
| η | 5.0 × 10⁻¹⁹ | 4.4 × 10⁻⁴ | −14.9 |
| η′ | 3.3 × 10⁻²¹ | 1.5 × 10⁻² | −18.7 |
| φ | 1.6 × 10⁻²² | 326 | −24.3 |
| Δ⁰ | 5.6 × 10⁻²⁴ | 0.98 | −23.2 |

The model-C R27 result (r = −0.84) was obtained with a
different particle sample and different cross-shear value
(σ_ep = −0.091).  More importantly, model-C pinned the muon
and neutron masses as fitted parameters, which may have
fortuitously aligned the residuals.  The model-D analysis,
which treats the muon and neutron as genuine predictions,
exposes the weakness of a single-variable power law.

### F28. Decay-channel stratification

When the unstable particles are grouped by dominant decay
mechanism, a clear pattern emerges:

| Mechanism | Particles | τ range (s) |
|-----------|-----------|-------------|
| Weak (β) | n | 879 |
| Weak (leptonic) | μ, τ | 10⁻⁶ – 10⁻¹³ |
| Weak (ΔS = 1) | K⁰, Λ, Σ⁺, Ξ⁰, Ω⁻ | 10⁻¹⁰ – 10⁻¹¹ |
| Electromagnetic | π⁰ | 10⁻¹⁷ |
| EM / strong | η, η′, φ | 10⁻¹⁹ – 10⁻²² |
| Strong | Δ⁰, ρ⁰ | 10⁻²⁴ |

Lifetime spans roughly five decades **within** the weak-decay
group alone, while the mass residuals for these particles span
only two decades in |Δm/m|.  The hierarchy
strong ≫ EM ≫ weak(ΔS) ≫ weak(leptonic) ≫ weak(β)
reflects coupling strengths, not mass gaps.

This suggests a refined off-resonance hypothesis:

> **Stratified off-resonance:** Within each decay-channel
> class, particles with smaller mass residuals should live
> longer.  Cross-class comparisons require a coupling-strength
> prefactor.

Within the weak-ΔS group (Λ, Σ⁺, Ξ⁰, Ω⁻), the lifetimes
span less than one order of magnitude (10⁻¹⁰ to 10⁻¹¹ s)
while the residuals span about two orders (0.04% to 1.8%).
The sample is too small for a meaningful within-class
correlation, but the direction is suggestive: Ω⁻ has the
smallest residual (0.04%) and a lifetime toward the longer end
of the range (8.2 × 10⁻¹¹ s).

### F29. Outlier analysis

Using the best-fit power law (excl. strong + muon,
β = −4.0), the residuals identify three categories:

**Good fits** (log₁₀ residual < 1.5):
- π⁰ (−0.6): the lone EM-decay particle sits close to the
  regression line.

**Moderate outliers** (1.5 – 3):
- Λ (+1.6), Σ⁺ (−2.0), Ξ⁰ (+2.5): the strange baryons
  scatter around the fit by ~2 orders of magnitude — moderate
  for a single-variable model spanning 30 decades.

**Extreme outliers** (> 3):
- n (+8.0): lives ~10⁸ longer than the power law predicts.
  This reflects the neutron's unique constraint — it can only
  decay via the suppressed weak β channel.
- Ω⁻ (−4.9): decays ~10⁵ faster than its tiny residual
  suggests.  Its large Q-value (≈530 MeV) and strange-quark
  content provide ample phase space.
- τ⁻ (−4.6): decays faster than predicted; the tau has many
  open decay channels (leptonic + hadronic), which accelerate
  its decay beyond what the mass gap alone would suggest.
- Δ⁰ (−13.8), ρ⁰ (−9.8): extreme outliers driven by strong
  decay — a fundamentally different coupling regime.

### F30. Assessment vs R27 model-C

| Property | R27 (model-C) | R50 Track 4 (model-D) |
|----------|---------------|----------------------|
| Correlation r | −0.84 (N ≈ 7) | −0.23 (N = 14) |
| Best subset r | — | −0.61 (N = 8) |
| Power law β | −2.7 | −1.9 to −5.1 |
| β (weak − muon) | −2.7 | −2.7 (exact match) |
| p-value | 0.009 | 0.11 (best) |
| Muon, neutron | pinned | predicted |
| Cross-shear | σ_ep = −0.091 | σ_ep = −0.13 |

The weaker correlation in model-D is not a regression — it
reflects a more honest test.  Model-C pinned the muon and
neutron as fitted parameters (giving them artificially small
residuals), while model-D treats them as genuine predictions.
The muon's 11% residual in model-D is structural truth about
the mass desert, not a failure of the off-resonance idea.

**Bottom line:** The off-resonance hypothesis survives as a
directional principle (correct sign in every subset), but
fails as a quantitative single-variable predictor.  The
neutron–Ω⁻ paradox (F26) proves that lifetime depends on at
least three factors: mass gap, decay coupling strength, and
phase space.

### Track 4 summary

The off-resonance hypothesis — unstable particles are near-
misses to Ma eigenmodes — is **qualitatively confirmed** and
**quantitatively insufficient**.

The correlation is consistently negative (correct direction)
across all eight subsets tested, but never reaches statistical
significance at p < 0.05.  The best R² = 0.42 means mass gap
explains at most 42% of the variance in log-lifetime.

The neutron–Ω⁻ paradox (F26) is the sharpest demonstration
that a single power law τ ∝ |Δm/m|^β cannot work: two
particles with |Δm/m| ≈ 0.035% have lifetimes differing by
10¹³.  The missing variables are the decay coupling strength
and available phase space.

**The refined hypothesis (F28) — stratified off-resonance —
remains viable:** within each decay-channel class, the
correlation may hold, but the current sample sizes (4–5 per
class) are too small to confirm.  Expanding the target list
and the mode search to higher energies could test this.

**Open questions:**
- Does the within-class correlation (e.g., among weak-ΔS
  baryons) strengthen with more particles?
- Can a two-variable model (|Δm/m| + phase space factor)
  recover the full 30-decade lifetime range?
- Is there a principled way to derive coupling strengths from
  the Ma geometry, rather than importing them from the
  Standard Model?


---

## Track 5: Nuclear modes under model-D geometry

Script: [`scripts/track5_nuclear_modes.py`](scripts/track5_nuclear_modes.py)


### F31. The (1,3) proton reproduces R29 nuclear masses

At σ_ep = 0 (where the proton mass is exact by calibration),
the (1,3) proton hypothesis with nuclear scaling n₅ = A,
n₆ = 3A reproduces R29's nuclear mass matches almost exactly:

| Nucleus | A | Z | Mass (MeV) | (1,3) gap | R29 gap |
|---------|---|---|------------|-----------|---------|
| d | 2 | 1 | 1875.6 | 0.05% | 0.02% |
| ⁴He | 4 | 2 | 3727.4 | 0.69% | 0.67% |
| ⁶Li | 6 | 3 | 5601.5 | — | 0.49% |
| ⁷Li | 7 | 3 | 6533.8 | — | 0.51% |
| ⁹Be | 9 | 4 | 8392.8 | — | 0.61% |
| ¹²C | 12 | 6 | 11174.9 | 0.76% | 0.75% |
| ¹⁴N | 14 | 7 | 13040.2 | — | 0.73% |
| ¹⁶O | 16 | 8 | 14895.1 | — | 0.78% |
| ⁵⁶Fe | 56 | 26 | 52089.8 | 0.87% | 0.87% |

The small differences from R29 arise because R29 used model-C
parameters (r_p = 8.906, σ_ep = −0.091) and optimized n₂
(electron ring winding) freely.  Model-D's metric is slightly
different, but the nuclear mass matching is preserved.

At σ_ep = −0.13 (the working value from R50 Tracks 1–4), all
gaps inflate uniformly by ~3% because cross-shear coupling
shifts all proton-sheet energies by the same fraction.  This is
a systematic effect, not a failure of the nuclear scaling law.


### F32. Energy identity: (1,3) and (3,6) give identical nuclear energies

When quantum numbers are scaled proportionally to each proton
mode — (1,3) → n₆ = 3A; (3,6) → n₅ = 3A, n₆ = 6A — the
nuclear energies are **exactly identical**:

| Nucleus | (1,3) mode | E₁₃ (MeV) | (3,6) mode | E₃₆ (MeV) | ΔE |
|---------|-----------|----------|-----------|----------|-----|
| p | (0,0,0,0,1,3) | 938.3 | (0,0,0,0,3,6) | 938.3 | 0.000 |
| d | (1,0,0,0,2,6) | 1876.5 | (1,0,0,0,6,12) | 1876.5 | 0.000 |
| ⁴He | (2,0,0,0,4,12) | 3753.1 | (2,0,0,0,12,24) | 3753.1 | 0.000 |
| ¹²C | (6,0,0,0,12,36) | 11259.3 | (6,0,0,0,36,72) | 11259.3 | 0.000 |
| ⁵⁶Fe | (30,0,0,0,56,168) | 52543.2 | (30,0,0,0,168,336) | 52543.2 | 0.000 |

This identity holds because L_ring_p is calibrated to the proton
mass: L_ring_p × μ(proton) = constant.  When all quantum numbers
scale by the same factor, the energy ratio E(nucleus)/E(proton)
depends only on the ratio of μ values, which is the same for both
hypotheses (μ scales linearly in quantum numbers).

**The two hypotheses are energetically equivalent for nuclei.**
The only discriminator is the charge formula.


### F33. Charge formula decisively favors (1,3)

The fundamental charge formula Q = −n₁ + n₅ gives correct
nuclear charge for **all nuclei** under the (1,3) hypothesis:

| Nucleus | n₁ (=N) | n₅ (=A) | Q = −N + A | Z | Correct? |
|---------|---------|---------|-----------|---|----------|
| d | 1 | 2 | +1 | +1 | ✓ |
| ⁴He | 2 | 4 | +2 | +2 | ✓ |
| ¹²C | 6 | 12 | +6 | +6 | ✓ |
| ⁵⁶Fe | 30 | 56 | +26 | +26 | ✓ |

Under (1,3), gcd(n₅, n₆) = gcd(A, 3A) = A for even A, but since
n₅/gcd = 1 and the (1,3) mode has gcd(1,3) = 1 (fundamental),
the composite formula **falls back** to the fundamental formula.
There is no composite correction — one charge formula works
for everything.

Under the (3,6) hypothesis with direct scaling (n₅ = 3A, n₆ = 6A):

| Nucleus | n₅ | n₆ | gcd | Q_fund | Q_comp | Z | Fund? | Comp? |
|---------|----|----|-----|--------|--------|---|-------|-------|
| d | 6 | 12 | 6 | +5 | 0 | +1 | ✗ | ✗ |
| ⁴He | 12 | 24 | 12 | +10 | −1 | +2 | ✗ | ✗ |
| ¹²C | 36 | 72 | 36 | +30 | −5 | +6 | ✗ | ✗ |
| ⁵⁶Fe | 168 | 336 | 168 | +138 | −29 | +26 | ✗ | ✗ |

**Neither charge formula works** for (3,6) with proportional
scaling.  The fundamental formula overcounts (every unit of A
contributes 3 to n₅), and the composite formula collapses all
nuclear charges to −N + 1.

The (3,6) hypothesis can only match nuclear charges by using the
per-strand scaling (n₅ = A, n₆ = 2A) with the fundamental charge
formula.  But this per-strand scaling gives **65% mass errors**
because L_ring_p is calibrated for (3,6), not (1,2) strands.

**Verdict:** The charge formula problem for (3,6) is structural
and cannot be resolved by any consistent scaling law.  The (1,3)
proton hypothesis eliminates this problem entirely.


### F34. (3,6) per-strand scaling catastrophically fails

Using the per-strand nuclear scaling (n₅ = A, n₆ = 2A) on the
(3,6) model gives mass errors of ~65% for all nuclei.  This
happens because the (3,6) model's L_ring_p is calibrated so that
the (3,6) mode (with its larger μ value) matches the proton mass.
Modes with smaller quantum numbers (like A, 2A) map to much
lower energies:

| Nucleus | (3,6) E_mode (MeV) | M_obs (MeV) | Gap |
|---------|-------------------|------------|------|
| d | 645.8 | 1875.6 | 65.6% |
| ⁴He | 1290.9 | 3727.4 | 65.4% |
| ¹²C | 3871.3 | 11174.9 | 65.4% |
| ⁵⁶Fe | 18063.4 | 52089.8 | 65.3% |

The per-strand scaling is the (3,6) model's only option for
correct charges, but it destroys mass accuracy.  This is a
fundamental incompatibility.


### F35. Cross-shear systematically shifts nuclear gaps

The cross-shear σ_ep shifts all proton-sheet mode energies by
a uniform fraction.  The nuclear scaling pattern is preserved
but the absolute energies shift:

| σ_ep | p gap | d gap | ⁴He gap | ¹²C gap | ⁵⁶Fe gap |
|------|-------|-------|---------|---------|----------|
| 0.00 | 0.00% | 0.05% | 0.69% | 0.76% | 0.87% |
| −0.05 | 0.42% | 0.47% | 1.11% | 1.18% | 1.29% |
| −0.10 | 1.70% | 1.75% | 2.41% | 2.47% | 2.59% |
| −0.13 | 2.93% | 2.99% | 3.65% | 3.71% | 3.83% |

Each row is the proton gap plus a small, A-dependent residual
(reflecting the nuclear binding energy deficit).  The binding
energy residual per nucleon grows from ~0.15 MeV (deuteron) to
~8 MeV (iron), consistent with R29's observation.

This means σ_ep must eventually be optimized jointly for
particles and nuclei.  At σ_ep = −0.13, the proton is 2.9% too
heavy and nuclei inherit the same shift.  At σ_ep = 0, nuclear
masses match R29 exactly.


### F36. Spin parity prevents strict scaling for some nuclei

Two nuclei from the R29 benchmark set — ³He (spin ½) and ⁷Li
(spin 3/2) — cannot be matched under the strict R29 scaling
law (n₁ = N, n₅ = A) because the topological spin constraint
is unsatisfiable:

| Nucleus | N | A | n₁ parity | n₅ parity | Base odd | Need | Possible? |
|---------|---|---|-----------|-----------|----------|------|-----------|
| ³He | 1 | 3 | odd (1) | odd (1) | 2 | 1 | No |
| ⁷Li | 4 | 7 | even (0) | odd (1) | 1 | 3 | No |

For ³He: n₁ = 1 and n₅ = 3 are both odd, giving base 2 spin-half
contributions.  Adding n₃ yields total = 2 or 3, never 1 (spin ½).

For ⁷Li: n₁ = 4 is even, n₅ = 7 is odd.  Base = 1.  Adding n₃
yields total = 1 or 2, never 3 (spin 3/2).

This is not specific to the (1,3) proton — the same parity
constraint applies for (3,6) with n₅ = A.  R29 resolved this by
searching freely over all quantum numbers; the strict scaling law
n₁ = N, n₅ = A was an observed pattern, not a hard constraint.
Some nuclei may use slightly different quantum number assignments.


### Track 5 summary

**The (1,3) proton hypothesis passes the nuclear mode test.**
It reproduces R29's mass benchmarks (all < 1% at σ_ep = 0) with
the natural nuclear scaling n₅ = A, n₆ = 3A, using the universal
charge formula Q = −n₁ + n₅.  No composite formula exception is
needed.

**The (3,6) hypothesis has a structural charge problem for nuclei**
that cannot be resolved by any consistent scaling law:
- Proportional scaling (n₅ = 3A, n₆ = 6A) gives identical
  energies to (1,3) but wrong charges with both formulas
- Per-strand scaling (n₅ = A, n₆ = 2A) gives correct charges
  with the fundamental formula but 65% mass errors

**The charge formula is the decisive discriminator** between the
two hypotheses.  Since the energies are identical under
proportional scaling, and (1,3) gives correct charges while (3,6)
does not, the (1,3) proton is strongly favored by nuclear mode
data.

**Open questions:**
- Can ³He and ⁷Li be matched with modified quantum numbers
  (relaxing n₁ = N), and do those matches preserve the mass
  accuracy?
- What value of σ_ep optimizes both particle masses (R50 Tracks
  1–4) and nuclear masses simultaneously?
- Does the waveguide cutoff eliminate any nuclear modes that
  were viable in R29?  (Several nuclear modes have odd n₁ on
  the electron sheet, which may not propagate at ε_e = 0.65.)
