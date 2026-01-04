414 Contractual Relations Between Firms


reliance on documented cost savings as a justification of a merger. With this change,
the antitrust authorities have indicated an increased willingness to judge a merger to be
pro-competitive if it generates cost savings that are likely to translate into lower consumer
prices. As we have already noted, however, most analysis finds that the cost savings
necessary to generate lower prices are substantial. Hence, the full implication of the 1997
cost efficiencies amendment is yet to be seen.

We should also note that merger-generated cost efficiencies are not necessarily completely
beneficial once entry possibilities are considered. If a merger generates lower marginal
costs, then any potential entrant will know that _if it enters_ price competition will be
relatively fierce. If the entrant has fixed costs, this will mean that the market will need to be
larger for entry to be profitable. In other words, for a given market size, merger-generated
cost efficiencies make post-merger entry less likely. Thus, cost savings can have two price
effects. One is the downward pressure on prices exerted by lower costs while the other is
the upward pressure exerted by the reduced likelihood of rival entry. Cabral (2003) shows
that it is possible that the former outweighs the latter.


15.7 EMPIRICAL APPLICATION: EVALUATING THE IMPACT OF
MERGERS WITH COMPUTER SIMULATION


In recent years, the important new tool of merger simulation has emerged to assist with
the evaluation of mergers. Merger simulation as pioneered by Werden and Froeb (1994,
2002) and extended recently by Epstein and Rubinfeld (2002) works in two steps. The
first is to obtain relevant information on such variables as firms’ costs, prices, and demand
elasticities, among others. This is usually accomplished with the aid of modern econometric
techniques. The second step is to use this evidence to run computer-simulated models of the
market in question both before and after a proposed merger. In effect, merger simulation
allows economists to conduct laboratory experiments to examine a merger’s likely effects.
While not necessarily conclusive, such experiments can be very helpful as an evaluative
tool.

To understand merger simulation better, consider an industry with four firms, each of
which produces a differentiated product and competes in prices against its rivals. For any
one firm, the first-order condition for profit maximization is effectively the Lerner condition.
That is,



_pi_ _c_
 
_pi_




[1]
+ _ηii_



= 0 _i_ = 1 to 4 (15.41)



Here, _ηii_ is the (negative of) the elasticity of the firm _i_ ’s demand with respect to its own
price. If we denote the price-cost margin term as _µi_ firm _i_ ’s market share as _si_ and then
; ;
multiply through by the elasticity of demand, equation (15.41) becomes:


_si_ _siηiiµi_ 0 (15.42)
+ =

If two firms merge, however, the first-order condition will change as we saw in Section
15.5. Now, the merged firm will coordinate the prices of its two separate products by
taking account of the cross demand effects between the two products. Specifically, assume


Horizontal Mergers 415


that firms 1 and 2 merge. Then it is straightforward to show that for the merged firm, the
first-order condition is:


_s_ 1 _s_ 1 _η_ 11 _µ_ 1 _s_ 2 _µ_ 2 _η_ 21 0
+ + =

_s_ 2 _s_ 2 _η_ 22 _µ_ 2 _s_ 1 _µ_ 2 _η_ 12 0 (15.43)
+ + =

where _ηij_ is the cross-elasticity of good _i_ with respect to the price of good _j_ . It is clear
from equations (15.42) and (15.43) that measures of the own and cross-price elasticities for
each good are critical to estimating the impact of a proposed merger. Indeed, once these
elasticities are known, it is relatively straightforward to work out the implied post-merger
equilibrium and, therefore, the post-merger prices.

In order to estimate the elasticities, one needs a model of market demand. One commonly
used model is derived from what is referred to as the Almost Ideal Demand System (AIDS)
as first described by Deaton and Mulbauer (1980). Essentially, such a system describes the
demand facing each firm as a function of its own price and the prices charged by other
firms, similar to the linear demand that we used to describe our initial model of Bertrand
competition with differentiated products. In the case of our four-firm example above, a
conventional approach would be to describe market demand with a system of equations
something like the following:



_s_ 1 = _a_ 1 + _b_ 11 ln _p_ 1 + _b_ 12 ln _p_ 2 + _b_ 13 ln _p_ 3 + _b_ 14 ln _p_ 4

_s_ 2 = _a_ 2 + _b_ 21 ln _p_ 1 + _b_ 22 ln _p_ 2 + _b_ 23 ln _p_ 3 + _b_ 24 ln _p_ 4

_s_ 3 = _a_ 3 + _b_ 31 ln _p_ 1 + _b_ 32 ln _p_ 2 + _b_ 33 ln _p_ 3 + _b_ 34 ln _p_ 4

_s_ 4 = _a_ 4 + _b_ 41 ln _p_ 1 + _b_ 42 ln _p_ 2 + _b_ 43 ln _p_ 3 + _b_ 44 ln _p_ 4 (15.44)



The _bij_ coefficients in the above system are directly linked to the demand elasticities
needed to run the merger simulation. Thus, econometric estimation of those coefficients is
the first step in obtaining a simulated outcome.

Not counting the _ai_ coefficients or intercepts, this still leaves 16 _bij_ coefficients to estimate
even in our small four-product example. In general, unless some restrictions are imposed
on the nature of the own and cross-price effects, there will be on the order of _n_ [2] coefficients
to estimate in a general _n_ -product demand system of the type illustrated above. This is a
rather large number of estimates to make with any degree of precision. To simplify matters,
it is common to impose restrictions that reduce the number of parameters to be estimated
directly.

For example, suppose that our four-firm example is characterized by q1 250 q2
100 q3 100 and q4 50 _,_ or _s_ 1 50 percent; _s_ 2 _s_ 3 20 percent; and _s_ 4 = 10 percent.; =
One way to proceed is to calibrate the model under the assumption of proportionality. As; = ; = = = = =
developed by Epstein and Rubinfeld (2002), Proportionally Calibrated AIDS (PCAIDS)
assumes that the output loss for good 1 caused by an increase in _p_ 1 will be allocated to the
other products in proportion to their market shares. Suppose that the overall elasticity of
market demand _η_ = −2 and the own price elasticity of good 1 is _η_ = −4 _._ If we think of
the overall industry price as the share-weighted average price across the four firms, then a
1 percent increase in firm 1’s price _p_ 1 translates into a [1] _/_ 2 percent increase in the industry
price, all else equal. Firm 1’s price increase will then reduce industry output by [1] _/_ 2 of 2
percent, or by 1 percent, which in this case is five units. Firm 1’s own output will fall by 4


416 Contractual Relations Between Firms


percent, or ten units. Thus, five of these ten units will be picked up in the demand for the
other firms if the net industry demand decline is to be just five units. The proportionality
assumption is that [0.2 _/(_ 0.2 + 0.2 + 0.1 _)_ ] × 5 or 2 units will be diverted to each of firms 2
and 3, while the remaining one unit will be diverted to firm 4. Note that this implies that
a 1 percent increase in firm 1’s price will raise the demand at each of the other firms by 2
percent, i.e., the cross elasticities _η_ 21 _, η_ 31 _,_ and _η_ 41 are −2 in each case.

What we have just shown is that with the proportionality restriction, the knowledge of
just the market demand elasticity and firm 1’s own price elasticity has permitted us to
deduce three other of the elasticity measures needed for simulation. As it turns out, we can
go much farther. In fact, the proportionality assumption permits the complete derivation
of all the relevant elasticities once the elasticity is known for the market and for one firm.
To put it slightly differently, knowing the market elasticity and own-price elasticity of
one firm permits complete calculation of all the _bij_ coefficients in equation (15.44). The
proportionality assumption reduces the number of parameters to be estimated from _n_ [2] to
just 2. Once that estimation is complete, we may use the resulting elasticity and market
share data to solve the first-order conditions in (15.42) and (15.43) for both the pre-merger
and post-merger market. We can then evaluate the price effects of the merger.

Of course, proportionality is a strong assumption. Other techniques for simplifying
the estimation procedure also exist. Unfortunately, which technique is chosen can affect
the predicted post-merger price change by a factor of ten, as Slade (2007) in particular,
has emphasized. Moreover, even if proportionality is assumed there are still two elasticity
parameters to be estimated. There is ultimately no way to avoid the use of some econometric
analysis in the merger evaluation process.

Efforts to estimate the relevant parameters from a demand system such as the one in
(15.44) are tricky at best. Even if only a few parameters are required, there remain difficult
measurement questions. And while the specification in (15.44) is common it is not the only
way to structure market demand. Alternative specifications will imply different functional
forms and cross-product elasticity restrictions that in turn will have different effects on the
post-merger equilibrium. For example, the linear demand function that we use in most of
the examples in this text implies that demand becomes more elastic as prices rise. This
imposes a constraint on post-merger prices even if a merger raises market power because
it means that consumers become increasingly sensitive to such price increases. In contrast,
a log-linear demand function implies a constant price elasticity of demand that will yield a
notably higher price rise for the same market power increase. Yet it is often far from clear
what precise specification is most appropriate.

A firm’s market share will depend heavily on the definition of the market employed. Yet
as we can see from the first-order conditions (15.41–43), these share values are crucial to
understanding market dynamics. Indeed, they are crucial to understanding whether or not
the merger raises antitrust concerns in the first place.

The difficulties posed by the econometrics in merger analysis were dramatically illustrated
by the proposed 1996 merger of two office superstore chains, Staples and Office Depot. [24]

Along with Office Max, the merging firms dominated the office superstore retail market.
Of course, these three firms are not the only retailers of office supplies. While Staples and
Office Depot had between 70 and 75 percent of the market defined by office superstores
alone, their combined share of the retail sales of office supplies by all stores, including large


24 For a more complete discussion of the econometric evidence in this case, see Ashenfelter et al. (2004).


Horizontal Mergers 417


discounters such as Wal-mart, drug store chains, and stationary stores, was probably under
10 percent. Accordingly, the question of whether the merger even crossed the threshold of
concern established by the Merger Guidelines had to be addressed.

Moreover, even within the category of office superstores, market definition remains
problematic. In the Staples case, it was widely agreed that there was not one national market
but many local ones. In principle, this means that estimation of a demand structure like that
in equation (15.44) would have to take the specific nature of each localized market into
account. That is, account would need to be taken of variation across locations in the extent
of competition. How should this variation be modeled?

