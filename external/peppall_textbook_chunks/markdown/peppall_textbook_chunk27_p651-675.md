Auctions: Basic Theory and Applications 639


there are five people bidding for a vintage baseball card and that the value _vi_ that each
places on the card is, in increasing order: $100 _,_ $200 _,_ $300 _,_ $400 _,_ and $500. Let’s denote
the bid of each player as _bi_ . If each player adopts the rule _b_ i _b(vi)_ _vi,_ then in a second
price auction the winning bid will be _bi_ $500 _,_ and the winner will pay the second-highest = =
bid value of _bi_ $400. Likewise, in an English auction once the bid rises to an arbitrarily =
small amount above $400 = _,_ all bidders except the one with the highest valuation will have
exited. Once again, if all bidders follow the rule _b_ i _b(vi)_ _vi,_ that is, if all bidders bid
their true value, the card will go to the bidder with the highest valuation at a price equal to = =
second-highest willingness to pay, namely, $400 in this case.

A question that immediately arises then is whether it makes sense for each bidder to bid a
true valuation in both an English or second-price auction. Another way to put this is to ask
in these settings. To see that it does, it is helpful to recognize that in both the Englishwhether the strategy _bi_ = _vi_ for each player simultaneously constitutes a Nash equilibrium
and second-price sealed bid auctions, what one bids determines only whether or not one
wins—not what one pays.

Returning to our example, suppose realistically that bidders know their own valuation of
the baseball card but not the valuations of others. All a bidder knows in this latter regard
is that the other bids are drawn randomly from a very large pool of potential bidders,
each drawn from a uniform distribution with a range of $0 to $600. Now suppose again
that all bidders are following the strategy of bidding their true valuation so that _bj_ _vj_
for each. Can any one bidder alter her behavior in a way that improves her expected =
outcome?

To see that the answer is no, think about a specific bidder, such as bidder 4. Suppose
that she lowers her bid to $390—$10 below her valuation. Even without knowing the
other valuations, she can foresee that this will lead to one of two outcomes. One of these
is that all the other bidders had lower valuations and that the next highest bid was less
than $390. In this case, the change has no effect on her chances of winning or what she
pays. The other possibility is that she had the highest valuation but that the next highest
exceeded $390 _,_ e.g., $395. In that case, the fact that other bidders are bidding their true
valuations will mean that bidding $390 will result in bidder 4 losing the chance to buy a
baseball card she values at $400 for less than that amount. In short, bidder 4’s decision
to reduce her bid below $400 will definitely not lead to any gain and may result in a
possible loss.

The foregoing reasoning also applies to a decision by bidder 4 to raise her bid above
$400—say to $410. If the winning bid was greater than this amount, e.g., $500 _,_ then
again bidder 4’s increase to $410 has no effect. However, if the winning bid was between
$400 and $410 _,_ e.g., $405 _,_ then bidder 4’s decision to bid $410 will mean she buys the
baseball card at a price that exceeds her personal valuation. Once again, the choice to
alter her bid—this time to raise it slightly—cannot improve her outcome but may lead to
a loss.

We can repeat the foregoing analysis for each bidder. It then becomes clear that with all
other bidders following the strategy _bi(vi)_ _vi_ _i_ _j,_ the best response for bidder _j_ is to
= ; ̸=
bid her valuation and set _bj_ _(vj_ _)_ _vj_ _,_ as well. Thus, the symmetric Nash equilibrium in a
=
second-price sealed bid auction is for each player to submit a bid equal to her true valuation.
The winning bid will then pay an amount equal to the second-highest valuation. As noted,
this is also exactly what would happen in an oral English auction. These two auctions are
functionally equivalent.

Because the actual amount paid in English and second-price auctions is equal to the
second-highest valuation, it is interesting to determine what the expected winning price


640 Networks, Auctions, and Strategic Commitment


will be. For this purpose, we need the concept of an order statistic. For a random sample
of _n_ from a given population, the _k_ th order statistic is the value of the _k_ th smallest value.
For example, in our sample of _n_ = 5 bidders with valuations $100 _,_ $200 _,_ $300 _,_ $400 _,_ and
$500 _,_ respectively, the first order statistic _v(_ 1 _)_ is the smallest value, or $100. The second
order statistic is _v(_ 2 _)_ = $200. Because we know that both a second-price sealed bid auction
and an English auction both result in a winning payment equal to the second-highest
valuation among the sample of bidders, we can work out the expected winning bid for
any sample of size _n_ by working out the _n_ -1th order statistic, e.g., for a random sample
of five bidders, the expected actual payment is the expected fourth-smallest valuation or
the fourth order statistic _v_ (4). For the uniform distribution between 0 and _V_ _[Max]_ _,_ this is
given by:



_k_
Expected Value of _k_ th Order Statistic with Sample Size _n_ E[ _v(_ k _)_ ]
= = _n_ 1 _[V][ Max]_
+



(23.1)
Thus, for our five bidder case with bids drawn randomly from a uniform distribution with
a maximum valuation of _V_ _[Max]_ = $600 _,_ we would expect that in a sample of five, the
second-highest (fourth-smallest) value and therefore the price paid by the winning bidder







would be E[ _v(_ 4 _)_ ] =




4



6



$600 = $400. This is also the revenue that the seller of the



baseball card should expect.



Note that as the number of bidders rises, the relevant order statistic also increases. If
instead we had a sample of ten bidders drawn from this same uniform distribution, we
would be interested in the ninth order statistic or the expected value of _v_ (9). This would be







given by: E[ _v(_ 9 _)_ ] =




9



11



$600 = $490.91. For the general case of _n_ bidders drawn from



a uniform distribution ranging from $0 to _V_ _[Max]_ _,_ we have the expected winning price _p_ as
the _n_ -1th order statistic or:







E[ _v(n_ - 1 _)_ ] = E _(p)_ =




_n_ - 1

_n_ + 1



_V_ _[Max]_ _._ (23.2)





More bidders means that it is more likely that the pool will include buyers with very high
valuations. As a result, the expected price or revenue to the seller rises closer and closer to
the maximum valuation among all potential bidders.


as the price in the auction is less than your true value of the good.


23.2.2 Equilibrium Bidding Strategies in Dutch and First-Price Private
Value Auctions


We now turn to the Dutch descending auction and the first-price sealed bid auction. A little
thought quickly reveals that these two auction types are also equivalent because the essential
strategic choice is the same in each. In each case, bidder _i_ must decide on a strike price at


Auctions: Basic Theory and Applications 641


which he or she will claim the item. The remaining question is what that strike price or bid
should be. The answer is suggested by the central difference between our two broad auction
types—the Dutch and first-price auctions on the one hand, and the English and second-price
auctions discussed above, on the other. This difference is that unlike our earlier cases, the
price the bidder pays in either a Dutch or first-price auction _is_ determined by the bid he
makes rather than the next highest bid. This immediately rules out ever bidding more than
one’s valuation. Instead, the fact that bidders in a Dutch or first-price auction pay precisely
what they bid instead of the next-highest bid, suggests that they may want to shade their
bids a bit relative to bidders in an English or second-price auction. The issue then becomes
the extent of such shading. How far below their private valuation should bidders in a Dutch
or first-price sealed bid auction bid?

Let’s start by focusing on a sealed bid auction for the rare baseball card imagined above
but also by simplifying that example by assuming just two random bidders. Bidder 1
personally values the card at $200 while bidder 2 values it at $400. However, the bidders
only know their own valuation. As before, all bidder _i_ knows about bidder _j_ ’s valuation is
that it is drawn randomly from a uniform distribution ranging from 0 to $600. Because we
are explicitly interested in bidding rules that may yield a bid lower than the bidder’s true
valuation, we will consider proportional rules of the form _bi(vi)_ _λvi,_ where 0 _λ_ 1.
= ≤ ≤
When _λ_ 1 _,_ bidders bid their full valuation _bi_ _vi_ . For smaller values of _λ_ bids are only
a fraction of that valuation. = =

Suppose that both bidders choose _λ_ = 0.9 _,_ that is, each bids 90 percent of their true
valuation. Because these bids are strictly proportional to the underlying valuations, the
probability of having the highest bid is exactly the same as the probability of having
the highest valuation. For bidder 1, given her value of $200 and what she knows about
the distribution of her rival’s valuation, she can work out that she has a one-third chance of
being the highest bidder. Similarly, bidder 2 can determine that he has a two-thirds chance
of being the highest bidder. Is this a Nash equilibrium?

Consider bidder 1 first. Right now, she is bidding 0.9 _v_ 1 0.9 $200 $180. While
she does not know her rival’s valuation, she knows that her rival is also submitting a bid of = × =
0.9 _v_ 2. So, as noted, bidder 1’s chance of submitting the winning bid is one-third. Because
she only gains if she is the winner, bidder 1’s expected outcome E[Y1] in the current
setting is:


E[Y1] 0.3333 [$200 $180] $6.67 (23.3)
= ×    - =

Suppose now that instead of continuing to bid 90 percent of her valuation, bidder 1
reduces her bid still further, say to 80 percent. This has the advantage of greatly increasing
the gain if she is in fact the high bidder. However, she is now bidding sufficiently low
that her chance of being the high bidder has also fallen. With a little effort, we can in fact
determine how this tension works out.

By bidding only 80 percent of her valuation, bidder 1 reducers her bid to $160. Hence, if
she wins the auction, she now gains $40 instead of only $20. What is the probability with
which this happens?

To answer this question first note that if bidder 1 were to subit a bid of $160 when _all_
bidders including bidder 1 bid 90 percent of their valuation, it would imply that bidder 1
had a true valuation of _v_ 1 $160 _/_ 0.9 $177.78. In reality, this is not her true value. But
this thought experiment is nevertheless instructive. In a world in which all other bidders are = =


