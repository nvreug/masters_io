_12.6. HIERARCHICAL BAYES FOR MIXED LOGIT_ 341


used for results A and B above. More flexible priors can be specified for
_W_, using the procedures of, for example, McCulloch and Rossi (2000),
though doing so makes the Gibbs sampling more complex.
A sample of _N_ people is observed. The chosen alternatives in
all time periods for person _n_ are denoted _yn_ _[′]_ [=] _[ ⟨][y][n]_ [1] _[, . . ., y][nT]_ _[⟩]_ [, and]
the choices of the entire sample are labeled _Y_ = _⟨y_ 1 _, . . ., yN_ _⟩_ . The
probability of person _n_ ’s observed choices, conditional on _β_, is








  _L_ ( _yn | β_ ) =

_t_




_e_ _[β][′][x][nyntt]_

~~�~~
_j_ _[e][β]_ ~~_[′]_~~ _[x][njt]_



_._



The probability _not_ conditional on _β_ is the integral of _L_ ( _yn | β_ ) over
all _β_ :

             _L_ ( _yn | b, W_ ) = _L_ ( _yn | β_ ) _φ_ ( _β | b, W_ ) _dβ_


where _φ_ ( _β | b, W_ ) is the normal density with mean _b_ and variance _W_ .
This _L_ ( _yn | b, W_ ) is the mixed logit probability.
The posterior distribution of _b_ and _W_ is, by definition


      _K_ ( _b, W | Y_ ) _∝_ _L_ ( _yn | b, W_ ) _k_ ( _b, W_ ) (12.4)

_n_


where _k_ ( _b, W_ ) is the prior on _b_ and _W_ described above (i.e., normal
for _b_ times inverted Wishart for _W_ ).
It would be _possible_ to draw directly from _K_ ( _b, W | Y_ ) with the
M-H algorithm. However, doing so would be computationally very
slow. For each iteration of the M-H algorithm, it would be necessary to calculate the right hand side of (12.4). However, the choice
probability _L_ ( _yn | b, W_ ) is an integral without a closed for and must
be approximated through simulation. Each iteration of the M-H algorithm would therefore require simulation of _L_ ( _yn | b, W_ ) for each _n_ . As
well as being very time consuming, the properties of the resulting estimator would be affected by this simulation within the M-H algorithm.
Recall that the properties of the simulated mean of the posterior were
derived under the assumption that draws can be taken from the posterior without needing to simulate the choice probabilities. M-H applied
to (12.3) violates this assumption.
Drawing from _K_ ( _b, W | Y_ ) becomes fast and simple if each _βn_ is
considered to be a parameter along with _b_ and _W_, and Gibbs sampling
is used for the three sets of parameters _b_, _W_, and _βn ∀n_ . The posterior


342 _CHAPTER 12. BAYESIAN PROCEDURES_


for _b, W,_ and _βn ∀n_ is:

      _K_ ( _b, W, βn ∀n | Y_ ) _∝_ _L_ ( _yn | βn_ ) _φ_ ( _βn | b, W_ ) _k_ ( _b, W_ )

_n_


Draws from this posterior are obtained through Gibbs sampling. A
draw of each parameter is taken, conditional on the other parameters:
(1) Take a draw of _b_ conditional on values of _W_ and _βn ∀n_ . (2) Take
a draw of _W_ conditional on values of _b_ and _βn ∀n_ . (3) Take a draw of
_βn∀n_ conditional on values of _b_ and _W_ . Each of these steps is easy, as
we will see. Step 1 uses result A, which gives the posterior of the mean
given the variance. Step 2 uses result B, which gives the posterior of
the variance given the mean. Step 3 uses a M-H algorithm, but in a
way that does not involve simulation within the algorithm. Each step
is described below.


1. _b | W, βn ∀n._ We condition on _W_ and each person’s _βn_ in this
step, which means that we treat these parameters as if they were
known. Result A gives us the posterior distribution of _b_ under
these conditions. The _βn_ ’s constitute a sample of _N_ realizations
from a normal distribution with unknown mean _b_ and known
variance _W_ . Given our diffuse prior on _b_, the posterior on _b_ is
_N_ ( _β, W/N_ [¯] ), where _β_ [¯] is the sample mean of the _βn_ ’s. A draw
from this posterior is obtained as described in section (12.5.1).


2. _W | b, βn ∀n._ Result B gives us the posterior for _W_ conditional
on _b_ and the _βn_ ’s. The _βn_ ’s constitute a sample from a normal
distribution with known mean _b_ and unknown variance _W_ . Under our prior on _W_, the posterior on _W_ is inverted Wishart with
_K_ where + _N S_ degrees of freedom and scale matrix (1 = (1 _/N_ ) [�] _n_ [(] _[β][n][ −]_ _[b]_ [)(] _[β][n][ −]_ _[b]_ [)] _[′]_ [ is the sample variance of] _KI_ + _NS_ 1) _/_ ( _K_ + _N_ )
the _βn_ ’s around the known mean _b_ . A draw from the inverted
Wishart is obtained as described in section (12.5.2).


3. _βn | b, W._ The posterior for each person’s _βn_, conditional on their
choices and the population mean and variance of _βn_ is


_K_ ( _βb | b, W, yn_ ) _∝_ _L_ ( _yn | βn_ ) _φ_ ( _βn | b, W_ ) (12.5)


There is no simple way to draw from this posterior, and so the
M-H algorithm is used. Note that the right hand side of (12.5)
is easy to calculate: _L_ ( _yn | βn_ ) is a product of logits and _φ_ ( _βn |_


_12.6. HIERARCHICAL BAYES FOR MIXED LOGIT_ 343


_b, W_ ) is the normal density. The M-H algorithm operates as
follows:


(a) Start with a value _βn_ [0][.]


(b) Draw _K_ independent values from a standard normal density
and stack the draws into a vector labeled _η_ [1] .

(c) Create a trial value of _βn_ [1] [as ˜] _[β]_ _n_ [1] [=] _[ β]_ _n_ [0] [+] _[ ρLη]_ [1][, where] _[ ρ]_ [ is]
a scalar specified by the researcher and _L_ is the Choleski
factor of _W_ . Note that the proposal distribution (which is
labeled _g_ ( _·_ ) in section (9.2.9)) is specified to be normal with
zero mean and variance _ρ_ [2] _W_ .

(d) Draw a standard uniform variable _µ_ [1] .


(e) Calculate the ratio


