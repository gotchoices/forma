# R43: Weinberg angle from cross-sheet geometry

**Status:** Framed — ready to compute.
**Questions:** Q96 §10.2
**Type:** compute
**Depends on:** R26 (three-sheet architecture, σ parameters),
R34 (midpoint coupling), R19 (shear-charge formula)

---

## Motivation

The Weinberg angle θ_W is the electroweak mixing angle.
It determines how the electromagnetic and weak forces
blend:

<!-- sin²θ_W ≈ 0.231 -->

| Quantity | Value |
|----------|-------|
| sin²θ_W | 0.2312 ± 0.0002 (at m_Z) |
| cos θ_W | 0.8815 |
| M_W / M_Z | cos θ_W = 80.4 / 91.2 = 0.882 |

In the Standard Model, sin²θ_W is a free parameter — it
is measured, not derived.  It determines the ratio of the
SU(2) coupling g to the U(1) hypercharge coupling g':

<!-- tan θ_W = g' / g -->
$$
\tan\theta_W = \frac{g'}{g}
$$

**The question:** in MaSt, where forces arise from field
coupling on compact geometry rather than from gauge groups,
does sin²θ_W emerge from the ratio of cross-sheet coupling
to within-sheet coupling?

---

## The MaSt interpretation

In MaSt (Q96), forces at different distance scales are the
same electromagnetic interaction seen from different vantage
points:

| Scale | Coupling | SM name |
|-------|----------|---------|
| r >> λ_C | α ≈ 1/137 (through Compton window) | Electromagnetic |
| r ~ λ_C | ~1 (direct torus overlap, no window) | Strong |
| Cross-sheet | σ² (inter-sheet mode coupling) | Weak |

The weak force is the cross-sheet coupling: how strongly
a mode on Ma_e interacts with modes on Ma_p or Ma_ν.
The electromagnetic force is the within-sheet projection
through the Compton window (strength α).

If the Weinberg angle is the ratio of these two paths:

<!-- tan θ_W = α / σ² or some function of α and σ -->

then sin²θ_W is determined by the geometry of the three
sheets — their radii, shears, and coupling parameters —
with no new free parameters.

---

## What to compute

### Track 1: Cross-sheet coupling ratio

The σ cross-shear parameters describe how strongly modes
on different sheets couple.  From R26:

| Parameter | Meaning |
|-----------|---------|
| σ_ep | Electron-proton cross-sheet coupling |
| σ_eν | Electron-neutrino cross-sheet coupling |
| σ_pν | Proton-neutrino cross-sheet coupling |

The Weinberg angle relates the EM and weak coupling
strengths.  In MaSt terms:

- **EM coupling** (within-sheet, projected through window):
  strength = α
- **Weak coupling** (cross-sheet): strength = f(σ)

The simplest hypothesis:

<!-- sin²θ_W = α / (α + σ²) -->
$$
\sin^2\theta_W = \frac{\alpha}{\alpha + \sigma_{\text{eff}}^2}
$$

where σ_eff is an effective cross-sheet coupling derived
from the σ parameters.  Solving for the target:

sin²θ_W = 0.231 → σ_eff² = α × (1 − 0.231) / 0.231
                           = (1/137) × 3.33
                           ≈ 0.0243

So σ_eff ≈ 0.156.  Is this consistent with the σ values
from R26?

### Track 2: W and Z masses from coupling barriers

If W and Z are cross-sheet resonances (Q96 §6), their
masses should be related to the energy barrier for
cross-sheet coupling.  The barrier height sets the mass;
the ratio M_W/M_Z = cos θ_W follows from how the
electromagnetic (within-sheet) and weak (cross-sheet)
channels mix.

Compute:
1. The cross-sheet coupling energy for each pair of
   sheets (Ma_e ↔ Ma_p, Ma_e ↔ Ma_ν, Ma_p ↔ Ma_ν)
2. The resonant energy of the coupled-sheet oscillation
3. Compare to M_W = 80.4 GeV and M_Z = 91.2 GeV

### Track 3: Alternative — geometric ratio

The Weinberg angle might emerge from a purely geometric
ratio.  Candidates:

| Ratio | Value | sin²θ_W equiv |
|-------|-------|---------------|
| 1/4 (ζ) | 0.250 | 8% off |
| 3/13 (3 sheets / 13 modes?) | 0.231 | exact |
| α × 137/4.33 | 0.231 | tautological |
| r_e / (r_e + r_p + r_ν) | needs values | geometric |
| Area_e / Area_total | needs values | geometric |

Compute the sheet area ratios and any other geometric
quantities that give dimensionless numbers near 0.231.

---

## Inputs (all from existing studies)

| Input | Source | Value | Status |
|-------|--------|-------|--------|
| α | Measured (A6) | 1/137.036 | Fixed |
| r_e (electron ring radius) | R2, R19 | 6.6 | Fixed |
| r_p (proton ring radius) | R20, R26 | 8.906 | Fixed |
| s_e (electron shear) | R19 | 0.01029 | Fixed |
| s_p (proton shear) | R19 | 0.00764 | Fixed |
| σ_ep | R26 F67 | 0.038 | **Pinned** by neutron mass |
| σ_eν | R26 F72 | < 0.05 | **Constrained** by ν Δm² ratio |
| σ_pν | R26 | free | Unconstrained |
| Ma_ν geometry | R26, R38 | (from findings) | Fixed |

No new free parameters.  Everything is determined by
existing particle mass fits.

### Consistency test

This study is not just a calculation — it is a **three-way
consistency test**.  Three independent experiments constrain
the same cross-shear parameters:

1. **Neutron mass** → σ_ep ≈ 0.038 (R26 F67)
2. **Neutrino Δm² ratio** → σ_eν < 0.05 (R26 F72)
3. **Weinberg angle** → some f(σ_ep, σ_eν, σ_pν, α) = 0.231

If the Weinberg constraint is satisfied AT the existing
pinned values (or pins the free σ_pν without conflicting),
the framework passes a non-trivial self-consistency check:
three unrelated measurements are explained by one geometry.

If the Weinberg constraint CONFLICTS with the existing pins,
the failure mode reveals where the model breaks — either
the symmetric-σ approximation is too crude, or the mixing
angle doesn't arise from cross-sheet coupling in this way.

---

## Success criteria

| Outcome | What it means |
|---------|---------------|
| sin²θ_W within 5% of 0.231 | Strong: the Weinberg angle is geometric |
| sin²θ_W within 20% | Promising: right ballpark, mechanism plausible |
| sin²θ_W off by > 50% | The simple ratio hypothesis fails; more complex mechanism needed |
| M_W/M_Z ratio matches cos θ_W | Very strong: both the angle and the mass ratio are geometric |

---

## Connection to the broader question

If sin²θ_W emerges from cross-sheet geometry, it means:

1. **SU(2)×U(1) is an effective description**, not a
   fundamental symmetry.  The gauge group structure is
   what you see when you describe cross-sheet coupling
   in the language of quantum field theory.

2. **The Higgs mechanism is geometric.**  Electroweak
   symmetry "breaking" is the statement that cross-sheet
   coupling has a specific strength relative to within-
   sheet coupling.  The "broken symmetry" was never a
   symmetry of the geometry — it was an artifact of
   describing the geometry in gauge-theory language.

3. **One fewer mystery.**  The SM has sin²θ_W as a free
   parameter.  If MaSt derives it from geometry, that's
   one fewer input constant.

---

## Files

| File | Purpose |
|------|---------|
| `README.md` | This document |
| `scripts/` | Computation scripts (to be created) |
| `findings.md` | Results (to be created) |

---

## Dependencies

numpy, scipy (all in project `.venv`)
Existing lib: `studies/lib/ma.py`, `studies/lib/ma_model.py`