642 Networks, Auctions, and Strategic Commitment


bidding 90 percent of their true value, bidder 1’s decision to submit a bid equal to 80 percent
of her true $200 value gives her the same chance of winning as if she had continued to
bid 90 percent of her value but had a value of only $177.78. Specifically, her chance of
winning now given her rival’s strategy is $177.78 _/_ $600 = 0.296. As expected, this is a
lower chance than before, but this fall in the likelihood of winning is more than offset by
the increased gain of winning. Bidder 1’s expected outcome now is:


E[Y1] 0.296 [$200 $160] $11.84 (23.4)
= ×    - =

From this it is clear that the strategy combination of each bidder shading his or her bid to
90 percent of its true value is _not_ a Nash equilibrium. If bidder 2 were to do this, bidder 1
would do better by unilaterally reducing her bid to 80 percent of its true value. Moreover,
this result is symmetric. If bidder 1 were submitting a bid equal to 90 percent of her true
value, bidder 2 could likewise do better by shading his bid more deeply as well.

We have just seen that _λ_ = 0.9 is too high a proportional bid to be consistent with a
Nash equilibrium. It is pretty clear however that some choices of _λ_ would be too small.
For example if both bidders set _λ_ arbitrarily close to zero, either one could virtually assure
herself of winning the auction by increasing its bid a little while still enjoying a very sizable
gain after the auction is won. The issue is then whether we can find a _λ_ value that is neither
too small nor too large—one that if used by both bidders implies that neither can gain by
raising or lowering his or her bid a small amount. As it turns out, we can and for this simple
two-bidder case, the Nash equilibrium is for each bidder to submit a bid that is one half of
the true value, i.e., _b(vi)_ 0.5 _vi_ . In this case, the expected gain for each bidder is
=

E[Y1] 0.3333 [$200 $100] $33.33
= ×    - =

E[Y2] 0.6667 [$400 $200] $133.33 (23.5)
= ×    - =



To illustrate that _b(vi)_ = 0.5 _vi_ constitutes a Nash equilibrium for both bidders, we work
through the logic of our earlier example and ask whether a small rise in the bid of either
bidder would yield a gain given that the rival bidder continues to set _b(vi)_ 0.5 _vi._
=



Consider bidder 1. With _b(vi)_ = 0.5 _vi,_ she bids $100 so that $33.33 is her expected win.� 


= 0.367. Her gain







If she raises her bid to $110 _,_ her chances of winning rise to




110 _/_ 0.5



600



if she wins is then _(_ $200–$110 _)_ = $90. So, her expected win if she increases her bid to
$110 while bidder 2 still plays _b(vi)_ = 0.5 _vi_ is

E[Y1] 0.367 [$200–$110 _)_ $33 (23.6)
= × =

This is less than the expected win if she continues with the strategy _b(vi)_ 0.5 _vi_ .
=
Accordingly, it does not pay to raise her bid.



Now consider what happens if bidder 1 lowers her bid, say to $90. In this case, her







= 0.30. Her expected win as a result



chances of winning the auction fall to

becomes:




90 _/_ 0.5



600



E[Y1] 0.3 [$200–$90 _)_ $33 (23.7)
= × =

Just as she has no reason to raise her bid, bidder 1 has no reason to lower it either.


Auctions: Basic Theory and Applications 643



What about bidder 2? The same calculations show that he too has no reason to deviate
from the strategy _b(vi)_ 0.5 _vi,_ given that bidder 1 has not done so. With both bidders
=
setting _b(vi)_ = 0.5 _vi,_ he has a 0.67 chance of winning $200 for an expected payoff of $134.� 


= 0.733 _,_







If he raises his bid to $220 _,_ he will increase his chance of winning to




220 _/_ 0.5



600



but lower the gain from winning to $400–$220 = $180. His expected payoff now given
that bidder 1 still plays _bi(vi)_ = 0.5 _vi_ declines to



E[Y2] 0.733 [$400–$220 _)_ $132 (23.8)
= × =



Similarly, if bidder 2 lowers his bid to $180 _,_ his gain if he wins rises to $220 but his chances



= 0.60. Hence, his expected payoff in this case is again:







of winning fall to




180 _/_ 0.5



600



E[Y2] 0.60 [$400–$180 _)_ $132 (23.9)
= × =

As $132 again implies a fall in bidder 2’s expected gain, it appears that with two bidders
submitting sealed bids in a first-price auction, there is a symmetric Nash equilibrium in
which each bidder submits a bid equal to one-half of his or her private evaluation given that
the valuation of the rival bidder is drawn from a uniform distribution. We have not proven
this formally here (the proof is in the appendix), yet the heuristic analysis is compelling.
We therefore assert the result here. In particular, we assert that:


_If two bidders, each with a private valuation drawn randomly from an identical uniform_
_distribution, compete in a first-price, sealed-bid auction the symmetric Nash equilibrium_
_bidding strategy is for each bidder to bid exactly one half of his or her true value_, vi _, i_ . _e_ .,
_b(vi)_ 0.5 _vi._
=


What happens if there are more than two bidders? We already have some intuition
regarding the answer. In our discussion of English and second-price auctions we learned
that as the number of bidders increased, the bidding became more competitive and the
winning bid rose higher toward its maximum possible value. It is reasonable to assume that
that same competitive pressure also holds in Dutch and first-price auctions. It follows that
as the number _n_ of bidders rises above two, that we should expect to see bidders offering to
pay a higher fraction—choose a higher _λ_ value—as part of their bidding strategies.

As it turns out, the foregoing intuition is exactly right. As we show in the Appendix to
this chapter, for bidders in a first-price or Dutch auction, the optimal value of _λ_ for the
general case of _n_ bidders with independent private value drawn from a common uniform



distribution is _λ_ _[n]_ [ −] [1]
= _n_



distribution is _λ_ . Again, the proof is given in the appendix but the insight is
= _n_

reflected in the following result:



_In a Dutch or first-price auction with n bidders with independent private values vi drawn from_
_a common uniform distribution, the symmetric equilibrium bidding is for each bidder to submit_

_a bid given by_ : b _(_ vi _)_ _[(n]_ [ −] [1] _[)]_ _vi_ .
= _n_


Once again, it is useful to determine the expected winning bid or equilibrium price that
will be paid for the auctioned item. For this purpose, we recall the order statistics for


644 Networks, Auctions, and Strategic Commitment



the uniform distribution. Because both the winning bid and the actual payment are equal
to the highest bid submitted, the expected price is just equal to the bid generated by the
above equilibrium bidding strategy when applied to the _n_ th highest expected value _vi_ from
a random sample of _n_ bidders whose values are drawn independently from a uniform



_V_ _[Max]_ so







distribution ranging from 0 to _V_ _[Max]_ . That _n_ th smallest value is given by

that the expected winning bid or price is:




_n_
_n_ + 1







_V_ _[Max]_ =







��
_n_
_n_ + 1




_n_ - 1

_n_ + 1



E _(p)_ =




_n_ - 1

_n_



_V_ _[Max]_ (23.10)





one of eight bidders in this auction and the most you would be willing to pay for this hat is
$200. Show that your optimal strategy is to submit a bid of $175 _._


23.2.3 The Revenue Equivalence Theorem


We are now in a position to state what may be the most famous result in all of auction
theory. A comparison of equations (23.2) and (23.10) reveals that they are identical. That is,
the expected price ultimately paid by the winning bid in an English or second-price auction
is exactly the same as the expected price paid in either a Dutch or first-price auction. That is,
from the standpoint of the seller, all auction designs yield the same expected revenue. This
result, originally due to Vickrey (1961), is known as the Revenue Equivalence Theorem.
We have shown it here for the specific case of the uniform distribution. However, it is a
quite general result that holds across different distributions of individual private values. We
state this theorem below:

Revenue Equivalence Theorem: _Any auction in which the item goes to the highest bidder_
_and in which risk neutral bidders have private values drawn independently from an identical_
_and continuous distribution and in which the expected payment from a bidder with value 0_
_is 0, will yield the same expected revenue to the seller_ .

The Revenue Equivalence Theorem is a remarkable result. [5] It also applies when more
than one unit is being auctioned so long as each bidder wants only one unit and the auction
gives the _m_ units being sold to the _m_ highest bidders. There are, of course, important
situations in which Revenue Equivalence will not hold. In particular, it will not hold when
any of the assumptions on which it relies such as risk-neutrality are not satisfied. [6] Yet
in such cases it is precisely the ability of the theorem to identify the reason that revenue
equivalence fails that makes the theorem so useful.


5 The initial observations behind the theorem are due to Vickrey (1961). The formalization of the theorem
itself is typically credited to both Riley and Samuelson (1981) and Myerson (1981).
6 Recall that bidders in the first-price auction take some risk of being outbid by a lower-valuation bidder in
that each bidder shades his bid below his personal valuation. If bidders are risk averse, they will shade their
bids less (buy insurance with a higher bid), in such cases leading to a higher overall revenue in first-price
auctions.


Auctions: Basic Theory and Applications 645


23.3 COMMON VALUE AUCTIONS AND THE WINNER’S CURSE


In the baseball card example above, we assumed that each bidder had his or her own private
value of the card, independent of what other bidder’s valued it. This may well be the case
for certain heirloom items, memorabilia, or art objects and similar items. Yet for many
items, the ultimate worth to the buyer depends on how much the item can be sold for later,
i.e., on its worth to others. Thus, when two companies bid for drilling rights on a particular
tract of land, or the legal rights to a specific patent, and when two bidders bid for a jar with
an undisclosed amount of quarters in it or perhaps even for a vintage baseball card, what
they truly care about is the item’s true market value or the price at which it can be sold—a
common value for which each bidder may only have a private estimate.

