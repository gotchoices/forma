# R30 Findings


## Track 4. The r → ∞ limit

Script: `scripts/track4_r_limit.py`


### F9. No phase transition — charge works at all r > 0.26

The shear-charge mechanism (R19) produces α = 1/137 for every
r > r_crit ≈ 0.26.  There is no upper bound.  As r increases:

| r | s | Tube E% | L_tube (fm) |
|---|---|---------|-------------|
| 0.3 | 0.193 | 77.3% | 2,760 |
| 1 | 0.065 | 21.1% | 5,285 |
| 6.6 | 0.010 | 0.58% | 31,955 |
| 8.9 | 0.008 | 0.32% | 43,121 |
| 100 | 0.0007 | 0.003% | 485,103 |
| 1000 | 0.00007 | 0.00003% | 4,852,456 |

The shear s decreases as 1/r, but the product r²s² converges
to 0.00465.  The α formula r²μ sin²(2πs)/[4π(2−s)²] stays
exactly 1/137 by construction.  Charge = e at every r.


### F10. The tube is topologically essential, energetically optional

At r = 1000:
- The tube is 4.9 million fm long (≈ 0.5 μm — macroscopic!)
- It contributes 0.00003% of the mode energy
- The electron still has charge −e and spin ½

The tube dimension is a **topological degree of freedom**: its
EXISTENCE creates the second winding number needed for charge
and spin.  Its SIZE is energetically irrelevant at large r.

This resolves the "too many dimensions" question: the tube
dimensions don't contribute significant energy and are
invisible in scattering experiments, but they MUST EXIST
for the charge/spin algebra to work.


### F11. r is free because charge is topological

The charge mechanism depends on:
1. The topology: a (1,2) geodesic wrapping tube once, ring twice
2. The existence of shear: s ≠ 0

It does NOT depend on:
- The magnitude of s (which self-adjusts via α constraint)
- The tube circumference (which can be arbitrarily large)
- The aspect ratio r (any r > 0.26 works)

This is why r produces a one-parameter family at every T²
sheet.  The charge is integer-quantized — it's either e or 0
with nothing in between.  Any geometry with nonzero shear
and a (1,2) geodesic produces exactly the same charge.


### F12. r_p = 8.906 is pinned by physics, not geometry

The proton's r = 8.906 comes from the neutron mass constraint
(R27 Track 2): the cross-shear σ_ep must shift the neutron
mode to 939.565 MeV, and this requires a specific r_p.

At r_p = 8.906, the proton tube contributes only 0.32% of E².
The proton is 99.7% ring-dominated.  Its tube is structurally
necessary (charge +1, spin ½) but energetically marginal.


### F13. The mode spectrum degenerates at large r

At r = 1 (tube = ring), the first 10 modes span a rich energy
landscape with both ring (n₂) and tube (n₁) excited modes.

At r > 5, the spectrum simplifies: the first ~10 modes are ALL
pure tube modes (n₁ ≠ 0, n₂ = 0), with energies far below the
electron mass.  Ring modes (which include the electron) are
at much higher energy.  The tube modes form a ladder at
E_n = n × ℏc/(r × L_ring), becoming a near-continuum at
large r.


### F14. Summary of Track 4

1. **No phase transition** in the charge mechanism.
   Charge = e for all r > 0.26.  No upper limit.

2. **The tube is topological, not energetic.**  It provides
   charge and spin through winding topology.  Its size
   (and energy contribution) can be arbitrarily small.

3. **r is free because charge is integer-quantized.**
   The α formula self-adjusts s(r) to maintain α = 1/137
   at every r.  No geometric principle selects r.

4. **The spectrum degenerates at large r** into a tube-mode
   ladder far below the particle mass.  Ring modes
   (including the electron) are isolated at higher energy.

5. **r_p = 8.906 is physically pinned**, not geometrically
   special.  The other r values (r_e, r_ν) remain free.


---

## Track 6. Shared-dimension T³

Script: `scripts/track6_shared_t3.py`


### F1. T³ reproduces electron, proton, and neutron masses

A T³ with circumferences (L_a, L_b, L_c) and modes:

| Particle | Mode | Energy | Charge | Mass match |
|----------|------|--------|--------|------------|
| Electron | (1, 2, 0) | 0.511 MeV | −1 | exact |
| Proton | (0, 1, 1) | 938.3 MeV | +1 | exact |
| Neutron | (−1, −199, −1) | 939.6 MeV | 0 | 0.001% |

Circumferences at L_b = 5000 fm:
    L_a = 10,068 fm  (electron tube scale)
    L_b = 5,000 fm   (shared dimension — free parameter)
    L_c = 1.321 fm   (proton ring scale)

The electron uses A and B (like a T² ring+tube).  The proton
uses B and C.  The neutron bridges all three with a high
winding on B (n_b ≈ 199) to close the 1.3 MeV mass gap.

L_b is free (any value > 4854 fm works), analogous to the
aspect ratio degeneracy in T².  L_c ≈ L₆/2 from T⁶ because
the proton uses n_c = 1 here vs n₆ = 2 in T⁶.


### F2. Neutral spin-½ is structurally impossible in T³

With the charge formula Q = −n_a + n_c:

    Q = 0  requires  n_a = n_c
    Same value → same parity → spin count always 0 or 2

