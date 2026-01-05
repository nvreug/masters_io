# Adverse Selection

*Converted from: Adverse_Selection.pdf*

---


## Page 1

ECN 532
Microeconomics II
Hector Chade
Second Quarter 2025


## Page 2

ADVERSE SELECTION


## Page 3

Lecture’s Objectives
We saw how hidden action or moral hazard can aﬀect transactions
The “remedy” is the proper design of incentive schemes
Another fundamental information friction is that of hidden information, which
is also called adverse selection
Pervasive problem that aﬀects markets and organizations
After discussing some real-world examples, we analyze the eﬀects of adverse
selection in markets, including the possibility of complete market failure
Then we will discuss some remedies such as signaling and screening


## Page 4

Adverse Selection: Deﬁnition and Examples


## Page 5

Deﬁnition and Historical Remarks
Let us deﬁne what the problem of adverse selection or hidden information is:
There is adverse selection when one party to a transaction knows something
that is payoﬀ-relevant but unknown to the other party
In earlier general equilibrium literature, this problem received little attention
Adam Smith (1776) mentioned problem of interest rates and bad borrowers
Hayek (1945) puts information at the heart of markets vs. planning debate
Mirrlees (1971) analyzes optimal taxation with hidden information
Fundamental contributions:
Akerlof (1970): adverse selection eﬀects in market settings
Spence (1973): signaling can mitigate adverse selection
Rothschild and Stiglitz (1976): screening can mitigate adverse selection
Stiglitz (1977), Mussa and Rosen (1978), Maskin and Riley (1984),
principal-agent with adverse selection, and Myerson (1981) for auctions


## Page 6

Real-World Examples
Hidden information or adverse selection is pervasive in economic interactions
Any time one party has private information that the other party would beneﬁt
from knowing it, there is a problem of hidden information
But there is a large class of hidden information problems (which are the ones
that should properly be called adverse selection problems) that are
particularly problematic and subtle
This class is the so called “selection markets”
Roughly speaking, those customers with a higher willingness to pay for a
good are also those more costly to serve
This applies in particular to insurance markets in general, but it has many
more applications of economic interest
We are going to begin with a series of examples to get a ﬂavor of the
problem we will analyze in detail below


## Page 7

Real-World Examples
American Airlines AAirpass
In 1981, for $250,000 one could buy a mileage pass with unlimited ﬁrst-class
travel for life
Generated big losses from the start
Problem: only those who traveled a lot bought the pass
Those are the most costly customers for AA
By 1990, AAirpass cost $600,000, and made the problem worse
Only those extreme frequent ﬂyers bought it, leading to losses for AA
The price increase to $1,000,000 and losses were worse
Program was canceled in 1994


## Page 8

Real-World Examples
Health insurance in West Hollywood
In the 80s, it became impossible for young men to get health insurance in
West Hollywood
Market in that area disappeared, while in East Hollywood things were ﬁne
Issue: West Hollywood had a large concentration of gay men at risk of AIDS,
which was extremely costly to treat at the time and thus very costly to insure
Those with a higher willingness to get insured were the most costly customers
SafetyNet, IncomeAssure, and layoﬀinsurance
Provided as much as $9,000 to cope with unemployment upon being laid oﬀ
Problem: only those who knew it was very likely that they would be let go
bought the insurance policy
Again, these are the most costly customers to insure
These insurance products stopped being oﬀered


## Page 9

Real-World Examples
SafeGuard Guaranty and divorce insurance
Provided insurance that covered legal costs upon divorce
Came with 48 months waiting period
Only couples who put a high probability of divorce bought the product
Premium was so high that demand was low; product canceled within two years
Petplan and pet insurance
This type of insurance was almost inexistent a few years ago
Now it exists but it is quite expensive, especially for older dogs
For a ﬁfteen year old dachshund, it costs $650 per month, 70%
reimbursement, and $15,000 cap, no coverage for routine care
For younger ones it is cheaper but still capped at $15,000
Again, those who demand the product more are most costly to insure


## Page 10

