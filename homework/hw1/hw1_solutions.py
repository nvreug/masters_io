"""
ECN 594: Homework 1 Solutions
Demand Estimation with pyblp
"""

import pyblp
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from matplotlib import pyplot as plt

# Configure pyblp
pyblp.options.digits = 4
pyblp.options.verbose = False

# =============================================================================
# Load Data
# =============================================================================
agent_data = pd.read_csv('agent_data.csv', index_col=[0])
product_data = pd.read_csv('product_data.csv', index_col=[0])

print("Product data shape:", product_data.shape)
print("Number of markets:", product_data['market_ids'].nunique())
print("Number of products:", product_data['product_ids'].nunique())

# =============================================================================
# Question 1: Basic Logit Model
# =============================================================================
print("\n" + "="*70)
print("QUESTION 1: BASIC LOGIT MODEL")
print("="*70)

# -----------------------------------------------------------------------------
# Q1(a): Berry Inversion
# -----------------------------------------------------------------------------
print("\n--- Q1(a): Berry Inversion ---")
print("""
The Berry inversion transforms the logit choice probabilities into a linear equation.

Starting from: s_j = exp(delta_j) / (1 + sum_k exp(delta_k))
              s_0 = 1 / (1 + sum_k exp(delta_k))

Taking the ratio: s_j / s_0 = exp(delta_j)

Taking logs: ln(s_j) - ln(s_0) = delta_j

Substituting delta_j = beta_0 + beta_1 * sugar_j + alpha * p_j + xi_j:

ln(s_j) - ln(s_0) = beta_0 + beta_1 * sugar_j + alpha * p_j + xi_j

This is a linear regression with:
- Dependent variable: ln(s_j) - ln(s_0)
- Regressors: constant, sugar, price
- Error term: xi_j (unobserved quality)
""")

# -----------------------------------------------------------------------------
# Q1(b): OLS Estimation
# -----------------------------------------------------------------------------
print("\n--- Q1(b): OLS Estimation ---")

# Compute outside share and create dependent variable
product_data_est = product_data.copy()
product_data_est['share_outside'] = 1 - (
    product_data_est
    .groupby('market_ids', as_index=False)['shares']
    .transform(sum)
)
product_data_est['y'] = (
    np.log(product_data_est['shares'])
    - np.log(product_data_est['share_outside'])
)

# OLS estimation
model_ols = smf.ols(
    formula='y ~ prices + sugar',
    data=product_data_est
)
result_ols = model_ols.fit()
print(result_ols.summary())

print("\nOLS Coefficients:")
print(f"  beta_0 (constant): {result_ols.params['Intercept']:.4f}")
print(f"  beta_1 (sugar):    {result_ols.params['sugar']:.4f}")
print(f"  alpha (price):     {result_ols.params['prices']:.4f}")

# -----------------------------------------------------------------------------
# Q1(c): OLS Bias Discussion
# -----------------------------------------------------------------------------
print("\n--- Q1(c): OLS Bias Discussion ---")
print("""
OLS is likely biased because prices are endogenous. Specifically:
- Firms set higher prices for products with higher unobserved quality (xi_j)
- This creates positive correlation between p_j and xi_j
- Since xi_j is in the error term, we have Cov(p_j, error) > 0
- This causes UPWARD bias in alpha (makes it less negative than true value)

Economic intuition: Products that consumers like for unobserved reasons
(brand reputation, taste, advertising) can charge higher prices. OLS
interprets high prices with high market shares as "price doesn't hurt
demand much" when really it's the unobserved quality driving both.
""")

# -----------------------------------------------------------------------------
# Q1(d): 2SLS Estimation
# -----------------------------------------------------------------------------
print("\n--- Q1(d): 2SLS Estimation ---")

# Using pyblp for 2SLS (it handles the IV estimation)
formulation_2sls = pyblp.Formulation('1 + prices + sugar')
problem_2sls = pyblp.Problem(formulation_2sls, product_data)
results_2sls = problem_2sls.solve()
print(results_2sls)

# Extract coefficients
beta_2sls = results_2sls.beta.flatten()
print("\n2SLS Coefficients:")
print(f"  beta_0 (constant): {beta_2sls[0]:.4f}")
print(f"  alpha (price):     {beta_2sls[1]:.4f}")
print(f"  beta_1 (sugar):    {beta_2sls[2]:.4f}")

