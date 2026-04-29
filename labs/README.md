# Labs

Proposed physical experiments to test predictions of the Ma
model and related hypotheses.  Each proposal is a self-contained
document describing what to measure, what equipment is needed,
what outcome the model predicts, and what outcome would falsify
it.

These are designs, not results.  None have been performed.

## Conventions

- Each proposal is filed as `L<NN>-slug.md`.
- Proposals reference the specific theoretical prediction they
  test (study finding, paper section, or QA entry).
- Each proposal contains one or more **tracks** — distinct
  experiments or iterations that build on each other within
  the same lab.  Track 1 is typically the simplest test; later
  tracks add complexity, different conditions, or follow-up
  measurements that depend on earlier results.
- Each track states:
  1. **Hypothesis** — the specific claim being tested.
  2. **Predicted outcome** — what the model says should happen.
  3. **Null outcome** — what happens if the model is wrong.
  4. **Procedure** — step-by-step protocol.
- The proposal as a whole also covers:
  - **Equipment** — what is needed across all tracks.
  - **Feasibility** — cost, difficulty, and access requirements.

## Index

| Lab | Tests | Status |
|-----|-------|--------|
| [L00](L00-reiter-replication.md) | Independent replication of Reiter's beam-split coincidence experiments (γ-ray and α-ray) | Proposed — prerequisite |
| [L01](L01-thz-write-read.md) | Can energy be written into and read from Ma_ν modes via THz radiation? | Proposed |
| [L02](L02-threshold-nuclear-loading.md) | Can IR at ~42 μm load energy through the neutrino Compton window to trigger nuclear events in deuterium? | Proposed |
| [L03](L03-scaffold-detection.md) | Can a neutrino scaffold (morphogenetic field) be detected by up-converting its 7 THz emission to visible light? | Proposed |
| [L04](L04-beta-decay-thz-resonance.md) | Can THz radiation at predicted neutrino mode frequencies modify beta decay rates? | Proposed |
| [L05](L05-optical-beat-absorption.md) | Can the ν-sheet coupling channel be detected as anomalous absorption at the predicted neutrino frequencies via optical heterodyne beating? | Proposed |

## Logical sequence for the ν-sheet coupling chain

L05 → L04 → L02 form a progressive chain on the same physics:

1. **L05** — does the ν-sheet coupling channel exist at all?  Optical beat absorption in transparent samples; no radioactives required.  Identifies the correct frequency family.
2. **L04** — can the channel modify a weak transition?  Tritium β-decay rate change at the family frequency from L05; requires tritium handling.
3. **L02** — can the channel trigger fusion?  Far-IR loading of D₂ across the 0.782 MeV threshold; nuclear safety required.

A negative L05 rules out intensity-coupling but leaves field-coupling open for L04.  A positive L05 motivates L04 and L02 directly.
