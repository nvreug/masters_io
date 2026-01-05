# Static Games Complete Info

*Converted from: Static_Games_Complete_Info.pdf*

---


## Page 1

ECN 532
Microeconomics II
Hector Chade
Second Quarter 2025


## Page 2

STATIC GAMES WITH COMPLETE INFORMATION


## Page 3

Lecture’s Objective
In this lecture we will start our coverage of game theory
After deﬁning game theory and what games are, we will
Deﬁne static games with complete information
Learn one way to represent games: the strategic or normal form of a game
Learn what a strategy is, and distinguish between pure and mixed strategies
Learn some solution concepts, including the fundamental Nash equilibrium


## Page 4

Notation
We will use the following notation:
Γ = (N, (Si)i∈N, (ui)i∈N) is a strategic-form game
Si is the set of (pure) strategies of player i
si ∈Si is a (pure) strategy of player i
S = ×n
i=1Si Cartesian product of Si’s
s = (s1, s2, ..., sn) ∈S is a (pure) strategy proﬁle
s = (si, s−i), s−i = (s1, s2, ..., si−1, si+1, ..., sn)
∆(Si) is the set of mixed strategies of player i
σi ∈∆(Si) is a mixed strategy of player i
σi(si) ≥0 and P
si∈Si σi(si) = 1
×n
i=1∆(Si) Cartesian product of ∆(Si)’s
σ = (σ1, σ2, ..., σn) ∈×n
i=1∆(Si) is a mixed strategy proﬁle
σ = (σi, σ−i), σ−i = (σ1, σ2, ..., σi−1, σi+1, ..., σn)
ui(si, s−i) utility of player i under (si, s−i)
ui(σi, σ−i) utility of player i under (σi, σ−i)


## Page 5

The Ground Rules of Game Theory


## Page 6

Preliminaries
What is game theory?
The study of models of conﬂict and cooperation among intelligent and rational
decision makers
Important: game theory is a mathematical tool
Fundamental in social sciences
Provides insight into many important economic applications
What is a game?
Any social situation involving two or more decision makers
Subsumes a broad class of problems across disciplines
What is a player?
The individuals involved in the game under consideration


## Page 7

Preliminaries
What is a rational decision maker?
One that makes decisions consistent with their objectives, that is, maximizes
utility or, if there is uncertainty, maximizes expected utility
What is an intelligent decision maker?
One that understands the situation under analysis as well as we do as analysts,
and thus can make the same inferences as we do
Remarks:
Example of setting with rational but not intelligent decision makers:
competitive equilibrium
Assumptions of game theory are strong, but avoids having agents that are
systematically fooled or that they make costly mistakes


## Page 8

Taxonomy of Games
A useful way to classify games is whether they are static or dynamic, and
whether they have complete or incomplete information
In a static game, players simultaneously and independently choose their
actions, and given the combination of actions chosen, each obtains a payoﬀ
In a dynamic game the strategic situation unfolds sequentially, and given the
players choices, at the end of the game each receives a payoﬀ
To deﬁne complete and incomplete information, we need the following:
An event is common knowledge if everyone knows the event, if everyone knows
that everyone knows the event, and so on ad-inﬁnitum


## Page 9

Taxonomy of Games
A game has complete information if the following items are common
knowledge among the players:
The actions available to every player
All the possible outcomes of the game, and how combinations of actions of all
the players aﬀect the outcome that obtains
The preferences of every player
In games of incomplete information at least one or more players have private
information about some of these features
We will thus study four classes of games:
Static games with complete information
Dynamic games with complete information
Static games with incomplete information
Dynamic games with incomplete information


## Page 10

Solution Concepts
Once we have represented a strategic situation as a game, we want to
analyze it and predict what will happen
For this purpose we will develop several solution concepts
Some criteria to evaluate solution concepts:
Existence: we want to make sure that a solution concept will actually deliver a
solution in a large class of games
Uniqueness: we would like a solution concept to restrict behavior, and ideally
deliver a unique solution, something we will see does not happen often
Sensitivity: a desirable feature of a solution concept is that its predictions are
robust to small changes in players’ payoﬀs
Welfare: does solution concept predict outcomes that are unimprovable
(Pareto optimal) for the players? We will see that often this is not the case


## Page 11

Strategic or Normal Representation of a Game


## Page 12

Strategic-Form Games
Recall that given a set A and a set B, the Cartesian product of these sets is
A × B, which consists of all the pairs (a, b) such that a ∈A and b ∈B
The Cartesian product of k sets A1, A2,...,Ak is ×k
i=1Ai
Positive orthant of R2 is R2
+ = R+ × R+, set of pairs (x, y) with x ≥0, y ≥0
Positive orthant of Rk is ×k
i=1Ri+, set of vectors (x1, ..., xk) with xi ≥0 all i
A strategic-form (normal-form) game Γ = (N, (Si)i∈N, (ui)i∈N) consists of
A set of players N = {1, 2, ..., n}
A set of strategies Si for each player i ∈N, where si denotes elements of Si
A utility function ui : S →R for each player i, where S = ×i∈NSi = ×n
i=1Si


## Page 13

Strategic-Form Games
This is a very useful and general way to represent games: it only requires the
analyst to specify players, strategies, and payoﬀs
It can be used to represent any game with complete information (we will see
how to adapt it to games with incomplete information)
It will be useful to introduce a piece of notation:
Consider player i and the strategy proﬁle is s = (s1, s2, ..., sn)
To isolate the role of player i, we will often denote s = (si, s−i)
Here si ∈Si, and s−i = (s1, s2, ..., si−1, si+1, ..., sn) ∈S−i = ×j̸=iSj
That is, s−i consists of strategies of all players except i, and similarly for S−i
We will use the notation “−i” repeatedly in the sequel


## Page 14

