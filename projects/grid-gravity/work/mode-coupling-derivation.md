# The detour, derived: mode-coupling n=0 ↔ n≥1 — a negative result

> **⚠ Superseded in its verdict by
> [gauge-invariant-coupling.md](gauge-invariant-coupling.md).** The "photon
> mass ∝ ρ_E" derived below (problems (a) and (c)) is a **gauge artifact**:
> it couples a bare phase *potential* to the n=0 gauge mode, which the photon's
> **established** masslessness (A4) forbids. Redone gauge-invariantly, the
> coupling is a **refractive index** (kinetic/metric-like), not a mass — so
> mechanism 2 is **not refuted**. Only problem **(b) (range / contact vs 1/r)**
> below survives, and it is the original make-or-break. Read this note for the
> (b) argument and the "metric vs potential" framing; disregard its "REFUTED"
> conclusion.

**Status:** Derivation (the review's §2 crux, in the user's detour framing).
Sets up the photon–compact-mode coupling from the boundedness nonlinearity
and asks whether the detour gives a **non-dispersive spatial refractive
index** (gravity) or something else. **Outcome: something else — and it does
not work.** This is a fail-fast: the honest derivation the review forced
shows mechanism 2, grounded in boundedness, does not give gravity.

Grades: **[derived]**, **[standard field theory]**, **[open]**.

---

## 1. Setup

ℵ-line field θ(y, x, t): y the compact coordinate (S¹), x the spatial
position. Modes θ = Σ_n a_n(x,t) e^{iny/R}. The **photon** is the massless
n=0 mode (ω² = c²k_x², speed set by the *spatial* scatter). The **mass** is a
standing wave in the n≥1 KK modes (mass ω₀ ≈ 1/R). Boundedness enters as a
compact/saturating structure; the detour needs the nonlinear part of it, so
model it as a symmetric potential V(θ) on the phase.

## 2. The coupling, and the photon self-energy [derived]

Expand V about the mass background θ_mass. The photon a_0 (n=0) couples to
the compact modes; at second order (the round-trip detour: photon → n≥1 →
photon) it acquires a self-energy from virtually exciting the massive modes:

<!-- Sigma(omega) ~ g^2 / (omega^2 - omega_0^2)  -->
$$
\Sigma(\omega) \;\sim\; \frac{g^2}{\omega^2 - \omega_0^2},
\qquad g \propto \langle\theta_{\text{mass}}^2\rangle \propto \rho_E .
$$

Because V is even (symmetric bound), the leading coupling is quartic, so the
photon picks up an **effective mass term**

<!-- delta(m^2) propto rho_E  ;  omega^2 = c^2 k^2 + delta(m^2) -->
$$
\omega^2 = c^2 k^2 + \delta m^2, \qquad \delta m^2 \propto \rho_E .
$$

## 3. Three problems — each fatal to the gravity claim

**(a) It is a *mass* term, not a refractive *index* → dispersive.** A
potential coupling adds a term ∝ a₀² (a mass), giving ω² = c²k² + δm² — the
phase velocity depends on k. That is **dispersive**, and it is *not* a
refractive index (which is a rescaling of the *kinetic* term, ω = ck/n, and
is non-dispersive). This is the crux the review flagged (§1/§2), now
derived: the boundedness (potential) coupling produces the *wrong tensor
structure*. Gravity — and the PV optical metric — is a **kinetic / metric**
effect (it multiplies (∂a)², universal and non-dispersive); a potential
gives a **mass** effect (field-specific, dispersive). Boundedness gives the
mass kind.

**(b) It is ∝ *local* energy density → short-range, not 1/r.** δm² ∝ ρ_E(x)
is nonzero only where the mass's amplitude reaches. A photon passing at
distance r (where ρ_E ≈ 0) feels **nothing**. The detour is a *contact*
interaction — the photon must be *at* the mass to detour — whereas gravity is
long-range (a mass sources a field that extends as 1/r). The earlier 1/r
([loops-and-range.md](loops-and-range.md)) *assumed* a spreading scalar
source; the actual coupling is contact, so the 1/r does not follow from the
mechanism (review §5, confirmed).

**(c) A potential on the U(1) phase breaks gauge invariance.** The photon is
massless *because* of U(1) gauge invariance (A4). A potential V(θ) on the
phase is a Stückelberg/Higgs mass term — it **gives the photon a mass** and
breaks the gauge symmetry that yields Maxwell. So the very nonlinearity the
detour needs is inconsistent with the massless photon. The gauge-invariant
version of boundedness — mere *compactness* (a free field on S¹) — is
**linear**, and a linear ℵ-line has *no* mode coupling and *no* detour
(aleph-grounding §3's own admission). So boundedness is caught between "gives
a photon mass" (nonlinear potential) and "no detour" (linear compactness).

## 4. Why this was findable only by derivation

Gravity is a **metric**: it modifies how *every* field propagates
(a kinetic/(∂a)² coupling), universally and non-dispersively. The optical-
metric/PV target is exactly this — a kinetic rescaling n(x). A mechanism that
produces a **potential/mass** coupling (as boundedness does) can be attractive
and energy-sourced and still *not be gravity*, because it has the wrong tensor
character (mass, not metric), the wrong range (contact, not 1/r), and the
wrong frequency behaviour (dispersive, not uniform). The mean-field
"softening → refractive index" step hid all three by never distinguishing a
*compact-stiffness* change (a mass) from a *spatial-speed* change (a metric).
The review named the gap; the derivation shows the gap is unbridgeable *with
this nonlinearity*.

## 5. Verdict and implications

**Mechanism 2 *in this form* (detour/refractive, grounded in boundedness as a
potential) does not give gravity.** It gives a short-range, dispersive,
gauge-breaking photon mass-shift ∝ local energy density — not a long-range,
non-dispersive, universal metric/index. This is a clean negative on the *form
tried*, found in the algebra before any chapter. It is **not** a proof that no
GRID mechanism gives gravity — only that a *potential/value-bound* nonlinearity
gives the wrong kind of coupling. The thesis (mass → local-time gradient →
gravity) stands open; the project is parked, not concluded, and can be
resurrected if the mechanism is seen from an angle that yields a *metric*
(kinetic) modification rather than a potential one.

The deep reason is instructive and worth keeping:

> Gravity is a **kinetic/metric** modification sourced by energy (universal,
> non-dispersive, long-range). A **potential/value-bound** nonlinearity
> (boundedness) gives a **mass/contact** coupling — the wrong kind. To get
> gravity mechanically one needs a mechanism that modifies the **metric**
> (the kinetic structure the photon propagates in), not the potential.

Implications:
- The **mechanical detour route to gravity is dead** in this form. Routes
  that remain (README Fail-fast): (i) **mechanical → entropy → Jacobson** —
  forma's existing route, which produces the *metric* thermodynamically (the
  right structure), and is where the substrate's gravity actually lives;
  (ii) a genuinely different mechanical mechanism that produces an
  **emergent metric / field-dependent kinetic term** sourced by energy —
  much harder, essentially the hard problem of emergent gravity.
- The project's honest standing drops from "mechanism 2 nearly there" to
  "mechanism 2 refuted; the mechanical-gravity thesis survives only via the
  entropy→Jacobson route or an unfound metric-producing mechanism."
- The coherence insights that *survive* independently of mechanism 2: the
  even/odd substrate-deviation → gravity/charge split is unaffected only in
  its *odd→charge* half (grid-primitive/09, real); the *even→gravity* half
  rested on this mechanism and falls with it.
