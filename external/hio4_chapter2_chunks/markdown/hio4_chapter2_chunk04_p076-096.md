discrete choice, so in this model stockpiling is achieved by buying larger sizes rather than

by buying a larger quantity as in the homogeneous good case.
The consumer also has to decide how much to consume each period. [62] To reduce the

state space Hendel and Nevo assume that the per period utility consumer _i_ obtains from

consuming in _t_ is the same as in equation (6.1). This assumption implies that there is no

differentiation in consumption: consumers care only about the quantity they consume but
not the brand. [63] They further assume that inventory cost depends only on total inventory,

hence _C_ ( _it_ ) for inventory _it_ . They introduce differentiation by assuming an instantaneous

utility associated with preference for the purchased brand. At period _t_ = 1, the purchase
and consumption decisions, _{c, j, q}_, are made to maximize


   - _∞_
_t_ =1 _[δ][t][−]_ [1][E][ [] _[u][i]_ [(] _[c][t]_ [ +] _[ ν][t]_ [)] _[ −]_ _[C][i]_ [(] _[i][t]_ [) +] _[ x][jqt][β][i]_ [ +] _[ α][i][p][jqt]_ [ +] _[ ξ][jqt]_ [ +] _[ ε][ijqt][ |]_ **[ s]** [1][]]

(6.3)



_s.t._ 0 _≤_ _it,_ 0 _≤_ _ct_ 


_j,q_ _[d][jqt]_ [ = 1] _[,]_ _it_ +1 = _it_ + [�]



_x_ _[d][jqt][q][t][ −]_ _[c][jt]_ _j_ = 1 _, ..., J_



where **s** _t_ is the information set at time _t_, _pjqt_ is the price of purchasing quantity _q_ of brand
_j_, _ξjqt_ is an unobserved (to the researcher) brand-specific quality, _xjqt_ are observed product
characteristics and _εijqt_ is a random shock. They allow _ξjqt_ to vary by brand in order to
capture differentiation across products, and across sizes.

The expectation E( _._ ) is taken with respect to the uncertainty regarding future shocks in
_νt_ and _**ε**_ _t_, and future prices (and other time-varying characteristics). They assume that _εijqt_
is i.i.d. type-1 extreme value, and as before that _νt_ is i.i.d. over time and across consumers.
Prices (and observed characteristics) evolve according to a first-order Markov process.
Let _Vi_ ( _**s**_ _t_ ) be the value function of consumer _i_ . Given the above assumptions _**s**_ _t_ consists
of inventory, _it_, a vector of current prices (and observed characteristics), which we will
denote (slightly abusing notation) by _**x**_ _t_, the scalar shock _νt_ and the vector of extreme
value shocks _**ε**_ _it_ . As usual in a dynamic programming problem, this value function can


62Alternatively, one can assume that consumption is constant over time, but varying across households,
and not a decision variable. A slightly more general model, than constant consumption, allows for random
shocks, that determine consumption. Both these models are nested within the above model and in principle
can be tested. The results in Hendel and Nevo (2006a) suggest that consumption is mostly constant, but
when inventory runs low consumers reduce consumption. This behavior is required to explain long periods
of no purchase followed by periods of frequent purchases observed in the data. Indeed, it is this variation
in inter-purchase time that identifies the utility from consumption.
63For the product they study, laundry detergents, this assumption makes sense. This of course raises
the question of why products are differentiated. Hendel and Nevo propose an interpretation that allows
differentiation in the linear part of the utility.


75


be obtained as the unique solution of a Bellman equation:


_Vi_ ( **s** _t_ ) = max
_{c,j,q}_ _[{][u][i]_ [(] _[c][t]_ [ +] _[ ν][t]_ [)] _[ −]_ _[C][i]_ [(] _[i][t]_ [) +] _[ x][jqt][β][i]_ [ +] _[ α][i][p][jqt]_ [ +] _[ ξ][jqt]_ [ +] _[ ε][ijqt]_


                     + _δ_ _Vi_ ( **s** _t_ +1) _dFs_ ( **s** _t_ +1 _|_ **s** _t, c, j, q_ ) _},_ (6.4)


where _Fs_ represents the transition probability of the vector of state variables. Given that
the state variables ( _νt,_ _**ε**_ _it_ ) are independently distributed over time, it is convenient to re
duce the dimensionality of this dynamic programming problem by using a value function

that is integrated over these i.i.d. random variables. The integrated value function, sometimes also called the ex-ante value function, is defined as _EVi_ ( _it,_ _**x**_ _t_ ) _≡_ - _Vi_ ( _**s**_ _t_ ) _dFε_ ( _**ε**_ _t_ ) _dFν_ ( _ν_ ),
where _F_ _**ε**_ and _Fν_ represent the CDFs of _**ε**_ _t_ and _νt_, respectively. The value function _EVi_ is
the unique solution of the integrated Bellman equation. Given the distributional assumptions on the shocks _**ε**_ _t_ and _νt_, the integrated Bellman equation is:



_ui_ ( _ct_ + _νt_ ) _−_ _Ci_ ( _it_ ) + _xjqtβi_ + _αipjqt_ + _ξjqt_


+ _δ_ E [ _EVi_ ( _it_ +1 _,_ _**x**_ _t_ +1) _| it,_ _**x**_ _t, c, j, q_ ]































  exp


_j_



 _dFν_ ( _νt_ ) _._




_EVi_ ( _it,_ _**x**_ _t_ ) = max
_c,q_




ln



(6.5)

Despite the significant reduction in size, the state space is still high dimensional.

Therefore, to reduce the dimension further, they note that the assumptions imply that

