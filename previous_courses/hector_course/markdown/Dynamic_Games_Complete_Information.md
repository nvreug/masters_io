# Dynamic Games Complete Information

*Converted from: Dynamic_Games_Complete_Information.pdf*

---


## Page 1

ECN 532
Microeconomics II
Hector Chade
Second Quarter 2025


## Page 2

DYNAMIC GAMES WITH COMPLETE INFORMATION


## Page 3

Lecture’s Objective
In this lecture we will cover dynamic strategic situations
We will learn the following
We will ﬁrst introduce the extensive form representation
We will then focus on games with complete and perfect information and learn
how to solve them by backward induction
Then we will turn to games with complete but imperfect information and
deﬁne a more general solution concept called subgame perfect equilibrium
This is a reﬁnement of Nash equilibrium
We will go over economic applications


## Page 4

Notation
We will use the following notation:
Γe is an extensive-form game
Game tree is collection of nodes X with precedence relation >
Hi collection of information sets hi of player i
Ai(hi) set of actions of i at hi
si : Hi →Ai, si(hi) ∈Ai(hi) is a pure strategy
σi is a probability distribution over pure strategies of i


## Page 5

Extensive-Form Games


## Page 6

Deﬁnition of Extensive-Form Games
An extensive form game, denoted by Γe, speciﬁes the following:
1. Set of players N = {1, 2, ..., n}
2. Order of moves of the players
3. Set of actions Ai of player i = 1, 2, ..., n when they can choose
4. Knowledge players have when they choose
5. Probability distributions over exogenous events (moves by Nature)
6. Payoﬀfunctions for each player, ui, as a function of outcomes
7. All of these items are common knowledge among all the players


## Page 7

Deﬁnition of Extensive-Form Games
Remarks:
Note that the ﬁrst and last item are as in the normal form
The rest provides more detail about interaction (order, actions, knowledge)
Regarding knowledge players have, if say player i chooses after player j, this
item speciﬁes whether i observes and thus knows j’s choice or not
When there is some exogenous uncertainty in the game (e.g., demand can be
high or low with given probabilities in a game among ﬁrms), we add a player,
Nature, who chooses according to a pre-speciﬁed probability distribution


## Page 8

Deﬁnition of Extensive-Form Games
Example: trust game
One individual has to decide whether to request a service from another
Requesting a service means “trust” while not doing it means “no trust”
If she does not request, each obtains a payoﬀof 0
If she requests it and the other person provides the service well, then payoﬀs
are 1 for each
If she requests it and the other provides an inferior low cost service, then
payoﬀs are −1 for individual who requested service and 2 for the other one


## Page 9

Deﬁnition of Extensive-Form Games
The extensive form game of the example is as follows:
Two players, 1 and 2
Player 1 chooses ﬁrst, player 2 chooses second
Player 1 can choose between T or N; player 2 chooses between G or B
Player 2 knows when they choose that player 1 has played T
Payoﬀs are u1(N, G) = u1(N, B) = 0, u1(T, G) = 1, u1(T, B) = −1 for
player 1; u2(N, G) = u2(N, B) = 0, u2(T, G) = 1, u2(T, B) = 2 for player 2


## Page 10

Deﬁnition of Extensive-Form Games
Example: Sequential version of coordination game
Consider a sequential version of the coordination game in which player 1
chooses O or B ﬁrst, player 2 observes and then makes a choice
The extensive form game of the example is as follows:
Two players, 1 and 2
Player 1 chooses ﬁrst, player 2 chooses second
Player 1 can choose between O or B; player 2 chooses between O or B
Player 2 knows when they choose that player 1 has played either O or B
Payoﬀs are u1(O, B) = u1(B, O) = 0, u1(O, O) = 2, u1(B, B) = 1 for player
1; u2(O, B) = u2(B, O) = 0, u2(O, O) = 1, u2(B, B) = 2 for player 2


## Page 11

