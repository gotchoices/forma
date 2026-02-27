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

`QUESTIONS.md` is the research question queue — open questions that
arise during studies. Review it when closing a study to decide what
to investigate next.

`answers/` contains standalone answers to questions that don't
warrant a full study. Each file is named `A<N>-<topic>.md` matching
the question ID in `QUESTIONS.md`. These are referenced by link from
the Answered section of `QUESTIONS.md`.

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

(none)

## Concluded Studies (chronological)

1. **`toroid-series/`** — Can a geometric series of nested toroidal
   sub-dimensions correct WvM's ~9% charge deficit? **Null result:**
   the deficit is an artifact of geometric approximations, not a robust
   target for series correction. Spawned `toroid-geometry/`.

2. **`toroid-geometry/`** — What effective geometry reproduces q = e?
   **Algebraic result:** a/R = 1/√(πα) ≈ 6.60 (inverting the WvM
   charge formula). Whether this geometry is physically realized or
   can be derived independently remains open. Spawned `knot-zoo/`.

3. **`knot-zoo/`** — What torus knots model known particles?
   **Demonstrated:** in the Frenet frame model, only (1,2) produces
   charge. **Algebraic:** the WvM formula maps specific a/R values
   to fractional charges. **Hypothesized:** compact dimensions,
   mass from photon energy. Raises foundational questions.

## Future Study Ideas

- **Compact dimension and mass spectrum.** Hypothesis: the torus is
  a fixed compact extra dimension. If so, the photon follows a
  geodesic (no confining force needed) and its energy determines the
  particle mass. This is untested — the study would formalize the
  hypothesis and check it against Kaluza-Klein theory. Two sub-models:
  - *Shared dimension:* All particles on one torus. Harmonics give
    the mass spectrum. Test: are m_μ/m_e ≈ 207 and m_τ/m_e ≈ 3477
    close to integers? (They are not — so the simplest version
    likely fails.)
  - *Per-particle dimensions:* Separate compact dimensions for
    leptons and quarks. More free parameters, fewer predictions.
  This study would also need to address whether the confinement
  problem is truly eliminated or merely reframed.

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
