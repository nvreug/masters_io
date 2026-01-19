# Mathematical Enhancements: Two-Part Tariffs and Merger Simulation

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add formal derivations for (1) two-part tariff optimization in L05, and (2) differentiated Bertrand as foundation for merger simulation in L10.

**Architecture:** Example first → Generalize to method. Show concrete worked examples, then explain the general approach.

**Tech Stack:** LaTeX/Beamer with amsmath for equations, existing slide template structure.

---

## Task 1: Add Two-Part Tariff Derivation to L05

**Files:**
- Modify: `/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/slides/lecture_05/lecture_05.tex`

**Step 1: Read current L05 structure**

Read the file to understand where to insert the new content. Look for the two-part tariff section.

**Step 2: Add worked example first (concrete before abstract)**

Insert a worked example slide before the formal derivation.

**NOTE:** Do NOT include "Take X minutes" on slides - professor will manage timing verbally.

```latex
\begin{frame}{Worked example: Two-part tariff}
	\begin{wideitemize}
		\item A gym has demand $q = 100 - 2p$ (visits per month)
		\item Marginal cost per visit: $c = 10$
		\item The gym charges a monthly membership fee $F$ plus per-visit fee $p$
		\item \textbf{Find:}
		\begin{wideenumerate}
			\item What per-visit price $p$ maximizes profit?
			\item What membership fee $F$ can the gym charge?
			\item What is total profit?
		\end{wideenumerate}
	\end{wideitemize}
\end{frame}

\begin{frame}{Worked example: Two-part tariff (solution)}
	\begin{solutionbox}[Solution]
		\begin{wideitemize}
			\item \textbf{(1)} Set $p^* = MC = 10$ (we'll see why!)
			\item \textbf{(2)} At $p = 10$: $q = 100 - 2(10) = 80$ visits
			\item Consumer surplus = area of triangle = $\frac{1}{2}(50 - 10)(80) = 1600$
			\item Set $F^* = CS = 1600$
			\item \textbf{(3)} $\pi = F + (p - c)q = 1600 + (10 - 10)(80) = 1600$
			\item \textbf{Compare to uniform pricing:}
			\item Monopoly: $MR = 50 - q = 10 \Rightarrow q = 40, p = 30$
			\item Monopoly profit: $(30 - 10)(40) = 800$
			\item Two-part tariff doubles profit!
		\end{wideitemize}
	\end{solutionbox}
\end{frame}
```

**Step 3: Add formal derivation (generalize from example)**

```latex
\begin{frame}{The general method: Two-part tariff optimization}
	\begin{wideitemize}
		\item Consumer has demand $q(p)$ and pays total $T = F + pq$
		\item \textbf{Step 1:} Consumer participates if surplus $\geq$ fee
		\begin{align*}
			CS(p) \geq F
		\end{align*}
		\item \textbf{Step 2:} Firm wants to extract maximum surplus
		\begin{align*}
			F^* = CS(p)
		\end{align*}
		\item \textbf{Step 3:} Firm's profit becomes
		\begin{align*}
			\pi = CS(p) + (p - c)q(p)
		\end{align*}
		\item This is total surplus! Firm captures everything.
	\end{wideitemize}
\end{frame}

\begin{frame}{Why price at marginal cost?}
	\begin{wideitemize}
		\item Firm profit = $CS(p) + (p - c)q(p)$ = Total surplus
		\item Total surplus is maximized at $p = c$ (no deadweight loss)
		\item \textbf{Intuition:}
		\begin{wideitemize}
			\vspace{5pt}
			\item High $p$: Earn margin on sales, but reduce $CS$ (and hence $F$)
			\item Low $p$: Lose margin, but $CS$ increases more
			\item Optimal: $p = c$, extract all surplus via $F$
		\end{wideitemize}
		\item \textbf{Result:} $p^* = c$, $F^* = CS(c)$, $\pi^* = CS(c)$
	\end{wideitemize}
\end{frame}

\begin{frame}{Deriving $p^* = c$ with calculus}
	\begin{wideitemize}
		\item For linear demand $q = a - bp$:
		\begin{align*}
			CS(p) = \frac{(a - bp)^2}{2b}
		\end{align*}
		\item Profit: $\pi = CS(p) + (p - c)(a - bp)$
		\item \textbf{FOC:}
		\begin{align*}
			\frac{d\pi}{dp} = \frac{dCS}{dp} + (a - bp) - b(p - c) = 0
		\end{align*}
		\item Since $\frac{dCS}{dp} = -(a - bp)$:
		\begin{align*}
			-(a - bp) + (a - bp) - b(p - c) = 0
		\end{align*}
		\item Simplifies to: $p^* = c$ $\checkmark$
	\end{wideitemize}
\end{frame}
```

