# ECN 594 Slide Outlines Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Create slide outlines for all 14 lectures of ECN 594: Advanced Topics in Competition Policy & Business Strategy

**Architecture:** Each lecture has two parts (60-75 min each, 20-30 slides per part). Part 1 (Lectures 1-7) covers Demand Estimation & Pricing. Part 2 (Lectures 8-14) covers Models of Competition & Industry Structure. Content draws from undergraduate IO slides (pricing, competition) and PhD IO slides (demand estimation), adapted to advanced undergraduate/masters level.

**Tech Stack:** LaTeX slides using format from `previous_courses/undergraduate_io/`

---

## Student Background (Important Context)

Students arrive with:
- **ECN 565 (Alvin Murphy):** Discrete choice econometrics (logit, probit, MLE)
- **ECN 532 (Hector Chade):** Game theory (Nash, Cournot, Bertrand, Stackelberg, repeated games, collusion)

**Implication:** Can do quick refreshers in IO notation; focus on applications rather than foundational theory.

---

## Part 1: Demand Estimation and Pricing (Lectures 1-7)

### Lecture 1 (Wed, Jan 21) - Introduction & Foundations

**Part 1: Introduction and Pricing** (Cabral Ch 3, 5)

Main topics:
- What is Industrial Organization?
  - Study of firm behavior, market structure, competition
  - Policy applications: antitrust, regulation
  - Business applications: pricing, platform design
- **Course structure: Theory + Empirical**
  - This course has both theoretical and empirical components
  - Empirical components (demand estimation) are mainly at PhD level
  - But they are so useful in practice that we will cover them here
  - Theory: pricing, oligopoly models, entry, mergers, vertical relationships
  - Empirical: demand estimation, merger simulation
- Why study IO? Real-world examples
  - Tech industry concentration (Google, Amazon, Apple)
  - Merger policy (recent cases)
  - Price discrimination in practice
- Review: Monopoly pricing
  - Profit maximization: MR = MC
  - Lerner index: L = (P - MC)/P = 1/|ε|
  - Deadweight loss from market power
- Monopoly regulation
  - Marginal cost pricing (and subsidy requirement)
  - Average cost pricing
  - Price caps
- Course roadmap and logistics

*Source:* Adapt from `previous_courses/undergraduate_io/slides/week_1/`
*Reference:* Cabral Ch 3 (basic economics), Ch 5 (monopoly)

---

**Part 2: Utility Models and Demand** (Train Ch 1-2; HIO Vol 4 Ch 2 Section 3)

Main topics:
- Why do we need demand models in IO?
  - Measure substitution patterns
  - Compute price elasticities
  - Evaluate mergers and policy
- Random utility framework (refresher from ECN 565)
  - Consumer i chooses product j to maximize utility
  - uᵢⱼ = Vᵢⱼ + εᵢⱼ (deterministic + random)
  - Choice probability: P(choose j) = P(uᵢⱼ > uᵢₖ for all k)
- From individual choice to market demand
  - Aggregate shares from individual probabilities
  - Market-level data vs individual-level data
- The dimensionality problem
  - J products → J² own/cross elasticities
  - Solution: characteristics-based models
- Preview: Logit and beyond

*Source:* Adapt from `previous_courses/phd_io/demand_estimation/`
*Reference:* Train Ch 1-2 (intro), HIO Vol 4 Ch 2 Section 3

---

### Lecture 2 (Fri, Jan 23) - Estimating Demand I

**[HW1 Released]**

**Part 1: Logit Demand Model** (Train Ch 3; HIO Vol 4 Ch 2 Section 3.2)

Main topics:
- Logit model derivation
  - Assume εᵢⱼ ~ Type I Extreme Value (Gumbel)
  - Closed-form choice probability: sⱼ = exp(δⱼ) / Σₖexp(δₖ)
  - Mean utility: δⱼ = xⱼβ + αpⱼ + ξⱼ
- Logit market shares
  - Adding outside option (j=0)
  - Share equation: sⱼ = exp(δⱼ) / [1 + Σₖexp(δₖ)]