the optimal consumption does not depend on which brand is purchased. Formally, let
_c_ _[∗]_ ( _**s**_ _t_ ; _q, k_ ) be the optimal consumption conditional on state _**s**_ _t_ and on purchase of size _q_ .
Lemma 1 in the appendix of Hendel and Nevo (2006a) shows that _c_ _[∗]_ ( _**s**_ _t_ ; _q, k_ ) = _c_ _[∗]_ ( _**s**_ _t_ ; _q, j_ ) =
_c_ _[∗]_ ( _**s**_ _t_ ; _q_ ). In words, the optimal consumption does not depend on the brand purchased,

only on the size.

This result implies that the (integrated) Bellman equation in (6.5) can be written as


_EVi_ ( _it,_ _**x**_ _t_ ) =







��



exp _{ui_ ( _ct_ + _vt_ ) _−_ _Ci_ ( _it_ ) + _ωiqt_ + _δ_ E [ _EVi_ ( _it_ +1 _,_ _**x**_ _t_ +1) _| it,_ _**x**_ _t, c, q_ ] _}_

_q_



_dFν_ ( _νt_ ) _,_


(6.6)



max
_c,q_




ln



where _ωiqt_ is the inclusive value from all brands of size _q_, as defined by equation (3.10),
��    i.e., _ωiqt_ = ln _j_ [exp(] _[x][jqt][β][i][ −]_ _[α][i][p][jqt]_ [ +] _[ ξ][jqt]_ [)] . In words, the problem can now be seen as


76


a choice between sizes, each with a utility given by the size-specific inclusive value (and

extreme value shock). The dimension of the state space is still large and includes all

characteristics and prices, because we need all the prices to compute the evolution of the

inclusive value.

To further reduce the state space Hendel and Nevo assume


_F_ ( _**ω**_ _i,t_ +1 _|_ _**s**_ _t_ ) = _F_ ( _**ω**_ _i,t_ +1 _|_ _**ω**_ _it_ ( _**x**_ _t_ )) _,_ (6.7)


where _**ω**_ _it_ is a vector of inclusive values for the different sizes. In words, the vector _**ω**_ _it_
contains all the relevant information in _**s**_ _t_ to obtain the probability distribution of _**ω**_ _i,t_ +1
conditional on _**s**_ _t_ . Instead of all the prices (and characteristics) we only need a single in
dex for each size. Two vectors of prices (and characteristics) that yield the same (vector

of) current inclusive values imply the same distribution of future inclusive values. This

assumption is violated if individual prices have predictive power above and beyond the

predictive power of _**ω**_ _it_ . Therefore, if the inclusive values can be estimated outside the

dynamic demand model, the assumption can be tested and somewhat relaxed by includ
ing additional statistics of prices (and characteristics) in the state space. Note, that _**ω**_ _it_

is consumer-specific: different consumers value a given set of products differently and

therefore this assumption does not further restrict the distribution of heterogeneity.

Given these assumptions Hendel and Nevo (2006a) show that


_EVi_ ( _it,_ _**p**_ _t_ ) = _EVi_ ( _it,_ _**ω**_ _it_ ( _**p**_ _t_ )) (6.8)


In words, the expected future value only depends on a lower dimensional statistic of the

full state vector.

Hendel and Nevo estimate the model using consumer level data and using a three-step

procedure. First they estimate many of the parameters (including various fixed effects)

with a static conditional Logit model where they use the probability of choosing a brand
_conditional_ on the size being purchased (i.e. they consider only options that have the

same size as the size purchased). They show that for this conditional probability they
do not need to solve the dynamic programming problem. [64] Next, they use the first-stage


64The intuition for the result is similar to the result in Chamberlain (1980) who proposes to estimate a
fixed effects Logit model by conditioning such that the fixed effects drop out. The same happens here, but
with the expected value function, instead of a fixed effect.


77


estimates to compute the transition process of the inclusive values. Finally, they estimate
a nested fixed point as in Rust (1987) to estimate the remaining parameters. [65]


They find that estimates that do not account for dynamics overestimate own-price

elasticities by roughly 30 percent and underestimate cross-price elasticities by as much as

a factor of 5. They also find that static estimates overstate the substitution to the outside

option by over 200 percent. Together these suggest that static estimates, like the ones

discussed above, might underestimate price–cost margins and be downward biased in

predicting the effects of mergers (i.e., static estimates will predict effects that are lower

compared to the dynamic model). The models has implications for other policy debates

as well. For example, Wang (2015) finds that a static model will overestimate the effect of

a soda tax, by as much as 60%.


**6.2.2** **Durable Products**


Many of the papers we discussed above involve estimation of demand for durable goods

(Bresnahan, 1987; Berry et al., 1995). Static models miss two important dynamic effects.

First, whether a product is owned (and which one) is likely to impact purchases. For

example, a consumer who more recently purchased a cell phone might be less likely to

buy a new phone than a consumer who owns an older model. Second, purchase decisions

will depend on expectations about future prices and quality. Expectation about the future

are especially important when nominal prices are declining and quality increasing, as is

the case in many durable good industries. The decline in quality-adjusted prices creates

a trade off for consumers between purchasing today, and getting the benefits of usage

earlier, or delaying purchase and paying a lower price (or getting higher quality).

Initially, the literature separated the modeling between two cases: with and without

repeat purchase, as far as we can tell mostly because the no repeat purchase was eas
ier to deal with. More recently the literature has focused on the repeat purchase case,

which seems to better fit reality, and that is the one we mostly focus on here. With repeat

purchases the main issues with the static model are the ones discussed in the previous

paragraph. It is difficult to theoretically sign the direction of the bias in a static model,
but empirically it seems like static estimates are lower in absolute value. [66]


65They need to modify the Rust estimation algorithm to account for the fact that inventory, a state variable, is unobserved.
66Without repeat purchase the issues with the static model are a bit different. First, after consumers
purchase they leave the market, and if consumers are heterogeneous then the distribution of the remaining
consumers changes over time in a way that is not accounted for by the static model. Second, if consumers


78