**Step 4: Verify lecture compiles**

Run: `cd "/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/slides/lecture_05" && pdflatex -interaction=nonstopmode lecture_05.tex`

**Step 5: Commit**

```bash
git add slides/lecture_05/lecture_05.tex
git commit -m "feat(L05): Add two-part tariff derivation with worked example first"
```

---

## Task 2: Add Differentiated Bertrand Setup to L10

**Files:**
- Modify: `/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/slides/lecture_10/lecture_10.tex`

**Step 1: Read current L10 structure**

Read the file to understand where to insert the new content. Look for the merger simulation section.

**Step 2: Add differentiated Bertrand setup slides**

Insert after the intro/plan slides, before merger simulation content:

```latex
\begin{frame}{From demand estimation to merger analysis}
	\begin{wideitemize}
		\item In Part 1, we estimated demand systems like:
		\begin{align*}
			q_j = q_j(p_1, p_2, \ldots, p_J; x, \xi)
		\end{align*}
		\item Now: How do firms \textit{set} these prices?
		\item \textbf{Assumption:} Bertrand-Nash competition with differentiated products
		\item Each firm sets price to maximize profit, taking rivals' prices as given
		\item This gives us the \textbf{pricing equations} we need for merger simulation
	\end{wideitemize}
\end{frame}

\begin{frame}{Bertrand with differentiated products: setup}
	\begin{wideitemize}
		\item Two firms with differentiated products
		\item \textbf{Demand system:}
		\begin{align*}
			q_1 &= a - bp_1 + dp_2 \\
			q_2 &= a - bp_2 + dp_1
		\end{align*}
		\item $b > d > 0$: own-price effect dominates cross-price
		\item $d$ measures substitutability (higher $d$ = closer substitutes)
		\item Marginal cost: $c$ (symmetric for now)
	\end{wideitemize}
\end{frame}

\begin{frame}{Firm 1's pricing problem}
	\begin{wideitemize}
		\item Firm 1 maximizes profit taking $p_2$ as given:
		\begin{align*}
			\max_{p_1} \quad \pi_1 = (p_1 - c)(a - bp_1 + dp_2)
		\end{align*}
		\item \textbf{First-order condition:}
		\begin{align*}
			\frac{\partial \pi_1}{\partial p_1} = (a - bp_1 + dp_2) + (p_1 - c)(-b) = 0
		\end{align*}
		\item Rearranging for $p_1$:
		\begin{align*}
			a - bp_1 + dp_2 - bp_1 + bc = 0
		\end{align*}
		\begin{align*}
			p_1 = \frac{a + bc + dp_2}{2b}
		\end{align*}
	\end{wideitemize}
\end{frame}

\begin{frame}{Best response functions}
	\begin{wideitemize}
		\item \textbf{Firm 1's best response:}
		\begin{align*}
			p_1^{BR}(p_2) = \frac{a + bc + dp_2}{2b}
		\end{align*}
		\item \textbf{Firm 2's best response:} (by symmetry)
		\begin{align*}
			p_2^{BR}(p_1) = \frac{a + bc + dp_1}{2b}
		\end{align*}
		\item Note: Best responses are \textit{upward sloping}
		\item If rival raises price $\rightarrow$ I raise my price too
		\item This is \textbf{strategic complementarity} in prices
	\end{wideitemize}
\end{frame}

\begin{frame}{Pre-merger equilibrium}
	\begin{wideitemize}
		\item \textbf{Symmetric equilibrium:} $p_1^* = p_2^* = p^*$
		\item Substitute into best response:
		\begin{align*}
			p^* = \frac{a + bc + dp^*}{2b}
		\end{align*}
		\item Solving:
		\begin{align*}
			2bp^* - dp^* = a + bc \implies p^* = \frac{a + bc}{2b - d}
		\end{align*}
		\item \textbf{Markup:} $p^* - c = \frac{a + bc}{2b - d} - c = \frac{a - c(2b - d - b)}{2b - d} = \frac{a - bc + dc}{2b - d}$
		\item As $d \to b$: $p^* \to \infty$ (but model breaks down---products identical)
		\item As $d \to 0$: $p^* \to \frac{a + bc}{2b}$ (independent monopolists)
	\end{wideitemize}
\end{frame}
```

