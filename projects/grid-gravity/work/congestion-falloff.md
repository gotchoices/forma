# Does the congestion field fall off as 1/r? — the gate derivation

**Status:** Working note (paper-first attempt at the feasibility gate).
Carries the derivation as far as it goes rigorously and marks where it
becomes conditional. Depends on the commitments in
[local-time.md](local-time.md).

Grades: **[rigorous]** (standard, follows), **[plausible]** (a reasoned
but unproven step), **[open]** (flagged, unresolved).

---

## 1. What the gate asks

Given a lossless, finite-bandwidth edge rule (delay in the edges, nodes
instantaneous — [local-time.md](local-time.md) Commitments 1–2), does a
persistent localized load produce a **proper-time field** that falls off
as **1/r (3D) / log r (2D), isotropically**? A Yukawa (e^(−r/ξ)/r) or
anisotropic result fails the gate.

## 2. The mapping: congestion network → lattice conduction problem

Model the steady state as a lattice conduction problem:

| Congestion picture | Conduction picture |
|---|---|
| edge congestion impedance (slow = high) | edge resistance / inverse conductance |
| persistent load of a mass at node n | steady current injected at n |
| proper-time deficit field q(x) | node potential V(x) |
| the mass's localized standing wave | a localized source of finite support |

The proper-time field q is what a clock reads relative to the unloaded
lattice; the gate is the spatial profile of q around n.

## 3. The crux: two dissipation channels, series vs shunt

The character of the impedance decides everything, and it splits into two
independent channels that the earlier "lossless ⇒ 1/r" shorthand
conflated:

- **Series impedance** — resistance *along* the edges, opposing flow and
  building a gradient. This is what makes a *static* field exist at all: a
  purely reactive (truly lossless, non-dissipative) delay line passes the
  steady component unchanged and forms **no static field**. So the
  congestion must be **irreversible** in the series sense — which is
  exactly the "irreversible" leg of the design trio. **[rigorous]**
- **Shunt loss** — the sourcing conserved quantity leaking to a bath at
  each node. A shunt term adds a mass: (∇² − m²)q = −Sδ, giving Yukawa
  e^(−r/ξ)/r with ξ = 1/m. **Long range requires no shunt.** "Lossless"
  in this project means precisely *no shunt loss* (energy is not leaked),
  **not** "no dissipation at all." **[rigorous]**

The trio therefore maps exactly onto the two channels:

> **irreversible = series impedance** (the field exists) ·
> **lossless = no shunt** (the field is long-range) ·
> **nonlinear = the impedance is load-dependent** (the field is sourced by
> the load, i.e. by energy).

Both dissipation channels are needed *and distinguished*: series present,
shunt absent.

## 4. The result for the conduction problem [rigorous]

With series impedance and **no shunt**, the steady-state field obeys the
source-driven Laplace equation on the lattice:

<!-- ∇² q = −S δ(x − n) -->
$$
\nabla^2 q = -\,S\,\delta(x - n)
$$

Its lattice Green's function is the standard one:

- **3D:** q(r) ∝ 1/r.
- **2D:** q(r) ∝ log r (the force, ∇q, ∝ 1/r — matching
  [sim-gravity-2](../../grid/sim-gravity-2/)).
- **Isotropy:** on the hexagonal lattice, 6-fold symmetry makes the
  leading continuum operator the isotropic ∇²; anisotropy enters only at
  higher order. So the leading falloff is isotropic by lattice symmetry —
  one of the reasons the hex lattice is the right substrate.
- **Localized source is fine.** A source of finite support still produces
  a 1/r *tail* beyond its support (multipole expansion: the monopole term
  is Q/(4π r), Q = ∫S). The mass being an exponentially-localized standing
  wave does **not** shorten the range — the range is the network's, not
  the source's. This retires the earlier worry that a localized particle
  would give a short-range field.

So **given series-impedance + no-shunt + hex**, the 1/r isotropic result
is rigorous and standard. The physics content is not here; it is in
whether the actual rule *lands* in this regime.

## 5. The genuine gap: does the nonlinear rule linearize to the no-shunt form? [the real work]

The load-bearing question the gate actually turns on:

> When the nonlinear finite-bandwidth edge rule is linearized about the
> loaded background, does the perturbation δq obey ∇²δq = source (no
> shunt, m = 0), or does it acquire a shunt/mass term?

- **Argument for no shunt [plausible].** Losslessness means no conserved
  quantity leaks to a bath. With nothing removed from the sourcing sector,
  there is no term proportional to q itself in the steady-state balance —
  only the divergence of a flux — so m = 0. This is the reason to expect
  1/r rather than Yukawa.
