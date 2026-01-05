# ECN 594 Slide Outlines Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Create slide outlines for all 14 lectures of ECN 594: Advanced Topics in Competition Policy & Business Strategy

**Architecture:** Each lecture has two parts (60-75 min each, 20-30 slides per part). Part 1 (Lectures 1-7) covers Demand Estimation & Pricing. Part 2 (Lectures 8-14) covers Models of Competition & Industry Structure.

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
  - Policy applications (antitrust) + business applications (pricing, platforms)
- **Course structure: Theory + Empirical**
  - Empirical components (demand estimation) are PhD level but so useful we cover them
  - Theory: pricing, oligopoly, entry, mergers, vertical
- Why study IO? Brief real-world examples (tech concentration, merger policy)
- Review: Monopoly pricing
  - MR = MC, Lerner index: L = (P - MC)/P = 1/|ε|
  - Deadweight loss from market power
- Monopoly regulation
  - Marginal cost pricing (and subsidy requirement)
  - Average cost pricing
  - Price caps
- Course roadmap and logistics

*Source:* Adapt from `previous_courses/undergraduate_io/slides/week_1/`
*Reference:* Cabral Ch 3, 5

---

**Part 2: Utility Models and Demand** (Train Ch 1-2; HIO Vol 4 Ch 2 Section 3)

Main topics:
- Why do we need demand models in IO?
  - Measure substitution, compute elasticities, evaluate policy
- **Ordinal vs cardinal utility**
  - Utility is typically ordinal: only rankings matter, not magnitudes
  - Problem: we want to measure consumer surplus in dollars!
  - Solution: quasi-linear utility makes utility cardinal
  - U = u(goods) + y (where y is income)
  - Take derivative: ∂U/∂y = 1 (marginal utility of income is constant)
  - This means we can measure utility in dollars
  - Consumer surplus has a meaningful interpretation
- Random utility framework (refresher)
  - uᵢⱼ = Vᵢⱼ + εᵢⱼ; Choice probability: P(uᵢⱼ > uᵢₖ for all k)
- **Why isn't income in the utility function?**
  - With quasi-linear utility: U = u(goods) + income
  - When comparing alternatives, income cancels out (only differences matter)
  - Price coefficient α captures marginal utility of income
  - This is why we can write uᵢⱼ = xⱼβ - αpⱼ + εᵢⱼ without income
  - Good intuition check for understanding the model
- From individual choice to market demand
  - Aggregate shares from individual probabilities
- The dimensionality problem
  - J products → J² elasticities; Solution: characteristics-based models

*Source:* Adapt from `previous_courses/phd_io/demand_estimation/`
*Reference:* Train Ch 1-2, HIO Vol 4 Ch 2 Section 3

---

### Lecture 2 (Fri, Jan 23) - Estimating Demand I

**[HW1 Released]**

**Part 1: Logit Demand Model** (Train Ch 3; HIO Vol 4 Ch 2 Section 3.2)

Main topics:
- Logit model derivation
  - εᵢⱼ ~ Type I Extreme Value → closed-form choice probabilities
  - Mean utility: δⱼ = xⱼβ + αpⱼ + ξⱼ
  - Share equation: sⱼ = exp(δⱼ) / [1 + Σₖexp(δₖ)]
- Adding outside option (j=0)
  - Why we need it: consumers can choose not to buy
- Berry (1994) inversion
  - ln(sⱼ) - ln(s₀) = δⱼ → can recover mean utilities from shares
  - This is the key insight that makes estimation tractable
- **Worked example: Elasticities in basic logit**
  - Own-price: ηⱼⱼ = αpⱼ(1 - sⱼ)
  - Cross-price: ηⱼₖ = -αpₖsₖ
  - *Given α = -0.5, p = 20, s = 0.1, compute own-price elasticity*
- IIA problem (preview only - full discussion in L4)
  - Logit implies proportional substitution
  - We'll return to this with the "red bus / blue bus" example later

*Source:* Adapt from `previous_courses/phd_io/demand_estimation/`
*Reference:* Train Ch 3, HIO Vol 4 Ch 2 Section 3.2

---

**Part 2: The Identification Problem & Instrumental Variables** (HIO Vol 4 Ch 2 Section 4)

> **IMPORTANT: This is conceptually the hardest lecture. Allocate extra slides and time. This is the first time students see price endogeneity in demand estimation.**

Main topics:

**1. The Classic Identification Problem (start here - 8-10 slides)**
- Setup: we observe equilibrium prices and quantities
- Problem: can't tell if demand shifted or supply shifted
- *Diagram: supply/demand with multiple equilibrium points*
  - If we just regress Q on P, what do we get? Neither demand nor supply!
- This is why "running a regression" isn't enough
- Key insight: we need variation that shifts ONE curve but not the other

**2. Direction of Bias (KEY - testable)**
- If high-quality (high ξ) products have high prices...
- OLS sees: high price, but demand still high (because of ξ)
- OLS concludes: price doesn't hurt demand much
- Result: α̂ biased toward zero (less negative than truth)
- *Worked example with numbers*

