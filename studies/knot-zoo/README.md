# Knot Zoo

What torus knots model known particles, and what quantum numbers do
they predict?

## Motivation

The WvM electron model uses a (2,1) torus knot: the photon loops
twice around the major axis for each circuit of the tube, producing
spin ½. This is the simplest closed geodesic with half-integer spin.
But many other torus knots exist — do any of them correspond to other
known particles?

## Key Questions

1. **Fermions (spin ½):** Which (p,q) torus knots give spin ½? Can
   muon and tau be modeled as higher-winding knots on the same torus?
   What sets the mass for each knot?
2. **Bosons (spin 0, 1, 2):** Do any torus knots produce integer spin?
   What about the photon (spin 1), W/Z bosons, or the Higgs (spin 0)?
3. **Charge:** Does the charge derivation (q = e via a/R = 1/√(πα))
   generalize to other knots, or is it specific to (2,1)? Do some
   knots predict fractional charge (quarks)?
4. **Composite particles:** Can baryons (3 quarks) be modeled as
   linked or braided knots? What about mesons (quark-antiquark)?

## Approach

Start with a systematic enumeration of (p,q) torus knots, computing
predicted spin, charge, and any other derivable quantum numbers for
each. Compare against the known particle spectrum.

## Scripts

All scripts require the project virtual environment (`.venv` at the
repo root) and the shared library (`../lib/`). Run from the repo root:

    source .venv/bin/activate
    python studies/knot-zoo/scripts/01_knot_survey.py

| Script | Findings | Description |
|--------|----------|-------------|
| `01_knot_survey.py` | F1 | Enumerates (p,q) torus knots, computes spin and charge predictions. |

## Other Files

| File | Contents |
|------|----------|
| `theory.md` | Framework: torus knots, spin from winding, charge from geometry |
| `findings.md` | Results and open questions |
| `STATUS.md` | Task checklist |
