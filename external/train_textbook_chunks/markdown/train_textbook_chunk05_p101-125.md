_4.2. NESTED LOGIT_ 91


has cumulative distribution:




- _K_


_k_ =1



 _λk_ []





 [�] _e_ _[−][ε][nj]_ _[/λ][k]_

_j∈Bk_




 _._ (4.1)



_exp_







 _−_







This distribution is a type of generalized extreme value (GEV) distribution. It is a generalization of the distribution that gives rise to
the logit model. For logit, each _εnj_ is independent with a univariate
extreme value distribution. For this GEV, the marginal distribution
of each _εnj_ is univariate extreme value. However, the _εnj_ ’s are correlated within nests. For any two alternatives _j_ and _m_ in nest _Bk_, _εnj_
is correlated with _εnm_ . For any two alternatives in different nests, the
unobserved portion of utility is still uncorrelated: _Cov_ ( _εnj, εnm_ ) = 0
for any _j ∈_ _Bk_ and _m ∈_ _Bℓ_ with _ℓ_ = _k_ .
The parameter _λk_ is a measure of the degree of independence in
unobserved utility among the alternatives in nest _k_ . A higher value
of _λk_ means greater independence and less correlation. The statistic
(1 _−_ _λk_ ) is a measure of correlation, in the sense that as _λk_ rises,
indicating less correlation, this statistic drops. As McFadden (1978)
points out, the correlation is actually more complex than (1 _−_ _λk_ ),
but (1 _−_ _λk_ ) can be used as an indication of correlation. A value
of _λk_ = 1 indicates complete independence within nest _k_, that is,
no correlation. When _λk_ = 1 for all _k_, representing independence
among all the alternatives in all nests, the GEV distribution becomes
the product of independent extreme value terms, whose distribution
is given in (3.2). In this case, the nested logit model reduces to the
standard logit model.
As shown by the authors cited above, this distribution for the unobserved components of utility gives rise to the following choice probability for alternative _i ∈_ _Bk_ :


��          - _λk−_ 1
_e_ _[V][ni][/λ][k]_ _j∈Bk_ _[e][V][nj]_ _[/λ][k]_
_Pni_ = ~~�~~ _K_ ~~��~~ ~~�~~ _λℓ_ _._ (4.2)

_ℓ_ =1 _j∈Bℓ_ _[e][V][nj]_ _[/λ][ℓ]_


We can use this formula to show that IIA holds within each subset
of alternatives but not across subsets. Consider alternatives _i ∈_ _Bk_ and
_m ∈_ _Bℓ_ . Since the denominator of (4.2) is the same for all alternatives,


92 _CHAPTER 4. GEV_


the ratio of probabilities is the ratio of numerators:

��          - _λk−_ 1
_Pni_ _e_ _[V][ni][/λ][k]_ _j∈Bk_ _[e][V][nj]_ _[/λ][k]_
_Pnm_ = _e_ _[V][nm][/λ][ℓ]_ ~~��~~ _j∈Bℓ_ _[e][V][nj]_ _[/λ][ℓ]_ ~~�~~ _λℓ−_ 1 _[.]_


If _k_ = _ℓ_ (i.e., _i_ and _m_ are in the same nest) then the terms in parentheses cancel out and we have


_Pni_
= _[e][V][ni][/λ][k]_
_Pnm_ _e_ _[V][nm][/λ][ℓ]_


This ratio is independent of all other alternatives. For _k ̸_ = _ℓ_ (i.e., _i_ and
_m_ are in different nests), the terms in parentheses do not cancel out.
The ratio of probabilities depends on the attributes of all alternatives
in the nests that contain _i_ and _m_ . Note, however, that the ratio does
not depend on the attributes of alternatives in nests other those containing _i_ and _m_ . A form of IIA holds, therefore, even for alternatives
in different nests. This form of IIA can be loosely described as “independence from irrelevant nests” or IIN. With a nested logit model, IIA
holds over alternatives in each nest and IIN holds over alternatives in
different nests. This property of nested logit models is reinforced in
the next section when we decompose the nested logit probability into
two standard logit probabilities.
When _λk_ = 1 for all _k_ (and hence 1 _−_ _λk_ = 0), indicating no correlation among the unobserved components of utility for alternatives
within a nest, the choice probabilities become simply logit. The nested
logit model is a generalization of logit that allows for a particular pattern of correlation in unobserved utility.
The parameter _λk_ can differ over nests, reflecting different correlation among unobserved factors within each nest. The researcher can
constrain the _λk_ ’s to be the same for all (or some) nests, indicating
that the correlation is the same in each of these nests. Hypothesis
testing can be used to determine whether constraints on the _λk_ ’s are
reasonable. Testing the constraint _λk_ = 1 _∀_ _k_ is equivalent to testing
whether the standard logit model is a reasonable specification against
the more general nested logit. These tests are performed most readily
with the likelihood ratio statistic described in section (3.8.2).
The value of _λk_ must be within a particular range for the model
to be consistent with utility maximizing behavior. If _λk ∀_ _k_ is between
zero and one, the model is consistent with utility maximization for


_4.2. NESTED LOGIT_ 93


all possible values of the explanatory variables. For _λk_ greater than
one, the model is consistent with utility maximizing behavior for some
range of the explanatory variables but not for all values. Kling and
Herriges (1995) and Herriges and Kling (1996) provide tests of consistency of nested logit with utility maximization when _λk >_ 1, and Train,
McFadden and Ben-Akiva (1987) and Lee (1999) provide examples of
models for which _λk >_ 1. A value of _λk_ below zero is inconsistent
with utility maximization and implies that improving the attributes of
an alternative (such as lowering its price) can decrease the probability of the alternative being chosen. With positive _λk_, the nested logit
approaches the “elimination by aspects” model of Tversky (1972) as
_λk →_ 0.
In the notation that we have been using, each _λk_ is a fixed parameter, which implies that all decision-makers have the same correlations
among unobserved factors. In reality, correlations might differ over
decision-makers based on their observed characteristics. To accommodate this possibility, each _λk_ can be specified to be a parametric
function of observed demographics or other variables, as long as the
function maintains a positive value. For example, Bhat (1997) specifies
_λ_ = _exp_ ( _αzn_ ), where _zn_ is a vector of characteristics of decision-maker
_n_ and _α_ is a vector of parameters to be estimated along with the parameters that enter representative utility. The exponential transformation
assures that _λ_ is positive.


**4.2.3** **Decomposition into two logits**


Expression (4.2) is not very illuminating as a formula. However, the
choice probabilities can be expressed in an alternative fashion that is
quite simple and readily interpretable. Without loss of generality, the
observed component of utility can be decomposed into two parts: (1) a
part labeled _W_ that is constant for all alternatives within a nest, and
(2) a part labeled _Y_ that varies over alternatives within a nest. Utility
is written as:


_Unj_ = _Wnk_ + _Ynj_ + _εnj_ (4.3)


for _j ∈_ _Bk_, where:


_Wnk_ depends only on variables that describe nest _k_ . These variables
differ over nests but not over alternatives within each nest.


94 _CHAPTER 4. GEV_


_Ynj_ depends on variables that describe alternative _j_ . These variables
vary over alternatives within nest _k_ .


