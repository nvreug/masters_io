discussed earlier. Second, we present various ways in which the supply side has been

modeled in the literature.

In some of the applications we will combine the demand model with a supply model

to estimate the parameters of both demand and supply and test the supply model, as we

saw in the motivating example discussed in Section 2. There are several ways to combine

demand and supply. First, we could use equation (2.3) to recover marginal costs without

assuming a parametric functional form for costs. Given demand estimates, a model of

pricing and observed prices, we can back out the marginal costs that make the first-order

condition for prices hold exactly for each observation in the data. Note, that the model

will perfectly fit the data and therefore we cannot test it, unless we bring in additional

information, such as information about marginal costs, and therefore markups.

Second, we can parameterize the marginal cost function and estimate its parameters,

potentially jointly with the demand equation using the demand parameters estimated in

a first stage. The advantage of estimating the marginal cost function is that it allows us

to extrapolate to counterfactual situations not observed in the data. It will also allow us

to test among models of competition, as we saw in Section 2, and estimate parameters

associated with the pricing model.

## **5.1 The Workhorse Model of Horizontal Competition**


The workhorse supply model in the study of differentiated-products industries is the
static pricing model, described in Section 2.1.1. [42] This model delivers a pricing equation

given in equation (2.2), which can be used in a few different ways that we discuss below.

Berry et al. (1995) is a seminal paper in the development of equilibrium models of de
mand and supply in differentiated-products industries, and where much of the demand

modeling discussed above was first developed. The authors were interested in under
standing the impact of a voluntary export restraints placed on exports of automobiles

from Japan to the United States. To study this question they developed and estimated a

model of demand and supply in Berry et al. (1995) and applied it to this question in Berry

et al. (1999).

The indirect utility in BLP is given by


_uijt_ = _xjtβi_ + _α_ ln( _yi −_ _pjt_ ) + _ξjt_ + _εijt_


42We will refer to this model interchangeably as the workhorse model and Nash-Bertrand model.


50


where _yi_ is income and all other variables are as previously defined. Note, that income
enters the indirect utility non-linearly and therefore will not cancel, as we discussed on

page 18. For estimation they assume that income is distributed log normal and estimate

the parameters of the distribution directly from income data. Consumer heterogeneity is

described by
_βi_ [(] _[k]_ [)] = _β_ 0 [(] _[k]_ [)] + _βν_ [(] _[k]_ [)] _[ν]_ _i_ [(] _[k]_ [)] _νi_ [(] _[k]_ [)] _∼_ _N_ (0 _,_ 1) _._


Finally, the utility from the outside option is given by


_ui_ 0 _t_ = _α_ ln( _yi_ ) + _εi_ 0 _t._


They estimate the model using 20 years of annual national data on the sales of auto
mobiles in the United States. The model is estimated using both demand and supply-side

moments. The demand-side IVs are the ones we described in Section 4.3.1. They also add

supply-side moments as we described in Section 4.3.2.

The paper delivers two sets of important results. First, the paper demonstrates the

importance of controlling for the endogeneity of price in the aggregate demand equation

derived from discrete choice. Nowadays this is taken as obvious – not surprisingly since

the importance of accounting for the endogeneity of price has been confirmed repeatedly

in numerous industries – but at the time it was questioned as empirically relevant. For

example, Table 3 of Berry et al. (1995) shows that a Logit demand model estimated with
out correcting for endogeneity of price yields a large number of inelastic demand curves

(1494/2217=67.3%), which is inconsistent with static profit maximization. Once they in
strument for price that number drops below 1%.

Second, the paper demonstrates the ability of the demand model to yield reasonable

substitution patterns. BLP present these in Tables 5-7 . For example, in Table 7 the authors

compare the diversion to the outside good, i.e., the fraction of consumers who substitute

to the outside good in response to a price increase as a fraction of all those who substitute

away from a product, implied by the Logit model and the more flexible random coeffi
cients model. For the Logit model, as expected, the diversion is roughly 90% for all cars,

which is roughly the share of the outside good. This number is high in absolute value,

but maybe more important is that it is roughly constant: if the price of a BMW 735i in
creases, consumers are equally likely to divert to the no-purchase option as consumers of

a Mazda 323. This seems unreasonable (and is totally driven by the Logit assumptions.)

The outside option includes all the choices that do not involve purchasing a new car,


51


such as buying a used car, not replacing an existing car or delaying purchase. Intuitively,

consumers who purchase a car are more likely to buy another car than switch to the no
purchase decision in response to a price increase, compared to the average consumer.

Furthermore, consumers who purchased a lower priced car are more likely to switch to

the no-purchase option in response to a price increase. In contrast to the Logit model, the

full model can capture these effects: the overall substitution to the outside good is lower

and the more expensive the car the lower the number. For example, the diversion for

Mazda 323 is roughly 27% while for BMW 735i is 10%.

In large part, the paper is able to deliver statistically significant estimates of the vari
ation in random coefficients because the authors impose the supply/pricing equation

in estimation. As we noted earlier, the supply equation, jointly with a functional form

for marginal costs that ensures that these costs will be non-negative, puts significant re
strictions on the demand estimates. For example, demand estimates that imply inelastic

demand also imply negative marginal cost under many models of pricing. A functional

form that imposes (a reasonable assumption) that all marginal cost are positive would

prevent this from happening. If we believe strongly in the supply model it is efficient to

impose it in estimation. However, as we discussed in Section 2, and as we discuss be
low, a large motivation for estimating demand and supply models is precisely to test the

supply model rather than assume it.

The paper abstracts from some elements of the car industry. For example, cars are a

durable good. Yet the demand system is static: consumers are not forward-looking in

the sense that they anticipate future needs, nor do they take into account whether they

own a car and if so which one, when they make a purchase decision. On the supply side,

the model assumes that manufacturers set a uniform price to consumers: dealers play no

role and there is no price discrimination. In reality, we know that cars are sold through

dealers and this market exhibits significant variation across consumers in the price they

pay. Furthermore, the pricing model is static while in reality prices might reflect inventory

considerations, generating brand loyalty or other dynamic effects. For many questions it

is fine to abstract away from these issues, yet for some questions these issues might be

quite important. Indeed, the paper inspired a large literature that relaxed some of these

modeling assumptions on both the demand and supply side. We discuss some of the

papers in this literature in the rest of this chapter and many others are discussed in other

chapters in this Handbook.


52


## **5.2 Distinguishing Between Models of Competition**

In this subsection we look to expand the supply, or pricing, models we consider. We will

have a dual goal of coming up with potentially more general, or more flexible, models

that would allow us to explain different patterns of pricing (and markups), as well as

testing the workhorse, Nash-Bertrand model, and finding ways to distinguish it from

alternative models. For the most part, the alternative models will focus on models that are

more ”collusive” and therefore tend to imply higher markups. We also use the discussion

below as an opportunity to discuss several empirical implementations of the demand

model.

A natural place to start thinking about expanding beyond the workhorse model is to

consider testing of the model. Testing will generally follow the ideas presented in Section

2. As we saw there, one way to test the model is to informally compare predictions of

prices and costs from different models to patterns we see in the data, even if only at an

aggregated level. Nevo (2001) does precisely that. He studies pricing in the ready-to-eat

cereal industry. The industry, at the time he studies it, was characterized by high concen
tration (the top 3 firms had approximately 75% share, and the top 6 approximately 90%),

”high” price-cost margins (approximated to be around 45%), large advertising to sales

ratios (roughly 13%) and numerous introductions of brands (67 new brands introduced

by top 6 firms in 1980’s). These facts were used to claim that this is a perfect example of

an industry where firms collude on pricing but compete on advertising and brand introductions. [43] The paper asks if prices observed in this industry, and the margins that were

approximated, are consistent with collusive pricing? Specifically, the paper notes that

seemingly high margins can be due to product differentiation and multi-product pricing

