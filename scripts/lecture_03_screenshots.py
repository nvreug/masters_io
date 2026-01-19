"""
Generate clean HTML outputs for Lecture 3 screenshots.
"""

import pyblp
import pandas as pd
import numpy as np
from pathlib import Path

# Suppress pyblp's verbose output
pyblp.options.verbose = False

# Output directory
output_dir = Path(__file__).parent.parent / "slides" / "lecture_03" / "figures"
output_dir.mkdir(parents=True, exist_ok=True)

# =============================================================================
# 1. DATA PREVIEW (table only, no code)
# =============================================================================
product_data = pd.read_csv(pyblp.data.BLP_PRODUCTS_LOCATION)

# Select key columns and first few rows
key_cols = ['market_ids', 'firm_ids', 'shares', 'prices', 'hpwt', 'air', 'mpd', 'space']
df_preview = product_data[key_cols].head(10).copy()

# Rename for display
df_preview.columns = ['Market', 'Firm', 'Share', 'Price', 'HP/Wt', 'Air', 'MPD', 'Space']

# Format numbers
df_preview['Share'] = df_preview['Share'].apply(lambda x: f"{x:.4f}")
df_preview['Price'] = df_preview['Price'].apply(lambda x: f"{x:.2f}")
df_preview['HP/Wt'] = df_preview['HP/Wt'].apply(lambda x: f"{x:.3f}")
df_preview['MPD'] = df_preview['MPD'].apply(lambda x: f"{x:.3f}")
df_preview['Space'] = df_preview['Space'].apply(lambda x: f"{x:.3f}")

# Create HTML - just the table, no code
html_data = """<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: 'SF Mono', 'Menlo', 'Monaco', monospace;
            background: #1e1e1e;
            color: #d4d4d4;
            padding: 20px;
            margin: 0;
        }
        .header {
            color: #569cd6;
            font-size: 16px;
            margin-bottom: 15px;
            font-weight: bold;
        }
        .table-box {
            background: #2d2d2d;
            padding: 20px;
            border-radius: 8px;
            display: inline-block;
        }
        table {
            border-collapse: collapse;
            font-size: 14px;
        }
        th {
            color: #569cd6;
            padding: 10px 18px;
            text-align: right;
            border-bottom: 2px solid #444;
            font-weight: bold;
        }
        td {
            padding: 8px 18px;
            text-align: right;
            color: #d4d4d4;
        }
        tr:nth-child(even) {
            background: #252525;
        }
        .note {
            color: #888;
            font-size: 13px;
            margin-top: 15px;
        }
    </style>
</head>
<body>
    <div class="header">BLP Automobile Data (1971-1990)</div>
    <div class="table-box">
        <table>
            <tr>
                <th>Market</th><th>Firm</th><th>Share</th><th>Price</th><th>HP/Wt</th><th>Air</th><th>MPD</th><th>Space</th>
            </tr>
"""

for _, row in df_preview.iterrows():
    html_data += f"            <tr><td>{row['Market']}</td><td>{row['Firm']}</td><td>{row['Share']}</td><td>{row['Price']}</td><td>{row['HP/Wt']}</td><td>{row['Air']}</td><td>{row['MPD']}</td><td>{row['Space']}</td></tr>\n"

html_data += """        </table>
        <p class="note">2,217 products across 20 markets (years) from 26 firms</p>
    </div>
</body>
</html>"""

with open(output_dir / "data_preview.html", "w") as f:
    f.write(html_data)

print(f"Saved: {output_dir / 'data_preview.html'}")

# =============================================================================
# 2. RESULTS OUTPUT (larger, cleaner)
# =============================================================================
formulation = pyblp.Formulation('1 + hpwt + air + mpd + space + prices')
problem = pyblp.Problem(formulation, product_data)
results = problem.solve()

# Get coefficients
beta = results.beta.flatten()
se = results.beta_se.flatten()
var_names = ['Constant', 'HP/Weight', 'Air', 'Miles/$', 'Space', 'Price']