Spin ½ requires exactly ONE odd tube winding.  But n_a = n_c
forces both to be odd (spin count 2) or both even (spin count 0).
**No neutral spin-½ mode exists in T³.**

This is not a parameter problem.  It is a topological
constraint — no choice of L_a, L_b, L_c, shears, or winding
numbers can produce Q = 0 with spin ½.

Affected particles: neutron (½), Λ (½), Ξ⁰ (½), K⁰ (0 but
its antiparticle has ½ components), and all neutral fermions.


### F3. The neutrino tube dimension is structurally necessary

In T⁶, the neutron mode is (0, −2, 1, 0, 0, 2):
- n₁ = 0 (electron tube, even → no charge, no spin)
- n₃ = 1 (neutrino tube, odd → spin ½ contribution)
- n₅ = 0 (proton tube, even → no charge, no spin)
- Charge: −0 + 0 = 0  ✓
- Spin: 0 + 1 + 0 = 1 → ½  ✓

The neutrino tube provides the single odd winding needed for
a neutral fermion.  **This is the structural reason T⁶ has
three T² sheets** — each sheet provides a "tube" dimension
that contributes independently to charge and spin.

Without the neutrino tube, the only way to get Q = 0 is
to match the electron and proton tube windings (n_a = n_c),
which locks their parities together and forbids spin ½.


### F4. T³ fails catastrophically on intermediate particles

| Particle | Mass (MeV) | Best T³ match | Gap |
|----------|-----------|--------------|------|
| μ⁻ | 105.7 | 7.4 MeV | 93% |
| π⁺ | 139.6 | 7.4 MeV | 95% |
| K⁺ | 493.7 | 938.3 MeV | 90% |
| η | 547.9 | 938.3 MeV | 71% |

The T³ spectrum has only two energy scales:
- L_c = 1.32 fm → modes at ~938 MeV (proton scale)
- L_b = 5000 fm → modes at ~0.25 MeV (fine spacing)

There is nothing at 20–50 fm that would produce modes in the
100–500 MeV range.  In T⁶, this is the proton TUBE
(L₅ = 23.7 fm, spacing ~53 MeV per step), which is a
separate dimension from the proton ring (L₆ = 2.66 fm).

T³ merges the proton's two dimensions into one shared surface,
losing the independent tube scale that creates the intermediate
energy ladder.  **The meson/baryon mass spectrum requires the
proton tube as a distinct dimension.**


### F5. T³ has 10× fewer ghost modes than T⁶

| | T³ | T⁶ |
|--|-----|------|
| Modes below 2 GeV | 89 | ~900 |
| Energy bands | 4 | ~48 |
| Mode/particle ratio | ~2× | ~20× |

The T³ ghost problem is much smaller — but this is a
consequence of having too FEW modes, not of having the right
number.  T³ fails to accommodate most known particles, so
its economy is not a virtue.


### F6. Alternative charge formulas cannot save T³

Several alternatives were tested:

1. **Q = −n_a + n_b + n_c**: Breaks the electron's charge
   (would be +1 instead of −1).

2. **Spin from A only**: Fixes neutron spin but breaks
   proton spin (proton has n_a = 0 → spin 0).

3. **Context-dependent spin**: Ad hoc and breaks the clean
   algebraic structure that makes T⁶ work.

4. **T⁴ = T³ × T¹**: Adding a neutrino tube (dimension D)
   fixes the spin problem.  Neutron mode (0, n_b, 0, 1)
   has Q = 0, spin = 1 → ½.  But the intermediate energy
   problem (F4) remains unless the proton tube is also
   restored as a separate dimension.


### F7. Why T⁶ needs exactly 6 compact dimensions

Track 6 reveals that each T² sheet contributes two
structurally essential things:

1. **A tube dimension** — provides charge (via shear) and
   spin (via parity).  Three independent tubes (electron,
   neutrino, proton) are needed for the charge/spin algebra
   to work for all particles, including neutral fermions.

2. **A ring dimension** — provides an energy scale.  The
   proton sheet needs BOTH a tube (L₅ ≈ 24 fm, ~53 MeV
   ladder) and a ring (L₆ ≈ 2.7 fm, ~470 MeV scale) to
   produce the rich energy spectrum where mesons and baryons
   live.

Sharing a ring dimension between sheets (T³) loses the
second energy scale and collapses the intermediate spectrum.
Removing a tube dimension (T² instead of T⁶) loses the spin
degree of freedom for neutral particles.

**3 sheets × 2 dimensions = 6 is the structural minimum.**


### F8. Summary of Track 6

1. **T³ masses work** for e, p, n — the shared dimension
   successfully bridges the 1836× mass ratio.

2. **T³ spin fails** — neutral spin-½ is topologically
   forbidden.  The neutrino tube cannot be eliminated.

3. **T³ spectrum fails** — only 2 energy scales vs T⁶'s 6.
   The proton tube's 53 MeV ladder is essential for mesons
   and baryons.

4. **6 dimensions are structurally necessary:**
   - 3 tubes for charge/spin independence
   - 3 rings for the energy scale hierarchy
   - Any reduction loses either spin or spectrum.

5. **The r-degeneracy is real** — T³ has the same free-L_b
   problem that T⁶ has with aspect ratios.  Reducing
   dimensions does not fix the under-determination.
