# Switch-on in 3D — the scatter's dynamics reach the static 1/r, at light speed

**Status:** Simulation result. **Step 4 of the mechanism 3 validation plan
([STATUS.md](STATUS.md)): passed.** A steady source switched on at the centre of
a 3D canonical-scatter lattice builds a static 1/r potential behind a front that
moves at the lattice light speed — isotropic, at the predicted amplitude, with
no drift or growth. Switched off, the potential leaves as a wave. It also pins
down *which* lattice quantity the carrier's potential is.

Script: [`../scripts/switch_on.py`](../scripts/switch_on.py).
Figures: [`../outputs/switch_on.png`](../outputs/switch_on.png),
[`../outputs/switch_on_off.png`](../outputs/switch_on_off.png).

Grades: **[rigorous]** (the prediction), **[simulated]**, **[assessment]**.

---

## 1. Why this was a real question

That the lattice Laplacian has a 1/r static solution is not in doubt (it is a
theorem, and [loops-and-range.md](loops-and-range.md) checked it). The open
question was dynamical: does the scatter, *run forward in time from nothing*,
arrive at that solution? [grid-duality](../../grid-duality/) had recorded a
negative in a neighbouring setting — in 2D, with a node pinned rather than
sourced, the scatter's field did not relax to the static one.

## 2. Which quantity is the potential [rigorous]

The scatter is a first-order form of the wave equation, and its registers hold
first-order quantities. In network terms (a node is a capacitor, a link an
inductor):

- a node's value V = (2/N)·Σ registers behaves as a **velocity** (the node
  voltage);
- the difference of the two amplitudes on a link is the **gradient** (the link
  current);
- the **potential** q — the quantity the local rate must follow (posit P5) — is
  neither. It is the **running sum of V** at each node.

A steady source therefore does *not* hold the node value V at a static 1/r: it
sends out a single pulse of V and leaves V = 0 behind it. What is left standing
is the accumulated q, and a steady 1/r² flow on the links. For an injection s
into each of a node's six registers every tick, the network equations give

<!-- 3 q̈ = ∇²q + 6s·δ   ⇒   behind the front  q(r) = 6s/(4πr),  front at r = t/√3 -->
$$
3\,\ddot q \;=\; \nabla^2 q + 6s\,\delta^3(\mathbf r)
\qquad\Longrightarrow\qquad
q(r) = \frac{6s}{4\pi r}\ \ (r < t/\sqrt3), \quad V = 0,\quad \text{link flux} \propto 1/r^2 .
$$

This was written down before the run.

**Consequence for the mechanism.** The carrier's potential is a *stored*
quantity — an accumulator at each node — while the scatter registers carry its
rate of change and its gradient. "Lattice members store a quantity in addition
to their scattering function" is exactly this. It is added to the ledger as a
refinement of P2.

## 3. Results [simulated]

Cubic lattice, canonical scatter, source at the centre switched on smoothly over
12 ticks. The run stops before n/2 ticks, so by strict causality (one node per
tick) the boundary cannot influence anything measured.

**Amplitude and isotropy** (241³, 118 ticks, front at r ≈ 65; prediction
q·r = 6/(4π) = 0.4775):

| r | q·r on an axis | face diagonal | body diagonal | spread |
|---|---|---|---|---|
| 3 | 0.4958 | 0.4762 | 0.4709 | 5.2% |
| 8 | 0.4795 | 0.4772 | 0.4763 | 0.7% |
| 16 | 0.4776 | 0.4770 | 0.4772 | 0.1% |
| 25 | 0.4776 | 0.4778 | 0.4769 | 0.2% |
| 35 | 0.4778 | 0.4769 | 0.4777 | 0.2% |

Mean for r ≥ 8: **0.4775 — ratio to prediction 1.0000.** The direction
dependence is confined to the few nodes nearest the source.

**The front, and what is behind it** (probes at r ≈ 18):

| direction | arrival | implied speed | final q / prediction | drift over the last 25% of the run |
|---|---|---|---|---|
| axis | tick 37 | 0.581 | 1.0004 | 0.21% |
| face diagonal | tick 38 | 0.575 | 0.9992 | 0.19% |
| body diagonal | tick 36 | 0.577 | 0.9995 | 0.20% |

The lattice light speed is 1/√3 = 0.5774. Once the front has passed, the
potential sits at its static value; the residual motion is the decaying ringing
of the switch-on. Behind the front the node value V has returned to ~10⁻⁴ of the
injection, and the link flux times r² approaches the same constant (0.473 at
r = 20, against 0.4775).

**Switched off again** (source on at t = 0, off at t = 50): at the probes the
potential rises to the static value, holds, and then falls back when the "off"
front arrives (t ≈ 87), leaving a residue of 0.03% – 0.3% of the peak. The field
of a removed source is not dissipated on the spot; it **leaves as a wave**. This
is the lossless form of "remove the load and the region relaxes" that the
mechanism requires ([sync-carrier-mechanism.md](sync-carrier-mechanism.md) §6).

## 4. What this establishes, and what it does not [assessment]

**Established.**
- The scatter's own dynamics produce the static 1/r potential, at the predicted
  amplitude to four figures, isotropically beyond a few nodes. Gate condition
  (1) is met *dynamically*, not just as a property of a static solve.
- The influence travels at exactly the speed of light on the same lattice,
  untuned — the time-domain confirmation of the step 1 argument that a carrier
  riding the same scatter shares light's spectrum.
- Relaxation is radiative, not dissipative.
- The potential is identified: an accumulator of the node value.

**On grid-duality's earlier negative.** It was a 2D, pinned-node test. In two
dimensions a switched-on source *never* reaches a static potential even in the
continuum — the potential keeps growing logarithmically, and only its gradient
settles — so a static fit there is expected to fail for reasons unrelated to the
scatter. That is offered as the likely reconciliation; it was not re-run here.

**Not established.** This is the *linear* carrier with an imposed source. The
source was not a standing wave feeding the carrier through the action of step 3,
and the potential q did not feed back into the storage weights of steps 1 and 3.
Closing that loop — a mass that sources q, a q that slows the mass's own
neighbourhood and everything passing through it — is the nonlinear problem of
step 5, along with the two flags carried from step 3 (the breathing source; the
second-order parameter β).

## Grades summary

- **[rigorous]** The identification of V, link difference and q; the prediction
  q = 6s/(4πr) behind a front at r = t/√3.
- **[simulated]** q·r = 0.4775 (ratio 1.0000) with < 0.2% anisotropy beyond
  r ≈ 16; front speed 0.575 – 0.581 in three directions; no drift; V → 0 behind
  the front; 1/r² link flux; radiative relaxation on switch-off.
- **[assessment]** Reconciliation with grid-duality's 2D result; what remains
  for step 5.
