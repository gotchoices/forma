# Chapter 3 — The compact-phase field value is intrinsically focusing

This is the key result of the matter half. It is a *conditional* derivation: one
foundational premise is stated up front, and everything else — including the sign
of the nonlinearity — follows. The soliton theory it lands on is standard and is
cited, not re-derived.

## §1 The premise

Take the binding field's *value* to be a **compact phase** — an angle φ living on
a circle [0, 2π), with φ and φ+2π identified. In GRID this is the **ℵ-line** (the
compact phase internal to each edge) at the Planck scale, or a particle sheet's
**U(1)** at the particle scale; a sheet must carry such a U(1) for charge to be a
winding ([metric-charge](../metric-charge/)). This is the choice left open by
Chapter 2's fork — *circle*, not *interval* — and it is a forma foundational
posit, **not** derivable from the bare scatter (see
[work/reduction-cosine-from-scatter.md](work/reduction-cosine-from-scatter.md)).
It is the one input; the rest is consequence. **[P]**

## §2 Periodicity gives the cosine

Because the value is an angle, any on-site potential must be periodic,
U(φ) = U(φ+2π). The **minimal** such potential carrying a mass m² — the lowest
Fourier harmonic — is the cosine, whose small-φ expansion is:

<!-- U(φ) = m²(1 − cos φ) = m²( φ²/2 − φ⁴/24 + φ⁶/720 − … ) -->
$$
U(\varphi) \;=\; m^2\,(1-\cos\varphi) \;=\; m^2\!\left(\frac{\varphi^2}{2} - \frac{\varphi^4}{24} + \frac{\varphi^6}{720} - \cdots\right).
$$

The quartic coefficient is **negative (−m²/24): focusing**; the sextic is
**positive (+m²/720): saturating**. That is precisely the recipe a bound state
needs — focusing to pull the mode together, saturation to stop it collapsing —
and it falls out of periodicity, provided the lowest harmonic dominates. (A
general periodic potential Σₙ aₙ(1−cos nφ) can flip the quartic sign if higher
harmonics win; "minimal" is the Occam assumption, not a theorem.) **[D, minimal-completion]**

## §3 Sine-Gordon: breather and kink

The resulting equation of motion is the **sine-Gordon** equation, whose soliton
content is textbook and taken as given: a **breather** — a localized, oscillating,
Lorentz-boostable lump of net winding zero — and a **kink** — a 2π twist of the
phase carrying a conserved topological (ℤ) winding number. We read them as the two
kinds of particle:

- **breather = neutral mass** (a winding-0 internal oscillation),
- **kink = charge** (a topological winding).

The forma-specific contribution is the confirmation that this survives
discreteness: on the actual (x,c) lattice the breather is stable, mobile, and
energy-conserving, and it crosses the Peierls–Nabarro barrier rather than pinning
([work/focusing-from-phase.md](work/focusing-from-phase.md)). **[C]**

## §4 Derived versus posited

Cleanly separated: the scatter supplies the kinetic (coupling) term; a compact
*coordinate* supplies the mass m² (Chapter 4); the compact *field-value phase*
supplies the periodic *form* — and hence the focusing+saturating signs — and the
sine-Gordon solitons follow. The single irreducible input is §1's premise, the
circle-over-interval topology, which the substrate does not fix.

## §5 Scale, and the two kinds of excitation

The mechanism is scale-blind: it needs only a compact phase. At the **ℵ-line**
(Planck) scale it describes a Planck-mass sector relevant to the photon/substrate
level; at a particle **sheet's U(1)** it describes ordinary matter, with mass set
by the sheet size (∝ 1/R). Note that mass and charge are *different* excitations,
not one object seen twice: mass is the breather's winding-0 **oscillation**, charge
a **topological winding**. On a 2D sheet both live together (the sheet's two
cycles; metric-charge's (m,n) knot), but the localized-3D construction is that
project's, deferred here. **[cite metric-charge; O]**

## §6 Why saturation failed

The premise also explains the project's own course-correction. The refuted
saturation hypothesis put the boundedness in a *clipped amplitude* — an interval,
a wall, defocusing (Chapter 2). The same boundedness put in a *phase* — a circle —
is periodic, softening, focusing. Identical "boundedness," opposite topology,
opposite sign. That single distinction is the sharpest statement of why the
compact phase works where the value-bound could not.