print(f"\nComparison of price coefficients:")
print(f"  OLS:  alpha = {result_ols.params['prices']:.4f}")
print(f"  2SLS: alpha = {beta_2sls[1]:.4f}")
print("""
As expected, the OLS estimate is LESS negative than 2SLS (-10.2 vs -10.9).
This confirms the upward bias from price endogeneity. The 2SLS estimate
suggests consumers are MORE price sensitive than OLS would indicate.
""")

# -----------------------------------------------------------------------------
# Q1(e): Own-Price Elasticities
# -----------------------------------------------------------------------------
print("\n--- Q1(e): Own-Price Elasticities ---")

# Compute elasticities using pyblp
elasticities_2sls = results_2sls.compute_elasticities()

# Focus on market C01Q1
mask = (product_data['market_ids'] == 'C01Q1')
own_elasticities_C01Q1 = np.diag(elasticities_2sls[mask])
prices_C01Q1 = product_data.loc[mask, 'prices'].values

# Create scatterplot
plt.figure(figsize=(8, 6))
plt.scatter(prices_C01Q1, own_elasticities_C01Q1, alpha=0.7)
plt.xlabel('Price', fontsize=12)
plt.ylabel('Own-Price Elasticity', fontsize=12)
plt.title('Q1(e): Own-Price Elasticities vs Prices (Basic Logit)', fontsize=14)
plt.axhline(y=-1, color='red', linestyle='--', alpha=0.5, label='Unit elastic')
plt.legend()
plt.tight_layout()
plt.savefig('q1e_elasticities_logit.png', dpi=150)
plt.show()

print("""
Pattern observed: There is a NEGATIVE linear relationship between prices
and own-price elasticities. Higher-priced products have more elastic demand.

This is a BUG (limitation) of the basic logit model, not a feature!

In the logit model: eta_jj = alpha * p_j * (1 - s_j)

Since alpha < 0 and (1 - s_j) is approximately 1 for most products with
small shares, the elasticity is roughly proportional to price. This
mechanical relationship is imposed by the functional form, not learned
from the data.

In reality, there's no reason to expect such a tight relationship. Some
high-priced products might have inelastic demand (luxury goods, loyal
customers) while some low-priced products might have elastic demand
(commodity products, many substitutes).
""")

# =============================================================================
# Question 2: Logit with Demographic Interactions
# =============================================================================
print("\n" + "="*70)
print("QUESTION 2: LOGIT WITH DEMOGRAPHIC INTERACTIONS")
print("="*70)

# -----------------------------------------------------------------------------
# Q2(a): Interpretation of alpha_inc
# -----------------------------------------------------------------------------
print("\n--- Q2(a): Interpretation of alpha_inc ---")
print("""
alpha_inc is the effect of income on price sensitivity.

Total price coefficient for consumer i: alpha_i = alpha_0 + alpha_inc * income_i

Expected sign: POSITIVE (making alpha_i less negative for high-income consumers)

Reasoning:
- Higher-income consumers are less price sensitive (they can afford to pay more)
- alpha_0 < 0 (everyone dislikes higher prices on average)
- If alpha_inc > 0, then high-income consumers have alpha_i closer to zero
  (less negative), meaning they are less responsive to price changes

Example: If alpha_0 = -5 and alpha_inc = 2
- Consumer with income = 0: alpha = -5 (very price sensitive)
- Consumer with income = 1: alpha = -3 (less price sensitive)
""")

# -----------------------------------------------------------------------------
# Q2(b): Estimation with Demographic Interactions
# -----------------------------------------------------------------------------
print("\n--- Q2(b): Estimation with Demographic Interactions ---")

# Define formulations
# X1: linear parameters (constant, price)
# X2: characteristics that interact with demographics (constant, price, sugar)
X1_formulation = pyblp.Formulation('1 + prices')
X2_formulation = pyblp.Formulation('1 + prices + sugar')
product_formulations = (X1_formulation, X2_formulation)

# Agent formulation: demographics that interact with X2
agent_formulation = pyblp.Formulation('0 + income')

