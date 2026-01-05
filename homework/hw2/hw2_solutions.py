"""
ECN 594: Homework 2 Solutions
Competition and Merger Simulation
"""

import numpy as np
from scipy.optimize import fsolve
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# PART A: OLIGOPOLY THEORY
# =============================================================================
print("="*70)
print("PART A: OLIGOPOLY THEORY")
print("="*70)

# -----------------------------------------------------------------------------
# Question 1: Cournot Competition
# -----------------------------------------------------------------------------
print("\n--- Question 1: Cournot Competition ---\n")

# Parameters
a = 100  # Demand intercept
c = 10   # Marginal cost

# Q1(a): 3-firm Cournot
print("Q1(a): 3-firm Cournot equilibrium")
N = 3
# Cournot formula: q* = (a - c) / (N + 1)
q_star = (a - c) / (N + 1)
Q_star = N * q_star
P_star = a - Q_star
profit_star = (P_star - c) * q_star

print(f"  Per-firm quantity: q* = {q_star:.2f}")
print(f"  Total quantity: Q* = {Q_star:.2f}")
print(f"  Price: P* = ${P_star:.2f}")
print(f"  Per-firm profit: pi* = ${profit_star:.2f}")

# Q1(b): Verify Lerner Index
print("\nQ1(b): Lerner Index verification")
L = (P_star - c) / P_star
s_j = 1 / N  # Market share
# Price elasticity of demand: dQ/dP * P/Q = -1 * P/Q
epsilon = -1 * P_star / Q_star  # Linear demand
L_formula = s_j / abs(epsilon)

print(f"  Lerner Index (direct): L = (P - MC)/P = {L:.4f}")
print(f"  Market share: s_j = {s_j:.4f}")
print(f"  Price elasticity: epsilon = {epsilon:.4f}")
print(f"  Lerner Index (formula): s_j/|epsilon| = {L_formula:.4f}")
print(f"  Match: {np.isclose(L, L_formula)}")

# Q1(c): 2-firm case and welfare comparison
print("\nQ1(c): 2-firm Cournot and welfare comparison")
N_2 = 2
q_star_2 = (a - c) / (N_2 + 1)
Q_star_2 = N_2 * q_star_2
P_star_2 = a - Q_star_2
profit_star_2 = (P_star_2 - c) * q_star_2

print(f"\n  2-firm equilibrium:")
print(f"    Per-firm quantity: q* = {q_star_2:.2f}")
print(f"    Total quantity: Q* = {Q_star_2:.2f}")
print(f"    Price: P* = ${P_star_2:.2f}")
print(f"    Per-firm profit: pi* = ${profit_star_2:.2f}")

# Consumer surplus: CS = 0.5 * Q * (a - P) = 0.5 * Q^2 (with linear demand)
CS_3 = 0.5 * Q_star**2
CS_2 = 0.5 * Q_star_2**2

# Producer surplus = total profit
PS_3 = N * profit_star
PS_2 = N_2 * profit_star_2

# Total welfare
TW_3 = CS_3 + PS_3
TW_2 = CS_2 + PS_2

print(f"\n  Welfare comparison:")
print(f"              3 firms     2 firms     Change")
print(f"  CS:         ${CS_3:8.2f}  ${CS_2:8.2f}  ${CS_2 - CS_3:+8.2f}")
print(f"  PS:         ${PS_3:8.2f}  ${PS_2:8.2f}  ${PS_2 - PS_3:+8.2f}")
print(f"  TW:         ${TW_3:8.2f}  ${TW_2:8.2f}  ${TW_2 - TW_3:+8.2f}")

print("""
  Interpretation: With fewer firms, price rises, consumer surplus falls,
  producer surplus rises, but total welfare falls due to DWL from higher price.
""")

# -----------------------------------------------------------------------------
# Question 2: Bertrand Competition
# -----------------------------------------------------------------------------
print("\n--- Question 2: Bertrand Competition ---\n")

print("Q2(a): Bertrand equilibrium with 3 identical firms")
print(f"  Equilibrium price: P* = c = ${c:.2f}")
print(f"  Per-firm profit: pi* = $0.00")
print("""
  With homogeneous products and Bertrand competition, firms undercut
  each other until price equals marginal cost (competitive outcome).
  This holds for any N >= 2.
""")