Gowrisankaran and Rysman (2012) offer a framework that extends the static BLP

model and allows for dynamics. Interestingly, their model in several ways is similar to

the inventory model we presented in the previous section, where the role of inventory

is equivalent to the role of the quality of the product owned, in the model below. In the

durable good model ”stockpiling” means buying a higher quality product, i.e., ”stock
piling” quality rather than quantity. The real difference between the two models is in

the pricing patterns and therefore the trade-off faced by consumers. In storable goods

markets, consumers face temporary price reductions that create an incentive to purchase

today for future consumption. In durable goods markets the typical pattern is a decreas
ing quality-adjusted price, which creates an incentive to delay purchase, either by not

buying today or by buying a lower quality product, with the intention of replacing it
soon, or renting/leasing. [67]


To model these effects, let the (indirect) utility consumer _i_ gets from product _j_ at time

_t_ be given by:
_uijt_ = _xjtβi_ + _αipjt_ + _ξjt_ + _εijt,_ (6.9)


where the notation follows the definitions of the static model in Section 3. For what follows it is convenient to define the flow utility as _γijt_ _[f]_ [=] _[ x][jt][β][i]_ [ +] _[ ξ][jt]_ [. If the consumer does]
not purchase she gets the utility _ui_ 0 _t_ = _γi_ _[f]_ 0 _t_ [+] _[ ε][i]_ [0] _[t]_ [ where]



_γi_ _[f]_ 0 _t_ [=]




0
_γ_ _[f]_
_i_ [�] _j_ [�] _t_



if no previous purchase
(6.10)
if last purchase was product _j_ at time _t_ _[.]_

[�] [�]



This definition of the utility from the outside option is the main difference between the

static model and the dynamic model. In the static model, the utility from the outside good

is constant (and normalized to zero) across consumers and over time. In the dynamic

model, once consumers purchase, the utility from the outside option changes. Forward
looking consumers take this into account when making current choices. Assuming that (i)

the consumer holds at most a single product at any time and (ii) there is no resale market,


are forward-looking then they realize there is an option value to not purchasing today. This option value is
reflected in the value of the outside option, which in the static model is assumed constant. Melnikov (2013)
and Conlon (2012) offer models and empirical estimates of the no-repeat purchase model.
67In some cases, dynamics can also arise due to temporary price changes in durable goods markets. For
example, Busse et al. (2010) study the 2005 Employee Discount Pricing, and show that its main effect was
to induce consumers to purchase earlier.


79


then the Bellman equation of the consumer problem is given by



_Vi_ ( _**ε**_ _it, γi_ _[f]_ 0 _t_ _[,]_ _**[ x]**_ _[t]_ [) = max]
_j_ =0 _,...J_




- _uijt_ + _δ_ E[ _EVi_ ( _γijt_ _[f]_ +1 _[,]_ _**[ x]**_ _[t]_ [+1][)] _[|]_ _**[x]**_ _[t]_ []] _,_ (6.11)



where _EVi_ ( _γijt_ _[f]_ _[,]_ _**[ x]**_ _[t]_ [) =] - _Vi_ ( _**ε**_ _it, γijt_ _[f]_ _[,]_ _**[ x]**_ _[t]_ [)] _[dF][ε]_ [(] _**[ε]**_ _[it]_ [)][, and] _**[ x]**_ _[t]_ [ represents the set of prices and other]
product characteristics at period _t_ . The expectation is taken with respect to the uncertainty

regarding future products, prices and characteristics.

Note, that there is another similarity with the storable goods model. Here the utility
carried forward is _γijt_ _[f]_ [and not] _[ γ]_ _ijt_ _[f]_ [+] _[ ε][ijt][.]_ [ Thus, just like in the inventory model there is a]
separation between the utility at the time of purchase and the utility at the time of usage.

As is usually the case, it is convenient to work with the integrated value function. Even

with this, the state space includes the vector of all characteristics and prices, which is still

too large to practically work with. They reduce the state space in a similar way to what we

saw in the storable goods model. The state space also includes the quality of the products

currently held, which is equivalent to the inventory in the storable good problem. Because

they assume that the consumer only holds a single product, this quality is a scalar. In

more general models the consumer might purchase or hold multiple products, or multiple

units of the same product, and the dimension of quality would be higher. To reduce

the dimension of the state space, they rely, similar to the storable goods model, on the

inclusive value. However, it will be defined slightly differently here. Specifically, define

the dynamic inclusive value from the _J_ inside alternatives as:







_._ (6.12)



_ωit_ ( _**x**_ _t_ ) = ln




- _J_

 




exp( _γijt_ _[f]_ [+] _[ α][i][p][jt]_ [ +] _[ δ]_ [ E][[] _[EV][i]_ [(] _[γ]_ _ijt_ _[f]_ +1 _[,]_ _**[ x]**_ _[t]_ [+1][)] _[ |]_ _**[ x]**_ _[t]_ [])]
_j_ =1



Note, that this definition is different in an important way from the definition given in

equation (3.10). The above definition provides the expected value, including the future

value, from the _J_ options, while the definition in equation (3.10) provides the expected

flow utility, not accounting for the future value. The difference is not just semantic. The

static definition basically provides a (utility-consistent welfare) statistic that is a summary

of prices and characteristics of available products. The dynamic definition also includes

(endogenous) future behavior of the agent. Once we impose a particular stochastic structure on the evolution of _ωit_ a natural question is whether the imposed structure is consistent with the consumer optimization problem. Gowrisankaran and Rysman (2012) offer


80


some discussion on whether or not this is restrictive, but generally little is known on what

behavioral assumptions are consistent with the imposed structure.

Given this definition, Gowrisankaran and Rysman make a similar assumption to equa
tion (6.7) made in the storable goods model


_F_ ( _ωi,t_ +1 _|_ _**x**_ _t_ ) = _F_ ( _ωi,t_ +1 _| ωit_ ( _**x**_ _t_ )) _._ (6.13)


