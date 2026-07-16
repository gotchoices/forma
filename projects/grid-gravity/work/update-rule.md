# The candidate update rule — and its two gate checks

**Status:** Working note (paper-first). Proposes one concrete
node/edge rule and carries the two gate checks
([congestion-falloff.md](congestion-falloff.md) §5, §6) as far as
leading-order analysis takes them. This is the decisive artifact: the
whole mechanism turns on whether such a rule exists and passes. Depends
on [local-time.md](local-time.md) and [congestion-falloff.md](congestion-falloff.md).

Grades: **[rigorous]**, **[plausible]** (leading-order, unproven at all
orders), **[open]**.

---

## 1. What the rule must satisfy

Three simultaneous demands, from the README trio and the two gate
conditions:

- **(i) Maxwell limit** — at low load it reduces to the existing junction
  behaviour (the 2/3 scatter that yields Maxwell).
- **(ii) No shunt on linearization** — the linearized congestion balance
  has no term ∝ q (mass), so the field is massless → 1/r.
- **(iii) Non-dispersive** — the load-dependent slowing is uniform across
  frequency (a delay, not a filter).

## 2. The candidate: a finite-bandwidth FIFO edge, an instantaneous node

**Node (instantaneous, unchanged).** Each node applies the existing
equal-impedance scatter the moment signal arrives:
outgoing = (2/3)·(total in) − (in on that edge). No node state, no node
delay — as in [local-time.md](local-time.md) Commitment 1.

**Edge (the new part).** Each directed edge is a **lossless FIFO transit
buffer** with:

- a nominal transit time τ₀ = 1 tick (the causal, empty-line speed);
- a maximum throughput μ (the bandwidth — quanta it can deliver to the far
  node per tick);
- an in-flight backlog Q (signal currently held on the edge).

Dynamics: signal enters from the near node at rate λ and leaves to the far
node at rate min(λ, μ). Nothing is dropped (lossless); surplus accumulates
in Q. By Little's law the transit time is

<!-- τ = τ₀ + Q/μ -->
$$
\tau \;=\; \tau_0 + Q/\mu.
$$

The proper-time field is the excess delay, q ≡ (τ − τ₀) = Q/μ. A massive
particle — a persistent standing wave — holds λ high on the edges it
occupies, so Q (hence q) builds there and, via node coupling, around
there.

This places **all timing in the edges** and makes the delay
**load-dependent** (the trio's *nonlinear* leg), while the node stays the
confirmed linear scatterer.

## 3. Demand (i): the Maxwell limit [rigorous]

Below saturation (λ < μ) the buffer never backs up: Q = 0, τ = τ₀, and
every quantum crosses in one tick. The rule is then *exactly* the existing
2/3 scatter on a one-tick edge — which [grid/sim-maxwell](../../grid/sim-maxwell/)
already showed yields directional wave propagation and exact
superposition, i.e. Maxwell. So the vacuum (unloaded) limit is Maxwell by
construction. ✓

## 4. Demand (ii): steady state → ∇²q, no shunt → 1/r [plausible]

In steady state, backlog is constant on each edge, so inflow equals
outflow at every node — discrete **flow conservation** (Kirchhoff):

<!-- Σ_edges J = source at n -->
$$
\sum_{\text{edges at }x} J \;=\; S\,\delta_{x,n}.
$$

The current J on an edge responds to the delay difference across it. To
leading order (weak load, linear response) this is an Ohmic/diffusive
constitutive relation, J ∝ −∇q (flow runs from more-delayed to
less-delayed, in proportion to the gradient). Substituting into
conservation gives the source-driven Laplace equation

<!-- ∇² q = −(S/D) δ(x−n) -->
$$
\nabla^2 q \;=\; -\,(S/D)\,\delta(x-n),
$$

whose hexagonal-lattice Green's function is **1/r (3D) / log r (2D),
isotropic** ([congestion-falloff.md](congestion-falloff.md) §4).

- **No shunt [plausible].** A term ∝ q would require Q to drain to a bath
  independent of neighbours. Here Q drains *only* by passing signal to the
  next node (lossless — nothing leaves the conserved sector), so there is
  no q-proportional sink and m = 0. The field is massless → power law, not
  Yukawa.
- **Caveat [open].** Both the linear constitutive relation and the
  no-effective-shunt claim are leading-order. The nonlinear back-reaction
  (q feeds λ feeds Q) could, on careful linearization, generate an
  effective q-term. This must be checked at the next order, not assumed.

## 5. Demand (iii): non-dispersive below saturation [plausible]

A FIFO buffer operating **below** saturation delays the entire stream by
the same Q/μ — it time-shifts without reshaping the spectrum. A pure time
shift is linear phase / flat group delay — **non-dispersive** — which is
exactly a local time-rescaling ([congestion-falloff.md](congestion-falloff.md)
§6). So in the weak-load regime the slowing is non-dispersive. ✓ (leading
order)

- **Strong-field caveat [open].** As λ → μ (saturation), the buffer can no
  longer pass high-frequency variation faster than μ — it becomes a
  low-pass filter, and the slowing turns **dispersive**. So the rule
  predicts non-dispersive time dilation in weak fields and *dispersion* in
  strong fields. Whether that is a genuine strong-field prediction
  (deviation from exact time dilation near very massive bodies) or a defect
  is left open — but it does not threaten the weak-field (ordinary-gravity)
  regime.

## 6. Preliminary verdict

The candidate rule **plausibly passes both gate conditions in the
weak-field regime**:

| Demand | Status |
|---|---|
| (i) Maxwell limit | ✓ rigorous (recovers the 2/3 scatter below saturation) |
| (ii) no shunt → 1/r | plausible (leading order); effective-shunt check open |
| (iii) non-dispersive | plausible below saturation; dispersive near saturation (open whether feature or defect) |

This is the first candidate that meets all three demands even at leading
order — enough to justify the numerical confirmation, not enough to call
the gate passed.

## 7. What must be nailed to close the gate

1. **The linearization at next order [open].** Expand q → λ → Q
   self-consistently and confirm the coefficient of the q-term is zero (no
   effective shunt, §4 caveat). This is the single load-bearing
   calculation; if a shunt appears, the field is Yukawa.
2. **The constitutive relation [open].** Verify J ∝ −∇q is the correct
   leading-order response of the FIFO edge, not merely the resistor-network
   analogy imported.
3. **Numerical confirmation.** Build the minimal lattice of finite-
   bandwidth FIFO edges, inject a persistent localized load, and measure
   (a) the radial falloff of q (1/r vs Yukawa vs anisotropic) and (b) the
   loaded dispersion relation ω_loaded(k)/ω_unloaded(k) for constancy
   ([congestion-falloff.md](congestion-falloff.md) §6). This is the
   go/no-go, and forma's existing dispersion/`band_structure` machinery
   applies.
4. **Coefficient [Objective 2].** Relate D and μ to ζ and check the
   magnitude reproduces G = 1/(4ζ).

## 8. If it fails here

A shunt at step 1, or an unavoidable dispersion at step 2/3, routes to the
README's Fail-fast options — most naturally the mechanical → entropy →
Jacobson retreat, since a FIFO edge that produces entropy (via its
irreversible ordering) may still supply the microscopic dS/dt even if it
does not produce a clean direct field.