(of substitute products) and are not necessarily indicative of collusion.

To separate the effect of collusion Nevo estimates a brand-level demand system, he

then computes price-cost margins implied by different pricing models and chooses the

pricing model that cannot reject the approximated margins of 45%. He finds that the

”high” margins are consistent with Nash-Bertrand pricing by multi-product firms and

therefore one does not need to rely on collusion to explain the ”high” margins. In other

words, the data cannot reject the Nash-Bertrand model.

The demand model he uses follows equation (3.3). He estimates the model using

scanner data for the top 25 brands of cereal. The data are aggregated to the MSA-quarter


43For example, Scherer (1982) argues that ”...the cereal industry’s conduct fits well the model of price
competition-avoiding, non-price competition-prone oligopoly” (p. 189)


53


level and he aggregates different SKUs to a brand. This results in 1,124 markets and

27,862 brand-quarter-MSA observations. He defines prices as total revenues divided by

the number of servings, which he defines using the suggested servings size. Character
istics come from nutritional information (e.g., fat or sugar content), segment information

used by the industry, and subjective information (e.g., he defines a “mushy” dummy

variable). He estimates demand using the BLP algorithm and prices in other cities as IVs.

Unlike BLP he estimates demand without imposing any supply-side moments, which

has the advantage of yielding consistent estimates even if we are unsure about the supply

model. He is able to do so because he has more markets than BLP and more variation in

demographics across markets.

For the supply side he computes three models: single product, multi product and

collusion, following the models discussed in Section 2.1.1. The markups implied by dif
ferent supply and demand models are presented in Table 8 in the original paper. Using

the random coefficients demand estimates he finds that the current ownership of the top

25 brands predicts an average margin of 42%, while joint ownership of these brands pre
dicts a margin of 73% (with a confidence interval between 62% and 97%). By comparing

these results to the approximation of the margins, which he estimates at 45%, he rejects

the null of perfect collusion, or joint profit maximization of the top 25 brands, but cannot

reject the null of Nash-Bertrand pricing.

Like BLP, this paper also raises several questions regarding the modeling assumptions.

First, a common concern is whether demand is really discrete. In micro data, we often

observe consumers purchasing more than one box of cereal, at times even different brands

on the same trip. How do we reconcile this pattern with a discrete choice? One option

is to think of the choice as happening at the time of consumption: at that point it seems

more reasonable to assume a discrete choice. Thinking of the model this way ignores

the two-step process, where the consumer first decides what to purchase at the store and

then what to consume from the brands available at home, but with aggregate data it is

unclear we can separate this process. In Section 6.1.1 we will discuss models that tackle

the modeling and estimation of multiple choices.

The paper does not explicitly model retailer behavior despite using retailer prices to

study manufacturer competition. This is consistent with retail margins going into the

cost manufacturers pay to get the product on the shelf. This assumption, however, is

not consistent with a strategic retailer who will change their margin in response to the


54


manufacturer pricing. In the next subsection, we will discuss how to add retailers to the

model.

Finally, much of the price variation at the store level is coming from ”sales”, or tempo
rary price reductions. This creates an incentive for consumers to purchase the products

when the prices are low and consume them later. Follow-up work by Hendel and Nevo

(2006a,b), which we discuss in Section 6.2.1, follows up on this issue.

One of the common uses of the supply model is to simulate the effects of a proposed

merger. The idea was discussed by Berry and Pakes (1993) and Werden and Froeb (1994),

and implemented empirically by Nevo (2000a). The basic idea is as follows. Using pre
merger data one can estimate demand and recover marginal costs. The marginal cost can

be recovered as in BLP, by parameterizing the cost function and estimating it jointly with

demand. Alternatively, marginal cost can be recovered, without making any parametric

assumptions on the cost function, by ”inverting” the pricing equation (2.2) such that


_**mc**_ **ˆ** = _**p**_ _−_ Ω [ˆ] _[−]_ [1] _**q**_ _,_ (5.1)


where Ω [ˆ] _[−]_ [1] is computed using the demand estimates and _**q**_ are observed quantities. One

then uses these estimates to simulate the effect of the merger by changing the ownership

structure defined in equation (2.1). In general, holding costs constant a merger between

substitutes products will lead to higher prices, and a merger between complements will

lead to lower prices. The real issue is not the direction of the effect, but the magnitude: if

the products are closer substitutes the effect will be larger. The reason to estimate demand

is to be able to quantify the effect. Furthermore, one could also use the model to simulate

the impact of various efficiencies such as reductions in marginal costs, or improvements
in qualities. This approach has found support in the academic literature and in practice. [44]


Simulating the effects of mergers can be the object of interest, but can also serve as a

way to test the model. An early attempt at this was provided by Peters (2006) who used

comparisons between predicted and actual outcomes of airlines mergers to test the de
mand model. Miller and Weinberg (2017) study the beer industry and use a joint venture,

which they treat as a merger, to test the Nash-Bertrand model. Their study is motivated

by a desire to understand the price effects after the 2008 Miller-Coors joint venture (JV).

The JV significantly increased concentration in the industry. After it, ABI (the producer


44For a discussion of the use in policy see Griffith and Nevo (2019), and for discussion of the use of
merger simulation in a specific merger see Bayot et al. (2018).


55


of Budweiser) had a 37% market share, Miller-Coors had 29%, Modelo (the producer of

Corona) had 9%, and Heineken had 5%.

They document, in Figure 1 (and Tables 2 and 3) of their paper, that post-JV (i) the

price of Miller-Coors products increased; (2) the price of ABI increased almost one-to-one

with the Miller-Coors price; and (3) the prices of Modelo and Heineken did not increase.

The direction of the first fact is not surprising, since, as we discussed above, this is what a

standard Nash-Bertrand model would predict. The magnitude might be higher than ex
pected, but we cannot measure that without knowing the cross-price elasticities between

the products. The fact that ABI prices increase should also not be surprising since prices

are strategic complements in a pricing game for many (but not all) demand models. In

these cases, the increase in the price of Miller-Coors would lead to an increase in the ABI

price. What is surprising is that the ABI price increase is similar in magnitude to the

Miller-Coors price increase. The paper sets to see if the demand estimates can reconcile

these increases with what a competitive pricing model would predict.

The demand model they estimate is a random coefficients Nested Logit model, where

all the products are in one nest and the outside good is in another. They estimate the

model using monthly (or quarterly) scanner data for 13 brands in 39 different distinct

regions, and the BLP nested fixed point algorithm discussed above. For IVs they use the

distance between the brewery and the region, an indicator variable equal to one for ABI

and Miller-Coors products after the merger, the number of products, mean income (by

region) interacted with product characteristics. Their estimates (Table 4 in the paper) find

statistically significant heterogeneity in preferences, but economically fairly small. The

implied elasticities (presented in Table 5) show a slight variation from the pattern implied

by the model with no heterogeneity: substitution between the inside goods is roughly

proportional to share.

To estimate the supply side they specify marginal cost as a function of distance from

the brewery, an indicator equal to 1 one for Miller-Coors products post-merger, and prod
uct region and period fixed effects. They use the model of Section 2.1.1 but slightly modify

the definition of the ownership, given in equation (2.1). Specifically, they assume that the

( _j, k_ ) element equals _κ_ if products _j_ and _k_ are sold by ABI and Miller-Coors post-merger.

This generates Nash–Bertrand competition in the post-merger periods if _κ_ = 0 and joint

profit maximization for ABI and Miller-Coors if _κ_ = 1. Putting this together with equation


56


(4.12) yields the estimating equation


_**p**_ _t_ = w _t_ _**γ**_ + Ω _[−]_ [1] ( _κ_ ) _**q**_ ( _**pt**_ ) + _**ω**_ _t,_


where variables are defined as in (4.12). They estimate the cost parameters and _κ_ using
GMM and assuming that _ωjt_ is mean independent of w _j_ and an indicator equal to one for
ABI and Miller-Coors products post merger. [45]


