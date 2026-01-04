# Train: Discrete Choice Methods with Simulation - Summary

**Title:** Discrete Choice Methods with Simulation
**Author:** Kenneth Train (University of California, Berkeley)
**Total Pages:** 388 (16 chunks of 25 pages each)

---

## Overview

This textbook provides a comprehensive treatment of discrete choice models and simulation-based estimation methods. It covers theoretical foundations, practical estimation, and advanced topics including Bayesian procedures. The book is essential for understanding consumer choice modeling in empirical IO.

---

## Chapter Structure & Page Ranges

| Chapter | Topic | Pages | Chunk |
|---------|-------|-------|-------|
| 1 | Introduction | 1-14 | 1 |
| 2 | Properties of Discrete Choice Models | 15-37 | 1-2 |
| 3 | Logit | 38-75 | 2-3 |
| 4 | GEV (Nested Logit) | 76-100 | 3-4 |
| 5 | Probit | 101-125 | 4-5 |
| 6 | Mixed Logit | 126-160 | 5-6 |
| 7 | Variations on a Theme | 161-193 | 7-8 |
| 8 | Numerical Maximization | 194-227 | 8-9 |
| 9 | Drawing from Densities | 228-260 | 9-10 |
| 10 | Simulation-Assisted Estimation | 261-293 | 10-11 |
| 11 | Individual-Level Parameters | 294-319 | 12-13 |
| 12 | Bayesian Procedures | 320-356 | 13-15 |
| - | Bibliography | 357-388 | 15-16 |

---

## Key Concepts by Chapter

### Chapter 1: Introduction
- Decision-makers choose among discrete alternatives
- Utility maximization framework: person n chooses alternative i if Uni > Unj for all j ≠ i
- Utility decomposition: Unj = Vnj + εnj (representative + unobserved)
- Choice probability: Pni = Prob(Vni + εni > Vnj + εnj ∀j ≠ i)

### Chapter 2: Properties of Discrete Choice Models
- **Key axioms:** Independence from irrelevant alternatives (in some models)
- **Identification:** Only differences in utility matter; need normalization
- **Aggregation:** Market shares from integrating over population
- **Elasticities:** Own-price and cross-price elasticity formulas
- **Consumer surplus:** Expected maximum utility (logsum)

### Chapter 3: Logit
- **Assumption:** εnj iid Type I extreme value (Gumbel)
- **Choice probability:** Pni = exp(Vni) / Σj exp(Vnj)
- **IIA property:** Pni/Pnj = exp(Vni)/exp(Vnj) independent of other alternatives
- **Red bus/blue bus paradox:** IIA can be restrictive
- **Estimation:** Maximum likelihood with closed-form probabilities
- **Specification:** Linear-in-parameters utility, alternative-specific constants

### Chapter 4: GEV (Nested Logit)
- **Generalized Extreme Value (GEV) family:** Relaxes IIA within nests
- **Nested structure:** Alternatives grouped into nests with correlated errors
- **Utility:** Unj = Vnj + εnj where εnj has GEV distribution
- **Two-level formula:** Pni = Pn(nest) × Pn(i|nest)
- **Inclusive value (logsum):** IVnk = ln[Σj∈Bk exp(Vnj/λk)]
- **Nesting parameter λ:** 0 < λ ≤ 1 for utility maximization; λ = 1 → logit
- **Cross-nested logit:** Alternatives can belong to multiple nests

### Chapter 5: Probit
- **Assumption:** ε ~ MVN(0, Σ) multivariate normal
- **Flexibility:** Any covariance pattern among alternatives
- **Identification issues:**
  - Level: Can only identify differences in means
  - Scale: Need to normalize one variance (e.g., first alternative = 1)
  - Only (J-1)(J-1+1)/2 - 1 free parameters in Σ for J alternatives
