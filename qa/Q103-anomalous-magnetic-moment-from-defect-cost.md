# Q103. Anomalous magnetic moment as defect-cost back-reaction

**Status:** Open — framing
**Related:**
  [`grid/sim-impedance/`](../grid/sim-impedance/) (α as defect cost),
  [`primers/alpha-in-grid.md`](../primers/alpha-in-grid.md) (α as impedance mismatch),
  [Q102](Q102-neutrino-neutrality-from-sheet-size.md) (charge threshold),
  R46 (electron filter), R47 (proton filter)

---

## 1. The observation

The electron's magnetic moment is not exactly 2 Bohr
magnetons.  It is slightly larger:

> g = 2.00231930436256 ± 0.00000000000035

The anomalous part (g − 2)/2 ≈ 0.001162 is one of the most
precisely measured quantities in physics.  QED computes it
as a perturbation series in α:

> (g − 2)/2 = α/(2π) + O(α²) ≈ 0.001162

The leading term α/(2π) accounts for >99.8% of the anomaly.
Higher-order terms (α², α³, ...) refine the prediction to
12-digit agreement with experiment.

The proton's magnetic moment is 2.7928 nuclear magnetons —
far from the Dirac prediction of 1 nuclear magneton for a
spin-1/2 particle, and far from whatever the bare mode
prediction would be.  The anomaly is order-1, not order-α.

## 2. The GRID interpretation

In the GRID + MaSt framework, a particle is a standing wave
on a 2D sheet (torus) whose phase winds through 2π around
the tube.  This winding is a topological defect in the
ambient 3D lattice.  The defect cost — the fraction of
energy that leaks into the ambient lattice as Coulomb field
— is α.

The same coupling that creates the charge also perturbs the
magnetic moment:

- The standing wave circulates on the torus in a pattern
  set by the mode numbers (n₁, n₂).
- The bare magnetic moment comes from the ring windings:
  for the electron (1,2), the bare moment is 2.
- But the wave doesn't circulate in a perfect pattern.
  The coupling to the ambient lattice (strength α)
  distorts the current distribution.
- The distortion adds a correction to the moment
  proportional to α.

**The anomalous magnetic moment is the back-reaction of the
defect cost on the wave that created the defect.**

The Coulomb field (energy αmc²) exerts a back-reaction on
the circulating wave, slightly reshaping the current loop.
The wave "overshoots" by α/(2π) because the field it
radiates into the ambient lattice acts back on the source.
The 2π in the denominator is the geometric factor from
integrating the back-reaction over the full tube
circumference.

## 3. Electron vs proton

| Property | Electron | Proton |
|----------|----------|--------|
| Mode | (1,2) | (1,2) or (3,6) — open |
| Sheet size | ~10²² L | ~10¹⁹ L |
| Bare moment | 2 | 2 or 6 — depends on mode |
| Measured moment | 2.00232 | 2.793 |
| Anomaly size | +0.12% | −53% (if bare=6) or +40% (if bare=2) |
| Coupling regime | Perturbative (α ≈ 1/137) | Non-perturbative (strong internal coupling) |

**Electron:** the sheet is large, the phase gradient per
cell is gentle, and the coupling to the ambient lattice is
weak (α ≈ 1/137).  The defect-cost correction is small and
calculable as a power series in α.  The standard QED
perturbation series IS this lattice calculation in the
continuum limit.  GRID doesn't add a new computation — it
gives the existing one a physical picture.

**Proton:** the sheet is ~1000× smaller.  The phase gradient
per cell is ~1000× steeper.  At the proton's energy scale
(~1 GeV), α runs to ~1/128, and internal mode overlaps on
Ma_p are strong — this is the regime where the strong force
operates as internal EM (Q95).  The defect-cost corrections
are large and non-perturbative.  The bare mode pattern is
heavily distorted by the coupling, shifting the moment far
from its topological prediction.

This explains the qualitative difference: the electron's
moment is almost exactly the bare value (small perturbative
correction), while the proton's moment is far from bare
(large non-perturbative correction).  Same physics
(junction coupling perturbs the circulating current),
different regime.

## 4. What this predicts

- The electron's anomalous moment should be exactly the
  QED series in α — which it is, to 12 digits.  GRID adds
  no new prediction here; it reinterprets the known result.

- The proton's anomalous moment should be computable from
  the full non-perturbative mode structure of Ma_p.  This
  requires solving the standing wave problem on the proton
  sheet with all internal couplings — a much harder
  calculation than the electron case.

- If the proton is a (3,6) mode, the bare moment is 6 and
  the coupling reduces it to 2.793 (a 53% reduction).  If
  it is a (1,2) mode, the bare moment is 2 and the coupling
  increases it to 2.793 (a 40% increase).  The direction
  and magnitude of the anomaly may help distinguish the two
  hypotheses.

## 5. Connection to other work

- **QED perturbation theory** computes (g−2)/2 as a series
  in α.  This is standard physics and is not claimed as a
  GRID result.  GRID's contribution is the physical picture:
  the series computes the back-reaction of the defect cost
  on the circulating wave.

- **Lattice QCD** computes the proton's magnetic moment
  from first principles (with significant computational
  effort).  If MaSt's mode structure on Ma_p can reproduce
  this result from the torus geometry, that would be a
  significant validation.

- **R47 (proton filter)** may help determine whether the
  proton is (1,2) or (3,6), which would fix the bare
  moment and clarify the direction of the anomaly.
