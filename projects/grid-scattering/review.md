# grid-scattering — framing review (2)

**Scope:** [README.md](README.md) and [Appendix.md](Appendix.md) as of commit ac895bc. The question is whether they are a fair and theoretically sound framing for investigating the goals in [../thoughts.md](../thoughts.md). It covers logical and structural problems only. The project sitting outside accepted physics is not counted as a problem; reasoning that does not follow, or that contradicts what the project itself depends on, is.

Items are numbered for reference. "The arena" means the (x, c) cylinder of README §3, "The arena, cut down".

---

## Fatal

### F1 — Putting x and c in separate groups removes the physics that makes a ring wave a particle

§2 defines a group as a **sheet**, and a sheet as a *plane*: a pair of dimensions. thoughts.md says the same ("A sheet is a plane… so that light/information can propagate in the same way as we have developed so far"). The arena then splits the node into an **x-group and a c-group**, so each group is a single dimension rather than a plane. That is more than a simplification. It changes what the rule does, in three ways.

1. **The particle cannot move.** Under the grouped rule, a c-group only links a node to its ring neighbours *at the same x*. Whatever circulates on the ring at x₀ stays at x₀ for good. It has no momentum along x and cannot be pushed, and the only way it could ever change location is through further overflow events.
2. **The ring energy is not mass in metric-mass's sense.** [metric-mass ch. 2](../metric-mass/02-mass-from-u.md) gets rest mass from *one* wave equation acting on both S and u together. The joint dispersion relation ω² = c²k_S² + (n c/R)² (ω the frequency, k_S the wavenumber along space, n the winding, R the ring radius) is what makes compact momentum act as inertia, p_S = m·v_g (v_g the group velocity). Grouping removes the shared Laplacian, so that relation never forms. The README's identification "a standing wave captive on a loop is exactly what metric-mass identifies as a particle at rest" (§3, §7) does not hold under the README's own rule. architecture.md even notes that Ma ⊗ S mixing "is just motion" ([architecture.md](../ma-domain/work/architecture.md), the scoping note above §3). A rule that forbids that mixing in linear operation forbids motion.
3. **The arena's validation does not transfer.** §7 cites grid-matter's M1 as having "verified the cylinder as a faithful arena". M1 verified the *pooled* N = 4 scatter ([results-m1-m2.md](../grid-matter/work/results-m1-m2.md)). The grouped rule is a different lattice and has not been validated.

Appendix H's justification for P1 has the same confusion. It says the uniform rule keeps modes apart "statistically" while the per-sheet rule keeps energy out "entirely". On a periodic product lattice, the linear uniform rule keeps winding sectors apart *exactly*. The real difference between the two rules is that the pooled rule gives one joint wave equation (KK dispersion, the cutoff, motion) and the grouped rule gives decoupled one-dimensional lines.

The idea in thoughts.md holds up if groups are what both documents say they are: S edges kept apart from *Ma* sheets, with S motion and particle existence still connected somehow. But any partition that separates S edges from compact edges runs into point 1, and the framing has to say how a particle travels through space under the per-sheet node. That question is upstream of every objective.

### F2 — In the arena, "a fit persists, a misfit decays" has no mechanism behind it, so §5's "Does it stay?" has a predetermined answer

A group with two edges scatters with S = (2/2)·J − I = [[0,1],[1,0]]. That is pure transmission: no reflection and no splitting, so the "Y junction" of §2 never occurs in the arena. The c-ring at each x is therefore a lossless delay line. On a ring of M discrete nodes, *every* register pattern is exactly a sum of the M harmonics the ring allows, so there is no such thing as a "wavelength that does not fit". A delay line has nothing that disperses or rejects any pattern. Overflow injected at one node (half each way) is a localized pulse. It will circulate unchanged indefinitely, apart from further saturation events.

Two consequences follow:
- §5's sweep of circumference against drive wavelength measures nothing: everything stays.
- The *selection* that thoughts.md's "the energy has to fit" was meant to supply cannot appear in this arena under any parameters.

(The pooled (x, c) rule does have a selection mechanism: the KK cutoff. A winding-n mode cannot propagate below frequency n·c/R. Grouping removes it; see F1.)

### F3 — The trigger is an amplitude ceiling, but the thresholds actually observed depend on energy per quantum, and differ from sheet to sheet