Note that this decomposition is fully general since for any _Wnk_, _Ynj_ is
defined as _Vnj −_ _Wnk_ .
With this decomposition of utility, the nested logit probability can
be written as the product of two standard logit probabilities. Let the
probability of choosing alternative _i ∈_ _Bk_ be expressed as the product
of two probabilities, namely: the probability that an alternative within
nest _Bk_ is chosen and the probability that the alternative _i_ is chosen
given that an alternative in _Bk_ is chosen. This is denoted as


_Pni_ = _Pni|Bk_ _PnBk_ _,_


where _Pni|Bk_ is the conditional probability of choosing alternative _i_
given that an alternative in nest _Bk_ is chosen, and _PnBk_ is the marginal
probability of choosing an alternative in nest _Bk_ (with the marginality
being over all alternatives in _Bk_ .) This equality is exact since any probability can be written as the product of a marginal and a conditional
probability.
The reason for decomposing _Pni_ into a marginal and a conditional
probability is that, with the nested logit formula for _Pni_, the marginal
and conditional probabilities take the form of logits. In particular, the
marginal and conditional probabilities can be expressed as


_e_ _[W][nk]_ [+] _[λ][k][I][nk]_
_PnBk_ = ~~�~~ _K_ (4.4)
_ℓ_ =1 _[e][W][nℓ]_ [+] _[λ][ℓ][I][nℓ]_

_e_ _[Y][ni][/λ][k]_
_Pni|Bk_ = ~~�~~ (4.5)
_j∈Bk_ _[e][Y][nj]_ _[/λ][k]_


where

      _Ink_ = _ln_ _e_ _[Y][nj]_ _[/λ][k]_

_j∈Bk_


The derivation of these expressions from the choice probability (4.2)
simply involves algebraic rearrangement. For interested readers, it is
given in section (4.2.5).
Stated in words, the probability of choosing an alternative in _Bk_
takes the form of the logit formula, as if it were a model for a choice
among nests. This probability includes variables _Wnk_ that vary over
nests but not over alternatives within each nest. It also includes a


_4.2. NESTED LOGIT_ 95


term labeled _Ink_ whose meaning we elucidate below. The conditional
probability of choosing _i_ given that an alternative in _Bk_ is chosen
is also a logit formula, as if it were a model for the choice among the
alternatives within the nest. This conditional probability includes variables _Ynj_ that vary over alternatives within the nest. Note that these
terms are divided by _λk_ such that, when _Ynj_ is linear in parameters,
the coefficients that enter this conditional probability are the original
coefficients divided by _λk_ . It is customary to refer to the marginal
probability (choice of nest) as the “upper model” and the conditional
probability (choice of alternative within the nest) as the “lower model,”
reflecting their relative positions in Figure 4.1.

The term _Ink_ links the upper and lower models by bringing information from the lower model into the upper model. Ben-Akiva (1972)
first identified the correct formula for this link. In particular, _Ink_ is
the log of the denominator of the lower model. This formula has an
important meaning. Recall from the discussion of consumer surplus for
a logit model (section 3.5) that the log of the denominator of the logit
model is the expected utility that the decision-maker obtains from the
choice situation, as shown by Williams (1977) and Small and Rosen
(1981). The same interpretation applies here: _λkInk_ is the expected
utility that decision-maker _n_ receives from the choice among the alternatives in nest _Bk_ . The formula for expected utility is the same here
as for a logit model because, conditional on the nest, the choice of alternatives within the nest is indeed a logit, as given by equation (4.5).
_Ink_ is often called the ”inclusive value” or ”inclusive utility” of nest
_Bk_ . It is also called the ”log-sum term” because it is the log of a sum
(of exponentiated representative utilities). The term ”inclusive price”
is sometimes used; however the negative of _Ink_ more closely resembles
a price.

The coefficient of _Ink_ in the upper model is _λk_, which is often called
the log-sum coefficient. As discussed above, _λk_ reflects the degree of
independence among the unobserved portions of utility for alternatives in nest _Bk_, with a lower _λk_ indicating less indendendent (more
correlation.)

It is appropriate that the inclusive value term enters as an explanatory variable in the upper model. Stated loosely, the probability
of choosing nest _Bk_ depends on the expected utility that the person
receives from that nest. This expected utility includes the utility that
he receives no matter which alternative he chooses in the nest, which


96 _CHAPTER 4. GEV_


is _Wnk_, plus the expected extra utility that he receives by being able
to choose the best alternative in the nest, which is _λkInk_ .
Recall that the coefficients that enter the lower model are divided
by _λk_, as given in equation 4.5. Models have been specified and estimated without dividing by _λk_ in the lower model. Daly (1987) and
Greene (2000) describes such a model, and the computer software
STATA includes it as their nested logit model in the nlogit command.
The package NLOGIT allows either specification. If the coefficients in
the lower model are not divided by _λk_, the choice probabilities are not
the same as those given in equation 4.2. As shown in the derivation
in section 4.2.5, the division by _λk_ is needed for the product of the
conditional and marginal probabilities to equal the nested logit probabilities given by equation 4.2. However, the fact that the model does
not give the probabilities in equation 4.2 does not necessarily mean that
the model is inappropriate. Koppelman and Wen (1998) and Hensher
and Greene (forthcoming) compare the two approaches (dividing by
_λk_ versus not) and show that the latter model is not consistent with
utility maximization when any coefficients are common across nests
(such as a cost coefficient that is the same for bus and car modes.)
Heiss (2002) points out the converse: if no coefficients are common
over nests, then the latter model is consistent with utility maximization, since the necessary division by _λk_ in each nest is accomplished
implicitly (rather than explicitly) by allowing separate coefficients in
each nests such that the scale of coefficients differs over nests. When
coefficients are common over nests, she found that not dividing by _λk_
provides counter-intuitive implications.


**4.2.4** **Estimation**


The parameters of a nested model can be estimated by standard maximum likelihood techniques. Substituting the choice probabilities of
expression (4.2) into the log likelihood function gives an explicit function of the parameters of this model. The value of the parameters that
maximizes this function is, under fairly general conditions, consistent
and efficient (Brownstone and Small, 1989).
Computer routines are available in commercial software packages
for estimating nested models by maximum likelihood. Hensher and
Greene (forthcoming) provide a guide for nested logits using available
software. Numerical maximization is sometimes difficult since the log

_4.2. NESTED LOGIT_ 97


likelihood function is not globally concave and even in concave areas is
not close to a quadratic. The researcher might need to help the routines
by trying different algorithms and/or starting values, as discussed in
Chapter 8.

Instead of performing maximum likelihood, nested logit models can
be estimated consistently (but not efficiently) in a sequential fashion,
exploiting the fact that the choice probabilities can be decomposed
into marginal and conditional probabilities that are logit. This sequential estimation is performed ”bottom up.” The lower models (for
the choice of alternative within a nest) are estimated first. Using the
estimated coefficients, the inclusive value term is calculated for each
lower model. Then the upper model (for choice of nest) is estimated,
with the inclusive value terms entering as explanatory variables.

Sequential estimation creates two difficulties that argue against its
use. First, the standard errors of the upper-model parameters are
biased downward, as Amemiya (1978) first pointed out. This bias
arises because the variance of the inclusive value estimate that enters
the upper model is not incorporated into the calculation of standard
errors. With downwardly biased standard errors, smaller confidence
bounds and larger t-statistics are estimated for the parameters than
are true, and the upper model will appear to be better than it actually
is. Ben-Akiva and Lerman (1985, p. 298) give a procedure for adjusting
the standard errors to eliminate the bias.

