# Studies

Each subfolder contains a self-contained investigation with its own
documentation and computational work.

## Study Folder Convention

Every study folder should contain these files:

| File | Purpose | Update cadence |
|------|---------|----------------|
| `README.md` | Brief summary of the study's question, approach, and scope. | Rarely — when scope changes. |
| `theory.md` | The "paper": hypotheses, mathematical framework, testable propositions. | Infrequently — when the theory itself is revised (new propositions, corrected math, scope shifts). |
| `findings.md` | Lab notebook: chronological log of what each experiment tried, what it found, and what it means for the next step. | After each script run or analysis. |
| `STATUS.md` | Bare checklist of tasks — completed, in progress, planned. | Ongoing, as tasks start and finish. |
| `scripts/` | Computational work. Each script is numbered (`01_`, `02_`, …) and references the findings entry and theory section it bears on. | As needed. |

Shared code lives in `lib/` at this level (not inside individual
studies) since physical constants and common utilities are universal.

### Guidelines

- **`theory.md` is slow-moving.** Don't update it after every script
  run. Revise it when a finding forces a change to the hypotheses,
  framework, or propositions.
- **`findings.md` is the running narrative.** Each entry gets a
  sequential ID (F1, F2, …), names the script, states the result, and
  notes implications. This is the place to record both positive and
  null results.
- **`STATUS.md` is a checklist, not prose.** Keep entries short. Move
  detail to `findings.md`.
- **Scripts are self-documenting.** Each script's docstring should
  reference the `theory.md` section and `findings.md` entry it
  corresponds to.

## Active Studies

- `knot-zoo/` — What torus knots model known particles? Systematic
  enumeration of (p,q) knots with predicted spin, charge, mass, and
  fermion/boson classification.

## Concluded Studies

- `toroid-geometry/` — What effective geometry reproduces q = e?
  **Answer:** a/R = 1/√(πα) ≈ 6.60 — the field extends 1/√(πα) orbital
  radii from the geodesic, filling a nearly spherical volume. Whether
  this can be derived independently of demanding q = e remains open.

- `toroid-series/` — Can a geometric series of nested toroidal
  sub-dimensions correct WvM's ~9% charge deficit? **Null result:**
  the deficit is an artifact of geometric approximations, not a robust
  target for series correction. Spawned `toroid-geometry/`.

## Future Study Ideas

- **Torus knot particle zoo.** The (2,1) torus knot gives spin ½ for
  the electron. What other knots properly model known or expected
  particles? Could (2,3) or (2,5) correspond to muon and tau (with
  winding complexity setting the mass)? What about bosons, baryons,
  or hypothetical particles? Systematic enumeration of knot types
  and their predicted quantum numbers.

- **α from geometry.** Study 2 showed a/R = 1/√(πα) gives q = e.
  This is algebraically exact but derived by demanding q = e. Can
  an independent physical argument (boundary matching, energy
  minimization, self-consistent confinement) select this ratio,
  thereby deriving α from geometry? All three candidate routes
  require solving the guided-wave profile — a substantial
  electromagnetic calculation.

- **Precession of the torus axis.** The (2,1) orbit produces an
  axially symmetric field, not a spherically symmetric one (~2.5%
  quadrupole at the horizon). If axis precession eliminates this
  anisotropy, what drives the precession — classically (spin-orbit
  coupling, self-interaction, Thomas precession analog) and
  mathematically (is it a natural consequence of the equations of
  motion in curved self-generated geometry)?

- **Confinement mechanism.** What physical mechanism (nonlinear vacuum,
  compactified dimension, self-gravity) confines the photon to the
  toroidal geodesic?
