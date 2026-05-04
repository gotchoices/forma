# Chapter 2 — Modes on a sheet

**Status:** Sparse outline. Each section is one to three sentences describing the derivation step that section will perform. To be expanded into full prose once the outline is approved.

This chapter takes the givens of [Chapter 1](01-foundation.md) — the manifold M, the bare diagonal metric, the real scalar field φ, the massless wave equation □φ = 0, and the periodicity conditions on (u, w) — and derives what kinds of solutions the wave equation actually admits.

The derivation arc parallels [metric-mass Chapter 2](../metric-mass/02-mass-from-u.md) but on a richer manifold: two compact directions instead of one, two extended spatial directions instead of one. Wherever the math is a routine extension of metric-mass's, we cite metric-mass and move on. Where the 2D compact sheet introduces genuinely new structure — the joint discrete (m, n) spectrum, the single-axis modes, the mass surface in mode space — we develop in detail.

---

## Bare outline

### 1. Setting up: separation of variables on M

Restate the wave equation from Chapter 1 §8. Note that it is now a PDE in five variables (t, S₁, S₂, u, w). Apply separation of variables: assume

φ(t, S₁, S₂, u, w) = T(t) · X₁(S₁) · X₂(S₂) · U(u) · W(w)

and substitute. Divide through by the product to obtain five separated terms, each depending on only one variable. Standard separation-constant argument: each term must equal a constant, with the sum of constants equal to zero. This gives five ordinary differential equations linked by one algebraic constraint — the *dispersion relation* (§4).

Cite metric-mass §1 for the technique itself; this section is a routine 5D extension.

### 2. The u- and w-equations under periodicity

Each compact direction has the same form of equation:

U″(u) = −k_u² U(u)
W″(w) = −k_w² W(w)

with periodic boundary conditions φ(u + L_u) = φ(u) and φ(w + L_w) = φ(w). Periodicity quantizes k_u and k_w independently:

k_u = 2π m / L_u  (m ∈ ℤ)
k_w = 2π n / L_w  (n ∈ ℤ)

The mode is labeled by an **integer pair (m, n)** — the winding numbers in u and w respectively. This is the analog of metric-mass's single integer n, doubled.

Note immediately: the (m, n) labeling is the substrate for everything in chapters 3–9. The closure condition (Chapter 4) is a rule about which (m, n) pairs satisfy it; the knot family (Chapter 3) is the geometric picture of (m, n) as closed paths on the torus; the gauge-promotion question (Chapter 5) asks which (m, n) modes source off-diagonals with the right structure.

### 3. The S₁, S₂, and t equations

The three extended directions yield the standard plane-wave/oscillator pieces:

X₁(S₁) ∝ exp(i k_{S₁} S₁)
X₂(S₂) ∝ exp(i k_{S₂} S₂)
T(t) ∝ exp(−i ω t)

with k_{S₁}, k_{S₂}, and ω all continuous (no periodicity to quantize them). This is identical to metric-mass §3, just with one extra spatial direction.

Note that nothing in the bare-metric derivation forces the S-momentum to lie along S₁ rather than S₂. We define **k_S** as the magnitude of the spatial momentum in the (S₁, S₂) plane:

k_S² = k_{S₁}² + k_{S₂}²

so that the dispersion relation can be written compactly using k_S alone. Single-knot derivations through chapter 7 will mostly use k_S without specifying its direction. (Chapter 8 of metric-binding distinguishes S₁ from S₂ when two knots sit at different positions.)

### 4. The dispersion relation

Substituting the separated solutions back into the wave equation produces the **dispersion relation**:

ω²/c² = k_S² + k_u² + k_w²

with k_u = 2πm/L_u and k_w = 2πn/L_w from §2. Equivalently:

ω²/c² = k_S² + (2π/L_u)² m² + (2π/L_w)² n²

This is the 2D-compact extension of metric-mass's ω²/c² = k_S² + (n/R_u)² dispersion. The new structure is the *joint* contribution from m and n.

### 5. The discrete mass spectrum

Set k_S = 0 (rest frame). The dispersion relation gives the rest energy:

E_rest = ℏω = ℏc · √((2π/L_u)² m² + (2π/L_w)² n²)

Using m = E_rest/c²:

m_{(m,n)} = (ℏ/c) · √((2π/L_u)² m² + (2π/L_w)² n²)

The mass is parametrized by the integer pair (m, n) — a *2D* discrete spectrum, where metric-mass had a 1D spectrum. The (m, n) labeling is the project's primary mode index from this point forward.

For the inertial proof (that this is operationally inertial mass via p_S = m · v_g in the slow-motion limit), cite [metric-mass Chapter 2 §6](../metric-mass/02-mass-from-u.md). The argument carries over without modification — it depends only on the dispersion-relation structure, not on the dimension of the compact direction.

### 6. The (0, 0) zero mode is ordinary light