html_results = """<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: 'SF Mono', 'Menlo', 'Monaco', monospace;
            background: #1e1e1e;
            color: #d4d4d4;
            padding: 20px;
            margin: 0;
        }
        .header {
            color: #569cd6;
            font-size: 16px;
            margin-bottom: 15px;
            font-weight: bold;
        }
        .results-box {
            background: #2d2d2d;
            padding: 25px;
            border-radius: 8px;
            display: inline-block;
        }
        table {
            border-collapse: collapse;
            font-size: 15px;
        }
        th {
            text-align: left;
            color: #4ec9b0;
            padding: 12px 20px;
            border-bottom: 2px solid #444;
            font-weight: bold;
        }
        td {
            padding: 10px 20px;
        }
        .var { color: #d4d4d4; }
        .coef { color: #dcdcaa; text-align: right; font-family: monospace; }
        .se { color: #888; text-align: right; font-size: 13px; }
        .sig { color: #4ec9b0; }
        .note { color: #888; font-size: 12px; margin-top: 15px; }
    </style>
</head>
<body>
    <div class="header">Logit Demand Estimation Results</div>
    <div class="results-box">
        <table>
            <tr>
                <th>Variable</th>
                <th style="text-align: right">Coefficient</th>
                <th style="text-align: right">Std. Error</th>
            </tr>
"""

for i, var in enumerate(var_names):
    sig = "***" if abs(beta[i] / se[i]) > 2.576 else ("**" if abs(beta[i] / se[i]) > 1.96 else "")
    html_results += f"""            <tr>
                <td class="var">{var}</td>
                <td class="coef">{beta[i]:>10.4f}<span class="sig">{sig}</span></td>
                <td class="se">({se[i]:.4f})</td>
            </tr>
"""

html_results += f"""        </table>
        <p class="note">N = 2,217 | 20 markets | Robust SEs | *** p&lt;0.01</p>
    </div>
</body>
</html>"""

with open(output_dir / "results_output.html", "w") as f:
    f.write(html_results)

print(f"Saved: {output_dir / 'results_output.html'}")

# =============================================================================
# 3. ELASTICITIES (larger)
# =============================================================================
elasticities = results.compute_elasticities()

# Get a 5x5 block for first market
n = 5
elast_sample = elasticities[:n, :n]

html_elast = """<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: 'SF Mono', 'Menlo', 'Monaco', monospace;
            background: #1e1e1e;
            color: #d4d4d4;
            padding: 20px;
            margin: 0;
        }
        .header {
            color: #569cd6;
            font-size: 16px;
            margin-bottom: 15px;
            font-weight: bold;
        }
        .matrix-box {
            background: #2d2d2d;
            padding: 25px;
            border-radius: 8px;
            display: inline-block;
        }
        table {
            border-collapse: collapse;
            font-size: 15px;
        }
        th {
            color: #569cd6;
            padding: 12px 18px;
            text-align: center;
            font-weight: bold;
        }
        td {
            padding: 10px 18px;
            text-align: right;
            font-family: monospace;
        }
        .own {
            color: #f44747;
            font-weight: bold;
        }
        .cross { color: #4ec9b0; }
        .note { color: #888; font-size: 12px; margin-top: 15px; }
    </style>
</head>
<body>
    <div class="header">Price Elasticity Matrix (First 5 Products, Market 1971)</div>
    <div class="matrix-box">
        <table>
            <tr>
                <th></th>
"""

for i in range(n):
    html_elast += f"                <th>Prod {i+1}</th>\n"
html_elast += "            </tr>\n"

for i in range(n):
    html_elast += f"            <tr>\n                <th>Prod {i+1}</th>\n"
    for j in range(n):
        cls = "own" if i == j else "cross"
        html_elast += f'                <td class="{cls}">{elast_sample[i, j]:.3f}</td>\n'
    html_elast += "            </tr>\n"

html_elast += """        </table>
        <p class="note">Diagonal (red): own-price elasticities | Off-diagonal (teal): cross-price elasticities</p>
    </div>
</body>
</html>"""

with open(output_dir / "elasticities.html", "w") as f:
    f.write(html_elast)

print(f"Saved: {output_dir / 'elasticities.html'}")

print("\nAll HTML files saved to:", output_dir)