Real-World Examples
Bidding and the winner’s curse
This is a variation on the adverse selection problem
Suppose you bid for a large contract and there are four other bidders
You estimate how much it will cost you to complete the project and submit a
bid based on that estimate and your conjecture about how the others will bid
Suppose your bid is the lowest one and you will the contract. You may suﬀer
from a winner’s curse
Why? Your bid was the lowest one, which means that you are the most
optimistic among all bidders regarding the completion cost of the contract
It is called a winner’s curse since if you are an unsophisticated bidder and bid
just based on your own estimate, you may end up with losses as the real cost
is likely to be higher than your estimate
Savvy bidders take this into account as follows: the bid is based not just on
your own estimate but also on the information that will be revealed if you win
the contract (that is, your cost estimate was the lowest)


## Page 11

Adverse Selection and Competitive Markets


## Page 12

A Market for Used Cars
Competitive market for used cars, with a large number of buyers and sellers
N sellers (N very large) and even larger number of buyers
Each seller has a used car, and only seller knows car quality
Quality of a car is θ ∈[θ, θ], θ ≥0, uniformly distributed over this interval
This means that there is an equal number of cars of each quality level
If θ ∈(θ, ¯θ), then the number of cars of quality at most θ is θ−θ
¯θ−θ N, and the
number of cars with quality above θ is
¯θ−θ
¯θ−θ N
If seller keeps the car, her payoﬀis θ, so she sells if and only if p ≥θ
A buyer’s utility for a car of quality θ is v(θ), where v(θ) ≥θ for all θ, and v
is strictly increasing and continuous
Buyer’s utility if he buys a car of quality θ and pays p is v(θ) −p
For concreteness, let us assume v(θ) = α + βθ, α ≥0 and β ≥0


## Page 13

Observable Quality Case
As a benchmark, consider the case in which buyers can observe θ
Then in this case the competitive market will work eﬃciently:
Separate market for each quality θ and an equilibrium price ˆp(θ) for each θ
More buyers than sellers in each market, and thus ˆp(θ) = α + βθ for all θ
All cars would be traded; allocation is eﬃcient
When θ is private information, things are more interesting
There will be a single price p∗for used cars (since buyers cannot distinguish
quality), so all cars traded are traded at that price


## Page 14

A Market for Used Cars
Let us derive the supply and demand for cars and the market equilibrium
Supply of cars xs(·): at each p, a seller with type θ sells iﬀp ≥θ, and so the
quantity of cars that will be oﬀered in the market at price p is
xs(p) =







1
if p ≥θ
p−θ
¯θ−θN
if θ < p < θ
0
if p ≤θ
The demand for cars is much more subtle, since buyers must infer from the
price p they observe what are the cars being oﬀered in the market
This way they can determine their willingness to pay for a used car


## Page 15

A Market for Used Cars
How do we calculate the demand for cars at a price p?
Note that at p, buyers understand that only sellers with cars whose quality
θ ≤p are willing to sell their car (those with θ > p prefer to keep it)
Thus, they infer than only qualities between θ and p are oﬀered in the market
Since they cannot observe the quality of any given car they buy, they calculate
the expected (average) quality of the car
Since the distribution of qualities is uniform, the average is θ+p
2
(check)
But since the utility that a buyer obtains from buying a car of quality θ is
v(θ) = α + βθ, it follows that the expected utility they obtain from buying one
of the cars available for sale at p is (check)
α + β
θ + p
2



## Page 16

A Market for Used Cars
It follows that a buyer will be willing to buy a car if and only if (why?)
α + β
θ + p
2

≥p
But then, the market demand for cars at price p is given by (check)
xd(p) =









0
if p > α + β

θ+p
2

[0, ∞)
if p = α + β

θ+p
2

∞
if p < α + β

θ+p
2

There is no demand at p above the expected utility of the average car oﬀered
in the market at p, inﬁnite demand at p strictly below that value (recall there
are lots of buyers), and any quantity at p exactly equal to that value


## Page 17

A Market for Used Cars
An equilibrium is a price p∗such that xs(p∗) = xd(p∗)
But we know buyers are willing to buy if and only if p∗≤α + β

θ+p∗
2

Since there are more buyers than sellers, price will settle at the highest value
consistent with this inequality
Thus, any p∗such that p∗= α + β