They estimate that _κ_ varies between 0.25 and 0.34, depending on the specification they

use. All the specifications reject the null hypothesis that _κ_ = 0, which is Nash-Bertrand

pricing post merger. Interestingly, the model also rejects joint profit maximizing pricing,

between ABI and Miller-Coors post merger. In other words, pricing is consistent with

some increased coordination post merger but not joint profit maximization.

Ciliberto and Williams (2014) use a similar idea to study multi-market contact in the
U.S. airline industry. They modify equation (2.1) by making the terms _Hjr_ a function
of a variable that measures the degree of multi-market contact between the airlines that

produce products _j_ and _r_ . They conclude that airlines with a higher degree of multi

market contact almost perfectly collude.

It is tempting to try to interpret intermediate values of _κ_ . For example, one interpreta
tion, which was popular for a while in the analysis of competition in homogeneous goods

industries, views _κ_ as a ”conduct parameter” that captures beliefs about the equilibrium

being played (Bresnahan, 1989). A slightly different interpretation views _κ_ as an ”as if”

parameter. For example, if _κ_ = 0 _._ 5 in a homogeneous good industry, the industry would

be seen as being as competitive as an industry with 2 symmetric firms playing Cournot.

Similar ”as if” potential interpretations exist for industries with differentiated products.

For example, building on Nevo (1998), Black et al. (2004) propose an interpretation of _κ_
as a measure of cross ownership. [46]


These attempts to interpret intermediate values of _κ_ have fallen mostly out of favor

for several reasons. For example, Corts (1999) notes that if the true model implies varia
tion in _κ_ over time within each regime, the ”as if” interpretation is problematic. Indeed,

he shows via simulations that the estimated _κ_ need not even be a good indicator of the

relative competitiveness of industries. His main complaint is not about the idea of having


45Note that prices appear on both sides of the estimating equation, and therefore we need an (additional)
IV, in this case an indicator equal to one for ABI and Miller-Coors products post merger.
46Backus et al. (2021) build on these ideas, and use data from the ready-to-eat cereal industry, to test
recent claims that common ownership facilitates collusion.


57


a parameter _κ_ but to the a-theoretical restrictions put on it. He calls for a specification

of a (structural) model of collusion in order to justify restrictions on _κ_ . Miller and Wein
berg (2017) are partly immune to this critique because of their focus on testing whether

_κ_ is statistically different than zero as a test for post-merger Nash–Bertrand competition

(since under the null the model is well specified).

Most of the above discussion of testing and distinguishing between models was some
what informal. However, the ideas are can be formalized. Bresnahan (1982) and Lau

(1982) discuss the use of rotation of the demand curve as an IV to estimate the model of

competition in homogeneous goods industries. Berry and Haile (2014) show that the basic

idea generalizes to models that study competition in differentiated products industries.

Specifically they show that the model of competition can be identified using the supplyside conditional moments _E_ ( _ωjt|_ _**Z**_ _t_ ) = 0, as defined in (4.12). The intuition behind this is

what we saw in the applications above: different models of competition have implications

for patterns we observe in the data. The patterns can be either average markups (Nevo,

2001), variation in prices after a merger (Miller and Weinberg, 2017), or co-variation in

prices and multi-market contact across markets Ciliberto and Williams (2014). The mo
ment condition is a way to summarize this variation.

Casting the problem as a moment condition allows Berry and Haile (2014) to formally

discuss identification. It also has the advantage of generalizing the idea of using a specific

event, for example, a merger, to using variation like that discussed in Section 4.2.2, to

distinguish models of competition. This raises the question of what IVs should be used.

Active areas of research are what IVs have power to distinguish models of competition

(Duarte et al., 2021) and somewhat related is what is the efficient ways to use these IVs

(Backus et al., 2021).

## **5.3 Adding Retailers Into the Mix**


One of the common complaints about some of the papers presented in the previous sub
section is that they are are concerned with competition between manufacturers yet use

retail data without explicitly modeling the retailers. This practice can be justified if we

treat the retailers as passive and therefore part of the manufacturer costs of getting the

products to market. In this subsection we discuss papers that allow retailers to make

strategic decisions in response to price changes by the manufacturers.

Villas-Boas (2007) asks what model best describes the relationship between manufac
turers and retailers in the yogurt industry. To answer this question she takes the idea of


58


using demand estimates jointly with a pricing model to recover cost, and adds to it an ad
ditional layer: her pricing models account for both retailer and manufacturer/wholesaler

behavior. She computes markups/costs under different models. She then chooses the

model that best describes the data.

To estimate demand she uses weekly scanner data for 43 products, produced by 5

manufacturers and sold by 3 retailers. She observes retail prices, advertising, aggregate

quantity (by product-retailer), and product characteristics, but does not observe whole
sale prices or contracts. She estimates a random coefficients Logit Model, where the choice

is store-brand. In other words, consumers choose not just the brand but also where to

purchase it.

She considers six supply models. In Model 1, manufacturers first set (linear) wholesale

prices and then retailers, taking these wholesale prices as given, set retail prices. In each

stage there is Nash-Bertrand pricing. This results in double marginalization. Formally,

retailer _r_ in market _t_ maximizes profits given by


      _πrt_ = [ _pjt −_ _p_ _[ω]_ _jt_ _[−]_ _[c]_ _jt_ _[r]_ []] _[q][jt]_ [(] _**[p]**_ _[t]_ [)] _[.]_

_j∈Jrt_


where _p_ _[ω]_ _jt_ [is the wholesale price paid by the retailer,] _[ c]_ _jt_ _[r]_ [is the retailer’s marginal cost and]
_Jrt_ is the set of products sold by the retailer. In her setting each ”product” _j_ is a brandretailer combination and therefore this setting allows for different wholesale and retail

prices to be charged for the same physical product. Rearranging the first-order conditions

we can write
_**p**_ _t −_ _**p**_ _**[ω]**_ _t_ _[−]_ _**[c]**_ _t_ _**[r]**_ [= (Ω] _[r]_ [)] _[−]_ [1] _**[q]**_ [(] _**[p]**_ _[t]_ [)] _[,]_


where Ω _[r]_ is a matrix with elements given by Ω _[r]_ _jk_ [=] _[ −][∂q][k][/∂p][j][ ·][ H]_ _jk_ _[r]_ [, where] _[ j]_ [ indexes rows]
and _k_ columns and _Hjk_ _[r]_ [is the retailer ownership structure, namely] _[ H]_ _jk_ _[r]_ [= 1][ if both] _[ j]_ [ and]
_k_ are sold by _r_ .

The manufacturers’ problem is to maximize profits given by


      _πωt_ = [ _p_ _[ω]_ _jt_ _[−]_ _[c]_ _jt_ _[ω]_ []] _[q][jt]_ [(] _**[p]**_ _[t]_ [)]

_j∈Jωt_


where _c_ _[ω]_ _jt_ [is the manufacturer’s marginal cost and] _[ J][ωt]_ [is the set of products produced by]
manufacturer _ω_ . Rearranging yields the following first-order conditions


_**p**_ _**[ω]**_ _t_ _[−]_ _**[c]**_ _t_ _**[ω]**_ [= (Ω] _[ω]_ [)] _[−]_ [1] _**[q]**_ [(] _**[p]**_ _[t]_ [)] _[,]_


59


where Ω _[ω]_ is a matrix with elements given by Ω _[ω]_ _jk_ [=] _[ −][∂q][k][/∂p]_ _j_ _[ω]_ _[·][ H]_ _jk_ _[ω]_ [, where] _[ j]_ [ indexes rows]
and _k_ columns and _Hjk_ _[ω]_ [is the manufacturer ownership structure. Note, that] _[ ∂q][k][/∂p]_ _j_ _[ω]_ [can]
be computed using the derivatives of the retail prices with respect to wholesale prices (by

totally differentiating the retailers first-order conditions with respect to wholesale prices)