_[β]_ [˜] _n_ [1][)] _[φ]_ [(] _[β]_ [˜] _n_ [1] _[|][ b, W]_ [)]
_F_ = _[L]_ [(] _[y][n][ |]_
_L_ ( _yn | βn_ [0] ) _φ_ ( _βn_ [0] _| b, W_ )


(f) If _µ_ [1] _≤_ _F_, accept _β_ [˜] _n_ [1] [and let] _[ β]_ _n_ [1] [= ˜] _[β]_ _n_ [1][. If] _[ µ]_ [1] _[ > F]_ [, reject ˜] _[β]_ _n_ [1]
and let _βn_ [1] [=] _[ β]_ _n_ [0][.]

(g) Repeat the process many times. For high enough _t_, _βn_ _[t]_ [is a]
draw from the posterior.


We now know how to draw from the posterior for each parameter
conditional on the other parameters. We combine the procedures into a
Gibbs sampler for the three sets of parameters. Start with any initial
values _b_ [0] _, W_ [0] _,_ and _βn_ [0] _[∀][n]_ [.] The _t_ -th iteration of the Gibbs sampler
consists of these steps:


1. Draw _b_ _[t]_ from _N_ ( _β_ [¯] _[t][−]_ [1] _, W_ _[t][−]_ [1] _/N_ ) where _β_ [¯] _[t][−]_ [1] is the mean of the
_βn_ _[t][−]_ [1] ’s.


2. Draw _Wt_ from _IW_ ( _K_ + _N,_ ( _KI_ + _NS_ _[t][−]_ [1] ) _/_ ( _K_ + _N_ )) where _S_ _[t][−]_ [1] =

  _n_ [(] _[β]_ _n_ _[t][−]_ [1] _−_ _b_ _[t]_ )( _βn_ _[t][−]_ [1] _−_ _b_ _[t]_ ) _[′]_ )) _/N_ .


3. For each _n_, draw _βn_ _[t]_ [using one iteration of the M-H algorithm]
described above, starting from _βn_ _[t][−]_ [1] and using the normal density
_φ_ ( _βn | b_ _[t]_ _, W_ _[t]_ ).


These three steps are repeated for many iterations. The resulting
values converge to draws from the joint posterior of _b, W,_ and _βn∀n_ .


344 _CHAPTER 12. BAYESIAN PROCEDURES_


Once the converged draws from the posterior are obtained, the mean
and standard deviation of the draws can be calculated to obtain estimates and standard errors of the parameters. Note that this procedure
provides information about _βn_ for each _n_, similar to the procedure described in Chapter 11 using classical estimation.

As stated, the Gibbs sampler converges, with enough iterations, to
draws from the joint posterior of all the parameters. The iterations
prior to convergence are often called “burn-in”. Unfortunately, it is
not always easy to determine when convergence has been achieved,
as emphasized by Kass et al. (1998). Cowles and Carlin (1996) provide a description of the various tests and diagnostics that have been
proposed. For example, Gelman and Rubin (1992) suggest starting
the Gibbs sampler from several different points and testing the hypothesis that the statistic of interest (in our case, the posterior mean)
is the same when calculated from each of the presumably converged
sequences. Sometimes convergence is fairly obvious such that formal
testing is unnecessary. During burn-in, the researcher will usually be
able to see the draws trending, that is, moving toward the mass of
the posterior. After convergence has been achieved, the draws tend to
move around (“traverse”) the posterior.

The draws from Gibbs sampling are correlated over iterations even
after convergence has been achieved, since each iteration builds on
the previous one. This correlation does not prevent the draws from
being used for calculating the posterior mean and standard deviation,
or other statistics. However, the researcher can reduce the amount
of correlation among the draws by using only a portion of the draws
that are obtained after convergence. For example, the researcher might
retain every tenth draw and discard the others, thereby reducing the
correlation among the retained draws by an order of 10. A researcher
might therefore specify a total of 20,000 iterations in order to obtain
1000 draws: 10,000 for burn-in and 10,000 after convergence of which
every tenth is retained.

One issue remains. In the M-H algorithm, the scalar _ρ_ is specified by the researcher. This scalar determines the size of each jump.
Usually, smaller jumps translate into more accepts and larger jumps
result in fewer accepts. However, smaller jumps means that the M-H
algorithm takes more iterations to converge and embodies more serial correlation in the draws after convergence. Gelman et al. (1995,
p. 335) have examined the optimal acceptance rate in the M-H algo

_12.6. HIERARCHICAL BAYES FOR MIXED LOGIT_ 345


rithm. They found that the optimal rate is about 0.44 when _K_ = 1
and drops toward .23 as _K_ rises. The value of _ρ_ can be set by the
researcher to achieve an acceptance rate in this neighborhood, lowering _ρ_ to obtain a higher acceptance rate and raising it to get a lower
acceptance rate.
In fact, _ρ_ can be adjusted within the iterative process. The researcher sets the initial value of _ρ_ . In each iteration, a trial _βn_ is
accepted or rejected for each sampled _n_ . If in an iteration, the acceptance rate among the _N_ observations is above a given value (say, .33),
then _ρ_ is raised. If the acceptance rate is below this value, _ρ_ is lowered.
The value of _ρ_ then moves during the iteration process to attain the
specified acceptance level.


**12.6.1** **Succinct restatement**


Now that the Bayesian procedures have been fully described, the model
and the Gibbs sampling can be stated succinctly, in the form that is
used in most publications. The model is:


Utility:

_Unjt_ = _βn_ _[′]_ _[x][njt]_ [+] _[ ε][njt]_
_εnjt_ iid extreme value

_βn_ _∼_ _N_ ( _b, W_ )


Observed choice:

_ynt_ = _i_ if and only if _Unit > Unjt ∀j ̸_ = _i_

Priors:


_k_ ( _b, W_ ) = _k_ ( _b_ ) _k_ ( _W_ )


where


_k_ ( _b_ ) is _N_ ( _b_ 0 _, S_ 0) with extremely large variance


_k_ ( _W_ ) is _IW_ ( _K, I_ )


The conditional posteriors are:




    _K_ ( _βn | b, W, yn_ ) _∝_



_e_ _[β]_ _n_ _[′]_ _[x][ny]_ _nt_ _[t]_

~~�~~ _[φ]_ [(] _[β][n][ |][ b, W]_ [)] _∀n_
_j_ _[e][β][n]_ ~~_[′]_~~ _[x][njt]_



_t_




        _K_ ( _b | W, βn ∀n_ ) is _N_ ( _β, W/N_ [¯] )) _,_ where _β_ [¯] =



_βn/N_
_n_



_K_ ( _W | b, βn ∀n_ ) is _IW_ ( _K_ + _N,_ ( _KI_ + _N_ _S_ [¯] ) _/_ ( _K_ + _N_ )) _,_


346 _CHAPTER 12. BAYESIAN PROCEDURES_


       where _S_ [¯] = ( _βn −_ _b_ )( _βn −_ _b_ ) _[′]_ _/N_

_n_