- **Substitution patterns:** Covariance determines substitution
- **Panel data:** Random effects probit for repeated choices
- **GHK simulator:** Sequential conditioning for probability simulation
  - Truncated normal draws using inverse CDF
  - Reduces J-dimensional integral to product of univariate truncated normals
  - Unbiased, smooth in parameters

### Chapter 6: Mixed Logit
- **Key innovation:** Random coefficients that vary across decision-makers
- **Utility:** Unj = β'n × xnj + εnj where βn ~ f(β|θ)
- **Choice probability:** Pni = ∫ Lni(β) f(β|θ) dβ (integral of logit over β distribution)
- **No IIA:** Substitution patterns determined by which alternatives share similar characteristics
- **Specifications:**
  - Random coefficients: βn = b + Σ^(1/2) νn where νn ~ N(0,I)
  - Error components: Additional error terms correlated across alternatives
- **Distributions:** Normal, lognormal, triangular, uniform
- **Panel data:** Same βn across choice situations for each person
- **Simulation:** Take R draws of β, compute logit for each, average

### Chapter 7: Variations on a Theme
- **Stated preference (SP) data:** Hypothetical choices in designed experiments
- **Revealed preference (RP) data:** Actual observed choices
- **Combining SP and RP:**
  - Different scale parameters for each
  - Same taste parameters, different variances
- **Ranked data:** Rank-ordered logit (exploded logit)
  - Probability = product of conditional logit probabilities
- **Ordered responses:** Ordered logit/probit for ordinal data
  - Latent variable crosses thresholds
- **Contingent valuation:** Willingness-to-pay estimation