- Berry (1994) inversion
  - ln(sⱼ) - ln(s₀) = δⱼ = xⱼβ + αpⱼ + ξⱼ
  - Linear regression possible!
- Elasticities in logit
  - Own-price: ηⱼⱼ = αpⱼ(1 - sⱼ)
  - Cross-price: ηⱼₖ = -αpₖsₖ
- IIA problem
  - Proportional substitution regardless of characteristics
  - "Red bus / blue bus" example
  - Why this matters for policy (mergers, entry)

*Source:* Adapt from `previous_courses/phd_io/demand_estimation/`
*Reference:* Train Ch 3 (logit), HIO Vol 4 Ch 2 Section 3.2

---

**Part 2: Logit Estimation** (HIO Vol 4 Ch 2 Section 4)

Main topics:
- Estimation setup
  - Data: market shares, prices, product characteristics
  - Goal: estimate β (tastes) and α (price sensitivity)
- The endogeneity problem
  - ξⱼ = unobserved product quality (brand equity, demand shocks)
  - Firms observe ξⱼ when setting prices → E[pⱼξⱼ] ≠ 0
  - OLS on ln(sⱼ) - ln(s₀) = xⱼβ + αpⱼ + ξⱼ is biased
- Instrumental variables for price
  - Hausman IVs: prices in other markets (common cost shocks)
  - BLP IVs: characteristics of competing products
  - Cost shifters: input prices, exchange rates
- IV estimation in practice
  - 2SLS with Berry inversion
  - Interpretation of coefficients
- Hands-on example preview (Python/statsmodels)

*Source:* Adapt from `previous_courses/phd_io/demand_estimation/`
*Reference:* HIO Vol 4 Ch 2 Section 4

---

### Lecture 3 (Mon, Jan 26) - Estimating Demand II

**Part 1: Mixed Logit / Random Coefficients** (Train Ch 6; HIO Vol 4 Ch 2 Section 3.2)

Main topics:
- Why move beyond logit?
  - IIA is unrealistic for many markets
  - Need flexible substitution patterns
  - Policy relevance: merger effects depend on substitution
- Random coefficients intuition
  - βᵢ = β̄ + Σνᵢ where νᵢ ~ N(0, I)
  - Consumers differ in tastes for characteristics
  - Similar products are closer substitutes
- Mixed logit shares
  - sⱼ = ∫ [exp(δⱼ + μᵢⱼ) / (1 + Σₖexp(δₖ + μᵢₖ))] dF(νᵢ)
  - μᵢⱼ = xⱼΣνᵢ captures heterogeneity
  - No closed form → simulation required
- Flexible substitution patterns
  - Cross-elasticities now depend on characteristic similarity
  - Products with similar x are closer substitutes
- Nested logit as special case (brief)
  - Groups/nests with correlation parameter
  - Simpler than full random coefficients

*Source:* Adapt from `previous_courses/phd_io/demand_estimation/`
*Reference:* Train Ch 6 (mixed logit), HIO Vol 4 Ch 2 Section 3.2

---

**Part 2: BLP Estimation** (HIO Vol 4 Ch 2 Section 4.3)

Main topics:
- The BLP algorithm overview
  - Berry, Levinsohn, Pakes (1995) - automobile demand
  - Combines demand estimation with supply-side pricing
- BLP contraction mapping
  - For given (β, Σ), find δ that matches observed shares
  - δʳ⁺¹ = δʳ + ln(s) - ln(σ̃(δʳ))
  - Iterates until convergence
- GMM estimation
  - Moment condition: E[ξⱼ | Zⱼ] = 0
  - ξⱼ = δⱼ - xⱼβ - αpⱼ
  - Search over (β, Σ, α) to minimize GMM objective
- Practical considerations
  - Simulation draws for integration
  - Starting values matter
  - Computational cost
- pyblp package introduction
  - Modern implementation of BLP
  - We'll use this for HW1

*Source:* Adapt from `previous_courses/phd_io/demand_estimation/`
*Reference:* HIO Vol 4 Ch 2 Section 4.3, Conlon & Gortmaker (2020) pyblp