Second, it is usually the case that some parameters appear in several submodels. Estimating the various upper and lower models separately provides separate estimations of whatever common parameters
appear in the model. Simultaneous estimation by maximum likelihood
assures that the common parameters are constrained to be the same
wherever they appear in the model.

These two complications are symptoms of a more general circumstance, namely, that sequential estimation of nested logit models, while
consistent, is not as efficient as simultaneous estimation by maximum
likelihood. With simultaneous estimation, all information is utilized
in the estimation of each parameter, and parameters that are common across components are necessarily constrained to be equal. Since
commercial software is available for simultaneous estimation, there is
little reason to estimate a nested logit sequentially. If problems arise
in simultaneous estimation, then the researcher might find it useful to
estimate the model sequentially and then use the sequential estimates


98 _CHAPTER 4. GEV_


as starting values in the simultaneous estimation. The main value of
the decomposition of the nested logit into its upper and lower components comes not in its use as a estimation tool but rather as a heuristic
device: the decomposition helps greatly in understanding the meaning
and structure of the nested logit model.


**4.2.5** **Equivalence of nested logit formulas**


We asserted in section (4.2.3) that the product of the marginal and
conditional probabilities in (4.4) and (4.5) equals the joint probability
in (4.2). We now verify this assertion.



��      - _λk−_ 1
_e_ _[V][ni][/λ][k]_ _j∈Bk_ _[e][V][nj]_ _[/λ][k]_
_Pni_ = ~~�~~




~~�~~ _K_ ~~��~~ ~~�~~ _λℓ_ by eq (4.2)
_ℓ_ =1 _j∈Bℓ_ _[e][V][nj]_ _[/λ][ℓ]_



_e_ _[V][ni][/λ][k]_
= ~~�~~
_j∈Bk_ _[e][V][nj]_ _[/λ][k]_




~~�~~ _K_ ~~��~~ ~~�~~ _λℓ_
_ℓ_ =1 _j∈Bℓ_ _[e][V][nj]_ _[/λ][ℓ]_



�� - _λk_
_j∈Bk_ _[e][V][nj]_ _[/λ][k]_



_e_ [(] _[W][nk]_ [+] _[Y][ni]_ [)] _[/λ][k]_
= ~~�~~
_j∈Bk_ _[e]_ [(] _[W][nk]_ [+] _[Y][nj]_ [)] _[/λ][k]_




~~�~~ _K_ ~~��~~ ~~�~~ _λℓ_ [using (4.3)]
_ℓ_ =1 _j∈Bℓ_ _[e]_ [(] _[W][nℓ]_ [+] _[Y][nj]_ [)] _[/λ][ℓ]_



�� - _λk_
_j∈Bk_ _[e]_ [(] _[W][nk]_ [+] _[Y][nj]_ [)] _[/λ][k]_



_e_ _[W][nk][/λ][k]_ _e_ _[Y][ni][/λ][k]_
=

_e_ _[W][nk][/λ][k]_ ~~[ �]~~ _j∈Bk_ _[e][Y][nj]_ _[/λ][k]_




~~�~~ _K_ ~~��~~ ~~�~~ _λℓ_
_ℓ_ =1 _[e][W][nℓ]_ _j∈Bℓ_ _[e][Y][nj]_ _[/λ][ℓ]_



��  - _λk_
_e_ _[W][nk]_ _j∈Bk_ _[e][Y][nj]_ _[/λ][k]_



_e_ _[Y][ni][/λ][k]_ _e_ _[W][nk]_ [+] _[λ][k][I][nk]_
= ~~�~~ ~~�~~ _K_
_j∈Bk_ _[e][Y][nj]_ _[/λ][k]_ _ℓ_ =1 _[e][W][nℓ]_ [+] _[λ][ℓ][I][nℓ]_

= _Pni|Bk_ _PnBk_ _._

where the next to last equality is because _Ink_ = _ln_ [�] _j∈Bk_ _[e][Y][nj]_ _[/λ][k]_ [,]
recognizing that _e_ _[x]_ _b_ _[c]_ = _e_ _[x]_ [+] _[cln]_ [(] _[b]_ [)] .

### **4.3 Three-Level Nested Logit**


The nested logit model that we have discussed up this this point is
called a two-level nested logit model because there are two levels of
modeling: the marginal probabilities (upper model) and the conditional probabilities (lower models.) In the case of the mode choice,


_4.3. THREE-LEVEL NESTED LOGIT_ 99


the two levels are the marginal model of auto versus transit and the
conditional models of type of auto or transit (auto alone or carpool
given auto, and bus or rail given transit).

In some situations, three- or higher level nested logit models are
appropriate. Three-level models are obtained by partitioning the set of
alternatives into nests and then partitioning each nest into subnests.
The probability formula is a generalization of (4.2) with extra sums
for the subnests within the sums for nests. See McFadden (1978) or
Ben-Akiva and Lerman (1985) for the formula.

As with a two-level nested logit, the choice probabilities for a threelevel model can be expressed as a series of logits. The top model
describes the choice of nest; the middle models describe the choice of
subnest within each nest; and the bottom models describe the choice of
alternative within each subnest. The top model includes an inclusive
value term for each nest. This term represents the expected utility
that the decision-maker can obtain from the subnests within the nest.
It is calculated as the log of the denominator of the middle model
for that nest. Similarly, the middle models include an inclusive value
term for each subnest that represents the expected utility that the
decision-maker can obtain from the alternatives within the subnest. It
is calculated as the log of the denominator of the bottom model for
the subnest.

As an example, consider a household’s choice of housing unit within
a metropolitan area. The household has a choice among all the available housing units in the city. The housing units are available in different neighborhoods in the city and with different numbers of bedrooms.
It is reasonable to assume that there are unobserved factors that are
common to all units in the same neighborhood, such as the proximity to shopping and entertainment. The unobserved portion of utility
is therefore expected to be correlated over all units in a given neighborhood. There are also unobserved factors that are common to all
units with the same number of bedrooms, such as the convenience of
working at home. We therefore expect the unobserved utility to be
even more highly correlated among units of the same size in the same
neighborhood than between units of different size in the same neighborhood. This pattern of correlation can be represented by nesting
the units by neighborhood and then subnesting them by number of
bedrooms. A tree diagram depicting this situation is given in Figure
4.2 for San Francisco. There are three levels of submodels: the proba

100 _CHAPTER 4. GEV_


bility for choice of neighborhood, the probability for choice of number
of bedrooms given the neighborhood, and the choice of unit given the
neighborhood and number of bedrooms.



![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/train_textbook_chunks/markdown/train_textbook_chunk05_p101-125_images/train_textbook_chunk05_p101-125.pdf-9-0.png)



Neighborhood


Number of
bedrooms


Housing unit



Figure 4.2: Three-level nested logit.