Example: Prisoner’s Dilemma
Two individuals have committed a serious crime and were apprehended
Police only has evidence to convict them for a lesser crime
They approach each of them separately with the following deal:
1. If you confess and incriminate your partner, then if your partner does not
confess, you go free and we convict your partner for the serious crime
2. If you do not confess and your partner does not either, then both will be
convicted for the lesser crime
3. If you confess and your partner confesses, then both are convicted for the
serious crime but with leniency for cooperation
4. If you do not confess and your partner confesses, then you will be convicted
for the serious crime and your partner goes free
Assume each individual cares only about their own welfare
It is clear that for each individual i, 1 ≻i 2 ≻i 3 ≻i 4


## Page 15

Example: Prisoner’s Dilemma
Let us denote confess by C and do not confess by M (for “to mum”)
We will assign some utility numbers that preserve the above ranking
Strategic-form representation:
Players: 1 and 2
Strategies: for player 1, C or M; for player 2, C or M
Payoﬀs: for player 1, u1(C, M) = 8, u1(M, M) = 5, u1(C, C) = 3, and
u1(M, C) = 0; for player 2, u2(C, M) = 0, u2(M, M) = 5, u2(C, C) = 3, and
u2(M, C) = 8
In matrix form
Player 2
M
C
Player 1
M
5, 5
0, 8
C
8, 0
3, 3


## Page 16

Example: Coordination Game
Consider the following game:
Individuals 1 and 2 want to coordinate on where to meet tonight
There is no way to communicate with each other
Both know that they prefer to be together tonight than apart
They both know that there are two events that they would like to attend:
opera (O), and ballet (B)
Each decides simultaneously and independently where to show up: O or B
Each obtains a payoﬀof 0 if they do not show up at the same event; player 1
obtains 2 and player 2 obtains 1 if they both show up at O; and player 1
obtains 1 and player 2 obtains 2 if they both show up at B


## Page 17

Example: Coordination Game
Strategic-form representation:
Players: 1 and 2
Strategies: for player 1, O or B; for player 2, O or B
Payoﬀs: for player 1, u1(O, O) = 2, u1(B, B) = 1, u1(O, B) = u1(B, O) = 0;
for player 2, u2(O, O) = 1, u2(B, B) = 2, u2(O, B) = u2(B, O) = 0
In matrix form
Player 2
O
B
Player 1
O
2, 1
0, 0
B
0, 0
1, 2


## Page 18

Example: Cournot Duopoly
There are two ﬁrms in the market, ﬁrm 1 and ﬁrm 2
Each sells the same product as the other one
The total cost of production of each ﬁrm is ci(qi) = q2
i , i = 1, 2
Total demand for the product is q = 100 −p, where q = q1 + q2
The ﬁrms compete as follows:
Simultaneously and independently, each chooses a quantity to produce
Then the demand determines the price per unit and the proﬁts for each ﬁrm
Firms seek to maximize proﬁts


## Page 19

Example: Cournot Duopoly
The strategic-form of this game is
Players: ﬁrm 1 and ﬁrm 2
Strategies: for ﬁrm 1, S1 = [0, ∞); for ﬁrm 2, s2 ∈S2 = [0, ∞) (si ∈Si is a
quantity qi of output)
Payoﬀs: for ﬁrm 1, u1(s1, s2) = (100 −s1 −s2)s1 −s2
1, for ﬁrm 2,
u2(s1, s2) = (100 −s1 −s2)s2 −s2
2
We cannot put it in matrix form since each ﬁrm has an inﬁnite strategy set


## Page 20

Example: Nash’s Demand Game
Two players, 1 and 2, bargain over the division of v dollars
They simultaneously and independently announce a share they would like to
have for themselves
If the sum of shares is less than v, then each gets the share they announce
If the sum of the shares is strictly bigger than v, then each one gets zero
Each player cares only about their share of v


## Page 21