print("Q2(b): Cournot vs Bertrand comparison")
print(f"  Cournot price: ${P_star:.2f}, profit: ${profit_star:.2f}")
print(f"  Bertrand price: ${c:.2f}, profit: $0.00")
print("""
  Cournot has higher prices and profits because quantity competition
  is less aggressive than price competition.

  Bertrand is more realistic when:
  - Products are substitutes and firms can easily adjust prices
  - Capacity constraints are not binding
  - Industries with low marginal costs and high price transparency

  Cournot is more realistic when:
  - Capacity must be committed in advance (e.g., manufacturing)
  - Output is hard to adjust quickly
  - Products are slightly differentiated
""")

# -----------------------------------------------------------------------------
# Question 3: Collusion
# -----------------------------------------------------------------------------
print("\n--- Question 3: Collusion ---\n")

print("Q3(a): Monopoly outcome")
# Monopoly: Q_m = (a - c) / 2
Q_m = (a - c) / 2
P_m = a - Q_m
profit_m = (P_m - c) * Q_m
q_collusion = Q_m / N
profit_collusion = profit_m / N

print(f"  Monopoly quantity: Q_m = {Q_m:.2f}")
print(f"  Monopoly price: P_m = ${P_m:.2f}")
print(f"  Monopoly profit: pi_m = ${profit_m:.2f}")
print(f"  Per-firm collusive quantity: q = {q_collusion:.2f}")
print(f"  Per-firm collusive profit: pi = ${profit_collusion:.2f}")

print("\nQ3(b): Optimal deviation")
# If 2 firms produce q_collusion each, total from others = 2 * q_collusion
q_others = (N - 1) * q_collusion
# Best response: q_dev = (a - c - Q_others) / 2
q_dev = (a - c - q_others) / 2
Q_dev = q_dev + q_others
P_dev = a - Q_dev
profit_dev = (P_dev - c) * q_dev

print(f"  Quantity from other firms: {q_others:.2f}")
print(f"  Optimal deviation quantity: q_dev = {q_dev:.2f}")
print(f"  Price after deviation: P = ${P_dev:.2f}")
print(f"  Deviation profit: pi_dev = ${profit_dev:.2f}")

print("\nQ3(c): Critical discount factor")
# Cournot punishment profit (Nash equilibrium)
profit_punish = profit_star

# Critical discount factor
# delta* = (pi_dev - pi_coll) / (pi_dev - pi_punish)
delta_star = (profit_dev - profit_collusion) / (profit_dev - profit_punish)

# Alternative formula from class
delta_star_formula = (N + 1)**2 / (N**2 + (N + 1)**2)

print(f"  Collusion profit: ${profit_collusion:.2f}")
print(f"  Deviation profit: ${profit_dev:.2f}")
print(f"  Punishment profit: ${profit_punish:.2f}")
print(f"\n  Critical discount factor (computed): delta* = {delta_star:.4f}")
print(f"  Critical discount factor (formula): delta* = {delta_star_formula:.4f}")
print(f"""
  Firms can sustain collusion if delta >= {delta_star:.4f}.
  This means they must value future profits at least {delta_star:.1%} as much
  as current profits. With delta = 0.9 (typical), collusion is sustainable.
""")

# =============================================================================
# PART B: MERGER SIMULATION
# =============================================================================
print("\n" + "="*70)
print("PART B: MERGER SIMULATION")
print("="*70)

# Parameters
alpha = -2.0
delta = np.array([-0.5, -0.3, -0.2, -0.4])
p0 = np.array([2.0, 2.5, 3.0, 2.2])
c = np.array([1.0, 1.2, 1.5, 1.1])
M = 1000  # Market size
J = 4  # Number of products

# -----------------------------------------------------------------------------
# Question 4: Pre-Merger Equilibrium
# -----------------------------------------------------------------------------
print("\n--- Question 4: Pre-Merger Equilibrium ---\n")

def compute_shares(p, delta, alpha):
    """Compute logit market shares."""
    v = delta + alpha * p
    exp_v = np.exp(v)
    denom = 1 + np.sum(exp_v)
    s = exp_v / denom
    s0 = 1 / denom
    return s, s0

def compute_elasticities(p, s, alpha):
    """Compute own-price elasticity matrix."""
    J = len(p)
    eta = np.zeros((J, J))
    for j in range(J):
        for k in range(J):
            if j == k:
                eta[j, k] = alpha * p[j] * (1 - s[j])
            else:
                eta[j, k] = -alpha * p[k] * s[k]
    return eta