**Step 3: Verify lecture compiles**

Run: `cd "/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/slides/lecture_10" && pdflatex -interaction=nonstopmode lecture_10.tex`

**Step 4: Commit**

```bash
git add slides/lecture_10/lecture_10.tex
git commit -m "feat(L10): Add differentiated Bertrand setup with FOC derivation"
```

---

## Task 3: Add Merger Analysis Example

**Files:**
- Modify: `/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/slides/lecture_10/lecture_10.tex`

**Step 1: Add worked example (pre-merger)**

```latex
\begin{frame}{Worked example: Pre-merger pricing}
	\begin{wideitemize}
		\item Demand: $q_i = 100 - 2p_i + p_j$, Cost: $c = 20$
		\item So $a = 100$, $b = 2$, $d = 1$
		\item \textbf{Find:}
		\begin{wideenumerate}
			\item Each firm's best response function
			\item Pre-merger equilibrium price
			\item Each firm's quantity and profit
		\end{wideenumerate}
	\end{wideitemize}
\end{frame}

\begin{frame}{Worked example: Pre-merger pricing (solution)}
	\begin{solutionbox}[Solution]
		\begin{wideitemize}
			\item \textbf{(1)} $p_i^{BR} = \frac{100 + 2(20) + p_j}{2(2)} = \frac{140 + p_j}{4}$
			\item \textbf{(2)} Symmetric: $p^* = \frac{140 + p^*}{4}$
			\item $4p^* = 140 + p^* \Rightarrow 3p^* = 140 \Rightarrow p^* = 46.67$
			\item \textbf{(3)} $q^* = 100 - 2(46.67) + 46.67 = 53.33$
			\item $\pi^* = (46.67 - 20)(53.33) = 1,422$
		\end{wideitemize}
	\end{solutionbox}
\end{frame}
```

**Step 2: Add merger analysis**