The government argued that the local market boundaries were those of the Metropolitan
Statistical Area (MSA) used by the Census Bureau. For any Staples store, competitors
included all other Office Depot and Office Max stores in the same MSA. In contrast, the
merging firms argued that there was a difference within an MSA depending on the actual
distance between rivals. That is, an Office Depot store exerted greater price pressure on a
Staples store if it were only five miles away than if it were ten, or twenty miles away. Again,
these seemingly small changes in specifying the competitive interaction can (and did) have
a large effect on the results. Just this one alteration led to more than a 3 percentage point
difference between the firms’ prediction that the merger would raise prices by about 0.8
percent and the government’s estimate of a rise of 4.1 percent. Together, these and other
modest econometric modifications meant that the range in predicted price increases varied
from less than 1 percent to almost 10 percent.

In short, simulating merger effects inevitably requires different estimation techniques and
structural demand assumptions that vary according to the conceptualization of the market
environment. Assumptions to ease the estimation burden do not alleviate other measurement
and econometric issues. We can expect self interest to lead each side in a merger case to
choose the framework and associated econometric techniques that yield parameter values
and other evidence most favorable to its own objective. Unfortunately, it is typically the
case that each approach has some objective justification. It becomes very difficult even for
economists to separate the truth from self-interest in interpreting the results. It is even more
difficult for the courts to resolve such debates. One of the striking features of the Staples
case is that the final court decision never mentions the econometric evidence despite the
fact that this case probably involved more econometric presentation than virtually any prior
merger litigation.


**Summary**



Horizontal mergers are combinations of firms
that are rivals within the same industry. Because
they result in the joining of firms that were
previously competitors, horizontal mergers raise
obvious antitrust concerns. Such mergers may,
in fact, be a means to create a legal cartel. One
major puzzle in economic analysis is the merger
paradox. This paradox reflects the fact that many
commonly used economic models suggest that
a merger is not profitable for the merging firms
and that the true beneficiaries of a merger are the
nonmerging firms.



The clue to resolving the merger paradox is
to find some means of credibly committing the
newly merged firm to a profit-enhancing strategy.
One way to do this in quantity-setting models is
to permit the merged firm to take on the role of
Stackelberg leader whose increased production is
credible. Another way is to consider merger decisions sequentially. Either of these approaches is
capable of generating profitable mergers that also
have adverse consequences for consumers. The
sequential merger approach can also help explain
the “domino effect” often observed, by which a


418 Contractual Relations Between Firms


merger of two firms in an industry is quickly
followed by similar marriages among other firms
in the same industry.

The merger paradox does not arise in markets where firms offer differentiated products and
compete in price for customers. In these markets,
the merging firms can easily make a convincing commitment to specific locations or product
designs—namely, those used by the firms before
they merged. The ability to make such a commitment is sufficient to make merger profitable.

Theambiguouseffectsofmergersfoundineconomic theory are also found in empirical analysis.
To date, there is little clear evidence that horizontal mergers have resulted in legalized cartels with
significantmonopolypower.Instead,whatisclear
is that the combination of theoretical and empirical ambiguity has led the legal authorities to take
a much less aggressive and much less rigid stand
against proposed mergers, a point to which we
return in the policy discussion of the next chapter.

Policy also increasingly includes formal
attempts to model the post-merger market and
to evaluate mergers on a case-by-case basis. The
theory behind this approach builds on the first

**Problems**


For problems 1, 2, 3, and 4 consider a market
containing four identical firms, each of which
makes an identical product. The inverse demand
for this product is _P_ = 100 − _Q,_ where _P_ is
price and _Q_ is aggregate output. The production
costs for firms 1, 2, and 3 are identical and given
by _C(qi)_ = 20 _qi_ ; _(_ i = 1 _,_ 2 _,_ 3 _),_ where _qi_ is the
output of firm _i_ . This means that for each of
these firms, variable costs are constant at $20
per unit. The production costs for firm 4 are
_C(q_ 4 _)_ _(_ 20 _γ )q_ 4 _,_ where _γ_ is some constant.
= +
Note that if _γ >_ 0 _,_ then firm 4 is a high-cost
firm, while if _γ <_ 0 _,_ firm 4 is a low-cost firm



_(_ | _γ_ | _<_ 20 _)_ . Note also that _Q_ =



�4



_i_ =1



_qi._



1. Assume that the firms each choose their
outputs to maximize profits given that they
each act as Cournot competitors.
a. Identify the Cournot equilibrium output for each firm, the product price, and
the profits of the four firms. For this to
be a “true” equilibrium, all of the firms



order conditions for profit maximization and uses
these along with the estimates of the relevant
price elasticities to analyze the optimal pricing
decisions of the merged firm and its rivals in the
post-merger market. In practice, this is hard work
and typically requires a number of simplifying
assumptions to identify the needed parameters.
However, there appears to be little alternative.

In sum, there is no general rule regarding the
impact of mergers. The merger paradox suggests
that only mergers that are associated with large
cost efficiencies will be profitable. Because firms
do not pursue unprofitable opportunities, this
suggests that any proposed merger must have
very large cost efficiencies and, perhaps, should
be approved. On the other hand, we know if
merged firms can acquire the ability to commit to
a production level before others, then the merger
can be profitable without cost savings and thus,
would be anticompetitive. Antitrust authorities
cannot rely solely on economic theory to determine whether or not a specific merger should
be challenged. This is an area where empirical
work based on advanced econometrics can be
predicted to play an important role.


must at least be covering their variable costs. Identify the constraint that
_γ_ must satisfy for this to be the case.
b. Assume that firms 1 and 2 merge and
that all firms continue to act as Cournot
competitors after the merger. Confirm
that this merger is unprofitable.
c. Now assume that firms 1 and 4 merge.
Can this merger be profitable if _γ_ is
positive so that firm 4 is a high-cost
firm? What has happened to the profits
of firm 2 as a result of this merger?


2. Now assume that each firm incurs fixed
costs of _F_ in addition to the variable costs
noted above. When two firms merge the
merged firm has fixed costs of _bF_ where
1 ≤ _b_ ≤ 2 _._
a. Suppose that firms 1 and 2 merge and
that _γ >_ 0. Derive a condition on _b, F,_
and _γ_ for this merger to be profitable.
Give an intuitive interpretation of this
condition.


b. Suppose by contrast that firms 1 and 4
merge. Repeat your analysis in (a).
c. Compare the conditions derived in (a)
and (b). What does this tell you about
mergers that create cost savings?


3. Assume that if two firms merge, the merged
firm will be able to act as an industry leader,
making its output decision before the nonmerged firms make theirs. Further assume
that _γ_ = 0 so that the firms are of equal
efficiency.
a. Confirm that a merger between firms
1 and 2 will now be profitable. What
has happened to the profits of the nonmerged firms and to the product price
as a result of this merger?
b. Confirm that the two remaining firms
will also want to merge and join the
leader group given that the leaders act
as Cournot competitors with respect to
each other (hint: this merger will create a leader group containing two firms
and a follower group containing none).
What does this second merger do to the
market price?


4. Continue with the conditions of question 3
but now suppose that for a merger to be
undertaken, the merging firms each have
to incur a fixed cost, _f_ (this might include
costs of identifying a merger partner, negotiating the terms of the merger, legal fees,
and so on).
a. How high must _f_ be for the merger
between firms 1 and 2 to be unprofitable?
b. How high must _f_ be for the subsequent merger between firms 3 and 4 to
be unprofitable?


5. In this chapter it was shown that for a twofirm merger to be profitable, the following
condition must be satisfied:



Horizontal Mergers 419


a. Assume that the number of firms in the
market is ten, that is, N = 10 _,_ and that,
as in question 4, a two-firm merger
requires that each of the merging firms
incurs a fixed cost of _f_ prior to the
merger. Derive a relationship, _f (L),_
between _f_ and the size of the leader
group, _L,_ such that if _f > f (L),_ the
two-firm merger will be unprofitable.
Calculate _f (L)_ for _L_ = 1 _,_ 2 _,_ 3 _,_ 4 _,_ and
5 to confirm that _f (L)_ is decreasing in
_L_ . Interpret this result.
b. Now assume that there are eight firms
in the market, that is, _N_ = 8. Repeat
your calculations in part (a) to show
that the function _f (L)_ rises as _N_ falls.
Interpret this result.

6. Normansville consists of a single High
Street that is one mile long and has 100
residents uniformly located along it. There
are three independent video rental stores
located in the town at distances 1/6, 1/2, and
5/6 of a mile from the left-hand edge of Normansville. Each resident rents one video per
day provided that the price charged is no
more than $5. If a consumer is located _s_
miles from a store, the transport costs of
getting a video from that store is $0.50 _s_ .
Suppose first that the two stores do not price
discriminate.
a. What rental charge will the three stores
set given that they act as price competitors?
b. What profits do they earn?

7. Suppose that two neighboring stores in Normansville merge.
a. What does this do to prices and profits?
b. Recalculate your answers to and 7(a)
assuming that the stores can perfectly
price discriminate.

8. Recall that the first-order condition for
maximizing profit may be written as:



_(A_ _c)_ [2]
_l_ _[L][(N]_ [ −] [1] _[, L]_ [ +][ 1] _[)]_ [ =] 
_B(L_ 2 _)_ [2] _(N_



_π_ _[L]_



_B(L_ + 2 _)_ [2] _(N_ - _L_ - 1 _)_



_p_ _[ε]_ [−][1]
= _ε_



_p_ _c_ where _ε_ is the absolute
= _ε_ ;

value of the firm’s elasticity. Show that
this result implies that, as an approximation, the proportional change in a
firm’s price as a result of a merger can



_(A_ _c)_ [2]
_f_ _[F]_ _[(N, L)]_ [ =][ 2] 
_B(L_ 1 _)_ [2] _(N_




_>_ 2 _.π_ _[F]_



_B(L_ + 1 _)_ [2] _(N_ - _L_ + 1 _)_ [2]



be written as: _[�][p]_




_[h]_ _[�][c]_

_h_ _c_

[+]



_c_

[;][ where]



Assume as in questions 1 and 2 that
A = 100 _,_ B = 1 _,_ c = 20. Further assume
that _γ_ = 0 _._



_h_ _[ε]_ [ −] [1]
= _ε_




_[p]_ _[�][h]_

_p_ _h_

[=]



. Suppose that as a result of a
_ε_


420 Contractual Relations Between Firms



merger and decline in competitive pressure, a firm’s demand elasticity falls by the
proportion _δ,_ i.e., _[�][h]_ _ε_ [′] = _(_ 1 − _δδ)ε_ . Show that



(i.e., the value of _[�][c]_

_c_ [), for the firm’s price]
not to rise if its initial elasticity is _ε_ = 2 _,_
and if as a result of a merger, its demand
elasticity falls by 10 percent, i.e., _δ_ = 0.1.
That is, by what proportion will costs have
to decline in this case to keep _p_ constant?



we may write _[�][h]_




_[h]_ _δ_

_h_ [=] _(_ 1 − _δ)ε_ - 1 _[.]_



9. Use your results in question 8 to determine
the necessary degree of cost efficiencies



**References**


Andrade, G., M. Mitchell, and E. Stafford. 2001.

“New Evidence and Perspectives on Mergers,” _Journal of Economic Perspectives_ 15
(Spring),: 103–20.
Ashenfelter, O., D. Ashmore, J. Baker, S. Glea
son, and D. Hosken. 2004. “Econometric
Methods in _Staples_,” in Princeton Law & Public Affairs Paper No. 04-007.
Baker, J. 2004. “Efficiencies and High Concen
tration: Heinz Proposes to Acquire Beech-Nut
(2001)” in J. Kwoka and L. White, eds. _The_
_Antitrust Revolution_, Oxford: Oxford University Press, 150–69.
Brito, D. 2003. “Preemptive Mergers Under

Spatial Competition,” Working Paper, FCT,
Universidade Nova de Lisboa.
Cabral, L., 2003. “Horizontal Mergers with Free

Entry: Why Cost Efficiencies May Be a Weak
Defense and Assets Sales a Poor Remedy,”
_International Journal of Industrial Organiza-_
_tion_ 21 (May): 607–23.
Daughety, A. F. 1990. “Beneficial Concentration,” _American_ _Economic_ _Review_
80:1,231–7.
Deneckere, R. and Davidson, C. 1985. “In
centives to Form Coalitions with Bertrand
Competition”, _Rand Journal of Economics_ 16
(Winter): 473–486.
Deaton, A., and J. Mulbauer, 1980. “An Almost

Ideal Demand System,” _American Economic_
_Review_ 70 (June): 312–26.
Epstein, R., and D. Rubinfeld, 2002. “Merger

Simulation: A Simplified Approach with New
Applications,” _Antitrust Law Journal_ 69:
883–920.
Farrell, J., and C. S. Shapiro, 1990. “Horizontal

Mergers: An Equilibrium Analysis,” _American_
_Economic Review_ 80:107–26.
Fauli-Oller, R. 200. “Takeover Waves.” _Jour-_

_nal of Economics & Management Strategy_ 9
(Summer), 189–210.



Gandhi, A., L. Froeb, S. Tschantz, and G.

Werden. 2008. “Post-Merger Product Repositioning.” _Journal of Industrial Economics_ 41
(March), 49–67.
Greenhut, J., G. Norman, and M. L. Green
hut. 1991. “Aspects of Airline Deregulation,”
_International Journal of Transport Economics_
18:3–30.
Hotelling, H. 1929. “Stability in Competition,”

_Economic Journal_ 39 (January): 31–47.
Judd, K., 1985. “Credible Spatial Preemption,”

_Rand Journal of Economics_ 16:153–66.
Lichtenberg, F., and D. Siegel. 1992. “Takeovers

and Corporate Overhead,” in F. Lichtenberg,
ed., _Corporate Takeovers and Productivity_,
Cambridge: MIT Press.
Loughran, T., and A. Vijh. 1997. “Do Long-Term

Shareholders Benefit from Corporate Acquisitions?” _Journal of Finance_ 52: 1765–90.
Maskimovic, V., and G. Phillips. 2001. “The

Market for Corporate Assets: Who Engages
in Mergers and Assets Sales and Are There
Efficiency Gains?” _Journal of Finance_ 56
(December): 2019–65.
Mueller, D. C., 1982. “A Theory of Conglomer
ate Mergers,” _Quarterly Journal of Economics_
82: 643–59.
Nilssen, T., and L. Sorgard. 1998. “Sequen
tial Horizontal Mergers.” _European Economic_
_Review._ 42 (November), 1683–1702.
Nocke, V., and M. Whinston. 2013. “Merger Pol
icy with Merger Choice.” _American Economic_
_Review_ 103 (April), 1006–1033.
Norman, G., L. Pepall, and D. Richards.
2005. “Product Differentiation, Cost-Reducing
Mergers, and Consumer Welfare,” _Canadian_
_Journal of Economics_ 38 (November)
Norman, G., and J. F. Thisse. 1996. “Prod
uct Variety and Welfare under Soft and
Tough Pricing Regimes,” _Economic Journal_
106:76–91.


Perry, M., and R. Porter. 1985. “Oligopoly and

the Incentive for Horizontal Merger,” _Ameri-_
_can Economic Review_ 75:219–27.
Posada, P., and O.D. Straume. 2004. “Merger,

Partial Collusions and Relocation,” _Journal of_
_Economics_ 83: 243–265.
Ravenscraft, D. J., and F. M. Scherer. 1989. “The

Profitability of Mergers,” _International Jour-_
_nal of Industrial Organization_ Special Issue
(March):101–16.
Reitzes, J. D., and D. T. Levy. 1995. “Price Dis
crimination and Mergers,” _Canadian Journal_
_of Economics_ 28:427–36.
Salant, S., S. Switzer, and R. Reynolds. 1983.

“Losses from Horizontal Merger: The Effects
of an Exogenous Change in Industry Structure on Cournot–Nash Equilibrium,” _Quar-_
_terly Journal of Economics_ 98:185–213.
Salinger, M., 2005. “Four Questions about Hori
zontal Merger Enforcement,” _Remarks to ABA_
_Economic Committee of Antitrust Section, 14_
September.
Salop, S. C., 1979. “Monopolistic Competition

with Outside Goods,” _Bell Journal of Eco-_
_nomics_ 10 (Spring):141–56.


**Appendix**



Horizontal Mergers 421


Salvo, A. 2010. “Sequential Cross-Border Merg
ers in Models of Oligopoly.” _Economica_ 77
(April), 352–83.
Schmalensee, R. 1978. “Entry Deterrence in

the Ready-to-Eat Breakfast Cereal Industry,” _Bell Journal of Economics_ 9 (Autumn):
305–27.
Slade, M. 2007. “Merger Simulations of Unilat
eral Effects: What Can We Learn from the
UK Brewing Industry?” forthcoming in B.
Lyons, Ed., _Cases in European Competition_
_Policy_ : _The Economic Analysis_, Cambridge:
Cambridge University Press.
Werden, G., and L. Froeb. 1994. “The Effects of

Mergers in Differentiated Products Industries:
Logit Demand and Merger Policy,” _Journal of_
_Law, Economics, and Organizations_ 10 (October): 407–26.
Werden, G., and L. Froeb. 2002. “The Antitrust

Logit Model for Predicting Unilateral Competitive Effects,” _Antitrust Law Journal_ 70:
257–60.



STACKELBERG LEADER-FOLLOWER MODEL WITH SEVERAL
LEADERS


Instead of assuming _N_ firms with one leader and _N_ - 1 followers, let us assume _N_ firms
with _L_ leaders and _N_ - _L_ = _F_ followers. Equation (15.21) still describes the best response
of the typical follower firm. Because there are _N_ - _L_ such firms, a little algebra quickly
reveals that total follower output _Q_ _[F]_ is then:



_f_ [∗] [=] _[(N]_ _B(N_ [ −] _[L)(A]_ _L_ [ −] 1 _[c)]_ _)_



(15A.1)
_(N_ - _L_ + 1 _)_



_Q_ _[F]_ _(N_ _L)qf_ [∗]
=  



[ −] _[L)(A]_ [ −] _[c)]_

_B(N_ - _L_ + 1 _)_ [−] _(N_ _[(N]_ - [ −] _L_ _[L)Q]_ + 1 _[L]_



Denote the output of any one leader firm as _q_ _[l]_ and that of all the leaders _other than firm l_,
_QL_ - _l_ . The residual demand function for firm _l_ is then:

_P_ = [ _A_  - _B(Q_ _[F]_ + _QL_  - _l)_ ] − _Bql_ (15.A2)

Substituting for total follower output _Q_ _[F]_ from equation (15A.1) and re-arranging yields
the typical leader’s demand:



_B_

_P_ _[A]_ [ +] _[ (N]_ [ −] _[L)c]_ [ −] _[BQ][L]_ [−] _[l]_ (15.A3)
= _(N_ _L_ 1 _)_ - _(N_ _L_ 1 _)_ _[q][l]_

      - +      - +


422 Contractual Relations Between Firms


Hence, the associated marginal revenue function is

_MRl_ = _[A]_ [ +] _[ (N]_ _(N_ [ −] _[L)c]_ _L_ [ −] 1 _[BQ]_ _)_ _[L]_ [−] _[l]_  - _(N_ 2 _LB_ 1 _)_ _[q][l]_ (15.A4)

       - +        - +

Equating this marginal revenue with marginal cost gives the leader firm _l_ ’s best output
response to the output produced by all the other leader firms, _QL_ - _l_ :




[ −] _[L)c]_ [ −] _[BQ][L]_ [−] _[l]_ 2 _B_

_(N_ _L_ 1 _)_ - _(N_ _L_ 1 _)_ _[q][l]_ [ =] _[ c]_ [ ⇒] _[q]_ _l_ [∗]
 - +  - +



(15.A5)



_MRl_ = _[A]_ [ +] _[ (N]_ _(N_ [ −] _[L)c]_ _L_ [ −] 1 _[BQ]_ _)_ _[L]_ [−] _[l]_



_l_ [∗] [=] _[A]_ 2 [ −] _B_ _[c]_




[ −] _[c]_

2 _B_ - _[Q][L]_ 2 [−] _[l]_



2



By symmetry, all leader firms produce the same output in equilibrium. Hence, _Q_ [∗]



_(L_ By symmetry, all leader firms produce the same output in equilibrium. Hence, − 1 _)ql_ [∗] [substituted into equation (15A.5) then yields the stage-one output chosen by] _Q_ [∗] _L_ - _l_ [=]



_(L_ - 1 _)ql_ [∗] [substituted into equation (15A.5) then yields the stage-one output chosen by]

each merged leader firm:



_l_ [∗] _l_

[⇒] _[q]_ [∗]



_l_ [∗] [=] _[A]_ 2 [ −] _B_ _[c]_



(15.A6)
_B(L_ + 1 _)_



_q_ [∗]




[ −] _[c]_

2 _B_ - _[(L]_ [ −] 2 [1] _[)]_



2 _ql_ [∗]



_A_ _c_
_l_ [∗] [=] _B(L_ - 1 _)_ [and] _[ Q][L]_ [ =] _[ Lq]_ _l_ [∗]
+



_l_ [∗] [=] _B(L_ _[L(A]_ [ −] 1 _[c)]_ _)_



Substituting _Q_ _[L]_ into equation (15A.1), total follower output _Q_ _[F]_ and individual output
for each follower _q_ [∗] _[ Q][F]_ _[/(N]_ _[L)]_ [ are:]



_f_ [∗]

[=] _[ Q][F]_ _[/(N]_ [ −] _[L)]_ [ are:]



_A_ _c_ _(N_ _L)(A_ _c)_

_qf_ [∗] [=] _B(L_ 1 _)(N_ - _L_ 1 _)_ [and] _[ Q][F]_ [ =] _B(L_ - 1 _)(N_ - _L_ 1 _)_ (15A.7)

+     - + +     - +



Total market output _Q_ and the equilibrium price _P_ :



_Q_ _[T]_ _Q_ _[L]_ _Q_ _[F]_ _[(N]_ [ +] _[ NL]_ [ −] _[L]_ [2] _[)(A]_ [ −] _[c)]_
= + = _B(L_ 1 _)(N_ _L_ 1 _)_




_[(N]_ [ +] _[ NL]_ [ −] _[L]_ [2] _[)(A]_ [ −] _[c)]_ _[A]_ [ +] _[ (N]_ [ +] _[ NL]_ [ −] _[L]_ [2] _[)c]_

_B(L_ + 1 _)(N_ - _L_ + 1 _)_ [and] _[ P]_ [ =] _(L_ + 1 _)(N_ - _L_ + 1 _)_



(15A.8)
_(L_ + 1 _)(N_ - _L_ + 1 _)_



The price-cost margin and profit for the typical leader firm and typical follower firm are:



_A_ _c_ _(A_ _c)_ [2]
_P_ _c_ -  - = _(L_ 1 _)(N_ _L_ 1 _)_ [;] _[ π]_ _[L][(N, L)]_ [ =] _B(L_ 1 _)_ [2] _(N_
+      - + +      


_(A_ _c)_ [2]
_π_ _[F]_ _(N, L)_ = _B(L_ 1 _)_ [2] _(N_



_B(L_ + 1 _)_ [2] _(N_ - _L_ + 1 _)_ [;][ and]



_B(L_ + 1 _)_ [2] _(N_ - _L_ + 1 _)_ [2] _[.]_ (15A.9)



PROOF THAT AN ADDITIONAL MERGER IS PROFITABLE IN THE
LEADER-FOLLOWER MODEL


From (15.33), the necessary condition for two firms to merge and join the leader group is

_(L_ + 1 _)_ [2] _(N_  - _L_ + 1 _)_ [2]  - 2 _(L_ + 2 _)_ [2] _(N_  - _L_  - 1 _) >_ 0 (15A.10)

Define _x_ = _L_ + 1 and _y_ = _N_ - _L_ - 1. Then we need to show that

_x_ [2] _(y_ + 2 _)_ [2] ≥ 2 _(x_ + 1 _)_ [2] _y_


Horizontal Mergers 423


Note that _d(y_ + 4 + 4 _/y)/dy_ = 1 − 4 _/y_ [2] is negative for 0 _< y <_ 2. For _y >_ 2 we have

_Y_ + 4 + 4 _/y_ ≥ 2 + 4 + 4 _/_ 2 = 8

with equality only for _y_ = 2. For _x_ ≥ 1 this inequality can be rewritten

_(y_ + 2 _)_ [2] ≥ 8 ≥ 2 _(_ 1 + 1 _/x)_ [2] _y_ = 2 _((x_ + 1 _)/x)_ [2] _y_

giving _x_ [2] _(y_ + 2 _)_ [2] ≥ 2 _(x_ + 1 _)_ [2] _y_ as required.


BERTRAND COMPETITION IN A SIMPLE LINEAR DEMAND
SYSTEM


Start with the inverse demand system of equations (15.35):



_p_ 1 _A_ _Bq_ 1 _s(q_ 2 _q_ 3 _)_
=  -  - +



_p_ 2 _A_ _Bq_ 2 _s(q_ 1 _q_ 3 _)_ _(s_ [0 _, B))_
=  -  - + ∈



_p_ 3 _A_ _Bq_ 3 _s(q_ 1 _q_ 2 _)_ (15A.11)
=  -  - +



Inverting and manipulating this demand system yields:



_q_ 1 _[A(B]_ [ −] _[s)]_ [ −] _[(B]_ [ +] _[ s)p]_ [1][ +] _[ s(p]_ [2][ +] _[ p]_ [3] _[)]_
= _(B_ _s)(B_ 2 _s)_

       - +

_q_ 2 _[A(B]_ [ −] _[s)]_ [ −] _[(B]_ [ +] _[ s)p]_ [2][ +] _[ s(p]_ [1][ +] _[ p]_ [3] _[)]_
= _(B_ _s)(B_ 2 _s)_

       - +

_q_ 3 _[A(B]_ [ −] _[s)]_ [ −] _[(B]_ [ +] _[ s)p]_ [3][ +] _[ s(p]_ [1][ +] _[ p]_ [2] _[)]_
= _(B_ _s)(B_ 2 _s)_



_(B_ - _s)(B_ + 2 _s)_



_(s_ [0 _, B))_
_(B_ _s)(B_ 2 _s)_ ∈
 - +



(15A.12)
_(B_ - _s)(B_ + 2 _s)_



The Pre-Merger Case


We begin by identifying the equilibrium when each firm acts independently. Profit to firm
1 is




           _A (B_ _s)_ _(B_ _s)p_ 1 _s(p_ 2 _p_ 3 _)_

_π_ 1 _(p_ 1 _c)q_ 1 _(p_ 1 _c)_ - - + + +
=  - =  - _(B_ _s)(B_ 2 _s)_

                 - +







(15A.13)



Differentiating with respect to _p_ 1 and simplifying gives the first-order condition for firm 1:



_∂π_ 1
_∂p_ 1




_[A(B]_ [ −] _[s)]_ [ −] [2] _[(B]_ [ +] _[ s)p]_ [1][ +] _[ s(p]_ [2][ +] _[ p]_ [3] _[)]_ [ +] _[ c(B]_ [ +] _[ s)]_ 0 (15A.14)
= _(B_ _s)(B_ 2 _s)_ =

         - +



Defines firm 1’s best response function. Imposing a symmetric _p_ [∗]



1

[=] _[ p]_ [∗]



2

[=] _[ p]_ [∗]



3

[=] _[ p]_ [∗]



_nm_ _[,]_



substitution into (15A.14) gives: _[A(B]_ [ −] _[s)]_ [ −] [2] _[Bp]_ [∗]



rium prices:




_[s)]_ [ −] [2] _[Bp]_ _nm_ [∗] [+] _[ c(B]_ [ +] _[ s)]_ 0. Implying equilib
_(B_ _s)(B_ 2 _s)_ =
 - +



_nm_ [∗] _[A(B]_ [ −] _[s)]_ [ +] _[ c(B]_ [ +] _[ s)]_

[=] 2 _B_



_p_ [∗]



(15A.15)
2 _B_


424 Contractual Relations Between Firms



_nm_ [∗] _[(A]_ [ −] _[c)(B]_ [ +] _[ s)]_

[=] 2 _B(B_ 2 _s))_



Equilibrium output for each firm is therefore _q_ [∗]



(15A.13) implies that no-merger profit for each firm of:



which, in turn,
2 _B(B_ + 2 _s))_