The mechanism fires when a node's summed input crosses one universal ceiling on *amplitude*. The cross-domain processes thoughts.md sets out to explain have thresholds set by the *energy per quantum*:
- γγ → e⁺e⁻ requires the photons' combined centre-of-mass energy to reach at least 2mₑc² ≈ 1.022 MeV. Two single gamma photons of tiny classical amplitude go over this threshold.
- An intense optical laser has enormous amplitude and stays below it. It makes no pairs until the field nears the Schwinger limit, about 10¹⁸ V/m, where the field becomes strong enough to tear pairs out of the vacuum.
- The thresholds also differ by target: about 1 MeV for an electron pair, about 211 MeV for a muon pair, about 1.9 GeV for a proton–antiproton pair. A single ceiling cannot produce three thresholds.

Appendix I establishes that GRID's energy is the plain sum of squared registers, with no frequency factor. The framing therefore contains nothing that converts "this photon has high ω" into "this node is near its ceiling". As written, the mechanism predicts pair production controlled by intensity, which is the observed behaviour only in the Schwinger regime.

A bridge is available and should be made explicit, because the whole mechanism depends on it. One option: a single quantum ℏω localized in a volume about one wavelength across has an amplitude that grows roughly as ω². That would turn an amplitude ceiling into a frequency threshold, but it brings ℏ (one quantum per wavelength volume) into a classical arena. The per-target thresholds then have to come from the target sheet's fundamental frequency (a fit condition), which F2 shows the arena does not have. Until both pieces are stated, the trigger variable is the wrong one.

---

## Moderate

### M1 — The prescribed overflow rule loses energy, which contradicts the project's own rules, and the loss is already known

§3 tells the rule to clip x and add the excess amplitude, half to each c-edge, and to treat the energy discrepancy as data. Splitting an excess e into e/2 + e/2 carries e²/2 rather than e². Combined with the clip, the energy change is A_max² + e²/2 − A² < 0 for every overflow (A the incoming amplitude, A_max the ceiling, e = A − A_max). The sign is fixed and the size can be computed in closed form, so nothing is learned by measuring it. This contradicts:
- Appendix E ("Fixed by requiring an exactly conserving rule");
- Appendix G ("No transfer claim from a ratio unless measured against an energy-conserving control");
- the README's own §6 step 1 ("a clip that… bleeds energy is no use").

It also repeats the selective-dissipation artifact of Appendix E: clipping removes energy unevenly across modes, so the winding fraction can rise even while the absolute winding content falls. The rotation in Appendix A, or simply splitting the excess as e/√2 to each side, is a conserving version and costs nothing.

### M2 — The ceiling's scope is never defined

"A node whose summed input exceeds the ceiling" could mean three things:
- the x-group's sum;
- each group's sum separately;
- the whole node's sum across groups.

The choice determines the physics:
- Decay (c → x) needs a c-group or whole-node test.
- The "steady low-level traffic" of §3 needs a whole-node test, so that a ring wave and an x wave passing through the same node can push it over together.
- Which registers get clipped, and in what proportion, is not stated.

grid-matter's "node, not edge" finding settles only that the test is not per edge. This is the single most consequential free choice in the rule, and it should be stated as a posit.

### M3 — Overflow throws away momentum along x

"It goes both ways at once — which is what keeps momentum balanced across a ninety-degree turn" balances momentum *along c* only. Whatever x-momentum the clipped part carried disappears. In a symmetric head-on collision that amount is zero, which is why the shotgun picture works. A single pulse strong enough to cross the ceiling alone, or an unequal collision, would lose x-momentum outright. A conserving rule should only let the zero-net-momentum (counter-propagating) part of the node's input overflow. Without that rule, any particle formed would always be created at rest, and by F1 it would stay there.

### M4 — "The principle is forced" claims more than the argument supports

Being discrete and finite forces a **bound**. It does not force **redirection** into other groups. The natural behaviour of a bounded register is either to clip (lose the excess) or to wrap around: base-2 overflow wraps to the opposite sign, so it does not spill. "Saturation is not an extra ingredient… with a base-2 register it is unavoidable" is true of the bound and false of the spill. Sending the excess to the *other groups' edges* is the project's posit and should be labelled as one. The "Honest footing" paragraph should put the boundary between forced and posited there, not between principle and implementation.

### M5 — The "equilibrium" prediction will produce classical equipartition, and that is the wrong target

