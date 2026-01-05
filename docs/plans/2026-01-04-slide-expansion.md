# Slide Expansion Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Expand all lecture slides to ~40 slides per lecture (target for 2.5-hour class with 15-minute break)

**Current State:** Most lectures have 22-32 slides, need 8-18 more slides each

---

## Slide Count Analysis

| Lecture | Current | Target | Gap | Priority |
|---------|---------|--------|-----|----------|
| 1 | 41 | 40 | ✓ | Done |
| 2 | 32 | 40 | -8 | Medium |
| 3 | 28 | 40 | -12 | High |
| 4 | 25 | 40 | -15 | High |
| 5 | 28 | 40 | -12 | High |
| 6 | 29 | 40 | -11 | Medium |
| 8 | 27 | 40 | -13 | High |
| 9 | 24 | 40 | -16 | High |
| 10 | 25 | 40 | -15 | High |
| 11 | 22 | 40 | -18 | High |
| 12 | 23 | 40 | -17 | High |
| 13 | 22 | 40 | -18 | High |

---

## Expansion Strategies (in priority order)

### 1. More Worked Examples (BEST)
- Add worked examples with the reveal pattern: Question slide → Students try → Solution slide
- Each worked example = 2-3 slides
- Maps directly to exam questions (assessment integration)

### 2. Deeper Explanations of Existing Topics
- Break complex slides into multiple slides
- Add "Intuition" slides after math
- Add "Why does this matter?" discussion slides

### 3. Case Studies and Applications
- Bresnahan (1987) - competition in autos (L3, L4)
- Nevo (2001) - cereal demand (L3)
- Cola Wars case (L8)
- Magicam case (L5 - price discrimination)

### 4. Additional Theory (use sparingly)
- Only if directly relevant to exam/homework

### 5. Diagrams and Pictures (NEW)
Reuse existing visuals from previous courses to add engagement and break up text-heavy slides.

---

## Available Diagrams Inventory

### From PhD IO Course (`previous_courses/phd_io/`)
| Image | Location | Use in Lecture |
|-------|----------|----------------|
| cereal.png | demand_estimation/ | L3 - Nevo cereal demand example |
| cheerios.png | demand_estimation/ | L3 - Brand-level demand |
| figure_2_c.jpg | demand_estimation/ | L2 or L3 - empirical results |
| gwr.jpg | entry/ | L9 - Entry example |
| truck_1.jpg | entry/ | L9 - Entry barriers |

### From Undergrad IO Course (`previous_courses/undergraduate_io/slides/`)
| Image | Location | Use in Lecture |
|-------|----------|----------------|
| **Price Discrimination** | | |
| iphone.png | week_2_and_3/ | L5 - Versioning example |
| rav4.png | week_2_and_3/ | L4 - Selection by indicators |
| **Cournot/Oligopoly** | | |
| firm_1_optimum.pdf | week_7/ | L8 - Cournot profit maximization |
| best_responses.pdf | week_7/ | L8 - Reaction functions diagram |
| convergence.pdf | week_7/ | L8 - Convergence to equilibrium |
| two_extreme.pdf | week_7/ | L8 - Monopoly vs competition extremes |
| **Bertrand/Hotelling** | | |
| bertrand.jpg | week_5/ | L8 - Portrait of Bertrand (fun) |
| hotelling_consumers.pdf | week_9/ | L8 - Hotelling line diagram |
| **Entry/Stackelberg** | | |
| dupont.png | week_8/ | L9 - Capacity commitment example |
| titanium.jpg | week_8/ | L9 - Entry deterrence case |
| medicare.jpg | week_8/ | L9 - Healthcare entry |
| stackelberg_1.pdf | week_8/ | L9 - Stackelberg diagram |
| **Market Structure** | | |
| beer.jpg | week_10/ | L10 - Market concentration example |
| concentration.jpg | week_10/ | L10 - Industry concentration trends |
| hdd.jpg | week_10/ | L10 - Hard drive consolidation |
| advertising.pdf | week_10/ | L10 - Advertising & market structure |
| **Mergers** | | |
| screening.png | week_13/ | L10 - Merger screening |
| guidelines_2023.pdf | week_13/ | L10 - DOJ merger guidelines |
| horizontal_mergers_1.pdf | week_13/ | L10 - Merger diagram |
| horizontal_mergers_2.pdf | week_13/ | L10 - Merger welfare effects |
| **Collusion** | | |
| handshake.jpg | week_12/ | L12 - Collusion image |
| **Vertical** | | |
| comcast.png | week_14/ | L11 - Vertical integration example |