---

### Lecture 4 (Wed, Jan 28) - Demand Applications & Price Discrimination I

**Part 1: Demand Estimation Applications** (HIO Vol 4 Ch 2 Section 5)

Main topics:
- From demand to supply
  - Nash-Bertrand pricing: firms maximize profits given competitors' prices
  - First-order condition: qⱼ + Σₖ∈Fⱼ (pₖ - mcₖ)(∂qₖ/∂pⱼ) = 0
  - Matrix form: p = mc + Ω⁻¹q(p)
- Recovering marginal costs
  - mc = p - Ω⁻¹q(p)
  - Use estimated demand derivatives
  - Markups: p - mc
- Market power measurement
  - Lerner indices by product
  - Aggregate measures
  - Comparison across markets
- Merger simulation preview
  - Change ownership matrix → new equilibrium prices
  - Will cover in detail in Part 2 of course
- Case study: Nevo (2001) cereal market
  - High margins explained by differentiation, not collusion
  - Importance of demand estimation for policy

*Source:* Adapt from `previous_courses/phd_io/demand_estimation/`
*Reference:* HIO Vol 4 Ch 2 Section 5, Nevo (2001)

---

**Part 2: Price Discrimination I - Third Degree** (Cabral Ch 6)

Main topics:
- Types of price discrimination (overview)
  - First degree: perfect/personalized pricing
  - Second degree: screening/menus
  - Third degree: group pricing (by observable characteristics)
- Third-degree price discrimination
  - Identify groups with different elasticities
  - Charge different prices to each group
  - Examples: student discounts, geographic pricing, time-of-day
- Optimal pricing across markets
  - Inverse elasticity rule: (pᵢ - mc)/pᵢ = 1/|εᵢ|
  - Higher markup in less elastic market
  - Condition: MR₁ = MR₂ = MC
- Welfare effects
  - Producer surplus increases (definitionally)
  - Consumer surplus: some gain, some lose
  - Total welfare: ambiguous - depends on whether new markets served
- When is price discrimination possible?
  - Identification: can observe group membership
  - Arbitrage prevention: can't resell between groups
  - Market power: must have pricing power

*Source:* Adapt from `previous_courses/undergraduate_io/slides/` (price discrimination)
*Reference:* Cabral Ch 6

---

### Lecture 5 (Mon, Feb 2) - Price Discrimination II & III

**Part 1: Price Discrimination II - Two-Part Tariffs** (Cabral Ch 6)

Main topics:
- Two-part tariff structure
  - Fixed fee F + per-unit price p
  - Examples: club memberships, phone plans, amusement parks
- Optimal two-part tariff (homogeneous consumers)
  - Set p = MC to maximize surplus
  - Extract all surplus with F = consumer surplus at p = MC
  - Achieves first-degree outcome
- Heterogeneous consumers
  - If charge p = MC, F limited by lowest-value consumer
  - Trade-off: raise F (exclude some) vs lower F (serve all)
  - May be optimal to exclude low types
- Comparison with uniform pricing
  - Two-part tariff dominates uniform pricing for firm
  - Can extract more surplus while maintaining efficiency
- Real-world applications
  - Costco membership model
  - Software licensing
  - Gym memberships

*Source:* Adapt from `previous_courses/undergraduate_io/slides/` (price discrimination)
*Reference:* Cabral Ch 6

---

**Part 2: Price Discrimination III - Second Degree / Screening** (Cabral Ch 6)

Main topics:
- Second-degree price discrimination
  - Cannot observe consumer type directly
  - Design menu of options to induce self-selection
  - "Damaged goods" strategy
- Menu design problem
  - Two types: high-value (H) and low-value (L)
  - Offer different quality/quantity bundles
  - Incentive compatibility: each type prefers own bundle
  - Individual rationality: each type willing to participate
- Optimal screening
  - "No distortion at the top": H gets efficient quality
  - Distort L's quality downward to prevent H from mimicking
  - Extract rent from H, leave L at reservation utility
- Quantity discounts
  - Larger packages at lower per-unit price
  - Induces high-demand types to buy more
  - Example: bulk pricing at Costco
