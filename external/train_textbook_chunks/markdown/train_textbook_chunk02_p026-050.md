16 _CHAPTER 2. PROPERTIES_


characteristics. First, the alternatives must be _mutually exclusive_ from
the decision-maker’s perspective. Choosing one alternative necessarily
implies not choosing any of the other alternatives. The decision-maker
chooses only one alternative from the choice set. Second, the choice
set must be _exhaustive_, in that all possible alternatives are included.
The decision-maker necessarily chooses one of the alternatives. Third,
the number of alternatives must be finite. The researcher can count
the alternatives and eventually be finished counting.


The first and second criteria are not restrictive. Appropriate definition of alternatives can nearly always assure that the alternatives
are mutually exclusive and the choice set is exhaustive. For example,
suppose two alternatives labeled A and B are not mutually exclusive
because the decision-maker can choose both of the alternatives. The
alternatives can be redefined to be “A only,” “B only,” and “both A
and B,” which are necessarily mutually exclusive. Similarly, a set of
alternatives might not be exhaustive because the decision-maker has
the option of not choosing any of them. In this case, an extra alternative can be defined as “none of the other alternatives.” The expanded
choice set, consisting of the original alternatives plus this new one, is
clearly exhaustive.


Often the researcher can satisfy these two conditions in several different ways. The appropriate specification of the choice set in these
situations is governed largely by the goals of the research and the data
that are available to the researcher. Consider households’ choice among
heating fuels, a topic which has been studied extensively in efforts to
forecast energy use and to develop effective fuel-switching and energy
conservation programs. The available fuels are usually natural gas,
electricity, oil and wood. These four alternatives, as listed, violate both
mutual exclusivity and exhaustiveness. The alternatives are not mutually exclusive because a household can (and many do) have two types
of heating, e.g., a natural gas central heater and electric room heaters,
or a wood stove along with electric baseboard heating. And the set
is not exhaustive because the household can have no heating (which,
unfortunately, is not as rare as one might hope.) The researcher can
handle each of these issues in several ways. To obtain mutually exclusive alternatives, one approach is to list every possible combination
of heating fuels as an alternative. The alternatives are then defined
as: “electricity alone,” “electricity and natural gas, but no other fuels,”
and so on. Another approach is to define the choice as the choice among


_2.2. THE CHOICE SET_ 17


fuels for the “primary” heating source. Under this procedure, the researcher develops a rule for determining which heating fuel is primary
when a household uses multiple heating fuels. By definition, only one
fuel (electricity, natural gas, oil, or wood) is primary. The advantage
of listing every possible combination of fuels is that it avoids the need
to define a “primary” fuel, which is a difficult and somewhat arbitrary
distinction. Also, with all combinations considered, the researcher has
the ability to examine the factors that determine households’ use of
multiple fuels. However, to implement this approach, the researcher
needs data that distinguish the alternatives, for example, the cost of
heating a house with natural gas and electricity versus the cost with
natural gas alone. If the researcher restricts the analysis to choice of
primary fuel, then the data requirements are less severe. Only the
costs associated with each fuel are needed. Also, a model with four
alternatives is inherently easier to estimate and forecast with than a
model with the large number of alternatives that arises when every
possible combination of fuels is considered. The researcher will need
to take these tradeoffs into consideration when specifying the choice
set.


The same type of issue arises with regard to exhaustiveness. In
our case of heating fuel choice, the researcher can either include “no
heating” as an alternative or can redefine the choice situation as being
the choice of heating fuel conditional on having heating. The first
approach allows the researcher to examine the factors that relate to
whether a household has heating. However, this ability is only realized
if the researcher has data that meaningfully relate to whether or not
a household has heating. Under the second approach, the researcher
excludes from the analysis households without heating, and, by doing
so, is relieved of the need for data that relate to these households.


As we have just described, the conditions of mutual exclusivity
and exhaustiveness can usually be satisfied, and the researcher often
has several approaches for doing so. In contrast, the third condition,
namely, that the number of alternatives is finite, is actually restrictive.
This condition is the defining characteristic of discrete choice models
and distinguishes their realm of application from that for regression
models. With regression models, the dependent variable is continuous,
which means that there is an infinite number of possible outcomes.
The outcome might be chosen by a decision-maker, such as the decision of how much money to hold in savings accounts. However, the


18 _CHAPTER 2. PROPERTIES_


alternatives available to the decision-maker, which are every possible
monetary value above zero, is not finite (at least not if all fractions
are considered, which is an issue we return to below.) When there is
an infinite number of alternatives, discrete choice models cannot be
applied.


Often regression models and discrete choice models are distinguished
by saying that regressions examine choices of “how much” and discrete
choice models examine choice of “which.” This distinction, while perhaps illustrative, is not actually accurate. Discrete choice models can
and have been used to examine choices of “how much.” A prominent
example is households’ choice of how many cars to own. The alternatives are 0, 1, 2, and so on, up to the highest number that the
researcher defines as feasible (or observed.) This choice set contains a
finite number of mutually exclusive and exhaustive alternatives, such
that it is appropriate for analysis via discrete choice models. The researcher can also define the choice set more succinctly as 0, 1, and
2 or more vehicles, if the goals of the research can be met with this
specification.


When considered in this way, most choices involving “how many”
can be represented in a discrete choice framework. In the case of
savings accounts, every one-dollar increment (or even every one-cent
increment) can be considered an alternative, and as long as some finite maximum exists, then the choice set fits the criteria for discrete
choice. Whether to use regression or discrete choice models in these
situations is a specification issue that the researcher must consider.
Usually a regression model is more natural and is certainly easier. A
discrete choice model would be used in these situations only if there
are compelling reasons for doing so. As an example, Train, McFadden
and Ben-Akiva (1987) analyzed the number and duration of phone
calls that households make, using a discrete choice model instead of a
regression model because the discrete choice model allowed greater flexibility in handling the non-linear price schedules that households face.
In general, the researcher needs to consider the goals of the research
and the capabilities of alternative methods when deciding whether to
apply a discrete choice model.


_2.3. DERIVATION OF CHOICE PROBABILITIES_ 19

# **2.3 Derivation of choice probabilities**


Discrete choice models are usually derived under an assumption of
utility-maximizing behavior by the decision-maker. Thurstone (1927)
originally developed the concepts in terms of psychological stimuli,
leading to a binary probit model of whether respondents can differentiate the level of stimulus. Marschak (1960) interpreted the stimuli
as utility and provided a derivation from utility maximization. Following Marschak, models that can be derived in this way are called
random utility models (RUMs). It is important to note, however, that
models derived from utility maximization can also be used to represent
decision-making that does not entail utility maximization. The derivation assures that the model is consistent with utility maximization; it
does not preclude the model from being consistent with other forms
of behavior. The models can also be seen as simply describing the
relation of explanatory variables to the outcome of a choice, without
reference to exactly how the choice is made.