Game Trees
A game tree is a diagrammatic description of Γe
A game tree is deﬁned as follows:
It is a set of nodes x ∈X with a precedence relation x > x′ (x precedes x′)
Every node has only one predecessor
> is transitive, asymmetric, and incomplete (not all nodes can be ordered)
The root of the tree, x0, is a node that precedes all of the other nodes
Nodes that precede other nodes are called terminal nodes. The set of terminal
nodes is denoted by Z, which is a subset of X
Each terminal node has associated payoﬀs for each player (end of the game)
Every node x that is not a terminal node is assigned either to a player i with
action set Ai(x), or to Nature


## Page 12

Game Trees
Example: Game tree of trust game
N
T
G
B
(0, 0)
(1, 1)
(−1, 2)
Player 1
Player 2


## Page 13

Game Trees
Example: Sequential version of coordination game
O
B
O
B
O
B
(2, 1)
(0, 0)
(0, 0)
(1, 2)
Player 1
Player 2
Player 2


## Page 14

Game Trees
Let us elaborate on the information a player has in a game
Each player i has a collection of information sets hi ∈Hi that partitions the
nodes at which i chooses, with the following properties:
If hi contains a single node x, then i knows that they are at x
If x ̸= x′, x ∈hi and x′ ∈hi, then i does not know whether they are at x or
x′ when choosing at x
If x ̸= x′ and x ∈hi and x′ ∈hi, then Ai(x) = Ai(x′)
Some intuition:
The ﬁrst condition says that i knows that when the game reaches x and it is
their turn to choose, i knows that they are at x
The second means that at hi, both x and x′ are consistent with reaching that
part of the game, and i does not know at which node they are choosing
Finally, the last condition is for logical consistency: if the action sets at the
two nodes where diﬀerent, then i would know whether they are at x or x′


## Page 15

Perfect and Imperfect Information
Consider a game with complete information:
If every information set of every player has only one node, then the game has
perfect information
If some information sets contain several nodes, then the game has imperfect
information
Examples:
Coordination game has imperfect information
Sequential version of coordination game has perfect information
Trust game has perfect information
Game tree of prisoner’s dilemma has imperfect information


## Page 16

Game Trees
Example: Coordination game
O
B
O
B
O
B
(2, 1)
(0, 0)
(0, 0)
(1, 2)
Player 1
Player 2
Player 2


## Page 17

Strategy in Γe
A pure strategy for player i in Γe is si : Hi →Ai that assigns si(hi) ∈Ai for
every information set
This dovetails nicely with the idea of a strategy as a complete plan of action
With one caveat: the deﬁnition above requires that si be deﬁned even at
places that are not reached when the game is played
This point will become clear later
A mixed strategy in Γe is a probability distribution over pure strategies si
A related notion is a behavioral strategy in Γe:
It speciﬁes for each information set hi an independent probability distribution
βi : Hi →∆(Ai(hi))
This says that instead of randomizing over pure strategies, player i can
randomize in each hi over the actions at that hi
If Γe has perfect recall (a player never forgets what they once knew), then
mixed and behavioral strategies are equivalent


## Page 18

Normal-Form Game from Extensive-Form Game
Given Γe, we can easily derive the associated Γ = (N, (Si)i∈N, (ui)i∈N)
Take the collection of all the pure strategies si deﬁned above, and call it Si,
i = 1, 2, ..., n
For any strategy proﬁle, deﬁne ui as the payoﬀobtained in the corresponding
terminal node of Γe
We immediately obtain the following:
The set of NE of Γe can be obtained by deriving all the NE of the associated Γ
Terminology:
Given a NE in Γe (in pure or mixed strategies), we say that an information set
is on-the-equilibrium path if it is reached with strictly positive probability
Given a NE in Γe (in pure or mixed strategies), we say that an information set
is oﬀ-the-equilibrium path if it is never reached


## Page 19

Backward Induction


## Page 20

