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

### F11. Neutron candidate found at σ_νp ≈ −0.13

**Best candidate across all sweeps:**

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

The neutron's spin comes from the neutrino sheet, and its mass
comes from the proton ring.  This is structurally different from
model-C's neutron mode (0, −2, 1, 0, 0, 2), which used all three
sheets and derived its proton-scale mass from a mode-C proton at
(1, 2) with r_p = 8.906.

### F12. σ_ep also produces a neutron candidate

A second candidate appears in the σ_ep sweep:

| Property | Value |
|----------|-------|
| Mode | (0, 4, 1, −2, 0, 8) |
| Energy | ~939.2 MeV (varies with σ_ep) |
| Minimum residual | 0.358 MeV |
| Cross-shear | σ_ep ≈ −0.130 |
| Sheets active | Ma_e + Ma_ν + Ma_p |

This three-sheet mode gets its spin from Ma_ν (n₃ = 1, odd tube),
its mass from Ma_p ring (n₆ = 8), and its σ_ep coupling from
Ma_e ring winding (n₂ = 4).  The electron ring winding is what
allows σ_ep to shift the energy — without it, the electron-proton
cross-term vanishes.

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

Two viable candidates exist:
- (0, 0, 2, 2, 0, −8) at σ_νp ≈ −0.13  (Δ = 0.25 MeV)
- (0, 4, 1, −2, 0, 8) at σ_ep ≈ −0.13  (Δ = 0.36 MeV)

Both get their spin from the neutrino sheet and their mass from
the proton ring.  The proton tube plays no role in the neutron,
consistent with the neutron having zero charge (no tube winding
on charged sheets).

**Open questions for Track 3:**
- Do the same σ values that produce the neutron also produce
  other known particles (muon, pion, kaon)?
- Is σ_νp or σ_ep the physically preferred coupling?
- The neutron near-miss distance (0.25–0.36 MeV) implies a
  quality factor Q ≈ m/Δm ≈ 3700.  Is this consistent with
  the neutron's 879-second lifetime under the off-resonance
  hypothesis?