_nm_ [∗] _[(A]_ [ −] _[c)]_ [2] _[(B]_ [ −] _[s)(B]_ [ +] _[ s)]_

[=] 4 _B_ [2] _(B_ 2 _s)_



_π_ [∗]



(15A.16)
4 _B_ [2] _(B_ + 2 _s)_



Merger of Firms 1 and 2


This post-merger profit-maximizing first-order conditions are



_∂(π_ 1 _π_ 2 _)_
+

_∂p_ 1



_∂(π_ 1 _π_ 2 _)_
+

_∂p_ 1

_∂(π_ 1 _π_ 2 _)_
+

_∂p_ 2



_∂(π_ 1 _π_ 2 _)_
+




_[A(B]_ [ −] _[s)]_ [ −] [2] _[(B]_ [ +] _[ s)p]_ [1][ +][ 2] _[sp]_ [2][ +] _[ sp]_ [3][ +] _[ cB]_
= _(B_ _s)(B_ 2 _s)_

       - +

_[A(B]_ [ −] _[s)]_ [ −] [2] _[(B]_ [ +] _[ s)p]_ [2][ +][ 2] _[sp]_ [3][ +] _[ sp]_ [3][ +] _[ cB]_
= _(B_ _s)(B_ 2 _s)_



0
_(B_ _s)(B_ 2 _s)_ =
 - +



_∂π_ 3
_∂p_ 3




_[A(B]_ [ −] _[s)]_ [ −] [2] _[(B]_ [ +] _[ s)p]_ [3][ +] _[ s(p]_ [1][ +] _[ p]_ [2] _[)]_ [ +] _[ c(B]_ [ +] _[ s)]_
= _(B_ _s)(B_ 2 _s)_



0 (15A.17)
_(B_ _s)(B_ 2 _s)_ =
 - +



0
_(B_ _s)(B_ 2 _s)_ =
 - +



Solving these for the equilibrium prices gives _p_ _[m]_



2 _[m]_ _[A(]_ [2] _[B]_ [ +][ 3] _[s)(B]_ [ −] _[s)]_ [ +] _[ c(]_ [2] _[B]_ [ +] _[ s)(B]_ [ +] _[ s)]_

[=] 2 _(_ 2 _B_ [2] 2 _Bs_ _s_ [2] _)_



1 _[m]_ 2

[=] _[ p][m]_



1 2

2 _(_ 2 _B_ [2] + 2 _Bs_                                  - _s_ [2] _)_
for the merged firm and _p_ _[nm]_ _[A(B]_ [ +] _[ s)(B]_ [ −] _[s)]_ [ +] _[ cB][(B]_ [ +][ 2] _[s)]_



3 _[nm]_ _[A(B]_ [ +] _[ s)(B]_ [ −] _[s)]_ [ +] _[ cB][(B]_ [ +][ 2] _[s)]_
= _(_ 2 _B_ [2] 2 _Bs_ _s_ [2] _)_



for the merged firm and _p_ 3 _[nm]_ for the nonmerged firm. Hence

= _(_ 2 _B_ [2] 2 _Bs_ _s_ [2] _)_

+              profits are:



_(A_ _c)_ [2] _(B_ _s)(B_ _s)_ [3]
3 _[m]_ - - +