and the derivatives of quantity with respect to retail prices.

In Model 2 the national brands are as in Model 1. However, the private labels are

treated as a vertically integrated (the “manufacturer” sets the retail price for them).
In Model 3 she explores non-linear pricing. She consider two cases. [47] In case 1, manufacturers set the wholesale price equal to cost, _p_ _[ω]_ _t_ [=] _[ c]_ _t_ _[ω]_ [and set fees] _[ F]_ [, aimed at extracting]
the retailers’ profits. In this case, the retail price is


_**p**_ _t −_ _**c**_ _**[ω]**_ _t_ _[−]_ _**[c]**_ _t_ _**[r]**_ [= (Ω] _[r]_ [)] _[−]_ [1] _**[q]**_ [(] _**[p]**_ _[t]_ [)]


In case 2, retailers’ margins are set to zero, _pjt_ = _p_ _[ω]_ _jt_ [+] _[ c]_ _jt_ _[r]_ [and the retailers set a fee] _[ F]_ [ to]
recover profits. Prices are set to maximize downstream profits for the manufacturers


_**p**_ _t −_ _**c**_ _**[ω]**_ _t_ _[−]_ _**[c]**_ _t_ _**[r]**_ [= (Ω] _[ωr]_ [)] _[−]_ [1] _**[q]**_ [(] _**[p]**_ _[t]_ [)]


where Ω _[ωr]_ is a matrix with elements given by Ω _[ωr]_ _jk_ [=] _[ −][∂q][k][/∂p][j][ ·][ H]_ _jk_ _[ω]_ [. The difference be-]
tween the two cases is in the ”ownership” structure used. In case 1 the pricing internalizes cross-price effects across brands _within_ a store, while in case 2 the pricing internalizes
cross-price effects within a brand _across_ stores.

Models 4-6 allow for coordination. Model 4 is like Model 1 but with manufacturer
level (perfect) collusion. Model 5 is like Model 1 but retail-level (perfect) collusion. Fi
nally, Model 6 offers a version of a vertically integrated monopolist.

Estimation of demand follows the standard approach, using as IVs cost data multi
plied by a product fixed effect (i.e., the costs are allowed to impact each product differ
ently). To choose between the supply models she uses two approaches. In the first she

regresses


_**pt**_ = w _tγ_ + _SIPCMr_ (Ω) _λr_ + _SIPCMω_ (Ω) _λω_ + _**ω**_ _t,_


where w are cost variables, _γ_ is a vector of coefficients, _SIPCMr_ (Ω) and _SIPCMω_ (Ω) re
tail and manufacturer price-cost margins, respectively, implied by the different scenarios


47See Bonnet and Dubois (2010) for the assumptions required to justify the first-order conditions that
follow as coming from two-part tariff contracts.


60


above. She then tests if _λ_ [ˆ] _r_ and _λ_ [ˆ] _ω_ are statistically different from 1. [48] The logic is that in a
well specified model the observed prices should equal marginal cost plus the wholesale
and retail margins, i.e., the coefficients on markups should equal 1. [49] Next, she uses a

statistical test of non-nested alternatives, as in Bresnahan (1987) and Gasmi et al. (1992),
using the procedure in Smith (1992). [50] Based on these she concludes that models that

assume zero wholesale margins and in which retailers have pricing decisions best fit the
data. She then discusses several contracts that are consistent with these outcomes. [51]


The paper shows that the logic of backing out markups and costs, presented in Section

2 can be extended to another (vertical) level of decisions. Indeed, the pricing equations

she proposes are direct extensions of the pricing equation we discussed in the previous

two subsections.

## **5.4 Models of Bargaining**


Up to this point the supply models we focused on dealt with situations where one side of

the market makes a take-it-or-leave-it offer. In the basic model, it was the manufacturers

making a take-it-or-leave-it offer to consumers or to retailers. In the previous subsection

we allowed retailers to make the offer to the manufacturers. In many real-world situa
tions neither of these fits what actually happens because, for example, the parties, say a

manufacturer and a retailer, negotiate the final outcome rather than one side dictating the

terms of trade and the other side simply accepting or rejecting the offer. Even if there is

no explicit negotiation, a bargaining model seems like a good way to model pricing that

is between either extreme of prices set by upstream or downstream firms.

To fix ideas, we focus on a specific example, the study by Crawford and Yurukoglu

(2012) of bargaining in TV markets. Crawford and Yurukoglu study the impact on con
sumer welfare of (un)bundling of TV channels offered in cable bundles. Generally ca
ble companies offer consumers a bundle of channels and consumers cannot subscribe


48Note that like our discussion of the supply model in Miller and Weinberg (2017), the parameters entering the pricing equation might require IVs to identify them because of the fact that the markup terms
_SIPCMr_ and _SIPCMω_ might also be functions of prices and shares and therefore correlated with the
econometric error _**ω**_ _t_ .
49Pakes (2017) conducts a similar exercise. Specifically, he uses demand estimates from Wollmann (2018)
to construct the markup term. He then regresses the estimated markup on IVs and regresses the observed
price on the observed cost determinants and this predicted markup. He finds that the estimated coefficient
is not statistically different than 1.
50See Rivers and Vuong (2002) and Duarte et al. (2021) for additional discussion of non-nested testing.
51See Bonnet and Dubois (2010) for follow up work that examines these issues.


61


