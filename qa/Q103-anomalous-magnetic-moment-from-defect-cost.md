# Q103. Anomalous magnetic moment as defect-cost back-reaction

**Status:** Open — framing
**Related:**
  [`grid/sim-impedance/`](../grid/sim-impedance/) (α as defect cost),
  [`grid/maxwell.md`](../grid/maxwell.md) (flux quantization → bare moment),
  [`primers/alpha-in-grid.md`](../primers/alpha-in-grid.md) (α as impedance mismatch),
  [Q102](Q102-neutrino-neutrality-from-sheet-size.md) (charge threshold),
  R46 (electron filter), R47 (proton filter), R52 (self-field moment)

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

- **R47 (proton filter)** identified (1,3) as the leading
  proton mode hypothesis, which fixes the bare moment via
  the flux quantization theorem (see §6) at 3 μ_N.  The
  measured value 2.793 μ_N is then a small (−6.9%) residual
  rather than a +179% deviation from Dirac.

## 6. The bare/anomaly decomposition (revised picture)

The original framing of Q103 (§§ 1–4) treated the entire
deviation from the Dirac value g = 2 as the "anomaly" to be
explained by defect-cost back-reaction.  The discovery of the
flux quantization theorem in [`grid/maxwell.md`](../grid/maxwell.md)
(§Magnetic flux quantization) reorganizes this picture into
a cleaner two-part decomposition:

### 6.1 The bare moment is topological (from MaSt + GRID)

GRID's flux quantization theorem (the dual of charge
quantization) says that a closed spatial winding of order n₂
encloses n₂ magnetic flux quanta.  The resulting bare
magnetic moment is:

> μ_bare = n₂ × (eℏ / 2m) = n₂ × magneton

This is **derived**, not postulated.  It is the spatial-loop
version of the same gauge holonomy rule that produces charge
quantization.  For the (1,2) electron, n₂ = 2 → 2 μ_B.  For
the (1,3) proton, n₂ = 3 → 3 μ_N.  No calculation, no
geometry parameters — just one integer.

This means MaSt absorbs into its "bare" value what standard
physics calls "internal substructure correction."  The proton's
+179% deviation from Dirac is not an anomaly in MaSt — it is
the n₂ = 3 winding, exact and topological.

### 6.2 The anomaly is dynamical (from S coupling via α)

The remaining residual — the deviation from the topological
bare value — is the genuine "anomaly":

| Particle | Mode | Bare (topological) | Measured | Residual |
|----------|------|-------------------|----------|----------|
| Electron | (1,2) | 2 μ_B | 2.00232 μ_B | +0.116% |
| Proton | (1,3) | 3 μ_N | 2.793 μ_N | −6.9% |

This residual is what S (the GRID lattice) needs to explain.
It is the back-reaction of the defect cost on the circulating
wave — the original Q103 picture, but now applied only to the
small residual rather than to the entire deviation from Dirac.

The electron's residual matches QED's α/(2π) ≈ +0.116%
to the precision of measurement.  The proton's residual
(−6.9%) is at non-perturbative coupling and would need a
much harder lattice calculation.

### 6.3 Standard physics comparison

For the electron, MaSt's "bare = 2 μ_B + S correction =
α/(2π)" is essentially identical to standard QED's
"Dirac = 2 + loop corrections = α/(2π)."  These are two
languages for the same physical process: a charged wave
emitting and reabsorbing field disturbances at coupling α.
MaSt does not add new content for the electron.

For the proton, the comparison is structurally different.
Standard physics computes the proton's full moment via QCD,
treating the deviation from Dirac as evidence of internal
quark/gluon substructure.  MaSt's flux quantization theorem
gets to the same result (within 7%) from a single integer
n₂ = 3.  This is an enormous economy if it is correct.

**The two pictures agree on the answer but disagree on the
mechanism:**

- Standard: three quarks + sea quarks + pion clouds + ...
  → ~2.79 μ_N via lattice QCD
- MaSt: n₂ = 3 closed spatial winding → 3 μ_N exactly,
  with a small residual handled by S coupling

Whether MaSt's mechanism is "correct" depends on whether the
7% residual can actually be derived from the lattice S
coupling at the proton's effective α.

## 7. The three-phase sign hypothesis

The two residuals (electron +0.116%, proton −6.9%) have
opposite signs.  This is unexplained in standard physics —
the electron's anomaly is computed by QED loops, the proton's
by QCD machinery, and there is no general rule connecting
their signs.

R52's central conjecture is that **the sign of the residual
is determined by the topology of the mode's spatial winding**:

- **n₂ = 2 (two-phase mode):** two antinodes 180° apart.  The
  self-field back-reaction is constructive (the fields from
  the two antinodes reinforce at each other's locations).
  Net effect: additive correction (electron +0.12%).

- **n₂ = 3 (three-phase mode):** three antinodes at 120°.
  The self-fields from any two antinodes partially cancel
  at the third's location (analogous to the zero-neutral-
  current property of balanced three-phase electrical
  systems).  Net effect: subtractive correction (proton −7%).

If this rule is real and derivable from MaSt + GRID, it would
be a structurally new piece of physics with no analog in
standard QED+QCD.  It would predict the sign of any future
particle's residual anomaly from its mode topology alone.

### 7.1 What R52 attempted (closed — all negative)

R52 ran five computational tracks attempting to demonstrate
the three-phase sign rule under various consistent sets of
classical-field assumptions:

| Track | Method | Result |
|-------|--------|--------|
| 1 | Classical current-loop integral | Wrong framework (bare moment is topological) |
| 2 | B-field surface integral | Same-sign for both modes |
| 4a | Pairwise antinode Coulomb (point sources) | Same-sign for both modes |
| 4b | Loop mutual inductance (n_ring coaxial loops) | Same-sign for both modes |
| 4c | Continuous self-energy (signed ψ) | Same-sign at r_p; sign flip exists but at r ≈ 25-30, far from physical r_p ≈ 8.9 |

**No classical field calculation reproduces the three-phase
sign rule at the proton's actual aspect ratio.**

The verbal three-phase argument — that n_ring = 3 antinodes at
120° produce destructive interference analogous to balanced
three-phase electrical systems — is intuitive, but the actual
geometry of the self-interaction on a torus does not produce
the predicted cancellation at physical aspect ratios.

A subtle point from track 4c: the sign flip DOES exist at very
large aspect ratios (r ≳ 25), but the physical proton has
r_p ≈ 8.9, well below this threshold.  An initial coarse-grid
scan misleadingly placed the crossover near r_p, but resolution
convergence testing showed this was a discretization artifact.

### 7.2 Status of the three-phase hypothesis

The three-phase sign rule, as a CLASSICAL self-interaction
phenomenon on a torus, is **not supported** by computation.
The hypothesis was an attractive verbal argument but does not
survive quantitative implementation.

The sign rule may still hold under some other mechanism:
- A genuine quantum lattice back-reaction (Track 5,
  lattice-native computation, never attempted)
- Cross-sheet coupling (R45 Track 3, never attempted)
- A non-classical effect not captured by surface integrals

But the simple classical versions tested by R52 do not
reproduce it, and the hypothesis should not be cited as an
established MaSt prediction unless one of the unattempted
approaches succeeds.

### 7.3 Implication for the bare/anomaly decomposition

The clean decomposition (MaSt → bare via flux quantization,
S → anomaly via dynamical correction) survives independently
of the sign rule.  MaSt's bare value of n₂ × magneton is a
solid theorem (§6).  What R52 falsified is the specific claim
that the sign of the residual anomaly can be derived from
mode topology via a classical self-interaction calculation.

The anomalies remain to be computed by S-domain methods (QED
loops for the electron, lattice QCD for the proton), with
MaSt providing the topological baseline.

## 8. Summary

The Q103 picture has evolved:

| Era | Bare moment | Anomaly | Status |
|-----|-------------|---------|--------|
| Original (§§ 1–4) | Dirac value (g = 2) | Entire deviation | Outdated for proton |
| Post-flux-quantization (§ 6) | n₂ × magneton (topological) | Small residual after MaSt baseline | **Current view** |
| With classical sign rule (§ 7) | Same | Sign from classical mode topology | **Falsified by R52** |

**What survives:** MaSt + GRID delivers the bare magnetic
moment via flux quantization (a topological theorem, exact
and free of computation).  This is the n₂ × magneton formula
derived in `grid/maxwell.md` §Magnetic flux quantization, and
it is a real piece of new content.

**What does not survive:** the conjecture that the SIGN of
the residual anomaly can be derived from a classical
self-interaction calculation on the embedded torus.  R52
tested this under five different sets of consistent
assumptions (Tracks 1, 2, 4a, 4b, 4c) and found that none
of them reproduce the predicted sign pattern at the proton's
actual aspect ratio.

The genuinely new MaSt content for the magnetic moment
problem is therefore the **bare value formula**, not the
sign rule.  Magnitudes and signs of the residual anomalies
remain to be computed by S-domain methods (QED for electron,
lattice QCD for proton, possibly cross-sheet dressing for
both).  The sign rule remains a verbal argument that could
be revisited under non-classical mechanisms, but it cannot
be cited as an established prediction.
