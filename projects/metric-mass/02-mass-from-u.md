# Chapter 2 — Solving the wave equation on M

**Status:** Bare outline. Each section is one sentence describing
the derivation step that section will perform. To be filled out
once the outline is approved.

This chapter takes the givens of [Chapter 1](01-foundation.md) —
the manifold M, the bare diagonal metric, the real scalar field φ,
the massless wave equation □φ = 0, and the periodicity condition
on u — and derives what kinds of solutions the wave equation
actually admits. We do not assume the answer; the math is allowed
to say whatever it says.

---

## Bare outline

### 1. Setting up: separation of variables

Try the ansatz φ(t, S, u) = T(t)·X(S)·U(u) and check whether the
wave equation splits cleanly into one equation per coordinate.

### 2. The u-equation under periodicity

Derive what shape U(u) must take given the boundary condition
φ(t, S, u + L_u) = φ(t, S, u), and see whether anything is forced
to be discrete.

### 3. The S- and t-equations

Examine what the remaining equations require of X(S) and T(t),
without yet assuming oscillatory or growing solutions.

### 4. The dispersion relation

Combine the three pieces to find what relation must hold among the
frequency ω, the spatial wavenumber k_S, and the u-mode label.

### 5. Energy and momentum of a mode

Use the standard wave-mechanics identifications p = ℏk and E = ℏω
to translate the dispersion relation from wave-vectors into
physical quantities.

### 6. Reading the dispersion relation as energy-momentum

Compare the result to the relativistic identity
E² = (pc)² + (mc²)² and see whether anything in the dispersion
relation plays the role of a "mass."

### 7. The lowest u-mode

Examine what kind of object the lowest-mode case is, and check
whether it is consistent with a massless object propagating along
S.

### 8. Higher u-modes

Examine what kind of object the higher-mode cases are, and derive
the form of any rest energy that appears.

### 9. Self-consistency of the bare metric

Verify whether the solutions we have found respect the
diagonal-and-constant metric of Chapter 1, or whether they force
any modification.

### 10. Summary of what we derived

List, in plain language, what the math actually establishes — and
what questions remain open for later chapters.

---

## What's next

After Chapter 2, the natural follow-ups depend on what the
self-consistency check (§9) reveals. See the project README for
the tentative downstream chapter arc.
