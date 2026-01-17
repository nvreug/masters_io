"""
ECN 594: Homework 1 Solutions
Demand Estimation with pyblp
"""

import matplotlib
matplotlib.use('Agg')  # Non-interactive backend

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
# Q1(b): Berry Inversion
# -----------------------------------------------------------------------------
print("\n--- Q1(b): Berry Inversion ---")

# -----------------------------------------------------------------------------
# Q1(c): OLS Estimation
# -----------------------------------------------------------------------------
print("\n--- Q1(c): OLS Estimation ---")

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

# -----------------------------------------------------------------------------
# Q1(f): Own-Price Elasticities
# -----------------------------------------------------------------------------
print("\n--- Q1(f): Own-Price Elasticities ---")

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
plt.title('Q1(f): Own-Price Elasticities vs Prices (Basic Logit)', fontsize=14)
plt.axhline(y=-1, color='red', linestyle='--', alpha=0.5, label='Unit elastic')
plt.legend()
plt.tight_layout()
plt.savefig('q1e_elasticities_logit.png', dpi=150)
plt.close()

# =============================================================================
# Question 2: Logit with Demographic Interactions
# =============================================================================
print("\n" + "="*70)
print("QUESTION 2: LOGIT WITH DEMOGRAPHIC INTERACTIONS")
print("="*70)

# -----------------------------------------------------------------------------
# Q2(c): Estimation with Demographic Interactions
# -----------------------------------------------------------------------------
print("\n--- Q2(c): Estimation with Demographic Interactions ---")

# Define formulations
# X1: linear parameters (constant, sugar, price)
# X2: characteristics that interact with demographics (sugar, price)
X1_formulation = pyblp.Formulation('1 + sugar + prices')
X2_formulation = pyblp.Formulation('0 + sugar + prices')
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
# X2 vars: sugar, prices
# Demographics: income
initial_pi = np.array([
    [0.1],   # income effect on sugar (beta_1_inc)
    [-5.0]   # income effect on price (alpha_inc)
])

# Sigma = 0 (no random coefficients)
initial_sigma = np.zeros((2, 2))

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
print(f"    beta_1 (sugar):    {results_demo.beta[1, 0]:.4f}")
print(f"    alpha_0 (price):   {results_demo.beta[2, 0]:.4f}")
print(f"  Pi (demographic interactions):")
print(f"    beta_1_inc (sugar x income): {results_demo.pi[0, 0]:.4f}")
print(f"    alpha_inc (price x income):  {results_demo.pi[1, 0]:.4f}")

# -----------------------------------------------------------------------------
# Q2(e): Elasticities with Demographics (Bonus)
# -----------------------------------------------------------------------------
print("\n--- Q2(e): Elasticities with Demographic Interactions (Bonus) ---")

# Compute elasticities
elasticities_demo = results_demo.compute_elasticities()

# Focus on market C01Q1
own_elasticities_demo_C01Q1 = np.diag(elasticities_demo[mask])

# Create scatterplot
plt.figure(figsize=(8, 6))
plt.scatter(prices_C01Q1, own_elasticities_demo_C01Q1, alpha=0.7)
plt.xlabel('Price', fontsize=12)
plt.ylabel('Own-Price Elasticity', fontsize=12)
plt.title('Q2(e): Own-Price Elasticities vs Prices (With Demographics)', fontsize=14)
plt.axhline(y=-1, color='red', linestyle='--', alpha=0.5, label='Unit elastic')
plt.legend()
plt.tight_layout()
plt.savefig('q2d_elasticities_demo.png', dpi=150)
plt.close()

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
plt.close()

print("\n" + "="*70)
print("END OF SOLUTIONS")
print("="*70)