- **Risk [open].** The load-dependence of the delay, τ(load), couples the
  field to itself (nonlinear back-reaction). On linearizing, that coupling
  could generate an *effective* shunt (a term ∝ q) even though nothing is
  literally leaked — producing screening. Whether it does depends on the
  specific τ(load), and cannot be settled without a concrete rule.

This is where the derivation hands off to the update-rule spec: the rule
must be exhibited and linearized, and the coefficient of any q-term
checked to be zero.

## 6. Non-dispersivity — and how to test it [open, but decidable]

[local-time.md](local-time.md) Commitment 3 requires the slowing to be
frequency-independent (a uniform rescaling), or it is an optical medium,
not time dilation. The physical fork, in signal terms:

- A **pure delay** (a delay line) has *linear phase* / flat group delay —
  it shifts every frequency by the same time. Non-dispersive, and it is
  what a local time-rescaling t → (1+q)t *is*.
- A **bandwidth limit** (a low-pass filter) delays high frequencies more
  than low near its cutoff. Dispersive.

So the question is whether the finite-bandwidth edge acts as a delay line
or a low-pass filter. The risk is specific: a finite-bandwidth channel is
a low-pass filter *by definition* near its cutoff, so congestion may be
dispersive precisely when it is doing its job (running near saturation).
Whether it instead acts as a uniform delay/rescaling is not decidable by
inspection — but it **is** decidable, three ways:

1. **The loaded dispersion relation [analytic, decisive].** Linearize the
   edge rule and compute ω_loaded(k). The slowing is non-dispersive **iff**
   ω_loaded(k) = s·ω_unloaded(k) with s constant — the dispersion curve
   keeps its shape and only changes slope. If ω_loaded(k)/ω_unloaded(k)
   depends on k, the slowing is dispersive.
2. **Structural classification.** Determine whether the finite-bandwidth
   edge reshapes the signal spectrum (filter → dispersive) or merely
   time-shifts it (delay → non-dispersive). A FIFO buffer below saturation
   approximates a delay; a channel at its bandwidth limit approximates a
   filter.
3. **Numerical group delay.** Inject wavepackets of different centre
   frequency through a loaded region and measure whether the delay is the
   same for all. forma already has the machinery
   ([grid/sim-maxwell](../../grid/sim-maxwell/), grid-quantization
   `band_structure.py`).

Non-dispersivity is therefore a **second gate condition** alongside §5,
and both are read off the *same* linearized rule: §5 checks the
coefficient of the q-term (no shunt → massless → 1/r); §6 checks the
k-dependence of the slowing (uniform → non-dispersive → time dilation).
One linearization answers both.

## 7. Coefficient [open, deferred to Objective 2]

The magnitude of q scales with the series impedance per edge, which scales
inversely with edge bandwidth — the same coordination/resolution quantity
that sets ζ. This is the direction of G = 1/(4ζ) (more bandwidth → weaker
field → smaller G). Turning "direction" into the numerical match is
Objective 2, not part of this gate.

## 8. Provisional conclusion

The gate reduces to a **conditional**:

> **If** the linearized congestion rule is (a) no-shunt (lossless →
> massless) and (b) non-dispersive, **then** a persistent localized load
> yields a 1/r (3D) / log (2D), isotropic proper-time field — rigorously,
> by the standard lattice Green's function on the hexagonal lattice.

So the derivation has **moved the question**. It is no longer "does 1/r
emerge?" — that is settled given (a) and (b). It is now the sharper,
rule-specific pair:

1. Does a concrete lossless finite-bandwidth edge rule linearize to the
   **no-shunt** form (§5)?
2. Can that rule's delay be made **non-dispersive** (§6)?

Both are properties of an explicit update rule. That is the next artifact:
the update-rule spec, which must be written and linearized to check (1)
and (2). Until then the gate is **conditionally passed** on the falloff
shape and **open** on the two rule-level conditions.

## 9. What would still fail it here

- The linearization carries an effective shunt (§5 risk) → Yukawa.
- No admissible rule is non-dispersive (§6) → optical medium, not time
  dilation.
- Higher-order lattice anisotropy survives to the observable scale (§4) →
  direction-dependent field. (Expected small on hex, but to be checked.)

Any of these routes to a pivot in the README's fail-fast options (e.g. the
mechanical → entropy → Jacobson retreat), not to the death of the general
hypothesis.