to channels `a la carte. Some have suggested that consumers are hurt by this arrange
ment because they have to pay for channels that they do not want. Crawford and Yu
rukoglu (2012) ask: what are the (equilibrium) welfare effects of unbundling? Hold
ing channel prices constant, consumers will be better off with unbundling because they

could purchase ”skinnier” bundles. However, Crawford and Yurukoglu point out that

this argument ignores equilibrium effects. Therefore, to answer the question of whether

consumers are better or worse off with unbundling, they need to model the effect of

unbundling on input prices, namely the prices paid to the content providers. To do so

they develop an empirical bargaining model based on the theoretical model of Horn and

Wolinsky (1988a,b).

They model the negotiation between each conglomerate of channels (e.g., ABC Disney,

which owns ESPN, ESPN2, Disney channel and other channels) and the operator/distributor

(e.g. Comcast), as a bilateral bargaining problem over linear (input) prices for that pair.

The Nash bargaining solution is the set of input prices that maximize the weighted prod
uct of the values to both parties from agreement (as a function of that price) relative to

the values without agreement. In general, the Nash bargaining solutions are interdepen
dent as the value from one agreement depends on what happens in the other agreements.

For example, if negotiations break down with one conglomerate the value of another

conglomerate to the distributor might increase. To make progress (Horn and Wolinsky,

1988a,b), make a Nash equilibrium like assumption: they assume that each negotiating
pair takes the outcome of other negotiations as given. [52] This setup is often called ”Nash
in-Nash” bargaining. As Crawford and Yurukoglu point out, this is a strong assump
tion, since the members of each pair also participate in other negotiations and realize that

whether an agreement is reached, and what is that agreement, will impact other negotia
tions. Furthermore, because the negotiating parties participate in other negotiations they

will have asymmetric information. Nevertheless, in order to make progress much of the
empirical work has relied on this assumption. [53]

Formally, let _p_ _[ω]_ _rj_ [be the wholesale price, or input cost, paid by distributor] _[ r]_ [ for chan-]
nel _j_, which is owned by conglomerate _f_ . Note that the distributors in this setting are

equivalent to downstream retailers and the conglomerates are the equivalent of upstream


52In bilateral negotiation, Rubinstein (1982) and Binmore et al. (1986) show that the Nash bargaining
solution corresponds to the unique subgame perfect equilibrium of an alternating offers non-cooperative
game. Collard-Wexler et al. (2019) provide conditions such that the Horn and Wolinsky solution is the same
as the unique perfect Bayesian equilibrium with passive beliefs of a specific simultaneous alternating offers
game with multiple parties.
53See Lee and Fong (2013), Ho and Lee (2019), Ghili (ming) and Liebman (2018) for alternatives.


62


manufacturers. Let _**p**_ _[ω]_ denote the vector of all wholesale prices, and let _**p**_ _[ω]_ _rf_ [be the vec-]
tor of wholesale prices paid for the channels of conglomerate _f_ . The conglomerate and
the distributor negotiate over the vector of wholesale prices, _**p**_ _[ω]_ _rf_ [. If negotiations break]
down the distributor will not have access to any of the conglomerate channels. The Nash
bargaining solution determines the prices _**p**_ _[ω]_ _rf_ [, taking as given all other prices] _**[ p]**_ _[ω]_ _−rf_ [, to]
maximize distributor _r_ ’s and conglomerate _f_ ’s Nash Product, defined by


_NPrf_ ( _**p**_ _[ω]_ _rf_ [;] _**[ p]**_ _[ω]_ _−rf_ [) = [] _[π][r]_ [(] _**[p]**_ _[ω]_ _rf_ [;] _**[ p]**_ _[ω]_ _−rf_ [)] _[−][π][r]_ [(] _[∞]_ [;] _**[ p]**_ _[ω]_ _−rf_ [)]] _[ζ][rf]_ [[] _[π][f]_ [(] _**[p]**_ _[ω]_ _rf_ [;] _**[ p]**_ _[ω]_ _−rf_ [)] _[−][π][f]_ [(] _[∞]_ [;] _**[ p]**_ _[ω]_ _−rf_ [)]][(1] _[−][ζ][rf]_ [)] _[,]_ [ (5.2)]


where _ζrf_ is a parameter that measures the (relative) bargaining power of _r_ when bargaining with _f_, and _πr_ and _πf_ are the profit functions of _r_ and _f_, respectively, when an
agreement is reached and when it is not (denoted by _**p**_ _[ω]_ _rf_ [=] _[ ∞]_ [). Note, that the infinite]
price in the case of disagreement reflects that the distributor will not have access to any of

the conglomerate channels. These profit functions are determined endogenously by parts

of the model explained below.

Two key determinants of the bargaining outcome are the bargaining power, captured

by _ζrf_, and the bargaining leverage, which is the loss from disagreeing relative to reaching

an agreement. The bargaining parameter varies between zero, where _f_ has all the bar
gaining power and the solution is equivalent to Nash-Bertrand pricing by the upstream

providers, and one, where _r_ has all the bargaining power and can impose its will (subject

to a participation constraint by _f_ ). Values between the two extremes allow for different
relative bargaining power. [54]


The leverage of the parties impacts the solution in a similar way: everything else equal

the bargaining solution is closer to the optimal solution of the party with the greater lever
age, namely the party with less to lose from a disagreement. For example, if distributor _r_
is negotiating with two different conglomerates _f_ and _f_ _[′]_ and the only difference is that


_πf_ ( _**p**_ _[ω]_ _rf_ [;] _**[ p]**_ _[ω]_ _−rf_ [)] _[ −]_ _[π][f]_ [(] _[∞]_ [;] _**[ p]**_ _[ω]_ _−rf_ [)] _[ > π][f]_ _[′]_ [(] _**[p]**_ _[ω]_ _rf_ _[′]_ [;] _**[ p]**_ _−_ _[ω]_ _rf_ _[′]_ [)] _[ −]_ _[π][f]_ _[′]_ [(] _[∞]_ [;] _**[ p]**_ _[ω]_ _−rf_ _[′]_ [)] _[.]_


Namely, that relative to _f_ _[′]_, _f_ has more to gain from an agreement, or more to lose from a
disagreement, then _f_ _[′]_ has more leverage and will obtain an outcome that is more favor
able from its prospective.


54To formally see these claims, note that the maximization problem is equivalent to maximizing the log
of the Nash product. Taking the first-order condition of the log of the Nash product and slightly rearranging
we see that the resulting first-order condition is just a weighted average of the maximization problems of _r_
and _f_, with the weights being a product of the relative bargaining leverage and bargaining power.


63


To compute the profit functions of both the conglomerate and the distributors Craw
ford and Yurukoglu estimate a viewership model and bundle (subscription) choice model.

They then back out the implied input cost from the bundle pricing equation and use it to

fit a parametric cost function for the distributors. The details of their modeling (and esti
mation) are a bit different from, for example, BLP, but the principle is the same: the pricing

equation and demand estimates are used to back out input costs or estimate an input cost

function. These input costs can then be used, the same way prices were used in the basic

supply model, to either recover costs (here these are upstream costs) or parameters of the

supply model (here bargaining parameters).

In their application, Crawford and Yurukoglu assume that upstream marginal costs

are zero and therefore they estimate the bargaining parameters. They do so by choosing
the bargaining parameters, _ζrf_ that minimize the difference between the programming
costs they recovered from the pricing and demand equations and those predicted by the

bargaining model. One way to implement this idea is to write


_p_ ˆ _[ω]_ _rj_ [=] _[ p]_ _rj_ _[ω][∗]_ [(] _[ζ][rf]_ [(] _[j]_ [)][) +] _[ ϵ][rj]_ (5.3)


where ˆ _p_ _[ω]_ _rj_ [is the wholesale price backed out from the pricing equation,] _[ p]_ _rj_ _[ω][∗]_ [(] _[ζ][rf]_ [(] _[j]_ [)][)][ is the]
wholesale price that maximizes the Nash product defined in (5.2) and _ϵrj_ is measurement
error, or an ”add-on” error term. The parameters _**ζ**_ can be estimated using, for example,

non-linear least squares.

Note, that the bargaining parameters vary by conglomerate and not channel and there
fore in principle are of lower dimension than the wholesale prices. In practice, Crawford

and Yurukoglu (2012) do not have enough variation to meaningfully estimate channel
level wholesale prices and instead estimate these at the conglomerate-level. This is of

little economic significance because the way they set up the bargaining model all that

matters is the total payment to each conglomerate. Furthermore, for computation rea
sons they solve the model for a market with ”typical” distributors. The bottom line is

that they have the same number of parameters as observations in the above equation and

therefore can compute the set of bargaining parameters that set the backed out input cost

exactly equal to those predicted by the bargaining model. This directly parallels the non
parametric approach to recovering cost discussed in the Introduction to this section. In

this approach some view the bargaining parameters as the ”error terms.”

In other settings (Grennan, 2013; Bagwell et al., 2020), the number of observations in

(5.3) is larger than the number of bargaining parameters and then those are estimated,


64


for example, by non-linear least squares. [55] In principle, the bargaining parameters can

be estimated jointly with the pricing and demand parameters, but computationally it is

easier to estimate them separately.

Using the estimated parameters Crawford and Yurukoglu are able to simulate the

model both with bundling, as in the data, and when the consumers are offered channels

`a la carte. They find that equilibrium effects are significant: the counterfactuals suggest

