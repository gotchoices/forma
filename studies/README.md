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

- `toroid-series/` — Can a series correction to the WvM charge
  estimate, based on nested toroidal sub-dimensions, converge to the
  measured electron charge?

## Future Study Ideas

- **Alternative field-distribution models for WvM charge.** The WvM
  charge estimate (q ≈ 0.91 e) relies on simplifying assumptions
  (homogeneous field, spherical cavity, specific charge radius). A
  study could explore whether more realistic field distributions close
  the 9% gap without requiring sub-structure.