Sequential Rationality and Credibility
Although we could use NE as our solution concept, we will see that it is too
weak in a precise sense in interactions that are sequential
The main issue is that strategies in a NE can lack the property of being
sequentially rational, or “credible”
Let us illustrate this point with a simple example, an entry game:
O
I
F
A
(0, 2)
(−3, −1)
(2, 1)
Player 1
Player 2


## Page 21

Sequential Rationality and Credibility
The strategic representation of this game is the one below:
Note that there are two NE: (I, A), (O, F)
If 1 thinks 2 will play A, the best response for 1 is I, and if 2 thinks 1 will play
I, the best for 2 is A. Thus, (I, A) is a NE
If 1 thinks 2 will play F, the best for 1 is O, and if 2 thinks 1 will play O, F is
one of the best responses. Thus, (O, F) is a NE
Note in passing that the second one is a NE in which player 2 plays a weakly
dominated strategy, F
Player 2
A
F
Player 1
I
2, 1
−3, −1
O
0, 2
0, 2


## Page 22

Sequential Rationality and Credibility
There is something unappealing about the second NE once we look at it in
the extensive form
Loosely speaking, it relies on an empty threat, or lacks credibility
Note that in (O, F), player 1 plays O because she believes that 2 will play F
But, a natural conjecture should be that if player 2 is asked to make a choice
at his information set, then he will play optimally having reached that point
That is, player 1 should expect player 2 to play A instead of F, since at 2’s
information set, this is the optimal choice for player 2
In other words, NE (O, F) fails to be sequentially rational, or lacks credibility
Instead, NE (I, A) satisﬁes sequential rationality at each information set
Problem: NE in an extensive form game puts no constraints on the belief a
player has about how the other player would play oﬀthe equilibrium path


## Page 23

Backward Induction
Let us deﬁne sequential rationality:
Given σ−i, we say that σi is sequentially rational if player i is playing a best
response to σ−i at each of their information sets
How do we ﬁnd strategy proﬁles that are NE and also satisfy sequential
rationality for each player?
For games with complete and perfect information, this is accomplished by a
procedure called backward induction
Start at the end of the game tree and check the last information sets
Find at each of those information sets the player’s optimal choice
Then move backwards to the next to last information sets, and choose the
optimal action for each of the players who make a choice, assuming that in the
last information sets choices will be optimal
Proceed inductively until reaching the root of the game tree


## Page 24

Backward Induction
Example: Entry game
In this game backward induction leads to the prediction (I, A)
Example: Sequential version of coordination game
What are the NE of this game? What is the backward induction prediction?
O
B
O
B
O
B
(2, 1)
(0, 0)
(0, 0)
(1, 2)
Player 1
Player 2
Player 2


## Page 25

Backward Induction
Regarding existence, one can easily prove (how?)
In any ﬁnite game with complete and perfect information, there is a
backward induction solution that is sequentially rational
And if there no ties for a player payoﬀs at any of their terminal nodes, then
the backward induction solution is unique
It follows that in any ﬁnite game with complete and perfect information, there
is a NE that is sequentially rational
But as the examples illustrate, there could be other NE that are not credible


## Page 26

Subgame Perfect Equilibrium


## Page 27

Subgames
We run into problems when we want to extend the backward induction
procedure to games with complete but imperfect information
Another issue is how to analyze sequentially rational NE in games with an
inﬁnite number of stages (or periods). We will deal with this issue later
Let us see an example with imperfect information:
Y
N
O
B
O
B
O
B
(1.5, 1.5)
(2, 1)
(0, 0)
(0, 0)
(1, 2)
Player 1
Player 1
Player 2
Player 2


## Page 28

Subgames
In this example player 1 ﬁrst chooses whether to play the coordination game
Note that it is unclear how to adapt backward induction to this case
Player 2 at the end has an information set with two nodes, and it is not clear
how player 2 will choose without having some belief about what player 1 will
choose in that part of the game
But beliefs are not part of the procedure of backward induction
To extend the logic of backward induction, we need the notion of subgame
A proper subgame G of Γe consists of a single node and all of its successors
with the property that if x ∈G and x′ ∈hi(x), then x ∈G
The subgame G is itself a game tree with information sets and payoﬀs
inherited from Γe