For example, suppose that we again have _n_ bidders interested in buying a vintage baseball
card, not as a personal prize but as an investment. As a result, each is interested in the card’s
true market value _V_ [∗] _,_ which is a random variable. After doing some research, the bidders
obtain an estimate _vi_ of _V_ [∗] that is related to their estimate by an error _εI_ as follows:

_vi_ = _V_ [∗] + _εi_ (23.11)

where the _εi_ term is distributed uniformly from −$100 to +$100. This means that for any
bidder, _vi_ is an unbiased estimate of the true value _V_ [∗] : E _(vi)_ = _V_ [∗] + E _(εi)_ = _V_ [∗] . Each
bidder of course only sees _vi_ —not its decomposition into _V_ and _εi_ . Yet given that the

[∗]
expected value of _εi_ is 0, a bidder who receives information that the baseball card is worth
$400 _,_ i.e., one for whom _vi_ $400 _,_ can reasonably take this value as an unbiased estimate
of the true value _V_ [∗] . As a result, each bidder may well be tempted to bid up to the bidder’s =
observed _vi_ value in order to procure the card.

Unfortunately, bidding _vi_ is likely to lead to overpaying in these situations. This is
because the winner will be the bidder for whom _εi_ was greatest. In other words, the auction
winner will likely be one whose value estimate _vi_ included a large positive value of _εi_ .
When the true market value _V_ [∗] is revealed, this winner will discover that she has overpaid.
This phenomenon is known as “the winner’s curse.” The problem is that the bidder is
interested in more than just an unbiased expectation of _V_ [∗] _,_ which in fact is provided by her
observed _vi_ . What the bidder is really interested in is the expected value of _V_ [∗] _conditional_
_on her having the winning bid_ . It is clear in this regard that the winning bidder will be the
one whose individual estimate _vi_ included the highest value of the error term _εi_ . That is,
each bidder can foresee that if she wins, it will be because her _vi_ estimate was the most
optimistic and likely overstates the true market value _V_ [∗] . Rational bidders need to take this
into account and again shade their bids to minimize the winner’s curse.

Once again we can work out the optimal amount of shading using the order statistics.
Effectively, the _vi_ are random observations drawn from a uniform distribution ranging from
_V_ [∗] –$100 to _V_ [∗] + $100. We know that if there are _n_ bidders, the expected value of the
highest bidder’s observed _vi_ lies a fraction _n/(n_ + 1 _)_ of this distance from the lower bound.
That is:











E[ _n_ th order statistic] = _V_ [∗] - $100 +



$200












_n_
_n_ + 1



_V_
= [∗] 



_n_ + 1



_n_ + 1




_n_ - 1

_n_ + 1




_n_
_n_ + 1



$200 = _V_ [∗] +



$100 _._ (23.12)



$100 +


646 Networks, Auctions, and Strategic Commitment



Equation (23.12) says that, conditional on winning, each bidder can infer that he was the







highest of the _n_ bidders in which case his observed value _vi_ is




_n_ - 1



_n_ + 1



$100 above the true





value _V_ [∗] . Thus each bidder should shade his bid below _vi_ by this amount. If there are just
two bidders, this shading amounts to bidding $33.33. If there are three bidders, the optimal
shading rises to $50. It continues to rise with the number of bidders and asymptotically
reaches $100 _._

The reason that the optimal shading increases with the number of bidders is that the
winner’s curse does as well. When there are many bidders, the bidder who finds himself
with the top estimate _vi_ has a very good reason to believe his estimate is an outlier. By
analogy, consider a student in a classroom who wants to ask a question. If there are just a
few other students, the student might not be too worried about raising his hand. However,
if there are many students, the student might rationally infer that if it were a good question,
someone else would have asked it. By the same logic, it is natural for any bidder to take a
very high estimate of the baseball card’s true value with several grains of salt if there are a
lot of other bidders interested in it as well. [7]

Note that in terms of the impact of the number of bidders _n,_ the winner’s curse
phenomenon in common value auctions cuts against the insight of equation (23.10) that
large numbers lead to higher bids. Economists are naturally drawn to the idea that more
bidders means more competition and that this will bid prices up. When there is a “winner’s
curse” possibility, though, as there is in common value auctions, having many bidders can
work in the opposite direction to lower the equilibrium price. [8]


celebration. You and your partner decide to bid for the franchise. Including your partnership
there are eight groups bidding in the auction. Your market research on expected attendance,
hot dog consumption, and costs suggests that the franchise is worth $20 _,_ 000. You know that
this value is an unbiased estimate of the true value but that it includes an error distributed
uniformly between −$3000 and +$3000. What is your expected monetary “curse” if you
bid $20 _,_ 000 for the concession?


23.4 AFFILIATED VALUES


The private value and common value cases represent the two polar auction cases. The
intermediate case involves elements of both. Thus, to return to our baseball card analogy, it
is possible that each bidder has his or her own private value for the card but that this private
value is nevertheless influenced by the values assigned to the card by other bidders. This
seems the most realistic assumption for many cases. Even devoted art collectors who know
and love specific artists or styles will likely care about the resale value of their acquisitions
notwithstanding their passionate views on an item’s worth. Conversely, while homebuyers


7 Revenue Equivalence can still hold in a common value auction if buyers’ signals are completely
independent.
8 For examples in which the winner’s curse hedging is the dominant force, see Bulow and Klemperer (2002).


Auctions: Basic Theory and Applications 647


clearly care about the market value of their property, each may differ on the utility or
psychic income that a specific parcel yields depending on how much it “speaks” to them.

When the values of each bidder are affiliated, it means that it is a little unclear what we
mean by the bidder’s privately observed value because for any given signal, the true value
is known to be affiliated with others’ observed signals. As a result, there is some ambiguity
regarding what is meant by a bidding rule that says the bidder should bid her own valuation,
i.e., _bi_ _vi_ . A good rule of thumb however is that bidders should bid their valuation as if
the next highest bidder had observed the same signal. This will still lead to differential bids =
because each bidder observes her own individual signal or value _vi_ . Moreover, the fact that
the _vi_ are affiliated means that if one bidder observes a fairly high value or _vi,_ others are
more likely to observe high values as well. The winner’s curse effect may thus be mitigated
in affiliated auctions but it is not in general eliminated.

The selection bias that leads to the winner’s curse phenomenon means that whenever
players’ signals are not independent, revenue equivalence will not hold. It follows that if
some auction designs are better than others in reducing the winner’s curse, such auctions will
also lead to less shading and higher equilibrium prices. In this respect, both an open English
auction and a second-price auction are likely to lead to higher equilibrium prices than either
a Dutch of first-price auction. Further, an English auction is likely to yield a higher price
than a second-price auction. The intuition behind these results is straightforward. The open
English auction limits the winner’s curse because bidders can see the bids and therefore
infer the signals received by other bidders. This gives more probabilistic support to their
own estimated value and reduces the possibility that they will greatly overbid. Likewise, the
second-price or Vickrey auction helps to reduce the winner’s curse because as noted earlier,
the bid determines only whether one wins. What one pays is decided by the next highest
bid. So, some protection against the winner’s curse is already built into the auction process.
The reason that an English auction dominates or, at least, can never yield a lower price than
the second price auction is that it naturally includes the second-price mechanism in its final
stage. That is, after _n_ - 2 bidders have dropped and there are just two bidders remaining,
the open English auction is equivalent to the second-price auction with the winner paying a
price equal to the value at which the next-to-last bidder quits.

Incidentally, this seems like a good moment to make clear a vital point. The winner’s
curse is an outcome that _can_ happen—the winner will regret how much she paid—if bidders
are irrational and do not shade their bids properly. If bidders are rational however, they
will make the appropriate adjustments such that the winning bid will not be too high, on
average. The winner’s curse should not be a commonly observed event in real auctions. To
the extent that it is observed (recall that Didius Julianus totally lost his head in winning the
Roman Empire), it calls into question bidder rationality—not the rationality of the bidding
strategies analyzed here. [9]


23.5 AUCTIONS AND INDUSTRIAL ORGANIZATION


What are the implications of auction theory for industrial organization? The study of
auctions is a relatively new field. Despite Vickrey’s (1961) path-breaking early work, it is
only in the last twenty years that the applications of auction theory have begun to be widely


9 Thaler’s (1992) well-known piece renewed interest in the winner’s curse by providing evidence that it was
frequently real.


648 Networks, Auctions, and Strategic Commitment



![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/peppall_textbook_chunks/markdown/peppall_textbook_chunk27_p651-675_images/peppall_textbook_chunk27_p651-675.pdf-9-2.png)





understood. While the insights from auction theory for economic analysis are numerous
and growing, we focus here on two that are particularly relevant to industrial organization.
The first of these has to do with oligopoly pricing. The second has to do with market
asymmetries, perhaps most notably, those between an entrant and an incumbent.


23.5.1 Auctions and Oligopoly Pricing


Consider the simple Bertrand model, in which two firms sell an identical product. Let us
start with a simple case. There is a buyer willing to pay at most _V_ for exactly one unit of the
good and each firm has a constant and identical marginal cost _ci_ with 0 ≤ _ci < V_ . To make
matters specific, let us assume that _V_ $110 _, c_ 1 $10 _,_ and _c_ 2 $15. In this initial case,
we will assume that all of the foregoing is common information known to all participants. = = =
The market interaction then proceeds as follows. Each firm is asked to post a price at which
it will sell and the buyer chooses the firm that offers the lowest price. In this case, it is
easy to see that the Nash equilibrium requires that each firm will quote a price equal to
_c_ 2 $15. If either firm ever expected the other to quote a price above $15 _,_ say $16 _,_ the
=


