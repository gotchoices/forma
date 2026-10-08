# grid-scattering — framing review (5)

**Scope:** The project as of commit 66422ed: [README.md](README.md), [work/measurements.md](work/measurements.md), [work/STATUS.md](work/STATUS.md), [work/junction-geometry.md](work/junction-geometry.md), [scripts/cylinder.py](scripts/cylinder.py), and the project index entry. It covers logical and structural problems only.

Checks run for this review (none committed):
- **Exact Bloch spectrum of the gradient coupling.** One tick (rotate, then propagate) is linear and translation-invariant, so the spectrum can be computed exactly for each (k_x, k_c), the wavenumbers along x and around c. A parameter search matched measurements.md §M5's published eigenvalues at **nc = 24, g = 3.0** (residual 10⁻⁴). The tables below use those values.
- **A symmetric variant of the same coupling**, in which each compact register couples equally to both x registers, run as a diagnostic.

---

## Fatal

### F1 — The gradient coupling does not give relativistic dispersion: the "rest" mode drifts, and the band is lopsided

The README's status line, §3b and STATUS mark motion as **resolved** on the strength of §M5. The evidence is "dispersion against √(k² + ω₀²): 0.0%, 0.7%, 0.5%, −0.6% at k_x = 0, 0.03, 0.06, 0.10" and "group velocity +0.159". (Group velocity v_g = dω/dk is the speed at which a wave packet travels.) Those samples cover only **positive k_x up to 0.10**. Over the full range, the heavy n = 1 branch of the (+x, +c) block is:

| k_x | ω | KK √(k_x² + ω₀²) | error | v_g | KK v_g = k_x/ω |
|---:|---:|---:|---:|---:|---:|
| −0.20 | 0.2830 | 0.3579 | −20.9% | **+0.044** | −0.559 |
| −0.10 | 0.2884 | 0.3132 | −7.9% | **+0.066** | −0.319 |
| 0.00 | 0.2968 | 0.2968 | 0 | **+0.107** | 0 |
| +0.10 | 0.3112 | 0.3132 | −0.6% | +0.191 | +0.319 |
| +0.20 | 0.3377 | 0.3579 | −5.7% | +0.356 | +0.559 |
| +0.30 | 0.3849 | 0.4220 | −8.8% | +0.592 | +0.711 |

Three conclusions follow:

1. **A wound mode at rest is not at rest.** At k_x = 0 it moves at +0.107. In the mirror block (−x, −c) it moves at −0.107. A standing ±n wave, which is the object metric-mass calls a particle at rest, therefore splits: its +n half drifts one way and its −n half the other.
2. **The band is not symmetric in k_x.** ω(−0.1) ≠ ω(+0.1), and for negative k_x the group velocity points the wrong way. Kaluza–Klein dispersion is even in k_x by construction. The 0–0.6% agreement holds only because the samples sat on the side, and in the range, where a fitted hyperbola and this tilted band happen to cross.
3. **The quoted v_g = 0.159 at k_x ≈ 0.07 is already 30% below KK's 0.23.** Being "between 0 and 1" is necessary for a massive particle but not sufficient.

The cause is the one flagged in the previous review (F1, L2). The coupling pairs +x with +c and −x with −c, so each compact direction hybridizes with only one x direction. Making the angle depend on winding, g·(1 − cos k_c), fixed the photon's mass gap. It did not touch this pairing, so the drift is still there.

**Diagnostic, not a fix.** If each compact register couples equally to both x registers (same angle law, same g), the drift disappears: the spectrum becomes even in k_x and v_g(0) = 0. Two problems remain:
- the heavy branch is still flatter than KK (ω = 0.3204 at k_x = 0.2, against 0.3596);
- the light wound branch becomes *exactly* massless at k_x = 0.

So the general requirement stands. A coupling that gives KK motion has to join ±x movers through c, with the right strength. None of the variants tried so far does.

With this result, the README's "**Status: active … The motion obstruction … is resolved**" and STATUS's "Wound modes have mass and move" are not supported. The project's own §M4 negative result (a made particle does not translate) stands, and the gradient coupling as built has not overturned it.

---

## Moderate

### M1 — The linear sector now duplicates what the pooled scatter already does correctly

Under the relaxed posit, unwound content (k_c = 0) never crosses linearly, and wound content crosses at a rate tied to winding. On a translation-invariant lattice, the Bloch sectors k_c = 0 and k_c ≠ 0 never mix linearly under *any* such rule. That includes the ordinary pooled scatter, as grid-matter's M1 verified and as the first review pointed out. So the linear half of the posit no longer distinguishes this model from the standard one. Meanwhile:
- the pooled N = 4 scatter is strictly node-local;
- it is reciprocal;
- it already gives KK dispersion to within 2% with v_g(0) = 0 ([grid-matter ch. 4](../grid-matter/04-matter-waves-and-de-broglie.md)).

The bespoke Fourier-space coupling does worse on all three counts. What remains distinctive about the project is the **overflow** rule, which is also what §Scope says is under test. The obvious configuration is the pooled scatter for the linear sector with overflow on top. The old E5 discriminator (pooled against grouped) is the experiment that would show whether grouping buys anything that can be observed. Unless a difference turns up, the §2 posit should be restated as a statement about the nonlinear channel only.

### M2 — The README contradicts itself on the main objective

