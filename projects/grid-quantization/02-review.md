# Review: Ch. 2 — Information becomes light

Checked against the cube-roots-of-unity junction eigenstructure,
`scripts/band_structure.py`, ch. 3 §3.3, sim-maxwell, and
`scripts/lib.py`. Errors, omissions, and bad logic only.

## Errors / bad logic

**1. §2.1 "a static disturbance ... cannot persist" — false for the
chapter's own symmetric mode.** The intuition is that the −1/3 reflection
"sends back the negative of what is there." But the **symmetric eigenmode
(1, 1, 1)** at a junction has eigenvalue +1 under the rule
(out = (2/3)·3 − 1 = 1) — it is *exactly* static and persists
indefinitely. Across the lattice this is the **ω = 0 flat band** that
ch. 3 §3.3 makes load-bearing (the demonstrated bound CLS sits there). So
"cannot persist" is wrong as stated; it should be qualified to
"non-symmetric disturbances oscillate; the symmetric (breathing) mode is
the static exception — the ω = 0 flat band of ch. 3." Without that
qualification ch. 2 and ch. 3 directly contradict each other.

**2. §2.4 "the two transverse (helical) modes … are the modes that
oscillate and propagate — the photon" — misidentifies a per-junction
basis with a lattice mode.** At a single junction the helical eigenmodes
(1, ω, ω²) and (1, ω², ω), with ω = e^(2πi/3), have eigenvalue **−1**
(out_i = (2/3)·(1+ω+ω²) − ω^(i−1) = −ω^(i−1) since 1+ω+ω² = 0), i.e.
they sit at **ω = π** — the *other* flat band, not on a propagating
band. The actual propagating photons live in the **dispersive bands**
(ch. 3 §3.2). The helical decomposition supplies the polarisation
*basis* for the dispersive bands; the per-junction helical eigenmodes
are themselves non-propagating. The chapter conflates the basis with
the mode.

**3. §2.1 oversimplifies the rule.** "The sign-flipped reflection sends
back the negative of what is there, so the pattern … is driven toward
its own inversion." The rule is out_i = (2/3)·(total) − in_i, not a
pure sign-flip; the next-tick state is only the inverse of the previous
for an antisymmetric eigenmode. The "driven toward its own inversion"
gloss is sharper than the rule warrants and obscures the per-mode
structure that errors 1 and 2 turn on.

**4. §2.4 parenthetical: "the symmetric mode is left unchanged" while
"the transverse modes carry the sign-flip — the restoring effect."**
This is internally correct (symmetric: eigenvalue +1; helical:
eigenvalue −1) but it directly contradicts §2.1's "static cannot
persist" — the very next paragraph names the static-persistent mode the
earlier paragraph denied existed.

## Material omissions

**5. The simulated dynamics do not carry helicity.** §2.4 says spin
"requires complex (phasor) amplitudes" — true. But `scripts/lib.py`
uses **real** amplitudes (`a_fwd, a_bwd`); the cited sim therefore does
*not* implement the helicity / spin story §2.4 tells, and getting it
needs the Tier-2 complex-amplitude work
([tier2-design.md](work/tier2-design.md) §4 protocol, which the project
elsewhere notes is unbuilt). The chapter should flag this — a reader
opening lib.py finds no helicity, period.

**6. The per-edge θ ↔ per-junction helical-complex-phase link is
asserted, not described.** §2.4a honestly says the KK / helical-junction
coincidence is "asserted here, not yet shown." Beyond honesty, the
chapter slides between "the phase the helical modes use" (a complex
coefficient across three edges, lives in C) and "the per-edge compact
phase θ" (one S¹ per edge, lives in R/2π) as if they're the same
object. They aren't, and the chapter doesn't describe how per-edge θ's
combine into a per-junction helical complex amplitude.

**7. Inherits ch. 1's state-model conflation
([01-review.md §3](01-review.md)).** "Phase-carrying edges" language
sits on ch. 1's claim that each edge carries one compact phase θ, while
the rule the chapter discusses operates on continuous real amplitudes.
The conflation propagates rather than being repaired.

## Imprecisions

**8. §2.3 "linear means non-dispersive ... a wave packet holds its
shape"** is correct but missing its because: linear ω(k) means group
velocity *equals* phase velocity, which is why the packet doesn't
disperse. Without that step the sentence reads as ipse dixit.

**9. §2.3 "the one-edge-per-tick speed of Chapter 1" vs the measured
0.41."** Same imprecision as ch. 1 §1.3: one-edge-per-tick is the
*causal ceiling* (= L/τ), and the photon's phase velocity (0.41) is
slower. The chapter treats them as the same speed.

---

## Author response

Integrated all nine items. The two-sources framing (propagation ←
spring; spin/handedness ← phase / ℵ-line) survives intact; the
corrections sharpen *what the helical decomposition is*, not what the
user's claim is. Notes:

- **Item 2 (the big one — helical eigenmodes mis-identified as
  propagating photons).** Verified the algebra: per-junction helical
  eigenvectors carry eigenvalue −1 under (2/3)·J − I, which on the
  lattice eigenphase circle is ω = π (the *other* flat band of ch. 3),
  not a dispersive band. Rewrote §2.4 so the helical eigenmodes are
  named the **polarisation basis** for the transverse sector; the
  propagating photon is the lattice-wide Bloch mode in a dispersive
  band (§3.2); the helical basis is what that mode carries at each
  junction. The §2.1 parenthetical now correctly says the symmetric
  mode is preserved by the rule and reappears as the ω = 0 flat band.
- **Items 1, 3, 4 (static-can't-persist vs symmetric-mode persistence).**
  Handled in §2.1 by qualifying to *transverse* disturbances and
  flagging the symmetric exception in a parenthetical that points to
  §2.4 and §3.3 — kills the §2.1 ↔ §2.4 contradiction in one stroke.
- **Item 5 (sim does not carry helicity).** Flagged explicitly in §2.4
  with a pointer to tier2-design §4 for the complex/phasor extension.
- **Item 6 (per-edge θ ↔ junction-helical complex phase).** Added a
  one-sentence bridge in §2.4: discrete Fourier transform of the three
  edges' e^{iθ_k} onto the cube-root weights. Not a full derivation;
  enough to stop the slide between the two representations.
- **Items 8, 9, 7.** Applied: v_g = v_p reason given for non-dispersive;
  causal-ceiling vs measured-wave-speed distinguished in §2.2 / §2.3;
  ch. 1 conflation fixed in ch. 1.