that `a la carte offering of channels will increase input prices enough to offset consumer

benefits from being able to choose only the channels they value most. Thus, unbundling

will decrease welfare.

It is possible to set up, at least for some bargaining problems, a ”structural” error

term that follows a bit more closely the logic of the model discussed in Sections 5.1-5.3.

This approach especially makes sense when the upstream costs are unknown and need

to be estimated: it seems natural to assume that the error term consists of unobserved
variation in marginal costs. Gowrisankaran et al. (2015) do precisely that. [56] They study

the effects of mergers when prices are negotiated using data from negotiations between

hospitals and health insurance companies, or managed care organizations (MCOs), to

demonstrate the effect. Following Town and Vistnes (2001) and Capps et al. (2003) they

set up the bargaining problems as follows. Let _r_ denote the MCO, and _f_ denote a system
of hospitals that includes hospitals _j ∈Jf_ . The negotiation is over the price that the MCO

will pay the hospital if one of its enrollees receives care in that hospital.

In this setting the MCO is the equivalent of the retailer or distributor, and the hos
pital system is the equivalent of the manufacturer or conglomerate. The Nash product

for this problem follows equation (5.2), with a small difference that the profit functions,

and therefore the Nash product, are a function of wholesale prices and the ”network”
(i.e., which MCO-hospital system pairs that reach an agreement). [57] Specifically, hospital

system, _f_ profit from an agreement relative to disagreement is given by


     
_qrj_ ( _N_ _,_ _**p**_ _[ω]_ )[ _p_ _[ω]_ _rj_ _[−]_ _[mc][rj]_ []] _[,]_ (5.4)
_j∈Jf_


55For consistency of the estimates, generally, the error term in (5.3) cannot appear inside _**p**_ _ω∗_ ( _·_ ) and
therefore needs to be an ”add-on” error term that is usually interpreted as ”measurement error”.
56Grennan (2013) also estimates costs parameters, but his econometric error term is in the bargaining
parameter.
57This is not a meaningful distinction because an infinite wholesale price can denote disagreement. The
main reason for the change in notation is to be more explicit about networks, which are of greater importance in health care where not all MCOs contract with all hospital systems.


65


where _p_ _[ω]_ _rj_ [is the price] _[ r]_ [ pays] _[ f]_ [ if one of its enrollees is treated in hospital] _[ j]_ [,] _**[ p]**_ _[ω]_ [ is the]
collection of all prices, _N_ is a description of the network (i.e., which hospitals have contracts), _qrj_ ( _N_ _,_ _**p**_ _[ω]_ ) are the patients that go to hospital _j_ given the network and the vector of
prices, _mcrj_ is the marginal cost of treating those patients (which are assumed (i) constant
in quantity; and (ii) to vary by MCO to allow for different composition of enrollees.) This

formulation assumes that patients do not go out of network and will not switch insurance

providers in the case of disagreement.
On the MCO side, the value of an agreement is given by _πr_ ( _Nr,_ _**p**_ _[ω]_ ) _−_ _πr_ ( _Nr \ Jf_ _,_ _**p**_ _[ω]_ ).
_πr_ ( _·_ ) is the value to the MCO of having a network (with and without system _f_ ). Note, that

as before, a breakdown in negotiation means the whole system leaves the network. The
paper builds _πr_ ( _·_ ) from micro-foundation based on consumers’ willingness-to-pay for an

insurance product that has a wider network.

They show that one can write the first-order conditions of the bargaining problem as



_∂qrk_

[�] _k∈Jf_ _∂p_ ~~_[ω]_~~ _rj_ [[] _[p]_ _rk_ _[ω]_ _[−]_ _[mc][rk]_ []]

~~�~~ _[ω]_



_qrj_ + [�]
(1 _−_ _ζrf_ )



_._ (5.5)



_rj_ = _−_ _ζrf_

_k∈Jf_ _[q][rk]_ [[] _[p]_ _rk_ _[ω]_ _[−]_ _[mc][rk]_ []]



_A_

~~�~~ �� ~~�~~
_∂πr_ ( _Nr,_ _**p**_ _[ω]_ )

_∂p_ _[ω]_ _rj_
_πr_ ( _Nr,_ _**p**_ _[ω]_ ) _−_ _πr_ ( _Nr \ Jf_ _,_ _**p**_ _[ω]_ )

- ~~�~~ - ~~�~~
_B_



The assumption of constant marginal costs implies that the first-order conditions in equa
tion (5.5) are separable across MCOs and therefore one can rearrange the joint system of
#( _Jf_ ) first-order conditions from (5.5) to write


_**q**_ + Ω( _**p**_ _−_ _**mc**_ ) = _−_ Λ( _**p**_ _−_ _**mc**_ ) (5.6)


where Ω and Λ are both #( _Jf_ ) _×_ #( _Jf_ ) size matrices, with elements Ω _jk_ = _∂q∂prk_ ~~_[ω]_~~ _rj_ [and]

Λ _jk_ = 1 _−ζrfζrf_ _BA_ _[q][rk]_ [. Solving for the equilibrium prices yields]


_**p**_ = _**mc**_ _−_ (Ω+ Λ) _[−]_ [1] _**q**_ _,_ (5.7)


where _**p**_, _**mc**_ and _**q**_ denote the price, marginal cost and quantity vectors respectively for

an MCO _r_ across the different hospitals. Equation (5.7), which characterizes the equi
librium prices, has a form almost identical to standard pricing games, but differs in the

inclusion of Λ. One case where Λ = 0 – and hence there is differentiated-products Nash

66


Bertrand pricing with individual prices for each MCO – is where hospitals have all the
bargaining weight, _ζrf_ = 0 _, ∀f_ .
Importantly, equation (5.7) shows that, as with static differentiated-products pricing

models, we can back out implied marginal costs for the bargaining model as a closed
form function of prices, quantities and derivatives, given MCO and patient incentives.

Furthermore, one can combine equation (5.7) with an assumption about cost, as in Section

4.3.2,
_mcrj_ = w _rj_ _**γ**_ + _ωrj_


to form a basis for estimation where _ωrj_ is the structural error term and can be used to
form a GMM objective function, as in equation (4.12).

The above discussion makes it clear that bargaining models can be specified in a vari
ety of ways that impact formulation as well as identification and estimation. Our discus
sion is just an introduction to the topic, which is further explored by Lee et al. (2021) in

this Handbook.

# **6 Extensions of the Demand Model**


In this section we discuss some of the extensions of the discrete choice demand model

discussed in Section 3. We start by outlining some extensions to the static model and then

discuss models of dynamic demand.

## **6.1 Extensions to the Static Demand Model**


A reasonably large literature has explored several extensions to the basic discrete choice

models discussed in Section 3. The motivation for these extensions varies. Some exten
sions are motivated by a desire to better marry the model with patterns observed in micro

data, and potentially explore the biases that would arise if we ignore these differences.

Other extensions are needed to address specific questions that the basic model could not

address. In many cases, the extensions are estimated using individual data, and therefore

might not generalize to the various applications previously discussed.

Here we focus on two such extensions: multiple goods and a more general charac
teristics model. There are other extensions that have been considered in the literature.

For example, Dubin and McFadden (1984) and Hanemann (1984) propose a model where

consumers make a discrete choice, say choose an appliance, followed by a continuous


67


choice, for example, how much to use that appliance. The two decisions are obviously

interlinked. These ideas have been used more recently in looking, for example, at store

choice (Smith, 2004; Thomassen et al., 2017) and in choice of internet service plan and

usage (Malone et al., 2020; Nevo et al., 2016).

Other areas that have received considerable attention are models where consumers do

not know the characteristics of the products and have to learn them through search. See

Honka et al. (2019) for a survey of this literature.


**6.1.1** **Multiple goods**


A common complaint about discrete choice models is that actual purchases, when they

are observed, are not of a single product or a single unit. For example, when studying

the purchase of cereal we might observe consumers buying, on a single shopping trip,

several boxes of the same cereal brand or buying several brands. One way to rationalize

the multiple choices is to assume a single purchase instance, which is what we observe, is

an aggregation over several consumption instances, which is what we are modeling. For

example, a consumer shopping in a store might be buying for several household mem
bers for a week. If we assume that there are 3 household members, each making a daily

consumption choice then we can view the single observed purchase as aggregation over

21 consumption choice instances. This can help rationalize purchase of multiple units,

as well as different brands, and is probably sufficient when working with aggregate data

where the individual choices are not observed anyway and we are already aggregating

across consumers. However, this explanation is somewhat unappealing when working

with individual-level data, in part because it assumes the choices across days are inde
pendent. Therefore, a somewhat better alternative is to more explicitly build the purchase

model from underlying choices.

One way to model multiple choices is to redefine what we mean by an option. For

example, assume that there are two brands, A and B, and consumers can buy no more

than 2 units of each. This gives 9 options, ranging from not buying either brand to buying

2 of each brand. The utility from each option could in principle, be additive, in the utility

from each brand separately or have interactions. For instance if buying one unit of each

brand there could be an interaction term, which can be positive or negative, so that the

utility is not just the sum of the utilities of buying each brand.

Gentzkow (2007) takes this approach when studying consumers’ choice between print

and online newspapers. He allows for purchase of more than one option and estimates


68


an interaction term in the utility function (to understand if print and online newspapers

are complements of substitutes.) In his setting, consumers choose between the printed

version of a newspaper, the online version, both, or neither. Thus, the choice is a discrete

choice between bundles. He further assumes that each bundle receives an i.i.d. shock,

as in the standard discrete choice model, and therefore he can estimate the model using

standard methods. Note, that this assumption requires that any correlation between op
tions, which include the same products, is captured through the rest of the utility terms.

Furthermore, this approach is feasible when the number of choices is small, since the

number of bundles increases exponentially with the number of products. For example,

with _J_ = 20 different options and even if the consumer can only choose at most one of
each there are 2 [20] = 1 _,_ 048 _,_ 576 different bundles available.

Another approach, proposed by Hendel (1999), and later also used by Dub´e (2004)

builds the demand explicitly from underlying tasks. Specifically, Hendel observes firms

simultaneously buying several brands of computers and several units of each brand. To

model this, he assumes that the firm has several tasks to do. For each task there is an

optimal choice, but the observed purchases are an aggregation over several tasks. He

does not allow for interaction in the utility from the different choices. He explains the

purchase of several units, of the same computer, by a decreasing marginal utility from

quantity, hence there is interaction in this dimension.

Fan (2013) studies mergers in the newspaper industry. She allows consumers to buy

more than a single newspaper (but at most one copy of each) and introduces a parameter

that measures the decrease in utility from a newspaper if it is bought ”second”. Therefore,

like Gentzkow (2007) she allows for an interaction in utility, but at the same time, like

Hendel (1999), does not treat the bundle as an independent option.

Nevo et al. (2005) study the decision of libraries to subscribe a subset of the 150 or so to

Economics and Business journals that they observe. The libraries in their data subscribe

to some subset of these 150 journals, but the subsets are not nested. If they were nested,

we could model the choice of a bundle as a choice of how many journals to purchase.

Instead, they model the choice problem as ranking journals by an index like that standard

index in discrete choice models, for example the one given in equation (3.3). Unlike the

standard discrete choice problem where the decision maker only chooses the top option,

here the decision maker subscribes to journals following this ranking until a (budget or

other) constraint is met. The utility from the journals does not interact (i.e., the utility

does not depend on what other products are in the bundle), but the interaction is through


69


a (budget) constraint. They show how one could estimate this model using library-level

subscriptions.


**6.1.2** **General Characteristics Demand Models**


In Section 3.1, when we discussed the various demand models, we separated models in

product space from models in characteristics space. For models in characteristics space

we focused on discrete choice models. The idea of using characteristics to reduce the

dimension of the estimation problem can be useful more generally. This turns out to

be especially helpful when trying to estimate demand for more than a single product

category. As such, this model offers an additional way to deal with multiple purchases.
Dubois et al. (2014) study such a problem. [58] They note, looking at household-level

purchase data from France, the United Kingdom and the United States, differences across

countries in the choices households make and in the prices and product offerings they

face. These differences amount to large difference in the nutritional intake. For example,

the average French consumer purchases roughly 200 calories less a day than the average

American consumer. They ask the extent to which cross-country differences in purchases

are attributable to differences in prices and the characteristics of products (the economic

environment). To address this question they develop a model in characteristics space,

based on Gorman (1980) and Lancaster (1966), that does not assume discrete choice. Their

motivation is to use the richness of their data, which include disaggregated purchases,

while still looking at the choice of a food ”bundle” rather than narrowly defined products

(e.g., soft drinks).

Specifically, a consumer _i_, with demographics _Di_, chooses from _J_ products, where
product _j_ is characterized by _K_ characteristics _{aj_ 1 _, .., ajK}_ and _K_ is much smaller than

_J_ . These characteristics will in principle include both observed characteristics, like calo
ries and protein in their example, and unobserved characteristics, which we previously
denoted by _ξ_ . The utility is given by _U_ ( _q_ 0 _,_ _**x**_ _,_ _**q**_ ; _Di_ ) where _q_ 0 is the amount of the numeraire good consumed, _**x**_ is a _K ×_ 1 vector of characteristics of food consumed by the
consumer across all the products and _**q**_ is a _J ×_ 1 vector of the quantities purchased of
all food products. Define the _J × K_ matrix _**A**_ _≡{ajk}j_ =1 _,..,J,k_ =1 _,..,K_ . This matrix will be


58See also Pinkse et al. (2002) who study competition between gas stations, and Pinkse and Slade (2004)
who study the beer market. In both cases they model demand using a system in products space, and model
the substitution matrix as a function of either physical distance or distance in attribute space. The resulting
system is a statistical mapping between price and quantities, but is not derived from a well defined utility
function nor is it guaranteed to be consistent with utility maximization.


70


used to transform the quantities of products purchased, given by _**q**_ into the characteristics
that they contain. [59] The household maximizes utility by choosing _**q**_, subject to a budget

constraint:

max _U_ ( _q_ 0 _,_ _**x**_ _,_ _**q**_ ; _Di_ )
_**q**_


_J_

    _s.t._ _**x**_ = _**A**_ _[′]_ _**q**_ ; _qj ≥_ 0 _, j_ = 0 _,_ 1 _..., J_

_j_ =0 _[q][j][p][j][ ≤]_ _[y][i]_ [ ;]


where _pj_ is the price of one unit of product _j_, and _yi_ is the household’s income.
Following standard arguments (and dropping the _i_ subscripts) this can be written as


            - _y −_ _**p**_ _′_ _**q**_            max _U_ _,_ _**A**_ _[′]_ _**q**_ _,_ _**q**_
_**q**_ _p_ 0


_s.t._ _qj ≥_ 0 _._


Assuming that quantities _{qj}_ _[J]_ _j_ =0 [are continuous, the first-order conditions are]



_K_ _∂U_

_−_ _[∂U]_
_k_ =1 _[a][jk]_ _∂xk_ _∂q_ 0



_K_




_∂q_ 0



_pj_
+ _[∂U]_ = 0 if _qj >_ 0 _._
_p_ 0 _∂qj_



This model nests various standard models. First, suppose the utility function is _U_ ( _q_ 0 _,_ _**x**_ ),

which is the case in discrete choice models or in hedonic models (Court, 1939; Griliches,

1961; Rosen, 1974; Epple, 1987). Because the transformation from products to characteristics is linear and in this case _∂U/∂qj_ = 0, at most _K_ of the _J_ products would be
purchased. If we restrict _qj ∈{_ 0 _,_ 1 _}_ and [�] _j_ _[J]_ =1 _[q][j][ ≤]_ [1][, the model collapses to the standard]
discrete choice model. In general, the prediction that at most _K_ products are purchased

is a problem since we would like to consider cases where the number of products chosen

is (much) greater than the number of observed characteristics.

Alternatively, if the utility function is _U_ ( _q_ 0 _,_ _**q**_ ) then we can generate standard demand

systems in product space. If we allow for a characteristic that is product-specific then

a model in characteristics space is equivalent to a model in product space, as long as

the characteristics do not vary over time or markets. Note, that we need more than just

different values on a small number of unobserved characteristics, but a totally different
characteristic that can _only_ be obtained from each product. To better understand the role

of the characteristics in this model we rewrite the first-order conditions for _j_ such that


59This linear transformation is quite natural for characteristics like calories, sugar and protein, where it
seems natural to aggregate across products. The linear transformation is less intuitive when it comes to
characteristics like _ξ_ in (3.3) that represent demand shocks more generally.


71


_qj >_ 0 as
_∂U/∂qj_
= _[p][j]_
_∂U/∂q_ 0 _p_ 0



_K_ _∂U/∂xk_

_k_ =1 _[a][jk]_ _∂U/∂q_



_K_

 
_[p][j]_ _−_

_p_ 0 _k_



_._
_∂U/∂q_ 0



Consider the case where characteristics do not enter the utility, i.e., _∂U/∂xk_ = 0. The
first-order conditions, in this case _[∂U/∂q][j]_ [=] _[p][j]_ [, which implicitly defines the demand corre-]




_[∂U/∂q][j]_ _[p][j]_

_∂U/∂q_ 0 [=] _p_ 0



first-order conditions, in this case _∂U/∂q_ 0 _[j]_ [=] _p_ 0 _[j]_ [, which implicitly defines the demand corre-]

spondence. A similar idea applies in the above model. Demand depends on the _hedonic_

_∂U/∂xk_

_prices_ of each good instead of prices. The hedonic prices, _[p][j]_ _[−]_ [�] _[K]_ _[a][jk]_ [, depend on]



_∂U/∂xk_

_[p][j]_

_p_ 0 _[−]_ [�] _k_ _[K]_ =1 _[a][jk]_ _∂U/∂q_ 0



_prices_ of each good instead of prices. The hedonic prices, _p_ 0 _[j]_ _[−]_ [�] _k_ =1 _[a][jk]_ _∂U/∂q_ 0 _k_ [, depend on]

the marginal utility of the consumer from the characteristics. In other words, if two prod
ucts have the same price but one has more of a characteristic, with a positive marginal

utility, then the effective price to the consumer will be lower for the product with the

higher value of the characteristic.

To estimate the model Dubois et al. (2014) focus on a particular functional form for util
ity and use rich household level data from France, the United Kingdom and the United

States. They use the estimated parameters to decompose the cross-country differences

into variation coming from differences in preferences and variation coming from the differences in the economic environment. [60]


## **6.2 Dynamic Demand**

Up to this point the models we discussed were static. In this section we explore the im
plications of dynamic demand. Dynamics in demand can arise for a variety of reasons,

including switching costs, learning, storable and durable products, non-separable (over

time) utility, pricing (e.g., monthly usage caps) that creates dynamic linkage, and other

reasons. Here we will mostly focus on storable and durable products. We will discuss

patterns in the data that suggest that dynamic demand is relevant, and discuss the im
plications of ignoring dynamics. We will then review some of the main modeling and

estimation challenges and solutions that have been offered in the literature.


**6.2.1** **Storable Products**


Many of the products that have been studied using the methods presented earlier in this

section are storable: in the sense that consumers can buy them in one period and con
sume in another. Furthermore, a typical pricing pattern in these markets involves short

lived price reductions (”sales”), with a return to the regular price. This pattern of prices


60Allcott et al. (2019) use a similar demand system, estimated somewhat differently, to study food deserts
in the U.S.


72


generates an incentive for consumers to purchase the product when the price is low and

store it for future consumption. Boizot et al. (2001) and Pesendorfer (2002) were among

the first to study the effects of temporary price reductions and storability in the economics

literature.

The empirical literature has found evidence consistent with the theoretical idea that

consumers have incentives to purchase not for immediate consumption but for inventory.

For example, Pesendorfer (2002), and Hendel and Nevo (2006b, 2013) find that aggregate

quantity sold depends on duration from previous sale, controlling for the current price.

Hendel and Nevo (2006b) show that a household’s likelihood of purchasing during a

temporary price reduction is correlated with proxies of storage costs. They also show

that when a household purchases during a temporary price reduction the duration to the

next purchase is longer (consistent with the household buying for storage rather than im
mediate consumption), and households who purchase more often on sale also purchase

less frequently overall (again consistent with the idea that these households store their

purchases).

Stockpiling behavior has several implications for demand estimates and how they

should be used. If consumers purchase for storage, and the evidence suggest that they

do, then there is a difference between the short-run response to a temporary price change,

and the long-run response to either a temporary or permanent price change. For most

economic applications we care about long-run changes. In many data sets temporary

price changes account for most of the observed variation in prices. Short-run responses

to temporary price reductions, interpreted through a static model, overestimate the long
term own-price effects. Typically, there is a large response to a temporary price reduc
tion, which in a static model is attributed to an increase in consumption (which in a

static model equals purchase), and not to an increase in storage. Similarly a post price

reduction dip, also often observed in the data, coincides with an increase in price, and

is mis-attributed by a static model as a decline in consumption. At the same time, static

estimation underestimates cross-price effects: the temporary price reduction diverts cur
rent sales from competing products, but it also diverts future sales (and past sales to the

extent that the reduction was at least partially anticipated). A static model misses these

additional effects and therefore underestimates the impact on other products.

The basic model of consumer stockpiling is an inventory model. Hendel and Nevo

(2006b) propose such a model for a homogeneous good, which abstracts from product

differentiation and assumes that purchases are of continuous quantities.


73


The per period utility consumer _i_ obtains from consuming at time _t_ is


_ui_ ( _ct_ + _νt_ ) + _αiq_ 0 _t,_ (6.1)


where _ct_ is the quantity consumed in _t_, _νt_ is a shock to utility that changes the consumption needs of the consumer, and _q_ 0 _t_ is the numeraire good consumed at time _t_ . Facing
random prices, _pt_, in each period the consumer has to decide how much to buy, denoted

by _qt_, and how much to consume, denoted by _ct_ . The consumer’s problem can therefore

be represented as


_V_ ( _**s**_ _t_ ) = _max_ ( _ct_ ( _·_ ) _,qt_ ( _·_ ))      - _∞t_ =1 _[δ][t][−]_ [1][E][ [] _[u]_ [(] _[c][t]_ [ +] _[ ν][t]_ [)] _[ −]_ _[C]_ [(] _[i][t]_ [) +] _[ αp][t][q][t][ |]_ _**[ s]**_ _[t]_ []]

(6.2)

_s.t._ 0 _≤_ _it,_ 0 _≤_ _ct_ 0 _≤_ _qt it_ = _it−_ 1 + _qt −_ _ct,_


where _α_ is the marginal utility from income, _δ_ is the discount factor, and _C_ ( _it_ ) is the

cost of storing inventory. The information set, or state space, at time _t_, _**s**_ _t_, consists of the

current inventory, _it_, current prices, and the current shock to utility from consumption, _νt_ .

Consumers face two sources of uncertainty: utility shocks and future prices. Hendel and

Nevo assume that shocks to utility, _νt_, are i.i.d. over time. Prices are assumed to evolve

according to a first-order Markov process and take on two states, sale and non-sale.

They show that within this setup the optimal consumer behavior is characterized by a

trigger _s_, and a target inventory _S_ . The target, _S_, is a decreasing function of current price.

On the other hand, the trigger, _s_, which is the sum of the target and current consumption,

depends on prices and the utility shock. They also show that the quantity purchased is a

function of lagged inventory, the current prices and the current utility shock.

A key challenge is how to expand this model to differentiated products. In principle,

this is simple: we can just make all the quantities in (6.1) vectors. This, of course, rein
troduces the dimensionality problem discussed in Section 3, except now the problem is

even worse and includes the well-known ”curse of dimensionality” in dynamic problems

(Rust, 1994). To deal with these issues, Hendel and Nevo (2006a) propose the following
model. [61] Now consumer _i_ can purchase one of _J_ + 1 brands (including a no purchase
decision), which come in different sizes, indexed by _q ∈{_ 1 _,_ 2 _, ..., Q}_ . Let _djqt_ equal to 1 if
the consumer purchases brand _j_ of size _q_ at time _t_, and 0 otherwise. Consumers make a


61See Aguirregabiria and Nevo (2013) for a more detailed discussion.


74