θ+p∗
2

is an equilibrium price
This is one equation in one unknown, p∗, and so the equilibrium price is
p∗= 2α + βθ
2 −β
What is the equilibrium quantity of cars oﬀered in the market?
q∗= xs(p∗) = p∗−θ
¯θ −θ N


## Page 18

A Market for Used Cars
Remarks:
Above we have implicitly assumed that β < 2, and that p∗≤¯θ
This is indeed the most interesting case
What if β ≥2? Then p∗≥¯θ and all the cars are sold
What if β < 2 but α large enough that p∗> ¯θ? Then equilibrium price is
again p∗≥¯θ and all the cars are sold
Note that in this case since all the cars are sold, the average quality of any
given car for a buyer is θ+¯θ
2
Thus, any buyer is willing to pay up to α + β θ+¯θ
2
What is the equilibrium price in this case? Since there are more buyers than
sellers, it follows that p∗= α + β θ+¯θ
2


## Page 19

A Market for Used Cars
Compared to the observable θ case, equilibrium is ineﬃcient when p∗∈[θ, θ)
since some cars are not traded despite the existence of gains to trade
The fraction
¯θ−p∗
¯θ−θ of the N cars will not be sold
Recall v(θ) = α + βθ > θ for all θ > θ, so there are gains to trade each θ
Thus, if buyers could observe the quality of any given car, there would be
trade at some price for each quality level
Economic intuition is that buyers understand that, given p, only an adverse
selection of cars in terms of quality is available in the market
As with externalities or imperfect competition, adverse selection is another
problem that can preclude the eﬃciency of competitive markets


## Page 20

A Market for Used Cars
Example: Market breakdown
Adverse selection can be so extreme that market might shut down
Assume that α = 0, β ∈(1, 2), and θ ∈[0, 2] uniformly distributed
Then the equilibrium price solves
p∗= α + β
θ + p∗
2

= β
2 p∗
But, since β
2 p < p for all p > 0, and the only equilibrium price is p∗= 0
Hence, essentially no car is traded in the market


## Page 21

Signaling and Screening


## Page 22

Some Remedies
Adverse selection can be a severe problem for transactions
A few (partial) remedies: information disclosure, signaling, and screening
Information disclosure:
Example: sellers might be legally mandated to disclose problems with the car
they sell; or they may voluntarily disclose that information if in equilibrium
everyone truthfully discloses the information they have
Signaling:
Example: seller of a high quality car could signal quality by allowing buyer to
inspect car or by oﬀering a warranty
Screening:
Example: buyer could design two contracts, one for a seller with a high quality
car that has a high price but also a generous warranty, and one for a seller
with a low quality car that has a low price but also a very limited warranty


## Page 23

Signaling
Informed party of “high quality” takes an action (signal) that would be too
costly for someone who is of “low quality”
Many examples of this sort:
Seller of a high quality used car can signal quality by letting buyer having their
own mechanic inspect the car, or by oﬀering a warranty
An entrepreneur with a high quality project might signal quality by keeping a
signiﬁcant stake in the project
Education (say university degree) can also serve as a signal of ability of worker
In all this cases, a party with a low quality good or with low ability would ﬁnd
it too costly to signal in this way
The uninformed party can infer quality, ability, etc., by observing the signal
(in some cases signal perfectly reveals quality, in other cases could be noisy)


## Page 24

Screening
Uninformed party designs a menu of contracts with diﬀerent terms that are
tailored to each individual quality, in a way that each individual takes the
contract designed to that individual’s private information
Many examples of this sort:
Buyer of a used car may approach a seller with a menu of contracts that a
seller can choose from, and by doing so reveal their information
An investor may approach an entrepreneur with a deal that they will buy a
stake in their project at a given price so long as the entrepreneur is willing to
keep a certain fraction of the project
Insurance companies (car, health, life, etc.) oﬀer a menu of policies consisting
of premium and coverage so that individuals of diﬀerent risk categories
self-select into the one design for their risk category
Companies like ATT, verizon, etc., design diﬀerent plans for diﬀerent
customers’ willingness to pay, and customers self-select