```latex
\begin{frame}{What happens when firms 1 and 2 merge?}
	\begin{wideitemize}
		\item \textbf{Key change:} Merged firm now owns \textit{both} products
		\item Sets $p_1$ and $p_2$ to maximize \textit{joint} profit:
		\begin{align*}
			\max_{p_1, p_2} \quad \pi = (p_1 - c)q_1 + (p_2 - c)q_2
		\end{align*}
		\item \textbf{New FOC for $p_1$:}
		\begin{align*}
			\frac{\partial \pi}{\partial p_1} = q_1 + (p_1 - c)\frac{\partial q_1}{\partial p_1} + (p_2 - c)\frac{\partial q_2}{\partial p_1} = 0
		\end{align*}
		\item The new term $(p_2 - c)\frac{\partial q_2}{\partial p_1}$ captures \textbf{cannibalization}
		\item When I raise $p_1$, some customers switch to product 2 (which I also own!)
	\end{wideitemize}
\end{frame}

\begin{frame}{Merger internalizes substitution}
	\begin{wideitemize}
		\item Pre-merger: Raising $p_1$ loses customers to rival (bad)
		\item Post-merger: Some of those customers go to product 2 (mine!)
		\item \textbf{Result:} Less aggressive pricing $\rightarrow$ higher prices
		\item With symmetric products and costs:
		\begin{align*}
			\frac{\partial \pi}{\partial p_1} = (a - bp_1 + dp_2) - b(p_1 - c) + d(p_2 - c) = 0
		\end{align*}
		\item Symmetric equilibrium ($p_1 = p_2 = p^M$):
		\begin{align*}
			a - bp^M + dp^M - bp^M + bc + dp^M - dc = 0
		\end{align*}
		\begin{align*}
			p^M = \frac{a + bc - dc}{2b - 2d} = \frac{a + (b-d)c}{2(b - d)}
		\end{align*}
	\end{wideitemize}
\end{frame}

\begin{frame}{Worked example: Post-merger pricing}
	\begin{wideitemize}
		\item Same setup: $q_i = 100 - 2p_i + p_j$, $c = 20$
		\item \textbf{Find:}
		\begin{wideenumerate}
			\item Post-merger equilibrium price
			\item Post-merger quantity (per product)
			\item Post-merger profit (total for merged firm)
			\item Compare to pre-merger: Price change? Profit change?
		\end{wideenumerate}
	\end{wideitemize}
\end{frame}

\begin{frame}{Worked example: Post-merger pricing (solution)}
	\begin{solutionbox}[Solution]
		\begin{wideitemize}
			\item \textbf{(1)} $p^M = \frac{100 + (2-1)(20)}{2(2-1)} = \frac{100 + 20}{2} = 60$
			\item \textbf{(2)} $q^M = 100 - 2(60) + 60 = 40$
			\item \textbf{(3)} $\pi^{total} = 2 \times (60 - 20)(40) = 2 \times 1,600 = 3,200$
			\item \textbf{(4)} Comparison:
			\begin{center}
				\begin{tabular}{|l|c|c|}
					\hline
					& Pre-merger & Post-merger \\
					\hline
					Price & 46.67 & 60 \\
					Quantity (each) & 53.33 & 40 \\
					Profit (total) & 2,844 & 3,200 \\
					\hline
				\end{tabular}
			\end{center}
			\item Price up 29\%, quantity down 25\%, profit up 13\%
		\end{wideitemize}
	\end{solutionbox}
\end{frame}
```

**Step 3: Verify compile and commit**

```bash
git add slides/lecture_10/lecture_10.tex
git commit -m "feat(L10): Add merger example showing price increase from internalized substitution"
```

---

## Task 4: Generalize to Method (Cookbook)

**Files:**
- Modify: `/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/slides/lecture_10/lecture_10.tex`

**Step 1: Add slides generalizing to merger simulation method**

```latex
\begin{frame}{The general method: Merger simulation}
	\begin{wideitemize}
		\item What we just did \textit{is} merger simulation!
		\item \textbf{The cookbook:}
		\begin{wideenumerate}
			\item Estimate demand system (Part 1: own and cross-price elasticities)
			\item Assume Bertrand-Nash pricing
			\item Use FOCs to back out marginal costs from observed prices
			\item Re-solve FOCs with merged ownership structure
			\item Compare pre- and post-merger prices
		\end{wideenumerate}
		\item Steps 3-5 are what we just did by hand
		\item In practice: Use estimated demand, not assumed linear form
	\end{wideitemize}
\end{frame}

\begin{frame}{Why Bertrand with differentiated products?}
	\begin{wideitemize}
		\item \textbf{Contrast with Cournot:}
		\begin{wideitemize}
			\vspace{5pt}
			\item Cournot: Firms choose quantities, price clears market
			\item ``Merger paradox'': Mergers often unprofitable (rivals expand)
		\end{wideitemize}
		\item \textbf{Differentiated Bertrand:}
		\begin{wideitemize}
			\vspace{5pt}
			\item Firms choose prices, consumers choose products
			\item Mergers typically profitable (internalize substitution)
			\item Matches most retail/consumer goods markets
		\end{wideitemize}
		\item This is why antitrust authorities care about mergers!
		\item The question isn't ``is it profitable?'' (yes)
		\item The question is ``how much do prices rise?'' (consumer harm)
	\end{wideitemize}
\end{frame}

\begin{frame}{Connecting to demand estimation}
	\begin{wideitemize}
		\item The demand system $q_i = a - bp_i + dp_j$ is simple
		\item In Part 1, we estimated richer models:
		\begin{align*}
			u_{ij} = x_j\beta - \alpha p_j + \xi_j + \varepsilon_{ij}
		\end{align*}
		\item These give us the \textbf{elasticity matrix} we computed in pyblp
		\item Merger simulation uses those elasticities in the same FOCs
		\item \textbf{Key insight:} Demand estimation + Bertrand = Merger simulation
	\end{wideitemize}
\end{frame}

\begin{frame}{The pricing equation in practice}
	\begin{wideitemize}
		\item With $J$ products, the FOC for product $j$ owned by firm $f$:
		\begin{align*}
			q_j + \sum_{k \in \mathcal{F}_f} (p_k - c_k) \frac{\partial q_k}{\partial p_j} = 0
		\end{align*}
		\item $\mathcal{F}_f$ = set of products owned by firm $f$
		\item Pre-merger: Each firm owns one product
		\item Post-merger: Merged firm owns multiple products
		\item The sum captures cannibalization across owned products
		\item \textbf{HW2:} You'll implement this!
	\end{wideitemize}
\end{frame}
```