A nested logit model with this nesting structure embodies IIA in
the following ways. (1) The ratio of probabilities of two housing units
in the same neighborhood and with the same number of bedrooms is
independent of the characteristics of all other units. For example, lowering the price of a two-bedroom apartment in Pacific Heights draws
proportionately from all one-bedroom units on Russian Hill. (2) The
ratio of probabilities of two housing units in the same neighborhood
but with different numbers of bedrooms is independent of the characteristics of units in other neighborhoods but depends on the characteristics of units in the same neighborhood that have the same number
of bedrooms as either of these units. Lowering the price of a twobedroom apartment in Pacific Heights draws proportionately from oneand two-bedroom units on Russian Hill, but draws disproportionately
from two-bedroom units in Pacific Heights relative to one-bedroom
units in Pacific Heights. (3) The ratio of probabilities of two housing
units in different neighborhoods depends on the characteristics of all
the other housing units in those neighborhoods but not on the characteristics of units in other neighborhoods. Lowering the price of a
two-bedroom apartment in Pacific Heights draws proportionately from
all units outside of Pacific Heights but draws disproportionately from


_4.4. OVERLAPPING NESTS_ 101


units in Pacific Heights relative to units outside of Pacific Heights.
Each layer of a nesting in a nested logit introduces parameters that
represent the degree of correlation among alternatives within the nests.
With the full set of alternatives partitioned into nests, the parameter
_λk_ is introduced for nest _k_, as described for two-level models. If the
nests are further partitioned into subnests, then a parameter _σmk_ is
introduced for subnest _m_ of nest _k_ . Using the decomposition of the
probability into a series of logit models, _σmk_ is the coefficient of the
inclusive value term in the middle model, and _λkσmk_ is the coefficient of
the inclusive value term in the top model. Just as for a two-level nested
logit, the value of these parameters must be in certain ranges to be
consistent with utility maximization. If 0 _< λk <_ 1 and 0 _< σmk <_ 1,
then the model is consistent with utility maximization for all levels
of the explanatory variables. A negative value for either parameter is
inconsistent with utility maximization. And values greater than one
are consistent for a range of explanatory variables.

### **4.4 Overlapping Nests**


For the nested logit models that we have considered, each alternative
is a member of only one nest (and, for three-level models, only one subnest.) This aspect of nested logit models is a restriction that is sometimes inappropriate. For example, in our example of mode choice, we
put carpool and auto alone into a nest because they have some similar
unobserved attributes. However, carpooling also has some unobserved
attributes that are similar to bus and rail, such as a lack of flexibility in
scheduling (the worker cannot go to work whenever he wants each day
but rather has to go at the time that the carpool has decided, similar
to taking a bus or rail line with fixed departure times.) It would be
useful to have a model in which the unobserved utility for the carpool
alternative could be correlated with that of auto alone and also correlated, though to a different degree, with that of bus and rail. Stated
equivalently, it would be useful for the carpool alternative to be in two
nests: one with auto alone and another with bus and rail.
Several kinds of GEV models have been specified with overlapping
nests, such that an alternative can be a member of more than one nest.
Vovsha (1997), Bierlaire (1998), and Ben-Akiva and Bierlaire (1999)
have proposed various models called cross-nested logits (CNL) that
contain multiple overlapping nests. Small (1987) considered a situa

102 _CHAPTER 4. GEV_


tion where the alternatives have a natural order, such as the number
of cars that a household owns (0, 1, 2, 3, and so on) or the destination
for shopping trips, with the shopping areas ordered by distance from
the household’s home. He specified a model called ordered generalized
extreme value (OGEV) in which the correlation in unobserved utility
between any two alternatives depends on their proximity in the ordering. This model has overlapping nests like the cross-nested logits,
but each nest consists of two alternatives and a pattern is imposed
on the correlations (higher correlation for closer pairs). Small (1994)
and Bhat (1998 _b_ ) described a nested version of the OGEV, which is
similar to a nested logit except that the lower models (for the alternatives given the nests) are OGEV rather than standard logit. Chu
(1981, 1989) proposed a model called the paired combinatorial logit
(PCL) in which each pair of alternatives constitutes a nest with its
own correlation. With _J_ alternatives, each alternative is a member of
_J −_ 1 nests and the correlation of its unobserved utility with each other
alternative is estimated. Wen and Koppelman (2001) have developed
a “generalized nested logit” (GNL) model that includes the PCL and
other cross-nested models as special cases. I describe below the PCL
and GNL, the former because of its simplicity and the later because of
its generality.


**4.4.1** **Paired combinatorial logit**


Each pair of alternatives is considered to be a nest. Since each alternative is paired with each of the other alternative, each alternative is
member of _J −_ 1 nests. A parameter labeled _λij_ indicates the degree
of independence between alternatives _i_ and _j_ . Stated equivalently:
(1 _−_ _λij_ ) is a measure of the correlation between the unobserved utility
of alternative _i_ and that of alternative _j_ . This parameter is analogous
to the _λk_ in a nested logit model, where _λk_ indicates the degree of
independence of alternatives within the nest and 1 _−_ _λk_ is a measure of
correlation within the nest. And as with nested logit, the PCL model
becomes a standard logit when _λij_ = 1 for all pairs of alternatives.
The choice probabilities for the PCL model are



_Pni_ =




- - - _λij_ _−_ 1
_j_ = _i_ _[e][V][ni][/λ][ij]_ _e_ _[V][ni][/λ][ij]_ + _e_ _[V][nj]_ _[/λ][ij]_

~~�~~ _Jk_ =1 _−_ 1 ~~�~~ _Jℓ_ = _k_ +1 ~~�~~ _eVnk/λkℓ_ + _eVnℓ/λkℓ_ ~~�~~ _λkℓ_ (4.6)



The sum in the numerator is over all _J −_ 1 nests that alternative _i_


_4.4. OVERLAPPING NESTS_ 103


is in. For each of these nests, the term being added is the same as
the numerator of the nested logit probability (4.2). In this sense, the
PCL is like the nested logit except that it allows _i_ to be in more
than one nest. The denominator in the PCL also take the same form
as in a nested logit: it is the sum over all nests of the sum of the
_exp_ ( _V/λ_ )’s within the nest, raised to the appropriate power _λ_ . If _λij_
is between zero and one for all _ij_ pairs, then the model is consistent
with utility maximization for all levels of the data. It is easy to verify
that _Pni_ becomes the standard logit formula when _λij_ = 1 _∀_ _i, j_ . In
their application, Koppelman and Wen (2000) found PCL to perform
better than nested logit or standard logit.


The researcher can test the hypothesis that _λij_ = 1 for some or all
of the pairs, using the likelihood ratio test of section (3.8.2). Acceptance of the hypothesis for a pair of alternatives implies that there is
no significant correlation in the unobserved utility for that pair. The
researcher can also place structure on the pattern of correlation. For
example, correlations can be assumed to be the same among a group
of alternatives; this assumption is imposed by setting _λij_ = _λkℓ_ for all
_i_, _j_, _k_, and _ℓ_ in the group. Small’s OGEV model is a PCL model in
which _λij_ is specified to be a function of the proximity between _i_ and
_j_ . With a large number of alternatives, the researcher will probably
need to impose some form of structure on the _λij_ ’s, simply to avoid
the proliferation of parameters that arises with large _J_ . This proliferation of parameters, one for each pair of alternatives, is what makes
the PCL so flexible. The researcher’s goal is to apply this flexibility
meaningfully for his particular situation.


