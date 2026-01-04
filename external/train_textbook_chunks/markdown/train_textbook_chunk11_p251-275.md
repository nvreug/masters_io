_9.2. RANDOM DRAWS_ 241


where _m_ = 1 _/_ 2 _[K]_ . For each draw, assign the weight



_f_ ( _ε_ ) _[m]_
_g_ ( _ε_ ) [=] _k_



_k_ _[|]_ [Ω] _[|]_ [(] _[−]_ 2 [1]



2 [1] [)] _e_ _[ε][′]_ [(Ω] _[−]_ [1] _[−][I]_ [)] _[ε]_ [)] _._



The weighted draws are equivalent to draws from _N_ (0 _,_ Ω) truncated
below at zero.
As a sidelight, note that the accept-reject procedure in section 9.2.6
is a type of importance sampling. The truncated distribution is the
target and the untruncated distribution is the proposal density. Each
draw from the untruncated density is weighted by a constant if the
draw is within the truncation space and weighted by zero if the draw
is outside the truncation space. Weighting by a constant or zero is
equivalent to weighting by one (accept) or zero (reject).


**9.2.8** **Gibbs sampling**


For multinomial distributions, it is sometimes difficult to draw directly
from the joint density and yet easy to draw from the conditional density
of each element given the values of the other elements. Gibbs sampling,
a term that was apparently introduced by Geman and Geman (1984),
can be used in these situations. A general explanation is provided by
Casella and George (1992), which the reader can use, if interested, to
supplement the more concise description that I give below.
Consider two random variables _ε_ 1 and _ε_ 2. Generalization to higher
dimension is obvious. The joint density is _f_ ( _ε_ 1 _, ε_ 2) and the conditional
densities are _f_ ( _ε_ 1 _|ε_ 2) and _f_ ( _ε_ 2 _|ε_ 1). Gibbs sampling proceeds by drawing iteratively from the conditional densities: drawing _ε_ 1 conditional
on a value of _ε_ 2, drawing _ε_ 2 conditional on this draw of _ε_ 1, drawing
a new _ε_ 1 conditional on the new value of _ε_ 2, and so on. This process
converges to draws from the joint density.
To be more precise: (1) Choose an initial value for _ε_ 1, called _ε_ [0] 1 [.]
Any value with non-zero density can be chosen. (2) Draw a value
of _ε_ 2, called _ε_ [0] 2 [, from] _[ f]_ [(] _[ε]_ [2] _[|][ε]_ [0] 1 [). (3) Draw a value of] _[ ε]_ [1][, called] _[ ε]_ [1] 1 [, from]
_f_ ( _ε_ 1 _|ε_ [0] 2 [). (4) Draw] _[ ε]_ [1] 2 [, from] _[ f]_ [(] _[ε]_ [2] _[|][ε]_ [1] 1 [). And so on. The values of] _[ ε][t]_ 1 [, from]
_f_ ( _ε_ 1 _|ε_ _[t]_ 2 _[−]_ [1] ) and the values of _ε_ _[t]_ 2 [, from] _[ f]_ [(] _[ε]_ [2] _[|][ε][t]_ 1 _[−]_ [1] ) constitute a sequence
in _t_ . For sufficiently high _t_ (that is, for sufficiently many iterations),
the sequence converges to draws from the joint density _f_ ( _ε_ 1 _, ε_ 2).
As an example, consider two standard normal deviates that are
independent except that they are truncated on the basis of their sum:


242 _CHAPTER 9. DRAWING FROM DENSITIES_

|Col1|ε2|
|---|---|
||_m_<br>_m_<br>2|
|||



Figure 9.3: Truncated normal density.


_ε_ 1 + _ε_ 2 _≤_ _m_ . Figure 9.3 depicts the truncated density. The circles
denote contours of the untruncated density and the shaded area represents the truncated density. To derive the conditional densities, consider first the untruncated normals. Since the two deviates are independent, the conditional density of each is the same as its unconditional
density. That is, ignoring truncation, _ε_ 1 _|ε_ 2 _∼_ _N_ (0 _,_ 1). The truncation
rule is _ε_ 1 + _ε_ 2 _≤_ _m_ which can be re-expressed as _ε_ 1 _≤_ _m −_ _ε_ 2. Therefore, _ε_ 1 _|ε_ 2 is distributed as a univariate standard normal truncated
from above at _m_ _−_ _ε_ 2. Given _ε_ 2, a draw of _ε_ 1 is obtained with the procedure in section 9.2.4: _ε_ 1 = Φ _[−]_ [1] ( _µ_ Φ( _m −_ _ε_ 2)), where _µ_ is a standard
uniform draw and Φ( _·_ ) is the cumulative standard normal distribution.
Draws from _ε_ 2 conditional on _ε_ 1 are obtained analogously. Drawing
sequentially from these conditional densities eventually provides draws
from the joint truncated density.


**9.2.9** **Metropolis-Hastings algorithm**


If all else fails, the Metropolis-Hastings (M-H) algorithm can be used
to obtain draws from a density. Initially developed by Metropolis et
al. (1953) and generalized by Hastings (1970), the M-H algorithm
operates as follows. The goal is to obtain draws from _f_ ( _ε_ ). (1) Start
with a value of the vector _ε_, labeled _ε_ [0] . (2) Choose a “trial” value of _ε_ [1]

as ˜ _ε_ [1] = _ε_ [0] + _η_ where _η_ is drawn from a distribution _g_ ( _η_ ) that has zero
mean. Usually a normal distribution is specified for _g_ ( _η_ ). (3) Calculate
the density at the trial value ˜ _ε_ [1] and compare it to the density at the


_9.2. RANDOM DRAWS_ 243


original value _ε_ [0] . That is, compare _f_ (˜ _ε_ [1] ) with _f_ ( _ε_ [0] ). If _f_ (˜ _ε_ [1] ) _> f_ ( _ε_ [0] ),
then accept ˜ _ε_ [1], label it _ε_ [1], and move to step 4. If _f_ (˜ _ε_ [1] ) _≤_ _f_ ( _ε_ [0] ),
then accept ˜ _ε_ [1] with probability _[f]_ [(˜] _[ε]_ [1][)]

_f_ ( _ε_ ~~[0]~~ ) [, and reject it with probability]

1 _−_ _[f]_ [(˜] _[ε]_ [1][)]

_f_ ( _ε_ ~~[0]~~ ) [. To determine whether to accept or reject ˜] _[ε]_ [1][ in this case,]



draw a standard uniform _µ_ . If _µ ≤_ _[f]_ [(˜] _[ε]_ [1][)]

~~[0]~~



draw a standard uniform _µ_ . If _µ ≤_ _[f]_ [(˜] _[ε]_ [)]