- Versioning and bundling
  - Software versions (Pro vs Basic)
  - Airline tickets (business vs economy)
  - Intentional quality degradation

*Source:* Adapt from `previous_courses/undergraduate_io/slides/` (price discrimination)
*Reference:* Cabral Ch 6

---

### Lecture 6 (Wed, Feb 4) - Review

**[HW1 Due]**

**Part 1: Review and Practice Questions - Demand Estimation**

Main topics:
- Logit model review
  - Derivation and key equations
  - Berry inversion
  - Elasticity formulas
  - IIA limitation
- Random coefficients / BLP review
  - Why heterogeneity matters
  - Estimation algorithm overview
  - Interpretation of results
- Supply side review
  - Nash-Bertrand pricing FOC
  - Marginal cost recovery
  - Markups and market power
- Practice problems
  - Elasticity calculations
  - Interpreting demand estimates
  - Policy application questions

*Source:* Create based on HW1 and lecture content
*Reference:* Review of HIO Vol 4 Ch 2

---

**Part 2: Review and Practice Questions - Pricing**

Main topics:
- Monopoly pricing review
  - MR = MC condition
  - Lerner index
  - Deadweight loss
- Price discrimination review
  - Three types and when each applies
  - Third degree: inverse elasticity rule
  - Two-part tariffs: F + p structure
  - Second degree: screening and IC/IR constraints
- Practice exam questions
  - Work through problems similar to undergrad midterms
  - Focus on problem-solving techniques
  - Common mistakes to avoid
- Q&A and clarifications

*Source:* Adapt practice questions from `previous_courses/undergraduate_io/exams/`
*Reference:* Cabral Ch 5, 6

---

### Lecture 7 (Mon, Feb 9) - Midterm

**Part 1: MIDTERM EXAM**
- 70 minutes
- Calculator + two-sided cheat sheet allowed
- Covers all Part 1 material (Lectures 1-6)

**Part 2: SKIP**

---

## Part 2: Models of Competition and Industry Structure (Lectures 8-14)

### Lecture 8 (Wed, Feb 11) - Oligopoly Competition

**Part 1: Cournot and Bertrand Competition** (Cabral Ch 8, 9)

Main topics:
- Oligopoly: between monopoly and perfect competition
- Cournot competition refresher (from ECN 532, IO notation)
  - Firms choose quantities simultaneously
  - Reaction functions: qᵢ = R(q₋ᵢ)
  - Nash equilibrium: mutual best responses
  - N-firm Cournot: q* = (a - c)/(N + 1), converges to competition as N → ∞
- Bertrand competition refresher
  - Firms choose prices simultaneously
  - Homogeneous goods: P = MC with just 2 firms!
  - Bertrand paradox: extreme result from homogeneity assumption
- Cournot vs Bertrand comparison
  - Which is "right"? Depends on context
  - Capacity constraints → Cournot-like outcomes
  - Quick adjustment → Bertrand-like outcomes
- Stackelberg (leader-follower) brief mention
  - Sequential quantity choice
  - First-mover advantage

*Source:* Adapt from `previous_courses/undergraduate_io/slides/` (oligopoly)
*Reference:* Cabral Ch 8 (Cournot), Ch 9 (Bertrand)

---

**Part 2: Hotelling Model and Differentiated Products** (Cabral Ch 12, 14)

Main topics:
- Why differentiation matters
  - Resolves Bertrand paradox
  - Real markets have differentiated products
  - Pricing power from differentiation
- Hotelling model setup
  - Consumers located uniformly on [0, 1] line
  - Two firms at locations a and b
  - Transport cost t per unit distance
  - Consumer utility: v - pⱼ - t|x - locⱼ|
- Hotelling equilibrium (fixed locations)
  - Find indifferent consumer
  - Derive demand for each firm
  - Profit maximization → equilibrium prices
  - p* = c + t (markup depends on differentiation t)
- Location choice
  - Minimum vs maximum differentiation
  - d'Aspremont et al. result with quadratic transport