# Setup problem
problem_demo = pyblp.Problem(
    product_formulations,
    product_data,
    agent_formulation,
    agent_data
)

# Initial values for Pi (demographic interactions)
# Pi has shape: (# X2 vars) x (# demographics)
# X2 vars: constant, prices, sugar
# Demographics: income
initial_pi = np.array([
    [1.0],   # income effect on constant
    [-5.0],  # income effect on price (expect positive to reduce sensitivity)
    [0.1]    # income effect on sugar
])

# Sigma = 0 (no random coefficients)
initial_sigma = np.zeros((3, 3))

# Optimization settings
optimization = pyblp.Optimization('bfgs', {'gtol': 1e-5})

# Solve
results_demo = problem_demo.solve(
    initial_sigma,
    initial_pi,
    optimization=optimization,
    method='1s'
)
print(results_demo)

# Extract and display parameters
print("\nParameter Estimates:")
print(f"  Beta (linear):")
print(f"    beta_0 (constant): {results_demo.beta[0, 0]:.4f}")
print(f"    alpha_0 (price):   {results_demo.beta[1, 0]:.4f}")
print(f"  Pi (demographic interactions):")
print(f"    beta_0_inc (constant x income): {results_demo.pi[0, 0]:.4f}")
print(f"    alpha_inc (price x income):     {results_demo.pi[1, 0]:.4f}")
print(f"    beta_1 (sugar x income):        {results_demo.pi[2, 0]:.4f}")

# Note: In this specification, sugar only enters through interaction
# The pure sugar effect is captured through the income interaction

# -----------------------------------------------------------------------------
# Q2(c): Elasticities with Demographics
# -----------------------------------------------------------------------------
print("\n--- Q2(c): Elasticities with Demographic Interactions ---")

# Compute elasticities
elasticities_demo = results_demo.compute_elasticities()

# Focus on market C01Q1
own_elasticities_demo_C01Q1 = np.diag(elasticities_demo[mask])

# Create scatterplot
plt.figure(figsize=(8, 6))
plt.scatter(prices_C01Q1, own_elasticities_demo_C01Q1, alpha=0.7)
plt.xlabel('Price', fontsize=12)
plt.ylabel('Own-Price Elasticity', fontsize=12)
plt.title('Q2(c): Own-Price Elasticities vs Prices (With Demographics)', fontsize=14)
plt.axhline(y=-1, color='red', linestyle='--', alpha=0.5, label='Unit elastic')
plt.legend()
plt.tight_layout()
plt.savefig('q2c_elasticities_demo.png', dpi=150)
plt.show()

# Comparison plot
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].scatter(prices_C01Q1, own_elasticities_C01Q1, alpha=0.7)
axes[0].set_xlabel('Price', fontsize=12)
axes[0].set_ylabel('Own-Price Elasticity', fontsize=12)
axes[0].set_title('Basic Logit', fontsize=14)
axes[0].axhline(y=-1, color='red', linestyle='--', alpha=0.5)

