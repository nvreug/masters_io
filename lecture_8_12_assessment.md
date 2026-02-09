# Assessment: Lectures 8-12 (Part 2 of ECN 594)

## Slide Count vs Target (~40 per lecture)

| Lecture | Topic | Slides | vs Target |
|---------|-------|--------|-----------|
| L08 | Product Differentiation / Hotelling | **23** | **Severely under** |
| L09 | Entry and Market Structure | 44 | On target |
| L10 | Mergers and Merger Policy | **59** | **Significantly over** |
| L11 | Vertical Relationships | 44 | On target |
| L12 | Collusion | 44 | On target |
| L13 | Final Review | 49 | Slightly over (fine for review) |

---

## Major Structural Issues

### 1. L08 is missing Cournot (biggest problem)

The schedule says L8 Part 1 = **"Cournot 1"**, Part 2 = **"Hotelling 1"**. But the current L08 file **only covers Hotelling** (23 slides). It opens with "Last time we covered Cournot and Bertrand" -- but "last time" was the **midterm exam** (L7). There is no dedicated Cournot derivation anywhere in L08-L12.

**However**, looking at L06 (lecture_06.tex), the second half of that lecture already covers Cournot and Bertrand as a refresher: Cournot duopoly derivation, n-firm Cournot, Bertrand paradox, Kreps-Scheinkman, and when each model applies. So the L08 recap slide ("Last time we covered Cournot and Bertrand") is referring back to L06 content that was delivered before the midterm.

**The question is:** Is the L06 Cournot/Bertrand treatment sufficient for Part 2, or does L08 need its own deeper Cournot section? L06 covers:
- Cournot duopoly worked example (P = 100 - Q, MC = 10)
- N-firm Cournot formulas
- Bertrand paradox
- Kreps-Scheinkman
- When each model applies

This is a decent refresher but only ~12 slides. The schedule explicitly lists "Cournot 1" as L08 Part 1, suggesting more Cournot content was intended (e.g., Cournot Lerner index `L = s_i/|epsilon|`, asymmetric cost Cournot, Cournot comparative statics on N, connection to market concentration). Without this, key formulas used later (in L09 entry, L10 mergers, L12 collusion) appear without a proper derivation in Part 2.

### 2. L10 is overloaded at 59 slides

The mergers lecture tries to cover: differentiated Bertrand derivation, merger simulation (pre/post), ownership matrices, worked examples, UPP, HHI, market definition, SSNIP, efficiency defense, Williamson trade-off, remedies, and recent cases. This is realistically 3+ hours of material for ~2 hours of teaching time.

### 3. L12 exists in the file but the schedule shows it as blank

The schedule has L12 (Wed Feb 25) with empty topic fields. Yet the file contains a full collusion lecture. Need to decide: is collusion officially L12 content, or does it need to be slotted elsewhere?

### 4. No solutionbox formatting on any worked examples

The CLAUDE.md specifies `solutionbox` environment for all worked example solutions. None of L08-L12 use it -- solutions are in plain `wideitemize` frames.

---

## Lecture-by-Lecture Assessment

### L08: Product Differentiation & Hotelling (23 slides)

**Content quality:** Good Hotelling treatment. Nice TikZ diagram, clean derivation, good worked example (ice cream vendors), T/F questions, welfare discussion, and a useful Hotelling-to-logit comparison table.

**Plan topics (3):** Product differentiation, Hotelling model, Connection to demand estimation

**Issues:**
- Missing entire Cournot Part 1 (~15-20 slides needed) -- see discussion above about whether L06 coverage is sufficient
- The "preview: merger simulation" slide at the end feels premature -- this should come after the worked example, not as a final slide
- Plan slide only lists 3 topics (should be 6-8 per guidelines, though with Part 1 Cournot this would expand naturally)

### L09: Entry and Market Structure (44 slides)

**Content quality:** Strong. Good progression from free entry condition through Cournot entry example, structural vs strategic barriers, entry deterrence with game tree, capacity commitment, Fudenberg-Tirole taxonomy, and empirical entry models (Bresnahan & Reiss, Berry).

**Plan topics (6):** What determines market structure, Free entry condition, Entry with Cournot worked example, Entry barriers, Entry deterrence strategies, Sequential game analysis

