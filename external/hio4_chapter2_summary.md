# Handbook of IO Vol 4 Chapter 2: Summary

**Title:** Empirical Models of Demand and Supply in Differentiated Products Industries
**Authors:** Amit Gandhi & Aviv Nevo (NBER Working Paper 29257, Sept 2021)
**Total Pages:** 96 (4 chunks of 25 pages each)

---

## Overview

This chapter provides a comprehensive review of empirical methods for modeling demand and supply in differentiated products industries. It is foundational material for modern empirical IO and underpins much of the research in competition policy, mergers, and market power analysis.

---

## Chapter Structure & Page Ranges

| Section | Topic | Pages | Chunk |
|---------|-------|-------|-------|
| 1 | Introduction | 3-4 | 1 |
| 2 | A Motivating Example (Bresnahan 1987) | 5-12 | 1 |
| 3 | Demand | 12-24 | 1 |
| 4 | Demand Estimation | 25-48 | 2 |
| 5 | Supply | 49-66 | 2-3 |
| 6 | Extensions of the Demand Model | 67-82 | 3-4 |
| 7 | Concluding Comments | 82 | 4 |
| References | | 83-96 | 4 |

---

## Key Concepts by Section

### Section 2: Motivating Example (Bresnahan 1987)
- **Key idea:** Use demand estimates + pricing model to recover unobserved marginal costs and markups
- **Application:** U.S. automobile industry 1954-1956, testing for collusion vs. competition
- **Ownership matrix H:** Defines which products are jointly priced (0/1 values)
- **Pricing equation:** p = mc + Ω⁻¹q(p) where Ω captures demand derivatives

### Section 3: Demand Models

#### 3.1 Background & Challenges
- Dimensionality problem: J² parameters with J products
- Need for product differentiation in modeling
- Solution: Characteristics-based models (Gorman 1956, Lancaster 1966, Rosen 1974)

#### 3.2 Discrete Choice Demand Models
- **Random utility:** uᵢⱼₜ = xⱼₜβᵢ + αᵢpⱼₜ + ξⱼₜ + εᵢⱼₜ
- **Mean utility:** δⱼₜ = xⱼₜβ₀ + α₀pⱼₜ + ξⱼₜ (product-specific, common across consumers)
- **ξⱼₜ:** Unobserved product characteristics (brand equity, demand shocks) - KEY for estimation
- **εᵢⱼₜ:** Idiosyncratic taste shock (usually Type-1 extreme value → Logit)

#### Logit Model
- Simple: share = exp(δⱼₜ) / Σexp(δₖₜ)
- Problem: IIA property, proportional substitution
- Cross-price elasticities depend only on shares, not characteristics proximity

#### Mixed Logit (Random Coefficients)
- Allows heterogeneous preferences: βᵢ = β₀ + βᵈDᵢₜ + βᵛνᵢ
- Flexible substitution patterns driven by characteristics
- Market shares: integration over distribution of heterogeneity

#### Consumer Welfare
- Inclusive value: ωᵢₐₜ = ln[Σⱼ∈A exp(δⱼₜ + μᵢⱼₜ)]
- Converts to monetary equivalent by dividing by price coefficient

### Section 4: Demand Estimation

#### 4.1-4.2 Identification
- Key moment condition: E[ξⱼₜ | Zₜ] = 0
- Need IVs because price correlated with ξ
- Cross-sectional variation in product characteristics identifies heterogeneity parameters

#### 4.3 GMM Estimation (BLP Algorithm)
1. For given (Γ, Σ), compute predicted shares via simulation
2. Invert shares to recover δ using contraction mapping: δʳ⁺¹ = δʳ + ln(s) - ln(σ̃)
3. Compute ξ = δ - xβ - αp, form GMM objective with IVs

#### Instrumental Variables
- **BLP IVs:** Own characteristics, sum of competitor characteristics, sum of own-firm other products
- **Differentiation IVs (Gandhi-Houde):** Distance measures in characteristics space
- **Hausman IVs:** Prices in other markets (common cost shocks)
- **Waldfogel IVs:** Demographics in other markets

#### 4.4 Extensions
- Handling zero market shares (Gandhi et al. 2021)
- Non-parametric/flexible estimation (Compiani 2019)
- ABLP algorithm (Lee & Seo 2015)

### Section 5: Supply Models

#### 5.1 Workhorse Model (Nash-Bertrand)
- **Pricing equation:** p = mc + Ω⁻¹q(p)
- **Key application:** BLP (1995) automobile demand
- Use to recover marginal costs: mc = p - Ω⁻¹q

#### 5.2 Testing Models of Competition
- **Nevo (2001):** Cereal industry - "high" margins explained by differentiation, not collusion
- **Miller & Weinberg (2017):** Beer industry, Miller-Coors JV - estimate conduct parameter κ
- **Merger simulation:** Change ownership matrix H, compute new equilibrium prices

#### 5.3 Adding Retailers
- **Villas-Boas (2007):** Two-level pricing (manufacturer → retailer → consumer)
- Double marginalization, vertical contracts, resale price maintenance

#### 5.4 Bargaining Models
- **Nash-in-Nash bargaining:** Horn & Wolinsky (1988)
- **Application:** Crawford & Yurukoglu (2012) cable TV bundling
- **Hospital-insurer bargaining:** Gowrisankaran, Nevo, Town (2015)
- Bargaining power parameter ζ, leverage affects outcomes

### Section 6: Extensions

#### 6.1 Static Extensions
- **Multiple goods:** Gentzkow (2007), Hendel (1999), Fan (2013)
- **General characteristics models:** Dubois et al. (2014) - food demand

#### 6.2 Dynamic Demand
- **Storable goods (Hendel & Nevo 2006):**
  - Inventory model with (S,s) policy
  - Short-run vs. long-run elasticities differ significantly
  - Static models overestimate own-price effects ~30%, underestimate cross-price effects 5x

- **Durable goods (Gowrisankaran & Rysman 2012):**
  - Forward-looking consumers consider future prices/quality
  - Utility from outside option changes after purchase
  - Uses dynamic inclusive value to reduce state space

---

## Key Equations Reference

1. **Pricing FOC:** q(p) - Ω(p - mc) = 0
2. **Mean utility:** δⱼₜ = xⱼₜβ₀ + α₀pⱼₜ + ξⱼₜ
3. **Logit share:** sⱼₜ = exp(δⱼₜ) / [1 + Σₖexp(δₖₜ)]
4. **Mixed Logit share:** sⱼₜ = ∫ [exp(δⱼₜ + μᵢⱼₜ) / (1 + Σₖexp(δₖₜ + μᵢₖₜ))] dF(Dᵢ,νᵢ)
5. **BLP contraction:** δʳ⁺¹ = δʳ + ln(s) - ln(σ̃(δʳ))
6. **Marginal cost recovery:** mc = p - Ω⁻¹q(p)

---

## Important Papers Referenced

- **Berry (1994):** Introduced discrete choice demand estimation with aggregate data
- **Berry, Levinsohn & Pakes (1995):** BLP - random coefficients demand with supply
- **Nevo (2000b):** Practitioner's guide to BLP estimation
- **Nevo (2001):** Cereal market power analysis
- **Gandhi & Houde (2020):** Differentiation instruments
- **Conlon & Gortmaker (2020):** Best practices for BLP estimation (pyblp)

---

## Relevance to Course

This chapter is the primary reference for:
- Demand estimation lectures (discrete choice, BLP)
- Supply-side analysis (pricing, markups, margins)
- Merger simulation
- Empirical methods in IO

The PhD demand slides mainly rely on this chapter per CLAUDE.md.