The three conditional posteriors are called “layers” of the Gibbs
sampling. The first layer for each _n_ depends only on data for that
person, rather than for the entire sample. The second and third layers
do not depend on the data directly, only on the draws of _βn_ which
themselves depend on the data.
The Gibbs sampling for this model is fast for two reasons. First,
none of the layers requires integration. In particular, the first layer utilizes a product of logit formulas for a given value of _βn_ . The Bayesian
procedure avoids the need to calculate the mixed logit probability, utilizing instead the simple logits conditional _βn_ . Second, layers 2 and 3
do not utilize the data at all, since they depend only on the draws of
_βn ∀n_ . Only the mean and variance of the _βn_ ’s need be calculated in
these layers.
The procedure is often called “hierarchical Bayes” (HB) because
there is a hierarchy of parameters. _βn_ is the “individual-level parameters” for person _n_, which describe the tastes of that person. The _βn_ ’s
are distributed in the population with mean _b_ and variance _W_ . The
parameters _b_ and _W_ are often called the “population-level parameters”
or “hyper-parameters”. There is also a hierarchy of priors. The prior
on each person’s _βn_ is the density of _βn_ in the population. This prior
has parameters (hyper-parameters), namely its mean _b_ and variance
_W_, which themselves have priors.

## **12.7 Case Study: Choice of energy supplier**


We apply the Bayesian procedures to the data that were described
in Chapter 11 regarding customers’ choice among energy suppliers.
The Bayesian estimates are compared with estimates obtained through
maximum simulated likelihood (MSL).
Each of 361 customers was presented with up to 12 hypothetical
choice situations. In each choice situation, four energy suppliers were
described and the respondent was asked which one he would choose if
facing the choice in the real world. The suppliers were differentiated on
the basis of six factors: (1) whether the supplier charged fixed prices,
and if so the rate in cents per kilowatt-hour (kWh), (2) the length
of contract in years, during which the rates were guaranteed and the
customer would be required a penalty to switch to another supplier,


_12.7. CASE STUDY: CHOICE OF ENERGY SUPPLIER_ 347


(3) whether the supplier was the local utility, (4) whether the supplier
was a well-known company other than the local utility, (5) whether the
supplier charged time-of-day (TOD) rates at specified prices in each
period, and (6) whether the supplier charged seasonal rates at specified
prices in each season. In the experimental design, the fixed rates varied
over situations, but the same prices were specified in all experiments
whenever a supplier was said to charge TOD or seasonal rates. The
coefficient of the dummies for TOD and seasonal rates therefore reflect
the value of these rates at the specified prices. The coefficient of the
fixed price indicates the value of each cent per kWh.


**12.7.1** **Independent normal coefficients**


A mixed logit model was estimated under the initial assumption that
the coefficients are independently normally distributed in the population. That is, _βn ∼_ _N_ ( _b, W_ ) with diagonal _W_ . The population
parameters are the mean and standard deviation of each coefficient.
Table 12.1 gives the simulated mean of the posterior (SMP) for these
parameters, along with the MSL estimates. For the Bayesian procedure, 20,000 iterations of the Gibbs sampling were performed. The
first 10,000 iterations were considered burn-in, and every tenth draw
was retained after convergence, for a total of 1000 draws from the posterior. The mean and standard deviation of these draws constitutes the
estimates and standard errors. For MSL, the mixed logit probability
was simulated with 200 Halton draws for each observation.
The two procedures provide similar results in this application. The
scale of the estimates from the Bayesian procedure is somewhat larger
than that for MSL. This difference indicates that the posterior is
skewed, with the mean exceeding the mode. When the MSL estimates
are scaled to have the same estimated mean for the price coefficient,
the two sets of estimates are remarkably close, in standard errors as
well as point estimates. Run time was essentially the same for each
approach.
In other applications, e.g., Ainslie et al. (2001), the MSL and SMP
estimates have differed. In general, the magnitude of differences depends on the number of observations relative to the number of parameters, as well as the amount of variation that is contained in the
observations. When the two sets of estimates differ, it means that
the asymptotics are not yet operating completely (i.e., sample size is


348 _CHAPTER 12. BAYESIAN PROCEDURES_


Table 12.1: Mixed Logit Model of Choice Among Energy Suppliers


|Estimates<br>(se’s in parens.)|MSL|SMP|Scaled MSL|
|---|---|---|---|
|Price coef:<br>mean<br>st dev|-0.976<br>(.0370)<br>.230<br>(.0195)|-1.04<br>(.0374)<br>.253<br>(.0169)|-1.04<br>(.0396)<br>.246<br>(.0209)|
|Contract coef:<br>mean<br>st dev|-0.194<br>(.0224)<br>.405<br>(.0238)|-0.240<br>(.0269)<br>.426<br>(.0245)|-0.208<br>(.0240)<br>.434<br>(.0255)|
|Local coef:<br>mean<br>st dev|2.24<br>(.118)<br>1.72<br>(.122)|2.41<br>(.140)<br>1.93<br>(.123)|2.40<br>(.127)<br>1.85<br>(.131)|
|Well-known coef:<br>mean<br>st dev|1.62<br>(.0865)<br>1.05<br>(.0849)|1.71<br>(.100)<br>1.28<br>(.0940)|1.74<br>(.0927)<br>1.12<br>(.0910)|
|TOD coef:<br>mean<br>st dev|-9.28<br>(.314)<br>2.00<br>(.147)|-10.0<br>(.315)<br>2.51<br>(.193)|-9.94<br>(.337)<br>2.14<br>(.157)|
|Seasonal coef:<br>mean<br>st dev|-9.50<br>(.312)<br>1.24<br>(.188)|-10.2<br>(.310)<br>1.66<br>(.182)|-10.2<br>(.333)<br>1.33<br>(.201)|


_12.7. CASE STUDY: CHOICE OF ENERGY SUPPLIER_ 349


insufficient for the asymptotic properties to be fully exhibited). The
researcher might want to apply a Bayesian perspective in this case (if
she is not already doing so) in order to utilize the Bayesian approach
to small sample inference. The posterior distribution contains the relevant information for Bayesian analysis with any sample size, whereas
the classical perspective requires the researcher to rely on asymptotic
formulas for the sampling distribution that need not be meaningful
with small samples. Allenby and Rossi (1999) provide examples of the
differences and the value of the Bayesian approaches and perspective.
We re-estimated the model under a variety of other distributional
assumptions. In the following sections, we describe how each method is
implemented under these alternative assumptions. For reasons that are
inherent to the methodologies, the Bayesian procedures are easier and
faster for some types of specifications, while the classical procedures are
easier and faster for other specifications. Understanding these realms of
relative convenience can assist the researcher in deciding which method
to use for a particular model.


**12.7.2** **Multivariate normal coefficients**