- Connection to demand estimation
  - Hotelling = specific form of differentiated Bertrand
  - Characteristics space in BLP is generalization
  - Nash-Bertrand pricing: p = mc + Ω⁻¹q(p)
- Merger simulation introduction
  - Pre-merger: firms compete
  - Post-merger: internalize competition for merged products
  - Change ownership matrix H → new equilibrium
  - Preview for HW2

*Source:* Adapt from `previous_courses/undergraduate_io/slides/` (product differentiation)
*Reference:* Cabral Ch 12 (product differentiation), Ch 14 (Hotelling)

---

### Lecture 9 (Mon, Feb 16) - Entry and Market Structure

**Part 1: Entry and Market Structure I** (Cabral Ch 10, 12)

Main topics:
- What determines market structure?
  - Number of firms in equilibrium
  - Entry and exit dynamics
- Free entry condition
  - Enter if expected profit > entry cost F
  - Equilibrium: π(N*) ≥ F > π(N* + 1)
- Entry with Cournot competition
  - More firms → lower price, lower per-firm profit
  - Equilibrium number of firms
- Fixed costs and natural monopoly
  - High F relative to market size → few firms
  - Economies of scale
- Excess entry theorem
  - Free entry may produce "too many" firms
  - Business stealing effect
  - Social vs private incentives to enter

*Source:* Adapt from `previous_courses/undergraduate_io/slides/` (market structure)
*Reference:* Cabral Ch 10 (market structure), Ch 12

---

**Part 2: Entry and Market Structure II** (Cabral Ch 10, 15)

Main topics:
- Entry barriers
  - Structural barriers: economies of scale, capital requirements
  - Strategic barriers: incumbent behavior
- Entry deterrence
  - Limit pricing: price low to make entry unprofitable
  - Capacity commitment: invest in capacity to credibly threaten
  - When is deterrence profitable vs accommodation?
- Entry deterrence model
  - Incumbent chooses strategy (deter or accommodate)
  - Entrant observes and decides whether to enter
  - Subgame perfect equilibrium
- Predatory pricing
  - Price below cost to drive out rival
  - Requires "deep pockets" or signaling
  - Legal issues and antitrust
- Empirical evidence on entry
  - Bresnahan & Reiss approach
  - How many firms can a market support?

*Source:* Adapt from `previous_courses/undergraduate_io/slides/` (entry)
*Reference:* Cabral Ch 10, 15 (strategic behavior)

---

### Lecture 10 (Wed, Feb 18) - Horizontal Relationships

**[HW2 Released]**

**Part 1: Horizontal Relationships I - Mergers** (Cabral Ch 11)

Main topics:
- Horizontal mergers: competitors combining
- Merger effects in Cournot model
  - Merger paradox: often unprofitable without efficiencies
  - Non-merging firms benefit (free-rider problem)
  - Need significant cost savings to be profitable
- Merger effects with differentiation
  - Less intense competition → higher prices
  - Internalize substitution between merged products
  - Generally profitable with differentiation
- Merger simulation in detail
  - Use demand estimates (from Part 1)
  - Change ownership matrix H
  - Solve for new equilibrium prices
  - Compute price changes and welfare effects
- Consumer welfare effects
  - Unilateral effects: higher prices from reduced competition
  - Coordinated effects: easier collusion post-merger
- HW2 preview: merger simulation exercise

*Source:* Adapt from `previous_courses/undergraduate_io/slides/` (mergers)
*Reference:* Cabral Ch 11 (mergers)

---

**Part 2: Horizontal Relationships II - Merger Policy** (Cabral Ch 11)

Main topics:
- Antitrust and merger policy
  - US: DOJ/FTC review, Hart-Scott-Rodino Act
  - Horizontal Merger Guidelines
- Market definition
  - SSNIP test (5% price increase)
  - Relevant market boundaries
  - Geographic and product markets
- Concentration measures
  - HHI: Herfindahl-Hirschman Index = Σsᵢ²
  - Merger guidelines thresholds
  - Limitations of concentration measures
- Efficiency defense
  - Mergers may generate cost savings
  - Williamson trade-off: market power vs efficiency
  - When do efficiencies outweigh price increases?
