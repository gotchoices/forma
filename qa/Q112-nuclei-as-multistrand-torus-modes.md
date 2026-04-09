# Q112. Nuclei as multi-strand torus modes

**Status:** Open — speculative framing
**Related:**
  [Q105 (atoms-as-cross-sheet-modes)](Q105-atoms-as-cross-sheet-modes.md),
  [Q108 (shell-capacity-from-knot-saturation)](Q108-shell-capacity-from-knot-saturation.md),
  [Q109 (mode-stability-and-composite-fission)](Q109-mode-stability-and-composite-fission.md),
  R47 (proton filter — (1,3) hypothesis),
  R52 (self-field moment),
  Q89 (fusion as mode transition)

---

## 1. The observation

In MaSt, the (1,3) hypothesis identifies the proton as a single
torus mode with n₁ = 1, n₂ = 3 on Ma_p.  The proton's three
"quark-like" antinodes are the 3 standing-wave nodes around
the tube direction.

A natural question: what about modes with higher integer
windings — (2,6), (3,6), (3,9), (4,12), etc.?  These have
the same topological character as (1,3) at integer multiples,
and their energies are approximately integer multiples of the
proton mass at the proton aspect ratio (r_p ≈ 8.9):

| Mode | gcd | Strands | Each strand | E / E_(1,3) |
|------|-----|---------|-------------|-------------|
| (1,3) | 1 | 1 | (1,3) | 1.00 |
| (2,6) | 2 | 2 | (1,3) | 2.00 |
| (3,9) | 3 | 3 | (1,3) | 3.00 |
| (4,12) | 4 | 4 | (1,3) | 4.00 |

A (p,q) torus knot has gcd(p,q) connected components.  When
gcd(p,q) = d > 1, the curve becomes d disjoint copies of the
(p/d, q/d) torus knot.

So **(d × 1, d × 3) is exactly d disjoint copies of the (1,3)
proton mode, sharing a single torus sheet.**  The energy scales
linearly with d (to leading order, ignoring inter-strand
binding), reproducing the mass scaling of d protons.

## 2. The hypothesis

**Atomic nuclei are multi-strand torus modes on Ma_p.**
A nucleus with mass number A and atomic number Z is a torus
mode whose strand structure encodes the nucleon count and the
proton/neutron split.

For a pure proton ensemble, the natural identification:
- Hydrogen (¹H, A=1, Z=1): single (1,3) strand
- Two protons sharing a sheet: (2,6) — 2 strands
- Three protons sharing a sheet: (3,9) — 3 strands
- Four protons sharing a sheet: (4,12) — 4 strands

For nuclei with neutrons, additional structure is needed (see
§5).  But the basic claim is that **a nucleus is one mode on
one sheet**, not a collection of separate sheets pulled
together by a force.

## 3. What this would explain

### 3.1 Nuclear binding energy

If A nucleons share one sheet rather than existing as A
separate sheets, the energy is *less* than A times the single-
particle energy by the amount of the interaction between
strands sharing the sheet.  This deficit is the binding energy.

> M_nucleus = A × M_nucleon − BE

The MaSt prediction: BE comes from the geometric cost of
maintaining a multi-strand mode versus single-strand modes on
separate sheets.  Multiple strands on one sheet share the
defect cost (the αmc² Coulomb term), so the total defect cost
is less than A × αmc² — and the savings is the binding energy.

### 3.2 Strong force as sheet-sharing

The "strong force" in standard physics is the residual exchange
force between color-neutral nucleons.  In MaSt, it would be
the geometric coupling between strands on the same torus.
There is no separate force — just the topological constraint
that strands cannot leave the shared sheet without destroying
the mode.

This would directly connect to Q95 (strong force as internal
EM on Ma_p), with the addition that the "internal" extends
across all strands on the same sheet.

### 3.3 Magic numbers

Nuclear physics observes that nuclei with certain proton/
neutron counts (2, 8, 20, 28, 50, 82, 126) are unusually
stable — the "magic numbers."  These are explained in standard
physics by closed shells in the nuclear shell model.

In MaSt, magic numbers would correspond to **mode counts at
which the multi-strand topology is specially symmetric.**  For
instance, certain strand arrangements may have higher symmetry
or lower defect cost than neighboring values, producing local
stability minima.

This is a concrete prediction: the magic numbers should be
derivable from the topology of multi-strand torus modes on
Ma_p, without invoking shells or quantum numbers.  If a
calculation shows that strand counts of 2, 8, 20, 28, 50, 82,
126 are topologically privileged, it would be a strong piece
of evidence.

### 3.4 Beta decay

In standard physics, beta decay (n → p + e⁻ + ν̄_e) is a
weak interaction where one quark inside a neutron changes
flavor.