As before, the assumption is that the inclusive value is sufficient to compute the transition

probabilities, but now it is the dynamic inclusive value, _ωit_ . Furthermore, now there is a

single inclusive value rather than a vector of size-specific inclusive values, as was the case

for the stockpiling model.

Using this assumption we can now write


             -              - ��
_EVi_ ( _γi_ _[f]_ 0 _t_ _[,]_ _**[ x]**_ _[t]_ [) =] _[ EV][i]_ [(] _[γ]_ _i_ _[f]_ 0 _t_ _[, ω][it]_ [) = ln] exp( _ωit_ ) + exp _γi_ _[f]_ 0 _t_ [+] _[ δ]_ [ E][[] _[EV][i]_ [(] _[γ]_ _i_ _[f]_ 0 _t_ +1 _[, ω][it]_ [+1] _[|][ω][it]_ []] _._
(6.14)

Several studies that have estimated demand for durable products using household
level data. [68] However, Gowrisankaran and Rysman (2012) offer a way to estimate the

model using aggregate data, which directly extend the methods of BLP.

If consumer level data are observed then, in principle, identification follows the standard arguments (Rust, 1994; Magnac and Thesmar, 2002). [69] With aggregate data we do

not observe the purchase history of each consumer, which makes identification signifi
cantly more difficult. Intuitively, the key to identifying the model and to separating the

different alternative models is the ability of the models to explain both the cross-sectional

variation, across markets and products, and the time series variation.

We are unaware of a formal identification proof. Standard identification proofs for

static models require some form of substitution between products (Berry et al., 2013). In

static models the substitution is between products in a given period, but here the require
ment is for substitution over time and across products. This need not be satisfied. For

example, if the price of a high quality product falls at time _t_ it could actually increase the
demand for a low quality product at _t −_ 1, because some consumers might buy it for one

period.

The estimation, using aggregate data, follows closely the method proposed by Berry

et al. (1995), but nests a solution of the dynamic programming problem inside the inner


68For example, Erdem et al. (2005), or Prince (2008).
69The standard arguments need to be adjusted for the existence of _ξjt_, but with enough observations
these could be controlled for and then we are back in the standard case.


81


loop. The idea is to follow the algorithm detailed in Section 4.3.4, but in Step 1 in order

to compute the market shares we need to solve the dynamic problem for each of the

simulated individuals. This is done by computing the inclusive value (using equation

(6.12) and an initial guess for _EVi_ ) for each simulated individual _i_ . This in turn is used to
compute _F_ ( _ωit_ +1 _| ωit_ ( _**x**_ _t_ )), which is used to update _EVi_ . The process is continued until
it converges. If we think of the BLP algorithm as a nested fixed point, then here we have

another layer of nesting in order to compute the market shares.

# **7 Concluding Comments**


In this chapter we review the modern IO approach to modeling demand and supply in

differentiated products industries. In many cases, we only scratch the surface of many of

the topics we discussed and there are many topics that are left uncovered. For example,

many of the applications of the models we discussed are covered in other chapters of this

Handbook. The success of the methods we discuss here is reflected in their application to

areas such as health, finance, taxation, housing and school choice, development, environ
mental policy and political economy, that historically were very different than IO. This

is a positive trend that we hope will continue into the future as IO economists continue

developing more flexible models and improved computational methods.


82


# **References**

Ackerberg, D., L. Benkard, S. Berry, and A. Pakes (2007). _Econometric Tools for Analyzing_
_Market Outcomes_, Volume 6A, pp. 4171–4276. Amsterdam: North-Holland. Draft Date:

June, 2006.


Ackerberg, D. A. and M. Rysman (2005). Unobserved product differentiation in discretechoice models: Estimating price elasticities and welfare effects. _The RAND Journal of_
_Economics 36_ (4), 771–788.


Aguirregabiria, V. and A. Nevo (2013). Recent developments in empirical io: Dynamic demand and dynamic games. In D. Acemoglu, M. Arellano, and E. Dekel (Eds.), _Advances_
_in Economics and Econometrics: Tenth World Congress_, Volume 3 of _Econometric Society_
_Monographs_, pp. 53–122. Cambridge University Press.


Allcott, H., R. Diamond, J.-P. Dub´e, J. Handbury, I. Rahkovsky, and M. Schnell (2019).
Food Deserts and the Causes of Nutritional Inequality. _The Quarterly Journal of Eco-_
_nomics 134_ (4), 1793–1844.


Anderson, S. P., A. de Palma, and J.-F. Thisse (1992). _Discrete Choice Theory of Product_
_Differentiation_ . MIT Press.


Arellano, M. and S. Bond (1991). Some tests of specification for panel data: Monte
carlo evidence and an application to employment equations. _International Economic_
_Review 58_ (2).


Athey, S. and G. Imbens (2007). Discrete choice models with multiple unobserved choice
characteristics. _International Economic Review 48_ (4), 1159–1192.


Backus, M., C. Conlon, and M. Sinkinson (2021). Common ownership and competition

in the ready-to-eat cereal industry. Working Paper 28350, National Bureau of Economic

Research.


Bagwell, K., R. W. Staiger, and A. Yurukoglu (2020). Quantitative analysis of multi-party
tariff negotiations estimation of a model of entry in the airline industry. _Working paper_ .


Bain, J. S. (1951). Relation of profit rate to industry concentration: American manufacturing, 1936–1940. _The Quarterly Journal of Economics 65_ (3), 293–324.


83


Barten, A. (1966). _Theorie en Empirie van een Volledig Stelsel van Vraagvergelijkingen, Doctoral_
_dissertation_ . Rotterdam: University of Rotterdam.


Bayot, D., K. Hatzitaskos, B. Howells, and A. Nevo (2018). The aetna-humana proposed
merger. In _The Antitrust Revolution, Volume 7_ . Oxford University Press.


Berry, S. (1994). Estimating discrete-choice models of product differentiation. _The RAND_
_Journal of Economics_, 242–262.


Berry, S., A. Gandhi, and P. Haile (2013). Connected substitutes and invertibility of demand. _Econometrica 81_ (5), 2087–2111.


Berry, S., J. Levinsohn, and A. Pakes (1995). Automobile prices in market equilibrium.
_Econometrica 63_ (4), 841–890.


Berry, S., J. Levinsohn, and A. Pakes (1999). Voluntary export restraints on automobiles:
Evaluating a trade policy. _American Economic Review 89_ (3), 400–430.


Berry, S., J. Levinsohn, and A. Pakes (2004). Differentiated products demand systems from
a combination of micro and macro data: The new vehicle market. _Journal of Political_
_Economy 112_, 68–104.


Berry, S., O. Linton, and A. Pakes (2004). Limit theorems for estimating the parameters of
differentiated product demand systems. _Review of Economic Studies 71_ (3), 613–654.


Berry, S. and A. Pakes (1993). Some applications and limitations of recent advances in
empirical industrial organization: Merger analysis. _American Economic Review 83_ (2),

247–252.


Berry, S. and A. Pakes (2007). The pure characteristics demand model. _International Eco-_
_nomic Review 48_ (4).


Berry, S. T. and P. A. Haile (2014). Identification in differentiated products markets using
market level data. _Econometrica 82_ (5), 1749–1797.


Berry, S. T. and P. A. Haile (2021). Foundations of demand estimation. Volume 4 of
_Handbook of Industrial Organization_ . Elsevier.


Bhattacharya, D. (2018). Empirical welfare analysis for discrete choice: Some general
results. _Quantitative Economics 9_ (2), 571–615.


84


Binmore, K., A. Rubinstein, and A. Wolinsky (1986). The Nash bargaining solution in
economic modelling. _The RAND Journal of Economics_, 176–188.


Black, R., G. S. Crawford, S. Lu, and H. White (2004). A virtual stakes approach to measuring competition in product markets. _Technical Paper_ .


Blundell, R. and S. Bond (1998). Initial conditions and moment restrictions in dynamic
panel data models. _Journal of Econometrics 87_, 115–143.


Boizot, C., J.-M. Robin, and M. Visser (2001). The demand for food products: An analysis
of interpurchase times and purchased quantities. _The Economic Journal 111_ (470), 391–

419.


Bonnet, C. and P. Dubois (2010). Inference on vertical contracts between manufacturers
and retailers allowing for nonlinear pricing and resale price maintenance. _The RAND_
_Journal of Economics 41_ (1), 139–164.


Boyd, J. H. and R. E. Mellman (1980). The effect of fuel economy standards on the u.s.
automotive market: An hedonic demand analysis. _Transportation Research 14a_, 367–368.


Bresnahan, T. (1981). Departures from marginal-cost pricing in the american automobile
industry: Estimates for 1977-1978. _Journal of Econometrics 17_ (2), 201–227.


Bresnahan, T. F. (1982). The oligopoly solution concept is identified. _Economics Let-_
_ters 10_ (1), 87 – 92.


Bresnahan, T. F. (1987). Competition and collusion in the american automobile industry:
The 1955 price war. _The Journal of Industrial Economics 35_ (4), 457–482.


Bresnahan, T. F. (1989). Chapter 17 empirical studies of industries with market power.
Volume 2 of _Handbook of Industrial Organization_, pp. 1011 – 1057. Elsevier.


Busse, M. R., D. I. Simester, and F. Zettelmeyer (2010). “The Best Price You’ll Ever Get”:
The 2005 employee discount pricing promotions in the u.s. automobile industry. _Mar-_
_keting Science 29_ (2), 268–290.


Capps, C., D. Dranove, and M. Satterthwaite (2003). Competition and market power in
option demand markets. _RAND Journal of Economics 34_ (4), 737–763.


85


Cardell, N. and F. Dunbar (1980). Measuring the societal impacts of automobile downsizing. _Transportation Research 14a_, 423–434.


Cardell, N. S. (1997). Variance components structures for the extreme-value and logistic
distributions with application to models of heterogeneity. _Econometric Theory 13_ (2),

185–213.


Chamberlain, G. (1980). Analysis of Covariance with Qualitative Data. _The Review of_
_Economic Studies 47_ (1), 225–238.


Chamberlain, G. (1987). Asymptotic efficiency in estimation with conditional moment
restrictions. _Journal of Econometrics 34_ (3), 305–334.


Christensen, L., D. Jorgenson, and L. Lau (1975). Transcendental logarithmic utility functions. _American Economic Review 65_, 367–83.


Ciliberto, F. and J. W. Williams (2014). Does multimarket contact facilitate tacit collusion? inference on conduct parameters in the airline industry. _The RAND Journal of_
_Economics 45_ (4), 764–791.


Collard-Wexler, A., G. Gowrisankaran, and R. S. Lee (2019). _Journal of Political Econ-_
_omy 127_ (1).


Compiani, G. (2019). Market counterfactuals and the specification of multi-product de
mand: a nonparametric approach. Technical report, Working paper. 3, 43.


Conlon, C. (2012). A dynamic model of prices and margins in the lcd tv industry. _Working_
_paper_ .


Conlon, C. and J. Gortmaker (2020). Best practices for differentiated products demand
estimation with pyblp. _The RAND Journal of Economics 51_ (4), 1108–1161.


Corts, K. S. (1999). Conduct parameters and the measurement of market power. _Journal_
_of Econometrics 88_ (2), 227–250.


Court, A. T. (1939). Hedonic price indexes with automotive examples. The Dynamics

of Automotive Demand, edited by Charles F. Roos, pp. 99–117. New York: General

Motors.


86


Crawford, G. S. and A. Yurukoglu (2012). The welfare effects of bundling in multichannel
television Markets. _American Economic Review 102_ (2), 643–685.


Davidson, R. and J. G. MacKinnon (1989). Testing for consistency using artificial regressions. _Econometric theory_, 363–384.


Deaton, A. (1986). Demand analysis. Volume 3 of _Handbook of Econometrics_, pp. 1767–1839.

Elsevier.


Deaton, A. and J. Muellbauer (1980). An almost ideal demand system. _American Economic_
_Review 70_, 312–26.


Debreu, G. (1960). Review of R.D. Luce, individual choice behavior: A theoretical analysis. _American Economic Review 50_, 186–188.


Dixit, A. and J. Stiglitiz (1977). Monopolistic competition and optimum product diversity.
_American Economic Review 67_, 297–308.


Donald, S. G., G. W. Imbens, and W. K. Newey (2003). Empirical likelihood estimation
and consistent tests with conditional moment restrictions. _Journal of Econometrics 117_ (1),

55–93.


Duarte, M., L. Magnolfi, M. Sølvsten, and C. Sullivan (2021). Testing firm conduct. Work
ing paper.


Dub´e, J.-P. (2004). Multiple discreteness and product differentiation: Demand for carbonated soft drinks. _Marketing Science 23_, 66–81.


Dub´e, J.-P. (2019). Microeconometric models of consumer demand. In J.-P. Dub´e and
P. Rossi (Eds.), _Handbook of the Economics of Marketing, Volume 1_ . Elsevier.


Dub´e, J.-P., J. T. Fox, and C.-L. Su (2012). Improving the numerical performance of static
and dynamic aggregate discrete choice random coefficients demand estimation. _Econo-_
_metrica 80_ (5), 2231–2267.


Dub´e, J.-P., A. Hortac¸su, and J. Joo (2021). Random-coefficients logit demand estimation
with zero-valued market shares. _Marketing Science_ .


Dubin, J. A. and D. McFadden (1984). An econometric analysis of residential electric
appliance holdings and consumption. _Econometrica 52_ (2), 345–62.


87


Dubois, P., R. Griffith, and A. Nevo (2014). Do prices and attributes explain international
differences in food purchases? _American Economic Review 104_ (3), 832–67.


Dubois, P., R. Griffith, and M. O’Connell (2020). How well targeted are soda taxes? _Amer-_
_ican Economic Review 110_ (11), 3661–3704.


Epple, D. (1987). Hedonic prices and implicit markets: Estimating demand and supply
functions for differentiated products. _Journal of Political Economy 95_ (1), 59–80.


Erdem, T., M. P. Keane, T. S. Onc¨u, and J. Strebel (2005). [¨] Learning about computers:
An analysis of information search and technology choice. _Quantitative Marketing and_
_Economics 3_ (3), 207–247.


Fan, Y. (2013). Ownership consolidation and product characteristics: A study of the us
daily newspaper market. _American Economic Review 103_ (5), 1598–1628.


Fosgerau, M., J. Monardo, and A. De Palma (2020). The inverse product differentiation

logit model.


Fox, J. T. and A. Gandhi (2016). Nonparametric identification and estimation of random
coefficients in multinomial choice models. _The RAND Journal of Economics 47_ (1), 118–

139.


Fox, J. T., K. il Kim, and C. Yang (2016). A simple nonparametric approach to estimating the distribution of random coefficients in structural models. _Journal of Economet-_
_rics 195_ (2), 236–254.


Fox, J. T., K. i. Kim, S. P. Ryan, and P. Bajari (2011). A simple estimator for the distribution
of random coefficients. _Quantitative Economics 2_ (3), 381–418.


Freyberger, J. (2015). Asymptotic theory for differentiated products demand models with
many markets. _Journal of Econometrics 181_ (1), 162–181.


Gandhi, A. and J.-F. Houde (2020). Measuring substitution patterns in differentiated products industries. _Working Paper_ .


Gandhi, A., Z. Lu, and X. Shi (2021). Estimating demand for differentiated products with
zeroes in market share data. _working paper_ .


88


Gandhi, A., A. Nevo, and J. Tao (2021). Flexible estimation of differentiated product
demand models using aggregate data. _Working paper_ .


Gasmi, F., J. Laffont, and Q. Vuong (1992). Econometric analysis of collusive behavior in
a soft-drink market. _Journal of Economics & Management Strategy 1_ (2), 277–311.


Gentzkow, M. (2007). Valuing new goods in a model with complementarity: Online newspapers. _American Economic Review 97_ (3), 713–744.


Ghili, S. (Forthcoming). Network formation and bargaining in vertical markets: The case
of narrow networks in health insurance. _Marketing Science_ .


Gorman, W. (1956). A possible procedure for analysing quality differentials in the egg
market. _Reprinted in The Review of Economic Studies (1980)_ .


Gorman, W. (1980). A possible procedure for analysing quality differentials in the egg
market. _Review of Economic Studies 47_ (5), 843–856.


Gowrisankaran, G., A. Nevo, and R. Town (2015). Mergers when prices are negotiated:
Evidence from the hospital industry. _American Economic Review_, 172–203.


Gowrisankaran, G. and M. Rysman (2012). Dynamics of consumer demand for new
durable goods. _Journal of Political Economy 120_ (6), 1173–1219.


Grennan, M. (2013). Price discrimination and bargaining: Empirical evidence from medical devices. _American Economic Review 103_ (1), 145–77.


Grieco, P. L. E., C. Murry, J. Pinkse, and S. Sagl (2021). Efficient estimation of random

coefficients demand models using product and consumer datasets. Working Paper.


Griffith, R. and A. Nevo (2019). Marketing and public policy. In J.-P. Dub´e and P. Rossi
(Eds.), _Handbook of the Economics of Marketing, Volume 1_ . Elsevier.


Griliches, Z. (1961). Hedonic price indexes for automobiles: An econometric analysis of
quality change. In _The Price Statistics of the Federal Government_, pp. 173–196. Cambridge,

MA: National Bureau of Economic Research.


Hanemann, W. M. (1984). Discrete/continuous models of consumer demand. _Economet-_
_rica 52_ (3), 541–561.


89


Hausman, J. (1996). Valuation of new goods under perfect and imperfect competition. In
T. Bresnahan and R. Gordon (Eds.), _The Economics of New Goods_, Volume 58 of _Studies in_
_Income and Wealth Vol. 58_ . Chicago: National Bureau of Economic Research.


Hausman, J., G. Leonard, and J. D. Zona (1994). Competitive Analysis with Differentiated
Products. _Annales D’Economie et de Statistique 34_, 159–180.


Hendel, I. (1999). Estimating multiple-discrete choice models: An application to computerization returns. _The Review of Economic Studies 66_ (2), 423–446.


Hendel, I. and A. Nevo (2006a). Measuring the implications of sales and consumer inventory behavior. _Econometrica 74_, 1637–1674.


Hendel, I. and A. Nevo (2006b). Sales and consumer inventory. _The RAND Journal of_
_Economics 37_ (3), 543–561.


Hendel, I. and A. Nevo (2013). Intertemporal price discrimination in storable goods markets. _American Economic Review 103_ (7), 2722–51.


Ho, K. and R. S. Lee (2019). Equilibrium insurer-provider networks: Bargaining and
exclusion in health care markets. _American Economic Review 109_ (2), 473–522.


Hong, H., H. Li, and J. Li (2021). BLP estimation using laplace transformation and overlapping simulation draws. _Journal of Econometrics 222_ (1), 56–72.


Honka, E., A. Hortac¸su, and M. Wildenbeest (2019). Empirical search and consideration
sets. In J.-P. Dub´e and P. E. Rossi (Eds.), _Handbook of the Economics of Marketing, Volume_
_1_, Volume 1 of _Handbook of the Economics of Marketing_, pp. 193–257. North-Holland.


Horn, H. and A. Wolinsky (1988a). Bilateral monopolies and incentives for merger. _RAND_
_Journal of Economics 19_ (3), 408–419.


Horn, H. and A. Wolinsky (1988b). Worker substitutability and patterns of unionisation.
_The Economic Journal 98_ (391), 484–497.


Knittel, C. R. and K. Metaxoglou (2014). Estimation of random-coefficient demand models: Two empiricists’ perspective. _Review of Economics and Statistics 96_, 34–59.


Lancaster, K. (1966). A new approach to consumer theory. _Journal of Political Econ-_
_omy 74_ (2).


90


Lau, L. J. (1982). On identifying the degree of competitiveness from industry price and
output data. _Economics Letters 10_ (1-2), 93–99.


Lee, J. and K. Seo (2015). A computationally fast estimator for random coefficients logit
demand models using aggregate data. _The RAND Journal of Economics 46_ (1), 86–102.


Lee, R., A. Yurukoglu, and M. Whinston (2021). Volume 4 of _Handbook of Industrial Orga-_
_nization_ . Elsevier.


Lee, R. S. and K. Fong (2013). Markov-perfect network formation an applied framework
for bilateral oligopoly and bargaining in buyer-seller networks. _Working paper_ .


Liebman, E. (2018). Bargaining in markets with exclusion: An analysis of health insurance
networks. _Working Paper_ .


Magnac, T. and D. Thesmar (2002). Identifying dynamic discrete decision processes.
_Econometrica 70_ (2), 801–816.


Malone, J., A. Nevo, and J. Williams (2020). The tragedy of the last mile: Congestion
externalities in broadband networks. _Working Paper_ .


McFadden, D. (1978). Modeling the choice of residential location. _in A. Karlgvist, et al.,_
_eds., Spatial Interaction Theory and Planning Models_ .


McFadden, D. (1981). Econometric models of probabilistic choice. _Structural analysis of_
_discrete data with econometric applications 198272_ .


McFadden, D. and K. Train (2000). Mixed MNL models for discrete response. _Journal of_
_Applied Econometrics 15_ (5), 447–470.


Melnikov, O. (2013). Demand for differentiated durable products: The case of the u.s.
computer printer market. _Economic Inquiry 51_ (2), 1277–1298.


Miller, N. H. and M. C. Weinberg (2017). Understanding the price effects of the millercoors
joint venture. _Econometrica 85_ (6), 1763–1791.


Nevo, A. (1998). Identification of the oligopoly solution concept in a differentiatedproducts industry. _Economics Letters 59_ (3), 391 – 395.


Nevo, A. (2000a). Mergers with differentiated products: The case of the ready-to-eat
cereal industry. _RAND Journal of Economics 31_, 395–421.


91


Nevo, A. (2000b). A practitioner’s guide to estimation of random-coefficients logit models
of demand. _Journal of Economics and Management Strategy 9_ (4), 513–548.


Nevo, A. (2001). Measuring market power in the ready-to-eat cereal industry. _Economet-_
_rica 69_ (2), 307–342.


Nevo, A. (2003). New products, quality changes and welfare measures computed from
estimated demand systems. _The Review of Economics and Statistics 85_ (2), 266–275.


Nevo, A. (2011). Empirical models of consumer behavior. _Annual Reviews_ .


Nevo, A., D. L. Rubinfeld, and M. McCabe (2005). Academic journal pricing and the
demand of libraries. _American Economic Review 95_ (2), 447–452.


Nevo, A., J. Turner, and J. Williams (2016). Usage-based pricing and demand for residential broadband. _Econometrica 84_ (2), 411–443.


Pakes, A. (2017). Empirical tools and competition analysis: Past progress and current
problems. _International Journal of Industrial Organization 53_, 241–266.


Pakes, A., S. Berry, and J. A. Levinsohn (1993). Applications and limitations of some

recent advances in empirical industrial organization: Price indexes and the analysis of
environmental change. _American Economic Review 83_ (2), 240–246.


Pesendorfer, M. (2002). Retail sales: A study of pricing behavior in supermarkets. _The_
_Journal of Business 75_ (1), 33–66.


Peters, C. (2006). Evaluating the Performance of Merger Simulations: Evidence from the
U.S. Airline Industry. _Journal of Law and Economics 47_ (3), 627–649.


Petrin, A. (2002). Quantifying the benefits of new products: The case of the minivan.
_Journal of Political Economy_, 705–29.


Pinkse, J. and M. Slade (2004). Mergers, brand competition, and the price of a pint. _Euro-_
_pean Economic Review 48_ (3), 617–643.


Pinkse, J., M. E. Slade, and C. Brett (2002). Spatial price competition: A semiparametric
approach. _Econometrica 70_ (3), 1111–1153.


92


Prince, J. T. (2008). Repeat purchase amid rapid quality improvement: Structural estimation of demand for personal computers. _Journal of Economics & Management Strat-_
_egy 17_ (1), 1–33.


Reiss, P. C. and F. A. Wolak (2007). _Structural Econometric Modeling: Rationales and Examples_
_from Industrial Organization_, Volume 6A. Amsterdam: North-Holland.


Reynaert, M. and F. Verboven (2014). Improving the performance of random coefficients
demand models: the role of optimal instruments. _Journal of Econometrics 179_ (1), 83–98.


Rivers, D. and Q. Vuong (2002). Model selection tests for nonlinear dynamic models. _The_
_Econometrics Journal 5_ (1), 1–39.


Rosen, S. (1974). Hedonic prices and implicit markets: Product differentiation in pure
competition. _Journal of Political Economy_, 34–55.


Rosse, J. N. (1970). Estimating cost function parameters without using cost data: Illustrated methodology. _Econometrica_, 256–275.


Rubinstein, A. (1982). Perfect equilibrium in a bargaining model. _Econometrica_ (50), 97–

109.


Rust, J. (1987). Optimal replacement of gmc bus engines: An empirical model of harold
zurcher. _Econometrica 55_ (5), 999–1033.


Rust, J. (1994). Chapter 51 structural estimation of markov decision processes. Volume 4
of _Handbook of Econometrics_, pp. 3081 – 3143. Elsevier.


Salani´e, B. and F. A. Wolak (2019). Fast,” robust”, and approximately correct: estimating

mixed demand systems. Technical report, National Bureau of Economic Research.


Scherer, F. M. (1982). The breakfast cereal industry. In W. Adams (Ed.), _The Structure of_
_American Industry_ . New York: Macmillan.


Schultz, H. (1938). _The Theory and Measurement of Demand_ . Chicago: The University of

Chicago Press.


Shaked, A. and J. Sutton (1983). Natural oligopolies. _Econometrica 51_ (5), 1469–1483.


Small, K. A. and H. S. Rosen (1981). Applied welfare analysis with discrete choice models.
_Econometrica 49_, 105–30.


93


Smith, H. (2004). Supermarket choice and supermarket competition in market equilibrium. _Review of Economic Studies 71_ (1), 235–263.


Smith, R. J. (1992). Non-nested tests for competing models estimated by generalized
method of moments. _Econometrica 60_ (4), 973–980.


Spence, M. (1976). Product selection, fixed costs, and monopolistic competition. _Review of_
_Economic Studies 43_, 217–235.


Stigler, G. (1954). The early studies of empirical studies of consumer behavior. _The Journal_
_of Political Economy 62_, 95–113.


Stone, J. (1954). _The Measurement of Consumer Expenditure and Behavior in the United King-_
_dom, 1920-1938, Vol 1_ . Cambridge University Press.


Sweeting, A. (2013). Dynamic product positioning in differentiated product industries:

The effect of fees for musical performance rights on the commercial radio industry.
_Econometrica 81_ (5), 1763–1803.


Theil, H. (1965). The information approach to demand analysis. _Econometrica 6_, 375–80.


Thomassen, Ø., H. Smith, S. Seiler, and P. Schiraldi (2017). Multi-category competition
and market power: A model of supermarket pricing. _American Economic Review 107_ (8),

2308–51.


Town, R. and S. Liu (2003). The welfare impact of medicare hmos. _The RAND Journal of_
_Economics 34_ (4), 719–736.


Town, R. and G. Vistnes (2001). Hospital competition in HMO networks. _Journal of Health_
_Economics 20_ (5), 733–752.


Trajtenberg, M. (1989). The welfare analysis of product innovations, with an application
to computed tomography scanners. _Journal of Political Economy 97_, 444–79.


Villas-Boas, S. (2007). Vertical relationships between manufacturers and retailers: Inference with limited data. _Review of Economic Studies 74_, 625–652.


Vuong, Q. H. (1989). Likelihood ratio tests for model selection and non-nested hypotheses. _Econometrica 57_, 307–33.


94


Waldfogel, J. (2003). Preference externalities: An empirical study of who benefits whom
in differentiated-product markets. _RAND Journal of Economics 34_ (3), 557–68.


Wang, E. Y. (2015). The impact of soda taxes on consumer welfare: implications of storability and taste heterogeneity. _The RAND Journal of Economics 46_ (2), 409–441.


Werden, G. J. and L. M. Froeb (1994). The effects of mergers in differentiated products
industries: Logit demand and merger policy. _Journal of Law, Economics, & Organiza-_
_tion 10_ (2), 407–426.


Wollmann, T. G. (2018). Trucks without bailouts: Equilibrium product characteristics for
commercial vehicles. _American Economic Review 108_ (6), 1364–1406.


95