**3. Identification in Practice**
- To identify demand: need supply shifters (cost changes that don't affect demand directly)
- To identify supply: need demand shifters
- Examples:
  - Weather affects crop supply but not demand → identifies demand
  - Income changes affect demand but not supply → identifies supply

**4. The Gold Standard: Experiments** (engaging real-world example)
- Best solution: randomize prices!
- **Uber's price "wiggles"** (Cohen et al. 2016)
  - Uber experimentally varies surge multipliers up and down
  - Same time, same location → different riders see different prices
  - This randomization creates exogenous price variation
  - Key insight: demand conditions are identical, only price differs
  - *Diagram idea: two riders at same corner, one sees 1.2x, other sees 1.4x*
  - Result: demand elasticity ≈ -0.5 (inelastic!)
- Why this is powerful:
  - No confounding: price variation is independent of demand shocks
  - Clean identification of the demand curve
  - Uber paper: [NBER Working Paper 22627](https://www.nber.org/papers/w22627)
- Why this matters for us:
  - Tech companies can run experiments → clean identification
  - Traditional industries can't randomize prices → need IVs
  - Most IO settings require instrumental variables (next section)

**5. Instrumental Variables as the Solution**
- Need: correlated with price, uncorrelated with ξ
- Hausman IVs: prices in other markets (common cost shocks)
- BLP IVs: characteristics of competing products
- Cost shifters: input prices, exchange rates
- **Worked example: IV intuition**
  - Why do competitor characteristics work?
  - More competitors nearby → more competition → lower price (relevance ✓)
  - But competitor characteristics don't affect YOUR unobserved quality (exclusion ✓)

*Source:* Adapt from `previous_courses/phd_io/demand_estimation/`
*Reference:* HIO Vol 4 Ch 2 Section 4

**Slide allocation note:** Budget 24-28 slides. The identification problem sections (1-2) are foundational—don't skip. Discrete choice connection moved to L3.

---

### Lecture 3 (Mon, Jan 26) - Demand Model & pyblp Estimation

**Part 1: Demand Model with Demographic Interactions** (HIO Vol 4 Ch 2 Section 3)

Main topics:
- **Recap: Endogeneity in discrete choice** (bridge from L2)
  - Our model: uᵢⱼ = xⱼβ + αpⱼ + ξⱼ + εᵢⱼ
  - Berry inversion: ln(sⱼ) - ln(s₀) = δⱼ
  - ξⱼ = unobserved product quality (brand equity, advertising, design)
  - Problem: firms OBSERVE ξⱼ when setting prices → E[pⱼξⱼ] > 0
  - This is why we need IVs (covered in L2)
  - Now: extend the model to allow heterogeneous preferences
- **Extending the model: heterogeneous preferences**
  - Basic logit: everyone has same β (homogeneous preferences)
  - Problem: doesn't capture that different consumers value characteristics differently
  - Solution: let preferences vary with observed demographics
- **The demographic interaction model:**
  - uᵢⱼ = xⱼβ + (Dᵢ × xⱼ)γ + αpⱼ + ξⱼ + εᵢⱼ
  - Dᵢ = observed consumer demographics (income, age, family size, etc.)
  - (Dᵢ × xⱼ) = interactions: e.g., high-income consumers value horsepower more
  - This creates heterogeneous preferences WITHOUT random coefficients
- **Examples of demographic interactions:**
  - Income × price: wealthy consumers less price-sensitive
  - Family size × car size: families prefer larger vehicles
  - Age × fuel efficiency: older consumers may care more about MPG
- **Why not random coefficients?**
  - Full mixed logit adds νᵢ ~ N(0,Σ) terms (unobserved heterogeneity)
  - Computationally harder, requires simulation
  - Demographic interactions capture a lot of the variation more simply
  - Mention: **mixed logit** is the full version, beyond our scope
- **Preview: demographics and IIA** (full discussion next lecture)
  - Recall: logit has IIA problem (proportional substitution)
  - Demographics partially solve this - different consumer types substitute differently
  - We'll work through the "red bus / blue bus" example in L4

*Source:* Adapt from `previous_courses/phd_io/demand_estimation/`
*Reference:* HIO Vol 4 Ch 2 Section 3, Train Ch 3

---

**Part 2: pyblp Estimation** (HIO Vol 4 Ch 2 Section 4)

> **IMPORTANT: This is critical for HW1 success. Don't rush it. All pyblp content is here.**

Main topics:
- **pyblp for demand estimation**
  - Modern, reliable package (Conlon & Gortmaker 2020)
  - Handles IV estimation, standard errors, post-estimation
  - Why use a package? Correct standard errors, tested code
- **Worked Example: pyblp car data** — allocate 20+ slides
  - Walk through pyblp step by step, slowly
  - Step 1: Data setup (products, markets, shares, characteristics)
    - What does the data look like? Show actual data
  - Step 2: Formulation (which variables, which IVs, demographic interactions)
    - How to specify xⱼβ + (Dᵢ × xⱼ)γ in pyblp
  - Step 3: Problem definition
  - Step 4: Solve
  - Step 5: Extract results (coefficients, standard errors)
  - Show actual Python code on slides
- **Interpreting output**
  - What do the coefficients mean?
  - Are they statistically significant?
  - Does the sign on α make sense?
  - How to interpret demographic interaction coefficients
- **Post-estimation: elasticities and markups**
  - pyblp computes elasticities automatically
  - Own-price and cross-price elasticities
  - Recovering markups from Lerner index
- **This prepares students for HW1** — if unclear here, HW1 will be painful

*Source:* Adapt from `previous_courses/phd_io/demand_estimation/`, pyblp docs
*Reference:* HIO Vol 4 Ch 2 Section 4, Conlon & Gortmaker (2020)

**Slide allocation note:** Budget 25-30 slides for this part. The pyblp walkthrough needs to be thorough enough that students can replicate it.

---

### Lecture 4 (Wed, Jan 28) - Demand Applications & Price Discrimination I

**Part 1: Consumer Surplus, IIA, and Applications** (HIO Vol 4 Ch 2 Section 5)

Main topics:
- **Consumer surplus: the log-sum formula**
  - Expected utility for consumer i: E[max uᵢⱼ] = ln[Σⱼ exp(δⱼ + μᵢⱼ)] + constant
  - Consumer surplus (in dollars): CSᵢ = (1/αᵢ) × ln[Σⱼ exp(δⱼ + μᵢⱼ)]
  - Aggregate CS: integrate over consumer types
  - **Worked example:** Compute CS change from removing a product
- **The IIA problem: Red Bus / Blue Bus (new goods focus)**
  - Setup: Consumers choose how to commute. Choices: Car, Red Bus
  - Assume: half choose Car, half choose Red Bus → δ_car = δ_redbus = 0
  - Now INTRODUCE a Blue Bus (but consumers are color-blind!)
  - Blue Bus is identical to Red Bus in every way
  - Reality: welfare should NOT change (it's the same bus, just different color)
  - **What does logit predict?**
    - Pre: Inclusive value = ln(e⁰ + e⁰) = ln(2)
    - Post: δ_bluebus = δ_redbus = 0, so IV = ln(e⁰ + e⁰ + e⁰) = ln(3)
    - Logit says welfare INCREASED! But nothing real changed.
  - **The problem:** logit gives an extra "lottery ticket" for each product
  - This is IIA: model doesn't know buses are close substitutes
  - Why it matters: valuing new products, merger analysis
- **How demographics help (partial solution)**
  - With demographics: different consumer types have different substitution patterns
  - Bus riders vs car commuters substitute differently
  - Aggregate substitution is richer, but IIA still holds within groups
  - Mixed logit fully relaxes IIA (beyond our scope)
- **Why demand estimation is key (not supply)**
  - Demand gives us elasticities, substitution, welfare - the hard part
  - Costs can often be backed out from pricing behavior (we'll see this in Part 2)
  - Estimating cost functions directly needs detailed cost data
  - Supply-side estimation outside scope of this course
- **From demand to supply: monopolist pricing FOC**
  - FOC: q + (p - mc)(∂q/∂p) = 0 → Lerner index
  - **Note:** Multi-firm pricing and merger simulation comes later (Part 2)
- **Recovering marginal costs**
  - If you work within a firm: you can just observe MC directly from cost data
  - If you're an outsider (e.g., regulator, academic): harder - need to back out from demand + pricing FOC
  - We won't cover the outsider case here, but the idea: mc = p - markup
- **What do markups tell us about market power?**
  - High markup = high market power (low elasticity)
  - Compare markups across products, markets

*Source:* Adapt from `previous_courses/phd_io/demand_estimation/`
*Reference:* HIO Vol 4 Ch 2 Section 5, Train Ch 3

---

**Part 2: Price Discrimination I - Selection by Indicators** (Cabral Ch 6)

Main topics:
- Types of price discrimination (Cabral terminology)
  - Perfect price discrimination
  - Selection by indicators (group pricing)
  - Self-selection (menu design)
- Selection by indicators
  - Divide buyers into groups by observable characteristics
  - Examples: student discounts, geographic pricing
- **Worked example: Optimal pricing across markets**
  - Inverse elasticity rule: (pᵢ - mc)/pᵢ = 1/|εᵢ|
  - *Two markets with ε₁ = -2, ε₂ = -4, MC = 6. Find optimal prices.*
- Welfare effects (brief)
  - PS increases; CS ambiguous; Total welfare depends on new markets served

*Source:* Adapt from `previous_courses/undergraduate_io/slides/`
*Reference:* Cabral Ch 6

---

### Lecture 5 (Mon, Feb 2) - Price Discrimination II & III

**Part 1: Price Discrimination II - Two-Part Tariffs** (Cabral Ch 6)

Main topics:
- Two-part tariff structure: Fixed fee F + per-unit price p
  - Examples: club memberships, phone plans
- **Worked example: Optimal two-part tariff (homogeneous consumers)**
  - Set p = MC; Extract all surplus with F = CS at p = MC
- Heterogeneous consumers (brief)
  - Trade-off: raise F (exclude some) vs lower F (serve all)
- Comparison with uniform pricing
  - Two-part tariff extracts more surplus

*Source:* Adapt from `previous_courses/undergraduate_io/slides/`
*Reference:* Cabral Ch 6

---

**Part 2: Price Discrimination III - Self-Selection** (Cabral Ch 6)

Main topics:
- Self-selection: cannot observe type directly
  - Design menu to induce consumers to reveal type
- **Worked example: Menu design problem**
  - Two types: H and L with different WTP for quality
  - Incentive compatibility + individual rationality constraints
  - "No distortion at the top": H gets efficient quality
  - Distort L's quality to prevent H from mimicking
- Versioning examples (brief)
  - Software versions, airline tickets, "damaged goods"

*Source:* Adapt from `previous_courses/undergraduate_io/slides/`
*Reference:* Cabral Ch 6

---

### Lecture 6 (Wed, Feb 4) - Review

**[HW1 Due]**

**Part 1: Review - Demand Estimation**

Main topics:
- Logit model review
  - Berry inversion, elasticity formulas
  - IIA limitation (and when logit is "good enough")
- Identification and IVs review
  - Why price is endogenous
  - What makes a good IV
- pyblp workflow review
  - Data → formulation → solve → interpret
- **Practice problems (exam-style)**
  - Elasticity calculations from logit
  - Interpreting demand estimates
  - Endogeneity and IV questions

*Focus:* Work through problems that will appear on midterm

---

**Part 2: Review - Pricing**

Main topics:
- Monopoly pricing review
  - MR = MC, Lerner index
- Price discrimination review
  - Selection by indicators: inverse elasticity rule
  - Two-part tariffs: F + p structure
  - Self-selection: IC/IR constraints
- **Practice problems (exam-style)**
  - Price discrimination problems
  - Two-part tariff optimization

*Focus:* Work through problems similar to undergrad midterms

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

**Cournot competition (from ECN 532 - quick refresher in IO notation)**
- Students derived Cournot equilibrium in Hector's class; here we use IO notation
- Firms choose quantities simultaneously
- Reaction functions: qᵢ = (a - c - Σⱼ≠ᵢqⱼ) / 2b
- N-firm symmetric equilibrium: q* = (a - c) / [b(N + 1)]
- **NEW IO application:** Market power measurement
  - Lerner index in Cournot: L = (P - MC)/P = sᵢ/|ε| where sᵢ = market share
  - This connects to demand estimation from Part 1!
- **Worked example: Cournot with market power calculation**
  - *P = 100 - Q, MC = 10. Find equilibrium quantities, price, and Lerner index.*

**Bertrand competition (from ECN 532 - quick refresher)**
- Students proved P = MC result; remind them of the logic
- Firms choose prices; Homogeneous goods: P = MC with 2+ firms
- Bertrand paradox: only 2 firms, but competitive outcome!

**NEW: Cournot vs Bertrand — when does each apply?**
- Capacity constraints → Cournot-like (firms commit to capacity first)
- Quick price adjustment → Bertrand-like
- Kreps-Scheinkman (1983): Capacity choice + price competition = Cournot outcome
- **IO insight:** Most empirical work uses differentiated Bertrand (next section)

*Source:* Adapt from `previous_courses/undergraduate_io/slides/`
*Reference:* Cabral Ch 8, 9

---

**Part 2: Hotelling Model** (Cabral Ch 12, 14)

Main topics:
- Why differentiation matters
  - Resolves Bertrand paradox; creates pricing power
- Hotelling model setup
  - Consumers on [0, 1] line; transport cost t
  - Utility: v - pⱼ - t|x - locⱼ|
- **Worked example: Hotelling equilibrium (fixed locations)**
  - Find indifferent consumer
  - Derive demand, profit maximization
  - p* = c + t
- **Welfare analysis in Hotelling** (deeper than undergrad)
  - Total welfare = consumer surplus + profits
  - Optimal firm locations vs equilibrium locations
  - Too much or too little differentiation?
  - Transport costs as deadweight loss
- Connection to demand estimation
  - Hotelling = specific differentiated Bertrand
  - Characteristics space generalizes this
- Merger simulation preview
  - Pre/post-merger ownership matrix

*Source:* Adapt from `previous_courses/undergraduate_io/slides/`
*Reference:* Cabral Ch 12, 14

---

### Lecture 9 (Mon, Feb 16) - Entry and Market Structure

**Part 1: Entry and Market Structure** (Cabral Ch 10)

Main topics:
- What determines market structure?
- Free entry condition
  - Enter if π > F; Equilibrium: π(N*) ≥ F > π(N* + 1)
- **Worked example: Entry with Cournot**
  - *Given demand and costs, find equilibrium number of firms*
- Fixed costs and natural monopoly
  - High F → few firms; economies of scale
- Excess entry theorem (brief)
  - Free entry may produce "too many" firms (business stealing)

*Source:* Adapt from `previous_courses/undergraduate_io/slides/`
*Reference:* Cabral Ch 10

---

**Part 2: Entry Deterrence** (Cabral Ch 15)

Main topics:

**Entry barriers**
- Structural barriers: economies of scale, capital requirements, patents
- Strategic barriers: incumbent behavior designed to deter entry

**Entry deterrence strategies**
- Limit pricing: price low enough that entry is unprofitable
- Capacity commitment: build excess capacity as credible threat
- **Game theory note (from ECN 532):** Students know SPE and backward induction
  - Entry deterrence is a classic sequential game application
  - Key question: Is the incumbent's threat to fight credible?

**Worked example: Entry deterrence game (uses SPE from ECN 532)**
- Stage 1: Incumbent chooses capacity K (or commits to fight/accommodate)
- Stage 2: Entrant observes and decides enter/stay out
- Stage 3: If entry, firms compete (Cournot or Bertrand)
- Solve by backward induction:
  - Find post-entry equilibrium profits
  - Entrant enters if π_E(enter) > 0
  - Incumbent chooses K to deter if deterrence is profitable
- *This is an IO application of the sequential games they studied*

**Predatory pricing (brief)**
- Price below cost to drive out competitor
- Requires "deep pockets" - must survive losses longer than rival
- Antitrust concern: hard to distinguish from legitimate competition

*Source:* Adapt from `previous_courses/undergraduate_io/slides/`
*Reference:* Cabral Ch 15

---

### Lecture 10 (Wed, Feb 18) - Horizontal Relationships

**[HW2 Released]**

**Part 1: Mergers** (Cabral Ch 11)

Main topics:
- Horizontal mergers: competitors combining
- Merger effects in Cournot
  - Often unprofitable without efficiencies (merger paradox - brief)
- Merger effects with differentiation
  - Internalize substitution → higher prices
- **Merger simulation in detail**
  - Use demand estimates
  - Change ownership matrix H
  - Solve for new equilibrium prices
  - *This connects Part 1 to Part 2*
- **Worked example: Simple merger simulation**
  - Two firms, each with one product. Products are substitutes.
  - Given: demand elasticities (own = -3, cross = 1), MC = 10, pre-merger prices = 15
  - Pre-merger: each firm maximizes own profit
  - Post-merger: single firm maximizes joint profit, internalizes substitution
  - Show: post-merger price increases (because cross-elasticity now "counts")
  - *Walk through the FOC change when ownership matrix changes*
- HW2 preview: merger simulation exercise (more products, given demand system)

*Source:* Adapt from `previous_courses/undergraduate_io/slides/`
*Reference:* Cabral Ch 11

---

**Part 2: Merger Policy** (Cabral Ch 11)

Main topics:
- Antitrust and merger policy
  - DOJ/FTC review, Horizontal Merger Guidelines
- Market definition
  - SSNIP test (5% price increase)
- Concentration measures
  - HHI = Σsᵢ²; Merger guidelines thresholds
- **Worked example: HHI calculation**
  - *Pre/post-merger HHI for a given market*
- Efficiency defense
  - Williamson trade-off: market power vs efficiency
- Recent merger cases (discussion)
  - Tech industry mergers (Google/Fitbit, Microsoft/Activision)
  - Hospital mergers
  - How theory applies to real cases

*Source:* Adapt from `previous_courses/undergraduate_io/slides/`
*Reference:* Cabral Ch 11

---

### Lecture 11 (Mon, Feb 23) - Vertical Relationships

**Part 1: Vertical Relationships I** (Cabral Ch 13)

Main topics:
- Vertical relationships: upstream and downstream firms
- **Worked example: Double marginalization**
  - Upstream monopolist + downstream monopolist
  - Two markups → price too high
  - *Calculate prices with/without integration*
- Solutions to double marginalization
  - Vertical integration
  - Two-part tariff (wholesale at MC + franchise fee)

*Source:* Adapt from `previous_courses/undergraduate_io/slides/`
*Reference:* Cabral Ch 13

---

**Part 2: Vertical Restraints** (Cabral Ch 13)

Main topics:
- Vertical restraints overview
  - Exclusive dealing, exclusive territories, tying
- Free-rider problem
  - Retailer provides services; consumers free-ride
  - RPM and exclusive territories as solutions
- Inter-brand vs intra-brand competition
  - Vertical restraints often reduce intra-brand
- Antitrust analysis (brief)
  - Rule of reason; efficiency justifications

*Source:* Adapt from `previous_courses/undergraduate_io/slides/`
*Reference:* Cabral Ch 13

---

### Lecture 12 (Wed, Feb 25) - Guest Lecture & Collusion

**Part 1: Guest Lecture (TBD)**

- Topic TBD based on guest availability
- Likely: applied IO research or industry experience

---

**Part 2: Collusion** (Cabral Ch 8)

Main topics:

**Brief refresher (from ECN 532):**
- Collusion: firms coordinating to raise prices
- Grim trigger strategy: collude until deviation, then Nash forever
- Basic condition: δ ≥ (πᴰ - πᶜ)/(πᴰ - πᴺᴱ) — students derived this in ECN 532, just remind them

**NEW: Critical discount factor with N firms (TESTABLE)**
- For symmetric Cournot with linear demand P = a - bQ:
  - Collusive profit per firm: πᶜ = πᴹ/N
  - Nash profit per firm: πᴺᴱ = [(a-c)/b(N+1)]² × (1/b)
  - Deviation profit: πᴰ (best response to others playing qᶜ)
- **Closed-form result for symmetric linear Cournot:**
  - δ* = (N+1)² / [N² + (N+1)²]
  - For N=2: δ* = 9/17 ≈ 0.53
  - For N=4: δ* = 25/41 ≈ 0.61
  - For N=10: δ* = 121/221 ≈ 0.55
- **Key insight:** Collusion becomes harder with more firms (higher δ* needed)
- **Worked example:** *"Market has 3 symmetric Cournot firms. Calculate minimum δ for collusion."*

**NEW: Cournot vs Bertrand collusion (TESTABLE)**
- Bertrand (homogeneous): πᴺᴱ = 0, so punishment is more severe
- For N-firm symmetric Bertrand:
  - πᶜ = πᴹ/N (split monopoly profits)
  - πᴰ = πᴹ (undercut slightly, capture whole market)
  - δ* = (πᴹ - πᴹ/N) / πᴹ = **(N-1)/N**
  - For N=2: δ* = 1/2 = 0.5
  - For N=4: δ* = 3/4 = 0.75
- **Key insight:** Compare Cournot vs Bertrand at N=2:
  - Cournot: δ* ≈ 0.53
  - Bertrand: δ* = 0.50
  - Bertrand collusion slightly easier because punishment (P=MC, π=0) is harsher!
- **Worked example:** *"Compare minimum δ for collusion in Cournot vs Bertrand duopoly."*

**NEW: Detection probability and fines (TESTABLE - policy relevant)**
- Cartel detected with probability ρ per period, pays fine F
- Modified collusion condition incorporates expected fines:
  - δ* = (πᴰ - πᶜ + ρF) / (πᴰ - πᴺᴱ + ρF)
- **Key insight:** Higher ρ or higher F → higher δ* → harder to sustain collusion
- **Worked example:** *"Cartel earns πᶜ=100/period. Detection prob ρ=0.1, fine F=500. πᴺᴱ=25, πᴰ=150. Find minimum δ."*
  - Answer: δ* = (150 - 100 + 50)/(150 - 25 + 50) = 100/175 = 4/7 ≈ 0.57

**NEW: Leniency programs (conceptual + simple calculation)**
- First firm to report gets reduced/zero fine
- Changes incentives: "race to report" destabilizes cartels
- Simple model: If reporting gives immunity, deviation becomes more attractive
- **Policy insight:** US leniency program (1993) → cartel detection increased dramatically
- Intuition question (exam): *"Explain why leniency programs help detect cartels."*

**Green-Porter model (intuition only - from ECN 532)**
- Students saw trigger strategies; this extends to unobservable actions
- Demand uncertainty: can't tell if low sales = cheating or bad demand
- Price wars as equilibrium punishment (not deviation!)
- Intuition only - calculation not on exam

**Algorithmic collusion (current policy topic)**
- Can pricing algorithms learn to collude without explicit communication?
- Calvano et al. (2020): Q-learning algorithms coordinate on supracompetitive prices
- Policy question: Does this violate antitrust law?
- Brief discussion—2-3 slides

*Source:* Adapt from `previous_courses/undergraduate_io/slides/`
*Reference:* Cabral Ch 8, Harrington (2006) for detection/leniency

---

### Lecture 13 (Mon, Mar 2) - Review

**[HW2 Due]**

**Part 1: Review - Competition Models**

Main topics:
- Cournot/Bertrand/Hotelling review
- Entry and market structure review
- Merger analysis review
- **Practice problems (exam-style)**
  - Oligopoly equilibrium
  - Entry problems
  - Merger simulation

---

**Part 2: Review - Vertical & Collusion + Comprehensive**

Main topics:
- Vertical relationships review (double marginalization)
- Collusion review (critical discount factor, Green-Porter)
- Comprehensive review
  - Connect demand estimation to merger analysis
- **Practice exam questions**
  - Full exam-style problems

---

### Lecture 14 (Wed, Mar 4) - Final Exam

**FINAL EXAM**
- 70 minutes
- Calculator + two-sided cheat sheet allowed
- Cumulative (covers all course material)

---

## Econometrics Exam Questions (Demand Estimation)

The midterm should include econometrics questions. These build through the course:

### Question Type 1: Interpreting Logit Coefficients
**Lecture coverage:** Lecture 2 Part 1 (elasticity worked example)
**HW1 coverage:** Interpret coefficient estimates from pyblp output
**Exam question example:**
> "You estimate a logit demand model and obtain α = -0.8 (price coefficient) and β_HP = 0.3 (horsepower coefficient).
> (a) Interpret α. What does a more negative α mean?
> (b) Product A has price $25,000 and market share 5%. Calculate its own-price elasticity.
> (c) If α were estimated using OLS instead of IV, would you expect the estimate to be biased toward zero or away from zero? Explain."

### Question Type 2: Endogeneity and Instrumental Variables
**Lecture coverage:** Lecture 2 Part 2 (endogeneity + IV worked examples)
**HW1 coverage:** Discussion question on IV choice
**Exam question example:**
> "In the Berry (1994) demand model, ln(sⱼ) - ln(s₀) = xⱼβ + αpⱼ + ξⱼ.
> (a) What does ξⱼ represent? Give two examples.
> (b) Why is price endogenous in this regression?
> (c) A researcher proposes using gasoline prices as an instrument for car prices. Is this a valid instrument? Explain using the two IV conditions."

### Question Type 3: IIA and Substitution Patterns
**Lecture coverage:** Lecture 2 Part 1 (IIA), Lecture 3 Part 2 (limitations)
**HW1 coverage:** Examine cross-elasticity patterns
**Exam question example:**
> "Consider a market with three products: Honda Civic, Toyota Camry, and BMW 3-Series. You estimate a logit demand model.
> (a) Under the logit model, if the Civic is removed from the market, what fraction of its consumers switch to the Camry vs the BMW?
> (b) Is this realistic? Why or why not?
> (c) What property of the logit model causes this issue? (Name it.)"

### Question Type 4: Elasticity Calculation
**Lecture coverage:** Lecture 2 Part 1 (worked example)
**HW1 coverage:** Compute elasticities from estimates
**Exam question example:**
> "A logit demand model yields α = -0.5. Product j has price pⱼ = $40 and market share sⱼ = 0.08.
> (a) Calculate the own-price elasticity of demand for product j.
> (b) Calculate the cross-price elasticity with respect to product k, which has pₖ = $35 and sₖ = 0.12.
> (c) Under logit, cross-elasticities only depend on the price and share of which product? Why is this a limitation?"

---

## Assessment Integration: Demand Estimation

| Concept | Lecture (introduce) | HW1 (apply) | Lecture 6 (review) | Midterm (test) |
|---------|---------------------|-------------|---------------------|----------------|
| Logit elasticity formula | L2 Part 1 worked example | Q: compute elasticities | Review + practice | Short answer |
| Endogeneity of price | L2 Part 2 worked example | Q: discuss IV choice | Review | MC or short answer |
| IV conditions | L2 Part 2 | Q: evaluate proposed IV | Review + practice | Short answer |
| IIA limitation | L2 Part 1, L3 Part 2 | Q: examine cross-elasticities | Review | Short answer |
| Interpret coefficients | L3 Part 1, L4 Part 1 | Full pyblp output | Review | Longer problem |

**Principle:** Every exam question has a clear path: Lecture → Homework → Review → Exam

---

## Collusion Exam Questions (Final Exam - NEW content beyond ECN 532)

These questions test material NOT covered in Hector's course:

### Question Type 1: Critical Discount Factor with N Firms
**Lecture coverage:** Lecture 12 Part 2 (new derivation)
**Exam question example:**
> "Consider a market with N = 4 symmetric Cournot firms. Linear demand is P = 100 - Q, and each firm has MC = 20.
> (a) Calculate the Nash equilibrium quantity per firm and industry profit.
> (b) Calculate the collusive (monopoly) quantity and profit per firm if they split equally.
> (c) If one firm deviates while others produce collusive quantities, find the deviator's profit.
> (d) Calculate the minimum discount factor δ* needed to sustain collusion.
> (e) How does δ* change if a 5th firm enters? Explain the intuition."

### Question Type 2: Cournot vs Bertrand Collusion
**Lecture coverage:** Lecture 12 Part 2 (new comparison)
**Exam question example:**
> "Compare collusion sustainability under Cournot and Bertrand competition.
> (a) For a duopoly, the critical discount factor under Cournot is δ* ≈ 0.53 and under Bertrand is δ* = 0.50. Which type of competition makes collusion easier to sustain?
> (b) Explain why this is the case. (Hint: Consider the severity of punishment.)
> (c) For N = 4 firms under Bertrand with homogeneous goods, calculate δ* = (N-1)/N.
> (d) As N increases, does Bertrand collusion become easier or harder? Compare to Cournot."

### Question Type 3: Detection and Fines
**Lecture coverage:** Lecture 12 Part 2 (new policy model)
**Exam question example:**
> "A cartel of 3 firms earns collusive profits πᶜ = 80 per firm per period. If they compete, each earns πᴺᴱ = 20. If one firm deviates, it earns πᴰ = 120. The cartel faces detection probability ρ = 0.15 per period with fine F = 400 per firm.
> (a) Without detection risk (ρ = 0), what is the minimum δ for collusion?
> (b) With detection risk, use δ* = (πᴰ - πᶜ + ρF)/(πᴰ - πᴺᴱ + ρF) to find the new minimum δ.
> (c) The government considers doubling the fine to F = 800. By how much does δ* increase?
> (d) Alternatively, the government could increase detection probability to ρ = 0.30 (same original fine). Which policy is more effective at destabilizing the cartel? Calculate and compare."

### Question Type 4: Leniency Programs (Conceptual)
**Lecture coverage:** Lecture 12 Part 2 (policy discussion)
**Exam question example:**
> "(a) Explain what a leniency program is and how it works.
> (b) Why does offering immunity to the first firm to report destabilize cartels? Use game theory intuition.
> (c) The US introduced its modern leniency program in 1993. Cartel prosecutions increased dramatically afterward. Is this evidence that leniency programs work, or could there be an alternative explanation?
> (d) A critic argues: 'Leniency programs reward criminals.' Provide an economic defense of leniency programs."

---

## Assessment Integration: Collusion (NEW)

| Concept | Lecture (introduce) | HW2 (apply) | Lecture 13 (review) | Final (test) |
|---------|---------------------|-------------|---------------------|--------------|
| δ* with N firms | L12 worked example | Q: compute for given N | Review + practice | Calculation |
| Cournot vs Bertrand collusion | L12 comparison | Q: compare for duopoly | Review | Short answer |
| Detection + fines model | L12 worked example | Q: policy analysis | Review | Calculation |
| Leniency programs | L12 discussion | Q: explain mechanism | Review | Conceptual |

---

## Homework Summary

| HW | Content | Due | Weight |
|----|---------|-----|--------|
| HW1 | Demand estimation (Python/pyblp): estimate logit, compute elasticities, interpret results, discuss IV | Feb 4 (L6) | 20% |
| HW2 | Part 2 topics + merger simulation (demand given) | Mar 2 (L13) | 20% |

---

## Practice Exams

- **Practice Midterm:** Very similar to actual midterm (same question types, different numbers)
  - Must include demand estimation questions (see above)
- **Practice Final:** Very similar to actual final

---

## Deliverables

Claude will create the following materials:

### 1. Lecture Slides
**Location:** `slides/`
**Structure:**
```
slides/
├── lecture_01/
│   ├── lecture_01_part1.tex    # Introduction and Pricing
│   └── lecture_01_part2.tex    # Utility Models and Demand
├── lecture_02/
│   ├── lecture_02_part1.tex    # Logit Demand Model
│   └── lecture_02_part2.tex    # Identification & IVs
├── lecture_03/
│   ├── lecture_03_part1.tex    # Demographic Interactions
│   └── lecture_03_part2.tex    # pyblp Estimation
...
├── lecture_13/
│   ├── lecture_13_part1.tex    # Review - Competition
│   └── lecture_13_part2.tex    # Review - Vertical & Collusion
└── lecture_14/
    └── (no slides - final exam)
```

### 2. Exams
**Location:** `exams/`
```
exams/
├── midterm/
│   ├── midterm.tex             # Actual midterm
│   └── midterm_solutions.tex   # Solutions
├── final/
│   ├── final.tex               # Actual final
│   └── final_solutions.tex     # Solutions
├── practice_midterm/
│   ├── practice_midterm.tex
│   └── practice_midterm_solutions.tex
└── practice_final/
    ├── practice_final.tex
    └── practice_final_solutions.tex
```

### 3. Homework Assignments
**Location:** `homework/`
```
homework/
├── hw1/
│   ├── hw1.tex                 # Problem set (demand estimation)
│   ├── hw1_solutions.tex       # Written solutions
│   ├── hw1_starter.py          # Starter code for students
│   └── hw1_solutions.py        # Solution code
└── hw2/
    ├── hw2.tex                 # Problem set (competition + merger sim)
    ├── hw2_solutions.tex
    ├── hw2_starter.py
    └── hw2_solutions.py
```

---

## Implementation Notes

1. Each Part = 60-75 minutes, 20-30 slides
2. Use LaTeX format from `previous_courses/undergraduate_io/`
3. For demand estimation: adapt PhD content to masters level (intuition over rigor)
4. Quick refreshers OK for game theory (students know from ECN 532)
5. **Every worked example should map to an exam question**
6. **Slides come in pairs** - each lecture folder has `part1.tex` and `part2.tex`

---

## CRITICAL: Voice, Notation, and Style

> **This course should sound like ME, not like AI-generated content.**

When creating slides, Claude MUST:

### 1. Copy My Wording
- Read the existing slides in `previous_courses/undergraduate_io/slides/` and `previous_courses/phd_io/`
- Use my exact phrasing where topics overlap
- Match my sentence structure, not generic textbook language
- If I say "Intuition:" on slides, keep saying "Intuition:"
- If I use casual asides like "Why does this matter?", keep that voice

### 2. Copy My Notation
- Use the SAME variable names I use (e.g., if I write π for profit, don't switch to Π)
- Match my subscript conventions (πᵢ vs π_i vs profit_i)
- Use the same symbols for elasticity, market share, etc.
- Check PhD slides for demand estimation notation specifically
- Check undergrad slides for oligopoly/pricing notation

### 3. Copy My Diagrams and Figures
- Recreate the SAME style of figures I use (TikZ, hand-drawn look, etc.)
- Use similar axis labels, colors, and annotations
- If I draw supply/demand a certain way, keep that style
- Don't introduce new diagram styles that look "polished" or AI-generated

### 4. Avoid AI-Sounding Patterns
- NO bullet points that all start with action verbs ("Identify...", "Analyze...", "Evaluate...")
- NO overly structured "learning objectives" language
- NO generic transitions like "Let's now turn to..." or "Building on this..."
- Keep my natural lecture flow - sometimes messy, sometimes with tangents
- Preserve my humor/asides if they exist in source material

### 5. When in Doubt, Quote Me
- If adapting content, prefer direct quotes from my existing slides
- Paraphrase minimally - my wording is intentional
- For NEW content (like detection/fines model), write in a style that matches adjacent slides

**Reference files for voice/style:**
- `previous_courses/undergraduate_io/slides/` - primary style reference
- `previous_courses/phd_io/demand_estimation/` - notation for empirical content
- Look at slide titles, bullet phrasing, worked example formatting

---

## Pedagogical Style

**Match tone and format from previous slides**

### Worked Examples (for key topics)
1. Concept explanation
2. Worked example slide (pose problem)
3. Students try (2-5 min)
4. Solution slide (professor walks through)

### Example structure:
```
Slide: Concept - Logit elasticity formula
Slide: Worked Example - "Given α = -0.5, p = 20, s = 0.1. Find own-price elasticity."
       [Students work 2-3 min]
Slide: Solution - ηⱼⱼ = αpⱼ(1 - sⱼ) = (-0.5)(20)(0.9) = -9
Slide: Discussion - "What happens to elasticity as market share increases?"
```

This pattern appears for KEY topics - not every concept.
