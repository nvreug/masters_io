"""
Generate data previews and regression outputs for Lecture 3 slides.
Outputs LaTeX tables for:
1. Data structure preview
2. Basic logit regression results
"""

import pyblp
import pandas as pd
import numpy as np

# Suppress pyblp's verbose output
pyblp.options.verbose = False

print("=" * 60)
print("LECTURE 3: pyblp Demo Outputs")
print("=" * 60)

# =============================================================================
# 1. LOAD AND INSPECT DATA
# =============================================================================
print("\n" + "=" * 60)
print("1. DATA STRUCTURE")
print("=" * 60)

# Load BLP automobile data
product_data = pd.read_csv(pyblp.data.BLP_PRODUCTS_LOCATION)

# Show key columns
key_cols = ['market_ids', 'firm_ids', 'shares', 'prices', 'hpwt', 'air', 'mpd', 'space']
df_preview = pd.DataFrame(product_data)[key_cols].head(6)

print("\nFirst 6 rows of key columns:")
print(df_preview.to_string(index=False))

# Generate LaTeX table for data preview
print("\n--- LaTeX TABLE: Data Preview ---")
latex_data = df_preview.copy()
latex_data.columns = ['Market', 'Firm', 'Share', 'Price', 'HP/Wt', 'Air', 'MPD', 'Space']

# Round for display
for col in ['Share', 'Price', 'HP/Wt', 'MPD', 'Space']:
    if col in latex_data.columns:
        latex_data[col] = latex_data[col].round(3)

print(latex_data.to_latex(index=False, escape=False, column_format='cccccccc'))

# Show data dimensions
print("\n--- Data Summary ---")
print(f"Number of observations: {len(product_data)}")
print(f"Number of markets: {len(np.unique(product_data['market_ids']))}")
print(f"Number of firms: {len(np.unique(product_data['firm_ids']))}")

# =============================================================================
# 2. BASIC LOGIT ESTIMATION (OLS for comparison)
# =============================================================================
print("\n" + "=" * 60)
print("2. BASIC LOGIT: OLS (no IV)")
print("=" * 60)

# Simple formulation for basic logit
formulation_ols = pyblp.Formulation('1 + hpwt + air + mpd + space + prices')

# Create problem
problem_ols = pyblp.Problem(formulation_ols, product_data)
print(problem_ols)

# Solve with OLS (using identity weighting, no instruments)
results_ols = problem_ols.solve()

print("\n--- OLS Results ---")
print(results_ols)

# =============================================================================
# 3. BASIC LOGIT WITH IV
# =============================================================================
print("\n" + "=" * 60)
print("3. BASIC LOGIT: IV Estimation")
print("=" * 60)

# For IV, we need to specify that price is endogenous
# pyblp uses demand_instruments columns automatically
formulation_iv = pyblp.Formulation('1 + hpwt + air + mpd + space + prices')

problem_iv = pyblp.Problem(formulation_iv, product_data)
results_iv = problem_iv.solve()

print("\n--- IV Results ---")
print(results_iv)

# =============================================================================
# 4. EXTRACT COEFFICIENTS FOR LATEX TABLE
# =============================================================================
print("\n" + "=" * 60)
print("4. COEFFICIENT TABLE (LaTeX)")
print("=" * 60)

# Get beta estimates and standard errors
beta_ols = results_ols.beta.flatten()
se_ols = results_ols.beta_se.flatten()

beta_iv = results_iv.beta.flatten()
se_iv = results_iv.beta_se.flatten()

# Variable names (order matches formulation)
var_names = ['Constant', 'HP/Weight', 'Air', 'Miles/\\$', 'Space', 'Price']

# Create comparison table
print("\n--- LaTeX TABLE: OLS vs IV Comparison ---")
print("\\begin{tabular}{lcc}")
print("\\toprule")
print("Variable & OLS & IV \\\\")
print("\\midrule")

for i, var in enumerate(var_names):
    ols_coef = f"{beta_ols[i]:.3f}"
    ols_se = f"({se_ols[i]:.3f})"
    iv_coef = f"{beta_iv[i]:.3f}"
    iv_se = f"({se_iv[i]:.3f})"
    print(f"{var} & {ols_coef} & {iv_coef} \\\\")
    print(f" & {ols_se} & {iv_se} \\\\")

print("\\midrule")
print(f"N & {len(product_data)} & {len(product_data)} \\\\")
print("\\bottomrule")
print("\\end{tabular}")

# =============================================================================
# 5. ELASTICITIES
# =============================================================================
print("\n" + "=" * 60)
print("5. OWN-PRICE ELASTICITIES")
print("=" * 60)

# Compute elasticities
elasticities = results_iv.compute_elasticities()

# Get own-price elasticities (diagonal)
own_elasticities = []
idx = 0
for market_id in np.unique(product_data['market_ids']):
    market_mask = product_data['market_ids'] == market_id
    n_products = np.sum(market_mask)
    market_elast = elasticities[idx:idx+n_products, idx:idx+n_products]
    own_elast = np.diag(market_elast)
    own_elasticities.extend(own_elast)
    idx += n_products

own_elasticities = np.array(own_elasticities)

print(f"\nOwn-price elasticity summary:")
print(f"  Mean:   {np.mean(own_elasticities):.3f}")
print(f"  Median: {np.median(own_elasticities):.3f}")
print(f"  Min:    {np.min(own_elasticities):.3f}")
print(f"  Max:    {np.max(own_elasticities):.3f}")

# Show elasticities for a few products in first market
print("\n--- Sample Elasticities (First Market, First 5 Products) ---")
first_market = np.unique(product_data['market_ids'])[0]
market_mask = product_data['market_ids'] == first_market
n_first = min(5, np.sum(market_mask))
sample_elast = elasticities[:n_first, :n_first]

# Create dataframe for display
elast_df = pd.DataFrame(sample_elast,
                        columns=[f'P{i+1}' for i in range(n_first)],
                        index=[f'Q{i+1}' for i in range(n_first)])
print("\nCross-price elasticity matrix (first 5 products):")
print(elast_df.round(3).to_string())

print("\n" + "=" * 60)
print("SCRIPT COMPLETE")
print("=" * 60)