- Recent merger cases
  - Tech industry mergers
  - Hospital mergers
  - Vertical merger concerns

*Source:* Adapt from `previous_courses/undergraduate_io/slides/` (mergers, antitrust)
*Reference:* Cabral Ch 11

---

### Lecture 11 (Mon, Feb 23) - Vertical Relationships

**Part 1: Vertical Relationships I** (Cabral Ch 13)

Main topics:
- Vertical relationships: upstream and downstream firms
- Double marginalization problem
  - Upstream monopolist + downstream monopolist
  - Two markups → price too high, quantity too low
  - Inefficient relative to vertical integration
- Solution: Vertical integration
  - Single firm controls both stages
  - Eliminates double marginalization
  - But: other considerations (specialization, incentives)
- Alternative solutions to double marginalization
  - Two-part tariff: wholesale at MC + fixed franchise fee
  - Quantity forcing: specify downstream quantity
  - Revenue sharing
- Resale Price Maintenance (RPM)
  - Manufacturer sets minimum retail price
  - Can solve free-riding problem
  - Controversial: antitrust treatment

*Source:* Adapt from `previous_courses/undergraduate_io/slides/` (vertical)
*Reference:* Cabral Ch 13

---

**Part 2: Vertical Relationships II** (Cabral Ch 13)

Main topics:
- Vertical restraints
  - Exclusive dealing: retailer sells only one brand
  - Exclusive territories: geographic restrictions
  - Tying and bundling
- Exclusive dealing effects
  - Can foreclose rivals from distribution
  - May have efficiency justifications
  - Antitrust analysis: rule of reason
- Inter-brand vs intra-brand competition
  - Inter-brand: competition between manufacturers
  - Intra-brand: competition among retailers of same brand
  - Vertical restraints often reduce intra-brand competition
- Free-rider problem
  - Retailer provides services (showroom, advice)
  - Consumers free-ride: get service at one store, buy at another
  - RPM and exclusive territories as solutions
- Vertical merger analysis
  - Different from horizontal: not direct competitors
  - Foreclosure concerns
  - Efficiency benefits

*Source:* Adapt from `previous_courses/undergraduate_io/slides/` (vertical)
*Reference:* Cabral Ch 13

---

### Lecture 12 (Wed, Feb 25) - Guest Lecture & Collusion

**Part 1: Guest Lecture (Matt Leisten?)**

- Topic TBD based on guest availability
- Likely: applied IO research, industry experience, or policy

---

**Part 2: Collusion** (Cabral Ch 8)

Main topics:
- Collusion: firms coordinating to raise prices
- Cartel formation
  - Joint profit maximization
  - Split monopoly profits
  - Incentive to cheat
- Repeated games framework (refresher from ECN 532)
  - Single-shot: Prisoner's dilemma, defect is dominant
  - Repeated: cooperation can be sustained
  - Grim trigger strategy
- Sustainability of collusion
  - Critical discount factor: δ* = (πᴰ - πᶜ)/(πᴰ - πᴺ)
  - πᶜ = collusion profit, πᴰ = deviation profit, πᴺ = Nash profit
  - Collusion sustainable if δ ≥ δ*
- Factors affecting collusion
  - Number of firms (fewer → easier)
  - Demand fluctuations
  - Price transparency
  - Frequency of interaction
  - Product homogeneity
- Detection and antitrust
  - Cartel detection methods
  - Leniency programs
  - Recent cases

*Source:* Adapt from `previous_courses/undergraduate_io/slides/` (collusion)
*Reference:* Cabral Ch 8

---

### Lecture 13 (Mon, Mar 2) - Review

**[HW2 Due]**

**Part 1: Review and Practice Questions - Competition Models**

Main topics:
- Cournot/Bertrand/Hotelling review
  - Key equations and intuition
  - When to use each model
- Entry and market structure review
  - Free entry condition
  - Entry deterrence
- Merger analysis review
  - Merger simulation steps
  - Welfare effects
  - Policy considerations