We now allow the coefficients to be correlated. That is, _W_ is full
rather than diagonal. The classical procedure is the same except that
drawing from _φ_ ( _βn | b, W_ ) for the simulation of the mixed logit probability requires creating correlation among independent draws from
a random number generator. The model is parameterized in terms
of the Choleski factor of _W_, labeled _L_ . The draws are calculated as
_β_ ˜ _n_ = _b_ + _Lη_ where _η_ is a draw of a _K_ -dimensional vector of independent standard normal deviates. In terms of computation time for
MSL, the main difference is that the model has far more parameters
with full _W_ than when _W_ is diagonal: _K_ + _K_ ( _K_ +1) _/_ 2 rather than the
2 _K_ parameters for independent coefficients. In our case with _K_ = 6,
the number of parameters rises from 12 to 27. The gradient with respect to each of the new parameters takes time to calculate, and the
model requires more iterations to locate the maximum over the largerdimensioned log-likelihood function. As shown in the second line of
Table 12.2, the run time nearly triples for the model with correlated
coefficients relative to independent coefficients.
With the Bayesian procedure, correlated coefficients are no harder
to handle than uncorrelated ones. For full _W_, the inverted gamma dis

350 _CHAPTER 12. BAYESIAN PROCEDURES_


Table 12.2: Run-Times in minutes

|Specification|MSL|SMP|
|---|---|---|
|All normal, no correlations<br>All normal, full covariance<br>1 ﬁxed, others normal, no corr<br>3 lognormal, 3 normal, no corr<br>All triangular, no corr|48<br>139<br>42<br>69<br>56|53<br>55<br>112<br>54<br>206|



tribution is replaced with its multivariate generalization, the inverted
Wishart. Draws are obtained by the procedure in section (12.5.2). The
only extra computer time relative to independent coefficients arises in
the calculation of the covariance matrix of the _βn_ ’s and its Choleski
factor, rather than the standard deviations of the _βn_ ’s. This difference is trivial for typical numbers of parameters. As shown in Table
12.2, run time for the model with full covariance among the random
coefficients was essentially the same as with independent coefficients.


**12.7.3** **Fixed coefficients for some variables**


There are various reasons that the researcher might choose to specify
some of the coefficients as fixed. (1) Ruud (1996) argues that a mixed
logit with all random coefficients is nearly unidentified empirically,
since only ratios of coefficients are economically meaningful. He recommends holding at least one coefficient fixed, particularly when the
data contain only one choice situation for each decision-maker. (2) In
a model with alternative-specific constants, the final iid extreme-value
terms constitute the random portion of these constants. Allowing the
coefficients of the alternative-specific dummies to be random in addition to having the final iid extreme-value terms is equivalent to assuming that the constants follow a distribution that is a mixture of extreme
value and whatever distribution is assumed for these coefficients. If
the two distributions are similar, such as a normal and extreme value,
the mixture can be unidentifiable empirically. In this case, the analyst might choose to keep the coefficients of the alternative-specific
constants fixed. (3) The goal of the analysis might be to forecast substitution patterns correctly rather than to understand the distribution
of coefficients. In this case, error components can be specified that
capture the correct substitution patterns while holding the coefficients


_12.7. CASE STUDY: CHOICE OF ENERGY SUPPLIER_ 351


of the original explanatory variables fixed (as in Brownstone and Train,
1999.) (4) The willingness to pay (wtp) for an attribute is the ratio of
the attribute’s coefficient to the price coefficient. If the price coefficient
is held fixed, the distribution of wtp is simply the scaled distribution
of the attribute’s coefficient. The distribution of wtp is more complex
when the price coefficient varies also. Furthermore, if the usual distributions are used for the price coefficient, such as normal or lognormal,
the issue arises of how to handle positive price coefficients, price coefficients that are close to zero such that the implied wtp is extremely
high, and price coefficients that are extremely negative. The first of
these issues is avoided with lognormals, but not the other two. The
analyst might choose to hold the price coefficient fixed to avoid these
problems.

In the classical approach, holding one or more coefficient fixed is
very easy. The corresponding elements of _W_ and _L_ are simply set to
zero, rather than treated as parameters. Run time is reduced since
there are fewer parameters. As indicated in the third line of Table
12.2, run time decreased by about 12 percent with one fixed coefficient
and the rest independent normal relative to all independent normals.
With correlated normals, a larger percent reduction would occur, since
the number of parameters drops more than proportionately.

In the Bayesian procedure, allowing for fixed coefficients requires
the addition of a new layer of Gibbs sampling. The fixed coefficient
cannot be drawn as part of the M-H algorithm for the random coefficients for each person. Recall that under M-H, trial draws are accepted
or rejected in each iteration. If a trial draw, which contains a new value
of a fixed coefficient along with new values of the random coefficients,
is accepted for one person, but the trial draw for another person is not
accepted, then the two people will have different values of the fixed
coefficient, which contradicts the fact that it is fixed. Instead, the random coefficients, and the population parameters of these coefficients,
must be drawn conditional on a value of the fixed coefficients; and
then the fixed coefficients are drawn conditional on the values of the
random coefficients. Drawing from the conditional posterior for the
fixed coefficients requires a M-H algorithm, in addition to the M-H
algorithm that is used to draw the random coefficients.

To be explicit, rewrite the utility function as


_Unjt_ = _α_ _[′]_ _znjt_ + _βn_ _[′]_ _[x][njt]_ [+] _[ ε][njt][,]_ (12.6)


352 _CHAPTER 12. BAYESIAN PROCEDURES_


where _α_ is a vector of fixed coefficients and _βn_ is random as before
with mean _b_ and variance _W_ . The probability of the person’s choice
sequence given _α_ and _βn_ is




   _L_ ( _yn | α, βn_ ) =

_t_



_e_ _[α][′][z][nyntt]_ [+] _[β]_ _n_ _[′]_ _[x][ny]_ _nt_ _[t]_

~~�~~ _[.]_ (12.7)
_j_ _[e][α]_ ~~_[′]_~~ _[z][njt]_ [+] _[β][n]_ ~~_[′]_~~ _[x][njt]_



The conditional posteriors for Gibbs sampling are:


1. _K_ ( _βn | α, b, W_ ) _∝_ _L_ ( _yn | α, βn_ ) _φ_ ( _βn | b, W_ ). M-H is used for
these draws in the same way as with all normals, except that
now _α_ _[′]_ _znjt_ is included in the logit formulas.

2. _K_ ( _b | W, βn ∀n_ ) is _N_ ( [�] _n_ _[β][n][/N, W/N]_ [)). Note that] _[ α]_ [ does not]
enter this posterior; its effect is incorporated into the draws of
_βn_ from layer 1.


3. _K_ ( _W | b, βn ∀n_ ) is _IW_ ( _K_ + _N,_ ( _KI_ + _N_ _S_ [¯] ) _/_ ( _K_ + _N_ )) where
_S_ ¯ = [�] _n_ [(] _[β][n][ −]_ _[b]_ [)(] _[β][n][ −]_ _[b]_ [)] _[′][/N]_ [. Again,] _[ α]_ [ does not enter directly.]

4. _K_ ( _α | βn_ ) _∝_ [�] _n_ _[L]_ [(] _[y][n][ |][ α, β][n]_ [), if the prior on] _[ α]_ [ is essentially]
flat (e.g., normal with sufficiently large variance.) Draws are
obtained with M-H on the pooled data.


