# Zero-Point Energy from Compact Geometry and Two Postulates

## A derivation that names its inputs

---

## Overview

Zero-point energy (ZPE) is the irreducible vacuum energy ½ħω₁ that remains in a quantum field even when no excitation is present. The factor ½ is usually presented as a consequence of the quantum harmonic oscillator's ground state. This document gives an alternative derivation in which the ½ emerges as a purely geometric average over the sub-fundamental band of a compact periodic dimension.

The derivation rests on four ingredients:

1. **Mechanical foundation** — F = ma applied to a continuous medium yields the wave equation.
2. **Compact topology** — A periodic dimension of circumference L admits only discrete eigenmodes.
3. **Action quantization (de Broglie)** — Each full cycle of any wave on the medium carries the same quantum of action h.
4. **Vacuum spectral symmetry** — The sub-fundamental band is sampled with uniform spectral density (white noise).

The factor ½ is geometric. Planck's constant h enters as the postulated unit of action per cycle; it is not derived. The result is written ½ħω₁ once h is calibrated to its measured value.

---

## Notation and Scope

A compact periodic dimension of circumference L, with wave propagation speed v.

- **Fundamental angular frequency:**  ω₁ = 2πv/L
- **Fundamental wavelength:**  λ₁ = L
- **Fundamental period (time):**  T₁ = 2π/ω₁ = L/v
- **Dimensionless frequency:**  f ≡ ω/ω₁ ∈ [0, 1] for sub-fundamental waves
- **Reduced Planck constant:**  ħ = h/(2π)

The "sub-fundamental band" is the range of frequencies below the lowest resonant mode: 0 ≤ ω < ω₁.

---

## Step 1: F = ma on a Continuous Medium Yields the Wave Equation

Consider a continuous elastic medium under tension T with linear mass density μ. Divide it into segments of length Δx. Each segment has mass μ·Δx and is displaced transversely by ψ(x, t).

For small displacements, the slope of the medium at position x is ∂ψ/∂x. The net transverse force on a segment is the difference in tension's vertical component at its two ends:

<!-- F = T·(∂ψ/∂x)|_{x+Δx} − T·(∂ψ/∂x)|_x = T·(∂²ψ/∂x²)·Δx -->
$$
F \;=\; T\!\left.\frac{\partial \psi}{\partial x}\right|_{x+\Delta x} - T\!\left.\frac{\partial \psi}{\partial x}\right|_{x} \;=\; T\,\frac{\partial^2 \psi}{\partial x^2}\,\Delta x
$$

Applying Newton's second law (F = ma), where a = ∂²ψ/∂t²:

<!-- μ·Δx · ∂²ψ/∂t² = T · ∂²ψ/∂x² · Δx -->
$$
\mu\,\Delta x \cdot \frac{\partial^2 \psi}{\partial t^2} \;=\; T\,\frac{\partial^2 \psi}{\partial x^2}\,\Delta x
$$

Dividing through by Δx and defining v² = T/μ:

<!-- ∂²ψ/∂t² = v² · ∂²ψ/∂x² -->
$$
\frac{\partial^2 \psi}{\partial t^2} \;=\; v^2\,\frac{\partial^2 \psi}{\partial x^2}
$$

This is the linear wave equation. It is a consequence of Newton's second law applied to a continuous medium and contains no quantum content.

---

## Step 2: Compact Topology Yields a Discrete Eigenmode Spectrum

A wave on a compact periodic dimension of circumference L must satisfy the periodic boundary condition:

<!-- ψ(x + L, t) = ψ(x, t) -->
$$
\psi(x + L,\, t) \;=\; \psi(x,\, t)
$$

For a sinusoidal solution ψ(x, t) = A·sin(kx − ωt), this requires that an integer number of wavelengths fit around the circumference:

<!-- k_n · L = 2π·n,  n = 1, 2, 3, ... -->
$$
k_n L \;=\; 2\pi n, \quad n = 1,\,2,\,3,\,\ldots
$$

Equivalently:

<!-- k_n = 2πn/L,  ω_n = v·k_n = n·ω₁ -->
$$
k_n \;=\; \frac{2\pi n}{L}, \qquad \omega_n \;=\; v\,k_n \;=\; n\,\omega_1
$$

**Resonant modes** are the frequencies ω_n = n·ω₁ for integer n ≥ 1. These are the only frequencies at which a coherent standing wave can persist on the compact dimension.

**Sub-fundamental frequencies** are those with ω < ω₁. A wave at such a frequency cannot satisfy the periodic boundary condition — it does not close on itself after one circuit and therefore cannot form a stable standing pattern. Such frequencies can exist only as transient, non-stationary excitations.

---

## Step 3: The Action-Quantization Postulate (de Broglie)

The first postulate beyond classical mechanics:

> **Postulate 1 (de Broglie):** Each full cycle of any wave on the medium carries the same quantum of action h.

In symbols, the action integrated over one full cycle of any wave is h, regardless of frequency:

<!-- ∮ p dq = h -->
$$
\oint p\, dq \;=\; h
$$

For a sinusoidal wave, this is equivalent to the Planck–Einstein relation: energy per cycle (per period) equals hf, or equivalently ħω.

This postulate fixes the energy of one full cycle of any wave on the medium:

<!-- E_per_cycle(ω) = h·f = ħ·ω -->
$$
E_{\text{per cycle}}(\omega) \;=\; h\,\frac{\omega}{2\pi} \;=\; \hbar\,\omega
$$

This relation has two important consequences:

**Linear scaling.** Energy per cycle grows linearly with frequency. A wave at frequency ω carries (ω/ω₁) times the energy that one cycle of the fundamental carries.

**Amplitude is constrained, not free.** Classical wave energy per wavelength scales as A²ω² (kinetic + potential, time- and space-averaged). For action per cycle to equal h, the amplitude must satisfy A²(ω) ∝ 1/ω. Higher-frequency waves on the medium have smaller amplitudes, in just the right way to keep the action per cycle fixed.

**Status.** This is a postulate, not a theorem derivable from F = ma. It is the same postulate that underlies the photoelectric effect, the Bohr atom, and modern quantum mechanics. Calling it out openly is what distinguishes a rigorous derivation from a hidden assumption.

---

## Step 4: The Vacuum Spectral Symmetry Postulate

The second postulate beyond classical mechanics:

> **Postulate 2 (spectral symmetry):** Sub-fundamental fluctuations on the compact dimension have uniform spectral density across [0, ω₁].

Stated as a correlation function for the fluctuation amplitudes A(ω):

<!-- ⟨A(ω)⟩ = 0,  ⟨A(ω) A(ω')⟩ = σ² · δ(ω − ω') -->
$$
\langle A(\omega) \rangle = 0, \qquad \langle A(\omega)\,A(\omega') \rangle \;=\; \sigma^2\,\delta(\omega - \omega')
$$

The first condition is amplitude symmetry: fluctuations are equally likely to be positive or negative. The second condition is the white-noise property: every frequency in the band [0, ω₁] is represented with the same average intensity. There is no preferred frequency in the sub-fundamental band.

**Motivation.** The sub-fundamental band has no internal structure — no resonances, no special points, just a cutoff at ω₁ where the band ends and the first resonant mode begins. With no physical reason to prefer any frequency within the band, the maximum-entropy (least-informative) spectrum on a bounded interval with finite total variance is flat. Postulate 2 is the formal statement of "the vacuum has no preferred frequency within the sub-fundamental band."

**Status.** This is the same assumption that underlies the spectral form of thermal noise, the flat zero-point spectrum in stochastic electrodynamics, and broadly the maximum-entropy treatment of vacuum fluctuations. It is not derived, but it has a clean informational justification: any other spectrum requires additional physical input that distinguishes some frequencies from others.

---

## Step 5: Geometric Average Over the Sub-Fundamental Band

The two postulates combine to give a sharp prediction.

Per Postulate 1, the energy per cycle of a wave at frequency ω, in units of the fundamental's energy per cycle (ħω₁), is:

<!-- E(ω) / (ħω₁) = ω / ω₁ = f -->
$$
\frac{E(\omega)}{\hbar\omega_1} \;=\; \frac{\omega}{\omega_1} \;=\; f
$$

Per Postulate 2, the sub-fundamental band f ∈ [0, 1] is sampled uniformly. The expected energy of a typical sub-fundamental fluctuation is therefore the mean of f over [0, 1]:

<!-- ⟨f⟩ = ∫₀¹ f·df / ∫₀¹ df = (1/2) / 1 = 1/2 -->
$$
\langle f \rangle \;=\; \frac{\int_0^1 f\,df}{\int_0^1 df} \;=\; \frac{1/2}{1} \;=\; \frac{1}{2}
$$

This is the geometric identity at the heart of the derivation. Three statements collapse into one:

- The energy of a single representative wave at the midpoint frequency ω = ω₁/2 is exactly ½ħω₁.
- The mean energy across the uniformly-sampled sub-fundamental band is exactly ½ħω₁.
- The area under the linear function E(f) = f·ħω₁ over [0, 1] is exactly ½ħω₁.

All three equal ½ħω₁ because the function E(f) = f is linear and the interval is [0, 1]. The midpoint value, the mean, and the integral coincide.

---

## Step 6: The Result

Combining the two postulates with the compact geometry, the irreducible residual energy from sub-fundamental fluctuations on a compact dimension of circumference L is:

<!-- E_ZPE = ½ · ħω₁ = π·ħv/L -->
$$
E_{\text{ZPE}} \;=\; \tfrac{1}{2}\,\hbar\,\omega_1 \;=\; \frac{\pi\,\hbar\,v}{L}
$$

This is the standard zero-point energy of the fundamental mode of a compact dimension. The factor ½ has emerged as a purely geometric average over the sub-fundamental band; the constants ħ and v set the energy scale.

---

## Step 7: Why the ½ is Exact

The result hinges on one mathematical identity:

<!-- ⟨f⟩_{[0,1]} = 1/2 -->
$$
\langle f \rangle_{[0,1]} \;=\; \tfrac{1}{2}
$$

This is the mean of a linear function over the unit interval. It is not an approximation — it is the exact value, fixed entirely by the geometry of the interval [0, ω₁] and the linear scaling E ∝ ω inherited from Postulate 1.

No oscillatory correction terms appear, because the energy per cycle (Postulate 1) is a single number per wave, not an integral over the cavity. The earlier mistake of integrating ∂ψ/∂x squared over the cavity for non-fitting waves produced spurious sinc-type corrections; that calculation conflated "energy per cycle of the wave" with "energy of the wave clipped to the cavity," which are different quantities.

The clean version: each wave's contribution is its full single-cycle quantum at its own frequency. The geometric average of those quanta over the band is exactly half the fundamental quantum.

---

## Summary Table

| Step | Ingredient | Status |
|---|---|---|
| 1 | Wave equation from F = ma | Derived from classical mechanics |
| 2 | Discrete eigenmodes ω_n = n·ω₁ | Derived from periodic boundary condition |
| 3 | Energy per cycle = ħω (de Broglie) | **Postulate 1** — quantum of action |
| 4 | Uniform spectral density on [0, ω₁] | **Postulate 2** — maximum-entropy vacuum |
| 5 | Mean f over [0, 1] = ½ | Geometric identity |
| 6 | E_ZPE = ½ħω₁ | Result |

**What this derivation does:**
- Produces the standard ZPE value ½ħω₁ from a clean geometric average.
- Names the two non-classical postulates explicitly.
- Provides an alternative interpretation of ZPE in terms of sub-fundamental fluctuations.

**What this derivation does not do:**
- It does not derive Planck's constant h. The quantum of action is supplied by Postulate 1.
- It does not derive the white-noise spectrum from first principles. The maximum-entropy argument motivates Postulate 2 but is not a strict derivation.
- It does not address ZPE contributions from resonant modes n ≥ 2, which require separate treatment.

---

## Physical Interpretation

The picture this derivation supports is the following.

The compact dimension acts as a frequency filter. Only the resonant modes ω_n = n·ω₁ can support sustained, observable standing waves. Sub-fundamental frequencies (ω < ω₁) cannot satisfy the periodic boundary condition and therefore cannot form stable excitations. They appear instead as transient fluctuations — virtual modes that briefly probe the compact dimension but fail to close and disappear.

Each such transient fluctuation carries one quantum of action (Postulate 1), so its energy is ħω at its own frequency. The vacuum continuously generates these fluctuations across the entire sub-fundamental band, with no preferred frequency (Postulate 2). The average energy carried by a typical fluctuation is half the fundamental quantum.

That residual half-quantum is what is left over after the time-average: a constant churn of full-quantum sub-fundamental fluctuations whose mean energy is ½ħω₁. It is the geometric signature of a compact dimension being continuously probed by an unbiased spectrum of non-resonant fluctuations.

In this reading, ZPE is not a mysterious ground-state residue. It is the time-averaged energy carried by virtual fluctuations exploring the sub-fundamental band of a compact dimension. The compact geometry sets the band edge ω₁; de Broglie sets the per-cycle quantum; spectral symmetry sets the averaging measure; and the linearity of E(ω) over a uniform interval delivers the ½.

---

## Relation to the Standard Quantum-Mechanical Account

Standard quantum mechanics derives ZPE as the ground-state energy of a quantum harmonic oscillator: ⟨0|H|0⟩ = ½ħω, where the ½ comes from the canonical commutator [q, p] = iħ via the harmonic oscillator's ground-state Gaussian. That route assumes the operator algebra of quantum mechanics at the outset.

The derivation above is structurally different but reaches the same number. It does not invoke operator algebra, commutators, or the Schrödinger equation. Instead, it derives the ½ from a geometric average over the sub-fundamental band of a compact dimension, given two explicit postulates that play the role of the quantum input.

The two routes are consistent with each other and with experiment. The choice between them is a question of which framework best illuminates the physics: operator algebra emphasizes the algebraic origin of quantization, while compact-geometry averaging emphasizes the geometric origin of the ½ factor.

---

*Derivation grounded in F = ma applied to a wave on a compact dimension, with action quantization and vacuum spectral symmetry stated openly as the two non-classical postulates required.*