Random utility models are derived as follows. A decision-maker,
labeled _n_, faces a choice among _J_ alternatives. The decision-maker
would obtain a certain level of utility (or profit) from each alternative.
The utility that decision-maker _n_ obtains from alternative _j_ is _Unj, j_ =
1 _, . . ., J_ . This utility is known to the decision-maker but not, as we see
below, by the researcher. The decision-maker chooses the alternative
that provides the greatest utility. The behavioral model is therefore:
choose alternative _i_ if and only if _Uni > Unj ∀_ _j ̸_ = _i_ .
Consider now the researcher. The researcher does not observe the
decision-maker’s utility. The researcher observes some attributes of
the alternatives as faced by the decision-maker, labeled _xnj ∀_ _j_, and
some attributes of the decision-maker, labeled _sn_, and can specify a
function that relates these observed factors to the decision-maker’s
utility. The function is denoted _Vnj_ = _V_ ( _xnj, sn_ ) _∀_ _j_ and is often
called ”representative utility.” Usually, _V_ depends on parameters that
are unknown to the researcher and therefore estimated statistically;
however, this dependence is suppressed for the moment.

Since there are aspects of utility that the researcher does not or
cannot observe, _Vnj ̸_ = _Unj_ . Utility is decomposed as _Unj_ = _Vnj_ + _εnj_,
where _εnj_ captures the factors that affect utility but are not included in
_Vnj_ . This decomposition is fully general, since _εnj_ is defined as simply
the difference between true utility _Unj_ and the part of utility that the


20 _CHAPTER 2. PROPERTIES_


researcher captures in _Vnj_ . Given its definition, the characteristics of
_εnj_, such as its distribution, depend critically on the researcher’s specification of _Vnj_ . In particular, _εnj_ is not defined for a choice situation
_per se_ . Rather, it is defined relative to a researcher’s representation of
that choice situation. This distinction becomes relevant when evaluating the appropriateness of various specific discrete choice models.
The researcher does not know _εnj ∀_ _j_ and therefore treats these
terms as random. The joint density of the random vector _εn_ = _⟨εn_ 1 _, . . ., εnJ_ _⟩_
is denoted _f_ ( _εn_ ). With this density, the researcher can make probabilistic statements about the decision-maker’s choice. The probability
that decision-maker _n_ chooses alternative _i_ is


_Pni_ = _Prob_ ( _Uni > Unj ∀_ _j ̸_ = _i_ )

= _Prob_ ( _Vni_ + _εni > Vnj_ + _εnj ∀_ _j ̸_ = _i_ )

= _Prob_ ( _εnj −_ _εni < Vni −_ _Vnj ∀_ _j ̸_ = _i_ ) (2.1)


This probability is a cumulative distribution, namely, the probability that each random term _εnj −_ _εni_ is below the observed quantity
_Vni −_ _Vnj_ . Using the density _f_ ( _εn_ ), this cumulative probability can be
rewritten as:



_Pni_ = _Prob_ ( _εnj −_ _εni < Vni −_ _Vnj ∀_ _j ̸_ = _i_ )




  =



_I_ ( _εnj −_ _εni < Vni −_ _Vnj ∀_ _j ̸_ = _i_ ) _f_ ( _εn_ ) _dεn,_ (2.2)
_ε_



where _I_ ( _·_ ) is the indicator function, equaling 1 when the term in parentheses is true and 0 otherwise. This is a multidimensional integral over
the density of the unobserved portion of utility, _f_ ( _εn_ ). Different discrete choice models are obtained from different specifications of this
density, that is, from different assumptions about the distribution of
the unobserved portion of utility. The integral takes a closed-form only
for certain specifications of _f_ ( _·_ ). Logit and nested logit have closedform expressions for this integral. They are derived under the assumption that the unobserved portion of utility is distributed iid extreme
value and a type of generalized extreme value, respectively. Probit is
derived under the assumption that _f_ ( _·_ ) is a multivariate normal, and
mixed logit is based on the assumption that the unobserved portion
of utility consists of a part that follows any distribution specified by
the researcher plus a part that is iid extreme value. With probit and
mixed logit, the resulting integral does not have a closed form and


_2.3. DERIVATION OF CHOICE PROBABILITIES_ 21


is evaluated numerically through simulation. Each of these models is
discussed in detail in subsequent chapters.
The meaning of choice probabilities is more subtle, and more revealing, than it might at first appear. An example serves as illustration.
Consider a person who can take either a car or bus to work. The
researcher observes the time and cost that the person would incur under each mode. However, the researcher realizes that there are factors
other than time and cost that affect the person’s utility and hence his
choice. The researcher specifies


_Vc_ = _αTc_ + _βMc_
_Vb_ = _αTb_ + _βMb_


where _Tc_ and _Mc_ are the time and cost (i.e., money) that the person
incurs traveling to work by car, _Tb_ and _Mb_ are defined analogously
for bus, and the subscript _n_ denoting the person is omitted for convenience. The coefficients _α_ and _β_ are either known or estimated by the
researcher.
Suppose that, given _α_ and _β_ and the researcher’s measures of the
time and cost by car and bus, it turns out that _Vc_ = 4 and _Vb_ = 3. This
means that, on observed factors, car is better for this person than bus
by 1 unit. (We discuss below the normalization of utility that sets the
dimension to these units.) It does not mean, however, that the person
necessarily chooses car, since there are other factors not observed by
the researcher that affect the person. The probability that the person
chooses bus instead of car is the probability that the unobserved factors for bus are sufficiently better than those for car to overcome the
advantage that car has on observed factors. Specifically, the person
will choose bus if the unobserved portion of utility is higher than that
for car by at least 1 unit, thus overcoming the 1 unit advantage that
car has on observed factors. The probability of this person choosing
bus is therefore the probability that _εb −_ _εc >_ 1. Conversely, the person will choose car if the unobserved utility for bus is _not_ better than
that for car by at least 1 unit, that is, if _εb −_ _εc <_ 1. Since 1 is the
difference between _Vc_ and _Vb_ in our example, the probabilities can be
stated more explicitly as:


_Pc_ = _Prob_ ( _εb −_ _εc < Vc −_ _Vb_ )

and

_Pb_ = _Prob_ ( _εb −_ _εc > Vc −_ _Vb_ )


22 _CHAPTER 2. PROPERTIES_


= _Prob_ ( _εc −_ _εb < Vb −_ _Vc_ ) _._


These equations are the same as equation (2.1) above, re-expressed for
our car-bus example.
The question arises in the derivation of the choice probabilities:
what is meant by the distribution of _εn_ ? The interpretation that the
researcher places on this density affects the researcher’s interpretation of the choice probabilities. The most prominent way to think
about this distribution is as follows. Consider a population of people who face the same observed utility _Vnj ∀_ _j_ as person _n_ . Among
these people, the values of the unobserved factors differ. The density
_f_ ( _εn_ ) is the distribution of the unobserved portion of utility within
the population of people who face the same observed portion of utility.
Under this interpretation, the probability _Pni_ is the share of people
who choose alternative _i_ within the population of people who face the
same observed utility for each alternative as person _n_ . The distribution can also be considered in subjective terms, as representing the
researcher’s subjective probability that the person’s unobserved utility
will take given values. In this case, the _Pni_ is the probability that
the researcher ascribes to the person’s choosing alternative _i_ given the
researcher’s ideas about the unobserved portions of the person’s utility. As a third possibility, the distribution can represent the effect of
factors that are quixotic to the decision-maker himself (representing,
e.g., aspects of bounded rationality), such that _Pni_ is the probability
that these quixotic factors induce the person to choose alternative _i_
given the observed, non-quixotic factors.

