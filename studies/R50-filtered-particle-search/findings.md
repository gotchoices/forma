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