Auctions: Basic Theory and Applications 649


other would win the competition by offering a price of $15.99. Yet this would mean that
the high-price firm would want to change its price quote, i.e., it would not meet the Nash
equilibrium criterion. Yet firm 2 will also never set a price below $15. If it does, it may
win the competition but it will lose money on the sale. The only possible Nash equilibrium
for this game is _p_ _c_ 2 $15 _,_ with firm 1 winning the bid. As is usual with Bertrand
pricing, we get price equal to the second-lowest marginal cost even though there are only = =
two firms. Indeed, adding a third or fourth with costs _c_ 3 $20 and _c_ 4 $25 would not
change the outcome. = =

Let us now, however, change the model slightly by altering the information structure. In
particular, let us assume that there are just the original two firms and that each firm knows
its own marginal cost _ci,_ but does not know the rival’s marginal cost. Instead, it knows
only that its rival’s marginal cost is distributed uniformly between 0 and $100. What price
should a firm post in this market setting?

The answer to this question comes from auction theory. The difference is that unlike the
analysis in Section 23.2, we are now considering a selling auction rather than a buying
auction. Nevertheless, the underlying principles are the same. Each firm will adopt a pricing
rule _pi_ _p(ci)_ that determines the price that will maximize its expected profit from the
sale of the one unit to be bought given the firm’s observed cost = _ci_ . We show below that the
pricing rule that achieves this outcome is:




[ −] _[c][i]_

[100][ +] _[ c][i]_
2 = 2



_p(ci)_ = _ci_ + [100] 2 [ −] _[c][i]_




_[i]_ (23.13)

2



Equation (23.13) says that in this duopoly case, each firm sets its price equal to its own
cost _ci_ plus an amount equal to half the difference between this cost and the maximum cost
_(_ $100 _)_ possible. This result is just the mirror image of our earlier work on bidding in a
second-price auction. The underlying logic is that this rule still implies that the firm with
the lowest cost will post the lowest price. It follows that the probability that firm _i_ wins the
sale is exactly the same as the probability that it has the lowest cost _ci._

In other words, if both firms follow the pricing rule, then


_prob(bi < bj_ _)_ = _prob(ci < cj_ _)_ ; _i_ = 1 _,_ 2; _i_ ̸= _j._

Given the uniform distribution of _ci_ between 0 and $100 _,_ this probability is equal to:



_prob(ci < cj_ _)_ [100][ −] _[c][i]_
= 100




[ −] _[c][i]_ 1

100 = - _[c][i]_




_[i]_

100 [;] _[ i]_ [ =][ 1] _[,]_ [ 2][;] _[ i]_ [ ̸=] _[ j.]_



The cumulative distribution of _ci_ at some value _c_ 1 is just the probability of the random
variable _ci_ being less than or equal to _c_ 1 _,_ and for the case at hand, this is given by _c_ 1 _/_ 100.
Therefore the probability of some randomly chosen _ci_ variable being greater than _c_ 1 is just
1 minus the cumulative distribution at _c_ 1 or 1– _c_ 1 _/_ 100 _._

For example, if firm 1 has a marginal cost of _c_ 1 $10 _,_ it would know that 90 percent of
the time its rival will be a firm with a higher marginal cost given that the marginal cost is =
distributed between 0 and $100. If both firms follow the pricing rule of equation (23.13),
this will also then be the probability with which firm 1 wins the sale. Recall that pricing
rule calls for firm 1 to set a price _p_ 1 $55 _,_ that is _(_ $100–$10 _)/_ 2 $45 above cost. Firm 1
will then have an expected profit E _(π)_ = of =

E _(π)_ = _prob(p_ 1 _< p_ 2 _)(p_ 1 − _c_ 1 _)_ = 0.9 _(_ $45 _)_ = $40.50 (23.14)


650 Networks, Auctions, and Strategic Commitment


Suppose instead that firm 1 set a price of $65. This will obviously increase its profit
margin but also decrease its chance of winning if firm 2 continues to follow the pricing
rule specified by equation (23.13). Specifically, by working that equation backward, we can
determine that if firm 1 sets a price of $65 _,_ it is acting as if its cost is $30. Firm 1’s chance
of winning the sale therefore becomes equivalent to the probability that its rival has a cost
greater than $30 _,_ namely, 70 percent. Hence, firm 1’s expected profit under this alternative
strategy becomes:


E _(π)_ _prob(_ $30 _< c_ 2 _)(p_ 1 _c_ 1 _)_ 0.7 _(_ $65 $10 _)_ $38.50 (23.15)
=    - =    - =


Similarly, if firm 1 decreased its bid to $50 _,_ it would be pricing as if it had a marginal cost
of _c_ 1 $0. It would raise its chance of winning the sale to 100 percent. Yet while it would
win with certainty, it would only earn $50–$10 = = $40 _,_ which is still less than the $40.50
earned using the optimal bidding strategy. In short, given that firm 2 is pricing according to
the rule specified in equation (23.13), the profit-maximizing choice for firm 1 is to follow
this rule as well. Obviously, the same is true in terms of firm 2’s best response if firm 1
follows that pricing rule. Thus, with each firm pricing as indicated by equation (23.13), each
will be making its best response to the other, i.e., the market will be in a Nash equilibrium.
While we have demonstrated this result here only by example, a general proof is provided
in the appendix.

There are a number of points worth noting about the Bertrand pricing equilibrium just
described. First, it generalizes to the case of _n_ = 3 _,_ 4 _,_ or more competitors. That is, for the
general case of _n_ firms the Nash equilibrium pricing rule is:




[ −] _[c][i]_

[100]
_n_ = _n_



_pi(ci, n)_ = _ci_ + [100] _n_ [ −] _[c][i]_




_[(n]_ [ −] [1] _[)]_
_n_ + _n_



_n_ _ci_ (23.16)



Thus, as the number of firms _n_ rises, the Bertrand pricing outcome now gets closer and
closer to the competitive outcome of _p_ = _c_ = marginal cost. Firms optimally reduce the
margin of their posted price over cost as they face more competitors.

Second, it is worthwhile to determine the expected price that will be paid in this Bertrand
market. For this purpose, it is helpful to recall the first two order statistics for the uniform
distribution between 0 and 100—the expected value of the lowest and second-lowest of _n_
random draws. These are:



_C_ [1] [100]
= _n_




[100] [200]

_n_ 1 [and] _[ C]_ [2][ =] _n_
+ +



(23.17)
_n_ + 1



Thus, with _n_ = 2 firms the lowest expected cost in our example is _C_ [1] = $100 _/_ 3 = $33.33
while the second-lowest expected cost is _C_ [2] = $200 _/_ 3 = $66.67. It follows that when
_n_ = 2 _,_ as in our example, we would expect _ex ante_ that the lowest cost firm would have
_ci_ $33.33. The pricing rule in (23.16) then implies that such firm would set a price equal
to = _(_ $100 + $33.33 _)/_ 2 = $66.67. Note that this expected price in the duopoly case is exactly
equal to _C_ [2] or the expected value of the second-lowest cost. This is no accident. It follows


Auctions: Basic Theory and Applications 651


directly from the Revenue Equivalence Theorem. If we were to hold a Dutch auction and
keep lowering the price until just one firm remained, we would expect that on average the
price at which one firm dropped out would be _C_ [2] = $66.67 _._

Moreover, this result generalizes to all values of _n_ . For example, when _n_ rises to 3, the
first order statistic falls to _C_ [1] = $25. In this case, the pricing formula of equation (23.16)
says that the expected market price is then:




_[(n]_ [ −] [1] _[)]_
_n_ + _n_




[2]
3 + 3



(23.18)
3 [$25][ =][ $50 when] _[ n]_ [ =][ 3]



_E(p, n)_ [$100]
= _n_




[1] _[)]_ _C_ [1] [$100]

_n_ = 3



From equation (23.17) we know that when _n_ = 3 _,_ the second order statistic _C_ [2] and the
expected winning bid = $200 _/_ 4 = $50 _,_ as well. We can repeat this for all values of _n_ .
However, simple algebra makes clear that with _C_ [1] = $100 _/(n_ + 1 _),_ the pricing formula of
equation (23.16) will always yield an expected winning price of _C_ [2] . Again, this is really
just an example of the Revenue Equivalence Theorem. The more important point here is
that even though we have Bertrand competition and identical products, we nevertheless get
a result in which the expected price generally exceeds the lowest marginal cost but moves
asymptotically closer to it as the number of firms _n_ rises. Market structure matters.


23.5.2 Auctions, Asymmetries, and Firm Rivalry


Thus far we have assumed that the bidders in auctions are symmetric. They may each realize
a different draw from a random distribution but each draws from the same distribution with
the same probabilistic parameters, and the price or payoff, conditional on that expectation,
is the same. Yet we know that in many real strategic settings, the players may not be equal.
For example, the gain to an incumbent firm from a new patent that partially replaces the
profit from its existing intellectual property may be less than the gain that the new patent
would yield to a new firm. Auction theory offers a powerful insight into the analysis of
these econometric cases as well. [10]

To understand the role of asymmetry, consider the following somewhat contrived but
revealing example. An incumbent, firm 1, dominates a local market but does face some
competition from a small, high-cost rival _R_ with a loyal following. More threatening to firm
1 is the potential entry of a highly efficient rival, firm 2. However, given the setup costs of
entering and establishing its own brand, firm 2 can only enter by buying the existing rival _R_
and transforming _R_ ’s operations with firm 2’s significantly more cost-effective technology
and management. The dominant incumbent can stop this, however, if it beats firm 2 to the
punch and acquires _R_ for itself. Hence, firm 1 and firm 2 will each be interested in buying
_R_ —the latter with a view to entering the market and the former with a view to blocking
such entry.

