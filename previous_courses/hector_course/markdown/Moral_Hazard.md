# Moral Hazard

*Converted from: Moral_Hazard.pdf*

---


## Page 1

ECN 532
Microeconomics II
Hector Chade
Second Quarter 2025


## Page 2

MORAL HAZARD AND INCENTIVE CONTRACTS


## Page 3

Lecture’s Objectives
First topic in information economics: moral hazard
Fundamental problem in many economic applications
We will deﬁne what moral hazard is and analyze its eﬀect
Methodology: principal-agent contracting problem
We will derive the following insights:
Crucial diﬀerence whether agent’s action is observable or not
Observable case: pure risk sharing problem, easy contract
Unobservable case: moral hazard, incentive contract
Moral hazard is costly for principal
Moral hazard leads to distortions in action agent takes


## Page 4

The Principal-Agent Problem


## Page 5

Motivation
Fundamental problem in Economics: moral hazard or hidden action
One party to a transaction takes an action that aﬀects the value of the
transaction to the other party, who cannot observe the action taken
Methodology: principal-agent problem with moral hazard
The principal oﬀers a contract to the agent, who has a known outside option if
she rejects the contract
If she accepts the contract, then she takes an action that is unobservable to
the principal and costly for the agent, and which aﬀects the principal’s payoﬀ
The principal can observe a random variable associated with the agent’s
action, and conditions the contract on that observation
Common interpretation of the random variable is output
Another interpretation: in insurance, signal is whether agent had an accident
Action often interpreted as eﬀort, but could be investment levels, projects, etc.


## Page 6

Historical Remarks
Historical accounts of insurance numerous, but not of moral hazard
Insurance literature recognized adverse selection but not moral hazard; ﬁrst
mention is in 1853 in ﬁre insurance
In the economics literature:
Adam Smith (1776): mentions incentive problem that separation of ownership
and management entails
Marshall (1890): mentions that having insurance may lead to carelessness
Haynes (1895): ﬁrst to use term moral hazard in insurance
Knight (1921): describes how moral hazard can limit size of organizations
First formal analysis: Arrow (1963) on health care, and Pauly (1968)
Current paradigm: Ross (1973), Mirrlees (1975), Shavell (1979), and mainly
Holmstrom (1979) and Grossman and Hart (1983)


## Page 7

The Model
A risk-neutral principal hires a strictly risk-averse agent to perform a task
Agent’s action/eﬀort a can be high, ah, or low, aℓ, unobservable to principal
Principal oﬀers contract based on a stochastic output x that depends on a
Principal maximizes expected proﬁts, that is, expected output minus
expected compensation to agent
Agent’s utility if wage is w and eﬀort is a is u(w) −c(a), where
u twice continuously diﬀerentiable with u′ > 0, u′′ < 0, unbounded below
0 = c(aℓ) < c(ah)
If the agent does not work for the principal, she can obtain a level of utility ¯u
in her next best alternative. We call ¯u the agent’s reservation utility
Agent maximizes expected utility using u(w) −c(a)


## Page 8

The Model
Output x can take value x1, x2, ..., xN with probability (given a)
P[x = xi|a] = πi(a) > 0, i = 1, 2, ..., N
Agent controls with her action a production function that is subject to shocks
Principal oﬀers a contract: compensation scheme (wages) w1, w2, ..., wN,
and a recommended action or eﬀort level a
After observing contract the agent accepts or rejects it
If she rejects the game ends and the agent obtains ¯u
If she accepts then the agent privately chooses a, a realization x obtains, the
corresponding wage is paid, and the game ends


## Page 9

The Model
The principal’s contracting problem is
max
w1,w2,...,wN,a
N
X
i=1
(xi −wi)πi(a)
s.t.
N
X
i=1
u(wi)πi(a) −c(a) ≥¯u
(P)
a solves
max
a′∈{aℓ.ah}
N
X
i=1
u(wi)πi(a′) −c(a′) (IC)
(P) is the participation constraint, (IC) the incentive constraint
Remarks:
Optimization problem of the principal depends on the optimization of the
agent at another level
Similar to Stackelberg problem (leader-follower)
In fact, solution here is the outcome of the SPE of principal-agent game


## Page 10

The Model
Questions we will address:
What determines the wages w1, w2, ..., wN?
The information contained in the output about the action taken by the agent
Is w1 ≤w2 ≤· · · ≤wN? (Higher output, higher wage)
We will provide suﬃcient conditions that ensure this property
Is the action a implemented distorted away from eﬃciency?
The answer is yes, so moral hazard has real eﬀects on the allocation of resources
What if in addition to x another signal y could be observed at no cost?
We will discuss why it is optimal to introduce y into the contract if informative