In MaSt with multi-strand modes, beta decay could be a
**strand identity change**.  One strand on the multi-strand
nucleus mode reorganizes from a (1,3) "neutron-flavored"
configuration to a (1,3) "proton-flavored" configuration,
with the difference (charge, spin, and kinetic energy)
emitted as an electron + antineutrino.

The "flavor" of a strand would be its winding sign or its
phase relationship to neighboring strands.  Beta decay then
becomes a topological reconfiguration of one strand, not a
quark-level process.

### 3.5 Fission and fusion

**Fission:** a multi-strand mode (e.g., A=235) becomes
unstable and splits into two smaller multi-strand modes
(A=144 + A=89 + neutrons).  This is a topological
restructuring: one connected mode separates into two
disconnected modes.  The energy released is the difference in
binding energy (more strands per sheet → lower defect cost
per strand → higher binding → less mass).

**Fusion:** two single-strand or low-strand modes (e.g., 2 ×
(1,3) deuterium components) merge into a multi-strand mode
(e.g., (4,12) helium).  Again topological restructuring.
Energy released because the multi-strand mode has lower mass
per nucleon than the separate modes.

This connects directly to Q89 (fusion as mode transition) —
the threshold for fusion is the energy needed to deform two
modes into a single multi-strand mode.

## 4. Quantitative predictions

### 4.1 Binding energy scaling

For a multi-strand (d × 1, d × 3) mode on Ma_p, the binding
energy comes from the geometric coupling between d strands
sharing one sheet.

If the coupling is dominated by pairwise interactions (each
pair of strands couples), the binding scales as d(d−1)/2 — the
number of pairs.  This gives B(A) ∝ A(A−1)/2 ∝ A² for large A.

But the observed nuclear binding energy per nucleon is roughly
constant (~8 MeV) for A > 12, with a broad maximum around iron
(A = 56).  This suggests the interaction is **saturated** —
each strand interacts only with its nearest neighbors on the
sheet, not with all others.

Saturation in MaSt would be geometric: a strand can only
"share defect cost" with strands within a certain distance on
the sheet.  Distant strands don't interact.  This produces
linear scaling B(A) ∝ A, matching observation.

The saturation distance becomes a measurable parameter — and
its value should follow from the GRID lattice scale and α.

### 4.2 The semi-empirical mass formula

The Bethe-Weizsäcker formula gives nuclear binding as:

> B(A,Z) = a_v A − a_s A^(2/3) − a_c Z²/A^(1/3) − a_a (A−2Z)²/A + δ

The five terms (volume, surface, Coulomb, asymmetry, pairing)
should each have a MaSt interpretation:

| Term | MaSt mechanism (proposed) |
|------|--------------------------|
| Volume (a_v A) | Saturated strand-strand binding from sheet sharing |
| Surface (-a_s A^(2/3)) | Strands on the boundary of the shared region have fewer neighbors |
| Coulomb (-a_c Z²/A^(1/3)) | Repulsion between charged strands (defect cost grows with charge density) |
| Asymmetry (-a_a (A-2Z)²/A) | Mismatch between proton-flavored and neutron-flavored strands costs energy |
| Pairing (δ) | Even-strand-count configurations have additional symmetry |

A successful MaSt derivation would reproduce the five
coefficients (a_v ≈ 15.5 MeV, a_s ≈ 16.8 MeV, a_c ≈ 0.72 MeV,
a_a ≈ 23 MeV, δ ≈ 11/√A MeV) from torus geometry.  Even
qualitative agreement on the ratios would be significant.

### 4.3 Specific test cases

| Nucleus | A | Z | Binding (MeV) | MaSt structure |
|---------|---|---|---------------|----------------|
| ²H | 2 | 1 | 2.22 | (2,6) — 2 strands |
| ³He | 3 | 2 | 7.72 | (3,9) — 3 strands |
| ⁴He | 4 | 2 | 28.30 | (4,12) — 4 strands, magic |
| ⁶Li | 6 | 3 | 31.99 | (6,18)? |
| ¹⁶O | 16 | 8 | 127.62 | (16,48), magic Z |
| ⁵⁶Fe | 56 | 26 | 492.26 | maximally bound |

The deuteron is the cleanest test: the (2,6) mode has 2× the
proton's energy, minus a small correction for the inter-strand
binding.  If the MaSt model gives B(²H) ≈ 2.22 MeV from the
torus geometry of (2,6), it would be a striking confirmation.

## 5. The neutron problem

The biggest challenge: most nuclei contain neutrons, not just
protons.  A pure (d × 1, d × 3) mode has all strands identical
— it represents d protons, not a mix of protons and neutrons.

Several possibilities:

### 5.1 Strands with different signs