In bidding for _R_ each firm makes use of the information that it has on the benefits and
costs of successful entry. This information is structured as follows. Based on its years of
experience of actual market operations, firm 1 knows that it will lose at least _G_ 1 in profit if
firm 2 enters. However, it may lose an additional but uncertain amount _G_ 2 depending on


10 See Klemperer (1998) and Maskin and Riley (2000) for formal analysis of the role of asymmetry in
auctions.


652 Networks, Auctions, and Strategic Commitment


firm 2’s cost-effectiveness and marketing skills. From firm 1’s perspective, _G_ 2 is distributed
continuously between 0 and a large number. Conversely, firm 2 knows its cost-efficiency
and marketing skills and therefore knows that it will gain at least _G_ 2 if it enters. It may also
gain the (to firm 2) unknown amount _G_ 1 depending on key features of the market known
to firm 1. Here again, firm 2 knows only that _G_ 1 is distributed continuously between 0 and
a much larger value.

total includes a known partIn short, both firms face an expected gain of _G_ 1 and an unknown component _G_ 1 + _G_ 2 from buying _G_ 2 _,_ and reflects the profit gain _R_ . For firm 1, this
from keeping firm 2 out of the market. For firm 2 the total is comprised of an uncertain
amount _G_ 1 and a certain component _G_ 2. This total reflects the entrant’s potential profit
gains from successful entry. The firms bid for _R_ in an English auction and the bidding stops
when one firm drops out.

How much should each firm bid? It is straightforward to show that firm 1 should bid up
to 2 _G_ 1 while firm 2 should spend up to 2 _G_ 2. That this is a Nash equilibrium can be seen as
follows. Given that both firms are following this strategy, firm 2 will drop out (forego entry)
as soon as the required expenditure reaches 2 _G_ 2. If this happens, firm 1 will claim _R_ and the
total gainthis only happens when _G_ 1 + _G_ 2 for an expense of 2 _G_ 1 _> G_ 2. As a result, firm 1 will know that with this strategy _G_ 2. Given the hypothesized bidding rule however,
precisely becausecombination, any time that it wins the auction, it gains _G_ 1 _> G_ 2 whenever firm 1 wins. Analogously, firm 2 will know that if it _G_ 1 + _G_ 2–2 _G_ 2 = _G_ 1– _G_ 2 _>_ 0
wins it does so at a commitment of 2 _G_ 1. Yet for this to be a winning bid means that _G_ 2 _> G_ 1
there is no sense in either firmwhich, in turn, means that when firm 2 wins, it gains _i_ committing to a higher expenditure strategy as this will not _G_ 1 + _G_ 2–2 _G_ 1 = _G_ 2– _G_ 1 _>_ 0. Clearly,
increase its chances of winning when _Gi > Gj_ but will result in firm _i_ enjoying a smaller
gain when it does win. Likewise, there is no sense in either firm adopting a lower expense
strategy. This will only result in a lost opportunity for a net gain, on average. In this setting,
we should therefore envision an equilibrium in which each firm _i_ will bid up to 2 _Gi_ to buy
the target firm _R_ as a means of either invading or defending the market. The winning bid
will therefore be equal to 2 Minimum[ _G_ 1 _, G_ 2] _._
×

As structured, the entry game just described is a common value auction in which each
are symmetric in that there is no reason to believe that either one will consistently faceplayer has specialized information about a common value _G_ 1 + _G_ 2 but in which the bidders
an essentially different payoff. Because it is a common value auction, we know that any
bidding strategy combination that is sensible must somehow involve a degree of optimal
shading to avoid the winner’s curse. The shading here is reflected in the fact that once the
bid reaches say 2 _G_ 1 firm 1 will accede to firm 2’s entry even though firm 1 then knows, by
virtue of the very fact that firm 2 has pushed the bidding up to 2 _G_ 1 _,_ that _G_ 2 must be at least
as large as _G_ 1 and may well be larger. Nevertheless, firm 1 does not increase its bid any
higher than 2 _G_ 1 because, again, again, firm 1 (and firm 2 as well) is not interested in the
expected value of the total gain but that expected value conditional on its winning the bid.

Now consider one small change to the above scenario. Specifically, let us make use of
what we know to be generally true in entry games, namely that the gain to the incumbent
of keeping the entrant out exceeds the gain to the entrant of successfully coming into the
market. This extra gain does not need to be large. Indeed, the main point of the exercise is
to show that even a small asymmetry can have very large consequences.


Auctions: Basic Theory and Applications 653


A numerical example may help. Let us imagine that _G_ 1 and _G_ 2 both vary between 0 and
$25 (million), and that when firm 2 wins the bidding for _R_ it gains as before the sum,
_G_ 1 _G_ 2. However, due to the asymmetry, if firm 1 outspends firm 2, it gains _G_ 1 _G_ 2 $1
(million). How does this change the outcome? + + +

Suppose that firm 2 continues to bid up to the value 2 _G_ 2. In that case, the incumbent
firm 1 will find it advantageous to bid up to the value 2 _(G_ 1 1 _)_ (in millions). If firm 1
gainsandwins, it must be because _G G_ 1 1 + $19.05 million, firm 1 will bid up to 2 1 + _G_ 2 for a net gain of _G_ 1 + 1 _> G G_ 2. In this case, firm 1 buys1 + 1– _G_ 2 _> (_ $19.05 0. For example, if + 1 _)_ _R_ $40.1 million. Because at a price of 2 _G_ 2 = $20 million _G_ 2 and
_G_ 2 $20 million, firm 1 will win the bidding at a price of $40 million and gain $0.1 million. = × + =

If, however, firm 1 adopts the bidding rule of bidding up to 2 = _(G_ 1 + 1 _)_ for _R,_ firm 2
will quickly find that bidding 2 _G_ 2 is no longer optimal. The more aggressive bidding by
firm 1 now increases the winner’s curse facing firm 2. Suppose again that firm 1 knows
that _G_ 1 $19.05 million and therefore bids up to $40.1 million for _R_ . This time though,
let firm 2 know that = _G_ 2 $20.051 million and therefore bid up to $40.102 million. It will
find it gains only $19.05 = + $20.051 = $40.101 million, implying a loss of $0.001 million
or $1 _,_ 000. Firm 2 can avoid this loss and the enlarged winner’s curse by shading its bid
further. In particular, firm 2 should set its top bid equal to 2 _(G_ 2–1 _)_ . In that case, it will
Hence, this means that firm 2 will now pay 2only win ifof _G_ Unfortunately, the revised bidding strategy on firm 2’s part is not the end of the story.2– _G_ 1–2 _G >_ 2 0 if–1 _> G G_ 2 _> G_ 1 + 1 or1 + _G_ 2 _._ 2 _> G_ 1 + 2 _(G,_ given that firm 1’s top bid is 21 + 1 _)_ for a gain of _G_ 1 + _G_ 2 or a net gain _(G_ 1 + 1 _)_ .

This is because firm 2’s decision to bid less aggressively lowers the potential winner’s curse
for firm 1 and therefore encourages firm 1 to bid even higher. Specifically, if firm 2’s top
bid is 2 _(G_ 2–1 _),_ then firm 1 will now find it optimal to set a top bid of 2 _(G_ 1 2 _)_ . Firm 1
will then find that it wins the bid wheneverWhen it wins, firm 1 will gain _G_ 1 _G_ 2 1 for a payment of 2 _G_ 1 + 2 _> G_ 2–1 _,_ i.e., whenever _(G_ 2–1 _),_ and therefore a net + _G_ 1 _> G_ 2–3.
satisfied. In turn though, this more aggressive bidding by firm 1 will induce firm 2 to reducegain of _G_ 1– _G_ 2 + 2 + 1 _,_ which of course is positive whenever the condition + + _G_ 1 _> G_ 2–3 is
its bid for _R_ still further. Where will the process end?

It should be clear that firm 2 will never bid less than _G_ 2 to acquire _R_ . No matter what
firm 1’s bidding strategy is, firm 2 cannot lose with a winning bid of _G_ 2 because it knows
that the entry access that ownership of _R_ confers is always worth at least this much. Yet the
surprising logic of our analysis above is that in equilibrium, the small asymmetry that we
have assumed also means that firm 2 will never bid _more_ than _G_ 2. Any higher bid will put
it at risk. Thus, in the usual case in which the incumbent’s gain _G_ 1 asymmetrically exceeds
the entrant’s gain _G_ 2 _,_ the incumbent will have a strong advantage in bidding for _R._

There are two lessons from the foregoing example. First, the fact that asymmetries
transform common value auctions into almost-common value auctions, means that auction
design again becomes important in such settings. In particular, the Revenue Equivalence
Theorem will no longer hold necessarily.

The second insight, though, is the one more important one from an industrial organization
perspective. This is the fact that even small advantages can have major implications
for the outcomes in imperfectly competitive markets. Thus, the advantages of say
incumbency—even if they are small—may have a major effect not just for entry battles but
also for patent races, advertising rights, and a host of other non-cooperative games.


654 Networks, Auctions, and Strategic Commitment


23.6 EMPIRICAL APPLICATION: SCHOOL MILK AUCTIONS,
COMPETITION, AND COLLUSION


