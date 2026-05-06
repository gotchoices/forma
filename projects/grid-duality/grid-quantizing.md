# Quantizing the lattice: from real values to bits

**Status:** Hypothesis and experimental program. Not yet implemented.
**Scope:** Asks whether the chapter-4 winning model (Scattering on a 2D hex lattice) continues to work when the per-cell state is quantized — first to integers, eventually to a single bit per cell — at sufficient lattice resolution.
**Relation to chapters:** Side-document. Does not change the chapter-4 verdict. Outlines a deeper-substrate question: what does the lattice look like if its cells are taken seriously as the smallest informational units?

---

## 1. Why ask this question

Chapter 4 selected Scattering as the model that best reproduces grid's wave-propagation and static-field behavior. The model uses **real-valued amplitudes** at each end of each edge, with the unitary scattering matrix S = (2/N)·J − I applied at every vertex per clock tick.

The substrate underlying GRID's framework, however, is informational. Jacobson's argument (and the entropy-emergence story in [grid/sim-gravity-2](../../grid/sim-gravity-2/)) treats each lattice cell as carrying a finite information capacity — ζ = 1/4 bit per cell in 3D, ζ = 1/3 in 2D under Model B counting. This is **not** an averaged or coarse-grained quantity; it is what the cell holds at the substrate level.

If the substrate cells are literal information primitives, then real-valued amplitudes are an effective theory rather than the fundamental dynamics. The fundamental dynamics should be in terms of bits (or small fixed alphabets). This document asks: under what conditions does Scattering with quantized state recover the same observable behavior as Scattering with real state?

The answer is that this is exactly the regime studied for decades under the names *lattice gas automata* and *lattice Boltzmann methods*. There is established mathematics and substantial computational evidence. This document collects what is known, applies it to the project's setup, and proposes a concrete experiment.

---

## 2. Recap: the working continuous model

[Chapter 4](04-model-comparison.md) selected Scattering as the lattice's dynamics. Reframed as a transmission-line network (see [review.md](review.md) §"Final suggestions"):

- Each **edge** is a 1D extended object with two ends. Each end carries a real-valued amplitude.
- Each **vertex** is a junction. It enforces voltage continuity (all incident lines see the same potential) and current conservation (Kirchhoff). The scattering matrix S = (2/N)·J − I is the unique solution to these constraints at an N-port equal-impedance junction.
- The **clock** has two phases (per [review.md](review.md)): nodes scatter (Phase 1), edges swap their end values (Phase 2). One full cycle propagates information by one edge length.

Total state per 2D hex unit cell: 6 real values (3 edges per A-vertex × 2 ends). The model passes the test bench cleanly: exactly unitary, exactly non-dispersive at coord 2, matched-impedance scattering to four decimals at coord-3 vertices.

The question of this document: if each of those 6 values per unit cell were not a real number but an **integer in some bounded range** — and eventually a single bit — would the macroscopic tests still pass at sufficient lattice resolution?

---

## 3. The hypothesis

Replace each edge-end's real-valued amplitude with an integer drawn from a finite alphabet of size N:

- **N = ∞** (or N = 2⁶⁴ for floating-point): the current model.
- **N = 256**: 8 bits per cell. Effectively continuous for any practical wavelength.
- **N = 16, N = 4**: a few bits per cell. Quantization noise becomes visible at the lattice scale; macroscopic tests still pass after coarse-graining.
- **N = 2**: a single bit per cell. The most extreme quantization. State per 2D hex unit cell drops to 6 bits.

The hypothesis: there exists a function s(N) — the lattice scale factor at which the test bench passes at fixed target accuracy — such that for any N ≥ 2, *some* lattice resolution s(N) suffices to recover the continuous test results to that accuracy. Equivalently: **the smallness of cells compensates for the low resolution per cell**, with the compensation rate set by quantization-noise scaling laws.

