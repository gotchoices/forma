# Knot Zoo — Concluded

What torus knots model known particles, and what quantum numbers do
they predict?

## Result

### Demonstrated

- Odd tube-windings (p) → fermion; even → boson (topological,
  robust). Only q = 1, 2 give known spin values in the a ≪ R
  limit (F1).
- In the Frenet frame model, only (1,2) produces nonzero charge.
  All other knots yield exactly zero (F3). This assumes a specific
  polarization transport rule.
- On a fixed torus, different knots cannot reproduce the known
  particle mass spectrum (F1).

### Shown algebraically (not physically demonstrated)

- The WvM charge formula maps specific a/R values to fractional
  charges: a/R = n/√(πα) for n = 1, 3/2, 3 gives e, 2e/3, e/3
  respectively (F4). This is algebra, not a physical demonstration
  that quarks are (1,2) knots on different tori.

### Hypothesized (untested)

- The compact dimension reframing: the torus as an extra dimension,
  mass from photon energy, generations as harmonics (F2).
- Three compact dimensions for three charge quanta (F4).

### Questions Raised

This study raises foundational questions about the nature of the
compact dimension(s): what is the space, how does it relate to xyz,
and what determines its shape? See [`../../qa/INBOX.md`](../../qa/INBOX.md).

## Approach

Systematic enumeration of (p,q) torus knots, computing spin, charge,
and mass predictions for each. Comparison against the known particle
spectrum.

## Scripts

All scripts require the project virtual environment (`.venv` at the
repo root) and the shared library (`../lib/`). Run from the repo root:

    source .venv/bin/activate
    python studies/knot-zoo/scripts/01_knot_survey.py

| Script | Findings | Description |
|--------|----------|-------------|
| `01_knot_survey.py` | F1 | Enumerates (p,q) torus knots, computes spin and mass ratio predictions. |
| `02_knot_charge.py` | F3 | Propagates circularly polarized E-field along each knot path, computes charge fractions. |
| `03_charge_geometry.py` | F4 | Tests whether fractional charges emerge from varying a/R (same knot, different torus). |

## Other Files

| File | Contents |
|------|----------|
| `theory.md` | Framework: torus knots, spin from winding, charge from geometry |
| `findings.md` | Results and open questions |
| `STATUS.md` | Task checklist |