_f_ ( _ε_ ~~[0]~~ ) [, then keep ˜] _[ε]_ [1][. Otherwise,]
reject ˜ _ε_ [1] . If ˜ _ε_ [1] is accepted, then label it _ε_ [1] . If ˜ _ε_ [1] is rejected, then
use _ε_ [0] as _ε_ [1] . (4) Choose a trial value of _ε_ [2] as ˜ _ε_ [2] = _ε_ [1] + _η_, where _η_ is
a new draw from _g_ ( _η_ ). (5) Apply the rule in step 3 to either accept
_ε_ ˜ [2] as _ε_ [2] or reject ˜ _ε_ [2] and use _ε_ [1] as _ε_ [2] . (6) Continue this process for
many iterations. The sequence _ε_ _[t]_ becomes equivalent to draws from
_f_ ( _ε_ ) for sufficiently large _t_ . The draws are serially correlated, since
each draw depends on the previous draw. In fact, when a trial value is
rejected the current draw is the same as the previous draw. This serial
correlation needs to be considered when using these draws.
The M-H algorithm can be applied with any density that can be
calculated. The algorithm is particularly useful when the normalizing
constant for a density is not known or cannot be easily calculated.
Suppose that we know that _ε_ is distributed proportional to _f_ _[∗]_ ( _ε_ ). This
means that the density of _ε_ is _f_ ( _ε_ ) = [1] _[f]_ _[∗]_ [(] _[ε]_ [), where the normalizing]



means that the density of _ε_ is _f_ ( _ε_ ) = [1]

        - _k_ _[f]_ _[∗]_ [(] _[ε]_ [), where the normalizing]
constant _k_ = _f_ _∗_ ( _ε_ ) _dε_ assures that _f_ integrates to 1. Usually _k_
cannot be calculated analytically, for the same reason that we need to
simulate integrals in other settings. Luckily, the M-H algorithm does
not utilize _k_ . A trial value of _ε_ _[t]_ is tested by first determining whether
_f_ (˜ _ε_ _[t]_ ) _> f_ ( _ε_ _[t][−]_ [1] ). This comparison is unaffected by the normalizing
constant, since the constant enters the denominator on both sides.
Then, if _f_ (˜ _ε_ _[t]_ ) _≤_ _f_ ( _ε_ _[t][−]_ [1] ), we accept the trial value with probability
_f_ (˜ _ε_ _[t]_ )
_f_ ( _ε_ ~~_[t][−]_~~ ~~[1]~~ ) [. The normalizing constant drops out of this ratio.]
The M-H algorithm is actually more general than I describe here,
though in practice it is usually applied as I describe. Chib and Greenberg (1995) provide an excellent description of the more general algorithm as well as an explanation of why it works. Under the more
general definition, Gibbs sampling is a special case of the M-H algorithm, as Gelman (1992) pointed out. The M-H algorithm and Gibbs
sampling are often called Markov Chain Monte Carlo (MCMC, or MCsquared) methods; a description of their use in econometrics is provided
by Chib and Greenberg (1996). The draws are Markov chains because
each value depends only on the immediately preceding one, and the
methods are Monte Carlo because random draws are taken. We ex

244 _CHAPTER 9. DRAWING FROM DENSITIES_


plore further issues about the M-H algorithm, such as how to choose
_g_ ( _ε_ ), in the context of its use with hierarchical Bayes procedures (in
chapter 12).

# **9.3 Variance Reduction**


The use of independent random draws in simulation is appealing because it is conceptually straightforward and the statistical properties
of the resulting simulator are easy to derive. However, there are other
ways to take draws that can provide greater accuracy for a given number of draws. We examine these alternative methods in the following
sections.
Recall that the objective is to approximate an integral of the form