[=] _(B_ 2 _s)(_ 2 _B_ [2] 2 _Bs_ _s_ [2] _)_



_π_ _[m]_



1 _[m]_ 2

[=] _[ π]_ _[m]_



2 _[m]_ _[B(A]_ [ −] _[c)]_ [2] _[(B]_ [ −] _[s)(]_ [2] _[B]_ [ +][ 3] _[s)]_ [2]

[=] 4 _(B_ 2 _s)(_ 2 _B_ [2] 2 _Bs_ _s_ [2] _)_ [2]



3

4 _(B_ 2 _s)(_ 2 _B_ [2] 2 _Bs_ _s_ [2] _)_ [2]
+ +  - [;] _[ π]_ _[m]_



_(B_ + 2 _s)(_ 2 _B_ [2] + 2 _Bs_ - _s_ [2] _)_ [2]



(15A.18)



Comparison of the Pre-Merger and Post-Merger Cases

Define _σ_ = _s/B,_ where _σ_ lies in the interval (0, 1) since we have that 0 ≤ _s < B_ :



_nm_ [∗] _[(A]_ [ −] _[c)]_ [2] _[(B]_ [ −] _[s)(B]_ [ +] _[ s)]_

[=] 4 _B_ [2] _(B_ 2 _s)_




[2] _[B]_ [2] _[(]_ [1][ −] _[σ)(]_ [1][ +] _[ σ)]_ _[(A]_ [ −] _[c)]_ [2] _[(]_ [1][ −] _[σ]_ [ 2] _[)]_

4 _B_ [3] _(_ 1 2 _σ)_ = 4 _B(_ 1 2 _σ)_
+ +



4 _B(_ 1 + 2 _σ)_



(15A.19)



_π_ [∗]




_[c)]_ [2] _[(B]_ [ −] _[s)(B]_ [ +] _[ s)]_ _[(A]_ [ −] _[c)]_ [2] _[B]_ [2] _[(]_ [1][ −] _[σ)(]_ [1][ +] _[ σ)]_

4 _B_ [2] _(B_ 2 _s)_ = 4 _B_ [3] _(_ 1 2 _σ)_
+ +



Profit of each division of the merged firm is:



_π_ _[m]_



1 _[m]_ 2

[=] _[ π]_ _[m]_



2 _[m]_ _[B(A]_ [ −] _[c)]_ [2] _[(B]_ [ −] _[s)(]_ [2] _[B]_ [ +][ 3] _[s)]_ [2]

4 _(B_ 2 _s)(_ 2 _B_ [2] 2 _Bs_ _s_ [2] _)_ [2]

[=]



4 _(B_ + 2 _s)(_ 2 _B_ [2] + 2 _Bs_ - _s_ [2] _)_ [2]




_[B]_ [4] _[(A]_ [ −] _[c)]_ [2] _[(]_ [1][ −] _[σ)(]_ [2][ +][ 3] _[σ)]_ [2]
= 4 _B_ [5] _(_ 1 2 _σ)(_ 2 2 _σ_ _σ_ [2] _)_ [2]




[4] _[(A]_ [ −] _[c)]_ [2] _[(]_ [1][ −] _[σ)(]_ [2][ +][ 3] _[σ)]_ [2]

_[(A]_ [ −] _[c)]_ [2] _[(]_ [1][ −] _[σ)(]_ [2][ +][ 3] _[σ)]_ [2]
4 _B_ [5] _(_ 1 2 _σ)(_ 2 2 _σ_ _σ_ [2] _)_ [2] 4 _B(_ 1 2 _σ)(_ 2 2 _σ_ _σ_ [2] _)_
+ +   - [=] + +   


(15A.20)
4 _B(_ 1 + 2 _σ)(_ 2 + 2 _σ_ - _σ_ [2] _)_ [2]



Without loss of generality, normalize _(A_  - _c)_ [2] _/B_ in unity. Profits are then a function
solely of _σ_ . A plot of (15A.19) and (15A.20) in the interval _σ_ ∈ [0,1 _)_ confirms that the
merger raises profits for all firms.


Horizontal Mergers 425


EQUILIBRIUM PRICES IN THE SPATIAL MODEL
WITHOUT A MERGER


Consider firm 3 as a representative firm. Demand for this firm from its left is _Nr_ 23 _,_ where
_r_ 23 is the marginal consumer given by



_m_ 3 _tr_ 23 _m_ 2 _t_
+ = +




- _L_

5

[=] _[ r]_ [23]



_r_ 23 _[m]_ [2][ −] _[m]_ [3]
⇒ = 2 _t_




_[m]_ [3] _[L]_

2 _t_ + 10



(15A.21)
10



Similarly, demand from consumers to the right of firm 3 is _Nr_ 34 _,_ where _r_ 34 is



_r_ 34 _[m]_ [4][ −] _[m]_ [3]
= 2 _t_




_[m]_ [3] _[L]_

2 _t_ + 10



(15A.22)
10



Firm 3’s profit is, therefore,


_π_ 3 _Nm_ 3 _(r_ 23 _r_ 34 _)_ _Nm_ 3
= + =




_m_ 2 _m_ 3
  



_[m]_ [3] _[L]_

2 _t_ + 5



5



- _m_ 3 _[m]_ [4][ −] _[m]_ [3]

2 _t_ + 2 _t_







(15A.23)



Differentiating this with respect to _m_ 3 to give the first-order condition for firm 3:




[3] _[L]_

_t_ + 5



5







_∂π_ 3
_∂m_ 3




_m_ 2 _m_ 4
+



= _N_



_m_ 4

2 _t_ - [2] _[m]_ _t_ [3]



= 0 (15A.24)



Since firms are identical, equilibrium requires _m_ 3 _m_ 2 _m_ 4. Hence, the Nash equilibrium prices is = =


_m_ [∗] = _tL/_ 5 (15A.25)


EQUILIBRIUM PRICES IN THE SPATIAL MODEL AFTER FIRMS 2
AND 3 MERGE


Conveniently changing the firms’ “labels” in equation (15A.23) we have:




_m_ 5 _m_ 1
  
2 _t_

_m_ 1 _m_ 2
  
2 _t_

_m_ 2 _m_ 3
  
2 _t_

_m_ 3 _m_ 4
  
2 _t_

_m_ 4 _m_ 5
  



_[m]_ [1] _[L]_

2 _t_ + 5

_[m]_ [2] _[L]_

2 _t_ + 5

_[m]_ [3] _[L]_

2 _t_ + 5

_[m]_ [4] _[L]_

2 _t_ + 5

_[m]_ [5] _[L]_

2 _t_ + 5



5



_π_ 1 _Nm_ 1
=


_π_ 2 _Nm_ 2
=


_π_ 3 _Nm_ 3
=


_π_ 4 _Nm_ 4
=


_π_ 5 _Nm_ 5
=



- _m_ 1 _[m]_ [2][ −] _[m]_ [1]

2 _t_ + 2 _t_

- _m_ 2 _[m]_ [3][ −] _[m]_ [2]

2 _t_ + 2 _t_

- _m_ 3 _[m]_ [4][ −] _[m]_ [3]

2 _t_ + 2 _t_

- _m_ 4 _[m]_ [5][ −] _[m]_ [4]

2 _t_ + 2 _t_

- _m_ 5 _[m]_ [1][ −] _[m]_ [5]

2 _t_ + 2 _t_



5



5



5



(15A.26)



5














426 Contractual Relations Between Firms


firms choose profit-maximizing prices as before. The first-order conditions are:The merged firm chooses _m_ 2 and _m_ 3 to maximize aggregate profit _π_ 2 + _π_ 3. Nonmerged



= 0


= 0




[1] _[L]_

_t_ + 5

[2] _[L]_

_t_ + 5

[3] _[L]_

_t_ + 5

[4] _[L]_

_t_ + 5

[5] _[L]_

_t_ + 5



5



_∂π_ 1
_∂m_ 1

_∂(π_ 2 _π_ 3 _)_
+

_∂m_ 2

_∂(π_ 2 _π_ 3 _)_
+

_∂m_ 3

_∂π_ 4
_∂m_ 4

_∂π_ 5
_∂m_ 5



= _N_


= _N_


= _N_


= _N_


= _N_




_m_ 5 _m_ 2
+

2 _t_

_m_ 1 _m_ 3
+

2 _t_

_m_ 2 _m_ 4
+

2 _t_

_m_ 3 _m_ 5
+

2 _t_

_m_ 4 _m_ 1
+



_m_ 2

2 _t_ - [2] _[m]_ _t_ [1]


_m_ 3

2 _t_ - [2] _[m]_ _t_ [2]


_m_ 4

2 _t_ - [2] _[m]_ _t_ [3]


_m_ 5

2 _t_ - [2] _[m]_ _t_ [4]


_m_ 1

2 _t_ - [2] _[m]_ _t_ [5]



5



= 0



5



2 _t_

[=][ 0]



5



_N_ _[m]_ [3]
+ 2 _t_

_N_ _[m]_ [2]
+ 2 _t_



(15A.27)
2 _t_

[=][ 0]



5















Solving these equations simultaneously gives the prices in the text. As noted, we assume
that no firm _i_ ever finds it profitable to price so low that it actually competes with firms
beyond _i_ - 1 and _i_ + 1 _._


# **16** **Vertical and Conglomerate Mergers**

In the fall of 2000, General Electric and Honeywell International announced that the two
companies would merge with GE acquiring Honeywell. GE is a very well-known firm with
annual revenues well over $100 billion. Its businesses are involved in everything from
lighting and appliances to television programming (it owns NBC) and financial services. GE
is also a major supplier of jet engines for commercial aircraft for which its chief competitors
are Rolls Royce and Pratt-Whitney. Honeywell was originally a leader in temperature and
environmental controls but has, over time, developed into a major aerospace firm whose
products include electric lighting, ventilation units, and braking systems for aircraft and
also starter motors for aircraft engines of the type GE builds. The deal was approved in
the United States. However, in July of 2001, the European Commission following the
recommendation of Competition Commissioner, Mario Monti, blocked the merger.

The proposed GE-Honeywell merger was a marriage of firms making complementary
products. The more aircraft engines GE sells, the more starter motors and other related
aircraft items Honeywell could sell. As a result, the proposed merger of GE and Honeywell
can be thought of as being equivalent to a vertical merger. Most often vertical mergers
combine firms operating at different levels of the production chain, say, a wholesaler
and a retailer. However, the connection between an upstream and a downstream firm is
qualitatively the same as the relation between Honeywell and GE, or that between computer
hardware and software, nuts and bolds, or zinc and copper, which are combined to make
brass. In all of these cases, two or more products are combined to yield the final good or
service. Because an upstream-downstream relationship is just one of the many types of
complementary relationships that may exist between firms, the term vertical merger has
come to have the more general interpretation of a merger between any firms that produce
complementary products.

