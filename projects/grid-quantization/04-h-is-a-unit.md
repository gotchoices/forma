# Ch. 4 — ℏ is a unit, not a target

**Status:** Draft (prose, first pass). Part of the [presentation arc](README.md#presentation-arc).
**Grade:** [reduced] — standard dimensional analysis and the principle-vs-scale stance.
**Role:** dissolve the "derive h" category error; locate ℏ as a substrate unit.

Approaching the quantum, it is easy to mistake what would count as
*deriving* ℏ, and the mistake costs an entire line of effort. This
chapter clears the confusion: Planck's constant has the wrong **type** to
be a derivation target, and what ought to be predicted is something
different.

## 4.1 The category error

ℏ has the dimensions of **action** — energy multiplied by time — and in
SI carries the units J·s. Its numerical value is whatever the chosen
unit system says it is: 1.054 × 10⁻³⁴ J·s in SI, and **1** by
construction in natural units. Setting ℏ = 1 is *defining* the action
unit; it is not a result. So a dimensionful "derive ℏ" would only
re-state the unit choice, and a dimensionless "derive ℏ" is impossible
— a pure number cannot fix a dimensionful quantity.

The right target is a dimensionless **principle**, not a number with
units. The *scale* of ℏ does not belong on the to-do list.

## 4.2 The substrate's three grains

The lattice arrives with three natural yardsticks:

- a length **L** — the lattice spacing (one edge);
- a time **τ** — the clock tick;
- an energy **dW** — the smallest energy step the substrate carries.

These are the smallest length, time, and energy the model has. Anything
dimensionful in it is built from these three.

## 4.3 c and ℏ are grain-combinations

Two famous "constants" of physics are just particular combinations of
the grains:

- **c = L / τ.** A speed (length divided by time). It is the substrate's
  *causal* limit — one edge per tick — and plays the role of the speed
  of light's *limiting* role in the continuum. (Actual wave packets
  travel slower than this ceiling, so c ↔ L/τ holds only up to an O(1)
  lattice factor — see §4.4.)
- **ℏ = dW · τ.** An action (energy multiplied by time). It is the
  smallest energy step times the smallest time step — the area of one
  phase-space cell of the substrate, up to the 2π convention that
  distinguishes h from ℏ (Bohr–Sommerfeld's "phase-space cell" of area
  h corresponds to 2πℏ; the grain identification is good to that
  conventional factor).

The form ℏ = dW · τ is **dimensionally forced**, not fitted: action has
units of energy × time, and the only thing the substrate's energy grain
and time grain can combine into with the right units is their product.
The same dimensional logic puts c at L / τ.

In substrate-natural units — energy measured in dW, time in τ, length
in L — both c and ℏ equal **1** by construction. Their familiar SI
numerical values reflect a choice of units, not a prediction.

One corollary is worth flagging here, since it is otherwise a separate
postulate. Because *every* field on the lattice is built from the same
three grains, the *same* ℏ governs every interaction automatically. The
**universality of action across fields** — which in standard physics is
a non-trivial empirical fact, separately assumed — falls out for free
on this picture: there is only one substrate, so there is only one ℏ.

A second consequence concerns the high-frequency edge of the spectrum.
The band structure's ω = π flat-band edge (§3.1) is the largest
eigenfrequency the discrete one-tick operator carries, and on the
energy reading this maps to a maximum quantum ≈ π · dW per mode — both
the substrate's **Nyquist limit** (no faster oscillation can be
represented on a clock of step τ) and an **ultraviolet cut-off** (no
higher single-mode energy is supported by the grain). Two readings, one
number, fixed by the grain.

## 4.4 The absolute scale is an identification, not a theorem

This does not yet say *how large* L, τ, and dW are; the grain ratios c
and ℏ leave the overall scale free. A third dimensionful input is needed
to fix it, and GRID supplies one through gravity: from
[axiom A5](../../grid/foundations.md) (each cell carries ζ = ¼ bit of
information — the foundational holographic-density axiom) the
gravitational coupling is

> G = 1 / (4 ζ),

derived from A5's horizon entropy density ζA fed into Jacobson's
thermodynamic recovery of Einstein's equations
([gravity.md](../../grid/gravity.md)). With c, ℏ, and G in hand the
lattice grains come out as the Planck units — L the Planck length,
τ the Planck time, dW the Planck energy
([foundations.md](../../grid/foundations.md)).

But this is a **consistency, not a proof that the cell *is* the Planck
length.** Tying the grains to (c, ℏ, G) is the framework's *posit* that
the grid is the fundamental Planck-scale substrate; given that posit,
the dimensional combination forces the identification. An absolute
length cannot be *derived* from theory without one dimensionful input,
and the grain *is* that input — so "cell = Planck length" is the
framework's identification, not a result this route establishes.
(c = L / τ itself holds only up to an O(1) lattice factor: the *causal*
limit is one edge per tick, but actual wave packets move slower, so even
the c-identification carries a dimensionless adjustment.)

## 4.5 h cannot be derived from α

A related expectation should also be retired. The fine-structure
constant α is a pure number; ℏ is dimensionful. No pure number can fix a
dimensionful quantity. The familiar relation

> α = e² / (4π ε₀ ℏ c)

does *not* solve for ℏ in terms of α alone — it requires the elementary
charge e as an additional dimensionful input. In GRID's natural units
the same relation reduces to e = √(4πα) (axiom A6) with ℏ = 1, which is
the *definition* of α given a unit choice, not a derivation of ℏ. There
is no path from "α ≈ 1/137" to a value of ℏ that does not pass through
other dimensionful quantities.

## 4.6 What is left to predict

After this clearing of the deck, the GRID quantities that are
*dimensionless* — and so the only ones where prediction even makes sense
— are:

- **ζ** (the per-cell information resolution, A5), and
- **α** (the electromagnetic coupling, A6).

Everything else dimensionful (ℏ, c, L, τ, dW, and the Planck units they
generate) is a *unit*: a yardstick fixed by the substrate's grains and a
choice of unit system. Putting "derive ℏ" or "derive c" on the agenda
was a category error; the right agenda is dimensionless.

---

The arc continues (see the [arc](README.md#presentation-arc)).

## Sources

- [energy-and-coherence.md](work/energy-and-coherence.md) §3–§4 — ℏ as the substrate action grain; the dimensional argument
- [tier2-design.md](work/tier2-design.md) §4b — the principle-vs-scale reframe
- [foundations.md](../../grid/foundations.md) — A5 (ζ, G = 1/(4ζ)), A6 (α)

## Claim discipline

[reduced]. Dimensional analysis + the principle-vs-scale stance. The
Planck-units result is a **consistency** of the framework's
identification (grid = fundamental Planck-scale substrate); it is
**not** a proof that the cell *is* the Planck length, and c = L/τ holds
only up to an O(1) lattice factor. ℏ is presented strictly as a unit,
never as a derivation.