# **2.4 Specific models**


Logit, GEV, probit, and mixed logit are discussed at length in the subsequent chapters. However, a quick preview of these models is useful
at this point, to show how they relate to the general derivation of all
choice models and how they differ within this derivation. As stated
above, different choice models are derived under different specifications
of the density of unobserved factors, _f_ ( _εn_ ). The issues therefore are:
what distribution is assumed for each model, and what is the motivation for these different assumptions.
Logit (discussed in Chapter 3) is by far the most widely used discrete choice model. It is derived under the assumption that _εni_ is


_2.4. SPECIFIC MODELS_ 23


distributed iid extreme value for all _i_ . The critical part of the assumption is that the unobserved factors are uncorrelated over alternatives,
as well as having the same variance for all alternatives. This assumption, while restrictive, provides a very convenient form for the choice
probability. The popularity of the logit model is due to this convenience. However, the assumption of independence can be inappropriate in some situations. Unobserved factors related to one alternative
might be similar to those related to another alternative. For example, a person who dislikes travel by bus because of the presence of
other riders might have a similar reaction to rail travel; if so, then the
unobserved factors affecting bus and rail are corrrelated rather than independent. The assumption of independence also enters When a logit
model is applied to sequences of choices over time. The logit model
assumes that each choice is independent of the others. In many cases,
one would expect that unobserved factors that affect the choice in one
period would persist, at least somewhat, into the next period, inducing
dependence among the choices over time.


The development of other models has arisen largely to avoid the
independence assumption within a logit. Generalized extreme value
models (GEV, discussed in Chapter 4) are based, as the name implies,
on a generalization of the extreme value distribution. The generalization can take many forms, but the common element is that it allows
correlation in unobserved factors over alternatives and collapses to the
logit model when this correlation is zero. Depending on the type of
GEV model, the correlations can be more or less flexible. For example,
a comparatively simple GEV model places the alternatives into several
groups called nests, with unobserved factors having the same correlation for all alternatives within a nest and no correlation for alternatives
in different nests. More complex forms allow essentially any pattern
of correlation. GEV models usually have closed-forms for the choice
probabilities, such that simulation is not required for their estimation.


Probits (Chapter 5) are based on the assumption that the unobserved factors are distributed jointly normal: _ε_ _[′]_ _n_ [=] _[ ⟨][ε][n]_ [1] _[, ldots, ε][nJ]_ _[⟩∼]_
_N_ (0 _,_ Ω). With full covariance matrix Ω, any pattern of correlation
and heteroskedasticity can be accommodated. When applied to sequences of choices over time, the unobserved factors are assumed to be
jointly normal over time as well as over alternatives, with any temporal correlation pattern. The flexibility of the probit model in handling
correlations over alternatives and time is its main advantage. Its only


24 _CHAPTER 2. PROPERTIES_


functional limitation is arises from its reliance on the normal distribution. In some situations, unobserved factors might not be normally
distributed. For example, customer’s willingness to pay for a desirable attribute of a product is necessary positive. Assuming that this
unobserved factor is normally distributed contradicts the fact that it
is positive, since the normal distribution has density on both sides of
zero.
Mixed logit (chapter 6) allows the unobserved factors to follow any
distribution. The defining characteristic of a mixed logit is that the
unobserved factors can be decomposed into a part that contains all the
correlation and heteroskedasticity, and another part that is iid extreme
value. The first part can follow any distribution, including non-normal
distributions. We will show that mixed logit can approximate any
discrete choice model and, as such, is fully general.
Other discrete choice models (Chapter 7) have been specified by
researchers for specific purposes. Often these models are obtained by
combining concepts from other models. For example, a mixed probit is
obtained by decomposing the unobserved factors into two parts, as in
mixed logit, but giving the second part a normal distribution instead
of extreme value. This model has the generality of mixed logit and
yet for some situations can be easier to estimate. By understanding
the derivation and motivation for all the models, each researcher can
specify a model that is tailor-made for the situation and goals of her
research.

# **2.5 Identification of choice models**


Several aspects of the behavioral decision process affect the specification and estimation of any discrete choice model. The issues can be
summarized easily in two statements: “Only differences in utility matter” and “The scale of utility is arbitrary.” The implications of these
statements are far-reaching, subtle and, in many cases, quite complex.
We discuss them below.


**2.5.1** **Only differences in utility matter**


The absolute level of utility is irrelevant to both the decision-maker’s
behavior and the researcher’s model. If a constant is added to the
utility of all alternatives, the alternative with the highest utility doesn’t


_2.5. IDENTIFICATION OF CHOICE MODELS_ 25


change. The decision-maker chooses the same alternative with _Unj ∀_ _j_
as with _Unj_ + _k ∀_ _j_ for any constant _k_ . A colloquial way to express
this fact is, “A rising tide raises all boats.”

The level of utility doesn’t matter from the researcher’s perspective
either. The choice probability is _Pni_ = _Prob_ ( _Uni > Unj ∀_ _j ̸_ = _i_ ) =
_Prob_ ( _Uni −_ _Unj >_ 0 _∀_ _j ̸_ = _i_ ), which depends only on the difference
in utility, not its absolute level. When utility is decomposed into the
observed and unobserved parts, equation (2.1) expresses the choice
probability as _Pni_ = _Prob_ ( _εnj −_ _εni < Vni −_ _Vnj ∀_ _j ̸_ = _i_ ), which also
depends only on differences.

The fact that only differences in utility matter has several implications for the identification and specification of discrete choice models.
In general it means that the only parameters that can be estimated
(that is, are identified) are those that capture differences across alternatives. This general statement takes several forms.


**Alternative-specific constants**


It is often reasonable to specify the observed part of utility to be linear
in parameters with a constant: _Vnj_ = _x_ _[′]_ _nj_ _[β]_ [ +] _[ k][j][,][ ∀]_ _[j]_ [, where] _[ x][nj]_ [ is a]
vector of variables that relate to alternative _j_ as faced by decisionmaker _n_, _β_ are coefficients of these variables, and _kj_ is a constant that
is specific to alternative _j_ . The alternative-specific constant for an
alternative captures the average impact on utility of all factors that
are not included in the model. As such, they serve a similar function
as the constant in a regression model, which also captures the average
impact of all unincluded factors.