The (m, n) = (0, 0) mode has no winding in either compact direction. From the dispersion relation:

ω²/c² = k_S²    →    ω = c · k_S

Massless. Propagates at speed c through (S₁, S₂). The field configuration is u-independent and w-independent — *no compact-direction structure at all.*

This is the analog of metric-mass's n = 0 mode: ordinary light, unaware of the compact structure. It does *not* satisfy the closure condition (which requires winding in w by §10 of Chapter 1), so it is not a candidate for charge promotion. It also does not source any off-diagonal metric entries (no compact-direction momentum), confirmed against [metric-mass Chapter 5](../metric-mass/05-metric-self-consistency.md) — vacuum and pure-light configurations leave the bare metric self-consistent.

### 7. The single-axis modes (m, 0) and (0, n)

Two important sub-families:

- **(m, 0) modes:** wind in u only, no w-winding. Carry mass m · 2πℏ/(L_u c). Source off-diagonal entries in g_μu but not g_μw.
- **(0, n) modes:** wind in w only, no u-winding. Carry mass n · 2πℏ/(L_w c). Source off-diagonal entries in g_μw but not g_μu.

Neither single-axis family satisfies the closure condition stated in Chapter 1 §10 — that condition requires *both* u and w to host a complete standing wave. The single-axis modes thus produce **mass without charge**: a structural form of neutrality, distinct from any pair-cancellation mechanism (Chapter 6).

These are the candidate **closure-failure mass-only modes** that Chapter 4 will interrogate further as candidates for neutrino-class behavior on a single sheet. Flag them here; they will be central in chapters 4 and 5.

### 8. The general (m, n) mode

Modes with both m ≠ 0 and n ≠ 0 wind in both compact directions. They carry mass

m_{(m,n)} = (ℏ/c) · √((2π m/L_u)² + (2π n/L_w)²)

and are the candidates for satisfying the closure condition. Whether a given (m, n) satisfies it depends on the standing-wave alignment — which is a phase-pattern question, taken up in Chapter 4.

Note that the mass spectrum is *not* just integer multiples of a single Compton wavelength; the two compact lengths give a **two-parameter discrete grid** in (m, n) space, with mass setting a curve (an ellipse) in the (m, n) plane for each value. This is structurally where the knot families of Chapter 3 will live.

### 9. Energy and momentum of a mode

Compute the four-momentum components for a generic (m, n) mode in motion. The result is a routine extension of metric-mass §5:

E = ℏω
p_S = ℏ k_S       (in the (S₁, S₂) plane)
p_u = ℏ k_u = (2π ℏ/L_u) m   (compact, quantized)
p_w = ℏ k_w = (2π ℏ/L_w) n   (compact, quantized)

The compact-direction momenta p_u and p_w are *internal* — they don't correspond to motion in observable spacetime. They are what shows up as off-diagonal sourcing in Chapter 5 (under the standard KK identification, p_u and p_w map to electric charge in each compact direction).

### 10. Reading the dispersion relation as energy-momentum

State the energy-momentum relation:

E² = (p_S c)² + (p_u c)² + (p_w c)² + (m c²)²

where the *m* on the right is the rest mass of the (m, n) mode. Equivalently:

E² = (p_S c)² + (m_{(m,n)} c²)²

— the rest mass already incorporates the compact-direction momenta. Either form is useful; the second matches the standard relativistic E² = (pc)² + (mc²)² once we identify m_{(m,n)} as rest mass.

This is the result that makes *m_{(m,n)}* operationally indistinguishable from inertial mass in the (t, S₁, S₂) sub-spacetime. The compact-direction structure is hidden inside m_{(m,n)} when viewed from extended spacetime alone.

### 11. What's next

[Chapter 3 — Knots on the torus](03-knots-on-the-torus.md). Take the (m, n) mode family derived here and reframe it geometrically: each (m, n) corresponds to a *closed curve* — a knot — traversing the (u, w) torus. Characterize the family by topological invariants (crossing number, genus, linking) and identify which (m, n) admit non-self-intersecting closures. The single-axis modes (m, 0) and (0, n) become trivially closed (parallel transport around one cycle); the diagonal (m, n) with both nonzero become genuine torus knots.

---

## Open questions flagged in this chapter

| Q | Where it goes |
|---|---------------|
| Are there mode families *other than* (m, n)? (e.g., non-separable solutions) | Chapter 4, when interrogating closure-condition variants |
| What does the energy-momentum tensor T_μν look like for a generic (m, n) mode? | Chapter 5 (gauge promotion analysis builds on T_μν) |
| Does the slow-motion inertial proof of metric-mass §6 generalize to the 2D-compact case? | Cited from metric-mass; verify in the prose expansion |
| What if k_S has a direction (k_{S₁} ≠ k_{S₂}) — does anything depend on the direction? | Chapter 8 of metric-binding, when two knots sit at different (S₁, S₂) |