Example: Nash’s Demand Game
The strategic-form of the game is as follows:
Players: player 1 and player 2
Strategies: for player 1, S1 = [0, v]; for player 2, S2 = [0, v] (si ∈Si is a the
share i announces)
Payoﬀs: for player i, i = 1, 2
ui(si, sj) =
(
si
if si + sj ≤v
0
if si + sj > v
We cannot put it in matrix form since each player has an inﬁnite strategy set


## Page 22

Pure and Mixed Strategies
In the examples Si was relatively simple
Finite set or inﬁnite set of scalars (e.g., quantities in Cournot duopoly)
But, in other games it can be a very complex object
For example, it could be a detailed contingent plan of choices, in which case
elements of Si will be complicated functions
In the examples, there was no uncertainty, but can easily be incorporated in
the payoﬀs of the deﬁnition of a strategic-form game
In the Cournot duopoly example, assume that the intercept of demand can be
100 or 200 with probabilities p and 1 −p
Assume both ﬁrms share this probability assessment and choose before
knowing the realization of the intercept
Then each ﬁrm maximizes expected proﬁts when choosing a quantity
Then the payoﬀui(s1, s2) is already the expected proﬁt of ﬁrm i


## Page 23

Pure and Mixed Strategies
So far we have assumed players choose a strategy in a non-random fashion
These strategies are called pure strategies
In prisoner’s dilemma each player either chooses confess or do not confess
In the Cournot duopoly each ﬁrm chooses a quantity
It is convenient in game theory to expand the notion of strategy and allow
players to add randomness to their choices if they want
For example, player i can ﬂip a coin or roll a die (or another randomizing
device) to determine what si they end up choosing among the elements in Si
These strategies are called mixed strategies, usually denoted with the letter σ
Given Si, let ∆(Si) be the set of probability distributions over strategies in Si
That is, σi ∈∆(Si), then σi(si) ≥0 for every si ∈Si and P
si∈Si σi(si) = 1
We denote by σ a strategy proﬁle (σ1, σ2, ..., σn) ∈×i∈N∆(Si)


## Page 24

Pure and Mixed Strategies
Remarks:
For a simple example, in the coordination game player i can choose O with
probability σi(O) ∈(0, 1) and B with probability 1 −σi(O)
A pure strategy for i is a special case of a mixed strategy that puts probability
one on a given si (e.g., choice of O is equivalent to choosing it with p = 1)
We will see that mixed strategies capture interesting behavior when players
want to avoid being predictable
We will see also that mixed strategies are technically important to ensure
existence of Nash equilibrium in a large class of games
If a player has 2 pure strategies, then a mixed strategy is summarized by one
number; if 3 by two numbers (check); if k by k −1 numbers (check)
What if i has an inﬁnite number of pure strategies as in Cournot duopoly?


## Page 25

Pure and Mixed Strategies
Recall the following concepts from probability theory:
Assume a random variable X takes on values on an interval [a, b]
The function F(x) = P[X ≤x] is cumulative distribution function (cdf) of X
F increasing in x, with limx→−∞F(x) = 0 and limx→∞F(x) = 1
In fact, F(b) = 1 and if F is continuous at x = a, then F(a) = 0
If F “has a probability density function” f (pdf), then F(x) =
R x
a f(τ)dτ; in
fact, in this case P[X ∈A] =
R
A f(τ)dτ, where A is any “well-behaved” set
In this case, it is common to say that “X is distributed with density f”


## Page 26

Pure and Mixed Strategies
x
fX(x)
x
F(x) = P[X ≤x] =
Z x
0
fX(τ) dτ
x
fX(x)
a
b
P[a < X < b] =
Z b
a
fX(τ) dτ


## Page 27

Pure and Mixed Strategies
Intuitively, if a player has an inﬁnite number of pure strategies that are real
numbers, we describe a mixed strategy by a cdf (or pdf if appropriate)
That is, σi can be represented by Fi(x) = P[si ≤x] or by fi(x) (recall that
fi is the derivative of Fi)
A mixed strategy for i is a probability distribution σi, but we can deﬁne a
random variable whose probability distribution is exactly σi
Example:
Consider the Cournot duopoly example
We saw that ﬁrm i can restrict attention to si ∈Si = [0, 100]
An example of a mixed strategy σi as a cdf is (draw the pdf)
Fi(x) =







0
if x < 20
x−20
40
if x ∈[20, 60]
1
if x > 60


## Page 28

Pure and Mixed Strategies
Assume that players play the mixed strategy proﬁle σ = (σ1, σ2, ..., σn), so
each i chooses σi simultaneously and independently from other players
How do we calculate player i’s payoﬀ? (Recall the notation “−i”)
Recall that if X and Y are independent random variables, each with
probability distribution PX and PY , then joint probability distribution PX,Y is
PX,Y [X = x, Y = y] = PX[X = x]PY [Y = y]
Note that in under σ, each s = (s1, s2, ..., sn) is chosen with probability
σ(s) = σ1(s1)σ2(s2)...σn(sn) =
n
Y
i=1
σi(si)
Then player i’s payoﬀui(σ) is given by expected utility
ui(σi, σ−i)=
X
s∈S
 n
Y
i=1
σi(si)
!
ui(s)
=
X
si∈Si
X
s−i∈S−i
σi(si)σ−i(s−i)ui(si, s−i) =
X
si∈Si
σi(si)ui(si, σ−i)


## Page 29

Pure and Mixed Strategies
Example:
In the coordination game, assume each player uses
σi = (σi(O), σi(B)) =
1
5, 4
5

Let us calculate the expected payoﬀof each player i = 1, 2
u1(σ1, σ2) = 1
5 × 1
5 × 2 + 1
5 × 4
5 × 0 + 4
5 × 1
5 × 0 + 4
5 × 4
5 × 1 = 18
25
u2(σ1, σ2) = 1
5 × 1
5 × 1 + 1
5 × 4
5 × 0 + 4
5 × 1
5 × 0 + 4
5 × 4
5 × 2 = 33
25
Player 2
O
B
Player 1
O
2, 1
0, 0
B
0, 0
1, 2


## Page 30

Pure and Mixed Strategies
In games with inﬁnite number of strategies, we replace sums with integrals
Example:
Consider Cournot duopoly and assume each player uses mixed strategy above
Then the expected proﬁts for each ﬁrm are (check)
u1(σ1, σ2) =
Z 60
20
Z 60
20
 (100 −s1 −s2)s1 −s2
1
 1
40
1
40ds1ds2 = −3, 200
3
u2(σ1, σ2) =
Z 60
20
Z 60
20
 (100 −s1 −s2)s2 −s2
2
 1
40
1
40ds1ds2 = −3, 200
3
To calculate the expected proﬁts in this case, all you need to remember is
Z b
a
xndx = xn+1
n + 1
b
a = bn+1
n + 1 −an+1
n + 1
and then ﬁrst solve for the integral with respect to s1 and then integrate the
resulting expression with respect to s2 (do it)


## Page 31

Dominance and Rationalizability


## Page 32

Introduction
Thus far we have learned
Ground rules of game theory (rationality, intelligence, common knowledge)
The diﬀerent classes of games that we will cover
Strategic-form (or normal-form) representation of games
We will now turn to solution concepts
Predictions about what will happen in a strategic situation
We will start with two solution concepts:
Iterated dominance and rationalizability
They study implications of rationality and common knowledge of rationality


## Page 33

Dominance
Let us start with a deﬁnition:
Let σi ∈∆(Si) and s′
i ∈Si be strategies for player i
s′
i is strictly dominated by σi if ui(σi, s−i) > ui(s′
i, s−i) for every s−i ∈S−i
If σi(si) = 1, then s′
i is strictly dominated by the pure strategy si
A strategy is strictly dominated for i if there is an alternative strategy that
yields strictly more utility to i no matter what the other players choose
The following result follows immediately from the deﬁnition:
A rational player will never choose a strictly dominated strategy
To see this, note that if a player chose a strictly dominated strategy, then
they would not be maximizing their payoﬀ
This is because the player has at least an alternative strategy that yields
uniformly strictly higher payoﬀs


## Page 34

Dominance
Example:
Consider the prisoner’s dilemma
Note that M is strictly dominated by C for player 1
To see this, apply the deﬁnition: if 2 plays M, then the best for 1 is to play C,
and if 2 plays C, then the best for 1 is to play C
No matter what 2 chooses, C yields a strictly higher payoﬀthan M for 1
The same holds for player 2 (check)
Hence, rational players play C in this game, and the prediction is (C, C)
Player 2
M
C
Player 1
M
5, 5
0, 8
C
8, 0
3, 3


## Page 35

Dominance
Example:
In the strategic-form game below, no strategy for either player is strictly
dominated by another pure strategy (check)
But, note that player 2 will not play R if player 1 plays either A or B (check)
We will show that R is strictly dominated by a mixed strategy
σ2 = (σ2(L), σ2(M), σ2(R)) = (p, 1 −p, 0)
From deﬁnition, must show u2(A, σ2) > u2(A, R) and u2(B, σ2) > u2(B, R)
This is the same as 3p > 1 or p > 1
3, and 4(1 −p) > 1 or p < 3
4
Hence, R is strictly dominated by σ2 with any p such that 1
3 < p < 3
4
Player 2
L
M
R
Player 1
A
4, 3
0, 0
2, 1
B
0, 0
3, 4
1, 1


## Page 36

Dominance
In the prisoner’s dilemma, since there are only two pure strategies and M is
strictly dominated by C, it follows that C is a dominant strategy
Let us deﬁne this formally:
A strategy si for player i is a strictly dominant strategy if for every s′
i ∈Si
with s′
i ̸= si, and for every s−i ∈S−i, ui(si, s−i) > ui(s′
i, s−i)
The following result follows immediately from the deﬁnition:
A rational player will always choose a strictly dominant strategy
If every player i has a strictly dominant strategy sd
i , then players’ rationality
predicts the strategy proﬁle (sd
1, sd
2, ..., sd
n) as the outcome of the game
If strictly dominant strategy proﬁle exists, it is unique and robust to small
changes in payoﬀs, but may not be Pareto optimal (e.g., prisoner’s dilemma)
In most economic applications players do not have strictly dominant strategies
(e.g., coordination game), so this solution concept is not powerful enough


## Page 37

Iterated Dominance
Rationality implies that players will not use a strictly dominated strategy
We will now use common knowledge of rationality to develop a solution
concept based on strictly dominated strategies
The basic idea is that rationality and common knowledge of rationality allow
us to remove strictly dominated strategies iteratively
Let us explain this ﬁrst with a simple example:
Note that in this game C is strictly dominated by R for player 2
Thus, rational player 2 will not play C
Player 2
L
C
R
Player 1
U
4, 3
5, 1
6, 2
M
2, 1
8, 4
3, 6
D
3, 0
9, 6
2, 8


## Page 38

Iterated Dominance
Since rationality is common knowledge, both know that 2 will not play C
In more detail:
Player 2 is rational and does not play C; player 1 knows player 2 is rational
and does not play C; player 2 knows that player 1 knows that player 2 is
rational and does not play C
Hence, we can eliminate C from the analysis of the game
Player 2
L
R
Player 1
U
4, 3
6, 2
M
2, 1
3, 6
D
3, 0
2, 8


## Page 39

Iterated Dominance
Now D is strictly dominated by U and M is strictly dominated by U for 1
Hence, player 1 will not play D or M
Since rationality is common knowledge, both know 1 will not play D or M
Hence, we can delete these strategies from the game to obtain
Player 2
L
R
Player 1
U
4, 3
6, 2


## Page 40

Iterated Dominance
But now R is strictly dominated by L for player 2
Hence, the only strategy proﬁle that survives the iterated elimination of
strictly dominated strategies is (U, L), and this is our prediction
Remarks:
In most games, a unique prediction will not obtain (e.g., coordination game),
but still a useful concept since often it reduces complexity of the game
Note that this concept just uses rationality and common knowledge of
rationality (although the latter is quite strong)


## Page 41

Iterated Dominance
Let us see another example:
No pure strategy is strictly dominated by another pure strategy for any of the
two players (check)
But R is strictly dominated by σ2 = (σ2(L), σ2(C), σ2(R)) = (p, 1 −p, 0)
To see this, note that u2(A, σ2) = p10 > 3 = u2(A, R) if and only if p >
3
10
Also, u2(B, σ2) = (1 −p)10 > 3 = u2(B, R) if and only if p <
7
10
Hence, σ2 strictly dominates R so long as
3
10 < p <
7
10
Player 2
L
M
R
Player 1
A
4, 10
3, 0
1, 3
B
0, 0
2, 10
10, 3


## Page 42

Iterated Dominance
Since player 2 is rational, they will not choose R
Common knowledge of rationality implies we can eliminate R from the game
But, now B is strictly dominated by A for player 1
Thus, player 1 will not choose B, and common knowledge of rationality
implies we can eliminate it from the game
Now M is strictly dominated by L, and reasoning as before, we eliminate M
Hence, the prediction is (A, L)
Player 2
L
M
Player 1
A
4, 10
3, 0
B
0, 0
2, 10


## Page 43

Iterated Dominance
An example with an inﬁnite number of strategies:
Cournot duopoly game with linear costs c(si) = 10si
Each ﬁrm solves maxsi(100 −si −sj)si −10si, i = 1, 2, j ̸= i
FOC is (check) s1 = 90−s2
2
, s2 = 90−s1
2
No ﬁrm will choose a quantity strictly larger than 45
Why? Because if s2 = 0, then s1 = 45, and if s1 = 0, then s2 = 45
Thus, every quantity strictly above 45 is strictly dominated for each ﬁrm, and
reasoning as above, can be eliminated from the game
No ﬁrm will choose a quantity strictly smaller than 22.5
Why? Because if s2 = 45, then s1 = 22.5, and if s1 = 45, then s2 = 22.5
Thus, we can eliminate all quantities below 22.5 for each ﬁrm
After two rounds of elimination of strictly dominated strategies we know that
only relevant quantities are 22.5 < si < 45, i = 1, 2


## Page 44

Iterated Dominance
After an inﬁnite number of rounds, the only strategy proﬁle that survives the
iterated elimination of strictly dominated strategies is (s1, s2) = (30, 30)
Suppose not, and suppose there is an interval [smin, smax] that survives
Then smin and smax satisfy the following equations:
smax = 90 −smin
2
, and smin = 90 −smax
2
But, the unique solution to these two equations is smin = smax = 30
In short, the solution concept of iterated elimination of strictly dominated
strategies yields a unique prediction in Cournot duopoly game
A picture of the two equations illustrates this process of elimination


## Page 45

Iterated Dominance
How do we deﬁne iterated elimination of strictly dominated strategies?
Suppose for each player i and each t = 1, 2, ..., T, there is a set of strategies
Xt
i such that
X1
i = Si (we start with the set of all strategies of i)
Xt+1
i
is a subset of Xt
i (at each stage we may eliminate some strategies)
For t = 1, ..., T −1 and for each player every strategy in Xt
i but not in Xt+1
i
is strictly dominated in the game in which the set of strategies of player j ̸= i
is Xt
j, and so we eliminated them
No strategy in XT
i is strictly dominated in the game in which the set of
strategies of j ̸= i is XT
j
Then the set of strategy proﬁles s = (s1, s2, ..., sn) such that si ∈XT
i for
every player survives the iterated elimination of strictly dominated strategies


## Page 46

Iterated Dominance
Remarks:
In games with inﬁnite strategies T can be inﬁnity
The order in which strategies are eliminated is irrelevant
For this solution concept, existence is guaranteed, and similarly with
robustness to small changes in payoﬀs (since dominance is strict)
But uniqueness does not hold (e.g., coordination game), and Pareto optimality
does not hold either (e.g., prisoner’s dilemma)


## Page 47

Rationalizability
We used above rationality and common knowledge of rationality to
Eliminate the strictly dominated strategies for each player (rationality)
Proceed iteratively to eliminate strictly dominated strategies (common
knowledge of rationality)
The analysis focused on eliminating all those strategies that are not going to
be played if players are rational and their rationality is common knowledge
This generated a prediction: a set of strategies for each player that survive
the iterated elimination of strictly dominated strategies
In some cases, only one strategy proﬁle survives and this is our prediction


## Page 48

Rationalizability
We will now focus on a related question:
If players are rational and rationality is common knowledge, what are the
strategy proﬁles may be played in a game?
Answer: only strategies for each player that are rationalizable strategies
The loose idea is that in with rationalizable strategies, each player can justify
their strategy choice by some conjecture they have about what other players
would do, which in turn is justiﬁed by what other players think that the player
under consideration would do, etc.
One can show the following results:
With just two players, the set of rationalizable strategies for each player is the
same as the set that survives the elimination of strictly dominated strategies
With more than two, set of rationalizable strategies can be a strict subset


## Page 49

Rationalizability
We will need the following important concept:
σi is a best response for player i when other players choose σ−i if
ui(σi, σ−i) ≥ui(σ′
i, σ−i), for all σ′
i ∈∆(Si)
σi is never a best response if there is no σ−i such that σi is a best response
In words:
A strategy is a best response against the strategies chosen by other players if
it yields as much expected utility as any other strategy of i
A strategy is never a best response if there is no conjecture a player can have
about what others are choosing that will make it a best response
Intuitively, strategies that are never a best response are not going to be
played, whereas those that are a best response against some strategy of other
players are can be part of the set of rationalizable strategies
If a strategy is strictly dominated, then it is never a best response (check)


## Page 50

Rationalizability
We can iteratively delete strategies that are never a best response
As with strictly dominated strategies, order of elimination does not matter
Set of strategies that survives is the rationalizable strategies of each player
These are strategies that a player can justify or rationalize by some conjecture
about other players choosing strategies that are best response to some
conjecture they have about other players that choose strategies that are best
response to some conjecture...and so on
Under weak conditions, each player has at least one rationalizable strategy
But there could be many of them (e.g., coordination game)


## Page 51

Rationalizability
Consider the following example:
In the ﬁrst round we can eliminate B4
It is strictly dominated by σ2 = (0.5, 0, 0.5, 0)
A strictly dominated strategy is never a best response
In the second round, we can eliminate A4
It is strictly dominated by A2
Player 2
B1
B2
B3
B4
Player 1
A1
0, 7
2, 5
7, 0
0, 1
A2
5, 2
3, 3
5, 2
0, 1
A3
7, 0
2, 5
0, 7
0, 1
A4
0, 0
0, −2
0, 0
10, −1


## Page 52

No more strategies can be eliminated
Rationalizable strategies: A1, A2, A3 for 1 and B1, B2, B3 for 2
A1 is a best response to B3, A2 to B2, and A3 to B1
B1 is a best response to A1, B2 to A2, and B3 to A3
Any of the nine strategy proﬁles may be played, since for each strategy a
player can provide a reasonable justiﬁcation for choosing it
Player 2
B1
B2
B3
B4
Player 1
A1
0, 7
2, 5
7, 0
0, 1
A2
5, 2
3, 3
5, 2
0, 1
A3
7, 0
2, 5
0, 7
0, 1
A4
0, 0
0, −2
0, 0
10, −1


## Page 53

Rationalizability
Player 1 can justify choosing A2 by the conjecture that player 2 will choose
B2, which player 1 can justify by the conjecture that player 2 thinks that 1
will choose A2, which is reasonable if 1 thinks that 2 is thinking that player 1
thinks that 2 will play B2, and so on ad inﬁnitum
Player 1 can justify choosing A1 with the conjecture that player 2 will choose
B3, which player 1 can justify by the conjecture that player 2 thinks that
player 1 will choose A3, which is reasonable if 1 thinks that 2 is thinking that
1 things that 2 will play B1, and so on ad inﬁnitum
Player 2
B1
B2
B3
B4
Player 1
A1
0, 7
2, 5
7, 0
0, 1
A2
5, 2
3, 3
5, 2
0, 1
A3
7, 0
2, 5
0, 7
0, 1
A4
0, 0
0, −2
0, 0
10, −1


## Page 54

Rationalizability
As another example, consider the coordination game:
Note that no player has a never a best response strategy (why?)
Note that each strategy of each player is rationalizable (check)
Thus, any of the four strategy proﬁles can emerge as a prediction (how?)
Player 2
O
B
Player 1
O
2, 1
0, 0
B
0, 0
1, 2


## Page 55

Rationalizability
Remarks:
This is as far as rationality and common knowledge of rationality take us
Sometimes (prisoner’s dilemma, Cournot duopoly) we obtain single prediction
But in general there are multiple ones and sometimes anything goes
Still they are useful concepts since can reduce complexity
Also, for games players play for the ﬁrst time rationalizability articulates the
strategic uncertainty in players’ minds
Note that existence holds, uniqueness does not (e.g., the two examples above),
sensitivity does, and Pareto optimality does not (e.g., prisoner’s dilemma)
To narrow our predictions further, we turn to solution concepts that impose
equilibrium requirements


## Page 56

Nash Equilibrium


## Page 57

Nash Equilibrium in Pure Strategies
We now turn to the most fundamental solution concept: Nash Equilibrium
To acquire some practice, we will ﬁrst deﬁne it just in terms of pure
strategies, solve some examples, and then extend it to mixed strategies
A strategy proﬁle s = (s1, s2, ..., sn) is a Nash equilibrium (in pure strategies)
of Γ = (N, (Si)i∈N, (ui)i∈N) if for every player i = 1, 2, ..., n and every
strategy s′
i ∈Si, we have ui(si, s−i) ≥ui(s′
i, s−i)
In words:
A strategy proﬁle is a Nash equilibrium (NE) if each player is choosing a best
response to the strategies chosen by other players
Players have a conjecture about what other players are choosing, and the
conjecture is correct
Rationalizability required that each player had a reasonable conjecture about
other players’s choices
NE demands that these conjectures are correct


## Page 58

Nash Equilibrium in Pure Strategies
Example: prisoner’s dilemma
Use deﬁnition to search for NE: there are 4 strategy proﬁles to check
Is (M, M) a NE? No, because at least one player has incentives to deviate (M
is not a best response to M)
Is (M, C) a NE? No, player 1 is not playing a best response to C by player 2
Is (C, M) a NE? No, player 2 is not playing a best response to C by player 1
Is (C, C) a NE? Yes, playing C is a best response to C for each player
NE predicts that both players will choose C
Player 2
M
C
Player 1
M
5, 5
0, 8
C
8, 0
3, 3


## Page 59

Nash Equilibrium in Pure Strategies
Example:
Find the NE in the following game
Player 2
L
C
R
Player 1
U
4, 3
5, 1
6, 2
M
2, 1
8, 4
3, 6
D
3, 0
9, 6
2, 8


## Page 60

Nash Equilibrium in Pure Strategies
Example: Cournot duopoly
Cournot duopoly game with linear costs c(si) = 10si
Each ﬁrm solves maxsi(100 −si −sj)si −10si, i = 1, 2, j ̸= i
FOC is (check) s1 = 90−s2
2
, s2 = 90−s1
2
Note what each equation means: it pins down the best response quantity for
each ﬁrm given what the other ﬁrm is producing
To be a NE, we need both ﬁrms choosing a best response
But this is the same as solving both equations simultaneously
Hence, NE is (s1, s2) = (30, 30)


## Page 61

Nash Equilibrium in Pure Strategies
Solved the examples by iterated elimination of strictly dominated strategies
The same prediction obtains with NE solution concept
Is this a coincidence? No
If a unique strategy proﬁle survives the iterated elimination of strictly
dominated strategies, then that strategy proﬁle is a NE (proof?)
If each player has a strictly dominant strategy, then the resulting strategy
proﬁle is a NE (proof?)
If after removing iteratively all the strategies that are never a best response
each player has a unique rationalizable strategy, then the resulting strategy
proﬁle is a NE (proof?)
Iterated dominance and rationalizability never eliminate a NE


## Page 62

Nash Equilibrium in Pure Strategies
Example: Coordination Game
Using the deﬁnition, it is clear that there are two Nash equilibria
(O, O) is a Nash equilibrium: If player 1 thinks player 2 will choose O, then
the best response for player 1 is to choose O; and if for player 2 thinks that
player 1 will choose O, the best response for player 2 is to choose O
(B, B) is a Nash equilibrium: If player 1 thinks player 2 will choose B, then
the best response for player 1 is to choose B, and similarly for player 2
Neither (O, B) nor (B, O) is a Nash equilibrium
Player 2
O
B
Player 1
O
2, 1
0, 0
B
0, 0
1, 2


## Page 63

Nash Equilibrium in Pure Strategies
Example: Nash’s demand game
Player 1 and player 2
Strategies: for player 1, S1 = [0, v]; for player 2, S2 = [0, v] (si ∈Si is a the
share i announces)
Payoﬀs: for player i, i = 1, 2
ui(si, sj) =
(
si
if si + sj ≤v
0
if si + sj > v
We claim that any (s1, s2) such that s1 + s2 = v is a Nash equilibrium
If player 1 conjectures that player 2 will choose s2 < v, then it is a unique best
response to choose s1 = v −s2 (why?), and similarly for player 2 if the
conjecture is that player 1 will choose s1 < v. If 1 conjectures s2 = v, then a
best response is s1 = 0, and similarly for 2, completing the proof of claim
There are other Nash equilibria (check)


## Page 64

Nash Equilibrium in Pure Strategies
Remarks:
Although there can be multiple Nash equilibria, note that “correct
conjectures” signiﬁcantly narrow set of predictions
Why would players play a Nash equilibrium?
If there is an obvious way to play the game, then that obvious way must be a
strategy proﬁle that is a Nash equilibrium (common conception of the game
and how it is played)
Pre-play communication: if players can engage in pre-play discussions, then if
they reach an agreement it better be that it is a Nash equilibrium of the game
Learning: under some conditions, if players play the same game over time,
then learning process settled on a strategy proﬁle that is a Nash equilibrium


## Page 65

Nash Equilibrium in Mixed Strategies
Every example we have seen has is at least one NE in pure strategies
But, consider the following simple example, known as matching pennies
(H, H) is not NE since player 1 prefers to choose T instead of H
(H, T) is not NE since player 2 prefers to choose H instead of H
(T, H) is not NE since player 1 prefers to choose T instead of H
(T, T) is not NE since player 2 prefers to choose H instead of T
Hence, there is no NE in pure strategies
We will show below that there is a unique NE but in mixed strategies
Player 2
H
T
Player 1
H
−1, 1
1, −1
T
1, −1
−1, 1


## Page 66

Nash Equilibrium in Mixed Strategies
Let us extend the notion of NE to mixed strategies
σ = (σ1, σ2, ..., σn) is a mixed strategy NE of Γ = (N, (Si)i∈N, (ui)i∈N) if for
every i = 1, 2, ..., n and every σ′
i ∈∆(Si), we have ui(σi, σ−i) ≥ui(σ′
i, σ−i)
It is the same deﬁnition as before but replacing pure by mixed strategies
Hard to check i does not have incentives to choose another mixed strategy
Fortunately, the following result shows that it is enough to consider
deviations to pure strategy
Let S+
i the set of strategies that player i plays with strictly positive probability
in σ = (σ1, σ2, ..., σn). Then σ is a mixed strategy NE if and only if for every
i = 1, 2, ..., n the following conditions hold:
ui(si, σ−i)= ui(s′
i, σ−i), for all si, s′
i ∈S+
i
ui(si, σ−i)≥ui(s′
i, σ−i), for all si ∈S+
i and s′
i /∈S+
i


## Page 67

Nash Equilibrium in Mixed Strategies
In words, this says that all the pure strategies that i plays with strictly
positive probability under σi yield exactly the same utility against σ−i, and
those play with zero probability yield a weakly lower payoﬀthat those played
with strictly positive probability against σ−i
Let us prove that these conditions are necessary (check suﬃciency)
We will show that if σ is a mixed strategy NE, then these two conditions hold
To see this, if either is violated, then there is si ∈S+
i and s′
i ∈Si such that
ui(s′
i, σ−i) > ui(si, σ−i)
But then, player i can increase their payoﬀstrictly against σ−i by playing s′
i
whenever they before played si
An implication of this result is that s = (s1, s2, ..., sn) is a pure strategy NE
if and only if it is a mixed strategy NE in which σi puts probability one on si
for every player i (why?)


## Page 68

Nash Equilibrium in Mixed Strategies
Example: Matching pennies
Let σ1 = (σ1(H), σ1(T)) = (p, 1 −p) and σ2 = (σ2(H), σ2(T)) = (q, 1 −q)
We want to ﬁnd values of p and q that will make (σ1, σ2) a mixed strategy NE
Use result above: to be a mixed strategy NE, it must satisfy for player 1
u1(H, σ2) = u1(T, σ2) ⇒q(−1) + (1 −q)1 = q1 + (1 −q)(−1) ⇒q = 0.5
and it must satisfy for player 2
u2(H, σ1) = u2(T, σ1) ⇒p1 + (1 −p)(−1) = p(−1) + (1 −p)1 ⇒p = 0.5
Thus, the mixed strategy NE is (σ1, σ2) = ((0.5, 0.5), (0.5, 0.5)), and each
player gets expected payoﬀof 0
Player 2
H
T
Player 1
H
−1, 1
1, −1
T
1, −1
−1, 1


## Page 69

Nash Equilibrium in Mixed Strategies
Example: Coordination game
We will see there is also a mixed strategy NE
Let σ1 = (σ1(O), σ1(B)) = (p, 1 −p) and σ2 = (σ2(O), σ2(B)) = (q, 1 −q)
Let us use the result: for player 1 we have
u1(O, σ2) = u1(B, σ2) ⇒q2 + (1 −q)0 = q0 + (1 −q)1 ⇒q = 1
3
and for player 2 we have
u2(O, σ1) = u2(B, σ1) ⇒p1 + (1 −p)0 = p0 + (1 −p)2 ⇒p = 2
3
Thus, the mixed strategy NE is σ1 =
  2
3, 1
3

and σ2 =
  1
3, 2
3

, and each player
gets expected payoﬀequal to 2
3
Player 2
O
B
Player 1
O
2, 1
0, 0
B
0, 0
1, 2


## Page 70

Mixed Strategy Nash Equilibrium
Example: Reporting a crime
A crime is observed by n people and each has to decide whether or not to
report the crime to the police
Each person derives utility v is the crime is reported
But the person who reports incurs cost c > 0, with c < v, so each person
prefers that someone else reports the crime
The strategic representation of the game is:
Players: n individuals
Strategies: Si = {C, D}, where C is call and D is do not call
Payoﬀs: each player i’s payoﬀis 0 if nobody reports; v is someone other than
i reports; v −c if i reports


## Page 71

Mixed Strategy Nash Equilibrium
Continuation of example:
This game has n pure strategy NE in which only one player reports and the
other ones do not (check)
There is also a mixed strategy NE that is symmetric: each player i plays
σi = (σi(C), σi(D)) = (p, 1 −p)
To ﬁnd p, by the result we have seen, it has to be the case that each i is
indiﬀerent between C and D when all other players play this strategy:
v −c = P[all other players play D] × 0 + P[at least one player −i plays C] × v
What is the probability that at least one player that is not i plays C?
This is the same as 1 −P[s−i = (D, D, ..., D)] = 1 −(1 −p)n−1 (check)
Thus, equation above is v −c = v(1 −(1 −p)n−1), which rearranges to
c
v = (1 −p)n−1 ⇒p = 1 −
 c
v

1
n−1


## Page 72

Mixed Strategy Nash Equilibrium
Continuation of the example:
Hence, the mixed strategy NE consists of every i playing
σi = (p, 1 −p) =

1 −
 c
v

1
n−1 ,
 c
v

1
n−1

Let us examine p = 1 −
  c
v

1
n−1
Note that as the group gets large (n increases), p decreases: the probability
that a player calls in equilibrium decreases in the number of people around
How about the probability that “at least someone will call”? Does it increase
or decrease in n? Fix any player i and write
P[every player plays D] = P[i plays D]P[every player −i plays D]
But we saw that that P[i plays D] increases in n (why?); also from equation
above P[every player −i plays D] = c
v , which is independent of n
Hence, the probability that nobody calls increases in n, which is surprising


## Page 73

Mixed Strategy Nash Equilibrium
Remarks:
NE is fundamental solution concept in games
We have seen many examples, some with a unique NE and some with multiple
In fact, in any game in which Si has a ﬁnite number of elements for every i
there exists a NE (could be in mixed strategies)
In games in which Si can be uncountable, a NE in pure strategies exists if (a)
Si is nonempty, convex, compact subset of Rk, and (b) ui is continuous in
(s1, s2, ..., sn) and (quasi-) concave in si
These two results cover a large class of games
Existence is satisﬁed, uniqueness is not since there can be multiple NE
Eﬃciency is not satisﬁed either (e.g., (C, C) in prisoner’s dilemma is a NE)
Some NE of a given game are not robust to small changes in payoﬀs


## Page 74

Best Response Correspondence
There is a nice way to visualize the NE in some of the examples using the
concept of best response correspondence of player i, denoted BRi:
BRi of player i maps each σ−i ∈∆(S−i) to a subset BRi(σ−i) of Si, where
each σi ∈BRi(σi) is a best response for player i against σ−i
Why is it called “correspondence” and not “function”?
If a player has a unique best response to each strategy proﬁle of the other
players, then BRi is a function (e.g., Cournot duopoly)
But, in some cases player i may have more than one best response when other
players play σ−i, hence the more general concept of correspondence
Note that (σ1, σ2, ..., σn) is a NE if σi ∈BRi(σ−i) for all i
Since a pure strategy is a special case of a mixed strategy, the same concept
holds for pure strategies


## Page 75

Best Response Correspondence
Example: Cournot duopoly
Recall that in that case FOCs are s1 = 90−s2
2
and s2 = 90−s1
2
Note what the ﬁrst equation says: for each quantity s2 that ﬁrm 2 produces,
the best response for ﬁrm 1 is to produce 90−s2
2
Thus, BR1(s2) = 90−s2
2
, and similarly BR2(s1) = 90−s1
2
The conditions for NE, s1 ∈BR1(s2) and s2 ∈BR2(s1), simply says that
(s1, s2) must solve the two equations in two unknowns
Graphically, it is depicted as the intersection of the two best responses


## Page 76

Best Response Correspondence
Example: Matching pennies
Recall σ1 = (p, 1 −p) and σ2 = (q, 1 −q)
Let us denote the best response of 1 by BR1(q), since σ2 is summarized by q
Facing q, payoﬀof H for 1 is q(−1) + (1 −q)1 = 1 −2q, and from T is 2q −1
Thus, if q < 0.5, then the best for player 1 is to choose H for sure (p = 1),
and if q > 0.5 the best for 1 is to choose L for sure (p = 0)
And if q = 0.5, then player 1 is indiﬀerent among all values of p ∈[0, 1]
Player 2
H
T
Player 1
H
−1, 1
1, −1
T
1, −1
−1, 1


## Page 77

Best Response Correspondence
Continuation of the example:
Let us analyze BR2(p) now
Facing p, payoﬀof H for 1 is p1 + (1 −p)(−1) = 2p −1, and from T is 1 −2p
Thus, if p < 0.5, then the best for player 2 is to choose T for sure (q = 0),
and if p > 0.5 the best for 2 is to choose H for sure (q = 1)
And if p = 0.5, then player 2 is indiﬀerent among all values of q ∈[0, 1]
Player 2
H
T
Player 1
H
−1, 1
1, −1
T
1, −1
−1, 1


## Page 78

Best Response Correspondence
Summarizing:
BR1(q) =







p = 1
if q < 0.5
p ∈[0, 1]
if q = 0.5
p = 0
if q > 0.5
BR2(p) =







q = 0
if p < 0.5
q ∈[0, 1]
if p = 0.5
q = 1
if p > 0.5
The only intersection is at p = q = 0.5 (check), the mixed strategy NE


## Page 79

Best Response Correspondence
Example: Coordination game
Proceeding as in the matching pennies example, we obtain
BR1(q) =







p = 0
if q < 1
3
p ∈[0, 1]
if q = 1
3
p = 1
if q > 1
3
BR2(p) =







q = 0
if p < 2
3
q ∈[0, 1]
if p = 2
3
q = 1
if p > 2
3
Now there are three intersections, the three NE (check)
Player 2
O
B
Player 1
O
2, 1
0, 0
B
0, 0
1, 2