print("Q4(a): Market shares")
s0_pre, s00_pre = compute_shares(p0, delta, alpha)
print(f"  Product 1: s = {s0_pre[0]:.4f} ({s0_pre[0]*100:.2f}%)")
print(f"  Product 2: s = {s0_pre[1]:.4f} ({s0_pre[1]*100:.2f}%)")
print(f"  Product 3: s = {s0_pre[2]:.4f} ({s0_pre[2]*100:.2f}%)")
print(f"  Product 4: s = {s0_pre[3]:.4f} ({s0_pre[3]*100:.2f}%)")
print(f"  Outside:   s = {s00_pre:.4f} ({s00_pre*100:.2f}%)")
print(f"  Sum inside: {np.sum(s0_pre):.4f}")

print("\nQ4(b): Own-price elasticities")
eta_pre = compute_elasticities(p0, s0_pre, alpha)
for j in range(J):
    print(f"  Product {j+1}: eta = {eta_pre[j,j]:.4f}", end="")
    if abs(eta_pre[j,j]) > 1:
        print(" (elastic)")
    else:
        print(" (inelastic)")

print("\nQ4(c): Verify FOC for product 1")
# FOC: p - c = -s / (ds/dp) = 1 / (|alpha| * (1 - s))
markup_foc = 1 / (abs(alpha) * (1 - s0_pre[0]))
markup_actual = p0[0] - c[0]
print(f"  Actual markup (p - c): ${markup_actual:.4f}")
print(f"  FOC markup: ${markup_foc:.4f}")
print(f"  Difference: ${abs(markup_actual - markup_foc):.4f}")

print("\nQ4(d): HHI calculation")
# HHI = sum of (100 * share)^2, using inside shares only
s_inside = s0_pre / np.sum(s0_pre)  # Normalize to inside market
HHI = np.sum((100 * s_inside)**2)
print(f"  Inside market shares: {s_inside}")
print(f"  HHI = {HHI:.0f}")
if HHI < 1500:
    print("  Market is unconcentrated (HHI < 1500)")
elif HHI < 2500:
    print("  Market is moderately concentrated (1500 <= HHI < 2500)")
else:
    print("  Market is highly concentrated (HHI >= 2500)")

# -----------------------------------------------------------------------------
# Question 5: Post-Merger Prices
# -----------------------------------------------------------------------------
print("\n--- Question 5: Post-Merger Prices ---\n")

print("Q5(a): Ownership matrices")
O_pre = np.eye(J)  # Pre-merger: each firm owns one product
O_post = np.eye(J)
O_post[0, 1] = 1  # Firm 1 now owns product 2
O_post[1, 0] = 1  # Symmetric
print("  Pre-merger ownership matrix:")
print(O_pre.astype(int))
print("\n  Post-merger ownership matrix:")
print(O_post.astype(int))

print("\nQ5(b): Intuition for price increase")
print("""
  After the merger, the merged firm internalizes the substitution between
  products 1 and 2. Before the merger, if Firm 1 raised prices, some
  customers would switch to Product 2 (owned by Firm 2) - lost sales.

  After the merger, those "lost" customers are recaptured by Product 2,
  which the merged firm also owns. This "recapture" effect means the
  merged firm faces less elastic residual demand, so it raises prices.

  The price increase is larger when:
  - Products 1 and 2 are close substitutes (high cross-elasticity)
  - Pre-merger margins are higher
""")

print("\nQ5(c): Compute post-merger equilibrium prices")

def foc_system(p, delta, alpha, c, O):
    """
    FOC system for differentiated products oligopoly.
    s_j + sum_k O_jk * (p_k - c_k) * ds_k/dp_j = 0
    """
    s, _ = compute_shares(p, delta, alpha)
    J = len(p)
    foc = np.zeros(J)

    for j in range(J):
        foc[j] = s[j]
        for k in range(J):
            if O[j, k] == 1:
                if j == k:
                    ds_dp = alpha * s[k] * (1 - s[k])
                else:
                    ds_dp = -alpha * s[j] * s[k]
                foc[j] += (p[k] - c[k]) * ds_dp

    return foc

# Solve for post-merger prices
p_post = fsolve(foc_system, p0, args=(delta, alpha, c, O_post))

print(f"\n  Pre-merger prices:  {p0}")
print(f"  Post-merger prices: {np.round(p_post, 4)}")

print("\nQ5(d): Price changes")
dp = p_post - p0
for j in range(J):
    print(f"  Product {j+1}: ${p0[j]:.2f} -> ${p_post[j]:.2f} ({dp[j]:+.4f}, {dp[j]/p0[j]*100:+.2f}%)")