- Practice problems
  - Oligopoly equilibrium calculations
  - Entry problems
  - Merger analysis

*Source:* Create based on HW2 and lecture content
*Reference:* Cabral Ch 8-15

---

**Part 2: Review and Practice Questions - Vertical & Collusion**

Main topics:
- Vertical relationships review
  - Double marginalization
  - Vertical restraints
- Collusion review
  - Critical discount factor
  - Sustainability conditions
- Comprehensive review
  - Connect Part 1 (demand) to Part 2 (competition)
  - How demand estimation informs merger/policy analysis
- Practice exam questions
  - Full exam-style problems
  - Time management tips
- Q&A and final clarifications

*Source:* Adapt practice questions from `previous_courses/undergraduate_io/exams/`
*Reference:* Review all Cabral chapters

---

### Lecture 14 (Wed, Mar 4) - Final Exam

**FINAL EXAM**
- 70 minutes
- Calculator + two-sided cheat sheet allowed
- Cumulative (covers all course material)
- Format: same as midterm (short answer + longer problems)

---

## Textbook Reference Summary

| Topic | Required (Cabral) | Supplementary |
|-------|-------------------|---------------|
| Intro, Monopoly | Ch 3, 5 | - |
| Price Discrimination | Ch 6 | - |
| Demand Estimation | - | HIO Vol 4 Ch 2, Train |
| Cournot/Bertrand | Ch 8, 9 | - |
| Product Differentiation | Ch 12, 14 | - |
| Entry | Ch 10, 15 | - |
| Mergers | Ch 11 | HIO Vol 4 Ch 2 (merger sim) |
| Vertical | Ch 13 | - |
| Collusion | Ch 8 | - |

---

## Source Material Mapping

| Lecture | Source |
|---------|--------|
| 1-4 (Demand) | `previous_courses/phd_io/demand_estimation/` |
| 1, 4-6 (Pricing) | `previous_courses/undergraduate_io/slides/` (pricing, price disc) |
| 8-12 (Competition) | `previous_courses/undergraduate_io/slides/` (oligopoly, entry, mergers, vertical) |

---

## Homework Summary

| HW | Content | Due | Weight |
|----|---------|-----|--------|
| HW1 | Demand estimation (Python/pyblp): estimate logit, compute elasticities | Feb 4 (Lecture 6) | 20% |
| HW2 | Part 2 topics + merger simulation (demand given, compute post-merger equilibrium) | Mar 2 (Lecture 13) | 20% |

---

## Implementation Notes

1. Each Part = 60-75 minutes, 20-30 slides
2. Use LaTeX format from `previous_courses/undergraduate_io/`
3. Reference Cabral chapter numbers for student reading
4. For demand estimation: adapt PhD content to masters level (less math rigor, more intuition)
5. Quick refreshers OK for game theory topics (students know from ECN 532)

## Pedagogical Style (CRITICAL)

**Match tone and format from previous slides in `previous_courses/undergraduate_io/slides/`**

### Worked Examples (for select key topics, NOT everything)

For important concepts, include worked examples directly ON THE SLIDES:

1. **Concept explanation** - Introduce the concept clearly
2. **Worked example slide** - Pose a question/problem on a slide
3. **Students try** - Give students a few minutes to work on it (2-5 minutes)
4. **Solution slide** - Professor goes through the solution with students

**Important:** Both the question AND the solution must be on the slides. The professor walks through the solution - students don't just see the answer.

### Reveal-style Questions

- Pose a thought-provoking question on one slide
- Discuss with students / let them think
- Reveal the answer on the next slide (or after a pause)
- This keeps students engaged and tests understanding

### Example structure for a key topic:
```
Slide: Concept - Lerner Index definition
Slide: Worked Example - "A firm has elasticity -2 and MC = 5. What is the optimal price?"
       [Students work for 2-3 minutes]
Slide: Solution - Show derivation step by step, professor walks through (p = 10)
Slide: Discussion question - "What happens as demand becomes more elastic?"
Slide: Reveal - Price approaches marginal cost
```

This interactive pattern should appear for KEY topics in each lecture part - not every single concept.
