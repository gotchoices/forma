# Q30: Prime q and harmonic avoidance

**Status:** Closed — negative result (R11)  
**Source:** User question  
**Related:** [Q18](Q18-deriving-alpha.md), [Q29](Q29-variational-principle-alpha.md), [R11](../studies/R11-prime-resonance/)

**Question:** 137 is prime. Is that functional — does prime q prevent sub-harmonic
energy leakage and thereby select q = 137?

---

that functional — not coincidental?

On the torus, the photon completes q major orbits per Compton
cycle.  Each orbit is a sub-cycle whose rotating E-field
contributes to the total field.  If q is composite
(e.g. q = 136 = 2³ × 17), then every divisor d of q creates
a sub-period: after q/d orbits the field pattern has partial
closure, a sub-harmonic mode that can siphon energy from the
fundamental (full Compton-cycle) resonance.

| q   | Factorization | # divisors | Sub-resonances |
|-----|---------------|------------|----------------|
| 131 | prime         | 2          | 0              |
| 135 | 3³ × 5       | 8          | 6              |
| 136 | 2³ × 17      | 8          | 6              |
| 137 | prime         | 2          | 0              |
| 139 | prime         | 2          | 0              |
| 140 | 2² × 5 × 7   | 12         | 10             |

For prime q, the only divisors are {1, q}.  No intermediate
sub-harmonics exist — all field energy is forced into the
fundamental mode.

This is a standard engineering principle: prime numbers are
used in turbine blade counts, gear ratios, and antenna
arrays specifically to prevent resonant coupling between
sub-systems.

**Three-part selection of q:**
1. Coulomb self-energy → q in range ~100–287
2. Primality → no energy leakage to sub-harmonics
3. Energy minimization (Q29) → selects which prime

**Proposed computation:** overlay q phase-shifted copies of
the wave — one per major orbit, each shifted by 2π/q.
For prime q, the superposition should destructively
interfere everywhere except at the fundamental period
(the full Compton cycle).  For composite q, constructive
interference at sub-harmonic periods should be visible —
representing energy leakage channels.  This is a direct,
computable discriminant.

Note: primality also guarantees gcd(p, q) = 1 for ANY
choice of minor winding p — the single-path topology is
automatic and maximally robust.  For composite q, only
specific p values avoid splitting into multiple loops.
*Source: user question*
*Status: CLOSED (R11 — negative).  Eight tracks found no
prime/composite distinction in any linear analysis.  q enters
the flat-material-sheet spectrum as a continuous parameter, not through
its factorization.  The hypothesis remains viable only in the
nonlinear/curved-torus regime.*