Layer 4 takes as much time as layer 1, since each involves calculation of a logit formula for each observation. The Bayesian procedure
with fixed and normal coefficients can therefore be expected to take
about twice as much time as with all normal coefficients. As indicated
in the third line of Table 12.2, this expectation is confirmed in our
application.


**12.7.4** **Lognormals**


Lognormal distributions are often specified when the analyst wants to
assure that the coefficient takes the same sign for all people. Little
changes in either procedure when some or all of the coefficients are
distributed lognormal instead of normal. Normally distributed coefficients are drawn, and then the ones that are lognormally distributed
are exponentiated when they enter utility. With all lognormals, utility
is specified as
_Unjt_ = ( _e_ _[β][n]_ ) _[′]_ _xnjt_ + _εnjt,_ (12.8)


_12.7. CASE STUDY: CHOICE OF ENERGY SUPPLIER_ 353


with _βn_ distributed normal as before with mean _b_ and variance _W_ .
The probability of the person’s choice sequence given _βn_ is




   _L_ ( _yn | α, βn_ ) =

_t_



_e_ [(] _[e][βn]_ [)] _[′][x][nyntt]_

~~�~~ _[.]_ (12.9)
_j_ _[e]_ [(] _[e][βn]_ [)] _[′][x][njt]_



With this one change, the rest of the steps are the same with both
procedures. In the classical approach, however, locating the maximum
of the likelihood function is considerably more difficult with lognormal coefficients than normal ones. Often the numerical maximization
procedures fail to find an increase after a number of iterations. Or
a “maximum” is found and yet the Hessian is singular at that point.
It is often necessary to specify starting values that are close to the
maximum. And the fact that the iterations can fail at most starting
values makes it difficult to determine whether a maximum is local or
global. The Bayesian procedure does not encounter these difficulties
since it does not search for the maximum. The Gibbs sampling seems
to converge a bit more slowly, but not appreciably so. As indicated
in Table 12.2, run time for the classical approach rose nearly 50 percent with lognormal relative to normals (due to more iterations being
needed), while the Bayesian procedure took about the same amount of
time with each. This comparison is generous to the classical approach,
since convergence at a maximum was achieved in this application while
in many other applications we have not been able to obtain convergence
with lognormals or have done so only after considerable time was spent
finding successful starting values.


**12.7.5** **Triangulars**


Normal and lognormal distributions allow coefficients of unlimited magnitude. In some situations, the analyst might want to assure that the
coefficients for all people remain within a reasonable range. This goal
is accomplished by specifying distributions that have bounded support, such as uniform, truncated normal, and triangular distributions.
In the classical approach, these distributions are easy to handle. The
only change occurs in the line of code that creates the random draws
from the distributions. For example, the density of a triangular distribution with mean _b_ and “spread” _s_ is zero beyond the range ( _b−s, b_ + _s_ ),
rises linearly from _b −_ _s_ to _b_, and drops linearly to _b_ + _s_ . A draw is

              created as _βn_ = _b_ + _s_ ( _[√]_ ~~2~~ ~~_µ_~~ _−_ 1) if _µ <_ 0 _._ 5 and = _b_ + _s_ (1 _−_ 2(1 _−_ _µ_ ))


354 _CHAPTER 12. BAYESIAN PROCEDURES_


otherwise, where _µ_ is a draw from a standard uniform. Given draws of
_βn_, the calculation of the simulated probability and the maximization
of the likelihood function are the same as with draws from a normal.
Experience indicates that estimation of the parameters of uniform,
truncated normal and triangular distributions takes about the same
number of iterations as for normals. The last line of Table 12.2 reflects
this experience.
With the Bayesian approach, the change to non-normal distributions is far more complicated. With normally distributed coefficients,
the conditional posterior for the population moments are very convenient: normal for the mean and inverted Wishart for the variance.
Most other distributions do not give such convenient posteriors. Usually, a M-H algorithm is needed for the population parameters, in addition to the M-H algorithm for the customer-level _βn_ ’s. This addition
adds considerably to computation time. The issue is exacerbated for
distributions with bounded support, since, as we see below, the M-H
algorithm can be expected to converge slowly for these distributions.
With independent triangular distributions for all coefficients with
mean and spread vectors _b_ and _s_, and flat priors on each, the conditional posteriors are:


1. _K_ ( _βn | b, s_ ) _∝_ _L_ ( _yn | βn_ ) _h_ ( _βn | b, s_ ) where _h_ is the triangular
density. Draws are obtained through M-H, separately for each
person. This step is the same as with independent normals except
that the density for _βn_ is changed.

2. _K_ ( _b, s | βn_ ) _∝_ [�] _n_ _[h]_ [(] _[β][n][ |][ b, s]_ [) when the priors on] _[ b]_ [ and] _[ s]_ [ are]
essentially flat. Draws are obtained through M-H on the _βn_ ’s for
all people.


Because of the bounded support of the distribution, the algorithm
is exceedingly slow to converge. Consider, for example, the spread of
the distribution. In the first layer, draws of _βn_ that are outside the
range ( _b −_ _s, b_ + _s_ ) from the second layer are necessarily rejected. And
in the second layer, draws of _b_ and _s_ that create a range ( _b −_ _s, b_ + _s_ )
that does not cover all the _βn_ ’s from the first layer are necessarily
rejected. It is therefore difficult for the range to grow narrower from
one iteration to the next. For example, if the range is 2 to 4 in one
iteration of the first layer, then the next iteration will result in values of
_βn_ between 2 and 4 and will usually cover most of the range if sample


_12.8. BAYESIAN PROCEDURES FOR PROBIT MODELS_ 355


size is sufficiently large. In the next draw of _b_ and _s_, any draw that
does not cover the range of the _βn_ ’s (which is nearly 2 to 4) will be
rejected. There is indeed some room for play, since the _βn_ ’s will not
cover the entire range from 2 to 4. The algorithm converges, but in our
application we found that far more iterations were needed to achieve a
semblance of convergence, compared with normal distributions. Run
time rose by a factor of four as a result.


**12.7.6** **Summary of results**


For normal distributions with full covariance matrixes, and for transformations of normals that can be expressed in the utility function,
such as exponentiating to represent lognormal distributions, the Bayesian
approach seems to be very attractive computationally. Fixed coefficients add a layer of conditioning to the Bayesian approach that doubles its run time. In contrast, the classical approach becomes faster
for each coefficient that is fixed instead of random, because there are
fewer parameters to estimate. For distributions with bounded support,
like triangulars, the Bayesian approach is very slow, while the classical
approach handles these distributions as quickly as normals.
These comparisons relate to mixed logits only. Other behavioral
models can be expected to have different relative run times for the two
approaches. The comparison with mixed logit elucidates the issues
that arise in implementing each method. Understanding these issues
assists the researcher in specifying the model and method that is most
appropriate and convenient for the choice situation.

## **12.8 Bayesian procedures for probit models**