§3 predicts that two-way traffic settles into an equilibrium between sheets, and calls one-way traffic a possible outright failure. A classical nonlinear lattice relaxes toward **equipartition**: equal energy per degree of freedom. In the arena each node has two x-registers and two c-registers, so the expected end state is about half of all light turned into ring content. That is a real prediction, it is contradicted by the observed world, and it does not depend on any parameter. Appendix B's P6 (domains ordered by state density) is a *quantum* counting argument. It works only because a quantum ℏω has to be paid before a compact mode can be occupied, and the classical arena has no such cost (F3). The framing should either say how the arena avoids equipartition or state that the equilibrium test cannot be interpreted until there is a quantum threshold.

### M6 — Objective 3 cannot be reached from the arena, and no path to it is laid out

Sargent's Q⁵ law, lepton universality and the neutron's 880 s lifetime come out of [leakage-rate.md](../ma-domain/work/leakage-rate.md) as Fermi's golden rule (a transition rate from a matrix element times phase space) with a three-body final state that includes a neutrino continuum. The arena has one compact ring, no hadron or lepton sheets, no neutrino line, and no quanta. Objective 3 also does not say how a classical overflow rate is supposed to correspond to "matrix element × phase space". Without an intermediate arena or a stated correspondence, the objective serves as decoration rather than as a test.

### M7 — Fidelity to thoughts.md: several original goals have been dropped without saying so, and one has changed meaning

Against the originating notes, the README:
- **Answers the opening question by assertion.** thoughts.md asks *whether* nodes access every sheet and how. The README posits the per-sheet node and tests something downstream of it (the rate). The question of whether grouping or pooling is right, which is the subject of F1, is never put to a test.
- **Changes the meaning of "fit".** In thoughts.md the fit is about *energy*: the quantum must fit the target sheet, with the remainder going to ZPE or to momentum in S. In the README it has become a *wavelength* fitting the circumference. That is a different condition, and in the arena it is empty (F2). Appendix E drops the energy staircase for good reasons, but the README still offers "fit" as if the original idea were being tested.
- **Leaves no objective for:** the energy ladder and the durability of ordinary matter, neutron decay, simultaneous creation of an electron and a neutrino, or the stability ordering. Objective 4 ("say what the mechanism forbids") is the only hook, and it is too vague to carry them. Deferring these is defensible, but the README should list them as deferred, so the narrowing to "rate" is visible rather than implicit.

### M8 — The project index contradicts the README

The [../README.md](../README.md) entry says:
- the first work item is "a derivation";
- the mechanism is "in standard terms a parametric process";
- "the linear substrate can never make a particle" because winding is conserved.

The README says the first work item is a simulation and deliberately keeps the parametric label out (Appendix J). It also rests on a different argument: per-sheet separation, not winding conservation under the uniform rule.

---

## Light

- **L1 — "§3a" does not exist.** README §5 says "Run §3a", and Appendix H mentions "README §3a". The arena section is an unnumbered subsection of §3.
- **L2 — No-backscatter claim.** "[It] does not travel back the way it came, because the rule subtracts the register's own prior content" holds only for N = 2. At a Y junction (N = 3) the scatter reflects −1/3 of the amplitude back along the arrival edge. The reflection term is what balances momentum, so the sentence gets the mechanism backwards.
- **L3 — Garbled energy sentence.** "Energy goes as amplitude squared and equal amplitudes are not equal energy" should read something like: splitting an amplitude e into two halves carries e²/2, not e².
- **L4 — Mass but no charge.** "On a single ring there is mass and no charge" assumes the pooled rule; under the grouped rule there is not even mass (F1). Also, the ±n reading in Appendix B (P4) relies on metric-mass's standing-wave commitment, and metric-mass's chapter 3 notes that commitment was itself a later downgrade of the matter/antimatter reading. It should be cited as a commitment, not as a result.
- **L5 — Stability is out of reach in the arena.** With a symmetric overflow rule and constant background traffic, every ring mode eventually decays. Nothing in a single real-valued ring protects a particle. Any decay rate measured there is the rate for an unprotected, neutral mode (closer to a π⁰ than a neutron), and the README should say so before objective 1 is read as "creation and decay".
- **L6 — The seed has no size in simulation units.** Appendix B fixes the background at ½ℏω per mode. The arena has no ℏ and no mapping from amplitude to quanta (F3), so the seed amplitude in simulation units is arbitrary until that mapping exists.
- **L7 — Several overflowing nodes give independent rings.** "Several nodes may overflow at once." Under the grouped rule, each overflowing x-position feeds its own isolated ring. A finite-width collision therefore produces several unconnected ring excitations rather than one coherent object (F1).