As discussed near the end of section (2.5), since the scale and level
of utility is immaterial, at most _J_ ( _J −_ 1) _/_ 2 _−_ 1 covariance parameters
can be estimated in a discrete choice model. A PCL model contains
_J_ ( _J −_ 1) _/_ 2 _λ_ ’s: one for each alternative paired with each other alternative, recognizing that _i_ paired with _j_ is the same as _j_ paired with _i_ .
The number of _λ_ _[′]_ _s_ exceeds the number of identifiable covariance parameters by exactly one. The researcher must therefore place at least
one constraint on the _λ_ ’s. This can be accomplished by normalizing
one of the _λ_ to 1. If structure is placed on the pattern of correlation,
as described in the previous paragraph, then this structure will usually
impose the normalization automatically.


104 _CHAPTER 4. GEV_


**4.4.2** **Generalized nested logit**


Nests of alternatives are labeled _B_ 1 _, B_ 2 _, . . ., BK_ . Each alternative can
be a member of more than one nest. Importantly, an alternative can
be in a nest to varying degrees. Stated differently, an alternative is
allocated among the nests, with the alternative being in some nests
more than other nests. An “allocation” parameter _αjk_ reflects the
extent to which alternative _j_ is a member of nest _k_ . This parameter
must be non-negative: _αjk ≥_ 0 _∀j, k_ . A value of zero means that
the alternative is not in the nest at all. Interpretation is facilitated
by having the allocation parameters sum to one over nests for any
alternative: [�] _k_ _[α][jk]_ [= 1] _[ ∀][j]_ [.] Under this condition, _αjk_ reflects the
portion of the alternative that is allocated to each nest.
A parameter _λk_ is defined for each nest and serves the same function
as in nested logit models, namely to indicate the degree of independence among alternatives within the nest: higher _λk_ translates into
greater independence and less correlation.
The probability that person _n_ chooses alternative _i_ is



_Pni_ =




- �� - _λk−_ 1
_k_ [(] _[α][ik][e][V][ni]_ [)][1] _[/λ][k]_ _j∈Bk_ [(] _[α][jk][e][V][nj]_ [)][1] _[/λ][k]_

~~�~~ _K_ ~~��~~ ~~�~~ _λℓ_ _._ (4.7)
_ℓ_ =1 _j∈Bℓ_ [(] _[α][jℓ][e][V][nj]_ [)][1] _[/λ][ℓ]_



This formula is similar to the nested logit probability given in equation
4.2, except that the numerator is a sum over all the nests that contains
alternative _i_, with weights applied to these nests. If each alternative
enters only one nest, with _αjk_ = 1 for _j ∈_ _Bk_ and zero otherwise, the
model becomes a nested logit model. And if, in addition, _λk_ = 1 for all
nests, then the model becomes standard logit. Wen and Koppelman
(2001) derive various cross-nested models as special cases of the GNL.
To facilitate interpretation, the GNL probability can be decomposed as:




 _Pni_ =



_Pni|Bk_ _Pnk,_
_k_



where the probability of nest _k_ is



_Pnk_ =




  _j_ [(] _[α][jk][e][V][nj]_ [)][1] _[/λ][k]_

~~�~~ _K_ ~~��~~ ~~�~~ _λℓ_
_ℓ_ =1 _j∈Bℓ_ [(] _[α][jℓ][e][V][nj]_ [)][1] _[/λ][ℓ]_


_4.5. HETEROSKEDASTIC LOGIT_ 105


and the probability of alternative _i_ given nest _k_ is


( _αike_ _[V][ni]_ ) [1] _[/λ][k]_
_Pni|Bk_ = ~~�~~ _[.]_
_j_ [(] _[α][jk][e][V][nj]_ [)][1] _[/λ][k]_

### **4.5 Heteroskedastic Logit**



Instead of capturing correlations among alternatives, the researcher
may simply want to allow the variance of unobserved factors to differ
over alternatives. Steckel and Vanhonacker (1988), Bhat (1995), and
Recker (1995) describe a type of GEV model, called “heteroskedastic
extreme value” (HEV), that is the same as logit except with different
variance for each alternative. Utility is specified as _Unj_ = _Vnj_ + _εnj_
where _εnj_ is distributed independently extreme value with variance
( _θjπ_ ) [2] _/_ 6. There is no correlation in unobserved factors over alternatives; however, the variance of the unobserved factors is different for
different alternatives. To set the overall scale of utility, the variance
for one alternative is normalized to _π_ [2] _/_ 6, which is the variance of the
standardized extreme value distribution. The variances for the other
alternatives are then estimated relative to the normalized variance.

The choice probabilities for this heteroskedastic logit are ((Bhat,
1995)):





[�] _e_ _[−][e][−]_ [(] _[Vni][−][Vnj]_ [+] _[θiw]_ [)] _[/θj]_ 

_j_ = _i_




   - []
_Pni_ = 



 [�]



 _e_ _[−][e][−][w]_ _e_ _[−][w]_ _dw_



where _w_ = _εni/θi_ . The integral does not take a closed form; however, it
can be approximated by simulation. Note that _exp_ ( _−exp_ ( _−w_ )) _exp_ ( _−w_ )
is the extreme value density, given in section 3.1. _Pni_ is therefore
the integral of the term in square brackets over the extreme value
density. It can be simulated as follows. (1) Take a draw from the
extreme value distribution, using the procedure described in section
9.2.3. (2) For this draw of _w_, calculate the term in brackets, namely:

_j_ = _i_ _[exp]_ [(] _[−][exp]_ [(] _[−]_ [(] _[v][ni]_ _[−][V][nj]_ [ +] _[θ][i][w]_ [)] _[/θ][j]_ [)). (3) Repeat steps 1 and 2 many]
times and average the results. This average is an approximation to _Pni_ .
Bhat (1995) shows that, since the integral is only one-dimensional, the
heteroskedastic logit probabilities can be calculated effectively with
quadrature rather than simulation.


106 _CHAPTER 4. GEV_

### **4.6 The GEV family**


We now describe the processs that McFadden (1978) developed to generate GEV models. Using this process, the researcher is able to develop
new GEV models that best fit the specific circumstances of his choice
situation. As illustration, we show how the procedure is used to generate models that we have already discussed, namely logit, nested logit,
and paired combinatorial logits. The same procedure can be applied
by a researcher to generate new models with properties that meet his
research needs.
For notational simplicity, we will omit the subscript _n_ denoting the
decision-maker. Also, since we will be using _exp_ ( _Vj_ ) repeatedly, let’s
denote it more compactly by _Yj_ . That is, let _Yj ≡_ _exp_ ( _Vj_ ). Note that
_Yj_ is necessarily positive.
Consider a function _G_ that depends on _Yj_ for all _j_ . We denote
this function _G_ = _G_ ( _Y_ 1 _, . . ., YJ_ ). Let _Gi_ be the derivative of _G_ with
respect to _Yi_ : _Gi_ = _∂G/∂Yi_ . If this function meets certain conditions,
then a discrete choice model can be based upon it. In particular, if G
satisfies the conditions that are listed below, then

_Pi_ = _[Y][i][G][i]_ (4.8)

_G_


is the choice probability for a discrete choice model that is consistent
with utility maximization. Any model that can be derived in this way
is a GEV model. This formula therefore defines the family of GEV
models.
The properties that the function must exhibit are the following.


1. _G ≥_ 0 for all positive values of _Yj ∀_ _j_ .