Each summer, public school districts around the country run an auction to solicit bids for
providing school lunch milk. Ohio is no exception to this rule. Unfortunately, Ohio is also
not an exception to the rule that school lunch auction bids often reflect collusion instead
of competition. The predictability and relatively inelastic demand for school milk coupled
with the homogeneity of the product, and therefore, the similarity of cost structures across
producers, facilitates collusive bidding. In addition, the fact that the districts announce the
identity of the winning bidder and the amount of the wining bid along with that fact that the
game is repeated each year so that any firm that does not cooperate can be punished soon
also make it easier to monitor and enforce collusive agreements. Consequently, it is not
surprising that collusion in school milk markets is relatively common, especially because
milk transport costs mean that the number of firms that could potentially serve a given
school district is typically small. Over the past twenty-five years, more than two dozen
states have launched investigations of price fixing in school milk auctions and guilty pleas
have been entered in over half of these cases.

Definitive legal proof of price-fixing is, however, difficult. Somehow, overt collusion
must be distinguished from the normal rivalry, which includes imperfect competition.
This is particularly true when conspirators engage in what is commonly referred to as
complementary or courtesy bidding. In such cases, the colluding firms submit bids to a
wide variety of buyer auctions in an effort to give the appearance of competition. In reality
though, the bids are deliberately set too high to provide any real competitive pressure
and thus allow the designated conspirator to win a particular auction at a high price.
Nevertheless, a sensible use of auction theory may help provide such compelling evidence.
Economists Robert Porter and J. Douglas Zona (1999) attempted to do just that and later
reviewed their findings in the paper “Ohio School Milk Markets: An Analysis of Bidding.”

The case investigated by Porter and Zona (1999) stemmed from state investigations
that led in 1993 to confessions by two Cincinnati dairies, Meyer and Coors Brothers, to
participation in bid-rigging schemes. Executives from both companies described a collusive
bidding ring that included a third Cincinnati dairy, Louis Trauth, in which different school
districts were allocated to each specific dairy with the other two dairies agreeing to submit
bids so as to give the appearance of competition but bids that, in actuality, were excessively
high bids so that the chosen dairy would still win the bidding with a profitable price. In
other words, the Myers and Coors executives described a standard case of complementary
bidding. Despite the confessions of Myers and Coors, Trauth maintained its innocence.
The case then proceeded as the state of Ohio pursued collusion charges against a number
of dairies.

Porter and Zona (1999) review bids from the roughly sixty different firms in 509
Ohio school districts over the eleven years, 1980–90. With these data, they construct a
control group of the vast majority of dairy distributors and processors presumed innocent
of any bid rigging. They then attempt to identify collusive bidding by testing for any
differences between the actual bidding practices of Meyer, Coors, and Trauth and the
bidding practices that these firms would have exhibited if they behaved like the competitive
control group firms.

Porter and Zona (1999) break the bidding process into two steps. First, there is the
decision simply to submit a bid. That is, each supplier has to determine whether or not to
submit a bid to any particular district. Second, conditional on submitting a bid to a particular


Auctions: Basic Theory and Applications 655


district, the firm has to determine how much to bid, i.e., what price it should ask for should
it indeed be the winning bidder.

The authors therefore start by using data from the control group to estimate a model
of the probability that a specific district receives a bid from a specific firm in a particular
year. Their findings may be briefly summarized as follows. First, processing firms that
actually transform raw milk into a finished product are more likely to submit bids to any
given district than are distributor firms that simply distribute processed milk. Second, all
milk sellers are more likely to submit bids in one direction from their base rather than in
multiple directions. Third, all sellers are more likely to submit bids in a nearby districts
rather than ones far away. Finally, fewer bids are submitted to those districts requiring that
complementary goods such as straws be provided along with the milk.

Turning to the price quoted in the bid given that a bid is submitted, the most important
finding is that the level of the bid rises as the distance between the bidder and the district
increases. However, Porter and Zona (1999) also find that distributors tend to submit higher
bids than do processing firms and that bids that have an escalator clause allowing for the
price to increase over the life of the contract, are also lower.

All of the foregoing results are quite plausible. Because processors often serve many
milk demands, they have more routes and therefore a greater likelihood of serving a route
that includes a school. Similarly, it is easier to serve schools that lie along an existing
route structure that runs, say, from east to west, rather than to serve a school along a new
route running from, say, south to north. Because transport costs are very significant, it makes
sense that firms will tend to submit bids in closer districts. Likewise, because providing
straws and other services (e.g., coolers) is expensive, districts that require these items
should also expect to get fewer bids.

The bid level results are also consistent with expectations. Again, the presence of
significant transport costs implies that a dairy firm’s bid should rise the further the dairy has
to transport the milk to delivery. Because distributors buy their milk from processors, one
would again expect that distributors would ask for a higher price, all else equal. Finally,
if a firm is protected against cost increases over time by means of an escalator clause, we
would expect that the firm can submit a lower bid free from any need for a premium to
protect against such risk.

In sum, there is ample reason to suspect that the behavior of the control group captures
the normal workings of Ohio’s imperfectly competitive school milk markets. In light of
these results, Porter and Zona (1999) then seek to determine whether and in what ways the
behavior of the three main alleged conspirators—Meyer, Coors, and Trauth—is different
from that of the control group.

Table 23.1 demonstrates one clear difference. Relative to the typical dairies in the
control group, the three accused firms submit bids much more frequently in nearby
markets—markets not far from any of the firms. Thus, the third row of the table indicates
that considering districts twenty to thirty miles from the dairy’s office, Coors submits 22.9
percent more bids, Meyer submits 18.5 percent more bids, and Louis Trauth submits 20.6
percent more bids than would the typical competitive firm draws from the control group
analysis. Moreover, many of these differences are statistically significant.

The true importance of the foregoing finding though only emerges when Porter and Zona
(1999) investigate the actual prices that the accused firms submit when they do bid. In
contrast to the behavior of the control group firms, the delivered milk prices offered by
the three Cincinnati firms _fall_ with distance. That is, these firms tend to offer a lower milk
price to school districts farther away even though shipping milk this distance incurs much


656 Networks, Auctions, and Strategic Commitment


**Table 23.1** Accused conspirators’ difference in bidding propensity from
control group by distance


_Distance in Miles_ _Coors Brothers_ _Meyer_ _Louis Trauth_


0–10 24.1% _>_ 5.6% _>_ 7.0% _>_
10–20 42.9% _>_ 8.2% 15.2% _>_
20–30 22.9% _>_ 18.5% _>_ 20.6% _>_
30–40 −17.1% _<_ 18.6% _>_ 0.1%
40–50 −9.5% _<_ −2.2% −4.3%
50–60 −6.0% −5.5% 6.9%
60–70 −6.0% −18.6% _<_ 47.1% _>_
70–80 −4.9% _<_ −25.0% _<_ 10.0% _>_
80–90 −2.4% _<_ −17.5% _<_ −2.5% _<_
90–100 −1.7% −7.7% _<_ 11.8% _<_
100–110 −1.3% 30.7% _>_ 8.7% _>_
110–120 −0.6% 0.5% −4.2% _<_
120–130 −0.5% −0.9% −3.6% _<_
130–140 −0.2% −0.3% −2.0%
140–150 −0.2% −0.1% −1.2%

_>_ Indicates statistical significance


higher transportation costs. This pattern is especially evident for Meyer and Trauth who, as
Table 23.1 shows, were the two of the three firms who submitted a lot of bids far away.
Taken together then, these findings reveal a pattern in which the Coors, Myer, and Trauth
submitted lots of bids in school districts close to their home town of Cincinnati where they
were in most direct competition. These bids were relatively high while the prices offered
to more distant school districts were noticeably lower. This of course is very consistent
with the practice of complementary bidding to which the Meyer and Coors executives
had confessed.

In addition to the above finding, Porter and Zona (1999) also offered further evidence
of bid rigging. First, the bids of the indicted conspirators were significantly lower in 1983
and 1989, the two years in which the Meyer and Coors executives testified that there was
a breakdown in the cartel. More formally, Porter and Zona (1999) examine two correlation
measures among the accused firms. Briefly put, if the three firms are truly submitting bids in
an independent fashion, then the fact that, say, Meyer bid unexpectedly in a particular district
should be totally uncorrelated with whether either Coors or Trauth also bid unexpectedly
in that district. However, complementary bidding would imply that these unexpected bids
would be positively correlated. In agreement with Meyer and Trauth, Coors would submit
bids in the same districts these firms did more often than not. Similarly, independence
would imply that in a district in which say, Coors submitted an unexpectedly high price,
we would not expect the bids of either Meyer or Trauth to show any pattern. In contrast,
a complementary bidding scheme would suggest that in such districts, Meyer and Trauth
would, if they bid at all, also submit bids that are unexpectedly high.

Porter and Zona (1999) therefore also consider the correlation between: 1) the unexpected
bid propensity measured as the unexplained residuals for the three firms from the regression
predicting their bidding submission; and 2) the unexpected level of the bid again measured


Auctions: Basic Theory and Applications 657


**Table 23.2** Pair-wise correlation coefficients on unexplained propensity to bid and unexplained
bid price


_Coors & Myer_ _Meyer & Trauth_ _Trauth & Coors_


Propensity to Bid 0.58 0.54 0.43
Bid Price 0.66 0.67 0.54


as the unexplained residuals now taken from the pricing equation estimated for the three
firms. Table 23.2 displays the pairwise correlations for each case.

As Table 23.2 indicates, the correlations are all positive and in each case, the estimated
correlation is significantly different from zero. In districts where one of the three firms
unexpectedly submitted a bid, the other two were statistically very likely to do the same.
Further, when bidding, if one of the three firms submitted an unexpectedly high bid, the
others were very likely to do so as well. Coupled with the earlier evidence, these findings
strongly reject the hypothesis of independent bidding. They are instead very consistent with
the complementary bidding scheme that was alleged.