_t_ ( _ε_ ) _f_ ( _ε_ ) _dε_ . In taking a sequence of draws from the density _f_ ( _· · ·_ ),
two issues are at stake: coverage and covariance. Consider coverage
first. The integral is over the entire density _f_ . It seems reasonable that
a more accurate approximation would be obtained by evaluating _t_ ( _ε_ )
at values of _ε_ that are spread throughout the domain of _f_ . With independent random draws, it is possible that the draws will be clumped
together, with no draws from large areas of the domain. Procedures
that guarantee better coverage can be expected to provide a better
approximation.
Covariance is another issue. With independent draws, the covariance over draws is zero. The variance of a simulator based on _R_ independent draws is therefore the variance based on 1 draw divided by
_R_ . If the draws are negatively correlated instead of independent, then
the variance of the simulator is lower. Consider _R_ = 2. The variance
of _t_ [ˇ] = [ _t_ ( _ε_ 1) + _t_ ( _ε_ 2)] _/_ 2 is [ _V_ ( _t_ ( _ε_ 1) + _V_ ( _t_ ( _ε_ 2) + 2 _Cov_ ( _t_ ( _ε_ 1) _, t_ ( _ε_ 2))] _/_ 4. If
the draws are independent, then the variance is _V_ ( _t_ ( _εr_ )) _/_ 2. If the two
draws are negatively correlated with each other, the covariance term
is negative and the variance becomes less than _V_ ( _t_ ( _εr_ )) _/_ 2. Essentially,
when the draws are negatively correlated within an unbiased simulator, a value above _t_ [¯] = _Er_ ( _t_ ( _ε_ )) for one draw will tend to be associated
with a value for the next draw that is below _Er_ ( _t_ ( _ε_ )), such that their
average is closer to the true value _t_ [¯] .
The same concept arises when simulators are summed over observations. For example, the simulated log-likelihood function is a sum
over observations of the log of simulated probabilities. If the draws
for each observation’s simulation are independent of the draws for the


_9.3. VARIANCE REDUCTION_ 245


other observations, then the variance of the sum is simply the sum of
the variances. If the draws are taken in a way that creates negative
correlation over observations, then the variance of the sum is lower.
For a given observation, the issue of covariance is related to coverage. By inducing a negative correlation between draws, better coverage
is usually assured. With _R_ = 2, if the two draws are taken independently, then both could end up being at the low side of the distribution.
If negative correlation is induced, then the second draw will tend to
be high if the first draw is low, which provides better coverage.
We describe below methods to attain better coverage for each observation’s integral and to induce negative correlation over the draws
for each observation as well as over observations. We assume for the
sake of discussion that the integral is a choice probability and that the
sum over observations is the simulated log-likelihood function. However, the concepts apply to other integrals, such as scores, and to other
sums, such as moment conditions and market shares. Also, unless otherwise noted, we illustrate the methods with only two random terms
so that the draws can be depicted graphically. The random terms are
labeled _ε_ _[a]_ and _ε_ _[b]_, and collectively as _ε_ = _⟨ε_ _[a]_ _, ε_ _[b]_ _⟩_ _[′]_ . A draw of _ε_ from its
density _f_ ( _ε_ ) is denoted _εr_ = _⟨ε_ _[a]_ _r_ _[, ε][b]_ _r_ _[⟩][′]_ [ for] _[ r]_ [ = 1] _[, . . ., R]_ [. Thus,] _[ ε][a]_ 3 [, e.g.,]
is the third draw of the first random term.


**9.3.1** **Antithetics**


Antithetic draws, suggested by Hammersley and Morton (1956), are
obtained by creating various types of mirror images of a random draw.
For a symmetric density that is centered on zero, the simplest antithetic
variate is created by reversing the sign of all elements of a draw. Figure
9.4 illustrates. Suppose a random draw is taken from _f_ ( _ε_ ) and the
value _ε_ 1 = _⟨ε_ _[a]_ 1 _[, ε][b]_ 1 _[⟩][′]_ [ is obtained. The second “draw”, which is called]
the antithetic of the first draw, is created as _ε_ 2 = _⟨−ε_ _[a]_ 1 _[,][ −][ε][b]_ 1 _[⟩][′]_ [. Each]
draw from _f_ creates a pair of “draws”, the original draw and its mirror
image (mirrored through the origin). To obtain a total of _R_ draws, _R/_ 2
draws are taken independently from _f_ and the other _R/_ 2 are created
as the negative of the original draws.
When the density is not centered on zero, the same concept is
applied but through a different process. For example, the standard
uniform density is between 0 and 1, centered on 0.5. A draw is taken,
labeled _µ_ 1, and its antithetic variate is created as _µ_ 2 = 1 _−_ _µ_ 1. The


246 _CHAPTER 9. DRAWING FROM DENSITIES_


ε [a]


ε

|Col1|εb ε|
|---|---|
||ε1|
|||



Figure 9.4: Reverse sign of both elements.


variate is the same distance from 0.5 as the original draw, but on the
other side of 0.5. In general, for any univariate density with cumulative
function _F_ ( _ε_ ), the antithetic of a draw _ε_ is created as _F_ _[−]_ [1] (1 _−F_ ( _ε_ )). In
the case of a symmetric density centered on zero, this general formula
is equivalent to simply reversing the sign. In the remaining discussion
we assume that the density is symmetric and centered on zero, which
makes the concepts easier to express and visualize.
The correlation between a draw and its antithetic variate is exactly -1, such that the variance of their sum is zero: _V_ ( _ε_ 1 + _ε_ 2) =
_V_ ( _ε_ 1) + _V_ ( _ε_ 2) + 2 _Cov_ ( _ε_ 1 _, ε_ 2) = 0. This fact does not mean that there
is no variance in the simulated probability that is based on these draws.
The simulated probability is a non-linear function of the random terms,
and so the correlation between _P_ ( _ε_ 1) and _P_ ( _ε_ 2) is less than one. The
variance of the simulated probability _P_ [ˇ] = (1 _/_ 2)[ _P_ ( _ε_ 1) + _P_ ( _ε_ 2)] is
greater than zero. However, the variance of the simulated probabilities
is less than (1 _/_ 2) _Vr_ ( _P_ ( _εr_ )), which is the variance with two independent
draws.
As shown in Figure 9.4, reversing the sign of a draw gives evaluation
points in opposite quadrants. The concept can be extended to obtain
draws in each quadrant. A draw is taken and then antithetic draws are
created by reversing the sign of each element alone (leaving the sign
of the other elements unchanged), reversing the sign of each pair of
elements, each triplet of elements, and so on. For _ε_ with two elements,
this process creates three antithetic draws for each independent draw.


_9.3. VARIANCE REDUCTION_ 247


For _ε_ 1 = _⟨ε_ _[a]_ 1 _[, ε][b]_ 1 _[⟩][′]_ [, the antithetic draws are]


_ε_ 2 = _⟨−ε_ _[a]_ 1 _[,]_ _ε_ _[b]_ 1 _[⟩][′]_

_ε_ 3 = _⟨_ _ε_ _[a]_ 1 _[,][ −][ε][b]_ 1 _[⟩][′]_

_ε_ 4 = _⟨−ε_ _[a]_ 1 _[,][ −][ε][b]_ 1 _[⟩][′][.]_


These draws are shown in Figure 9.5. Each quadrant contains a draw.



ε
2


ε
4





ε [a]


|Col1|εb ε|
|---|---|
||1|
||ε|



Figure 9.5: Reverse sign of each element then both.


Better coverage and higher negative correlation can be obtained by
shifting the position of each element as well as reversing their signs. In
Figure 9.5, _ε_ 1 and _ε_ 2 are fairly close together, as are _ε_ 3 and _ε_ 4. This
placement leaves large uncovered areas between _ε_ 1 and _ε_ 3 and between
_ε_ 2 and _ε_ 4. Orthogonal draws with even placement can be obtained
by switching element _ε_ _[a]_ 1 [with] _[ ε]_ 1 _[b]_ [while also reversing the signs. The]
antithetic draws are


_ε_ 2 = _⟨−ε_ _[b]_ 1 _[,]_ _ε_ _[a]_ 1 _[⟩][′]_

_ε_ 3 = _⟨_ _ε_ _[b]_ 1 _[,][ −][ε][a]_ 1 _[⟩][′]_

_ε_ 4 = _⟨−ε_ _[a]_ 1 _[,][ −][ε][b]_ 1 _[⟩][′][,]_


which are illustrated in Figure 9.6. These concepts can, of course, be
extended to any number of dimensions. For _M_ -dimensional _ε_, each
random draw creates 2 _[M]_ antithetic draws (including the original one),
with one in each quadrant.


248 _CHAPTER 9. DRAWING FROM DENSITIES_


ε
2


ε [a]


3


ε
4

|Col1|εb ε|
|---|---|
||1|
||ε|



Figure 9.6: Switch positions and reverse signs.


Comparisons performed by Vijverberg (1997) and S´andor and Andr´as
(2001) show that antithetics substantially improve the estimation of
probit models. Similarly, Geweke (1988) has shown their value when
calculating statistics based on Bayesian posteriors.


**9.3.2** **Systematic sampling**


Coverage can also be improved through systematic sampling (McGrath,
1970), which creates a grid of points over the support of the density
and randomly shifts the entire grid. Consider draws from a uniform
distribution between 0 and 1. If four draws are taken independently,
the points could look like those in the top part of Figure 9.7, which
provide fairly poor coverage. Instead the unit interval is divided into
four segments and draws taken in a way that assures one draw in each
segment with equal distance between the draws. Take a draw from a
uniform between 0 and .25 (by drawing from a standard uniform and
dividing the result by 4.) Label the draw _ε_ 1. Three other draws are
created as


_ε_ 2 = _._ 25 + _ε_ 1

_ε_ 3 = _._ 50 + _ε_ 1

_ε_ 4 = _._ 75 + _ε_ 1


These draws look like those in the bottom part of Figure 9.7, which
provide better coverage than independent draws.


_9.3. VARIANCE REDUCTION_ 249



|0 1<br>Random draws|Col2|Col3|Col4|
|---|---|---|---|
|||||


0



1/4 1/2 3/4 1

Systematic draws







Figure 9.7: Draws from standard uniform.


The issue arises of how finely to segment the interval. For example,
to obtain a total of 100 draws, the unit interval can be divided into 100
segments. A draw between 0 and 0.01 is taken and then the other 99
draws are created from this one draw. Instead, the unit interval can be
divided into fewer than 100 draws and more independent draws taken.
If the interval is divided into four segments, then 25 independent draws
are taken between 0 and 0.25, and three draws in the other segments
are created for each of the independent draws. There is a tradeoff
that the researcher must consider in deciding how fine a grid to use in
systematic sampling. More segments provide more even coverage for a
given total number of draws. However, fewer segments provide more
randomness to the process. In our example with _R_ = 100, there is only
one random draw when 100 segments are used, whereas there are 25
random draws when four segments are used.
The randomness of simulation draws is a necessary component in
the derivation of the asymptotic properties of the simulation-based
estimators, as described in Chapter 10. Many of the asymptotic properties rely on the concept that the number of random draws increases
without bound with sample size. The asymptotic distributions become
relatively accurate only when enough random draws have been taken.
Therefore, for a given total number of draws, the goal of better coverage, which is attained with a more finely defined segmentation, needs
to be traded-off against the goal of having enough randomness for the
asymptotic formulas to apply, which is attained with a more coarsely
defined segmentation. The same issue applies to the antithetics discussed above.
Systematic sampling can be performed in multiple dimensions. Consider a two-dimensional uniform on the unit square. A net is created


250 _CHAPTER 9. DRAWING FROM DENSITIES_


by dividing each dimension into segments. As shown in Figure 9.8,
when each dimension is divided into four segments, the unit square is
partitioned into 16 areas. A draw between 0 and .25 is taken for each
element, giving _ε_ 1 = _⟨ε_ _[a]_ 1 _[, ε][b]_ 1 _[⟩][′]_ [, where 0] _[ < ε][a]_ 1 _[<]_ [ 0] _[.]_ [25 and 0] _[ < ε]_ 1 _[b]_ _[<]_ [ 0] _[.]_ [25.]
This draw falls somewhere in the bottom-left area in Figure 9.8. Fifteen other draws are then created as the “origin” of each area plus
_⟨ε_ _[a]_ 1 _[, ε][b]_ 1 _[⟩][′]_ [. For example, the point that is created for the bottom-right]
area is _ε_ 4 = _⟨_ (0 _._ 75 + _ε_ _[a]_ 1 [)] _[,]_ [ (0 +] _[ ε][b]_ 1 [)] _[⟩][′]_ [.]



3/4


1/2


1/4



|ε<br>13|ε<br>14|ε<br>15|ε<br>16|
|---|---|---|---|
|ε9|ε10|ε11|ε12|
|ε5|ε6|ε7|ε8|
|ε1|ε2|ε3|ε4|


1/4 1/2 3/4



Figure 9.8: Systematic draws in two dimensions.


These draws are defined for a uniform distribution. When _f_ represents another density, the points are transformed using the method
described in section (9.2.3). In particular, let _F_ be the cumulative distribution associated with univariate density _f_ . Systematic draws from
_f_ are created by transforming each systematic draw from a uniform
by _F_ _[−]_ [1] . For example, for a standard normal, four equal-sized segments of the density are created with breakpoints: Φ _[−]_ [1] (0 _._ 25) = _−._ 67,
Φ _[−]_ [1] (0 _._ 5) = 0, and Φ _[−]_ [1] (0 _._ 75) = _._ 67. As shown in Figure 9.9, these segments are equal-sized in the sense that each contains the same mass.
The draws for the standard normal are created by taking a draw from
a uniform between 0 and 0.25, labeled _µ_ 1. The corresponding point
on the normal is _ε_ 1 = Φ _[−]_ [1] ( _µ_ 1), which falls in the first segment. The
points for the other three segments are created as: _ε_ 2 = Φ _[−]_ [1] (0 _._ 25+ _µ_ 1),
_ε_ 3 = Φ _[−]_ [1] (0 _._ 5 + _µ_ 1), and _ε_ 4 = Φ _[−]_ [1] (0 _._ 75 + _µ_ 1).
Draws of multi-dimensional random terms are obtained similarly,


_9.3. VARIANCE REDUCTION_ 251


Figure 9.9: Systematic draws for univariate normal.


provided that the elements are independent. For example, if _ε_ consists
of two elements each of which is standard normal, then draws analogous
to those in Figure 9.8 are obtained as follows: Draw _µ_ _[a]_ 1 [and] _[ µ]_ 1 _[b]_ [from]
a uniform between 0 and 0.25. Calculate _ε_ 1 as _⟨_ Φ _[−]_ [1] ( _µ_ _[a]_ 1 [)] _[,]_ [ Φ] _[−]_ [1][(] _[µ][b]_ 1 [)] _[⟩][′]_ [.]
Calculate the other 15 points as _εr_ as _⟨_ Φ _[−]_ [1] ( _xr_ + _µ_ _[a]_ 1 [)] _[,]_ [ Φ] _[−]_ [1][(] _[y][r]_ [ +] _[ µ][b]_ 1 [)] _[⟩][′]_ [,]
where _⟨xr, yr⟩_ _[′]_ is the origin of area _r_ in the unit square.
The requirement that the elements of _ε_ be independent is not restrictive. Correlated random elements are created through transformations of independent elements, such as the Choleski transformation.
The independent elements are drawn from their density and then the
correlation is created inside the model.

Obviously, numerous sets of systemtically sampled draws can be
obtained to gain more randomization. In two dimensions with four
segments in each dimension, 64 draws are obtained by taking 4 independent draws in the 0 to 1/4 square and creating 15 other draws from
each. This procedure provides greater randomization but less fine coverage than defining the draws in terms of 8 segments in each dimension
such that each random draw in the 0 to 1/8 square translates into 64
systematic draws.

The draws for the normal distribution that are created as just described are not symmetric around zero. An alternative approach can
be used to assure such symmetry. For a uni-dimensional normal, 4
draws that are symmetric around zero are obtained as follows. Draw
a uniform between 0 and 0.25, labeled _µ_ 1. Create the draw from the
normal as _ε_ 1 = Φ _[−]_ [1] ( _µ_ 1). Create the draw for the second segment as
_ε_ 2 = Φ _[−]_ [1] (0 _._ 25 + _µ_ 1). Then create the draws for the third and fourth
segments as the negative of these draws: _ε_ 3 = _−ε_ 2 and _ε_ 4 = _−ε_ 1. Fig


![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/train_textbook_chunks/markdown/train_textbook_chunk11_p251-275_images/train_textbook_chunk11_p251-275.pdf-10-0.png)
252 _CHAPTER 9. DRAWING FROM DENSITIES_


ure 9.10 illustrates the draws using the same _µ_ 1 as for Figure 9.9. This
procedure combines systematic sampling with antithetics. It can be
extended to multiple dimensions by creating systematic draws for the
positive quadrant and then creating antithetic variates for the other
quadrants.


1 2 3 4
_ 0.67 0 0.67


Figure 9.10: Symmetric systematic draws.


**9.3.3** **Halton sequences**



![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/train_textbook_chunks/markdown/train_textbook_chunk11_p251-275_images/train_textbook_chunk11_p251-275.pdf-11-0.png)

Halton sequences (Halton, 1960) provide coverage and, unlike the other
methods we have discussed, induce a negative correlation over observations. A Halton sequence is defined in terms of a given number,
usually a prime. The sequence is most easily understood though an
example. Consider the prime 3. The Halton sequence for 3 is created by dividing the unit interval into three parts with breaks at [1]

3
and [2]

3 [, as shown in the top panel of Figure 9.11. The first terms in]
the sequence are these breakpoints: 1 [2]
3 _[,]_ 3 [. Then each of the three seg-]



the sequence are these breakpoints:
3 _[,]_ 3 [. Then each of the three seg-]

ments is divided into thirds, and the breakpoints for these segments
are added to the sequences in a particular way. The sequence becomes: [1] [2] [1] [4] [7] [2] [5] [8]

3 _[,]_ 3 _[,]_ 9 _[,]_ 9 _[,]_ 9 _[,]_ 9 _[,]_ 9 _[,]_ 9 [Note that the lower breakpoints in all three]

segments ( [1] [4] [7]

9 _[,]_ 9 _[,]_ 9 [) are entered in the sequence before the higher break-]

points ( [2] [5] [8]

9 _[,]_ 9 _[,]_ 9 [.) Then each of the 9 segments is divided into thirds,]

with the breakpoints added to the sequences. The sequence becomes:
1 [2] [1] [4] [7] [2] [5] [8] [1] [10] [19] [4] [13]
3 _[,]_ 3 _[,]_ 9 _[,]_ 9 _[,]_ 9 _[,]_ 9 _[,]_ 9 _[,]_ 9 _[,]_ 27 _[,]_ 27 _[,]_ 27 _[,]_ 27 _[,]_ 27 [, and so on. This process is contin-]




[1] [2]

3 _[,]_ 3




[2] [1]

3 _[,]_ 9




[1] [4]

9 _[,]_ 9




[2] [5]

9 _[,]_ 9




[5] [8]

9 _[,]_ 9




[1] [4]

9 _[,]_ 9

[5] [8]

9 _[,]_ 9




[4] [7]

9 _[,]_ 9




[7] [2]

9 _[,]_ 9




[2] [5]

9 _[,]_ 9




[4] [7]

9 _[,]_ 9




[2] [1]

3 _[,]_ 9




[1] [4]

9 _[,]_ 9




[4] [7]

9 _[,]_ 9




[7] [2]

9 _[,]_ 9




[2] [5]

9 _[,]_ 9




[5] [8]

9 _[,]_ 9




[8] [1]

9 _[,]_




[1] [10]

27 _[,]_ 27




[10] [19]

27 _[,]_ 27




[19] [4]

27 _[,]_




[4] [13]

27 _[,]_ 27



3 _[,]_ 3 _[,]_ 9 _[,]_ 9 _[,]_ 9 _[,]_ 9 _[,]_ 9 _[,]_ 9 _[,]_ 27 _[,]_ 27 _[,]_ 27 _[,]_ 27 _[,]_ 27 [, and so on. This process is contin-]

ued for as many points as the researcher wants to obtain.
From a programming perspective, it is easy to create a Halton
sequence. The sequence is created iteratively. At each iteration _t_, the
sequence is denoted _s_ _[t]_, which is a series of numbers. The sequence is


_9.3. VARIANCE REDUCTION_ 253



_a_



_b_







|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|1/3<br>2/3<br>_a_<br>_e_<br>_b_<br>_c_<br>_d_|1/3<br>2/3<br>_a_<br>_e_<br>_b_<br>_c_<br>_d_|1/3<br>2/3<br>_a_<br>_e_<br>_b_<br>_c_<br>_d_|1/3<br>2/3<br>_a_<br>_e_<br>_b_<br>_c_<br>_d_|1/3<br>2/3<br>_a_<br>_e_<br>_b_<br>_c_<br>_d_|1/3<br>2/3<br>_a_<br>_e_<br>_b_<br>_c_<br>_d_|1/3<br>2/3<br>_a_<br>_e_<br>_b_<br>_c_<br>_d_|1/3<br>2/3<br>_a_<br>_e_<br>_b_<br>_c_<br>_d_|1/3<br>2/3<br>_a_<br>_e_<br>_b_<br>_c_<br>_d_|
|1/9<br>4/9<br>7/9<br>_a_<br>_b_<br>_e_<br>_c_<br>_d_<br>_h_<br>_f_<br>_g_|1/9<br>4/9<br>7/9<br>_a_<br>_b_<br>_e_<br>_c_<br>_d_<br>_h_<br>_f_<br>_g_|1/9<br>4/9<br>7/9<br>_a_<br>_b_<br>_e_<br>_c_<br>_d_<br>_h_<br>_f_<br>_g_|1/9<br>4/9<br>7/9<br>_a_<br>_b_<br>_e_<br>_c_<br>_d_<br>_h_<br>_f_<br>_g_|1/9<br>4/9<br>7/9<br>_a_<br>_b_<br>_e_<br>_c_<br>_d_<br>_h_<br>_f_<br>_g_|1/9<br>4/9<br>7/9<br>_a_<br>_b_<br>_e_<br>_c_<br>_d_<br>_h_<br>_f_<br>_g_|1/9<br>4/9<br>7/9<br>_a_<br>_b_<br>_e_<br>_c_<br>_d_<br>_h_<br>_f_<br>_g_|1/9<br>4/9<br>7/9<br>_a_<br>_b_<br>_e_<br>_c_<br>_d_<br>_h_<br>_f_<br>_g_|1/9<br>4/9<br>7/9<br>_a_<br>_b_<br>_e_<br>_c_<br>_d_<br>_h_<br>_f_<br>_g_|
||||||||||


2/9 5/9 8/9



Figure 9.11: Halton sequence for prime 3.



extended in each iteration with the new sequence being _st_ +1 = _{st, st_ +
1 _/_ 3 _[t]_ _, st_ + 2 _/_ 3 _[t]_ _}_ . Start with 0 as the initial sequence: _s_ 0 = _{_ 0 _}_ . The
number zero is not actually part of a Halton sequence, but considering
to be the first element facilitates creation of the sequence, as we will
see. It can be dropped after the entire sequence is created. In the first
iteration, add 1 _/_ 3 [1] (= [1] [2]

3 [) and then 2] _[/]_ [3][1][ (=] 3 [) to this sequence and]

append the results, to get _{_ 0 _,_ [1] _[,]_ [2] _[}]_ [. The sequence has three elements.]




[1] [2]

3 [) and then 2] _[/]_ [3][1][ (=] 3




[1] [2]

3 _[,]_ 3




[1] [2]

9 [) and then 2] _[/]_ [3][2][ (=] 9



append the results, to get _{_ 0 _,_

3 _[,]_ 3 _[}]_ [. The sequence has three elements.]

In the second iteration, add 1 _/_ 3 [2] (= [1] [2]

9 [) and then 2] _[/]_ [3][2][ (=] 9 [) to each]

element of the sequence and append the results:



0 0
1 _/_ 3 1 _/_ 3
2 _/_ 3 1 _/_ 3
0 + 1 _/_ 9 1 _/_ 9
1 _/_ 3 + 1 _/_ 9 = 4 _/_ 9
2 _/_ 3 + 1 _/_ 9 7 _/_ 9
0 + 2 _/_ 9 2 _/_ 9
1 _/_ 3 + 2 _/_ 9 5 _/_ 9
2 _/_ 3 + 2 _/_ 9 7 _/_ 9


The new sequence consists of nine elements.


254 _CHAPTER 9. DRAWING FROM DENSITIES_


In the third iteration, add 1 _/_ 3 [3] (= 1 1
27 [) and then 2] _[/]_ [3][3][ (=] 27 [) to]
each element of this sequence and append the results:


0 0
1 _/_ 3 1 _/_ 3
2 _/_ 3 2 _/_ 3
1 _/_ 9 1 _/_ 9
4 _/_ 9 4 _/_ 9
7 _/_ 9 7 _/_ 9
2 _/_ 9 2 _/_ 9
5 _/_ 9 5 _/_ 9
8 _/_ 9 8 _/_ 9
0 + 1 _/_ 27 = 1 _/_ 27
1 _/_ 3 + 1 _/_ 27 10 _/_ 27
2 _/_ 3 + 1 _/_ 27 19 _/_ 27
1 _/_ 9 + 1 _/_ 27 4 _/_ 27
4 _/_ 9 + 1 _/_ 27 13 _/_ 27
7 _/_ 9 + 1 _/_ 27 22 _/_ 27
2 _/_ 9 + 1 _/_ 27 7 _/_ 27
5 _/_ 9 + 1 _/_ 27 16 _/_ 27
8 _/_ 9 + 1 _/_ 27 25 _/_ 27
0 + 2 _/_ 27 2 _/_ 27
1 _/_ 3 + 2 _/_ 27 11 _/_ 27
2 _/_ 3 + 2 _/_ 27 20 _/_ 27
1 _/_ 9 + 2 _/_ 27 5 _/_ 27
4 _/_ 9 + 2 _/_ 27 14 _/_ 27
7 _/_ 9 + 2 _/_ 27 23 _/_ 27
2 _/_ 9 + 2 _/_ 27 8 _/_ 27
5 _/_ 9 + 2 _/_ 27 17 _/_ 27
8 _/_ 9 + 2 _/_ 27 26 _/_ 27



The sequence now consists of 27 elements. In the fourth iteration, add
1 _/_ 3 [4] (= [1] [2]

81 [) and then 2] _[/]_ [3][4][ (=] 81 [) to each element of the sequence and]

append the results. And so on.


Note that the sequence cycles over the unit interval every 3 num

_9.3. VARIANCE REDUCTION_ 255


bers:


0 1 _/_ 3 2 _/_ 3
1 _/_ 9 4 _/_ 9 7 _/_ 9
2 _/_ 9 5 _/_ 9 8 _/_ 9
1 _/_ 27 10 _/_ 27 19 _/_ 27
4 _/_ 27 13 _/_ 27 22 _/_ 27
7 _/_ 27 16 _/_ 27 25 _/_ 27
2 _/_ 27 11 _/_ 27 20 _/_ 27
5 _/_ 27 14 _/_ 27 23 _/_ 27
8 _/_ 27 17 _/_ 27 26 _/_ 27


Within each cycle the numbers are ascending.



Halton sequences for other prime numbers are created similarly.
The sequence for 2 is _{_ [1] [1] [3] [1] [5] [3] [7] [1] [9]

2 _[,]_ 4 _[,]_ 4 _[,]_ 8 _[,]_ 8 _[,]_ 8 _[,]_ 8 _[,]_ 16 _[,]_ 16 _[. . . .]_ [ In general, the se-]

quence for prime _k_ is created iteratively, with the sequence at iteration
_t_ + 1 being _st_ +1 = _{st, st_ + 1 _/k_ _[t]_ _, st_ + 2 _/k_ _[t]_ _, . . ., st_ + ( _k −_ 1) _/k_ _[t]_ _}_ . The
sequence contains cycles of length _k_, where each cycle consists of _k_
ascending points on the unit interval equidistant from each other.




[1] [1]

2 _[,]_ 4




[1] [3]

4 _[,]_ 4




[3] [1]

4 _[,]_ 8




[1] [5]

8 _[,]_ 8




[5] [3]

8 _[,]_ 8




[3] [7]

8 _[,]_ 8




[7] [1]

8 _[,]_




[1] [9]

16 _[,]_



Since a Halton sequence is defined on the unit interval, its elements
can be considered as well-placed “draws” from a standard uniform
density. The Halton draws provide better coverage than random draws,
on average, because they are created to progressively fill-in the unit
interval evenly and evermore densely. The elements in each cycle are
equidistant apart, and each cycle covers the unit interval in the areas
not covered by previous cycles.


When using Halton draws for a sample of observations, one long
Halton sequence is usually created and then part of the sequence is used
for each observation. The initial elements of the sequence are discarded
for reasons we will discuss. The remaining elements are then used in
groups, with each group of elements constituting the “draws” for one
observation. For example, suppose there are two observations, and the
researcher wants _R_ = 5 draws for each. If the prime 3 is used, and the
researcher decides to discard the first 10 elements, then a sequence of


256 _CHAPTER 9. DRAWING FROM DENSITIES_


length 20 is created. This sequence is:


0 1 _/_ 3 2 _/_ 3
1 _/_ 9 4 _/_ 9 7 _/_ 9
2 _/_ 9 5 _/_ 9 8 _/_ 9
1 _/_ 27 10 _/_ 27 19 _/_ 27
4 _/_ 27 13 _/_ 27 22 _/_ 27
7 _/_ 27 16 _/_ 27 25 _/_ 27
2 _/_ 27 11 _/_ 27 _._



After eliminating the first 10 elements, the Halton draws for the first
observation are _{_ [10] _[,]_ [19] _[,]_ [4] _[,]_ [13] _[,]_ [22] _[}]_ [ and the Halton draws for the second]




[10] [19]

27 _[,]_ 27

[7] [16]

27 _[,]_ 27




[19] [4]

27 _[,]_




[4] [13]

27 _[,]_ 27

[25] [2]

27 _[,]_ 27



observation are _{_

27 _[,]_ 27 _[,]_ 27 _[,]_ 27 _[,]_ 27 _[}]_ [ and the Halton draws for the second]

observation are _{_ [7] _[,]_ [16] _[,]_ [25] _[,]_ [2] _[,]_ [11] _[}]_ [. These draws are illustrated in Fig-]




[16] [25]

27 _[,]_ 27




[13] [22]

27 _[,]_ 27

[2] [11]

27 _[,]_ 27



observation are _{_

27 _[,]_ 27 _[,]_ 27 _[,]_ 27 _[,]_ 27 _[}]_ [. These draws are illustrated in Fig-]

ure 9.12. Note that the gaps in coverage for the first observation are



1 [st] observation


2 [nd] observation

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|10/27<br>13/27<br>19/27<br>22/27<br>4/27|10/27<br>13/27<br>19/27<br>22/27<br>4/27|10/27<br>13/27<br>19/27<br>22/27<br>4/27|10/27<br>13/27<br>19/27<br>22/27<br>4/27|10/27<br>13/27<br>19/27<br>22/27<br>4/27|10/27<br>13/27<br>19/27<br>22/27<br>4/27|10/27<br>13/27<br>19/27<br>22/27<br>4/27|10/27<br>13/27<br>19/27<br>22/27<br>4/27|10/27<br>13/27<br>19/27<br>22/27<br>4/27|10/27<br>13/27<br>19/27<br>22/27<br>4/27|10/27<br>13/27<br>19/27<br>22/27<br>4/27|
||||||||||||



Figure 9.12: Halton draws for two observations.



filled by the draws for the second observation. For example, the large
gap between 4 [10]
27 [and] 27 [for the first observation is filled in by the mid-]



gap between
27 [and] 27 [for the first observation is filled in by the mid-]

point of this gap, 7 [13]
27 [, for the second observation. The gap between] 27

and [19] [16]

27 [is filled in by its midpoint,] 27 [, for the second observation. And]

so on. The pattern by which Halton sequences are created make it such
that each subsequence fills in the gaps of the previous subsequences.
Because of this filling-in property, simulated probabilities based
on Halton draws tend to be self-correcting over observations. The
draws for one observation tend to be negatively correlated with those
for the previous observation. In our example, the average of the first
observation’s draws is above 0.5 while the average of the draws for
the second observation is below 0.5. This negative correlation reduces
error in the simulated log-likelihood function.
When the number of draws used for each observation rises, the coverage for each observation improves. The negative covariance across




[19] [16]

27 [is filled in by its midpoint,] 27


_9.3. VARIANCE REDUCTION_ 257


observations diminishes, since there are fewer gaps in each observation’s coverage to be filled in by the next observation. The selfcorrecting aspect of Halton draws over observations is greatest when
few draws are used for each observation such that the correction is
most needed. However, accuracy improves with more Halton draws
since coverage is better for each observation.
As described so far, the Halton draws are for a uniform density. To
obtain a sequence of points for other univariate densities, the inverse
cumulative distribution is evaluated at each element of the Halton
sequence. For example, suppose the researcher wants draws from a
standard normal density. A Halton sequence is created for, say, prime
3 and the inverse cumulative normal is taken for each element. The
resulting sequence is:


Φ _[−]_ [1] (1 _/_ 3) _−._ 43
Φ _[−]_ [1] (2 _/_ 3) _._ 43
Φ _[−]_ [1] (1 _/_ 9) = _−_ 1 _._ 2
Φ _[−]_ [1] (4 _/_ 9) _−._ 14
Φ _[−]_ [1] (7 _/_ 9) _._ 76
_. . . ._


This sequence is depicted in Figure 9.13. It can be considered the same
as for the unit interval, as dividing the density into three segments of
equal mass, with breakpoints at -.43 and +.43, and then dividing each
segment into three subsegments of equal mass, and so on.


Figure 9.13: Halton draws for a standard normal.



![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/train_textbook_chunks/markdown/train_textbook_chunk11_p251-275_images/train_textbook_chunk11_p251-275.pdf-16-0.png)
258 _CHAPTER 9. DRAWING FROM DENSITIES_


Halton sequences in multiple dimensions are obtained by creating
a Halton sequence for each dimension with a different prime for each
dimension. For example, a sequence in two dimensions is obtained by
creating pairs from the Halton sequence for primes 2 and 3. The points
are


_ε_ 1 = _⟨_ [1] 2 _[,]_ 13 _[⟩]_


_ε_ 2 = _⟨_ [1] 4 _[,]_ 23 _[⟩]_


_ε_ 3 = _⟨_ [3] 4 _[,]_ 19 _[⟩]_


_ε_ 4 = _⟨_ [1] 8 _[,]_ 49 _[⟩]_


_ε_ 5 = _⟨_ [5] 8 _[,]_ 79 _[⟩]_


_ε_ 6 = _⟨_ [3] 8 _[,]_ 29 _[⟩]_

_. . ._


This sequence is depicted in Figure 9.14. To obtain draws for a two


ε
5



2/3


1/3



ε
2



ε
4



ε
1

ε
6


1/2



ε
3



Figure 9.14: Halton sequence in two dimensions for primes 2 and 3.


dimensional independent standard normal, the inverse cumulative nor

_9.3. VARIANCE REDUCTION_ 259


mal is taken of each element of these pairs. The draws are


_ε_ 1 = _⟨_ 0 _,_ _−._ 43 _⟩_
_ε_ 2 = _⟨_ _−._ 67 _,_ _._ 43 _⟩_
_ε_ 3 = _⟨_ _._ 67 _,_ _−_ 1 _._ 2 _⟩_
_ε_ 4 = _⟨_ _−_ 1 _._ 15 _,_ _−._ 14 _⟩_
_ε_ 5 = _⟨_ _._ 32 _,_ _._ 76 _⟩_
_ε_ 6 = _⟨_ _−._ 32 _,_ _−._ 76 _⟩_
_. . ._


which are shown in Figure 9.15.


ε _[b]_


ε
5



![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/train_textbook_chunks/markdown/train_textbook_chunk11_p251-275_images/train_textbook_chunk11_p251-275.pdf-18-0.png)



ε _[a]_





ε
1





ε
3


Figure 9.15: Halton sequence for 2-dimensional standard normal.



When creating sequences in several dimensions, it is customary
to eliminate the initial part of the series. The initial terms of two
Halton sequences are highly correlated, through at least the first cycle
of each sequence. For example, the sequences for 7 and 11 begin with
_{_ [1] _[,]_ [2] _[,]_ [3] _[,]_ [4] _[,]_ [5] _[,]_ [6] _[}]_ [ and] _[ {]_ [1] _[,]_ [2] _[,]_ [3] _[,]_ [4] _[,]_ [5] _[,]_ [6] _[. . .][}]_ [. These first elements fall]




[1] [2]

7 _[,]_ 7




[2] [3]

7 _[,]_ 7




[3] [4]

7 _[,]_ 7




[4] [5]

7 _[,]_ 7




[5] [6]

7 _[,]_ 7




[6] [1]

7 _[}]_ [ and] _[ {]_




[1] [2]

11 _[,]_




[2] [3]

11 _[,]_




[3] [4]

11 _[,]_




[4] [5]

11 _[,]_ 11




[5] [6]

11 _[,]_



_{_

7 _[,]_ 7 _[,]_ 7 _[,]_ 7 _[,]_ 7 _[,]_ 7 _[}]_ [ and] _[ {]_ 11 _[,]_ 11 _[,]_ 11 _[,]_ 11 _[,]_ 11 _[,]_ 11 _[. . .][}]_ [. These first elements fall]

in a line in two dimensions, as shown in Figure 9.16. The correlation
dissipates after each sequence has cycled through the unit interval since
sequences with different primes cycle at different rates. Discarding the
initial part of the sequence eliminates the correlated portion. The


260 _CHAPTER 9. DRAWING FROM DENSITIES_


number of initial elements to discard needs to be at least as large as
the largest prime that is used in creating the sequences.


Figure 9.16: First six elements of Halton sequence for primes 7 and 11.


The potential for correlation is the reason that prime numbers are
used to create the Halton sequences instead of non-primes. If a nonprime is used, then there is a possibility that the cycles will coincide
throughout the entire sequence, rather than for just the initial elements. For example, if Halton sequences are created for 3 and 6, the
sequence for 3 cycles twice for every one cycle of the sequence for 6.
Since the elements within a cycle are ascending, the elements in each
cycle of the sequence for 3 are correlated with the elements in the
cycle of the sequence for 6. Using only prime numbers avoids this
overlapping of cycles.
The superior coverage and the negative correlation over observations that are obtained with Halton draws combine to make Halton
draws far more effective than random draws for simulation. Spanier
and Maize (1991) have shown that a small number of Halton draws provide relatively good integration. In the context of discrete choice models, Bhat (2001) found that 100 Halton draws provided more precise
results for his mixed logit than 1000 random draws. In fact, the simulation error with 125 Halton draws was half as large as with 1000 random
draws and somewhat smaller than with 2000 random draws. Train
(2000), Munizaga and Alvarez-Daziano (2001), and Hensher (2001)



![](/Users/nicholasvreugdenhil/ASU Dropbox/Nicholas Vreugdenhil/masters_io_2026/external/train_textbook_chunks/markdown/train_textbook_chunk11_p251-275_images/train_textbook_chunk11_p251-275.pdf-19-0.png)
_9.3. VARIANCE REDUCTION_ 261


confirm these results on other datasets.

As illustration, consider the mixed logit model that is described
extensively in Chapter 11. Briefly, the model is for household’s choice
of electricity supplier. In a stated preference survey, respondents were
presented with a series of hypothetical choice situations. In each situation, four energy suppliers were described and the respondent was
asked which company he/she would choose. The suppliers were differentiated on the basis of their price, whether the company required
the customer to sign a long-term contract, whether the supplier was
the local energy utility, whether the supplier was a well-known company, and whether the supplier offered time-of-day (TOD) or seasonal
rates. A mixed logit model was estimated with these six characteristics as explanatory variables. The coefficient of each variable was
assumed to be normally distributed, except for the price coefficient
which was assumed to be fixed. The model therefore contained five
random terms for simulation. A complete description of the data, the
estimated model, and its implications are given in Chapter 11, where
the content of the model is relevant to the topic of that chapter. For
now, we are concerned only with the issue of Halton draws compared
to random draws.

To investigate this issue, the model was estimated with 1000 random draws and then with 100 Halton draws. More specifically, the
model was estimated five times using five different sets of 1000 random draws. The mean and standard deviation of the estimated parameters from these five runs were calculated. The model was then
estimated five times with Halton sequences. The first model used the
primes 2,3,5,7,11 for the five dimensions of simulation. The order of the
primes was switched for the other models, such that the dimension for
which each prime was used changed in the five runs. The average and
standard deviation of the five sets of estimated were then calculated.

The means of the parameter estimates over the five runs are given
in Table 9.1. The mean for the runs based on random draws are given
in the first column, and the means for the runs based on Halton draws
are given in the second column. The two sets of means are very similar.
This result indicates that the Halton draws provide the same estimates,
_on average_, as random draws.

The standard deviations of the parameter estimates are given in
Table 9.2. For all but one of the 11 parameters, the standard deviations
are lower with 100 Halton draws than with 1000 random draws. For


262 _CHAPTER 9. DRAWING FROM DENSITIES_


Table 9.1: Means of Parameter Estimates

1000 random draws 100 Halton draws
Price -0.8607 -0.8588
Contract length
Mean -0.1955 -0.1965
Std. Dev. 0.3092 0.3158
Local utility
Mean 2.0967 2.1142
Std. Dev. 1.0535 1.0236
Known company
Mean 1.4310 1.4419
Std. Dev. 0.8208 0.6894
TOD rates
Mean -8.3760 -8.4149
Std. Dev. 2.4647 2.5466
Seasonal rates
Mean -8.6286 -8.6381
Std. Dev. 1.8492 1.8977


8 of the parameters, the standard deviations are half as large. Given
that both sets of draws give essentially the same means, the lower
standard deviations with the Halton draws indicates that a researcher
can expect to be closer to the expected values of the estimates using
100 Halton draws than 1000 random draws.


These results show the value of Halton draws. Computer time can
be reduced by a factor of ten by using Halton draws in lieu of random
draws, without reducing, and in fact increasing, accuracy.


These results need to be viewed with caution, however. The use
of Halton draws and other quasi-random numbers in simulation-based
estimation is fairly new and not completely understood. For example,
an anomaly arose in the analysis that serves as a helpful warning. The
model was re-estimated with 125 Halton draws instead of 100. It was
estimated five times under each of the five orderings of the prime numbers as described above. Four of the five runs provided very similar
estimates. However, the fifth run gave estimates that were noticeably
different from the others. For example, the estimated price coefficient
for the first four runs was -0.862, -0.865, -0.863, and -0.864, respectively, while the fifth gave -0.911. The standard deviations over the five


_9.3. VARIANCE REDUCTION_ 263


Table 9.2: Standard deviations of Parameter Estimates

1000 random draws 100 Halton draws
Price 0.0310 0.0169
Contract length
Mean 0.0093 0.0045
Std. Dev. 0.0222 0.0108
Local utility
Mean 0.0844 0.0361
Std. Dev. 0.1584 0.1180
Known company
Mean 0.0580 0.0242
Std. Dev. 0.0738 0.1753
TOD rates
Mean 0.3372 0.1650
Std. Dev. 0.1578 0.0696
Seasonal rates
Mean 0.4134 0.1789
Std. Dev. 0.2418 0.0679


sets of estimates were lower than with 1000 random draws, confirming
the value of the Halton draws. However, the standard deviations were
greater with 125 Halton draws than with 100 Halton draws, due to the
last run with 125 draws providing such different results. The reason
for this anomaly has not been determined. Its occurrence indicates the
need for further investigation of the properties of Halton sequences in
simulation-based estimation.


**9.3.4** **Randomized Halton draws**


Halton sequences are systematic rather than random. However, the
asymptotic properties of simulation-based estimators are derived under
the concept that the draws are random. There are two ways that
this issue can be addressed. First, one can realize that draws from
a random number generator are not actually random either. They
are systematic, like anything done by a computer. A random number
generator creates draws that have the characteristics of truly random
draws, but the fact that they are systematic is why they are called
“pseudo-random draws.” In this regard, therefore, Halton draws can
be seen as a systematic way of approximating integration that is more


264 _CHAPTER 9. DRAWING FROM DENSITIES_


precise than using pseudo-random draws, which are also systematic.
Neither matches the theoretical concept of randomness, and, in fact,
it is not clear that the theoretical concept actually has a real-world
counterpart. Both meet the basic underlying goal of approximating an
integral over a density.
Second, Halton sequences can be transformed in a way that makes
them random, at least in the same way that pseudo-random numbers
are random. Bhat (forthcoming) describes the process, based on procedures introduced by Tuffin (1996):


1. Take a draw from a standard uniform density. Label this random
draw as _µ_ .


2. Add _µ_ to each element of the Halton sequence. If the resulting
element exceeds one, subtract 1 from it. Otherwise, keep the
resulting element as is (without subtracting 1).


The formula for this transformation is _sn_ = _mod_ ( _so_ + _µ_ ), where _so_
is the original element of the Halton sequence, _sn_ is the transformed
element, and _mod_ takes the fractional part of the term in parentheses.
The transformation is depicted in Figure 9.17. Suppose the draw of
_µ_ from the uniform density is 0.40. The number .33 is the first element
of the Halton sequence for prime 3. This element is transformed, as
shown in the top panel, to _._ 33 + _._ 40 = _._ 73, which is just a .40 move
up the line. The number .67 is the second element of the sequence.
It is transformed by adding .4 and then, since the result exceeds 1,
by subtracting 1 to get 0.07. ( _._ 67 + _._ 40 _−_ 1 = _._ 07). As shown in the
bottom panel, this transformation is visualized as moving the original
point up by a distance of .40, but wrapping around when the end of
the unit interval is reached. The point moves up .33 to where the line
ends, and then wraps to the start of the line and continues to move up
another .07, for a total movement of .40.
Figure 9.18 depicts the transformation for the first five elements
of the sequence. The relation between the points and the degree of
coverage are the same before and after the transformation. However,
since the transformation is based on the random draw of _µ_, the numerical values of the transformed sequence are random. The resulting
sequence is called a randomized Halton sequence. It has the same
properties of coverage and negative correlation over observations as
the original Halton draws, since the relative placement of the elements
are the same; however, it is now random.


_9.3. VARIANCE REDUCTION_ 265


Figure 9.17: Random transformation of Halton draws with _µ_ = 0 _._ 40.


Original
sequence


Transformed
sequence


Figure 9.18: Randomization of Halton sequence in one dimension.


With multiple dimensions, the sequence used for each dimension is
transformed separately based on its own draw from the standard uniform density. Figure 9.19 represents a transformation of a 2-dimensional
sequence of length 3 defined in primes 2 and 3. The sequence in prime
3 is given by the x-axis and obtains a random draw of 0.40. The sequence for prime 2 obtains a draw of 0.35. Each point in the original
2-dimensional sequence is moved to the left by .40 and up by .35, wrapping as needed. The relation between the points in each dimension is
maintained, and yet the sequence is now random.


**9.3.5** **Scrambled Halton draws**


Another issue with Halton draws arises when they are used in high
dimensions. For simulation of high-dimensional integrals, Halton sequences based on large primes are necessary. For example, with 15
dimensions, the primes up to 47 are needed. However, Halton draws
defined by large primes can be highly correlated with each other over
large portions of the sequence. The correlation is not confined to the
initial elements as described above, and so cannot be eliminated by