## Page 11

Methodology to Solve the Problem


## Page 12

Two-Step Methodology
The following methodology is similar to what we do in cost and production:
Step 1: Cost Minimization. For each a ∈{aℓ, ah}, solve
min
w1,w2,...,wN
N
X
i=1
wiπi(a)
subject to (P) and (IC). Denote the value C(a) (principal’s cost function)
Step 2: Proﬁt Maximization. Let B(a) = PN
i=1 xiπi(a) be the expected value
of output given action a, and solve
max{B(aℓ) −C(aℓ), B(ah) −C(ah)}
At the end of the second step we have the optimal contract, that is, the
compensation scheme and the recommended eﬀort
We will see that most of the insights come from Step 1


## Page 13

Observable Action Case


## Page 14

Observable Action Case
As a benchmark, assume a is observable, so there is no moral hazard
A contract is now a compensation scheme w1, w2, ..., wN and an enforceable
action a (since a is observable, its level can be contractually enforced)
The principal’s problem in this case is
max
w1,w2,...,wN,a
N
X
i=1
(xi −wi)πi(a)
s.t.
N
X
i=1
u(wi)πi(a) −c(a) ≥¯u
(P)
Unlike full problem with moral hazard, constraint (IC) is absent (why?)


## Page 15

Observable Action Case
First step: principal solves, for each a ∈{aℓ, ah}
min
w1,w2,...,wN
N
X
i=1
wiπi(a)
s.t.
N
X
i=1
u(wi)πi(a) −c(a) ≥¯u
(P)
We will see that the solution is very simple
We will ﬁrst derive it without calculus and then with calculus
Let us show that for each a, constraint (P) holds with equality
Assume at the optimum PN
i=1 u(wi)πi(a) −c(a) > ¯u
Let δ > 0 be the amount on the left side of the inequality
Let ˆwi be ˆwi = wi −ηi for all xi, where ηi > 0 solves u(wi −ηi) = u(wi) −δ
ˆw1, ˆw2, ..., ˆwN is strictly cheaper for principal, contradicting w1, ..., wN optimal


## Page 16

Observable Action Case
Second, let us show that wi solves u(wi) −c(a) = ¯u for each i, and so,
wi = u−1(¯u + c(a)) for every i, a constant wage
If wi is optimal but is not constant for every i, then the principal can instead
oﬀer the constant wage ˆw = PN
i=1 wiπi(a) and obtain same cost
But with ˆw = PN
i=1 wiπi(a), constraint (P) holds with strict inequality, since
u
 N
X
i=1
wiπi(a)
!
>
N
X
i=1
u(wi)πi(a) = ¯u + c(a)
where the strict inequality follows since for any strictly concave function g,
g(E[X]) > E[g(X)] (Jensen’s inequality), and the equality follows because we
are assuming that (w1, w2, ..., wN) is optimal, and thus (P) is binding
It follows now that the principal can do strictly better (reduce cost) with
another constant wage that is smaller, namely, ˜w = PN
i=1 wiπi(a) −ε, where
ε > 0 uniquely solve u(PN
i=1 wiπi(a) −ε) = ¯u + c(a)
Thus, ˜w = u−1(¯u + c(a)) strictly reduces expected cost, and thus the original
contract cannot be optimal


## Page 17

Observable Action Case
That the wage is constant is not surprising, since without moral hazard this is
just a risk sharing problem between a risk neutral party and a strictly risk
averse one, and full insurance obtains
The value of the problem for each action a is Co(a) = u−1(¯u + c(a))
Note that Co is strictly increasing in ¯u and a
In short, in the ﬁrst step we have shown the following (recall c(aℓ) = 0) :
If principal wants the agent to take a = aℓ, then oﬀer a contract that says “I
will pay you ˜w = u−1(¯u) and you will have to exert eﬀort level aℓ”
If principal wants the agent to take a = ah, then oﬀer a contract that says “I
will pay you ˜w = u−1(¯u + c(ah)) and you will have to exert eﬀort level ah”
In each case the agent is willing to accept the contract (why?)
In the second step, principal decides whether to induce aℓor ah depending on
max{B(aℓ) −Co(aℓ), B(ah) −Co(ah)}


## Page 18