Bayesian procedures can be applied to probit models. In fact, the
methods are even faster for probit models than mixed logits. The procedure is described by Albert and Chib (1993), McCulloch and Rossi
(1994), Allenby and Rossi (1999), and McCulloch and Rossi (2000).
The method differs in a critical way from the procedure for mixed
logits. In particular, for a probit model, the probability of each person’s choices condition on the coefficients of the variables, which is the
analog to _L_ ( _yn | βn_ ) for logit, is not a closed form. Procedures that
utilize this probability, as in the first layer of Gibbs sampling for mixed
logit, cannot be readily applied to probit. Instead, Gibbs sampling for


356 _CHAPTER 12. BAYESIAN PROCEDURES_


probits is accomplished by considering the utility of each alternative,
_Unjt_, to be parameters themselves. The conditional posterior for each
_Unjt_ is truncated normal, which is easy to draw from. The layers for
the Gibbs sampling are:


1. Draw _b_ conditional on _W_ and _βn ∀n_ .


2. Draw _W_ conditional on _b_ and _βn ∀n_ . These two layers are the
same as for mixed logit.


3. For each _n_, draw _βn_ conditional on _Unjt ∀j, t._ These draws are
obtained by recognizing that, given the value of utility, the function _Unjt_ = _βnxnjt_ + _εnjt_ is a regression of _xnjt_ on _Unjt_ . Bayesian
posteriors for regression coefficients and normally distributed errors have been derived (similar to our results A and B) and are
easy to draw from.


4. For each _n, i, t_, draw _Unit_ conditional on _βn_ and the value of _Unjt_
for each _j ̸_ = _i_ . As stated above, the conditional posterior for
each _Unit_ is a univariate truncated normal, which is easy to draw
from with the procedure given in section (9.2.4).


Details are provided in the cited articles.
Bolduc, Fortin and Gordon (1997) compared the Bayesian method
with MSL and found the Bayesian procedure to require about half as
much computer time as MSL with random draws. If Halton draws
had been used, it seems that MSL would have been faster for the
same level of accuracy, since fewer than half as many draws would
be needed. The Bayesian procedure for probit relies on all random
terms being normally distributed. However, the concept of treating
the utilities as parameters can be generalized for other distributions,
giving a Bayesian procedure for mixed probits.
Bayesian procedures can be developed in some form or another for
essentially any behavioral model. In many cases, they provide large
computational advantages over classical procedures. Examples include
the dynamic discrete choice models of Ching, Imai and Jain (2001), the
joint models of the timing and quantity of purchases of Boatwright,
Borle and Kadane (2001), and Brownstone’s (2001) mixtures of distinct
discrete choice models. The power of these procedures, and especially
the potential for cross-fertilization with classical methods, create a
bright outlook for the field.


# **Bibliography**

Adamowicz, W. (1994), ‘Habit formation and variety seeking in a discrete choice model of recreation demand’, _Journal of Agricultural_
_and Resource Economics_ **19**, 19–31.


Ainslie, A., R. Andrews and I. Currim (2001), ‘An empirical comparison of logit choice models with discrete vs. continuous representation of heterogeneity’, Working Paper, Department of Business
Administration, University of Delaware.


Albert, J. and S. Chib (1993), ‘Bayesian analysis of binary and polychotomous response data’, _Journal of the American Statistical As-_
_sociation_ **88**, 669–679.


Allenby, G. (1997), ‘An introduction to hierarchical bayesian modeling’, Tutorial notes, Advanced Research Techniques Forum,
American Marketing Association.


Allenby, G. and P. Lenk (1994), ‘Modeling household purchase behavior with logistic normal regression’, _Journal of the American_
_Statistical Association_ **89**, 1218–1231.


Allenby, G. and P. Rossi (1999), ‘Marketing models of consumer heterogeneity’, _Journal of Econometrics_ **89**, 57–78.


Amemiya, T. (1978), ‘On two-step estimation of multivariate logit
models’, _Journal of Econometrics_ **8**, 13–21.


Arora, N., G. Allenby and J. Ginter (1998), ‘A hierachical bayes model
of primary and secondary demand’, _Marketing Science_ **17**, 29–44.


Beggs, S., S. Cardell and J. Hausman (1981), ‘Assessing the potential
demand for electric cars’, _Journal of Econometrics_ **16**, 1–19.


357


358 _BIBLIOGRAPHY_


Bellman, R. (1957), _Dynamic Programming_, Princeton University
Press, Princeton NJ.


Ben-Akiva, M. (1972), The Structure of Travel Demand Models, PhD
thesis, MIT.


Ben-Akiva, M. and B. Francois (1983), ‘Mu-homogenous generalized
extreme value model’, Working Paper, Department of Civil Engineering, MIT.


Ben-Akiva, M. and D. Bolduc (1996), ‘Multinomial probit with a
logit kernel and a general parametric specification of the covariance structure’, Working Paper, Department of Civil Engineering,
MIT.


Ben-Akiva, M., D. Bolduc and J. Walker (2001), ‘Specification, estimation and identification of the logit kernel (or continuous mixed
logit) model’, Working Paper, Department of Civil Engineering,
MIT.


Ben-Akiva, M., D. Bolduc and M. Bradley (1993), ‘Estimation of travel
model choice models with randomly distributed values of time’,
_Transportation Research Record_ **1413**, 88–97.


Ben-Akiva, M. and M. Bierlaire (1999), Discrete choice methods and
their applications in short term travel decisions, _in_ R.Hall, ed.,
‘The Handbook of Transportation Science’, Kluwer, Dordrecht,
the Netherlands, pp. 5–33.


Ben-Akiva, M. and S. Lerman (1985), _Discrete Choice Analysis : The-_
_ory and Application to Travel Demand_, MIT Press, Cambridge,
Massahusetts.


Ben-Akiva, M. and T. Morikawa (1990), ‘Estimation of switching models from revealed preferences and stated intentions’, _Transporta-_
_tion Research A_ **24**, 485–495.


Berkovec, J. and S. Stern (1991), ‘Job exit behavior of older men’,
_Econometrica_ **59**, 189–210.


Berndt, E., B. Hall, R. Hall and J. Hausman (1974), ‘Estimation and
inference in nonlinear structural models’, _Annals of Economic and_
_Social Measurement_ **3/4**, 653–665.


_BIBLIOGRAPHY_ 359


Bernstein, S. (1917), _Calcul des probabilites_ .


Berry, S. (1994), ‘Estimating discrete choice models of product differentiation’, _RAND Journal of Economics_ **25**, 242–262.


Berry, S., J. Levinsohn and A. Pakes (1995), ‘Automobile prices in
market equilibrium’, _Econometrica_ **63**, 841–889.


Bhat, C. (1995), ‘A heteroscedastic extreme value model of intercity
mode choice’, _Transportation Research B_ **29**, 471–483.


