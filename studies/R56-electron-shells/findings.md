# R56: Electron shell structure — Findings

## Track 1: Classical packing of distributed-charge electrons

### F1. Shell structure does NOT emerge from geometric packing

Energy minimization of Compton-scale charged spheres around a
point nucleus produces a smooth energy landscape with no
discontinuities at 2, 8, or 18 electrons.

| Shell 1 (polar) | ΔE per electron (keV) |
|---|---|
| N=1 | −38.4 |
| N=2 | −36.7 |
| N=3 | −35.5 |
| N=4 | −33.8 |
| N=5 | −8.1 |

No sharp closure at N=2.  The cost decreases smoothly.

| Shell 2 (equatorial ring) | ΔE per pair (keV) |
|---|---|
| N_ring=2 | −70.6 |
| N_ring=4 | −64.5 |
| N_ring=6 | −59.3 |
| N_ring=8 | −53.4 |
| N_ring=10 | −47.5 |

No discontinuity at 8.  Smooth diminishing returns.

Both electron size models (R = 751 fm and R = 386 fm) give
the same qualitative result: smooth energy decrease, no shell
closure.

### F2. Why classical packing fails

The distributed charge makes close-range repulsion SOFTER,
which makes packing EASIER — the opposite of what's needed
for shell closure.  In a purely classical model, there's no
mechanism to make one specific electron count per shell
energetically special.  The 2, 8, 18 structure requires:

1. **Quantized angular momentum** — discrete orbital shapes
   (s, p, d, f) limiting configurations per energy level
2. **Pauli exclusion** — at most 2 electrons per orbital

Both are quantum rules absent from classical packing.

### F3. Conclusion: shell structure is genuinely quantum

The MaSt insight (electrons have Compton-scale spatial extent)
is real but insufficient to derive shell structure.  The Pauli
exclusion principle is not a geometric consequence of packing.
This is a negative result — and it's informative: it marks the
boundary between what geometry alone explains (particle masses,
charge, spin) and what requires quantum mechanics (multi-
particle state counting).

### Track 1 status

**Complete — negative result.**  Classical packing of
distributed-charge electrons does not reproduce 2, 8, 18.

---

## Open: MaSt interpretation of Pauli exclusion

Track 1 showed that classical packing fails.  But MaSt is not
purely classical — its particles are standing waves with
quantized winding numbers.  The Pauli exclusion principle, in
standard QM, says "no two identical fermions can occupy the
same quantum state."  What does this mean in MaSt language?

### The quantum numbers and their MaSt analogs

In standard QM, an electron in an atom has four quantum numbers:

| QM number | Values | Meaning | MaSt analog? |
|-----------|--------|---------|-------------|
| **n** (principal) | 1, 2, 3, ... | Energy level / shell | Distance from nucleus in S? Or mode number in Ma? |
| **l** (angular momentum) | 0 to n−1 | Orbital shape (s, p, d, f) | Winding pattern around nucleus? |
| **m** (magnetic) | −l to +l | Orbital orientation in space | Orientation of winding axis in S? |
| **s** (spin) | +½ or −½ | Intrinsic angular momentum | Tube winding sign: n₁ = +1 or −1 |

The Pauli principle: no two electrons can share all four.

### The "2" in 2n²: two tube orientations in Ma

In MaSt, the electron is mode (1, 0) on the e-sheet (in the
s ≈ 0 frame).  The tube winding n₁ = +1 gives spin +½; the
opposite winding n₁ = −1 gives spin −½.  These are NOT two
different particles — they are two orientations of the SAME
mode on the SAME torus.

**Hypothesis:** two electrons with opposite tube winding
(+1 and −1) can coexist at the same location in S because
their Ma structures are complementary — they "interleave"
on the torus without conflicting.  They are counter-rotating
standing waves on the same resonator.  A third electron would
need the same tube winding as one of the first two, creating
a conflict on Ma — a resonance that destructively interferes.

This gives the factor of **2** in 2n² — two electrons per
spatial orbital, one for each tube orientation.

### What about l, m, n?  The spatial quantum numbers

The remaining quantum numbers (n, l, m) describe how the
electron distributes itself in S around the nucleus.  In MaSt:

- **n (principal):** the radial distance from the nucleus.
  Each shell is a different distance, set by the balance
  between nuclear attraction and electron-electron repulsion.
  This IS a spatial (S) phenomenon.

- **l (angular momentum):** the shape of the electron's
  spatial distribution.  l = 0 is spherical (s orbital);
  l = 1 has two lobes (p orbital); l = 2 has four lobes (d).
  In MaSt, these might correspond to the electron torus's
  ORIENTATION relative to the nucleus — a torus can be
  oriented with its axis pointing radially (l = 0?), or
  tangentially (l = 1?), or at various angles.

- **m (magnetic):** the orientation of l relative to an
  external axis.  For l = 1: three orientations (m = −1, 0, +1)
  corresponding to the three spatial directions.

### Possible hypotheses for further tracks

**Hypothesis A: The "2" is topological, the rest is spatial.**
Two electrons fit per orbital because of tube winding
complementarity (Ma phenomenon).  The number of orbitals per
shell (1, 3, 5, 7 for s, p, d, f) is the number of distinct
spatial orientations of the electron torus around the nucleus
(S phenomenon).  Shell structure = Ma constraint (×2) times
S constraint (number of orientations).

**Hypothesis B: Torus orientation quantization.**
The electron torus at Compton scale (~5 pm) orbiting a nucleus
at Bohr scale (~50 pm) has a discrete set of stable orientations,
like a gyroscope in a gravitational field.  The number of stable
orientations at distance n from the nucleus is n² (from the
geometry of orientations on a sphere of radius n × a₀).  Each
orientation holds 2 electrons (tube winding ±1).  Total per
shell: 2n².

**Hypothesis C: Standing-wave quantization in S.**
The electron's Coulomb interaction with the nucleus creates a
potential well in S.  Standing waves in this well (the
Schrödinger solutions) have discrete angular patterns — the
spherical harmonics.  The number of angular patterns at
principal quantum number n is n².  This is standard QM, but
with the MaSt reinterpretation: the "wave" that has standing
modes is not an abstract probability amplitude but the
electromagnetic field of the electron torus as it distributes
around the nucleus.

**Hypothesis D: Interference exclusion.**
Two electron tori with the same tube winding at the same
position in S would create destructive interference in their
Ma fields — the standing waves cancel.  Opposite tube windings
don't cancel (they're orthogonal modes).  This is Pauli
exclusion as destructive interference on the Ma torus, not as
an abstract quantum rule.

### Recommended next tracks

| Track | Hypothesis | Approach |
|-------|-----------|----------|
| 2 | A (topological ×2, spatial rest) | Count stable torus orientations around a Coulomb center at each shell radius |
| 3 | B (orientation quantization) | Compute the classical orientational modes of a gyroscopic torus in a 1/r potential |
| 4 | D (interference exclusion) | Model two co-located electron tori on Ma and show same-winding modes destructively interfere |

Track 4 (interference exclusion) is the most distinctively
MaSt — it would derive Pauli exclusion from the standing-wave
nature of particles, rather than postulating it.  If two
same-spin electrons at the same location produce destructive
interference on Ma, the exclusion principle follows from wave
physics, not from an axiom.