## Page 29

Subgames
Examples:
In the previous example there are two proper subgames: the whole game, and
the one that starts at the second node of player 1
In the sequential version of the coordination game there are three proper
subgames (which ones?)
O
B
O
B
O
B
(2, 1)
(0, 0)
(0, 0)
(1, 2)
Player 1
Player 2
Player 2


## Page 30

Subgame Perfect Equilibrium
We can now deﬁne the following solution concept
A strategy proﬁle σ = (σ1, σ2, ..., σn) is a subgame perfect equilibrium (SPE)
of Γe if for every proper subgame G of Γe, the restriction of σ to G is a NE
It is also called subgame perfect Nash equilibrium (SPNE)
Note that it is a natural generalization of the backward induction solution,
and in games with perfect information SPE reduces to the NE found by
backward induction
Hence, SPE applies to both games with perfect and imperfect information
SPE ensures that players strategies are sequentially rational in each proper
subgame G (oﬀand on equilibrium path) by requiring to be a NE in G
In particular, this implies that a SPE is indeed a NE (the entire game is a
proper subgame of itself) but in sequentially rational strategies (credible)


## Page 31

Subgame Perfect Equilibrium
Example:
In the coordination game in which 1 can decide whether to play it or not,
there are two proper subgames
Y
N
O
B
O
B
O
B
(1.5, 1.5)
(2, 1)
(0, 0)
(0, 0)
(1, 2)
Player 1
Player 1
Player 2
Player 2


## Page 32

Subgame Perfect Equilibrium
Example:
Let us start the analysis from the back of the game: in that subgame there are
two NE, (O, O) and (B, B)
Pick one of them, say (O, O); then moving back, player 1 anticipates that if
she chooses Y the continuation is (O, O) and thus she obtains 2
Hence, it is optimal for her to play Y and the following is a SPE: ((Y, O), O)
Pick now the NE (B, B); then moving back player 1 anticipates that if she
chooses Y the continuation is (B, B) and she obtains 1
Hence, it is optimal for her to play N and the following is a SPE: ((N, B), B)
Thus, in this game there are two SPE (check that both are NE); and there is
another NE that is not SPE (which one?)


## Page 33

Subgame Perfect Equilibrium
Remarks:
SPE was developed by Selten (1975), backward induction by Zermelo (1913)
SPE is a reﬁnement of NE (it is a NE that satisﬁes an additional property)
Regarding existence, since we need to check that a SPE is a NE in each proper
subgame, and there is always a NE in any ﬁnite game, it follows that a SPE
exists in every ﬁnite game (with perfect or imperfect information)
As the previous example illustrates, it need not be unique, and one can show
that it need not be eﬃcient
Terminology: the strategy proﬁle that is a SPE is a complete plan on and oﬀ
the equilibrium path; the outcome of a SPE is the equilibrium path traced by
the strategy proﬁle
For example, ((N, B), B) is a SPE, whose outcome is N with payoﬀs (1.5, 1.5)


## Page 34

Muti-Stage Games


## Page 35

Deﬁnition of a Multi-Stage Games
A particular class of extensive form games important for economic
applications is the class of multi-stage games with observed actions:
It is divided into T ≤∞stages (or periods)
Within each stage, players play simultaneously and each player moves only
once in each stage
At the end of each stage t, players know the actions taken by all the players
(including moves by nature) in all previous stages
The payoﬀof player i at the end of the game depends on the entire history of
play from the initial stage 0 to the ﬁnal stage T
At each stage t, the history up to that point is ht = (a0, a1, ..., at−1), where
ak = (ak
1, ak
2, ..., ak
n) is vector of actions chosen by the n players in stage k
Regarding the payoﬀof i (most) common speciﬁcations are:
The sum of payoﬀs of each stage PT
t=0 ui(at)
The discounted sum of payoﬀs of each stage PT
t=0 δtui(at), with δ ∈(0, 1)


