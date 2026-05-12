# Review — work-ch9.md

The split between work-m8a (σ alone, Ch 8) and work-ch9 (σ + ε together, Ch 9) is clean and the cross-references between them are healthy. One substantive issue and two minor cleanups.

---

## Issue 1: §7 (Parametrization choice) is now stale

§7 presents View A vs View B as an open architectural decision with three commitment options, recommending that "Ch 9 should commit explicitly." That commitment has already been made — the discipline pass settled this in [Ch 1 §3, §4](01-foundation.md):

- σ_uw (bare σ as shorthand) is the working parametrization.
- s is the lattice-shear translation label for R-track-study correspondence (s = σ_uw/ε).
- The two are different numbers, not interchangeable; transform documented.
- |σ_uw| < 1 is a binding positive-definiteness constraint, not a parametrization artifact.

This is effectively option (III) of §7.3 (use both with translation rules, σ_uw primary), settled at the Ch 1 framing level rather than left for Ch 9 to decide.

**What §7 should do under the new framing:**

- Drop the "three options to commit to" presentation.
- Cite the Ch 1 §4 settlement and the σ_uw / s transform as given.
- Narrow the remaining open question to: **does the §4 σ → 1 principal-axis suppression mechanism — which is the load-bearing piece for the lepton-like sheet's character — survive when results are translated to lattice-shear form for study-correspondence?** This is the substantive question that work-ch9 §4.4 already raises; it should be §7's central content rather than the parametrization-commitment framing.

The mechanism is in View A by construction (the (1−σ²)⁻¹ factor is what produces the suppression). Translating numerical predictions to s for empirical correspondence is mechanical (use the transform), but verifying that the predicted sheet character is preserved across the translation at large σ (where second-order terms dominate the transform) is the open quantitative question.

§7's restructured payload: confirm the parametrization is settled at Ch 1, then carry the σ → 1 mechanism analysis through to the empirical-translation step, with attention to the second-order divergence between σ_uw and s.

## Issue 2: Naming note is slightly misleading

The opening "Naming note" says the file uses View A/View B labels that map to Ch 1's σ / s. In practice the file already uses bare σ in the math throughout §§2–6, and "View A vs View B" is the language only in §7. A reader looking for σ_m or σ_L per the naming note's wording will not find them; what they will find is σ used as the working symbol and "View A/B" only when contrasting parametrizations.

Minor fix: rewrite the naming note to say "this file already uses σ as the working symbol consistent with Ch 1 §4. Where §7 contrasts parametrizations using 'View A vs View B' language, those map to Ch 1's σ_uw and s respectively." Removes the σ_m / σ_L reference that doesn't match the file's actual content.

## Issue 3: Cross-reference to work-m8a §4.4

§3.2(d) and §4 both reference the σ → 1 suppression as the framework's main candidate resolution to the single-axis dominance puzzle. §4.4 caveats that the mechanism is View-A-specific. §6.1 ("Lepton-like sheet") says the architectural question of §3 is resolved by mechanism (d) "if View A is the framework's parametrization (§7)." Now that §7's settlement is upstream rather than pending, §6.1's qualifier becomes "given Ch 1's parametrization commitment" rather than "if §7 decides View A." Small framing update.

---

## Verdict

The split is structurally sound. work-ch9's content (combined parameter landscape, three regimes, three sheet types, σ → 1 suppression) is properly Ch 9's territory and does not overlap with work-m8a's Ch 8 scope.

The Issue 1 §7 restructuring is the only substantive change needed. Issues 2 and 3 are small cleanups that ride along.

After those updates, work-ch9 is ready to feed the eventual Ch 9 writing.