### TikZ Diagrams in Source Files (can copy/adapt)
| Diagram Type | Source File | Use in Lecture |
|--------------|-------------|----------------|
| Supply/demand | week_1/pricing/*.tex | L2 - Identification problem |
| Price discrimination areas | week_2_and_3/*.tex | L4, L5 - Consumer surplus |
| Game trees | week_4/*.tex | L9 - Entry deterrence games |
| Collusion timeline | week_12/collusion*.tex | L12 - Grim trigger |
| Vertical chain | week_14/*.tex | L11 - Double marginalization |

---

## Task List by Lecture

### Task 1: Lecture 2 Expansion (+8 slides)

**Current:** 32 slides
**Target:** 40 slides

**Files:**
- Modify: `slides/lecture_02/lecture_02.tex`
- Copy: TikZ supply/demand diagram from `previous_courses/undergraduate_io/slides/week_1/pricing/*.tex`

**Additions:**
1. **Part 1 - Logit Demand (+3 slides)**
   - Add worked example: "Given shares, compute mean utilities using Berry inversion" (2 slides: question + solution)
   - Add intuition slide: "What drives the IIA property?"

2. **Part 2 - Identification (+5 slides)**
   - **DIAGRAM:** Add supply/demand diagram showing identification problem (copy TikZ from week_1/pricing)
   - Add worked example: "Evaluate if gasoline prices are a valid IV" (2 slides)
   - Add slide: "Summary - What makes a good IV?"
   - Add Uber example slide (from plan outline - already drafted)

**Verification:** Run `grep -c '\\begin{frame}' slides/lecture_02/lecture_02.tex` → should show 40

---

### Task 2: Lecture 3 Expansion (+12 slides)

**Current:** 28 slides
**Target:** 40 slides

**Files:**
- Modify: `slides/lecture_03/lecture_03.tex`
- Copy: `previous_courses/phd_io/demand_estimation/cereal.png`
- Copy: `previous_courses/phd_io/demand_estimation/cheerios.png`

**Additions:**
1. **Part 1 - Demographics (+4 slides)**
   - Add slide: "Why do we need heterogeneous preferences?"
   - **PICTURE:** Add cereal.png - "Nevo (2001): Cereal demand estimation"
   - Add worked example: "Income × price interaction interpretation" (2 slides)
   - Add slide: "Limitations of demographic approach vs mixed logit"

2. **Part 2 - pyblp (+8 slides)**
   - **PICTURE:** Add cheerios.png - "Brand-level demand: what data do we need?"
   - Add 4 more slides showing actual pyblp code step-by-step
   - Add worked example: "Interpret this pyblp output" (2 slides)
   - Add slide: "Common pyblp errors and how to fix them"
   - Add slide: "How to check your results make sense"

**Verification:** Run `grep -c '\\begin{frame}' slides/lecture_03/lecture_03.tex` → should show 40

---

### Task 3: Lecture 4 Expansion (+15 slides)

**Current:** 25 slides
**Target:** 40 slides

**Files:**
- Modify: `slides/lecture_04/lecture_04.tex`
- Copy: `previous_courses/undergraduate_io/slides/week_2_and_3/rav4.png`
- Copy: TikZ consumer surplus diagram from `week_2_and_3/price_discrimination*.tex`

**Additions:**
1. **Part 1 - Consumer Surplus & IIA (+8 slides)**
   - **DIAGRAM:** Add TikZ consumer surplus area diagram (copy from price_discrimination.tex)
   - Add worked example: "Compute CS change from price increase" (2 slides)
   - Add full "Red Bus / Blue Bus" walkthrough (3 slides with math)
   - Add slide: "When is IIA 'good enough'?"
   - Add worked example: "Given logit shares, compute CS and show IIA problem" (2 slides)

2. **Part 2 - Selection by Indicators (+7 slides)**
   - **PICTURE:** Add rav4.png - "Geographic pricing: Why do car prices differ by region?"
   - Add worked example: "Two-market pricing optimization" (3 slides: setup, students try, solution)
   - Add slide: "Real-world examples of selection by indicators"
   - Add worked example: "Student discounts - calculate optimal prices" (2 slides)
   - Add slide: "When is price discrimination welfare-improving?"

**Verification:** Run `grep -c '\\begin{frame}' slides/lecture_04/lecture_04.tex` → should show 40

---

### Task 4: Lecture 5 Expansion (+12 slides)

**Current:** 28 slides
**Target:** 40 slides

**Files:**
- Modify: `slides/lecture_05/lecture_05.tex`
- Copy: `previous_courses/undergraduate_io/slides/week_2_and_3/iphone.png`

**Additions:**
1. **Part 1 - Two-Part Tariffs (+6 slides)**
   - Add worked example: "Gym membership pricing" (3 slides)
   - Add slide: "Two-part tariffs with heterogeneous consumers"
   - Add worked example: "Choose F and p to maximize profit with two consumer types" (2 slides)

2. **Part 2 - Self-Selection (+6 slides)**
   - Add slide: "The self-selection problem - why can't we just ask?"
   - **PICTURE:** Add iphone.png - "iPhone versioning: 64GB vs 256GB"
   - Add worked example: "Airline ticket menu design" (3 slides with IC/IR constraints)
   - Add slide: "Damaged goods - Intel 486 case"
   - Add slide: "Summary: When does each type of price discrimination apply?"

**Verification:** Run `grep -c '\\begin{frame}' slides/lecture_05/lecture_05.tex` → should show 40

---

### Task 5: Lecture 6 Expansion (+11 slides)

**Current:** 29 slides
**Target:** 40 slides

**Files:**
- Modify: `slides/lecture_06/lecture_06.tex`

**Additions:**
1. **Part 1 - Demand Review (+5 slides)**
   - Add 2 more practice problems (4 slides: 2 questions, 2 solutions)
   - Add slide: "Quick summary: Logit elasticity formulas"

2. **Part 2 - Pricing Review (+6 slides)**
   - Add 2 more practice problems (4 slides)
   - Add slide: "Price discrimination decision tree - which type?"
   - Add slide: "Checklist for midterm preparation"

**Verification:** Run `grep -c '\\begin{frame}' slides/lecture_06/lecture_06.tex` → should show 40

---

### Task 6: Lecture 8 Expansion (+13 slides)

**Current:** 27 slides
**Target:** 40 slides

**Files:**
- Modify: `slides/lecture_08/lecture_08.tex`
- Copy: `previous_courses/undergraduate_io/slides/week_7/best_responses.pdf`
- Copy: `previous_courses/undergraduate_io/slides/week_7/convergence.pdf`
- Copy: `previous_courses/undergraduate_io/slides/week_9/hotelling_consumers.pdf`
- Copy: `previous_courses/undergraduate_io/slides/week_5/bertrand.jpg`

**Additions:**
1. **Part 1 - Cournot/Bertrand (+7 slides)**
   - **DIAGRAM:** Add best_responses.pdf - Cournot reaction functions
   - **DIAGRAM:** Add convergence.pdf - Convergence to Cournot equilibrium
   - **PICTURE:** Add bertrand.jpg - Portrait of Joseph Bertrand (adds personality!)
   - Add worked example: "3-firm Cournot with asymmetric costs" (3 slides)
   - Add slide: "Lerner index in Cournot - the sᵢ/|ε| formula"
   - Add worked example: "Compute Lerner index from Cournot equilibrium" (2 slides)
   - Add slide: "Summary: Cournot vs Bertrand predictions"

2. **Part 2 - Hotelling (+6 slides)**
   - **DIAGRAM:** Add hotelling_consumers.pdf - The Hotelling line with consumers
   - Add worked example: "Hotelling with different marginal costs" (3 slides)
   - Add slide: "Hotelling and product positioning"
   - Add slide: "Connection to demand estimation - characteristics space"
   - Add slide: "Preview: How does this connect to merger simulation?"

**Verification:** Run `grep -c '\\begin{frame}' slides/lecture_08/lecture_08.tex` → should show 40

---

### Task 7: Lecture 9 Expansion (+16 slides)

**Current:** 24 slides
**Target:** 40 slides

**Files:**
- Modify: `slides/lecture_09/lecture_09.tex`
- Copy: `previous_courses/undergraduate_io/slides/week_8/dupont.png`
- Copy: `previous_courses/undergraduate_io/slides/week_8/titanium.jpg`
- Copy: `previous_courses/undergraduate_io/slides/week_8/stackelberg_1.pdf`
- Copy: `previous_courses/phd_io/entry/gwr.jpg`
- Copy: TikZ game tree from `week_4/game_theory*.tex`

**Additions:**
1. **Part 1 - Entry (+8 slides)**
   - Add slide: "What determines market structure? Overview"
   - **PICTURE:** Add gwr.jpg - "Entry example: How many firms can a market support?"
   - Add worked example: "Free entry with Cournot - find N*" (3 slides)
   - Add slide: "Natural monopoly and economies of scale"
   - Add worked example: "Is entry socially optimal?" (2 slides)
   - Add slide: "Excess entry theorem - intuition"

2. **Part 2 - Entry Deterrence (+8 slides)**
   - Add slide: "Types of entry barriers"
   - **PICTURE:** Add dupont.png - "DuPont titanium dioxide: Capacity as entry deterrence"
   - **PICTURE:** Add titanium.jpg - "The titanium dioxide market"
   - Add worked example: "Limit pricing calculation" (3 slides)
   - **DIAGRAM:** Add stackelberg_1.pdf - Stackelberg leadership diagram
   - Add slide: "Capacity commitment as entry deterrence"
   - **DIAGRAM:** Add game tree for entry deterrence (copy TikZ from week_4)
   - Add worked example: "Entry deterrence game - solve by backward induction" (3 slides)

**Verification:** Run `grep -c '\\begin{frame}' slides/lecture_09/lecture_09.tex` → should show 40

---

### Task 8: Lecture 10 Expansion (+15 slides)

**Current:** 25 slides
**Target:** 40 slides

**Files:**
- Modify: `slides/lecture_10/lecture_10.tex`
- Copy: `previous_courses/undergraduate_io/slides/week_10/concentration.jpg`
- Copy: `previous_courses/undergraduate_io/slides/week_10/beer.jpg`
- Copy: `previous_courses/undergraduate_io/slides/week_10/hdd.jpg`
- Copy: `previous_courses/undergraduate_io/slides/week_13/screening.png`
- Copy: `previous_courses/undergraduate_io/slides/week_13/horizontal_mergers_1.pdf`

**Additions:**
1. **Part 1 - Mergers (+8 slides)**
   - **PICTURE:** Add concentration.jpg - "Industry concentration over time"
   - Add slide: "The merger paradox - why merge?"
   - Add worked example: "Simple 2-firm merger simulation" (4 slides: setup, ownership matrix, new FOCs, solve)
   - **DIAGRAM:** Add horizontal_mergers_1.pdf - Merger welfare effects diagram
   - Add slide: "Connection to HW2"
   - Add slide: "What drives merger profitability?"
   - Add slide: "Efficiency defense intuition"

2. **Part 2 - Merger Policy (+7 slides)**
   - **PICTURE:** Add beer.jpg - "The beer industry: A merger case study"
   - **PICTURE:** Add hdd.jpg - "Hard drive consolidation: From 80+ to 3 firms"
   - **PICTURE:** Add screening.png - "DOJ merger screening process"
   - Add worked example: "HHI before/after merger" (2 slides)
   - Add slide: "DOJ/FTC merger guidelines thresholds"
   - Add slide: "Market definition - SSNIP test walkthrough"
   - Add slide: "Recent cases: Microsoft/Activision"
   - Add slide: "Recent cases: Hospital mergers"
   - Add slide: "Summary: Merger review framework"

**Verification:** Run `grep -c '\\begin{frame}' slides/lecture_10/lecture_10.tex` → should show 40

---

### Task 9: Lecture 11 Expansion (+18 slides)

**Current:** 22 slides
**Target:** 40 slides

**Files:**
- Modify: `slides/lecture_11/lecture_11.tex`
- Copy: `previous_courses/undergraduate_io/slides/week_14/comcast.png`
- Copy: TikZ vertical chain diagram from `week_14/vertical_relationships*.tex`

**Additions:**
1. **Part 1 - Double Marginalization (+9 slides)**
   - **DIAGRAM:** Add TikZ vertical supply chain diagram (copy from vertical_relationships.tex)
   - Add slide: "Vertical relationships overview"
   - **NEW DIAGRAM:** Create simple "Upstream → Downstream → Consumer" flow chart
   - Add worked example: "Double marginalization calculation" (4 slides: setup, upstream price, downstream price, integrated price)
   - Add slide: "Why is double marginalization bad for everyone?"
   - Add slide: "Solutions overview"
   - Add worked example: "Two-part tariff solves double marginalization" (2 slides)

2. **Part 2 - Vertical Restraints (+9 slides)**
   - **PICTURE:** Add comcast.png - "Comcast/NBC merger: Vertical integration in media"
   - Add slide: "Types of vertical restraints - overview"
   - Add slide: "Exclusive dealing - example"
   - Add slide: "Free-rider problem detailed"
   - **NEW DIAGRAM:** Free-rider problem illustration (retailer services → consumer free-rides)
   - Add worked example: "Why does free-riding hurt manufacturers?" (2 slides)
   - Add slide: "RPM as solution to free-riding"
   - Add slide: "Inter-brand vs intra-brand competition"
   - Add slide: "Antitrust treatment of vertical restraints"
   - Add slide: "Summary: When are vertical restraints procompetitive?"

**Verification:** Run `grep -c '\\begin{frame}' slides/lecture_11/lecture_11.tex` → should show 40

---

### Task 10: Lecture 12 Expansion (+17 slides)

**Current:** 23 slides
**Target:** 40 slides

**Files:**
- Modify: `slides/lecture_12/lecture_12.tex`
- Copy: `previous_courses/undergraduate_io/slides/week_12/handshake.jpg`
- Copy: TikZ collusion timeline from `week_12/collusion*.tex`

**Additions:**
1. **Part 1 - Guest Lecture (+0 slides)**
   - Keep placeholder for guest lecture

2. **Part 2 - Collusion (+17 slides)**
   - **PICTURE:** Add handshake.jpg - "Collusion: Secret agreements to raise prices"
   - **DIAGRAM:** Add TikZ collusion timeline (copy from collusion.tex) - "Grim trigger strategy: Cooperate → Deviate → Punish forever"
   - Add slide: "Collusion refresher - grim trigger"
   - Add worked example: "Critical discount factor for N=3 Cournot" (3 slides)
   - **NEW DIAGRAM:** Create plot showing δ* vs N (increases with more firms)
   - Add slide: "Closed-form formula: δ* = (N+1)²/[N² + (N+1)²]"
   - Add worked example: "How does δ* change with N?" (2 slides)
   - Add slide: "Cournot vs Bertrand collusion - key insight"
   - Add worked example: "Compare δ* in duopoly Cournot vs Bertrand" (2 slides)
   - Add slide: "Detection and fines model setup"
   - Add worked example: "Calculate δ* with detection probability" (3 slides)
   - Add slide: "Leniency programs - how they work"
   - **NEW PICTURE:** Find/create image of lysine cartel or vitamin cartel case
   - Add slide: "Policy effectiveness: detection vs fines"
   - Add slide: "Algorithmic collusion - current debate"

**Verification:** Run `grep -c '\\begin{frame}' slides/lecture_12/lecture_12.tex` → should show 40

---

### Task 11: Lecture 13 Expansion (+18 slides)

**Current:** 22 slides
**Target:** 40 slides

**Files:**
- Modify: `slides/lecture_13/lecture_13.tex`

**Additions:**
1. **Part 1 - Competition Review (+9 slides)**
   - Add 2 practice problems: Cournot equilibrium (4 slides)
   - Add 1 practice problem: Merger simulation (3 slides)
   - Add slide: "Competition models summary table"
   - Add slide: "Connection: demand estimation → merger simulation"

2. **Part 2 - Comprehensive Review (+9 slides)**
   - Add 2 practice problems: Collusion (4 slides)
   - Add 1 practice problem: Vertical integration (2 slides)
   - Add slide: "Course themes: Market power measurement"
   - Add slide: "Course themes: Policy implications"
   - Add slide: "Final exam preparation checklist"

**Verification:** Run `grep -c '\\begin{frame}' slides/lecture_13/lecture_13.tex` → should show 40

---

## Implementation Notes

1. **Match existing style**: Copy phrasing, notation, and diagram style from existing slides
2. **Worked examples pattern**: Question slide → "(Try this - 2 minutes)" → Solution slide
3. **Assessment integration**: Each new worked example should map to a potential exam question
4. **Don't over-polish**: Keep natural lecture flow, occasional asides
5. **Source material**: Draw from `previous_courses/undergraduate_io/` and textbooks

---

## New Diagrams to Create

These diagrams don't exist in previous courses but would be valuable:

### Demand Estimation (L2-L4)
| Diagram | Lecture | Description |
|---------|---------|-------------|
| Identification problem | L2 | Supply/demand with multiple equilibrium points, showing we can't identify either curve |
| Uber price experiment | L2 | Two riders at same corner seeing different surge prices |
| Red bus / blue bus | L4 | Three circles (Car, Red Bus, Blue Bus) showing IIA substitution problem |
| Log-sum CS formula | L4 | Visual showing how expected utility aggregates across options |

### Competition Models (L8-L10)
| Diagram | Lecture | Description |
|---------|---------|-------------|
| Cournot profit surface | L8 | 3D surface showing πᵢ(qᵢ, qⱼ) with best response highlighted |
| Hotelling product space | L8 | Extension to 2D characteristics space (not just line) |
| Merger ownership matrix | L10 | Visual showing pre/post merger ownership matrix H |
| SSNIP test flowchart | L10 | Decision tree for market definition |

### Collusion (L12)
| Diagram | Lecture | Description |
|---------|---------|-------------|
| δ* vs N plot | L12 | Graph showing critical discount factor increases with firms |
| Leniency program game | L12 | Game tree showing "race to report" incentives |

### Vertical (L11)
| Diagram | Lecture | Description |
|---------|---------|-------------|
| Double marginalization | L11 | Price stacking: manufacturer markup + retailer markup |
| Free-rider problem | L11 | Consumer learns at Store A, buys at Store B (no service) |

### Suggestions for External Images to Find
- **Uber surge pricing screenshot** - for L2 identification lecture
- **Lysine cartel photo** (ADM executives) - for L12 collusion
- **Microsoft/Activision merger news** - for L10 merger policy
- **Amazon vertical integration diagram** - for L11 vertical relationships
- **Airline yield management screen** - for L5 price discrimination

---

## Verification Checklist

After completing all tasks, run:
```bash
cd slides && for f in lecture_*/lecture_*.tex; do echo "$f: $(grep -c '\\begin{frame}' "$f")"; done
```

Expected output:
- Each lecture should show 38-42 slides
- Total should be ~500 slides across all lectures