## Page 36

Deﬁnition of Multi-Stage Games
Remarks:
One way to interpret this class of games is that players play a sequence of
normal form games, which need not be the same game in each stage
Regarding the discounted sum of payoﬀs, player i receives a payoﬀat the end
of each stage t, and so
T
X
t=0
δtui(at) = ui(a0) + δui(a1) + · · · + δT ui(aT )
The discount factor δ reﬂects the degree of patience of player i
Extreme case of impatience is δ = 0: only payoﬀs in current stage matter
Extreme case of patience is δ = 1: receiving a given payoﬀtoday or tomorrow
is valued the same way
Higher value of δ means that a player is more patient and thus puts higher
value on future payoﬀs


## Page 37

Subgame Perfect Equilibrium
Since a multi-stage game with observed actions is an extensive form game
with complete and imperfect information
We use SPE as our solution concept
Example: Prisoner’s dilemma
Recall the prisoner’s dilemma and assume that is is played twice
Assume payoﬀto each player is sum of each stage payoﬀ
Find the subgame perfect equilibria of the game
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


## Page 38

Subgame Perfect Equilibrium
The following results are now very intuitive (proof?):
If σ is a NE (in pure or mixed strategies) of the multi-stage game consisting of
a sequence Γ0, Γ1,...,ΓT normal form games, then the restriction of σ to the
game in stage T must be a NE of that stage game
In a ﬁnite multi-stage game, if the simultaneous game played at each stage
has a unique NE, then the multi-stage game has a unique SPE
Note how the second result is based on the ﬁrst one:
By the ﬁrst result, it must be the case that in the last stage the unique NE is
played after each history reaching that part
Moving backwards to the beginning of previous stage, the unique NE must be
played since no matter what is played the continuation is the same
Continuing backwards we reach the root of the game tree and at that stage
the unique NE is played as well
We have thus constructed the unique SPE of the multi-stage game


## Page 39

Subgame Perfect Equilibrium
A third result is the following one:
In a multi-stage game, if σt is a NE of stage t, t = 0, 1, ..., T, then the
resulting sequence σ0, σ1, ..., σT is a SPE of the multi-stage game
Regardless of history at each stage a NE is played, and thus resulting proﬁle
constitutes a SPE, since in every subgame a NE is played (check)
Example: Variation of prisoner’s dilemma
Assume two stages, discount factor is δ ∈(0, 1)
First stage prisoner’s dilemma is played; second stage, game below is played
Player 2
l
g
Player 1
L
1, 1
−4, −1
G
−1, −4
−2, −2


## Page 40

Subgame Perfect Equilibrium
Continuation of example:
In the ﬁrst stage there is a unique NE, (C, C)
In the second stage there are two NE in pure strategies, (L, l) and (G, g) (and
one in mixed strategies)
Applying previous result, playing (C, C) in ﬁrst stage and (L, l) in second
stage after every history is a SPE
(C, C) in ﬁrst stage and (G, g) in second stage after every history is a SPE
(C, C) in ﬁrst stage and the NE in mixed strategies in second stage after every
history is a SPE


## Page 41

Subgame Perfect Equilibrium
Continuation of the example:
We can say something much more interesting if players condition their play on
the history of ﬁrst stage. Consider the following strategies for each player
Player 1: I will play M in ﬁrst stage; in the second stage, if 2 played M in ﬁrst
stage, I will play L; otherwise I will play G
Player 2: I will play M in ﬁrst stage; in the second stage, if 1 played M in ﬁrst
stage, I will play l; otherwise I will play g
Let us check that these strategies are a SPE if δ is large enough
In the second stage, after each history a subgame starts and players play a NE
Consider player i, i = 1, 2, in the ﬁrst stage
If player i plays M, then payoﬀis 5 + δ2
If player i plays C, then payoﬀis 8 + δ(−2)
Thus 5 + δ2 ≥8 + δ(−2) if and only if δ ≥3
4, in which case we have a SPE