If true, the lattice's physical content is fundamentally bit-valued, and the continuous Scattering model is its effective theory at scales much larger than the cell spacing. This is a structural claim about the substrate, not a refutation of chapter 4.

---

## 4. Prior art

The hypothesis is not novel. Three lines of work establish that binary cellular automata can produce continuous physics in the macroscopic limit.

### 4.1 Lattice gas automata (FHP and predecessors)

In 1973, Hardy, de Pazzis, and Pomeau introduced the **HPP lattice gas**: a 2D square-lattice cellular automaton where each site holds bits indicating particle presence in each of four directions. Particles propagate to neighbors and collide at sites under deterministic rules that conserve particle count and momentum. HPP recovers fluid dynamics in the continuum limit but suffers from anisotropy due to the square lattice's 4-fold symmetry (real fluids have full rotational symmetry).

In 1986, Frisch, Hasslacher, and Pomeau extended the construction to a hexagonal lattice (**FHP**), whose 6-fold symmetry is sufficient to recover the full Navier-Stokes equations including isotropy. The proof uses the **Chapman-Enskog expansion** to expand the discrete update in powers of the small parameter ε = cell-size / wavelength; the leading-order term is Navier-Stokes, with errors O(ε²).

The FHP result is the canonical demonstration that purely binary cellular automata can produce continuous fluid waves. It is widely understood and replicated.

References: U. Frisch, B. Hasslacher, Y. Pomeau, *Lattice-Gas Automata for the Navier-Stokes Equation*, Phys. Rev. Lett. 56, 1505 (1986). See also S. Wolfram, *Cellular automaton fluids 1: Basic theory*, J. Stat. Phys. 45, 471 (1986) for an independent derivation.

### 4.2 Lattice Boltzmann methods

Lattice Boltzmann (LB) methods, developed in the late 1980s by McNamara, Zanetti, and others, generalize FHP by replacing binary occupation with real-valued probability distributions. The streaming-collision structure is preserved; the state at each site becomes a real-valued vector representing the local Boltzmann distribution. LB methods are now a standard computational tool for fluid dynamics, electromagnetic propagation, and lattice gauge simulation.

For our purposes, LB sits at the *real-valued* end of the spectrum — close to the chapter-4 Scattering model — while FHP sits at the *binary* end. The continuum behavior is the same; what differs is the per-cell precision.

References: G. R. McNamara, G. Zanetti, *Use of the Boltzmann Equation to Simulate Lattice-Gas Automata*, Phys. Rev. Lett. 61, 2332 (1988). Comprehensive review: S. Succi, *The Lattice Boltzmann Equation: For Fluid Dynamics and Beyond*, Oxford University Press, 2001.

### 4.3 Quantum lattice gases and discrete substrates

Building on the FHP / LB framework, quantum lattice gas automata extend the construction to recover quantum field equations including Maxwell's. The general claim is that linear wave equations are recoverable from binary cellular automata at the macroscopic limit, given an appropriate symmetry structure on the lattice.

Independently, 't Hooft and others have proposed that fundamental physics may be a deterministic cellular automaton at the Planck scale, with quantum behavior emerging from coarse-graining. While speculative, this program supplies the philosophical motivation for the question this document asks: **if the substrate is genuinely a binary cellular automaton, what does it look like, and how does the chapter-4 continuous model emerge from it?**

References: J. Yepez, *Quantum Lattice-Gas Model for the Many-Particle Schrödinger Equation in d Dimensions*, Phys. Rev. E 63, 046702 (2001). G. 't Hooft, *The Cellular Automaton Interpretation of Quantum Mechanics*, Springer, 2016.

### 4.4 The holographic principle and Bekenstein bound