- **Status line and §3b:** active, motion resolved.
- **§3 "But it cannot move":** "Two attempts to supply motion have been withdrawn."
- **§5:** "What was not [established]: a particle that moves."
- **§6 "Revival conditions":** "The project is parked rather than closed." Its condition 2, a coupling that leaves k = 0 alone, is the one §3b says has been met.
- **§3 "The arena, cut down":** still describes the non-local argmax as the rule ("lets only the single largest-|T| position… overflow"), but the script now defaults to the local rule.
- **§3 "What has been measured":** still reports 99.95% (one-point) and "1.5×, 0.370 against 0.252", which contradict the ~5× in the paragraph above it and in §M3.
- **§2:** still describes the *constant* rotation family as the dial that realises the posit ("weak always-on"), which §3 withdraws.
- **Ordering:** §3b comes before §3a.

Elsewhere:
- **junction-geometry.md** has not been updated. §2 and §3 still claim that "a shared coupling, however weak, gives one wave operator … ω² = c²k² + ω₀²" and that "ordinary propagation … is carried by the weak linear coupling". STATUS has retracted both.
- **STATUS "Queued — experiments"** is unchanged from the last two reviews:
  - E0 cites the withdrawn 1.5×;
  - E2's pre-registration uses the withdrawn soliton logic;
  - E6 is marked done with the withdrawn 12–58×;
  - E7 says the books will not balance.
- **The "Queued — writing" items** are stale.

The project index entry should be checked against whichever verdict survives F1.

### M3 — The resonance claim is thin, and was measured without the coupling it now depends on

- **Three seeds, with overlap.** At nc = λ the seeds give 0.0215–0.0641. Seed 3 (0.0215) is only 1.2× the strongest off-resonant run (nc = 26, seed 2, 0.0185). "Resonance is real at roughly 5×" (the §M3 heading) overstates an average of three runs with no error bar. The README's "a lead, not a result" is the right wording, and §M3 and STATUS ("Settled") should match it.
- **Small absolute fraction.** About 4.5% of the energy ends up wound at resonance. Whether that counts as "a particle made" depends on a threshold that has not been stated.
- **No frequency sweep.** Nothing confirms that the peak tracks ω = 2πm/nc at fixed nc with the conserving rule. The only sweep (E6) was withdrawn, but STATUS still marks it done.
- **Measured with g = 0.** With the coupling on, the n = 1 rest frequency moves from the bare ring value 0.2618 to 0.2968, a 13% shift. The argument that "the threshold lands at the particle's own mass scale" now has two candidate frequencies, and the coupled model has to say which one the resonance locks to. That needs measuring with g > 0.

### M4 — The ceiling still bounds nothing

The previous review's M2 is unaddressed. The overflow rotates by gain × (excess) and leaves registers above "the ceiling", yet §2 still motivates saturation as a register that "holds only so much". The reverse channel now nets against the forward one (angle ∝ over − back), so when both fire at a node they partly cancel. That makes the crossing a smooth function of the difference between the two groups' excesses, which is even further from a capacity bound. Either implement a bound (rotate exactly enough to bring |T| back to sat), or redraw the forced/posited boundary in §2.

### M5 — The coupling is neither weak nor local, and its mass tower is not monotonic

- **Not weak.** At g = 3 the per-tick angles are 0.10, 0.40 and 0.88 rad for n = 1, 2, 3. For wound content, the regime the posit was about, space and sheet exchange strongly.
- **Not monotonic.** The angle law g(1 − cos k_c) is periodic in the angle. At nc = 24 it reaches 6 rad at n = 12, which is equivalent to −0.28 rad, so the coupling, and the mass tower with it, is not monotonic in n at high winding. That needs either a reason or a bound on n.
- **Not local.** The rule is applied in the c-Fourier basis. measurements.md acknowledges that it is not strictly local and that light's masslessness is built in by design. Both points belong in the README's §3b, not only in the measurements file.

### M6 — §M4 and §M5 cannot be reproduced from the repo

measurements.md opens with "All runs below are reproducible from the command lines given". §M4 (ring seeding, the angled shot, centroids) and §M5 (the 4096-tick time series, the Bloch eigenphases, the group velocity) give no command lines. `cylinder.py` also has no options for seeding a ring, launching a packet, recording a time series or computing a Bloch spectrum. The negative motion result and the positive dispersion claim are the two most consequential numbers in the project, and neither can be checked from what is committed. Per [AGENTS.md](../AGENTS.md), these capabilities belong in the script with argparse options.

---

## Light

- **L1 — The lesson in STATUS.** STATUS records that the rule which works "was named in the review as an open question and simply had not been tried". The previous review specified a coupling that joins +x to −x movers through c. The rule tried joins +x only to +c (F1), so it is not that rule. The lesson about overreaching from a few cases is sound, and it applies in both directions: the "resolved" verdict also rests on a few samples.
- **L2 — The second branch.** The light wound branch (ω = 0.035 at n = 1 in the implemented rule, exactly 0 in the symmetric variant) is an x-travelling wave modulated around c: light that carries winding. The 3-torus comparison is apt. It is also the branch a random seed excited preferentially (§M5), so it matters for any packet experiment, not only as a spectral curiosity.
- **L3 — Packet construction.** §M5 reports that three packet attempts failed because a mixture excites both branches. The Bloch eigenvectors are already computed, so a single-branch packet is a superposition of one branch's eigenvectors over a narrow band of k_x, built in Fourier space. Under the current rule it would show the F1 drift directly.
- **L4 — The forward/reverse netting** in `step()` (angle ∝ over − back) is a modelling choice that the README does not mention. It makes creation and decay at a single node mutually exclusive within a tick.