## Page 42

Repeated Games


## Page 43

Deﬁnition of Repeated Game
Repeated games are a special class of multi-stage games:
In this class, the same normal form game is played at every stage
A repeated game can have ﬁnite or inﬁnite horizon
Most common player’s payoﬀfunction is discounted sum of utilities, with
discount factor δ ∈(0, 1)
This class shows up in many relevant applications:
Firms competing repeatedly over time for many periods
A ﬁrm and its suppliers interact repeatedly over time
Politicians repeatedly negotiate among them in congress
Workers producing in teams that interact repeatedly
Countries engage repeatedly in bilateral or multilateral agreements
Analysis of repeated games sheds light on logic of long-term interaction


## Page 44

Finitely Repeated Games
Recall Γ is a strategic form game
A ﬁnitely repeated game with horizon T < ∞consists of
A stage game Γ that is played consecutively T times
Players’ payoﬀs are given by a discounted sum of utilities with common
discount factor δ ∈(0, 1]
Remarks:
Note that in this case we allow δ = 1 (no discounting)
We assume a common δ but this can easily be relaxed


## Page 45

Finitely Repeated Games
Recall the following result we stated for multi-stage games:
In a ﬁnite multi-stage game, if the simultaneous game played at each stage
has a unique NE, then the multi-stage game has a unique SPE
This result also applies to ﬁnitely repeated games:
At each stage the same normal form game Γ is repeated
If Γ has a unique NE, then the ﬁnitely repeated game has a unique SPE
The outcome of that SPE is that the NE of Γ is played at every stage
Implication:
In ﬁnitely repeated prisoner’s dilemma, SPE outcome is (C, C) every period
Counterintuitive if one thinks about T very large, say 100


## Page 46

Finitely Repeated Games
Things are more interesting if the stage game has more than one NE
Example:
Consider the game below played twice
There are two NE in pure strategies in the stage game, (B, b) and (C, c)
There is another one in mixed strategies, but let us focus on these two
Note they are Pareto ranked (both players are strictly better oﬀin (C, c))
By a previous result for multi-stage games, playing any sequence of these NE
during the two periods constitute a SPE (check)
Player 2
a
b
c
Player 1
A
4, 4
−1, 5
0, 0
B
5, −1
1, 1
0, 0
C
0, 0
0, 0
3, 3


## Page 47

Finitely Repeated Games
Continuation of example:
We know in second period in each subgame a NE must be played (why?), but
which one is played can be dependent on the ﬁrst period
Suppose player 1 plays A in the ﬁrst period; in second period plays C if player
2 played a in ﬁrst period, otherwise plays B in second period
Suppose player 2 plays a in the ﬁrst period; in second period plays c if player 1
played A in ﬁrst period, otherwise plays b in second period
If δ ≥0.5, then this is a SPE, with outcome (A, a), (C, c) (check)
Player 2
a
b
c
Player 1
A
4, 4
−1, 5
0, 0
B
5, −1
1, 1
0, 0
C
0, 0
0, 0
3, 3


## Page 48

Finitely Repeated Games
Remarks:
Note that in the second period each player is playing optimally given what the
other is doing (NE logic)
Regarding the ﬁrst period, each player by playing its part obtains 4 in that
period and 3 in the second one
By deviating in the ﬁrst period a player can obtain 5 in the ﬁrst period, but
given the assumed strategies, the player obtains 1 in the second period
By deviating a player makes 1 more in ﬁrst period but 2 less in second period
So if second period payoﬀs are not discounted more than half, then each
player will not deviate in ﬁrst or second period, and the strategies are a SPE
The existence of multiple NE in stage game allows players to design strategies
that incorporate “rewards and punishments”


## Page 49