Standard results in black-hole thermodynamics (Bekenstein, Hawking) and in the holographic principle ('t Hooft, Susskind) bound the information content of a region of space by a quantity proportional to the region's bounding area in Planck units. The factor of 1/4 in the Bekenstein-Hawking entropy formula is the same 1/4 bit per Planck cell that GRID's axiom A5 uses.

This is the physical anchor for the binary-substrate hypothesis: if information density per Planck area is bounded, the lattice's per-cell capacity at the Planck scale is finite — and small. A few bits per cell is consistent with the Bekenstein-Hawking ratio; a single bit per cell is the most aggressive form of this bound.

References: J. D. Bekenstein, *Black Holes and Entropy*, Phys. Rev. D 7, 2333 (1973). G. 't Hooft, *Dimensional Reduction in Quantum Gravity*, gr-qc/9310026 (1993). L. Susskind, *The World as a Hologram*, J. Math. Phys. 36, 6377 (1995).

---

## 5. The bit-budget trade-off

For the lattice to encode a smooth wave with macroscopic resolution Δ at amplitude A, the **total bit count per macroscopic averaging region** must be sufficient. With M cells per region and log₂(N) bits per cell:

<!-- total bits = M · log₂(N) -->
$$
\text{total bits per region} = M \cdot \log_2 N
$$

Two regimes for how bits-per-cell trade against cells-per-region:

### 5.1 Digital-encoding regime (bits as independent information)

If each cell carries an independent piece of macroscopic information, doubling N doubles the macroscopic bit budget. M scales as 1/log₂(N) for fixed accuracy. This is rare in lattice physics — cells are usually correlated.

### 5.2 Analog-averaging regime (bits as redundant samples)

If cells redundantly encode local field values and macroscopic amplitudes emerge from spatial averaging, quantization noise reduces by √M (central limit theorem). The effective amplitude resolution after averaging is N · √M. To achieve target macroscopic resolution ε:

<!-- M ≥ (1 / (N · ε))² -->
$$
M \geq \left(\frac{1}{N \cdot \varepsilon}\right)^2
$$

That is, **M scales as 1/N²** for fixed ε. Halving the per-cell bit count quadruples the cells-per-region requirement. This is the regime relevant to wave physics on a lattice gas.

### 5.3 Numerical example

For target macroscopic resolution ε = 10⁻⁶ (one part per million):

| N (levels per cell) | bits per cell | M (cells per region) |
|---|---|---|
| ∞ (continuous) | 64+ | ~1 |
| 256 | 8 | ~16 |
| 16 | 4 | ~4,000 |
| 4 | 2 | ~250,000 |
| 2 (binary) | 1 | ~10¹² |

For comparison: a Planck-scale lattice (cell size ~10⁻³⁵ m) has ~10¹⁴⁰ cells per cubic meter, or ~10⁴⁰ cells per (10⁻¹⁰ m)³ ≈ atomic volume. So binary cells achieve ε = 10⁻⁶ resolution at any macroscopic scale of physical interest, with vast margin to spare.

The hypothesis is not that binary works at the scale of the chapter-4 test bench; it works at the scale of the Planck lattice. The chapter-4 lattice (14×14 hex) is far too coarse to test binary directly — but the *scaling law* M ∝ 1/N² is testable at intermediate resolutions.

### 5.4 Locality of the update rule

The "macroscopic averaging region" in §5.1–§5.3 is an **observer concept** — a window over which an analyst computes coarse-grained observables from the lattice's state. The lattice's *dynamics* are strictly local: every vertex update reads from and writes to only the edge-ends directly touching that vertex. Information propagates at exactly one edge per tick, regardless of the per-cell quantization level.

Concretely, per-tick at each vertex:

1. Read the value at each incident edge-end (the end of the edge that touches this vertex).
2. Apply the local rule (Boolean for binary state, scattering matrix for continuous state) to those values alone.
3. Write new values back to those same edge-ends.

No vertex ever reads from another vertex directly, from edge-ends not touching it, or from cells more than one edge away. The locality is the same whether the per-cell precision is 1 bit or 64 bits.

What averaging does is **post-hoc reconstruction**: an analyst takes the bit field over a region of cells and computes its average to recover a coarse-grained wave amplitude. The cells themselves are unaware of the averaging. They simply continue updating locally, like atoms in a fluid that interact only with their immediate neighbors while an experimenter measures the averaged "fluid velocity" from outside.

This is the same separation that holds in standard coarse-grained physics: microscopic interactions are local, macroscopic fields are observer-side reconstructions. Quantizing per-cell precision changes how many cells an observer must average to recover macroscopic resolution; it does not change the locality of the update rule, and it does not change the lattice's signal-speed limit (one edge per tick).

---

## 6. Quantization-noise scaling

The bit-budget argument above assumes the discretization is well-behaved. There are two paths to making this concrete, with different error-accumulation characteristics.

### 6.1 Naive quantization

Start with the continuous Scattering update. After each scatter step, round each (a_fwd, a_bwd) to the nearest representable value in the N-level alphabet. This introduces quantization noise of order 1/N per step.

After T ticks, cumulative error in the wave amplitude scales as:

- O(T / N) if the noise is systematic (correlated across cells/ticks)
- O(√T / N) if the noise is random (independent)

For the project's existing tests (~80–100 ticks) and binary state (N = 2):
- Systematic: cumulative error ~ 50, much larger than the signal.
- Random: cumulative error ~ 5, comparable to the signal.

Neither passes at the chapter-4 lattice resolution. Both improve as the lattice is refined: at scale s = 10 (10× finer than chapter-4's lattice), each macroscopic feature spans ~100 cells, and the per-feature quantization noise reduces by √100 = 10 — bringing the random-noise case into the percent-error range.

This regime is straightforward to implement and gives the cleanest picture of the scaling law.

### 6.2 Lattice-gas-style Boolean rules

The naive approach accumulates noise because rounding is an irreversible non-conservative operation. The FHP / lattice-Boltzmann tradition avoids this by designing **deterministic Boolean update rules** that conserve bit count exactly per scattering event — no rounding, no quantization noise per step. The continuum behavior emerges purely from coarse-graining over many cells, not from any per-step approximation.

For our hex Y-junction, the design problem is: find a Boolean rule mapping the 2³ = 8 input configurations of three incoming bits to 8 output configurations such that:

1. **Bit count is conserved** (energy conservation per junction).
2. **Symmetry is respected** (rotational symmetry of the hex lattice; reflection symmetry across each axis).
3. **The macroscopic average reproduces matched-impedance scattering** (1/9 reflected, 4/9 to each transmission arm) when averaged over many junctions.

Such rules exist; the FHP collision-rule construction is the standard template. The cost is design effort; the benefit is exact reversibility, exact energy conservation, and no compounding noise. This is the more physically natural form of the hypothesis.

For the present document, naive quantization is the recommended starting point. If the scaling law is favorable, lattice-gas-style Boolean rules become the principled refinement.

---

## 7. Experimental design

A two-axis sweep on the existing test bench:

### 7.1 Axes

- **N**: levels per cell. Sweep N ∈ {∞, 256, 64, 16, 4, 2}, including the continuous baseline as N = ∞.
- **s**: lattice scale factor. s = 1 is the chapter-4 lattice (e.g., 14×14 hex for stability tests; 25×25 for static-field tests). s ∈ {1, 2, 4, 8, 16} where s = 2 has cells half as wide and 4× as many cells per area.

### 7.2 Tests

Run each of the chapter-3 tests (S1, S2, L1, L2, L3, G1, G2) on each (N, s) combination. Record the test outputs. Tests are passed at chosen tolerance ε_test.

### 7.3 Expected pattern

For each test, the error should scale as:

<!-- error(N, s) ≈ C_test · 1 / (N · s^p) -->
$$
\text{error}(N, s) \approx C_{\text{test}} \cdot \frac{1}{N \cdot s^p}
$$

with p ≈ 1 for tests dominated by random-walk quantization noise and p ≈ 2 for tests dominated by spatial-averaging convergence. The test-specific constant C_test depends on the test setup. The contour error(N, s) = ε_test in (N, s) space is the trade-off curve: equivalent (N, s) pairs at fixed accuracy.

The two regimes converge for large s. The slope of the (log N, log s) trade-off curve identifies p empirically.

### 7.4 Specific test predictions

- **L1 (1D dispersion at coord 2)**: should pass exactly at any (N, s), because the continuous scattering matrix at coord 2 is a permutation, and a binary bit-swap reproduces it exactly. No coarse-graining needed; the test transfers exactly.
- **L2 (Y-junction matched-impedance)**: should require coarse-graining. Predicted failure at (N=2, s=1); convergence to test-pass as s grows.
- **L3 (linearity / superposition)**: should pass at sufficient s for any N, because the leading-order coarse-grained dynamics is linear regardless of bit precision.
- **G1 (substrate Laplacian)**: independent of model dynamics; passes at all (N, s) trivially.
- **S1, S2 (stability)**: pass if the rule is bit-count-conserving; fail with naive quantization at small (N, s) due to compounding rounding errors.

### 7.5 Extrapolation

The fitted scaling law gives a prediction for the cell count s_binary(N=2) needed to recover continuous-test accuracy at any specified ε_test. Applied to the test bench's macroscopic features (which represent some "effective scale" relative to the lattice), this extrapolates to a Planck-cell budget per macroscopic feature in the physical lattice. Because the predicted budget is many orders of magnitude smaller than the cell count actually available at the Planck scale, the experiment supports the hypothesis with broad margin.

---

## 8. Implementation

### 8.1 Code structure

Add a quantizing wrapper around the existing Scattering model in `scripts/models.py`:

```
class QuantizedScattering(Scattering):
    def __init__(self, N_levels):
        self.N = N_levels
    def update(self, state, lattice):
        new_state = super().update(state, lattice)
        # Round each amplitude to the nearest of N levels
        # ...
        return quantized_state
```

The lattice-scale axis is handled by the existing `make_2d_hex_torus(nx, ny)` constructor with larger (nx, ny). The test bench scripts can be modified to accept (N, s) parameters and produce the trade-off plots.

### 8.2 Outputs

For each test, plot:

1. **Test error vs N** at fixed s (one curve per s).
2. **Test error vs s** at fixed N (one curve per N).
3. **Iso-accuracy contours** in (log N, log s) space.
4. **Fitted scaling law** with fit constants C_test and exponent p.

Estimated effort: a few days to implement the quantizing wrapper and adapt the test bench; an evening to run the sweeps.

---

## 9. Physical implications, if the hypothesis holds

If the experiment confirms the M ∝ 1/N² scaling for amplitude tests and M ∝ 1/N for L2-style scattering tests, several consequences follow:

1. **The continuous Scattering model is an effective theory.** The substrate is binary; the chapter-4 model is its coarse-grained limit. This is consistent with GRID's axiom A5 (1/4 bit per cell as fundamental information capacity).

2. **The cell spacing is the Planck length.** The lattice's bit count per macroscopic region equals the Bekenstein-Hawking bound — this is what motivates ζ = 1/4 in 3D. The hypothesis makes this literal rather than averaged.

3. **Wave amplitudes are emergent statistical quantities.** A "photon" or "wavepacket" in the continuum theory is, at the substrate level, a coordinated pattern in the bit field across many Planck cells. The quantum of energy per cell is 1 bit · ℏ ω_lattice, set by the lattice's clock frequency.

4. **Reversibility is exact at the substrate.** A bit-conservative Boolean scattering rule preserves microscopic reversibility. Macroscopic irreversibility (the second law) emerges from coarse-graining and observer ignorance, not from the substrate.

5. **The chapter-7 α question gains structure.** If the substrate is binary, charge quantization (the U(1) winding of chapter 7) is a property of *bit configurations* on closed loops, not of continuous phase. The bit field naturally supports topological invariants (winding numbers count cells in a particular state around a loop). This may give a cleaner derivation of α as a discrete combinatorial quantity than a continuous one.

None of these are required by the hypothesis to be valid; they are what the hypothesis would imply if confirmed.

---

## 10. What this would and would not change for the project

**Would not change:**

- The chapter-4 verdict. Continuous Scattering remains the right effective model for the project's tests and for any practical computational use. The quantized version is a deeper substrate, not a replacement.
- The bridges to grid/sim-maxwell and grid/sim-gravity-2. Those run on the continuous model; the binary substrate is one level below.
- The wrap-promotion ladder structure (chapters 5–7). The ladder is about lattice geometry, which is the same in both versions.

**Would change:**

- **Documentation of what the lattice "is."** The current chapters present the substrate as if cells are scalar/real-valued. Under the binary hypothesis, cells hold one (or a few) bits, and the continuous model is their coarse-grained behavior.
- **Connection to information-theoretic gravity.** Jacobson's argument becomes literal rather than effective; ζ = 1/4 is exactly the bit count per cell, not a metaphor.
- **Future α / charge-emergence work.** The combinatorial structure of bit configurations on closed loops becomes the natural setting, replacing or complementing the continuous-phase treatment.

---

## 11. Summary

The chapter-4 winning model (continuous Scattering on a 2D hex lattice) is plausibly the effective theory of a binary cellular automaton at the substrate scale. The hypothesis sits in a well-developed research tradition (FHP lattice gas, lattice Boltzmann methods, quantum lattice gases, deterministic-substrate interpretations). The trade-off between bits per cell and cells per macroscopic region follows quantization-noise scaling, with M ∝ 1/N² in the analog-averaging regime. The experimental program is a two-axis (N, s) sweep on the existing test bench, measuring how each test's error scales as the per-cell precision is reduced and the lattice is refined.

The hypothesis is not novel; the application to this specific lattice and this specific test bench is. If confirmed, the project's connection to information-theoretic foundations of physics (Bekenstein-Hawking, holographic principle, axiom A5) becomes literal rather than analogical, and the future α work in chapters 5–7 gains a discrete combinatorial setting that may produce cleaner derivations than the continuous-phase treatment.

The experiment is straightforward to run; the analytical predictions are well-established; the prior art is substantial. This document is the proposal; the implementation and results are open.

---

## References

- U. Frisch, B. Hasslacher, Y. Pomeau, *Lattice-Gas Automata for the Navier-Stokes Equation*, Phys. Rev. Lett. **56**, 1505 (1986).
- J. Hardy, Y. Pomeau, O. de Pazzis, *Time evolution of a two-dimensional model system. I. Invariant states and time correlation functions*, J. Math. Phys. **14**, 1746 (1973).
- G. R. McNamara, G. Zanetti, *Use of the Boltzmann Equation to Simulate Lattice-Gas Automata*, Phys. Rev. Lett. **61**, 2332 (1988).
- S. Succi, *The Lattice Boltzmann Equation: For Fluid Dynamics and Beyond*, Oxford University Press, 2001.
- J. Yepez, *Quantum Lattice-Gas Model for the Many-Particle Schrödinger Equation in d Dimensions*, Phys. Rev. E **63**, 046702 (2001).
- G. 't Hooft, *The Cellular Automaton Interpretation of Quantum Mechanics*, Springer, 2016.
- J. D. Bekenstein, *Black Holes and Entropy*, Phys. Rev. D **7**, 2333 (1973).
- G. 't Hooft, *Dimensional Reduction in Quantum Gravity*, arXiv:gr-qc/9310026 (1993).
- L. Susskind, *The World as a Hologram*, J. Math. Phys. **36**, 6377 (1995).
- T. Jacobson, *Thermodynamics of Spacetime: The Einstein Equation of State*, Phys. Rev. Lett. **75**, 1260 (1995).
- S. Wolfram, *Cellular automaton fluids 1: Basic theory*, J. Stat. Phys. **45**, 471 (1986).