Bhat, C. (1997), ‘Covariance heterogeneity in nested logit models:
Econometric structure and application to intercity travel’, _Trans-_
_portation Research B_ **31**, 11–21.


Bhat, C. (1998 _a_ ), ‘Accommodating variations in responsiveness to
level-of-service variables in travel mode choice models’, _Trans-_
_portation Research A_ **32**, 455–507.


Bhat, C. (1998 _b_ ), ‘An analysis of travel mode and departure time
choice for urban shopping trips’, _Transportation Research B_
**32**, 361–371.


Bhat, C. (1999), ‘An analysis of evening commute stop-making behavior using repeated choice observation from a multi-day survey’,
_Transportation Research B_ **33**, 495–510.


Bhat, C. (2000), ‘Incorporating observed and unobserved heterogeneity in urban work mode choice modeling’, _Transportation Science_
**34**, 228–238.


Bhat, C. (2001), ‘Quasi-random maximum simulated likelihood estimation of the mixed multinomial logit model’, _Transportation Re-_
_search B_ **35**, 677–693.


Bhat, C. (forthcoming), ‘Simulation estimation of mixed discrete
choice models using randomized and scrambled halton sequences’,
_Transportation Research_ .


Bhat, C. and S. Castelar (2001), ‘A unified mixed logit framework
for modeling revealed and stated preferences: Formulation and
application to congestion pricing analysis in the san francisco bay
area’, _Transportation Research_ .


360 _BIBLIOGRAPHY_


Bickel, P. and K. Doksum (2000), _Mathematical Statistics: Basic ideas_
_and Selected Topics_, Vol. 1, Prentice Hall, Upper Saddle River,
NJ.


Bierlaire, M. (1998), Discrete choice models, _in_ m. Labbe, G.Laporte,
K.Tanczos and P.Toint, eds, ‘Operations Research and Decision
Aid Methodologies in Traffic and Transportation Management’,
Spinger Verlag, Heidelberg, Germany, pp. 203–227.


Boatwright, P., S. Borle and J. Kadane (2001), ‘A model of the joint
distribution of purchase quantity and timing’, Conference Presentation, Bayesian Applications and Methods in Marketing Conference, Ohio State University.


Bolduc, D. (1992), ‘Generalized autoregressive errors: the multinomial
probit model’, _Transportation Research B_ **26**, 155–170.


Bolduc, D. (1993), ‘Maximum simulated likelihood estimation of mnp
models using the ghk probability simulation with analytic derivatives’, Working Paper, Department d’ Economique, Universite
Laval, Quebec.


Bolduc, D. (1999), ‘A practical technique to estimate multinomial probit models in transportation’, _Transportation Research B_ **33**, 63–
79.


Bolduc, D., B. Fortin and M. Fournier (1996), ‘The impact of incentive
policies on the practice location of doctors: A multinomial probit
analysis’, _Journal of Labor Economics_ **14**, 703–732.


Bolduc, D., B. Fortin and S. Gordon (1997), ‘Multinomial probit estimation of spatially interdependent choices: An empirical comparison of two new techniques’, _International Regional Science_
_Review_ **20**, 77–101.


Borsch-Supan, A. and V. Hajivassiliou (1993), ‘Smooth unbiased multivariate probablility simulation for maximum likelihood estimation
of limited dependent variable models’, _Journal of Econometrics_
**58**, 347–368.


Borsch-Supan, A., V. Hajivassiliou, L. Kotlikoff and J. Morris (1991),
Health, children, and elderly living arrangements: A multiperiod


_BIBLIOGRAPHY_ 361


multinomial probit model with unobserved heterogeneity and autocorrelated errors, _in_ D.Wise, ed., ‘Topics in the Economics of
Aging’, University of Chicago Press, Chicago, IL.


Boyd, J. and J. Mellman (1980), ‘The effect of fuel economy standards on the u.s. automotive market: a hedonic demand analysis’,
_Transportation Research A_ **14**, 367–378.


Braatan and Weller (1979), ‘An improved low-discrepancy sequence
for multi-dimensional quasi-monte carlo integration’, _Journal of_
_Computational Physics_ **33**, 249–258.


Bradley, M. and Andrew Daly (1994), ‘Use of the logit scaling approach
to test for rank-order and fatigue effects in stated preference data’,
_Transportation_ **21**, 167–184.


Bradlow, E. and P. Fader (2001), ‘A bayesian lifetime model for the
’hot 100’ billboard songs’, Working Paper, The Wharton School,
University of Pennsylvania.


Brownstone, D. (2001), Discrete choice modeling for transportation, _in_
D.Hensher, ed., ‘Travel Behavior Research: The Leading Edge’,
Elsevier, Oxford, UK, pp. 97–124.


Brownstone, D., D. Bunch and K. Train (2000), ‘Joint mixed logit
models of stated and revealed preferences for alternative-fuel vehicles’, _Transportation Research B_ **34**, 315–338.


Brownstone, D. and K. Small (1989), ‘Efficient estimation of nested
logit model’, _Journal of Business and Economic Statistics_ **7**, 67–
74.


Brownstone, D. and K. Train (1999), ‘Forecasting new product penetration with flexible substitution patterns’, _Journal of Economet-_
_rics_ **89**, 109–129.


Bunch, D. (1991), ‘Estimability in the multinomial probit model’,
_Transportation Research B_ **25**, 1–12.


Bunch, D. and R. Kitamura (1989), ‘Multinomial probit estimation
revisited: Testing new algorithms and evaluation of alternative
model specification of household car ownership’, Transportation
Research Group Report UCD-TRG-RR-4, University of California, Davis.


362 _BIBLIOGRAPHY_


Butler, J. and R. Moffitt (1982), ‘A computationally efficient quadrature procedure for the one factor multinomial probit model’,
_Econometrica_ **50**, 761–764.


Cai, Y., I. Deilami and K. Train (1998), ‘Customer retention in a
competitive power market: Analysis of a ‘double-bounded plus
follow-ups’ questionnaire’, _The Energy Journal_ **19**, 191–215.


Cam, L. Le and G. Yang (1990), _Asymptotics in Statistics_, SpringerVerlag, New York.


Cameron, T. (1988), ‘A new paradigm for valuing non-market goods
using referendum data: Maximum likelihood estimation by censored logistic regression’, _Journal of Environmental Economics_
_and Management_ **15**, 355–379.


Cameron, T. and J. Quiggin (1994), ‘Estimation using contingent valuation data from a ‘dichotomous choice with follow-up’ questionnaire’, _Journal of Environmental Economics and Management_
**27**, 218–234.


Cameron, T. and M. James (1987), ‘Efficient estimation methods for
closed-ended contingent valuation survey data’, _Review of Eco-_
_nomics and Statistics_ **69**, 269–276.


Cardell, S. and F. Dunbar (1980), ‘Measuring the societal impacts of
automobile downsizing’, _Tranportation Research A_ **14**, 423–434.