When alternative-specific constants are included, the unobserved
portion of utility, _εnj_, has zero mean by construction. If _εnj_ has a
nonzero mean when the constants are not included, then adding the
constants makes the remaining error have zero mean: that is, if _Unj_ =
_x_ _[′]_ _nj_ _[β]_ [ +] _[ ε][∗]_ _nj_ [with] _[ E]_ [(] _[ε][nj]_ [)] _[∗]_ [=] _[ k][j][ ̸]_ [= 0, then] _[ U][nj]_ [ =] _[ x]_ _nj_ _[′]_ _[β]_ [ +] _[ k][j]_ [ +] _[ ε][nj]_ [ with]
_E_ ( _εnj_ ) = 0. It is reasonable, therefore, to include a constant in _Vnj_
for each alternative. However, since only differences in utility matter,
only differences in the alternative-specific constants are relevant, not
their absolute levels. To reflect this fact, the researcher must set the
overall level of these constants.

The concept is readily apparent in the car-bus example. A specifi

26 _CHAPTER 2. PROPERTIES_


cation of utility that takes the form:


_Uc_ = _αTc_ + _βMc_ + _kc_ [0] [+] _[ ε][c]_
_Ub_ = _αTb_ + _βMb_ + _kb_ [0] [+] _[ ε][b]_

with _kb_ [0] _[−]_ _[k]_ _c_ [0] [=] _[ d]_ [, is equivalent to a model with]

_Uc_ = _αTc_ + _βMc_ + _kc_ [1] [+] _[ ε][c]_
_Ub_ = _αTb_ + _βMb_ + _kb_ [1] [+] _[ ε][b]_


where the difference in the new constants is the same as the difference
in the old constants, namely _kb_ [1] _[−]_ _[k]_ _c_ [1] [=] _[ d]_ [ =] _[ k]_ _b_ [0] _[−]_ _[k]_ _c_ [0][. Any model with]
the same difference in constants is equivalent. In terms of estimation,
it is impossible to estimate both constants since an infinite number of
values of the two constants (any values that have the same difference)
result in the same choice probabilities.
To account for this fact, the researcher must normalize the absolute
levels of the constants. The standard procedure is to normalize one
of the constants to zero. For example, the researcher might normalize
the constant for the car alternative to zero:


_Uc_ = _αTc_ + _βMc_ + _εc_
_Ub_ = _αTb_ + _βMb_ + _kb_ + _εb_


Under this normalization, the value of _kb_ is _d_, which is the difference in
the original (unnormalized) constants. The bus constant is interpreted
as the average impact of unincluded factors on the utility of bus _relative_
to car.
With _J_ alternatives, at most _J −_ 1 alternative-specific constants
can enter the model, with one of the constants normalized to zero. It
is irrelevant which constant is normalized to zero: the other constants
are interpreted as being relative to whichever one is set to zero. The
researcher could normalize to some value other than zero, of course;
however, there would be no point in doing so, since normalizing to
zero is easier (the constant is simply left out of the model) and has the
same effect.


**Socio-demographic variables**


The same issue affects the way that socio-demographic variables enter
a model. Attributes of the alternatives, such as the time and cost of


_2.5. IDENTIFICATION OF CHOICE MODELS_ 27


travel on different modes, generally vary over alternatives. However,
attributes of the decision-maker do not vary over alternatives. They
can only enter the model if they are specified in ways that create
differences in utility over alternatives.
Consider for example the impact of a person’s income on the decision of whether to take bus or car to work. It is reasonable to suppose
that a person’s utility is higher with higher income, whether the person
takes bus or car. Utility is specified as:


_Uc_ = _αTc_ + _βMc_ + _θc_ [0] _[Y]_ [ +] _[ ε][c]_
_Ub_ = _αTb_ + _βMb_ + _θb_ [0] _[Y]_ [ +] _[ k][b]_ [+] _[ ε][b]_


where _Y_ is income and _θc_ [0] [and] _[ θ]_ _b_ [0] [capture the effect of changes in]
income on the utility of taking car and bus, respectively. We expect
that _θc_ [0] _[>]_ [ 0 and] _[ θ]_ _b_ [0] _[>]_ [ 0 since greater income makes people happier no]
matter what mode they take. However, _θc_ [0] [=] _[ θ]_ _b_ [0] [since income probably]
has a different effect on the person depending on their mode of travel.
Since only differences in utility matter, the absolute levels of _θc_ [0] [and]
_θb_ [0] [cannot be estimated, only their difference. To set the level, one of]
these parameters is normalized to zero. The model becomes:


_Uc_ = _αTc_ + _βMc_ + _εc_
_Ub_ = _αTb_ + _βMb_ + _θbY_ + _kb_ + _εb_


where _θb_ = _θb_ [0] _[−][θ]_ _c_ [0] [and is interpreted as the differential effect of income]
on the utility of bus compared to car. The value of _θb_ can be either
positive or negative.
Socio-demographic variables can enter utility in other ways. For
example, cost is often divided by income:


_Uc_ = _αTc_ + _βMc/Y_ + _εc_
_Ub_ = _αTb_ + _βMb/Y_ + _θbY_ + _kb_ + _εb_


The coefficient of cost in this specification is _β/Y_ . Since this coefficient
decreases in _Y_, the model reflects the concept that cost becomes less
important in a person’s decision-making, relative to other issues, when
income rises.
When socio-demographic variables are interacted with attributes
of the alternatives, there is no need to normalize the coefficients. The
socio-demographic variables affect the differences in utility through


28 _CHAPTER 2. PROPERTIES_


their interaction with the attributes of the alternatives. The difference
_Uc −_ _Ub_ = _. . . β_ ( _Mc −_ _Mb_ ) _/Y . . ._ varies with income since costs differ
over alternatives.


**Number of independent error terms**


As given by equation (2.2), the choice probabilities take the form


       _Pni_ = _I_ ( _εnj −_ _εni > Vnj −_ _Vni ∀_ _j ̸_ = _i_ ) _f_ ( _εn_ ) _dεn._

_ε_


This probability is a _J_ dimensional integral over the density of the _J_
error terms in _εn_ = _⟨εn_ 1 _, . . ., εnJ_ _⟩_ . The dimension can be reduced,
however, through recognizing that only differences in utility matter.
With _J_ errors (one for each alternative), there are _J −_ 1 error differences. The choice probability can be expressed as a _J −_ 1 dimensional
integral over the density of these error differences:


_Pni_ = _Prob_ ( _Uni > Unj ∀_ _j ̸_ = _i_ )

= _Prob_ ( _εnj −_ _εni < Vni −_ _Vnj ∀_ _j ̸_ = _i_ )

= _Prob_ (˜ _εnji < Vni −_ _Vnj ∀_ _j ̸_ = _i_ )

         = _I_ (˜ _εnji < Vni −_ _Vnj ∀_ _j ̸_ = _i_ ) _g_ (˜ _εni_ ) _dε_ ˜ _ni_


