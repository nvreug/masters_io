# Lecture 03: Worked Example Redesign

## Goal
Restructure the worked example section to:
1. Match HW1's two-model structure (basic logit, then with demographics)
2. Use simpler specifications (hpwt + price, like HW1's sugar + price)
3. Show explicit model specifications before code/results

## Updated Plan Slide (7 items)
1. Recap: The IIA problem
2. The demographic interaction model
3. Why demographics help with IIA
4. Introduction to pyblp
5. Worked example: Basic logit
6. Worked example: With demographics
7. Interpreting results

## Slide Flow

### Section 5: Worked example: Basic logit

**Slide: Plan (bold item 5)**

**Slide: The BLP automobile data**
- Simplify table to show: market_id, shares, prices, hpwt
- Keep: 2,217 products across 20 years

**Slide: Model 1 specification**
```
u_{ijt} = β₁ · hpwt_{jt} + α · p_{jt} + ξ_{jt} + ε_{ijt}
```
- Parameters: β₁ (hpwt), α (price)
- Note: Simplified model with one characteristic

**Slide: Estimating Model 1 (code)**
```python
formulation = pyblp.Formulation('0 + hpwt + prices')
problem = pyblp.Problem(formulation, product_data)
results = problem.solve()
```

**Slide: Model 1 results**
- Table with β̂₁, α̂ estimates
- Note: α < 0 as expected

### Section 6: Worked example: With demographics

**Slide: Plan (bold item 6)**

**Slide: Agent data structure**
- Explain what agent_data contains:
  - market_ids: Which market each consumer draw belongs to
  - weights: Weight of each draw (e.g., 1/20 if 20 draws per market)
  - income: Draw from income distribution in that market
- Show example table:
  | market_ids | weights | income |
  |------------|---------|--------|
  | 1971       | 0.05    | 45.2   |
  | 1971       | 0.05    | 62.8   |
  | ...        | ...     | ...    |
- Note: pyblp uses these draws to integrate over consumer heterogeneity

**Slide: Model 2 specification**
```
u_{ijt} = (β₁ + β₁,inc · income_i) · hpwt_{jt} + (α₀ + α_inc · income_i) · p_{jt} + ξ_{jt} + ε_{ijt}
```
- Linear parameters: β₁, α₀
- Demographic interactions: β₁,inc, α_inc
- Note: Same structure as HW1 Q2

**Slide: Estimating Model 2 (code)**
```python
X1 = pyblp.Formulation('0 + hpwt + prices')
X2 = pyblp.Formulation('0 + hpwt + prices')
agent_formulation = pyblp.Formulation('0 + income')

problem = pyblp.Problem(
    (X1, X2), product_data,
    agent_formulation, agent_data
)
results = problem.solve(sigma=0, pi=initial_pi)
```

**Slide: Model 2 results**
- Table with all four parameters: β̂₁, α̂₀, β̂₁,inc, α̂_inc
- Interpret α_inc: positive means high-income less price-sensitive

### Section 7: Interpreting results

**Slide: Plan (bold item 7)**

**Keep existing slides (with minor updates):**
- Interpreting pyblp output
- Worked example: Interpreting coefficients (question + answer)
- Post-estimation: Elasticities
- Elasticity matrix example
- Post-estimation: Markups
- Worked example: positive price coefficient (question + answer)
- Common pyblp errors
- How to check results make sense
- This prepares you for HW1

## Key Alignment with HW1

| Lecture (cars) | HW1 (cereal) |
|----------------|--------------|
| hpwt | sugar |
| prices | prices |
| income × hpwt | income × sugar |
| income × prices | income × prices |

Both use:
- No intercept in formulation
- Two-model progression (basic → demographics)
- Same parameter structure
