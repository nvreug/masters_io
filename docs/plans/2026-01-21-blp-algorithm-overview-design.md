# BLP Algorithm Overview for Lecture 3

## Purpose
Add a brief (2-slide) conceptual overview of the BLP estimation algorithm to lecture 3, positioned after the demographic model recap and before the Nevo (2001) example.

## Location in Lecture
After "Recap: The demographic model", before "Classic example: Nevo (2001)"

## Slide Design

### Slide 1: "The BLP estimation algorithm"

**Framing:** "We have the model, but how do we actually estimate it?"

**Content:**
- Step 1: Estimate π and δ via maximum likelihood
  - For each guess of π, invert to find δ values that match observed shares
  - MLE finds the π that best predicts consumer choices
- Step 2: Recover β and α via 2SLS
  - Use estimated mean utilities: δ_jt = x_jt β + α p_jt + ξ_jt
  - Instruments handle price endogeneity

**Key message:** "pyblp handles all of this for you"

### Slide 2: "The inversion step"

**Content:**
- Problem: Given a guess of π, how do we find the δ values?
- Solution: Berry's (1994) iterative contraction mapping
- Key equation: δ^{r+1}_{jt} = δ^r_{jt} + ln(s_{jt}) - ln(ŝ_{jt})
- Intuition: If predicted share too low, increase δ; if too high, decrease δ
- Berry (1994) proved this always converges to a unique solution

## Notation
Uses lecture 2's notation consistently:
- δ_jt: mean utility
- μ_ijt: individual deviation from demographics
- π: demographic interaction coefficients
- β, α: linear parameters in mean utility

## Implementation Notes
- Update all Plan slides to include new topic "The BLP algorithm"
- Add section header comment before new slides
- Compile and verify page count