**Step 2: Verify compile and commit**

```bash
git add slides/lecture_10/lecture_10.tex
git commit -m "feat(L10): Add merger simulation cookbook connecting to demand estimation"
```

---

## Task 5: Update CLAUDE.md and Final Compile

**Files:**
- Modify: `/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/CLAUDE.md`

**Step 1: Add note about mathematical approach**

Find the Pedagogical Style section and add:

```markdown
*Mathematical Derivations*
- Use "example first, then generalize" approach
- Pattern: Concrete worked example → Solve step-by-step → Generalize to method
- Key derivations:
  - L05: Two-part tariff optimization (FOC shows p* = MC, F* = CS)
  - L10: Differentiated Bertrand → Merger simulation (connects demand estimation to competition policy)
```

**Step 2: Compile L05 and L10**

```bash
cd "/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/slides/lecture_05"
pdflatex -interaction=nonstopmode lecture_05.tex

cd "/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/slides/lecture_10"
pdflatex -interaction=nonstopmode lecture_10.tex
```

**Step 3: Final commit and push**

```bash
git add CLAUDE.md slides/lecture_05/lecture_05.tex slides/lecture_05/lecture_05.pdf slides/lecture_10/lecture_10.tex slides/lecture_10/lecture_10.pdf
git commit -m "feat(L05, L10): Add mathematical derivations for two-part tariffs and merger simulation

L05 - Two-part tariff optimization:
- Worked example (gym membership) with solution
- General method: participation constraint binds
- Calculus derivation: FOC shows p* = MC

L10 - Merger simulation foundation:
- Differentiated Bertrand setup with FOC derivation
- Pre/post-merger pricing examples
- Generalize to merger simulation cookbook
- Connect to demand estimation from Part 1

Update CLAUDE.md with mathematical approach notes"
git push
```

---

## Summary

This enhancement adds **two coherent units**:

### L05: Two-Part Tariff Optimization
1. **Worked example** (gym membership) - students solve first
2. **General method** - participation constraint binds, profit = total surplus
3. **Calculus derivation** - FOC shows p* = c

### L10: Merger Simulation Foundation
1. **Derives** differentiated Bertrand pricing from first principles
2. **Shows** a concrete merger example (prices rise, profits rise)
3. **Generalizes** to the merger simulation method
4. **Connects** to demand estimation from Part 1

**Exam question types enabled:**

| Topic | Question Type |
|-------|---------------|
| Two-part tariff | "Find optimal p and F given demand" |
| Two-part tariff | "Compare profit to uniform monopoly pricing" |
| Merger simulation | "Solve for pre-merger Bertrand equilibrium prices" |
| Merger simulation | "Calculate post-merger prices and compare" |
| Merger simulation | "Explain why mergers raise prices with differentiated products" |
