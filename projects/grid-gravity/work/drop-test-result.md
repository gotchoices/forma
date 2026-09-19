# Drop test — packets fall in a gradient of the storage weight, all alike

**Status:** Simulation result. **Step 2 of the mechanism 3 validation plan
([STATUS.md](STATUS.md)): passed.** On the canonical scatter with the storage
register of [uniform-q-theorem.md](uniform-q-theorem.md), wave packets released
in a gentle gradient of the storage weight accelerate toward the slower region,
at an acceleration that does not depend on their mass or construction, and
moving packets — massive and light alike — follow the ray equations of the
local spectrum. Reflection from a gradient is negligible once the gradient is
longer than about a wavelength.

Script: [`../scripts/drop_test.py`](../scripts/drop_test.py).
Figure: [`../outputs/drop_test.png`](../outputs/drop_test.png).

Grades: **[simulated]**, **[rigorous]** (the predictions), **[assessment]**.

---

## 1. Setup

An (x, c) lattice — x extended, c compact with n_c nodes — running the
canonical scatter, each node carrying a storage register of weight Y(x). The
compact direction is treated exactly through its Bloch phase, so a compact mode
number n fixes k_c = 2πn/n_c and the run is one-dimensional in x. Energy is
conserved to ~10⁻¹⁴ throughout.

The storage weight rises uniformly, Y(x) = 1 + 10⁻⁴·(x − x₀): the local rate
factor 1/√(1 + Y/4) falls slowly toward +x. Packets are built from the exact
positive-frequency eigenvectors and released at x₀; their energy centroid is
tracked.

## 2. Predictions, fixed before the run [rigorous]

A packet follows Hamilton's ray equations for the local spectrum
ω(k_x, k_c; Y(x)) of [uniform-q-theorem.md](uniform-q-theorem.md) §3:
dx/dt = ∂ω/∂k_x, dk_x/dt = −∂ω/∂x. With g = dY/dx and c the local light speed:

- **At rest, low frequency:** a = −c·(dc/dx) = g/(4 + Y)² — toward larger Y,
  the slower region. No dependence on the packet's mass.
- **At rest, exact lattice:** a = [g/(4 + Y)²] / cos²(ω₀/2), with ω₀ the
  packet's rest frequency. The factor 1/cos²(ω₀/2) ≈ 1 + ω₀²/4 is the
  lattice-scale departure from universality — of order (rest frequency × tick)².
- **Moving at speed v:** a = −c·(dc/dx)·(1 − 2v²/c²). The coordinate
  acceleration depends on speed (as it does in general relativity, in
  coordinates of this kind) — and on **nothing else**: not on mass, not on
  whether the packet is light or matter.

## 3. Results [simulated]

**Released at rest** (n_c = 32; predicted low-frequency a = 4.000×10⁻⁶
nodes/tick²):

| compact mode n | rest frequency ω₀ | a (sim) | a (exact prediction) | sim / exact | sim / low-frequency |
|---|---|---|---|---|---|
| 1 | 0.124 | 3.998×10⁻⁶ | 4.015×10⁻⁶ | 0.996 | 1.000 |
| 2 | 0.247 | 4.055×10⁻⁶ | 4.062×10⁻⁶ | 0.998 | 1.014 |
| 3 | 0.369 | 4.135×10⁻⁶ | 4.140×10⁻⁶ | 0.999 | 1.034 |

Three packets whose masses differ by a factor of three fall together; the
spread between them (up to 3.4%) is the predicted 1/cos²(ω₀/2) factor, and it
shrinks as the masses get lighter relative to the lattice scale (n_c = 128:
sim / low-frequency = 0.986, 0.997, 1.002).

The small remaining deficits are also understood: a packet "at rest" has a
spread of momenta, and the speed-dependence of §2 acting on that spread predicts
a reduction of 2·(c·σ_k/ω₀)². For the lightest packet tried (ω₀ = 0.031) that
is 0.9854; measured 0.9852.

**Moving packets** (deflection = run with gradient − control run without, so
the packet's own velocity and spreading cancel):

| packet | speed | deflection (sim) | deflection (ray) | sim / ray |
|---|---|---|---|---|
| massive, n = 1, k_x = 0.10 | 0.288 | +18.085 nodes | +18.088 | 0.9998 |
| photon, k_x = 0.30 | 0.628 | −10.313 nodes | −10.313 | 1.0000 |

The massive packet is pulled toward the slower region. The photon, heading
into the slower region, falls *behind* its control — it is delayed, the lattice
counterpart of the extra light-travel time near a mass.

A five-times steeper gradient gives the same agreement (sim / exact = 0.992 –
0.995), so the acceleration is linear in the gradient over that range.

**Reflection** (photon of wavelength 20.9 nodes crossing a ramp Y: 0 → 2, an
18% change in speed; step prediction from the index ratio R = 0.0102):

| ramp length | in wavelengths | reflected fraction |
|---|---|---|
| 0 (abrupt step) | 0 | 1.08×10⁻² (1.06 × the step prediction) |
| 8 | 0.38 | 4.1×10⁻⁴ |
| 32 | 1.5 | 9.6×10⁻⁵ |
| 128 | 6.1 | 3.9×10⁻⁶ |
| 512 | 24 | 1.8×10⁻⁷ |

An abrupt step reflects as an ordinary index step does; any gradient longer
than a wavelength or so is transparent. A gravitational field varies over
lengths enormously larger than any wavelength that probes it.

## 4. What this establishes, and what it does not [assessment]

**Established.** Given a *static* profile of the storage weight, the rule of
step 1 produces falling: toward the slower region, at an acceleration set by the
gradient of the local rate, **the same for every mass** up to corrections of
order (rest frequency × tick)², with light delayed rather than reflected. This
is the equivalence principle emerging from the rule rather than being imposed,
and it confirms that the uniform-q theorem survives a non-uniform q.

**Not established.** The profile here was imposed by hand. Nothing yet says a
mass *produces* such a profile — that is the sourcing question, step 3 — nor
that the profile is 1/r and reaches its static form dynamically, step 4. And
the ray equations here are those of an isotropic slowing, which carry the
half-value of light bending (γ = 0) noted in step 1; the speed-dependence
measured above, (1 − 2v²/c²), is that same fact seen in one dimension.

## Grades summary

- **[rigorous]** The three predictions of §2 (from the closed-form spectrum).
- **[simulated]** Universality of free fall across mass; ray-following for
  moving massive and light packets to better than 0.1%; reflection falling
  from 1% at a step to < 10⁻⁴ beyond 1.5 wavelengths; exact energy
  conservation.
- **[open]** Sourcing (step 3); dynamic relaxation to 1/r (step 4); γ (step 3).