axes[1].scatter(prices_C01Q1, own_elasticities_demo_C01Q1, alpha=0.7)
axes[1].set_xlabel('Price', fontsize=12)
axes[1].set_ylabel('Own-Price Elasticity', fontsize=12)
axes[1].set_title('Logit with Demographics', fontsize=14)
axes[1].axhline(y=-1, color='red', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('q2c_comparison.png', dpi=150)
plt.show()

print("""
Comparison with Basic Logit:

With demographic interactions, the tight linear relationship between prices
and elasticities is BROKEN. The pattern is now more scattered.

Why this happens:
- In the basic logit, all consumers have the same alpha, so elasticity
  mechanically depends on price
- With demographic interactions, different consumers have different alpha_i
- The aggregate elasticity depends on the distribution of consumer types
  in each market and how they sort across products
- Products that attract high-income consumers (who are less price sensitive)
  may have lower elasticities even at high prices

This is more realistic! The model now allows the data to reveal the
relationship between prices and elasticities, rather than imposing it
through functional form.
""")

# -----------------------------------------------------------------------------
# Q2(d): IIA Discussion
# -----------------------------------------------------------------------------
print("\n--- Q2(d): Does Adding Demographics Help with IIA? ---")
print("""
IIA (Independence of Irrelevant Alternatives) says that the ratio of
choice probabilities for any two products depends only on those two
products, not on other alternatives.

Does adding demographics help?

PARTIALLY YES:
- With demographic interactions, different consumer types have different
  substitution patterns
- When a product is removed, consumers substitute based on their
  individual preferences
- High-income consumers might substitute differently than low-income
  consumers
- At the AGGREGATE level, this creates richer substitution patterns

STILL LIMITED:
- For any INDIVIDUAL consumer type, IIA still holds
- A given consumer with specific income still has logit substitution
  patterns within their preference structure
- We haven't added random coefficients that would give each consumer
  a unique preference ordering

WHAT WOULD FULLY ADDRESS IIA:
- Random coefficients (mixed logit / BLP with sigma terms)
- This allows consumers to have idiosyncratic preferences even
  conditional on demographics
- Substitution patterns then depend on similarity in characteristic
  space, not just market shares

Bottom line: Demographics help at the aggregate level by creating
different consumer segments, but don't fully solve IIA at the
individual level.
""")

# =============================================================================
# Question 3: Consumer Surplus
# =============================================================================
print("\n" + "="*70)
print("QUESTION 3: CONSUMER SURPLUS")
print("="*70)

# -----------------------------------------------------------------------------
# Q3(a): Consumer Surplus Formula
# -----------------------------------------------------------------------------
print("\n--- Q3(a): Consumer Surplus Formula ---")
print("""
For the logit model, expected consumer surplus per consumer is derived
from the expected maximum utility:

E[max_j u_ij] = E[max_j (delta_j + epsilon_ij)]

For Type 1 Extreme Value errors, this has a closed form:

E[max_j u_ij] = ln(sum_j exp(delta_j)) + gamma

where gamma is Euler's constant (approximately 0.577).

The "inclusive value" or "log-sum" is:
IV_t = ln(1 + sum_{j=1}^{J_t} exp(delta_jt))

(The 1 inside is from the outside option with delta_0 = 0)

Consumer surplus in monetary units requires dividing by the marginal
utility of income, which is |alpha|:

E[CS_t] = (1/|alpha|) * ln(1 + sum_{j=1}^{J_t} exp(delta_jt))

This gives expected CS per consumer in market t. Note:
- CS is measured relative to having no products (only outside option)
- The outside option contributes the "1" inside the log
- Each product j contributes exp(delta_jt) to the sum
""")

# -----------------------------------------------------------------------------
# Q3(b): Consumer Surplus Calculation
# -----------------------------------------------------------------------------
print("\n--- Q3(b): Consumer Surplus Calculation ---")

# Get alpha from 2SLS results
alpha = results_2sls.beta[1, 0]  # price coefficient
print(f"Price coefficient (alpha): {alpha:.4f}")

# Get delta (mean utilities) for market C01Q1
# delta = ln(s_j) - ln(s_0) from Berry inversion
# We already computed this
market_data = product_data_est[mask].copy()
delta_C01Q1 = market_data['y'].values  # This is delta from Berry inversion

print(f"\nNumber of products in C01Q1: {len(delta_C01Q1)}")
print(f"Mean delta: {delta_C01Q1.mean():.4f}")
print(f"Min delta: {delta_C01Q1.min():.4f}")
print(f"Max delta: {delta_C01Q1.max():.4f}")

# Compute inclusive value and consumer surplus
# IV = ln(1 + sum exp(delta))
IV_full = np.log(1 + np.sum(np.exp(delta_C01Q1)))
CS_full = IV_full / np.abs(alpha)

print(f"\nWith all products:")
print(f"  Inclusive Value: {IV_full:.4f}")
print(f"  Expected CS per consumer: ${CS_full:.4f}")

# Now remove product F1B04
product_ids = market_data['product_ids'].values
f1b04_idx = np.where(product_ids == 'F1B04')[0][0]
print(f"\nProduct F1B04 is at index {f1b04_idx}")
print(f"  Price: ${market_data['prices'].iloc[f1b04_idx]:.4f}")
print(f"  Sugar: {market_data['sugar'].iloc[f1b04_idx]}")
print(f"  Share: {market_data['shares'].iloc[f1b04_idx]:.4f}")
print(f"  Delta: {delta_C01Q1[f1b04_idx]:.4f}")

# CS without F1B04
delta_without_f1b04 = np.delete(delta_C01Q1, f1b04_idx)
IV_without = np.log(1 + np.sum(np.exp(delta_without_f1b04)))
CS_without = IV_without / np.abs(alpha)

print(f"\nWithout F1B04:")
print(f"  Inclusive Value: {IV_without:.4f}")
print(f"  Expected CS per consumer: ${CS_without:.4f}")

CS_change = CS_without - CS_full
print(f"\nChange in Consumer Surplus: ${CS_change:.4f}")
print(f"  (Negative means consumers are worse off)")

# -----------------------------------------------------------------------------
# Q3(c): Which Products Matter Most/Least
# -----------------------------------------------------------------------------
print("\n--- Q3(c): Which Products Matter Most/Least ---")

# Compute CS change for removing each product
cs_changes = []
for i, pid in enumerate(product_ids):
    delta_without_i = np.delete(delta_C01Q1, i)
    IV_without_i = np.log(1 + np.sum(np.exp(delta_without_i)))
    CS_without_i = IV_without_i / np.abs(alpha)
    cs_change_i = CS_without_i - CS_full
    cs_changes.append({
        'product_id': pid,
        'price': market_data['prices'].iloc[i],
        'sugar': market_data['sugar'].iloc[i],
        'share': market_data['shares'].iloc[i],
        'delta': delta_C01Q1[i],
        'cs_change': cs_change_i
    })

cs_df = pd.DataFrame(cs_changes)
cs_df = cs_df.sort_values('cs_change')

print("\nProducts ranked by CS impact (most to least harmful to remove):")
print(cs_df[['product_id', 'price', 'sugar', 'share', 'cs_change']].head(10).to_string())

print("\n...")
print(cs_df[['product_id', 'price', 'sugar', 'share', 'cs_change']].tail(5).to_string())

# Identify extremes
most_valuable = cs_df.iloc[0]
least_valuable = cs_df.iloc[-1]

print(f"\n\nProduct whose removal MOST harms consumers:")
print(f"  Product ID: {most_valuable['product_id']}")
print(f"  Price: ${most_valuable['price']:.4f}")
print(f"  Sugar: {most_valuable['sugar']}")
print(f"  Market Share: {most_valuable['share']:.4f}")
print(f"  CS Change: ${most_valuable['cs_change']:.4f}")

print(f"\nProduct whose removal LEAST harms consumers:")
print(f"  Product ID: {least_valuable['product_id']}")
print(f"  Price: ${least_valuable['price']:.4f}")
print(f"  Sugar: {least_valuable['sugar']}")
print(f"  Market Share: {least_valuable['share']:.4f}")
print(f"  CS Change: ${least_valuable['cs_change']:.4f}")

print("""
\nIntuition:

Products with HIGHER delta (mean utility) contribute more to consumer
surplus. From the log-sum formula, products with high exp(delta) have
a larger impact on the inclusive value.

What makes delta high?
- delta = beta_0 + beta_1 * sugar + alpha * price + xi
- Low price (since alpha < 0)
- Characteristics that consumers value
- High unobserved quality (xi)

The most valuable products tend to have:
- High market share (which is driven by high delta)
- Often lower prices
- Characteristics that match consumer preferences

The least valuable products tend to have:
- Low market share
- Less attractive combination of price and characteristics

This makes intuitive sense: removing a popular product that many
consumers choose hurts welfare more than removing a niche product
that few consumers buy.
""")

# Create visualization
plt.figure(figsize=(10, 6))
plt.scatter(cs_df['share'], cs_df['cs_change'], alpha=0.7)
plt.xlabel('Market Share', fontsize=12)
plt.ylabel('CS Change from Removal ($)', fontsize=12)
plt.title('Consumer Surplus Impact vs Market Share', fontsize=14)
plt.axhline(y=0, color='red', linestyle='--', alpha=0.3)
plt.tight_layout()
plt.savefig('q3c_cs_vs_share.png', dpi=150)
plt.show()

print("\n" + "="*70)
print("END OF SOLUTIONS")
print("="*70)