### Chapter 8: Numerical Maximization
- **First-order conditions:** Score = gradient of log-likelihood = 0
- **Newton-Raphson:** θ(t+1) = θ(t) - H^(-1) × g
- **BHHH algorithm:** Approximates Hessian with outer product of scores
  - H ≈ Σn (sn × sn')
- **BFGS/DFP:** Quasi-Newton methods that update Hessian approximation
- **Line search:** Find step size λ in direction of improvement
- **Convergence criteria:** Gradient close to zero, improvement in LL small
- **Starting values:** Important for avoiding local maxima

### Chapter 9: Drawing from Densities
- **Pseudorandom draws:** Standard computer-generated "random" numbers
- **Inverse CDF method:** For any distribution F, draw u ~ Uniform(0,1), return F^(-1)(u)
- **Accept-reject method:** For complex densities
- **Normal draws:** Box-Muller transformation
- **Truncated normals:** Inverse CDF on truncated range
- **Importance sampling:** Draw from proposal g, weight by f/g
- **Halton sequences:** Low-discrepancy sequences for variance reduction
  - More evenly distributed than pseudorandom
  - Prime base determines sequence
  - Can reduce needed draws by factor of 5-10
- **Antithetics:** Use both ε and -ε to reduce variance
- **Gibbs sampling:** Draw each parameter conditional on others
- **Metropolis-Hastings:** Accept/reject algorithm for any distribution

### Chapter 10: Simulation-Assisted Estimation
- **Maximum Simulated Likelihood (MSL):**
  - Simulate choice probability Ř = (1/R) Σr L(β^r)
  - Maximize Σn ln(Řn)
  - Properties depend on how R grows with N:
    - R fixed: Inconsistent
    - R rises slower than √N: Consistent but not asymptotically normal
    - R rises faster than √N: Equivalent to ML
- **Method of Simulated Moments (MSM):**
  - Consistent and asymptotically normal for fixed R
  - Less efficient than ML
- **Method of Simulated Scores (MSS):**
  - Use unbiased score simulators
  - Consistent and asymptotically normal for fixed R
  - Efficient if R rises at any rate with N
- **Bias from simulation:** Log of average ≠ average of logs

### Chapter 11: Individual-Level Parameters
- **Goal:** Infer individual βn from their observed choices
- **Conditional distribution:** h(β|yn,xn,θ) = L(yn|xn,β) × g(β|θ) / P(yn|xn,θ)
  - Posterior on β given person's choices
- **Conditional mean:** β̄n = E[β|yn] is weighted average
  - Weight = probability of observed choices given that β
- **Simulation:**
  1. Draw β^r from population distribution g(β|θ)
  2. Calculate weight w^r ∝ L(yn|xn,β^r)
  3. β̄n = Σr w^r × β^r
- **Applications:**
  - Targeted marketing
  - Predicting future choices
  - Clustering/segmentation
- **As T→∞:** β̄n converges to true βn (Bernstein-von Mises)

### Chapter 12: Bayesian Procedures
- **Prior and posterior:**
  - Prior k(θ): beliefs before seeing data
  - Posterior K(θ|Y) ∝ L(Y|θ) × k(θ)
- **Bernstein-von Mises theorem:**
  - Posterior mean asymptotically equivalent to MLE
  - θ̄ ~a N(θ*, (-H)^(-1)/N) same as θ̂ML
- **Hierarchical Bayes for mixed logit:**
  - Individual level: βn ~ N(b, W)
  - Population level: priors on b and W
- **Gibbs sampling layers:**
  1. Draw b | W, βn∀n from N(β̄, W/N)
  2. Draw W | b, βn∀n from Inverted Wishart
  3. Draw βn | b, W using Metropolis-Hastings
- **Advantages over classical:**
  - No maximization required
  - Consistent with fixed R draws
  - Handles lognormals more easily
- **Disadvantages:**
  - Convergence of MCMC hard to assess
  - Slower for bounded distributions (triangular, uniform)

---

## Key Equations Reference

1. **Logit probability:** Pni = exp(Vni) / Σj exp(Vnj)

2. **Nested logit:** Pni = [exp(Vni/λk) / Σj∈Bk exp(Vnj/λk)] × [IVk^λk / Σl IVl^λl]

3. **Mixed logit:** Pni = ∫ [exp(β'xni) / Σj exp(β'xnj)] f(β|θ) dβ

4. **Consumer surplus (logsum):** CS = (1/α) × ln[Σj exp(Vnj)]

5. **GHK simulator:** P̃ = Π_j Φ[(η*j - Σk<j ljk ηk) / ljj]

6. **Simulated probability:** P̃ = (1/R) Σr L(β^r)

7. **Conditional mean:** β̄n = Σr w^r β^r where w^r ∝ L(yn|β^r)

8. **Bayes' rule:** K(θ|Y) ∝ L(Y|θ) k(θ)

---

## Important Technical Details

### Simulation Variance Reduction
- **Halton sequences:** Use prime bases, skip first ~10 draws
- **Antithetics:** Combine +ε and -ε draws
- **Common random numbers:** Use same draws across parameter values

### Identification in Probit
- Cannot identify: Level of utility, scale of each error
- Can identify: (J-1)(J-1+1)/2 - 1 covariance parameters
- Normalization: Set σ₁₁ = 1

### Panel Data
- Mixed logit: Same βn across all T choice situations
- Probability: Pn = ∫ [Πt Lnt(β)] f(β|θ) dβ
- More observations → tighter conditional distribution on βn

---

## Relevance to Course

This textbook is the primary reference for:
- Discrete choice theory and foundations
- Logit, nested logit, probit, and mixed logit models
- Simulation methods (GHK, Halton, Gibbs sampling)
- Demand estimation at the micro level
- Bayesian vs. classical estimation approaches

Key chapters for the master's course:
- **Chapters 3-6:** Core discrete choice models (Logit through Mixed Logit)
- **Chapter 8:** Numerical optimization methods
- **Chapter 10:** Simulation-based estimation (connects to BLP)
- **Chapter 12:** Bayesian procedures (for those interested in advanced methods)

The book provides the micro-foundations for BLP-style aggregate demand estimation covered in the Handbook of IO chapter.
