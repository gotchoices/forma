# Quantum Measurement as Wave Interaction on Compact Dimensions
## Collapse via detector thresholds, and Born's rule as sampling of an unreachable phase

**Status:** Interpretive companion to the ma-domain particle-spectrum work, scoped to **single-particle measurement**. The geometric foundations it builds on — quantization from single-valuedness, wave energy from F = ma, zero-point energy as a geometric residue — are established elsewhere in the project and only sketched here. The measurement claims (collapse as a detector event, Born's rule as phase-blind sampling) are proposed mechanisms with the open points marked. Entanglement and Bell correlations are out of scope; §5 explains why that boundary is principled rather than incidental.

**Cross-references:**
- [zpe_derivation.md](zpe_derivation.md) — ½ℏω₁ as the average energy of the sub-fundamental band, and the F = ma wave-energy result sketched in §1.3
- [threshold-dynamics.md](threshold-dynamics.md) — the threshold/preload mechanism for decay and production; the detector side of collapse (§3) is its measurement-facing companion
- [architecture.md](architecture.md) — the closure condition T(1, n), the project's form of "quantization from single-valuedness"
- [cand-QY-ED.md](cand-QY-ED.md) — the candidate particle content (6 Ma dims, particles as 2D sheet modes) that the single-loop language here specializes

---

## 1. The Picture: Particle and Observer as Waves on the Compact Domain

### 1.1 A realist wavefunction on a compact dimension

Schrödinger's original (1926) reading of ψ was realist: a physical wave, not a probability amplitude. The ma-domain posture is the same — "particles are confined light," waves trapped on material geometry. The wavefunction is a physical wave on a richer geometry that carries one or more **compact** (closed, periodic) dimensions at every point in space.

In the minimal case of a single compact coordinate, the complex wavefunction seen in ordinary 3D space, ψ(x,t) = A(x,t)·e^(iφ(x,t)), is the projection of a higher-dimensional real wave:

<!-- Ψ(x, y, t) = A(x,t) · e^(iny/R) -->
$$
\Psi(x, y, t) \;=\; A(x,t)\,\cdot\, e^{i n y / R}
$$

where y is the compact coordinate of period 2πR and n is the winding number. The imaginary unit is not a bookkeeping device: it tracks rotation of the wave around the compact loop. **The phase φ is the compact-dimension angle — and it is exactly the coordinate an observer in ordinary space cannot read directly.** That inaccessibility is the seed of everything below: measurement is the only way to interrogate the compact phase, and it is destructive.

### 1.2 Quantization from single-valuedness (sketch)

A wave on a compact dimension of circumference L must close on itself: ψ(x + L) = ψ(x). For e^(ikx) this forces e^(ikL) = 1, hence kL = 2πn with integer n. The allowed states are therefore **countable** — drawn from the integers, not the reals — and quantization is a geometric consequence of closure, not a postulate. In the full framework this is the closure condition T(1, n) on a 2D sheet; see [architecture.md](architecture.md) and [metric-charge ch. 4](../../metric-charge/04-the-closure-condition.md). The indivisible particle is one quantum of a closure-satisfying mode.

### 1.3 Zero-point energy and wave energy (sketch)

Two results are imported and used, not re-derived (full treatment in [zpe_derivation.md](zpe_derivation.md)):

- **Wave energy is quadratic in amplitude.** Applying F = ma to a continuous medium yields the wave equation, and its conserved energy density is e ∝ (∂ψ/∂x)² ∝ A² (time-averaged). Energy delivered by a wave scales as amplitude squared — a fact §4 needs.
- **Sub-fundamental probing carries ½ℏω₁.** Fluctuations below the fundamental ω₁ = 2πv/L cannot close on the compact dimension and cannot persist, but they carry real energy; averaged over the sub-fundamental band the typical fluctuation holds ½ℏω₁. This zero-point background is continuous and stochastic, so it **randomizes the compact phase** of every resident wave — the noise that makes the compact angle effectively unknowable between measurements.

### 1.4 Single loop vs. the full Ma sector

The single-loop language used throughout is the minimal pedagogical case. In the full framework the compact sector is six-dimensional, and a particle is a standing-wave mode on it whose dimensionality is not fixed in advance: a photon may be information on a *single* compact dimension (consistent with spin 1), while many particles are 2D modes on a dim-pair Ma(i, j) — a "sheet," with closure modes T(m_t, m_r). The measurement arguments below do not depend on the mode's dimensionality — wherever this file says "compact dimension," read "the particle's compact mode," of whatever dimensionality the framework assigns it.

---

## 2. Measurement as Wave Interaction

### 2.1 Two waves, one region

Let the particle be ψ_p = A_p·e^(iφ_p) and the observer be ψ_o = A_o·e^(iφ_o). Both are physical waves on compact dimensions; both carry energy in their amplitudes; both have compact phases that the zero-point background continuously stirs.

When the two waves share a region the field is their **superposition**, and the observable intensity carries an interference cross-term:

<!-- |ψ_p + ψ_o|² = A_p² + A_o² + 2 A_p A_o cos(φ_p − φ_o) -->
$$
|\psi_p + \psi_o|^2 \;=\; A_p^2 + A_o^2 + 2 A_p A_o \cos(\varphi_p - \varphi_o)
$$

The cross-term is constructive where the compact phases match (φ_p = φ_o) and destructive where they oppose. So the interaction **concentrates where the two compact phases agree**. The standard quantum inner product ⟨ψ_o|ψ_p⟩ is the spatial integral of this cross-term; the local pattern above is the integrand, and it is what fixes *where* the interaction localizes.

### 2.2 Two regimes: clean interaction vs. detection

How does a wave interaction become a recorded measurement? The phenomenology splits into two regimes, and the split is the spine of the collapse account in §3.

**Clean particle–particle interaction is threshold-free.** The cleanest photon–electron interaction is Compton scattering: photon + electron → photon + electron, genuinely two-body, with the photon *surviving* rather than being absorbed. (A free electron cannot absorb a photon at all — energy-momentum conservation forbids it.) Compton scattering is **continuous in energy, with no threshold**: two waves interfere, both survive, and the process is unitary. Nothing here discretizes or records anything.

**Detection requires a bound detector with a threshold.** The photoelectric effect is what earns its place in this account — not as a clean photon–electron process (it is atomic, at least three-body, since the lattice must absorb recoil) but for two lessons it teaches about *detectors*:

- **Energy enters per cycle as ℏω.** The relation E = ℏω − W is frequency-dependent and intensity-independent: the wave loads energy into the bound electron one compact cycle at a time.
- **A threshold discretizes, and preloading sets the timing.** The bound electron loads continuously from the incoming wave and is liberated only when accumulated energy crosses the work function W. A pre-loaded electron crosses sooner — which dissolves the old "instantaneity" objection without invoking a particle.

The work function W is **emergent atomic structure**, not a fundamental photon–electron threshold. So the threshold that makes a measurement *discrete and recorded* is a property of the **detector**, not of the particle–particle interaction. (The preload mechanism and its empirical signatures are developed in [threshold-dynamics.md](threshold-dynamics.md).)

---

## 3. Collapse: Localize, Discretize, Persist

Collapse is not one event but three, in two different regimes:

**Part 1 — Interference localizes (particle–particle, threshold-free).** The superposed intensity (§2.1) is large where the compact phases match and cancelled where they oppose, so interference sets *where* the interaction concentrates. Two constraints: a single localized spot (not a fringe pattern) requires the observer wave to be a localized packet; and interference *redistributes* amplitude rather than destroying it (∫|ψ|² is conserved). Localization alone therefore explains *where*, but not discreteness or persistence.

**Part 2 — Threshold discretizes (detector, bound/atomic).** A click — one discrete, recorded outcome — requires the detector threshold of §2.2. The combined wave plus the detector's own zero-point preload crosses that threshold at the localized match point. This is the "snap" of [threshold-dynamics.md](threshold-dynamics.md) seen from the measurement side.

**Part 3 — Consumption persists (countability).** Once the threshold is crossed, the closure mode is delivered to the detector and consumed. Countability ensures one mode, one event: nothing remains to deliver elsewhere, so the outcome persists after the waves separate. *(Open point: the closure number is a topological invariant, so its transfer requires an unwinding/rewinding event — a coordinated zero-amplitude crossing on both waves — that the framework must still exhibit explicitly. §6.)*

| Face of the measurement problem | Mechanism | Regime |
|---|---|---|
| *Where* is the particle found? | Interference reinforcement at the phase-match point | Particle–particle, threshold-free (Compton-clean) |
| *Why discrete* — one click? | Detector threshold crossing + preload | Detector, bound/atomic (photoelectric-type) |
| *Why persistent* — stays collapsed? | Closure-mode consumption (countability) | Topological (open point) |

**The headline: collapse is not a clean two-particle phenomenon.** Particle–particle interaction is unitary, threshold-free interference; the discrete, persistent, recorded collapse appears only when a bound detector with a threshold takes part. This is also why a single quantum triggers one and only one detector — photon antibunching (Kimble, Dagenais & Mandel, 1977) is the experimental face of closure-mode countability: one mode is consumed by one threshold crossing.

---

## 4. Born's Rule as Sampling of an Unreachable Phase

The ambition is not to reproduce Born's rule to the last factor, but to show *why a probabilistic description is forced* on an observer of a deterministic wave — and why the description takes the modulus-squared form.

### 4.1 Probability lives in the event, not the particle

Take the wave to be **deterministic**: ψ evolves with no randomness of its own. The observer still cannot read it without a destructive measurement — §3 supplies the reason the measurement is destructive (the closure mode is consumed). An observer who couples to the wave at an uncontrolled moment samples it at an uncontrolled compact phase. With the phase neither knowable nor repeatable, a probability distribution is the *only* faithful description of the outcome — **even though the particle itself carried no probability.** The randomness is a property of the *measurement event* (an arbitrary sampling of a hidden phase), not of the particle. This is the inverted reading of randomness here: epistemic, located in the observer's access, not ontological.

### 4.2 Why modulus, and why squared

The Born form |ψ|² answers two questions, and each maps onto a piece of this picture:

- **The modulus removes the unreachable compact phase.** Write ψ = A·e^(iφ). The observable cannot depend on φ, because φ is the compact angle no observer reaches (§1.1) and the zero-point background randomizes it anyway (§1.3). The operation that strips φ is precisely |ψ|² = ψ*ψ = A². Equivalently: over an uncontrolled relative phase φ_p − φ_o, the interference cross-term of §2.1 averages to zero, leaving the phase-independent intensity A_p² + A_o². **The modulus is what "the compact domain is beyond reach" looks like mathematically.**
- **The square is wave energy.** The detector responds to *energy delivered*, and wave energy scales as amplitude squared (§1.3). The surviving phase-independent quantity that the threshold actually integrates is the intensity A², not the amplitude A.

Together: a detector sampling a deterministic wave at a random compact phase responds to the energy that survives phase-averaging, which is |ψ|². The modulus and the square are not two postulates but two facts of this geometry — an unreachable phase and a quadratic energy.

### 4.3 What is established, and what is assumed

Firmly: the *form* |ψ|² is forced — phase-independence gives the modulus, quadratic wave energy gives the square. **Assumed, not derived:** that the sampling measure over the compact phase is uniform, so the weights normalize to genuine probabilities. This is the same "quantum equilibrium" assumption that de Broglie–Bohm and stochastic electrodynamics carry; deriving the uniform measure from the zero-point dynamics is the remaining work (§6). The claim, then, is the *general idea* of Born — probability as the observer's only honest model of a hidden-phase sampling event — with the modulus-squared form explained and the normalization left open.

---

## 5. The Single-Particle Boundary (Why Bell Is Out of Scope)

The account of §4 is deliberately a **local** one: each particle carries a definite (if unreadable) wave, and the observer samples it. For a single particle this is complete and raises no difficulty.

It is also, stated plainly, a **local hidden-variable story** — the particle's state was there all along; the observer merely lacked access. Bell's theorem, confirmed by the Aspect experiments, rules out exactly this class *for entangled pairs*: no local account reproduces the measured correlations. So the sampling picture is licensed precisely on the **single-particle side** of the Bell boundary. The moment two correlated particles are involved, the same epistemic story would have to be replaced or supplemented by genuinely nonlocal wave structure — and demonstrating that is a separate, unsolved problem.

That is why entanglement is out of scope here, and the exclusion is principled: this document claims only what a local, single-particle wave picture can honestly claim. Bell is named, not addressed, because no apparent violation arises within the single-particle scope; it marks the frontier where this picture stops.

---

## 6. Open Points

- **Born normalization.** The uniform sampling measure over the compact phase (§4.3) is assumed. Deriving it from the zero-point dynamics would turn the "general idea" of Born into a quantitative result.
- **Topological transfer in collapse.** Part 3 of §3 requires an integer closure mode to move between two waves; exhibiting the unwinding/rewinding (zero-amplitude crossing) that respects topological conservation is unfinished.
- **Where the detector boundary lies.** §2.2 separates threshold-free particle–particle interaction from threshold-bearing detection. At what scale or degree of binding a system acquires a measurement threshold — and how that connects quantitatively to [threshold-dynamics.md](threshold-dynamics.md) — is open.
- **The entanglement frontier.** Whether the Ma compact sector has global (shared-across-space) character is the structural question that any future entanglement/Bell treatment would have to settle (§5).

---

## References

- **Schrödinger (1926)** — realist wave interpretation of ψ; the starting posture here.
- **Compton (1923)** — photon–electron scattering as the clean, threshold-free two-body interaction (§2.2).
- **Kimble, Dagenais & Mandel (1977)** — photon antibunching; the experimental face of closure-mode countability (§3).
- **de Broglie–Bohm; Marshall, Boyer, de la Peña (stochastic electrodynamics)** — quantum behavior from a real wave plus a zero-point background, and the "quantum equilibrium" measure assumption echoed in §4.3.
- **Bell (1964); Aspect, Grangier & Roger (1982)** — the theorem and experiments that fix the single-particle boundary of §5.

---

*Measurement-theory companion to the ma-domain particle-spectrum work; shares its foundations with [zpe_derivation.md](zpe_derivation.md) and [architecture.md](architecture.md), and its detector mechanism with [threshold-dynamics.md](threshold-dynamics.md).*
