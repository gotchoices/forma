# Knot Zoo — Concluded

What torus knots model known particles, and what quantum numbers do
they predict?

## Result

**Only the (1,2) knot matters.** It is the only torus knot that
produces net electric charge (F3). Different particles are not
different knots — they are the same (1,2) knot on compact dimensions
with different aspect ratios (F4). The winding determines spin; the
geometry determines charge; photon energy determines mass.

### Key Findings

- Odd tube-windings (p) → fermion; even → boson. Only q = 1, 2
  give physically known spins (F1).
- Varying the knot winding does NOT produce fractional charges —
  all knots except (1,2) yield exactly zero charge (F3).
- Fractional charges (1/3, 2/3 for quarks) emerge from different
  torus aspect ratios: a/R = n/√(πα) for n = 1, 3/2, 3 (F4).
- Mass comes from photon energy, not topology — generations are
  energy levels on the same compact dimension (F2).

### Questions Raised

This study raises foundational questions about the nature of the
compact dimension(s): what is the space, how does it relate to xyz,
and what determines its shape? See `../QUESTIONS.md`.

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