Carneiro, P., J. Heckman and E. Vytlacil (2001), ‘Estimating the returns to education when it varies among individuals’, Working
Paper, Department of Economics, University of Chicago.


Casella, G. and E. George (1992), ‘Explaining the gibbs sampler’, _The_
_American Statistician_ **46**, 167–174.


Chapman, R. and R. Staelin (1982), ‘Exploiting rank ordered choice
set data within the stochastic utility model’, _Journal of Marketing_
_Research_ **14**, 288–301.


Chesher, A. and J. Santos-Silva (2002), ‘Taste variation in discrete
choice models’, _Review of Economic Studies_ **69**, 62–78.


_BIBLIOGRAPHY_ 363


Chiang, J., S. Chib and C. Narasimhan (1999), ‘Markov chain monte
carlo and models of consideration set and parameter heterogeneity’, _Journal of Econometrics_ **89**, 223–248.


Chib, S. and E. Greenberg (1995), ‘Understanding the metropolis hastings algorithm’, _American Statistician_ **49**, 327–335.


Chib, S. and E. Greenberg (1996), ‘Markov chain monte carlo simulation methods in econometrics’, _Econometric Theory_ **12**, 409–431.


Chib, S. and E. Greenberg (1998), ‘Analysis of multivariate probit
models’, _Biometrika_ **85**, 347–361.


Ching, A., S. Imai and N. Jain (2001), ‘Bayesian estimation of dynamics discrete choice models’, Conference Presentation, Bayesian Applications and Methods in Marketing Conference, Ohio State University.


Chintagunta, P., D. Jain and N. Vilcassim (1991), ‘Investigating heterogeneity in brand preference in logit models for panel data’,
_Journal of Marketing Research_ **28**, 417–428.


Chipman, J. (1960), ‘The foundations of utility’, _Econometrica_
**28**, 193–224.


Chu, C. (1981), Structural Issues and Sources of Bias in Residential
Location and Travel Choice Models, PhD thesis, Northwestern
University.


Chu, C. (1989), ‘A paired combinational logit model for travel demand
analysis’, _Proceedings of Fifth World Conference on Transporta-_
_tion Research_ **4**, 295–309.


Clark, C. (1961), ‘The greatest of a finite set of random variables’,
_Operations Research_ **9**, 145–162.


Cosslett, S. (1981), Efficient estimation of discrete choice models, _in_
C.Manski and D.McFadden, eds, ‘Structural Analysis of Discrete
Data with Econometric Applications’, MIT Press, Cambridge,
MA.


Cowles, M. and B. Carlin (1996), ‘Markov chain monte carlo convergence diagnostics: A comparative review’, _Journal of American_
_Statistical Association_ **91**, 883–904.


364 _BIBLIOGRAPHY_


Daganzo, C. (1979), _Multinomial Probit: The Theory and Its Applica-_
_tion to Demand Forecasting_, Academic Press, New York.


Daganzo, C., F. Bouthelier and Y. Sheffi (1977), ‘Multinomial probit
and qualitative choice: A computationally efficient algorithm’,
_Transportation Science_ **11**, 338–358.


Dagsvik, J. (1994), ‘Discrete and continuous choice max-stable processes and independence from irrelevant alternatives’, _Economet-_
_rica_ **62**, 1179–205.


Daly, A. (1987), ‘Estimating ’tree’ logit models’, _Transportation Re-_
_search B_ **21**, 251–267.


Daly, A. and S. Zachary (1978), Improved multiple choice models, _in_
D.Hensher and M.Dalvi, eds, ‘Determinants of Travel Choice’,
Saxon House, Sussex.


Debreu, G. (1960), ‘Review of r.d. luce individual choice behavior’,
_American Economic Review_ **50**, 186–88.


DeSarbo, W., V. Ramaswamy and S. Cohen (1995), ‘Market segmentation with choice-based conjoint analysis’, _Marketing Letters_
**6**, 137–147.


Desvousges, W., S. Waters and K. Train (1996), ‘Potential economic
losses associated with recreational services in the upper clark fork
river basin’, Report, Triangle Economic Research, Durham, NC.


Dubin, J. and D. McFadden (1984), ‘An econometric analysis of residential electric appliance holdings and consumption’, _Economet-_
_rica_ **52**, 345–362.


Eckstein, Z. and K. Wolpin (1989), ‘The specification and estimation
of dynamic stochastic discrete choice models: A survey’, _Journal_
_of Human resources_ **24**, 562–598.


Elrod, T. and M. Keane (1995), ‘A factor analytic probit model for
representing the market structure in panel data’, _Journal of Mar-_
_keting Research_ **32**, 1–16.


Erdem, T. (1996), ‘A dynamic analysis of market structure based on
panel data’, _Marketing Science_ **15**, 359–378.


_BIBLIOGRAPHY_ 365


Forinash, C. and F. Koppelman (1993), ‘Application and interpretation
of nested logit models of intercity mode choice’, _Transportation_
_Research Record_ **1413**, 98–106.


Gelman, A. (1992), ‘Iterative and non-iterative simulation algorithms’,
_Computing Science and Statistics (Interface Proceedings)_ **24**, 433–
438.


Gelman, A. and D. Rubin (1992), ‘Inference from iterative simulation
using multiple sequences’, _Statistical Sciences_ **7**, 457–511.


Gelman, A., J. Carlin, H. Stern and D. Rubin (1995), _Bayesian Data_
_Analysis_, Chapman and Hall, Suffolk.


Geman, S. and D. Geman (1984), ‘Stochastic relaxation gibbs distributions and the bayesian restoration of images’, _IEEE Transactions_
_on Pattern Analysis and Machine Intelligence_ **6**, 721–741.


Geweke, J. (1988), ‘Antithetic acceleration of monte carlo integration
in bayesian inference’, _Journal of Econometrics_ **38**, 73–89.


Geweke, J. (1989), ‘Bayesian inference in econometric models using
monte carlo integration’, _Econometrica_ **57**, 1317–1339.


Geweke, J. (1991), ‘Efficient simulation from the multivariate normal
and student -t distributions subject to linear constraints’, _Com-_
_puter Science and Statistics: Proceedings of the Twenty-Third_
_Symposium on the Interface_ pp. 571–578.


Geweke, J. (1992), Evaluating the accuracy of sampling-based approaches to the calculation of posterior moments, _in_ J.Bernardo,
J.Berger, A.Dawid and F.Smith, eds, ‘Bayesian Statistics’, Oxford
University Press, New York, pp. 169–193.


Geweke, J. (1996), Monte carlo simulation and numerical integration,
_in_ D.Kendrick and J.Rust, eds, ‘Handbook of Computational Economics’, Elsevier Science, Amsterdam, pp. 731–800.


Geweke, J. (1997), Posterior simulators in econometrics, _in_ D.Kreps
and K.Wallis, eds, ‘Advance Economics and Econometric Theory
and Applications’, Cambridge University Press, New York.