We showed in Chapter 8 that the separate production of complementary goods—each
one produced by a firm with monopoly power—reduces the joint profit of the two firms
and imposes an efficiency loss on both firms and consumers. The intuition behind this
result is straightforward. Each firm’s pricing decision imposes an externality on the other
firm. A high price for computer hardware reduces demand for PCs. It also reduces demand
for programs and operating systems. The hardware manufacturer takes the first effect
into account, but not the second. The same is true, of course, in reverse. The software
manufacturer does not take into account the impact its price choice has on the demand for
hardware. In the non-cooperative Nash equilibrium, the prices of both goods are too high.
If, say, the hardware firm were to cut its price, this would generate additional demand and


428 Contractual Relations Between Firms


additional profit for the software firm. However, because the hardware firm does not receive
any of this additional profit, its incentive to reduce price is weakened. This suggests that,
with cooperation, both firms will lower their prices and be better off. Consumers, too, will
gain as a result of lower prices and expanded output.

One way to achieve the profit and efficiency gains of cooperation is for the two firms
to merge. Such a merger creates a single decision-making entity and, therefore, permits
the externality to be internalized. The combined hardware and software firm maximizes its
total profit by reducing the prices of both complementary goods so as to maximize the joint
profit from each. Whenever firms with monopoly power produce complementary products,
they have a strong incentive either to merge or to devise some other method to ensure
cooperative production and pricing of the complementary products.

Precisely the same issues of cooperation arise when the complementary relationships
arise because the firms occupy different levels in the vertical production chain. This is
important because it sheds light on how vertical mergers affect competition and so consumer
welfare. In the 1980s, the realization that vertical mergers can generate efficiency gains led
to something of a revolution in antitrust policy related to vertical mergers. In the decades
prior to 1980, vertical mergers were often seen as anticompetitive because of the fear that
such mergers would facilitate foreclosure. That is, the upstream merger partner would, after
the merger, refuse to supply its product to other downstream firms and thereby either drive
them out of the market or create barriers to entry that adversely affect them.

Economists primarily associated with the Chicago School challenged this negative view
of vertical mergers. They argued that vertical mergers could also achieve complementary
efficiencies and that “vertical integration was most likely pro-competitive or competitively
neutral” (Riordan 1998, 1232). By the 1980s, the Chicago School approach began to gain
in the courts and vertical mergers were treated increasingly favorably by the antitrust
authorities. However, by the mid-1990s the pendulum once more began to swing the other
way. A post-Chicago approach has now emerged that employs game theoretic tools to build
new and logically consistent models of vertical mergers in which once again the potential
for consumer harm is real. This counter-revolution has led to a detailed scrutiny of a number
of vertical combinations, most notably, those in the telecommunications sector.

We begin this chapter by developing an analysis of vertical mergers based on the
proposition that these are pro-competitive and correct market inefficiencies. In section 2,
we consider some of the more recent analysis suggesting that such mergers might adversely
affect competition in final product markets. Section 3 presents a simple formal model to
illustrate this phenomenon.

Section 4 turns to the third and final type of mergers. These are conglomerate mergers
involving the combination of firms without either a clear substitute or a clear complementary
relationship. Examples include the purchase of Duracell Batteries by Gillette, the purchase
of Columbia Pictures by Sony, and the series of acquisitions in 1986 by Daimler-Benz,
a luxury car and truck manufacturer, which turned it into Germany’s largest industrial
concern, producing everything from aerospace to household goods. Finally, section 5
presents a brief overview of antitrust policy with respect to different types of mergers.


16.1 PRO-COMPETITIVE VERTICAL MERGERS


When firms occupy different stages of the production stream the convention is to label those
firms farthest from the final consumer of the product as upstream and those closest to that
consumer as downstream. Film production companies and movie theaters are an example.


Vertical and Conglomerate Mergers 429


In this case, the production company is the upstream firm and the theater that shows the film
is the downstream firm. Manufacturers and retailers have a similar upstream–downstream
relationship. All such relationships can be usefully viewed as being complementary to each
other. Each firm in the vertical chain provides an essential service to other firms in the
chain. Our first order of business is to show that vertical relationships between two firms,
each with monopoly power, lead to a loss of economic efficiency in the absence of some
mechanism to coordinate the decisions of the two firms. In the case of vertically related
firms, this is referred to as the problem of _double marginalization_ .

Suppose that we have a single upstream supplier, the manufacturer, who sells a unique
product to a single downstream firm, the retailer. The manufacturer produces the good at
constant unit cost, _c_, and sells it to the retailer at a wholesale price, _r_ . The retailer resells
the product to consumers at the market-clearing price, _P_ . For simplicity, we assume that
the retailer has no other retailing costs. Consumer demand for the good is described by our
familiar linear inverse demand function _P_ = _A_ - _BQ_, and we assume of course that _c < A_ .

Given that the retailer purchases _Q_ units from the manufacturer at wholesale price _r_ and
resells these _Q_ units to consumers at price _P_ = _A_ - _BQ_ the retailer’s profit is

_�_ _[D]_ _(Q, r)_ = _(P_ - _r)Q_ = _(A_ - _BQ)Q_ - _rQ_ (16.1)


The retailer maximizes profit by equating marginal revenue with marginal cost. Marginal
revenue is _MR_ = _A_ - 2 _BQ_ and marginal cost is _r_ . Equating these two terms yields the
optimal downstream output,


_Q_ _[D]_ = _(A_ - _r)/_ 2 _B_ (16.2)


Substituting this expression into the demand function gives the market-clearing retail
price _P_ _[D]_ = _(A_ + _r)/_ 2. From equation (16.1) the retailer’s profit is, therefore, _�_ _[D]_ =
_(A_ - _r)_ [2] _/_ 4 _B_ . Figure 16.1 illustrates these results.

What about the manufacturer? What wholesale price should be charged? It is clear
from equation (16.2) that the wholesale price determines the number of units the upstream


_A_



( _A_ + _r_ )/2


_r_



![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/peppall_textbook_chunks/markdown/peppall_textbook_chunk18_p426-450_images/peppall_textbook_chunk18_p426-450.pdf-15-2.png)

2 _B_



_A/B_

Quantity



**Figure 16.1** Independent retailer’s optimal pricing as a function of manufacturer’s wholesale
price, _r_
At wholesale price _r_ the retailer will set retail price _P_ = _(A_ + _r)/_ 2 to maximize profit. Total retail profit is
indicated by the shaded region.


430 Contractual Relations Between Firms


supplier is able to sell to the retailer. At the wholesale price _r_ the retailer chooses to
sell _Q_ _[D]_ = _(A_ - _r)/_ 2 _B_ units. The retailer must purchase this number of units from the
manufacturer. In other words, _Q_ = _(A_ - _r)/_ 2 _B_ is the demand curve that the upstream
manufacturer faces. It describes the relationship between the wholesale price _r_ set by the
manufacturer and the quantity of the product demanded by the retailer. But this means that
_the inverse demand facing the upstream manufacturer at wholesale price r is r_ = _A_ - 2 _BQ_,
_which is also the marginal revenue function facing the retailer_ . [1]


by _P_ = 3,000 − _Q/_ 2. The retailer buys gold bracelets at a wholesale price, _r_, set by
the manufacturer. Show that the inverse demand curve facing the manufacturer is _r_ =
3,000 − _Q_ . Suppose instead that the retailer has additional marginal costs (labor etc.) of
_c_ _[D]_ . Show that the inverse demand curve facing the manufacturer is _r_ = _(_ 3,000 − _c_ _[D]_ _)_ - _Q_ .


We can now derive the profit-maximizing price that the manufacturer charges for its
product. Very simply, the manufacturer equates marginal cost with marginal revenue. The
inverse demand curve for the manufacturer is _r_ = _A_ - 2 _BQ_, so the marginal revenue curve
for the manufacturer is _MR_ = _A_ - 4 _BQ_ . Equating this with marginal cost _c_ yields the
profit-maximizing output and wholesale price. These are, respectively,



_Q_ _[U]_ _[A]_ [ −] _[c]_
= 4 _B_




[ −] _[c]_

and _r_ _[U]_ _[A]_ [ +] _[ c]_
4 _B_ = 2



(16.3)
2



This analysis is illustrated in Figure 16.2. When the upstream manufacturer sets the price
_r_ _[U]_ = _(A_ + _c)/_ 2, the downstream retailer charges a price _P_ _[D]_ = _(A_ + _r_ _[U]_ _)/_ 2 = _(_ 3 _A_ + _c)/_ 4.
The retailer sells _Q_ _[D]_ = _(A_ - _c)/_ 4 _B_ units, which is, of course, precisely the amount the
upstream manufacturer anticipated it would sell when it set its upstream price _r_ _[U]_ =
_(A_ + _c)/_ 2 in the first place. The profit of the manufacturer, shown in Figure 16.2 as the
darkly shaded area _wrgv_, is _�_ _[U]_ = _(A_ - _c)_ [2] _/_ 8 _B_ . The profit of the retailer, shown as the
lightly shaded area _refg_, is _�_ _[D]_ = _(A_ - _c)_ [2] _/_ 16 _B_ . The combined profit of the two firms is,
of course, just the sum of these two areas, 3 _(A_ - _c)_ [2] _/_ 16 _B_ .

Suppose now that the two firms merge so that the manufacturer becomes the upstream
division of an integrated firm, selling its output to the downstream retail division of the
same parent company. The manufactured good is still produced at constant marginal cost,
_c_ . This effectively transforms the integrated firm into a simple monopoly whose goal is to
maximize monopoly profit through its choice of retail price _P_ . This profit is total revenue
_PQ_ minus total cost _cQ_, which is _�_ _[I]_ = _(A_ - _BQ)Q_ - _cQ_ .

The marginal revenue curve of the integrated firm is the marginal revenue curve of
the nonintegrated retailer, _MR_ _[I]_ = _A_ - 2 _BQ_ . Equating this with marginal cost _c_ gives the
profit-maximizing output of the integrated firm, _Q_ _[I]_ = _(A_ - _c)/_ 2 _B_ . Substitution of this into
the inverse demand curve then gives the retail price to consumers, _P_ _[I]_ = _(A_ + _c)/_ 2.

The merger of the manufacturer and retailer results in consumers being charged a lower
price. As a result, the merged firm sells more of the product than did the two independent


