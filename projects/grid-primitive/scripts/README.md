# scripts/ — Numerical fail-fast tests for grid-primitive

Numerical tests that confront the cylinder primitive's predictions with specific scalings — fastest path to confirming or falsifying the project's load-bearing bets, in advance of full mathematical derivation.

## Style

These scripts follow the spirit of [grid/sim-gravity-2/](../../../grid/sim-gravity-2/): focused, single-purpose Python scripts that each answer one specific question. Output goes to `output/` (created if absent). Each script's docstring explains what it tests, what it does not, and how to interpret results.

## Available scripts

### `sim-defect-gravity.py`

The first fail-fast test for theory 7 of [../README.md](../README.md). Question:

> *Does the cylinder primitive's 2D stress vector field on a 2D lattice produce a 1/r force law (the 2D analog of gravity), or does it produce 1/r² (the elastic spring-lattice failure mode of [grid/sim-gravity/](../../../grid/sim-gravity/))?*

**Method.** Static (T = 0) Green's-function-style test. Pin a circular inclusion at the center of an N×N lattice, solve for the equilibrium 2-component stress vector field, and check whether |ψ(r)| decays logarithmically (consistent with a 2D Laplacian Green's function and a 1/r force law) or follows some other power law.

**Run.**
```
cd projects/grid-primitive/scripts
python sim-defect-gravity.py
```

**Output.**
- `output/field-and-decay.png` — field visualization and radial-decay plot with both log-fit and power-fit overlaid
- `output/result.txt` — fit parameters and a one-line verdict

**What this script tests.**
The static, kinematic regime of the cylinder primitive. A logarithmic decay confirms that the lattice is *kinematically compatible* with 2D entropic gravity (the right Green's function structure). A 1/r² decay, or any non-logarithmic decay, falsifies theory 7 outright (independent of the entropy mechanism).

**What this script does NOT test.**
- Finite-temperature entropy (the actual *entropic* contribution to the force). The static result captures only the linear Green's function — see `sim-entropy-shadow.py` below.
- Whether the coefficient matches GRID's ζ = 1/4. That is a coefficient question; the static test is a scaling question.
- Topological-defect statistics (BKT, vortex–antivortex condensation). Those require a constrained nonlinear sigma model, deferred to a future script.

### `sim-entropy-shadow.py`

The thermal follow-up to `sim-defect-gravity.py`. Same lattice setup, but now run heat-bath Monte Carlo at temperature T to sample the Gaussian field and measure the *variance shadow* — the pattern of reduced fluctuations near the pinned inclusion.

Direct analog of [grid/sim-gravity-2/](../../../grid/sim-gravity-2/)'s entropy-shadow test, with the cylinder primitive's 2-component stress vector replacing sim-gravity-2's mode tower.

**Run.**
```
cd projects/grid-primitive/scripts
python sim-entropy-shadow.py
```

**Output.**
- `output/entropy-shadow.png` — mean-field map, variance map, and radial-decay fits for both
- `output/entropy-shadow-result.txt` — fit parameters and verdict

**What this script tests.**
At finite T, does the cylinder primitive's stress vector field show the variance reduction (entropy shadow) around the inclusion that gives an entropic 1/r force in 2D — the signature that sim-gravity-2 verified for its mode-tower model? A logarithmic decay of both the mean field and the variance is the pass criterion; this confirms the kinematic + entropic structure of theory 7 in the linear-Gaussian regime.

**What this script does NOT test.**
- Topological-defect (vortex) statistics. Those require constraining ψ to a manifold (e.g., |ψ| = const, the 2D XY model) where vortices are topologically protected. The linear theory tested here has no such protection; defect-style entropy contributions are deferred to a future BKT-specific script.
- Coefficient matching to ζ = 1/4. That requires careful normalization not handled here.

The verdict logic uses the sim-gravity-2 fit window (r up to ~0.45 × half-box) to avoid contamination from the outer Dirichlet boundary, which suppresses fluctuations and creates a non-monotonic profile artifact at large r.

### `sim-two-body.py`

Direct measurement of the force law between two pinned inclusions on the cylinder-primitive lattice. Where `sim-defect-gravity.py` infers a 1/r force from the logarithmic decay of a single inclusion's field, this script computes `E_int(r) = E_total(r) − E_self_1 − E_self_2` directly across a sweep of separations, fits log(r), and verifies that r·F(r) is asymptotically constant.

**Run.**
```
cd projects/grid-primitive/scripts
python sim-two-body.py
```

**Output.**
- `output/two-body.png` — interaction energy, force magnitude, r·F, and ΔE vs log(r) plots
- `output/two-body-result.txt` — fit parameters, force diagnostics, and verdict

**What this script tests.**
The most direct demonstration of a 2D-Coulomb / 2D-gravity force law. Sweeps both like-charge (both inclusions pinned to ψ = (1, 0)) and unlike-charge (one to (1, 0), other to (−1, 0)) configurations. Like-charge result is the cleaner test, since same-sign image charges in the Dirichlet boundary act symmetrically; unlike-charge has stronger boundary-image contamination at large separations.

A like-charge log fit with R² > 0.95 and r·F asymptotically constant confirms F ∝ 1/r — the 2D entropic-gravity force scaling.

## Sequence

1. `sim-defect-gravity.py` — static (T = 0) check that a single inclusion's field decays logarithmically (Green's function structure → 1/r force scaling).
2. `sim-entropy-shadow.py` — finite-T check that thermal fluctuations show the expected variance shadow around an inclusion (entropic 1/r scaling).
3. `sim-two-body.py` — direct force-vs-separation measurement, confirming F ∝ 1/r between two embedded "particles."
4. *(future)* BKT / topological-defect script — testing whether nonlinear constraints supply additional entropy structure beyond the linear Gaussian regime, and whether the coefficient matches ζ.

If 1, 2, and 3 pass, theory 7 has cleared its kinematic, linear-thermal, and direct-force-law hurdles. The full match to Jacobson's ζ = 1/4 awaits step 4.
