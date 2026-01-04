_10.5. SIMULATION-BASED ESTIMATORS_ 291



This is the same asymptotic distribution as ML. When _R_ rises faster
_√_
than _N_, MSL is consistent, asymptotically normal and efficient,

asymptotically equivalent to ML.
_√_
Suppose that _R_ rises with _N_ but at a rate that is slower than _N_ .

_√_
In this case, the ratio _N_ _/R_ grows larger as _N_ rises. There is no limit
_√_ _√_
ing distribution for _N_ ( _θ_ [ˆ] _−_ _θ_ _[∗]_ ) because the bias term, ( _N/R_ ) _Z_ rises



_√_
_N_ ( _θ_ [ˆ] _−_ _θ_ _[∗]_ ) because the bias term, (



ing distribution for _N_ ( _θ_ [ˆ] _−_ _θ_ ) because the bias term, ( _N/R_ ) _Z_ rises

with _N_ . However, the estimator itself converges on the true value. _θ_ [ˆ]
_√_
depends on (1 _/R_ ) _Z_, not multiplied by _N_ . This bias term disappears

when _R_ rises at any rate. Therefore, the estimator converges on the
true value, just like its non-simulated counterpart, which means that
_θ_ ˆ is consistent. However, the estimator is not asymptotically normal
_√_
since _N_ ( _θ_ [ˆ] _−_ _θ_ _[∗]_ ) has no limiting distribution. Standard errors cannot



since _N_ ( _θ_ [ˆ] _−_ _θ_ _[∗]_ ) has no limiting distribution. Standard errors cannot

be calculated, and confidence intervals cannot be constructed.
_√_
When _R_ is fixed, the bias rises as _N_ rises. _N_ ( _θ_ [ˆ] _−θ_ _[∗]_ ) does not have



When _R_ is fixed, the bias rises as _N_ rises. _N_ ( _θ_ [ˆ] _−θ_ _[∗]_ ) does not have

a limiting distribution. Moreover, the estimator itself, _θ_ [ˆ], contains bias
_B_ = (1 _/R_ ) _Z_ that does not disappear as sample size rises with fixed
_R_ . The MSL estimator is neither consistent nor asymptotically normal
when _R_ is fixed.
The properties of MSL can be summarized as follows:



1. If _R_ is fixed, MSL is inconsistent.

_√_
2. If _R_ rises slower than _N_, MSL is consistent but not asymptot
ically normal.



_√_
3. If _R_ rises faster than _N_, MSL is consistent, asymptotically

normal and efficient, equivalent to ML.


**10.5.2** **Method of simulated moments**

For MSM with fixed instruments, ˇ _gn_ ( _θ_ ) = [�] _j_ [[] _[d][nj][ −]_ _[P]_ [ˇ] _[nj]_ [(] _[θ]_ [)]] _[z][nj]_ [, which]
is unbiased for _gn_ ( _θ_ ) since the simulated probability enters linearly.
The bias term is zero. The distribution of the estimator is determined
only by term _A_, which is the same as in the traditional MOM without
simulation, and term _C_, which reflects simulation noise:
_√_ _[√]_



_N_ ( _θ_ [ˆ] _−_ _θ_ _[∗]_ ) = _−D_ [ˇ] _[−]_ [1] _[√]_



_N_ ( _A_ + _C_ ) _._



Suppose that _R_ is fixed. Since _D_ [ˇ] converges to its expectation **D**, we
have _−√N_ _D_ [ˇ] _[−]_ [1] _A_ _→_ _[d]_ _N_ (0 _,_ **D** _[−]_ [1] **WD** _[−]_ [1] ) and _−√N_ _D_ [ˇ] _[−]_ [1] _C_ _→d_ _N_ (0 _,_ **D** _−_ 1( **S**



_√_
_N_ _D_ [ˇ] _[−]_ [1] _A_ _→_ _[d]_ _N_ (0 _,_ **D** _[−]_ [1] **WD** _[−]_ [1] ) and _−_



have _−_ _N_ _D_ [ˇ] _[−]_ [1] _A_ _→_ _[d]_ _N_ (0 _,_ **D** _[−]_ [1] **WD** _[−]_ [1] ) and _−_ _N_ _D_ [ˇ] _[−]_ [1] _C_ _→d_ _N_ (0 _,_ **D** _−_ 1( **S** _/R_ ) **D** _−_ 1),

such that
_√_



_N_ ( _θ_ [ˆ] _−_ _θ_ _[∗]_ ) _→_ _[d]_ _N_ (0 _,_ **D** _[−]_ [1] [ **W** + **S** _/R_ ] **D** _[−]_ [1] ) _._


292 _CHAPTER 10. SIMULATION-ASSISTED ESTIMATION_


The asymptotic distribution of the estimator is then


_θ_ ˆ _∼_ _[a]_ _N_ ( _θ_ _[∗]_ _,_ **D** _[−]_ [1] [ **W** + **S** _/R_ ] **D** _[−]_ [1] _/N_ ) _._


The estimator is consistent and asymptotically normal. Its variance is
greater than its non-simulated counterpart by **D** _[−]_ [1] **SD** _[−]_ [1] _/RN_, reflecting simulation noise.
Suppose now that _R_ rises with _N_ at any rate. The extra variance
due to simulation noise disappears, such that _θ_ [ˆ] _∼_ _[a]_ _N_ ( _θ_ _[∗]_ _,_ **D** _[−]_ [1] **WD** _[−]_ [1] _/N_ ),
the same as its non-simulated counterpart. When non-ideal instruments are used, **D** _[−]_ [1] **WD** _[−]_ [1] = _−_ **H** _[−]_ [1] and so the estimator (in either
its simulated or non-simulated form) is less efficient than ML.
If simulated instruments are used in MSM, then the properties
of the estimator depend on how the instruments are simulated. If the
instruments are simulated without bias and independently of the probability that enters the residual, then this MSM has the same properties
as MSM with fixed weights. If the instruments are simulated with bias
and the instruments are not ideal, then the estimator has the same
properties as MSL except that it is not asymptotically efficient since
the information identity does not apply. MSM with simulated ideal
instruments is MSS, which we discuss next.


**10.5.3** **Method of simulated scores**


With MSS using unbiased score simulators, ˇ _gn_ ( _θ_ ) is unbiased for _gn_ ( _θ_ ),
and, moreover, _gn_ ( _θ_ ) is the score such that the information identity applies. The analysis is the same as for MSM except that the information
identity makes the estimator efficient when _R_ rises with _N_ . As with
MSM, we have


_θ_ ˆ _∼_ _[a]_ _N_ ( _θ_ _[∗]_ _,_ **D** _[−]_ [1] [ **W** + **S** _/R_ ] **D** _[−]_ [1] _/N_ )


which, since _gn_ ( _θ_ ) is the score, becomes


_θ_ ˆ _∼_ _[a]_ _N_ ( _θ_ _[∗]_ _,_ **H** _[−]_ [1] [ **V** + **S** _/R_ ] **H** _[−]_ [1] _/N_ ) = _N_ ( _θ_ _[∗]_ _, −_ **H** _[−]_ [1] _/N_ + **H** _[−]_ [1] **SH** _[−]_ [1] _/RN_ )


When _R_ is fixed, the estimator is consistent and asymptotically normal,
but its covariance is larger than with ML because of simulation noise.
If _R_ rises at any rate with _N_, then we have


_θ_ ˆ _∼_ _[a]_ _N_ (0 _, −_ **H** _[−]_ [1] _/N_ ) _._


_10.6. NUMERICAL SOLUTION_ 293



MSS with unbiased score simulators is asymptotically equivalent to
ML when _R_ rises at any rate with _N_ .
This analysis shows that MSS with unbiased score simulators has
better properties than MSL in two regards. First, for fixed _R_, MSS is
consistent and asymptotically normal while MSL is neither. Second,
for _R_ rising with _N_, MSS is equivalent to ML no matter how fast _R_
is rising, while MSL is equivalent to ML only if the rate is faster than
_√_

_N_ .
As we discussed in section (10.2.3), finding unbiased score simulators with good numerical properties is difficult. MSS is sometimes
applied with biased score simulators. In this case, the properties of
the estimator are the same as MSL: the bias in the simulated scores
translates into bias in the estimator which disappears from the limiting
_√_
distribution only if _R_ rises faster than _N_ .

### **10.6 Numerical Solution**


The estimators are defined as the value of _θ_ that solves ˇ _g_ ( _θ_ ) = 0,
where ˇ _g_ ( _θ_ ) = [�] _n_ _[g]_ [ˇ] _[n]_ [(] _[θ]_ [)] _[/N]_ [ is the sample average of a simulated statistic]
_g_ ˇ _n_ ( _θ_ ). Since ˇ _gn_ ( _θ_ ) is a vector, we need to solve the set of equations for
the parameters. The question arises: how are these equations solved
numerically to obtain the estimates?
Chapter 8 describes numerical methods for maximizing a function.
These procedures can also be used for solving a set of equations. Let _T_
be the negative of the inner product of the defining term for an estimator: _T_ = _−g_ ˇ( _θ_ ) _[′]_ _g_ ˇ( _θ_ ) = _−_ ( [�] _n_ _[g]_ [ˇ] _[n]_ [(] _[θ]_ [))] _[′]_ [(][�] _n_ _[g]_ [ˇ] _[n]_ [(] _[θ]_ [))] _[/N]_ [2][.] _[ T]_ [ is necessarily]
less than or equal to zero, since T is the negative of a sum of squares.
_T_ has a highest value of 0, which is attained only when the squared
terms that compose it are all 0. That is, the maximum of _T_ is attained
when ˇ _g_ ( _θ_ ) = 0. Maximizing _T_ is equivalent to solving the equation
_g_ ˇ( _θ_ ) = 0. The approaches described in Chapter 8, with the exception
of BHHH, can be used for this maximization. BHHH cannot be used
because that method assumes that the function being maximized is a
sum of observation-specific terms, whereas _T_ takes the square of each
sum of observation-specific terms. The other approaches, especially
BFGS and DFP, have proven very effective at locating the parameters
at which ˇ _g_ ( _θ_ ) = 0.
With MSL, it is usually easier to maximize the simulated likelihood
function rather than _T_ . BHHH can be used in this case, as well as the


294 _CHAPTER 10. SIMULATION-ASSISTED ESTIMATION_


other methods.


## **Chapter 11**

# **Individual-Level** **Parameters**

### **11.1 Introduction**

Mixed logit and probit models allow random coefficients whose distribution in the population is estimated. Consider, for example, the
model in Chapter 6, of angler’s choice among fishing sites. The sites are
differentiated on the basis of whether campgrounds are available at the
site. Some anglers like having campgrounds at the fishing sites since
they can use the grounds for overnight stays. Other anglers dislike
the crowds and noise that are associated with campgrounds and prefer
fishing at more isolated spots. To capture these differences in tastes, a
mixed logit model was specified that included random coefficients for
the campground variable and other site attributes. The distribution
of coefficients in the population was estimated. Figure 11.1 gives the
estimated distribution of the campground coefficient. The distribution
was specified to be normal. The mean was estimated as 0.116, and the
standard deviation was estimated as 1.655. This distribution provides
useful information about the population. For example, the estimates
imply that 47 percent of the population dislike having campgrounds
at their fishing sites, while the other 53 percent like having them.
The question arises: where in the distribution of tastes does a
particular angler lie? Is there a way to determine whether a given
person tends to like or dislike having campgrounds at fishing sites?
A person’s choices reflect their own tastes. Stated in reverse, a person’s choices reveal something about their tastes, which the researcher


295


296 _CHAPTER 11. INDIVIDUAL-LEVEL PARAMETERS_



![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/train_textbook_chunks/markdown/train_textbook_chunk13_p301-325_images/train_textbook_chunk13_p301-325.pdf-5-0.png)



= 0.116


Figure 11.1: Distribution of coefficient of campgrounds in population
of all anglers.


can, in principle, discover. If the researcher observes that a particular
angler consistently chooses sites without campgrounds, even when the
cost of driving to these sites is higher, then the researcher can reasonably infer that this angler dislikes campgrounds. There is a precise
way for performing this type of inference, given by Revelt and Train
(2000).
We explain the procedure in the context of a mixed logit model;
however, any behavioral model that incorporates random coefficients
can be used, including probit. The central concept is a distinction
between two distributions: the distribution of tastes in the population,
and the distribution of tastes in the subpopulation of people who make
particular choices. Denote the random coefficients as vector _β_ . The
distribution of _β_ in the population of all people is denoted _g_ ( _β | θ_ )
where _θ_ is the parameters of this distribution, such as the mean and
variance.
A choice situation consists of several alternatives described collectively by variables _x_ . Consider the following thought experiment.
Suppose everyone in the population faced the same choice situation described by the same variables _x_ . Some portion of the population will
choose each alternative. Consider the people who choose alternative _i_ .
The tastes of these people are not all the same: there is a distribution
of coefficients among these people. Let _h_ ( _β | i, x, θ_ ) denote the distribution of _β_ in the subpopulation of people who, when faced with the


_11.1. INTRODUCTION_ 297


choice situation described by variables _x_, would choose alternative _i_ .
_g_ ( _β | θ_ ) is the distribution of _β_ in the entire population. _h_ ( _β |_
_i, x, θ_ ) is the distribution of _β_ in the subpopulation of people who
would choose alternative _i_ when facing a choice situation described by
_x_ .
We can generalize the notation to allow for repeated choices. Let _y_
denote a sequence of choices in a series of situations described collectively by variables _x_ . The distribution of coefficients in the subpopulation of people who would make the sequences of choices _y_ when facing
situations described by _x_ is denoted _h_ ( _β | y, x, θ_ ).
Note that _h_ ( _·_ ) conditions on _y_, while _g_ ( _·_ ) does not. It is sometimes
useful to call _h_ the conditional distribution and _g_ the unconditional
distribution. Two such distributions are depicted in Figure 11.2. If we
knew nothing about a person’s past choices, then the best we could do
in describing the person’s tastes is to say that the person’s coefficients
lie somewhere in _g_ ( _β | θ_ ). However, if we have observed that the person
made choices _y_ when facing situations described by _x_, then we know
that that person’s coefficients are in distribution _h_ ( _β | y, x, θ_ ). Since _h_
is tighter than _g_, we have better information about the person’s tastes
by conditioning on their past choices.



![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/train_textbook_chunks/markdown/train_textbook_chunk13_p301-325_images/train_textbook_chunk13_p301-325.pdf-6-0.png)





0


Figure 11.2: Unconditional (population) distribution _g_ and condition
(subpopulation) distribution _h_ for subpopulation of anglers who chose
sites without campgrounds.


Inference of this form has long been conducted with linear regres

298 _CHAPTER 11. INDIVIDUAL-LEVEL PARAMETERS_


sion models, where the dependent variable and the distribution of coefficients are both continuous (Griffiths, 1972; Judge, Hill, Griffiths,
Lutkepohl and Lee, 1988). Regime-switching models, particularly in
macroeconomics, have used an analogous procedure to assess the probability that an observation is within a given regime (Hamilton and Susmel, 1994; Hamilton, 1996). In these models, the dependent variable is
continuous and the distribution of coefficients is discrete (representing
one set of coefficients for each regime.) In contrast to both of these
traditions, our models have discrete dependent variables. DeSarbo,
Ramaswamy and Cohen (1995) developed an approach in the context
of a discrete choice model with a discrete distribution of coefficients
(that is, a latent class model). They used maximum likelihood procedures to estimate the coefficients for each segment, and then calculated
the probability that an observation is within each segment based on
the observed choices of the observation. The approach that we describe
here applies to discrete choice models with continuous or discrete distributions of coefficients and uses maximum likelihood (or other classical
methods) for estimation. The model of DeSarbo et al. (1995) is a special case of this more general method. Bayesian procedures have been
also developed to perform this inference within discrete choice models
(Rossi, McCulloch and Allenby, 1996; Allenby and Rossi, 1999). We
describe the Bayesian methods in Chapter 12.

### **11.2 Derivation of conditional distribution**


The relation between _h_ and _g_ can be established precisely. Consider a
choice among alternatives _j_ = 1 _, . . ., J_ in choice situations _t_ = 1 _, . . ., T_ .
The utility that person _n_ obtains from alternative _j_ in situation _t_ is


_Unjt_ = _βn_ _[′]_ _[x][njt]_ [+] _[ ε][njt]_


where _εnjt ∼_ iid extreme value, and _βn ∼_ _g_ ( _β | θ_ ) in the population.
The variables _xnjt_ can be denoted collectively for all alternatives and
choice situations as _xn_ . Let _yn_ = _⟨yn_ 1 _, . . ., ynT ⟩_ denote the person’s
sequence of chosen alternatives. If we knew _βn_, then the probability
of the person’s sequence of choices would be a product of logits:



_P_ ( _yn | xn, β_ ) =




- _T_

_Lnt_ ( _ynt | β_ )
_t_ =1


_11.2. DERIVATION OF CONDITIONAL DISTRIBUTION_ 299



where



_Lnt_ ( _ynt | β_ ) = ~~�~~ _[e][β][′][x][nyntt]_ _[.]_

_j_ _[e][β]_ ~~_[′]_~~ _[x][njt]_



Since we do not know _βn_, the probability of the person’s sequence of
choices is the integral of _P_ ( _yn | xn, β_ ) over the distribution of _β_ :

             _P_ ( _yn | xn, θ_ ) = _P_ ( _yn | xn, β_ ) _g_ ( _β | θ_ ) _dβ._ (11.1)


This is the mixed logit probability that we discussed in Chapter 6.
We can now derive _h_ ( _β | yn, xn, θ_ ). By Bayes’ rule,


_h_ ( _β | yn, xn, θ_ ) _× P_ ( _yn | xn, θ_ ) = _P_ ( _yn | xn, β_ ) _× g_ ( _β | θ_ ) _._


This equation simply states that the joint density of _β_ and _yn_ can be
expressed as the probability of _yn_ times the probability of _β_ conditional
on _yn_ (which is the left hand side), or with the other direction of conditioning, as the probability of _β_ times the probability of _yn_ conditional
on _β_ (which is the right hand side.) Rearranging:


_h_ ( _β | yn, xn, θ_ ) = _[P]_ [(] _[y][n][ |][ x][n][, β]_ [)] _[g]_ [(] _[β][ |][ θ]_ [)] _._ (11.2)

_P_ ( _yn | xn, θ_ )


We know all the terms on the right hand side. From these, we can
calculate _h_ .
Equation (11.2) also provides a way to interpret _h_ intuitively. Note
that the denominator _P_ ( _yn | xn, θ_ ) is the integral of the numerator,
as given by the definition in (11.1). As such, the denominator is a
constant that makes _h_ integrate to 1, as required for any density. Since
the denominator is a constant, _h_ is proportional to the numerator,
_P_ ( _yn | xn, β_ ) _g_ ( _β | yn, xn, θ_ ). This relation makes interpretation of _h_
relatively easy. Stated in words: the density of _β_ in the subpopulation
of people who would choose sequence _yn_ when facing _xn_ is proportional
to the density of _β_ in the entire population _times_ the probability that
_yn_ would be chosen if the person’s coefficients were _β_ .
Using (11.2), various statistics can be derived conditional on _yn_ .
The mean _β_ in the subpopulation of people who would choose _yn_ when
facing _xn_ is

           _β_ ¯ _n_ = _β · h_ ( _β | yn, xn, θ_ ) _dβ._


300 _CHAPTER 11. INDIVIDUAL-LEVEL PARAMETERS_


This mean generally differs from the mean _β_ in the entire population.
Substituting the formula for _h_,



_β_ ¯ _n_ =


=




_β · P_ ( _yn | xn, β_ ) _g_ ( _β | θ_ ) _dβ_

_P_ ( _yn | xn, θ_ )

_β · P_ ( _yn | xn, β_ ) _g_ ( _β | θ_ ) _dβ_

~~�~~ (11.3)
_P_ ( _yn | xn, β_ ) _g_ ( _β | θ_ ) _dβ_



The integrals in this equation do not have a closed form; however,
they can be readily simulated. Take draws of _β_ from the population
density _g_ ( _β | θ_ ). Calculate the weighted average of these draws, with
the weight for draw _β_ _[r]_ being proportional to _P_ ( _yn | xn, β_ _[r]_ ). The
simulated subpopulation mean is



where the weights are




  _β_ ˇ _n_ = _w_ _[r]_ _β_ _[r]_

_r_


_P_ ( _yn | xn, β_ _[r]_ )
_w_ _[r]_ = ~~�~~ (11.4)
_r_ _[P]_ [(] _[y][n][ |][ x][n][, β][r]_ [)] _[.]_



Other statistics can also be calculated. Suppose the person faces
a new choice situation described by variables _xnjT_ +1 _∀j_ . If we had
no information on the person’s past choices, then we would assign the
following probability to his choosing alternative _i_ :

              _P_ ( _i | xnT_ +1 _, θ_ ) = _LnT_ +1( _i | β_ ) _g_ ( _β | θ_ ) _dβ_ (11.5)



where



_e_ _[β][′][x][niT]_ [ +1]
_LnT_ +1( _i | β_ ) = ~~�~~

_[.]_
_j_ _[e][β]_ ~~_[′]_~~ _[x][njT]_ [ +1]



This is just the mixed logit probability using the population distribution of _β_ . If we observed the past choices of the person, then the
probability can be conditioned on these choices. The probability becomes:

            _P_ ( _i | xnT_ +1 _, yn, xn, θ_ ) = _LnT_ +1( _i | β_ ) _h_ ( _β | yn, xn, θ_ ) _dβ._ (11.6)


This is also a mixed logit probability, but using the conditional distribution _h_ instead of the unconditional distribution _g_ . When we do


_11.3. IMPLICATIONS OF ESTIMATION OF θ_ 301


not know the person’s previous choices, we mix the logit formula over
density of _β_ in the entire population. However, when we know the
person’s previous choices, we can improve our prediction by mixing
over the density of _β_ in the subpopulation who would have made the
same choices as this person.
To calculate this probability, we substitute the formula for _h_ from
(11.2):



_P_ ( _i | xnT_ +1 _, yn, xn, θ_ ) =




_LnT_ +1( _i | β_ ) _P_ ( _yn | xn, β_ ) _g_ ( _β | θ_ ) _dβ_

~~�~~ _._
_P_ ( _yn | xn, β_ ) _g_ ( _β | θ_ ) _dβ_



The probability is simulated by taking draws of _β_ from the population
distribution _g_, calculating the logit formula for each draw, and taking
a weighted average of the results:

      _P_ ˇ _niT_ +1( _yn, xn, θ_ ) = _w_ _[r]_ _LnT_ +1( _i | β_ _[r]_ )

_r_


where the weights are given by (11.4).

### 11.3 Implications of estimation of θ


The population parameters _θ_ are estimated in any of the ways described in Chapter 10. The most common approach is maximum simulated likelihood, with the simulated value of _P_ ( _yn | xn, θ_ ) entering the
log-likelihood function. An estimate of _θ_, labeled _θ_ [ˆ], is obtained. We
know that there is sampling variance in the estimator. The asymptotic
covariance of the estimator is also estimated, which we label _W_ [ˆ] . The
asymptotic distribution is therefore estimated to be _N_ ( _θ,_ [ˆ] _W_ [ˆ] ).
The parameter _θ_ describes the distribution of _β_ in the population,
giving, for example, the mean and variance of _β_ over all decisionmakers. For any value of _θ_, equation (11.2) gives the conditional distribution of _β_ in the subpopulation of people who would make choices
_yn_ when faced with situations described by _xn_ . This relation is exact in the sense that there is no sampling or other variance associated
with it. Similarly, any statistic based on _h_ is exact given a value of _θ_ .
For example, the mean of the conditional distribution, _β_ [¯] _n_, is exactly
equation (11.3) for a given value of _θ_ .
Given this correspondence between _θ_ and _h_, the fact that _θ_ is estimated can be handled in two different ways. The first approach is
to use the point estimate of _θ_ to calculate statistics associated with


302 _CHAPTER 11. INDIVIDUAL-LEVEL PARAMETERS_


the conditional distribution _h_ . Under this approach, the mean of the
condition distribution, _β_ [¯] _n_, is calculated by inserting _θ_ [ˆ] into (11.3). The
probability in a new choice situation is calculated by inserting _θ_ [ˆ] into
(11.6). If the estimator of _θ_ is consistent, then this approach is consistent for statistics based on _θ_ .
The second approach is to take the sampling distribution of _θ_ [ˆ] into
consideration. Each possible value of _θ_ implies a value of _h_, and hence
a value of any statistic associated with _h_, such as _β_ [¯] _n_ . The sampling
variance in the estimator of _θ_ induces sampling variance in the statistics
that are calculated on the basis of _θ_ . This sampling variance can be
calculated through simulation, by taking draws of _θ_ from its estimated
sampling distribution and calculating the corresponding statistic for
each of these draws.
For example, to represent the sampling distribution of _θ_ [ˆ] in the
calculation of _β_ [¯] _n_, the following steps are taken.


1. Take a draw from _N_ ( _θ,_ [ˆ] _W_ [ˆ] ), which is the estimated sampling
distribution of _θ_ [ˆ] . This step is accomplished as follows. Take
_K_ draws from a standard normal density and label the vector
of these draws _η_ _[r]_, where _K_ is the length of _θ_ . Then create
_θ_ _[r]_ = _θ_ [ˆ] + _Lη_ _[r]_, where _L_ is the Choleski factor of _W_ [ˆ] .


2. Calculate _β_ [¯] _n_ _[r]_ [based on this] _[ θ][r]_ [. Since the formula for ¯] _[β][n]_ [involves]
integration, we simulate it using formula (11.3).


3. Repeat steps 1 and 2 many times, with the number of times
labeled _R_ .


The resulting values are draws from the sampling distribution of _β_ [¯] _n_
induced by the sampling distribution of _θ_ [ˆ] . The average of _β_ [¯] _n_ _[r]_ [over the]
_R_ draws of _θ_ _[r]_ is the mean of the sampling distribution of _β_ [¯] _n_ . The
standard deviation of the draws gives the asymptotic standard error
of _β_ [¯] _n_ that is induced by the sampling variance of _θ_ [ˆ] .
Note that this process involves simulation within simulation. For
each draw of _θ_ _[r]_, the statistic _β_ [¯] _n_ _[r]_ [is simulated with multiple draws of] _[ β]_
from the population density _g_ ( _β | θ_ _[r]_ ).
Suppose either of these approaches is used to estimate _β_ [¯] _n_ . The
question arises: can the estimate of _β_ [¯] _n_ be considered an estimate of
_βn_ ? That is: is the estimated mean of the conditional distribution
_h_ ( _β | yn, xn, θ_ ), which is conditioned on person _n_ ’s past choices, an
estimate of person _n_ ’s coefficients?


_11.3. IMPLICATIONS OF ESTIMATION OF θ_ 303


There are two possible answers, depending on how the researcher
views the data generation process. If the number of choice situations
that the researcher can observe for each decision-maker is fixed, then
the estimate of _β_ [¯] _n_ is not a consistent estimate of _βn_ . When _T_ is fixed,
consistency requires that the estimate converge to the true value when
sample size rises without bound. If sample size rises, but the choice
situations faced by person _n_ is fixed, then the conditional distribution
and its mean does not change. Insofar as person _n_ ’s coefficients do
not happen to coincide with the mean of the conditional distribution
(a essentially impossible event), the mean of the conditional distribution will never equal the person’s coefficients no matter how large the
sample is. Raising sample size improves the estimate of _θ_ and hence
provides a better estimate of the mean of the conditional distribution,
since this mean depends only on _θ_ . However, raising sample size does
not make the conditional mean equal to the person’s coefficients.

When the number of choice situations is fixed, then the conditional
mean has the same interpretation as the population mean, but for a
different, and less diverse, group of people. When predicting the future
behavior of the person, one can expect to obtain better predictions
using the conditional distribution, as in (11.6), than the population
distribution. In the case study presented below, we show that the
improvement can be large.

If the number of choice situations that a person faces can be considered to rise, then the estimate of _β_ [¯] _n_ can be considered to be an
estimate of _βn_ . Let _T_ be the number of choice situations that person _n_
faces. If we observe more choices by the person (i.e., _T_ rises), then we
are better able to identify the person’s coefficients. Figure 11.3 gives
the conditional distribution _h_ ( _β | yn, xn, θ_ ) for three different values
of _T_ . The conditional distribution tends to move toward the person’s
own _βn_ as _T_ rises, and to become more concentrated. As _T_ rises without bound, the conditional distribution collapses onto _βn_ . The mean
of the conditional distribution converges to the true value of _βn_ as the
number of choice situations rises without bound. The estimate of _β_ [¯] _n_
is therefore consistent for _βn_ .
In Chapter 12, we describe the Bernstein-von Mises theorem. This
theorem states that, under fairly mild conditions, the mean of a posterior distribution for a parameter is asymptotically equivalent to the
maximum of the likelihood function. The conditional distribution _h_
is a posterior distribution: by (11.2) _h_ is proportional to a density _g_,


304 _CHAPTER 11. INDIVIDUAL-LEVEL PARAMETERS_


_g_ with ten
observed choices



![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/train_textbook_chunks/markdown/train_textbook_chunk13_p301-325_images/train_textbook_chunk13_p301-325.pdf-13-0.png)



Figure 11.3: Conditional distribution with _T_ = 0, 1, and 10.


which can be interpreted as a prior distribution on _βn_, _times_ the likelihood of person _n_ ’s _T_ choices given _βn_, which is _P_ ( _yn | xn, βn_ ). By the
Bernstein-von Mises theorem, the mean of _h_ is therefore an estimator
of _βn_ that is asymptotically equivalent to the maximum likelihood estimator of _βn_, where the asymptotics are defined as _T_ rising. These
concepts are described more fully in Chapter 12; we mention them now
simply to provide another interpretation of the mean of the conditional
distribution.

### **11.4 Monte Carlo illustration**


To illustrate the concepts, I constructed a hypothetical data set where
the true population parameters _θ_ are known as well as the true _βn_ for
each decision-maker. These data allow us to compare the mean of the
conditional distribution for each decision-maker’s choices, _β_ [¯] _n_, with the
_βn_ for that decision-maker. It also allows us to investigate the impact
of increasing the number of choice situations on the conditional distribution. For this experiment, I constructed data sets consisting of 300
“customers” each facing _T_ =1, 10, 20, and 50 choice situations. There
are three alternatives and four variables in each data set. The coeffi

_11.4. MONTE CARLO ILLUSTRATION_ 305


cients for the first two variables are held fixed for the entire population
at 1.0, and the coefficients for the last two variables are distributed
normal with a mean and variance of 1.0. Utility is specified to include
these variables plus a final iid term that is distributed extreme value,
such that the model is a mixed logit. The dependent variable for each
customer was created by taking a draw from the density of the random
terms, calculating the utility of each alternative with this draw, and
determining which alternative had the highest utility. To minimize
the effect of simulation noise in the creation of the data, I constructed
50 datasets for each level of _T_ . The results that are reported are the
average over these 50 datasets.

The mean of the conditional distribution for each customer, _β_ [¯] _n_,
was calculated. The standard deviation of _β_ [¯] _n_ over the 300 customers
was calculated, as well as the average absolute deviation of _β_ [¯] _n_ from
the customer’s _βn_ (i.e., the average over _n_ of _|_ _β_ [¯] _n −_ _βn |_ ). Table
11.1 presents these statistics. Consider first the standard deviation. If
there were no observed choice situations on which to condition ( _T_ =
0), then the conditional distribution for each customer would be the
unconditional (population) distribution. Each customer would have
the same _β_ [¯] _n_ equal to the population mean of _β_ . In this case, the
standard deviation of _β_ [¯] _n_ would be zero, since all customers have the
same _β_ [¯] _n_ . At the other extreme, if we observed an unboundedly large
number of choice situations ( _T →∞_ ), then the conditional distribution
for each customer would collapse to their own _βn_ . In this case, the
standard deviation of _β_ [¯] _n_ would equal the standard deviation of the
population distribution of _βn_, which is 1 in this experiment. For _T_
between 0 and _∞_, the standard deviation of _β_ [¯] _n_ is between 0 and the
standard deviation of _βn_ in the population.


In Table 11.1, we see that conditioning on only a few choice situations captures a large share of the variation in _β_ ’s over customers.
With only one choice situation, the standard deviation of _β_ [¯] _n_ is over
.4. Since the standard deviation of _βn_ in the population is 1 in this
experiment, this result means that conditioning on one choice situation
captures over 40 percent of the variation in _βn_ . With 10 choices situations, over 80 percent of the variation is captured. There are strongly
decreasing return to observing more choice situations. Doubling from
_T_ = 10 to _T_ = 20 only increases the percent of variation captured from
about .83 to about .89. Increasing _T_ to 50 raises the percent to about
.95.


306 _CHAPTER 11. INDIVIDUAL-LEVEL PARAMETERS_


Table 11.1: Monte Carlo Illustration

1st coef. 2nd coef.
1 choice situation
Standard deviation of _β_ [¯] _n_ 0.413 0.416
Absolute difference between _β_ [¯] _n_ and _βn_ 0.726 0.718
10 choice situation
Standard deviation of _β_ [¯] _n_ 0.826 0.826
Absolute difference between _β_ [¯] _n_ and _βn_ 0.422 0.448
20 choice situation
Standard deviation of _β_ [¯] _n_ 0.894 0.886
Absolute difference between _β_ [¯] _n_ and _βn_ 0.354 0.350
50 choice situation
Standard deviation of _β_ [¯] _n_ 0.951 0.953
Absolute diference between _β_ [¯] _n_ and _βn_ 0.243 0.243


Consider now the absolute difference between the mean of the customer’s conditional distribution, _β_ [¯] _n_, and the customer’s actual _βn_ .
With no conditioning ( _T_ = 0), the average absolute difference would
be 0.8, which is the expected absolute difference for deviates that follow
a standard normal as we have in our experiment. With perfect conditioning ( _T →∞_ ), _β_ [¯] _n_ = _βn_ for each customer, and so the absolute
difference is 0. With only one choice situation, the average absolute
deviation drops from 0.8 (without conditioning) to about 0.72, for a
10 percent improvement. The absolute deviation drops further as the
number of choice situations rises.


Notice that the drop in the absolute deviation is smaller than the
increase in the standard deviation. For example, with one choice situation the absolute deviation moves 10 percent of the way from no
conditioning to perfect knowledge (from .80 with _T_ = 0 to .72 with
_T_ = 1, which is 10 percent of the way to 0 with _T →∞_ ). Yet the
standard deviation moves about 40 percent of the way from no conditioning to perfect knowledge (.4 with _T_ = 1 is 40 percent of the
distance from 0 with _T_ = 0 to 1 with _T →∞_ ). This difference is due
to the fact that the standard deviation incorporates movement of _β_ [¯] _n_
away from _βn_ as well as movement towards _βn_ . This fact is important
to recognize when evaluating the standard deviation of _β_ [¯] _n_ in empirical applications, where the absolute difference cannot be calculated
since _βn_ is not known. That is, the standard deviation of _β_ [¯] _n_ expressed


_11.5. AVERAGE CONDITIONAL DISTRIBUTION_ 307


as a percent of the estimated standard deviation in the population,
is an overestimate of the amount of information that is contained in
the _β_ [¯] _n_ ’s. With ten choice situations, the average standard deviation
in _β_ [¯] _n_ is over 80 percent of the value that it would have with perfect
knowledge, and yet the absolute deviation is less than half as high as
would be attained without conditioning.

### **11.5 Average conditional distribution**


For a correctly specified model at the true population parameters, the
conditional distribution of tastes, aggregated over all customers, equals
the population distribution of tastes. Given a series of choice situations
described by _xn_, there is a set of possible sequences of choices. Label
these possible sequences as _ys_ for _s_ = 1 _, . . ., S_ . Denote the true frequency of _ys_ as _m_ ( _ys | xn, θ_ _[∗]_ ), which depends on the true parameters
_θ_ _[∗]_ . If the model is correctly specified and consistently estimated, then
_P_ ( _ys | xn,_ _θ_ [ˆ] ) approaches _m_ ( _ys | xn, θ_ _[∗]_ ) asymptotically. Conditional on
the explanatory variables, the expected value of _h_ ( _β | ys, xn,_ _θ_ [ˆ] ) is then:




    _Eyh_ ( _β | y, xn,_ _θ_ [ˆ] ) =



_s_




 _→_



_P_ ( _ys | xn, β_ ) _g_ ( _β | xn,_ _θ_ [ˆ] )

_m_ ( _yn | xn, θ_ _[∗]_ )
_P_ ( _ys | xn,_ _θ_ [ˆ] )



_P_ ( _ys | xn, β_ ) _g_ ( _β | xn,_ _θ_ [ˆ] )
_s_



= _g_ ( _β | xn,_ _θ_ [ˆ] ) _._


This relation provides a diagnostic tool (Allenby and Rossi, 1999). If
the average of the sampled customers’ conditional taste distributions
is similar to the estimated population distribution, the model is correctly specified and accurately estimated. If they are not similar, the
difference could be due to: (1) specification error, (2) an insufficient
number of draws in simulation, (3) an inadequate sample size, and/or
(4) the maximum likelihood routine converging at a local rather than
global maximum.

### **11.6 Case study: choice of energy supplier**


**Population distribution**


We obtained stated-preference data on residential customers’ choice
of electricity supplier. Surveyed customers were presented with 8-12


308 _CHAPTER 11. INDIVIDUAL-LEVEL PARAMETERS_


hypothetical choice situations called experiments. In each experiment,
the customer was presented with four alternative suppliers with different prices and other characteristics. The suppliers differed on the
basis of price (fixed price at a given cents per kWh, time-of-day prices
with stated prices in each time period, or seasonal prices with stated
prices in each time period), the length of the contract (during which
the supplier is required to provide service at the stated price and the
customer would need to pay a penalty for leaving the supplier), and
whether the supplier was their local utility, a well-known company
other than their local utility, or an unfamiliar company. The data
were collected by Research Triangle Institute (1997) for the Electric
Power Research Institute and have been used by Goett (1998) to estimate mixed logits. We utilize a specification similar to Goett’s, but
we eliminate or combine variables that he found to be insignificant.
Two mixed logit models were estimated on these data, based on
different specifications for the distribution of the random coefficients.
All choices except the last situation for each customer are used to estimate the parameters of the population distribution, and the customer’s
last choice situation was retained for use in comparing the predictive
ability of different models and methods.
Table 11.2 gives the estimated population parameters. The price
coefficient in both models is fixed across the population such that the
distribution of willingness to pay for each non-price attribute (which
is the ratio of the attribute’s coefficient to the price coefficient) has
the same distribution as the attribute’s coefficient. For model 1, all
of the non-price coefficients are specified to be normally distributed in
the population. The mean _m_ and standard deviation _s_ of each coefficient are estimated. For model 2, the first three non-price coefficients
are specified to be normal, and the fourth and fifth are log-normal.
The fourth and fifth variable are indicators of time-of-day and seasonal rates, and their coefficients must logically be negative for all
customers. The log-normal distribution (with the signs of the variable
reversed) provides for this necessity. The log of these coefficients is
distributed normal with mean _m_ and standard deviation _s_, which are
the parameters that are estimated. The coefficients themselves have
mean _exp_ ( _m_ +( _s_ [2] _/_ 2)) and standard deviation equal to the mean times


( _exp_ ( _s_ ~~[2]~~ ) _−_ 1).
The estimates provide the following qualitative results:


_•_ The average customer is willing to pay about a fifth to a quarter


_11.6. CASE STUDY_ 309


Table 11.2: Mixed logit model of energy supplier choice


Standard errors in parentheses.
TOD rates: 11c/kWh 8am-8pm, 5c/kWh 8pm-8am
Seasonal rates: 10c/kWh summer, 8c/kWh winter, 6c/kWh spring-fall



![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/train_textbook_chunks/markdown/train_textbook_chunk13_p301-325_images/train_textbook_chunk13_p301-325.pdf-18-0.png)
310 _CHAPTER 11. INDIVIDUAL-LEVEL PARAMETERS_


cent per kWh in higher price, depending on the model, in order
to have a contract that is shorter by one year. Stated conversely,
a supplier that requires customers to sign a four to five-year
contract must discount its price by one cent per kWh to attract
the average customer.


_•_ There is considerable variation in customers’ attitudes towards
contract length, with a sizeable share of customers preferring a
longer contract to a shorter contract. A long-term contract constitutes insurance for the customer against price increases with
the supplier being locked into the stated price for the length of
the contract. Such contracts prevent the customer from taking advantage of lower prices that might arise during the term
of the contract. Apparently, many customers value the insurance against higher prices more than they mind losing the option to take advantage of potentially lower prices. The degree
of customer heterogeneity implies that the market can sustain
contracts of different lengths with suppliers making profits by
writing contracts that appeal to different segments of the population.


_•_ The average customer is willing to pay a whopping 2.5 cents per
kWh more for its local supplier than for an unknown supplier.
Only a small share of customers prefer an unknown supplier to
their local utility. This finding has important implications for
competition. It implies that entry in the residential market by
previously unknown suppliers will be very difficult, particularly
since the price discounts that entrants can potentially offer in
most markets are fairly small. The experience in California,
where only 1 percent of residential customers have switched away
from their local utility after several years of open access, is consistent with this finding.


_•_ The average customer is willing to pay 1.8 cents per kWh for a
known supplier relative to an unknown one. The estimated values
of _s_ imply that a sizeable share of customers would be willing to
pay more for a known supplier than for their local utility, presumably because of a bad experience or a negative attitude toward
the local energy utility. These results imply that companies that
are known to customers, such as their long distance carriers, lo

_11.6. CASE STUDY_ 311


cal telecommunications carriers, local cable companies, and even
retailers like Sears and Home Depot, may be successful in attracting customers for electricity supply relative to companies
that were unknown prior to their entry as an energy supplier.


_•_ The average customer evaluates the TOD rates in a way that is
fairly consistent with time-of-day usage patterns. In model 1, the
mean coefficient of the dummy variable for the TOD rates implies
that the average customer considers these rates to be equivalent
to a fixed price of 9.7 cents per kWh. In model 2, the estimated
mean and standard deviation of the log of the coefficient imply a
median willingness to pay of 8.4 cents and a mean of 10.4 cents,
which span the mean from model 1. 9.5 cents is the average price
that a customer would pay under the TOD rates if 75 percent
of its consumption occurred during the day (between 8AM and
8PM) and the other 25 percent occurred at night. These shares,
while perhaps slightly high for the day, are not unreasonable.
The estimated values of s are highly significant, reflecting heterogeneity in usage patterns and perhaps in customers’ ability
to shift consumption in response to TOD prices. These values
are larger than reasonable implying that a non-negligible share
of customers treat the TOD prices as being equivalent to a fixed
price that is higher than the highest TOD price or lower than
the lowest TOD price.


_•_ The average customer seems to avoid seasonal rates for reasons
beyond the prices themselves. The average customers treats the
seasonal rates as being equivalent to a fixed ten cents per kWh,
which is the highest seasonal price. A possible explanation for
this result relates to the seasonal variation in customers’ bills.
In many areas, electricity consumption is highest in the summer,
when air-conditioners are being run, and energy bills are therefore higher in the summer than in other seasons, even under fixed
rates. The variation in bills over months without commensurate
variation in income makes it more difficult for customers to pay
for their summer bills. In fact, nonpayment for most energy utilities is most frequent in the summer. Seasonal rates, which apply
the highest price in the summer, increase the seasonal variation
in bills. Customers would rationally avoid a rate plan that exacerbates an already existing difficulty. If this interpretation is cor

312 _CHAPTER 11. INDIVIDUAL-LEVEL PARAMETERS_


rect, then seasonal rates combined with bill-smoothing (by which
the supplier carries a portion of the summer bills over to the winter) could provide an attractive arrangement for customers and
suppliers alike.


Model 2 attains the a higher log-likelihood value than model 1,
presumably because the lognormal distribution assures negative coefficients for the TOD and seasonal variables.


**Conditional distributions**


We now use the estimated models to calculate customers’ conditional
distributions and the means of these distributions. We calculate _β_ [¯] _n_ for
each customer in two ways. First, we calculate _β_ [¯] _n_ using equation (11.3)
with the point estimates of the population parameters, _θ_ [ˆ] . Second,
we use the procedure in section (11.3) to integrate over the sampling
distribution of the estimated population parameters.
The means and standard deviations of _β_ [¯] _n_ over the sampled customers calculated by these two methods are given in Tables 11.3 and
11.4, respectively. The price coefficient is not listed in Table 11.3 since
it is fixed across the population. Table 11.4 incorporates the sampling
distribution of the population parameters, which includes variance in
the price coefficient.
Consider the results in Table 11.3 first. The mean of _β_ [¯] _n_ is very
close to the estimated population mean given in Table 11.2. This similarity as expected for a correctly specified and consistently estimated
model. The standard deviation of _β_ [¯] _n_ would be zero if there were no
conditioning and would equal the population standard deviation if each
customer’s coefficient were known exactly. The standard deviations in
Table 11.3 are considerably above zero and are fairly close to the estimated population standard deviations in Table 11.2. For example, in
model 1, the conditional mean of the coefficient of contract length has
a standard deviation of 0.318 over customers, and the point estimate
of the standard deviation in the population is 0.379. Thus, variation
in _β_ [¯] _n_ captures more than 70 percent of the total estimated variation in
this coefficient. Similar results are obtained for other coefficients. This
result implies that the mean of a customer’s conditional distribution
captures a fairly large share of the variation in coefficients across customers and has the potential to be useful in distinguishing customers.


_11.6. CASE STUDY_ 313


Table 11.3: Average _β_ [¯] _n_ using point estimate _θ_ [ˆ]

Model 1 Model 2
Contract length
Mean -0.2028 -0.2149
Std dev 0.3175 0.3262
Local utility
Mean 2.1205 2.2146
Std dev 1.2472 1.3836
Known company
Mean 1.5360 1.5997
Std dev 0.6676 0.6818
TOD rate
Mean -8.3194 -9.2584
Std dev 2.2725 3.1051
Seasonal rate
Mean -8.6394 -9.1344
Std dev 1.7072 2.0560


As discussed in section (11.5), a diagnostic check on the specification and estimation of the model is obtained by comparing the sample
average of the conditional distributions with the estimated population
distribution. The means in Table 11.3 represent the means of the sample average of the conditional distributions. The standard deviation
of the sample-average conditional distribution depends on the standard deviation of _β_ [¯] _n_ which is given in Table 11.3, plus the standard
deviation of _βn −_ _β_ [¯] _n_ . When this latter portion is added, the standard
deviation of each coefficient matches very closely the estimated population standard deviation. This equivalence suggests that there is not
significant specification error and that the estimated population parameters are fairly accurate. This suggestion is somewhat tempered,
however, by the results in Table 11.4.


Table 11.4 gives the sample mean and standard deviation of the
mean of the sampling distribution of _β_ [¯] _n_ that is induced by the sampling distribution of _θ_ [ˆ] . The means in Table 11.4 represent the means
of the sample average of _h_ ( _β | yn, xn,_ _θ_ [ˆ] ) integrated over the sampling
distribution of _θ_ [ˆ] . For model 1, a discrepancy occurs that indicates
possible misspecification. In particular, the means of the TOD and
seasonal rates coefficients in Table 11.4 exceed their estimated popula

314 _CHAPTER 11. INDIVIDUAL-LEVEL PARAMETERS_


Table 11.4: Average _β_ [¯] _n_ with sampling dist. of _θ_ [ˆ]

Model 1 Model 2
Price
Mean -0.8753 -0.8836
Std dev 0.5461 0.0922
Contract length
Mean -0.2004 -0.2111
Std dev 0.3655 0.3720
Local utility
Mean 2.1121 2.1921
Std dev 1.5312 1.6815
Known company
Mean 1.5413 1.5832
Std dev 0.9364 0.9527
TOD rate
Mean -9.1615 -9.0216
Std dev 2.4309 3.8785
Seasonal rate
Mean -9.4528 -8.9408
Std dev 1.9222 2.5615


_11.6. CASE STUDY_ 315


Table 11.5: Condition means for three customers

Population Customer 1 Customer 2 Customer 3
Contract length -0.213 0.198 -0.208 -0.401
Local utility 2.23 2.91 2.17 0.677
Known company 1.59 1.79 2.15 1.24
TOD rates -9.19 -5.59 -8.92 -12.8
Seasonal rates -9.02 -5.86 -11.1 -10.9


tion means in Table 11.2. Interestingly, the means for these coefficients
in Table 11.4 for model 1 are closer to the analogous means for model
2 than to the estimated population means for model 1 in Table 11.2.
Model 2 has the more reasonably shaped lognormal distribution for
these coefficients and obtains a considerably better fit than model 1.
The conditioning in model 1 appears to be moving the coefficients
closer to the values in the better-specified model 2 and away from its
own misspecified population distributions. This is an example of how a
comparison of the estimated population distribution with the sample
average of the conditional distribution can reveal information about
specification and estimation.

The standard deviations in Table 11.4 are larger than those in Table
11.3. This difference is due to the fact that the sampling variance in
the estimated population parameters is included in the calculations for
Table 11.4 but not for Table 11.3. The larger standard deviations do
not mean that the portion of total variance in _βn_ that is captured by
variation in _β_ [¯] _n_ is larger when the sampling distribution is considered
than when not.
Useful marketing information can be obtained by examining the _β_ [¯] _n_
of each customer. The value of this information for targeted marketing has been emphasized by Rossi et al. (1996). Table 11.5 gives the
calculated _β_ [¯] _n_ for the first three customers in the data set, along with
the population mean of _βn_ .

The first customer wants to enter a long-term contract, compared
with the vast majority of customers who dislike long-term contracts.
He is willing to pay a higher energy price if the price is guaranteed
through a long-term contract. He evaluates TOD and seasonal rates
very generously, as if all of his consumption were in the lowest-priced
period (note that the lowest price under TOD rates is 5 cents per kWh
and the lowest price under seasonal rates is 6 cents per kWh.) That