1 If, by contrast, the retailer has additional marginal costs of _c_ _[D]_ then the inverse demand facing the
manufacturer is _(A_  - _r_  - _c_ _[D]_ _)_  - 2 _BQ_ : see Practice Problem 16.1.


Vertical and Conglomerate Mergers 431



_A_

(3 _A_ + _c_ ) _e_
4



![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/peppall_textbook_chunks/markdown/peppall_textbook_chunk18_p426-450_images/peppall_textbook_chunk18_p426-450.pdf-17-0.png)





( _A_ + _c_ )
~~2~~













_w_









_A/B_
Quantity



4 _B_



**Figure 16.2** Upstream and downstream profit maximization without vertical integration
The retailer’s marginal revenue curve _MR_ _[B]_ is the manufacturer’s demand curve _D_ _[U]_ . Double marginalization
results when the manufacturer sets its optimal wholesale price _r_ = _(A_ + _c)/_ 2 above marginal cost _c_, after which,
the retailer adds a further markup by setting retail price _P_ = _(_ 3 _A_ + _c)/_ 4. Retail profit is area _refg_ The
manufacturer’s profit is area _wrgv_ .


firms. But is this merger profitable? Yes! The profit earned by the integrated firm is _�_ _[I]_ =
_(A_ - _c)_ [2] _/_ 4 _B_ . This is 33.3 percent greater than the aggregate premerger profit of the manufacturer and the retailer, which we saw was 3 _(A_ - _c)_ [2] _/_ 16 _B_ . From a social welfare point of
view, _integrating the two monopoly firms has benefited everyone_ . Total profit is increased
_and_ consumer surplus is increased with more of the good being sold at a lower price.

The gains from this vertical merger are illustrated in Figure 16.3. The retailer’s premerger
profit, area _refg_, is redistributed to consumers as consumer surplus. In addition, consumers
gain the area _fgi_ . The manufacturer’s profit has doubled from area _wrgv_ to _wrib_ and this
more than offsets the loss of the retailer’s profit.

Merger of vertically related firms generates an all around efficiency gain because it
allows the separate but related activities to be coordinated and, thereby, to internalize the


_A_



(3 _A_ + _c_ )
4

( _A_ + _c_ )
~~2~~



_e_


_r_


_w_
















|f<br>g i<br>DD<br>v b<br>MC<br>MRU MRD = DU|Col2|
|---|---|
|||
||_v_|
||_MRU_<br><br>|



Quantity



_A/B_



4 _B_



2 _B_



**Figure 16.3** Upstream and downstream profit maximization with vertical integration
An integrated manufacturer-retailer sets a retail price to consumers at _P_ = _(A_ + _c)/_ 2. The area _refg_ that would
have been profit for a non-integrated retailer now becomes part of consumer surplus. However, the increased
sales volume generates a more than offsetting profit gain of area _gjbv_ . Total profit for the integrated firm is _rjbw_ .


432 Contractual Relations Between Firms


externality that each imposes on the other. In the absence of coordination, the final product
price reflects a double marginalization. The independent manufacturer marks up its price
to the retailer who then compounds that price-cost distortion by adding a further markup in
setting a price to the consumer. This is the basis of the old saying, “What is worse than a
monopoly? A chain of monopolies!”


curve _P_ = 100 − _Q_ . Widget retailing is controlled by the monopolist WR Inc., which
obtains its widgets from the monopoly wholesaler WW Inc. at a wholesale price of _ww_ per
widget. WW Inc. obtains the widgets in turn from the monopoly manufacturer WM Ltd. at
a manufacturing price of _wm_ per widget. WM Inc. incurs marginal costs of $10 per unit in
making widgets. WW and WR each incur marginal costs of $5 in addition to the prices that
they have to pay for widgets.


a. What is the equilibrium widget price to consumers, _P_, the equilibrium wholesale price
_ww_, and the equilibrium manufacturing price _wr_ ? What is the profit earned by each
firm at these prices?
b. Show that vertical integration by any two of these firms increases profit and benefits
consumers.
c. Show that integration of all three firms is even more beneficial.


There are, of course, several qualifications to this analysis that we should mention. Some
are noted in the accompanying Reality Checkpoint regarding the auto industry. In addition,
it is important to note that the benefits of the vertical merger just described assume that
the downstream firm uses a fixed amount of the upstream firm’s product for every unit of
output that the downstream firm sells. In our example of a manufacturer and a downstream
retailer, this assumption makes sense. The retailer has to have one unit of the manufacturer’s
product for every unit it sells to its customers. But in other situations this assumption could
be too strong. For example, if the upstream firm is a steel producer and the downstream
firm is an automobile manufacturer, the steel firm’s decision to charge the car manufacturer
a price that includes a high markup may induce the automaker to reduce its use of steel
in favor of aluminum or perhaps fiberglass. In such a case, the potential gains of the car
manufacturer integrating backwards into the steel market are less clear-cut.

In summary, vertical integration of a chain of producers, each of which has monopoly
power, is likely to benefit both firms and consumers by correcting the market failure
associated with double (and triple and quadruple _. . ._ ) marginalization. These benefits are
more likely to arise when the technology operated by downstream firms offers limited
opportunities for substitution into other inputs.


16.2 POSSIBLE ANTICOMPETITIVE EFFECTS OF
VERTICAL MERGERS


The merger analysis of the previous section suggests that the antitrust authorities should be
less concerned about the welfare impact of vertical mergers than the impact of horizontal
mergers. However, the analysis is based upon some important assumptions that drive the


Vertical and Conglomerate Mergers 433



![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/peppall_textbook_chunks/markdown/peppall_textbook_chunk18_p426-450_images/peppall_textbook_chunk18_p426-450.pdf-19-2.png)







results. In particular, we have assumed that there is a single market in which the final output
is sold and that there is monopoly at each stage in the vertical chain. Before coming to the
general conclusion that “vertical mergers are good for firms and consumers,” we should
check on the effects of relaxing these assumptions.


434 Contractual Relations Between Firms


16.2.1 Vertical Merger to Facilitate Price Discrimination


While life is good for a monopolist, it is even better for a monopolist who price discriminates.
This is equally true for an upstream monopolist selling to a number of downstream firms.
Moreover, there are many cases in which those downstream firms differ in their willingness
to pay for the upstream firm’s product. Examples include a wholesaler supplying retailers
in different cities, a manufacturer of motorcar parts supplying automakers in different
countries, a consultant advising different firms in different industries, and so on. In these
circumstances, the upstream firm would like to charge a high price for its product or service
to those firms whose demand is inelastic and a low price to those whose demand is elastic.

Our earlier discussion of price discrimination showed, however, that successful price
discrimination has two requirements. First, the firm must be able to identify which buyers
have elastic and which have inelastic demand. Second, the firm must somehow prevent
resale of its product among its buyers. Such arbitrage would clearly undo any price
discrimination efforts. We will assume that the firm has somehow solved the identification
problem. The question then becomes, what strategies can the firm use to surmount the
arbitrage problem?

The simplest approach would be for the upstream firm to write a no-resale contract
with its buyers. In many circumstances, however, such contracts are unenforceable—for
example when the client firms are in different legal jurisdictions—in which case some other
approach is necessary. One such approach is for the upstream firm to merge with some or
all of its downstream customers.

Suppose that the upstream firm supplies a series of downstream firms and that, because
of financial constraints, the upstream firm can integrate forwards with only some of the
downstream firms. Then, as Practice Problem 16.3 shows, _it should merge first into markets_
_with the highest elasticities of demand_ . Because the merger allows the upstream firm to
prevent resale, it also allows the firm to charge high profit-maximizing prices in the other,
low-demand-elasticity markets. Is such a merger pro- or anti-competitive? Successful price
discrimination can improve economic efficiency. When success is achieved by means of a
vertical merger the effect on economic efficiency is, however, ambiguous. The reason is
that while the merger increases profits and removes double marginalization in one group
of markets, the merger also leads to increased prices in the remaining markets. In other
words, some consumers gain and others lose from the vertical merger. The overall effect is
uncertain and can be resolved only when we have more information on the precise nature
of demand in the various markets.


demand for gizmos is _Pgb_ 1 _Qgb_, and TruGizmo Inc. of New York, where demand for
gizmos is _Pgn_ 0.5 0.2 = _Qgn_ . Assume that WI’s marginal costs of supplying both markets −
is $0.1 per widget and that both Gizmo Inc. and TruGizmo Inc. need exactly one widget = for every gizmo they sell. Both gizmo dealers have other costs of production that amount
to $0.1 per gizmo.


a. What are the profit-maximizing prices for widgets and gizmos in these two markets if
Widget International cannot price discriminate? What are the profits of the three firms?
b. What are the profit-maximizing prices for widgets and gizmos in these two markets if
Widget International can price discriminate? What are the profits of the three firms?


Vertical and Conglomerate Mergers 435


c. Show that if WI can merge with either Gizmo Inc. or TruGizmo Inc., it prefers to merge
with TruGizmo Inc.
d. What is the effect of the merger on consumer prices and consumer surplus when WI (i)
cannot and (ii) can price discriminate pre-merger?


16.2.2 Vertical Merger, Oligopoly, and Market Foreclosure


Now consider the second important assumption underlying the analysis in Section 16.1.
The gains from the merger hinge crucially on the fact that prior to the merger there is
monopoly at both levels of activity, manufacture and retail. Suppose, instead, that we start
with either a competitive manufacturing sector upstream selling to a monopoly downstream,
or a monopoly upstream firm selling to a competitive retail sector. In the former case, price
competition upstream among manufacturers leads to a wholesale price equal to marginal
cost. In the latter, competition among retailers downstream drives the retail price equal to the
upstream price _P_ _[U]_ plus any downstream cost _cD_ . In either case, no double marginalization
can occur, and there is no efficiency gain to vertical integration.

It could be argued, of course, that assuming perfect competition rather than monopoly
in either the upstream or downstream market merely replaces one extreme assumption by
another. We now turn, therefore, to the more realistic case in which both upstream and
downstream markets are oligopolies. This raises another important issue that needs to be
considered explicitly. Beyond the desire to reduce or eliminate double marginalization,
there is an additional motive for vertical integration that is more clearly anticompetitive.
The motive is the possibility of _market foreclosure_ . That is, the merger of vertically related
firms might result in an upstream–downstream company that can either deny downstream
rivals a source of inputs, or upstream competitors a market for their products.