where ˜ _εnji_ = _εnj −_ _εni_ is the difference in errors for alternatives _i_
and _j_ ; ˜ _εni_ = _⟨ε_ ˜ _n_ 1 _i, . . ., εnJi⟩_ is the _J −_ 1 dimensional vector of error
differences, with the _. . ._ over all alternatives except _i_ ; and _g_ ( _·_ ) is the
density of these error differences. Expressed in this way, the choice
probability is a _J −_ 1 dimensional integral.
The density of the error differences _g_ ( _·_ ), and the density of the
original errors, _f_ ( _·_ ), are related in a particular way. Suppose a model
is specified with an error for each alternative: _εn_ = _⟨εn_ 1 _, . . ., εnJ_ _⟩_
with density _f_ ( _εn_ ). This model is equivalent to a model with _J −_ 1
errors defined as ˜ _εnjk_ = _εnj −_ _εnk_ for any _k_ and density _g_ (˜ _εnk_ ) derived
from _f_ ( _εn_ ). For any _f_ ( _εn_ ), the corresponding _g_ (˜ _εnk_ ) can be derived.
However, since _εn_ has more elements than ˜ _εnk_, there is an infinite
number of densities for the _J_ error terms that give the same density for
the _J −_ 1 error differences. Stated equivalently, any _g_ (˜ _εnk_ ) is consistent
with an infinite number of different _f_ ( _εn_ )’s. Since choice probabilities
can always be expressed as depending only on _g_ (˜ _εnk_ ), one dimension


_2.5. IDENTIFICATION OF CHOICE MODELS_ 29


of the density of _f_ ( _εn_ ) is not identified and must be normalized by the
researcher.
The normalization of _f_ ( _εn_ ) can be handled in various ways. For
some models, such as logit, the distribution of the error terms is sufficiently restrictive that the normalization occurs automatically with
the assumptions on the distribution. For other models, such as probit,
identification is often obtained by specifying the model only in terms
of error differences, that is, by parameterizing _g_ ( _·_ ) without reference to
_f_ ( _·_ ). In all but the simplest models, the researcher needs to consider
the fact that only the density of error differences affects the probabilities and therefore is identified. In discussing the various models in
subsequent chapters, we will return to this issue and how to handle it.


**2.5.2** **The overall scale of utility is irrelevant**


Just as adding a constant to the utility of all alternatives does not
change the decision-maker’s choice, neither does multiplying each alternative’s utility by a constant. The alternative with the highest utility is
the same no matter how utility is scaled. The model _Unj_ [0] [=] _[ V][nj]_ [ +] _[ε][nj][ ∀][j]_
is equivalent to _Unj_ [1] [=] _[ λV][nj]_ [ +] _[ λε][nj][ ∀][j]_ [ for any] _[ λ >]_ [ 0. To account for]
this fact, the researcher must normalize the scale of utility.
The standard way to normalize the scale of utility is to normalize
the variance of the error terms. The scale of utility and the variance of
the error terms are definitionally linked. When utility is multiplied by
_λ_, the variance of each _εnj_ changes by _λ_ [2] : _V ar_ ( _λεnj_ ) = _λ_ [2] _V ar_ ( _εnj_ ).
Therefore normalizing the variance of the error terms is equivalent to
normalizing the scale of utility.


**Normalization with iid errors**


If the error terms are assumed to be independently, identically distributed, then the normalization for scale is straightforward. The researcher normalizes the error variance to some number, which is usually
chosen for convenience. Since all the errors have the same variance by
assumption, normalizing the variance of any of them sets the variance
for them all.
When the observed portion of utility is linear in parameters, the
normalization provides a way of interpreting coefficients. Consider
the model _Unj_ [0] [=] _[ x]_ _nj_ _[′]_ _[β]_ [ +] _[ ε]_ [0] _nj_ [where the variance of the error terms is]
_V ar_ ( _ε_ [0] _nj_ [) =] _[ σ]_ [2][. Suppose the research normalizes the scale by setting]


30 _CHAPTER 2. PROPERTIES_


the error variance to 1. The original model becomes the following
equivalent specification: _Unj_ [1] [=] _[ x]_ _nj_ _[′]_ [(] _[β/σ]_ [) +] _[ ε]_ [1] _nj_ [with] _[ V ar]_ [(] _[ε]_ _nj_ [1] [) = 1.]
The original coefficients _β_ are divided by the standard deviation of
the unobserved portion of utility. The new coefficients _β/σ_ reflect,
therefore, the impact of the observed variables _relative_ to the standard
deviation of the unobserved factors.



The same concepts apply for whatever number the researcher chooses
for normalization. As we will see in the next chapter, the error variances in a standard logit model are traditionally normalized to _π_ [2] _/_ 6,
which is a _√_ bout 1 _._ 6. In this case, the above model becomes _Unj_ =
_x_ _[′]_ _nj_ [(] _[β/σ]_ [)] 1 _._ 6 + _εnj_ with _V ar_ ( _εnj_ ) = 1 _._ 6. The coefficients still reflect



_xnj_ [(] _[β/σ]_ [)] 1 _._ 6 + _εnj_ with _V ar_ ( _εnj_ ) = 1 _._ 6. The coefficients still reflect

the variance of the unobserved portion of utility. The only difference
_√_
is that the coefficients are larger by a factor of 1 _._ 6.


While it is immaterial which number is used by the researcher for
normalization, interpretation of model results must take the normalization into consideration. Suppose, for example, that a logit and an
independent probit model were both estimated on the same data. As
stated above, the error variance is normalized to 1 _._ 6 for logit. Suppose the researcher normalized the probit to have error variances of
1, which is traditional with independent probits. This difference in
normalization must be kept in mind when comparing estimates from
the two models. In particular, the coefficients in the logit model will
_√_
be 1 _._ 6 times larger than those for the probit model, simply due to

the difference in normalization. If the researcher does not take this
scale difference into account when comparing the models, she might
inadvertently think that the logit model implies that people care more
about the attributes (since the coefficients are larger) than implied by
the probit model. For example, in a mode choice model, supposed
the estimated cost coefficient is _−_ 0 _._ 55 from a logit model and _−_ 0 _._ 45
from an independent probit model. It is incorrect to say that the logit
model implies more sensitivity to costs than the probit model. The
coefficients in one of the models must be adjusted to account for the
_√_
difference in scale. The logit coefficients can be divided by 1 _._ 6, so

that the error variance is 1, just like the probit model. With this adjustment, the comparable coefficients are _−_ 0 _._ 43 for the logit model and

_−_ 0 _._ 45 for the probit model. The logit model implies less price sensitivity than the probit. Instead, the probit coefficients could be converted
_√_
to the scale of the logit coefficients by multiplying them by 1 _._ 6, in

which case the comparable coefficients would be _−_ 0 _._ 55 for logit and



1 _._ 6.


_2.5. IDENTIFICATION OF CHOICE MODELS_ 31


_−_ 0 _._ 57 for probit.
A similar issue of interpretation arises when the same model is
estimated on different data sets. The relative scale of the estimates
from the two data sets reflects the relative variance of unobserved
factors in the data sets. Suppose mode choice models were estimated
in Chicago and Boston. For Chicago, the estimated cost coefficient is