**Issues:**
- The Fudenberg-Tirole taxonomy slide is dropped in without much setup -- students may not grasp the 2x2 without more explanation
- The entry deterrence worked example solution has a minor issue: "If K is large, incumbent produces q_I = K" -- this needs a brief explanation of why (because MC=0 up to K, so it's always optimal to produce up to capacity)
- Predatory pricing section is very brief (1 slide) -- could either be expanded or cut
- Good connection to merger analysis at the end

### L10: Mergers and Merger Policy (59 slides)

**Content quality:** Excellent and comprehensive. The differentiated Bertrand derivation, ownership matrix formulation, worked merger simulation, UPP, HHI, and policy material are all well done. The connection between Part 1 demand estimation and merger simulation is clearly drawn.

**Plan topics (6):** Horizontal mergers effects, Merger simulation, Worked example, Antitrust and merger review, Market definition and HHI, Efficiency defense

**Issues:**
- At 59 slides, this is ~50% over target. At 3 min/slide, that's ~3 hours of material for a 2.25-hour class
- **Suggestion:** Split this into two lectures. The natural break is after the merger simulation worked example (~slide 35): Part 1 = "Mergers: theory and simulation", Part 2 = "Merger policy: HHI, SSNIP, efficiencies"
- Or alternatively, cut some slides: the "recent merger cases" and "remedies" slides could become optional reading
- Two separate merger simulation worked examples (the first with `q = 100 - 2p + p_j` and the second with `q = 100 - 3p + p_k`) is redundant -- keep the better one

### L11: Vertical Relationships (44 slides)

**Content quality:** Good. Clean double marginalization derivation, good worked example, two-part tariff solution, vertical restraints overview, free-rider problem with diagram, and antitrust implications.

**Plan topics (6):** Vertical relationships, Double marginalization, Solutions (integration/two-part tariffs), Vertical restraints, Free-rider problem, Antitrust implications

**Issues:**
- The practice problem solution on slide 339-353 has what looks like a calculation error: "Retailer: q = (100-w) = 100-w" and "p = (100+w)/2" -- but with `q = 200 - 2p`, the inverse demand is `p = 100 - q/2`, so the retailer's MR calculation needs more care. Worth double-checking.
- The "successive oligopoly" section (1 slide) is very thin -- either develop it or cut it
- The Apple App Store case study is good and timely
- No worked example for vertical restraints (only T/F) -- could add one on exclusive dealing or RPM

### L12: Collusion (44 slides)

**Content quality:** Strong. Good refresher from ECN 532, clean N-firm derivation for both Cournot and Bertrand, detection/fines framework, leniency programs, and modern topics (algorithmic collusion).

**Plan topics (6):** Collusion refresher, Critical discount factor with N firms, Cournot vs Bertrand collusion, Detection and fines, Leniency programs, Antitrust enforcement

**Issues:**
- The Cournot collusion worked example has an internal inconsistency: the computed delta* = 0.571 doesn't match the formula result of 0.64. The slide acknowledges this as "rounding" but it's actually because the deviation profit calculation assumes a specific best response that doesn't match the formula's assumption. This should be cleaned up -- either use the formula consistently or do the full manual calculation correctly.
- The Cournot delta* table has a non-monotonic pattern (N=2: 0.53, N=3: 0.64, N=4: 0.61, N=10: 0.55) which is actually correct but will confuse students. Needs a slide or comment explaining the non-monotonicity.
- Algorithmic collusion (Assad et al. 2024) is a nice touch for a masters audience
- Hub-and-spoke arrangement is good but could use a concrete example (e.g., the e-books case)

---

## Cross-Cutting Issues

### Pedagogical Pattern
All lectures follow the good pattern: Concept -> Worked example -> Practice T/F -> Key points. This is consistent with the teaching style from L01-L06. However, compared to the guidelines, "reveal-style questions" (pose question, discuss, then reveal answer) are underused -- most engagement is through T/F blocks rather than standalone reveal questions.

### Assessment Integration
Strong overall. L10 explicitly connects to HW2 multiple times. L09 connects entry to merger review. L12 connects collusion to coordinated effects in mergers. The final review (L13) covers all topics with practice problems that mirror lecture examples.

### Topic Sequencing
The current sequence (Hotelling -> Entry -> Mergers -> Vertical -> Collusion) makes sense, but the missing/thin Cournot content is a gap since Cournot equilibrium is used repeatedly in L09 (entry with Cournot) and L12 (Cournot collusion). L06 partially fills this gap.

### Comparison to L01-L06 Style
- L01-L06 use single .tex files (same as L08-L12) -- consistent
- L01-L06 also don't use solutionbox for worked examples (so this is consistent, though CLAUDE.md says they should)
- Plan slides in L01-L06 have 4-8 topics (L08 only has 3, which is low)
- L01-L06 make heavier use of `\pause` for reveal-style content; L08-L12 use it less

---

## Summary of Recommended Actions (Priority Order)

1. **Resolve the Cournot gap in L08** -- Either add ~15-20 slides of Cournot content (Lerner index derivation `L = s_i/|epsilon|`, asymmetric costs, connection to concentration) or explicitly acknowledge L06 as sufficient and update the schedule
2. **Trim L10** from 59 to ~40 slides -- remove one of the two merger simulation worked examples, cut "recent cases" and "remedies" to optional, or redistribute content to fill L12's empty schedule slot
3. **Resolve L12 schedule** -- officially assign collusion there, or rethink the sequencing
4. **Fix the collusion worked example** discrepancy in L12 (0.571 vs 0.64)
5. **Double-check the L11 practice problem** calculation for the `q = 200 - 2p` case
6. **Add `solutionbox`** formatting to all worked example solution slides across L08-L12 (and L01-L06 for consistency)
7. **Add a comment on Cournot delta* non-monotonicity** in L12