Inﬁnitely Repeated Games
Now T = ∞, so stage game is played an inﬁnite number of times
Equivalently, at each stage there is a positive probability the game continues
Plausible assumption in economic applications in which players do not know
how many times they are going to play the stage game
For example, oligopolistic markets in which same set of ﬁrms compete over
and over again without a foreseeable end
Some remarks about inﬁnite discounted sums of payoﬀs:
Suppose an individual obtains $100 in perpetuity; discount factor is δ ∈(0, 1)
Let S be discounted sum P∞
t=0 $10; it satisﬁes S = $10 + δS ⇒S = $10
1−δ
Hence, the discounted sum of receiving an amount ˆu of utility is
ˆu
1−δ
For a stream (u0, u1, u2, ...) we do not have a closed form in general, but as
long as these utility amounts are bounded, then sum is well deﬁned (check)
If v = P∞
i=0 δtut(at), then ¯v = (1 −δ) P∞
i=0 δtut(at) is the average payoﬀ
(allows to compare inﬁnitely repeated game payoﬀwith stage game payoﬀs)


## Page 50

Inﬁnitely Repeated Games
Recall that a strategy is a complete contingent plan which speciﬁes how a
player would choose at each of their information sets
Inﬁnitely repeated game: each player has inﬁnite number of information sets
How is a strategy deﬁned in this case?
Key observation: each information set t identiﬁed with a unique path up to t
Thus, to each information set of a player, there exists a unique history that
reaches that information set
Identify each information set with a history of play (one-to-one relationship)
The deﬁnition of a strategy is now obvious:
Ht set of all t-histories ht ∈Ht, and H = ∪∞
t=1Ht set of all histories
A pure strategy for player i in the inﬁnitely repeated game is si : H →Si,
where Si is the set of actions of player i in the stage game
A behavioral strategy for player i in inﬁnitely repeated game is σi : H →∆(Si)


## Page 51

Inﬁntely Repeated Games
Checking whether a strategy proﬁle is SPE seems impossible
Checking if a deviation is proﬁtable requires to check all possible deviations
(at only one information set, at two, at three,...,at an inﬁnite number)
A similar issue applies to any multi-stage game:
Checking for all possible deviations can be a very complex task
The one-shot deviation principle (OSDP) comes to our rescue:
For any multi-stage game, consider σi, and let σa,hi
i
be the strategy that is
identical to σi except after history hi, where it replaces whatever σi plays by
action a of player i
A strategy satisﬁes OSDP if, given σ−i, for every a and hi of player i, there is
no deviation from σi to σa,hi
i
that is proﬁtable
Given σ−i, if σi satisﬁes OSDP, then it is optimal for player i


## Page 52

Inﬁnitely Repeated Games
This is an amazing result that drastically simpliﬁes checking for SPE:
In any multi-stage game (actually in any extensive form game), one only needs
to check that a strategy proﬁle satisﬁes OSDP for each player
Particularly useful in inﬁnitely repeated games:
Each information set at t is associated with a history of play ht
For (σ1, σ2, ..., σn) to be SPE of inﬁnitely repeated game, suﬃces to check
that for each i, given σ−i, the strategy σi satisﬁes OSDP
Easy to sketch why OSDP implies optimality:
If σi satisﬁes OSDP but is not optimal, then some σ′
i is strictly better
If σ′
i involves deviations are a ﬁnite number of information sets, then at the last
one of those, OSDP of σi implies that from that point on σ′
i is better than σ′
i
Moving back, same holds at next to last deviation; so on until ﬁrst deviation,
and it follows that σi has weakly higher payoﬀthan σ′
i, contradiction
Similar argument if σ′
i entails an inﬁnite number of deviations


## Page 53

Inﬁnitely Repeated Games
In ﬁnitely repeated prisoner’s dilemma unique SPE yields (C, C) in every t
This need not be the case in the inﬁnitely repeated version
Example: Prisoner’s Dilemma
Note there is a SPE in which each player plays si(ht) = C for every t
But if players are patient enough, there are other SPE
The idea once again is to structure punishments and rewards
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