_−_ 0 _._ 55 and the estimated coefficient of time is _−_ 1 _._ 78. For Boston, the
estimates are _−_ 0 _._ 81 and _−_ 2 _._ 69. The ratio of the cost coefficient to the
time coefficient is very similar in the two cities: 0 _._ 309 in the Chicago
and 0 _._ 301 in Boston. However, the scale of the coefficients is about fifty
percent higher for Boston than Chicago. This scale difference means
that the unobserved portion of utility has less variance in Boston than
Chicago: since the coefficients are divided by the standard deviation
of the unobserved portion of utility, lower coefficients mean higher
standard deviation and hence variance. The models are revealing that
factors other than time and cost have less effect on people in Boston
than in Chicago. Stated more intuitively, time and cost have more
importance, relative to unobserved factors, in Boston than in Chicago

- which is consistent with the larger scale of the coefficients for Boston.


**Normalization with heteroskedastic errors**


In some situations, the variance of the error terms can be different
for different segments of the population. The researcher cannot set
the overall level of utility by normalizing the variance of the errors
for all segments, since the variance is different in different segments.
Instead, the researcher sets the overall scale of utility by normalizing
the variance for one segment, and then estimates the variance (and
hence scale) for each segment relative to this one segment.
For example, consider the situation described in the previous section, where the unobserved factors have greater variance in Chicago
than in Boston. If separate models are estimated for Chicago and
Boston, then the variance of the error term is normalized separately
for each model. The scale of the parameters in each model reflect the
variance of unincluded factors in that area. Suppose, however, that the
researcher wants to estimate a model on data for both Chicago and
Boston. She cannot normalize the variance of the unobserved factors
for all travelers to the same number, since the variance is different for
travelers in Boston than those in Chicago. Instead, the researcher sets


32 _CHAPTER 2. PROPERTIES_


the overall scale of utility by normalizing the variance in one area (say
Boston) and then estimates the variance in the other area _relative_ that
in the first area (the variance in Chicago relative to that in Boston).
The model in its original form is


_Unj_ = _αTnj_ + _βMnj_ + _ε_ _[B]_ _nj_ _[∀][n]_ [ in Boston]

_Unj_ = _αTnj_ + _βMnj_ + _ε_ _[C]_ _nj_ _[∀][n]_ [ in Chicago] _[,]_


where the variance of _ε_ _[B]_ _nj_ [is not the same as the variance of] _[ ε]_ _nj_ _[C]_ [. Label]
the ratio of variances as _k_ = _V ar_ ( _ε_ _[C]_ _nj_ [)] _[/V ar]_ [(] _[ε][B]_ _nj_ [). We can divide the]
_√_
utility for travelers in Chicago by _k_ ; this division doesn’t affect their

choices, of course, since the scale of utility doesn’t matter. However,
doing so allows us to re-write the model as



_Unj_ = _αTnj_ + _βMnj_ + _εnj ∀n_ in Boston



_√_
_Unj_ = ( _α/_



_√_
_k_ ) _Tnj_ + ( _β/_



_k_ ) _Mnj_ + _εnj ∀n_ in Chicago _,_