The (n₁, n₂) mode notation does not distinguish positive and
negative winding.  If different strands of a multi-strand mode
can carry opposite signs (some n₁ = +1, others n₁ = −1), the
total charge can be anything from −d to +d in steps of 2.

For deuterium (Z=1, A=2): one (+1,3) strand and one (−1,3)
strand.  But this gives net charge 0, which is wrong.

This doesn't work as stated.  Sign-mixing would give even
charges only.

### 5.2 Strands with different mode types

If strands within a multi-strand mode can have different
(n₁, n₂) values — e.g., (1,3) and (1,3') with the prime
denoting a phase variant — the proton and neutron could be
two different strand types.

This is closer to the standard view: protons and neutrons are
distinct constituents.  In MaSt terms, they would be different
single-strand modes that can coexist on a shared sheet.

But it's not clear the multi-strand torus mode formalism
allows this — the gcd argument assumes all strands are
identical.

### 5.3 Strand orientation

Each strand has an internal phase (e.g., n₅ winding) that
distinguishes its identity.  Two strands with the same
(n₁, n₂) but different n₅ are different particles.  Beta
decay would be one strand changing its n₅ value, emitting an
electron + antineutrino.

This is the most promising option.  It preserves the
multi-strand topology while allowing different strand
identities.  But it requires extending the mode notation to
include strand-internal quantum numbers.

### 5.4 Free neutrons

If the neutron is unstable in isolation (true) because it
needs to be part of a multi-strand configuration with at least
one proton-strand to be stable, this would explain why free
neutrons decay (β) but bound neutrons (in stable nuclei) do
not.  The decay would be a strand-identity change driven by
the absence of a stabilizing partner.

## 6. Sub-questions

1. **Does the (2,6) mode actually exist as a stable
   configuration?**  R47/R50 mode filtering would need to
   check this.  If (2,6) has a stable single-mode realization,
   it is a candidate for the deuteron.

2. **What is the binding energy of (2,6) relative to two
   separate (1,3) sheets?**  Compute the energy difference
   from the MaSt formula and compare to the observed deuteron
   binding (2.22 MeV).

3. **Can magic numbers be derived from multi-strand
   topology?**  This would be a major calculation.  Test:
   compute the energy of (d × 1, d × 3) modes for d = 1 to
   100 and check whether d = 2, 8, 20, 28, 50, 82 are local
   minima.

4. **How do neutrons fit?**  See §5.  This is the main
   structural problem.  Without resolving it, multi-strand
   modes can only describe pure-proton systems.

5. **What happens at very high A?**  Standard physics
   predicts no stable nuclei beyond Z ≈ 82 (lead).  Does the
   MaSt model produce a similar cutoff naturally?  This would
   be a clean test.

6. **What is the relationship to atomic structure (Q105,
   Q108)?**  If nuclei are multi-strand Ma_p modes and atoms
   are cross-sheet modes (Ma_e + Ma_p), the multi-strand
   nucleus would couple to a multi-strand electron cloud.
   This could connect to the periodic table directly.

7. **Does this conflict with the "(3,6) = 3 quarks" picture
   from the original proton hypothesis?**  Yes.  In that
   picture, (3,6) was a single proton with 3 internal quark
   structures.  In the multi-strand picture, (3,6) is 3
   electron-mode strands sharing a sheet.  The two
   interpretations cannot both be right.  R47 is the
   relevant study to revisit.

## 7. Why this is worth pursuing

If multi-strand torus modes can describe nuclei, MaSt would
gain access to the entire field of nuclear physics with a
single new postulate (modes can have multiple strands).  The
payoff would be:

- Nuclear binding energy from geometric first principles
- Strong force as sheet-sharing, no separate force
- Magic numbers from topology
- Fission/fusion as mode transitions
- Beta decay as strand identity change

The risk is that the framework can't accommodate neutrons
cleanly, in which case the picture is limited to pure-proton
systems and is not really nuclear physics.

The first concrete computation: take the (2,6) mode on Ma_p
at the proton aspect ratio, compute its energy and structure,
and compare to two separate (1,3) modes.  If the energy
difference is in the range of 1–10 MeV (not 0 and not 100s
of MeV), it's worth pursuing.  If it's wildly off, the
multi-strand picture has serious problems.

## 8. Status

This question is **purely speculative** as of writing.  No
calculations have been done.  The torus knot decomposition
(d × 1, d × 3) = d strands of (1,3) is geometric fact, but
whether this corresponds to physical nuclei is untested.

The next concrete step would be to compute the (2,6) mode
energy on Ma_p at r_p ≈ 8.9 and compare to 2 × m_p − 2.22 MeV
(the deuteron mass).  If the agreement is within ~10%, the
hypothesis is worth a full study.  If not, the picture needs
significant revision.