## Page 54

Inﬁnitely Repeated Games
Continuation of example:
Consider the following strategies for each player i = 1, 2
Player i starts by playing M, and continues to do so at each t if history of play
is (M, M), (M, M),...; if not, i plays C from that point onwards
Formally, for both i = 1, 2, si(h0) = M, s(ht) = M if
ht = ((M, M), (M, M), ..., (M, M)); for any other ht, st(ht) = C
Each player starts being “nice” and continues to be nice if both have been nice
in the past; otherwise, “trust” or “credibility” is lost and each switches to C
Called a trigger strategy: a deviation triggers a change in behavior forever
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


## Page 55

Inﬁnitely Repeated Games
Continuation of example:
Let us check that this strategy proﬁle (s1, s2) is SPE of the inﬁnitely repeated
game when players are patient enough
Trigger strategies partition the set of all histories into two sets
One set consists of ht = ((M, M), (M, M), ..., (M, M)) for each t
The other set consists of all other ht for each t
In the second set, note that players are playing (C, C) all the time in each of
the ht, which is a NE in any of the subgames that starts at such ht
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


## Page 56

Inﬁnitely Repeated Games
Continuation of the example:
Consider now any ht = ((M, M), (M, M), ..., (M, M))
By OSDP, it is enough to check for a single deviation an any point in time
along this history, given the strategy of the other player
Player i has two choices: if i plays M today then discounted payoﬀis (why?)
5 + δ5 + δ25 + δ35 + · · · =
5
1 −δ = 5 +
δ
1 −δ 5
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


## Page 57

Inﬁnitely Repeated Games
Continuation of example:
If instead player i plays C today, then discounted payoﬀis (why?)
8 +
δ
1 −δ 3
Thus, i’s strategy is optimal if and only if (why?)
5 +
δ
1 −δ 5 ≥8 +
δ
1 −δ 3 ⇒δ ≥3
5
Thus, if δ ≥0.6, then (s1, s2) is a SPE, since players are playing a NE in every
proper subgame of the inﬁnitely repeated game (check)
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


## Page 58

Inﬁnitely Repeated Games
Remarks:
The example illustrates a general insight from inﬁnitely repeated games
Repetition without a foreseeable end can expand the predictions that we
obtain from a ﬁnitely repeated game
In this example, the credible threat that play will switch to (C, C) forever
upon a deviation from playing (M, M), makes playing (M, M) all the time an
equilibrium path, which involves behavior that is not NE in the stage game
Same is true in a general inﬁnitely repeated game, not just prisoner’s dilemma
The SPE constructed is not the only one besides repetition of NE
For example, one can also construct a SPE in which players alternate between
(M, C) in odd periods and (C, M) in even periods, again with the threat of
reverting to (C, C) forever (check)
Indeed, the number of SPE payoﬀs that can be sustained in an inﬁnitely
repeated game is enormous, as exempliﬁed by the so called “folk theorem”


## Page 59

Inﬁnitely Repeated Games
Folk theorem asserts the following:
Let Γ be a ﬁnite stage game that inﬁnitely repeated
Let V be the convex set of payoﬀs constructed from payoﬀvectors of Γ
Let u∗= (u∗
1, u∗
2, ..., u∗
n) be the payoﬀfrom a NE in Γ
Let v = (v1, v2, ..., vn) be a vector of payoﬀs in V such that vi > u∗
i for all i
If δ suﬃciently close to 1, there is a SPE (s1, s2, ..., sn) in the inﬁnitely
repeated game that yields average payoﬀs arbitrarily close to (v1, v2, ..., vn)
Easy to illustrate the Folk theorem in the prisoner’s dilemma (check)
Remark:
There are more general versions of the folk theorem in the literature, as well
versions in which the actions of players are not observable but a noisy signal is