where now _√_ the variance of _εnj_ is the same for all _n_ in both cities (since
_V ar_ ( _ε_ _[C]_ _nj_ _[/]_ _k_ ) = (1 _/k_ ) _V ar_ ( _ε_ _[C]_ _nj_ [) = [] _[V ar]_ [(] _[ε][B]_ _nj_ [)] _[/V ar]_ [(] _[ε][C]_ _nj_ [)]] _[V ar]_ [(] _[ε][C]_ _nj_ [) =] _[ V ar]_ [(] _[ε][B]_ _nj_ [).]

The scale of utility is set by normalizing the variance of _εnj_ . The parameter _k_, which is often called the scale parameter, is estimated along
with _β_ and _α_ . The estimated value of _k_ tells the researcher the variance of unobserved factors in Chicago relative to that in Boston. For
example, _k_ [ˆ] = 1 _._ 2 implies that the variance of unobserved factors is
twenty percent greater in Chicago than Boston.
The variance of the error term can differ over geographic regions,
data sets, time, or other factors. In all cases, the researcher sets the
overall scale of utility by normalizing one of the variances and then
estimating the other variances relative to the normalized one. Swait
and Louviere (1993) discuss the role of the scale parameter in discrete
choice models, describing the variety of reasons that variances can differ over observations. As well as the traditional concept of variance in
unobserved factors, psychological factors can come into play, depending on the choice situation and the interpretation of the researcher.
For example, Bradley and Daly (1994) allow the scale parameter to
vary over stated preference experiments in order to account for respondents’ fatigue in answering the survey questions. Ben-Akiva and
Morikawa (1990) allow the scale parameter to differ for respondents’
stated intentions versus their actual market choices.


_2.5. IDENTIFICATION OF CHOICE MODELS_ 33


**Normalization with correlated errors**



In the discussion so far we have assumed that _εnj_ is independent over
alternatives. When the errors are correlated over alternatives, normalizing for scale is more complex. We have talked in terms of setting the
scale of utility. However, since only differences in utility matter, it is
more appropriate to talk in terms of setting the scale of utility _differ-_
_ences_ . However, when errors are correlated, normalizing the variance
of the error for one alternative is not sufficient to set the scale of utility
differences.
The issue is most readily described in terms of a 4-alternative example. The utility for the four alternatives is _Unj_ = _Vnj_ + _εnj, j_ = 1 _, . . .,_ 4.
The error vector _εn_ = _⟨εn_ 1 _, . . ., εn_ 4 _⟩_ has zero mean and covariance matrix:  



_σ_ 11 _σ_ 12 _σ_ 13 _σ_ 14

_·_ _σ_ 22 _σ_ 23 _σ_ 24

_·_ _·_ _σ_ 33 _σ_ 34

_·_ _·_ _·_ _σ_ 44





 (2.3)








Ω=













where the dots refer to the corresponding elements on the upper part
of the symmetric matrix.
Since only differences in utility matter, this model is equivalent to
one in which all utilities are differenced from, say, the first alternative.
The equivalent model is _U_ [˜] _nj_ 1 = _V_ [˜] _nj_ 1 _−_ _ε_ ˜ _nj_ 1 for _j_ = 2 _,_ 3 _,_ 4, where
_U_ ˜ _nj_ 1 = _Unj −_ _Un_ 1, ˜ _Vnj_ 1 = _Vnj −_ _Vn_ 1, and the vector of error differences
is ˜ _εn_ 1 = _⟨_ ( _εn_ 2 _−_ _εn_ 1) _,_ ( _εn_ 3 _−_ _εn_ 1) _,_ ( _εn_ 4 _−_ _εn_ 1) _⟩_ . The variance of each
error difference depends on the variances and covariances of the original
errors. For example, the variance of the difference between the first and
second errors is: _V ar_ (˜ _εn_ 21) = _V ar_ ( _εn_ 2 _−_ _εn_ 1) = _V ar_ ( _εn_ 1)+ _V ar_ ( _εn_ 2) _−_
2 _Cov_ ( _εn_ 1 _, εn_ 2) = _σ_ 11 + _σ_ 22 _−_ 2 _σ_ 12. We can similarly calculate the
covariance between ˜ _εn_ 21, which is the difference between the first and
second errors, and ˜ _εn_ 31, which is the difference between the first and
third errors: _Cov_ (˜ _εn_ 21 _,_ ˜ _εn_ 31) = _E_ ( _εn_ 2 _−_ _εn_ 1)( _εn_ 3 _−_ _εn_ 1) = _E_ ( _εn_ 2 _εn −_
_εn_ 2 _εn_ 1 _−εn_ 3 _εn_ 1 + _εn_ 1 _εn_ 1) = _σ_ 23 _−σ_ 21 _−σ_ 31 + _σ_ 11. The covariance matrix
for the vector of error differences becomes:











 _._



˜Ω1 =



_σ_ 11 + _σ_ 22 _−_ 2 _σ_ 12 _σ_ 11 + _σ_ 23 _−_ _σ_ 12 _−_ _σ_ 13 _σ_ 11 + _σ_ 24 _−_ _σ_ 12 _−_ _σ_ 14

 _·_ _σ_ 11 + _σ_ 33 _−_ 2 _σ_ 13 _σ_ 11 + _σ_ 34 _−_ _σ_ 13 _−_ _σ_ 14

_·_ _·_ _σ_ 11 + _σ_ 44 _−_ 2 _σ_ 14



Setting the variance of one of the original errors is not sufficient to
set the variance of the error differences. For example, if the variance for


34 _CHAPTER 2. PROPERTIES_


the first alternative were set to some number _σ_ 11 = _k_, the variance of
the difference between the errors for the first two alternatives becomes
_k_ + _σ_ 22 _−_ _σ_ 12. An infinite number of values for _σ_ 22 _−_ _σ_ 12 provide
equivalent models.
A common way to set the scale of utility when errors are not iid is
to normalize the variance of one of the error differences to some number. Setting the variance of an error difference sets the scale of utility
differences and hence of utility. Suppose we normalize the variance of
_ε_ ˜ _n_ 21 to 1. The covariance matrix for the error differences, expressed in
terms of the covariances of the original errors, becomes:





1 ( _σ_ 11 + _σ_ 23 _−_ _σ_ 12 _−_ _σ_ 13) _/m_ ( _σ_ 11 + _σ_ 24 _−_ _σ_ 12 _−_ _σ_ 14) _/m_

 _·_ ( _σ_ 11 + _σ_ 33 _−_ 2 _σ_ 13) _/m_ ( _σ_ 11 + _σ_ 34 _−_ _σ_ 13 _−_ _σ_ 14) _/m_

_·_ _·_ ( _σ_ 11 + _σ_ 44 _−_ 2 _σ_ 14) _/m_







 _,_



(2.4)
where _m_ = _σ_ 11 + _σ_ 22 _−_ 2 _σ_ 12. Utility is divided by _[√]_ _σ_ 11 + _σ_ 22 ~~_−_~~ 2 _σ_ 12
to obtain this scaling.
Note that when the error terms are iid, normalizing the variance of
one of these errors automatically normalizes the variance of the error
differences. With iid errors, _σjj_ = _σii_ and _σij_ = 0 for _i ̸_ = _j_ . Therefore,
if _σ_ 11 is normalized to _k_, then the variance of the error difference
becomes _σ_ 11 + _σ_ 22 _−_ 2 _σ_ 12 = _k_ + _k −_ 0 = 2 _k_ . The variance of the error
difference is indeed being normalized, the same as with non-iid errors.
Normalization has implications for the number of parameters that
can be estimated in the covariance matrix. The covariance of the original errors, Ωin equation (2.3), has ten elements in our 4-alternative
example. However, the covariance matrix of the error differences has
six elements, one of which is normalized to set the scale of utility differences. The covariance matrix for error differences with the variance
of the first error difference normalized to _k_ takes the form:







 (2.5)



˜Ω _[∗]_ 1 [=]





_k_ _ωab_ _ωac_

 _·_ _ωbb_ _ωbc_

_·_ _·_ _ωcc_



which has only five parameters. By recognizing the fact that only
differences matter and that the scale of utility is arbitrary, the number
of covariance parameters drops from ten to five. A model with _J_
alternatives has at most _J_ ( _J −_ 1) _/_ 2 _−_ 1 covariance parameters after
normalization.


_2.6. AGGREGATION_ 35


Interpretation of the model is affected by the normalization. Suppose for example that the elements of matrix (2.5) were estimated. The
parameter _ωbb_ is the variance of the difference between the errors for
the first and third alternatives _relative_ to the variance of the difference
between the errors for the first and second alternatives. Complicating
interpretation even further is the fact that the variance of the difference between the errors for two alternatives reflects the variances of
both as well as their covariance.
As we will see, the normalization of logit and nested logit models
is automatic with the distributional assumptions that are placed on
the error terms. Interpretation under these assumptions is relatively
straightforward. For mixed logit and probit, fewer assumptions are
placed on the distribution of error terms such that normalization is
not automatic. The researcher must keep the normalization issues in
mind when specifying and interpreting a model. We return to this topic
when discussing each discrete choice model in subsequent chapters.

# **2.6 Aggregation**


Discrete choice models operate at the level of individual decisionmakers. However, the researcher is usually interested in some aggregate
measure, such as the average probability within a population or the
average response to a change in some factor.
In linear regression models, estimates of aggregate values of the
dependent variable are obtained by inserting aggregate values of the
explanatory variables into the model. For example, suppose _hn_ is housing expenditures of person _n_, _yn_ is the income of the person, and the
model relating them is _hn_ = _α_ + _βyn_ . Since this model is linear, the
average expenditure on housing is simply calculated as _α_ + _βy_ ¯, where ¯ _y_
is average income. Similarly, the average response to a one-unit change
in income is simply _β_, since _β_ is the response for each person.
Discrete choice models are not linear in explanatory variables, and,
consequently, inserting aggregate values of the explanatory variables
into the models will not provide an unbiased estimate of the average probability or average response. The point can be made visually.
Consider Figure 2.1, which gives the probabilities of choosing a particular alternative for two individuals with the observed portion of their
utility (their “representative utility”) being _a_ and _b_ . The average probability is the average of the probabilities for the two people, namely,


36 _CHAPTER 2. PROPERTIES_


( _Pa_ + _Pb_ ) _/_ 2. The average representative utility is ( _a_ + _b_ ) _/_ 2, and the
probability evaluated at this average is the point on the curve above
( _a_ + _b_ ) _/_ 2. As shown for this case, the average probability is greater
than the probability evaluated at the average representative utility. In
general, the probability evaluated at the average representative utility
underestimates the average probability when the individuals’ choice
probabilities are low and overestimates when they are high.


Choice
Probability


_Pb_


average
probability


probability at
average

_Pa_


_a_ _a + b_ _b_ Representative

_2_

Utility


Figure 2.1: Difference between average probability and probability calculated at average representative utility.


Estimating the average response by calculating derivatives and elasticities at the average of the explanatory variables is similarly problematic. Consider Figure 2.2, depicting two individuals with representative
utilities _a_ and _b_ . The derivative of the choice probability for a change
in representative utility is small for both of these people (the slope of
the curve above _a_ and _b_ ). Consequently, the average derivative is also
small. However, the derivative at the average representative utility is
very high (the slope above ( _a_ + _b_ ) _/_ 2.) Estimating average response in
this way can be seriously misleading. In fact, Talvitie (1976) found, in
a mode choice situation, that elasticities at the average representative
utility can be as much as two or three times greater or less than the
average of the individual elasticities.



![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/train_textbook_chunks/markdown/train_textbook_chunk02_p026-050_images/train_textbook_chunk02_p026-050.pdf-20-0.png)
_2.6. AGGREGATION_ 37


Choice
Probability


_a_ _a + b_ _b_ Representative

_2_ Utility


Figure 2.2: Difference between average response and response calculated at average representative utility.


Aggregate outcome variables can be obtained consistently from discrete choice models in two ways, by sample enumeration or segmentation. We discuss each approach below.


**2.6.1** **Sample enumeration**


The most straightforward, and by far the most popular, approach is
sample enumeration, by which the choice probabilities of each decisionmaker in a sample are summed, or averaged, over decision-makers.
Consider a discrete choice model that gives probability _Pni_ that decisionmaker _n_ will choose alternative _i_ from a set of alternatives. Suppose a
sample of _N_ decision-makers, labeled _n_ = 1 _, . . ., N_, is drawn from the
population for which aggregate statistics are required. (This sample
might be the sample on which the model was estimated. However,
it could also be a different sample, collected in a different area or a
later date than the estimation sample.) Each sampled decision-maker
_n_ has some weight associated with him, _wn_, representing the number
of decision-makers similar to him in the population. For samples based
on exogenous factors, this weight is the inverse of the probability that
the decision-maker was selected into the sample. If the sample is purely



![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/train_textbook_chunks/markdown/train_textbook_chunk02_p026-050_images/train_textbook_chunk02_p026-050.pdf-21-0.png)
38 _CHAPTER 2. PROPERTIES_


random, then _wn_ is the same for all _n_ ; and if the sample is stratified
random, then _wn_ is the same for all _n_ within a stratum.
A consistent estimate of the total number of decision-makers in the
population who choose alternative _i_, labeled _N_ [ˆ] _i_, is simply the weighted
sum of the individual probabilities:


      _N_ ˆ _i_ = _wnPni._

_n_


The average probability, which is the estimated market share, is _N_ [ˆ] _i/N_ .
Average derivatives and elasticities are similarly obtained by calculating the derivative and elasticity for each sampled person and taking
the weighted average.


**2.6.2** **Segmentation**


When the number of explanatory variables is small, and those variables
take only a few values, it is possible to estimate aggregate outcomes
without utilizing a sample of decision-makers. Consider, for example,
a model with only two variables entering the representative utility of
each alternative: education level and gender. Suppose the education
variable consists of four categories: did not complete high school, completed high school but did not attend college, attended college but did
not receive a degree, received a college degree. Then the total number
of different types of decision-makers (called ”segments”) is eight: the
four education levels for each of the two genders. Choice probabilities
vary only over these eight segments, not over individuals within each
segment.

If the researcher has data on the number of people in each segment,
then the aggregate outcome variables can be estimated by calculating
the choice probability for each segment and taking the weighted sum
of these probabilities. The number of people estimated to choose alternative _i_ is



_N_ ˆ _i_ =



�8

_wsPsi,_
_s_ =1



where _Psi_ is the probability that a decision-maker in segment _s_ chooses
alternative _i_, and _ws_ is the number of decision-makers in segment _s_ .


_2.7. FORECASTING_ 39

# **2.7 Forecasting**


For forecasting into some future year, the procedures described above
for aggregate variables are applied. However, the exogenous variables
and/or the weights are adjusted to reflect changes that are anticipated
over time. With sample enumeration, the sample is adjusted so that
it _looks like_ a sample that would be drawn in the future year. For
example, to forecast the number of people who will choose a given
alternative five years in the future, a sample drawn from the current
year is adjusted to reflect changes in socioeconomic and other factors
that are expected to occur over the next five years. The sample is adjusted by (i) changing the value of the variables associated with each
sampled decision-maker (e.g., increasing each decision-maker’s income
to represent real income growth over time), and/or (ii) changing the
weight attached to each decision-maker to reflect changes over time
in the number of decision-makers in the population that are similar to
the sampled decision-maker (e.g., increasing the weights for one-person
households and decreasing weights for large households to reflect expected decreases in household size over time.)
For the segmentation approach, changes in explanatory variables
over time are represented by changes in the number of decision-makers
in each segment. The explanatory variables themselves cannot logically
be adjusted since the distinct values of the explanatory variables define
the segments. Changing the variables associated with a decision-maker
in one segment simply shifts the decision-maker to another segment.

# **2.8 Recalibration of constants**


As described in section (2.5.1), alternative-specific constants are often included in a model to capture the average impact of unobserved
factors. In forecasting, it is often useful to adjust these constants, to
reflect the fact that unobserved factors are different for the forecast
area or year compared to the estimation sample. Market share data
from the forecast area can be used to “recalibrate” the constants appropriately. The recalibrated model can then be used to predict changes
in market shares due to changes in explanatory factors.
An iterative process is used to recalibrate the constants. Let _αj_ [0]
be the estimated alternative-specific constant for alternative _j_ . The
superscript 0 is used to indicate that these are the starting values in


40 _CHAPTER 2. PROPERTIES_


the iterative process. Let _Si_ denote the share of decision-makers in the
forecast area that choose alternative _j_ in the “base” year (usually, the
latest year for which such data are available.) Using the discrete choice
model with its original values of _αj_ [0] _[∀]_ _[j]_ [, predict the share of decision-]
makers in the forecast area who will choose each alternative. Label
these predictions _S_ [ˆ] _j_ [0] _[∀]_ _[j]_ [. Compare the predicted shares with the actual]
shares. If the actual share for an alternative exceeds the predicted
share, raise the constant for that alternative. Lower the constant if
the actual share is below the predicted. An effective adjustment is:


_αj_ [1] [=] _[ α]_ _j_ [0] [+] _[ ln]_ [(] _[S][j][/]_ [ ˆ] _[S]_ _j_ [0][)] _[.]_


With the new constants, predict the share again, compare with the
actual shares, and if needed adjust the constants again. The process
is repeated until the forecasted shares are sufficiently close to the actual shares. The model with these recalibrated constants is then used
to predict changes from base-year shares due to changes in observed
factors that affect decision-makers’ choices.