2. _G_ is homogeneous of degree one. That is, if each _Yj_ is raised by
some proportion _ρ_, _G_ rises by proportion _ρ_ also: _G_ ( _ρY_ 1 _, . . ., ρYJ_ ) =
_ρG_ ( _Y_ 1 _, . . ., YJ_ ). Actually, Ben-Akiva and Francois (1983) showed
that this condition can be relaxed to allow any degree of homogeneity. We retain the usage of degree one since doing makes the
condition easier to interpret and is consistent with McFadden’s
original description.


3. _G →∞_ as _Yj →∞_ for any _j_ .


4. The cross partial derivatives of _G_ change signs in a particular
way. That is: _Gi ≥_ 0 for all _i_, _Gij_ = _∂Gi/∂Yj ≤_ 0 for all _j ̸_ = _i_,


_4.6. THE GEV FAMILY_ 107


_Gijk_ = _∂Gij/∂Yk ≥_ 0 for any distinct _i_, _j_, and _k_, and so on for
higher order cross-partials.


There is little economic intuition to motivate these properties, particularly the last one. However, it is easy to verify whether a function
exhibits these properties. The lack of intuition behind the properties
is a blessing and a curse. The disadvantage is that the researcher has
little guidance on how to specify a _G_ that provides a model that meets
the needs of his research. The advantage is that the purely mathematical approach allows the researcher to generate models that he might
not have developed while relying only on his economic intuition. Karlstrom (2001) provides an example: he arbitrarily specified a _G_ (in the
sense that it was not based on behavioral concepts) and found that
the resulting probability formula fit his data better than logit, nested
logit, and PCL.

We can now show how logit, nested logit, and PCL models are
obtained under appropriate specifications of _G_ .


**Logit**

Let _G_ = [�] _[J]_ _j_ =1 _[Y][j]_ [. This] _[ G]_ [ exhibits the four required properties. (1)]
The sum of positive _Yj_ ’s is positive. (2) If all _Yj_ ’s are raised by a factor
_ρ_, _G_ rises by that same factor. (3) If any _Yj_ rises without bound, then
_G_ does also. (4) The first partial derivative is _Gi_ = _∂G/∂Yi_ = 1 which
meets the criterion that _Gi ≥_ 0. And the higher-order derivatives are
all zero, which clearly meets the criterion since they are _≥_ 0 or _≤_ 0 as
required.
Inserting this _G_ and its first derivative _Gi_ into (4.8), the resulting
choice probability is:


_YiGi_
_Pi_ =

_G_

_Yi_
= ~~�~~ _J_
_j_ =1 _[Y][j]_

_e_ _[V][i]_
= ~~�~~ _J_
_j_ =1 _[e][V][j]_


which is the logit formula.


108 _CHAPTER 4. GEV_


**Nested Logit**



The _J_ alternatives are partitioned into _K_ nests labeled _B_ 1 _, . . ., BK_ .
Let




 - _K_

_G_ =

_ℓ_ =1







 [�] _Yj_ [(1] _[/λ][ℓ]_ [)]

_j∈Bℓ_










_λℓ_

_._



with each _λk_ between zero and one. The first three properties are
easy to verify. For the fourth property, we calculate the first partial
derivative














_λk−_ 1
_λ_ 1 _k_ _Yi_ [(1] _[/λ][k]_ [)] _[−]_ [1]










_Gi_ = _λ_ _[k]_



 [�]



_Yj_ [(1] _[/λ][k]_ [)]
_j∈Bk_







_._



_λk−_ 1



= _Yi_ [(1] _[/λ][k]_ [)] _[−]_ [1]



 [�] _Yj_ [(1] _[/λ][k]_ [)]

_j∈Bk_



 [�]



for _i ∈_ _Bk_ . Since _Yj ≥_ 0 _∀_ _j_, _Gi ≥_ 0, as required. The second crosspartial derivative is



_∂Gi_
_Gim_ =
_∂Ym_


= ( _λk −_ 1) _Yi_ [(1] _[/λ][k]_ [)] _[−]_ [1]



_Yj_ [(1] _[/λ][k]_ [)]
_j∈Bk_







_λk−_ 2
1
_λk_ _Ym_ [(1] _[/λ][k]_ [)] _[−]_ [1]



 [�]











  _λk −_ 1
=

_λk_




( _YiYm_ ) [(1] _[/λ][k]_ [)] _[−]_ [1]







 [�] _Yj_ [(1] _[/λ][k]_ [)]

_j∈Bk_



 [�]










_λk−_ 2



for _m ∈_ _Bk_ and _m ̸_ = _i_ . With _λk ≤_ 1, _Gij ≤_ 0, as required. For
_j_ in a different nest than _i_, _Gij_ = 0 which also meets the criterion.
Higher cross-partials are calculated similarly; they exhibit the required
property if 0 _< λk ≤_ 1.
The choice probability becomes:



_YiGi_
_Pi_ =



_G_



��     - _λk−_ 1
_YiYi_ [(1] _[/λ][k]_ [)] _[−]_ [1] _j∈Bk_ _[Y]_ _j_ [ (1] _[/λ][ℓ]_ [)]
= ~~�~~




~~�~~ _K_ ~~��~~ ~~�~~ _λℓ_
_ℓ_ =1 _j∈Bℓ_ _[Y]_ _j_ [ (1] _[/λ][ℓ]_ [)]


_4.6. THE GEV FAMILY_ 109



��    - _λk−_ 1
_Yi_ [(1] _[/λ][k]_ [)] _j∈Bk_ _[Y]_ _j_ [ (1] _[/λ][ℓ]_ [)]
= ~~�~~




~~�~~ _K_ ~~��~~ ~~�~~ _λℓ_
_ℓ_ =1 _j∈Bℓ_ _[Y]_ _j_ [ (1] _[/λ][ℓ]_ [)]



( _e_ _[V][i]_ ) [(1] _[/λ][k]_ [)][ ��] _j∈Bk_ [(] _[e][V][j]_ [)][(1] _[/λ][ℓ]_ [)][�] _[λ][k][−]_ [1]
= ~~�~~




~~�~~ _K_ ~~��~~ ~~�~~ _λℓ_
_ℓ_ =1 _j∈Bℓ_ [(] _[e][V][j]_ [)][(1] _[/λ][ℓ]_ [)]



��    - _λk−_ 1
_e_ _[V][i][/λ][k]_ _j∈Bk_ _[e][V][j]_ _[/λ][ℓ]_
= ~~�~~




~~�~~ _K_ ~~��~~ ~~�~~ _λℓ_
_ℓ_ =1 _j∈Bℓ_ _[e][V][j]_ _[/λ][ℓ]_



which is the nested logit formula (4.2).


**Paired combinatorial logit**



Let




 - _J_


_ℓ_ = _k_ +1




- _Yk_ [(1] _[/λ][kℓ]_ [)] + _Yℓ_ [(1] _[/λ][kℓ]_ [)] - _λkℓ_ _._



_G_ =



_J_ - _−_ 1


_k_ =1



The required properties are verified in the same way as for the nested
logit. We have




- - - _λij_ _−_ 1 1

_λji_ _Yi_ [(1] _[/λ][ij]_ [)] + _Yj_ [(1] _[/λ][ij]_ [)] _λ_
_j_ = _i_




  _Gi_ =



_λij_ _Yi_ [(1] _[/λ][ij]_ [)] _[−]_ [1]



= - _Yi_ [(1] _[/λ][ij]_ [)] _[−]_ [1] - _Yi_ [(1] _[/λ][ij]_ [)] + _Yj_ [(1] _[/λ][ij]_ [)] - _λij_ _−_ 1 _._