Consider a hypothetical case in which two suppliers of computer chips compete for sales
to two downstream computer manufacturers who in turn sell to the general public. The
chips of the two upstream firms are identical so that, if the two suppliers compete in price,
they must sell at marginal cost. Hence, only the two downstream firms earn any economic
profit. Suppose now that one of the chip manufacturers and one of the computer firms
merge. The argument that this merger may be anticompetitive goes roughly as follows.
The upstream chip division of the newly merged firm no longer offers to sell any chips
to the remaining independent computer firm, that is, it forecloses sales of its product to
this downstream rival. Why? The answer is that such foreclosure leaves the independent
computer firm with only one supplier, namely, the remaining independent chip firm. That
independent chip producer now has monopoly power vis-`a-vis the independent computer
firm and, accordingly, sets a monopoly wholesale price for its chips. In turn, this raises the
costs of the independent computer firm relative to the pre-merger situation and makes it
less able to compete with the downstream computer division of the integrated firm. As a
result, the merged firm can raise the price of its computers and earn more profit. Because
the upstream market was initially competitive there was no double-marginalization and
because there are no other cost savings as a result of the merger, this vertical integration


436 Contractual Relations Between Firms


is clearly anticompetitive. [2] The merger raises the cost of the nonintegrated rivals on the
supply side and thereby leaves them at a disadvantage relative to the integrated firm.

The telecommunications industry is one in which foreclosure concerns have been quite
real for regulatory authorities in both the United States and in Europe. In this industry,
the local telephone network has generally been monopolized by a firm that also competes
in the more competitive long-distance market. Because a long-distance provider, such as
Sprint or say 1st Family, has to gain access to its potential customers by connecting to
the local network, the local network provider has the potential to price its long-distance
competitors out of the market by charging them a very high price for network access or, in
an extreme case, denying them access to the network at all. Accordingly, a major concern
of the regulatory authorities has been the prices that suppliers of local telephone networks
are allowed to charge for access to the local network.

Alcoa has been accused of subjecting its rivals to a similar price squeeze, both by
making contractual arrangements with power companies to prevent them from supplying
vital electricity to competing aluminum producers and by charging very high prices for
aluminum ingots that were used by rivals that competed with Alcoa in downstream markets
such as the aluminum sheet market. In short, foreclosure arguments suggest that monopoly
power in one, say upstream, market may be leveraged into power in another, downstream
market.


by the inverse demand curve _P_ = 100 − _Q_ . Retailers have zero production costs, but do
incur a fee, _r_, for every unit sold. This fee is the payment that retailers must pay to the only
manufacturer of widgets, the monopolist Widget International (WI). WI bears no fixed cost.
It does, however, have a constant marginal cost of $10.


a. What is the equilibrium price to consumers, _P_, and fee to retailers, _r_ ? What is the profit
earned by retailers and WI at these prices?
b. Show that vertical integration by which WI becomes the single producer and retailer of
widgets does not raise WI’s profit and does not lower the price to consumers.
c. What is the price to consumers if both widget manufacturing and retailing are
competitive?


16.3 FORMAL OLIGOPOLY MODELS OF VERTICAL
INTEGRATION


The conventional foreclosure argument that we just presented is compelling, particularly
when buttressed by the accompanying examples. However, there are also some clear
weaknesses in the argument that need to be confronted. The local phone network and Alcoa
examples are different from our hypothetical computer chip story in that these real world
cases begin with something less than competition in the upstream market. We have not


2 For a description many ways in which an integrated firm can impose a cost squeeze, see Krattenmaker and
Salop (1986).


Vertical and Conglomerate Mergers 437


identified why this may be the case. Apart from this practical consideration, the logic of the
argument is still incomplete. We have not explained why the integrated firm will definitely
stop selling chips to the independent downstream computer firm. Nor have we considered
an obvious response by the remaining independent firms, namely, to merge and similarly
enjoy the benefits of vertical integration. In the next section, we describe two models of
foreclosure through vertical integration that address these concerns. One is due to Salinger
(1988) and is based on Cournot competition. The other is due to Ordover, Saloner, and
Salop (1990) and is rooted in price competition.


16.3.1 Vertical Integration and Foreclosure in a Cournot Model


To illustrate Salinger’s (1988) basic contribution we return to our basic Cournot model
except that we now assume that Cournot competition applies both in an upstream market
populated by two firms and in a downstream market, also with two firms. The upstream
firms produce a homogeneous intermediate good that is used by the downstream firms to
make a homogeneous good for final consumption. One unit of downstream output requires
exactly one unit of the intermediate product. Each upstream firm has constant marginal
costs of _c_ _[U]_ per unit and each downstream firm has constant marginal costs, excluding the
cost of the intermediate good, of _c_ _[D]_ per unit. Inverse demand for the final consumption
good is:


_P_ _A_ _BQ_ _A_ _B(q_ 1 _q_ 2 _)_ (16.4)
=  - =  - +

The market game has two stages. In the first stage, the two upstream firms compete
in quantities, generating a price _P_ _[U]_ for the intermediate product. In the second stage,
the downstream firms compete in quantities taking the upstream price _P_ _[U]_ as given.
Consider first what happens when there is no vertical merger and then compare this
outcome with what happens when there is vertical merger. Such a comparison is easier
to make when we have a specific numerical example and so later we will use the values:
_A_ = 100; _B_ = 1; and _c_ _[U]_ = _c_ _[D]_ = 23.

_(i) No Vertical Mergers_


Cournot competition upstream in the first stage leads to a market-clearing intermediate
product price of _P_ _[U]_ so that each downstream firm in the second stage faces marginal cost
_P_ _[U]_ + _c_ _[D]_ . Cournot competition downstream leads each downstream firm to produce: [3]



_q_ _[D]_



1 _[D]_ 2

[=] _[ q][D]_



2 _[D]_ _[A]_ [ −] _[P][ U]_ [ −] _[c][D]_

[=] 3 _B_



(16.5)
3 _B_



and to earn a downstream profit of



_π_ _[D]_



1 _[D]_ 2

[=] _[ π]_ _[D]_



2 _[D]_ _[(A]_ [ −] _[P][ U]_ [ −] _[c][D][)]_ [2]

[=] 9 _B_



(16.6)
9 _B_



We can use equation (16.5) to identify the _derived demand_ that the upstream firms face.
Aggregate downstream output is _Q_ _[D]_ = 2 _(A_ - _P_ _[U]_ - _c_ _[D]_ _)/_ 3 _B_ . Because each unit of final

3 See Chapter 9 for the derivation of the Cournot equilibrium.


438 Contractual Relations Between Firms


product output requires one unit of the intermediate product, this is also the aggregate
demand, _Q_ _[U]_ = _Q_ _[D]_ for the intermediate product, which we can write in inverse form as:

_P_ _[U]_ = _(A_  - _c_ _[D]_ _)_  - [3] 2 _[B]_ _[Q][U]_ (16.7)


The next step in the analysis is simplified once we recognize that this is in standard linear
form _P_ = _a_ - _bQ_, where _a_ = _A_ - _c_ _[D]_ and _b_ = 3 _B/_ 3. In the first stage of the game, the
Cournot equilibrium output of each upstream firm is, therefore:




_[c][D][)]_ [ −] _[c][U]_ [2] _[(A]_ [ −] _[c][U]_ [ −] _[c][D][)]_

9 _B/_ 2 = 9 _B_



_q_ _[U]_



1 _[U]_ 2

[=] _[ q][U]_



2 _[U]_ _[a]_ [ −] _[c][U]_

[=] 3 _b_




_[c][U]_ _[(A]_ [ −] _[c][D][)]_ [ −] _[c][U]_

3 _b_ = 9 _B/_ 2



(16.8)
9 _B_



It follows that aggregate output in the upstream market is _Q_ _[U]_ = 4 _(A_ - _c_ _[U]_ - _c_ _[D]_ _)/_ 9 _B_ .
Substituting this into the upstream demand of equation (16.7) gives the equilibrium
upstream price for the intermediate product:




_[B]_ [4] _[(A]_ [ −] _[c][U]_ [ −] _[c][D][)]_

2 9 _B_

[×]



_P_ _[U]_ _(A_ _c_ _[D]_ _)_
=  -  - [3] 2 _[B]_




_[c][U]_ [ −] _[c][D][)]_ _[(A]_ [ −] _[c][D]_ [ +][ 2] _[c][U]_ _[)]_

9 _B_ = 3



(16.9)
3



Profit of each upstream supplier is _(P_ _[U]_ - _c_ _[U]_ _)qi_ _[U]_ [, which from (16.8) and (16.9) gives]



_π_ _[U]_



1 _[U]_ 2

[=] _[ π]_ _[U]_



2 _[U]_ [2] _[(A]_ [ −] _[c][U]_ [ −] _[c][D][)]_ [2]

[=] 27 _B_



(16.10)
27 _B_



Finally, substituting the upstream price into equations (16.5) and (16.6) gives the equilibrium
output and profit for each downstream firm:



_q_ _[D]_



1 _[D]_ 2

[=] _[ q][D]_


1 _[D]_ 2

[=] _[ π]_ _[D]_



2 _[D]_ [2] _[(A]_ [ −] _[c][U]_ [ −] _[c][D][)]_

[=] 9 _B_



(16.11)
9 _B_



_π_ _[D]_



2 _[D]_ [4] _[(A]_ [ −] _[c][U]_ [ −] _[c][D][)]_ [2]

[=] 81 _B_



(16.12)
81 _B_



It is easy to check that, as we would expect, aggregate downstream demand equals aggregate
upstream output. Using the numbers from our specific example, total output is 24 units. The
wholesale price is $41 and the price to consumers is $76. Each upstream firm earns $216 in
profit and each downstream firm earns $144.


_(ii) Vertical Integration of an Upstream and Downstream Firm_


Now consider what happens if one of the downstream firms _D_ 1 and one of the upstream
firms _U_ 1 merge. Assume for the moment that this newly merged firm refuses to supply
the independent downstream firm at all. Hence, the downstream firm _D_ 2 has to turn to the
remaining independent wholesaler _U_ 2 for its input supply, _and U_ 2 _knows this_ . It follows
that the upstream firm _U_ 2 has monopoly power over _D_ 2 and will set a price to _D_ 2 of
_P_ _[U]_ _> c_ _[U]_ . As a result, _D_ 2 has marginal cost _P_ _[U]_ + _c_ _[U]_ while _D_ 1 has marginal cost _c_ _[U]_ + _c_ _[D]_ .
In other words, the integrated firm has removed the double-markup in its pricing. As a
result, it now competes in the downstream market as a low-cost competitor vis-`a-vis _D_ 2.