Overall, Porter and Zona (1999) estimate that on average, the collusion raised
prices by 6.5 percent over what they otherwise would have been. For some school
districts—particularly those in which one of the three alleged conspirators already had a
contract and in which therefore the other two were strongly encouraged not to undercut
that incumbent’s prices—the bid-rigging is estimated to have raised school milk prices by
as much as 49 percent.


**Summary**



The common use of auctions for all sorts of market transactions raises many important questions.
One of the most important is the impact of auction
design. That is, are the market outcomes different
for English or Dutch or first-price or secondprice sealed-bid auctions? Vickrey’s (1961) pathbreaking work provides a key answer. His main
result, typically referred to as the Revenue Equivalence Theorem, is that the expected price or
revenue is the same under each auction design
_provided_ that the bidders’ values are independent.

Apart from auction design, auctions also differ
depending on whether the item(s) being sold has
only a purely private value or, instead, a common
value that will be revealed after the auction is
completed. A common value auction—in which
the item(s) being sold ultimately have a true market value common to all bidders but unknown to
any bidder prior to the bidding—has the potential
for a “winner’s curse.” Bidders in auctions for
real estate, oil tract rights, radio spectra, and so
on know that their signal or guess as to what the



item is truly worth is based on the information
that they happened to observe. Therefore, any
bidder who wins a common value auction can
infer that he or she must have had the most optimistic signal or estimate of the item’s true market
value. Unless bidders shade their bids below the
value implied by the information they have they
will find that they have paid more than the item’s
true value. If bidders shade their bids optimally,
they will avoid the “winner’s curse” of paying
too much in a common value auction.

When the signals of bidders are affiliated, the
potential for a “winner’s curse” and other features imply that auction design does matter. In
general, the ranking is that an open English or
ascending auction leads to a higher price than
does a second-price auction. In turn, a secondprice auction yields a higher selling price than
does a first-price, sealed bid auction.

Auction theory offers many insights for
industrial organization analysis. It provides an
alternative interpretation of the Bertrand price


658 Networks, Auctions, and Strategic Commitment



competition model in which the number of competitors does matter. It also makes clear how
market asymmetries can have a lasting impact on
market outcomes.

Equally important, auctions markets are subject to the same industrial organization influences
as are other markets. In such markets, there
still remains the temptation for firm imperfect competitors to collude. Examination of the


**Problems**


1. Suppose that there are six bidders in an
English auction for an antique 1950s Vaporizer. Each has his or her own private value
for the vintage machine. In ascending order,
these values are $50 _,_ $60 _,_ $70 _,_ $80 _,_ $90 _,_ and
$100. What will be the winning bid?
a. What will be the winning bid if the
highest three bidders collude?
b. What will be the winning bid if the
middle three bidders collude?


2. Imagine that you are an educational consultant and that you have been asked to submit
a bid for a month-long project by a small
liberal arts college. You know that the college’s willingness to pay for your service
is uniformly distributed between $5,000 and
$15,000. Assuming that you have other earning opportunities for that month for which
you would be paid $5,000, what should you
bid?


3. In a “war of attrition” two bidders with valuations drawn independently from the same
uniform distribution ranging from 0 to $10 _,_
bid for an object but in this case, _both_ pay
the losing bid. Derive the equilibrium for this
game. [Hint: Use the Revenue Equivalence
Theorem.]


4. The wallet game is a well-known common
value auction. In this game, two players are
each given a chance to bid for a total amount


**References**


Cary, E. 1960. _Dio’s Roman History: Translation_

_by Earnest Cary_, London: J. Heineman.
Bulow, J., and P. Klemperer. 2002. “Prices and

the Winner’s Curse,” _Rand Journal of Eco-_
_nomics_ 33 (Spring): 1–21.



auction markets for school milk in Ohio using
standard microeconomic concepts to determine
non-collusive bidding strongly implies that some
firms in Ohio did collude. They bid too much,
too high, and offered bids that declined with distance despite the fact of very high transport costs
for processed milk. In short, auction theory has
become an important part of both the theory and
practice of industrial organization.


equal to the sum of the money they are carrying in their wallets. For example, if the
amount in player 1’s wallet _w_ 1 is $20 and
the amount in player 2’s wallet _w_ 2 is $45 _,_ the
total prize is $65. Of course, each bidder only
knows the amount in his or her own wallet.
Player 1 knows _w_ 1 and player 2 knows _w_ 2.
Show that each player following the bidding
rule _b(wi)_ = 2 _wi_ is a (Nash) equilibrium.

5. Up until the 1990s, the US Treasury has
auctioned off its debt instruments of Treasury bills and notes using a discriminatory
format. Under this procedure, the supply of
securities would be auctioned off in lots at
different prices until the available supply was
purchased. That is, bidders submit bids indicating both the price they will pay and how
many securities they wish to buy at that price.
In response, the Treasury fills the demand of
the highest priced bidder first. It then moves
on to the demand of the second-highest bidder, and so on until all the supply of Treasury
securities is sold. However, in the 1990s the
Treasury moved to a uniform price auction in which roughly the above procedure
was followed except that now, all bidders
paid the same price—namely the lowest
price at which the supply cleared. Why
might the uniform price auction have encouraged more bidders to participate in Treasury
auctions?


Klemperer, P. 1998. “Auctions with Almost

Common Values: The Wallet Game and Its
Applications,” _European Economic Review_
42: 757–69.


Auctions: Basic Theory and Applications 659



Klemperer, P. 2003. “Why Every Economist

Should Learn Some Auction Theory,” in
_Advances in Economics and Econometrics_
(Volume 1 of Eighth World Congress—
Econometric Society Monograph), M. Dewatripont, L. Hansen, and S. Turnovsky, eds.,
25–35. Cambridge: Cambridge University
Press.
Krishna, V. 2010. _Auction Theory_, 2 _nd edition_ .

Amsterdam: Elsevier.
Loertscher, S. 2008. “Market Making
Oligopoly,” _Journal of Industrial Economics_
56 (June): 263–89.
Maskin, E., and J. Riley. 2000. “Asymmetric

Auctions,” _Review of Economic Studies_ 67
(July): 439–54.
Myerson, R., 1981. “Optimal Auction Design,”

_Mathematics of Operations Research_ 6 (February): 580–73.


**Appendix**



Porter, R., and J. D. Zona. 1999. “Ohio School

Milk Markets: An Analysis of Bidding,” _Rand_
_Journal of Economics_ 30 (Summer): 263–88.
Riley, J., and W. Samuelson. 1981. “Optimal

Auctions,” _American Economic Review_ 71
(June): 381–92.
Scarre, C., 1995. _Chronicle of the Roman Emper-_

_ors: The Reign-by-Reign Record of the Rulers_
_of Imperial Rome_, London: Thames & Hudson.
Thaler, R. 1992. _The Winner’s Curse: Paradoxes_

_and Anomalies of Economic Life_, New York:
Simon & Schuster.
Vickrey, W. 1961. “Counterspeculation, Auc
tions, and Competitive Sealed Tenders,” _Jour-_
_nal of Finance_ 16 (March): 8–37.



OPTIMAL BIDDING IN FIRST-PRICE AUCTIONS



We show that optimal bidding in a sealed-bid first price auction with _n_ bidders with
valuations _vi_ drawn from a uniform distribution ranging from 0 to _V_ _[Max]_ is for each bidder



_i_ to bid _bi_ = _[(n]_ [ −] _n_ [1] _[)]_



_n_ _vi_ . We assume that any equilibrium bidding rule _b(vi)_ adopted by all



bidders must imply _b(vi) > b(vj_ _)_ if _vi > vj_ _,_ i.e., the bidder with the highest value _vi_ will
have the highest bid. Bidder _i_ ’s expected gain is then:



Prob _(vi > vj_ for _j_ = 1 _, n_ and _j_ ̸= _i)_ × [ _vi_ - _b(vi)_ ] (23.A1)



Uniformity implies that the probability that any randomly drawn valuation will have
a value less than _vi_ is _vi/V_ _[Max]_ . In a sample of _n_ bidders with independent valuations� _vi_ - _n_ −1

the probability that all of the _n_ 1 valuations are below _vi_ is . Hence, any
             - _V_ _[Max]_

admissible bidding rule _b(v)_ in (23.A1) implies:



the probability that all of the _n_ - 1 valuations are below _vi_ is




_vi_



_V_ _[Max]_




- _n_ −1




[ _vi_ _b(v)_ ] (23.A2)
 



- _n_ −1



Expected Gain for Bidder _i_ =




_v_
_V_ _[Max]_



Taking the derivative with respect to _v_ and setting it to zero at _v_ = _vi_ we have:



_b_ [′] _(vi)_ 0 (23.A3)
=



_n_ 2

         - _)_