_j_ = _i_



And so the choice probability is:



_YiGi_
_Pi_ =



_G_




  -  -  - _λij_ _−_ 1
_Yi_ _j_ = _i_ _[Y]_ _i_ [ (1] _[/λ][ij]_ [)] _[−]_ [1] _Yi_ [(1] _[/λ][ij]_ [)] + _Yj_ [(1] _[/λ][ij]_ [)]
= ~~�~~ ~~�~~




~~�~~ _Jk_ =1 _−_ 1 ~~�~~ _Jℓ_ = _k_ +1 ~~�~~ _Yk_ [(1] _[/λ][kℓ]_ [)] + _Yℓ_ [(1] _[/λ][kℓ]_ [)] ~~�~~ _λkℓ_



=


=




- - - _λij_ _−_ 1
_j_ = _i_ _[Y]_ _i_ [ (1] _[/λ][ij]_ [)] _Yi_ [(1] _[/λ][ij]_ [)] + _Yj_ [(1] _[/λ][ij]_ [)]

~~�~~ _Jk_ =1 _−_ 1 ~~�~~ _Jℓ_ = _k_ +1 ~~�~~ _Yk_ [(1] _[/λ][kℓ]_ [)] + _Yℓ_ [(1] _[/λ][kℓ]_ [)] ~~�~~ _λkℓ_




- - - _λij_ _−_ 1
_j_ = _i_ _[e][V][i][/λ][ij]_ _e_ _[V][i][/λ][ij]_ + _e_ _[V][j]_ _[/λ][ij]_

~~�~~ _Jk_ =1 _−_ 1 ~~�~~ _Jℓ_ = _k_ +1 ~~�~~ _eVk/λkℓ_ + _eVℓ/λkℓ_ ~~�~~ _λkℓ_



which is the PCL formula (4.6).


110 _CHAPTER 4. GEV_


**Generalized nest logit**



The reader can verify that the GNL probabilities in equation 4.7 are
derived from



_λk_

_._







 [�] ( _αjkYj_ ) [(1] _[/λ][k]_ [)]

_j∈Bk_










_G_ =




- _K_


_k_ =1



Using the same process, researchers can generate other GEV models.


## **Chapter 5**

# **Probit**

### **5.1 Choice probabilities**

The logit model is limited in three important ways. It cannot represent
random taste variation. It exhibits restrictive substitution patterns
due to the IIA property. And it cannot be used with panel data when
unobserved factors are correlated over time for each decision-maker.
GEV models relax the second of these restrictions, but not the other
two. Probit models solve all three issues. They can handle random
taste variation, they allow any pattern of substitution, and they are
applicable to panel data with temporally correlated errors.
The only limitation of probit models is that they require normal distributions for all unobserved components of utility. In many, perhaps
most situations, normal distributions provide an adequate representation of the random components. However, in some situations, normal
distributions are inappropriate and can lead to perverse forecasts. A
prominent example relates to price coefficients. For a probit model
with random taste variation, the coefficient of price is assumed to be
normally distributed in the population. Since the normal distribution
has density on both sides of zero, the model necessarily implies that
some people have a positive price coefficient. The use of a distribution that has density only on one side of zero, such as the log-normal,
is more appropriate and yet cannot be accommodated within probit.
Other than this restriction, the probit model is quite general.
The probit model is derived under the assumption of jointly normal unobserved utility components. The first derivation, by Thurstone
(1927) for a binary probit, used the terminology of psychological stim

111


112 _CHAPTER 5. PROBIT_


uli, which Marschak (1960) translated into economic terms as utility.
Hausman and Wise (1978) and Daganzo (1979) elucidated the generality of the specification for representing various aspects of choice
behavior. Utility is decomposed into observed and unobserved parts:
_Unj_ = _Vnj_ + _εnj ∀_ _j_ . Consider the vector composed of each _εnj_, labeled
_ε_ _[′]_ _n_ [=] _[ ⟨][ε][n]_ [1] _[, . . ., ε][nJ]_ _[⟩]_ [. We assume that] _[ ε][n]_ [is distributed normal with a]
mean vector of zero and covariance matrix Ω. The density of _εn_ is



1
_φ_ ( _εn_ ) = _J_



_J_ 1 _e_ _[−]_ 2 [1]

2 _|_ Ω _|_ 2



_J_
(2 _π_ ) 2




[1] 2 _[ε]_ _n_ _[′]_ [Ω] _[−]_ [1] _[ε][n]_ _._



The covariance Ωcan depend on variables faced by decision-maker _n_,
such that Ω _n_ is the more appropriate notation; however, we omit the
subscript for the sake of simplicity.
The choice probability is


_Pni_ = _Prob_ ( _Vni_ + _εni > Vnj_ + _εnj ∀_ _j ̸_ = _i_ )

        = _I_ ( _Vni_ + _εni > Vnj_ + _εnj ∀_ _j ̸_ = _i_ ) _φ_ ( _εn_ ) _dεn_ (5.1)


where _I_ ( _·_ ) is an indicator of whether the statement in parentheses holds
and the integral is over all values of _εn_ . This integral does not have a
closed form. It must be evaluated numerically through simulation.
The choice probabilities can be expressed in a couple of other ways
that are useful for simulating the integral. Let _Bni_ be the set of error
terms _εn_ that result in the decision-maker choosing alternative _i_ : _Bni_ =
_{εn_ s.t. _Vni_ + _εni > Vnj_ + _εnj ∀_ _j ̸_ = _i}_ . Then

             _Pni_ = _φ_ ( _εn_ ) _dεn_ (5.2)

_εn∈Bni_


which is an integral over only some of the values of _εn_ rather than all
possible values, namely, the _εn_ ’s in _Bni_ .
Expressions (5.1) and (5.2) are _J_ dimensional integrals over the
_J_ errors _εnj, j_ = 1 _, . . ., J_ . Since only differences in utility matter,
the choice probabilities can be equivalently expressed as _J −_ 1 dimensional integrals over the differences between the errors. Let us
difference against alternative _i_, the alternative for which we are calculating the probability. Define _U_ [˜] _nji_ = _Unj −_ _Uni_, _V_ [˜] _nji_ = _Vnj −_ _Vni_,
and ˜ _εnji_ = _εnj −_ _εni_ . Then _Pni_ = _Prob_ ( _U_ [˜] _nji <_ 0 _∀_ _j ̸_ = _i_ ). That is,
the probability of choosing alternative _i_ is the probability that all the


_5.1. CHOICE PROBABILITIES_ 113


utility differences, when differenced against _i_, are negative. Define the
vector ˜ _εni_ = _⟨ε_ ˜ _n_ 1 _i, . . .,_ ˜ _εnJ_ 1 _⟩_ where the “ _. . ._ ” is over all alternatives except _i_, such that ˜ _εni_ has dimension _J −_ 1. Since the difference between
two normals is normal, the density of the error differences is



1
_φ_ (˜ _εni_ ) = [1]




[1] 2 [(] _[J][−]_ [1)] _|_ Ω [˜] _i|_ 12 _e_ _[−]_ 2 [1]



(2 _π_ ) _[−]_ [1] 2




[1] 2 _[ε]_ [˜] _ni_ _[′]_ [˜Ω] _[i][ε]_ [˜] _[ni]_