print("""
  Products 1 and 2 (merging firms) see price increases.
  Products 3 and 4 (non-merging) also see small price increases
  because they face less competitive pressure after the merger.
""")

# -----------------------------------------------------------------------------
# Question 6: Welfare Analysis
# -----------------------------------------------------------------------------
print("\n--- Question 6: Welfare Analysis ---\n")

def compute_cs(p, delta, alpha, M):
    """Compute total consumer surplus."""
    v = delta + alpha * p
    IV = np.log(1 + np.sum(np.exp(v)))
    CS_per_consumer = IV / abs(alpha)
    return CS_per_consumer * M

def compute_profits(p, c, s, M):
    """Compute profits for each product."""
    return (p - c) * s * M

print("Q6(a): Consumer surplus")
CS_pre = compute_cs(p0, delta, alpha, M)
CS_post = compute_cs(p_post, delta, alpha, M)
dCS = CS_post - CS_pre

print(f"  Pre-merger CS:  ${CS_pre:.2f}")
print(f"  Post-merger CS: ${CS_post:.2f}")
print(f"  Change in CS:   ${dCS:.2f} ({dCS/CS_pre*100:+.2f}%)")

print("\nQ6(b): Producer profits")
s_pre, _ = compute_shares(p0, delta, alpha)
s_post, _ = compute_shares(p_post, delta, alpha)

profits_pre = compute_profits(p0, c, s_pre, M)
profits_post = compute_profits(p_post, c, s_post, M)

print(f"  Pre-merger profits:")
for j in range(J):
    print(f"    Firm {j+1}: ${profits_pre[j]:.2f}")
print(f"    Total PS: ${np.sum(profits_pre):.2f}")

print(f"\n  Post-merger profits:")
print(f"    Merged firm (1+2): ${profits_post[0] + profits_post[1]:.2f}")
print(f"    Firm 3: ${profits_post[2]:.2f}")
print(f"    Firm 4: ${profits_post[3]:.2f}")
print(f"    Total PS: ${np.sum(profits_post):.2f}")

dPS = np.sum(profits_post) - np.sum(profits_pre)
merged_pre = profits_pre[0] + profits_pre[1]
merged_post = profits_post[0] + profits_post[1]

print(f"\n  Does merged firm benefit? Pre: ${merged_pre:.2f}, Post: ${merged_post:.2f}")
print(f"  Do non-merging firms benefit? Firm 3: ${profits_post[2] - profits_pre[2]:+.2f}, Firm 4: ${profits_post[3] - profits_pre[3]:+.2f}")

print("\nQ6(c): Total welfare")
TW_pre = CS_pre + np.sum(profits_pre)
TW_post = CS_post + np.sum(profits_post)
dTW = TW_post - TW_pre

print(f"  Pre-merger TW:  ${TW_pre:.2f}")
print(f"  Post-merger TW: ${TW_post:.2f}")
print(f"  Change in TW:   ${dTW:.2f} ({dTW/TW_pre*100:+.2f}%)")

if dTW < 0:
    print("\n  The merger is WELFARE-REDUCING.")
else:
    print("\n  The merger is WELFARE-IMPROVING.")

print("\nQ6(d): Efficiency defense (10% cost reduction)")
c_eff = c.copy()
c_eff[0] = 0.9   # 10% reduction
c_eff[1] = 1.08  # 10% reduction

p_post_eff = fsolve(foc_system, p0, args=(delta, alpha, c_eff, O_post))
s_post_eff, _ = compute_shares(p_post_eff, delta, alpha)

CS_post_eff = compute_cs(p_post_eff, delta, alpha, M)
profits_post_eff = compute_profits(p_post_eff, c_eff, s_post_eff, M)
TW_post_eff = CS_post_eff + np.sum(profits_post_eff)

print(f"  Post-merger prices with efficiencies: {np.round(p_post_eff, 4)}")
print(f"  Consumer surplus: ${CS_post_eff:.2f} (change: ${CS_post_eff - CS_pre:+.2f})")
print(f"  Total welfare: ${TW_post_eff:.2f} (change: ${TW_post_eff - TW_pre:+.2f})")

if TW_post_eff > TW_pre:
    print("\n  With efficiency gains, the merger becomes WELFARE-IMPROVING.")
    print("  The efficiency defense succeeds.")
else:
    print("\n  Even with efficiency gains, the merger is WELFARE-REDUCING.")
    print("  The efficiency defense fails.")

print("\n" + "="*70)
print("END OF SOLUTIONS")
print("="*70)