Observable Action Case
As a consistency check, let us re-derive the optimal contract using calculus
Form the Lagrangian with a multiplier λ
L =
N
X
i=1
wiπi(a) + λ
 
¯u −
N
X
i=1
u(wi)πi(a) + c(a)
!
The FOC with respect to wi, i = 1, 2, ..., N is
πi(a) −λu′(wi)πi(a) = 0 ⇒
1
u′(wi) = λ, i = 1, 2, ..., N
We immediately obtain the following results:
u′ > 0 implies λ > 0, which implies that (P) must hold with equality
Since for every i,
1
u′(wi) is equal to the same constant, wi is constant for all i
But since (P) holds with equality and wi is constant in i (pays the same
amount for every xi observed, it follows that the only candidate for an optimal
compensation scheme given a is u( ˜w) = ¯u + c(a) or ˜w = u−1(¯u + c(a))
The rest of the analysis is now the same


## Page 19

Unobservable Action (Moral Hazard) Case


## Page 20

Unobservable Action Case
Henceforth action is unobservable, that is, there is moral hazard
Recall that a ∈{aℓ, ah}, aℓ< ah, with c(aℓ) = 0 < c(ah), and that the
principal’s problem is given by
max
w1,w2,...,wN,a
N
X
i=1
(xi −wi)πi(a)
s.t.
N
X
i=1
u(wi)πi(a) −c(a) ≥¯u
(P)
a solves
max
a′∈{aℓ.ah}
N
X
i=1
u(wi)πi(a′) −c(a′) (IC)
We are going to apply our two-step methodology to solve it


## Page 21

Unobservable Action Case
Let us solve the cost-minimization problem for each a
Cost-minimization problem trivial for a = aℓ:
If principal pays constant wage, then (IC) constraint holds with strict
inequality (why?)
Thus principal can oﬀer same wage from observable case
It follows that C(aℓ) = Co(aℓ) = u−1(¯u)


## Page 22

Unobservable Action Case
Things are much more diﬃcult but more interesting for a = ah
Principal solves
min
w1,w2,...,wN
N
X
i=1
wiπi(a)
s.t.
N
X
i=1
u(wi)πi(a) −c(a) ≥¯u
(P)
N
X
i=1
u(wi)πi(ah) −c(ah) ≥
N
X
i=1
u(wi)πi(aℓ) (IC)
Fundamental trade-oﬀin moral hazard: risk sharing versus incentives
For risk sharing, principal prefers constant wage, but this violates (IC)
For incentives, variability in wages is needed, which is costly to the principal


## Page 23

Unobservable Action Case
Let λ ≥0 be the multiplier of (P) and µ ≥0 of (IC)
Fact: If a multiplier is strictly positive the constraint holds with equality
The Lagrangian of the problem is
L=
N
X
i=1
wiπi(a) + λ
 
¯u −
N
X
i=1
u(wi)πi(a) + c(a)
!
+µ
 N
X
i=1
u(wi)πi(aℓ) −
 N
X
i=1
u(wi)πi(ah) −c(ah)
!!
The FOC with respect to wi, i = 1, 2, ..., N, is (check)
1
u′(wi) = λ + µ

1 −πi(aℓ)
πi(ah)

, i = 1, 2, ..., N
Note that λ > 0 and µ > 0 at the optimum
Multiplying by πi(ah) and adding yield λ = PN
i=1
1
u′(wi)πi(ah) > 0
If µ = 0, then
1
u′(wi) = λ for all i, and wi is constant in i, violating (IC)


## Page 24

Unobservable Action Case
There is an important economic insight emerging from FOC
1
u′(wi) = λ + µ

1 −πi(aℓ)
πi(ah)

, i = 1, 2, ..., N
Interpretation:
Wages vary in xi now, unlike observable case
wi paid when output is xi is pinned down by the likelihood ratio πi(ah)
πi(aℓ)
Likelihood ratio: information xi contains about agent taking ah instead of aℓ
Optimal compensation pays more when xi observed has a higher πi(ah)
πi(aℓ)
If πi(ah)
πi(aℓ) increases in i (called monotone likelihood ratio property, or MLRP),
then agent gets a higher wage when the output observed is higher (something
we commonly observe)
C(ah) > Co(ah) since wages vary: moral hazard strictly increases costs
To impose variability on agent’s compensation, that is, risk, principal must on
average pay the agent more for her to bear the risk


## Page 25

Unobservable Action Case
The second step is trivial: choose aℓor ah according to
max{B(aℓ) −C(aℓ), B(ah) −C(ah)}
Since C(aℓ) = Co(aℓ) and C(ah) > Co(ah), the action ah is implemented
“less often” under moral hazard
Cases with observable action with ah optimal but under moral hazard aℓis
Moral hazard distorts the optimal action downward in this case


## Page 26

Unobservable Action Case
Example
Assume u(w) = √w and N = 2 (two output levels)
To simplify notation, let π2(ah) = p, and π2(aℓ) = q, with p > q > 0
Note that in this case if v = u(w), then u−1(v) = v2
Observable case is easy: Co(aℓ) = (¯u)2 and Co(ah) = (¯u + c(ah))2
Since B(aℓ) = qx2 + (1 −q)x1 and B(ah) = px2 + (1 −p)x1, principal chooses
to implement aℓor ah depending on max{B(aℓ) −Co(¯u), B(ah) −Co(ah)}
In the moral hazard case, we know that C(aℓ) = Co(ah) = (¯u)2, since it is
enough to pay a constant wage w = (¯u)2


## Page 27

Unobservable Action Case
Continuation of the example:
The cost-minimizing contract when the principal wants to induce the agent to
exert high eﬀort ah solves
min
w1,w2(1 −p)w1 + pw2
s.t. (1 −p)√w1 + p√w2 −c(ah) ≥¯u
(1 −p)√w1 + p√w2 −c(ah) ≥(1 −q)√w1 + q√w2
When N = 2, solving this problem is easy since we know from above that
λ > 0 and µ > 0 and thus both constraints hold with equality by the “fact”
Let v1 = √w1 and v2 = √w2. Then (P)–(IC) with equality become (check)
(1 −p)v1 + pv2 = ¯u + c(ah)
−(p −q)v1 + (p −q)v2 = c(ah)
These are two linear equations in two unknowns, v1 and v2
We can solve them and then invert to obtain w1 and w2


## Page 28

Unobservable Action Case
Continuation of the example:
Solving the system yields (check)
v1 = ¯u + c(ah) −p
c
p −q
v2 = ¯u + c(ah) + (1 −p)
c
p −q
Note both utility levels cover outside option and disutility of eﬀort
But with moral hazard v1 is lowered by −p
c
p−q (a penalty), and v2 is raised by
(1 −p)
c
p−q (a bonus)
Since vi = √wi, we have wi = v2
i and thus wages and C(ah) are
w1 =

¯u + c(ah) −p
c
p −q
2
w2 =

¯u + c(ah) + (1 −p)
c
p −q
2
C(ah) = (1 −p)

¯u + c(ah) −p
c
p −q
2
+ p

¯u + c(ah) + (1 −p)
c
p −q
2


## Page 29

Unobservable Action Case
Continuation of the example:
Finally, the optimal contract solves max{B(aℓ) −C(aℓ), B(ah) −C(ah)}
If B(aℓ) −C(aℓ) > B(ah) −C(ah), then moral hazard is severe enough that
principal prefers to implement aℓat a constant wage
If B(ah) −C(ah) ≥B(aℓ) −C(aℓ), then the principal implements ah with the
contract derived above


## Page 30

Real-World Examples
Incentive contracts are ubiquitous, and at all levels of the organization:
CEO compensation: many items tied to proﬁts of the ﬁrm
Middle and lower level managers: bonuses tied to performance
Salespeople: commissions depend on level of sales
Factory workers: piece-rate contracts provide incentives to produce
Moral hazard is also pervasive in insurance markets
Policies with less than full insurance (e.g., deductibles) can be explained by
moral hazard: e.g., a driver has more incentives to drive carefully if they are
responsible for a signiﬁcant fraction of the repair
Similarly with the threat of increase in future premium upon an accident


## Page 31

Real-World Examples


## Page 32

Additional Signals: Suﬃcient Statistic Result
In many settings under moral hazard, in addition to x, the principal can
observe, at no cost, another signal y
Let y take values y1 < y2 < · · · < yK with some probability distribution
The main question is the following:
Should principal condition compensation on realization of x and y or just x?
The answer is simple and intuitive (suﬃcient statistic result):
If y provides information about the agent’s action, then it should be included
So wage paid should be w(x, y), e.g., if x = xi and y = yj, then wage is wij
By “information” we mean likelihood ratio
πij(ah)
πij(aℓ) is not independent of j
This result has many applications
CEO and stock options with industry-index strike price; salespeople and
information about state of demand; relative performance evaluation
In all these cases, there is an additional signal that is used in the contract