where Ω [˜] _i_ is the covariance of ˜ _εni_, derived from Ω. Then the choice
probability expressed in utility differences is:

         _Pni_ = _I_ ( _V_ [˜] _nji_ + ˜ _εnji <_ 0 _∀_ _j ̸_ = _i_ ) _φ_ (˜ _εni_ ) _dε_ ˜ _ni_ (5.3)


which is a _J −_ 1 dimensional integral over all possible values of the
error differences. An equivalent expression is:

             _Pni_ = _φ_ (˜ _εni_ ) _dε_ ˜ _ni_ (5.4)

_ε_ ˜ _ni∈B_ [˜] _ni_


where _B_ [˜] _ni_ = _{ε_ ˜ _ni_ s.t. _V_ [˜] _nji_ + ˜ _εnji <_ 0 _∀_ _j ̸_ = _i}_, which is a _J −_ 1
dimensional integral over the error differences in _B_ [˜] _ni_ .
Expressions (5.3) and (5.4) utilize the covariance matrix Ω [˜] _i_ of the
error differences. There is a straightforward way to derive Ω [˜] _i_ from the
covariance of the errors themselves, Ω. Let _Mi_ be the _J −_ 1 identity
matrix with an extra column of _−_ 1’s added as the _i_ -th column. The
extra column makes the matrix have size _J −_ 1 by _J_ . For example,
with _J_ = 4 alternatives and _i_ = 3, _Mi_ is







 _._



_Mi_ =





1 0 _−_ 1 0

 0 1 _−_ 1 0
0 0 _−_ 1 1



This matrix can be used to transform the covariance matrix of
errors into the covariance matrix of error differences: Ω [˜] _i_ = _Mi_ Ω _Mi_ _[′][.]_
Note that Ω [˜] _i_ is ( _J −_ 1) _×_ ( _J −_ 1) while Ωis _J ×_ _J_, since _Mi_ is ( _J −_ 1) _×_
_J_ . As illustration, consider a three-alternative situation with errors
_⟨εn_ 1 _, εn_ 2 _, εn_ 3 _⟩_ that have covariance







 _._



Ω=





_σ_ 11 _σ_ 12 _σ_ 13

 _σ_ 12 _σ_ 22 _σ_ 23
_σ_ 13 _σ_ 23 _σ_ 33


114 _CHAPTER 5. PROBIT_


Suppose we takes differences against alternative 2. We know from first
principles that the error differences _⟨ε_ ˜ _n_ 12 _,_ ˜ _εn_ 32 _⟩_ have covariance











˜Ω2 = _Cov_




_εn_ 1 _−_ _εn_ 2
_εn_ 3 _−_ _εn_ 2



=




_σ_ 11 + _σ_ 22 _−_ 2 _σ_ 12 _σ_ 13 + _σ_ 22 _−_ _σ_ 12 _−_ _σ_ 23
_σ_ 13 + _σ_ 22 _−_ _σ_ 12 _−_ _σ_ 23 _σ_ 33 + _σ_ 22 _−_ 2 _σ_ 23



_._



This covariance matrix can also be derived by the transformation Ω [˜] 2 =
_M_ 2Ω _M_ 2 _[′]_ [:]







1 0

 _−_ 1 _−_ 1
0 1












- []

_σ_ 11 _σ_ 12 _σ_ 13

 _σ_ 12 _σ_ 22 _σ_ 23
_σ_ 13 _σ_ 23 _σ_ 33











˜Ω _n_ =


=


=


=




1 _−_ 1 0
0 _−_ 1 1




_σ_ 11 + _σ_ 22 _−_ 2 _σ_ 12 _σ_ 13 + _σ_ 22 _−_ _σ_ 12 _−_ _σ_ 23
_σ_ 13 + _σ_ 22 _−_ _σ_ 12 _−_ _σ_ 23 _σ_ 33 + _σ_ 22 _−_ 2 _σ_ 23




_σ_ 11 _−_ _σ_ 12 _σ_ 12 _−_ _σ_ 22 _σ_ 13 _−_ _σ_ 23
_−σ_ 12 + _σ_ 13 _−σ_ 22 + _σ_ 23 _−σ_ 23 + _σ_ 33




- []



1 0

 _−_ 1 _−_ 1
0 1












_σ_ 11 _−_ _σ_ 12 _−_ _σ_ 12 + _σ_ 22 _−σ_ 12 + _σ_ 22 + _σ_ 13 _−_ _σ_ 23
_−σ_ 12 + _σ_ 13 + _σ_ 22 _−_ _σ_ 23 _σ_ 22 _−_ _σ_ 23 _−_ _σ_ 23 + _σ_ 33











As we will see, this transformation by _Mi_ comes in handy when simulating probit probabilities.

### **5.2 Identification**


As described in section (2.5), any discrete choice model must be normalized to account for the fact that the level and scale of utility is irrelevant. The level of utility is immaterial since a constant can be added
to the utility of all alternatives without changing which alternative has
the highest utility: the alternative with the highest utility before the
constant is added still has the highest utility after the constant is added
to all utilities. Similarly, the scale of utility doesn’t matter since the
utility of each alternative can be multiplied by a (positive) constant
without changing which alternative has the highest utility. In logit and
nested logit models, the normalization for scale and level occurs automatically with the distributional assumptions that are placed on the
error terms. As a result, normalization does not need to be considered


_5.2. IDENTIFICATION_ 115


explicitly for these models. With probit models, however, normalization for scale and level does not occur automatically. The researcher
must normalize the model directly.


Normalization of the model is related to parameter identification.
A parameter is “identified” if it can be estimated and is “unidentified”
if it cannot be estimated. An example of an unidentified parameter is
_k_ in the utility specification _Unj_ = _Vnj_ + _k_ + _εnj_ . While the researcher
might write utility in this way, and might want to estimate _k_ to obtain
a measure of the overall level of utility, doing so is impossible. The
behavior of the decision-maker is unaffected by _k_, and so the researcher
cannot infer the value of _k_ from the choices that decision-makers have
made. Stated directly: parameters that do not affect the behavior of
decision-makers cannot be estimated. In an unnormalized model, parameters can appear that are not identified; these parameters relate to
the scale and level of utility, which do not affect behavior. Once the
model is normalized, these parameters disappear. The difficulty arises
because it is not always obvious which parameters relate to scale and
level. In the above example, the fact that _k_ is unidentified is fairly
obvious. In many cases, it is not at all obvious which parameters are
identified. Bunch and Kitamura (1989) have shown that the probit
models in several published articles are not normalized and contain
unidentified parameters. The fact that neither the authors nor the reviewers of these articles could tell that the models were un-normalized
is a testament to the complexity of the issue.


I provide below a procedure that can always be used to normalize
a probit model and assure that all parameters are identified. It is not
the only procedure that can be used; see, for example, Bunch (1991).
In some cases a researcher might find other normalization procedures
more convenient. However, the procedure I give can always be used,
either by itself or as a check on whatever other procedure the researcher
uses for normalization.


I describe the procedure in terms of a four-alternative model. Generalization to more alternatives is obvious. As usual, utility is expressed as _Unj_ = _Vnj_ + _εnj j_ = 1 _, . . .,_ 4. The vector of errors is
_ε_ _[′]_ _n_ [=] _[ ⟨][ε][n]_ [1] _[, . . ., ε][n]_ [4] _[⟩]_ [.] The error vector is normally distributed with