[ _vi_ - _b(vi)_ ] _(n_ - 1 _)_ _(V_ _[(v][Max][i]_ _)_ _[n]_ [−][1] [−]




_vi_



_V_ _[Max]_




- _n_ −1



Simplifying, we than obtain the differential equation:



_vi_







_vi_











(23.A4)



_b_ [′] _(vi)_ _(n_ 1 _)_
=   




1 − _[b]_


660 Networks, Auctions, and Strategic Commitment


For which the solution is readily confirmed to be:







_b(vi)_
=




_n_ - 1

_n_



_vi_ (23.A5)



When _n_ 2 _,_ each bidder bids an amount equal to 0.5 _vi_ . As _n_ grows ever larger, bidding
=
becomes more competitive. In the limit, _bi_ ⇒ _vi_ as _n_ ⇒∞ _._


OPTIMAL BIDDING IN OLIGOPOLISTIC BERTRAND
COMPETITION WITH INCOMPLETE INFORMATION



We assume _n_ firms competing in price to sell a good for whom the consumer has valuation
_V_ and each firm has cost _c_ i drawn from a uniform distribution ranging from 0 to _C_ _[Max]_ . The








- _n_ −1



probability that _c_ i is the lowest cost is



1 _ci_
 - _C_ _[Max]_



. Given a pricing function _p(ci)_ that



preserves this ranking, firm _i_ ’s expected net gain is:




[ _p(c)_ _ci_ ] (23.A6)
  



- _n_ −1



E _(_ Gaini _)_
=





_c_
1
 - _C_ _[Max]_



Therefore, the optimal pricing function must satisfy:



_p_ [′] _(ci)_ = _[(n]_ _C_ [ −] _[Max]_ [1] _[)]_




- _n_ −2




[ _p(ci)_ _ci_ ] (23.A7)
   




_c_
1
 - _C_ _[Max]_








- _n_ −1





1 _ci_
 - _C_ _[Max]_



Simplifying equation (23.A7) then yields:


_(n_ 1 _)_ [ _p(ci)_ _ci_ ] _p_ [′] _(ci)_ [ _C_ _[Max]_ _ci_ ] (23.A8)
  -   - =   
The pricing function that satisfies this differential equation for all permissible values of
_ci_ is:







_p(ci)_ = _[C][Max]_ _n_ +




_n_ - 1

_n_



_ci_ (23.A9)


# **24** **Strategic Commitments and International Trade**

The first US Secretary of the Treasury was the brilliant but prideful Alexander Hamilton
whose picture still adorns the US ten-dollar bill. Hamilton came to his position just as the
new country was struggling with a host of financial issues accumulated from its long war
for independence and the somewhat chaotic financing that had thereafter characterized the
eight years under the Articles of Confederation. Of crucial importance to Hamilton was
the young country’s international profile. He was convinced that America had to establish
its identity in international markets. In particular, Hamilton argued forcefully that America
had to raise sufficient taxes to pay off its accumulated foreign debt and eliminate any fear
of default. Yet Hamilton’s vision did not stop there. He also had a very clear idea about
the sort of taxes that would best serve the United States in its quest for a respected place
in the international community. In Hamilton’s view, the United States had to have an
internationally competitive manufacturing sector. Therefore, in his _Report on Manufactures_
(1791), Hamilton argued strongly for tariffs on manufacturing imports. This would help
raise the revenue necessary for debt service and, by discouraging imports, encourage
the development of US manufacturing that Hamilton viewed so central to the country’s
future economic success. In fact, he also recommended the establishment of a Society for
Useful Manufactures to subsidize certain key industries that he saw as critical to a vibrant
manufacturing sector.

The issues raised by Hamilton’s analysis have carried forward to this day. As this text is
going to press, the countries of the Euro zone are struggling with the issue of credible debt
reduction. Simultaneously, countries around the globe are concerned about the trade policies
that will best insure the health of their manufacturing sector, especially in light of the rapid
emergence of manufacturing bases in China and other newly industrialized nations.

As it turns out, these issues have a significant industrial organization component. The
gains from strategic trade policy depend critically on both the element of commitment that
they introduce into trade models and also on the nature of competition in those trade sectors.
In this chapter, we use the tools developed earlier to explore industrial competition in an
international context. [1]


1 Many authors have contributed to the strategic trade literature. Central contributions include Spencer
and Brander (1983), Brander and Spencer (1985), Eaton and Grossman (1986), and Krugman (1986).
Fudenberg and Tirole (1984) offer a classic analysis of strategic commitment.


662 Networks, Auctions, and Strategic Commitment


24.1 STRATEGIC COMMITMENTS IN INTERNATIONAL
MARKETS


We begin with a simple numerical illustration. Assume that Boeing and Airbus are the only
two international producers of large passenger aircraft. Assume that each is considering a
major investment in the development of a new super jumbo jet capable of carrying over 500
passengers. Both recognize that the size of the jet may make it economical but also limit its
market to routes connecting airports that have both the demand for and the facilities needed
to handle such a large passenger load. As a result, there is really only room for one firm to
develop the aircraft successfully. If a firm sinks the development costs and is not the firm
to survive it will suffer a major loss. This is illustrated in Table 24.1 below in which all
payoffs are in millions of Euros.

As can be seen, this simple game has two Nash equilibria. In one of these, Airbus develops
the new superjumbo jet. In the other, Boeing does. Absent some explicit coordination or
other device, there is no way to determine which of these two equilibria will prevail. We
could imagine a probabilistic equilibrium where each firm develops the new plane with
a probability of, say, one-third, but does not with a probability of two-thirds. Instead,
however, let’s assume that the European Union commits to financing Airbus’s R&D in the
amount of 3.5 billion. With this change, the payoff matrix is now that of Table 24.2.

Now Airbus has a dominant strategy, namely, to develop the new aircraft. The Nash
equilibrium therefore becomes one in which Airbus develops the plane and Boeing stays
out of the race. As a result, Airbus earns a surplus of 9500 _million_ . Assuming these funds
accrue to Europeans, the Union as a whole has gained from its commitment to Airbus. The
subsidy of 3500 million has been worthwhile.


24.1.1 Strategic Subsidies in an International Cournot Model


To investigate the role of R&D subsidies more formally, suppose that there are two
countries, A and B, in each of which there is a domestic monopoly firm, _a_ and _b_,
respectively. However, while firms _a_ and _b_ do not compete with each other in their
home markets, they do compete in other markets which we shall simply designate as the


**Table 24.1** The strategic R&D game without subsidies

|Col1|Col2|Boeing|Col4|
|---|---|---|---|
|||_Don’t Develop_|_Develop_|
|Airbus|Don’t Develop|0,0|0, 6000|
|Airbus|Develop|6000_,_ 0|−3000_,_ −3000|



**Table 24.2** The strategic R&D game with a subsidy for airbus


|Col1|Col2|Boeing|Col4|
|---|---|---|---|
|||_Don’t Develop_|_Develop_|
|Airbus|Don’t Develop|0,0|0, 6000|
|Airbus|Develop|9500_,_ 0|500_,_ −3000|


Strategic Commitments and International Trade 663


international market. Demand in this market is given by _P_ = _A_ - _Q_, and each firm has a
constant marginal cost _c >_ 0. Hence, from Chapter 9 we know that the equilibrium quantity
and profit of each firm are: _q_ 1 _q_ 2 _(A_ _c)/_ 3; and _πa_ _πb_ _(A_ _c)_ [2] _/_ 9.

Now imagine that firm _a_ persuades its government to subsidize its costs to the extent of = =  - = =  _s_ per unit. As a result, firm _a_ now faces a reduced constant marginal cost of _c_ - _s_ . Its profit
function will therefore be:


_πa_ _(A_ _qa_ _qb_ _c_ _s)qa_ (24.1)
=  -  -  - +

As we saw in Chapter 9, firm _a_ ’s best response function is now:



_qa_ = _[(A]_ [ −] 2 _[c]_ [ +] _[ s)]_




_[c]_ [ +] _[ s)]_

2 - _[q]_ 2 _[b]_




_[b]_ (24.2)

2



Of course, because it receives no subsidy, firm _b_ ’s best response function is given
by equation (24.2) with _s_ = 0. Combining these two equations, we then have the new
equilibrium outputs in the international market:



_qa_ = _[(A]_ [ −] _[c]_ 3 [ +][ 2] _[s)]_




_[c]_ [ −] _[s)]_ _Q_ [2] _[(A]_ [ −] _[c)]_ [ +] _[ s]_

3 ; = 3




_[c]_ 3 [ +][ 2] _[s)]_ ; _qb_ = _[(A]_ [ −] 3 _[c]_ [ −] _[s)]_




_[c)]_ [ +] _[ s]_ _P_ _[A]_ [ +][ 2] _[c]_ [ −] _[s]_

3 ; = 3



(24.3)
3



In turn, this implies that firm _a_ earns profit:

_πa_ = _[(A]_ [ −] _[c]_ 9 [ +][ 2] _[s)]_ [2] (24.4)



In the absence of any subsidy, _s_ = 0 and firm _a_ earns the standard Cournot duopoly profit

[2]



_πa_ = _[(A]_ [ −] 9 _[c)]_ [2]



. Therefore, the profit increase _�π_ for firm _a_ that the subsidy generates is:
9



_�π_ _[(A]_ [ −] _[c]_ [ +][ 2] _[s)]_ [2]
= 9




[ +][ 2] _[s)]_ [2]

9 - _[(A]_ [ −] 9 _[c)]_ [2]




_[c)]_ [2] [4] _[(A]_ [ −] _[c)s]_ [ +][ 4] _[s]_ [2]

9 = 9



(24.5)
9



The total cost _TC(s)_ of the subsidy is _s_ times the number of units firm _a_ produces. Hence:




[ +][ 2] _[s)]_ [3] _[(A]_ [ −] _[c)s]_ [ +][ 6] _[s]_ [2]

3 = 9



_TC(s)_ _s_ _[(A]_ [ −] _[c]_ [ +][ 2] _[s)]_
= 3



(24.6)
9



Hence, the net benefit of the subsidy _NB(s)_ is:


_NB(s)_ _�π_ _TC(s)_ _[(A]_ [ −] _[c)s]_ [ −] [2] _[s]_ [2] (24.7)
=    - = 9


The subsidy should of course be chosen so as to maximize the net benefit shown in
equation (24.7). A straightforward application of calculus then yields the optimum per unit
subsidy _s_ [∗] :


_s_ [∗] _[A]_ [ −] _[c]_ (24.8)
= 4


